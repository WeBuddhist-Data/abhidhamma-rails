"""pi-7 Paṭṭhāna, Hindi plain RAILS: formula constants and the sample builder.

Import read-only:  import build_rails_sample as R   (no side effects on import)
  R.NAME[k], R.ABL[k], R.NABL[k], R.NNAME[k], R.LOC[k], R.NLOC[k], R.INS(k, g), R.NINS(k, g), R.SADISA[k] ...
  R.CH("hetupaccayā ārammaṇapaccayā")  -> "मूल-कारण से, विषय-कारण से"
  R.count_hi("Hetuyā nava, ārammaṇe tīṇi.") -> "मूल-कारण में नौ, विषय-कारण में तीन।"
  R.translate_line(pali_line) -> Hindi line (block ID not included)
Run as a script to rebuild the sample:
  python -I -B -X utf8 build_rails_sample.py
Every string here is also listed in hi-rails-formulas.md.
"""
import os
import re

# ---------------------------------------------------------------- 1. book frame and headings

NAMO = "उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन"
ABHIDHAMMAPITAKE = "अभिधम्म पिटक में"
BOOK_TITLE = "कारण-संबंध"

HEAD = {
    # book frame and divisions
    "Namo tassa bhagavato arahato sammāsambuddhassa": NAMO,
    "Abhidhammapiṭake": ABHIDHAMMAPITAKE,
    "Paṭṭhānapāḷi": BOOK_TITLE,
    "(Paṭhamo bhāgo)": "(पहला भाग)",
    "Dhammānulome": "परिघटनाओं का सकारात्मक क्रम",
    "Tikapaṭṭhānaṃ": "तीन-तीन के वर्गीकरणों के कारण-संबंध",
    # sections
    "Paccayuddeso": "कारणों की सूची",
    "Paccayaniddeso": "कारणों की व्याख्या",
    "Pucchāvāro": "पूछताछ का खंड",
    "Paṭiccavāro": "निर्भरता का खंड",
    "Vibhaṅgavāro": "विश्लेषण का खंड",
    "Saṅkhyāvāro": "गणना का खंड",
    "Pañhāvāro": "प्रश्नों का खंड",
    "Paccayānulomaṃ": "कारणों का सकारात्मक क्रम",
    "Paccayapaccanīyaṃ": "कारणों का नकारात्मक क्रम",
    "Paccayānulomapaccanīyaṃ": "कारणों का सकारात्मक-नकारात्मक क्रम",
    "Paccayapaccanīyānulomaṃ": "कारणों का नकारात्मक-सकारात्मक क्रम",
    "Anulomaṃ – hetupaccayo": "सकारात्मक क्रम – मूल-कारण",
    "Paccanīyaṃ – nahetupaccayo": "नकारात्मक क्रम – मूल-कारण का अभाव",
    # series (mūlaka)
    "Ekamūlakaṃ": "एक कारण वाली शृंखला",
    "Dumūlakādi": "दो कारणों वाली शृंखला आदि",
    "Hetumūlakaṃ": "मूल-कारण से शुरू होने वाली शृंखला",
    "Ārammaṇamūlakādi": "विषय-कारण से शुरू होने वाली शृंखला आदि",
    # items (pada)
    "Kusalapadaṃ": "हितकर पद",
    "Akusalapadaṃ": "हानिकर पद",
    "Abyākatapadaṃ": "नैतिक रूप से अनिर्धारित पद",
    "Kusalābyākatapadaṃ": "हितकर और नैतिक रूप से अनिर्धारित पद",
    "Akusalābyākatapadaṃ": "हानिकर और नैतिक रूप से अनिर्धारित पद",
    "Kusalākusalapadaṃ": "हितकर और हानिकर पद",
    "Kusalākusalābyākatapadaṃ": "हितकर, हानिकर और नैतिक रूप से अनिर्धारित पद",
    # triad name
    "Kusalattikaṃ": "हितकर वाला तीन का वर्गीकरण",
    # counting headings
    "Suddhaṃ": "अकेले-अकेले कारण",
    "Gaṇanā hetumūlakā": "मूल-कारण से शुरू होने वाली गणना",
    "Dukaṃ": "दो कारणों का मेल",
    "Tikaṃ": "तीन कारणों का मेल",
    "Dvādasakaṃ": "बारह कारणों का मेल",
    "Terasakaṃ": "तेरह कारणों का मेल",
    "Bāvīsakaṃ": "बाईस कारणों का मेल",
    "Ārammaṇādidukāni": "विषय-कारण आदि के साथ दो कारणों के मेल",
    "Āhārādidukāni": "आहार-कारण आदि के साथ दो कारणों के मेल",
}

# ---------------------------------------------------------------- 2. the 24 conditions

# key (Pāli stem), Hindi name, count locative (Pāli), negative prefix
CONDS = [
    ("hetu", "मूल-कारण", "hetuyā", "na"),
    ("ārammaṇa", "विषय-कारण", "ārammaṇe", "na"),
    ("adhipati", "प्रधानता-कारण", "adhipatiyā", "na"),
    ("anantara", "निकटता-कारण", "anantare", "na"),
    ("samanantara", "पूर्ण निकटता-कारण", "samanantare", "na"),
    ("sahajāta", "सह-उत्पत्ति-कारण", "sahajāte", "na"),
    ("aññamañña", "परस्पर-कारण", "aññamaññe", "na"),
    ("nissaya", "आश्रय-कारण", "nissaye", "na"),
    ("upanissaya", "प्रबल आश्रय-कारण", "upanissaye", "na"),
    ("purejāta", "पूर्व-उत्पत्ति-कारण", "purejāte", "na"),
    ("pacchājāta", "पश्चात्-उत्पत्ति-कारण", "pacchājāte", "na"),
    ("āsevana", "पुनरावृत्ति-कारण", "āsevane", "na"),
    ("kamma", "कर्म-कारण", "kamme", "na"),
    ("vipāka", "कर्म-फल-कारण", "vipāke", "na"),
    ("āhāra", "आहार-कारण", "āhāre", "na"),
    ("indriya", "क्षमता-कारण", "indriye", "na"),
    ("jhāna", "ध्यान-कारण", "jhāne", "na"),
    ("magga", "मार्ग-कारण", "magge", "na"),
    ("sampayutta", "जुड़ाव-कारण", "sampayutte", "na"),
    ("vippayutta", "अलगाव-कारण", "vippayutte", "na"),
    ("atthi", "उपस्थिति-कारण", "atthiyā", "no"),
    ("natthi", "अनुपस्थिति-कारण", "natthiyā", "no"),
    ("vigata", "विलीनता-कारण", "vigate", "no"),
    ("avigata", "अविलीनता-कारण", "avigate", "no"),
]
KEYS = [c[0] for c in CONDS]
NAME = {k: h for k, h, _, _ in CONDS}                      # hetupaccayo (named condition, heading)
ABL = {k: h + " से" for k, h, _, _ in CONDS}               # hetupaccayā
NABL = {k: h + " के बिना" for k, h, _, _ in CONDS}         # nahetupaccayā
NNAME = {k: h + " का अभाव" for k, h, _, _ in CONDS}        # nahetupaccayo (heading, note)
LOC = {k: h + " में" for k, h, _, _ in CONDS}              # hetuyā (count)
NLOC = {k: h + " के अभाव में" for k, h, _, _ in CONDS}     # nahetuyā (count)
SADISA = {k: h + " के समान" for k, h, _, _ in CONDS}       # hetupaccayasadisaṃ
NSADISA = {k: h + " के अभाव के समान" for k, h, _, _ in CONDS}  # nahetupaccayasadisaṃ
MULAKA = {k: h + " से शुरू होने वाली शृंखला" for k, h, _, _ in CONDS}      # hetumūlakaṃ
MULAKE = {k: h + " से शुरू होने वाली शृंखला में" for k, h, _, _ in CONDS}  # āsevanamūlake (note)
DUKA = {k: h + " के साथ दो कारणों का मेल" for k, h, _, _ in CONDS}         # Āsevanadukaṃ (count heading)
NDUKA = {k: h + " के अभाव के साथ दो कारणों का मेल" for k, h, _, _ in CONDS}  # Nahetudukaṃ

# verb of "… paccayo": agrees with the subject (ms, fs, mp, fp)
VERB = {"ms": "होता है", "fs": "होती है", "mp": "होते हैं", "fp": "होती हैं"}
NVERB = {"ms": "होता", "fs": "होती", "mp": "होते", "fp": "होतीं"}


def INS(k, g):
    """Xpaccayena paccayo = '<name> के रूप में कारण होता/होती है/होते/होती हैं'."""
    return f"{NAME[k]} के रूप में कारण {VERB[g]}"


def NINS(k, g):
    """na Xpaccayena paccayo = '<name> के रूप में कारण नहीं होता/होती/होते/होतीं'."""
    return f"{NAME[k]} के रूप में कारण नहीं {NVERB[g]}"


# Pāli word forms -> Hindi
P_NOM, P_ABL, P_NABL, P_LOC, P_NLOC = {}, {}, {}, {}, {}
for _k, _h, _loc, _neg in CONDS:
    P_NOM[_k + "paccayo"] = NAME[_k]
    P_NOM[_k + "paccayoti"] = NAME[_k]
    P_ABL[_k + "paccayā"] = ABL[_k]
    P_NABL[_neg + _k + "paccayā"] = NABL[_k]
    P_LOC[_loc] = LOC[_k]
    P_NLOC[_neg + _loc] = NLOC[_k]

