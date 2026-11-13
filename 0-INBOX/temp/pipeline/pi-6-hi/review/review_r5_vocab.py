import re, os, collections
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
c = collections.Counter()
for n in range(7, 12):
    t = open(os.path.join(base, "7-%02d-anusayayamaka.md" % n), encoding="utf-8").read()
    t = re.sub(r"\^[\w-]+", "", t)
    for w in re.findall(r"[^\W\d_]+", t):
        c[w] += 1
skip = ("anusay",)
for w, k in sorted(c.items(), key=lambda x: -x[1]):
    if "anusay" in w:
        continue
    print(k, w)
