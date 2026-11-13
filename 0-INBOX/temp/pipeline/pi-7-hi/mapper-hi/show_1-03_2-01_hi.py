"""Show Pāli, Hindi, keywords (and mapped line if any) for given ids.
usage: python -I -B -X utf8 show_1-03_2-01_hi.py <file> id [id …]   (id may be a prefix ending with *)
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali, HERE

f = sys.argv[1]
hi, pa = read_hindi(f), read_pali(f)
kw = dict(read_keywords(f))
mp = {}
mf = HERE / f"{f}.mapped.md"
if mf.exists():
    for l in mf.read_text(encoding="utf-8").splitlines():
        b, _, r = l.partition("] ")
        mp[b[1:]] = r
ids = []
order = [b for b, _ in read_keywords(f)]
for a in sys.argv[2:]:
    if a.endswith("*"):
        ids += [b for b in order if b.startswith(a[:-1])]
    else:
        ids.append(a)
for b in ids:
    print("=====", b)
    print("PI:", pa.get(b))
    print("HI:", hi.get(b))
    print("KW:", ", ".join(kw.get(b, [])))
    if b in mp:
        print("MP:", mp[b])
