---
layout: default
title: "Horizon Summary: 2026-05-28 (ZH)"
date: 2026-05-28
lang: zh
---

> From 115 items, 21 important content pieces were selected

---

1. [LangGraph SDK 0.4.0 发布，重大流式与子图升级](#item-1) ⭐️ 9.0/10
2. [开源框架关键漏洞影响 VLLM 和 MCP 服务器](#item-2) ⭐️ 9.0/10
3. [Anthropic 和 OpenAI 找到了产品市场契合点，Willison 认为](#item-3) ⭐️ 8.0/10
4. [谷歌宣称用户喜爱 AI 模式后，DuckDuckGo 访问量激增 28%](#item-4) ⭐️ 8.0/10
5. [SQLite 发布 AGENTS.md 定义 AI 智能体政策](#item-5) ⭐️ 8.0/10
6. [Multiplayer：面向编码代理的本地调试代理](#item-6) ⭐️ 8.0/10
7. [OpenClaw 危机：智能体 AI 安全失败完整时间线](#item-7) ⭐️ 8.0/10
8. [95%的 AI 代理演示在 24 小时内死于生产环境](#item-8) ⭐️ 8.0/10
9. [研究：五个前沿 LLM 在 67%的事实核查声明上存在分歧](#item-9) ⭐️ 7.0/10
10. [Kirkland & Ellis 投资 5 亿美元自建 AI 平台](#item-10) ⭐️ 7.0/10
11. [AGI 时间线追踪器引发关于认知劳动自动化的辩论](#item-11) ⭐️ 7.0/10
12. [AI 代理获得基于 DNS 的电话目录用于发现](#item-12) ⭐️ 7.0/10
13. [Visa 投资 Replit 助力代理支付](#item-13) ⭐️ 7.0/10
14. [General Compute 押注 SambaNova 成为下一个 Cerebras](#item-14) ⭐️ 7.0/10
15. [Snowflake 与 AWS 签署 60 亿美元 AI 芯片协议](#item-15) ⭐️ 7.0/10
16. [Z.ai 更换 GLM-5.1 推理网络架构，性能大幅提升](#item-16) ⭐️ 7.0/10
17. [Reachy Mini 机器人现已完全本地运行 LLM 对话](#item-17) ⭐️ 7.0/10
18. [Krasis v1.0 在 8GB GPU 上以阅读速度运行 Qwen 35B 模型](#item-18) ⭐️ 7.0/10
19. [Nvidia LocateAnything：并行框解码提速 10 倍](#item-19) ⭐️ 7.0/10
20. [Qwen 35B 模型在 RTX 3060 12GB 上以 37 t/s 运行并支持 128K 上下文](#item-20) ⭐️ 7.0/10
21. [使用 Neo4j 和混合 RAG 的 AI 编码代理本地执行层](#item-21) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LangGraph SDK 0.4.0 发布，重大流式与子图升级](https://github.com/langchain-ai/langgraph/releases/tag/sdk%3D%3D0.4.0) ⭐️ 9.0/10

LangChain 发布了 LangGraph SDK 0.4.0 版本，引入了带 SSE 传输的 v3 流式原语、WebSocket 流支持、同步作用域子图以及流重连增强。 此重大更新显著提升了代理编排的可靠性和灵活性，使开发者能够构建更强大的实时 AI 代理，并更好地管理流式传输和子图。 主要特性包括异步流重连支持、同步作用域子图句柄、消息/工具调用投影以及共享流订阅。该版本还将核心 langgraph 包升级到 1.2.2。

github · github-actions[bot] · May 28, 14:11

**背景**: LangGraph 是一个用于构建可靠 AI 代理的框架，提供高层抽象和细粒度控制。流式传输对于实时代理交互至关重要，子图则允许对复杂代理管道进行模块化编排。新的 v3 流式原语和 SSE 传输提高了通信效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.langchain.com/langgraph">LangGraph: Agent Orchestration Framework for Reliable AI Agents</a></li>
<li><a href="https://docs.langchain.com/oss/python/langgraph/event-streaming">Event streaming - Docs by LangChain</a></li>

</ul>
</details>

**标签**: `#LangGraph`, `#AI agents`, `#framework`, `#streaming`, `#orchestration`

---

<a id="item-2"></a>
## [开源框架关键漏洞影响 VLLM 和 MCP 服务器](https://www.reddit.com/r/LocalLLaMA/comments/1tpp2th/vulnerability_found_in_framework_used_by_vllm/) ⭐️ 9.0/10

在 VLLM、MCP 服务器及其他 LLM 工具所用的开源框架中发现了一个关键漏洞，可能危及数百万 AI 代理的安全。该漏洞由 Ars Technica 报道并在 Reddit 上引发讨论。 该漏洞对快速增长的 AI 代理和 LLM 应用生态构成严重安全威胁，因为 VLLM 和 MCP 是广泛使用的组件。一旦被利用，攻击者可能获得对 AI 系统的未授权访问或控制，影响到无数用户和服务。 该漏洞存在于一个未公开的开源包中，许多 LLM 工具（包括用于高效模型服务的 VLLM 和用于工具集成的 MCP 服务器）都依赖它。具体细节和 CVE 编号尚未公布，但影响被描述为关键。

rss · r/LocalLLaMA RSS · May 28, 01:27

**背景**: VLLM 是一个用于高效推理和服务大型语言模型的开源框架，采用 PagedAttention 等技术。MCP（模型上下文协议）是 Anthropic 推出的开放标准，用于连接 AI 应用与外部工具和数据源。两者都依赖多个开源包，该漏洞影响了一个共同的依赖项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: Reddit 帖子由用户 Hrethric 提交，提醒社区检查是否受影响，并对尚未有人发布表示惊讶。提供的内容中无其他评论。

**标签**: `#vulnerability`, `#VLLM`, `#MCP`, `#security`, `#AI agents`

---

<a id="item-3"></a>
## [Anthropic 和 OpenAI 找到了产品市场契合点，Willison 认为](https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything) ⭐️ 8.0/10

Simon Willison 认为 Anthropic 和 OpenAI 已经找到了产品市场契合点，其依据是 Anthropic 即将迎来首个盈利季度，以及企业版定价转向基于 API 的计费模式（涉及 Claude Code 和 OpenAI Codex）。 这标志着 LLM 行业的一次重大转变：企业客户愿意支付高昂的 API 使用费用，表明 AI 编程助手已成为高薪专业人士不可或缺的工具，可能会推动新一轮 AI 商业化浪潮。 Willison 估算自己个人消费了价值 2180 美元的 API token，却仅支付了 200 美元订阅费，表明个人用户享受了慷慨补贴。同时，Anthropic 将企业版从固定座位费改为每座位 20 美元加 API 按量计费，OpenAI 也在 2026 年 4 月跟进了类似调整。

rss · Simon Willison · May 27, 16:38 · [社区讨论](https://news.ycombinator.com/item?id=48296794)

**背景**: 产品市场契合度（PMF）指产品满足强大市场需求的程度。在 LLM 领域，Anthropic 和 OpenAI 等公司长期面临能否持续盈利的质疑。开发者社区备受尊敬的 Simon Willison 认为，不断增长的企业 API 账单和即将到来的盈利能力证明了 PMF 已经实现，尤其是在 Claude Code 和 Codex 这类编程代理工具上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://grokipedia.com/page/Claude_Code">Claude Code</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>

</ul>
</details>

**社区讨论**: 评论出现了不同反应。有人（如 trjordan）强调需要回收的巨额资本成本（5-10 万亿美元），而另一些人（noddingham）则批评该帖子是“AI 精神病”并对 ROI 提出质疑。aerhardt 认为分析混淆了 PMF 与盈利能力，binary0010 则质疑在 GLM-5.1 等开源替代品面前其商业模式能否成立。

**标签**: `#AI industry`, `#product-market fit`, `#LLM economics`, `#Anthropic`, `#OpenAI`

---

<a id="item-4"></a>
## [谷歌宣称用户喜爱 AI 模式后，DuckDuckGo 访问量激增 28%](https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/) ⭐️ 8.0/10

在谷歌宣称用户喜爱其 AI 模式后的一周内，DuckDuckGo 的无 AI 搜索页面访问量增加了 28%。 这表明用户对搜索中集成 AI 的强烈抵触，可能使市场份额从谷歌转向注重隐私的替代方案如 DuckDuckGo。 数据显示，5 月 20 日至 25 日期间，noai.duckduckgo.com 的访问量平均增长 22.7%，而 DuckDuckGo 整体流量上升 28%。谷歌的 AI 模式基于 Gemini 2.0，直接在搜索结果中提供生成式 AI 响应。

hackernews · HelloUsername · May 27, 16:28 · [社区讨论](https://news.ycombinator.com/item?id=48296649)

**背景**: DuckDuckGo 是一个注重隐私的搜索引擎，不跟踪用户。谷歌越来越多地将 AI 功能（如 AI 概览和 AI 模式）集成到搜索中，一些用户认为这具有侵扰性。DuckDuckGo 访问量的激增反映了用户对更简单、无 AI 搜索体验的日益增长的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/websearch/answer/16011537?hl=en&co=GENIE.Platform=Android">Get AI-powered responses with AI Mode in Google Search - Android - Google Search Help</a></li>
<li><a href="https://blog.google/products-and-platforms/products/search/explore-web-generative-ai-search/">5 new ways to explore the web with generative AI in Search</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈的反 AI 情绪，用户因对谷歌推动 AI 感到沮丧而转向 DuckDuckGo。一些人指出，AI 摘要对简单查询有用，但会降低复杂主题的搜索质量。对谷歌声称用户喜爱 AI 模式的说法存在怀疑。

**标签**: `#search engines`, `#AI mode`, `#user behavior`, `#DuckDuckGo`, `#Google`

---

<a id="item-5"></a>
## [SQLite 发布 AGENTS.md 定义 AI 智能体政策](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.0/10

SQLite 发布了 AGENTS.md 文件，明确拒绝接受智能体代码，但欢迎智能体提交的 bug 报告和文档补丁。该文件已更新，移除了“目前”一词，强化了拒绝智能体代码的立场。 这为开源项目管理 AI 智能体贡献树立了明确先例，突显了自动化与质量控制之间的张力。可能会影响其他基础项目处理智能体代码和错误报告的方式。 SQLite 不接受没有事先协议和法律文件将其置于公共领域的拉取请求。人类开发者会审查简洁的拉取请求作为概念验证，然后再重新实现。由于 AI 生成的 bug 报告泛滥，SQLite 论坛已专门创建了一个单独的 Bug 论坛。

rss · Simon Willison · May 27, 23:44

**背景**: AGENTS.md 是一种被超过 6 万个开源项目采用的约定，用于为 AI 编码智能体提供指导，类似于面向智能体的 README。Agentic coding 指的是自主 AI 智能体，它们与文件交互、运行命令并解决多步骤问题，几乎无需人工干预。SQLite 是一款广泛使用的嵌入式数据库引擎，其政策反映了对低质量自动化贡献的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agents.md/">AGENTS . md</a></li>
<li><a href="https://medium.com/@nareshkukkala/introducing-agentic-coding-the-future-of-development-with-xcode-b83d85d23297">Introducing Agentic Coding : The Future of Development... | Medium</a></li>

</ul>
</details>

**标签**: `#AI-agents`, `#open-source`, `#software-development-policy`, `#SQLite`

---

<a id="item-6"></a>
## [Multiplayer：面向编码代理的本地调试代理](https://www.multiplayer.app/) ⭐️ 8.0/10

Multiplayer 是一款新型调试代理，可在 Claude Code 等编码代理旁边本地运行，捕获未采样的全栈会话数据，包括前端用户操作、后端追踪、日志以及请求/响应内容。 该工具解决了 AI 编码代理因可观测性数据不完整而生成看似合理但有缺陷的代码（PR slop）的关键痛点，提供了系统故障的完整、关联视图。 Multiplayer 仅在出现问题时保存数据，从而降低存储成本，并在将问题传递给编码代理之前进行本地去重，因此跨多个会话的相同错误会变成一个提示。

rss · Hacker News - AI & Agents · May 28, 14:16

**背景**: 可观测性依赖于日志、指标和追踪，但许多工具使用采样来控制成本，这可能会遗漏关键数据。依赖此类不完整数据的 AI 编码代理可能会生成在生产环境中失败的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://observability.opensearch.org/docs/send-data/opentelemetry/sampling/">Sampling Strategies | OpenSearch - Observability Stack</a></li>
<li><a href="https://www.ibm.com/think/insights/observability-pillars">Three pillars of observability: Logs, metrics and traces - IBM</a></li>

</ul>
</details>

**标签**: `#debugging`, `#observability`, `#AI agents`, `#coding agents`

---

<a id="item-7"></a>
## [OpenClaw 危机：智能体 AI 安全失败完整时间线](https://www.reddit.com/r/artificial/comments/1tq0t1g/the_openclaw_crisis_is_the_most_complete_case/) ⭐️ 8.0/10

2026 年 5 月 15 日，Cyera Research 披露了 OpenClaw（一个拥有超过 34.6 万 GitHub 星标的开源 AI 智能体平台）中的四个可串联的 CVE（CVSS 评分 7.7–9.6）。此前，1 月至 2 月发生了一起供应链攻击，导致 1184 个恶意市场技能和超过 30000 个实例被入侵。 这是智能体 AI 系统中安全故障最全面的案例研究，展示了攻击者如何将多个漏洞串联起来，在不触发传统监控的情况下实现完全入侵。它为所有部署 AI 智能体的组织敲响了警钟，突出了插件生态系统、沙箱实现和凭证管理中的系统性风险。 披露的漏洞包括：通过 TOCTOU 竞态条件的文件系统读取逃逸（CVE-2026-44113，CVSS 7.7）、通过未加引号的 heredoc 导致的凭证泄露（CVE-2026-44115，CVSS 8.8）、MCP 环回权限提升（CVE-2026-44118，CVSS 7.8）以及关键的文件系统写入逃逸（CVE-2026-44112，CVSS 9.6）。此外，有 24.5 万个实例暴露于公共互联网，ClawHub 市场中有 12%被入侵。

rss · r/artificial RSS · May 28, 11:28

**背景**: TOCTOU（检查时间到使用时间）是一种竞态条件漏洞，攻击者利用检查资源状态和使用资源之间的时间差进行攻击。沙箱逃逸允许恶意代码突破隔离环境，访问宿主系统。可串联的 CVE 指多个漏洞可以链接在一起形成完整的攻击链。OpenClaw 是一个用于构建和部署 AI 智能体的开源平台，拥有第三方技能市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use">Time-of-check to time-of-use - Wikipedia</a></li>
<li><a href="https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw">Claw Chain: Cyera Research Unveil Four Chainable ...</a></li>
<li><a href="https://aiweekly.co/alerts/openclaw-cve-chain-leaves-245000-ai-agent-instances-exposed">OpenClaw CVE chain leaves 245,000 AI agent instances exposed</a></li>

</ul>
</details>

**标签**: `#agent security`, `#open-source vulnerability`, `#CVE`, `#AI agent platform`, `#critical incident`

---

<a id="item-8"></a>
## [95%的 AI 代理演示在 24 小时内死于生产环境](https://www.reddit.com/r/artificial/comments/1tq0sqk/95_of_the_agents_posted_here_would_be_dead_within/) ⭐️ 8.0/10

一位拥有 18 个月代理基础设施构建经验的 Reddit 用户发帖指出，95%在线发布的 AI 代理演示在真实生产流量下 24 小时内就会失败，原因在于基础设施问题而非模型限制。帖子指出了三个关键失败模式：重启后记忆丢失、无限循环无法检测、以及缺乏可审计性。 这一批评凸显了 AI 代理行业过度关注模型能力而忽视可靠性基础设施——这实际上是生产系统的真正护城河。它标志着从提示工程转向构建健壮的内存、循环检测和审计层作为下一个竞争前沿。 帖子指出了三个不性感但致命的基建缺口：失忆（重启后代理忘记状态）、循环自杀（代理盲目重复工具调用浪费 token）和黑箱（无推理记录可调试）。作者构建了一个框架无关的解决方案（octopodas.com），通过持久内存、自动循环检测和防篡改审计轨迹来解决这些问题。

rss · r/artificial RSS · May 28, 11:28

**背景**: AI 代理是由 LLM 驱动的系统，通过调用工具和推理数据来自主执行任务。大多数演示在精心策划、受控的环境中运行，但真实生产环境会引入崩溃、网络问题和不可预测的用户行为。最近的行业报告证实，代理会导致无声故障，甚至失控时删除数据库，强调了超越模型本身的可靠性工程需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.humai.blog/why-your-ai-agent-works-in-the-demo-and-breaks-in-the-real-world/">Why Your AI Agent Works in the Demo and Breaks in the Real World</a></li>
<li><a href="https://aiweekly.co/alerts/ai-agents-trigger-silent-outages-enterprises-miss">AI agents trigger silent outages enterprises miss | AI Weekly</a></li>
<li><a href="https://www.statebase.org/guide/llm-agent-reliability">The Complete Guide to LLM Agent Reliability in Production</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Production Deployment`, `#Agent Infrastructure`, `#LLM Reliability`

---

<a id="item-9"></a>
## [研究：五个前沿 LLM 在 67%的事实核查声明上存在分歧](https://lenz.io/research/llm-disagreement) ⭐️ 7.0/10

Lenz.io 的一项研究测试了五个前沿 LLM 对 1000 个真实世界的事实核查声明，发现它们在 67%的声明上存在分歧，仅在 45 个声明上达成一致。研究者使用的提示要求将声明分类为真实、基本真实、误导或虚假。 如此高的分歧率削弱了 LLM 用于自动化事实核查的可靠性，并突显了它们在新闻、社交媒体审核和信息验证中的关键局限性。 该研究使用了用户提交给事实核查平台的声明，而不是带有公开答案键的基准项目。提示明确禁止解释，只要求输出标签。

hackernews · kostaj · May 28, 12:20 · [社区讨论](https://news.ycombinator.com/item?id=48307887)

**背景**: 前沿 LLM 指处于 AI 能力最前沿的最先进的大型语言模型，例如 GPT-4、Claude、Gemini 等。尽管存在幻觉和偏见等已知问题，这些模型越来越多地被用于事实核查任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Frontier_AI_models">Frontier AI models</a></li>
<li><a href="https://arxiv.org/abs/2507.07313">[2507.07313] Frontier LLMs Still Struggle with Simple Reasoning Tasks</a></li>

</ul>
</details>

**社区讨论**: 社区评论提出了几个担忧：提示设计（例如，没有'未知'选项）、排除了 Grok 作为数据点，以及使用 LLM 撰写批评 LLM 可靠性的报告的讽刺。一位评论者指出，事实核查本身是主观的，并非 LLM 独有问题。

**标签**: `#LLM`, `#fact-checking`, `#reliability`, `#research`

---

<a id="item-10"></a>
## [Kirkland & Ellis 投资 5 亿美元自建 AI 平台](https://www.ft.com/content/1825bb59-7b28-460d-b009-ee3cea5dbac3) ⭐️ 7.0/10

收入最高的律师事务所 Kirkland & Ellis 已拨出 5 亿美元，用于构建自己的专有 AI 平台，这标志着单一律所在法律 AI 领域已知的最大投资之一。 此举表明大型律师事务所愿意进行大规模、定制化的 AI 投资，而非仅仅依赖第三方工具，这可能会重塑法律科技领域的竞争格局，并迫使其他律所效仿。 这笔 5 亿美元的投资用于开发针对 Kirkland 特定法律工作流程的专有 AI 平台，包括文件审查、合同分析和诉讼支持。该律所未透露时间表或技术合作伙伴。

rss · Hacker News - AI & Agents · May 28, 15:20

**背景**: 律师事务所传统上对 AI 的采用持谨慎态度，但大语言模型的兴起加速了兴趣。Kirkland & Ellis 年收入超过 60 亿美元，是全球收入最高的律师事务所，这使其有资源构建定制解决方案，而非许可现成的产品。

**社区讨论**: Hacker News 上的讨论很少，只有 1 条评论和 4 个点赞，表明该故事尚未引起显著的社区辩论。

**标签**: `#AI platform`, `#legal AI`, `#enterprise AI`, `#investment`

---

<a id="item-11"></a>
## [AGI 时间线追踪器引发关于认知劳动自动化的辩论](https://futuresearch.ai/blog/agi-timeline-tracker/) ⭐️ 7.0/10

FutureSearch 发布了一篇新博文，介绍了 AGI 时间线追踪器，并估算了 AI 何时能自动化所有认知劳动，在 Hacker News 上引发了广泛讨论。 这个话题之所以重要，是因为它探讨了 AI 对劳动力的影响以及技术变革可能的速度，这将影响政策制定者、工人和科技公司等各方。 该追踪器综合了各种 AI 里程碑和专家意见，得出了一个中位数时间线估计，但博文也承认此类预测存在高度不确定性。

rss · Hacker News - AI & Agents · May 28, 14:21

**背景**: 通用人工智能（AGI）指的是能够执行人类所能完成的任何智力任务的 AI。认知劳动包括解决问题、写作和决策等任务。时间线追踪器汇总专家的预测，以了解这些里程碑可能何时实现。关于 AGI 时间线的争论通常集中在进展是在加速还是遇到根本性限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agitimelines.org/">AGI Timeline Tracker</a></li>
<li><a href="https://trackagi.github.io">AGI Progress Tracker | AI Milestones Timeline</a></li>

</ul>
</details>

**标签**: `#AGI`, `#AI automation`, `#cognitive labor`, `#timeline`

---

<a id="item-12"></a>
## [AI 代理获得基于 DNS 的电话目录用于发现](https://www.theregister.com/ai-ml/2026/05/28/ai-agents-get-their-own-phone-directory-built-atop-dns/5247539) ⭐️ 7.0/10

研究人员推出了代理名称服务（ANS），这是一个类似 DNS 的目录系统，使 AI 代理能够以去中心化的方式相互发现和通信。该架构利用公钥基础设施（PKI）证书实现可验证的身份和信任。 ANS 解决了 AI 代理缺乏公共、安全发现框架的关键问题，这对于多代理协调和代理间通信至关重要。这可能实现跨不同平台和组织的可互操作 AI 代理的新生态系统。 ANS 是协议无关的，包含一个协议适配器层，支持 A2A、MCP 和 ACP 协议。它使用 JSON-LD 进行结构化元数据，并设计为安全且可扩展。

rss · Hacker News - AI & Agents · May 28, 13:46

**背景**: 域名系统（DNS）是一种分层、去中心化的命名系统，用于连接互联网的计算机、服务或其他资源。目前 AI 代理缺乏标准的相互发现和信任方式，阻碍了多代理系统的发展。ANS 将 DNS 原理应用于创建代理身份和能力的公共账本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.10609">Agent Name Service (ANS): A Universal Directory for Secure AI Agent ...</a></li>
<li><a href="https://www.ietf.org/archive/id/draft-narajala-ans-00.html">Agent Name Service (ANS): A Universal Directory for Secure AI Agent ...</a></li>
<li><a href="https://genai.owasp.org/resource/agent-name-service-ans-for-secure-al-agent-discovery-v1-0/">Agent Name Service (ANS) for Secure Al Agent Discovery v1.0</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#DNS`, `#agent-to-agent communication`, `#decentralized discovery`, `#multi-agent coordination`

---

<a id="item-13"></a>
## [Visa 投资 Replit 助力代理支付](https://techcrunch.com/2026/05/28/visa-invests-in-replit-to-power-agentic-payments-for-developers/) ⭐️ 7.0/10

Visa 已投资 Replit，这是一个 AI 驱动的软件开发平台，旨在为开发者提供代理支付能力。超过 1000 名 Visa 员工已经在使用 Replit 进行原型设计和开发。 此次投资标志着 AI 代理在支付领域的重大行业应用，可能改变交易的发起和执行方式。它可能加速从人工发起到代理中介的支付转变，影响开发者和金融服务。 此次投资基于 Replit 现有的 AI 代理能力，该能力允许用户使用自然语言构建完整应用。Visa 的代理支付计划旨在让 AI 代理代表用户自主处理金融交易。

rss · TechCrunch AI · May 28, 14:00

**背景**: Replit 最初是一个协作编码平台，现已发展为 AI 驱动的软件创建生态系统，包括其 Agent 功能，该功能可通过自然语言描述构建应用。代理支付是指 AI 系统能够代表用户自主发起和管理金融交易，这一概念在支付行业日益受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Replit">Replit - Wikipedia</a></li>
<li><a href="https://www.imf.org/en/publications/imf-notes/issues/2026/04/22/how-agentic-ai-will-reshape-payments-575560">How Agentic AI Will Reshape Payments - IMF</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Payments`, `#Replit`, `#Developer Tools`, `#Industry News`

---

<a id="item-14"></a>
## [General Compute 押注 SambaNova 成为下一个 Cerebras](https://techcrunch.com/2026/05/28/has-the-hunt-for-ai-compute-uncovered-the-next-cerebras/) ⭐️ 7.0/10

投资公司 General Compute 押注 SambaNova 将成为继 Cerebras 之后的下一个突破性 AI 芯片制造商。 这标志着投资者对 GPU 之外的替代 AI 硬件的信心日益增强，可能推动 AI 计算基础设施领域的竞争和创新。 SambaNova 最近发布了 SN50 AI 芯片，声称性能比竞争芯片快 5 倍，并与 Intel 合作。该公司早期的 SN40L 芯片已被定位为领先的推理解决方案。

rss · TechCrunch AI · May 28, 13:00

**背景**: 像 Cerebras 和 SambaNova 这样的 AI 芯片初创公司正在设计针对 AI 工作负载优化的专用处理器，旨在挑战 Nvidia 在 GPU 领域的主导地位。Cerebras 的 WSE-3 是有史以来最大的 AI 芯片，而 SambaNova 则专注于推理和代理型 AI。投资者正在寻找这个领域的下一个大赢家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sambanova.ai/">SambaNova | The Fastest AI Inference Platform</a></li>
<li><a href="https://sambanova.ai/blog/sn40l-chip-best-inference-solution">Why SambaNova 's SN40L Chip Is the Best for Inference</a></li>
<li><a href="https://www.cerebras.ai/chip">Cerebras is the go-to platform for fast and effortless AI training.</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#compute`, `#SambaNova`, `#Cerebras`, `#semiconductors`

---

<a id="item-15"></a>
## [Snowflake 与 AWS 签署 60 亿美元 AI 芯片协议](https://techcrunch.com/2026/05/27/in-more-good-news-for-amazon-snowflake-signs-6b-deal-with-aws-for-ai-cpu-chips/) ⭐️ 7.0/10

Snowflake 与亚马逊云服务（AWS）签署了一份为期五年、价值 60 亿美元的协议，以获得 AWS 自研 AI 芯片（Trainium 和 Inferentia）用于其数据云平台，从而减少对 Nvidia GPU 的依赖。 该协议标志着云 AI 基础设施的重大转变，Snowflake 等主要玩家正从 Nvidia 占主导地位的 GPU 产品转向定制芯片，后者承诺为 AI 工作负载提供更好的成本效益和性能。 该协议为期五年，金额达 60 亿美元，涵盖用于 AI 训练的 AWS Trainium 芯片和用于推理的 Inferentia 芯片。Snowflake 将使用这些芯片来支持其 AI 功能，包括 Cortex AI 和文档 AI。

rss · TechCrunch AI · May 27, 20:10

**背景**: Snowflake 是一个云原生数据平台，支持数据仓库、分析和 AI 工作负载。AWS Trainium 和 Inferentia 是自研的 AI 加速器，与 Nvidia 的 GPU 竞争。Trainium 专注于训练，Inferentia 专注于推理，提供成本优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS | Amazon Web Services , Inc.</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Snowflake_Inc.">Snowflake Inc. - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Cloud Computing`, `#AI Chips`, `#AWS`, `#Snowflake`, `#Infrastructure`

---

<a id="item-16"></a>
## [Z.ai 更换 GLM-5.1 推理网络架构，性能大幅提升](https://www.reddit.com/r/LocalLLaMA/comments/1tq35a0/zai_replaced_the_network_architecture_running/) ⭐️ 7.0/10

Z.ai 与清华大学和 HarnetsAI 合作，在运行 GLM-5.1 推理的千卡 GPU 集群上，用自研的 ZCube 架构替换了标准的 ROFT 网络拓扑。这一生产级改动使交换机和光模块成本降低 33%，GPU 推理吞吐量提升 15%，P99 首 token 延迟降低 40.6%。 这一优化表明，重新设计网络架构可以同时降低基础设施成本并提升性能，这在 LLM 服务中实属罕见。它也凸显了网络设计对日益普及的解耦推理系统的重要性——此类系统正成为大规模模型部署的标准方案。 ZCube 架构是一种完全扁平化的网络，消除了 Spine 层，采用两个交换机组之间的完全二分互连，避免了因 Prefill-Decode 解耦推理流量不对称导致的拥塞。整个软件栈和 GPU 保持不变，性能与成本收益完全来自网络改动。

rss · r/LocalLLaMA RSS · May 28, 13:09

**背景**: 采用 Prefill-Decode 解耦的 LLM 推理会产生不对称的网络流量：不同节点间的 KV 缓存传输差异导致在 ROFT（Rail-Optimized Fat Tree）等传统拓扑上形成热点和包反压。ZCube 架构专为解决这些瓶颈而设计，采用扁平化结构和混合单轨/多轨接入方式以实现更好的负载均衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/zcube">Next-generation LLM Inference Network: How ZCube Alleviates ...</a></li>
<li><a href="https://xix.ai/live/4493">Zhipu AI and partners implemented the ZCube network architec ...</a></li>

</ul>
</details>

**标签**: `#inference optimization`, `#network architecture`, `#GLM`, `#GPU clusters`, `#LLM serving`

---

<a id="item-17"></a>
## [Reachy Mini 机器人现已完全本地运行 LLM 对话](https://www.reddit.com/r/LocalLLaMA/comments/1tq4x48/reachy_mini_goes_fully_local/) ⭐️ 7.0/10

Hugging Face 宣布，开源桌面机器人 Reachy Mini 现在可以完全本地运行大型语言模型（LLM）驱动的对话，并提供了详细的设置指南。 这使得与实体机器人进行隐私保护且离线运行的语音交互成为可能，展示了本地 LLM 在具身 AI 中的实际应用，避免了云端依赖。 该设置使用 Python SDK 和 Hugging Face 集成；博客包括针对多种用例的修改，即使没有 Reachy Mini 硬件，也可作为构建本地语音代理的路线图。

rss · r/LocalLLaMA RSS · May 28, 14:15

**背景**: Reachy Mini 是一款开源桌面人形机器人，售价 299 美元起，专为 AI 开发者探索人机交互而设计。本地运行 LLM 意味着模型在用户自己的硬件上执行，确保数据隐私和离线功能。Hugging Face 是开源机器学习模型和工具的领先平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reachymini.net/">Reachy Mini - Open-Source Desktop Humanoid Robot</a></li>
<li><a href="https://grokipedia.com/page/Reachy_Mini">Reachy Mini</a></li>

</ul>
</details>

**标签**: `#local LLM`, `#robotics`, `#voice agents`, `#Hugging Face`, `#open-source`

---

<a id="item-18"></a>
## [Krasis v1.0 在 8GB GPU 上以阅读速度运行 Qwen 35B 模型](https://www.reddit.com/r/LocalLLaMA/comments/1tpyqng/krasis_update_qwen3635ba3b_q4_at_reading_speed_1x/) ⭐️ 7.0/10

Krasis v1.0，一个混合 LLM 运行时，现在可以高效地将大型模型从系统内存流式传输到 VRAM，在单个 8GB RTX 3070 移动 GPU 上，为 Qwen3.6-35B-A3B 模型实现了 222 tok/s 的预填充和 12.48 tok/s 的解码速度。 这一突破使得在消费级 GPU 上运行超出 VRAM 容量的模型成为可能，大幅降低了本地 LLM 推理的硬件门槛，让更多用户能够使用 Qwen-35B 等大型模型。 Krasis v1.0 在热路径上完全使用 Rust 执行，支持 Ampere GPU（RTX 3000 系列），并引入了新的 HQQ 注意力机制及 4/6/8 位 KV 缓存。基准测试报告的是各提示长度下的最佳吞吐量，而非平均值。

rss · r/LocalLLaMA RSS · May 28, 09:42

**背景**: 大型语言模型（LLM）推理需要大量 VRAM；像 Qwen-35B 这样的模型通常需要 20-40GB。Krasis 通过按需从系统内存向 VRAM 流式传输模型权重来克服这一限制，类似于 CPU-GPU 内存交换，但针对 LLM 的预填充和解码阶段进行了优化。半二次量化（HQQ）无需校准数据集即可压缩模型权重，因此适用于运行时量化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/brontoguana/krasis">GitHub - brontoguana/krasis: Krasis is a Hybrid LLM runtime ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=47419138">Krasis LLM Runtime – run large LLM models on a single GPU ...</a></li>
<li><a href="https://dropbox.github.io/hqq_blog/">HQQ quantization</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#runtime optimization`, `#Krasis`, `#Qwen`, `#local LLM`

---

<a id="item-19"></a>
## [Nvidia LocateAnything：并行框解码提速 10 倍](https://www.reddit.com/r/LocalLLaMA/comments/1tpvldv/nvidia_locateanything_fast_and_highquality/) ⭐️ 7.0/10

Nvidia 发布了 LocateAnything，一个 3B 参数的视觉语言定位模型，采用并行框解码（Parallel Box Decoding）技术，在定位任务上比 Qwen3-VL 快 10 倍。 这一突破通过降低推理延迟，显著加速了实时视觉定位应用，例如机器人和增强现实。同时，它提供了开源模型和代码，促进了更广泛的采用和进一步研究。 该模型在超过 1.38 亿个样本上训练，并采用纠正机制：当检测到格式不规则或空间矛盾时，并行解码会回退到顺序逐位解码。该 3B 参数模型已在 Hugging Face 上发布，代码托管在 GitHub 的 NVlabs/Eagle 仓库中。

rss · r/LocalLLaMA RSS · May 28, 06:43

**背景**: 视觉语言定位是根据文本描述（例如'红色汽车'）在图像中定位物体的任务。传统模型以自回归方式逐词生成边界框坐标，速度较慢。并行框解码利用框坐标的结构化特性同时生成多个词元，但需要保障措施来维持精度。Qwen3-VL 是阿里云推出的一系列多模态大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.machinebrief.com/news/locateanything-accelerating-visual-grounding-with-parallel-b-s4lp">LocateAnything: Accelerating Visual Grounding with Parallel ...</a></li>
<li><a href="https://arxiv.org/html/2605.27365v1">LocateAnything: Fast and High-Quality Vision-Language ...</a></li>

</ul>
</details>

**标签**: `#vision-language`, `#NVIDIA`, `#open-source`, `#LLM`, `#grounding`

---

<a id="item-20"></a>
## [Qwen 35B 模型在 RTX 3060 12GB 上以 37 t/s 运行并支持 128K 上下文](https://www.reddit.com/r/LocalLLaMA/comments/1tq0h1p/qwen3635ba3bapex_128k_ctx_on_rtx_3060_12gb_37_ts/) ⭐️ 7.0/10

一位用户展示了在单张 RTX 3060 12GB GPU 上，使用 spiritbuun 的 llama.cpp 分支和 mudler 的 APEX I-Compact 量化，以每秒 37 个 token 的生成速度和 128K 上下文长度运行 Qwen3.6-35B-A3B-APEX 模型。 这表明 35B 参数的大模型可以在消费级 12GB GPU 上高效运行，显著降低了本地 LLM 推理的硬件门槛，并在廉价硬件上实现了更长上下文的任务。 该模型量化为 APEX I-Compact（可能约 4 位），由于 spiritbuun 的 fused MMA fix、TurboQuant 和 flash attention 优化，将约 17GB 的数据卸载到 12GB 显卡成为可能。用户在 needle-in-a-haystack 测试中达到 100%检索准确率，enwik8 数据集上的困惑度为 3.25。

rss · r/LocalLLaMA RSS · May 28, 11:12

**背景**: Qwen3.6-35B-A3B 是一个混合专家（MoE）模型，总参数量 35B 但每个 token 只激活 3B，使其比稠密模型更高效。llama.cpp 是一个流行的本地 LLM 推理引擎，支持 CPU/GPU 运行；量化则减少模型大小以适应有限的显存。APEX 是 mudler 提出的一种新量化格式，声称在困惑度和速度之间取得更好的平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/20969">TurboQuant - Extreme KV Cache Quantization · ggml-org llama ...</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#quantization`, `#llama.cpp`, `#RTX 3060`, `#Qwen`

---

<a id="item-21"></a>
## [使用 Neo4j 和混合 RAG 的 AI 编码代理本地执行层](https://www.reddit.com/r/LocalLLaMA/comments/1tq6sd0/i_built_an_enforcement_layer_for_ai_coding_agents/) ⭐️ 7.0/10

一位开发者发布了 Writ，这是一个面向 AI 编码代理的开源执行层，它利用本地 Neo4j 知识图谱和混合 RAG 仅检索相关规则，并通过 30 个 bash 钩子脚本在进程级别强制合规。 这解决了 AI 编码代理可靠性的一个关键缺口：没有硬性执行，代理往往会忽略或误解大量规则。Writ 的本地架构使其适用于云端和本地 LLM 部署，有望在自动化开发流程中提高代码质量和安全性。 检索管道结合了通过 Tantivy 实现的 BM25、使用 ONNX 托管的 all-MiniLM-L6-v2 嵌入的向量相似度、Neo4j 图遍历、倒数排名融合以及上下文预算管理——全部本地运行，无需外部 API 调用。执行层利用了 Claude Code 的钩子系统，但设计为可适配任何暴露工具调用事件的代理。

rss · r/LocalLLaMA RSS · May 28, 15:23

**背景**: 检索增强生成（RAG）通过检索相关文档来增强 LLM 输出，但标准 RAG 通常检索到不相关内容。混合 RAG 结合向量搜索与知识图谱遍历，实现更精准的检索。Writ 在本地实现了这一方法以强制编码标准，通过 bash 钩子拦截工具调用，防止跳过测试或未经批准的计划就编写代码等违规行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2408.04948v1">HybridRAG: Integrating Knowledge Graphs and Vector Retrieval ...</a></li>
<li><a href="https://github.com/quickwit-oss/tantivy">GitHub - quickwit-oss/tantivy: Tantivy is a full-text search ...</a></li>
<li><a href="https://www.sbert.net/docs/sentence_transformer/pretrained_models.html">Pretrained Models — Sentence Transformers documentation</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#RAG`, `#Knowledge Graphs`, `#Code Agents`, `#Local LLM`

---