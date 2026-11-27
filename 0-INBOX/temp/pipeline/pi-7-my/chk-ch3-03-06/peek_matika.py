import sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import importlib.util
spec = importlib.util.spec_from_file_location("f", HERE / "my7_formulas.py")
F = importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
seg = F.FINAL.SEG["1"]
for k, (f, p, m) in seg.items():
    if re.match(r"\^1-M2-(1[4-9]|[2-4]\d)$", k) or re.match(r"\^1-M-2-[3-9]-0$", k):
        print(k, "|", " / ".join(p), "\n   ", " / ".join(m))
