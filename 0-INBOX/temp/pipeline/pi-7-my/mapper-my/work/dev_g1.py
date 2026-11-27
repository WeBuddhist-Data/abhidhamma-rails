"""g1 dev helper: dry run of the g1 chapters with map_g1 tables (if present) and dump sources."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map7_rules as R
try:
    import map_g1 as G
    M = G.mapper()
except Exception as e:
    print("no map_g1:", e)
    M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
CH = ["1-01-kusalattika", "1-03-vipakattika", "1-04-upadinnattika", "1-05-sankilitthattika"]
mode = sys.argv[1] if len(sys.argv) > 1 else "sum"
out = HERE / "work" / f"dev-g1-{mode}.txt"
L = []
pairs = collections.Counter(); srcs = {}
for ch in CH:
    my, pa = R.burmese(ch), R.pali(ch)
    lines, problems, unmapped, nne = M.map_chapter(ch)
    L.append(f"{ch}: lines {len(lines)} problems {len(problems)} unmapped {len(unmapped)} NDE {nne}")
    for x in unmapped: L.append(f"  UNMAPPED {x}")
    for x in problems: L.append(f"  FAIL {x}")
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            s = M.SRC.get((sid, k)) or "?"
            pairs[(k, v, s.split(":")[0] if not s.startswith("base") else s)] += 1
            if s == "stem" or s.endswith("stem"):
                L.append(f"  STEM ^{sid} {k} = {v}\n      PA: {pa.get(sid,'')[:300]}\n      MY: {my[sid][:400]}")
src = collections.Counter()
for (k, v, s), c in pairs.items(): src[s.split(':')[0]] += c
L.append("sources " + str(src.most_common()))
if mode == "pairs":
    for (k, v, s), c in sorted(pairs.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
        L.append(f"{k}\t{v}\t{c}\t{s}")
out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(out)
