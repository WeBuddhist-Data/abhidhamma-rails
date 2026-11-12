"""Print pi-1 Pāli sentences matching a regex, with the aligned pi-1 rails Hindi sentence.

Lines align one to one (non-empty lines); inside a line, sentences are paired by order
(Pāli split after . ? ; Hindi after । ?). If the sentence counts differ, the whole Hindi line is shown.

usage: python -I -X utf8 build_rails_12_pi1grep.py <regex> [maxhits] [book-glob]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"
pat = re.compile(sys.argv[1])
maxhits = int(sys.argv[2]) if len(sys.argv) > 2 else 3
glob = sys.argv[3] if len(sys.argv) > 3 else "*.md"
SP = re.compile(r"(?<=[.?])\s+(?=\S)")
SH = re.compile(r"(?<=[।?])\s+(?=\S)")
hits = 0
for p in sorted(PA.glob(glob)):
    h = HI / p.name
    if not h.exists():
        continue
    a = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l for l in h.read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(a) != len(b):
        print("!! misaligned", p.name, len(a), len(b))
        continue
    for x, y in zip(a, b):
        if not pat.search(x):
            continue
        xs, ys = SP.split(x), SH.split(y)
        print(f"== {p.name}  ({len(xs)}/{len(ys)} sentences)")
        if len(xs) == len(ys):
            for s, t in zip(xs, ys):
                if pat.search(s):
                    print("PA:", s)
                    print("HI:", t)
        else:
            print("PA:", x)
            print("HI:", y)
        hits += 1
        if hits >= maxhits:
            sys.exit()
