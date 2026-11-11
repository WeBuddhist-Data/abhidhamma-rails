"""Count distinct Hindi matches of a regex per part (optionally only on lines whose Pāli matches a regex).

usage: python -I -X utf8 hz_kwic.py <hindi_regex> [pali_regex] [parts-prefix,...] [--bak]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz_common import PARTS, HERE, pairs

args = [a for a in sys.argv[1:] if not a.startswith("--")]
hdir = os.path.join(HERE, "backup-pre-harmonise") if "--bak" in sys.argv else None
hr = re.compile(args[0])
pr = re.compile(args[1]) if len(args) > 1 and args[1] else None
pref = args[2].split(",") if len(args) > 2 else None
for part in PARTS:
    if pref and not any(part.startswith(x) for x in pref):
        continue
    c = collections.Counter()
    for p, h in (pairs(part, hdir) if hdir else pairs(part)):
        if pr and not pr.search(p):
            continue
        for m in hr.finditer(h):
            c[m.group(0)] += 1
    if c:
        print("===", part)
        for k, v in c.most_common():
            print(f"  {v:4d}  {k}")
