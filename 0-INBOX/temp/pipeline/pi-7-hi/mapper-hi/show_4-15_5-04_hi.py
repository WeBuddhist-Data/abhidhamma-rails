"""Print Pāli, Hindi, keywords (and mapped line if any) for segments of one of my files.
usage: python -I -B -X utf8 show_4-15_5-04_hi.py <file> id [id …]   (id may end with * for a prefix)
"""
import sys, pathlib
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import read_keywords, read_hindi, read_pali

f = sys.argv[1]
pa, hi = read_pali(f), read_hindi(f)
kw = dict(read_keywords(f))
mp = {}
mf = HERE / f"{f}.mapped.md"
if mf.exists():
    for l in mf.read_text(encoding="utf-8").splitlines():
        b, _, r = l.partition("] ")
        mp[b[1:]] = r
ids = []
for a in sys.argv[2:]:
    if a.endswith("*"):
        ids += [b for b in kw if b.startswith(a[:-1])]
    else:
        ids.append(a)
for b in ids:
    print("=====", b)
    print("PA:", pa.get(b))
    print("HI:", hi.get(b))
    print("KW:", ", ".join(kw.get(b, [])))
    if b in mp:
        print("MP:", mp[b])
