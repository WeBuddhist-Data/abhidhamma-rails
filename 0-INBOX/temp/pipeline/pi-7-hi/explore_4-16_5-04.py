"""Exploration helper for build_4-16_5-04_hi.py: list parenthetical notes in my files."""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
FILES = ["4-16-tikaduka-sappaccayaduka.md", "4-17-tikaduka-asavaduka.md", "4-18-tikaduka-sarammanaduka.md",
         "4-19-tikaduka-kilesaduka.md", "4-20-tikaduka-dassanenapahatabbaduka.md", "4-21-tikaduka-sauttaraduka.md",
         "5-01-anuloma-tikatika.md", "5-02-anuloma-dukaduka.md", "5-03-paccaniya-tika.md", "5-04-paccaniya-duka.md"]
c = collections.Counter()
for f in FILES:
    t = (PALI / f).read_text(encoding="utf-8")
    for m in re.finditer(r"\(([^()]*)\)", t):
        if not re.fullmatch(r"\d+", m.group(1)):
            c[m.group(1)] += 1
for k, v in sorted(c.items()):
    print(v, "|", k)
