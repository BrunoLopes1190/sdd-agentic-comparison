# SLR protocol (draft)

Status: draft, not frozen. Method: Kitchenham & Charters (2007); PRISMA 2020 (Page et al., 2021).
Built step by step following the week 4 SLR module (`course-materials/week-04/slr-mini-tutorial.md`).
Reference text: the approved formalisation (`admin/formalizacao_1240441.pdf`).

## 1. Objective, scope and review questions

**Objective.** Characterise the Spec-Driven Development (SDD) approaches for development with coding agents, and the evidence on how such approaches and coding agents are evaluated and compared.

**Scope.** 2023 to the search cut-off date. Primary and secondary studies. SDD, or structured specifications and related context mechanisms (e.g. AGENTS.md), used by LLM-based coding agents.
The start year is 2023 because the evaluation of autonomous coding agents starts then (needed for RQ2 and RQ3); SDD for agents only appears in 2025, which the selection criteria handle.

**Unit of analysis.** A study that describes, applies or evaluates an SDD approach with coding agents, or that evaluates or compares coding agents under controlled conditions.

| RQ | Question | Serves |
|---|---|---|
| RQ1 | Which SDD approaches for development with agents are described, and what do they prescribe (artefacts, phases, human review points)? | O1, comparative framework |
| RQ2 | How are the results of SDD approaches and coding agents measured: which cost, quality and human effort metrics are used, and how are they collected? | O2, metrics |
| RQ3 | How do comparative studies make conditions comparable: reference project or task set, common briefing, acceptance tests, baseline, control of agent, model and operator, repetitions for non-determinism? | O2 and O3, evaluation design |
| RQ4 | Which results, limitations and gaps are reported on the effect of SDD, and of related context mechanisms, on cost and quality? | Research gap |

RQ3 is not limited to SDD: comparisons of SDD approaches on the same project are almost absent (the gap), so RQ3 draws on comparative evaluations of coding agents in general (benchmarks, controlled experiments, workflow comparisons).
Related context mechanisms (e.g. Gloaguen et al., 2026) are in scope for RQ2–RQ4 only.

## 2. Concept blocks and search strings

Synonyms are joined with OR inside a block; blocks are joined with AND. Draft lists, to be refined by the pilot search (P4); changes go to the change log.

| Block | Concept | Terms (draft) |
|---|---|---|
| A1 | Spec-Driven Development | "spec-driven", "specification-driven", "spec-first", "spec kit", OpenSpec, BMAD, Kiro |
| A2 | Related context mechanisms | "AGENTS.md", "context file*", "repository-level context", "instruction file*", "rules file*", "agent manifest*" |
| B | Coding agents | "coding agent*", "AI coding agent*", "software engineering agent*", "agentic coding", "agentic software", "AI coding assistant*"; and ("LLM-based agent*" OR "autonomous agent*") only together with ("software engineering" OR "software development" OR "code generation") |
| C | Comparative evaluation | benchmark*, "empirical stud*", "controlled experiment*", "comparative evaluation", "comparative study" |
| D | Cost, quality and effort metrics | "token usage", "token consumption", "inference cost", "API cost", "pass@k", "resolve rate", "task success", "functional correctness", "code quality", maintainability, "technical debt", "human effort", "developer effort", "human intervention" |

| String | Logic | Serves |
|---|---|---|
| S1 | (A1 OR A2) AND B | RQ1, RQ2, RQ4 |
| S2 | B AND (C OR D) | RQ2, RQ3 |

