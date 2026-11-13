"""Side-by-side review helper: python -I -X utf8 review_4-16_5-04.py <file> <regex> [maxchars] [skip] [count]"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
f, rx = sys.argv[1], re.compile(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 220
skip = int(sys.argv[4]) if len(sys.argv) > 4 else 0
cnt = int(sys.argv[5]) if len(sys.argv) > 5 else 60
p = (ROOT / "pali" / "pi-7_split_chapters" / f).read_text(encoding="utf-8").splitlines()
h = (ROOT / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters" / f).read_text(encoding="utf-8").splitlines()
hits = [i for i, l in enumerate(p) if l.strip() and rx.search(l)]
for i in hits[skip:skip + cnt]:
    print(f"P{i + 1}| {p[i][:mx]}")
    print(f"H{i + 1}| {h[i][:mx]}")
