"""Find a Pāli regex in the pi-1 Pāli split chapters; print the aligned pi-1 rails Burmese line (line-for-line).
usage: p1find.py REGEX [maxhits] [--cut N]"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
P = ROOT / "AI_translation/pali/pi-1_split_chapters"
B = ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
rx = re.compile(sys.argv[1])
mx = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 5
cut = 600
if "--cut" in sys.argv:
    cut = int(sys.argv[sys.argv.index("--cut") + 1])
n = 0
for p in sorted(P.glob("*.md")):
    pl = p.read_text(encoding="utf-8-sig").split("\n")
    bl = (B / p.name).read_text(encoding="utf-8").split("\n")
    if len(pl) != len(bl):
        print("LINECOUNT DIFF", p.name, len(pl), len(bl))
    for i, l in enumerate(pl):
        m = rx.search(l)
        if m:
            print(f"== {p.name}:{i+1}  match@{m.start()}")
            print("PI:", l[:cut])
            print("MY:", bl[i][:cut] if i < len(bl) else "?")
            n += 1
            if n >= mx:
                sys.exit()
