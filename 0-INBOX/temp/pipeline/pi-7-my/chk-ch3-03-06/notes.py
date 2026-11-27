import sys, pathlib, importlib.util, re, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-03-06.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
mk.K.CUR["fix"] = True
K, F = mk.K, mk.F
cnt = collections.Counter(); where = {}
for n in (sys.argv[1:] or mk.NAMES):
    src = (mk.PALI / n).read_text(encoding="utf-8-sig")
    for d, t in mk.M3.parts_of(src):
        mk.M3.set_dyad(F, d); mk.M3.set_dyad(mk.FG, d)
        t2 = mk.M3.prep(t, d)
        s = re.sub(r"\{[^{}]*\}", "", t2)
        for m in re.finditer(r"\(([^()]*)\)", s):
            k = m[0]
            if re.fullmatch(r"\(\d+\)", k) or k in F.NOTES: continue
            try:
                r = K.note_unit(k)
            except Exception as e:
                r = None
            if r is None:
                cnt[k] += 1; where.setdefault(k, (n, d))
for k, v in cnt.most_common():
    print(v, where[k], k)
