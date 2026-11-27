import sys, re, collections, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[6]
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
def low(w): return w[:1].lower() + w[1:]
P = {}
for t in ("pi-1", "pi-2", "pi-3", "pi-4"):
    d = collections.defaultdict(collections.Counter)
    for l in (ROOT / f"AI_translation/burmese/{t}-keywords-by-reference-pali-burmese-plain.md").read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if m:
            for kv in m.group(2).split(", "):
                if "=" in kv:
                    k, v = kv.split("=", 1); d[low(k)][v] += 1
    P[t] = d
for kw in sys.argv[1:]:
    out = []
    for t in P:
        c = P[t].get(low(kw))
        if c: out.append(f"{t}: " + " | ".join(f"{v} ({n})" for v, n in c.most_common(4)))
    print(kw, "::", "; ".join(out) or "-")
