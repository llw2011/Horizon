"""Twitter scraper using X/Twitter internal GraphQL API directly."""

import asyncio
import json
import logging
import os
import re
import time
from datetime import datetime, timezone
from html import unescape
from typing import Dict, List, Optional

import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, TwitterConfig

logger = logging.getLogger(__name__)

# ---------- GraphQL endpoint constants ----------

# X changes queryIds on every frontend deploy.  We resolve them
# dynamically by scraping the main JS bundle from abs.twimg.com.
# Fallback values (will be overwritten on first successful resolve):
_FALLBACK_QUERY_IDS: Dict[str, str] = {
    "UserByScreenName": "IGgvgiOx4QZndDHuD3x9TQ",
    "UserTweets": "lrMzG9qPQHpqJdP3AbM-bQ",
    "TweetDetail": "_i0BBmP_dK_ZLFa2Y-ei9Q",
}

# SearchAdaptive — used for fetching replies (conversation_id search)
_SEARCH_ADAPTIVE_URL = "https://x.com/i/api/2/search/adaptive.json"

# Regex to extract queryId + operationName from X's JS bundles.
_QID_RE = re.compile(
    r'queryId:"([a-zA-Z0-9_-]{15,30})",operationName:"(\w+)"'
)

# Feature flags required by the UserTweets endpoint.
# These are the standard set as of 2025. If the API starts returning
# "Missing feature flags" type errors, capture the updated set from
# a browser network request.
_TWEET_FEATURES = {
    "rweb_tipjar_consumption_enabled": True,
    "responsive_web_graphql_exclude_directive_enabled": True,
    "verified_phone_label_enabled": False,
    "creator_subscriptions_tweet_preview_api_enabled": True,
    "responsive_web_graphql_timeline_navigation_enabled": True,
    "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
    "communities_web_enable_tweet_community_results_fetch": True,
    "c9s_tweet_anatomy_moderator_badge_enabled": True,
    "articles_preview_enabled": True,
    "responsive_web_edit_tweet_api_enabled": True,
    "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
    "view_counts_everywhere_api_enabled": True,
    "longform_notetweets_consumption_enabled": True,
    "responsive_web_twitter_article_tweet_consumption_enabled": True,
    "tweet_awards_web_tipping_enabled": False,
    "creator_subscriptions_quote_tweet_preview_enabled": False,
    "freedom_of_speech_not_reach_fetch_enabled": True,
    "standardized_nudges_misinfo": True,
    "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
    "rweb_video_timestamps_enabled": True,
    "longform_notetweets_rich_text_read_enabled": True,
    "longform_notetweets_inline_media_enabled": True,
    "responsive_web_enhance_cards_enabled": False,
}

# Rate-limit guard: minimum seconds between requests to avoid 429.
_MIN_REQUEST_INTERVAL = 1.5


