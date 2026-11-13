"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 1-01-kusalattika.md (the whole wholesome triad).

Imports the approved sample builder read-only (its constants are reused verbatim) and extends its tables with the
frames of the later sections (sahajāta / paccaya / nissaya / saṃsaṭṭha / sampayutta, pañhāvāra, ghaṭanā, counts).
Run:  python -I -B -X utf8 build_rails_1-01.py
The output's non-empty lines 1-190 and 1235-1262 are checked against sample-1 byte for byte.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_rails_sample as S  # noqa: E402  (read-only)

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters", "1-01-kusalattika.md")
DST = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters", "1-01-kusalattika.md")

NAME, ABL, NABL, NNAME, LOC, NLOC = S.NAME, S.ABL, S.NABL, S.NNAME, S.LOC, S.NLOC
KEYS = S.KEYS
NEGP = {k: ("no" if k in ("atthi", "natthi", "vigata", "avigata") else "na") for k in KEYS}


def andjoin(items):
    items = list(items)
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " और " + items[-1]


# ================================================================ numbers and counting words

NUM = dict(S.NUM)
NUM.update({"dasa": "दस", "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह", "cuddasa": "चौदह",
            "pannarasa": "पंद्रह", "soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह"})
CNT = {"Dukaṃ": "दो", "Tikaṃ": "तीन", "Catukkaṃ": "चार", "Pañcakaṃ": "पाँच", "Chakkaṃ": "छह", "Sattakaṃ": "सात",
       "Aṭṭhakaṃ": "आठ", "Navakaṃ": "नौ", "Dasakaṃ": "दस", "Ekādasakaṃ": "ग्यारह", "Dvādasakaṃ": "बारह",
       "Terasakaṃ": "तेरह", "Cuddasakaṃ": "चौदह", "Pannarasakaṃ": "पंद्रह", "Soḷasakaṃ": "सोलह",
       "Sattarasakaṃ": "सत्रह", "Aṭṭhārasakaṃ": "अठारह", "Vīsakaṃ": "बीस", "Ekavīsakaṃ": "इक्कीस",
       "Bāvīsakaṃ": "बाईस", "Tevīsakaṃ": "तेईस", "Catuvīsakaṃ": "चौबीस"}
SAHITA = {"sāsevanaṃ": "पुनरावृत्ति-कारण सहित", "savipākaṃ": "कर्म-फल-कारण सहित", "sāhāraṃ": "आहार-कारण सहित",
          "saindriyaṃ": "क्षमता-कारण सहित", "saupanissayaṃ": "प्रबल आश्रय-कारण सहित", "sakammaṃ": "कर्म-कारण सहित"}

NMULAKA = {k: NNAME[k][: -len(" का अभाव")] + " के अभाव से शुरू होने वाली शृंखला" for k in KEYS}
NDUKA = {k: NNAME[k][: -len(" का अभाव")] + " के अभाव के साथ दो कारणों का मेल" for k in KEYS}
NSADISA = S.NSADISA
SADISA = S.SADISA
MULAKA = S.MULAKA


def nbase(k):
    """«X-कारण के अभाव» (oblique of «X-कारण का अभाव»)."""
    return NAME[k] + " के अभाव"


# ================================================================ headings

HEAD = dict(S.HEAD)
for _c, _n in CNT.items():
    HEAD.setdefault(_c, f"{_n} कारणों का मेल")
for _k in KEYS:
    _neg = NEGP[_k] + _k
    HEAD[_neg[0].upper() + _neg[1:] + "dukaṃ"] = NDUKA[_k]
    HEAD[_k[0].upper() + _k[1:] + "sabhāgaṃ"] = NAME[_k] + " के साथी कारण"
HEAD.update({
    "Sahajātavāro": "सह-उत्पत्ति का खंड",
    "Paccayavāro": "कारण का खंड",
    "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड",
    "Sampayuttavāro": "जुड़ाव का खंड",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Anulomaṃ": "सकारात्मक क्रम",
    "Paccanīyaṃ": "नकारात्मक क्रम",
    "Namaggatikaṃ": NAME["magga"] + " के अभाव के साथ तीन कारणों का मेल",
    "Naadhipatyādi": NNAME["adhipati"] + " आदि",
    "Tikādi": "तीन कारणों का मेल आदि",
    "Chakkādi": "छह कारणों का मेल आदि",
    "Ārammaṇādipaccayā": NAME["ārammaṇa"] + " आदि",
    "Āhārādipaccayā": NAME["āhāra"] + " आदि",
    "Atthiādipaccayā": NAME["atthi"] + " आदि",
    "Atthipaccayādi": NAME["atthi"] + " आदि",
    "Naanantarādipaccayā": NNAME["anantara"] + " आदि",
    "Napacchājātādipaccayā": NNAME["pacchājāta"] + " आदि",
    "Naāhārādipaccayā": NNAME["āhāra"] + " आदि",
    "Nasampayuttādipaccayā": NNAME["sampayutta"] + " आदि",
    "Naadhipatiādipaccayā": NNAME["adhipati"] + " आदि",
    "Kamma-vipākadukāni": f"{NAME['kamma']} और {NAME['vipāka']} के साथ दो कारणों के मेल",
    "Ārammaṇādidukāni": S.HEAD["Ārammaṇādidukāni"],
    "Sahajātādidukāni": NAME["sahajāta"] + " आदि के साथ दो कारणों के मेल",
    "Anantarādidukāni": NAME["anantara"] + " आदि के साथ दो कारणों के मेल",
    "Atthiādidukādi": NAME["atthi"] + " आदि के साथ दो कारणों के मेल आदि",
    "Naanantarādidukāni": nbase("anantara") + " आदि के साथ दो कारणों के मेल",
    "Naāhārādidukāni": nbase("āhāra") + " आदि के साथ दो कारणों के मेल",
    "Anantara-samanantaradukāni": f"{NAME['anantara']} और {NAME['samanantara']} के साथ दो कारणों के मेल",
    "Nissaya-upanissayadukāni": f"{NAME['nissaya']} और {NAME['upanissaya']} के साथ दो कारणों के मेल",
    "Natthi-vigatadukāni": f"{NAME['natthi']} और {NAME['vigata']} के साथ दो कारणों के मेल",
    "Napacchājāta-naāsevanadukāni": f"{nbase('pacchājāta')} और {nbase('āsevana')} के साथ दो कारणों के मेल",
    "Nonatthi-novigatadukāni": f"{nbase('natthi')} और {nbase('vigata')} के साथ दो कारणों के मेल",
    "Naanantara-nasamanantaradukāni": f"{nbase('anantara')} और {nbase('samanantara')} के साथ दो कारणों के मेल",
    "Paccayapaccanīyānulomaṃ": S.HEAD["Paccayapaccanīyānulomaṃ"],
})

# ghaṭanā headings: [X][kind]ghaṭanā, kind = sāmañña / missaka / pakiṇṇaka, or sa-Y(-Z) «… सहित संयोजन»
GH_HEAD_STEM = {"hetu": "hetu", "ārammaṇa": "ārammaṇa", "adhipati": "adhipati", "anantara": "anantara",
                "samanantara": "samanantara", "sahajāta": "sahajāta", "aññamañña": "aññamañña",
                "nissaya": "nissaya", "upanissaya": "upanissaya", "purejāta": "purejāta",
                "pacchājāta": "pacchājāta", "āsevana": "āsevana", "kamma": "kamma", "vipāka": "vipāka",
                "āhāra": "āhāra", "indriya": "indriya", "jhāna": "jhāna", "magga": "magga",
                "sampayutta": "sampayutta", "vippayutta": "vippayutta", "atthi": "atthi", "natthi": "natthi",
                "vigata": "vigata", "avigata": "avigata"}
GH_SA = {"saindriya": ["indriya"], "sādhipati": ["adhipati"], "sakamma": ["kamma"], "samagga": ["magga"],
         "sajhāna": ["jhāna"], "sāhāra": ["āhāra"], "sahetu": ["hetu"], "sahetādhipati": ["hetu", "adhipati"]}
ADHIPATI_GH = {"cittādhipati": "प्रधान बने हुए मन", "vīriyādhipati": "प्रधान बने हुए उत्साह",
               "vīmaṃsādhipati": "प्रधान बनी हुई जाँच-परख", "chandādhipati": "प्रधान बनी हुई चाह"}


def gh_heading(body):
    m = re.fullmatch(r"(.*?)ghaṭanā(?: \((\d+)\))?", body)
    if not m:
        return None
    stem, num = m.group(1).lower(), m.group(2)
    tail = f" ({num})" if num else ""
    if stem in ("", "sāmañña"):
        return ("सामान्य संयोजन" if stem else "संयोजन") + tail
    if stem == "pakiṇṇaka":
        return "फुटकर संयोजन" + tail
    if stem.startswith("sahajāta") and stem[len("sahajāta"):].lstrip("-") in ADHIPATI_GH:
        return f"सह-उत्पत्ति रूपी {ADHIPATI_GH[stem[len('sahajāta'):].lstrip('-')]} के संयोजन" + tail
    if stem in ADHIPATI_GH:
        return f"{ADHIPATI_GH[stem]} के संयोजन" + tail
    for kind, h in (("sāmañña", "सामान्य संयोजन"), ("missaka", "मिश्रित संयोजन"), ("pakiṇṇaka", "फुटकर संयोजन")):
        if stem.endswith(kind):
            base = stem[: -len(kind)].rstrip("-")
            if base in GH_HEAD_STEM:
                return f"{NAME[base]} के {h}" + tail
    if stem in GH_HEAD_STEM:
        return f"{NAME[stem]} के संयोजन" + tail
    # sa-forms: Saindriya-magga, Sādhipati-indriya-magga, Sahetu-adhipati-magga, Sahetādhipati-indriya …
    parts = stem.split("-")
    conds = []
    first = parts[0]
    if first in GH_SA:
        conds += GH_SA[first]
    elif first.startswith("saindriya"):
        conds += ["indriya"]
        parts.insert(1, first[len("saindriya"):])
    else:
        raise KeyError(f"ghaṭanā heading: {body!r}")
    for p in parts[1:]:
        if not p:
            continue
        if p not in GH_HEAD_STEM:
            raise KeyError(f"ghaṭanā heading member: {p!r} in {body!r}")
        conds.append(p)
    return andjoin(NAME[c] for c in conds) + " सहित संयोजन" + tail


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)(\(\d+\.?\) )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    if body in HEAD:
        h = HEAD[body]
    else:
        m2 = re.fullmatch(r"(.*?) \(([^()]+)\)", body)
        if m2 and m2.group(1) in HEAD and m2.group(2) in SAHITA:
            h = f"{HEAD[m2.group(1)]} ({SAHITA[m2.group(2)]})"
        else:
            h = gh_heading(body)
            if h is None:
                raise KeyError(f"heading: {body!r}")
    return f"{hashes} {st}{num or ''}{h}{en}"


