"""Hindi plain zero-shot of pi-7 files 2-01-vitakkattika, 2-02-pitittika, 2-03-dassanenapahatabbattika.

Composes every line from fixed frames: the Pāli is normalised (triad items -> @<ending> slots,
conditions -> %A/%N/%I slots), each normalised clause is looked up in the template table
(tpl_2-01_2-03.py), and the Hindi template is filled with the item / condition forms.
Identical Pāli therefore always gives identical Hindi.

    python -I -B -X utf8 build_2-01_2-03_hi.py            # write + check
    python -I -B -X utf8 build_2-01_2-03_hi.py --dry      # list unmatched clauses only
"""
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
sys.path.insert(0, str(HERE))
import build_sample_hi as S  # noqa: E402
import tpl_2_01_2_03 as TP   # noqa: E402

FILES = ["2-01-vitakkattika.md", "2-02-pitittika.md", "2-03-dassanenapahatabbattika.md"]

# =====================================================================================
# Items (pi-1 1-matika.md, triads 6, 7, 8)
# =====================================================================================
END = {"f": "ी", "m": "ा", "mo": "े"}
ITEM_HI = {
    "sv": "आरंभिक विचार और सतत विचार वाल{E}",
    "avm": "आरंभिक विचार से रहित, केवल सतत विचार वाल{E}",
    "aa": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "pi": "उल्लास के साथ होने वाल{E}",
    "su": "सुख के साथ होने वाल{E}",
    "up": "समभाव के साथ होने वाल{E}",
    "da": "सत्य-दर्शन से छोड़{E} जाने वाल{E}",
    "bh": "मानसिक अभ्यास से छोड़{E} जाने वाल{E}",
    "ne": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़{E} जाने वाल{E}",
}
ITEM_STEM = {
    "sv": "savitakkasavicār", "avm": "avitakkavicāramatt", "aa": "avitakkaavicār",
    "pi": "pītisahagat", "su": "sukhasahagat", "up": "upekkhāsahagat",
    "ne": "nevadassanena nabhāvanāya pahātabb", "da": "dassanena pahātabb", "bh": "bhāvanāya pahātabb",
}
STEM2KEY = {v.lower(): k for k, v in ITEM_STEM.items()}
# endings: (pāli ending, slot case, has 'ca')
ENDINGS = [
    ("acittasamaṅgissa", "acittasamaṅgissa", False), ("amūlakā", "amūlakā", False),
    ("amūlake", "amūlake", False), ("ādhipati", "ādhipati", False),
    ("ānañca", "ānaṃ", True), ("assa ca", "assa", True), ("āya ca", "āya", True), ("ena ca", "ena", True),
    ("ānaṃ", "ānaṃ", False), ("assa", "assa", False), ("añca", "aṃ", True), ("āya", "āya", False),
    ("āni", "āni", False), ("ena", "ena", False), ("o ca", "o", True), ("ā ca", "ā", True),
    ("e ca", "e", True), ("opi", "opi", False), ("aṃ", "aṃ", False), ("o", "o", False), ("ā", "ā", False),
    ("e", "e", False), ("a", "a", False),
]
_STEMS_RX = "|".join(re.escape(s) for s in sorted(ITEM_STEM.values(), key=len, reverse=True))
_END_RX = "|".join(re.escape(e) for e, _, _ in ENDINGS)
ITEM_RX = re.compile(r"(?<![\wāīūṃñṅṭḍṇḷ])(" + _STEMS_RX + r")(" + _END_RX + r")(?![\wāīūṃñṅṭḍṇḷ])", re.I)
END2 = {e: (c, ca) for e, c, ca in ENDINGS}


def adj(key, g):
    return ITEM_HI[key].replace("{E}", END[g])


def join(ws):
    return ws[0] if len(ws) == 1 else ", ".join(ws[:-1]) + " और " + ws[-1]


class Item:
    def __init__(self, keys, case):
        self.keys, self.case = keys, case

    def form(self, f):
        ks = self.keys
        pl = len(ks) > 1
        if f in ("f", "m", "mo"):
            return join([adj(k, f) for k in ks])
        if f == "dh":      # OBJ: X परिघटना और Y परिघटना
            return join([f"{adj(k, 'f')} {S.DHAMMA}" for k in ks])
        if f == "dat":
            return join([f"{adj(k, 'f')} {S.DHAMMA}" for k in ks]) + " के लिए"
        if f == "dhs":     # RES: X परिघटना / X और Y परिघटनाएँ
            return (join([adj(k, "f") for k in ks]) + " " + S.DHAMMA_PL) if pl else f"{adj(ks[0], 'f')} {S.DHAMMA}"
        if f == "upp":
            return "उत्पन्न होती हैं" if pl else "उत्पन्न होती है"
        if f == "hoti":
            return "होती हैं" if pl else "होती है"
        raise KeyError(f)


class Cond:
    def __init__(self, k, kind):
        self.k, self.kind = k, kind

    def form(self, f=None):
        k = self.k
        return {"A": S.ABL, "N": S.NABL, "I": S.INS, "P": S.NAME, "NP": S.NNAME}[self.kind](k)


_COND_STEMS = "|".join(sorted(S.COND_KEYS, key=len, reverse=True))
COND_RX = re.compile(r"(?<![\wāīūṃñṅṭḍṇḷ])(na|no)?(" + _COND_STEMS + r")paccay(ena paccayo|ā|o)(?![\wāīūṃñṅṭḍṇḷ])", re.I)


def normalize(text):
    """-> (normalised key, [slots])"""
    text = text.replace("avitakka vicāramatt", "avitakkavicāramatt")   # source spacing slip (2-01)
    slots = []
    out = []
    pos = 0
    events = []
    for m in ITEM_RX.finditer(text):
        events.append((m.start(), m.end(), "item", m))
    for m in COND_RX.finditer(text):
        events.append((m.start(), m.end(), "cond", m))
    events.sort(key=lambda e: e[0])
    i = 0
    while i < len(events):
        s, e, kind, m = events[i]
        if s < pos:
            i += 1
            continue
        out.append(text[pos:s])
        if kind == "cond":
            neg, stem, end = m.group(1), m.group(2).lower(), m.group(3)
            if end == "ena paccayo":
                kd = "IN" if neg else "I"
            elif end == "ā":
                kd = "N" if neg else "A"
            else:
                kd = "NP" if neg else "P"
            slots.append(Cond(stem, kd))
            out.append("%" + kd)
            pos = e
            i += 1
            continue
        # item, possibly a 'ca' group
        keys = [STEM2KEY[m.group(1).lower()]]
        case, ca = END2[m.group(2).lower()] if m.group(2).lower() in END2 else END2[m.group(2)]
        pos = e
        i += 1
        while ca and i < len(events) and events[i][2] == "item":
            s2, e2, _, m2 = events[i]
            if text[pos:s2].strip():
                break
            c2, ca2 = END2[m2.group(2).lower()]
            if not ca2 or c2 != case:
                break
            keys.append(STEM2KEY[m2.group(1).lower()])
            pos = e2
            i += 1
        slots.append(Item(keys, case))
        out.append("@" + case)
    out.append(text[pos:])
    key = "".join(out)
    key = key[:1].lower() + key[1:]
    return key, slots


SLOT_RX = re.compile(r"\{(\d+)(?::(\w+))?\}")


def render(tpl, slots):
    def rep(m):
        n, f = int(m.group(1)), m.group(2)
        sl = slots[n - 1]
        return sl.form(f) if isinstance(sl, Item) else sl.form()
    return SLOT_RX.sub(rep, tpl)


# =====================================================================================
# Templates
# =====================================================================================
TPL = {}
for raw in TP.TEMPLATES.splitlines():
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    p, h = line.split(" ⇒ ")
    p = p.strip()
    if p in TPL and TPL[p] != h.strip():
        raise SystemExit(f"conflicting template: {p}")
    TPL[p] = h.strip()

UNMATCHED = collections.Counter()
UNM_EX = {}
STATE = {"verb": "होती है"}   # agreement of a subject-less "…paccayena paccayo" (reset per line)


def lookup(text):
    key, slots = normalize(text.strip())
    if key in TPL:
        tpl = TPL[key]
        m = re.search(r"\{(\d+):dhs\}", tpl)
        if m:
            STATE["verb"] = slots[int(m.group(1)) - 1].form("hoti")
        return render(tpl, slots)
    return np_engine(key, slots)


