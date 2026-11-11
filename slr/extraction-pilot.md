# Extraction form pilot (P4)

Pilot of the data extraction form (`protocol.md` §5–6) on three studies of different natures, before the protocol is frozen (week 4, mini-tutorial slide 20, steps 1–2).
Studies: P1 Panda (2026), compares; P2 Gloaguen et al. (2026), evaluates and compares; P3 Macedo (2026), conceptual / document-based comparison.

Procedure: an AI assistant (Claude Code, Claude Opus 5.5) drafted each record from the full PDF, with the page of every value (week 4 slides 29–31: AI may draft extraction; it does not decide). The author verifies the drafts against the PDFs. These records are a pilot, not the final extraction, which is redone with the frozen form if the study is included.

Status: drafts done 2026-11-11. The author verified 3–4 key values per study (the riskiest ones, noted under each record); all confirmed, one value corrected (P2, DEV vs LLM). Quality answers are AI drafts not confirmed one by one: the pilot tested the checklist, and quality is assessed again by the author at the real extraction.

## P1 — Panda (2026), arXiv:2606.30689v1

AI draft; text extracted with pdftotext; printed page numbers = PDF page numbers. Table 1 (p. 6) columns came out jumbled: values mapped to conditions from Figure 1 (p. 6) and the text on p. 14.

