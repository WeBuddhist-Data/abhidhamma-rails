"""Segments where two different Pāli headwords (not compound-related) get the same termbase term (single-sense only)."""
import re, pathlib, collections, sys
B = pathlib.Path(__file__).resolve().parents[5]
T = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else B / "AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md"
M = B / "AI_translation/burmese/pi-5-keywords-by-reference-pali-burmese-plain.md"
tb = {}
for line in T.read_text(encoding="utf-8").splitlines():
    hw, body = line.split(": {", 1)
    tb[hw.lower()] = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
def norm(h):
    h = h.lower()
    for e in ("ñceva", "ñca", "mpi", "pi", "nti", "ti", "eva"):
        if h.endswith(e) and len(h) > len(e) + 3: h = h[:-len(e)]
    return h[:-2] if len(h) > 5 else h
pairs = collections.Counter(); ex = {}
for l in M.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\[([^\]]+)\] (.*)", l)
    if not m: continue
    kws = {p.partition("=")[0] for p in m.group(2).split(", ")}
    by = collections.defaultdict(set)
    for k in kws:
        t = tb.get(k.lower())
        if t and len(t) == 1: by[t[0]].add(k)
    for t, ks in by.items():
        ks = sorted(ks)
        for i in range(len(ks)):
            for j in range(i+1, len(ks)):
                a, b = ks[i], ks[j]
                na, nb = norm(a), norm(b)
                if na in b.lower() or nb in a.lower() or a.lower() in b.lower() or b.lower() in a.lower(): continue
                key = (a, b, t); pairs[key] += 1; ex.setdefault(key, m.group(1))
for (a, b, t), n in sorted(pairs.items(), key=lambda x: -x[1]):
    print(f"{n:4d}  {a} | {b} = {t}   e.g. {ex[(a, b, t)]}")
