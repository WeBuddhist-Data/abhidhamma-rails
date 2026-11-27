import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F = X.F
import re
pat = re.compile(sys.argv[1])
for name in ("LEX","FIXED","QUAL","NOUN","SK","SKF","NOTES","HLINES"):
    dct = getattr(F, name)
    for k, v in dct.items():
        if pat.search(k): print(name, repr(k), "=>", v)
for k, v in X.K.NOTE_FIXED.items():
    if pat.search(k): print("NOTE_FIXED", repr(k), "=>", v)
for k, v in X.D.NOTEP.items():
    if pat.search(k): print("NOTEP", repr(k), "=>", v)
for k, v in getattr(X.M, "NOTE_ADD", {}).items():
    if pat.search(k): print("M.NOTE_ADD", repr(k), "=>", v)
