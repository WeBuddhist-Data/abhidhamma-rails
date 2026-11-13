import re, sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *

PL = "a-zāīūṃñṅṭḍṇḷ"
STEMS = ["hetu", "ārammaṇa", "adhipati", "anantara", "samanantara", "sahajāta", "aññamañña",
         "nissaya", "upanissaya", "purejāta", "pacchājāta", "āsevana", "kamma", "vipāka", "āhāra",
         "indriya", "jhāna", "magga", "sampayutta", "vippayutta", "atthi", "natthi", "vigata", "avigata"]
HN = ["मूल", "विषय", "प्रधानता", "निकटता", "पूर्ण निकटता", "सह-उत्पत्ति", "परस्पर", "आश्रय", "प्रबल आश्रय",
      "पूर्व-उत्पत्ति", "पश्चात्-उत्पत्ति", "पुनरावृत्ति", "कर्म", "कर्म-फल", "आहार", "क्षमता", "ध्यान", "मार्ग",
      "जुड़ाव", "अलगाव", "उपस्थिति", "अनुपस्थिति", "विलीनता", "अविलीनता"]
H2P = dict(zip(HN, STEMS))
_alts = []
for s in STEMS:
    if s.endswith("a"):
        _alts.append("(?P<%s>%s)(?:apaccay[%s]*|e(?![%s]))" % ("s_" + str(STEMS.index(s)), s[:-1], PL, PL))
    else:
        _alts.append("(?P<%s>%s)(?:paccay[%s]*|yā(?![%s]))" % ("s_" + str(STEMS.index(s)), s, PL, PL))
_alts.sort(key=len, reverse=True)
PRE0 = re.compile(r"(?<![" + PL + r"])(?P<neg>na ?|no ?)?(?:" + "|".join(sorted(_alts, key=lambda a: -len(a.split('>')[1]))) + ")")

class _M:
    pass

class PREc:
    @staticmethod
    def finditer(t):
        for m in PRE0.finditer(t):
            st = [STEMS[int(k[2:])] for k, v in m.groupdict().items() if k.startswith("s_") and v]
            o = _M(); o.neg = m.group("neg"); o.stem = st[0]
            yield o
PRE = PREc
HRE = re.compile(r"(?<![ऀ-ॿ-])(" + "|".join(sorted(HN, key=len, reverse=True)) + r")-कारण(\s+(?:के बिना|का अभाव|के अभाव))?")

PNUM = {"ekaṃ": 1, "eko": 1, "ekā": 1, "dve": 2, "tayo": 3, "tīṇi": 3, "tisso": 3, "cattāro": 4, "cattāri": 4,
        "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12,
        "terasa": 13, "cuddasa": 14, "pannarasa": 15, "soḷasa": 16, "sattarasa": 17, "aṭṭhārasa": 18,
        "ekūnavīsati": 19, "vīsati": 20, "ekavīsati": 21, "bāvīsati": 22, "tevīsati": 23, "catuvīsati": 24}
HNUM = {"एक": 1, "दो": 2, "तीन": 3, "चार": 4, "पाँच": 5, "छह": 6, "सात": 7, "आठ": 8, "नौ": 9, "दस": 10,
        "ग्यारह": 11, "बारह": 12, "तेरह": 13, "चौदह": 14, "पंद्रह": 15, "सोलह": 16, "सत्रह": 17, "अठारह": 18,
        "उन्नीस": 19, "बीस": 20, "इक्कीस": 21, "बाईस": 22, "तेईस": 23, "चौबीस": 24}
PNRE = re.compile(r"(?<![" + PL + r"])(" + "|".join(sorted(PNUM, key=len, reverse=True)) + r")(?![" + PL + r"])")
HNRE = re.compile(r"(?<![ऀ-ॿ-])(" + "|".join(sorted(HNUM, key=len, reverse=True)) + r")(?![ऀ-ॿ-])")

TERMS = [  # (name, pali regex, hindi regex)
    ("cittasamutthana", r"cittasamuṭṭhān", r"मन से उत्पन्न"),
    ("katatta", r"kaṭattā", r"किए गए कर्म से उत्पन्न"),
    ("upada", r"upādā", r"व्युत्पन्न"),
    ("patisandhi", r"paṭisandhi", r"पुनर्जन्म"),
    ("vatthu", r"vatth[uū]", r"आधार"),
    ("mahabhuta", r"mahābhūt", r"महाभूत"),
    ("khandha", r"khandh", r"समूह"),
    ("asanna", r"asaññasatt", r"पहचान-रहित"),
    ("bahira", r"bāhir", r"बाह्य"),
    ("ahara-samu", r"āhārasamuṭṭhān", r"आहार से उत्पन्न"),
    ("utu", r"utusamuṭṭhān", r"तापमान से उत्पन्न"),
    ("kiriya", r"kiriy", r"क्रिया"),
    ("vipaka-adj", r"vipāk(?!apaccay)", r"कर्म-फल(?!-कारण)"),
    ("pavatte", r"pavatt", r"जीवन-प्रवाह|प्रवाह"),
    ("rupa", r"rūp", r"भौतिक|रूप"),
]

def items_p(p):
    q = p.lower()
    q = q.replace("vipākābyākataṃ kiriyābyākataṃ", "XBYAKAT")
    ab = len(re.findall(r"byākat", q)) + q.count("XBYAKAT")
    k = 0; a = 0
    for m in re.finditer(r"kusal", q):
        s = m.start()
        if s > 0 and q[s - 1] in "aā":
            a += 1
        else:
            k += 1
    return k, a, ab

def items_h(h):
    return h.count("हितकर"), h.count("हानिकर"), h.count("अनिर्धारित")

def conds_p(p):
    return Counter((m.stem, "N" if m.neg else "P") for m in PRE.finditer(p.lower()))

def conds_h(h):
    return Counter((H2P[m.group(1)], "N" if m.group(2) else "P") for m in HRE.finditer(h))

res = {"cond": [], "item": [], "num": [], "term": []}
for f in FILES[1:]:
    for n, sid, p, h in pairs(f):
        if p.startswith("#"):
            continue
        pb = re.sub(r"\{[^}]*\}", "", p); hb = re.sub(r"\[[^\]]*\]", "", h)
        cp, ch = conds_p(pb), conds_h(hb)
        if cp != ch:
            res["cond"].append((f, n, sid, dict(cp - ch), dict(ch - cp)))
        ip, ih = items_p(pb), items_h(hb)
        if ip != ih:
            res["item"].append((f, n, sid, ip, ih))
        np_ = Counter(PNUM[m.group(1)] for m in PNRE.finditer(pb.lower()))
        nh = Counter(HNUM[m.group(1)] for m in HNRE.finditer(hb))
        if np_ != nh:
            res["num"].append((f, n, sid, dict(np_ - nh), dict(nh - np_)))
        for name, pr, hr in TERMS:
            a = len(re.findall(pr, pb.lower())); b = len(re.findall(hr, hb))
            if a != b:
                res["term"].append((f, n, sid, name, a, b))

with open(os.path.join(OUT, "review_r1_check_out.txt"), "w", encoding="utf-8") as fh:
    for k, v in res.items():
        fh.write(f"##### {k} {len(v)}\n")
        for r in v:
            fh.write(" ".join(str(x) for x in r) + "\n")
for k, v in res.items():
    print(k, len(v))
c = Counter(r[3] for r in res["term"])
print(c)

