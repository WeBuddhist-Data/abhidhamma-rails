"""Print termbase entries whose headword matches any given regex (case-insensitive, anchored at start).
usage: python -I -B -X utf8 tb_2-09_2-17.py word1 word2 ..."""
import re
import sys

TB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md"
lines = open(TB, encoding="utf-8").read().splitlines()
for w in sys.argv[1:]:
    rx = re.compile("^(" + w + ")", re.I)
    hits = [l for l in lines if rx.match(l.split(":", 1)[0])]
    print(f"== {w}: {len(hits)}")
    for l in hits[:12]:
        print("  ", l)
