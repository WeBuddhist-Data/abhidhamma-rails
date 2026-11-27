import sys, importlib.util, pathlib, re, traceback
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
F, M3, K, FG, G = mk.F, mk.M3, mk.K, mk.FG, mk.G
d = sys.argv[1]
M3.set_dyad(F, d); M3.set_dyad(FG, d); FG.translate("")
for u in sys.argv[2:]:
    try:
        print(FG.unit_my(G.prep(u)))
    except Exception as e:
        traceback.print_exc(limit=-5)
