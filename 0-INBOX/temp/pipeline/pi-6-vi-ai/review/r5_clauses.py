import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *

VERB = r"(?:nappajjah|nappajah|pajah|uppajj|upapajj|bhāv|bhav|parijān|sacchikar)\w*"
PCL = re.compile(r"<I(\w)>\w*(?: ca)?[\s…pe]*?\s*(na\s+)?(" + VERB + r")")

def ptense(v):
    if "itth" in v: return "past"
    if "iss" in v or "ess" in v: return "fut"
    return "pres"

def pclauses(s):
    out = []
    last = 0
    for m in PCL.finditer(s):
        pre = s[last:m.start()]
        noca = bool(re.search(r"\bno ca\b", pre))
        neg = bool(m.group(2)) or m.group(3).startswith("napp")
        out.append((m.group(1), (neg != noca), ptense(m.group(3)), "noca" if noca else ""))
        last = m.end()
    return out

VV = r"(sinh khởi|tu tập|hiểu biết trọn vẹn|tự mình chứng nghiệm|dứt bỏ)"
MOD = r"((?:(?:cũng|vẫn|sẽ|đã|từng|không|chưa)\s+)*)"
VPOST = re.compile(r"(không có\s+)?<I(\w)>\s+" + MOD + r"sinh khởi")
VPRE = re.compile(MOD + r"(tu tập|hiểu biết trọn vẹn|tự mình chứng nghiệm|dứt bỏ)\s+<I(\w)>")

def vmods(mod):
    w = mod.split()
    neg = ("không" in w) or ("chưa" in w)
    if "chưa" in w or "đã" in w or "từng" in w: t = "past"
    elif "sẽ" in w: t = "fut"
    else: t = "pres"
    return neg, t, ("vẫn" in w)

def vclauses(s):
    out = []
    for m in VPOST.finditer(s):
        neg, t, van = vmods(m.group(3))
        if m.group(1): neg = not neg
        out.append((m.start(), m.group(2), neg, t, "noca" if (m.group(1) or van) else ""))
    for m in VPRE.finditer(s):
        neg, t, van = vmods(m.group(1))
        out.append((m.start(), m.group(3), neg, t, "noca" if van else ""))
    out.sort()
    return [x[1:] for x in out]

files = FILES if len(sys.argv) < 2 else ["10-%s-indriyayamaka.md" % x for x in sys.argv[1].split(",")]
bad = 0; n = 0
seen = Counter(); stat = Counter()
for fn, ln, sid, P, V in pairs(files):
    if P.startswith("#"): continue
    sp = sentences(P); sv = sentences(V)
    if len(sp) != len(sv):
        sp = [" ".join(sp)]; sv = [" ".join(sv)]
    for a, b in zip(sp, sv):
        pn, _ = norm_p(a); vn = norm_v(b)
        o = order_of(pn); pt = lettered(pn, o); vt = lettered(vn, o)
        pc = pclauses(pt); vc = vclauses(vt)
        n += 1
        nv = len([w for w in re.findall(r"\b" + VERB, pt) if not re.match(r"upapajj|uppajjant|bhāvena|bhav(?!iss)|\w+(itvā|ānaṃ|īnaṃ)$", w)])
        if len(pc) < nv and "…" not in pt:
            print("UNDERCOUNT %s:%d %s | %s" % (fn[3:5], ln, len(pc), pt))
        stat[len(pc)] += 1
        pc2 = [x[:3] for x in pc]; vc2 = [x[:3] for x in vc]
        # noca marker: Pali noca with neg verb should give vẫn in VI
        ok = pc2 == vc2
        if ok:
            for x, y in zip(pc, vc):
                pass
        if not ok:
            key = (pt, vt)
            seen[key] += 1
            if seen[key] == 1:
                bad += 1
                print("== %s:%d %s\n P %s\n V %s\n p=%s\n v=%s" % (fn[3:5], ln, sid, pt, vt, pc2, vc2))
print("sentences", n, "distinct mismatches", bad, "clauses/sentence", sorted(stat.items()))
