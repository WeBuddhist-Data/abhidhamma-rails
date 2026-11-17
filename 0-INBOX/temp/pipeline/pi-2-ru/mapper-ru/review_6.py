"""Distinct keyword -> values (with counts and first id) of the chapter 6 resolver, for review (no writing).
usage: python -I -X utf8 review_6.py"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_6_ru as M  # noqa: E402

res = M.resolver_for(M.PART)
agg = collections.defaultdict(collections.Counter)
first = {}
for bid, kws in M.read_keywords(M.PART):
    for kw in kws:
        v = res(bid, kw, kws)
        agg[kw][v] += 1
        first.setdefault((kw, v), bid)
for kw in sorted(agg, key=lambda x: x.lower()):
    print(kw + ": " + " | ".join(f"{v} ({n}, {first[(kw, v)]})" for v, n in agg[kw].most_common()))
