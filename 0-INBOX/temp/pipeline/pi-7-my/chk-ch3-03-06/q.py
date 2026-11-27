import sys, pathlib, importlib.util
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-03-06.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
F = mk.F
import re
pat = sys.argv[1]
for nm, d in (("QUAL", F.QUAL), ("NOUN", F.NOUN), ("FIXED", F.FIXED), ("LEX", F.LEX), ("NOTES", F.NOTES), ("HLINES", F.HLINES), ("NOTE_FIXED", mk.K.NOTE_FIXED), ("SK", F.SK), ("SKF", F.SKF)):
    for k, v in d.items():
        if re.search(pat, k):
            print(nm, repr(k), "=>", v)
