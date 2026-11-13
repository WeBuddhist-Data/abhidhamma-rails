"""List the unique keywords of the 3-0x Āyatana files with their default value (PI6/PI2/CH2) and how often the
default is present in the segment's Hindi.  usage: python -I -X utf8 kw_3_hi.py [file ...]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, pi6_value, present, PI6, lc, prior  # noqa: E402

try:
    from map_3_hi import T  # noqa: E402
except Exception:
    T = {}

ALL = "all" in sys.argv
files = [a for a in sys.argv[1:] if a != "all"] or [f"3-0{i}-ayatanayamaka" for i in range(1, 7)]
stat = collections.defaultdict(lambda: [0, 0, set(), set()])
for f in files:
    hi = read_hindi(f)
    for bid, kws in read_keywords(f):
        for kw in kws:
            k = kw
            try:
                v = pi6_value(kw, kws, {**PI6, **T}, bid, hi.get(bid))
            except KeyError:
                v = None
            s = stat[k]
            s[0] += 1
            if v is not None and present(v, hi.get(bid)):
                s[1] += 1
            else:
                s[3].add(bid)
            s[2].add(v)
for k in sorted(stat, key=lambda x: lc(x)):
    n, ok, vs, miss = stat[k]
    if ok < n or ALL:
        print(f"{k} | n={n} ok={ok} | {vs} | miss {sorted(miss)[:6]}")
