# PREPD 2026-27 Context (Bruno Lopes, MEI-ISEP)

Updated on 2026-11-22. Summary of the state of the proposal and the decisions taken. This file is self-contained: it allows the work to be continued on any computer.
Course synthesis: `course-materials/course-overview.md`. PREPD plan: `planning/prepd-work-plan.md`.

## 0. Current status and next steps

- **Phase:** formalisation submitted on 2026-10-14 and approved; the approved text is `admin/formalizacao_1240441.pdf` (version with citations). All PREPD work starts from it. No reviewer comments so far. The title on the platform is correct. **M2 done on 16 Nov: email 2 sent** by the author from the ISEP Outlook (`planning/emails/2026-11-16-email-2.md`, text as sent), with all 12 open questions of plan §6 (second reviewer first, answer needed by 20 Nov) and a meeting request for this week; attachments: document draft (32 pages, Harvard citations, WBS and Oates figures) and frozen SLR protocol (19 pages). M2 products: SLR protocol frozen on 11 Nov after the extraction pilot (P3, P4; `slr/extraction-pilot.md`); research design (P2, 11 Nov; `doc/chapters/03-research-method.md`); stakeholders and problem interpretation (P8, 12 Nov; `doc/chapters/01-introduction.md`); project charter (P9, 13 Nov), planning approach (P10, hybrid) and WBS with dictionary (P11, 15 Nov; figure `doc/figures/wbs.pptx`/`wbs.png`), all in `doc/chapters/07-work-plan.md`; ethics (P13, 13 Nov; `doc/chapters/06-ethics.md`); competencies (P1) self-assessment and action plan done on 9 Nov (critical thinking, time management, written communication), **P1 still in progress: hetero-assessment on hold** (email 2 question 9). Citation style: the build uses Harvard (Cite Them Right, `doc/harvard-cite-them-right.csl`) since 16 Nov, as in D4; `doc/reference.docx` (template styles) does not exist yet. **MS Project done on 16 Nov:** the ISEP IT services reset the MFA; the author registered Microsoft Authenticator (default) and SMS (backup); Project Professional 2021 (64-bit, English, matching Microsoft 365 Apps x64, Current Channel) installed from Azure Dev Tools for Teaching (Azure Education hub, student account validated), activated with the academic key and tested on the week 10 example `.mpp`; charter cost table: no cost, ISEP academic licence. P12 (Gantt) unblocked, due at M3 (30 Nov). No work on 17 Nov. **P5 on 18 Nov: final SLR search done** (cut-off 2026-11-18; `slr/search-log.md`, "Final search"): arXiv by API (S1 57, S2 1548), IEEE Xplore (S1 10, S2 157 exported of 159 shown), Web of Science (S1 5, S2 128), ACM DL Guide (S1 10, S2 216); 2131 records exported to `slr/exports/` and imported into Zotero (collection SLR, one subcollection per database; no merge in Zotero). Deduplication by `slr/dedup.py` (DOI then title, published over preprint; protocol change log 2026-11-18): 269 removed, then 4 more by Rayyan's check; **1858 records to screen** in the Rayyan review "SLR SDD agentic coding – main screening" (export `slr/rayyan-after-dedup-2026-11-18.csv`). Second-reviewer calibration (5 pilot records) and sample (30 records) drawn with seed 20261118 (`slr/draw_sample.py`), used only if a reviewer is confirmed by 20 Nov. **19 Nov:** `doc/reference.docx` built from the ISEP `.dotx` by `doc/make_reference_docx.py` (line spacing 1.5 by the author's decision; Pandoc installed on this computer); P1 hetero-assessment requested from an MSc colleague (answers go into `doc/chapters/07-work-plan.md`); screening sheet `slr/screening-sheet.md`; title/abstract screening started in Rayyan: pass 1 (title) on about 1650 of 1858 records (about 200 left, mostly IEEE and WoS), 57% excluded at 800. The day's Rayyan export held only the undecided records without decisions; not committed (it also contains the author's email). **20 Nov:** P1 done (colleague's hetero-assessment added; key competencies kept). Second reviewer dropped (no reply, no reviewer; protocol §4.1 removed, threat to validity). Rayyan's free plan stopped taking decisions after 876 pass-1 exclusions (`slr/screening-pass1-2026-11-20.csv`, all IC1); a check found 354 of them with in-scope titles, sent back to pass 2 (`slr/pass1-recheck-2026-11-20.csv`). Pass 2 (title/abstract) moved to a local tool, `python slr/screen.py` (http://127.0.0.1:8765): queue `slr/pass2-queue.csv` (1307), decisions `slr/pass2-decisions.csv` (append-only, last row per key), AI suggestions `slr/pass2-ai-suggestions.csv` shown only after the author decides (protocol step 9; `doc/ai-usage.md`). 29 decisions made in the second Rayyan review are in `slr/screening-pass2-rayyan-2026-11-20.csv`. End of day: 450 of 1307 decided (Include 249, Maybe 5, IC1 115, EC5 59, EC1 22), 56% pass (51% in the last 209); author–AI in/out agreement before seeing the suggestion 78% in the last 209. Projection about 680 records to pass 3. The review of author–AI disagreements on early records moves to pass 3. From decision 135: few maybes, borderline kept as include; a **pass 3** narrows group (c) (benchmarks/evaluations) with a criterion to define and log **before** pass 3. **21 Nov: pass 2 done** (about 2 h 20 min in the tool, about 300 records/h): 1307 of 1307 decided (Include 682, Maybe 12, IC1 337, EC5 223, EC1 50, Other 3), **694 pass (53%)**; the 344 records sent back from pass 1 passed at 54%. Author–AI agreement on the first (blind) decision: exact 73%, in/out 84% (89% in the last 349); 107 decisions changed after seeing the suggestion, including 47 blind includes against an AI exclusion that ended mostly as excludes (review in pass 3; possible anchoring, to state in protocol §7). By the AI's group as proxy, about 534 of the 694 are group (c) and about 150 are (a)/(b), so pass 3 must bring (c) to about 100 for about 250 at full text. Draft criterion proposed by Claude, **not decided**: EC6, group (c) only, keep a record only if (i) it evaluates agents on feature- or project-level development (building or extending an application from natural-language requirements) or (ii) its contribution is the evaluation method (cost, quality or human-effort metrics; repetitions or non-determinism; controlled comparison of agents, models or workflows on the same tasks); excluded in particular, unless (ii): observational studies of agent use (mining PRs/commits), benchmarks limited to issue repair, one task type (tests, review, security) or one domain. Keyword sizing of group (c): new benchmark ~200, issue/SWE-bench ~140, mining/real use ~115, feature/project-level ~90, security ~65; estimate 100–150 kept, so 250–300 in total; stronger fallback: (i) and (ii). **22 Nov: pass 3 done.** Criterion **EC6** decided by the author and logged in `slr/protocol.md` before pass 3 (group (c) kept only for code-development tasks at feature or project level, or when the evaluation method is the contribution; issue repair always out); rule "LLM vs humans" confirmed in the screening-sheet decision log; pass-3 flow in `slr/screening-sheet.md`. New AI suggestions on all criteria for 876 records (`slr/pass3-ai-suggestions.csv`, 6 subagents, quotes verified); 108 resolved pass-2 disagreements dropped; queue `slr/pass3-queue.csv` (768, `slr/build_pass3_queue.py`), tool `python slr/screen.py 3`, decisions `slr/pass3-decisions.csv`. Result: of the 694, 300 kept (AI group c 153, b 108, a 39), EC6 348; 46 switched-after-AI all excluded; 28 open disagreements all included; **328 to full text**. Agreement on the blind decision exact 97%, in/out 99% (pass 2: 84%), 3 changed after the suggestion; the author wrote decisions in their own notes first, then entered them (timestamps are not reading time); learning effect stated in protocol §7. **Next (23 Nov):** full-text screening of the 328 (capacity about 250: §7 fallback if needed; IC4 when no access), then snowballing and PRISMA on 24 Nov; quality assessment and extraction 25–27 Nov (about 220–250 studies expected; heavy, consider a lighter extraction for group (c)). The pass-3 notes were not kept; stated in the protocol (step 4b). **23 Nov:** week 9 materials added (competency action plan: SWOT, GRIT, market analysis, GROW, SMART); P1 reopened for these additions (by M3). Full-text procedure decided and logged (protocol §4.2 step 7): full-text decision, quality assessment and extraction in one sitting per study, groups (a) then (b) then (c), AI suggestion only after the author's decision, AI drafts of extraction and quality checked by the author; §6 nature "proposes an approach" added and DARE only for reviews that describe their search. Full texts: **327 of 328** in `slr/fulltext/` (git-ignored; `slr/fetch_fulltext.py`, access log `slr/fulltext-access.csv`): 296 from arXiv, 2 open access, 29 fetched by hand by the author (14 IEEE, 13 ACM, 2 Elsevier); only `rayyan-800486762` (Wiley, LEAF) not obtained, IC4 unless found. The 29 hand-fetched ones still need AI suggestions and, for groups (a)/(b), AI drafts. Tool: `python slr/screen.py ft` (queue by AI group, view cut from the full text, P opens the PDF, codes incl. IC4/EC2–EC4, notes kept; after an Include the extraction panel shows the AI draft from `slr/extraction/ai-drafts/<key>.json`, checked record saved to `slr/extraction/<key>.json`). AI suggestions `slr/ft-ai-suggestions.csv` for all 298 with text (quotes verified); group (c) suggestions harmonised (four agents applied EC6 unevenly; one pass with a single rule set changed 9 of 149; original kept in column s0). AI drafts done for all 149 group (a)/(b) studies with a full text (32 + 117; structure checked; 98.3% of their numbers appear verbatim in the text, the rest mostly derived or rebuilt from jumbled tables, noted in Notes; Q11 flagged where a DOI record was read from arXiv); group (c) drafts to make only for the author's (c) includes, and drafts for the 30 hand-fetched papers once they are in. No full-text decision made yet by the author. **Next:** author screens (a) then (b) in the tool, checking each included study's extraction; fetch the 30 by hand; then (c) (drafts for its includes on demand); then snowballing and PRISMA.
- **Reference text:** the approved formalisation (`admin/formalizacao_1240441.pdf`, 14 Oct) replaces the Word of 6 Oct (section 2 below is the 6 Oct text; its problem statement was reworded on 14 Oct).
- **Supervision:** supervisor only (Paulo Gandra de Sousa, pag@isep.ipp.pt); no co-supervisor. The supervisor gave no specific instructions beyond following the classes. GenAI use: no restriction, but it must be declared.
- **Extended abstract:** the supervisor will review it until 15 Dec; draft sent 13 Dec (M4). Function and structure now published (`course-materials/general/extended-abstract-function.txt`, `extended-abstract-structure.txt`, 2026-11-04): it is not graded but lets the course head decide whether to schedule the final exam; 8 sections, about 4–5 pages, 10–20 references. Language still to confirm with the supervisor.
- **SLR decisions (2026-11-06):** second reviewer conditional, **dropped on 20 Nov** (no reviewer found; single reviewer stated as a threat to validity; AI never a reviewer); strings for all databases generated by `slr/build_strings.py`; pilot totals S1 69, S2 1908 before deduplication; arXiv unrestricted (via API); ACM Guide to Computing Literature; Zotero (references) + Rayyan (screening, free plan, blind mode) with CSV exports to the repo; one snowballing iteration, stated as a limitation. Group (c) criterion adopted as EC5 on 2026-11-09. Supervisor not reached on 9–10 Nov; the second-reviewer question was sent in email 2 on 16 Nov (answer needed by 20 Nov; if none, protocol §4.1 is dropped and stated as a limitation). Details: `slr/protocol.md` change log.
- **Email 1** sent 2026-11-04 (`planning/emails/2026-11-04-email-1.md`). Scopus dropped from the SLR sources (no ISEP licence). No reply; all open questions were repeated in email 2 (sent 2026-11-16).
- **Assessment:** 10-minute presentation; exam date to be announced at the end of December.
- **State of the art:** full SLR (student's decision, 2 Nov).
- **Resources:** no fixed hours; no token budget; runs (dissertation only) may use the student's personal Claude Pro plan (22.14 € per month; counted in the charter only for the months of the runs). No employer is linked to the work.
- **Not yet answered by the supervisor (no reply by 19 Nov):** all 12 questions of email 2 (sent 16 Nov): second reviewer (by 20 Nov), P.PORTO Code art. 10, citation style and page limit, extended abstract language, Pro plan and local models, Scopus, charter approval, student benefit in the charter, competency hetero-assessment, fixed dates of the dissertation, open research data, repository access. Meeting requested for the week of 16 Nov. See `planning/prepd-work-plan.md` §6.
- **Next:** see the products and dates in `planning/prepd-work-plan.md` §4.
- **Left to the dissertation:** agents and models, definition of "total cost", final metrics, number of approaches and of repetitions, reference project, all runs.

## 1. Working documents

| Document | Where | Content |
|---|---|---|
| Dissertation Proposal | https://claude.ai/code/artifact/47a68173-e319-4be2-ba23-57d908f056d6 | Complete proposal in Portuguese, working notes (historical; local copy removed) |
| PREPD Formalisation: proposed answers | https://claude.ai/code/artifact/f5c489da-f4f2-4f42-a086-8f9f67cfee88 | Draft answers before submission (historical; local copy removed). Approved text: `admin/formalizacao_1240441.pdf` |
| DissertationProposal-1240441.docx | Sent to the professor on 6 Oct | Reference text shared with the supervisor |
| Course materials | `C:\Users\BIMMS-BLopes\Desktop\PREPD` (bimmsport43); `C:\dev\PREPD` (desktop-r8kfvjg) | PDFs, templates, FAQ |

## 2. Reference texts (identical to the Word of 6 Oct)

**Title:** Spec-Driven for Agentic Software Development: A Characterisation and Comparison of Existing Approaches
(Chosen by Bruno. Grammatically, "Development" is missing after "Spec-Driven"; confirm with the supervisor, together with the title error on the platform.)

**Research question:** Which Spec-Driven Development approaches exist for development with agents, how do they differ, and how do they affect the total cost and the quality of development when applied to the same project?

**Question (PT):** Que abordagens de Spec-Driven Development existem para o desenvolvimento com agentes, em que diferem e como afetam o custo total e a qualidade do desenvolvimento quando aplicadas ao mesmo projeto?

**Problem:**
AI coding agents now carry out complete development tasks: they analyse repositories, plan changes, modify multiple files and run tests. Spec-Driven Development (SDD) proposes that the specification should be the central artefact of this work, giving the agent persistent and structured context.

In little more than a year, several approaches have emerged that implement SDD in different ways, such as GitHub Spec Kit, OpenSpec, Kiro and the BMAD Method. They differ in the artefacts they require, the phases of the process and the points of human review.

A team that wants to adopt SDD has no comparable evidence today on which to base its choice. The available comparisons are almost all grey literature, and the academic works are conceptual, taxonomic or evaluate a single approach in isolation.

The problem to be addressed is the lack of a common characterisation of the existing SDD standards and of a comparison of their results when applied to the same project.

**Proposed approach:** (1) Characterise the approaches in a common comparative framework: which standards exist, what each one prescribes and how it can be used. (2) Apply them to the same example project and compare the results, with each other and with a baseline without a structured specification, through cost and quality metrics defined in advance. Evaluation details (agents, models, final metrics) are refined during the state of the art.

**Objectives:**
Main objective: to identify and characterise the existing Spec-Driven Development standards for development with agents, and to compare their effect on the total cost and the quality of development when applied to the same project.
1. Identify the existing SDD standards and characterise them in a common comparative framework: what each one prescribes and how it can be used.
2. Design a reproducible evaluation protocol, with a reference project and cost and quality metrics defined in advance.
3. Apply each approach to the same example project, together with a baseline without a structured specification.
4. Compare the results of the approaches, with each other and with the baseline.
5. Produce a decision guide on which approach to use in which situation.

**Expected results:** the comparative framework, a reproducible evaluation protocol with the reference project, and a decision guide on which approach to use in which situation.

## 3. Bruno's decisions

| Topic | Decision |
|---|---|
| Focus | Identify SDD standards and compare them on the same example project; address the gap identified by Macedo and by Díaz et al. |
| Spec-first | Do not restrict the title, question or problem to spec-first |
| Agents | Several agents allowed; the agent is a recorded factor. Details in the state of the art |
| Total cost | Open; to be defined in the state of the art |
| Baseline | Kept (without a structured specification) |
| Decision guide | Kept (objective 5) |
| Language | Formal texts in English; emails to the professor in Portuguese |
| Consistency | The Word, the formalisation and the emails must not diverge; the submitted formalisation of 14 Oct is the reference text |
| State of the art | Full SLR (2 Nov) |
| Ethics | ACM Code of Ethics (2018) as the one code, plus ALLEA principles; no ethics committee (art. 10); research data published openly at the end of the dissertation with a persistent identifier (13 Nov) |

How to separate what counts as an SDD "standard": three layers. Method (flow of phases; object of comparison), artefact format (spec.md, delta specs, AGENTS.md; characteristic described), execution tool (CLI, IDE, agent, model; recorded factor). Inclusion criteria: persistent artefacts before the code; repeatable flow; public documentation and a pinnable version; able to carry out the example project; terms of use that allow research use (13 Nov).

Characteristics of the example project: neutral briefing; executable by all approaches and agents; verifiable by external acceptance tests via API; new project; 8 to 10 features, repeatable in a few hours; tasks of different types; testable architectural constraints; some deliberately ambiguous requirements; original domain; reproducible.

The formalisation is approved (`admin/formalizacao_1240441.pdf`); its open decisions were closed at submission.

## 4. Verified literature (abstracts read on 2026-10-02; Panda, Gloaguen et al. and Macedo read in full in the extraction pilot on 2026-11-11, `slr/extraction-pilot.md`)

| Source | Type | Main point |
|---|---|---|
| Böckeler (2025), martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html | Grey | Spec-first, spec-anchored and spec-as-source levels; analyses Kiro, spec-kit, Tessl |
| Piskala (2026), arXiv:2602.00180 | Conceptual preprint | Three levels of rigour and a decision framework |
| Macedo (2026), arXiv:2606.04967 | Preprint, taxonomy | 6 dimensions across 6 frameworks; lack of benchmarks of the complete process |
| Díaz et al. (2026), arXiv:2609.00252 | Preprint, multivocal review | SDD for human-agent work; no established peer-reviewed evidence |
| Gloaguen et al. (2026), arXiv:2602.11988 | Preprint, experiment | Model-generated context files do not significantly improve success and raise cost by about 20% (+20%/+23%) |
| Panda (2026), arXiv:2606.30689 | Preprint, experiment | Compares traceSDD, Spec Kit and OpenSpec on determinism and hallucination detection |
| Taghavi and Bhavani (2026), arXiv:2604.05278 | Preprint | Evaluates an extension to Spec Kit |
| Alenezi (2026), arXiv:2607.16680 | Preprint, design science | SDD as governance; no new data |
| Tanaka et al. (2026), arXiv:2608.30572 | Preprint, teaching report | 14 students; higher throughput, less understanding |
| Uvik (2026), uvik.net/spec-driven-development-benchmark | Industrial benchmark | 4 frameworks + control; not peer-reviewed |

Stated gap: the search carried out found no peer-reviewed study that compares SDD approaches on the same project in terms of cost and quality. Pilot searches done on IEEE Xplore, WoS, ACM and arXiv (4–6 Nov); Scopus dropped (no ISEP licence); final search on 16–17 Nov.

## 5. The course
- PREPD (1st semester) prepares the dissertation (DIMEI, 2nd semester). Portal: https://projetos.dei.isep.ipp.pt
- Competences CO1 to CO5: problem analysis, literature review, plan, coherent proposal, communication.

## 6. Dates ("Processo e Datas" slide)
| Phase | Task | By |
|---|---|---|
| Proposal | Application, assignment, acceptance, approval | 2026-10-09 (done) |
| Project | Supervisor invitation + formalisation submission | 2026-10-14 |
| Project | Formalisation review | 2026-10-24 |
| Project | Extended abstract | 2026-12-16 |
| Project | Final document | 2027-01-06 |
| Assessment | Oral examination | 2027-01-04 to 01-09 |

## 7. Assessment and rules
- 30-minute online oral examination on the document; panel: chair, supervisor, examiner. Submission: ZIP with two PDFs.
- Criteria: context, critical and ethical interpretation of the problem, objectives and method, state of the art with method, planning, structure, writing (sentences < 30 words), ethics.
- There must be design and development. Supervisor: DEI lecturer with a doctorate or a specialist; a proposing lecturer takes on the supervision but must be invited in the formalisation.
- Generative AI allowed, declared in «Utilização de conteúdo gerado por IA».

## 8. Tools from the classes
Oates (2005): design and creation + experiment. Shaw (2002): types of RQ. Project Charter, 5W matrix, databases ACM DL, IEEE Xplore, arXiv, B-On, WoS.

## 9. History
- Professor's proposal: "Agentic Software Development Lifecycle".
- Bruno's v1: "Quanto e como especificar para agentes".
- Feedback: focus on the spec-driven options and the existing standards; include an evaluation with an example project.
- 2 Oct: proposal reworked. 6 Oct: consolidated Word sent; professor submitted the proposal. 11 Oct: formalisation reviewed.