Term choices:
- "specification" alone is excluded: it retrieves formal-specification work (Z, TLA+) outside scope.
- Bare "cost", "quality", "accuracy", "usability" are excluded: too frequent in abstracts. "Credits" is excluded: vendor pricing, and it matches acknowledgements.
- Agent product names (e.g. Claude Code, Cursor, Copilot) are excluded from block B to avoid vendor bias; generic terms cover them.
- File names such as CONTEXT.md or ARCHITECTURE.md are excluded: databases drop punctuation, so they become "context", "architecture" and retrieve noise. AGENTS.md is kept as an open, multi-vendor convention; the pilot checks how each database handles it.
- S2 is one string because (B AND C) OR (B AND D) = B AND (C OR D). In the pilot, B AND C and B AND D are also run separately to see what each block adds.
- A2 studies are eligible for RQ2–RQ4 only (see selection criteria).
- "LLM-based agent*" and "autonomous agent*" are generic: alone they retrieve agents from other domains (in the pilot, 162 of 207 S2 records, mostly robotics, UAV, networks and healthcare). They count only with a software engineering term.
- "agentic software engineering" is not added: the phrase "agentic software" already matches it.
- CLAUDE.md and similar vendor file names are excluded, by the same rule as product names; AGENTS.md is kept (see above). In the pilot, "AGENTS.md" returned only records about the file.

## 3. Sources

Chosen before the search, following the week 4 module (slide 8) and the approved formalisation.

| Source | Role | Justification |
|---|---|---|
| Web of Science | Main | Multidisciplinary; named in the formalisation |
| IEEE Xplore | Main | Software engineering venues; named in the formalisation |
| ACM Digital Library | Main | Computing and SE conferences (ICSE, FSE); named in the formalisation |
| arXiv | Main (added) | SDD for agents emerged in 2025 and almost no peer-reviewed work exists yet; the evidence base relies on preprints and grey literature (Díaz et al., 2026). Preprints are flagged as not peer-reviewed and this is weighed in the quality assessment |
| Google Scholar | Snowballing only (backward and forward, one iteration, §4.2) | Complementary source, never the only one (week 4, slide 8) |

The formalisation names Scopus, Web of Science, IEEE Xplore and ACM DL as "main sources". Scopus is dropped: ISEP has no Scopus licence (checked 2026-11-04). For software engineering, Scopus mostly indexes IEEE and ACM venues, which are searched directly, and Web of Science covers the multidisciplinary side. This is stated as a limitation of the review. Adding arXiv is a justified extension.
Access: Web of Science only from the ISEP network or VPN (confirmed 2026-11-03).
The string for each database is generated by `slr/build_strings.py` and kept in `search-log.md` ("Strings v2 per database"). arXiv is searched through its API, because the web advanced search has no nested Boolean; this keeps one query per string.

**Documentary analysis (separate track, not part of the SLR).** Tool documentation and repositories are the object being characterised, not studies, so they do not enter the PRISMA flow, the IC/EC or the quality checklist.
For each candidate approach (from the SLR and from known approaches): official documentation and repository at a pinned version and access date; assessed with the 5W Information Source Evaluation Matrix (week 3: who, what, where, when, why; 1–5 each); characterised with the same extraction fields as RQ1. Both tracks feed the comparative framework (P7).

## 4. Selection criteria

Applied at title/abstract screening and again at full-text screening. Every exclusion is logged with the code of the criterion; the codes feed the PRISMA exclusion reasons.

**Inclusion (all must hold):**

| Code | Criterion |
|---|---|
| IC1 | The study addresses (a) SDD with coding agents [RQ1–RQ4], or (b) related context mechanisms (e.g. AGENTS.md, context files) with coding agents [RQ2–RQ4], or (c) the evaluation or comparison of coding agents on software development tasks [RQ2–RQ3] |
| IC2 | Published between 2023-01-01 and the search cut-off date |
| IC3 | Written in English |
| IC4 | Full text accessible |

**Exclusion (any one is enough):**

| Code | Criterion |
|---|---|
| EC1 | Only code completion or single-function generation (HumanEval style), with no agentic behaviour (multi-step, repository-level) |
| EC2 | "Specification" in the formal-methods or requirements-engineering sense, with no coding agents |
| EC3 | Editorial, keynote, poster, abstract only, or tutorial |
| EC4 | Earlier or duplicate version of an included study (the most complete version is kept, e.g. the published version over the arXiv preprint) |

