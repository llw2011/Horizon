---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 50 items, 15 important content pieces were selected

---

1. [微软 BitLocker YellowKey 零日漏洞绕过加密](#item-1) ⭐️ 8.0/10
2. [MIT RLCR：教 AI 模型说‘不确定’](#item-2) ⭐️ 8.0/10
3. [谷歌与 Cloudflare 收窄 AI 代理的网络访问通道](#item-3) ⭐️ 8.0/10
4. [Hugging Face 发布 ml-intern 实现本地 AI 研究代理](#item-4) ⭐️ 8.0/10
5. [TinySearch：面向本地 LLM 的轻量级 MCP 网络搜索工具](#item-5) ⭐️ 8.0/10
6. [Claude AI 恢复价值 40 万美元的 11 年比特币钱包](#item-6) ⭐️ 7.0/10
7. [Anthropic 推出面向小企业的 Claude](#item-7) ⭐️ 7.0/10
8. [Notion 将工作空间转变为 AI 代理中心](#item-8) ⭐️ 7.0/10
9. [Nvidia 发布 NVFP4 量化版 Kimi 2.6 和 2.5 模型](#item-9) ⭐️ 7.0/10
10. [多令牌预测使 Qwen 在 LLaMA.cpp 上推理速度提升 40%](#item-10) ⭐️ 7.0/10
11. [Scenema Audio：零样本情感语音克隆发布](#item-11) ⭐️ 7.0/10
12. [RTX 5090 在 LLM 推理中的功耗与性能基准测试](#item-12) ⭐️ 7.0/10
13. [在 GTX 1080 上 30B MoE 模型实现 24+ tok/s](#item-13) ⭐️ 7.0/10
14. [Opendesk：通过 MCP 让 AI 在 WiFi 下控制多台电脑](#item-14) ⭐️ 7.0/10
15. [在 llama.cpp 中为 AMD ROCm 实现 TurboQuant TBQ4 KV 缓存和 MTP](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [微软 BitLocker YellowKey 零日漏洞绕过加密](https://www.tomshardware.com/tech-industry/cyber-security/microsoft-bitlocker-protected-drives-can-now-be-opened-with-just-some-files-on-a-usb-stick-yellowkey-zero-day-exploit-demonstrates-an-apparent-backdoor) ⭐️ 8.0/10

一名名为 Eclipse 的研究人员公布了 YellowKey 的概念验证（PoC）代码，这是一个零日漏洞利用，通过将特定文件放在 USB 闪存盘上并重启进入 Windows 恢复环境（WinRE）来绕过微软 BitLocker 加密，从而获得对受保护驱动器完全访问权限。第二个漏洞利用 GreenPlasma 针对 Windows CTFMON 中的权限提升漏洞，但尚未发布完整的 PoC。 此漏洞利用非常重要，因为 BitLocker 被企业和个人广泛用于保护丢失或被盗设备上的静态数据。这种绕过方式破坏了人们对 BitLocker 的信任，攻击者可能利用它访问敏感信息，或可能被执法机构用于取证数据恢复。 YellowKey 漏洞利用的原理是：将名为'FsTx'的文件夹写入 USB 闪存盘或 EFI 系统分区，然后通过强制重启触发 WinRE，打开一个具有完全访问 BitLocker 加密卷权限的命令提示符，无需密码或恢复密钥。GreenPlasma 被描述为一种本地权限提升漏洞，可赋予系统级访问权限，但其完整 PoC 尚未发布。

hackernews · cookiengineer · May 14, 02:45 · [社区讨论](https://news.ycombinator.com/item?id=48130519)

**背景**: BitLocker 是 Windows 内置的全盘加密功能，使用可信平台模块（TPM）来保护加密密钥。零日漏洞利用针对的是供应商未修补的漏洞，PoC 代码通常被发布以演示该缺陷。YellowKey 漏洞利用利用了 Windows 恢复环境（通常提供恢复工具），但可以被操纵以绕过身份验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/microsoft-bitlocker-protected-drives-can-now-be-opened-with-just-some-files-on-a-usb-stick-yellowkey-zero-day-exploit-demonstrates-an-apparent-backdoor">Microsoft BitLocker-protected drives can now be opened with just some files on a USB stick — YellowKey zero-day exploit demonstrates an apparent backdoor | Tom's Hardware</a></li>
<li><a href="https://www.forbes.com/sites/daveywinder/2026/05/13/microsoft-windows-alert-angry-hacker-drops-2-new-zero-day-exploits/">Microsoft Windows Alert—Angry Hacker Drops 2 New Zero-Day Exploits</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/">Windows BitLocker zero-day gives access to protected drives, PoC released</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些评论者认为该漏洞利用是 BitLocker 中故意设置后门的迹象，并批评微软对安全的承诺。另一些人则赞扬零日漏洞的公开披露，指出将其在市场上出售本可获得巨额利润，暗示其动机是道德的。还有技术讨论指出，当硬件安全（例如证书泄露导致的安全启动）已经受损时，BitLocker 本身存在局限性。

**标签**: `#security`, `#microsoft`, `#bitlocker`, `#zero-day`, `#exploit`

---

<a id="item-2"></a>
## [MIT RLCR：教 AI 模型说‘不确定’](https://www.reddit.com/r/LocalLLaMA/comments/1tczrop/mit_rlcr_teaching_ai_models_to_say_im_not_sure/) ⭐️ 8.0/10

MIT CSAIL 的研究人员引入了 RLCR（强化学习与校准奖励）训练方法，该方法在不牺牲准确性的情况下降低 AI 模型过度自信，使模型能够适当表达不确定性。 AI 系统的过度自信可能导致误导性和危险的输出，尤其是在医疗或自动驾驶等高风险的领域。RLCR 改善了模型校准，使 AI 输出更加可靠和值得信赖。 RLCR 使用一个奖励信号，对错误答案的高置信度进行惩罚，对正确答案的低置信度进行奖励，这不同于事后校准方法。该方法使用 20,000 个示例进行训练，并通过精确字符串匹配来计算正确性，其表现优于训练后校准方法。

rss · r/LocalLLaMA RSS · May 14, 14:24

**背景**: AI 模型经常产生不反映其真实准确性的置信度分数，这个问题称为校准不良。传统的校准方法是在训练后应用的，而 RLCR 将校准直接集成到强化学习训练过程中，使模型能够同时学习正确性和适当的置信度。该研究详细见于论文《Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty》（arXiv:2507.16806）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2507.16806">Beyond Binary Rewards: Training LMs to Reason About Their...</a></li>
<li><a href="https://www.commonwealthunion.com/ai-that-knows-when-its-wrong-rlcr-training-method-tackles-dangerous-overconfidence/">AI That Knows When It’s Wrong? RLCR Training Method Tackles...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#calibration`, `#reasoning`, `#RL`, `#MIT`

---

<a id="item-3"></a>
## [谷歌与 Cloudflare 收窄 AI 代理的网络访问通道](https://www.reddit.com/r/LocalLLaMA/comments/1tcaboi/websearch_is_coming_to_a_screeching_performance/) ⭐️ 8.0/10

谷歌正在逐步取消其免费的特定站点搜索功能，仅保留 50 个域名的免费额度，最终截止日期为 2027 年 1 月 1 日，且高级搜索无公开定价。同时，Cloudflare 已将反 AI 爬虫保护设为所有客户的默认设置，并与 GoDaddy 合作扩大覆盖范围。 这些变化直接影响了依赖网络搜索获取实时数据的 AI 代理和本地模型，可能削弱其联网能力。社区现在必须寻找或构建开源替代方案以维持代理功能。 谷歌的 Custom Search API 目前每天免费提供 100 次查询，但新政策将特定站点搜索限制为总共 50 个域名。Cloudflare 的“AI Labyrinth”向爬虫提供无意义内容以消耗其资源，而与 GoDaddy 的合作影响了其托管的数百万个域名。

rss · r/LocalLLaMA RSS · May 13, 19:35

**背景**: AI 代理通常依赖网络爬取或搜索 API 获取最新信息。谷歌的 Custom Search API 是常见的付费方式，而免费爬虫面临 Cloudflare 等服务的日益封锁。Cloudflare 目前将超过 30%的爬虫流量识别为恶意并进行挑战。这些障碍促使开发者转向隐身浏览器或专用爬取服务，但这一趋势威胁着开源 AI 工具的可行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.google.com/custom-search/v1/overview">Custom Search JSON API | Google for Developers</a></li>
<li><a href="https://www.businessinsider.com/thwart-big-tech-ai-bots-feed-them-gibberish-cloudflare-2025-4">How to Thwart Big Tech's Data-Sucking AI Bots ... - Business Insider</a></li>

</ul>
</details>

**社区讨论**: Reddit 帖子表达了沮丧，警告网络搜索正返回 400 错误，并呼吁社区驱动开源项目填补空白。用户可能会讨论分布式搜索索引、自建爬虫或新 API 等替代方案，但未提供具体评论。

**标签**: `#web scraping`, `#AI agents`, `#Google search`, `#Cloudflare`, `#open source`

---

<a id="item-4"></a>
## [Hugging Face 发布 ml-intern 实现本地 AI 研究代理](https://www.reddit.com/r/LocalLLaMA/comments/1tcu5r8/automated_ai_researcher_running_locally_with/) ⭐️ 8.0/10

Hugging Face 发布了 ml-intern，这是一个代理框架，可以结合 llama.cpp 或 ollama 在本地运行自动化的 AI 研究，并与 transformers、datasets、trl 等开源库集成。 这使得 AI 研究者可以在笔记本电脑上全天候运行自动化工作流，而无需担心 API 令牌限制，从而使代理式研究更加可及且成本更低。 该框架最初为 Claude Opus 构建，现在支持本地模型；演示中 Qwen3.6-35B-A3B 通过编排 CPU/GPU 沙箱和 Hub 任务，端到端地执行监督微调。

rss · r/LocalLLaMA RSS · May 14, 10:32

**背景**: Llama.cpp 是一个开源库，能在本地硬件（包括笔记本电脑）上高效运行大型语言模型。代理框架提供工具和系统提示，使 LLM 能够自主执行复杂的多步骤任务，例如训练其他模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/">GitHub - ggml-org/llama.cpp: LLM inference in C/C++ · GitHub</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#agentic framework`, `#open-source`, `#Hugging Face`, `#local LLM`

---

<a id="item-5"></a>
## [TinySearch：面向本地 LLM 的轻量级 MCP 网络搜索工具](https://www.reddit.com/r/LocalLLaMA/comments/1tczzga/a_very_lightweight_open_websearch_tool_for/) ⭐️ 8.0/10

TinySearch 是一个开源 MCP 工具，通过 DuckDuckGo 进行网络搜索，使用 Crawl4AI 抓取页面，并通过分块、检索和重排序返回精简的上下文块，减少小型本地 LLM 的上下文过载。 它解决了本地代理设置中的一个关键痛点——网页结果冗长导致的上下文过载——使小型模型能够使用网络搜索而不会在抓取的垃圾信息上浪费上下文，让本地 LLM 代理更加实用。 它使用 DuckDuckGo 进行搜索，Crawl4AI 进行抓取，并结合了密集检索和 BM25 式检索与重排序。它还支持作为 FastAPI 服务器运行，在 M4 Mac 等硬件上端到端耗时 5-12 秒。

rss · r/LocalLLaMA RSS · May 14, 14:32

**背景**: MCP（模型上下文协议）是 Anthropic 引入的开放标准，用于标准化 AI 系统与外部工具和数据源的集成方式。Cline 和 Roo 是流行的本地编码代理，依赖工具调用能力。TinySearch 通过提供尊重小型模型上下文限制的轻量级网络搜索工具，融入这一生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://docs.crawl4ai.com/">Crawl 4 AI , Open-source LLM-Friendly Web Crawler & Scraper</a></li>
<li><a href="https://mychen76.medium.com/vibe-coding-locally-with-cline-roo-and-ollama-better-experience-a8846c829d66">Vibe Coding ‘Locally’ with Cline/Roo and Ollama — Better Experience!</a></li>

</ul>
</details>

**标签**: `#MCP`, `#web-search`, `#local-LLM`, `#agent-tooling`, `#open-source`

---

<a id="item-6"></a>
## [Claude AI 恢复价值 40 万美元的 11 年比特币钱包](https://www.tomshardware.com/tech-industry/cryptocurrency/bitcoin-trader-recovers-usd400-000-using-claude-ai-after-losing-wallet-password-11-years-ago-bot-tried-3-5-trillion-passwords-before-decrypting-an-old-wallet-backup) ⭐️ 7.0/10

一名用户使用 Claude AI 对丢失的密码进行暴力破解，成功恢复了 11 年间无法访问的价值 40 万美元的比特币钱包。该 AI 尝试了 3.5 万亿种密码组合，最终成功解密了钱包备份。 这展示了 AI 在密码恢复任务中的实际应用，突显了大语言模型如何在典型对话或编程之外协助解决复杂问题。同时也引发了关于 AI 代理在现实世界安全漏洞和密码恢复中潜力的关注。 用户在一本大学笔记本中找到了旧的助记词种子短语，这是实现针对性暴力破解的关键突破。Claude AI 被用来编写和执行密码破解脚本，利用其对加密钱包格式的理解以及协调恢复过程的能力。

hackernews · cednore · May 14, 14:49 · [社区讨论](https://news.ycombinator.com/item?id=48136240)

**背景**: 比特币钱包由私钥或密码保护；丢失它们可能导致资金永久锁定。传统的密码恢复通常使用诸如 hashcat 之类的专用工具，但需要专业技术知识。Claude AI 是 Anthropic 开发的大语言模型，能够生成代码并解决多步骤问题，使非专家也能尝试此类恢复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://hashcat.net/">hashcat - World's fastest and most advanced password recovery utility</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了类似的使用 Claude AI 处理非显而易见任务的故事，例如恢复损坏的图像和从浏览器内部提取文本。有人指出找到种子短语才是真正的突破，任何密码破解软件都可以完成暴力破解，但也有人称赞 Claude 编写自定义脚本的能力。

**标签**: `#Claude AI`, `#cryptocurrency`, `#AI agents`, `#practical AI`, `#recovery`

---

<a id="item-7"></a>
## [Anthropic 推出面向小企业的 Claude](https://www.anthropic.com/news/claude-for-small-business) ⭐️ 7.0/10

Anthropic 宣布推出 Claude for Small Business，这是一个专为中小企业定制的订阅计划，提供 AI 驱动的功能，如发票处理、工资对账和早间简报。 此举标志着 Anthropic 战略性地进入中小企业市场，挑战 Microsoft Copilot 等现有工具。它可能使技术资源有限的小型企业能够利用 AI 自动化，从而可能改变其生产力和运营方式。 该服务与电子邮件和会计软件等常见商业工具集成，利用 Claude 的代理能力实现任务自动化。社区讨论指出，为 Claude Code 提供用户友好的界面可以进一步促进非开发人员的采用，但当前的实现仍需要一定的技术知识。

hackernews · neilfrndes · May 14, 03:59 · [社区讨论](https://news.ycombinator.com/item?id=48130950)

**背景**: Anthropic 是一家由前 OpenAI 员工创立的 AI 安全公司，开发了 Claude 系列大型语言模型。Claude Code 是一个命令行工具，允许开发人员将编码任务委托给 AI 代理。新的 SMB 产品旨在将类似的代理能力带给非技术业务用户，自动化重复的行政任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://michaelcrist.substack.com/p/personal-ai-assistant">How I Built My Personal AI Assistant (Claude Code Tutorial)</a></li>
<li><a href="https://www.bcg.com/capabilities/artificial-intelligence/ai-agents">AI Agents: What They Are and Their Business Impact | BCG</a></li>

</ul>
</details>

**社区讨论**: 评论总体上是积极的，用户分享了非开发人员使用 Claude Code 自动化任务（如发票分类）的成功案例。然而，一些欧洲用户质疑该服务在其地区的价值，指出工资对账已经很简单。总体而言，人们对让普通用户更容易使用 AI 代理表现出浓厚兴趣。

**标签**: `#Claude`, `#AI agents`, `#Anthropic`, `#small business`, `#productivity`

---

<a id="item-8"></a>
## [Notion 将工作空间转变为 AI 代理中心](https://techcrunch.com/2026/05/13/notion-just-turned-its-workspace-into-a-hub-for-ai-agents/) ⭐️ 7.0/10

2026 年 5 月 13 日，Notion 推出了一个新的开发者平台，使团队能够将 AI 代理、外部数据源和自定义代码直接集成到其工作空间中。 这使 Notion 成为代理式生产力中心，用户可以无需离开平台即可自动化复杂工作流，可能重塑企业管理和处理任务与数据的方式。 该平台支持使用 Workers 和持久化游标将外部记录持续写入 Notion 数据库，并提供声明式模式以实现集成灵活性。

rss · TechCrunch AI · May 13, 21:45

**背景**: Notion 是一款广泛使用的笔记、数据库和项目管理工作空间工具。AI 代理是能够执行任务的自主软件系统，而代理框架帮助开发者构建此类代理。Notion 的开发者平台降低了团队将 AI 代理能力直接嵌入日常工作的门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notion.com/product/dev">Build with Notion’s Developer Platform</a></li>
<li><a href="https://makewithnotion.com/">Notion Developer Platform Launch — May 13</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#agentic frameworks`, `#Notion`, `#productivity`, `#developer platform`

---

<a id="item-9"></a>
## [Nvidia 发布 NVFP4 量化版 Kimi 2.6 和 2.5 模型](https://www.reddit.com/r/LocalLLaMA/comments/1tcxb77/nvfp4_kimi26_and_kimi_25_released_by_nvidia/) ⭐️ 7.0/10

Nvidia 使用 Model Optimizer 库发布了 Moonshot AI 的 Kimi-K2.6 和 Kimi-K2.5 模型的 NVFP4 量化版本，基准测试结果显示在多项指标上与原生 INT4 基线性能相当甚至略有提升。 这表明 NVFP4 量化可在保持精度的同时将模型大小减少约 2 倍，从而在 Nvidia 硬件上更高效地部署 Kimi 等大型 MoE 模型。同时展示了 Nvidia Model Optimizer 在生产环境量化中的实际应用。 NVFP4 量化的 Kimi-K2.6 模型在 GPQA Diamond 上得分为 90.4（基线 90.9），SciCode 上 54.4（基线 52.6），MMMU Pro 上 76.5（基线 75.6），精度损失极小，部分基准甚至略有提升。这些模型已在 Hugging Face 上发布，可用于商业和非商业用途。

rss · r/LocalLLaMA RSS · May 14, 12:53

**背景**: NVFP4 是 Nvidia 的 4 位浮点量化格式，采用 E4M3 FP8 变体和非二的幂缩放因子以实现更精确的编码。Kimi-K2.6 和 Kimi-K2.5 是 Moonshot AI 基于混合专家（MoE）架构开发的大语言模型，总参数量 1 万亿，激活参数 320 亿。Nvidia Model Optimizer 是一个统一的模型压缩库，支持量化、剪枝、蒸馏等技术，目标部署在 TensorRT-LLM 和 vLLM 上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | NVIDIA Technical Blog</a></li>
<li><a href="https://github.com/NVIDIA/Model-Optimizer">GitHub - NVIDIA/Model-Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#model quantization`, `#Nvidia`, `#Kimi`, `#LLM inference`, `#HuggingFace`

---

<a id="item-10"></a>
## [多令牌预测使 Qwen 在 LLaMA.cpp 上推理速度提升 40%](https://www.reddit.com/r/LocalLLaMA/comments/1tckzy2/multitoken_prediction_mtp_for_qwen_on_llamacpp/) ⭐️ 7.0/10

一位开发者在 LLaMA.cpp 的分支中集成了针对 Qwen 模型的多令牌预测（MTP）和 TurboQuant，在 MacBook Pro M5 Max 上实现了 40%的加速（从 21 tok/s 提升到 34 tok/s），接受率达到 90%。 这一突破在不损失质量的前提下显著提升了本地 LLM 推理速度，使高性能 AI 更贴近消费级硬件。它展示了将推测解码技术与先进量化方法结合用于边缘部署的实际可行性。 该实现利用 MTP 中的轻量级草稿模型并行预测多个令牌，目标 Qwen 模型通过单次前向传递进行验证。TurboQuant 通过接近最优失真的向量量化进一步减小模型大小，使 27B 和 35B 的 Qwen 模型能够在配备 64GB RAM 的 MacBook 上高效运行。

rss · r/LocalLLaMA RSS · May 14, 02:35

**背景**: 多令牌预测（MTP）是一种推理加速技术：小型草稿模型同时预测多个未来令牌，较大的目标模型通过单次前向传递验证这些预测，从而提高吞吐量。TurboQuant 是 Google Research 开发的向量量化方法，能够在极小精度损失下压缩模型权重和 KV 缓存。LLaMA.cpp 是一个流行的开源 C++实现，用于在 CPU 和 GPU 上高效运行量化后的 LLM。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Multi-Token Prediction`, `#LLaMA.cpp`, `#TurboQuant`, `#LLM Inference`, `#Local LLM`

---

<a id="item-11"></a>
## [Scenema Audio：零样本情感语音克隆发布](https://www.reddit.com/r/LocalLLaMA/comments/1tcwqdd/scenema_audio_zeroshot_expressive_voice_cloning/) ⭐️ 7.0/10

Scenema AI 发布了 Scenema Audio 的模型权重和推理代码，这是一个零样本情感语音克隆和语音生成模型，它将情感表现与声音身份分离，使任何声音都能在没有事先录音的情况下表现任何情感。 这一开源版本使开发者能够将高度表现力、可控制情感的语音合成集成到应用中，将语音克隆从中性 TTS 推进，并使自然情感语音生成更加普及。 该模型是基于扩散的音频模型，源自 LTX 2.3，只需要一段文本提示来控制情感，以及可选的 10 秒参考音频用于语音克隆；它支持 8 步去噪和带有自动 VRAM 管理的 Docker REST API。

rss · r/LocalLLaMA RSS · May 14, 12:29

**背景**: 传统的文本到语音（TTS）系统难以自然地传达情感，且大多数语音克隆模型需要多个样本或无法泛化到未见过的情感。零样本语音克隆旨在通过简短录音复制说话者的身份，无需额外训练。Scenema Audio 的创新之处在于将情感表达与声音身份解耦，使用户能够独立于说话者的声音控制语音的情感表现（如愤怒、兴奋）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ScenemaAI/scenema-audio">GitHub - ScenemaAI/scenema-audio: Zero-shot expressive voice cloning and speech generation. Generate anything from short clips to full-length audiobooks with realistic emotional delivery, pacing, and breath control. Clone any voice from a 10-second reference and perform emotions the original speaker never recorded. · GitHub</a></li>
<li><a href="https://scenema.ai/audio">Scenema Audio: Zero-Shot Expressive Voice Cloning and Speech Generation | Scenema AI</a></li>

</ul>
</details>

**标签**: `#voice cloning`, `#speech generation`, `#open-source`, `#zero-shot`, `#AI/ML`

---

<a id="item-12"></a>
## [RTX 5090 在 LLM 推理中的功耗与性能基准测试](https://www.reddit.com/r/LocalLLaMA/comments/1tcvji7/benchmark_5090rtx_promt_parsing_token_generation/) ⭐️ 7.0/10

一位 Reddit 用户对 RTX 5090 GPU 进行本地 LLM 推理基准测试，测量了提示解析速度、令牌生成速率以及 400W–600W 范围内的功耗，以确定最佳功耗水平。 这为 LLM 爱好者和研究人员提供了实用数据，帮助优化推理时的 GPU 功耗设置，有望在不显著牺牲性能的情况下降低电费和发热。 使用 llama.cpp 和 Qwen3.6-27B 模型（Q6_K_P 量化），基准测试显示提示处理对功耗限制比令牌生成更敏感；RTX 5090 在 600W 限制下峰值达 592W，且功耗尖峰超出设定限制 10–12W。

rss · r/LocalLLaMA RSS · May 14, 11:38

**背景**: 提示解析和令牌生成是 LLM 推理的两个关键阶段：解析处理输入上下文，而生成产生输出令牌。GPU 功耗限制可降低最大功耗，在适度限制下通常会导致近乎线性的性能下降，但不同工作负载的反应有所不同。

**标签**: `#LLM inference`, `#GPU benchmarking`, `#token generation`, `#power optimization`

---

<a id="item-13"></a>
## [在 GTX 1080 上 30B MoE 模型实现 24+ tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1tcc7h5/24_toks_from_30b_moe_models_on_an_old_gtx_1080_8/) ⭐️ 7.0/10

一位用户在老旧 GTX 1080（8 GB 显存）上，通过 llama.cpp 和 TurboQuant KV 缓存量化技术，结合 CPU 卸载冷专家权重，成功让 Qwen 3.6 35B-A3B 和 Gemma 4 26B-A4B MoE 模型在 128k 上下文下达到 24+ tokens/秒。 这表明大型混合专家模型可以在十年前的消费级硬件上高效运行，大大降低了本地 LLM 推理的门槛，并使长上下文应用无需昂贵 GPU 即可实现。 关键技术是 MoE 卸载：llama.cpp 将不常用的专家权重放在系统 RAM 中，并通过 PCIe 3.0 流式传输到 GPU，同时将热层和 KV 缓存保留在 GPU 上。此外，Gemma 4 的多令牌预测（MTP）需要手动修复，将嵌入表移至 GPU，以获得约 22%的速度提升。

rss · r/LocalLLaMA RSS · May 13, 20:41

**背景**: 混合专家（MoE）模型在每层使用多个专门的子网络（专家），但每个令牌仅激活一部分，从而降低计算成本。TurboQuant 是 Google DeepMind 提出的一种 KV 缓存量化算法，可将缓存压缩至 3 比特，且精度损失极小。多令牌预测（MTP）是一种让模型同时预测多个未来令牌的技术，可用于推测解码以加速推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/0xSero/turboquant">GitHub - 0xSero/ turboquant : TurboQuant : Near-optimal KV cache ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2404.19737">[2404.19737] Better & Faster Large Language Models via Multi-token Prediction</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#quantization`, `#MoE`, `#llama.cpp`, `#local LLM`

---

<a id="item-14"></a>
## [Opendesk：通过 MCP 让 AI 在 WiFi 下控制多台电脑](https://www.reddit.com/r/LocalLLaMA/comments/1tcpgsv/computeruse_mcp_that_can_control_multiple/) ⭐️ 7.0/10

Opendesk 是一个开源工具，它利用 Computer-use MCP（模型上下文协议）让 AI 代理能够通过 WiFi 在远程电脑上查看、点击、输入和导航，无需云服务或账号。 这使 AI 代理的能力从单机控制扩展到本地网络上的多机编排，为远程桌面管理、测试和多设备工作流带来了强大的自动化能力。 该工具免费、开源，支持 Mac、Linux 和 Windows。通信完全在本地网络进行并全加密，只需配对一次。

rss · r/LocalLLaMA RSS · May 14, 06:13

**背景**: 模型上下文协议 (MCP) 是 Anthropic 于 2024 年 11 月推出的开放标准，用于连接 AI 助手与外部系统。Computer-use MCP 是一个专用服务器，允许像 Claude 这样的 AI 模型控制计算机的鼠标和键盘。Opendesk 在此基础上实现了远程控制多台机器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol</a></li>
<li><a href="https://github.com/domdomegg/computer-use-mcp">GitHub - domdomegg/ computer - use - mcp : Give AI models...</a></li>

</ul>
</details>

**标签**: `#MCP`, `#Computer Use`, `#Multi-machine`, `#AI Agents`, `#Desktop Control`

---

<a id="item-15"></a>
## [在 llama.cpp 中为 AMD ROCm 实现 TurboQuant TBQ4 KV 缓存和 MTP](https://www.reddit.com/r/LocalLLaMA/comments/1tcrtxm/turboquantmtp_for_rocmllama_cpp/) ⭐️ 7.0/10

一位开发者在 llama.cpp 中为 AMD ROCm GPU 实现了 TurboQuant TBQ4 KV 缓存和多令牌预测（MTP），使得在 24GB 显存上达到 64k 上下文，并提升了令牌生成速率。 此优化显著扩展了消费级 AMD GPU 上可用的上下文长度，使 ROCm 在本地 LLM 推理中更具竞争力，无需昂贵硬件即可处理更大规模的任务。 在 RX 7900 XTX 上使用 Qwen3.6-27B Q4_K_M MTP GGUF 模型测试，TBQ4 KV 缓存在 64k 上下文时达到 38-54 tok/s，占用约 20 GB 显存；而 q8_0 基线在 32k 上下文时占用约 22-23 GB 显存，速度降至约 31 tok/s。

rss · r/LocalLLaMA RSS · May 14, 08:24

**背景**: TurboQuant 是一种接近最优的向量量化方法，可将 KV 缓存压缩 4-7 倍，同时质量损失极小。MTP（多令牌预测）利用模型内置的草稿头进行推测解码，每次前向传播生成多个令牌。两者结合可在有限显存内容纳极长上下文，同时保持高吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://turbo-quant.com/turboquant">TurboQuant Algorithm: PolarQuant + QJL Explained for Developers</a></li>
<li><a href="https://github.com/Firmamento-Technologies/TurboQuant">GitHub - Firmamento-Technologies/ TurboQuant : Near-optimal vector...</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#ROCm`, `#quantization`, `#MTP`, `#llama.cpp`

---