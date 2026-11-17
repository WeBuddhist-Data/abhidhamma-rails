"""List distinct keywords of a part with counts and first ids. usage: python -I -X utf8 kwlist_pi2_ru.py PART"""
import collections
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi2_ru import read_keywords  # noqa: E402

c, first = collections.Counter(), {}
for bid, kws in read_keywords(sys.argv[1]):
    for k in kws:
        c[k] += 1
        first.setdefault(k, bid)
print(len(c))
print(" | ".join(f"{k}:{n}:{first[k]}" for k, n in sorted(c.items())))
