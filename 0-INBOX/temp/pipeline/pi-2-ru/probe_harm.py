"""Probe for the harmonise pass: print aligned Pāli/Russian lines whose Pāli (or Russian with -r) matches a regex.
usage: python -I -X utf8 probe_harm.py <regex> [-r] [--cur] [--pi1] [--max N] [--cut N]
  -r: match the Russian line instead; --cur: current outputs (default backup); --pi1: scan pi-1 rails instead
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ru_common
from ru_common import PARTS, PARTS1, pairs, R1DIR, P1DIR, ID

a = sys.argv[1:]
rx = re.compile(a[0])
onru = "-r" in a
mx = int(a[a.index("--max") + 1]) if "--max" in a else 50
cut = int(a[a.index("--cut") + 1]) if "--cut" in a else 100000
if "--cur" not in a:
    ru_common.CUR["rdir"] = ru_common.BAK
n = 0
plist = PARTS1 if "--pi1" in a else PARTS
for part in plist:
    pr = pairs(part, R1DIR, P1DIR) if "--pi1" in a else pairs(part)
    for i, (p, r) in enumerate(pr):
        if rx.search(r if onru else p):
            n += 1
            if n <= mx:
                print(f"[{part[:6]} L{i+1}] P: {p[:cut]}\n    R: {r[:cut]}")
print("matches:", n)
