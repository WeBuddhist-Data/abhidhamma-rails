import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *

c = Counter()
for fn, ln, sid, P, V in pairs():
    if P.startswith("#"): continue
    for s in sentences(V):
        if s.endswith("?"):
            if not ("có phải" in s and s.endswith("không?")):
                print("Q-FORM", fn[3:5], ln, sid, s[:160])
            c["q"] += 1
    if re.search(r"\s{2,}", V): print("DBLSPACE", fn[3:5], ln, sid)
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]{3,}", re.sub(r"\[[^\]]*\]", "", V)):
        lat = [w for w in re.findall(r"\b[\w-]+\b", re.sub(r"\[[^\]]*\]", "", V)) if re.search(r"[āīūṃṅñṭḍṇḷ]", w)]
        if lat: print("PALI-LEFT", fn[3:5], ln, sid, lat[:5])
    if "—" in V: print("EMDASH", fn[3:5], ln)
    if re.search(r"\.\.|,,|\?\.|\.\?", V.replace("…", "")): print("PUNCT", fn[3:5], ln, sid)
    if re.search(r",\s*thì\s+thì|\bthì thì\b|\bở ở\b|\bnhững những\b|\bcũng cũng\b", V): print("DUPWORD", fn[3:5], ln, sid)
print(c)
