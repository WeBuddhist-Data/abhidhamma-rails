import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("d", H / "make_ch3-01-02.py")
D = importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
print(D._END)
print([k for k in D.F.LEX][:80])
print(len(D.F.LEX), len(D.F.SK), len(D.F.SKF), len(D.F.FIXED))