# =====================================================================================
# Noun-phrase engine (dependency, pañhā and arising clauses built from nominals)
# =====================================================================================
# Hindi nouns: (direct sg, direct pl, oblique sg, oblique pl, gender)
NH = {
    "khandha": ("समूह", "समूह", "समूह", "समूहों", "m"),
    "vitakka": ("आरंभिक विचार", "आरंभिक विचार", "आरंभिक विचार", "आरंभिक विचारों", "m"),
    "vicara": ("सतत विचार", "सतत विचार", "सतत विचार", "सतत विचारों", "m"),
    "vatthu": ("आधार", "आधार", "आधार", "आधारों", "m"),
    "mahabhuta": ("महाभूत", "महाभूत", "महाभूत", "महाभूतों", "m"),
    "csr": (S.CSR, S.CSR, S.CSR, S.CSR_OBL, "m"),
    "ktr": (S.KTR, S.KTR, S.KTR, S.KTR_OBL, "m"),
    "upr": (S.UPR, S.UPR, S.UPR, S.UPR_OBL, "m"),
    "cetana": ("इरादा", "इरादे", "इरादे", "इरादों", "m"),
    "moha": ("मोह", "मोह", "मोह", "मोहों", "m"),
    "hetu": ("मूल", "मूल", "मूल", "मूलों", "m"),
    "adhipati": ("प्रधानता", "प्रधानताएँ", "प्रधानता", "प्रधानताओं", "f"),
    "ahara": ("आहार", "आहार", "आहार", "आहारों", "m"),
    "indriya": ("क्षमता", "क्षमताएँ", "क्षमता", "क्षमताओं", "f"),
    "jhananga": ("ध्यान का अंग", "ध्यान के अंग", "ध्यान के अंग", "ध्यान के अंगों", "m"),
    "magganga": ("मार्ग का अंग", "मार्ग के अंग", "मार्ग के अंग", "मार्ग के अंगों", "m"),
    "rji": (S.RUPAJIVITINDRIYA, S.RUPAJIVITINDRIYA, S.RUPAJIVITINDRIYA, S.RUPAJIVITINDRIYA, "f"),
    "kabalikara": ("कौर-कौर खाया जाने वाला भोजन", "", "कौर-कौर खाए जाने वाले भोजन", "", "m"),
    "dhamma": (S.DHAMMA, S.DHAMMA_PL, S.DHAMMA, S.DHAMMA_OBL_PL, "f"),
    "citta": ("मन", "मन", "मन", "मनों", "m"),
    "anuloma": ("अनुरूपता", "अनुरूपताएँ", "अनुरूपता", "अनुरूपताओं", "f"),
    "gotrabhu": (S.GOTRABHU, S.GOTRABHU, S.GOTRABHU, S.GOTRABHU, "m"),
    "vodana": (S.VODANA, S.VODANA, S.VODANA, S.VODANA, "f"),
    "magga": ("मार्ग", "मार्ग", "मार्ग", "मार्गों", "m"),
    "phala": ("फल", "फल", "फल", "फलों", "m"),
    "phalasamapatti": ("फल की ध्यान-अवस्था", "", "फल की ध्यान-अवस्था", "", "f"),
    "cuticitta": ("मृत्यु का मन", "", "मृत्यु के मन", "", "m"),
    "upapatticitta": ("जन्म का मन", "", "जन्म के मन", "", "m"),
    "bhavanga": ("जीवन-धारा का मन", "", "जीवन-धारा के मन", "", "m"),
    "avajjana": ("मन को विषय की ओर मोड़ना", "", "मन को विषय की ओर मोड़ने", "", "m"),
    "vutthana": ("बाहर आना", "", "बाहर आने", "", "m"),
    "kusalakusala": ("हितकर और हानिकर मन", "", "हितकर और हानिकर मन", "", "m"),
    "kiriya": ("केवल क्रिया रूपी मन", "", "केवल क्रिया रूपी मन", "", "m"),
    "vmvd": ("कर्म के फल रूपी मन की चेतना का तत्व", "", "कर्म के फल रूपी मन की चेतना के तत्व", "", "m"),
    "kmvd": ("केवल क्रिया रूपी मन की चेतना का तत्व", "", "केवल क्रिया रूपी मन की चेतना के तत्व", "", "m"),
    "vmd": ("कर्म के फल रूपी मन का तत्व", "", "कर्म के फल रूपी मन के तत्व", "", "m"),
    "kayavinnana": ("शरीर की चेतना", "", "शरीर की चेतना", "", "f"),
    "nsna": ("न पहचान न अ-पहचान का क्षेत्र", "", "न पहचान न अ-पहचान के क्षेत्र", "", "m"),
    "nirodha_nsna": ("समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति का न पहचान न अ-पहचान का क्षेत्र", "",
                     "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति के न पहचान न अ-पहचान के क्षेत्र", "", "m"),
    "aka": ("अनंत आकाश का क्षेत्र", "", "अनंत आकाश के क्षेत्र", "", "m"),
    "vinna": ("अनंत चेतना का क्षेत्र", "", "अनंत चेतना के क्षेत्र", "", "m"),
    "akin": ("कुछ भी न होने का क्षेत्र", "", "कुछ भी न होने के क्षेत्र", "", "m"),
    "nibbana": ("निर्वाण", "", "निर्वाण", "", "m"),
    "saddha": ("श्रद्धा", "", "श्रद्धा", "", "f"),
    "sila": ("सदाचार", "", "सदाचार", "", "m"),
    "suta": ("सुना-सीखा ज्ञान", "", "सुने-सीखे ज्ञान", "", "m"),
    "caga": ("त्याग", "", "त्याग", "", "m"),
    "panna": ("प्रज्ञा", "", "प्रज्ञा", "", "f"),
    "raga": ("राग", "", "राग", "", "m"),
    "dosa": ("द्वेष", "", "द्वेष", "", "m"),
    "mana": ("अहंकार", "", "अहंकार", "", "m"),
    "ditthi": ("दृष्टि", "", "दृष्टि", "", "f"),
    "patthana": ("कामना", "", "कामना", "", "f"),
    "vicikiccha": ("संशय", "", "संशय", "", "m"),
    "uddhacca": ("बेचैनी", "", "बेचैनी", "", "f"),
    "domanassa": ("उदासी", "", "उदासी", "", "f"),
    "kayika_sukha": ("शारीरिक सुख", "", "शारीरिक सुख", "", "m"),
    "kayika_dukkha": ("शारीरिक दुःख", "", "शारीरिक दुःख", "", "m"),
    "utu": ("तापमान", "", "तापमान", "", "m"),
    "bhojana": ("भोजन", "", "भोजन", "", "m"),
    "senasana": ("निवास-स्थान", "", "निवास-स्थान", "", "m"),
    "kaya_pure": ("पहले उत्पन्न इस शरीर", "", "पहले उत्पन्न इस शरीर", "", "m"),
    "kaya": ("इस शरीर", "", "इस शरीर", "", "m"),
    "vinnana5": ("", "पाँच प्रकार की चेतनाएँ", "", "पाँच प्रकार की चेतनाओं", "f"),
}

# Pāli forms -> ("N", nid, case, num); case: N nom, A acc, NA either, G gen/dat, I instr
LEX = {}


def _n(nid, **forms):
    for case_num, words in forms.items():
        case, num = case_num.split("_")
        for w in words.split("|"):
            LEX[w] = ("N", nid, case, num, False)


_n("khandha", N_sg="khandho", N_pl="khandhā", A_sg="khandhaṃ", A_pl="khandhe", G_pl="khandhānaṃ",
   G_sg="khandhassa")
_n("vitakka", N_sg="vitakko", A_sg="vitakkaṃ", G_sg="vitakkassa", N_pl="vitakkā")
_n("vicara", N_sg="vicāro", A_sg="vicāraṃ", G_sg="vicārassa")
_n("vatthu", N_sg="vatthu", A_sg="vatthuṃ", G_sg="vatthussa")
_n("mahabhuta", N_pl="mahābhūtā", A_pl="mahābhūte", NA_sg="mahābhūtaṃ", G_pl="mahābhūtānaṃ",
   G_sg="mahābhūtassa")
