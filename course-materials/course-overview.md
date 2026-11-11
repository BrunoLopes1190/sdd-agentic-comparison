# PREPD 2026/27: course overview

Synthesis of every file in `course-materials/` (read in full on 2026-11-02). Each point names its source file.
**[F]** = documented fact. **[I]** = interpretation, not stated in any course document. **[S]** = stated by the student or supervisor, not in writing.
Update this file when new weekly materials are added.

## 1. Purpose

[F] Main goal: develop a work proposal that guides a complex Informatics Engineering project, integrating its scientific, technical, ethical and planning dimensions (`week-01/prepd-introduction-and-operation.md`, "Propósitos").

| Code | Course objective (summary) | Level |
|---|---|---|
| CO1 | Critically analyse an engineering problem: context, good practice, ethics | 5/6 |
| CO2 | Literature review: search, analyse, relate, synthesise; academic integrity | 6/6 |
| CO3 | Integrated, feasible plan: scope, activities, resources, schedule, cost, quality, risk, milestones, monitoring | 6/6 |
| CO4 | Coherent proposal: problem, objectives/RQs, existing knowledge, method, solution, evaluation, plan | 6/6 |
| CO5 | Written and oral communication with technical, scientific and ethical rigour | 5/6 |

[F] The curricular modules are not assessed on their own. They support the project (`prepd-introduction`, "Módulos curriculares").
[F] A proposal cannot be literature review only. It must include design and development (`general/faq.txt`, P13).

## 2. Calendar

| Date | Milestone | Source |
|---|---|---|
| 2026-10-09 | Proposal approved | [F] `general/important-deadlines.txt`; intro slide 10 |
| 2026-10-14 | Formalisation submitted | [F] same |
| 2026-10-24 | Formalisation review (RUC + reviewer) | [F] intro slide 10 |
| 2026-12-16 | Extended abstract, "Estudante (+ Orientadores)" | [F] same |
| 2027-01-06 | Final document (project delivery) | [F] same |
| 2027-01-04 to 01-09 | Assessment | [F] same |

Module schedule. [F] Labelled "Calendarização Provisória" (intro slide 6). [I] Week dates inferred from the SLR module dated 2026-10-06 (week 4).

| Week | Approx. dates [I] | Module (provisional) | Materials in repo |
|---|---|---|---|
| 1 | 14–18 Sep | Course objectives and operation | `week-01/` |
| 2 | 21–25 Sep | Project planning: project charter | `week-02/` |
| 3 | 28 Sep–2 Oct | Research methods (given here, not week 4) | `week-03/` |
| 4 | 5–9 Oct | Literature review / SLR (given here, not week 3) | `week-04/` |
| 5 | 12–16 Oct | Self-organisation: competencies | `week-05/` |
| 6 | 19–23 Oct | Ethics in research (T) and engineering (TP) | `week-06/` |
| 7 | 26–30 Oct | Technical-scientific writing | none; [S] no class was held |
| 8 | 2–6 Nov | Project planning: approaches, WBS | `week-08/` |
| 9 | 9–13 Nov | Project planning | none; [S] no class was held |
| 10 | 16–20 Nov | Self-organisation; [F] materials are project planning: schedule construction, WBS example, MS Project | `week-10/` (published 2026-11-11) |
| 11 | 23–27 Nov | Project planning | pending |
| 12 | 30 Nov–4 Dec | Project planning | pending |
| 13 | 7–11 Dec | (none) | pending |

## 3. Deliverables

