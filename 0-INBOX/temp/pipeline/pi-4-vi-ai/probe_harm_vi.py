"""Probe for the pi-4 harmonise pass: print aligned Pāli / Vietnamese lines matching a regex (12 pi-4 files only).

usage: python -I -X utf8 probe_harm_vi.py <pali-regex|-> [<vi-regex|->] [--bak] [--full] [--sent]
  --sent: print only the matching sentence pieces (split on «. ? ;») instead of whole lines
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, segments, short

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
rp = None if args[0] == "-" else re.compile(args[0])
rv = None if len(args) < 2 or args[1] == "-" else re.compile(args[1])
full = "--full" in sys.argv
sent = "--sent" in sys.argv
SPLIT = re.compile(r"(?<=[?.;!])\s+")
n = 0
for part in PARTS:
    for sid, ps, vs in segments(part):
        for i, (p, v) in enumerate(zip(ps, vs)):
            if rp and not rp.search(p):
                continue
            if rv and not rv.search(v):
                continue
            n += 1
            if sent:
                sp = [x for x in SPLIT.split(p) if (rp is None or rp.search(x))]
                sv = [x for x in SPLIT.split(v) if (rv is None or rv.search(x))]
                print(f"{short(part)}:{sid}.{i+1} P: {' | '.join(sp)[:400]}")
                print(f"{' ' * len(short(part) + sid)}  V: {' | '.join(sv)[:400]}")
            else:
                lim = None if full else 600
                print(f"{short(part)}:{sid}.{i+1} P: {p[:lim]}")
                print(f"{' ' * len(short(part) + sid)}  V: {v[:lim]}")
print("matches:", n)
