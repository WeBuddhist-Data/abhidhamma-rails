import sys, importlib.util, pathlib, time
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
t=time.time()
spec = importlib.util.spec_from_file_location("b", H / "make_ch3-07-08-10.py")
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
print("load", time.time()-t)
F=B.F
for w in sys.argv[1:]:
    print(w, "LEX", F.LEX.get(w), "NOUN", F.NOUN.get(w), "FIXED", F.FIXED.get(w), "QUAL", F.QUAL.get(w))
