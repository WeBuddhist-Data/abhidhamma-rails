"""Print the XML context of a regex in a VRI/CST XML file (UTF-16 or UTF-8).

usage: python -I -B -X utf8 find_in_xml.py <xml> <regex> [chars=300]
"""
import re, sys, pathlib

raw = pathlib.Path(sys.argv[1]).read_bytes()
for enc in ("utf-16", "utf-8-sig"):
    try:
        text = raw.decode(enc)
        if "Yamak" in text or "yamak" in text:
            break
    except UnicodeDecodeError:
        continue
n = int(sys.argv[3]) if len(sys.argv) > 3 else 300
for m in re.finditer(sys.argv[2], text):
    print("...", text[max(0, m.start() - n): m.end() + n].replace("\n", " "), "...\n")
