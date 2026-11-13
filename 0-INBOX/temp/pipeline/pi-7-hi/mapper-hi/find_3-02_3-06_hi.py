"""Print the Hindi context (±W chars) of substrings in segments; queries in q_3-02_3-06_hi.txt, one per line:
<file-prefix>|<bid>|<hindi substring>      (file-prefix e.g. 3-02)
usage: python -I -B -X utf8 find_3-02_3-06_hi.py [W]
"""
import sys, pathlib; sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import read_hindi  # noqa
FILES = ["3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka", "3-05-ganthagocchaka",
         "3-06-oghayogagocchaka"]
W = int(sys.argv[1]) if len(sys.argv) > 1 else 80
cache = {}
for line in (HERE / "q_3-02_3-06_hi.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    fp, bid, s = line.split("|", 2)
    f = next(x for x in FILES if x.startswith(fp))
    if f not in cache:
        cache[f] = read_hindi(f)
    h = cache[f].get(bid, "")
    print("==", fp, bid, s)
    i = h.find(s)
    while i >= 0:
        print("   …" + h[max(0, i - W): i + len(s) + W].replace("\n", " / ") + "…")
        i = h.find(s, i + 1)
