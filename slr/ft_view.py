"""Print the mechanical full-text view the author decides on in the tool (no AI), for AI runs to read the same parts.

Usage: python slr/ft_view.py <key> [<key> ...]
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
keys, sys.argv = sys.argv[1:], sys.argv[:1]
import screen  # noqa: E402  (pass-2 defaults; view() does not depend on the pass)

sys.stdout.reconfigure(encoding="utf-8")
for k in keys:
    print(json.dumps({"key": k, **(screen.view(k) or {"error": "no full text"})}, ensure_ascii=False, indent=1))
