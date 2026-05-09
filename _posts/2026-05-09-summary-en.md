---
layout: default
title: "Horizon Summary: 2026-05-09 (EN)"
date: 2026-05-09
lang: en
---

> From 103 items, 15 important content pieces were selected

---

1. [Teaching Claude Why: LLMs Learn to Reason About Instructions](#item-1) ⭐️ 9.0/10
2. [ChatGPT 5.5 Pro Can Solve 'Gentle' Math Problems, Says Gowers](#item-2) ⭐️ 8.0/10
3. [MTP + TurboQuant Achieves 80+ t/s on RTX 4090 for Qwen3.6-27B](#item-3) ⭐️ 8.0/10
4. [DeepSeek Seeks $7.35B, Plans V4.1 Release Next Month](#item-4) ⭐️ 8.0/10
5. [CUDA inference on Apple Silicon via PCI passthrough](#item-5) ⭐️ 8.0/10
6. [DS4: A DeepSeek 4 Flash Inference Engine for MacBooks](#item-6) ⭐️ 8.0/10
7. [UUID v4 Collision Reported in Production with 15k Records](#item-7) ⭐️ 7.0/10
8. [AI detects pancreatic cancer up to 3 years earlier than doctors](#item-8) ⭐️ 7.0/10
9. [New benchmark tests AI coding agents' consistency during edits](#item-9) ⭐️ 7.0/10
10. [AMD's open-source GAIA AI now integrates with Gmail](#item-10) ⭐️ 7.0/10
11. [Qwen 35B-A3B Runs Well on 12GB VRAM with Tuning](#item-11) ⭐️ 7.0/10
12. [AI2 Releases EMO: 1B-Active MoE with Document-Level Domain Routing](#item-12) ⭐️ 7.0/10
13. [MTP acceptance rate determines inference speedup](#item-13) ⭐️ 7.0/10
14. [Gemma 4 26B Hits 600 tok/s on Single RTX 5090 with DFlash](#item-14) ⭐️ 7.0/10
15. [Ring 2.6 1T Model Free on OpenRouter; Open-Weight Hopes](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Teaching Claude Why: LLMs Learn to Reason About Instructions](https://www.anthropic.com/research/teaching-claude-why) ⭐️ 9.0/10

Anthropic's 'Teaching Claude Why' research introduces a method to train large language models to reason about the purpose behind instructions, improving both alignment and capability. This approach could significantly improve AI safety by making models less likely to follow harmful instructions when they understand the underlying intent, and the method generalizes beyond Claude to open-weight models. The research builds on Anthropic's earlier case study on agentic misalignment and includes fine-tuned open models (Llama 3.1 8B, Qwen 2.5 32B, Qwen 3 32B) trained for toy values. A related paper 'Model Spec Midtraining' (arXiv:2605.02087) discusses similar results.

hackernews · pretext · May 8, 17:59 · [Discussion](https://news.ycombinator.com/item?id=48066592)

**Background**: Large language models are typically trained to follow instructions literally, which can lead to misaligned behavior when instructions conflict with ethical guidelines. Reinforcement learning from human feedback (RLHF) is a common alignment technique, but it often fails to capture reasoning about intent. 'Teaching Claude Why' aims to imbue models with the ability to infer the purpose of instructions, akin to teaching them 'why' rather than just 'what'. This aligns with research on reasoning models and chain-of-thought prompting.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/teaching-claude-why">Teaching Claude why \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Community commenters engaged in broader discussions about alignment definitions, pedagogical parallels, and philosophical implications. Some praised the research's generalizability to open models and its distinctive art style.

**Tags**: `#AI alignment`, `#Claude`, `#model reasoning`, `#Anthropic`, `#agent alignment`

---

<a id="item-2"></a>
## [ChatGPT 5.5 Pro Can Solve 'Gentle' Math Problems, Says Gowers](https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/) ⭐️ 8.0/10

Timothy Gowers, a Fields Medalist and Cambridge mathematician, reports that ChatGPT 5.5 Pro successfully solved a series of 'gentle' research-level math problems, a capability he previously thought would take decades. This suggests that large language models are approaching the ability to automate parts of mathematical research, particularly routine or 'gentle' problems, which could fundamentally alter how PhD students are trained and what tasks remain for human mathematicians. Gowers notes that the model's performance on a 'gentle' problem from his own research was so thorough that he could have written the paper himself based on the LLM's output, though he emphasizes that the model still fails on more difficult problems and requires careful prompting.

hackernews · _alternator_ · May 9, 02:41 · [Discussion](https://news.ycombinator.com/item?id=48071262)

**Background**: "Gentle problems" are research-level math problems that are approachable for beginners but not trivial; they often serve as starting points for PhD students. Gowers has been a prominent voice on the impact of AI on mathematics, previously organizing the Polymath project to crowdsource problem-solving and predicting a shift in mathematical practice.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Timothy_Gowers">Timothy Gowers - Wikipedia</a></li>
<li><a href="https://numberwarrior.wordpress.com/2009/03/25/a-gentle-introduction-to-the-polymath-project/">A gentle introduction to the Polymath project | The Number Warrior</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a mix of awe and concern: some noted the financial barrier to accessing such models in academia, especially in Eastern Europe, while others reflected on the emotional and philosophical implications for mathematicians' sense of purpose and immortality through their work.

**Tags**: `#AI`, `#LLM`, `#mathematical reasoning`, `#OpenAI`, `#ChatGPT`

---

<a id="item-3"></a>
## [MTP + TurboQuant Achieves 80+ t/s on RTX 4090 for Qwen3.6-27B](https://www.reddit.com/r/LocalLLaMA/comments/1t7kyju/got_mtp_turboquant_running_qwen3627b_80_ts_at/) ⭐️ 8.0/10

A developer achieved 80-87 tokens per second on a single RTX 4090 for the Qwen3.6-27B model with 262K context by combining Multi-Token Prediction (MTP) with TurboQuant KV cache quantization (TBQ4_0). The implementation is open-sourced on GitHub and includes technical blog details. This demonstrates that near-lossless KV cache compression (TurboQuant) and speculative decoding (MTP) can dramatically accelerate local LLM inference on consumer hardware, making large models with long contexts practical for real-time agent applications. It achieves nearly double the typical throughput for this class of models. The model used is Qwen3.6-27B-Heretic-v2 Q4_K_M with grafted MTP heads, running on Ubuntu 24.04 with CUDA 12.x. The MTP draft acceptance rate was around 73% with 3 draft tokens. The fork is based on llama.cpp and the code is buildable for reproduction.

rss · r/LocalLLaMA RSS · May 8, 21:15

**Background**: Multi-Token Prediction (MTP) is a speculative decoding technique where a small draft model predicts multiple future tokens in parallel, then the main model verifies them, achieving speedups by processing multiple tokens per forward pass. TurboQuant is a Google DeepMind algorithm that compresses KV cache to 3 bits per value with negligible accuracy loss, drastically reducing memory usage for long context lengths. Combining both allows running a 27B parameter model with 262K context on a single 24GB GPU with high throughput.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/0xSero/turboquant">GitHub - 0xSero/ turboquant : TurboQuant : Near-optimal KV cache ...</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/Multi_Token_Prediction.html">Multi Token Prediction (MTP) — vllm-ascend</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#quantization`, `#Multi-Token Prediction`, `#llama.cpp`, `#TurboQuant`

---

<a id="item-4"></a>
## [DeepSeek Seeks $7.35B, Plans V4.1 Release Next Month](https://www.reddit.com/r/LocalLLaMA/comments/1t7bfpw/reports_suggest_deepseek_is_seeking_735_billion/) ⭐️ 8.0/10

DeepSeek is reportedly seeking to raise up to $7.35 billion (RMB 50 billion) in its first funding round, with founder Liang Wenfeng contributing the maximum allowable amount. The company also plans to release the V4.1 update of its large language model in June. If completed, this would be the largest single fundraising round in Chinese AI history, signaling DeepSeek's rapid push toward commercialization and profitability. The accelerated model release pace (V4.1 in June) intensifies competition with both domestic and global AI leaders. DeepSeek's V4 series includes the flagship V4-Pro with 1.6 trillion total parameters (49B activated) and supports a 1-million-token context window. The company's shift to faster iteration aligns with mainstream industry practices as it pursues revenue generation.

rss · r/LocalLLaMA RSS · May 8, 15:34

**Background**: DeepSeek is a Chinese AI startup founded in 2023 in Hangzhou, gaining global attention in early 2025 with competitive open-source models. The company has been known for efficient training and low costs, challenging US big tech. This funding round aims to accelerate commercialization, as DeepSeek seeks to generate revenue from its models.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://www.pbs.org/newshour/science/what-is-deepseek-heres-a-quick-guide-to-the-chinese-ai-company">What is DeepSeek? Here's a quick guide to the Chinese AI company</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#funding`, `#LLM`, `#AI industry`, `#open-source`

---

<a id="item-5"></a>
## [CUDA inference on Apple Silicon via PCI passthrough](https://www.reddit.com/r/LocalLLaMA/comments/1t7cqg9/you_can_do_cuda_inference_on_an_apple_silicon_mac/) ⭐️ 8.0/10

A project modifies QEMU on macOS to enable PCI passthrough of an external GPU to a Linux VM, allowing CUDA inference on Apple Silicon Macs. Benchmarks show competitive performance for LLM inference. This enables Apple Silicon users to harness NVIDIA GPUs for CUDA-accelerated LLM inference, closing a major gap in the Mac ecosystem. It expands options for local AI workloads on Macs. The QEMU patch focuses on PCI passthrough on macOS host, using Thunderbolt-connected eGPUs. The post includes benchmarks comparing LLM token generation speeds against native Linux setups.

rss · r/LocalLLaMA RSS · May 8, 16:20

**Background**: Apple Silicon Macs do not natively support NVIDIA GPUs due to driver restrictions. CUDA is NVIDIA's parallel computing platform used for AI workloads. PCI passthrough allows a hypervisor like QEMU to assign a physical device directly to a guest VM, enabling GPU acceleration in virtualized environments.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/foxlet/macOS-Simple-KVM/blob/master/docs/guide-passthrough.md">macOS -Simple-KVM/docs/guide- passthrough .md at master...</a></li>
<li><a href="https://superuser.com/questions/1726305/how-to-passthrough-gpu-pci-e-with-qemu-7-0-on-macos-host-to-windows-guest">virtual machine - How to passthrough GPU/ PCI -e with QEMU 7.0 on...</a></li>
<li><a href="https://ai-manual.ru/article/kak-zapustit-cuda-inferens-na-apple-silicon-mac-polnyij-gajd-po-pci-passthrough/">CUDA на Mac через PCI Passthrough: гайд для Apple Silicon (2026)</a></li>

</ul>
</details>

**Tags**: `#LLM Inference`, `#GPU Passthrough`, `#Apple Silicon`, `#CUDA`, `#QEMU`

---

<a id="item-6"></a>
## [DS4: A DeepSeek 4 Flash Inference Engine for MacBooks](https://www.reddit.com/r/LocalLLaMA/comments/1t72tk9/ds4_a_deepseek_4_flash_specific_inference_engine/) ⭐️ 8.0/10

Antirez, a respected developer, has open-sourced DS4, a dedicated inference engine designed specifically for DeepSeek V4 Flash models on 128GB MacBooks. This enables running a powerful 284B-parameter MoE model locally on consumer hardware, bridging the gap between cloud-based and desktop AI inference. DS4 is specifically optimized for DeepSeek V4 Flash's architecture, which has 284B total parameters but only 13B activated per token, fitting within 128GB unified memory.

rss · r/LocalLLaMA RSS · May 8, 09:26

**Background**: DeepSeek V4 Flash is a Mixture-of-Experts (MoE) language model preview with 284B total parameters and a 1M-token context window. Running such large models locally requires efficient inference engines that manage memory and compute. DS4 joins other inference engines like vLLM and TensorRT-LLM but is tailored for this specific model and Mac hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek -V 4 - Flash · Hugging Face</a></li>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-flash">deepseek -v 4 - flash Model by Deepseek -ai | NVIDIA NIM</a></li>
<li><a href="https://ollama.com/library/deepseek-v4-flash">deepseek -v 4 - flash</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#DeepSeek`, `#open-source`, `#macOS`, `#local LLM`

---

<a id="item-7"></a>
## [UUID v4 Collision Reported in Production with 15k Records](https://news.ycombinator.com/item?id=48060054) ⭐️ 7.0/10

A developer reported a UUID v4 collision in a production database with only 15,000 records, using the npm 'uuid' package, where a UUID generated a year ago matched a newly generated one. This incident challenges the widespread belief that UUID v4 collisions are practically impossible, highlighting the critical importance of high-quality entropy sources and proper PRNG seeding in UUID generation, especially for production systems relying on uniqueness. The collision involved the exact UUID 'b6133fd6-70fe-4fe3-bed6-8ca8fc9386cd'. The developer used the standard uuidv4() call and confirmed it was not a double-insert bug; community analysis points to insufficient entropy or PRNG seeding as likely causes.

hackernews · Hacker News - AI & Agents · May 8, 07:57

**Background**: UUID v4 uses 122 bits of randomness from a cryptographically secure random number generator, making collisions mathematically improbable. However, the actual randomness relies on the entropy source provided by the system; poor seeding, hardware defects, or buggy PRNG implementations can drastically increase collision probability. Many developers assume UUID v4 uniqueness is guaranteed, but real-world incidents show that assumption can be fragile when entropy quality degrades.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier - Wikipedia</a></li>
<li><a href="https://bugzilla.mozilla.org/show_bug.cgi?id=335549">335549 - [FIX]UUID generator is nonrandom on x86-64</a></li>

</ul>
</details>

**Discussion**: Commenters like jandrewrogers note that UUID v4 collisions are 'surprisingly common' due to broken entropy sources, while others share anecdotes of companies creating dedicated UUID generation microservices, reflecting widespread misunderstanding. Some discuss how frontend environments are fundamentally unreliable for UUID generation compared to well-configured backends.

**Tags**: `#UUID`, `#randomness`, `#developer-tools`, `#bugs`, `#serverless`

---

<a id="item-8"></a>
## [AI detects pancreatic cancer up to 3 years earlier than doctors](https://www.reddit.com/r/artificial/comments/1t7au63/new_ai_model_spots_pancreatic_cancer_up_to_3/) ⭐️ 7.0/10

A new AI model demonstrated the ability to detect pancreatic cancer up to three years earlier than human doctors in a test, as reported by Live Science. Pancreatic cancer is notoriously difficult to detect early, leading to a five-year survival rate of less than 9%. This AI breakthrough could significantly improve early diagnosis and patient outcomes. The study used non-contrast CT scans and a deep learning approach similar to PANDA (pancreatic cancer detection with artificial intelligence), which was trained on a large dataset.

rss · r/artificial RSS · May 8, 15:12

**Background**: Pancreatic cancer is one of the deadliest cancers, often diagnosed at late stages when treatment is difficult. AI models like convolutional neural networks have been explored to analyze medical images for early signs of disease. The PANDA model, for instance, can detect pancreatic lesions with high accuracy via non-contrast CT.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12534903/">Early detection of pancreatic cancer on computed tomography...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#healthcare`, `#cancer detection`

---

<a id="item-9"></a>
## [New benchmark tests AI coding agents' consistency during edits](https://www.reddit.com/r/artificial/comments/1t7m8bg/i_built_a_benchmark_for_ai_memory_in_coding/) ⭐️ 7.0/10

A developer created a benchmark called 'continuity-benchmarks' that measures how well AI coding agents maintain consistency with project rules throughout the editing process, not just after the fact. The benchmark evaluates action alignment, multi-session consistency, and retrieval timing, finding a 3x improvement in action alignment over baseline RAG setups. This benchmark addresses a critical, overlooked failure mode in coding agents: breaking earlier decisions during modifications. It provides a standardized evaluation method for memory systems, enabling comparison of tools like LangChain and custom RAG stacks in mutation-heavy workflows. The benchmark checks whether edits respect earlier architectural decisions, if behavior stays consistent across multiple sessions with added noise, and whether retrieval is triggered at the right moment. Early results show approximately 3× better action alignment and stronger multi-session consistency compared to typical RAG-based memory setups.

rss · r/artificial RSS · May 8, 22:05

**Background**: Most existing AI memory benchmarks focus on semantic recall—the ability to retrieve facts from memory. However, coding agents often fail differently: they break their own earlier decisions while editing code, leading to inconsistencies. This benchmark targets that specific failure mode by simulating editing workflows and measuring consistency in real time.

<details><summary>References</summary>
<ul>
<li><a href="https://mastra.ai/docs/memory/semantic-recall">Semantic recall | Memory | Mastra Docs</a></li>
<li><a href="https://hindsight.vectorize.io/blog/2026/03/23/agent-memory-benchmark">Agent Memory Benchmark : A Manifesto | Hindsight</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Benchmark`, `#Coding Agents`, `#Agent Evaluation`

---

<a id="item-10"></a>
## [AMD's open-source GAIA AI now integrates with Gmail](https://www.reddit.com/r/artificial/comments/1t77n9a/amds_local_opensource_ai_can_now_easily_interact/) ⭐️ 7.0/10

AMD's open-source GAIA framework has added Gmail integration, enabling users to perform email tasks locally via a personal AI agent running on Ryzen AI hardware. This demonstrates local AI agents gaining practical integration with widely-used cloud services, enhancing privacy by keeping email processing on-device. It signals growing ecosystem maturity for open-source local AI frameworks. The integration uses GAIA's tool-calling capabilities to interact with Gmail's API, and the entire agent runs locally on Ryzen AI PCs without cloud dependencies.

rss · r/artificial RSS · May 8, 13:15

**Background**: GAIA (pronounced "Guy-uh") is AMD's open-source framework for building AI agents that run locally on Ryzen AI hardware, leveraging the NPU for efficient LLM inference. It supports tools, document search, and task automation. This Gmail integration is a new extension showcasing its ability to interact with external services.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/amd/gaia">GitHub - amd/gaia: Build AI agents for your PC · GitHub</a></li>
<li><a href="https://amd-gaia.ai/docs">Welcome - GAIA SDK</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/gaia-an-open-source-project-from-amd-for-running-local-llms-on-ryzen-ai.html">GAIA: An Open-Source Project from AMD for Running Local LLMs on Ryzen™ AI</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Open Source`, `#Local AI`, `#Email Integration`, `#AMD`

---

<a id="item-11"></a>
## [Qwen 35B-A3B Runs Well on 12GB VRAM with Tuning](https://www.reddit.com/r/LocalLLaMA/comments/1t7l56a/qwen_35ba3b_is_very_usable_with_12gb_of_vram/) ⭐️ 7.0/10

A Reddit user successfully ran the Qwen 35B-A3B model (IQ4_XS quantization) on an RTX 3060 12GB GPU, achieving ~46.8 tokens/s decoding and ~914 tokens/s prefill using llama.cpp with MoE block offloading and optimal KV cache settings. This demonstrates that large MoE models like 35B are practically usable on widely available consumer GPUs with 12GB VRAM, lowering the barrier for local LLM inference. The detailed tuning guide provides actionable advice for the community to maximize performance on such hardware. The user tested the Qwen3.6-35B-A3B-MTP-IQ4_XS.gguf model with llama.cpp, using the -ncmoe flag to control MoE block offloading and found that q8_0 KV cache performed best. MTP speculative decoding provided only a 2% generation speedup over well-tuned plain decoding.

rss · r/LocalLLaMA RSS · May 8, 21:22

**Background**: Qwen 35B-A3B is a Mixture-of-Experts (MoE) model with 35 billion total parameters but only about 3 billion active per token, making it more efficient than dense models of similar size. MoE block offloading allows parts of the model to reside in system RAM, reducing GPU memory usage. IQ4_XS is an importance-weighted 4-bit quantization method that offers better quality than standard Q4. llama-bench is a benchmarking tool included in llama.cpp for measuring prompt processing and token generation speeds.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Ex0bit/Elbaz-NVIDIA-Nemotron-3-Nano-30B-A3B-PRISM">Ex0bit/Elbaz-NVIDIA-Nemotron-3-Nano-30B-A3B-PRISM · Hugging Face</a></li>
<li><a href="https://deepwiki.com/ModelTC/lightx2v/5.5-mixture-of-experts-models-(wan-2.2-moe)">Mixture-of-Experts Models (Wan 2.2 MoE ) | ModelTC/lightx2v | DeepWiki</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md">llama.cpp/ tools / llama - bench /README.md at master...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#local inference`, `#quantization`, `#MoE`, `#Qwen`

---

<a id="item-12"></a>
## [AI2 Releases EMO: 1B-Active MoE with Document-Level Domain Routing](https://www.reddit.com/r/LocalLLaMA/comments/1t7kgy4/new_moe_from_ai2_emo/) ⭐️ 7.0/10

AI2 has released EMO, a Mixture-of-Experts model with 1 billion activated parameters out of 14 billion total, trained on 1 trillion tokens. It introduces document-level routing, where experts naturally cluster by domain (e.g., health, news) instead of surface linguistic patterns. This routing approach could lead to more interpretable and specialized expert usage, improving efficiency and domain adaptation in large language models. It represents a notable architectural innovation in MoE research, potentially influencing future model designs. The model is available as a Hugging Face collection (allenai/emo), with checkpoints and inference code. EMO's document-level routing processes entire documents before assigning them to experts, unlike token-level routing used in most MoE models.

rss · r/LocalLLaMA RSS · May 8, 20:57

**Background**: Mixture of Experts (MoE) is a neural network architecture that uses multiple specialized sub-models (experts) and a routing mechanism to activate only a subset for each input, improving efficiency. Traditional MoE routes each token independently, often capturing syntactic patterns. EMO's document-level routing instead considers the entire document context, leading to domain-specific expert clusters that align with semantic topics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts? | IBM</a></li>

</ul>
</details>

**Tags**: `#MoE`, `#AI2`, `#LLM`, `#routing`, `#model release`

---

<a id="item-13"></a>
## [MTP acceptance rate determines inference speedup](https://www.reddit.com/r/LocalLLaMA/comments/1t7mdrl/mtp_is_all_about_acceptance_rate/) ⭐️ 7.0/10

A user benchmarked multi-token prediction (MTP) on Gemma4-26b-a4b using mlx-vlm on an M4 Max Studio, finding a 1.53× speedup for code generation, negligible gain for long-form prose (0.95×), and a 0.50× slowdown for JSON output. Token acceptance rates were 66%, 31%, and 8% respectively. This demonstrates that MTP's benefit is highly workload-dependent, with speedups only materializing when the draft acceptance rate exceeds roughly 50%. It informs practitioners when to enable speculative decoding in local LLM inference. The test used Gemma4-26b-a4b with structured output disabled, as mlx-vlm does not support spec-decode with JSON schema. The author notes that Gemma's JSON instruction following is good, and disabling structured output reduces the generation penalty, but MTP overhead still dominates at low acceptance rates.

rss · r/LocalLLaMA RSS · May 8, 22:11

**Background**: Multi-token prediction (MTP) is a form of speculative decoding where a smaller draft model generates multiple candidate tokens ahead, and the main model verifies them in parallel. The acceptance rate—fraction of drafted tokens accepted—is the key metric determining speedup. Below ~50% acceptance, the overhead of drafting and verification outweighs the gains.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/mtp/mtp">Gemma 4 Multi-Token Prediction ( MTP ) using Hugging Face...</a></li>
<li><a href="https://huggingface.co/nebius/MTP-DeepSeek-V3-0324">nebius/ MTP -DeepSeek-V3-0324 · Hugging Face</a></li>
<li><a href="https://github.com/Blaizzy/mlx-vlm">GitHub - Blaizzy/ mlx - vlm : MLX - VLM is a package for inference and...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#inference`, `#speculative decoding`, `#MTP`, `#performance`

---

<a id="item-14"></a>
## [Gemma 4 26B Hits 600 tok/s on Single RTX 5090 with DFlash](https://www.reddit.com/r/LocalLLaMA/comments/1t796qe/gemma_4_26b_hits_600_toks_on_one_rtx_5090/) ⭐️ 7.0/10

A user benchmarked Gemma 4 26B (4-bit AWQ) using DFlash speculative decoding in vLLM 0.19.2rc1, achieving up to 578 output tokens per second (2.56x speedup) on a single RTX 5090 with 32GB VRAM. This benchmark demonstrates that speculative decoding can dramatically accelerate LLM inference on consumer hardware, making high-quality models like Gemma 4 practical for real-time agent and chatbot applications at low cost. The optimal configuration used num_speculative_tokens=13 and max_num_batched_tokens=8192; increasing batched tokens improved tail latency despite slightly higher mean latency. The draft model was z-lab/gemma-4-26B-A4B-it-DFlash, a lightweight companion to the main model.

rss · r/LocalLLaMA RSS · May 8, 14:13

**Background**: Speculative decoding is an inference optimization where a small draft model proposes token sequences that a larger target model verifies in one forward pass, preserving output distribution while accelerating generation. vLLM is a high-performance inference engine for LLMs, and AWQ (Activation-aware Weight Quantization) reduces memory footprint with minimal quality loss.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/vllm">vLLM · Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2306.00978">[2306.00978] AWQ : Activation-aware Weight Quantization for LLM...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#speculative decoding`, `#Gemma 4`, `#RTX 5090`, `#LLM inference`

---

<a id="item-15"></a>
## [Ring 2.6 1T Model Free on OpenRouter; Open-Weight Hopes](https://www.reddit.com/r/LocalLLaMA/comments/1t7bvmq/ring_26_1t/) ⭐️ 7.0/10

A new 1 trillion parameter model named Ring 2.6 has been listed for free on OpenRouter, with community members hoping for an open-weight release following the precedent of Ring 2.5 and Ling 2.6. If released as open-weights, this 1T model could significantly advance open-source AI capabilities, offering a rare opportunity for researchers and developers to access a model of this scale without cost. The model is currently only available via OpenRouter's free tier, and its open-weight status remains unconfirmed. The previous version, Ring 2.5, was open-weights, fueling optimism.

rss · r/LocalLLaMA RSS · May 8, 15:50

**Background**: Large language models (LLMs) with 1 trillion parameters (1T) are extremely large and typically require vast computational resources. OpenRouter is a platform that provides access to various AI models, often with free tiers. 'Open weights' means the model's trained parameters are publicly released, allowing local deployment and fine-tuning.

**Tags**: `#LLM`, `#inference`, `#open-source`, `#large model`, `#OpenRouter`

---