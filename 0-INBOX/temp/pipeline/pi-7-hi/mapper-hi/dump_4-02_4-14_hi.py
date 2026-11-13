"""Helper: print Pāli, Hindi, keywords and current mapping of segments.
usage: python -I -B -X utf8 dump_4-02_4-14_hi.py <file> id1 id2 ...        (ids)
       python -I -B -X utf8 dump_4-02_4-14_hi.py <file> --kw kw1 [kw2 ...] [--max N]  (segments with these keywords)
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali, HERE  # noqa: E402

f = sys.argv[1]
args = sys.argv[2:]
mx = 999
if "--max" in args:
    mx = int(args[args.index("--max") + 1]); args = args[:args.index("--max")]
kws = dict(read_keywords(f))
hi, pa = read_hindi(f), read_pali(f)
mp = {}
mf = HERE / f"{f}.mapped.md"
if mf.exists():
    for l in mf.read_text(encoding="utf-8").splitlines():
        b, _, r = l.partition("] ")
        mp[b[1:]] = r
if args and args[0] == "--kw":
    want = set(args[1:])
    ids = [b for b, k in kws.items() if want & set(k)][:mx]
else:
    ids = args
for b in ids:
    print("##", b)
    print("PI:", pa.get(b))
    print("HI:", hi.get(b))
    print("KW:", ", ".join(kws.get(b, [])))
    if b in mp:
        print("MP:", mp[b])
    print()
