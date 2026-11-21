"""r4: print Pali / Vietnamese interleaved for a chapter (console only).
Usage: python -I -X utf8 -B r4_side.py <ch.md> [start_line] [end_line]
   or: python -I -X utf8 -B r4_side.py --ts <firstID> <lastID>   (prints reference lines between those IDs, console only)
"""
import re
import sys

BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PDIR = BASE + r"\pali\pi-5_split_chapters"
VDIR = BASE + r"\vietnamese\pi-5-vietnamese-plain-rails_split_chapters"
TS = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-5-tinh_su.md"


def nonempty(path):
    with open(path, encoding="utf-8") as f:
        return [l for l in f.read().split("\n") if l.strip()]


if sys.argv[1] == "--ts":
    a, b = sys.argv[2], sys.argv[3]
    with open(TS, encoding="utf-8") as f:
        tl = f.read().split("\n")
    on = False
    for l in tl:
        if not on and re.search(r"pi-5\.md#\^" + re.escape(a) + r"\]\]", l):
            on = True
        if on and l.strip() and not l.startswith("![["):
            print(l)
        if on and re.search(r"\^" + re.escape(b) + r"\s*$", l):
            break
    sys.exit()

ch = sys.argv[1]
pl, vl = nonempty(PDIR + "\\" + ch), nonempty(VDIR + "\\" + ch)
s = int(sys.argv[2]) if len(sys.argv) > 2 else 1
e = int(sys.argv[3]) if len(sys.argv) > 3 else len(pl)
for i in range(s - 1, min(e, len(pl))):
    print("P%d: %s" % (i + 1, pl[i]))
    print("V%d: %s" % (i + 1, vl[i]))
