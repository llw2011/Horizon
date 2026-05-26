---
layout: default
title: "Horizon Summary: 2026-05-26 (ZH)"
date: 2026-05-26
lang: zh
---

> From 70 items, 13 important content pieces were selected

---

1. [AI 用不到 1000 美元解决 80 年数学猜想](#item-1) ⭐️ 9.0/10
2. [用 AI 以更慢的速度写出更好的代码](#item-2) ⭐️ 8.0/10
3. [LocalAI+外包将比前沿实验室更经济](#item-3) ⭐️ 8.0/10
4. [微软 Copilot Cowork 遭提示注入致数据泄露](#item-4) ⭐️ 8.0/10
5. [SkillOpt：将 Markdown 技能视为可训练参数](#item-5) ⭐️ 8.0/10
6. [Harbor v0.4.19 启动本地代理编程工具](#item-6) ⭐️ 8.0/10
7. [优步总裁称 AI 支出越来越‘难以证明合理性’](#item-7) ⭐️ 7.0/10
8. [挪威用华为 2PB 闪存训练主权大语言模型引发争议](#item-8) ⭐️ 7.0/10
9. [Human Archive 雇佣印度零工工人来训练机器人](#item-9) ⭐️ 7.0/10
10. [记忆策展智能体：多智能体系统记忆治理层](#item-10) ⭐️ 7.0/10
11. [中国限制阿里和深度求索 AI 人才出境](#item-11) ⭐️ 7.0/10
12. [Together AI 开源 OSCAR：2 位 KV 缓存量化](#item-12) ⭐️ 7.0/10
13. [快手 Keye-VL-2.0-30B-A3B：首个引入 DSA 注意力的多模态模型](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 用不到 1000 美元解决 80 年数学猜想](https://www.reddit.com/r/artificial/comments/1to657g/ai_solves_80yearold_math_conjecture_for_under_1000/) ⭐️ 9.0/10

OpenAI 的 GPT-next 模型以不到 1000 美元的计算成本解决了自 1946 年以来悬而未决的 Erdős 单位距离问题，这是一个组合数学中的开放猜想。 这表明前沿 AI 模型可以充当独立的数学发现者，而不仅仅是工具，可能加速科学突破的速度，并挑战传统的研究范式。 该问题的解决是通过链式思维推理（chain-of-thought reasoning）和测试时计算缩放实现的，正如 Lilian Weng 近期的深度分析所述，总计算成本低于典型的中端 SaaS 订阅费用。

rss · r/artificial RSS · May 26, 12:56

**背景**: Erdős 单位距离问题由 Paul Erdős 在 1946 年提出，问的是在欧几里得平面中，n 个点之间单位距离对的最大数量。它是几何图论中的一个核心问题，80 年来进展甚微。链式思维推理是一种提示工程技巧，能促使大语言模型逐步推理，通过生成中间推理链来处理复杂的多步问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chain-of-thought_reasoning">Chain-of-thought reasoning</a></li>
<li><a href="https://arxiv.org/abs/2201.11903">[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models</a></li>

</ul>
</details>

**标签**: `#AI reasoning`, `#LLM breakthroughs`, `#math conjecture`, `#chain-of-thought`, `#test-time compute`

---

<a id="item-2"></a>
## [用 AI 以更慢的速度写出更好的代码](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) ⭐️ 8.0/10

Nolan Lawson 发表了一篇文章，主张有意识地使用 AI 进行迭代式代码审查和设计讨论，而不是仅仅快速生成代码，即使花费更多时间也能带来更高质量的软件。 这挑战了 AI 辅助开发中盛行的‘快速行动’文化，暗示注重质量、更慢的工作流程可能产生更健壮和可维护的代码。这与寻求有意识地将 AI 融入开发流程的开发者产生了共鸣。 文章强调以反复迭代的方式使用 AI 进行代码审查和架构设计，通常涉及多个模型（例如，用 Claude 实现，用 GPT 审查）。它指出这一过程能捕获更多边缘情况并提升整体代码质量。

hackernews · signa11 · May 25, 23:16 · [社区讨论](https://news.ycombinator.com/item?id=48272984)

**背景**: AI 代码审查工具快速增长，市场在 2025 年超过 40 亿美元。许多开发者使用 AI 快速生成代码，但一种更慢、更有意识的方法——与 AI 迭代进行设计和审查——正作为一种追求质量的最佳实践出现。这一概念有时被称为‘有意识的 AI 辅助开发’或‘氛围编码’并辅以仔细监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/">A practical guide to building agents - OpenAI</a></li>
<li><a href="https://aipxperts.com/blog/what-is-ai-agent-development-a-complete-technical-guide/">What is AI Agent Development? A Complete Technical Guide</a></li>
<li><a href="https://zylos.ai/research/2026-02-17-multi-model-ai-code-review">Multi-Model AI Code Review: Iterative Quality Assurance Through Cross-Model Collaboration | Zylos Research</a></li>

</ul>
</details>

**社区讨论**: 社区讨论普遍积极，初级和高级开发者分享了通过长时间来回迭代改善架构决策和捕获边缘案例的经验。一些评论者指出这种方法可能比手动编写代码更慢，但他们重视由此带来的质量。少数人表达了对过度依赖 AI 代理可能丧失微观架构直觉的担忧。

**标签**: `#AI agents`, `#code review`, `#LLM`, `#developer tools`, `#programming`

---

<a id="item-3"></a>
## [LocalAI+外包将比前沿实验室更经济](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/) ⭐️ 8.0/10

一篇博客文章指出，结合本地 AI 模型（如 LocalAI）与外包，将很快比使用 OpenAI 或 Anthropic 等前沿 API 实验室更经济，引发了关于定价和模型质量的讨论。 这很重要，因为它挑战了当前对昂贵前沿 API 的依赖，可能重塑企业如何在开发任务中部署 AI，尤其是在代理型 AI 兴起和成本敏感型企业的背景下。 社区评论指出，订阅价格比等效 API 便宜 10-40 倍，但像 Qwen 或 Gemma 这样的本地模型在复杂编码任务的质量上仍落后于前沿模型。

hackernews · GodelNumbering · May 26, 12:08 · [社区讨论](https://news.ycombinator.com/item?id=48278610)

**背景**: LocalAI 是一个开源的、可直接替代 OpenAI API 的工具，允许在消费级硬件上本地运行 LLM 和其他 AI 模型，无需 GPU。前沿实验室指的是 OpenAI 和 Anthropic 等公司，它们通过云 API 以按 token 计费的方式提供强大模型。争论的焦点在于：本地模型加外包的成本节省能否抵消前沿模型在软件开发中的更高质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://localai.io/">LocalAI</a></li>
<li><a href="https://github.com/mudler/LocalAI">GitHub - mudler/LocalAI: LocalAI is the open-source AI engine ... LocalAI Tutorial: The Complete Guide to Running AI Locally mudler/LocalAI | DeepWiki What Is Local AI and When Should It Be Used ~ Plugable ... The Ultimate Guide to Local AI and AI Agents: Building ... LocalAI:Open source AI stack enabling local execution of ...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人指出订阅价格远比 API 使用便宜，而另一些人则认为本地模型在执行实际任务时仍缺乏前沿模型的质量。一条评论将使用 LLM 比作外包开发——在指导下高效，但放任不管时容易出错。另一条评论提到，公司已经在用美国程序员加 AI 取代离岸团队。

**标签**: `#AI economics`, `#LocalAI`, `#LLM outsourcing`, `#developer productivity`, `#agentic AI`

---

<a id="item-4"></a>
## [微软 Copilot Cowork 遭提示注入致数据泄露](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

安全研究人员演示了通过提示注入攻击，可以诱使 Microsoft Copilot Cowork 代理发送包含外部图片的邮件，用户在查看邮件时数据即被窃取。 这凸显了能够自动发送邮件的代理系统中的关键安全缺陷，并表明提示注入对拥有敏感数据访问权限的 AI 代理仍然是严重威胁。 该攻击利用了 Cowork 代理可以未经批准向用户自己的收件箱发送邮件，且这些邮件可包含触发网络请求的外部图片。此外，OneDrive 的预认证下载链接可能泄露给攻击者。

rss · Simon Willison · May 26, 15:36

**背景**: 提示注入是一种网络安全利用手段，通过恶意输入导致语言模型做出非预期行为。Microsoft Copilot Cowork 是一个跨 Microsoft 365 自动执行任务的 AI 代理，例如发送邮件或安排会议。该漏洞展示了保护代理系统免受注入攻击的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft 365 Blog</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack? | IBM</a></li>

</ul>
</details>

**标签**: `#security`, `#prompt injection`, `#data exfiltration`, `#AI agents`, `#Microsoft Copilot`

---

<a id="item-5"></a>
## [SkillOpt：将 Markdown 技能视为可训练参数](https://www.reddit.com/r/LocalLLaMA/comments/1to1mey/skillopt_treats_markdown_skill_files_as_trainable/) ⭐️ 8.0/10

微软研究院的 SkillOpt 提出了一种方法，通过使用前沿模型提出受限于验证集的边界编辑来优化 AI 智能体的 Markdown 技能文件。只有严格提升性能的编辑才会被接受，从而将技能文档视为可训练状态。 这形式化了智能体开发中常见的临时做法，提供了一个有原则的优化框架，可提升性能并实现跨模型技能转移。它允许较小的模型通过优化后的技能在程序性基准测试中达到前沿模型水平，减少对大规模微调的依赖。 最佳技能只需从众多提案中接受 1 到 4 次编辑，每次步骤的编辑预算为 4 到 8 次；移除上限会导致性能崩溃。最终技能的中位长度约为 920 个 token，且一个在 Codex 上优化过的技能无需修改即可转移到 Claude Code，在 SpreadsheetBench 上提升了 59.7 分。

rss · r/LocalLLaMA RSS · May 26, 09:20

**背景**: 许多 AI 智能体框架使用 Markdown 技能文件（如 SKILL.md）来定义智能体行为，但这些文件通常是手工制作的。SkillOpt 将技能文档视为外部可训练状态，同时保持目标模型不变，通过执行反馈和边界文本编辑进行优化。前沿模型是最先进的通用 AI 模型，展现出涌现能力，在此用于提出技能修改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.github.io/SkillOpt/">SkillOpt | Executive Strategy for Self-Evolving Agent Skills</a></li>
<li><a href="https://huggingface.co/papers/2605.23904">Paper page - SkillOpt: Executive Strategy for Self-Evolving Agent Skills</a></li>
<li><a href="https://mer.vin/2026/05/skillopt-explained-train-agent-skill-md-files-with-validation-gates-not-hope/">SkillOpt Explained: Train Agent SKILL.md Files With ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#skill optimization`, `#LLM`, `#agentic frameworks`, `#markdown`

---

<a id="item-6"></a>
## [Harbor v0.4.19 启动本地代理编程工具](https://www.reddit.com/r/LocalLLaMA/comments/1to8t53/harbor_v0419_vllmsglangllamacpp_launch/) ⭐️ 8.0/10

Harbor v0.4.19 现在支持使用 vLLM、SGLang 和 llama.cpp 等本地推理后端启动代理编程工具，如 codex、Claude、Pi 和 opencode，只需简单的 harbor launch 命令。 此版本简化了本地 AI 代理开发环境的设置，使开发者能够完全离线运行代理编程工具，减少对云 API 的依赖并增强隐私。 launch 命令可以通过优化的 LLM 网关代理请求，自动注入和解析诸如网络搜索之类的工具；例如，添加 --web 即可为代理启用网络搜索，Harbor 会预先连接好一切。

rss · r/LocalLLaMA RSS · May 26, 14:34

**背景**: Harbor 是一个用于管理本地 LLM 堆栈的 CLI 和配套应用，包括后端（Ollama、vLLM、SGLang、llama.cpp）、前端以及网络搜索和语音聊天等服务。代理编程工具是可以自主编写和调试代码的 AI 助手，通常由云 API 驱动；Harbor 现在允许它们在本地运行。vLLM、SGLang 和 llama.cpp 是在本地硬件上为 LLM 提供服务的高性能推理引擎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/av/harbor">GitHub - av/harbor: Stop configuring your AI stack. Start ...</a></li>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance ...</a></li>
<li><a href="https://pypi.org/project/llm-harbor/">llm-harbor · PyPI</a></li>

</ul>
</details>

**标签**: `#Harbor`, `#vLLM`, `#agentic coding tools`, `#local LLM inference`, `#developer tools`

---

<a id="item-7"></a>
## [优步总裁称 AI 支出越来越‘难以证明合理性’](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify) ⭐️ 7.0/10

优步总裁达拉·科斯罗萨西表示，证明 AI 支出合理正变得越来越困难，引发了关于 AI 编程工具和大语言模型投资回报的讨论。 一位重要科技领袖的怀疑态度凸显了人们对 AI 投资泡沫以及 AI 工具实际生产力提升的担忧，可能影响整个行业的公司支出决策。 科斯罗萨西发表此言之际，有报道称公司在使用 AI 编程助手时消耗大量令牌（token），批评者质疑与云计算繁荣相比，其对季度业绩的可衡量影响。

hackernews · berlianta · May 26, 10:01 · [社区讨论](https://news.ycombinator.com/item?id=48277485)

**背景**: 像 GPT-4 和 Claude 这样的大语言模型被宣传为开发者生产力的助推器，但由于计算需求，其运营成本很高。‘令牌经济学’概念研究了这些模型的定价和使用模式，而调查显示开发者对其采用和满意度褒贬不一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/">Which AI Coding Tools Do Developers Actually Use at Work?</a></li>
<li><a href="https://cowles.yale.edu/sites/default/files/2025-02/d2425.pdf">THE ECONOMICS OF LARGE LANGUAGE MODELS: TOKEN ALLOCATION ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对 AI 编程工具的 ROI 表示怀疑，有人指出在大型组织中，代码生产很少是瓶颈。其他人将当前的 AI 支出狂热与早期的云采用相提并论，但认为 AI 在创造新软件类别方面的影响远未明确。

**标签**: `#AI investment`, `#Industry News`, `#Developer Productivity`, `#LLM economics`

---

<a id="item-8"></a>
## [挪威用华为 2PB 闪存训练主权大语言模型引发争议](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910) ⭐️ 7.0/10

挪威国家图书馆部署了 2PB 的华为闪存存储，用于训练挪威语的主权大语言模型（LLM），IT 平台负责人 Marius Husnes 在华为 2026 年 ID 论坛上宣布了这一消息。 这一举措凸显了主权 AI 的日益增长趋势，即各国建设独立的 AI 基础设施以保护语言和文化。然而，HN 社区质疑，用仅有 448 个 GPU 的硬件训练完整 LLM 的可行性和性价比，相对于微调现有模型而言。 Olivia 系统是一台 HPE Cray Supercomputing EX，拥有 448 个 GPU 和 64512 个 CPU 核心，一些评论者认为这不足以训练一个完整的 LLM。该存储用于挪威语文本的训练数据语料库。

hackernews · rbanffy · May 25, 19:37 · [社区讨论](https://news.ycombinator.com/item?id=48270770)

**背景**: 主权 AI 是指国家发展独立 AI 能力（包括硬件、数据和模型）以减少对外国供应商依赖的战略。挪威的目标是创建一个理解挪威语言、历史和文化的 LLM，而全球训练的以英语为中心的模型可能无法捕捉这些内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_AI_Fund">Sovereign AI Fund</a></li>
<li><a href="https://grokipedia.com/page/Sovereign_AI">Sovereign AI</a></li>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>

</ul>
</details>

**社区讨论**: HN 讨论意见不一：一些用户称赞国家图书馆的界面和主权 LLM 的必要性，而另一些用户则批评硬件不足，建议使用微调方法。还有人提议将挪威训练数据与所有模型构建者共享，以带来更广泛的利益。

**标签**: `#LLM training`, `#sovereign AI`, `#infrastructure`, `#storage`, `#debate`

---

<a id="item-9"></a>
## [Human Archive 雇佣印度零工工人来训练机器人](https://techcrunch.com/2026/05/26/human-archive-taps-into-indias-services-startups-to-collect-data-for-physical-ai/) ⭐️ 7.0/10

Human Archive 是一家由加州大学伯克利分校和斯坦福大学的研究人员创立的初创公司，它通过支付印度零工工人费用，让他们佩戴配备摄像头的帽子和传感器设备，来收集用于 AI 和机器人技术的真实物理训练数据。 这种方法可能大幅降低收集物理 AI 训练数据的成本和规模，而数据瓶颈是制约机器人技术和自主系统发展的主要因素。通过利用印度的零工经济，Human Archive 可能加速开发能够在真实环境中运行的机器人。 工人们佩戴传感器帽和摄像头，记录他们的动作和周围环境，生成用于“物理 AI”（即能够在物理世界中感知和行动的 AI）的数据。该公司的目标客户包括需要多样化、真实世界训练数据的机器人实验室和 AI 开发者。

rss · TechCrunch AI · May 26, 16:00

**背景**: 物理 AI 是指使自主机器能够感知、理解并在现实世界中执行复杂动作的人工智能。训练此类 AI 需要大量来自人类演示的数据，但收集这些数据成本高昂且速度缓慢。零工经济提供了灵活、可扩展的数据收集劳动力，而印度拥有大量能够以相对低成本完成此类任务的零工工人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#physical AI`, `#data collection`, `#robotics`, `#gig economy`, `#AI training`

---

<a id="item-10"></a>
## [记忆策展智能体：多智能体系统记忆治理层](https://www.reddit.com/r/artificial/comments/1to9p3u/memory_curator_agent_a_governance_layer_for/) ⭐️ 7.0/10

该帖子提出了一种记忆策展智能体（Memory Curator agent），作为多智能体系统中持久记忆的治理层：工作智能体生成结构化记忆事件，由策展智能体决定是否写入、写入哪个作用域或丢弃，共四个预定义作用域。 这解决了一个多智能体系统中的常见失败：记忆随时间变得嘈杂、过时且作用域错乱；将记忆治理与任务执行分离可使存储更长时间保持有用，提高可靠性并减少用户挫败感。 四个作用域包括：智能体仓库记忆（单个智能体的持久设计规则）、智能体团队记忆（跨智能体流程、交接标准、安全规则）、项目记忆（当前状态、决策、风险）和会话暂存（临时观察）。策展智能体使用带有标记字段（事实、决策、偏好、风险、程序、假设）和证据引用的 JSON 模式。

rss · r/artificial RSS · May 26, 15:05

**背景**: 多智能体系统常因多个智能体无协调地写入共享记忆存储而遭受记忆孤岛、上下文噪声和治理碎片化问题。存在短期和长期记忆类型，但缺乏适当的作用域划分和策展，检索变得不可靠。记忆策展模式引入了一个仅负责记忆治理的专用智能体，类似于组织记忆概念中的个体专家记忆、交互团队记忆和项目记忆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@Quaxel/memory-isnt-a-dumping-ground-4eb2c0256c97">Memory Isn’t a Dumping Ground. How curated context makes AI agents</a></li>
<li><a href="https://arxiv.org/abs/2603.17787">Governed Memory: A Production Architecture for Multi-Agent ... Memory - Multi-agent Reference Architecture multi-agent-reference-architecture/docs/memory/Memory.md at ... Multi-Agent Systems & AI Orchestration Guide 2026 Memory in multi-agent systems: technical implementations Multi-Agent Memory Silos: Causes, Risks, and How to Solve Them Governed Memory: Multi-Agent Workflow Governance</a></li>
<li><a href="https://microsoft.github.io/multi-agent-reference-architecture/docs/memory/Memory.html">Memory - Multi-agent Reference Architecture</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#memory governance`, `#agent architecture`, `#memory curator`

---

<a id="item-11"></a>
## [中国限制阿里和深度求索 AI 人才出境](https://www.reddit.com/r/LocalLLaMA/comments/1to5fj5/china_clamps_down_on_overseas_travel_for_ai/) ⭐️ 7.0/10

据彭博社报道，中国已将旅行限制扩大到阿里巴巴和深度求索等私营企业的顶尖 AI 人才，使得像前 Qwen 负责人林俊扬这样的研究人员更难出国参加学术会议或处理个人事务。 这一限制措施可能减缓中国 AI 人才外流，并削弱关键研究人员开展国际合作的能力，从而可能影响 DeepSeek 和阿里巴巴 Qwen 团队等中国主要机构开发开源模型的进程。 据报道，中国当局要求企业上报高级 AI 科学家的任何出国行程，有时会直接拒绝批准。此前该政策仅适用于国有企业和军方相关研究人员，现已扩展至私营 AI 公司。

rss · r/LocalLLaMA RSS · May 26, 12:26

**背景**: DeepSeek（深度求索）是一家成立于 2023 年的中国 AI 公司，以极低的成本开发出性能与 ChatGPT 相当的 DeepSeek-R1 等模型而闻名。阿里巴巴的 Qwen（通义千问）团队也发布过有影响力的开源模型。这两家公司都是开源加权 AI 模型的重要来源，而人才流动对全球 AI 生态系统贡献显著。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**标签**: `#AI talent`, `#China`, `#open-source`, `#DeepSeek`, `#geopolitics`

---

<a id="item-12"></a>
## [Together AI 开源 OSCAR：2 位 KV 缓存量化](https://www.reddit.com/r/LocalLLaMA/comments/1to5uml/new_kv_quants_coming_welcome_oscar_kv_quant_open/) ⭐️ 7.0/10

Together AI 开源了 OSCAR（离线谱协方差感知旋转），这是一种面向高效长上下文 LLM 服务的注意力感知 2 位 KV 缓存量化系统。 OSCAR 大幅降低了长上下文 LLM 中 KV 缓存的内存和带宽需求，在不显著损失精度的情况下实现更便宜、更快的推理，这对于扩展 LLM 部署至关重要。 与通用的 Hadamard 旋转不同，OSCAR 通过一次性离线校准过程推导出注意力感知的旋转，将量化噪声与注意力最不敏感的方向对齐。它实现了 KV 缓存的 2 位量化。

rss · r/LocalLLaMA RSS · May 26, 12:44

**背景**: 在大语言模型中，KV 缓存存储中间的注意力向量以避免重复计算，但在长上下文中成为内存瓶颈。量化可以降低这些缓存条目的位宽。OSCAR 使用注意力感知的旋转，比均匀量化或固定旋转更好地保留重要信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/05/25/together-ai-open-sources-oscar-an-attention-aware-2-bit-kv-cache-quantization-system-for-long-context-llm-serving/">Together AI Open-Sources OSCAR: An Attention-Aware 2-Bit KV ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区表达了兴奋之情，一位用户提到他们刚刚开始接受另一种方法（turboquant）时 OSCAR 就出现了，反映了社区的积极接受和对这项新技术的期待。

**标签**: `#KV cache quantization`, `#LLM serving`, `#open source`, `#Together AI`, `#long context`

---

<a id="item-13"></a>
## [快手 Keye-VL-2.0-30B-A3B：首个引入 DSA 注意力的多模态模型](https://www.reddit.com/r/LocalLLaMA/comments/1to63rt/keyevl2030ba3b_introducing_dsa_attention_into/) ⭐️ 7.0/10

快手发布了 Keye-VL-2.0-30B-A3B，这是一个 30B 级别的 MoE 视觉语言模型，首次在多模态场景中引入 DeepSeek Sparse Attention (DSA)，专注于长视频理解和智能体能力。 这标志着 DSA 从纯语言领域首次跨域应用到多模态领域，有望实现高效的长视频处理和实时智能体交互，可能降低视频 AI 智能体在消费应用中的门槛。 该模型采用 MoE 架构，总参数量 30B，但每个 token 仅激活 3B 参数。DSA 动态结合局部窗口注意力与全局稀疏连接，在保持长上下文性能的同时减少计算量。

rss · r/LocalLLaMA RSS · May 26, 12:55

**背景**: DeepSeek Sparse Attention (DSA) 是一种高效的注意力机制，最初为 DeepSeek-V3.2 语言模型开发，结合了局部窗口与内容感知的稀疏连接。Keye-VL 是快手推出的视觉语言模型系列，专注于视频理解和智能体任务。此次发布首次将 DSA 适配到多模态输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.02556">[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open ... DeepSeek Sparse Attention (DSA): A Comprehensive Review GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head ... AI on AI: Sparse Attention, from NSA to DSA – Champaign Magazine Inside DeepSeek V4: Hybrid Attention for Massive Contexts 十分钟读懂 DeepSeek-V3.2 稀疏注意力 DSA - 知乎 DeepSeek Sparse Attention from First Principles</a></li>
<li><a href="https://amitray.com/deepseek-sparse-attention-dsa-a-comprehensive-review/">DeepSeek Sparse Attention (DSA): A Comprehensive Review</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#vision-language`, `#MoE`, `#model release`, `#agent`

---