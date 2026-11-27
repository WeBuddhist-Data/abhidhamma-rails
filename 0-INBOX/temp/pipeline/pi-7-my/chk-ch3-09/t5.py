import sys, importlib.util, pathlib, re, traceback
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
F, M3, K = mk.F, mk.M3, mk.K
d = sys.argv[1]
M3.set_dyad(F, d)
F.translate("")
for fr in sys.argv[2:]:
    sk, slots = F.slot(F.lc(M3.prep(fr, d)))
    print("SK:", sk, slots)
    for p in re.split(r"(, |; )", sk.strip().rstrip(".")):
        if p in (", ", "; "): continue
        ti, ci, vi = [0], [0], [0]
        try:
            r = K._piece(p, slots, ti, ci, vi)
        except Exception as e:
            r = repr(e)
        print("  PIECE:", p, "=>", r)
