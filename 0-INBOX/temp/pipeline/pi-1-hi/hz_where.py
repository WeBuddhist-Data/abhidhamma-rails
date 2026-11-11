"""List where Pāli regexes occur: part, segment id, line index in segment.

usage: python -I -X utf8 hz_where.py <regex> [<regex> ...]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz_common import PARTS, segments

for rx in sys.argv[1:]:
    r = re.compile(rx)
    hits = []
    for part in PARTS:
        for sid, ps, hs in segments(part):
            for k, p in enumerate(ps):
                if r.search(p):
                    hits.append(f"{part[:4]}:{sid}:{k}")
    print(f"{rx}: {len(hits)} :: {' '.join(hits[:40])}")
