import sys, importlib.util, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
F = mk.F
pat = sys.argv[1]
for name in ("NOUN", "FIXED", "QUAL", "SK", "SKF", "NOTES", "HLINES"):
    for k, v in getattr(F, name).items():
        if re.search(pat, k):
            print(name, repr(k), v)
