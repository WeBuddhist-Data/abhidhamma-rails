import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F = X.F
d = sys.argv[1]
for t in sys.argv[2:]:
    try:
        print(X.B._engine(t, d))
    except BaseException as e:
        print("FAIL", type(e).__name__, str(e)[:400])
