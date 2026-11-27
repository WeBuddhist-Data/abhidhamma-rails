import importlib.util, pathlib, sys, copy
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
import my7_formulas as F
import make_sample  # noqa
snap = {k: copy.deepcopy(getattr(F, k)) for k in ("NOUN", "QUAL", "FIXED", "LEX", "NOTES", "COUNT", "GROUP", "PREFIX", "LINK", "EDNOTES")}
spec = importlib.util.spec_from_file_location("ch101", HERE / "make_ch1-01.py")
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
out = []
for k, old in snap.items():
    new = getattr(F, k)
    for key, val in new.items():
        if key in old and old[key] == val:
            continue
        if k == "LINK":
            val = val("X")
        if isinstance(val, tuple):
            val = val[0]
        if k == "LEX" and key.endswith(" ca"):
            continue
        out.append(f"- {key} = {str(val).rstrip('+')}" + ("  [" + k + "]"))
print("\n".join(sorted(set(out))))
