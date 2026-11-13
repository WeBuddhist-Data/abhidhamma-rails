"""Phrase tables for build_3-01_3-02_3-10_hi.py (Pāli unit, first letter lower-cased -> Hindi)."""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

N, A, NA = S.NAME, S.ABL, S.NABL

# =====================================================================================
# Headings
# =====================================================================================
HEAD = {
    "(Tatiyo bhāgo)": S.BHAGA[3],
    "Dhammānulome dukapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.DUKAPATTHANA}",
    "Hetugocchakaṃ": S.GOCCHAKA("मूलों"),
    "Cūḷantaradukaṃ": "बीच के छोटे दो-दो के वर्गीकरण",
    "Upādānagocchakaṃ": S.GOCCHAKA("आसक्ति"),
    "Paṭiccavāro": S.VARA["paṭicca"],
    "Sahajātavāro": S.VARA["sahajāta"],
    "Paccayavāro": S.VARA["paccaya"],
    "Nissayavāro": S.VARA["nissaya"],
    "Saṃsaṭṭhavāro": S.VARA["saṃsaṭṭha"],
    "Sampayuttavāro": S.VARA["sampayutta"],
    "Pañhāvāro": S.VARA["pañhā"],
    "Vibhaṅgavāro": S.VARA["vibhaṅga"],
    "Saṅkhyāvāro": S.VARA["saṅkhyā"],
    "Paccayānulomaṃ": S.PACCAYANULOMA,
    "Paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "Paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA,
    "Paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA,
    "Anulomapaccanīyaṃ": S.ANULOMAPACCANIYA,
    "Suddhaṃ": S.SUDDHA,
    "Hetudukaṃ": S.DUKA("मूल"),                       # the dyad (heading level 6)
    "*Hetudukaṃ*": "*" + S.DUKANI("hetu") + "*",       # counting: hetu + other conditions
    "*Nahetudukaṃ*": "*" + S.DUKANI("hetu", neg=True) + "*",
}

PH = {}
LINES = {}

# =====================================================================================
# Noun-phrase lexicon (see build_3-01_3-02_3-10_hi.py, section 3)
# =====================================================================================
HN, NOUNF, HA, ADJF, NUMF = {}, {}, {}, {}, {}

# verb phrases after "X upanissāya" (X-के प्रबल आश्रय से ...)
VPH = {
    "dānaṃ deti": "दान देता है",
    "sīlaṃ samādiyati": "सदाचार ग्रहण करता है",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है",
    "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है",
    "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है",
    "maggaṃ uppādeti": "मार्ग उत्पन्न करता है",
    "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "mānaṃ jappeti": "अहंकार करता है",
    "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "pāṇaṃ hanati": "प्राणी की हत्या करता है",
    "adinnaṃ ādiyati": "बिना दी गई वस्तु ले लेता है",
    "adinnaṃ": "बिना दी गई वस्तु",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "dānaṃ": "दान",
}


def noun(key, gender, dsg, dpl=None, osg=None, opl=None, forms=()):
    """forms: (pāli, num, is_gen) tuples."""
    HN[key] = (gender, dsg, dpl or dsg, osg or dsg, opl or dpl or dsg)
    for p, n, g in forms:
        NOUNF[p] = (key, n, g)


def a_noun(key, stem, gender, dsg, dpl=None, osg=None, opl=None, extra=()):
    """a-stem masculine: khandha -> khandhaṃ khandho khandhā khandhe khandhānaṃ khandhassa."""
    noun(key, gender, dsg, dpl, osg, opl, forms=[(stem + "aṃ", "sg", False), (stem + "o", "sg", False),
                                                 (stem + "ā", "pl", False), (stem + "e", "pl", False),
                                                 (stem + "ānaṃ", "pl", True), (stem + "assa", "sg", True)]
         + list(extra))


def adj(key, m_sg, m_oth=None, f=None, group=None, stems=(), forms=()):
    HA[key] = (m_sg, m_oth or m_sg, f or m_sg, group)
    for st in stems:      # a-stems
        for e, g in (("aṃ", False), ("o", False), ("ā", False), ("e", False), ("ānaṃ", True), ("assa", True),
                     ("āya", True), ("akā", False), ("ake", False), ("akānaṃ", True), ("a", False),
                     ("āni", False)):
            ADJF.setdefault(st + e, (key, g))
    for p in forms:
        ADJF[p] = (key, p.endswith(("ānaṃ", "assa", "ūnaṃ", "īnaṃ")))


def vala(x):  # "<x> वाला" adjective
    return (f"{x} वाला", f"{x} वाले", f"{x} वाली")


# nouns ---------------------------------------------------------------------------------
a_noun("khandha", "khandh", "m", "समूह", "समूह", "समूह", "समूहों")
noun("vatthu", "m", "आधार", "आधार", "आधार", "आधारों",
     forms=[("vatthu", "sg", False), ("vatthuṃ", "sg", False), ("vatthussa", "sg", True)])
noun("hetu", "m", "मूल", "मूल", "मूल", "मूलों",
     forms=[("hetu", "sg", False), ("hetuṃ", "sg", False), ("hetū", "pl", False), ("hetūnaṃ", "pl", True),
            ("hetussa", "sg", True)])
a_noun("mahābhūta", "mahābhūt", "m", "महाभूत", "महाभूत", "महाभूत", "महाभूतों")
a_noun("moha", "moh", "m", "मोह", "मोह", "मोह", "मोहों")
a_noun("lobha", "lobh", "m", "लोभ", "लोभ", "लोभ", "लोभों")
a_noun("dosa", "dos", "m", "द्वेष", "द्वेष", "द्वेष", "द्वेषों")
a_noun("alobha", "alobh", "m", "लोभ का अभाव", "लोभ के अभाव", "लोभ के अभाव", "लोभ के अभावों")
a_noun("adosa", "ados", "m", "द्वेष का अभाव", "द्वेष के अभाव", "द्वेष के अभाव", "द्वेष के अभावों")
a_noun("amoha", "amoh", "m", "मोह का अभाव", "मोह के अभाव", "मोह के अभाव", "मोह के अभावों")
a_noun("rāga", "rāg", "m", "राग", "राग", "राग", "रागों")
a_noun("māna", "mān", "m", "अहंकार", "अहंकार", "अहंकार", "अहंकारों")
noun("vipāka", "m", "कर्म-फल", "कर्म-फल", "कर्म-फल", "कर्म-फलों",
     forms=[("vipāko", "sg", False), ("vipākassa", "sg", True), ("vipākaṃ", "sg", False)])
noun("gotrabhu", "m", S.GOTRABHU, forms=[("gotrabhu", "sg", False), ("gotrabhuṃ", "sg", False),
                                         ("gotrabhussa", "sg", True)])
noun("vodāna", "f", S.VODANA, forms=[("vodānaṃ", "sg", False), ("vodānassa", "sg", True)])
noun("magga", "m", "मार्ग", "मार्ग", "मार्ग", "मार्गों",
     forms=[("maggo", "sg", False), ("maggaṃ", "sg", False), ("maggassa", "sg", True), ("maggā", "pl", False)])
noun("phala", "m", "फल", "फल", "फल", "फलों", forms=[("phalaṃ", "sg", False), ("phalassa", "sg", True)])
noun("phalasamāpatti", "f", "फल की ध्यान-अवस्था",
     forms=[("phalasamāpatti", "sg", False), ("phalasamāpattiyā", "sg", True)])
noun("anuloma", "m", "अनुकूलता का क्षण", "अनुकूलता के क्षण", "अनुकूलता के क्षण", "अनुकूलता के क्षणों",
     forms=[("anulomaṃ", "sg", False), ("anulomassa", "sg", True)])
noun("āvajjanā", "f", "मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ने",
     "मन को विषय की ओर मोड़ने", forms=[("āvajjanā", "sg", False), ("āvajjanāya", "sg", True)])
noun("nibbāna", "m", S.NIBBANA, forms=[("nibbānaṃ", "sg", False), ("nibbānassa", "sg", True)])
noun("bhavaṅga", "m", "जीवन-धारा का मन", "जीवन-धारा के मन", "जीवन-धारा के मन", "जीवन-धारा के मनों",
     forms=[("bhavaṅgaṃ", "sg", False), ("bhavaṅgassa", "sg", True)])
noun("cuticitta", "m", "मृत्यु का मन", "मृत्यु के मन", "मृत्यु के मन", "मृत्यु के मनों",
     forms=[("cuticittaṃ", "sg", False)])
noun("upapatticitta", "m", "जन्म का मन", "जन्म के मन", "जन्म के मन", "जन्म के मनों",
     forms=[("upapatticittassa", "sg", True)])
noun("kāyikasukha", "m", "शारीरिक सुख", forms=[("kāyikaṃ sukhaṃ", "sg", False), ("kāyikassa sukhassa", "sg", True)])
noun("kāyikadukkha", "m", "शारीरिक दुःख", forms=[("kāyikaṃ dukkhaṃ", "sg", False),
                                                 ("kāyikassa dukkhassa", "sg", True)])
noun("utu", "m", "तापमान", forms=[("utu", "sg", False), ("utuṃ", "sg", False)])
noun("bhojana", "m", "भोजन", forms=[("bhojanaṃ", "sg", False), ("bhojanassa", "sg", True)])
noun("senāsana", "m", "निवास-स्थान", forms=[("senāsanaṃ", "sg", False)])
noun("saddhā", "f", "श्रद्धा", forms=[("saddhā", "sg", False), ("saddhaṃ", "sg", False), ("saddhāya", "sg", True)])
noun("sīla", "m", "सदाचार", forms=[("sīlaṃ", "sg", False), ("sīlassa", "sg", True)])
noun("paññā", "f", "प्रज्ञा", forms=[("paññā", "sg", False), ("paññaṃ", "sg", False), ("paññāya", "sg", True)])
noun("patthanā", "f", "कामना", forms=[("patthanā", "sg", False), ("patthanaṃ", "sg", False),
                                       ("patthanāya", "sg", True)])
