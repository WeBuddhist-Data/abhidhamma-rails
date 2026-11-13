import sys, os, re
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *

STEMS = ["hetu", "ārammaṇa", "adhipati", "anantara", "samanantara", "sahajāta", "aññamañña", "nissaya",
         "upanissaya", "purejāta", "pacchājāta", "āsevana", "kamma", "vipāka", "āhāra", "indriya", "jhāna",
         "magga", "sampayutta", "vippayutta", "atthi", "natthi", "vigata", "avigata"]
# locative / count forms
LOC = {"hetu": ["hetuyā"], "ārammaṇa": ["ārammaṇe"], "adhipati": ["adhipatiyā"], "anantara": ["anantare"],
       "samanantara": ["samanantare"], "sahajāta": ["sahajāte"], "aññamañña": ["aññamaññe"], "nissaya": ["nissaye"],
       "upanissaya": ["upanissaye"], "purejāta": ["purejāte"], "pacchājāta": ["pacchājāte"], "āsevana": ["āsevane"],
       "kamma": ["kamme"], "vipāka": ["vipāke"], "āhāra": ["āhāre"], "indriya": ["indriye"], "jhāna": ["jhāne"],
       "magga": ["magge"], "sampayutta": ["sampayutte"], "vippayutta": ["vippayutte"], "atthi": ["atthiyā"],
       "natthi": ["natthiyā"], "vigata": ["vigate"], "avigata": ["avigate"]}
SUF = ["paccayā", "paccayena", "paccayo", "paccayādi", "paccaye", "paccayaṃ", "dukaṃ"]
HN = {"hetu": "मूल", "ārammaṇa": "विषय", "adhipati": "प्रधानता", "anantara": "निकटता", "samanantara": "पूर्ण निकटता",
      "sahajāta": "सह-उत्पत्ति", "aññamañña": "परस्पर", "nissaya": "आश्रय", "upanissaya": "प्रबल आश्रय",
      "purejāta": "पूर्व-उत्पत्ति", "pacchājāta": "पश्चात्-उत्पत्ति", "āsevana": "पुनरावृत्ति", "kamma": "कर्म",
      "vipāka": "कर्म-फल", "āhāra": "आहार", "indriya": "क्षमता", "jhāna": "ध्यान", "magga": "मार्ग",
      "sampayutta": "जुड़ाव", "vippayutta": "अलगाव", "atthi": "उपस्थिति", "natthi": "अनुपस्थिति",
      "vigata": "विलीनता", "avigata": "अविलीनता"}
H2S = {v: k for k, v in HN.items()}
halt = sorted(HN.values(), key=len, reverse=True)
HRE = re.compile(r"(" + "|".join(re.escape(x) for x in halt) + r")-कारण( के बिना| के अभाव| का अभाव)?")

forms = {}
for s in STEMS:
    for suf in SUF:
        forms[s + suf] = s
    for l in LOC[s]:
        forms[l] = s


def pconds(text):
    out = []
    for tok in re.findall(r"[a-zāīūṃṅñṭḍṇḷ]+", text.lower()):
        if tok in forms:
            out.append((forms[tok], "+")); continue
        for pre in ("no", "na"):
            if tok.startswith(pre) and tok[len(pre):] in forms:
                out.append((forms[tok[len(pre):]], "-")); break
    return out


def hconds(text):
    return [(H2S[m.group(1)], "-" if m.group(2) else "+") for m in HRE.finditer(text)]


PN = {"ekaṃ": 1, "eko": 1, "ekā": 1, "ekena": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tīṇi": 3, "tiṇṇaṃ": 3,
      "tiṇṇannaṃ": 3, "cattāri": 4, "cattāro": 4, "catunnaṃ": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8,
      "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12, "terasa": 13, "cuddasa": 14, "pannarasa": 15,
      "soḷasa": 16, "sattarasa": 17, "aṭṭhārasa": 18, "ekūnavīsati": 19, "vīsati": 20}
