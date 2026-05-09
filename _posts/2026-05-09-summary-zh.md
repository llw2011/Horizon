---
layout: default
title: "Horizon Summary: 2026-05-09 (ZH)"
date: 2026-05-09
lang: zh
---

> From 103 items, 15 important content pieces were selected

---

1. [Anthropic 教 Claude 理解自身的推理过程](#item-1) ⭐️ 9.0/10
2. [OpenAI Agents SDK v0.17.0: 默认模型变更和沙箱修复](#item-2) ⭐️ 8.0/10
3. [为何 HTML 优于 Markdown 用于 Claude Code 提示](#item-3) ⭐️ 8.0/10
4. [代理编码工具分析：Claude Code 与 Codex](#item-4) ⭐️ 8.0/10
5. [AI 比医生早三年发现胰腺癌](#item-5) ⭐️ 8.0/10
6. [MTP + TurboQuant 在 Qwen3.6-27B 上实现单卡 RTX 4090 80+ tokens/秒](#item-6) ⭐️ 8.0/10
7. [DeepSeek 寻求 73.5 亿美元融资，计划发布 V4.1](#item-7) ⭐️ 8.0/10
8. [Gemma 4 26B 在 RTX 5090 上通过 DFlash 实现 2.56 倍加速至 578 tok/s](#item-8) ⭐️ 8.0/10
9. [AI 正在打破两种漏洞文化](#item-9) ⭐️ 7.0/10
10. [新基准测试 AI 编码代理的记忆一致性](#item-10) ⭐️ 7.0/10
11. [AMD 的 GAIA 开源 AI 现已集成 Gmail](#item-11) ⭐️ 7.0/10
12. [亚洲 AI 战略：越南立法、日本无处罚、韩国排除 Naver](#item-12) ⭐️ 7.0/10
13. [Qwen 35B-A3B MoE 在 12GB 显存上运行良好](#item-13) ⭐️ 7.0/10
14. [AI2 发布 EMO：1B/14B MoE 模型，采用文档级路由](#item-14) ⭐️ 7.0/10
15. [DS4：专为 128GB MacBook 上的 DeepSeek 4 Flash 打造的推理引擎](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 教 Claude 理解自身的推理过程](https://www.anthropic.com/research/teaching-claude-why) ⭐️ 9.0/10

Anthropic 发表了新研究，探索如何训练 Claude 理解其自身的内部推理过程，旨在提升 AI 对齐性和可解释性。 这项工作有望带来更安全、更可控的 AI 智能体，因为能够解释其推理的模型更容易被审计并与人类价值观对齐。 该研究专注于教模型内省其推理链，并且可能推广到 Claude 之外的其他开源模型，如相关的 Model Spec Midtraining 工作所示。

hackernews · pretext · May 8, 17:59 · [社区讨论](https://news.ycombinator.com/item?id=48066592)

**背景**: AI 对齐旨在将人类价值观和目标编码到大语言模型中，使其更有帮助、更安全、更可靠。理解模型如何推理是一个关键挑战，因为当前的 LLM 往往在其决策过程中缺乏透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.ibm.com/blog/what-is-alignment-ai">What is AI alignment ? - IBM Research</a></li>
<li><a href="https://serokell.io/blog/what-is-ai-alignment">What Is AI Alignment ?</a></li>
<li><a href="https://news.mit.edu/2025/large-language-models-reason-about-diverse-data-general-way-0219">Like human brains, large language models reason about diverse data in a general way | MIT News | Massachusetts Institute of Technology</a></li>

</ul>
</details>

**社区讨论**: 评论反映了哲学对齐关切和技术兴趣的混合。用户质疑对齐的模型是否仍可能造成社会危害，而另一些人则将对齐视为一个教学挑战。一些人指出相关的开源权重研究是互补的。

**标签**: `#AI alignment`, `#Anthropic`, `#LLM reasoning`, `#AI safety`, `#agentic AI`

---

<a id="item-2"></a>
## [OpenAI Agents SDK v0.17.0: 默认模型变更和沙箱修复](https://github.com/openai/openai-agents-python/releases/tag/v0.17.0) ⭐️ 8.0/10

OpenAI 发布了 openai-agents-python SDK 的 v0.17.0 版本，将 RealtimeAgent 的默认模型从之前的版本改为 gpt-realtime-2。该版本还收紧了沙箱本地源代码物化规则，禁止复制基目录之外的文件，除非显式授权。 此次更新意义重大，因为 gpt-realtime-2 提供了 GPT-5 级别的推理能力和改进的音频理解能力，增强了语音代理的功能。沙箱安全修复堵住了主机文件可能被无意暴露给沙箱环境的潜在漏洞。 gpt-realtime-2 模型支持 128K 上下文、五级推理和并行工具调用，在基准测试中相比前代有显著提升。沙箱变更要求开发者对 SDK 进程当前工作目录之外的主机路径使用 SandboxPathGrant，并建议只读访问。

github · seratch · May 8, 08:09

**背景**: OpenAI Agents SDK 是一个用于构建 AI 代理的 Python 工具包，具有工具使用、交接和沙箱环境等功能。RealtimeAgent 是通过 WebSocket 传输使用 Realtime API 进行低延迟语音交互的专用代理。沙箱物化是指将本地文件复制到沙箱环境中供代理任务使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.github.io/openai-agents-python/ref/realtime/agent/">RealtimeAgent - OpenAI Agents SDK</a></li>
<li><a href="https://openai.github.io/openai-agents-python/sandbox/guide/">Concepts - OpenAI Agents SDK</a></li>
<li><a href="https://awesomeagents.ai/models/gpt-realtime-2/">GPT - Realtime - 2 | Awesome Agents</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#agents-sdk`, `#release`, `#AI agents`

---

<a id="item-3"></a>
## [为何 HTML 优于 Markdown 用于 Claude Code 提示](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/#atom-everything) ⭐️ 8.0/10

Anthropic Claude Code 团队的 Thariq Shihipar 倡导在提示 Claude 时请求 HTML 输出而非 Markdown，并提供了具体示例和提示模板。Simon Willison 用 GPT-5.5 测试了该方法，以解释一个 Linux 漏洞，生成了包含交互元素的丰富 HTML 页面。 这种提示工程的转变能显著提升 AI 生成解释的质量，通过实现更丰富的格式、内联图表和交互式小部件，尤其有利于 agentic 编码工作流。它挑战了长期以来因 token 效率而偏爱 Markdown 的习惯，提供了一种更有效的传递复杂信息的方式。 文章推荐了诸如“帮我通过创建一个 HTML 制品来审查这个 PR”之类的提示，并附带了一个示例网站。Simon 使用 GPT-5.5 对 copy.fail 漏洞进行的测试生成了一个带有黄色边框安全提示和编号步骤的 HTML 页面，但输出更侧重于 Python 脚本框架而非漏洞本身，凸显了精确指令的必要性。

rss · Simon Willison · May 8, 21:00

**背景**: Claude Code 是 Anthropic 为开发者提供的 agentic 编码工具，允许 AI 理解代码库、编辑文件和运行命令。历史上，Markdown 因 token 效率高而被偏好用于 LLM 输出，尤其是在 GPT-4 时代上下文窗口有限的情况下。HTML 虽然 token 消耗更多，但提供了更丰富的格式化能力，如 SVG 图表、页面内导航和交互式小部件，使其更适用于复杂解释。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#LLM prompting`, `#HTML`, `#agentic workflows`, `#prompt engineering`

---

<a id="item-4"></a>
## [代理编码工具分析：Claude Code 与 Codex](https://thezvi.substack.com/p/claude-code-codex-and-agentic-coding-f54) ⭐️ 8.0/10

本文分析了 Claude Code、Codex 及其他代理编码工具，讨论了它们对 AI 辅助软件开发的影响，包括其能力、局限性以及对开发者的意义。 随着代理编码工具变得越来越复杂，它们有潜力显著提高开发者的生产力并改变软件开发工作流程，因此本文的分析对于理解 AI 在编码领域的当前状态和未来方向非常有价值。 文章详细比较了 Claude Code（来自 Anthropic）和 Codex（来自 OpenAI），涵盖了它们的基础模型、代码编辑和执行能力，以及如何集成到开发者环境中。文章还讨论了这些工具的潜在风险和局限性。

rss · Hacker News - AI & Agents · May 8, 21:23

**背景**: Claude Code 是 Anthropic 开发的代理编码工具，能够理解代码库、编辑文件并运行命令。Codex 是 OpenAI 的软件工程代理，旨在帮助编码、调试和代码审查。这两种工具代表了 AI 辅助编程的新范式，代理与开发者积极协作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://openai.com/index/running-codex-safely/">Running Codex safely at OpenAI | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Agentic Coding`, `#Claude Code`, `#Codex`, `#LLM Tools`

---

<a id="item-5"></a>
## [AI 比医生早三年发现胰腺癌](https://www.reddit.com/r/artificial/comments/1t7au63/new_ai_model_spots_pancreatic_cancer_up_to_3/) ⭐️ 8.0/10

一项新的人工智能模型在临床测试中展现出比人类医生早最多三年发现胰腺癌的能力，可能实现更早的干预。 胰腺癌以早期难发现和低生存率著称；更早的检测可显著改善患者预后并降低死亡率。 该 AI 模型分析医学影像数据（如 CT 扫描或 MRI），识别人眼可能遗漏的胰腺癌细微指标。测试显示其比标准诊断提前三年发现。

rss · r/artificial RSS · May 8, 15:12

**背景**: 胰腺癌通常在晚期才出现症状，早期检测极具挑战。在大型数据集上训练的 AI 模型能学会识别与早期疾病相关的模式，为高危人群筛查提供了有前景的工具。

**标签**: `#AI`, `#healthcare`, `#pancreatic cancer`, `#machine learning`, `#medical imaging`

---

<a id="item-6"></a>
## [MTP + TurboQuant 在 Qwen3.6-27B 上实现单卡 RTX 4090 80+ tokens/秒](https://www.reddit.com/r/LocalLLaMA/comments/1t7kyju/got_mtp_turboquant_running_qwen3627b_80_ts_at/) ⭐️ 8.0/10

一位 Reddit 用户成功将多令牌预测（MTP）与 TurboQuant KV 缓存量化（TBQ4_0）集成到 Qwen3.6-27B 模型上，在单张 RTX 4090 上以 262K 上下文实现了每秒 80-87 个令牌的生成速度。 这表明将 MTP 投机解码与极端 KV 缓存量化相结合可以大幅提升消费级硬件上的推理吞吐量，使长上下文本地 LLM 推理对开发者和爱好者来说变得更加实用。 该配置使用了 Q4_K_M 量化的 Qwen3.6-27B-Heretic-v2 模型并嫁接 MTP 头部，在 Ubuntu 24.04 和 CUDA 12.x 上运行。用户报告 MTP 草稿接受率约为 73%，并已发布集成了该功能的 llama.cpp 分支。

rss · r/LocalLLaMA RSS · May 8, 21:15

**背景**: 多令牌预测（MTP）是一种投机解码技术，其中轻量级草稿模型并行预测多个未来令牌；TurboQuant 是一种将 KV 缓存近乎无损地量化为极低位宽（例如每值 4.25 比特）的方法。结合这两者可以减少内存带宽和计算开销，从而在有限硬件上实现更快的长上下文推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/20969">TurboQuant - Extreme KV Cache Quantization · ggml-org/llama.cpp · Discussion #20969</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#quantization`, `#MTP`, `#llama.cpp`, `#local LLM`

---

<a id="item-7"></a>
## [DeepSeek 寻求 73.5 亿美元融资，计划发布 V4.1](https://www.reddit.com/r/LocalLLaMA/comments/1t7bfpw/reports_suggest_deepseek_is_seeking_735_billion/) ⭐️ 8.0/10

据报 DeepSeek 正寻求首轮融资高达 735 亿美元（500 亿元人民币），并计划于 6 月发布升级版 V4.1 模型。 这将是中国 AI 公司历史上最大单轮融资，标志着 DeepSeek 加快商业化进程，与主要大模型提供商竞争。 创始人梁文锋计划在本轮中投入最高允许额度。公司拟加快模型发布节奏以符合行业惯例。

rss · r/LocalLLaMA RSS · May 8, 15:34

**背景**: DeepSeek 是一家中国 AI 初创公司，以其大语言模型（包括 V4 系列）著称。V4 模型因性能突出而备受关注。本轮融资旨在支持创收计划和快速迭代。

**标签**: `#DeepSeek`, `#funding`, `#LLM`, `#AI industry news`, `#V4.1`

---

<a id="item-8"></a>
## [Gemma 4 26B 在 RTX 5090 上通过 DFlash 实现 2.56 倍加速至 578 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1t796qe/gemma_4_26b_hits_600_toks_on_one_rtx_5090/) ⭐️ 8.0/10

一位 Reddit 用户进行的基准测试表明，在单张 RTX 5090 上使用 vLLM 中的 DFlash 推测解码，Gemma 4 26B 模型达到了每秒 578 个输出 token，相比无推测解码时的 228 tok/s 基准实现了 2.56 倍加速。 这表明先进的推测解码技术可以大幅提升消费级 GPU 上的推理吞吐量，使大型语言模型在本地部署和实时应用中更加实用。 最佳设置是 num_speculative_tokens=13 和 max_num_batched_tokens=8192，平均延迟从 4455 毫秒降至 1738 毫秒。值得注意的是，最快的平均设置并非总是对服务最优，更大的批次大小（8192 对比 4096）改善了尾部延迟。

rss · r/LocalLLaMA RSS · May 8, 14:13

**背景**: 推测解码是一种技术，先由一个小而快的草稿模型并行提出多个 token，再由更大的目标模型并行验证，从而在保证质量的前提下实现高达 2-3 倍的加速。DFlash 是一种专为轻量级推测起草设计的新型块扩散模型。vLLM 是一个高吞吐量推理引擎，支持包括 DFlash 在内的多种推测解码方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z-lab.ai/projects/dflash/">DFlash : Block Diffusion for Flash Speculative Decoding - Z Lab</a></li>
<li><a href="https://github.com/z-lab/dflash">z-lab/ dflash : DFlash : Block Diffusion for Flash Speculative Decoding ...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/">Speculative Decoding - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#speculative decoding`, `#Gemma 4`, `#RTX 5090`, `#LLM inference`

---

<a id="item-9"></a>
## [AI 正在打破两种漏洞文化](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures) ⭐️ 7.0/10

AI 正在加速漏洞利用代码的生成，并重塑漏洞披露实践，暴露出全披露与协调补丁之间原有的紧张关系。 这可能会缩短披露窗口，使小型组织更难及时修补，并可能从根本上改变开源安全生态系统。 文章认为，AI 能够从补丁或描述中快速生成漏洞利用代码，实际上消除了协调披露的保护窗口，迫使人们在透明性与安全性之间做出抉择。

hackernews · speckx · May 8, 17:55 · [社区讨论](https://news.ycombinator.com/item?id=48066524)

**背景**: 协调漏洞披露（CVD）是一种模型，研究人员私下通知厂商，在公开披露前留出修补时间。全披露则立即发布细节。AI 从少量信息生成可用漏洞利用的能力削弱了协调模型，因为攻击者现在可以在补丁部署之前利用漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure</a></li>

</ul>
</details>

**社区讨论**: tptacek 指出这一转变早已被预见，主要驱动力是软件透明度和逆向工具，而不仅仅是 LLM。freeqaz 以 Log4Shell 为例，说明监测提交会导致攻击。rikafurude21 认为这是旧问题被重新包装，便宜的漏洞利用生成反而可能使协调披露更重要。dmurray 讽刺地建议 Linux 转向闭源模式。

**标签**: `#AI security`, `#vulnerability disclosure`, `#open source`, `#cybersecurity`, `#LLM impact`

---

<a id="item-10"></a>
## [新基准测试 AI 编码代理的记忆一致性](https://www.reddit.com/r/artificial/comments/1t7m8bg/i_built_a_benchmark_for_ai_memory_in_coding/) ⭐️ 7.0/10

一名开发者发布了名为 Continuity Benchmarks 的新基准测试，专门评估 AI 编码代理在任务执行过程中保持项目规则一致性的能力，而非仅仅测量语义回忆。早期结果显示，与基线 RAG 风格内存方案相比，动作对齐提升约 3 倍，多会话一致性显著增强。 现有的 AI 代理基准测试忽略了一个关键失败模式：编码代理在工作过程中经常违反自己之前的决策。该基准填补了这一空白，为代理内存系统提供了标准化比较方法，对于构建可靠的长期运行编码代理至关重要。 该基准检查编辑是否尊重早期架构决策、行为在多会话（含噪声）中是否一致，以及检索是否在正确时机触发。完整的测试框架、数据集和评分方法可在 GitHub 上获取：github.com/Alienfader/continuity-benchmarks。

rss · r/artificial RSS · May 8, 22:05

**背景**: AI 编码代理使用大型语言模型在多步骤中生成和修改代码。现有的大多数内存基准测试主要测试语义回忆（即基于 RAG 的相关信息搜索），但并未测试代理在活跃开发过程中是否与自身过去的决策保持一致。这个新基准专注于行动一致性——一个此前被广泛忽视的维度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-agent-memory/">Agents that remember: introducing Agent Memory</a></li>
<li><a href="https://www.letta.com/blog/benchmarking-ai-agent-memory">Benchmarking AI Agent Memory: Is a Filesystem All You Need? | Letta</a></li>

</ul>
</details>

**标签**: `#coding agents`, `#memory benchmark`, `#AI agents`, `#consistency`, `#evaluation`

---

<a id="item-11"></a>
## [AMD 的 GAIA 开源 AI 现已集成 Gmail](https://www.reddit.com/r/artificial/comments/1t77n9a/amds_local_opensource_ai_can_now_easily_interact/) ⭐️ 7.0/10

AMD 的 GAIA 框架 v0.15 版本现已通过代理工具集成 Gmail，使本地 AI 能够读取和发送电子邮件，同时保护数据隐私。 这实现了在本地硬件上进行隐私保护的电子邮件自动化，减少了对云端 AI 的依赖，并为 AMD 的 Ryzen AI PC 提供了独特的卖点。 GAIA 是一个用于构建 AI PC 代理的开源 SDK，可在 Ryzen AI NPU 上本地运行大语言模型。Gmail 集成通过 GAIA 的代理框架与 Gmail API 交互，同时保持所有处理在设备本地进行。

rss · r/artificial RSS · May 8, 13:15

**背景**: GAIA 是 AMD 的一个开源项目，旨在利用神经处理单元（NPU）在 Ryzen AI PC 上本地运行大语言模型。最初专注于 LLM 推理，后来 GAIA 演变为具有工具使用能力的代理框架。v0.15 版本于 2026 年 1 月与 CES 公告一同发布，新增了 Gmail 集成作为改进代理用户体验的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/amd-gaia">AMD GAIA</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/gaia-an-open-source-project-from-amd-for-running-local-llms-on-ryzen-ai.html">GAIA : An Open-Source Project from AMD for Running Local LLMs on...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#open-source`, `#AMD`, `#local AI`, `#email integration`

---

<a id="item-12"></a>
## [亚洲 AI 战略：越南立法、日本无处罚、韩国排除 Naver](https://www.reddit.com/r/artificial/comments/1t7h9gt/compiled_every_national_ai_strategy_in_asia/) ⭐️ 7.0/10

Reddit 上的一篇帖子汇编了亚洲各国的 AI 战略，重点介绍了越南的独立 AI 法（2026 年 3 月生效）、日本的无处罚 AI 促进法，以及韩国因使用 Qwen 权重而将 Naver 排除在主权大语言模型竞争之外。帖子指出，多数亚洲政府采取促进性而非惩罚性策略。 这份概述揭示了亚洲独特的 AI 治理范式——侧重于激励和主权能力，而非严格监管，可能影响全球 AI 政策走向。因 Qwen 权重排除 Naver 一事，凸显了开源模型与 AI 开发中国家主权之间的紧张关系。 越南 AI 法共 36 条，采用三层风险分类，罚款最高可达年收入的 2%。日本法律无处罚条款，旨在缩小采用差距（仅 9%的个人使用生成式 AI）。中国的开源产业政策已导致 Hugging Face 上出现超过 10 万个 Qwen 衍生模型。

rss · r/artificial RSS · May 8, 19:00

**背景**: 主权大语言模型是利用国内基础设施构建的国家级 AI 模型，以确保战略自主。Qwen 是阿里巴巴的开源权重模型系列，已被广泛微调和采用。欧盟 AI 法案采用事前风险分级方法并设有处罚，与亚洲的促进性立场形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#National AI Strategy`, `#Asia`, `#Regulation`, `#Open Source`

---

<a id="item-13"></a>
## [Qwen 35B-A3B MoE 在 12GB 显存上运行良好](https://www.reddit.com/r/LocalLLaMA/comments/1t7l56a/qwen_35ba3b_is_very_usable_with_12gb_of_vram/) ⭐️ 7.0/10

一位 Reddit 用户分享了详细基准测试，显示 Qwen 35B-A3B 混合专家模型（量化为 4 位 IQ4_XS）在 12GB 显存的 RTX 3060 上运行切实可行，预填充速度约 914 tokens/s，普通解码约 46.8 tokens/s，并支持 32k 上下文。 这表明总参数达 35B 的混合专家模型可以在仅 12GB 显存的消费级 GPU 上运行，使高质量本地 LLM 推理对没有昂贵硬件的开发者和爱好者更加可及。 该模型使用 IQ4_XS 量化，需要仔细调整`-ncmoe`参数以在 GPU 上保留足够多的 MoE 专家；安全解码的最佳点设为`-ncmoe 18`，32k 上下文设为`-ncmoe 20`，而`-ctk q8_0 -ctv q8_0` KV 缓存量化几乎无性能损失。

rss · r/LocalLLaMA RSS · May 8, 21:22

**背景**: 混合专家（MoE）是一种神经网络架构，每个 token 只激活一部分“专家”子网络，从而减少计算量。Qwen 35B-A3B 模型总参数 35B，但每个 token 仅激活约 3B 参数，效率更高。量化通过减少每个权重的位数来缩小模型大小；IQ4_XS 是一种 4 位格式，使用重要性矩阵保持精度。llama.cpp 是一个推理引擎，支持多种量化和卸载策略，包括控制多少 MoE 层卸载到 GPU 的`-ncmoe`参数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/issues/15263">Feature Request: --n-cpu-moe option for multi GPU? · Issue #15263 · ggml-org/llama.cpp</a></li>
<li><a href="https://huggingface.co/blog/Doctor-Shotgun/llamacpp-moe-offload-guide">Performant local mixture-of-experts CPU inference with GPU acceleration in llama.cpp</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#Qwen`, `#MoE`, `#VRAM`, `#local deployment`

---

<a id="item-14"></a>
## [AI2 发布 EMO：1B/14B MoE 模型，采用文档级路由](https://www.reddit.com/r/LocalLLaMA/comments/1t7kgy4/new_moe_from_ai2_emo/) ⭐️ 7.0/10

AI2 发布了 EMO，这是一个混合专家模型，具有 10 亿活跃参数和 140 亿总参数，在 1 万亿 token 上训练。它引入了文档级路由，专家按领域（如健康、新闻）进行聚类，而非按表面模式。 这项工作展示了 MoE 模型中专家专业化的新颖方法，通过按语义分组专家，可能提高效率和可解释性。它可能影响未来大型语言模型的 MoE 设计，特别是在特定领域的应用中。 EMO 使用 top-2 路由和容量因子，文档级路由通过将整个文档分配给同一组专家来实现。该模型是开源的，可在 Hugging Face 上获取，包括检查点和代码。

rss · r/LocalLLaMA RSS · May 8, 20:57

**背景**: 混合专家（MoE）是一种神经网络架构，使用多个'专家'子网络和路由机制，每个输入只激活部分专家，从而在较低计算成本下实现大模型容量。传统 MoE 路由在每个 token 上操作，通常使专家围绕句法模式聚类。而 EMO 中的文档级路由旨在通过一致地路由整个文档来学习更语义化的专家专业化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoE`, `#AI2`, `#routing`, `#open-source`

---

<a id="item-15"></a>
## [DS4：专为 128GB MacBook 上的 DeepSeek 4 Flash 打造的推理引擎](https://www.reddit.com/r/LocalLLaMA/comments/1t72tk9/ds4_a_deepseek_4_flash_specific_inference_engine/) ⭐️ 7.0/10

Redis 的创建者 antirez 发布了 DS4，这是一个专为在 128GB MacBook（Apple Silicon）上运行 DeepSeek V4 Flash 而优化的开源推理引擎。 DS4 使得在消费级硬件上本地运行 284B 参数的 MoE 模型成为可能，从而民主化地提供了对大规模 AI 的访问，减少了对云服务的依赖。 DeepSeek V4 Flash 总参数量为 284B，但每个 token 仅激活 13B 参数，并支持 1M token 的上下文窗口。DS4 针对高端 MacBook 的 128GB 统一内存进行了定制，利用了其 CPU-GPU 共享内存架构。

rss · r/LocalLLaMA RSS · May 8, 09:26

**背景**: 大型语言模型通常需要高端 GPU 和充足的显存，但像 DeepSeek V4 Flash 这样的模型采用混合专家（MoE）架构来减少活跃参数。搭载 Apple Silicon 的 MacBook 使用统一内存，使 CPU 和 GPU 能够访问同一 RAM 池，可以将大型模型完全装入内存。由于通用框架可能无法充分利用该硬件，因此需要一个专门的推理引擎来高效地加载和运行模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek -V 4 - Flash · Hugging Face</a></li>
<li><a href="https://ollama.com/library/deepseek-v4-flash">deepseek -v 4 - flash</a></li>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-flash">deepseek -v 4 - flash Model by Deepseek -ai | NVIDIA NIM</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#DeepSeek`, `#Mac`, `#local AI`, `#open-source`

---