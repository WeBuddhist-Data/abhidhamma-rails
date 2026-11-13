"""List the Pāli word bigrams used in the WHO phrases of answer sentences, with per-file counts."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C
from who_scan6 import SP, COR

cnt = collections.defaultdict(collections.Counter)
for part in C.PARTS:
    for p, h in C.pairs(part):
        if p.startswith("#"):
            continue
        for a in SP.split(C.norm(p)):
            m = COR.match(a)
            if not m or m.group(1).lower().startswith(("yassa", "yattha", "no ca")):
                continue
            w = m.group(1).lower().replace("…pe…", " ").split()
            for i in range(len(w)):
                cnt[w[i]][C.short(part)] += 1
for k, v in sorted(cnt.items(), key=lambda kv: -sum(kv[1].values())):
    print(f"{k:45s} {sum(v.values()):5d} {' '.join(sorted(v))}")
