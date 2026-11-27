import sys, importlib.util, pathlib, traceback
sys.dont_write_bytecode = True
H = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("mk", H / "make_ch3-07-08-10.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
D, K, F = mk.D, mk.K, mk.F
K.CUR["fix"] = True
d = sys.argv[2]
for s in sys.argv[3:]:
    D.set_dyad(F, d); D.set_dyad(D.FG, d); D.FG.translate("")
    t = D.prep(s, d)
    print("PREP:", t)
    try:
        print("OUT:", F.translate(t))
    except Exception as e:
        print("ERR:", repr(e)[:1500])