_n("csr", NA_sg="cittasamuṭṭhānaṃ rūpaṃ", G_pl="cittasamuṭṭhānānaṃ rūpānaṃ")
_n("ktr", NA_sg="kaṭattārūpaṃ", G_pl="kaṭattārūpānaṃ")
_n("upr", NA_sg="upādārūpaṃ", G_pl="upādārūpānaṃ")
_n("cetana", N_sg="cetanā", A_sg="cetanaṃ", G_sg="cetanāya")
_n("moha", N_sg="moho", A_sg="mohaṃ", G_sg="mohassa")
_n("hetu", N_pl="hetū", N_sg="hetu")
_n("adhipati", N_sg="adhipati")
_n("ahara", N_pl="āhārā")
_n("indriya", N_pl="indriyā")
_n("jhananga", NA_pl="jhānaṅgāni")
_n("magganga", NA_pl="maggaṅgāni")
_n("rji", NA_sg="rūpajīvitindriyaṃ")
_n("kabalikara", N_sg="kabaḷīkāro āhāro")
_n("dhamma", N_sg="dhammo", N_pl="dhammā", A_sg="dhammaṃ", G_sg="dhammassa", G_pl="dhammānaṃ")
_n("citta", I_sg="cittena", NA_sg="cittaṃ")
_n("anuloma", NA_sg="anulomaṃ")
_n("gotrabhu", NA_sg="gotrabhu", G_sg="gotrabhussa")
_n("vodana", NA_sg="vodānaṃ", G_sg="vodānassa")
_n("magga", N_sg="maggo", A_sg="maggaṃ", G_sg="maggassa")
_n("phala", NA_sg="phalaṃ", G_sg="phalassa")
_n("phalasamapatti", G_sg="phalasamāpattiyā")
_n("cuticitta", NA_sg="cuticittaṃ")
_n("upapatticitta", G_sg="upapatticittassa")
_n("bhavanga", NA_sg="bhavaṅgaṃ", G_sg="bhavaṅgassa")
_n("avajjana", N_sg="āvajjanā", G_sg="āvajjanāya")
_n("vutthana", G_sg="vuṭṭhānassa")
_n("kusalakusala", NA_sg="kusalākusalaṃ")
_n("kiriya", NA_sg="kiriyaṃ")
_n("vmvd", N_sg="vipākamanoviññāṇadhātu", G_sg="vipākamanoviññāṇadhātuyā")
_n("kmvd", N_sg="kiriyamanoviññāṇadhātu", G_sg="kiriyamanoviññāṇadhātuyā")
_n("vmd", N_sg="vipākamanodhātu", G_sg="vipākamanodhātuyā")
_n("kayavinnana", NA_sg="kāyaviññāṇaṃ", G_sg="kāyaviññāṇassa")
_n("nsna", NA_sg="nevasaññānāsaññāyatanaṃ", G_sg="nevasaññānāsaññāyatanassa")
_n("nirodha_nsna", NA_sg="nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanaṃ")
_n("aka", NA_sg="ākāsānañcāyatanaṃ")
_n("vinna", G_sg="viññāṇañcāyatanassa")
_n("akin", NA_sg="ākiñcaññāyatanaṃ")
_n("nibbana", NA_sg="nibbānaṃ")
_n("saddha", N_sg="saddhā", A_sg="saddhaṃ", G_sg="saddhāya")
_n("sila", NA_sg="sīlaṃ", G_sg="sīlassa")
_n("suta", NA_sg="sutaṃ", G_sg="sutassa")
_n("caga", N_sg="cāgo", A_sg="cāgaṃ", G_sg="cāgassa")
_n("panna", N_sg="paññā", A_sg="paññaṃ", G_sg="paññāya")
_n("raga", N_sg="rāgo", A_sg="rāgaṃ", G_sg="rāgassa")
_n("dosa", N_sg="doso", A_sg="dosaṃ", G_sg="dosassa")
_n("mana", N_sg="māno", A_sg="mānaṃ", G_sg="mānassa")
_n("ditthi", N_sg="diṭṭhi", A_sg="diṭṭhiṃ", G_sg="diṭṭhiyā")
_n("patthana", N_sg="patthanā", A_sg="patthanaṃ", G_sg="patthanāya")
_n("vicikiccha", N_sg="vicikicchā")
_n("uddhacca", NA_sg="uddhaccaṃ")
_n("domanassa", NA_sg="domanassaṃ")
_n("kayika_sukha", NA_sg="kāyikaṃ sukhaṃ", G_sg="kāyikassa sukhassa")
_n("kayika_dukkha", NA_sg="kāyikaṃ dukkhaṃ", G_sg="kāyikassa dukkhassa")
_n("utu", N_sg="utu", A_sg="utuṃ")
_n("bhojana", NA_sg="bhojanaṃ")
_n("senasana", NA_sg="senāsanaṃ")
_n("kaya_pure", G_sg="purejātassa imassa kāyassa")
_n("kaya", G_sg="imassa kāyassa")
_n("vinnana5", G_pl="pañcannaṃ viññāṇānaṃ")

# 'ca' variants: "X ca" and "Xñca" (for -ṃ forms); special multiword ca forms
for _w, _v in list(LEX.items()):
    LEX[_w + " ca"] = _v[:4] + (True,)
    if _w.endswith("ṃ") and " " not in _w:
        LEX[_w[:-1] + "ñca"] = _v[:4] + (True,)
LEX["cittasamuṭṭhānañca rūpaṃ"] = ("N", "csr", "NA", "sg", True)
LEX["cittasamuṭṭhānānañca rūpānaṃ"] = ("N", "csr", "G", "pl", True)
LEX["kaṭattā ca rūpaṃ"] = ("N", "ktr", "NA", "sg", True)
LEX["kaṭattā ca rūpānaṃ"] = ("N", "ktr", "G", "pl", True)

# numbers: (hindi, number, case)
for _w, _h, _num, _case in [("eko", "एक", "sg", "N"), ("ekaṃ", "एक", "sg", "NA"), ("ekassa", "एक", "sg", "G"),
                            ("dve", "दो", "pl", "NA"), ("tayo", "तीन", "pl", "NA"),
                            ("tiṇṇannaṃ", "तीन", "pl", "G"), ("dvinnaṃ", "दो", "pl", "G")]:
    LEX[_w] = ("NUM", _h, _num, _case)

# fixed modifiers: (forms {f,m,mo} or str, case, before-number?)
def _mod(w, forms, case, pre=True):
    LEX[w] = ("MOD", forms, case, pre)


def _e(stem):
    return {g: stem.replace("{E}", END[g]) for g in ("f", "m", "mo")}


_mod("ahetukaṃ", S.AHETUKA, "NA")
_mod("ahetuke", S.AHETUKA, "A")
_mod("ahetukā", S.AHETUKA, "N")
_mod("vipākaṃ", "कर्म के फल रूपी", "NA")
_mod("vipāke", "कर्म के फल रूपी", "A")
_mod("vipākā", "कर्म के फल रूपी", "N")
_mod("vipāko", "कर्म के फल रूपी", "N")
_mod("vipākānaṃ", "कर्म के फल रूपी", "G")
_mod("bāhiraṃ", S.BAHIRA, "NA", False)
_mod("āhārasamuṭṭhānaṃ", S.AHARASAM, "NA")
_mod("utusamuṭṭhānaṃ", S.UTUSAM, "NA")
_mod("pañcaviññāṇasahagataṃ", _e("पाँच प्रकार की चेतना के साथ होने वाल{E}"), "NA")
_mod("catuviññāṇasahagataṃ", _e("चार प्रकार की चेतना के साथ होने वाल{E}"), "NA")
_mod("kāyaviññāṇasahagataṃ", _e("शरीर की चेतना के साथ होने वाल{E}"), "NA")
_mod("vicikicchāsahagate uddhaccasahagate", _e("संशय के साथ होने वाल{E} और बेचैनी के साथ होने वाल{E}"), "A")
_mod("vicikicchāsahagataṃ uddhaccasahagataṃ", _e("संशय के साथ होने वाल{E} या बेचैनी के साथ होने वाल{E}"), "NA")
_mod("vicikicchāsahagato uddhaccasahagato", _e("संशय के साथ होने वाल{E} या बेचैनी के साथ होने वाल{E}"), "N")
_mod("sampayuttakānaṃ", {"f": "जुड़ी हुई", "m": "जुड़ा हुआ", "mo": "जुड़े हुए"}, "G")
_mod("purimā purimā", _e("पहले-पहले क{E}"), "N")
_mod("purimo purimo", _e("पहले-पहले क{E}"), "N")
_mod("pacchimānaṃ pacchimānaṃ", _e("बाद-बाद क{E}"), "G")
_mod("pacchimassa pacchimassa", _e("बाद-बाद क{E}"), "G")
_mod("pacchājātā", "बाद में उत्पन्न", "N")
_mod("purejātaṃ", "पहले उत्पन्न", "NA")

