"""Side-by-side lobha string items: Pāli word / 4-01 item / 4-02 item (only differing rows)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz_common import segments


def get(part, sid):
    for s, ps, hs in segments(part):
        if s == sid:
            return ps[0], hs[0]


p, a = get("4-01-nikkhepakandam", "1-1065")
_, b = get("4-02-nikkhepakandam", "1-1236")
pw = re.sub(r"\[[^\]]*\]", "", p.split("Yo ", 1)[1].split(" – ")[0]).split()
cut = lambda h: [x.strip() for x in re.sub(r"\[[^\]]*\]", "", h.split("? ", 1)[1].split(" – ")[0]).split(",")]
ia, ib = cut(a), cut(b)
print(len(pw), len(ia), len(ib))
for i in range(max(len(pw), len(ia), len(ib))):
    x = pw[i] if i < len(pw) else ""
    y = ia[i] if i < len(ia) else ""
    z = ib[i] if i < len(ib) else ""
    if y != z or "-a" in sys.argv:
        print(f"{i:3d} {x:22s} | {y:30s} | {z}")