| Deliverable | Content | Format | Weight |
|---|---|---|---|
| Formalisation | Form fields a) to k) (`week-01/formalization-form-en.md`) | Platform | Not graded [I] |
| Extended abstract | [F] Lets the course head (RUC) check five things: problem formulated and bounded; command of the state of the art; objectives and method coherent and feasible; realistic, structured work plan; ethical, professional and social implications considered. A positive answer justifies scheduling the final exam. Suggested structure (8 sections, about 4–5 pages): provisional title; introduction and problem, with stakeholders (~½ p); main RQ, sub-RQs, objectives, contributions (~⅓ p); systematised state of the art: search method, review questions, keywords, IC/EC, compared perspectives, explicit gap (~1–1.5 p); proposed method (~⅓ p); work plan to the PREPD document and to the thesis, with deliverables (WBS), milestones and a preliminary Gantt or timeline (~½ p); ethical and professional considerations: codes followed, personal data, human participants, confidential information, impacts, professional competencies (~½ p); 10–20 essential references, consistent style (~1 p). `general/extended-abstract-function.txt`, `general/extended-abstract-structure.txt`. [S] The supervisor reviews it until 15 Dec | PDF (format not stated) | Not graded; gate to the final exam [F] |
| Final document | Report assessed on the 8 document criteria (section 4) | ZIP with two PDFs: report + presentation (`general/dissertation-guidelines.md` p.1) | 75% |
| Oral exam | Presentation + discussion, online, synchronous | 30 min | 25% |

[F] Panel: chair, supervisor, examiner (intro slide 8). Supervisor and examiner each grade the sheet (`general/prepd-evaluation.xlsx`).
[F] Final grade = `ROUND(0.75 × document + 0.25 × presentation, 2)`, each part 0–20 (`prepd-evaluation.xlsx`, cell F29).
[F] Each item is rated 0 (not provided) to 5 (very good) and multiplied by 4. An alert fires if the two graders differ by more than 2 on an item (`prepd-evaluation.xlsx`, sheets "Evaluation" and "Data").
[S] The presentation lasts 10 minutes. The exam date will be announced at the end of December.

## 4. Assessment criteria

Weights from `general/prepd-evaluation.xlsx`. Guiding questions summarised from the "Notes" sheets and `general/dissertation-guidelines.md`.

### Document (75%)

| Item | Weight | What the graders ask |
|---|---|---|
| Background, context, rationale | 10 | Causes of the problem; deficiencies of current practice backed by sources; resource constraints |
| Analytical, critical, ethical interpretation of the problem | 10 | Stakeholders and interests; clear problem; societal impact; consequences of not solving; legal/social concerns; multiple perspectives; credible evidence |
| Objectives, research process, methods, questions | 10 | Clear objectives aligned with RQs; gap addressed; method fits RQs; feasible; limits stated; bias and validity threats; link to literature |
| State-of-the-art review | 20 | Review method identified and followed; maturity of sources; grey literature justified; critical comparison, not summaries |
| Ethical considerations | 10 | Compliance with an ethical board or code ("two are indicated at Moodle"); permissions; informed participants; privacy |
| Schedule of activities | 20 | Skills to develop and tasks for them; project charter elements reflected in the plan; scope by deliverables and phases aligned with the method; dates, durations, milestones, dependencies; cost if applicable; monitoring and control; risks identified, analysed, managed |
| Document structure | 5 | Chapters, abstract, ToC, references, lists of abbreviations, figures and tables; flow; every part linked to problem and objectives |
| Technical/scientific accuracy and writing | 15 | Alignment with title; no writing errors; sentences under ~30 words; consistent formatting and citation style |

### Presentation and discussion (25%)

| Item | Weight | What the graders ask |
|---|---|---|
| Quality of visual materials | 20 | Readable without zoom; slides paginated |
| Clarity and engagement | 20 | Natural delivery facing the camera; clear pace |
| Technical/scientific accuracy | 25 | No unexplained jargon |
| Conciseness (and coverage) | 10 | Within time, key aspects covered |
| Self-assurance and arguing | 25 | Clear, objective answers to the panel |

## 5. Methods taught, by part of the work

