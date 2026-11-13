"""Locate the approved sample lines inside 1-mulayamaka.md / 2-01-khandhayamaka.md (raw and non-empty numbering)."""
import os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

samp = []
for f in sorted(glob.glob(os.path.join(C.HERE, "sample", "s*.md"))):
    if f.endswith("-pali.md"):
        continue
    samp += [l.strip() for l in open(f, encoding="utf-8-sig").read().splitlines() if l.strip()]
S = set(samp)
for part in ["1-mulayamaka", "2-01-khandhayamaka"]:
    raw = open(os.path.join(C.BAK, part + ".md"), encoding="utf-8-sig").read().split("\n")
    ne = 0
    hits_raw, hits_ne = [], []
    for i, l in enumerate(raw, 1):
        if l.strip():
            ne += 1
            if l.strip() in S:
                hits_raw.append(i); hits_ne.append(ne)

    def runs(x):
        out, s = [], None
        for a, b in zip([None] + x, x + [None]):
            if a is None or b is None or b != a + 1:
                pass
        r = []
        for v in x:
            if r and v == r[-1][1] + 1:
                r[-1][1] = v
            else:
                r.append([v, v])
        return r
    print(part, "raw runs:", runs(hits_raw))
    print(part, "non-empty runs:", runs(hits_ne))
print("sample lines:", len(samp), "unique:", len(S))
