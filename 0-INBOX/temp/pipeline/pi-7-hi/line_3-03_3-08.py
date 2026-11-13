"""line_3-03_3-08.py <file> <n> [<n> ...] -> print non-empty Pāli line n (and English)."""
import sys, pathlib, re
R = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
nl = lambda p: [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
f = sys.argv[1]
P = nl(R / "pali" / "pi-7_split_chapters" / f)
E = nl(R / "english" / "pi-7-english-plain-zeroshot_split_chapters" / f)
H = R / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters" / f
Hl = nl(H) if H.exists() and "--hi" in sys.argv else None
for a in sys.argv[2:]:
    if a.startswith("--"):
        continue
    n = int(a)
    print(f"[{n}] P:", P[n - 1])
    if "--en" in sys.argv:
        print(f"[{n}] E:", E[n - 1])
    if Hl:
        print(f"[{n}] H:", Hl[n - 1])
