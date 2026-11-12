"""Draft aid for 16-nanavibhango / 18-dhammahadayavibhango / 5-indriyavibhango (writes nothing).

usage: python -I -X utf8 draft_16_18_5_hi.py <chapter> [mode] [ids...]
  mode 'missing'  : unique keywords with no table value, with prior (pi-1/3/4/5) values present in some segment
  mode 'absent'   : (bid, kw, value) where the current resolver value is absent from the segment's Hindi
  mode 'show'     : Pali / Hindi / keywords=values of the given ids
"""
import collections
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali, present, prior, lc, NDE  # noqa: E402
import map_16_18_5_hi as M  # noqa: E402

ch = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "absent"
ids = sys.argv[3:]
kwl = read_keywords(ch)
hi = read_hindi(ch)
res = M.RESOLVERS[ch]

if mode == "missing":
    seen = collections.OrderedDict()
    for bid, kws in kwl:
        for kw in kws:
            try:
                res(bid, kw, kws)
            except KeyError:
                seen.setdefault(lc(kw), []).append(bid)
    for k, bids in seen.items():
        pr = prior(k)
        cands = collections.Counter()
        for n, c in pr.items():
            for v, x in c.items():
                cands[v] += x
        ok = [v for v, _ in cands.most_common(6) if any(present(v, hi.get(b, "")) for b in bids)]
        allv = [v for v, _ in cands.most_common(4)]
        print(f"{k} ({len(bids)}: {' '.join(bids[:3])}) :: OK {ok} ;; prior {allv}")
elif mode == "absent":
    for bid, kws in kwl:
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                continue
            if v != NDE and not present(v, hi.get(bid, "")):
                print(bid, kw, "=", v)
elif mode == "sizes":
    print(" ".join(f"{b}:{len(hi.get(b, ''))}/{len(k)}" for b, k in kwl))
elif mode == "kw":          # keywords=values only, '!' marks a value absent from the segment
    d = dict(kwl)
    for i in ids:
        out = []
        for kw in d.get(i, []):
            try:
                v = res(i, kw, d[i])
                t = hi.get(i, "")
                out.append(f"{kw}={v}" + ("" if present(v, t) else "~" if M.present_ext(v, t) else "!"))
            except KeyError:
                out.append(f"{kw}=???")
        print(f"[{i}] {', '.join(out)}\n")
else:
    pi = read_pali(ch)
    d = dict(kwl)
    for i in ids:
        out = []
        for kw in d.get(i, []):
            try:
                out.append(f"{kw}={res(i, kw, d[i])}")
            except KeyError:
                c = collections.Counter()
                for n, cc in prior(kw).items():
                    c.update(cc)
                ok = [v for v, _ in c.most_common(8) if present(v, hi.get(i, ""))]
                out.append(f"{kw}=???" + (f"[{' | '.join(ok)}]" if ok else ""))
        print(f"=== {i}\nPI: {pi.get(i)}\nHI: {hi.get(i)}\nKW: {', '.join(out)}\n")
