import sys, os, re
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *

m = defaultdict(lambda: defaultdict(list))
for fn in FILES:
    P, H = pairs(fn)
    for i, (a, b) in enumerate(zip(P, H), 1):
        if a.startswith("#"):
            ka = IDRE.sub("", a).strip()
            kb = IDRE.sub("", b).strip()
            ka = re.sub(r"^#+\s*", "", ka); kb = re.sub(r"^#+\s*", "", kb)
            m[ka][kb].append(f"{fn[:4]}:{i}")
for ka in sorted(m):
    for kb, locs in m[ka].items():
        print(f"{ka} || {kb} || {len(locs)} {locs[:3]}")
