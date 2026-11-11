"""Build the Hindi plain zero-shot of pi-1 part 4-01 (Nikkhepakaṇḍaṃ: summary of the triads,
the root group, the short intermediate pairs, the taint, fetter and tie groups).

usage: python -I -X utf8 build_4-01_hi.py
Matrix item wording comes from build_matika_hi (BARE, QUESTION, ANSWER); synonym strings and
factor names from build_ch2_01_sample_hi. Every recurring formula is a fixed constant below,
so every repeat is byte-identical. Importing this module does not write anything.
Structure mirrors 0-INBOX/temp/pipeline/pi-1-en/build_4-01_4-03.py (build_401).
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_hi as M          # noqa: E402  (import does not write anything)
import build_ch2_01_sample_hi as C   # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "4-01-nikkhepakandam.md"
OUT = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters" / "4-01-nikkhepakandam.md"

D = C.DASH          # "–", only where the Pāli has one
DANDA = M.DANDA     # "।"
N = C.NAMES
V = C.V             # variant bracket helper: V("s"|"p", sigla, pali)


# ---------------------------------------------------------------- matrix items -------
def item(mid, l):
    """Bare matrix item name, e.g. item('1-1', 'क') -> 'हितकर परिघटनाएँ'."""
    return M.BARE[(f"1-M{mid}", l)]


def obl(name):
    """Oblique plural of a '… परिघटनाएँ' item (object of 'को विषय बनाकर')."""
    assert name.endswith("परिघटनाएँ"), name
    return name[:-len("परिघटनाएँ")] + "परिघटनाओं"


def Q(mid, l):
    return M.QUESTION(item(mid, l))


def A(mid, l):
    return M.ANSWER(item(mid, l))


def QA(mid, l, body):
    """Katame dhammā X? <body> – ime dhammā X."""
    return f"{Q(mid, l)} {body} {D} {A(mid, l)}"


# ---------------------------------------------------------------- headings -----------
H_CH4 = "### सारांश का अध्याय"
H_TIKA = "#### तीन-तीन के वर्गीकरणों का सारांश"
H_DUKA = "#### दो-दो के वर्गीकरणों का सारांश"
END_TIKA = "तीन-तीन के वर्गीकरण।"                 # Tikaṃ.
END_BHANA1 = "सारांश के अध्याय का पहला पाठ-खंड।"   # Nikkhepakaṇḍe paṭhamabhāṇavāro.

# ---------------------------------------------------------------- fixed strings ------
# spheres: kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā
SPH = {"k": "इंद्रिय-सुखों के लोक से संबंधित", "r": "सूक्ष्म भौतिक लोक से संबंधित",
       "a": "अभौतिक लोक से संबंधित"}
APAR = {"m": "अस्तित्व के लोकों में न समाए हुए", "f": "अस्तित्व के लोकों में न समाई हुई"}


def whether(keys, g="m", subj="वे", verb="हों"):
    """'kāmāvacarā, rūpāvacarā, …' after a noun: 'चाहे वे X, Y या Z हों'."""
    parts = [SPH[k] if k != "p" else APAR[g] for k in keys]
    if len(parts) == 1:
        return f"जो {parts[0]} {'है' if verb == 'हो' else 'हैं'}"
    return f"चाहे {subj} " + ", ".join(parts[:-1]) + " या " + parts[-1] + f" {verb}"


W4M = whether("krap", "m")        # after कर्म-फल (m.)
W4F = whether("krap", "f")        # after परिघटनाएँ (f.)
W3 = whether("kra")               # no gendered word

KH4 = "अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह"
KH_PE = "अनुभूति का समूह … चेतना का समूह"                     # vedanākkhandho…pe… viññāṇakkhandho
KH5 = "भौतिक रूप का समूह, " + KH4
KH_R_PE = "भौतिक रूप का समूह … चेतना का समूह"                 # rūpakkhandho…pe… viññāṇakkhandho
TAM = "उनसे जुड़ा"                                             # taṃsampayutto
TS4 = f"{TAM} {KH4}"
TS_PE = f"{TAM} {KH_PE}"
TS3 = f"{TAM} पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह"
KAMMA = "उनसे उत्पन्न शारीरिक कर्म, वाणी का कर्म, मानसिक कर्म"   # taṃsamuṭṭhānaṃ kāyakammaṃ …
TADEK = "और उनके साथ रहने वाले मन के क्लेश"                     # tadekaṭṭhā ca kilesā
TADEK_LDM = "उनके साथ रहने वाला लोभ, द्वेष, मोह"                # Tadekaṭṭho lobho, doso, moho
ROOTS_K = f"तीन हितकर मूल {D} {N['alobho']}, {N['adoso']}, {N['amoho']}"
ROOTS_A = f"तीन हानिकर मूल {D} लोभ, द्वेष, मोह"
KIRIYA_BARE = ("वे परिघटनाएँ जो केवल क्रिया रूपी हैं, न हितकर हैं, न हानिकर, "
               "और न ही कर्म-फल रूपी")                           # (ye ca) dhammā kiriyā neva kusalā …
KIRIYA = "और " + KIRIYA_BARE                                    # ye ca … inside a list; bare at ^1-993's start
RUPA_ASANKH = "सारा भौतिक रूप और अनिर्मित तत्व"                  # sabbañca rūpaṃ, asaṅkhatā ca dhātu
ASANKHATA = "अनिर्मित तत्व"                                     # asaṅkhatā dhātu
MAGGA = "अस्तित्व के लोकों में न समाए हुए मार्ग, मार्गों के फल और अनिर्मित तत्व"
PATHS4 = "अस्तित्व के लोकों में न समाए हुए चार मार्ग"               # Cattāro maggā apariyāpannā
VIPAKA = "हितकर और हानिकर परिघटनाओं के कर्म-फल"                  # Kusalākusalānaṃ dhammānaṃ vipākā
KUSAKU = "हितकर और हानिकर परिघटनाएँ"                             # kusalākusalā dhammā
KUSAB = "हितकर और नैतिक रूप से अनिर्धारित परिघटनाएँ"             # kusalābyākatā dhammā
ALL3 = "हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ"       # kusalākusalābyākatā dhammā
SAS = "मन के मैलों का विषय बनने वाली"                            # sāsavā (before a plural noun)
TE_THAPETVA = "उन परिघटनाओं को छोड़कर बाकी " + ALL3              # Te dhamme ṭhapetvā avasesā …
RUPA_DHAY = ("जो भौतिक रूप दिखाई न देने वाला, टकराव से रहित और मन के विषयों के "
             "इंद्रिय-क्षेत्र में समाया हुआ है")                   # yañca rūpaṃ anidassanaṃ appaṭighaṃ …


def CITTACET(obj):
    """X ārabbha ye uppajjanti cittacetasikā dhammā"""
    return f"{obj} को विषय बनाकर जो मन और मन की सहचर परिघटनाएँ उत्पन्न होती हैं"


KATATTA = "जो भौतिक रूप कर्म किए जाने के कारण बना है"              # yañca rūpaṃ kammassa katattā
NA_KATATTA = "जो भौतिक रूप कर्म किए जाने के कारण नहीं बना है"
KATATTA_FUT = "जो भौतिक रूप कर्म किए जाने के कारण उत्पन्न होगा"

BASE = {"cakkh": "आँख का इंद्रिय-क्षेत्र", "sot": "कान का इंद्रिय-क्षेत्र", "ghān": "नाक का इंद्रिय-क्षेत्र",
        "jivh": "जीभ का इंद्रिय-क्षेत्र", "kāy": "शरीर का इंद्रिय-क्षेत्र", "rūp": "दृश्य रूप का इंद्रिय-क्षेत्र",
        "sadd": "ध्वनि का इंद्रिय-क्षेत्र", "gandh": "गंध का इंद्रिय-क्षेत्र", "ras": "स्वाद का इंद्रिय-क्षेत्र",
        "phoṭṭhabb": "स्पर्श का इंद्रिय-क्षेत्र"}

# ---------------------------------------------------------------- frames -------------
def T(x, body, close=None):
    """Tattha katamo/katamā/katamaṃ X? <body> – ayaṃ/idaṃ vuccati X.  (pi-4 ^4-45 … frame)"""
    return f"यहाँ {x} क्या है? {body} {D} इसे {close or x} कहा जाता है{DANDA}"


def TPE(x):
    """Tattha katamā X…pe… ayaṃ vuccati X."""
    return f"यहाँ {x} क्या है … इसे {x} कहा जाता है{DANDA}"


def JO(s):
    """'Yo/Yā/Yaṃ S' (a synonym string): 'जो <first> है, <rest>' (pi-4 ^4-45 form)."""
    first, rest = s.split(", ", 1)
    return f"जो {first} है, {rest}"


# ---------------------------------------------------------------- defilement names ---
SAKKAYA = "स्थायी आत्मा की ग़लत दृष्टि"                  # sakkāyadiṭṭhi (pi-5)
VICI = "संशय"                                           # vicikicchā
SILABBATA = "सदाचार और व्रतों के बारे में ग़लत धारणा"      # sīlabbataparāmāsa
THREE_FETTERS = f"तीन बंधन {D} {SAKKAYA}, {VICI}, {SILABBATA}"   # Tīṇi saṃyojanāni – …

KAMASAVA = "इंद्रिय-सुखों का मैल"
BHAVASAVA = "अस्तित्व का मैल"
DITTHASAVA = "दृष्टि का मैल"
AVIJJASAVA = "अज्ञान का मैल"

SY = {"kāmarāga": "इंद्रिय-सुखों के राग का बंधन", "paṭigha": "चिढ़ का बंधन",
      "māna": "अहंकार का बंधन", "diṭṭhi": "दृष्टि का बंधन", "vicikicchā": "संशय का बंधन",
      "sīlabbataparāmāsa": f"{SILABBATA} का बंधन", "bhavarāga": "अस्तित्व के राग का बंधन",
      "issā": "ईर्ष्या का बंधन", "macchariya": "कंजूसी का बंधन", "avijjā": "अज्ञान का बंधन"}

G_ABH = "लालच रूपी काया की गाँठ"
G_BYA = "दुर्भावना रूपी काया की गाँठ"
G_SIL = f"{SILABBATA} रूपी काया की गाँठ"
G_IDAM = "“केवल यही सत्य है” के आग्रह रूपी काया की गाँठ"


def obl_name(x):
    """'अज्ञान का मैल' -> 'अज्ञान के मैल' (oblique, before 'के साथ'); feminine names unchanged."""
    return re.sub(r" का (\S+)$", r" के \1", x)


# ---------------------------------------------------------------- synonym strings ----
# diṭṭhi string: approved Hindi pi-4 ^4-62, with parāmāso = ग़लत धारणा (matrix term)
DS_WORDS = ["दृष्टि में पड़ जाना", "दृष्टि का घना जंगल", "दृष्टि का बीहड़", "दृष्टि का टेढ़ापन{v}",
            "दृष्टि की छटपटाहट", "दृष्टि का बंधन", "पकड़", "कसकर पकड़ना", "आग्रह", "ग़लत धारणा",
            "कुमार्ग", "ग़लत रास्ता", "ग़लतपन", "मतवादों का अड्डा", "उलटी पकड़"]
DS = ", ".join(DS_WORDS)
EVA_DITTHI = "जो इस प्रकार की दृष्टि है, " + DS.format(v="")          # yā evarūpā diṭṭhi diṭṭhigataṃ …
EVA_DITTHI_V = "जो इस प्रकार की दृष्टि है, " + DS.format(v=V("s", "Sī.", "diṭṭhivisūkāyitaṃ"))

SAKKAYA_BODY = (
    "यहाँ कोई अशिक्षित साधारण व्यक्ति, जिसने आर्यों के दर्शन नहीं किए, जो आर्यों की शिक्षा में "
    "निपुण नहीं और आर्यों की शिक्षा में प्रशिक्षित नहीं, जिसने सज्जनों के दर्शन नहीं किए, जो सज्जनों "
    "की शिक्षा में निपुण नहीं और सज्जनों की शिक्षा में प्रशिक्षित नहीं, भौतिक रूप को आत्मा के रूप में "
    "देखता है, या आत्मा को भौतिक रूप वाला, या आत्मा में भौतिक रूप को, या भौतिक रूप में आत्मा को। "
    "वह अनुभूति को आत्मा के रूप में देखता है, या आत्मा को अनुभूति वाला, या आत्मा में अनुभूति को, "
    "या अनुभूति में आत्मा को। वह पहचान को आत्मा के रूप में देखता है, या आत्मा को पहचान वाला, "
    "या आत्मा में पहचान को, या पहचान में आत्मा को। वह मानसिक रचनाओं को आत्मा के रूप में देखता है, "
    "या आत्मा को मानसिक रचनाओं वाला, या आत्मा में मानसिक रचनाओं को, या मानसिक रचनाओं में आत्मा को। "
    "वह चेतना को आत्मा के रूप में देखता है, या आत्मा को चेतना वाला, या आत्मा में चेतना को, "
    "या चेतना में आत्मा को। " + EVA_DITTHI_V[0].upper() + EVA_DITTHI_V[1:])

PS_DHAMMA = "कार्य-कारण के नियम से परस्पर-आश्रित रूप से उत्पन्न परिघटनाओं"  # idappaccayatā paṭiccasamuppannesu dhammesu
KANKHA_OBJ = ["गुरु", "शिक्षा", "संघ", "प्रशिक्षण", "अतीत", "भविष्य", "अतीत और भविष्य दोनों", PS_DHAMMA]
VICI_INTRO = "कोई " + ", ".join(f"{o} के बारे में शंका करता है, संशय करता है" for o in KANKHA_OBJ)
KANKHA_STR = ("जो इस प्रकार की शंका है, शंका करना, शंका से भरा होना, दुविधा, संशय, दोचित्तापन, दोराहा, "
              "संदेह, किसी एक बात को पक्का न पकड़ पाना, हिचकिचाना, बार-बार हिचकिचाना, गहराई में न उतर पाना, "
              "मन का जड़ हो जाना, मन की खरोंच")

SIL_INTRO = ("इस शिक्षा से बाहर के श्रमण और ब्राह्मण मानते हैं कि “सदाचार से शुद्धि होती है, व्रत से "
             "शुद्धि होती है, सदाचार और व्रत से शुद्धि होती है”")

# greed (lobha string)
LOBHA = [
    "राग", "गहरा राग", "झुकाव", "अनुकूल होना", "रस लेना", "रस-भरा राग{v1}", "मन का गहरा राग", "इच्छा",
    "मूर्छा", "चिपके रहना", "लालसा", "गहरी लालसा", "लगाव", "कीचड़", "हलचल", "कपट", "जन्म देने वाली",
    "उत्पन्न करने वाली", "सिलने वाली{v2}", "जाल बुनने वाली", "धारा", "फँसाने वाली", "धागा", "फैली हुई",
    "जुटाने वाली{v3}", "साथिन", "आकांक्षा", "अस्तित्व की डोर", "वन", "झाड़-झंखाड़", "घनिष्ठता", "स्नेह",
    "अपेक्षा", "नाता", "आशा", "आशा करना", "आशा से भरा होना{v4}", "दृश्य रूपों की आशा", "ध्वनियों की आशा",
    "गंधों की आशा", "स्वादों की आशा", "स्पर्शों की आशा", "लाभ की आशा", "धन की आशा", "संतान की आशा",
    "जीवन की आशा", "तड़प", "गहरी तड़प", "अत्यधिक तड़प", "तड़प", "तड़पना", "तड़प से भरा होना", "लोलुपता",
    "लोलुप होना", "लोलुपता से भरा होना", "चापलूसी{v5}", "बढ़िया चीज़ों की चाह", "अनैतिक राग", "अनुचित लोभ",
    "रुचि", "गहरी कामना", "कामना", "ललक", "प्रबल कामना", "इंद्रिय-सुखों की तृष्णा", "अस्तित्व की तृष्णा",
    "अनस्तित्व की तृष्णा", "सूक्ष्म भौतिक अस्तित्व की तृष्णा", "अभौतिक अस्तित्व की तृष्णा",
    "समाप्ति की तृष्णा", "दृश्य रूपों की तृष्णा", "ध्वनियों की तृष्णा", "गंधों की तृष्णा", "स्वादों की तृष्णा",
    "स्पर्शों की तृष्णा", "मन के विषयों की तृष्णा", "बाढ़", "जकड़न", "गाँठ", "आसक्ति", "आवरण", "बाधा",
    "पर्दा", "बेड़ी", "दूषण", "सुप्त प्रवृत्ति", "आवेश", "लता", "लोभीपन", "दुःख का मूल", "दुःख का स्रोत",
    "दुःख का उद्गम", "मार का फंदा", "मार का काँटा", "मार का क्षेत्र", "तृष्णा की नदी", "तृष्णा का जाल",
    "तृष्णा का पट्टा", "तृष्णा का सागर", "लालच", "लोभ", "हानिकर मूल"]
assert len(LOBHA) == 102, len(LOBHA)   # 103 Pāli words; "cittassa sārāgo" is one item
LOBHA_STR = ", ".join(LOBHA)
LOBHA_V = LOBHA_STR.format(v1=V("s", "Sī.", "nandirāgo"), v2=V("s", "Sī.", "sibbanī"),
                           v3=V("s", "Sī., Syā.", "āyūhanī"),
                           v4=V("s", "Sī., Syā.", "āsiṃsanā āsiṃsitattaṃ"),
                           v5=" [वर्तनी-भेद (Syā.): puñcikatā; (Sī.): pucchikatā]")
LOBHA_PLAIN = LOBHA_STR.format(v1="", v2="", v3="", v4="", v5="")

# hate (dosa string); the kodho … anattamanatā cittassa tail is the approved pi-4 ^4-45 wording
DOSA_INTRO = ("“उसने मेरा अहित किया” इस विचार से आक्रोश उत्पन्न होता है, “वह मेरा अहित कर रहा है” इस "
              "विचार से आक्रोश उत्पन्न होता है, “वह मेरा अहित करेगा” इस विचार से आक्रोश उत्पन्न होता है, "
              "“उसने मेरे प्रिय और मनभावन व्यक्ति का अहित किया … अहित कर रहा है … अहित करेगा” इस विचार से "
              "आक्रोश उत्पन्न होता है, “उसने मेरे अप्रिय और मन को न भाने वाले व्यक्ति का हित किया … हित कर "
              "रहा है … हित करेगा” इस विचार से आक्रोश उत्पन्न होता है, या बिना कारण भी आक्रोश उत्पन्न होता है।")
DOSA_STR = ("जो इस प्रकार का मन का आक्रोश है, प्रतिघात, चिढ़, प्रतिविरोध, कोप, प्रकोप, तीव्र प्रकोप, द्वेष, "
            "गहरा द्वेष, तीव्र द्वेष, मन की दुर्भावना, मन का द्वेष, क्रोध, क्रोध करना, क्रुद्ध होना, द्वेष, "
            "द्वेष करना, द्वेष से भरा होना, दुर्भावना, दुर्भावना रखना, दुर्भावना से भरा होना, विरोध, "
            "प्रतिविरोध, उग्रता, कटु वचन, मन की अप्रसन्नता")
DOSA_BODY = DOSA_INTRO + " " + DOSA_STR

# knowledge / lack of knowledge of the four truths, past, future, conditionality
NANA_OBJ = ["दुःख", "दुःख की उत्पत्ति", "दुःख के अंत", "दुःख के अंत की ओर ले जाने वाले मार्ग", "अतीत",
            "भविष्य", "अतीत और भविष्य दोनों", PS_DHAMMA]
NANA_OBJ_GEN = ["दुःख का", "दुःख की उत्पत्ति का", "दुःख के अंत का", "दुःख के अंत की ओर ले जाने वाले मार्ग का",
                "अतीत का", "भविष्य का", "अतीत और भविष्य दोनों का", PS_DHAMMA + " का"]
NANA4 = ", ".join(f"{o} ज्ञान" for o in NANA_OBJ_GEN)                 # Dukkhe ñāṇaṃ … ñāṇaṃ
ANANA4 = ", ".join(f"{o} को न जानना" for o in NANA_OBJ)               # Dukkhe aññāṇaṃ … aññāṇaṃ
# moha string: approved pi-4 ^4-60 wording, with yoga = जकड़न and akusalamūlaṃ = हानिकर मूल
MOHA_REST = ("न देखना, सत्य तक न पहुँचना, बोध न होना, पूर्ण बोध न होना, भेद न पाना, न समेट पाना, "
             "गहराई में न उतर पाना, निष्पक्ष रूप से न देखना, पुनः विचार न करना, प्रत्यक्ष न करना, "
             "दुर्बुद्धि, मूर्खता, स्पष्ट समझ का अभाव, मोह, गहरा मोह, घोर मोह, अज्ञान, अज्ञान की बाढ़, "
             "अज्ञान की जकड़न, अज्ञान की सुप्त प्रवृत्ति, अज्ञान का आवेश, अज्ञान की रुकावट, मोह, हानिकर मूल")
EVA_MOHA = "जो इस प्रकार का न जानना है, " + MOHA_REST              # yaṃ evarūpaṃ aññāṇaṃ adassanaṃ …

assert C.S_PANNA.startswith("प्रज्ञा, ")
EVA_PANNA = "जो इस प्रकार की प्रज्ञा है, " + C.S_PANNA[len("प्रज्ञा, "):]   # yā evarūpā paññā pajānanā …
BOJJH = "परिघटनाओं की छानबीन रूपी जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ"
# dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ

METTA = ("मैत्री, मैत्री करना, मैत्री से भरा होना, दया, दया करना, दया से भरा होना, हित की कामना, "
         "सहानुभूति")   # metti mettāyanā mettāyitattaṃ anuddā anuddāyanā anudāyitattaṃ hitesitā anukampā
S_ADOSA_X = C.S_ADOSA.replace("द्वेष से भरा न होना, ", "द्वेष से भरा न होना, " + METTA + ", ", 1)
assert S_ADOSA_X != C.S_ADOSA
assert C.S_ADOSA.startswith("द्वेष का अभाव, द्वेष न करना, द्वेष से भरा न होना, ")
S_ADOSA_PE = ("द्वेष का अभाव, द्वेष न करना, द्वेष से भरा न होना … "
              + C.S_ADOSA[C.S_ADOSA.index("दुर्भावना का अभाव"):])
# Yo adoso adussanā adussitattaṃ…pe… abyāpādo abyāpajjo adoso kusalamūlaṃ

KAMA_STR = ("इंद्रिय-सुखों के प्रति जो इंद्रिय-सुखों की चाह है, इंद्रिय-सुखों का राग, इंद्रिय-सुखों में "
            "रस लेना, इंद्रिय-सुखों की तृष्णा, इंद्रिय-सुखों का स्नेह, इंद्रिय-सुखों का ताप, "
            "इंद्रिय-सुखों की मूर्छा, इंद्रिय-सुखों से चिपके रहना")
BHAVA_STR = ("अस्तित्व के प्रति जो अस्तित्व की चाह है{v}, अस्तित्व का राग, अस्तित्व में रस लेना, "
             "अस्तित्व की तृष्णा, अस्तित्व का स्नेह, अस्तित्व का ताप, अस्तित्व की मूर्छा, "
             "अस्तित्व से चिपके रहना")

VIEWS10 = ["लोक शाश्वत है", "लोक शाश्वत नहीं है", "लोक सीमित है", "लोक असीम है",
           "जो जीव है, वही शरीर है", "जीव अलग है, शरीर अलग है", "मृत्यु के बाद तथागत रहता है",
           "मृत्यु के बाद तथागत नहीं रहता", "मृत्यु के बाद तथागत रहता भी है और नहीं भी रहता",
           "मृत्यु के बाद तथागत न रहता है, न नहीं रहता"]                  # wording of the Hindi pi-5
VIEWS10_STR = " या ".join(f"“{v}”" for v in VIEWS10)
IDAM10_STR = "; या ".join(f"“{v}, केवल यही सत्य है, बाकी सब झूठ है”" for v in VIEWS10)
MICCHA_ALL = "सारी ग़लत दृष्टि {} है।"                                  # Sabbāpi micchādiṭṭhi X.

MANA_BODY = ("“मैं श्रेष्ठ हूँ” यह अहंकार, “मैं बराबर हूँ” यह अहंकार, “मैं हीन हूँ” यह अहंकार। "
             "जो इस प्रकार का अहंकार है, मान लेना, मान चुका होना, ऊँचा उठना, अकड़"
             + V("s", "Syā.", "uṇṇati uṇṇāmo") + ", झंडा, स्वयं को ऊपर उठाना, मन की झंडा फहराने की इच्छा")
# issā / macchariya: approved Hindi pi-4 ^4-49 / ^4-50 verbatim
ISSA_BODY = ("दूसरों को मिलने वाले लाभ, सत्कार, सम्मान, आदर, वंदना और पूजा को लेकर जो ईर्ष्या है, "
             "ईर्ष्या करना, ईर्ष्या से भरा होना, जलन, जलना, जलन से भरा होना"
             + V("s", "Ka.", "ussuyā ussuyanā ussuyitattaṃ"))
MACCH_BODY = (f"कंजूसी पाँच प्रकार की होती है {D} निवास-स्थान को लेकर कंजूसी, (सहायक) परिवारों को लेकर "
              "कंजूसी, लाभ को लेकर कंजूसी, प्रशंसा को लेकर कंजूसी, शिक्षा को लेकर कंजूसी। जो इस प्रकार की "
              "कंजूसी है, कंजूसी करना, कंजूस होना, लोभीपन, कृपणता, मुट्ठी भींचे रखना, मन का संकुचित होना")

# ---------------------------------------------------------------- relative frames ----
def REL(pred):
    """Tehi dhammehi ye dhammā X (sahetukā / ahetukā / na hetū sahetukā …)"""
    return f"उन परिघटनाओं के संबंध में जो परिघटनाएँ {pred}"


ASSOC = "उन परिघटनाओं से जो परिघटनाएँ जुड़ी हैं"        # Tehi dhammehi ye dhammā sampayuttā
DISS = "उन परिघटनाओं से जो परिघटनाएँ अलग हैं"           # Tehi dhammehi ye dhammā vippayuttā
EXCL = "उनमें से उन्हीं परिघटनाओं को छोड़कर"            # (…,) te dhamme ṭhapetvā


def AMONG(pred):
    """Tehi dhammehi ye dhammā X, te dhamme ṭhapetvā"""
    return f"{REL(pred)}, {EXCL}"


AMONG_ASSOC = f"{ASSOC}, {EXCL}"
YANI = "यानी"   # links a relative clause to the list it names (Pāli has no word here)


def both(pairs, sg_root, sg_assoc):
    """'X Y-ena Z ceva Z-sampayutto ca' -> 'X, Y के साथ, Z भी है और Z से जुड़ा भी'."""
    return ", ".join(f"{x}, {obl_name(y)} के साथ, {sg_root} भी है और {sg_assoc} भी" for x, y in pairs)


# ---------------------------------------------------------------- arising / time -----
POS = ["जन्मी हुई", "हो चुकी", "भली-भाँति जन्मी", "पैदा हुई", "पूरी तरह पैदा हुई", "प्रकट हुई", "उत्पन्न",
       "भली-भाँति उत्पन्न", "उठी हुई", "भली-भाँति उठी हुई"]
# jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā uppannā samuppannā uṭṭhitā samuṭṭhitā
NEG = ["न " + w for w in POS]
PAST = ["बीत चुकी", "समाप्त हो चुकी", "जा चुकी", "बदल चुकी", "अस्त हो चुकी", "पूरी तरह अस्त हो चुकी",
        "उत्पन्न होकर जा चुकी"]
# atītā niruddhā vigatā vipariṇatā atthaṅgatā abbhatthaṅgatā uppajjitvā vigatā
NAMES5 = "भौतिक रूप{v}, अनुभूति, पहचान, मानसिक रचनाएँ, चेतना"


def ARISEN(words, state, label, v=""):
    """Ye dhammā <words> <state> <state>aṃsena saṅgahitā, rūpaṃ, vedanā, …"""
    return (f"जो परिघटनाएँ {', '.join(words)} हैं, {state} हैं और “{label}” के अंतर्गत गिनी जाती हैं, "
            f"{YANI} " + NAMES5.format(v=v))


# ---------------------------------------------------------------- the planes ---------
def bhumi(plane, keys, excl):
    """'<X>bhūmiyaṃ kāmāvacare, …, <X> ṭhapetvā'; plane = '<X> की भूमि' / '<X> वाली भूमि'"""
    s = f"{plane} में, " + whether(keys, "f", "वह", "हो")
    return s + (f", {excl} को छोड़कर" if excl else "")


# ---------------------------------------------------------------- kenaci viññeyyā ----
SENSE = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर"}


def kenaci_seg(pali):
    pairs = re.findall(r"Ye te dhammā (\w+?)viññeyyā,? na te dhammā (\w+?)viññeyyā", pali)
    assert len(pairs) == 20, len(pairs)
    sents = []
    for a, b in pairs:
        A_, B_ = SENSE[a], SENSE[b]
        sents.append(f"जो परिघटनाएँ {A_} की चेतना से जानी जा सकती हैं, वे {B_} की चेतना से नहीं जानी जा "
                     f"सकतीं; और जो परिघटनाएँ {B_} की चेतना से जानी जा सकती हैं, वे {A_} की चेतना से नहीं "
                     f"जानी जा सकतीं।")
    a, b = item("2-13", "क"), item("2-13", "ख")
    return " ".join([f"{a} और {b} कौन-सी हैं?"] + sents + [f"ये {a} और {b} हैं{DANDA}"])


# ---------------------------------------------------------------- build --------------
def build(pali_text):
    S = {}
    S["1-3-0"] = [H_CH4]
    S["1-3-1-0"] = [H_TIKA]
    S["1-985"] = [QA("1-1", "क", f"{ROOTS_K}; {TS4}; {KAMMA}")]
    S["1-986"] = [QA("1-1", "ख", f"{ROOTS_A}; {TADEK}; {TS4}; {KAMMA}")]
    S["1-987"] = [QA("1-1", "ग", f"{VIPAKA}, {W4M}; {KH4}; {KIRIYA}; {RUPA_ASANKH}")]
    sukha_v = "सुखद अनुभूति"
    dukkha_v = "दुःखद अनुभूति"
    neut_v = "न दुःखद, न सुखद अनुभूति"
    S["1-988"] = [QA("1-2", "क", f"{bhumi(sukha_v + ' की भूमि', 'krp', sukha_v)}; {TS3}")]
    S["1-989"] = [QA("1-2", "ख", f"{bhumi(dukkha_v + ' की भूमि', 'k', dukkha_v)}; {TS3}")]
    S["1-990"] = [QA("1-2", "ग", f"{bhumi(neut_v + ' की भूमि', 'krap', neut_v)}; {TS3}")]
    S["1-991"] = [QA("1-3", "क", f"{VIPAKA}, {W4M}; {KH_PE}")]
    S["1-992"] = [QA("1-3", "ख", f"{KUSAKU}, {W4F}; {KH_PE}")]
    S["1-993"] = [QA("1-3", "ग", f"{KIRIYA_BARE}, {RUPA_ASANKH}")]
    S["1-994"] = [QA("1-4", "क", f"मन के मैलों का विषय बनने वाले, {VIPAKA}, {W3}; {KH_PE}; और {KATATTA}")]
    S["1-995"] = [QA("1-4", "ख", f"{SAS} {KUSAKU}, {W3}; {KH_PE}; {KIRIYA}; और {NA_KATATTA}")]
    S["1-996"] = [QA("1-4", "ग", MAGGA)]
    S["1-997"] = [QA("1-5", "क", f"{ROOTS_A}; {TADEK}; {TS_PE}; {KAMMA}")]
    S["1-998"] = [QA("1-5", "ख", f"{SAS} {KUSAB}, {W3}; {KH5}")]
    S["1-999"] = [QA("1-5", "ग", MAGGA)]
    vv = "आरंभिक विचार और सतत विचार"
    S["1-1000"] = [QA("1-6", "क", f"{bhumi(vv + ' वाली भूमि', 'krp', vv)}; {TS_PE}")]
    S["1-1001"] = [QA("1-6", "ख", f"{bhumi('आरंभिक विचार से रहित, केवल सतत विचार वाली भूमि', 'rp', 'सतत विचार')}; "
                                   f"{TS_PE}")]
    S["1-1002"] = [QA("1-6", "ग", f"{bhumi(vv + ' दोनों से रहित भूमि', 'krap', None)}; {KH_PE}; {RUPA_ASANKH}")]
    S["1-1003"] = [QA("1-7", "क", f"{bhumi('उल्लास की भूमि', 'krp', 'उल्लास')}; {TS_PE}")]
    S["1-1004"] = [QA("1-7", "ख", f"{bhumi('सुख की भूमि', 'krp', 'सुख')}; {TS3}")]
    S["1-1005"] = [QA("1-7", "ग", f"{bhumi('समभाव की भूमि', 'krap', 'समभाव')}; {TS3}")]
    S["1-1006"] = [f"{Q('1-8', 'क')} {THREE_FETTERS}{DANDA}"]
    S["1-1007"] = [T(SAKKAYA, SAKKAYA_BODY)]
    S["1-1008"] = [T(VICI, VICI_INTRO + "। " + KANKHA_STR)]
    S["1-1009"] = [T(SILABBATA, SIL_INTRO + "; " + EVA_DITTHI)]
    S["1-1010"] = [f"ये तीन बंधन; {TADEK}; {TS_PE}; {KAMMA} {D} {A('1-8', 'क')}"]
    S["1-1011"] = [QA("1-8", "ख", f"बाकी लोभ, द्वेष, मोह; {TADEK}; {TS_PE}; {KAMMA}")]
    S["1-1012"] = [QA("1-8", "ग", f"{KUSAB}, {W4F}; {KH_PE}; {RUPA_ASANKH}")]
    S["1-1013"] = [f"{Q('1-9', 'क')} {THREE_FETTERS}{DANDA}"]
    S["1-1014"] = [TPE(SAKKAYA)]
    S["1-1015"] = [TPE(VICI)]
    S["1-1016"] = [TPE(SILABBATA)]
    S["1-1017"] = [f"ये तीन बंधन; {TADEK}; {TS_PE}; {KAMMA} {D} {A('1-9', 'क')} "
                   f"{THREE_FETTERS} {D} {A('1-8', 'क')} "
                   f"{TADEK_LDM} {D} ये सत्य-दर्शन से छोड़े जाने वाले मूल हैं{DANDA} "
                   f"{TADEK}; {TS_PE}; {KAMMA} {D} {A('1-9', 'क')}"]
    S["1-1018"] = [f"{Q('1-9', 'ख')} बाकी लोभ, द्वेष, मोह {D} ये मानसिक अभ्यास से छोड़े जाने वाले मूल हैं{DANDA} "
                   f"{TADEK}; {TS_PE}; {KAMMA} {D} {A('1-9', 'ख')}"]
    S["1-1019"] = [QA("1-9", "ग", f"{TE_THAPETVA}, {W4F}; {KH4}; {RUPA_ASANKH}")]
    S["1-1020"] = [QA("1-10", "क", f"{SAS} {KUSAKU}, {W3}; {KH_PE}")]
    S["1-1021"] = [QA("1-10", "ख", PATHS4)]
    S["1-1022"] = [QA("1-10", "ग", f"{VIPAKA}, {W4M}; {KH_PE}; {KIRIYA}; {RUPA_ASANKH}")]
    S["1-1023"] = [QA("1-11", "क", f"{PATHS4}, और श्रमण-जीवन के तीन निचले फल")]
    S["1-1024"] = [QA("1-11", "ख", "सबसे ऊपर का" + V("p", "Syā.", "uparimaṃ") + " फल, यानी अर्हत्-पद का फल")]
    S["1-1025"] = [QA("1-11", "ग", f"{TE_THAPETVA}, {W3}; {KH_PE}; {RUPA_ASANKH}")]
    S["1-1026"] = [QA("1-12", "क", f"इंद्रिय-सुखों के लोक से संबंधित सभी {ALL3}; {KH_R_PE}")]
    S["1-1027"] = [QA("1-12", "ख", f"सूक्ष्म भौतिक लोक से और अभौतिक लोक से संबंधित {KUSAB}; {KH_PE}")]
    S["1-1028"] = [QA("1-12", "ग", MAGGA)]
    for bid, src, dst in (("1-1029", "क", "क"), ("1-1030", "ख", "ख"), ("1-1031", "ग", "ग")):
        S[bid] = [QA("1-13", dst, CITTACET(obl(item("1-12", src))))]
    S["1-1032"] = [QA("1-14", "क", f"{ROOTS_A}; {TADEK}; {TS_PE}; {KAMMA}")]
    S["1-1033"] = [QA("1-14", "ख", f"{SAS} {KUSAB}, {W3}, {KH_R_PE}")]
    S["1-1034"] = [QA("1-14", "ग", MAGGA)]
    S["1-1035"] = [QA("1-15", "क", "तत्काल फल देने वाले पाँच घोर कर्म, और जो ग़लत दृष्टि निश्चित परिणाम वाली है")]
    S["1-1036"] = [QA("1-15", "ख", PATHS4)]
    S["1-1037"] = [QA("1-15", "ग", f"{TE_THAPETVA}, {W4F}; {KH_PE}; {RUPA_ASANKH}")]
    S["1-1038"] = [QA("1-16", "क", CITTACET("आर्य मार्ग"))]
    sam = "आर्य मार्ग से युक्त व्यक्ति में"            # Ariyamaggasamaṅgissa
    S["1-1039"] = [f"{Q('1-16', 'ख')} {sam} मार्ग के अंगों को छोड़कर; {TS_PE} {D} {A('1-16', 'ख')} "
                   f"{sam} सही दृष्टि मार्ग भी है और मूल भी, सही दृष्टि को छोड़कर, {TS_PE} {D} {A('1-16', 'ख')} "
                   f"{sam} {N['alobho']}, {N['adoso']}, {N['amoho']} {D} ये मार्ग के मूल हैं{DANDA} "
                   f"{TS_PE} {D} {A('1-16', 'ख')}"]
    S["1-1040"] = [f"{Q('1-16', 'ग')} आर्य मार्ग को प्रधान बनाकर जो मन और मन की सहचर परिघटनाएँ उत्पन्न होती हैं "
                   f"{D} {A('1-16', 'ग')} जो आर्य मार्ग से युक्त व्यक्ति जाँच-परख की प्रधानता वाले मार्ग का "
                   f"अभ्यास करता है, उसमें जाँच-परख को छोड़कर; {TS_PE} {D} {A('1-16', 'ग')}"]
    S["1-1041"] = [QA("1-17", "क", ARISEN(POS, "उत्पन्न", "उत्पन्न", V("p", "अनेक संस्करण", "rūpā")))]
    S["1-1042"] = [QA("1-17", "ख", ARISEN(NEG, "उत्पन्न नहीं", "उत्पन्न न हुई"))]
    S["1-1043"] = [QA("1-17", "ग", f"अनपके कर्म-फल वाली {obl(KUSAKU)} के कर्म-फल, "
                                    f"{W4M}; {KH_PE}; और {KATATTA_FUT}")]
    S["1-1044"] = [QA("1-18", "क", ARISEN(PAST, "अतीत की", "अतीत"))]
    S["1-1045"] = [QA("1-18", "ख", ARISEN(NEG, "भविष्य की", "भविष्य"))]
    S["1-1046"] = [QA("1-18", "ग", ARISEN(POS, "वर्तमान की", "वर्तमान"))]
    for bid, l in (("1-1047", "क"), ("1-1048", "ख"), ("1-1049", "ग")):
        S[bid] = [QA("1-19", l, CITTACET(obl(item("1-18", l))))]
    own = "उनकी अपनी, उन्हीं से बँधी, हर व्यक्ति की निजी और कर्म से उत्पन्न"
    S["1-1050"] = [QA("1-20", "क", f"जो परिघटनाएँ उन-उन प्राणियों के भीतर, {own} हैं, {YANI} "
                                    + NAMES5.format(v=""))]
    S["1-1051"] = [QA("1-20", "ख", f"जो परिघटनाएँ उन-उन दूसरे प्राणियों, दूसरे व्यक्तियों के भीतर, {own} हैं, "
                                    f"{YANI} " + NAMES5.format(v=""))]
    S["1-1052"] = [QA("1-20", "ग", "ये दोनों")]
    for bid, l in (("1-1053", "क"), ("1-1054", "ख"), ("1-1055", "ग")):
        S[bid] = [QA("1-21", l, CITTACET(obl(item("1-20", l))))]
    S["1-1056"] = [QA("1-22", "क", BASE["rūp"])]
    S["1-1057"] = [QA("1-22", "ख", ", ".join(BASE[k] for k in
                                             ("cakkh", "sot", "ghān", "jivh", "kāy", "sadd", "gandh", "ras",
                                              "phoṭṭhabb")))]
    S["1-1058"] = [QA("1-22", "ग", f"{KH4}; और {RUPA_DHAY}; और {ASANKHATA}"), END_TIKA]

    # ---- pairs: roots
    S["1-3-2-0"] = [H_DUKA]
    S["1-3-2-1-0"] = [M.GROUPS["1-M-2-1-0"][0]]
    sph_k, sph_r, sph_a = SPH["k"], SPH["r"], SPH["a"]
    S["1-1059"] = [f"{Q('2-1', 'क')} तीन हितकर मूल, तीन हानिकर मूल, तीन नैतिक रूप से अनिर्धारित मूल, "
                   f"{sph_k} नौ मूल, {sph_r} छह मूल, {sph_a} छह मूल, {APAR['m']} छह मूल{DANDA}"]
    R3K, R3A, R3U = "तीन हितकर मूल", "तीन हानिकर मूल", "तीन नैतिक रूप से अनिर्धारित मूल"
    S["1-1060"] = [f"यहाँ {R3K} कौन-से हैं? {N['alobho']}, {N['adoso']}, {N['amoho']}{DANDA}"]
    S["1-1061"] = [T(N["alobho"], JO(C.S_ALOBHA))]
    S["1-1062"] = [T(N["adoso"], JO(S_ADOSA_X))]
    S["1-1063"] = [T(N["amoho"], NANA4 + ", " + EVA_PANNA), f"ये {R3K} हैं{DANDA}"]
    S["1-1064"] = [f"यहाँ {R3A} कौन-से हैं? लोभ, द्वेष, मोह{DANDA}"]
    S["1-1065"] = [T("लोभ", JO(LOBHA_V))]
    S["1-1066"] = [T("द्वेष", DOSA_BODY)]
    S["1-1067"] = [T("मोह", ANANA4 + ", " + EVA_MOHA), f"ये {R3A} हैं{DANDA}"]
    NGD = f"{N['alobho']}, {N['adoso']}, {N['amoho']}"
    VIP_OF = "हितकर परिघटनाओं के कर्म-फल के रूप में"          # Kusalānaṃ (vā) dhammānaṃ vipākato
    S["1-1068"] = [f"यहाँ {R3U} कौन-से हैं? {VIP_OF}, या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित परिघटनाओं "
                   f"में होने वाला {NGD} {D} ये {R3U} हैं{DANDA}"]
    S["1-1069"] = [f"यहाँ {sph_k} नौ मूल कौन-से हैं? {R3K}, {R3A}, {R3U} {D} ये {sph_k} नौ मूल हैं{DANDA}"]
    for bid, sph in (("1-1070", sph_r), ("1-1071", sph_a), ("1-1072", APAR["m"])):
        S[bid] = [f"यहाँ {sph} छह मूल कौन-से हैं? {R3K}, {R3U} {D} ये {sph} छह मूल हैं{DANDA}"]
    S["1-1073"] = S["1-1060"]
    S["1-1074"] = S["1-1061"]
    S["1-1075"] = [T(N["adoso"], JO(S_ADOSA_PE))]
    S["1-1076"] = [T(N["amoho"], NANA4 + ", " + EVA_PANNA + ", " + BOJJH), f"ये {R3K} हैं{DANDA}"]
    S["1-1077"] = [f"यहाँ {R3U} कौन-से हैं? {VIP_OF} होने वाला {NGD} {D} ये {R3U} हैं{DANDA} "
                   f"ये {APAR['m']} छह मूल {D} {A('2-1', 'क')}"]
    S["1-1078"] = [QA("2-1", "ख", f"{TE_THAPETVA}, {W4F}; {KH_PE}; {RUPA_ASANKH}")]
    S["1-1079"] = [QA("2-2", "क", f"{REL('मूल वाली हैं')}, {YANI} {KH_PE}")]
    S["1-1080"] = [QA("2-2", "ख", f"{REL('मूल से रहित हैं')}, {YANI} {KH_PE}, {RUPA_ASANKH}")]
    S["1-1081"] = [QA("2-3", "क", f"{ASSOC}, {YANI} {KH_PE}")]
    S["1-1082"] = [QA("2-3", "ख", f"{DISS}, {YANI} {KH_PE}, {RUPA_ASANKH}")]
    gm = [("लोभ", "मोह"), ("मोह", "लोभ"), ("द्वेष", "मोह"), ("मोह", "द्वेष")]
    S["1-1083"] = [QA("2-4", "क", both(gm, "मूल रूपी", "मूल वाला")
                      + f"; {NGD}, ये एक-दूसरे के साथ मूल रूपी भी हैं और मूल वाले भी")]
    S["1-1084"] = [QA("2-4", "ख", f"{AMONG('मूल वाली हैं')}, {KH_PE}")]
    S["1-1085"] = [QA("2-5", "क", both(gm, "मूल रूपी", "मूल से जुड़ा")
                      + f"; {NGD}, ये एक-दूसरे के साथ मूल रूपी भी हैं और मूलों से जुड़े भी")]
    S["1-1086"] = [QA("2-5", "ख", f"{AMONG_ASSOC}, {KH_PE}")]
    S["1-1087"] = [QA("2-6", "क", f"{REL('मूल रूपी नहीं हैं, पर मूल वाली हैं')}, {YANI} {KH_PE}")]
    S["1-1088"] = [QA("2-6", "ख", f"{REL('मूल रूपी नहीं हैं और मूल से रहित हैं')}, {YANI} {KH_PE}, {RUPA_ASANKH}")]

    # ---- short intermediate pairs
    S["1-3-2-2-0"] = [M.GROUPS["1-M-2-2-0"][0]]
    S["1-1089"] = [QA("2-7", "क", f"पाँच समूह {D} {KH5}")]
    S["1-1090"] = [QA("2-7", "ख", ASANKHATA)]
    S["1-1091"] = [f"{Q('2-8', 'क')} जो परिघटनाएँ कारणों पर निर्भर हैं, वही परिघटनाएँ निर्मित हैं{DANDA}"]
    S["1-1092"] = [f"{Q('2-8', 'ख')} जो परिघटना कारणों पर निर्भर नहीं रहती, वही परिघटना अनिर्मित है{DANDA}"]
    S["1-1093"] = [QA("2-9", "क", BASE["rūp"])]
    S["1-1094"] = [QA("2-9", "ख", f"{BASE['cakkh']} … {BASE['phoṭṭhabb']}, {KH_PE}, और {RUPA_DHAY}, "
                                   f"और {ASANKHATA}")]
    S["1-1095"] = [QA("2-10", "क", f"{BASE['cakkh']} … {BASE['phoṭṭhabb']}")]
    S["1-1096"] = [QA("2-10", "ख", f"{KH_PE}, और {RUPA_DHAY}, और {ASANKHATA}")]
    S["1-1097"] = [QA("2-11", "क", "चार महाभूत और चार महाभूतों से व्युत्पन्न भौतिक रूप")]
    S["1-1098"] = [QA("2-11", "ख", f"{KH_PE}, और {ASANKHATA}")]
    S["1-1099"] = [QA("2-12", "क", f"{SAS} {ALL3}, {W3}, {KH_R_PE}")]
    S["1-1100"] = [QA("2-12", "ख", MAGGA)]
    S["1-1101"] = [kenaci_seg(pali_text)]

    # ---- taints
    S["1-3-2-3-0"] = [M.GROUPS["1-M-2-3-0"][0]]
    S["1-1102"] = [f"{Q('2-14', 'क')} मन के चार मैल {D} {KAMASAVA}, {BHAVASAVA}, {DITTHASAVA}, {AVIJJASAVA}{DANDA}"]
    S["1-1103"] = [T(KAMASAVA, KAMA_STR)]
    S["1-1104"] = [T(BHAVASAVA, BHAVA_STR.format(v=V("s", "Sī., Syā.", "bhavacchando")))]
    S["1-1105"] = [T(DITTHASAVA, VIEWS10_STR + "; " + EVA_DITTHI) + " " + MICCHA_ALL.format(DITTHASAVA)]
    S["1-1106"] = [T(AVIJJASAVA, ANANA4 + "; " + EVA_MOHA), A("2-14", "क")]

    def group(first, mid0, plural, pred_sas, both_body, sas_first):
        """first: block number of the 'no X' item; mid0: matrix pair number of the 'X' item.
        pred_sas: 'मन के मैलों / बंधनों / गाँठों का विषय बनती हैं'.
        sas_first: the Pāli opens the 'X-niya' answer with 'Sāsavā' (fetters, ties) or not (taints)."""
        m = lambda i: f"2-{mid0 + i}"
        b = lambda i: f"1-{first + i}"
        S[b(0)] = [QA(m(0), "ख", f"{TE_THAPETVA}, {W4F}; {KH_PE}; {RUPA_ASANKH}")]
        S[b(1)] = [QA(m(1), "क", f"{SAS + ' ' if sas_first else ''}{ALL3}, {W3}; {KH_R_PE}")]
        S[b(2)] = [QA(m(1), "ख", MAGGA)]
        S[b(3)] = [QA(m(2), "क", f"{ASSOC}, {YANI} {KH_PE}")]
        S[b(4)] = [QA(m(2), "ख", f"{DISS}, {YANI} {KH_PE}; {RUPA_ASANKH}")]
        S[b(5)] = [f"{Q(m(3), 'क')} वे ही {plural}, {item(m(3), 'क')} हैं{DANDA}"]
        S[b(6)] = [QA(m(3), "ख", f"{AMONG(pred_sas)} बाकी, {SAS} {ALL3}, {W3}; {KH_R_PE}")]
        S[b(7)] = [QA(m(4), "क", both_body)]
        S[b(8)] = [QA(m(4), "ख", f"{AMONG_ASSOC}, {KH_PE}")]
        S[b(9)] = [QA(m(5), "क", f"{DISS} और {SAS} {ALL3} हैं, {W3}, {KH_R_PE}")]
        S[b(10)] = [QA(m(5), "ख", MAGGA)]

    av = [(KAMASAVA, AVIJJASAVA), (AVIJJASAVA, KAMASAVA), (BHAVASAVA, AVIJJASAVA), (AVIJJASAVA, BHAVASAVA),
          (DITTHASAVA, AVIJJASAVA), (AVIJJASAVA, DITTHASAVA)]
    group(1107, 14, "मन के मैल", "मन के मैलों का विषय बनती हैं",
          both(av, "मन का मैल", "मन के मैल से जुड़ा"), False)
    S["1-1117"].append(END_BHANA1)

    # ---- fetters
    S["1-3-2-4-0"] = [M.GROUPS["1-M-2-4-0"][0]]
    order = ["kāmarāga", "paṭigha", "māna", "diṭṭhi", "vicikicchā", "sīlabbataparāmāsa", "bhavarāga", "issā",
             "macchariya", "avijjā"]
    S["1-1118"] = [f"{Q('2-20', 'क')} दस बंधन {D} " + ", ".join(SY[k] for k in order) + DANDA]
    S["1-1119"] = [T(SY["kāmarāga"], KAMA_STR)]
    S["1-1120"] = [T(SY["paṭigha"], DOSA_BODY)]
    S["1-1121"] = [T(SY["māna"], MANA_BODY)]
    S["1-1122"] = [T(SY["diṭṭhi"], VIEWS10_STR + "; " + EVA_DITTHI) + f" {obl_name(SY['sīlabbataparāmāsa'])} को छोड़कर "
                   + MICCHA_ALL.format(SY["diṭṭhi"])]
    S["1-1123"] = [T(SY["vicikicchā"], VICI_INTRO + "; " + KANKHA_STR)]
    S["1-1124"] = [T(SY["sīlabbataparāmāsa"], SIL_INTRO + "; " + EVA_DITTHI)]
    S["1-1125"] = [T(SY["bhavarāga"], BHAVA_STR.format(v=""))]
    S["1-1126"] = [T(SY["issā"], ISSA_BODY)]
    S["1-1127"] = [T(SY["macchariya"], MACCH_BODY)]
    S["1-1128"] = [T(SY["avijjā"], ANANA4 + "; " + EVA_MOHA), A("2-20", "क")]
    fp = []
    for k in order[:-1]:
        fp += [(SY[k], SY["avijjā"]), (SY["avijjā"], SY[k])]
    group(1129, 20, "बंधन", "बंधनों का विषय बनती हैं", both(fp, "बंधन", "बंधन से जुड़ा"), True)

    # ---- ties
    S["1-3-2-5-0"] = [M.GROUPS["1-M-2-5-0"][0]]
    S["1-1140"] = [f"{Q('2-26', 'क')} चार गाँठें {D} {G_ABH}, {G_BYA}, {G_SIL}, {G_IDAM}{DANDA}"]
    S["1-1141"] = [T(G_ABH, JO(LOBHA_PLAIN))]
    S["1-1142"] = [T(G_BYA, DOSA_BODY)]
    S["1-1143"] = [T(G_SIL, SIL_INTRO + "; " + EVA_DITTHI)]
    S["1-1144"] = [T(G_IDAM, IDAM10_STR + "; " + EVA_DITTHI) + f" {G_SIL} को छोड़कर " + MICCHA_ALL.format(G_IDAM),
                   A("2-26", "क")]
    gp = [(G_SIL, G_ABH), (G_ABH, G_SIL), (G_IDAM, G_ABH), (G_ABH, G_IDAM)]
    group(1145, 26, "गाँठें", "गाँठों का विषय बनती हैं", both(gp, "गाँठ", "गाँठ से जुड़ी"), True)
    return S


# ---------------------------------------------------------------- assemble -----------
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
LATIN = re.compile(r"[A-Za-zĀ-ž]")


def pali_segments(text):
    segs, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = ID.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return segs


def dashes(t):
    return t.count("–") + t.count("—")


def assemble(pali_text, S):
    out, problems = [], []
    segs = pali_segments(pali_text)
    assert set(S) == {b for b, _ in segs}, (set(S) ^ {b for b, _ in segs})
    for bid, plines in segs:
        hlines = S[bid]
        if len(hlines) != len(plines):
            problems.append((bid, "lines", len(plines), len(hlines)))
        for p, h in zip(plines, hlines):
            if dashes(p) != dashes(h):
                problems.append((bid, "dash", dashes(p), dashes(h)))
            if p.count("…pe…") != h.count("…"):
                problems.append((bid, "pe", p.count("…pe…"), h.count("…")))
            if p.count("[") != h.count("["):
                problems.append((bid, "variant", p.count("["), h.count("[")))
            if p.rstrip().endswith("?") != h.rstrip().endswith("?"):
                problems.append((bid, "final ?"))
            if p.startswith("#") and (len(p) - len(p.lstrip("#"))) != (len(h) - len(h.lstrip("#"))):
                problems.append((bid, "heading level"))
            if ":-" in h or "  " in h or "—" in h or "ः" in h.replace("दुःख", "").replace("पुनः", ""):
                problems.append((bid, "bad chars"))
            if LATIN.search(re.sub(r"\[[^\]]*\]", "", h)):
                problems.append((bid, "latin", LATIN.findall(re.sub(r"\[[^\]]*\]", "", h))[:5]))
            if h != h.strip() or ",," in h or " ," in h or " ।" in h:
                problems.append((bid, "spacing"))
        out.append("\n".join(hlines[:-1] + [hlines[-1] + f" ^{bid}"]))
    return "\n\n".join(out) + "\n", problems, len(segs)


PALI_TEXT = PALI.read_text(encoding="utf-8")
SEGS = build(PALI_TEXT)

if __name__ == "__main__":
    text, problems, n = assemble(PALI_TEXT, SEGS)
    for pr in problems:
        print(pr)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT.name, "segments", n, "problems", len(problems))
    sys.exit(1 if problems else 0)
