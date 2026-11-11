"""Hindi rails builder for pi-1 chapter 2-05 (Cittuppādakaṇḍa: supramundane results, unwholesome results, functional minds).

The path segments ^1-505 … ^1-552 are compiled phrase by phrase from the Pāli with fixed strings, so that identical Pāli
gives identical Hindi; the rest are composed from the same strings. Shared formulas come from build_rails_sample.py.

usage: python -I -X utf8 build_rails_2-05.py
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\rails")
from build_rails_sample import CLOSE_OTHERS, F, OUT, PALI, S, answer_end, d, emit, hoti, question, segments  # noqa: E402

CH = "2-05-cittuppadakandam.md"

# ------------------------------------------------------------------ fixed strings
ABY = "नैतिक रूप से अनिर्धारित"
Q_AB = f"{ABY} परिघटनाएँ कौन-सी हैं?"
A_AB = f"ये {ABY} परिघटनाएँ हैं"
A_KU = "ये हितकर परिघटनाएँ हैं"
AKV = "हानिकर कर्म के फल रूपी"
KATA_AK = "हानिकर कर्म किए जाने और संचित होने के कारण कर्म के फल रूपी"
TASSEVA = "उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण,"
KIR = "केवल क्रिया रूपी"
NEVA = "न हितकर, न हानिकर, न ही कर्म-फल"
TKP = "और उस समय"
SUBJ = "कोई"
SAS = "प्रेरणा सहित"
DWELL = "प्राप्त करके उसमें रहता है"
J1 = f"इंद्रिय-सुखों से अलग होकर… पहला ध्यान {DWELL}"
V_VU = "आरंभिक विचार और सतत विचार के शांत होने से…"
J2_4 = "दूसरा ध्यान… तीसरा ध्यान… चौथा ध्यान… पहला ध्यान…"
J2_5 = f"{J2_4} पाँचवाँ ध्यान {DWELL}"
NIY = "जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला होता है"
DIT = "दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए"
SESA = "बिना कुछ शेष रखे छोड़ने के लिए"
LE2 = "इंद्रिय-सुखों के राग और दुर्भावना को क्षीण करने के लिए और दूसरे चरण की प्राप्ति के लिए"
LE3 = f"इंद्रिय-सुखों के राग और दुर्भावना को {SESA} और तीसरे चरण की प्राप्ति के लिए"
LE4 = f"सूक्ष्म भौतिक लोक के राग, अभौतिक लोक के राग, अहंकार, बेचैनी और अज्ञान को {SESA} और चौथे चरण की प्राप्ति के लिए"
Y_DITTHA = "जो इसी जीवन में सुख से रहने के लिए होता है"
EARTH = "पृथ्वी के ध्यान-मंडल पर"
ARU1 = ("भौतिक रूप की पहचानों को पूरी तरह पार कर जाने से, टकराव की पहचानों के मिट जाने से, "
        "विविधता की पहचानों पर मनोयोग न करने से और सुख को छोड़ने से…")
SUKHA_AND = "को पूरी तरह पार करके और सुख को छोड़ने से…"
MULA = f"रूपी {ABY} मूल"

F.update({
    "dukkhaṃ": ("दुःख", "m"),
    "dukkhindriyaṃ": ("दुःख की क्षमता", "f"),
    "upekkhā": ("समभाव", "m"),
    "upekkhindriyaṃ": ("समभाव की क्षमता", "f"),
    "aññindriyaṃ": ("पूर्ण ज्ञान की क्षमता", "f"),
    "aññātāvindriyaṃ": ("पूर्ण ज्ञान पा चुके की क्षमता", "f"),
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", "m"),
})

# ------------------------------------------------------------------ attribute table
PROG = {
    "dukkhapaṭipadaṃ dandhābhiñña": "दुःखद प्रगति और धीमे उच्च ज्ञान वाला",
    "dukkhapaṭipadaṃ khippābhiñña": "दुःखद प्रगति और शीघ्र उच्च ज्ञान वाला",
    "sukhapaṭipadaṃ dandhābhiñña": "सुखद प्रगति और धीमे उच्च ज्ञान वाला",
    "sukhapaṭipadaṃ khippābhiñña": "सुखद प्रगति और शीघ्र उच्च ज्ञान वाला",
    "suññata": "शून्य",
    "animitta": "चिह्नों से रहित",
    "appaṇihita": "इच्छा-रहित",
    "chandādhipateyya": "चाह की प्रधानता वाला",
    "vīriyādhipateyya": "उत्साह की प्रधानता वाला",
    "cittādhipateyya": "मन की प्रधानता वाला",
    "vīmaṃsādhipateyya": "जाँच-परख की प्रधानता वाला",
}
ATTR = "(?:" + "|".join(sorted(PROG, key=len, reverse=True)) + ")"
SEQ = f"{ATTR}(?:ṃ {ATTR})*"


def attr_hi(text):
    parts = [PROG[t] for t in re.findall(ATTR, text)]
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{parts[0]} और {parts[1]}"
    assert len(parts) == 3, text
    return f"{parts[0]}, {parts[1]} और {parts[2]}"


LOKUTTARA = {
    "jhānaṃ": "ध्यान", "maggaṃ": "मार्ग", "satipaṭṭhānaṃ": "सजगता के आधार", "sammappadhānaṃ": "सही प्रयास",
    "iddhipādaṃ": "सिद्धि के आधार", "indriyaṃ": "क्षमता", "balaṃ": "बल", "bojjhaṅgaṃ": "जागृति के अंग",
    "saccaṃ": "सत्य", "samathaṃ": "शांति", "dhammaṃ": "परिघटना", "khandhaṃ": "समूह",
    "āyatanaṃ": "इंद्रिय-क्षेत्र", "dhātuṃ": "तत्व", "āhāraṃ": "आहार", "phassaṃ": "संपर्क", "vedanaṃ": "अनुभूति",
    "saññaṃ": "पहचान", "cetanaṃ": "इरादे", "cittaṃ": "मन",
}

CLOSING = {
    "Suddhikapaṭipadā.": "केवल प्रगति का ढंग।",
    "Suddhikasuññataṃ.": "केवल शून्यता।",
    "Suññatapaṭipadā.": "शून्यता और प्रगति का ढंग।",
    "Suddhikaappaṇihitaṃ.": "केवल इच्छाओं का अभाव।",
    "Appaṇihitapaṭipadā.": "इच्छाओं का अभाव और प्रगति का ढंग।",
    "Vīsati mahānayā.": "बीस बड़ी विधियाँ।",
    "Chandādhipateyyasuddhikapaṭipadā.": "चाह की प्रधानता वाला केवल प्रगति का ढंग।",
    "Chandādhipateyyasuddhikasuññatā.": "चाह की प्रधानता वाली केवल शून्यता।",
    "Paṭhamamaggavipāko.": "पहले मार्ग का कर्म-फल रूपी मन।",
}


def compile_path(line):
    """Phrase-by-phrase Pāli to Hindi for the supramundane-result segments."""
    if line in CLOSING:
        return CLOSING[line]
    p = line.replace(" …pe…", "…pe…").replace("viharati, animittaṃ", "viharati animittaṃ")
    p = p.replace("ime dhammā kusalā tasseva", "ime dhammā kusalā. Tasseva").replace("kāmarā gabyā", "kāmarāgabyā")
    p = p.replace("Katame dhammā abyākatā? ", f"{Q_AB} ")
    p = p.replace("Yasmiṃ samaye lokuttaraṃ", f"जिस समय {SUBJ} lokuttaraṃ")
    p = re.sub(r"lokuttaraṃ (\S+?) bhāveti", lambda m: f"लोकोत्तर {LOKUTTARA[m.group(1)]} का अभ्यास करता है", p)
    p = p.replace(" niyyānikaṃ apacayagāmiṃ ", f", {NIY}, ")
    p = p.replace("diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā ", f"{DIT}, ")
    p = p.replace("kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā", LE2)
    p = p.replace("kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā", LE3)
    p = p.replace("rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā ", f"{LE4}, ")
    p = p.replace("Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati",
                  f"{TASSEVA} इंद्रिय-सुखों से अलग होकर… कर्म के फल रूपी पहला ध्यान {DWELL}")
    p = p.replace("vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati", J1)
    p = p.replace("vitakkavicārānaṃ vūpasamā…pe… ", f"{V_VU} ")
    p = p.replace("dutiyaṃ jhānaṃ…pe… tatiyaṃ jhānaṃ…pe… catutthaṃ jhānaṃ…pe… paṭhamaṃ jhānaṃ…pe… pañcamaṃ jhānaṃ upasampajja viharati", J2_5)
    p = re.sub(r"(उसमें रहता है) (?=[a-zāīūṃ])", r"\1, ", p)
    p = re.sub(rf"({SEQ})nti kusalaṃ", lambda m: f"“{attr_hi(m.group(1))}”, यह हितकर है", p)
    p = re.sub(rf"({SEQ})nti vipāko", lambda m: f"“{attr_hi(m.group(1))}”, यह कर्म-फल रूपी है", p)
    p = re.sub(rf"({SEQ})ṃ", lambda m: f"जो {attr_hi(m.group(1))} होता है", p)
    p = p.replace("tasmiṃ samaye phasso hoti", "उस समय संपर्क होता है")
    p = p.replace("aññindriyaṃ hoti", "पूर्ण ज्ञान की क्षमता होती है")
    p = p.replace("aññātāvindriyaṃ hoti", "पूर्ण ज्ञान पा चुके की क्षमता होती है")
    p = p.replace("avikkhepo hoti", "भटकाव का अभाव होता है")
    p = p.replace("ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā", CLOSE_OTHERS)
    p = p.replace("ime dhammā kusalā.", f"{A_KU}।").replace("ime dhammā abyākatā.", f"{A_AB}।")
    p = p.replace("…pe…", "…")
    assert not re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", p), p
    return p


# ------------------------------------------------------------------ non-path helpers
def rows(keys):
    return ", ".join(f"{F[k][0]} {hoti(F[k][1])}" for k in keys)


def names(keys):
    return ", ".join(F[k][0] for k in keys)


def others(tail="।"):
    return f"{CLOSE_OTHERS} – {A_AB}{tail}"


def count(ind, elem_gen):
    """elem_gen: the element's genitive before «एक तत्व», as in 2-04 (शरीर की चेतना का एक तत्व)."""
    return (f"{TKP} चार समूह होते हैं, दो इंद्रिय-क्षेत्र होते हैं, दो तत्व होते हैं, तीन आहार होते हैं, {ind} क्षमताएँ होती हैं, "
            f"एक संपर्क होता है… {elem_gen} एक तत्व होता है, मन के विषयों का एक इंद्रिय-क्षेत्र होता है, मन के विषयों का एक तत्व होता है; {others('…।')}")


