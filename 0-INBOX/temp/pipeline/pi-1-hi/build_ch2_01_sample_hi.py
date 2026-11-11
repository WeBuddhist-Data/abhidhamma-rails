"""Build the Hindi plain zero-shot SAMPLE of pi-1 ch.2 opening (^1-1 ... ^1-57).

usage: python -I -X utf8 build_ch2_01_sample_hi.py
All recurring strings are fixed constants below, so every repeat is byte-identical.
Importing this module does not write the file. Exposes NAMES, GENDER, STRINGS, FRAMES and the
frame functions (Q, A, QA, T, KAYA, CITTA, SHAME, LIST_ITEM, YEVAPANA) for later chapters.
"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_matika_hi import BARE, QUESTION, ANSWER, DANDA  # noqa: E402

PALI = HERE / "ch2-01-pali-1-122.md"
OUT = HERE / "ch2-01-sample.md"

DASH = "–"  # the en dash used by the Pāli source; only where the Pāli has one

KUSALA = BARE[("1-M1-1", "क")]      # हितकर परिघटनाएँ
AKUSALA = BARE[("1-M1-1", "ख")]     # हानिकर परिघटनाएँ
ABYAKATA = BARE[("1-M1-1", "ग")]    # नैतिक रूप से अनिर्धारित परिघटनाएँ

# ---- headings ------------------------------------------------------------------------
H_CH2 = "### मन की उत्पत्ति का अध्याय"
H_KAMA_KUSALA = "#### इंद्रिय-सुखों के लोक से संबंधित हितकर मन"
H_PADA = "##### पदों का विश्लेषण"
END_PADA = "पदों का विश्लेषण।"
END_BHANA1 = "पहला पाठ-खंड।"

# ---- names of the factors (Pāli = (Hindi, gender)), used in the list and in Q/A frames ----
M, F = "m", "f"
NAMES_G = {
    "phasso": ("संपर्क", M),
    "vedanā": ("अनुभूति", F),
    "saññā": ("पहचान", F),
    "cetanā": ("इरादा", M),
    "cittaṃ": ("मन", M),
    "vitakko": ("आरंभिक विचार", M),
    "vicāro": ("सतत विचार", M),
    "pīti": ("उल्लास", M),
    "sukhaṃ": ("सुख", M),
    "cittassekaggatā": ("मन की एकाग्रता", F),
    "saddhindriyaṃ": ("श्रद्धा की क्षमता", F),
    "vīriyindriyaṃ": ("उत्साह की क्षमता", F),
    "satindriyaṃ": ("सजगता की क्षमता", F),
    "samādhindriyaṃ": ("एकाग्रता की क्षमता", F),
    "paññindriyaṃ": ("प्रज्ञा की क्षमता", F),
    "manindriyaṃ": ("मन की क्षमता", F),
    "somanassindriyaṃ": ("प्रसन्नता की क्षमता", F),
    "jīvitindriyaṃ": ("जीवन-क्षमता", F),
    "sammādiṭṭhi": ("सही दृष्टि", F),
    "sammāsaṅkappo": ("सही संकल्प", M),
    "sammāvāyāmo": ("सही प्रयास", M),
    "sammāsati": ("सही सजगता", F),
    "sammāsamādhi": ("सही एकाग्रता", F),
    "saddhābalaṃ": ("श्रद्धा का बल", M),
    "vīriyabalaṃ": ("उत्साह का बल", M),
    "satibalaṃ": ("सजगता का बल", M),
    "samādhibalaṃ": ("एकाग्रता का बल", M),
    "paññābalaṃ": ("प्रज्ञा का बल", M),
    "hiribalaṃ": ("लज्जा का बल", M),
    "ottappabalaṃ": ("बुराई के डर का बल", M),
    "alobho": ("लोभ का अभाव", M),
    "adoso": ("द्वेष का अभाव", M),
    "amoho": ("मोह का अभाव", M),
    "anabhijjhā": ("लालच का अभाव", M),
    "abyāpādo": ("दुर्भावना का अभाव", M),
    "hirī": ("लज्जा", F),
    "ottappaṃ": ("बुराई का डर", M),
    "kāyapassaddhi": ("मानसिक काया की प्रशांति", F),
    "cittapassaddhi": ("मन की प्रशांति", F),
    "kāyalahutā": ("मानसिक काया का हल्कापन", M),
    "cittalahutā": ("मन का हल्कापन", M),
    "kāyamudutā": ("मानसिक काया की मृदुता", F),
    "cittamudutā": ("मन की मृदुता", F),
    "kāyakammaññatā": ("मानसिक काया की कार्य-योग्यता", F),
    "cittakammaññatā": ("मन की कार्य-योग्यता", F),
    "kāyapāguññatā": ("मानसिक काया की दक्षता", F),
    "cittapāguññatā": ("मन की दक्षता", F),
    "kāyujukatā": ("मानसिक काया का सीधापन", M),
    "cittujukatā": ("मन का सीधापन", M),
    "sati": ("सजगता", F),
    "sampajaññaṃ": ("स्पष्ट समझ", F),
    "samatho": ("शांति", F),
    "vipassanā": ("अंतर्दृष्टि", F),
    "paggāho": ("तत्परता", F),
    "avikkhepo": ("भटकाव का अभाव", M),
}
NAMES = {k: v[0] for k, v in NAMES_G.items()}
GENDER = {k: v[1] for k, v in NAMES_G.items()}
N = NAMES
HOTI = {M: "होता है", F: "होती है"}  # 'X hoti' in a list: 'there is X'

# ---- fixed synonym strings (Pāli string = Hindi string) -------------------------------
TAJJA = "उसके अनुरूप मन की चेतना के तत्व के संपर्क से उत्पन्न"
# "में" (in) rather than a genitive, so the frame needs no gender agreement with the string
G_KAYA = "अनुभूति के समूह, पहचान के समूह और मानसिक रचनाओं के समूह में"
G_CITTA = "चेतना के समूह में"
G_JIVITA = "उन अभौतिक परिघटनाओं की"
ROOT = "हितकर मूल"

STRINGS = {
    "phasso phusanā saṃphusanā saṃphusitattaṃ":
        "संपर्क, छूना, भली-भाँति छूना, भली-भाँति छुआ हुआ होना",
    "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        "मानसिक सुहावनापन, मानसिक सुख, मन के संपर्क से उत्पन्न सुहावना, सुखद अनुभव, "
        "मन के संपर्क से उत्पन्न सुहावनी, सुखद अनुभूति",
    "saññā sañjānanā sañjānitattaṃ":
        "पहचान, पहचानना, पहचान चुका होना",
    "cetanā sañcetanā cetayitattaṃ":
        "इरादा, इरादा करना, इरादा कर चुका होना",
    "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu":
        "मन, मानस, मानसिक क्रिया, हृदय, उज्ज्वलता, मानस, मन का इंद्रिय-क्षेत्र, मन की क्षमता, "
        "चेतना, चेतना का समूह, उसके अनुरूप मन की चेतना का तत्व",
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo":
        "सोचना, आरंभिक विचार, संकल्प, टिकाना, भली-भाँति टिकाना, मन को विषय की ओर ले जाना, सही संकल्प",
    "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā":
        "विचरण, सतत विचार, बार-बार विचरण, निकट विचरण, मन का विषय से जुड़े रहना, उसे लगातार निहारते रहना",
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa":
        "उल्लास, आनंद, आनंदित होना, प्रमुदित होना, हर्ष, महाहर्ष, तृप्ति, उमंग, मन का खिल उठना",
    "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ sammāsamādhi":
        "मन की स्थिरता, ठहराव, दृढ़ता, बिखराव का अभाव, भटकाव का अभाव, मन का न बिखरा होना, "
        "शांति, एकाग्रता की क्षमता, एकाग्रता का बल, सही एकाग्रता",
    "saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ":
        "श्रद्धा, श्रद्धा रखना, भरोसा करना, गहरी आस्था, श्रद्धा, श्रद्धा की क्षमता, श्रद्धा का बल",
    "cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā "
    "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo":
        "मानसिक रूप से उत्साह जगाना, आगे बढ़ना, प्रयत्न, उद्यम, प्रयास, जोश, लगन, शक्ति, धैर्य, "
        "ढीला न पड़ने वाला प्रयत्न, चाह को न छोड़ना, भार को न उतारना, भार को दृढ़ता से उठाए रखना, "
        "उत्साह, उत्साह की क्षमता, उत्साह का बल, सही प्रयास",
    # sati and paññā strings: verbatim from the approved Hindi pi-4 (^4-79, ^4-80)
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati":
        "सजगता, बार-बार स्मरण, पुनः स्मरण, सजगता, याद रखना, मन में धारण करना, उथला न होना, भूल न जाना, "
        "सजगता, सजगता की क्षमता, सजगता का बल, सही सजगता",
    "paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā "
    "paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
    "amoho dhammavicayo sammādiṭṭhi":
        "प्रज्ञा, जानना, छानबीन, गहरी छानबीन, परिघटनाओं की छानबीन, पहचानना, भली-भाँति पहचानना, "
        "हर पहलू को पहचानना, पांडित्य, कुशलता, निपुणता, विवेक, चिंतन, परख, व्यापक बुद्धि, मेधा, "
        "मार्गदर्शक बुद्धि, अंतर्दृष्टि, स्पष्ट समझ, अंकुश, प्रज्ञा, प्रज्ञा की क्षमता, प्रज्ञा का बल, "
        "प्रज्ञा रूपी शस्त्र, प्रज्ञा रूपी महल, प्रज्ञा रूपी आलोक, प्रज्ञा रूपी आभा, प्रज्ञा रूपी दीपक, "
        "प्रज्ञा रूपी रत्न, मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि",
    "āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        "आयु, टिके रहना, चलते रहना, चलाए रखना, गतिशील रहना, बने रहना, पालन, जीवन, जीवन-क्षमता",
    # hirī / ottappa strings: the approved pi-4 wording (^4-73, ^4-74), with परिघटनाओं for dhammānaṃ
    "hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        "जिस बात पर लज्जा आनी चाहिए, उस पर लज्जा आना, बुरी और हानिकर परिघटनाओं को अपनाने पर लज्जा आना",
    "ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        "जिस बात से डरना चाहिए, उससे डरना, बुरी और हानिकर परिघटनाओं को अपनाने से डरना",
    "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ":
        "लोभ का अभाव, लोभ न करना, लोभ से भरा न होना, राग का अभाव, राग न करना, राग से भरा न होना, "
        "लालच का अभाव, लोभ का अभाव, " + ROOT,
    "adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ":
        "द्वेष का अभाव, द्वेष न करना, द्वेष से भरा न होना, दुर्भावना का अभाव, दुर्भावना न रखना, "
        "द्वेष का अभाव, " + ROOT,
    "passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ":
        "प्रशांति, गहरी प्रशांति, शांत होना, पूरी तरह शांत होना, पूरी तरह शांत हो चुका होना",
    "lahutā lahupariṇāmatā adandhanatā avitthanatā":
        "हल्कापन, जल्दी बदल पाना, सुस्ती का अभाव, जड़ता का अभाव",
    "mudutā maddavatā akakkhaḷatā akathinatā":
        "मृदुता, कोमलता, कठोरता का अभाव, कड़ेपन का अभाव",
    "kammaññatā kammaññattaṃ kammaññabhāvo":
        "कार्य-योग्यता, कार्य-योग्य होना, कार्य-योग्य होने का भाव",
    "paguṇatā paguṇattaṃ paguṇabhāvo":
        "दक्षता, दक्ष होना, दक्ष होने का भाव",
    "ujutā ujukatā ajimhatā avaṅkatā akuṭilatā":
        "सीधाई, सीधापन, टेढ़ेपन का अभाव, वक्रता का अभाव, कुटिलता का अभाव",
}
S = {k.split()[0] if not k.startswith("cetasikaṃ sātaṃ") else "sāta": v for k, v in STRINGS.items()}
assert len(S) == len(STRINGS)
S_PHASSA = S["phasso"]
S_SUKHA = S["sāta"]
S_SANNA = S["saññā"]
S_CETANA = S["cetanā"]
S_CITTA = S["cittaṃ"]
S_VITAKKA = S["takko"]
S_VICARA = S["cāro"]
S_PITI = S["pīti"]
S_SAMADHI = S["cittassa"]
S_SADDHA = S["saddhā"]
S_VIRIYA = S["cetasiko"]
S_SATI = S["sati"]
S_PANNA = S["paññā"]
S_JIVITA = S["āyu"]
S_HIRI = S["hirīyati"]
S_OTTAPPA = S["ottappati"]
S_ALOBHA = S["alobho"]
S_ADOSA = S["adoso"]
S_PASSADDHI = S["passaddhi"]
S_LAHUTA = S["lahutā"]
S_MUDUTA = S["mudutā"]
S_KAMMANNATA = S["kammaññatā"]
S_PAGUNATA = S["paguṇatā"]
S_UJUTA = S["ujutā"]


def V(kind, sigla, text):
    label = "पाठभेद" if kind == "p" else "वर्तनी-भेद"
    return f" [{label} ({sigla}): {text}]"


# variant-bearing forms (first occurrences in ^1-5, ^1-13, ^1-19, ^1-33, ^1-40)
S_CETANA_V = S_CETANA + V("p", "Syā.", "sañcetayitattaṃ")
S_VIRIYA_V = (S_VIRIYA
              .replace("मानसिक रूप से उत्साह जगाना,",
                       "मानसिक रूप से उत्साह जगाना" + V("s", "Sī., Syā.", "viriyārambho") + ",", 1)
              .replace(" लगन,", " लगन" + V("s", "Sī.", "ussoḷhi") + ",", 1))
S_JIVITA_V = S_JIVITA.replace("गतिशील रहना,", "गतिशील रहना" + V("s", "Sī.", "irīyanā") + ",", 1)
S_ADOSA_V = S_ADOSA.replace("द्वेष से भरा न होना,",
                            "द्वेष से भरा न होना" + V("s", "Syā.", "adūsanā adūsitattaṃ") + ",", 1)
S_PASSADDHI_V = (S_PASSADDHI
                 .replace("गहरी प्रशांति,", "गहरी प्रशांति" + V("s", "Sī., Syā.", "paṭippassaddhi") + ",", 1)
                 .replace("पूरी तरह शांत होना,",
                          "पूरी तरह शांत होना" + V("s", "Sī., Syā.", "paṭippassambhanā") + ",", 1)
                 + V("s", "Sī., Syā.", "paṭippassambhitattaṃ"))
for a, b, n in ((S_CETANA, S_CETANA_V, 1), (S_VIRIYA, S_VIRIYA_V, 2), (S_JIVITA, S_JIVITA_V, 1),
                (S_ADOSA, S_ADOSA_V, 1), (S_PASSADDHI, S_PASSADDHI_V, 3)):
    assert b.count("[") == n, b

# ---- frames ----------------------------------------------------------------------------
OPEN_KAMA_KUSALA = "जिस समय इंद्रिय-सुखों के लोक से संबंधित हितकर मन उत्पन्न होता है"
ACC_SOMA_NANA = "जो प्रसन्नता के साथ होता है और ज्ञान से जुड़ा होता है"
ARAMMANA = ("जिसका विषय दृश्य रूप हो, या ध्वनि, या गंध, या स्वाद, या स्पर्श, या मन का विषय, "
            "या चाहे वह जिस किसी को भी विषय बनाए")
YEVAPANA_BODY = "उस समय जो भी दूसरी परस्पर-आश्रित रूप से उत्पन्न अभौतिक परिघटनाएँ होती हैं"


def YEVAPANA(item=KUSALA):
    """'ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā X.' (without 'or')"""
    return f"{YEVAPANA_BODY} {DASH} {ANSWER(item)}"


def Q(x):
    """'Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti?'"""
    return f"उस समय {x} क्या है?"


def A(s, x, pre=""):
    """'Yo/Yā/Yaṃ tasmiṃ samaye [pre] S – ayaṃ/idaṃ tasmiṃ samaye X hoti.'"""
    return f"उस समय {pre}जो {s} है {DASH} यह उस समय {x} है{DANDA}"


def QA(key, s, pre="", end=DANDA):
    a = A(s, N[key], pre)
    if end != DANDA:
        a = a[:-1] + end
    return Q(N[key]) + " " + a


def T(key, s):
    """with tajjāmanoviññāṇadhātusamphassaja-"""
    return QA(key, s, TAJJA + " ")


def KAYA(key, s):
    return QA(key, s, G_KAYA + " ")


def CITTA(key, s):
    return QA(key, s, G_CITTA + " ")


def JIVITA(key, s):
    """'Yo tesaṃ arūpīnaṃ dhammānaṃ S – idaṃ tasmiṃ samaye X hoti.' (no tasmiṃ samaye at the start)"""
    return Q(N[key]) + f" {G_JIVITA} जो {s} है {DASH} यह उस समय {N[key]} है{DANDA}"


def SHAME(key, s):
    """'Yaṃ tasmiṃ samaye hirīyati … / ottappati … – idaṃ/ayaṃ tasmiṃ samaye X hoti.'"""
    return Q(N[key]) + f" उस समय {s} {DASH} यह उस समय {N[key]} है{DANDA}"


def LIST_ITEM(key, var=""):
    """'X hoti' inside the list of ^1-1: 'there is X'."""
    return f"{N[key]}{var} {HOTI[GENDER[key]]}"


FRAMES = {
    "Katame dhammā kusalā?": QUESTION(KUSALA),
    "ime dhammā kusalā": ANSWER(KUSALA),
    "Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti?": Q("X"),
    "Yo/Yā/Yaṃ tasmiṃ samaye S – ayaṃ/idaṃ tasmiṃ samaye X hoti.": A("S", "X"),
    "Yā/Yaṃ tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajā/-jaṃ S – ayaṃ tasmiṃ samaye X hoti.":
        A("S", "X", TAJJA + " "),
    "Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa S – ayaṃ tasmiṃ samaye X hoti.":
        A("S", "X", G_KAYA + " "),
    "Yā tasmiṃ samaye viññāṇakkhandhassa S – ayaṃ tasmiṃ samaye X hoti.": A("S", "X", G_CITTA + " "),
    "Yo tesaṃ arūpīnaṃ dhammānaṃ S – idaṃ tasmiṃ samaye X hoti.":
        f"{G_JIVITA} जो S है {DASH} यह उस समय X है{DANDA}",
    "Yaṃ tasmiṃ samaye hirīyati… / ottappati… – idaṃ/ayaṃ tasmiṃ samaye X hoti.":
        f"उस समय S {DASH} यह उस समय X है{DANDA}",
    "Ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā.":
        "या " + YEVAPANA(),
    "Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti": OPEN_KAMA_KUSALA,
    "somanassasahagataṃ ñāṇasampayuttaṃ": ACC_SOMA_NANA,
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": ARAMMANA,
    "tasmiṃ samaye X hoti, Y hoti, …": "उस समय X होता है / होती है, Y होता है / होती है, …",
    "(in ^1-1, after the list) ; ye vā pana …": "; या " + YEVAPANA(),
}

# ---- ^1-1 ------------------------------------------------------------------------------
LIST_1_1 = [
    ("phasso", ""), ("vedanā", ""), ("saññā", ""), ("cetanā", ""), ("cittaṃ", ""), ("vitakko", ""),
    ("vicāro", ""), ("pīti", ""), ("sukhaṃ", ""), ("cittassekaggatā", ""), ("saddhindriyaṃ", ""),
    ("vīriyindriyaṃ", V("s", "Sī., Syā.", "viriyindriyaṃ")), ("satindriyaṃ", ""), ("samādhindriyaṃ", ""),
    ("paññindriyaṃ", ""), ("manindriyaṃ", ""), ("somanassindriyaṃ", ""), ("jīvitindriyaṃ", ""),
    ("sammādiṭṭhi", ""), ("sammāsaṅkappo", ""), ("sammāvāyāmo", ""), ("sammāsati", ""), ("sammāsamādhi", ""),
    ("saddhābalaṃ", ""), ("vīriyabalaṃ", V("s", "Sī., Syā.", "viriyabalaṃ")), ("satibalaṃ", ""),
    ("samādhibalaṃ", ""), ("paññābalaṃ", ""), ("hiribalaṃ", ""), ("ottappabalaṃ", ""), ("alobho", ""),
    ("adoso", ""), ("amoho", ""), ("anabhijjhā", ""), ("abyāpādo", ""), ("sammādiṭṭhi", ""), ("hirī", ""),
    ("ottappaṃ", ""), ("kāyapassaddhi", V("s", "Syā.", "kāyappassaddhi")),
    ("cittapassaddhi", V("s", "Syā.", "cittappassaddhi")), ("kāyalahutā", ""), ("cittalahutā", ""),
    ("kāyamudutā", ""), ("cittamudutā", ""), ("kāyakammaññatā", ""), ("cittakammaññatā", ""),
    ("kāyapāguññatā", ""), ("cittapāguññatā", ""), ("kāyujukatā", V("s", "Sī., Ka.", "kāyujjukatā")),
    ("cittujukatā", V("s", "Sī., Ka.", "cittujjukatā")), ("sati", ""), ("sampajaññaṃ", ""), ("samatho", ""),
    ("vipassanā", ""), ("paggāho", ""), ("avikkhepo", ""),
]
SEG_1_1 = (
    QUESTION(KUSALA) + " " + OPEN_KAMA_KUSALA + ", " + ACC_SOMA_NANA + ", " + ARAMMANA + ", उस समय "
    + ", ".join(LIST_ITEM(k, v) for k, v in LIST_1_1)
    + "; या " + YEVAPANA()
)

# ---- segments in source order --------------------------------------------------------
SEGMENTS = [
    ("1-1-0", [H_CH2]),
    ("1-1-1-0", [H_KAMA_KUSALA]),
    ("1-1-1-1-0", [H_PADA]),
    ("1-1", [SEG_1_1]),
    ("1-2", [QA("phasso", S_PHASSA)]),
    ("1-3", [T("vedanā", S_SUKHA)]),
    ("1-4", [T("saññā", S_SANNA)]),
    ("1-5", [T("cetanā", S_CETANA_V)]),
    ("1-6", [QA("cittaṃ", S_CITTA)]),
    ("1-7", [QA("vitakko", S_VITAKKA)]),
    ("1-8", [QA("vicāro", S_VICARA)]),
    ("1-9", [QA("pīti", S_PITI)]),
    ("1-10", [QA("sukhaṃ", S_SUKHA)]),
    ("1-11", [QA("cittassekaggatā", S_SAMADHI)]),
    ("1-12", [QA("saddhindriyaṃ", S_SADDHA)]),
    ("1-13", [QA("vīriyindriyaṃ", S_VIRIYA_V)]),
    ("1-14", [QA("satindriyaṃ", S_SATI)]),
    ("1-15", [QA("samādhindriyaṃ", S_SAMADHI)]),
    ("1-16", [QA("paññindriyaṃ", S_PANNA)]),
    ("1-17", [QA("manindriyaṃ", S_CITTA)]),
    ("1-18", [QA("somanassindriyaṃ", S_SUKHA)]),
    ("1-19", [JIVITA("jīvitindriyaṃ", S_JIVITA_V)]),
    ("1-20", [QA("sammādiṭṭhi", S_PANNA)]),
    ("1-21", [QA("sammāsaṅkappo", S_VITAKKA)]),
    ("1-22", [QA("sammāvāyāmo", S_VIRIYA)]),
    ("1-23", [QA("sammāsati", S_SATI)]),
    ("1-24", [QA("sammāsamādhi", S_SAMADHI)]),
    ("1-25", [QA("saddhābalaṃ", S_SADDHA)]),
    ("1-26", [QA("vīriyabalaṃ", S_VIRIYA)]),
    ("1-27", [QA("satibalaṃ", S_SATI)]),
    ("1-28", [QA("samādhibalaṃ", S_SAMADHI)]),
    ("1-29", [QA("paññābalaṃ", S_PANNA)]),
    ("1-30", [SHAME("hiribalaṃ", S_HIRI)]),
    ("1-31", [SHAME("ottappabalaṃ", S_OTTAPPA)]),
    ("1-32", [QA("alobho", S_ALOBHA)]),
    ("1-33", [QA("adoso", S_ADOSA_V, end="?")]),  # the Pāli ends this answer with "?" (source slip, kept)
    ("1-34", [QA("amoho", S_PANNA + ", " + N["amoho"] + ", " + ROOT)]),
    ("1-35", [QA("anabhijjhā", S_ALOBHA)]),
    ("1-36", [QA("abyāpādo", S_ADOSA)]),
    ("1-37", [QA("sammādiṭṭhi", S_PANNA)]),
    ("1-38", [SHAME("hirī", S_HIRI)]),
    ("1-39", [SHAME("ottappaṃ", S_OTTAPPA)]),
    ("1-40", [KAYA("kāyapassaddhi", S_PASSADDHI_V)]),
    ("1-41", [CITTA("cittapassaddhi", S_PASSADDHI)]),
    ("1-42", [KAYA("kāyalahutā", S_LAHUTA)]),
    ("1-43", [CITTA("cittalahutā", S_LAHUTA)]),
    ("1-44", [KAYA("kāyamudutā", S_MUDUTA)]),
    ("1-45", [CITTA("cittamudutā", S_MUDUTA)]),
    ("1-46", [KAYA("kāyakammaññatā", S_KAMMANNATA)]),
    ("1-47", [CITTA("cittakammaññatā", S_KAMMANNATA)]),
    ("1-48", [KAYA("kāyapāguññatā", S_PAGUNATA)]),
    ("1-49", [CITTA("cittapāguññatā", S_PAGUNATA)]),
    ("1-50", [KAYA("kāyujukatā", S_UJUTA)]),
    ("1-51", [CITTA("cittujukatā", S_UJUTA)]),
    ("1-52", [QA("sati", S_SATI)]),
    ("1-53", [QA("sampajaññaṃ", S_PANNA)]),
    ("1-54", [QA("samatho", S_SAMADHI)]),
    ("1-55", [QA("vipassanā", S_PANNA)]),
    ("1-56", [QA("paggāho", S_VIRIYA)]),
    ("1-57", [QA("avikkhepo", S_SAMADHI), "या " + YEVAPANA(), END_PADA, END_BHANA1]),
]


def build():
    out = []
    for bid, lines in SEGMENTS:
        lines = list(lines)
        lines[-1] += f" ^{bid}"
        out.append("\n".join(lines))
    return "\n\n".join(out) + "\n"


TEXT = build()
assert "—" not in TEXT and ":-" not in TEXT

if __name__ == "__main__":
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT)