Workshop and short papers are included: in a field this young much work appears there; rigour is handled by the quality assessment.
Secondary studies (reviews) are included: they are a source of approaches and gaps (RQ1, RQ4) and a starting set for snowballing. In the synthesis, evidence they report is not counted twice when the primary studies they cite are also included.

**Candidate criterion, decided before the protocol is frozen (not adopted at the pilot, 2026-11-05):** exclude group (c) studies whose main contribution is not the evaluation itself (a new agent tested on an existing benchmark). Adopted only if the pilot shows that S2 returns too many records of this kind; the decision and its reason are logged.

**Currency of included reviews.** For each included review: (1) record its own search cut-off date, so that later work it cannot cover is known; (2) forward snowballing (Google Scholar "Cited by") to find later reviews, comments or rebuttals; (3) check for retraction or withdrawal (publisher page, Crossref/Retraction Watch, latest arXiv version); (4) assess it with the DARE criteria recommended for secondary studies by Kitchenham & Charters (2007). Where a later review contradicts an earlier one, both are reported and the difference is discussed.

### 4.1 Second reviewer (conditional, D2a)

The review has a single reviewer, the author. This procedure applies only if a second reviewer is found by **2026-11-20**; otherwise it is removed (logged in the change log) and the single reviewer is reported as a threat to validity (§7).

| Item | Rule |
|---|---|
| Who | A person with a software engineering background (supervisor, MEI colleague or other), confirmed by the author. An AI system is never the second reviewer (week 4: eligibility decisions are not delegated to AI) |
| What is reviewed | (a) Title/abstract screening of **30 records**, drawn at random from the records that enter screening (after deduplication). (b) Optional, only if the reviewer has time: quality assessment (§5) and extraction (§6) of 2 included studies. Full-text screening has no second review |
| Effort asked | (a) about 1 hour, sent around 2026-11-20. (b) about 2–3 hours |
| Independence | The reviewer screens the 30 records in a separate Rayyan review with blind mode on, with title, abstract, keywords and the IC/EC sheet, and does not see the author's decisions. Before the sample, a 15-minute calibration on 5 pilot records (`pilot/`), which are excluded from the sample |
| Agreement | Cohen's kappa on include/exclude ("?" counts as include, since it goes to full text), plus percentage agreement. Target κ ≥ 0.61 ("substantial", Landis & Koch, 1977); the threshold is a convention and is stated as such |
| Below the target | Disagreements are discussed; the criterion that caused them is clarified (logged in the change log) and the author re-applies the clarified criterion to all screened records |
| Disagreements | Resolved by discussion; if unresolved, the record goes to full-text screening. Every decision is in the Rayyan export (CSV in `slr/`) |
| Sampling | Python `random.Random(seed).sample`, seed logged in `search-log.md`, as in the pilot |

AI may be used as an extra check only: screening the same sample and comparing it with the author's decisions. It is not counted in the kappa, the author's decision stands, and the use is logged in `doc/ai-usage.md`.

### 4.2 Selection procedure

Tools: Zotero holds the references; Rayyan (web screening tool) holds the screening decisions. Rayyan decisions are exported as CSV to `slr/` after each stage, so the PRISMA counts and the kappa (§4.1) are computed from files in the repository. Rayyan free plan (checked 2026-11-06): 3 active reviews, 2 invited reviewers, 1 sample; enough for the main screening, the second-reviewer sample (§4.1) and snowballing. Blind mode is not listed in the plan; to confirm in the review settings before 2026-11-20.

