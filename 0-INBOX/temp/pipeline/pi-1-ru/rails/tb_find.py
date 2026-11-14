"""Print termbase lines whose KEY matches any of the given regexes (case-insensitive).
Usage: python -I -X utf8 tb_find.py regex1 regex2 ..."""
import re, sys
from pathlib import Path

TB = Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-1-pali-russian-termbase-plain.md")

if __name__ == "__main__":
    pats = [re.compile(p, re.I) for p in sys.argv[1:]]
    for line in TB.read_text(encoding="utf-8").splitlines():
        if ": {" not in line:
            continue
        k = line.split(": {", 1)[0]
        if any(p.search(k) for p in pats):
            print(line)
