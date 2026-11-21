"""Probe for the harmonise pass: print aligned Pāli / Vietnamese lines.
usage: python -I -X utf8 probe_harm_vi.py verses            (all lines after the first of a multi-line segment)
       python -I -X utf8 probe_harm_vi.py <pali-regex> [chapters,comma] [maxchars]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vi_common import PARTS, segments, pairs, short

if sys.argv[1] == "verses":
    for part in PARTS:
        for sid, ps, vs in segments(part):
            if len(ps) > 1:
                print(f"== {short(part)} ^{sid}")
                for p, v in zip(ps[1:], vs[1:]):
                    print("  P:", p)
                    print("  V:", v)
else:
    rx = re.compile(sys.argv[1])
    chs = sys.argv[2].split(",") if len(sys.argv) > 2 and sys.argv[2] not in ("", "all") else None
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
    for part in PARTS:
        if chs and short(part) not in chs:
            continue
        for sid, ps, vs in segments(part):
            for p, v in zip(ps, vs):
                if rx.search(p):
                    print(f"== {short(part)} ^{sid}")
                    print("P:", p[:mx])
                    print("V:", v[:mx])
