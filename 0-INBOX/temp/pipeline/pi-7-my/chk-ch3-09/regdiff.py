import sys, importlib.util, pathlib, difflib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
mk.K.CUR["fix"] = True
for n in sys.argv[1:]:
    if n.startswith("2-"):
        mk.M3.set_dyad(mk.F, None); mk.M3.set_dyad(mk.FG, None)
        txt = mk.M.translate(n)
    elif n in mk.M3.NAMES:
        txt = mk.M3.translate(n)
    else:
        txt = mk.M4.translate(n)
    pub = (mk.OUT / n).read_text(encoding="utf-8").splitlines()
    for i, (a, b) in enumerate(zip(txt.splitlines(), pub)):
        if a != b:
            sm = difflib.SequenceMatcher(None, a, b)
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op != "equal":
                    print(n, i + 1, op, "NEW:", a[max(0, i1 - 40):i2 + 40], "| PUB:", b[max(0, j1 - 40):j2 + 40])
