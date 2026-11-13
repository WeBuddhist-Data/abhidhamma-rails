"""Survey of the unique keywords in 7-06 .. 7-11 (read-only; prints only).
usage: python -I -X utf8 survey_7b_hi.py [table]   (table: also show the value map_7b_hi would give)"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, pi6_value, PI6, prior  # noqa: E402

FILES = [f"7-{i:02d}-anusayayamaka" for i in range(6, 12)]
cnt = collections.Counter()
where = collections.defaultdict(set)
for f in FILES:
    for bid, kws in read_keywords(f):
        for k in kws:
            cnt[k] += 1
            where[k].add(f[:4])
table = PI6
if len(sys.argv) > 1:
    import map_7b_hi as M
    table = M.TABLE
for k, n in sorted(cnt.items(), key=lambda x: x[0].lower()):
    try:
        v = pi6_value(k, [k], table)
    except KeyError:
        v = "???"
    pr = prior(k)
    prs = "; ".join(f"pi-{b}:" + "|".join(f"{x}({c})" for x, c in pv.most_common(3)) for b, pv in pr.items())
    print(f"{k}\t{n}\t{','.join(sorted(where[k]))}\t{v}\t{prs}")
