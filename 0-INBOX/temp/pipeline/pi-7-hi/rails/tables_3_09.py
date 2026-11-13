"""Tables for build_rails_3-09.py (3-09-mahantaraduka, Hindi plain RAILS)."""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as R  # noqa: E402

# ------------------------------------------------------------------ dyad items ({a} = ा / े / ी agreement)

DYAD_HI = {
    "Sārammaṇadukaṃ": {"P": "विषय वाल{a}", "N": "विषय से रहित"},
    "Cittadukaṃ": {"P": "मन रूपी", "N": "मन रूपी न होने वाल{a}"},
    "Cetasikadukaṃ": {"P": "मन क{a} सहचर", "N": "मन क{a} सहचर न होने वाल{a}"},
    "Cittasampayuttadukaṃ": {"P": "मन से जुड़{a}", "N": "मन से अलग"},
    "Cittasaṃsaṭṭhadukaṃ": {"P": "मन से घुल{a}-मिल{a}", "N": "मन से घुल{a}-मिल{a} न होने वाल{a}"},
    "Cittasamuṭṭhānadukaṃ": {"P": "मन से उत्पन्न", "N": "मन से उत्पन्न न होने वाल{a}"},
    "Cittasahabhūdukaṃ": {"P": "मन के साथ-साथ होने वाल{a}", "N": "मन के साथ-साथ न होने वाल{a}"},
    "Cittānuparivattidukaṃ": {"P": "मन का अनुसरण करने वाल{a}", "N": "मन का अनुसरण न करने वाल{a}"},
    "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ": {"P": "मन से घुल{a}-मिल{a} और मन से उत्पन्न",
                                      "N": "मन से घुल{a}-मिल{a} और मन से उत्पन्न न होने वाल{a}"},
    "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ": {
        "P": "मन से घुल{a}-मिल{a}, मन से उत्पन्न और मन के साथ-साथ होने वाल{a}",
        "N": "मन से घुल{a}-मिल{a}, मन से उत्पन्न और मन के साथ-साथ होने वाल{a} न होने वाल{a}"},
    "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ": {
        "P": "मन से घुल{a}-मिल{a}, मन से उत्पन्न और मन का अनुसरण करने वाल{a}",
        "N": "मन से घुल{a}-मिल{a}, मन से उत्पन्न और मन का अनुसरण करने वाल{a} न होने वाल{a}"},
    "Ajjhattikadukaṃ": {"P": "आंतरिक", "N": "बाह्य"},
    "Upādādukaṃ": {"P": "व्युत्पन्न", "N": "व्युत्पन्न न होने वाल{a}"},
    "Upādinnadukaṃ": {"P": "कर्म से उत्पन्न", "N": "कर्म से उत्पन्न न होने वाल{a}"},
}

# dyad names (harmonise-notes.md §1, binding)
DYAD_NAME = {
    "Sārammaṇadukaṃ": "विषय वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Cittadukaṃ": "मन रूपी परिघटनाओं वाला दो का वर्गीकरण",
    "Cetasikadukaṃ": "मन की सहचर परिघटनाओं वाला दो का वर्गीकरण",
    "Cittasampayuttadukaṃ": "मन से जुड़ी परिघटनाओं वाला दो का वर्गीकरण",
    "Cittasaṃsaṭṭhadukaṃ": "मन से घुली-मिली परिघटनाओं वाला दो का वर्गीकरण",
    "Cittasamuṭṭhānadukaṃ": "मन से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण",
    "Cittasahabhūdukaṃ": "मन के साथ-साथ होने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Cittānuparivattidukaṃ": "मन का अनुसरण करने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ": "मन से घुली-मिली और मन से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण",
    "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ":
        "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ":
        "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Ajjhattikadukaṃ": "आंतरिक परिघटनाओं वाला दो का वर्गीकरण",
    "Upādādukaṃ": "व्युत्पन्न परिघटनाओं वाला दो का वर्गीकरण",
    "Upādinnadukaṃ": "कर्म से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण",
}
CLUSTER = "बीच के बड़े दो-दो के वर्गीकरण"

# ------------------------------------------------------------------ headings

N = R.NAME
HEAD9 = dict(DYAD_NAME)
HEAD9.update({
    "Mahantaradukaṃ": CLUSTER,
    "1-4. Paccayānulomādi": "1-4. कारणों का सकारात्मक क्रम आदि",
    "Sahajātavāro": "सह-उत्पत्ति का खंड",
    "Paccayavāro": "कारण का खंड",
    "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड",
    "Sampayuttavāro": "जुड़ाव का खंड",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Pacchājātāsevanapaccayā": f"{N['pacchājāta']} और {N['āsevana']}",
    "Vipāka-āhārapaccayā": f"{N['vipāka']} और {N['āhāra']}",
    "Vipākāhārapaccayā": f"{N['vipāka']} और {N['āhāra']}",
    "Kamma-vipākapaccayā": f"{N['kamma']} और {N['vipāka']}",
})
for _k in R.KEYS:
    _c = _k[0].upper() + _k[1:]
    HEAD9[_c + "paccayādi"] = f"{N[_k]} आदि"
    _n = ("No" if _k in ("atthi", "natthi", "vigata", "avigata") else "Na") + _k
    HEAD9[_n + "paccayādi"] = f"{R.NNAME[_k]} आदि"

CLOSING9 = {f"{k} niṭṭhitaṃ.": f"{v} समाप्त।" for k, v in DYAD_NAME.items()}
CLOSING9["Mahantaradukaṃ niṭṭhitaṃ."] = f"{CLUSTER} समाप्त।"

# ------------------------------------------------------------------ lexicon for the NP parser


def _n(d, o=None, g="m", n="s", case="nom", complex_=False):
    return {"d": d, "o": o or d, "g": g, "n": n, "case": case, "complex": complex_}


