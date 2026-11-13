"""Probe for 3-09-mahantaraduka: unresolved keywords (with counts + first ids) and fallback-sourced values.
usage: python -I -B -X utf8 probe_3-09_hi.py [missing|fallback|seg id ...|kw kw ...]
"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
import map_sample_hi as M

F = "3-09-mahantaraduka"
import importlib.util
_p = M.HERE / "map_3-09_hi.py"
if _p.exists():
    _s = importlib.util.spec_from_file_location("map_3_09_hi", _p)
    _m = importlib.util.module_from_spec(_s)
    _s.loader.exec_module(_m)
    T, OVR = _m.T, _m.OVR
else:
    T, OVR = {}, {}

mode = sys.argv[1] if len(sys.argv) > 1 else "missing"
kwl = read_keywords(F)
hi, pa = read_hindi(F), read_pali(F)
if mode == "missing":
    miss = collections.defaultdict(list)
    for bid, kws in kwl:
        for kw in kws:
            if kw in OVR.get(bid, {}):
                continue
            try:
                pi7_value(kw, kws, {**PI7, **T}, pa.get(bid), hi.get(bid))
            except KeyError:
                miss[kw].append(bid)
    for kw, ids in sorted(miss.items(), key=lambda x: -len(x[1])):
        print(f"{len(ids):4} {kw} :: {' '.join(ids[:4])}")
    print("unique missing", len(miss))
elif mode in ("fallback", "all"):
    log = {}
    res = make_resolver(F, {**PI7, **T}, OVR, log)
    for bid, kws in kwl:
        for kw in kws:
            try:
                res(bid, kw, kws)
            except KeyError:
                pass
    by_kw = collections.defaultdict(list)
    for (kw, v), c in log.items():
        by_kw[kw].append((v, dict(c)))
    for kw in sorted(by_kw, key=lc):
        vals = by_kw[kw]
        if mode == "fallback" and all(set(c) <= {"table", "heading", "override"} for _, c in vals):
            continue
        print(kw, "->", "; ".join(f"{v} {c}" for v, c in vals))
elif mode == "seg":
    for bid in sys.argv[2:]:
        print("==", bid)
        print("PA:", pa.get(bid))
        print("HI:", hi.get(bid))
        print("KW:", dict(kwl).get(bid))
elif mode == "ctx":
    # ctx kw [max]: for each segment listing kw, the Pāli line containing it and the Hindi line at the same index
    kw = sys.argv[2]
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    n = 0
    for bid, kws in kwl:
        if kw not in kws:
            continue
        pl, hl = (pa.get(bid) or "").split("\n"), (hi.get(bid) or "").split("\n")
        for i, l in enumerate(pl):
            if kw in l:
                j = l.find(kw)
                print(f"[{bid}] L{i}/{len(pl)}~{len(hl)} PA: …{l[max(0, j-80):j+80]}…")
                print("      HI:", hl[i][:500] if i < len(hl) else "?")
                break
        else:
            print(f"[{bid}] (kw not literally in Pāli)")
        n += 1
        if n >= mx:
            break
elif mode == "hg":
    # hg <hindi-substring> [bid ...]: Hindi context (±60) of each occurrence, in the given segments or all
    s = sys.argv[2]
    ids = sys.argv[3:] or list(hi)
    for bid in ids:
        t = hi.get(bid) or ""
        j = t.find(s)
        while j >= 0:
            print(f"[{bid}] …{t[max(0, j-60):j+len(s)+60]}…".replace("\n", " / "))
            j = t.find(s, j + 1)
elif mode == "kw":
    want = set(sys.argv[2:])
    for bid, kws in kwl:
        if want & set(kws):
            print(bid, [k for k in kws if k in want])