noun("kusalākusalakamma", "m", "हितकर और हानिकर कर्म", forms=[("kusalākusalaṃ kammaṃ", "sg", False)])
for _p, _h in (("iddhividhañāṇ", S.IDDHIVIDHA_OBL), ("cetopariyañāṇ", S.CETOPARIYA_OBL),
               ("pubbenivāsānussatiñāṇ", S.PUBBENIVASA_OBL), ("yathākammūpagañāṇ", S.YATHAKAMMUPAGA_OBL),
               ("anāgataṃsañāṇ", S.ANAGATAMSA_OBL)):
    noun(_p, "m", _h.replace(" के ज्ञान", " का ज्ञान"), _h, _h, _h, forms=[(_p + "assa", "sg", True)])
noun("suciṇṇa", "m", "पहले भली-भाँति किए गए कार्य", "पहले भली-भाँति किए गए कार्य", S.SUCINNA, S.SUCINNA,
     forms=[("pubbe suciṇṇāni", "pl", False)])
for _p, _k in (("ākāsānañcāyatan", "ākāsānañca"), ("viññāṇañcāyatan", "viññāṇañca"),
               ("ākiñcaññāyatan", "ākiñcañña"), ("nevasaññānāsaññāyatan", "nevasaññānāsañña")):
    _h = S.ARUPA_AYATANA[_k]
    noun("arupa-" + _k, "m", _h, S.ARUPA_OBL(_k), S.ARUPA_OBL(_k), S.ARUPA_OBL(_k),
         forms=[(_p + "aṃ", "sg", False), (_p + "assa", "sg", True)])
noun("cetanā", "m", "इरादा", "इरादे", "इरादे", "इरादों",
     forms=[("cetanā", "sg", False), ("cetanaṃ", "sg", False), ("cetanāya", "sg", True)])
noun("csr", "m", S.CSR, S.CSR, S.CSR, S.CSR_OBL,
     forms=[("cittasamuṭṭhānaṃ rūpaṃ", "sg", False), ("cittasamuṭṭhānānaṃ rūpānaṃ", "pl", True),
            ("cittasamuṭṭhānā rūpā", "pl", False)])
noun("ktr", "m", S.KTR, S.KTR, S.KTR, S.KTR_OBL,
     forms=[("kaṭattārūpaṃ", "sg", False), ("kaṭattā rūpaṃ", "sg", False), ("kaṭattārūpānaṃ", "pl", True),
            ("kaṭattā rūpānaṃ", "pl", True), ("kaṭattārūpā", "pl", False)])
noun("upr", "m", S.UPR, S.UPR, S.UPR, S.UPR_OBL,
     forms=[("upādārūpaṃ", "sg", False), ("upādārūpānaṃ", "pl", True)])
noun("upādāna", "f", "आसक्ति", "आसक्तियाँ", "आसक्ति", "आसक्तियों",
     forms=[("upādānaṃ", "sg", False), ("upādānā", "pl", False), ("upādāne", "pl", False),
            ("upādānānaṃ", "pl", True), ("upādānassa", "sg", True), ("upādānāni", "pl", False)])
for _p, _h in (("kāmupādān", "इंद्रिय-सुखों के प्रति आसक्ति"), ("diṭṭhupādān", "दृष्टियों के प्रति आसक्ति"),
               ("sīlabbatupādān", "सदाचार और व्रतों के प्रति आसक्ति"), ("attavādupādān", "आत्मवाद के प्रति आसक्ति")):
    noun(_p, "f", _h, _h, _h, _h, forms=[(_p + "aṃ", "sg", False), (_p + "assa", "sg", True)])
noun("diṭṭhi", "f", "दृष्टि", "दृष्टियाँ", "दृष्टि", "दृष्टियों",
     forms=[("diṭṭhi", "sg", False), ("diṭṭhiṃ", "sg", False), ("diṭṭhiyā", "sg", True)])
noun("āhāra", "m", "आहार", "आहार", "आहार", "आहारों",
     forms=[("āhāro", "sg", False), ("āhārā", "pl", False), ("āhārānaṃ", "pl", True), ("āhāraṃ", "sg", False)])
noun("kabaḷīkāra", "m", "कौर-कौर खाया जाने वाला भोजन", "कौर-कौर खाए जाने वाले भोजन",
     "कौर-कौर खाए जाने वाले भोजन", "कौर-कौर खाए जाने वाले भोजनों",
     forms=[("kabaḷīkāro āhāro", "sg", False), ("kabaḷīkāraṃ āhāraṃ", "sg", False),
            ("kabaḷīkārassa āhārassa", "sg", True)])
noun("indriya", "f", "क्षमता", "क्षमताएँ", "क्षमता", "क्षमताओं",
     forms=[("indriyā", "pl", False), ("indriyānaṃ", "pl", True)])
noun("kāya", "m", "शरीर", "शरीर", "शरीर", "शरीरों", forms=[("kāyassa", "sg", True)])
noun("adhipati", "f", "प्रधानता", forms=[("adhipati", "sg", False)])
noun("hetuadhipati", "f", "मूल रूपी प्रधानता", forms=[("hetu adhipati", "sg", False)])
noun("vuṭṭhāna", "m", "उत्थान", forms=[("vuṭṭhānassa", "sg", True), ("vuṭṭhānaṃ", "sg", False)])
noun("parikamma", "f", "तैयारी", forms=[("parikammaṃ", "sg", False)])
noun("viññāṇa", "f", "चेतना", "चेतनाएँ", "चेतना", "चेतनाओं", forms=[("viññāṇānaṃ", "pl", True)])
noun("jhānaṅga", "m", "ध्यान का अंग", "ध्यान के अंग", "ध्यान के अंग", "ध्यान के अंगों",
     forms=[("jhānaṅgāni", "pl", False)])
noun("maggaṅga", "m", "मार्ग का अंग", "मार्ग के अंग", "मार्ग के अंग", "मार्ग के अंगों",
     forms=[("maggaṅgāni", "pl", False)])
noun("rūpajīvitindriya", "f", S.RUPAJIVITINDRIYA, forms=[("rūpajīvitindriyaṃ", "sg", False)])
noun("jīvitindriya", "f", "जीवन-क्षमता", forms=[("jīvitindriyaṃ", "sg", False)])
noun("itthindriya", "f", "स्त्रीत्व की क्षमता", forms=[("itthindriyaṃ", "sg", False), ("itthindriyassa", "sg", True)])
noun("purisindriya", "f", "पुरुषत्व की क्षमता", forms=[("purisindriyaṃ", "sg", False)])
noun("āpodhātu", "m", "जल तत्व", "जल तत्व", "जल तत्व", "जल तत्वों",
     forms=[("āpodhātu", "sg", False), ("āpodhātuṃ", "sg", False), ("āpodhātuyā", "sg", True)])
for _s in S.SENSES:
    _base = {"cakkhu": "cakkhu", "sota": "sota", "ghāna": "ghāna", "jivhā": "jivhā", "kāya": "kāya"}[_s]
    noun("vin-" + _s, "f", S.VINNANA(_s), forms=[(_base + "viññāṇaṃ", "sg", False),
                                                  (_base + "viññāṇassa", "sg", True)])
    _ay = {"cakkhu": "cakkhāyatan", "sota": "sotāyatan", "ghāna": "ghānāyatan", "jivhā": "jivhāyatan",
           "kāya": "kāyāyatan"}[_s]
    _h = S.AYA_SENSE(_s)
    noun("aya-" + _s, "m", _h, _h.replace(" का ", " के "), _h.replace(" का ", " के "),
         _h.replace(" का ", " के ") + "ों",
         forms=[(_ay + "aṃ", "sg", False), (_ay + "assa", "sg", True)])
    _ind = {"cakkhu": "cakkhundriy", "sota": "sotindriy", "ghāna": "ghānindriy", "jivhā": "jivhindriy",
            "kāya": "kāyindriy"}[_s]
    noun("ind-" + _s, "f", S.INDRIYA_SENSE(_s), forms=[(_ind + "aṃ", "sg", False), (_ind + "assa", "sg", True)])
for _o in S.OBJECTS:
    _ay = {"rūpa": "rūpāyatan", "sadda": "saddāyatan", "gandha": "gandhāyatan", "rasa": "rasāyatan",
           "phoṭṭhabba": "phoṭṭhabbāyatan"}[_o]
    _h = S.AYA_OBJ(_o)
    noun("ayo-" + _o, "m", _h, _h.replace(" का ", " के "), _h.replace(" का ", " के "),
         _h.replace(" का ", " के ") + "ों",
         forms=[(_ay + "aṃ", "sg", False), (_ay + "assa", "sg", True)])

# adjectives ----------------------------------------------------------------------------
adj("sahetuka", *vala("मूल"), stems=["sahetuk"])
adj("ahetuka", "मूल से रहित", stems=["ahetuk"])
adj("nahetu", *vala("मूल रूपी न होने"), forms=["nahetu", "nahetuṃ", "nahetū", "nahetūnaṃ", "nahetussa"])
adj("hetusampayutta", "मूलों से जुड़ा", "मूलों से जुड़े", "मूलों से जुड़ी", stems=["hetusampayutt"])
adj("hetuvippayutta", "मूलों से अलग", stems=["hetuvippayutt"])
adj("nahetusahetuka", "मूल रूपी न होने वाला, पर मूल वाला", "मूल रूपी न होने वाले, पर मूल वाले",
    "मूल रूपी न होने वाली, पर मूल वाली", stems=["nahetusahetuk"])
adj("nahetuahetuka", "मूल रूपी न होने वाला और मूल से रहित", "मूल रूपी न होने वाले और मूल से रहित",
    "मूल रूपी न होने वाली और मूल से रहित", stems=["nahetuahetuk"])
adj("sampayuttaka", "जुड़ा हुआ", "जुड़े हुए", "जुड़ी हुई",
    forms=["sampayuttakā", "sampayuttake", "sampayuttakānaṃ", "sampayuttakaṃ", "sampayuttako", "sampayuttassa"])