RC, RK, RU = R.RUPA_CITTA, R.RUPA_KATATTA, R.RUPA_UPADA
NOUN = {
    "khandhaṃ": _n("समूह", case="acc"),
    "khandho": _n("समूह"),
    "khandhā": _n("समूह", "समूहों", n="p"),
    "khandhe": _n("समूह", "समूहों", n="p", case="acc"),
    "khandhānaṃ": _n("समूह", "समूहों", n="p", case="dat"),
    "mahābhūtaṃ": _n("महाभूत", case="acc"),
    "mahābhūtā": _n("महाभूत", "महाभूतों", n="p"),
    "mahābhūte": _n("महाभूत", "महाभूतों", n="p", case="acc"),
    "mahābhūtānaṃ": _n("महाभूत", "महाभूतों", n="p", case="dat"),
    "vatthu": _n("आधार"),
    "vatthuṃ": _n("आधार", case="acc"),
    "vatthussa": _n("आधार", case="dat"),
    "cittaṃ": _n("मन", case="acc"),
    "cittassa": _n("मन", case="dat"),
    "cittādhipati": _n("प्रधान बना हुआ मन"),
    "cittasamuṭṭhānaṃ rūpaṃ": _n(RC, case="acc", complex_=True),
    "cittasamuṭṭhānaṃ & rūpaṃ": _n(RC, case="acc", complex_=True),
    "cittasamuṭṭhānānaṃ rūpānaṃ": _n(RC, "मन से उत्पन्न भौतिक रूपों", n="p", case="dat", complex_=True),
    "cittasamuṭṭhānānaṃ & rūpānaṃ": _n(RC, "मन से उत्पन्न भौतिक रूपों", n="p", case="dat", complex_=True),
    "kaṭattā & rūpaṃ": _n(RK, case="acc", complex_=True),
    "kaṭattārūpaṃ": _n(RK, case="acc", complex_=True),
    "kaṭattā & rūpānaṃ": _n(RK, "किए गए कर्म से उत्पन्न भौतिक रूपों", n="p", case="dat", complex_=True),
    "kaṭattārūpānaṃ": _n(RK, "किए गए कर्म से उत्पन्न भौतिक रूपों", n="p", case="dat", complex_=True),
    "upādārūpaṃ": _n(RU, case="acc", complex_=True),
    "upādārūpānaṃ": _n(RU, "व्युत्पन्न भौतिक रूपों", n="p", case="dat", complex_=True),
    "rūpaṃ": _n("भौतिक रूप", case="acc"),
    "cetanā": _n("इरादा", "इरादे"),
    "hetū": _n("मूल", "मूलों", n="p"),
    "moho": _n("मोह"),
    "nibbānaṃ": _n("निर्वाण", case="acc"),
    "kabaḷīkāro āhāro": _n("कौर-कौर खाया जाने वाला भोजन", "कौर-कौर खाए जाने वाले भोजन", complex_=True),
    "imassa kāyassa": _n("इस शरीर", case="dat"),
    "purejātassa imassa kāyassa": _n("पहले उत्पन्न इस शरीर", case="dat"),
    "vuṭṭhānassa": _n("बाहर आने", case="dat"),
    "phalasamāpattiyā": _n("फल की ध्यान-अवस्था", g="f", case="dat"),
    "maggassa": _n("मार्ग", case="dat"),
    "phalassa": _n("फल", case="dat"),
    "gotrabhussa": _n("गोत्र-परिवर्तन", case="dat"),
    "vodānassa": _n("शुद्धि", g="f", case="dat"),
    "āvajjanāya": _n("मन को विषय की ओर मोड़ने", case="dat"),
    "rūpajīvitindriyaṃ": _n("भौतिक जीवन-क्षमता", g="f", case="acc"),
    # upanissaya lists
    "saddhā": _n("श्रद्धा", g="f"),
    "paññā": _n("प्रज्ञा", g="f"),
    "rāgo": _n("राग"),
    "patthanā": _n("कामना", g="f"),
    "kāyikaṃ sukhaṃ": _n("शारीरिक सुख", case="acc"),
    "kāyikaṃ dukkhaṃ": _n("शारीरिक दुःख", case="acc"),
    "sīlaṃ": _n("सदाचार", case="acc"),
    "utu": _n("तापमान"),
    "bhojanaṃ": _n("भोजन", case="acc"),
    "senāsanaṃ": _n("निवास-स्थान", case="acc"),
    "saddhāya": _n("श्रद्धा", g="f", case="dat"),
    "paññāya": _n("प्रज्ञा", g="f", case="dat"),
    "rāgassa": _n("राग", case="dat"),
    "patthanāya": _n("कामना", g="f", case="dat"),
    "kāyikassa sukhassa": _n("शारीरिक सुख", case="dat"),
    "kāyikassa dukkhassa": _n("शारीरिक दुःख", case="dat"),
}
_SENSE = [("cakkhu", "आँख", "cakkh"), ("sota", "कान", "sot"), ("ghāna", "नाक", "ghān"),
          ("jivhā", "जीभ", "jivh"), ("kāya", "शरीर", "kāy")]
for _p, _h, _s in _SENSE:
    NOUN[_p + "viññāṇaṃ"] = _n(f"{_h} की चेतना", g="f", case="acc")
    NOUN[_p + "viññāṇassa"] = _n(f"{_h} की चेतना", g="f", case="dat")
    NOUN[_s + "āyatanaṃ"] = _n(f"{_h} का इंद्रिय-क्षेत्र", f"{_h} के इंद्रिय-क्षेत्र", case="acc")
    NOUN[_s + ("undriyaṃ" if _s == "cakkh" else "indriyaṃ")] = _n(f"{_h} की क्षमता", g="f", case="acc")
for _p, _h in [("rūp", "दृश्य रूप"), ("sadd", "ध्वनि"), ("gandh", "गंध"), ("ras", "स्वाद"), ("phoṭṭhabb", "स्पर्श")]:
    NOUN[_p + "āyatanaṃ"] = _n(f"{_h} का इंद्रिय-क्षेत्र", f"{_h} के इंद्रिय-क्षेत्र", case="acc")
for _k, _h in R.NANA.items():
    if _k.endswith("ñāṇassa"):
        NOUN[_k] = _n(_h, case="dat")
NOUN.update({
    "anulomaṃ": _n("अनुरूपता", g="f"),
    "āhārā": _n("आहार", "आहारों", n="p"),
    "indriyā": _n("क्षमताएँ", "क्षमताओं", g="f", n="p"),
    "upekkhindriyaṃ": _n("समभाव की क्षमता", g="f", case="acc"),
    "sukhindriyaṃ": _n("सुख की क्षमता", g="f", case="acc"),
    "dukkhindriyaṃ": _n("दुःख की क्षमता", g="f", case="acc"),
    "rūpānaṃ": _n("भौतिक रूप", "भौतिक रूपों", n="p", case="dat"),
    "kāyassa": _n("शरीर", case="dat"),
    "ākāsānañcāyatanaṃ": _n("अनंत आकाश का क्षेत्र", "अनंत आकाश के क्षेत्र", case="acc"),
    "ākiñcaññāyatanaṃ": _n("कुछ भी न होने का क्षेत्र", "कुछ भी न होने के क्षेत्र", case="acc"),
    "viññāṇañcāyatanassa": _n("अनंत चेतना का क्षेत्र", "अनंत चेतना के क्षेत्र", case="dat"),
    "nevasaññānāsaññāyatanassa": _n("न पहचान न अ-पहचान का क्षेत्र", "न पहचान न अ-पहचान के क्षेत्र", case="dat"),
    "kusalākusalaṃ kammaṃ": _n("हितकर और हानिकर कर्म", case="acc"),
    "pañcaviññāṇaṃ": _n("पाँच प्रकार की चेतना", g="f", case="acc"),
    "bhavaṅgaṃ": _n("जीवन-धारा", g="f", case="acc"),
    "āvajjanā": _n("मन को विषय की ओर मोड़ना"),
    "pañcannaṃ viññāṇānaṃ": _n("पाँच प्रकार की चेतना", g="f", case="dat"),
    "vipākamanodhātu": _n("कर्म-फल रूपी मन का तत्व"),
    "vipākamanodhātuyā": _n("कर्म-फल रूपी मन का तत्व", "कर्म-फल रूपी मन के तत्व", case="dat"),
    "vipākamanoviññāṇadhātu": _n("कर्म-फल रूपी मन की चेतना का तत्व"),
    "vipākamanoviññāṇadhātuyā": _n("कर्म-फल रूपी मन की चेतना का तत्व", "कर्म-फल रूपी मन की चेतना के तत्व",
                                   case="dat"),
    "kiriyamanoviññāṇadhātuyā": _n("केवल क्रिया रूपी मन की चेतना का तत्व",
                                   "केवल क्रिया रूपी मन की चेतना के तत्व", case="dat"),
    "vipākassa": _n("कर्म-फल", case="dat"),
})
for _p, _h in [("cakkhu", "आँख"), ("kāya", "शरीर"), ("vaṇṇa", "रंग-रूप"), ("sadda", "ध्वनि"), ("gandha", "गंध"),
               ("rasa", "स्वाद")]:
    NOUN[_p + "sampadaṃ"] = _n(f"{_h} की संपन्नता", g="f", case="acc")
    NOUN[_p + "sampadā"] = _n(f"{_h} की संपन्नता", g="f")


