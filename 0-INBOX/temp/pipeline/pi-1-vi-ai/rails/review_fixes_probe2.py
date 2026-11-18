"""Show a window of the aligned Pāli / Vietnamese line after an anchor.

usage: python -I -X utf8 review_fixes_probe2.py <pali_regex> <pali_anchor> <vi_anchor> [width] [--bak]
Prints, per matching line, the Pāli text from <pali_anchor> and the Vietnamese text from <vi_anchor> (width chars).
"""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_fixes_probe_lib import aligned, PARTS, VDIR, BAK

a = sys.argv[1:]
vdir = VDIR
if "--bak" in a:
    a.remove("--bak"); vdir = BAK
prx, pa, va = re.compile(a[0]), a[1], a[2]
w = int(a[3]) if len(a) > 3 else 300
n = 0
for part in PARTS:
    pl, vl, sid = aligned(part, vdir)
    for k, (p, v) in enumerate(zip(pl, vl)):
        if not prx.search(p):
            continue
        n += 1
        pi = p.find(pa); vi = v.find(va)
        print(f"[{part[:4]} L{k + 1} ^{sid.get(k)}]")
        for m in re.finditer(re.escape(pa), p):
            print("  P:", p[m.start():m.start() + w])
        for m in re.finditer(re.escape(va), v):
            print("  V:", v[m.start():m.start() + w])
print("matches:", n)
