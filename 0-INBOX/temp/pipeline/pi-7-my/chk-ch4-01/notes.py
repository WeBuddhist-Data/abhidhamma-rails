import sys, importlib.util, pathlib, re, collections
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F, K, D = X.F, X.K, X.D
src = (X.PALI / X.NAMES[0]).read_text(encoding="utf-8-sig")
parts = D.parts_of(src)
seen = collections.OrderedDict()
for d, t in parts:
    D.set_dyad(F, d); D.set_dyad(X.FG, d)
    pt = D.prep(t, d)
    D.chapter_notes(pt, d)
    s = re.sub(r"\{[^{}]*\}", "", pt)
    for m in re.finditer(r"\(([^()]*)\)", s):
        k = m[0]
        if re.fullmatch(r"\(\d+\)", k): continue
        ok = k in F.NOTES or F.lc(k) in F.NOTES
        if not ok:
            try:
                ok = K.note_unit(k) is not None
            except Exception:
                ok = False
        seen.setdefault(k, (d, ok))
for k, (d, ok) in seen.items():
    if not ok: print(d, "|", k)
print(sum(1 for v in seen.values() if not v[1]), "unrendered of", len(seen))
