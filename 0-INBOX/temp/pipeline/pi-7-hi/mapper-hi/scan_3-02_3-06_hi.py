"""Scan the Pāli of my files for a keyword's occurrences whose preceding word matches/doesn't match a pattern.
usage: python -I -B -X utf8 scan_3-02_3-06_hi.py <kw> <regex-the-preceding-word-must-NOT-match>
"""
import re, sys, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_pali, read_keywords  # noqa
FILES = ["3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka", "3-05-ganthagocchaka",
         "3-06-oghayogagocchaka"]
kw, notrx = sys.argv[1], sys.argv[2]
for f in FILES:
    pa = read_pali(f)
    for bid, kws in read_keywords(f):
        if kw not in kws:
            continue
        p = pa.get(bid, "")
        for m in re.finditer(r"(\S+)\s+" + re.escape(kw) + r"(?![^\W\d_])", p):
            if not re.search(notrx, m.group(1)):
                print(f[:4], bid, "…" + p[max(0, m.start() - 40): m.end() + 40].replace("\n", " / ") + "…")