# ================================================================ frames (paṭicca and the other dependent sections)

ACC, NOM = S.ACC, S.NOM
ARISES = S.ARISES
VFRAME = {"paṭicca": S.PATICCA, "sahajāto": "के साथ जन्म लेकर", "paccayā": "के कारण", "nissāya": "के आश्रय से",
          "saṃsaṭṭho": "से घुल-मिलकर", "sampayutto": "से जुड़कर"}
VBODY = dict(VFRAME)
VBODY.update({"sahajātā": VFRAME["sahajāto"], "sahajātaṃ": VFRAME["sahajāto"], "saṃsaṭṭhā": VFRAME["saṃsaṭṭho"],
              "sampayuttā": VFRAME["sampayutto"]})


def frame(x, v, y, chain):
    yh, n = NOM[y]
    return f"{ACC[x]} {VFRAME[v]} {yh} {S.CH(chain)} {ARISES[n]}"


SUBJ_P = dict(S.SUBJ_P)
SUBJ_P.update({
    "kusalaṃ ekaṃ khandhañca vatthuñca": "एक हितकर समूह और आधार",
    "akusalaṃ ekaṃ khandhañca vatthuñca": "एक हानिकर समूह और आधार",
    "tayo khandhe ca vatthuñca": "तीन समूहों और आधार",
    "dve khandhe ca vatthuñca": "दो समूहों और आधार",
    "kusale khandhe ca vatthuñca": "हितकर समूहों और आधार",
    "akusale khandhe ca vatthuñca": "हानिकर समूहों और आधार",
    "vicikicchāsahagate uddhaccasahagate khandhe ca vatthuñca":
        "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों और आधार",
    "cakkhāyatanaṃ": "आँख के इंद्रिय-क्षेत्र",
    "sotāyatanaṃ": "कान के इंद्रिय-क्षेत्र",
    "ghānāyatanaṃ": "नाक के इंद्रिय-क्षेत्र",
    "jivhāyatanaṃ": "जीभ के इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ": "शरीर के इंद्रिय-क्षेत्र",
    # slip «dve khandha nissāya» (^7-2-334), rendered as meant
    "dve khandha": "दो समूहों",
})
OBJ_P = dict(S.OBJ_P)
OBJ_P.update({
    "cakkhuviññāṇaṃ": "आँख की चेतना",
    "sotaviññāṇaṃ": "कान की चेतना",
    "ghānaviññāṇaṃ": "नाक की चेतना",
    "jivhāviññāṇaṃ": "जीभ की चेतना",
    "kāyaviññāṇaṃ": "शरीर की चेतना",
    "kusalā khandhā": "हितकर समूह",
    "akusalā khandhā": "हानिकर समूह",
    "vipākābyākatā kiriyābyākatā khandhā": "कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह",
    "vipākābyākatā khandhā": "कर्म-फल रूपी नैतिक रूप से अनिर्धारित समूह",
    "kiriyābyākatā khandhā": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह",
    "ahetukā vipākābyākatā kiriyābyākatā khandhā":
        "मूल से रहित, कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह",
    "ahetukavipākābyākatā kiriyābyākatā khandhā":
        "मूल से रहित, कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह",
})
PREFIX = dict(S.PREFIX)

_ALT = lambda d: "|".join(re.escape(k) for k in sorted(d, key=len, reverse=True))  # noqa: E731
ACC_ALT, NOM_ALT = _ALT(ACC), _ALT(NOM)
CHAIN_RE = S.CHAIN_RE
FRAME_RE = re.compile(rf"(?<!\w)({ACC_ALT}) dhammaṃ ({_ALT(VFRAME)}) ({NOM_ALT}) (?:dhammo uppajjati|dhammā uppajjanti) "
                      rf"({CHAIN_RE})")
PCLAUSE_RE = re.compile(rf"^(?:({_ALT(PREFIX)}) )?({_ALT(SUBJ_P)}) ({_ALT(VBODY)})(?: ({_ALT(OBJ_P)}))?$")
PART_FRAME_RE = re.compile(rf"^({ACC_ALT}) dhammaṃ ({_ALT(VFRAME)}) ({NOM_ALT}) (?:dhammo|dhammā)$")
NOM_ONLY_RE = re.compile(rf"^({NOM_ALT}) (?:dhammo|dhammā)$")
NOM_VERB_RE = re.compile(rf"^({NOM_ALT}) (?:dhammo uppajjati|dhammā uppajjanti) ({CHAIN_RE})$")
ACC_ONLY_RE = re.compile(rf"^({ACC_ALT}) dhammaṃ$")
SHORT_RE = S.SHORT_RE

# ================================================================ pañhāvāra subjects and datives

SUBJ = dict(S.SUBJ)
NANA_NOM = {"iddhividhañāṇaṃ": "अलौकिक शक्तियों का ज्ञान", "cetopariyañāṇaṃ": "दूसरों के मन को जानने का ज्ञान",
            "pubbenivāsānussatiñāṇaṃ": "पूर्व जन्मों के अनुस्मरण का ज्ञान",
            "yathākammūpagañāṇaṃ": "प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान"}
ORD = {"paṭham": ("पहला", "पहले"), "dutiy": ("दूसरा", "दूसरे"), "tatiy": ("तीसरा", "तीसरे"),
       "catutth": ("चौथा", "चौथे")}
FALLBACK_LOG = []
AYATANA = {"ākāsānañcāyatana": "अनंत आकाश का क्षेत्र", "viññāṇañcāyatana": "अनंत चेतना का क्षेत्र",
           "ākiñcaññāyatana": "कुछ भी न होने का क्षेत्र", "nevasaññānāsaññāyatana": "न पहचान न अ-पहचान का क्षेत्र"}


def obl(h):
    """oblique of a «… का क्षेत्र» noun phrase: «… के क्षेत्र»."""
    return re.sub(r" का (\S+)$", r" के \1", h)