NUM = {"ekaṃ": "एक", "dve": "दो", "tīṇi": "तीन", "cattāri": "चार", "pañca": "पाँच", "cha": "छह",
       "satta": "सात", "aṭṭha": "आठ", "nava": "नौ"}

for _k in KEYS:
    HEAD[_k[0].upper() + _k[1:] + "paccayo"] = NAME[_k]
    _n = ("no" if _k in ("atthi", "natthi", "vigata", "avigata") else "na") + _k
    HEAD[_n[0].upper() + _n[1:] + "paccayo"] = NNAME[_k]
    HEAD[_k[0].upper() + _k[1:] + "dukaṃ"] = DUKA[_k]
# combined headings «X-Ypaccayā» = «X-कारण और Y-कारण»; negated = «X-कारण का अभाव और Y-कारण का अभाव»
HEAD["Anantara-samanantarapaccayā"] = f"{NAME['anantara']} और {NAME['samanantara']}"
HEAD["Jhāna-maggapaccayā"] = f"{NAME['jhāna']} और {NAME['magga']}"
HEAD["Natthi-vigatapaccayā"] = f"{NAME['natthi']} और {NAME['vigata']}"
HEAD["Naanantara-nasamanantarapaccayā"] = f"{NNAME['anantara']} और {NNAME['samanantara']}"
HEAD["Napacchājāta-naāsevanapaccayā"] = f"{NNAME['pacchājāta']} और {NNAME['āsevana']}"
HEAD["Nonatthi-novigatapaccayā"] = f"{NNAME['natthi']} और {NNAME['vigata']}"


def _cond_word(w):
    for d in (P_ABL, P_NABL):
        if w in d:
            return d[w]
    raise KeyError(w)


COND_ALT = "|".join(sorted(list(P_ABL) + list(P_NABL), key=len, reverse=True))
_SEP = r"(?: |… |…pe… | …pe… | … )"
CHAIN_RE = rf"(?:{COND_ALT})(?:{_SEP}(?:{COND_ALT}))*"


def CH(chain):
    """A chain of ablatives: words joined by ', '; '…pe…' becomes '…'."""
    out = []
    for tok in re.split(r"( …pe… | … |…pe… |… | )", chain):
        if not tok:
            continue
        if tok == " ":
            out.append(", ")
        elif "…" in tok:
            out.append(tok.replace("…pe…", "…"))
        else:
            out.append(_cond_word(tok))
    return "".join(out)


# ---------------------------------------------------------------- 3. kusalattika items

ACC = {  # X dhammaṃ (paṭicca object, oblique before पर)
    "kusalaṃ": "हितकर परिघटना",
    "akusalaṃ": "हानिकर परिघटना",
    "abyākataṃ": "नैतिक रूप से अनिर्धारित परिघटना",
    "kusalañca abyākatañca": "हितकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना",
    "akusalañca abyākatañca": "हानिकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना",
    "kusalañca akusalañca": "हितकर परिघटना और हानिकर परिघटना",
    "kusalañca akusalañca abyākatañca": "हितकर परिघटना, हानिकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना",
}
NOM = {  # X dhammo (sg) / X ca Y ca dhammā (pl)
    "kusalo": ("हितकर परिघटना", "s"),
    "akusalo": ("हानिकर परिघटना", "s"),
    "abyākato": ("नैतिक रूप से अनिर्धारित परिघटना", "s"),
    "kusalo ca abyākato ca": ("हितकर और नैतिक रूप से अनिर्धारित परिघटनाएँ", "p"),
    "akusalo ca abyākato ca": ("हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ", "p"),
    "kusalo ca akusalo ca": ("हितकर और हानिकर परिघटनाएँ", "p"),
    "kusalo ca akusalo ca abyākato ca": ("हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ", "p"),
}
DAT_ITEM = {  # X dhammassa (pañhāvāra)
    "kusalassa dhammassa": "हितकर परिघटना के लिए",
    "akusalassa dhammassa": "हानिकर परिघटना के लिए",
    "abyākatassa dhammassa": "नैतिक रूप से अनिर्धारित परिघटना के लिए",
    "kusalassa ca abyākatassa ca dhammassa": "हितकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना के लिए",
    "akusalassa ca abyākatassa ca dhammassa": "हानिकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना के लिए",
}

ARISES = {"s": "उत्पन्न होती है", "p": "उत्पन्न होती हैं"}            # uppajjati / uppajjanti
MAY_ARISE = {"s": "उत्पन्न हो सकती है", "p": "उत्पन्न हो सकती हैं"}   # uppajjeyya / uppajjeyyuṃ
PATICCA = "पर निर्भर होकर"


def paticca_frame(x, y, chain):
    """X dhammaṃ paṭicca Y dhammo uppajjati <chain>."""
    yh, n = NOM[y]
    return f"{ACC[x]} {PATICCA} {yh} {CH(chain)} {ARISES[n]}"


def siya_frame(x, y, chain, dots=""):
    """Siyā X dhammaṃ paṭicca Y dhammo uppajjeyya <chain>. (question form approved by the user)"""
    yh, n = NOM[y]
    return f"क्या {ACC[x]} {PATICCA} {yh} {CH(chain)}{dots} {MAY_ARISE[n]}?"


# ---------------------------------------------------------------- 4. khandha / matter clauses (paṭicca bodies)

SUBJ_P = {  # object of paṭicca, oblique form
    "kusalaṃ ekaṃ khandhaṃ": "एक हितकर समूह",
    "akusalaṃ ekaṃ khandhaṃ": "एक हानिकर समूह",
    "vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ": "कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित एक समूह",
    "ahetukaṃ vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ":
        "मूल से रहित, कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित एक समूह",
    "vipākābyākataṃ ekaṃ khandhaṃ": "कर्म-फल रूपी नैतिक रूप से अनिर्धारित एक समूह",
    "kiriyābyākataṃ ekaṃ khandhaṃ": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित एक समूह",
    "pañcaviññāṇasahagataṃ ekaṃ khandhaṃ": "पाँच प्रकार की चेतना के साथ होने वाले एक समूह",
    "tayo khandhe": "तीन समूहों",
    "dve khandhe": "दो समूहों",
    "khandhe": "समूहों",
    "kusale khandhe": "हितकर समूहों",
    "akusale khandhe": "हानिकर समूहों",
    "vipākābyākate kiriyābyākate khandhe": "कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूहों",
    "vipākābyākate khandhe": "कर्म-फल रूपी नैतिक रूप से अनिर्धारित समूहों",
    "kiriyābyākate khandhe": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूहों",
    "vicikicchāsahagate uddhaccasahagate khandhe": "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों",
    "kusale khandhe ca mahābhūte ca": "हितकर समूहों और महाभूतों",
    "akusale khandhe ca mahābhūte ca": "हानिकर समूहों और महाभूतों",
    "vatthuṃ": "आधार",
    "ekaṃ mahābhūtaṃ": "एक महाभूत",
    "tayo mahābhūte": "तीन महाभूतों",
    "dve mahābhūte": "दो महाभूतों",
    "mahābhūte": "महाभूतों",
    "bāhiraṃ ekaṃ mahābhūtaṃ": "एक बाह्य महाभूत",
    "āhārasamuṭṭhānaṃ ekaṃ mahābhūtaṃ": "आहार से उत्पन्न एक महाभूत",
    "utusamuṭṭhānaṃ ekaṃ mahābhūtaṃ": "तापमान से उत्पन्न एक महाभूत",
    "asaññasattānaṃ ekaṃ mahābhūtaṃ": "पहचान-रहित प्राणियों में एक महाभूत",
    "bāhire mahābhūte": "बाह्य महाभूतों",
    "āhārasamuṭṭhāne mahābhūte": "आहार से उत्पन्न महाभूतों",
    "utusamuṭṭhāne mahābhūte": "तापमान से उत्पन्न महाभूतों",
    "asaññasattānaṃ mahābhūte": "पहचान-रहित प्राणियों में महाभूतों",
}
for _x, _h in ACC.items():
    SUBJ_P[_x + " dhammaṃ"] = _h

PREFIX = {
    "arūpe": "अभौतिक लोक में",
    "paṭisandhikkhaṇe": "पुनर्जन्म के क्षण में",
    "ahetukapaṭisandhikkhaṇe": "मूल से रहित पुनर्जन्म के क्षण में",
}

RUPA_CITTA = "मन से उत्पन्न भौतिक रूप"          # cittasamuṭṭhānaṃ rūpaṃ
RUPA_KATATTA = "किए गए कर्म से उत्पन्न भौतिक रूप"  # kaṭattārūpaṃ / kaṭattā ca rūpaṃ
RUPA_UPADA = "व्युत्पन्न भौतिक रूप"              # upādārūpaṃ

