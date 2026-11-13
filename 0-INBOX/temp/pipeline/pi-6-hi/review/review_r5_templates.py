import re, os, collections
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_r5_check.py")
ns = {}
exec(open(src_path, encoding="utf-8").read().split("report = []")[0], ns)
cl = {'__file__': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'review_r5_clause.py')}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_r5_clause.py"), encoding="utf-8").read().split("rep = []")[0], cl)
base = ns["base"]

def pnorm(s):
    s = ns["P_ITEM"].sub("X", s)
    s = re.sub(r"X\w*", "X", s)
    s = re.sub(r"(X ca )+X ca", "XL", s)  # list ca
    s = re.sub(r"(Xñca )+", "XL ", s)
    s = ns["P_PLACE"].sub("L", s)
    s = re.sub(r"(L )+L", "L", s)
    s = ns["P_PERS_RE"].sub("Q", s)
    s = re.sub(r"\(\w+\)", "", s)
    return re.sub(r"\s+", " ", s).strip()

def hnorm(s):
    s = re.sub(r"(इंद्रिय-सुखों के राग|चिढ़|अहंकार|दृष्टि|संशय|अस्तित्व के राग|अज्ञान) की सुप्त प्रवृत्ति", "X", s)
    s = re.sub(r"X(, X)*( और X)", "XL", s)
    s = re.sub(r"X(, X)+", "XL", s)
    s = ns["H_PLACE"].sub("L", s)
    s = re.sub(r"L में(, L में)*( और L में)?", "LL में", s)
    s = re.sub(r"L में(, L में)*", "LL में", s)
    s = ns["H_PERS_RE"].sub("Q", s)
    s = re.sub(r"\([^)]*\)", "", s)
    return re.sub(r"\s+", " ", s).strip()

m = collections.defaultdict(collections.Counter)
ex = {}
for n in range(7, 11):
    f = "7-%02d-anusayayamaka.md" % n
    P = ns["lines"](os.path.join(base, "pali", "pi-6_split_chapters", f))
    H = ns["lines"](os.path.join(base, "hindi", "pi-6-hindi-plain-rails_split_chapters", f))
    for i, (p, h) in enumerate(zip(P, H), 1):
        if "dhātupucchāvāro" in p: break
        if p.startswith("#"): continue
        ps, hs = cl["psplit"](p), cl["hsplit"](h)
        if [len(x) for x in ps] != [len(x) for x in hs]: continue
        for a, b in zip(ps, hs):
            for pa, hb in zip(a, b):
                k = pnorm(pa); v = hnorm(hb)
                m[k][v] += 1
                ex.setdefault((k, v), "%s:%d" % (f[:4], i))
for k, c in sorted(m.items(), key=lambda x: -sum(x[1].values())):
    if len(c) > 1:
        print("P:", k)
        for v, cnt in c.most_common():
            print("   %4d %s  [%s]" % (cnt, v, ex[(k, v)]))
