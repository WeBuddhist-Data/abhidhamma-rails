"""Survey helper for map_7a_hi.py: unique keywords of the given files, count, current default value, prior values.
usage: python -I -X utf8 map_7a_survey_hi.py 7-01-anusayayamaka [...]   (prints only; writes nothing)"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, pi6_value, PI6, prior  # noqa: E402

try:
    from map_7_common_hi import T7  # noqa: E402
except Exception:
    T7 = {}

cnt = collections.Counter()
for f in sys.argv[1:]:
    for bid, kws in read_keywords(f):
        for k in kws:
            cnt[k] += 1
for k, n in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
    try:
        v = pi6_value(k, [k], {**PI6, **T7})
    except KeyError:
        v = "???"
    p = prior(k)
    ps = "; ".join(f"{b}:" + "|".join(f"{x}({c})" for x, c in c_.most_common(3)) for b, c_ in p.items())
    print(f"{n:4d}  {k} = {v}    [{ps}]")