| Step | Rule |
|---|---|
| 1. Export | Each database and string exported (RIS or BibTeX) to `slr/exports/`, file name with database, string and date. Imported into Zotero, one collection per database. Records per database go to the PRISMA "identification" box |
| 2. Deduplication | Zotero duplicate detection, then Rayyan's duplicate check, then a DOI and title check. Between a preprint and its published version, the published one is kept (EC4). Duplicates removed are counted |
| 3. Pass 1: title | Exclude only when the title is clearly out of scope (another domain); any doubt goes to pass 2. Rayyan keyword highlighting may be used to read faster |
| 4. Pass 2: title, abstract, keywords | IC/EC applied (§4). Decision: include, exclude (with code) or maybe. Maybe goes to full text |
| 5. Index-term-only records | No automatic removal (pilot decision, `search-log.md`): screened like any other record; most fail IC1 |
| 6. Exclusion codes | The IC that fails (IC1–IC4) or the EC that applies (EC1–EC4), set as a Rayyan exclusion label. The pilot code OUT-SE becomes IC1 |
| 7. Full text | IC/EC applied again on the full text, with a code for every exclusion. Access tried through the publisher (ISEP), arXiv and Google Scholar; if none works, excluded under IC4 |
| 8. Snowballing | **One iteration** of backward (reference lists) and forward (Google Scholar "Cited by") snowballing on the studies included after full text, with the same criteria and codes. Not iterated to saturation as Wohlin (2014) recommends; stated as a limitation (§7). Counted in the PRISMA "other methods" branch |
| 9. AI | AI takes no screening decision (§4.1). Rayyan's relevance predictions are not used to decide; if used to order records, this is declared in `doc/ai-usage.md` |
| 10. Time-box | Title/abstract screening 2026-11-18 to 2026-11-20 (about 2.5 hours a day) |

## 5. Quality assessment

Quality is not a selection criterion: it does not exclude studies, it weighs the evidence in the synthesis (week 4: eligibility is not quality). What each study found goes to the extraction form (§6), not here.
Answers: Yes = 1, Partly = 0.5, No = 0, N/A when the question does not apply. Score = points / applicable questions (relative score, so conceptual and empirical studies can be compared).
Secondary studies are assessed with the DARE criteria instead (§4).

| # | Question | Applies to |
|---|---|---|
| | **Design** | |
| Q1 | Are the aims or research questions of the study clear? | All |
| Q2 | Is the method described in enough detail to be replicated? | All |
| Q3 | Are the agent, model and tool versions identified? | Empirical |
| Q4 | Are the tasks, project or benchmark described and available? | Empirical |
| | **Evaluation** | |
| Q5 | Is effectiveness measured against an independent criterion (acceptance tests, ground truth, expert review), not only the authors' judgement? | Empirical |
| Q6 | Are the metrics defined, and do they cover both cost and quality? | Empirical |
| Q7 | Is there a baseline or an alternative evaluated under the same conditions? | Empirical |
| Q8 | Is variability handled (repetitions, statistical analysis of differences)? | Empirical |
| Q9 | Do the conclusions follow from the results, including negative or mixed ones? | All |
| | **Credibility** | |
| Q10 | Are threats to validity and limitations discussed? | All |
| Q11 | Was it peer-reviewed? | All |
| Q12 | Are the authors independent of the vendor of the tool evaluated? | All |
| | **Feasibility** | |
| Q13 | Is the proposed approach feasible to implement in practice: its requirements (tools, compute, cost) are stated and within reach of a typical development team? | Conceptual studies and studies that propose an approach |

Q13 measures practical feasibility, not research rigour: an approach that needs very costly compute may be sound research but is of little use to the target audience of the decision guide (O5). This is stated when the score is used in the synthesis.

## 6. Data extraction form

One row per study. Every field exists because it answers an RQ (week 4, slides 7 and 15). Fields that do not apply are marked N/A. The form is piloted on 2–3 studies before the protocol is frozen (P4).