def sankhara(keys):
    return (f"{question('saṅkhārakkhandho')} {names(keys)}; {CLOSE_OTHERS}, अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, "
            f"चेतना के समूह को छोड़कर – {answer_end('saṅkhārakkhandho', '…')} {A_AB}।")


def obj(last):
    return f"जिसका विषय दृश्य रूप हो… या {last}, या जिस किसी को भी वह विषय बनाए,"


def kir(elem, feeling, object_clause):
    return f"जिस समय {elem} उत्पन्न होता है, जो {KIR} है, {NEVA}, जो {feeling} है और {object_clause}"


def jhana_open(sphere):
    return f"जिस समय {SUBJ} {sphere} से संबंधित ध्यान का अभ्यास करता है, जो {KIR} है, {NEVA}, {Y_DITTHA},"


CONTACT_TO_AVIK = "उस समय संपर्क होता है… भटकाव का अभाव होता है…"
KAYA_TAIL = "शारीरिक असुहावनापन, शारीरिक दुःख, शरीर के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, शरीर के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति"
UP = "समभाव के साथ होने वाला"
SOM = "प्रसन्नता के साथ होने वाला"
UP_F = "समभाव के साथ होने वाली"
ME = "मन का तत्व"
MVE = "मन की चेतना का तत्व"
MVE_GEN = "मन की चेतना का"

