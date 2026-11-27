"""Compact view of tb.py --file output: word -> distinct Burmese values (read-only helper)."""
import re, sys
cur = None; vals = {}
order = []
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.rstrip("\n")
    if line.startswith("NOT IN"):
        print(line); continue
    if not line.startswith("  "):
        cur = line; order.append(cur); vals[cur] = []; continue
    v = line.split(": ", 1)[1]
    for sense in re.split(r"; (?=[a-z'(])", v):
        b = sense.rsplit(": ", 1)[-1]
        if b not in vals[cur]:
            vals[cur].append(b)
for w in order:
    print(w, "=", " | ".join(vals[w]))
