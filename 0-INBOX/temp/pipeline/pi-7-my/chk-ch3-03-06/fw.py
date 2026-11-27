import sys, pathlib, importlib.util, re
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("f", HERE / "my7_formulas.py")
F = importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
pat, mpat = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "")
n = 0
for b, segs in F.FINAL.SEG.items():
    for k, (f, p, m) in segs.items():
        P, Mm = " ".join(p), " ".join(m)
        if re.search(pat, P) and re.search(mpat, Mm):
            i = re.search(pat, P).start()
            print(b, k, "|", P[max(0,i-60):i+100]); 
            j = re.search(mpat, Mm).start() if mpat else 0
            print("    ", Mm[max(0,j-80):j+120]); n += 1
            if n > 6: sys.exit()
