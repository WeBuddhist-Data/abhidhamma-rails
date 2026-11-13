"""Survey the keywords of 10-01 .. 10-06 (Indriyayamaka, first half): distinct keywords (lower-case first letter),
count, the default value the tables would give (PI6/PI2/CH2, after -ti/-ñca stripping) and the pi-1..5 prior values.
usage: python -I -X utf8 survey_10a_hi.py [file ...]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI6, PI2, CH2, lc, prior, read_keywords, _strip_particles  # noqa: E402

FILES = sys.argv[1:] or [f"10-0{i}-indriyayamaka" for i in range(1, 7)]
cnt = collections.Counter()
where = collections.defaultdict(set)
for f in FILES:
    for bid, kws in read_keywords(f):
        for k in kws:
            cnt[lc(k)] += 1
            where[lc(k)].add(f[:5])


def default(k):
    for cand in [k] + _strip_particles(k):
        for name, t in (("PI6", PI6), ("PI2", PI2), ("CH2", CH2)):
            if cand in t:
                return f"{name}({cand})={t[cand]}"
    return "-"


for k in sorted(cnt):
    pr = {n: dict(c.most_common(3)) for n, c in prior(k).items()}
    print(k, cnt[k], sorted(where[k]), "|", default(k), "|", pr if pr else "-")