| Group | Fields | Serves |
|---|---|---|
| Identification | ID; reference; year; publication type (journal, conference, workshop, preprint); author affiliation; nature of the study: evaluates / compares / proposes an evaluation method / conceptual / review | All; Q11, Q12 |
| Approach | Name and version; artefacts prescribed; phases of the flow; human review points; SDD level (spec-first, spec-anchored, spec-as-source; Böckeler, 2025) | RQ1 |
| Context of application | Task type (new project or existing code base); size; domain; team profile | O5 (decision guide) |
| Measurement | Cost metrics (tokens, time, money); functional quality metrics (tests, resolve rate); internal quality metrics (maintainability, technical debt); human effort metrics; how they are collected (automatic or manual) | RQ2 |
| Evaluation (each configuration on its own) | One entry per configuration evaluated, judged on its own and not against the others. A configuration is one approach (or the baseline) run with one agent and one model, e.g. "Spec Kit + Claude Code + Sonnet". For each: success criterion used; metric values; verdict: works / partly / does not work | RQ4 |
| Comparison: design | Project or tasks; configurations compared; baseline; what is held constant (agent, model, operator, briefing); acceptance tests; number of repetitions; rules for human intervention | RQ3 |
| Comparison: result | Which configuration is better, on which dimension, by how much; is the difference significant | RQ4 |
| Comparison: did the method work | Did it distinguish the configurations; was it repeatable; limitations of the comparison method stated by the authors | RQ3 |
| Conclusions | Limitations and gaps stated by the authors | RQ4 |
| Quality | Q1–Q13 score, or DARE for reviews (§5) | Synthesis |

Tools and agents supported by each approach are not extracted from studies: they come from the documentary analysis (§3).

## 7. Synthesis plan

Synthesis by RQ, comparing patterns across studies rather than summarising study by study (week 4, slides 16–18). No meta-analysis: designs and metrics are too heterogeneous; narrative and tabular synthesis is used.

| RQ | Synthesis | Output |
|---|---|---|
| RQ1 | Table of approach × dimensions (artefacts, phases, review points, SDD level), merging the SLR and the documentary analysis. Starting dimensions: the six of Macedo (2026) and the levels of Böckeler (2025) | Comparative framework (P7) |
| RQ1, RQ4 | Evidence map: for each approach, number of studies that describe it, evaluate it and compare it; and a matrix of which approaches were compared with which. Frequency shows how much evidence exists, not which approach is better (slide 16) | Where evidence is concentrated or missing |
| RQ2 | Metrics grouped by category (cost, functional quality, internal quality, human effort) with how they are collected; counted and assessed for adequacy | Candidate metrics for O2 |
| RQ3 | Table of the design elements of comparative studies (project, baseline, what is held constant, repetitions), the threat each element controls, and whether the method worked | Design principles for the evaluation protocol |
| RQ4 | Results grouped by approach and dimension; convergent, divergent and mixed results set against each other; then the Evidence → Observation → Limitation → Gap → Opportunity chain (slide 18) | Research gap and contribution |

Cross-cutting rules:
1. Every claim states how many studies support it and their quality.
2. Sensitivity analysis: each conclusion is checked again using only studies with a quality score of at least 0.5 (half of the applicable questions met). A conclusion that holds only because of lower-scored studies is reported as weak evidence. The 0.5 threshold is a convention and is stated as such.
3. A conclusion that rests only on studies that were not peer-reviewed is flagged as such.
4. Threats to validity of the review are discussed: single reviewer (mitigated by a second reviewer on a sample if one is found, §4.1; full-text screening always single-reviewer), English only, young field with many preprints, unstable terminology (the strings may miss terms), Web of Science access, snowballing limited to one iteration (studies reachable only through a second or later iteration are missed).

## 8. Search cut-off date

The cut-off date is the day of the final search in all databases (planned 16–17 Nov 2026); the exact date is recorded in the search log.
Snowballing applies the same cut-off. A critical study published after the cut-off may be mentioned in the text as later work, outside the PRISMA flow. The formal search update is done in the dissertation.

## Protocol change log

