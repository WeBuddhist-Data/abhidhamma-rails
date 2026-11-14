"""Per-line dash check: Pāli file vs English file (non-empty lines). Counts EM DASH (U+2014) and EN DASH (U+2013).

usage: python -I -X utf8 dashcheck.py <pali_file> <english_file>
"""
import sys

DASHES = ("—", "–")


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


def count(t):
    return sum(t.count(d) for d in DASHES)


a, b = lines(sys.argv[1]), lines(sys.argv[2])
bad = [i for i, (x, y) in enumerate(zip(a, b)) if count(x) != count(y)]
em = sum(l.count("—") for l in b) - sum(l.count("—") for l in a)
print("lines", len(a), len(b), "dash-line mismatches", len(bad), bad[:5],
      "| dashes pali", sum(map(count, a)), "english", sum(map(count, b)), "| extra em-dashes", em)
