import re, sys, collections
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
files = ["7-%02d-anusayayamaka.md" % i for i in range(6, 12)]
NAMES = ["kāmarāg", "paṭigh", "mān", "diṭṭh", "vicikicch", "bhavarāg", "avijj"]
pat = re.compile(r"(kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay(\w*)")
cnt = collections.Counter()
ex = {}
for f in files:
    for ln in open(base + "\\" + f, encoding="utf-8").read().splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        ln = re.sub(r"\s*\^[\d-]+$", "", ln)
        # split into clauses
        for s in re.split(r"(?<=[.?;])\s+", ln):
            t = pat.sub(lambda m: "A" + ("_" + m.group(2) if m.group(2) else ""), s)
            t = re.sub(r"(A\S* ca )+", "A* ca ", t)
            t = re.sub(r"(A_ñca )+", "A_ñca* ", t)
            cnt[t] += 1
            ex.setdefault(t, f)
for t, c in sorted(cnt.items(), key=lambda x: -x[1]):
    print(c, "|", t)
print(len(cnt), file=sys.stderr)
