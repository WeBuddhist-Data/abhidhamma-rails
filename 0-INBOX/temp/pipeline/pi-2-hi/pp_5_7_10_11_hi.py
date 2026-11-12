# -*- coding: utf-8 -*-
"""pi-2 Hindi zero-shot, chapters 5, 7, 10, 11: shared formula strings and the Pañhāpucchaka engine.

Imported by build_5-indriyavibhango_hi.py, build_7-satipatthanavibhango_hi.py,
build_10-bojjhangavibhango_hi.py and build_11-maggangavibhango_hi.py. Writes nothing itself.

The Pañhāpucchaka (question-and-answer) lines are generated from the Pāli line itself: every matrix
term is looked up in TERMS (wording of the pi-1 Hindi matrix, 1-matika.md), so identical Pāli always
gives identical Hindi. Agreement markers in the templates: "~" -> ी/े/ा, "#" -> की/के/का, "@" -> ई/ए/आ
(feminine / masculine plural / masculine singular).
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi"
sys.path.insert(0, HERE)
import build_ch1_sample_hi as S  # noqa: E402  (approved sample: constants and assemble(); importing writes nothing)

DASH = S.DASH
ROOT = S.ROOT
PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR
ID = S.ID

# =====================================================================================  shared formulas
# --- pi-1 reused verbatim (checked in check_pi1() below) -----------------------------------------
MAGGANGA = "मार्ग का अंग, मार्ग में समाया हुआ"                          # maggaṅgaṃ maggapariyāpannaṃ
PANNA_PE = "प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि"     # paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi
VIRIYA_PE = "मानसिक रूप से उत्साह जगाना… सही प्रयास"                    # cetasiko vīriyārambho…pe… sammāvāyāmo
SATI_PE = "सजगता, बार-बार स्मरण… सही सजगता"                             # sati anussati…pe… sammāsati
SATI_SHORT = "सजगता, बार-बार स्मरण, सही सजगता"                           # sati anussati sammāsati
SAMADHI_PE = "मन की स्थिरता… सही एकाग्रता"                              # cittassa ṭhiti…pe… sammāsamādhi
SAMADHI_FULL = ("मन की स्थिरता, ठहराव, दृढ़ता, बिखराव का अभाव, भटकाव का अभाव, मन का न बिखरा होना, शांति, "
                "एकाग्रता की क्षमता, एकाग्रता का बल, सही एकाग्रता")             # pi-1 ^1-11
RAGA_PE = "राग, प्रबल राग… मन का प्रबल राग"                               # rāgo sārāgo…pe… cittassa sārāgo
DOMANASSA_DEF = ("मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
                 "मन के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति")              # pi-1 ^1-415 (without tajjā…)
FOUR_TRUTHS = ("दुःख का ज्ञान, दुःख की उत्पत्ति का ज्ञान, दुःख के अंत का ज्ञान, "
               "दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग का ज्ञान")         # pi-1 ^1-1067
SAMMAVAYAMA = (
    "यहाँ भिक्षु उत्पन्न न हुई बुरी हानिकर परिघटनाओं को उत्पन्न न होने देने के लिए चाह जगाता है, प्रयास करता है, "
    "उत्साह जगाता है, मन को तत्पर करता है, पूरा ज़ोर लगाता है, उत्पन्न हो चुकी बुरी हानिकर परिघटनाओं को छोड़ने के लिए "
    "चाह जगाता है, प्रयास करता है, उत्साह जगाता है, मन को तत्पर करता है, पूरा ज़ोर लगाता है, उत्पन्न न हुई हितकर "
    "परिघटनाओं की उत्पत्ति के लिए चाह जगाता है, प्रयास करता है, उत्साह जगाता है, मन को तत्पर करता है, पूरा ज़ोर लगाता है, "
    "उत्पन्न हो चुकी हितकर परिघटनाओं की स्थिरता के लिए, उनके लुप्त न होने के लिए, उन्हें और बढ़ाने के लिए, उनकी विपुलता "
    "के लिए, उनके अभ्यास के लिए, उनकी परिपूर्णता के लिए चाह जगाता है, प्रयास करता है, उत्साह जगाता है, मन को तत्पर "
    "करता है, पूरा ज़ोर लगाता है")                                           # pi-1 ^1-1377
VACA_DEF = ("वाणी के चार दुराचरणों से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, "
            "दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना")       # pi-1 ^1-299
KAMMANTA_DEF = ("शरीर के तीन दुराचरणों से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, "
                "दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना")   # pi-1 ^1-300
AJIVA_DEF = ("ग़लत आजीविका से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, "
             "दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना")      # pi-1 ^1-301
SANKAPPA_FULL = "सोचना, आरंभिक विचार, संकल्प, टिकाना, भली-भाँति टिकाना, मन को विषय की ओर ले जाना"  # pi-1 ^1-7
PITI_FULL = "उल्लास, आनंद, आनंदित होना, प्रमुदित होना, हर्ष, महाहर्ष, तृप्ति, उमंग"       # pi-1 ^1-9 (bracket after उमंग)
PITI_END = "मन का खिल उठना"
PASSADDHI_REST = "प्रशांति, पूरी प्रशांति, शांत होना, पूरी तरह शांत होना, पूरी तरह शांत हो चुका होना"  # pi-1 ^1-40
LOKUTTARA = ("लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला होता है, "
             "दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए, इंद्रिय-सुखों से अलग होकर… पहले ध्यान को "
             "प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है")   # pi-1 ^1-277
LOKUTTARA_HEAD = "यहाँ जिस समय भिक्षु " + LOKUTTARA                       # Idha bhikkhu yasmiṃ samaye …
PHASSA_PE = "उस समय संपर्क होता है… भटकाव का अभाव होता है"                    # tasmiṃ samaye phasso hoti…pe… avikkhepo hoti
PHASSA_PE_YO = "उस समय जो संपर्क होता है… भटकाव का अभाव होता है"              # yo tasmiṃ samaye phasso hoti…
KUSALA_END = "ये हितकर परिघटनाएँ हैं।"                                        # ime dhammā kusalā
VIPAKA = ("उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण जिस समय वह इंद्रिय-सुखों से अलग होकर… "
          "कर्म के फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला और शून्य होता है")  # pi-1 ^1-505
JHANA4 = (  # the four jhāna clauses (pi-1 ^1-160 … ^1-163), each "… को प्राप्त करके उसमें रहता है"
    "इंद्रिय-सुखों से अलग होकर, हानिकर परिघटनाओं से अलग होकर, आरंभिक विचार और सतत विचार वाले, अलगाव से उत्पन्न उल्लास "
    "और सुख वाले पहले ध्यान को प्राप्त करके उसमें रहता है; आरंभिक विचार और सतत विचार के शांत होने से, स्वयं में निर्मलता "
    "वाले, मन के एक बिंदु पर टिकने वाले, आरंभिक विचार और सतत विचार से रहित, एकाग्रता से उत्पन्न उल्लास और सुख वाले "
    "दूसरे ध्यान को प्राप्त करके उसमें रहता है; उल्लास के फीका पड़ने से वह समभाव के साथ, सजग और स्पष्ट समझ रखते हुए "
    "रहता है और काया से सुख का अनुभव करता है, जिसके बारे में आर्य कहते हैं “समभाव वाला, सजगता वाला, सुख से रहने वाला”, "
    "ऐसे तीसरे ध्यान को प्राप्त करके उसमें रहता है; सुख को छोड़ने से और दुःख को छोड़ने से, और पहले ही प्रसन्नता और उदासी "
    "के मिट जाने से, न दुःखद, न सुखद, समभाव और सजगता से पूरी तरह शुद्ध चौथे ध्यान को प्राप्त करके उसमें रहता है")

# --- new in pi-2 (also in notes-5-7-10-11.md) ----------------------------------------------------
AVASESA = "बाकी परिघटनाएँ {} से जुड़ी हैं।"                                   # Avasesā dhammā X-sampayuttā.
UPEKKHA_DEF = "समभाव, समभाव रखना, तटस्थ भाव से देखना, मन की तटस्थता"            # upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa
NISSITA = {  # vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ
    "m": "जो अलगाव पर आधारित, वैराग्य पर आधारित, समाप्ति पर आधारित और त्याग में परिणत होने वाला है",
    "f": "जो अलगाव पर आधारित, वैराग्य पर आधारित, समाप्ति पर आधारित और त्याग में परिणत होने वाली है",
}
ANUPASSI = {  # kāye kāyānupassī … (pi-5: शरीर में शरीर का अवलोकन करते हुए रहता है)
    "kaya": "शरीर में शरीर का", "vedana": "अनुभूतियों में अनुभूतियों का",
    "citta": "मन में मन का", "dhamma": "परिघटनाओं में परिघटनाओं का",
}
OBJ = {"kaya": "शरीर", "vedana": "अनुभूतियों", "citta": "मन", "dhamma": "परिघटनाओं"}  # with ajjhatta/bahiddhā
SELF = {"a": "स्वयं से संबंधित", "b": "दूसरों से संबंधित", "ab": "स्वयं और दूसरों दोनों से संबंधित"}
VIHARATI = "अवलोकन करते हुए रहता है"
FORMULA = "उद्यमी, स्पष्ट समझ रखते हुए और सजग, लोक में लालच और उदासी को दूर करके"  # ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ


def anupassi(k, self_=None):
    """[ajjhattaṃ] kāye kāyānupassī viharati"""
    if self_ is None:
        return f"{ANUPASSI[k]} {VIHARATI}"
    return f"{SELF[self_]} {OBJ[k]} में {ANUPASSI[k].split(' में ')[1]} {VIHARATI}"


def four_satipatthana(with_formula):
    """Cattāro satipaṭṭhānā – idha bhikkhu kāye kāyānupassī viharati[ ātāpī …], vedanāsu …"""
    parts = [anupassi(k) + (", " + FORMULA if with_formula else "") for k in ("kaya", "vedana", "citta", "dhamma")]
    return f"सजगता के चार आधार {DASH} यहाँ भिक्षु " + ", ".join(parts) + "।"


SB = {  # bojjhaṅgas: nominative, oblique
    "sati": "सजगता नामक जागृति का अंग",
    "dv": "परिघटनाओं की छानबीन नामक जागृति का अंग",
    "viriya": "उत्साह नामक जागृति का अंग",
    "piti": "उल्लास नामक जागृति का अंग",
    "passaddhi": "प्रशांति नामक जागृति का अंग",
    "samadhi": "एकाग्रता नामक जागृति का अंग",
    "upekkha": "समभाव नामक जागृति का अंग",
}
SB_ORDER = ["sati", "dv", "viriya", "piti", "passaddhi", "samadhi", "upekkha"]


def obl_sb(k):
    return SB[k].replace("जागृति का अंग", "जागृति के अंग")


SEVEN_SB = "जागृति के सात अंग " + DASH + " " + ", ".join(SB[k] for k in SB_ORDER) + "।"

MAGGA = {  # path factors: (Hindi, gender)
    "ditthi": ("सही दृष्टि", "f"), "sankappa": ("सही संकल्प", "m"), "vaca": ("सही वाणी", "f"),
    "kammanta": ("सही कर्म", "m"), "ajiva": ("सही आजीविका", "f"), "vayama": ("सही प्रयास", "m"),
    "sati": ("सही सजगता", "f"), "samadhi": ("सही एकाग्रता", "f"),
}
M8 = ["ditthi", "sankappa", "vaca", "kammanta", "ajiva", "vayama", "sati", "samadhi"]
M5 = ["ditthi", "sankappa", "vayama", "sati", "samadhi"]
ATTHANGIKA = "आठ अंगों वाला मार्ग"          # pi-1 aṭṭhaṅgiko maggo
PANCANGIKA = "पाँच अंगों वाला मार्ग"         # pi-1 pañcaṅgiko maggo


def what(x, g):
    """Tattha katamo/katamā X?"""
    return f"यहाँ {x} क्या है?"


def called(x, g, quoted=True, pl=False):
    """ayaṃ/idaṃ vuccati "X" -> यह “X” कहा/कही जाता/जाती है"""
    q = f"“{x}”" if quoted else x
    if pl:
        return f"ये {q} {'कहे जाते हैं' if g == 'm' else 'कही जाती हैं'}।"
    return f"यह {q} {'कहा जाता है' if g == 'm' else 'कही जाती है'}।"


# =====================================================================================  Pañhāpucchaka engine
AGR = {"f": ("ी", "की", "ई"), "m": ("े", "के", "ए"), "ms": ("ा", "का", "आ")}


def agree(t, g):
    a = AGR[g]
    return t.replace("~", a[0]).replace("#", a[1]).replace("@", a[2])


KEEP = {"na", "no", "neva", "ca", "cā", "ceva", "kenaci", "siyā"}


def nw(w):
    w = w.lower().strip()
    if w in KEEP:
        return w
    if w.endswith("ṃ"):
        w = w[:-1]
    if w.endswith("ino") or w.endswith("uno"):
        w = w[:-2]
    if w and w[-1] in "aāiīuūoe":
        w = w[:-1]
    return w


def norm(p):
    return " ".join(nw(w) for w in p.split())


VAL = "वाल~"
TERMS_RAW = {
    # triads (pi-1 matrix ^1-M1-1 … ^1-M1-22)
    "kusalā": "हितकर", "akusalā": "हानिकर", "abyākatā": "नैतिक रूप से अनिर्धारित",
    "sukhāya vedanāya sampayuttā": "सुखद अनुभूति से जुड़~",
    "dukkhāya vedanāya sampayuttā": "दुःखद अनुभूति से जुड़~",
    "adukkhamasukhāya vedanāya sampayuttā": "न दुःखद, न सुखद अनुभूति से जुड़~",
    "vipākā": "कर्म-फल रूपी", "vipākadhammadhammā": "कर्म-फल उत्पन्न करने " + VAL,
    "nevavipākanavipākadhammadhammā": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने " + VAL,
    "upādinnupādāniyā": "कर्म से उत्पन्न और आसक्ति का विषय बनने " + VAL,
    "anupādinnupādāniyā": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने " + VAL,
    "anupādinnaanupādāniyā": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने " + VAL,
    "saṃkiliṭṭhasaṃkilesikā": "क्लेशों से मलिन और क्लेशों का विषय बनने " + VAL,
    "asaṃkiliṭṭhasaṃkilesikā": "क्लेशों से मलिन न होने वाल~, पर क्लेशों का विषय बनने " + VAL,
    "asaṃkiliṭṭhaasaṃkilesikā": "क्लेशों से मलिन न होने वाल~ और क्लेशों का विषय न बनने " + VAL,
    "savitakkasavicārā": "आरंभिक विचार और सतत विचार " + VAL,
    "avitakkavicāramattā": "आरंभिक विचार से रहित, केवल सतत विचार " + VAL,
    "avitakkaavicārā": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "pītisahagatā": "उल्लास के साथ होने " + VAL, "sukhasahagatā": "सुख के साथ होने " + VAL,
    "upekkhāsahagatā": "समभाव के साथ होने " + VAL,
    "dassanena pahātabbā": "सत्य-दर्शन से छोड़~ जाने " + VAL,
    "bhāvanāya pahātabbā": "मानसिक अभ्यास से छोड़~ जाने " + VAL,
    "neva dassanena na bhāvanāya pahātabbā": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़~ जाने " + VAL,
    "dassanena pahātabbahetukā": "सत्य-दर्शन से छोड़े जाने वाले मूलों " + VAL,
    "bhāvanāya pahātabbahetukā": "मानसिक अभ्यास से छोड़े जाने वाले मूलों " + VAL,
    "neva dassanena na bhāvanāya pahātabbahetukā": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों " + VAL,
    "ācayagāmino": "संचय की ओर ले जाने " + VAL, "apacayagāmino": "संचय घटाने की ओर ले जाने " + VAL,
    "nevācayagāmināpacayagāmino": "न संचय की ओर, न संचय घटाने की ओर ले जाने " + VAL,
    "sekkhā": "सीखने के चरण #", "asekkhā": "सीखना पूरा होने के चरण #",
    "nevasekkhanāsekkhā": "न सीखने के चरण #, न सीखना पूरा होने के चरण #",
    "parittā": "सीमित", "mahaggatā": "उन्नत", "appamāṇā": "अपरिमित",
    "parittārammaṇā": "सीमित विषय " + VAL, "mahaggatārammaṇā": "उन्नत विषय " + VAL,
    "appamāṇārammaṇā": "अपरिमित विषय " + VAL,
    "hīnā": "हीन", "majjhimā": "मध्यम", "paṇītā": "उत्तम",
    "micchattaniyatā": "ग़लत दिशा में निश्चित", "sammattaniyatā": "सही दिशा में निश्चित",
    "aniyatā": "अनिश्चित", "niyatā": "निश्चित",
    "maggārammaṇā": "मार्ग को विषय बनाने " + VAL, "maggahetukā": "मार्ग को मूल बनाने " + VAL,
    "maggādhipatino": "मार्ग की प्रधानता " + VAL,
    "uppannā": "उत्पन्न हो चुक~", "anuppannā": "उत्पन्न न हु@", "uppādino": "उत्पन्न होने " + VAL,
    "atītā": "अतीत #", "anāgatā": "भविष्य #", "paccuppannā": "वर्तमान #",
    "atītārammaṇā": "अतीत के विषय " + VAL, "anāgatārammaṇā": "भविष्य के विषय " + VAL,
    "paccuppannārammaṇā": "वर्तमान के विषय " + VAL,
    "ajjhattā": "स्वयं से संबंधित", "bahiddhā": "दूसरों से संबंधित",
    "ajjhattabahiddhā": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattārammaṇā": "स्वयं से संबंधित विषय " + VAL, "bahiddhārammaṇā": "दूसरों से संबंधित विषय " + VAL,
    "ajjhattabahiddhārammaṇā": "स्वयं और दूसरों दोनों से संबंधित विषय " + VAL,
    "anidassanasappaṭighā": "दिखाई न देने वाल~, पर टकराव " + VAL,
    "anidassanaappaṭighā": "दिखाई न देने वाल~ और टकराव से रहित",
    # dyads: roots (^1-M2-1 … 6)
    "hetū": "मूल रूपी", "na hetū": "मूल रूपी न होने " + VAL,
    "sahetukā": "मूल " + VAL, "ahetukā": "मूल से रहित",
    "hetusampayuttā": "मूलों से जुड़~", "hetuvippayuttā": "मूलों से अलग",
    "na hetū sahetukā": "मूल रूपी न होने वाल~, पर मूल " + VAL,
    "na hetū ahetukā": "मूल रूपी न होने वाल~ और मूल से रहित",
    "na hetusahetuko": "मूल रूपी न होने वाल~, पर मूल " + VAL,
    "na hetuahetuko": "मूल रूपी न होने वाल~ और मूल से रहित",
    # small intermediate dyads (^1-M2-7 … 13)
    "sappaccayā": "कारणों पर निर्भर रहने " + VAL, "saṅkhatā": "निर्मित",
    "anidassanā": "दिखाई न देने " + VAL, "sappaṭighā": "टकराव " + VAL, "appaṭighā": "टकराव से रहित",
    "rūpā": "भौतिक", "arūpā": "अभौतिक", "lokiyā": "लौकिक", "lokuttarā": "लोकोत्तर",
    "kenaci viññeyyā": "किसी एक प्रकार की चेतना से जान~ जा सकने " + VAL,
    "kenaci na viññeyyā": "किसी एक प्रकार की चेतना से न जान~ जा सकने " + VAL,
    # large intermediate dyads (^1-M2-55 … 68)
    "sārammaṇā": "विषय " + VAL, "anārammaṇā": "विषय से रहित",
    "cittā": "मन रूपी", "no cittā": "मन रूपी न होने " + VAL,
    "cetasikā": "मन # सहचर", "acetasikā": "मन # सहचर न होने " + VAL,
    "cittasampayuttā": "मन से जुड़~", "cittavippayuttā": "मन से अलग",
    "cittena sampayuttaṃ": "मन से जुड़~", "cittena vippayuttaṃ": "मन से अलग",
    "cittasaṃsaṭṭhā": "मन से घुल~-मिल~", "cittavisaṃsaṭṭhā": "मन से घुल~-मिल~ न होने " + VAL,
    "cittena saṃsaṭṭhaṃ": "मन से घुल~-मिल~", "cittena visaṃsaṭṭhaṃ": "मन से घुल~-मिल~ न होने " + VAL,
    "cittasamuṭṭhānā": "मन से उत्पन्न", "no cittasamuṭṭhānā": "मन से उत्पन्न न होने " + VAL,
    "cittasahabhuno": "मन के साथ-साथ होने " + VAL, "no cittasahabhuno": "मन के साथ-साथ न होने " + VAL,
    "cittānuparivattino": "मन का अनुसरण करने " + VAL, "no cittānuparivattino": "मन का अनुसरण न करने " + VAL,
    "cittasaṃsaṭṭhasamuṭṭhānā": "मन से घुल~-मिल~ और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhuno": "मन से घुल~-मिल~, मन से उत्पन्न और मन के साथ-साथ होने " + VAL,
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "मन से घुल~-मिल~, मन से उत्पन्न और मन का अनुसरण करने " + VAL,
    "ajjhattikā": "आंतरिक", "bāhirā": "बाह्य",
    "upādā": "व्युत्पन्न", "no upādā": "व्युत्पन्न न होने " + VAL,
    "upādinnā": "कर्म से उत्पन्न", "anupādinnā": "कर्म से उत्पन्न न होने " + VAL,
    # last dyads (^1-M2-83 … 100)
    "na dassanena pahātabbā": "सत्य-दर्शन से न छोड़~ जाने " + VAL,
    "na bhāvanāya pahātabbā": "मानसिक अभ्यास से न छोड़~ जाने " + VAL,
    "na dassanena pahātabbahetukā": "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित",
    "na bhāvanāya pahātabbahetukā": "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित",
    "savitakkā": "आरंभिक विचार " + VAL, "avitakkā": "आरंभिक विचार से रहित",
    "savicārā": "सतत विचार " + VAL, "avicārā": "सतत विचार से रहित",
    "sappītikā": "उल्लास " + VAL, "appītikā": "उल्लास से रहित",
    "na pītisahagatā": "उल्लास के साथ न होने " + VAL, "na sukhasahagatā": "सुख के साथ न होने " + VAL,
    "na upekkhāsahagatā": "समभाव के साथ न होने " + VAL,
    "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित",
    "na kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित न होने " + VAL,
    "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित",
    "na rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित न होने " + VAL,
    "arūpāvacarā": "अभौतिक लोक से संबंधित",
    "na arūpāvacarā": "अभौतिक लोक से संबंधित न होने " + VAL,
    "pariyāpannā": {"f": "अस्तित्व के लोकों में समाई हुई", "m": "अस्तित्व के लोकों में समाए हुए",
                    "ms": "अस्तित्व के लोकों में समाया हुआ"},
    "apariyāpannā": {"f": "अस्तित्व के लोकों में न समाई हुई", "m": "अस्तित्व के लोकों में न समाए हुए",
                     "ms": "अस्तित्व के लोकों में न समाया हुआ"},
    "niyyānikā": "मुक्ति की ओर ले जाने " + VAL, "aniyyānikā": "मुक्ति की ओर न ले जाने " + VAL,
    "sauttarā": "सर्वोच्च न होने " + VAL, "anuttarā": "सर्वोच्च",
    "saraṇā": "संघर्ष " + VAL, "araṇā": "संघर्ष से रहित",
}
# negations rendered as "X नहीं होती/होते" (no matrix label of their own)
NEG_RAW = {
    "no cittasaṃsaṭṭhasamuṭṭhānā": "cittasaṃsaṭṭhasamuṭṭhānā",
    "no cittasaṃsaṭṭhasamuṭṭhānasahabhuno": "cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
    "no cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
}

# the defilement groups (^1-M2-14 … 82): (G, niya, aniya, sampayutta, vippayutta, vipp+niya, vipp+aniya), X1, X2, ref
GROUPS = [
    (("āsavā", "sāsavā", "anāsavā", "āsavasampayuttā", "āsavavippayuttā", "āsavavippayuttasāsavā",
      "āsavavippayuttaanāsavā"), "मन के मैल", "मन के मैलों", "उनका"),
    (("saṃyojanā", "saṃyojaniyā", "asaṃyojaniyā", "saṃyojanasampayuttā", "saṃyojanavippayuttā",
      "saṃyojanavippayuttasaṃyojaniyā", "saṃyojanavippayuttaasaṃyojaniyā"), "बंधन", "बंधनों", "उनका"),
    (("ganthā", "ganthaniyā", "aganthaniyā", "ganthasampayuttā", "ganthavippayuttā", "ganthavippayuttaganthaniyā",
      "ganthavippayuttaaganthaniyā"), "गाँठ", "गाँठों", "उनका"),
    (("oghā", None, None, None, None, None, None), "बाढ़", "बाढ़ों", "उनका"),
    (("yogā", None, None, None, None, None, None), "जकड़न", "जकड़नों", "उनका"),
    (("nīvaraṇā", "nīvaraṇiyā", "anīvaraṇiyā", "nīvaraṇasampayuttā", "nīvaraṇavippayuttā",
      "nīvaraṇavippayuttanīvaraṇiyā", "nīvaraṇavippayuttaanīvaraṇiyā"), "बाधा", "बाधाओं", "उनका"),
    (("parāmāsā", "parāmaṭṭhā", "aparāmaṭṭhā", "parāmāsasampayuttā", "parāmāsavippayuttā",
      "parāmāsavippayuttaparāmaṭṭhā", "parāmāsavippayuttaaparāmaṭṭhā"), "ग़लत धारणा", "ग़लत धारणा", "उसका"),
    (("upādānā", "upādāniyā", "anupādāniyā", "upādānasampayuttā", "upādānavippayuttā",
      "upādānavippayuttaupādāniyā", "upādānavippayuttaanupādāniyā"), "आसक्ति", "आसक्ति", "उसका"),
    (("kilesā", "saṃkilesikā", "asaṃkilesikā", "kilesasampayuttā", "kilesavippayuttā",
      "kilesavippayuttasaṃkilesikā", "kilesavippayuttaasaṃkilesikā"), "मन के क्लेश", "क्लेशों", "क्लेशों का"),
]

TERMS, PAIRS = {}, {}
for k, v in TERMS_RAW.items():
    TERMS[norm(k)] = v
NEGS = {norm(k): norm(v) for k, v in NEG_RAW.items()}
for (G, niya, aniya, samp, vipp, vn, va), X1, X2, ref in GROUPS:
    TERMS[norm(G)] = X1 + " रूपी"
    TERMS[norm("no " + G)] = X1 + " रूपी न होने " + VAL
    if niya is None:
        continue
    TERMS[norm(niya)] = X2 + " का विषय बनने " + VAL
    TERMS[norm(aniya)] = X2 + " का विषय न बनने " + VAL
    TERMS[norm(samp)] = X2 + " से जुड़~"
    TERMS[norm(vipp)] = X2 + " से अलग"
    TERMS[norm(vn)] = X2 + " से अलग, पर " + ref + " विषय बनने " + VAL
    TERMS[norm(va)] = X2 + " से अलग और " + ref + " विषय न बनने " + VAL
    PAIRS[("both", norm(G), norm(niya))] = X1 + " रूपी भी और " + X2 + " का विषय बनने वाल~ भी"
    PAIRS[("butnot", norm(niya), norm(G))] = X2 + " का विषय बनने वाल~, पर स्वयं " + X1 + " रूपी न होने " + VAL
    PAIRS[("both", norm(G), norm(samp))] = X1 + " रूपी भी और " + X2 + " से जुड़~ भी"
    PAIRS[("butnot", norm(samp), norm(G))] = X2 + " से जुड़~, पर स्वयं " + X1 + " रूपी न होने " + VAL
TERMS[norm("saṃkiliṭṭhā")] = "क्लेशों से मलिन"
TERMS[norm("asaṃkiliṭṭhā")] = "क्लेशों से मलिन न होने " + VAL
PAIRS[("both", norm("kilesā"), norm("saṃkiliṭṭhā"))] = "मन के क्लेश रूपी भी और क्लेशों से मलिन भी"
PAIRS[("butnot", norm("saṃkiliṭṭhā"), norm("kilesā"))] = "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने " + VAL
PAIRS[("both", norm("hetū"), norm("sahetukā"))] = "मूल रूपी भी और मूल वाल~ भी"
PAIRS[("butnot", norm("sahetukā"), norm("hetū"))] = "मूल वाल~, पर स्वयं मूल रूपी न होने " + VAL
PAIRS[("both", norm("hetū"), norm("hetusampayuttā"))] = "मूल रूपी भी और मूलों से जुड़~ भी"
PAIRS[("butnot", norm("hetusampayuttā"), norm("hetū"))] = "मूलों से जुड़~, पर स्वयं मूल रूपी न होने " + VAL


class Subj:
    def __init__(self, hi, obl, g, pl, pron=False):
        self.hi, self.obl, self.g, self.pl, self.pron = hi, obl, g, pl, pron

    @property
    def ag(self):
        return "f" if self.g == "f" else ("m" if self.pl else "ms")

    def pronoun(self):
        return Subj("ये" if self.pl else "यह", None, self.g, self.pl, True)

    def obj(self):
        if self.pron:
            return "इन्हें" if self.pl else "इसे"
        return self.obl + " को"


NUMS = [("dasindriyā", "दस"), ("cha indriyā", "छह"), ("cattārindriyā", "चार"), ("tīṇindriyā", "तीन"),
        ("dvindriyā", "दो"), ("navindriyā", "नौ"), ("sattindriyā", "सात"), ("pañcindriyā", "पाँच"),
        ("dvādasindriyā", "बारह"), ("ekādasindriyā", "ग्यारह"), ("pannarasindriyā", "पंद्रह"),
        ("soḷasindriyā", "सोलह"), ("sattarasindriyā", "सत्रह"), ("aṭṭhārasindriyā", "अठारह"),
        ("cuddasindriyā", "चौदह"), ("terasindriyā", "तेरह"), ("aṭṭhindriyā", "आठ"), ("ekavīsatindriyā", "इक्कीस")]
SUBJECTS = {}
for key, h in NUMS:
    SUBJECTS[key] = Subj(f"{h} क्षमताएँ", f"{h} क्षमताओं", "f", True)
for p, h in {"domanassindriyaṃ": "उदासी की क्षमता",
             "anaññātaññassāmītindriyaṃ": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
             "jīvitindriyaṃ": "जीवन-क्षमता", "somanassindriyaṃ": "प्रसन्नता की क्षमता",
             "upekkhindriyaṃ": "समभाव की क्षमता", "aññindriyaṃ": "पूर्ण ज्ञान की क्षमता",
             "aññātāvindriyaṃ": "पूर्ण ज्ञान पा चुके की क्षमता", "manindriyaṃ": "मन की क्षमता"}.items():
    SUBJECTS[p] = Subj(h, h, "f", False)
SUBJECTS["pītisambojjhaṅgo"] = Subj(SB["piti"], obl_sb("piti"), "m", False)
SUBJECTS["dhammavicayasambojjhaṅgo"] = Subj(SB["dv"], obl_sb("dv"), "m", False)
SUBJECTS["cha bojjhaṅgā"] = Subj("जागृति के छह अंग", "जागृति के छह अंगों", "m", True)
SUBJECTS["sammāsaṅkappo"] = Subj("सही संकल्प", "सही संकल्प", "m", False)
SUBJECTS["sammādiṭṭhi"] = Subj("सही दृष्टि", "सही दृष्टि", "f", False)
SUBJECTS["satta maggaṅgā"] = Subj("मार्ग के सात अंग", "मार्ग के सात अंगों", "m", True)
_SUBJ_RE = re.compile(r"^(" + "|".join(sorted(map(re.escape, SUBJECTS), key=len, reverse=True)) + r")(?=\s|$)\s*(.*)$",
                      re.I | re.S)
TI = re.compile(r"(n?ti(?:\s?pi)?)$")


class PPError(Exception):
    pass


def _clean_item(t, strip_ti=False):
    q = '"' in t
    t = t.replace('"', "").strip()
    if strip_ti:
        t = TI.sub("", t).strip()
    t = re.sub(r"ñceva\b", "ṃ ceva", t)
    t = re.sub(r"ñc([aā])\b", r"ṃ c\1", t)
    return t, q


def _resolve_one(t):
    """one Pāli term (already without quotes / ti) -> (template, neg)"""
    m = re.match(r"^(.+?) ceva (?:no|na) ca (.+)$", t)
    if m:
        k = ("butnot", norm(m.group(1)), norm(m.group(2)))
        if k in PAIRS:
            return PAIRS[k], False
        raise PPError("pair? " + t)
    m = re.match(r"^(.+?) ceva (.+?)\s?c[aā]$", t)
    if m:
        k = ("both", norm(m.group(1)), norm(m.group(2)))
        if k in PAIRS:
            return PAIRS[k], False
        raise PPError("pair? " + t)
    n = norm(t)
    if n in TERMS:
        return TERMS[n], False
    if n in NEGS:
        return TERMS[NEGS[n]], True
    words = n.split()
    if words and words[0] in ("na", "no") and " ".join(words[1:]) in TERMS:
        return TERMS[" ".join(words[1:])], True
    # sequence of terms ("pītisahagataṃ na sukhasahagataṃ na upekkhāsahagataṃ", "anāsavā āsavavippayuttā")
    out, i = [], 0
    while i < len(words):
        for j in range(len(words), i, -1):
            k = " ".join(words[i:j])
            if k in TERMS:
                out.append(TERMS[k])
                i = j
                break
        else:
            raise PPError("term? " + t)
    if len(out) > 1:
        return ", ".join(out[:-1]) + " और " + out[-1], False
    return out[0], False


def phrase(t, g):
    tmpl, neg = _resolve_one(t)
    if isinstance(tmpl, dict):
        return tmpl[g], neg
    return agree(tmpl, g), neg


def _hoti(s, neg=False):
    if s.g == "f":
        base = "होती"
    else:
        base = "होते" if s.pl else "होता"
    if neg:
        return "नहीं " + (base + "ं" if (s.g == "f" and s.pl) else base)
    return base + (" हैं" if s.pl else " है")


def _cop(s):
    return "हैं" if s.pl else "है"


def _split_clauses(sent):
    """-> [(sep_before, text)]; separators ', ' '; ' and '…pe…'"""
    toks = re.split(r"(,\s+|;\s+|…pe…\s?)", sent)
    out, sep = [], ""
    for i, t in enumerate(toks):
        if i % 2 == 1:
            sep = t
            continue
        if t.strip() == "" and i % 2 == 0:
            if out:  # "…pe…" directly followed by end
                out[-1] = (out[-1][0], out[-1][1], out[-1][2] + sep)
            continue
        t = t.strip()
        # "siyā X siyā Y" without a comma: split before the inner "siyā" (Hindi gets a comma)
        m = _SUBJ_RE.match(t)
        head, rest = (m.group(1) + " ", m.group(2)) if m else ("", t)
        bits = re.split(r"\s+(?=[Ss]iyā\s)", rest)
        bits = [b for b in bits if b]
        if not bits:
            bits = [""]
        out.append((sep, head + bits[0], ""))
        for b in bits[1:]:
            out.append((", ", b, ""))
        sep = ""
    return out


def _hsep(sep):
    if sep.startswith(","):
        return ", "
    if sep.startswith(";"):
        return "; "
    if sep.startswith("…pe…"):
        return "… " if sep.endswith(" ") else "…"
    return ""


def render_line(pali, default, debug=False):
    """Hindi for one Pañhāpucchaka line (block ID already removed)."""
    pali = pali.strip()
    pali = re.sub(r"\b([Aa])raṇāti\.$", r"\1raṇā.", pali)  # closing "…araṇāti."
    sents = re.findall(r".+?[.?](?=\s|$)", pali)
    assert "".join(sents).replace(" ", "") == pali.replace(" ", ""), "sentence split: " + pali
    out_sents = []
    last_subj = default
    prev_sent_nv = False
    for sent in sents:
        end = sent[-1]
        body = sent[:-1]
        clauses = _split_clauses(body)
        hi = []
        cur = None
        prev_kind = None
        nv_open = None  # index in hi of the open nv clause
        for ci, (sep, text, tail) in enumerate(clauses):
            m = _SUBJ_RE.match(text)
            explicit = None
            if m:
                explicit = SUBJECTS[m.group(1).lower()]
                text = m.group(2)
            low = text.lower()
            # kind
            if low.startswith("siyā na vattabb"):
                kind, rest = "snv", re.sub(r"^siyā na vattabb\S*\s*", "", text, flags=re.I)
            elif low.startswith("na vattabb"):
                kind, rest = "nv", re.sub(r"^na vattabb\S*\s*", "", text, flags=re.I)
            else:
                t0, _ = _clean_item(text)
                if not low.startswith("siyā") and TI.search(t0) and not explicit:
                    kind, rest = "item", text
                elif low.startswith("siyā "):
                    kind, rest = "siya", text[5:]
                else:
                    kind, rest = "aff", text
            # subject for this clause
            emit = None
            if explicit:
                cur = explicit
                last_subj = explicit
                emit = "full"
            elif ci == 0:
                # "… na vattabbā – "hetū ceva sahetukā cā"ti. Sahetukā ceva na ca hetū." continues the subject
                if (prev_sent_nv and " ceva " in text) or kind == "item":
                    cur = last_subj.pronoun()
                    emit = "pron"
                else:
                    cur = default
                    last_subj = default
                    emit = "full"
            else:
                if sep.startswith(";") and low.startswith("kenaci"):
                    cur = default
                    emit = "full"
                elif sep.startswith(";") or (prev_kind in ("nv", "snv", "item") and kind in ("aff", "siya")):
                    emit = "pron"
                elif kind in ("nv", "snv"):
                    emit = "pron"
            if kind == "item" and prev_kind in ("nv", "snv", "item") and ci > 0:
                it, q = _clean_item(rest, True)
                p, _ = phrase(it, cur.ag)
                hi[nv_open][1].append((p, q))
                hi.append(("sepitem", _hsep(sep)))
                prev_kind = "item"
                continue
            if kind in ("nv", "snv", "item"):
                dash = rest.lstrip().startswith(DASH)
                rest = rest.lstrip().lstrip(DASH).strip()
                it, q = _clean_item(rest, True)
                p, _ = phrase(it, cur.ag)
                obj = (cur if emit == "full" else (cur.pronoun() if not cur.pron else cur)).obj()
                hi.append(("nv", [(p, q)], dash, obj, kind == "snv", _hsep(sep)))
                nv_open = len(hi) - 1
                prev_kind = kind if kind != "item" else "nv"
                continue
            # aff / siya
            it, q = _clean_item(rest)
            p, neg = phrase(it, cur.ag)
            if q:
                p = f"“{p}”"
            if kind == "siya":
                pred = f"कभी {p} {_hoti(cur, neg)}"
            else:
                pred = f"{p} {_hoti(cur, True) if neg else _cop(cur)}"
            if emit == "full":
                subj = cur.hi
            elif emit == "pron":
                subj = cur.pronoun().hi if not cur.pron else cur.hi
            else:
                subj = None
            hi.append(("txt", _hsep(sep) + (subj + " " if subj else "") + pred + (_hsep(tail) if tail else "")))
            prev_kind = kind
        # render
        s = ""
        for h in hi:
            if h[0] == "txt":
                s += h[1]
            elif h[0] == "sepitem":
                continue
            else:
                _, items, dash, obj, siya, sp = h
                pre = sp + ("कभी " if siya else "")
                if dash:
                    if len(items) == 1:
                        lst = (f"“{items[0][0]}”" if items[0][1] else items[0][0])
                    else:
                        lst = ", ".join("न " + (f"“{p}”" if q else p) for p, q in items)
                    s += f"{pre}{obj} नहीं कहा जा सकता {DASH} {lst}"
                else:
                    ps = [(f"“{p}”" if q else p) for p, q in items]
                    if len(ps) == 1:
                        s += f"{pre}{obj} {ps[0]} नहीं कहा जा सकता"
                    else:
                        s += f"{pre}{obj} न {ps[0]} कहा जा सकता है, " + ", ".join("न " + x for x in ps[1:])
        s += "।" if end == "." else end
        prev_sent_nv = prev_kind in ("nv", "snv", "item")
        out_sents.append(s)
        if debug:
            print("P:", sent)
            print("H:", s)
    return " ".join(out_sents)


# =====================================================================================  build helpers
def pali_lines(chapter):
    return open(os.path.join(PALI_DIR, chapter), encoding="utf-8-sig").read().splitlines()


def strip_id(line):
    return ID.sub("", line).rstrip()


def write_chapter(chapter, hindi_lines):
    pl = pali_lines(chapter)
    n = sum(1 for l in pl if l.strip())
    assert n == len(hindi_lines), f"{chapter}: {n} Pāli lines vs {len(hindi_lines)} Hindi lines"
    text = S.assemble(pl, hindi_lines)
    assert "—" not in text and ":-" not in text
    with open(os.path.join(HI_DIR, chapter), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("written", chapter, n, "lines")


TIKA_HEAD = "##### तीन-तीन के वर्गीकरण"     # ##### Tikaṃ (pi-1 तीन-तीन के वर्गीकरणों की मूल सूची)
DUKA_HEAD = "##### दो-दो के वर्गीकरण"       # ##### Dukaṃ
ALL_FACULTIES = Subj("सभी क्षमताएँ", "सभी क्षमताओं", "f", True)   # subjectless sentence in ch. 5
THESE_M = Subj("ये", None, "m", True, pron=True)                 # subjectless sentence in ch. 7, 10, 11


def question_kati(whole_obl, masc):
    """<X>naṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?"""
    k = "कितने" if masc else "कितनी"
    v = "वाले" if masc else "वाली"
    return (f"{whole_obl} में से {k} हितकर हैं, {k} हानिकर हैं, {k} नैतिक रूप से अनिर्धारित हैं… "
            f"{k} संघर्ष {v} हैं, {k} संघर्ष से रहित हैं?")


def build(chapter, manual, pp_lines, default, show=False):
    """manual: {Pāli line number (1-based): Hindi}; pp_lines: Pāli line numbers rendered by the engine."""
    pl = pali_lines(chapter)
    out = []
    for i, l in enumerate(pl, 1):
        if not l.strip():
            continue
        if i in pp_lines:
            h = render_line(strip_id(l), default)
        else:
            assert i in manual, f"{chapter}: no Hindi for line {i}: {l[:60]}"
            h = manual[i]
        if show:
            print(f"[{i}] {h}")
        out.append(h)
    extra = set(manual) - {i for i, l in enumerate(pl, 1) if l.strip()}
    assert not extra, f"manual lines not in source: {sorted(extra)}"
    write_chapter(chapter, out)


PI1_REUSED = [MAGGANGA, SATI_SHORT.split(", सही")[0], SAMADHI_FULL, DOMANASSA_DEF, FOUR_TRUTHS, SAMMAVAYAMA,
              VACA_DEF, KAMMANTA_DEF, AJIVA_DEF, SANKAPPA_FULL, PITI_FULL, PASSADDHI_REST, LOKUTTARA,
              PHASSA_PE, VIPAKA, "परिघटनाओं की छानबीन नामक जागृति का अंग", "एकाग्रता नामक जागृति का अंग",
              "उत्साह नामक जागृति का अंग",
              "प्रज्ञा, जानना", "मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि", "मानसिक रूप से उत्साह जगाना",
              "मन का प्रबल राग", "राग, प्रबल राग", "पूर्ण ज्ञान पा चुके की क्षमता", "पूर्ण ज्ञान की क्षमता",
              "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता", "उदासी की क्षमता", "प्रसन्नता की क्षमता",
              "समभाव की क्षमता", "सुख की क्षमता", "दुःख की क्षमता", "जीवन-क्षमता", "आठ अंगों वाला",
              "पाँच अंगों वाला", "स्त्री की आकृति, स्त्री का चिह्न, स्त्री का आचरण, स्त्री का ढंग, स्त्री होना, स्त्री होने का भाव",
              "पुरुष की आकृति, पुरुष का चिह्न, पुरुष का आचरण, पुरुष का ढंग, पुरुष होना, पुरुष होने का भाव",
              "आयु, टिके रहना, चलते रहना, चलाए रखना, गतिशील रहना, बने रहना, पालन, जीवन, जीवन-क्षमता",
              "चार महाभूतों से व्युत्पन्न", "यह सूना गाँव भी है", "सुहावना सुखद अनुभव", "असुहावना दुःखद अनुभव",
              "श्रद्धा, श्रद्धा रखना, भरोसा करना, गहरी आस्था, श्रद्धा, श्रद्धा की क्षमता, श्रद्धा का बल",
              "सजगता, बार-बार स्मरण, पुनः स्मरण, सजगता, याद रखना, धारण करना, उथला न होना, भूल न जाना, सजगता, सजगता की क्षमता, सजगता का बल, सही सजगता",
              "आगे बढ़ना, प्रयत्न, उद्यम, प्रयास, जोश, लगन, शक्ति",
              "ढीला न पड़ने वाला प्रयत्न, चाह न छोड़ना, भार न छोड़ना, भार को दृढ़ता से उठाए रखना, उत्साह, उत्साह की क्षमता, उत्साह का बल",
              "जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है", "ये हितकर परिघटनाएँ हैं।",
              "आरंभिक विचार और सतत विचार वाले, अलगाव से उत्पन्न उल्लास और सुख वाले पहले ध्यान",
              "आरंभिक विचार और सतत विचार के शांत होने से, स्वयं में निर्मलता वाले, मन के एक बिंदु पर टिकने वाले, आरंभिक विचार और सतत विचार से रहित, एकाग्रता से उत्पन्न उल्लास और सुख वाले दूसरे ध्यान",
              "उल्लास के फीका पड़ने से वह समभाव के साथ, सजग और स्पष्ट समझ रखते हुए रहता है और काया से सुख का अनुभव करता है, जिसके बारे में आर्य कहते हैं",
              "“समभाव वाला, सजगता वाला, सुख से रहने वाला”",
              "सुख को छोड़ने से और दुःख को छोड़ने से, और पहले ही प्रसन्नता और उदासी के मिट जाने से, न दुःखद, न सुखद, समभाव और सजगता से पूरी तरह शुद्ध चौथे ध्यान"]


def check_pi1():
    corpus = "\n".join(S._read(os.path.join(S.PI1_HI_DIR, f)) for f in os.listdir(S.PI1_HI_DIR) if f.endswith(".md"))
    corpus = re.sub(r"\s*\[[^\]]*\]", "", corpus)
    missing = [s for s in PI1_REUSED if s.rstrip("।") not in corpus]
    assert not missing, "not found in pi-1 Hindi: " + " | ".join(missing)
    # matrix labels used in TERMS must exist in the pi-1 matrix (feminine forms)
    mat = S._read(os.path.join(S.PI1_HI_DIR, "1-matika.md"))
    mat = re.sub(r"\s*\[[^\]]*\]", "", mat)
    bad = []
    for k, v in list(TERMS.items()) + list(PAIRS.items()):
        f = v["f"] if isinstance(v, dict) else agree(v, "f")
        if f + " परिघटनाएँ" not in mat and f not in mat:
            bad.append(f)
    return bad
