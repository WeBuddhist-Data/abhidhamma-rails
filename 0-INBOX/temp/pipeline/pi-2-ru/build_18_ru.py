# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: chapter 18 (Dhammahadayavibhaṅga), the last chapter of the book.

usage: python -I -X utf8 build_18_ru.py
Writes AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\18-dhammahadayavibhango.md.
Imports build_ch1_sample_ru (S: paths, DASH, attach_ids, write). Every Pāli line is translated by a handler chosen by
its section; the Pañhāpucchaka-style predication lines (sections 3, 7-10) go through a small subject/predicate
engine. After building, every Pāli sentence that also occurs in pi-2 ch1-17 or pi-1 (sentence-aligned lines) must
get byte-identical Russian (asserted). Reused pi-1 strings are asserted against the pi-1 Russian. Importing writes
nothing.
"""
import glob, os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru"
sys.path.insert(0, HERE)
import build_ch1_sample_ru as S  # noqa: E402

DASH = S.DASH
D = f" {DASH} "
FN = "18-dhammahadayavibhango.md"
AI = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PI1_RU = "\n".join(open(f, encoding="utf-8").read()
                   for f in sorted(glob.glob(os.path.join(AI, "russian", "pi-1-russian-plain-rails_split_chapters", "*.md"))))
PI2_RU = "\n".join(open(os.path.join(S.RU_DIR, f), encoding="utf-8").read()
                   for f in sorted(os.listdir(S.RU_DIR)) if f.endswith(".md") and not f.startswith("18-"))
PI5_RU = "\n".join(open(f, encoding="utf-8").read()
                   for f in sorted(glob.glob(os.path.join(AI, "russian", "pi-5-russian-plain-rails_split_chapters", "*.md"))))


def in_pi1(*parts):
    for p in parts:
        assert p in PI1_RU, "not in pi-1: " + p[:100]


def in_pi2(*parts):
    for p in parts:
        assert p in PI2_RU, "not in pi-2 ch1-17: " + p[:100]


def in_pi5(*parts):
    for p in parts:
        assert p in PI5_RU, "not in pi-5: " + p[:100]


def cap(s):
    return s[:1].upper() + s[1:]


def low(s):
    return s[:1].lower() + s[1:]


# ================================================================ 1. names
NAME = {
    # aggregates [pi-1]
    "rūpakkhandho": "совокупность материальной формы", "vedanākkhandho": "совокупность чувств",
    "saññākkhandho": "совокупность восприятия", "saṅkhārakkhandho": "совокупность формирующих факторов",
    "viññāṇakkhandho": "совокупность сознания",
    # bases [ch2]
    "cakkhāyatanaṃ": "сфера глаза", "rūpāyatanaṃ": "сфера видимых форм", "sotāyatanaṃ": "сфера уха",
    "saddāyatanaṃ": "сфера звуков", "ghānāyatanaṃ": "сфера носа", "gandhāyatanaṃ": "сфера запахов",
    "jivhāyatanaṃ": "сфера языка", "rasāyatanaṃ": "сфера вкусов", "kāyāyatanaṃ": "сфера тела",
    "phoṭṭhabbāyatanaṃ": "сфера осязаемого", "manāyatanaṃ": "сфера ума", "dhammāyatanaṃ": "сфера объектов ума",
    # elements [ch3]
    "cakkhudhātu": "элемент глаза", "rūpadhātu": "элемент видимых форм", "cakkhuviññāṇadhātu": "элемент зрительного сознания",
    "sotadhātu": "элемент уха", "saddadhātu": "элемент звуков", "sotaviññāṇadhātu": "элемент слухового сознания",
    "ghānadhātu": "элемент носа", "gandhadhātu": "элемент запахов", "ghānaviññāṇadhātu": "элемент обонятельного сознания",
    "jivhādhātu": "элемент языка", "rasadhātu": "элемент вкусов", "jivhāviññāṇadhātu": "элемент вкусового сознания",
    "kāyadhātu": "элемент тела", "phoṭṭhabbadhātu": "элемент осязаемого", "kāyaviññāṇadhātu": "элемент осязательного сознания",
    "manodhātu": "элемент ума", "dhammadhātu": "элемент объектов ума", "manoviññāṇadhātu": "элемент умственного сознания",
    # truths [ch4]
    "dukkhasaccaṃ": "истина о страдании", "samudayasaccaṃ": "истина о возникновении страдания",
    "nirodhasaccaṃ": "истина о прекращении страдания", "maggasaccaṃ": "истина о пути",
    # faculties [ch5]
    "cakkhundriyaṃ": "способность глаза", "sotindriyaṃ": "способность уха", "ghānindriyaṃ": "способность носа",
    "jivhindriyaṃ": "способность языка", "kāyindriyaṃ": "способность тела", "manindriyaṃ": "способность ума",
    "itthindriyaṃ": "способность женственности", "purisindriyaṃ": "способность мужественности",
    "jīvitindriyaṃ": "жизненная способность", "sukhindriyaṃ": "способность удовольствия", "dukkhindriyaṃ": "способность боли",
    "somanassindriyaṃ": "способность радости", "domanassindriyaṃ": "способность уныния",
    "upekkhindriyaṃ": "способность невозмутимости", "saddhindriyaṃ": "способность веры", "vīriyindriyaṃ": "способность усердия",
    "satindriyaṃ": "способность осознанности", "samādhindriyaṃ": "способность сосредоточения",
    "paññindriyaṃ": "способность мудрости", "anaññātaññassāmītindriyaṃ": "способность познания непознанного",
    "aññindriyaṃ": "способность окончательного знания", "aññātāvindriyaṃ": "способность обладателя окончательного знания",
    "rūpajīvitindriyaṃ": "материальная жизненная способность",
    # nutriment [pi-1]
    "kabaḷīkārāhāro": "съедаемая пища", "kabaḷīkāro āhāro": "съедаемая пища", "phassāhāro": "питание контактом",
    "manosañcetanāhāro": "питание умственным намерением", "viññāṇāhāro": "питание сознанием",
    # contacts [pi-1 words; new]
    "cakkhusamphasso": "контакт глаза", "sotasamphasso": "контакт уха", "ghānasamphasso": "контакт носа",
    "jivhāsamphasso": "контакт языка", "kāyasamphasso": "контакт тела", "manodhātusamphasso": "контакт элемента ума",
    "manoviññāṇadhātusamphasso": "контакт элемента умственного сознания",
    # the five kinds of consciousness [ch1]
    "cakkhuviññāṇaṃ": "зрительное сознание", "sotaviññāṇaṃ": "слуховое сознание", "ghānaviññāṇaṃ": "обонятельное сознание",
    "jivhāviññāṇaṃ": "вкусовое сознание", "kāyaviññāṇaṃ": "осязательное сознание",
    # roots [pi-1]
    "alobho kusalahetu": "отсутствие жадности как благой корень", "adoso kusalahetu": "отсутствие злобы как благой корень",
    "amoho kusalahetu": "отсутствие заблуждения как благой корень", "lobho akusalahetu": "жадность как неблагой корень",
    "doso akusalahetu": "злоба как неблагой корень", "moho akusalahetu": "заблуждение как неблагой корень",
    "alobho vipākahetu": "отсутствие жадности как корень, являющийся результатом действий",
    "adoso vipākahetu": "отсутствие злобы как корень, являющийся результатом действий",
    "amoho vipākahetu": "отсутствие заблуждения как корень, являющийся результатом действий",
    "alobho": "отсутствие жадности", "adoso": "отсутствие злобы", "amoho": "отсутствие заблуждения",
    "tayo kusalahetū": "три благих корня", "tayo akusalahetū": "три неблагих корня", "dve akusalahetū": "два неблагих корня",
    "tayo abyākatahetū": "три этически неопределённых корня",
}
DOORS = {"cakkhu": "глаза", "sota": "уха", "ghāna": "носа", "jivhā": "языка", "kāya": "тела", "manodhātu": "элемента ума",
         "manoviññāṇadhātu": "элемента умственного сознания"}
BORN = {"vedanā": "чувство", "saññā": "восприятие", "cetanā": "намерение"}
for _d, _g in DOORS.items():
    for _p, _r in BORN.items():
        NAME[f"{_d}samphassajā {_p}"] = f"рождённое контактом {_g} {_r}"   # S.six_born word order

in_pi1("Питание контактом, питание умственным намерением, питание сознанием", "съедаемая пища",
       "отсутствие жадности как благой корень", "жадность как неблагой корень", "заблуждение как неблагой корень",
       "жадности как корень, являющийся результатом действий", "рождённое контактом глаза",
       "элемента умственного сознания")
in_pi2("материальная жизненная способность", "способность познания непознанного, способность окончательного знания и "
       "способность обладателя окончательного знания", "элемент объектов ума и элемент умственного сознания",
       "сфера осязаемого, сфера ума и сфера объектов ума", "истина о возникновении страдания")


def name(p):
    k = p.strip().lower()
    return NAME[k]


ELL = re.compile(r"\s*…(?:pe…)?\s*")


def conv_list(text):
    """'A, B…pe… C' / 'X vā Y vā' -> Russian with the same separators; case of the first item follows the Pāli."""
    out = []
    for part in re.split(r"(, |\s*…(?:pe…)?\s*)", text):
        if part == "":
            continue
        if part == ", ":
            out.append(", ")
        elif ELL.fullmatch(part):
            out.append("… ")
        else:
            m = re.fullmatch(r"(.+?) vā (.+?) vā", part)
            r = f"{name(m.group(1))} или {name(m.group(2))}" if m else name(part)
            out.append(cap(r) if part[:1].isupper() else r)
    return "".join(out).rstrip()


# ================================================================ 2. counts
NOUN = {  # nom sg, gen sg, gen pl, ins sg, ins pl, gender
    "khandha": ("совокупность", "совокупности", "совокупностей", "совокупностью", "совокупностями", "f"),
    "ayatana": ("сфера восприятия", "сферы восприятия", "сфер восприятия", "сферой восприятия", "сферами восприятия", "f"),
    "dhatu": ("элемент", "элемента", "элементов", "элементом", "элементами", "m"),
    "sacca": ("истина", "истины", "истин", "истиной", "истинами", "f"),
    "indriya": ("способность", "способности", "способностей", "способностью", "способностями", "f"),
    "hetu": ("корень", "корня", "корней", "корнем", "корнями", "m"),
    "ahara": ("вид питания", "вида питания", "видов питания", "видом питания", "видами питания", "m"),
    "phassa": ("вид контакта", "вида контакта", "видов контакта", "видом контакта", "видами контакта", "m"),
    "vedana": ("чувство", "чувства", "чувств", "чувством", "чувствами", "n"),
    "sanna": ("восприятие", "восприятия", "восприятий", "восприятием", "восприятиями", "n"),
    "cetana": ("намерение", "намерения", "намерений", "намерением", "намерениями", "n"),
    "citta": ("вид ума", "вида ума", "видов ума", "видом ума", "видами ума", "m"),
}
NUM_NOM = {2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
           11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
           16: "шестнадцать", 18: "восемнадцать", 22: "двадцать два"}
ONE = {"m": ("один", "одним"), "f": ("одна", "одной"), "n": ("одно", "одним")}
NUM_INS = {2: "двумя", 3: "тремя", 4: "четырьмя", 5: "пятью", 6: "шестью", 7: "семью", 8: "восемью", 9: "девятью",
           10: "десятью", 11: "одиннадцатью", 12: "двенадцатью", 13: "тринадцатью", 14: "четырнадцатью",
           18: "восемнадцатью", 22: "двадцатью двумя"}
NUM_GEN = {2: "двух", 3: "трёх", 4: "четырёх", 5: "пяти", 7: "семи", 12: "двенадцати", 18: "восемнадцати", 22: "двадцати двух"}


def num_nom(n, g):
    s = NUM_NOM[n]
    if g == "f" and n in (2, 22):
        s = s[:-1] + "е"   # две / двадцать две
    return s


def cnt(noun, n, case="nom"):
    ns, gs, gp, is_, ip, g = NOUN[noun]
    if case == "nom":
        if n == 1:
            return f"{ONE[g][0]} {ns}"
        return f"{num_nom(n, g)} {gs if n in (2, 3, 4, 22) else gp}"
    if case == "ins":
        if n == 1:
            return f"{ONE[g][1]} {is_}"
        return f"{NUM_INS[n]} {ip}"
    if case == "gen":
        return f"{NUM_GEN[n]} {gp}"
    raise KeyError(case)


ORDER12 = ["khandha", "ayatana", "dhatu", "sacca", "indriya", "hetu", "ahara", "phassa", "vedana", "sanna", "cetana", "citta"]
HOW = {k: "сколько " + NOUN[k][2] for k in ORDER12}     # kati khandhā = сколько совокупностей …
GROUPS_GEN = "из пяти совокупностей"
LAST_GEN = "из семи видов ума"

COUNTP = {  # Pāli count phrase -> (noun, n)
    "pañcakkhandhā": ("khandha", 5), "cattāro khandhā": ("khandha", 4), "eko khandho": ("khandha", 1),
    "dvādasāyatanāni": ("ayatana", 12), "cha āyatanāni": ("ayatana", 6), "dve āyatanāni": ("ayatana", 2),
    "ekādasāyatanāni": ("ayatana", 11), "dasāyatanāni": ("ayatana", 10), "navāyatanāni": ("ayatana", 9),
    "sattāyatanāni": ("ayatana", 7), "pañcāyatanāni": ("ayatana", 5),
    "aṭṭhārasa dhātuyo": ("dhatu", 18), "nava dhātuyo": ("dhatu", 9), "dve dhātuyo": ("dhatu", 2),
    "ekādasa dhātuyo": ("dhatu", 11), "dasa dhātuyo": ("dhatu", 10), "satta dhātuyo": ("dhatu", 7),
    "pañca dhātuyo": ("dhatu", 5),
    "cattāri saccāni": ("sacca", 4), "tīṇi saccāni": ("sacca", 3), "dve saccāni": ("sacca", 2), "ekaṃ saccaṃ": ("sacca", 1),
    "bāvīsatindriyāni": ("indriya", 22), "cuddasindriyāni": ("indriya", 14), "ekādasindriyāni": ("indriya", 11),
    "dvādasindriyāni": ("indriya", 12), "terasindriyāni": ("indriya", 13), "dasindriyāni": ("indriya", 10),
    "navindriyāni": ("indriya", 9), "aṭṭhindriyāni": ("indriya", 8), "sattindriyāni": ("indriya", 7),
    "pañcindriyāni": ("indriya", 5), "cattārindriyāni": ("indriya", 4), "ekindriyaṃ": ("indriya", 1),
    "nava hetū": ("hetu", 9), "aṭṭha hetū": ("hetu", 8), "cha hetū": ("hetu", 6), "tayo hetū": ("hetu", 3),
    "dve hetū": ("hetu", 2),
    "cattāro āhārā": ("ahara", 4), "tayo āhārā": ("ahara", 3),
    "satta phassā": ("phassa", 7), "cattāro phassā": ("phassa", 4), "eko phasso": ("phassa", 1),
    "satta vedanā": ("vedana", 7), "catasso vedanā": ("vedana", 4), "ekā vedanā": ("vedana", 1),
    "satta saññā": ("sanna", 7), "catasso saññā": ("sanna", 4), "ekā saññā": ("sanna", 1),
    "satta cetanā": ("cetana", 7), "catasso cetanā": ("cetana", 4), "ekā cetanā": ("cetana", 1),
    "satta cittāni": ("citta", 7), "cattāri cittāni": ("citta", 4), "ekaṃ cittaṃ": ("citta", 1),
}


def cp(p, case="nom"):
    noun, n = COUNTP[p.strip().lower()]
    return cnt(noun, n, case)


def count_list(text):
    """'pañcakkhandhā, dvādasāyatanāni, …' -> 'пять совокупностей, двенадцать сфер восприятия, …'"""
    return ", ".join(cp(x) for x in text.split(", "))


# ================================================================ 3. realms and beings
REALM = {"kāmadhātuyā": "в мире чувственных желаний", "rūpadhātuyā": "в мире форм", "arūpadhātuyā": "в мире без форм",
         "apariyāpanne": "в том, что не принадлежит к кругам существования"}
in_pi5("В мире чувственных желаний", "В мире форм", "В мире без форм")
in_pi1("Явления, не принадлежащие к кругам существования")
REALM_FIRST = {k: cap(v) + ("," if k == "apariyāpanne" else "") for k, v in REALM.items()}
MOMENT = {k: "в момент перерождения " + v for k, v in REALM.items() if k != "apariyāpanne"}

BEINGS = [  # (Pāli words, Russian, is_attribute)
    ("kāmāvacarānaṃ devānaṃ", "у богов, относящихся к миру чувственных желаний", False),
    ("paṭhamakappikānaṃ manussānaṃ", "у людей первой эпохи", False),
    ("opapātikānaṃ petānaṃ", "у рождающихся самопроизвольно духов умерших", False),
    ("opapātikānaṃ asurānaṃ", "у рождающихся самопроизвольно асуров", False),
    ("opapātikānaṃ tiracchānagatānaṃ", "у рождающихся самопроизвольно животных", False),
    ("nerayikānaṃ", "у обитателей ада", False),
    ("gabbhaseyyakānaṃ sattānaṃ", "у существ, рождающихся из утробы", False),
    ("paripuṇṇāyatanānaṃ", "обладающих полным набором сфер восприятия", True),
    ("jaccandhabadhirānaṃ", "слепых и глухих от рождения", True),
    ("jaccandhānaṃ", "слепых от рождения", True),
    ("jaccabadhirānaṃ", "глухих от рождения", True),
    ("sahetukānaṃ ñāṇasampayuttānaṃ", "имеющих корни и связанных со знанием", True),
    ("sahetukānaṃ ñāṇavippayuttānaṃ", "имеющих корни и не связанных со знанием", True),
    ("ahetukānaṃ", "не имеющих корней", True),
    ("ṭhapetvā napuṃsakānaṃ", "кроме бесполых", True),
    ("napuṃsakānaṃ", "бесполых", True),
]
in_pi1("нет рождающихся самопроизвольно существ")
in_pi5("духом умершего", "обитателем ада", "животным", "асуры")


def beings(text):
    words = text.replace(",", "").lower().split()
    out, i = [], 0
    while i < len(words):
        for p, r, _a in BEINGS:
            pw = p.split()
            if words[i:i + len(pw)] == pw:
                out.append(r)
                i += len(pw)
                break
        else:
            raise KeyError(" ".join(words[i:]))
    return cap(", ".join(out))


# ================================================================ 4. gods [pi-5 ^5-? 10-dutiyavaggo names; pi-1 in ^2-1020]
GODS = {  # Pāli genitive plural stem -> Russian genitive plural «богов …»
    "cātumahārājikānaṃ": "богов Четырёх Великих Царей", "cātummahārājikānaṃ": "богов Четырёх Великих Царей",
    "tāvatiṃsānaṃ": "богов Тридцати трёх", "yāmānaṃ": "богов Ямы", "tusitānaṃ": "богов Тушиты",
    "nimmānaratīnaṃ": "богов, наслаждающихся творением",
    "paranimmitavasavattīnaṃ": "богов, властвующих над творениями других",
    "brahmapārisajjānaṃ": "богов свиты Брахмы", "brahmapurohitānaṃ": "богов-советников Брахмы",
    "mahābrahmānaṃ": "Великих Брахм", "parittābhānaṃ": "богов ограниченного сияния",
    "appamāṇābhānaṃ": "богов безмерного сияния", "ābhassarānaṃ": "богов струящегося сияния",
    "parittasubhānaṃ": "богов ограниченного великолепия", "appamāṇasubhānaṃ": "богов безмерного великолепия",
    "subhakiṇhānaṃ": "богов сплошного великолепия", "asaññasattānaṃ": "богов без восприятия",
    "vehapphalānaṃ": "богов великого плода", "avihānaṃ": "богов, не отпадающих от своего мира",
    "atappānaṃ": "невозмутимых богов", "sudassānaṃ": "богов прекрасного облика", "sudassīnaṃ": "богов ясного видения",
    "akaniṭṭhānaṃ": "высочайших богов",
    "ākāsānañcāyatanūpagānaṃ": "богов, достигших сферы бесконечного пространства",
    "viññāṇañcāyatanūpagānaṃ": "богов, достигших сферы бесконечного сознания",
    "ākiñcaññāyatanūpagānaṃ": "богов, достигших сферы отсутствия чего-либо",
    "nevasaññānāsaññāyatanūpagānaṃ": "богов, достигших сферы ни восприятия, ни невосприятия",
}
in_pi5(*[v for k, v in GODS.items() if k not in ("asaññasattānaṃ", "viññāṇañcāyatanūpagānaṃ", "ākiñcaññāyatanūpagānaṃ",
                                                 "nevasaññānāsaññāyatanūpagānaṃ", "mahābrahmānaṃ")])
in_pi5("Великих Брахм", "существ без восприятия")
in_pi2("достигает сферы бесконечного сознания", "достигает сферы отсутствия чего-либо",
       "достигает сферы ни восприятия, ни невосприятия")
SAHABYA = "перерождаются в обществе"


# ================================================================ 5. predication engine (sections 3, 7-10)
def isv(m, f, n, p):
    return {"m": "является " + m, "f": "является " + f, "n": "является " + n, "pl": "являются " + p}


def short(stem_m, rest=""):  # short participle/adjective forms
    base = {"m": stem_m, "f": stem_m + "а", "n": stem_m + "о", "pl": stem_m + "ы"}
    return {k: v + rest for k, v in base.items()}


def verb(sg, pl):
    return {"m": sg, "f": sg, "n": sg, "pl": pl}


def gend(m, f, n, p):
    return {"m": m, "f": f, "n": n, "pl": p}


ADM = "чувством, которое ни болезненно, ни приятно"
PRED = {  # key: (positive forms, negative forms or None, type)
    "§sukha": (short("связан", " с приятным чувством"), None, "v"),
    "§dukkha": (short("связан", " с болезненным чувством"), None, "v"),
    "§adm": (short("связан", " с " + ADM), None, "v"),
    "kusal": (isv("благим", "благой", "благим", "благими"), None, "k"),
    "akusal": (isv("неблагим", "неблагой", "неблагим", "неблагими"), None, "k"),
    "abyākat": (isv("этически неопределённым", "этически неопределённой", "этически неопределённым",
                    "этически неопределёнными"), None, "k"),
    "nevavipākanavipākadhammadhamm": (gend("не является результатом действий и не способен приносить результаты",
                                           "не является результатом действий и не способна приносить результаты",
                                           "не является результатом действий и не способно приносить результаты",
                                           "не являются результатом действий и не способны приносить результаты"), None, "k"),
    "vipākadhammadhamm": (gend("способен приносить результаты", "способна приносить результаты",
                               "способно приносить результаты", "способны приносить результаты"), None, "k"),
    "vipāk": (verb("является результатом действий", "являются результатом действий"), None, "k"),
    "upādinnupādāniy": (gend("охвачен цеплянием и служит его объектом", "охвачена цеплянием и служит его объектом",
                             "охвачено цеплянием и служит его объектом", "охвачены цеплянием и служат его объектом"),
                        None, "k"),
    "anupādinnupādāniy": (gend("не охвачен цеплянием, но служит его объектом",
                               "не охвачена цеплянием, но служит его объектом",
                               "не охвачено цеплянием, но служит его объектом",
                               "не охвачены цеплянием, но служат его объектом"), None, "k"),
    "anupādinnaanupādāniy": (gend("не охвачен цеплянием и не служит его объектом",
                                  "не охвачена цеплянием и не служит его объектом",
                                  "не охвачено цеплянием и не служит его объектом",
                                  "не охвачены цеплянием и не служат его объектом"), None, "k"),
    "savitakkasavicār": (verb("является явлением с направленной мыслью и удержанием мысли",
                              "являются явлениями с направленной мыслью и удержанием мысли"), None, "k"),
    "avitakkavicāramatt": (verb("является явлением без направленной мысли, только с удержанием мысли",
                                "являются явлениями без направленной мысли, только с удержанием мысли"), None, "k"),
    "avitakkaavicār": (verb("является явлением без направленной мысли и без удержания мысли",
                            "являются явлениями без направленной мысли и без удержания мысли"), None, "k"),
    "sārammaṇārammaṇ": (verb("имеет объектом то, что имеет объект", "имеют объектом то, что имеет объект"), None, "k"),
    "anārammaṇārammaṇ": (verb("имеет объектом то, что не имеет объекта", "имеют объектом то, что не имеет объекта"),
                         None, "k"),
    "sārammaṇ": (verb("имеет объект", "имеют объект"), None, "k"),
    "anārammaṇ": (verb("не имеет объекта", "не имеют объекта"), None, "k"),
    "arūpadhātupariyāpann": (verb("принадлежит к миру без форм", "принадлежат к миру без форм"),
                             verb("не принадлежит к миру без форм", "не принадлежат к миру без форм"), "k"),
    "rūpadhātupariyāpann": (verb("принадлежит к миру форм", "принадлежат к миру форм"),
                            verb("не принадлежит к миру форм", "не принадлежат к миру форм"), "k"),
    "kāmadhātupariyāpann": (verb("принадлежит к миру чувственных желаний", "принадлежат к миру чувственных желаний"),
                            verb("не принадлежит к миру чувственных желаний", "не принадлежат к миру чувственных желаний"),
                            "k"),
    "apariyāpann": (verb("не принадлежит к кругам существования", "не принадлежат к кругам существования"), None, "k"),
    "pariyāpann": (verb("принадлежит к кругам существования", "принадлежат к кругам существования"), None, "k"),
    "arūp": (isv("нематериальным", "нематериальной", "нематериальным", "нематериальными"), None, "k"),
    "rūp": (isv("материальным", "материальной", "материальным", "материальными"), None, "k"),
    "lokiy": (isv("мирским", "мирской", "мирским", "мирскими"), None, "k"),
    "lokuttar": (isv("надмирским", "надмирской", "надмирским", "надмирскими"), None, "k"),
    "abhiññeyy": (verb("следует постичь высшим знанием", "следует постичь высшим знанием"), None, "a"),
    "pariññeyy": (verb("следует полностью понять", "следует полностью понять"), None, "a"),
    "pahātabb": (verb("следует устранить", "следует устранить"), verb("не следует устранять", "не следует устранять"), "a"),
    "bhāvetabb": (verb("следует развивать", "следует развивать"), verb("не следует развивать", "не следует развивать"), "a"),
    "sacchikātabb": (verb("следует осуществить", "следует осуществить"),
                     verb("не следует осуществлять", "не следует осуществлять"), "a"),
    "diṭṭh": (short("увиден"), short("не увиден"), "d"),
    "viññāt": (short("познан"), short("не познан"), "d"),
    "sut": (short("услышан"), short("не услышан"), "d"),
    "mut": (gend("ощущён", "ощущена", "ощущено", "ощущены"), gend("не ощущён", "не ощущена", "не ощущено", "не ощущены"),
            "d"),
}
PKEYS = sorted(PRED, key=len, reverse=True)
QUOTE = {  # na vattabba: quoted predicate (sg, pl)
    "§sukha": ("явление, связанное с приятным чувством", "явления, связанные с приятным чувством"),
    "§dukkha": ("явление, связанное с болезненным чувством", "явления, связанные с болезненным чувством"),
    "§adm": ("явление, связанное с " + ADM, "явления, связанные с " + ADM),
    "savitakkasavicār": ("явление с направленной мыслью и удержанием мысли",
                         "явления с направленной мыслью и удержанием мысли"),
    "avitakkavicāramatt": ("явление без направленной мысли, только с удержанием мысли",
                           "явления без направленной мысли, только с удержанием мысли"),
    "avitakkaavicār": ("явление без направленной мысли и без удержания мысли",
                       "явления без направленной мысли и без удержания мысли"),
}
NV = "нельзя определить"
PRON = {"m": "его", "f": "её", "n": "его", "pl": "их"}
in_pi2("иногда её нельзя определить – ни как «явление, связанное с приятным чувством»",
       "иногда её нельзя определить – ни как «явление с направленной мыслью и удержанием мысли», ни как «явление без "
       "направленной мысли, только с удержанием мысли», ни как «явление без направленной мысли и без удержания мысли»")


def pkey(word):
    for k in PKEYS:
        if word.startswith(k):
            return k
    raise KeyError(word)


def F(nom, g, acc=None):
    return (nom, acc or nom, g)


SUBJ = {
    "Rūpakkhandho": F("Совокупность материальной формы", "f"),
    "Saṅkhārakkhandho": F("Совокупность формирующих факторов", "f"),
    "Cattāro khandhā": F("Четыре совокупности", "pl"), "Tayo khandhā": F("Три совокупности", "pl"),
    "Dve khandhā": F("Две совокупности", "pl"),
    "Dasāyatanā": F("Десять сфер восприятия", "pl"), "Dve āyatanā": F("Две сферы восприятия", "pl"),
    "Dvāyatanā": F("Две сферы восприятия", "pl"), "Cattāro āyatanā": F("Четыре сферы восприятия", "pl"),
    "Pañcāyatanā": F("Пять сфер восприятия", "pl"), "Sattāyatanā": F("Семь сфер восприятия", "pl"),
    "Manāyatanaṃ": F("Сфера ума", "f", "Сферу ума"), "Dhammāyatanaṃ": F("Сфера объектов ума", "f", "Сферу объектов ума"),
    "Rūpāyatanaṃ": F("Сфера видимых форм", "f", "Сферу видимых форм"),
    "Saddāyatanaṃ": F("Сфера звуков", "f", "Сферу звуков"),
    "Gandhāyatanaṃ… rasāyatanaṃ… phoṭṭhabbāyatanaṃ": F("Сфера запахов… сфера вкусов… сфера осязаемого", "f",
                                                       "Сферу запахов… сферу вкусов… сферу осязаемого"),
    "Soḷasa dhātuyo": F("Шестнадцать элементов", "pl"), "Dve dhātuyo": F("Два элемента", "pl"),
    "Dasa dhātuyo": F("Десять элементов", "pl"), "Satta dhātuyo": F("Семь элементов", "pl"),
    "Cha dhātuyo": F("Шесть элементов", "pl"), "Pañca dhātuyo": F("Пять элементов", "pl"),
    "Terasa dhātuyo": F("Тринадцать элементов", "pl"), "Pannarasa dhātuyo": F("Пятнадцать элементов", "pl"),
    "Manodhātu": F("Элемент ума", "m"), "Manoviññāṇadhātu": F("Элемент умственного сознания", "m"),
    "Dhammadhātu": F("Элемент объектов ума", "m"), "Kāyaviññāṇadhātu": F("Элемент осязательного сознания", "m"),
    "Rūpadhātu": F("Элемент видимых форм", "m"), "Saddadhātu": F("Элемент звуков", "m"),
    "Gandhadhātu… rasadhātu… phoṭṭhabbadhātu": F("Элемент запахов… элемент вкусов… элемент осязаемого", "m"),
    "Samudayasaccaṃ": F("Истина о возникновении страдания", "f", "Истину о возникновении страдания"),
    "Maggasaccaṃ": F("Истина о пути", "f", "Истину о пути"),
    "Nirodhasaccaṃ": F("Истина о прекращении страдания", "f", "Истину о прекращении страдания"),
    "Dukkhasaccaṃ": F("Истина о страдании", "f", "Истину о страдании"),
    "Dve saccā": F("Две истины", "pl"), "Tīṇi saccāni": F("Три истины", "pl"),
    "Dasindriyā": F("Десять способностей", "pl"), "Tīṇindriyā": F("Три способности", "pl"),
    "Navindriyā": F("Девять способностей", "pl"), "Terasindriyā": F("Тринадцать способностей", "pl"),
    "Cuddasindriyā": F("Четырнадцать способностей", "pl"), "Aṭṭhindriyā": F("Восемь способностей", "pl"),
    "Sattindriyā": F("Семь способностей", "pl"), "Cha indriyā": F("Шесть способностей", "pl"),
    "Cattārindriyā": F("Четыре способности", "pl"), "Pañcindriyā": F("Пять способностей", "pl"),
    "Dvindriyā": F("Две способности", "pl"), "Dvādasindriyā": F("Двенадцать способностей", "pl"),
    "Ekādasindriyā": F("Одиннадцать способностей", "pl"), "Bāvīsatindriyā": F("Двадцать две способности", "pl"),
    "Domanassindriyaṃ": F("Способность уныния", "f"), "Anaññātaññassāmītindriyaṃ": F("Способность познания непознанного", "f"),
    "Aññindriyaṃ": F("Способность окончательного знания", "f"),
    "Aññātāvindriyaṃ": F("Способность обладателя окончательного знания", "f"),
    "Jīvitindriyaṃ": F("Жизненная способность", "f", "Жизненную способность"),
    "Upekkhindriyaṃ": F("Способность невозмутимости", "f"),
    "Tayo akusalahetū": F("Три неблагих корня", "pl"), "Tayo kusalahetū": F("Три благих корня", "pl"),
    "Tayo abyākatahetū": F("Три этически неопределённых корня", "pl"), "Cha hetū": F("Шесть корней", "pl"),
    "Nava hetū": F("Девять корней", "pl"), "Satta hetū": F("Семь корней", "pl"),
    "Doso akusalahetu": F("Злоба как неблагой корень", "f", "Злобу как неблагой корень"),
    "Moho akusalahetu": F("Заблуждение как неблагой корень", "n"),
    "Kabaḷīkāro āhāro": F("Съедаемая пища", "f", "Съедаемую пищу"),
    "Tayo āhārā": F("Три вида питания", "pl"), "Cattāro āhārā": F("Четыре вида питания", "pl"),
    "Manoviññāṇadhātusamphasso": F("Контакт элемента умственного сознания", "m"),
    "Manodhātusamphasso": F("Контакт элемента ума", "m"),
    "Kāyaviññāṇadhātusamphasso": F("Контакт элемента осязательного сознания", "m"),
    "Manoviññāṇadhātusamphassajā vedanā": F("Рождённое контактом элемента умственного сознания чувство", "n"),
    "Manoviññāṇadhātusamphassajā saññā": F("Рождённое контактом элемента умственного сознания восприятие", "n"),
    "Manoviññāṇadhātusamphassajā cetanā": F("Рождённое контактом элемента умственного сознания намерение", "n"),
}
SUBJ_L = {k.lower(): v for k, v in SUBJ.items()}
SUBJ_RE = re.compile(r"^(" + "|".join(map(re.escape, sorted(SUBJ_L, key=len, reverse=True))) + r")(?= )", re.I)
CNUM = {"pañca": "пять", "cha": "шесть", "satta": "семь"}
CNOUN = {"phassā": "видов контакта", "vedanā": "чувств", "saññā": "восприятий", "cetanā": "намерений", "cittā": "видов ума"}
_ITEM = r"(?:pañca|cha|satta) (?:phassā|vedanā|saññā|cetanā|cittā)"
COMP_RE = re.compile(r"^(" + _ITEM + r"(?:…\s*" + _ITEM + r")*)(?= )", re.I)


def subject(seg):
    """-> (pāli subject, nom, acc, gender) or None"""
    m = SUBJ_RE.match(seg)
    if m:
        nom, acc, g = SUBJ_L[m.group(1).lower()]
        if m.group(1)[:1].islower():
            nom, acc = low(nom), low(acc)
        return m.group(1), nom, acc, g
    m = COMP_RE.match(seg)
    if m:
        parts = m.group(1).split("…")
        ru = "… ".join(f"{CNUM[p.split()[0].lower()]} {CNOUN[p.split()[1]]}" for p in (x.strip() for x in parts))
        ru = cap(ru) if m.group(1)[:1].isupper() else ru
        return m.group(1), ru, ru, "pl"
    return None


def qkey(tok):
    t = re.sub(r"(?:n?ti ?pi|ti)$", "", tok)
    return pkey(t)


def render_clause(subj, segs):
    """subj = (pāli, nom, acc, g); segs = list of (separator_before, text) predicate segments."""
    _p, nom, acc, g = subj
    num = "pl" if g == "pl" else "sg"
    out, use_acc, prev_neg, i = [], False, False, 0
    while i < len(segs):
        sep, text = segs[i]
        words = text.split()
        siya = False
        pieces = []
        j = 0
        while j < len(words):
            w = words[j]
            if w == "siyā":
                siya = True
                j += 1
                continue
            neg = False
            if w == "na":
                neg = True
                j += 1
                w = words[j]
            if neg and w.startswith("vattabb"):          # na vattabba: the rest of the clause is the quoted list
                quotes = [qkey(x) for x in words[j + 1:]]
                k = i + 1
                while k < len(segs) and re.search(r"(?:ti ?pi)$", segs[k][1]):
                    quotes += [qkey(x) for x in segs[k][1].split()]
                    k += 1
                qs = [QUOTE[q][0 if num == "sg" else 1] for q in quotes]
                body = NV + " ни как " + ", ни как ".join(f"«{q}»" for q in qs)
                if not pieces and not siya and not out:
                    use_acc = True
                    pieces.append(body)
                else:
                    pieces.append(f"{PRON[g]} {body}")
                i = k - 1
                j = len(words)
                break
            k_ = pkey(w)
            pos, negf, typ = PRED[k_]
            if typ == "a" and not out and not pieces:
                use_acc = True
            if neg:
                piece = negf[g] if negf else "не " + pos[g]
            else:
                piece = pos[g]
                if typ == "d" and prev_neg:
                    piece = "но " + piece
            prev_neg = neg
            pieces.append(piece)
            j += 1
        chunk = ", ".join(pieces)
        if siya:
            chunk = "иногда " + chunk
        out.append((sep, chunk))
        i += 1
    head = acc if use_acc else nom
    text = head + " " + out[0][1] + "".join(s + c for s, c in out[1:])
    return text


SEP = re.compile(r"(\. |; |, )")


def predication(line):
    body = line.rstrip()
    assert body.endswith("."), body[-30:]
    body = body[:-1]
    parts = SEP.split(body)
    segs = [("", parts[0])] + [(parts[k], parts[k + 1]) for k in range(1, len(parts), 2)]
    clauses = []   # (sep_before, subj, [(sep, text)])
    for sep, text in segs:
        s = subject(text)
        if s:
            rest = text[len(s[0]):].strip()
            clauses.append((sep, s, [("", rest)]))
        else:
            assert clauses, text
            clauses[-1][2].append((sep, text))
    out = ""
    for sep, s, segl in clauses:
        out += sep + render_clause(s, segl)
    return out + "."


VED_FIX = [("adukkhamasukhāya vedanāya sampayutt", "§adm"), ("dukkhamasukhāya vedanāya sampayutt", "§adm"),
           ("dukkhāya vedanāya sampayutt", "§dukkha"), ("sukhāya vedanāya sampayutt", "§sukha")]
FIXES = [  # punctuation / spacing / spelling slips in the Pāli (reported); words translated as written
    ("siyā kāmadhātu pariyāpanno", "siyā kāmadhātupariyāpanno"),
    ("cha saññā … cha cetanā", "cha saññā… cha cetanā"),
    ("siyā sārammaṇārammaṇo siyā anārammaṇārammaṇo", "siyā sārammaṇārammaṇo, siyā anārammaṇārammaṇo"),
    ("siyā vipākā siyā vipākadhammadhammā", "siyā vipākā, siyā vipākadhammadhammā"),
    ("siyā avitakkaavicāro siyā na vattabbo", "siyā avitakkaavicāro, siyā na vattabbo"),
    ("pañca cittā avitakkaavicārā manodhātu", "pañca cittā avitakkaavicārā, manodhātu"),
    ("satta cetanā satta cittā", "satta cetanā… satta cittā"),
    ("sampayuttoti pi", "sampayuttotipi"),
    ("anupādinnupādāniyo 4.", "anupādinnupādāniyo #4."),
]


def pred_line(p):
    t = re.sub(r"…pe…", "…", p)
    for a, b in FIXES:
        t = t.replace(a, b)
    for a, b in VED_FIX:
        t = t.replace(a, b)
    if "#4." in t:   # a stray digit in the Pāli after the first sentence; kept at the same spot
        a, b = t.split(" #4. ", 1)
        return predication(a + ".")[:-1] + " 4. " + predication(b)
    return predication(t)


def howmany(preds, last=LAST_GEN):
    p = preds[0] + "".join(", сколько " + x for x in preds[1:])
    return f"Сколько {GROUPS_GEN} {p}… сколько {last} {p}?"


Q_KUS = ["являются благими", "неблагими", "этически неопределёнными"]
in_pi2("Сколько из пяти совокупностей являются благими, сколько неблагими, сколько этически неопределёнными…")


# ================================================================ 6. headings
HEAD = {
    "### Dhammahadayavibhaṅgo": "### " + S.CHAPTER_TITLES[18],
    "#### Sabbasaṅgāhikavāro": "#### Раздел, охватывающий всё",
    "#### Uppattānuppattivāro": "#### Раздел о том, что возникает и что не возникает",
    "##### Kāmadhātu": "##### Мир чувственных желаний",
    "##### Rūpadhātu": "##### Мир форм",
    "##### Arūpadhātu": "##### Мир без форм",
    "##### Apariyāpannaṃ": "##### Не принадлежащее к кругам существования",
    "#### Pariyāpannāpariyāpannavāro": "#### Раздел о принадлежащем и не принадлежащем",
    "##### Pariyāpannāpariyāpannaṃ": "##### Принадлежащее и не принадлежащее к кругам существования",
    "#### Dhammadassanavāro": "#### Раздел о проявлении явлений",
    "##### Asaññasattā": "##### Существа без восприятия",
    "#### Bhūmantaradassanavāro": "#### Раздел о различии уровней",
    "#### Uppādakakammaāyuppamāṇavāro": "#### Раздел о порождающих действиях и продолжительности жизни",
    "##### Uppādakakammaṃ": "##### Порождающие действия",
    "##### Āyuppamāṇaṃ": "##### Продолжительность жизни",
    "#### Abhiññeyyādivāro": "#### Раздел о том, что следует постичь высшим знанием, и прочем",
    "#### Sārammaṇānārammaṇavāro": "#### Раздел об имеющем объект и не имеющем объекта",
    "#### Diṭṭhasutādidassanavāro": "#### Раздел об увиденном, услышанном и прочем",
    "#### Tikādidassanavāro": "#### Раздел о тройках и прочем",
    "##### Kusalattikaṃ": "##### Тройка о благом",
    "##### Vedanātikaṃ": "##### Тройка о чувстве",
    "##### Vipākattikaṃ": "##### Тройка о результате действий",
    "##### Upādinnattikaṃ": "##### Тройка об охваченном цеплянием",
    "##### Vitakkattikaṃ": "##### Тройка о направленной мысли",
    "##### (1) Rūpadukaṃ": "##### (1) Пара о материальном",
    "##### (2) Lokiyadukaṃ": "##### (2) Пара о мирском",
}


# ================================================================ 7. section handlers
def q_tattha_list(p):
    """Tattha katam… [REALM] COUNT? LIST – im… vucca… "[realm] COUNT"."""
    m = re.match(r'^Tattha katam\w+ (?:(kāmadhātuyā|rūpadhātuyā|arūpadhātuyā|apariyāpanne) )?(.+?)\? (.+?)(…pe…)? ?'
                 r'(?:' + DASH + r' )?(?:ime|imāni|imā|ayaṃ|idaṃ) (?:vuccanti|vuccati|vuccatti) "(?:\w+ )?(.+)"\.$', p)
    assert m, p
    realm, count, lst, pe = m.group(1), m.group(2), m.group(3), m.group(4)
    r = (" " + REALM[realm]) if realm else ""
    ru_list = conv_list(lst)
    sep = "… " if pe else D
    return f"Что такое здесь {cp(count)}{r}? {ru_list}{sep}это называется «{cp(count, 'ins')}{r}»."


HETU_KUS = "Отсутствие жадности как благой корень, отсутствие злобы как благой корень, отсутствие заблуждения как благой корень"
HETU_AKUS = "Жадность как неблагой корень, злоба как неблагой корень, заблуждение как неблагой корень"
HETU_ABY = ("Отсутствие жадности, отсутствие злобы, отсутствие заблуждения в виде результатов благих явлений или в "
            "этически неопределённых функциональных явлениях")
in_pi1(HETU_ABY + D + "это три этически неопределённых корня.", "Три благих корня, три неблагих корня, три этически "
       "неопределённых корня")
HETU_ABY_APAR = "Отсутствие жадности, отсутствие злобы, отсутствие заблуждения в виде результатов благих явлений"
NINE_HETU = "Три благих корня, три неблагих корня, три этически неопределённых корня"
TWELVE_Q = ", ".join(HOW[k] for k in ORDER12)


def realm_q(realm, keys, pe_after=None):
    """Kāmadhātuyā kati khandhā, … kati cittāni? -> «В мире … сколько совокупностей, …?»"""
    items = [HOW[k] for k in keys]
    if pe_after is not None:
        s = ", ".join(items[:pe_after]) + "… " + HOW["citta"]
    else:
        s = ", ".join(items)
    return f"{REALM_FIRST[realm]} {s}?"


# The section-based dispatcher below handles the lines in file order.
def translate(lines):
    out = []
    sec = None
    sub = None
    tattha_q = []
    for p in lines:
        if p.startswith("#"):
            out.append(HEAD[p])
            if p.startswith("#### "):
                sec = p
            sub = p
            continue
        out.append(line_ru(p, sec, sub))
    return out


# ---------------------------------------------------------------- per-line translation
TATTHA_RE = re.compile(r"^Tattha katam")


def line_ru(p, sec, sub):
    if sec == "#### Sabbasaṅgāhikavāro" or sec == "#### Uppattānuppattivāro":
        return sec12(p, sub)
    if sec == "#### Pariyāpannāpariyāpannavāro":
        return sec3(p, sub)
    if sec == "#### Dhammadassanavāro":
        return sec4(p, sub)
    if sec == "#### Bhūmantaradassanavāro":
        return sec5(p)
    if sec == "#### Uppādakakammaāyuppamāṇavāro":
        return sec6(p)
    if sec in ("#### Abhiññeyyādivāro", "#### Sārammaṇānārammaṇavāro", "#### Diṭṭhasutādidassanavāro",
               "#### Tikādidassanavāro"):
        return sec7_10(p, sec, sub)
    raise KeyError((sec, p[:60]))


REALM_OF_SUB = {"##### Kāmadhātu": "kāmadhātuyā", "##### Rūpadhātu": "rūpadhātuyā", "##### Arūpadhātu": "arūpadhātuyā",
                "##### Apariyāpannaṃ": "apariyāpanne"}


def sec12(p, sub):
    p = S.ID.sub("", p).rstrip()
    p = p.replace("imā vuccatti", "imā vuccanti").replace("Cakkhusamphasso sotasamphasso", "Cakkhusamphasso, sotasamphasso")
    if p.startswith("Kati khandhā"):
        return cap(TWELVE_Q) + "?"
    if p.startswith("Pañcakkhandhā, dvādasāyatanāni"):
        return cap(count_list(p[:-1])) + "."
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā|Apariyāpanne) kati khandhā(.*)\?$", p)
    if m:
        realm = m.group(1).lower()
        rest = m.group(2)
        if rest.startswith(", kati āyatanāni, kati dhātuyo, kati saccāni, kati indriyāni, kati hetū"):
            return f"{REALM_FIRST[realm]} {', '.join(HOW[k] for k in ORDER12)}?"
        if rest == ", kati āyatanā, kati dhātuyo, kati saccāni, kati indriyāni…pe… kati cittāni":
            return f"{REALM_FIRST[realm]} {', '.join(HOW[k] for k in ORDER12[:5])}… {HOW['citta']}?"
        assert rest == "…pe… kati cittāni", rest
        return f"{REALM_FIRST[realm]} {HOW['khandha']}… {HOW['citta']}?"
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā|Apariyāpanne) (.+)\.$", p)
    if m:
        return f"{REALM_FIRST[m.group(1).lower()]} {count_list(m.group(2))}."
    if p.startswith("Tattha katame nava hetū?"):
        return f"Что такое здесь {cnt('hetu', 9)}? {NINE_HETU}."
    if p.startswith("Tattha katame tayo kusalahetū?"):
        return f"Что такое здесь три благих корня? {HETU_KUS}{D}это три благих корня."
    if p.startswith("Tattha katame tayo akusalahetū?"):
        return f"Что такое здесь три неблагих корня? {HETU_AKUS}{D}это три неблагих корня."
    if p.startswith("Tattha katame dve akusalahetū?"):
        return (f"Что такое здесь два неблагих корня? Жадность как неблагой корень, заблуждение как неблагой корень{D}это "
                "два неблагих корня.")
    if p.startswith("Tattha katame tayo abyākatahetū?"):
        realm = REALM_OF_SUB.get(sub)
        if p.endswith('Ime vuccanti "nava hetū".'):
            tail = f" Это называется «{cnt('hetu', 9, 'ins')}»."
        elif p.endswith("Ime vuccanti rūpadhātuyā aṭṭha hetū."):
            tail = f" Это называется восемью корнями {REALM['rūpadhātuyā']}."
        elif p.endswith('Ime vuccanti "apariyāpanne cha hetū".'):
            tail = f" Это называется «шестью корнями {REALM['apariyāpanne']}»."
        else:
            raise KeyError(p)
        body = HETU_ABY_APAR if realm == "apariyāpanne" else HETU_ABY
        return f"Что такое здесь три этически неопределённых корня? {body}{D}это три этически неопределённых корня.{tail}"
    m = re.match(r"^Tattha katame (\w+ )?(nava|aṭṭha|cha) hetū\? (.+)$", p)
    if m:
        realm = (m.group(1) or "").strip()
        r = (" " + REALM[realm]) if realm else ""
        n = {"nava": 9, "aṭṭha": 8, "cha": 6}[m.group(2)]
        rest = m.group(3)
        if rest == "Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū.":
            return f"Что такое здесь {cnt('hetu', n)}{r}? {NINE_HETU}."
        if rest == "Tayo kusalahetū, dve akusalahetū, tayo abyākatahetū.":
            return f"Что такое здесь {cnt('hetu', n)}{r}? Три благих корня, два неблагих корня, три этически неопределённых корня."
        if rest == "Tayo kusalahetū, tayo abyākatahetū.":
            return f"Что такое здесь {cnt('hetu', n)}{r}? Три благих корня, три этически неопределённых корня."
        m2 = re.match(r'^(.+)…pe… ime vuccanti "\w+ (.+)"\.$', rest)
        assert m2, rest
        return f"Что такое здесь {cnt('hetu', n)}{r}? {conv_list(m2.group(1))}… это называется «{cnt('hetu', n, 'ins')}{r}»."
    m = re.match(r"^Tattha katamā (\w+) (catasso|ekā) vedanā…pe… (?:catasso|ekā) saññā…pe… (?:catasso|ekā) cetanā…pe… "
                 r"(cattāri cittāni|ekaṃ cittaṃ)\? (.+?) " + DASH + r" (?:imāni|idaṃ) (?:vuccanti|vuccati) \"\w+ (.+)\"\.$", p)
    if m:
        realm, n = m.group(1), (4 if m.group(2) == "catasso" else 1)
        r = " " + REALM[realm]
        return (f"Что такое здесь {cnt('vedana', n)}{r}… {cnt('sanna', n)}… {cnt('cetana', n)}… {cnt('citta', n)}? "
                f"{conv_list(m.group(4))}{D}это называется «{cnt('citta', n, 'ins')}{r}».")
    if p.startswith("Tattha katame cattāro āhārā?"):
        return ("Что такое здесь четыре вида питания? Съедаемая пища [вариант написания (Sī., Syā.): kabaḷiṃkāro āhāro], "
                "питание контактом, питание умственным намерением, питание сознанием" + D +
                "это называется «четырьмя видами питания».")
    if TATTHA_RE.match(p):
        return q_tattha_list(p)
    raise KeyError(p)


def sec3(p, sub):
    p = S.ID.sub("", p).rstrip()
    if p.startswith("Pañcannaṃ khandhānaṃ kati"):
        if "kati apariyāpannā" in p:
            preds = [PRED["pariyāpann"][0]["pl"], PRED["apariyāpann"][0]["pl"]]
        else:
            key = {"##### Kāmadhātu": "kāmadhātupariyāpann", "##### Rūpadhātu": "rūpadhātupariyāpann",
                   "##### Arūpadhātu": "arūpadhātupariyāpann"}[sub]
            preds = [PRED[key][0]["pl"], PRED[key][1]["pl"]]
        return howmany(preds)
    return pred_line(p)


# ---------------------------------------------------------------- section 4: Dhammadassanavāro
APPEAR = {"pātubhavanti": "появляются", "pātubhavati": "появляется"}


def sec4(p, sub):
    p = S.ID.sub("", p).rstrip()
    p = p.replace("kāyindriyaṃ manindriyaṃ", "kāyindriyaṃ, manindriyaṃ").replace("ekā vedanā … ekā saññā",
                                                                                    "ekā vedanā… ekā saññā")
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā) upapattikkhaṇe kati khandhā pātubhavanti…pe… kati cittāni "
                 r"pātubhavanti\?$", p)
    if m:
        mo = cap(MOMENT[m.group(1).lower()])
        return f"{mo} {HOW['khandha']} появляется… {HOW['citta']} появляется?"
    if p.startswith("Asaññasattānaṃ devānaṃ upapattikkhaṇe kati khandhā"):
        return f"В момент перерождения богов без восприятия {HOW['khandha']} появляется… {HOW['citta']} появляется?"
    if p.startswith("Asaññasattānaṃ devānaṃ upapattikkhaṇe eko khandho"):
        return ("В момент перерождения богов без восприятия появляется одна совокупность" + D + "совокупность материальной "
                "формы; появляются две сферы восприятия" + D + "сфера видимых форм, сфера объектов ума; появляются два "
                "элемента" + D + "элемент видимых форм, элемент объектов ума; появляется одна истина" + D + "истина о "
                "страдании; появляется одна способность" + D + "материальная жизненная способность. Боги без восприятия "
                "появляются без корней, без питания, без контакта, без чувства, без восприятия, без намерения, без ума.")
    if p.startswith("Kāmadhātuyā upapattikkhaṇe sabbesaṃ pañcakkhandhā pātubhavanti; kassaci"):
        return dd_kama_summary(p)
    if p.startswith("Rūpadhātuyā upapattikkhaṇe, ṭhapetvā"):
        return dd_summary(p, "Rūpadhātuyā upapattikkhaṇe, ṭhapetvā asaññasattānaṃ devānaṃ, ",
                          cap(MOMENT["rūpadhātuyā"]) + ", кроме богов без восприятия, ")
    if p.startswith("Arūpadhātuyā upapattikkhaṇe cattāro khandhā"):
        return dd_summary(p, "Arūpadhātuyā upapattikkhaṇe ", cap(MOMENT["arūpadhātuyā"]) + " ")
    # "… kassa N X pātubhavanti? <beings> upapattikkhaṇe N X pātubhavanti – <list>. … etesaṃ im… N X pātubhavanti."
    m = re.match(r"^Kāmadhātuyā upapattikkhaṇe kassa (aparāni |aparā )?(.+?) pātubhavanti\? (.+?) upapattikkhaṇe (.+?) "
                 r"pātubhavanti " + DASH + r" (.+?)\. Kāmadhātuyā upapattikkhaṇe etesaṃ (?:imāni|imā|ime) (.+?) "
                 r"pātubhavanti\.(.*)$", p)
    if m:
        other, cnt_p, who, cnt2, lst, cnt3, extra = m.groups()
        mo = cap(MOMENT["kāmadhātuyā"])
        oth = ("другие " if other else "")
        ru = (f"{mo} у кого появляются {oth}{cp(cnt_p)}? {beings(who)}, в момент перерождения появляются {cp(cnt2)}{D}"
              f"{conv_list(lst)}. {mo} у них появляются эти {cp(cnt3)}.")
        if extra:
            assert extra == " Avasesānaṃ sattānaṃ [avasesā sattā (?)] ahetukā pātubhavanti.", extra
            ru += " У остальных существ [вариант чтения (?): avasesā sattā] появление происходит без корней."
        return ru
    # "R upapattikkhaṇe (sabbesaṃ )?katam… N X pātubhava…[?.] LIST – r upapattikkhaṇe (sabbesaṃ )?im… N X pātubhava…."
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā) upapattikkhaṇe (sabbesaṃ )?katam\w+ (.+?) (pātubhavanti|pātubhavati)"
                 r"[?.] (.+?) " + DASH + r" \w+ upapattikkhaṇe (?:sabbesaṃ )?(?:ime|imāni|imā|ayaṃ|idaṃ) (.+?) "
                 r"(pātubhavanti|pātubhavati)\.$", p)
    if m:
        realm, allp, what, verb_, lst, what2, verb2 = m.groups()
        mo = cap(MOMENT[realm.lower()])
        sab = " у всех" if allp else ""
        v = APPEAR[verb_]
        what_ru = dd_what(what)
        which = {"pl": "какие", "m": "какой", "f": "какая", "n": "какое"}
        g = dd_gender(what)
        lst_ru = conv_list(lst)
        q = f"{mo} {which[g]} {what_ru} {v}{sab}?"
        a = f"{lst_ru}{D}{MOMENT[realm.lower()]}{sab} {APPEAR[verb2]} {dd_this(what2)}."
        return q + " " + a
    raise KeyError(p)


def dd_gender(what):
    noun, n = COUNTP[what.split("…")[0].strip().lower()]
    if n == 1:
        return NOUN[noun][5]
    return "pl"


def dd_what(what):
    """'ekā vedanā… ekā saññā… ekā cetanā… ekaṃ cittaṃ' / 'pañcakkhandhā' -> Russian (nominative)"""
    parts = [x.strip() for x in re.split(r"\s*…(?:pe…)?\s*", what) if x.strip()]
    return "… ".join(cp(x) for x in parts)


def dd_this(what):
    parts = [x.strip() for x in re.split(r"\s*…(?:pe…)?\s*", what) if x.strip()]
    out = []
    for x in parts:
        noun, n = COUNTP[x.lower()]
        g = NOUN[noun][5] if n == 1 else "pl"
        this = {"pl": "эти", "m": "этот", "f": "эта", "n": "это"}[g]
        out.append(f"{this} {cnt(noun, n)}")
    return "… ".join(out)


def dd_summary(p, pali_head, ru_head):
    assert p.startswith(pali_head), p[:60]
    body = p[len(pali_head):]
    assert body.endswith(".")
    items = body[:-1].split(", ")
    out = []
    for it in items:
        m = re.match(r"^(.+) (pātubhavanti|pātubhavati)$", it)
        assert m, it
        out.append(f"{APPEAR[m.group(2)]} {dd_what(m.group(1))}")
    return ru_head + ", ".join(out) + "."


def dd_kama_summary(p):
    head = "Kāmadhātuyā upapattikkhaṇe "
    assert p.startswith(head)
    body = p[len(head):-1]
    out = []
    for it in body.split("; "):
        m = re.match(r"^(sabbesaṃ|kassaci) (?:\[keci \(syā\.\)\] )?(aparāni |aparā )?(.+) (pātubhavanti|pātubhavati)$", it)
        assert m, it
        who = "у всех" if m.group(1) == "sabbesaṃ" else "у некоторых"
        if "[keci (syā.)]" in it:
            who += " [вариант чтения (Syā.): keci]"
        if m.group(3) == "ahetukā":
            out.append(f"{who} появление происходит без корней")
            continue
        oth = "другие " if m.group(2) else ""
        out.append(f"{who} {APPEAR[m.group(4)]} {oth}{dd_what(m.group(3))}")
    return cap(MOMENT["kāmadhātuyā"]) + " " + "; ".join(out) + "."


# ---------------------------------------------------------------- section 5: Bhūmantaradassanavāro [pi-1 ^1-1287 … ^1-1294]
KAMA_WORLD = ("Если взять снизу за границу ад Авичи, а сверху включить в эти пределы богов, властвующих над творениями "
              "других, то всё, что в этих пределах относится к этому миру и принадлежит к нему: совокупности, элементы и "
              "сферы восприятия; материальная форма, чувство, восприятие, формирующие факторы, сознание" + D +
              "это явления, относящиеся к миру чувственных желаний.")
RUPA_WORLD = ("Если взять снизу за границу мир Брахмы, а сверху включить в эти пределы богов Аканиттха, то всё, что в "
              "этих пределах относится к этому миру и принадлежит к нему: ум и сопутствующие уму явления того, кто вошёл в "
              "медитативное достижение, или того, кто переродился, или того, кто пребывает в счастье в этой жизни," + D +
              "это явления, относящиеся к миру форм.")
ARUPA_WORLD = ("Если взять снизу за границу богов, рождённых в сфере бесконечного пространства, а сверху включить в эти "
               "пределы богов, рождённых в сфере ни восприятия, ни невосприятия, то всё, что в этих пределах относится к "
               "этому миру и принадлежит к нему: ум и сопутствующие уму явления того, кто вошёл в медитативное достижение, "
               "или того, кто переродился, или того, кто пребывает в счастье в этой жизни," + D +
               "это явления, относящиеся к миру без форм.")
PARIY = ("Подверженные влечениям благие, неблагие и этически неопределённые явления, относящиеся к миру чувственных "
         "желаний, к миру форм или к миру без форм: совокупность материальной формы, совокупность чувств, совокупность "
         "восприятия, совокупность формирующих факторов, совокупность сознания" + D +
         "это явления, принадлежащие к кругам существования.")
in_pi1(KAMA_WORLD.split(" [")[0].replace("других, то", "других [вариант написания (Sī., Ka.): paranimmitavasavattideve], то"),
       RUPA_WORLD.replace("богов Аканиттха,", "богов Аканиттха [вариант написания (Sī., Ka.): akaniṭṭhadeve],")
       .replace("в этой жизни,", "в этой жизни [вариант написания (Ka.): diṭṭhadhammasukhavihārassa],"),
       ARUPA_WORLD, PARIY.replace("совокупность материальной формы, совокупность чувств, совокупность восприятия, "
                                  "совокупность формирующих факторов, совокупность сознания",
                                  "совокупность материальной формы… совокупность сознания"))
MATRIX8 = ("Явления, относящиеся к миру чувственных желаний; явления, не относящиеся к миру чувственных желаний; явления, "
           "относящиеся к миру форм; явления, не относящиеся к миру форм; явления, относящиеся к миру без форм; явления, не "
           "относящиеся к миру без форм; явления, принадлежащие к кругам существования; явления, не принадлежащие к кругам "
           "существования.")


def sec5(p):
    p = S.ID.sub("", p).rstrip()
    table = [
        ("Kāmāvacarā dhammā, na kāmāvacarā dhammā", MATRIX8),
        ("Katame dhammā kāmāvacarā?", "Что такое явления, относящиеся к миру чувственных желаний? " + KAMA_WORLD),
        ("Katame dhammā na kāmāvacarā?", "Что такое явления, не относящиеся к миру чувственных желаний? Явления, "
         "относящиеся к миру форм и к миру без форм, и явления, не принадлежащие к кругам существования," + D +
         "это явления, не относящиеся к миру чувственных желаний."),
        ("Katame dhammā rūpāvacarā?", "Что такое явления, относящиеся к миру форм? " + RUPA_WORLD),
        ("Katame dhammā na rūpāvacarā?", "Что такое явления, не относящиеся к миру форм? Явления, относящиеся к миру "
         "чувственных желаний и к миру без форм, и явления, не принадлежащие к кругам существования," + D +
         "это явления, не относящиеся к миру форм."),
        ("Katame dhammā arūpāvacarā?", "Что такое явления, относящиеся к миру без форм? " + ARUPA_WORLD),
        ("Katame dhammā na arūpāvacarā?", "Что такое явления, не относящиеся к миру без форм? Явления, относящиеся к миру "
         "чувственных желаний и к миру форм, и явления, не принадлежащие к кругам существования," + D +
         "это явления, не относящиеся к миру без форм."),
        ("Katame dhammā pariyāpannā?", "Что такое явления, принадлежащие к кругам существования? " + PARIY),
        ("Katame dhammā apariyāpannā?", "Что такое явления, не принадлежащие к кругам существования? Пути, плоды путей и "
         "необусловленный элемент" + D + "это явления, не принадлежащие к кругам существования."),
    ]
    for pref, ru in table:
        if p.startswith(pref):
            in_pi1(*[x for x in re.split(r"(?<=[?.]) ", ru) if x not in (KAMA_WORLD, RUPA_WORLD, PARIY, MATRIX8)])
            return ru
    raise KeyError(p)


# ---------------------------------------------------------------- section 6: Uppādakakamma, Āyuppamāṇa
NUMW = {"tatiyo bhāgo": "треть", "upaḍḍhakappo": "половина"}
DIVINE = [  # (Pāli god stem, human years per divine day, divine years (words), human count (words))
    ("cātumahārājikānaṃ", "Пятьдесят человеческих лет", "Пятьсот таких божественных лет составляют",
     "Девять миллионов лет."),
    ("tāvatiṃsānaṃ", "Сто человеческих лет", "Тысяча таких божественных лет составляет", "Тридцать шесть миллионов лет."),
    ("yāmānaṃ", "Двести человеческих лет", "Две тысячи таких божественных лет составляют",
     "Сто сорок четыре миллиона лет."),
    ("tusitānaṃ", "Четыреста человеческих лет", "Четыре тысячи таких божественных лет составляют",
     "Пятьсот семьдесят шесть миллионов лет."),
    ("nimmānaratīnaṃ", "Восемьсот человеческих лет", "Восемь тысяч таких божественных лет составляют",
     "Два миллиарда триста четыре миллиона лет."),
    ("paranimmitavasavattīnaṃ", "Тысяча шестьсот человеческих лет", "Шестнадцать тысяч таких божественных лет составляют",
     "Девять миллиардов двести шестнадцать миллионов лет."),
]
# check: 50*30*12*500 = 9e6; 100*360*1000 = 3.6e7; 200*360*2000 = 1.44e8; 400*360*4000 = 5.76e8;
# 800*360*8000 = 2.304e9; 1600*360*16000 = 9.216e9; sum = 1.2285e10 (the verse: 1200 koṭi + 28 koṭi + 50 lakh)
assert 50 * 360 * 500 == 9_000_000 and 100 * 360 * 1000 == 36_000_000 and 200 * 360 * 2000 == 144_000_000
assert 400 * 360 * 4000 == 576_000_000 and 800 * 360 * 8000 == 2_304_000_000 and 1600 * 360 * 16000 == 9_216_000_000
assert 9_000_000 + 36_000_000 + 144_000_000 + 576_000_000 + 2_304_000_000 + 9_216_000_000 == 1200 * 10 ** 7 + 28 * 10 ** 7 + 50 * 10 ** 5
in_pi5("Продолжительность жизни богов Четырёх Великих Царей составляет пятьсот лет", "длится треть эпохи")

JH = {"Paṭhamaṃ": "первое", "Dutiyaṃ": "второе", "Tatiyaṃ": "третье", "Catutthaṃ": "четвёртое"}
DEG = {"parittaṃ": "в ограниченной мере", "majjhimaṃ": "в средней мере", "paṇītaṃ": "в высшей мере"}
SPAN = {"Kappassa tatiyo bhāgo.": "Треть эпохи.", "Upaḍḍhakappo.": "Половина эпохи.",
        "Kappo [eko kappo (syā.)].": "Эпоха [вариант чтения (Syā.): eko kappo].", "Dve kappā.": "Две эпохи.",
        "Cattāro kappā.": "Четыре эпохи.", "Aṭṭha kappā.": "Восемь эпох.", "Soḷasa kappā.": "Шестнадцать эпох.",
        "Bāttiṃsa kappā.": "Тридцать две эпохи.", "Catusaṭṭhi kappā.": "Шестьдесят четыре эпохи.",
        "Pañcakappasatāni.": "Пятьсот эпох.", "Kappasahassaṃ.": "Тысяча эпох.", "Dve kappasahassāni.": "Две тысячи эпох.",
        "Cattāri kappasahassāni.": "Четыре тысячи эпох.", "Aṭṭha kappasahassāni.": "Восемь тысяч эпох.",
        "Soḷasa kappasahassāni.": "Шестнадцать тысяч эпох.", "Vīsati kappasahassāni.": "Двадцать тысяч эпох.",
        "Cattārīsa kappasahassāni.": "Сорок тысяч эпох.", "Saṭṭhi kappasahassāni.": "Шестьдесят тысяч эпох.",
        "Caturāsīti kappasahassānīti.": "Восемьдесят четыре тысячи эпох."}
VERSE_LIFE = [
    "Эти шесть видов богов [вариант чтения (Syā.): chapi te], относящихся к миру чувственных желаний, изобилуют всеми "
    "чувственными благами;",
    "Если сложить вместе срок жизни их всех, каков он?",
    "У них двенадцать миллиардов и ещё двести восемьдесят миллионов;",
    "И пять миллионов лет: так возвещено по счёту лет.",
]
VERSE_END = [
    "Вознесённые силой заслуг, ушедшие в уделы мира чувственных желаний и мира форм,",
    "Даже достигшие вершины существования [вариант чтения (Syā.): bhavaggaṃ vāpi] вновь приходят [вариант чтения (Syā.): "
    "puna gacchanti] в дурной удел.",
    "Даже столь долгоживущие существа умирают, когда исчерпан срок жизни;",
    "Нет никакого постоянного существования, так сказал великий мудрец.",
    "Поэтому мудрые, благоразумные, проницательные, размышляющие о благе,",
    "Ради освобождения от старения и смерти развивают высший путь.",
    "Развив чистый путь, ведущий к погружению в нирвану,",
    "Полностью поняв все влечения, свободные от влечений, достигают окончательного угасания.",
]
VERSE_LIFE_P = ["Cha ete [chapi te (syā.)] kāmāvacarā", "Sabbesaṃ ekasaṅkhāto", "Dvādasa koṭisataṃ tesaṃ",
                "Paññāsa satasahassāni"]
VERSE_END_P = ["Ukkhittā puññatejena", "Bhavaggatampi [bhavaggaṃ vāpi (syā.)]", "Tāva dīghāyukā sattā",
               "Natthi koci bhavo nicco", "Tasmā hi dhīrā nipakā", "Jarāmaraṇamokkhāya", "Bhāvayitvā suciṃ maggaṃ",
               "Sabbāsave pariññāya"]


def who_did(jh, deg):
    d = (" " + DEG[deg]) if deg else ""
    return f"кто развил {JH[jh]} медитативное погружение{d}"


def sec6(p):
    p = S.ID.sub("", p).rstrip()
    fixed = {
        "Devāti.": "«Боги»: есть три вида богов" + D + "боги по общему признанию [вариант написания (Syā.): sammatidevā], "
                   "боги по рождению, боги по чистоте.",
        "Sammutidevā nāma": "Боги по общему признанию" + D + "это цари, царицы и царевичи.",
        "Upapattidevā nāma": "Боги по рождению" + D + "это боги, начиная с богов Четырёх Великих Царей [вариант написания "
                             "(Sī., Syā.): cātummahārājike], и выше.",
        "Visuddhidevā nāma": "Боги по чистоте" + D + "так называют архатов.",
        "Manussānaṃ kittakaṃ": "Какова продолжительность жизни людей? Сто лет, немного меньше или больше [вариант чтения "
                               "(Syā., Ka.): appaṃ vā bhiyyo vā; dī. ni. 2.7].",
    }
    for k, v in fixed.items():
        if p.startswith(k):
            return v
    if p.startswith("Dānaṃ datvā"):
        did = "дал подаяние, взял на себя нравственность, соблюдал постный день"
        dest = ["богатых знатных правителей", "богатых брахманов", "богатых домохозяев"] + \
               [GODS[g] for g in ("cātumahārājikānaṃ", "tāvatiṃsānaṃ", "yāmānaṃ", "tusitānaṃ", "nimmānaratīnaṃ",
                                  "paranimmitavasavattīnaṃ")]
        assert p.count("sahabyataṃ upapajjanti") == len(dest)
        return (f"Где перерождаются те, кто {did}? Из тех, кто {did}, " +
                ", ".join(f"некоторые {SAHABYA} {d}" for d in dest) + ".")
    for i, (g, day, years, human) in enumerate(DIVINE):
        if p.startswith(g[:1].upper() + g[1:] + " devānaṃ kittakaṃ"):
            gods = GODS[g]
            var = " [вариант написания (Ka.): rattidivo; a. ni. 3.71]" if i == 0 else ""
            return (f"Какова продолжительность жизни {gods}? {day} составляют одни сутки{var} для {gods}. Тридцать таких "
                    f"ночей составляют месяц. Двенадцать таких месяцев составляют год. {years} продолжительность жизни "
                    f"{gods}. Сколько это по человеческому счёту? {human}")
    for k, r in zip(VERSE_LIFE_P + VERSE_END_P, VERSE_LIFE + VERSE_END):
        if p.startswith(k):
            return r
    m = re.match(r"^(Paṭhamaṃ|Dutiyaṃ|Tatiyaṃ) jhānaṃ (parittaṃ|majjhimaṃ|paṇītaṃ) bhāvetvā kattha upapajjanti\? \1 jhānaṃ "
                 r"\2 bhāvetvā (\w+) devānaṃ sahabyataṃ upapajjanti\. Tesaṃ kittakaṃ āyuppamāṇaṃ\? (.+)$", p)
    if m:
        jh, deg, god, span = m.groups()
        w = who_did(jh, deg)
        return (f"Где перерождаются те, {w}? Те, {w}, {SAHABYA} {GODS[god]}. Какова продолжительность их жизни? "
                f"{SPAN[span]}")
    if p.startswith("Catutthaṃ jhānaṃ bhāvetvā"):
        gods = re.findall(r"appekacce (\w+) devānaṃ sahabyataṃ upapajjanti", p)
        assert len(gods) == 11 and p.count("appekacce") == 11, gods
        return (f"Из тех, {who_did('Catutthaṃ', None)}, вследствие различия объектов, различия внимания, различия "
                "желания, различия устремления, различия решимости, различия направленности, различия мудрости " +
                ", ".join(f"некоторые {SAHABYA} {GODS[g]}" for g in gods) + ".")
    m = re.match(r"^(\w+?)ñca (\w+?)ñca devānaṃ kittakaṃ āyuppamāṇaṃ\? (.+)$", p)
    if m:
        a, b, span = m.groups()
        return f"Какова продолжительность жизни {GODS[a.lower() + 'ṃ']} и {GODS[b + 'ṃ']}? {SPAN[span]}"
    m = re.match(r"^(\w+) devānaṃ kittakaṃ āyuppamāṇaṃ\? (.+)$", p)
    if m:
        return f"Какова продолжительность жизни {GODS[m.group(1).lower()]}? {SPAN[m.group(2)]}"
    raise KeyError(p)


# ---------------------------------------------------------------- sections 7-10
Q7 = ["следует постичь высшим знанием", "следует полностью понять", "следует устранить", "следует развивать",
      "следует осуществить", "не следует устранять, не следует развивать, не следует осуществлять"]
Q_SUB = {
    "##### Kusalattikaṃ": Q_KUS,
    "##### Vedanātikaṃ": [PRED[k][0]["pl"] for k in ("§sukha", "§dukkha", "§adm")],
    "##### Vipākattikaṃ": [PRED[k][0]["pl"] for k in ("vipāk", "vipākadhammadhamm", "nevavipākanavipākadhammadhamm")],
    "##### Upādinnattikaṃ": [PRED[k][0]["pl"] for k in ("upādinnupādāniy", "anupādinnupādāniy", "anupādinnaanupādāniy")],
    "##### Vitakkattikaṃ": [PRED["savitakkasavicār"][0]["pl"], "явлениями без направленной мысли, только с удержанием "
                            "мысли", "явлениями без направленной мысли и без удержания мысли"],
    "##### (1) Rūpadukaṃ": ["являются материальными", "нематериальными"],
}


def sec7_10(p, sec, sub):
    p = S.ID.sub("", p).rstrip()
    if p.startswith("Pañcannaṃ khandhānaṃ kati"):
        if sec == "#### Abhiññeyyādivāro":
            return howmany(Q7)
        if sec == "#### Sārammaṇānārammaṇavāro":
            if "sārammaṇārammaṇā" in p:
                return howmany([PRED["sārammaṇārammaṇ"][0]["pl"], PRED["anārammaṇārammaṇ"][0]["pl"]])
            return howmany(["имеют объект", "не имеют объекта"])
        if sec == "#### Diṭṭhasutādidassanavāro":
            return howmany(["увидены", "услышаны", "ощущены", "познаны", "не увидены, не услышаны, не ощущены, не познаны"])
        if sub == "##### (2) Lokiyadukaṃ":
            pr = "являются мирскими, сколько надмирскими"
            return (f"Сколько из пяти совокупностей {pr}? Сколько из двенадцати сфер восприятия {pr}? Сколько из "
                    f"восемнадцати элементов {pr}? Сколько из четырёх истин {pr}… сколько {LAST_GEN} {pr}?")
        return howmany(Q_SUB[sub])
    if p.startswith("Abhiññā dve sārammaṇā"):
        return "Высшее знание, два раздела об объекте, увиденное, благое, чувство;"
    if p.startswith("Vipākā ca upādinnā"):
        return "Результаты действий и охваченное цеплянием, направленная мысль, материальное и мирское."
    if p == "Dhammahadayavibhaṅgo niṭṭhito.":
        return S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[18])
    if p == "Vibhaṅgapakaraṇaṃ niṭṭhitaṃ.":
        return "Книга «" + S.BOOK_TITLE + "» завершена."
    if p.endswith("lokuttarāti."):
        p = p[:-len("ti.")] + "."
    return pred_line(p)


in_pi1("Книга «Перечисление явлений» завершена.", "Раздел о материальной форме завершён.")


# ================================================================ 8. sentence-level consistency with pi-2 ch1-17 / pi-1
SPLIT = re.compile(r"(?<=[.?!])\s+(?=[\"(“«„A-ZĀĪŪṬḌÑṆṄṂḶА-ЯЁ])")


def sents(s):
    return [x.strip() for x in SPLIT.split(S.ID.sub("", s).strip()) if x.strip()]


def sentence_map():
    m = {}
    for pd, rd, skip in (("pi-2_split_chapters", "pi-2-russian-plain-zeroshot_split_chapters", "18-"),
                         ("pi-1_split_chapters", "pi-1-russian-plain-rails_split_chapters", None)):
        for p in sorted(glob.glob(os.path.join(AI, "pali", pd, "*.md"))):
            nm = os.path.basename(p)
            if skip and nm.startswith(skip):
                continue
            rp = os.path.join(AI, "russian", rd, nm)
            if not os.path.exists(rp):
                continue
            pl = open(p, encoding="utf-8").read().split("\n")
            rl = open(rp, encoding="utf-8").read().split("\n")
            if len(pl) != len(rl):
                continue
            for a, b in zip(pl, rl):
                if not a.strip() or a.startswith("#"):
                    continue
                sa, sb = sents(a), sents(b)
                if len(sa) == len(sb):
                    for x, y in zip(sa, sb):
                        m.setdefault(x, y)
    return m


# ================================================================ 9. build
def build():
    pali = open(os.path.join(S.PALI_DIR, FN), encoding="utf-8").read().rstrip("\n").split("\n")
    nonempty = [l for l in pali if l.strip()]
    clean = [S.ID.sub("", l).rstrip() for l in nonempty]
    ru = translate(clean)
    assert len(ru) == len(nonempty), (len(ru), len(nonempty))
    for p, r in zip(clean, ru):
        assert p.count(DASH) + p.count("—") == r.count(DASH), ("dash count", p[:90], r[:120])
        assert "—" not in r and "  " not in r, r[:80]
        assert p.startswith("#") == r.startswith("#"), (p[:40], r[:40])
        assert not re.search(r"[A-Za-zĀāĪīŪūṬṭḌḍÑñṆṇṄṅṂṃḶḷ]", re.sub(r"\[[^\]]*\]", "", r)), ("latin", r[:160])
        assert not re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", r), r[:80]
        assert r.count("«") == r.count("»") and r.count("„") == r.count("“"), ("quotes", r[:120])
        assert not re.search(r"\.\.|,,|\s[,.;?]", r), ("punct", r[:200])
    # identical Pāli sentence = identical Russian (pi-2 ch1-17, pi-1)
    smap = sentence_map()
    hits, bad = 0, []
    for p, r in zip(clean, ru):
        if p.startswith("#"):
            continue
        sp, sr = sents(p), sents(r)
        if len(sp) != len(sr):
            continue
        for a, b in zip(sp, sr):
            if a in smap:
                hits += 1
                if smap[a] != b:
                    bad.append((a, smap[a], b))
    for a, x, y in bad:
        print("MISMATCH:", a, "\n  old:", x, "\n  new:", y)
    assert not bad, len(bad)
    lines = S.attach_ids(pali, ru)
    S.write(os.path.join(S.RU_DIR, FN), lines)
    print("OK:", FN, "|", len(ru), "non-empty lines |", hits, "sentences identical to pi-2 ch1-17 / pi-1")


if __name__ == "__main__":
    build()
