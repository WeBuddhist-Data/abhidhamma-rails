"""Probe: aligned sentences (lines split on «. ? ; !» + space; only lines where Pāli and Vietnamese give the same
number of sentences) whose Pāli sentence matches a regex; prints the Vietnamese sentence beside it.
Lines with unequal sentence counts are reported as UNALIGNED with the whole Vietnamese line start.

usage: python -I -X utf8 probe_sent_vi.py <pali-regex> [<vi-regex>] [--bak] [--short]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, segments, short, norm

SPLIT = re.compile(r"(?<=[?.;!])\s+")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
rp = re.compile(args[0])
rv = re.compile(args[1]) if len(args) > 1 and args[1] != "-" else None
lim = 160 if "--short" in sys.argv else 1000
n = un = 0
for part in PARTS:
    for sid, ps, vs in segments(part):
        for i, (p, v) in enumerate(zip(ps, vs)):
            if not rp.search(p):
                continue
            cp = [c for c in SPLIT.split(norm(p)) if c.strip()]
            cv = [c for c in SPLIT.split(norm(v)) if c.strip()]
            if len(cp) != len(cv):
                un += 1
                print(f"UNALIGNED {short(part)}:{sid}.{i+1} ({len(cp)} vs {len(cv)})")
                continue
            for a, b in zip(cp, cv):
                if rp.search(a) and (rv is None or rv.search(b)):
                    n += 1
                    print(f"{short(part)}:{sid}.{i+1} P: {a[:lim]}")
                    print(f"{' ' * len(short(part) + sid)}    V: {b[:lim]}")
print("aligned matches:", n, "unaligned lines:", un)
