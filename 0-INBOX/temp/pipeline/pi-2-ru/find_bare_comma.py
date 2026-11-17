"""Find «X, – это» where the comma follows a plain noun or list (russian-style: comma before the dash only
when it closes a participial phrase or clause). The k-th dash of a Russian line is aligned with the k-th dash
of its Pāli line; a hit needs a Pāli stretch before the dash without a relative/clause word and a Russian
stretch without clause or participle markers.
usage: python -I -X utf8 find_bare_comma.py [--cur]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ru_common
from ru_common import PARTS, pairs

if "--cur" not in sys.argv:
    ru_common.CUR["rdir"] = ru_common.BAK
DASH = re.compile(r"\s[–—]\s")
P_CLAUSE = re.compile(r"\b(?:[Yy]o|[Yy]ā|[Yy]aṃ|[Yy]e|[Yy]asmiṃ|[Yy]assa|[Yy]ena|[Yy]āni|[Yy]āya|[Yy]asmā|[Yy]attha)\b|ti\b|…pe…")
R_CLAUSE = re.compile(r"котор|то, что|что |где |когда |если |чтобы|как |лишь|…")
R_PART = re.compile(r"\w+(?:щ|вш|нн|ённ|енн|ем|им|ом)(?:ий|ая|ое|ие|его|ей|их|ым|ыми|ую|ее|ый|ые|ой|ых|ого|ому|ем|им)\b")
n = 0
for part in PARTS:
    for i, (p, r) in enumerate(pairs(part)):
        pd = [m.start() for m in DASH.finditer(p)]
        rd = [m.start() for m in DASH.finditer(r)]
        if len(pd) != len(rd):
            continue
        for k, (a, b) in enumerate(zip(pd, rd)):
            if r[b - 1] != ",":
                continue
            ps = p[:a]
            ps = re.split(r"[.?;:]\s|\s[–—]\s", ps)[-1]
            rs = r[:b]
            rs = re.split(r"[.?;:]\s|\s[–—]\s", rs)[-1]
            if P_CLAUSE.search(ps) or R_CLAUSE.search(rs):
                continue
            last = rs.rstrip(",").split(",")[-1]
            if R_PART.search(last):
                continue
            n += 1
            print(f"[{part} L{i+1}] P: …{ps[-140:]}\n    R: …{rs[-160:]} –")
print("candidates:", n)
