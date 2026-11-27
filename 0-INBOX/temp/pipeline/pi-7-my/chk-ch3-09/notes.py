import sys, importlib.util, pathlib, re, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
F, M3, K = mk.F, mk.M3, mk.K
src = (mk.PALI / mk.NAMES[0]).read_text(encoding="utf-8-sig")
cnt = collections.Counter()
ok = collections.Counter()
for d, t in M3.parts_of(src):
    M3.set_dyad(F, d); M3.set_dyad(mk.FG, d)
    p = M3.prep(t, d)
    M3.chapter_notes(p, d)
    s = re.sub(r"\{[^{}]*\}", "", p)
    for m in re.finditer(r"\([^()]*\)", s):
        k = m[0]
        if re.fullmatch(r"\(\d+\)", k): continue
        if k in F.NOTES or F.lc(k) in F.NOTES:
            ok[k] += 1; continue
        try:
            r = K.note_unit(k)
        except Exception as e:
            r = None
        if r is None:
            cnt[(d, k)] += 1
        else:
            ok[k] += 1
for (d, k), n in sorted(cnt.items(), key=lambda x: -x[1]):
    print(n, d, k)
print(len(cnt), "unknown;", len(ok), "known")
