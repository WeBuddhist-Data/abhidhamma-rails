"""Probe for the review fixes.
usage:
  review_fixes_probe.py id <ID> [<ID> ...]          print Pāli + Vietnamese lines of these segments (pi-2)
  review_fixes_probe.py pali <regex> [max]          lines whose Pāli matches (pi-2), with Vietnamese
  review_fixes_probe.py vi <regex> [max]            lines whose Vietnamese matches (pi-2), with Pāli
  review_fixes_probe.py p1 <regex> [max]            pi-1 lines whose Pāli matches, with pi-1 Vietnamese
  review_fixes_probe.py p1vi <regex> [max]          pi-1 lines whose Vietnamese matches
Add --bak as last arg to read the pi-2 Vietnamese from backup-pre-review.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_fixes_lib import *

args = sys.argv[1:]
vdir = VDIR
if args and args[-1] == "--bak":
    vdir = BAK
    args = args[:-1]
mode = args[0]
if mode in ("kw", "pkw"):  # kw <IDs,|*> <regex> [width]: windows of the Vietnamese (pkw: Pāli) around matches
    want, rx = set(args[1].split(",")), re.compile(args[2])
    w = int(args[3]) if len(args) > 3 else 120
    for part in PARTS:
        pl, vl, sid = aligned(part, vdir)
        for k in range(len(pl)):
            if "*" not in want and sid.get(k) not in want:
                continue
            s = vl[k] if mode == "kw" else pl[k]
            for m in rx.finditer(s):
                a, b = max(0, m.start() - w), min(len(s), m.end() + w)
                print(f"[{part[:3]} ^{sid.get(k)} L{k + 1}] …{s[a:b]}…")
    sys.exit()
if mode == "len":  # len <ID>: line lengths only
    for part in PARTS:
        pl, vl, sid = aligned(part, vdir)
        for k in range(len(pl)):
            if sid.get(k) in args[1:]:
                print(f"[{part[:3]} ^{sid[k]} L{k + 1}] P{len(pl[k])} V{len(vl[k])} | {pl[k][:100]} | {vl[k][:100]}")
    sys.exit()
if mode == "id":
    want = set(args[1:])
    for part in PARTS:
        pl, vl, sid = aligned(part, vdir)
        for k in range(len(pl)):
            if sid.get(k) in want:
                print(f"[{part[:3]} ^{sid[k]} L{k + 1}]\n  P: {pl[k]}\n  V: {vl[k]}")
else:
    rx = re.compile(args[1])
    mx = int(args[2]) if len(args) > 2 else 40
    n = 0
    if mode in ("pali", "vi"):
        for part in PARTS:
            pl, vl, sid = aligned(part, vdir)
            for k in range(len(pl)):
                s = pl[k] if mode == "pali" else vl[k]
                if rx.search(s):
                    n += 1
                    if n <= mx:
                        print(f"[{part[:3]} ^{sid.get(k)} L{k + 1}]\n  P: {pl[k]}\n  V: {vl[k]}")
    else:
        for part in P1_PARTS:
            pl, vl, sid = aligned(part, P1_VDIR, P1_PDIR)
            for k in range(len(pl)):
                s = pl[k] if mode == "p1" else vl[k]
                if rx.search(s):
                    n += 1
                    if n <= mx:
                        print(f"[pi1 {part[:6]} ^{sid.get(k)} L{k + 1}]\n  P: {pl[k]}\n  V: {vl[k]}")
    print("TOTAL", n)
