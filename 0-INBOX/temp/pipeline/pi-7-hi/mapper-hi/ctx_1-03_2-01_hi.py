"""Segments of a file whose Pāli matches a regex and whose keyword list has kw; prints the mapped value(s)
and Pāli snippets around each regex match. usage: ctx_1-03_2-01_hi.py <file> <kw> <regex> [width]"""
import sys, pathlib, re
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_pali, HERE

f, kw, rx = sys.argv[1], sys.argv[2], sys.argv[3]
w = int(sys.argv[4]) if len(sys.argv) > 4 else 60
pa = read_pali(f)
mp = {}
for l in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
    b, _, r = l.partition("] ")
    mp[b[1:]] = [x.split("=", 1) for x in r.split(", ")] if r else []
for bid, kws in read_keywords(f):
    p = pa.get(bid, "")
    if kw in kws and re.search(rx, p):
        vals = sorted({v for k, v in mp[bid] if k == kw})
        snips = [p[max(0, m.start() - w):m.end() + w].replace("\n", " ") for m in re.finditer(rx, p)][:3]
        print(bid, kws.count(kw), vals, "|", " || ".join(snips))
