"""List unique keywords of the 6/9 files: count, current default value (or MISSING), prior values.
usage: python -I -X utf8 kw_6_9_hi.py [file ...]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, pi6_value, prior, PI6  # noqa: E402

FILES = sys.argv[1:] or ["6-01-sankharayamaka", "6-02-sankharayamaka", "9-01-dhammayamaka",
                         "9-02-dhammayamaka", "9-03-dhammayamaka"]
try:
    from map_6_9_hi import TABLE
except Exception:
    TABLE = PI6
cnt = collections.Counter()
ctx = {}
for f in FILES:
    for bid, kws in read_keywords(f):
        for k in kws:
            cnt[k] += 1
            ctx.setdefault(k, (f, bid, kws))
for k, n in sorted(cnt.items(), key=lambda x: x[0].lower()):
    f, bid, kws = ctx[k]
    try:
        v = pi6_value(k, kws, TABLE)
    except KeyError:
        v = "MISSING"
    pr = {b: dict(c.most_common(3)) for b, c in prior(k).items()}
    print(f"{k} [{n}] = {v}   {pr if pr else ''}")
