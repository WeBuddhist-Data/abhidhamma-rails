"""read-only helper: the first N characters of the Burmese (and optionally Pāli) of segments. usage: head.py CH N [p] SID..."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
a = sys.argv[1:]
import map_all as M
my, pa, rows = M.load(a[0]); n = int(a[1]); sids = a[2:]; P = False
if sids and sids[0] == "p": P = True; sids = sids[1:]
for sid in sids:
    print("==", sid)
    if P: print("P:", pa.get(sid, "")[:n])
    print("B:", my[sid][:n])
