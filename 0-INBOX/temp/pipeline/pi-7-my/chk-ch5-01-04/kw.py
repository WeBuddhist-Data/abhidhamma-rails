import sys, pathlib, re
P = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/pali/pi-7_split_chapters")
B = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters")
pat = re.compile(sys.argv[1], re.I)
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 6
n = 0
for b in sorted(B.glob("*.md")):
    if b.name.startswith("5-"): continue
    pl = (P / b.name).read_text(encoding="utf-8-sig").splitlines()
    bl = b.read_text(encoding="utf-8").splitlines()
    for i, l in enumerate(pl):
        if pat.search(l) and i < len(bl):
            print(f"[{b.name[:4]}:{i+1}] P: {l[:400]}\n          B: {bl[i][:600]}")
            n += 1
            if n >= lim: sys.exit()