SUBJ.update({
    # anantara / samanantara / āsevana / natthi / vigata / upanissaya
    "purimā purimā kusalā khandhā": ("पहले-पहले के हितकर समूह", "mp"),
    "purimā purimā akusalā khandhā": ("पहले-पहले के हानिकर समूह", "mp"),
    "purimā purimā vipākābyākatā kiriyābyākatā khandhā":
        ("पहले-पहले के कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह", "mp"),
    # comma after vipākābyākatā in ^7-2-423, as written; no effect on the Hindi
    "purimā purimā vipākābyākatā, kiriyābyākatā khandhā":
        ("पहले-पहले के कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह", "mp"),
    "purimā purimā kiriyābyākatā khandhā": ("पहले-पहले के केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह", "mp"),
    "anulomaṃ": ("अनुरूपता", "fs"),
    "arahato anulomaṃ": ("अर्हत् की अनुरूपता", "fs"),
    "gotrabhu": ("गोत्र-परिवर्तन", "ms"),
    "vodānaṃ": ("शुद्धि", "fs"),
    "maggo": ("मार्ग", "ms"),
    "kusalaṃ": ("हितकर मन", "ms"),
    "akusalaṃ": ("हानिकर मन", "ms"),
    "kiriyaṃ": ("केवल क्रिया रूपी मन", "ms"),
    "bhavaṅgaṃ": ("जीवन-धारा", "fs"),
    "āvajjanā": ("मन को विषय की ओर मोड़ना", "ms"),
    "nevasaññānāsaññāyatanakusalaṃ": ("न पहचान न अ-पहचान के क्षेत्र का हितकर मन", "ms"),
    "nevasaññānāsaññāyatanakiriyaṃ": ("न पहचान न अ-पहचान के क्षेत्र का केवल क्रिया रूपी मन", "ms"),
    # sahajāta / aññamañña / nissaya / sampayutta / vipāka / atthi / avigata
    "kusalo eko khandho": ("एक हितकर समूह", "ms"),
    "akusalo eko khandho": ("एक हानिकर समूह", "ms"),
    "vipākābyākato kiriyābyākato eko khandho":
        ("कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित एक समूह", "ms"),
    "vipākābyākato eko khandho": ("कर्म-फल रूपी नैतिक रूप से अनिर्धारित एक समूह", "ms"),
    "tayo khandhā": ("तीन समूह", "mp"),
    "dve khandhā": ("दो समूह", "mp"),
    "khandhā": ("समूह", "mp"),
    "vatthu": ("आधार", "ms"),
    "ekaṃ mahābhūtaṃ": ("एक महाभूत", "ms"),
    "tayo mahābhūtā": ("तीन महाभूत", "mp"),
    "dve mahābhūtā": ("दो महाभूत", "mp"),
    "bāhiraṃ ekaṃ mahābhūtaṃ": ("एक बाह्य महाभूत", "ms"),
    "āhārasamuṭṭhānaṃ ekaṃ mahābhūtaṃ": ("आहार से उत्पन्न एक महाभूत", "ms"),
    "utusamuṭṭhānaṃ ekaṃ mahābhūtaṃ": ("तापमान से उत्पन्न एक महाभूत", "ms"),
    "asaññasattānaṃ ekaṃ mahābhūtaṃ": ("पहचान-रहित प्राणियों में एक महाभूत", "ms"),
    "kusalā khandhā ca mahābhūtā ca": ("हितकर समूह और महाभूत", "mp"),
    "akusalā khandhā ca mahābhūtā ca": ("हानिकर समूह और महाभूत", "mp"),
    "kusalo eko khandho ca vatthu ca": ("एक हितकर समूह और आधार", "mp"),
    "akusalo eko khandho ca vatthu ca": ("एक हानिकर समूह और आधार", "mp"),
    "tayo khandhā ca vatthu ca": ("तीन समूह और आधार", "mp"),
    "dve khandhā ca vatthu ca": ("दो समूह और आधार", "mp"),
    "vipākābyākatā kiriyābyākatā khandhā": ("कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह", "mp"),
    "vipākābyākatā khandhā": ("कर्म-फल रूपी नैतिक रूप से अनिर्धारित समूह", "mp"),
    "pacchājātā kusalā khandhā": ("बाद में उत्पन्न हितकर समूह", "mp"),
    "pacchājātā akusalā khandhā": ("बाद में उत्पन्न हानिकर समूह", "mp"),
    "pacchājātā vipākābyākatā kiriyābyākatā khandhā":
        ("बाद में उत्पन्न कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूह", "mp"),
    "kusalā khandhā ca kabaḷīkāro āhāro ca": ("हितकर समूह और कौर-कौर खाया जाने वाला भोजन", "mp"),
    "akusalā khandhā ca kabaḷīkāro āhāro ca": ("हानिकर समूह और कौर-कौर खाया जाने वाला भोजन", "mp"),
    "kusalā khandhā ca rūpajīvitindriyañca": ("हितकर समूह और भौतिक जीवन-क्षमता", "mp"),
    "akusalā khandhā ca rūpajīvitindriyañca": ("हानिकर समूह और भौतिक जीवन-क्षमता", "mp"),
    "pacchājātā kusalā khandhā ca rūpajīvitindriyañca": ("बाद में उत्पन्न हितकर समूह और भौतिक जीवन-क्षमता", "mp"),
    # kamma, āhāra, indriya, jhāna, magga
    "kusalā cetanā": ("हितकर इरादा", "ms"),
    "akusalā cetanā": ("हानिकर इरादा", "ms"),
    "vipākābyākatā kiriyābyākatā cetanā": ("कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित इरादा", "ms"),
    "vipākābyākatā cetanā": ("कर्म-फल रूपी नैतिक रूप से अनिर्धारित इरादा", "ms"),
    "kusalā āhārā": ("हितकर आहार", "mp"),
    "akusalā āhārā": ("हानिकर आहार", "mp"),
    "vipākābyākatā kiriyābyākatā āhārā": ("कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित आहार", "mp"),
    "vipākābyākatā āhārā": ("कर्म-फल रूपी नैतिक रूप से अनिर्धारित आहार", "mp"),
    "kusalā indriyā": ("हितकर क्षमताएँ", "fp"),
    "akusalā indriyā": ("हानिकर क्षमताएँ", "fp"),
    "vipākābyākatā kiriyābyākatā indriyā":
        ("कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित क्षमताएँ", "fp"),
    "vipākābyākatā indriyā": ("कर्म-फल रूपी नैतिक रूप से अनिर्धारित क्षमताएँ", "fp"),
    "kusalāni jhānaṅgāni": ("हितकर ध्यान के अंग", "mp"),
    "akusalāni jhānaṅgāni": ("हानिकर ध्यान के अंग", "mp"),
    "vipākābyākatāni kiriyābyākatāni jhānaṅgāni":
        ("कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित ध्यान के अंग", "mp"),
    "vipākābyākatāni jhānaṅgāni": ("कर्म-फल रूपी नैतिक रूप से अनिर्धारित ध्यान के अंग", "mp"),
    "kusalāni maggaṅgāni": ("हितकर मार्ग के अंग", "mp"),
    "akusalāni maggaṅgāni": ("हानिकर मार्ग के अंग", "mp"),
    "vipākābyākatāni kiriyābyākatāni maggaṅgāni":
        ("कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मार्ग के अंग", "mp"),
    "vipākābyākatāni maggaṅgāni": ("कर्म-फल रूपी नैतिक रूप से अनिर्धारित मार्ग के अंग", "mp"),
    # upanissaya
    "saddhā": ("श्रद्धा", "fs"), "sīlaṃ": ("सदाचार", "ms"), "sutaṃ": ("सुना-सीखा ज्ञान", "ms"),
    "cāgo": ("त्याग", "ms"), "paññā": ("प्रज्ञा", "fs"),
    "rāgo": ("राग", "ms"), "doso": ("द्वेष", "ms"), "moho": ("मोह", "ms"), "māno": ("अहंकार", "ms"),
    "diṭṭhi": ("दृष्टि", "fs"), "patthanā": ("कामना", "fs"),
    "kāyikaṃ sukhaṃ": ("शारीरिक सुख", "ms"), "kāyikaṃ dukkhaṃ": ("शारीरिक दुःख", "ms"),
    "utu": ("तापमान", "ms"), "bhojanaṃ": ("भोजन", "ms"), "senāsanaṃ": ("निवास-स्थान", "ms"),
    "phalasamāpatti": ("फल की ध्यान-अवस्था", "fs"),
    "kusalaṃ kammaṃ": ("हितकर कर्म", "ms"), "akusalaṃ kammaṃ": ("हानिकर कर्म", "ms"),
    "pāṇātipāto": ("जीव-हत्या", "fs"), "adinnādānaṃ": ("बिना दिया हुआ लेना", "ms"),
    "kāmesumicchācāro": ("इंद्रिय-सुखों में दुराचार", "ms"), "musāvādo": ("झूठ बोलना", "ms"),
    "pisuṇavācā": ("चुगली", "fs"), "pharusavācā": ("कठोर वचन", "ms"),
    "samphappalāpo": ("व्यर्थ की बकवास", "fs"), "abhijjhā": ("लालच", "ms"), "byāpādo": ("दुर्भावना", "fs"),
    "micchādiṭṭhi": ("ग़लत दृष्टि", "fs"),
    "mātughātikammaṃ": ("माता की हत्या का कर्म", "ms"), "pitughātikammaṃ": ("पिता की हत्या का कर्म", "ms"),
    "arahantaghātikammaṃ": ("अर्हत् की हत्या का कर्म", "ms"),
    "ruhiruppādakammaṃ": ("बुद्ध का खून बहाने का कर्म", "ms"),
    "saṅghabhedakammaṃ": ("संघ में फूट डालने का कर्म", "ms"),
    "niyatamicchādiṭṭhi": ("निश्चित ग़लत दृष्टि", "fs"),
    "dibbacakkhu": ("दिव्य आँख", "fs"), "dibbasotadhātu": ("दिव्य कान का तत्व", "ms"),
    "paṭhamo maggo": ("पहला मार्ग", "ms"), "dutiyo maggo": ("दूसरा मार्ग", "ms"),
    "tatiyo maggo": ("तीसरा मार्ग", "ms"),
    "kabaḷīkāro āhāro": S.SUBJ["kabaḷīkāro āhāro"],
    "kusalo ca abyākato ca dhammā": ("हितकर और नैतिक रूप से अनिर्धारित परिघटनाएँ,", "fp"),
    "akusalo ca abyākato ca dhammā": ("हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ,", "fp"),
})
for _k, _h in NANA_NOM.items():
    SUBJ[_k] = (_h, "ms")
for _o, (_h, _ho) in ORD.items():
    SUBJ[f"{_o}aṃ jhānaṃ"] = (f"{_h} ध्यान", "ms")
    SUBJ[f"{_o}assa jhānassa parikammaṃ"] = (f"{_ho} ध्यान की प्रारंभिक तैयारी", "fs")
    SUBJ[f"{_o}assa maggassa parikammaṃ"] = (f"{_ho} मार्ग की प्रारंभिक तैयारी", "fs")
for _a, _h in AYATANA.items():
    if _a != "nevasaññānāsaññāyatana":
        SUBJ[_a + "ṃ"] = (_h, "ms")
    SUBJ[_a + "ssa parikammaṃ"] = (obl(_h) + " की प्रारंभिक तैयारी", "fs")
SUBJ["dibbassa cakkhussa parikammaṃ"] = ("दिव्य आँख की प्रारंभिक तैयारी", "fs")
SUBJ["dibbāya sotadhātuyā parikammaṃ"] = ("दिव्य कान के तत्व की प्रारंभिक तैयारी", "fs")
for _w in ("iddhividha", "cetopariya", "pubbenivāsānussati", "yathākammūpaga", "anāgataṃsa"):
    SUBJ[_w + "ñāṇassa parikammaṃ"] = (S.NANA[_w + "ñāṇassa"] + " की प्रारंभिक तैयारी", "fs")

DAT = dict(S.DAT)
PATISAMBHIDA = ("अर्थ के विश्लेषणात्मक ज्ञान, परिघटनाओं के विश्लेषणात्मक ज्ञान, भाषा के विश्लेषणात्मक ज्ञान, "
                "सूझ-बूझ के विश्लेषणात्मक ज्ञान और संभव और असंभव को जानने की कुशलता के लिए")
