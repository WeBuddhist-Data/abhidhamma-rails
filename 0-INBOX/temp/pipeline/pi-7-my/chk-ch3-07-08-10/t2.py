import sys, importlib.util, pathlib, traceback
sys.dont_write_bytecode = True
H = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("mk", H / "make_ch3-07-08-10.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
D, K, F, M = mk.D, mk.K, mk.F, mk.M
K.CUR["fix"] = True
d = sys.argv[2]
D.set_dyad(F, d); D.set_dyad(D.FG, d); D.FG.translate("")
u = D.prep(sys.argv[3], d)
try:
    print(M._K_UNIT(u))
except Exception:
    traceback.print_exc()
