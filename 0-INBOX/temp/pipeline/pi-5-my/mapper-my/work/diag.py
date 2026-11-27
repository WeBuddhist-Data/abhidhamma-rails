"""diagnostics: map a chapter with the module (+ map_ch1 tables if importable) and print unmapped / problems / values."""
import sys, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
try:
    import map_ch1 as C
    M = C.mapper()
except Exception as e:
    print("no map_ch1:", e); M = R.Mapper()
ch = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "summary"
lines, problems, unmapped, nne = M.map_chapter(ch)
vals = collections.defaultdict(collections.Counter); src = collections.defaultdict(collections.Counter)
for l in lines:
    sid, rest = l[1:].split("] ", 1)
    for kv in rest.split(", "):
        k, v = kv.split("=", 1); vals[k][v] += 1; src[k][M.SRC.get((sid, k), "?")] += 1
u = collections.Counter(k for _, k in unmapped)
print("lines", len(lines), "unmapped uses", len(unmapped), "distinct", len(u), "problems", len(problems), "NONE", nne)
if mode in ("summary", "unmapped"):
    for k, n in u.most_common():
        print(f"  U {n:4d} {k}  e.g. " + " ".join([s for s, kk in unmapped if kk == k][:4]))
if mode in ("summary", "problems"):
    for p in problems[:80]: print("  P", p)
if mode == "values":
    for k in sorted(vals, key=lambda k: -sum(vals[k].values())):
        print(f"{sum(vals[k].values()):4d} {k} = " + " | ".join(f"{v} ({n})" for v, n in vals[k].most_common()) + "   [" + ",".join(f"{s}:{n}" for s, n in src[k].items()) + "]")