adj("vicikicchā", *vala("संशय के साथ होने"), group="vu", stems=["vicikicchāsahagat"])
adj("uddhacca", *vala("बेचैनी के साथ होने"), group="vu", stems=["uddhaccasahagat"])
adj("dgvlobha", *vala("ग़लत दृष्टि से अलग और लोभ के साथ होने"), stems=["diṭṭhigatavippayuttalobhasahagat"])
adj("dgv", "ग़लत दृष्टि से अलग", stems=["diṭṭhigatavippayutt"])
adj("upādānasampayutta", "आसक्ति से जुड़ा", "आसक्ति से जुड़े", "आसक्ति से जुड़ी", stems=["upādānasampayutt"])
adj("upādānavippayutta", "आसक्ति से अलग", stems=["upādānavippayutt"])
adj("noupādāna", *vala("आसक्ति रूपी न होने"), stems=["noupādān"])
adj("upādāniya", *vala("आसक्ति का विषय बनने"), stems=["upādāniy"])
adj("anupādāniya", *vala("आसक्ति का विषय न बनने"), stems=["anupādāniy"])
adj("sappaccaya", *vala("कारणों पर निर्भर रहने"), stems=["sappaccay"])
adj("appaccaya", *vala("कारणों पर निर्भर न रहने"), stems=["appaccay"])
adj("saṅkhata", "निर्मित", stems=["saṅkhat"])
adj("asaṅkhata", "अनिर्मित", stems=["asaṅkhat"])
adj("sanidassana", *vala("दिखाई देने"), stems=["sanidassan"])
adj("anidassana", *vala("दिखाई न देने"), stems=["anidassan"])
adj("sappaṭigha", *vala("टकराव"), stems=["sappaṭigh"])
adj("appaṭigha", "टकराव से रहित", stems=["appaṭigh"])
adj("rūpī", "भौतिक", forms=["rūpiṃ", "rūpī", "rūpino", "rūpīnaṃ", "rūpissa"])
adj("arūpī", "अभौतिक", forms=["arūpiṃ", "arūpī", "arūpino", "arūpīnaṃ", "arūpissa"])
adj("lokiya", "लौकिक", stems=["lokiy"])
adj("lokuttara", "लोकोत्तर", stems=["lokuttar"])
adj("kenaciviññeyya", "किसी एक प्रकार की चेतना से जाना जा सकने वाला",
    "किसी एक प्रकार की चेतना से जाने जा सकने वाले", "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    forms=["kenaci viññeyyaṃ", "kenaci viññeyyo", "kenaci viññeyyā", "kenaci viññeyye", "kenaci viññeyyānaṃ",
           "kenaci viññeyyassa"])
adj("kenacinaviññeyya", "किसी एक प्रकार की चेतना से न जाना जा सकने वाला",
    "किसी एक प्रकार की चेतना से न जाने जा सकने वाले", "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
    forms=["kenaci naviññeyyaṃ", "kenaci naviññeyyo", "kenaci naviññeyyā", "kenaci naviññeyye",
           "kenaci naviññeyyānaṃ", "kenaci naviññeyyassa"])
adj("vipāka", "कर्म के फल रूपी", forms=["vipākānaṃ", "vipākā", "vipāke"])
adj("purima", "पहले-पहले का", "पहले-पहले के", "पहले-पहले की", forms=["purimā purimā", "purimo purimo"])
adj("pacchima", "बाद-बाद का", "बाद-बाद के", "बाद-बाद की",
    forms=["pacchimānaṃ pacchimānaṃ", "pacchimassa pacchimassa"])
adj("pacchājāta", "बाद में उत्पन्न", forms=["pacchājātā", "pacchājāto"])
adj("purejāta", "पहले उत्पन्न", forms=["purejātassa"])
adj("bāhira", S.BAHIRA, forms=["bāhiraṃ", "bāhire", "bāhirā"])
adj("āhārasamuṭṭhāna", S.AHARASAM, forms=["āhārasamuṭṭhānaṃ", "āhārasamuṭṭhāne", "āhārasamuṭṭhānā"])
adj("utusamuṭṭhāna", S.UTUSAM, forms=["utusamuṭṭhānaṃ", "utusamuṭṭhāne", "utusamuṭṭhānā"])
adj("ajjhattika", "आंतरिक", forms=["ajjhattikā", "ajjhattikaṃ", "ajjhattike"])

adj("ima", "यह", "इस", "यह", forms=["imassa"])
HA["hetu-adj"] = ("मूल रूपी", "मूल रूपी", "मूल रूपी", None)
ADJF["nahetu sahetuko"] = ("nahetusahetuka", False)
ADJF["nahetu ahetuko"] = ("nahetuahetuka", False)
adj("upādāna", "आसक्ति रूपी", forms=["upādāna"])
adj("ghaṭanā", "मेल रूपी", forms=["ghaṭana"])
adj("paṭhama", "पहला", "पहले", "पहली", forms=["paṭhamo", "paṭhamassa"])
adj("dutiya", "दूसरा", "दूसरे", "दूसरी", forms=["dutiyo", "dutiyassa"])
adj("tatiya", "तीसरा", "तीसरे", "तीसरी", forms=["tatiyo", "tatiyassa"])
adj("catuttha", "चौथा", "चौथे", "चौथी", forms=["catuttho", "catutthassa"])
adj("cakkhuviññāṇasahagata", *vala("आँख की चेतना के साथ होने"), stems=["cakkhuviññāṇasahagat"])
adj("kāyaviññāṇasahagata", *vala("शरीर की चेतना के साथ होने"), stems=["kāyaviññāṇasahagat"])
# compound items (pi-1 wording), masculine forms for khandha / hetu / cetanā
adj("sahetuka-nahetu", "मूल वाला, पर स्वयं मूल रूपी न होने वाला", "मूल वाले, पर स्वयं मूल रूपी न होने वाले",
    "मूल वाली, पर स्वयं मूल रूपी न होने वाली", forms=["§snh"])
adj("upādānasampayutta-noupādāna", "आसक्ति से जुड़ा, पर स्वयं आसक्ति रूपी न होने वाला",
    "आसक्ति से जुड़े, पर स्वयं आसक्ति रूपी न होने वाले", "आसक्ति से जुड़ी, पर स्वयं आसक्ति रूपी न होने वाली",
    forms=["§usnu"])
adj("upādāniya-noupādāna", "आसक्ति का विषय बनने वाला, पर स्वयं आसक्ति रूपी न होने वाला",
    "आसक्ति का विषय बनने वाले, पर स्वयं आसक्ति रूपी न होने वाले",
    "आसक्ति का विषय बनने वाली, पर स्वयं आसक्ति रूपी न होने वाली", forms=["§uynu"])
adj("upādāna-upādānasampayutta", "आसक्ति रूपी भी और आसक्ति से जुड़ा भी", "आसक्ति रूपी भी और आसक्ति से जुड़े भी",
    "आसक्ति रूपी भी और आसक्ति से जुड़ी भी", forms=["§uus"])
COMPOUND = {
    "sahetukā ceva na ca hetū": "§snh", "sahetukānañceva na ca hetūnaṃ": "§snh", "sahetukañceva na ca hetuṃ": "§snh",
    "sahetuke ceva na ca hetū": "§snh", "sahetuko ceva na ca hetu": "§snh",
    "upādānasampayuttā ceva no ca upādānā": "§usnu", "upādānasampayuttakānañceva no ca upādānānaṃ": "§usnu",
    "upādānasampayutte ceva no ca upādāne": "§usnu", "upādānasampayuttañceva no ca upādānaṃ": "§usnu",
    "upādāniyañceva no ca upādānaṃ": "§uynu", "upādāniye ceva no ca upādāne": "§uynu",
    "upādāniyā ceva no ca upādānā": "§uynu",
    "upādānā ceva upādānasampayuttā ca": "§uus",
    "nahetu sahetukādhipati": "nahetusahetuka adhipati",
    "sahetukā ceva na ca hetu": "§snh",
    "nahetu sahetuko": "nahetusahetuko", "nahetu ahetuko": "nahetuahetuko",
    "nahetū sahetukā": "nahetusahetukā", "nahetū ahetukā": "nahetuahetukā",
    "nahetū sahetuke": "nahetusahetuke", "nahetū ahetuke": "nahetuahetuke",
    "diṭṭhigatavippayuttalobhassa": "diṭṭhigatavippayutto lobhassa",
}

# numerals ------------------------------------------------------------------------------
for _p, _h in (("ekaṃ", "एक"), ("eko", "एक"), ("dve", "दो"), ("tayo", "तीन"), ("tiṇṇannaṃ", "तीन"),
               ("dvinnaṃ", "दो"), ("pañcannaṃ", "पाँच"), ("catunnaṃ", "चार")):
    NUMF[_p] = (_h, False)

# objects in the plural (accusative), e.g. "phoṭṭhabbe aniccato"
for _p, _h in (("rūpe", "दृश्य रूप", "दृश्य रूपों"), ("sadde", "ध्वनि", "ध्वनियों"), ("gandhe", "गंध", "गंधों"),
               ("rase", "स्वाद", "स्वादों"), ("phoṭṭhabbe", "स्पर्श", "स्पर्शों")) if False else ():
    pass
for _p, _d, _o in (("rūpe", "दृश्य रूप", "दृश्य रूपों"), ("sadde", "ध्वनियाँ", "ध्वनियों"), ("gandhe", "गंध", "गंधों"),
                   ("rase", "स्वाद", "स्वादों"), ("phoṭṭhabbe", "स्पर्श", "स्पर्शों")):
    noun("obj-" + _p, "m", _d, _d, _o, _o, forms=[(_p, "pl", False)])
noun("sanidassanarūpa", "m", "दिखाई देने वाला भौतिक रूप", "दिखाई देने वाले भौतिक रूप", "दिखाई देने वाले भौतिक रूप",
     "दिखाई देने वाले भौतिक रूपों", forms=[("sanidassanaṃ rūpaṃ", "sg", False)])

