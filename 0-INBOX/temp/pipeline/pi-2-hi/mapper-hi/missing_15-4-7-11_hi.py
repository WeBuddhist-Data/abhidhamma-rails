"""List unique keywords of a chapter whose default (chapter script resolver, else PI2) is missing or absent
from the segment's Hindi, with the segment ids and the pi-1/3/4/5 values.

usage: python -I -X utf8 missing_15-4-7-11_hi.py <chapter> [id ...]
"""
import collections
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import PI2, pi2_value, read_keywords, read_hindi, present, prior, lc  # noqa: E402

ch, ids = sys.argv[1], set(sys.argv[2:])
resolver = None
p = HERE / f"map_{ch}_hi.py"
if p.exists():
    spec = importlib.util.spec_from_file_location("chmod", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    resolver = m.resolver
hi = read_hindi(ch)
bad = collections.defaultdict(list)
for bid, kws in read_keywords(ch):
    if ids and bid not in ids:
        continue
    for kw in kws:
        try:
            v = resolver(bid, kw, kws) if resolver else pi2_value(kw, kws, PI2, bid, hi.get(bid))
            if present(v, hi.get(bid, "")):
                continue
        except KeyError:
            v = "???"
        bad[(lc(kw), v)].append(bid)
for (k, v), bids in sorted(bad.items()):
    pr = "; ".join(f"pi{n}: " + " | ".join(f"{x}({c})" for x, c in cnt.most_common(3)) for n, cnt in prior(k).items())
    print(f"{k} = {v}  [{' '.join(bids[:6])}{' …' if len(bids) > 6 else ''}]  :: {pr}")
