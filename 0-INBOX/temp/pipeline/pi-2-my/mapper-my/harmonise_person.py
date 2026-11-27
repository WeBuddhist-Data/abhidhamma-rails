"""Person rule scan (map-harmonise decision 3): every value whose LAST chunk is «Xသော» matched only through the
text's person noun «Xသူ» (not literally «Xသော»), and every value that ends in «…သူ» / «…သူ၏».
usage: python3 -I -X utf8 harmonise_person.py"""
import sys, re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from harmonise_show import segments, MY, PI  # noqa: E402
A, B = collections.defaultdict(list), collections.defaultdict(list)
for f in sorted(HERE.glob("*.mapped.md")):
    ch = f.name[:-len(".mapped.md")]
    my = segments(MY / f"{ch}.md")
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1); sid = sid[1:]
        t = re.sub("[“”‘’]", "", my[sid])
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            c = v.split()[-1] if v.split() else ""
            if c.endswith("သော") and c not in t and c[:-3] + "သူ" in t:
                A[(k, v)].append(sid)
            if re.search("သူ(၏)?$", v):
                B[(k, v)].append(sid)
print("## «…သော» values whose text has the person noun «…သူ» (and not «…သော»)")
for (k, v), s in sorted(A.items()):
    print(f"{k}\t{v}\t{len(s)}\t{' '.join(s[:10])}")
print("## values ending in «…သူ» / «…သူ၏»")
for (k, v), s in sorted(B.items()):
    print(f"{k}\t{v}\t{len(s)}\t{' '.join(s[:10])}")
