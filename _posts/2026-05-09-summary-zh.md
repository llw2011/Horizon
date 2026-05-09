---
layout: default
title: "Horizon Summary: 2026-05-09 (ZH)"
date: 2026-05-09
lang: zh
---

> From 103 items, 15 important content pieces were selected

---

1. [Teaching Claude Why: 让 LLM 学会推理指令意图](#item-1) ⭐️ 9.0/10
2. [Gowers 称 ChatGPT 5.5 Pro 可解决“温和”数学问题](#item-2) ⭐️ 8.0/10
3. [MTP + TurboQuant 在 RTX 4090 上为 Qwen3.6-27B 实现 80+ t/s](#item-3) ⭐️ 8.0/10
4. [DeepSeek 寻求 73.5 亿美元融资，下月发布 V4.1](#item-4) ⭐️ 8.0/10
5. [在 Apple Silicon 上通过 PCI 直通实现 CUDA 推理](#item-5) ⭐️ 8.0/10
6. [DS4：为 MacBook 优化的 DeepSeek 4 Flash 推理引擎](#item-6) ⭐️ 8.0/10
7. [生产环境 UUID v4 碰撞报告：仅 15,000 条记录就发生了重复](#item-7) ⭐️ 7.0/10
8. [AI 提前 3 年检测胰腺癌，超越人类医生](#item-8) ⭐️ 7.0/10
9. [新基准测试 AI 编码代理在编辑中的一致性](#item-9) ⭐️ 7.0/10
10. [AMD 开源 GAIA AI 现已集成 Gmail](#item-10) ⭐️ 7.0/10
11. [Qwen 35B-A3B 在 12GB 显存上经过调优运行良好](#item-11) ⭐️ 7.0/10
12. [AI2 发布 EMO：1B 激活参数的文档级领域路由 MoE 模型](#item-12) ⭐️ 7.0/10
13. [MTP 接受率决定推理加速效果](#item-13) ⭐️ 7.0/10
14. [Gemma 4 26B 在单张 RTX 5090 上通过 DFlash 达到 600 tok/s](#item-14) ⭐️ 7.0/10
15. [Ring 2.6 1T 模型在 OpenRouter 上免费提供；希望开放权重](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Teaching Claude Why: 让 LLM 学会推理指令意图](https://www.anthropic.com/research/teaching-claude-why) ⭐️ 9.0/10

Anthropic 的 'Teaching Claude Why' 研究提出了一种训练大语言模型推理指令背后目的的方法，从而提升了对齐性和能力。 该方法通过让模型理解潜在意图，降低遵循有害指令的可能性，可能显著提升 AI 安全性，并且该方法从 Claude 推广到了开放权重模型。 该研究基于 Anthropic 早前的 agentic misalignment 案例研究，并包括针对玩具价值观微调的开放模型（Llama 3.1 8B, Qwen 2.5 32B, Qwen 3 32B）。相关论文'Model Spec Midtraining'（arXiv:2605.02087）讨论了类似结果。

hackernews · pretext · May 8, 17:59 · [社区讨论](https://news.ycombinator.com/item?id=48066592)

**背景**: 大语言模型通常被训练去字面遵循指令，这在指令与伦理准则冲突时可能导致失调行为。基于人类反馈的强化学习（RLHF）是一种常见的对齐技术，但往往无法捕捉对意图的推理。'Teaching Claude Why'旨在赋予模型推断指令目的的能力，类似于教它们'为什么'而非仅仅是'是什么'。这与推理模型和思维链提示的研究方向一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/teaching-claude-why">Teaching Claude why \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论者就更广泛的对齐定义、教育学类比和哲学含义展开了讨论。一些人称赞了该研究向开放模型的泛化能力及其独特的艺术风格。

**标签**: `#AI alignment`, `#Claude`, `#model reasoning`, `#Anthropic`, `#agent alignment`

---

<a id="item-2"></a>
## [Gowers 称 ChatGPT 5.5 Pro 可解决“温和”数学问题](https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/) ⭐️ 8.0/10

菲尔兹奖得主、剑桥数学家 Timothy Gowers 报告称，ChatGPT 5.5 Pro 成功解决了一系列“温和”的研究级数学问题，这一能力他此前以为还需数十年才能实现。 这表明大语言模型正接近能够自动化部分数学研究，尤其是常规或“温和”问题，这可能根本性地改变博士生培养方式以及人类数学家可承担的任务。 Gowers 指出，该模型在他自己研究中的一个“温和”问题上的表现非常详尽，以至于他本可以根据 LLM 的输出直接撰写论文，但他强调模型在更困难的问题上仍然失败，且需要仔细的提示。

hackernews · _alternator_ · May 9, 02:41 · [社区讨论](https://news.ycombinator.com/item?id=48071262)

**背景**: “温和问题”是指研究级别的数学问题，对初学者可触及但不简单；它们常作为博士生的起点。Gowers 一直是关于人工智能对数学影响的知名声音，此前组织了 Polymath 项目来众包问题解决，并预测了数学实践的变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Timothy_Gowers">Timothy Gowers - Wikipedia</a></li>
<li><a href="https://numberwarrior.wordpress.com/2009/03/25/a-gentle-introduction-to-the-polymath-project/">A gentle introduction to the Polymath project | The Number Warrior</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了敬畏与担忧的混合情绪：一些人指出，在学术界尤其是东欧，获得此类模型访问存在财务障碍；另一些人则反思了对于数学家工作目的感和通过工作实现永生的情感与哲学影响。

**标签**: `#AI`, `#LLM`, `#mathematical reasoning`, `#OpenAI`, `#ChatGPT`

---

<a id="item-3"></a>
## [MTP + TurboQuant 在 RTX 4090 上为 Qwen3.6-27B 实现 80+ t/s](https://www.reddit.com/r/LocalLLaMA/comments/1t7kyju/got_mtp_turboquant_running_qwen3627b_80_ts_at/) ⭐️ 8.0/10

一位开发者在单张 RTX 4090 上，结合多 Token 预测（MTP）与 TurboQuant KV 缓存量化（TBQ4_0），为 Qwen3.6-27B 模型在 262K 上下文长度下实现了每秒 80-87 个 token 的推理速度。相关实现已在 GitHub 开源，并附有技术博客详解。 这表明，接近无损的 KV 缓存压缩（TurboQuant）和投机解码（MTP）可以显著加速消费级硬件上的本地 LLM 推理，使具有长上下文的大模型在实时代理应用中变得实际可行。其吞吐量几乎达到了同类模型典型值的两倍。 所用模型为 Qwen3.6-27B-Heretic-v2 Q4_K_M，并接入了 MTP 头，运行于 Ubuntu 24.04 和 CUDA 12.x。MTP 的草稿接受率约为 73%，使用 3 个草稿 token。该分支基于 llama.cpp，代码可构建以供复现。

rss · r/LocalLLaMA RSS · May 8, 21:15

**背景**: 多 Token 预测（MTP）是一种投机解码技术，由一个小型草稿模型并行预测多个未来 token，再由主模型验证，通过每次前向处理多个 token 来实现加速。TurboQuant 是 Google DeepMind 提出的算法，可将 KV 缓存压缩至每个值 3 比特，精度损失可忽略不计，从而显著降低长上下文的显存占用。两者结合使得在单张 24GB GPU 上以高吞吐运行 27B 参数、262K 上下文的模型成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/0xSero/turboquant">GitHub - 0xSero/ turboquant : TurboQuant : Near-optimal KV cache ...</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/Multi_Token_Prediction.html">Multi Token Prediction (MTP) — vllm-ascend</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#quantization`, `#Multi-Token Prediction`, `#llama.cpp`, `#TurboQuant`

---

<a id="item-4"></a>
## [DeepSeek 寻求 73.5 亿美元融资，下月发布 V4.1](https://www.reddit.com/r/LocalLLaMA/comments/1t7bfpw/reports_suggest_deepseek_is_seeking_735_billion/) ⭐️ 8.0/10

据报道，DeepSeek 正寻求在首轮融资中筹集高达 73.5 亿美元（500 亿元人民币），创始人梁文锋将贡献最大允许额度。该公司还计划于 6 月发布其大语言模型 V4.1 更新。 若完成，这将成为中国 AI 史上单笔最大的融资轮，标志着 DeepSeek 加速推进商业化和盈利。加速模型发布节奏（6 月发布 V4.1）将加剧与国内外 AI 巨头的竞争。 DeepSeek 的 V4 系列包括旗舰版 V4-Pro，总参数量 1.6 万亿（激活参数 490 亿），支持 100 万 token 上下文窗口。公司转向更快迭代周期以与主流行业实践对齐，同时追求创收。

rss · r/LocalLLaMA RSS · May 8, 15:34

**背景**: DeepSeek 是一家成立于 2023 年的杭州 AI 初创公司，于 2025 年初因发布具有竞争力的开源模型而受到全球关注。该公司以高效训练和低成本闻名，挑战美国大型科技公司。本轮融资旨在加速商业化，因 DeepSeek 寻求从其模型中创收。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://www.pbs.org/newshour/science/what-is-deepseek-heres-a-quick-guide-to-the-chinese-ai-company">What is DeepSeek? Here's a quick guide to the Chinese AI company</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#funding`, `#LLM`, `#AI industry`, `#open-source`

---

<a id="item-5"></a>
## [在 Apple Silicon 上通过 PCI 直通实现 CUDA 推理](https://www.reddit.com/r/LocalLLaMA/comments/1t7cqg9/you_can_do_cuda_inference_on_an_apple_silicon_mac/) ⭐️ 8.0/10

一个项目修改了 macOS 上的 QEMU，实现了将外部 GPU 通过 PCI 直通传递给 Linux 虚拟机，从而在 Apple Silicon Mac 上运行 CUDA 推理。基准测试显示 LLM 推理性能具有竞争力。 这使得 Apple Silicon 用户能够利用 NVIDIA GPU 进行 CUDA 加速的 LLM 推理，弥补了 Mac 生态系统中的重大空白。它扩展了 Mac 上本地 AI 工作负载的选择。 QEMU 补丁侧重于 macOS 主机上的 PCI 直通，使用 Thunderbolt 连接的外部 GPU。该文章包含了 LLM 令牌生成速度与原生 Linux 设置的基准对比。

rss · r/LocalLLaMA RSS · May 8, 16:20

**背景**: 由于驱动程序限制，Apple Silicon Macs 原生不支持 NVIDIA GPU。CUDA 是 NVIDIA 用于 AI 工作负载的并行计算平台。PCI 直通允许像 QEMU 这样的虚拟机监控程序将物理设备直接分配给客户虚拟机，从而在虚拟化环境中实现 GPU 加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/foxlet/macOS-Simple-KVM/blob/master/docs/guide-passthrough.md">macOS -Simple-KVM/docs/guide- passthrough .md at master...</a></li>
<li><a href="https://superuser.com/questions/1726305/how-to-passthrough-gpu-pci-e-with-qemu-7-0-on-macos-host-to-windows-guest">virtual machine - How to passthrough GPU/ PCI -e with QEMU 7.0 on...</a></li>
<li><a href="https://ai-manual.ru/article/kak-zapustit-cuda-inferens-na-apple-silicon-mac-polnyij-gajd-po-pci-passthrough/">CUDA на Mac через PCI Passthrough: гайд для Apple Silicon (2026)</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#GPU Passthrough`, `#Apple Silicon`, `#CUDA`, `#QEMU`

---

<a id="item-6"></a>
## [DS4：为 MacBook 优化的 DeepSeek 4 Flash 推理引擎](https://www.reddit.com/r/LocalLLaMA/comments/1t72tk9/ds4_a_deepseek_4_flash_specific_inference_engine/) ⭐️ 8.0/10

备受尊敬的开发者 antirez 开源了 DS4，这是一个专为 128GB MacBook 上的 DeepSeek V4 Flash 模型设计的专用推理引擎。 这使得在消费级硬件上本地运行强大的 284B 参数 MoE 模型成为可能，弥合了云端与桌面 AI 推理之间的差距。 DS4 专门针对 DeepSeek V4 Flash 的架构进行了优化，该模型总参数为 284B，但每次推理仅激活 13B 参数，从而适配 128GB 统一内存。

rss · r/LocalLLaMA RSS · May 8, 09:26

**背景**: DeepSeek V4 Flash 是 DeepSeek 发布的 MoE 语言模型预览版，总参数 284B，支持 1M token 上下文窗口。在本地运行如此大的模型需要高效管理内存和计算的推理引擎。DS4 加入了 vLLM 和 TensorRT-LLM 等推理引擎的行列，但专为特定模型和 Mac 硬件定制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek -V 4 - Flash · Hugging Face</a></li>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-flash">deepseek -v 4 - flash Model by Deepseek -ai | NVIDIA NIM</a></li>
<li><a href="https://ollama.com/library/deepseek-v4-flash">deepseek -v 4 - flash</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#DeepSeek`, `#open-source`, `#macOS`, `#local LLM`

---

<a id="item-7"></a>
## [生产环境 UUID v4 碰撞报告：仅 15,000 条记录就发生了重复](https://news.ycombinator.com/item?id=48060054) ⭐️ 7.0/10

一位开发者报告称，在使用 npm 的“uuid”包的生产数据库中，仅 15,000 条记录就发生了 UUID v4 碰撞：一年前生成的 UUID 与今天新生成的 UUID 完全相同。 这一事件挑战了广泛认为 UUID v4 碰撞几乎不可能的信念，突显了在 UUID 生成中高质量熵源和正确 PRNG 种子设置的关键重要性，尤其对于依赖唯一性的生产系统而言。 碰撞涉及具体的 UUID 'b6133fd6-70fe-4fe3-bed6-8ca8fc9386cd'。开发者使用了标准的 uuidv4()调用，并排除了重复插入错误；社区分析认为熵源不足或 PRNG 种子设置不当是可能的原因。

hackernews · Hacker News - AI & Agents · May 8, 07:57

**背景**: UUID v4 使用 122 位来自密码学安全随机数生成器的随机数，数学上碰撞概率极低。然而，实际随机性依赖于系统提供的熵源；种子不足、硬件缺陷或有缺陷的 PRNG 实现会大幅提高碰撞概率。许多开发者假设 UUID v4 的唯一性有保证，但真实事件表明，当熵源质量下降时，这种假设可能很脆弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier - Wikipedia</a></li>
<li><a href="https://bugzilla.mozilla.org/show_bug.cgi?id=335549">335549 - [FIX]UUID generator is nonrandom on x86-64</a></li>

</ul>
</details>

**社区讨论**: 评论者如 jandrewrogers 指出，由于熵源损坏，UUID v4 碰撞“出奇地常见”；其他人分享了公司创建专用 UUID 生成微服务的轶事，反映了普遍的误解。部分讨论涉及前端环境在 UUID 生成上根本不可靠，而配置良好的后端则更可靠。

**标签**: `#UUID`, `#randomness`, `#developer-tools`, `#bugs`, `#serverless`

---

<a id="item-8"></a>
## [AI 提前 3 年检测胰腺癌，超越人类医生](https://www.reddit.com/r/artificial/comments/1t7au63/new_ai_model_spots_pancreatic_cancer_up_to_3/) ⭐️ 7.0/10

据《Live Science》报道，一种新的人工智能模型在测试中展现出比人类医生提前最多三年检测出胰腺癌的能力。 胰腺癌因早期难以检测而臭名昭著，五年生存率低于 9%。这一 AI 突破可能显著改善早期诊断和患者预后。 该研究使用非增强 CT 扫描和类似于 PANDA（胰腺癌人工智能检测）的深度学习方法，该模型在大型数据集上训练而成。

rss · r/artificial RSS · May 8, 15:12

**背景**: 胰腺癌是最致命的癌症之一，通常在治疗困难的晚期才被诊断出来。诸如卷积神经网络等 AI 模型已被探索用于分析医学图像以发现疾病的早期迹象。例如，PANDA 模型可以通过非增强 CT 高精度地检测胰腺病变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12534903/">Early detection of pancreatic cancer on computed tomography...</a></li>

</ul>
</details>

**标签**: `#AI`, `#healthcare`, `#cancer detection`

---

<a id="item-9"></a>
## [新基准测试 AI 编码代理在编辑中的一致性](https://www.reddit.com/r/artificial/comments/1t7m8bg/i_built_a_benchmark_for_ai_memory_in_coding/) ⭐️ 7.0/10

一位开发者创建了名为'continuity-benchmarks'的基准测试，用于衡量 AI 编码代理在编辑过程中保持与项目规则一致性的能力，而不仅仅是事后检查。该基准评估了行为对齐、多会话一致性和检索时机，发现相比基线 RAG 设置，行为对齐提升了约 3 倍。 该基准解决了一个被忽视的关键故障模式：编码代理在修改过程中破坏先前决策。它提供了内存系统的标准化评估方法，使得在频繁修改的工作流中比较 LangChain 和自定义 RAG 栈等工具成为可能。 该基准检查编辑是否尊重先前的架构决策、在添加噪声后跨多个会话的行为是否一致，以及检索是否在正确的时机触发。初步结果显示，与典型的基于 RAG 的内存设置相比，行为对齐提高了约 3 倍，多会话一致性更强。

rss · r/artificial RSS · May 8, 22:05

**背景**: 大多数现有的 AI 内存基准测试侧重于语义召回——从内存中检索事实的能力。然而，编码代理的失败方式不同：它们在编辑代码时会破坏自己先前的决策，导致不一致。该基准通过模拟编辑工作流并实时测量一致性，针对这一特定故障模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mastra.ai/docs/memory/semantic-recall">Semantic recall | Memory | Mastra Docs</a></li>
<li><a href="https://hindsight.vectorize.io/blog/2026/03/23/agent-memory-benchmark">Agent Memory Benchmark : A Manifesto | Hindsight</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Benchmark`, `#Coding Agents`, `#Agent Evaluation`

---

<a id="item-10"></a>
## [AMD 开源 GAIA AI 现已集成 Gmail](https://www.reddit.com/r/artificial/comments/1t77n9a/amds_local_opensource_ai_can_now_easily_interact/) ⭐️ 7.0/10

AMD 的开源 GAIA 框架新增了 Gmail 集成功能，使用户能够通过 Ryzen AI 硬件本地运行的个人 AI 代理来执行电子邮件任务。 这展示了本地 AI 代理与广泛使用的云服务实现实用集成，通过将电子邮件处理保留在设备上增强隐私。它标志着开源本地 AI 框架生态系统日益成熟。 该集成利用 GAIA 的工具调用能力与 Gmail API 交互，整个代理完全在 Ryzen AI PC 上本地运行，无需云依赖。

rss · r/artificial RSS · May 8, 13:15

**背景**: GAIA（发音为"Guy-uh"）是 AMD 的开源框架，用于构建在 Ryzen AI 硬件上本地运行的 AI 代理，利用 NPU 进行高效的 LLM 推理。它支持工具、文档搜索和任务自动化。此次 Gmail 集成是一个新扩展，展示了其与外部服务交互的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/amd/gaia">GitHub - amd/gaia: Build AI agents for your PC · GitHub</a></li>
<li><a href="https://amd-gaia.ai/docs">Welcome - GAIA SDK</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/gaia-an-open-source-project-from-amd-for-running-local-llms-on-ryzen-ai.html">GAIA: An Open-Source Project from AMD for Running Local LLMs on Ryzen™ AI</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Open Source`, `#Local AI`, `#Email Integration`, `#AMD`

---

<a id="item-11"></a>
## [Qwen 35B-A3B 在 12GB 显存上经过调优运行良好](https://www.reddit.com/r/LocalLLaMA/comments/1t7l56a/qwen_35ba3b_is_very_usable_with_12gb_of_vram/) ⭐️ 7.0/10

一位 Reddit 用户成功在 RTX 3060 12GB 显卡上运行了 Qwen 35B-A3B 模型（IQ4_XS 量化），通过 llama.cpp 的 MoE 块卸载和最优 KV 缓存设置，实现了约 46.8 token/s 的解码速度和约 914 token/s 的预处理速度。 这表明像 35B 这样的大型 MoE 模型实际上可以在广泛使用的 12GB 显存消费级显卡上运行，降低了本地 LLM 推理的门槛。详细的调优指南为社区提供了在类似硬件上最大化性能的可行建议。 用户使用 llama.cpp 测试了 Qwen3.6-35B-A3B-MTP-IQ4_XS.gguf 模型，通过 -ncmoe 参数控制 MoE 块卸载，并发现 q8_0 KV 缓存性能最佳。MTP 推测解码相比经过良好调优的普通解码仅带来 2% 的生成速度提升。

rss · r/LocalLLaMA RSS · May 8, 21:22

**背景**: Qwen 35B-A3B 是一个混合专家（MoE）模型，总参数为 350 亿，但每个 token 仅激活约 30 亿参数，使其比相同规模的密集模型更高效。MoE 块卸载允许模型部分驻留在系统内存中，从而降低 GPU 内存使用。IQ4_XS 是一种基于重要性的 4 位量化方法，相比标准 Q4 提供更好的质量。llama-bench 是 llama.cpp 中包含的基准测试工具，用于测量提示处理和 token 生成速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Ex0bit/Elbaz-NVIDIA-Nemotron-3-Nano-30B-A3B-PRISM">Ex0bit/Elbaz-NVIDIA-Nemotron-3-Nano-30B-A3B-PRISM · Hugging Face</a></li>
<li><a href="https://deepwiki.com/ModelTC/lightx2v/5.5-mixture-of-experts-models-(wan-2.2-moe)">Mixture-of-Experts Models (Wan 2.2 MoE ) | ModelTC/lightx2v | DeepWiki</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md">llama.cpp/ tools / llama - bench /README.md at master...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#local inference`, `#quantization`, `#MoE`, `#Qwen`

---

<a id="item-12"></a>
## [AI2 发布 EMO：1B 激活参数的文档级领域路由 MoE 模型](https://www.reddit.com/r/LocalLLaMA/comments/1t7kgy4/new_moe_from_ai2_emo/) ⭐️ 7.0/10

AI2 发布了 EMO，这是一个混合专家模型，总参数量 14B，激活参数量 1B，在 1 万亿 token 上训练。它引入了文档级路由机制，使专家按领域（如健康、新闻）自然聚类，而非按表层语言模式。 这种路由方法有望带来更可解释和更专业的专家使用，提高大型语言模型的效率和领域适应能力。它代表了 MoE 研究中一项值得关注的架构创新，可能影响未来模型的设计方向。 该模型以 Hugging Face 集合（allenai/emo）的形式提供，包含检查点和推理代码。EMO 的文档级路由在将文档分配给专家之前对整个文档进行处理，不同于大多数 MoE 模型采用的 token 级路由。

rss · r/LocalLLaMA RSS · May 8, 20:57

**背景**: 混合专家模型是一种神经网络架构，使用多个专门的子模型（专家）和路由机制，对每个输入仅激活部分专家，从而提高效率。传统的 MoE 对每个 token 独立路由，通常捕捉句法模式。EMO 的文档级路由则考虑整个文档上下文，从而形成与语义主题一致的领域特定专家集群。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts? | IBM</a></li>

</ul>
</details>

**标签**: `#MoE`, `#AI2`, `#LLM`, `#routing`, `#model release`

---

<a id="item-13"></a>
## [MTP 接受率决定推理加速效果](https://www.reddit.com/r/LocalLLaMA/comments/1t7mdrl/mtp_is_all_about_acceptance_rate/) ⭐️ 7.0/10

一名用户在 M4 Max Studio 上使用 mlx-vlm 对 Gemma4-26b-a4b 的多 token 预测（MTP）进行基准测试，发现代码生成加速 1.53 倍，长文本生成无明显提升（0.95 倍），JSON 输出反而降速 0.5 倍。token 接受率分别为 66%、31%和 8%。 这表明 MTP 的收益高度依赖工作负载，只有当草稿接受率超过约 50%时才能实现加速。它为实践者在本地 LLM 推理中何时启用推测解码提供了参考。 测试使用了 Gemma4-26b-a4b，并关闭了结构化输出，因为 mlx-vlm 不支持带 JSON schema 的推测解码。作者指出 Gemma 的 JSON 指令遵循能力良好，关闭结构化输出可减少生成开销，但在低接受率下 MTP 的开销仍然占主导地位。

rss · r/LocalLLaMA RSS · May 8, 22:11

**背景**: 多 token 预测（MTP）是推测解码的一种形式，其中较小的草稿模型提前生成多个候选 token，主模型并行验证它们。接受率——被接受的草稿 token 占比——是决定加速效果的关键指标。当接受率低于约 50%时，草稿生成和验证的开销会超过收益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/mtp/mtp">Gemma 4 Multi-Token Prediction ( MTP ) using Hugging Face...</a></li>
<li><a href="https://huggingface.co/nebius/MTP-DeepSeek-V3-0324">nebius/ MTP -DeepSeek-V3-0324 · Hugging Face</a></li>
<li><a href="https://github.com/Blaizzy/mlx-vlm">GitHub - Blaizzy/ mlx - vlm : MLX - VLM is a package for inference and...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference`, `#speculative decoding`, `#MTP`, `#performance`

---

<a id="item-14"></a>
## [Gemma 4 26B 在单张 RTX 5090 上通过 DFlash 达到 600 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1t796qe/gemma_4_26b_hits_600_toks_on_one_rtx_5090/) ⭐️ 7.0/10

一位用户使用 vLLM 0.19.2rc1 中的 DFlash 投机解码对 Gemma 4 26B（4 位 AWQ）进行基准测试，在单张 32GB 显存的 RTX 5090 上实现了高达 578 输出 token/秒（2.56 倍加速）。 这一基准测试表明，投机解码可以大幅加速消费级硬件上的 LLM 推理，使 Gemma 4 等高质量模型在低成本下适用于实时智能体和聊天机器人应用。 最优配置使用了 num_speculative_tokens=13 和 max_num_batched_tokens=8192；增加批处理 token 数改善了尾延迟，尽管平均延迟略有增加。草稿模型是 z-lab/gemma-4-26B-A4B-it-DFlash，主模型的轻量级配套模型。

rss · r/LocalLLaMA RSS · May 8, 14:13

**背景**: 投机解码是一种推理优化技术，小型的草稿模型提议 token 序列，再由较大的目标模型在单次前向传播中验证，从而在保持输出分布的同时加速生成。vLLM 是一种高性能 LLM 推理引擎，AWQ（激活感知权重量化）以极小的质量损失减少内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/vllm">vLLM · Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2306.00978">[2306.00978] AWQ : Activation-aware Weight Quantization for LLM...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#speculative decoding`, `#Gemma 4`, `#RTX 5090`, `#LLM inference`

---

<a id="item-15"></a>
## [Ring 2.6 1T 模型在 OpenRouter 上免费提供；希望开放权重](https://www.reddit.com/r/LocalLLaMA/comments/1t7bvmq/ring_26_1t/) ⭐️ 7.0/10

一个名为 Ring 2.6 的 1 万亿参数模型已在 OpenRouter 上免费提供，社区成员希望它能够像 Ring 2.5 和 Ling 2.6 一样开放权重发布。 如果以开放权重形式发布，这个 1T 模型可能显著推进开源 AI 的能力，为研究人员和开发者提供罕见的机会，免费访问如此规模的模型。 该模型目前仅通过 OpenRouter 的免费层级可用，其开放权重状态尚未确认。之前的版本 Ring 2.5 是开放权重的，这激发了乐观情绪。

rss · r/LocalLLaMA RSS · May 8, 15:50

**背景**: 具有 1 万亿参数（1T）的大型语言模型非常庞大，通常需要巨大的计算资源。OpenRouter 是一个提供各种 AI 模型访问的平台，通常提供免费层级。'开放权重'意味着模型的训练参数公开发布，允许本地部署和微调。

**标签**: `#LLM`, `#inference`, `#open-source`, `#large model`, `#OpenRouter`

---