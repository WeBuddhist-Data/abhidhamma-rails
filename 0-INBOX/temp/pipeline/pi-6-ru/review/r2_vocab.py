import re, sys, collections, os
PD = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
RD = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-6-russian-plain-rails_split_chapters"
FILES = [f"3-0{i}-ayatanayamaka.md" for i in range(1, 7)]
which = sys.argv[1] if len(sys.argv) > 1 else "p"
c = collections.Counter()
for f in FILES:
    d = PD if which == "p" else RD
    t = open(os.path.join(d, f), encoding="utf-8").read()
    t = re.sub(r"\^[\d-]+", " ", t)
    for w in re.findall(r"[^\W\d_]+", t):
        c[w.lower()] += 1
for w, n in sorted(c.items(), key=lambda x: -x[1]):
    print(n, w)
