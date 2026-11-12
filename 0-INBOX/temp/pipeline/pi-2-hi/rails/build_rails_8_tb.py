"""Print termbase entries whose key matches any of the given regexes (read-only helper).

usage: python -I -X utf8 build_rails_8_tb.py "^mano$" "^upeto" ...
"""
import pathlib
import re
import sys

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-pali-hindi-termbase-plain.md")
pats = [re.compile(a, re.I) for a in sys.argv[1:]]
for line in TB.read_text(encoding="utf-8").splitlines():
    k = line.split(": {", 1)[0]
    if any(p.search(k) for p in pats):
        print(line)