| Field | Value | Page(s) |
|---|---|---|
| **ID** | P1 | — |
| Reference | Panda, S. (2026). *Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code*. arXiv:2606.30689v1 [cs.SE], 28 Jun 2026 | 1 |
| Year | 2026 | 1 |
| Publication type | Preprint (arXiv) | 1 |
| Author affiliation | Not stated (personal gmail address only) | 1 |
| Nature of the study | Compares (two controlled studies, 3 SDD frameworks + one ablation condition) | 1, 4 |
| **Approach A: traceSDD (cited)** | Version: Not stated. Artefacts: hierarchical REQ-XXX.Y.Z spec; mandatory inline `# [REQ-XXX.Y.Z]` citation on every non-trivial line; orphan-REQ check. Phases: not stated as a flow (spec → code with citations → orphan check). Human review: Not stated. SDD level: Not stated | 1, 2, 4, 11 |
| **Approach A′: traceSDD uncited** (ablation) | Same REQ-format spec, no inline citations. Other fields Not stated | 4 |
| **Approach B: Spec Kit** | Version: Not stated. Artefacts: native prose spec (user stories, FR-XXX, acceptance scenarios). Phases: spec → plan → tasks (whether plan and tasks were run is not stated). Human review: Not stated. SDD level: Not stated | 2, 4 |
| **Approach C: OpenSpec** | Version: Not stated. Artefacts: capability/scenario spec with C-NNN markers; post-hoc trace YAML sidecars. Phases, human review, SDD level: Not stated | 2, 5 |
| Task type | Not stated (benchmark tasks implemented from a spec; no existing code base mentioned) | 4–5 |
| Size | Study 1: 15 single-file (50–100 lines) + 5 multi-file (600–800 lines). Study 2: 37 small + 13 large. Range 50–1,000 lines | 4, 14 |
| Domain | Python; Study 1: 5 SE domains; Study 2: 8 SE domains (DSA, Web/API, validation, security, file I/O, concurrency, config, testing) | 4, 14 |
| Team profile | N/A (no human participants) | — |
| Cost metrics | None measured (detection "O(1) per file", not measured) | 11 |
| Functional quality metrics | TPR: share of ground-truth tests passed (tests not described) | 5 |
| Internal quality metrics | None of the listed kind. Main outcomes: LSS (determinism), TDR and FPR (hallucination detection) | 5 |
| Human effort metrics | None (claims "zero manual effort" for detection) | 11 |
| How metrics are collected | Automatic: LSS via difflib on stripped code; TDR/FPR via set difference of cited REQ IDs; TPR via tests. Hallucinations injected (who/how not stated) | 5, 11 |
| **Evaluation** | Criteria: pre-registered H1–H3. Agent/harness not stated for any configuration | 4 |
| – traceSDD cited + n.s. + Claude Sonnet 4.6 | LSS 0.535 (SD 0.167); TDR 86.4%; FPR 0%; TPR 100%. Partly | 6, 11, 13 |
| – traceSDD uncited + n.s. + Claude Sonnet 4.6 | LSS 0.745 (SD 0.194); TDR 0%; TPR 100%. Works (determinism), not (detection) | 6, 11 |
| – Spec Kit + n.s. + Claude Sonnet 4.6 | LSS 0.460; TDR 0%; TPR 100%. Does not work ("weakest choice") | 6, 11, 14 |
| – OpenSpec + n.s. + Claude Sonnet 4.6 | LSS 0.487; TDR 0%; TPR 100%. Partly | 6, 11, 14 |
| – traceSDD cited + n.s. + GLM-5-turbo | LSS 0.510 (SD 0.147); TDR 88.0%; FPR 0%; TPR 100%. Partly | 6, 11 |
| – traceSDD uncited + n.s. + GLM-5-turbo | LSS 0.644 (SD 0.160); TDR 0%; TPR 100%. Works (determinism), not (detection) | 6, 11 |
| – Spec Kit + n.s. + GLM-5-turbo | LSS 0.434; TDR 0%; TPR 100%. Does not work | 6, 11, 14 |
| – OpenSpec + n.s. + GLM-5-turbo | LSS 0.480; TDR 0%; TPR 100%. Partly | 6, 11, 14 |
| **Comparison: design** | Tasks: Study 1, 20 named Python tasks; Study 2, 50 new tasks (not named). 4 conditions × 2 models, separate studies; 840 implementations. Baseline: none single (Spec Kit, OpenSpec "external baselines"; uncited the "critical control"). Held constant: model within study; same spec content cited vs uncited; agent, prompt, temperature, operator Not stated. Acceptance tests: "ground-truth tests", not described. Repetitions: 3 cold-start sessions. Human intervention: Not stated | 1, 2, 4, 5 |
| **Comparison: result** | Determinism: uncited > cited > OpenSpec > Spec Kit in both models (uncited vs Spec Kit d=0.98/1.05; cited vs Spec Kit d=0.47/0.42; cited vs OpenSpec d=0.18/0.14). Detection: only cited. Correctness: all 100%. Significant except cited vs OpenSpec (p=0.44/0.32); after Holm also Spec Kit vs OpenSpec not significant | 1, 5, 7, 8, 11 |
| **Comparison: did the method work** | Distinguished most pairs, not cited vs OpenSpec; TPR separated none. Repeatable: cross-model replication claimed. Limitations: LSS lexical; injected IDs easier than real hallucinations; Claude study underpowered; session independence limited | 7, 8, 11, 13–15 |
| Conclusions: limitations and gaps | Python only, 50–1,000 lines; two models; orphan check misses uncited hallucinated lines (~12%); future: more models, production scale, temperature, maintenance cost, CI/CD | 13–15 |
| Q1 | Yes (1): RQ1, RQ2, H1–H4 | 3–4 |
| Q2 | Partly (0.5): no prompts, harness, temperature, injection procedure, replication package | 4–5 |
| Q3 | Partly (0.5): models named; no agent or framework versions | 1, 4 |
| Q4 | Partly (0.5): Study 2 tasks only by category; availability not stated | 4 |
| Q5 | Partly (0.5): TPR against tests; TDR against author-injected IDs | 5 |
| Q6 | Partly (0.5): no cost metrics | 5 |
| Q7 | Yes (1) | 4–5 |
| Q8 | Yes (1): 3 runs, paired tests, effect sizes, CIs, Holm | 5, 7 |
| Q9 | Partly (0.5): H1 "supported" vs Spec Kit below pre-registered d>0.5; abstract and body statistics differ | 1, 4, 7, 8 |
| Q10 | Yes (1): Section 8 | 14–15 |
| Q11 | No (0): preprint | 1 |
| Q12 | Partly (0.5), unclear: no affiliation; author's relation to traceSDD not stated | 1, 3 |
| Q13 | N/A | — |
| **Score** | 7.5 / 12 = 0.63 | — |

To check in the PDF: Table 1 mapping and SD (text p. 6 says Spec Kit has the highest variance); Table 3 TDR 100% per type vs 86.4% / 88.0% overall.

**Verified by the author (2026-11-11):** (1) Table 1 LSS values for Claude confirmed; (2) only the models are named (Claude Sonnet 4.6, GLM-5-turbo), no agent or harness; (3) Spec Kit: only "native prose specification format" is stated, not whether plan and tasks were run; (4) no affiliation, confirmed.

