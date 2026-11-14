"""Build the Russian plain zero-shot of pi-1 parts 2-01 (after the approved sample) and 2-02.

usage: python -I -X utf8 build_2-01_2-02_ru.py          (runs the self-test, then builds both parts)

Importing this file does NOT build anything.
Method (mirrors the approved English builder): every Pāli line is translated by fixed formula strings.
The line translators raise KeyError on any Pāli they do not know, so nothing is guessed silently,
and every repeat is byte-identical by construction. 2-01 starts with the approved sample
(ch2-01-sample.md) byte for byte.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_ru as M  # noqa: E402  (importing does not write)
import build_ch2_01_sample_ru as C  # noqa: E402  (importing does not write)

PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters"
SAMPLE = HERE / "ch2-01-sample.md"
SAMPLE_PALI = HERE / "ref" / "ch2-01-pali-1-122.md"

DASH = C.DASH
PE, ELL = "…pe…", "…"
TASMIM = C.TASMIM
KUSALA = C.KUSALA


def cap(s):
    return s[:1].upper() + s[1:]


# =========================================================================================
# 1. Names: pali -> (nominative, instrumental, gender m/f/n)
# =========================================================================================
GENDER = {
    "phasso": "m", "vedanā": "n", "saññā": "n", "cetanā": "n", "cittaṃ": "m",
    "manindriyaṃ": "f",
}
NAME = {k: (C.NAMES[k], C.INS[k], GENDER.get(k, "")) for k in C.NAMES}
NAME.update({
    "upekkhā": ("невозмутимость", "невозмутимостью", "f"),
    "upekkhindriyaṃ": ("способность невозмутимости", "способностью невозмутимости", "f"),
    "vedanākkhandho": ("совокупность чувств", "совокупностью чувств", "f"),
    "saññākkhandho": ("совокупность восприятия", "совокупностью восприятия", "f"),
    "saṅkhārakkhandho": ("совокупность формирующих факторов", "совокупностью формирующих факторов", "f"),
    "viññāṇakkhandho": ("совокупность сознания", "совокупностью сознания", "f"),
    "manāyatanaṃ": ("сфера ума", "сферой ума", "f"),
    "dhammāyatanaṃ": ("сфера объектов ума", "сферой объектов ума", "f"),
    "manoviññāṇadhātu": ("элемент умственного сознания", "элементом умственного сознания", "m"),
    "dhammadhātu": ("элемент объектов ума", "элементом объектов ума", "m"),
    "phassāhāro": ("питание контактом", "питанием контактом", "n"),
    "manosañcetanāhāro": ("питание умственным намерением", "питанием умственным намерением", "n"),
    "viññāṇāhāro": ("питание сознанием", "питанием сознанием", "n"),
})
assert "совокупности чувств" in C.G_KAYA and "совокупности сознания" in C.G_CITTA

# Koṭṭhāsavāra: counted groups (nominative, instrumental)
COUNTED = {
    "cattāro khandhā": ("четыре совокупности", "четырьмя совокупностями"),
    "dvāyatanāni": ("две сферы восприятия", "двумя сферами восприятия"),
    "dve dhātuyo": ("два элемента", "двумя элементами"),
    "tayo āhārā": ("три вида питания", "тремя видами питания"),
    "aṭṭhindriyāni": ("восемь способностей", "восемью способностями"),
    "sattindriyāni": ("семь способностей", "семью способностями"),
    "pañcaṅgikaṃ jhānaṃ": ("пятичастное медитативное погружение", "пятичастным медитативным погружением"),
    "caturaṅgikaṃ jhānaṃ": ("четырёхчастное медитативное погружение", "четырёхчастным медитативным погружением"),
    "tivaṅgikaṃ jhānaṃ": ("трёхчастное медитативное погружение", "трёхчастным медитативным погружением"),
    "duvaṅgikaṃ jhānaṃ": ("двухчастное медитативное погружение", "двухчастным медитативным погружением"),
    "pañcaṅgiko maggo": ("пятичастный путь", "пятичастным путём"),
    "caturaṅgiko maggo": ("четырёхчастный путь", "четырёхчастным путём"),
    "satta balāni": ("семь сил", "семью силами"),
    "cha balāni": ("шесть сил", "шестью силами"),
    "tayo hetū": ("три корня", "тремя корнями"),
    "dve hetū": ("два корня", "двумя корнями"),
}
# Suññatavāra: bare group names
SUNNATA = {
    "dhammā": ("явления", "явлениями"),
    "khandhā": ("совокупности", "совокупностями"),
    "āyatanāni": ("сферы восприятия", "сферами восприятия"),
    "dhātuyo": ("элементы", "элементами"),
    "āhārā": ("виды питания", "видами питания"),
    "indriyāni": ("способности", "способностями"),
    "jhānaṃ": ("медитативное погружение", "медитативным погружением"),
    "maggo": ("путь", "путём"),
    "balāni": ("силы", "силами"),
    "hetū": ("корни", "корнями"),
}
ONE = {"m": ("один", "одним"), "f": ("одна", "одной"), "n": ("одно", "одним")}
ONE_PALI = {"eko": "m", "ekā": "f", "ekaṃ": "n"}  # Pāli gender, only checked for presence


def info(p):
    """pali name -> (nominative, instrumental)"""
    if p in COUNTED:
        return COUNTED[p]
    if p in SUNNATA:
        return SUNNATA[p]
    if p in NAME:
        return NAME[p][:2]
    m = re.fullmatch(r"(eko|ekā|ekaṃ) (\S+)", p)
    if m and m.group(2) in NAME:
        nom, ins, g = NAME[m.group(2)]
        if not g:
            raise KeyError("gender: " + p)
        return f"{ONE[g][0]} {nom}", f"{ONE[g][1]} {ins}"
    raise KeyError("name: " + p)


def q_ru(p):
    return f"Что {TASMIM} является {info(p)[1]}"


def this_ru(p):
    return f"это и есть {info(p)[0]} {TASMIM}"


def there_ru(p):
    return f"есть {info(p)[0]}"


assert q_ru("phasso") + "?" == C.Q("phasso")

# =========================================================================================
# 2. Synonym strings (Pāli string = Russian). The sample's STRINGS plus new ones.
# =========================================================================================
STR = dict(C.STRINGS)
S_PANNA_P = [k for k in C.STRINGS if k.startswith("paññā ")][0]
S_UPEKKHA_P = ("cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ "
               "cetosamphassajā adukkhamasukhā vedanā")
S_UPEKKHA = ("душевное состояние, которое ни отрадно, ни неотрадно, рождённое контактом ума переживание, "
             "которое ни болезненно, ни приятно, рождённое контактом ума чувство, которое ни болезненно, "
             "ни приятно")
STR[S_UPEKKHA_P] = S_UPEKKHA
STR[S_PANNA_P + " amoho kusalamūlaṃ"] = C.S_PANNA + ", " + C.N["amoho"] + ", " + C.ROOT
# abbreviated wisdom string (…pe… inside the string)
STR["paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi"] = (
    "мудрость, понимание… отсутствие заблуждения, исследование явлений, правильное воззрение")
assert C.S_PANNA.startswith("мудрость, понимание, ") and C.S_PANNA.endswith(
    ", отсутствие заблуждения, исследование явлений, правильное воззрение")

# qualifiers placed between «в это время» and «есть»
STR_PREFIX = [
    ("tajjāmanoviññāṇadhātusamphassajaṃ ", ", " + C.TAJJA + ","),
    ("tajjāmanoviññāṇadhātusamphassajā ", ", " + C.TAJJA + ","),
    ("vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa ", " " + C.G_KAYA),
    ("viññāṇakkhandhassa ", " " + C.G_CITTA),
]

# =========================================================================================
# 3. Variant brackets: all variants in these parts are spelling variants
# =========================================================================================
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "bahūsu": "во многих изданиях"}


def var_ru(br):
    m = re.fullmatch(r"\[(.+?) \(([^)]*)\)\]", br)
    words, sig = m.groups()
    return M.V("s", ", ".join(SIGLA[s] for s in sig.split()), words).strip()


# =========================================================================================
# 4. Tails: "ye vā pana …", "ayaṃ tasmiṃ samaye X hoti", "ime dhammā kusalā", "…pe…"
# =========================================================================================
YVP_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
YVP_R = "или же " + C.YEVAPANA_BODY
assert "Или же " + C.YEVAPANA() == cap(YVP_R) + ", " + DASH + " " + M.ANSWER(KUSALA)
THAP_P = "ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_R = "кроме совокупности чувств, кроме совокупности восприятия, кроме совокупности сознания"
THAP_PV = "ṭhapetvā [thapetvā (ka.)] vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_RV = THAP_R.replace("кроме ", "кроме " + var_ru("[thapetvā (ka.)]") + " ", 1)
KUSALA_P, KUSALA_R = "ime dhammā kusalā", M.ANSWER_BARE(KUSALA)
assert KUSALA_R + "." == M.ANSWER(KUSALA)


def tail_tr(t):
    t = t.replace(YVP_P + " " + THAP_PV + " " + DASH, YVP_R + ", " + THAP_RV + ", " + DASH)
    t = t.replace(YVP_P + " " + THAP_P + " " + DASH, YVP_R + ", " + THAP_R + ", " + DASH)
    t = t.replace(YVP_P + " " + DASH, YVP_R + ", " + DASH)
    assert YVP_P not in t, t
    t = re.sub(r"(?<!\S)(ayaṃ|idaṃ|ime|imāni|imā) tasmiṃ samaye (.+?) (hoti|honti)",
               lambda m: this_ru(m.group(2)), t)
    t = t.replace(KUSALA_P, KUSALA_R)
    t = t.replace(PE, ELL)
    return t


# =========================================================================================
# 5. Lists
# =========================================================================================
def there_list(s):
    """'phasso hoti, vedanā hoti…pe… avikkhepo hoti' -> 'есть контакт, есть чувство… есть …'"""
    parts = re.split(r"(?:(?<=hoti)|(?<=honti))(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p.replace(PE, ELL) if PE in p else ", ")
        else:
            m = re.fullmatch(r"(.+) (hoti|honti)", p)
            out.append(there_ru(m.group(1)))
    return "".join(out)


def name_list(s):
    """'Phasso cetanā…pe… avikkhepo' / 'Vedanākkhandho, saññākkhandho' -> Russian names, comma-separated"""
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


def str_ru(s):
    pre = ""
    for p, r in STR_PREFIX:
        if s.startswith(p):
            s, pre = s[len(p):], r
            break
    return pre, STR[s]


def answer_ru(a):
    m = ARE.fullmatch(a)
    if m:
        s, rest = m.groups()
        pre, sr = str_ru(s)
        if s.startswith(("hirīyati", "ottappati")):
            return f"То, что {TASMIM} {sr}, {DASH} " + tail_tr(rest)
        return f"То, что {TASMIM}{pre} есть {sr}, {DASH} " + tail_tr(rest)
    m = JRE.fullmatch(a)
    if m:
        s, rest = m.groups()
        return f"То, что {C.G_JIVITA} есть {STR[s]}, {DASH} " + tail_tr(rest)
    m = LRE.fullmatch(a)
    names, rest = m.groups()
    return cap(name_list(names)) + tail_tr(rest)


def qa_ru(line):
    m = QRE.fullmatch(line)
    name, verb, mark, rest = m.groups()
    q = q_ru(name)
    if mark == "?":
        return q + "? " + answer_ru(rest)
    return q + ELL + " " + tail_tr(rest)


# =========================================================================================
# 7. "Katame dhammā kusalā? Yasmiṃ samaye …" sentences: fixed phrase table
# =========================================================================================
Q_KUSALA = M.QUESTION(KUSALA)
INTROS = [
    # (Pāli, Russian, gender of the qualifiers hīnaṃ/majjhimaṃ/paṇītaṃ)
    ("rūpūpapattiyā maggaṃ bhāveti ",
     "В то время, когда человек, развивая путь к рождению в мире форм, ", "n"),
    ("arūpūpapattiyā maggaṃ bhāveti ",
     "В то время, когда человек, развивая путь к рождению в мире без форм, ", "n"),
    ("kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti ", C.OPEN_KAMA_KUSALA + ", ", "m"),
]
assert C.OPEN_KAMA_KUSALA.startswith("В то время, когда ")

# ordinal: (neuter accusative/nominative, preposition «в/во»)
ORD = {"paṭhamaṃ": ("первое", "в"), "dutiyaṃ": ("второе", "во"), "tatiyaṃ": ("третье", "в"),
       "catutthaṃ": ("четвёртое", "в"), "pañcamaṃ": ("пятое", "в")}
J = "медитативное погружение"
DWELL = "и пребывает в нём"
BORN = "с восторгом и счастьем, рождёнными"

# {V} marks where a variant bracket of that phrase goes (else it goes at the end of the phrase)
PH = {
    # --- the absorption formulas (full) -------------------------------------------------
    "vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ "
    "upasampajja viharati":
        f"полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений, входит в первое "
        f"{J}{{V}}, с направленной мыслью и удержанием мысли, {BORN} уединением",
    "vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ "
    "pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        f"с затиханием направленной мысли и удержания мысли входит во второе {J}{{V}}, с внутренней ясностью "
        f"и единением ума, без направленной мысли и без удержания мысли, {BORN} сосредоточением",
    "pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti yaṃ taṃ ariyā "
    "ācikkhanti – \"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati":
        f"с угасанием восторга пребывает невозмутимым, осознанным и ясно понимающим, испытывает телом счастье, "
        f"о котором благородные говорят {DASH} «Невозмутимый, осознанный, пребывающий в счастье», и входит "
        f"в третье {J}{{V}}",
    "sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ "
    "upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati":
        f"с устранением приятного и с устранением болезненного, с исчезновением ещё прежде радости и уныния "
        f"входит в четвёртое {J}{{V}}, которое ни болезненно, ни приятно, с чистотой осознанности благодаря "
        f"невозмутимости",
    "avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        f"входит во второе {J}{{V}}, без направленной мысли, только с удержанием мысли, {BORN} "
        f"сосредоточением",
    # --- the absorption formulas (opening words only, before …pe…) ---------------------
    "vivicceva kāmehi": "полностью уединившись от чувственных удовольствий",
    "vitakkavicārānaṃ vūpasamā": "с затиханием направленной мысли и удержания мысли",
    "pītiyā ca virāgā": "с угасанием восторга",
    "sukhassa ca pahānā": "с устранением приятного",
    # --- modes of practice ---------------------------------------------------------------
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "с трудным способом практики{V} и медленным высшим знанием",
    "dukkhapaṭipadaṃ khippābhiññaṃ": "с трудным способом практики{V} и быстрым высшим знанием",
    "sukhapaṭipadaṃ dandhābhiññaṃ": "с лёгким способом практики{V} и медленным высшим знанием",
    "sukhapaṭipadaṃ khippābhiññaṃ": "с лёгким способом практики{V} и быстрым высшим знанием",
    # --- the absorption and its object (neuter: agrees with «медитативное погружение») ----
    "parittaṃ parittārammaṇaṃ": "ограниченное и с ограниченным объектом",
    "parittaṃ appamāṇārammaṇaṃ": "ограниченное и с безмерным объектом",
    "appamāṇaṃ parittārammaṇaṃ": "безмерное и с ограниченным объектом",
    "appamāṇaṃ appamāṇārammaṇaṃ": "безмерное и с безмерным объектом",
    # --- all-encompassing objects (kasiṇa) ------------------------------------------------
    "pathavīkasiṇaṃ": "на всеохватном объекте земли",
    "āpokasiṇaṃ": "на всеохватном объекте воды",
    "tejokasiṇaṃ": "на всеохватном объекте огня",
    "vāyokasiṇaṃ": "на всеохватном объекте воздуха",
    "nīlakasiṇaṃ": "на синем всеохватном объекте",
    "pītakasiṇaṃ": "на жёлтом всеохватном объекте",
    "lohitakasiṇaṃ": "на красном всеохватном объекте",
    "odātakasiṇaṃ": "на белом всеохватном объекте",
    # --- spheres of overcoming (abhibhāyatana) ---------------------------------------------
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati":
        "не воспринимая материальной формы внутри себя, видя видимые формы вовне",
    "parittāni": "ограниченные",
    "appamāṇāni": "безмерные",
    "suvaṇṇadubbaṇṇāni": "красивые и некрасивые",
    "nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni": "синие, синего цвета, синие на вид, с синим сиянием",
    "pītāni pītavaṇṇāni pītanidassanāni pītanibhāsāni": "жёлтые, жёлтого цвета, жёлтые на вид, с жёлтым сиянием",
    "lohitakāni lohitakavaṇṇāni lohitakanidassanāni lohitakanibhāsāni":
        "красные, красного цвета, красные на вид, с красным сиянием",
    "odātāni odātavaṇṇāni odātanidassanāni odātanibhāsāni": "белые, белого цвета, белые на вид, с белым сиянием",
    "tāni abhibhuyya jānāmi passāmīti": "преодолев их с мыслью: «Я знаю, я вижу»",
    # --- liberations ------------------------------------------------------------------------
    "rūpī rūpāni passati": "обладая материальной формой, видя видимые формы",
    "subhanti": "с мыслью: «Прекрасно»",
    # --- divine abidings ----------------------------------------------------------------------
    "mettāsahagataṃ": "сопровождаемое доброжелательностью",
    "karuṇāsahagataṃ": "сопровождаемое состраданием",
    "muditāsahagataṃ": "сопровождаемое сорадованием",
    "upekkhāsahagataṃ": "сопровождаемое невозмутимостью",
    # --- the unattractive ------------------------------------------------------------------------
    "uddhumātakasaññāsahagataṃ": "сопровождаемое восприятием вздувшегося трупа",
    "vinīlakasaññāsahagataṃ": "сопровождаемое восприятием посиневшего трупа",
    "vipubbakasaññāsahagataṃ": "сопровождаемое восприятием гноящегося трупа",
    "vicchiddakasaññāsahagataṃ": "сопровождаемое восприятием разрубленного трупа",
    "vikkhāyitakasaññāsahagataṃ": "сопровождаемое восприятием объеденного трупа",
    "vikkhittakasaññāsahagataṃ": "сопровождаемое восприятием разбросанного трупа",
    "hatavikkhittakasaññāsahagataṃ": "сопровождаемое восприятием изрубленного и разбросанного трупа",
    "lohitakasaññāsahagataṃ": "сопровождаемое восприятием кровоточащего трупа",
    "puḷavakasaññāsahagataṃ": "сопровождаемое восприятием кишащего червями трупа",
    "aṭṭhikasaññāsahagataṃ": "сопровождаемое восприятием скелета",
    # --- the absorptions of the world without forms ----------------------------------------
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā":
        "полностью преодолев восприятия материальной формы, с исчезновением восприятий соударения, "
        "не уделяя внимания восприятиям разнообразия",
    "ākāsānañcāyatanasaññāsahagataṃ": "с восприятием сферыбесконечного пространства",
    "sabbaso ākāsānañcāyatanaṃ samatikkamma": "полностью преодолев сферу бесконечного пространства",
    "viññāṇañcāyatanasaññāsahagataṃ": "с восприятием сферыбесконечного сознания",
    "sabbaso viññāṇañcāyatanaṃ samatikkamma": "полностью преодолев сферу бесконечного сознания",
    "ākiñcaññāyatanasaññāsahagataṃ": "с восприятием сферыотсутствия чего-либо",
    "sabbaso ākiñcaññāyatanaṃ samatikkamma": "полностью преодолев сферу отсутствия чего-либо",
    "nevasaññānāsaññāyatanasaññāsahagataṃ":
        "с восприятием сферыни восприятия, ни невосприятия",
    # --- level (gendered, see PHG) and dominant factor -------------------------------------
    "chandādhipateyyaṃ": "при преобладании желания",
    "vīriyādhipateyyaṃ": "при преобладании усердия",
    "cittādhipateyyaṃ": "при преобладании ума",
    "vīmaṃsādhipateyyaṃ": "при преобладании пытливости",
    # --- the eight wholesome minds of the world of sense desires (masculine: «ум») ---------
    "somanassasahagataṃ ñāṇasampayuttaṃ": C.ACC_SOMA_NANA,
    "somanassasahagataṃ ñāṇavippayuttaṃ": "сопровождаемый радостью и не связанный со знанием",
    "upekkhāsahagataṃ ñāṇasampayuttaṃ": "сопровождаемый невозмутимостью и связанный со знанием",
    "upekkhāsahagataṃ ñāṇavippayuttaṃ": "сопровождаемый невозмутимостью и не связанный со знанием",
    "sasaṅkhārena": "с побуждением",
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": C.ARAMMANA,
    "rūpārammaṇaṃ vā": "имеющий объектом видимую форму",
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": "или объект ума, или что бы то ни было",
}
assert C.ARAMMANA.startswith(PH["rūpārammaṇaṃ vā"] + ", ")
assert C.ARAMMANA.endswith(", " + PH["dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"])
for p, (o, prep) in ORD.items():
    PH[f"{p} jhānaṃ upasampajja viharati"] = f"входит {prep} {o} {J}{{V}}"
    PH[f"{p} jhānaṃ"] = f"{o} {J}{{V}}"
PHG = {  # gendered qualifiers: m agrees with «ум», n with «медитативное погружение»
    "hīnaṃ": {"m": "низший", "n": "низшее"},
    "majjhimaṃ": {"m": "средний", "n": "среднее"},
    "paṇītaṃ": {"m": "высший", "n": "высшее"},
}
PH_MAX = max(len(k.split()) for k in PH)


def chunk_tr(part, gender):
    words = []
    for t in re.findall(r"\[[^\]]*\]|[^\s\[]+", part):
        if t.startswith("["):
            words[-1][1].append(var_ru(t))
        else:
            words.append([t.rstrip(","), []])
    res, i = [], 0
    while i < len(words):
        for L in range(min(PH_MAX, len(words) - i), 0, -1):
            key = " ".join(w for w, _ in words[i:i + L])
            if key in PH or (L == 1 and key in PHG):
                break
        else:
            raise KeyError("phrase: " + " ".join(w for w, _ in words[i:]))
        ru = PH[key] if key in PH else PHG[key][gender]
        vs = [v for _, vv in words[i:i + L] for v in vv]
        if vs:
            vt = " " + " ".join(vs)
            ru = ru.replace("{V}", vt) if "{V}" in ru else ru + vt
        res.append(ru.replace("{V}", ""))
        i += L
    return ", ".join(res)


def x_tr(x, gender):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(part.replace(PE, ELL))
        elif part.strip():
            out.append(chunk_tr(part, gender))
    return "".join(out)


def kusala_ru(line):
    body = line[len("Katame dhammā kusalā? Yasmiṃ samaye "):]
    for p, r, g in INTROS:
        if body.startswith(p):
            body, intro, gender = body[len(p):], r, g
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
        sep = ","  # ^1-189: the Pāli has no comma here; Russian punctuation requires one
    m = re.fullmatch(r"(.*? hoti)(…pe… ime dhammā kusalā.*|; ye vā pana.*)", rest)
    xr = x_tr(x, gender)
    if "upasampajja viharati" in x:
        # «upasampajja viharati» = «входит в … и пребывает в нём»; «и пребывает в нём» closes the whole
        # qualifier chain, so that the qualifiers that follow in the Pāli (kasiṇa, mode of practice,
        # object, sahagata, level …) agree with «медитативное погружение»
        assert x.count("upasampajja viharati") == 1
        xr += (" " if re.search(J + r"( \[[^\]]*\])?$", xr) else ", ") + DWELL
    return (Q_KUSALA + " " + intro + xr + sep + f" {TASMIM} " + there_list(m.group(1))
            + tail_tr(m.group(2)))


def summary_ru(line):
    """'Tasmiṃ kho pana samaye cattāro khandhā honti, …; ye vā pana …' (Koṭṭhāsa / Suññata summaries)"""
    body = line[len("Tasmiṃ kho pana samaye "):]
    items, rest = body.split(";", 1)
    return f"И {TASMIM} " + there_list(items) + ";" + tail_tr(rest)


# =========================================================================================
# 8. Headings and closing lines (exact; headings from ru-zeroshot-terms.md)
# =========================================================================================
H_KAMA = C.H_KAMA_KUSALA[len("#### "):]  # «Благой ум, относящийся к миру чувственных желаний»
H_RUPA = "Благой ум, относящийся к миру форм"
H_ARUPA = "Благой ум, относящийся к миру без форм"
SIXTEEN = "шестнадцатикратный разбор"
EXACT = {
    "Padabhājanīyaṃ.": C.END_PADA,
    "Paṭhamabhāṇavāro.": C.END_BHANA1,
    "##### Koṭṭhāsavāro": "##### Раздел о составных частях",
    "Koṭṭhāsavāro.": "Раздел о составных частях.",
    "##### Suññatavāro": "##### Раздел о пустоте",
    "Suññatavāro.": "Раздел о пустоте.",
    "Paṭhamaṃ cittaṃ.": "Первый вид ума.",
    "Dutiyaṃ cittaṃ.": "Второй вид ума.",
    "Tatiyaṃ cittaṃ.": "Третий вид ума.",
    "Catutthaṃ cittaṃ.": "Четвёртый вид ума.",
    "Pañcamaṃ cittaṃ.": "Пятый вид ума.",
    "Chaṭṭhaṃ cittaṃ.": "Шестой вид ума.",
    "Sattamaṃ cittaṃ.": "Седьмой вид ума.",
    "Aṭṭhamaṃ cittaṃ.": "Восьмой вид ума.",
    "Aṭṭha kāmāvacaramahākusalacittāni.":
        "Восемь великих благих видов ума, относящихся к миру чувственных желаний.",
    "Dutiyabhāṇavāro.": "Второй раздел для чтения вслух.",
    # 2-02
    "#### Rūpāvacarakusalaṃ": "#### " + H_RUPA,
    "#### Arūpāvacarakusalaṃ": "#### " + H_ARUPA,
    "#### Tebhūmakakusalaṃ": "#### Благой ум трёх миров",
    "##### Kāmāvacarakusalaṃ": "##### " + H_KAMA,
    "##### Rūpāvacarakusalaṃ": "##### " + H_RUPA,
    "##### Arūpāvacarakusalaṃ": "##### " + H_ARUPA,
    "Kāmāvacarakusalaṃ.": H_KAMA + ".",
    "Rūpāvacarakusalaṃ.": H_RUPA + ".",
    "Arūpāvacarakusalaṃ.": H_ARUPA + ".",
    "##### Catukkanayo": "##### Четверичный метод",
    "Catukkanayo.": "Четверичный метод.",
    "##### Pañcakanayo": "##### Пятеричный метод",
    "Pañcakanayo.": "Пятеричный метод.",
    "##### Catasso paṭipadā": "##### Четыре способа практики",
    "Catasso paṭipadā.": "Четыре способа практики.",
    "##### Cattāri ārammaṇāni": "##### Четыре вида объектов",
    "Cattāri ārammaṇāni.": "Четыре вида объектов.",
    "##### Dve ārammaṇāni": "##### Два вида объектов",
    "Dve ārammaṇāni.": "Два вида объектов.",
    "##### Soḷasakkhattukaṃ": "##### Шестнадцатикратный разбор",
    "Soḷasakkhattukaṃ.": "Шестнадцатикратный разбор.",
    "##### Aṭṭhakkhattukaṃ": "##### Восьмикратный разбор",
    "Aṭṭhakkhattukaṃ.": "Восьмикратный разбор.",
    "##### Idampi aṭṭhakkhattukaṃ": "##### Это тоже восьмикратный разбор",
    "Idampi aṭṭhakkhattukaṃ.": "Это тоже восьмикратный разбор.",
    "##### Aparampi aṭṭhakkhattukaṃ": "##### Ещё один восьмикратный разбор",
    "Aparampi aṭṭhakkhattukaṃ.": "Ещё один восьмикратный разбор.",
    "##### Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": f"##### Восемь всеохватных объектов, {SIXTEEN}",
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ.": f"Восемь всеохватных объектов, {SIXTEEN}.",
    "##### Abhibhāyatanāni parittāni": "##### Ограниченные сферы преодоления",
    "##### Appamāṇāni": "##### Безмерные",
    "Imānipi abhibhāyatanāni soḷasakkhattukāni.":
        f"Эти сферы преодоления тоже даны в шестнадцатикратном разборе.",
    "##### Tīṇi vimokkhāni soḷasakkhattukāni": f"##### Три освобождения, {SIXTEEN}",
    "Imānipi tīṇi vimokkhāni soḷasakkhattukāni.": "Эти три освобождения тоже даны в шестнадцатикратном разборе.",
    "##### Cattāri brahmavihārajhānāni soḷasakkhattukāni":
        f"##### Четыре медитативных погружения божественных обителей, {SIXTEEN}",
    "Cattāri brahmavihārajhānāni [brahmavihārajjhānāni (sī. syā.)] soḷasakkhattukāni.":
        "Четыре медитативных погружения божественных обителей"
        + M.V("s", "Sī., Syā.", "brahmavihārajjhānāni") + f", {SIXTEEN}.",
    "##### Asubhajhānaṃ soḷasakkhattukaṃ": f"##### Медитативное погружение на непривлекательном, {SIXTEEN}",
    "Asubhajhānaṃ [asubhajjhānaṃ (sī. syā.)] soḷasakkhattukaṃ.":
        "Медитативное погружение на непривлекательном" + M.V("s", "Sī., Syā.", "asubhajjhānaṃ")
        + f", {SIXTEEN}.",
    "##### Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni":
        "##### Четыре медитативных погружения мира без форм" + M.V("s", "Sī., Syā.", "arūpajjhānāni")
        + f", {SIXTEEN}",
    "Cattāri arūpajhānāni soḷasakkhattukāni.": f"Четыре медитативных погружения мира без форм, {SIXTEEN}.",
}
assert EXACT["##### Kāmāvacarakusalaṃ"] == "#" + C.H_KAMA_KUSALA

# =========================================================================================
# 9. Line dispatch, segments, build
# =========================================================================================
IDRE = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def translate_line(line):
    if line in EXACT:
        return EXACT[line]
    if line.startswith("Katame dhammā kusalā? Yasmiṃ samaye "):
        return kusala_ru(line)
    if line.startswith("Tasmiṃ kho pana samaye "):
        return summary_ru(line)
    if QRE.fullmatch(line):
        return qa_ru(line)
    if line.startswith("Ye vā pana ") or re.match(r"(Ime|Imāni|Imā|Idaṃ|Ayaṃ) tasmiṃ samaye ", line):
        return cap(tail_tr(line[0].lower() + line[1:]))
    raise KeyError("line: " + line[:80])


PALI_CHARS = set("āīūṃṅñṭḍṇḷ")


def check_line(pali, ru):
    bare = re.sub(r"\[вариант [^\]]*\]", "", ru)
    bad = PALI_CHARS & set(bare)
    assert not bad, (bad, ru[:120])
    assert not re.search(r"[A-Za-z]", bare), ru[:120]
    assert "—" not in ru and ":-" not in ru
    assert pali.count(DASH) == ru.count(DASH), (pali[:80], ru[:120])
    assert not re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", ru), ru[:120]


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
        ru = [cap(translate_line(l)) for l in lines]
        for p, r in zip(lines, ru):
            check_line(p, r)
        ru[-1] += f" ^{bid}"
        out.append("\n".join(ru))
    return out


def build_2_01():
    segs = segments((PALI_DIR / "2-01-cittuppadakandam.md").read_text(encoding="utf-8"))
    ids = [b for b, _ in segs]
    k = ids.index("1-57") + 1
    sample = SAMPLE.read_bytes().decode("utf-8")
    assert sample.endswith(" ^1-57\n") and sample == C.TEXT
    return sample + "\n" + "\n\n".join(render(segs[k:])) + "\n", len(segs)


def build_2_02():
    segs = segments((PALI_DIR / "2-02-cittuppadakandam.md").read_text(encoding="utf-8"))
    return "\n\n".join(render(segs)) + "\n", len(segs)


def selftest():
    """Run the translators on the sample's Pāli; every line must equal the approved sample, except
    headings and the segments whose strings carry variant brackets (built by hand in the sample)."""
    pal = segments(SAMPLE_PALI.read_text(encoding="utf-8"))
    rus = segments(SAMPLE.read_text(encoding="utf-8"))
    skip = {"1-1-0", "1-1-1-0", "1-1-1-1-0", "1-1", "1-5", "1-13", "1-19", "1-33", "1-40"}
    ok = bad = 0
    for (b, pl), (b2, rl) in zip(pal, rus):
        assert b == b2
        if b in skip:
            continue
        for p, r in zip(pl, rl):
            got = cap(translate_line(p))
            if got == r:
                ok += 1
            else:
                bad += 1
                print("SELFTEST MISMATCH", b, "\n  got:", got, "\n  exp:", r)
    print(f"selftest: {ok} lines identical to the approved sample, {bad} mismatches")
    return bad == 0


if __name__ == "__main__":
    assert selftest()
    for name, fn in (("2-01-cittuppadakandam.md", build_2_01), ("2-02-cittuppadakandam.md", build_2_02)):
        text, n = fn()
        assert "\r" not in text and "\n\n\n" not in text
        (OUT_DIR / name).write_bytes(text.encode("utf-8"))
        print("wrote", OUT_DIR / name, n, "segments")
