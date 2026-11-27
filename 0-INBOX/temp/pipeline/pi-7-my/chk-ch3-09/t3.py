import sys, importlib.util, pathlib, re, traceback
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
F, M3, K = mk.F, mk.M3, mk.K
M3.set_dyad(F, "cetasika")
for ph in sys.argv[1:]:
    try:
        print(K.link_np(ph.split(), "paṭicca", iter(["Q", "R"])))
    except Exception:
        traceback.print_exc(limit=-4)
