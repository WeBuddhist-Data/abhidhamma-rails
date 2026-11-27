"""dev.py ch [ch …]: map chapters in memory (nothing written) and print unmapped / failing / per-source counts and
the distinct keyword = value pairs (development helper)."""
import sys, pathlib, collections, time
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import map7_rules as R
t0 = time.time()
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))
show = "--pairs" in sys.argv
chs = [a for a in sys.argv[1:] if not a.startswith("--")]
for ch in chs:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    print(ch, "lines", len(lines), "unmapped", len(unmapped), "fails", len(problems), "NDE", nne, f"{time.time()-t0:.1f}s")
    uc = collections.Counter(k for _, k in unmapped)
    print("  UNMAPPED", uc.most_common(60))
    for x in problems[:20]:
        print("  FAIL", x)
    if show:
        pairs = collections.Counter(); src = {}
        for l in lines:
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
                k, v = kv.split("=", 1); pairs[(k, v)] += 1; src.setdefault((k, v), M.SRC.get((sid, k), "?"))
        for (k, v), n in sorted(pairs.items(), key=lambda x: R.low(x[0][0])):
            print(f"  {k} = {v}   [{n} {src[(k, v)]}]")
print("sources", collections.Counter(v.split(':')[0] if v else v for v in M.SRC.values()).most_common())