def _a(ms, mo=None, f=None, short=False, pre=False):
    return {"ms": ms, "mo": mo or ms, "f": f or ms, "short": short, "pre": pre}


def _va(stem):  # «… वाला» adjective
    return _a(stem + "ा", stem + "े", stem + "ी")


ADJ = {}
for _w in ("ahetukaṃ", "ahetuke", "ahetukā", "ahetuko", "ahetukānaṃ"):
    ADJ[_w] = _a("मूल से रहित")
for _w in ("sampayuttakā", "sampayuttake", "sampayuttakānaṃ"):
    ADJ[_w] = _a("जुड़ा हुआ", "जुड़े हुए", "जुड़ी हुई")
ADJ["vicikicchāsahagate uddhaccasahagate"] = _a("संशय के साथ होने वाले और बेचैनी के साथ होने वाले",
                                                 f="संशय के साथ होने वाली और बेचैनी के साथ होने वाली")
for _w in ("vicikicchāsahagato uddhaccasahagato", "vicikicchāsahagataṃ uddhaccasahagataṃ"):
    ADJ[_w] = _a("संशय के साथ होने वाला या बेचैनी के साथ होने वाला",
                 "संशय के साथ होने वाले या बेचैनी के साथ होने वाले",
                 "संशय के साथ होने वाली या बेचैनी के साथ होने वाली")
for _p, _h, _s in _SENSE:
    for _e in ("aṃ", "ā", "ānaṃ", "o", "e"):
        ADJ[_p + "viññāṇasahagat" + _e] = _va(f"{_h} की चेतना के साथ होने वाल")
ADJ["bāhiraṃ"] = _a("बाह्य", short=True)
ADJ["āhārasamuṭṭhānaṃ"] = _a("आहार से उत्पन्न")
ADJ["utusamuṭṭhānaṃ"] = _a("तापमान से उत्पन्न")
ADJ["asaññasattānaṃ"] = _a("पहचान-रहित प्राणियों में", pre=True)
for _w in ("vipākānaṃ", "vipākassa", "vipākā"):
    ADJ[_w] = _a("कर्म-फल रूपी")
for _w in ("purimā purimā", "purimaṃ purimaṃ"):
    ADJ[_w] = _a("पहले-पहले का", "पहले-पहले के", "पहले-पहले की", pre=True)
for _w in ("pacchimānaṃ pacchimānaṃ", "pacchimassa pacchimassa"):
    ADJ[_w] = _a("बाद-बाद का", "बाद-बाद के", "बाद-बाद की", pre=True)

ADJ["pacchājātā"] = _a("बाद में उत्पन्न")
ADJ["sahajātā"] = _a("साथ उत्पन्न")
ADJ["vipāko"] = _a("कर्म-फल रूपी")
ADJ["purejātassa"] = _a("पहले उत्पन्न", pre=True)
ADJ["imassa"] = _a("इस", pre=True)
ADJ["cittasamuṭṭhānaṃ"] = _a("मन से उत्पन्न")
ADJ["cittasaṃsaṭṭhā"] = _a("मन से घुला-मिला", "मन से घुले-मिले", "मन से घुली-मिली")
for _e in ("aṃ", "ā", "ānaṃ", "o", "e"):
    ADJ["pañcaviññāṇasahagat" + _e] = _va("पाँच प्रकार की चेतना के साथ होने वाल")
_B3 = "बाह्य, आहार से उत्पन्न और तापमान से उत्पन्न"
_B4 = "बाह्य, आहार से उत्पन्न, तापमान से उत्पन्न और पहचान-रहित प्राणियों में होने वाल"
_B3A = "बाह्य, तापमान से उत्पन्न और पहचान-रहित प्राणियों में होने वाल"
for _w in ("bāhiraṃ āhārasamuṭṭhānaṃ utusamuṭṭhānaṃ", "bāhire āhārasamuṭṭhāne utusamuṭṭhāne"):
    ADJ[_w] = _a(_B3)
for _w in ("bāhiraṃ āhārasamuṭṭhānaṃ utusamuṭṭhānaṃ asaññasattānaṃ",
           "bāhire āhārasamuṭṭhāne utusamuṭṭhāne asaññasattānaṃ"):
    ADJ[_w] = _va(_B4)
for _w in ("bāhiraṃ utusamuṭṭhānaṃ asaññasattānaṃ", "bāhire utusamuṭṭhāne asaññasattānaṃ"):
    ADJ[_w] = _va(_B3A)

NUMW = {"ekaṃ": "एक", "eko": "एक", "dve": "दो", "tayo": "तीन", "tiṇṇannaṃ": "तीन", "dvinnaṃ": "दो",
        "cattāro": "चार"}

PREFIX9 = {
    "arūpe": "अभौतिक लोक में",
    "paṭisandhikkhaṇe": "पुनर्जन्म के क्षण में",
    "ahetukapaṭisandhikkhaṇe": "मूल से रहित पुनर्जन्म के क्षण में",
}

LABEL9 = {
    "sahajātā": "सह-उत्पत्ति", "sahajātaṃ": "सह-उत्पत्ति", "sahajāto": "सह-उत्पत्ति",
    "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātā": "पश्चात्-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति",
    "āhāraṃ": "आहार", "indriyaṃ": "क्षमता", "nānākkhaṇikā": "भिन्न क्षण",
    "ārammaṇādhipati": "विषय रूपी प्रधानता", "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
    "ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय",
    "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय",
    "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति", "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति",
}

# ------------------------------------------------------------------ multi-piece phrases (dative lists)

_NANA = dict(R.NANA)
_NANA["phalassa"] = "फल"


def _dl(keys):
    hs = [_NANA[k] for k in keys]
    return ", ".join(hs[:-1]) + " और " + hs[-1]


PHRASES = {}
for _l in ["iddhividhañāṇassa, cetopariyañāṇassa, pubbenivāsānussatiñāṇassa, yathākammūpagañāṇassa, anāgataṃsañāṇassa, āvajjanāya",
           "iddhividhañāṇassa, pubbenivāsānussatiñāṇassa, anāgataṃsañāṇassa, āvajjanāya",
           "gotrabhussa, vodānassa, maggassa, phalassa, āvajjanāya",
           "gotrabhussa, vodānassa, maggassa, phalassa,"]:
    _ks = [k for k in _l.replace(",", " ").split()]
    PHRASES[_l] = ("NP", _dl(_ks), "ms", "dat")
# ^7-32-386 area: «Upādā dhammañca noupādā dhammañca dhammaṃ» (dhamma doubled in the source): the same pair in Hindi
PHRASES["‹P:x› dhammañca ‹N:x› dhammañca dhammaṃ"] = ("NP", "{P:f} परिघटना और {N:f} परिघटना", "fp", "acc")

# ------------------------------------------------------------------ narrative pieces (exact, after item tokens)

