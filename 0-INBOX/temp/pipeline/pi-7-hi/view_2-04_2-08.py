"""Print Hindi non-empty lines of one output file: view_2-04_2-08.py <fid> <n1> [n2 ...] (n = non-empty line no.)"""
import sys, pathlib
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters")
f = next(D.glob(sys.argv[1] + "-*.md"))
lines = [l for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
for a in sys.argv[2:]:
    lo, _, hi = a.partition("-")
    for n in range(int(lo), int(hi or lo) + 1):
        print(f"[{n}] {lines[n - 1]}")
