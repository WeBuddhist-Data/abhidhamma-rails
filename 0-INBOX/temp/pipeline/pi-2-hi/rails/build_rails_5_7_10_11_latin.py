"""Check the four Hindi chapters: Latin-script words outside [..] brackets (ignoring ^IDs), double blank lines, '??'.

usage: python -I -X utf8 build_rails_5_7_10_11_latin.py
"""
import pathlib
import re

OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters")
for name in ["5-indriyavibhango.md", "7-satipatthanavibhango.md", "10-bojjhangavibhango.md", "11-maggangavibhango.md"]:
    t = (OUT / name).read_text(encoding="utf-8")
    bad = []
    for i, line in enumerate(t.splitlines(), 1):
        s = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", line)
        s = re.sub(r"\[[^\]]*\]", "", s)
        if re.search(r"[A-Za-zāīūṃṇñṭḍḷṅ]", s) or "??" in s:
            bad.append(i)
    print(name, "latin/??:", bad[:10], "| double blank:", "\n\n\n" in t, "| CR:", "\r" in t)