L_BASE = ["phasso", "vedanā", "saññā", "cetanā", "cittaṃ"]
VV = ["vitakko", "vicāro"]
L556 = L_BASE + ["dukkhaṃ", "cittassekaggatā", "manindriyaṃ", "dukkhindriyaṃ", "jīvitindriyaṃ"]
L562 = L_BASE + VV + ["upekkhā", "cittassekaggatā", "manindriyaṃ", "upekkhindriyaṃ", "jīvitindriyaṃ"]
L568 = L_BASE + VV + ["pīti", "sukhaṃ", "cittassekaggatā", "vīriyindriyaṃ", "samādhindriyaṃ", "manindriyaṃ", "somanassindriyaṃ", "jīvitindriyaṃ"]
L574 = L_BASE + VV + ["upekkhā", "cittassekaggatā", "vīriyindriyaṃ", "samādhindriyaṃ", "manindriyaṃ", "upekkhindriyaṃ", "jīvitindriyaṃ"]
SK_561 = ["phasso", "cetanā", "cittassekaggatā", "jīvitindriyaṃ"]
SK_563 = ["phasso", "cetanā", "vitakko", "vicāro", "cittassekaggatā", "jīvitindriyaṃ"]
SK_573 = ["phasso", "cetanā", "vitakko", "vicāro", "pīti", "cittassekaggatā", "vīriyindriyaṃ", "samādhindriyaṃ", "jīvitindriyaṃ"]
SK_575 = ["phasso", "cetanā", "vitakko", "vicāro", "cittassekaggatā", "vīriyindriyaṃ", "samādhindriyaṃ", "jīvitindriyaṃ"]