OBJ_P = {  # what arises (nominative)
    "tayo khandhā": "तीन समूह",
    "eko khandho": "एक समूह",
    "dve khandhā": "दो समूह",
    "khandhā": "समूह",
    "vatthu": "आधार",
    "cittasamuṭṭhānaṃ rūpaṃ": RUPA_CITTA,
    "kaṭattārūpaṃ": RUPA_KATATTA,
    "upādārūpaṃ": RUPA_UPADA,
    "cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ": f"{RUPA_CITTA}, {RUPA_KATATTA} और {RUPA_UPADA}",
    "cittasamuṭṭhānaṃ rūpaṃ upādārūpaṃ": f"{RUPA_CITTA} और {RUPA_UPADA}",
    "kaṭattārūpaṃ upādārūpaṃ": f"{RUPA_KATATTA} और {RUPA_UPADA}",
    "tayo mahābhūtā": "तीन महाभूत",
    "ekaṃ mahābhūtaṃ": "एक महाभूत",
    "dve mahābhūtā": "दो महाभूत",
    "vicikicchāsahagato uddhaccasahagato moho": "संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह",
    "kusalā cetanā": "हितकर इरादा",
    "akusalā cetanā": "हानिकर इरादा",
    "kiriyābyākatā cetanā": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित इरादा",
    "rūpajīvitindriyaṃ": "भौतिक जीवन-क्षमता",
}
OBJ_SUFFIX = {
    " cittasamuṭṭhānañca rūpaṃ": " और " + RUPA_CITTA,
    " kaṭattā ca rūpaṃ": " और " + RUPA_KATATTA,
    " vatthu ca": " और आधार",
}
for _o, _h in list(OBJ_P.items()):
    if _o in ("tayo khandhā", "eko khandho", "dve khandhā"):
        for _s, _sh in OBJ_SUFFIX.items():
            OBJ_P[_o + _s] = _h + _sh

# short ablative sentences: "Vatthuṃ purejātapaccayā." / "Khandhā vatthuṃ vippayuttapaccayā."
SHORT_ON = {"vatthuṃ": "आधार", "khandhe": "समूहों"}
SHORT_SUBJ = {"khandhā": "समूह", "cittasamuṭṭhānaṃ rūpaṃ": RUPA_CITTA, "kaṭattārūpaṃ": RUPA_KATATTA,
              "vatthu": "आधार"}

# ---------------------------------------------------------------- 5. definition / pañhāvāra frame

# "<SUBJ> <DAT> <X>paccayena paccayo" = "<SUBJ> <DAT> <X-कारण> के रूप में कारण होता है"
SUBJ = {
    "hetū": ("मूल,", "mp"),
    "rūpāyatanaṃ": ("दृश्य रूप का इंद्रिय-क्षेत्र", "ms"),
    "saddāyatanaṃ": ("ध्वनि का इंद्रिय-क्षेत्र", "ms"),
    "gandhāyatanaṃ": ("गंध का इंद्रिय-क्षेत्र", "ms"),
    "rasāyatanaṃ": ("स्वाद का इंद्रिय-क्षेत्र", "ms"),
    "phoṭṭhabbāyatanaṃ": ("स्पर्श का इंद्रिय-क्षेत्र", "ms"),
    "rūpāyatanaṃ saddāyatanaṃ gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ":
        ("दृश्य रूप का इंद्रिय-क्षेत्र, ध्वनि का इंद्रिय-क्षेत्र, गंध का इंद्रिय-क्षेत्र, स्वाद का इंद्रिय-क्षेत्र और स्पर्श का इंद्रिय-क्षेत्र", "mp"),
    "sabbe dhammā": ("सभी परिघटनाएँ", "fp"),
    "te te dhammā": ("वे-वे परिघटनाएँ", "fp"),
    # after «yaṃ yaṃ dhammaṃ …» the Hindi correlative is singular, so that it points back to the object, not to «जो-जो»
    "te te dhammā§sg": ("वह-वह परिघटना", "fs"),
    "chandādhipati": ("प्रधान बनी हुई चाह,", "fs"),
    "vīriyādhipati": ("प्रधान बना हुआ उत्साह,", "ms"),
    "cittādhipati": ("प्रधान बना हुआ मन,", "ms"),
    "vīmaṃsādhipati": ("प्रधान बनी हुई जाँच-परख,", "fs"),
    "cakkhuviññāṇadhātu taṃsampayuttakā ca dhammā": ("आँख की चेतना का तत्व और उससे जुड़ी परिघटनाएँ", "fp"),
    "sotaviññāṇadhātu taṃsampayuttakā ca dhammā": ("कान की चेतना का तत्व और उससे जुड़ी परिघटनाएँ", "fp"),
    "ghānaviññāṇadhātu taṃsampayuttakā ca dhammā": ("नाक की चेतना का तत्व और उससे जुड़ी परिघटनाएँ", "fp"),
    # spelling slip ghāṇa- in ^7-1-5, rendered as meant
    "ghāṇaviññāṇadhātu taṃsampayuttakā ca dhammā": ("नाक की चेतना का तत्व और उससे जुड़ी परिघटनाएँ", "fp"),
    "jivhāviññāṇadhātu taṃsampayuttakā ca dhammā": ("जीभ की चेतना का तत्व और उससे जुड़ी परिघटनाएँ", "fp"),
    "kāyaviññāṇadhātu taṃsampayuttakā ca dhammā": ("शरीर की चेतना का तत्व और उससे जुड़ी परिघटनाएँ", "fp"),
    "manodhātu taṃsampayuttakā ca dhammā": ("मन का तत्व और उससे जुड़ी परिघटनाएँ", "fp"),
    "purimā purimā kusalā dhammā": ("पहले-पहले की हितकर परिघटनाएँ", "fp"),
    "purimā purimā akusalā dhammā": ("पहले-पहले की हानिकर परिघटनाएँ", "fp"),
    "purimā purimā abyākatā dhammā": ("पहले-पहले की नैतिक रूप से अनिर्धारित परिघटनाएँ", "fp"),
    "purimā purimā kiriyābyākatā dhammā": ("पहले-पहले की केवल क्रिया रूपी नैतिक रूप से अनिर्धारित परिघटनाएँ", "fp"),
    "cattāro khandhā arūpino": ("चार अभौतिक समूह", "mp"),
    "cattāro mahābhūtā": ("चार महाभूत", "mp"),
    "okkantikkhaṇe nāmarūpaṃ": ("गर्भ में उतरने के क्षण में मानसिक पक्ष और भौतिक रूप", "mp"),
    "cittacetasikā dhammā": ("मन और मन की सहचर परिघटनाएँ", "fp"),
    "mahābhūtā": ("महाभूत", "mp"),
    "rūpino dhammā": ("भौतिक परिघटनाएँ", "fp"),
    "arūpino dhammā": ("अभौतिक परिघटनाएँ", "fp"),
    "cakkhāyatanaṃ": ("आँख का इंद्रिय-क्षेत्र", "ms"),
    "sotāyatanaṃ": ("कान का इंद्रिय-क्षेत्र", "ms"),
    "ghānāyatanaṃ": ("नाक का इंद्रिय-क्षेत्र", "ms"),
    "jivhāyatanaṃ": ("जीभ का इंद्रिय-क्षेत्र", "ms"),
    "kāyāyatanaṃ": ("शरीर का इंद्रिय-क्षेत्र", "ms"),
    "taṃ rūpaṃ": ("वह भौतिक रूप", "ms"),
    "utubhojanampi": ("तापमान और भोजन भी", "mp"),
    "puggalopi": ("व्यक्ति भी", "ms"),
    "senāsanampi": ("निवास-स्थान भी", "ms"),
    "pacchājātā cittacetasikā dhammā": ("बाद में उत्पन्न मन और मन की सहचर परिघटनाएँ", "fp"),
    "kusalākusalaṃ kammaṃ": ("हितकर और हानिकर कर्म,", "ms"),
    "cetanā": ("इरादा", "ms"),
    "vipākā cattāro khandhā arūpino": ("कर्म-फल रूपी चार अभौतिक समूह", "mp"),
    "kabaḷīkāro āhāro": ("कौर-कौर खाया जाने वाला भोजन", "ms"),
    "arūpino āhārā": ("अभौतिक आहार", "mp"),
    "cakkhundriyaṃ": ("आँख की क्षमता", "fs"),
    "sotindriyaṃ": ("कान की क्षमता", "fs"),
    "ghānindriyaṃ": ("नाक की क्षमता", "fs"),
    "jivhindriyaṃ": ("जीभ की क्षमता", "fs"),
    "kāyindriyaṃ": ("शरीर की क्षमता", "fs"),
    "rūpajīvitindriyaṃ": ("भौतिक जीवन-क्षमता", "fs"),
    "arūpino indriyā": ("अभौतिक क्षमताएँ", "fp"),
    "jhānaṅgāni": ("ध्यान के अंग", "mp"),
    "maggaṅgāni": ("मार्ग के अंग", "mp"),
    "samanantaraniruddhā cittacetasikā dhammā": ("बिलकुल ठीक पहले समाप्त हो चुके मन और मन की सहचर परिघटनाएँ", "fp"),
    "samanantaravigatā cittacetasikā dhammā": ("बिलकुल ठीक पहले विलीन हो चुके मन और मन की सहचर परिघटनाएँ", "fp"),
    # pañhāvāra
    "kusalo dhammo": ("हितकर परिघटना,", "fs"),
    "akusalo dhammo": ("हानिकर परिघटना,", "fs"),
    "abyākato dhammo": ("नैतिक रूप से अनिर्धारित परिघटना,", "fs"),
    "kusalā hetū": ("हितकर मूल", "mp"),
    "akusalā hetū": ("हानिकर मूल", "mp"),
    "vipākābyākatā kiriyābyākatā hetū": ("कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मूल", "mp"),
    "vipākābyākatā hetū": ("कर्म-फल रूपी नैतिक रूप से अनिर्धारित मूल", "mp"),
    "ākāsānañcāyatanakusalaṃ": ("अनंत आकाश के क्षेत्र का हितकर मन,", "ms"),
    "ākiñcaññāyatanakusalaṃ": ("कुछ भी न होने के क्षेत्र का हितकर मन,", "ms"),
    "ākāsānañcāyatanakiriyaṃ": ("अनंत आकाश के क्षेत्र का केवल क्रिया रूपी मन,", "ms"),
    "ākiñcaññāyatanakiriyaṃ": ("कुछ भी न होने के क्षेत्र का केवल क्रिया रूपी मन,", "ms"),
    "kusalā khandhā": ("हितकर समूह", "mp"),
    "akusalā khandhā": ("हानिकर समूह", "mp"),
    "abyākatā khandhā": ("नैतिक रूप से अनिर्धारित समूह", "mp"),
    "nibbānaṃ": ("निर्वाण", "ms"),
    "kusalādhipati": ("हितकर प्रधानता", "fs"),
    "akusalādhipati": ("हानिकर प्रधानता", "fs"),
    "vipākābyākatakiriyābyākatādhipati": ("कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित प्रधानता", "fs"),
}

