"""Probe: aligned lines whose Pāli matches <pali_rx> but whose Russian does NOT match <ru_rx>.
usage: python -I -X utf8 probe_none.py <pali_rx> <ru_rx> [--cur] [--max N] [--cut N]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ru_common
from ru_common import PARTS, pairs

a = sys.argv[1:]
px, rx = re.compile(a[0]), re.compile(a[1])
mx = int(a[a.index("--max") + 1]) if "--max" in a else 40
cut = int(a[a.index("--cut") + 1]) if "--cut" in a else 300
if "--cur" not in a:
    ru_common.CUR["rdir"] = ru_common.BAK
n = 0
for part in PARTS:
    for i, (p, r) in enumerate(pairs(part)):
        if px.search(p) and not rx.search(r):
            n += 1
            if n <= mx:
                print(f"[{part[:6]} L{i+1}] P: {p[:cut]}\n    R: {r[:cut]}")
print("matches:", n)
