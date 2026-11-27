import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F,K,D,M,B,S=X.F,X.K,X.D,X.M,X.B,X.S
for n in sys.argv[1:]:
    try: print(n, "=", repr(eval(n)))
    except Exception as e: print(n, "ERR", e)
