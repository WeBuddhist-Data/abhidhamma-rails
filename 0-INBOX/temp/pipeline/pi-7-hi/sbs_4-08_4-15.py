"""Side-by-side viewer for 4-08..4-15: python sbs_4-08_4-15.py <file> <regex on Pāli> (read-only helper)."""
import pathlib
import re
import sys

P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
H = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters")
f, rx = sys.argv[1], re.compile(sys.argv[2])
pl = [l for l in (P / f).read_text(encoding="utf-8").splitlines() if l.strip()]
hl = [l for l in (H / f).read_text(encoding="utf-8").splitlines() if l.strip()]
for a, b in zip(pl, hl):
    if rx.search(a):
        print("P:", a[:400])
        print("H:", b[:400])
        print()