class TwitterScraper(BaseScraper):
    """Fetch tweets via X/Twitter's internal GraphQL API using cookies."""

    def __init__(self, config: TwitterConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.config: TwitterConfig = config
        self._user_id_cache: Dict[str, str] = {}
        self._last_request_time: float = 0.0
        self._query_ids: Dict[str, str] = dict(_FALLBACK_QUERY_IDS)  # resolved lazily

    # ------------------------------------------------------------------
    # Dynamic queryId resolution
    # ------------------------------------------------------------------

    async def _resolve_query_ids(self) -> None:
        """Fetch X's main JS bundle and extract current GraphQL queryIds."""
        if self._query_ids.get("_resolved"):
            return
        try:
            # Step 1: find the main JS bundle URL from the HTML page
            resp = await self.client.get(
                "https://x.com", follow_redirects=True, timeout=10.0
            )
            html = resp.text
            # Extract all client-web JS URLs
            js_urls = re.findall(
                r'https://abs\.twimg\.com/responsive-web/client-web/main\.[a-f0-9]+\.js',
                html,
            )
            if not js_urls:
                logger.warning("Could not find X main.js bundle URL, using fallback queryIds")
                return

            # Step 2: download the main JS bundle and extract queryIds
            js_resp = await self.client.get(js_urls[0], timeout=15.0)
            js_text = js_resp.text

            for qid, op_name in _QID_RE.findall(js_text):
                if op_name in self._query_ids:
                    self._query_ids[op_name] = qid
                    logger.debug(f"Resolved queryId: {op_name} -> {qid}")

            self._query_ids["_resolved"] = "true"
            logger.info(
                f"X queryIds resolved: UserByScreenName={self._query_ids.get('UserByScreenName')}, "
                f"UserTweets={self._query_ids.get('UserTweets')}"
            )
        except Exception as exc:
            logger.warning(f"Failed to resolve X queryIds dynamically: {exc}")

    def _graphql_url(self, operation: str) -> str:
        """Build a GraphQL URL for the given operation name."""
        qid = self._query_ids.get(operation, "")
        return f"https://x.com/i/api/graphql/{qid}/{operation}"

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.config.enabled:
            return []

        users = [u.strip().lstrip("@") for u in self.config.users if u.strip()]
        if not users:
            logger.debug("No Twitter users configured, skipping.")
            return []

        creds = self._load_credentials()
        if creds is None:
            return []

        bearer, ct0, auth_token, cookies_str = creds

        await self._resolve_query_ids()

        # Quick connectivity check — if auth is broken (ct0 expired, etc.)
        # skip the entire Twitter fetch instead of failing per-user.
        if not await self._test_connectivity(bearer, ct0, cookies_str):
            logger.warning(
                "X API connectivity check failed (ct0 expired or endpoint blocked). "
                "Skipping Twitter source entirely."
            )
            return []

        logger.info(f"Fetching Twitter (GraphQL) for users: {users}")

        all_items: List[ContentItem] = []

        for username in users:
            try:
                items = await self._fetch_user_tweets(
                    username, since, bearer, ct0, auth_token, cookies_str
                )
                all_items.extend(items)
            except Exception as exc:
                logger.warning(f"Failed to fetch tweets for @{username}: {exc}")

        logger.info(f"Fetched {len(all_items)} tweets via GraphQL.")
        return all_items

    async def fetch_replies_for_item(self, item: ContentItem) -> List[str]:
        """Fetch reply texts for one tweet using adaptive search."""
        if not self.config.fetch_reply_text:
            return []

        creds = self._load_credentials()
        if creds is None:
            return []

        bearer, ct0, auth_token, cookies_str = creds

        conversation_id = str(item.metadata.get("conversation_id") or "")
        if not conversation_id:
            return []

        max_replies = max(self.config.max_replies_per_tweet, 0)
        if max_replies == 0:
            return []

        headers = self._build_headers(bearer, ct0)
        headers["cookie"] = cookies_str

        params = {
            "q": f"conversation_id:{conversation_id}",
            "count": str(min(100, max_replies * 5)),
            "query_source": "typed_query",
            "pc": "1",
            "spelling_corrections": "0",
        }

        try:
            await self._rate_limit_guard()
            resp = await self.client.get(
                _SEARCH_ADAPTIVE_URL,
                headers=headers,
                params=params,
                timeout=20.0,
            )
            if resp.status_code == 429:
                logger.warning("Rate limited while fetching replies, backing off.")
                await asyncio.sleep(15)
                return []
            if resp.status_code in (401, 403):
                logger.error(f"Auth error fetching replies: {resp.status_code}")
                return []
            resp.raise_for_status()
        except Exception as exc:
            logger.warning(f"Failed to fetch replies for tweet {item.id}: {exc}")
            return []

        data = resp.json()
        tweets = data.get("globalObjects", {}).get("tweets", {})
        users_map = data.get("globalObjects", {}).get("users", {})

        return self._extract_reply_lines_from_search(
            item, tweets, users_map, max_replies
        )

    @staticmethod
    def append_discussion_content(item: ContentItem, reply_lines: List[str]) -> bool:
        """Append reply lines under Top Comments marker."""
        if not reply_lines:
            return False

        existing = item.content or ""
        marker = "--- Top Comments ---"
        block = "\n".join(reply_lines)

        if marker in existing:
            if block in existing:
                return False
            item.content = existing + "\n" + block
            return True

        if existing:
            item.content = existing + f"\n\n{marker}\n" + block
        else:
            item.content = f"{marker}\n" + block
        return True

    # ------------------------------------------------------------------
    # Credential helpers
    # ------------------------------------------------------------------

    def _load_credentials(
        self,
    ) -> Optional[tuple[str, str, str, str]]:
        """Load and validate API credentials from environment.

        Returns (bearer, ct0, auth_token, cookies_str) or None on failure.
        """
        bearer = os.environ.get(self.config.bearer_env, "")
        ct0 = os.environ.get(self.config.ct0_env, "")
        auth_token = os.environ.get(self.config.auth_token_env, "")

        if not ct0 or not auth_token:
            logger.warning(
                f"Missing X credentials (need {self.config.ct0_env}, "
                f"{self.config.auth_token_env}). Skipping Twitter."
            )
            return None

        # Fall back to the well-known public bearer token if not provided.
        if not bearer:
            bearer = (
                "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs"
                "%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
            )

        # Build the cookie header string.  Also send twid if available.
        twid = os.environ.get("X_TWID", "")
        cookie_parts = [f"auth_token={auth_token}", f"ct0={ct0}"]
        if twid:
            cookie_parts.append(f"twid={twid}")
        cookies_str = "; ".join(cookie_parts)

        return bearer, ct0, auth_token, cookies_str

    def _build_headers(self, bearer: str, ct0: str) -> Dict[str, str]:
        return {
            "authorization": f"Bearer {bearer}",
            "x-csrf-token": ct0,
            "x-twitter-active-user": "yes",
            "x-twitter-auth-type": "OAuth2Session",
            "x-twitter-client-language": "en",
            "content-type": "application/json",
        }

    # ------------------------------------------------------------------
    # Connectivity check
    # ------------------------------------------------------------------

    async def _test_connectivity(
        self, bearer: str, ct0: str, cookies_str: str
    ) -> bool:
        """Single lightweight request to verify auth + queryId work."""
        try:
            headers = self._build_headers(bearer, ct0)
            headers["cookie"] = cookies_str
            variables = json.dumps(
                {"screen_name": "X", "withSafetyModeUserFields": True},
                separators=(",", ":"),
            )
            features = json.dumps(
                {
                    "hidden_profile_subscriptions_enabled": True,
                    "responsive_web_graphql_exclude_directive_enabled": True,
                    "verified_phone_label_enabled": False,
                    "responsive_web_graphql_timeline_navigation_enabled": True,
                },
                separators=(",", ":"),
            )
            resp = await self.client.get(
                self._graphql_url("UserByScreenName"),
                headers=headers,
                params={"variables": variables, "features": features},
                timeout=10.0,
            )
            ok = resp.status_code == 200
            if not ok:
                logger.warning(f"Connectivity check returned {resp.status_code}")
            return ok
        except Exception as exc:
            logger.warning(f"Connectivity check failed: {exc}")
            return False

    # ------------------------------------------------------------------
    # User ID resolution
    # ------------------------------------------------------------------

    async def _resolve_user_id(
        self,
        username: str,
        bearer: str,
        ct0: str,
        cookies_str: str,
    ) -> Optional[str]:
        """Resolve a screen name to a Twitter user ID (rest_id)."""
        if username.lower() in self._user_id_cache:
            return self._user_id_cache[username.lower()]

        headers = self._build_headers(bearer, ct0)
        headers["cookie"] = cookies_str

        variables = json.dumps(
            {"screen_name": username, "withSafetyModeUserFields": True},
            separators=(",", ":"),
        )
        features = json.dumps(
            {
                "hidden_profile_subscriptions_enabled": True,
                "rweb_tipjar_consumption_enabled": True,
                "responsive_web_graphql_exclude_directive_enabled": True,
                "verified_phone_label_enabled": False,
                "subscriptions_verification_info_is_identity_verified_enabled": True,
                "subscriptions_verification_info_verified_since_enabled": True,
                "highlights_tweets_tab_ui_enabled": True,
                "responsive_web_twitter_article_notes_tab_enabled": True,
                "subscriptions_feature_can_gift_premium": True,
                "creator_subscriptions_tweet_preview_api_enabled": True,
                "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                "responsive_web_graphql_timeline_navigation_enabled": True,
            },
            separators=(",", ":"),
        )

        params = {"variables": variables, "features": features}

        try:
            await self._rate_limit_guard()
            resp = await self.client.get(
                self._graphql_url("UserByScreenName"),
                headers=headers,
                params=params,
                timeout=15.0,
            )
            if resp.status_code == 429:
                logger.warning(f"Rate limited resolving @{username}, backing off.")
                await asyncio.sleep(15)
                return None
            if resp.status_code in (401, 403):
                logger.error(
                    f"Auth error resolving @{username}: {resp.status_code} "
                    f"— credentials may be expired."
                )
                return None
            if resp.status_code == 404:
                logger.warning(
                    f"Got 404 resolving @{username} — queryId expired or "
                    f"endpoint blocked. Skipping Twitter."
                )
                return None
            if resp.status_code != 200:
                logger.warning(
                    f"Unexpected status {resp.status_code} resolving @{username}."
                )
                return None

            data = resp.json()
            result = data.get("data", {}).get("user", {}).get("result", {})
            legacy = result.get("legacy", {})
            user_id = result.get("rest_id") or legacy.get("id_str")

            if user_id:
                self._user_id_cache[username.lower()] = user_id
                logger.debug(f"Resolved @{username} → user_id={user_id}")
                return user_id

            logger.warning(f"Could not resolve user_id for @{username}")
            return None
        except Exception as exc:
            logger.warning(f"Failed to resolve @{username}: {exc}")
            return None

    # ------------------------------------------------------------------
    # Tweet fetching
    # ------------------------------------------------------------------

    async def _fetch_user_tweets(
        self,
        username: str,
        since: datetime,
        bearer: str,
        ct0: str,
        auth_token: str,
        cookies_str: str,
    ) -> List[ContentItem]:
        """Fetch recent tweets for a single user, stopping at pagination."""
        user_id = await self._resolve_user_id(username, bearer, ct0, cookies_str)
        if not user_id:
            return []

        headers = self._build_headers(bearer, ct0)
        headers["cookie"] = cookies_str

        items: List[ContentItem] = []
        cursor: Optional[str] = None
        max_pages = 5  # safety bound
        page = 0

        while page < max_pages:
            page += 1

            variables = {
                "userId": user_id,
                "count": min(self.config.fetch_limit, 40),
                "includePromotedContent": False,
                "withQuickPromoteEligibilityTweetFields": True,
                "withVoice": True,
                "withV2Timeline": True,
            }
            if cursor:
                variables["cursor"] = cursor
            if cursor and cursor.startswith("scroll:"):
                # The "scroll:" prefixed cursor is a bottom-of-page cursor.
                variables["cursor"] = cursor

            features = json.dumps(_TWEET_FEATURES, separators=(",", ":"))
            variables_json = json.dumps(variables, separators=(",", ":"))

            params = {"variables": variables_json, "features": features}

            try:
                await self._rate_limit_guard()
                resp = await self.client.get(
                    self._graphql_url("UserTweets"),
                    headers=headers,
                    params=params,
                    timeout=20.0,
                )
            except httpx.HTTPError as exc:
                logger.warning(f"Network error fetching @{username} page {page}: {exc}")
                break

            if resp.status_code == 429:
                logger.warning(
                    f"Rate limited fetching @{username}, backing off (page {page})."
                )
                await asyncio.sleep(30)
                continue  # retry same page

            if resp.status_code in (401, 403):
                logger.error(
                    f"Auth error for @{username}: {resp.status_code} — "
                    f"credentials may be expired."
                )
                break  # no point retrying

            if resp.status_code != 200:
                logger.warning(
                    f"Unexpected status {resp.status_code} for @{username} "
                    f"tweets (page {page})."
                )
                break

            data = resp.json()
            entries, next_cursor = self._parse_timeline(data)

            for entry in entries:
                parsed = self._parse_tweet_entry(entry, since)
                if parsed:
                    items.append(parsed)

            # If no next cursor or we've collected enough, stop.
            if not next_cursor:
                break
            cursor = next_cursor

            # If all tweets on this page are older than `since`, stop paging.
            # (Not perfectly accurate due to sort order, but a good heuristic.)

        return items

    # ------------------------------------------------------------------
    # Response parsing
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_timeline(data: dict) -> tuple[list, Optional[str]]:
        """Extract tweet entries and the bottom cursor from a GraphQL response."""
        instructions = (
            data.get("data", {})
            .get("user", {})
            .get("result", {})
            .get("timeline_v2", {})
            .get("timeline", {})
            .get("instructions", [])
        )

        entries = []
        next_cursor: Optional[str] = None

        for instruction in instructions:
            # TimelineTimelineItem — single entry wrapper
            inst_type = instruction.get("type", "")
            if inst_type == "TimelineClearCache":
                continue

            entry_list = instruction.get("entries", [])

            # Some responses wrap entries inside an "entry" field
            if not entry_list:
                single_entry = instruction.get("entry")
                if single_entry:
                    entry_list = [single_entry]

            for entry in entry_list:
                content = entry.get("content", {})
                entry_type = content.get("entryType", "")

                if entry_type == "TimelineTimelineItem":
                    item_content = content.get("itemContent", {})
                    if item_content.get("itemType") == "TimelineTweet":
                        entries.append(item_content)

                elif entry_type == "TimelineTimelineCursor":
                    cursor_type = content.get("cursorType", "")
                    if cursor_type == "Bottom":
                        next_cursor = content.get("value")

        return entries, next_cursor

    def _parse_tweet_entry(self, item_content: dict, since: datetime) -> Optional[ContentItem]:
        """Parse a single TimelineTweet itemContent into a ContentItem."""
        try:
            tweet_result = item_content.get("tweet_results", {}).get("result", {})

            # Handle tweet-with-visibility-results wrapper
            if tweet_result.get("__typename") == "TweetWithVisibilityResults":
                tweet_result = tweet_result.get("tweet", tweet_result)

            legacy = tweet_result.get("legacy", {})
            core = tweet_result.get("core", {}).get("user_results", {}).get("result", {})
            core_legacy = core.get("legacy", {})

            # --- created_at ---
            created_at_str = legacy.get("created_at", "")
            if not created_at_str:
                return None
            published_at = self._parse_twitter_date(created_at_str)
            if published_at.tzinfo is None:
                published_at = published_at.replace(tzinfo=timezone.utc)
            if published_at < since:
                return None

            # --- IDs ---
            tweet_id = tweet_result.get("rest_id") or legacy.get("id_str", "")
            if not tweet_id:
                return None
            conversation_id = legacy.get("conversation_id_str", tweet_id)

            # --- Author ---
            screen_name = core_legacy.get("screen_name", "unknown")
            author_name = core_legacy.get("name", screen_name)

            # --- Text ---
            # Prefer full_text; note_retweeted_tweet_result for retweets
            text = legacy.get("full_text", "")
            if not text:
                # Check if this is a retweet wrapper
                rt_result = legacy.get("retweeted_status_result", {}).get("result", {})
                if rt_result:
                    rt_legacy = rt_result.get("legacy", {})
                    text = rt_legacy.get("full_text", "")
                    if not text:
                        return None
                else:
                    return None

            from html import unescape as _unescape
            text = _unescape(text)
            if not text.strip():
                return None

            # --- URL ---
            url = f"https://x.com/{screen_name}/status/{tweet_id}"

            # --- Title ---
            title_body = text[:50].replace("\n", " ").strip()
            if len(text) > 50:
                title_body += "..."
            title = f"@{screen_name}: {title_body}"

            # --- Engagement metrics ---
            favorite_count = legacy.get("favorite_count", 0)
            retweet_count = legacy.get("retweet_count", 0)
            reply_count = legacy.get("reply_count", 0)
            view_count = tweet_result.get("views", {}).get("count")
            bookmark_count = legacy.get("bookmark_count", 0)

            # --- Reply metadata ---
            in_reply_to_status_id = legacy.get("in_reply_to_status_id_str")
            in_reply_to_screen_name = legacy.get("in_reply_to_screen_name")
            is_reply = in_reply_to_status_id is not None

            # --- Media entities (for metadata) ---
            media_urls = []
            for medium in legacy.get("entities", {}).get("media", []):
                media_url = medium.get("media_url_https", "")
                if media_url:
                    media_urls.append(media_url)

            # --- Hashtags ---
            hashtags = [
                h.get("text", "")
                for h in legacy.get("entities", {}).get("hashtags", [])
            ]

            return ContentItem(
                id=self._generate_id(SourceType.TWITTER.value, "tweet", tweet_id),
                source_type=SourceType.TWITTER,
                title=title,
                url=url,
                content=text,
                author=author_name,
                published_at=published_at,
                metadata={
                    "tweet_id": tweet_id,
                    "conversation_id": conversation_id,
                    "screen_name": screen_name,
                    "favorite_count": int(favorite_count),
                    "retweet_count": int(retweet_count),
                    "reply_count": int(reply_count),
                    "view_count": int(view_count) if view_count else None,
                    "bookmark_count": int(bookmark_count) if bookmark_count else None,
                    "is_reply": is_reply,
                    "in_reply_to_status_id": in_reply_to_status_id,
                    "in_reply_to_screen_name": in_reply_to_screen_name,
                    "hashtags": hashtags,
                    "media_count": len(media_urls),
                },
            )
        except Exception as exc:
            logger.debug(f"Failed to parse tweet entry: {exc}")
            return None

    # ------------------------------------------------------------------
    # Reply parsing (adaptive search)
    # ------------------------------------------------------------------

    def _extract_reply_lines_from_search(
        self,
        item: ContentItem,
        tweets: dict,
        users_map: dict,
        max_replies: int,
    ) -> List[str]:
        """Convert adaptive search results into compact reply lines."""
        min_likes = max(self.config.reply_min_likes, 0)
        tweet_id = str(item.metadata.get("tweet_id") or "")
        own_author = (item.metadata.get("screen_name") or "").lower()

        candidates: list[tuple[int, str]] = []

        for tid, tweet_data in tweets.items():
            if tid == tweet_id:
                continue

            # Author
            user_id = tweet_data.get("user_id_str", "")
            user_info = users_map.get(user_id, {})
            handle = user_info.get("screen_name", "unknown")

            if handle.lower() == own_author:
                continue

            text = unescape((tweet_data.get("full_text") or "").strip())
            if not text:
                continue

            likes = int(tweet_data.get("favorite_count", 0))
            replies = int(tweet_data.get("reply_count", 0))
            if likes < min_likes:
                continue

            score = likes * 2 + replies
            line = f"[@{handle} | ❤️ {likes} | 💬 {replies}] {text[:280]}"
            candidates.append((score, line))

        candidates.sort(key=lambda x: x[0], reverse=True)
        return [line for _, line in candidates[:max_replies]]

    # ------------------------------------------------------------------
    # Utility helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_twitter_date(date_str: str) -> datetime:
        """Parse Twitter date format: 'Mon Jan 01 12:00:00 +0000 2025'."""
        try:
            from datetime import datetime as _dt

            return _dt.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")
        except ValueError:
            from dateutil.parser import isoparse

            return isoparse(date_str)

    async def _rate_limit_guard(self) -> None:
        """Ensure a minimum interval between successive API requests."""
        now = time.monotonic()
        elapsed = now - self._last_request_time
        if elapsed < _MIN_REQUEST_INTERVAL:
            await asyncio.sleep(_MIN_REQUEST_INTERVAL - elapsed)
        self._last_request_time = time.monotonic()
