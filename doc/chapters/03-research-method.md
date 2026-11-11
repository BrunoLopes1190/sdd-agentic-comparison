# Research method

## Research questions

The main research question comes from the approved formalisation:

> Which Spec-Driven Development approaches exist for development with agents, how do they differ, and how do they affect the total cost and the quality of development when applied to the same project?

It is broken down into five sub-questions (SRQ).
Each one is typed with Shaw's (2002) classification of research questions in software engineering and linked to a specific objective.
They are named SRQ to keep them apart from the review questions RQ1–RQ4 of the systematic literature review.

: Sub-questions, Shaw type, objective and strategy {#tbl:srq}

| Sub-question | Question | Shaw type | Objective | Strategy |
|---|---|---|---|---|
| SRQ1 | Which SDD approaches for development with agents exist, and what does each one prescribe (artefacts, phases, human review points)? | Generalisation or characterisation: what are the varieties of X? | O1 | Systematic literature review and documented analysis of tool documentation |
| SRQ2 | How do these approaches differ from one another? | Generalisation or characterisation: how are the varieties of X related? | O1 | Comparative framework built from the SRQ1 results |
| SRQ3 | How can the total cost and the quality of developing the same project with different SDD approaches be measured in a reproducible way? | Method for analysis: how can I evaluate the quality of X? | O2 | Design and creation: evaluation protocol, reference project and metrics defined in advance |
| SRQ4 | How do the selected approaches compare with each other, and with a baseline without a structured specification, in total cost and quality on the same reference project? | Design, evaluation or analysis of a particular instance: how does X compare to Y? | O3, O4 | Experiment |
| SRQ5 | Which approach should be used in which situation? | Method for analysis: how do I choose between X and Y? | O5 | Synthesis of the SRQ2 and SRQ4 results into a decision guide |

The review questions feed the sub-questions.
RQ1 answers SRQ1 and supports SRQ2.
RQ2 and RQ3 inform the design of the protocol (SRQ3).
RQ4 establishes the research gap.

SRQ1 and SRQ2 are answered in this preparation phase, and SRQ3 is answered at the design level.
SRQ4 and SRQ5 are answered in the dissertation, when the experiment is run.

## Research process

The research process follows the model of @oatesResearchingInformationSystems2006.
The figure below shows the model, with the elements used in this work highlighted.

![Research process, adapted from @oatesResearchingInformationSystems2006. Highlighted boxes are the elements used in this work.](figures/research-process.png){#fig:research-process width=100%}

The starting point is the problem stated in the introduction.
Several SDD approaches for agents appeared in little more than a year, and there is no comparable evidence to choose between them.
A systematic literature review, together with a documented analysis of the tools' documentation, gives the state of the art.
From it comes the conceptual framework: a common comparative framework of the SDD approaches, which answers SRQ2.
The research questions are the main question and SRQ1–SRQ5 above.

Two strategies are combined, which Oates calls a one-to-many relation between questions and strategies.
Design and creation produces the artefacts: the evaluation protocol, the reference project and the metrics (SRQ3), and later the decision guide (SRQ5).
The experiment applies each selected approach, and a baseline without a structured specification, to the same reference project (SRQ4).

Data are generated in three ways.
Documents are the papers and the tools' documentation and repositories.
Observation covers the agent runs.
Logs and metrics are the session logs, usage records and test and code analysis results of each run; this box was added to the original model.

Analysis is quantitative and qualitative.
The cost and quality metrics are compared across approaches and with the baseline.
The review results, the framework and the observations of the runs are synthesised qualitatively.

In this preparation phase, the process covers the review, the framework, the research questions and the design of the evaluation protocol.
The experiment and the decision guide belong to the dissertation.

## Threats to validity

The threats below concern the design of the experiment.
They are grouped by the four types of validity used in software engineering experiments [@wohlinExperimentationSoftwareEngineering2012].
Two of them are the sampling and confirmation biases discussed in the course on research ethics.
The threats to the validity of the literature review are discussed with its results.

: Threats to the validity of the experiment and how they are reduced {#tbl:threats}

| # | Type | Threat | Mitigation |
|---|---|---|---|
| T1 | Construct | Cost: the personal Claude Pro plan has a flat price, so there is no real cost per run. An estimate from tokens is not the price paid, and token counts differ between models | Tokens are measured from the session logs. Cost is estimated from the public API price on a fixed date. Tokens and estimated cost are reported separately |
| T2 | Construct | Quality: part of the assessment of quality is subjective and may differ between assessors | Objective measures come first (acceptance tests, static analysis). The subjective part uses a rubric fixed in advance and is assessed blind, without knowing the approach |
| T3 | Internal | Language models are not deterministic, so one run may succeed or fail by chance | Each condition is repeated. The briefing, the tests, and the agent and model versions are the same for every run |
| T4 | Internal | The author may intervene during runs or learn from one run to the next | Prompts are fixed in advance. Every human intervention is logged and counted as effort |
| T5 | Internal | Confirmation bias: the author may favour one approach | Acceptance tests and metrics are fixed before any run. Measurement is automatic. Logs and data are published |
| T6 | Internal | The model may have seen the project, or a similar one, during training | The reference project is new and synthetic, and is published only after the runs |
| T7 | Internal | Tools change weekly, and the provider may update a model during the experiment. The order of runs may also affect results | Tool versions and access dates are pinned, and model identifiers are fixed. All runs take place in a short window, in a random order interleaved across approaches |
| T8 | External | Sampling bias: one reference project and one agent vendor may not represent other projects and agents | This is stated as a limit. The project's characteristics are described, and the agent and model are recorded as factors |
| T9 | Conclusion | Few repetitions give weak statistical power | Spread is reported, not only means. Non-parametric tests are used. Claims are kept to what the data support |
| T10 | Conflict of interest | Claude is both an agent under study and the assistant used for this work | This is declared in the ethics chapter. The agent is a recorded factor |

Limited resources make some of these threats worse.
Language models are expensive, and the runs may only use the author's personal Claude Pro plan and models that run on the author's hardware.
The local models that this hardware can run are smaller than the leading ones, which weakens external validity (T8).
Usage limits reduce the number of repetitions, which weakens conclusion validity (T9).
They may also interrupt a run, which then differs from the others; an interrupted run is logged and repeated from the start.
