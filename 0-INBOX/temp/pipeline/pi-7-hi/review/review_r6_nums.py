import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *

PN = {"ekaṃ": 1, "eko": 1, "ekā": 1, "ekassa": 1, "ekena": 1, "ekañca": 1, "ekaṃyeva": 1,
      "dve": 2, "dvinnaṃ": 2, "dvīsu": 2, "dvepi": 2, "dvīhi": 2,
      "tayo": 3, "tīṇi": 3, "tiṇṇaṃ": 3, "tīsu": 3, "tīṇipi": 3, "tīsupi": 3, "tiṇṇampi": 3, "tīsuyeva": 3,
      "cattāro": 4, "cattāri": 4, "catunnaṃ": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "navapi": 9,
      "navasu": 9, "navasupi": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12, "terasa": 13}
HNUM = {"एक": 1, "दो": 2, "दोनों": 2, "तीन": 3, "तीनों": 3, "चार": 4, "चारों": 4, "पाँच": 5, "छह": 6, "सात": 7, "आठ": 8,
        "नौ": 9, "दस": 10, "ग्यारह": 11, "बारह": 12, "तेरह": 13}


def pnums(t):
    t = re.sub(r"\{[^}]*\}", "", IDRE.sub("", t))
    t = re.sub(r"\(\d+\)", "", t)
    ws = re.findall(r"[a-zāīūṃṅñṭḍṇḷ]+", t.lower())
    return [PN[w] for w in ws if w in PN]


def hnums(t):
    t = re.sub(r"\[(पाठभेद|वर्तनी-भेद)[^\]]*\]", "", IDRE.sub("", t))
    t = re.sub(r"\(\d+\)", "", t)
    t = re.sub(r"दो(-दो)? (का|के|की) वर्गीकरण", "", t)
    t = re.sub(r"दो का वर्गीकरण|दो के वर्गीकरण", "", t)
    t = t.replace("एक-एक", "")
    ws = re.findall(r"[\u0900-\u0963\u0966-\u097F]+", t)
    return [HNUM[w] for w in ws if w in HNUM]

n = 0
for fi, f in enumerate(FILES):
    for r in pairs(f):
        a = pnums(r["p"]); b = hnums(r["h"])
        if a != b:
            n += 1
            tag = "ORDER" if sorted(a) == sorted(b) else "DIFF"
            print(f"{fi}|{r['id']}|k{r['k']} {tag} P{a} H{b}")
print("mismatches", n)

