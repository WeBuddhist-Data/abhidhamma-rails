import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F, D = X.F, X.D
d = sys.argv[1]; u = sys.argv[2]
D.set_dyad(F, d)
pp = D.prep(u, d)
print("PREP:", pp)
sk = F.slot(F.lc(F.pe(pp.strip())))
print("SLOT:", sk[0])
print("in SK:", sk[0] in F.SK)
for k in F.SKF:
    if k in sk[0]: print("SKF hit:", repr(k), "=>", F.SKF[k])
