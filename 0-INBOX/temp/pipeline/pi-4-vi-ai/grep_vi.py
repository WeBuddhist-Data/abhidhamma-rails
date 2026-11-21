"""Regex over the 12 pi-4 Vietnamese zero-shot files (or the Pāli with --pali), printing the match with context.

usage: python -I -X utf8 grep_vi.py <regex> [ctx=60] [--pali] [--bak]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, segments, short

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
rx = re.compile(args[0])
ctx = int(args[1]) if len(args) > 1 else 60
n = 0
for part in PARTS:
    for sid, ps, vs in segments(part):
        for i, (p, v) in enumerate(zip(ps, vs)):
            t = p if "--pali" in sys.argv else v
            for m in rx.finditer(t):
                n += 1
                a, b = max(0, m.start() - ctx), min(len(t), m.end() + ctx)
                print(f"{short(part)}:{sid}.{i+1} | {t[a:b]}")
print("matches:", n)
