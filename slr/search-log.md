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
| 2026-11-04 | IEEE Xplore | S2 v2 | Year 2023–2026 (results sidebar) | 146 | Pilot | CSV export has 144 rows. Against v1: 117 records out (mostly outside SE), 54 in (from "autonomous agent*"). Key SE records kept. 99 enter through the generic branch; in 44 of them the SE term is only in IEEE index terms, not in title, abstract or keywords. Open: restrict the SE terms to title/abstract fields at the freeze, or remove at screening |
