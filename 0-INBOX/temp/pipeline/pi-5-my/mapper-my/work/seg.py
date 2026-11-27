"""usage: seg.py ID [ID…] [--kw KW] — Pāli (around KW), Burmese, keyword=value of segments in any chapter"""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
args = sys.argv[1:]; kw = None; width = 400
if "--kw" in args:
    i = args.index("--kw"); kw = args[i + 1]; del args[i:i + 2]
if "--w" in args:
    i = args.index("--w"); width = int(args[i + 1]); del args[i:i + 2]
own = {}
for ch in R.CHAPTERS:
    for sid in R.pali(ch):
        own[sid] = ch
for sid in args:
    ch = own[sid]
    pa, my = R.pali(ch)[sid], R.burmese(ch)[sid]
    mapped = dict(l[1:].split("] ", 1) for l in (R.HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines())
    print("=====", ch, sid)
    if kw:
        i = pa.lower().find(R.low(kw).lower()[:5]); print("PI:", pa[max(0, i - width // 2): i + width // 2])
    else:
        print("PI:", pa[:width])
    print("MY:", my[:width * 3])
    if kw:
        print("MAP:", [kv for kv in mapped.get(sid, "").split(", ") if kw.lower()[:4] in kv.lower()])
