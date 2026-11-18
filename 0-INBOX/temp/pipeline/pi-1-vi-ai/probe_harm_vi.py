"""Probe for the harmonise pass: print aligned Pāli / Vietnamese lines whose Pāli (or Vietnamese) matches a regex.

usage: python -I -X utf8 probe_harm_vi.py <pali_regex> [--vi <vi_regex>] [--parts 2-03,4-01] [--max N] [--bak] [--short]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, segments

args = sys.argv[1:]


def opt(name, default=None):
    if name in args:
        i = args.index(name)
        return args[i + 1]
    return default


if "--bak" in args:
    vi_common.CUR["vdir"] = vi_common.BAK
prx = re.compile(args[0])
vrx = re.compile(opt("--vi")) if opt("--vi") else None
parts = opt("--parts")
mx = int(opt("--max", "40"))
shortp = "--short" in args
n = 0
for part in PARTS:
    if parts and not any(part.startswith(x) for x in parts.split(",")):
        continue
    k = 0
    for sid, ps, vs in segments(part):
        for i, (p, v) in enumerate(zip(ps, vs)):
            k += 1
            if not prx.search(p):
                continue
            if vrx and not vrx.search(v):
                continue
            n += 1
            if n <= mx:
                print(f"== {part[:4]} ^{sid} (nonempty line {k})")
                if not shortp:
                    print("P:", p)
                print("V:", v)
print("matches:", n)
