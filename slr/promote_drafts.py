"""Final AI extraction drafts after the verification rounds (slr/ai-prompts/draft-verify.md).

Usage: python slr/promote_drafts.py   (re-runnable)
Reads slr/extraction/ai-drafts-r0 (original) .. ai-drafts-r3 and writes slr/extraction/ai-drafts/<key>.json, which the tool shows.
Three rounds per record; by the author's decisions of 2026-11-23, group (b) records whose AI majority suggestion
(slr/ft-ai-suggestions.csv) is not Include stop after round 2, and the verification was paused: each record is promoted
from the last round it has (state in slr/extraction/verification-progress.csv). A record with no round yet is shown as drafted.
Each field keeps the last round's value plus "rev" (rounds that corrected it or were unsure, with why) and "warn", a short
pt-PT text shown to the author when a round was unsure (the round's "doubt"), the value changed in two or more rounds, or
it changed in the last round. slr/extraction/ai-drafts-rules/<key>.json (rules-pass.md: the author's rules of 2026-11-23,
for drafts verified before them) overrides values and doubts.
"""
import json, os, re
from collections import Counter

X = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extraction")
same = lambda a, b: re.sub(r"\s+", " ", a or "").strip() == re.sub(r"\s+", " ", b or "").strip()  # noqa: E731
load = lambda p: json.load(open(p, encoding="utf-8"))  # noqa: E731
stats = Counter()
for fn in sorted(os.listdir(os.path.join(X, "ai-drafts-r0"))):
    have = [n for n in range(4) if os.path.exists(os.path.join(X, f"ai-drafts-r{n}", fn))]
    last = len(have) - 1  # rounds run in order
    if have != list(range(last + 1)):
        continue
    R = [load(os.path.join(X, f"ai-drafts-r{n}", fn)) for n in range(last + 1)]
    by = [{f["f"]: f for f in r["fields"]} for r in R]
    rules_p = os.path.join(X, "ai-drafts-rules", fn)
    rules = {f["f"]: f for f in load(rules_p)["fields"]} if os.path.exists(rules_p) else {}
    rounds = range(1, last + 1)
    fields = []
    for f in R[last]["fields"]:
        name = f["f"]
        changed = [n for n in rounds if not same(by[n].get(name, {}).get("v"), by[n - 1].get(name, {}).get("v"))]
        rev = [{"round": n, "verdict": by[n].get(name, {}).get("verdict", ""), "why": by[n].get(name, {}).get("why", "")}
               for n in rounds if n in changed or by[n].get(name, {}).get("verdict") == "uncertain"]
        unsure = [n for n in rounds if by[n].get(name, {}).get("verdict") == "uncertain"]
        doubt = next((by[n][name].get("doubt") for n in reversed(unsure) if by[n][name].get("doubt")), "")
        warn = []
        if unsure:
            warn.append(doubt or f"A IA ficou com dúvidas neste campo (verificação {unsure[-1]}); o motivo está no histórico "
                                  "(passa o rato sobre o nome do campo).")
        if len(changed) >= 2 or (last and last in changed):
            warn.append(f"O valor foi corrigido na{'s' if len(changed) > 1 else ''} verificaç"
                        f"{'ões' if len(changed) > 1 else 'ão'} {' e '.join(map(str, changed))}; confirma-o no texto.")
        v = f.get("v", "")
        if name in rules:
            if rules[name].get("v"):
                v = rules[name]["v"]
                rev.append({"round": "regras", "verdict": "corrected", "why": rules[name].get("why", "")})
            if "doubt" in rules[name]:
                warn = [rules[name]["doubt"]] if rules[name]["doubt"] else []
        fields.append({"f": name, "v": v, "p": f.get("p", ""), "rev": rev, "warn": " ".join(warn)})
    # rounds started with Q13 limited to "proposes an approach"; §5 also applies it to conceptual studies
    nat, q13 = next((f for f in fields if f["f"] == "Nature of the study"), {}), next((f for f in fields if f["f"] == "Q13"), {})
    if nat.get("v", "").lower().startswith("conceptual") and q13.get("v", "").upper().startswith("N/A"):
        q13["warn"] = " ".join(filter(None, [q13["warn"], "Estudo conceptual: a Q13 aplica-se (§5); pontua-a."]))
    stats["fields"] += len(fields)
    stats["warn"] += sum(bool(f["warn"]) for f in fields)
    json.dump({"key": R[last].get("key", fn[:-5]), "model": R[0].get("model", ""), "rounds": last, "fields": fields},
              open(os.path.join(X, "ai-drafts", fn), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    stats[f"records ({last} rounds)"] += 1
print(dict(stats))
