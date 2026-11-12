"""Extra checks for ch8/ch18 Hindi: double blank lines, CR, Latin words outside [...] brackets, ':-'.

usage: python -I -X utf8 build_rails_8_check.py <hindi file> ...
"""
import re
import sys

for p in sys.argv[1:]:
    t = open(p, encoding="utf-8", newline="").read()
    print(p)
    print("  CR:", "\r" in t, " double blank:", "\n\n\n" in t, " ':-':", ":-" in t)
    bad = []
    for i, line in enumerate(t.split("\n"), 1):
        s = re.sub(r"\[[^\]]*\]", "", line)
        s = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", s)
        w = re.findall(r"[A-Za-zĀ-ž]{2,}", s)
        if w:
            bad.append((i, w[:5]))
    print("  latin outside brackets:", bad[:10])
