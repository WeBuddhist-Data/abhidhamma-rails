"""Report Latin-script words outside square brackets (block ids excluded) in the given Hindi files.

usage: python -I -X utf8 build_rails_3_latin.py <file> [<file> ...]
"""
import re
import sys

for p in sys.argv[1:]:
    t = open(p, encoding="utf-8").read()
    bad = []
    for n, line in enumerate(t.splitlines(), 1):
        s = re.sub(r"\[[^\]]*\]", "", line)
        s = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", s)
        w = re.findall(r"[A-Za-zĀāĪīŪūṃṅñṭḍṇḷ]+", s)
        if w:
            bad.append((n, w[:5]))
    print(p.split("\\")[-1], "latin outside brackets:", len(bad), bad[:5], "| double blank:", "\n\n\n" in t)
