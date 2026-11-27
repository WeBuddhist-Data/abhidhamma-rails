"""diagnostics for the ch2-15 group: map chapters with map_ch2-15 tables (if importable) and print unmapped / problems."""
import sys, collections, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map5_rules as R
spec = importlib.util.spec_from_file_location("m215", HERE / "map_ch2-15.py")
try:
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); M = m.mapper()
except FileNotFoundError:
    M = R.Mapper()
chs = sys.argv[1].split(",")
mode = sys.argv[2] if len(sys.argv) > 2 else "summary"
for ch in chs:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    print("##", ch, "lines", len(lines), "unmapped", len(unmapped), "problems", len(problems), "NONE", nne)
    if mode in ("summary",):
        for sid, k in unmapped: print("  U", sid, k)
        for p in problems: print("  P", p)
    if mode == "uniq":
        import collections
        vals = collections.defaultdict(collections.Counter)
        for l in lines:
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                vals[k][(v, M.SRC.get((sid, k), "?"))] += 1
        for k in vals:
            print(k, "=", " | ".join(f"{v}<{s}>{n if n > 1 else ''}" for (v, s), n in vals[k].most_common()))
    if mode == "values":
        for l in lines:
            sid, rest = l[1:].split("] ", 1)
            print(f"[{sid}]")
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                print(f"   {k} = {v}   <{M.SRC.get((sid, k), '?')}>")
