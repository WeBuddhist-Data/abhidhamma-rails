"""read-only helper: per segment, the unmapped keywords, then the Pāli (optional) and the Burmese.
usage: unm.py CH [--pali] [--from SID --to SID]"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
a = sys.argv[1:]
import map_all as M
ch = a[0]; showp = "--pali" in a
lo = a[a.index("--from") + 1] if "--from" in a else None
hi = a[a.index("--to") + 1] if "--to" in a else None
my, pa, rows = M.load(ch)
on = lo is None
for sid, kws in rows:
    if sid == lo: on = True
    if not on: continue
    miss = []
    for kw in [k.strip() for k in kws.split(", ")]:
        try:
            M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
        except KeyError:
            miss.append(kw)
    if miss:
        print("==", sid, "|", ", ".join(miss))
        if showp: print("P:", pa.get(sid))
        print("B:", my[sid])
    if sid == hi: break