HNUM = {"एक": 1, "दो": 2, "तीन": 3, "चार": 4, "पाँच": 5, "छह": 6, "सात": 7, "आठ": 8, "नौ": 9, "दस": 10,
        "ग्यारह": 11, "बारह": 12, "तेरह": 13, "चौदह": 14, "पंद्रह": 15, "सोलह": 16, "सत्रह": 17, "अठारह": 18,
        "उन्नीस": 19, "बीस": 20}


def pnums(t):
    t = re.sub(r"\{[^}]*\}", "", t)
    return [PN[w] for w in re.findall(r"[a-zāīūṃṅñṭḍṇḷ]+", t.lower()) if w in PN]


def hnums(t):
    t = re.sub(r"\[[^\]]*\]", "", t)
    toks = re.findall(r"[ऀ-ॣ०-ॿ]+", t)
    return [HNUM[w] for w in toks if w in HNUM]


TERMS = [  # (pali regex, hindi regex, name)
    (r"paṭisandhi", r"पुनर्जन्म", "patisandhi"),
    (r"cittasamuṭṭhān", r"मन से उत्पन्न", "cittasamutthana"),
    (r"kaṭattā", r"किए गए कर्म से उत्पन्न", "katatta"),
    (r"upādārūp", r"व्युत्पन्न", "upadarupa"),
    (r"mahābhūt", r"महाभूत", "mahabhuta"),
    (r"vatthu", r"आधार", "vatthu"),
    (r"khandh", r"समूह", "khandha"),
    (r"bāhir", r"बाह्य", "bahira"),
    (r"āhārasamuṭṭhān", r"आहार से उत्पन्न", "aharasamutthana"),
    (r"utusamuṭṭhān", r"तापमान से उत्पन्न", "utusamutthana"),
    (r"asaññasatt", r"पहचान-रहित", "asannasatta"),
    (r"cetan", r"इरादा|इरादे", "cetana"),
    (r"vicikicch", r"संशय", "vicikiccha"),
    (r"uddhacc", r"बेचैनी", "uddhacca"),
    (r"cakkaṃ", r"चक्र", "cakkam"),
    (r"saṃkhitt", r"संक्षिप्त", "samkhitta"),
    (r"(?<!a)kusal", r"हितकर", "kusala"),
    (r"akusal", r"हानिकर", "akusala"),
    (r"abyākat", r"अनिर्धारित", "abyakata"),
    (r"jīvitindriy", r"जीवन-क्षमता", "jivitindriya"),
    (r"kabaḷīkār", r"कौर", "kabalikara"),
    (r"nibbān", r"निर्वाण", "nibbana"),
    (r"gotrabhu", r"गोत्र", "gotrabhu"),
    (r"āvajjan", r"मोड़न", "avajjana"),
    (r"(?<![a-z])(lobh|alobh)", r"लोभ", "lobha"),
    (r"(?<![a-z])(dos|ados)", r"द्वेष", "dosa"),
    (r"(?<![a-z])(moh|amoh)", r"मोह", "moha"),
    (r"arūp", r"अभौतिक", "arupa"),
    (r"diṭṭh", r"दृष्टि", "ditthi"),
    (r"(?<![a-z])rūpāyatan", r"दृश्य रूप का", "rupayatana"),
    (r"cakkhuviññāṇ", r"आँख की चेतना", "cakkhuvinnana"),
    (r"kāyaviññāṇ", r"शरीर की चेतना", "kayavinnana"),
    (r"pañcaviññāṇ", r"पाँच प्रकार की चेतना", "pancavinnana"),
    (r"(?<!s)ahetuk", r"मूल से रहित", "ahetuka"),
    (r"kāmupādān|kāmūpādān", r"काम", "kamupadana"),
    (r"sīlabbat", r"शील|व्रत", "silabbata"),
    (r"attavād", r"आत्म", "attavada"),
    (r"(?<![a-z])rāg", r"राग", "raga"),
    (r"pacchājāt", r"बाद में उत्पन्न|पश्चात्", "pacchajata"),
    (r"purejāt", r"पहले उत्पन्न|पूर्व-उत्पत्ति", "purejata"),
    (r"(?<![a-z])(anulom)", r"सकारात्मक|अनुरूपता|अनुलोम", "anuloma"),
    (r"paccanīy", r"नकारात्मक", "paccaniya"),
]


