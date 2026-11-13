import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r2_align import pairs, FILES
c = collections.Counter()
first = {}
for f in FILES:
    P, H = pairs(f)
    for k, (n, p) in enumerate(P):
        if p.startswith("#"):
            continue
        for w in re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+", p):
            wl = w.lower()
            c[wl] += 1
            first.setdefault(wl, f"{f[:4]}#{k+1}")
for w, n in sorted(c.items(), key=lambda x: -x[1]):
    print(n, w, first[w])
