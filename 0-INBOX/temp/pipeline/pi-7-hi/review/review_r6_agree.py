import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *
c = collections.Counter(); ex = {}
for fi, f in enumerate(FILES):
    for r in pairs(f):
        p = r["p"]; h = r["h"]
        m = re.match(r"^(?P<x>.+?) dhamm(?P<n>o|ā) (?P<y>.+?) dhammassa (?P<c>\w+?)paccayena paccayo", p)
        if not m:
            continue
        mh = re.match(r"^(?P<x>.+?परिघटना(?:एँ)?), (?P<y>.+?) के लिए (?P<c>.+?) के रूप में कारण (?P<v>होती हैं|होती है)", h)
        key = (m.group("n"), mh.group("x").endswith("एँ"), mh.group("v"))
        c[key] += 1
        ex.setdefault(key, []).append(f"{fi}|{r['id']}|k{r['k']}")
for k, v in c.items():
    print(k, v, ex[k][:40])

