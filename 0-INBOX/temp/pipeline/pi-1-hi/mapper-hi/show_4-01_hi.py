"""Print Pāli (and optionally Hindi) segments of 4-01 by id. usage: show_4-01_hi.py [h] id id ..."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import read_pali, read_hindi  # noqa: E402

PART = "4-01-nikkhepakandam"
args = sys.argv[1:]
hi = args and args[0] == "h"
if hi:
    args = args[1:]
P = read_pali(PART)
H = read_hindi(PART)
for a in args:
    print(f"== {a} PALI:\n{P.get(a)}")
    if hi:
        print(f"-- HINDI:\n{H.get(a)}")
