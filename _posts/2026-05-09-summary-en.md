---
layout: default
title: "Horizon Summary: 2026-05-09 (EN)"
date: 2026-05-09
lang: en
---

> From 103 items, 15 important content pieces were selected

---

1. [Anthropic Teaches Claude to Understand Its Own Reasoning](#item-1) ⭐️ 9.0/10
2. [OpenAI Agents SDK v0.17.0: Default model change and sandbox fix](#item-2) ⭐️ 8.0/10
3. [Why HTML Beats Markdown for Claude Code Prompts](#item-3) ⭐️ 8.0/10
4. [Agentic Coding Tools Analysis: Claude Code and Codex](#item-4) ⭐️ 8.0/10
5. [AI detects pancreatic cancer 3 years earlier than doctors](#item-5) ⭐️ 8.0/10
6. [MTP + TurboQuant on Qwen3.6-27B: 80+ t/s on RTX 4090](#item-6) ⭐️ 8.0/10
7. [DeepSeek Seeks $7.35B Funding, Plans V4.1 Launch](#item-7) ⭐️ 8.0/10
8. [Gemma 4 26B Achieves 2.56x Speedup to 578 tok/s on RTX 5090 with DFlash](#item-8) ⭐️ 8.0/10
9. [AI is breaking two vulnerability cultures](#item-9) ⭐️ 7.0/10
10. [New Benchmark Tests AI Coding Agent Memory Consistency](#item-10) ⭐️ 7.0/10
11. [AMD's GAIA open-source AI now integrates with Gmail](#item-11) ⭐️ 7.0/10
12. [Asian AI Strategies: Vietnam's Law, Japan's No Penalties, Korea's Naver Exclusion](#item-12) ⭐️ 7.0/10
13. [Qwen 35B-A3B MoE Runs Well on 12GB GPU](#item-13) ⭐️ 7.0/10
14. [AI2 Releases EMO: 1B/14B MoE with Document-Level Routing](#item-14) ⭐️ 7.0/10
15. [DS4: Custom Inference Engine for DeepSeek 4 Flash on 128GB MacBooks](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic Teaches Claude to Understand Its Own Reasoning](https://www.anthropic.com/research/teaching-claude-why) ⭐️ 9.0/10

Anthropic has published new research exploring how to train Claude to understand its own internal reasoning, aiming to improve AI alignment and transparency. This work could lead to safer and more controllable AI agents, as models that can explain their reasoning are easier to audit and align with human values. The research focuses on teaching models to introspect on their reasoning chains, potentially generalizing beyond Claude to other open-weight models as shown in related work like Model Spec Midtraining.

hackernews · pretext · May 8, 17:59 · [Discussion](https://news.ycombinator.com/item?id=48066592)

**Background**: AI alignment aims to encode human values and goals into large language models to make them helpful, safe, and reliable. Understanding how models reason is a key challenge, as current LLMs often lack transparency in their decision-making processes.

<details><summary>References</summary>
<ul>
<li><a href="https://research.ibm.com/blog/what-is-alignment-ai">What is AI alignment ? - IBM Research</a></li>
<li><a href="https://serokell.io/blog/what-is-ai-alignment">What Is AI Alignment ?</a></li>
<li><a href="https://news.mit.edu/2025/large-language-models-reason-about-diverse-data-general-way-0219">Like human brains, large language models reason about diverse data in a general way | MIT News | Massachusetts Institute of Technology</a></li>

</ul>
</details>

**Discussion**: Comments reflect a mix of philosophical alignment concerns and technical interest. Users question whether aligned models could still cause societal harm, while others see alignment as a pedagogical challenge. Some point to related open-weight research as complementary.

**Tags**: `#AI alignment`, `#Anthropic`, `#LLM reasoning`, `#AI safety`, `#agentic AI`

---

<a id="item-2"></a>
## [OpenAI Agents SDK v0.17.0: Default model change and sandbox fix](https://github.com/openai/openai-agents-python/releases/tag/v0.17.0) ⭐️ 8.0/10

OpenAI released v0.17.0 of its openai-agents-python SDK, changing the default model for RealtimeAgent from previous versions to gpt-realtime-2. The release also tightens sandbox local source materialization to prevent files outside the base directory from being copied unless explicitly granted. This update is significant because gpt-realtime-2 offers GPT-5-class reasoning and improved audio understanding, enhancing voice agent capabilities. The sandbox security fix closes a potential vulnerability where host files could be unintentionally exposed to sandbox environments. The gpt-realtime-2 model supports 128K context, five reasoning levels, and parallel tool calling, with significant benchmark improvements over its predecessor. The sandbox change requires developers to use SandboxPathGrant with read-only access for host paths outside the SDK process current working directory.

github · seratch · May 8, 08:09

**Background**: The OpenAI Agents SDK is a Python toolkit for building AI agents with features like tool use, handoffs, and sandbox environments. RealtimeAgent is a specialized agent for low-latency voice interactions via the Realtime API using WebSocket transport. Sandbox materialization refers to copying local files into a sandbox environment for agent tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.github.io/openai-agents-python/ref/realtime/agent/">RealtimeAgent - OpenAI Agents SDK</a></li>
<li><a href="https://openai.github.io/openai-agents-python/sandbox/guide/">Concepts - OpenAI Agents SDK</a></li>
<li><a href="https://awesomeagents.ai/models/gpt-realtime-2/">GPT - Realtime - 2 | Awesome Agents</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#agents-sdk`, `#release`, `#AI agents`

---

<a id="item-3"></a>
## [Why HTML Beats Markdown for Claude Code Prompts](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/#atom-everything) ⭐️ 8.0/10

Thariq Shihipar from Anthropic's Claude Code team advocates for requesting HTML output instead of Markdown when prompting Claude, providing concrete examples and prompt templates. Simon Willison tested this approach with GPT-5.5 to explain a Linux exploit, producing a rich HTML page with interactive elements. This shift in prompt engineering can significantly improve the quality of AI-generated explanations by enabling richer formatting, inline diagrams, and interactive widgets, especially beneficial for agentic coding workflows. It challenges the long-held preference for Markdown due to token efficiency, offering a more effective way to convey complex information. The article recommends prompts like 'Help me review this PR by creating an HTML artifact that describes it' and includes a dedicated site with examples. Simon's test with GPT-5.5 on the copy.fail exploit produced an HTML page with a yellow-bordered safety callout and numbered steps, but the output focused more on the Python harness than the exploit itself, highlighting the need for precise instructions.

rss · Simon Willison · May 8, 21:00

**Background**: Claude Code is Anthropic's agentic coding tool for developers, allowing AI to understand codebases, edit files, and run commands. Historically, Markdown has been preferred for LLM outputs due to its token efficiency, especially during the GPT-4 era with limited context windows. HTML, while more token-heavy, offers far richer formatting capabilities such as SVG diagrams, in-page navigation, and interactive widgets, making it more effective for complex explanations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#LLM prompting`, `#HTML`, `#agentic workflows`, `#prompt engineering`

---

<a id="item-4"></a>
## [Agentic Coding Tools Analysis: Claude Code and Codex](https://thezvi.substack.com/p/claude-code-codex-and-agentic-coding-f54) ⭐️ 8.0/10

This article analyzes Claude Code, Codex, and other agentic coding tools, discussing their impact on AI-assisted software development, including their capabilities, limitations, and implications for developers. As agentic coding tools become more sophisticated, they have the potential to significantly boost developer productivity and change the software development workflow, making this analysis valuable for understanding the current state and future direction of AI in coding. The article provides a detailed comparison of Claude Code (by Anthropic) and Codex (by OpenAI), covering their underlying models, code editing and execution capabilities, and how they integrate into developer environments. It also addresses potential risks and limitations of these tools.

rss · Hacker News - AI & Agents · May 8, 21:23

**Background**: Claude Code is an agentic coding tool developed by Anthropic that understands codebases, edits files, and runs commands. Codex is OpenAI's software engineering agent designed to help with coding, debugging, and code review. Both tools represent a new paradigm of AI-assisted programming where the agent actively collaborates with developers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://openai.com/index/running-codex-safely/">Running Codex safely at OpenAI | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Agentic Coding`, `#Claude Code`, `#Codex`, `#LLM Tools`

---

<a id="item-5"></a>
## [AI detects pancreatic cancer 3 years earlier than doctors](https://www.reddit.com/r/artificial/comments/1t7au63/new_ai_model_spots_pancreatic_cancer_up_to_3/) ⭐️ 8.0/10

A new AI model has demonstrated the ability to detect pancreatic cancer up to three years earlier than human doctors in a clinical test, potentially allowing for earlier intervention. Pancreatic cancer is notoriously difficult to detect early and has a low survival rate; earlier detection could significantly improve patient outcomes and reduce mortality. The AI model analyzes medical imaging data, such as CT scans or MRIs, to identify subtle indicators of pancreatic cancer that may be missed by the human eye. The test showed a 3-year lead time over standard diagnosis.

rss · r/artificial RSS · May 8, 15:12

**Background**: Pancreatic cancer often presents no symptoms until advanced stages, making early detection challenging. AI models trained on large datasets can learn to recognize patterns associated with early-stage disease, offering a promising tool for screening high-risk populations.

**Tags**: `#AI`, `#healthcare`, `#pancreatic cancer`, `#machine learning`, `#medical imaging`

---

<a id="item-6"></a>
## [MTP + TurboQuant on Qwen3.6-27B: 80+ t/s on RTX 4090](https://www.reddit.com/r/LocalLLaMA/comments/1t7kyju/got_mtp_turboquant_running_qwen3627b_80_ts_at/) ⭐️ 8.0/10

A Reddit user successfully integrated Multi-Token Prediction (MTP) with TurboQuant KV cache quantization (TBQ4_0) on the Qwen3.6-27B model, achieving 80-87 tokens per second with 262K context on a single RTX 4090. This demonstrates that combining MTP speculative decoding with extreme KV cache quantization can dramatically increase inference throughput on consumer hardware, making long-context local LLM inference far more practical for developers and enthusiasts. The setup uses Qwen3.6-27B-Heretic-v2 in Q4_K_M quantization with grafted MTP heads, running on Ubuntu 24.04 with CUDA 12.x. The user reported an MTP draft acceptance rate of about 73% and has released a fork of llama.cpp with the integration.

rss · r/LocalLLaMA RSS · May 8, 21:15

**Background**: Multi-Token Prediction (MTP) is a speculative decoding technique where a lightweight drafter predicts multiple future tokens in parallel, while TurboQuant is a method for near-lossless quantization of the KV cache to very low bit widths (e.g., 4.25 bits per value). Combining these can reduce memory bandwidth and computational overhead, enabling faster inference at long contexts on limited hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/20969">TurboQuant - Extreme KV Cache Quantization · ggml-org/llama.cpp · Discussion #20969</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#quantization`, `#MTP`, `#llama.cpp`, `#local LLM`

---

<a id="item-7"></a>
## [DeepSeek Seeks $7.35B Funding, Plans V4.1 Launch](https://www.reddit.com/r/LocalLLaMA/comments/1t7bfpw/reports_suggest_deepseek_is_seeking_735_billion/) ⭐️ 8.0/10

DeepSeek is reportedly seeking to raise up to $7.35 billion (RMB 50 billion) in its first funding round and plans to release an updated V4.1 model in June. This would be the largest single fundraising round by a Chinese AI company, signaling DeepSeek's push to accelerate commercialization and compete with major LLM providers. Founder Liang Wenfeng plans to contribute the maximum allowable amount in this round. The company intends to speed up model release cadence to align with industry practices.

rss · r/LocalLLaMA RSS · May 8, 15:34

**Background**: DeepSeek is a Chinese AI startup known for its large language models, including the V4 series. The V4 model has gained attention for its competitive performance. This funding round aims to support revenue-generation plans and rapid iteration.

**Tags**: `#DeepSeek`, `#funding`, `#LLM`, `#AI industry news`, `#V4.1`

---

<a id="item-8"></a>
## [Gemma 4 26B Achieves 2.56x Speedup to 578 tok/s on RTX 5090 with DFlash](https://www.reddit.com/r/LocalLLaMA/comments/1t796qe/gemma_4_26b_hits_600_toks_on_one_rtx_5090/) ⭐️ 8.0/10

A benchmark by a Reddit user showed that using DFlash speculative decoding in vLLM on a single RTX 5090, the Gemma 4 26B model reached 578 output tokens per second, a 2.56x speedup over the 228 tok/s baseline without speculative decoding. This demonstrates that advanced speculative decoding techniques can drastically improve inference throughput on consumer-grade GPUs, making large language models more practical for local deployment and real-time applications. The optimal setting was num_speculative_tokens=13 and max_num_batched_tokens=8192, with mean latency dropping from 4455 ms to 1738 ms. Notably, the fastest average setting was not always the best for serving, as a larger batch size (8192 vs 4096) improved tail latency.

rss · r/LocalLLaMA RSS · May 8, 14:13

**Background**: Speculative decoding is a technique where a small, fast draft model proposes multiple tokens that a larger target model then verifies in parallel, enabling up to 2-3x speedups without loss of quality. DFlash is a novel block diffusion model designed specifically for lightweight speculative drafting. vLLM is a high-throughput inference engine that supports various speculative decoding methods, including DFlash.

<details><summary>References</summary>
<ul>
<li><a href="https://z-lab.ai/projects/dflash/">DFlash : Block Diffusion for Flash Speculative Decoding - Z Lab</a></li>
<li><a href="https://github.com/z-lab/dflash">z-lab/ dflash : DFlash : Block Diffusion for Flash Speculative Decoding ...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/">Speculative Decoding - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#speculative decoding`, `#Gemma 4`, `#RTX 5090`, `#LLM inference`

---

<a id="item-9"></a>
## [AI is breaking two vulnerability cultures](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures) ⭐️ 7.0/10

AI is accelerating the generation of exploit code and reshaping vulnerability disclosure practices, exposing pre-existing tensions between full disclosure and coordinated patching. This could shorten disclosure windows, making it harder for smaller organizations to patch in time, and may fundamentally alter the open-source security ecosystem. The article argues that AI enables rapid exploit generation from patches or descriptions, effectively eliminating the protective window of coordinated disclosure and forcing a reckoning between transparency and security.

hackernews · speckx · May 8, 17:55 · [Discussion](https://news.ycombinator.com/item?id=48066524)

**Background**: Coordinated vulnerability disclosure (CVD) is a model where researchers privately notify vendors and allow time for a patch before public disclosure. Full disclosure releases details immediately. AI's ability to generate working exploits from minimal information undermines the coordination model, as attackers can now exploit vulnerabilities before patches are deployed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure</a></li>

</ul>
</details>

**Discussion**: tptacek noted this shift has been long anticipated, driven by software transparency and reversing tools, not just LLMs. freeqaz cited Log4Shell as a case where commit monitoring led to attacks. rikafurude21 argued this is an old problem reframed, and cheaper exploit generation may actually make coordinated disclosure more important. dmurray sarcastically suggested Linux move to a closed-source model.

**Tags**: `#AI security`, `#vulnerability disclosure`, `#open source`, `#cybersecurity`, `#LLM impact`

---

<a id="item-10"></a>
## [New Benchmark Tests AI Coding Agent Memory Consistency](https://www.reddit.com/r/artificial/comments/1t7m8bg/i_built_a_benchmark_for_ai_memory_in_coding/) ⭐️ 7.0/10

A developer has released a new benchmark called Continuity Benchmarks that evaluates how consistently AI coding agents follow project rules during task execution, rather than just measuring semantic recall. Early results show approximately 3× better action alignment and significantly stronger multi-session consistency compared to baseline RAG-style memory setups. Existing AI agent benchmarks overlook a critical failure mode: coding agents often violate their own earlier decisions while working. This benchmark fills that gap and provides a standardized way to compare memory systems for agents, which is essential for building reliable long-running coding agents. The benchmark checks whether edits respect earlier architectural decisions, whether behavior stays consistent across multiple sessions with noise, and whether retrieval kicks in at the right moment. The full harness, dataset, and scoring method are available on GitHub at github.com/Alienfader/continuity-benchmarks.

rss · r/artificial RSS · May 8, 22:05

**Background**: AI coding agents use large language models to generate and modify code over multiple steps. Most existing memory benchmarks test semantic recall, which is essentially RAG-based search for relevant information, but they do not test whether an agent can maintain consistency with its own past decisions during active development. This new benchmark focuses on action consistency—a dimension that has been largely ignored.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-agent-memory/">Agents that remember: introducing Agent Memory</a></li>
<li><a href="https://www.letta.com/blog/benchmarking-ai-agent-memory">Benchmarking AI Agent Memory: Is a Filesystem All You Need? | Letta</a></li>

</ul>
</details>

**Tags**: `#coding agents`, `#memory benchmark`, `#AI agents`, `#consistency`, `#evaluation`

---

<a id="item-11"></a>
## [AMD's GAIA open-source AI now integrates with Gmail](https://www.reddit.com/r/artificial/comments/1t77n9a/amds_local_opensource_ai_can_now_easily_interact/) ⭐️ 7.0/10

AMD's GAIA framework version 0.15 now includes Gmail integration via an agentic tool, enabling local AI to read and send emails while keeping data private. This enables privacy-preserving email automation on local hardware, reducing reliance on cloud AI and giving AMD's Ryzen AI PCs a unique selling point. GAIA is an open-source SDK for building AI PC agents, running large language models locally on the Ryzen AI NPU. The Gmail integration uses GAIA's agent framework to interact with the Gmail API while keeping all processing on-device.

rss · r/artificial RSS · May 8, 13:15

**Background**: GAIA is an open-source project by AMD designed to run large language models locally on Ryzen AI PCs using the Neural Processing Unit (NPU). Initially focused on LLM inference, GAIA evolved into an agent framework with tool-use capabilities. Version 0.15, released in January 2026 alongside CES announcements, added the Gmail integration as part of its improved agent user experience.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/amd-gaia">AMD GAIA</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/gaia-an-open-source-project-from-amd-for-running-local-llms-on-ryzen-ai.html">GAIA : An Open-Source Project from AMD for Running Local LLMs on...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#open-source`, `#AMD`, `#local AI`, `#email integration`

---

<a id="item-12"></a>
## [Asian AI Strategies: Vietnam's Law, Japan's No Penalties, Korea's Naver Exclusion](https://www.reddit.com/r/artificial/comments/1t7h9gt/compiled_every_national_ai_strategy_in_asia/) ⭐️ 7.0/10

A Reddit post compiles national AI strategies across Asia, highlighting Vietnam's standalone AI law (effective March 2026), Japan's AI Promotion Act without penalties, and Korea's exclusion of Naver from sovereign LLM competition for using Qwen weights. The post notes that most Asian governments take promotional approaches rather than punitive ones. This overview reveals a distinct Asian AI governance paradigm focused on incentives and sovereign capability rather than heavy regulation, which could influence global AI policy direction. The exclusion of Naver over Qwen weights highlights tensions between open-source models and national sovereignty in AI development. Vietnam's AI law has 36 articles with three-tier risk classification and fines up to 2% of annual revenue. Japan's act has no penalties and aims to close adoption gaps (only 9% of individuals use gen AI). China's open-source-as-industrial-policy has led to over 100,000 Qwen derivatives on Hugging Face.

rss · r/artificial RSS · May 8, 19:00

**Background**: Sovereign LLMs are national AI models built with domestic infrastructure to ensure strategic autonomy. Qwen is Alibaba's open-weight model family, which has been widely fine-tuned and adopted. The EU AI Act uses an ex-ante risk-based approach with penalties, contrasting with Asia's promotional stance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI Policy`, `#National AI Strategy`, `#Asia`, `#Regulation`, `#Open Source`

---

<a id="item-13"></a>
## [Qwen 35B-A3B MoE Runs Well on 12GB GPU](https://www.reddit.com/r/LocalLLaMA/comments/1t7l56a/qwen_35ba3b_is_very_usable_with_12gb_of_vram/) ⭐️ 7.0/10

A Reddit user shared detailed benchmarks showing that the Qwen 35B-A3B mixture-of-experts model (quantized to 4-bit IQ4_XS) runs practically on a 12GB RTX 3060, achieving about 914 tokens per second for prefill and 46.8 tokens per second for plain decoding, with support for 32k context. This demonstrates that large Mixture-of-Experts models with 35B total parameters can be run on consumer-grade GPUs with as little as 12GB VRAM, making high-quality local LLM inference more accessible for developers and enthusiasts without expensive hardware. The model uses IQ4_XS quantization and requires careful tuning of the `-ncmoe` parameter to keep enough MoE experts on GPU; the sweet spot was `-ncmoe 18` for safe decoding and `-ncmoe 20` for 32k context, with `-ctk q8_0 -ctv q8_0` KV cache quantization providing nearly free performance.

rss · r/LocalLLaMA RSS · May 8, 21:22

**Background**: Mixture-of-Experts (MoE) is a neural network architecture where only a subset of 'expert' sub-networks are activated per token, reducing computation. The Qwen 35B-A3B model has 35B total parameters but only about 3B active per token, making it efficient. Quantization reduces model size by using fewer bits per weight; IQ4_XS is a 4-bit format with importance matrices to maintain accuracy. llama.cpp is an inference engine that supports various quantization and offloading strategies, including the `-ncmoe` flag to control how many MoE layers are offloaded to GPU.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/issues/15263">Feature Request: --n-cpu-moe option for multi GPU? · Issue #15263 · ggml-org/llama.cpp</a></li>
<li><a href="https://huggingface.co/blog/Doctor-Shotgun/llamacpp-moe-offload-guide">Performant local mixture-of-experts CPU inference with GPU acceleration in llama.cpp</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#Qwen`, `#MoE`, `#VRAM`, `#local deployment`

---

<a id="item-14"></a>
## [AI2 Releases EMO: 1B/14B MoE with Document-Level Routing](https://www.reddit.com/r/LocalLLaMA/comments/1t7kgy4/new_moe_from_ai2_emo/) ⭐️ 7.0/10

AI2 has released EMO, a mixture-of-experts model with 1 billion active parameters and 14 billion total parameters, trained on 1 trillion tokens. It introduces document-level routing, where experts are clustered by domain (e.g., health, news) rather than by surface patterns. This work demonstrates a novel approach to expert specialization in MoE models, potentially improving efficiency and interpretability by grouping experts semantically. It could influence future MoE designs for large language models, especially in domain-specific applications. EMO uses a top-2 routing with a capacity factor, and the document-level routing operates by assigning entire documents to the same set of experts. The model is open-source and available on Hugging Face, with checkpoints and code.

rss · r/LocalLLaMA RSS · May 8, 20:57

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that uses multiple 'expert' sub-networks and a routing mechanism to activate only a subset of experts per input, allowing large model capacity with lower computational cost. Traditional MoE routing operates per token and often clusters experts around syntactic patterns. Document-level routing, as in EMO, aims to learn more semantic expert specializations by routing entire documents consistently.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoE`, `#AI2`, `#routing`, `#open-source`

---

<a id="item-15"></a>
## [DS4: Custom Inference Engine for DeepSeek 4 Flash on 128GB MacBooks](https://www.reddit.com/r/LocalLLaMA/comments/1t72tk9/ds4_a_deepseek_4_flash_specific_inference_engine/) ⭐️ 7.0/10

Antirez, creator of Redis, released DS4, an open-source inference engine specifically optimized to run DeepSeek V4 Flash on 128GB MacBooks with Apple Silicon. DS4 makes it practical to run a 284B-parameter MoE model locally on consumer hardware, democratizing access to large-scale AI and reducing reliance on cloud services. DeepSeek V4 Flash has 284B total parameters but only 13B activated per token, and supports a 1M-token context window. DS4 is tailored for the 128GB unified memory of high-end MacBooks, leveraging their CPU-GPU shared memory architecture.

rss · r/LocalLLaMA RSS · May 8, 09:26

**Background**: Large language models typically require high-end GPUs with ample VRAM, but models like DeepSeek V4 Flash use a Mixture-of-Experts (MoE) architecture to reduce active parameters. MacBooks with Apple Silicon use unified memory, allowing the CPU and GPU to access the same RAM pool, which is capable of holding large models entirely in memory. A specialized inference engine is needed to efficiently load and run the model on this architecture, as general-purpose frameworks may not fully exploit the hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek -V 4 - Flash · Hugging Face</a></li>
<li><a href="https://ollama.com/library/deepseek-v4-flash">deepseek -v 4 - flash</a></li>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-flash">deepseek -v 4 - flash Model by Deepseek -ai | NVIDIA NIM</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#DeepSeek`, `#Mac`, `#local AI`, `#open-source`

---