# =====================================================================================
# Headings (generated) and the dyad names
# =====================================================================================
_UP = lambda s: s[:1].upper() + s[1:]
for _k in S.COND_KEYS:
    _neg = S.NEG_PREFIX_PALI[_k]
    HEAD[_UP(_k) + "paccayo"] = S.NAME(_k)
    HEAD[_UP(_k) + "paccayādi"] = S.NAME(_k) + " आदि"
    HEAD[_UP(_neg + _k) + "paccayo"] = S.NNAME(_k)
    HEAD[_UP(_neg + _k) + "paccayādi"] = S.NNAME(_k) + " आदि"
HEAD.update({
    "Kamma-vipākapaccayā": f"{N('kamma')} और {N('vipāka')}",
    "Pacchājātāsevanapaccayā": f"{N('pacchājāta')} और {N('āsevana')}",
    "Vipākāhārapaccayā": f"{N('vipāka')} और {N('āhāra')}",
    "Ārammaṇadukaṃ": S.DUKANI("ārammaṇa"),
    "Naadhipatidukaṃ": S.DUKANI("adhipati", neg=True),
    "Paccayānulomādi": S.PACCAYANULOMA + " आदि",
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों का चयन",
    "Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        "सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "Nissaya-saṃsaṭṭha-sampayuttavāro": "आश्रय, घुले-मिले होने और जुड़ाव का खंड",
})
DUKA_NAME = {
    "hetudukaṃ": S.DUKA("मूल"),
    "sahetukadukaṃ": S.DUKA("मूल वाली परिघटनाओं"),
    "hetusampayuttadukaṃ": S.DUKA("मूलों से जुड़ी परिघटनाओं"),
    "hetusahetukadukaṃ": S.DUKA("मूल रूपी भी और मूल वाली भी परिघटनाओं"),
    "hetuhetusampayuttadukaṃ": S.DUKA("मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं"),
    "nahetusahetukadukaṃ": S.DUKA("मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं"),
    "sappaccayadukaṃ": S.DUKA("कारणों पर निर्भर रहने वाली परिघटनाओं"),
    "saṅkhatadukaṃ": S.DUKA("निर्मित परिघटनाओं"),
    "sanidassanadukaṃ": S.DUKA("दिखाई देने वाली परिघटनाओं"),
    "sappaṭighadukaṃ": S.DUKA("टकराव वाली परिघटनाओं"),
    "rūpīdukaṃ": S.DUKA("भौतिक परिघटनाओं"),
    "lokiyadukaṃ": S.DUKA("लौकिक परिघटनाओं"),
    "kenaciviññeyyadukaṃ": S.DUKA("किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं"),
    "upādānadukaṃ": S.DUKA("आसक्ति"),
    "upādāniyadukaṃ": S.DUKA("आसक्ति का विषय बनने वाली परिघटनाओं"),
    "upādānasampayuttadukaṃ": S.DUKA("आसक्ति से जुड़ी परिघटनाओं"),
    "upādānaupādāniyadukaṃ": S.DUKA("आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी परिघटनाओं"),
    "upādānaupādānasampayuttadukaṃ": S.DUKA("आसक्ति रूपी भी और आसक्ति से जुड़ी भी परिघटनाओं"),
    "upādānavippayuttaupādāniyadukaṃ": S.DUKA("आसक्ति से अलग, पर उसका विषय बनने वाली परिघटनाओं"),
}
for _k, _h in DUKA_NAME.items():
    if _k != "hetudukaṃ":
        HEAD[_UP(_k)] = _h
    PH[_k + " niṭṭhitaṃ"] = _h + " समाप्त"


def _sad(x):  # "<x> के समान"
    return f"{x} के समान"


DUKA_OBL = {k: v.replace(" वाला दो का वर्गीकरण", " वाले दो के वर्गीकरण") for k, v in DUKA_NAME.items()}