AND_ASSOC = "और उससे जुड़ी परिघटनाओं के लिए"            # taṃsampayuttakānañca dhammānaṃ
AND_PRODUCED = "और उनसे उत्पन्न भौतिक रूपों के लिए"      # taṃsamuṭṭhānānañca rūpānaṃ
DHATU_DAT = {  # X-dhātuyā (dative)
    "cakkhuviññāṇadhātuyā": "आँख की चेतना के तत्व के लिए",
    "sotaviññāṇadhātuyā": "कान की चेतना के तत्व के लिए",
    "ghānaviññāṇadhātuyā": "नाक की चेतना के तत्व के लिए",
    "jivhāviññāṇadhātuyā": "जीभ की चेतना के तत्व के लिए",
    "kāyaviññāṇadhātuyā": "शरीर की चेतना के तत्व के लिए",
    "manodhātuyā": "मन के तत्व के लिए",
    "manoviññāṇadhātuyā": "मन की चेतना के तत्व के लिए",
}
NANA = {  # the knowledges (genitive/dative)
    "iddhividhañāṇassa": "अलौकिक शक्तियों के ज्ञान",
    "cetopariyañāṇassa": "दूसरों के मन को जानने के ज्ञान",
    "pubbenivāsānussatiñāṇassa": "पूर्व जन्मों के अनुस्मरण के ज्ञान",
    "yathākammūpagañāṇassa": "प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान",
    "anāgataṃsañāṇassa": "भविष्य को जानने के ज्ञान",
    "āvajjanāya": "मन को विषय की ओर मोड़ने",
    "gotrabhussa": "गोत्र-परिवर्तन",
    "vodānassa": "शुद्धि",
    "maggassa": "मार्ग",
}


def dat_list(pali):
    """A list of 3+ datives (with or without commas in the Pāli): 'A, B और C के लिए'."""
    hs = [NANA[w] for w in re.split(r",? ", pali)]
    return ", ".join(hs[:-1]) + " और " + hs[-1] + " के लिए"


DAT = {
    "hetusampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ": "मूलों से जुड़ी परिघटनाओं के लिए " + AND_PRODUCED,
    "sampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ": "जुड़ी हुई परिघटनाओं के लिए " + AND_PRODUCED,
    "chandasampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ": "चाह से जुड़ी परिघटनाओं के लिए " + AND_PRODUCED,
    "vīriyasampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ": "उत्साह से जुड़ी परिघटनाओं के लिए " + AND_PRODUCED,
    "cittasampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ": "मन से जुड़ी परिघटनाओं के लिए " + AND_PRODUCED,
    "vīmaṃsasampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ": "जाँच-परख से जुड़ी परिघटनाओं के लिए " + AND_PRODUCED,
    "jhānasampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ": "ध्यान से जुड़ी परिघटनाओं के लिए " + AND_PRODUCED,
    "maggasampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ": "मार्ग से जुड़ी परिघटनाओं के लिए " + AND_PRODUCED,
    "tesaṃ tesaṃ dhammānaṃ": "उन-उन परिघटनाओं के लिए",
    "pacchimānaṃ pacchimānaṃ kusalānaṃ dhammānaṃ": "बाद-बाद की हितकर परिघटनाओं के लिए",
    "pacchimānaṃ pacchimānaṃ akusalānaṃ dhammānaṃ": "बाद-बाद की हानिकर परिघटनाओं के लिए",
    "pacchimānaṃ pacchimānaṃ abyākatānaṃ dhammānaṃ": "बाद-बाद की नैतिक रूप से अनिर्धारित परिघटनाओं के लिए",
    "pacchimānaṃ pacchimānaṃ kiriyābyākatānaṃ dhammānaṃ": "बाद-बाद की केवल क्रिया रूपी नैतिक रूप से अनिर्धारित परिघटनाओं के लिए",
    "pacchimānaṃ pacchimānaṃ kusalānaṃ dhammānaṃ kesañci": "बाद-बाद की कुछ हितकर परिघटनाओं के लिए",
    "pacchimānaṃ pacchimānaṃ akusalānaṃ dhammānaṃ kesañci": "बाद-बाद की कुछ हानिकर परिघटनाओं के लिए",
    "aññamaññaṃ": "एक-दूसरे के लिए",
    "cittasamuṭṭhānānaṃ rūpānaṃ": "मन से उत्पन्न भौतिक रूपों के लिए",
    "upādārūpānaṃ": "व्युत्पन्न भौतिक रूपों के लिए",
    "arūpīnaṃ dhammānaṃ": "अभौतिक परिघटनाओं के लिए",
    "rūpīnaṃ dhammānaṃ": "भौतिक परिघटनाओं के लिए",
    "manodhātuyā ca manoviññāṇadhātuyā ca taṃsampayuttakānañca dhammānaṃ":
        "मन के तत्व के लिए, मन की चेतना के तत्व के लिए और उनसे जुड़ी परिघटनाओं के लिए",
    "purejātassa imassa kāyassa": "पहले उत्पन्न इस शरीर के लिए",
    "imassa kāyassa": "इस शरीर के लिए",
    "vipākānaṃ khandhānaṃ kaṭattā ca rūpānaṃ": "कर्म-फल रूपी समूहों के लिए और किए गए कर्म से उत्पन्न भौतिक रूपों के लिए",
    "kaṭattārūpānaṃ": "किए गए कर्म से उत्पन्न भौतिक रूपों के लिए",
    "paṭuppannānaṃ cittacetasikānaṃ dhammānaṃ": "वर्तमान मन और मन की सहचर परिघटनाओं के लिए",
    # pañhāvāra
    "sampayuttakānaṃ khandhānaṃ": "जुड़े हुए समूहों के लिए",
    "sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ": "जुड़े हुए समूहों के लिए और मन से उत्पन्न भौतिक रूपों के लिए",
    "sampayuttakānaṃ khandhānaṃ kaṭattā ca rūpānaṃ": "जुड़े हुए समूहों के लिए और किए गए कर्म से उत्पन्न भौतिक रूपों के लिए",
    "viññāṇañcāyatanakusalassa": "अनंत चेतना के क्षेत्र के हितकर मन के लिए",
    "nevasaññānāsaññāyatanakusalassa": "न पहचान न अ-पहचान के क्षेत्र के हितकर मन के लिए",
    "viññāṇañcāyatanavipākassa ca, kiriyassa ca": "अनंत चेतना के क्षेत्र के कर्म-फल रूपी मन के लिए और केवल क्रिया रूपी मन के लिए",
    "nevasaññānāsaññāyatanavipākassa ca, kiriyassa ca":
        "न पहचान न अ-पहचान के क्षेत्र के कर्म-फल रूपी मन के लिए और केवल क्रिया रूपी मन के लिए",
    "viññāṇañcāyatanakiriyassa": "अनंत चेतना के क्षेत्र के केवल क्रिया रूपी मन के लिए",
    "nevasaññānāsaññāyatanakiriyassa": "न पहचान न अ-पहचान के क्षेत्र के केवल क्रिया रूपी मन के लिए",
    "cakkhuviññāṇassa": "आँख की चेतना के लिए",
    "kāyaviññāṇassa": "शरीर की चेतना के लिए",
    "phalassa": "फल के लिए",
    "phalassa āvajjanāya": "फल के लिए और मन को विषय की ओर मोड़ने के लिए",
}
for _d, _h in DHATU_DAT.items():
    DAT[_d + " taṃsampayuttakānañca dhammānaṃ"] = _h + " " + AND_ASSOC
