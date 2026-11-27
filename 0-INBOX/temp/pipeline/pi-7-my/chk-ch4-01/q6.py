import sys, importlib.util, pathlib, copy
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
# load B alone first to snapshot tables, then load mine in a fresh process? Instead: load mine, and compare to B-only snapshot in a separate run
spec = importlib.util.spec_from_file_location("b", H / "make_ch3-07-08-10.py")
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
F = B.F
import json
snap = {n: {k: repr(v) for k, v in getattr(F, n).items()} for n in ("LEX", "FIXED", "QUAL", "NOUN", "SK", "SKF", "NOTES", "HLINES")}
snapg = {n: {k: repr(v) for k, v in getattr(B.FG, n).items()} for n in ("LEX", "FIXED", "QUAL", "NOUN")}
pathlib.Path(H / "chk-ch4-01/snapB.json").write_text(json.dumps([snap, snapg]))
print("ok")
