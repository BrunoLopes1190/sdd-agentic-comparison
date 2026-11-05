# SLR search log

One row per query run. Strings come from `protocol.md` §2. Pilot runs (P4) are marked "pilot"; they refine the strings and do not enter the PRISMA flow.

## IEEE Xplore: how the strings are run

Advanced Search → Command Search. No field prefix, so IEEE Xplore searches all metadata (title, abstract, keywords and other metadata). The year range 2023–2026 is set in the results sidebar (Command Search has no year field). No language or document-type filter: IC3 and EC3 are applied at screening, so the count is the raw one. IEEE limits: 25 terms per clause, 10 wildcards per search.

## Strings, version 1 (pilot run 1, 2026-11-04)

S1:

```
("spec-driven" OR "specification-driven" OR "spec-first" OR "spec kit" OR openspec OR bmad OR kiro OR "AGENTS.md" OR "context file*" OR "repository-level context" OR "instruction file*" OR "rules file*") AND ("coding agent*" OR "AI coding agent*" OR "software engineering agent*" OR "agentic coding" OR "agentic software" OR "LLM-based agent*" OR "AI coding assistant*")
```

S2:

```
("coding agent*" OR "AI coding agent*" OR "software engineering agent*" OR "agentic coding" OR "agentic software" OR "LLM-based agent*" OR "AI coding assistant*") AND (benchmark* OR "empirical stud*" OR "controlled experiment*" OR "comparative evaluation" OR "comparative study" OR "token usage" OR "token consumption" OR "inference cost" OR "API cost" OR "pass@k" OR "resolve rate" OR "task success" OR "functional correctness" OR "code quality" OR maintainability OR "technical debt" OR "human effort" OR "developer effort" OR "human intervention")
```

S2a (B AND C) and S2b (B AND D): S2 with the second bracket cut to block C or block D. Check of the file name: `"AGENTS.md"`.

## Strings, version 2 (after pilot run 1)

Changes (protocol change log, 2026-11-04): "LLM-based agent*" only counts together with a software engineering context, and "autonomous agent*" is added under the same condition; "agent manifest*" added to A2. Wildcards: S1 uses 10 (the IEEE maximum), S2 uses 9.

S1:

```
("spec-driven" OR "specification-driven" OR "spec-first" OR "spec kit" OR openspec OR bmad OR kiro OR "AGENTS.md" OR "context file*" OR "repository-level context" OR "instruction file*" OR "rules file*" OR "agent manifest*") AND ("coding agent*" OR "AI coding agent*" OR "software engineering agent*" OR "agentic coding" OR "agentic software" OR "AI coding assistant*" OR (("LLM-based agent*" OR "autonomous agent*") AND ("software engineering" OR "software development" OR "code generation")))
```

S2:

```
("coding agent*" OR "AI coding agent*" OR "software engineering agent*" OR "agentic coding" OR "agentic software" OR "AI coding assistant*" OR (("LLM-based agent*" OR "autonomous agent*") AND ("software engineering" OR "software development" OR "code generation"))) AND (benchmark* OR "empirical stud*" OR "controlled experiment*" OR "comparative evaluation" OR "comparative study" OR "token usage" OR "token consumption" OR "inference cost" OR "API cost" OR "pass@k" OR "resolve rate" OR "task success" OR "functional correctness" OR "code quality" OR maintainability OR "technical debt" OR "human effort" OR "developer effort" OR "human intervention")
```

## Runs

