"""Print termbase entries whose Pāli key matches any of the given regexes (case-insensitive, anchored at start).

usage: python -I -X utf8 rails_sample_tb.py <regex> [<regex> ...]
"""
import pathlib
import re
import sys

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-pali-hindi-termbase-plain.md")
pats = [re.compile(p, re.I) for p in sys.argv[1:]]
for line in TB.read_text(encoding="utf-8").splitlines():
    k = line.split(": {", 1)[0]
    if any(p.fullmatch(k) for p in pats):
        print(line)