def strip_id(l):
    return IDRE.sub("", l).rstrip()


def tail(l):
    s = strip_id(l)
    s = re.sub(r"\s*\(\d+\)\s*$", "", s)
    return s


issues = defaultdict(list)
nseg = 0
nlines = 0
for fn in FILES:
    P, H = pairs(fn)
    nseg += len(segments(P))
    ne = 0
    for i, (a, b) in enumerate(zip(P, H), 1):
        if not a.strip():
            continue
        ne += 1
        nlines += 1
        loc = f"{fn[:4]}:{i}(ne{ne})"
        pid = IDRE.search(a); hid = IDRE.search(b)
        if (pid.group(1) if pid else None) != (hid.group(1) if hid else None):
            issues["id"].append((loc, a[-30:], b[-30:]))
        if a.startswith("#"):
            if a.split()[0] != b.split()[0]:
                issues["headlevel"].append((loc, a, b))
            continue
        # markers
        pm = re.findall(r"\((\d+)\)", a); hm = re.findall(r"\((\d+)\)", b)
        if pm != hm:
            issues["marker"].append((loc, pm, hm))
        # conditions
        pc = pconds(a); hc = hconds(b)
        if pc != hc:
            issues["cond"].append((loc, pc, hc))
        # numbers
        pn = pnums(a); hn = hnums(b)
        if pn != hn:
            issues["num"].append((loc, pn, hn))
        # dashes
        pd = a.count("–") + a.count("—"); hd = b.count("–") + b.count("—")
        if pd != hd:
            issues["dash"].append((loc, pd, hd))
        if "—" in b:
            issues["emdash"].append((loc,))
        # quotes
        if '"' in b or "'" in b:
            issues["straightquote"].append((loc, b[:60]))
        if b.count("“") != b.count("”"):
            issues["quotebal"].append((loc,))
        pq = a.count('"') // 2 + a.count("“"); hq = b.count("“")
        if pq != hq:
            issues["quotecount"].append((loc, pq, hq))
        # latin outside brackets
        bb = re.sub(r"\[[^\]]*\]", "", strip_id(b))
        lat = re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", bb)
        if lat:
            issues["latin"].append((loc, lat))
        # braces -> brackets
        if a.count("{") != b.count("[पाठभेद") + b.count("[वर्तनी-भेद"):
            issues["variant"].append((loc, a.count("{"), b.count("[")))
        # ending punct
        ta = tail(a); tb = tail(b)
        ea = ta[-1:] if ta else ""; eb = tb[-1:] if tb else ""
        exp = {".": "।", "?": "?", "…": "…", ")": ")", ";": ";", ",": ","}.get(ea, ea)
        if ea == "." and ta.endswith("….") :
            exp = "।"
        if eb != exp:
            if not (ea == ")" and tb.endswith("।)")) and not (ea == "." and eb == "?"):
                issues["endpunct"].append((loc, ta[-25:], tb[-25:]))
        if "।।" in b or "। ।" in b or "  " in strip_id(b):
            issues["doublepunct/space"].append((loc,))
        if "." in re.sub(r"\[[^\]]*\]", "", strip_id(b)).replace("...", ""):
            # period inside Hindi (not in brackets)
            if re.search(r"[ऀ-ॿ]\.", bb) or re.search(r"\.\s", bb):
                issues["period"].append((loc, bb[max(0, bb.find('.')-20):bb.find('.')+10]))
        # cakkam etc term counts
        al = a.lower()
        for pr, hr, nm in TERMS:
            c1 = len(re.findall(pr, al)); c2 = len(re.findall(hr, b))
            if nm == "anuloma":
                c2 = len(re.findall(hr, b))
            if c1 != c2:
                issues["term:" + nm].append((loc, c1, c2))

print("non-empty lines", nlines, "segments", nseg)
for k in sorted(issues):
    v = issues[k]
    print(f"=== {k}: {len(v)}")
    for x in v[: int(sys.argv[1]) if len(sys.argv) > 1 else 40]:
        print("   ", x)
