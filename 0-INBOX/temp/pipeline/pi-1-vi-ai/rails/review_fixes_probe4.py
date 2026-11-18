"""Compact listing: for every Vietnamese line matching <vi_regex>, show ID, the Pāli window at the same relative spot
and the Vietnamese window around the match.

usage: python -I -X utf8 review_fixes_probe4.py <vi_regex> [before] [after] [--bak]
"""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_fixes_probe_lib import aligned, PARTS, VDIR, BAK

a = sys.argv[1:]
vdir = VDIR
if "--bak" in a:
    a.remove("--bak"); vdir = BAK
rx = re.compile(a[0])
b = int(a[1]) if len(a) > 1 else 20
f = int(a[2]) if len(a) > 2 else 80
n = 0
for part in PARTS:
    pl, vl, sid = aligned(part, vdir)
    for k, (p, v) in enumerate(zip(pl, vl)):
        for m in rx.finditer(v):
            n += 1
            print(f"{part[:4]} L{k + 1} ^{sid.get(k)} | V: …{v[max(0, m.start() - b):m.end() + f]}")
print("occurrences:", n)