SAMADHI_NO_SAMMA = S["samādhi"]
assert SAMADHI_NO_SAMMA.endswith(", सही एकाग्रता")
SAMADHI_NO_SAMMA = SAMADHI_NO_SAMMA[: -len(", सही एकाग्रता")]
VIRIYA_NO_SAMMA = S["vīriya_plain"]
assert VIRIYA_NO_SAMMA.endswith(", सही प्रयास")
VIRIYA_NO_SAMMA = VIRIYA_NO_SAMMA[: -len(", सही प्रयास")]

# ------------------------------------------------------------------ build
h = {}
for sid, plines in segments(PALI / CH):
    n = int(sid.split("-")[1]) if re.fullmatch(r"1-\d+", sid) else None
    if n is not None and 505 <= n <= 553:
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x) for x in plines]
        h[sid] = [compile_path(x) for x in lines]

h["1-1-8-0"] = ["#### लोकोत्तर कर्म-फल रूपी मन: पहले मार्ग के कर्म-फल रूपी मन"]
h["1-1-8-1-0"] = ["##### केवल प्रगति का ढंग"]
h["1-1-8-2-0"] = ["##### केवल शून्यता"]
h["1-1-8-3-0"] = ["##### शून्यता और प्रगति का ढंग"]
h["1-1-8-4-0"] = ["##### केवल इच्छाओं का अभाव"]
h["1-1-8-5-0"] = ["##### इच्छाओं का अभाव और प्रगति का ढंग"]
h["1-1-8-6-0"] = ["##### बीस बड़ी विधियाँ"]
h["1-1-8-7-0"] = ["##### चाह की प्रधानता वाला केवल प्रगति का ढंग"]
h["1-1-8-8-0"] = ["##### चाह की प्रधानता वाली केवल शून्यता"]
h["1-1-8-9-0"] = ["##### दूसरे आदि मार्गों का कर्म-फल रूपी मन"]

