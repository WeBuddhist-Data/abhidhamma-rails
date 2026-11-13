"""Hindi formula builder for the pi-7 (Paṭṭhāna) plain zero-shot SAMPLE.

Importable: every formula below is a constant or a small pure function, so later agents can
`import build_sample_hi as F` and reuse F.NAME("hetu"), F.ABL("hetu"), F.PATICCA(...), F.count_hi(...)
etc. verbatim. Importing does NOT write anything.

Run as a script to (re)write the sample outputs and check them:
    python -I -B -X utf8 build_sample_hi.py          # write + check
    python -I -B -X utf8 build_sample_hi.py --check  # check only

Outputs:
    AI_translation/hindi/pi-7-hindi-plain-zeroshot_split_chapters/preamble.md
    AI_translation/hindi/pi-7-hindi-plain-zeroshot_split_chapters/1-00-paccaya.md
    0-INBOX/temp/pipeline/pi-7-hi/sample/<name>-pali.md and <name>.md  (s2, s3, s4)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
HI_DIR = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"
SAMPLE_DIR = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-7-hi" / "sample"

# =====================================================================================
# 1. Book frame and headings
# =====================================================================================
HOMAGE = "उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन"
ABHIDHAMMAPITAKE = "अभिधम्म पिटक में"
BOOK_TITLE = "कारण-संबंध"                      # Paṭṭhānapāḷi
BOOK_TITLE_ALTERNATIVES = ["परिघटनाओं के कारण-संबंध", "कारण-संबंधों का ग्रंथ"]

BHAGA = {1: "(पहला भाग)", 2: "(दूसरा भाग)", 3: "(तीसरा भाग)", 4: "(चौथा भाग)",
         5: "(पाँचवाँ भाग)", 6: "(छठा भाग)"}

# methods (naya): anuloma / paccanīya and their mixtures
ANULOMA = "सकारात्मक क्रम"
PACCANIYA = "नकारात्मक क्रम"
ANULOMAPACCANIYA = "सकारात्मक-नकारात्मक क्रम"
PACCANIYANULOMA = "नकारात्मक-सकारात्मक क्रम"

DHAMMANULOMA = "परिघटनाओं का सकारात्मक क्रम"                    # Dhammānulome
DHAMMAPACCANIYA = "परिघटनाओं का नकारात्मक क्रम"                 # Dhammapaccanīye
DHAMMANULOMAPACCANIYA = "परिघटनाओं का सकारात्मक-नकारात्मक क्रम"  # Dhammānulomapaccanīye
DHAMMAPACCANIYANULOMA = "परिघटनाओं का नकारात्मक-सकारात्मक क्रम"  # Dhammapaccanīyānulome

PACCAYANULOMA = "कारणों का सकारात्मक क्रम"                       # Paccayānulomaṃ
PACCAYAPACCANIYA = "कारणों का नकारात्मक क्रम"                    # Paccayapaccanīyaṃ
PACCAYANULOMAPACCANIYA = "कारणों का सकारात्मक-नकारात्मक क्रम"     # Paccayānulomapaccanīyaṃ
PACCAYAPACCANIYANULOMA = "कारणों का नकारात्मक-सकारात्मक क्रम"     # Paccayapaccanīyānulomaṃ

TIKA_PL = "तीन-तीन के वर्गीकरण"     # tika (pi-2 heading "Tikaṃ")
DUKA_PL = "दो-दो के वर्गीकरण"       # duka (pi-2 heading "Dukaṃ")
PATTHANA_OF = "के कारण-संबंध"
TIKAPATTHANA = "तीन-तीन के वर्गीकरणों के कारण-संबंध"
DUKAPATTHANA = "दो-दो के वर्गीकरणों के कारण-संबंध"
DUKATIKAPATTHANA = "दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध"
TIKADUKAPATTHANA = "तीन-तीन और दो-दो के वर्गीकरणों के कारण-संबंध"
TIKATIKAPATTHANA = "तीन-तीन और तीन-तीन के वर्गीकरणों के कारण-संबंध"
DUKADUKAPATTHANA = "दो-दो और दो-दो के वर्गीकरणों के कारण-संबंध"

PACCAYUDDESA = "कारणों की सूची"          # Paccayuddeso
PACCAYANIDDESA = "कारणों की व्याख्या"     # Paccayaniddeso
NIDDESAVARE = "व्याख्या के खंड में"       # Niddesavāre

VARA = {  # section names (vāra = खंड, as pi-6 "मूल का खंड")
    "pucchā": "पूछताछ का खंड",          # Pucchāvāro
    "paṭicca": "निर्भरता का खंड",        # Paṭiccavāro
    "sahajāta": "सह-उत्पत्ति का खंड",     # Sahajātavāro
    "paccaya": "कारण का खंड",            # Paccayavāro
    "nissaya": "आश्रय का खंड",           # Nissayavāro
    "saṃsaṭṭha": "घुले-मिले होने का खंड",  # Saṃsaṭṭhavāro
    "sampayutta": "जुड़ाव का खंड",        # Sampayuttavāro
    "pañhā": "प्रश्नों का खंड",           # Pañhāvāro
    "vibhaṅga": "विश्लेषण का खंड",        # Vibhaṅgavāro
    "saṅkhyā": "गणना का खंड",            # Saṅkhyāvāro
}

# triad / dyad / cluster headings
def TIKA(x):      # Kusalattikaṃ -> TIKA("हितकर")
    return f"{x} वाला तीन का वर्गीकरण"


def DUKA(x):      # Hetudukaṃ -> DUKA("मूल")
    return f"{x} वाला दो का वर्गीकरण"


def GOCCHAKA(x):  # Hetugocchakaṃ -> GOCCHAKA("मूलों")  (pi-1: "मूलों का वर्ग")
    return f"{x} का वर्ग"


# =====================================================================================
# 2. Core terms
# =====================================================================================
DHAMMA, DHAMMA_PL, DHAMMA_OBL_PL = "परिघटना", "परिघटनाएँ", "परिघटनाओं"
PACCAYA = "कारण"
T = {"k": "हितकर", "a": "हानिकर", "ab": "नैतिक रूप से अनिर्धारित"}   # kusala / akusala / abyākata

KHANDHA, KHANDHA_OBL_PL = "समूह", "समूहों"
RUPA = "भौतिक रूप"
CSR = "मन से उत्पन्न भौतिक रूप"                 # cittasamuṭṭhānaṃ rūpaṃ
CSR_OBL = "मन से उत्पन्न भौतिक रूपों"            # cittasamuṭṭhānānaṃ rūpānaṃ
AND_CSR = "और मन से उत्पन्न भौतिक रूप"          # cittasamuṭṭhānañca rūpaṃ
KTR = "किए गए कर्म से उत्पन्न भौतिक रूप"         # kaṭattārūpaṃ
KTR_OBL = "किए गए कर्म से उत्पन्न भौतिक रूपों"   # kaṭattārūpānaṃ
AND_KTR = "और किए गए कर्म से उत्पन्न भौतिक रूप"  # kaṭattā ca rūpaṃ
UPR = "व्युत्पन्न भौतिक रूप"                     # upādārūpaṃ
UPR_OBL = "व्युत्पन्न भौतिक रूपों"
TAMSAM_RUPA_OBL = "उनसे उत्पन्न भौतिक रूपों"     # taṃsamuṭṭhānānaṃ rūpānaṃ
VATTHU = "आधार"                                  # vatthu (pi-2)
MAHABHUTA = "महाभूत"
MAHABHUTA_OBL = "महाभूतों"
PATISANDHI = "पुनर्जन्म के क्षण में"             # paṭisandhikkhaṇe
AHETUKA_PATISANDHI = "मूल से रहित पुनर्जन्म के क्षण में"  # ahetukapaṭisandhikkhaṇe
OKKANTI = "गर्भ में उतरने के क्षण में"           # okkantikkhaṇe
NAMARUPA = "मानसिक पक्ष और भौतिक रूप"            # nāmarūpaṃ (pi-2)
ARUPE = "अभौतिक लोक में"                         # arūpe (pi-6)
BAHIRA = "बाह्य"                                  # bāhiraṃ (pi-1/pi-2)
AHARASAM = "आहार से उत्पन्न"                     # āhārasamuṭṭhānaṃ
UTUSAM = "तापमान से उत्पन्न"                     # utusamuṭṭhānaṃ
ASANNASATTA = "पहचान-रहित प्राणियों में"         # asaññasattānaṃ (pi-6 "पहचान-रहित प्राणी")
AHETUKA = "मूल से रहित"                           # ahetukaṃ (pi-6)
VIPAKA_ABY = "कर्म के फल रूपी नैतिक रूप से अनिर्धारित"       # vipākābyākata (pi-1)
KIRIYA_ABY = "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित"      # kiriyābyākata (pi-1)
VK_SG = "कर्म के फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित"  # vipākābyākataṃ kiriyābyākataṃ (sg.)
VK_PL = "कर्म के फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित"  # vipākābyākate kiriyābyākate (pl.)
CITTACETASIKA = "मन और मन की सहचर परिघटनाएँ"      # cittacetasikā dhammā (pi-1)
CITTACETASIKA_OBL = "मन और मन की सहचर परिघटनाओं"
ARUPINO_KHANDHA = "चार अभौतिक समूह"                # cattāro khandhā arūpino
CATTARO_MAHABHUTA = "चार महाभूत"
ANNAMANNAM = "एक-दूसरे के लिए"                    # aññamaññaṃ
SAMPAYUTTAKA_KH_OBL = "जुड़े हुए समूहों"           # sampayuttakānaṃ khandhānaṃ
SAMPAYUTTAKA_DH_OBL = "जुड़ी हुई परिघटनाओं"        # sampayuttakānaṃ dhammānaṃ
CETANA = "इरादा"
PANCAVINNANA_SAHAGATA = "पाँच प्रकार की चेतना के साथ होने वाले"  # pañcaviññāṇasahagataṃ (oblique)
RUPAJIVITINDRIYA = "भौतिक जीवन-क्षमता"
MOHA_VU = "संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह"
KHANDHE_VU = "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों"

SENSE = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर"}
SENSES = ["cakkhu", "sota", "ghāna", "jivhā", "kāya"]
OBJECT = {"rūpa": "दृश्य रूप", "sadda": "ध्वनि", "gandha": "गंध", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श"}
OBJECTS = ["rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba"]


def VD(s):            # cakkhuviññāṇadhātu
    return f"{SENSE[s]} की चेतना का तत्व"


def VD_OBL(s):        # cakkhuviññāṇadhātuyā
    return f"{SENSE[s]} की चेतना के तत्व"


def VINNANA(s):       # cakkhuviññāṇa (not dhātu), as in the pañhāvāra
    return f"{SENSE[s]} की चेतना"


MANODHATU, MANODHATU_OBL = "मन का तत्व", "मन के तत्व"
MVD, MVD_OBL = "मन की चेतना का तत्व", "मन की चेतना के तत्व"


def AYA_SENSE(s):     # cakkhāyatanaṃ
    return f"{SENSE[s]} का इंद्रिय-क्षेत्र"


def AYA_OBJ(o):       # rūpāyatanaṃ
    return f"{OBJECT[o]} का इंद्रिय-क्षेत्र"


def INDRIYA_SENSE(s):  # cakkhundriyaṃ
    return f"{SENSE[s]} की क्षमता"


def FOR_ASSOC(obl):   # X-dhātuyā taṃsampayuttakānañca dhammānaṃ
    return f"{obl} के लिए और उससे जुड़ी परिघटनाओं के लिए"


# =====================================================================================
# 3. The 24 conditions
# =====================================================================================
COND_KEYS = ["hetu", "ārammaṇa", "adhipati", "anantara", "samanantara", "sahajāta", "aññamañña",
             "nissaya", "upanissaya", "purejāta", "pacchājāta", "āsevana", "kamma", "vipāka",
             "āhāra", "indriya", "jhāna", "magga", "sampayutta", "vippayutta", "atthi", "natthi",
             "vigata", "avigata"]
COND_BASE = {
    "hetu": "मूल", "ārammaṇa": "विषय", "adhipati": "प्रधानता", "anantara": "निकटता",
    "samanantara": "पूर्ण निकटता", "sahajāta": "सह-उत्पत्ति", "aññamañña": "परस्पर",
    "nissaya": "आश्रय", "upanissaya": "प्रबल आश्रय", "purejāta": "पूर्व-उत्पत्ति",
    "pacchājāta": "पश्चात्-उत्पत्ति", "āsevana": "पुनरावृत्ति", "kamma": "कर्म",
    "vipāka": "कर्म-फल", "āhāra": "आहार", "indriya": "क्षमता", "jhāna": "ध्यान",
    "magga": "मार्ग", "sampayutta": "जुड़ाव", "vippayutta": "अलगाव", "atthi": "उपस्थिति",
    "natthi": "अनुपस्थिति", "vigata": "विलीनता", "avigata": "अविलीनता",
}
# Pāli locative used in the counting sections (hetuyā nava, ārammaṇe tīṇi ...)
COND_LOC_PALI = {
    "hetu": "hetuyā", "ārammaṇa": "ārammaṇe", "adhipati": "adhipatiyā", "anantara": "anantare",
    "samanantara": "samanantare", "sahajāta": "sahajāte", "aññamañña": "aññamaññe",
    "nissaya": "nissaye", "upanissaya": "upanissaye", "purejāta": "purejāte",
    "pacchājāta": "pacchājāte", "āsevana": "āsevane", "kamma": "kamme", "vipāka": "vipāke",
    "āhāra": "āhāre", "indriya": "indriye", "jhāna": "jhāne", "magga": "magge",
    "sampayutta": "sampayutte", "vippayutta": "vippayutte", "atthi": "atthiyā",
    "natthi": "natthiyā", "vigata": "vigate", "avigata": "avigate",
}
NEG_PREFIX_PALI = {k: ("no" if k in ("atthi", "natthi", "vigata", "avigata") else "na") for k in COND_KEYS}


def NAME(k):    # hetupaccayo (name, heading, list)
    return f"{COND_BASE[k]}-कारण"


def ABL(k):     # hetupaccayā (frame: "... मूल-कारण से उत्पन्न होती है")
    return f"{NAME(k)} से"


def NABL(k):    # nahetupaccayā
    return f"{NAME(k)} के बिना"


def INS(k):     # hetupaccayena paccayo  (+ होता/होती/होते है/हैं)
    return f"{NAME(k)} के रूप में कारण"


def LOC(k):     # hetuyā (counts)
    return f"{NAME(k)} में"


def NLOC(k):    # nahetuyā (counts)
    return f"{NAME(k)} के अभाव में"


def NNAME(k):   # nahetupaccayo (heading)
    return f"{NAME(k)} का अभाव"


def NNAME_OBL(k):  # nahetupaccaya- before a postposition: "मूल-कारण के अभाव के समान"
    return f"{NAME(k)} के अभाव"


def DEF(k):     # Hetupaccayoti – (start of a niddesa line)
    return f"{NAME(k)} –"


def SADISA(k, neg=False):  # X-paccayasadisaṃ / naX-paccayasadisaṃ
    return f"{NNAME_OBL(k) if neg else NAME(k)} के समान"


def CH(*items):
    """Ablative chain: CH("hetu", "-ārammaṇa") -> "मूल-कारण से, विषय-कारण के बिना"."""
    return ", ".join(NABL(i[1:]) if i.startswith("-") else ABL(i) for i in items)


# subtypes used in the pañhāvāra (proposed for the later chapters)
ARAMMANADHIPATI = "विषय रूपी प्रधानता"          # ārammaṇādhipati
SAHAJATADHIPATI = "सह-उत्पत्ति रूपी प्रधानता"   # sahajātādhipati
ARAMMANUPANISSAYA = "विषय रूपी प्रबल आश्रय"      # ārammaṇūpanissayo
ANANTARUPANISSAYA = "निकटता रूपी प्रबल आश्रय"    # anantarūpanissayo
PAKATUPANISSAYA = "स्वाभाविक प्रबल आश्रय"        # pakatūpanissayo
ARAMMANAPUREJATA = "विषय रूपी पूर्व-उत्पत्ति"     # ārammaṇapurejātaṃ
VATTHUPUREJATA = "आधार रूपी पूर्व-उत्पत्ति"       # vatthupurejātaṃ

# =====================================================================================
# 4. Numbers (counting sections)
# =====================================================================================
NUM = {"ekaṃ": "एक", "dve": "दो", "tīṇi": "तीन", "cattāri": "चार", "pañca": "पाँच", "cha": "छह",
       "satta": "सात", "aṭṭha": "आठ", "nava": "नौ", "dasa": "दस", "ekādasa": "ग्यारह",
       "dvādasa": "बारह", "terasa": "तेरह", "cuddasa": "चौदह", "pannarasa": "पंद्रह",
       "soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह", "ekūnavīsati": "उन्नीस",
       "vīsati": "बीस", "ekavīsati": "इक्कीस", "bāvīsati": "बाईस", "tevīsati": "तेईस",
       "catuvīsati": "चौबीस", "tīṇeva": "तीन ही"}
# heading names of the combination groups (Dukaṃ, Tikaṃ, Dvādasakaṃ ...)
GROUP = {"dukaṃ": 2, "tikaṃ": 3, "catukkaṃ": 4, "pañcakaṃ": 5, "chakkaṃ": 6, "sattakaṃ": 7,
         "aṭṭhakaṃ": 8, "navakaṃ": 9, "dasakaṃ": 10, "ekādasakaṃ": 11, "dvādasakaṃ": 12,
         "terasakaṃ": 13, "cuddasakaṃ": 14, "pannarasakaṃ": 15, "vīsakaṃ": 20, "ekavīsakaṃ": 21,
         "bāvīsakaṃ": 22, "tevīsakaṃ": 23}
NUM_WORD = {1: "एक", 2: "दो", 3: "तीन", 4: "चार", 5: "पाँच", 6: "छह", 7: "सात", 8: "आठ", 9: "नौ",
            10: "दस", 11: "ग्यारह", 12: "बारह", 13: "तेरह", 14: "चौदह", 15: "पंद्रह", 20: "बीस",
            21: "इक्कीस", 22: "बाईस", 23: "तेईस", 24: "चौबीस"}


def GROUP_HI(n):          # Dukaṃ -> "दो कारणों का मेल"
    return f"{NUM_WORD[n]} कारणों का मेल"


SASEVANA = "(पुनरावृत्ति-कारण सहित)"    # (sāsevanaṃ)
SAVIPAKA = "(कर्म-फल-कारण सहित)"       # (savipākaṃ)
SUDDHA = "अकेले-अकेले कारण"            # Suddhaṃ
SABBATTHA_EKAM = "(हर जगह एक)"          # (sabbattha ekaṃ)


def SERIES(n):            # ekamūlakaṃ, dumūlakaṃ ... (n = 1..23); n=0 -> sabbamūlakaṃ
    if n == 0:
        return "सभी कारणों वाली शृंखला"
    return "एक कारण वाली शृंखला" if n == 1 else f"{NUM_WORD[n]} कारणों वाली शृंखला"


def MULAKA(k, neg=False):  # hetumūlakaṃ / nahetumūlakaṃ
    return f"{NNAME_OBL(k) if neg else NAME(k)} से शुरू होने वाली शृंखला"


def GANANA_MULAKA(k, neg=False):  # Gaṇanā hetumūlakā
    return f"{NNAME_OBL(k) if neg else NAME(k)} से शुरू होने वाली गणना"


def DUKANI(k, neg=False, plural=False):  # Āsevanadukaṃ / Nahetudukaṃ / Ārammaṇādidukāni
    base = NNAME_OBL(k) if neg else NAME(k)
    return f"{base} के साथ दो कारणों {'के मेल' if plural else 'का मेल'}"


# =====================================================================================
# 5. Frames
# =====================================================================================
# dependence words of the six "dependent" sections
DEP = {"paṭicca": "पर निर्भर होकर", "sahajāta": "के साथ जन्म लेकर", "paccaya": "के कारण",
       "nissaya": "के आश्रय से", "saṃsaṭṭha": "से घुल-मिलकर", "sampayutta": "से जुड़कर"}


def OBJ(items):
    """Pāli accusative item(s): kusalaṃ dhammaṃ / kusalañca abyākatañca dhammaṃ."""
    w = [f"{T[i]} {DHAMMA}" for i in items]
    return w[0] if len(w) == 1 else (", ".join(w[:-1]) + " और " + w[-1])


def RES(items):
    """Pāli nominative item(s): kusalo dhammo / kusalo ca abyākato ca dhammā."""
    if len(items) == 1:
        return f"{T[items[0]]} {DHAMMA}"
    w = [T[i] for i in items]
    return ", ".join(w[:-1]) + " और " + w[-1] + " " + DHAMMA_PL


def DAT(items):
    """Pāli dative/genitive item(s): kusalassa dhammassa / kusalassa ca abyākatassa ca dhammassa."""
    return OBJ(items) + " के लिए"


def VERB(items, potential=False):
    """uppajjati / uppajjanti -> "उत्पन्न होती है/हैं"; uppajjeyya / uppajjeyyuṃ (potential) -> "उत्पन्न हो सकती है/हैं"."""
    pl = len(items) > 1
    if potential:
        return "उत्पन्न हो सकती हैं" if pl else "उत्पन्न हो सकती है"
    return "उत्पन्न होती हैं" if pl else "उत्पन्न होती है"


SIYA = "क्या"   # Siyā … uppajjeyya (pucchāvāra): a question, «क्या … उत्पन्न हो सकती है?» (user, 2026-11-13)


def PATICCA(o, r, cond, dep="paṭicca"):
    """Kusalaṃ dhammaṃ paṭicca kusalo dhammo uppajjati hetupaccayā (cond = ABL(..)/NABL(..)/CH(..))."""
    return f"{OBJ(o)} {DEP[dep]} {RES(r)} {cond} {VERB(r)}"


def Q(o, r, cond, dep="paṭicca"):
    """Siyā kusalaṃ dhammaṃ paṭicca kusalo dhammo uppajjeyya hetupaccayā (final «?» added by the caller)."""
    return f"{SIYA} {OBJ(o)} {DEP[dep]} {RES(r)} {cond} {VERB(r, True)}"


def PANHA(src, dst, k, neg=False):
    """Kusalo dhammo kusalassa dhammassa hetupaccayena paccayo."""
    ins = INS(k)
    return f"{RES(src)}, {DAT(dst)} {ins} {'नहीं होती' if neg else 'होती है'}"


# khandha / mahābhūta phrases ("dependent" word is a parameter for the other sections)
def KH(first, tail="", dep="paṭicca"):
    """<first> paṭicca tayo khandhā<tail>, tayo khandhe paṭicca eko khandho<tail>, dve ... dve khandhā<tail>"""
    d = DEP[dep]
    return (f"{first} {d} तीन समूह{tail}, तीन समूहों {d} एक समूह{tail}, "
            f"दो समूहों {d} दो समूह{tail}")


def KH13(first, dep="paṭicca"):   # kusalaṃ ekaṃ khandhaṃ paṭicca tayo khandhā
    return f"{first} {DEP[dep]} तीन समूह"


KH_FIRST = {  # "<adj> ekaṃ khandhaṃ"
    "k": "एक हितकर समूह", "a": "एक हानिकर समूह", "vk": f"{VK_SG} एक समूह",
    "v": f"{VIPAKA_ABY} एक समूह", "ki": f"{KIRIYA_ABY} एक समूह",
    "ahetuka_vk": f"{AHETUKA}, {VK_SG} एक समूह", "arupe_k": f"{ARUPE} एक हितकर समूह",
    "arupe_a": f"{ARUPE} एक हानिकर समूह", "arupe_vk": f"{ARUPE} {VK_SG} एक समूह",
    "pancavinnana": f"{PANCAVINNANA_SAHAGATA} एक समूह",
}


def KHE(adj, dep="paṭicca"):      # kusale khandhe paṭicca
    return f"{adj} समूहों {DEP[dep]}"


KH_VATTHU = "समूहों पर निर्भर होकर आधार, आधार पर निर्भर होकर समूह"   # khandhe paṭicca vatthu, vatthuṃ paṭicca khandhā


def MB(first="एक महाभूत", dep="paṭicca"):
    """ekaṃ mahābhūtaṃ paṭicca tayo mahābhūtā, tayo mahābhūte paṭicca ekaṃ mahābhūtaṃ, dve ... dve mahābhūtā"""
    d = DEP[dep]
    return f"{first} {d} तीन महाभूत, तीन महाभूतों {d} एक महाभूत, दो महाभूतों {d} दो महाभूत"


def MB13(first="एक महाभूत", dep="paṭicca"):
    return f"{first} {DEP[dep]} तीन महाभूत"


def MBE(x, adj="", dep="paṭicca"):  # (bāhire) mahābhūte paṭicca X
    a = f"{adj} " if adj else ""
    return f"{a}महाभूतों {DEP[dep]} {x}"


EXT_CHAIN = f"{BAHIRA}… {AHARASAM}… {UTUSAM}… {ASANNASATTA}"   # bāhiraṃ… āhārasamuṭṭhānaṃ… utusamuṭṭhānaṃ… asaññasattānaṃ
KH_AND_MB_CSR = "समूहों और महाभूतों पर निर्भर होकर " + CSR   # (kusale) khandhe ca mahābhūte ca paṭicca cittasamuṭṭhānaṃ rūpaṃ


def KH_MB(adj):
    return f"{adj} {KH_AND_MB_CSR}"


# pañhāvāra wording
DANA3 = "दान देकर, सदाचार ग्रहण करके, उपवास-व्रत का पालन करके"   # dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā
SUCINNA = "पहले भली-भाँति किए गए कार्यों"                        # pubbe suciṇṇāni (oblique)
SEKKHA = "सीखने के चरण वाले"                                     # sekkhā
PUTHUJJANA = "साधारण व्यक्ति"                                    # puthujjanā
SEKKHA_VA_PUTHUJJANA = f"{SEKKHA} या {PUTHUJJANA}"
ARAHA = "अर्हत्"
GOTRABHU = "गोत्र-परिवर्तन"                                       # gotrabhu
VODANA = "शुद्धि"                                                 # vodāna
PHALA, NIBBANA = "फल", "निर्वाण"
ANICCA3 = "अनित्य, दुःख और आत्मा से रहित के रूप में"             # aniccato dukkhato anattato
VIPASSATI, VIPASSANTI = "अंतर्दृष्टि से देखता है", "अंतर्दृष्टि से देखते हैं"
REVIEW_SG, REVIEW_PL = "पुनः विचार करता है", "पुनः विचार करते हैं"  # paccavekkhati / -anti
CETOPARIYA = "दूसरों के मन को जानने का ज्ञान"
CETOPARIYENA = "दूसरों के मन को जानने के ज्ञान से"
IDDHIVIDHA_OBL = "अलौकिक शक्तियों के ज्ञान"
CETOPARIYA_OBL = "दूसरों के मन को जानने के ज्ञान"
PUBBENIVASA_OBL = "पूर्व जन्मों के अनुस्मरण के ज्ञान"
YATHAKAMMUPAGA_OBL = "प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान"
ANAGATAMSA_OBL = "भविष्य को जानने के ज्ञान"
AVAJJANA_FOR = "मन को विषय की ओर मोड़ने के लिए"                 # āvajjanāya
ASSADA = "का रस लेता है"                                          # assādeti
ABHINANDA = "में आनंद लेता है"                                    # abhinandati
ARABBHA = "को विषय बनाकर"                                         # ārabbha
GARUM = "को महत्व देकर"                                           # garuṃ katvā
TADARAMMANA = "कर्म-फल उसी विषय को लेकर उत्पन्न होता है"         # vipāko tadārammaṇatā uppajjati
AROSE5 = ("राग उत्पन्न होता है, दृष्टि उत्पन्न होती है, संशय उत्पन्न होता है, "
          "बेचैनी उत्पन्न होती है, उदासी उत्पन्न होती है")
AROSE4 = "राग उत्पन्न होता है, दृष्टि उत्पन्न होती है, संशय उत्पन्न होता है, बेचैनी उत्पन्न होती है"
AROSE2 = "राग उत्पन्न होता है, दृष्टि उत्पन्न होती है"
ARUPA_AYATANA = {"ākāsānañca": "अनंत आकाश का क्षेत्र", "viññāṇañca": "अनंत चेतना का क्षेत्र",
                 "ākiñcañña": "कुछ भी न होने का क्षेत्र",
                 "nevasaññānāsañña": "न पहचान न अ-पहचान का क्षेत्र"}


def ARUPA_OBL(x):
    return ARUPA_AYATANA[x].replace(" का क्षेत्र", " के क्षेत्र")


SENSE_ACC_PL = ["कान", "नाक", "जीभ", "शरीर", "दृश्य रूपों", "ध्वनियों", "गंधों", "स्वादों",
                "स्पर्शों", "आधार"]   # Sotaṃ… ghānaṃ… jivhaṃ… kāyaṃ… rūpe… sadde… gandhe… rase… phoṭṭhabbe… vatthuṃ…


def SENSE_CHAIN(post):  # "कान को… नाक को… … आधार को…"
    return " ".join(f"{w} {post}…" for w in SENSE_ACC_PL)


# =====================================================================================
# 6. Counting-line converter (saṅkhyāvāra)
# =====================================================================================
_STEMS = sorted(COND_KEYS, key=len, reverse=True)
_ABL_RX = re.compile(r"^(?:(na|no)\s?)?(" + "|".join(_STEMS) + r")paccayā$")
_LOC2KEY = {v: k for k, v in COND_LOC_PALI.items()}
_LOC_RX = re.compile(r"^(?:(na|no)\s?)?(" + "|".join(sorted(_LOC2KEY, key=len, reverse=True)) + r")$")
_SLIPS = {"nadhipatipaccayā": ("neg_abl", "adhipati")}   # elided na+adhipati (source slip)


def _classify(tok):
    low = tok[0].lower() + tok[1:]
    if low in _SLIPS:
        kind, k = _SLIPS[low]
        return kind, k
    m = _ABL_RX.match(low)
    if m:
        return ("neg_abl" if m.group(1) else "abl"), m.group(2)
    m = _LOC_RX.match(low)
    if m:
        return ("neg_loc" if m.group(1) else "loc"), _LOC2KEY[m.group(2)]
    if low in NUM:
        return "num", low
    return "other", tok


def count_hi(pali):
    """Convert a counting line (no block ID): "Hetupaccayā ārammaṇe tīṇi, adhipatiyā nava…pe…."
    -> "मूल-कारण से, विषय-कारण में तीन, प्रधानता-कारण में नौ…।"
    Rules: ablative (= the fixed conditions) -> "X-कारण से" / "X-कारण के बिना"; locative (= the condition
    counted) -> "X-कारण में" / "X-कारण के अभाव में"; numbers as Hindi words; "…pe…" -> "…";
    final "." -> "।"; a comma is put after every ablative and after every number that is followed by
    another word (the Pāli sometimes leaves them out). Raises ValueError on an unknown word.
    """
    toks = re.findall(r"…pe…|…|\(sabbattha ekaṃ\)|[,;.]|na [^\s,;.…]+|[^\s,;.…]+", pali)
    items = []
    for t in toks:
        if t in ("…pe…", "…"):
            items.append(("ell", "…"))
        elif t == "(sabbattha ekaṃ)":
            items.append(("paren", SABBATTHA_EKAM))
        elif t in ",;.":
            items.append(("punct", t))
        else:
            kind, v = _classify(t.replace(" ", ""))
            if kind == "other":
                raise ValueError(f"unknown word in count line: {t!r}")
            items.append((kind, v))
    words = ("abl", "neg_abl", "loc", "neg_loc", "num", "paren")
    out = ""
    for i, (kind, v) in enumerate(items):
        nxt = items[i + 1][0] if i + 1 < len(items) else None
        if kind in words:
            text = {"abl": ABL, "neg_abl": NABL, "loc": LOC, "neg_loc": NLOC}[kind](v) \
                if kind in ("abl", "neg_abl", "loc", "neg_loc") else (NUM[v] if kind == "num" else v)
            if kind in ("abl", "neg_abl", "num") and nxt in words:
                text += ","
            if out and not out.endswith(" "):
                out += " "
            out += text
        else:  # ellipsis or punctuation attaches to the previous word (dropping a comma we added)
            out = out.rstrip(" ").rstrip(",") + ("…" if kind == "ell" else ("।" if v == "." else v))
    return out.strip()


# =====================================================================================
# 7. Verse (the "six methods" stanza)
# =====================================================================================
VERSE_LETTER = {"Ka": "(क)", "Kha": "(ख)", "Ga": "(ग)", "Gha": "(घ)"}


def VERSE(letter, method):
    return [
        f"{VERSE_LETTER[letter]} तीन-तीन के वर्गीकरणों के श्रेष्ठ कारण-संबंध और दो-दो के वर्गीकरणों के उत्तम कारण-संबंध,",
        "दो-दो के साथ तीन-तीन, और तीन-तीन के साथ दो-दो;",
        "तीन-तीन के साथ तीन-तीन, और दो-दो के साथ दो-दो,",
        f"{method} में ये छह विधियाँ अत्यंत गहन हैं।",
    ]


# =====================================================================================
# 8. Assembly helpers
# =====================================================================================
ID_RX = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def nonempty(text):
    return [l for l in text.splitlines() if l.strip()]


def assemble(pali_text, hindi_lines):
    """Lay Hindi lines (without IDs) onto the Pāli layout: same blank lines, same IDs at line end."""
    out, it = [], iter(hindi_lines)
    n = 0
    for line in pali_text.splitlines():
        if not line.strip():
            out.append("")
            continue
        try:
            h = next(it)
        except StopIteration:
            raise SystemExit(f"too few Hindi lines (have {n})")
        n += 1
        m = ID_RX.search(line)
        if m:
            h = f"{h} ^{m.group(1)}"
        lp = len(line) - len(line.lstrip("#"))
        lh = len(h) - len(h.lstrip("#"))
        if lp != lh:
            raise SystemExit(f"heading level differs at Hindi line {n}: {h[:60]}")
        out.append(h)
    rest = list(it)
    if rest:
        raise SystemExit(f"{len(rest)} Hindi lines too many")
    return "\n".join(out).rstrip("\n") + "\n"


def excerpt(fname, first, last):
    """Pāli excerpt by NON-EMPTY line numbers (1-based, inclusive), keeping the blank lines between."""
    lines = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
    out, n, on = [], 0, False
    for line in lines:
        if line.strip():
            n += 1
            on = first <= n <= last
            if n > last:
                break
        if on:
            out.append(line)
    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out) + "\n"


# =====================================================================================
# 9. Content: preamble and 1-00-paccaya
# =====================================================================================
def build_preamble():
    return [HOMAGE, f"# {ABHIDHAMMAPITAKE}", f"## {BOOK_TITLE}"]


def _purima(x, y, k, some=False):
    s = "कुछ " if some else ""
    return f"पहले-पहले की {T[x]} {DHAMMA_PL} बाद-बाद की {s}{T[y]} {DHAMMA_OBL_PL} के लिए {INS(k)} होती हैं।"


def _yam(kind, k):
    lead = {"ārabbha": "जिस-जिस परिघटना को विषय बनाकर",
            "garu": "जिस-जिस परिघटना को महत्व देकर",
            "anantara": "जिन-जिन परिघटनाओं के ठीक बाद",
            "samanantara": "जिन-जिन परिघटनाओं के बिलकुल ठीक बाद"}[kind]
    return (f"{lead} जो-जो परिघटनाएँ, यानी {CITTACETASIKA}, उत्पन्न होती हैं, "
            f"वे-वे परिघटनाएँ उन-उन परिघटनाओं के लिए {INS(k)} होती हैं।")


def _adhipati_sentence(subj, gender, assoc):
    verb = "होती है" if gender == "f" else "होता है"
    return f"{subj}, {assoc} से जुड़ी परिघटनाओं के लिए और {TAMSAM_RUPA_OBL} के लिए {INS('adhipati')} {verb}।"


def _dhatu_lines(k):
    out = [f"{VD(s)} और उससे जुड़ी परिघटनाएँ {FOR_ASSOC(MANODHATU_OBL)} {INS(k)} होती हैं। "
           f"{MANODHATU} और उससे जुड़ी परिघटनाएँ {FOR_ASSOC(MVD_OBL)} {INS(k)} होती हैं।" for s in SENSES]
    out.append(" ".join([_purima("k", "k", k), _purima("k", "ab", k)]))
    out.append(" ".join([_purima("a", "a", k), _purima("a", "ab", k)]))
    out.append(" ".join([_purima("ab", "ab", k), _purima("ab", "k", k), _purima("ab", "a", k)]))
    return out


def _group5(k, mutual=True):
    a = f"{ANNAMANNAM} " if mutual else ""
    return [f"{ARUPINO_KHANDHA} {a}{INS(k)} होते हैं।",
            f"{CATTARO_MAHABHUTA} {a}{INS(k)} होते हैं।",
            f"{OKKANTI} {NAMARUPA} {a}{INS(k)} होते हैं।",
            f"{CITTACETASIKA} {CSR_OBL} के लिए {INS(k)} होती हैं।",
            f"{MAHABHUTA} {UPR_OBL} के लिए {INS(k)} होते हैं।"]


def _sense_bases(k):
    return " ".join(f"{AYA_SENSE(s)} {FOR_ASSOC(VD_OBL(s))} {INS(k)} होता है।" for s in SENSES)


def _object_bases(k):
    one = [f"{AYA_OBJ(o)} {FOR_ASSOC(VD_OBL(s))} {INS(k)} होता है।" for o, s in zip(OBJECTS, SENSES)]
    five = ", ".join(AYA_OBJ(o) for o in OBJECTS[:-1]) + " और " + AYA_OBJ(OBJECTS[-1])
    one.append(f"{five} {FOR_ASSOC(MANODHATU_OBL)} {INS(k)} होते हैं।")
    return " ".join(one)


YAM_RUPA = "जिस भौतिक रूप के आश्रय से मन का तत्व और मन की चेतना का तत्व क्रियाशील होते हैं, वह भौतिक रूप"
FOR_MD_MVD = "मन के तत्व के लिए, मन की चेतना के तत्व के लिए और उनसे जुड़ी परिघटनाओं के लिए"


def _yam_rupa_both(k):
    return f"{YAM_RUPA} {FOR_MD_MVD} {INS(k)} होता है।"


SEVEN_RES = {  # result order in the pucchāvāra item paragraphs
    "k": [["k"], ["a"], ["ab"]], "a": [["a"], ["k"], ["ab"]], "ab": [["ab"], ["k"], ["a"]],
    "mix": [["k"], ["a"], ["ab"]],
}
TAIL_RES = [["k", "ab"], ["a", "ab"], ["k", "a"], ["k", "a", "ab"]]


def _pada(obj, first3, cond):
    return " ".join(Q(obj, r, cond) + "?" for r in first3 + TAIL_RES)


def build_1_00():
    K = COND_KEYS
    H = []
    H += ["### " + BHAGA[1], "#### " + DHAMMANULOMA, "##### " + TIKAPATTHANA,
          "###### (1) " + PACCAYUDDESA,
          ", ".join(NAME(k) for k in K[:-1]) + " और " + NAME(K[-1]) + "।",
          "###### (2) " + PACCAYANIDDESA]
    # hetu
    H.append(f"{DEF('hetu')} मूल, मूलों से जुड़ी परिघटनाओं के लिए और {TAMSAM_RUPA_OBL} के लिए "
             f"{INS('hetu')} होते हैं [पाठभेद (Syā.): paccayoti]।")
    # ārammaṇa
    H.append(f"{DEF('ārammaṇa')} {_object_bases('ārammaṇa')} "
             f"सभी परिघटनाएँ {FOR_ASSOC(MVD_OBL)} {INS('ārammaṇa')} होती हैं।")
    H.append(_yam("ārabbha", "ārammaṇa"))
    # adhipati
    H.append(f"{DEF('adhipati')} " + " ".join([
        _adhipati_sentence("प्रधान बनी हुई चाह", "f", "चाह"),
        _adhipati_sentence("प्रधान बना हुआ उत्साह", "m", "उत्साह"),
        _adhipati_sentence("प्रधान बना हुआ मन", "m", "मन"),
        _adhipati_sentence("प्रधान बनी हुई जाँच-परख", "f", "जाँच-परख")]))
    H.append(_yam("garu", "adhipati"))
    # anantara / samanantara
    for k in ("anantara", "samanantara"):
        dl = _dhatu_lines(k)
        dl[0] = f"{DEF(k)} " + dl[0]
        H += dl
        H.append(_yam(k, k))
    # sahajāta
    g = _group5("sahajāta")
    H.append(f"{DEF('sahajāta')} " + " ".join(g) +
             f" भौतिक परिघटनाएँ अभौतिक परिघटनाओं के लिए किसी समय [पाठभेद (Syā.): kañci kālaṃ] "
             f"{INS('sahajāta')} होती हैं, किसी समय {INS('sahajāta')} नहीं होतीं।")
    # aññamañña
    H.append(f"{DEF('aññamañña')} " + " ".join(_group5("aññamañña", mutual=False)[:3]))
    # nissaya
    H.append(f"{DEF('nissaya')} " + " ".join(_group5("nissaya")))
    H.append(_sense_bases("nissaya") + " " + _yam_rupa_both("nissaya"))
    # upanissaya
    k = "upanissaya"
    H.append(f"{DEF(k)} " + " ".join([_purima("k", "k", k), _purima("k", "a", k, True), _purima("k", "ab", k)]))
    H.append(" ".join([_purima("a", "a", k), _purima("a", "k", k, True), _purima("a", "ab", k)]))
    H.append(" ".join([_purima("ab", "ab", k), _purima("ab", "k", k), _purima("ab", "a", k)]))
    H.append(f"तापमान और भोजन भी {INS(k)} होते हैं। व्यक्ति भी {INS(k)} होता है। "
             f"निवास-स्थान भी {INS(k)} होता है।")
    # purejāta
    k = "purejāta"
    H.append(f"{DEF(k)} " + _sense_bases(k))
    H.append(_object_bases(k))
    H.append(f"{YAM_RUPA} {FOR_ASSOC(MANODHATU_OBL)} {INS(k)} होता है। "
             f"{FOR_ASSOC(MVD_OBL)} वह किसी समय {INS(k)} होता है, किसी समय {INS(k)} नहीं होता।")
    # pacchājāta
    H.append(f"{DEF('pacchājāta')} बाद में उत्पन्न {CITTACETASIKA} पहले उत्पन्न इस शरीर के लिए "
             f"{INS('pacchājāta')} होती हैं।")
    # āsevana
    k = "āsevana"
    H.append(f"{DEF(k)} " + " ".join([
        _purima("k", "k", k), _purima("a", "a", k),
        f"पहले-पहले की {KIRIYA_ABY} {DHAMMA_PL} बाद-बाद की {KIRIYA_ABY} {DHAMMA_OBL_PL} के लिए {INS(k)} होती हैं।"]))
    # kamma
    k = "kamma"
    H.append(f"{DEF(k)} हितकर और हानिकर कर्म, कर्म के फल रूपी समूहों के लिए और {KTR_OBL} के लिए {INS(k)} होता है। "
             f"{CETANA} {SAMPAYUTTAKA_DH_OBL} के लिए और {TAMSAM_RUPA_OBL} के लिए {INS(k)} होता है।")
    # vipāka
    H.append(f"{DEF('vipāka')} कर्म के फल रूपी {ARUPINO_KHANDHA} {ANNAMANNAM} {INS('vipāka')} होते हैं।")
    # āhāra
    k = "āhāra"
    H.append(f"{DEF(k)} कौर-कौर खाया जाने वाला [वर्तनी-भेद (Ka., Sī., Syā.): kabaḷiṅkāro] भोजन "
             f"इस शरीर के लिए {INS(k)} होता है। अभौतिक आहार {SAMPAYUTTAKA_DH_OBL} के लिए और "
             f"{TAMSAM_RUPA_OBL} के लिए {INS(k)} होते हैं।")
    # indriya
    k = "indriya"
    H.append(f"{DEF(k)} " + " ".join(
        f"{INDRIYA_SENSE(s)} {FOR_ASSOC(VD_OBL(s))} {INS(k)} होती है।" for s in SENSES) +
        f" {RUPAJIVITINDRIYA} {KTR_OBL} के लिए {INS(k)} होती है।")
    H.append(f"अभौतिक क्षमताएँ {SAMPAYUTTAKA_DH_OBL} के लिए और {TAMSAM_RUPA_OBL} के लिए {INS(k)} होती हैं।")
    # jhāna / magga
    H.append(f"{DEF('jhāna')} ध्यान के अंग ध्यान से जुड़ी परिघटनाओं के लिए और {TAMSAM_RUPA_OBL} के लिए "
             f"{INS('jhāna')} होते हैं।")
    H.append(f"{DEF('magga')} मार्ग के अंग मार्ग से जुड़ी परिघटनाओं के लिए और {TAMSAM_RUPA_OBL} के लिए "
             f"{INS('magga')} होते हैं।")
    # sampayutta / vippayutta
    H.append(f"{DEF('sampayutta')} {ARUPINO_KHANDHA} {ANNAMANNAM} {INS('sampayutta')} होते हैं।")
    k = "vippayutta"
    H.append(f"{DEF(k)} भौतिक परिघटनाएँ अभौतिक परिघटनाओं के लिए {INS(k)} होती हैं। "
             f"अभौतिक परिघटनाएँ भौतिक परिघटनाओं के लिए {INS(k)} होती हैं।")
    # atthi
    k = "atthi"
    H.append(f"{DEF(k)} " + " ".join(_group5(k)))
    H.append(_sense_bases(k))
    H.append(_object_bases(k))
    H.append(_yam_rupa_both(k))
    # natthi / vigata
    H.append(f"{DEF('natthi')} बिलकुल ठीक पहले समाप्त हो चुकी {CITTACETASIKA} वर्तमान "
             f"{CITTACETASIKA_OBL} के लिए {INS('natthi')} होती हैं।")
    H.append(f"{DEF('vigata')} बिलकुल ठीक पहले विलीन हो चुकी {CITTACETASIKA} वर्तमान "
             f"{CITTACETASIKA_OBL} के लिए {INS('vigata')} होती हैं।")
    # avigata
    k = "avigata"
    H.append(f"{DEF(k)} " + " ".join(_group5(k)))
    H.append(_sense_bases(k))
    H.append(_object_bases(k))
    H.append(_yam_rupa_both(k))
    H.append(PACCAYANIDDESA + "।")

    # ---------------- pucchāvāra
    H += ["###### " + VARA["pucchā"], "####### *" + PACCAYANULOMA + "*", "######## *" + SERIES(1) + "*"]
    padas = [("(1.)", ["k"], "k"), ("(2)", ["a"], "a"), ("(3)", ["ab"], "ab"), ("(4)", ["k", "ab"], "mix"),
             ("(5)", ["a", "ab"], "mix"), ("(6)", ["k", "a"], "mix"), ("(7)", ["k", "a", "ab"], "mix")]
    for num, obj, order in padas:
        H.append(f"######## *{num} {RES(obj).replace(' ' + DHAMMA_PL, '').replace(' ' + DHAMMA, '')} पद*")
        H.append(_pada(obj, SEVEN_RES[order], ABL("hetu")))
    H.append(NAME("hetu") + " का खंड।")
    H.append(Q(["k"], ["k"], ABL("ārammaṇa")) + "?")
    H.append("(जैसे मूल-कारण का विस्तार किया गया है, वैसे ही विषय-कारण का भी पाठ के क्रम से विस्तार करना चाहिए।)")
    H.append(f"{SIYA} {OBJ(['k'])} पर निर्भर होकर {RES(['k'])} " + "… ".join(ABL(k) for k in K[2:23]) +
             f" {VERB(['k'], True)}?")
    objs = [["a"], ["ab"], ["k", "ab"], ["a", "ab"], ["k", "a"], ["k", "a", "ab"]]
    res7 = [["k"], ["a"], ["ab"], ["k", "ab"], ["a", "ab"], ["k", "a"], ["k", "a", "ab"]]
    part1 = f"{SIYA} {OBJ(['k'])} पर निर्भर होकर {RES(['k'])} {ABL('avigata')} {VERB(['k'], True)}?…"
    part2 = "… ".join(f"{OBJ(o)} पर निर्भर होकर" for o in objs)
    part3 = "… ".join(f"{RES(r)} {VERB(r, True)}" for r in res7[:-1])
    last = res7[-1]
    H.append(f"{part1} {part2} {part3}… {RES(last)} {ABL('avigata')} {VERB(last, True)}?")
    H.append("(जैसे मूल-कारण का विस्तार किया गया है, वैसे ही अविलीनता-कारण का भी पाठ के क्रम से विस्तार करना चाहिए।)")
    H.append(SERIES(1) + "।")
    # dumūlakādi
    QK = f"{SIYA} {OBJ(['k'])} पर निर्भर होकर {RES(['k'])}"
    QV = VERB(["k"], True)
    H += ["####### *" + SERIES(2) + " आदि*", "######## *" + MULAKA("hetu") + "*"]
    H.append(f"{QK} {CH('hetu', 'ārammaṇa')} {QV}?… {SIYA} {OBJ(['k', 'a', 'ab'])} पर निर्भर होकर "
             f"{RES(['k', 'a', 'ab'])} {CH('hetu', 'ārammaṇa')} {VERB(['k', 'a'], True)}?")
    H.append(f"{QK} {CH('hetu', 'adhipati')}… {CH('hetu', 'anantara')}… {CH('hetu', 'samanantara')}… "
             f"{CH('hetu', 'avigata')} {QV}?")
    H.append(SERIES(2) + "।")
    H.append(f"{QK} {CH('hetu', 'ārammaṇa', 'adhipati')}… {CH('hetu', 'ārammaṇa', 'anantara')}… "
             f"{CH('hetu', 'ārammaṇa', 'avigata')} {QV}?")
    H.append(SERIES(3) + "।")
    H.append(f"{QK} {CH('hetu', 'ārammaṇa', 'adhipati', 'anantara')}… "
             f"{CH('hetu', 'ārammaṇa', 'adhipati', 'avigata')} {QV}?")
    H.append(SERIES(4) + "।")
    H.append(f"({SERIES(5)} आदि संक्षिप्त कर दी गई हैं। {SERIES(1)}, {SERIES(2)}, {SERIES(3)}, "
             f"{SERIES(4)}, {SERIES(5)} और {SERIES(0)} का बिना भ्रमित हुए विस्तार करना चाहिए।)")
    H.append(MULAKA("hetu") + "।")
    H.append("######## *" + MULAKA("ārammaṇa") + " आदि*")
    H.append(f"{QK} {CH('ārammaṇa', 'hetu')}… {CH('ārammaṇa', 'adhipati')}… {CH('ārammaṇa', 'avigata')} {QV}?")
    H.append(f"{QK} {ABL('adhipati')}… {ABL('anantara')}… {ABL('samanantara')}… {ABL('sahajāta')}… "
             f"{ABL('aññamañña')}… {CH('avigata', 'hetu')}… {CH('avigata', 'ārammaṇa')}… "
             f"{CH('avigata', 'adhipati')}… {CH('avigata', 'vigata')} {QV}?")
    H.append(SERIES(2) + "।")
    H.append(f"{QK} {CH('avigata', 'hetu', 'ārammaṇa')}… {CH('avigata', 'hetu', 'adhipati')}… "
             f"{CH('avigata', 'hetu', 'anantara')}… {CH('avigata', 'hetu', 'vigata')} {QV}?")
    H.append(f"{QK} {CH('avigata', 'hetu', 'ārammaṇa', 'adhipati')}… "
             f"{CH('avigata', 'hetu', 'ārammaṇa', 'anantara')}… {ABL('vigata')} {QV}?")
    H.append(f"(हर एक पद की {SERIES(1)}, {SERIES(2)}, {SERIES(3)}, {SERIES(4)}, {SERIES(5)} और "
             f"{SERIES(0)} का बिना भ्रमित हुए विस्तार करना चाहिए।)")
    H += VERSE("Ka", ANULOMA)
    # paccanīya
    H.append("######## *" + PACCAYAPACCANIYA + "*")
    H.append(Q(["k"], ["k"], NABL("hetu")) + "?")
    H.append("(जैसे सकारात्मक क्रम में मूल-कारण का विस्तार किया गया है, वैसे ही नकारात्मक क्रम में भी "
             "मूल-कारण के अभाव का विस्तार करना चाहिए।)")
    H.append(f"{QK} " + "… ".join(NABL(k) for k in K[1:]) + f" {QV}?")
    H.append(f"{QK} {CH('-hetu', '-ārammaṇa')}… {QV}?")
    H.append(f"(जैसे सकारात्मक क्रम में हर एक पद की {SERIES(1)}, {SERIES(2)}, {SERIES(3)}, {SERIES(4)}, "
             f"यहाँ तक कि {SERIES(23)} तक, वैसे ही नकारात्मक क्रम में भी विस्तार करना चाहिए।)")
    H += VERSE("Kha", PACCANIYA)
    # anulomapaccanīya
    H.append("######## *" + PACCAYANULOMAPACCANIYA + "*")
    H.append(f"{QK} {CH('hetu', '-ārammaṇa')} {QV}?… {SIYA} {OBJ(['k'])} पर निर्भर होकर {RES(['a'])} "
             f"{CH('hetu', '-ārammaṇa')} {QV}?")
    H.append("(जैसे सकारात्मक क्रम में मूल-कारण का विस्तार किया गया है, वैसे ही सकारात्मक-नकारात्मक क्रम में भी "
             "पद का विस्तार करना चाहिए।)")
    H.append(f"{QK} {CH('hetu', '-adhipati')}… {CH('hetu', '-anantara')}… {CH('hetu', '-avigata')} {QV}?")
    H.append(f"{QK} {CH('hetu', 'ārammaṇa', '-adhipati')}… {CH('hetu', 'ārammaṇa', '-anantara')}… "
             f"{CH('hetu', 'ārammaṇa', '-avigata')} {QV}?")
    H.append(f"{CH('hetu', 'ārammaṇa', 'adhipati', '-anantara')}… {CH('hetu', 'ārammaṇa', 'adhipati', '-avigata')}।")
    H.append(f"{CH('hetu', 'ārammaṇa', 'adhipati', 'anantara', '-samanantara')}… "
             f"{CH('hetu', 'ārammaṇa', 'adhipati', 'anantara', '-avigata')}…।")
    H.append(CH(*K[:23], "-avigata") + "।")
    H.append(f"{QK} {ABL('ārammaṇa')}… {ABL('adhipati')}… {ABL('anantara')}… {CH('avigata', '-hetu')}… "
             f"{CH('avigata', '-ārammaṇa')}… {CH('avigata', '-vigata')} {QV}?")
    H.append(f"{CH('avigata', 'hetu', '-ārammaṇa')}… {CH('avigata', 'hetu', '-vigata')}।")
    H.append(f"{CH('avigata', 'hetu', 'ārammaṇa', '-adhipati')}… {CH('avigata', 'hetu', 'ārammaṇa', '-vigata')}।")
    H.append(f"{CH('avigata', 'hetu', 'ārammaṇa', 'adhipati', 'anantara', 'samanantara', 'sahajāta')}… "
             f"{NABL('vigata')}।")
    H += VERSE("Ga", ANULOMAPACCANIYA)
    # paccanīyānuloma
    H.append("######## *" + PACCAYAPACCANIYANULOMA + "*")
    H.append(f"{QK} {CH('-hetu', 'ārammaṇa')} {QV}? {QK} {CH('-hetu', 'adhipati')}… {CH('-hetu', 'avigata')} {QV}?")
    H.append(f"{QK} {CH('-hetu', '-ārammaṇa', 'adhipati')}… {ABL('avigata')} {QV}?")
    H.append(f"{CH('-hetu', '-ārammaṇa', '-adhipati')}… {ABL('avigata')}।")
    H.append(f"{CH('-hetu', '-ārammaṇa', '-adhipati', '-anantara', '-samanantara')}… "
             f"{CH('-atthi', '-natthi', '-vigata', 'avigata')}।")
    H.append(Q(["k"], ["k"], CH("-ārammaṇa", "hetu")) + "?")
    H.append(f"{QK} {CH('-ārammaṇa', 'adhipati')}… {CH('-ārammaṇa', 'avigata')}… {CH('-avigata', 'hetu')}… "
             f"{CH('-avigata', 'ārammaṇa')}… {CH('-avigata', 'vigata')} {QV}?")
    H.append(f"{CH('-avigata', '-hetu', 'ārammaṇa')}… {CH('-avigata', '-hetu', 'vigata')}।")
    H.append(f"{CH('-avigata', '-hetu', '-ārammaṇa', '-adhipati')}… {CH('-atthi', '-natthi', 'vigata')}।")
    H += VERSE("Gha", PACCANIYANULOMA)
    H.append(VARA["pucchā"] + "।")
    H.append(f"{NIDDESAVARE} तेईस कारण हैं।")
    return H


# =====================================================================================
# 10. Content: sample 2 (paṭiccavāra, anuloma: vibhaṅga + saṅkhyā)
# =====================================================================================
def _kusala_block(x, k, cnt="(3)", neg=False):
    """The 3-question paragraph for kusala (x='k') or akusala (x='a') under condition k."""
    c = NABL(k) if neg else ABL(k)
    return (f"{PATICCA([x], [x], c)} – {KH(KH_FIRST[x])}। "
            f"{PATICCA([x], ['ab'], c)} – {KHE(T[x])} {CSR}। "
            f"{PATICCA([x], [x, 'ab'], c)} – {KH(KH_FIRST[x], ' ' + AND_CSR)}। {cnt}")


def _mix_line(x, k, cnt=" (1)", neg=False):
    c = NABL(k) if neg else ABL(k)
    return f"{PATICCA([x, 'ab'], ['ab'], c)} – {KH_MB(T[x])}।{cnt}"


def build_s2():
    H = []
    H += ["###### " + TIKA("हितकर"), "####### *" + VARA["paṭicca"] + "*",
          "####### *" + PACCAYANULOMA + "*", "######## *" + VARA["vibhaṅga"] + "*",
          f"######## *{ANULOMA} – {NAME('hetu')}*"]
    k = "hetu"
    H.append(_kusala_block("k", k))
    H.append(_kusala_block("a", k))
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH(KH_FIRST['vk'], ' ' + AND_CSR)}; "
             f"{PATISANDHI} {KH(KH_FIRST['v'], ' ' + AND_KTR)}; {KH_VATTHU}; "
             f"{MB()}, {MBE(CSR + ', ' + KTR + ', ' + UPR)}। (1)")
    H.append(_mix_line("k", k))
    H.append(_mix_line("a", k))
    # ārammaṇa
    k = "ārammaṇa"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH(KH_FIRST['k'])}। (1)")
    H.append(f"{PATICCA(['a'], ['a'], ABL(k))} – {KH(KH_FIRST['a'])}। (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH(KH_FIRST['vk'])}; {PATISANDHI} {KH(KH_FIRST['v'])}, "
             f"आधार पर निर्भर होकर समूह। (1)")
    # adhipati
    k = "adhipati"
    H.append(f"######## *{NAME(k)}*")
    H.append(_kusala_block("k", k))
    H.append(_kusala_block("a", k))
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH(KH_FIRST['vk'], ' ' + AND_CSR)}; "
             f"{MB()}, {MBE(CSR + ', ' + UPR)}। (1)")
    H.append(_mix_line("k", k))
    H.append(_mix_line("a", k))
    # anantara-samanantara
    H.append(f"######## *{NAME('anantara')} और {NAME('samanantara')}*")
    H.append(f"{OBJ(['k'])} पर निर्भर होकर {RES(['k'])} {ABL('anantara')}… {ABL('samanantara')} {VERB(['k'])} – "
             f"{KH13(KH_FIRST['k'])}। ({NAME('anantara')} भी और {NAME('samanantara')} भी "
             f"{SADISA('ārammaṇa')} हैं।)")
    # sahajāta
    k = "sahajāta"
    H.append(f"######## *{NAME(k)}*")
    H.append(_kusala_block("k", k))
    H.append(_kusala_block("a", k))
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH(KH_FIRST['vk'], ' ' + AND_CSR)}; "
             f"{PATISANDHI} {KH(KH_FIRST['v'], ' ' + AND_KTR)}; {KH_VATTHU}; "
             f"{MB()}, {MBE(CSR + ', ' + KTR + ', ' + UPR)}; "
             f"{MB('एक ' + BAHIRA + ' महाभूत')}, {MBE(UPR)}; "
             f"{MB(AHARASAM + ' एक महाभूत')}, {MBE(UPR)}; "
             f"{MB(UTUSAM + ' एक महाभूत')}, {MBE(UPR)}; "
             f"{MB(ASANNASATTA + ' एक महाभूत')}, {MBE(KTR + ', ' + UPR)}। (1)")
    H.append(_mix_line("k", k))
    H.append(_mix_line("a", k))
    # aññamañña
    k = "aññamañña"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH(KH_FIRST['k'])}। (1)")
    H.append(f"{PATICCA(['a'], ['a'], ABL(k))} – {KH(KH_FIRST['a'])}। (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH(KH_FIRST['vk'])}; "
             f"{PATISANDHI} {KH(KH_FIRST['v'], ' और आधार')}; {KH_VATTHU}; {MB()}; "
             f"{EXT_CHAIN} {MB()}। (1)")
    # nissaya
    k = "nissaya"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH_FIRST['k']} पर निर्भर होकर…। "
             f"({NAME(k)} {SADISA('sahajāta')} है।)")
    # upanissaya
    k = "upanissaya"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH_FIRST['k']} पर निर्भर होकर…। "
             f"({NAME(k)} {SADISA('ārammaṇa')} है।)")
    # purejāta
    k = "purejāta"
    H.append(f"######## *{NAME(k)}*")
    VP = f"आधार पर {ABL(k)}।"
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH(KH_FIRST['k'])}। {VP} (1)")
    H.append(f"{PATICCA(['a'], ['a'], ABL(k))} – {KH(KH_FIRST['a'])}। {VP} (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH(KH_FIRST['vk'])}। {VP} (1)")
    # āsevana
    k = "āsevana"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH(KH_FIRST['k'])}। (1)")
    H.append(f"{PATICCA(['a'], ['a'], ABL(k))} – {KH(KH_FIRST['a'])}। (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH(KH_FIRST['ki'])}। (1)")
    # kamma
    k = "kamma"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH_FIRST['k']} पर निर्भर होकर… तीन।")
    H.append(f"{OBJ(['a'])} पर निर्भर होकर… तीन।")
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH_FIRST['vk']} पर निर्भर होकर… {PATISANDHI}… "
             f"{MB13()}… {MBE(CSR + ', ' + KTR + ', ' + UPR)}; {ASANNASATTA} {MB13()}… "
             f"{MBE(KTR + ', ' + UPR)}। (1)")
    H.append(_mix_line("k", k))
    H.append(_mix_line("a", k))
    # vipāka
    k = "vipāka"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH(KH_FIRST['v'], ' ' + AND_CSR)}; "
             f"{PATISANDHI} {KH(KH_FIRST['v'], ' ' + AND_KTR)}; {KH_VATTHU}; {MB13()}; "
             f"तीन महाभूतों पर निर्भर होकर एक महाभूत, दो महाभूतों पर निर्भर होकर दो महाभूत, "
             f"{MBE(CSR + ', ' + KTR + ', ' + UPR)}। (1)")
    # āhāra
    k = "āhāra"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH_FIRST['k']} पर निर्भर होकर… तीन।")
    H.append(f"{PATICCA(['a'], ['a'], ABL(k))} – {KH_FIRST['a']} पर निर्भर होकर… तीन।")
    H.append(f"{PATICCA(['ab'], ['ab'], ABL(k))} – {KH_FIRST['vk']} पर निर्भर होकर… {PATISANDHI}… "
             f"{MB13()}… {MBE(CSR + ', ' + KTR + ', ' + UPR)}; {AHARASAM} एक महाभूत पर निर्भर होकर… "
             f"{MBE(UPR)}।")
    H.append(f"{OBJ(['k', 'ab'])} पर निर्भर होकर…।")
    H.append(f"{PATICCA(['a', 'ab'], ['ab'], ABL(k))} – {KH_MB(T['a'])}।")
    # indriya
    k = "indriya"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH_FIRST['k']} पर निर्भर होकर… तीन।")
    H.append(f"{OBJ(['a'])} पर निर्भर होकर… तीन।")
    H.append(f"{OBJ(['ab'])} पर निर्भर होकर… {ASANNASATTA} एक महाभूत पर निर्भर होकर…। "
             f"({NAME(k)} {SADISA('kamma')} है।)")
    # jhāna-magga
    H.append(f"######## *{NAME('jhāna')} और {NAME('magga')}*")
    H.append(f"{OBJ(['k'])} पर निर्भर होकर {RES(['k'])} {ABL('jhāna')}… {ABL('magga')} {VERB(['k'])}। "
             f"({NAME('jhāna')} भी और {NAME('magga')} भी {SADISA('hetu')} हैं।)")
    # sampayutta
    k = "sampayutta"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH_FIRST['k']} पर निर्भर होकर…। "
             f"({NAME(k)} {SADISA('ārammaṇa')} है।)")
    # vippayutta
    k = "vippayutta"
    V = ABL(k)
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], V)} – {KH(KH_FIRST['k'])}; आधार पर {V}। "
             f"{PATICCA(['k'], ['ab'], V)} – {KHE(T['k'])} {CSR}। समूहों पर {V}। "
             f"{PATICCA(['k'], ['k', 'ab'], V)} – {KH13(KH_FIRST['k'])} {AND_CSR}; "
             f"तीन समूहों पर निर्भर होकर एक समूह {AND_CSR}, दो समूहों पर निर्भर होकर दो समूह {AND_CSR}। "
             f"समूह आधार पर {V}। {CSR} समूहों पर {V}। (3)")
    H.append(f"{PATICCA(['a'], ['a'], V)} – {KH(KH_FIRST['a'])}। आधार पर {V}। "
             f"{PATICCA(['a'], ['ab'], V)} – {KHE(T['a'])} {CSR}। समूहों पर {V}। "
             f"{PATICCA(['a'], ['a', 'ab'], V)} – {KH(KH_FIRST['a'], ' ' + AND_CSR)}। "
             f"समूह आधार पर {V}। {CSR} समूहों पर {V}। (3)")
    H.append(f"{PATICCA(['ab'], ['ab'], V)} – {KH(KH_FIRST['vk'], ' ' + AND_CSR)}। समूह आधार पर {V}। "
             f"{CSR} समूहों पर {V}। {PATISANDHI} {KH(KH_FIRST['v'], ' ' + AND_KTR)}। समूह आधार पर {V}। "
             f"{KTR} समूहों पर {V}। {KH_VATTHU}। समूह आधार पर {V}। आधार समूहों पर {V}। "
             f"{MB()}, {MBE(CSR + ', ' + KTR + ', ' + UPR)}। समूहों पर {V}। (1)")
    H.append(f"{_mix_line('k', k, cnt='')} समूहों पर {V}। (1)")
    H.append(f"{_mix_line('a', k, cnt='')} समूहों पर {V}। (1)")
    # atthi
    k = "atthi"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH13(KH_FIRST['k'])}।")
    H.append(f"(संक्षिप्त। {NAME(k)} {SADISA('sahajāta')} है।)")
    # natthi-vigata
    H.append(f"######## *{NAME('natthi')} और {NAME('vigata')}*")
    H.append(f"{OBJ(['k'])} पर निर्भर होकर {RES(['k'])} {ABL('natthi')}… {ABL('vigata')} {VERB(['k'])}। "
             f"({NAME('natthi')} भी और {NAME('vigata')} भी {SADISA('ārammaṇa')} हैं।)")
    # avigata
    k = "avigata"
    H.append(f"######## *{NAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], ABL(k))} – {KH13(KH_FIRST['k'])}। ({NAME(k)} {SADISA('sahajāta')} है)।")
    H.append("(इन तेईस कारणों का पाठ करते हुए विस्तार करना चाहिए।)")
    # saṅkhyāvāra
    P = (PALI_DIR / "1-01-kusalattika.md").read_text(encoding="utf-8").splitlines()

    def cl(phys):  # count line from physical line number (1-based), without the block ID
        return count_hi(ID_RX.sub("", P[phys - 1]))

    H += ["####### *" + PACCAYANULOMA + "*", "######## *" + VARA["saṅkhyā"] + "*", "######## *" + SUDDHA + "*",
          cl(131), "######## *" + GANANA_MULAKA("hetu") + "*", "######## *" + GROUP_HI(2) + "*", cl(137),
          "######## *" + GROUP_HI(3) + "*", cl(141), "######## *" + GROUP_HI(12) + "*", cl(145),
          "######## *" + GROUP_HI(22) + "*", cl(149), "######## *" + GROUP_HI(13) + "*", cl(153),
          "######## *" + GROUP_HI(22) + "*", cl(157), GANANA_MULAKA("hetu") + "।",
          "######## *" + DUKANI("ārammaṇa", plural=True).replace(NAME("ārammaṇa"), NAME("ārammaṇa") + " आदि") + "*",
          "(विषय-कारण पर टिके रहने पर हर जगह तीन ही प्रश्न हैं।)"]
    H += [cl(n) for n in range(164, 172)]
    H.append("######## *" + DUKANI("āsevana") + "*")
    H.append(_count_with_note(P[174], "(Āsevanamūlake vipākaṃ natthi.)",
                              f"({MULAKA('āsevana')} में {NAME('vipāka')} नहीं है।)"))
    H.append("######## *" + DUKANI("kamma") + "*")
    H.append(cl(179))
    H.append("######## *" + DUKANI("vipāka") + "*")
    H.append(_count_with_note(P[182], "(Vipākamūlake āsevanaṃ natthi.)",
                              f"({MULAKA('vipāka')} में {NAME('āsevana')} नहीं है।)"))
    H.append("######## *" + DUKANI("āhāra", plural=True).replace(NAME("āhāra"), NAME("āhāra") + " आदि") + "*")
    H += [cl(n) for n in range(187, 196)]
    H.append("######## *" + DUKANI("avigata") + "*")
    H.append(cl(199))
    H.append("(एक-एक कारण को शुरुआत बनाकर पाठ करते हुए गिनना चाहिए।)")
    H.append(ANULOMA + "।")
    return H


def _count_with_note(pali_line, note_pali, note_hi):
    body = ID_RX.sub("", pali_line).replace(" " + note_pali, "")
    return count_hi(body) + " " + note_hi


# =====================================================================================
# 11. Content: sample 3 (paṭiccavāra, paccanīya: vibhaṅga)
# =====================================================================================
def build_s3():
    H = ["####### *" + PACCAYAPACCANIYA + "*", "######## *" + VARA["vibhaṅga"] + "*",
         f"######## *{PACCANIYA} – {NNAME('hetu')}*"]
    k = "hetu"
    H.append(f"{PATICCA(['a'], ['a'], NABL(k))} – {KHE_VU()} {MOHA_VU}। (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], NABL(k))} – {KH(KH_FIRST['ahetuka_vk'], ' ' + AND_CSR)}; "
             f"{AHETUKA_PATISANDHI} {KH(KH_FIRST['v'], ' ' + AND_KTR)}; {KH_VATTHU}; "
             f"{MB()}, {MBE(CSR + ', ' + KTR + ', ' + UPR)}; {EXT_CHAIN} {MB()}, {MBE(KTR + ', ' + UPR)}। (1)")
    # na-ārammaṇa
    k = "ārammaṇa"
    N = NABL(k)
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['k'], ['ab'], N)} – {KHE(T['k'])} {CSR}। (1)")
    H.append(f"{PATICCA(['a'], ['ab'], N)} – {KHE(T['a'])} {CSR}। (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], N)} – {KHE(VK_PL)} {CSR}; {PATISANDHI} {KHE(VIPAKA_ABY)} {KTR}; "
             f"समूहों पर निर्भर होकर आधार; {MB()}, {MBE(CSR + ', ' + KTR + ', ' + UPR)}; "
             f"{EXT_CHAIN} {MB()}, {MBE(KTR + ', ' + UPR)}। (1)")
    H.append(_mix_line("k", k, neg=True))
    H.append(_mix_line("a", k, neg=True))
    # na-adhipati
    k = "adhipati"
    N = NABL(k)
    H.append(f"######## *{NNAME(k)}*")
    H.append(_kusala_block("k", k, neg=True))
    H.append(_kusala_block("a", k, neg=True))
    H.append(f"{PATICCA(['ab'], ['ab'], N)} – {KH(KH_FIRST['vk'], ' ' + AND_CSR)}; "
             f"{PATISANDHI} {KH(KH_FIRST['v'], ' ' + AND_KTR)}। {KH_VATTHU}। "
             f"{MB()}, {MBE(CSR + ', ' + KTR + ', ' + UPR)}; {EXT_CHAIN} {MB()}, {MBE(KTR + ', ' + UPR)}। (1)")
    H.append(_mix_line("k", k, neg=True))
    H.append(_mix_line("a", k, neg=True))
    # na-anantara / na-samanantara
    H.append(f"######## *{NNAME('anantara')} और {NNAME('samanantara')}*")
    H.append(f"{OBJ(['k'])} पर निर्भर होकर {RES(['ab'])} {NABL('anantara')}… {NABL('samanantara')} "
             f"{VERB(['ab'])} – {KHE(T['k'])} {CSR}। ({NNAME('anantara')} भी और {NNAME('samanantara')} भी "
             f"{SADISA('ārammaṇa', neg=True)} हैं।)")
    # na-aññamañña
    k = "aññamañña"
    N = NABL(k)
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['k'], ['ab'], N)} – {KHE(T['k'])} {CSR}। (1)")
    H.append(f"{PATICCA(['a'], ['ab'], N)} – {KHE(T['a'])} {CSR}। (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], N)} – {KHE(VK_PL)} {CSR}; {PATISANDHI} {KHE(VIPAKA_ABY)} {KTR}; "
             f"{MBE(CSR + ', ' + KTR + ', ' + UPR)}; {MBE(UPR, BAHIRA)}; {MBE(UPR, AHARASAM)}; "
             f"{MBE(UPR, UTUSAM)}; {MBE(KTR + ', ' + UPR, ASANNASATTA)}। (1)")
    H.append(_mix_line("k", k, neg=True))
    H.append(_mix_line("a", k, neg=True))
    # na-upanissaya
    k = "upanissaya"
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['k'], ['ab'], NABL(k))} – {KHE(T['k'])} {CSR}। "
             f"({NNAME(k)} {SADISA('ārammaṇa', neg=True)} है।)")
    # na-purejāta
    k = "purejāta"
    N = NABL(k)
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], N)} – {KH(KH_FIRST['arupe_k'])}। "
             f"{PATICCA(['k'], ['ab'], N)} – {KHE(T['k'])} {CSR}। (2)")
    H.append(f"{PATICCA(['a'], ['a'], N)} – {KH(KH_FIRST['arupe_a'])}। "
             f"{PATICCA(['a'], ['ab'], N)} – {KHE(T['a'])} {CSR}। (2)")
    H.append(f"{PATICCA(['ab'], ['ab'], N)} – {KH(KH_FIRST['arupe_vk'])}, {KHE(VK_PL)} {CSR}; "
             f"{PATISANDHI} {KH(KH_FIRST['v'], ' ' + AND_KTR)}। {KH_VATTHU}। "
             f"{MB()}, {MBE(CSR + ', ' + KTR + ', ' + UPR)}; {EXT_CHAIN} {MB()}, {MBE(KTR + ', ' + UPR)}। (1)")
    H.append(_mix_line("k", k, neg=True))
    H.append(_mix_line("a", k, neg=True))
    # na-pacchājāta / na-āsevana
    H.append(f"######## *{NNAME('pacchājāta')} और {NNAME('āsevana')}*")
    H.append(f"{PATICCA(['k'], ['k'], NABL('pacchājāta'))} – {KH_FIRST['k']} पर निर्भर होकर…।")
    H.append(f"{PATICCA(['k'], ['k'], NABL('āsevana'))} – {KH_FIRST['k']} पर निर्भर होकर…। "
             f"({NNAME('pacchājāta')} भी और {NNAME('āsevana')} भी {SADISA('adhipati', neg=True)} हैं।)")
    # na-kamma
    k = "kamma"
    N = NABL(k)
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], N)} – {KHE(T['k'])} हितकर {CETANA}। (1)")
    H.append(f"{PATICCA(['a'], ['a'], N)} – {KHE(T['a'])} हानिकर {CETANA}। (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], N)} – {KHE(KIRIYA_ABY)} {KIRIYA_ABY} {CETANA}; "
             f"{BAHIRA}… {AHARASAM}… {MB(UTUSAM + ' एक महाभूत')}, {MBE(UPR)}। (1)")
    # na-vipāka
    k = "vipāka"
    N = NABL(k)
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], N)} – {KH_FIRST['k']} पर निर्भर होकर… तीन।")
    H.append(f"{PATICCA(['a'], ['a'], N)}… तीन।")
    H.append(f"{PATICCA(['ab'], ['ab'], N)} – {KH(KH_FIRST['ki'], ' ' + AND_CSR)}; {MB13()}… "
             f"{MBE(CSR + ', ' + UPR)}; {EXT_CHAIN} {MB13()}… {MBE(KTR + ', ' + UPR)}।")
    H.append(_mix_line("k", k, cnt="", neg=True))
    H.append(_mix_line("a", k, cnt="", neg=True))
    # na-āhāra
    k = "āhāra"
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['ab'], ['ab'], NABL(k))} – {BAHIRA}… {UTUSAM}… {ASANNASATTA} {MB13()}… "
             f"{MBE(KTR + ', ' + UPR)}। (1)")
    # na-indriya
    k = "indriya"
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['ab'], ['ab'], NABL(k))} – {BAHIRA}… {AHARASAM}… {MB13(UTUSAM + ' एक महाभूत')}… "
             f"{MBE(UPR)}; {MBE(RUPAJIVITINDRIYA, ASANNASATTA)}। (1)")
    # na-jhāna
    k = "jhāna"
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['ab'], ['ab'], NABL(k))} – {KH13(KH_FIRST['pancavinnana'])}; "
             f"तीन समूहों पर निर्भर होकर एक समूह, दो समूहों पर निर्भर होकर दो समूह; "
             f"{EXT_CHAIN} {MB13()}… {MBE(KTR + ', ' + UPR)}। (1)")
    # na-magga
    k = "magga"
    N = NABL(k)
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['ab'], ['ab'], N)} – {KH(KH_FIRST['ahetuka_vk'], ' ' + AND_CSR)}; "
             f"{AHETUKA_PATISANDHI} {KH(KH_FIRST['v'], ' ' + AND_KTR)}। {KH_VATTHU}। {MB()}; "
             f"{MBE(CSR + ', ' + KTR + ', ' + UPR)}; {EXT_CHAIN} {MB13()}… {MBE(KTR + ', ' + UPR)}। (1)")
    # na-sampayutta
    k = "sampayutta"
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['k'], ['ab'], NABL(k))} – {KHE(T['k'])} {CSR}। ({SADISA('ārammaṇa', neg=True)} है।)")
    # na-vippayutta
    k = "vippayutta"
    N = NABL(k)
    H.append(f"######## *{NNAME(k)}*")
    H.append(f"{PATICCA(['k'], ['k'], N)} – {KH(KH_FIRST['arupe_k'])}। (1)")
    H.append(f"{PATICCA(['a'], ['a'], N)} – {KH(KH_FIRST['arupe_a'])}। (1)")
    H.append(f"{PATICCA(['ab'], ['ab'], N)} – {KH(KH_FIRST['arupe_vk'])}; {EXT_CHAIN} {MB13()}… "
             f"{MBE(KTR + ', ' + UPR)}। (1)")
    # no-natthi / no-vigata
    H.append(f"######## *{NNAME('natthi')} और {NNAME('vigata')}*")
    H.append(f"{OBJ(['k'])} पर निर्भर होकर {RES(['ab'])} {NABL('natthi')}… {NABL('vigata')} {VERB(['ab'])} – "
             f"{KHE(T['k'])} {CSR}। ({SADISA('ārammaṇa', neg=True)} है।)")
    return H


def KHE_VU():
    return f"{KHE_VU_TEXT}"


KHE_VU_TEXT = f"{KHANDHE_VU} पर निर्भर होकर"


# =====================================================================================
# 12. Content: sample 4 (pañhāvāra: hetu, ārammaṇa, adhipati)
# =====================================================================================
def _assada(obj, pron="उस"):
    """X assādeti abhinandati -> "X का रस लेता है, उसमें आनंद लेता है" (pronouns written joined: उसका)."""
    sep = "" if obj in ("उस", "उन") else " "
    return f"{obj}{sep}{ASSADA}, {pron}{ABHINANDA}"


def build_s4():
    A = INS("ārammaṇa")
    D = INS("adhipati")
    Hh = INS("hetu")
    KNOW3 = f"{CETOPARIYA_OBL}, {PUBBENIVASA_OBL}, {YATHAKAMMUPAGA_OBL}"
    H = ["####### *" + VARA["pañhā"] + "*", "####### *" + PACCAYANULOMA + "*",
         "######## *" + VARA["vibhaṅga"] + "*", "######## *" + NAME("hetu") + "*"]
    for x in ("k", "a"):
        H.append(f"{PANHA([x], [x], 'hetu')} – {T[x]} मूल {SAMPAYUTTAKA_KH_OBL} के लिए {Hh} होते हैं। "
                 f"{PANHA([x], ['ab'], 'hetu')} – {T[x]} मूल {CSR_OBL} के लिए {Hh} होते हैं। "
                 f"{PANHA([x], [x, 'ab'], 'hetu')} – {T[x]} मूल {SAMPAYUTTAKA_KH_OBL} के लिए और {CSR_OBL} के लिए "
                 f"{Hh} होते हैं। (3)")
    H.append(f"{PANHA(['ab'], ['ab'], 'hetu')} – {VK_PL} मूल {SAMPAYUTTAKA_KH_OBL} के लिए और {CSR_OBL} के लिए "
             f"{Hh} होते हैं; {PATISANDHI} {VIPAKA_ABY} मूल {SAMPAYUTTAKA_KH_OBL} के लिए और {KTR_OBL} के लिए "
             f"{Hh} होते हैं। (1)")
    # ārammaṇa
    H.append("######## *" + NAME("ārammaṇa") + "*")
    H.append(f"{PANHA(['k'], ['k'], 'ārammaṇa')} – {DANA3} उस पर {REVIEW_SG}, {SUCINNA} पर {REVIEW_SG}, "
             f"ध्यान से उठकर ध्यान पर {REVIEW_SG}, {SEKKHA} {GOTRABHU} पर {REVIEW_PL}, {VODANA} पर {REVIEW_PL}, "
             f"{SEKKHA} मार्ग से उठकर मार्ग पर {REVIEW_PL}, {SEKKHA_VA_PUTHUJJANA} हितकर को {ANICCA3} {VIPASSANTI}, "
             f"{CETOPARIYENA} हितकर मन से युक्त व्यक्ति के मन को जानते हैं। "
             f"{ARUPA_OBL('ākāsānañca')} का हितकर मन {ARUPA_OBL('viññāṇañca')} के हितकर मन के लिए {A} होता है। "
             f"{ARUPA_OBL('ākiñcañña')} का हितकर मन {ARUPA_OBL('nevasaññānāsañña')} के हितकर मन के लिए {A} होता है। "
             f"हितकर समूह {IDDHIVIDHA_OBL}, {KNOW3} और {ANAGATAMSA_OBL} के लिए {A} होते हैं। (1)")
    H.append(f"{PANHA(['k'], ['a'], 'ārammaṇa')} – {DANA3} {_assada('उस')}; उसे विषय बनाकर {AROSE5}। "
             f"{_assada(SUCINNA, 'उन')}; उसे विषय बनाकर {AROSE5}। "
             f"ध्यान से उठकर {_assada('ध्यान')}; उसे विषय बनाकर {AROSE4}। "
             f"ध्यान के छूट जाने पर ग्लानि से भरे व्यक्ति में उदासी उत्पन्न होती है। (2)")
    H.append(f"{PANHA(['k'], ['ab'], 'ārammaṇa')} – {ARAHA} मार्ग से उठकर मार्ग पर {REVIEW_SG}; "
             f"{SUCINNA} पर {REVIEW_SG}; हितकर को {ANICCA3} {VIPASSATI}; "
             f"{CETOPARIYENA} हितकर मन से युक्त व्यक्ति के मन को जानता है। "
             f"{SEKKHA_VA_PUTHUJJANA} हितकर को {ANICCA3} {VIPASSANTI}, हितकर के समाप्त होने पर {TADARAMMANA}। "
             f"{_assada('हितकर')}; उसे विषय बनाकर {AROSE5}, हानिकर के समाप्त होने पर {TADARAMMANA}। "
             f"{ARUPA_OBL('ākāsānañca')} का हितकर मन {ARUPA_OBL('viññāṇañca')} के कर्म के फल रूपी मन के लिए और "
             f"केवल क्रिया रूपी मन के लिए {A} होता है। "
             f"{ARUPA_OBL('ākiñcañña')} का हितकर मन {ARUPA_OBL('nevasaññānāsañña')} के कर्म के फल रूपी मन के लिए "
             f"और केवल क्रिया रूपी मन के लिए {A} होता है। "
             f"हितकर समूह {KNOW3} और {ANAGATAMSA_OBL} के लिए तथा {AVAJJANA_FOR} {A} होते हैं। (3)")
    H.append(f"{PANHA(['a'], ['a'], 'ārammaṇa')} – {_assada('राग')}; उसे विषय बनाकर {AROSE5}। "
             f"{_assada('दृष्टि')}; उसे विषय बनाकर {AROSE5}। "
             f"संशय को विषय बनाकर संशय उत्पन्न होता है, दृष्टि उत्पन्न होती है, बेचैनी उत्पन्न होती है, "
             f"उदासी उत्पन्न होती है। "
             f"बेचैनी को विषय बनाकर बेचैनी उत्पन्न होती है, दृष्टि उत्पन्न होती है, संशय उत्पन्न होता है, "
             f"उदासी उत्पन्न होती है। "
             f"उदासी को विषय बनाकर उदासी उत्पन्न होती है, दृष्टि उत्पन्न होती है, संशय उत्पन्न होता है, "
             f"बेचैनी उत्पन्न होती है। (1)")
    H.append(f"{PANHA(['a'], ['k'], 'ārammaṇa')} – {SEKKHA} छोड़े जा चुके मन के क्लेशों "
             f"[वर्तनी-भेद (Syā.): pahīnakilese] पर {REVIEW_PL}, दबाए जा चुके मन के क्लेशों "
             f"[वर्तनी-भेद (Syā.): vikkhambhitakilese] पर {REVIEW_PL}, पहले बार-बार उठे मन के क्लेशों को जानते हैं, "
             f"{SEKKHA_VA_PUTHUJJANA} हानिकर को {ANICCA3} {VIPASSANTI}, "
             f"{CETOPARIYENA} हानिकर मन से युक्त व्यक्ति के मन को जानते हैं। "
             f"हानिकर समूह {KNOW3} और {ANAGATAMSA_OBL} के लिए {A} होते हैं। (2)")
    H.append(f"{PANHA(['a'], ['ab'], 'ārammaṇa')} – {ARAHA} छोड़े जा चुके मन के क्लेशों पर {REVIEW_SG}, "
             f"पहले बार-बार उठे मन के क्लेशों को जानता है, हानिकर को {ANICCA3} {VIPASSATI}, "
             f"{CETOPARIYENA} हानिकर मन से युक्त व्यक्ति के मन को जानता है, "
             f"{SEKKHA_VA_PUTHUJJANA} हानिकर को {ANICCA3} {VIPASSANTI}, हितकर के समाप्त होने पर {TADARAMMANA}। "
             f"{_assada('हानिकर')}; उसे विषय बनाकर {AROSE5}। हानिकर के समाप्त होने पर {TADARAMMANA}। "
             f"हानिकर समूह {KNOW3} और {ANAGATAMSA_OBL} के लिए तथा {AVAJJANA_FOR} {A} होते हैं। (3)")
    H.append(f"{PANHA(['ab'], ['ab'], 'ārammaṇa')} – {ARAHA} फल पर {REVIEW_SG}, निर्वाण पर {REVIEW_SG}। "
             f"निर्वाण फल के लिए और {AVAJJANA_FOR} {A} होता है। "
             f"{ARAHA} आँख को {ANICCA3} {VIPASSATI}। {SENSE_CHAIN('को')} {VK_PL} समूहों को {ANICCA3} {VIPASSATI}, "
             f"दिव्य आँख से दृश्य रूप देखता है, दिव्य कान के तत्व से ध्वनि सुनता है, "
             f"{CETOPARIYENA} {VK_SG} मन से युक्त व्यक्ति के मन को जानता है। "
             f"{ARUPA_OBL('ākāsānañca')} का केवल क्रिया रूपी मन {ARUPA_OBL('viññāṇañca')} के केवल क्रिया रूपी मन के लिए "
             f"{A} होता है। {ARUPA_OBL('ākiñcañña')} का केवल क्रिया रूपी मन "
             f"{ARUPA_OBL('nevasaññānāsañña')} के केवल क्रिया रूपी मन के लिए {A} होता है। "
             f"{AYA_OBJ('rūpa')} {VINNANA('cakkhu')} के लिए {A} होता है। "
             f"{AYA_OBJ('sadda')} {VINNANA('sota')} के लिए… {AYA_OBJ('gandha')} {VINNANA('ghāna')} के लिए… "
             f"{AYA_OBJ('rasa')} {VINNANA('jivhā')} के लिए… {AYA_OBJ('phoṭṭhabba')} {VINNANA('kāya')} के लिए "
             f"{A} होता है। {T['ab']} समूह {IDDHIVIDHA_OBL}, {CETOPARIYA_OBL}, {PUBBENIVASA_OBL} और "
             f"{ANAGATAMSA_OBL} के लिए तथा {AVAJJANA_FOR} {A} होते हैं। (1)")
    H.append(f"{PANHA(['ab'], ['k'], 'ārammaṇa')} – {SEKKHA} फल पर {REVIEW_PL}, निर्वाण पर {REVIEW_PL}। "
             f"निर्वाण {GOTRABHU} के लिए, {VODANA} के लिए, मार्ग के लिए {A} होता है। "
             f"{SEKKHA_VA_PUTHUJJANA} आँख को {ANICCA3} {VIPASSANTI}। {SENSE_CHAIN('को')} {VK_PL} समूहों को "
             f"{ANICCA3} {VIPASSANTI}, दिव्य आँख से दृश्य रूप देखते हैं, दिव्य कान के तत्व से ध्वनि सुनते हैं, "
             f"{CETOPARIYENA} {VK_SG} मन से युक्त व्यक्ति के मन को जानते हैं। "
             f"{T['ab']} समूह {IDDHIVIDHA_OBL}, {CETOPARIYA_OBL}, {PUBBENIVASA_OBL} और {ANAGATAMSA_OBL} के लिए "
             f"{A} होते हैं।")
    H.append(f"{PANHA(['ab'], ['a'], 'ārammaṇa')} – {_assada('आँख')}; उसे विषय बनाकर {AROSE5}। "
             f"{SENSE_CHAIN('का')} {VK_PL} समूहों {ASSADA}, उनमें आनंद लेता है; उसे विषय बनाकर {AROSE5}। (3)")
    # adhipati
    H.append("######## *" + NAME("adhipati") + "*")
    AS = f"{ARAMMANADHIPATI}, {SAHAJATADHIPATI}।"
    H.append(f"{PANHA(['k'], ['k'], 'adhipati')}। {AS} {ARAMMANADHIPATI} – {DANA3}, उसे महत्व देकर उस पर "
             f"{REVIEW_SG}, {SUCINNA} को महत्व देकर उन पर {REVIEW_SG}, ध्यान से उठकर ध्यान को महत्व देकर उस पर "
             f"{REVIEW_SG}। {SEKKHA} {GOTRABHU} को महत्व देकर उस पर {REVIEW_PL}, {VODANA} को महत्व देकर उस पर "
             f"{REVIEW_PL}। {SEKKHA} मार्ग से उठकर मार्ग को महत्व देकर उस पर {REVIEW_PL}। "
             f"{SAHAJATADHIPATI} – हितकर प्रधानता {SAMPAYUTTAKA_KH_OBL} के लिए {D} होती है। (1)")
    H.append(f"{PANHA(['k'], ['a'], 'adhipati')}। {ARAMMANADHIPATI} – {DANA3}, उसे महत्व देकर "
             f"{_assada('उस')}; उसे महत्व देकर {AROSE2}, {SUCINNA} को महत्व देकर {_assada('उन', 'उन')}; "
             f"उसे महत्व देकर {AROSE2}। ध्यान से उठकर ध्यान को महत्व देकर {_assada('उस')}; "
             f"उसे महत्व देकर {AROSE2}।")
    H.append(f"{PANHA(['k'], ['ab'], 'adhipati')}। {AS} {ARAMMANADHIPATI} – {ARAHA} मार्ग से उठकर मार्ग को महत्व "
             f"देकर उस पर {REVIEW_SG}। {SAHAJATADHIPATI} – हितकर प्रधानता {CSR_OBL} के लिए {D} होती है। (3)")
    H.append(f"{PANHA(['k'], ['k', 'ab'], 'adhipati')}। {SAHAJATADHIPATI} – हितकर प्रधानता {SAMPAYUTTAKA_KH_OBL} "
             f"के लिए और {CSR_OBL} के लिए {D} होती है। (4)")
    H.append(f"{PANHA(['a'], ['a'], 'adhipati')}। {AS} {ARAMMANADHIPATI} – राग को महत्व देकर {_assada('उस')}; "
             f"उसे महत्व देकर {AROSE2}। दृष्टि को महत्व देकर {_assada('उस')}; उसे महत्व देकर {AROSE2}। "
             f"{SAHAJATADHIPATI} – हानिकर प्रधानता {SAMPAYUTTAKA_KH_OBL} के लिए {D} होती है। (1)")
    H.append(f"{PANHA(['a'], ['ab'], 'adhipati')}। {SAHAJATADHIPATI} – हानिकर प्रधानता {CSR_OBL} के लिए "
             f"{D} होती है। (2)")
    H.append(f"{PANHA(['a'], ['a', 'ab'], 'adhipati')}। {SAHAJATADHIPATI} – हानिकर प्रधानता "
             f"{SAMPAYUTTAKA_KH_OBL} के लिए और {CSR_OBL} के लिए {D} होती है। (3)")
    H.append(f"{PANHA(['ab'], ['ab'], 'adhipati')}। {AS} {ARAMMANADHIPATI} – {ARAHA} फल को महत्व देकर उस पर "
             f"{REVIEW_SG}, निर्वाण को महत्व देकर उस पर {REVIEW_SG}। निर्वाण फल के लिए {D} होता है। "
             f"{SAHAJATADHIPATI} – {VK_PL} प्रधानता {SAMPAYUTTAKA_KH_OBL} के लिए और {CSR_OBL} के लिए "
             f"{D} होती है। (1)")
    H.append(f"{PANHA(['ab'], ['k'], 'adhipati')}। {ARAMMANADHIPATI} – {SEKKHA} फल को महत्व देकर उस पर "
             f"{REVIEW_PL}, निर्वाण को महत्व देकर उस पर {REVIEW_PL}। निर्वाण {GOTRABHU} के लिए, {VODANA} के लिए, "
             f"मार्ग के लिए {D} होता है। (2)")
    H.append(f"{PANHA(['ab'], ['a'], 'adhipati')}। {ARAMMANADHIPATI} – आँख को महत्व देकर {_assada('उस')}; "
             f"उसे महत्व देकर {AROSE2}। {SENSE_CHAIN('को')} {VK_PL} समूहों को महत्व देकर "
             f"{_assada('उन', 'उन')}; उसे महत्व देकर {AROSE2}। (3)")
    return H


# =====================================================================================
# 13. Write and check
# =====================================================================================
SAMPLES = {  # name: (pali file, first, last non-empty line, builder)
    "s2-paticca-anuloma": ("1-01-kusalattika.md", 1, 128, build_s2),
    "s3-paticca-paccaniya": ("1-01-kusalattika.md", 129, 190, build_s3),
    "s4-panha": ("1-01-kusalattika.md", 1235, 1262, build_s4),
}


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def outputs():
    """Return {path: text} for every output (Pāli excerpts and Hindi)."""
    res = {}
    pre = (PALI_DIR / "preamble.md").read_text(encoding="utf-8")
    res[HI_DIR / "preamble.md"] = assemble(pre, build_preamble())
    p00 = (PALI_DIR / "1-00-paccaya.md").read_text(encoding="utf-8")
    res[HI_DIR / "1-00-paccaya.md"] = assemble(p00, build_1_00())
    for name, (fname, a, b, fn) in SAMPLES.items():
        ptxt = excerpt(fname, a, b)
        res[SAMPLE_DIR / f"{name}-pali.md"] = ptxt
        res[SAMPLE_DIR / f"{name}.md"] = assemble(ptxt, fn())
    return res


LATIN_RX = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")


def check(pairs):
    """Brace-normalised copy of verify_hi.py + Latin/dash/blank checks.
    pi-7 Pāli marks variants with {…}; the Hindi uses «[…]» as the style requires, so '{' is counted
    as '[' on the Pāli side."""
    bad = 0
    for p, h in pairs:
        pt = p.read_text(encoding="utf-8").replace("{", "[").replace("}", "]")
        ht = h.read_text(encoding="utf-8")
        errs = []
        pl, hl = nonempty(pt), nonempty(ht)
        if len(pl) != len(hl):
            errs.append(f"non-empty lines {len(pl)} vs {len(hl)}")
        for i, (a, b) in enumerate(zip(pl, hl), 1):
            da = a.count("–") + a.count("—")
            db = b.count("–") + b.count("—")
            if da != db:
                errs.append(f"line {i}: dash {da} vs {db}")
            if a.count("[") != b.count("["):
                errs.append(f"line {i}: '[' {a.count('[')} vs {b.count('[')}")
            ma, mb = ID_RX.search(a), ID_RX.search(b)
            if (ma and ma.group(1)) != (mb and mb.group(1)):
                errs.append(f"line {i}: id differs")
            if (len(a) - len(a.lstrip("#"))) != (len(b) - len(b.lstrip("#"))):
                errs.append(f"line {i}: heading level")
            body = ID_RX.sub("", re.sub(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]", "", b))
            if LATIN_RX.search(body):
                errs.append(f"line {i}: Latin left: {LATIN_RX.search(body).group(0)}")
            if "—" in b or ":-" in b:
                errs.append(f"line {i}: em dash or ':-'")
        if "\r" in ht or "\n\n\n" in ht or not ht.endswith("\n") or ht.endswith("\n\n"):
            errs.append("CR / double blank / bad ending")
        if [l == "" for l in pt.splitlines()] != [l == "" for l in ht.splitlines()]:
            errs.append("blank-line layout differs")
        print(f"{h.name}: {len(hl)} lines", "OK" if not errs else "ERRORS")
        for e in errs[:15]:
            print("   ", e)
        bad += bool(errs)
    return bad


def main():
    outs = outputs()
    if "--check" not in sys.argv:
        for path, text in outs.items():
            _write(path, text)
            print("wrote", path)
    pairs = [(PALI_DIR / "preamble.md", HI_DIR / "preamble.md"),
             (PALI_DIR / "1-00-paccaya.md", HI_DIR / "1-00-paccaya.md")]
    pairs += [(SAMPLE_DIR / f"{n}-pali.md", SAMPLE_DIR / f"{n}.md") for n in SAMPLES]
    sys.exit(1 if check(pairs) else 0)


if __name__ == "__main__":
    main()
