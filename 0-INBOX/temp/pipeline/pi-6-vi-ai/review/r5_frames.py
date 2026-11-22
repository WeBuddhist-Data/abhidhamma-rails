import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *

mode = sys.argv[1] if len(sys.argv) > 1 else "fwd"
files = FILES if len(sys.argv) < 3 else ["10-%s-indriyayamaka.md" % x for x in sys.argv[2].split(",")]

LBLP = re.compile(r"^\((Ka|Kha|Ga|Gha)\)\s*")
LBLV = re.compile(r"^\((a|b|c|d)\)\s*")

def pkey(s):
    s = LBLP.sub("", s)
    s = s.replace("tāsaṃ", "tesaṃ").replace("upapajjantīnaṃ", "upapajjantānaṃ")
    s = s[0].lower() + s[1:] if s else s
    return s

def vkey(s):
    s = LBLV.sub("", s)
    return s

fwd = defaultdict(Counter); loc = defaultdict(list); rev = defaultdict(Counter); revloc = defaultdict(list)
samples = {}
nsent = 0
for fn, ln, sid, P, V in pairs(files):
    if P.startswith("#"):
        continue
    sp = sentences(P); sv = sentences(V)
    if len(sp) != len(sv):
        continue
    for a, b in zip(sp, sv):
        nsent += 1
        pn, toks = norm_p(pkey(a))
        vn = norm_v(vkey(b))
        o = order_of(pn)
        pt = lettered(pn, o); vt = lettered(vn, o)
        fwd[pt][vt] += 1
        loc[(pt, vt)].append("%s:%d/%s" % (fn[3:5], ln, sid))
        rev[vt][pt] += 1
        revloc[(vt, pt)].append("%s:%d/%s" % (fn[3:5], ln, sid))
print("sentences", nsent, "pali templates", len(fwd), "vi templates", len(rev))
if mode == "fwd":
    for pt, c in fwd.items():
        if len(c) > 1:
            print("\n## P:", pt)
            for vt, n in c.most_common():
                L = loc[(pt, vt)]
                print("  [%d] V: %s\n      at %s" % (n, vt, " ".join(L[:6]) + (" ..." if len(L) > 6 else "")))
elif mode == "rev":
    for vt, c in rev.items():
        if len(c) > 1:
            print("\n## V:", vt)
            for pt, n in c.most_common():
                L = revloc[(vt, pt)]
                print("  [%d] P: %s\n      at %s" % (n, pt, " ".join(L[:4])))
elif mode == "all":
    lo = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    hi = int(sys.argv[4]) if len(sys.argv) > 4 else 10**9
    k = 0
    for pt, c in fwd.items():
        for vt, n in c.most_common():
            if lo <= k < hi:
                print("#%d [%d] %s\nP: %s\nV: %s" % (k, n, loc[(pt, vt)][0], pt, vt))
            k += 1