CETO = R.CETOPARIYA
ANI = R.ANICCA
KIL = R.KILESA
REV_S, REV_P = R.REVIEW["s"], R.REVIEW["p"]
SAV = "उसका रस लेता है, उसमें आनंद लेता है"
SAV_PL = "उनका रस लेता है, उनमें आनंद लेता है"
PIECE9 = {
    "kāyaviññāṇasahagataṃ": "शरीर की चेतना के साथ होने वाले",
    "kāyaviññāṇasahagate": "शरीर की चेतना के साथ होने वाले",
    "kāyaviññāṇasahagato": "शरीर की चेतना के साथ होने वाला",
    "kāyaviññāṇasahagatā": "शरीर की चेतना के साथ होने वाले",
    "cakkhuviññāṇasahagato": "आँख की चेतना के साथ होने वाला",
    "pañcaviññāṇasahagataṃ": "पाँच प्रकार की चेतना के साथ होने वाले",
    "asaññasattānaṃ": "पहचान-रहित प्राणियों में",
    "saṃkhittaṃ": "संक्षिप्त",
    "anulomaṃ": "सकारात्मक क्रम",
    "paccanīyaṃ": "नकारात्मक क्रम",
    # unclosed parentheses in the source (^7-32-256 area, ^7-32-466 area), kept as written
    "purejātaṃ (saṃkhittaṃ": "पूर्व-उत्पत्ति (संक्षिप्त",
    "āhāraṃ (saṃkhittaṃ": "आहार (संक्षिप्त",
    "yathā nikkhittapadāni vitthāretabbāni": "जैसे रखे गए पद हैं, वैसे उनका विस्तार करना चाहिए",
    # ārammaṇa / adhipati narrative
    "dānaṃ": "दान",
    "dānaṃ datvā": "दान देकर",
    "dānaṃ datvā sīlaṃ": "दान देकर, सदाचार",
    "uposathakammaṃ katvā taṃ paccavekkhati": f"उपवास-व्रत का पालन करके उस पर {REV_S}",
    "uposathakammaṃ katvā taṃ paccavekkhati assādeti abhinandati":
        f"उपवास-व्रत का पालन करके उस पर {REV_S}, {SAV}",
    "uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati assādeti abhinandati":
        f"उपवास-व्रत का पालन करके उसे महत्व देकर {REV_S}, {SAV}",
    "pubbe": "पहले",
    "pubbe suciṇṇāni": "पहले भली-भाँति किए गए कार्य",
    "pubbe samudāciṇṇe": "पहले बार-बार उठे",
    "jhānā": "ध्यान से",
    "jhānaṃ": "ध्यान",
    "jhānā vuṭṭhahitvā jhānaṃ": "ध्यान से उठकर ध्यान",
    "ariyā maggā": "आर्य मार्ग से",
    "ariyā maggā vuṭṭhahitvā": "आर्य मार्ग से उठकर",
    "ariyā maggā vuṭṭhahitvā maggaṃ": "आर्य मार्ग से उठकर मार्ग",
    "ariyā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": f"आर्य मार्ग से उठकर मार्ग पर {REV_P}",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ": "आर्य मार्ग से उठकर मार्ग को महत्व",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā": "आर्य मार्ग से उठकर मार्ग को महत्व देकर",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti": f"आर्य मार्ग से उठकर मार्ग को महत्व देकर {REV_P}",
    "phalaṃ": "फल",
    "phalaṃ paccavekkhanti": f"फल पर {REV_P}",
    "phalaṃ garuṃ": "फल को महत्व",
    "phalaṃ garuṃ katvā paccavekkhanti": f"फल को महत्व देकर {REV_P}",
    "nibbānaṃ garuṃ katvā": "निर्वाण को महत्व देकर",
    "ariyā nibbānaṃ paccavekkhanti": f"आर्य निर्वाण पर {REV_P}",
    "ariyā nibbānaṃ garuṃ katvā paccavekkhanti": f"आर्य निर्वाण को महत्व देकर {REV_P}",
    "pahīne kilese": KIL["pahīne"],
    "vikkhambhite kilese": KIL["vikkhambhite"],
    "ariyā pahīne kilese": f"आर्य {KIL['pahīne']}",
    "ariyā pahīne kilese paccavekkhanti": f"आर्य {KIL['pahīne']} पर {REV_P}",
    "ariyā ‹N:e› pahīne kilese paccavekkhanti": f"आर्य {{N:mo}} {KIL['pahīne']} पर {REV_P}",
    "ariyā ‹P:e› pahīne kilese paccavekkhanti": f"आर्य {{P:mo}} {KIL['pahīne']} पर {REV_P}",
    "cakkhuṃ": "आँख",
    "cakkhuṃ aniccato": "आँख को अनित्य",
    "kāyaṃ aniccato": "शरीर को अनित्य",
    "vatthuṃ aniccato": "आधार को अनित्य",
    "phoṭṭhabbe aniccato": "स्पर्शों को अनित्य",
    "phoṭṭhabbe vatthuṃ aniccato": "स्पर्शों, आधार को अनित्य",
    "rase vatthuṃ aniccato": "स्वादों, आधार को अनित्य",
    "cittasamuṭṭhāne rūpe": "मन से उत्पन्न दृश्य रूपों",
    "vipassati": "अंतर्दृष्टि से देखता है",
    "assādeti": "उसका रस लेता है",
    "assādeti abhinandati": SAV,
    "vipassati assādeti abhinandati": f"अंतर्दृष्टि से देखता है, {SAV}",
    "vatthuṃ garuṃ katvā assādeti abhinandati": f"आधार को महत्व देकर {SAV}",
    "rase vatthuṃ garuṃ katvā assādeti abhinandati": f"स्वादों, आधार को महत्व देकर {SAV_PL}",
    "taṃ ārabbha rāgo": "उसे विषय बनाकर राग",
    "kusalākusale niruddhe vipāko tadārammaṇatā uppajjati":
        "हितकर और हानिकर के समाप्त होने पर " + R.VIPAKA_TADARAMMANA,
    "ākāsānañcāyatanaṃ viññāṇañcāyatanassa": "अनंत आकाश का क्षेत्र, अनंत चेतना के क्षेत्र के लिए",
    "ākiñcaññāyatanaṃ nevasaññānāsaññāyatanassa": "कुछ भी न होने का क्षेत्र, न पहचान न अ-पहचान के क्षेत्र के लिए",
    "ākāsānañcāyatanaṃ": "अनंत आकाश का क्षेत्र",
    "ākiñcaññāyatanaṃ": "कुछ भी न होने का क्षेत्र",
    "ākāsānañcāyatanakusalaṃ viññāṇañcāyatanavipākassa":
        "अनंत आकाश के क्षेत्र का हितकर मन, अनंत चेतना के क्षेत्र के कर्म-फल रूपी मन के लिए",
    "ākiñcaññāyatanakusalaṃ": "कुछ भी न होने के क्षेत्र का हितकर मन",
    # upanissaya narrative
    "saddhaṃ upanissāya dānaṃ deti": "श्रद्धा के प्रबल आश्रय से दान देता है",
    "kāyikaṃ sukhaṃ upanissāya dānaṃ deti": "शारीरिक सुख के प्रबल आश्रय से दान देता है",
    "kāyikaṃ dukkhaṃ upanissāya dānaṃ deti": "शारीरिक दुःख के प्रबल आश्रय से दान देता है",
    "senāsanaṃ upanissāya dānaṃ deti": "निवास-स्थान के प्रबल आश्रय से दान देता है",
    "bhojanaṃ upanissāya dānaṃ deti": "भोजन के प्रबल आश्रय से दान देता है",
    "senāsanaṃ cittaṃ upanissāya dānaṃ deti": "निवास-स्थान, मन के प्रबल आश्रय से दान देता है",
    "mānaṃ jappeti": "अहंकार पालता है",
    "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "paññaṃ": "प्रज्ञा",
    "rāgaṃ": "राग",
    "patthanaṃ": "कामना",
    "patthanaṃ kāyikaṃ sukhaṃ": "कामना, शारीरिक सुख",
    "utuṃ": "तापमान",
    "‹P:aṃ› utuṃ": "{P:ms} तापमान",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "pāṇaṃ hanati": "जीव की हत्या करता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "saddhaṃ upanissāya attānaṃ ātāpeti paritāpeti": "श्रद्धा के प्रबल आश्रय से स्वयं को तपाता है, कष्ट देता है",
    "senāsanaṃ upanissāya attānaṃ ātāpeti paritāpeti":
        "निवास-स्थान के प्रबल आश्रय से स्वयं को तपाता है, कष्ट देता है",
    "pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti": "खोज के कारण होने वाला दुःख भोगता है",
    "kusalākusalaṃ kammaṃ vipākassa upanissayapaccayena paccayo":
        f"हितकर और हानिकर कर्म, कर्म-फल के लिए {R.INS('upanissaya', 'ms')}",
    # anantara
    "nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanaṃ phalasamāpattiyā anantarapaccayena paccayo":
        "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में न पहचान न अ-पहचान का क्षेत्र फल की ध्यान-अवस्था के लिए "
        + R.INS("anantara", "ms"),
    "purimaṃ purimaṃ cittaṃ pacchimassa pacchimassa": "पहले-पहले का मन बाद-बाद के",
    "bhavaṅgaṃ āvajjanāya": "जीवन-धारा मन को विषय की ओर मोड़ने के लिए",
    "cittasaṃsaṭṭhā sampayuttakā khandhā": "मन से घुल-मिलकर जुड़े हुए समूह",
    "dvepi kātabbā": "दोनों करने चाहिए",
    "paṭisandhikkhaṇe ekaṃ": "पुनर्जन्म के क्षण में एक",
    "paṭisandhikkhaṇe dve": "पुनर्जन्म के क्षण में दो",
    # ^7-32-65 area, clauses run together in the source (as written, a comma added)
    "vatthuṃ paccayā ahetukā ‹N:e› khandhā vicikicchāsahagate uddhaccasahagate khandhe ca vatthuñca paccayā "
    "vicikicchāsahagato uddhaccasahagato moho":
        "आधार के कारण मूल से रहित, {N:mo} समूह, संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों और आधार "
        "के कारण संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह",
}
# item-token narrative pieces (same for P and N)
for _s in ("P", "N"):
    _f = "{%s:mo}" % _s
    PIECE9.update({
        f"‹{_s}:e› khandhe aniccato": f"{_f} समूहों को अनित्य",
        f"‹{_s}:x› khandhe aniccato": f"{_f} समूहों को अनित्य",
        f"vatthuṃ ‹{_s}:e› khandhe aniccato": f"आधार, {_f} समूहों को अनित्य",
        f"vatthuṃ ‹{_s}:x› khandhe aniccato": f"आधार, {_f} समूहों को अनित्य",
        f"phoṭṭhabbe ‹{_s}:e› khandhe aniccato": f"स्पर्शों, {_f} समूहों को अनित्य",
        f"phoṭṭhabbe ‹{_s}:x› khandhe aniccato": f"स्पर्शों, {_f} समूहों को अनित्य",
        f"‹{_s}:e› khandhe garuṃ katvā": f"{_f} समूहों को महत्व देकर",
        f"‹{_s}:e› khandhe garuṃ katvā assādeti abhinandati": f"{_f} समूहों को महत्व देकर {SAV_PL}",
        f"vatthuṃ ‹{_s}:e› khandhe garuṃ katvā assādeti abhinandati": f"आधार, {_f} समूहों को महत्व देकर {SAV_PL}",
        f"phoṭṭhabbe ‹{_s}:e› khandhe garuṃ katvā assādeti abhinandati":
            f"स्पर्शों, {_f} समूहों को महत्व देकर {SAV_PL}",
        f"phoṭṭhabbe ‹{_s}:x› khandhe garuṃ katvā assādeti abhinandati":
            f"स्पर्शों, {_f} समूहों को महत्व देकर {SAV_PL}",
        f"‹{_s}:e› rūpe": f"{_f} दृश्य रूपों",
        f"kāyaṃ ‹{_s}:e› rūpe": f"शरीर, {_f} दृश्य रूपों",
        f"dibbena cakkhunā ‹{_s}:aṃ› rūpaṃ passati": f"दिव्य आँख से {_f} दृश्य रूप को देखता है",
        f"‹{_s}:aṃ›": "{%s:mo}" % _s,
        f"‹{_s}:ā›": "{%s:mo}" % _s,
        f"‹{_s}:x›": "{%s:mo}" % _s,
    })

