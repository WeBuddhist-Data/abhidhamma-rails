"""For each regex given, print the first matching pi-1 Pāli line and its aligned pi-1 rails Hindi line.

usage: python -I -X utf8 build_rails_3_pi1multi.py <regex> [<regex> ...]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"
pairs = []
for p in sorted(PA.glob("*.md")):
    h = HI / p.name
    if not h.exists():
        continue
    a = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l for l in h.read_text(encoding="utf-8").splitlines() if l.strip()]
    pairs += [(p.name, x, y) for x, y in zip(a, b)]
for arg in sys.argv[1:]:
    pat = re.compile(arg)
    for name, x, y in pairs:
        if pat.search(x):
            print(f"### {arg}\n== {name}\nPA: {x}\nHI: {y}\n")
            break
    else:
        print(f"### {arg}\n(no match)\n")
