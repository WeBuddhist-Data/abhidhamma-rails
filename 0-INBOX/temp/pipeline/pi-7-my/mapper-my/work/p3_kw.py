"""phase 3 helper: every use of the given keywords in the current *.mapped.md (value counts, segments), and with
--ctx N the Pāli / Burmese of the first N segments per value (the keyword's neighbourhood only, --win chars).
usage: p3_kw.py KW [KW …] [--ctx N] [--win 120] [--dir DIR] [--ci]"""
import sys
import re
import pathlib
import collections

D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D))
sys.dont_write_bytecode = True
import map7_rules as R  # noqa: E402

args = sys.argv[1:]
ctx = 0
win = 120
d = D
if "--ctx" in args:
    i = args.index("--ctx"); ctx = int(args[i + 1]); del args[i:i + 2]
if "--win" in args:
    i = args.index("--win"); win = int(args[i + 1]); del args[i:i + 2]
if "--dir" in args:
    i = args.index("--dir"); d = pathlib.Path(args[i + 1]); del args[i:i + 2]
ci = "--ci" in args
args = [a for a in args if a != "--ci"]
want = set(R.low(a) for a in args) if ci else set(args)
uses = collections.defaultdict(lambda: collections.defaultdict(list))
for ch in R.chapters():
    f = d / f"{ch}.mapped.md"
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if (R.low(k) if ci else k) in want:
                uses[k][v].append((ch, sid))
for k in sorted(uses):
    print(f"== {k}")
    for v, ss in sorted(uses[k].items(), key=lambda x: -len(x[1])):
        chs = sorted(set(c for c, _ in ss))
        print(f"   {len(ss):5d}  «{v}»  [{' '.join(c.split('-')[0] + '-' + c.split('-')[1] if '-' in c else c for c in chs)}]  "
              f"{' '.join(s for _, s in ss[:8])}")
        for ch, sid in ss[:ctx]:
            p = R.pali(ch).get(sid, "")
            b = R.burmese(ch)[sid]
            m = re.search(re.escape(k), p)
            ps = p[max(0, m.start() - win):m.end() + win] if m else p[:2 * win]
            print(f"        ^{sid} P: {ps}")
            if v != R.NONE:
                first = v.split(" … ")[0].split()[0]
                j = b.find(first)
                bs = b[max(0, j - win):j + 2 * win] if j >= 0 else b[:2 * win]
            else:
                bs = b[:2 * win]
            print(f"               B: {bs}")
