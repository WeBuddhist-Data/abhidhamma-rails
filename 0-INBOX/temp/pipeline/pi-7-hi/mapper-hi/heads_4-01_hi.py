"""List heading segments of 4-01 with Pāli | Hindi (filtered by optional substring).
usage: python -I -B -X utf8 heads_4-01_hi.py [filter]"""
import sys, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_hindi, read_pali

F = "4-01-kilesagocchaka"
hi, pa = read_hindi(F), read_pali(F)
flt = sys.argv[1] if len(sys.argv) > 1 else None
seen = set()
for bid, t in pa.items():
    if t.startswith("#"):
        key = (t, hi.get(bid))
        if key in seen and not flt:
            continue
        seen.add(key)
        if flt and flt not in t:
            continue
        print(bid, "|", t, "|", hi.get(bid))
