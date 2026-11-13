"""Compact KWIC: for lines whose Pāli matches <pali-regex>, print the Pāli match (+-N chars) and each Hindi match (+-M chars).
usage: python -I -B -X utf8 hz7_win.py <pali-regex> <hindi-regex> [pw] [hw] [max] [file-prefix]
"""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz7_common import PARTS, pairs, short

pr, hr = re.compile(sys.argv[1]), re.compile(sys.argv[2])
pw = int(sys.argv[3]) if len(sys.argv) > 3 else 30
hw = int(sys.argv[4]) if len(sys.argv) > 4 else 40
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 100
pref = sys.argv[6] if len(sys.argv) > 6 else ""
n = 0
for part in PARTS:
    if not part.startswith(pref):
        continue
    for i, (p, h) in enumerate(pairs(part)):
        pm = list(pr.finditer(p))
        if not pm:
            continue
        hm = list(hr.finditer(h))
        n += 1
        if n > mx:
            continue
        ps = " | ".join(p[max(0, m.start() - pw):m.end() + pw] for m in pm[:3])
        hs = " | ".join(h[max(0, m.start() - hw):m.end() + hw] for m in hm[:4])
        print(f"{short(part)}:{i+1} P: {ps}\n      H: {hs}")
print("lines:", n)
