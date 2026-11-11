"""Print Pāli (and optionally Hindi / keywords) segments for given ids of a part.

usage: python -I -X utf8 show_4-02_4-03_hi.py PART id1 id2 ... [-h] [-k]
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import read_pali, read_hindi, read_keywords  # noqa: E402

part = sys.argv[1]
ids = [a for a in sys.argv[2:] if not a.startswith("-")]
pi = read_pali(part)
hi = read_hindi(part) if "-h" in sys.argv else {}
kw = dict(read_keywords(part)) if "-k" in sys.argv else {}
for i in ids:
    print(f"[{i}] PI:", pi.get(i))
    if hi:
        print(f"[{i}] HI:", hi.get(i))
    if kw:
        print(f"[{i}] KW:", ", ".join(kw.get(i, [])))
    print()
