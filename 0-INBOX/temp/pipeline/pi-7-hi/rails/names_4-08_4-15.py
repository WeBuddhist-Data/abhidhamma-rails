"""Print the termbase name of every dyad / triad that occurs in the headings of 4-08 .. 4-15.
usage: python -I -B -X utf8 names_4-08_4-15.py
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[5]
PALI = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
TB = ROOT / "AI_translation" / "hindi" / "pi-7-pali-hindi-termbase-plain.md"
FILES = ["4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md", "4-10-dukatika-sarammanaduka.md",
         "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md", "4-13-dukatika-dassanenapahatabbaduka.md",
         "4-14-dukatika-saranaduka.md", "4-15-tikaduka-hetuduka.md"]
tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w.lower()] = body[:-1]
names = set()
for f in FILES:
    for ln in (PALI / f).read_text(encoding="utf-8").splitlines():
        m = re.match(r"#+ \*?[\d-]+\. ([^ *]+?)(?:\*)? \^", ln)
        if m and "-" in m.group(1):
            for part in m.group(1).split("-"):
                names.add(part.rstrip("ṃ"))
for n in sorted(names):
    hits = [k for k in (n.lower(), n.lower() + "ṃ") if k in tb]
    out = tb[hits[0]].rsplit(": ", 1)[1] if hits else "-- not in termbase"
    print(n, "=>", out)
