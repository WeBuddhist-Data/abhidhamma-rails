"""read-only helper: prior pi-1 … pi-5 values of keywords. usage: prior6.py kw [kw …]"""
import sys, re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
ROOT = HERE.parents[4]
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
def low(w): return w[:1].lower() + w[1:]
P = {}
for t in ("pi-1", "pi-2", "pi-3", "pi-4", "pi-5"):
    d = collections.defaultdict(collections.Counter)
    for l in (ROOT / f"AI_translation/burmese/{t}-keywords-by-reference-pali-burmese-plain.md").read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if not m: continue
        for kv in m.group(2).split(", "):
            if "=" in kv:
                k, v = kv.split("=", 1); d[low(k)][v] += 1
    P[t] = d
for kw in sys.argv[1:]:
    print(kw)
    for t in P:
        c = P[t].get(low(kw))
        if c: print("  ", t, c.most_common(6))
