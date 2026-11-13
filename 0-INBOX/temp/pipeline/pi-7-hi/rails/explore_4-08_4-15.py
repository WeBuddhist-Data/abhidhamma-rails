"""Exploration helper for 4-08 .. 4-15: distinct parentheticals, dash clauses, headings, odd lines.
usage: python -I -B -X utf8 explore_4-08_4-15.py notes|dash|heads|words
"""
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[5]
PALI = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
FILES = ["4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md", "4-10-dukatika-sarammanaduka.md",
         "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md", "4-13-dukatika-dassanenapahatabbaduka.md",
         "4-14-dukatika-saranaduka.md", "4-15-tikaduka-hetuduka.md"]
ID = re.compile(r" \^[0-9A-Za-z-]+\s*$")
mode = sys.argv[1]
c = collections.Counter()
for f in FILES:
    for ln in (PALI / f).read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        body = ID.sub("", ln)
        if mode == "heads" and body.startswith("#"):
            c[re.sub(r"^#+ \*?(\d+(-\d+)*\.? )?", "", body).strip("*")] += 1
        elif mode == "notes":
            for m in re.findall(r"\(([^()]*[^\d()][^()]*)\)", body):
                c[m] += 1
        elif mode == "dash":
            for m in re.findall(r"– ([^.()]*)", body):
                c[m] += 1
        elif mode == "words" and not body.startswith("#"):
            for w in re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+", body):
                c[w.lower()] += 1
for k, n in sorted(c.items(), key=lambda x: (-x[1], x[0])):
    print(f"{n:4d} {k}")
