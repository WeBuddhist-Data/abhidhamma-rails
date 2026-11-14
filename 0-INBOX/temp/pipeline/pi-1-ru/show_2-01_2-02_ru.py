"""Print the opening of selected Russian lines (up to «в это время есть») for review.
usage: python -I -X utf8 show_2-01_2-02_ru.py <part.md> <id> [<id> ...]"""
import sys

path, ids = sys.argv[1], sys.argv[2:]
lines = open(path, encoding="utf-8").read().split("\n\n")
for seg in lines:
    for i in ids:
        if seg.rstrip().endswith(" ^" + i):
            for ln in seg.split("\n"):
                k = ln.find(" в это время есть ")
                print(i, "|", ln if k < 0 else ln[:k + 18] + "[…]")
            print()