h["1-554"] = [d("phasso", S["phasso"], final="…।")]
h["1-555"] = [
    f"{question('aññātāvindriyaṃ')} उन पूर्ण ज्ञान पा चुकी परिघटनाओं की जो पूर्ण ज्ञान, {S['paññā']}, परिघटनाओं की छानबीन नामक जागृति का अंग, "
    f"मार्ग का अंग, मार्ग में समाया हुआ है – {answer_end('aññātāvindriyaṃ', '…')} {others()}",
    "दूसरे आदि मार्गों का कर्म-फल रूपी मन।",
    "लोकोत्तर कर्म-फल रूपी मन।",
]

# Unwholesome results
h["1-1-9-0"] = [f"#### {AKV} {ABY} मन"]
h["1-1-9-1-0"] = [f"##### {AKV} पाँच प्रकार की चेतना"]
h["1-556"] = [
    f"{Q_AB} जिस समय {KATA_AK} आँख की चेतना उत्पन्न होती है, जो {UP_F} है और जिसका विषय दृश्य रूप है… "
    f"कान की चेतना उत्पन्न होती है, जो {UP_F} है और जिसका विषय ध्वनि है… "
    f"नाक की चेतना उत्पन्न होती है, जो {UP_F} है और जिसका विषय गंध है… "
    f"जीभ की चेतना उत्पन्न होती है, जो {UP_F} है और जिसका विषय स्वाद है… "
    f"शरीर की चेतना उत्पन्न होती है, जो दुःख के साथ होने वाली है और जिसका विषय स्पर्श है, "
    f"उस समय {rows(L556)}; {others()}"
]
h["1-557"] = [d("phasso", S["phasso"])]
h["1-558"] = [d("vedanā", f"उसके अनुरूप शरीर की चेतना के तत्व के संपर्क से उत्पन्न {KAYA_TAIL}", final="…।")]
h["1-559"] = [d("dukkhaṃ", KAYA_TAIL, final="…।")]
h["1-560"] = [
    f"{d('dukkhindriyaṃ', KAYA_TAIL, final='…')} {others()}",
    count("तीन", "शरीर की चेतना का"),
]
h["1-561"] = [sankhara(SK_561), f"{AKV} पाँच प्रकार की चेतना।"]

h["1-1-9-2-0"] = [f"##### {AKV} {ME}"]
h["1-562"] = [
    f"{Q_AB} जिस समय {KATA_AK} {ME} उत्पन्न होता है, जो {UP} है और {obj('स्पर्श')} उस समय {rows(L562)}; {others('…।')}",
    count("तीन", "मन का"),
]
h["1-563"] = [sankhara(SK_563), f"{AKV} {ME}।"]

h["1-1-9-3-0"] = [f"##### {AKV} {MVE}"]
h["1-564"] = [
    f"{Q_AB} जिस समय {KATA_AK} {MVE} उत्पन्न होता है, जो {UP} है और {obj('मन का विषय')} उस समय {rows(L562)}; {others('…।')}",
    count("तीन", MVE_GEN),
]
h["1-565"] = [sankhara(SK_563), f"{AKV} {MVE}।", f"कर्म-फल रूपी {ABY} मन।"]

# Rootless functional minds
h["1-1-10-0"] = [f"#### मूल से रहित {KIR} {ABY} मन"]
h["1-1-10-1-0"] = [f"##### {KIR} {ME}"]
h["1-566"] = [
    f"{Q_AB} {kir(ME, UP, obj('स्पर्श'))} उस समय {rows(L562)}; {others('…।')}",
    count("तीन", "मन का"),
]
h["1-567"] = [sankhara(SK_563), f"{KIR} {ME}।"]

h["1-1-10-2-0"] = [f"##### {KIR}, {SOM} {MVE}"]
h["1-568"] = [f"{Q_AB} {kir(MVE, SOM, obj('मन का विषय'))} उस समय {rows(L568)}; {others()}"]
h["1-569"] = [d("phasso", S["phasso"], final="…।")]
h["1-570"] = [d("cittassekaggatā", SAMADHI_NO_SAMMA)]
h["1-571"] = [d("vīriyindriyaṃ", VIRIYA_NO_SAMMA)]
h["1-572"] = [
    f"{d('samādhindriyaṃ', SAMADHI_NO_SAMMA, final='…')} {others()}",
    count("पाँच", MVE_GEN),
]
h["1-573"] = [sankhara(SK_573), f"{KIR}, {SOM} {MVE}।"]