DEP_LEX = {"paṭicca": S.DEP["paṭicca"], "paccayā": S.DEP["paccaya"], "nissāya": S.DEP["nissaya"],
           "saṃsaṭṭho": S.DEP["saṃsaṭṭha"], "saṃsaṭṭhā": S.DEP["saṃsaṭṭha"], "saṃsaṭṭhaṃ": S.DEP["saṃsaṭṭha"],
           "sampayutto": S.DEP["sampayutta"], "sampayuttā": S.DEP["sampayutta"],
           "sampayuttaṃ": S.DEP["sampayutta"], "sahajāto": S.DEP["sahajāta"], "sahajātā": S.DEP["sahajāta"],
           "ārabbha": S.ARABBHA, "garuṃ katvā": S.GARUM, "upanissāya": "के प्रबल आश्रय से"}
for _w, _h in DEP_LEX.items():
    LEX[_w] = ("DEP", _h)
ADV_LEX = {"paṭisandhikkhaṇe": S.PATISANDHI, "arūpe": S.ARUPE, "asaññasattānaṃ": S.ASANNASATTA, "ahetukapaṭisandhikkhaṇe": S.AHETUKA_PATISANDHI,
           "taṃ ārabbha": "उसे विषय बनाकर", "taṃ garuṃ katvā": "उसे महत्व देकर"}
for _w, _h in ADV_LEX.items():
    LEX[_w] = ("ADV", _h)
for _w in ("uppajjati", "uppajjanti"):
    LEX[_w] = ("VERB", "उत्पन्न")


def _p(pl):
    return "उन" if pl else "उस"


# verb phrases taking the preceding noun phrase as object: (post-position, text(object plural?))
def _vp(w, post, fn):
    LEX[w] = ("VP", post, fn)


A3 = S.ANICCA3
for _sg, _suf in ((True, ""), (False, "")):
    pass
_VPS = {
    # pāli: (post, sg-subject text, pl-subject text)
    "paccavekkhati": ("पर", lambda p: S.REVIEW_SG),
    "paccavekkhanti": ("पर", lambda p: S.REVIEW_PL),
    "garuṃ katvā paccavekkhati": ("को", lambda p: f"महत्व देकर {_p(p)} पर {S.REVIEW_SG}"),
    "garuṃ katvā paccavekkhanti": ("को", lambda p: f"महत्व देकर {_p(p)} पर {S.REVIEW_PL}"),
    "jānāti": ("को", lambda p: "जानता है"),
    "jānanti": ("को", lambda p: "जानते हैं"),
    "aniccato dukkhato anattato": ("को", lambda p: A3),
    "aniccato dukkhato anattato vipassati": ("को", lambda p: f"{A3} {S.VIPASSATI}"),
    "aniccato dukkhato anattato vipassanti": ("को", lambda p: f"{A3} {S.VIPASSANTI}"),
    "aniccato dukkhato anattato vipassati assādeti abhinandati":
        ("को", lambda p: f"{A3} {S.VIPASSATI}, {_p(p)}{S.ASSADA}, {_p(p)}{S.ABHINANDA}"),
    "aniccato dukkhato anattato vipassanti assādenti abhinandanti":
        ("को", lambda p: f"{A3} {S.VIPASSANTI}, {_p(p)}का रस लेते हैं, {_p(p)}में आनंद लेते हैं"),
    "assādeti abhinandati": ("का", lambda p: f"रस लेता है, {_p(p)}{S.ABHINANDA}"),
    "assādeti": ("का", lambda p: "रस लेता है"),
    "garuṃ katvā assādeti abhinandati": ("को", lambda p: f"महत्व देकर {_p(p)}{S.ASSADA}, {_p(p)}{S.ABHINANDA}"),
    "garuṃ katvā": ("को", lambda p: "महत्व देकर"),
    "garuṃ katvā assādeti": ("को", lambda p: f"महत्व देकर {_p(p)}{S.ASSADA}"),
    "uppādeti": ("", lambda p: "उत्पन्न करता है"),
}
for _w, (_post, _fn) in _VPS.items():
    _vp(_w, _post, _fn)

# literal pieces (no noun phrase inside)
LIT_LEX = {
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā": S.DANA3,
    "taṃ paccavekkhati": f"उस पर {S.REVIEW_SG}",
    "taṃ paccavekkhanti": f"उस पर {S.REVIEW_PL}",
    "taṃ garuṃ katvā paccavekkhati": f"उसे महत्व देकर उस पर {S.REVIEW_SG}",
    "taṃ garuṃ katvā paccavekkhanti": f"उसे महत्व देकर उस पर {S.REVIEW_PL}",
    "taṃ assādeti abhinandati": f"उस{S.ASSADA}, उस{S.ABHINANDA}",
    "taṃ garuṃ katvā assādeti abhinandati": f"उसे महत्व देकर उस{S.ASSADA}, उस{S.ABHINANDA}",
    "dānaṃ deti": "दान देता है",
    "sīlaṃ samādiyati": "सदाचार ग्रहण करता है",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है",
    "mānaṃ jappeti": "अहंकार पालता है",
    "diṭṭhiṃ gaṇhāti": "दृष्टि को पकड़ता है",
    "pāṇaṃ hanati": "प्राणी की हत्या करता है",
    "adinnaṃ ādiyati": "बिना दिया हुआ लेता है",
    "musā bhaṇati": "झूठ बोलता है",
    "pisuṇaṃ bhaṇati": "चुगली करता है",
    "samphaṃ palapati": "व्यर्थ बकवास करता है",
    "sandhiṃ chindati": "सेंध लगाता है",
    "nillopaṃ harati": "डाका डालता है",
    "ekāgārikaṃ karoti": "किसी एक घर को लूटता है",
    "paripanthe tiṭṭhati": "राह में घात लगाकर खड़ा होता है",
    "paradāraṃ gacchati": "पराई स्त्री के पास जाता है",
    "gāmaghātaṃ karoti": "गाँव पर धावा बोलता है",
    "nigamaghātaṃ karoti": "कस्बे पर धावा बोलता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "dibbena cakkhunā rūpaṃ passati": "दिव्य आँख से दृश्य रूप देखता है",
    "dibbāya sotadhātuyā saddaṃ suṇāti": "दिव्य कान के तत्व से ध्वनि सुनता है",
    "ariyā": "आर्य",
}
for _w, _h in LIT_LEX.items():
    LEX[_w] = ("LIT", _h)