_PS = ("atthappaṭisambhidāya, dhammappaṭisambhidāya, niruttippaṭisambhidāya, paṭibhānappaṭisambhidāya, "
       "ṭhānāṭhānakosallassa")
KAYIKA3 = "शारीरिक सुख, शारीरिक दुःख और फल की ध्यान-अवस्था के लिए"
DAT.update({
    "pacchimānaṃ pacchimānaṃ kusalānaṃ khandhānaṃ": "बाद-बाद के हितकर समूहों के लिए",
    "pacchimānaṃ pacchimānaṃ akusalānaṃ khandhānaṃ": "बाद-बाद के हानिकर समूहों के लिए",
    "pacchimānaṃ pacchimānaṃ vipākābyākatānaṃ kiriyābyākatānaṃ khandhānaṃ":
        "बाद-बाद के कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूहों के लिए",
    "pacchimānaṃ pacchimānaṃ kiriyābyākatānaṃ khandhānaṃ":
        "बाद-बाद के केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूहों के लिए",
    "gotrabhussa": "गोत्र-परिवर्तन के लिए", "vodānassa": "शुद्धि के लिए", "maggassa": "मार्ग के लिए",
    "vuṭṭhānassa": "बाहर आने के लिए", "phalasamāpattiyā": "फल की ध्यान-अवस्था के लिए",
    "sekkhāya phalasamāpattiyā": "सीखने के चरण वाले व्यक्ति की फल की ध्यान-अवस्था के लिए",
    "āvajjanāya": "मन को विषय की ओर मोड़ने के लिए",
    "kusalānaṃ khandhānaṃ": "हितकर समूहों के लिए", "akusalānaṃ khandhānaṃ": "हानिकर समूहों के लिए",
    "vipākābyākatānaṃ kiriyābyākatānaṃ khandhānaṃ":
        "कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूहों के लिए",
    "tiṇṇannaṃ khandhānaṃ": "तीन समूहों के लिए", "ekassa khandhassa": "एक समूह के लिए",
    "dvinnaṃ khandhānaṃ": "दो समूहों के लिए", "vatthussa": "आधार के लिए", "khandhānaṃ": "समूहों के लिए",
    "tiṇṇannaṃ mahābhūtānaṃ": "तीन महाभूतों के लिए", "ekassa mahābhūtassa": "एक महाभूत के लिए",
    "dvinnaṃ mahābhūtānaṃ": "दो महाभूतों के लिए",
    "cittasamuṭṭhānānaṃ rūpānaṃ kaṭattārūpānaṃ upādārūpānaṃ":
        "मन से उत्पन्न भौतिक रूपों, किए गए कर्म से उत्पन्न भौतिक रूपों और व्युत्पन्न भौतिक रूपों के लिए",
    "cittasamuṭṭhānānaṃ rūpānaṃ, kaṭattārūpānaṃ, upādārūpānaṃ":
        "मन से उत्पन्न भौतिक रूपों, किए गए कर्म से उत्पन्न भौतिक रूपों और व्युत्पन्न भौतिक रूपों के लिए",
    "kaṭattārūpānaṃ upādārūpānaṃ": "किए गए कर्म से उत्पन्न भौतिक रूपों और व्युत्पन्न भौतिक रूपों के लिए",
    "kaṭattārūpānaṃ, upādārūpānaṃ": "किए गए कर्म से उत्पन्न भौतिक रूपों और व्युत्पन्न भौतिक रूपों के लिए",
    # comma before cittasamuṭṭhānānañca in ^7-2-427, as written; no effect on the Hindi
    "sampayuttakānaṃ khandhānaṃ, cittasamuṭṭhānānañca rūpānaṃ": S.DAT["sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ"],
    "sotaviññāṇassa": "कान की चेतना के लिए", "ghānaviññāṇassa": "नाक की चेतना के लिए",
    "jivhāviññāṇassa": "जीभ की चेतना के लिए",
    "vipākassa": "कर्म-फल के लिए",
    "sekkhānaṃ " + _PS: "सीखने के चरण वाले व्यक्तियों के " + PATISAMBHIDA,
    "arahato " + _PS: "अर्हत् के " + PATISAMBHIDA,
    "kāyikassa sukhassa": "शारीरिक सुख के लिए", "kāyikassa dukkhassa": "शारीरिक दुःख के लिए",
    "kāyikassa sukhassa, kāyikassa dukkhassa, phalasamāpattiyā": KAYIKA3,
    "saddhāya": "श्रद्धा के लिए", "sīlassa": "सदाचार के लिए", "sutassa": "सुने-सीखे ज्ञान के लिए",
    "cāgassa": "त्याग के लिए", "paññāya": "प्रज्ञा के लिए",
    "rāgassa": "राग के लिए", "dosassa": "द्वेष के लिए", "mohassa": "मोह के लिए", "mānassa": "अहंकार के लिए",
    "diṭṭhiyā": "दृष्टि के लिए", "patthanāya": "कामना के लिए",
    "pāṇātipātassa": "जीव-हत्या के लिए", "adinnādānassa": "बिना दिया हुआ लेने के लिए",
    "kāmesumicchācārassa": "इंद्रिय-सुखों में दुराचार के लिए", "musāvādassa": "झूठ बोलने के लिए",
    "pisuṇāya vācāya": "चुगली के लिए", "pharusāya vācāya": "कठोर वचन के लिए",
    "samphappalāpassa": "व्यर्थ की बकवास के लिए", "abhijjhāya": "लालच के लिए", "byāpādassa": "दुर्भावना के लिए",
    "micchādiṭṭhiyā": "ग़लत दृष्टि के लिए",
    "mātughātikammassa": "माता की हत्या के कर्म के लिए", "pitughātikammassa": "पिता की हत्या के कर्म के लिए",
    "arahantaghātikammassa": "अर्हत् की हत्या के कर्म के लिए",
    "ruhiruppādakammassa": "बुद्ध का खून बहाने के कर्म के लिए",
    "saṅghabhedakammassa": "संघ में फूट डालने के कर्म के लिए",
    "niyatamicchādiṭṭhiyā": "निश्चित ग़लत दृष्टि के लिए",
    "dibbassa cakkhussa": "दिव्य आँख के लिए", "dibbāya sotadhātuyā": "दिव्य कान के तत्व के लिए",
})
for _k in ("iddhividhañāṇassa", "cetopariyañāṇassa", "pubbenivāsānussatiñāṇassa", "yathākammūpagañāṇassa",
           "anāgataṃsañāṇassa"):
    DAT.setdefault(_k, S.NANA[_k] + " के लिए")
for _o, (_h, _ho) in ORD.items():
    DAT[f"{_o}assa jhānassa"] = f"{_ho} ध्यान के लिए"
    DAT[f"{_o}assa maggassa"] = f"{_ho} मार्ग के लिए"
for _a, _h in AYATANA.items():
    DAT[_a + "ssa"] = obl(_h) + " के लिए"
for _base in ("tiṇṇannaṃ khandhānaṃ", "ekassa khandhassa", "dvinnaṃ khandhānaṃ"):
    DAT[_base + " cittasamuṭṭhānānañca rūpānaṃ"] = DAT[_base] + " और मन से उत्पन्न भौतिक रूपों के लिए"
    DAT[_base + " kaṭattā ca rūpānaṃ"] = DAT[_base] + " और किए गए कर्म से उत्पन्न भौतिक रूपों के लिए"
    DAT[_base + " vatthussa ca"] = DAT[_base] + " और आधार के लिए"

INS_ALT = S.INS_ALT
DEF_RE = re.compile(rf"(?<!\w)(?:({_ALT(SUBJ)}) )?(?:({_ALT(DAT)}) )?(?:(kiñci kāle) )?(na )?({INS_ALT})paccayena paccayo")
SUBJ_WORD_RE = re.compile(rf"(?<!\w)({_ALT(SUBJ)})(?!\w)")
PAIR_RE = re.compile(rf"^({_ALT(SUBJ)}) ({_ALT(DAT)})$")
PAIR_UPA_RE = re.compile(rf"^(?:({_ALT(SUBJ)}) )?({_ALT(DAT)}) upanissaya$")

# ================================================================ clauses

CLAUSE = dict(S.CLAUSE)
GERUND = {"paccavekkhati": "पुनः विचार करता है"}
LABEL = {"sahajātaṃ": "सह-उत्पत्ति", "sahajātā": "सह-उत्पत्ति", "sahajāto": "सह-उत्पत्ति",
         "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति", "pacchājātā": "पश्चात्-उत्पत्ति",
         "āhāraṃ": "आहार", "indriyaṃ": "क्षमता", "nānākkhaṇikā": "भिन्न क्षण",
         "ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय",
         "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय", "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति",
         "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति"}
CLAUSE.update(LABEL)
VARE = {"paṭiccavāre": "निर्भरता के खंड में", "paccayavāre": "कारण के खंड में", "nissayavāre": "आश्रय के खंड में",
        "saṃsaṭṭhavāre": "घुले-मिले होने के खंड में"}
METHOD = {"anulomaṃ": "सकारात्मक क्रम", "paccanīyaṃ": "नकारात्मक क्रम", "anulomapaccanīyaṃ": "सकारात्मक-नकारात्मक क्रम",
          "paccanīyānulomaṃ": "नकारात्मक-सकारात्मक क्रम"}
CLAUSE.update(METHOD)
for _v, _vh in VARE.items():
    for _m, _mh in METHOD.items():
        CLAUSE[f"{_v} {_m}"] = f"{_vh} {_mh}"
for _k in KEYS:
    CLAUSE[_k + "mūlakaṃ"] = MULAKA[_k]
    CLAUSE[NEGP[_k] + _k + "mūlakaṃ"] = NMULAKA[_k]
