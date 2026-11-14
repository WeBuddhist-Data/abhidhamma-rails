"""Probe helper for map_2-05_3-01_ru.py: list keywords of a part not covered by CH2 (with counts),
or print the Russian + Pāli of given segment ids.

usage: python -I -X utf8 probe_2-05_3-01_ru.py PART            (uncovered keywords)
       python -I -X utf8 probe_2-05_3-01_ru.py PART id1 id2 ... (show segments)
"""
import collections
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_ru import CH2, lc, read_keywords, read_pali, read_russian  # noqa: E402

part = sys.argv[1]
if len(sys.argv) > 2:
    ru, pi = read_russian(part), read_pali(part)
    kw = dict(read_keywords(part))
    for bid in sys.argv[2:]:
        print("==", bid)
        print("PI:", pi.get(bid))
        print("RU:", ru.get(bid))
        print("KW:", ", ".join(kw.get(bid, [])))
else:
    c = collections.Counter()
    for bid, kws in read_keywords(part):
        for k in kws:
            if lc(k) not in CH2 and not lc(k).startswith("samaye "):
                c[k] += 1
    for k, n in sorted(c.items()):
        print(n, k)
