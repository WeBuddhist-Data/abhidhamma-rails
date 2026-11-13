import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *

f = sys.argv[1]
pats = sys.argv[2:]
_, _, hn = load(HDIR, f)
pr = pairs(f)
for pat in pats:
    hits = [(n, sid) for (n, sid, p, h) in pr if pat in h]
    ids = []
    for n, sid in hits:
        if sid not in ids:
            ids.append(sid)
    print(pat, "| n:", [n for n, _ in hits], "| ids:", ids)
