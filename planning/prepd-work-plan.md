# PREPD work plan

Created 2026-11-02. What must be produced in PREPD, mapped to the methods taught and to the deadlines.
Course facts and sources: `course-materials/course-overview.md`. Current status: `admin/context.md`.
**[F]** = documented fact. **[I]** = interpretation. **[S]** = stated by the student or supervisor.

## 1. Principle

PREPD prepares the dissertation. It does not run it.
In PREPD, the scope, method and plan are fixed and the state of the art is done.
The experiment, the reference project and the choice of agents and models belong to the dissertation (2nd semester).
[S] The supervisor asked for the course to be done following the classes. Every product below names the class it comes from.

## 2. Milestones

The milestones are the commitments. Day-by-day dates inside a milestone are guidelines only.
Note: the exam window (4–9 Jan) starts before M7. Exam scheduling is the course's responsibility; no action planned.

| # | Date | Milestone | Done when | Status |
|---|---|---|---|---|
| M1 | 2026-11-04 | Email 1 to the supervisor | Sent with the work ready at that moment and the assumptions to confirm (§2.1) | Done 2026-11-04 |
| M2 | 2026-11-16 | Email 2: everything up to week 9 done; feedback and meeting requested; all open questions (§6) | P1–P4, P8–P11, P13 done, no week 9 classes; SLR protocol frozen (done 11 Nov). P11 (WBS) is the first item to move to M3 if time runs short | In progress |
| M3 | 2026-12-01 | Email 3: supervisor's corrections applied, plus the work from the later classes | M2 feedback applied; weeks 10–11 class work; SLR search, screening and synthesis (P5–P7); P12 draft | Not started |
| M4 | 2026-12-13 | Extended abstract draft sent to the supervisor | [S] He reviews it until the 15th | Not started |
| M5 | 2026-12-16 | Extended abstract submitted | [F] Fixed (intro slide 10). [F] Not graded, but a positive review justifies scheduling the final exam (`general/extended-abstract-function.txt`) | Not started |
| M6 | 2027-01-02 | Draft of the whole document and slides sent to the supervisor | Full draft of P16 and P17 | Not started |
| M7 | 2027-01-06 | Everything done: ZIP with two PDFs (report + presentation) submitted | [F] Fixed | Not started |
| — | 2027-01-04 to 01-09 | Oral exam, 10-min presentation | [F] Fixed; [S] date announced end of December |

### 2.1 Email 1 to the supervisor (4 Nov)

The supervisor may not reply in time. One email, sent early, carries everything that needs his view.
Each question states the student's current assumption and asks for the supervisor's opinion on it.

**Preparation, 3–4 Nov (guideline):**

| Day | Prepare | Product | Goes in the email as |
|---|---|---|---|
| 3 Nov | Review RQs, concept blocks and synonyms, Boolean string, databases with justification, IC/EC | P3 (draft) | Attached protocol draft (1–2 pages) |
| 3 Nov | Quality checklist and extraction fields | P3 (draft) | Part of the protocol draft |
| 4 Nov | Pilot search on Scopus (institutional login): number of hits, 20–30 records inspected, terms added; logged in `slr/search-log.md` | P4 | One paragraph with numbers |
| 4 Nov | Position on P.PORTO art. 10: no human participants or personal data; agents run on a synthetic project in an isolated folder; proposed answer "no ethics committee review needed", to confirm | P13 (draft) | One paragraph |
| 4 Nov | Proposed decisions D2a, D4, D5, D7 and the extended abstract outline (§4, "Proposed structure") | §3, §4 | Numbered list of proposals |
| 4 Nov | Planned dates (§2) | §2 | Short timeline |

The protocol draft is kept in `slr/protocol.md`.

**Scope rule:** the email goes on 4 Nov with whatever is ready at that moment. No step is shortened to fit the email; unfinished parts are named as in progress. The email must not be questions only.

**Email structure:** short status (formalisation submitted, plan); the work done so far (protocol draft, pilot results, or the parts that are ready); numbered questions from §6, each presented as the student's assumption with a request for the supervisor's opinion; whether he wants access to the GitHub repository; the milestones (§2), announcing email 2 on 15 Nov with a meeting request.

