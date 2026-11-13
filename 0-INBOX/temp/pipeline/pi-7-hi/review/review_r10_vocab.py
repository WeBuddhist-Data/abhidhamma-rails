import os, sys, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs
hc = collections.Counter(); pc = collections.Counter(); nn = collections.Counter()
for f, pl, hl in pairs():
    for a, b in zip(pl, hl):
        for m in re.finditer(r'((?:[^\s,।…()“”\*]+ )?[^\s,।…()“”\*]+?)-कारण', b):
            hc[m.group(1)] += 1
        for m in re.finditer(r"\b(na|no)([a-zāīūṃṅñṭḍṇḷ]+)", a.lower()):
            pc[m.group(0)] += 1
        for m in re.finditer(r"\bnana\w*|\bnona\w*|\bnono\w*", a.lower()):
            nn[m.group(0)] += 1
print(hc.most_common())
print(len(pc)); print(pc.most_common(400))
print(nn.most_common(100))