| Date | Change | Reason |
|---|---|---|
| 2026-11-03 | Section 1 agreed with the author | First draft |
| 2026-11-03 | Section 2 agreed: blocks A1, A2, B, C, D; strings S1, S2 | Metrics block D and the A1/A2 split proposed by the author |
| 2026-11-03 | Section 3 agreed: four main databases plus arXiv; Google Scholar for snowballing only | Field too recent for peer-reviewed coverage alone |
| 2026-11-03 | Documentary analysis of tool documentation defined as a separate track (D3) | Documentation is the object, not a study; formalisation requires explicit quality criteria |
| 2026-11-03 | Section 4 agreed: IC1–IC4, EC1–EC4; reviews and workshop papers included; "main contribution" criterion left to the pilot | Author decided to keep all group (c) studies until the pilot shows the volume |
| 2026-11-03 | Section 5 agreed: Q1–Q13, relative score, peer review counted in the score | Author asked for a fuller evaluation block (Q5–Q9), vendor independence (Q12) and feasibility of conceptual proposals (Q13) |
| 2026-11-03 | Section 6 agreed: one row per study; evaluation of each configuration kept apart from comparison; context of application added; supported tools moved to the documentary analysis | Author separated "does the tool work" from "which is better" and "did the comparison method work" |
| 2026-11-03 | Sections 7 and 8 agreed: synthesis plan with evidence map and sensitivity analysis; cut-off at the final search | Author asked for counts of how often each approach was evaluated and compared |
| 2026-11-04 | Pilot search (P4) run on IEEE Xplore instead of Scopus | Scopus not accessible (eduVPN and b-on tried); the b-on discovery search is not Scopus and is not reproducible as a source |
| 2026-11-04 | Scopus dropped from the sources (§3) | ISEP has no Scopus licence; IEEE Xplore and ACM DL cover its SE venues; WoS keeps multidisciplinary coverage. Raised with the supervisor in email 1 |
| 2026-11-04 | Block B: "LLM-based agent*" restricted to a software engineering context, "autonomous agent*" added under the same condition; A2: "agent manifest*" added (strings v2 in `search-log.md`) | Pilot run 1: 162 of 207 S2 records entered only through "LLM-based agent*", mostly outside SE; "agent manifest" found in relevant abstracts |
| 2026-11-05 | Pilot inspection (P4): strings v2 kept, index-term-only records removed at screening; candidate group (c) criterion (§4) not adopted for now | Results and reasons in `search-log.md`, "Pilot inspection"; author re-evaluates the criterion before the freeze |
| 2026-11-06 | §4.1 added: conditional second reviewer (30-record screening sample, optional quality/extraction of 2 studies, kappa target 0.61); removed if no reviewer by 2026-11-20. AI never the second reviewer, only an extra check | D2a; week 4 "AI-assisted reviewing" slides. Author keeps the option to drop it; supervisor asked in person on 2026-11-09 |
| 2026-11-06 | Strings v2 written for Web of Science, ACM DL and arXiv (generated from §2 by `slr/build_strings.py`); arXiv via the API instead of split web queries (§3) | Same logic in every database; arXiv web search lacks nested Boolean. arXiv count test: S1 50, S2 1466 |
| 2026-11-06 | arXiv kept without category restriction (no `cat:cs.SE`) | A cs.SE restriction would drop 689 S2 records, and a random sample of them includes in-scope evaluation studies. Pilot totals before deduplication: S1 69, S2 1908. Decided by the author before the freeze, not after seeing screening results |
| 2026-11-06 | ACM DL searched in the ACM Guide to Computing Literature, not only the Full-Text Collection | Pilot: Guide S1 10 / S2 209 vs Full-Text 8 / 175. Wider coverage of other publishers partly compensates for Scopus |
| 2026-11-06 | §4.2 added: selection procedure (Zotero for references, Rayyan for screening with CSV exports to the repository; deduplication; two-pass title/abstract screening; exclusion codes; full text; one snowballing iteration). §4.1 uses a separate blind Rayyan review | Volume (about 1700 records after deduplication) and blind mode for the second reviewer; the author accepts one snowballing iteration as an explicit limitation |
