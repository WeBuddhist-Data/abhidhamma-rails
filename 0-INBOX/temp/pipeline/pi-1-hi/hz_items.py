"""Item-by-item comparison of two Hindi renderings of the same Pāli line.

usage: python -I -X utf8 hz_items.py <part1> <id1> <part2> <id2> [line-index-in-segment]
Splits Pāli on spaces/commas/dashes is not reliable, so Hindi is split on ', ' and ' – ' and compared
pairwise by position (both renderings), printing only differing positions.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz_common import segments

SPL = re.compile(r",\s+|\s+[–—]\s+|(?<=[।?])\s+")


def get(part, sid, k):
    for s, ps, hs in segments(part):
        if s == sid:
            return ps[k], hs[k]
    raise SystemExit(f"not found {part} {sid}")


part1, id1, part2, id2 = sys.argv[1:5]
k = int(sys.argv[5]) if len(sys.argv) > 5 else 0
p1, h1 = get(part1, id1, k)
p2, h2 = get(part2, id2, k)
a, b = SPL.split(h1), SPL.split(h2)
print("items", len(a), len(b))
import difflib
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != "equal":
        print(f"[{i1}] {op}: {' | '.join(a[i1:i2])}  ==>  {' | '.join(b[j1:j2])}")
