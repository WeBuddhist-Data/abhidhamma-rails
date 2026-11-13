"""Print aligned Pāli / Hindi sample lines (non-empty) whose Pāli matches a regex.
usage: python -I -B -X utf8 lookup_2-09_2-17.py <regex> [max] [maxchars]"""
import re
import sys

D = r"D:\Work\OpenPecha\abhidhamma-rails"
PAIRS = [
    (D + r"\0-INBOX\temp\pipeline\pi-7-hi\rails\sample-1\1-01-a-pali-sample.md",
     D + r"\0-INBOX\temp\pipeline\pi-7-hi\rails\sample-1\1-01-a-sample.md"),
    (D + r"\0-INBOX\temp\pipeline\pi-7-hi\rails\sample-1\1-01-b-pali-sample.md",
     D + r"\0-INBOX\temp\pipeline\pi-7-hi\rails\sample-1\1-01-b-sample.md"),
    (D + r"\AI_translation\pali\pi-7_split_chapters\1-00-paccaya.md",
     D + r"\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\1-00-paccaya.md"),
]


def lines(p):
    return [l for l in open(p, encoding="utf-8").read().splitlines() if l.strip()]


rx = re.compile(sys.argv[1])
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 10
mc = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
n = 0
for a, b in PAIRS:
    pa, hb = lines(a), lines(b)
    for x, y in zip(pa, hb):
        if rx.search(x):
            print("P:", x[:mc])
            print("H:", y[:mc])
            print()
            n += 1
            if n >= mx:
                sys.exit()
