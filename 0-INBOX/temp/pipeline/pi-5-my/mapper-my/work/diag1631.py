"""diagnostics for the ch16-31 group: map chapters with map_ch16-31 (if present) and print unmapped / problems / values."""
import sys, collections, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map5_rules as R
p = HERE / "map_ch16-31.py"
if p.exists():
    spec = importlib.util.spec_from_file_location("m1631", p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); M = m.mapper()
else:
    import map_ch1 as C1
    class M1(R.Mapper):
        def lookup(self, ch, sid, kw, pali, my):
            if R.table_get(self.ctx.get(sid, {}), kw) is None and R.table_get(self.tables.get(ch, {}), kw) is None \
               and R.table_get(R.FRAME, kw) is None and R.table_get(R.STOCK, kw) is None:
                v = R.table_get(C1.T_CH1, kw)
                if v is not None and not v.startswith("@") and R.presence(v, my)[0]:
                    self.SRC[(sid, kw)] = "ch1"; return v
            return super().lookup(ch, sid, kw, pali, my)
    M = M1(funcs=C1.FUNCS1)
chs = sys.argv[1].split(",")
mode = sys.argv[2] if len(sys.argv) > 2 else "summary"
for ch in chs:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    print("##", ch, "lines", len(lines), "unmapped", len(unmapped), "problems", len(problems), "NONE", nne)
    if mode == "summary":
        for sid, k in unmapped: print("  U", sid, k)
        for p_ in problems: print("  P", p_)
    if mode == "uniq":
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
