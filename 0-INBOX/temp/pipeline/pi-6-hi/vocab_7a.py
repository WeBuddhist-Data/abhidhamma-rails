import re, sys, collections
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
files = sys.argv[1:] or ["7-01-anusayayamaka.md", "7-02-anusayayamaka.md", "7-03-anusayayamaka.md", "7-04-anusayayamaka.md", "7-05-anusayayamaka.md"]
c = collections.Counter()
for f in files:
    t = open(base + "\\" + f, encoding="utf-8").read()
    t = re.sub(r"\^[\d-]+", " ", t)
    for w in re.findall(r"[^\s.,?!()\[\]…:;–—#]+", t):
        c[w.lower()] += 1
for w, n in sorted(c.items()):
    print(n, w)