| Date | Database | String | Filters | Hits | Pilot? | Notes |
|---|---|---|---|---|---|---|
| 2026-11-04 | IEEE Xplore | S1 v1 | Year 2023–2026 (results sidebar) | 7 | Pilot | All 2025–2026 |
| 2026-11-04 | IEEE Xplore | S2 v1 | Year 2023–2026 (results sidebar) | 209 | Pilot | CSV export has 207 rows; 1 title appears twice. 162 of 207 match block B only through "LLM-based agent*", mostly outside software engineering (robotics, UAV, networks, healthcare) |
| 2026-11-04 | IEEE Xplore | S2a v1 | Year 2023–2026 (results sidebar) | 152 | Pilot | |
| 2026-11-04 | IEEE Xplore | S2b v1 | Year 2023–2026 (results sidebar) | 87 | Pilot | S2a + S2b = 239, so 30 records are in both. CSV export has 85 rows |
| 2026-11-04 | IEEE Xplore | "AGENTS.md" | Year 2023–2026 (results sidebar) | 4 | Pilot | All 2026; all four are about the file |
| 2026-11-04 | IEEE Xplore | S1 v2 | Year 2023–2026 (results sidebar) | 7 | Pilot | Same 7 records as S1 v1 |
| 2026-11-04 | IEEE Xplore | S2 v2 | Year 2023–2026 (results sidebar) | 146 | Pilot | CSV export has 144 rows. Against v1: 117 records out (mostly outside SE), 54 in (from "autonomous agent*"). Key SE records kept. 99 enter through the generic branch; in 44 of them the SE term is only in IEEE index terms, not in title, abstract or keywords. Decided 2026-11-05 (pilot inspection): keep the string, remove at screening |

## Pilot inspection (P4, 2026-11-05)

Sheet: `pilot/pilot-inspection-2026-11-05.xlsx`. 20 records judged by the author on title and abstract: all 7 of S1 v2 and 13 of S2 v2. Columns: decision (I/E/?), criterion (IC1a–c, EC1–EC4, OUT-SE, OTHER), reason, group (c) "new agent on existing benchmark" (Y/N), missing or noisy terms. A record can meet more than one IC.

Sample. 23 records were drawn at random from the 142 S2 v2 records not in S1 (Python `random.Random(20261105).sample`, IDs P08–P30 in export order). During the inspection the sample was cut to the lower bound of the plan (20–30 records): `random.Random(20261105).sample(the 23 IDs, 13)` kept 13. The two records already judged (P08, P09) were then put back, and two of the 12 still unjudged were dropped instead (`random.Random(20261105).sample(the 12 IDs, 2)` → P13, P29). Kept: P08–P12, P15, P18, P21, P23, P25, P27, P28, P30. Dropped: P13, P14, P16, P17, P19, P20, P22, P24, P26, P29. IDs keep the original numbering.

| String | Judged | I | E | ? | Precision |
|---|---|---|---|---|---|
| S1 v2 | 7 | 7 | 0 | 0 | 100% |
| S2 v2 | 13 | 7 | 6 | 0 | 54% |
| Total | 20 | 14 | 6 | 0 | 70% |

Criteria: IC1a 7, IC1b 4, IC1c 10 (multi-counted over 14 included); OUT-SE 4, OTHER 2. Group (c), over the 10 IC1c records: Y 6, N 4 (S2 only: Y 3, N 3). Terms column empty: no term proposed or flagged.

Index terms. 5 of the 6 S2 exclusions (P09, P11, P18, P25, P28) are among the 44 records where the SE term is only in the index terms; 1 of the 7 inclusions (P27, "software models", "model-driven engineering") is too. Restricting the SE terms to title/abstract would raise S2 precision in the sample to 6/7 but lose P27; the restriction would also only act on IEEE Xplore (INSPEC terms). Reproduced from the CSV: 99 records via the generic branch, 44 of them without the SE term in title, abstract or author keywords; only 10 of the 44 have it in the exported IEEE Terms, so the rest match on INSPEC terms, which the export does not include.

Decisions (author, 2026-11-05):
- The 44 index-term records: keep strings v2 and remove them at screening (recall over precision; same string across databases; about 40 extra titles). No string v3.
- Candidate group (c) criterion (`protocol.md` §4): not adopted for now; the author re-evaluates it before the freeze. The pilot data above are kept for that decision.
