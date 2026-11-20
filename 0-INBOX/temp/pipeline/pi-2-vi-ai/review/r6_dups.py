import re
from collections import Counter
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
CH = "17-khuddakavatthuvibhango.md"
P = ROOT + r"\AI_translation\pali\pi-2_split_chapters\\" + CH
V = ROOT + r"\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\\" + CH
def lines(p):
    return [l.rstrip("\n") for l in open(p, encoding="utf-8") if l.strip()]
pl, vl = lines(P), lines(V)
for i, (p, v) in enumerate(zip(pl, vl)):
    if len(v) < 150:
        continue
    for sent in re.split(r"[.;?–]", re.sub(r"\[[^\]]*\]", "", v)):
        items = [x.strip() for x in sent.split(",") if x.strip()]
        c = Counter(items)
        d = {k: n for k, n in c.items() if n > 1 and len(k) > 3}
        if d:
            print(i, d)
