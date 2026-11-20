# Screening sheet (title/abstract)

Quick reference for screening in Rayyan, from `protocol.md` §4 and §4.2. The protocol rules; this sheet only summarises it.

## Procedure

| Pass | Read | Rule |
|---|---|---|
| 1 | Title | Exclude only when clearly out of scope (another domain). Any doubt goes to pass 2 |
| 2 | Title, abstract, keywords | Apply IC/EC below. Include, exclude (with label) or maybe. Maybe goes to full text |

- Every exclusion gets **one** label: the first criterion that fails, in the order of the decision flow below.
- Index-term-only records are screened like any other (no automatic removal, §4.2 step 5).
- Rayyan's relevance predictions are not used to decide (§4.2 step 9).
- A new rule of thumb adopted during screening goes into the decision log at the end, so it is applied the same way to every record.

## Decision flow

1. **Another domain?** Agents in robotics, vehicles, networks, healthcare, finance, dialogue, multi-agent LLM systems in general, not software development → **IC1**.
2. **Coding agents at all?** It must be (a) SDD with coding agents, (b) AGENTS.md, context, rules or instruction files with coding agents, or (c) evaluation or comparison of coding agents on software development tasks. Otherwise → **IC1**.
3. **Only code completion or single-function generation** (HumanEval style), no multi-step or repository-level behaviour → **EC1**.
4. **"Specification" in the formal-methods or requirements sense** (Z, TLA+, requirements documents) with no coding agents → **EC2**.
5. **Editorial, keynote, panel, poster, abstract only, tutorial** → **EC3**.
6. **Earlier or duplicate version** of another record (keep the most complete; published over preprint) → **EC4**.
7. **Group (c) only:** main contribution is a new agent or technique run on an existing benchmark (e.g. SWE-bench), and it adds nothing to the evaluation method (no new metric, no repetitions, no control of agent and model, no new comparison design) → **EC5**.
8. Published before 2023 → **IC2**; not in English → **IC3**. IC4 (full text) is checked at full-text screening.

Otherwise **include**. From decision 135 of pass 2 (2026-11-20): decide include or exclude on every record, keeping borderline records as **include**; **maybe** only when the abstract does not make clear what the study does. Group (c) is narrowed later in pass 3 (protocol §4.2 step 4b).

Kept: workshop and short papers; secondary studies (reviews, surveys); new benchmarks or evaluation methods for coding agents (a contribution to the evaluation method, so not EC5).

## Rayyan labels

