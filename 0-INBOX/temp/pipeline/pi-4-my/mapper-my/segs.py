"""read-only helper: print Pāli and Burmese of segments. usage: segs.py CH SID..."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
a = sys.argv[1:]
import map_all as M
my, pa, rows = M.load(a[0])
for sid in a[1:]:
    print("==", sid); print(pa.get(sid)); print(my[sid])
