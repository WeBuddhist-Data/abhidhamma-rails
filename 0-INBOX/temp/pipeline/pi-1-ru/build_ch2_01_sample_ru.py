"""Build the Russian plain zero-shot SAMPLE of pi-1 ch.2 opening (^1-1-0 ... ^1-57).

usage: python -I -X utf8 build_ch2_01_sample_ru.py
All recurring strings are fixed constants below, so every repeat is byte-identical.
Importing this module does not write the file. Exposes NAMES (nominative), INS (instrumental),
STRINGS, FRAMES and the frame functions (Q, A, QA, T, KAYA, CITTA, JIVITA, SHAME, LIST_ITEM, YEVAPANA)
for later chapters.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_matika_ru import BARE, QUESTION, ANSWER, V  # noqa: E402

PALI = HERE / "ref" / "ch2-01-pali-1-122.md"
OUT = HERE / "ch2-01-sample.md"

DASH = "–"  # the en dash used by the Pāli source; only where the Pāli has one

KUSALA = ("1-M1-1", "а")      # благие явления
AKUSALA = ("1-M1-1", "б")     # неблагие явления
ABYAKATA = ("1-M1-1", "в")    # этически неопределённые явления

# ---- headings ------------------------------------------------------------------------
H_CH2 = "### Раздел о возникновении ума"
H_KAMA_KUSALA = "#### Благой ум, относящийся к миру чувственных желаний"
H_PADA = "##### Разбор терминов"
END_PADA = "Разбор терминов."
END_BHANA1 = "Первый раздел для чтения вслух."

# ---- names of the factors: Pāli = (nominative, instrumental) ---------------------------
# nominative: list of ^1-1 («есть X») and the answer («это и есть X в это время»);
# instrumental: the question («Что в это время является X?»).
KAYA_N = "умственного тела"   # kāya- in kāyapassaddhi … kāyujukatā (the three mental aggregates)
CITTA_N = "ума"


def pair(nom, ins):
    """(kāya-X, citta-X) names from the head noun in both cases."""
    return ((f"{nom} {KAYA_N}", f"{ins} {KAYA_N}"), (f"{nom} {CITTA_N}", f"{ins} {CITTA_N}"))


_PASS = pair("безмятежность", "безмятежностью")
_LAHU = pair("лёгкость", "лёгкостью")
_MUDU = pair("мягкость", "мягкостью")
_KAMM = pair("работоспособность", "работоспособностью")
_PAGU = pair("натренированность", "натренированностью")
_UJU = pair("прямота", "прямотой")

NAMES_C = {
    "phasso": ("контакт", "контактом"),
    "vedanā": ("чувство", "чувством"),
    "saññā": ("восприятие", "восприятием"),
    "cetanā": ("намерение", "намерением"),
    "cittaṃ": ("ум", "умом"),
    "vitakko": ("направленная мысль", "направленной мыслью"),
    "vicāro": ("удержание мысли", "удержанием мысли"),
    "pīti": ("восторг", "восторгом"),
    "sukhaṃ": ("счастье", "счастьем"),
    "cittassekaggatā": ("однонаправленность ума", "однонаправленностью ума"),
    "saddhindriyaṃ": ("способность веры", "способностью веры"),
    "vīriyindriyaṃ": ("способность усердия", "способностью усердия"),
    "satindriyaṃ": ("способность осознанности", "способностью осознанности"),
    "samādhindriyaṃ": ("способность сосредоточения", "способностью сосредоточения"),
    "paññindriyaṃ": ("способность мудрости", "способностью мудрости"),
    "manindriyaṃ": ("способность ума", "способностью ума"),
    "somanassindriyaṃ": ("способность радости", "способностью радости"),
    "jīvitindriyaṃ": ("жизненная способность", "жизненной способностью"),
    "sammādiṭṭhi": ("правильное воззрение", "правильным воззрением"),
    "sammāsaṅkappo": ("правильный помысел", "правильным помыслом"),
    "sammāvāyāmo": ("правильное усилие", "правильным усилием"),
    "sammāsati": ("правильная осознанность", "правильной осознанностью"),
    "sammāsamādhi": ("правильное сосредоточение", "правильным сосредоточением"),
    "saddhābalaṃ": ("сила веры", "силой веры"),
    "vīriyabalaṃ": ("сила усердия", "силой усердия"),
    "satibalaṃ": ("сила осознанности", "силой осознанности"),
    "samādhibalaṃ": ("сила сосредоточения", "силой сосредоточения"),
    "paññābalaṃ": ("сила мудрости", "силой мудрости"),
    "hiribalaṃ": ("сила совестливости", "силой совестливости"),
    "ottappabalaṃ": ("сила страха перед дурным", "силой страха перед дурным"),
    "alobho": ("отсутствие жадности", "отсутствием жадности"),
    "adoso": ("отсутствие злобы", "отсутствием злобы"),
    "amoho": ("отсутствие заблуждения", "отсутствием заблуждения"),
    "anabhijjhā": ("отсутствие алчности", "отсутствием алчности"),
    "abyāpādo": ("отсутствие недоброжелательности", "отсутствием недоброжелательности"),
    "hirī": ("совестливость", "совестливостью"),
    "ottappaṃ": ("страх перед дурным", "страхом перед дурным"),
    "kāyapassaddhi": _PASS[0], "cittapassaddhi": _PASS[1],
    "kāyalahutā": _LAHU[0], "cittalahutā": _LAHU[1],
    "kāyamudutā": _MUDU[0], "cittamudutā": _MUDU[1],
    "kāyakammaññatā": _KAMM[0], "cittakammaññatā": _KAMM[1],
    "kāyapāguññatā": _PAGU[0], "cittapāguññatā": _PAGU[1],
    "kāyujukatā": _UJU[0], "cittujukatā": _UJU[1],
    "sati": ("осознанность", "осознанностью"),
    "sampajaññaṃ": ("ясное понимание", "ясным пониманием"),
    "samatho": ("успокоение", "успокоением"),
    "vipassanā": ("прозрение", "прозрением"),
    "paggāho": ("напряжение сил", "напряжением сил"),
    "avikkhepo": ("отсутствие отвлечения", "отсутствием отвлечения"),
}
NAMES = {k: v[0] for k, v in NAMES_C.items()}
INS = {k: v[1] for k, v in NAMES_C.items()}
N = NAMES

# ---- fixed synonym strings (Pāli string = Russian string) -----------------------------
TAJJA = "рождённое контактом соответствующего элемента умственного сознания"  # agrees with «то, что»
G_KAYA = "в совокупности чувств, совокупности восприятия и совокупности формирующих факторов"
G_CITTA = "в совокупности сознания"
G_JIVITA = "у этих нематериальных явлений"
ROOT = "благой корень"

STRINGS = {
    "phasso phusanā saṃphusanā saṃphusitattaṃ":
        "контакт, касание, соприкосновение, состояние соприкосновения",
    "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        "душевная отрада, душевное счастье, рождённое контактом ума отрадное и приятное переживание, "
        "рождённое контактом ума отрадное и приятное чувство",
    "saññā sañjānanā sañjānitattaṃ":
        "восприятие, узнавание, состояние узнавания",
    "cetanā sañcetanā cetayitattaṃ":
        "намерение, проявление намерения, состояние намеренности",
    "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu":
        "ум, разум, умственная деятельность, сердце, чистота, разум, сфера ума, способность ума, "
        "сознание, совокупность сознания, соответствующий элемент умственного сознания",
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo":
        "мышление, направленная мысль, помысел, прикрепление мысли, прочное прикрепление мысли, "
        "направление ума на объект, правильный помысел",
    "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā":
        "движение мысли, удержание мысли, продолжительное удержание мысли, пристальное удержание мысли, "
        "непрерывная связь ума с объектом, неотрывное наблюдение за объектом",
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa":
        "восторг, ликование, веселье, оживление, весёлость, бурная весёлость, удовлетворённость, "
        "воодушевление, довольство ума",
    "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ sammāsamādhi":
        "устойчивость ума, его собранность, его стабильность, отсутствие рассеяния, отсутствие отвлечения, "
        "нерассеянность ума, успокоение, способность сосредоточения, сила сосредоточения, "
        "правильное сосредоточение",
    "saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ":
        "вера, доверие, уверенность, глубокая убеждённость, вера, способность веры, сила веры",
    "cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā "
    "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo":
        "душевное приложение усердия, порыв, напор, старание, усилие, рвение, упорство, стойкость, твёрдость, "
        "неослабевающий напор, неотступное желание, неотступное несение бремени, крепкое удержание бремени, "
        "усердие, способность усердия, сила усердия, правильное усилие",
    # sati and paññā strings: the approved Russian pi-4 wording (^4-79, ^4-80);
    # only «правильные взгляды» -> «правильное воззрение» (diṭṭhi = воззрение)
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati":
        "осознанность, припоминание, воспоминание, осознанность, способность помнить, "
        "способность удерживать в памяти, отсутствие поверхностности, отсутствие забывчивости, "
        "осознанность, способность осознанности, сила осознанности, правильная осознанность",
    "paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā "
    "paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
    "amoho dhammavicayo sammādiṭṭhi":
        "мудрость, понимание, исследование, тщательное исследование, исследование явлений, различение, "
        "распознавание, точное распознавание, учёность, умелость, тонкость, ясность суждения, размышление, "
        "проверка, широта ума, разумность, руководящая сила, прозрение, ясное понимание, стрекало, мудрость, "
        "способность мудрости, сила мудрости, меч мудрости, башня мудрости, свет мудрости, сияние мудрости, "
        "светоч мудрости, сокровище мудрости, отсутствие заблуждения, исследование явлений, "
        "правильное воззрение",
    "āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        "срок жизни, сохранение, поддержание, продление, движение, течение, сбережение, жизнь, "
        "жизненная способность",
    # hirī / ottappa strings: the approved Russian pi-4 wording (^4-73, ^4-74), verbatim
    "hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        "человек стыдится того, чего следует стыдиться, стыдится допускать в себе дурные неблагие явления",
    "ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        "человек боится того, чего следует бояться, боится допускать в себе дурные неблагие явления",
    "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ":
        "отсутствие жадности, непроявление жадности, свобода от жадности, отсутствие страсти, "
        "непроявление страсти, свобода от страсти, отсутствие алчности, отсутствие жадности, " + ROOT,
    "adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ":
        "отсутствие злобы, непроявление злобы, свобода от злобы, отсутствие недоброжелательности, "
        "отсутствие неприязни, отсутствие злобы, " + ROOT,
    "passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ":
        "безмятежность, полная безмятежность, утихание, полное утихание, состояние полного утихания",
    "lahutā lahupariṇāmatā adandhanatā avitthanatā":
        "лёгкость, быстрота перемен, отсутствие медлительности, отсутствие скованности",
    "mudutā maddavatā akakkhaḷatā akathinatā":
        "мягкость, гибкость, отсутствие грубости, отсутствие жёсткости",
    "kammaññatā kammaññattaṃ kammaññabhāvo":
        "работоспособность, состояние работоспособности, свойство быть работоспособным",
    "paguṇatā paguṇattaṃ paguṇabhāvo":
        "натренированность, состояние натренированности, свойство быть натренированным",
    "ujutā ujukatā ajimhatā avaṅkatā akuṭilatā":
        "прямота, прямизна, отсутствие кривизны, отсутствие изогнутости, отсутствие извилистости",
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

# variant-bearing forms (first occurrences in ^1-5, ^1-13, ^1-19, ^1-33, ^1-40)
S_CETANA_V = S_CETANA + V("p", "Syā.", "sañcetayitattaṃ")
S_VIRIYA_V = (S_VIRIYA
              .replace("душевное приложение усердия,",
                       "душевное приложение усердия" + V("s", "Sī., Syā.", "viriyārambho") + ",", 1)
              .replace(" упорство,", " упорство" + V("s", "Sī.", "ussoḷhi") + ",", 1))
S_JIVITA_V = S_JIVITA.replace(" движение,", " движение" + V("s", "Sī.", "irīyanā") + ",", 1)
S_ADOSA_V = S_ADOSA.replace("свобода от злобы,",
                            "свобода от злобы" + V("s", "Syā.", "adūsanā adūsitattaṃ") + ",", 1)
S_PASSADDHI_V = (S_PASSADDHI
                 .replace("полная безмятежность,",
                          "полная безмятежность" + V("s", "Sī., Syā.", "paṭippassaddhi") + ",", 1)
                 .replace("полное утихание,",
                          "полное утихание" + V("s", "Sī., Syā.", "paṭippassambhanā") + ",", 1)
                 + V("s", "Sī., Syā.", "paṭippassambhitattaṃ"))
for a, b, n in ((S_CETANA, S_CETANA_V, 1), (S_VIRIYA, S_VIRIYA_V, 2), (S_JIVITA, S_JIVITA_V, 1),
                (S_ADOSA, S_ADOSA_V, 1), (S_PASSADDHI, S_PASSADDHI_V, 3)):
    assert b.count("[") == n, b

# ---- frames ----------------------------------------------------------------------------
OPEN_KAMA_KUSALA = "В то время, когда возникает благой ум, относящийся к миру чувственных желаний"
ACC_SOMA_NANA = "сопровождаемый радостью и связанный со знанием"
ARAMMANA = ("имеющий объектом видимую форму, или звук, или запах, или вкус, или осязаемое, "
            "или объект ума, или что бы то ни было")
TASMIM = "в это время"  # tasmiṃ samaye
YEVAPANA_BODY = "любые другие нематериальные явления, возникшие в зависимости от условий, какие есть в это время"


def YEVAPANA(item=KUSALA):
    """'ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā X.'
    (without the opening «или же»)"""
    return f"{YEVAPANA_BODY}, {DASH} {ANSWER(item)}"


def Q(key):
    """'Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti?'"""
    return f"Что {TASMIM} является {INS[key]}?"


def A(s, key, mid=""):
    """'Yo/Yā/Yaṃ tasmiṃ samaye [mid] S – ayaṃ/idaṃ tasmiṃ samaye X hoti.'"""
    return f"То, что {TASMIM}{mid} есть {s}, {DASH} это и есть {N[key]} {TASMIM}."


def QA(key, s, mid="", end="."):
    a = A(s, key, mid)
    if end != ".":
        a = a[:-1] + end
    return Q(key) + " " + a


def T(key, s):
    """with tajjāmanoviññāṇadhātusamphassaja-"""
    return QA(key, s, ", " + TAJJA + ",")


def KAYA(key, s):
    return QA(key, s, " " + G_KAYA)


def CITTA(key, s):
    return QA(key, s, " " + G_CITTA)


def JIVITA(key, s):
    """'Yo tesaṃ arūpīnaṃ dhammānaṃ S – idaṃ tasmiṃ samaye X hoti.' (no tasmiṃ samaye at the start)"""
    return Q(key) + f" То, что {G_JIVITA} есть {s}, {DASH} это и есть {N[key]} {TASMIM}."


def SHAME(key, s):
    """'Yaṃ tasmiṃ samaye hirīyati … / ottappati … – idaṃ/ayaṃ tasmiṃ samaye X hoti.'"""
    return Q(key) + f" То, что {TASMIM} {s}, {DASH} это и есть {N[key]} {TASMIM}."


def LIST_ITEM(key, var=""):
    """'X hoti' inside the list of ^1-1: «есть X»."""
    return f"есть {N[key]}{var}"


FRAMES = {
    "Katame dhammā kusalā?": QUESTION(KUSALA),
    "ime dhammā kusalā (after the Pāli –)": ANSWER(KUSALA),
    "Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti?": f"Что {TASMIM} является X (творительный падеж)?",
    "Yo/Yā/Yaṃ tasmiṃ samaye S – ayaṃ/idaṃ tasmiṃ samaye X hoti.":
        f"То, что {TASMIM} есть S, {DASH} это и есть X {TASMIM}.",
    "Yā/Yaṃ tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajā/-jaṃ S – ayaṃ tasmiṃ samaye X hoti.":
        f"То, что {TASMIM}, {TAJJA}, есть S, {DASH} это и есть X {TASMIM}.",
    "Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa S – ayaṃ tasmiṃ samaye X hoti.":
        f"То, что {TASMIM} {G_KAYA} есть S, {DASH} это и есть X {TASMIM}.",
    "Yā tasmiṃ samaye viññāṇakkhandhassa S – ayaṃ tasmiṃ samaye X hoti.":
        f"То, что {TASMIM} {G_CITTA} есть S, {DASH} это и есть X {TASMIM}.",
    "Yo tesaṃ arūpīnaṃ dhammānaṃ S – idaṃ tasmiṃ samaye X hoti.":
        f"То, что {G_JIVITA} есть S, {DASH} это и есть X {TASMIM}.",
    "Yaṃ tasmiṃ samaye hirīyati… / ottappati… – idaṃ/ayaṃ tasmiṃ samaye X hoti.":
        f"То, что {TASMIM} S, {DASH} это и есть X {TASMIM}.",
    "Ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā.":
        "Или же " + YEVAPANA(),
    "Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti": OPEN_KAMA_KUSALA,
    "somanassasahagataṃ ñāṇasampayuttaṃ": ACC_SOMA_NANA,
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": ARAMMANA,
    "tasmiṃ samaye X hoti, Y hoti, …": f"{TASMIM} есть X, есть Y, …",
    "(in ^1-1, after the list) ; ye vā pana …": "; или же " + YEVAPANA(),
    "tasmiṃ samaye": TASMIM,
    "kusalamūlaṃ (closing a root string)": ROOT,
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
    QUESTION(KUSALA) + " " + OPEN_KAMA_KUSALA + ", " + ACC_SOMA_NANA + ", " + ARAMMANA + ", " + TASMIM + " "
    + ", ".join(LIST_ITEM(k, v) for k, v in LIST_1_1)
    + "; или же " + YEVAPANA()
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
    ("1-57", [QA("avikkhepo", S_SAMADHI), "Или же " + YEVAPANA(), END_PADA, END_BHANA1]),
]

ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def pali_segments():
    segs, n = [], 0
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        n += 1
        m = ID.search(line)
        if m:
            segs.append((m.group(1), n))
            n = 0
    return segs


def build():
    psegs = pali_segments()
    assert [b for b, _ in psegs] == [b for b, _ in SEGMENTS], "block IDs differ from the Pāli slice"
    out = []
    for (bid, lines), (_, pn) in zip(SEGMENTS, psegs):
        assert len(lines) == pn, (bid, len(lines), pn)
        lines = list(lines)
        lines[-1] += f" ^{bid}"
        out.append("\n".join(lines))
    return "\n\n".join(out) + "\n"


TEXT = build()
assert "—" not in TEXT and ":-" not in TEXT

if __name__ == "__main__":
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT)