CLAUSE.update({
    "paṭiccavāro": "निर्भरता का खंड", "sahajātavāro": "सह-उत्पत्ति का खंड", "paccayavāro": "कारण का खंड",
    "nissayavāro": "आश्रय का खंड", "saṃsaṭṭhavāro": "घुले-मिले होने का खंड", "sampayuttavāro": "जुड़ाव का खंड",
    "anulomapaccanīyagaṇanā": "सकारात्मक-नकारात्मक क्रम की गणना",
    "pañhāvārassa vibhaṅgo": "प्रश्नों के खंड का विश्लेषण",
    "pañhāvārassa anulomagaṇanā": "प्रश्नों के खंड में सकारात्मक क्रम की गणना",
    "pañhāvārassa paccanīyuddhāro": "प्रश्नों के खंड में नकारात्मक क्रम के लिए कारणों की छँटाई",
    "pañhāvārassa paccanīyagaṇanā": "प्रश्नों के खंड में नकारात्मक क्रम की गणना",
    "pañhāvārassa anulomapaccanīyaṃ": "प्रश्नों के खंड में सकारात्मक-नकारात्मक क्रम",
    "pañhāvārassa paccanīyānulomaṃ": "प्रश्नों के खंड में नकारात्मक-सकारात्मक क्रम",
    "kusalattikaṃ niṭṭhitaṃ": S.HEAD["Kusalattikaṃ"] + " समाप्त",
    "ekaṃ": "एक", "upādārūpaṃ": S.RUPA_UPADA,
    "vipākābyākataṃ": "कर्म-फल रूपी नैतिक रूप से अनिर्धारित",
    "kiriyābyākataṃ ekaṃ khandhaṃ": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित एक समूह",
    "āhārasamuṭṭhānaṃ ekaṃ mahābhūtaṃ": "आहार से उत्पन्न एक महाभूत",
    "mahābhūte paccayā cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ khandhe vippayuttapaccayā":
        f"महाभूतों के कारण {S.OBJ_P['cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ']} समूहों पर "
        f"{ABL['vippayutta']}",
    "kaṭattārūpaṃ khandhe vippayuttapaccayā": f"{S.RUPA_KATATTA} समूहों पर {ABL['vippayutta']}",
    "nirodhā vuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में",
    "utuṃ": "तापमान", "saṅkhāre aniccato dukkhato anattato vipassati":
        f"निर्मित परिघटनाओं को {S.ANICCA} {S.VIPASSATI['s']}",
    "saṅkhāre aniccato dukkhato anattato vipassanti": f"निर्मित परिघटनाओं को {S.ANICCA} {S.VIPASSATI['p']}",
    "vatthuṃ aniccato dukkhato anattato vipassati": f"आधार को {S.ANICCA} {S.VIPASSATI['s']}",
    "vatthuṃ aniccato dukkhato anattato vipassanti": f"आधार को {S.ANICCA} {S.VIPASSATI['p']}",
    "sekkhā vā puthujjanā vā cakkhuṃ aniccato dukkhato anattato vipassanti":
        f"{S.SEKKHA_PUTHU} आँख को {S.ANICCA} {S.VIPASSATI['p']}",
    "purejātaṃ sekkhā vā puthujjanā vā cakkhuṃ aniccato dukkhato anattato vipassanti":
        f"पूर्व-उत्पत्ति, {S.SEKKHA_PUTHU} आँख को {S.ANICCA} {S.VIPASSATI['p']}",
    "vatthuṃ assādeti abhinandati": "आधार का " + S.SAVOURS.format(p="उसमें"),
    "vatthuṃ assādeti": "आधार का रस लेता है",
    "purejātaṃ cakkhuṃ assādeti": "पूर्व-उत्पत्ति, आँख का रस लेता है",
    "abhinandati": "उसमें आनंद लेता है",
    "dibbena cakkhunā rūpaṃ passati": S.CLAUSE["dibbena cakkhunā rūpaṃ passati"],
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ garuṃ katvā assādeti abhinandati":
        f"{S.GIFT} उसे महत्व देकर उसका " + S.SAVOURS.format(p="उसमें"),
    "taṃ garuṃ katvā assādeti abhinandati": S.CLAUSE["taṃ garuṃ katvā assādeti abhinandati"],
})
for _w, _h in (("sotaṃ", "कान"), ("ghānaṃ", "नाक"), ("jivhaṃ", "जीभ"), ("kāyaṃ", "शरीर"), ("rūpe", "दृश्य रूपों"),
               ("sadde", "ध्वनियों"), ("gandhe", "गंधों"), ("rase", "स्वादों"), ("phoṭṭhabbe", "स्पर्शों"),
               ("vatthuṃ", "आधार")):
    CLAUSE.setdefault(_w, _h)

# upanissāya: «X के प्रबल आश्रय से …»
UPA_OBJ = {"saddhaṃ": "श्रद्धा", "sīlaṃ": "सदाचार", "sutaṃ": "सुने-सीखे ज्ञान", "cāgaṃ": "त्याग", "paññaṃ": "प्रज्ञा",
           "rāgaṃ": "राग", "dosaṃ": "द्वेष", "mohaṃ": "मोह", "mānaṃ": "अहंकार", "diṭṭhiṃ": "दृष्टि",
           "patthanaṃ": "कामना", "kāyikaṃ sukhaṃ": "शारीरिक सुख", "kāyikaṃ dukkhaṃ": "शारीरिक दुःख",
           "utuṃ": "तापमान", "bhojanaṃ": "भोजन", "senāsanaṃ": "निवास-स्थान", "maggaṃ": "मार्ग"}
UPA_WHO = {"sekkhā": S.SEKKHA, "arahā": S.ARAHA}
ACT = {
    "dānaṃ deti": "दान देता है", "sīlaṃ samādiyati": "सदाचार ग्रहण करता है",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है", "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है",
    "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है", "maggaṃ uppādeti": "मार्ग उत्पन्न करता है",
    "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है", "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "mānaṃ jappeti": "अहंकार पालता है", "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "attānaṃ ātāpeti paritāpeti": "स्वयं को तपाता है, कष्ट देता है",
    "pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti": "खोज के कारण होने वाला दुःख भोगता है",
    "pāṇaṃ hanati": "जीव की हत्या करता है", "adinnaṃ ādiyati": "बिना दिया हुआ लेता है",
    "musā bhaṇati": "झूठ बोलता है", "pisuṇaṃ bhaṇati": "चुगली की बातें बोलता है",
    "pharusaṃ bhaṇati": "कठोर वचन बोलता है", "samphaṃ palapati": "व्यर्थ बकवास करता है",
    "sandhiṃ chindati": "सेंध लगाता है", "nillopaṃ harati": "डाका डालता है",
    "ekāgārikaṃ karoti": "एक ही घर में डाका डालता है", "paripanthe tiṭṭhati": "राह में घात लगाता है",
    "paradāraṃ gacchati": "पराई स्त्री के पास जाता है", "gāmaghātaṃ karoti": "गाँव पर हमला करता है",
    "nigamaghātaṃ karoti": "कस्बे पर हमला करता है", "mātaraṃ jīvitā voropeti": "माता की जान लेता है",
    "pitaraṃ jīvitā voropeti": "पिता की जान लेता है", "arahantaṃ jīvitā voropeti": "अर्हत् की जान लेता है",
    "duṭṭhena cittena tathāgatassa lohitaṃ uppādeti": "दुष्ट मन से तथागत का खून बहाता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "anuppannaṃ kiriyasamāpattiṃ uppādeti": "उत्पन्न न हुई केवल क्रिया रूपी ध्यान-अवस्था उत्पन्न करता है",
    "uppannaṃ samāpajjati": "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करता है",
    "anuppannaṃ samāpattiṃ uppādenti": "उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं",
    "uppannaṃ samāpajjanti": "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं",
}
ABS = {
    "pāṇaṃ hantvā": "जीव की हत्या करके", "adinnaṃ ādiyitvā": "बिना दिया हुआ लेकर", "musā bhaṇitvā": "झूठ बोलकर",
    "pisuṇaṃ bhaṇitvā": "चुगली की बातें बोलकर", "pharusaṃ bhaṇitvā": "कठोर वचन बोलकर",
    "samphaṃ palapitvā": "व्यर्थ बकवास करके", "sandhiṃ chinditvā": "सेंध लगाकर", "nillopaṃ haritvā": "डाका डालकर",
    "ekāgārikaṃ karitvā": "एक ही घर में डाका डालकर", "paripanthe ṭhatvā": "राह में घात लगाकर",
    "paradāraṃ gantvā": "पराई स्त्री के पास जाकर", "gāmaghātaṃ karitvā": "गाँव पर हमला करके",
    "nigamaghātaṃ karitvā": "कस्बे पर हमला करके", "mātaraṃ jīvitā voropetvā": "माता की जान लेकर",
    "pitaraṃ jīvitā voropetvā": "पिता की जान लेकर", "arahantaṃ jīvitā voropetvā": "अर्हत् की जान लेकर",
    "duṭṭhena cittena tathāgatassa lohitaṃ uppādetvā": "दुष्ट मन से तथागत का खून बहाकर",
    "saṅghaṃ bhinditvā": "संघ में फूट डालकर",
}
CLAUSE.update(ACT)
CLAUSE.update(ABS)
UPA_RE = re.compile(rf"^(?:({_ALT(UPA_WHO)}) )?({_ALT(UPA_OBJ)}) upanissāya(?: ({_ALT(ACT)}))?$")
PATIGHATA_RE = re.compile(rf"^({_ALT(ABS)}) tassa paṭighātatthāya ({_ALT(ACT)})$")

# ================================================================ notes


