"""Probe: print aligned pi-5 Pāli / Vietnamese zero-shot lines matching a Pāli regex (and/or a Vietnamese regex).

usage: python -I -X utf8 probe_vi.py <pali_regex|-> [vi_regex|-] [chapters e.g. 10,15 or all] [maxchars] [--bak] [--full]
Prints the location (chapter:block id, line number in the non-empty-line list), a Pāli window and a Vietnamese window
around the first match (or the whole lines with --full).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, segments, short

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
full = "--full" in sys.argv
pr = None if args[0] == "-" else re.compile(args[0])
vr = None if len(args) < 2 or args[1] == "-" else re.compile(args[1])
chs = None if len(args) < 3 or args[2] == "all" else set(args[2].split(","))
maxc = int(args[3]) if len(args) > 3 else 400

for part in PARTS:
    if chs and short(part) not in chs:
        continue
    n = 0
    for sid, ps, vs in segments(part):
        for i, (p, v) in enumerate(zip(ps, vs)):
            n += 1
            mp = pr.search(p) if pr else None
            mv = vr.search(v) if vr else None
            if (pr and not mp) or (vr and not mv):
                continue
            print(f"[{short(part)}:{sid} line {i + 1}/{len(ps)}]")
            if full:
                print("  PI:", p)
                print("  VI:", v)
            else:
                s = max(0, (mp.start() if mp else 0) - maxc // 3)
                print("  PI:", p[s:s + maxc])
                s = max(0, (mv.start() if mv else 0) - maxc // 3)
                print("  VI:", v[s:s + maxc])
