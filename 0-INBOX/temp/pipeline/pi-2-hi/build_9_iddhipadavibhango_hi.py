# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga ch. 9 (Iddhipādavibhaṅga), Hindi plain zero-shot.

usage: python -I -X utf8 build_9_iddhipadavibhango_hi.py
Writes AI_translation\\hindi\\pi-2-hindi-plain-zeroshot_split_chapters\\9-iddhipadavibhango.md
Block IDs are copied from the Pāli at build time (S.assemble).
"""
import os, sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import build_ch1_sample_hi as S  # noqa: E402

D = S.DASH
FILE = "9-iddhipadavibhango.md"

# ---------------------------------------------------------------- terms
IP = "सिद्धि का आधार"            # iddhipāda (pi-1)
IP_OBL = "सिद्धि के आधार"
IP4 = "सिद्धि के चार आधार"       # cattāro iddhipādā (pi-5)
IP3 = "सिद्धि के तीन आधार"       # tayo iddhipādā
FACTOR = {"chanda": "चाह", "viriya": "उत्साह", "citta": "मन", "vimamsa": "जाँच-परख"}   # pi-1 adhipati words
SAMADHI = {k: f"{v} से प्राप्त एकाग्रता" for k, v in FACTOR.items()}               # chandasamādhi ...
NAMED = {k: f"{v} रूपी {IP}" for k, v in FACTOR.items()}                             # chandiddhipādo ...
NAMED_OBL = {k: f"{v} रूपी {IP_OBL}" for k, v in FACTOR.items()}
PS = "प्रयत्न की रचना"            # padhānasaṅkhāro
PS_PL = "प्रयत्न की रचनाएँ"       # padhānasaṅkhārā
PS_OBL_PL = "प्रयत्न की रचनाओं"


def full(k):
    """chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ (oblique, before 'का अभ्यास करता है')"""
    return f"{SAMADHI[k]} और {PS_OBL_PL} से संपन्न {IP_OBL}"


def samannagato(k):
    """chandasamādhipadhānasaṅkhārasamannāgato"""
    return f"{SAMADHI[k]} और {PS_OBL_PL} से संपन्न"


def bhaveti(k):
    return f"{full(k)} का अभ्यास करता है"


INTRO = (f"{IP4} {D} यहाँ भिक्षु {bhaveti('chanda')}, {bhaveti('viriya')}, {bhaveti('citta')}, "
         f"{bhaveti('vimamsa')}।")                                                                  # ^2-431/444


def kathanca(k):
    return f"और भिक्षु {full(k)} का अभ्यास कैसे करता है?"


# pi-1 ^1-1377 (sammappadhāna formula), "So" = वह
SP_1 = "उत्पन्न न हुई बुरी हानिकर परिघटनाओं को उत्पन्न न होने देने के लिए"
SP_2 = "उत्पन्न हो चुकी बुरी हानिकर परिघटनाओं को छोड़ने के लिए"
SP_3 = "उत्पन्न न हुई हितकर परिघटनाओं की उत्पत्ति के लिए"
SP_4 = ("उत्पन्न हो चुकी हितकर परिघटनाओं की स्थिरता के लिए, उनके लुप्त न होने के लिए, उन्हें और बढ़ाने के लिए, "
        "उनकी विपुलता के लिए, उनके अभ्यास के लिए, उनकी परिपूर्णता के लिए")
SP_V = "चाह जगाता है, प्रयास करता है, उत्साह जगाता है, मन को तत्पर करता है, पूरा ज़ोर लगाता है"
SP_FULL = f"वह {SP_1} {SP_V}, {SP_2} {SP_V}, {SP_3} {SP_V}, {SP_4} {SP_V}।"
SP_SHORT = f"वह {SP_1} {SP_V}, {SP_2}… {SP_3}… {SP_4} {SP_V}।"
PS_CALLED = f"ये “{PS_PL}” कही जाती हैं।"                                   # Ime vuccanti "padhānasaṅkhārā".
GATHER = "उन्हें एक साथ इकट्ठा करके, संक्षेप में समेटकर"                    # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā


def iti(k):
    return f"इस प्रकार यह {SAMADHI[k]} है और ये {PS_PL} हैं"


def reckoned(k, variant=""):
    return f"यह “{SAMADHI[k]} और {PS}” की ही गिनती{variant} में आता है"


def obtains(k, variant=""):
    """Chandaṃ ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ, labhati cittassekaggataṃ – ayaṃ vuccati "chandasamādhi"."""
    return (f"यदि भिक्षु {FACTOR[k]} को प्रधान बनाकर एकाग्रता प्राप्त करता है, मन की एकाग्रता{variant} प्राप्त करता है "
            f"{D} यह “{SAMADHI[k]}” कही जाती है।")


def sutta_first_line(k):
    if k == "chanda":
        return (f"{kathanca(k)} {obtains(k, ' [वर्तनी-भेद (Sī., Syā.): cittassa ekaggataṃ]')} {SP_FULL} {PS_CALLED} "
                f"{iti(k)}। {GATHER} {reckoned(k, ' [वर्तनी-भेद (Sī.): saṅkhaṃ]')}।")
    return f"{kathanca(k)} {obtains(k)} {SP_SHORT} {PS_CALLED} {iti(k)}; {GATHER} {reckoned(k)}।"


# definitions (pi-1 synonym strings)
CHANDA_DEF = "जो चाह, चाहत रखना, करने की इच्छा, हितकर परिघटना रूपी चाह है"   # chando chandikatā kattukamyatā kusalo dhammacchando
SAMADHI_LIST = ("मन की स्थिरता, ठहराव, दृढ़ता, बिखराव का अभाव, भटकाव का अभाव, मन का न बिखरा होना, शांति, "
                "एकाग्रता की क्षमता, एकाग्रता का बल, सही एकाग्रता")             # pi-1 ^1-287
VIRIYA_LIST_T = ("मानसिक रूप से उत्साह जगाना, आगे बढ़ना, प्रयत्न, उद्यम, प्रयास, जोश, लगन, शक्ति, स्थिरता, "
                 "ढीला न पड़ने वाला प्रयत्न, चाह न छोड़ना, भार न छोड़ना, भार को दृढ़ता से उठाए रखना, उत्साह, "
                 "उत्साह की क्षमता, उत्साह का बल, सही प्रयास")                 # pi-1 ^1-22, with ṭhiti (pi-1: dhiti = धैर्य)
VIRIYA_SHORT = "मानसिक रूप से उत्साह जगाना… सही प्रयास"
CITTA_SHORT = "मन, मानस, मानसिक क्रिया… उसके अनुरूप मन की चेतना का तत्व"          # pi-1 ^1-6
PANNA_SHORT = "प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि"       # pi-1 ^1-1344
SAMADHI_TAIL = "एकाग्रता नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ"      # pi-1 ^1-287
VIRIYA_TAIL = "उत्साह नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ"
PANNA_TAIL = "परिघटनाओं की छानबीन नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ"  # pi-1 ^1-292


def q(word):
    return f"यहाँ {word} क्या है?"


def called_f(word):
    return f"यह “{word}” कही जाती है।"


def called_m(word):
    return f"यह “{word}” कहा जाता है।"


CHANDA_LINE = f"{q('चाह')} {CHANDA_DEF} {D} {called_f('चाह')}"
SAMADHI_FULL_LINE = f"{q('एकाग्रता')} जो {SAMADHI_LIST} है {D} {called_f('एकाग्रता')}"
SAMADHI_SHORT_LINE = f"{q('एकाग्रता')} जो मन की स्थिरता, ठहराव… सही एकाग्रता है {D} {called_f('एकाग्रता')}"
SAMADHI_LOK_LINE = f"{q('एकाग्रता')} जो मन की स्थिरता, ठहराव… सही एकाग्रता, {SAMADHI_TAIL} है {D} {called_f('एकाग्रता')}"
VIRIYA_LINE = f"{q('उत्साह')} जो {VIRIYA_SHORT} है {D} {called_m('उत्साह')}"
VIRIYA_LOK_LINE = f"{q('उत्साह')} जो {VIRIYA_SHORT}, {VIRIYA_TAIL} है {D} {called_m('उत्साह')}"
CITTA_LINE = f"{q('मन')} जो {CITTA_SHORT} है {D} {called_m('मन')}"
VIMAMSA_LINE = f"{q('जाँच-परख')} जो {PANNA_SHORT} है {D} {called_f('जाँच-परख')}"
VIMAMSA_LOK_LINE = f"{q('जाँच-परख')} जो {PANNA_SHORT}, {PANNA_TAIL} है {D} {called_f('जाँच-परख')}"

ENDOWED_FULL = ("युक्त होता है, भली-भाँति युक्त होता है, उन तक पहुँचा हुआ, भली-भाँति पहुँचा हुआ, उनसे सुसज्जित, "
                "उनसे परिपूर्ण, उनसे संपन्न होता है")                        # upeto hoti samupeto ... samannāgato
ENDOWED_SHORT = "युक्त होता है… उनसे संपन्न होता है"


def endowed(k, short=True):
    obj = {"chanda": "इस चाह से", "viriya": "इस उत्साह से", "citta": "इस मन से", "vimamsa": "इस जाँच-परख से"}[k]
    return f"इस प्रकार वह {obj}, इस एकाग्रता से और इस {PS} से {ENDOWED_SHORT if short else ENDOWED_FULL}।"


def tena(k, end="।"):
    return f"इसीलिए कहा जाता है “{samannagato(k)}”{end}"


def ps_line(k, lok=False, short=True, tena_end="।"):
    body = VIRIYA_SHORT + (f", {VIRIYA_TAIL}" if lok else "") if short else VIRIYA_LIST_T
    return f"{q(PS)} जो {body} है {D} {called_f(PS)} {endowed(k, short)} {tena(k, tena_end)}"


IDDHI_LINE = ("“सिद्धि” का अर्थ है उन परिघटनाओं की सिद्धि, समृद्धि, सफल होना, भली-भाँति सफल होना, लाभ, उपलब्धि, "
              "प्राप्ति, भली-भाँति प्राप्ति, स्पर्श करना, साक्षात्कार और पूरी तरह प्राप्त करना।")
TATHA = "ऐसी स्थिति वाले व्यक्ति का"                                               # tathābhūtassa
KH4 = "अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह"
IP_KH_FULL = f"“{IP}” का अर्थ है {TATHA} {KH4}।"
IP_KH_SHORT = f"“{IP}” का अर्थ है {TATHA} अनुभूति का समूह… चेतना का समूह।"
IP_PHASSA = f"“{IP}” का अर्थ है {TATHA} संपर्क… तत्परता, भटकाव का अभाव।"              # phasso…pe… paggāho avikkhepo
BHAVETI = f"{IP_OBL} का अभ्यास करता है"
BHAVETI_LINE = (f"“{BHAVETI}” का अर्थ है वह उन परिघटनाओं का निरंतर सेवन करता है, अभ्यास करता है, उन्हें बार-बार करता है। "
                f"इसीलिए कहा जाता है “{BHAVETI}”।")                         # Te dhamme āsevati bhāveti bahulīkaroti.

# Abhidhammabhājanīya: pi-1 ^1-277 (lokuttara first jhāna), "Idha bhikkhu yasmiṃ samaye"
LOK = ("यहाँ जिस समय भिक्षु लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला होता है, "
       "दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए, इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके "
       "उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है")


def abhi_first_line(k):
    return f"{kathanca(k)} {LOK}, उस समय वह {bhaveti(k)}।"


def vibhanga_line(k):
    """Tattha katamo chandiddhipādo? Idha bhikkhu yasmiṃ samaye ..., yo tasmiṃ samaye chando ... – ayaṃ vuccati "chandiddhipādo"."""
    what = {
        "chanda": "चाह, चाहत रखना, करने की इच्छा, हितकर परिघटना रूपी चाह",
        "viriya": f"{VIRIYA_SHORT}, {VIRIYA_TAIL}",
        "citta": CITTA_SHORT,
        "vimamsa": f"{PANNA_SHORT}, {PANNA_TAIL}",
    }[k]
    return (f"यहाँ {NAMED[k]} क्या है? {LOK}, उस समय जो {what} है {D} {called_m(NAMED[k])} "
            f"शेष परिघटनाएँ {NAMED_OBL[k]} से जुड़ी हैं।")


# ---------------------------------------------------------------- Pañhāpucchaka (masc. pl., subject: सिद्धि के आधार)
def siya(*items):
    return "कभी " + ", कभी ".join(items) + " होते हैं।"


TIKA = " ".join([
    "ये केवल हितकर हैं।",
    siya("सुखद अनुभूति से जुड़े", "न दुःखद, न सुखद अनुभूति से जुड़े"),
    "कर्म-फल उत्पन्न करने वाले हैं।",
    "न कर्म से उत्पन्न हैं, न आसक्ति का विषय बनने वाले।",
    "क्लेशों से मलिन न होने वाले और क्लेशों का विषय न बनने वाले हैं।",
    siya("आरंभिक विचार और सतत विचार वाले", "आरंभिक विचार से रहित, केवल सतत विचार वाले",
         "आरंभिक विचार और सतत विचार दोनों से रहित"),
    siya("उल्लास के साथ होने वाले", "सुख के साथ होने वाले", "समभाव के साथ होने वाले"),
    "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले हैं।",
    "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाले हैं।",
    "संचय घटाने की ओर ले जाने वाले हैं।",
    "सीखने के चरण के हैं।",
    "अपरिमित हैं।",
    "अपरिमित विषय वाले हैं।",
    "उत्तम हैं।",
    "सही दिशा में निश्चित हैं।",
    "मार्ग को विषय बनाने वाले नहीं हैं, मार्ग को मूल बनाने वाले हैं, मार्ग की प्रधानता वाले नहीं हैं।",
    "कभी उत्पन्न हो चुके, कभी उत्पन्न न हुए होते हैं, इन्हें उत्पन्न होने वाले नहीं कहा जा सकता।",
    siya("अतीत के", "भविष्य के", "वर्तमान के"),
    "इन्हें न अतीत के विषय वाले कहा जा सकता है, न भविष्य के विषय वाले, न वर्तमान के विषय वाले।",
    siya("स्वयं से संबंधित", "दूसरों से संबंधित", "स्वयं और दूसरों दोनों से संबंधित"),
    "दूसरों से संबंधित विषय वाले हैं।",
    "दिखाई न देने वाले और टकराव से रहित हैं।",
])

V = NAMED["vimamsa"]
V_OBL = NAMED_OBL["vimamsa"]
C = NAMED["citta"]
C_OBL = NAMED_OBL["citta"]


def three_vs_citta(pos3, neg_c):
    return f"{IP3} {pos3} हैं, {C} {neg_c} है।"


def three_vs_citta_nv(pos3, a, b):
    return f"{IP3} {pos3} हैं, {C_OBL} को न {a} कहा जा सकता है, न {b}।"


DUKA_1 = " ".join([
    f"{V} मूल रूपी है, {IP3} मूल रूपी नहीं हैं।",
    "मूल वाले हैं।",
    "मूलों से जुड़े हैं।",
    f"{V} मूल रूपी भी है और मूल वाला भी, {IP3}ों को मूल रूपी भी और मूल वाले भी नहीं कहा जा सकता, वे मूल वाले हैं, पर स्वयं मूल रूपी नहीं हैं।",
    f"{V} मूल रूपी भी है और मूलों से जुड़ा भी, {IP3}ों को मूल रूपी भी और मूलों से जुड़े भी नहीं कहा जा सकता, वे मूलों से जुड़े हैं, पर स्वयं मूल रूपी नहीं हैं।",
    f"{IP3} मूल रूपी न होकर मूल वाले हैं, {V_OBL} को न मूल रूपी न होने वाला, पर मूल वाला कहा जा सकता है, न मूल रूपी न होने वाला और मूल से रहित।",
    "कारणों पर निर्भर रहने वाले हैं।",
    "निर्मित हैं।",
    "दिखाई न देने वाले हैं।",
    "टकराव से रहित हैं।",
    "अभौतिक हैं।",
    "लोकोत्तर हैं।",
    "किसी एक प्रकार की चेतना से जाने जा सकने वाले हैं, किसी एक प्रकार की चेतना से न जाने जा सकने वाले हैं।",
    "मन के मैल रूपी नहीं हैं।",
    "मन के मैलों का विषय न बनने वाले हैं।",
    "मन के मैलों से अलग हैं।",
    "इन्हें न मन के मैल रूपी भी और मन के मैलों का विषय बनने वाले भी कहा जा सकता है, न मन के मैलों का विषय बनने वाले, पर स्वयं मन के मैल रूपी न होने वाले।",
    "इन्हें न मन के मैल रूपी भी और मन के मैलों से जुड़े भी कहा जा सकता है, न मन के मैलों से जुड़े, पर स्वयं मन के मैल रूपी न होने वाले।",
    "मन के मैलों से अलग हैं।",
    "मन के मैलों का विषय न बनने वाले हैं।",
])
DUKA_2 = " ".join([
    "बंधन रूपी नहीं हैं… गाँठ रूपी नहीं हैं… बाढ़ रूपी नहीं हैं… जकड़न रूपी नहीं हैं… बाधा रूपी नहीं हैं… ग़लत धारणा रूपी नहीं हैं… विषय वाले हैं।",
    f"{IP3} मन रूपी नहीं हैं, {C} मन है।",
    three_vs_citta("मन के सहचर", "मन का सहचर नहीं"),
    three_vs_citta_nv("मन से जुड़े", "मन से जुड़ा", "मन से अलग"),
    three_vs_citta_nv("मन से घुले-मिले", "मन से घुला-मिला", "मन से घुला-मिला न होने वाला"),
    three_vs_citta("मन से उत्पन्न", "मन से उत्पन्न नहीं"),
    three_vs_citta("मन के साथ-साथ होने वाले", "मन के साथ-साथ होने वाला नहीं"),
    three_vs_citta("मन का अनुसरण करने वाले", "मन का अनुसरण करने वाला नहीं"),
    three_vs_citta("मन से घुले-मिले और मन से उत्पन्न", "मन से घुला-मिला और मन से उत्पन्न नहीं"),
    three_vs_citta("मन से घुले-मिले, मन से उत्पन्न और मन के साथ-साथ होने वाले",
                   "मन से घुला-मिला, मन से उत्पन्न और मन के साथ-साथ होने वाला नहीं"),
    three_vs_citta("मन से घुले-मिले, मन से उत्पन्न और मन का अनुसरण करने वाले",
                   "मन से घुला-मिला, मन से उत्पन्न और मन का अनुसरण करने वाला नहीं"),
])
DUKA_3 = " ".join([
    f"{IP3} बाह्य हैं, {C} आंतरिक है।",
    "व्युत्पन्न नहीं हैं।",
    "कर्म से उत्पन्न नहीं हैं।",
    "आसक्ति रूपी नहीं हैं… मन के क्लेश रूपी नहीं हैं… सत्य-दर्शन से छोड़े जाने वाले नहीं हैं।",
    "मानसिक अभ्यास से छोड़े जाने वाले नहीं हैं।",
    "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित हैं।",
    "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित हैं।",
    siya("आरंभिक विचार वाले", "आरंभिक विचार से रहित"),
    siya("सतत विचार वाले", "सतत विचार से रहित"),
    siya("उल्लास वाले", "उल्लास से रहित"),
    siya("उल्लास के साथ होने वाले", "उल्लास के साथ न होने वाले"),
    siya("सुख के साथ होने वाले", "सुख के साथ न होने वाले"),
    siya("समभाव के साथ होने वाले", "समभाव के साथ न होने वाले"),
    "इंद्रिय-सुखों के लोक से संबंधित नहीं हैं।",
    "सूक्ष्म भौतिक लोक से संबंधित नहीं हैं।",
    "अभौतिक लोक से संबंधित नहीं हैं।",
    "अस्तित्व के लोकों में न समाए हुए हैं।",
    "मुक्ति की ओर ले जाने वाले हैं।",
    "निश्चित हैं।",
    "सर्वोच्च हैं।",
    "संघर्ष से रहित हैं।",
])

SEC = S.SECTION_TITLES
KEYS = ("chanda", "viriya", "citta", "vimamsa")
DEF_SUTTA = {"chanda": CHANDA_LINE, "viriya": VIRIYA_LINE, "citta": CITTA_LINE, "vimamsa": VIMAMSA_LINE}
DEF_ABHI = {"chanda": CHANDA_LINE, "viriya": VIRIYA_LOK_LINE, "citta": CITTA_LINE, "vimamsa": VIMAMSA_LOK_LINE}
HEAD = {k: "##### " + NAMED[k] for k in KEYS}


def lines():
    L = ["### " + S.CHAPTER_TITLES[9], "#### " + SEC["Suttantabhājanīyaṃ"], INTRO]
    for k in KEYS:
        first = k == "chanda"
        L += [HEAD[k], sutta_first_line(k), DEF_SUTTA[k],
              SAMADHI_FULL_LINE if k in ("chanda", "viriya") else SAMADHI_SHORT_LINE,
              ps_line(k, short=not first),
              IDDHI_LINE,
              IP_KH_FULL if k in ("chanda", "vimamsa") else IP_KH_SHORT,
              BHAVETI_LINE]
    L.append(SEC["Suttantabhājanīyaṃ"] + "।")
    L += ["#### " + SEC["Abhidhammabhājanīyaṃ"], INTRO]
    for k in KEYS:
        last = k == "vimamsa"
        ps = (f"{q(PS)} जो {VIRIYA_SHORT}, {VIRIYA_TAIL} है {D} {called_f(PS)} "
              f"{endowed(k, short=not last)} {tena(k, '' if last else '।')}")
        L += [HEAD[k], abhi_first_line(k), DEF_ABHI[k], SAMADHI_LOK_LINE, ps, IDDHI_LINE, IP_PHASSA, BHAVETI_LINE]
    L.append(f"{IP4} {D} {NAMED['chanda']}, {NAMED['viriya']}, {NAMED['citta']}, {NAMED['vimamsa']}।")
    L += [vibhanga_line(k) for k in KEYS]
    L.append(SEC["Abhidhammabhājanīyaṃ"] + "।")
    L += ["#### " + SEC["Pañhāpucchakaṃ"],
          (f"{IP4} {D} यहाँ भिक्षु {bhaveti('chanda')}, {SAMADHI['viriya']}… {SAMADHI['citta']}… "
           f"{bhaveti('vimamsa')}।"),
          (f"{IP4}ों में से कितने हितकर हैं, कितने हानिकर, कितने नैतिक रूप से अनिर्धारित… "
           f"कितने संघर्ष वाले हैं, कितने संघर्ष से रहित?"),
          "##### तीन-तीन के वर्गीकरण", TIKA,
          "##### दो-दो के वर्गीकरण", DUKA_1, DUKA_2, DUKA_3,
          SEC["Pañhāpucchakaṃ"] + "।",
          S.CHAPTER_TITLES[9] + " पूरा हुआ।"]
    return L


def main():
    pali = S._read(os.path.join(S.PALI_DIR, FILE)).splitlines()
    out = S.assemble(pali, lines())
    with open(os.path.join(S.HI_DIR, FILE), "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print("written", FILE)


if __name__ == "__main__":
    main()
