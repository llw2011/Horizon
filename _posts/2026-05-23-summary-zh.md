---
layout: default
title: "Horizon Summary: 2026-05-23 (ZH)"
date: 2026-05-23
lang: zh
---

> From 97 items, 13 important content pieces were selected

---

1. [微软因开发者偏爱取消 Claude Code 许可证](#item-1) ⭐️ 8.0/10
2. [Project Glasswing：AI 发现 90.6%真实漏洞](#item-2) ⭐️ 8.0/10
3. [Anthropic 的 Code with Claude 预示 AI 编码未来](#item-3) ⭐️ 8.0/10
4. [Apex-Testing 更新：真实世界智能编码基准测试](#item-4) ⭐️ 8.0/10
5. [BeeLlama v0.2.0：DFlash 将本地 LLM 推理速度提升超过 4 倍](#item-5) ⭐️ 8.0/10
6. [Needle 26M 在 CPU 函数调用基准测试中击败 Qwen3-0.6B](#item-6) ⭐️ 8.0/10
7. [Pydantic AI v1.102.0 修复 SSRF 漏洞](#item-7) ⭐️ 7.0/10
8. [KanBots：开源看板，每卡片并行运行 AI 代理](#item-8) ⭐️ 7.0/10
9. [AI 数据中心需求挤压消费级内存供应](#item-9) ⭐️ 7.0/10
10. [代理 AI 代币消耗高 1000 倍，科技巨头缩减使用](#item-10) ⭐️ 7.0/10
11. [Polsia 融资 3000 万美元，AI 自主运营 7600 家企业](#item-11) ⭐️ 7.0/10
12. [AMD Radeon 16GB LLM 测试仓库发布](#item-12) ⭐️ 7.0/10
13. [开发者搭建路由层，将代理成本降至 16 美元](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [微软因开发者偏爱取消 Claude Code 许可证](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad) ⭐️ 8.0/10

微软计划取消大部分 Claude Code 许可证，并推动开发者转而使用 GitHub Copilot CLI，因为 Claude Code 在内部开发者中更受欢迎。 此举凸显了微软自家 Copilot 工具与 Anthropic 的 Claude Code 之间的竞争张力，表明即使是主导平台供应商也无法假设开发者忠诚度。这也凸显了 agentic 编码工具在开发者生态系统中日益增长的重要性。 据文章称，微软向开发者同时提供了 Claude Code 和 Copilot，希望获得两者的反馈，但开发者压倒性地选择了 Claude Code，削弱了微软新的 GitHub Copilot CLI 工具。

hackernews · robertkarl · May 22, 17:32 · [社区讨论](https://news.ycombinator.com/item?id=48238896)

**背景**: Claude Code 是 Anthropic 推出的一款 AI 驱动的编码助手，作为终端中的 agentic 工具运行，能够理解代码库并自主执行任务。GitHub Copilot CLI 是微软的类似命令行工具，可在 VS Code 等编辑器之外运行。Agentic 编码工具超越了简单的自动补全，能接受高级指令并执行多步开发任务，这是软件工程中快速发展的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://www.nytimes.com/2026/01/23/technology/claude-code.html">Five Ways People Are Using Claude Code - The New York Times</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，开发者经常面临使用最有效工具以免被解雇的压力，因此 token 效率成为次要问题。一些人指出，监督式、人机协作的 Claude Code 使用比完全自主的 agentic 工作流更高效且消耗更少 token。讨论还强调，微软可能预期 Copilot 会胜出，但开发者用行动做出了选择。

**标签**: `#AI agents`, `#Claude Code`, `#Microsoft`, `#Copilot`, `#developer tools`

---

<a id="item-2"></a>
## [Project Glasswing：AI 发现 90.6%真实漏洞](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 8.0/10

Anthropic 的 Project Glasswing 更新报告称，AI 代码分析工具 Mythos 发现了数千个漏洞，真实阳性率达 90.6%，并由独立安全公司验证。 这表明 AI 驱动的静态分析可以达到高精度，可能通过实现更快、更可靠的大规模漏洞检测来改变软件安全格局。 在 1752 个被评估的高或关键级漏洞中，1587 个（90.6%）为有效真阳性，1094 个（62.4%）被确认为高或关键严重性。该工具像安全导向的审查者一样分析代码。

hackernews · louiereederson · May 22, 19:31 · [社区讨论](https://news.ycombinator.com/item?id=48240419)

**背景**: Project Glasswing 是 Anthropic 围绕 Claude Mythos Preview 前沿模型构建的防御性网络安全计划。Mythos 是一个 AI 代理，它推理代码、生成假设并对发现进行排序，旨在保护 AI 时代的关键软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>
<li><a href="https://hivesecurity.gitlab.io/blog/project-glasswing-anthropic-claude-mythos-cybersecurity/">Project Glasswing : Anthropic 's AI That Finds... — Hive Security</a></li>

</ul>
</details>

**社区讨论**: 评论褒贬不一：一些用户报告类似工具在实践中准确率高，而另一些人（如 curl 维护者 Daniel Steinberg）质疑 Mythos 是否显著优于现有工具。关于补丁周期和供应链风险也存在讨论。

**标签**: `#AI agent`, `#code analysis`, `#security`, `#Anthropic`, `#vulnerability detection`

---

<a id="item-3"></a>
## [Anthropic 的 Code with Claude 预示 AI 编码未来](https://www.reddit.com/r/artificial/comments/1tlh202/anthropics_code_with_claude_showed_off_codings/) ⭐️ 8.0/10

Anthropic 在其“Code with Claude”开发者大会上演示了代理式编码工具“Claude Code”，展示了能够自主理解代码库、编辑文件和运行命令的 AI。 这标志着 AI 辅助软件开发的一次重大飞跃，可能提高开发者的生产力，同时也引发了对就业替代和代码质量的担忧。 Claude Code 通过终端或 IDE 集成运行，利用 Claude Sonnet 4.6 等模型，并与 OpenAI 更新的 Codex 同时发布，加剧了 AI 编码代理领域的竞争。

rss · r/artificial RSS · May 23, 13:50

**背景**: AI 编码工具已从简单的自动补全演变为能够管理整个开发工作流的自主代理。Anthropic 的 Claude Code 代表了向代理式 AI 的最新转变，模型不仅建议代码，还能直接执行终端命令和编辑文件，模糊了助手与开发者之间的界限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent , Terminal, IDE</a></li>
<li><a href="https://www.anthropic.com/news/Introducing-code-with-claude">Code with Claude - Anthropic 's First Developer Conference</a></li>

</ul>
</details>

**标签**: `#AI coding`, `#Claude`, `#Anthropic`, `#AI agents`, `#coding tools`

---

<a id="item-4"></a>
## [Apex-Testing 更新：真实世界智能编码基准测试](https://www.reddit.com/r/LocalLLaMA/comments/1tlh4vq/apextesting_realworld_real_repos_agentic_coding/) ⭐️ 8.0/10

Apex-Testing 已更新至覆盖 95%当前模型的版本，使用 65-70 个真实私有 GitHub 仓库，包含 8 个类别的 70 个任务来评估智能编码能力。 该基准测试通过在真实错误和功能请求上测试模型，打破了营销炒作和刷榜行为，为开发者和研究人员提供了编码智能体性能的真实衡量标准。 指标包括平均成本、平均时间、基于类别/难度的评分以及基于 ELO 的排行榜。部分运行尚未完成：Qwen3.7 Max（约 40/70 任务）、Deepseek v4 pro+flash，本地 Qwen 模型待添加。

rss · r/LocalLLaMA RSS · May 23, 13:54

**背景**: 智能编码（Agentic coding）是指 AI 智能体在开发任务中主动协作，而不仅仅是自动补全。刷榜（Benchmaxxing）指模型为优化基准分数而牺牲真实性能，是古德哈特定律的一种表现。Apex-Testing 通过使用模型未曾见过的私有仓库来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krowdev.com/guide/agentic-coding-getting-started/">Getting Started with Agentic Coding — krowdev</a></li>
<li><a href="https://saanyaojha.substack.com/p/from-progress-to-pageantry-benchmaxxing">From Progress to Pageantry: Benchmaxxing in the Age of AI</a></li>

</ul>
</details>

**标签**: `#agentic coding`, `#benchmark`, `#real-world`, `#coding agents`, `#LLM evaluation`

---

<a id="item-5"></a>
## [BeeLlama v0.2.0：DFlash 将本地 LLM 推理速度提升超过 4 倍](https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/) ⭐️ 8.0/10

BeeLlama v0.2.0 带来了重大的 DFlash 推测解码更新，在单张 RTX 3090 上实现了 Gemma 4 31B 高达 4.93 倍的加速（177.8 tps）和 Qwen 3.6 27B 4.40 倍的加速（163.9 tps），而提示处理速度仍接近基线。 这一版本显著降低了在消费级 GPU 上本地运行大型语言模型的门槛，无需昂贵的数据中心硬件即可实现高速推理。这展示了先进推测解码技术对开源 LLM 社区的实际影响。 DFlash 实现包括高效的草稿 KV 缓存投影缓存、更干净的预填充处理以及更安全的 CUDA 执行。更新还增加了对 Gemma 4 31B 的完整支持（含视觉），支持 DFlash GGUF，并强化了推理和工具调用边界。

rss · r/LocalLLaMA RSS · May 22, 17:34

**背景**: BeeLlama 是 llama.cpp 的一个性能优化分支，增加了 DFlash 推测解码、自适应草稿控制、TurboQuant KV 缓存压缩和推理循环保护。推测解码使用轻量级草稿模型提出多个标记，目标模型并行验证，从而加速生成而不损失质量。DFlash 是一种块扩散方法，可实现高效的并行草稿生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Anbeeld/beellama.cpp">GitHub - Anbeeld/beellama.cpp: DFlash & TurboQuant in llama.cpp with up ...</a></li>
<li><a href="https://z-lab.ai/projects/dflash/">DFlash : Block Diffusion for Flash Speculative Decoding - Z Lab</a></li>
<li><a href="https://huggingface.co/z-lab/Qwen3.5-9B-DFlash">z-lab/Qwen3.5-9B- DFlash · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#BeeLlama`, `#DFlash`, `#local LLM`, `#GPU acceleration`

---

<a id="item-6"></a>
## [Needle 26M 在 CPU 函数调用基准测试中击败 Qwen3-0.6B](https://www.reddit.com/r/LocalLLaMA/comments/1tljs5o/benchmarked_needle_26m_vs_qwen306b_on_cpu/) ⭐️ 8.0/10

一项在 4 核 CPU 上进行的基准测试比较了 Needle 26M（一个从 Gemini 蒸馏而来的微型专用函数调用模型）与 Qwen3-0.6B（一个通用小型模型）。尽管参数数量少 23 倍，Needle 仍以 72% 的工具匹配准确率击败 Qwen3 的 56%，并且速度快 4.4 倍（平均延迟 10.9 秒对 47.9 秒）。 这一结果表明，小型专用模型在函数调用等特定任务上可以超越大得多的模型，这对于计算和内存有限的设备端 AI 代理和边缘部署至关重要。同时，它揭示了专用模型与通用模型之间的不同失败模式，为实践者选择合适的模型架构提供了指导。 Needle 的失败主要是选择了错误工具（例如将系统命令路由到 search_web），而 Qwen3 的失败则是完全解析失败（用散文响应而非发出 <tool_call> 标签）。Needle 首轮因 schema 不匹配（OpenAI JSON Schema 与其扁平 schema）仅得 8%，转换后跃升至 72%。Qwen3 需要使用 tokenizer.apply_chat_template 并设置 enable_thinking=False，以避免消耗全部 256 个 token 的预算。

rss · r/LocalLLaMA RSS · May 23, 15:38

**背景**: 大语言模型中的函数调用是指模型输出结构化调用以触发预定义工具或 API 的能力，从而实现代理行为。模型蒸馏是一种技术，通过训练较小的学生模型模仿较大教师模型的输出，将知识压缩到更少的参数中。Needle 是一个 26M 参数的模型，专门从 Google 的 Gemini 3.1 蒸馏而来，用于函数调用，旨在高效运行在消费级 CPU 上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/ needle : 26 m function call model that runs on...</a></li>
<li><a href="https://byteiota.com/needle-26m-model-gemini-tool-calling-runs-on-devices/">Needle 26 M Model : Gemini Tool Calling Runs on Devices | byteiota</a></li>
<li><a href="https://dev.to/jtorchia/show-hn-needle-distilled-gemini-tool-calling-into-26m-parameters-technical-read-zero-hype-46jo">Show HN: Needle distilled Gemini tool calling into 26 M parameters...</a></li>

</ul>
</details>

**标签**: `#Agent Frameworks`, `#LLM Inference`, `#Function Calling`, `#Benchmark`, `#Small Models`

---

<a id="item-7"></a>
## [Pydantic AI v1.102.0 修复 SSRF 漏洞](https://github.com/pydantic/pydantic-ai/releases/tag/v1.102.0) ⭐️ 7.0/10

Pydantic AI v1.102.0 通过扩展 IPv6 过渡形式的处理，修复了 URL 验证中的一个 SSRF 漏洞，专门解决了 NAT64 和 ISATAP 地址格式可能绕过云元数据黑名单的问题。 此安全补丁对于在具有 NAT64/ISATAP 的 IPv6-only 或双栈网络上运行应用程序的用户至关重要，因为它可以防止可能暴露云元数据的服务器端请求伪造攻击。 该漏洞仅影响那些在 NAT64 或 ISATAP 配置网络上，显式将 FileUrl 的 force_download 设置为 'allow-local' 并接受不可信输入的设置；标准的双栈云虚拟机以及捆绑的集成不受影响。

github · dsfaccini · May 23, 01:02

**背景**: IPv6 过渡机制如 NAT64 和 ISATAP 通过将 IPv4 地址嵌入到 IPv6 地址中，允许仅 IPv6 主机与仅 IPv4 主机通信。这些嵌入地址可能被操纵以绕过 URL 验证黑名单，导致 SSRF 攻击。Pydantic AI 的 URL 验证之前未能完全处理这些过渡形式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NAT64">NAT64</a></li>
<li><a href="https://en.wikipedia.org/wiki/ISATAP">ISATAP</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_IPv6_transition_mechanisms">List of IPv6 transition mechanisms - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#pydantic-ai`, `#SSRF`, `#URL validation`

---

<a id="item-8"></a>
## [KanBots：开源看板，每卡片并行运行 AI 代理](https://www.kanbots.dev/) ⭐️ 7.0/10

KanBots 是一款开源桌面看板应用，允许用户在每张卡片上并行运行 AI 代理，从而实现多个独立代理同时自动执行任务。 该工具满足了软件开发中对高效多代理编排日益增长的需求，提供了本地优先、无需服务器的方案，这与现有依赖云的解决方案形成对比。它可能减少管理多个编码代理的负担。 KanBots 是本地优先的，所有数据存储在代码库旁的 .kanbots 文件夹中（SQLite 数据库、配置、工作树），无需云账户或遥测。它面向桌面使用，并与 Claude Code 和 Codex 代理等工具集成。

hackernews · vitriapp · May 22, 18:17 · [社区讨论](https://news.ycombinator.com/item?id=48239413)

**背景**: 看板是一种视觉工作流管理方法，源自丰田制造系统，旨在限制在制品并优化流程。AI 代理是能够执行编码或测试等特定任务的自主程序。代理编排则是协调多个专业化代理以完成复杂工作流。KanBots 将这些概念融合成一款桌面应用，每张看板卡片可生成一个独立的 AI 代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://firethering.com/kanbots-ai-kanban-board-claude-code-codex-agents/">KanBots: Open-Source AI Kanban Board for Claude Code... - Firethering</a></li>
<li><a href="https://departmentofproduct.substack.com/p/what-is-parallel-ai-agent-coding">What is parallel AI agent coding? An in-depth guide for product teams</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agent-orchestration">What is AI Agent Orchestration? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区成员反应不一：一些人赞赏其本地优先设计，但另一些提出了实践上的担忧。一位开发者指出审查一晚上的代理活动很困难；另一个将其与因盈利问题而被放弃的 Vibe Kanban 比较；一位评论者认为该工具违背了看板限制在制品的原则；还有人强调了监督多个代理并合并其产出的挑战。

**标签**: `#AI Agents`, `#Open Source`, `#Kanban`, `#Agent Orchestration`

---

<a id="item-9"></a>
## [AI 数据中心需求挤压消费级内存供应](https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything) ⭐️ 7.0/10

由于 AI 数据中心对 HBM 内存需求激增，内存制造商将晶圆产能从 DDR 和 LPDDR 转向 HBM，导致消费级内存供应减少，推高了智能手机等电子产品的价格。

rss · Simon Willison · May 22, 22:01

**背景**: HBM（高带宽内存）是一种用于 AI 加速器的 3D 堆叠 DRAM，具有高带宽特性。DDR 用于台式机，LPDDR 用于移动设备。晶圆产能分配决定了每种内存类型的产量。此次短缺预计至少持续到 2030 年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HBM_memory_shortage">HBM memory shortage</a></li>
<li><a href="https://semiwiki.com/wikis/semiconductor-ip-wikis/ddr-vs-lpddr-vs-hbm-wiki/">DDR vs. LPDDR vs. HBM Wiki - Semiwiki</a></li>

</ul>
</details>

**标签**: `#memory`, `#AI infrastructure`, `#hardware pricing`, `#HBM`, `#DDR`

---

<a id="item-10"></a>
## [代理 AI 代币消耗高 1000 倍，科技巨头缩减使用](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-cost-crisis-hits-tech-giants-as-employee-tokenmaxxing-backfires-agentic-ai-eats-up-to-1000x-more-tokens-than-standard-ai-sparks-corporate-pullback-at-microsoft-meta-and-amazon) ⭐️ 7.0/10

微软、Meta 和亚马逊正缩减代理 AI 的使用，原因是员工的 token 消耗量比标准 AI 高出 1000 倍，引发成本危机，使得“tokenmaxxing”策略适得其反。 这揭示了在企业中部署自主 AI 代理的根本经济障碍，可能减缓采用速度，并迫使公司重新设计 AI 工作流程以控制成本。 代理 AI 系统执行多步推理和工具调用，消耗的 token 比简单问答模型高达 1000 倍。“Tokenmaxxing”指员工最大化 AI 使用量以推高生产力指标，结果成本膨胀适得其反。

rss · Hacker News - AI & Agents · May 23, 15:03

**背景**: 代理 AI 指能自主设定目标、规划并执行复杂任务、仅需最少人工干预的系统。Token 使用量是 AI 服务的主要成本指标，每个 token 代表一个处理单元。“Tokenmaxxing”是近期趋势，员工大量使用 AI 以显得高产，但在此案例中导致了科技巨头不可持续的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Token_maxxing">Token maxxing - Wikipedia</a></li>
<li><a href="https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/">The Pulse: ‘Tokenmaxxing’ as a weird new trend - The Pragmatic Engineer</a></li>
<li><a href="https://www.hostinger.com/tutorials/what-is-agentic-ai">hostinger.com/tutorials/what-is- agentic - ai</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Cost`, `#Token Usage`, `#Enterprise AI`, `#Agentic AI`

---

<a id="item-11"></a>
## [Polsia 融资 3000 万美元，AI 自主运营 7600 家企业](https://noqta.tn/en/news/polsia-ai-autonomous-company-30m-funding-2026) ⭐️ 7.0/10

Polsia 获得了 3000 万美元融资，用于扩展其自主 AI 系统，该系统目前无需人工干预即可运营 7600 家企业。 这标志着 AI 驱动业务自动化的重要里程碑，证明智能体框架现在可以管理全规模运营，可能重塑创业方式和小企业管理。 Polsia 的 AI 系统全天候处理规划、编码和营销，已有 500 多家公司和超过 45 万美元的年经常性收入在该平台上运行。这 3000 万美元融资将加速部署和开发。

rss · Hacker News - AI & Agents · May 23, 14:56

**背景**: Polsia 是一个自主智能体平台，充当全天候的数字联合创始人，整合了战略规划、软件开发和全漏斗营销。它属于新兴的智能体框架类别——能够独立设定目标、做出决策并执行复杂任务的 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://polsia.com/">Polsia — AI That Runs Your Company While You Sleep</a></li>
<li><a href="https://moge.ai/product/polsia">Polsia : Autonomous company-operating platform that... - MOGE</a></li>
<li><a href="https://www.toolcenter.ai/en/tools/polsia">Polsia : Autonomous AI system that plans, codes, and... | ToolCenter</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Automation`, `#Funding`, `#Agentic Framework`

---

<a id="item-12"></a>
## [AMD Radeon 16GB LLM 测试仓库发布](https://www.reddit.com/r/LocalLLaMA/comments/1tl4o1m/clubrdna16_practical_16gb_amdradeon_local_llm/) ⭐️ 7.0/10

一个新的 GitHub 仓库 club-rdna16 提供了在 16GB AMD Radeon GPU 上运行大型语言模型的实用测试配置，包括精确的 llama.cpp 启动设置、上下文长度和长上下文检索检查。在 RX 6900 XT 上的早期结果表明，使用 UD-IQ3_XXS 量化和 q8 KV 缓存的 Qwen3.6 35B-A3B 模型可实现 131k 上下文长度。 该仓库填补了 AMD GPU 用户在本地 LLM 推理方面缺乏标准化、可重复基准测试的空白，而 NVIDIA 生态系统则更为成熟。它帮助社区优化消费级 AMD 硬件的模型，可能扩大本地 AI 推理的普及范围。 该仓库配置包括精确的 llama.cpp 启动命令、适合的上下文长度、KV 缓存类型（q8）、电源配置文件说明和 ROCm/HIP 设置细节。初始测试侧重于使用 Unsloth MTP GGUFs 和 UD-IQ3_XXS 量化的 Qwen3.6 模型（27B 和 35B-A3B）。

rss · r/LocalLLaMA RSS · May 23, 03:16

**背景**: llama.cpp 是一种流行的在本地运行 LLM 的 C++实现，支持包括 AMD GPU 的 ROCm 在内的多种后端。ROCm 是 AMD 的开源 GPU 计算平台，HIP 是 CUDA 代码的转换层。量化降低模型精度以适应有限显存，KV 缓存优化对长上下文推理至关重要。多令牌预测（MTP）是一种可在不损失精度的情况下将推理速度提高一倍的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF">unsloth /Qwen3.6-27B- MTP -GGUF · Hugging Face</a></li>
<li><a href="https://unsloth.ai/docs/models/qwen3.6">Qwen3.6 - How to Run Locally | Unsloth Documentation</a></li>
<li><a href="https://ollama.com/danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-IQ3_XXS">danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-IQ3_XXS</a></li>

</ul>
</details>

**标签**: `#AMD`, `#local-LLM`, `#GPU-inference`, `#llama.cpp`, `#quantization`

---

<a id="item-13"></a>
## [开发者搭建路由层，将代理成本降至 16 美元](https://www.reddit.com/r/LocalLLaMA/comments/1tljn16/16_refactor_400_steps_95_routed_to_open_moe/) ⭐️ 7.0/10

一名开发者构建了一个路由层，将简单的代理步骤定向到本地 21B 参数的 MoE 模型（Hunyuan Hy3 preview），复杂步骤交给 Opus，在 400 步的 Python 重构任务中取得了 93.4%的成功率，总成本仅 15.60 美元。 该方法展示了一种实用的代理编排成本节约策略：用本地小模型处理常规任务，将昂贵的顶尖模型保留给困难场景，可能使 AI 代理更加平价和普及。 路由层使用 vLLM 0.8 并启用 enable_auto_tool_choice，常规步骤设置 reasoning 为 no_think 使 token 消耗减少约 30%。Hunyuan Hy3 preview 是一个 295B 参数的 MoE 模型，其中 21B 活跃参数，运行在 2 块 A100 GPU 上。

rss · r/LocalLLaMA RSS · May 23, 15:33

**背景**: 混合专家（MoE）架构每 token 只激活部分参数，使大模型运行更高效。腾讯开发的 Hunyuan Hy3 preview 总参数 295B，活跃参数 21B。vLLM 是一个高吞吐推理引擎，通过 enable_auto_tool_choice 支持工具调用。这种设置允许开发者在本地模型和云端模型之间路由任务，以平衡成本和能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/stable/features/tool_calling/">Tool Calling - vLLM</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy3-preview">GitHub - Tencent- Hunyuan / Hy 3 -preview: Hy 3 preview...</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts ? | IBM</a></li>

</ul>
</details>

**标签**: `#agent orchestration`, `#cost optimization`, `#MoE`, `#vLLM`, `#routing`

---