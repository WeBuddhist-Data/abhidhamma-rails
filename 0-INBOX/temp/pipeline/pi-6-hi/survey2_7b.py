import re, collections
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
files = ["7-%02d-anusayayamaka.md" % i for i in range(6, 12)]
an = re.compile(r"(?i)(kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay\w*")
heads = collections.Counter()
words = collections.Counter()
for f in files:
    for ln in open(base + "\\" + f, encoding="utf-8").read().splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        ln = re.sub(r"\s*\^[\d-]+$", "", ln)
        for s in re.split(r"(?<=[.?;,])\s+", ln):
            m = an.search(s)
            h = s[:m.start()] if m else s
            heads[h.strip()] += 1
            for w in an.sub("A", s).split():
                words[w] += 1
for h, c in sorted(heads.items()):
    print(c, "|", h)
print("=====")
for w, c in sorted(words.items()):
    print(c, w)