DAT.update(DAT_ITEM)
for _l in ["iddhividhañāṇassa cetopariyañāṇassa pubbenivāsānussatiñāṇassa yathākammūpagañāṇassa anāgataṃsañāṇassa",
           "cetopariyañāṇassa, pubbenivāsānussatiñāṇassa, yathākammūpagañāṇassa, anāgataṃsañāṇassa, āvajjanāya",
           "cetopariyañāṇassa, pubbenivāsānussatiñāṇassa, yathākammūpagañāṇassa anāgataṃsañāṇassa",
           "cetopariyañāṇassa pubbenivāsānussatiñāṇassa yathākammūpagañāṇassa anāgataṃsañāṇassa āvajjanāya",
           "iddhividhañāṇassa, cetopariyañāṇassa, pubbenivāsānussatiñāṇassa, anāgataṃsañāṇassa, āvajjanāya",
           "iddhividhañāṇassa cetopariyañāṇassa pubbenivāsānussatiñāṇassa anāgataṃsañāṇassa",
           "gotrabhussa vodānassa maggassa",
           "gotrabhussa, vodānassa, maggassa"]:
    DAT[_l] = dat_list(_l)

KINCI_KALE = "किसी समय"  # kiñci kāle

# ---------------------------------------------------------------- 6. other clauses (dict, lowercase Pāli)

ANICCA = "अनित्य, दुःख और आत्मा से रहित के रूप में"   # aniccato dukkhato anattato
VIPASSATI = {"s": "अंतर्दृष्टि से देखता है", "p": "अंतर्दृष्टि से देखते हैं"}
REVIEW = {"s": "पुनः विचार करता है", "p": "पुनः विचार करते हैं"}   # paccavekkhati / -nti
GIFT = "दान देकर, सदाचार ग्रहण करके, उपवास-व्रत का पालन करके"      # dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā
SAVOURS = "रस लेता है, {p} आनंद लेता है"                           # assādeti abhinandati
SEKKHA = "सीखने के चरण वाले व्यक्ति"
SEKKHA_PUTHU = "सीखने के चरण वाले या साधारण व्यक्ति"
CETOPARIYA = "दूसरों के मन को जानने के ज्ञान से"
DEEDS = "पहले भली-भाँति किए गए कार्यों"                             # pubbe suciṇṇāni
KILESA = {"pahīne": "छोड़े जा चुके मन के क्लेशों", "vikkhambhite": "दबाए जा चुके मन के क्लेशों",
          "pubbe samudāciṇṇe": "पहले बार-बार उठे मन के क्लेशों"}
ARAHA = "अर्हत्"
UNWHOLE_ARISING = {  # rāgo / diṭṭhi / vicikicchā / uddhaccaṃ / domanassaṃ uppajjati
    "rāgo": "राग उत्पन्न होता है", "diṭṭhi": "दृष्टि उत्पन्न होती है", "vicikicchā": "संशय उत्पन्न होता है",
    "uddhaccaṃ": "बेचैनी उत्पन्न होती है", "domanassaṃ": "उदासी उत्पन्न होती है",
}
OBJ_NOUN = {"rāgaṃ": "राग", "diṭṭhiṃ": "दृष्टि", "vicikicchaṃ": "संशय", "uddhaccaṃ": "बेचैनी", "domanassaṃ": "उदासी",
            "cakkhuṃ": "आँख", "kusalaṃ": "हितकर", "akusalaṃ": "हानिकर", "phalaṃ": "फल", "nibbānaṃ": "निर्वाण",
            "jhānaṃ": "ध्यान", "maggaṃ": "मार्ग", "gotrabhuṃ": "गोत्र-परिवर्तन", "vodānaṃ": "शुद्धि",
            "taṃ": "उस", "vipākābyākate kiriyābyākate khandhe": "कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूहों"}
VIPAKA_TADARAMMANA = "कर्म-फल उसी विषय को लेकर उत्पन्न होता है"   # vipāko tadārammaṇatā uppajjati

