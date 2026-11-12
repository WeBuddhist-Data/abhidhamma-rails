"""Check double blank lines, CR characters, Latin words outside [...] brackets and the word 'seed' in output chapters.

usage: python -I -X utf8 build_rails_12_check.py <file> [<file> ...]
"""
import re
import sys

for p in sys.argv[1:]:
    t = open(p, encoding="utf-8", newline="").read()
    print(p.rsplit("\\", 1)[-1], "CR" if "\r" in t else "noCR", "double-blank" if "\n\n\n" in t else "no-double-blank",
          "seed!" if "seed" in t.lower() else "")
    for n, line in enumerate(t.splitlines(), 1):
        s = re.sub(r"\[[^\]]*\]", "", line)
        s = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", s)
        lat = re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]+", s)
        if lat:
            print("  latin line", n, lat[:5])
