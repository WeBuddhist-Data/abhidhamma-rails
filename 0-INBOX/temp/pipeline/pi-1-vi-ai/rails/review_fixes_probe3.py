"""List aligned lines whose Pāli matches <pali_regex> but whose Vietnamese does NOT match <vi_regex>.

usage: python -I -X utf8 review_fixes_probe3.py <pali_regex> <vi_regex> [--full]
"""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_fixes_probe_lib import aligned, PARTS

a = sys.argv[1:]
full = "--full" in a
if full:
    a.remove("--full")
prx, vrx = re.compile(a[0]), re.compile(a[1])
n = m = 0
for part in PARTS:
    pl, vl, sid = aligned(part)
    for k, (p, v) in enumerate(zip(pl, vl)):
        if prx.search(p):
            n += 1
            if not vrx.search(v):
                m += 1
                print(f"[{part[:4]} L{k + 1} ^{sid.get(k)}]")
                print("  P:", p if full else p[:400])
                print("  V:", v if full else v[:400])
print("pali matches:", n, "vi misses:", m)