def yatha(x, verb="विस्तार करना चाहिए"):
    return f"जैसे {x} है, वैसे ही {verb}।"


NOTE = dict(S.NOTE)
NOTE.update({
    "yathā hetumūlakaṃ, evaṃ vitthāretabbaṃ.": yatha(MULAKA["hetu"]),
    "yathā hetumūlakaṃ, evaṃ gaṇetabbaṃ.": yatha(MULAKA["hetu"], "गिनना चाहिए"),
    "yathā ārammaṇamūlakaṃ, evaṃ vitthāretabbaṃ.": yatha(MULAKA["ārammaṇa"]),
    "yathā nahetumūlakaṃ, evaṃ vitthāretabbaṃ.": yatha(NMULAKA["hetu"]),
    "yathā nahetumūlakaṃ, evaṃ vitthāretabbaṃ": yatha(NMULAKA["hetu"])[:-1],
    "yathā nahetumūlakaṃ evaṃ vitthāretabbaṃ.": yatha(NMULAKA["hetu"]),
    "yathā naaññamaññamūlakaṃ evaṃ vitthāretabbaṃ.": yatha(NMULAKA["aññamañña"]),
    "yathā noatthimūlakaṃ, evaṃ vitthāretabbaṃ.": yatha(NMULAKA["atthi"]),
    "yathā nahetumūlakaṃ, evaṃ najhānamūlakaṃ vitthāretabbaṃ.":
        f"जैसे {NMULAKA['hetu']} है, वैसे ही {NMULAKA['jhāna']} का विस्तार करना चाहिए।",
    "yathā nahetupaccayā, evaṃ vitthāretabbaṃ": yatha(NABL["hetu"])[:-1],
    "yathā nahetumūlakaṃ. saṃkhittaṃ": f"{NMULAKA['hetu']} की तरह। संक्षिप्त",
    "ārammaṇamūlakaṃ yathā hetumūlakaṃ, evaṃ vitthāretabbaṃ.": f"{MULAKA['ārammaṇa']}: " + yatha(MULAKA["hetu"]),
    "anantarapaccayā samanantarapaccayā yathā ārammaṇapaccayā, evaṃ vitthāretabbā.":
        f"{NAME['anantara']} और {NAME['samanantara']}: " + yatha(NAME["ārammaṇa"]),
    "indriyapaccayā yathā kammapaccayā, evaṃ vitthāretabbaṃ.": f"{NAME['indriya']}: " + yatha(NAME["kamma"]),
    "jhānapaccayāpi maggapaccayāpi yathā hetupaccayā, evaṃ vitthāretabbaṃ.":
        f"{NAME['jhāna']} और {NAME['magga']} भी: " + yatha(NAME["hetu"]),
    "nissayapaccayā yathā sahajātamūlakaṃ. upanissayapaccayā yathā ārammaṇamūlakaṃ.":
        f"{NAME['nissaya']} {MULAKA['sahajāta']} की तरह। {NAME['upanissaya']} {MULAKA['ārammaṇa']} की तरह।",
    "nissayapaccayā yathā sahajātapaccayā.": f"{NAME['nissaya']} {NAME['sahajāta']} की तरह।",
    "upanissayapaccayā ārammaṇapaccayasadisaṃ.": f"{NAME['upanissaya']} {SADISA['ārammaṇa']} है।",
    "yathā hetupaccayaṃ, evaṃ vitthāretabbaṃ.": yatha(NAME["hetu"]),
    "yathā ārammaṇapaccayaṃ, evaṃ vitthāretabbaṃ.": yatha(NAME["ārammaṇa"]),
    "yathā sahajātapaccayaṃ, evaṃ vitthāretabbaṃ.": yatha(NAME["sahajāta"]),
    "yathā anantarapaccayaṃ, evaṃ vitthāretabbaṃ.": yatha(NAME["anantara"]),
    "yathā atthipaccayaṃ, evaṃ vitthāretabbaṃ.": yatha(NAME["atthi"]),
    "yathā anulome sahajātapaccayaṃ, evaṃ gaṇetabbaṃ.": yatha(f"सकारात्मक क्रम में {NAME['sahajāta']}", "गिनना चाहिए"),
    "yathā anulome sahajātapaccayaṃ, evaṃ vitthāretabbaṃ.": yatha(f"सकारात्मक क्रम में {NAME['sahajāta']}"),
    "yathā paṭiccavāre evaṃ vitthāretabbaṃ.": yatha("निर्भरता के खंड में"),
    "yathā paṭiccavāre, evaṃ vitthāretabbaṃ.": yatha("निर्भरता के खंड में"),
    "yathā paṭiccavāre naārammaṇapaccayā, evaṃ vitthāretabbaṃ.": yatha(f"निर्भरता के खंड में {NABL['ārammaṇa']}"),
    "avasesaṃ yathā paṭiccavāre paccanīyaṃ, evaṃ vitthāretabbaṃ.":
        "बाकी: " + yatha("निर्भरता के खंड में नकारात्मक क्रम"),
    "yathā paṭiccavāragaṇanā, evaṃ gaṇetabbaṃ.": yatha("निर्भरता के खंड की गणना", "गिनना चाहिए"),
    "yathā paccayavāre, evaṃ vitthāretabbaṃ.": yatha("कारण के खंड में"),
    "yathā atthipaccayo vitthārito evaṃ avigatapaccayo vitthāretabbo.":
        f"जैसे {NAME['atthi']} का विस्तार किया गया है, वैसे ही {NAME['avigata']} का विस्तार करना चाहिए।",
    "paṭiccattaṃ nāma sahajātattaṃ, sahajātattaṃ nāma paṭiccattaṃ.":
        "निर्भर होने का अर्थ है साथ जन्म लेना, साथ जन्म लेने का अर्थ है निर्भर होना।",
    "paccayattaṃ nāma nissayattaṃ, nissayattaṃ nāma paccayattaṃ.":
        "कारण से होने का अर्थ है आश्रय से होना, आश्रय से होने का अर्थ है कारण से होना।",
    "saṃsaṭṭhattaṃ nāma sampayuttattaṃ, sampayuttattaṃ nāma saṃsaṭṭhattaṃ.":
        "घुले-मिले होने का अर्थ है जुड़े होना, जुड़े होने का अर्थ है घुले-मिले होना।",
    "sabbattha ekaṃ": "हर जगह एक", "sabbattha dve": "हर जगह दो", "sabbattha satta": "हर जगह सात",
    "naārammaṇapaccayasadisaṃ": NSADISA["ārammaṇa"],
    "nahetupaccayasadisaṃ": NSADISA["hetu"], "noatthipaccayasadisaṃ": NSADISA["atthi"],
    "ārammaṇapaccayasadisaṃ.": SADISA["ārammaṇa"] + "।", "ārammaṇapaccayasadisaṃ": SADISA["ārammaṇa"],
    "sahajātapaccayasadisaṃ": SADISA["sahajāta"], "hetupaccayasadisaṃ": SADISA["hetu"],
    "saṃkhittaṃ.": "संक्षिप्त।", "saṃkhittaṃ": "संक्षिप्त", "saṃkhittaṃ. paripuṇṇaṃ.": "संक्षिप्त। परिपूर्ण।",
    "paripuṇṇaṃ.": "परिपूर्ण।", "kātabbaṃ": "करना चाहिए", "mūlakaṃ saṃkhittaṃ": "शृंखला संक्षिप्त है",
    "yāvāsevanā sabbaṃ sadisaṃ, nakamme gaṇite pañca pañhā honti.":
        f"{NAME['āsevana']} तक सब समान है, {NNAME['kamma']} को गिनने पर पाँच प्रश्न होते हैं।",
    "atthipaccayā sahajātapaccayasadisaṃ kātabbaṃ. natthipaccayā vigatapaccayā ārammaṇapaccayasadisaṃ, "
    "avigatapaccayā sahajātapaccayasadisaṃ.":
        f"{NAME['atthi']} को {SADISA['sahajāta']} करना चाहिए। {NAME['natthi']} और {NAME['vigata']} "
        f"{SADISA['ārammaṇa']} हैं, {NAME['avigata']} {SADISA['sahajāta']} है।",
    "abyākataṃ paripuṇṇaṃ kātabbaṃ": "नैतिक रूप से अनिर्धारित को परिपूर्ण करना चाहिए",
    "napacchājātapaccayampi naāsevanapaccayampi paripuṇṇaṃ, sattarasa.":
        f"{NNAME['pacchājāta']} और {NNAME['āsevana']} भी परिपूर्ण हैं, सत्रह।",
    "vipākaṃ ṭhapetvā sabbattha vitthāretabbaṃ.": "कर्म-फल रूपी को छोड़कर हर जगह विस्तार करना चाहिए।",
    "najhāne idaṃ nānākaraṇaṃ.": f"{NLOC['jhāna']} यह अंतर है।",
    "namagge idaṃ nānākaraṇaṃ.": f"{NLOC['magga']} यह अंतर है।",
    "adhipati paṭisandhikkhaṇe natthi.": f"पुनर्जन्म के क्षण में {NAME['adhipati']} नहीं है।",
    "sabbāni padāni hetumūlakasadisāni": f"सभी पद {MULAKA['hetu']} के समान हैं",
    "imāni padāni hetupaccayasadisāni.": f"ये पद {SADISA['hetu']} हैं।",
    "hetumūlakaṃ vitthāretabbaṃ.": f"{MULAKA['hetu']} का विस्तार करना चाहिए।",
    "saṃsaṭṭhavāre paccanīyavibhaṅge nakamme ca navipāke ca paṭisandhi natthi; avasesesu sabbattha atthi.":
        f"घुले-मिले होने के खंड में, नकारात्मक क्रम के विश्लेषण में, {NLOC['kamma']} और {NLOC['vipāka']} "
        "पुनर्जन्म नहीं है; बाकी में हर जगह है।",
    "navippayutte paṭisandhi natthi.": f"{NLOC['vippayutta']} पुनर्जन्म नहीं है।",
    "navipākaṃ namaggaṃ navippayuttaṃ nakammapaccayasadisaṃ.":
        f"{NNAME['vipāka']}, {NNAME['magga']} और {NNAME['vippayutta']} {NSADISA['kamma']} हैं।",
    "naadhipatimūlakaṃ nahetumhi ṭhitena nahetumūlakasadisaṃ kātabbaṃ.":
        f"{nbase('hetu')} पर टिके रहने पर {NMULAKA['adhipati']} को {NMULAKA['hetu']} के समान करना चाहिए।",
    "sabbāni padāni vitthāretabbāni, imāni alikhitesu padesu tīṇi pañhā. napurejātamūlake nahetuyā ṭhitena "
    "āsevane ca magge ca eko pañho kātabbo, avasesāni nahetupaccayasadisāni. napacchājātapaccayā paripuṇṇaṃ "
    "naadhipatipaccayasadisaṃ.":
        "सभी पदों का विस्तार करना चाहिए, इन न लिखे गए पदों में तीन प्रश्न हैं। "
        f"{NMULAKA['pacchājāta'].replace('पश्चात्', 'पूर्व')} में, {nbase('hetu')} पर टिके रहने पर, "
        f"{LOC['āsevana']} और {LOC['magga']} एक प्रश्न करना चाहिए, बाकी {NSADISA['hetu']} हैं। "
        f"{NABL['pacchājāta']} परिपूर्ण है, {NSADISA['adhipati']}।",
    "avasesāni padāni etenupāyena vitthāretabbāni. saṃkhittaṃ.":
        "बाकी पदों का इसी उपाय से विस्तार करना चाहिए। संक्षिप्त।",
    "navipākamūlake idaṃ nānākaraṇaṃ, avasesāni yathā nahetumūlakaṃ.":
        f"{NMULAKA['vipāka']} में यह अंतर है, बाकी {NMULAKA['hetu']} की तरह।",
    "naāsevanapaccayamūlakampi nahetumūlakasadisaṃ.": f"{NMULAKA['āsevana']} भी {NMULAKA['hetu']} के समान है।",
    "imāni tīṇi mūlāni ekasadisāni": "ये तीन शृंखलाएँ एक समान हैं",
    "cakkaṃ bandhitabbaṃ.": "चक्र बाँधना चाहिए।", "cakkaṃ kātabbaṃ.": "चक्र बनाना चाहिए।",
    "natthipaccayampi vigatapaccayampi anantarapaccayasadisaṃ.":
        f"{NAME['natthi']} और {NAME['vigata']} भी {SADISA['anantara']} हैं।",
    "naindriyapaccayā kamme satta pañhā.": f"{NABL['indriya']}, {LOC['kamma']} सात प्रश्न।",
})
NOTE.update({f"{s} – {n}": f"{SAHITA['savipākaṃ'] if s == 'savipākaṃ' else 'कर्म-फल-कारण रहित'} – {n}"
             for s in ("avipākaṃ", "savipākaṃ") for n in range(1, 10)})
