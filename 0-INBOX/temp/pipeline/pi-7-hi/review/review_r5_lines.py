import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *
# usage: lines.py "3-01:82,3-01:167,..." [e]
withE = len(sys.argv) > 2
cache = {}
for spec in sys.argv[1].split(","):
    f, n = spec.split(":"); n = int(n)
    fn = [x for x in FILES if x.startswith(f)][0]
    if fn not in cache:
        P, H = pairs(fn)
        E = load(os.path.join(EDIR, fn))
        cache[fn] = (P, H, E)
    P, H, E = cache[fn]
    print(f"[{spec}] P: {P[n-1]}")
    if withE:
        print(f"[{spec}] E: {E[n-1]}")
    print(f"[{spec}] H: {H[n-1]}")
    print()