# more nouns
NH.update({
    "jhana": ("ध्यान", "ध्यान", "ध्यान", "ध्यानों", "m"),
    "kilesa": ("मन का क्लेश", "मन के क्लेश", "मन के क्लेश", "मन के क्लेशों", "m"),
    "sucinna": ("", "पहले भली-भाँति किए गए कार्य", "", "पहले भली-भाँति किए गए कार्यों", "m"),
    "ariya": ("आर्य", "आर्य", "आर्य", "आर्यों", "m"),
    "cakkhu": ("आँख", "", "आँख", "", "f"),
    "sota": ("कान", "", "कान", "", "m"),
    "ghana": ("नाक", "", "नाक", "", "f"),
    "jivha": ("जीभ", "", "जीभ", "", "f"),
    "kaya_s": ("शरीर", "", "शरीर", "", "m"),
    "rupa_o": ("दृश्य रूप", "दृश्य रूप", "दृश्य रूप", "दृश्य रूपों", "m"),
    "sadda": ("ध्वनि", "ध्वनियाँ", "ध्वनि", "ध्वनियों", "f"),
    "gandha": ("गंध", "गंध", "गंध", "गंधों", "f"),
    "rasa": ("स्वाद", "स्वाद", "स्वाद", "स्वादों", "m"),
    "photthabba": ("स्पर्श", "स्पर्श", "स्पर्श", "स्पर्शों", "m"),
    "vipassana": ("अंतर्दृष्टि", "", "अंतर्दृष्टि", "", "f"),
    "abhinna": ("उच्च ज्ञान", "", "उच्च ज्ञान", "", "m"),
    "samapatti": ("ध्यान-अवस्था", "", "ध्यान-अवस्था", "", "f"),
    "ceto": (S.CETOPARIYA, "", S.CETOPARIYA_OBL, "", "m"),
    "iddhi": ("अलौकिक शक्तियों का ज्ञान", "", S.IDDHIVIDHA_OBL, "", "m"),
    "pubbe": ("पूर्व जन्मों के अनुस्मरण का ज्ञान", "", S.PUBBENIVASA_OBL, "", "m"),
    "yatha": ("प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान", "", S.YATHAKAMMUPAGA_OBL, "", "m"),
    "anagata": ("भविष्य को जानने का ज्ञान", "", S.ANAGATAMSA_OBL, "", "m"),
    "aya_cakkhu": (S.AYA_SENSE("cakkhu"), "", S.AYA_SENSE("cakkhu").replace(" का ", " के "), "", "m"),
    "aya_kaya": (S.AYA_SENSE("kāya"), "", S.AYA_SENSE("kāya").replace(" का ", " के "), "", "m"),
    "aya_rupa": (S.AYA_OBJ("rūpa"), "", S.AYA_OBJ("rūpa").replace(" का ", " के "), "", "m"),
    "aya_phot": (S.AYA_OBJ("phoṭṭhabba"), "", S.AYA_OBJ("phoṭṭhabba").replace(" का ", " के "), "", "m"),
    "cakkhuvinnana": (S.VINNANA("cakkhu"), "", S.VINNANA("cakkhu"), "", "f"),
    "ar_label_sahajata": ("सह-उत्पत्ति", "", "सह-उत्पत्ति", "", "f"),
    "ar_dhipati": (S.ARAMMANADHIPATI, "", S.ARAMMANADHIPATI, "", "f"),
    "sj_dhipati": (S.SAHAJATADHIPATI, "", S.SAHAJATADHIPATI, "", "f"),
    "ar_upa": (S.ARAMMANUPANISSAYA, "", S.ARAMMANUPANISSAYA, "", "m"),
    "an_upa": (S.ANANTARUPANISSAYA, "", S.ANANTARUPANISSAYA, "", "m"),
    "pa_upa": (S.PAKATUPANISSAYA, "", S.PAKATUPANISSAYA, "", "m"),
    "ar_pure": (S.ARAMMANAPUREJATA, "", S.ARAMMANAPUREJATA, "", "f"),
    "va_pure": (S.VATTHUPUREJATA, "", S.VATTHUPUREJATA, "", "f"),
    "tam": ("वह", "", "उस", "", "m"),
})
LEX["taṃ"] = ("N", "tam", "NA", "sg", False)
for _w, _nid, _case, _num in [
        ("jhānā", "jhana", "B", "sg"), ("maggā", "magga", "B", "sg"), ("phalā", "phala", "B", "sg"),
        ("jhānaṃ", "jhana", "NA", "sg"), ("jhānassa", "jhana", "G", "sg"),
        ("kilese", "kilesa", "A", "pl"),
        ("pubbe suciṇṇāni", "sucinna", "NA", "pl"),
        ("cakkhuṃ", "cakkhu", "NA", "sg"), ("sotaṃ", "sota", "NA", "sg"), ("ghānaṃ", "ghana", "NA", "sg"),
        ("jivhaṃ", "jivha", "NA", "sg"), ("kāyaṃ", "kaya_s", "NA", "sg"), ("rūpe", "rupa_o", "A", "pl"),
        ("sadde", "sadda", "A", "pl"), ("gandhe", "gandha", "A", "pl"), ("rase", "rasa", "A", "pl"),
        ("phoṭṭhabbe", "photthabba", "A", "pl"), ("phoṭṭhabbaṃ", "photthabba", "NA", "sg"),
        ("vipassanaṃ", "vipassana", "NA", "sg"), ("abhiññaṃ", "abhinna", "NA", "sg"),
        ("samāpattiṃ", "samapatti", "NA", "sg"),
        ("cetopariyañāṇassa", "ceto", "G", "sg"), ("iddhividhañāṇassa", "iddhi", "G", "sg"),
        ("pubbenivāsānussatiñāṇassa", "pubbe", "G", "sg"), ("yathākammūpagañāṇassa", "yatha", "G", "sg"),
        ("anāgataṃsañāṇassa", "anagata", "G", "sg"),
        ("cakkhāyatanaṃ", "aya_cakkhu", "NA", "sg"), ("kāyāyatanaṃ", "aya_kaya", "NA", "sg"),
        ("rūpāyatanaṃ", "aya_rupa", "NA", "sg"), ("phoṭṭhabbāyatanaṃ", "aya_phot", "NA", "sg"),
        ("cakkhuviññāṇassa", "cakkhuvinnana", "G", "sg"),
        ("ārammaṇādhipati", "ar_dhipati", "N", "sg"), ("sahajātādhipati", "sj_dhipati", "N", "sg"),
        ("ārammaṇūpanissayo", "ar_upa", "N", "sg"), ("anantarūpanissayo", "an_upa", "N", "sg"),
        ("pakatūpanissayo", "pa_upa", "N", "sg"),
        ("ārammaṇapurejātaṃ", "ar_pure", "NA", "sg"), ("vatthupurejātaṃ", "va_pure", "NA", "sg"),
]:
    LEX[_w] = ("N", _nid, _case, _num, False)
    LEX[_w + " ca"] = ("N", _nid, _case, _num, True)
    if _w.endswith("ṃ"):
        LEX[_w[:-1] + "ñca"] = ("N", _nid, _case, _num, True)
LEX["kāyaviññāṇassa"] = ("N", "kayavinnana", "G", "sg", False)
_mod("pahīne", "छोड़े जा चुके", "A")
_mod("vikkhambhite", "दबाए जा चुके", "A")
_mod("pubbe samudāciṇṇe", "पहले बार-बार उठे", "A")
_mod("vicākānaṃ", "कर्म के फल रूपी", "G")       # source slip for vipākānaṃ
_mod("vipākassa", "कर्म के फल रूपी", "G")
LEX["kaṭattā rūpānaṃ"] = ("N", "ktr", "G", "pl", False)   # source: kaṭattā rūpānaṃ (= kaṭattārūpānaṃ)
# preliminary work (parikamma) of the jhānas, formless spheres and higher knowledges
_PK = {"dutiyassa jhānassa": "दूसरे ध्यान", "tatiyassa jhānassa": "तीसरे ध्यान",
       "catutthassa jhānassa": "चौथे ध्यान", "ākāsānañcāyatanassa": "अनंत आकाश के क्षेत्र",
       "viññāṇañcāyatanassa": "अनंत चेतना के क्षेत्र", "ākiñcaññāyatanassa": "कुछ भी न होने के क्षेत्र",
       "nevasaññānāsaññāyatanassa": "न पहचान न अ-पहचान के क्षेत्र", "dibbassa cakkhussa": "दिव्य आँख",
       "dibbāya sotadhātuyā": "दिव्य कान के तत्व", "iddhividhañāṇassa": S.IDDHIVIDHA_OBL,
       "cetopariyañāṇassa": S.CETOPARIYA_OBL, "pubbenivāsānussatiñāṇassa": S.PUBBENIVASA_OBL,
       "yathākammūpagañāṇassa": S.YATHAKAMMUPAGA_OBL, "anāgataṃsañāṇassa": S.ANAGATAMSA_OBL,
       "jhānassa": "ध्यान"}
for _w, _h in _PK.items():
    _nid = "pk_" + _w
    NH[_nid] = (f"{_h} की प्रारंभिक तैयारी", "", f"{_h} की प्रारंभिक तैयारी", "", "f", "mo")
    LEX[_w + " parikammaṃ"] = ("N", _nid, "NA", "sg", False)
    LEX[_w + " parikammañca"] = ("N", _nid, "NA", "sg", True)
    gid = "g_" + _w
    NH[gid] = (_h, "", _h, "", "m")
    if _w not in LEX:
        LEX[_w] = ("N", gid, "G", "sg", False)
        LEX[_w + " ca"] = ("N", gid, "G", "sg", True)
