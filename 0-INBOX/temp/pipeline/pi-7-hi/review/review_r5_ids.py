import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *
# usage: ids.py "3-02:277,3-02:278"  -> segment id + non-empty line number
cache = {}
for spec in sys.argv[1].split(","):
    f, n = spec.split(":"); n = int(n)
    fn = [x for x in FILES if x.startswith(f)][0]
    if fn not in cache:
        P, H = pairs(fn)
        segs = segments(P)
        m = {}
        for sid, lines in segs:
            for (ln, ne, _) in lines:
                m[ln] = (sid, ne)
        cache[fn] = m
    sid, ne = cache[fn][n]
    print(f"{spec} -> ID ^{sid}, ne{ne}")
