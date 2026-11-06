"""Search strings v2 for each database, built from the blocks in protocol.md §2.

Run: python slr/build_strings.py   (prints every string; asserts the IEEE output matches search-log.md)
"""
import re
import urllib.parse

A = ["spec-driven", "specification-driven", "spec-first", "spec kit", "openspec", "bmad", "kiro",
     "AGENTS.md", "context file*", "repository-level context", "instruction file*", "rules file*",
     "agent manifest*"]
B = ["coding agent*", "AI coding agent*", "software engineering agent*", "agentic coding",
     "agentic software", "AI coding assistant*"]
B_GENERIC = ["LLM-based agent*", "autonomous agent*"]
SE = ["software engineering", "software development", "code generation"]
CD = ["benchmark*", "empirical stud*", "controlled experiment*", "comparative evaluation",
      "comparative study", "token usage", "token consumption", "inference cost", "API cost", "pass@k",
      "resolve rate", "task success", "functional correctness", "code quality", "maintainability",
      "technical debt", "human effort", "developer effort", "human intervention"]

SPECIAL = {"stud*": ["study", "studies"], "benchmark*": ["benchmark", "benchmarks", "benchmarking"]}


def variants(term):
    """Explicit forms of a wildcard term, for databases without wildcards inside phrases."""
    if not term.endswith("*"):
        return [term]
    head, _, last = term.rpartition(" ")
    words = SPECIAL.get(last, [last[:-1], last[:-1] + "s"])
    return [f"{head} {w}".strip() for w in words]


def quote(term):
    return term if re.fullmatch(r"\w+\*?", term) else f'"{term}"'


def strings(block):
    """block(terms) -> query text for one OR-group. Returns (S1, S2)."""
    b = f"({block(B)[1:-1]} OR ({block(B_GENERIC)} AND {block(SE)}))"
    return f"{block(A)} AND {b}", f"{b} AND {block(CD)}"


def ieee(terms):  # also Web of Science inside TS=(...)
    return "(" + " OR ".join(quote(t) for t in terms) + ")"


def acm(terms):
    inner = "(" + " OR ".join(f'"{v}"' for t in terms for v in variants(t)) + ")"
    return f"(Title:{inner} OR Abstract:{inner} OR Keyword:{inner})"


def arxiv(terms):
    return "(" + " OR ".join(f'{f}:"{v}"' for t in terms for v in variants(t) for f in ("ti", "abs")) + ")"


ARXIV_DATES = "submittedDate:[202301010000 TO 202612312359]"

if __name__ == "__main__":
    s1, s2 = strings(ieee)
    log = open("slr/search-log.md", encoding="utf-8").read().split("## Strings, version 2")[1]
    assert s1 in log and s2 in log, "IEEE strings differ from search-log.md v2"
    out = {"IEEE Xplore": strings(ieee),
           "Web of Science": tuple(f"TS=({s}) AND PY=(2023-2026)" for s in strings(ieee)),
           "ACM DL": strings(acm),
           "arXiv API": tuple(f"({s}) AND {ARXIV_DATES}" for s in strings(arxiv))}
    for db, (q1, q2) in out.items():
        print(f"## {db}\n\nS1:\n{q1}\n\nS2:\n{q2}\n")
    for name, q in zip(("S1", "S2"), out["arXiv API"]):
        print(f"arXiv {name} URL: https://export.arxiv.org/api/query?max_results=1&search_query="
              + urllib.parse.quote(q))
