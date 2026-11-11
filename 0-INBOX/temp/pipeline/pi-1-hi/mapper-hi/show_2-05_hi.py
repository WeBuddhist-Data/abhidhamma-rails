"""Print the Pāli and Hindi of given segment ids of 2-05 (read-only helper).
usage: python -I -X utf8 show_2-05_hi.py ID [ID ...]   (prefix with p: for Pāli only, h: for Hindi only)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import read_hindi, read_pali  # noqa: E402

PART = "2-05-cittuppadakandam"
hi, pi = read_hindi(PART), read_pali(PART)
for a in sys.argv[1:]:
    mode, bid = ("b", a)
    if a[:2] in ("p:", "h:"):
        mode, bid = a[0], a[2:]
    print(f"== {bid}")
    if mode in "bp":
        print("PI:", pi.get(bid))
    if mode in "bh":
        print("HI:", hi.get(bid))