### Form problems (P1)

- No agent named ("cold-start LLM sessions"): agent slot Not stated everywhere; no place for an ablation variant; no single baseline.
- Main outcomes (determinism, hallucination detection) fit no metric field.
- One paper, two studies with different tasks, N and models; design block assumes one.
- Approach fields assume the whole workflow was run; only the spec format seems used.
- No place for reporting problems (abstract vs body, hypothesis below its threshold) or pre-registration and replication package.
- Q12 and Q13 ambiguous (author's link to traceSDD unclear; traceSDD "novel" and compared).

## P2 — Gloaguen et al. (2026), arXiv:2602.11988v3

AI draft (Claude Code, Claude Opus 5.5), main paper + appendices as needed. To be verified by the author.

| Field | Value | Page(s) |
|---|---|---|
| **ID** | P2 | — |
| Reference | Gloaguen, T., Mündler-Sasahara, N., Müller, M. N., Raychev, V., Vechev, M. (2026). *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* arXiv:2602.11988v3 [cs.SE], 29 Sep 2026 | 1 |
| Year | 2026 (v3, 29 Sep 2026) | 1 |
| Publication type | Preprint (arXiv) | 1 |
| Author affiliation | ETH Zurich (Gloaguen, Mündler-Sasahara, Vechev); LogicStar.ai (Müller, Raychev) | 1 |
| Nature of the study | Compares (no context file vs LLM-generated vs developer-written); also proposes a benchmark (CTXBENCH) | 1–2, 5 |
| **Approach A: LLM-generated context file** | Version: none (context files "formalized in August 2025"). Artefact: one file at repo root (CLAUDE.md for Claude Code; AGENTS.md for Codex, Qwen Code); content: overview, tooling, testing. Phases: init command generates file → file in context → agent resolves task → tests. Human review: none (used unedited). SDD level: Not stated | 2–5, 7, 16 |
| **Approach B: Developer-committed context file** | Version: none. Artefact: existing file at pre-patch state; mean 641 words, 9.7 sections; 8 of 12 have a codebase overview. Phases: as A. Human review: Not stated. SDD level: Not stated | 2, 4–5, 7, 17–18 |
| Task type | Existing code bases: bug fixing and feature addition from GitHub PRs | 2, 3 |
| Size | SWE-bench Lite: 300 tasks, 11 repos. CTXBENCH: 138 instances, 12 repos; mean 3,337 files; gold patch mean 118.9 lines, 2.5 files | 2, 5 |
| Domain | Open-source Python repos (django, sympy, transformers, …) | 4, 5, 14 |
| Team profile | Not stated (autonomous agents) | — |
| Cost metrics | Steps; LLM inference cost USD per task (Qwen via OpenRouter price); reasoning tokens (GPT only). No wall-clock time | 6, 8 |
| Functional quality metrics | Success (resolution) rate: % of patches passing all tests | 3, 6 |
| Internal quality metrics | Not measured (efficiency, security as future work) | 9 |
| Human effort metrics | Not measured | — |
| How metrics are collected | Automatic (tests in Docker, traces); LLM-as-judge for tool intent and overview detection; manual trace inspection and cheating check | 6, 7, 13 |
| **Evaluation** | Success % SWE / CTX; cost USD per instance SWE / CTX. Criterion: tests pass | 6, 15 |
| – None + Claude Code + Sonnet-4.5 | 59.9 / 73.2; 1.30 / 1.15. Baseline | 6, 15 |
| – LLM + Claude Code + Sonnet-4.5 | 58.7 / 65.2; 1.51 / 1.33. Does not work | 6, 15 |
| – DEV + Claude Code + Sonnet-4.5 | CTX 70.3; 1.30. Does not work | 6, 15 |
| – None + Codex + GPT-5.2 | 56.6 / 65.2; 0.32 / 0.38. Baseline | 6, 15 |
| – LLM + Codex + GPT-5.2 | 54.4 / 68.1; 0.43 / 0.57. Does not work (mixed) | 6, 15 |
| – DEV + Codex + GPT-5.2 | CTX 68.1; 0.54. Partly (+2.9, n.s.) | 6, 15 |
| – None + Codex + GPT-5.1 Mini | 47.7 / 54.3; 0.18 / 0.18. Baseline | 6, 15 |
| – LLM + Codex + GPT-5.1 Mini | 47.6 / 50.7; 0.22 / 0.20. Does not work | 6, 7, 15 |
| – DEV + Codex + GPT-5.1 Mini | CTX 55.8; 0.19. Partly (+1.5, n.s.) | 6, 15 |
| – None + Qwen Code + Qwen3-30B-Coder | 31.1 / 45.7; 0.12 / 0.13. Baseline | 6, 15 |
| – LLM + Qwen Code + Qwen3-30B-Coder | 32.4 / 47.1; 0.13 / 0.15. Partly / no (n.s.) | 6, 15 |
| – DEV + Qwen Code + Qwen3-30B-Coder | CTX 53.6; 0.15. Partly (+7.9) | 6, 15 |
| **Comparison: design** | Tasks: SWE-bench Lite (300) + CTXBENCH (138, LLM-generated descriptions and tests, reviewed manually). Configurations: 4 agent+model × {None, LLM, DEV}; DEV only on CTXBENCH (20 cells) + ablations. Baseline: None. Held constant: default agent settings, temperature, task, Docker, no git history. Acceptance tests: hidden tests (75% coverage of modified code; 25/138 edited). Repetitions: 1. Human intervention: none during runs; manual cheating check after | 3–5, 8–9, 13, 16–18 |
| **Comparison: result** | LLM vs None: −0.5% SWE (p=0.87), −2% CTX (p=0.37). DEV vs None: +2.4% (p=0.21). DEV vs LLM: DEV better (p=0.038). Text (p. 2): "7% on average" better performance; Table 5 success-rate differences per model 0 (GPT-5.2) to 6.5 points (Qwen3-30B), about 5 for the others; the text figure is not explained. Cost: LLM +20%/+23%, +2.45/+3.92 steps; DEV +3.34 steps, ≤+19% cost. Significant: only DEV vs LLM on success; all cost/step increases (p ≤ 0.0287) | 2, 6, 8, 16 |
| **Comparison: did the method work** | Distinguished on cost and steps; mostly not on success. Repeatable: single sample; SE and tests reported; temperature 0 for 3 of 4; no code/data release stated. Limitations: SWE-bench per-repo noisy; CTXBENCH tasks ~15% easier; contamination checked; Python only | 5–6, 9, 14–18 |
| Conclusions: limitations and gaps | Python only; only task resolution measured; how to generate useful context files is open; recommends only non-standard instructions in context files | 2, 9 |
| Q1 | Yes (1) | 1–2 |
| Q2 | Yes (1): setup and all prompts given | 5, 13, 19–23 |
| Q3 | Partly (0.5): no agent/CLI versions | 5 |
| Q4 | Partly (0.5): CTXBENCH availability not stated | 3–5 |
| Q5 | Yes (1): hidden tests | 3, 5 |
| Q6 | Yes (1): success, steps, USD cost | 6 |
| Q7 | Yes (1): None baseline | 5 |
| Q8 | Partly (0.5): single run, but statistical tests | 5, 6, 16–17 |
| Q9 | Yes (1) | 6, 9 |
| Q10 | Partly (0.5): short limitations section; no threats section | 9, 16–18 |
| Q11 | No (0): preprint | 1 |
| Q12 | Yes (1): ETH, LogicStar.ai; not tool vendors | 1 |
| Q13 | N/A | — |
| **Score** | 8.5 / 12 = 0.71 | — |

**Verified by the author (2026-11-11):** (1) Table 5 success rates for Claude Code + Sonnet-4.5 confirmed (CTXBENCH rows labelled "PLAN-BENCH"); (2) one run per configuration confirmed; (3) the text claims "7% on average" better performance for DEV vs LLM, while Table 5 success-rate differences go from 0 (GPT-5.2) to 6.5 points (Qwen3-30B), 4–5 for the others; (4) affiliations confirmed.

### Form problems (P2)

- Configuration at two levels: crossed with 2 benchmarks plus ablations; needs a benchmark/dataset dimension and a place for ablations.
- Per-configuration numbers only in an appendix table; text and table disagree ("7%" vs ≈4.2 pts); needs a "source used" and "notes / inconsistencies" field.
- Approach fields assume a workflow; a context file is a single artefact; Böckeler levels do not cover "context file without a spec".
- One verdict per configuration hides that quality is flat but cost worse; split into quality and cost verdicts.
- No field for mechanism/behaviour findings (instructions followed, more testing) or benchmark construction quality.
- Nature of the study not exclusive (compares + proposes benchmark); Q12 unclear when a co-author company works on agents but does not make the tools evaluated.

## P3 — Macedo (2026), arXiv:2606.04967

AI draft (Claude Code, Claude Opus 5.5), whole PDF read; printed page numbers = PDF page numbers. To be verified by the author.

| Field | Value | Page(s) |
|---|---|---|
| **ID** | P3 | — |
| Reference | Macedo, S. O. de (2026). *From Prompt to Process: a Process Taxonomy and Comparative Assessment of Frameworks Supporting AI Software Development Agents*. arXiv:2606.04967v1 [cs.SE], 3 Jun 2026 | 1 |
| Year | 2026 | 1 |
| Publication type | Preprint (arXiv) | 1 |
| Author affiliation | Federal Institute of Goias (single author) | 1 |
| Nature of the study | Compares (qualitative, document-based comparison of frameworks); also proposes an evaluation instrument (six-dimension taxonomy + 0/1/2 scoring rubric). Paper: "a comparative study… grounded in a directed and qualitative search of primary sources rather than in an exhaustive systematic review" | 3, 11 |
| **Approach: GitHub Spec Kit** | Version: Not stated (sources accessed 2026-05-26). Artefacts: constitution, specification, plan, tasks. Phases: constitution → specification → plan → tasks → implementation (+ optional clarification, analysis, checklist commands). Human review: "reviewable intermediate artifacts"; analysis/checklist commands; "checklists and gates". SDD level: Not stated in Böckeler's terms ("the specification is a source of truth, not a disposable document") | 8, 9, 13, 15–16 |
| **Approach: OpenSpec** | Version: Not stated. Artefacts: single unified specification + traceable change proposals. Phases: "structured change-management flow" via slash commands (steps not listed). Human review: Not stated. SDD level: Not stated | 10 |
| **Approach: BMAD Method** | Version: Not stated. Artefacts: product brief, PRD, architecture, epics, stories, code review. Phases: optional analysis, planning, solution, implementation + "quick flow". Roles: analyst, PM, architect, developer, UX, tech writer. Human review: PRD review, readiness checks, code review ("gates"). SDD level: Not stated | 8, 9, 10 |
| **Approach: Get Shit Done (GSD)** | Version: Not stated (repo moved to open-gsd/gsd-core). Artefacts: specifications and executable steps; focus on context assembly. Phases: Not stated. Human review: Not stated. Coupled to Claude Code. SDD level: Not stated | 10, 16 |
| **Approach: Spec Kitty** | Version: Not stated. Artefacts: specs, plans, tasks in a repo directory; work packages in git worktrees. Phases: spec → plan → tasks → next → review → accept → merge. Human review: review and acceptance before merge. Agents: Claude, Cursor, Gemini. SDD level: Not stated | 8, 10–11 |
| **Approach: Reversa** (author's own) | Version: Not stated. Artefacts: operational specifications recovered from legacy code, with traceability, confidence and gap labels. Phases: Not stated. Human review: Not stated. SDD level: Not stated; reverse direction (legacy code → spec) | 8, 11 |
| **Approach: Spec-Flow** (out-of-sample) | Version: Not stated. Phases: spec → plan → tasks → implement → optimize → ship. Mechanisms: persistent domain memory, backend/frontend/DB agents, TDD, worktrees, tiered quality gates, multi-agent voting. Human review: Not stated. Claude Code (+ Gemini CLI extension). SDD level: Not stated | 13 |
| Task type | Greenfield (Spec Kit, OpenSpec, BMAD, GSD, Spec Kitty); legacy/brownfield (Reversa). No tasks run | 2, 11 |
| Size | Not stated | — |
| Domain | Not stated (general software development) | — |
| Team profile | Not stated; target user "a developer who already operates a development agent" | 3 |
| Cost metrics | None measured; productivity claims "treated qualitatively… never a number of our own"; token cost only proposed as future metric | 4, 14 |
| Functional quality metrics | None measured | — |
| Internal quality metrics | None measured | — |
| Human effort metrics | None measured; proposed: "rate of human review required", "number of corrections per phase" | 14 |
| How metrics are collected | Manual: one rater scores each framework 0/1/2 on six dimensions from official docs and repos. Traction (stars, last push) automatic via GitHub API, 26–28 May 2026 | 4, 5, 11–12 |
| **Evaluation** | No agent + model configurations; unit is the framework. Criterion: rubric (0 absent, 1 partial, 2 strong) on Spec, Ctx, Roles, Exec, Valid, Port. Verdict: N/A | 11–12 |
| – Spec Kit | 2,1,1,1,1,2 = 8/12 | 12 |
| – OpenSpec | 2,1,0,1,0,2 = 6 | 12 |
| – BMAD Method | 2,2,2,1,2,1 = 10 | 12 |
| – GSD | 1,2,0,1,0,0 = 4 | 12 |
| – Spec Kitty | 2,1,1,2,2,1 = 9 | 12 |
| – Reversa | 2,2,0,0,1,1 = 6 | 12 |
| – Spec-Flow (out-of-sample) | 2,2,2,2,2,1 = 11 | 13 |
| **Comparison: design** | Document-based. Project/tasks: N/A. Compared: 6 frameworks + Spec-Flow out-of-sample. Baseline: none. Held constant: same rubric, rater, source type. Acceptance tests: N/A. Repetitions: one scoring, one rater, no inter-rater check. Intervention rules: N/A. Selection: 4 functional conditions + traction filter (≥1000 stars, push in last 6 months); 9 candidates → 6 | 3–5, 11–12 |
| **Comparison: result** | BMAD 10, Spec Kitty 9, Spec Kit 8, OpenSpec 6, Reversa 6, GSD 4. Most portable: Spec Kit, OpenSpec. No framework scores 2 on all dimensions; trade-off process depth vs portability. Roles and validation separate most; specification least. Significance: N/A | 12 |
| **Comparison: did the method work** | Distinguished: yes (4–10). Repeatable: claimed, but one rater, no inter-rater reliability; generality checked on Spec-Flow. Limitations stated: single rater; scores are "the authors' judgement… not a third-party-validated empirical measurement"; stars an unstable proxy; grey-literature promotional bias; traction selects by adoption | 5, 12, 13 |
| Conclusions: limitations and gaps | Non-exhaustive search; stars snapshot May 2026; grey-literature bias; single rater; conflict of interest (Reversa). No framework independently evaluated academically; productivity claims rest on demos; no benchmarks of the complete process. Risks: spec/code drift, over-trust in generated artefacts, fragile extensions, lock-in | 1, 4–6, 11, 13, 15 |
| Q1 | Yes (1): explicit RQ1–RQ4 | 2 |
| Q2 | Partly (0.5): criteria, thresholds and rubric explicit; rubric levels generic, one rater, snapshot CSV without URL | 3–5, 11 |
| Q3–Q8 | N/A (not empirical) | — |
| Q9 | Yes (1): hedged; mixed/negative findings reported | 12, 15 |
| Q10 | Yes (1): "Limitations of the method" paragraph | 5 |
| Q11 | No (0): arXiv preprint | 1 |
| Q12 | Partly (0.5): independent for 5 of 6; author wrote Reversa (declared) | 3–5 |
| Q13 | N/A: proposes an evaluation instrument, not an SDD approach | — |
| **Score** | 4 / 6 = 0.67 | — |

**Verified by the author (2026-11-11):** (1) totals in the p. 12 table confirmed; (2) the author declares Reversa as his own framework; (3) "Limitations of the method" paragraph admits a single rater.

### Form problems (P3)

- Evaluation group assumes approach + agent + model configurations; here the unit is the framework scored from documentation; verdict has no meaning.
- Nature of the study allows one value; this study compares and proposes an evaluation instrument. Q13 does not cover studies proposing an evaluation method.
- Q3–Q8 all N/A for non-empirical studies; score rests on 6 questions and is not comparable with an experiment's score.
- Böckeler SDD level does not fit: the paper does not use the terms; Reversa is reverse direction (code → spec).
- No place for: tool selection criteria, per-tool evidence level, out-of-sample check, proposed future metrics, the author's AI use; no slot for agents supported (portability).
- Q12 is per study but independence varies per tool.
