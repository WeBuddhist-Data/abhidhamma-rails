"""Lines whose Pāli matches regex A but whose Vietnamese does NOT match regex B (pi-2 rails).
usage: review_fixes_probe2.py <pali-regex> <vi-regex> [width] [--bak]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_fixes_lib import *

args = sys.argv[1:]
vdir = BAK if args[-1] == "--bak" else VDIR
args = [a for a in args if a != "--bak"]
pa, vb = re.compile(args[0]), re.compile(args[1])
w = int(args[2]) if len(args) > 2 else 200
for part in PARTS:
    pl, vl, sid = aligned(part, vdir)
    for k in range(len(pl)):
        if pa.search(pl[k]) and not vb.search(vl[k]):
            m = pa.search(pl[k])
            print(f"[{part[:3]} ^{sid.get(k)} L{k + 1}]\n  P: …{pl[k][max(0, m.start() - 80):m.end() + 80]}…\n  V: {vl[k][:w]}")
