"""Print Pāli + Hindi for a range of segments of part 5 (helper for reading).
usage: python -I -X utf8 show_5-atthakathakandam.py START END [nopali]
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import read_keywords, read_hindi, read_pali  # noqa: E402

PART = "5-atthakathakandam"
kws = read_keywords(PART)
hi = read_hindi(PART)
pi = read_pali(PART)
a, b = int(sys.argv[1]), int(sys.argv[2])
nopali = len(sys.argv) > 3
for i, (bid, k) in enumerate(kws[a:b], start=a):
    print(f"#{i} [{bid}]")
    if not nopali:
        print("PI:", pi.get(bid, "??"))
    print("HI:", hi.get(bid, "??"))
    print()
