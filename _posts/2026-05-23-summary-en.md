---
layout: default
title: "Horizon Summary: 2026-05-23 (EN)"
date: 2026-05-23
lang: en
---

> From 97 items, 13 important content pieces were selected

---

1. [Microsoft Cancels Claude Code Licenses After Developer Preference](#item-1) ⭐️ 8.0/10
2. [Project Glasswing: AI Finds 90.6% Real Vulnerabilities](#item-2) ⭐️ 8.0/10
3. [Anthropic's Code with Claude signals AI coding future](#item-3) ⭐️ 8.0/10
4. [Apex-Testing Update: Real-World Agentic Coding Benchmark](#item-4) ⭐️ 8.0/10
5. [BeeLlama v0.2.0: DFlash Boosts Local LLM Inference Speed Over 4x](#item-5) ⭐️ 8.0/10
6. [Needle 26M beats Qwen3-0.6B in CPU function calling benchmark](#item-6) ⭐️ 8.0/10
7. [Pydantic AI v1.102.0 Patches SSRF Vulnerability](#item-7) ⭐️ 7.0/10
8. [KanBots: Open-Source Kanban with Parallel AI Agents](#item-8) ⭐️ 7.0/10
9. [AI Data Center Demand Squeezes Consumer Memory Supply](#item-9) ⭐️ 7.0/10
10. [Tech giants scale back agentic AI due to 1000x token costs](#item-10) ⭐️ 7.0/10
11. [Polsia Raises $30M as AI Autonomously Runs 7,600 Businesses](#item-11) ⭐️ 7.0/10
12. [AMD Radeon 16GB LLM Testing Repo Launched](#item-12) ⭐️ 7.0/10
13. [Developer Builds Routing Layer to Cut Agent Costs to $16](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Microsoft Cancels Claude Code Licenses After Developer Preference](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad) ⭐️ 8.0/10

Microsoft is planning to remove most of its Claude Code licenses and push developers to use GitHub Copilot CLI instead, after Claude Code proved more popular among internal developers. This move highlights the competitive tension between Microsoft's own Copilot tools and Anthropic's Claude Code, signaling that even dominant platform vendors cannot assume developer loyalty. It also underscores the growing importance of agentic coding tools in the developer ecosystem. According to the article, Microsoft offered developers both Claude Code and Copilot, hoping for feedback on both, but developers overwhelmingly chose Claude Code, undermining Microsoft's new GitHub Copilot CLI tool.

hackernews · robertkarl · May 22, 17:32 · [Discussion](https://news.ycombinator.com/item?id=48238896)

**Background**: Claude Code is an AI-powered coding assistant from Anthropic that operates as an agentic tool in the terminal, understanding codebases and executing tasks autonomously. GitHub Copilot CLI is a similar command-line tool from Microsoft that runs outside of editors like VS Code. Agentic coding tools go beyond simple autocomplete by taking high-level instructions and executing multi-step development tasks, a rapidly evolving area in software engineering.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://www.nytimes.com/2026/01/23/technology/claude-code.html">Five Ways People Are Using Claude Code - The New York Times</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**Discussion**: Commenters noted that developers often face pressure to use the most effective tool to avoid being fired, making token efficiency a secondary concern. Some pointed out that supervised, human-in-the-loop use of Claude Code is more productive and consumes fewer tokens than fully autonomous agentic workflows. The discussion also highlighted that Microsoft likely expected Copilot to win, but developers voted with their feet.

**Tags**: `#AI agents`, `#Claude Code`, `#Microsoft`, `#Copilot`, `#developer tools`

---

<a id="item-2"></a>
## [Project Glasswing: AI Finds 90.6% Real Vulnerabilities](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 8.0/10

Anthropic's Project Glasswing update reports that Mythos, an AI code analysis tool, identified thousands of vulnerabilities with a 90.6% true positive rate, validated by independent security firms. This demonstrates that AI-driven static analysis can achieve high accuracy, potentially transforming software security by enabling faster, more reliable vulnerability detection at scale. Out of 1,752 assessed high- or critical-rated vulnerabilities, 1,587 (90.6%) were valid true positives, and 1,094 (62.4%) confirmed as high or critical severity. The tool analyzes code like a security-focused reviewer.

hackernews · louiereederson · May 22, 19:31 · [Discussion](https://news.ycombinator.com/item?id=48240419)

**Background**: Project Glasswing is an Anthropic defensive cybersecurity initiative built around Claude Mythos Preview, a frontier model. Mythos is an AI agent that reasons about code, generating hypotheses and ranking findings, aiming to secure critical software in the AI era.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>
<li><a href="https://hivesecurity.gitlab.io/blog/project-glasswing-anthropic-claude-mythos-cybersecurity/">Project Glasswing : Anthropic 's AI That Finds... — Hive Security</a></li>

</ul>
</details>

**Discussion**: Comments show a mix of praise and skepticism: some users report high accuracy in practice with similar tools, while others, like curl maintainer Daniel Steinberg, question whether Mythos significantly outperforms existing tools. There is also debate about patch cycles and supply chain risks.

**Tags**: `#AI agent`, `#code analysis`, `#security`, `#Anthropic`, `#vulnerability detection`

---

<a id="item-3"></a>
## [Anthropic's Code with Claude signals AI coding future](https://www.reddit.com/r/artificial/comments/1tlh202/anthropics_code_with_claude_showed_off_codings/) ⭐️ 8.0/10

Anthropic demonstrated its agentic coding tool 'Claude Code' at the 'Code with Claude' developer conference, showcasing AI that can understand codebases, edit files, and run commands autonomously. This marks a significant leap in AI-assisted software development, potentially accelerating productivity for developers while also raising concerns about job displacement and code quality. Claude Code operates via a terminal or IDE integration, leveraging models like Claude Sonnet 4.6, and was released alongside OpenAI's updated Codex, intensifying competition in AI coding agents.

rss · r/artificial RSS · May 23, 13:50

**Background**: AI coding tools have evolved from simple autocomplete to autonomous agents that can manage entire development workflows. Anthropic's Claude Code represents the latest shift toward agentic AI, where the model not only suggests code but also executes terminal commands and edits files directly, blurring the line between assistant and developer.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent , Terminal, IDE</a></li>
<li><a href="https://www.anthropic.com/news/Introducing-code-with-claude">Code with Claude - Anthropic 's First Developer Conference</a></li>

</ul>
</details>

**Tags**: `#AI coding`, `#Claude`, `#Anthropic`, `#AI agents`, `#coding tools`

---

<a id="item-4"></a>
## [Apex-Testing Update: Real-World Agentic Coding Benchmark](https://www.reddit.com/r/LocalLLaMA/comments/1tlh4vq/apextesting_realworld_real_repos_agentic_coding/) ⭐️ 8.0/10

Apex-Testing has been updated to version covering 95% of current models, using 65-70 real private GitHub repos with 70 tasks across 8 categories to evaluate agentic coding abilities. This benchmark cuts through marketing hype and benchmaxxing by testing models on actual bugs and feature requests, providing developers and researchers with a realistic measure of coding agent performance. Metrics include average cost, average time, category/difficulty scoring, and an ELO-based leaderboard. Some runs are incomplete: Qwen3.7 Max (~40/70 tasks), Deepseek v4 pro+flash, and local Qwen models pending addition.

rss · r/LocalLLaMA RSS · May 23, 13:54

**Background**: Agentic coding involves AI agents actively collaborating on development tasks beyond simple autocomplete. Benchmaxxing refers to models optimizing for benchmark scores at the expense of real-world performance, a form of Goodhart's Law. Apex-Testing addresses this by using private repos that models haven't seen before.

<details><summary>References</summary>
<ul>
<li><a href="https://krowdev.com/guide/agentic-coding-getting-started/">Getting Started with Agentic Coding — krowdev</a></li>
<li><a href="https://saanyaojha.substack.com/p/from-progress-to-pageantry-benchmaxxing">From Progress to Pageantry: Benchmaxxing in the Age of AI</a></li>

</ul>
</details>

**Tags**: `#agentic coding`, `#benchmark`, `#real-world`, `#coding agents`, `#LLM evaluation`

---

<a id="item-5"></a>
## [BeeLlama v0.2.0: DFlash Boosts Local LLM Inference Speed Over 4x](https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/) ⭐️ 8.0/10

BeeLlama v0.2.0 introduces a major DFlash speculative decoding update, achieving up to 4.93x speedup for Gemma 4 31B (177.8 tps) and 4.40x for Qwen 3.6 27B (163.9 tps) on a single RTX 3090, with prompt processing speed remaining near baseline. This release significantly lowers the barrier for running large language models locally on consumer GPUs, making high-speed inference accessible without expensive data-center hardware. It demonstrates the practical impact of advanced speculative decoding techniques for the open-source LLM community. The DFlash implementation includes efficient draft KV cache projection caching, cleaner prefill handling, and safer CUDA execution. The update also adds full Gemma 4 31B support with vision, supports DFlash GGUFs, and tightens reasoning and tool-call boundaries.

rss · r/LocalLLaMA RSS · May 22, 17:34

**Background**: BeeLlama is a performance-focused fork of llama.cpp that adds DFlash speculative decoding, adaptive draft control, TurboQuant KV-cache compression, and reasoning-loop protection. Speculative decoding uses a lightweight draft model to propose multiple tokens that the target model verifies in parallel, accelerating generation without quality loss. DFlash is a block diffusion approach that enables efficient parallel drafting.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Anbeeld/beellama.cpp">GitHub - Anbeeld/beellama.cpp: DFlash & TurboQuant in llama.cpp with up ...</a></li>
<li><a href="https://z-lab.ai/projects/dflash/">DFlash : Block Diffusion for Flash Speculative Decoding - Z Lab</a></li>
<li><a href="https://huggingface.co/z-lab/Qwen3.5-9B-DFlash">z-lab/Qwen3.5-9B- DFlash · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#BeeLlama`, `#DFlash`, `#local LLM`, `#GPU acceleration`

---

<a id="item-6"></a>
## [Needle 26M beats Qwen3-0.6B in CPU function calling benchmark](https://www.reddit.com/r/LocalLLaMA/comments/1tljs5o/benchmarked_needle_26m_vs_qwen306b_on_cpu/) ⭐️ 8.0/10

A benchmark on a 4-core CPU compared Needle 26M, a tiny specialist model distilled from Gemini for function calling, against Qwen3-0.6B, a general-purpose small model. Needle achieved 72% tool_match accuracy vs 56% for Qwen3, while being 4.4x faster (10.9s vs 47.9s mean latency) despite having 23x fewer parameters. This result demonstrates that small, specialized models can outperform much larger ones for specific tasks like tool calling, which is crucial for on-device AI agents and edge deployment where compute and memory are limited. It also highlights different failure modes between specialist and generalist models, guiding practitioners in selecting the right model architecture. Needle's failures were mostly wrong tool selection (e.g., routing system commands to search_web), while Qwen3's failures were complete parse failures (responding in prose instead of emitting <tool_call> tags). Needle scored 8% on first pass due to schema mismatch (OpenAI JSON Schema vs its flat schema), but after conversion jumped to 72%. Qwen3 required using tokenizer.apply_chat_template with enable_thinking=False to avoid consuming full 256-token budget.

rss · r/LocalLLaMA RSS · May 23, 15:38

**Background**: Function calling in LLMs refers to the model's ability to output structured calls to predefined tools or APIs, enabling agentic behavior. Model distillation is a technique where a smaller student model is trained to mimic the outputs of a larger teacher model, compressing knowledge into fewer parameters. Needle is a 26M parameter model distilled from Google's Gemini 3.1 specifically for function calling, aiming to run efficiently on consumer CPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/ needle : 26 m function call model that runs on...</a></li>
<li><a href="https://byteiota.com/needle-26m-model-gemini-tool-calling-runs-on-devices/">Needle 26 M Model : Gemini Tool Calling Runs on Devices | byteiota</a></li>
<li><a href="https://dev.to/jtorchia/show-hn-needle-distilled-gemini-tool-calling-into-26m-parameters-technical-read-zero-hype-46jo">Show HN: Needle distilled Gemini tool calling into 26 M parameters...</a></li>

</ul>
</details>

**Tags**: `#Agent Frameworks`, `#LLM Inference`, `#Function Calling`, `#Benchmark`, `#Small Models`

---

<a id="item-7"></a>
## [Pydantic AI v1.102.0 Patches SSRF Vulnerability](https://github.com/pydantic/pydantic-ai/releases/tag/v1.102.0) ⭐️ 7.0/10

Pydantic AI v1.102.0 fixes an SSRF vulnerability in URL validation by expanding IPv6 transition-form handling, specifically addressing NAT64 and ISATAP address formats that could bypass the cloud-metadata blocklist. This security patch is critical for users running applications on IPv6-only or dual-stack networks with NAT64/ISATAP, as it prevents potential server-side request forgery attacks that could expose cloud metadata. The vulnerability only affects setups that explicitly opt a FileUrl into force_download='allow-local' with untrusted input on NAT64- or ISATAP-configured networks; standard dual-stack cloud VMs and bundled integrations are not affected.

github · dsfaccini · May 23, 01:02

**Background**: IPv6 transition mechanisms like NAT64 and ISATAP allow IPv6-only hosts to communicate with IPv4-only hosts by embedding IPv4 addresses into IPv6 addresses. These embedded addresses can be manipulated to bypass URL validation blocklists, leading to SSRF attacks. Pydantic AI's URL validation previously did not fully handle these transition forms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NAT64">NAT64</a></li>
<li><a href="https://en.wikipedia.org/wiki/ISATAP">ISATAP</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_IPv6_transition_mechanisms">List of IPv6 transition mechanisms - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#pydantic-ai`, `#SSRF`, `#URL validation`

---

<a id="item-8"></a>
## [KanBots: Open-Source Kanban with Parallel AI Agents](https://www.kanbots.dev/) ⭐️ 7.0/10

KanBots is an open-source desktop Kanban app that allows users to run parallel AI agents on every card, enabling automated task execution across multiple independent agents simultaneously. This tool addresses the growing demand for efficient multi-agent orchestration in software development, offering a local-first, no-server approach that contrasts with existing cloud-dependent solutions. It could reduce the overhead of managing multiple coding agents. KanBots is local-first, storing everything in a .kanbots folder next to the repo (SQLite database, configs, worktrees), with no cloud account or telemetry. It is designed for desktop use and integrates with tools like Claude Code and Codex agents.

hackernews · vitriapp · May 22, 18:17 · [Discussion](https://news.ycombinator.com/item?id=48239413)

**Background**: Kanban is a visual workflow management method originating from Toyota's manufacturing system, designed to limit work-in-progress and optimize flow. AI agents are autonomous programs that can perform specific tasks like coding or testing. Agent orchestration is the coordination of multiple specialized agents to complete complex workflows. KanBots merges these concepts into a desktop app where each Kanban card spawns an independent AI agent.

<details><summary>References</summary>
<ul>
<li><a href="https://firethering.com/kanbots-ai-kanban-board-claude-code-codex-agents/">KanBots: Open-Source AI Kanban Board for Claude Code... - Firethering</a></li>
<li><a href="https://departmentofproduct.substack.com/p/what-is-parallel-ai-agent-coding">What is parallel AI agent coding? An in-depth guide for product teams</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agent-orchestration">What is AI Agent Orchestration? | IBM</a></li>

</ul>
</details>

**Discussion**: Community members expressed mixed reactions: some praised the local-first design but others voiced practical concerns. One developer noted the difficulty of reviewing a night's worth of agent activity, while another compared it to Vibe Kanban which was abandoned due to lack of profitability. A commenter argued the tool contradicts Kanban's principle of limiting work-in-progress. Others highlighted the challenge of supervising multiple agents and merging their outputs.

**Tags**: `#AI Agents`, `#Open Source`, `#Kanban`, `#Agent Orchestration`

---

<a id="item-9"></a>
## [AI Data Center Demand Squeezes Consumer Memory Supply](https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything) ⭐️ 7.0/10

Memory manufacturers are reallocating wafer capacity from DDR and LPDDR to HBM due to surging AI data center demand, reducing consumer memory supply and raising prices for electronics like smartphones. 这种产能转移使得消费电子产品（尤其是100美元以下的廉价智能手机）更加昂贵，在非洲和南亚等对价格敏感的市场中可及性下降。 Only three major memory manufacturers exist, and they under-provision capacity to avoid oversupply. HBM consumes over three times the wafer capacity per gigabyte compared to DDR or LPDDR.

rss · Simon Willison · May 22, 22:01

**Background**: HBM (High-Bandwidth Memory) is a 3D-stacked DRAM used in AI accelerators for high bandwidth. DDR and LPDDR are used in desktops and mobile devices respectively. Wafer allocation determines how much of each memory type can be produced. The shortage is expected to last until at least 2030.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HBM_memory_shortage">HBM memory shortage</a></li>
<li><a href="https://semiwiki.com/wikis/semiconductor-ip-wikis/ddr-vs-lpddr-vs-hbm-wiki/">DDR vs. LPDDR vs. HBM Wiki - Semiwiki</a></li>

</ul>
</details>

**Tags**: `#memory`, `#AI infrastructure`, `#hardware pricing`, `#HBM`, `#DDR`

---

<a id="item-10"></a>
## [Tech giants scale back agentic AI due to 1000x token costs](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-cost-crisis-hits-tech-giants-as-employee-tokenmaxxing-backfires-agentic-ai-eats-up-to-1000x-more-tokens-than-standard-ai-sparks-corporate-pullback-at-microsoft-meta-and-amazon) ⭐️ 7.0/10

Microsoft, Meta, and Amazon are pulling back from agentic AI after employees' token usage skyrocketed up to 1000 times that of standard AI, causing a cost crisis and rendering the 'tokenmaxxing' strategy counterproductive. This reveals a fundamental economic barrier to deploying autonomous AI agents in enterprises, potentially slowing adoption and forcing companies to redesign AI workflows to manage costs. Agentic AI systems perform multi-step reasoning and tool use, consuming up to 1000x more tokens than simple Q&A models. 'Tokenmaxxing' refers to employees maximizing AI usage to inflate productivity metrics, which backfired when costs ballooned.

rss · Hacker News - AI & Agents · May 23, 15:03

**Background**: Agentic AI refers to autonomous systems that set goals, plan, and execute complex tasks with minimal human intervention. Token usage is the primary cost metric in AI services, with each token representing a unit of processing. 'Tokenmaxxing' emerged as a trend where workers use AI extensively to appear productive, but in this case it led to unsustainable costs for tech giants.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Token_maxxing">Token maxxing - Wikipedia</a></li>
<li><a href="https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/">The Pulse: ‘Tokenmaxxing’ as a weird new trend - The Pragmatic Engineer</a></li>
<li><a href="https://www.hostinger.com/tutorials/what-is-agentic-ai">hostinger.com/tutorials/what-is- agentic - ai</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Cost`, `#Token Usage`, `#Enterprise AI`, `#Agentic AI`

---

<a id="item-11"></a>
## [Polsia Raises $30M as AI Autonomously Runs 7,600 Businesses](https://noqta.tn/en/news/polsia-ai-autonomous-company-30m-funding-2026) ⭐️ 7.0/10

Polsia has secured $30 million in funding to scale its autonomous AI system that currently operates 7,600 businesses without human intervention. This marks a significant milestone for AI-driven business automation, demonstrating that agentic frameworks can now manage full-scale operations, potentially reshaping entrepreneurship and small business management. Polsia’s AI system handles planning, coding, and marketing around the clock, with over 500 companies and $450K+ ARR already running on the platform. The $30M funding round will accelerate deployment and development.

rss · Hacker News - AI & Agents · May 23, 14:56

**Background**: Polsia is an autonomous agent platform that acts as a 24/7 digital co-founder, integrating strategic planning, software development, and full-funnel marketing. It belongs to the emerging category of agentic frameworks—AI systems that can set goals, make decisions, and execute complex tasks independently.

<details><summary>References</summary>
<ul>
<li><a href="https://polsia.com/">Polsia — AI That Runs Your Company While You Sleep</a></li>
<li><a href="https://moge.ai/product/polsia">Polsia : Autonomous company-operating platform that... - MOGE</a></li>
<li><a href="https://www.toolcenter.ai/en/tools/polsia">Polsia : Autonomous AI system that plans, codes, and... | ToolCenter</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Automation`, `#Funding`, `#Agentic Framework`

---

<a id="item-12"></a>
## [AMD Radeon 16GB LLM Testing Repo Launched](https://www.reddit.com/r/LocalLLaMA/comments/1tl4o1m/clubrdna16_practical_16gb_amdradeon_local_llm/) ⭐️ 7.0/10

A new GitHub repository, club-rdna16, provides practical testing profiles for running large language models on 16GB AMD Radeon GPUs, including exact llama.cpp launch settings, context lengths, and long-context retrieval checks. Early results on an RX 6900 XT show that Qwen3.6 35B-A3B with UD-IQ3_XXS quantization and q8 KV cache achieves 131k context length. This repo fills a gap for AMD GPU users who lack standardized, reproducible benchmarks for local LLM inference, unlike the more mature NVIDIA ecosystem. It helps the community optimize models for consumer AMD hardware, potentially expanding access to local AI inference. The repo profiles include exact llama.cpp launch commands, context lengths that fit, KV cache types (q8), power profile notes, and ROCm/HIP setup details. The initial tests focus on Qwen3.6 models (27B and 35B-A3B) using Unsloth MTP GGUFs and UD-IQ3_XXS quantizations.

rss · r/LocalLLaMA RSS · May 23, 03:16

**Background**: llama.cpp is a popular C++ implementation for running LLMs locally, supporting various backends including ROCm for AMD GPUs. ROCm is AMD's open-source GPU computing platform, and HIP is a translation layer for CUDA code. Quantization reduces model precision to fit in limited VRAM, and KV cache optimization is critical for long-context inference. Multi-Token Prediction (MTP) is a technique that can double inference speed without accuracy loss.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF">unsloth /Qwen3.6-27B- MTP -GGUF · Hugging Face</a></li>
<li><a href="https://unsloth.ai/docs/models/qwen3.6">Qwen3.6 - How to Run Locally | Unsloth Documentation</a></li>
<li><a href="https://ollama.com/danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-IQ3_XXS">danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-IQ3_XXS</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#local-LLM`, `#GPU-inference`, `#llama.cpp`, `#quantization`

---

<a id="item-13"></a>
## [Developer Builds Routing Layer to Cut Agent Costs to $16](https://www.reddit.com/r/LocalLLaMA/comments/1tljn16/16_refactor_400_steps_95_routed_to_open_moe/) ⭐️ 7.0/10

A developer created a routing layer that directs simple agent steps to a local 21B-parameter MoE model (Hunyuan Hy3 preview) and complex steps to Opus, achieving 93.4% success on a 400-step Python refactoring task at a total cost of $15.60. This approach demonstrates a practical cost-saving strategy for agent orchestration by using smaller local models for routine tasks and reserving expensive frontier models for difficult cases, potentially making AI agents more accessible and affordable. The routing layer uses vLLM 0.8 with enable_auto_tool_choice, and setting reasoning to no_think on routine steps cut token spend by roughly 30%. The model Hunyuan Hy3 preview is a 295B-parameter MoE model with 21B active parameters, running on 2x A100 GPUs.

rss · r/LocalLLaMA RSS · May 23, 15:33

**Background**: Mixture-of-Experts (MoE) architectures activate only a subset of parameters per token, enabling large models to run efficiently. Hunyuan Hy3 preview, developed by Tencent, uses 21B active parameters out of 295B total. vLLM is a high-throughput inference engine that supports tool calling via enable_auto_tool_choice. This setup allows developers to route tasks between local and cloud models to balance cost and capability.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/stable/features/tool_calling/">Tool Calling - vLLM</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy3-preview">GitHub - Tencent- Hunyuan / Hy 3 -preview: Hy 3 preview...</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts ? | IBM</a></li>

</ul>
</details>

**Tags**: `#agent orchestration`, `#cost optimization`, `#MoE`, `#vLLM`, `#routing`

---