"""Look up pi-1 Pāli lines matching a regex and print the aligned pi-1 rails Hindi line (by non-empty line index).

usage: python -I -X utf8 build_rails_3_pi1.py <regex> [max]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"
pat = re.compile(sys.argv[1])
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 3
n = 0
for p in sorted(PA.glob("*.md")):
    h = HI / p.name
    if not h.exists():
        continue
    a = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l for l in h.read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(a) != len(b):
        print("!! misaligned", p.name, len(a), len(b))
    for x, y in zip(a, b):
        if pat.search(x):
            print(f"== {p.name}\nPA: {x}\nHI: {y}\n")
            n += 1
            if n >= mx:
                sys.exit()
