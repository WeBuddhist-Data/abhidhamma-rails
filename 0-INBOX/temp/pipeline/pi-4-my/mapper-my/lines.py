"""read-only helper: print aligned Pāli / Burmese lines of a segment. usage: lines.py CH SID [lineno ...] (lineno = item number in parentheses or 0-based index with i)"""
import sys, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
a = sys.argv[1:]
import map_all as M
def seglines(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip(): continue
        buf.append(re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", l))
        m = M.ID.search(l)
        if m: out[m.group(1)] = buf; buf = []
    return out
P = seglines(M.PI / f"{a[0]}.md"); B = seglines(M.MY / f"{a[0]}.md")
sid = a[1]; want = a[2:]
for i, (p, b) in enumerate(zip(P[sid], B[sid])):
    n = re.match(r"\((\d+)\)", p)
    if want and not ((n and n.group(1) in want) or f"i{i}" in want): continue
    print("P:", p); print("B:", b)
