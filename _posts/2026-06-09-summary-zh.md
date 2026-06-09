---
layout: default
title: "Horizon Summary: 2026-06-09 (ZH)"
date: 2026-06-09
lang: zh
---

> From 76 items, 8 important content pieces were selected

---

1. [苹果重构 Apple Intelligence，基于谷歌 Gemini 模型搭建新架构](#item-1) ⭐️ 8.0/10
2. [MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second](#item-2) ⭐️ 8.0/10
3. [苹果推出 Core AI 框架，有望取代 Core ML](#item-3) ⭐️ 8.0/10
4. [FrontierCode](#item-4) ⭐️ 8.0/10
5. [Confidential submission of draft S-1 to the SEC](#item-5) ⭐️ 8.0/10
6. [OpenAI 秘密提交 IPO 申请，紧随 Anthropic 之后](#item-6) ⭐️ 8.0/10
7. [AI is slowing down](#item-7) ⭐️ 7.0/10
8. [Siri AI at WWDC 2026](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [苹果重构 Apple Intelligence，基于谷歌 Gemini 模型搭建新架构](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/) ⭐️ 8.0/10

苹果公布了 Apple Intelligence 的全新架构，将谷歌 Gemini 模型作为核心组件之一，通过端侧路由逻辑和苹果的 Private Cloud Compute（PCC）调用，不再仅依赖自家基础模型。这是苹果迄今最明确地承认其 AI 体系部分能力由第三方前沿模型驱动。 这表明即便是资源雄厚的苹果，也实际上已在基础模型竞赛中退场，转而把自己定位为运行在他人 LLM 之上的「隐私保护编排层」，将重塑业界对模型提供方与产品层关系的认知。同时这也强化了谷歌在 AI 价值链中的地位——Gemini 如今同时驱动着 Android 和越来越多的 iOS 默认助手。 苹果声称用户数据仅用于完成当下请求，苹果与谷歌均无法访问，且外部专家可「随时」验证 PCC 的隐私承诺；端侧路由会在本地 Apple Foundation Models 与 PCC 边界内的 Gemini 云端调用之间做选择。但仍有诸多疑问：苹果用的是 Gemini 旗舰版、微调版还是蒸馏版？哪些任务跑在苹果芯片上、哪些跑在谷歌硬件上？目前都不清楚。

hackernews · unclefuzzy · Jun 8, 19:14 · [社区讨论](https://news.ycombinator.com/item?id=48450142)

**背景**: Apple Intelligence 是苹果推出的端云协同 AI 系统，为 iPhone、iPad、Mac 提供写作工具、升级版 Siri 和图像生成等功能。Private Cloud Compute（PCC）是苹果自建的服务器架构，最初基于 Apple Silicon 打造，用于处理设备本身扛不住的 AI 请求，同时保证连苹果自己也无法突破的端到端隐私承诺。谷歌的 Gemini 是 Google DeepMind 推出的前沿多模态模型家族，目前旗舰是 Gemini 3.5。在此之前，苹果一直公开强调自家的 Apple Foundation Models，Gemini 集成被定位为类似 ChatGPT 的可选附加项，而非核心基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://security.apple.com/blog/expanding-pcc/">Expanding Private Cloud Compute - Apple Security Research</a></li>
<li><a href="https://security.apple.com/documentation/private-cloud-compute">Private Cloud Compute Security Guide | Documentation</a></li>
<li><a href="https://deepmind.google/models/gemini/">Gemini 3.5 - Google DeepMind</a></li>

</ul>
</details>

**社区讨论**: 评论者认为这是非常「苹果式」的打法——用隐私架构包装别人家的 AI，再把编排层产品化——但对苹果与谷歌之间的数据边界能否真正守住，多数人持怀疑态度，认为缺乏可验证的密码学强制手段。也有人质疑：在与 Android 直接竞争的背景下，苹果为何不选 Anthropic 或 OpenAI？还有人吐槽这本质上就是 Siri 和 Google Assistant 套了层新壳。

**💬 点评**: 苹果嘴硬好几年说要走自己的 AI 路线，结果「自己的路」最后变成了「让谷歌干，但客气点」。PCC 这层隐私外壳工程上确实牛，但再怎么玩密码学折纸艺术，也改变不了一个事实：Siri 的脑子如今住在山景城。

**标签**: `#apple-intelligence`, `#google-gemini`, `#llm-orchestration`, `#privacy`, `#industry-news`

---

<a id="item-2"></a>
## [MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) ⭐️ 8.0/10

Xiaomi's MiMo-v2.5-Pro-UltraSpeed delivers 1000 tokens/second on a 1-trillion-parameter model at competitive pricing, intensifying the speed and cost competition with US AI providers.

hackernews · gainsurier · Jun 8, 15:27 · [社区讨论](https://news.ycombinator.com/item?id=48446639)

**标签**: `#LLM-inference`, `#model-serving`, `#speed-optimization`, `#open-source-models`, `#MiMo`

---

<a id="item-3"></a>
## [苹果推出 Core AI 框架，有望取代 Core ML](https://developer.apple.com/documentation/coreai/) ⭐️ 8.0/10

在 WWDC 2026 上，苹果发布了全新的 Core AI 框架，用于在 CPU、GPU 和 Apple Neural Engine 上编写、优化与部署 AI 模型；同时向下载量低于 200 万的应用免费开放 Private Cloud Compute 服务。 Core AI 标志着苹果从传统机器学习工具链向生成式 AI 工作流的战略转向；凭借其庞大的设备保有量，苹果在量化格式和端侧推理上的选择，可能会左右整个行业 1000 亿参数以下模型的训练与部署方式。 该框架似乎提供了一条全新的流水线，可将 PyTorch 模型转换并跨 CPU、GPU 和 ANE 运行，据称还在推进 w4a8、w4a16 等激活量化方案；WWDC 2026 也专门安排了三场关于模型编写、优化和集成的开发者讲座。

hackernews · hmokiguess · Jun 8, 18:47 · [社区讨论](https://news.ycombinator.com/item?id=48449665)

**背景**: Core ML 是苹果自 2017 年起推出的机器学习框架，用于在苹果设备上运行模型，配套的 Core ML Tools 负责从 PyTorch、TensorFlow 等格式做模型转换。Apple Neural Engine（ANE）是苹果芯片内置的专用 NPU，处理神经网络任务比 CPU 或 GPU 更高效。Private Cloud Compute 于 2024 年推出，将苹果端侧的隐私保障延伸到云端，专门承接本地硬件跑不动的 AI 任务。Core AI 在这套技术栈之上，明显把重心从传统 ML 转向了生成式模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://appleinsider.com/articles/26/03/01/wwdc-2026-to-introduce-core-ai-as-replacement-for-core-ml">WWDC 2026 to introduce Core AI as replacement for Core ...</a></li>
<li><a href="https://security.apple.com/blog/expanding-pcc/">Expanding Private Cloud Compute - Apple Security Research</a></li>
<li><a href="https://developer.apple.com/machine-learning/core-ml/">Core ML Overview - Machine Learning - Apple Developer</a></li>

</ul>
</details>

**社区讨论**: 评论区在讨论 Core AI 是否会完全替代 Core ML，对新的 PyTorch 转换路径和 ANE 部署方案兴趣浓厚。不少开发者欢迎面向小型应用的免费 Private Cloud Compute 额度，但希望苹果突破 200 万下载量的上限；也有人指出苹果可能在 w4a8、w4a16 等量化格式上拥有行业话语权。

**💬 点评**: 苹果在 LLM 这波热潮里看似掉队，其实是在闷声攒大招：当一家手握十亿台 NPU 设备的公司开始定义什么叫"优化"，全世界训练百亿参数以下模型的人就算不情愿，也得乖乖研究 w4a8 了。

**标签**: `#apple`, `#on-device-ai`, `#core-ai`, `#model-optimization`, `#llm-inference`

---

<a id="item-4"></a>
## [FrontierCode](https://cognition.ai/blog/frontier-code) ⭐️ 8.0/10

Cognition AI introduces FrontierCode, a benchmark with 3000 rubrics from 20+ open-source maintainers measuring whether AI-generated code would actually get merged in real repos.

hackernews · streamer45 · Jun 8, 20:45 · [社区讨论](https://news.ycombinator.com/item?id=48451723)

**标签**: `#benchmarks`, `#coding-agents`, `#cognition-ai`, `#evaluation`, `#ai-agents`

---

<a id="item-5"></a>
## [Confidential submission of draft S-1 to the SEC](https://openai.com/index/openai-submits-confidential-s-1/) ⭐️ 8.0/10

OpenAI has confidentially submitted a draft S-1 filing to the SEC, signaling preparations for a potential IPO.

hackernews · hackerBanana · Jun 8, 21:22 · [社区讨论](https://news.ycombinator.com/item?id=48452317)

**标签**: `#OpenAI`, `#IPO`, `#industry-news`, `#SEC`, `#business`

---

<a id="item-6"></a>
## [OpenAI 秘密提交 IPO 申请，紧随 Anthropic 之后](https://techcrunch.com/2026/06/08/following-anthropic-openai-files-confidentially-for-ipo/) ⭐️ 8.0/10

OpenAI 已向 SEC 秘密提交了首次公开募股（IPO）申请，距其主要竞争对手 Anthropic 提交类似申请仅过去一周多。两家 AI 巨头如今正并肩走向公开市场。 IPO 将成为这两家顶级 AI 实验室的重大转折点，使它们直面公开市场的审视、季度财报压力，同时也能撬动远超私募规模的资金池来支撑算力饥渴的前沿模型。此举还表明 AI 资本支出军备竞赛已超出私募轮次的承载能力，正在重塑整个智能体与模型生态的资金底盘。 秘密递交制度源于 2012 年的 JOBS 法案，并于 2017 年扩展至所有发行人，允许公司私下与 SEC 沟通并打磨 S-1 文件，仅在路演前至少 15 天才需公开披露。OpenAI 和 Anthropic 均未披露发行规模、估值目标或时间表，而且秘密递交并不保证 IPO 一定会推进。

rss · TechCrunch AI · Jun 8, 21:29

**背景**: OpenAI 是 ChatGPT 和 GPT 系列模型的开发者，Anthropic 则打造了 Claude 模型家族，两者被普遍视为美国最顶尖的前沿 AI 实验室。两家公司已从 Microsoft、Google、Amazon 等投资方筹得数百亿美元私募资金，其中 Anthropic 近期估值据报道已接近万亿美元区间。向 SEC 秘密递交申请如今已是标准的 IPO 前置流程，允许公司在正式公开发行前，私下反复打磨注册文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/confidential-ipo-filings">Understanding Confidential IPO Filings</a></li>
<li><a href="https://www.torresbusinesslaw.com/blog/confidential-vs-public-filing-ipo-despac/">Confidential vs. Public Filing of Initial Draft Prospectus: Strategic Considerations for IPOs and De-SPAC Transactions – Torres & Zheng at Law, P.C.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>

</ul>
</details>

**💬 点评**: 两家天天警告我们 AI 可能毁灭人类的公司，居然前后脚十天内冲刺 IPO，让人不禁怀疑它们真正在抢的到底是 AGI 还是早期投资人的退出通道。不管怎样，准备好迎接史上第一场把「人类灭绝概率」当作前瞻性指引来念的季度财报电话会议吧。

**标签**: `#OpenAI`, `#Anthropic`, `#IPO`, `#AI industry`, `#business`

---

<a id="item-7"></a>
## [AI is slowing down](https://www.wheresyoured.at/ai-is-slowing-down/) ⭐️ 7.0/10

Ed Zitron argues the AI industry is decelerating and would need over $3 trillion in revenue by 2030 to sustain its current trajectory, questioning the viability of current investments.

hackernews · crescit_eundo · Jun 8, 15:46 · [社区讨论](https://news.ycombinator.com/item?id=48446893)

**标签**: `#AI industry`, `#economics`, `#commentary`, `#market analysis`, `#LLMs`

---

<a id="item-8"></a>
## [Siri AI at WWDC 2026](https://simonwillison.net/2026/Jun/8/wwdc/#atom-everything) ⭐️ 7.0/10

Simon Willison offers cautious analysis of Apple's WWDC 2026 Siri AI announcements, noting the use of a custom Gemini-derived model on Private Cloud Compute and vision LLMs to extract screen context.

rss · Simon Willison · Jun 8, 23:58

**标签**: `#Apple Intelligence`, `#Siri`, `#Vision LLMs`, `#Gemini`, `#WWDC`

---