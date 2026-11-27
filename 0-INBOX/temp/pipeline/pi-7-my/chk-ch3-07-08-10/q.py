import sys, re
sys.path.insert(0, sys.argv[1])
sys.dont_write_bytecode = True
import importlib.util, pathlib
HERE = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("F", HERE / "my7_formulas.py")
F = importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
pat = sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 20
n = 0
for b, d in F.FINAL.SEG.items():
    for k, (f, p, m) in d.items():
        for i, (a, c) in enumerate(zip(p, m)):
            if re.search(pat, a):
                print(f"[{b} {f} {k}] {a[:400]}\n    {c[:600]}")
                n += 1
                break
        if n >= mx: break
    if n >= mx: break
