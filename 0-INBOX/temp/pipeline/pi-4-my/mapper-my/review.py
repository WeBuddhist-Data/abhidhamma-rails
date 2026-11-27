"""read-only helper: distinct (keyword, value, source) of chapters, with count and first segment.
usage: review.py CH[,CH] [src,src]"""
import sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
a = sys.argv[1:]
import map_all as M
chs = a[0].split(","); srcs = set(a[1].split(",")) if len(a) > 1 else None
d = collections.OrderedDict()
for ch in chs:
    my, pa, rows = M.load(ch)
    for sid, kws in rows:
        for kw in [k.strip() for k in kws.split(", ")]:
            v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid]); s = M.SRC.get((sid, kw))
            if srcs and s not in srcs: continue
            key = (kw, v, s)
            if key not in d: d[key] = [0, sid]
            d[key][0] += 1
for (kw, v, s), (n, sid) in d.items():
    print(f"{kw}={v} [{s}] {n} {sid}")