**No reply (internal rule, not stated in the email):** work continues on the stated assumptions. Questions still open are raised again in emails 2 and 3. Late feedback is applied as a logged protocol change.

The same scope rule applies to emails 2 and 3: they go on the milestone date with what is ready, and unfinished parts are named as in progress.

### 2.2 Path to M2 (5–16 Nov, guideline)

| Days | Work | Class |
|---|---|---|
| 5–6 | Finish the SLR protocol draft; set up Zotero + Better BibTeX; create the Rayyan account (check free-plan limits and that blind mode is included) | Week 4 |
| 7–8 | No work (unavailable) | — |
| 9 | Competencies: self-assessment and action plan (~2–2.5 h; hetero-assessment on hold, to discuss with the supervisor); ask the supervisor about the second reviewer; start the research design | Weeks 5 and 3 |
| 10 | Done 11 Nov. Research design: Oates figure, validity threats (sub-RQs done 9 Nov). On the computer with Pandoc: run `doc/build.ps1`; move the References section out of `01-introduction.md` into `99-references.md` | Week 3 |
| 11 | Done 11 Nov. Pilot the extraction on 2–3 papers; freeze the protocol (with any supervisor reply). Week 10 materials added to the course overview | Weeks 4 and 10 |
| 12 | Done 12 Nov. Stakeholders (power × interest) and problem interpretation (P8 done); project charter sections 1–6 | Week 2 |
| 13 | Project charter sections 7–10 (assumptions, restrictions, risks, approval); ethics (one code, art. 10, licences, data); install MS Project, step by step below | Weeks 2, 6 and 10 |
| 14 | Planning approach, WBS by life cycle (first to cut), in the form of the week 10 example | Weeks 8 and 10 |
| 16 (Mon) | Email 2 with a meeting request; all open questions of §6 | — |

**MS Project installation (13 Nov), step by step** (from `course-materials/week-10/ms-project-installation-v01.md`):

1. Go to https://moodle.isep.ipp.pt/ and open "MSDN Academic Alliance".
2. Find Microsoft Project 2019 or later (2021 may be needed, depending on the installed Office). Prefer the English version.
3. If MS Project is not listed: validate the student account, enter the profile and the school, then the profile details; it then appears for download.
4. Download and install.
5. Back on the portal, get the product key and enter it in MS Project, so it is the licensed version and not the trial.
6. Open MS Project and check that it is activated.
7. Open `course-materials/week-10/example-project-code-design-part-1.mpp` to check that it works.
8. Confirm the licence source in the charter cost table (`doc/chapters/07-work-plan.md`).

### 2.3 Path to M3 (16 Nov – 1 Dec, guideline)

| Days | Work |
|---|---|
| 16–17 | Apply supervisor feedback; final search on all databases; export to Zotero; search log |
| 17–18 | Deduplication |
| 18–20 | Title/abstract screening with reasons; sample to the second reviewer |
| 21–23 | Full-text screening; backward/forward snowballing; PRISMA diagram |
| 24–27 | Quality assessment and extraction of every included study |
| 28–29 | Synthesis by RQ, gap, comparative framework (with the tool documentation analysis) |
| 30 | Schedule (Gantt) draft for Feb–Jun 2027 in MS Project, built from the WBS (week 10: logic network, three-point estimates, critical path, milestones as 0-day tasks, baseline) |
| Throughout | Week 11 class work (week 10 work goes into P11 and P12) |
| 1 Dec | Email 3; announces the extended abstract draft for 13 Dec |

Corpus size is unknown until the pilot search (M1). Fallback: email 3 reports the SLR as far as it got; synthesis is finished before M4. A supervisor meeting during this phase may change the protocol; changes are logged.

### 2.4 Path to M4 and M5 (2–16 Dec, guideline)

| Days | Work |
|---|---|
| 2–6 | Week 12 class work; apply feedback on email 3; finish the SLR if anything is left |
| 2–8 | Complete the planning: final schedule, cost estimate, risk register, monitoring and control |
| 7–11 | Week 13 class work; write the extended abstract in the published structure (§4, "Extended abstract structure") |
| 12–13 | Review (sentences under 30 words; every reference exists and was read); send the draft (M4) |
| 14–15 | Apply supervisor feedback, if any |
| 16 | Submit (M5) |

