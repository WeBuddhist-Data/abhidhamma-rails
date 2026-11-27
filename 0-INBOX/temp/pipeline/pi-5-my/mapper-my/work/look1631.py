"""per segment of a chapter: the unmapped keywords (map_ch16-31) and, for each, the first Pāli sentence that has it
with the aligned Burmese sentence(s). usage: look1631.py CH [sid ...] [--all] [--w N]"""
import sys, pathlib, re, importlib.util
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "work"))
import map5_rules as R, sent1631 as S
spec = importlib.util.spec_from_file_location("m1631", HERE / "map_ch16-31.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); M = m.mapper()
args = [a for a in sys.argv[1:] if not a.startswith("--")]
W = 260
if "--w" in sys.argv:
    W = int(sys.argv[sys.argv.index("--w") + 1]); args.remove(str(W))
ch, sids = args[0], set(args[1:])
SEEN = {}
my, pa = R.burmese(ch), R.pali(ch)
def stem(w):
    w = R.low(w)
    return w[:max(4, len(w) - 2)] if len(w) > 5 else w
for sid, kws in R.keyword_rows(ch):
    if sids and sid not in sids: continue
    un = []
    for k in kws:
        try:
            v = M.lookup(ch, sid, k, pa.get(sid, ""), my[sid])
            if not R.presence(v, my[sid])[0]: un.append((k, "!" + v))
            elif "--all" in sys.argv: un.append((k, v))
        except KeyError:
            un.append((k, None))
    if "--once" in sys.argv:
        un2 = []
        for k, v in un:
            if k in SEEN: SEEN[k].append(sid)
            else: SEEN[k] = []; un2.append((k, v))
        un = un2
    if not un: continue
    a, b = S.pali_sents(pa.get(sid, "")), S.my_sents(my[sid])
    al = S.align(a, b)
    amap = {}
    for ia, ib in al:
        for i in ia: amap[i] = ib
    groups = {}
    for k, v in un:
        st = [stem(w) for w in k.split()]
        hit = None
        for i, s in enumerate(a):
            sl = s.lower()
            if all(x.lower() in sl for x in st): hit = i; break
        if hit is None:
            for i, s in enumerate(a):
                if st[0].lower() in s.lower(): hit = i; break
        groups.setdefault(hit, []).append(k + (f"={v}" if v else ""))
    print(f"===== {sid}  ({len(a)}/{len(b)})")
    for hit, ks in groups.items():
        if hit is None:
            print("  ?? " + " | ".join(ks)); continue
        ib = amap.get(hit, [])
        if not ib:
            ib = [min(len(b) - 1, round(hit * len(b) / max(1, len(a))))]
        lo, hi = max(0, ib[0]), min(len(b), ib[-1] + 1)
        print("  * " + " | ".join(ks))
        print("    PI: " + a[hit][:W])
        print("    MY: " + " ".join(b[lo:hi])[:int(W * 1.6)])
if "--once" in sys.argv:
    print("REPEATS:", " ; ".join(f"{k}: {len(v)}" for k, v in SEEN.items() if v))