h["1-1-10-3-0"] = [f"##### {KIR}, {UP} {MVE}"]
h["1-574"] = [
    f"{Q_AB} {kir(MVE, UP, obj('मन का विषय'))} उस समय {rows(L574)}; {others('…।')}",
    count("पाँच", MVE_GEN),
]
h["1-575"] = [sankhara(SK_575), f"{KIR}, {UP} {MVE}।", f"मूल से रहित {KIR} {ABY} मन।"]

# Rooted functional minds of the sense sphere
SAHETUKA = f"मूल वाला, इंद्रिय-सुखों के लोक से संबंधित {KIR} मन"
h["1-1-10-4-0"] = [f"##### {SAHETUKA}"]
JS, JV = "ज्ञान से जुड़ा", "ज्ञान से अलग"
EIGHT = "… ".join(
    f"{x} और {j} होता है… {x}, {j} और {SAS} होता है" for x in (SOM, UP) for j in (JS, JV)
)
h["1-576"] = [
    f"{Q_AB} जिस समय {MVE} उत्पन्न होता है, जो {KIR} है, {NEVA}, जो {EIGHT} और {obj('मन का विषय')} "
    f"{CONTACT_TO_AVIK} {A_AB}… लोभ का अभाव {MULA}… द्वेष का अभाव {MULA}… {A_AB}।",
    f"{SAHETUKA}।",
]

# Fine-material functional minds
RUPA_KIR = f"सूक्ष्म भौतिक लोक से संबंधित {KIR} मन"
h["1-1-10-5-0"] = [f"##### {RUPA_KIR}"]
h["1-577"] = [f"{Q_AB} {jhana_open('सूक्ष्म भौतिक लोक')} इंद्रिय-सुखों से अलग होकर… {EARTH} पहला ध्यान {DWELL}, {CONTACT_TO_AVIK} {A_AB}।"]
h["1-578"] = [
    f"{Q_AB} {jhana_open('सूक्ष्म भौतिक लोक')} {V_VU} {J2_4} {EARTH} पाँचवाँ ध्यान {DWELL}, {CONTACT_TO_AVIK} {A_AB}।",
    f"{RUPA_KIR}।",
]

# Immaterial functional minds
ARUPA_KIR = f"अभौतिक लोक से संबंधित {KIR} मन"
h["1-1-10-6-0"] = [f"##### {ARUPA_KIR}"]


def arupa(entry, base):
    return (f"{Q_AB} {jhana_open('अभौतिक लोक')} {entry} {base} की पहचान के साथ होने वाला चौथा ध्यान {DWELL}, "
            f"{CONTACT_TO_AVIK} {A_AB}")


A1, A2, A3, A4 = ("अनंत आकाश के क्षेत्र", "अनंत चेतना के क्षेत्र", "कुछ भी न होने के क्षेत्र", "न पहचान, न अ-पहचान के क्षेत्र")
h["1-579"] = [arupa(ARU1, A1) + "।"]
h["1-580"] = [arupa(f"{A1} {SUKHA_AND}", A2) + "।"]
h["1-581"] = [arupa(f"{A2} {SUKHA_AND}", A3) + "।"]
h["1-582"] = [
    arupa(f"{A3} {SUKHA_AND}", A4) + f"… लोभ का अभाव {MULA}… द्वेष का अभाव {MULA}… मोह का अभाव {MULA}… {A_AB}।",
    f"{ARUPA_KIR}।",
    f"{KIR} {ABY} मन।",
    "मन की उत्पत्ति का अध्याय पूरा हुआ।",
]

if __name__ == "__main__":
    emit(PALI / CH, h, OUT / CH)
