import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *

CONDS = [("hetu", "मूल"), ("ārammaṇa", "विषय"), ("adhipati", "प्रधानता"), ("samanantara", "पूर्ण निकटता"),
         ("anantara", "निकटता"), ("sahajāta", "सह-उत्पत्ति"), ("aññamañña", "परस्पर"), ("upanissaya", "प्रबल आश्रय"),
         ("nissaya", "आश्रय"), ("purejāta", "पूर्व-उत्पत्ति"), ("pacchājāta", "पश्चात्-उत्पत्ति"), ("āsevana", "पुनरावृत्ति"),
         ("vipāka", "कर्म-फल"), ("kamma", "कर्म"), ("āhāra", "आहार"), ("indriya", "क्षमता"), ("jhāna", "ध्यान"),
         ("magga", "मार्ग"), ("vippayutta", "अलगाव"), ("sampayutta", "जुड़ाव"), ("natthi", "अनुपस्थिति"), ("atthi", "उपस्थिति"),
         ("avigata", "अविलीनता"), ("vigata", "विलीनता")]
P2H = dict(CONDS)
LOC = {"hetu": "hetuyā", "ārammaṇa": "ārammaṇe", "adhipati": "adhipatiyā", "samanantara": "samanantare", "anantara": "anantare",
       "sahajāta": "sahajāte", "aññamañña": "aññamaññe", "upanissaya": "upanissaye", "nissaya": "nissaye", "purejāta": "purejāte",
       "pacchājāta": "pacchājāte", "āsevana": "āsevane", "vipāka": "vipāke", "kamma": "kamme", "āhāra": "āhāre", "indriya": "indriye",
       "jhāna": "jhāne", "magga": "magge", "vippayutta": "vippayutte", "sampayutta": "sampayutte", "natthi": "natthiyā", "atthi": "atthiyā",
       "avigata": "avigate", "vigata": "vigate"}
stems = sorted(P2H, key=len, reverse=True)
alts = []
for s in stems:
    alts.append(re.escape(s) + r"(?:paccay(?:ā|o|ena|e|aṃ|ādi|ādī|assa|āti|ā\b))")
    alts.append(re.escape(LOC[s]) + r"(?![a-zāīūṃṅñṭḍṇḷ])")
PRE = re.compile(r"(?<![a-zāīūṃṅñṭḍṇḷ])(na|no)?(" + "|".join(alts) + r")", re.I)
loc2s = {v: k for k, v in LOC.items()}


def pali_conds(t):
    t = re.sub(r"\{[^}]*\}", "", t)
    out = []
    for m in PRE.finditer(t):
        neg, w = m.group(1), m.group(2).lower()
        # find stem
        st = None
        for s in stems:
            if w.startswith(s + "paccay"):
                st = s; break
        if st is None:
            st = loc2s.get(w)
        if st is None:
            continue
        # "nonatthi"/"novigata" etc: na/no prefix; but natthi itself starts with 'n'
        out.append((st, bool(neg)))
    return out

HN = sorted(P2H.values(), key=len, reverse=True)
HRE = re.compile(r"(" + "|".join(re.escape(x) for x in HN) + r")-कारण(ों)?( के अभाव| के बिना| का अभाव| के अभावों| न होने)?")
H2P = {v: k for k, v in P2H.items()}


def hindi_conds(t):
    t = re.sub(r"\[(पाठभेद|वर्तनी-भेद)[^\]]*\]", "", t)
    return [(H2P[m.group(1)], bool(m.group(3))) for m in HRE.finditer(t)]

if __name__ == "__main__":
    n = 0
    for fi, f in enumerate(FILES):
        for r in pairs(f):
            pc = pali_conds(IDRE.sub("", r["p"])); hc = hindi_conds(r["h"])
            if pc != hc:
                n += 1
                print(f"{fi}|{r['id']}|k{r['k']}")
                print("   P:", pc)
                print("   H:", hc)
                if len(sys.argv) > 1:
                    print("   PT:", r["p"][:300]); print("   HT:", r["h"][:300])
    print("mismatch lines", n)
