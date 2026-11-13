import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *

f = sys.argv[1]
ns = []
for a in sys.argv[2:]:
    if "-" in a:
        x, y = a.split("-"); ns += list(range(int(x), int(y) + 1))
    else:
        ns.append(int(a))
_, _, pn = load(PDIR, f)
_, _, hn = load(HDIR, f)
eng = os.environ.get("R1ENG")
if eng:
    _, _, en = load(EDIR, f)
for n in ns:
    print(f"--- {n} (L{pn[n-1][0]})")
    print("P:", pn[n - 1][1])
    print("H:", hn[n - 1][1])
    if eng:
        print("E:", en[n - 1][1])