| Label | Meaning |
|---|---|
| IC1 | Not SDD, context files or coding-agent evaluation (includes the pilot's OUT-SE and OTHER) |
| IC2 | Before 2023 |
| IC3 | Not in English |
| EC1 | Completion or single function only, not agentic |
| EC2 | Formal or requirements specification, no coding agents |
| EC3 | Editorial, keynote, panel, poster, abstract, tutorial |
| EC4 | Earlier or duplicate version |
| EC5 | New agent on existing benchmark, nothing for the evaluation method |

Optional inclusion labels, useful later for extraction: IC1a, IC1b, IC1c.

## Examples from the pilot (5 Nov)

The pilot decisions predate EC5 (adopted 9 Nov). The group (c) "Y" records are the ones EC5 now targets.

| ID | Title (short) | Pilot decision | Note for now |
|---|---|---|---|
| P02 | Evolution Context Gap: agent manifests | I (IC1b, IC1c) | Context files: clear include |
| P06 | Spec-Driven AI: multiagent SDLC framework | I (IC1a) | SDD: clear include |
| P04 | Execution control harness for LLM code generation | I (IC1c, IC1a), group (c) Y | Compared with a spec-driven baseline, so IC1a holds: include |
| P01 | MCP coding agent for accessibility fixes | I (IC1c), group (c) Y | New setup, four LLM backends on one test case: EC5 candidate |
| P15 | LLM failure localisation in microservices | I (IC1c), group (c) Y | Own multi-agent system on an existing benchmark: EC5 candidate |
| P30 | Human-in-the-loop software development agents | I (IC1c), group (c) N | Evaluation is the contribution: include |
| P10 | Developer-agent collaborations in the wild | E (OTHER) | Now IC1 |
| P11 | Autonomous intersection management (vehicles) | E (OUT-SE) | IC1, another domain |
| P28 | AgentLeak: privacy leakage in multi-agent LLMs | E (OUT-SE) | IC1, not software development |
| P09 | Fairness in autonomous ecosystems | E (OTHER) | IC1, another domain |

## Decision log (rules of thumb adopted during screening)

| Date | Case | Rule |
|---|---|---|
| 2026-11-20 | Coding agents and games | Games are software, so the topic alone does not exclude. Agent that plays the game (game-playing, RL, NPCs) or generates non-code content (levels, narrative, assets) → IC1. Agent that writes or changes a game's code → normal flow (a/b/c, EC5) |
| 2026-11-20 | Comparison on an existing benchmark | EC5 depends on the main contribution, not on the benchmark being new. A new agent or technique on an existing benchmark with nothing for the evaluation method → EC5. An empirical study comparing existing agents or models (no new agent proposed) → include, the comparison is the contribution (as P30). A new benchmark → include. Test: does the paper sell an agent or measure agents? |
| 2026-11-20 | Multi-agent systems | Multi-agent coordination in general (not software development) → IC1. New multi-agent coding framework on an existing benchmark → EC5. Study comparing agent configurations on software tasks (single vs multi-agent, coordination strategies, roles, topologies) → include, relevant to RQ3. New benchmark or method for evaluating coordination of coding agents → include |
| 2026-11-20 | Agent as developer vs agent as component | The agent must develop software (write, change, test code). Agents as part of the system's architecture or product (e.g. microservices vs LLM multi-agent systems, chatbots, data pipelines) → IC1, even in a software engineering venue |
| 2026-11-20 | Record with no abstract | Maybe, unless the title alone is clearly out of scope (then exclude with the code). Before full text, one extra pass over these Maybe records to look up the abstract (DOI, publisher, Google Scholar) and decide by the normal flow |

## Appendix: IEEE records with no search term in title or abstract

27 records found only by IEEE Xplore whose title and abstract contain none of the string terms: they matched on index terms (INSPEC) or on IEEE's word stemming. Same situation as the pilot's 44 index-term records. Not removed automatically (§4.2 step 5): screen them like the others, but expect most to fail IC1. Some look relevant (e.g. repository-level benchmarks, testing agents), so read them. Listed by a string-term check over `rayyan-after-dedup-2026-11-18.csv` on 2026-11-19.

| # | Title | Rayyan key |
|---|---|---|
| 1 | A Comparative Study Towards Designing a Hybrid Architecture of Microservices and LLM-based Multi-Agent Systems | rayyan-800742549 |
| 2 | A First Look at Privacy Risks of Android Task-executable Voice Assistant Applications | rayyan-800742569 |
| 3 | A Large Language Model-Based Agent for Automated Bidding Strategy Generation in Electricity Markets | rayyan-800742556 |
| 4 | A Preliminary Study on 3DAV Coding Resource Allocation Optimized by Multi-Agent Game | rayyan-800742598 |
| 5 | AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems | rayyan-800742546 |
| 6 | Agentic AI Quiz-Based Learning System: Enhancing MCQ Generation via Long-Context Cached Retrieval-Augmented Generation | rayyan-800742594 |
| 7 | Agentic AI: An Emerging Paradigm of Computing?: Panel Discussion at IEEE CISOSE 2026 | rayyan-800742619 |
| 8 | Agentic SOC: A Hierarchical Swarm-Orchestrated Multi-Agent LLM Architecture for Autonomous OT Cyber Defense | rayyan-800742563 |
| 9 | An Efficient LLM Agent Framework for Cost Optimization through Token Optimization and Trajectory Reduction | rayyan-800742561 |
| 10 | An Empirical Evaluation of LLM-Based Approaches for Code Vulnerability Detection: RAG, SFT, and Dual-Agent Systems | rayyan-800742559 |
| 11 | An Intelligent Agentic System for Autonomous Codebase Enhancement | rayyan-800742553 |
| 12 | An LLM-Based Multi-Agent Architecture for Schema-Aware Data Mining in Intelligent Information Systems | rayyan-800742577 |
| 13 | Autonomous Intersection Management with Heterogeneous Vehicles: A Multi-Agent Reinforcement Learning Approach | rayyan-800742591 |
| 14 | Closing the Loop: Overcoming the Tool-Feedback Gap in Agentic Hardware Design | rayyan-800742573 |
| 15 | DS-Agent: Role-Aware Hybrid LLM Assignment for Cost-Efficient Automated Data Science | rayyan-800742599 |
| 16 | Deciding the Path: Leveraging Multi-Agent Systems for Solving Complex Tasks | rayyan-800742568 |
| 17 | Evaluating Self-Reflective LLM Agents for Autonomous Kubernetes Troubleshooting | rayyan-800742593 |
| 18 | FedLMA: A Federated Learning Framework Integrating LLM-Based Multi-Agent Reasoning With Knowledge Distillation | rayyan-800742595 |
| 19 | Large Language Models and Smart Contract Security in Autonomous Financial Systems | rayyan-800742551 |
| 20 | MUATC: Multi-Agent Utilization to Augment Test Coverage | rayyan-800742575 |
| 21 | Meta-agentic Framework for Software bug detection using Large Language Models | rayyan-800742583 |
| 22 | Multi-Agent AI Engineering: Design, build, and operate AI systems that think and act as coordinated teams | rayyan-800742534 |
| 23 | POS-MAS: An Autonomous Multi Agent and RAG Driven Diagnostic Platform for Token POS Systems | rayyan-800742596 |
| 24 | RepoTransBench: A Real-World Multilingual Benchmark for Repository-Level Code Translation | rayyan-800742530 |
| 25 | Towards Autonomous Testing Agents via Conversational Large Language Models | rayyan-800742539 |
| 26 | Where AI Use is Normalized, Author Seniority But Not AI Disclosure Biases Code Review | rayyan-800742557 |
| 27 | Why Neural Coding Is a Cognitive Trap as an Evolutionary Step From Vibe Coding | rayyan-800742543 |
