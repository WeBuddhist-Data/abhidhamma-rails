"""Build the Hindi plain zero-shot of pi-1 part 2-05 (end of the consciousness chapter, ^1-505 ... ^1-582).

usage: python -I -X utf8 build_2-05_hi.py
Mirrors pi-1-en/build_2-05.py: each Pāli line is split at '…pe…', every chunk is translated by fixed
rules / fixed strings below (same Pāli chunk = same Hindi), and the chunks are re-joined with '…'.
Shared names, strings and frames come from the approved builders (build_matika_hi, build_ch2_01_sample_hi);
importing them does not rewrite their outputs.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_hi as M  # noqa: E402
import build_ch2_01_sample_hi as C  # noqa: E402

ROOT = HERE.parents[3]
PART = "2-05-cittuppadakandam.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / PART
OUT = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters" / PART

DASH = C.DASH
DANDA = M.DANDA
PE = "…"

KUSALA = C.KUSALA
ABYAKATA = C.ABYAKATA
Q_ABY = M.QUESTION(ABYAKATA)            # नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं?
A_ABY = M.ANSWER(ABYAKATA)              # ये नैतिक रूप से अनिर्धारित परिघटनाएँ हैं।
A_ABY_BARE = M.ANSWER_BARE(ABYAKATA)
A_KUS = M.ANSWER(KUSALA)
A_KUS_BARE = M.ANSWER_BARE(KUSALA)
YEVA_ABY = C.YEVAPANA(ABYAKATA)         # उस समय जो भी दूसरी … होती हैं – ये नैतिक रूप से अनिर्धारित परिघटनाएँ हैं।


def nodanda(s):
    assert s.endswith(DANDA), s
    return s[:-1]


# ---- headings and closing lines --------------------------------------------------------
KIR = "केवल क्रिया रूपी"
AKV = "हानिकर कर्म के फल रूपी"
HEAD = {
    # level 4: verbatim from hi-zeroshot-terms.md
    "Lokuttaravipāka-paṭhamamaggavipākā": "लोकोत्तर कर्म-फल: पहले मार्ग के कर्म-फल",
    "Akusalavipākaabyākataṃ": "हानिकर कर्म के फल रूपी नैतिक रूप से अनिर्धारित मन",
    "Ahetukakiriyāabyākataṃ": "मूल से रहित, केवल क्रिया रूपी, नैतिक रूप से अनिर्धारित मन",
    # level 5 (suddhika = केवल, paṭipadā = प्रगति के ढंग, as build_2-03_hi.py)
    "Suddhikapaṭipadā": "केवल प्रगति के ढंग",
    "Suddhikasuññataṃ": "केवल शून्यता",
    "Suññatapaṭipadā": "शून्यता के साथ प्रगति के ढंग",
    "Suddhikaappaṇihitaṃ": "केवल इच्छाओं का अभाव",
    "Appaṇihitapaṭipadā": "इच्छाओं के अभाव के साथ प्रगति के ढंग",
    "Vīsati mahānayā": "बीस मुख्य विधियाँ",
    "Chandādhipateyyasuddhikapaṭipadā": "चाह की प्रधानता के साथ केवल प्रगति के ढंग",
    "Chandādhipateyyasuddhikasuññatā": "चाह की प्रधानता के साथ केवल शून्यता",
    "Dutiyādimaggavipāko": "दूसरे और आगे के मार्गों का कर्म-फल",
    # the pattern of build_2-04_hi.py ("हितकर कर्म के फल रूपी …", "{KV}, प्रसन्नता के साथ होने वाला …")
    "Akusalavipākapañcaviññāṇāni": AKV + " पाँच प्रकार की चेतना",
    "Akusalavipākamanodhātu": AKV + " मन का तत्व",
    "Akusalavipākamanoviññāṇadhātu": AKV + " मन की चेतना का तत्व",
    "Kiriyāmanodhātu": KIR + " मन का तत्व",
    "Kiriyāmanoviññāṇadhātusomanassasahagatā": KIR + ", प्रसन्नता के साथ होने वाला मन की चेतना का तत्व",
    "Kiriyāmanoviññāṇadhātuupekkhāsahagatā": KIR + ", समभाव के साथ होने वाला मन की चेतना का तत्व",
    "Sahetukakāmāvacarakiriyā": "मूल वाला, इंद्रिय-सुखों के लोक से संबंधित " + KIR + " मन",
    "Rūpāvacarakiriyā": "सूक्ष्म भौतिक लोक से संबंधित " + KIR + " मन",
    "Arūpāvacarakiriyā": "अभौतिक लोक से संबंधित " + KIR + " मन",
}
CLOSE = {
    "Suddhikapaṭipadā.": HEAD["Suddhikapaṭipadā"] + DANDA,
    "Suddhikasuññataṃ.": HEAD["Suddhikasuññataṃ"] + DANDA,
    "Suññatapaṭipadā.": HEAD["Suññatapaṭipadā"] + DANDA,
    "Suddhikaappaṇihitaṃ.": HEAD["Suddhikaappaṇihitaṃ"] + DANDA,
    "Appaṇihitapaṭipadā.": HEAD["Appaṇihitapaṭipadā"] + DANDA,
    "Vīsati mahānayā.": HEAD["Vīsati mahānayā"] + DANDA,
    "Chandādhipateyyasuddhikapaṭipadā.": HEAD["Chandādhipateyyasuddhikapaṭipadā"] + DANDA,
    "Chandādhipateyyasuddhikasuññatā.": HEAD["Chandādhipateyyasuddhikasuññatā"] + DANDA,
    "Paṭhamamaggavipāko.": "पहले मार्ग का कर्म-फल" + DANDA,
    "Dutiyādimaggavipāko.": HEAD["Dutiyādimaggavipāko"] + DANDA,
    "Lokuttaravipāko.": "लोकोत्तर कर्म-फल" + DANDA,
    "Akusalavipākapañcaviññāṇāni.": HEAD["Akusalavipākapañcaviññāṇāni"] + DANDA,
    "Akusalavipākā manodhātu.": HEAD["Akusalavipākamanodhātu"] + DANDA,
    "Akusalavipākā manoviññāṇadhātu.": HEAD["Akusalavipākamanoviññāṇadhātu"] + DANDA,
    "Vipākā abyākatā.": "नैतिक रूप से अनिर्धारित कर्म-फल" + DANDA,  # = terms' Abyākatavipāko
    "Kiriyā manodhātu.": HEAD["Kiriyāmanodhātu"] + DANDA,
    "Kiriyā manoviññāṇadhātu somanassasahagatā.": HEAD["Kiriyāmanoviññāṇadhātusomanassasahagatā"] + DANDA,
    "Kiriyā manoviññāṇadhātu upekkhāsahagatā.": HEAD["Kiriyāmanoviññāṇadhātuupekkhāsahagatā"] + DANDA,
    "Ahetukā kiriyā abyākatā.": HEAD["Ahetukakiriyāabyākataṃ"] + DANDA,
    "Sahetukā kāmāvacarakiriyā.": HEAD["Sahetukakāmāvacarakiriyā"] + DANDA,
    "Rūpāvacarakiriyā.": HEAD["Rūpāvacarakiriyā"] + DANDA,
    "Arūpāvacarakiriyā.": HEAD["Arūpāvacarakiriyā"] + DANDA,
    "Kiriyā abyākatā.": KIR + ", नैतिक रूप से अनिर्धारित मन" + DANDA,
    "Cittuppādakaṇḍaṃ niṭṭhitaṃ.": "मन की उत्पत्ति का अध्याय पूरा हुआ" + DANDA,
}

# ---- factor names (approved sample + new ones) -----------------------------------------
NAMES_G = dict(C.NAMES_G)
NAMES_G.update({
    "dukkhaṃ": ("दुःख", C.M),
    "dukkhindriyaṃ": ("दुःख की क्षमता", C.F),                    # pi-3
    "upekkhā": ("समभाव", C.M),
    "upekkhindriyaṃ": ("समभाव की क्षमता", C.F),                 # pi-3
    "aññindriyaṃ": ("पूर्ण ज्ञान की क्षमता", C.F),               # pi-3 / pi-5
    "aññātāvindriyaṃ": ("पूर्ण ज्ञान पा चुके व्यक्ति की क्षमता", C.F),  # pi-3 / pi-5
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", C.M),          # pi-3
})
N = {k: v[0] for k, v in NAMES_G.items()}
G = {k: v[1] for k, v in NAMES_G.items()}


def HOTI(key):
    """'X hoti' in a list: 'X होता/होती है' (as LIST_ITEM in the sample)."""
    return f"{N[key]} {C.HOTI[G[key]]}"


assert HOTI("phasso") == C.LIST_ITEM("phasso")

# ---- fixed formula strings -------------------------------------------------------------
# The world-transcending wholesome clause and the result / functional frames are the same Pāli as in
# parts 2-03 (lokuttara kusala) and 2-04 (vipāka); the strings below are copied byte-for-byte from
# build_2-03_hi.py and build_2-04_hi.py (marked "2-03" / "2-04") so that identical Pāli gives identical Hindi.
THERE_CONTACT = "उस समय " + HOTI("phasso")           # tasmiṃ samaye phasso hoti
BHAVETI = "का अभ्यास करता है"                         # bhāveti (bhāvanā = मानसिक अभ्यास)  [2-03]
LEADS = ("जो " + M.BARE[("1-M2-97", "क")].replace(" परिघटनाएँ", "").replace("वाली", "वाला") + " और "
         + M.BARE[("1-M1-10", "ख")].replace(" परिघटनाएँ", "").replace("वाली", "वाला") + " है")
assert LEADS == "जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला है", LEADS  # [2-03]
STAGE = {  # [2-03]
    1: "दृष्टियों में फँसने को छोड़ने के लिए, पहले चरण की प्राप्ति के लिए",
    2: "इंद्रिय-सुखों के राग और दुर्भावना को क्षीण करने के लिए, दूसरे चरण की प्राप्ति के लिए",
    3: "इंद्रिय-सुखों के राग और दुर्भावना को पूरी तरह छोड़ने के लिए, तीसरे चरण की प्राप्ति के लिए",
    4: ("सूक्ष्म भौतिक लोक के राग, अभौतिक लोक के राग, अहंकार, बेचैनी और अज्ञान को पूरी तरह छोड़ने के लिए, "
        "चौथे चरण की प्राप्ति के लिए"),
}
VIV = "इंद्रिय-सुखों से अलग होकर"                       # vivicceva kāmehi (pi-4)  [2-03]
VUP = "आरंभिक विचार और सतत विचार के शांत होने से"        # vitakkavicārānaṃ vūpasamā (pi-4)  [2-03]
LOK_KUS = f"जिस समय कोई लोकोत्तर ध्यान {BHAVETI}, {LEADS}, और"   # [2-03] CL(): "{dev}, {LEADS}, और {STAGE}, …"
# 'Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ' (cf. 2-04 RES_OF: "… के किए जाने और
# संचित होने के कारण, उसके फल के रूप में, जब वह ")
VIPAKA_OPEN = "उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण, उसके फल के रूप में, जब वह " + VIV
AKUS_KAMMA = "जिस समय हानिकर कर्म के किए जाने और संचित होने के कारण कर्म-फल रूपी"   # cf. 2-04 RES_KAMA
KIRIYA = "जो केवल क्रिया रूपी है, न हितकर, न हानिकर और न कर्म-फल"   # kiriyā neva kusalā nākusalā na ca kammavipākā
SUKHAVIHARA = "इसी जीवन में सुख से रहने के लिए"                  # diṭṭhadhammasukhavihāraṃ (pi-5)
ACC_UPEKKHA = "जो समभाव के साथ होता है"                          # upekkhāsahagatā (m.)
ACC_SOMA = "जो प्रसन्नता के साथ होता है"                          # somanassasahagatā (m.)
assert C.ACC_SOMA_NANA.startswith(ACC_SOMA + " और ")
# object strings: pieces of the sample's ARAMMANA, byte-identical
_AR = C.ARAMMANA.split(", ")
assert len(_AR) == 7, _AR
OBJ = {
    "rūpārammaṇā vā": _AR[0],               # जिसका विषय दृश्य रूप हो
    "phoṭṭhabbārammaṇā vā": _AR[4],         # या स्पर्श
    "dhammārammaṇā vā": _AR[5],             # या मन का विषय
}
YAM_YAM = _AR[6]                            # या चाहे वह जिस किसी को भी विषय बनाए
ORD = {"paṭhamaṃ": "पहले", "dutiyaṃ": "दूसरे", "tatiyaṃ": "तीसरे", "catutthaṃ": "चौथे", "pañcamaṃ": "पाँचवें"}
ENTER = "ध्यान को प्राप्त करके उसमें रहता है"                    # jhānaṃ upasampajja viharati (pi-4)
ATTR = {
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "दुःखद प्रगति और धीमे उच्च ज्ञान वाला",
    "dukkhapaṭipadaṃ khippābhiññaṃ": "दुःखद प्रगति और शीघ्र उच्च ज्ञान वाला",
    "sukhapaṭipadaṃ dandhābhiññaṃ": "सुखद प्रगति और धीमे उच्च ज्ञान वाला",
    "sukhapaṭipadaṃ khippābhiññaṃ": "सुखद प्रगति और शीघ्र उच्च ज्ञान वाला",
    "suññataṃ": "शून्य",                           # [2-03] EMPTY
    "animittaṃ": "चिह्नों से रहित",                  # pi-5 animitto
    "appaṇihitaṃ": "इच्छा-रहित",                     # [2-03] DESIRELESS
    "chandādhipateyyaṃ": "चाह की प्रधानता वाला",     # [2-03] ADHI
    "vīriyādhipateyyaṃ": "उत्साह की प्रधानता वाला",
    "cittādhipateyyaṃ": "मन की प्रधानता वाला",
    "vīmaṃsādhipateyyaṃ": "जाँच-परख की प्रधानता वाला",
}
EARTH = "पृथ्वी के ध्यान-मंडल को आधार बनाकर"          # pathavīkasiṇaṃ  [2-04]
JO_DHYANA = "जो ध्यान"                              # the qualifiers stand in «जो ध्यान … है»  [2-03]
LABEL = {"kusalaṃ": " (हितकर)", "vipāko": " (कर्म-फल)"}
TWENTY = {  # lokuttaraṃ X bhāveti: 'लोकोत्तर X का अभ्यास करता है' (X in the oblique)
    "maggaṃ": "मार्ग",
    "satipaṭṭhānaṃ": "सजगता के आधार",
    "sammappadhānaṃ": "सही प्रयास",          # pi-3: cattāro sammappadhānā = चार सही प्रयास
    "iddhipādaṃ": "सिद्धि के आधार",
    "indriyaṃ": "क्षमता",
    "balaṃ": "बल",
    "bojjhaṅgaṃ": "जागृति के अंग",
    "saccaṃ": "सत्य",
    "samathaṃ": "शांति",
    "dhammaṃ": "परिघटना",
    "khandhaṃ": "समूह",
    "āyatanaṃ": "इंद्रिय-क्षेत्र",
    "dhātuṃ": "तत्व",
    "āhāraṃ": "आहार",
    "phassaṃ": "संपर्क",
    "vedanaṃ": "अनुभूति",
    "saññaṃ": "पहचान",
    "cetanaṃ": "इरादे",
    "cittaṃ": "मन",
}
ARUPA = {
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā ākāsānañcāyatanasaññāsahagataṃ":
        "भौतिक रूप की पहचानों को पूरी तरह पार कर जाने से, टकराव की पहचानों के मिट जाने से, विविधता की पहचानों पर "
        "मनोयोग न करने से, अनंत आकाश के क्षेत्र की पहचान के साथ",   # [2-01_2-02 PH]
    "sabbaso ākāsānañcāyatanaṃ samatikkamma viññāṇañcāyatanasaññāsahagataṃ":
        "अनंत आकाश के क्षेत्र को पूरी तरह पार करके, अनंत चेतना के क्षेत्र की पहचान के साथ",
    "sabbaso viññāṇañcāyatanaṃ samatikkamma ākiñcaññāyatanasaññāsahagataṃ":
        "अनंत चेतना के क्षेत्र को पूरी तरह पार करके, कुछ भी न होने के क्षेत्र की पहचान के साथ",
    "sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ":
        "कुछ भी न होने के क्षेत्र को पूरी तरह पार करके, न पहचान न अ-पहचान के क्षेत्र की पहचान के साथ",
}
SUKHA_PAHANA = "सुख के त्याग से"                                  # sukhassa ca pahānā (pi-4)
PROMPTED = "जो प्रेरणा के साथ उत्पन्न होता है"      # sasaṅkhārena, its own clause  [2-01_2-02 PH]


def ACC(acc, assoc):                                # [2-04]
    return f"जो {acc} के साथ होता है और {assoc} होता है"


def F_ACC(acc):                                     # for a viññāṇa (feminine)  [2-04]
    return f"जो {acc} के साथ होती है"


def VOBJ(obj):                                      # [2-04] OBJ
    return f"जिसका विषय {obj} है"


JOY, EQU, KNOW_A, KNOW_D = "प्रसन्नता", "समभाव", "ज्ञान से जुड़ा", "ज्ञान से अलग"
assert ACC(JOY, KNOW_A) == C.ACC_SOMA_NANA
CITTA_KIND = {}  # sahetuka kiriyā (m., agreeing with मन की चेतना का तत्व); 2-04 EIGHT wording
for _pa, _acc in (("somanassasahagatā", JOY), ("upekkhāsahagatā", EQU)):
    for _pk, _kn in (("ñāṇasampayuttā", KNOW_A), ("ñāṇavippayuttā", KNOW_D)):
        CITTA_KIND[f"{_pa} {_pk}"] = ACC(_acc, _kn)
        CITTA_KIND[f"{_pa} {_pk} sasaṅkhārena"] = ACC(_acc, _kn) + ", " + PROMPTED
# body-pain string: the painful counterpart of 2-04's S_KAYASUKHA, with 2-04's asāta = असुहावना (S_DUKKHA)
P_KAYA_DUKKHA = ("kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
                 "kāyasamphassajā asātā dukkhā vedanā")
S_KAYA_DUKKHA = ("शारीरिक असुहावनापन, शारीरिक दुःख, शरीर के संपर्क से उत्पन्न असुहावना, दुःखद अनुभव, "
                 "शरीर के संपर्क से उत्पन्न असुहावनी, दुःखद अनुभूति")
TAJJA_KAYA = "उसके अनुरूप शरीर की चेतना के तत्व के संपर्क से उत्पन्न"   # cf. C.TAJJA
# shortened strings (functional mind: without the path factor at the end)
assert C.S_SAMADHI.endswith(", " + N["sammāsamādhi"]) and C.S_VIRIYA.endswith(", " + N["sammāvāyāmo"])
S_SAMADHI_SHORT = C.S_SAMADHI[: -len(", " + N["sammāsamādhi"])]
S_VIRIYA_SHORT = C.S_VIRIYA[: -len(", " + N["sammāvāyāmo"])]
P_SAMADHI_SHORT = "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ"
P_VIRIYA_SHORT = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
                  "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ "
                  "vīriyindriyaṃ vīriyabalaṃ")
assert any(k.startswith(P_SAMADHI_SHORT + " sammāsamādhi") for k in C.STRINGS)
assert any(k.startswith(P_VIRIYA_SHORT + " sammāvāyāmo") for k in C.STRINGS)
P_PANNA = [k for k in C.STRINGS if k.startswith("paññā ")][0]
AÑÑA = "पूर्ण ज्ञान"                                                 # aññā (before the paññā string)
G_AÑÑATAVI = "उन पूर्ण ज्ञान पा चुकी परिघटनाओं की"                       # tesaṃ aññātāvīnaṃ dhammānaṃ (cf. C.G_JIVITA)
PATH_TAIL = "परिघटनाओं की छानबीन नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ"
P_PATH_TAIL = "dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"
APART = "अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, चेतना के समूह को छोड़कर"
KOT_AGGR = ("और उस समय चार समूह होते हैं, दो इंद्रिय-क्षेत्र होते हैं, दो तत्व होते हैं, तीन आहार होते हैं, "
            "{n} क्षमताएँ होती हैं, एक संपर्क होता है")
# «एक X होता है», as build_2-01_2-02_hi.py / 2-03 / 2-04 (एक शरीर की चेतना का तत्व होता है)
KOT_TAIL = "एक {e} का तत्व होता है, एक मन के विषयों का इंद्रिय-क्षेत्र होता है, एक मन के विषयों का तत्व होता है; या "
ELEM = {"kāyaviññāṇadhātu": "शरीर की चेतना", "manodhātu": "मन", "manoviññāṇadhātu": "मन की चेतना"}
ROOT_ABY = "नैतिक रूप से अनिर्धारित मूल"                               # abyākatamūlaṃ (cf. C.ROOT हितकर मूल)


def QA_plain(key, s):
    return C.Q(N[key]) + " " + C.A(s, N[key])


EXACT = {
    ".": DANDA,
    "avikkhepo hoti": HOTI("avikkhepo"),
    "aññindriyaṃ hoti": HOTI("aññindriyaṃ"),
    "aññātāvindriyaṃ hoti": HOTI("aññātāvindriyaṃ"),
    "ime dhammā abyākatā.": A_ABY,
    "ime dhammā abyākatā": A_ABY_BARE,
    "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā.":
        "या " + YEVA_ABY,
    "alobho abyākatamūlaṃ": N["alobho"] + ", " + ROOT_ABY,
    "adoso abyākatamūlaṃ": N["adoso"] + ", " + ROOT_ABY,
    "amoho abyākatamūlaṃ": N["amoho"] + ", " + ROOT_ABY,
    # world-transcending openers
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā vivicceva kāmehi":
        f"{Q_ABY} {LOK_KUS} {STAGE[1]}, {VIV}",
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā vitakkavicārānaṃ vūpasamā":
        f"{Q_ABY} {LOK_KUS} {STAGE[1]}, {VUP}",
    "ime dhammā kusalā. Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi":
        A_KUS + " " + VIPAKA_OPEN,
    # ^1-528: the Pāli has no full stop after kusalā (translated as written, with a semicolon)
    "ime dhammā kusalā tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi":
        A_KUS_BARE + "; " + VIPAKA_OPEN,
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ maggaṃ bhāveti":
        f"{Q_ABY} जिस समय कोई लोकोत्तर {TWENTY['maggaṃ']} {BHAVETI}",
    "lokuttaraṃ cittaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā vivicceva kāmehi":
        f"लोकोत्तर {TWENTY['cittaṃ']} {BHAVETI}, {LEADS}, और {STAGE[1]}, {VIV}",
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā":
        f"{Q_ABY} {LOK_KUS} {STAGE[2]}",
    # "kāmarā gabyāpādānaṃ": broken word in the source, read as kāmarāgabyāpādānaṃ
    "kāmarā gabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā": STAGE[3],
    "rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā vivicceva kāmehi":
        f"{STAGE[4]}, {VIV}",
    # Q/A
    "Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – ayaṃ tasmiṃ samaye phasso hoti":
        nodanda(QA_plain("phasso", C.S_PHASSA)),
    "Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – ayaṃ tasmiṃ samaye phasso hoti.":
        QA_plain("phasso", C.S_PHASSA),
    "Katamaṃ tasmiṃ samaye aññātāvindriyaṃ hoti? Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā " + P_PANNA + " "
    + P_PATH_TAIL + " – idaṃ tasmiṃ samaye aññātāvindriyaṃ hoti":
        C.Q(N["aññātāvindriyaṃ"]) + f" {G_AÑÑATAVI} जो {AÑÑA}, {C.S_PANNA}, {PATH_TAIL} है {DASH} "
        f"यह उस समय {N['aññātāvindriyaṃ']} है",
    # unwholesome results: the five kinds of consciousness
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ rūpārammaṇaṃ":
        f"{Q_ABY} {AKUS_KAMMA} आँख की चेतना उत्पन्न होती है, {F_ACC(EQU)}, {VOBJ('दृश्य रूप')}",
    "sotaviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ saddārammaṇaṃ":
        f"कान की चेतना उत्पन्न होती है, {F_ACC(EQU)}, {VOBJ('ध्वनि')}",
    "ghānaviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ gandhārammaṇaṃ":
        f"नाक की चेतना उत्पन्न होती है, {F_ACC(EQU)}, {VOBJ('गंध')}",
    "jivhāviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ rasārammaṇaṃ":
        f"जीभ की चेतना उत्पन्न होती है, {F_ACC(EQU)}, {VOBJ('स्वाद')}",
    "Katamā tasmiṃ samaye vedanā hoti? Yaṃ tasmiṃ samaye tajjākāyaviññāṇadhātusamphassajaṃ " + P_KAYA_DUKKHA
    + " – ayaṃ tasmiṃ samaye vedanā hoti":
        nodanda(C.Q(N["vedanā"]) + " " + C.A(S_KAYA_DUKKHA, N["vedanā"], TAJJA_KAYA + " ")),
    "Katamaṃ tasmiṃ samaye dukkhaṃ hoti? Yaṃ tasmiṃ samaye " + P_KAYA_DUKKHA + " – idaṃ tasmiṃ samaye dukkhaṃ hoti":
        nodanda(QA_plain("dukkhaṃ", S_KAYA_DUKKHA)),
    "Katamaṃ tasmiṃ samaye dukkhindriyaṃ hoti? Yaṃ tasmiṃ samaye " + P_KAYA_DUKKHA
    + " – idaṃ tasmiṃ samaye dukkhindriyaṃ hoti":
        nodanda(QA_plain("dukkhindriyaṃ", S_KAYA_DUKKHA)),
    "Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, tīṇindriyāni honti, eko phasso hoti":
        KOT_AGGR.format(n="तीन"),
    "Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, pañcindriyāni honti, eko phasso hoti":
        KOT_AGGR.format(n="पाँच"),
    # unwholesome results: mind element, mind-consciousness element
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākā manodhātu uppannā hoti upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} {AKUS_KAMMA} मन का तत्व उत्पन्न होता है, {ACC_UPEKKHA}, " + OBJ["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākā manoviññāṇadhātu uppannā hoti upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} {AKUS_KAMMA} मन की चेतना का तत्व उत्पन्न होता है, {ACC_UPEKKHA}, " + OBJ["rūpārammaṇā vā"],
    # functional
    "Katame dhammā abyākatā? Yasmiṃ samaye manodhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} जिस समय मन का तत्व उत्पन्न होता है, {KIRIYA}, {ACC_UPEKKHA}, " + OBJ["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā somanassasahagatā rūpārammaṇā vā":
        f"{Q_ABY} जिस समय मन की चेतना का तत्व उत्पन्न होता है, {KIRIYA}, {ACC_SOMA}, " + OBJ["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} जिस समय मन की चेतना का तत्व उत्पन्न होता है, {KIRIYA}, {ACC_UPEKKHA}, " + OBJ["rūpārammaṇā vā"],
    "Katamā tasmiṃ samaye cittassekaggatā hoti? Yā tasmiṃ samaye " + P_SAMADHI_SHORT
    + " – ayaṃ tasmiṃ samaye cittassekaggatā hoti.":
        QA_plain("cittassekaggatā", S_SAMADHI_SHORT),
    "Katamaṃ tasmiṃ samaye vīriyindriyaṃ hoti? Yo tasmiṃ samaye " + P_VIRIYA_SHORT
    + " – idaṃ tasmiṃ samaye vīriyindriyaṃ hoti.":
        QA_plain("vīriyindriyaṃ", S_VIRIYA_SHORT),
    "Katamaṃ tasmiṃ samaye samādhindriyaṃ hoti? Yā tasmiṃ samaye " + P_SAMADHI_SHORT
    + " – idaṃ tasmiṃ samaye samādhindriyaṃ hoti":
        nodanda(QA_plain("samādhindriyaṃ", S_SAMADHI_SHORT)),
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā somanassasahagatā ñāṇasampayuttā":
        f"{Q_ABY} जिस समय मन की चेतना का तत्व उत्पन्न होता है, {KIRIYA}, "
        + CITTA_KIND["somanassasahagatā ñāṇasampayuttā"],
    "upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena rūpārammaṇā vā":
        CITTA_KIND["upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena"] + ", " + OBJ["rūpārammaṇā vā"],
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha, tasmiṃ samaye phasso hoti":
        f"{OBJ['dhammārammaṇā vā']}, {YAM_YAM}, {THERE_CONTACT}",
    # fine-material and immaterial functional absorption
    "Katame dhammā abyākatā? Yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ vivicceva kāmehi":
        f"{Q_ABY} जिस समय कोई सूक्ष्म भौतिक लोक से संबंधित ध्यान {BHAVETI}, {KIRIYA}, {SUKHAVIHARA}, {VIV}",
    "Katame dhammā abyākatā? Yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ vitakkavicārānaṃ vūpasamā":
        f"{Q_ABY} जिस समय कोई सूक्ष्म भौतिक लोक से संबंधित ध्यान {BHAVETI}, {KIRIYA}, {SUKHAVIHARA}, {VUP}",
}
for k, v in CITTA_KIND.items():
    EXACT.setdefault(k, v)
for k, v in TWENTY.items():
    EXACT.setdefault(f"lokuttaraṃ {k} bhāveti", f"लोकोत्तर {v} {BHAVETI}")
for k, v in ARUPA.items():
    EXACT["Katame dhammā abyākatā? Yasmiṃ samaye arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca "
          "kammavipākaṃ diṭṭhadhammasukhavihāraṃ " + k + " sukhassa ca pahānā"] = \
        f"{Q_ABY} जिस समय कोई अभौतिक लोक से संबंधित ध्यान {BHAVETI}, {KIRIYA}, {SUKHAVIHARA}, {v}, {SUKHA_PAHANA}"

RE_PATH = re.compile(r"^(?:(?P<ord>paṭhamaṃ|dutiyaṃ|tatiyaṃ|catutthaṃ|pañcamaṃ) jhānaṃ"
                     r"(?P<enter> upasampajja viharati)?,?)?\s*(?P<attrs>.*?)"
                     r"(?P<tail>,? ?tasmiṃ samaye phasso hoti)?$")
RE_LIST = re.compile(r"^(?P<pre>.*?), tasmiṃ samaye (?P<list>(?:\S+ hoti,? ?)+); ye vā pana tasmiṃ samaye aññepi "
                     r"atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā(?P<dot>\.?)$")
RE_SANKHARA = re.compile(r"^Katamo tasmiṃ samaye saṅkhārakkhandho hoti\? (?P<list>[^;]+); ye vā pana tasmiṃ samaye "
                         r"aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā vedanākkhandhaṃ ṭhapetvā "
                         r"saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti$")
RE_KOT_TAIL = re.compile(r"^ekā (?P<e>\S+) hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti; ye vā pana tasmiṃ samaye "
                         r"aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā$")
PRE = {
    "kāyaviññāṇaṃ uppannaṃ hoti dukkhasahagataṃ phoṭṭhabbārammaṇaṃ":
        f"शरीर की चेतना उत्पन्न होती है, {F_ACC('दुःख')}, {VOBJ('स्पर्श')}",
    "phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha": OBJ["phoṭṭhabbārammaṇā vā"] + ", " + YAM_YAM,
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha": OBJ["dhammārammaṇā vā"] + ", " + YAM_YAM,
}


def attrs_hi(s):
    """Translate a run of path attributes, e.g. 'dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ'."""
    words, out, i = s.split(), [], 0
    while i < len(words):
        two = " ".join(words[i:i + 2])
        if two in ATTR:
            out.append(ATTR[two]); i += 2
        elif words[i] in ATTR:
            out.append(ATTR[words[i]]); i += 1
        else:
            raise KeyError(f"attr? {words[i]!r} in {s!r}")
    # 'A' / 'A और B' (as 2-03: PP + " और " + EMPTY) / 'A, B और C'
    return out[0] if len(out) == 1 else ", ".join(out[:-1]) + " और " + out[-1]


def tr_chunk(c):
    if c in EXACT:
        return EXACT[c]
    m = RE_LIST.match(c)
    if m:
        names = [w for w in re.split(r"\s*hoti,?\s*", m["list"]) if w]
        return (PRE[m["pre"]] + ", उस समय " + ", ".join(HOTI(w) for w in names)
                + "; या " + (YEVA_ABY if m["dot"] else nodanda(YEVA_ABY)))
    m = RE_KOT_TAIL.match(c)
    if m:
        return KOT_TAIL.format(e=ELEM[m["e"]]) + nodanda(YEVA_ABY)
    m = RE_SANKHARA.match(c)
    if m:
        names = [N[w[0].lower() + w[1:]] for w in m["list"].split()]
        return (C.Q(N["saṅkhārakkhandho"]) + " " + ", ".join(names)
                + "; या " + C.YEVAPANA_BODY + ", " + APART
                + f" {DASH} यह उस समय {N['saṅkhārakkhandho']} है")
    m = RE_PATH.match(c)
    if m and (m["ord"] or m["attrs"] or m["tail"]):
        attrs, label = m["attrs"].strip(), ""
        for lab in LABEL:
            if attrs.endswith("nti " + lab):
                attrs = attrs[: -len("nti " + lab)] + "ṃ"
                label = LABEL[lab]
        head = (f"{ORD[m['ord']]} " + (ENTER if m["enter"] else "ध्यान को")) if m["ord"] else ""
        if attrs == "pathavīkasiṇaṃ":
            head, attrs = (head + ", " if head else "") + EARTH, ""
        return ("PATH", head, attrs_hi(attrs) if attrs else "", label, bool(m["tail"]))
    raise KeyError(f"no rule for chunk: {c!r}")


def tr_line(line):
    """Join the chunks with '…'. Qualifiers of the absorption go into «जो ध्यान … है» (as 2-03): a run of
    unlabelled qualifier chunks shares one «जो ध्यान» and one «है»; a labelled chunk is closed at once."""
    if line in CLOSE:
        return CLOSE[line]
    pieces, run = [], False

    def close():
        nonlocal run
        if run:
            pieces[-1] += " है"
            run = False

    for c in (c.strip() for c in line.split("…pe…")):
        h = tr_chunk(c)
        if not isinstance(h, tuple):
            close()
            pieces.append(h)
            continue
        _, head, q, label, tail = h
        if head:
            close()
        text = head
        if q:
            if run and not head and not label:
                text = q                                    # continues «जो ध्यान A… B…»
            else:
                close()
                text += (", " if text else "") + f"{JO_DHYANA} {q}"
                run = True
                if label:
                    text += " है" + label
                    run = False
        if tail:
            if run:
                text += " है"
                run = False
            text += ", " + THERE_CONTACT
        pieces.append(text)
    close()
    out = pieces[0]
    for p in pieces[1:]:
        out += PE + ("" if p == DANDA else " ") + p
    return out


def build():
    out_lines = []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            out_lines.append("")
            continue
        m = re.match(r"^(.*?)(\s*\^[0-9A-Za-z-]+)?$", line)
        body, bid = m.group(1), m.group(2) or ""
        bid = (" " + bid.strip()) if bid else ""
        if body.startswith("#"):
            hashes, title = body.split(" ", 1)
            out_lines.append(f"{hashes} {HEAD[title]}{bid}")
        else:
            out_lines.append(tr_line(body) + bid)
    return "\n".join(out_lines).rstrip("\n") + "\n"


TEXT = build()
assert "—" not in TEXT and ":-" not in TEXT
_latin = re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]+", re.sub(r"\^[0-9A-Za-z-]+", "", TEXT))
assert not _latin, ("Latin left", _latin[:10])

if __name__ == "__main__":
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT)
