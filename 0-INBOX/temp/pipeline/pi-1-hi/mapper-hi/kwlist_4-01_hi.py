"""List the distinct keywords of 4-01 with counts and their CH2 / matrix default (helper)."""
import collections
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import read_keywords, CH2, lc, matrix_names  # noqa: E402

PART = "4-01-nikkhepakandam"
MN = matrix_names()
cnt = collections.Counter()
for bid, kws in read_keywords(PART):
    for k in kws:
        cnt[k] += 1
for k, n in sorted(cnt.items(), key=lambda x: lc(x[0])):
    d = CH2.get(lc(k))
    m = MN.get(k) or MN.get(lc(k))
    print(f"{n:4d} {k} | CH2={d} | MX={m}")
