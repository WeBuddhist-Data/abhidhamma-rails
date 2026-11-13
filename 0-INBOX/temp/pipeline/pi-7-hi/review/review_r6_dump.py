import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *
# usage: dump.py fileidx startk endk [filter-substring]
f = FILES[int(sys.argv[1])]
a, b = int(sys.argv[2]), int(sys.argv[3])
flt = sys.argv[4] if len(sys.argv) > 4 else None
for r in pairs(f):
    if a <= r["k"] <= b and (flt is None or flt in r["p"] or flt in r["h"]):
        print(f"[{r['k']}] P: {r['p']}")
        print(f"[{r['k']}] H: {r['h']}")
