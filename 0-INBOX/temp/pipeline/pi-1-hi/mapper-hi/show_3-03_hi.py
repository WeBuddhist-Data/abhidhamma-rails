"""Print Pāli / Hindi / keywords side by side for 3-03-rupakandam segments.

usage: python -I -X utf8 show_3-03_hi.py FROM_INDEX TO_INDEX   (0-based indices into the keyword file)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import read_keywords, read_hindi, read_pali  # noqa: E402

PART = "3-03-rupakandam"
a, b = int(sys.argv[1]), int(sys.argv[2])
kws = read_keywords(PART)
hi, pi = read_hindi(PART), read_pali(PART)
for i, (bid, k) in enumerate(kws[a:b], a):
    print(f"=== {i} [{bid}]")
    print("PI:", pi.get(bid))
    print("HI:", hi.get(bid))
    print("KW:", ", ".join(k))
