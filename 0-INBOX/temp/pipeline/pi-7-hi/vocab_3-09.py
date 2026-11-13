"""Helper for build_3-09_hi.py: list the word forms of 3-09-mahantaraduka.md with counts."""
import collections
import pathlib
import re
import sys

P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters\3-09-mahantaraduka.md")
text = P.read_text(encoding="utf-8")
c = collections.Counter()
for line in text.splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    line = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", line)
    for w in re.findall(r"[^\s,;.…()\-–—{}\[\]?:0-9]+", line):
        c[w.lower()] += 1
mode = sys.argv[1] if len(sys.argv) > 1 else "all"
for w, n in sorted(c.items(), key=lambda x: (-x[1], x[0])):
    print(n, w)
print("TOTAL unique", len(c))
