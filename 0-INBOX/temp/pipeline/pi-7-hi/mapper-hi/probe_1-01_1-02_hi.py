"""Probe for 1-01 / 1-02: unmapped keywords and fallback sources (prints only).
usage: python -I -B -X utf8 probe_1-01_1-02_hi.py <f> [missing|fallback|show id …|kw word …]
"""
import sys, pathlib, collections; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
from map_1_01_1_02_tables_hi import T, OVR  # noqa

f, mode = sys.argv[1], sys.argv[2]
args = sys.argv[3:]
hi, pa = read_hindi(f), read_pali(f)
table = {**PI7, **T}
ovr = OVR.get(f, {})
if mode == "missing":
    miss = collections.Counter(); ex = {}
    for bid, kws in read_keywords(f):
        for kw in kws:
            if kw in ovr.get(bid, {}):
                continue
            try:
                pi7_value(kw, kws, table, pa.get(bid), hi.get(bid))
            except KeyError:
                miss[kw] += 1; ex.setdefault(kw, bid)
    for kw, n in miss.most_common():
        print(n, kw, ex[kw])
    print("distinct", len(miss))
elif mode == "fallback":
    audit(f, table, ovr, only_fallback=True)
elif mode == "all":
    audit(f, table, ovr)
elif mode in ("show", "short"):
    kd = dict(read_keywords(f))
    cut = (lambda s: s if s is None or len(s) < 700 else s[:700] + " [...]") if mode == "short" else (lambda s: s)
    for bid in args:
        print("==", bid); print("PA:", cut(pa.get(bid))); print("HI:", cut(hi.get(bid))); print("KW:", ", ".join(kd.get(bid, [])))
elif mode == "ctx":                       # ctx <bid> <regex> [paliregex]
    import re
    bid, rx = args[0], args[1]
    for m in list(re.finditer(rx, hi.get(bid, "")))[:6]:
        print("HI…", hi[bid][max(0, m.start() - 80): m.end() + 80].replace("\n", " "))
    if len(args) > 2:
        for m in list(re.finditer(args[2], pa.get(bid, "")))[:6]:
            print("PA…", pa[bid][max(0, m.start() - 80): m.end() + 80].replace("\n", " "))
elif mode == "heads":
    kd = dict(read_keywords(f))
    for bid, kws in read_keywords(f):
        if (pa.get(bid) or "").startswith("#"):
            vals = [pi7_value(k, kws, table, pa.get(bid), hi.get(bid))[0] if True else "" for k in []]
            out = []
            for k in kws:
                try:
                    out.append(f"{k}={pi7_value(k, kws, table, pa.get(bid), hi.get(bid))[0]}")
                except KeyError:
                    out.append(f"{k}=???")
            print(bid, "|", pa[bid].lstrip("# "), "|", (hi.get(bid) or "").lstrip("# "), "|", ", ".join(out))
elif mode == "kw":
    for w in args:
        n = 0
        for bid, kws in read_keywords(f):
            if w in kws:
                n += 1
                if n <= 4:
                    print("==", bid, "|", ", ".join(kws)); print("PA:", pa.get(bid)); print("HI:", hi.get(bid))
        print(w, "occurs in", n, "lines")
