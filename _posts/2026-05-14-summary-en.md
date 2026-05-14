---
layout: default
title: "Horizon Summary: 2026-05-14 (EN)"
date: 2026-05-14
lang: en
---

> From 50 items, 15 important content pieces were selected

---

1. [Microsoft BitLocker YellowKey zero-day bypass exploit](#item-1) ⭐️ 8.0/10
2. [MIT RLCR teaches AI to express uncertainty accurately](#item-2) ⭐️ 8.0/10
3. [Google and Cloudflare tighten web access for AI agents](#item-3) ⭐️ 8.0/10
4. [Hugging Face Releases ml-intern for Local AI Research Agents](#item-4) ⭐️ 8.0/10
5. [TinySearch: Lightweight MCP Tool for Local LLM Web Search](#item-5) ⭐️ 8.0/10
6. [Claude AI recovers 11-year-old Bitcoin wallet worth $400,000](#item-6) ⭐️ 7.0/10
7. [Anthropic Launches Claude for Small Business](#item-7) ⭐️ 7.0/10
8. [Notion turns workspace into hub for AI agents](#item-8) ⭐️ 7.0/10
9. [Nvidia releases NVFP4 quantized Kimi 2.6 and 2.5 models](#item-9) ⭐️ 7.0/10
10. [Multi-Token Prediction Boosts Qwen Inference 40% on LLaMA.cpp](#item-10) ⭐️ 7.0/10
11. [Scenema Audio: Zero-shot expressive voice cloning released](#item-11) ⭐️ 7.0/10
12. [RTX 5090 Power and Performance Benchmarks for LLM Inference](#item-12) ⭐️ 7.0/10
13. [24+ tok/s from 30B MoE models on GTX 1080](#item-13) ⭐️ 7.0/10
14. [Opendesk: AI controls multiple computers over WiFi via MCP](#item-14) ⭐️ 7.0/10
15. [TurboQuant TBQ4 KV Cache + MTP for AMD ROCm in llama.cpp](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Microsoft BitLocker YellowKey zero-day bypass exploit](https://www.tomshardware.com/tech-industry/cyber-security/microsoft-bitlocker-protected-drives-can-now-be-opened-with-just-some-files-on-a-usb-stick-yellowkey-zero-day-exploit-demonstrates-an-apparent-backdoor) ⭐️ 8.0/10

A researcher named Eclipse published proof-of-concept (PoC) code for YellowKey, a zero-day exploit that bypasses Microsoft BitLocker encryption by placing specific files on a USB stick and rebooting into the Windows Recovery Environment (WinRE), granting full access to protected drives. A second exploit, GreenPlasma, targets a privilege escalation vulnerability in Windows CTFMON, though a complete PoC has not yet been released. This exploit is critical because BitLocker is widely used by enterprises and individuals to protect data at rest on lost or stolen devices. The bypass undermines the trust in BitLocker and could be exploited by attackers to access sensitive information, or potentially by law enforcement agencies for forensic data recovery. The YellowKey exploit works by writing a folder named 'FsTx' to either a USB stick or the EFI system partition, then triggering WinRE via a forced reboot, which opens a command prompt with full access to the BitLocker-encrypted volume without requiring a password or recovery key. GreenPlasma is described as a local privilege escalation that gives system-level access, but its complete PoC has not been released.

hackernews · cookiengineer · May 14, 02:45 · [Discussion](https://news.ycombinator.com/item?id=48130519)

**Background**: BitLocker is a full-disk encryption feature built into Windows that uses a Trusted Platform Module (TPM) to protect the encryption keys. A zero-day exploit targets a vulnerability that is unpatched by the vendor, and PoC code is often released to demonstrate the flaw. The YellowKey exploit takes advantage of the Windows Recovery Environment, which normally provides recovery tools, but can be manipulated to bypass authentication.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/microsoft-bitlocker-protected-drives-can-now-be-opened-with-just-some-files-on-a-usb-stick-yellowkey-zero-day-exploit-demonstrates-an-apparent-backdoor">Microsoft BitLocker-protected drives can now be opened with just some files on a USB stick — YellowKey zero-day exploit demonstrates an apparent backdoor | Tom's Hardware</a></li>
<li><a href="https://www.forbes.com/sites/daveywinder/2026/05/13/microsoft-windows-alert-angry-hacker-drops-2-new-zero-day-exploits/">Microsoft Windows Alert—Angry Hacker Drops 2 New Zero-Day Exploits</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/">Windows BitLocker zero-day gives access to protected drives, PoC released</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some commenters view the exploit as a sign of a deliberate backdoor in BitLocker and criticize Microsoft's commitment to security. Others applaud the public disclosure of the zero-day, noting that selling it on the market would have been far more lucrative, suggesting ethical motives. There is also technical discussion about the limitations of BitLocker when hardware security (e.g., secure boot with certificate leaks) is already compromised.

**Tags**: `#security`, `#microsoft`, `#bitlocker`, `#zero-day`, `#exploit`

---

<a id="item-2"></a>
## [MIT RLCR teaches AI to express uncertainty accurately](https://www.reddit.com/r/LocalLLaMA/comments/1tczrop/mit_rlcr_teaching_ai_models_to_say_im_not_sure/) ⭐️ 8.0/10

MIT CSAIL researchers have introduced RLCR (Reinforcement Learning with Calibration Rewards), a training method that reduces AI model overconfidence without sacrificing accuracy, enabling models to express uncertainty appropriately. Overconfidence in AI systems can lead to misleading and dangerous outputs, especially in high-stakes fields like healthcare or autonomous driving. RLCR improves model calibration, making AI outputs more reliable and trustworthy. RLCR uses a reward signal that penalizes high confidence on incorrect answers and rewards low confidence on correct ones, unlike post-hoc calibration methods. The method was trained on 20,000 examples using exact string match for correctness, and it outperformed post-training calibration approaches.

rss · r/LocalLLaMA RSS · May 14, 14:24

**Background**: AI models often produce confidence scores that do not reflect their true accuracy, a problem known as poor calibration. Traditional calibration methods are applied after training, but RLCR integrates calibration directly into the reinforcement learning training process, allowing the model to learn both correctness and appropriate confidence simultaneously. The research is detailed in the paper 'Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty' (arXiv:2507.16806).

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2507.16806">Beyond Binary Rewards: Training LMs to Reason About Their...</a></li>
<li><a href="https://www.commonwealthunion.com/ai-that-knows-when-its-wrong-rlcr-training-method-tackles-dangerous-overconfidence/">AI That Knows When It’s Wrong? RLCR Training Method Tackles...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#calibration`, `#reasoning`, `#RL`, `#MIT`

---

<a id="item-3"></a>
## [Google and Cloudflare tighten web access for AI agents](https://www.reddit.com/r/LocalLLaMA/comments/1tcaboi/websearch_is_coming_to_a_screeching_performance/) ⭐️ 8.0/10

Google is phasing out its free site-specific search tier to just 50 domains, effective January 1, 2027, with no public pricing for advanced queries. Meanwhile, Cloudflare has made its anti-AI-bot protection the default for all customers and partnered with GoDaddy to extend this coverage. These changes directly impact AI agents and local models that depend on web search for real-time data, potentially crippling their internet-pulling capabilities. The community must now seek or build open-source alternatives to maintain agent functionality. Google's free Custom Search API currently offers 100 queries/day per day, but the new policy caps site-specific searches to 50 domains entirely. Cloudflare's 'AI Labyrinth' feeds bots gibberish to waste their resources, and the GoDaddy partnership affects millions of domains hosted there.

rss · r/LocalLLaMA RSS · May 13, 19:35

**Background**: AI agents often rely on web scraping or search APIs to gather up-to-date information. Google's Custom Search API is a common paid method, while free scrapers face increasing blocks from services like Cloudflare, which now detects and challenges over 30% of bot traffic as malicious. These barriers push developers toward workarounds like stealth browsers or dedicated scraping services, but the trend threatens the viability of open-source AI tools.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.google.com/custom-search/v1/overview">Custom Search JSON API | Google for Developers</a></li>
<li><a href="https://www.businessinsider.com/thwart-big-tech-ai-bots-feed-them-gibberish-cloudflare-2025-4">How to Thwart Big Tech's Data-Sucking AI Bots ... - Business Insider</a></li>

</ul>
</details>

**Discussion**: The Reddit post expresses frustration and warns that web searches are returning 400 errors, calling for community-driven open projects to fill the gap. Users are likely to discuss alternatives like distributed search indexes, self-hosted crawlers, or new APIs, though no specific comments are provided.

**Tags**: `#web scraping`, `#AI agents`, `#Google search`, `#Cloudflare`, `#open source`

---

<a id="item-4"></a>
## [Hugging Face Releases ml-intern for Local AI Research Agents](https://www.reddit.com/r/LocalLLaMA/comments/1tcu5r8/automated_ai_researcher_running_locally_with/) ⭐️ 8.0/10

Hugging Face has released ml-intern, an agent harness that enables automated AI research to run locally using llama.cpp or ollama, integrating with open-source libraries like transformers, datasets, and trl. This allows AI researchers to run automated workflows 24/7 on a laptop without exhausting API token limits, making agentic research more accessible and cost-effective. Initially built for Claude Opus, ml-intern now supports local models; a demonstration shows Qwen3.6-35B-A3B performing supervised fine-tuning end-to-end by orchestrating CPU/GPU sandboxes and Hub jobs.

rss · r/LocalLLaMA RSS · May 14, 10:32

**Background**: Llama.cpp is an open-source library that enables efficient inference of large language models on local hardware, including laptops. Agent harnesses provide tools and system prompts that allow LLMs to autonomously execute complex multi-step tasks, such as training other models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/">GitHub - ggml-org/llama.cpp: LLM inference in C/C++ · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#agentic framework`, `#open-source`, `#Hugging Face`, `#local LLM`

---

<a id="item-5"></a>
## [TinySearch: Lightweight MCP Tool for Local LLM Web Search](https://www.reddit.com/r/LocalLLaMA/comments/1tczzga/a_very_lightweight_open_websearch_tool_for/) ⭐️ 8.0/10

TinySearch is an open-source MCP tool that performs web search via DuckDuckGo, crawls pages with Crawl4AI, and returns a condensed context blob using chunking, retrieval, and reranking, reducing context overload for small local LLMs. It addresses a key pain point for local agent setups—context overload from verbose web results—enabling small models to use web search without wasting context on scraped garbage, making local LLM agents more practical. It uses DuckDuckGo for search, Crawl4AI for crawling, and combines dense and BM25-style retrieval with reranking. It also supports running as a FastAPI server and takes 5–12 seconds end-to-end on hardware like an M4 Mac.

rss · r/LocalLLaMA RSS · May 14, 14:32

**Background**: MCP (Model Context Protocol) is an open standard introduced by Anthropic to standardize how AI systems integrate with external tools and data sources. Cline and Roo are popular local coding agents that rely on tool-calling capabilities. TinySearch fits into this ecosystem by providing a lightweight web search tool that respects small model context limits.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://docs.crawl4ai.com/">Crawl 4 AI , Open-source LLM-Friendly Web Crawler & Scraper</a></li>
<li><a href="https://mychen76.medium.com/vibe-coding-locally-with-cline-roo-and-ollama-better-experience-a8846c829d66">Vibe Coding ‘Locally’ with Cline/Roo and Ollama — Better Experience!</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#web-search`, `#local-LLM`, `#agent-tooling`, `#open-source`

---

<a id="item-6"></a>
## [Claude AI recovers 11-year-old Bitcoin wallet worth $400,000](https://www.tomshardware.com/tech-industry/cryptocurrency/bitcoin-trader-recovers-usd400-000-using-claude-ai-after-losing-wallet-password-11-years-ago-bot-tried-3-5-trillion-passwords-before-decrypting-an-old-wallet-backup) ⭐️ 7.0/10

A user recovered a Bitcoin wallet worth $400,000 that had been inaccessible for 11 years by using Claude AI to brute-force the lost password. The AI attempted 3.5 trillion password combinations before successfully decrypting the wallet backup. This demonstrates a practical application of AI in cryptographic recovery tasks, highlighting how large language models can assist in complex problem-solving beyond typical conversation or coding. It also raises awareness about the potential of AI agents for real-world security breaches and password recovery. The user found an old mnemonic seed phrase in a college notebook, which was the critical breakthrough enabling the targeted brute-force attack. Claude AI was used to write and execute password cracking scripts, leveraging its ability to understand cryptographic wallet formats and orchestrate the recovery process.

hackernews · cednore · May 14, 14:49 · [Discussion](https://news.ycombinator.com/item?id=48136240)

**Background**: Bitcoin wallets are protected by private keys or passwords; losing them can permanently lock funds. Traditional password recovery often uses specialized tools like hashcat, but they require technical expertise. Claude AI, a large language model by Anthropic, can generate code and solve multi-step problems, making it accessible for non-experts to attempt such recoveries.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://hashcat.net/">hashcat - World's fastest and most advanced password recovery utility</a></li>

</ul>
</details>

**Discussion**: Commenters shared similar stories of using Claude AI for non-obvious tasks like recovering malformed images and extracting text from browser internals. Some noted that finding the seed phrase was the real breakthrough, and that any password cracking software could have done the brute-force, but others praised Claude's ability to write custom scripts.

**Tags**: `#Claude AI`, `#cryptocurrency`, `#AI agents`, `#practical AI`, `#recovery`

---

<a id="item-7"></a>
## [Anthropic Launches Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) ⭐️ 7.0/10

Anthropic announced Claude for Small Business, a subscription plan tailored for small and medium-sized businesses, offering AI-powered features like invoice processing, payroll reconciliation, and morning briefs. This move signals Anthropic's strategic entry into the SMB market, challenging established tools like Microsoft Copilot. It could empower small businesses with limited technical resources to leverage AI automation, potentially transforming their productivity and operations. The service integrates with common business tools like email and accounting software, leveraging Claude's agentic capabilities for task automation. Community discussions highlight that a user-friendly UI for Claude Code could further unlock non-developer adoption, though current implementation still requires some technical know-how.

hackernews · neilfrndes · May 14, 03:59 · [Discussion](https://news.ycombinator.com/item?id=48130950)

**Background**: Anthropic, an AI safety company founded by former OpenAI employees, developed the Claude family of large language models. Claude Code is a command-line tool that allows developers to delegate coding tasks to an AI agent. The new SMB offering aims to bring similar agentic capabilities to non-technical business users, automating repetitive administrative tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://michaelcrist.substack.com/p/personal-ai-assistant">How I Built My Personal AI Assistant (Claude Code Tutorial)</a></li>
<li><a href="https://www.bcg.com/capabilities/artificial-intelligence/ai-agents">AI Agents: What They Are and Their Business Impact | BCG</a></li>

</ul>
</details>

**Discussion**: Comments are largely positive, with users sharing success stories of non-developers using Claude Code to automate tasks like invoice categorization. However, some European users question the value for their region, noting that payroll reconciliation is already simple. Overall, there is strong interest in making AI agents more accessible to average users.

**Tags**: `#Claude`, `#AI agents`, `#Anthropic`, `#small business`, `#productivity`

---

<a id="item-8"></a>
## [Notion turns workspace into hub for AI agents](https://techcrunch.com/2026/05/13/notion-just-turned-its-workspace-into-a-hub-for-ai-agents/) ⭐️ 7.0/10

On May 13, 2026, Notion launched a new developer platform that enables teams to connect AI agents, external data sources, and custom code directly into their workspace. This positions Notion as an agentic productivity hub, allowing users to automate complex workflows without leaving the platform, potentially transforming how enterprises manage tasks and data. The platform supports continuous upserting of external records into Notion databases using Workers and a persistent cursor, and provides a declarative schema for integration flexibility.

rss · TechCrunch AI · May 13, 21:45

**Background**: Notion is a widely used workspace tool for notes, databases, and project management. AI agents are autonomous software systems that can perform tasks, and agentic frameworks help developers build such agents. Notion's developer platform lowers the barrier for teams to embed AI agent capabilities directly into their daily workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.notion.com/product/dev">Build with Notion’s Developer Platform</a></li>
<li><a href="https://makewithnotion.com/">Notion Developer Platform Launch — May 13</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#agentic frameworks`, `#Notion`, `#productivity`, `#developer platform`

---

<a id="item-9"></a>
## [Nvidia releases NVFP4 quantized Kimi 2.6 and 2.5 models](https://www.reddit.com/r/LocalLLaMA/comments/1tcxb77/nvfp4_kimi26_and_kimi_25_released_by_nvidia/) ⭐️ 7.0/10

Nvidia has released NVFP4 quantized versions of Moonshot AI's Kimi-K2.6 and Kimi-K2.5 models using the Model Optimizer library, with benchmark results showing comparable or slightly better performance versus the native INT4 baseline on several metrics. This demonstrates that NVFP4 quantization can reduce model size by approximately 2x while maintaining accuracy, enabling more efficient deployment of large MoE models like Kimi on Nvidia hardware. It also showcases the practical use of Nvidia's Model Optimizer for production-ready quantization. The NVFP4 quantized Kimi-K2.6 model achieved 90.4 on GPQA Diamond vs 90.9 baseline, 54.4 on SciCode vs 52.6 baseline, and 76.5 on MMMU Pro vs 75.6 baseline, showing minimal accuracy loss and even slight gains in some benchmarks. The models are released on Hugging Face for commercial and non-commercial use.

rss · r/LocalLLaMA RSS · May 14, 12:53

**Background**: NVFP4 is a 4-bit floating-point quantization format from Nvidia that uses the E4M3 FP8 variant with non-power-of-two scaling factors for more accurate encoding. The Kimi-K2.6 and Kimi-K2.5 are large language models from Moonshot AI based on a mixture-of-experts (MoE) architecture with 1 trillion total parameters and 32 billion active parameters. Nvidia's Model Optimizer is a unified library for model compression techniques like quantization, pruning, and distillation, targeting deployment on TensorRT-LLM and vLLM.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | NVIDIA Technical Blog</a></li>
<li><a href="https://github.com/NVIDIA/Model-Optimizer">GitHub - NVIDIA/Model-Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#model quantization`, `#Nvidia`, `#Kimi`, `#LLM inference`, `#HuggingFace`

---

<a id="item-10"></a>
## [Multi-Token Prediction Boosts Qwen Inference 40% on LLaMA.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1tckzy2/multitoken_prediction_mtp_for_qwen_on_llamacpp/) ⭐️ 7.0/10

A developer has implemented Multi-Token Prediction (MTP) for Qwen models in a patched fork of LLaMA.cpp combined with TurboQuant, achieving a 40% speedup on a MacBook Pro M5 Max (from 21 to 34 tokens/s) with a 90% acceptance rate. This breakthrough significantly improves local LLM inference speed without quality loss, bringing high-performance AI closer to consumer hardware. It demonstrates the practical viability of combining speculative decoding techniques with advanced quantization for edge deployment. The implementation uses a lightweight drafter model within MTP to predict multiple tokens in parallel, which the target Qwen model verifies in a single forward pass. TurboQuant further reduces model size via vector quantization with near-optimal distortion, enabling the 27B and 35B Qwen models to run efficiently on a MacBook with 64GB RAM.

rss · r/LocalLLaMA RSS · May 14, 02:35

**Background**: Multi-Token Prediction (MTP) is an inference acceleration technique where a small drafter model predicts several future tokens simultaneously, and a larger target model verifies them in one forward pass, achieving higher throughput. TurboQuant is a vector quantization method developed by Google Research that compresses model weights and KV cache with minimal accuracy loss. LLaMA.cpp is a popular open-source C++ implementation for running quantized LLMs efficiently on CPU and GPU.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Multi-Token Prediction`, `#LLaMA.cpp`, `#TurboQuant`, `#LLM Inference`, `#Local LLM`

---

<a id="item-11"></a>
## [Scenema Audio: Zero-shot expressive voice cloning released](https://www.reddit.com/r/LocalLLaMA/comments/1tcwqdd/scenema_audio_zeroshot_expressive_voice_cloning/) ⭐️ 7.0/10

Scenema AI has released the model weights and inference code for Scenema Audio, a zero-shot expressive voice cloning and speech generation model that separates emotional performance from voice identity, allowing any voice to perform any emotion without prior recording. This open-source release enables developers to integrate highly expressive, emotion-controllable speech synthesis into applications, advancing voice cloning beyond neutral TTS and democratizing access to natural-sounding emotional speech generation. The model is a diffusion-based audio model derived from LTX 2.3, requiring only a text prompt for emotion and an optional 10-second reference for voice cloning; it supports 8-step denoising and a Docker REST API with automatic VRAM management.

rss · r/LocalLLaMA RSS · May 14, 12:29

**Background**: Traditional text-to-speech (TTS) systems struggle to convey emotion naturally, and most voice cloning models require multiple samples or fail to generalize to unseen emotions. Zero-shot voice cloning aims to replicate a speaker's identity from a brief recording without additional training. Scenema Audio innovates by decoupling emotional expression from voice identity, allowing users to control how speech sounds (e.g., rage, excitement) independently of the speaker's voice.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ScenemaAI/scenema-audio">GitHub - ScenemaAI/scenema-audio: Zero-shot expressive voice cloning and speech generation. Generate anything from short clips to full-length audiobooks with realistic emotional delivery, pacing, and breath control. Clone any voice from a 10-second reference and perform emotions the original speaker never recorded. · GitHub</a></li>
<li><a href="https://scenema.ai/audio">Scenema Audio: Zero-Shot Expressive Voice Cloning and Speech Generation | Scenema AI</a></li>

</ul>
</details>

**Tags**: `#voice cloning`, `#speech generation`, `#open-source`, `#zero-shot`, `#AI/ML`

---

<a id="item-12"></a>
## [RTX 5090 Power and Performance Benchmarks for LLM Inference](https://www.reddit.com/r/LocalLLaMA/comments/1tcvji7/benchmark_5090rtx_promt_parsing_token_generation/) ⭐️ 7.0/10

A Reddit user benchmarked the RTX 5090 GPU for local LLM inference, measuring prompt parsing speed, token generation rate, and power consumption across a 400W–600W range to identify optimal power levels. This provides practical data for LLM enthusiasts and researchers to optimize GPU power settings for inference, potentially reducing electricity costs and heat without sacrificing significant performance. Using llama.cpp with a Qwen3.6-27B model (Q6_K_P quant), the benchmark showed prompt processing is more sensitive to power limits than token generation, and the RTX 5090 peaked at 592W despite a 600W limit, with spikes exceeding the set limit by 10–12W.

rss · r/LocalLLaMA RSS · May 14, 11:38

**Background**: Prompt parsing and token generation are two key phases in LLM inference: parsing ingests input context, while generation produces output tokens. GPU power limiting reduces maximum power draw, often yielding near-linear performance drops at moderate limits, but different workloads respond differently.

**Tags**: `#LLM inference`, `#GPU benchmarking`, `#token generation`, `#power optimization`

---

<a id="item-13"></a>
## [24+ tok/s from 30B MoE models on GTX 1080](https://www.reddit.com/r/LocalLLaMA/comments/1tcc7h5/24_toks_from_30b_moe_models_on_an_old_gtx_1080_8/) ⭐️ 7.0/10

A user achieved 24+ tokens per second for Qwen 3.6 35B-A3B and Gemma 4 26B-A4B MoE models on an old GTX 1080 (8 GB VRAM) with 128k context using llama.cpp and TurboQuant KV cache quantization, leveraging CPU offloading of cold expert weights. This demonstrates that large Mixture-of-Experts models can run efficiently on decade-old consumer hardware, significantly lowering the barrier for local LLM inference and enabling long-context applications without expensive GPUs. The key technique is MoE offloading: llama.cpp parks infrequently used expert weights in system RAM and streams them over PCIe 3.0 to the GPU, while keeping hot layers and KV cache on GPU. Additionally, Gemma 4's Multi-Token Prediction (MTP) required a manual fix to move the embedding table to GPU for a ~22% speedup.

rss · r/LocalLLaMA RSS · May 13, 20:41

**Background**: Mixture-of-Experts (MoE) models use multiple specialized sub-networks (experts) per layer, but only activate a subset for each token, reducing computational cost. TurboQuant is a KV cache quantization algorithm from Google DeepMind that compresses cache to 3 bits with minimal accuracy loss. Multi-Token Prediction (MTP) is a technique where a model predicts several future tokens simultaneously, which can be used for speculative decoding to speed up inference.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/0xSero/turboquant">GitHub - 0xSero/ turboquant : TurboQuant : Near-optimal KV cache ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2404.19737">[2404.19737] Better & Faster Large Language Models via Multi-token Prediction</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#quantization`, `#MoE`, `#llama.cpp`, `#local LLM`

---

<a id="item-14"></a>
## [Opendesk: AI controls multiple computers over WiFi via MCP](https://www.reddit.com/r/LocalLLaMA/comments/1tcpgsv/computeruse_mcp_that_can_control_multiple/) ⭐️ 7.0/10

Opendesk is an open-source tool that uses the Computer-use Model Context Protocol (MCP) to let AI agents see, click, type, and navigate on a remote computer over WiFi, without cloud dependency or accounts. This extends AI agent capabilities from single-machine control to multi-machine orchestration over a local network, enabling powerful automation for remote desktop management, testing, and multi-device workflows. The tool is free, open-source, and supports Mac, Linux, and Windows. Communication stays on the local network with full encryption, and pairing is needed only once.

rss · r/LocalLLaMA RSS · May 14, 06:13

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 for connecting AI assistants to external systems. Computer-use MCP is a specialized server that allows AI models like Claude to control a computer's mouse and keyboard. Opendesk builds on this to control multiple machines remotely.

<details><summary>References</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol</a></li>
<li><a href="https://github.com/domdomegg/computer-use-mcp">GitHub - domdomegg/ computer - use - mcp : Give AI models...</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#Computer Use`, `#Multi-machine`, `#AI Agents`, `#Desktop Control`

---

<a id="item-15"></a>
## [TurboQuant TBQ4 KV Cache + MTP for AMD ROCm in llama.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1tcrtxm/turboquantmtp_for_rocmllama_cpp/) ⭐️ 7.0/10

A developer implemented TurboQuant TBQ4 KV cache and Multi-Token Prediction (MTP) for AMD ROCm GPUs in llama.cpp, enabling 64k context on 24GB VRAM with improved token rates. This optimization significantly expands usable context length on consumer AMD GPUs, making ROCm more competitive for local LLM inference and enabling larger-scale tasks without expensive hardware. Tested on an RX 7900 XTX with Qwen3.6-27B Q4_K_M MTP GGUF model, TBQ4 KV cache at 64k context achieved 38–54 tok/s using ~20 GB VRAM, while the q8_0 baseline used ~22–23 GB VRAM and dropped to ~31 tok/s at 32k context.

rss · r/LocalLLaMA RSS · May 14, 08:24

**Background**: TurboQuant is a near-optimal vector quantization method that compresses KV cache by 4-7x with minimal quality loss. MTP (Multi-Token Prediction) uses the model's built-in draft heads for speculative decoding, generating multiple tokens per forward pass. Combining both allows fitting very long contexts into limited VRAM while maintaining high throughput.

<details><summary>References</summary>
<ul>
<li><a href="https://turbo-quant.com/turboquant">TurboQuant Algorithm: PolarQuant + QJL Explained for Developers</a></li>
<li><a href="https://github.com/Firmamento-Technologies/TurboQuant">GitHub - Firmamento-Technologies/ TurboQuant : Near-optimal vector...</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#ROCm`, `#quantization`, `#MTP`, `#llama.cpp`

---