The extended abstract is the first time the separate products are written as one text; allow time for it.

### 2.5 Path to M6 and M7 (17 Dec – 6 Jan, guideline)

| Days | Work |
|---|---|
| 17–23 | Write the full document from the extended abstract, following the proposed structure (§4) |
| 24–26 | Break |
| 27–30 | Finish the document: "Use of AI-generated content" section from `doc/ai-usage.md`; lists of figures, tables and acronyms. The exam date is announced |
| 30 Dec – 1 Jan | 10-min slides: 8–10 slides, paginated, readable without zoom |
| 2 Jan | Draft of the document and slides to the supervisor (M6) |
| 3–5 | Apply feedback, if any; final review (short sentences, consistent citations, every reference checked) |
| 6 Jan | Submit the ZIP with two PDFs (M7) |
| Until the exam | Rehearse: time the 10 minutes; prepare answers to likely questions (arguing is 25% of the presentation grade) |

## 3. Decisions taken for PREPD

| # | Decision | Basis | Status |
|---|---|---|---|
| D1 | The approved formalisation (2026-10-14, with citations; `admin/formalizacao_1240441.pdf`) is the reference text for title, problem, objectives and RQ | [S] | Taken |
| D2 | State of the art = **full SLR** (Kitchenham & Charters 2007): protocol written and frozen before the search, changes logged; reproducible search; IC/EC; formal quality assessment of every included study; extraction form piloted; PRISMA 2020; synthesis by RQ; threats to validity of the review | [S] student's choice; `week-04/systematic-literature-review-v1.md` slides 8, 11–22; formalisation field f | Taken |
| D2a | Single-reviewer mitigation [I]: a second person (supervisor or a colleague) independently screens a random sample of records and assesses a sample of included studies; agreement measured (Cohen's kappa); disagreements resolved and logged | Kitchenham & Charters (2007) | Conditional (`slr/protocol.md` §4.1): 30-record screening sample; dropped if no reviewer by 2026-11-20. In-person meeting of 2026-11-09 at risk; no reply to email 1; question text prepared 2026-11-09; supervisor not reached by 10 Nov, so it goes in email 2 (16 Nov) |
| D3 | arXiv preprints are an SLR source, justified by the field's age. Tool documentation, repositories and practitioner articles are **not** SLR studies: they are analysed separately, with a documented procedure and the 5W matrix, as input to the comparative framework (RQ1) | `week-03/source-evaluation-matrix.docx`; grading question on grey literature | Taken 2026-11-03 (no need to ask the supervisor; justified in `slr/protocol.md` §3) |
| D4 | Citation style author-date (Harvard), as in the template and the submitted formalisation; `doc/ieee.csl` to be replaced | `.dotx`; formalisation | Proposed; confirm with the supervisor |
| D5 | PREPD document follows the template structure (front matter, lists, references) | `.dotx`; grading item "Document structure" | Proposed |
| D6 | No supervisor-imposed restriction on GenAI; all use is logged in `doc/ai-usage.md` and declared in the document | [S]; `ai-generated-content-guidelines.txt` | Taken |
| D7 | Experimental runs, when they happen (dissertation), may only use the student's personal Claude Pro plan; there is no token budget. Proposed 2026-11-04: also open models run locally (e.g. Ollama), limited by the available hardware | [S] | Constraint (see §7); local models proposed in email 1 |

## 4. Products and the method each one comes from

| # | Product | Method / class | Feeds grading item | Due | Status |
|---|---|---|---|---|---|
| P1 | Competency self-diagnosis + hetero-assessment by a colleague; ≥ 3 key competencies with objectives; ≥ 2 actions each, with metrics | Week 5: `competencies.pdf`, `self-assessment.docx`, `assessment.docx` | Schedule (20) | M2 | In progress (self-assessment and action plan done; hetero-assessment on hold) |
| P2 | Research design: main RQ (formalisation) + sub-RQs typed by Shaw; Oates process figure (strategies: design and creation + experiment; data: documents, observation, logs; analysis: quantitative + qualitative); validity threats and bias controls | Week 3: `research-methods-t.md`, `research-process-figure.pptx`, TP activity I | Objectives/method (10) | M2 | Done 2026-11-11 |
| P3 | SLR protocol (frozen before the search): review RQs, concept blocks and synonyms, string per database, databases and justification, search cut-off date, IC/EC, quality assessment checklist, extraction form, synthesis plan, second-reviewer procedure (D2a), protocol change log | Week 4: SLR module + mini-SLR tutorial; Kitchenham & Charters (2007) | State of the art (20) | Draft M1; frozen M2 | Done 2026-11-11 (frozen) |
| P4 | Pilot search on one database (inspect 20–30 results); pilot the extraction form; refine and log changes; then freeze the protocol | Week 4: tutorial slide 20, steps 1–2 | State of the art | Search M1; extraction pilot M2 | Done 2026-11-11 |
| P5 | Final search on all databases; exports; search log (query, date, filters, n); deduplication; title/abstract and full-text screening with reasons; second-reviewer sample and kappa; backward/forward snowballing; PRISMA 2020 diagram | Week 4; Wohlin (2014); Page et al. (2021) | State of the art | M3 | Not started |
| P6 | Quality assessment of every included study; extraction matrix; critical synthesis by RQ; Evidence → Limitation → Gap → RQ → Contribution chain; threats to validity of the review | Week 4: slides 22–28 | State of the art; Background (10) | M3 | Not started |
| P7 | Preliminary comparative framework of SDD approaches, from the SLR plus the documented analysis of tool documentation (D3) (RQ1 / O1) | Week 4 synthesis; Macedo (2026) dimensions | State of the art | M3 | Not started |
| P8 | Stakeholder analysis (power × interest) and problem interpretation from several perspectives | Week 2 charter; grading notes | Problem interpretation (10) | M2 | Done 2026-11-12 |
| P9 | Project charter for the dissertation | Week 2: `project-charter-template-v01.docx` | Schedule (20) | M2 | In progress |
| P10 | Planning approach (predictive / adaptive / hybrid) with justification | Week 8: `planning-approach-v1.md` | Schedule | M2 | Not started |
| P11 | WBS by life-cycle phase aligned with the research method, plus WBS dictionary (acceptance and progress criteria) | Week 8: `wbs-concepts-v01.md`, `wbs-template-v01.pptx`; week 10: `wbs-example-v01.md` (phases → deliverables → tasks) | Schedule | M2 | Not started |
| P12 | Schedule (Gantt) Feb–Jun 2027 in MS Project: logic network, three-point (PERT) estimates, dependencies, critical path and slack, milestones as 0-day tasks, baseline; cost from resources; risk register; monitoring and control | Week 10: `schedule-construction-v1.md`, `wbs-example-v01.md`, MS Project; weeks 11–12 pending; grading notes | Schedule | Draft M3; final M6 | Not started |
| P13 | Ethics: chosen code (one, applied in full); ALLEA principles; position on P.PORTO art. 10; licences and terms of the tools; FAIR data plan; conflicts of interest; GenAI use | Week 6: `t06.md`, `tp06.pdf` | Ethics (10) | M2 | In progress |
| P14 | "Use of AI-generated content" section, from `doc/ai-usage.md` | `ai-generated-content-guidelines.txt` | Accuracy; Ethics | M4, M6, M7 | Not started |
| P15 | Extended abstract | `general/extended-abstract-structure.txt`; condensed P1, P2, P6–P9, P11–P13 | Gate to the final exam (`general/extended-abstract-function.txt`) | Draft M4; submitted M5 | Not started |
| P16 | Final PREPD document | All of the above | All document items | Draft M6; final M7 | Not started |
| P17 | 10-min slides, paginated, readable; rehearsed with Q&A | Grading sheet "Presentation" | Presentation (25%) | Draft M6; final M7; rehearse before the exam | Not started |

P1, P2 and P8–P13 are written as chapters in `doc/chapters/` (decided 2026-11-09), so they feed P15 and P16 directly.
Planning outputs P10–P12 are refined as the week 10–12 materials arrive (no classes in week 9). Add each new module's method to this table.

### Extended abstract structure [F]

From `general/extended-abstract-structure.txt` (published 2026-11-04). About 4–5 pages. Each section names the products it condenses.

| # | Section | Length | Content | From |
|---|---|---|---|---|
| 1 | Provisional title | — | Clearly bounded topic, not generic | Formalisation (D1) |
| 2 | Introduction and problem | ~½ p | Domain context; relevance; precise bounds; research problem; main stakeholders | P8 |
| 3 | Research questions and objectives | ~⅓ p | Main RQ and sub-RQs; concrete, verifiable objectives; contributions | P2 |
| 4 | State of the art (systematised) | ~1–1.5 p | Search process (method, review questions, keywords, IC/EC); main approaches compared, not lists of authors; explicit gap. May come after the method | P3–P7 |
| 5 | Proposed method | ~⅓ p | Research or engineering strategy; data sources; analysis techniques; feasibility | P2 |
| 6 | Work plan | ~½ p | Tasks up to the PREPD document; up to the thesis: deliverables (WBS), milestones, preliminary Gantt or timeline | P9–P12 |
| 7 | Ethical and professional considerations | ~½ p | Codes followed and how; personal data, human participants, confidential information, impacts (or why none); how professional competencies are ensured | P13, P1 |
| 8 | References | ~1 p | 10–20 essential, current references from the state of the art; scientific papers and books, not web generalities; one consistent style | P6 |

The course head uses it to check five points: problem bounded; command of the state of the art; objectives and method coherent and feasible; realistic work plan; ethical and professional reflection (`general/extended-abstract-function.txt`).

### Proposed structure of the PREPD document [I]

Mapped to the grading items. To confirm against the week 9–13 materials and with the supervisor.

1. Front matter: abstract, keywords, ToC, lists of figures, tables and acronyms.
2. Introduction: context, problem, stakeholders, objectives, RQs, expected contributions.
3. Research method: Oates figure, strategies, data, analysis, validity threats.
4. State of the art: review method, results (PRISMA), synthesis by RQ, comparative framework, gap.
5. Proposed solution and evaluation design: what will be built and how it will be evaluated, at the level bounded in §5.
6. Ethical considerations.
7. Work plan: charter elements, planning approach, WBS, schedule, cost, risks, monitoring and control, competency plan.
8. Use of AI-generated content.
9. References.

## 5. What is bounded now vs. left to the dissertation

| Topic | Bounded in PREPD | Left to the dissertation |
|---|---|---|
| Problem, objectives, main RQ | Fixed (submitted formalisation) | — |
| Sub-RQs and review RQs | Defined | — |
| Research method | Strategies, data generation, analysis, validity threats | Detailed experimental procedures |
| State of the art | Full SLR done, with a documented cut-off date | Update search before writing the dissertation |
| SDD approaches | Candidate list and inclusion criteria from the review | Final selection and versions to pin |
| Agents and models | Constraint stated (D7); the choice is a recorded factor | Choice |
| Reference project | Required characteristics (proposal §7.1) | Design, briefing, acceptance tests, build |
| Metrics | Dimensions (cost, functional and internal quality, conformance, human effort) | Final metrics, definition of "total cost", main metric |
| Conditions and repetitions | Design principles (baseline, same briefing, fixed tests) | Number of conditions and repetitions |
| Experiment runs | None | All, outside this repo (`experiment/protocol.md`) |
| Decision guide (O5) | How it will be built and evaluated | Production |
| Plan | Full plan for Feb–Jun 2027 | Monitoring and re-planning |

## 6. Open questions for the supervisor

Sent in email 1 (§2.1), each with the student's assumption. Questions still open are repeated in emails 2 and 3.

1. Full SLR (D2): who can act as second reviewer for the sample (D2a; about 1 h, 30 abstracts, around 20 Nov)? May it be someone outside MEI? Supervisor not reached in person by 10 Nov; asked in email 2 (16 Nov). The protocol was frozen on 11 Nov on the current assumptions; any later comment is applied as a logged protocol change.
2. P.PORTO Code art. 10 (autonomous systems using AI): is ethics committee review required for experiments with coding agents and no human participants?
3. Citation style and template for the PREPD document (D4, D5); page limit?
4. Extended abstract format. Asked in email 1 with the assumption "up to 1000 words or 2 A4 pages". Structure and length answered by the course on 2026-11-04 (§4, about 4–5 pages). Still open: language.
5. Experiments limited to a personal Claude Pro plan (D7), plus open models run locally (e.g. Ollama): acceptable, given that it constrains the agents that can be tested?
6. Does the supervisor want access to the repository, to follow the work? (Not asked in email 1; ask in email 2.)
7. Scopus: ISEP has no licence, so it was dropped from the SLR sources (IEEE Xplore and ACM DL cover its SE venues; WoS stays). Does the supervisor agree, or know of legitimate access through ISEP?
8. Project charter benefits (P9): B1–B3 go to the teams adopting SDD. Should the charter also list a benefit for the student (degree and the three key competencies)? Removed on 2026-11-12 until the supervisor answers (email 2).
9. Fixed dates of the dissertation (submission and defence) for the charter and the schedule: not yet known (email 2).

## 7. Risks for PREPD

| Risk | Cause | Impact | Response |
|---|---|---|---|
| Full SLR not finished by M3 (1 Dec) | Searches not started; no full paper read yet; full SLR adds quality assessment and a second reviewer | Weak extended abstract; 20% item at risk | Freeze the protocol by M2; time-box screening; cut-off date; if late, report the SLR up to full-text screening in the extended abstract and finish synthesis for the final document |
| Supervisor does not reply in time | Availability | Decisions stall | Email on 4 Nov stating assumptions; work continues on them; feedback logged as changes (§2.1); if there is still no reply, talk to him in person |
| No second reviewer available | Single student | Reduced reliability of the SLR | Ask in email 1 (§6 Q1) and again in email 2 (16 Nov); if none by 20 Nov, drop §4.1 of the protocol and state it as a threat to validity |
| Formal databases return few hits | Most SDD work is arXiv or grey literature | Thin PRISMA corpus | Include arXiv and grey literature by protocol (D3), justified |
| Planning chapter depends on modules up to week 12 (ends ~4 Dec, after M3) | Course calendar | 20% item done in a rush | Draft P9–P11 by M2; week 12 work goes into M4–M6 |
| Christmas break between 16 Dec and 6 Jan | Calendar | Less supervisor feedback on the M6 draft | Get the main feedback on emails 2 and 3 and on the M4 draft |
| Field changes weekly | New preprints and tool versions | State of the art goes stale | Explicit cut-off date; update in the dissertation |
| Extended abstract judged insufficient | It is the gate to the final exam (`general/extended-abstract-function.txt`) | No exam scheduled | Follow the published structure; supervisor review by 15 Dec; WBS (P11) and preliminary Gantt (P12) must exist by M4, since section 6 needs them |
| Single vendor for runs and for the writing assistant | D7; Claude used to assist this work | Perceived conflict of interest; agent choice constrained | Declare in the ethics section; record the agent as a factor |
| Pro plan usage limits; no per-token cost visible | D7 | "Total cost" hard to measure; fewer runs | Define a cost proxy in the dissertation; state as a limitation |
| Over-reliance on AI | Heavy assistant use | Misconduct; weak oral defence | Follow the SLR-module rules on AI use; read every source; log use |

## 8. Progress log

How to track progress: when an item starts or finishes, update its Status above (`Not started`, `In progress`, `Done YYYY-MM-DD`, `Moved to Mx`) and add one line here. Then regenerate the HTML view: `python planning/build_plan_html.py`.

| Date | What was done | Items |
|---|---|---|
| 2026-11-02 | Course materials analysed; course overview and this plan written and reviewed with the student, point by point | — |
| 2026-11-03 | Approved formalisation (`admin/formalizacao_1240441.pdf`) set as the reference text; SLR protocol draft started | P3 |
| 2026-11-03 | SLR protocol draft written (`slr/protocol.md` §1–8: RQs, strings, sources, IC/EC, quality, extraction, synthesis, cut-off); D3 taken. Pending: per-database strings (pilot), second reviewer (D2a) | P3 |
| 2026-11-04 | Pilot search on IEEE Xplore (Scopus not licensed at ISEP; dropped from the sources). Strings v2: "LLM-based agent*" restricted to SE context, "agent manifest*" added; S2 209 → 146. Open: manual inspection of 20–30 records; SE terms restricted to title/abstract at the freeze. Log in `slr/search-log.md` | P3, P4 |
| 2026-11-04 | Ethics position on P.PORTO art. 10 drafted (no ethics committee review proposed) and sent in email 1 | P13 |
| 2026-11-04 | Email 1 sent with the protocol draft (PDF), pilot results, ethics position and questions 1–5 and 7 of §6 (text in `planning/emails/`). Not sent: repository access, timeline, meeting request, who the second reviewer is; to raise in email 2 | M1 |
| 2026-11-04 | Extended abstract function and structure published by the course: plan updated (§4 structure table, M5, P15, §6 Q4, risks). It is a gate to the final exam; the WBS and a preliminary Gantt are needed by M4 | P15 |
| 2026-11-05 | Pilot inspection on IEEE Xplore: 20 records (7 S1, 13 S2, random, seed logged) judged by the author; precision S1 100%, S2 54%, total 70%. Decided: strings v2 kept (no v3), index-term-only records removed at screening; candidate group (c) criterion not adopted for now. Pending for P4: extraction form pilot, freeze. Log in `slr/search-log.md` | P4 |
| 2026-11-06 | Second-reviewer procedure (D2a) written as conditional `slr/protocol.md` §4.1: 30-record screening sample, kappa target 0.61, AI only as an extra check; dropped if no reviewer by 20 Nov. To ask the supervisor in person on 9 Nov | P3 |
| 2026-11-06 | Strings v2 for WoS, ACM DL and arXiv generated by `slr/build_strings.py` and logged in `slr/search-log.md`; arXiv via the API. arXiv count test: S1 50, S2 1466 (IEEE S2 146): screening volume to decide. Pending: WoS and ACM count tests (author) | P3, P4 |
| 2026-11-06 | Pilot counts on all databases (S1 69, S2 1908 before deduplication); arXiv kept unrestricted; ACM Guide used. Selection procedure written (`slr/protocol.md` §4.2): Zotero + Rayyan with CSV exports, two-pass screening, one snowballing iteration as a stated limitation. Pending for P3/P4: extraction form pilot, freeze | P3, P4 |
| 2026-11-06 | Zotero 7 + Better BibTeX set up (collections `SLR` and `Dissertation`; Better BibLaTeX auto-export of `Dissertation` to `doc/references.bib`); Pandoc 3.13 installed; build tested with the first real entry (Spec Kit). Rayyan account still to create | — |
| 2026-11-06 | Rayyan account created; free plan: 3 active reviews, 2 invited reviewers, 1 sample (enough; noted in `slr/protocol.md` §4.2). Blind mode included (confirmed by the author) | — |
| 2026-11-08 | No work on 7–8 Nov. Competencies self-assessment moved to 9 Nov (with the start of the research design, so a heavier day); hetero-assessment on hold until it is discussed with the supervisor | P1, P2 |
| 2026-11-09 | Progress review. M2 started (P3, P4, P13 in progress); M2 scope kept (P1–P4, P8–P11, P13 by 15 Nov). No reply to email 1; the in-person meeting of 9 Nov is at risk; if there is no reply, talk to the supervisor in person. Week 9 materials not yet published. P1, P2, P8–P13 to be written in `doc/chapters/`. Group (c) criterion adopted as EC5 (`slr/protocol.md` §4) | M2, P3 |
| 2026-11-09 | Competency self-assessment done with the author (27 items, importance and level); key competencies chosen: A critical thinking, B time management, C written communication, two actions each with metrics (`doc/chapters/07-work-plan.md`). Hetero-assessment still on hold. The course does not ask for the `.docx` grid to be submitted; the table goes in the document | P1 |
| 2026-11-09 | Question to the supervisor about the second reviewer prepared (Portuguese, deadline 20 Nov); to ask in person or by email | D2a |
| 2026-11-10 | Supervisor not reached (no meeting, no reply to email 1). Work continues on the current assumptions; all open questions (§6) go in email 2, moved to Monday 16 Nov. Week 9 materials still not published | M2, D2a |
| 2026-11-10 | References section moved to `doc/chapters/99-references.md`; document build tested (`doc/build.ps1`, Pandoc 3.13): chapters 01, 03, 07 and the bibliography render | — |
| 2026-11-09 | Research design started: main RQ split into SRQ1–SRQ5, typed by Shaw (2002) and linked to objectives (`doc/chapters/03-research-method.md`). Pending for 10 Nov: Oates figure, validity threats | P2 |
| 2026-11-09 | Document build not tested: Pandoc missing on this computer. Build check and the References move added to 10 Nov | — |
| 2026-11-11 | Oates research process figure done (`doc/figures/research-process.png`, from the week 3 template) and described in `doc/chapters/03-research-method.md`. Pending for P2: validity threats. Week 9 had no classes; week 10 materials published (to add to the course overview) | P2 |
| 2026-11-11 | Threats to validity of the experiment design written (T1–T10 by Wohlin et al. 2012 types, plus resource constraints); Oates (2005) and Wohlin et al. (2012) added to Zotero. P2 done | P2 |
| 2026-11-11 | Extraction form pilot started on 3 studies of different natures: Panda (2026, compares), Gloaguen et al. (2026, evaluates), Macedo (2026, conceptual); imported into the Zotero `SLR` collection. AI drafts each record with page references; the author verifies every field | P4 |
| 2026-11-11 | Extraction pilot done (`slr/extraction-pilot.md`): AI drafts verified by the author on 3–4 key values per study, one value corrected. The pilot showed gaps common to all three studies; form changes C1–C8 accepted by the author and applied to `slr/protocol.md` §5–6. **SLR protocol frozen.** Next: final search on 16–17 Nov | P3, P4 |
| 2026-11-11 | Week 10 materials added (`course-materials/week-10/`, renamed to English, text extracted): schedule construction (logic network, PERT estimates, critical path, slack, baseline), dissertation WBS example by life cycle and its MS Project Gantt, MS Project installation. Course overview updated (calendar, methods, image-only slides). Plan: P11 follows the week 10 WBS example; P12 built in MS Project; MS Project installation added on 16–17 Nov. No classes in week 9 | P11, P12 |
| 2026-11-12 | Day plan: stakeholders (P8), then charter (P9), then ethics (P13), one step at a time with the author. P8 started: stakeholder identification and power × interest grid (week 2 method), to go in `doc/chapters/01-introduction.md` | P8 |
| 2026-11-12 | Stakeholders written with the author (`doc/chapters/01-introduction.md`): S1–S8, three-level power and interest scale, power × interest matrix, strategy per stakeholder. Next for P8: problem interpretation from several perspectives | P8 |
| 2026-11-12 | Problem interpretation written with the author (`doc/chapters/01-introduction.md`): problem, three perspectives, consequences of not solving, wider impact (financial cost, quality and security, licences). Education, employment and energy cost excluded by the author. Pending: three pilot papers to add to the Zotero `Dissertation` collection so their citation keys resolve | P8 |
| 2026-11-12 | Gloaguen et al., Macedo and Panda added to the Zotero `Dissertation` collection; citations resolve. P8 reviewed and confirmed by the author. **P8 done.** Next: project charter (P9) | P8 |
| 2026-11-12 | P9 started: project charter following the 10 sections of the week 2 template, to go in `doc/chapters/07-work-plan.md` | P9 |
| 2026-11-12 | Charter sections 1–6 written with the author: general information, team, stakeholders (link to P8), scope (benefits B1–B3 with measures, deliverables, exclusions), time (PREPD milestones; dissertation dates unknown), cost (Pro plan 22.14 €/month for the run months only). Student benefit removed until the supervisor answers; article submission cost left out. New open questions 8–9 (§6). Next, 13 Nov: charter sections 7–10, ethics (P13), MS Project installation | P9 |