NOTE.update(SAHITA)

# ================================================================ variants and slips

VARIANTS = dict(S.VARIANTS)
VARIANTS.update({
    "{āruppe (sabbattha)}": ("पाठभेद", "अभौतिक लोक में"),
    "{nānākhaṇikā (ka.)}": ("वर्तनी-भेद", "भिन्न क्षण"),
    "{nahetumūlake (syā.)}": ("पाठभेद", f"{NMULAKA['hetu']} की तरह"),
})


def variant_hi(v, kind):
    m = re.fullmatch(r"\{(.*) \(([^)]*)\)\}", v)
    if m and m.group(2) == "sabbattha":
        return f"[{kind} (हर जगह): {m.group(1)}]"
    return S.variant_hi(v, kind)


# pure spelling / spacing slips, rendered as meant (each is listed in notes-1-01.md)
SLIPS = [
    ("na aññamaññapaccayā", "naaññamaññapaccayā"),     # ^7-2-90 (sample)
    ("adhipati paccayena", "adhipatipaccayena"),       # ^7-2-415 (sample)
    ("naaññamañña-paccayā", "naaññamaññapaccayā"),
    ("Nadhipatipaccayā", "Naadhipatipaccayā"),
    ("na anantare", "naanantare"), ("na ārammaṇe", "naārammaṇe"), ("na indriye", "naindriye"),
    ("na jhāne", "najhāne"), ("Na jhāne", "Najhāne"), ("na pacchājāte", "napacchājāte"),
    ("na āsevane", "naāsevane"), ("na adhipatiyā", "naadhipatiyā"), ("na hetupaccayā", "nahetupaccayā"),
    ("no avigate", "noavigate"),
    ("naanantare sattaṃ", "naanantare satta"),
    ("na-ārammaṇe", "naārammaṇe"), ("naṃindriye", "naindriye"),
    ("vippayuttaṃ-avigatanti", "vippayutta-avigatanti"), ("vipākaṃ-indriya", "vipāka-indriya"),
    ("paññaṃ upanissaya dānaṃ", "paññaṃ upanissāya dānaṃ"),
    ("dve khandha nissāya", "dve khandha nissāya"),  # kept: SUBJ_P «dve khandha» renders it as meant
    # not a slip: «sutaṃ» as object of upanissāya in an elided list takes the oblique (§ = object marker)
    ("sutaṃ…pe… cāgaṃ", "sutaṃ§…pe… cāgaṃ"),
]
CLAUSE_OBJ_MARK = {"sutaṃ§": "सुने-सीखे ज्ञान"}

# ================================================================ counting lines

PH0, PH1 = "\x1e", "\x1f"
PH_RE = re.compile(PH0 + r"(\d+)" + PH1)
COUNT_WORDS = set(S.P_ABL) | set(S.P_NABL) | set(S.P_LOC) | set(S.P_NLOC) | set(NUM)
CNT_TOK = re.compile(r"( …pe… | … |…pe…|…|, |; | |\.|\(\d+\))")


def count_tokens(seg):
    return [t for t in CNT_TOK.split(seg) if t]


def is_count_seg(seg):
    """True if every word of the segment is a count word or a single-word clause (Hetumūlakaṃ.)."""
    words = [t for t in count_tokens(seg) if t.strip(" ") and not CNT_TOK.fullmatch(t)]
    return all(w in COUNT_WORDS or w in CLAUSE for w in words), sum(w in COUNT_WORDS for w in words)


def count_hi(seg):
    toks = count_tokens(seg)
    out = []
    for i, t in enumerate(toks):
        if t == " ":
            prev = toks[i - 1] if i else ""
            out.append(", " if prev in S.P_ABL or prev in S.P_NABL else " ")
        elif t in (" …pe… ", " … "):
            out.append(" … ")
        elif t == "…pe…":
            out.append("…")
        elif t == ".":
            out.append("।")
        elif t in ("…", ", ", "; ") or re.fullmatch(r"\(\d+\)", t):
            out.append(t)
        else:
            for d in (S.P_ABL, S.P_NABL, S.P_LOC, S.P_NLOC, NUM, CLAUSE):
                if t in d:
                    out.append(d[t])
                    break
            else:
                raise KeyError(t)
    return "".join(out)


# ================================================================ ghaṭanā («A-B-Cnti n»)

GH_STEMS = sorted(KEYS, key=len, reverse=True)


def gh_split(comp):
    s = re.sub(r"[\s-]", "", comp)
    s = s.replace("hetādhipati", "hetuadhipati").replace("ādhipati", "aadhipati").replace("ūpanissaya", "aupanissaya")
    out, i = [], 0
    while i < len(s):
        for k in GH_STEMS:
            if s.startswith(k, i):
                out.append(k)
                i += len(k)
                break
        else:
            return None
    return out


GH_SENT_RE = re.compile(r"^(.+?)(nti|īti) (.+)$")


def gh_sentence(sent):
    """'hetu-sahajāta-…-avigatanti satta' or '…-avigatanti naārammaṇe satta, …' -> Hindi, or None."""
    m = GH_SENT_RE.match(sent)
    if not m:
        return None
    comp = m.group(1) + ("i" if m.group(2) == "īti" else "")
    conds = gh_split(comp)
    if not conds or len(conds) < 2:
        return None
    rest = m.group(3)
    names = andjoin(NAME[c] for c in conds)
    if rest in NUM:
        return f"{names} के संयोजन में {NUM[rest]}"
    ok, n = is_count_seg(rest)
    if ok and n:
        return f"{names} के संयोजन से, {count_hi(rest)}"
    return None


def try_ghatana(text):
    """text: lower-cased, notes already placeholders. Returns Hindi or None."""
    parts = re.split(r"(\. |\.$)", text)
    out, hit = [], False
    for p in parts:
        if p in (". ", "."):
            out.append("। " if p == ". " else "।")
            continue
        if not p.strip(" "):
            out.append(p)
            continue
        core = p.strip(" ")
        if re.fullmatch(rf"(?:(?:{PH0}\d+{PH1}|\(\d+\)) ?)+", core):
            out.append(p)
            continue
        h = gh_sentence(core)
        if h is None:
            return None
        hit = True
        out.append(p.replace(core, h))
    return "".join(out) if hit else None


# ================================================================ hand lines

