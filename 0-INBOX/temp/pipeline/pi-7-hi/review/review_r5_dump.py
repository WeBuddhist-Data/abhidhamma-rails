import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *
# usage: dump.py fileidx start end [e]
fi = int(sys.argv[1]); s = int(sys.argv[2]); e = int(sys.argv[3])
withE = len(sys.argv) > 4
fn = FILES[fi]
P, H = pairs(fn)
E = load(os.path.join(EDIR, fn)) if withE else None
for i in range(s, min(e, len(P)) + 1):
    a = P[i-1]
    if not a.strip():
        continue
    print(f"[{i}] P: {a}")
    if withE:
        print(f"[{i}] E: {E[i-1]}")
    print(f"[{i}] H: {H[i-1]}")