| Part | Method | Source |
|---|---|---|
| Research design | Oates (2005) process model: experiences/motivation, literature review, conceptual framework → RQs → strategy (survey, design and creation, experiment, case study, action research, ethnography) → data generation (interviews, observation, questionnaires, documents; also logs, repository mining, benchmarks, simulation) → quantitative/qualitative analysis | `week-03/research-methods-t.md` slides 4–23 |
| Research process figure | Template to "illustrate your research process", highlighting chosen strategies and methods | `week-03/research-process-figure.pptx` |
| Research questions | Shaw (2002) RQ types; focus from area → topic → question; TP activity: 1–2 RQs, how to answer, analyse, expected results | `research-methods-t.md` slides 7–11; `week-03/research-methods-tp.pdf` slide 2 |
| Sources | Primary/secondary/tertiary; maturity scale; citation counts and caveats; JCR, SJR, CORE; GenAI hallucination risks | `research-methods-t.md` slides 25–59 |
| Source evaluation | Information Source Evaluation Matrix (5W: who, what, where, when, why; 1–5 each, max 25) | `week-03/source-evaluation-matrix.docx`; `information-source-evaluation-matrix.md` |
| Libraries and tools | RECIPP, B-On, ACM DL, IEEE Xplore, DBLP, arXiv; reference manager (Zotero etc.) | `week-03/research-methods-tp.pdf` slides 3–6; `search-activities-tp.pdf` |
| Literature review | Three levels: narrative review, structured state of the art, SLR. "A Master's dissertation can have a rigorous, systematised State of the Art without claiming to be a full SLR" | `week-04/systematic-literature-review-v1.md` slides 8, 11 |
| SLR process | Kitchenham & Charters (2007), Okoli (2015), PRISMA 2020, Wohlin (2014) snowballing. RQs → concept blocks + synonyms → Boolean string → justified databases (Scopus, WoS, IEEE, ACM; Google Scholar complementary; Google only for justified grey literature) → pilot → search log → dedup → title/abstract → full text → quality assessment → extraction matrix → synthesis by RQ → Evidence → Limitation → Gap → RQ → Contribution | `systematic-literature-review-v1.md` slides 12–28; `week-04/slr-mini-tutorial.md` |
| SLR outputs | Protocol, search log, screening log, quality assessment, extraction matrix, PRISMA, synthesis by RQ, limitations, research gap | `slr-mini-tutorial.md` slide 20 |
| AI in the review | AI may support synonyms, query critique, prioritisation, extraction drafts. It must not make eligibility decisions, supply unverified references or claim gaps | `systematic-literature-review-v1.md` slides 29–31 |
| Project charter | Stakeholders (power × interest), scope, objectives, benefits, deliverables, milestones, costs, assumptions, restrictions, risks (cause, effect, response); success metrics, governance, exit conditions | `week-02/project-charter-v1.md`; `project-charter-template-v01.docx` |
| Planning approach | Predictive, adaptive or hybrid, with pros and cons | `week-08/planning-approach-v1.md` |
| WBS | Deliverable-oriented tree, structured by life-cycle phase; 100% rule; one decomposition criterion per level; terminal tasks 8–80 h; dictionary with acceptance and progress criteria | `week-08/wbs-concepts-v01.md`; `wbs-template-v01.pptx` |
| WBS example | A dissertation WBS by life cycle: 1.1 Planning (project charter, WBS, plan), 1.2 Design, 1.3 Build, 1.4 Evaluate, 1.5 Conclusions (final report, final presentation); level 1 = phases, below = deliverables, then tasks. The same WBS becomes the MS Project schedule: WBS code and level (project, phase, deliverable, task, milestone) per row, durations, predecessors, and a "Milestones" summary of 0-day tasks (e.g. plan delivered, report v0.1 delivered, final report delivered, presentation date) | `week-10/wbs-example-v01.md` (slides 3–4 are images: Gantt charts read from the PDF on 2026-11-11) |
| Schedule | Logic network (sequenced terminal WBS tasks; AON/PDM, four dependency types, lags and leads; mandatory, external or optional dependencies) as the base for dates; estimates by the people doing the work, with a reserve: analogy, bottom-up from the WBS, parametric, three-point (PERT = (O+4M+P)/6, SD = (P−O)/6); milestones and deadlines; project, resource and task calendars; critical path method, free and total slack, negative slack; crashing and fast tracking; resources (work, material) for cost; baseline saved before execution, re-baselined only on approved change, rolling-wave detail or an unrealistic plan. Tool: MS Project 2019 or later, English version preferred, from the ISEP MSDN Academic Alliance | `week-10/schedule-construction-v1.md`; `ms-project-installation-v01.md`; `example-project-code-design-part-1.mpp` (MS Project file, not extracted) |
| Competencies | Self-diagnosis (importance + level) and hetero-assessment by a peer; at least 3 key competencies with objectives; at least 2 actions each; strategies and metrics | `week-05/competencies.pdf`; `self-assessment.docx`; `assessment.docx` |
| Research ethics | Misconduct (fabrication, falsification, plagiarism); bias; ALLEA European Code of Conduct (2023); P.PORTO Code (Despacho 11171/2020), arts. 6, 8, 10; GDPR; FAIR data; company work; GenAI rules | `week-06/t06.md`; `european-code-of-conduct-2023.pdf` |
| Engineering ethics | NSPE, ACM, ACM/IEEE-CS SE codes; "choose one code and follow it, not selectively"; 5-step ethical decision method; licences; EU law (AI Act, CRA, GDPR) | `week-06/tp06.pdf`; `codes-of-ethics.txt`; `additional-resources-law.txt` |
| GenAI declaration | Section "Use of AI-generated content": systems, parts, nature and extent; editing/grammar exempt. T06 adds: tool version; agree use with supervisors task by task; hiding AI use is misconduct | `general/ai-generated-content-guidelines.txt`; `t06.md` slides 43–44 |
| Document template | Harvard (author, date) citations; Calibri 11, 1.5 spacing; abstract ≤ 200 words; ≤ 6 keywords; an English thesis needs a Portuguese extended abstract ≤ 1000 words; 60–120 pages (dissertation) | `general/tmdei-2425-dissertation-template.dotx` |

