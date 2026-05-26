---
layout: default
title: "Horizon Summary: 2026-05-26 (EN)"
date: 2026-05-26
lang: en
---

> From 70 items, 13 important content pieces were selected

---

1. [AI solves 80-year-old math conjecture for under $1000](#item-1) ⭐️ 9.0/10
2. [Using AI to Write Better Code More Slowly](#item-2) ⭐️ 8.0/10
3. [LocalAI + Outsourcing to Beat Frontier Labs on Cost](#item-3) ⭐️ 8.0/10
4. [Microsoft Copilot Cowork Vulnerable to Prompt Injection Data Exfiltration](#item-4) ⭐️ 8.0/10
5. [SkillOpt Treats Markdown Skills as Trainable Parameters](#item-5) ⭐️ 8.0/10
6. [Harbor v0.4.19 launches local agentic coding tools](#item-6) ⭐️ 8.0/10
7. [Uber president says AI spending is getting 'harder to justify'](#item-7) ⭐️ 7.0/10
8. [Norway's 2PB Huawei flash storage for sovereign LLM sparks debate](#item-8) ⭐️ 7.0/10
9. [Human Archive pays Indian gig workers to train robots](#item-9) ⭐️ 7.0/10
10. [Memory Curator Agent Governance Layer for Multi-Agent Memory](#item-10) ⭐️ 7.0/10
11. [China Restricts Overseas Travel for AI Talent at Alibaba, DeepSeek](#item-11) ⭐️ 7.0/10
12. [Together AI Open-Sources OSCAR: 2-bit KV Cache Quantization](#item-12) ⭐️ 7.0/10
13. [Kwai Keye-VL-2.0-30B-A3B: First Multimodal Model with DSA Attention](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI solves 80-year-old math conjecture for under $1000](https://www.reddit.com/r/artificial/comments/1to657g/ai_solves_80yearold_math_conjecture_for_under_1000/) ⭐️ 9.0/10

OpenAI's GPT-next model has solved the Erdős unit distance problem, an open conjecture in combinatorics since 1946, for less than $1,000 in compute costs. This demonstrates that frontier AI models can function as independent mathematical discoverers rather than just tools, potentially accelerating the rate of scientific breakthroughs and challenging traditional notions of research. The problem's solution was achieved through chain-of-thought reasoning and test-time compute scaling, as detailed in Lilian Weng's recent deep dive, and the total compute cost was lower than a typical mid-tier SaaS subscription.

rss · r/artificial RSS · May 26, 12:56

**Background**: The Erdős unit distance problem, posed by Paul Erdős in 1946, asks for the maximum number of unit-distance pairs among n points in the Euclidean plane. It is a central problem in geometric graph theory and had resisted progress for eight decades. Chain-of-thought reasoning is a prompt engineering technique that elicits step-by-step reasoning in large language models, enabling them to tackle complex multistep problems by generating intermediate inference chains.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chain-of-thought_reasoning">Chain-of-thought reasoning</a></li>
<li><a href="https://arxiv.org/abs/2201.11903">[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models</a></li>

</ul>
</details>

**Tags**: `#AI reasoning`, `#LLM breakthroughs`, `#math conjecture`, `#chain-of-thought`, `#test-time compute`

---

<a id="item-2"></a>
## [Using AI to Write Better Code More Slowly](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) ⭐️ 8.0/10

Nolan Lawson published an article arguing that deliberately using AI for iterative code review and design discussions, rather than just generating code fast, leads to higher quality software even if it takes more time. This challenges the prevailing 'move fast' culture in AI-assisted development, suggesting that quality-focused, slower workflows may produce more robust and maintainable code. It resonates with developers seeking a deliberate approach to integrating AI into their processes. The article emphasizes using AI for code review and architectural design in a back-and-forth, iterative manner, often involving multiple models (e.g., Claude for implementation, GPT for review). It highlights that this process can catch more edge cases and improve overall code quality.

hackernews · signa11 · May 25, 23:16 · [Discussion](https://news.ycombinator.com/item?id=48272984)

**Background**: AI code review tools have grown rapidly, with the market reaching over $4 billion in 2025. Many developers use AI for quick code generation, but a slower, more deliberate approach—iterating with AI on design and review—is emerging as a best practice for quality. The concept is sometimes called 'deliberate AI-assisted development' or 'vibe coding' with careful oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/">A practical guide to building agents - OpenAI</a></li>
<li><a href="https://aipxperts.com/blog/what-is-ai-agent-development-a-complete-technical-guide/">What is AI Agent Development? A Complete Technical Guide</a></li>
<li><a href="https://zylos.ai/research/2026-02-17-multi-model-ai-code-review">Multi-Model AI Code Review: Iterative Quality Assurance Through Cross-Model Collaboration | Zylos Research</a></li>

</ul>
</details>

**Discussion**: The community discussion is generally positive, with juniors and seniors sharing experiences of long back-and-forth sessions that improve architectural decisions and catch corner cases. Some commenters note that this approach can be slower than writing code manually, but they value the resulting quality. A few express concerns about losing micro-architectural intuition when relying heavily on AI agents.

**Tags**: `#AI agents`, `#code review`, `#LLM`, `#developer tools`, `#programming`

---

<a id="item-3"></a>
## [LocalAI + Outsourcing to Beat Frontier Labs on Cost](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/) ⭐️ 8.0/10

A blog post argues that combining local AI models (e.g., LocalAI) with outsourcing will soon be more economical than using frontier API labs like OpenAI or Anthropic, sparking debate on pricing and model quality. This matters because it challenges the current reliance on expensive frontier APIs, potentially reshaping how companies deploy AI for development tasks, especially with the rise of agentic AI and cost-sensitive enterprises. Community comments highlight that subscription pricing is 10x-40x cheaper than API equivalents, but local models like Qwen or Gemma still lag behind frontier models in quality for complex coding tasks.

hackernews · GodelNumbering · May 26, 12:08 · [Discussion](https://news.ycombinator.com/item?id=48278610)

**Background**: LocalAI is an open-source, drop-in replacement for the OpenAI API that allows running LLMs and other AI models locally on consumer hardware, without requiring a GPU. Frontier labs refer to companies like OpenAI and Anthropic that offer powerful models via cloud APIs at a per-token cost. The debate centers on whether the cost savings of local models plus outsourcing can offset the higher quality of frontier models for software development.

<details><summary>References</summary>
<ul>
<li><a href="https://localai.io/">LocalAI</a></li>
<li><a href="https://github.com/mudler/LocalAI">GitHub - mudler/LocalAI: LocalAI is the open-source AI engine ... LocalAI Tutorial: The Complete Guide to Running AI Locally mudler/LocalAI | DeepWiki What Is Local AI and When Should It Be Used ~ Plugable ... The Ultimate Guide to Local AI and AI Agents: Building ... LocalAI:Open source AI stack enabling local execution of ...</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some note that subscription pricing is far cheaper than API usage, while others argue that local models still lack the quality of frontier models for real tasks. One comment compares working with LLMs to offshore development—productive when guided, but prone to errors when left unsupervised. Another mentions that companies are already replacing offshore teams with US programmers plus AI.

**Tags**: `#AI economics`, `#LocalAI`, `#LLM outsourcing`, `#developer productivity`, `#agentic AI`

---

<a id="item-4"></a>
## [Microsoft Copilot Cowork Vulnerable to Prompt Injection Data Exfiltration](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

Security researchers demonstrated that Microsoft Copilot Cowork agents can be tricked via prompt injection to send emails containing external images, which exfiltrate data when the user views the email. This highlights a critical security flaw in agentic systems that can automate email sending, and shows that prompt injection remains a severe threat to AI agents with access to sensitive data. The attack exploits that Cowork agents can send emails to the user's own inbox without approval, and those messages can contain external images that trigger network requests. Additionally, OneDrive pre-authenticated download links can be leaked to attackers.

rss · Simon Willison · May 26, 15:36

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs cause language models to behave unintendedly. Microsoft Copilot Cowork is an AI agent that automates tasks across Microsoft 365, such as sending emails or scheduling meetings. The vulnerability demonstrates the challenge of securing agentic systems against injection attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft 365 Blog</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack? | IBM</a></li>

</ul>
</details>

**Tags**: `#security`, `#prompt injection`, `#data exfiltration`, `#AI agents`, `#Microsoft Copilot`

---

<a id="item-5"></a>
## [SkillOpt Treats Markdown Skills as Trainable Parameters](https://www.reddit.com/r/LocalLLaMA/comments/1to1mey/skillopt_treats_markdown_skill_files_as_trainable/) ⭐️ 8.0/10

Microsoft Research's SkillOpt introduces a method to optimize markdown skill files for AI agents by using a frontier model to propose bounded edits gated by a held-out validation set. Only edits that strictly improve performance are accepted, treating the skill document as trainable state. This formalizes a common ad-hoc practice in agent development, providing a principled optimization framework that improves performance and enables cross-model skill transfer. It allows smaller models with optimized skills to match frontier model performance on procedural benchmarks, reducing reliance on large-scale fine-tuning. Optimal skills converge with 1 to 4 accepted edits out of many proposals, with an edit budget of 4 to 8 per step; removing the cap causes performance collapse. The median final skill length is ~920 tokens, and a skill optimized on Codex transferred to Claude Code with zero modification, gaining +59.7 on SpreadsheetBench.

rss · r/LocalLLaMA RSS · May 26, 09:20

**Background**: Many AI agent frameworks use markdown skill files (e.g., SKILL.md) to define agent behavior, but these are typically hand-crafted. SkillOpt treats the skill document as external trainable state while keeping the target model frozen, applying optimization through execution feedback and bounded textual edits. Frontier models are the most advanced general-purpose AI models that exhibit emergent capabilities, used here to propose skill modifications.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.github.io/SkillOpt/">SkillOpt | Executive Strategy for Self-Evolving Agent Skills</a></li>
<li><a href="https://huggingface.co/papers/2605.23904">Paper page - SkillOpt: Executive Strategy for Self-Evolving Agent Skills</a></li>
<li><a href="https://mer.vin/2026/05/skillopt-explained-train-agent-skill-md-files-with-validation-gates-not-hope/">SkillOpt Explained: Train Agent SKILL.md Files With ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#skill optimization`, `#LLM`, `#agentic frameworks`, `#markdown`

---

<a id="item-6"></a>
## [Harbor v0.4.19 launches local agentic coding tools](https://www.reddit.com/r/LocalLLaMA/comments/1to8t53/harbor_v0419_vllmsglangllamacpp_launch/) ⭐️ 8.0/10

Harbor v0.4.19 now supports launching agentic coding tools such as codex, Claude, Pi, and opencode using local inference backends like vLLM, SGLang, and llama.cpp, all with a simple harbor launch command. This release simplifies the setup of local AI agent development environments, enabling developers to run agentic coding tools fully offline with local models, reducing dependency on cloud APIs and enhancing privacy. The launch command can proxy requests through an optimizing LLM gateway that automatically injects and resolves tools like web search; for example, adding --web enables web search for an agent, and Harbor pre-wires everything.

rss · r/LocalLLaMA RSS · May 26, 14:34

**Background**: Harbor is a CLI and companion app for managing a local LLM stack, including backends (Ollama, vLLM, SGLang, llama.cpp), frontends, and services like web search and voice chat. Agentic coding tools are AI assistants that can autonomously write and debug code, typically powered by cloud APIs; Harbor now lets them run locally. vLLM, SGLang, and llama.cpp are high-performance inference engines for serving LLMs on local hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/av/harbor">GitHub - av/harbor: Stop configuring your AI stack. Start ...</a></li>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance ...</a></li>
<li><a href="https://pypi.org/project/llm-harbor/">llm-harbor · PyPI</a></li>

</ul>
</details>

**Tags**: `#Harbor`, `#vLLM`, `#agentic coding tools`, `#local LLM inference`, `#developer tools`

---

<a id="item-7"></a>
## [Uber president says AI spending is getting 'harder to justify'](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify) ⭐️ 7.0/10

Uber President Dara Khosrowshahi stated that justifying AI spending is becoming increasingly difficult, sparking debate on the return on investment from AI coding tools and large language models. This skepticism from a major tech leader highlights growing concerns about AI investment bubbles and the actual productivity gains from AI tools, potentially influencing corporate spending decisions across the industry. Khosrowshahi's remarks come amid reports of massive token burn by companies using AI coding assistants, with critics questioning the measurable impact on quarterly results compared to the cloud computing boom.

hackernews · berlianta · May 26, 10:01 · [Discussion](https://news.ycombinator.com/item?id=48277485)

**Background**: Large language models (LLMs) like GPT-4 and Claude are marketed as productivity boosters for developers, but their operational costs are high due to compute requirements. The concept of 'token economics' examines the pricing and usage patterns of these models, while surveys show mixed adoption and satisfaction among developers.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/">Which AI Coding Tools Do Developers Actually Use at Work?</a></li>
<li><a href="https://cowles.yale.edu/sites/default/files/2025-02/d2425.pdf">THE ECONOMICS OF LARGE LANGUAGE MODELS: TOKEN ALLOCATION ...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed skepticism about AI coding tools' ROI, with one noting that in large organizations, code production is rarely the bottleneck. Others compared the current AI spending frenzy to early cloud adoption, but argued that AI's impact on creating new software categories is far less clear.

**Tags**: `#AI investment`, `#Industry News`, `#Developer Productivity`, `#LLM economics`

---

<a id="item-8"></a>
## [Norway's 2PB Huawei flash storage for sovereign LLM sparks debate](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910) ⭐️ 7.0/10

Norway's National Library has deployed 2 petabytes of Huawei flash storage to train a sovereign large language model (LLM) for the Norwegian language, as announced by IT Platform Head Marius Husnes at Huawei's ID Forum 2026 in Paris. This initiative highlights the growing trend of sovereign AI, where countries build independent AI infrastructure to preserve language and culture. However, the HN community questions the feasibility and cost-effectiveness of training a full LLM with only 448 GPUs compared to fine-tuning existing models. The Olivia system, an HPE Cray Supercomputing EX, has 448 GPUs and 64,512 CPU cores, which some commenters argue is insufficient for training a fully fledged LLM. The storage is used for the training data corpus of Norwegian texts.

hackernews · rbanffy · May 25, 19:37 · [Discussion](https://news.ycombinator.com/item?id=48270770)

**Background**: Sovereign AI refers to national strategies to develop independent AI capabilities, including hardware, data, and models, to reduce reliance on foreign providers. Norway's goal is to create an LLM that understands Norwegian language, history, and culture, which globally trained English-centric models may not capture.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_AI_Fund">Sovereign AI Fund</a></li>
<li><a href="https://grokipedia.com/page/Sovereign_AI">Sovereign AI</a></li>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>

</ul>
</details>

**Discussion**: The HN discussion is mixed: some users praise the National Library's interface and the need for sovereign LLMs, while others criticize the hardware as inadequate and suggest using fine-tuning instead. There is also a proposal to share Norwegian training data with all model builders for broader benefit.

**Tags**: `#LLM training`, `#sovereign AI`, `#infrastructure`, `#storage`, `#debate`

---

<a id="item-9"></a>
## [Human Archive pays Indian gig workers to train robots](https://techcrunch.com/2026/05/26/human-archive-taps-into-indias-services-startups-to-collect-data-for-physical-ai/) ⭐️ 7.0/10

Human Archive, a startup founded by Berkeley and Stanford researchers, is paying gig workers in India to wear camera-equipped caps and sensor devices to collect real-world physical training data for AI and robotics. This approach could dramatically reduce the cost and scale of collecting physical AI training data, which is a major bottleneck for advancing robotics and autonomous systems. By leveraging India's gig economy, Human Archive may accelerate the development of robots that can operate in real-world environments. Workers wear sensor caps and cameras that capture their movements and surroundings, generating data for 'physical AI' — AI that perceives and acts in the physical world. The company targets clients including robotics labs and AI developers who need diverse, real-world training data.

rss · TechCrunch AI · May 26, 16:00

**Background**: Physical AI refers to artificial intelligence that enables autonomous machines to perceive, understand, and perform complex actions in the real world. Training such AI requires vast amounts of data from human demonstrations, but collecting that data is costly and slow. The gig economy offers a flexible, scalable workforce for data collection, and India has a large pool of gig workers who can perform such tasks at relatively low cost.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>

</ul>
</details>

**Tags**: `#physical AI`, `#data collection`, `#robotics`, `#gig economy`, `#AI training`

---

<a id="item-10"></a>
## [Memory Curator Agent Governance Layer for Multi-Agent Memory](https://www.reddit.com/r/artificial/comments/1to9p3u/memory_curator_agent_a_governance_layer_for/) ⭐️ 7.0/10

The post proposes a Memory Curator agent that acts as a governance layer for durable memory in multi-agent systems, where worker agents emit structured memory events and the curator decides whether to write, scope, or discard them across four predefined scopes. This addresses a common failure in multi-agent systems where memory becomes noisy, stale, and mis-scoped over time, and separating memory governance from task execution keeps the store useful longer, improving reliability and reducing user frustration. The four scopes are agent repo memory (durable design rules for one agent), agent team memory (cross-agent procedures, handoff standards, safety rules), project memory (current state, decisions, risks for one engagement), and session scratch (temporary observations). The curator uses a JSON schema with tagged fields (fact, decision, preference, risk, procedure, hypothesis) and an evidence reference.

rss · r/artificial RSS · May 26, 15:05

**Background**: Multi-agent systems often suffer from memory silos, noisy context, and governance fragmentation when multiple agents write to a shared memory store without coordination. Short-term and long-term memory types exist, but without proper scoping and curation, retrieval becomes unreliable. The Memory Curator pattern introduces a dedicated agent that handles only memory governance, analogous to organizational memory concepts like individual specialist memory, transactive team memory, and project memory.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@Quaxel/memory-isnt-a-dumping-ground-4eb2c0256c97">Memory Isn’t a Dumping Ground. How curated context makes AI agents</a></li>
<li><a href="https://arxiv.org/abs/2603.17787">Governed Memory: A Production Architecture for Multi-Agent ... Memory - Multi-agent Reference Architecture multi-agent-reference-architecture/docs/memory/Memory.md at ... Multi-Agent Systems & AI Orchestration Guide 2026 Memory in multi-agent systems: technical implementations Multi-Agent Memory Silos: Causes, Risks, and How to Solve Them Governed Memory: Multi-Agent Workflow Governance</a></li>
<li><a href="https://microsoft.github.io/multi-agent-reference-architecture/docs/memory/Memory.html">Memory - Multi-agent Reference Architecture</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#memory governance`, `#agent architecture`, `#memory curator`

---

<a id="item-11"></a>
## [China Restricts Overseas Travel for AI Talent at Alibaba, DeepSeek](https://www.reddit.com/r/LocalLLaMA/comments/1to5fj5/china_clamps_down_on_overseas_travel_for_ai/) ⭐️ 7.0/10

According to Bloomberg reports, China has expanded travel restrictions to include top AI talent at private firms such as Alibaba and DeepSeek, making it harder for researchers like former Qwen head Junyang Lin to travel abroad for conferences or personal reasons. This clampdown could slow the outflow of Chinese AI expertise and reduce the ability for key researchers to collaborate internationally, potentially impacting the development of open-source models from major Chinese players like DeepSeek and Alibaba's Qwen team. The travel curbs are reportedly being enforced by Chinese authorities asking companies to notify them of any overseas trips by senior AI scientists and sometimes denying approval. The policy previously applied to state-owned enterprises and military-linked researchers but now extends to private AI firms.

rss · r/LocalLLaMA RSS · May 26, 12:26

**Background**: DeepSeek is a Chinese AI company founded in 2023, known for developing highly competitive large language models like DeepSeek-R1 at a fraction of the cost of US rivals. Alibaba's Qwen (通义千问) team has also produced influential open-source models. Both companies have been key sources of open-weight AI models, with talent mobility contributing to the global AI ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**Tags**: `#AI talent`, `#China`, `#open-source`, `#DeepSeek`, `#geopolitics`

---

<a id="item-12"></a>
## [Together AI Open-Sources OSCAR: 2-bit KV Cache Quantization](https://www.reddit.com/r/LocalLLaMA/comments/1to5uml/new_kv_quants_coming_welcome_oscar_kv_quant_open/) ⭐️ 7.0/10

Together AI has open-sourced OSCAR (Offline Spectral Covariance-Aware Rotation), an attention-aware 2-bit KV cache quantization system for efficient long-context LLM serving. OSCAR significantly reduces memory and bandwidth demands for KV cache in long-context LLMs, enabling cheaper and faster inference without major accuracy loss, which is critical for scaling LLM deployment. Unlike generic Hadamard rotations, OSCAR derives attention-aware rotations from a one-time offline calibration pass, aligning quantization noise with directions where attention is least sensitive. It achieves 2-bit quantization of the KV cache.

rss · r/LocalLLaMA RSS · May 26, 12:44

**Background**: In large language models, the key-value (KV) cache stores intermediate attention vectors to avoid recomputation, but it becomes a memory bottleneck for long contexts. Quantization reduces the bit-width of these cache entries. OSCAR uses an attention-aware rotation to preserve important information better than uniform quantization or fixed rotations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/05/25/together-ai-open-sources-oscar-an-attention-aware-2-bit-kv-cache-quantization-system-for-long-context-llm-serving/">Together AI Open-Sources OSCAR: An Attention-Aware 2-Bit KV ...</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed excitement, with one user noting they were just starting to embrace another method (turboquant) when OSCAR appeared, reflecting a positive reception and eagerness to adopt the new technique.

**Tags**: `#KV cache quantization`, `#LLM serving`, `#open source`, `#Together AI`, `#long context`

---

<a id="item-13"></a>
## [Kwai Keye-VL-2.0-30B-A3B: First Multimodal Model with DSA Attention](https://www.reddit.com/r/LocalLLaMA/comments/1to63rt/keyevl2030ba3b_introducing_dsa_attention_into/) ⭐️ 7.0/10

Kwai released Keye-VL-2.0-30B-A3B, a 30B-class MoE vision-language model that integrates DeepSeek Sparse Attention (DSA) for the first time in a multimodal context, targeting long-video understanding and agent capabilities. This marks the first cross-domain application of DSA from pure language to multimodality, potentially enabling efficient long-video processing and real-time agent interactions. It could lower the barrier for video AI agents in consumer applications. The model uses a MoE architecture with 30B total parameters but only 3B activated per token. DSA dynamically combines local window attention with global sparse connections to reduce computation while preserving long-context performance.

rss · r/LocalLLaMA RSS · May 26, 12:55

**Background**: DeepSeek Sparse Attention (DSA) is an efficient attention mechanism originally developed for the DeepSeek-V3.2 language model, combining local windows with content-aware sparse connections. Keye-VL is Kwai's series of vision-language models aimed at video understanding and agent tasks. This release adapts DSA for multimodal inputs, a first in the field.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.02556">[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open ... DeepSeek Sparse Attention (DSA): A Comprehensive Review GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head ... AI on AI: Sparse Attention, from NSA to DSA – Champaign Magazine Inside DeepSeek V4: Hybrid Attention for Massive Contexts 十分钟读懂 DeepSeek-V3.2 稀疏注意力 DSA - 知乎 DeepSeek Sparse Attention from First Principles</a></li>
<li><a href="https://amitray.com/deepseek-sparse-attention-dsa-a-comprehensive-review/">DeepSeek Sparse Attention (DSA): A Comprehensive Review</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#vision-language`, `#MoE`, `#model release`, `#agent`

---