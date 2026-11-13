import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *
# usage: long.py fileprefix start end minlen
fp, s, e, ml = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
fn = [x for x in FILES if x.startswith(fp)][0]
P, H = pairs(fn)
n = 0
for i in range(s, min(e, len(P)) + 1):
    a = P[i-1]; b = H[i-1]
    if not a.strip() or a.startswith("#"):
        continue
    if len(a) < ml:
        continue
    n += 1
    print(f"[{i}] P: {a}")
    print(f"[{i}] H: {b}")
print("COUNT", n, file=sys.stderr)
