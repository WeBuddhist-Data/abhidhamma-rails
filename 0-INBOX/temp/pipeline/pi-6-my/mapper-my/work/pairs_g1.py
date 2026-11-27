"""read-only helper (g1): distinct keyword=value pairs the module gives in the given chapters, with uses and source."""
import sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))
pairs = collections.Counter(); src = {}
for ch in sys.argv[1:]:
    lines, *_ = M.map_chapter(ch)
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            pairs[(k, v)] += 1
            src.setdefault((k, v), M.SRC.get((sid, k), "?"))
for (k, v), c in sorted(pairs.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
    print(f"{k} = {v} | {c} | {src[(k, v)]}")