# ------------------------------------------------------------------ editorial notes (key = text inside the parentheses, lower initials)

PAT = "निर्भरता के खंड के समान"
PAC = "कारण के खंड के समान"
PRE = "पूर्व-उत्पत्ति-कारण के समान"
NNK = "बिना किसी अंतर के"
PG = "पहले प्रसंग के समान"
CSD = "मन से उत्पन्न परिघटनाओं वाले दो के वर्गीकरण के समान"
CHD = "मन के साथ-साथ होने वाली परिघटनाओं वाले दो के वर्गीकरण के समान"
PS = "पुनर्जन्म के क्षण में"
MOHA3 = "मोह तीन में ही"
NOTE9 = {
    "saṃkhittaṃ": "संक्षिप्त",
    "saṃkhittaṃ.": "संक्षिप्त।",
    "anulomaṃ": "सकारात्मक क्रम",
    "paccanīyaṃ": "नकारात्मक क्रम",
    "cakkaṃ": "चक्र",
    "mūlaṃ": "मूल वाक्य",
    "mūlaṃ kātabbaṃ": "मूल वाक्य बनाना चाहिए",
    "mūlaṃ pucchitabbaṃ": "मूल वाक्य पूछना चाहिए",
    "mūlaṃ pucchitabbaṃ, tīṇi upanissayā": "मूल वाक्य पूछना चाहिए, तीन प्रबल आश्रय",
    "yāva asaññasattā": "पहचान-रहित प्राणियों तक",
    "yāva asaññasattā kātabbā": "पहचान-रहित प्राणियों तक करना चाहिए",
    "yāva mahābhūtā": "महाभूतों तक",
    "yāva utusamuṭṭhānaṃ": "तापमान से उत्पन्न तक",
    "yāva asaññasattā, evaṃ tīṇi noupādāmūlake":
        "पहचान-रहित प्राणियों तक, इसी तरह व्युत्पन्न न होने वाली परिघटना से शुरू होने वाली शृंखला में तीन",
    "paṭiccasadisā": PAT, "paṭiccasadisaṃ": PAT, "paṭiccavārasadisaṃ": PAT, "paṭiccavārasadisā": PAT,
    "paccayavārasadisā": PAC, "paccayavārasadisaṃ": PAC, "paccayasadisā": PAC,
    "purejātasadisaṃ": PRE,
    "purejātasadisaṃ, saṃkhittaṃ": f"{PRE}, संक्षिप्त",
    "purejātasadisaṃ, ninnānākaraṇaṃ": f"{PRE}, {NNK}",
    "purejātasadisaṃ ninnānākaraṇaṃ": f"{PRE}, {NNK}",
    "purejātasadisaṃ ninnānaṃ": f"{PRE}, {NNK}",
    "saṃkhittaṃ. purejātasadisaṃ ninnānākaraṇaṃ": f"संक्षिप्त। {PRE}, {NNK}",
    "pacchājātasadisaṃ kātabbaṃ": "पश्चात्-उत्पत्ति-कारण के समान करना चाहिए",
    "paṭiccavāre sahajātasadisā": "निर्भरता के खंड में सह-उत्पत्ति-कारण के समान",
    "paṭiccavāre aññamaññasadisaṃ": "निर्भरता के खंड में परस्पर-कारण के समान",
    "paccayavāre nissayasadiso": "कारण के खंड में आश्रय-कारण के समान",
    "paccayavāre nissayasadisā": "कारण के खंड में आश्रय-कारण के समान",
    "paccayavāre nissayasadisaṃ": "कारण के खंड में आश्रय-कारण के समान",
    "sahajātavāropi paṭiccavārasadiso.": "सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान है।",
    "sahajātavāro paṭiccavārasadiso.": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।",
    "nissayavāro paccayavārasadiso.": "आश्रय का खंड कारण के खंड के समान है।",
    "evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.": "इसी तरह बाकी दो गणनाएँ और जुड़ाव का खंड भी करना चाहिए।",
    "evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbā.": "इसी तरह बाकी दो गणनाएँ और जुड़ाव का खंड भी करने चाहिए।",
    "evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.": "इसी तरह बाकी दो गणनाएँ और आश्रय का खंड भी करना चाहिए।",
    "evaṃ itare dve gaṇanāpi sampayuttavārāpi kātabbā.": "इसी तरह बाकी दो गणनाएँ और जुड़ाव के खंड भी करने चाहिए।",
    "evaṃ itare dve gaṇanāpi sampayuttavāropi sabbe kātabbā.":
        "इसी तरह बाकी दो गणनाएँ और जुड़ाव का खंड भी, सब करने चाहिए।",
    "itare dve gaṇanāpi sampayuttavāropi sabbaṃ kātabbaṃ.": "बाकी दो गणनाएँ और जुड़ाव का खंड भी, सब करना चाहिए।",
    "itare dve gaṇanāpi sampayuttavāropi kātabbo.": "बाकी दो गणनाएँ और जुड़ाव का खंड भी करना चाहिए।",
    "evaṃ itare dvepi gaṇanā kātabbā": "इसी तरह बाकी दोनों गणनाएँ करनी चाहिए",
    "itare dve gaṇanā, imassa sadisāyeva kātabbā": "बाकी दो गणनाएँ इसी के समान करनी चाहिए",
    "anulomamātikā kātabbā": "सकारात्मक क्रम की मूल सूची बनानी चाहिए",
    "anulomamātikā vitthāretabbā": "सकारात्मक क्रम की मूल सूची का विस्तार करना चाहिए",
    "anulomagaṇanā kātabbā": "सकारात्मक क्रम की गणना करनी चाहिए",
    "sabbattha nava, anulomamātikā": "हर जगह नौ, सकारात्मक क्रम की मूल सूची",
    "paṭisandhikkhaṇe": PS,
    "paṭisandhikkhaṇe ekaṃ": f"{PS} एक",
    "paṭisandhikkhaṇe dve": f"{PS} दो",
    "paṭisandhikkhaṇe dvepi": f"{PS} दोनों",
    "paṭisandhikkhaṇepi dve": f"{PS} भी दो",
    "paṭisandhikkhaṇe ekaṃ kātabbaṃ": f"{PS} एक करना चाहिए",
    "paṭisandhikkhaṇe dve kātabbā": f"{PS} दो करने चाहिए",
    "paṭisandhikkhaṇe dvepi kātabbā": f"{PS} दोनों करने चाहिए",
    "paṭisandhikkhaṇe tīṇi kātabbā": f"{PS} तीन करने चाहिए",
    "paṭisandhikkhaṇe tīṇipi kātabbā": f"{PS} तीनों करने चाहिए",
    "paṭisandhikkhaṇe ekaṃ, saṃkhittaṃ": f"{PS} एक, संक्षिप्त",
    "paṭisandhikkhaṇe dve, saṃkhittaṃ": f"{PS} दो, संक्षिप्त",
    "paṭisandhikkhaṇe ekaṃ kātabbaṃ, saṃkhittaṃ": f"{PS} एक करना चाहिए, संक्षिप्त",
    "paṭisandhikkhaṇe dvepi kātabbā, saṃkhittaṃ": f"{PS} दोनों करने चाहिए, संक्षिप्त",
    "paṭisandhikkhaṇe dvepi paṭiccavārasadisā": f"{PS} दोनों, {PAT}",
    "paṭisandhikkhaṇe tīṇipi kātabbā paṭiccavārasadisā": f"{PS} तीनों करने चाहिए, {PAT}",
    "paṭisandhikkhaṇe dvepi kātabbā paṭiccavārasadisā": f"{PS} दोनों करने चाहिए, {PAT}",
    "paṭisandhikkhaṇe dvepi kātabbā, yāva ajjhattikā mahābhūtā": f"{PS} दोनों करने चाहिए, आंतरिक महाभूतों तक",
    "ahetukapaṭisandhikkhaṇe dvepi kātabbā": f"मूल से रहित {PS} दोनों करने चाहिए",
    "paṭisandhiyā dve kātabbā": "पुनर्जन्म में दो करने चाहिए",
    "paṭhamagamanaṃ": "पहला प्रसंग",
    "paṭhamagamanasadisaṃ": PG,
    "paṭhamagamanasadisaṃ ninnānākaraṇaṃ, imaṃ nānaṃ": f"{PG}, {NNK}, अंतर यह है",
    "tīṇi, paṭhamagamanasadisaṃ ninnānākaraṇaṃ": f"तीन, {PG}, {NNK}",
    "dvepi gamanā paṭhamagamanasadisaṃ ninnānākaraṇaṃ. ārammaṇādhipati sahajātādhipati kātabbā":
        f"दोनों प्रसंग {PG} हैं, {NNK}। विषय रूपी प्रधानता और सह-उत्पत्ति रूपी प्रधानता करनी चाहिए",
    "tīṇipi garukārammaṇā kātabbā, ārammaṇādhipatiyeva": "तीनों में महत्व दिए गए विषय करने चाहिए, विषय रूपी प्रधानता ही",
    "ārammaṇādhipatiyeva": "विषय रूपी प्रधानता ही",
    "ime dve pūretukāmena kātabbā, purimagamanasadisaṃ":
        "पूरा करना चाहने वाले को ये दो करने चाहिए, पहले वाले प्रसंग के समान",
    "ime dvepi pūretukāmena sabbattha kātabbā, paṭhamagamanasadisaṃ ninnānākaraṇaṃ":
        f"पूरा करना चाहने वाले को ये दोनों हर जगह करने चाहिए, {PG}, {NNK}",
    "evaṃ tīṇi kātabbāni, paṭhamagamanasadisaṃ. pūritvā kātabbaṃ, ninnānākaraṇaṃ":
        f"इसी तरह तीन करने चाहिए, {PG}। पूरा करके करना चाहिए, {NNK}",
    "nava pañhā pañcaviññāṇampi yathā ārammaṇapaccayā evaṃ kātabbaṃ, tīsuyeva moho. sabbe pañhā pavattipaṭisandhiyā kātabbā asammohantena.":
        "नौ प्रश्न; पाँच प्रकार की चेतना भी जैसे विषय-कारण में है, वैसे ही करनी चाहिए, मोह तीन में ही है। "
        "सभी प्रश्न जीवन-काल और पुनर्जन्म में बिना भ्रमित हुए करने चाहिए।",
    "evaṃ pañcapi pañhā kātabbā, tīṇiyeva moho. saṃkhittaṃ": f"इसी तरह पाँचों प्रश्न करने चाहिए, {MOHA3}। संक्षिप्त",
    "āvajjanāpi vuṭṭhānampi natthi": "मन को विषय की ओर मोड़ना भी और बाहर आना भी नहीं है",
    "vuṭṭhānaṃ natthi": "बाहर आना नहीं है",
    "tīṇi kātabbā, vuṭṭhānaṃ natthi": "तीन करने चाहिए, बाहर आना नहीं है",
    "tīṇi pañhā kātabbā": "तीन प्रश्न करने चाहिए",
    "evaṃ navapi pañhā kātabbā. ahetukanti sabbattha niyāmetabbaṃ, ekaṃyeva mohaṃ mūlapade.":
        "इसी तरह सभी नौ प्रश्न करने चाहिए। हर जगह “मूल से रहित” निश्चित करना चाहिए, मूल पद में केवल एक मोह।",
    "evaṃ dve pañhā pavattipaṭisandhi kātabbā. saṃkhittaṃ.":
        "इसी तरह दो प्रश्न जीवन-काल और पुनर्जन्म में करने चाहिए। संक्षिप्त।",
    "paṭiccasadisā, pañhāghaṭanā natthi": f"{PAT}, प्रश्नों का संयोजन नहीं है",
    "paccayavārasadisā, pañhāghaṭanā natthi": f"{PAC}, प्रश्नों का संयोजन नहीं है",
    "cittasaṃsaṭṭhadukaṃ yathā cittasampayuttadukaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ.":
        "मन से घुली-मिली परिघटनाओं वाला दो का वर्गीकरण वैसे ही करना चाहिए जैसे मन से जुड़ी परिघटनाओं वाला दो का "
        f"वर्गीकरण, {NNK}।",
    "sabbe navapi pañhā kātabbā, paṭiccavārasadisā. pañcaviññāṇampi kātabbaṃ. tīṇiyeva moho.":
        f"सभी नौ प्रश्न करने चाहिए, {PAT}। पाँच प्रकार की चेतना भी करनी चाहिए। {MOHA3}।",
    "pañca pañhā kātabbā. tīṇi. moho": "पाँच प्रश्न करने चाहिए। तीन। मोह",
    "ārabbha kātabbā": "विषय बनाकर करने चाहिए",
    "tīṇipi ārammaṇādhipati, sahajātādhipatipi kātabbā":
        "तीनों में विषय रूपी प्रधानता, और सह-उत्पत्ति रूपी प्रधानता भी करनी चाहिए",
    "iminākāreneva pacchājāto vitthāretabbo": "इसी ढंग से पश्चात्-उत्पत्ति-कारण का विस्तार करना चाहिए",
    "paccayavārasadisaṃ paṭisandhipi pavattipi kātabbā sabbesampi pañhānaṃ.":
        f"{PAC}, सभी प्रश्नों के लिए पुनर्जन्म भी और जीवन-काल भी करना चाहिए।",
    "arūpaṃ sabbaṃ uddharitabbaṃ. cittasamuṭṭhānadukasadisaṃ.": f"अभौतिक सब निकालना चाहिए। {CSD}।",
    "mahābhūtā chasupi pañhesu kātabbā, adhipatiyā tīsu natthi.":
        "महाभूत छहों प्रश्नों में करने चाहिए, प्रधानता-कारण में तीन में नहीं हैं।",
    'evaṃ navapi pañhā kātabbā. "ahetuka"nti niyāmetabbaṃ. yathā anulome labbhati evaṃ kātabbaṃ. tīṇi moho yathā cittasamuṭṭhānaduke evameva kātabbā.':
        "इसी तरह सभी नौ प्रश्न करने चाहिए। “मूल से रहित” निश्चित करना चाहिए। जैसा सकारात्मक क्रम में लागू होता है, "
        "वैसा ही करना चाहिए। मोह वाले तीन जैसे मन से उत्पन्न परिघटनाओं वाले दो के वर्गीकरण में हैं, वैसे ही करने चाहिए।",
    "paṭiccavārasadisaṃ, sabbe mahābhūtā": f"{PAT}, सभी महाभूत",
    "paṭiccasadisaṃ, sabbe mahābhūtā": f"{PAT}, सभी महाभूत",
    "sabbe mahābhūtā paṭiccasadisaṃ": f"सभी महाभूत {PAT}",
    "imaṃ cittasamuṭṭhānadukaṃ paccayavāre ārammaṇasadisaṃ. channampi imesaṃ pañcaviññāṇamūlā kātabbā. saṃkhittaṃ.":
        "मन से उत्पन्न परिघटनाओं वाला यह दो का वर्गीकरण कारण के खंड में विषय-कारण के समान है। इन छहों में भी पाँच "
        "प्रकार की चेतना पर आधारित प्रश्न करने चाहिए। संक्षिप्त।",
    "saṃkhittaṃ. sabbaṃ kātabbaṃ. paccayavārassa pañcaviññāṇaṃ channampi mūlā kātabbā. sabbe mahābhūte tīṇiyeva moho. saṃkhittaṃ.":
        "संक्षिप्त। सब करना चाहिए। कारण के खंड की पाँच प्रकार की चेतना के लिए छहों मूल वाक्य करने चाहिए। सभी "
        f"महाभूत; {MOHA3}। संक्षिप्त।",
    "tīṇi, moho": "तीन, मोह",
    "saṃkhittaṃ. tīṇiyeva moho": f"संक्षिप्त। {MOHA3}",
    "saṃkhittaṃ, sabbaṃ kātabbaṃ": "संक्षिप्त, सब करना चाहिए",
    "ārammaṇādhipatipi sahajātādhipatipi kātabbā": "विषय रूपी प्रधानता भी और सह-उत्पत्ति रूपी प्रधानता भी करनी चाहिए",
    "ārammaṇādhipatipi sahajātādhipatipi imesampi tiṇṇaṃ kātabbā. navapi pañhā cittasamuṭṭhānadukasadisā. ante tīṇi ārammaṇādhipatiyeva":
        "इन तीनों के लिए भी विषय रूपी प्रधानता भी और सह-उत्पत्ति रूपी प्रधानता भी करनी चाहिए। सभी नौ प्रश्न "
        f"{CSD}। अंत के तीन में विषय रूपी प्रधानता ही",
    "cittasamuṭṭhānadukasadisā": CSD,
    "cittasamuṭṭhānadukasadisaṃ": CSD,
    "cittasamuṭṭhānadukasadisaṃ, ninnānākaraṇaṃ": f"{CSD}, {NNK}",
    "nocittasahabhū mūlaṃyeva labbhati, cittasamuṭṭhānadukasadisā. tīṇipi ninnānākaraṇaṃ":
        f"केवल मन के साथ-साथ न होने वाली परिघटना वाला मूल वाक्य ही लागू होता है, {CSD}। तीनों {NNK}",
    "cittasamuṭṭhānadukasadisā. imampi ekaṃ kabaḷīkāraāhārasadisaṃ":
        f"{CSD}। यह एक भी कौर-कौर खाए जाने वाले भोजन के समान",
    "sabbaṃ paṭisandhiyaṃ kātabbaṃ, sahajātaṃ purejātampi":
        "सब पुनर्जन्म में करना चाहिए, सह-उत्पत्ति और पूर्व-उत्पत्ति भी",
    "yathā cittasahabhūdukaṃ evaṃ imaṃ dukaṃ kātabbaṃ, ninnānākaraṇaṃ":
        "जैसे मन के साथ-साथ होने वाली परिघटनाओं वाला दो का वर्गीकरण है, वैसे ही यह दो का वर्गीकरण करना चाहिए, "
        + NNK,
    "evaṃ nava pañhā kātabbā. paccayavāre pañcaviññāṇampi kātabbaṃ, tīṇiyeva moho":
        f"इसी तरह नौ प्रश्न करने चाहिए। कारण के खंड में पाँच प्रकार की चेतना भी करनी चाहिए, {MOHA3}",
    "saṃkhittaṃ. yathā cittasahabhūduke ārammaṇaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ. navapi pañhā.":
        "संक्षिप्त। जैसे मन के साथ-साथ होने वाली परिघटनाओं वाले दो के वर्गीकरण में विषय-कारण है, वैसे ही करना "
        f"चाहिए, {NNK}। सभी नौ प्रश्न।",
    "dvepi adhipatī kātabbā": "दोनों प्रधानताएँ करनी चाहिए",
    "dvepi adhipati kātabbā": "दोनों प्रधानताएँ करनी चाहिए",
    "ekāyeva adhipati kātabbā, navapi pañhā. yathā cittasahabhūdukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ":
        "एक ही प्रधानता करनी चाहिए, सभी नौ प्रश्न। जैसे मन के साथ-साथ होने वाली परिघटनाओं वाला दो का वर्गीकरण, "
        f"वैसे ही करना चाहिए, {NNK}",
    "navapi pañhā cittasahabhūdukasadisā": f"सभी नौ प्रश्न {CHD}",
    "navapi pañhā cittasahabhūdukasadisā, ninnānākaraṇaṃ": f"सभी नौ प्रश्न {CHD}, {NNK}",
    "cittasahabhūdukasadisā, ninnānākaraṇaṃ": f"{CHD}, {NNK}",
    "cittasahabhūdukasadisā, ninnānākaraṇaṃ. tīṇipi pacchājātā. dve. ekamūlānaṃ ekā ghaṭanā":
        f"{CHD}, {NNK}। तीनों पश्चात्-उत्पत्ति। दो। एक कारण वाली शृंखलाओं का एक संयोजन",
    "cittasahabhūdukasadisā ninnānākaraṇā. tīṇipi sahajātā, nānākkhaṇikā":
        f"{CHD}, {NNK}। तीनों सह-उत्पत्ति और भिन्न क्षण",
    "cittasahabhūgamanasadisā, ekaṃyeva kabaḷīkāraṃ āhāraṃ":
        "मन के साथ-साथ होने वाली परिघटनाओं वाले प्रसंग के समान, केवल एक कौर-कौर खाया जाने वाला भोजन",
    "purejātasadisaṃ purejātaṃ kātabbaṃ. sabbaṃ saṃkhittaṃ. vitthāretabbaṃ":
        f"{PRE} पूर्व-उत्पत्ति करनी चाहिए। सब संक्षिप्त। विस्तार करना चाहिए",
    "yathā cittasaṃsaṭṭhasamuṭṭhānadukaṃ, evaṃ imampi dukaṃ, ninnānākaraṇaṃ":
        "जैसे मन से घुली-मिली और मन से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण है, वैसे ही यह दो का वर्गीकरण भी, "
        + NNK,
    "yathā cittasaṃsaṭṭhasamuṭṭhānadukasadisaṃ, ninnānākaraṇaṃ":
        f"जैसे मन से घुली-मिली और मन से उत्पन्न परिघटनाओं वाले दो के वर्गीकरण के समान, {NNK}",
    "saṃkhittaṃ. evaṃ navapi pañhā kātabbā. pañcaviññāṇampi pavesetvā tīṇiyeva moho.":
        f"संक्षिप्त। इसी तरह सभी नौ प्रश्न करने चाहिए। पाँच प्रकार की चेतना को भी शामिल करके, {MOHA3}।",
    "evaṃ pañca kātabbā, tīṇiyeva moho": f"इसी तरह पाँच करने चाहिए, {MOHA3}",
    "dve adhipatī tiṇṇampi kātabbā": "तीनों के लिए दो प्रधानताएँ करनी चाहिए",
    "tiṇṇampi ekāyeva adhipati": "तीनों के लिए एक ही प्रधानता",
    "tiṇṇampi ekasadisā": "तीनों एक समान",
    "tīṇipi pūretvā kātabbā, cittassāti kātabbā, sampayuttakānañcāti kātabbā":
        "तीनों पूरे करके करने चाहिए, “मन के लिए” करना चाहिए, “और जुड़े हुए के लिए” करना चाहिए",
    "evaṃ navapi pañhā kātabbā": "इसी तरह सभी नौ प्रश्न करने चाहिए",
    "nava pañhā kātabbā": "नौ प्रश्न करने चाहिए",
    "idha atthi sabbaṭṭhāne sahajātaṃ paccayavārasadisaṃ. purejātaṃ purejātasadisaṃ. pacchājātaṃ pacchājātasadisaṃ kātabbaṃ, ninnānākaraṇaṃ":
        f"यहाँ उपस्थिति-कारण में हर स्थान पर सह-उत्पत्ति {PAC} है। पूर्व-उत्पत्ति {PRE}। पश्चात्-उत्पत्ति "
        f"पश्चात्-उत्पत्ति-कारण के समान करनी चाहिए, {NNK}",
    "sabbaṃ vitthāretabbaṃ": "सब का विस्तार करना चाहिए",
    "sahajātapaccayavārasadisaṃ ninnānākaraṇaṃ, paṭhamagamanasadisaṃyeva. sabbe padā paṭhamaghaṭanānayena vibhajitabbā":
        f"सह-उत्पत्ति वाले कारण के खंड के समान, {NNK}, {PG} ही। सभी पदों का पहले संयोजन की विधि से विश्लेषण करना चाहिए",
    "saṃkhittaṃ. sabbe padā vibhajitabbā paṭhamaghaṭanānayena":
        "संक्षिप्त। सभी पदों का पहले संयोजन की विधि से विश्लेषण करना चाहिए",
    "noupādāmūlake tīṇipi paṭiccasadisā, ninnānākaraṇā":
        f"व्युत्पन्न न होने वाली परिघटना से शुरू होने वाली शृंखला में तीनों {PAT}, {NNK}",
    "evaṃ gaṇetabbaṃ": "इसी तरह गिनना चाहिए",
    "tīṇipi paṭiccasadisā, ninnānākaraṇā": f"तीनों {PAT}, {NNK}",
    "noupādāmūlake tīṇi, paṭisandhikkhaṇe tīṇipi kātabbā":
        f"व्युत्पन्न न होने वाली परिघटना से शुरू होने वाली शृंखला में तीन, {PS} तीनों करने चाहिए",
    "nahetusadisaṃ, moho natthi": "मूल-कारण के अभाव के समान, मोह नहीं है",
    "saṃkhittaṃ. upādinnamūlake tīṇi.": "संक्षिप्त। कर्म से उत्पन्न परिघटना से शुरू होने वाली शृंखला में तीन।",
    "upādinnamūlake tīṇi, paṭhamasseva rūpajīvitindriyaṃ, itaresu natthi":
        "कर्म से उत्पन्न परिघटना से शुरू होने वाली शृंखला में तीन, केवल पहले में भौतिक जीवन-क्षमता, बाकी में नहीं",
    "saṃkhittaṃ. yathā nikkhittapadāni vibhajitabbāni paripuṇṇāni":
        "संक्षिप्त। जैसे रखे गए पद हैं, वैसे ही उनका पूरा-पूरा विश्लेषण करना चाहिए",
    "saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni": "संक्षिप्त, जैसे रखे गए पद हैं, वैसे उनका विस्तार करना चाहिए",
    "saṃkhittaṃ, yathā nikkhittapadāni vibhajitabbāni": "संक्षिप्त, जैसे रखे गए पद हैं, वैसे उनका विश्लेषण करना चाहिए",
}
for _n_ in ("ekaṃ", "dve", "tīṇi", "pañca", "satta", "nava"):
    NOTE9["sabbattha " + _n_] = "हर जगह " + R.NUM[_n_]
