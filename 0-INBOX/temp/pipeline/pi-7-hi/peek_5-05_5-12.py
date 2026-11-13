import sys, pathlib
P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
# usage: peek_5-05_5-12.py <file-prefix> <nonempty line> [<nonempty line> ...]
pre = sys.argv[1]
f = next(p for p in P.iterdir() if p.name.startswith(pre))
lines = [l for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
for a in sys.argv[2:]:
    n = int(a)
    print(f"--- {f.name} {n}: {lines[n - 1]}")
