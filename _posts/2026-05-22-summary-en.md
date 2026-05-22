---
layout: default
title: "Horizon Summary: 2026-05-22 (EN)"
date: 2026-05-22
lang: en
---

> From 73 items, 16 important content pieces were selected

---

1. [OWASP's First Top 10 for AI Agents: 88% Hit by Incidents](#item-1) ⭐️ 9.0/10
2. [DeepSeek Secures $10.29B, Vows Open-Source AI Path](#item-2) ⭐️ 9.0/10
3. [Pydantic AI v2.0.0b2 Adds Message Queue, MCP Background Tasks](#item-3) ⭐️ 8.0/10
4. [Cleve Moler, Creator of MATLAB, Passes Away](#item-4) ⭐️ 8.0/10
5. [Datasette Agent: Conversational AI for SQLite Data Exploration](#item-5) ⭐️ 8.0/10
6. [LeCun's World Models & JEPA: Not an LLM Replacement](#item-6) ⭐️ 8.0/10
7. [Quantization Shootout on Qwen3-Coder-Next Reveals UD-Q5_K_M as Quality Winner](#item-7) ⭐️ 8.0/10
8. [Pydantic AI v1.101.0 adds MCP background tasks and XSearch subagent fallback](#item-8) ⭐️ 7.0/10
9. [AI Memory Demand Drives Up Consumer Electronics Prices](#item-9) ⭐️ 7.0/10
10. [Multi-Stream LLMs: Parallelizing Prompts, Thinking, I/O](#item-10) ⭐️ 7.0/10
11. [Waymo pauses Atlanta robotaxi service after flood incident](#item-11) ⭐️ 7.0/10
12. [Pentagon Shifts AI Strategy: From Anthropic to Multi-Vendor](#item-12) ⭐️ 7.0/10
13. [Anthropic's $10.9B Q2 Revenue Tops 2025, Outpaces Google and Meta Pre-IPO](#item-13) ⭐️ 7.0/10
14. [Qwen 3.7 Open-Weight Release Hailed as New King](#item-14) ⭐️ 7.0/10
15. [Mixed KV Cache Quantization in llama.cpp: CPU Fallback Issue and Fix](#item-15) ⭐️ 7.0/10
16. [llama.cpp b9274 Fixes MTP VRAM Leak](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OWASP's First Top 10 for AI Agents: 88% Hit by Incidents](https://www.reddit.com/r/artificial/comments/1tjy19a/owasp_published_its_first_top_10_for_ai_agents_88/) ⭐️ 9.0/10

OWASP released its first Top 10 for Agentic Applications in December 2025, a formal risk taxonomy for autonomous AI agents, citing that 88% of enterprises suffered AI agent security incidents in the past year. This is the first standardized security framework for autonomous agents, addressing a growing attack surface as agent adoption accelerates—88% of enterprises already affected, yet only 21% have runtime visibility. The taxonomy includes 10 risks such as Agent Goal Hijack, Tool Misuse, and Supply Chain Compromise, with real-world examples like poisoned MCP servers where 5.5% of public servers contain malicious tool descriptions achieving 84.2% attack success.

rss · r/artificial RSS · May 21, 21:10

**Background**: OWASP (Open Worldwide Application Security Project) is a nonprofit foundation that publishes widely-adopted security standards like the OWASP Top 10 for web applications. AI agents differ from chatbots by autonomously planning, using tools, maintaining memory, and acting without human permission. MCP (Model Context Protocol) is a protocol for connecting AI agents to external tools and data sources.

<details><summary>References</summary>
<ul>
<li><a href="https://jumpcloud.com/it-index/what-is-goal-hijacking">What Is Goal Hijacking? A Guide to ASI01 - JumpCloud</a></li>
<li><a href="https://www.crowdstrike.com/en-us/blog/ai-tool-poisoning/">AI Tool Poisoning: How Hidden Instructions Threaten AI Agents</a></li>

</ul>
</details>

**Tags**: `#OWASP`, `#AI Agents`, `#Security`, `#MCP`, `#Risk Taxonomy`

---

<a id="item-2"></a>
## [DeepSeek Secures $10.29B, Vows Open-Source AI Path](https://www.reddit.com/r/LocalLLaMA/comments/1tkfvvj/deepseek_is_pushing_forward_with_1029_billion/) ⭐️ 9.0/10

DeepSeek is pushing forward with a $10.29 billion financing round, and founder Liang Wenfeng has committed to continuing to develop open-source AI models rather than pursuing short-term commercialization goals. This massive financing round signals strong investor confidence in DeepSeek's open-source approach, which has already disrupted the AI industry by delivering high-performance models at a fraction of the cost of rivals. It reinforces the viability of open-source AI development as a strategic path toward AGI. The round is reportedly valued at $10.29 billion, and Liang Wenfeng has explicitly stated that the funds will be used to advance AGI research rather than near-term monetization. DeepSeek's models are released under open-source licenses like the MIT License, though training data is not openly licensed.

rss · r/LocalLLaMA RSS · May 22, 11:14

**Background**: DeepSeek, founded in July 2023 by Liang Wenfeng, is a Chinese AI company backed by hedge fund High-Flyer. It gained global attention in January 2025 with the release of DeepSeek-R1, a model that matched GPT-4 and o1 at a fraction of the training cost ($6 million vs. $100 million for GPT-4). The company's use of mixture-of-experts (MoE) and training on weaker export-restricted chips demonstrated cost-efficient innovation, triggering a 'Sputnik moment' for US AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://www.deepseek.com/en/">DeepSeek</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Open-Source`, `#AI Financing`, `#LLM`, `#AGI`

---

<a id="item-3"></a>
## [Pydantic AI v2.0.0b2 Adds Message Queue, MCP Background Tasks](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b2) ⭐️ 8.0/10

Pydantic AI released v2.0.0b2 with three major features: a pending message queue via ctx.enqueue/agent_run.enqueue, support for MCP background tasks per SEP-1686, and a model-agnostic XSearch capability using subagent fallback. The release also adds top_k model settings for Google, Anthropic, and Cohere models, along with several bug fixes. These features significantly enhance Pydantic AI's orchestration capabilities, enabling asynchronous message handling, long-running MCP tool execution without blocking, and flexible search across different LLM providers. This positions Pydantic AI as a more robust framework for building complex agent systems that require reliable background processing and model-agnostic tool use. The pending message queue allows agents to enqueue messages for later processing, useful for asynchronous workflows. MCP background tasks enable tools to run in the background with progress tracking, adhering to the SEP-1686 specification. The XSearch capability uses a subagent fallback mechanism to make search model-agnostic when the primary model lacks search functionality.

github · DouweM · May 22, 05:08

**Background**: Pydantic AI is a Python agent framework that integrates with various LLM providers and tools. MCP (Model Context Protocol) is an open protocol for connecting AI agents to external tools and data sources. The subagent fallback pattern allows an agent to delegate tasks to a secondary model when the primary model cannot perform a specific capability.

<details><summary>References</summary>
<ul>
<li><a href="https://pydantic.dev/docs/ai/api/pydantic-ai/mcp/">pydantic_ai.mcp | Pydantic Docs</a></li>
<li><a href="https://github.com/pydantic/pydantic-ai/issues/4266">FastMCPToolset: add support for MCP background tasks (SEP-1686) · Issue #4266 · pydantic/pydantic-ai</a></li>
<li><a href="https://ai.pydantic.dev/mcp/">Overview | Pydantic Docs</a></li>

</ul>
</details>

**Tags**: `#pydantic-ai`, `#agent-framework`, `#MCP`, `#orchestration`, `#release`

---

<a id="item-4"></a>
## [Cleve Moler, Creator of MATLAB, Passes Away](https://www.mathworks.com/company/aboutus/founders/clevemoler.html) ⭐️ 8.0/10

Cleve Moler, the creator of MATLAB and co-founder of MathWorks, has passed away, prompting an outpouring of tributes from the scientific computing community. Moler's creation of MATLAB revolutionized numerical computing and data analysis, becoming an essential tool in academia and industry; his loss marks the end of an era for a pioneer whose work shaped modern scientific computing. Moler originally wrote MATLAB as a simple interface to the LINPACK and EISPACK Fortran libraries, consisting of about 2,000 lines of Fortran code, to help his students avoid compiling Fortran programs.

hackernews · mychele · May 22, 02:35 · [Discussion](https://news.ycombinator.com/item?id=48231319)

**Background**: Cleve Moler was an American mathematician and computer scientist specializing in numerical analysis. He co-authored the LINPACK and EISPACK Fortran libraries in the 1970s, and later created MATLAB to make these libraries accessible. In 1984, he co-founded MathWorks with Jack Little to commercialize MATLAB.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cleve_Moler">Cleve Moler</a></li>

</ul>
</details>

**Discussion**: Community comments recall Moler as a friendly, approachable mentor and a pioneer; one notes his influence on open-source ecosystems like NumPy/SciPy, while another points to his creation of canonical Fortran libraries and the original MATLAB's simplicity.

**Tags**: `#MATLAB`, `#numerical computing`, `#scientific computing`, `#community tribute`, `#pioneer`

---

<a id="item-5"></a>
## [Datasette Agent: Conversational AI for SQLite Data Exploration](https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything) ⭐️ 8.0/10

Simon Willison announced the first release of Datasette Agent, an extensible AI assistant that provides a conversational interface for querying and charting data stored in Datasette (SQLite databases). It can be extended with plugins such as datasette-agent-charts for chart generation using Observable Plot. Datasette Agent integrates LLMs directly into Datasette, making data exploration accessible to non-technical users via natural language queries. It demonstrates the power of combining AI agents with open-source data tools, potentially lowering the barrier for data analysis. The live demo runs on Gemini 3.1 Flash-Lite, which is cheap and fast for writing SQLite queries. The agent can generate SQL queries from natural language questions, as shown in the demo where it answered 'when did Simon most recently see a pelican?' by querying a blog database. Plugin support allows adding tools like charting and image generation.

rss · Simon Willison · May 21, 19:52

**Background**: Datasette is an open-source tool for exploring and publishing data stored in SQLite databases, created by Simon Willison. LLM is his Python library for interacting with large language models. Datasette Agent combines these two projects, allowing users to interact with Datasette through a conversational interface powered by LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help explore and analyze data in SQLite</a></li>
<li><a href="https://simonwillison.net/2026/May/21/datasette-agent/">Datasette Agent</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#Datasette`, `#LLM`, `#Data Exploration`, `#Open Source`

---

<a id="item-6"></a>
## [LeCun's World Models & JEPA: Not an LLM Replacement](https://www.reddit.com/r/artificial/comments/1tjuats/so_what_is_yann_lecuns_world_models_and_jepa_and/) ⭐️ 8.0/10

A Reddit post analyzes Yann LeCun's LeWorldModel (LeWM) and Joint-Embedding Predictive Architecture (JEPA), arguing that JEPA is designed for visual processing in robotics and autonomous driving, not as a replacement for large language models. This discussion clarifies misconceptions about LeCun's work, positioning JEPA as a specialized architecture for physical AI rather than a general-purpose language model, which could influence future AI research directions. LeWorldModel is the first JEPA that trains stably end-to-end from raw pixels using only two loss terms, and its 15 million parameters are optimized for pixel-based prediction, not language.

rss · r/artificial RSS · May 21, 18:59

**Background**: World models are AI systems that learn internal representations of environments to simulate dynamics and enable planning. JEPA (Joint-Embedding Predictive Architecture) is a self-supervised learning approach that predicts representations of image regions in an abstract space, avoiding pixel-level generation. LeWorldModel implements JEPA for vision-based tasks like robotics and autonomous driving, contrasting with LLMs like GPT-4 that process text.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2301.08243">[2301.08243] Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>

</ul>
</details>

**Tags**: `#world models`, `#JEPA`, `#Yann LeCun`, `#AI research`, `#LLM alternatives`

---

<a id="item-7"></a>
## [Quantization Shootout on Qwen3-Coder-Next Reveals UD-Q5_K_M as Quality Winner](https://www.reddit.com/r/LocalLLaMA/comments/1tkmjmq/i_ran_a_quantization_shootout_on_qwen3coder_and/) ⭐️ 8.0/10

A user tested four quantization formats on Qwen3-Coder-Next using llama.cpp and found that UD-Q5_K_M achieved the highest same top-1 accuracy (94%) and lowest KL divergence, outperforming MXFP4, Q4_K_M, and Q5_K_M. This comparison provides practical guidance for deploying Qwen3-Coder locally, showing that moderate quantization (UD-Q5_K_M) can retain quality nearly on par with full precision while still being memory-efficient. It also highlights the importance of token accuracy compounding over long outputs, especially for coding tasks. The user ran the test using llama.cpp Vulkan on 3x Radeon PRO 9700 GPUs (96 GB VRAM) with wikitext-2 evaluation (512 context). UD-Q5_K_M was only ~10 GB larger than MXFP4 but showed significantly better quality metrics; decode speed of UD-Q5_K_M was within 9% of Q4_K_M despite being 22% larger.

rss · r/LocalLLaMA RSS · May 22, 15:35

**Background**: Quantization reduces model size and speeds up inference by storing weights in lower precision. Qwen3-Coder-Next is an open-weight coding model from Alibaba's Qwen team, optimized for agentic coding workflows. Unsloth is a library for efficient fine-tuning and quantization, and MXFP4 is a 4-bit format designed for mixture-of-experts (MoE) models. The 'UD' prefix in UD-Q5_K_M likely stands for Unsloth Dynamic precision, an approach that dynamically adjusts quantization for better fidelity.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3-Coder-Next">Qwen/ Qwen 3 - Coder - Next · Hugging Face</a></li>
<li><a href="https://unsloth.ai/">Unsloth - Train and Run Models Locally</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/quantization/">Quantization - vLLM</a></li>

</ul>
</details>

**Tags**: `#quantization`, `#LLM inference`, `#Qwen`, `#llama.cpp`, `#open-source models`

---

<a id="item-8"></a>
## [Pydantic AI v1.101.0 adds MCP background tasks and XSearch subagent fallback](https://github.com/pydantic/pydantic-ai/releases/tag/v1.101.0) ⭐️ 7.0/10

Pydantic AI v1.101.0 introduces a pending message queue via ctx.enqueue/agent_run.enqueue, support for MCP background tasks, model-agnostic XSearch subagent fallback, and top_k model settings for GoogleModel, AnthropicModel, and CohereModel. These enhancements significantly improve pydantic-ai's capabilities for building complex AI agents, particularly through MCP background tasks that enable asynchronous tool execution and model-agnostic search fallback. This strengthens the framework's position in the AI agent ecosystem and promotes broader MCP adoption. MCP background tasks allow tools marked with TaskConfig(mode="optional") to run asynchronously while the agent continues processing. The XSearch subagent fallback makes the search capability work with any LLM, not just specific models. top_k support is now available in three model providers.

github · DouweM · May 22, 04:49

**Background**: MCP (Model Context Protocol) is a standard for connecting AI models with external tools and data, enabling rich integrations. Pydantic-ai is a framework for building AI agents with type-safe tool definitions and model-agnostic execution. Subagents are specialized AI agents for specific tasks, and a pending message queue allows asynchronous message delivery to agent sessions.

<details><summary>References</summary>
<ul>
<li><a href="https://pydantic.dev/docs/ai/api/pydantic-ai/mcp/">pydantic_ai.mcp | Pydantic Docs</a></li>
<li><a href="https://ai.pydantic.dev/message-history/">Messages and chat history | Pydantic Docs</a></li>

</ul>
</details>

**Tags**: `#pydantic-ai`, `#MCP`, `#AI agents`, `#release notes`

---

<a id="item-9"></a>
## [AI Memory Demand Drives Up Consumer Electronics Prices](https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone) ⭐️ 7.0/10

The article explains that surging demand for High Bandwidth Memory (HBM) used in AI GPUs is diverting wafer capacity away from DDR and LPDDR production, causing a DRAM shortage that raises prices for consumer electronics like smartphones and laptops. This trend reverses years of declining memory prices, making budget smartphones and laptops more expensive and potentially slowing adoption of affordable devices. It also highlights how AI infrastructure investments indirectly affect everyday consumers. Building a state-of-the-art DRAM fab costs $15-20 billion, plus billions for equipment, and takes years to reach acceptable yields. Modern DRAM manufacturing is extraordinarily complex, and silicon wafers allocated to HBM cannot be used for DDR or LPDDR, creating a supply squeeze.

hackernews · d0ks · May 21, 21:55 · [Discussion](https://news.ycombinator.com/item?id=48229319)

**Background**: DRAM (Dynamic Random-Access Memory) is the main memory used in computers and smartphones, with variants like DDR (high bandwidth) for laptops and LPDDR (low power) for mobiles. HBM is a 3D-stacked memory interface offering extremely high bandwidth, essential for AI training on large GPU clusters. Both types are manufactured on the same silicon wafers, so increased HBM production reduces capacity for other DRAM types.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_random-access_memory">Dynamic random-access memory - Wikipedia</a></li>
<li><a href="https://www.rambus.com/blogs/hbm3-everything-you-need-to-know/">High Bandwidth Memory ( HBM ): Everything You Need to... - Rambus</a></li>

</ul>
</details>

**Discussion**: Commenters praised the article for its deep explanation of the memory market dynamics. One user shared a tweet describing the DRAM crunch as resulting from speculative purchasing of future memory for GPUs that don't exist yet. Another highlighted the surprising cost and complexity of building DRAM fabs. A technical user explained the difference between DDR and LPDDR in terms of voltage and bandwidth needs.

**Tags**: `#AI infrastructure`, `#memory shortage`, `#DRAM`, `#HBM`, `#hardware pricing`

---

<a id="item-10"></a>
## [Multi-Stream LLMs: Parallelizing Prompts, Thinking, I/O](https://arxiv.org/abs/2605.12460) ⭐️ 7.0/10

A new arXiv paper (2505.12460) proposes Multi-Stream LLMs, an architecture that separates prompts, thinking, and I/O into parallel streams processed simultaneously in a single forward pass. This could significantly reduce latency and improve throughput for LLM-based agents by enabling parallel tool calls, thinking steps, and output generation, but trade-offs exist between speed and output quality. The architecture uses multiple I/O streams where each step is one forward pass generating tokens across all output channels in parallel, rather than the traditional single-stream autoregressive generation.

hackernews · atomicthumbs · May 21, 19:37 · [Discussion](https://news.ycombinator.com/item?id=48227923)

**Background**: Traditional LLMs generate tokens autoregressively, one at a time, which limits parallelism. Multi-stream architectures allow overlapping computation and I/O, similar to how operating systems use threads for concurrency. This paper explores applying that concept to LLM inference.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.12460">Multi - Stream LLMs: Unblocking Language Models with Parallel...</a></li>
<li><a href="https://www.emergentmind.com/topics/multistream-language-model-architecture">Multistream Language Model Architecture</a></li>
<li><a href="https://github.com/RichardMinsooGo/LLM_multistream-transformers">GitHub - RichardMinsooGo/ LLM _ multistream -transformers...</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some praise the idea for enabling dynamic parallel tool calls and timing awareness, while others report that disabling parallel tool calls improved output quality in their own systems, preferring serialized execution for correctness.

**Tags**: `#LLM`, `#parallelism`, `#research paper`, `#multi-stream`, `#AI architecture`

---

<a id="item-11"></a>
## [Waymo pauses Atlanta robotaxi service after flood incident](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/) ⭐️ 7.0/10

Waymo has paused its robotaxi service in Atlanta after one of its autonomous vehicles became stuck in unexpected flash flooding. The incident occurred during a sudden heavy rainstorm that caused rapid flooding on roads. This event underscores the difficulty autonomous vehicles still face in handling rare and unpredictable edge cases like flash floods. It highlights a key limitation in current AI-driven systems that could affect public trust and regulatory decisions for robotaxi expansion. Only one Waymo vehicle was affected, and the flash flood was unexpected—3-4 inches of rain in 30 minutes with warnings issued after flooding occurred. Waymo paused service likely to review and improve its handling of such weather events.

hackernews · mattas · May 21, 16:30 · [Discussion](https://news.ycombinator.com/item?id=48225426)

**Background**: Waymo is a leading autonomous driving company, operating robotaxi services in several US cities. Autonomous vehicles rely on sensors and AI to navigate, but they can struggle with unusual conditions not well represented in training data. Flash floods are a challenging edge case because they can appear suddenly and alter road conditions rapidly.

**Discussion**: Community comments show mixed views. Some see the incident as a normal part of deployment learning (dhbradshaw), while others express broader concerns about AI's inability to handle edge cases (etempleton). A commenter notes that the event was caused by exceptionally rare weather (DannyBee), and another quips that the car achieved 'human-level intelligence' by driving into floodwater (paxys).

**Tags**: `#autonomous-vehicles`, `#waymo`, `#AI-safety`, `#edge-cases`, `#robotaxi`

---

<a id="item-12"></a>
## [Pentagon Shifts AI Strategy: From Anthropic to Multi-Vendor](https://www.reddit.com/r/artificial/comments/1tjy1it/ai_models/) ⭐️ 7.0/10

The Pentagon is actively evaluating frontier AI models from OpenAI and Google Gemini across military commands, moving away from heavy reliance on Anthropic's Claude after contract disputes over 'lawful operational use' terms that could permit mass surveillance or autonomous weapons. This shift to a multi-vendor AI strategy improves resilience and bargaining power for the Pentagon, but also reveals growing tension between commercial AI safety policies and national security priorities, with OpenAI and Google emerging as main beneficiaries. Anthropic was designated a 'supply-chain risk' after negotiations collapsed; the Pentagon is now testing how models from OpenAI, Google, Microsoft, AWS, NVIDIA, and xAI respond differently to identical prompts in high-stakes military workflows.

rss · r/artificial RSS · May 21, 21:10

**Background**: Frontier AI models are general-purpose models trained with enormous computational resources, capable of exceeding state-of-the-art across multiple domains. A 'supply-chain risk' designation in military procurement blocks contracts and causes reputational damage, as seen in the Pentagon's decision against Anthropic.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>
<li><a href="https://www.techbuzz.ai/articles/big-tech-lobby-pushes-back-on-anthropic-supply-chain-label">Big Tech Lobby Pushes Back on Anthropic Supply Chain Label</a></li>

</ul>
</details>

**Tags**: `#AI models`, `#military`, `#Pentagon`, `#OpenAI`, `#Google Gemini`

---

<a id="item-13"></a>
## [Anthropic's $10.9B Q2 Revenue Tops 2025, Outpaces Google and Meta Pre-IPO](https://www.reddit.com/r/artificial/comments/1tjr61r/anthropics_109b_q2_tops_2025_and_grows_faster/) ⭐️ 7.0/10

Anthropic reported $10.9 billion in Q2 2025 revenue, surpassing its previous highs and growing faster than Google and Meta did before their IPOs. This milestone underscores Anthropic's rapid ascent in the AI industry, signaling strong commercial adoption of its models and potentially reshaping the competitive landscape alongside OpenAI and others. The revenue figure marks a significant leap from prior quarters, and the company is reportedly on track to achieve its first profit in 2026.

rss · r/artificial RSS · May 21, 17:15

**Background**: Anthropic is a leading AI company founded by former OpenAI employees, known for developing the Claude series of large language models. Pre-IPO growth rates for Google and Meta are often cited benchmarks for tech startups, as those companies achieved dominant market positions before going public.

**Tags**: `#Anthropic`, `#AI Industry`, `#Revenue Growth`, `#Valuation`

---

<a id="item-14"></a>
## [Qwen 3.7 Open-Weight Release Hailed as New King](https://www.reddit.com/r/LocalLLaMA/comments/1tjvz6l/waiting_for_qwen_37_open_weight_the_new_king_has/) ⭐️ 7.0/10

A Reddit post on r/LocalLLaMA announces the upcoming release of Qwen 3.7 open-weight model, hyping it as the new king of open-source LLMs. The release of Qwen 3.7 open-weight could significantly impact the open-source LLM ecosystem, providing a powerful alternative to other open models. The post does not provide specific technical details but links to the Qwen blog for more information. Qwen models are developed by Alibaba Cloud and often released under the Apache 2.0 license.

rss · r/LocalLLaMA RSS · May 21, 19:56

**Background**: Qwen is a family of large language models from Alibaba Cloud, many of which are open-source. Open-weight models make the trained parameters available, allowing community usage and fine-tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Qwen`, `#LLM`, `#Open-source`, `#Model Release`, `#LocalLLaMA`

---

<a id="item-15"></a>
## [Mixed KV Cache Quantization in llama.cpp: CPU Fallback Issue and Fix](https://www.reddit.com/r/LocalLLaMA/comments/1tkih6y/llamacpp_asymmetric_kv_q8q4_cache_current_caveats/) ⭐️ 7.0/10

A Reddit post highlights that using asymmetric KV cache quantization (e.g., -ctk q8_0 -ctv q4_0) in llama.cpp causes prompt processing to fall back to CPU instead of GPU. A GitHub discussion proposes a fix that compiles the KV cache quantization combo without requiring the full FA_ALL_QUANTS flag, and shows that this mixed quantization costs only 1.3% precision loss while saving more than half the memory compared to f16. This is significant because many users attempt to use mixed KV cache quantization to reduce memory usage without realizing it causes a severe performance penalty (CPU fallback). The proposed fix could unlock substantial memory savings (over 50%) with minimal accuracy loss (1.3%), making large language model inference more efficient on consumer GPUs. The CPU fallback occurs for all asymmetric combinations like q8_0 key / q4_0 value. The GitHub user sanmai suggests including the specific KV cache quantization combo during compilation as a simpler alternative to the cmake flag GGML_CUDA_FA_ALL_QUANTS, which takes very long. The eval confirms 1.3% precision loss for the q8/q4 mix compared to f16, while memory usage drops from ~1030MB per concurrency (fp16) to significantly less.

rss · r/LocalLLaMA RSS · May 22, 13:07

**Background**: llama.cpp is an open-source software library for performing inference on large language models, co-developed with the GGML tensor library. KV cache quantization reduces memory usage by storing the key-value cache in lower precision (e.g., q8_0, q4_0) instead of float16. Asymmetric quantization uses different precisions for keys and values, which can save more memory but requires careful implementation to avoid performance degradation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Reddit post and GitHub discussion express relief that a fix is being explored, with users confirming the CPU fallback issue. Some commenters note that the 1.3% precision loss is acceptable for the memory gains, while others ask about support for other GPU backends beyond CUDA. The discussion is constructive and focused on technical details.

**Tags**: `#llama.cpp`, `#KV cache quantization`, `#GPU optimization`, `#LLM inference`

---

<a id="item-16"></a>
## [llama.cpp b9274 Fixes MTP VRAM Leak](https://www.reddit.com/r/LocalLLaMA/comments/1tk0grd/latest_b9274_addresses_mtp_vram_leak/) ⭐️ 7.0/10

Release b9274 of llama.cpp fixes a VRAM leak in multi-token prediction (MTP) models that occurred during sleep/resume cycles in the server. The patch ensures that the draft model, draft context, and speculative decoder resources are properly freed. This fix prevents out-of-memory crashes for users running MTP models in llama.cpp, improving the stability and reliability of long-running inference servers. It is especially important for applications that rely on speculative decoding for faster generation. The memory leak was caused by the destroy() function in server_context_impl only cleaning the main model and context, but not the speculative decoder (spec), draft context (ctx_dft), or draft model (model_dft). The fix explicitly resets these resources in the correct order to avoid use-after-free errors.

rss · r/LocalLLaMA RSS · May 21, 22:43

**Background**: Multi-Token Prediction (MTP) is a technique where a language model predicts multiple future tokens from each position, improving sample efficiency. Speculative decoding accelerates inference by using a smaller draft model to propose tokens that a larger model verifies. llama.cpp is an open-source C++ implementation for running LLMs efficiently on consumer hardware, supporting both MTP and speculative decoding.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Multi-token_prediction">Multi-token prediction</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog</a></li>

</ul>
</details>

**Discussion**: The original poster noted that while they observed VRAM creep, they were not sure if this fix addresses their separate issue of MTP models unloading after a few minutes. The discussion is limited to this single comment expressing cautious optimism.

**Tags**: `#llama.cpp`, `#MTP`, `#VRAM leak`, `#LLM inference`, `#bug fix`

---