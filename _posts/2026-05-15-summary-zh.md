---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 85 items, 24 important content pieces were selected

---

1. [vLLM v0.21.0 发布：重大升级与破坏性变更](#item-1) ⭐️ 9.0/10
2. [Codex 现已登陆 ChatGPT 移动应用](#item-2) ⭐️ 8.0/10
3. [arXiv 对幻觉参考文献作者禁发一年](#item-3) ⭐️ 8.0/10
4. [Anthropic 隐瞒强大 AI 是因成本？](#item-4) ⭐️ 8.0/10
5. [前沿 AI 访问可能受限，但开放权重提供了替代方案](#item-5) ⭐️ 8.0/10
6. [安大略审计员发现医生使用的 AI 笔记工具经常捏造基本事实](#item-6) ⭐️ 8.0/10
7. [Richard Socher 的 6.5 亿美元初创公司旨在建造自我改进的 AI](#item-7) ⭐️ 8.0/10
8. [Cerebras 融资 55 亿美元，股价飙升 108%，创 AI 硬件 IPO 里程碑](#item-8) ⭐️ 8.0/10
9. [Anthropic 2028 AI 情景论文警告美中领导力的两种未来](#item-9) ⭐️ 8.0/10
10. [Arc Gate：阻止 LangChain AI 代理的提示注入](#item-10) ⭐️ 8.0/10
11. [字节跳动发布开源 Cola-DLM 模型](#item-11) ⭐️ 8.0/10
12. [小模型通过自我纠错训练，在 HumanEval 上达到 80%](#item-12) ⭐️ 8.0/10
13. [拆除 2024 款 RAV4 的调制解调器和 GPS 以阻止遥测](#item-13) ⭐️ 7.0/10
14. [Antirez 发布 DwarfStar4 用于本地 DeepSeek 推理](#item-14) ⭐️ 7.0/10
15. [Anthropic 发布 Claude for Legal，集成新工具](#item-15) ⭐️ 7.0/10
16. [旧科技消亡，新 AI 时代难以诞生](#item-16) ⭐️ 7.0/10
17. [GGUF 格式：单文件理念与缺失功能](#item-17) ⭐️ 7.0/10
18. [克劳德代码处理大型代码库的智能搜索](#item-18) ⭐️ 7.0/10
19. [人机回环治理：企业 AI 的幻觉？](#item-19) ⭐️ 7.0/10
20. [InternLM 发布 35B 科学多模态模型 Intern-S2-Preview](#item-20) ⭐️ 7.0/10
21. [用户报告 Qwen 3.6 MTP 模型带来 1.5 倍速度提升](#item-21) ⭐️ 7.0/10
22. [RAG 聊天机器人评测：昂贵模型表现反而不佳](#item-22) ⭐️ 7.0/10
23. [TurboQuant 研究：FP8 在 KV 缓存量化中优于 TurboQuant](#item-23) ⭐️ 7.0/10
24. [本地运行 DeepSeek V4 Pro 的性能基准测试](#item-24) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.21.0 发布：重大升级与破坏性变更](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 9.0/10

vLLM v0.21.0 正式弃用 Transformers v4，要求 C++20 编译器，集成 KV 卸载与混合内存分配器 (HMA)，为推理模型引入带思考预算的推测解码，并为 Blackwell GPU 新增 TOKENSPEED_MLA 后端。 此次发布标志着 vLLM 向最新 Transformers v5 生态系统和 Blackwell 硬件迈出重要一步，同时通过推测解码改进，为推理模型实现了更高效的内存管理和更快速的推理。 C++20 要求是破坏性构建变更，用户必须升级编译器。TOKENSPEED_MLA 后端专门针对 Blackwell GPU 上的 DeepSeek-R1 和 Kimi-K25 模型进行了优化。混合内存分配器集成通过智能卸载减少了 KV 缓存占用。

github · khluu · May 15, 08:44

**背景**: vLLM 是一个高性能的开源 LLM 推理框架。混合内存分配器 (HMA) 管理跨 GPU 和 CPU 内存的 KV 缓存以提高吞吐量。推测解码使用较小的草稿模型预测 token，然后用主模型验证，在不降低质量的情况下加速生成。Blackwell GPU 是 NVIDIA 的最新架构，为 LLM 推理提供极致性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fenado.ai/articles/lightseek-foundation-unveils-open-source-tokenspeed-llm-engine-with-vllm-integration-for-nvidia-blackwell">LightSeek Foundation Unveils Open-Source TokenSpeed LLM Engine with vLLM Integration for NVIDIA Blackwell | TokenSpeed, LLM inference engine, Fenado AI</a></li>
<li><a href="https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html">Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) | vLLM Blog</a></li>
<li><a href="https://developer.nvidia.com/blog/blackwell-breaks-the-1000-tps-user-barrier-with-metas-llama-4-maverick/">Blackwell Breaks the 1,000 TPS/User Barrier With Meta’s Llama 4 Maverick | NVIDIA Technical Blog</a></li>

</ul>
</details>

**社区讨论**: vLLM 社区一直积极讨论弃用 Transformers v4 和新的构建要求。一些用户对迁移工作量表示担忧，而另一些用户则赞赏性能提升，特别是推理模型的推测解码改进。

**标签**: `#vLLM`, `#LLM inference`, `#open-source`, `#GPU optimization`, `#speculative decoding`

---

<a id="item-2"></a>
## [Codex 现已登陆 ChatGPT 移动应用](https://openai.com/index/work-with-codex-from-anywhere/) ⭐️ 8.0/10

OpenAI 将其编程智能体 Codex 集成到 ChatGPT 移动应用中，使用户能够直接在智能手机上执行编码任务并管理工作流程。 这一扩展极大地提高了 AI 辅助编程的可及性，使开发者能够在远离桌面时编码、调试或解除任务阻塞，从而可能提高生产力并减少上下文切换。 Codex 在 ChatGPT 应用内免费提供，但交互可能用于训练。移动智能体支持权限请求和通知，允许用户批准操作并接收长时间运行任务的更新。

hackernews · mikeevans · May 14, 20:06 · [社区讨论](https://news.ycombinator.com/item?id=48140529)

**背景**: Codex 是 OpenAI 开发的用于软件工程任务（如编写代码和修复错误）的 AI 智能体。它最初于 2025 年 4 月作为 CLI 工具和桌面应用发布，现在通过 ChatGPT 扩展到移动端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的社区评论显示出不同的观点：一些用户认为移动体验因屏幕尺寸和缺乏键盘而效果不佳，而另一些用户则赞赏批准权限和通知等功能。Codex 包含在免费计划中的这一点也受到好评。

**标签**: `#AI Agents`, `#Codex`, `#OpenAI`, `#ChatGPT`, `#Mobile Development`

---

<a id="item-3"></a>
## [arXiv 对幻觉参考文献作者禁发一年](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv 宣布新政策，对提交包含幻觉参考文献论文的作者实施 1 年禁令，并要求后续提交必须首先被信誉良好的同行评审场所接受。 这项政策直接解决了 AI 生成的幻觉引用污染科学文献这一日益严重的问题，该问题威胁学术诚信并浪费审稿人时间。 禁令自通知之日起持续一年，之后作者的提交必须先被信誉良好的同行评审场所接受才能在 arXiv 上发布。该政策针对故意或疏忽使用 LLM 编造参考文献的行为。

hackernews · gjuggler · May 14, 20:39 · [社区讨论](https://news.ycombinator.com/item?id=48140922)

**背景**: 大型语言模型（LLM）有时会“幻觉”——生成看似合理但事实错误的内容，包括虚假参考文献。最近的分析发现数千篇论文含有潜在幻觉引用，破坏了科学可靠性。arXiv 是一个免费预印本服务器，广泛用于物理、数学、计算机科学及相关领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/d41586-026-00969-z">Hallucinated citations are polluting the scientific literature. What can be done?</a></li>
<li><a href="https://arxiv.org/abs/2601.18724">[2601.18724] HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区普遍支持该政策，用户 btown 称其“对科学非常有益”，rgmerk 表示“如果你不值得花时间仔细检查 LLM 的输出，那也不值得我花时间去阅读。”一些评论者如 mks_shuffle 希望做更多工作以解决创建正确 BibTeX 条目的根本问题，注意到 Zotero 等工具已使引用提取更容易。

**标签**: `#arXiv`, `#LLM`, `#hallucination`, `#policy`, `#academic integrity`

---

<a id="item-4"></a>
## [Anthropic 隐瞒强大 AI 是因成本？](https://kingy.ai/ai/too-dangerous-to-release-or-just-too-expensive-the-real-reason-anthropic-is-hiding-its-most-powerful-ai/) ⭐️ 8.0/10

一篇文章质疑 Anthropic 暂不发布其最先进 AI 模型 Mythos 的决定，究竟是出于安全考虑还是部署成本过高，引发了 AI 社区的讨论。 这一争论凸显了 AI 安全与商业可行性之间的张力，影响着前沿模型的部署方式，并塑造了公众对 AI 公司的信任。 Mythos 被描述为能大规模发现零日漏洞的通用前沿模型。Anthropic 公开表示计算成本不是限制部署的因素，并强调安全防护措施。

hackernews · chbint · May 15, 12:49 · [社区讨论](https://news.ycombinator.com/item?id=48147945)

**背景**: Anthropic 和 OpenAI 等 AI 公司有时会以安全风险（如用于网络攻击）为由暂不发布强大模型。批评者认为，高昂的推理成本才是真正原因，因为运行此类模型费用不菲。安全与盈利之间的平衡是行业讨论的关键。

**社区讨论**: 社区评论意见不一：一些人怀疑 Anthropic 的动机，认为成本才是真正问题（如 wood_spirit）。一位 Anthropic 员工（smca）反驳称安全是首要因素，且未考虑计算成本。还有人批评文章来源或指出网站无法访问。

**标签**: `#Anthropic`, `#AI safety`, `#LLM`, `#cost`, `#discussion`

---

<a id="item-5"></a>
## [前沿 AI 访问可能受限，但开放权重提供了替代方案](https://writing.antonleicht.me/p/cut-off) ⭐️ 8.0/10

一篇讨论文章认为，前沿 AI 模型的访问很快将受到经济因素和安全问题的限制，但社区评论者反驳称，来自中国实验室及其他地方的开放权重模型正在迅速缩小差距。 这一争论对依赖尖端模型的 AI 生态系统参与者——初创企业、企业和政府——至关重要。如果限制收紧，开放权重替代方案可能提供可行路径，重塑地缘政治 AI 格局，减少对少数主导提供商的依赖。 文章侧重于经济和安全限制，但明显忽略了开放权重模型的讨论。评论者指出，像 Qwen、Llama 和 DeepSeek 这样的模型仅落后前沿领先者数月，而本地推理硬件（如 DGX Sparks）已经能充分满足许多用例。

hackernews · thoughtpeddler · May 15, 01:08 · [社区讨论](https://news.ycombinator.com/item?id=48143284)

**背景**: 前沿 AI 模型是最先进的通用模型，使用巨大的计算预算（例如约 10^26 次浮点运算）进行训练。开放权重模型公开其训练好的参数，允许任何人下载并在本地运行，但缺乏完全的开源透明度（例如训练数据）。LLM 经济学指的是训练、部署和使用大型语言模型的成本与权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>
<li><a href="https://www.datacamp.com/blog/frontier-models">Frontier Models Explained: What Defines the Cutting Edge of AI | DataCamp</a></li>
<li><a href="https://neysa.ai/blog/open-weights-open-source/">Open Weights vs Open Source : What’s the Real Difference?</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对预测的访问限制表示不担忧。一位用户指出，中国实验室已实现“逃逸速度”，开放权重模型仅落后数月。另一位分享了一个实际例子：在两台 DGX Sparks 上运行本地模型，达到约 35 tokens/s，这对他们的公司来说已经足够。第三位强调，数据中心容量而非模型访问才是真正的瓶颈。

**标签**: `#AI access`, `#frontier models`, `#open weights`, `#geopolitical AI`, `#LLM economics`

---

<a id="item-6"></a>
## [安大略审计员发现医生使用的 AI 笔记工具经常捏造基本事实](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771) ⭐️ 8.0/10

安大略审计员进行审计后发现，医生使用的 AI 笔记工具经常生成错误的诊断、症状和其他基本事实，引发了严重的患者安全担忧。 这削弱了对 AI 辅助医疗文档的信任，并凸显了在依赖 AI 生成的医疗记录前进行严格验证的关键需求。 审计特别指出，这些 AI 工具捏造了不存在的病情和症状，与实际就诊情况相矛盾；而且这些工具缺乏足够的防护措施来防止此类幻觉。

hackernews · sohkamyung · May 14, 22:37 · [社区讨论](https://news.ycombinator.com/item?id=48142188)

**背景**: 驱动这些笔记工具的大语言模型（LLM）容易出现“幻觉”——生成听起来合理但事实错误的内容。在医疗领域，即使是微小的错误也可能导致误诊或不当治疗，因此准确性至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/blogs/what-are-llm-hallucinations/">What are LLM Hallucinations? - GeeksforGeeks</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-hallucinations">What are AI hallucinations? - IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了 AI 笔记工具捏造细节的个人经历（例如，将跑步膝诊断为骨质疏松症）。一些人指出，带有时间戳链接的录音有助于验证准确性，但在医疗领域，HIPAA 等法规限制使此类解决方案充满挑战。

**标签**: `#AI agents`, `#LLM reliability`, `#healthcare AI`, `#factual accuracy`

---

<a id="item-7"></a>
## [Richard Socher 的 6.5 亿美元初创公司旨在建造自我改进的 AI](https://techcrunch.com/2026/05/14/what-happens-when-ai-starts-building-itself/) ⭐️ 8.0/10

Richard Socher 启动了一家获得 6.5 亿美元融资的初创公司，旨在开发能够无限期自我研究和改进的 AI，同时还要交付实际产品。 这代表了向递归自我改进 AI 迈出的重要一步，这一概念常与潜在的智能爆炸和超级智能相关联，而巨额融资表明投资者对此类系统可行性的强烈信心。 该初创公司由 AI 领域知名人物 Richard Socher 领导；6.5 亿美元的融资对早期初创公司来说异常巨大，Socher 声称该 AI 不仅能自我改进，还能交付实际产品。

rss · TechCrunch AI · May 14, 19:57

**背景**: 递归自我改进（RSI）是指 AI 系统重写自身代码以增强能力的过程，可能导致智能爆炸。历史上，RSI 一直被视为通往超级智能的理论路径，但最近的进展表明该过程的某些部分可能已在实施中。Socher 的初创公司旨在实现这一概念，同时关注商业可行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://spectrum.ieee.org/recursive-self-improvement">Recursive Self - Improvement Edges Closer In AI Labs - IEEE Spectrum</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Self-Improving AI`, `#Startup`, `#Richard Socher`, `#Funding`

---

<a id="item-8"></a>
## [Cerebras 融资 55 亿美元，股价飙升 108%，创 AI 硬件 IPO 里程碑](https://techcrunch.com/2026/05/14/cerebras-raises-5-5b-kicking-off-2026s-ipo-season-with-a-bang/) ⭐️ 8.0/10

Cerebras Systems 于 2026 年 5 月在纳斯达克首次公开募股（IPO）中筹集了 55 亿美元，其股票在首个交易日以代码 CBRS 飙升了 108%。 这次 IPO 是 2026 年首个大型科技公司上市，表明投资者对专用 AI 硬件充满信心，可能加速晶圆级加速器作为 GPU 替代方案在 AI 工作负载中的采用。 股价飙升使 Cerebras 的估值超过 100 亿美元；其第三代晶圆级引擎（WSE-3）拥有 4 万亿个晶体管、90 万个 AI 优化核心，峰值 AI 性能达到 125 petaflops。

rss · TechCrunch AI · May 14, 16:30

**背景**: Cerebras Systems 成立于 2015 年，开发晶圆级 AI 芯片，其尺寸远大于传统 GPU——WSE-3 比典型 GPU 大 58 倍。这些芯片将整个硅晶圆用作单一处理器，从而实现大规模并行计算和高内存带宽，适用于 AI 训练和推理。该公司于 2026 年 4 月提交 IPO 申请，次月上市。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.nasdaq.com/newsroom/cerebras-ipo-ushering-new-era-ai-hardware">Cerebras IPO: Ushering in a New Era of AI Hardware | Nasdaq</a></li>
<li><a href="https://news.ucr.edu/articles/2025/06/16/wafer-scale-accelerators-could-redefine-ai">Wafer-scale accelerators could redefine AI | UCR News | UC ...</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#IPO`, `#Cerebras`, `#Industry News`, `#LLM Inference`

---

<a id="item-9"></a>
## [Anthropic 2028 AI 情景论文警告美中领导力的两种未来](https://www.reddit.com/r/artificial/comments/1td99uw/anthropic_just_published_a_pretty_alarming_2028/) ⭐️ 8.0/10

Anthropic 发布了一篇研究论文，概述了到 2028 年全球 AI 领导力的两种可能情景，重点关注算力优势、芯片走私和蒸馏攻击。论文警告，如果美国不堵上漏洞，中国可能达到 AI 均势并塑造全球 AI 规范。 这项分析之所以重要，是因为它将 AI 竞争界定为地缘政治斗争而非单纯的技术竞赛，并呼吁立法将蒸馏攻击定为工业间谍罪。它凸显了出口管制与执法将决定哪个政治体系制定全球 AI 治理标准。 论文描述了两种情景：'好'的情景是美国堵上漏洞，将算力差距扩大到 11 倍并保持 12-24 个月的领先；'坏'的情景是中国接近均势并以更便宜的模型充斥市场。蒸馏攻击涉及创建数千个虚假账户以窃取模型输出，Anthropic 的新模型 Mythos Preview 据称帮助 Firefox 在一个月内修复了比 2025 全年更多的安全漏洞。

rss · r/artificial RSS · May 14, 19:53

**背景**: 前沿 AI 模型是最先进的通用 AI 系统，使用巨大的计算资源进行训练。蒸馏攻击是一种敌方利用虚假账户查询模型并复制其行为的方法，实质上是窃取知识产权。美国目前凭借 NVIDIA 和台积电等公司在 AI 算力上领先，但出口管制旨在阻止中国获取先进芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.iiss.org/online-analysis/cyber-power-matrix/2026/05/ai-distillation-attacks-in-the-uschina-contest/">AI distillation attacks in the US-China contest</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI geopolitics`, `#export controls`, `#frontier AI`, `#AI safety`

---

<a id="item-10"></a>
## [Arc Gate：阻止 LangChain AI 代理的提示注入](https://www.reddit.com/r/artificial/comments/1tdedmo/built_a_tool_that_stops_ai_agents_from_being/) ⭐️ 8.0/10

一位开发者发布了 Arc Gate，这是一个开源的 LangChain 回调，通过强制执行只有原始用户指令具有权限，来检测并阻止提示注入攻击。它通过一行代码即可与任何 LangChain LLM 集成，并提供了实时演示供红队测试。 提示注入是 AI 代理工作流中的关键安全漏洞，网页或邮件中的恶意内容可以劫持代理的行为。Arc Gate 提供了一种简单实用的防御措施，可能成为基于 LangChain 构建的代理系统的标准安全层。 Arc Gate 的核心见解是提示注入是关于未经授权的指令权限转移，而非危险词汇。它作为 LangChain 回调工作，检测到注入时会抛出 ValueError，项目还包含一个实时演示页面，用户可以尝试破解该过滤器。

rss · r/artificial RSS · May 14, 23:06

**背景**: 提示注入是一种攻击方式，恶意文本被插入到大语言模型（LLM）的输入中，以覆盖其原始指令。LangChain 是一个开源框架，用于构建由 LLM 驱动的应用程序，包括可以与外部数据源交互的 AI 代理。Arc Gate 作为该生态系统中的安全工具，区分用户指令和来自网页、邮件或工具输出的不可信内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/LangChain">LangChain - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack? | IBM</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#agent security`, `#LangChain`, `#AI agents`, `#security tool`

---

<a id="item-11"></a>
## [字节跳动发布开源 Cola-DLM 模型](https://www.reddit.com/r/LocalLLaMA/comments/1tdtaqt/bytedanceseedcoladlm_hugging_face/) ⭐️ 8.0/10

字节跳动开源了 Cola-DLM，这是一个层次化连续潜在空间扩散语言模型，结合了文本 VAE 和通过流匹配训练的块因果扩散变压器（DiT）先验。 此次发布将基于扩散的语言模型替代方案引入开源生态，可能开启关于连续潜在空间生成的新研究，并在生成质量和速度之间提供不同的权衡。 该模型采用两阶段训练：先预训练文本 VAE，再联合训练 VAE 和 DiT，优化目标为流匹配。发布的检查点对应 2000 EFLOPs 计算量，使用 OLMo 2 分词器（词汇量 100,278），采用 Apache 2.0 许可证。

rss · r/LocalLLaMA RSS · May 15, 11:19

**背景**: 扩散模型通过逆转逐步加噪的过程来生成数据，已成为图像生成领域的先进技术。扩散变压器（DiT）用变压器替代传统 U-Net 骨干，提升了可扩展性。流匹配提供了一种免模拟的方法来训练连续归一化流。Cola-DLM 将这些技术适配到语言建模：首先通过 VAE 将文本编码到连续潜在空间，然后在该潜在空间中应用扩散过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Variational_autoencoder">Variational autoencoder - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2210.02747">[2210.02747] Flow Matching for Generative Modeling - arXiv.org</a></li>
<li><a href="https://arxiv.org/abs/2212.09748">[2212.09748] Scalable Diffusion Models with Transformers</a></li>

</ul>
</details>

**标签**: `#diffusion language models`, `#LLM`, `#ByteDance`, `#DiT`, `#flow matching`

---

<a id="item-12"></a>
## [小模型通过自我纠错训练，在 HumanEval 上达到 80%](https://www.reddit.com/r/LocalLLaMA/comments/1tde3m1/i_let_a_small_model_train_on_its_own_mistakes_it/) ⭐️ 8.0/10

这表明小模型可以在没有人类标注数据的情况下，通过可验证奖励的自我监督学习大幅提升性能，可能使 AI 训练民主化。同时，它显示基础模型可以媲美更大的、经过人类反馈调优的版本，挑战了广泛 RLHF 的必要性。 最初尝试因评分器 Bug（截断函数后再评分）而失败；修复后，Qwen 2.5 14B 基础模型与它自己的 RLHF 调优版本仅差 4 分。使用随机垃圾数据的对照实验未显示改进，证实自我纠错信号驱动了性能提升。

rss · r/LocalLLaMA RSS · May 14, 22:55

**背景**: HumanEval 是一个包含 164 个编程问题的基准测试，用于评估功能正确性。可验证奖励是来自外部评估器（如 Python 解释器）的二进制通过/未通过信号，在 DeepSeek-R1 的 GRPO 方法中使用。RunPod 是一个云 GPU 服务。基于错误自我训练是一种强化学习形式，模型从自身生成的修正中学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2503.06639v1">Reinforcement Learning with Verifiable Rewards: GRPO’s ...</a></li>
<li><a href="https://llm-stats.com/benchmarks/humaneval">HumanEval Benchmark Leaderboard</a></li>
<li><a href="https://gpus.io/en/providers/runpod">Runpod GPU Pricing & Review - Cloud GPU Provider Analysis</a></li>

</ul>
</details>

**标签**: `#LLM training`, `#self-improvement`, `#reinforcement learning`, `#small models`, `#HumanEval`

---

<a id="item-13"></a>
## [拆除 2024 款 RAV4 的调制解调器和 GPS 以阻止遥测](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 7.0/10

一篇详细指南发布，展示了如何从 2024 款丰田 RAV4 混合动力车上物理拆除蜂窝调制解调器和 GPS 模块，以防止车辆向丰田发送遥测数据。 这一点很重要，因为现代汽车越来越多地收集和传输敏感数据，而本指南为注重隐私的车主提供了一种恢复控制权的实用方法。同时，它也凸显了汽车公司利用驾驶员数据盈利的更广泛趋势。 作者指出，拆除调制解调器后，通过蓝牙连接手机仍会让汽车使用手机网络发送遥测数据，但使用有线 USB 连接则不会。指南还警告说，CarPlay 和 Android Auto 都会捕获各自的遥测数据。

hackernews · arkadiyt · May 14, 17:08 · [社区讨论](https://news.ycombinator.com/item?id=48138136)

**背景**: 现代汽车配备了远程信息处理控制单元（TCU），用于收集和传输车辆数据，通常用于导航、紧急服务以及数据变现。这种做法引发了隐私担忧，因为数据可能包括位置、驾驶行为甚至车内音频。作者的指南旨在通过物理拆除 TCU 组件来禁用连接功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telematic_control_unit">Telematic control unit - Wikipedia</a></li>
<li><a href="https://www.bbc.com/future/article/20260513-your-car-is-spying-on-you-its-about-to-get-worse">Trillions of miles of data : Your car is spying on you, and it's only just.....</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了额外的见解和担忧。有人指出，即使禁用了数据收集，汽车的蓝牙仍可通过手机网络传输遥测数据，而 USB 则不会。另一评论者提到 GPS 损坏导致导航问题，并对丰田拒绝修复表示失望。

**标签**: `#privacy`, `#telemetry`, `#IoT security`, `#car hacking`, `#data collection`

---

<a id="item-14"></a>
## [Antirez 发布 DwarfStar4 用于本地 DeepSeek 推理](https://antirez.com/news/165) ⭐️ 7.0/10

Antirez 发布了 DwarfStar4 (DS4)，这是一个极简、自包含的 LLM 推理运行时，专门用于在 Apple Silicon Mac 和 NVIDIA DGX Spark 系统上本地运行 DeepSeek V4 Flash 模型，主要支持 Metal 后端。 该项目为一个最强大的开放权重模型提供了高度优化、功能专注的推理引擎，使爱好者无需依赖通用框架即可本地运行 DeepSeek，并突显了消费级硬件上高效本地 LLM 部署的日益增长的需求。 DS4 需要 96GB VRAM，主要后端是 Metal，针对 96GB RAM 的 MacBook；它还支持 NVIDIA CUDA 和 AMD ROCm（ROCm 在一个独立社区维护的分支中）。该项目承认其得益于 llama.cpp 和 GGML。

hackernews · caust1c · May 14, 22:29 · [社区讨论](https://news.ycombinator.com/item?id=48142108)

**背景**: 像 DS4 这样的 LLM 推理运行时允许用户在自己的硬件上运行大型语言模型，从而保护隐私并降低成本。Metal 是 Apple 的低级 GPU API，可加速 macOS 和 iOS 上的图形和计算任务。DeepSeek 是一家中国 AI 公司，已发布多个强大的开放权重模型，包括 DeepSeek V4 Flash。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash local inference engine ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Metal_(API)">Metal (API) - Wikipedia</a></li>
<li><a href="https://developer.apple.com/metal/">Metal Overview - Apple Developer</a></li>

</ul>
</details>

**社区讨论**: 社区成员普遍持正面态度，一些人称赞其专注的设计和性能。用户 petercooper 分享了在 Mac Studio 上使用 Q4 版本的积极体验，指出它与其他代理一起表现良好。其他人评论了高 VRAM 要求（96GB），并将其比作家用计算机的早期阶段。

**标签**: `#LLM inference`, `#DeepSeek`, `#local LLM`, `#open source`, `#Metal backend`

---

<a id="item-15"></a>
## [Anthropic 发布 Claude for Legal，集成新工具](https://github.com/anthropics/claude-for-legal) ⭐️ 7.0/10

Anthropic 发布了 Claude for Legal，包含 20 多个 MCP 连接器和 12 个插件，旨在将 Claude 与法律软件集成，并自动化合同审查和起草等任务。 此次发布标志着生成式 AI 向法律行业的重要推进，但专家警告，使用 AI 处理法律任务可能损害律师-客户保密特权及数据隐私，对律师和客户构成严重风险。 该包包含针对 LexisNexis 等工具的连接器，以及针对特定实践领域的插件。然而，社区的一个拉取请求指出，初始版本可能无意中移除或破坏了现有的 Lexis 集成。

hackernews · Einenlum · May 14, 21:05 · [社区讨论](https://news.ycombinator.com/item?id=48141234)

**背景**: MCP（模型上下文协议）连接器允许 Claude 与外部软件工具交互。律师-客户保密特权保护律师与客户之间的机密通信不被法庭披露。如果未妥善保护，使用 AI 工具可能会暴露这些通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/claude-for-the-legal-industry">Claude for the legal industry | Claude</a></li>

</ul>
</details>

**社区讨论**: 评论者（包括一名律师）强烈警告，AI 聊天历史不受律师-客户保密特权保护，可能被用作证据。一些人对 Anthropic 的做法表示怀疑，指出以往法律 AI 的失败案例。其他人则质疑为何没有房地产工具，并指出可能存在 Lexis 集成问题。

**标签**: `#AI Agents`, `#Legal AI`, `#Claude`, `#Anthropic`, `#Ethics`

---

<a id="item-16"></a>
## [旧科技消亡，新 AI 时代难以诞生](https://www.baldurbjarnason.com/2026/the-old-world-of-tech-is-dying/) ⭐️ 7.0/10

Baldur Bjarnason 发表了一篇文章，认为旧科技产业正在消亡，而新的人工智能驱动时代难以诞生，文章还评论了监管和生产力问题。 该分析捕捉了科技行业转型的关键时刻，反映了人们对 AI 对生产力的影响以及监管在塑造未来方面的作用的广泛不确定性。 作者批评了以技术而非社会效应来定义的监管，这一概念被称为'technopolistic'。这篇文章在 Hacker News 上获得了很高的关注度，有 112 个点赞和 85 条评论。

hackernews · speckx · May 15, 12:29 · [社区讨论](https://news.ycombinator.com/item?id=48147793)

**背景**: 该文章考察了从旧科技产业（如广告科技、社交媒体）向以人工智能为中心的新产业的转型。它讨论了当前的监管框架可能不足，以及 AI 带来的生产力提升尚未完全实现的原因，这与关于技术停滞和更新的辩论相呼应。

**社区讨论**: 评论者大多称赞这篇文章富有洞察力且写得很好，一些人指出 AI 的巨大需求与挣扎的叙述相矛盾。其他人则强调了根据技术的社会影响而非技术本身进行监管的重要性。

**标签**: `#tech industry analysis`, `#AI`, `#regulation`, `#productivity`

---

<a id="item-17"></a>
## [GGUF 格式：单文件理念与缺失功能](https://nobodywho.ooo/posts/whats-in-a-gguf/) ⭐️ 7.0/10

对 GGUF 二进制格式的技术深度解析揭示了其内部结构，诸如单文件模块化和可扩展性等优势，并指出投影模型（例如视觉语言模型）通常单独存储，这违背了单文件理念。 GGUF 是通过 llama.cpp 进行本地 LLM 推理的标准格式；理解其设计权衡有助于用户和开发者更好地管理模型分发，而对缺失功能的讨论则指明了开源机器学习生态系统的未来改进方向。 GGUF 将令牌、元数据和张量存储在单个二进制文件中，支持可扩展的键值对。然而，多模态模型的投影模型通常作为单独的 GGUF 文件保留，这一决定被 GGUF 设计者 Philpax 所遗憾，因为它与最初的单文件设计目标相冲突。

hackernews · bashbjorn · May 14, 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48138332)

**背景**: GGUF 是从 GGML 演化而来的，GGML 是 llama.cpp 的原始文件格式，llama.cpp 是一个 C/C++推理引擎，用于在本地硬件上运行大型语言模型，依赖最少。与 PyTorch 的 safetensors 需要多个 JSON 配置文件不同，GGUF 将所有内容打包到一个自包含文件中，简化了模型分发和加载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>
<li><a href="https://huggingface.co/docs/hub/gguf">GGUF · Hugging Face</a></li>
<li><a href="https://medium.com/@vimalkansal/understanding-the-gguf-format-a-comprehensive-guide-67de48848256">Understanding the GGUF Format : A Comprehensive Guide | Medium</a></li>

</ul>
</details>

**社区讨论**: Philpax 对投影模型最终作为单独文件表示遗憾，希望有人能合并它们。uyzstvqs 称赞 GGML/GGUF 使得 llama.cpp 等本地 AI 工具在多个平台上完美运行。Amelius 批评了 GGUF 的可读性，将其与 XML 相比并认为不如 XML。Sharlin 指出，在图像生成领域，通过 safetensors 实现的单文件模型已经很常见。

**标签**: `#GGUF`, `#llama.cpp`, `#LLM inference`, `#local AI`, `#ML format`

---

<a id="item-18"></a>
## [克劳德代码处理大型代码库的智能搜索](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) ⭐️ 7.0/10

Claude Code 使用智能搜索，能够遍历文件系统、读取文件并使用 grep，避免了嵌入管道和集中式索引，官方博文详细介绍了这一点。 这种方法使开发者无需维护索引即可处理大型代码库，但实际使用中暴露出高令牌消耗和不完整的文件分析问题，展示了智能编码在规模上的权衡。 博客文章强调智能搜索在本地运行，无需将代码上传到服务器，但 HN 评论报告称，即使小型项目在第一个提示中也可能消耗掉 35% 的五小时使用限制，而且 Claude 最初可能只读取每个文件的前 40 行。

hackernews · shenli3514 · May 15, 04:15 · [社区讨论](https://news.ycombinator.com/item?id=48144494)

**背景**: 智能搜索是一种技术，AI 代理像人类开发者一样主动导航代码库，使用 grep 和文件遍历等工具来查找相关上下文，而不是依赖预先构建的嵌入索引。传统搜索方法需要维护一个集中式索引，这种索引在快速变化的代码库中可能过时或不完整。Claude Code 的智能搜索旨在通过动态探索代码库来克服这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dtunkelang.medium.com/agentic-search-as-an-agile-engineering-process-5514b0790e8e">Agentic Search as an Agile Engineering Process | by Daniel... | Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-search-practical-guide-ecommerce-teams-algolia-bpt3e">Agentic search : a practical guide for ecommerce teams</a></li>

</ul>
</details>

**社区讨论**: HN 评论者报告了复杂的体验：一些人赞赏智能方法避免了索引维护，而另一些人则强调高令牌成本（例如，小型项目每个提示消耗 35% 的使用限制）、超时以及 Claude 忽略指令的倾向。一位用户指出，Claude 最初只读取文件的前 40 行，后来通过 AST 分析修复了该方法，质疑其可靠性。

**标签**: `#Claude Code`, `#AI Agents`, `#Agentic Coding`, `#Best Practices`

---

<a id="item-19"></a>
## [人机回环治理：企业 AI 的幻觉？](https://www.reddit.com/r/artificial/comments/1td300k/i_think_humanintheloop_may_become_one_of_the/) ⭐️ 7.0/10

Reddit 上一篇文章指出，企业 AI 中的人机回环治理存在结构性缺陷，因为 AI 系统自行决定何时上报给人类，形成了自我参照的悖论。 这一批评揭示了随着 AI 系统从推荐转向自主执行，治理中存在的根本性紧张关系，可能削弱如欧盟 AI 法案等要求人工监督的法规效力。 作者列举了 AI 可能基于过时或不完整数据做出看似合理但错误的决策的例子，并建议从'人机回环'转向'人类治理的自主性'。

rss · r/artificial RSS · May 14, 16:16

**背景**: 人机回环治理是指在 AI 输出被采纳前由人类审查。但随着 AI 系统越来越多地承担风险分类和上报决策，人工监督变得依赖于 AI 自身的判断，形成了可能无法捕捉微妙错误的治理循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://airia.com/human-in-the-loop-enterprise-ai-controls/">Human in the Loop: The Enterprise Case for Keeping Humans in ...</a></li>
<li><a href="https://www.dnb.com/en-us/blog/ai/a-practical-model-for-agentic-era.html">Agentic AI Governance: Human at the Helm vs Human in the Loop</a></li>
<li><a href="https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/">Introducing the Agent Governance Toolkit: Open-source runtime security ...</a></li>

</ul>
</details>

**社区讨论**: 该帖子在 Reddit 上引发了讨论，评论者认同其内在悖论，并分享了自身经历的例子。许多人呼吁建立更健壮的治理架构，定义自治边界，而非依赖 AI 自我报告。

**标签**: `#AI governance`, `#human-in-the-loop`, `#AI safety`, `#enterprise AI`, `#autonomous agents`

---

<a id="item-20"></a>
## [InternLM 发布 35B 科学多模态模型 Intern-S2-Preview](https://www.reddit.com/r/LocalLLaMA/comments/1tdrw0s/internlminterns2preview_hugging_face/) ⭐️ 7.0/10

InternLM 发布了 Intern-S2-Preview，一个 350 亿参数的科学多模态基础模型，引入了任务缩放——增加科学任务的难度、多样性和覆盖范围——以实现与万亿参数级 Intern-S1-Pro 相媲美的强大性能。 该模型表明，任务缩放（而非简单地缩放参数或数据）可以在保持模型尺寸适中（35B）的同时，显著提升专业科学领域的能力，使高级 AI 更易于用于科学研究和 Agent 工作流。 Intern-S2-Preview 基于 Qwen3.5 进行继续预训练，采用从预训练到强化学习的全链条训练，是首个支持材料晶体结构生成的开源模型。它还具备带 KL loss 的多 token 预测（MTP）以实现高效 RL 推理，以及 CoT 压缩以缩短响应。

rss · r/LocalLLaMA RSS · May 15, 10:09

**背景**: 基础模型通常通过增加模型参数或训练数据量来缩放，但任务缩放侧重于在训练过程中扩展任务的多样性和难度。Intern-S2-Preview 将这种方法应用于分子建模和基于 Agent 的科学工作流等科学任务。该模型在保持通用推理和多模态能力的同时，在专业科学基准上表现优异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/">Towards a science of scaling agent systems: When and why agent systems work</a></li>
<li><a href="https://ourworldindata.org/scaling-up-ai">Scaling up: how increasing inputs has made artificial intelligence more ...</a></li>

</ul>
</details>

**标签**: `#open-source`, `#LLM`, `#multimodal`, `#science`, `#foundation model`

---

<a id="item-21"></a>
## [用户报告 Qwen 3.6 MTP 模型带来 1.5 倍速度提升](https://www.reddit.com/r/LocalLLaMA/comments/1tdns1i/used_over_a_million_tokens_in_three_separate/) ⭐️ 7.0/10

一位 Reddit 用户测试了 Qwen3.6-35B 的新型多令牌预测（MTP）版本，在大型上下文（高达 30 万 token）的编码项目中，与之前的测试相比，每秒 token 速度提升了约 1.5 倍。该用户使用了 Qwen3.6-35B-A3B-UD-Q5_K_S GGUF 模型，并通过 Docker 在 Ubuntu 上运行 llama.cpp MTP 原型服务器。 这次实际测试表明，MTP 可以显著加速本地 LLM 在真实代理工作流中的推理，可能使大上下文代码生成在消费级硬件上变得可行。这种加速可以降低开发者在本地运行强大模型以处理复杂多文件项目的门槛。 用户最初以为使用了 Q8_0 量化的 KV 缓存，但后来更正为 q4_0，并表示将用 Q8 重新测试。他们还由于在深上下文（约 20 万 token）时出现问题，从 35B MoE 模型切换到了 27B 非 MoE 模型。使用的 GPU 是 AMD Radeon R9700（32GB 显存），在 30 万上下文时显存占用为 28.3/32 GB。

rss · r/LocalLLaMA RSS · May 15, 06:20

**背景**: 多令牌预测（MTP）是一种训练技术，语言模型同时预测多个未来令牌，从而实现推测性解码，可以在不牺牲质量的情况下提高推理速度。Qwen3.6 是阿里巴巴 Qwen 团队最新的模型系列，其中 35B-A3B 变体是一种混合专家（MoE）模型，每个令牌仅激活 3B 参数，使其在本地部署中高效运行。本地 LLM 推理允许用户在自己的硬件上运行模型，而无需依赖云 API，提供了隐私和控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3.6">GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series ...</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#multi-token prediction`, `#local LLMs`, `#llama.cpp`, `#inference speed`

---

<a id="item-22"></a>
## [RAG 聊天机器人评测：昂贵模型表现反而不佳](https://www.reddit.com/r/LocalLLaMA/comments/1tdusvx/evaluated_a_rag_chatbot_and_the_most_expensive/) ⭐️ 7.0/10

一位开发者对客服 RAG 聊天机器人进行了评估，发现最昂贵的模型表现最差，而优化检索质量和去重后，质量提升了 19%，成本降低了 79%。 这表明在 RAG 系统中，检索质量和分块管理通常比模型大小更重要，系统化的评估可以大幅提升成本与性能的平衡。 评估使用 LLM 裁判（Claude Haiku 4.5）进行 0-10 分打分，并测试了 5 个模型。Gemma 4 26B 得分 7.88，而 Gemini 3.1 Flash Lite 得分为 7.33，但成本降低 75%。表现最差的是最贵的模型（帖子中未指名）。

rss · r/LocalLLaMA RSS · May 15, 12:24

**背景**: RAG（检索增强生成）结合文档检索与 LLM 生成，将答案锚定在提供的知识上。ChromaDB 是一个开源的向量数据库，用于存储和查询文档嵌入。相似度阈值设置不当会导致检索返回空结果，使 LLM 无法回答。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChromaDB">ChromaDB</a></li>
<li><a href="https://medium.com/aimonks/introduction-to-chromadb-vector-store-for-generative-ai-llms-28f90535086">Introduction To ChromaDB | Vector Store For Generative AI... | Medium</a></li>

</ul>
</details>

**标签**: `#RAG`, `#LLM evaluation`, `#chatbot`, `#retrieval`, `#cost-performance`

---

<a id="item-23"></a>
## [TurboQuant 研究：FP8 在 KV 缓存量化中优于 TurboQuant](https://www.reddit.com/r/LocalLLaMA/comments/1tdb4ic/a_first_comprehensive_study_of_turboquant/) ⭐️ 7.0/10

一项全面比较 TurboQuant 和 FP8 KV 缓存量化的研究发现，FP8 因其可忽略的精度损失和显著的性能提升而仍是最佳默认选择，而大多数 TurboQuant 变体并未显示出优势或反而降低了性能。 这对 LLM 推理效率至关重要，因为 KV 缓存量化对于减少长上下文服务中的内存使用至关重要。研究结果指导实践者优先选择 FP8 而非较新的 TurboQuant 方法用于生产部署。 TurboQuant k8v4 仅提供最小的容量提升（2.4 倍对 2 倍），但会带来吞吐量/延迟惩罚。TurboQuant 4bit-nc 适用于内存受限的边缘部署，但会牺牲精度和速度。激进的变体（k3v4-nc, 3bit-nc）显示出显著的精度下降，尤其是在推理任务上。

rss · r/LocalLLaMA RSS · May 14, 20:59

**背景**: KV 缓存存储来自 Transformer 注意力层的键值对，在长序列中占据主导内存。量化降低精度（如 FP8）以压缩缓存，用部分精度换取内存节省。TurboQuant 是一种较新的量化方法，使用极坐标和残差校正的向量量化，但这项研究表明它在大多数场景下表现不如 FP8。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant: Redefining AI efficiency with extreme compression</a></li>
<li><a href="https://arxiv.org/abs/2504.19874">[2504.19874] TurboQuant: Online Vector Quantization with Near ... TurboQuant - Wikipedia TurboQuant: Online Vector Quantization with Near-optimal ... turboquant - vLLM I spent 31 hours on the math behind TurboQuant so you don't ... TurboQuant Paper, arXiv & GitHub — Research Resources</a></li>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#quantization`, `#KV-cache`, `#TurboQuant`, `#LocalLLaMA`

---

<a id="item-24"></a>
## [本地运行 DeepSeek V4 Pro 的性能基准测试](https://www.reddit.com/r/LocalLLaMA/comments/1tdpk3f/i_have_even_faster_deepseek_v4_pro_at_home/) ⭐️ 7.0/10

一位用户分享了使用 ktransformers 框架在 EPYC 9374F CPU 和 RTX PRO 6000 Max-Q GPU 上本地运行 DeepSeek V4 Pro 模型的详细性能基准测试，在不同上下文深度（最高 131K tokens）下实现了约 7 tokens/秒的稳定生成速度。 该基准测试表明，通过 CPU-GPU 异构计算，可在消费级硬件上高效运行 1.6 万亿参数的 MoE 模型，减少对云服务的依赖，实现本地私有化推理。 预填充速度保持在约 46 tokens/秒，而生成速度随上下文深度从 0 增加到 65K tokens 而略微下降（7.54 降至 6.80 tokens/秒）。首 Token 延迟（TTFT）从深度 0 时的 12.9 秒增加到深度 65K 时的超过 1400 秒。

rss · r/LocalLLaMA RSS · May 15, 07:59

**背景**: KTransformers 是一个研究框架，通过 CPU/GPU 异构计算实现高效的大模型推理，利用系统内存和 CPU 计算将大模型卸载到有限 GPU 显存之外。DeepSeek V4 Pro 是混合专家（MoE）模型的预览版，总参数量 1.6 万亿，但每个 token 仅激活 49 亿参数，支持多达一百万个 token 的上下文窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/kvcache-ai/ktransformers">GitHub - kvcache-ai/ ktransformers : A Flexible Framework for...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://github.com/eugr/llama-benchy">GitHub - eugr/llama-benchy: llama-benchy - llama-bench style ...</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#ktransformers`, `#DeepSeek`, `#local LLM`, `#performance benchmarking`

---