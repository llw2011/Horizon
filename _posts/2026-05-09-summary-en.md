---
layout: default
title: "Horizon Summary: 2026-05-09 (EN)"
date: 2026-05-09
lang: en
---

> From 103 items, 16 important content pieces were selected

---

1. [AI is breaking two vulnerability cultures](#item-1) ⭐️ 8.0/10
2. [Anthropic Research: Teaching AI the Reasons Behind Rules](#item-2) ⭐️ 8.0/10
3. [Continuity Benchmark Tests Coding Agent Consistency During Edits](#item-3) ⭐️ 8.0/10
4. [DeepSeek seeks $7.35B funding, plans V4.1 release next month](#item-4) ⭐️ 8.0/10
5. [Gemma 4 26B Hits 600 tok/s on Single RTX 5090 with DFlash](#item-5) ⭐️ 8.0/10
6. [DS4: Specialized Inference Engine for DeepSeek 4 Flash on 128GB MacBooks](#item-6) ⭐️ 8.0/10
7. [HTML Over Markdown for LLM Outputs](#item-7) ⭐️ 7.0/10
8. [Pentagon will avoid single AI provider dependency](#item-8) ⭐️ 7.0/10
9. [AI Model Detects Pancreatic Cancer Up to 3 Years Earlier](#item-9) ⭐️ 7.0/10
10. [AMD's open-source GAIA AI gains Gmail integration](#item-10) ⭐️ 7.0/10
11. [vLLM ROCm Backend Added to Lemonade as Experimental Option](#item-11) ⭐️ 7.0/10
12. [AI2 Releases EMO: 1B/14B MoE with Document-Level Routing](#item-12) ⭐️ 7.0/10
13. [MTP + TurboQuant on Qwen3.6-27B achieves 80+ t/s on RTX 4090 with 262K context](#item-13) ⭐️ 7.0/10
14. [MTP Speedup Depends Heavily on Acceptance Rate](#item-14) ⭐️ 7.0/10
15. [Z-Lab Releases DFlash Speculative Decoding for Gemma-4-26B](#item-15) ⭐️ 7.0/10
16. [CUDA Inference on Apple Silicon via PCI Passthrough](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI is breaking two vulnerability cultures](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures) ⭐️ 8.0/10

AI-assisted exploit generation is accelerating the existing trend of rapid vulnerability exploitation, driven by increased software transparency and improved reversing tools. This shift undermines the traditional vulnerability disclosure ecosystem, making it harder for defenders to stay ahead of attackers, especially for organizations that cannot patch quickly. The article references Log4Shell as an example, where black hats patch-diffed commits before the official patch was released. AI makes exploit generation cheaper and faster, exacerbating the existing asymmetry.

hackernews · speckx · May 8, 17:55 · [Discussion](https://news.ycombinator.com/item?id=48066524)

**Background**: The news discusses two vulnerability cultures: one where vulnerabilities are responsibly disclosed with embargoes, and another where attackers quickly develop and deploy exploits. The increasing transparency of software, such as open source and improved decompilation tools, blurs the line. AI-assisted tools like LLMs can now generate exploit code from vulnerability descriptions, shortening the window for patching.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@instatunnel/wwai-powered-attack-automation-when-machine-learning-writes-the-exploit-code-9eb00af91a51">AI-Powered Attack Automation: When Machine Learning Writes the Exploit Code - Medium</a></li>
<li><a href="https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024">Framing Software Component Transparency (2024) - CISA</a></li>

</ul>
</details>

**Discussion**: Security expert tptacek notes this has been predicted long before LLMs, with the catalyst being software transparency. freeqaz recounts the Log4Shell timeline. rikafurude21 argues this is an old problem reframed as AI, and suggests cheaper exploit generation makes coordinated disclosure more important. dmurray sarcastically suggests moving Linux to closed-source.

**Tags**: `#AI`, `#vulnerability disclosure`, `#LLM security`, `#software transparency`, `#exploit generation`

---

<a id="item-2"></a>
## [Anthropic Research: Teaching AI the Reasons Behind Rules](https://www.anthropic.com/research/teaching-claude-why) ⭐️ 8.0/10

Anthropic has published research on teaching AI models the rationale behind rules rather than just the rules themselves, aiming to improve alignment and generalization. This approach could lead to more robust and flexible AI systems that better understand human values, reducing the risk of reward hacking and misaligned behavior in novel situations. The research uses synthetic data and chain-of-thought reasoning to train models to articulate why certain rules exist, and they found that this improves generalization to out-of-distribution scenarios.

hackernews · pretext · May 8, 17:59 · [Discussion](https://news.ycombinator.com/item?id=48066592)

**Background**: AI alignment aims to ensure AI systems pursue intended goals. Standard training often uses proxy objectives like human approval, which can lead to reward hacking. Teaching models the underlying reasons for rules may help them infer appropriate behavior in new contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://www.alignmentforum.org/">AI Alignment Forum</a></li>

</ul>
</details>

**Discussion**: Commenters noted parallels with philosophy and education, with some questioning whether current alignment definitions are sufficient. Others highlighted that Anthropic has extended similar research to open-weight models, showing broader applicability.

**Tags**: `#AI alignment`, `#Anthropic`, `#LLM training`, `#model behavior`, `#alignment research`

---

<a id="item-3"></a>
## [Continuity Benchmark Tests Coding Agent Consistency During Edits](https://www.reddit.com/r/artificial/comments/1t7m8bg/i_built_a_benchmark_for_ai_memory_in_coding/) ⭐️ 8.0/10

Alienfader released a new benchmark, 'continuity-benchmarks', that evaluates coding agents' ability to stay consistent with project rules during code edits, not just after. Early results show ~3× better action alignment and that retrieval timing is more critical than mere existence. Existing AI memory benchmarks focus on semantic recall, but coding agents often break their own decisions during task execution. This benchmark exposes a critical failure mode and provides a standardized way to compare memory systems, potentially improving the reliability of AI coding agents in production. The benchmark repository includes a full evaluation harness, dataset, and scoring mechanism. It tests multi-session consistency by injecting noise between sessions, and the author challenges others to run their agent memory systems—such as LangChain, LlamaIndex, and custom RAG stacks—against it.

rss · r/artificial RSS · May 8, 22:05

**Background**: Coding agents are AI assistants that autonomously write or edit code. They often use retrieval-augmented generation (RAG) to fetch relevant project context, but during multi-step edits they may lose consistency with earlier architectural decisions. Most benchmarks test memory after task completion, not during execution. This new benchmark fills that gap by measuring consistency while edits are being made.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2603.25764v2">Consistency Amplifies: How Behavioral Variance Shapes Agent ...</a></li>
<li><a href="https://github.com/Abelo9996/agent-consistency">GitHub - Abelo9996/ agent - consistency : How consistent are LLM...</a></li>
<li><a href="https://dataworkers.io/resources/consistency-of-ai-data-agents/">Consistency Of Ai Data Agents | Dataworkers</a></li>

</ul>
</details>

**Tags**: `#AI Agent benchmarks`, `#coding agents`, `#LLM orchestration`, `#agent evaluation`

---

<a id="item-4"></a>
## [DeepSeek seeks $7.35B funding, plans V4.1 release next month](https://www.reddit.com/r/LocalLLaMA/comments/1t7bfpw/reports_suggest_deepseek_is_seeking_735_billion/) ⭐️ 8.0/10

DeepSeek is reportedly raising up to $7.35 billion (RMB 50 billion) in its first funding round, with founder Liang Wenfeng contributing the maximum allowable amount. The company also plans to launch V4.1, an updated version of its V4 model, in June. This record funding round for a Chinese AI company signals DeepSeek's aggressive push into commercialization and monetization, potentially reshaping the competitive landscape of open-weight LLMs. The rapid iteration to V4.1 also indicates an accelerated release cadence that may increase pressure on rivals like OpenAI and Meta. The funding round could reach RMB 50 billion ($7.35 billion), making it the largest single fundraising round in Chinese AI history. The V4.1 update is expected in June, following the V4 Preview released in April 2026 with 1M context length and cost-efficient performance.

rss · r/LocalLLaMA RSS · May 8, 15:34

**Background**: DeepSeek is a leading open-weight AI company known for its large language models that rival proprietary systems at lower cost. Its V4 model, released as a preview in April 2026, offers a 1 million-token context window and strong agent capabilities. The company has gained attention for its cost-effective approach and open-source contributions.

<details><summary>References</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/news/news260424">DeepSeek V4 Preview Release</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Funding`, `#V4.1`, `#LLM`, `#Open-Source`

---

<a id="item-5"></a>
## [Gemma 4 26B Hits 600 tok/s on Single RTX 5090 with DFlash](https://www.reddit.com/r/LocalLLaMA/comments/1t796qe/gemma_4_26b_hits_600_toks_on_one_rtx_5090/) ⭐️ 8.0/10

A benchmark demonstrates that the Gemma 4 26B quantized model achieves 578 output tokens per second on a single RTX 5090 using DFlash speculative decoding in vLLM 0.19.2rc1, a 2.56x speedup over the baseline without speculation. This result highlights the potential of speculative decoding as a practical technique for significantly speeding up LLM inference on consumer GPUs, making larger models more usable for local applications and reducing latency. The benchmark used a 4-bit AWQ quantized main model and a specialized DFlash draft model, with the best performance observed at num_speculative_tokens=13 and max_num_batched_tokens=8192, yielding ~578 tok/s and ~1738 ms mean end-to-end latency.

rss · r/LocalLLaMA RSS · May 8, 14:13

**Background**: Speculative decoding is a technique to accelerate autoregressive LLM generation by using a small draft model to propose multiple tokens per step, which are then verified by the main model in parallel. DFlash is a block diffusion framework that further improves efficiency by generating draft sequences coherently. vLLM is an open-source inference engine that supports various optimization methods, including speculative decoding.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/z-lab/dflash">DFlash: Block Diffusion for Flash Speculative Decoding - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2602.06036">DFlash: Block Diffusion for Flash Speculative Decoding</a></li>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#speculative decoding`, `#Gemma 4`, `#RTX 5090`, `#inference optimization`

---

<a id="item-6"></a>
## [DS4: Specialized Inference Engine for DeepSeek 4 Flash on 128GB MacBooks](https://www.reddit.com/r/LocalLLaMA/comments/1t72tk9/ds4_a_deepseek_4_flash_specific_inference_engine/) ⭐️ 8.0/10

Antirez, the creator of Redis, released DS4, a dedicated inference engine for DeepSeek V4 Flash that runs efficiently on 128GB MacBooks using Metal acceleration. This development significantly lowers the barrier for running state-of-the-art LLMs locally on consumer hardware, enabling developers and researchers to deploy DeepSeek V4 Flash without cloud dependency. DS4 is a small C-based engine that uses only specific GGUF files provided by the author and has been tested against official logits at various context sizes.

rss · r/LocalLLaMA RSS · May 8, 09:26

**Background**: DeepSeek V4 Flash is a lightweight variant of DeepSeek's V4 model, designed for faster inference and lower cost while approaching Pro-level capabilities. Running such models locally on MacBooks has been challenging due to memory and computational constraints. DS4 leverages Apple's Metal framework to optimize performance on the unified memory architecture of 128GB MacBooks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ ds 4 : DeepSeek 4 Flash local inference engine for Metal</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424">DeepSeek V4 Preview Release | DeepSeek API Docs</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#DeepSeek`, `#MacBook optimization`, `#open-source`, `#local LLM`

---

<a id="item-7"></a>
## [HTML Over Markdown for LLM Outputs](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/#atom-everything) ⭐️ 7.0/10

Thariq Shihipar, a member of the Claude Code team at Anthropic, advocates for requesting HTML instead of Markdown from Claude to obtain richer, more structured outputs, providing examples and prompt suggestions. Simon Willison echoes the idea, highlighting that HTML allows embedding SVG diagrams, interactive widgets, and in-page navigation, which Markdown cannot. This shift from Markdown to HTML for LLM outputs can significantly improve the clarity and interactivity of generated explanations, benefiting developers, technical writers, and anyone using LLMs for complex document generation. It also reflects a broader trend toward leveraging HTML's full capabilities in agentic workflows and prompt engineering. The article includes specific prompt examples, such as asking Claude to review a pull request by creating an HTML artifact with inline margin annotations and color-coded findings. Simon Willison also tested the approach with GPT-5.5 on a Linux security exploit from copy.fail, generating an interactive HTML explanation.

rss · Simon Willison · May 8, 21:00

**Background**: Markdown has been a popular output format for LLMs due to its token efficiency, which was crucial during the GPT-4 era with its 8,192 token limit. HTML, while less token-efficient, offers richer formatting capabilities such as tables, embedded images, CSS styling, and interactive JavaScript components. Claude Code is Anthropic's agentic coding tool that helps developers understand codebases, edit files, and run commands.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://grokipedia.com/page/Claude_Code">Claude Code</a></li>

</ul>
</details>

**Tags**: `#prompt engineering`, `#HTML`, `#Claude`, `#LLM output`, `#agent interaction`

---

<a id="item-8"></a>
## [Pentagon will avoid single AI provider dependency](https://www.nextgov.com/artificial-intelligence/2026/05/pentagon-will-never-again-rely-single-ai-provider-official-says/413399/) ⭐️ 7.0/10

A Pentagon official announced that the department will 'never again' rely on a single AI provider, signaling a strategic shift toward multi-provider solutions and open standards. This policy shift could accelerate adoption of interoperability standards like MCP and A2A, reduce vendor lock-in risks, and foster a more competitive AI ecosystem benefiting national security and innovation. The statement was made in the context of the Pentagon's broader AI strategy, emphasizing the need for modular, interchangeable AI components to avoid past mistakes of over-reliance on single vendors.

rss · Hacker News - AI & Agents · May 8, 21:26

**Background**: The Pentagon has historically faced challenges with vendor lock-in, especially in large defense contracts. By mandating multi-provider AI, the department aims to increase flexibility, resilience, and competition, while promoting open architectures and data interoperability.

**Tags**: `#AI policy`, `#Pentagon`, `#multi-provider`, `#AI agents`, `#interoperability`

---

<a id="item-9"></a>
## [AI Model Detects Pancreatic Cancer Up to 3 Years Earlier](https://www.reddit.com/r/artificial/comments/1t7au63/new_ai_model_spots_pancreatic_cancer_up_to_3/) ⭐️ 7.0/10

A new AI model called REDMOD, developed by the Mayo Clinic, can detect pancreatic cancer on routine CT scans up to three years before clinical diagnosis, as reported in a study published in Gut. Pancreatic cancer has a five-year survival rate of only 13% because it is often detected too late; earlier detection could dramatically improve survival outcomes and change treatment paradigms. The REDMOD model uses radiomics to identify subtle, subvisual signatures of pancreatic ductal adenocarcinoma in standard-of-care CT images, and it was validated as part of the ongoing AI-PACED prospective clinical trial at Mayo Clinic.

rss · r/artificial RSS · May 8, 15:12

**Background**: Pancreatic cancer is notoriously difficult to detect early because symptoms often appear only at advanced stages, and conventional imaging may miss precancerous changes. AI models like REDMOD aim to overcome this by learning patterns invisible to the human eye from large datasets of CT scans.

<details><summary>References</summary>
<ul>
<li><a href="https://gut.bmj.com/content/early/2026/04/22/gutjnl-2025-337266">Next-generation AI for visually occult pancreatic cancer ...</a></li>
<li><a href="https://www.goodnewsnetwork.org/mayo-clinic-creates-ai-that-can-detect-pancreatic-cancer-up-to-3-years-before-diagnosis/">Mayo Clinic’s AI Can Detect Pancreatic Cancer up to 3 Years ...</a></li>
<li><a href="https://www.insideprecisionmedicine.com/topics/oncology/mayo-clinics-redmod-ai-doubles-early-detection-sensitivity-in-pancreatic-cancer/">Mayo Clinic's REDMOD AI Doubles Early Detection Sensitivity ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#healthcare`, `#pancreatic cancer`, `#medical AI`

---

<a id="item-10"></a>
## [AMD's open-source GAIA AI gains Gmail integration](https://www.reddit.com/r/artificial/comments/1t77n9a/amds_local_opensource_ai_can_now_easily_interact/) ⭐️ 7.0/10

AMD's open-source GAIA AI assistant has added Gmail integration, allowing it to read and interact with emails locally on AMD Ryzen AI PCs. This integration demonstrates practical, privacy-preserving AI agent tool use for everyday tasks, reducing reliance on cloud services and keeping data local. GAIA is built on AMD's open-source framework and runs entirely on local AMD Ryzen AI hardware, requiring no internet connection for core AI operations.

rss · r/artificial RSS · May 8, 13:15

**Background**: GAIA is AMD's open-source software development kit (SDK) for building AI agents that run locally on Ryzen AI PCs. It enables developers to create private, offline AI assistants that can interact with applications and services via tool-use APIs like Gmail.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/amd/gaia">GitHub - amd/gaia: Build AI agents for your PC · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#open-source`, `#tool use`, `#AMD`, `#email integration`

---

<a id="item-11"></a>
## [vLLM ROCm Backend Added to Lemonade as Experimental Option](https://www.reddit.com/r/LocalLLaMA/comments/1t7g70j/vllm_rocm_has_been_added_to_lemonade_as_an/) ⭐️ 7.0/10

AMD has added experimental support for the vLLM ROCm backend to the Lemonade local AI runtime, allowing users to run safetensors LLMs on AMD GPUs with simple commands like `lemonade backends install vllm:rocm`. This integration fills a gap in the AMD GPU ecosystem, providing an easy way to leverage vLLM's high-performance inference for safetensors models without requiring model conversion to GGUF. It broadens hardware options for LLM users and could accelerate adoption of AMD GPUs for local AI workloads. The backend is considered experimental, with day-0 model support, multi-GPU concurrency, and a self-contained bundle. Currently only Linux is supported, and users are encouraged to provide feedback on rough edges.

rss · r/LocalLLaMA RSS · May 8, 18:21

**Background**: vLLM is a high-performance inference engine for large language models, originally built for NVIDIA CUDA but since expanded to AMD ROCm. Lemonade is an open-source local AI runtime sponsored by AMD that provides a unified interface to run models on various backends. Safetensors is a model format that stores weights safely, while GGUF is another format that bundles everything into one file. This addition allows Lemonade users to run safetensors LLMs on AMD GPUs using vLLM instead of having to convert to GGUF for llama.cpp.

<details><summary>References</summary>
<ul>
<li><a href="https://lemonade-server.ai/news/vllm-rocm.html">vLLM ROCm now in Lemonade - Lemonade Server</a></li>
<li><a href="https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/vllm-optimization.html">vLLM V1 performance optimization — ROCm Documentation</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#ROCm`, `#AMD`, `#Lemonade`, `#LLM inference`

---

<a id="item-12"></a>
## [AI2 Releases EMO: 1B/14B MoE with Document-Level Routing](https://www.reddit.com/r/LocalLLaMA/comments/1t7kgy4/new_moe_from_ai2_emo/) ⭐️ 7.0/10

AI2 (Allen Institute for AI) has released EMO, a new Mixture-of-Experts (MoE) language model with 1 billion active parameters and 14 billion total parameters, trained on 1 trillion tokens. The key innovation is document-level routing, where experts specialize in broad domains such as health and news rather than token-level patterns. EMO's emergent modularity through document-level routing could lead to more efficient inference and better domain specialization, making large models more practical for deployment. This open-source contribution advances MoE architecture research and may inspire further work on expert specialization. The model uses a document-level routing mechanism that clusters experts by domain (e.g., health, news) instead of token-level surface patterns. EMO is available on Hugging Face as part of the allenai/emo collection, and was pretrained end-to-end without human-defined priors for expert specialization.

rss · r/LocalLLaMA RSS · May 8, 20:57

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that uses multiple specialized sub-networks (experts) and a routing mechanism to activate only a subset of experts for each input, improving efficiency. Traditional MoE models use token-level routing, where each token is sent to the top-k experts, which can lead to fragmented specialization. Document-level routing instead routes entire documents to specific experts, encouraging broader domain-level specialization.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/allenai/emo">EMO: Pretraining mixture of experts for emergent modularity</a></li>
<li><a href="https://x.com/allen_ai/status/2052784995710681180">Ai2 on X: "Today we’re releasing EMO, a new mixture-of-experts (MoE) model trained so modular structure emerges directly from data without human-defined priors. EMO can use a small subset of its experts for a given task while keeping near full-model performance. 🧵 https://t.co/xXcWsYh50D" / X</a></li>

</ul>
</details>

**Tags**: `#MoE`, `#AI2`, `#EMO`, `#LLM architecture`, `#document routing`

---

<a id="item-13"></a>
## [MTP + TurboQuant on Qwen3.6-27B achieves 80+ t/s on RTX 4090 with 262K context](https://www.reddit.com/r/LocalLLaMA/comments/1t7kyju/got_mtp_turboquant_running_qwen3627b_80_ts_at/) ⭐️ 7.0/10

A user has combined Multi-Token Prediction (MTP) and TurboQuant's lossless KV cache compression (TBQ4_0) on a modified llama.cpp fork to run Qwen3.6-27B at 80–87 tokens per second with 262K context on a single RTX 4090. This demonstrates that large long-context models can run efficiently on consumer hardware, potentially enabling more accessible and faster local LLM inference for complex tasks. The setup uses Qwen3.6-27B-Heretic-v2 quantized to Q4_K_M, with grafted MTP heads and TurboQuant's TBQ4_0 KV cache quantization, achieving ~73% MTP draft acceptance. The code is available on GitHub as a fork of llama.cpp.

rss · r/LocalLLaMA RSS · May 8, 21:15

**Background**: Multi-Token Prediction (MTP) is a technique where an LLM predicts multiple future tokens simultaneously, enabling speculative decoding to accelerate inference. TurboQuant is a lossless quantization method for KV cache, reducing memory usage without sacrificing output quality. The combination allows models with large context windows to run on limited GPU memory.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Firmamento-Technologies/TurboQuant">GitHub - Firmamento-Technologies/ TurboQuant : Near-optimal vector...</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/mtp/">Multi - Token Prediction ( MTP ) | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**Discussion**: The Reddit post received a score of 7.0, indicating positive reception. The user notes they are not a professional and welcome feedback, encouraging community testing of the fork.

**Tags**: `#LLM inference`, `#MTP`, `#TurboQuant`, `#llama.cpp`, `#local LLM`

---

<a id="item-14"></a>
## [MTP Speedup Depends Heavily on Acceptance Rate](https://www.reddit.com/r/LocalLLaMA/comments/1t7mdrl/mtp_is_all_about_acceptance_rate/) ⭐️ 7.0/10

A user benchmarked Multi-Token Prediction (MTP) on Gemma4 using mlx-vlm and found that the acceptance rate varies dramatically by workload, with code generation achieving a 1.53x speedup (66% acceptance) but JSON output being 0.5x slower (8% acceptance). This highlights that MTP is not universally beneficial; its effectiveness hinges on the draft acceptance rate. Developers must evaluate MTP's cost-benefit for their specific use case, especially for structured output tasks where acceptance may be very low. The benchmarks were run on an M4 Max Studio with Gemma4-26b-a4b, using mlx-vlm without json_schema support for speculative decoding. The user observed that once token acceptance dips below 50%, the overhead of verification kills the benefit.

rss · r/LocalLLaMA RSS · May 8, 22:11

**Background**: Multi-Token Prediction (MTP) is a speculative decoding technique where a lightweight draft model predicts multiple future tokens in one forward pass, and the target model verifies them in parallel. The acceptance rate—the fraction of draft tokens accepted by the target model—determines the effective speedup. If the draft predictions are often rejected, the overhead of generating and verifying drafts can degrade overall performance.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters - Google Blog</a></li>
<li><a href="https://ai.google.dev/gemma/docs/mtp/mtp">Gemma 4 Multi-Token Prediction (MTP) using Hugging Face Transformers</a></li>
<li><a href="https://www.generalcompute.com/blog/draft-model-selection-for-speculative-decoding">Draft Model Selection for Speculative Decoding | General ...</a></li>

</ul>
</details>

**Tags**: `#MTP`, `#speculative decoding`, `#LLM inference`, `#localLLaMA`, `#optimization`

---

<a id="item-15"></a>
## [Z-Lab Releases DFlash Speculative Decoding for Gemma-4-26B](https://www.reddit.com/r/LocalLLaMA/comments/1t79ayh/zlab_released_gemma426ba4bitdflash_anybody_tried/) ⭐️ 7.0/10

Z-lab has released a DFlash version of Gemma-4-26B, a speculative decoding technique that uses block diffusion drafting to generate multiple tokens in parallel. This model claims faster generation than multi-token prediction (MTP) methods, especially for long contexts. DFlash could significantly improve inference efficiency for large language models, achieving lossless speedups of up to 6x. It offers a promising alternative to MTP, particularly for sparse models like Gemma-4-26B and Qwen-3.6-35B, and its stateful design reduces KV cache overhead in long sessions. DFlash uses a lightweight block diffusion model as a drafter, conditioned on the target model's hidden states, enabling parallel block drafting. It currently supports only vLLM inference engine, and community interest exists in bringing it to llama.cpp.

rss · r/LocalLLaMA RSS · May 8, 14:18

**Background**: Speculative decoding accelerates LLM inference by using a small 'drafter' model to propose multiple tokens, which are then verified by the large target model. DFlash is a new method where the drafter is a block diffusion model that predicts entire blocks of tokens in one pass, rather than autoregressively. In contrast, MTP trains a multi-token prediction head on the target model itself. DFlash is designed to be lightweight and maintain a persistent state across iterations, reducing recomputation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.06036">[2602.06036] DFlash: Block Diffusion for Flash Speculative Decoding - arXiv</a></li>
<li><a href="https://github.com/z-lab/dflash">DFlash: Block Diffusion for Flash Speculative Decoding - GitHub</a></li>
<li><a href="https://z-lab.ai/projects/dflash/">DFlash: Block Diffusion for Flash Speculative Decoding - Z Lab</a></li>

</ul>
</details>

**Tags**: `#inference`, `#speculative decoding`, `#gemma-4`, `#dflash`, `#open-source`

---

<a id="item-16"></a>
## [CUDA Inference on Apple Silicon via PCI Passthrough](https://www.reddit.com/r/LocalLLaMA/comments/1t7cqg9/you_can_do_cuda_inference_on_an_apple_silicon_mac/) ⭐️ 7.0/10

A user has demonstrated running CUDA inference on an Apple Silicon Mac by using QEMU with PCI passthrough to give a Linux VM direct access to an external NVIDIA GPU. The setup includes AI benchmarks, showing that GPU-accelerated LLM inference is possible on Mac hardware previously limited to Metal frameworks. This workaround breaks the long-standing limitation that Apple Silicon Macs cannot run CUDA, opening the door for Mac users to leverage NVIDIA GPUs for local AI inference and development. It highlights the growing demand for GPU passthrough solutions in the Apple ecosystem and could influence future virtualization or driver support. The method requires an external GPU enclosure connected via Thunderbolt and relies on QEMU's PCI passthrough implementation on macOS, which is still experimental. The benchmarks focus on gaming but include AI inference results, though performance may be lower than native x86 systems due to virtualization overhead.

rss · r/LocalLLaMA RSS · May 8, 16:20

**Background**: Apple Silicon Macs use Apple's own GPU architecture and do not support NVIDIA CUDA, which is the dominant framework for GPU-accelerated AI workloads. PCI passthrough is a virtualization technique that allows a virtual machine to directly control a physical PCI device, such as a GPU. Traditionally, PCI passthrough on macOS has been challenging due to Apple's limited I/O virtualization support, but recent efforts have made it feasible for external GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://pve.proxmox.com/wiki/PCI(e)_Passthrough">PCI(e) Passthrough - Proxmox VE</a></li>
<li><a href="https://appleinsider.com/articles/26/04/04/amd-or-nvidia-egpus-can-work-on-apple-silicon-macs-but-not-for-graphic-acceleration">AMD or Nvidia eGPUs can work on Apple Silicon Macs, but not for graphic acceleration</a></li>
<li><a href="https://wiki.archlinux.org/title/QEMU/Guest_graphics_acceleration">QEMU /Guest graphics acceleration - ArchWiki</a></li>

</ul>
</details>

**Tags**: `#Apple Silicon`, `#CUDA`, `#PCI Passthrough`, `#LLM Inference`, `#QEMU`

---