CLAUSE = {
    # 1-00
    "yaṃ yaṃ dhammaṃ ārabbha ye ye dhammā uppajjanti cittacetasikā dhammā":
        "जिस-जिस परिघटना को विषय बनाकर जो-जो परिघटनाएँ उत्पन्न होती हैं, यानी मन और मन की सहचर परिघटनाएँ",
    "yaṃ yaṃ dhammaṃ garuṃ katvā ye ye dhammā uppajjanti cittacetasikā dhammā":
        "जिस-जिस परिघटना को महत्व देकर जो-जो परिघटनाएँ उत्पन्न होती हैं, यानी मन और मन की सहचर परिघटनाएँ",
    "yesaṃ yesaṃ dhammānaṃ anantarā ye ye dhammā uppajjanti cittacetasikā dhammā":
        "जिन-जिन परिघटनाओं के ठीक बाद जो-जो परिघटनाएँ उत्पन्न होती हैं, यानी मन और मन की सहचर परिघटनाएँ",
    "yesaṃ yesaṃ dhammānaṃ samanantarā ye ye dhammā uppajjanti cittacetasikā dhammā":
        "जिन-जिन परिघटनाओं के बिलकुल ठीक बाद जो-जो परिघटनाएँ उत्पन्न होती हैं, यानी मन और मन की सहचर परिघटनाएँ",
    "yaṃ rūpaṃ nissāya manodhātu ca manoviññāṇadhātu ca vattanti":
        "जिस भौतिक रूप के आश्रय से मन का तत्व और मन की चेतना का तत्व क्रियाशील होते हैं",
    "paccayaniddeso": "कारणों की व्याख्या",
    "hetupaccayavāro": "मूल-कारण का खंड",
    "ekamūlakaṃ": "एक कारण वाली शृंखला",
    "dumūlakaṃ": "दो कारणों वाली शृंखला",
    "timūlakaṃ": "तीन कारणों वाली शृंखला",
    "catumūlakaṃ": "चार कारणों वाली शृंखला",
    "hetumūlakaṃ": MULAKA["hetu"],
    "pucchāvāro": "पूछताछ का खंड",
    "niddesavāre tevīsatipaccayā": "व्याख्या के खंड में तेईस कारण",
    # 1-01 a
    "tīṇi": "तीन",
    "anulomaṃ": "सकारात्मक क्रम",
    "gaṇanā hetumūlakā": "मूल-कारण से शुरू होने वाली गणना",
    "bāhiraṃ": "बाह्य",
    "āhārasamuṭṭhānaṃ": "आहार से उत्पन्न",
    "utusamuṭṭhānaṃ": "तापमान से उत्पन्न",
    # 1-01 b
    "ārammaṇādhipati": "विषय रूपी प्रधानता",
    "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā": GIFT,
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ paccavekkhati": f"{GIFT} उस पर {REVIEW['s']}",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ assādeti abhinandati":
        f"{GIFT} उसका " + SAVOURS.format(p="उसमें"),
    "pubbe suciṇṇāni paccavekkhati": f"{DEEDS} पर {REVIEW['s']}",
    "pubbe suciṇṇāni assādeti abhinandati": f"{DEEDS} का " + SAVOURS.format(p="उनमें"),
    "jhānā vuṭṭhahitvā jhānaṃ paccavekkhati": f"ध्यान से उठकर ध्यान पर {REVIEW['s']}",
    "jhānā vuṭṭhahitvā jhānaṃ assādeti abhinandati": "ध्यान से उठकर ध्यान का " + SAVOURS.format(p="उसमें"),
    "sekkhā gotrabhuṃ paccavekkhanti": f"{SEKKHA} गोत्र-परिवर्तन पर {REVIEW['p']}",
    "vodānaṃ paccavekkhanti": f"शुद्धि पर {REVIEW['p']}",
    "sekkhā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": f"{SEKKHA} मार्ग से उठकर मार्ग पर {REVIEW['p']}",
    "arahā maggā vuṭṭhahitvā maggaṃ paccavekkhati": f"{ARAHA} मार्ग से उठकर मार्ग पर {REVIEW['s']}",
    "arahā phalaṃ paccavekkhati": f"{ARAHA} फल पर {REVIEW['s']}",
    "nibbānaṃ paccavekkhati": f"निर्वाण पर {REVIEW['s']}",
    "sekkhā phalaṃ paccavekkhanti": f"{SEKKHA} फल पर {REVIEW['p']}",
    "nibbānaṃ paccavekkhanti": f"निर्वाण पर {REVIEW['p']}",
    "sekkhā pahīne kilese paccavekkhanti": f"{SEKKHA} {KILESA['pahīne']} पर {REVIEW['p']}",
    "vikkhambhite kilese paccavekkhanti": f"{KILESA['vikkhambhite']} पर {REVIEW['p']}",
    "pubbe samudāciṇṇe kilese jānanti": f"{KILESA['pubbe samudāciṇṇe']} को जानते हैं",
    "arahā pahīne kilese paccavekkhati": f"{ARAHA} {KILESA['pahīne']} पर {REVIEW['s']}",
    "pubbe samudāciṇṇe kilese jānāti": f"{KILESA['pubbe samudāciṇṇe']} को जानता है",
    "sekkhā vā puthujjanā vā kusalaṃ aniccato dukkhato anattato vipassanti":
        f"{SEKKHA_PUTHU} हितकर को {ANICCA} {VIPASSATI['p']}",
    "sekkhā vā puthujjanā vā akusalaṃ aniccato dukkhato anattato vipassanti":
        f"{SEKKHA_PUTHU} हानिकर को {ANICCA} {VIPASSATI['p']}",
    # vippassati / vippassanti: spelling slips for vipassati / vipassanti, rendered as meant
    "kusalaṃ aniccato dukkhato anattato vippassati": f"हितकर को {ANICCA} {VIPASSATI['s']}",
    "akusalaṃ aniccato dukkhato anattato vipassati": f"हानिकर को {ANICCA} {VIPASSATI['s']}",
    "arahā cakkhuṃ aniccato dukkhato anattato vipassati": f"{ARAHA} आँख को {ANICCA} {VIPASSATI['s']}",
    "sekkhā vā puthujjanā vā cakkhuṃ aniccato dukkhato anattato vippassanti":
        f"{SEKKHA_PUTHU} आँख को {ANICCA} {VIPASSATI['p']}",
    "vipākābyākate kiriyābyākate khandhe aniccato dukkhato anattato vipassati":
        f"{OBJ_NOUN['vipākābyākate kiriyābyākate khandhe']} को {ANICCA} {VIPASSATI['s']}",
    "vipākābyākate kiriyābyākate khandhe aniccato dukkhato anattato vipassanti":
        f"{OBJ_NOUN['vipākābyākate kiriyābyākate khandhe']} को {ANICCA} {VIPASSATI['p']}",
    "cetopariyañāṇena kusalacittasamaṅgissa cittaṃ jānanti": f"{CETOPARIYA} हितकर मन से युक्त व्यक्ति के मन को जानते हैं",
    "cetopariyañāṇena kusalacittasamaṅgissa cittaṃ jānāti": f"{CETOPARIYA} हितकर मन से युक्त व्यक्ति के मन को जानता है",
    "cetopariyañāṇena akusalacittasamaṅgissa cittaṃ jānanti": f"{CETOPARIYA} हानिकर मन से युक्त व्यक्ति के मन को जानते हैं",
    "cetopariyañāṇena akusalacittasamaṅgissa cittaṃ jānāti": f"{CETOPARIYA} हानिकर मन से युक्त व्यक्ति के मन को जानता है",
    "cetopariyañāṇena vipākābyākatakiriyābyākatacittasamaṅgissa cittaṃ jānāti":
        f"{CETOPARIYA} कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन से युक्त व्यक्ति के मन को जानता है",
    "cetopariyañāṇena vipākābyākatakiriyābyākatacittasamaṅgissa cittaṃ jānanti":
        f"{CETOPARIYA} कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन से युक्त व्यक्ति के मन को जानते हैं",
    "taṃ ārabbha rāgo uppajjati": "उसे विषय बनाकर " + UNWHOLE_ARISING["rāgo"],
    "vicikicchaṃ ārabbha vicikicchā uppajjati": "संशय को विषय बनाकर " + UNWHOLE_ARISING["vicikicchā"],
    "uddhaccaṃ ārabbha uddhaccaṃ uppajjati": "बेचैनी को विषय बनाकर " + UNWHOLE_ARISING["uddhaccaṃ"],
    "domanassaṃ ārabbha domanassaṃ uppajjati": "उदासी को विषय बनाकर " + UNWHOLE_ARISING["domanassaṃ"],
    "jhāne parihīne vippaṭisārissa domanassaṃ uppajjati":
        "ध्यान के छूट जाने पर ग्लानि से भरे व्यक्ति में " + UNWHOLE_ARISING["domanassaṃ"],
    "kusale niruddhe vipāko tadārammaṇatā uppajjati": "हितकर के समाप्त होने पर " + VIPAKA_TADARAMMANA,
    "akusale niruddhe vipāko tadārammaṇatā uppajjati": "हानिकर के समाप्त होने पर " + VIPAKA_TADARAMMANA,
    "taṃ garuṃ katvā paccavekkhati": f"उसे महत्व देकर {REVIEW['s']}",
    "pubbe suciṇṇāni garuṃ katvā paccavekkhati": f"{DEEDS} को महत्व देकर {REVIEW['s']}",
    "jhānā vuṭṭhahitvā jhānaṃ garuṃ katvā paccavekkhati": f"ध्यान से उठकर ध्यान को महत्व देकर {REVIEW['s']}",
    "sekkhā gotrabhuṃ garuṃ katvā paccavekkhanti": f"{SEKKHA} गोत्र-परिवर्तन को महत्व देकर {REVIEW['p']}",
    "vodānaṃ garuṃ katvā paccavekkhanti": f"शुद्धि को महत्व देकर {REVIEW['p']}",
    "sekkhā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti":
        f"{SEKKHA} मार्ग से उठकर मार्ग को महत्व देकर {REVIEW['p']}",
    "arahā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhati": f"{ARAHA} मार्ग से उठकर मार्ग को महत्व देकर {REVIEW['s']}",
    "arahā phalaṃ garuṃ katvā paccavekkhati": f"{ARAHA} फल को महत्व देकर {REVIEW['s']}",
    "nibbānaṃ garuṃ katvā paccavekkhati": f"निर्वाण को महत्व देकर {REVIEW['s']}",
    "sekkhā phalaṃ garuṃ katvā paccavekkhanti": f"{SEKKHA} फल को महत्व देकर {REVIEW['p']}",
    "nibbānaṃ garuṃ katvā paccavekkhanti": f"निर्वाण को महत्व देकर {REVIEW['p']}",
    "taṃ garuṃ katvā assādeti abhinandati": "उसे महत्व देकर उसका " + SAVOURS.format(p="उसमें"),
    "taṃ garuṃ katvā rāgo uppajjati": "उसे महत्व देकर " + UNWHOLE_ARISING["rāgo"],
    "pubbe suciṇṇāni garuṃ katvā assādeti abhinandati": f"{DEEDS} को महत्व देकर उनका " + SAVOURS.format(p="उनमें"),
    "jhānā vuṭṭhahitvā jhānaṃ garuṃ katvā assādeti abhinandati":
        "ध्यान से उठकर ध्यान को महत्व देकर उसका " + SAVOURS.format(p="उसमें"),
    "dibbena cakkhunā rūpaṃ passati": "दिव्य आँख से दृश्य रूप को देखता है",
    "dibbena cakkhunā rūpaṃ passanti": "दिव्य आँख से दृश्य रूप को देखते हैं",
    "dibbāya sotadhātuyā saddaṃ suṇāti": "दिव्य कान के तत्व से ध्वनि को सुनता है",
    "dibbāya sotadhātuyā saddaṃ suṇanti": "दिव्य कान के तत्व से ध्वनि को सुनते हैं",
    "saddāyatanaṃ sotaviññāṇassa": "ध्वनि का इंद्रिय-क्षेत्र कान की चेतना के लिए",
    "gandhāyatanaṃ ghānaviññāṇassa": "गंध का इंद्रिय-क्षेत्र नाक की चेतना के लिए",
    "rasāyatanaṃ jivhāviññāṇassa": "स्वाद का इंद्रिय-क्षेत्र जीभ की चेतना के लिए",
    # elided objects of vipassati / assādeti in the «Sotaṃ… ghānaṃ…» lists
    "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhaṃ": "जीभ", "kāyaṃ": "शरीर", "rūpe": "दृश्य रूपों", "sadde": "ध्वनियों",
    "gandhe": "गंधों", "rase": "स्वादों", "phoṭṭhabbe": "स्पर्शों", "vatthuṃ": "आधार",
}
for _w in ("rāgo", "diṭṭhi", "vicikicchā", "uddhaccaṃ", "domanassaṃ"):
    CLAUSE[_w + " uppajjati"] = UNWHOLE_ARISING[_w]
for _w in ("kusalaṃ", "akusalaṃ", "rāgaṃ", "diṭṭhiṃ", "cakkhuṃ"):
    CLAUSE[_w + " assādeti abhinandati"] = f"{OBJ_NOUN[_w]} का " + SAVOURS.format(p="उसमें")
for _w in ("rāgaṃ", "diṭṭhiṃ", "cakkhuṃ"):
    CLAUSE[_w + " garuṃ katvā assādeti abhinandati"] = f"{OBJ_NOUN[_w]} को महत्व देकर उसका " + SAVOURS.format(p="उसमें")
CLAUSE["vipākābyākate kiriyābyākate khandhe assādeti abhinandati"] = \
    f"{OBJ_NOUN['vipākābyākate kiriyābyākate khandhe']} का " + SAVOURS.format(p="उनमें")
CLAUSE["vipākābyākate kiriyābyākate khandhe garuṃ katvā assādeti abhinandati"] = \
    f"{OBJ_NOUN['vipākābyākate kiriyābyākate khandhe']} को महत्व देकर उनका " + SAVOURS.format(p="उनमें")
for _p, _h in PREFIX.items():
    CLAUSE[_p] = _h
CLAUSE.update(P_NOM)

# ---------------------------------------------------------------- 7. editorial notes (inside the parentheses)

