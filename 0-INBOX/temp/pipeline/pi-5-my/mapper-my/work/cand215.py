"""candidates for the unmapped keywords of a chapter (ch2-15 group helper): prior / ch1 / module values of keywords
with the same stem, compound splits, and the aligned Burmese sentence."""
import sys, collections, pathlib, importlib.util, re
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "work"))
import map5_rules as R
import map_ch1 as C1
spec = importlib.util.spec_from_file_location("m215", HERE / "map_ch2-15.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); M = m.mapper()
# value pool: {low(kw): Counter(value)}
POOL = collections.defaultdict(collections.Counter)
for t in R.PRIOR_ORDER:
    for k, c in R.prior()[t].items():
        POOL[k].update(c)
for tab in (C1.T_CH1, R.FRAME, R.STOCK):
    for k, v in tab.items():
        if not v.startswith("@") and v != R.NONE:
            POOL[R.low(k)][v] += 50
for k, v in R.terms().items():
    POOL[k][v] += 20
try:
    for tab in m.TABLES.values():
        for k, v in tab.items():
            if not v.startswith("@") and v != R.NONE:
                POOL[R.low(k)][v] += 100
except Exception:
    pass
KEYS = sorted(POOL)
def stem_cands(kw):
    k = R.low(kw)
    out = collections.Counter()
    for n in range(len(k), max(3, len(k) - 4) - 1, -1):
        pre = k[:n]
        for kk in KEYS:
            if kk.startswith(pre) and abs(len(kk) - len(k)) <= 5 and " " not in kk:
                for v, c in POOL[kk].items():
                    out[v] += c * n
        if out:
            break
    return out
def ok(v, my):
    return R.presence(v, my)[0]
import align as A
def sent_align(kw, pa, my):
    p, m = A.split(pa, my)
    key = R.low(kw.split()[0]).lower()
    key = key[:max(4, len(key) - 2)]
    for i, s in enumerate(p):
        if key in s.lower():
            if len(p) == len(m):
                return s[:200], m[i][:240]
            f = sum(len(x) for x in p[:i]) / max(1, sum(len(x) for x in p))
            j = int(f * sum(len(x) for x in m)); mm = " | ".join(m)
            return s[:200], "~" + mm[max(0, j - 100): j + 200]
    return pa[:150], my[:200]
def main():
    chs = sys.argv[1].split(",")
    for ch in chs:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        my, pa = R.burmese(ch), R.pali(ch)
        seen = collections.OrderedDict()
        for sid, k in unmapped:
            seen.setdefault(k, []).append(sid)
        print("##", ch, len(seen), "keywords")
        for k, sids in seen.items():
            cands = []
            for v, c in stem_cands(k).most_common(40):
                if all(ok(v, my[s]) for s in sids):
                    cands.append(v)
            # compound split
            kl = R.low(k)
            if " " not in k and not cands:
                for i in range(3, len(kl) - 2):
                    a, b = kl[:i], kl[i:]
                    ca = [v for v, _ in stem_cands(a).most_common(8)]
                    cb = [v for v, _ in stem_cands(b).most_common(8)]
                    for x in ca:
                        for y in cb:
                            for j in ("", " "):
                                v = x + j + y
                                if v in my[sids[0]] and v not in cands:
                                    cands.append(v)
            ps, ms = sent_align(k, pa.get(sids[0], ""), my[sids[0]])
            if " " in k and "multi" not in sys.argv: continue
            print(f"{k!r}: {len(sids)} {sids[0]} | C: {' | '.join(cands[:5])}")
            if not cands or "all" in sys.argv:
                print("      PI:", ps); print("      MY:", ms)

if __name__ == '__main__':
    main()
