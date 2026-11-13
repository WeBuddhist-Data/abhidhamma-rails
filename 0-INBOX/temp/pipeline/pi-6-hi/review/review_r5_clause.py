import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location("chk", os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_r5_check.py"))
# reuse functions without running the main loop: exec only the definitions
src = open(spec.origin, encoding="utf-8").read().split("report = []")[0]
ns = {}
exec(src, ns)
base = ns["base"]

def psplit(p):
    p = ns["strip_id"](p)
    p = re.sub(r"\[[^\]]*\]", "", p)
    sents = [s for s in re.split(r"(?<=[.?])\s+", p) if s.strip()]
    out = []
    for s in sents:
        for part in s.split(";"):
            pieces = re.split(r",\s*(?=no ca )", part)
            out.append(pieces)
    return out

def hsplit(h):
    h = ns["strip_id"](h)
    h = re.sub(r"\[[^\]]*\]", "", h)
    sents = [s for s in re.split(r"(?<=[।?])\s+", h) if s.strip()]
    out = []
    for s in sents:
        for part in s.split(";"):
            pieces = re.split(r",\s*(?=पर )", part)
            out.append(pieces)
    return out

rep = []
for n in range(7, 11):
    f = "7-%02d-anusayayamaka.md" % n
    P = ns["lines"](os.path.join(base, "pali", "pi-6_split_chapters", f))
    H = ns["lines"](os.path.join(base, "hindi", "pi-6-hindi-plain-rails_split_chapters", f))
    for i, (p, h) in enumerate(zip(P, H), 1):
        if "dhātupucchāvāro" in p:
            break
        if p.startswith("#"):
            continue
        ps, hs = psplit(p), hsplit(h)
        tag = "%s:%d" % (f[:4], i)
        if [len(x) for x in ps] != [len(x) for x in hs]:
            rep.append((tag, "SHAPE", [len(x) for x in ps], [len(x) for x in hs]))
            continue
        for a, b in zip(ps, hs):
            for pa, hb in zip(a, b):
                pn = ns["pali_neg"](pa if not pa.startswith("no ca") else pa)
                # pali_neg handles 'no ca' flip itself
                hn = ns["hindi_neg"](hb)
                if pn != hn:
                    rep.append((tag, "CL-NEG", pn, hn, pa[:70], hb[:70]))
                pi = [ns["PMAP"][m.group(1).lower()] for m in ns["P_ITEM"].finditer(pa)]
                hi = [ns["HMAP"][m.group(1)] for m in ns["H_ITEM"].finditer(hb)]
                if pi != hi:
                    rep.append((tag, "CL-ITEMS", "".join(pi), "".join(hi), pa[:70]))
                pp = [ns["pplace"](m.group(1)) for m in ns["P_PLACE"].finditer(pa)]
                hp = [ns["hplace"](m.group(1)) for m in ns["H_PLACE"].finditer(hb)]
                if pp != hp:
                    rep.append((tag, "CL-PLACES", pp, hp, pa[:70]))
                pr = ns["seq"](ns["P_PERS_RE"], ns["P_PERS"], pa)
                hr = ns["seq"](ns["H_PERS_RE"], ns["H_PERS"], hb)
                if pr != hr:
                    rep.append((tag, "CL-PERS", pr, hr, pa[:70]))
                pv, hv = ns["pali_verbs"](pa), ns["hindi_verbs"](hb)
                if pv != hv:
                    rep.append((tag, "CL-VERBS", pv, hv, pa[:70]))
                # 'tassa/tesam' (sg/pl) in no ca clause vs Hindi उसमें/उनमें
                if pa.startswith("no ca"):
                    if " tesaṃ " in pa and "उनमें" not in hb:
                        rep.append((tag, "CL-NUM", "tesaṃ", hb[:60]))
                    if " tassa " in pa and "उसमें" not in hb:
                        rep.append((tag, "CL-NUM", "tassa", hb[:60]))
for r in rep:
    print(*r, sep=" | ")
print("flags", len(rep))