## 6. Contradictions, gaps and ambiguities

| # | Issue | Sources | Status |
|---|---|---|---|
| 1 | Presentation 5 min + 25 debate vs 10 + 20 | intro slide 8 vs `dissertation-guidelines` p.1 | [S] 10 min confirmed |
| 2 | "100% of the grade" vs 75/25 split | intro slide 8 vs `.xlsx` F29 | [I] Same exam, two components |
| 3 | Assessment may start 2027-01-04; final document due 2027-01-06 | intro slide 10 | [S] Exam date announced end of December |
| 4 | Extended abstract content, length and weight undefined | all | Resolved 2026-11-04: function and structure in `general/extended-abstract-function.txt`, `general/extended-abstract-structure.txt`; not graded, gate to the final exam. Language still open |
| 5 | PREPD document length and template not fixed; the `.dotx` is the dissertation template | `.dotx` | [I] Use the template structure |
| 6 | Template requires Harvard citations; `doc/build.ps1` uses `ieee.csl` | `.dotx` vs repo | Open (see `planning/prepd-work-plan.md`) |
| 7 | "Two ethics codes indicated at Moodle"; `codes-of-ethics.txt` lists three | `.xlsx` notes vs `codes-of-ethics.txt` | Minor |
| 8 | Module order and lecturers differ from the provisional schedule | intro slide 6 vs materials | Minor |
| 9 | P.PORTO Code art. 10 requires ethics committee review "as required by law" for research on autonomous systems, "in particular when using AI" | `t06.md` slides 23–24 | Relevant to this project |

## 7. Files whose content is partly image-only

Text was not extracted from: the `week-10/schedule-construction-v1` slides "Ciclo de vida do projeto" and "Elementos a adotar" and the network figures; `week-10/example-project-code-design-part-1.mpp` (open in MS Project); the `tp01.pdf` platform screenshots; `research-methods-t` slides 32 and 37; `systematic-literature-review-v1` slides 9 and 19; the stakeholder-examples and life-cycle figures in `project-charter-v1` and `wbs-concepts-v01`. Check the PDF if those slides matter.
