"""List distinct parenthesised notes and headings in my files (with counts).
usage: python -I -B -X utf8 notes_scan_4-16_5-04.py"""
import collections
import os
import re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters"
FILES = ["4-16-tikaduka-sappaccayaduka.md", "4-17-tikaduka-asavaduka.md", "4-18-tikaduka-sarammanaduka.md",
         "4-19-tikaduka-kilesaduka.md", "4-20-tikaduka-dassanenapahatabbaduka.md", "4-21-tikaduka-sauttaraduka.md",
         "5-01-anuloma-tikatika.md", "5-02-anuloma-dukaduka.md", "5-03-paccaniya-tika.md", "5-04-paccaniya-duka.md"]
notes = collections.Counter()
heads = collections.Counter()
for f in FILES:
    for ln in open(os.path.join(ROOT, f), encoding="utf-8").read().splitlines():
        ln = re.sub(r" \^[0-9A-Za-z-]+\s*$", "", ln)
        if ln.startswith("#"):
            heads[re.sub(r"^#+ \*?(\d+ ?-?[\d-]*\. )?", "", ln).rstrip("*")] += 1
            continue
        for m in re.findall(r"\(([^()]*)\)", ln):
            if not re.fullmatch(r"\d+", m):
                notes[m] += 1
print("NOTES")
for k, v in sorted(notes.items()):
    print(v, k)
print("HEADS")
for k, v in sorted(heads.items()):
    print(v, k)
