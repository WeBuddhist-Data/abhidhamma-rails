"""Build the Hindi plain zero-shot of pi-1 parts 4-02 and 4-03 (Nikkhepakaṇḍa, continued).

usage: python -I -X utf8 build_4-02_4-03_hi.py
Mirrors the English builders build_4-02.py and build_4-01_4-03.py (build_403).
Matrix item names and the question/answer frames come from build_matika_hi (MATRIX_ITEMS_HI,
BARE, QUESTION, ANSWER); synonym strings from build_ch2_01_sample_hi. Every recurring formula
is a constant below, so every repeat is byte-identical. Runs self-checks and writes both parts.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_hi as M          # noqa: E402  (importing does not write anything)
import build_ch2_01_sample_hi as C   # noqa: E402

ROOT = HERE.parents[3]
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters"

D = C.DASH          # "–", only where the Pāli has one
DANDA = M.DANDA     # "।"
V = M.V             # variant bracket (with leading space)

# ---- matrix items ------------------------------------------------------------------------
VAR = re.compile(r"\s*\[[^\]]*\]")


def _norm(p):
    p = VAR.sub("", p).strip().rstrip(".")
    p = " ".join(w for w in p.split() if w != "dhammā")
    p = p.replace(" kho pana", "")
    return re.sub(r"pi$", "", p)


ITEM = {}
_first = {}
_kho = {bid for bid, l, p, h in M.MATRIX_ITEMS_HI if l == "क" and "kho pana" in p}
for bid, letter, pali, hi in sorted(M.MATRIX_ITEMS_HI, key=lambda t: t[0].startswith("1-M2")):
    key = _norm(pali)
    if letter == "क":
        _first[bid] = pali.split()[0]
    elif bid in _kho:
        key = _first[bid] + " " + key
    ITEM[key] = M.BARE[(bid, letter)]  # pair entries come last and win (identical wording anyway)


def I(p):
    assert p in ITEM, p
    return ITEM[p]


def NM(mid, l):
    """bare matrix name by block id, e.g. NM('2-109', 'क')"""
    return M.BARE[(f"1-M{mid}", l)]


def ADJ(mid, l):
    """the qualifier of '<qualifier> परिघटनाएँ'"""
    n = NM(mid, l)
    assert n.endswith(" परिघटनाएँ"), n
    return n[:-len(" परिघटनाएँ")]


def Q(p):
    return M.QUESTION(I(p))


def E(p):
    return f"{D} {M.ANSWER(I(p))}"


def L(p):
    return M.ANSWER(I(p))


def TQ(x):
    """Tattha katamo/katamā/katamaṃ X?  (pi-4 wording)"""
    return f"यहाँ {x} क्या है?"


def CALLED(x):
    """– ayaṃ/idaṃ vuccati X.  (pi-4 wording)"""
    return f"{D} इसे {x} कहा जाता है{DANDA}"


def T(x, body):
    return f"{TQ(x)} {body} {CALLED(x)}"


def QA(p, body):
    return f"{Q(p)} {body} {E(p)}"


def J(s):
    """Yo/Yā/Yaṃ S  ->  'जो S है' (sample frame A, pi-4 ^4-59/^4-79)"""
    return f"जो {s} है"


def EVA(first, gender, rest):
    """yo/yā/yaṃ evarūpo/-ā/-aṃ X …  ->  'जो इस प्रकार का/की X है, …' (pi-4 ^4-50/^4-62)"""
    ka = "का" if gender == "m" else "की"
    return f"जो इस प्रकार {ka} {first} है, {rest}"


# ---- fixed phrases ------------------------------------------------------------------------
GROUP_H = {bid.replace("1-M-2-", "1-3-2-"): v[0] for bid, v in M.GROUPS.items()}
H_SUTTANTA_NIKKHEPA = "#### उपदेशों के दो-दो के वर्गीकरणों का सारांश"
END_BHANA2 = "सारांश के अध्याय का दूसरा पाठ-खंड।"
END_ABHI = "अभिधम्म के दो-दो के वर्गीकरण।"
END_NIKKHEPA = "सारांश का अध्याय पूरा हुआ।"

VEDANA, SANNA, SANKHARA, VINNANA, RUPAK = ("अनुभूति का समूह", "पहचान का समूह", "मानसिक रचनाओं का समूह",
                                          "चेतना का समूह", "भौतिक रूप का समूह")
VV = f"{VEDANA}… {VINNANA}"                       # vedanākkhandho…pe… viññāṇakkhandho
RV = f"{RUPAK}… {VINNANA}"                        # rūpakkhandho…pe… viññāṇakkhandho
FEEL3 = f"{VEDANA}, {SANNA}, {SANKHARA}"
FOUR = f"{FEEL3}, {VINNANA}"
PERC3 = f"{SANNA}, {SANKHARA}, {VINNANA}"
ASANKHATA = "अनिर्मित तत्व"                        # asaṅkhatā dhātu
RA = f"सारा भौतिक रूप और {ASANKHATA}"              # sabbañca rūpaṃ, asaṅkhatā ca dhātu
MIND_RA = f"मन, {RA}"                              # cittañca, sabbañca rūpaṃ, asaṅkhatā ca dhātu
MIND_REM = f"मन, शेष भौतिक रूप और {ASANKHATA}"     # cittañca, avasesañca rūpaṃ, asaṅkhatā ca dhātu
LOKUT = f"अस्तित्व के लोकों में न समाए हुए मार्ग, मार्गों के फल और {ASANKHATA}"
PATHS4 = "अस्तित्व के लोकों में न समाए हुए चार मार्ग"   # cattāro maggā apariyāpannā
P_ = "परिघटनाएँ"
KUA = f"हितकर, हानिकर और नैतिक रूप से अनिर्धारित {P_}"   # kusalākusalābyākatā dhammā
KA = f"हितकर और नैतिक रूप से अनिर्धारित {P_}"            # kusalābyākatā dhammā
KU = f"हितकर और हानिकर {P_}"                           # kusalākusalā dhammā
SASAVA = "मन के मैलों का विषय बनने वाली"                 # sāsavā
SPH = {"k": "इंद्रिय-सुखों के लोक से संबंधित", "r": "सूक्ष्म भौतिक लोक से संबंधित",
       "a": "अभौतिक लोक से संबंधित"}


def whether(keys, pron="वे", verb="हों", notincl="न समाई हुई"):
    """kāmāvacarā, rūpāvacarā, arūpāvacarā[, apariyāpannā] -> 'चाहे वे … हों, … या … हों'"""
    parts = [f"{SPH[k]} {verb}" if k != "p" else f"अस्तित्व के लोकों में {notincl} {verb}" for k in keys]
    return f"चाहे {pron} " + ", ".join(parts[:-1]) + " या " + parts[-1]


W4 = whether("krap")
W3 = whether("kra")
PL3 = whether("krp", "वह", "हो", "न समाया हुआ")     # bhūmi (स्तर, m. sg.) in kāma/rūpa/apariyāpanna
PL4 = whether("krap", "वह", "हो", "न समाया हुआ")

TADEKA = "उनके साथ-साथ रहने वाले मन के क्लेश"                      # tadekaṭṭhā ca kilesā
TAMSAMP = f"उनसे जुड़ा {VV}"                                      # taṃsampayutto vedanākkhandho…pe…
TAMSAM = "उनसे उत्पन्न शरीर का कर्म, वाणी का कर्म, मन का कर्म"      # taṃsamuṭṭhānaṃ kāyakammaṃ …
ROOT_TAIL = f"{TADEKA}, {TAMSAMP}, {TAMSAM}"
ROOTS3 = "तीन हानिकर मूल"                                         # tīṇi akusalamūlāni
GHD = "लोभ, द्वेष, मोह"
REMAINING_GHD = f"शेष {GHD}"                                       # avaseso lobho doso moho
KUSALAMULA_A = "हानिकर मूल"                                        # akusalamūlaṃ (kusalamūlaṃ = हितकर मूल)

# ---- answer frames (mirror build_4-02.py) ----------------------------------------------
def F_NO(p):
    """Te dhamme ṭhapetvā avasesā kusalākusalābyākatā dhammā kāmāvacarā, …, apariyāpannā; vedanā…viññāṇa;
    sabbañca rūpaṃ, asaṅkhatā ca dhātu"""
    return f"{Q(p)} उन परिघटनाओं को छोड़कर शेष {KUA}, {W4}; {VV}; {RA} {E(p)}"


def F_SAS(p):
    """Sāsavā kusalākusalābyākatā dhammā kāmāvacarā, rūpāvacarā, arūpāvacarā; rūpa…viññāṇa"""
    return f"{Q(p)} {SASAVA} {KUA}, {W3}; {RV} {E(p)}"


def F_LOKUT(p):
    """Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu"""
    return f"{Q(p)} {LOKUT} {E(p)}"


def F_SAMP(p):
    """Tehi dhammehi ye dhammā sampayuttā vedanā…viññāṇa"""
    return f"{Q(p)} उन परिघटनाओं से जुड़ी परिघटनाएँ: {VV} {E(p)}"


def F_VIPP(p):
    """Tehi dhammehi ye dhammā vippayuttā vedanā…viññāṇa; sabbañca rūpaṃ, asaṅkhatā ca dhātu"""
    return f"{Q(p)} उन परिघटनाओं से अलग परिघटनाएँ: {VV}; {RA} {E(p)}"


def F_NIYA_NOT(p, rel):
    """Tehi dhammehi ye dhammā X-niyā, te dhamme ṭhapetvā avasesā sāsavā kusalākusalābyākatā …; rūpa…viññāṇa"""
    return (f"{Q(p)} {rel} परिघटनाओं में से उन परिघटनाओं को छोड़कर शेष {SASAVA} {KUA}, {W3}; {RV} "
            f"{E(p)}")


def F_NOT_OF(p, rel):
    """Tehi dhammehi ye dhammā sampayuttā/saṃkiliṭṭhā, te dhamme ṭhapetvā vedanā…viññāṇa"""
    return f"{Q(p)} {rel} परिघटनाओं में से उन परिघटनाओं को छोड़कर {VV} {E(p)}"


def F_VIPP_NIYA(p, kus):
    """Tehi dhammehi ye dhammā vippayuttā sāsavā kusal(ākusal)ābyākatā …; rūpa…viññāṇa"""
    return f"{Q(p)} उन परिघटनाओं से अलग, {SASAVA} {kus}, {W3}; {RV} {E(p)}"


REL_OBJ = "उन परिघटनाओं का विषय बनने वाली"        # tehi dhammehi ye dhammā nīvaraṇiyā / parāmaṭṭhā / upādāniyā
REL_SAMKILESIKA = "उन परिघटनाओं की ओर ले जाने वाली"
REL_SAMP = "उन परिघटनाओं से जुड़ी"
REL_SAMKILITTHA = "उन परिघटनाओं से मलिन"

# ---- definition strings (bare; the frames add 'जो … है') ------------------------------
# Yo kāmesu kāmacchando kāmarāgo kāmanandī kāmataṇhā kāmasineho kāmapariḷāho kāmamucchā kāmajjhosānaṃ
S_KAMA = ("इंद्रिय-सुखों के प्रति जो इंद्रिय-सुखों की चाह, इंद्रिय-सुखों का राग, इंद्रिय-सुखों का आनंद, "
          "इंद्रिय-सुखों की तृष्णा, इंद्रिय-सुखों का स्नेह, इंद्रिय-सुखों की जलन, इंद्रिय-सुखों का नशा, "
          "इंद्रिय-सुखों में डूबे रहना है")
# Yo bhavesu bhavachando…pe… bhavajjhosānaṃ (same pattern)
S_BHAVA_PE = "अस्तित्वों के प्रति जो अस्तित्व की चाह… अस्तित्व में डूबे रहना है"

# Anatthaṃ me acarīti āghāto jāyati … aṭṭhāne vā pana āghāto jāyati.
_AG = "यह सोचकर आक्रोश उत्पन्न होता है"
AGHATA = (f"“उसने मेरा अहित किया” {_AG}, “वह मेरा अहित कर रहा है” {_AG}, “वह मेरा अहित करेगा” {_AG}, "
          f"“उसने मेरे प्रिय और मनभावन व्यक्ति का अहित किया… अहित कर रहा है… अहित करेगा” {_AG}, "
          f"“उसने मेरे अप्रिय और अनचाहे व्यक्ति का हित किया… हित कर रहा है… हित करेगा” {_AG}, "
          f"या बिना कारण ही आक्रोश उत्पन्न होता है{DANDA}")
# Yo evarūpo cittassa āghāto paṭighāto paṭighaṃ … anattamanatā cittassa  (tail = pi-4 ^4-45 kodha string)
KODHA_PI4 = ("क्रोध, क्रोध करना, क्रुद्ध होना, द्वेष, द्वेष करना, द्वेष से भरा होना, दुर्भावना, दुर्भावना रखना, "
             "दुर्भावना से भरा होना, विरोध, प्रतिविरोध, उग्रता, कटु वचन, मन की अप्रसन्नता")
S_DOSA = EVA("मन का आक्रोश", "m", "प्रतिघात, चिढ़, प्रतिविरोध, कोप, प्रकोप, भारी प्रकोप, द्वेष, गहरा द्वेष, "
             "भारी द्वेष, मन की दुर्भावना, मन में द्वेष, " + KODHA_PI4)
DOSA = AGHATA + " " + S_DOSA

# Yā cittassa akallatā akammaññatā olīyanā sallīyanā līnaṃ līyanā līyitattaṃ thinaṃ thiyanā thiyitattaṃ cittassa
S_THINA = J("मन की अस्वस्थता, कार्य-अयोग्यता, ढीला पड़ना, सिकुड़ जाना, शिथिलता, शिथिल होना, शिथिल हो चुका होना, "
            "आलस्य, आलसी होना, मन का आलस्य से भरा होना")
# Yā kāyassa akallatā akammaññatā onāho pariyonāho antosamorodho middhaṃ soppaṃ pacalāyikā soppaṃ supanā supitattaṃ
S_MIDDHA = J("मानसिक काया की अस्वस्थता, कार्य-अयोग्यता, ढक जाना, पूरी तरह ढक जाना, भीतर ही भीतर घिर जाना, "
             "तंद्रा, नींद, ऊँघ, नींद, सोना, सोया हुआ होना")
# Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa
S_UDDHACCA = J("मन की बेचैनी, अशांति, मन का भटकाव, मन का डाँवाडोल होना")
# Akappiye kappiyasaññitā, … Yaṃ evarūpaṃ kukkuccaṃ kukkuccāyanā kukkuccāyitattaṃ cetaso vippaṭisāro manovilekho
KUKKUCCA = ("जो अनुचित है उसे उचित समझना, जो उचित है उसे अनुचित समझना, जो निर्दोष है उसे निंदनीय समझना, "
            "जो निंदनीय है उसे निर्दोष समझना। "
            + EVA("पछतावा", "m", "पछताना, पछतावे से भरा होना, मन की ग्लानि, मन को कुरेदना"))

# Satthari kaṅkhati vicikicchati, … idappaccayatā paṭiccasamuppannesu dhammesu kaṅkhati vicikicchati
_KV = "शंका और संशय करता है"
VICI_HEAD = f"कोई व्यक्ति गुरु के विषय में {_KV}"
VICI_INTRO = (f"{VICI_HEAD}, शिक्षा के विषय में {_KV}, संघ के विषय में {_KV}, प्रशिक्षण के विषय में {_KV}, "
              f"अतीत के विषय में {_KV}, भविष्य के विषय में {_KV}, अतीत और भविष्य दोनों के विषय में {_KV}, "
              f"कार्य-कारण के नियम से परस्पर-आश्रित रूप से उत्पन्न परिघटनाओं के विषय में {_KV}")
# yā evarūpā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo
# anekaṃsaggāho āsappanā parisappanā apariyogāhanā thambhitattaṃ cittassa manovilekho
VICI_TAIL = "मन की जड़ता, मन को कुरेदना"
VICI_STR = EVA("शंका", "f", "शंका करना, शंका से भरा होना, मति-भ्रम, संशय, दुविधा, दोराहा, संदेह, "
               "किसी एक बात पर न टिक पाना, डगमगाना, बार-बार डगमगाना, गहराई में न उतर पाना, " + VICI_TAIL)
VICI_SHORT_BODY = f"{VICI_HEAD}… {VICI_TAIL}"     # Satthari kaṅkhati vicikicchati…pe… thambhitattaṃ cittassa manovilekho

# Dukkhe aññāṇaṃ, … idappaccayatā paṭiccasamuppannesu dhammesu aññāṇaṃ
_NJ = "के विषय में न जानना"
MOHA_INTRO = (f"दुःख {_NJ}, दुःख की उत्पत्ति {_NJ}, दुःख के अंत {_NJ}, दुःख के अंत की ओर ले जाने वाले रास्ते {_NJ}, "
              f"अतीत {_NJ}, भविष्य {_NJ}, अतीत और भविष्य दोनों {_NJ}, "
              f"कार्य-कारण के नियम से परस्पर-आश्रित रूप से उत्पन्न परिघटनाओं {_NJ}")
# yaṃ evarūpaṃ aññāṇaṃ adassanaṃ … avijjālaṅgī moho akusalamūlaṃ  (pi-4 ^4-60, with yoga = जकड़न,
# akusalamūla = हानिकर मूल)
MOHA_LIST = ["न जानना", "न देखना", "सत्य तक न पहुँचना", "बोध न होना", "पूर्ण बोध न होना", "भेद न पाना",
             "न समेट पाना", "गहराई में न उतर पाना", "निष्पक्ष रूप से न देखना", "पुनः विचार न करना",
             "प्रत्यक्ष न करना", "दुर्बुद्धि", "मूर्खता", "स्पष्ट समझ का अभाव", "मोह", "गहरा मोह", "घोर मोह",
             "अज्ञान", "अज्ञान की बाढ़", "अज्ञान की जकड़न", "अज्ञान की सुप्त प्रवृत्ति", "अज्ञान का आवेश",
             "अज्ञान की रुकावट", "मोह", KUSALAMULA_A]
MOHA_STR = EVA(MOHA_LIST[0], "m", ", ".join(MOHA_LIST[1:]))
MOHA_PE = J(f"{MOHA_LIST[0]}, {MOHA_LIST[1]}… " + ", ".join(MOHA_LIST[-3:]))  # Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ

# Sassato lokoti vā, … neva hoti na na hoti tathāgato paraṃ maraṇāti vā  (pi-5 ^5-708 wording)
VIEWS10 = ", या ".join(f"“{v}”" for v in (
    "लोक शाश्वत है", "लोक शाश्वत नहीं है", "लोक सीमित है", "लोक असीम है", "जो जीव है, वही शरीर है",
    "जीव अलग है, शरीर अलग है", "मृत्यु के बाद तथागत रहता है", "मृत्यु के बाद तथागत नहीं रहता",
    "मृत्यु के बाद तथागत रहता भी है और नहीं भी रहता", "मृत्यु के बाद तथागत न रहता है, न नहीं रहता"))
# yā evarūpā diṭṭhi diṭṭhigataṃ … vipariyāsaggāho  (pi-4 ^4-62; patiṭṭhāho, parāmāso adapted)
DITTHI_HEAD = "दृष्टि में पड़ जाना"
DITTHI_TAIL = "उलटी पकड़"
DITTHI_STR = EVA("दृष्टि", "f", f"{DITTHI_HEAD}, दृष्टि का घना जंगल, दृष्टि का बीहड़, दृष्टि का टेढ़ापन, "
                 "दृष्टि की छटपटाहट, दृष्टि का बंधन, पकड़, अड़ जाना, आग्रह, ग़लत धारणा, कुमार्ग, ग़लत रास्ता, "
                 f"ग़लतपन, मतवादों का अड्डा, {DITTHI_TAIL}")
DITTHI_SHORT = EVA("दृष्टि", "f", f"{DITTHI_HEAD}… {DITTHI_TAIL}")   # diṭṭhigataṃ…pe… vipariyāsaggāho

# Natthi dinnaṃ, … pavedentīti  (pi-4 ^4-62 wording)
NATTHI = ("“दान व्यर्थ है, यज्ञ व्यर्थ है, आहुति व्यर्थ है; अच्छे और बुरे कर्मों का कोई फल या परिणाम नहीं होता; "
          "न यह लोक है, न परलोक है; न माता है, न पिता है; स्वतः जन्म लेने वाले प्राणी नहीं होते; संसार में ऐसे "
          "श्रमण और ब्राह्मण नहीं हैं जो सही ढंग से पहुँचे हुए{v} और सही ढंग से साधना करने वाले हों, जो इस लोक और "
          "परलोक को स्वयं उच्च ज्ञान से जानकर और साक्षात्कार करके बताते हों”")
NATTHI_V = NATTHI.format(v=V("p", "Ka.", "samaggatā"))
NATTHI_PLAIN = NATTHI.format(v="")
# Atthi dinnaṃ, … pavedentīti  (pi-4 ^4-82 wording)
ATTHI = ("“दान व्यर्थ नहीं है, यज्ञ व्यर्थ नहीं है, आहुति व्यर्थ नहीं है; अच्छे और बुरे कर्मों का फल और परिणाम होता "
         "है; यह लोक है, परलोक है; माता है, पिता है; स्वतः जन्म लेने वाले प्राणी होते हैं; संसार में ऐसे श्रमण और "
         "ब्राह्मण हैं जो सही ढंग से पहुँचे हुए और सही ढंग से साधना करने वाले हैं, जो इस लोक और परलोक को स्वयं उच्च "
         "ज्ञान से जानकर और साक्षात्कार करके बताते हैं”")
# Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi, vatena suddhi, sīlabbatena suddhīti
SILABBATA = ("इस शिक्षा के बाहर के श्रमणों और ब्राह्मणों का यह मत कि “कर्मकांड से शुद्धि होती है, व्रत से शुद्धि होती है, "
             "कर्मकांड और व्रत से शुद्धि होती है”")
# Idha assutavā puthujjano … viññāṇasmiṃ vā attānaṃ.
SAKKAYA = ("इस संसार में कोई अशिक्षित साधारण व्यक्ति, जो आर्यों को नहीं देखता, आर्यों की शिक्षा से अनजान है, आर्यों की "
           "शिक्षा में अनुशासित नहीं है, जो सज्जनों को नहीं देखता, सज्जनों की शिक्षा से अनजान है, सज्जनों की शिक्षा में "
           "अनुशासित नहीं है, भौतिक रूप को आत्मा मानता है, या आत्मा को भौतिक रूप वाला, या आत्मा में भौतिक रूप को, "
           "या भौतिक रूप में आत्मा को। अनुभूति को… पहचान को… मानसिक रचनाओं को… चेतना को आत्मा मानता है, या आत्मा "
           "को चेतना वाला, या आत्मा में चेतना को, या चेतना में आत्मा को।")

# Yo rāgo sārāgo … abhijjhā lobho akusalamūlaṃ
LOBHA_PALI = ("Yo rāgo sārāgo anunayo anurodho nandī nandīrāgo cittassa sārāgo icchā mucchā ajjhosānaṃ gedho "
              "paligedho saṅgo paṅko ejā māyā janikā sañjananī sibbinī jālinī saritā visattikā suttaṃ visaṭā "
              "āyūhinī dutiyā paṇidhi bhavanetti vanaṃ vanatho santhavo sineho apekkhā paṭibandhu āsā āsisanā "
              "āsisitattaṃ rūpāsā saddāsā gandhāsā rasāsā phoṭṭhabbāsā lābhāsā dhanāsā puttāsā jīvitāsā jappā "
              "pajappā abhijappā jappā jappanā jappitattaṃ loluppaṃ loluppāyanā loluppāyitattaṃ pucchañjikatā "
              "sādhukamyatā adhammarāgo visamalobho nikanti nikāmanā patthanā pihanā sampatthanā kāmataṇhā "
              "bhavataṇhā vibhavataṇhā rūpataṇhā arūpataṇhā nirodhataṇhā rūpataṇhā saddataṇhā gandhataṇhā "
              "rasataṇhā phoṭṭhabbataṇhā dhammataṇhā ogho yogo gantho upādānaṃ āvaraṇaṃ nīvaraṇaṃ chādanaṃ "
              "bandhanaṃ upakkileso anusayo pariyuṭṭhānaṃ latā vevicchaṃ dukkhamūlaṃ dukkhanidānaṃ dukkhappabhavo "
              "mārapāso mārabaḷisaṃ māravisayo taṇhānadī taṇhājālaṃ taṇhāgaddulaṃ taṇhāsamuddo abhijjhā lobho "
              "akusalamūlaṃ")
LOBHA = [
    "राग", "प्रबल राग", "झुकाव", "अनुकूलता", "आनंद", "आनंद और राग", "मन का प्रबल राग", "इच्छा", "नशा",
    "डूबे रहना", "भूख", "गहरी भूख", "लगाव", "कीचड़", "हलचल", "कपट", "जन्म देने वाली", "उत्पन्न करने वाली",
    "सीने वाली", "जाल बिछाने वाली", "धारा", "उलझाने वाली", "धागा", "फैली हुई", "जुटाने वाली", "साथिन",
    "आकांक्षा", "अस्तित्व की ओर ले जाने वाली डोर", "वन", "झाड़-झंखाड़", "घनिष्ठता", "स्नेह", "अपेक्षा", "नाता",
    "आशा", "आशा करना", "आशा से भरा होना", "दृश्य रूपों की आशा", "ध्वनियों की आशा", "गंधों की आशा",
    "स्वादों की आशा", "स्पर्शों की आशा", "लाभ की आशा", "धन की आशा", "संतान की आशा", "जीवन की आशा", "ललक",
    "तीव्र ललक", "अत्यधिक ललक", "ललक", "ललक रखना", "ललक से भरा होना", "लोलुपता", "लोलुप होना",
    "लोलुपता से भरा होना", "चापलूसी", "बढ़िया चीज़ों की चाह", "अनुचित राग", "अन्यायपूर्ण लोभ", "रुचि", "कामना",
    "चाहना", "ललचाना", "गहरी चाहना", "इंद्रिय-सुखों की तृष्णा", "अस्तित्व की तृष्णा", "अनस्तित्व की तृष्णा",
    "सूक्ष्म भौतिक अस्तित्व की तृष्णा", "अभौतिक अस्तित्व की तृष्णा", "निरोध की तृष्णा", "दृश्य रूपों की तृष्णा",
    "ध्वनियों की तृष्णा", "गंधों की तृष्णा", "स्वादों की तृष्णा", "स्पर्शों की तृष्णा", "मन के विषयों की तृष्णा",
    "बाढ़", "जकड़न", "गाँठ", "आसक्ति", "आवरण", "बाधा", "ढक्कन", "बेड़ी", "मलिनता", "सुप्त प्रवृत्ति", "आवेश",
    "लता", "लोभीपन", "दुःख का मूल", "दुःख का स्रोत", "दुःख का उद्गम", "मार का फंदा", "मार का काँटा",
    "मार का क्षेत्र", "तृष्णा की नदी", "तृष्णा का जाल", "तृष्णा का पट्टा", "तृष्णा का सागर", "लालच", "लोभ",
    KUSALAMULA_A]
assert len(LOBHA) == len(LOBHA_PALI.split()) - 2, (len(LOBHA), len(LOBHA_PALI.split()))  # minus Yo, cittassa
S_LOBHA = J(", ".join(LOBHA))
# Seyyohamasmīti māno, … ketukamyatā cittassa
MANA = ("“मैं श्रेष्ठ हूँ” यह अहंकार, “मैं बराबर हूँ” यह अहंकार, “मैं हीन हूँ” यह अहंकार; "
        + EVA("अहंकार", "m", "स्वयं को कुछ मानना, स्वयं को कुछ मान बैठना, घमंड, अकड़, झंडा उठाना, स्वयं को ऊँचा रखना, "
              "मन की ध्वजा फहराने की चाह"))
# Yaṃ na hirīyati hiriyitabbena, na hirīyati … / Yaṃ na ottappati …  (negations of C.S_HIRI / C.S_OTTAPPA)
AHIRIKA = "जिस बात पर लज्जा आनी चाहिए, उस पर लज्जा न आना, बुरी और हानिकर परिघटनाओं को अपनाने पर लज्जा न आना"
ANOTTAPPA = "जिस बात से डरना चाहिए, उससे न डरना, बुरी और हानिकर परिघटनाओं को अपनाने से न डरना"
assert AHIRIKA.replace(" न आना", " आना") == C.S_HIRI and ANOTTAPPA.replace("न डरना", "डरना") == C.S_OTTAPPA

# ---- names ---------------------------------------------------------------------------------
N_NIV = {
    "kāmacchandanīvaraṇa": "इंद्रिय-सुखों की चाह की बाधा",
    "byāpādanīvaraṇa": "दुर्भावना की बाधा",
    "thinamiddhanīvaraṇa": "आलस्य और तंद्रा की बाधा",
    "uddhaccakukkuccanīvaraṇa": "बेचैनी और पछतावे की बाधा",
    "vicikicchānīvaraṇa": "संशय की बाधा",
    "avijjānīvaraṇa": "अज्ञान की बाधा",
    "uddhaccanīvaraṇa": "बेचैनी की बाधा",
    "kukkuccanīvaraṇa": "पछतावे की बाधा",
}
N_UPA = {
    "kāmupādāna": "इंद्रिय-सुखों के प्रति आसक्ति",
    "diṭṭhupādāna": "दृष्टियों के प्रति आसक्ति",
    "sīlabbatupādāna": "कर्मकांडों और व्रतों के प्रति आसक्ति",
    "attavādupādāna": "आत्मा के सिद्धांत के प्रति आसक्ति",
}
N_KIL = {  # stem: (name, gender)
    "lobh": ("लोभ", "m"), "dos": ("द्वेष", "m"), "moh": ("मोह", "m"), "mān": ("अहंकार", "m"),
    "diṭṭhi": ("दृष्टि", "f"), "vicikicchā": ("संशय", "m"), "thin": ("आलस्य", "m"),
    "uddhacc": ("बेचैनी", "f"), "ahirik": ("निर्लज्जता", "f"), "anottapp": ("बुराई के प्रति निडरता", "f"),
}
K = {k: v[0] for k, v in N_KIL.items()}
SAKKAYADITTHI = "स्थायी आत्मा की ग़लत दृष्टि"                    # pi-5
SILABBATAPARAMASA = "कर्मकांडों और व्रतों से जुड़ी ग़लत धारणा"     # sīlabbata (pi-5) + parāmāsa (matrix)
DITTHIPARAMASA = "दृष्टि रूपी ग़लत धारणा"
THINA, MIDDHA, UDDHACCA, KUKKUCCA_N, VICIKICCHA = "आलस्य", "तंद्रा", "बेचैनी", "पछतावा", "संशय"
MICCHADITTHI = "सारी ग़लत दृष्टि"                                  # sabbāpi micchādiṭṭhi (pi-4)


def kil_name(w):
    w = w.strip()
    for stem in sorted(N_KIL, key=len, reverse=True):
        if w.startswith(stem):
            return N_KIL[stem]
    raise KeyError(w)


def niv_name(w):
    return (N_NIV[re.sub(r"ena$", "a", re.sub(r"ṃ$", "", w))], "f")


def upa_name(w):
    return (N_UPA[re.sub(r"ena$", "a", re.sub(r"ṃ$", "", w))], "f")


def pairs_sentence(body, names, kind, assoc):
    """'A B-ena X ceva Y-sampayutto ca, …' -> 'A, B के साथ, <kind> भी है और <assoc> से जुड़ा/जुड़ी भी है; …'"""
    out = []
    for part in body.split(", "):
        w = part.split()
        (a, g), (b, _) = names(w[0][0].lower() + w[0][1:]), names(w[1])
        j = "जुड़ा" if g == "m" else "जुड़ी"
        out.append(f"{a}, {b} के साथ, {kind} भी है और {assoc} से {j} भी है")
    return "; ".join(out)


P = {}  # Pāli bodies of the long pair lists


# ---- 4-02 -----------------------------------------------------------------------------------
def build_402():
    seg = {}
    seg["1-3-2-6-0"] = [GROUP_H["1-3-2-6-0"]]
    seg["1-1156"] = [f"{Q('oghā')} चार बाढ़ें… {L('oghavippayuttā oghaniyā')}"]
    seg["1-3-2-7-0"] = [GROUP_H["1-3-2-7-0"]]
    seg["1-1157"] = [f"{Q('yogā')} चार जकड़नें… {L('yogavippayuttā yoganiyā')}"]

    # hindrances
    n = N_NIV
    seg["1-3-2-8-0"] = [GROUP_H["1-3-2-8-0"]]
    seg["1-1158"] = [f"{Q('nīvaraṇā')} छह बाधाएँ{V('p', 'Syā.', 'nīvaraṇāni')} {D} "
                     + ", ".join(list(n.values())[:6]) + DANDA]
    seg["1-1159"] = [T(n["kāmacchandanīvaraṇa"], S_KAMA)]
    seg["1-1160"] = [T(n["byāpādanīvaraṇa"], DOSA)]
    seg["1-1161"] = [f"{TQ(n['thinamiddhanīvaraṇa'])} {THINA} होता है, और {MIDDHA} होती है{DANDA}"]
    seg["1-1162"] = [T(THINA, S_THINA)]
    seg["1-1163"] = [f"{T(MIDDHA, S_MIDDHA)} इस प्रकार यह {THINA} और यह {MIDDHA} "
                     f"{CALLED(n['thinamiddhanīvaraṇa'])}"]
    seg["1-1164"] = [f"{TQ(n['uddhaccakukkuccanīvaraṇa'])} {UDDHACCA} होती है, और {KUKKUCCA_N} होता है{DANDA}"]
    seg["1-1165"] = [T(UDDHACCA, S_UDDHACCA)]
    seg["1-1166"] = [f"{T(KUKKUCCA_N, KUKKUCCA)} इस प्रकार यह {UDDHACCA} और यह {KUKKUCCA_N} "
                     f"{CALLED(n['uddhaccakukkuccanīvaraṇa'])}"]
    seg["1-1167"] = [T(n["vicikicchānīvaraṇa"], f"{VICI_INTRO}{DANDA} {VICI_STR}")]
    seg["1-1168"] = [T(n["avijjānīvaraṇa"], f"{MOHA_INTRO}; {MOHA_STR}"), L("nīvaraṇā")]
    seg["1-1169"] = [F_NO("no nīvaraṇā")]
    seg["1-1170"] = [F_SAS("nīvaraṇiyā")]
    seg["1-1171"] = [F_LOKUT("anīvaraṇiyā")]
    seg["1-1172"] = [F_SAMP("nīvaraṇasampayuttā")]
    seg["1-1173"] = [F_VIPP("nīvaraṇavippayuttā")]
    seg["1-1174"] = [f"{Q('nīvaraṇā ceva nīvaraṇiyā ca')} वे ही बाधाएँ {I('nīvaraṇā ceva nīvaraṇiyā ca')} हैं{DANDA}"]
    seg["1-1175"] = [F_NIYA_NOT("nīvaraṇiyā ceva no ca nīvaraṇā", REL_OBJ)]
    seg["1-1176"] = [f"{Q('nīvaraṇā ceva nīvaraṇasampayuttā ca')} "
                     f"{pairs_sentence(P['1-1176'], niv_name, 'बाधा', 'बाधा')} "
                     f"{E('nīvaraṇā ceva nīvaraṇasampayuttā ca')}"]
    seg["1-1177"] = [F_NOT_OF("nīvaraṇasampayuttā ceva no ca nīvaraṇā", REL_SAMP)]
    seg["1-1178"] = [F_VIPP_NIYA("nīvaraṇavippayuttā nīvaraṇiyā", KA)]
    seg["1-1179"] = [F_LOKUT("nīvaraṇavippayuttā anīvaraṇiyā")]

    # misapprehension
    seg["1-3-2-9-0"] = [GROUP_H["1-3-2-9-0"]]
    seg["1-1180"] = [f"{Q('parāmāsā')} {DITTHIPARAMASA}{DANDA}"]
    seg["1-1181"] = [f"{T(DITTHIPARAMASA, f'{VIEWS10}; {DITTHI_STR}')} {MICCHADITTHI} {DITTHIPARAMASA} है{DANDA}",
                     L("parāmāsā")]
    seg["1-1182"] = [F_NO("no parāmāsā")]
    seg["1-1183"] = [F_SAS("parāmaṭṭhā")]
    seg["1-1184"] = [F_LOKUT("aparāmaṭṭhā")]
    seg["1-1185"] = [F_SAMP("parāmāsasampayuttā")]
    seg["1-1186"] = [F_VIPP("parāmāsavippayuttā")]
    one = I("parāmāsā ceva parāmaṭṭhā ca")
    assert one.endswith(" परिघटनाएँ")
    seg["1-1187"] = [f"{Q('parāmāsā ceva parāmaṭṭhā ca')} वही ग़लत धारणा {one[:-len('परिघटनाएँ')]}परिघटना है{DANDA}"]
    seg["1-1188"] = [F_NIYA_NOT("parāmaṭṭhā ceva no ca parāmāsā", REL_OBJ)]
    seg["1-1189"] = [F_VIPP_NIYA("parāmāsavippayuttā parāmaṭṭhā", KUA)]
    seg["1-1190"] = [F_LOKUT("parāmāsavippayuttā aparāmaṭṭhā")]

    # long intermediate pairs
    seg["1-3-2-10-0"] = [GROUP_H["1-3-2-10-0"]]
    seg["1-1191"] = [QA("sārammaṇā", FOUR)]
    seg["1-1192"] = [QA("anārammaṇā", RA)]
    seg["1-1193"] = [QA("cittā", "आँख की चेतना, कान की चेतना, नाक की चेतना, जीभ की चेतना, शरीर की चेतना, "
                              "मन का तत्व, मन की चेतना का तत्व")]
    seg["1-1194"] = [QA("no cittā", f"{FEEL3}, {RA}")]
    seg["1-1195"] = [QA("cetasikā", FEEL3)]
    seg["1-1196"] = [QA("acetasikā", MIND_RA)]
    seg["1-1197"] = [QA("cittasampayuttā", FEEL3)]
    seg["1-1198"] = [QA("cittavippayuttā", RA) + f" मन के बारे में यह नहीं कहना चाहिए {D} न यह कि वह "
                     f"“मन से जुड़ा” है, न यह कि वह “मन से अलग” है{DANDA}"]
    seg["1-1199"] = [QA("cittasaṃsaṭṭhā", FEEL3)]
    seg["1-1200"] = [QA("cittavisaṃsaṭṭhā", RA) + f" मन के बारे में यह नहीं कहना चाहिए {D} न यह कि वह "
                     f"“मन से घुला-मिला” है, न यह कि वह “मन से घुला-मिला नहीं” है{DANDA}"]
    INTIM = "शरीर द्वारा अभिव्यक्ति, वाणी द्वारा अभिव्यक्ति"       # kāyaviññatti, vacīviññatti
    seg["1-1201"] = [QA("cittasamuṭṭhānā",
                        f"{FEEL3}; {INTIM}; या जो भी दूसरा भौतिक रूप मन से जन्मा, मन के कारण से और मन से उत्पन्न "
                        "है: दृश्य रूप का इंद्रिय-क्षेत्र, ध्वनि का इंद्रिय-क्षेत्र, गंध का इंद्रिय-क्षेत्र, स्वाद का "
                        "इंद्रिय-क्षेत्र, स्पर्श का इंद्रिय-क्षेत्र, आकाश तत्व, जल तत्व, भौतिक रूप का हल्कापन, "
                        "भौतिक रूप की मृदुता, भौतिक रूप की कार्य-योग्यता, भौतिक रूप की वृद्धि, भौतिक रूप की "
                        "निरंतरता, कौर-कौर खाया जाने वाला भोजन")]
    seg["1-1202"] = [QA("no cittasamuṭṭhānā", MIND_REM)]
    EXPR = f"{FEEL3}, {INTIM}"
    seg["1-1203"] = [QA("cittasahabhuno", EXPR)]
    seg["1-1204"] = [QA("no cittasahabhuno", MIND_REM)]
    seg["1-1205"] = [QA("cittānuparivattino", EXPR)]
    seg["1-1206"] = [QA("no cittānuparivattino", MIND_REM)]
    for bid, key in (("1-1207", "cittasaṃsaṭṭhasamuṭṭhānā"), ("1-1209", "cittasaṃsaṭṭhasamuṭṭhānasahabhuno"),
                     ("1-1211", "cittasaṃsaṭṭhasamuṭṭhānānuparivattino")):
        seg[bid] = [QA(key, FEEL3)]
        seg["1-" + str(int(bid[2:]) + 1)] = [QA("no " + key, MIND_RA)]
    seg["1-1213"] = [QA("ajjhattikā", "आँख का इंद्रिय-क्षेत्र… मन का इंद्रिय-क्षेत्र")]
    seg["1-1214"] = [QA("bāhirā", "दृश्य रूप का इंद्रिय-क्षेत्र… मन के विषयों का इंद्रिय-क्षेत्र")]
    seg["1-1215"] = [QA("upādā", "आँख का इंद्रिय-क्षेत्र… कौर-कौर खाया जाने वाला भोजन")]
    seg["1-1216"] = [QA("no upādā", f"{FOUR}, चार महाभूत और {ASANKHATA}")]
    seg["1-1217"] = [QA("upādiṇṇā", f"हितकर और हानिकर परिघटनाओं के, {SASAVA.replace('वाली', 'वाले')} कर्म-फल, "
                                    f"{W3}; {VV}; और जो भौतिक रूप किए गए कर्म के कारण है")]
    seg["1-1218"] = [QA("anupādiṇṇā", f"{SASAVA} {KU}, {W3}; {VV}; जो परिघटनाएँ केवल क्रिया हैं, न हितकर, न "
                                      f"हानिकर, न कर्म-फल; जो भौतिक रूप किए गए कर्म के कारण नहीं है; {LOKUT}")]

    # clinging
    u = N_UPA
    seg["1-3-2-11-0"] = [GROUP_H["1-3-2-11-0"]]
    seg["1-1219"] = [f"{Q('upādānā')} चार आसक्तियाँ {D} " + ", ".join(u.values())
                     + V("s", "Sī.", "kāmūpādānaṃ diṭṭhūpādānaṃ sīlabbatūpādānaṃ attavādūpādānaṃ") + DANDA]
    seg["1-1220"] = [T(u["kāmupādāna"], S_KAMA)]
    seg["1-1221"] = [T(u["diṭṭhupādāna"], f"{NATTHI_V} {D} {DITTHI_STR}")
                     + f" {u['sīlabbatupādāna']} और {u['attavādupādāna']} को छोड़कर {MICCHADITTHI} "
                       f"{u['diṭṭhupādāna']} है{DANDA}"]
    seg["1-1222"] = [T(u["sīlabbatupādāna"], f"{SILABBATA} {D} {DITTHI_STR}")]
    seg["1-1223"] = [T(u["attavādupādāna"], f"{SAKKAYA} {DITTHI_STR}"), L("upādānā")]
    seg["1-1224"] = [F_NO("no upādānā")]
    seg["1-1225"] = [F_SAS("upādāniyā")]
    seg["1-1226"] = [F_LOKUT("anupādāniyā")]
    seg["1-1227"] = [F_SAMP("upādānasampayuttā")]
    seg["1-1228"] = [F_VIPP("upādānavippayuttā")]
    seg["1-1229"] = [f"{Q('upādānā ceva upādāniyā ca')} वे ही आसक्तियाँ {I('upādānā ceva upādāniyā ca')} हैं{DANDA}"]
    seg["1-1230"] = [F_NIYA_NOT("upādāniyā ceva no ca upādānā", REL_OBJ)]
    seg["1-1231"] = [f"{Q('upādānā ceva upādānasampayuttā ca')} "
                     f"{pairs_sentence(P['1-1231'], upa_name, 'आसक्ति', 'आसक्ति')} "
                     f"{E('upādānā ceva upādānasampayuttā ca')}"]
    seg["1-1232"] = [F_NOT_OF("upādānasampayuttā ceva no ca upādānā", REL_SAMP)]
    seg["1-1233"] = [F_VIPP_NIYA("upādānavippayuttā upādāniyā", KUA)]
    seg["1-1234"] = [F_LOKUT("upādānavippayuttā anupādāniyā"), END_BHANA2]

    # defilements
    seg["1-3-2-12-0"] = [GROUP_H["1-3-2-12-0"]]
    seg["1-1235"] = [f"{Q('kilesā')} मन के क्लेशों के दस आधार {D} " + ", ".join(K.values()) + DANDA]
    seg["1-1236"] = [T(K["lobh"], S_LOBHA)]
    seg["1-1237"] = [T(K["dos"], DOSA)]
    seg["1-1238"] = [T(K["moh"], f"{MOHA_INTRO}{DANDA} {MOHA_STR}")]
    seg["1-1239"] = [T(K["mān"], MANA)]
    seg["1-1240"] = [T(K["diṭṭhi"], f"{VIEWS10}; {DITTHI_STR}") + f" {MICCHADITTHI} {K['diṭṭhi']} है{DANDA}"]
    seg["1-1241"] = [T(K["vicikicchā"], f"{VICI_INTRO}; {VICI_STR}")]
    seg["1-1242"] = [T(K["thin"], S_THINA)]
    seg["1-1243"] = [T(K["uddhacc"], S_UDDHACCA)]
    seg["1-1244"] = [T(K["ahirik"], AHIRIKA)]
    seg["1-1245"] = [T(K["anottapp"], ANOTTAPPA), L("kilesā")]
    seg["1-1246"] = [F_NO("no kilesā")]
    seg["1-1247"] = [F_SAS("saṃkilesikā")]
    seg["1-1248"] = [F_LOKUT("asaṃkilesikā")]
    seg["1-1249"] = [QA("saṃkiliṭṭhā", f"{ROOTS3} {D} {GHD}; {ROOT_TAIL}")]
    seg["1-1250"] = [QA("asaṃkiliṭṭhā", f"{KA}, {W4}; {VV}; {RA}")]
    seg["1-1251"] = [F_SAMP("kilesasampayuttā")]
    seg["1-1252"] = [F_VIPP("kilesavippayuttā")]
    seg["1-1253"] = [f"{Q('kilesā ceva saṃkilesikā ca')} वे ही मन के क्लेश {I('kilesā ceva saṃkilesikā ca')} हैं{DANDA}"]
    seg["1-1254"] = [F_NIYA_NOT("saṃkilesikā ceva no ca kilesā", REL_SAMKILESIKA)]
    seg["1-1255"] = [f"{Q('kilesā ceva saṃkiliṭṭhā ca')} वे ही मन के क्लेश {I('kilesā ceva saṃkiliṭṭhā ca')} हैं{DANDA}"]
    seg["1-1256"] = [F_NOT_OF("saṃkiliṭṭhā ceva no ca kilesā", REL_SAMKILITTHA)]
    seg["1-1257"] = [f"{Q('kilesā ceva kilesasampayuttā ca')} "
                     f"{pairs_sentence(P['1-1257'], kil_name, 'मन का क्लेश', 'क्लेश')} "
                     f"{E('kilesā ceva kilesasampayuttā ca')}"]
    seg["1-1258"] = [F_NOT_OF("kilesasampayuttā ceva no ca kilesā", REL_SAMP)]
    seg["1-1259"] = [F_VIPP_NIYA("kilesavippayuttā saṃkilesikā", KA)]
    seg["1-1260"] = [F_LOKUT("kilesavippayuttā asaṃkilesikā")]

    # closing pairs
    seg["1-3-2-13-0"] = [GROUP_H["1-3-2-13-0"]]
    THREE_F = f"तीन बंधन {D} {SAKKAYADITTHI}, {VICIKICCHA}, {SILABBATAPARAMASA}"
    SAKK = T(SAKKAYADITTHI, f"{SAKKAYA} {DITTHI_SHORT}")
    VICI_S = T(VICIKICCHA, VICI_SHORT_BODY)
    SILA = T(SILABBATAPARAMASA, f"{SILABBATA} {D} {DITTHI_SHORT}")
    seg["1-1261"] = [f"{Q('dassanena pahātabbā')} {THREE_F}{DANDA}"]
    seg["1-1262"] = [SAKK]
    seg["1-1263"] = [VICI_S]
    seg["1-1264"] = [f"{SILA} ये तीन बंधन, {ROOT_TAIL} {E('dassanena pahātabbā')}"]
    seg["1-1265"] = [F_NO("na dassanena pahātabbā")]
    seg["1-1266"] = [QA("bhāvanāya pahātabbā", f"{REMAINING_GHD}, {ROOT_TAIL}")]
    seg["1-1267"] = [F_NO("na bhāvanāya pahātabbā")]
    seg["1-1268"] = [f"{Q('dassanena pahātabbahetukā')} {THREE_F}{DANDA}"]
    seg["1-1269"] = [SAKK]
    seg["1-1270"] = [VICI_S]
    seg["1-1271"] = [f"{SILA} ये तीन बंधन, {ROOT_TAIL} {E('dassanena pahātabbahetukā')} "
                     f"{THREE_F} {E('dassanena pahātabbā')} उनके साथ-साथ रहने वाले {GHD} {D} ये सत्य-दर्शन से "
                     f"छोड़े जाने वाले मूल हैं{DANDA} {ROOT_TAIL} {E('dassanena pahātabbahetukā')}"]
    seg["1-1272"] = [F_NO("na dassanena pahātabbahetukā")]
    seg["1-1273"] = [f"{Q('bhāvanāya pahātabbahetukā')} {REMAINING_GHD} {D} ये मानसिक अभ्यास से छोड़े जाने वाले "
                     f"मूल हैं{DANDA} {ROOT_TAIL} {E('bhāvanāya pahātabbahetukā')}"]
    seg["1-1274"] = [F_NO("na bhāvanāya pahātabbahetukā")]

    def with_(p, plane, opts, factor, assoc=VV):
        return QA(p, f"{plane} पर, {opts}, {factor} को छोड़कर, उससे जुड़ा {assoc}")

    def without(p, plane, opts, factor):
        return QA(p, f"{plane} पर, {opts}: {VV}; {factor}, {RA}")

    VIT, VIC, PITI, SUKHA, UPEK = "आरंभिक विचार", "सतत विचार", "उल्लास", "सुख", "समभाव"
    seg["1-1275"] = [with_("savitakkā", f"{VIT} वाले स्तर", PL3, VIT)]
    seg["1-1276"] = [without("avitakkā", f"{VIT} से रहित स्तर", PL4, VIT)]
    seg["1-1277"] = [with_("savicārā", f"{VIC} वाले स्तर", PL3, VIC, FOUR)]
    seg["1-1278"] = [without("avicārā", f"{VIC} से रहित स्तर", PL4, VIC)]
    seg["1-1279"] = [with_("sappītikā", f"{PITI} वाले स्तर", PL3, PITI)]
    seg["1-1280"] = [without("appītikā", f"{PITI} से रहित स्तर", PL4, PITI)]
    seg["1-1281"] = [with_("pītisahagatā", f"{PITI} के स्तर", PL3, PITI)]
    seg["1-1282"] = [without("na pītisahagatā", f"{PITI} के स्तर से भिन्न स्तर", PL4, PITI)]
    seg["1-1283"] = [with_("sukhasahagatā", f"{SUKHA} के स्तर", PL3, SUKHA, PERC3)]
    seg["1-1284"] = [without("na sukhasahagatā", f"{SUKHA} के स्तर से भिन्न स्तर", PL4, SUKHA)]
    seg["1-1285"] = [with_("upekkhāsahagatā", f"{UPEK} के स्तर", PL4, UPEK, PERC3)]
    seg["1-1286"] = [without("na upekkhāsahagatā", f"{UPEK} के स्तर से भिन्न स्तर", PL3, UPEK)]

    RANGE = "इसी दायरे में विचरने वाली और इसी में समाई हुई"     # etthāvacarā ettha pariyāpannā (cittacetasikā)
    WHO = ("चाहे वे ध्यान-अवस्था में लीन व्यक्ति की हों, या वहाँ जन्मे व्यक्ति की हों, या इसी जीवन में सुख से रहने "
           "वाले{v} व्यक्ति की हों")
    CC = "मन और मन की सहचर परिघटनाएँ"                        # cittacetasikā dhammā
    seg["1-1287"] = [QA("kāmāvacarā",
                        "नीचे अवीचि नरक को सीमा बनाकर, और ऊपर दूसरों द्वारा रचे गए भोगों पर अधिकार रखने वाले देवताओं"
                        + V("s", "Sī., Ka.", "paranimmitavasavattideve")
                        + " को भीतर लेकर, इस बीच जो समूह, तत्व और इंद्रिय-क्षेत्र इसी दायरे में विचरते हैं और इसी में "
                          "समाए हुए हैं: भौतिक रूप, अनुभूति, पहचान, मानसिक रचनाएँ, चेतना")]
    seg["1-1288"] = [QA("na kāmāvacarā", f"{I('rūpāvacarā')}, {I('arūpāvacarā')}, {I('apariyāpannā')}")]
    seg["1-1289"] = [QA("rūpāvacarā",
                        "नीचे ब्रह्मलोक को सीमा बनाकर, और ऊपर अकनिष्ठ देवताओं" + V("s", "Sī., Ka.", "akaniṭṭhadeve")
                        + f" को भीतर लेकर, इस बीच {RANGE} {CC}, "
                        + WHO.format(v=V("s", "Ka.", "diṭṭhadhammasukhavihārassa")))]
    seg["1-1290"] = [QA("na rūpāvacarā", f"{I('kāmāvacarā')}, {I('arūpāvacarā')}, {I('apariyāpannā')}")]
    seg["1-1291"] = [QA("arūpāvacarā",
                        "नीचे अनंत आकाश के क्षेत्र में उत्पन्न देवताओं को सीमा बनाकर, और ऊपर न पहचान न अ-पहचान के "
                        f"क्षेत्र में उत्पन्न देवताओं को भीतर लेकर, इस बीच {RANGE} {CC}, " + WHO.format(v=""))]
    seg["1-1292"] = [QA("na arūpāvacarā", f"{I('kāmāvacarā')}, {I('rūpāvacarā')}, {I('apariyāpannā')}")]
    seg["1-1293"] = [F_SAS("pariyāpannā")]
    seg["1-1294"] = [QA("apariyāpannā", f"मार्ग, मार्गों के फल और {ASANKHATA}")]
    seg["1-1295"] = [QA("niyyānikā", PATHS4)]
    seg["1-1296"] = [F_NO("aniyyānikā")]
    seg["1-1297"] = [QA("niyatā", f"अगले ही जन्म में निश्चित फल देने वाले पाँच कर्म, निश्चित ग़लत दृष्टि, और {PATHS4}")]
    seg["1-1298"] = [F_NO("aniyatā")]
    seg["1-1299"] = [F_SAS("sauttarā")]
    seg["1-1300"] = [F_LOKUT("anuttarā")]
    seg["1-1301"] = [QA("saraṇā", f"{ROOTS3}: {GHD}; {ROOT_TAIL}")]
    seg["1-1302"] = [QA("araṇā", f"{KA}, {W4}; {VV}; {RA}"), END_ABHI]
    return seg


# ---- 4-03 -----------------------------------------------------------------------------------
_PH = C.S_PANNA.split(", ")
PANNA_PE = f"{_PH[0]}, {_PH[1]}… " + ", ".join(_PH[-3:])      # paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi
PANNA_PE_REST = f"{_PH[1]}… " + ", ".join(_PH[-3:])            # after 'जो (…) प्रज्ञा है, '
_SH = C.S_SAMADHI.split(", ")
SAM_PE = J(f"{_SH[0]}… {_SH[-1]}")                            # Yā cittassa ṭhiti…pe… sammāsamādhi
_VH = C.S_VIRIYA.split(", ")
VIR_PE = J(f"{_VH[0]}… {_VH[-1]}")                            # Yo cetasiko vīriyārambho…pe… sammāvāyāmo
assert _PH[0] == "प्रज्ञा" and _SH[0] == "मन की स्थिरता" and _VH[-1] == "सही प्रयास"


def build_403():
    S = {}
    S["1-3-3-0"] = [H_SUTTANTA_NIKKHEPA]
    S["1-1303"] = [QA("vijjābhāgino", "विद्या से जुड़ी परिघटनाएँ")]
    S["1-1304"] = [QA("avijjābhāgino", "अज्ञान से जुड़ी परिघटनाएँ")]
    S["1-1305"] = [QA("vijjūpamā", "नीचे के तीन आर्य मार्गों में प्रज्ञा")]
    S["1-1306"] = [QA("vajirūpamā", "सबसे ऊपर के मार्ग, अर्हत्-पद के मार्ग में प्रज्ञा")]
    AH = f"{NM('2-115', 'क')} और {NM('2-115', 'ख')}"      # ahirīkañca anottappañca
    HI = f"{NM('2-116', 'क')} और {NM('2-116', 'ख')}"      # hirī ca ottappañca
    ALL_A, ALL_K = "सभी हानिकर परिघटनाएँ", "सभी हितकर परिघटनाएँ"   # sabbepi akusalā / kusalā dhammā
    S["1-1307"] = [QA("bālā", AH) + f" {ALL_A} {ADJ('2-103', 'क')} हैं{DANDA}"]
    S["1-1308"] = [QA("paṇḍitā", HI) + f" {ALL_K} {ADJ('2-103', 'ख')} हैं{DANDA}"]
    S["1-1309"] = [QA("kaṇhā", AH) + f" {ALL_A} {ADJ('2-104', 'क')} हैं{DANDA}"]
    # the Pāli ends this answer with "?" ("ime dhammā sukkā?"): kept (source slip)
    S["1-1310"] = [QA("sukkā", HI)[:-1] + f"? {ALL_K} {ADJ('2-104', 'ख')} हैं{DANDA}"]
    S["1-1311"] = [QA("tapanīyā", "शरीर का दुराचरण, वाणी का दुराचरण, मन का दुराचरण")
                   + f" {ALL_A} {ADJ('2-105', 'क')} हैं{DANDA}"]
    S["1-1312"] = [QA("atapanīyā", "शरीर का सदाचरण, वाणी का सदाचरण, मन का सदाचरण")
                   + f" {ALL_K} {ADJ('2-105', 'ख')} हैं{DANDA}"]
    NAMING = ("उन-उन परिघटनाओं की जो गणना है, संज्ञा, नामकरण, व्यवहार, नाम, नाम देना, अभिधान, अभिव्यक्ति, "
              "शब्द, उच्चारण")
    for bid, key, mid in (("1-1313", "adhivacanā", "2-106"), ("1-1314", "nirutti", "2-107"),
                          ("1-1315", "paññatti", "2-108")):
        S[bid] = [QA(key, NAMING) + f" सभी परिघटनाएँ {ADJ(mid, 'ख')} हैं{DANDA}"]
    x = NM
    S["1-1316"] = [T(x("2-109", "क"), f"{FOUR} और {ASANKHATA}")]
    S["1-1317"] = [T(x("2-109", "ख"), "चार महाभूत और चार महाभूतों से व्युत्पन्न भौतिक रूप")]
    S["1-1318"] = [T(x("2-110", "क"), MOHA_PE)]
    S["1-1319"] = [T(x("2-110", "ख"), S_BHAVA_PE)]
    for bid, mid, l, v in (("1-1320", "2-111", "क", "आत्मा और लोक का अस्तित्व रहेगा"),
                           ("1-1321", "2-111", "ख", "आत्मा और लोक का अस्तित्व नहीं रहेगा"),
                           ("1-1322", "2-112", "क", "आत्मा और लोक शाश्वत हैं"),
                           ("1-1323", "2-112", "ख", "आत्मा और लोक का विनाश हो जाएगा"),
                           ("1-1324", "2-113", "क", "आत्मा और लोक सीमित हैं"),
                           ("1-1325", "2-113", "ख", "आत्मा और लोक असीम हैं")):
        S[bid] = [T(x(mid, l), f"“{v}”, {DITTHI_SHORT}")]
    ARISE = "को विषय बनाकर जो दृष्टि उत्पन्न होती है, " + f"{DITTHI_HEAD}… {DITTHI_TAIL}"
    S["1-1326"] = [T(x("2-114", "क"), "अतीत " + ARISE)]
    S["1-1327"] = [T(x("2-114", "ख"), "भविष्य " + ARISE)]
    S["1-1328"] = [T(x("2-115", "क"), AHIRIKA)]
    S["1-1329"] = [T(x("2-115", "ख"), ANOTTAPPA)]
    S["1-1330"] = [T(x("2-116", "क"), C.S_HIRI)]
    S["1-1331"] = [T(x("2-116", "ख"), C.S_OTTAPPA)]
    SPOKEN = "शिक्षा के अनुसार कुछ कहे जाने पर "      # sahadhammike vuccamāne (pi-4 ^4-55/^4-75)
    S["1-1332"] = [T(x("2-117", "क"), SPOKEN + "सलाह न मानना, सलाह न मानने का भाव, सलाह न मानने की प्रवृत्ति, उलटा "
                                            "पकड़ना, विरोध में रस लेना, अनादर, अनादर का भाव, अगौरव, बात पर कान न देना")]
    ASSOC = ("उनकी जो संगति है, उनकी लगातार संगति, उनकी घनिष्ठ संगति, उनसे मेल-जोल, उनसे घनिष्ठ मेल-जोल, उनके प्रति "
             "लगाव, उनके प्रति गहरा लगाव, उनकी ओर झुकाव")   # pi-4 ^4-56/^4-76
    S["1-1333"] = [T(x("2-117", "ख"), "जो व्यक्ति श्रद्धाहीन, दुराचारी, कम सुने-सीखे, कंजूस और प्रज्ञाहीन हैं, " + ASSOC)]
    S["1-1334"] = [T(x("2-118", "क"), SPOKEN + "सलाह मानना, सलाह मानने का भाव, सलाह मानने की प्रवृत्ति, उलटा न पकड़ना, "
                                            "विरोध में रस न लेना, गौरव, आदर, आदर का भाव, बात पर कान देना")]
    S["1-1335"] = [T(x("2-118", "ख"), "जो व्यक्ति श्रद्धावान, सदाचारी, बहुत सुने-सीखे, उदार और प्रज्ञावान हैं, " + ASSOC)]
    PPE = f", {PANNA_PE}"
    S["1-1336"] = [T(x("2-119", "क"), "दोषों की पाँच श्रेणियाँ भी दोष हैं, दोषों की सात श्रेणियाँ भी दोष हैं। उन दोषों के "
                                     f"संबंध में जो {x('2-119', 'क')} है" + PPE)]
    S["1-1337"] = [T(x("2-119", "ख"), "उन दोषों से उबरने में जो कुशलता है" + PPE)]
    T6 = [BARE6[:-len(" परिघटनाएँ")] for BARE6 in (NM("1-6", "क"), NM("1-6", "ख"), NM("1-6", "ग"))]
    S["1-1338"] = [T(x("2-120", "क"), ", ".join(f"{t} ध्यान-अवस्था होती है" for t in T6)
                     + f"। उन ध्यान-अवस्थाओं के संबंध में जो {x('2-120', 'क')} है" + PPE)]
    S["1-1339"] = [T(x("2-120", "ख"), "उन ध्यान-अवस्थाओं से बाहर आने में जो कुशलता है" + PPE)]
    EL18 = ("आँख का तत्व, दृश्य रूप का तत्व, आँख की चेतना का तत्व, कान का तत्व, ध्वनि का तत्व, कान की चेतना का तत्व, "
            "नाक का तत्व, गंध का तत्व, नाक की चेतना का तत्व, जीभ का तत्व, स्वाद का तत्व, जीभ की चेतना का तत्व, "
            "शरीर का तत्व, स्पर्श का तत्व, शरीर की चेतना का तत्व, मन का तत्व, मन के विषयों का तत्व, "
            "मन की चेतना का तत्व")
    S["1-1340"] = [T(x("2-121", "क"), f"अठारह तत्व: {EL18}। उन तत्वों के संबंध में जो {x('2-121', 'क')} है" + PPE)]
    S["1-1341"] = [T(x("2-121", "ख"), f"उन तत्वों के संबंध में जो {x('2-121', 'ख')} है" + PPE)]
    B12 = ("आँख का इंद्रिय-क्षेत्र, दृश्य रूप का इंद्रिय-क्षेत्र, कान का इंद्रिय-क्षेत्र, ध्वनि का इंद्रिय-क्षेत्र, "
           "नाक का इंद्रिय-क्षेत्र, गंध का इंद्रिय-क्षेत्र, जीभ का इंद्रिय-क्षेत्र, स्वाद का इंद्रिय-क्षेत्र, "
           "शरीर का इंद्रिय-क्षेत्र, स्पर्श का इंद्रिय-क्षेत्र, मन का इंद्रिय-क्षेत्र, मन के विषयों का इंद्रिय-क्षेत्र")
    S["1-1342"] = [T(x("2-122", "क"), f"बारह इंद्रिय-क्षेत्र {D} {B12}। उन इंद्रिय-क्षेत्रों के संबंध में जो "
                                     f"{x('2-122', 'क')} है" + PPE)]
    TATTHA_PANNA = f"इसमें जो {_PH[0]} है, {PANNA_PE_REST}"      # yā tattha paññā pajānanā…pe… sammādiṭṭhi
    PS = ("अज्ञान के कारण मानसिक रचनाएँ होती हैं, मानसिक रचनाओं के कारण चेतना, चेतना के कारण मानसिक पक्ष और भौतिक "
          "रूप, मानसिक पक्ष और भौतिक रूप के कारण छह इंद्रिय-क्षेत्र, छह इंद्रिय-क्षेत्रों के कारण संपर्क, संपर्क के कारण "
          "अनुभूति, अनुभूति के कारण तृष्णा, तृष्णा के कारण आसक्ति, आसक्ति के कारण अस्तित्व, अस्तित्व के कारण जन्म, "
          "जन्म के कारण बुढ़ापा और मृत्यु, शोक, विलाप, दुःख, उदासी और निराशा उत्पन्न होते हैं; इस प्रकार दुःख के इस "
          "पूरे पुंज की उत्पत्ति होती है। ")
    S["1-1343"] = [T(x("2-122", "ख"), PS + TATTHA_PANNA)]
    S["1-1344"] = [T(x("2-123", "क"), "जो-जो परिघटनाएँ जिन-जिन परिघटनाओं की उत्पत्ति के लिए"
                     + V("p", "Sī., Ka.", "upādāya") + " मूल और कारण हैं, वह-वह संभव बात है; " + TATTHA_PANNA)]
    S["1-1345"] = [T(x("2-123", "ख"), "जो-जो परिघटनाएँ जिन-जिन परिघटनाओं की उत्पत्ति के लिए न मूल हैं, न कारण, "
                                     "वह-वह असंभव बात है; " + TATTHA_PANNA)]
    UJ = C.S_UJUTA.split(", ")
    S["1-1346"] = [T(x("2-124", "क"), J(", ".join([x("2-124", "क")] + UJ[2:])))]
    S["1-1347"] = [T(x("2-124", "ख"), J(C.S_MUDUTA + ", मन की विनम्रता"))]
    S["1-1348"] = [T(x("2-125", "क"), J("सहनशीलता, क्षमा करना, सह लेना, उग्रता का अभाव, कटु वचन का अभाव, "
                                       "मन का खिल उठना"))]
    NONTR = "शरीर से उल्लंघन न करना, वाणी से उल्लंघन न करना, शरीर और वाणी दोनों से उल्लंघन न करना"   # pi-4 ^4-81
    TR = ("शरीर से किया गया उल्लंघन, वाणी से किया गया उल्लंघन, शरीर और वाणी दोनों से किया गया उल्लंघन")  # pi-4 ^4-61
    RESTRAINT = "सदाचार का सारा संयम {} है।"                                                         # pi-4 ^4-81
    S["1-1349"] = [T(x("2-125", "ख"), NONTR) + " " + RESTRAINT.format(x("2-125", "ख"))]
    S["1-1350"] = [T(x("2-126", "क"),
                     "जो वाणी रूखी, कठोर, दूसरों को कड़वी लगने वाली, दूसरों को चुभने वाली, क्रोध के निकट और एकाग्रता "
                     "की ओर न ले जाने वाली है, वैसी वाणी को छोड़कर, जो वाणी निर्दोष, कानों को सुख देने वाली, प्रेमपूर्ण, "
                     "हृदय को छूने वाली, शिष्ट, बहुत लोगों को प्रिय और बहुत लोगों को मनभावन है, वैसी वाणी बोलने वाला "
                     "होता है; इसमें जो वाणी की कोमलता है, वाणी की मधुरता, वाणी का कठोर न होना")]
    hosp = x("2-126", "ख")
    S["1-1351"] = [T(hosp, f"{hosp} दो प्रकार का होता है {D} भौतिक वस्तुओं से {hosp} और शिक्षा से {hosp}। इस संसार में "
                           f"कोई भौतिक वस्तुओं से {hosp} द्वारा या शिक्षा से {hosp} द्वारा {hosp} करने वाला होता है")]

    def senses(neg):
        g = ("उसकी समग्र छवि को पकड़ लेता है, उसके ब्योरों को पकड़ लेता है" if neg
             else "उसकी समग्र छवि को नहीं पकड़ता, उसके ब्योरों को नहीं पकड़ता")
        act = ("उसके संयम के लिए वह प्रयत्न नहीं करता, {f} की इंद्रिय की रक्षा नहीं करता, {f} की इंद्रिय पर संयम नहीं "
               "रखता" if neg else
               "उसके संयम के लिए वह प्रयत्न करता है, {f} की इंद्रिय की रक्षा करता है, {f} की इंद्रिय पर संयम रखता है")
        why = ("जिस {f} की इंद्रिय को असंयमित छोड़कर रहने से लालच और उदासी जैसी बुरी और हानिकर परिघटनाएँ मन में घुस "
               "आ सकती हैं, ")
        return (f"इस संसार में कोई व्यक्ति आँख से दृश्य रूप देखकर {g}। " + why.format(f="आँख") + act.format(f="आँख")
                + "। कान से ध्वनि सुनकर… नाक से गंध सूँघकर… जीभ से स्वाद चखकर… शरीर से स्पर्श अनुभव करके… "
                f"मन से मन के विषय को जानकर {g}। " + why.format(f="मन") + act.format(f="मन") + "। ")
    S["1-1352"] = [T(x("2-127", "क"), senses(True) + "इन छह इंद्रियों की रक्षा न करना, उन्हें न सँभालना, उनकी चौकसी "
                                                     "न करना, उन पर संयम न रखना")]
    S["1-1353"] = [T(x("2-127", "ख"), "इस संसार में कोई व्यक्ति बिना सोचे-विचारे, अनुचित ढंग से भोजन करता है, मौज के "
                                     "लिए, मद के लिए, शरीर सुडौल बनाने के लिए, सुंदर दिखने के लिए। भोजन के विषय में "
                                     "उसमें जो असंतोष, मात्रा का ज्ञान न होना, बिना सोचे-विचारे खाना है")]
    S["1-1354"] = [T(x("2-128", "क"), senses(False) + "इन छह इंद्रियों की रक्षा करना, उन्हें सँभालना, उनकी चौकसी "
                                                      "करना, उन पर संयम रखना")]
    S["1-1355"] = [T(x("2-128", "ख"), f"इस संसार में कोई व्यक्ति सोच-विचारकर, उचित ढंग से भोजन करता है {D} न मौज के "
                                     "लिए, न मद के लिए, न शरीर सुडौल बनाने के लिए, न सुंदर दिखने के लिए, केवल इस शरीर को "
                                     "टिकाए रखने और चलाए रखने के लिए, कष्ट मिटाने के लिए, पवित्र जीवन में सहायता के लिए, "
                                     "यह सोचकर कि “इस प्रकार मैं पुरानी अनुभूति को मिटाऊँगा और नई अनुभूति उत्पन्न नहीं "
                                     "करूँगा, मेरा जीवन-निर्वाह होगा, निर्दोषता होगी और सुख से रहना होगा”। भोजन के "
                                     "विषय में उसमें जो संतोष, मात्रा का ज्ञान, सोच-विचारकर खाना है")]
    S["1-1356"] = [T(x("2-129", "क"), J("सजगता का अभाव, बार-बार स्मरण का अभाव, पुनः स्मरण का अभाव, सजगता का अभाव, "
                                       "याद न रखना, मन में धारण न करना, उथला होना, भूल जाना"))]
    S["1-1357"] = [T(x("2-129", "ख"), MOHA_PE)]
    S["1-1358"] = [T(x("2-130", "क"), J(C.S_SATI))]
    S["1-1359"] = [T(x("2-130", "ख"), J(PANNA_PE))]
    S["1-1360"] = [T(x("2-131", "क"), J(PANNA_PE))]
    PRACTICE = "निरंतर सेवन, मानसिक अभ्यास, बार-बार करना"        # āsevanā bhāvanā bahulīkammaṃ
    S["1-1361"] = [T(x("2-131", "ख"), f"हितकर परिघटनाओं का जो {PRACTICE} है")
                   + f" जागृति के सातों अंग भी {x('2-131', 'ख')} हैं{DANDA}"]
    S["1-1362"] = [T(x("2-132", "क"), SAM_PE)]
    S["1-1363"] = [T(x("2-132", "ख"), J(PANNA_PE))]
    S["1-1364"] = [T(x("2-133", "क"), SAM_PE)]
    S["1-1365"] = [T(x("2-133", "ख"), VIR_PE)]
    S["1-1366"] = [T(x("2-134", "क"), VIR_PE)]
    S["1-1367"] = [T(x("2-134", "ख"), SAM_PE)]
    S["1-1368"] = [T(x("2-135", "क"), TR) + f" सारा दुराचार {x('2-135', 'क')} है{DANDA}"]
    S["1-1369"] = [T(x("2-135", "ख"), f"{NATTHI_PLAIN}; {DITTHI_SHORT}") + f" {MICCHADITTHI} {x('2-135', 'ख')} है{DANDA}"]
    S["1-1370"] = [T(x("2-136", "क"), NONTR) + " " + RESTRAINT.format(x("2-136", "क"))]
    S["1-1371"] = [T(x("2-136", "ख"), f"{ATTHI}; " + EVA(_PH[0], "f", PANNA_PE_REST))
                   + f" सारी सही दृष्टि {x('2-136', 'ख')} है{DANDA}"]
    S["1-1372"] = [T(x("2-137", "क"), NONTR) + " " + RESTRAINT.format(x("2-137", "क"))]
    S["1-1373"] = [f"{TQ(x('2-137', 'ख'))} यह ज्ञान कि कर्म ही अपनी संपत्ति है, सत्यों के अनुरूप ज्ञान, मार्ग से युक्त "
                   f"व्यक्ति का ज्ञान, फल से युक्त व्यक्ति का ज्ञान{DANDA}"]

    def cite(mid, l):
        return f"“{x(mid, l)}”"
    S["1-1374"] = [f"{cite('2-138', 'क')} {D} {J(PANNA_PE)}{DANDA}"]
    S["1-1375"] = [f"{cite('2-138', 'ख')} {D} {VIR_PE}{DANDA}"]
    S["1-1376"] = [f"“मन का झकझोरा जाना” {D} जन्म का भय, बुढ़ापे का भय, रोग का भय, मृत्यु का भय{DANDA} "
                   f"“झकझोर देने वाली बातें”{V('s', 'Sī.', 'saṃvejanīyaṃ')} {D} जन्म, बुढ़ापा, रोग, मृत्यु{DANDA}"]
    EFF = "चाह जगाता है, प्रयास करता है, उत्साह जगाता है, मन को तत्पर करता है, पूरा ज़ोर लगाता है"
    S["1-1377"] = [f"{cite('2-139', 'ख')} {D} इस संसार में कोई भिक्षु अनुत्पन्न बुरी और हानिकर परिघटनाओं को उत्पन्न न "
                   f"होने देने के लिए {EFF}; उत्पन्न बुरी और हानिकर परिघटनाओं को छोड़ने के लिए {EFF}; अनुत्पन्न हितकर "
                   f"परिघटनाओं को उत्पन्न करने के लिए {EFF}; उत्पन्न हितकर परिघटनाओं की स्थिरता, उनके लुप्त न होने, "
                   f"उनकी बढ़ोतरी, विपुलता, मानसिक अभ्यास और परिपूर्णता के लिए {EFF}{DANDA}"]
    S["1-1378"] = [f"{cite('2-140', 'क')} {D} हितकर परिघटनाओं के मानसिक अभ्यास में संतुष्ट न होने वाले व्यक्ति की जो "
                   f"और अधिक की चाह है{DANDA}"]
    S["1-1379"] = [f"{cite('2-140', 'ख')} {D} हितकर परिघटनाओं के मानसिक अभ्यास में जो सावधानी से करना, लगातार करना, "
                   f"बिना रुके करना, ढीला न पड़ना, चाह को न छोड़ना, भार को न उतारना, {PRACTICE} है{DANDA}"]
    S["1-1380"] = [f"{cite('2-141', 'क')} {D} तीन विद्याएँ {D} पूर्व जन्मों के स्मरण का ज्ञान विद्या है, प्राणियों के "
                   f"मरने और जन्म लेने का ज्ञान विद्या है, मन के मैलों के क्षय का ज्ञान विद्या है{DANDA}"]
    S["1-1381"] = [f"{cite('2-141', 'ख')} {D} दो मुक्तियाँ {D} मन का{V('p', 'Sī., Syā.', 'cittassa ca')} छुटकारा, "
                   f"और निर्वाण{DANDA}"]
    S["1-1382"] = [f"{cite('2-142', 'क')} {D} मार्ग से युक्त व्यक्ति का ज्ञान{DANDA}"]
    S["1-1383"] = [f"{cite('2-142', 'ख')} {D} फल से युक्त व्यक्ति का ज्ञान{DANDA}", END_NIKKHEPA]
    return S


# ---- assemble and check ---------------------------------------------------------------
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
LATIN = re.compile(r"[A-Za-zĀāĪīŪūṃṅñṭḍṇḷ]+")


def pali_segments(path):
    segs, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
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


def assemble(part, S):
    segs = pali_segments(PALI_DIR / part)
    assert set(S) == {b for b, _ in segs}, (set(S) ^ {b for b, _ in segs})
    out, problems = [], []
    for bid, plines in segs:
        hlines = S[bid]
        if len(hlines) != len(plines):
            problems.append((bid, "lines", len(plines), len(hlines)))
        for p, h in zip(plines, hlines):
            if dashes(p) != dashes(h):
                problems.append((bid, "dash", dashes(p), dashes(h)))
            if p.count("[") != h.count("["):
                problems.append((bid, "variant", p.count("["), h.count("[")))
            if p.count("…pe…") != h.count("…"):
                problems.append((bid, "ellipsis", p.count("…pe…"), h.count("…")))
            if p.count("?") != h.count("?"):
                problems.append((bid, "?", p.count("?"), h.count("?")))
            if p.startswith("#") and (len(p) - len(p.lstrip("#"))) != (len(h) - len(h.lstrip("#"))):
                problems.append((bid, "heading level"))
            m = re.match(r"Katame dhammā (.+?)\?", p)
            if m and not h.startswith(Q(re.sub(r"\s+", " ", m.group(1)))):
                problems.append((bid, "question", m.group(1)))
            ip = len(re.findall(r"\b[Ii]me dhammā\b", p))
            ih = len(re.findall(r"(?:^|\s)ये [^।?]*?(?:परिघटनाएँ|नहीं|मूल) हैं[।?]", h))
            if ip != ih:
                problems.append((bid, "ime dhammā", ip, ih))
            bare = VAR.sub("", h)
            lat = LATIN.findall(bare)
            if lat:
                problems.append((bid, "latin", lat[:5]))
            for bad in ("—", ":-", "\r", "  ", "seed", "धर्म"):
                if bad in h:
                    problems.append((bid, "forbidden", bad))
        out.append("\n".join(hlines[:-1] + [hlines[-1] + f" ^{bid}"]))
    return "\n\n".join(out) + "\n", problems, len(segs)


if __name__ == "__main__":
    p402 = dict(pali_segments(PALI_DIR / "4-02-nikkhepakandam.md"))
    for b in ("1-1176", "1-1231", "1-1257"):
        P[b] = p402[b][0].split("? ", 1)[1].rsplit(f" {D} ime dhammā", 1)[0]
    ok = True
    for part, S in (("4-02-nikkhepakandam.md", build_402()), ("4-03-nikkhepakandam.md", build_403())):
        text, problems, n = assemble(part, S)
        for pr in problems:
            print(part, "PROBLEM", pr)
        ok = ok and not problems
        (OUT_DIR / part).write_text(text, encoding="utf-8", newline="\n")
        print("wrote", part, "segments", n, "problems", len(problems))
    sys.exit(0 if ok else 1)
