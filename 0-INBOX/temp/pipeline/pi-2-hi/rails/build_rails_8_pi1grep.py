"""Find Pāli substrings in pi-1 and print the aligned pi-1 rails Hindi line (read-only helper).

usage: python -I -X utf8 build_rails_8_pi1grep.py "<pali substring>" [max]
"""
import pathlib
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"

pat = sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 3
n = 0
for p in sorted(PA.glob("*.md")):
    h = HI / p.name
    if not h.exists():
        continue
    a = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l for l in h.read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, l in enumerate(a):
        if pat in l:
            print(f"== {p.name}:{i}")
            print("PA:", l)
            print("HI:", b[i] if i < len(b) else "<none>")
            n += 1
            if n >= mx:
                sys.exit()