# =====================================================================================
# Phrase table
# =====================================================================================
PH.update({
    # frame pieces, labels, numbers
    "paṭisandhikkhaṇe": S.PATISANDHI,
    "ahetukapaṭisandhikkhaṇe": S.AHETUKA_PATISANDHI,
    "cakkaṃ": "बारी-बारी से",
    "saṃkhittaṃ": "संक्षिप्त",
    "sahajātā": "सह-उत्पत्ति", "sahajātaṃ": "सह-उत्पत्ति", "sahajāto": "सह-उत्पत्ति",
    "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति", "pacchājātā": "पश्चात्-उत्पत्ति",
    "nānākkhaṇikā": "भिन्न क्षण", "āhāraṃ": "आहार", "indriyaṃ": "क्षमता",
    "ārammaṇādhipati": S.ARAMMANADHIPATI, "sahajātādhipati": S.SAHAJATADHIPATI,
    "ārammaṇūpanissayo": S.ARAMMANUPANISSAYA, "anantarūpanissayo": S.ANANTARUPANISSAYA,
    "pakatūpanissayo": S.PAKATUPANISSAYA,
    "anantarūpanissayo pakatūpanissayo": f"{S.ANANTARUPANISSAYA}, {S.PAKATUPANISSAYA}",
    "ārammaṇapurejātaṃ": S.ARAMMANAPUREJATA, "vatthupurejātaṃ": S.VATTHUPUREJATA,
    "ekaṃ": "एक", "dve": "दो", "tīṇi": "तीन", "cha": "छह", "nava": "नौ",
    "anulomaṃ": S.ANULOMA, "paccanīyaṃ": S.PACCANIYA, "anulomapaccanīyaṃ": S.ANULOMAPACCANIYA,
    "paccanīyānulomaṃ": S.PACCANIYANULOMA,
    "hetugocchakaṃ niṭṭhitaṃ": S.GOCCHAKA("मूलों") + " समाप्त",
    "cūḷantaradukaṃ niṭṭhitaṃ": "बीच के छोटे दो-दो के वर्गीकरण समाप्त",
    "upādānagocchakaṃ niṭṭhitaṃ": S.GOCCHAKA("आसक्ति") + " समाप्त",
    "tatiyo bhāgo niṭṭhito": "तीसरा भाग समाप्त",
    # sense objects and the like (abbreviated lists)
    "cakkhuṃ": "आँख को", "sotaṃ": "कान को", "kāyaṃ": "शरीर को", "sadde": "ध्वनियों को",
    "vatthuṃ aniccato dukkhato anattato": f"आधार को {S.ANICCA3}",
    "dibbena cakkhunā rūpaṃ passati": "दिव्य आँख से दृश्य रूप देखता है",
    "dibbāya sotadhātuyā saddaṃ suṇāti": "दिव्य कान के तत्व से ध्वनि सुनता है",
    "dibbena cakkhunā": "दिव्य आँख से",
    "domanassaṃ uppajjati": "उदासी उत्पन्न होती है",
    "diṭṭhi uppajjati": "दृष्टि उत्पन्न होती है",
    "rāgo uppajjati": "राग उत्पन्न होता है",
    "uddhaccaṃ uppajjati": "बेचैनी उत्पन्न होती है",
    "vicikicchā uddhaccaṃ domanassaṃ uppajjati": "संशय, बेचैनी और उदासी उत्पन्न होती है",
    "vicikicchā": "संशय", "uddhaccaṃ": "बेचैनी",
    "jhāne parihīne vippaṭisārissa domanassaṃ uppajjati":
        "ध्यान के छूट जाने पर ग्लानि से भरे व्यक्ति में उदासी उत्पन्न होती है",
    "assādeti abhinandati": f"{S.ASSADA.replace('का ', 'उसका ', 1)}, उस{S.ABHINANDA}",
    "arūpino khandhe garuṃ katvā assādeti": f"अभौतिक समूहों को महत्व देकर उनका रस लेता है",
    "vipassati": S.VIPASSATI,
    "saṅkhāre aniccato dukkhato anattato vipassanti": f"मानसिक रचनाओं को {S.ANICCA3} {S.VIPASSANTI}",
    "taṃ ārabbha diṭṭhigatavippayutto rāgo": "उसे विषय बनाकर ग़लत दृष्टि से अलग राग",
    # meritorious deeds
    "dānaṃ": "दान", "sīlaṃ": "सदाचार", "jhānaṃ": "ध्यान", "pubbe": "पहले", "uposathakammaṃ": "उपवास-व्रत",
    "dānaṃ datvā": "दान देकर",
    "dānaṃ datvā sīlaṃ": "दान देकर, सदाचार",
    "sīlaṃ samādiyitvā": "सदाचार ग्रहण करके",
    "uposathakammaṃ katvā": "उपवास-व्रत का पालन करके",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है",
    "uposathakammaṃ katvā taṃ paccavekkhati": f"उपवास-व्रत का पालन करके उस पर {S.REVIEW_SG}",
    "uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati": f"उपवास-व्रत का पालन करके उसे महत्व देकर उस पर {S.REVIEW_SG}",
    "uposathakammaṃ katvā taṃ assādeti abhinandati": f"उपवास-व्रत का पालन करके उस{S.ASSADA}, उस{S.ABHINANDA}",
    "uposathakammaṃ katvā taṃ garuṃ katvā assādeti abhinandati":
        f"उपवास-व्रत का पालन करके उसे महत्व देकर उस{S.ASSADA}, उस{S.ABHINANDA}",
    "uposathakammaṃ katvā taṃ paccavekkhati assādeti abhinandati":
        f"उपवास-व्रत का पालन करके उस पर {S.REVIEW_SG}, उस{S.ASSADA}, उस{S.ABHINANDA}",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati":
        f"{S.DANA3}, उसे महत्व देकर उस पर {S.REVIEW_SG}",
    "jhānā": "ध्यान से", "jhānā vuṭṭhahitvā": "ध्यान से उठकर",
    "jhānā vuṭṭhahitvā jhānaṃ": "ध्यान से उठकर ध्यान पर",
    "ariyā maggā vuṭṭhahitvā": "आर्य मार्ग से उठकर",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā": "आर्य मार्ग से उठकर मार्ग को महत्व देकर",
    "phalaṃ garuṃ katvā": "फल को महत्व देकर",
    "sekkhā gotrabhuṃ garuṃ katvā": f"{S.SEKKHA} {S.GOTRABHU} को महत्व देकर",
    "pahīne kilese": "छोड़े जा चुके मन के क्लेशों पर",
    "vikkhambhite kilese": "दबाए जा चुके मन के क्लेशों पर",
    "pubbe samudāciṇṇe": "पहले बार-बार उठे",
    "pubbe samudāciṇṇe kilese": "पहले बार-बार उठे मन के क्लेशों को",
    "pubbe samudāciṇṇe kilese jānanti": "पहले बार-बार उठे मन के क्लेशों को जानते हैं",
    "pahīne kilese paccavekkhanti": f"छोड़े जा चुके मन के क्लेशों पर {S.REVIEW_PL}",
    "vikkhambhite kilese paccavekkhanti": f"दबाए जा चुके मन के क्लेशों पर {S.REVIEW_PL}",
    "ariyā pahīne kilese": "आर्य छोड़े जा चुके मन के क्लेशों पर",
    "ariyā pahīne kilese paccavekkhanti": f"आर्य छोड़े जा चुके मन के क्लेशों पर {S.REVIEW_PL}",
    "ariyā nahetū pahīne kilese paccavekkhanti":
        f"आर्य मूल रूपी न होने वाले, छोड़े जा चुके मन के क्लेशों पर {S.REVIEW_PL}",
    "ariyā ahetuke pahīne kilese paccavekkhanti": f"आर्य मूल से रहित, छोड़े जा चुके मन के क्लेशों पर {S.REVIEW_PL}",
    "ariyā noupādāne pahīne kilese": "आर्य आसक्ति रूपी न होने वाले, छोड़े जा चुके मन के क्लेशों पर",
    "ariyā upādānavippayutte pahīne kilese": "आर्य आसक्ति से अलग, छोड़े जा चुके मन के क्लेशों पर",
    # strong support
    "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है", "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है", "mānaṃ jappeti": "अहंकार करता है",
    "pāṇaṃ hanati": "प्राणी की हत्या करता है", "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है",
    "gāmaghātaṃ karoti": "गाँव पर हमला करता है", "nigamaghātaṃ karoti": "कस्बे पर हमला करता है",
    "gāmaghātaṃ": "गाँव पर हमला", "ekāgārikaṃ": "एक ही घर में चोरी", "musā": "झूठ", "nillopaṃ": "डाका",
    "paradāraṃ": "पराई स्त्री के पास जाना", "paripanthe": "राह में घात", "pisuṇaṃ": "चुगली",
    "samphaṃ": "व्यर्थ बातें", "sandhiṃ": "सेंध",
    "ariyā maggaṃ upanissāya anuppannaṃ samāpattiṃ uppādenti":
        "आर्य मार्ग के प्रबल आश्रय से अब तक उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं",
    "uppannaṃ samāpajjanti": "उत्पन्न हो चुकी (ध्यान-अवस्था) में प्रवेश करते हैं",
    "ariyānaṃ maggo": "आर्यों का मार्ग",
    "ṭhānāṭhānakosallassa upanissayapaccayena paccayo":
        f"उचित और अनुचित की कुशलता के लिए {S.INS('upanissaya')} होता है",
    "paṭhamassa maggassa parikammaṃ paṭhamassa maggassa upanissayapaccayena paccayo":
        f"पहले मार्ग की तैयारी पहले मार्ग के लिए {S.INS('upanissaya')} होती है",
    "catutthassa maggassa parikammaṃ catutthassa maggassa upanissayapaccayena paccayo":
        f"चौथे मार्ग की तैयारी चौथे मार्ग के लिए {S.INS('upanissaya')} होती है",
    "vaṇṇasampadaṃ patthayamāno dānaṃ": "रूप-सौंदर्य की कामना करते हुए दान",
    "vaṇṇasampadā saddhāya": "रूप-सौंदर्य श्रद्धा के लिए",
    "tīṇi upanissayā": "तीनों प्रबल आश्रय",
    # adhipati compounds
    "hetu ceva sahetukādhipati sampayuttakānaṃ khandhānaṃ hetūnañca adhipatipaccayena paccayo":
        f"मूल रूपी भी और मूल वाली भी प्रधानता जुड़े हुए समूहों के लिए और मूलों के लिए {S.INS('adhipati')} होती है",
    "hetu ceva sahetukādhipati sampayuttakānaṃ hetūnaṃ adhipatipaccayena paccayo":
        f"मूल रूपी भी और मूल वाली भी प्रधानता जुड़े हुए मूलों के लिए {S.INS('adhipati')} होती है",
    "hetu ceva sahetukādhipati sampayuttakānaṃ khandhānaṃ adhipatipaccayena paccayo":
        f"मूल रूपी भी और मूल वाली भी प्रधानता जुड़े हुए समूहों के लिए {S.INS('adhipati')} होती है",
    "sahajātādhipati nahetu adhipati sampayuttakānaṃ hetūnaṃ adhipatipaccayena paccayo":
        f"{S.SAHAJATADHIPATI} मूल रूपी न होने वाली प्रधानता जुड़े हुए मूलों के लिए {S.INS('adhipati')} होती है",
    "upādāniyā ceva no ca upādānādhipati sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ "
    "adhipatipaccayena paccayo":
        "आसक्ति का विषय बनने वाली, पर स्वयं आसक्ति रूपी न होने वाली प्रधानता जुड़े हुए समूहों के लिए और "
        f"{S.CSR_OBL} के लिए {S.INS('adhipati')} होती है",
    # misc. abbreviated items
    "asaññasattānaṃ": S.ASANNASATTA, "bāhiraṃ": S.BAHIRA, "utusamuṭṭhānaṃ": S.UTUSAM,
    "āhārasamuṭṭhānaṃ": S.AHARASAM, "bāhire": S.BAHIRA, "utusamuṭṭhāne": S.UTUSAM, "āhārasamuṭṭhāne": S.AHARASAM,
    "bāhirā": S.BAHIRA, "utusamuṭṭhānā": S.UTUSAM, "āhārasamuṭṭhānā": S.AHARASAM,
    "asaññasattānaṃ ekaṃ": f"{S.ASANNASATTA} एक",
    "asaññasattānaṃ ekaṃ mahābhūtaṃ": f"{S.ASANNASATTA} एक महाभूत",
    "asaññasattānaṃ mahābhūte paṭicca rūpajīvitindriyaṃ": f"{S.ASANNASATTA} महाभूतों पर निर्भर होकर {S.RUPAJIVITINDRIYA}",
    "asaññasattānaṃ mahābhūte paṭicca sanidassanaṃ kaṭattārūpaṃ upādārūpaṃ":
        f"{S.ASANNASATTA} महाभूतों पर निर्भर होकर दिखाई देने वाला {S.KTR}, {S.UPR}",
    "asaññasattānaṃ mahābhūte paṭicca sanidassanañca anidassanañca kaṭattārūpaṃ":
        f"{S.ASANNASATTA} महाभूतों पर निर्भर होकर दिखाई देने वाला और दिखाई न देने वाला {S.KTR}",
    "asaññasattānaṃ mahābhūtā sanidassanānaṃ kaṭattārūpānaṃ":
        f"{S.ASANNASATTA} महाभूत दिखाई देने वाले {S.KTR_OBL} के लिए",
    "asaññasattānaṃ mahābhūtā sanidassanānañca anidassanānañca kaṭattārūpānaṃ upādārūpānaṃ "
    "atthipaccayena paccayo":
        f"{S.ASANNASATTA} महाभूत दिखाई देने वाले और दिखाई न देने वाले {S.KTR_OBL} के लिए और {S.UPR_OBL} के लिए "
        f"{S.INS('atthi')} होते हैं",
    "sabbe mahābhūtā": "सभी महाभूत",
    "pañcaviññāṇaṃ": "पाँच प्रकार की चेतना",
    "kāyaviññāṇasahagataṃ": "शरीर की चेतना के साथ होने वाले",
    "kāyaviññāṇasahagato": "शरीर की चेतना के साथ होने वाला",
    "nahetū ahetukā khandhā purejātassa": "मूल रूपी न होने वाले और मूल से रहित समूह पहले उत्पन्न",
    "paṭisandhikkhaṇe sahetuko": f"{S.PATISANDHI} मूल वाला",
    "vipāko appaṭigho": "टकराव से रहित कर्म-फल",
    "vipāko upādānavippayutto eko": "आसक्ति से अलग एक कर्म-फल",
    "lokuttaro dhammo": "लोकोत्तर परिघटना",
    "appaṭigho eko khandho tiṇṇannaṃ khandhānaṃ sappaṭighānañca appaṭighānañca":
        "टकराव से रहित एक समूह तीन समूहों के लिए, टकराव वालों के लिए और टकराव से रहितों के लिए",
    "ekoyeva kabaḷīkāro āhāro": "केवल एक, कौर-कौर खाया जाने वाला भोजन",
    "rūpajīvitindriyaṃ ekaṃyeva": "केवल एक, भौतिक जीवन-क्षमता",
    "kāmupādānaṃ saṃsaṭṭhaṃ diṭṭhupādānaṃ": "इंद्रिय-सुखों के प्रति आसक्ति से घुल-मिलकर दृष्टियों के प्रति आसक्ति",
    "diṭṭhupādānaṃ saṃsaṭṭhaṃ kāmupādānaṃ": "दृष्टियों के प्रति आसक्ति से घुल-मिलकर इंद्रिय-सुखों के प्रति आसक्ति",
    "lokiye ekaṃ": "लौकिक में एक", "lokuttare tīṇi": "लोकोत्तर में तीन",
    "phoṭṭhabbāyatanaṃ kāyaviññāṇassāti idaṃ natthi":
        f"{S.AYA_OBJ('phoṭṭhabba')} {S.VINNANA('kāya')} के लिए, यह नहीं है",
    "rūpāyatanaṃ cakkhuviññāṇassa": f"{S.AYA_OBJ('rūpa')} {S.VINNANA('cakkhu')} के लिए",
    # editorial notes
    "paripuṇṇaṃ": "पूर्ण", "sabbaṃ paripuṇṇaṃ": "सब पूर्ण", "paripuṇṇaṃ nava": "पूर्ण, नौ",
    "navapi paripuṇṇaṃ": "नौ के नौ पूर्ण",
    "natthi": "नहीं है", "paṭisandhi natthi": "पुनर्जन्म नहीं है", "rūpaṃ natthi": "भौतिक रूप नहीं है",
    "dvīsupi paṭisandhi natthi": "दोनों में पुनर्जन्म नहीं है",
    "āvajjanā natthi": "मन को विषय की ओर मोड़ना नहीं है",
    "āvajjanampi bhavaṅgampi natthi": "मन को विषय की ओर मोड़ना भी नहीं है, जीवन-धारा का मन भी नहीं है",
    "āvajjanāpi vuṭṭhānampi natthi": "मन को विषय की ओर मोड़ना भी नहीं है, उत्थान भी नहीं है",
    "bāhirā mahābhūtā natthi": "बाह्य महाभूत नहीं हैं",
    "yāva asaññasattā moho natthi": "पहचान-रहित प्राणियों तक; मोह नहीं है",
    "upādāniye lokuttaraṃ natthi": "आसक्ति का विषय बनने वाली में लोकोत्तर नहीं है",
    "iha ghaṭanā natthi": "यहाँ मेल नहीं है", "ghaṭanā natthi": "मेल नहीं है",
    "ghaṭanā tīṇi": "मेल में तीन", "ghaṭanā adhipati tīṇi": "मेल में प्रधानता के तीन",
    "ghaṭanādhipatipi tīṇi": "मेल में प्रधानता भी तीन",
    "tīṇi ghaṭanupanissayepi tīṇi": "तीन, मेल वाले प्रबल आश्रय में भी तीन",
    "ghaṭane tīṇipi kātabbā": "मेल में तीनों करने चाहिए",
    "ghaṭanepi tīṇi pañhā kātabbā": "मेल में भी तीन प्रश्न करने चाहिए",
    "yāva asaññasattā": f"{S.ASANNASATTA.replace(' में', '')} तक",
    "sabbe mahābhūtā yāva asaññasattā": "पहचान-रहित प्राणियों तक सभी महाभूत",
    "yāva asaññasattā tāva vitthāro": "पहचान-रहित प्राणियों तक विस्तार",
    "yāva asaññasattā kātabbaṃ": "पहचान-रहित प्राणियों तक करना चाहिए",
    "sabbaṃ yāva asaññasattā tāva kātabbaṃ": "पहचान-रहित प्राणियों तक सब करना चाहिए",
    "yāva ajjhattikā mahābhūtā": "आंतरिक महाभूतों तक",
    "yāva kāyaviññāṇaṃ": f"{S.VINNANA('kāya')} तक",
    "yāva vatthu nahetū khandhā": "आधार और मूल रूपी न होने वाले समूहों तक",
    "yāva vatthu nahetū ca khandhā tāva kātabbaṃ": "आधार और मूल रूपी न होने वाले समूहों तक करना चाहिए",
    "ca tāva kātabbaṃ": "तक करना चाहिए",
    "vitthāretabbaṃ yāva": "विस्तार करना चाहिए, तक",
    "vitthāretabbaṃ": "विस्तार करना चाहिए",
    "evaṃ vitthāretabbaṃ": "इस प्रकार विस्तार करना चाहिए",
    "evaṃ vibhajitabbaṃ": "इस प्रकार अलग-अलग दिखाना चाहिए",
    "evaṃ kātabbaṃ": "इस प्रकार करना चाहिए", "evaṃ gaṇetabbaṃ": "इस प्रकार गिनना चाहिए",
    "evaṃ sabbe kātabbā": "इस प्रकार सब करने चाहिए", "sabbe kātabbā": "सब करने चाहिए",
    "evaṃ navapi kātabbā": "इस प्रकार नौ के नौ करने चाहिए",
    "evaṃ navapi pañhā kātabbā": "इस प्रकार नौ के नौ प्रश्न करने चाहिए",
    "navapi pañhā kātabbā": "नौ के नौ प्रश्न करने चाहिए",
    "iminā kāraṇena nava pañhā kātabbā": "इसी तरीके से नौ प्रश्न करने चाहिए",
    "evaṃ avasesā pañhā": "इस प्रकार बाकी प्रश्न",
    "evaṃ avasesāpi dve gaṇanā gaṇetabbā": "इस प्रकार बाकी दो गणनाएँ भी गिननी चाहिए",
    "evaṃ indriyapaccayā vitthāretabbā": f"इस प्रकार {N('indriya')} का विस्तार करना चाहिए",
    "evaṃ sabbaṃ sappaccayagaṇanāhi saddhiṃ kātabbaṃ":
        f"इस प्रकार सब कुछ {DUKA_OBL['sappaccayadukaṃ']} की गणनाओं के साथ करना चाहिए",
    "evaṃ itare dve gaṇanāpi nissayavāropi kātabbo":
        f"इस प्रकार बाकी दो गणनाएँ भी और {S.VARA['nissaya']} भी करना चाहिए",
    "evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo":
        f"इस प्रकार बाकी दो गणनाएँ भी और {S.VARA['sampayutta']} भी करना चाहिए",
    "itare dve gaṇanāpi kātabbā": "बाकी दो गणनाएँ भी करनी चाहिए",
    "itarepi dve pañhā kātabbā": "बाकी दो प्रश्न भी करने चाहिए", "itarepi dve kātabbā": "बाकी दो भी करने चाहिए",
    "avasesā dvepi pañhā kātabbā": "बाकी दोनों प्रश्न भी करने चाहिए",
    "avasesā pañca pañhā paṭiccavārasadisā": "बाकी पाँच प्रश्न निर्भरता के खंड के समान हैं",
    "appaṭighamūlakaṃ itarepi dve pañhā kātabbā": "टकराव से रहित परिघटना से शुरू होने वाले बाकी दो प्रश्न भी करने चाहिए",
    "ajjhattikā bāhirā mahābhūtā sabbe jānitvā kātabbā": "आंतरिक और बाह्य सभी महाभूतों को जानकर करना चाहिए",
    "ime ajjhattikabāhirā mahābhūtā kātabbā": "ये आंतरिक और बाह्य महाभूत करने चाहिए",
    "sabbe mahābhūtā kātabbā": "सभी महाभूत करने चाहिए",
    "paṭisandhi vajjetabbā": "पुनर्जन्म को छोड़ देना चाहिए",
    "āsevanapaccaye vajjetabbā navapi": f"{N('āsevana')} में छोड़ देने चाहिए, नौ के नौ",
    "paṭisandhi kātabbā": "पुनर्जन्म करना चाहिए",
    "pavattipaṭisandhi kātabbā": "जीवन-काल और पुनर्जन्म करने चाहिए",
    "pavattipaṭisandhi vibhajitabbā": "जीवन-काल और पुनर्जन्म अलग-अलग दिखाने चाहिए",
    "pavattipaṭisandhi paripuṇṇaṃ": "जीवन-काल और पुनर्जन्म पूर्ण",
    "pavattipaṭisandhi satta pañhā": "जीवन-काल और पुनर्जन्म में सात प्रश्न",
    "paṭisandhi kabaḷīkāro āhāro dvīsupi kātabbo agge": "पुनर्जन्म और कौर-कौर खाया जाने वाला भोजन दोनों में सबसे पहले करना चाहिए",
    "tīsupi jīvitindriyaṃ agge kātabbaṃ": "तीनों में जीवन-क्षमता सबसे पहले करनी चाहिए",
    "tīsupi kabaḷīkāro āhāro kātabbo": "तीनों में कौर-कौर खाया जाने वाला भोजन करना चाहिए",
    "tīsupi rūpajīvitindriyaṃ": f"तीनों में {S.RUPAJIVITINDRIYA}",
    "tīsupi dvepi adhipati kātabbā": "तीनों में दोनों प्रधानताएँ करनी चाहिए",
    "tīṇipi kātabbā": "तीनों करने चाहिए", "tīṇipi": "तीनों",
    "cattāripi kātabbāni": "चारों करने चाहिए",
    "cakkaṃ kātabbaṃ": "बारी-बारी से करना चाहिए", "sabbaṃ cakkaṃ kātabbaṃ": "सबको बारी-बारी से करना चाहिए",
    "sabbe cakkā kātabbā": "सभी को बारी-बारी से करना चाहिए",
    "arūpaṃyeva kātabbaṃ": "केवल अभौतिक करना चाहिए", "arūpaṃyeva": "केवल अभौतिक", "arūpameva": "केवल अभौतिक",
    "arūpapañhāyeva": "केवल अभौतिक प्रश्न",
    "rūpaṃ chaḍḍetabbaṃ": "भौतिक रूप को छोड़ देना चाहिए",
    "rūpaṃ chaḍḍetvā arūpeyeva nava pañhā": "भौतिक रूप को छोड़कर केवल अभौतिक में नौ प्रश्न",
    "imaṃ nānaṃ": "यह अंतर है",
    "ninnānaṃ": "बिना किसी अंतर के", "ninnānākaraṇaṃ": "बिना किसी अंतर के", "ninnānākaraṇā": "बिना किसी अंतर के",
    "upādānadukasadisā ninnānā": f"{_sad(DUKA_OBL['upādānadukaṃ'])}, बिना किसी अंतर के",
    "āmasanaṃ nānākaraṇaṃ": "केवल उल्लेख में अंतर है",
    "āmasanaṃ nānākaraṇaṃ upādānadukasadisaṃ nava pañhā":
        f"केवल उल्लेख में अंतर है, {_sad(DUKA_OBL['upādānadukaṃ'])}, नौ प्रश्न",
    "pañhā": "प्रश्न", "nava pañhā": "नौ प्रश्न", "cha pañhā": "छह प्रश्न", "satta pañhā": "सात प्रश्न",
    "pañca pañhā": "पाँच प्रश्न", "cattāri cattāri pañhā": "चार-चार प्रश्न",
    "sabbattha ekāyeva pañhā": "हर जगह एक ही प्रश्न", "ekāyeva pañhā": "एक ही प्रश्न",
    "ekekassa mūle tīṇi tīṇi pañhā": "हर एक आरंभिक पद पर तीन-तीन प्रश्न",
    "dve pañhā upanissayamūlaṃ": f"{N('upanissaya')} पर आधारित दो प्रश्न",
    "saha gaṇanāhi dve pañhā": "गणनाओं सहित दो प्रश्न",
    "nahetupaccayā nava pañhā": f"{N('hetu')} के अभाव में नौ प्रश्न",
    "vipākavibhaṅge nava pañhā": f"{N('vipāka')} के विश्लेषण में नौ प्रश्न",
    "adhipatiyā nava pañhā pavatteyeva": f"{S.LOC('adhipati')} नौ प्रश्न, केवल जीवन के दौरान",
    "navapi pañhā arūpe dve upādānā": "नौ के नौ प्रश्न; अभौतिक लोक में दो आसक्तियाँ",
    "imesu dvīsu nava": "इन दोनों में नौ",
    "napacchājāte nava": f"{S.NLOC('pacchājāta')} नौ", "napurejāte nava": f"{S.NLOC('purejāta')} नौ",
    "naāsevane nava": f"{S.NLOC('āsevana')} नौ",
    "aññamaññapaccaye cha": f"{S.LOC('aññamañña')} छह", "nissayapaccaye satta pañhā": f"{S.LOC('nissaya')} सात प्रश्न",
    "sahajātapaccaye satta": f"{S.LOC('sahajāta')} सात",
    "hetumūlake tīṇi": "मूल रूपी परिघटना से शुरू होने वाले प्रश्नों में तीन",
    "nahetumūlakaṃ tīṇipi ekasadisaṃ": "मूल रूपी न होने वाली परिघटना से शुरू होने वाले तीनों प्रश्न एक समान हैं",
    "sahetuko ceva na ca hetumūlakaṃ tīṇipi ekasadisā":
        "मूल वाली, पर स्वयं मूल रूपी न होने वाली परिघटना से शुरू होने वाले तीनों प्रश्न एक समान हैं",
    "sahetukamūlakaṃ paṭiccavārasadisaṃ": "मूल वाली परिघटना से शुरू होने वाले प्रश्न निर्भरता के खंड के समान हैं",
    "sahetuko ceva na ca hetumūlake iminākārena vitthāretabbā avasesā dve pañhā":
        "मूल वाली, पर स्वयं मूल रूपी न होने वाली परिघटना से शुरू होने वाले प्रश्नों में बाकी दो प्रश्नों का इसी तरह "
        "विस्तार करना चाहिए",
    "mūlaṃ kātabbaṃ": "आरंभिक पद बनाना चाहिए", "mūlaṃ pucchitabbaṃ": "आरंभिक पद पूछना चाहिए",
    "dve mūlāni pucchitabbāni": "दो आरंभिक पद पूछने चाहिए",
    "imesaṃ dvinnampi pañhānaṃ mūlāni pucchitabbāni": "इन दोनों प्रश्नों के आरंभिक पद पूछने चाहिए",
    "dvinnampi mūlā kātabbā": "दोनों के आरंभिक पद बनाने चाहिए",
    "navapi vipākanti niyāmetabbaṃ": "नौ के नौ में “कर्म-फल” निश्चित करना चाहिए",
    "indriyanti niyāmetabbaṃ": "“क्षमता” निश्चित करनी चाहिए",
    "ahetukanti niyāmetabbaṃ": "“मूल से रहित” निश्चित करना चाहिए",
    "yathā hetupaccayā evaṃ vitthāretabbaṃ": f"जैसे {N('hetu')}, वैसे ही विस्तार करना चाहिए",
    "yathā paṭhamagamanaṃ evaṃ ninnānaṃ": "जैसे पहला दौर, वैसे ही, बिना किसी अंतर के",
    "paṭhamagamanaṃyeva": "केवल पहला दौर",
    "tattha tattha ṭhitena imaṃ kātabbaṃ dutiyagamanasadisaṃ":
        "उस-उस स्थान पर टिके रहकर इसे दूसरे दौर के समान करना चाहिए",
    "dutiyaupanissayasadisaṃ": "दूसरे प्रबल आश्रय (प्रश्न) के समान",
    "yathā paṭiccavārasadisaṃ": "जैसे निर्भरता के खंड के समान",
    "yathā hetusahetukadukaṃ evaṃ vitthāretabbaṃ":
        f"जैसे {DUKA_NAME['hetusahetukadukaṃ']}, वैसे ही विस्तार करना चाहिए",
    "yathā lokiyadukaṃ": f"जैसे {DUKA_NAME['lokiyadukaṃ']}",
    "imaṃ dukaṃ yathā sappaccayadukaṃ": f"इस दो के वर्गीकरण को, जैसे {DUKA_NAME['sappaccayadukaṃ']}",
    "imaṃ dukaṃ cūḷantaraduke lokiyadukasadisaṃ":
        f"यह दो का वर्गीकरण बीच के छोटे दो-दो के वर्गीकरणों में {_sad(DUKA_OBL['lokiyadukaṃ'])} है",
    "iminā kāraṇena vitthāretabbaṃ yathā sahetukadukaṃ ninnānākaraṇaṃ":
        f"इसी तरीके से विस्तार करना चाहिए, जैसे {DUKA_NAME['sahetukadukaṃ']}, बिना किसी अंतर के",
    "paccanīyampi itare dve gaṇanāpi upādānadukasadisaṃ":
        f"नकारात्मक क्रम भी और बाकी दो गणनाएँ भी {_sad(DUKA_OBL['upādānadukaṃ'])} हैं",
    "sabbe paccayā upādānadukasadisā": f"सभी कारण {_sad(DUKA_OBL['upādānadukaṃ'])} हैं",
    "upādānadukasadisā": _sad(DUKA_OBL["upādānadukaṃ"]),
    "itare dve upādānadukasadisā": f"बाकी दो {_sad(DUKA_OBL['upādānadukaṃ'])} हैं",
    "avasesā dvepi ārammaṇādhipati sahajātādhipatipi upādānadukasadisā":
        f"बाकी दोनों, {S.ARAMMANADHIPATI} भी और {S.SAHAJATADHIPATI} भी, {_sad(DUKA_OBL['upādānadukaṃ'])} हैं",
    "heṭṭhā adhipati tīṇi": "नीचे प्रधानता में तीन",
    "ārammaṇādhipatiyeva": f"केवल {S.ARAMMANADHIPATI}",
    "ārabbha kātabbā": "“को विषय बनाकर” करना चाहिए",
    "imesu catūsupi yathā kammapaccaye diṭṭhigatavippayutto lobho dassito evaṃ dassetabbo":
        f"इन चारों में भी, जैसे {N('kamma')} में ग़लत दृष्टि से अलग लोभ दिखाया गया है, वैसे ही दिखाना चाहिए",
    "imesu sahajātaṃ sahajātasadisaṃ": f"इनमें सह-उत्पत्ति {_sad(N('sahajāta'))}",
    "purejātaṃ purejātasadisaṃ": f"पूर्व-उत्पत्ति {_sad(N('purejāta'))}",
    "purejātasadisaṃ purejātaṃ": f"{_sad(N('purejāta'))} पूर्व-उत्पत्ति",
    "sahajātasadisaṃ sahajātaṃ vibhajitabbaṃ": f"{_sad(N('sahajāta'))} सह-उत्पत्ति को अलग-अलग दिखाना चाहिए",
    "ārammaṇapaccayamhi pañca viññāṇā kātabbā": f"{S.LOC('ārammaṇa')} पाँच प्रकार की चेतनाएँ करनी चाहिए",
    "dvepi vārā kātabbā": "दोनों खंड करने चाहिए",
    "sabbaṃ saṃkhittaṃ": "सब संक्षिप्त",
    "ime pañca pañhā hetusadisā": f"ये पाँच प्रश्न {_sad(N('hetu'))} हैं",
    "ime dvepi paṭiccasadisā": "ये दोनों निर्भरता के खंड के समान हैं",
    "tīṇipi paccayā paṭiccavāre hetusadisā": f"तीनों कारण निर्भरता के खंड में {_sad(N('hetu'))} हैं",
    "jhānampi maggampi sahajātapaccayasadisā": f"{N('jhāna')} भी और {N('magga')} भी {_sad(N('sahajāta'))} हैं",
    "nissayapaccayo paccayavāre nissayapaccayasadiso": f"{N('nissaya')} कारण के खंड में {_sad(N('nissaya'))} है",
    "paṭiccavāre nissayapaccayasadisaṃ": f"निर्भरता के खंड में {_sad(N('nissaya'))}",
    "paṭiccavāre sahajātasadisaṃ": f"निर्भरता के खंड में {_sad(N('sahajāta'))}",
    "paṭiccavāre sampayuttasadisā cha pañhā": f"निर्भरता के खंड में {_sad(N('sampayutta'))} छह प्रश्न",
    "anantarasadisaṃ": _sad(N("anantara")), "sahajātasadisaṃ": _sad(N("sahajāta")),
    "purejātasadisaṃ": _sad(N("purejāta")), "napurejātasadisaṃ": _sad(S.NNAME_OBL("purejāta")),
    "anulomasahajātasadisā": f"सकारात्मक क्रम के {_sad(N('sahajāta'))}",
    "paccayasadisaṃ": "कारण के खंड के समान",
    "paṭiccasadisaṃ": "निर्भरता के खंड के समान", "paṭiccasadisā": "निर्भरता के खंड के समान",
    "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान", "paṭiccavārasadisā": "निर्भरता के खंड के समान",
    "paṭiccavārasadisaṃyeva": "निर्भरता के खंड के समान ही",
    "paṭiccasadisaṃ yāva asaññasattā": "पहचान-रहित प्राणियों तक निर्भरता के खंड के समान",
    "paṭiccasadisā paṭhamapañhā": "पहला प्रश्न निर्भरता के खंड के समान है",
    "paccayavārasadisaṃ": "कारण के खंड के समान",
    # section notes
    "sahajātavāro paṭiccavārasadiso": f"{S.VARA['sahajāta']} निर्भरता के खंड के समान है",
    "sahajātavāropi paṭiccavārasadiso": f"{S.VARA['sahajāta']} भी निर्भरता के खंड के समान है",
    "nissayavāro paccayavārasadiso": f"{S.VARA['nissaya']} कारण के खंड के समान है",
    "nissayavāropi paccayavārasadiso": f"{S.VARA['nissaya']} भी कारण के खंड के समान है",
    "sampayuttavāro saṃsaṭṭhavārasadiso": f"{S.VARA['sampayutta']} घुले-मिले होने के खंड के समान है",
    "sampayuttavāropi saṃsaṭṭhavārasadiso": f"{S.VARA['sampayutta']} भी घुले-मिले होने के खंड के समान है",
    "nissayavāropi evaṃ kātabbo": f"{S.VARA['nissaya']} भी इसी प्रकार करना चाहिए",
    "saṃsaṭṭhavāro evaṃ vitthāretabbo": f"{S.VARA['saṃsaṭṭha']} का इसी प्रकार विस्तार करना चाहिए",
    "saṃsaṭṭhavārepi sabbattha ekaṃ": f"{S.VARA['saṃsaṭṭha'].replace('का खंड', 'के खंड')} में भी हर जगह एक",
    "sahajātavārepi evaṃ gaṇetabbaṃ": "सह-उत्पत्ति के खंड में भी इसी प्रकार गिनना चाहिए",
    "sahajātavāropi paccayavāropi nissayavāropi paṭiccavārasadisāyeva pañhā":
        "सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, निर्भरता के खंड के समान ही प्रश्न हैं",
    "saṃsaṭṭhavāropi sampayuttavāropi paripuṇṇo": "घुले-मिले होने का खंड भी, जुड़ाव का खंड भी पूर्ण है",
    "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā":
        "सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी, जुड़ाव का खंड भी "
        "निर्भरता के खंड के समान हैं",
    "evaṃ paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo":
        "इस प्रकार कारण के खंड का भी, आश्रय के खंड का भी, घुले-मिले होने के खंड का भी, जुड़ाव के खंड का भी "
        "विस्तार करना चाहिए",
    "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi evaṃ vitthāretabbā":
        "सह-उत्पत्ति के खंड का भी, कारण के खंड का भी, आश्रय के खंड का भी, घुले-मिले होने के खंड का भी, "
        "जुड़ाव के खंड का भी इसी प्रकार विस्तार करना चाहिए",
    "yathā upādānadukaṃ evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi "
    "sampayuttavāropi kātabbā":
        f"जैसे {DUKA_NAME['upādānadukaṃ']}, वैसे ही निर्भरता का खंड भी, सह-उत्पत्ति का खंड भी, कारण का खंड भी, "
        "आश्रय का खंड भी, घुले-मिले होने का खंड भी, जुड़ाव का खंड भी करना चाहिए",
    "evaṃ sabbepi vārā vitthāretabbā": "इस प्रकार सभी खंडों का विस्तार करना चाहिए",
    "paccayavāre vatthu ca pañcāyatanāni ca dassetabbāni":
        "कारण के खंड में आधार और पाँच इंद्रिय-क्षेत्र दिखाने चाहिए",
    "yathā yathā labbhati taṃ taṃ kātabbaṃ": "जैसा-जैसा मिलता है, वैसा-वैसा करना चाहिए",
    "pañcāyatanāni anulomepi paccanīyepi yathā labbhanti tathā kātabbā":
        "पाँच इंद्रिय-क्षेत्र सकारात्मक क्रम में भी और नकारात्मक क्रम में भी जैसे मिलते हैं, वैसे करने चाहिए",
    "mahābhūtesu niṭṭhitesu \"vatthuṃ paccayā\"ti kātabbā":
        "महाभूत पूरे हो जाने पर “आधार के कारण” ऐसा करना चाहिए",
    "sahajātavāro paṭiccavārasadiso vibhajantena diṭṭhupādānaṃ \"sahajātaṃ kāmupādāna\"nti kātabbaṃ":
        f"{S.VARA['sahajāta']} निर्भरता के खंड के समान है; अलग-अलग दिखाते हुए “दृष्टियों के प्रति आसक्ति के साथ "
        "जन्म लेकर इंद्रिय-सुखों के प्रति आसक्ति” ऐसा करना चाहिए",
    "upādānasampayuttañceva no ca upādānaṃ dhammaṃ paṭicca":
        "आसक्ति से जुड़ी, पर स्वयं आसक्ति रूपी न होने वाली परिघटना पर निर्भर होकर",
})
# parenthetical notes of the counting lines (looked up whole, original case)
PH.update({
    "evaṃ gaṇetabbaṃ": "इस प्रकार गिनना चाहिए",
    "evaṃ anumajjantena gaṇetabbaṃ": "इस प्रकार क्रम से जाँचते हुए गिनना चाहिए",
    "sabbattha ekaṃ": "हर जगह एक", "sabbattha dve": "हर जगह दो", "sabbattha tīṇi": "हर जगह तीन",
    "sabbattha cattāri": "हर जगह चार", "sabbattha pañca": "हर जगह पाँच", "sabbattha cha": "हर जगह छह",
    "sabbattha satta": "हर जगह सात", "sabbattha nava": "हर जगह नौ",
    "saṃkhittaṃ. Sabbattha tīṇi": "संक्षिप्त। हर जगह तीन",
    "saṃkhittaṃ. Sabbattha nava": "संक्षिप्त। हर जगह नौ",
    "saṃkhittaṃ. Sabbattha satta": "संक्षिप्त। हर जगह सात",
    "saṃkhittaṃ. Sabbattha nava, evaṃ gaṇetabbaṃ": "संक्षिप्त। हर जगह नौ, इस प्रकार गिनना चाहिए",
    "saṃkhittaṃ, sabbe kātabbā": "संक्षिप्त, सब करने चाहिए",
    "sabbe kātabbā": "सब करने चाहिए",
    "paṭiccasadisaṃ": "निर्भरता के खंड के समान",
    "anulomamātikā": "सकारात्मक क्रम की सूची",
    "anulomamātikā kātabbā": "सकारात्मक क्रम की सूची बनानी चाहिए",
    "anulomamātikā gaṇetabbā": "सकारात्मक क्रम की सूची गिननी चाहिए",
    "naanantarapadādī paccanīyasadisā": f"{S.NNAME('anantara')} वाले पद आदि नकारात्मक क्रम के समान हैं",
    "nasamanantarapadādī paccanīyasadisā": f"{S.NNAME('samanantara')} वाले पद आदि नकारात्मक क्रम के समान हैं",
    "lokuttare arūpe vipākanti niyāmetabbaṃ": "लोकोत्तर में, अभौतिक लोक में “कर्म-फल” निश्चित करना चाहिए",
    "naāsevanamūlake lokuttare suddhake vipākoti niyāmetabbaṃ, avasesā pakatikāyeva":
        f"{S.MULAKA('āsevana', neg=True)} में, लोकोत्तर में, अकेले कारण में “कर्म-फल” निश्चित करना चाहिए, "
        "बाकी सामान्य ही हैं",
    "evaṃ cattāripi gaṇanā paripuṇṇā": "इस प्रकार चारों गणनाएँ पूर्ण हैं",
    "evaṃ paccanīyagaṇanāpi kātabbā": "इस प्रकार नकारात्मक क्रम की गणना भी करनी चाहिए",
    "Evaṃ paccanīyādīni gaṇanāpi sampayuttavārepi sabbe kātabbā. Ekoyeva pañho":
        "इस प्रकार नकारात्मक क्रम आदि की गणनाएँ भी और जुड़ाव के खंड में भी सब करने चाहिए। एक ही प्रश्न है",
    "ārammaṇe noupādānamūlake pañcāyatanañca vatthuñca kātabbā":
        f"{S.LOC('ārammaṇa')}, आसक्ति रूपी न होने वाली परिघटना से शुरू होने वाले प्रश्नों में पाँच इंद्रिय-क्षेत्र "
        "और आधार करने चाहिए",
})
noun("cakkhu", "f", "आँख", "आँखें", "आँख", "आँखों", forms=[("cakkhuṃ", "sg", False)])
noun("jhāna", "m", "ध्यान", forms=[("jhānaṃ", "sg", False)])
NOUNF["cittasamuṭṭhānānaṃ rūpaṃ"] = ("csr", "sg", False)     # source slip (gen. pl. + sg.), see notes
ADJF["arūpi"] = ("arūpī", False)
ADJF["rūpi"] = ("rūpī", False)
PH.update({
    "purejātaṃ vatthu ahetukānaṃ khandhānaṃ mohassa ca purejātapaccayena paccayo":
        f"पूर्व-उत्पत्ति आधार मूल से रहित समूहों के लिए और मोह के लिए {S.INS('purejāta')} होता है",
    "hetuṃ dhammaṃ paṭicca sampayuttakā khandhā cittasamuṭṭhānañca rūpaṃ":
        f"मूल रूपी परिघटना पर निर्भर होकर जुड़े हुए समूह और {S.CSR}",
    "nirodhā vuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से उठने वाले व्यक्ति में",
})

# the variant reading in 3-01 (rendered after the word concerned)
PH["ākāsānañcāyatanakiriyaṃ (syā.) evamuparipi tīsu ṭhānesu"] = \
    "[पाठभेद (Syā.): ākāsānañcāyatanakiriyaṃ; आगे के तीन स्थानों पर भी इसी प्रकार]"
