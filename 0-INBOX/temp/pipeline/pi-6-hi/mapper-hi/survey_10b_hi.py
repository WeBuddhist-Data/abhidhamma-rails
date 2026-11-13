"""Survey the keywords of 10-07..10-13: unique keyword (lower-case first letter), count, files, current default
(pi6_value with PI6 [+ map_10_common_hi + map_10b_hi T if importable]) and the pi-1..5 prior values.
usage: python -I -X utf8 survey_10b_hi.py [missing-only]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI6, lc, prior, read_keywords, pi6_value  # noqa: E402

FILES = [f"10-{n:02d}-indriyayamaka" for n in range(7, 14)]
table = dict(PI6)
try:
    import map_10_common_hi as C  # noqa: E402
    table.update(C.IND)
except ImportError:
    pass
if len(sys.argv) > 2 and sys.argv[2] == "withT":
    import map_10b_hi as B  # noqa: E402
    table.update(B.T)
miss_only = len(sys.argv) > 1 and sys.argv[1] == "missing"
cnt, files = collections.Counter(), collections.defaultdict(set)
for f in FILES:
    for bid, kws in read_keywords(f):
        for k in kws:
            cnt[k] += 1
            files[k].add(f[3:5])
for k in sorted(cnt, key=lc):
    try:
        v = pi6_value(k, [k], table)
    except KeyError:
        v = "?"
    if miss_only and v != "?":
        continue
    pr = {n: dict(c.most_common(2)) for n, c in prior(k).items()}
    print(k, cnt[k], ",".join(sorted(files[k])), "|", v, "|", pr if pr else "-")
