import sys, re, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("mk", H / "make_ch3-07-08-10.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
D, K, F = mk.D, mk.K, mk.F
seen = {}
for n in mk.NAMES:
    src = (mk.PALI / n).read_text(encoding="utf-8-sig")
    for d, part in D.parts_of(src):
        t = re.sub(r"\{[^{}]*\}", "", part)
        for m in re.finditer(r"\([^()]*\)", t):
            k = m[0]
            if re.fullmatch(r"\(\d+\)", k) or k in D.NOTEP: continue
            r = K.note_unit(k)
            if r is None:
                seen.setdefault(k, (n[:4], d))
for k, v in seen.items():
    print(v, k)
print(len(seen))