LEX["dutiye jhāne"] = ("ADV", "दूसरे ध्यान में")
LEX["dānaṃ datvā"] = ("LIT", "दान देकर")
_mod("vicikicchāsahagate", _e("संशय के साथ होने वाल{E}"), "A")
_mod("vicikicchāsahagato", _e("संशय के साथ होने वाल{E}"), "N")
_mod("uddhaccasahagate", _e("बेचैनी के साथ होने वाल{E}"), "A")
_mod("uddhaccasahagato", _e("बेचैनी के साथ होने वाल{E}"), "N")
LEX["vicikicchaṃ"] = ("N", "vicikiccha", "A", "sg", False)
NH["cakkhuvinnana_n"] = (S.VINNANA("cakkhu"), "", S.VINNANA("cakkhu"), "", "f")
LEX["cakkhuviññāṇaṃ"] = ("N", "cakkhuvinnana_n", "NA", "sg", False)
NH["chandaraga_sa"] = ("अपनी वस्तुओं के प्रति चाह-राग", "", "अपनी वस्तुओं के प्रति चाह-राग", "", "m")
NH["chandaraga_pa"] = ("पराई वस्तुओं के प्रति चाह-राग", "", "पराई वस्तुओं के प्रति चाह-राग", "", "m")
NH["chandaraga_sp"] = ("अपनी अधिकृत चीज़ों के प्रति चाह-राग", "", "अपनी अधिकृत चीज़ों के प्रति चाह-राग", "", "m")
NH["chandaraga_pp"] = ("दूसरों की अधिकृत चीज़ों के प्रति चाह-राग", "", "दूसरों की अधिकृत चीज़ों के प्रति चाह-राग",
                       "", "m")
LEX["sakabhaṇḍe chandarāgo"] = ("N", "chandaraga_sa", "N", "sg", False)
LEX["parabhaṇḍe chandarāgassa"] = ("N", "chandaraga_pa", "G", "sg", False)
LEX["sakapariggahe chandarāgo"] = ("N", "chandaraga_sp", "N", "sg", False)
LEX["parapariggahe chandarāgassa"] = ("N", "chandaraga_pp", "G", "sg", False)
NH["indr_cakkhu"] = (S.INDRIYA_SENSE("cakkhu"), "", S.INDRIYA_SENSE("cakkhu"), "", "f")
NH["indr_kaya"] = (S.INDRIYA_SENSE("kāya"), "", S.INDRIYA_SENSE("kāya"), "", "f")
for _w, _nid in (("cakkhundriyaṃ", "indr_cakkhu"), ("kāyindriyaṃ", "indr_kaya")):
    LEX[_w] = ("N", _nid, "NA", "sg", False)
    LEX[_w[:-1] + "ñca"] = ("N", _nid, "NA", "sg", True)
LEX["vuṭṭhahitvā"] = ("DEP", "से उठकर")
LEX["upanissāya"] = ("DEP", "के प्रबल आश्रय से")
LEX_MAXW = max(len(k.split()) for k in LEX)


def _verb(pl, g, stem=""):
    v = ("होती हैं" if pl else "होती है") if g == "f" else ("होते हैं" if pl else "होता है")
    return (stem + " " + v).strip()


class Member:
    def __init__(self):
        self.mods = []      # (forms, pre)
        self.num = None     # (hindi, number)
        self.noun = None    # (nid, num)
        self.ca = False
        self.sep = None
        self.case = None
        self.items = None   # Item slot used as modifier

    def gnum(self):
        nid, num = self.noun
        if self.num:
            num = self.num[1]
        if self.items and len(self.items.keys) > 1 and nid == "dhamma" and num == "pl":
            num = "pl"
        return NH[nid][4], num

    def render(self, obl):
        nid, num = self.noun
        if self.num:
            num = self.num[1]
        hs = NH[nid]
        g = hs[4]
        noun = hs[(2 if obl else 0) + (1 if num == "pl" else 0)]
        agr = "f" if g == "f" else ("m" if (num == "sg" and not obl) else "mo")
        if len(hs) > 5:
            agr = hs[5]
        pre = []
        post = []
        if self.items is not None and nid == "dhamma" and num == "sg" and len(self.items.keys) > 1:
            return join([f"{adj(k, 'f')} {noun}" for k in self.items.keys])
        for forms, p in self.mods:
            if forms == "@ITEM":
                pre.append(self.items.form(agr))
                continue
            txt = forms if isinstance(forms, str) else forms[agr]
            (pre if p else post).append(txt)
        parts = [", ".join(pre)] if pre else []
        if self.num:
            parts.append(self.num[0])
        parts += post
        parts.append(noun)
        return " ".join(p for p in parts if p)


def _cls(case):
    return {"N": "N", "A": "A", "NA": "X", "G": "G", "I": "I", "B": "B"}[case]


def _compatible(a, b):
    return a == b or (a == "X" and b in ("N", "A")) or (b == "X" and a in ("N", "A"))


SEP_TOKENS = {"…pe…": "…", "…": "…", ",": ","}


