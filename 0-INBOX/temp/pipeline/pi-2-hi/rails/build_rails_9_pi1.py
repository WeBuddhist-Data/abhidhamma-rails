"""Helper (read-only): find a Pāli substring in pi-1 Pāli split chapters and print the aligned pi-1 rails Hindi line.

usage: python -I -X utf8 build_rails_9_pi1.py <substring> [max_hits] [maxchars]
"""
import pathlib
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"

pat = sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 3
mc = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
hits = 0
for p in sorted(PA.glob("*.md")):
    h = HI / p.name
    if not h.exists():
        continue
    pl = [x for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
    hl = [x for x in h.read_text(encoding="utf-8").splitlines() if x.strip()]
    for i, line in enumerate(pl):
        if pat in line:
            print(f"== {p.name} #{i}")
            print("PA:", line[:mc])
            print("HI:", hl[i][:mc] if i < len(hl) else None)
            hits += 1
            if hits >= mx:
                sys.exit()