NOTE = {
    "anantarampi samanantarampi ārammaṇapaccayasadisaṃ.":
        f"{NAME['anantara']} और {NAME['samanantara']} भी {SADISA['ārammaṇa']} हैं।",
    "nissayapaccayaṃ sahajātapaccayasadisaṃ.": f"{NAME['nissaya']} {SADISA['sahajāta']} है।",
    "upanissayapaccayaṃ ārammaṇapaccayasadisaṃ.": f"{NAME['upanissaya']} {SADISA['ārammaṇa']} है।",
    "indriyapaccayaṃ kammapaccayasadisaṃ.": f"{NAME['indriya']} {SADISA['kamma']} है।",
    "jhānapaccayampi maggapaccayampi hetupaccayasadisaṃ.": f"{NAME['jhāna']} और {NAME['magga']} भी {SADISA['hetu']} हैं।",
    "sampayuttapaccayaṃ ārammaṇapaccayasadisaṃ.": f"{NAME['sampayutta']} {SADISA['ārammaṇa']} है।",
    "saṅkhitaṃ. atthipaccayaṃ sahajātapaccayasadisaṃ.": f"संक्षिप्त। {NAME['atthi']} {SADISA['sahajāta']} है।",
    "natthipaccayampi vigatapaccayampi ārammaṇapaccayasadisaṃ.":
        f"{NAME['natthi']} और {NAME['vigata']} भी {SADISA['ārammaṇa']} हैं।",
    "avigatapaccayaṃ sahajātapaccayasadisaṃ": f"{NAME['avigata']} {SADISA['sahajāta']} है",
    "ime tevīsatipaccayā sajjhāyantena vitthāretabbā.": "इन तेईस कारणों का पाठ करते हुए विस्तार करना चाहिए।",
    "ārammaṇe ṭhitena sabbattha tīṇeva pañhā.": "विषय-कारण पर टिके रहने पर हर जगह तीन ही प्रश्न हैं।",
    "āsevanamūlake vipākaṃ natthi.": f"{MULAKE['āsevana']} {NAME['vipāka']} नहीं है।",
    "vipākamūlake āsevanaṃ natthi.": f"{MULAKE['vipāka']} {NAME['āsevana']} नहीं है।",
    "ekekaṃ paccayaṃ mūlakaṃ kātūna sajjhāyantena gaṇetabbāti.":
        "हर एक कारण से शुरू होने वाली शृंखला बनाकर पाठ करते हुए गिनना चाहिए।",
    "naanantarapaccayampi nasamanantarapaccayampi naārammaṇapaccayasadisaṃ.":
        f"{NNAME['anantara']} और {NNAME['samanantara']} भी {NSADISA['ārammaṇa']} हैं।",
    "naupanissayapaccayaṃ naārammaṇapaccayasadisaṃ.": f"{NNAME['upanissaya']} {NSADISA['ārammaṇa']} है।",
    "napacchājātapaccayampi naāsevanapaccayampi naadhipatipaccayasadisaṃ.":
        f"{NNAME['pacchājāta']} और {NNAME['āsevana']} भी {NSADISA['adhipati']} हैं।",
    "naārammaṇapaccayasadisaṃ.": f"{NSADISA['ārammaṇa']}।",
    # 1-00
    "yathā hetupaccayo vitthārito, evaṃ ārammaṇapaccayopi vitthāretabbo vācanāmaggena.":
        f"जैसे {NAME['hetu']} का विस्तार किया गया है, वैसे ही {NAME['ārammaṇa']} का भी पाठ के क्रम से विस्तार करना चाहिए।",
    "yathā hetupaccayo vitthārito, evaṃ avigatapaccayopi vitthāretabbo vācanāmaggena.":
        f"जैसे {NAME['hetu']} का विस्तार किया गया है, वैसे ही {NAME['avigata']} का भी पाठ के क्रम से विस्तार करना चाहिए।",
    "pañcamūlakādikā saṃkhittā. ekamūlakaṃ, dumūlakaṃ, timūlakaṃ, catumūlakaṃ, pañcamūlakaṃ, sabbamūlakaṃ asammuyhantena vitthāretabbaṃ.":
        "पाँच कारणों वाली शृंखला आदि संक्षिप्त हैं। एक कारण वाली शृंखला, दो कारणों वाली शृंखला, तीन कारणों वाली शृंखला, "
        "चार कारणों वाली शृंखला, पाँच कारणों वाली शृंखला और सभी कारणों वाली शृंखला का बिना भ्रमित हुए विस्तार करना चाहिए।",
    "ekekassa padassa ekamūlakaṃ, dumūlakaṃ, timūlakaṃ, catumūlakaṃ, pañcamūlakaṃ, sabbamūlakaṃ asammuyhantena vitthāretabbaṃ. ":
        "हर एक पद की एक कारण वाली शृंखला, दो कारणों वाली शृंखला, तीन कारणों वाली शृंखला, चार कारणों वाली शृंखला, "
        "पाँच कारणों वाली शृंखला और सभी कारणों वाली शृंखला का बिना भ्रमित हुए विस्तार करना चाहिए।",
    "yathā anulome hetupaccayo vitthārito, evaṃ paccanīyepi nahetupaccayo vitthāretabbo.":
        f"जैसे सकारात्मक क्रम में {NAME['hetu']} का विस्तार किया गया है, वैसे ही नकारात्मक क्रम में भी "
        f"{NAME['hetu']} के अभाव का विस्तार करना चाहिए।",
    "yathā anulome ekekassa padassa ekamūlakaṃ, dumūlakaṃ, timūlakaṃ, catumūlakaṃ, yāva tevīsatimūlakaṃ evaṃ paccanīyepi vitthāretabbaṃ. ":
        "जैसे सकारात्मक क्रम में हर एक पद की एक कारण वाली शृंखला, दो कारणों वाली शृंखला, तीन कारणों वाली शृंखला, "
        "चार कारणों वाली शृंखला, और इसी तरह तेईस कारणों वाली शृंखला तक है, वैसे ही नकारात्मक क्रम में भी विस्तार करना चाहिए।",
    "yathā anulome hetupaccayo vitthārito, evaṃ anulomapaccanīyepi padaṃ vitthāretabbaṃ.":
        f"जैसे सकारात्मक क्रम में {NAME['hetu']} का विस्तार किया गया है, वैसे ही सकारात्मक-नकारात्मक क्रम में भी "
        "पद का विस्तार करना चाहिए।",
}

# ---------------------------------------------------------------- 8. the "six methods" stanza and hand lines

STANZA_1 = "{s} तीन-तीन के वर्गीकरणों के श्रेष्ठ कारण-संबंध और दो-दो के वर्गीकरणों के उत्तम कारण-संबंध,"
STANZA_2 = "दो-दो के साथ तीन-तीन, और तीन-तीन के साथ दो-दो;"
STANZA_3 = "तीन-तीन के साथ तीन-तीन, और दो-दो के साथ दो-दो,"
STANZA_4 = "{m} में ये छह विधियाँ अत्यंत गहन हैं।"
SIGLA_KA = {"Ka": "क", "Kha": "ख", "Ga": "ग", "Gha": "घ", "Ṅa": "ङ"}
METHOD_LOC = {"anulomamhi": "सकारात्मक क्रम", "paccanīyamhi": "नकारात्मक क्रम",
              "anulomapaccanīyamhi": "सकारात्मक-नकारात्मक क्रम", "paccanīyānulomamhi": "नकारात्मक-सकारात्मक क्रम"}

LINE_HAND = {
    "Dukaṃ tikañceva tikaṃ dukañca;": STANZA_2,
    "Tikaṃ tikañceva dukaṃ dukañca,": STANZA_3,
}
for _p, _h in SIGLA_KA.items():
    LINE_HAND[f"({_p}) tikañca paṭṭhānavaraṃ dukuttamaṃ,"] = STANZA_1.format(s=f"({_h})")
for _p, _h in METHOD_LOC.items():
    LINE_HAND[f"Cha {_p} nayā sugambhīrāti."] = STANZA_4.format(m=_h)

# ^7-1-34, first line: the item list after «…pe…»
LINE_HAND[
    "Siyā kusalaṃ dhammaṃ paṭicca kusalo dhammo uppajjeyya avigatapaccayā…pe… akusalaṃ dhammaṃ paṭicca… "
    "abyākataṃ dhammaṃ paṭicca… kusalañca abyākatañca dhammaṃ paṭicca… akusalañca abyākatañca dhammaṃ paṭicca… "
    "kusalañca akusalañca dhammaṃ paṭicca… kusalañca akusalañca abyākatañca dhammaṃ paṭicca kusalo dhammo uppajjeyya… "
    "akusalo dhammo uppajjeyya… abyākato dhammo uppajjeyya… kusalo ca abyākato ca dhammā uppajjeyyuṃ… "
    "akusalo ca abyākato ca dhammā uppajjeyyuṃ… kusalo ca akusalo ca dhammā uppajjeyyuṃ… "
    "kusalo ca akusalo ca abyākato ca dhammā uppajjeyyuṃ avigatapaccayā."
] = (
    siya_frame("kusalaṃ", "kusalo", "avigatapaccayā") + "… "
    + "… ".join(f"{ACC[x]} {PATICCA}" for x in ["akusalaṃ", "abyākataṃ", "kusalañca abyākatañca",
                                                "akusalañca abyākatañca", "kusalañca akusalañca"])
    + f"… {ACC['kusalañca akusalañca abyākatañca']} {PATICCA} "
    + "… ".join(f"{NOM[y][0]} {MAY_ARISE[NOM[y][1]]}" for y in
                ["kusalo", "akusalo", "abyākato", "kusalo ca abyākato ca", "akusalo ca abyākato ca", "kusalo ca akusalo ca"])
    + f"… {NOM['kusalo ca akusalo ca abyākato ca'][0]} {ABL['avigata']} {MAY_ARISE['p']}?"
)

