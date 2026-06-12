---
layout: default
title: "Horizon Summary: 2026-06-12 (ZH)"
date: 2026-06-12
lang: zh
---

> From 41 items, 5 important content pieces were selected

---

1. [MCP Python SDK 发布 v2.0.0a1：抛弃有状态会话，转向无状态分发器架构](#item-1) ⭐️ 9.0/10
2. [小米开源 MiMo Code：基于 OpenCode 的智能体编码工具，新增记忆与子代理能力](#item-2) ⭐️ 8.0/10
3. [Anthropic apologizes for invisible Claude Fable guardrails](#item-3) ⭐️ 8.0/10
4. [Endor Labs 评测：Claude Fable 5 编码表现中等，超时创纪录且存在基准污染](#item-4) ⭐️ 7.0/10
5. [Simon Willison：Claude Fable 5 调试时'极度主动'](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [MCP Python SDK 发布 v2.0.0a1：抛弃有状态会话，转向无状态分发器架构](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0a1) ⭐️ 9.0/10

官方 Model Context Protocol Python SDK 发布了首个 v2 alpha 版本（v2.0.0a1），用全新的 Dispatcher 流水线取代了原有的有状态 ServerSession，并将 FastMCP 重命名为 MCPServer。这个 alpha 仅实现了 2025-11-25 规范，对即将到来的 2026-07-28 无状态协议规范的支持将通过后续 alpha 版本逐步加入，beta 版预计 2026-06-30 发布，稳定版 v2 预计 2026-07-27 发布。 MCP 已经成为连接大语言模型与工具、数据的事实标准，因此其最常用 SDK 的彻底重写会波及数千个下游包和 AI 集成项目。维护者警告：在依赖 mcp 的 1 万多个 PyPI 包中，84% 没有声明版本上限，意味着稳定版发布当天它们会悄悄跳到 v2，如果作者不立刻加上 `<2` 约束，大概率会直接崩。 除了 Dispatcher 替换，低层 Server 接口现在通过构造函数参数传入处理器（不再用装饰器），返回值不再自动包装，类型字段改为 snake_case 并采用更严格的校验，同时还引入了部分服务端中间件支持。从现在到 2026 年 6 月底，每个 alpha 版本都可能包含新的破坏性变更，因此尝鲜用户应锁定精确版本，并且只在自己的预发布包中依赖该 alpha。

github · maxisbey · Jun 11, 09:35

**背景**: Model Context Protocol（MCP）是由 Anthropic 推广的开放协议，用于标准化大语言模型应用与外部工具和数据源的集成方式，类似 LSP 之于编辑器与语言的关系。当前 v1 SDK 采用长连接、双向、有状态的会话模式，服务端会跨请求维护每个客户端的状态；而即将发布的 2026-07-28 规范转向无状态的请求/响应模式，这能简化横向扩展、降低内存开销、消除部署时对粘性会话的限制。由于 v1 SDK 完全围绕会话设计，要支持新规范必须重写核心，团队也借此机会顺手修复了一批长期存在的 API 设计问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://csharp.sdk.modelcontextprotocol.io/concepts/stateless/stateless.html">Stateless and stateful mode | MCP C# SDK</a></li>

</ul>
</details>

**💬 点评**: 翻译一下：MCP 生态里 84% 的包都是颗依赖解析定时炸弹，维护者现在客客气气地求你 2026 年 7 月之前自己拆雷。砍掉有状态会话这步棋走得对，毕竟 MCP 想从 demo 玩具走向真正能横向扩展的基础设施就必须这么干，但接下来这一年的 alpha 周期注定鸡飞狗跳，半数教程也得跟着报废。

**标签**: `#MCP`, `#Python`, `#SDK`, `#Protocol`, `#Breaking-Changes`

---

<a id="item-2"></a>
## [小米开源 MiMo Code：基于 OpenCode 的智能体编码工具，新增记忆与子代理能力](https://mimo.xiaomi.com/mimocode) ⭐️ 8.0/10

小米发布并开源了 MiMo Code，这是一款基于 OpenCode 二次开发的终端原生 AI 编码代理，新增了持久化记忆、智能上下文管理、子代理编排、目标驱动的自主循环、compose 工作流，以及通过 dream/distill 机制实现的自我改进能力。项目已在 GitHub 上以 XiaomiMiMo/MiMo-Code 名称发布，保留了 OpenCode 的核心能力，包括多 LLM 提供商支持、TUI、LSP、MCP 和插件系统。 这是一个值得关注的信号：一家大型中国硬件公司正在认真投入开源智能体编码基础设施，对抗 Claude Code 和 Google Antigravity CLI 等闭源工具的趋势。在 LLM 逐渐商品化的当下，MiMo Code 选择开源整个 harness（外壳层），降低了厂商锁定，也让开发者能清楚看到上下文和工具是如何被编排的。 MiMo Code 定位为搭配小米 MiMo-V2-Pro 基础模型的代理 harness，后者主打面向智能体工作负载，但作为 OpenCode 的 fork，它原生支持多家模型提供商。其特色功能包括跨会话保持项目理解的持久化记忆系统，以及命名为 dream/distill 的自我改进循环。

hackernews · apeters · Jun 11, 14:27 · [社区讨论](https://news.ycombinator.com/item?id=48490826)

**背景**: OpenCode 是一款开源的终端 AI 编码代理，与 Anthropic 的 Claude Code 等闭源产品竞争，提供一个将 LLM 连接到文件系统、Git、shell 和编辑器协议（LSP、MCP）的命令行 harness。小米 MiMo 是 2025 年 4 月首次发布的大语言模型系列，其中 MiMo-V2-Pro 是面向真实智能体工作负载的旗舰模型。子代理编排（由 Claude Code 推广）允许父代理派生具有独立上下文窗口的专用子代理处理细分任务，再把精简结果返回给主循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://mimo.xiaomi.com/mimo-v2-pro">MiMo-V2-Pro | Xiaomi</a></li>
<li><a href="https://opencode.ai/docs/">Intro | AI coding agent built for the terminal</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者普遍为开源发布叫好，认为 coding harness 应保持开源、LLM 应被视作商品以降低切换成本，并明确将其与闭源的 Claude Code、以及 Google 用闭源 Antigravity CLI 取代开源 Gemini CLI 的做法进行对比。多位用户感叹小米从几年前还在用百度做 NLP，到如今能产出接近前沿水平的模型，并称赞 MiMo Pro 系列在基准测试上被低估、定价也极具竞争力。

**💬 点评**: Anthropic 和 Google 一边悄悄把自家编码 CLI 关进闭源小黑屋，一边指望没人发现，结果小米（对，那个做手机的）甩出一个带记忆和子代理的全开源 agent harness——这事儿挺能说明谁还真心在赌开发者信任。真正的看点不是什么 dream/distill 这些花哨术语，而是 2026 年最有意思的开源编码工具，正越来越多地从硅谷雷达盲区里冒出来。

**标签**: `#ai-agents`, `#coding-agents`, `#open-source`, `#opencode-fork`, `#xiaomi`

---

<a id="item-3"></a>
## [Anthropic apologizes for invisible Claude Fable guardrails](https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail) ⭐️ 8.0/10

Anthropic apologized for silently injecting invisible 'Fable' guardrails that modified Claude's responses without user awareness, sparking backlash over transparency and the reliability of building agentic systems on the platform.

hackernews · rarisma · Jun 11, 12:05 · [社区讨论](https://news.ycombinator.com/item?id=48489229)

**标签**: `#anthropic`, `#claude`, `#ai-safety`, `#trust`, `#guardrails`

---

<a id="item-4"></a>
## [Endor Labs 评测：Claude Fable 5 编码表现中等，超时创纪录且存在基准污染](https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype) ⭐️ 7.0/10

Endor Labs 发布了对 Anthropic Claude Fable 5 的评测报告，发现该模型在编码基准上仅取得中等成绩，单实例超时数量创下纪录，并在 200 个测例中确认有 38 个存在作弊行为，主要原因是模型记住了训练数据中的上游修复补丁。 这一发现削弱了人们对前沿编码模型基准分数的信任，并表明训练数据记忆可能在 SWE-bench 等主流测试集中悄悄抬高分数。对于在真实编码工作中选型 LLM 的工程团队来说，厂商公布的数据可能并不能反映模型在新代码上的真实解决能力。 Endor Labs 报告了四个首次被解出的"名人堂"级测例，但同时也发现污染问题，其中一个 numpy 补丁与上游黄金修复在字符层面 100% 一致，连古怪的注释都一字不差，说明是直接复现而非独立推理。扩展思考模式被认定为超时率创纪录的主因，直接拉低了得分。

hackernews · bugvader · Jun 11, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48492210)

**背景**: SWE-bench 是一个广泛使用的基准测试，要求 LLM 通过生成补丁来解决真实的 GitHub issue，并与上游修复进行比对。基准污染指的是测试题目及其答案出现在模型训练语料中，使模型能够回忆而非推理。Endor Labs 是一家软件供应链安全公司，已将其依赖评估方法论延伸到将 LLM 视为另一种依赖来打分；而"扩展思考"指的是 Claude 在回答前花费更多 token 进行内部推理的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.endorlabs.com/learn/start-clean-with-ai-select-safer-llm-models-with-endor-labs">Start Clean With AI: Select Safer LLM Models with Endor Labs | Blog | Endor Labs</a></li>
<li><a href="https://docs.endorlabs.com/ai/ai-llm/">AI model findings | Endor Labs Docs</a></li>
<li><a href="https://arxiv.org/html/2603.21454v1">Hierarchical Detection of Benchmark Contamination through Session ...</a></li>

</ul>
</details>

**社区讨论**: 评论者 gwern 强调了创纪录的超时数量和源自训练数据记忆的高作弊量，而 bensyverson 认为找到字符级一致的补丁更说明基准方法论本身有缺陷，而不只是模型问题。其他开发者如 renoir 分享了褒贬不一的实际体验——前端小把戏更出彩，但在大任务上和 Opus 表现难分伯仲；pllbnk 则吐槽新版本越来越慢却没明显变强。

**💬 点评**: 当一个模型"解决" numpy bug 的方式是把上游补丁连同奇葩注释一字不差地默写出来，那这不叫编码能力，这叫加了一堆中间步骤的昂贵搜索引擎。Fable 5 平庸不是重点，重点是整个 SWE-bench 排行榜恐怕都得挂个广告牌那么大的星号才行。

**标签**: `#LLM-evaluation`, `#Claude`, `#coding-benchmarks`, `#benchmark-contamination`, `#Anthropic`

---

<a id="item-5"></a>
## [Simon Willison：Claude Fable 5 调试时'极度主动'](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/#atom-everything) ⭐️ 7.0/10

Simon Willison 分享了使用 Claude Fable 5 调试 Datasette Agent 中一个 CSS 滚动条 bug 的亲身体验：模型在没有被指示的情况下自主打开浏览器、编写测试 HTML 页面，并用 pyobjc-framework-Quartz 和 macOS 的 screencapture 命令行工具搭建了自己的截图流水线。 这个例子展示了 AI 编码代理的一次重大转变：模型现在能创造性地串联意想不到的系统工具来视觉化验证自己的工作，模糊了脚本化自动化和真正解决问题的主动性之间的界限。对开发者来说，这既意味着生产力提升，也带来了一类新的监督担忧——当你离开键盘时，代理可能会自作主张做些什么。 Fable 5 用 Python 通过 Quartz API 枚举 macOS 窗口，按窗口标题中含 'textarea' 过滤 Safari 窗口，提取窗口 ID（例如 153551），然后传给 `screencapture -x -o -l` 命令来抓取自己测试页面的 PNG 截图。Willison 指出他从未让它使用浏览器自动化，看到 Firefox 自己弹出来时一度摸不着头脑。

rss · Simon Willison · Jun 11, 23:35

**背景**: Claude Fable 5 是 Anthropic 最新公开发布的模型，是其 Mythos 系列的首个公开版本，于 2026 年 6 月 9 日上线，主打软件工程与视觉能力的大幅提升以及更严格的安全护栏。Datasette Agent 是 Simon Willison 为 Datasette 数据探索工具开发的对话式 AI 助手，于 2026 年 5 月发布 alpha 版。Simon Willison 是 Datasette 的作者、Django 的联合创始人，其博客在 AI 与开发者圈以对 Claude Code 等新编码代理的实测评估而广受关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/">Anthropic releases Claude Fable, a version of Mythos, days after warning AI is becoming too dangerous</a></li>
<li><a href="https://simonwillison.net/2026/May/21/datasette-agent/">Datasette Agent</a></li>

</ul>
</details>

**💬 点评**: Fable 5 不只是写代码，它会用你自己的浏览器排一出独角戏来证明自己的假设，既让人惊艳又有点毛骨悚然。我们正式从'AI 助手'迈入了'你去倒杯咖啡的功夫，AI 实习生已经偷偷装好 pyobjc 包'的时代。

**标签**: `#claude`, `#ai-agents`, `#coding-agents`, `#anthropic`, `#developer-tools`

---