def _tokens(key, slots):
    key = key.replace("…pe…", " …pe… ").replace("…", " … ").replace(" … pe … ", " …pe… ")
    key = re.sub(r",(\s|$)", r" , ", key)
    words = key.split()
    toks = []
    i = 0
    si = 0
    while i < len(words):
        w = words[i]
        if w in ("…pe…", "…"):
            toks.append(("SEP", "…"))
            i += 1
            continue
        if w == ",":
            toks.append(("SEP", ","))
            i += 1
            continue
        if w.startswith("@"):
            sl = slots[si]
            if sl.case == "ādhipati":          # pītisahagatādhipati
                toks.append(("ITEM", Item(sl.keys, "ā")))
                toks.append(("N", "adhipati", "N", "sg", False))
            else:
                toks.append(("ITEM", sl))
            si += 1
            i += 1
            continue
        if w.startswith("%"):
            toks.append(("COND", slots[si]))
            si += 1
            i += 1
            continue
        for n in range(min(LEX_MAXW, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            if cand in LEX:
                toks.append(LEX[cand])
                i += n
                break
        else:
            return None
    # Hindi order: an instrumental "X मन से" goes before the object of the verb that follows it
    k = 0
    while k < len(toks) - 2:
        if (toks[k][0] == "ITEM" and toks[k][1].case == "ena" and toks[k + 1][0] == "N"
                and toks[k + 1][2] == "I" and toks[k + 2][0] == "VP"):
            j = k
            while j > 0 and toks[j - 1][0] in ("N", "NUM", "MOD", "ITEM", "SEP") and not (
                    toks[j - 1][0] == "N" and toks[j - 1][2] in ("I", "B")):
                j -= 1
            if j < k:
                toks[j:k + 2] = toks[k:k + 2] + toks[j:k]
        k += 1
    return toks


def np_engine(key, slots):
    toks = _tokens(key, slots)
    if toks is None:
        return None
    # Hindi order: "... मूल-कारण से उत्पन्न होती है" (condition before the verb)
    for k in range(len(toks) - 1):
        if toks[k][0] == "VERB" and toks[k + 1][0] == "COND" and toks[k + 1][1].kind in ("A", "N"):
            toks[k], toks[k + 1] = ("PRECOND", toks[k + 1][1]), toks[k]
    out = []
    pending = []
    after_dat = [False]
    buf = []          # members of the open noun phrase
    cur = Member()
    subject = []      # members of the first direct noun phrase

    def emit(txt):
        out.append(txt)

    def attach(txt):          # attach punctuation to the previous output
        if out:
            out[-1] = out[-1] + txt
        else:
            out.append(txt)

    def close_member():
        nonlocal cur, buf
        if cur.noun is not None:
            if buf and not _compatible(buf_cls(), _cls(cur.case)):
                m = cur
                cur = Member()
                auto_flush()
                cur = m
            buf.append(cur)
        elif cur.mods or cur.num or cur.items:
            raise _Fail()
        cur = Member()

    def buf_cls():
        c = None
        for m in buf:
            k = _cls(m.case)
            if c is None or c == "X":
                c = k
        return c

    def render_list(members, obl, post, each):
        """members joined; 'each' = text after every member (के लिए); post = postposition repeated
        after each separator-closed segment (को/का/पर in chains)."""
        segs, curseg = [], []
        for m in members:
            curseg.append(m)
            if m.sep:
                segs.append((curseg, m.sep))
                curseg = []
        if curseg:
            segs.append((curseg, None))
        parts = []
        for seg, sep in segs:
            jn = join if any(x.ca for x in seg) else (lambda xs: ", ".join(xs))
            txt = jn([x.render(obl) + each for x in seg])
            if sep:
                txt += (" " + post if post and sep == "…" else "") + sep
            parts.append(txt)
        return " ".join(parts)

    def flush(ctx, post=""):
        nonlocal buf
        close_member()
        if not buf:
            return False
        if ctx == "dat":
            txt = render_list(buf, True, "", " के लिए")
            after_dat[0] = True
        elif ctx in ("obl", "ins", "abl"):
            txt = render_list(buf, True, post, "")
            if buf[-1].sep:
                emit(txt)
                buf = []
                return True
            if ctx == "ins":
                txt += " से"
        elif ctx == "objdir":
            txt = render_list(buf, False, "", "")
        else:
            txt = render_list(buf, False, "", "")
            if after_dat[0] or (subject and subject[-1].sep):
                subject.clear()
                after_dat[0] = False
            if not subject:
                subject.extend(buf)
                if buf[-1].noun[0] == "dhamma" and not buf[-1].sep:
                    txt += ","      # "X परिघटना, Y परिघटना के लिए …" (pañhā frame)
        emit(txt)
        buf = []
        return True

    def auto_flush():
        if cur.noun is not None:
            close_member()
        c = buf_cls()
        flush("dat" if c == "G" else ("ins" if c == "I" else ("abl" if c == "B" else "dir")))

    def agree(members):
        if not members:
            return None
        if any(m.sep == "…" for m in members):     # "rāgo… doso… patthanā": agree with the last one
            members = members[-1:]
        pl = len(members) > 1 or members[0].gnum()[1] == "pl"
        g = "f" if all(m.gnum()[0] == "f" for m in members) else "m"
        return pl, g

    def fix_dhamma_comma():
        # a comma after a dhamma subject is only wanted before a dative list
        if out and out[-1].endswith(",") and subject and subject[-1].noun[0] == "dhamma":
            out[-1] = out[-1][:-1]

    try:
        for t in toks:
            kind = t[0]
            if kind in ("N", "NUM", "MOD", "ITEM"):
                if kind == "N":
                    case = t[2]
                elif kind == "NUM":
                    case = t[3]
                elif kind == "MOD":
                    case = t[2]
                else:
                    case = {"aṃ": "NA", "o": "N", "ā": "N", "e": "A", "assa": "G", "ānaṃ": "G", "āya": "G",
                            "ena": "I", "āni": "NA"}.get(t[1].case)
                    if case is None:
                        return None
                if cur.noun is not None:
                    close_member()
                if not cur.mods and not cur.num and not cur.items and buf:
                    c = buf_cls()
                    k = _cls(case)
                    if not _compatible(c, k):
                        if c != "G" and out and out[-1].endswith(",") is False and k == "G":
                            pass
                        auto_flush()
                if kind == "N":
                    cur.noun = (t[1], t[3])
                    cur.ca = t[4]
                    if cur.case is None or case != "NA" or t[1].startswith("pk_"):
                        cur.case = case
                elif kind == "NUM":
                    cur.num = (t[1], t[2])
                    cur.case = cur.case or case
                elif kind == "MOD":
                    cur.mods.append((t[1], t[3]))
                    cur.case = cur.case or case
                else:
                    cur.items = t[1]
                    cur.mods.append(("@ITEM", True))   # keeps the Pāli order of modifiers
                    cur.case = cur.case or case
            elif kind == "SEP":
                if cur.noun is not None:
                    cur.sep = t[1]
                    close_member()
                elif cur.mods and not cur.num and not cur.items:
                    # bare modifiers in a chain: "bāhiraṃ… āhārasamuṭṭhānaṃ…"
                    mm = cur
                    cur = Member()
                    auto_flush()
                    emit(" ".join(f if isinstance(f, str) else f["m"] for f, _ in mm.mods))
                    attach(t[1])
                elif cur.mods or cur.num or cur.items:
                    return None
                elif buf:
                    buf[-1].sep = t[1]
                else:
                    attach(t[1])
            elif kind == "PRECOND":
                close_member()
                pending.append(t[1].form())
            elif kind == "DEP":
                close_member()
                last = max((i for i, m in enumerate(buf) if m.sep), default=-1)
                if last >= 0 and t[1] != "के प्रबल आश्रय से":          # "dve khandhe…pe… vatthuṃ paccayā": the chain part stays apart
                    rest = buf[last + 1:]
                    buf = buf[:last + 1]
                    flush("dir")
                    buf = rest
                flush("obl")
                emit(t[1])
            elif kind in ("ADV", "LIT"):
                auto_flush()
                if out and out[-1].endswith(",") and kind == "LIT":
                    pass
                emit(t[1])
            elif kind == "VERB":
                close_member()
                members = list(buf)
                flush("dir")
                fix_dhamma_comma()
                pl, g = agree(members) or (False, "f")
                out.extend(pending)
                pending.clear()
                emit(_verb(pl, g, "उत्पन्न"))
            elif kind == "VP":
                post, fn = t[1], t[2]
                close_member()
                objpl = bool(buf) and (len(buf) > 1 or buf[-1].gnum()[1] == "pl")
                had = bool(buf)
                if had and not post:
                    flush("objdir")
                elif had:
                    last_sep = buf[-1].sep
                    flush("obl", post)
                    if not last_sep and post:
                        attach(" " + post)
                emit(fn(objpl))
            elif kind == "COND":
                c = t[1]
                close_member()
                if c.kind == "I":
                    if buf and buf_cls() == "G":
                        flush("dat")
                    elif buf:
                        flush("dir")
                        fix_dhamma_comma()
                    a = agree(subject)
                    v = _verb(*a) if a else STATE["verb"]
                    STATE["verb"] = v
                    emit(f"{c.form()} {v}")
                    subject.clear()
                elif c.kind in ("A", "N"):
                    if buf and buf[-1].sep:
                        auto_flush()
                    if buf:
                        k = 1
                        if buf[0].ca:
                            while k < len(buf) and buf[k].ca:
                                k += 1
                        if k >= len(buf):
                            k = 0
                        if k:
                            obj = buf[k:]
                            buf = buf[:k]
                            flush("dir")
                            buf = obj
                        flush("obl")
                        attach(" पर")
                    emit(c.form())
                else:
                    return None
            else:
                return None
        auto_flush()
        fix_dhamma_comma()
        out.extend(pending)
    except _Fail:
        return None
    if subject:
        a = agree(subject)
        STATE["verb"] = _verb(*a)
    res = " ".join(out)
    res = res.replace(" …", "…").replace(" ,", ",")
    res = re.sub(r"(^|\s)(उस|उन) का ", r"\1\2का ", res)
    res = re.sub(r"(^|\s)उस को ", r"\1उसे ", res)
    res = re.sub(r"(^|\s)उन को ", r"\1उन्हें ", res)
    return res


class _Fail(Exception):
    pass


# =====================================================================================
# Line translation
# =====================================================================================
PIECE_DELIM = re.compile(r"(…pe…|…|, )")
SENT_DELIM = re.compile(r"( – |\. |; |\.$)")


def tr_sentence(sent):
    """Translate one sentence (no ' – ' / '. ' inside). Greedy longest span of pieces."""
    if not sent.strip():
        return sent
    h = lookup(sent)
    if h is not None:
        return h
    parts = PIECE_DELIM.split(sent)
    pieces = parts[0::2]
    delims = parts[1::2] + [""]
    out = []
    i = 0
    n = len(pieces)
    while i < n:
        done = False
        for j in range(n, i, -1):
            span = "".join(pieces[k] + (delims[k] if k < j - 1 else "") for k in range(i, j))
            if j - i > 1 or True:
                if not span.strip():
                    h = span
                else:
                    h = lookup(span)
            if h is not None:
                lead = span[: len(span) - len(span.lstrip())]
                trail = span[len(span.rstrip()):]
                out.append(lead + h.strip() + trail)
                out.append(DELIM_HI[delims[j - 1]])
                i = j
                done = True
                break
        if not done:
            key, _ = normalize(pieces[i].strip())
            UNMATCHED[key] += 1
            UNM_EX.setdefault(key, pieces[i])
            out.append("⟪" + pieces[i] + "⟫")
            out.append(DELIM_HI[delims[i]])
            i += 1
    return "".join(out)


DELIM_HI = {"…pe…": "…", "…": "…", ", ": ", ", "": "", " – ": " – ", ". ": "। ", "; ": "; ", ".": "।"}


def tr_text(text):
    """Text without parentheses."""
    parts = SENT_DELIM.split(text)
    out = []
    for k, p in enumerate(parts):
        if k % 2 == 1:
            out.append(DELIM_HI[p])
        else:
            lead = p[: len(p) - len(p.lstrip())]
            trail = p[len(p.rstrip()):]
            out.append(lead + tr_sentence(p.strip()) + trail if p.strip() else p)
    return "".join(out)


PAREN_RX = re.compile(r"\(([^()]*)\)|\{([^{}]*)\}")


def variant(inner):
    m = re.match(r"^(.*) \(([^)]*)\)$", inner.strip())
    word, sig = m.group(1), m.group(2)
    sig = ", ".join(s.strip().capitalize() + "." for s in sig.split(".") if s.strip())
    kind = TP.VARIANT_KIND.get(word, "पाठभेद")
    return f"[{kind} ({sig}): {word}]"


def tr_line(text):
    text = text.replace("rāgassa.. ", "rāgassa… ")   # source slip ".." for "…" (2-03)
    # whole-line templates first (lets a line be matched as one unit)
    key0, _ = normalize(text.strip())
    if key0 in TPL:
        return lookup(text)
    out = []
    pos = 0
    for m in PAREN_RX.finditer(text):
        out.append(tr_text(text[pos:m.start()]) if text[pos:m.start()].strip() else text[pos:m.start()])
        if m.group(2) is not None:
            out.append(variant(m.group(2)))
        else:
            inner = m.group(1)
            if re.fullmatch(r"\d+", inner):
                out.append(f"({inner})")
            else:
                h = None
                if inner.endswith(".") and not inner.endswith("…."):
                    h = lookup(inner[:-1])
                    if h is not None:
                        h += "।"
                if h is None:
                    h = lookup(inner)
                out.append("(" + (h if h is not None else tr_text(inner)) + ")")
        pos = m.end()
    if pos < len(text):
        out.append(tr_text(text[pos:]))
    res = "".join(out)
    return res


# =====================================================================================
# Counting lines
# =====================================================================================
_NUMS = dict(S.NUM)
_NUMS.update({"soḷasa": "सोलह", "tiṃsa": "तीस", "ekavīsa": "इक्कीस", "bāvīsa": "बाईस", "tevīsa": "तेईस",
              "pañcavīsa": "पच्चीस", "aṭṭhavīsa": "अट्ठाईस", "tettiṃsa": "तैंतीस", "sattatiṃsa": "सैंतीस",
              "chabbīsa": "छब्बीस", "sattavīsa": "सत्ताईस", "catuvīsa": "चौबीस", "ekūnavīsa": "उन्नीस",
              "ekatiṃsa": "इकतीस", "dvattiṃsa": "बत्तीस", "catuttiṃsa": "चौंतीस", "pañcatiṃsa": "पैंतीस",
              "chattiṃsa": "छत्तीस", "ekūnatiṃsa": "उनतीस", "aṭṭhatiṃsa": "अड़तीस", "ekūnacattālīsa": "उनतालीस", "cattālīsa": "चालीस"})
_COUNT_EXTRA = {"sabbattha": "हर जगह", "sabbe": "सभी में"}


def is_count_line(text):
    t = re.sub(r"\([^)]*\)", "", text)
    toks = re.findall(r"[^\s,;.…]+", t.replace("…pe…", " "))
    if not toks:
        return False
    for tok in toks:
        low = tok[0].lower() + tok[1:]
        kind, _ = S._classify(low)
        if kind == "other" and low not in _COUNT_EXTRA and low not in _NUMS:
            return False
    return True


def count_line(text):
    """Like S.count_hi plus 'sabbattha'/'sabbe' and parenthesised notes."""
    out = ""
    pos = 0
    pieces = []
    for m in re.finditer(r"\(([^()]*)\)", text):
        pieces.append(("t", text[pos:m.start()]))
        pieces.append(("p", m.group(1)))
        pos = m.end()
    pieces.append(("t", text[pos:]))
    res = []
    for kind, val in pieces:
        if kind == "p":
            h = lookup(val)
            if h is None:
                key, _ = normalize(val)
                UNMATCHED[key] += 1
                UNM_EX.setdefault(key, val)
                h = "⟪" + val + "⟫"
            res.append("(" + h + ")")
        elif val.strip():
            res.append(_count_core(val))
        else:
            res.append(val)
    return "".join(res).replace("  ", " ")


def _count_core(pali):
    lead = pali[: len(pali) - len(pali.lstrip())]
    trail_sp = pali[len(pali.rstrip()):]
    toks = re.findall(r"…pe…|…|[,;.]|na [^\s,;.…]+|[^\s,;.…]+", pali)
    items = []
    for t in toks:
        if t in ("…pe…", "…"):
            items.append(("ell", "…"))
        elif t in ",;.":
            items.append(("punct", t))
        else:
            low = t[0].lower() + t[1:]
            if low in _COUNT_EXTRA:
                items.append(("extra", _COUNT_EXTRA[low]))
                continue
            if low in _NUMS:
                items.append(("num", _NUMS[low]))
                continue
            kind, v = S._classify(low.replace(" ", ""))
            if kind == "other":
                raise ValueError(f"unknown word in count line: {t!r}")
            items.append((kind, v))
    words = ("abl", "neg_abl", "loc", "neg_loc", "num", "extra")
    out = ""
    for i, (kind, v) in enumerate(items):
        nxt = items[i + 1][0] if i + 1 < len(items) else None
        if kind in words:
            if kind in ("abl", "neg_abl", "loc", "neg_loc"):
                text = {"abl": S.ABL, "neg_abl": S.NABL, "loc": S.LOC, "neg_loc": S.NLOC}[kind](v)
            else:
                text = v
            if kind in ("abl", "neg_abl", "num") and nxt in ("abl", "neg_abl", "loc", "neg_loc", "num", "extra"):
                text += ","
            if out and not out.endswith(" "):
                out += " "
            out += text
        else:
            out = out.rstrip(" ").rstrip(",") + ("…" if kind == "ell" else ("।" if v == "." else v))
    return lead + out.strip() + trail_sp


# =====================================================================================
# Headings
# =====================================================================================
HEAD_RX = re.compile(r"^(#+) (\*?)(.*?)(\*?)$")


def tr_heading(line):
    m = HEAD_RX.match(line)
    hashes, st, body, en = m.groups()
    if body not in TP.HEADINGS:
        UNMATCHED["HEADING: " + body] += 1
        return f"{hashes} {st}⟪{body}⟫{en}"
    return f"{hashes} {st}{TP.HEADINGS[body]}{en}"


# =====================================================================================
# Build
# =====================================================================================
def build(fname):
    src = (S.PALI_DIR / fname).read_text(encoding="utf-8")
    H = []
    for line in src.splitlines():
        if not line.strip():
            continue
        body = S.ID_RX.sub("", line)
        STATE["verb"] = "होती है"
        if body.startswith("#"):
            H.append(tr_heading(body))
        elif is_count_line(body):
            H.append(count_line(body))
        else:
            H.append(tr_line(body))
    return S.assemble(src, H)


def main():
    outs = {f: build(f) for f in FILES}
    if "--show" in sys.argv:
        f, a, b = sys.argv[sys.argv.index("--show") + 1: sys.argv.index("--show") + 4]
        hl = [l for l in outs[f].splitlines() if l.strip()]
        pl = [l for l in (S.PALI_DIR / f).read_text(encoding="utf-8").splitlines() if l.strip()]
        for i in range(int(a) - 1, min(int(b), len(hl))):
            if "--unm" in sys.argv and "⟪" not in hl[i]:
                continue
            if "--pali" in sys.argv:
                print(f"P{i + 1}: {pl[i]}")
            print(f"H{i + 1}: {hl[i]}")
        return
    if UNMATCHED:
        print(f"UNMATCHED: {len(UNMATCHED)} distinct, {sum(UNMATCHED.values())} total")
        lim = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 80
        for k, v in UNMATCHED.most_common(lim):
            print(f"{v}\t{k}")
        if "--dry" in sys.argv:
            return
        sys.exit("unmatched clauses left: nothing written")
    if "--dry" in sys.argv:
        print("all matched")
        return
    for f, text in outs.items():
        S._write(S.HI_DIR / f, text)
        print("wrote", f)
    pairs = [(S.PALI_DIR / f, S.HI_DIR / f) for f in FILES]
    sys.exit(1 if S.check(pairs) else 0)


if __name__ == "__main__":
    main()
