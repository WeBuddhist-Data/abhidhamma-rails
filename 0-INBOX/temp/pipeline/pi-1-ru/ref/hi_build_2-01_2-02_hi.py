"""Build the Hindi plain zero-shot of pi-1 parts 2-01 (after the approved sample) and 2-02.

usage: python -I -X utf8 build_2-01_2-02_hi.py      (runs the self-test, then builds both parts)

Importing this file does NOT build anything. Later parts can load the fixed formulas with
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-1-hi")
    import importlib; F = importlib.import_module("build_2-01_2-02_hi")
and then use F.translate_line(pali_line) or the constants (NAMEINFO, STR, PH, EXACT, ...).

Method (mirrors the English builder pi-1-en/build_2-01_2-02.py): every line is translated from the
Pāli source by fixed formula strings. The line translators raise KeyError on any Pāli they do not
know, so nothing is guessed silently. Repeats are byte-identical by construction, and every string
shared with the approved sample comes from build_ch2_01_sample_hi (C) / build_matika_hi (M).
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_hi as M  # noqa: E402  (importing does not rewrite the matrix)
import build_ch2_01_sample_hi as C  # noqa: E402  (importing does not rewrite the sample)

PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters"
SAMPLE = HERE / "ch2-01-sample.md"
SAMPLE_PALI = HERE / "ch2-01-pali-1-122.md"

DASH, DANDA = C.DASH, M.DANDA
PE, ELL = "…pe…", "…"
MS, FS = C.M, C.F
KUSALA = C.KUSALA

# =========================================================================================
# 1. Names: pali -> (Hindi noun, gender, plural)
# =========================================================================================
NAMEINFO = {k: (h, g, False) for k, (h, g) in C.NAMES_G.items()}
NEW_NAMES = {
    "upekkhā": ("समभाव", MS),
    "upekkhindriyaṃ": ("समभाव की क्षमता", FS),
    "vedanākkhandho": ("अनुभूति का समूह", MS),
    "saññākkhandho": ("पहचान का समूह", MS),
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", MS),
    "viññāṇakkhandho": ("चेतना का समूह", MS),
    "manāyatanaṃ": ("मन का इंद्रिय-क्षेत्र", MS),
    "dhammāyatanaṃ": ("मन के विषयों का इंद्रिय-क्षेत्र", MS),
    "manoviññāṇadhātu": ("मन की चेतना का तत्व", MS),
    "dhammadhātu": ("मन के विषयों का तत्व", MS),
    "phassāhāro": ("संपर्क रूपी आहार", MS),
    "manosañcetanāhāro": ("मानसिक इरादा रूपी आहार", MS),
    "viññāṇāhāro": ("चेतना रूपी आहार", MS),
}
for k, (h, g) in NEW_NAMES.items():
    assert k not in NAMEINFO
    NAMEINFO[k] = (h, g, False)
# the names must agree with the sample's synonym strings and with the core terms
assert "मन का इंद्रिय-क्षेत्र" in C.S_CITTA and "चेतना का समूह" in C.S_CITTA
assert C.TAJJA.endswith("मन की चेतना के तत्व के संपर्क से उत्पन्न")

# Koṭṭhāsavāra (section on parts): counted groups
NUM = {"eko": "एक", "dve": "दो", "tayo": "तीन", "cattāro": "चार", "cattāri": "चार", "pañca": "पाँच",
       "cha": "छह", "satta": "सात", "aṭṭha": "आठ", "nava": "नौ", "tīṇi": "तीन"}
KOTTHASA = {
    "cattāro khandhā": ("चार समूह", MS),
    "dvāyatanāni": ("दो इंद्रिय-क्षेत्र", MS),
    "dve dhātuyo": ("दो तत्व", MS),
    "tayo āhārā": ("तीन आहार", MS),
    "navindriyāni": ("नौ क्षमताएँ", FS),
    "aṭṭhindriyāni": ("आठ क्षमताएँ", FS),
    "sattindriyāni": ("सात क्षमताएँ", FS),
    "pañcindriyāni": ("पाँच क्षमताएँ", FS),
    "cattāri indriyāni": ("चार क्षमताएँ", FS),
    "tīṇindriyāni": ("तीन क्षमताएँ", FS),
    "satta balāni": ("सात बल", MS),
    "cha balāni": ("छह बल", MS),
    "cattāri balāni": ("चार बल", MS),
    "tīṇi balāni": ("तीन बल", MS),
    "tayo hetū": ("तीन मूल", MS),
    "dve hetū": ("दो मूल", MS),
}
for k, (h, g) in KOTTHASA.items():
    NAMEINFO[k] = (h, g, True)
FACTORED = {
    "pañcaṅgikaṃ jhānaṃ": "पाँच अंगों वाला ध्यान",
    "caturaṅgikaṃ jhānaṃ": "चार अंगों वाला ध्यान",
    "tivaṅgikaṃ jhānaṃ": "तीन अंगों वाला ध्यान",
    "duvaṅgikaṃ jhānaṃ": "दो अंगों वाला ध्यान",
    "aṭṭhaṅgiko maggo": "आठ अंगों वाला मार्ग",
    "pañcaṅgiko maggo": "पाँच अंगों वाला मार्ग",
    "caturaṅgiko maggo": "चार अंगों वाला मार्ग",
    "tivaṅgiko maggo": "तीन अंगों वाला मार्ग",
    "duvaṅgiko maggo": "दो अंगों वाला मार्ग",
}
for k, h in FACTORED.items():
    NAMEINFO[k] = (h, MS, False)
NAMEINFO["eko hetu"] = ("एक मूल", MS, False)

# Suññatavāra (section on emptiness): bare group names
SUNNATA = {
    "dhammā": ("परिघटनाएँ", FS, True),
    "khandhā": ("समूह", MS, True),
    "āyatanāni": ("इंद्रिय-क्षेत्र", MS, True),
    "dhātuyo": ("तत्व", MS, True),
    "āhārā": ("आहार", MS, True),
    "indriyāni": ("क्षमताएँ", FS, True),
    "jhānaṃ": ("ध्यान", MS, False),
    "maggo": ("मार्ग", MS, False),
    "balāni": ("बल", MS, True),
    "hetū": ("मूल", MS, True),
}
NAMEINFO.update(SUNNATA)


def info(p):
    """pali name -> (Hindi, gender, plural). 'eko/ekā/ekaṃ X' = 'एक X'."""
    if p in NAMEINFO:
        return NAMEINFO[p]
    m = re.fullmatch(r"(?:eko|ekā|ekaṃ) (\S+)", p)
    if m and m.group(1) in NAMEINFO and not NAMEINFO[m.group(1)][2]:
        h, g, _ = NAMEINFO[m.group(1)]
        # 'एक' + the full name (एक अनुभूति का समूह), as build_2-03_hi.py also writes it
        return ("एक " + h, g, False)
    raise KeyError("name: " + p)


VERB = {(MS, False): "होता है", (FS, False): "होती है", (MS, True): "होते हैं", (FS, True): "होती हैं"}


def _chk(p, verb):
    h, g, pl = info(p)
    assert pl == (verb == "honti"), (p, verb)
    return h, g, pl


def q_hi(p, verb):
    """'Katamo/Katamā/Katamaṃ/Katame/Katamāni tasmiṃ samaye X hoti/honti' (without the mark)"""
    h, g, pl = _chk(p, verb)
    return f"उस समय {h} क्या {'हैं' if pl else 'है'}"


def this_hi(p, verb):
    """'ayaṃ/idaṃ/ime/imāni/imā tasmiṃ samaye X hoti/honti'"""
    h, g, pl = _chk(p, verb)
    return f"{'ये' if pl else 'यह'} उस समय {h} {'हैं' if pl else 'है'}"


def there_hi(p, verb):
    """'X hoti' in a list: 'X होता है / होती है / होते हैं / होती हैं'"""
    h, g, pl = _chk(p, verb)
    return f"{h} {VERB[(g, pl)]}"


for _k in C.NAMES:  # the list items of the sample are reproduced exactly
    assert there_hi(_k, "hoti") == C.LIST_ITEM(_k), _k

# =========================================================================================
# 2. Synonym strings (Pāli string = Hindi). The sample's STRINGS plus new ones.
# =========================================================================================
STR = dict(C.STRINGS)
S_UPEKKHA_P = ("cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ "
               "cetosamphassajā adukkhamasukhā vedanā")
NDNS = "न दुःखद, न सुखद"  # as in the matrix item ^1-M1-2 (ग)
assert M.BARE[("1-M1-2", "ग")] == NDNS + " अनुभूति से जुड़ी परिघटनाएँ"
S_UPEKKHA = (f"न सुहावना, न असुहावना मानसिक भाव, मन के संपर्क से उत्पन्न {NDNS} अनुभव, "
             f"मन के संपर्क से उत्पन्न {NDNS} अनुभूति")
STR[S_UPEKKHA_P] = S_UPEKKHA
# abbreviated paññā string (…pe… inside the string), cut from the sample's full string
S_PANNA_ABBR = C.S_PANNA.split(", ")[0] + ", " + C.S_PANNA.split(", ")[1] + ELL + " " + ", ".join(
    C.S_PANNA.split(", ")[-3:])
assert S_PANNA_ABBR == "प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि", S_PANNA_ABBR
STR["paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi"] = S_PANNA_ABBR

STR_PREFIX = [
    ("tajjāmanoviññāṇadhātusamphassajaṃ ", C.TAJJA + " "),
    ("tajjāmanoviññāṇadhātusamphassajā ", C.TAJJA + " "),
    ("vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa ", C.G_KAYA + " "),
    ("viññāṇakkhandhassa ", C.G_CITTA + " "),
]

# =========================================================================================
# 3. Variant brackets (every variant after the sample is spelling-only)
# =========================================================================================
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "bahūsu": "कई संस्करणों में"}


def var_hi(br):
    m = re.fullmatch(r"\[(.+?) \(([^)]*)\)\]", br)
    words, sig = m.groups()
    return C.V("s", ", ".join(SIGLA[s] for s in sig.split()), words).strip()


# =========================================================================================
# 4. Tails: "ye vā pana …", "ayaṃ tasmiṃ samaye X hoti", "ime dhammā kusalā", "…pe…"
# =========================================================================================
YVP_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
YVP_H = "या " + C.YEVAPANA_BODY
assert C.YEVAPANA() == C.YEVAPANA_BODY + " " + DASH + " " + M.ANSWER(KUSALA)
THAP_P = "ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
CHOD = "को छोड़कर"
THAP_H = (f"अनुभूति के समूह {CHOD}, पहचान के समूह {CHOD}, चेतना के समूह {CHOD}")
THAP_PV = "ṭhapetvā [thapetvā (ka.)] vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_HV = THAP_H.replace(CHOD, CHOD + C.V("s", "Ka.", "thapetvā"), 1)
KUSALA_P, KUSALA_H = "ime dhammā kusalā", M.ANSWER_BARE(KUSALA)


def tail_tr(t):
    t = t.replace(YVP_P + " " + THAP_PV, YVP_H + ", " + THAP_HV)
    t = t.replace(YVP_P + " " + THAP_P, YVP_H + ", " + THAP_H)
    t = t.replace(YVP_P, YVP_H)
    t = re.sub(r"(?<!\S)(ayaṃ|idaṃ|ime|imāni|imā) tasmiṃ samaye (.+?) (hoti|honti)(?=[.?…]|$)",
               lambda m: this_hi(m.group(2), m.group(3)), t)
    t = t.replace(KUSALA_P, KUSALA_H)
    t = t.replace(PE, ELL)
    if t.endswith("."):
        t = t[:-1] + DANDA
    assert "." not in re.sub(r"\[[^\]]*\]", "", t), t
    return t


# =========================================================================================
# 5. Lists
# =========================================================================================
def there_list(s):
    """'phasso hoti, vedanā hoti…pe… avikkhepo hoti' -> 'संपर्क होता है, अनुभूति होती है… …'"""
    parts = re.split(r"(?:(?<=hoti)|(?<=honti))(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p.replace(PE, ELL) if PE in p else ", ")
        else:
            m = re.fullmatch(r"(.+) (hoti|honti)", p)
            out.append(there_hi(m.group(1), m.group(2)))
    return "".join(out)


def name_list(s):
    """'Phasso cetanā…pe… avikkhepo' / 'Vedanākkhandho, saññākkhandho' -> Hindi names, comma-separated"""
    parts = re.split(r"(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p.replace(PE, ELL) if PE in p else ", ")
        else:
            out.append(info(p[0].lower() + p[1:])[0])
    return "".join(out)


# =========================================================================================
# 6. Q/A frames
# =========================================================================================
QRE = re.compile(r"Katam(?:o|ā|aṃ|e|āni) tasmiṃ samaye (.+?) (hoti|honti)(\?|…pe…)\s*(.*)$")
ARE = re.compile(r"(?:Yo|Yā|Yaṃ) tasmiṃ samaye (.+?) – ((?:ayaṃ|idaṃ) tasmiṃ samaye .+)$")
JRE = re.compile(r"Yo tesaṃ arūpīnaṃ dhammānaṃ (.+?) – (idaṃ tasmiṃ samaye .+)$")
LRE = re.compile(r"(.+?)(\s–\s.*|;.*|\.)$")


def str_hi(s):
    pre = ""
    for p, h in STR_PREFIX:
        if s.startswith(p):
            s, pre = s[len(p):], h
            break
    return pre, STR[s]


def answer_hi(a):
    m = ARE.fullmatch(a)
    if m:
        s, rest = m.groups()
        pre, sh = str_hi(s)
        if s.startswith(("hirīyati", "ottappati")):
            return f"उस समय {sh} {DASH} " + tail_tr(rest)
        return f"उस समय {pre}जो {sh} है {DASH} " + tail_tr(rest)
    m = JRE.fullmatch(a)
    if m:
        s, rest = m.groups()
        return f"{C.G_JIVITA} जो {STR[s]} है {DASH} " + tail_tr(rest)
    m = LRE.fullmatch(a)
    names, rest = m.groups()
    return name_list(names) + (DANDA if rest == "." else tail_tr(rest))


def qa_hi(line):
    m = QRE.fullmatch(line)
    name, verb, mark, rest = m.groups()
    q = q_hi(name, verb)
    if mark == "?":
        return q + "? " + answer_hi(rest)
    return q + ELL + " " + tail_tr(rest)


# =========================================================================================
# 7. "Katame dhammā kusalā? Yasmiṃ samaye …" sentences: fixed phrase table
# =========================================================================================
Q_KUSALA = M.QUESTION(KUSALA)
assert C.FRAMES["Katame dhammā kusalā?"] == Q_KUSALA
INTROS = [
    ("rūpūpapattiyā maggaṃ bhāveti ",
     "जिस समय कोई सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है और "),
    ("arūpūpapattiyā maggaṃ bhāveti ",
     "जिस समय कोई अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है और "),
    ("kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti ", C.OPEN_KAMA_KUSALA + ", "),
]

ORD = {"paṭhamaṃ": "पहले", "dutiyaṃ": "दूसरे", "tatiyaṃ": "तीसरे", "catutthaṃ": "चौथे", "pañcamaṃ": "पाँचवें"}
J_ENTER = "{} ध्यान{{V}} को प्राप्त करके उसमें रहता है"
VIVEKA = "इंद्रिय-सुखों से अलग होकर"
VUPASAMA = "आरंभिक विचार और सतत विचार के शांत होने से"
VIRAGA = "उल्लास के फीके पड़ने से"
PAHANA = "सुख के त्याग"
PITISUKHA = "और जिसमें उल्लास और सुख है"
SAMADHIJA = "एकाग्रता से उत्पन्न है"
NANA = {"ñāṇasampayuttaṃ": "ज्ञान से जुड़ा होता है", "ñāṇavippayuttaṃ": "ज्ञान से अलग होता है"}
VED = {"somanassasahagataṃ": "प्रसन्नता", "upekkhāsahagataṃ": "समभाव"}


def KASINA(x):
    return f"{x} ध्यान-मंडल को आधार बनाकर"


def ASUBHA(x):
    return f"जो {x} की पहचान के साथ होता है"


def COLOUR(adj, fem):
    return f"जो {adj} हैं, {adj} रंग वाले, {adj} दिखने वाले, {fem} आभा वाले"


def PATIPADA(prog, abhi):
    return f"{prog} प्रगति{{V}} और {abhi} उच्च ज्ञान के साथ"


def OBJ(a, b):
    return f"जो {a} है और {b} विषय वाला है"


PH = {
    # --- the absorption formulas (full); first and fourth after the approved Hindi pi-4 ------
    "vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ "
    "upasampajja viharati":
        f"{VIVEKA}, हानिकर परिघटनाओं से अलग होकर, {J_ENTER.format('पहले')}, जो आरंभिक विचार और सतत विचार "
        f"सहित है, अलगाव से उत्पन्न है, {PITISUKHA}",
    "vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ "
    "pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        f"{VUPASAMA} {J_ENTER.format('दूसरे')}, जिसमें भीतरी निर्मलता और मन का एक बिंदु पर टिकना होता है, "
        f"जो आरंभिक विचार और सतत विचार से रहित है, {SAMADHIJA}, {PITISUKHA}",
    "pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti yaṃ taṃ ariyā "
    "ācikkhanti – \"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati":
        f"{VIRAGA} समभाव के साथ, सजग और स्पष्ट समझ रखते हुए रहता है, शरीर से सुख का अनुभव करता है, "
        f"और उस {J_ENTER.format('तीसरे')} जिसके विषय में आर्य कहते हैं {DASH} "
        "“समभाव वाला, सजग, सुख से रहने वाला”",
    "sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ "
    "upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati":
        f"{PAHANA} और दुःख के त्याग से, और पहले ही प्रसन्नता और उदासी के मिट जाने से, "
        f"{J_ENTER.format('चौथे')}, जो {NDNS} है, और जिसमें समभाव से सजगता पूरी तरह "
        "शुद्ध होती है",
    "avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        f"{J_ENTER.format('दूसरे')}, जो आरंभिक विचार से रहित है, केवल सतत विचार वाला है, {SAMADHIJA}, "
        f"{PITISUKHA}",
    # --- the absorption formulas (opening words only, before …pe…) ---------------------
    "vivicceva kāmehi": VIVEKA,
    "vitakkavicārānaṃ vūpasamā": VUPASAMA,
    "pītiyā ca virāgā": VIRAGA,
    "sukhassa ca pahānā": PAHANA + " से",
    # --- modes of progress ---------------------------------------------------------------
    "dukkhapaṭipadaṃ dandhābhiññaṃ": PATIPADA("दुःखद", "धीमे"),
    "dukkhapaṭipadaṃ khippābhiññaṃ": PATIPADA("दुःखद", "तीव्र"),
    "sukhapaṭipadaṃ dandhābhiññaṃ": PATIPADA("सुखद", "धीमे"),
    "sukhapaṭipadaṃ khippābhiññaṃ": PATIPADA("सुखद", "तीव्र"),
    # --- the absorption and its object (matrix: paritta = सीमित, appamāṇa = अपरिमित) ----------
    "parittaṃ parittārammaṇaṃ": OBJ("सीमित", "सीमित"),
    "parittaṃ appamāṇārammaṇaṃ": OBJ("सीमित", "अपरिमित"),
    "appamāṇaṃ parittārammaṇaṃ": OBJ("अपरिमित", "सीमित"),
    "appamāṇaṃ appamāṇārammaṇaṃ": OBJ("अपरिमित", "अपरिमित"),
    # --- meditation devices (pi-5 ध्यान-मंडल) ----------------------------------------------
    "pathavīkasiṇaṃ": KASINA("पृथ्वी के"),
    "āpokasiṇaṃ": KASINA("जल के"),
    "tejokasiṇaṃ": KASINA("अग्नि के"),
    "vāyokasiṇaṃ": KASINA("वायु के"),
    "nīlakasiṇaṃ": KASINA("नीले"),
    "pītakasiṇaṃ": KASINA("पीले"),
    "lohitakasiṇaṃ": KASINA("लाल"),
    "odātakasiṇaṃ": KASINA("सफ़ेद"),
    # --- bases of mastery ---------------------------------------------------------------------
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati":
        "स्वयं में भौतिक रूप की पहचान न रखते हुए बाहर दृश्य रूपों को देखता है",
    "parittāni": "जो सीमित हैं",
    "appamāṇāni": "जो अपरिमित हैं",
    "suvaṇṇadubbaṇṇāni": "सुंदर और कुरूप",
    "nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni": COLOUR("नीले", "नीली"),
    "pītāni pītavaṇṇāni pītanidassanāni pītanibhāsāni": COLOUR("पीले", "पीली"),
    "lohitakāni lohitakavaṇṇāni lohitakanidassanāni lohitakanibhāsāni": COLOUR("लाल", "लाल"),
    "odātāni odātavaṇṇāni odātanidassanāni odātanibhāsāni": COLOUR("सफ़ेद", "सफ़ेद"),
    "tāni abhibhuyya jānāmi passāmīti": "और उन पर विजय पाकर सोचता है, “मैं जानता हूँ, मैं देखता हूँ”",
    # --- liberations ------------------------------------------------------------------------------
    "rūpī rūpāni passati": "स्वयं भौतिक रूप वाला होकर दृश्य रूपों को देखता है",
    "subhanti": "“सुंदर” इस भाव के साथ",
    # --- divine abidings ------------------------------------------------------------------------
    "mettāsahagataṃ": "जो मैत्री के साथ होता है",
    "karuṇāsahagataṃ": "जो करुणा के साथ होता है",
    "muditāsahagataṃ": "जो दूसरों के सुख पर प्रसन्नता के साथ होता है",
    "upekkhāsahagataṃ": "जो समभाव के साथ होता है",
    # --- the unattractive ---------------------------------------------------------------------------
    "uddhumātakasaññāsahagataṃ": ASUBHA("फूली हुई लाश"),
    "vinīlakasaññāsahagataṃ": ASUBHA("नीली पड़ चुकी लाश"),
    "vipubbakasaññāsahagataṃ": ASUBHA("पीप से भरी लाश"),
    "vicchiddakasaññāsahagataṃ": ASUBHA("बीच से कटी लाश"),
    "vikkhāyitakasaññāsahagataṃ": ASUBHA("जानवरों द्वारा नोची गई लाश"),
    "vikkhittakasaññāsahagataṃ": ASUBHA("बिखरी हुई लाश"),
    "hatavikkhittakasaññāsahagataṃ": ASUBHA("काटकर बिखेरी गई लाश"),
    "lohitakasaññāsahagataṃ": ASUBHA("खून से सनी लाश"),
    "puḷavakasaññāsahagataṃ": ASUBHA("कीड़ों से भरी लाश"),
    "aṭṭhikasaññāsahagataṃ": ASUBHA("कंकाल"),
    # --- the immaterial absorptions (pi-5: अनंत आकाश का क्षेत्र …) ------------------------------
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā":
        "भौतिक रूप की पहचानों को पूरी तरह पार कर जाने से, टकराव की पहचानों के मिट जाने से, "
        "विविधता की पहचानों पर मनोयोग न करने से",
    "ākāsānañcāyatanasaññāsahagataṃ": "अनंत आकाश के क्षेत्र की पहचान के साथ",
    "sabbaso ākāsānañcāyatanaṃ samatikkamma": "अनंत आकाश के क्षेत्र को पूरी तरह पार करके",
    "viññāṇañcāyatanasaññāsahagataṃ": "अनंत चेतना के क्षेत्र की पहचान के साथ",
    "sabbaso viññāṇañcāyatanaṃ samatikkamma": "अनंत चेतना के क्षेत्र को पूरी तरह पार करके",
    "ākiñcaññāyatanasaññāsahagataṃ": "कुछ भी न होने के क्षेत्र की पहचान के साथ",
    "sabbaso ākiñcaññāyatanaṃ samatikkamma": "कुछ भी न होने के क्षेत्र को पूरी तरह पार करके",
    "nevasaññānāsaññāyatanasaññāsahagataṃ": "न पहचान न अ-पहचान के क्षेत्र की पहचान के साथ",
    # --- levels and dominant factors (matrix: हीन / मध्यम / उत्तम) -----------------------------
    "hīnaṃ": "जो हीन है",
    "majjhimaṃ": "जो मध्यम है",
    "paṇītaṃ": "जो उत्तम है",
    "chandādhipateyyaṃ": "जिसमें चाह प्रधान है",
    "vīriyādhipateyyaṃ": "जिसमें उत्साह प्रधान है",
    "cittādhipateyyaṃ": "जिसमें मन प्रधान है",
    "vīmaṃsādhipateyyaṃ": "जिसमें जाँच-परख प्रधान है",
    # --- the eight wholesome minds of the sense sphere ------------------------------------------
    "sasaṅkhārena": "जो प्रेरणा के साथ उत्पन्न होता है",
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": C.ARAMMANA,
    "rūpārammaṇaṃ vā": "जिसका विषय दृश्य रूप हो",
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": "या मन का विषय, या चाहे वह जिस किसी को भी विषय बनाए",
}
for v, vh in VED.items():
    for n, nh in NANA.items():
        PH[f"{v} {n}"] = f"जो {vh} के साथ होता है और {nh}"
assert PH["somanassasahagataṃ ñāṇasampayuttaṃ"] == C.ACC_SOMA_NANA
assert C.ARAMMANA.startswith(PH["rūpārammaṇaṃ vā"] + ", ")
assert C.ARAMMANA.endswith(", " + PH["dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"])
assert PH["upekkhāsahagataṃ"] == PH["upekkhāsahagataṃ ñāṇasampayuttaṃ"].split(" और ")[0]
for p, h in ORD.items():
    PH[f"{p} jhānaṃ upasampajja viharati"] = J_ENTER.format(h)
    PH[f"{p} jhānaṃ"] = f"{h} ध्यान{{V}} को"
PH_MAX = max(len(k.split()) for k in PH)


def chunk_tr(part):
    words = []
    for t in re.findall(r"\[[^\]]*\]|[^\s\[]+", part):
        if t.startswith("["):
            words[-1][1].append(var_hi(t))
        else:
            words.append([t.rstrip(","), []])
    res, i = [], 0
    while i < len(words):
        for L in range(min(PH_MAX, len(words) - i), 0, -1):
            key = " ".join(w for w, _ in words[i:i + L])
            if key in PH:
                break
        else:
            raise KeyError("phrase: " + " ".join(w for w, _ in words[i:]))
        h = PH[key]
        vs = [v for _, vv in words[i:i + L] for v in vv]
        if vs:
            vt = " " + " ".join(vs)
            h = h.replace("{V}", vt) if "{V}" in h else h + vt
        res.append(h.replace("{V}", ""))
        i += L
    return ", ".join(res)


def x_tr(x):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(part.replace(PE, ELL))
        elif part.strip():
            out.append(chunk_tr(part))
    return "".join(out)


def kusala_hi(line):
    body = line[len("Katame dhammā kusalā? Yasmiṃ samaye "):]
    for p, h in INTROS:
        if body.startswith(p):
            body, intro = body[len(p):], h
            break
    else:
        raise KeyError("intro: " + body[:60])
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    if x.endswith(DASH):
        sep, x = " " + DASH, x[:-1].rstrip()
    elif x.endswith(","):
        sep, x = ",", x[:-1]
    else:
        sep = ""  # the Pāli has no punctuation here; kept as written
    m = re.fullmatch(r"(.*? hoti)(…pe… ime dhammā kusalā.*|; ye vā pana.*)", rest)
    return (Q_KUSALA + " " + intro + x_tr(x) + sep + " उस समय " + there_list(m.group(1))
            + tail_tr(m.group(2)))


def summary_hi(line):
    """'Tasmiṃ kho pana samaye cattāro khandhā honti, …; ye vā pana …' (Koṭṭhāsa / Suññata summaries)"""
    body = line[len("Tasmiṃ kho pana samaye "):]
    items, rest = body.split(";", 1)
    return "और उस समय " + there_list(items) + ";" + tail_tr(rest)


# =========================================================================================
# 8. Headings and closing lines (exact). Headings from hi-zeroshot-terms.md, verbatim.
# =========================================================================================
H_RUPA = "सूक्ष्म भौतिक लोक से संबंधित हितकर मन"
H_ARUPA = "अभौतिक लोक से संबंधित हितकर मन"
H_KAMA = C.H_KAMA_KUSALA[len("#### "):]
assert H_KAMA == "इंद्रिय-सुखों के लोक से संबंधित हितकर मन"
SOLASA, ATTHA = "सोलह गुना", "आठ गुना"
# Terms file: "##### Appamāṇāni = ##### असीम भाव". Here the heading names the bases of mastery
# over immeasurable forms (it pairs with "Abhibhāyatanāni parittāni"), so the approved wording looks
# like a mismatch; kept verbatim as instructed and reported. Proposed alternative:
H_APPAMANANI_ALT = "अपरिमित रूपों पर विजय के आधार"
H_APPAMANANI = "असीम भाव"
ORD_CITTA = ["पहले", "दूसरे", "तीसरे", "चौथे", "पाँचवें", "छठे", "सातवें", "आठवें"]
PALI_ORD = ["Paṭhamaṃ", "Dutiyaṃ", "Tatiyaṃ", "Catutthaṃ", "Pañcamaṃ", "Chaṭṭhaṃ", "Sattamaṃ", "Aṭṭhamaṃ"]
EXACT = {
    # sample (for the self-test)
    "### Cittuppādakaṇḍaṃ": C.H_CH2,
    "#### Kāmāvacarakusalaṃ": C.H_KAMA_KUSALA,
    "##### Padabhājanī": C.H_PADA,
    "Padabhājanīyaṃ.": C.END_PADA,
    "Paṭhamabhāṇavāro.": C.END_BHANA1,
    # 2-01
    "##### Koṭṭhāsavāro": "##### भागों में बाँटने का खंड",
    "Koṭṭhāsavāro.": "भागों में बाँटने का खंड" + DANDA,
    "##### Suññatavāro": "##### शून्यता का खंड",
    "Suññatavāro.": "शून्यता का खंड" + DANDA,
    "Aṭṭha kāmāvacaramahākusalacittāni.": "इंद्रिय-सुखों के लोक से संबंधित आठ महान हितकर मन" + DANDA,
    "Dutiyabhāṇavāro.": "दूसरा पाठ-खंड" + DANDA,
    # 2-02
    "#### Rūpāvacarakusalaṃ": "#### " + H_RUPA,
    "#### Arūpāvacarakusalaṃ": "#### " + H_ARUPA,
    "#### Tebhūmakakusalaṃ": "#### तीनों लोकों से संबंधित हितकर मन",
    "##### Kāmāvacarakusalaṃ": "##### " + H_KAMA,
    "##### Rūpāvacarakusalaṃ": "##### " + H_RUPA,
    "##### Arūpāvacarakusalaṃ": "##### " + H_ARUPA,
    "Kāmāvacarakusalaṃ.": H_KAMA + DANDA,
    "Rūpāvacarakusalaṃ.": H_RUPA + DANDA,
    "Arūpāvacarakusalaṃ.": H_ARUPA + DANDA,
    "##### Catukkanayo": "##### चार-चार की विधि",
    "Catukkanayo.": "चार-चार की विधि" + DANDA,
    "##### Pañcakanayo": "##### पाँच-पाँच की विधि",
    "Pañcakanayo.": "पाँच-पाँच की विधि" + DANDA,
    "##### Catasso paṭipadā": "##### प्रगति के चार ढंग",
    "Catasso paṭipadā.": "प्रगति के चार ढंग" + DANDA,
    "##### Cattāri ārammaṇāni": "##### चार प्रकार के विषय",
    "Cattāri ārammaṇāni.": "चार प्रकार के विषय" + DANDA,
    "##### Dve ārammaṇāni": "##### दो प्रकार के विषय",
    "Dve ārammaṇāni.": "दो प्रकार के विषय" + DANDA,
    "##### Soḷasakkhattukaṃ": "##### " + SOLASA,
    "Soḷasakkhattukaṃ.": SOLASA + DANDA,
    "##### Aṭṭhakkhattukaṃ": "##### " + ATTHA,
    "Aṭṭhakkhattukaṃ.": ATTHA + DANDA,
    "##### Idampi aṭṭhakkhattukaṃ": "##### यह भी " + ATTHA,
    "Idampi aṭṭhakkhattukaṃ.": "यह भी " + ATTHA + " है" + DANDA,
    "##### Aparampi aṭṭhakkhattukaṃ": "##### एक और " + ATTHA,
    "Aparampi aṭṭhakkhattukaṃ.": "एक और " + ATTHA + DANDA,
    "##### Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": "##### आठ ध्यान-मंडल, " + SOLASA,
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ.": "आठ ध्यान-मंडल, " + SOLASA + DANDA,
    "##### Abhibhāyatanāni parittāni": "##### सीमित रूपों पर विजय के आधार",
    "##### Appamāṇāni": "##### " + H_APPAMANANI,
    "Imānipi abhibhāyatanāni soḷasakkhattukāni.": "विजय के ये आधार भी " + SOLASA + " हैं" + DANDA,
    "##### Tīṇi vimokkhāni soḷasakkhattukāni": "##### तीन मुक्ति-अवस्थाएँ, " + SOLASA,
    "Imānipi tīṇi vimokkhāni soḷasakkhattukāni.": "ये तीन मुक्ति-अवस्थाएँ भी " + SOLASA + " हैं" + DANDA,
    "##### Cattāri brahmavihārajhānāni soḷasakkhattukāni": "##### ब्रह्म-विहारों के चार ध्यान, " + SOLASA,
    "Cattāri brahmavihārajhānāni [brahmavihārajjhānāni (sī. syā.)] soḷasakkhattukāni.":
        "ब्रह्म-विहारों के चार ध्यान" + C.V("s", "Sī., Syā.", "brahmavihārajjhānāni") + ", " + SOLASA + DANDA,
    "##### Asubhajhānaṃ soḷasakkhattukaṃ": "##### असुंदरता पर ध्यान, " + SOLASA,
    "Asubhajhānaṃ [asubhajjhānaṃ (sī. syā.)] soḷasakkhattukaṃ.":
        "असुंदरता पर ध्यान" + C.V("s", "Sī., Syā.", "asubhajjhānaṃ") + ", " + SOLASA + DANDA,
    "##### Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni":
        "##### चार अभौतिक ध्यान" + C.V("s", "Sī., Syā.", "arūpajjhānāni") + ", " + SOLASA,
    "Cattāri arūpajhānāni soḷasakkhattukāni.": "चार अभौतिक ध्यान, " + SOLASA + DANDA,
}
for p, h in zip(PALI_ORD, ORD_CITTA):
    EXACT[f"{p} cittaṃ."] = f"{h} प्रकार का मन{DANDA}"

# =========================================================================================
# 9. Line dispatch, segments, build
# =========================================================================================
IDRE = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def translate_line(line):
    if line in EXACT:
        return EXACT[line]
    if line.startswith("Katame dhammā kusalā? Yasmiṃ samaye "):
        return kusala_hi(line)
    if line.startswith("Tasmiṃ kho pana samaye "):
        return summary_hi(line)
    if QRE.fullmatch(line):
        return qa_hi(line)
    if line.startswith("Ye vā pana ") or re.match(r"(Ime|Imāni|Imā|Idaṃ|Ayaṃ) tasmiṃ samaye ", line):
        return tail_tr(line[0].lower() + line[1:])
    raise KeyError("line: " + line[:80])


def check_clean(h):
    """No Pāli/Latin outside variant brackets, no '.', no em dash, no ':-'."""
    bare = re.sub(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]", "", h)
    assert not re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", bare), h[:160]
    assert "." not in bare and "—" not in h and ":-" not in h and "  " not in h, h[:160]


def segments(text):
    segs, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = IDRE.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return segs


def render(segs):
    out = []
    for bid, lines in segs:
        hl = [translate_line(l) for l in lines]
        for h in hl:
            check_clean(h)
        hl[-1] += f" ^{bid}"
        out.append("\n".join(hl))
    return out


def build_2_01():
    segs = segments((PALI_DIR / "2-01-cittuppadakandam.md").read_text(encoding="utf-8"))
    ids = [b for b, _ in segs]
    k = ids.index("1-57") + 1
    sample = SAMPLE.read_text(encoding="utf-8")
    assert sample.endswith(" ^1-57\n") and sample == C.TEXT
    return sample + "\n" + "\n\n".join(render(segs[k:])) + "\n", len(segs)


def build_2_02():
    segs = segments((PALI_DIR / "2-02-cittuppadakandam.md").read_text(encoding="utf-8"))
    return "\n\n".join(render(segs)) + "\n", len(segs)


def selftest():
    """Re-translate the sample's Pāli: every line must equal the approved sample, except the segments
    whose strings carry variant brackets (built by hand in the sample) and ^1-34 (amoho + root).
    ^1-1 is compared with all variant brackets removed on both sides."""
    pal = segments(SAMPLE_PALI.read_text(encoding="utf-8"))
    hin = segments(SAMPLE.read_text(encoding="utf-8"))
    skip = {"1-5", "1-13", "1-19", "1-33", "1-34", "1-40"}
    nob = lambda s: re.sub(r" \[[^\]]*\]", "", s)
    ok = bad = 0
    for (b, pl), (b2, hl) in zip(pal, hin):
        assert b == b2
        if b in skip:
            continue
        for p, h in zip(pl, hl):
            got = translate_line(nob(p)) if b == "1-1" else translate_line(p)
            exp = nob(h) if b == "1-1" else h
            if got == exp:
                ok += 1
            else:
                bad += 1
                print("SELFTEST MISMATCH", b, "\n  got:", got, "\n  exp:", exp)
    print(f"selftest: {ok} lines identical to the approved sample, {bad} mismatches")
    return bad == 0


if __name__ == "__main__":
    assert selftest()
    for name, fn in (("2-01-cittuppadakandam.md", build_2_01), ("2-02-cittuppadakandam.md", build_2_02)):
        text, n = fn()
        (OUT_DIR / name).write_text(text, encoding="utf-8", newline="\n")
        print("wrote", OUT_DIR / name, n, "segments")