LINE_HAND = dict(S.LINE_HAND)
LINE_HAND.update({
    "Kusalo ca abyākato ca dhammā kusalassa dhammassa sahajātaṃ, purejātaṃ.":
        f"हितकर और नैतिक रूप से अनिर्धारित परिघटनाएँ, {S.DAT['kusalassa dhammassa']} सह-उत्पत्ति, पूर्व-उत्पत्ति।",
    "Kusalo ca abyākato ca dhammā abyākatassa dhammassa sahajātaṃ, pacchājātaṃ, āhāraṃ, indriyaṃ. (2)":
        f"हितकर और नैतिक रूप से अनिर्धारित परिघटनाएँ, {S.DAT['abyākatassa dhammassa']} सह-उत्पत्ति, "
        "पश्चात्-उत्पत्ति, आहार, क्षमता। (2)",
    "Akusalo ca abyākato ca dhammā akusalassa dhammassa sahajātaṃ, purejātaṃ.":
        f"हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ, {S.DAT['akusalassa dhammassa']} सह-उत्पत्ति, पूर्व-उत्पत्ति।",
    "Akusalo ca abyākato ca dhammā abyākatassa dhammassa sahajātaṃ, pacchājātaṃ, āhāraṃ, indriyaṃ. (2)":
        f"हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ, {S.DAT['abyākatassa dhammassa']} सह-उत्पत्ति, "
        "पश्चात्-उत्पत्ति, आहार, क्षमता। (2)",
    "Nonatthipaccayā nahetuyā pannarasa (saṃkhittaṃ). Nonatthiyā ca, novigate ca (nahetupaccayasadisaṃ).":
        f"{NABL['natthi']}, {NLOC['hetu']} पंद्रह (संक्षिप्त)। {NLOC['natthi']} और {NLOC['vigata']} "
        f"({NSADISA['hetu']})।",
})

# ================================================================ the line translator


def clause(piece):
    core = piece.strip()
    if not core:
        return piece
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    m = None
    if core in CLAUSE_OBJ_MARK:
        h = CLAUSE_OBJ_MARK[core]
    elif core in CLAUSE:
        h = CLAUSE[core]
    elif PCLAUSE_RE.match(core):
        pre, subj, v, obj = PCLAUSE_RE.match(core).groups()
        h = (PREFIX[pre] + " " if pre else "") + f"{SUBJ_P[subj]} {VBODY[v]}" + (" " + OBJ_P[obj] if obj else "")
    elif SHORT_RE.match(core):
        subj, on, cond = SHORT_RE.match(core).groups()
        h = (S.SHORT_SUBJ[subj] + " " if subj else "") + f"{S.SHORT_ON[on]} पर {S._cond_word(cond)}"
    elif (m := PART_FRAME_RE.match(core)):
        x, v, y = m.groups()
        h = f"{ACC[x]} {VFRAME[v]} {NOM[y][0]}"
    elif (m := NOM_VERB_RE.match(core)):
        y, chain = m.groups()
        h = f"{NOM[y][0]} {S.CH(chain)} {ARISES[NOM[y][1]]}"
    elif (m := NOM_ONLY_RE.match(core)):
        h = NOM[m.group(1)][0]
    elif (m := ACC_ONLY_RE.match(core)):
        h = ACC[m.group(1)]
    elif re.fullmatch(CHAIN_RE, core):
        h = S.CH(core)
    elif (m := UPA_RE.match(core)):
        who, obj, act = m.groups()
        h = (UPA_WHO[who] + " " if who else "") + f"{UPA_OBJ[obj]} के प्रबल आश्रय से" + (" " + ACT[act] if act else "")
    elif (m := PATIGHATA_RE.match(core)):
        h = f"{ABS[m.group(1)]} उसके प्रतिकार के लिए {ACT[m.group(2)]}"
    elif (m := PAIR_RE.match(core)):
        h = f"{SUBJ[m.group(1)][0]} {DAT[m.group(2)]}"
    elif (m := PAIR_UPA_RE.match(core)):
        s, d = m.groups()
        h = (SUBJ[s][0] + " " if s else "") + f"{DAT[d]} {NAME['upanissaya']}"
    elif core in SUBJ:
        h = SUBJ[core][0].rstrip(",")
    elif core in DAT:
        h = DAT[core]
    elif core in UPA_OBJ:
        h = UPA_OBJ[core]
    else:
        raise KeyError(f"no clause for: {core!r}")
    return lead + h + trail


def note_hi(key):
    if key in NOTE:
        return NOTE[key]
    raise KeyError(f"note: {key!r}")


def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    if line in LINE_HAND:
        return LINE_HAND[line]
    inserts = []
    for v, (kind, anchor) in VARIANTS.items():
        if v in line:
            line = line.replace(" " + v, "")
            inserts.append((anchor, variant_hi(v, kind)))
    if "{" in line:
        raise KeyError(f"unregistered variant in: {line!r}")
    for a, b in SLIPS:
        line = re.sub(r"(?<!\w)" + re.escape(a), b, line)
    text = S.lower_initials(line)
    store = []

    def keep(h):
        store.append(h)
        return f"{PH0}{len(store) - 1}{PH1}"

    text = re.sub(r"\(([^()]*[^\d().][^()]*)\)", lambda m: keep("(" + note_hi(m.group(1)) + ")"), text)

    # ghaṭanā lines
    g = try_ghatana(text)
    if g is not None:
        return _finish(g, store, inserts)

    # counting / chain-only lines: every segment between notes is a count segment
    segs = PH_RE.split(text)
    plain = [s for i, s in enumerate(segs) if i % 2 == 0]
    checks = [is_count_seg(s) for s in plain if s.strip()]
    if checks and all(ok for ok, _ in checks) and sum(n for _, n in checks):
        out = []
        for i, s in enumerate(segs):
            if i % 2:
                out.append(f"{PH0}{s}{PH1}")
            elif s.strip():
                lead = s[: len(s) - len(s.lstrip())]
                out.append(lead + count_hi(s[len(lead):]))
            else:
                out.append(s)
        return _finish("".join(out), store, inserts)

    # frames
    text = S.SIYA_RE.sub(lambda m: keep(S.siya_frame(m.group(1), m.group(2), m.group(3), m.group(4) or "")), text)
    text = FRAME_RE.sub(lambda m: keep(frame(*m.groups())), text)
    state = {"g": None}

    def defn(m):
        subj, dat, kinci, neg, k = m.groups()
        parts = []
        if subj:
            sh, state["g"] = SUBJ[subj]
            parts.append(sh)
        else:
            prev = SUBJ_WORD_RE.findall(PH_RE.sub(" ", text[: m.start()]))
            if prev:
                state["g"] = SUBJ[prev[-1]][1]
                FALLBACK_LOG.append(f"{prev[-1]} -> {m.group(0)}")
            elif state["g"] is not None:
                FALLBACK_LOG.append(f"(carried {state['g']}) -> {m.group(0)}")
        if state["g"] is None:
            raise KeyError(f"no subject before: {m.group(0)!r}")
        if dat:
            parts.append(DAT[dat])
        if kinci:
            parts.append(S.KINCI_KALE)
        parts.append(S.NINS(k, state["g"]) if neg else S.INS(k, state["g"]))
        return keep(" ".join(parts))

    text = DEF_RE.sub(defn, text)
    out = []
    for tok in re.split(r"( – |; |, |\. |…pe…|…|\.$)", text):
        if tok in (" – ", "; ", ", ", "…"):
            out.append(tok)
        elif tok == ". ":
            out.append("। ")
        elif tok == ".":
            out.append("।")
        elif tok == "…pe…":
            out.append("…")
        elif tok:
            for part in re.split(r"(\d+|\(\d+\))", tok):
                if not part.strip() or re.fullmatch(r"\d+|\(\d+\)", part):
                    out.append(part)
                else:
                    out.append(clause(part))
    return _finish("".join(out), store, inserts)


def _finish(s, store, inserts):
    for _ in range(3):
        s = PH_RE.sub(lambda m: store[int(m.group(1))], s)
    s = s.replace("?।", "?")
    for anchor, br in inserts:
        assert anchor in s, (anchor, s)
        s = s.replace(anchor, anchor + " " + br, 1)
    return s


# ================================================================ file builder and sample check

ID_RE = S.ID_RE


def build(src, dst):
    lines = open(src, encoding="utf-8").read().split("\n")
    out, errors = [], []
    n = 0
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        n += 1
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        try:
            hi = translate_line(body)
        except Exception as e:  # collect, report all at once
            errors.append(f"[{n}] {type(e).__name__}: {e}"[:400])
            hi = "!!! " + body
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    return errors


def check_samples(dst):
    hi = [l for l in open(dst, encoding="utf-8").read().split("\n") if l.strip()]
    bad = 0
    for name, a, b in (("1-01-a-sample.md", 1, 190), ("1-01-b-sample.md", 1235, 1262)):
        smp = [l for l in open(os.path.join(HERE, "sample-1", name), encoding="utf-8").read().split("\n") if l.strip()]
        mine = hi[a - 1: b]
        if mine != smp:
            for i, (x, y) in enumerate(zip(mine, smp)):
                if x != y:
                    bad += 1
                    if bad <= 5:
                        print(f"SAMPLE MISMATCH line {a + i}:\n  mine:   {x[:300]}\n  sample: {y[:300]}")
            if len(mine) != len(smp):
                bad += 1
                print("SAMPLE length mismatch", name, len(mine), len(smp))
    print("sample regions identical" if not bad else f"sample mismatches: {bad}")
    return bad


if __name__ == "__main__":
    errs = build(SRC, DST)
    import collections
    c = collections.Counter(errs)
    print("lines with errors:", len(errs), "kinds:", len(c))
    for k, n in list(c.items())[: int(sys.argv[1]) if len(sys.argv) > 1 else 40]:
        print(n, k)
    fl = collections.Counter(FALLBACK_LOG)
    print("subject fallbacks:", len(FALLBACK_LOG))
    if "-v" in sys.argv:
        for k, n in fl.items():
            print("  ", n, k[:160])
    check_samples(DST)
