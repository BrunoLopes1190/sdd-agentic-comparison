# PREPD 2026-27 Context (Bruno Lopes, MEI-ISEP)

Updated on 2026-11-02. Summary of the state of the proposal and the decisions taken. This file is self-contained: it allows the work to be continued on any computer.
Course synthesis: `course-materials/course-overview.md`. PREPD plan: `planning/prepd-work-plan.md`.

## 0. Current status and next steps

- **Phase:** formalisation submitted on 2026-10-14 and approved; the approved text is `admin/formalizacao_1240441.pdf` (version with citations). All PREPD work starts from it. No reviewer comments so far. The title on the platform is correct. PREPD course work (charter, competencies, SLR, plan) not started.
- **Reference text:** the approved formalisation (`admin/formalizacao_1240441.pdf`, 14 Oct) replaces the Word of 6 Oct (section 2 below is the 6 Oct text; its problem statement was reworded on 14 Oct).
- **Supervision:** supervisor only; no co-supervisor. The supervisor gave no specific instructions beyond following the classes. GenAI use: no restriction, but it must be declared.
- **Extended abstract:** the supervisor will review it until 15 Dec; send the draft (target 4 Dec) and ask for a meeting.
- **Assessment:** 10-minute presentation; exam date to be announced at the end of December.
- **State of the art:** full SLR (student's decision, 2 Nov).
- **Resources:** no fixed hours; no token budget; runs (dissertation only) may use the student's personal Claude Pro plan. No employer is linked to the work.
- **Not yet discussed with the supervisor:** P.PORTO Code art. 10 (ethics review for autonomous AI systems); second reviewer for the SLR. See `planning/prepd-work-plan.md` §6.
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

How to separate what counts as an SDD "standard": three layers. Method (flow of phases; object of comparison), artefact format (spec.md, delta specs, AGENTS.md; characteristic described), execution tool (CLI, IDE, agent, model; recorded factor). Inclusion criteria: persistent artefacts before the code; repeatable flow; public documentation and a pinnable version; able to carry out the example project.

Characteristics of the example project: neutral briefing; executable by all approaches and agents; verifiable by external acceptance tests via API; new project; 8 to 10 features, repeatable in a few hours; tasks of different types; testable architectural constraints; some deliberately ambiguous requirements; original domain; reproducible.

The formalisation is approved (`admin/formalizacao_1240441.pdf`); its open decisions were closed at submission.

## 4. Verified literature (abstracts read on 2026-10-02; full papers not yet read)

| Source | Type | Main point |
|---|---|---|
| Böckeler (2025), martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html | Grey | Spec-first, spec-anchored and spec-as-source levels; analyses Kiro, spec-kit, Tessl |
| Piskala (2026), arXiv:2602.00180 | Conceptual preprint | Three levels of rigour and a decision framework |
| Macedo (2026), arXiv:2606.04967 | Preprint, taxonomy | 6 dimensions across 6 frameworks; lack of benchmarks of the complete process |
| Díaz et al. (2026), arXiv:2609.00252 | Preprint, multivocal review | SDD for human-agent work; no established peer-reviewed evidence |
| Gloaguen et al. (2026), arXiv:2602.11988 | Preprint, experiment | Context files do not generally improve success and increase cost by more than 20% |
| Panda (2026), arXiv:2606.30689 | Preprint, experiment | Compares traceSDD, Spec Kit and OpenSpec on determinism and hallucination detection |
| Taghavi and Bhavani (2026), arXiv:2604.05278 | Preprint | Evaluates an extension to Spec Kit |
| Alenezi (2026), arXiv:2607.16680 | Preprint, design science | SDD as governance; no new data |
| Tanaka et al. (2026), arXiv:2608.30572 | Preprint, teaching report | 14 students; higher throughput, less understanding |
| Uvik (2026), uvik.net/spec-driven-development-benchmark | Industrial benchmark | 4 frameworks + control; not peer-reviewed |

Stated gap: the search carried out found no peer-reviewed study that compares SDD approaches on the same project in terms of cost and quality. ACM, IEEE and Scopus have not yet been searched.

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