# ---------------------------------------------------------------- 9. variants {…}

SIGLA = {"ka": "Ka", "sī": "Sī", "syā": "Syā", "kaṃ": "Kaṃ", "pī": "Pī", "i": "I"}
# Pāli variant -> (kind, Hindi anchor after which the bracket goes; "" = before the final «।»)
VARIANTS = {
    "{paccayoti (syā.)}": ("पाठभेद", "कारण होते हैं"),
    "{kañci kālaṃ (syā.)}": ("पाठभेद", KINCI_KALE),
    "{kabaḷiṅkāro (ka. sī. syā.)}": ("वर्तनी-भेद", "खाया जाने वाला"),
    "{pahīnakilese (syā.)}": ("वर्तनी-भेद", KILESA["pahīne"]),
    "{vikkhambhitakilese (syā.)}": ("वर्तनी-भेद", KILESA["vikkhambhite"]),
}


def variant_hi(v, kind):
    m = re.fullmatch(r"\{(.*) \(([^)]*)\)\}", v)
    if not m:
        return f"[पाठभेद: {v[1:-1]}]"
    sig = ", ".join(SIGLA[s.strip().rstrip(".")] + "." for s in m.group(2).split(". ") if s.strip())
    return f"[{kind} ({sig}): {m.group(1)}]"


# ---------------------------------------------------------------- 10. counting lines


def is_count(text):
    toks = [t for t in re.split(r"(…pe…|…|, |; | |\.)", text) if t and t not in ("…pe…", "…", ", ", "; ", " ", ".")]
    words = set(P_ABL) | set(P_NABL) | set(P_LOC) | set(P_NLOC) | set(NUM)
    return bool(toks) and all(t in words for t in toks)


def count_hi(text):
    """Counting / chain-only lines. Ablatives joined by ', ', an ablative before a locative takes ', ',
    locative + number with a space, no comma added where the Pāli has none, '…pe…' -> '…', final '.' -> '।'."""
    text = lower_initials(text)
    toks = [t for t in re.split(r"(…pe…|…|, |; | |\.$)", text) if t]
    out = []
    for i, t in enumerate(toks):
        if t == " ":
            prev = toks[i - 1]
            out.append(", " if prev in P_ABL or prev in P_NABL else " ")
        elif t == "…pe…":
            out.append("…")
        elif t == ".":
            out.append("।")
        elif t in ("…", ", ", "; "):
            out.append(t)
        else:
            for d in (P_ABL, P_NABL, P_LOC, P_NLOC, NUM):
                if t in d:
                    out.append(d[t])
                    break
            else:
                raise KeyError(t)
    return "".join(out)


# ---------------------------------------------------------------- 11. the line translator

ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")
_ALT = lambda d: "|".join(re.escape(k) for k in sorted(d, key=len, reverse=True))
ACC_ALT, NOM_ALT = _ALT(ACC), _ALT(NOM)
SIYA_RE = re.compile(rf"siyā ({ACC_ALT}) dhammaṃ paṭicca ({NOM_ALT}) (?:dhammo uppajjeyya|dhammā uppajjeyyuṃ) "
                     rf"({CHAIN_RE})(…(?=\.))?")
PATICCA_RE = re.compile(rf"(?<!\w)({ACC_ALT}) dhammaṃ paṭicca ({NOM_ALT}) (?:dhammo uppajjati|dhammā uppajjanti) ({CHAIN_RE})")
INS_ALT = "|".join(re.escape(k) for k in sorted(KEYS, key=len, reverse=True))
DEF_RE = re.compile(rf"(?<!\w)(?:({_ALT(SUBJ)}) )?(?:({_ALT(DAT)}) )?(?:(kiñci kāle) )?(na )?({INS_ALT})paccayena paccayo")
PCLAUSE_RE = re.compile(rf"^(?:({_ALT(PREFIX)}) )?({_ALT(SUBJ_P)}) paṭicca(?: ({_ALT(OBJ_P)}))?$")
SHORT_RE = re.compile(rf"^(?:({_ALT(SHORT_SUBJ)}) )?({_ALT(SHORT_ON)}) ({COND_ALT})$")
SLIPS = {"na aññamaññapaccayā": "naaññamaññapaccayā", "adhipati paccayena": "adhipatipaccayena"}


def lower_initials(s):
    return re.sub(r"(?<!\w)([A-ZĀĪŪṄÑṬḌṆḶṂ])", lambda m: m.group(1).lower(), s)


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)(\(\d+\.?\) )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    return f"{hashes} {st}{num or ''}{HEAD[body]}{en}"


def clause(piece):
    core = piece.strip()
    if not core:
        return piece
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    if core in CLAUSE:
        h = CLAUSE[core]
    elif PCLAUSE_RE.match(core):
        pre, subj, obj = PCLAUSE_RE.match(core).groups()
        h = (PREFIX[pre] + " " if pre else "") + f"{SUBJ_P[subj]} {PATICCA}" + (" " + OBJ_P[obj] if obj else "")
    elif SHORT_RE.match(core):
        subj, on, cond = SHORT_RE.match(core).groups()
        h = (SHORT_SUBJ[subj] + " " if subj else "") + f"{SHORT_ON[on]} पर {_cond_word(cond)}"
    else:
        raise KeyError(f"no clause for: {core!r}")
    return lead + h + trail


def translate_line(line):
    """One non-empty Pāli line (block ID removed) -> Hindi."""
    if line.startswith("#"):
        return heading(line)
    if line in LINE_HAND:
        return LINE_HAND[line]
    if line == "Namo tassa bhagavato arahato sammāsambuddhassa":
        return NAMO
    inserts = []
    for v, (kind, anchor) in VARIANTS.items():
        if v in line:
            line = line.replace(" " + v, "")
            inserts.append((anchor, variant_hi(v, kind)))
    if "{" in line:
        raise KeyError(f"unregistered variant in: {line!r}")
    for a, b in SLIPS.items():
        line = line.replace(a, b)
    text = lower_initials(line)
    if text.startswith("yaṃ yaṃ dhammaṃ"):
        text = text.replace(", te te dhammā ", ", te te dhammā§sg ")
    store = []

    def keep(h):
        store.append(h)
        return f"{len(store) - 1}"

    # notes and counts
    text = re.sub(r"\(([^()]*[^\d().][^()]*)\)", lambda m: keep("(" + NOTE[m.group(1)] + ")"), text)
    # counting / chain-only lines (text before the first note)
    head, sep, rest = text.partition("")
    if is_count(head.rstrip(" (")):
        core = head.rstrip(" (")
        return _finish(count_hi(core) + text[len(core):], store)
    # frames
    text = SIYA_RE.sub(lambda m: keep(siya_frame(m.group(1), m.group(2), m.group(3), m.group(4) or "")), text)
    text = PATICCA_RE.sub(lambda m: keep(paticca_frame(*m.groups())), text)
    state = {"g": None}

    def defn(m):
        subj, dat, kinci, neg, k = m.groups()
        parts = []
        if subj:
            sh, state["g"] = SUBJ[subj]
            parts.append(sh)
        if state["g"] is None:
            raise KeyError(f"no subject before: {m.group(0)!r}")
        if dat:
            parts.append(DAT[dat])
        if kinci:
            parts.append(KINCI_KALE)
        parts.append(NINS(k, state["g"]) if neg else INS(k, state["g"]))
        return keep(" ".join(parts))

    text = DEF_RE.sub(defn, text)
    # split the rest into pieces
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
            # placeholders and counts "(3)" pass through; the text between them is a clause
            for part in re.split(r"(\d+|\(\d+\))", tok):
                if not part.strip() or re.fullmatch(r"\d+|\(\d+\)", part):
                    out.append(part)
                else:
                    out.append(clause(part))
    hi = _finish("".join(out), store)
    for anchor, br in inserts:
        if anchor:
            assert anchor in hi, (anchor, hi)
            hi = hi.replace(anchor, anchor + " " + br, 1)
    return hi


def _finish(s, store):
    s = re.sub(r"(\d+)", lambda m: store[int(m.group(1))], s)
    s = s.replace("?।", "?")
    return s


# ---------------------------------------------------------------- 12. file builder

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", ".."))
PALI_DIR = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
OUT_DIR = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters")
SAMPLE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample-1")


def build_file(src, dst):
    lines = open(src, encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        hi = translate_line(body)
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")


def build_all():
    os.makedirs(OUT_DIR, exist_ok=True)
    for name in ("preamble.md", "1-00-paccaya.md"):
        build_file(os.path.join(PALI_DIR, name), os.path.join(OUT_DIR, name))
    for part in ("a", "b"):
        build_file(os.path.join(SAMPLE_DIR, f"1-01-{part}-pali-sample.md"),
                   os.path.join(SAMPLE_DIR, f"1-01-{part}-sample.md"))


if __name__ == "__main__":
    build_all()
    print("built: preamble.md, 1-00-paccaya.md, sample-1/1-01-a-sample.md, sample-1/1-01-b-sample.md")
