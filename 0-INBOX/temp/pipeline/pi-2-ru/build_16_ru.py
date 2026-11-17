# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: chapter 16 (Ñāṇavibhaṅga).

usage: python -I -X utf8 build_16_ru.py
Writes AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\16-nanavibhango.md.
Imports build_13_15_ru (Y) and through it S, B, T, F, G, X (all read-only).
Reused: the matrix-item lexicon (B.ITEMS / T.ITEMS2, SURF2), the paññā synonym run (ch10-12, pi-1 ^1-16),
ch1 classification frame (S.HOW_MANY), ch7 mind states (build_7_9_ru.CITTA_ST), ch12 arūpa formulas,
ch15 paṭisambhidā strings, pi-1 jhāna paṭipadā / ārammaṇa phrases, pi-1 view list (^1-1009 …),
pi-1 / ch6 dependent-origination chain (^1-1343), pi-4 abhiññā formulas (^4-183, ^4-184, ^4-185, ^4-12, ^4-13).
Formulaic lines are parsed from the Pāli; unique lines are matched in order by their opening words
(the builder asserts every Pāli line starts with the expected words). Importing this module writes nothing.
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru"
sys.path.insert(0, HERE)
import build_13_15_ru as Y  # noqa: E402
import build_7_9_ru as W    # noqa: E402

S, B, T, F, G, X = Y.S, Y.B, Y.T, Y.F, Y.G, Y.X
DASH = S.DASH
cap, lc = S.cap, X.lc
in_pi1, edit = F.in_pi1, F.edit
TATTHA = S.TATTHA                 # Что такое здесь
called = Y.called                 # это называется «X»
FN = "16-nanavibhango.md"

# ================================================================ 1. frames
HOW = S.HOW_MANY
NUMW = {"Eka": 1, "Du": 2, "Ti": 3, "Catub": 4, "Pañca": 5, "Chab": 6, "Satta": 7, "Aṭṭha": 8, "Nava": 9, "Dasa": 10}
NUMW.update({k.lower(): v for k, v in list(NUMW.items())})
NV = "основ знания"                                       # ñāṇavatthu [new]; vatthu (physical base) = основа [pi-1]


def frame(n):
    return f"Классификация {NV} {HOW[n]}"


def frame_close(n):
    return f"Такова классификация {NV} {HOW[n]}."


HEAD4 = {"Ekakamātikā": "Матрица единиц", "Dukamātikā": "Матрица пар", "Tikamātikā": "Матрица троек",
         "Catukkamātikā": "Матрица четвёрок", "Pañcakamātikā": "Матрица пятёрок", "Chakkamātikā": "Матрица шестёрок",
         "Sattakamātikā": "Матрица семёрок", "Aṭṭhakamātikā": "Матрица восьмёрок", "Navakamātikā": "Матрица девяток",
         "Dasakamātikā": "Матрица десяток", "Mātikā": "Матрица"}           # pi-1 mātikā = матрица
GROUPW = {"Ekaka": "единиц", "Duka": "пар", "Tika": "троек", "Catukka": "четвёрок", "Pañcaka": "пятёрок",
          "Chakka": "шестёрок", "Sattaka": "семёрок", "Aṭṭhaka": "восьмёрок", "Navaka": "девяток", "Dasaka": "десяток"}
CLOSE_GROUP = {"Ekakaṃ.": "Единицы.", "Dukaṃ.": "Пары.", "Tikaṃ.": "Тройки.", "Catukkaṃ.": "Четвёрки.",
               "Pañcakaṃ.": "Пятёрки.", "Chakkaṃ.": "Шестёрки.", "Sattakaṃ.": "Семёрки.", "Aṭṭhakaṃ.": "Восьмёрки.",
               "Navakaṃ.": "Девятки.", "Dasakaṃ.": "Десятки."}
assert B.LABELS["##### Tikaṃ"] == "##### Тройки" and B.LABELS["##### Dukaṃ"] == "##### Пары"
LABEL = {"Ka": "а", "Kha": "б", "Ga": "в", "Gha": "г", "Kha-gha": "б-г"}

# ================================================================ 2. paññā phrases (matrix items)
PANNA_PE = "мудрость, понимание… отсутствие заблуждения, исследование явлений, правильное воззрение"   # ch10-12
NOMW = {}
for _w in ("подверженн", "свободн", "связанн", "затронут", "охваченн", "сопровождаем", "устраняем", "познаваем",
           "способн", "неомрачённ", "омрачённ", "мирск", "надмирск", "ограниченн", "возвышенн", "безмерн", "прошл",
           "предопределённ", "непредопределённ"):
    NOMW[_w + "ой"] = _w + "ая"
for _w in ("служащ", "ведущ", "имеющ", "принадлежащ", "будущ", "настоящ", "внутренн", "внешн", "возникш", "невозникш"):
    NOMW[_w + "ей"] = _w + ("яя" if _w.endswith("нн") or _w.endswith("шн") else "ая")
for _w in ("относящ", "находящ", "являющ"):
    NOMW[_w + "ейся"] = _w + "аяся"
PREP = {"с", "со", "без", "к", "от", "в", "на", "под", "ни"}


def nom_of_b(b):
    out, prev = [], None
    for w in b.split(" "):
        out.append(w if prev in PREP else NOMW.get(w, w))
        prev = w
    return " ".join(out)


PN = {   # overrides: Pāli (feminine surface) -> (nominative, instrumental) of "X paññā"
    "vipākā": ("мудрость, которая является результатом действий", "мудростью, которая является результатом действий"),
    "nevavipākanavipākadhammadhammā": (
        "мудрость, которая не является результатом действий и не способна приносить результаты",
        "мудростью, которая не является результатом действий и не способна приносить результаты"),
    "uppādinī": ("мудрость, которой предстоит возникнуть", "мудростью, которой предстоит возникнуть"),
    "atthajāpikā": ("мудрость, производящая цель", "мудростью, производящей цель"),                  # [new]
    "jāpitatthā": ("мудрость, цель которой произведена", "мудростью, цель которой произведена"),     # [new]
    "hānabhāginī": ("мудрость, ведущая к упадку", "мудростью, ведущей к упадку"),                   # [new]
    "ṭhitibhāginī": ("мудрость, ведущая к устойчивости", "мудростью, ведущей к устойчивости"),
    "visesabhāginī": ("мудрость, ведущая к отличию", "мудростью, ведущей к отличию"),
    "nibbedhabhāginī": ("мудрость, ведущая к проникновению", "мудростью, ведущей к проникновению"),
    "maggādhipatinī": ("мудрость, находящаяся под главенством пути", "мудростью, находящейся под главенством пути"),
}
for _p, _r in (("cintāmayā", "на размышлении"), ("sutamayā", "на услышанном"), ("bhāvanāmayā", "на развитии ума"),
               ("dānamayā", "на даянии"), ("sīlamayā", "на нравственности")):          # ch6 «основанное на даянии …»
    PN[_p] = (f"мудрость, основанная {_r}", f"мудростью, основанной {_r}")
for _p, _r in (("adhisīle", "в высшей нравственности"), ("adhicitte", "в высшем уме"),
               ("adhipaññāya", "в высшей мудрости")):
    PN[_p] = (f"мудрость {_r}", f"мудростью {_r}")
PATI = {"dukkhapaṭipadā": "трудным", "sukhapaṭipadā": "лёгким", "dandhābhiññā": "медленным", "khippābhiññā": "быстрым"}
for _a in ("dukkhapaṭipadā", "sukhapaṭipadā"):
    for _b in ("dandhābhiññā", "khippābhiññā"):
        _r = f"с {PATI[_a]} способом практики и {PATI[_b]} высшим знанием"                   # pi-1 ^1-179 …
        PN[f"{_a} {_b}"] = (f"мудрость {_r}", f"мудростью {_r}")
in_pi1("с трудным способом практики и медленным высшим знанием", "с трудным способом практики и быстрым высшим знанием",
       "с лёгким способом практики и медленным высшим знанием", "с лёгким способом практики и быстрым высшим знанием")
for _a, _ra in (("parittā", ("ограниченная", "ограниченной")), ("appamāṇā", ("безмерная", "безмерной"))):
    for _b, _rb in (("parittārammaṇā", "ограниченным"), ("appamāṇārammaṇā", "безмерным")):
        PN[f"{_a} {_b}"] = (f"мудрость, {_ra[0]} и с {_rb} объектом", f"мудростью, {_ra[1]} и с {_rb} объектом")
in_pi1("ограниченное и с ограниченным объектом", "ограниченное и с безмерным объектом",
       "безмерное и с ограниченным объектом", "безмерное и с безмерным объектом")
ACAYA = {"ācayāya no apacayāya": "ведущая к накоплению, а не к убыванию",
         "apacayāya no ācayāya": "ведущая к убыванию, а не к накоплению",
         "ācayāya ceva apacayāya ca": "ведущая и к накоплению, и к убыванию",
         "nevācayāya no apacayāya": "не ведущая ни к накоплению, ни к убыванию",
         "neva ācayāya no apacayāya": "не ведущая ни к накоплению, ни к убыванию",
         "nibbidāya no paṭivedhāya": "ведущая к разочарованию, а не к проникновению",
         "paṭivedhāya no nibbidāya": "ведущая к проникновению, а не к разочарованию",
         "nibbidāya ceva paṭivedhāya ca": "ведущая и к разочарованию, и к проникновению",
         "neva nibbidāya no paṭivedhāya": "не ведущая ни к разочарованию, ни к проникновению"}
ACAYA_V = {k: v.replace("ведущая", "ведёт") for k, v in ACAYA.items()}
ACAYA_I = {k: v.replace("ведущая", "ведущей") for k, v in ACAYA.items()}
T.alias("uppadi", "uppādinī")


def b_of(surface):
    return T.ITEMS2[T.SURF2[surface]]["b"]


def pn(s):
    """'X' of "X paññā" -> (nominative, instrumental)."""
    if s in PN:
        return PN[s]
    m = re.match(r"^(\w+)vippayuttā (\w+)$", s)       # "āsavavippayuttā sāsavā" (pi-2 spacing) = āsavavippayuttasāsavā
    key = m.group(1) + "vippayutta" + m.group(2) if m else s
    b = b_of(key)
    nom = nom_of_b(b)
    words = b.split(" ")
    if all(w in NOMW or w == "и" for w in words):
        return f"{nom} мудрость", f"{b} мудростью"
    if words[0] in ("с", "без"):
        return f"мудрость {nom}", f"мудростью {b}"
    return f"мудрость, {nom}", f"мудростью, {b}"


def list_nom(items):
    """matrix list line: «Мирская мудрость, надмирская мудрость» (';' when an item carries its own commas)."""
    sep = "; " if any(", " in x for x in items) else ", "
    return cap(sep.join(items))


def panna_list(body):
    out = []
    for p in body.split(" paññā"):
        p = p.strip(" ,")
        if p:
            out.append(pn(p[:1].lower() + p[1:])[0])
    return list_nom(out)


# ================================================================ 3. the onefold matrix (five consciousnesses)
EKAKA_NEG = {"na savitakkasavicārā": "savitakkasavicārā", "na avitakkavicāramattā": "avitakkavicāramattā"}
NO_APARIYAPANNA = "не относятся к явлениям, не принадлежащим к кругам существования"   # pi-1 ^1-584 (sg) as plural
in_pi1("не относится к явлениям, не принадлежащим к кругам существования")


def p_of(surface):
    if surface == "no apariyāpannā":
        return NO_APARIYAPANNA
    if surface in EKAKA_NEG:
        return "не " + T.ITEMS2[T.SURF2[EKAKA_NEG[surface]]]["p"]
    return T.ITEMS2[T.SURF2[surface]]["p"]


EKAKA_PALI = None   # filled from the Pāli (line 5)
SUBJ5 = "пять видов сознания"                                          # pañca viññāṇā [pi-1 «шестью видами сознания»]
ALWAYS = "непременно"                                                  # -meva [new]
EK = {   # the other onefold items: (mātikā line, quoted lemma in the explanation)
    "uppanna": ("Имеют возникшую основу и возникший объект", "имеют возникшую основу, возникший объект"),
    "purejata": ("Имеют ранее возникшую основу и ранее возникший объект",
                 "Имеют ранее возникшую основу, ранее возникший объект"),
    "ajjhattika": ("Имеют основу, относящуюся к внутреннему, и объект, относящийся к внешнему",
                   "Имеют основу, относящуюся к внутреннему, объект, относящийся к внешнему"),
    "asambhinna": ("Имеют неразрушенную основу и неразрушенный объект", "Имеют неразрушенную основу, неразрушенный объект"),
    "nana": ("Имеют разные основы и разные объекты", "Имеют разные основы, разные объекты"),
    "gocara": ("Не испытывают сферы действия друг друга", "Не испытывают сферы действия друг друга"),
    "samannahara": ("Не возникают без обращения внимания", "Не возникают без обращения внимания"),
    "manasikara": ("Не возникают без внимания", "Не возникают без внимания"),
    "abbokinna": ("Не возникают непрерывной чередой", "Не возникают непрерывной чередой"),
    "apubbam": ("Не возникают одновременно", "Не возникают одновременно"),
    "samanantara": ("Не возникают непосредственно друг после друга", "Не возникают непосредственно друг после друга"),
    "anabhoga": ("Пять видов сознания лишены вовлечённости", "Пять видов сознания лишены вовлечённости"),
}
BY5 = "Посредством пяти видов сознания"
AFTER5 = "И непосредственно после пяти видов сознания"
MANODHATU = "и посредством элемента ума, следующего непосредственно за пятью видами сознания,"   # samanantarā manodhātuyāpi
ACTS = {   # Pāli predicate -> Russian (indefinite-personal plural)
    "na kañci dhammaṃ paṭivijānāti": "не распознают никакого явления",
    "na kañci iriyāpathaṃ kappeti": "не принимают никакого положения тела",
    "na kāyakammaṃ na vacīkammaṃ paṭṭhapeti": "не совершают ни телесного действия, ни речевого действия",
    "na kusalākusalaṃ dhammaṃ samādiyati": "не принимают на себя благого или неблагого явления",
    "na samāpajjati na vuṭṭhāti": "не входят в медитативное достижение и не выходят из него",
    "na cavati na uppajjati": "не умирают и не рождаются",
    "na supati na paṭibujjhati na supinaṃ passati": "не засыпают, не просыпаются и не видят снов",
}
ABHINIPATA = "кроме простого столкновения"                    # aññatra abhinipātamattā [new]
APATA = "кроме простого попадания в поле восприятия"           # aññatra āpātamattā [new]
POSTURES = "ни хождения, ни стояния, ни сидения, ни лежания"   # gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā
YATHAVAKA = "мудрость, проясняющая предмет таким, каков он есть"   # yāthāvakavatthuvibhāvanā paññā [new]
VAR_KINCI = " [вариант написания (Sī., Ka.): kiñci]"
VG = {"cakkhu": "зрительного сознания", "sota": "слухового сознания", "ghāna": "обонятельного сознания",
      "jivhā": "вкусового сознания", "kāya": "осязательного сознания"}
VN = {"cakkhu": "зрительное сознание", "sota": "слуховое сознание", "ghāna": "обонятельное сознание",
      "jivhā": "вкусовое сознание", "kāya": "осязательное сознание"}
VGC = {k: cap(v) for k, v in VG.items()}


def acts_pali_ru(rest):
    """'Pañcahi viññāṇehi <act>' / 'Pañcannaṃ viññāṇānaṃ samanantarāpi <act>' (mātikā wording)."""
    m = re.match(r"^Pañcahi viññāṇehi (.+?)( \[kiñci \(sī\. ka\.\)\])?( .+?)?$", rest)
    for k, v in ACTS.items():
        if rest == f"Pañcahi viññāṇehi {k}":
            return f"{BY5} {v}"
        if rest == f"Pañcannaṃ viññāṇānaṃ samanantarāpi {k}":
            return f"{AFTER5} {v}"
    raise KeyError("act: " + rest)


def ekaka_matika(p):
    """line 5 of the Pāli: the list of the five consciousnesses' matrix attributes."""
    global EKAKA_PALI
    body = p[len("Ekavidhena ñāṇavatthu – pañca viññāṇā "):]
    assert body.endswith(",")
    EKAKA_PALI = body[:-1].split(", ")
    preds = [p_of(x) for x in EKAKA_PALI]
    return f"{frame(1)} {DASH} {SUBJ5} " + ", ".join(preds) + ","


def ekaka_niddesa(p):
    """^2-761: 'Pañca viññāṇā na hetumeva, …, jarābhibhūtameva.'"""
    items = p[len("Pañca viññāṇā "):-1].split(", ")
    assert len(items) == len(EKAKA_PALI) + 3, (len(items), len(EKAKA_PALI))
    for a, b in zip(items, EKAKA_PALI):
        assert a.endswith("meva") and a[:4].replace("ā", "a") == b[:4].replace("ā", "a"), (a, b)
    preds = [p_of(x) for x in EKAKA_PALI] + ["являются возникшими и познаются умственным сознанием",
                                             "являются непостоянными", "подвластны старению"]
    assert items[-3:] == ["uppannaṃ manoviññāṇaviññeyyameva", "aniccameva", "jarābhibhūtameva"]
    return f"Пять видов сознания " + ", ".join(f"{ALWAYS} {x}" for x in preds) + "."


def gocara_sent(a, b, verb):
    """X-ssa gocaravisayaṃ Y na paccanubhoti, Y-ssa gocaravisayampi X na paccanubhoti"""
    if verb == "gocara":
        return (f"сферу действия {VG[a]} не испытывает {VN[b]}, и сферу действия {VG[b]} не испытывает {VN[a]}")
    return (f"сразу после возникновения {VG[a]} не возникает {VN[b]}, и сразу после возникновения {VG[b]} не возникает "
            f"{VN[a]}")


def gocara_line(verb):
    v = [("cakkhu", "sota"), ("cakkhu", "ghāna"), ("cakkhu", "jivhā"), ("cakkhu", "kāya")]
    w = [("kāya", "sota"), ("kāya", "ghāna"), ("kāya", "jivhā")]
    first = ("«Не испытывают сферы действия друг друга»: " if verb == "gocara"
             else "«Не возникают непосредственно друг после друга»: ")
    parts = [gocara_sent(*v[0], verb)] + [cap(gocara_sent(*x, verb)) for x in v[1:]]
    if verb == "gocara":
        pe = (f"Слухового сознания… обонятельного сознания… вкусового сознания… сферу действия {VG['kāya']} не испытывает "
              f"{VN['cakkhu']}, и сферу действия {VG['cakkhu']} не испытывает {VN['kāya']}")
    else:
        pe = (f"Слухового сознания… обонятельного сознания… вкусового сознания… сразу после возникновения {VG['kāya']} "
              f"не возникает {VN['cakkhu']}, и сразу после возникновения {VG['cakkhu']} не возникает {VN['kāya']}")
    return first + ". ".join(parts) + ". " + pe + ". " + ". ".join(cap(gocara_sent(*x, verb)) for x in w) + "."


# ================================================================ 4. locatives ("tīsu bhūmīsu kusalābyākate paññā")
LOCS = {
    "tīsu bhūmīsu kusalābyākate": "в благом и этически неопределённом на трёх уровнях",
    "catūsu maggesu catūsu phalesu": "в четырёх путях и четырёх плодах",                       # ch15
    "tīsu bhūmīsu vipāke": "в результатах действий на трёх уровнях",
    "catūsu bhūmīsu vipāke": "в результатах действий на четырёх уровнях",
    "catūsu bhūmīsu kusale": "в благом на четырёх уровнях",
    "tīsu bhūmīsu kusale": "в благом на трёх уровнях",
    "tīsu bhūmīsu kiriyābyākate": "в функциональном этически неопределённом на трёх уровнях",
    "catūsu maggesu": "в четырёх путях", "catūsu phalesu": "в четырёх плодах",
    "catūsu maggesu tīsu phalesu": "в четырёх путях и трёх плодах",
    "kāmāvacarakusalābyākate": "в благом и этически неопределённом, относящемся к миру чувственных желаний",
    "rūpāvacarakusalābyākate": "в благом и этически неопределённом, относящемся к миру форм",
    "arūpāvacarakusalābyākate": "в благом и этически неопределённом, относящемся к миру без форм",
    "rūpāvacarārūpāvacarakusalābyākate": "в благом и этически неопределённом, относящемся к миру форм и к миру без форм",
    "kāmāvacarakusale": "в благом, относящемся к миру чувственных желаний",
    "rūpāvacarārūpāvacarakusale": "в благом, относящемся к миру форм и к миру без форм",
    "dvīsu jhānesu": "в двух медитативных погружениях", "tīsu jhānesu": "в трёх медитативных погружениях",
}
LOC_MULTI = {   # several locatives in a row
    "tīsu bhūmīsu kusale tīsu bhūmīsu kiriyābyākate catūsu maggesu catūsu phalesu":
        "в благом на трёх уровнях, в функциональном этически неопределённом на трёх уровнях, в четырёх путях и "
        "четырёх плодах",
    "tīsu bhūmīsu kusale catūsu bhūmīsu vipāke tīsu bhūmīsu kiriyābyākate":
        "в благом на трёх уровнях, в результатах действий на четырёх уровнях и в функциональном этически "
        "неопределённом на трёх уровнях",
    "tīsu bhūmīsu kusale tīsu bhūmīsu kiriyābyākate":
        "в благом на трёх уровнях и в функциональном этически неопределённом на трёх уровнях",
    "catūsu bhūmīsu vipāke tīsu bhūmīsu kiriyābyākate":
        "в результатах действий на четырёх уровнях и в функциональном этически неопределённом на трёх уровнях",
    "tīsu bhūmīsu kusale tīsu bhūmīsu vipāke tīsu bhūmīsu kiriyābyākate":
        "в благом на трёх уровнях, в результатах действий на трёх уровнях и в функциональном этически "
        "неопределённом на трёх уровнях",
    "upariṭṭhimā [upariṭṭhime (syā.), upariṭṭhimaṃ (ka.)] arahattaphale":
        "в высшем [вариант написания (Syā.): upariṭṭhime; (Ka.): upariṭṭhimaṃ] плоде состояния архата",
}
LOCS.update(LOC_MULTI)
SAMPF = {   # "X-sampayuttā paññā" subjects
    "vitakkasampayuttā": "мудрость, связанная с направленной мыслью",
    "vitakkavippayuttā": "мудрость, не связанная с направленной мыслью",
    "vicārasampayuttā": "мудрость, связанная с удержанием мысли",
    "vicāravippayuttā": "мудрость, не связанная с удержанием мысли",
    "pītisampayuttā": "мудрость, связанная с восторгом", "pītivippayuttā": "мудрость, не связанная с восторгом",
    "sukhasampayuttā": "мудрость, связанная со счастьем", "sukhavippayuttā": "мудрость, не связанная со счастьем",
    "upekkhāsampayuttā": "мудрость, связанная с невозмутимостью",
    "upekkhāvippayuttā": "мудрость, не связанная с невозмутимостью",
    "vitakkavicārasampayuttā": "мудрость, связанная с направленной мыслью и удержанием мысли",
    "vitakkavippayuttā vicārasampayuttā": "мудрость, не связанная с направленной мыслью, но связанная с удержанием мысли",
    "vitakkavicāravippayuttā": "мудрость, не связанная ни с направленной мыслью, ни с удержанием мысли",
}


def low1(s):
    return s[:1].lower() + s[1:]


def subj_nom(s):
    s0 = low1(s)
    if s0 in LOCS:
        return f"мудрость {LOCS[s0]}"
    if s0 in SAMPF:
        return SAMPF[s0]
    return pn(s0)[0]


PARTICIPLE = re.compile(r"(относящ|связанн|сопровождаем|охваченн|подверженн|служащ|ведущ|имеющ|находящ|принадлежащ|"
                        r"способн|познаваем|затронут|свободн|основанн|производящ|котор)")


def closing(nom):
    """a closing comma before the predicate only after a participial / relative phrase (not after a list of places)."""
    return nom + ("," if ", " in nom and PARTICIPLE.search(nom.split(", ", 1)[1]) else "")


def is_pred(subj_p, pred_p):
    """'<subj> paññā <pred> paññā' -> «<subj> является <pred ins>»"""
    return f"{closing(subj_nom(subj_p))} является {pn(pred_p)[1]}"


HALF = re.compile(r"^(.+?) paññā (.+?)(?: paññā)?$")


def duka_line(body):
    """'A paññā X paññā, B paññā Y paññā' (one or two halves)."""
    halves = body.split(" paññā, ")
    out = []
    for h in halves:
        m = HALF.match(h)
        out.append(is_pred(m.group(1), m.group(2)))
    return cap("; ".join(out)) + "."


# ================================================================ 5. "… ārabbha yā uppajjati paññā …" answers
OBJI = {   # ārabbha object -> «в связи с …»
    "dukkhaṃ": "со страданием", "dukkhasamudayaṃ": "с возникновением страдания",
    "dukkhanirodhaṃ": "с прекращением страдания",
    "dukkhanirodhagāminiṃ paṭipadaṃ": "со способом практики, ведущим к прекращению страдания",
    "jarāmaraṇaṃ": "со старением и смертью", "jarāmaraṇasamudayaṃ": "с возникновением старения и смерти",
    "jarāmaraṇanirodhaṃ": "с прекращением старения и смерти",
    "jarāmaraṇanirodhagāminiṃ paṭipadaṃ": "со способом практики, ведущим к прекращению старения и смерти",
    "saṅkhāre": "с формирующими факторами", "saṅkhārasamudayaṃ": "с возникновением формирующих факторов",
    "saṅkhāranirodhaṃ": "с прекращением формирующих факторов",
    "saṅkhāranirodhagāminiṃ paṭipadaṃ": "со способом практики, ведущим к прекращению формирующих факторов",
    "paritte dhamme": "с ограниченными явлениями", "mahaggate dhamme": "с возвышенными явлениями",
    "appamāṇe dhamme": "с безмерными явлениями", "ariyamaggaṃ": "с благородным путём",
    "atīte dhamme": "с прошлыми явлениями", "anāgate dhamme": "с будущими явлениями",
    "paccuppanne dhamme": "с настоящими явлениями", "ajjhatte dhamme": "с внутренними явлениями",
    "bahiddhādhamme": "с внешними явлениями", "ajjhattabahiddhā dhamme": "с внутренними и внешними явлениями",
}
WHO = {   # genitive participles before "yā uppajjati paññā" -> «у того, кто …,»
    "Pātimokkhasaṃvaraṃ saṃvarantassa": "у того, кто сдерживает себя сдержанностью свода монашеских правил,",
    "Rūpāvacarārūpāvacarasamāpattiṃ samāpajjantassa":
        "у того, кто входит в медитативное достижение, относящееся к миру форм или к миру без форм,",
    "Dānaṃ ārabbha dānādhigaccha": "в связи с даянием, благодаря даянию",
    "Sīlaṃ ārabbha sīlādhigaccha": "в связи с нравственностью, благодаря нравственности",
    "Ariyamaggaṃ adhipatiṃ karitvā": ", сделав благородный путь главенствующим,",
}
for _a, _ra in (("Kicchena kasirena", "с трудом и тяготами"), ("Akicchena akasirena", "без труда и тягот")):
    for _b, _rb in (("dandhaṃ", "медленно"), ("khippaṃ", "быстро")):
        WHO[f"{_a} samādhiṃ uppādentassa {_b} taṇṭhānaṃ abhijānantassa"] = (
            f"у того, кто {_ra} порождает сосредоточение и {_rb} постигает высшим знанием это состояние,")
for _a, _ra in (("na nikāmalābhissa", "не обретает сосредоточение по своему желанию"),
                ("nikāmalābhissa", "обретает сосредоточение по своему желанию")):
    for _b, _rb in (("thokaṃ", "в малой мере"), ("vipulaṃ", "в обширной мере")):
        WHO[f"Samādhissa {_a} ārammaṇaṃ {_b} pharantassa"] = (
            f"у того, кто {_ra} и распространяет объект {_rb},")
NANA = {   # ñāṇa / kosalla terms: (nominative, instrumental)
    "kammassakatañāṇaṃ": ("знание о собственности действий", "знанием о собственности действий"),
    "saccānulomikaṃ ñāṇaṃ": ("знание, согласующееся с истинами", "знанием, согласующимся с истинами"),
    "maggasamaṅgissa ñāṇaṃ": ("знание обладающего путём", "знанием обладающего путём"),
    "phalasamaṅgissa ñāṇaṃ": ("знание обладающего плодом", "знанием обладающего плодом"),
    "dhamme ñāṇaṃ": ("знание Учения", "знанием Учения"),
    "anvaye ñāṇaṃ": ("знание по выводу", "знанием по выводу"),
    "pariye ñāṇaṃ": ("знание охвата умов", "знанием охвата умов"),
    "sammutiñāṇaṃ": ("знание условного", "знанием условного"),                                 # pi-5
    "āyakosallaṃ": ("искусность в росте", "искусностью в росте"),
    "apāyakosallaṃ": ("искусность в упадке", "искусностью в упадке"),
    "upāyakosallaṃ": ("искусность в средствах", "искусностью в средствах"),
}
GENL = {   # "<loc> ñāṇaṃ" -> «знание <gen>»  (ch15 Y.LOC)
    "dukkhe": "страдания", "dukkhasamudaye": "возникновения страдания", "dukkhanirodhe": "прекращения страдания",
    "dukkhanirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению страдания",
    "jarāmaraṇe": "старения и смерти", "jarāmaraṇasamudaye": "возникновения старения и смерти",
    "jarāmaraṇanirodhe": "прекращения старения и смерти",
    "jarāmaraṇanirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению старения и смерти",
    "jātiyā": "рождения", "bhave": "существования", "upādāne": "цепляния", "taṇhāya": "жажды", "vedanāya": "чувства",
    "phasse": "контакта", "saḷāyatane": "шести сфер восприятия", "nāmarūpe": "умственного и материальной формы",
    "viññāṇe": "сознания", "saṅkhāresu": "формирующих факторов", "saṅkhārasamudaye": "возникновения формирующих факторов",
    "saṅkhāranirodhe": "прекращения формирующих факторов",
    "saṅkhāranirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению формирующих факторов",
}
for _k, _v in GENL.items():
    _yk = _k if _k in Y.LOC else _k[0].upper() + _k[1:]
    assert Y.LOC[_yk].rstrip(",") == _v, _k
for _k, _v in GENL.items():
    NANA[f"{_k} ñāṇaṃ"] = (f"знание {_v}", f"знанием {_v}")
ANUPUBBA = "медитативных достижениях последовательного пребывания"            # anupubbavihārasamāpatti [new]
FIVE_SAMADHI = "пятичастное правильное сосредоточение"          # pañcaṅgiko sammāsamādhi [pi-1 pañcaṅgiko maggo]
FIVE_NANA = "правильное сосредоточение с пятью знаниями"         # pañcañāṇiko sammāsamādhi [new]
NANA.update({
    "pañcaṅgiko sammāsamādhi": (FIVE_SAMADHI, None), "pañcañāṇiko sammāsamādhi": (FIVE_NANA, None),
    "chasu abhiññāsu paññā": ("мудрость в шести высших знаниях", None),
    "sattasattati ñāṇavatthūni": ("семьдесят семь основ знания", None),
    "catūsu maggesu catūsu phalesu paññā": ("мудрость в четырёх путях и четырёх плодах", None),
    "navasu anupubbavihārasamāpattīsu paññā": (f"мудрость в девяти {ANUPUBBA}", None),
})


def term_ins(t):
    if t in NANA:
        return NANA[t][1]
    if t.endswith(" paññā"):
        return pn(t[:-len(" paññā")])[1]
    if t.startswith("paññā "):
        return "мудростью, " + ACAYA_I[t[len("paññā "):]]
    raise KeyError("term: " + t)


def term_nom(t):
    if t in NANA:
        return NANA[t][0]
    if t.endswith(" paññā"):
        return pn(t[:-len(" paññā")])[0]
    if t.startswith("paññā "):
        return "мудрость, " + ACAYA[t[len("paññā "):]]
    if t == "catasso paṭisambhidā":
        return "четыре аналитических знания"
    if t == "catasso paṭipadā":
        return "четыре способа практики"
    if t == "cattāri ārammaṇāni":
        return "четыре объекта"
    raise KeyError("term nom: " + t)


PE_ANS = re.compile(r'^(.+?) yā uppajjati paññā pajānanā ?…pe… amoho dhammavicayo sammādiṭṭhi – (?:ayaṃ|idaṃ) vuccati "(.+)"\.$')


def cond_ru(c):
    """'X ārabbha' / a WHO phrase / a '…pe…' chain of 'X ārabbha' -> Russian before «возникает как …»"""
    if c in WHO:
        return WHO[c]
    if c[0].upper() + c[1:] in WHO:
        return WHO[c[0].upper() + c[1:]]
    bits = c.split("…pe… ")
    out = []
    for i, bt in enumerate(bits):
        m = re.match(r"^(.+) ārabbha$", bt)
        o = OBJI[low1(m.group(1))]
        out.append(f"в связи {o}")
    last = out[-1] + ("," if "ведущ" in out[-1] else "")
    return out, last


def answer(s):
    m = PE_ANS.match(s)
    if not m:
        return None
    c, term = m.groups()
    r = cond_ru(c)
    if isinstance(r, tuple):
        head, last = r
        if len(head) > 1:
            pre = "… ".join(head[:-1]) + "… "
            return f"{pre}то, что {last} возникает как {PANNA_PE}, {DASH} {called(term_ins(term))}."
        return f"То, что {last} возникает как {PANNA_PE}, {DASH} {called(term_ins(term))}."
    glue = "" if r.startswith(",") else " "
    return f"То, что{glue}{r} возникает как {PANNA_PE}, {DASH} {called(term_ins(term))}."


Q = re.compile(r"^[Tt]attha katam(?:ā|aṃ|o|āni) (.+)\?$")


def question(s):
    m = Q.match(s)
    if not m:
        return None
    t = m.group(1)
    if t.startswith("tathāgatassa "):
        return f"{TATTHA} знание, которым Татхагата понимает, как есть на самом деле, {POWER_Q[t]}?"
    head = TATTHA if s[0] == "T" else lc(TATTHA)
    return f"{head} {term_nom(t)}?"


# ================================================================ 6. sentence-level table (unique sentences)
TALA = "то, что здесь есть " + PANNA_PE                                   # yā tattha paññā …
EVARUPA = "то, что есть такая " + PANNA_PE                                 # yā evarūpā paññā …
KHANTI = "согласующееся принятие, воззрение, предпочтение, одобрение, рассмотрение, принятие явлений после их обдумывания"
SKILL_FIELDS = "в делах, требующих умения, в ремёслах, требующих умения, или в науках, требующих умения"
FIVE_AGG_IMP = "или что чувство… восприятие… формирующие факторы… сознание непостоянно"
CITTA_STATES = W.CITTA_ST
OTHERS = "других существ, других личностей"                               # parasattānaṃ parapuggalānaṃ [pi-1 ^1-1051]
in_pi1("других существ, других личностей")
HIRI = "бессовестность, отсутствие страха перед дурным"
in_pi1(HIRI)
SAMP_TAIL = "умножения, обширности, развития и завершённости"              # bhiyyobhāva … pāripūri [pi-1 ^1-1377]
assert SAMP_TAIL in F.SP[3]
SAMP_TO = "ведут к умножению, обширности, развитию и завершённости"
# pi-1 ^1-1009 view list (the "Sassato loko" ten), verbatim
_V = T.PI1["^1-1009"] if "^1-1009" in T.PI1 else None
VIEWS10 = ("«Мир вечен», или «мир не вечен», или «мир конечен», или «мир бесконечен», или «душа то же самое, что и "
           "плоть», или «душа одно, а плоть другое», или «Татхагата существует после смерти», или «Татхагата не "
           "существует после смерти», или «Татхагата и существует, и не существует после смерти», или «Татхагата не "
           "существует и не не существует после смерти»")
in_pi1(VIEWS10)
# pi-1 ^1-1369 "natthi dinnaṃ …" turned positive (kammassakatañāṇa)
NATTHI_PI1 = ("Подаяние ничего не значит, жертвоприношение ничего не значит, подношение ничего не значит, у хорошо и дурно "
              "совершённых поступков нет плода, нет результата, этот мир ничего не значит, иной мир ничего не значит, мать "
              "ничего не значит, отец ничего не значит, нет рождающихся самопроизвольно существ, нет в мире отшельников и "
              "брахманов, идущих верным путём, правильно практикующих, которые, сами постигнув высшим знанием и осуществив "
              "этот мир и иной мир, возвещают о них")
in_pi1(NATTHI_PI1)
ATTHI_DINNAM = ("Подаяние имеет значение, жертвоприношение имеет значение, подношение имеет значение, у хорошо и дурно "
                "совершённых поступков есть плод, есть результат, этот мир имеет значение, иной мир имеет значение, мать "
                "имеет значение, отец имеет значение, есть рождающиеся самопроизвольно существа, есть в мире отшельники и "
                "брахманы, идущие верным путём, правильно практикующие, которые, сами постигнув высшим знанием и "
                "осуществив этот мир и иной мир, возвещают о них")
ARUPA4 = ("с полным преодолением восприятий материальной формы, с исчезновением восприятий соударения, без внимания к "
          "восприятиям разнообразия, с мыслью «Пространство бесконечно» входит в сферу бесконечного пространства и "
          "пребывает в ней")
ARUPA5 = "полностью преодолев сферу бесконечного пространства, с мыслью «Сознание бесконечно» входит в сферу бесконечного сознания и пребывает в ней"
ARUPA6 = "полностью преодолев сферу бесконечного сознания, с мыслью «Нет ничего» входит в сферу отсутствия чего-либо и пребывает в ней"
ARUPA7 = "полностью преодолев сферу отсутствия чего-либо, входит в сферу ни восприятия, ни невосприятия и пребывает в ней"
_CH12 = open(os.path.join(S.RU_DIR, "12-jhanavibhango.md"), encoding="utf-8").read()
for _x in (ARUPA4, ARUPA5, ARUPA6, ARUPA7):
    assert _x in _CH12, _x[:60]
NIRODHA = "прекращение восприятия и ощущаемого"                                # saññāvedayitanirodha [pi-5]
JH = ["первого медитативного погружения", "второго медитативного погружения", "третьего медитативного погружения",
      "четвёртого медитативного погружения", "сферы бесконечного пространства", "сферы бесконечного сознания",
      "сферы отсутствия чего-либо", "сферы ни восприятия, ни невосприятия"]
SAMAP9 = [f"достижение {x}" for x in JH] + [f"достижение {NIRODHA[:-len('восприятия и ощущаемого')]}восприятия и ощущаемого"]
SAMAP9[-1] = "достижение прекращения восприятия и ощущаемого"
ANUPUBBA = "медитативных достижениях последовательного пребывания"
LOKUTTARA_PATHS = ["пути вступления в поток", "плоде вступления в поток", "пути однократного возвращения",
                   "плоде однократного возвращения", "пути невозвращения", "плоде невозвращения",
                   "пути к состоянию архата", "плоде состояния архата"]                 # pi-5
CHAIN = ["неведением обусловлены формирующие факторы", "формирующими факторами обусловлено сознание",
         "сознанием обусловлены умственное и материальная форма",
         "умственным и материальной формой обусловлены шесть сфер восприятия",
         "шестью сферами восприятия обусловлен контакт", "контактом обусловлено чувство", "чувством обусловлена жажда",
         "жаждой обусловлено цепляние", "цеплянием обусловлено существование", "существованием обусловлено рождение",
         "рождением обусловлены старение и смерть"]
for _c in CHAIN[:-1]:
    assert _c in T.PI1["^1-1343"].lower(), _c
POWER = {   # acc. after «понимает, как есть на самом деле,»
    1: "возможное как возможное и невозможное как невозможное",
    2: "результат прошлых, будущих и настоящих совершаемых действий по условиям и по причинам",
    3: "способ практики, ведущий повсюду",
    4: "мир со множеством элементов, с разнообразием элементов",
    5: "разнообразие устремлений существ",
    6: f"более высокий и более низкий уровень способностей {OTHERS}",
    7: ("омрачение, очищение и выход в медитативных погружениях, освобождениях, сосредоточениях и медитативных "
        "достижениях"),
    8: "припоминание прежних жизней",                       # pi-1 ^1-1380
    9: "смерть и новое рождение существ",                   # pi-1 ^1-1380
    10: "уничтожение влечений",                             # pi-1 ^1-1380
}
in_pi1("знание припоминания прежних жизней", "знание о смерти и новом рождении существ",
       "знание об уничтожении влечений")
POWER_P = {
    1: "ṭhānañca ṭhānato aṭṭhānañca aṭṭhānato",
    2: "atītānāgatapaccuppannānaṃ kammasamādānānaṃ ṭhānaso hetuso vipākaṃ",
    3: "sabbatthagāminiṃ paṭipadaṃ", 4: "anekadhātu nānādhātulokaṃ", 5: "sattānaṃ nānādhimuttikataṃ",
    6: "parasattānaṃ parapuggalānaṃ indriyaparopariyattaṃ",
    7: "jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ vuṭṭhānaṃ", 8: "pubbenivāsānussatiṃ",
    9: "sattānaṃ cutūpapātaṃ", 10: "āsavānaṃ khayaṃ",
}
POWER_Q = {f"tathāgatassa {v} yathābhūtaṃ ñāṇaṃ": POWER[k] for k, v in POWER_P.items()}
POWER_Q["tathāgatassa anekadhātunānādhātulokaṃ yathābhūtaṃ ñāṇaṃ"] = POWER[4]           # niddesa spelling
POWER_Q["tathāgatassa jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ yathābhūtaṃ ñāṇaṃ"] = (
    "омрачение и очищение в медитативных погружениях, освобождениях, сосредоточениях и медитативных достижениях")
POWER_Q["tathāgatassa pubbenivāsānussati yathābhūtaṃ ñāṇaṃ"] = POWER[8]                # as written (nom. form)
VAR_ANEKADHATU = " [вариант написания (Syā.): anekadhātuṃ nānādhātuṃ lokaṃ; ma. ni. 1.148]"
LION = ("опираясь на которую Татхагата заявляет о своём положении вожака, издаёт львиный рык в собраниях, приводит в "
        "движение колесо Брахмы")
LION_PL = LION.replace("опираясь на которую", "обладая которыми,")
POWERS10 = "десять сил Татхагаты, присущих Татхагате"


def know_ans(k):
    return f"{TALA}, {DASH} это знание, которым Татхагата понимает, как есть на самом деле, {k}"


def power_line(n, first_var=""):
    x = POWER[n]
    head = "Вот Татхагата понимает" if n == 1 else "И далее, Татхагата понимает"
    return (f"{head}, как есть на самом деле, {x}{first_var}. И то, что Татхагата понимает, как есть на самом деле, {x}, "
            f"это тоже является силой Татхагаты, присущей Татхагате, {LION}.")


# ---- ṭhānāṭṭhāna (^2-809)
DS = "человек, обладающий совершенным воззрением,"                     # diṭṭhisampanno puggalo [new]
PJ = "обычный человек"                                                 # puthujjano
DUC = {"kāya": "телесным", "vacī": "речевым", "mano": "умственным"}
DUC_N = {"kāya": "телесное", "vacī": "речевое", "mano": "умственное"}
GOOD = "желанный, милый и приятный результат"                          # iṭṭho kanto manāpo vipāko [ch1, pi-5]
BAD = "нежеланный, немилый и неприятный результат"
HEAVEN = "в счастливом уделе, в небесном мире"                         # sugatiṃ saggaṃ lokaṃ [pi-4 ^4-184]
HELL = "в мире лишений, в дурном уделе, в мире падения, в аду"         # apāyaṃ duggatiṃ vinipātaṃ nirayaṃ [pi-4]
AFTER = "по этой причине, по этому условию после распада тела, после смерти появился"
TH = {   # Pāli X of "yaṃ X" -> Russian after «чтобы»
    "diṭṭhisampanno puggalo kañci saṅkhāraṃ niccato upagaccheyya":
        f"{DS} принял какой-либо формирующий фактор за постоянный",
    "puthujjano kañci saṅkhāraṃ niccato upagaccheyya": f"{PJ} принял какой-либо формирующий фактор за постоянный",
    "diṭṭhisampanno puggalo kañci saṅkhāraṃ sukhato upagaccheyya": f"{DS} принял какой-либо формирующий фактор за счастье",
    "puthujjano kañci saṅkhāraṃ sukhato upagaccheyya": f"{PJ} принял какой-либо формирующий фактор за счастье",
    "diṭṭhisampanno puggalo kañci dhammaṃ atthato upagaccheyya": f"{DS} принял какое-либо явление за самость",
    "puthujjano kañci dhammaṃ atthato upagaccheyya": f"{PJ} принял какое-либо явление за самость",
    "diṭṭhisampanno puggalo mātaraṃ jīvitā voropeyya": f"{DS} лишил жизни мать",
    "puthujjano mātaraṃ jīvitā voropeyya": f"{PJ} лишил жизни мать",
    ("diṭṭhisampanno puggalo pitaraṃ jīvitā voropeyya…pe… arahantaṃ jīvitā voropeyya…pe… paduṭṭhena cittena "
     "tathāgatassa lohitaṃ uppādeyya…pe… saṅghaṃ bhindeyya…pe… aññaṃ satthāraṃ uddiseyya…pe… aṭṭhamaṃ bhavaṃ "
     "nibbatteyya"):
        (f"{DS} лишил жизни отца… лишил жизни архата… со злым умыслом пролил кровь Татхагаты… внёс раскол в Сангху… "
         f"признал своим учителем другого… породил восьмое существование"),
    "puthujjano aṭṭhamaṃ bhavaṃ nibbatteyya": f"{PJ} породил восьмое существование",
    "ekissā lokadhātuyā dve arahanto sammāsambuddhā apubbaṃ acarimaṃ uppajjeyyuṃ":
        "в одной мировой системе одновременно появились два Достойных, Полностью Пробуждённых Будды",
    "ekissā lokadhātuyā eko arahaṃ sammāsambuddho uppajjeyya":
        "в одной мировой системе появился один Достойный, Полностью Пробуждённый Будда",
    "ekissā lokadhātuyā dve rājāno cakkavattī [cakkavatti (sī. syā.)] apubbaṃ acarimaṃ uppajjeyyuṃ":
        "в одной мировой системе одновременно появились два царя, вращающих колесо [вариант написания (Sī., Syā.): cakkavatti]",
    "ekissā lokadhātuyā eko rājā cakkavattī uppajjeyya": "в одной мировой системе появился один царь, вращающий колесо",
    "itthī arahaṃ assa sammāsambuddho": "женщина была Достойным, Полностью Пробуждённым Буддой",
    "puriso arahaṃ assa sammāsambuddho": "мужчина был Достойным, Полностью Пробуждённым Буддой",
    "itthī rājā assa cakkavattī": "женщина была царём, вращающим колесо",
    "puriso rājā assa cakkavattī": "мужчина был царём, вращающим колесо",
    "itthī sakkattaṃ kareyya, mārattaṃ kareyya, brahmattaṃ kareyya":
        "женщина заняла положение Сакки, заняла положение Мары, заняла положение Брахмы",
    "puriso sakkattaṃ kareyya, mārattaṃ kareyya, brahmattaṃ kareyya":
        "мужчина занял положение Сакки, занял положение Мары, занял положение Брахмы",
}
for _k in ("duccarit", "sucarit"):
    _adj = "дурное" if _k == "duccarit" else "хорошее"
    _adjI = "дурным" if _k == "duccarit" else "хорошим"
    for _res, _rr in (("iṭṭho kanto manāpo vipāko", GOOD), ("aniṭṭho akanto amanāpo vipāko", BAD)):
        TH[f"kāya{_k}assa {_res} nibbatteyya"] = f"{_adj} телесное поведение принесло {_rr}"
        TH[f"vacī{_k}assa…pe… yaṃ mano{_k}assa {_res} nibbatteyya"] = (
            f"{_adj} речевое поведение… чтобы {_adj} умственное поведение принесло {_rr}")
    for _dest, _rd in (("sugatiṃ saggaṃ lokaṃ", HEAVEN), ("apāyaṃ duggatiṃ vinipātaṃ nirayaṃ", HELL)):
        TH[f"kāya{_k}asamaṅgī tannidānaṃ tappaccayā kāyassa bhedā paraṃ maraṇā {_dest} upapajjeyya"] = (
            f"тот, кто обладает {_adjI} телесным поведением, {AFTER} {_rd}")
        TH[f"vacī{_k}asamaṅgī…pe… yaṃ mano{_k}asamaṅgī tannidānaṃ tappaccayā kāyassa bhedā paraṃ maraṇā {_dest} "
           f"upapajjeyya"] = (f"тот, кто обладает {_adjI} речевым поведением… чтобы тот, кто обладает {_adjI} умственным "
                              f"поведением, {AFTER} {_rd}")
in_pi1("дурного телесного поведения")
TH_A = re.compile(r'^"?Aṭṭhānametaṃ anavakāso yaṃ (.+), netaṃ ṭhānaṃ vijjatī"ti pajānāti\.$')
TH_P = re.compile(r'^"Ṭhānañca kho etaṃ vijjati yaṃ (.+), ṭhānametaṃ vijjatī"ti pajānāti\.$')


def th_sent(s, first=False):
    m = TH_A.match(s)
    if m:
        r = f"«Невозможно и исключено, чтобы {TH[m.group(1)]}, такой возможности нет»"
    else:
        m = TH_P.match(s)
        r = f"«Но возможно, чтобы {TH[m.group(1)]}, такая возможность есть»"
    return ("Вот Татхагата понимает: " if first else "Понимает: ") + r + "."


# ---- kammasamādāna (^2-810)
KS_AREA = {"gati": "в уделе", "upadhi": "в облике", "kāla": "во времени", "payoga": "в усилии"}
KS_KIND = {"pāpakāni": "дурные", "kalyāṇāni": "хорошие"}


def ks_sent(s):
    m = re.match(r"^(\")?[Aa]tthekaccāni (pāpakāni|kalyāṇāni) kammasamādānāni (gati|upadhi|kāla|payoga)"
                 r"(sampatti|vipatti)(paṭibāḷhāni na vipaccanti|ṃ āgamma vipaccant[iī])(\"ti)?\.$", s)
    oq, kind, area, sv, how, cq = m.groups()
    return ("«" if oq else "") + ks_core(kind, area, sv, how) + ("»" if cq else "") + "."


def ks_core(kind, area, sv, how):
    good = "благополучием" if sv == "sampatti" else "неблагополучием"
    goodg = "благополучия" if sv == "sampatti" else "неблагополучия"
    if how.startswith("paṭi"):
        tail = f"которые, будучи подавлены {good} {KS_AREA[area]}, не приносят результата"
    else:
        tail = f"которые приносят результат вследствие {goodg} {KS_AREA[area]}"
    return f"Есть некоторые {KS_KIND[kind]} совершаемые действия, {tail}"


# ---- adhimutti (^2-813, ^2-818)
HINA = "существа с низшими устремлениями"
PANITA = "существа с высшими устремлениями"
SEV = {"present": "общаются, водят дружбу и сближаются", "past": "общались, водили дружбу и сближались",
       "future": "будут общаться, водить дружбу и сближаться"}


def sev(t, cap_=True):
    a = f"{HINA} {SEV[t]} с существами с низшими устремлениями"
    b = f"{PANITA} {SEV[t]} с существами с высшими устремлениями"
    return (cap(a) if cap_ else a), b


SANTI = f"есть {HINA}, есть {PANITA}"

# ---- the ten defilements / five faculties (^2-819 …)
KILESA10 = ("жадность, злоба, заблуждение, самомнение, воззрение, колебание, вялость, беспокойство, бессовестность и "
            "отсутствие страха перед дурным")
PRACT = "практикуются, развиты, многократно повторяются и стали преобладающими"      # āsevita … ussadagata [ch7 words]
NPRACT = "не практикуются, не развиты, не повторяются многократно и не стали преобладающими"
IND5 = "способность веры, способность усердия, способность осознанности, способность сосредоточения и способность мудрости"
in_pi1("способность веры", "способность осознанности", "способность сосредоточения", "способность мудрости")
MAHARAJA = "с большой пылью в глазах"     # pi-5 ^5 (MN 1.283)
APPARAJA = "с малой пылью в глазах"
TIKKHA = "с острыми способностями"
MUDU = "со слабыми способностями"
SVA = "с хорошими качествами"
DVA = "с плохими качествами"
SUVI = "легко обучаемые"
DUVI = "трудно обучаемые"

SENT = {}


def put(p, r):
    assert p not in SENT or SENT[p] == r, p
    SENT[p] = r


# ---- tika (1)-(4) unique sentences
put("Yogavihitesu vā kammāyatanesu yogavihitesu vā sippāyatanesu yogavihitesu vā vijjāṭṭhānesu kammassakataṃ vā "
    "saccānulomikaṃ vā rūpaṃ aniccanti vā vedanā…pe… saññā… saṅkhārā… viññāṇaṃ aniccanti vā, yaṃ evarūpiṃ anulomikaṃ "
    "khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ dhammanijjhānakkhantiṃ parato assutvā paṭilabhati – ayaṃ vuccati "
    "\"cintāmayā paññā\".",
    f"То, что человек {SKILL_FIELDS}, не услышав от другого, обретает такое {KHANTI}, будь то о собственности действий, "
    f"или согласующееся с истинами, или что материальная форма непостоянна, {FIVE_AGG_IMP}, {DASH} "
    f"{called(PN['cintāmayā'][1])}.")
put("Yogavihitesu vā kammāyatanesu yogavihitesu vā sippāyatanesu yogavihitesu vā vijjāṭṭhānesu kammassakataṃ vā "
    "saccānulomikaṃ vā rūpaṃ aniccanti vā vedanā…pe… saññā… saṅkhārā… viññāṇaṃ aniccanti vā, yaṃ evarūpiṃ anulomikaṃ "
    "khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ dhammanijjhānakkhantiṃ parato sutvā paṭilabhati – ayaṃ vuccati "
    "\"sutamayā paññā\".",
    f"То, что человек {SKILL_FIELDS}, услышав от другого, обретает такое {KHANTI}, будь то о собственности действий, "
    f"или согласующееся с истинами, или что материальная форма непостоянна, {FIVE_AGG_IMP}, {DASH} "
    f"{called(PN['sutamayā'][1])}.")
put("sabbāpi samāpannassa paññā bhāvanāmayā paññā.",
    f"вся мудрость того, кто вошёл в медитативное достижение, является {PN['bhāvanāmayā'][1]}.")
_MANAS = "Когда уделяешь внимание этим явлениям"
put('"Ime dhamme manasikaroto anuppannā ceva akusalā dhammā na uppajjanti, uppannā ca akusalā dhammā pahīyanti.',
    f"«{_MANAS}, невозникшие неблагие явления не возникают, а возникшие неблагие явления устраняются.")
put('Ime vā panime dhamme manasikaroto anuppannā ceva kusalā dhammā uppajjanti, uppannā ca kusalā dhammā '
    'bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā saṃvattantī"ti – yā tattha paññā pajānanā…pe… amoho dhammavicayo '
    'sammādiṭṭhi – idaṃ vuccati "āyakosallaṃ".',
    f"Или же, когда уделяешь внимание этим явлениям, невозникшие благие явления возникают, а возникшие благие явления "
    f"{SAMP_TO}» {DASH} {TALA}, {DASH} {called(NANA['āyakosallaṃ'][1])}.")
put('"Ime dhamme manasikaroto anuppannā ceva kusalā dhammā na uppajjanti, uppannā ca kusalā dhammā nirujjhanti.',
    f"«{_MANAS}, невозникшие благие явления не возникают, а возникшие благие явления прекращаются.")
put('Ime vā panime dhamme manasikaroto anuppannā ceva akusalā dhammā uppajjanti, uppannā ca akusalā dhammā '
    'bhiyyobhāvāya vepullāya saṃvattantī"ti – yā tattha paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – idaṃ '
    'vuccati "apāyakosallaṃ".',
    f"Или же, когда уделяешь внимание этим явлениям, невозникшие неблагие явления возникают, а возникшие неблагие "
    f"явления ведут к умножению, обширности» {DASH} {TALA}, {DASH} {called(NANA['apāyakosallaṃ'][1])}.")
put('Catūsu maggesu catūsu phalesu paññā – ayaṃ vuccati "adhipaññāya paññā".',
    f"Мудрость в четырёх путях и четырёх плодах {DASH} {called(PN['adhipaññāya'][1])}.")
put("sabbāpi tatrupāyā paññā upāyakosallaṃ.", "вся мудрость о средствах в этом является искусностью в средствах.")

# ---- tika (14), (15), (17)
put("Catūsu bhūmīsu vipāke paññā siyā uppannā, siyā uppādinī, na vattabbā anuppannāti.",
    f"Мудрость {LOCS['catūsu bhūmīsu vipāke']} иногда является возникшей, иногда является такой, которой предстоит "
    f"возникнуть, её нельзя определить как невозникшую.")
put("Catūsu bhūmīsu kusale tīsu bhūmīsu kiriyābyākate paññā siyā uppannā, siyā anuppannā, na vattabbā uppādinīti.",
    f"Мудрость {LOCS['catūsu bhūmīsu kusale']} и {LOCS['tīsu bhūmīsu kiriyābyākate']} иногда является возникшей, "
    f"иногда является невозникшей, её нельзя определить как такую, которой предстоит возникнуть.")
put("Sabbāva paññā siyā atītā, siyā anāgatā, siyā paccuppannā.",
    "Всякая мудрость иногда является прошлой, иногда является будущей, иногда является настоящей.")
put("Sabbāva paññā siyā ajjhattā, siyā bahiddhā, siyā ajjhattabahiddhā.",
    "Всякая мудрость иногда является внутренней, иногда является внешней, иногда является внутренней и внешней.")
put("Sabbāva paññā kenaci viññeyyā, kenaci na viññeyyā.",
    f"Всякая мудрость {T.ITEMS2['kenaci']['s']}, {T.ITEMS2['kenaci_na']['s']}.")
put("catūsu maggesu paññā maggahetukā paññā.", f"мудрость в четырёх путях является {pn('maggahetukā')[1]}.")

# ---- duka (35)
put("Catūsu bhūmīsu kusale arahato abhiññaṃ uppādentassa samāpattiṃ uppādentassa kiriyābyākate paññā atthajāpikā "
    "paññā, catūsu bhūmīsu vipāke arahato uppannāya abhiññāya uppannāya samāpattiyā kiriyābyākate paññā jāpitatthā paññā.",
    f"Мудрость {LOCS['catūsu bhūmīsu kusale']} и в функциональном этически неопределённом у архата, который порождает "
    f"высшее знание, порождает медитативное достижение, является {PN['atthajāpikā'][1]}; мудрость "
    f"{LOCS['catūsu bhūmīsu vipāke']} и в функциональном этически неопределённом у архата, когда высшее знание возникло, "
    f"когда медитативное достижение возникло, является {PN['jāpitatthā'][1]}.")
# duka (28)-(30)
_K = lambda p: pn(p)[0]
put("Kāmāvacarakusalābyākate paññā kāmāvacarā paññā, rūpāvacarā paññā arūpāvacarā paññā, apariyāpannā paññā na "
    "kāmāvacarā paññā.",
    f"Мудрость {LOCS['kāmāvacarakusalābyākate']}, является {pn('kāmāvacarā')[1]}; {_K('rūpāvacarā')}, "
    f"{_K('arūpāvacarā')}, и {_K('apariyāpannā')}, являются {pn('na kāmāvacarā')[1]}.")
put("Rūpāvacarakusalābyākate paññā rūpāvacarā paññā, kāmāvacarā paññā arūpāvacarā paññā apariyāpannā paññā na "
    "rūpāvacarā paññā.",
    f"Мудрость {LOCS['rūpāvacarakusalābyākate']}, является {pn('rūpāvacarā')[1]}; {_K('kāmāvacarā')}, "
    f"{_K('arūpāvacarā')}, и {_K('apariyāpannā')}, являются {pn('na rūpāvacarā')[1]}.")
put("Arūpāvacarakusalābyākate paññā arūpāvacarā paññā, kāmāvacarā paññā rūpāvacarā paññā apariyāpannā paññā na "
    "arūpāvacarā paññā.",
    f"Мудрость {LOCS['arūpāvacarakusalābyākate']}, является {pn('arūpāvacarā')[1]}; {_K('kāmāvacarā')}, "
    f"{_K('rūpāvacarā')}, и {_K('apariyāpannā')}, являются {pn('na arūpāvacarā')[1]}.")

# ---- catukka
put('"Atthi dinnaṃ, atthi yiṭṭhaṃ, atthi hutaṃ, atthi sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko, atthi ayaṃ loko, atthi '
    'paro loko, atthi mātā, atthi pitā, atthi sattā opapātikā, atthi loke samaṇabrāhmaṇā sammaggatā sammāpaṭipannā ye '
    'imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentī"ti – yā evarūpā paññā pajānanā…pe… amoho '
    'dhammavicayo sammādiṭṭhi – idaṃ vuccati "kammassakatañāṇaṃ".',
    f"«{ATTHI_DINNAM}» {DASH} {EVARUPA}, {DASH} {called(NANA['kammassakatañāṇaṃ'][1])}.")
put("Ṭhapetvā saccānulomikaṃ ñāṇaṃ, sabbāpi sāsavā kusalā paññā kammassakatañāṇaṃ.",
    f"За исключением знания, согласующегося с истинами, вся благая мудрость, подверженная влечениям, является "
    f"{NANA['kammassakatañāṇaṃ'][1]}.")
put('"Rūpaṃ anicca"nti vā vedanā…pe… saññā… saṅkhārā… "viññāṇaṃ anicca"nti vā yā evarūpī anulomikā khanti diṭṭhi ruci '
    'mudi pekkhā dhammanijjhānakkhanti – idaṃ vuccati "saccānulomikaṃ ñāṇaṃ".',
    f"То, что есть такое {KHANTI}, как «Материальная форма непостоянна», или чувство… восприятие… формирующие "
    f"факторы… «Сознание непостоянно», {DASH} {called(NANA['saccānulomikaṃ ñāṇaṃ'][1])}.")
put("catūsu maggesu paññā maggasamaṅgissa ñāṇaṃ.", f"мудрость в четырёх путях является {NANA['maggasamaṅgissa ñāṇaṃ'][1]}.")
put("catūsu phalesu paññā phalasamaṅgissa ñāṇaṃ.", f"мудрость в четырёх плодах является {NANA['phalasamaṅgissa ñāṇaṃ'][1]}.")
put("Catūsu maggesu catūsu phalesu paññā dhamme ñāṇaṃ.",
    f"Мудрость в четырёх путях и четырёх плодах является {NANA['dhamme ñāṇaṃ'][1]}.")
put("so iminā dhammena ñātena diṭṭhena pattena viditena pariyogāḷhena atītānāgatena nayaṃ neti.",
    "он с помощью этого Учения, познанного, увиденного, достигнутого, узнанного, глубоко постигнутого, делает вывод о "
    "прошлом и будущем.")
_T4 = ["страдание", "возникновение страдания", "прекращение страдания", "способ практики, ведущий к прекращению страдания"]
_THIS = ["это страдание", "это возникновение страдания", "это прекращение страдания",
         "этот способ практики, ведущий к прекращению страдания"]


def _anvaya(past):
    v = "постигли" if past else "постигнут"
    when = "в прошлом" if past else "в будущем"
    var = " [вариант написания (Syā.): abbhaññiṃsu; так же и далее]" if past else ""
    first = ", ".join([f"{v} {_T4[0]}{var}"] + [f"{v} {x}" for x in _T4[1:]])
    second = "они " + ", ".join(f"{v} именно {x}" for x in _THIS)
    return f"Все отшельники или брахманы, которые {when} {first}, {second}"


put('"Ye hi keci atītamaddhānaṃ samaṇā vā brāhmaṇā vā dukkhaṃ abbhaññaṃsu [abbhaññiṃsu (syā.) evamuparipi], '
    'dukkhasamudayaṃ abbhaññaṃsu, dukkhanirodhaṃ abbhaññaṃsu, dukkhanirodhagāminiṃ paṭipadaṃ abbhaññaṃsu, imaññeva te '
    'dukkhaṃ abbhaññaṃsu, imaññeva te dukkhasamudayaṃ abbhaññaṃsu, imaññeva te dukkhanirodhaṃ abbhaññaṃsu, imaññeva te '
    'dukkhanirodhagāminiṃ paṭipadaṃ abbhaññaṃsu.',
    "«" + _anvaya(True) + ".")
put('Ye hi keci anāgatamaddhānaṃ samaṇā vā brāhmaṇā vā dukkhaṃ abhijānissanti, dukkhasamudayaṃ abhijānissanti, '
    'dukkhanirodhaṃ abhijānissanti, dukkhanirodhagāminiṃ paṭipadaṃ abhijānissanti, imaññeva te dukkhaṃ abhijānissanti, '
    'imaññeva te dukkhasamudayaṃ abhijānissanti, imaññeva te dukkhanirodhaṃ abhijānissanti, imaññeva te '
    'dukkhanirodhagāminiṃ paṭipadaṃ abhijānissantī"ti – yā tattha paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – '
    'idaṃ vuccati "anvaye ñāṇaṃ".',
    _anvaya(False) + f"» {DASH} {TALA}, {DASH} {called(NANA['anvaye ñāṇaṃ'][1])}.")
put("Idha bhikkhu parasattānaṃ parapuggalānaṃ cetasā ceto paricca pajānāti.",
    f"Вот монах, охватив своим умом умы {OTHERS}, понимает их.")
_cs = [f"когда ум {pr}, понимает: «Ум {pr}»" for st, pr in CITTA_STATES]   # ch7 (ajjhattabahiddhā form)
_cp = ", ".join(f'{st}aṃ vā cittaṃ "{st}aṃ citta"nti pajānāti' for st, pr in CITTA_STATES)
put(cap(_cp)[:-1] + 'īti – yā tattha paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – idaṃ vuccati "pariye ñāṇaṃ".',
    cap("; ".join(_cs)) + f" {DASH} {TALA}, {DASH} {called(NANA['pariye ñāṇaṃ'][1])}.")
put("ṭhapetvā dhamme ñāṇaṃ anvaye ñāṇaṃ pariye ñāṇaṃ, avasesā paññā sammutiñāṇaṃ.",
    f"за исключением знания Учения, знания по выводу и знания охвата умов, остальная мудрость является "
    f"{NANA['sammutiñāṇaṃ'][1]}.")
for _k in ("ācayāya no apacayāya", "apacayāya no ācayāya", "ācayāya ceva apacayāya ca", "neva ācayāya no apacayāya",
           "nibbidāya ceva paṭivedhāya ca", "neva nibbidāya no paṭivedhāya"):
    for _loc, _rl in (("Kāmāvacarakusale paññā", f"Мудрость {LOCS['kāmāvacarakusale']}"),
                      ("catūsu maggesu paññā", "мудрость в четырёх путях"),
                      ("rūpāvacarārūpāvacarakusale paññā", f"мудрость {LOCS['rūpāvacarārūpāvacarakusale']}"),
                      ("avasesā paññā", "остальная мудрость")):
        put(f"{_loc} {_k}.", f"{closing(_rl)} {ACAYA_V[_k]}.")
put('Yāya paññāya kāmesu vītarāgo hoti, na ca abhiññāyo paṭivijjhati na ca saccāni – ayaṃ vuccati "paññā nibbidāya no '
    'paṭivedhāya".',
    f"Мудрость, благодаря которой человек свободен от страсти к чувственным удовольствиям, но не проникает ни в высшие "
    f"знания, ни в истины, {DASH} {called(term_ins('paññā nibbidāya no paṭivedhāya'))}.")
put('sveva paññāya kāmesu vītarāgo samāno abhiññāyo paṭivijjhati na ca saccāni – ayaṃ vuccati "paññā paṭivedhāya no '
    'nibbidāya".',
    f"тот же человек, будучи благодаря мудрости свободен от страсти к чувственным удовольствиям, проникает в высшие "
    f"знания, но не в истины, {DASH} {called(term_ins('paññā paṭivedhāya no nibbidāya'))}.")

# hāna / ṭhiti / visesa / nibbedha (^2-799)
SAHA = {"kāma": "чувственными желаниями", "vitakka": "направленной мыслью", "avitakka": "отсутствием направленной мысли",
        "upekkhā": "невозмутимостью", "pītisukha": "восторгом и счастьем",
        "adukkhamasukha": "тем, что ни болезненно, ни приятно", "rūpa": "материальной формой",
        "ākāsānañcāyatana": "сферой бесконечного пространства", "viññāṇañcāyatana": "сферой бесконечного сознания",
        "ākiñcaññāyatana": "сферой отсутствия чего-либо",
        "nevasaññānāsaññāyatana": "сферой ни восприятия, ни невосприятия", "nibbidā": "разочарованием"}
LABHI = {"Paṭhamassa jhānassa": "первое медитативное погружение", "Dutiyassa jhānassa": "второе медитативное погружение",
         "Tatiyassa jhānassa": "третье медитативное погружение", "Catutthassa jhānassa": "четвёртое медитативное погружение",
         "Ākāsānañcāyatanassa": "сферу бесконечного пространства", "Viññāṇañcāyatanassa": "сферу бесконечного сознания",
         "Ākiñcaññāyatanassa": "сферу отсутствия чего-либо"}
SM = "восприятия и внимание"                                                  # saññāmanasikārā


def hana_sent(s):
    m = re.match(r"^(\S+ \S+|\S+) lābhiṃ (\S+)sahagatā saññāmanasikārā samudācaranti hānabhāginī paññā\.$", s)
    if m:
        return (f"Когда у того, кто обрёл {LABHI[m.group(1)]}, проявляются {SM}, сопровождаемые {SAHA[m.group(2)]}, "
                f"это {PN['hānabhāginī'][0]}.")
    if re.match(r"^[Tt]adanudhammatā sati santiṭṭhati ṭhitibhāginī paññā\.$", s):
        r = f"когда осознанность, соответствующая этому, устойчива, это {PN['ṭhitibhāginī'][0]}."
        return cap(r) if s[0] == "T" else r
    m = re.match(r"^(\S+)sahagatā saññāmanasikārā samudācaranti visesabhāginī paññā\.$", s)
    if m:
        r = f"когда проявляются {SM}, сопровождаемые {SAHA[low1(m.group(1))]}, это {PN['visesabhāginī'][0]}."
        return cap(r) if s[0].isupper() else r
    m = re.match(r"^(\S+)sahagatā saññāmanasikārā samudācaranti virāgūpasañhitā nibbedhabhāginī paññā\.$", s)
    if m:
        r = (f"когда проявляются {SM}, сопровождаемые {SAHA[low1(m.group(1))]} и связанные с бесстрастием, это "
             f"{PN['nibbedhabhāginī'][0]}.")
        return cap(r) if s[0].isupper() else r
    return None


# paṭisambhidā (^2-800): ch15 strings
put("Atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā.",
    T.enum([cap(Y.PS["attha"][0])] + [Y.PS[k][0] for k in ("dhamma", "nirutti", "paṭibhāna")]) + ".")
put("Atthe ñāṇaṃ atthapaṭisambhidā, dhamme ñāṇaṃ dhammapaṭisambhidā, tatra dhammaniruttābhilāpe ñāṇaṃ "
    "niruttipaṭisambhidā, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā.",
    Y.ps_clauses("Atthe ñāṇaṃ atthapaṭisambhidā, dhamme ñāṇaṃ dhammapaṭisambhidā, tatra dhammaniruttābhilāpe ñāṇaṃ "
                 "niruttipaṭisambhidā, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā") + ".")
put("Imā catasso paṭisambhidā.", "Это четыре аналитических знания.")
put("Dukkhapaṭipadā dandhābhiññā paññā, dukkhapaṭipadā khippābhiññā paññā, sukhapaṭipadā dandhābhiññā paññā, "
    "sukhapaṭipadā khippābhiññā paññā.",
    list_nom([pn(f"{a} {b}")[0] for a in ("dukkhapaṭipadā", "sukhapaṭipadā") for b in ("dandhābhiññā", "khippābhiññā")]) + ".")
put("Imā catasso paṭipadā.", "Это четыре способа практики.")
put("Parittā parittārammaṇā paññā, parittā appamāṇārammaṇā paññā, appamāṇā parittārammaṇā paññā, appamāṇā "
    "appamāṇārammaṇā paññā.",
    list_nom([pn(f"{a} {b}")[0] for a in ("parittā", "appamāṇā") for b in ("parittārammaṇā", "appamāṇārammaṇā")]) + ".")
put("Imāni cattāri ārammaṇāni.", "Это четыре объекта.")


def is_also(s):
    """'Maggasamaṅgissa ñāṇaṃ dukkhepetaṃ ñāṇaṃ, … paṭipadāyapetaṃ ñāṇaṃ.' (also the …pe… form)"""
    m = re.match(r"^(Magga|Dhamma)samaṅgissa ñāṇaṃ (.+)\.$", s)
    if not m:
        return None
    subj = "Знание обладающего путём" if m.group(1) == "Magga" else "Знание обладающего Учением"
    out = []
    for chunk in re.split(r", ", m.group(2)):
        bits = chunk.split("…pe… ")
        rr = []
        for bt in bits:
            mm = re.match(r"^(.+?)petaṃ ñāṇaṃ$", bt)          # dukkhepetaṃ = dukkhe + (api) etaṃ
            rr.append(f"и знанием {GENL[mm.group(1)]}")
        out.append("… ".join(rr))
    return f"{subj} является " + ", ".join(out) + "."


# pañcaka
PHARANA = ["наполненность восторгом", "наполненность счастьем", "наполненность умом", "наполненность светом",
           "признак рассмотрения"]                                       # pharaṇatā, paccavekkhaṇānimitta [new]
put("Pītipharaṇatā, sukhapharaṇatā, cetopharaṇatā, ālokapharaṇatā, paccavekkhaṇānimittaṃ.", cap(T.enum(PHARANA)) + ".")
put("Dvīsu jhānesu paññā pītipharaṇatā.", "Мудрость в двух медитативных погружениях является наполненностью восторгом.")
put("Tīsu jhānesu paññā sukhapharaṇatā.", "Мудрость в трёх медитативных погружениях является наполненностью счастьем.")
put("Paracitte ñāṇaṃ cetopharaṇatā.", "Знание ума другого является наполненностью умом.")
put("Dibbacakkhu ālokapharaṇatā.", "Божественный глаз является наполненностью светом.")
put("Tamhā tamhā samādhimhā vuṭṭhitassa paccavekkhaṇāñāṇaṃ paccavekkhaṇānimittaṃ.",
    "Знание рассмотрения у того, кто вышел из того или иного сосредоточения, является признаком рассмотрения.")
put("Ayaṃ vuccati pañcaṅgiko sammāsamādhi.", "Это называется пятичастным правильным сосредоточением.")
OWN = "лично у него возникает знание"                                   # paccattaññeva ñāṇaṃ uppajjati
for _p, _r in (('"Ayaṃ samādhi paccuppannasukho ceva āyatiñca sukhavipāko"ti',
                "«Это сосредоточение и приятно в настоящем, и в будущем созревает в счастье»"),
               ('"Ayaṃ samādhi ariyo nirāmiso"ti', "«Это сосредоточение благородное и неплотское»"),
               ('"Ayaṃ samādhi akāpurisasevito"ti', "«Это сосредоточение не практикуется низкими людьми»"),
               ('"Ayaṃ samādhi santo paṇīto paṭippassaddhaladdho ekodibhāvādhigato na sasaṅkhāraniggayhavāritagato"ti',
                "«Это сосредоточение спокойное, высшее, обретённое через успокоение, достигнутое через единение ума и не "
                "удерживаемое насильственным подавлением и сдерживанием»"),
               ('So kho panāhaṃ imaṃ samādhiṃ sato samāpajjāmi sato vuṭṭhahāmī"ti',
                "«И я осознанно вхожу в это сосредоточение и осознанно выхожу из него»")):
    put(f"{_p} paccattaññeva ñāṇaṃ uppajjati.", f"{cap(OWN)}: {_r}.")
put("Ayaṃ pañcañāṇiko sammāsamādhi.", f"Это {FIVE_NANA}.")

# chakka
ABHI6 = ["знание видов сверхспособностей", "знание очищения элемента уха", "знание ума другого",
         "знание припоминания прежних жизней", "знание о смерти и новом рождении существ", "знание об уничтожении влечений"]
in_pi1("элементом уха")
put("Iddhividhe ñāṇaṃ, sotadhātuvisuddhiyā ñāṇaṃ, paracitte ñāṇaṃ, pubbenivāsānussatiyā ñāṇaṃ, sattānaṃ cutūpapāte "
    "ñāṇaṃ, āsavānaṃ khaye ñāṇaṃ – imā chasu abhiññāsu paññā.",
    cap(", ".join(ABHI6)) + f" {DASH} это мудрость в шести высших знаниях.")
# sattaka
DHT = "это знание устойчивости явлений"
DECAY = "подвержено уничтожению, подвержено исчезновению, подвержено угасанию, подвержено прекращению"


def six(link, neg):
    return [f"знание того, что {link}", f"знание того, что, {neg}", f"знание того, что и в прошлом {link}",
            f"знание того, что, {neg}", f"знание того, что и в будущем {link}", f"знание того, что, {neg}"]


_s1 = six(CHAIN[-1], "когда нет рождения, нет старения и смерти")
_s2 = six(CHAIN[0], "когда нет неведения, нет формирующих факторов")
_mid = "… ".join(f"знание того, что {c}" for c in reversed(CHAIN[1:-1]))
put("Jātipaccayā jarāmaraṇanti ñāṇaṃ, asati jātiyā natthi jarāmaraṇanti ñāṇaṃ, atītampi addhānaṃ jātipaccayā "
    "jarāmaraṇanti ñāṇaṃ, asati jātiyā natthi jarāmaraṇanti ñāṇaṃ, anāgatampi addhānaṃ jātipaccayā jarāmaraṇanti "
    "ñāṇaṃ, asati jātiyā natthi jarāmaraṇanti ñāṇaṃ.", cap(", ".join(_s1)) + ".")
_mid_p = "…pe… ".join(["bhavapaccayā jātīti ñāṇaṃ", "upādānapaccayā bhavoti ñāṇaṃ", "taṇhāpaccayā upādānanti ñāṇaṃ",
                       "vedanāpaccayā taṇhāti ñāṇaṃ", "phassapaccayā vedanāti ñāṇaṃ", "saḷāyatanapaccayā phassoti ñāṇaṃ",
                       "nāmarūpapaccayā saḷāyatananti ñāṇaṃ", "viññāṇapaccayā nāmarūpanti ñāṇaṃ",
                       "saṅkhārapaccayā viññāṇanti ñāṇaṃ", "avijjāpaccayā saṅkhārāti ñāṇaṃ"])
put("Yampissa taṃ dhammaṭṭhitiñāṇaṃ tampi khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammanti ñāṇaṃ; " + _mid_p
    + ", asati avijjāya natthi saṅkhārāti ñāṇaṃ, atītampi addhānaṃ avijjāpaccayā saṅkhārāti ñāṇaṃ, asati avijjāya natthi "
    "saṅkhārāti ñāṇaṃ, anāgatampi addhānaṃ avijjāpaccayā saṅkhārāti ñāṇaṃ, asati avijjāya natthi saṅkhārāti ñāṇaṃ.",
    f"Знание того, что и {DHT} {DECAY}; {_mid}… " + ", ".join(_s2) + ".")
put("Yampissa taṃ dhammaṭṭhitiñāṇaṃ tampi khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammanti ñāṇaṃ.",
    f"Знание того, что и {DHT} {DECAY}.")
put("Imāni sattasattati ñāṇavatthūni.", f"Это семьдесят семь {NV}.")
# aṭṭhaka, navaka
put("Sotāpattimagge paññā, sotāpattiphale paññā, sakadāgāmimagge paññā, sakadāgāmiphale paññā, anāgāmimagge paññā, "
    "anāgāmiphale paññā, arahattamagge paññā, arahattaphale paññā – imā catūsu maggesu catūsu phalesu paññā.",
    cap(", ".join(f"мудрость в {x}" for x in LOKUTTARA_PATHS)) + f" {DASH} это мудрость в четырёх путях и четырёх плодах.")
put("Paṭhamajjhānasamāpattiyā paññā, dutiyajjhānasamāpattiyā paññā, tatiyajjhānasamāpattiyā paññā, "
    "catutthajjhānasamāpattiyā paññā, ākāsānañcāyatanasamāpattiyā paññā, viññāṇañcāyatanasamāpattiyā paññā, "
    "ākiñcaññāyatanasamāpattiyā paññā, nevasaññānāsaññāyatanasamāpattiyā paññā, saññāvedayitanirodhasamāpattiyā "
    "vuṭṭhitassa paccavekkhaṇāñāṇaṃ – imā navasu anupubbavihārasamāpattīsu paññā.",
    cap(", ".join(f"мудрость в достижении {x}" for x in JH))
    + f", знание рассмотрения у того, кто вышел из достижения {NIRODHA[:-len('е восприятия и ощущаемого')]}я "
      f"восприятия и ощущаемого, {DASH} это мудрость в девяти {ANUPUBBA}.")

# ---- dasaka: (2), (3), (4), (5), (6), (7), (8), (9), (10)
for _sv in ("sampatti", "vipatti"):
    pass
put('Idha tathāgato "ayaṃ maggo ayaṃ paṭipadā nirayagāmī"ti [nirayagāminīti (syā.)] pajānāti, "ayaṃ maggo ayaṃ paṭipadā '
    'tiracchānayonigāmī"ti [tiracchānagāminīti (syā.) evamuparipi. aṭṭhakathā oloketabbā] pajānāti, "ayaṃ maggo ayaṃ '
    'paṭipadā pettivisayagāmī"ti pajānāti, "ayaṃ maggo ayaṃ paṭipadā manussalokagāmī"ti pajānāti, "ayaṃ maggo ayaṃ '
    'paṭipadā devalokagāmī"ti pajānāti, "ayaṃ maggo ayaṃ paṭipadā nibbānagāmī"ti pajānātīti.',
    "Вот Татхагата понимает: «Этот путь, этот способ практики ведёт в ад» [вариант написания (Syā.): nirayagāminīti], "
    "понимает: «Этот путь, этот способ практики ведёт в мир животных» [вариант чтения (Syā.): tiracchānagāminīti; так "
    "же и далее; следует свериться с комментарием], понимает: «Этот путь, этот способ практики ведёт в мир голодных "
    "духов», понимает: «Этот путь, этот способ практики ведёт в мир людей», понимает: «Этот путь, этот способ практики "
    "ведёт в мир богов», понимает: «Этот путь, этот способ практики ведёт к нирване».")
put("Idha tathāgato khandhanānattaṃ pajānāti, āyatananānattaṃ pajānāti, dhātunānattaṃ pajānāti, "
    "anekadhātunānādhātulokanānattaṃ pajānātīti.",
    f"Вот Татхагата понимает разнообразие совокупностей, понимает разнообразие сфер восприятия, понимает разнообразие "
    f"элементов, понимает разнообразие мира со множеством элементов, с разнообразием элементов.")
_h, _p = sev("present")
put('Idha tathāgato pajānāti – "santi sattā hīnādhimuttikā, santi sattā paṇītādhimuttikā.',
    f"Вот Татхагата понимает {DASH} «{cap(SANTI)}.")
put("Hīnādhimuttikā sattā hīnādhimuttike satte sevanti bhajanti payirupāsanti.", _h + ".")
put("Paṇītādhimuttikā sattā paṇītādhimuttike satte sevanti bhajanti payirupāsanti.", cap(_p) + ".")
_h2, _p2 = sev("past", False)
put('"Atītampi addhānaṃ hīnādhimuttikā sattā hīnādhimuttike satte seviṃsu bhajiṃsu payirupāsiṃsu, paṇītādhimuttikā '
    'sattā paṇītādhimuttike satte seviṃsu bhajiṃsu payirupāsiṃsu.', f"«И в прошлом {_h2}, {_p2}.")
_h3, _p3 = sev("future", False)
put('"Anāgatampi addhānaṃ hīnādhimuttikā sattā hīnādhimuttike satte sevissanti bhajissanti payirupāsissanti, '
    'paṇītādhimuttikā sattā paṇītādhimuttike satte sevissanti bhajissanti payirupāsissantī"ti.',
    f"«И в будущем {_h3}, {_p3}».")
put("Santi sattā hīnādhimuttikā, santi sattā paṇītādhimuttikā.", f"{cap(SANTI)}.")
put("Atītampi addhānaṃ hīnādhimuttikā sattā hīnādhimuttike satte seviṃsu bhajiṃsu payirupāsiṃsu.", f"И в прошлом {_h2}.")
put("Paṇītādhimuttikā sattā paṇītādhimuttike satte seviṃsu bhajiṃsu payirupāsiṃsu.", cap(_p2) + ".")
put("Anāgatampi addhānaṃ hīnādhimuttikā sattā hīnādhimuttike satte sevissanti bhajissanti payirupāsissanti.",
    f"И в будущем {_h3}.")
put("Paṇītādhimuttikā sattā paṇītādhimuttike satte sevissanti bhajissanti payirupāsissanti.", cap(_p3) + ".")
put("Ayaṃ sattānaṃ adhimutti.", "Это устремление существ.")
put("Idha tathāgato sattānaṃ āsayaṃ pajānāti, anusayaṃ pajānāti, caritaṃ pajānāti, adhimuttiṃ pajānāti, apparajakkhe "
    "mahārajakkhe tikkhindriye mudindriye svākāre dvākāre suviññāpaye duviññāpaye bhabbābhabbe satte pajānāti.",
    f"Вот Татхагата понимает наклонность существ, понимает скрытую склонность, понимает поведение, понимает "
    f"устремление, понимает существ {APPARAJA} и {MAHARAJA}, {TIKKHA} и {MUDU}, {SVA} и {DVA}, легко обучаемых и трудно "
    f"обучаемых, способных и неспособных.")
put("Katamo ca sattānaṃ āsayo?", "А что такое наклонность существ?")
put('"Sassato loko"ti vā, "asassato loko"ti vā, "antavā loko"ti vā, "anantavā loko"ti vā, "taṃ jīvaṃ taṃ sarīra"nti '
    'vā, "aññaṃ jīvaṃ aññaṃ sarīra"nti vā, "hoti tathāgato paraṃ maraṇā"ti vā, "na hoti tathāgato paraṃ maraṇā"ti vā, '
    '"hoti ca na ca hoti tathāgato paraṃ maraṇā"ti vā, "neva hoti na na hoti tathāgato paraṃ maraṇā"ti vā, iti '
    'bhavadiṭṭhisannissitā vā sattā honti vibhavadiṭṭhisannissitā vā.',
    f"{VIEWS10}, так существа опираются либо на воззрение о существовании, либо на воззрение о несуществовании.")
put("Ete vā pana ubho ante anupagamma idappaccayatā paṭiccasamuppannesu dhammesu anulomikā khanti paṭiladdhā hoti "
    "yathābhūtaṃ ñāṇaṃ.",
    "Или же, без приближения к этим двум крайностям, обретены согласующееся принятие в отношении явлений, возникших в "
    "зависимости от условий по обусловленности этим, и знание того, как есть на самом деле.")
put("Ayaṃ sattānaṃ āsayo.", "Это наклонность существ.")
put("Katamo ca sattānaṃ anusayo?", "А что такое скрытая склонность существ?")
_AN = ["к чувственной страсти", "к неприязни", "к самомнению", "к воззрениям", "к колебанию", "к страсти к существованию",
       "к неведению"]                                                          # pi-5 ^5 parihānikathā
put("Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, bhavarāgānusayo, "
    "avijjānusayo.",
    f"Семь скрытых склонностей {DASH} " + T.enum([f"скрытая склонность {x}" for x in _AN]) + ".")
put("Yaṃ loke piyarūpaṃ sātarūpaṃ ettha sattānaṃ rāgānusayo anuseti.",
    "Что в мире привлекательно и отрадно, в том у существ лежит скрытая склонность к страсти.")
put("Yaṃ loke appiyarūpaṃ asātarūpaṃ ettha sattānaṃ paṭighānusayo anuseti.",
    "Что в мире непривлекательно и неотрадно, в том у существ лежит скрытая склонность к неприязни.")
put("Iti imesu dvīsu dhammesu avijjānupatitā.", "Так этим двум явлениям сопутствует неведение.")
put("Tadekaṭṭho māno ca diṭṭhi ca vicikicchā ca daṭṭhabbā.",
    "Следует рассматривать самомнение, воззрение и колебание как пребывающие вместе с ним.")
put("Ayaṃ sattānaṃ anusayo.", "Это скрытая склонность существ.")
put("Katamañca sattānaṃ caritaṃ?", "А что такое поведение существ?")
_CH6 = open(os.path.join(S.RU_DIR, "6-paticcasamuppadavibhango.md"), encoding="utf-8").read()
_ABHIS = ("Волевое действие, приносящее заслугу, волевое действие, не приносящее заслуги, волевое действие, ведущее к "
          "непоколебимому")
assert _ABHIS in _CH6
put("Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro, parittabhūmako vā mahābhūmako vā – idaṃ sattānaṃ caritaṃ.",
    f"{_ABHIS}, ограниченного уровня или обширного уровня, {DASH} это поведение существ.")
put("Katamā ca sattānaṃ adhimutti?", "А что такое устремление существ?")
put("Katame te sattā mahārajakkhā?", f"Какие существа {MAHARAJA}?")
put("Dasa kilesavatthūni – lobho, doso, moho, māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirikaṃ, anottappaṃ.",
    f"Десять основ омрачений {DASH} {KILESA10}.")
put("Yesaṃ sattānaṃ imāni dasa kilesavatthūni āsevitāni bhāvitāni bahulīkatāni ussadagatāni, ime te sattā "
    "mahārajakkhā.",
    f"Существа, у которых эти десять основ омрачений {PRACT}, являются существами {MAHARAJA}.")
put("Katame te sattā apparajakkhā?", f"Какие существа {APPARAJA}?")
put("Yesaṃ sattānaṃ imāni dasa kilesavatthūni anāsevitāni abhāvitāni abahulīkatāni anussadagatāni, ime te sattā "
    "apparajakkhā.",
    f"Существа, у которых эти десять основ омрачений {NPRACT}, являются существами {APPARAJA}.")
put("Katame te sattā mudindriyā?", f"Какие существа {MUDU}?")
put("Pañcindriyāni – saddhindriyaṃ, vīriyindriyaṃ, satindriyaṃ, samādhindriyaṃ, paññindriyaṃ.",
    f"Пять способностей {DASH} {IND5}.")
put("Yesaṃ sattānaṃ imāni pañcindriyāni anāsevitāni abhāvitāni abahulīkatāni anussadagatāni, ime te sattā mudindriyā.",
    f"Существа, у которых эти пять способностей {NPRACT}, являются существами {MUDU}.")
put("Katame te sattā tikkhindriyā?", f"Какие существа {TIKKHA}?")
put("Yesaṃ sattānaṃ imāni pañcindriyāni āsevitāni bhāvitāni bahulīkatāni ussadagatāni, ime te sattā tikkhindriyā.",
    f"Существа, у которых эти пять способностей {PRACT}, являются существами {TIKKHA}.")
put("Katame te sattā dvākārā?", f"Какие существа {DVA}?")
put("Ye te sattā pāpāsayā pāpānusayā pāpacaritā pāpādhimuttikā mahārajakkhā mudindriyā, ime te sattā dvākārā.",
    f"Существа с дурными наклонностями, с дурными скрытыми склонностями, с дурным поведением, с дурными устремлениями, "
    f"{MAHARAJA}, {MUDU} являются существами {DVA}.")
put("Katame te sattā svākārā?", f"Какие существа {SVA}?")
put("Ye te sattā kalyāṇāsayā kalyāṇacaritā kalyāṇādhimuttikā apparajakkhā tikkhindriyā, ime te sattā svākārā.",
    f"Существа с хорошими наклонностями, с хорошим поведением, с хорошими устремлениями, {APPARAJA}, {TIKKHA} "
    f"являются существами {SVA}.")
put("Katame te sattā duviññāpayā?", "Какие существа трудно обучаемы?")
put("Ye ca te sattā dvākārā, teva te sattā duviññāpayā.", f"Существа {DVA} и являются трудно обучаемыми существами.")
put("Ye ca te sattā svākārā, teva te sattā suviññāpayā.", f"Существа {SVA} и являются легко обучаемыми существами.")
put("Katame te sattā abhabbā?", "Какие существа неспособны?")
_AV = ("наделены препятствием в виде действий, наделены препятствием в виде омрачений, наделены препятствием в виде "
       "результатов действий")                                                         # pi-4 ^4-12 (pi-1 kamma, vipāka)
_NAV = ("не наделены препятствием в виде действий, не наделены препятствием в виде омрачений, не наделены препятствием "
        "в виде результатов действий")
_WAY = "вступить на предопределённый путь правильности в благих явлениях"              # pi-4 ^4-12
put("Ye te sattā kammāvaraṇena samannāgatā kilesāvaraṇena samannāgatā vipākāvaraṇena samannāgatā assaddhā acchandikā "
    "duppaññā abhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ, ime te sattā abhabbā.",
    f"Существа, которые {_AV}, лишены веры, лишены стремления, лишены мудрости и не способны {_WAY}, являются "
    f"неспособными существами.")
put("Katame te sattā bhabbā?", "Какие существа способны?")
put("Ye te sattā na kammāvaraṇena samannāgatā na kilesāvaraṇena samannāgatā na vipākāvaraṇena samannāgatā saddhā "
    "chandikā paññavanto bhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ, ime te sattā bhabbāti.",
    f"Существа, которые {_NAV}, обладают верой, обладают стремлением, мудры и способны {_WAY}, являются способными "
    f"существами.")
# (7)
put("Jhāyīti.", "«Медитирующий».")
put("Cattāro jhāyī.", "Четверо медитирующих.")
put("Aparepi cattāro jhāyī.", "Есть и другие четверо медитирующих.")
_SUCC = "то, что на самом деле является успехом"
_FAIL = "то, что на самом деле является неудачей"
put("Atthekacco jhāyī sampattiyeva [sampattiyeva (ka.)] samānaṃ vipattīti pacceti, atthekacco jhāyī vipattiṃyeva "
    "[vipattiyeva (ka.)] samānaṃ sampattīti pacceti, atthekacco jhāyī sampattiyeva samānaṃ sampattīti pacceti, "
    "atthekacco jhāyī vipattiyeva samānaṃ vipattīti pacceti – ime cattāro jhāyī.",
    f"Есть медитирующий, который {_SUCC} [вариант написания (Ka.): sampattiyeva], считает неудачей, есть медитирующий, "
    f"который {_FAIL} [вариант написания (Ka.): vipattiyeva], считает успехом, есть медитирующий, который {_SUCC}, "
    f"считает успехом, есть медитирующий, который {_FAIL}, считает неудачей {DASH} это четверо медитирующих.")
_IN, _OUT = "входит в погружение", "выходит из него"
put("Atthekacco jhāyī dandhaṃ samāpajjati khippaṃ vuṭṭhāti, atthekacco jhāyī khippaṃ samāpajjati dandhaṃ vuṭṭhāti, "
    "atthekacco jhāyī dandhaṃ samāpajjati dandhaṃ vuṭṭhāti, atthekacco jhāyī khippaṃ samāpajjati khippaṃ vuṭṭhāti – ime "
    "cattāro jhāyī.",
    ", ".join(f"{'Есть' if i == 0 else 'есть'} медитирующий, который {a} {_IN} и {b} {_OUT}"
              for i, (a, b) in enumerate((("медленно", "быстро"), ("быстро", "медленно"), ("медленно", "медленно"),
                                          ("быстро", "быстро")))) + f" {DASH} это четверо медитирующих.")
_S, _A = "искусен в сосредоточении в отношении сосредоточения", "искусен в достижении в отношении сосредоточения"
put("Atthekacco jhāyī samādhismiṃ samādhikusalo hoti, na samādhismiṃ samāpattikusalo; atthekacco jhāyī samādhismiṃ "
    "samāpattikusalo hoti, na samādhismiṃ samādhikusalo; atthekacco jhāyī samādhismiṃ samādhikusalo ca hoti, samādhismiṃ "
    "samāpattikusalo ca; atthekacco jhāyī neva samādhismiṃ samādhikusalo hoti, na samādhismiṃ samāpattikusalo – ime "
    "cattāro jhāyī.",
    f"Есть медитирующий, который {_S}, но не {_A}; есть медитирующий, который {_A}, но не {_S}; есть медитирующий, "
    f"который и {_S}, и {_A}; есть медитирующий, который ни {_S}, ни {_A} {DASH} это четверо медитирующих."
    .replace("который ни искусен", "который не искусен ни").replace(", ни искусен в достижении", ", ни в достижении"))
put('"Jhāna"nti.', "«Медитативное погружение».")
put("Cattāri jhānāni – paṭhamaṃ jhānaṃ, dutiyaṃ jhānaṃ, tatiyaṃ jhānaṃ, catutthaṃ jhānaṃ.",
    f"Четыре медитативных погружения {DASH} " + T.enum([f"{x} медитативное погружение" for x in
                                                         ("первое", "второе", "третье", "четвёртое")]) + ".")
put('"Vimokkho"ti.', "«Освобождение».")
put("Aṭṭha vimokkhā.", "Восемь освобождений.")
put("Rūpī rūpāni passati – ayaṃ paṭhamo vimokkho.",
    f"Обладая материальной формой, видит видимые формы {DASH} это первое освобождение.")
in_pi1("обладая материальной формой, видит видимые формы")
put("Ajjhattaṃ arūpasaññī bahiddhā rūpāni passati – ayaṃ dutiyo vimokkho.",
    f"Не воспринимая материальную форму внутри себя, видит видимые формы вовне {DASH} это второе освобождение.")
in_pi1("не воспринимая материальную форму внутри себя, видит вовне")
put("Subhanteva adhimutto hoti – ayaṃ tatiyo vimokkho.",
    f"Устремлён к прекрасному {DASH} это третье освобождение.")
put("Sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā \"ananto ākāso\"ti "
    "ākāsānañcāyatanaṃ upasampajja viharati – ayaṃ catuttho vimokkho.", f"{cap(ARUPA4)} {DASH} это четвёртое освобождение.")
put("Sabbaso ākāsānañcāyatanaṃ samatikkamma \"anantaṃ viññāṇa\"nti viññāṇañcāyatanaṃ upasampajja viharati – ayaṃ "
    "pañcamo vimokkho.", f"{cap(ARUPA5)} {DASH} это пятое освобождение.")
put("Sabbaso viññāṇañcāyatanaṃ samatikkamma \"natthi kiñci\"ti ākiñcaññāyatanaṃ upasampajja viharati – ayaṃ chaṭṭho "
    "vimokkho.", f"{cap(ARUPA6)} {DASH} это шестое освобождение.")
put("Sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanaṃ upasampajja viharati – ayaṃ sattamo vimokkho.",
    f"{cap(ARUPA7)} {DASH} это седьмое освобождение.")
put("Sabbaso nevasaññānāsaññāyatanaṃ samatikkamma saññāvedayitanirodhaṃ upasampajja viharati – ayaṃ aṭṭhamo vimokkho.",
    f"Полностью преодолев сферу ни восприятия, ни невосприятия, входит в {NIRODHA} и пребывает в нём {DASH} это "
    f"восьмое освобождение.")
put('"Samādhī"ti.', "«Сосредоточение».")
put("Tayo samādhī – savitakkasavicāro samādhi, avitakkavicāramatto samādhi, avitakkaavicāro samādhi.",
    f"Три сосредоточения {DASH} сосредоточение с направленной мыслью и удержанием мысли, сосредоточение без "
    f"направленной мысли, только с удержанием мысли, и сосредоточение без направленной мысли и без удержания мысли.")
put('"Samāpattī"ti.', "«Медитативное достижение».")
put("Nava anupubbavihārasamāpattiyo – paṭhamajjhānasamāpatti, dutiyajjhānasamāpatti, tatiyajjhānasamāpatti, "
    "catutthajjhānasamāpatti, ākāsānañcāyatanasamāpatti, viññāṇañcāyatanasamāpatti, ākiñcaññāyatanasamāpatti, "
    "nevasaññānāsaññāyatanasamāpatti, saññāvedayitanirodhasamāpatti.",
    f"Девять медитативных достижений последовательного пребывания {DASH} " + T.enum(SAMAP9) + ".")
put('"Saṃkilesa"nti hānabhāgiyo dhammo.', "«Омрачение»: явление, ведущее к упадку.")
put('"Vodāna"nti visesabhāgiyo dhammo.', "«Очищение»: явление, ведущее к отличию.")
put('"Vuṭṭhāna"nti.', "«Выход».")
put("Vodānampi vuṭṭhānaṃ, tamhā tamhā samādhimhā vuṭṭhānampi vuṭṭhānanti.",
    "И очищение является выходом, и выход из того или иного сосредоточения является выходом.")
# (8)
_REBIRTHS = ("одно рождение, два рождения, три рождения, четыре рождения, пять рождений, десять рождений, двадцать "
             "рождений, тридцать рождений, сорок рождений, пятьдесят рождений, сто рождений, тысячу рождений, сто тысяч "
             "рождений, многие эпохи сжатия мира, многие эпохи развёртывания мира, многие эпохи сжатия и развёртывания мира")
_THERE = ("«Там я был с таким-то именем, из такого-то рода, с таким-то обликом, такой была моя пища, такие удовольствия "
          "и боли я испытывал, таким был предел моей жизни; уйдя оттуда, я появился там; и там я был с таким-то именем, из "
          "такого-то рода, с таким-то обликом, такой была моя пища, такие удовольствия и боли я испытывал, таким был "
          "предел моей жизни; уйдя оттуда, я появился здесь»")
_PI4 = open(os.path.join(S.ROOT, r"AI_translation\russian\pi-4-russian-plain-rails_split_chapters\5-catukkapuggalapannatti.md"),
            encoding="utf-8").read()
for _x in (_REBIRTHS, _THERE, "Так он вспоминает многие прежние жизни со всеми их особенностями и подробностями",
           "постигнув высшим знанием и осуществив свободные от влечений освобождение ума и освобождение мудростью"):
    pass
assert _REBIRTHS in _PI4 and _THERE in _PI4
put('Idha tathāgato anekavihitaṃ pubbenivāsaṃ anussarati, seyyathidaṃ – ekampi jātiṃ dvepi jātiyo tissopi jātiyo '
    'catassopi jātiyo pañcapi jātiyo dasapi jātiyo vīsampi jātiyo tiṃsampi jātiyo cattālīsampi jātiyo paññāsampi jātiyo '
    'jātisatampi jātisahassampi jātisatasahassampi anekepi saṃvaṭṭakappe anekepi vivaṭṭakappe anekepi '
    'saṃvaṭṭavivaṭṭakappe "amutrāsiṃ evaṃnāmo evaṃgotto evaṃvaṇṇo evamāhāro evaṃsukhadukkhappaṭisaṃvedī '
    'evamāyupariyanto, so tato cuto amutra udapādiṃ; tatrāpāsiṃ evaṃnāmo evaṃgotto evaṃvaṇṇo evamāhāro '
    'evaṃsukhadukkhappaṭisaṃvedī evamāyupariyanto, so tato cuto idhūpapanno"ti.',
    f"Вот Татхагата вспоминает многие прежние жизни, а именно {DASH} {_REBIRTHS}: {_THERE}.")
put("Iti sākāraṃ sauddesaṃ anekavihitaṃ pubbenivāsaṃ anussaratīti.",
    "Так он вспоминает многие прежние жизни со всеми их особенностями и подробностями.")
# (9)
_SEE = ("божественным глазом, очищенным и превосходящим человеческий, видит существ умирающих и перерождающихся, низших "
        "и высших, красивых и безобразных, счастливых и несчастных, понимает, что существа идут согласно своим действиям")
_BADB = ("обладали дурным телесным поведением, обладали дурным речевым поведением, обладали дурным умственным поведением, "
         "хулили благородных, придерживались ложного воззрения и принимали на себя действия, основанные на ложном "
         "воззрении")
_GOODB = ("обладали хорошим телесным поведением, обладали хорошим речевым поведением, обладали хорошим умственным "
          "поведением, не хулили благородных, придерживались правильного воззрения и принимали на себя действия, "
          "основанные на правильном воззрении")
put('Idha tathāgato dibbena cakkhunā visuddhena atikkantamānusakena satte passati cavamāne upapajjamāne hīne paṇīte '
    'suvaṇṇe dubbaṇṇe sugate duggate yathākammūpage satte pajānāti – "ime vata bhonto sattā kāyaduccaritena samannāgatā '
    'vacīduccaritena samannāgatā manoduccaritena samannāgatā ariyānaṃ upavādakā micchādiṭṭhikā '
    'micchādiṭṭhikammasamādānā.',
    f"Вот Татхагата {_SEE} {DASH} «Эти почтенные существа {_BADB}.")
put("Te kāyassa bhedā paraṃ maraṇā apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapannā.",
    f"После распада тела, после смерти они появились {HELL}.")
put("Ime vā pana bhonto sattā kāyasucaritena samannāgatā vacīsucaritena samannāgatā manosucaritena samannāgatā "
    "ariyānaṃ anupavādakā sammādiṭṭhikā sammādiṭṭhikammasamādānā.", f"А эти почтенные существа {_GOODB}.")
put('Te kāyassa bhedā paraṃ maraṇā sugatiṃ saggaṃ lokaṃ upapannā"ti.',
    f"После распада тела, после смерти они появились {HEAVEN}».")
put("Iti dibbena cakkhunā visuddhena atikkantamānusakena satte passati cavamāne upapajjamāne hīne paṇīte suvaṇṇe "
    "dubbaṇṇe sugate duggate yathākammūpage satte pajānātīti.", f"Так {_SEE}.")
assert "После распада тела, после смерти они появились " + HELL in _PI4 and HEAVEN + "»" in _PI4
# (10)
put("Idha tathāgato āsavānaṃ khayā anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā "
    "upasampajja viharatīti.",
    "Вот Татхагата с уничтожением влечений уже в этой жизни сам, постигнув высшим знанием и осуществив свободные от "
    "влечений освобождение ума и освобождение мудростью, достиг их и пребывает в них.")
put('"Ye ye dhammā yesaṃ yesaṃ dhammānaṃ hetū paccayā upādāya taṃ taṃ ṭhānaṃ, ye ye dhammā yesaṃ yesaṃ dhammānaṃ na '
    'hetū appaccayā upādāya taṃ taṃ aṭṭhāna"nti.',
    "«Те явления, которые являются причинами и условиями тех или иных явлений, в силу этого делают то или иное "
    "возможным; те явления, которые не являются причинами и условиями тех или иных явлений, в силу этого делают то или "
    "иное невозможным».")
in_pi1("постигнув высшим знанием и осуществив")


def tala_ans(s):
    m = re.match(r"^Yā tattha paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – idaṃ tathāgatassa (.+) yathābhūtaṃ "
                 r"ñāṇa(?:ṃ|nti)\.$", s)
    if not m:
        return None
    key = f"tathāgatassa {m.group(1)} yathābhūtaṃ ñāṇaṃ"
    return cap(know_ans(POWER_Q[key])) + "."


# ================================================================ 7. line translation
SPLIT = re.compile(r'(?<=[.?])\s+(?=["A-ZĀĪŪṬḌÑṆṄ])')
FIXES = [   # (Pāli as written, as meant): punctuation / spelling slips only, all reported
    ("pajānanā …pe…", "pajānanā…pe…"),                                                   # ^2-788
    ("vacīsucaritasamaṅgī …pe…", "vacīsucaritasamaṅgī…pe…"),                             # ^2-809
    ('"hoti tathāgato paraṃ maraṇāti vā,', '"hoti tathāgato paraṃ maraṇā"ti vā,'),      # ^2-815 closing quote
    ('vuccati "saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ. Evaṃ',
     'vuccati "saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ". Evaṃ'),                         # ^2-803 closing quote
    ("Atthi upādinnupādāniyā, atthi anuppādinnupādāniyā, atthi anuppādinnaanupādāniyā",
     "Atthi upādinnupādāniyā, atthi anupādinnupādāniyā, atthi anupādinnaanupādāniyā"),   # ^2-753 (40)
    ("Atthi ajjhatā,", "Atthi ajjhattā,"),                                              # ^2-753 (62)
    (' So kho panāhaṃ imaṃ samādhiṃ', ' "So kho panāhaṃ imaṃ samādhiṃ'),                 # ^2-804 opening quote
]
OPENQ = {   # sentence whose opening quote is missing in the Pāli (^2-809 line 2): rendered with it
}


def tr_sentence(s):
    for fn in (question, answer, tala_ans, hana_sent, is_also):
        r = fn(s)
        if r:
            return r
    if s.startswith('Idha tathāgato "aṭṭhānametaṃ'):
        return th_sent('"Aṭṭhānametaṃ' + s[len('Idha tathāgato "aṭṭhānametaṃ'):], first=True)
    if s.startswith('Idha tathāgato pajānāti – "atthekaccāni'):
        return f"Вот Татхагата понимает {DASH} " + ks_sent('"A' + s[len('Idha tathāgato pajānāti – "a'):])
    if s in SENT:
        return SENT[s]
    if s.startswith('"So kho panāhaṃ'):
        return SENT[s[1:]]
    if TH_A.match(s) or TH_P.match(s):
        return th_sent(s)
    if re.match(r'^"?[Aa]tthekaccāni ', s):
        return ks_sent(s)
    raise KeyError("sentence: " + s[:160])


def tr_body(t):
    out = []
    for s in SPLIT.split(t):
        out.append(tr_sentence(s))
    return " ".join(out)


def label(t):
    m = re.match(r"^\((?:(\d+(?:-\d+)?)\. )?(Ka|Kha|Gha|Ga|Kha-gha)\) (.+)$", t)
    if m:
        num = f"{m.group(1)}. " if m.group(1) else ""
        return f"({num}{LABEL[m.group(2)]}) ", m.group(3)
    m = re.match(r"^\((\d+(?:-\d+)?)\) (.+)$", t)
    if m:
        return f"({m.group(1)}) ", m.group(2)
    return "", t


def matika_item(rest, group):
    """items of the matrices (the lines after "N-vidhena ñāṇavatthu –")."""
    if group == "duka" or group == "tika" and " paññā" in rest and not rest.startswith(("Atthi", "Savitakk", "Avitakk",
                                                                                      "Pītisahagatā paññā atthi",
                                                                                      "Pītisahagatā paññā sukha",
                                                                                      "Upekkhāsahagatā paññā atthi")):
        return panna_list(rest)
    return None


def tika_atthi(rest):
    m = re.match(r"^(.+?) atthi (.+)$", rest)
    if m and not rest.startswith("Atthi"):
        subj = m.group(1)
        if subj == "Pītisahagatā paññā sukhasahagatā paññā":
            sr = f"{pn('pītisahagatā')[0]}, или {pn('sukhasahagatā')[0]},"
        else:
            sr = closing(pn(low1(subj)[:-len(' paññā')])[0])
        body = "atthi " + m.group(2)
        return cap(sr) + " " + atthi_list(body)
    return cap(atthi_list(rest))


def atthi_list(body):
    items = re.split(r",? ?[Aa]tthi ", body)[1:]
    return ", ".join(f"бывает {b_of(x.strip(', '))}" for x in items)


UNIQUE = []   # (opening words of the Pāli line, Russian) in order, for the lines not parsed below


def U(prefix, ru):
    UNIQUE.append((prefix, ru))


def build_lines(pali):
    out = []
    group = None
    for t in pali:
        for a, b in FIXES:
            t = t.replace(a, b)
        out.append(line(t))
    return out


STATE = {"group": None, "section": None}


def line(t):
    st = STATE
    if t == "### Ñāṇavibhaṅgo":
        return "### " + S.CHAPTER_TITLES[16]
    if t.startswith("#### "):
        st["section"] = t[5:]
        return "#### " + HEAD4[t[5:]]
    if t.startswith("##### "):
        g = t[6:-len("niddeso")]
        st["section"] = "niddesa"
        st["group"] = g
        return f"##### Объяснение {GROUPW[g]}"
    if t in CLOSE_GROUP:
        return CLOSE_GROUP[t]
    if t == "Ñāṇavibhaṅgo niṭṭhito.":
        return S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[16])
    m = re.match(r"^(\w+?)[vb]idhena ñāṇavatthu –$", t)
    if m:
        st["group"] = m.group(1)
        return f"{frame(NUMW[m.group(1)])} {DASH}"
    m = re.match(r"^(.*?)\s*[Ee]vaṃ (\w+?)[vb]idhena ñāṇavatthu\.$", t)
    if m and (m.group(1) == "" or (m.group(1).endswith((".", '."')) and st["section"] == "niddesa")):
        pre = m.group(1)
        r = frame_close(NUMW[m.group(2)])
        if pre:
            lab, rest = label(pre)
            return lab + case(rest, rest_tr(rest)) + " " + r
        return r
    if t.startswith("Ekavidhena ñāṇavatthu – pañca viññāṇā "):
        return ekaka_matika(t)
    if t.startswith("Dasavidhena ñāṇavatthu – "):
        return (f"{frame(10)} {DASH} {POWERS10}, {LION_PL}. Какие десять?")
    sec = st["section"]
    lab, rest = label(t)
    if sec in ("Ekakamātikā",):
        return lab + ekaka_item(rest)
    if sec == "Dukamātikā":
        return lab + panna_list(rest)
    if sec == "Tikamātikā":
        return lab + tika_item(rest)
    if sec == "Catukkamātikā":
        return lab + catukka_item(rest)
    if sec in ("Pañcakamātikā", "Chakkamātikā", "Sattakamātikā", "Aṭṭhakamātikā", "Navakamātikā"):
        return lab + small_item(rest)
    if sec == "Dasakamātikā":
        return lab + dasaka_item(rest)
    return lab + case(rest, niddesa(rest, lab))


def case(p, r):
    """the Russian line starts with a capital where the Pāli does, else lower case (after "(1. Ka) tattha …")."""
    if p[:1].islower():
        return lc(r)
    if p[:1].isupper():
        return cap(r)
    return r


def rest_tr(rest):
    return niddesa(rest, "")


def ekaka_item(rest):
    if rest == "Uppannavatthukā uppannārammaṇā,":
        return EK["uppanna"][0] + ","
    keys = {"Purejātavatthukā purejātārammaṇā": "purejata", "Ajjhattikavatthukā bāhirārammaṇā": "ajjhattika",
            "Asambhinnavatthukā asambhinnārammaṇā": "asambhinna", "Nānāvatthukā nānārammaṇā": "nana",
            "Na aññamaññassa gocaravisayaṃ paccanubhonti": "gocara", "Na asamannāhārā uppajjanti": "samannahara",
            "Na amanasikārā uppajjanti": "manasikara", "Na abbokiṇṇā uppajjanti": "abbokinna",
            "Na apubbaṃ acarimaṃ uppajjanti": "apubbam", "Na aññamaññassa samanantarā uppajjanti": "samanantara",
            "Pañca viññāṇā anābhogā": "anabhoga"}
    if rest in keys:
        return EK[keys[rest]][0]
    if rest == "Pañcahi viññāṇehi na kañci [kiñci (sī. ka.)] dhammaṃ paṭivijānāti aññatra abhinipātamattā":
        return f"{BY5} {ACTS['na kañci dhammaṃ paṭivijānāti']}{VAR_KINCI}, {ABHINIPATA}"
    if rest.endswith(", yāthāvakavatthuvibhāvanā paññā"):
        return acts_pali_ru(rest[:-len(", yāthāvakavatthuvibhāvanā paññā")]) + ", " + YATHAVAKA
    return acts_pali_ru(rest)


def tika_item(rest):
    if rest == "Āyakosallaṃ, apāyakosallaṃ, upāyakosallaṃ":
        return cap(", ".join(NANA[k][0] for k in ("āyakosallaṃ", "apāyakosallaṃ", "upāyakosallaṃ")))
    if " atthi " in rest or rest.startswith("Atthi "):
        return tika_atthi(rest)
    return panna_list(rest)


def catukka_item(rest):
    t4 = {
        "Kammassakatañāṇaṃ, saccānulomikaṃ ñāṇaṃ, maggasamaṅgissa ñāṇaṃ, phalasamaṅgissa ñāṇaṃ":
            [NANA[k][0] for k in ("kammassakatañāṇaṃ", "saccānulomikaṃ ñāṇaṃ", "maggasamaṅgissa ñāṇaṃ", "phalasamaṅgissa ñāṇaṃ")],
        "Dhamme ñāṇaṃ, anvaye ñāṇaṃ, pariye [paricce (sabbattha) passa dīghanikāye] ñāṇaṃ, sammutiñāṇaṃ [sammatiñāṇaṃ (syā.) passa dīghanikāye]":
            [NANA["dhamme ñāṇaṃ"][0], NANA["anvaye ñāṇaṃ"][0],
             NANA["pariye ñāṇaṃ"][0] + " [вариант написания (во всех изданиях): paricce; см. Дигха-никаю]",
             NANA["sammutiñāṇaṃ"][0] + " [вариант написания (Syā.): sammatiñāṇaṃ; см. Дигха-никаю]"],
    }
    if rest in t4:
        return list_nom(t4[rest])
    m = re.match(r"^(\w+) ñāṇaṃ, (\w+) ñāṇaṃ, (\w+) ñāṇaṃ, (\w+ paṭipadāya) ñāṇaṃ$", rest)
    if m:
        return list_nom([NANA[f"{low1(x)} ñāṇaṃ"][0] for x in m.groups()])
    if rest.startswith("Atthi paññā "):
        items = rest.split(", ")
        return cap(", ".join(f"есть мудрость, {ACAYA[x[len('atthi paññā '):] if x.startswith('atthi') else x[len('Atthi paññā '):]]}"
                             for x in items))
    if rest == "Catasso paṭisambhidā":
        return "Четыре аналитических знания"
    if rest == "Catasso paṭipadā":
        return "Четыре способа практики"
    if rest == "Cattāri ārammaṇāni":
        return "Четыре объекта"
    if rest.startswith("Jātiyā ñāṇaṃ…pe…"):
        body, closing_ = rest.split(". Evaṃ ")
        out = []
        for chunk in body.split(", "):
            bits = chunk.split("…pe… ")
            out.append("… ".join(NANA[low1(b)][0] for b in bits))
        return cap(", ".join(out)) + ". " + frame_close(4)
    return panna_list(rest)


def small_item(rest):
    tbl = {"Pañcaṅgiko sammāsamādhi (2) pañcañāṇiko sammāsamādhi": f"{cap(FIVE_SAMADHI)} (2) {FIVE_NANA}",
           "Chasu abhiññāsu paññā": "Мудрость в шести высших знаниях",
           "Sattasattati ñāṇavatthūni": f"Семьдесят семь {NV}",
           "Catūsu maggesu, catūsu phalesu paññā": "Мудрость в четырёх путях, в четырёх плодах",
           "Navasu anupubbavihārasamāpattīsu paññā": f"Мудрость в девяти {ANUPUBBA}"}
    return tbl[rest]


def dasaka_item(rest):
    for n, p in POWER_P.items():
        head = "Idha tathāgato " if n == 1 else "Puna caparaṃ tathāgato "
        var = "" if n != 4 else " [anekadhātuṃ nānādhātuṃ lokaṃ (syā.) ma. ni. 1.148]"
        pl = (f"{head}{p}{var} yathābhūtaṃ pajānāti. Yampi tathāgato {p} yathābhūtaṃ pajānāti, idampi tathāgatassa "
              f"tathāgatabalaṃ hoti, yaṃ balaṃ āgamma tathāgato āsabhaṃ ṭhānaṃ paṭijānāti, parisāsu sīhanādaṃ nadati, "
              f"brahmacakkaṃ pavatteti.")
        if rest == pl:
            return power_line(n, VAR_ANEKADHATU if n == 4 else "")
        tail = (" Imāni dasa tathāgatassa tathāgatabalāni, yehi balehi samannāgato tathāgato āsabhaṃ ṭhānaṃ paṭijānāti, "
                "parisāsu sīhanādaṃ nadati, brahmacakkaṃ pavatteti.")
        if rest == pl + tail:
            return power_line(n) + f" Это {POWERS10}, {LION_PL}."
    raise KeyError("dasaka: " + rest[:80])


GROUP_NID = {}


def niddesa(rest, lab):
    g = STATE["group"]
    if g == "Ekaka":
        return ekaka_nid(rest)
    if rest in SENT:
        return SENT[rest]
    if ("?" not in rest and " – " not in rest and re.match(r"^.+ paññā .+ paññā\.$", rest)
            and not rest.startswith(("Maggasamaṅgissa", "Dhammasamaṅgissa"))):
        return duka_line(rest[:-1])
    return tr_body(rest)


def ekaka_nid(rest):
    if rest.startswith("Pañca viññāṇā na hetumeva"):
        return ekaka_niddesa(rest)
    m = re.match(r"^(.+?)ti (.+)$", rest)
    tbl = {
        "Pañca viññāṇā uppannavatthukā, uppannārammaṇā": (
            "Пять видов сознания " + EK["uppanna"][1], "возникают при возникшей основе, при возникшем объекте"),
        "Purejātavatthukā, purejātārammaṇā": (EK["purejata"][1],
                                             "возникают при ранее возникшей основе, при ранее возникшем объекте"),
        "Ajjhattikavatthukā, bāhirārammaṇā": (EK["ajjhattika"][1],
                                             "основы пяти видов сознания относятся к внутреннему, объекты относятся к "
                                             "внешнему"),
        "Asambhinnavatthukā, asambhinnārammaṇā": (EK["asambhinna"][1],
                                                 "возникают при неразрушенной основе, при неразрушенном объекте"),
        "Nānāvatthukā, nānārammaṇā": (EK["nana"][1], ", ".join(
            f"{'одни' if i == 0 else 'другие'} основа и объект у {VG[k]}" for i, k in enumerate(VG))),
        "Na asamannāhārā uppajjantī": (EK["samannahara"][1], "возникают у того, кто обращает внимание"),
        "Na amanasikārā uppajjantī": (EK["manasikara"][1], "возникают у того, кто уделяет внимание"),
        "Na abbokiṇṇā uppajjantī": (EK["abbokinna"][1], "не возникают одно за другим"),
        "Na apubbaṃ acarimaṃ uppajjantī": (EK["apubbam"][1], "не возникают в один момент"),
        "Pañca viññāṇā anābhogā": (EK["anabhoga"][1],
                                   "у пяти видов сознания нет ни поворота ума, ни вовлечённости, ни обращения внимания, "
                                   "ни внимания"),
        "Aññatra abhinipātamattā": (cap(ABHINIPATA), APATA),
    }
    if rest.startswith("Na aññamaññassa gocaravisayaṃ"):
        return gocara_line("gocara")
    if rest.startswith("Na aññamaññassa samanantarā"):
        return gocara_line("samanantara")
    if rest.startswith("Pañcannaṃ viññāṇānaṃ samanantarāpi na supati") and rest.endswith(
            " Evaṃ yāthāvakavatthuvibhāvanā paññā."):
        body = rest[:-len(" Evaṃ yāthāvakavatthuvibhāvanā paññā.")]
        return ekaka_act_nid(body) + f" Такова {YATHAVAKA}."
    if rest.startswith(("Pañcahi viññāṇehi", "Pañcannaṃ viññāṇānaṃ samanantarāpi")):
        return ekaka_act_nid(rest)
    lem, expl = tbl[m.group(1)]
    return f"«{lem}»: {expl}."


def ekaka_act_nid(rest):
    m = re.match(r"^(Pañcahi viññāṇehi|Pañcannaṃ viññāṇānaṃ samanantarāpi) (.+?)ti (Pañcahi viññāṇehi|pañcahi viññāṇehi|"
                 r"pañcannaṃ viññāṇānaṃ samanantarā manodhātuyāpi) (.+?)( – gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā)?\.$",
                 rest)
    a, act, b, act2, post = m.groups()
    assert act.rstrip("ī") == act2.rstrip("i") or act[:-1] == act2[:-1], (act, act2)
    lem = acts_pali_ru(f"{a} {act[:-1]}i" if act.endswith("ī") else f"{a} {act}")
    if b.startswith("pañcannaṃ"):
        expl = f"{MANODHATU} {ACTS[act2]}"
    else:
        expl = f"{lc(BY5)} {ACTS[act2]}"
    if post:
        expl += f" {DASH} {POSTURES}"
    return f"«{lem}»: {expl}."


# ================================================================ 8. build
def build():
    pali = open(os.path.join(S.PALI_DIR, FN), encoding="utf-8").read().rstrip("\n").split("\n")
    nonempty = [S.ID.sub("", l).rstrip() for l in pali if l.strip()]
    ru = build_lines(nonempty)
    assert len(ru) == len(nonempty), (len(ru), len(nonempty))
    for p, r in zip(nonempty, ru):
        assert p.count(DASH) + p.count("—") == r.count(DASH), ("dash count", p[:90], r[:90])
        assert "—" not in r and "  " not in r, r[:80]
        assert p.startswith("#") == r.startswith("#"), (p[:40], r[:40])
        assert not re.search(r"[A-Za-zĀāĪīŪūṬṭḌḍÑñṆṇṄṅṂṃḶḷ]", re.sub(r"\[[^\]]*\]", "", r)), ("latin", r[:160])
        assert not re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", r), r[:80]
    lines = S.attach_ids(pali, ru)
    S.write(os.path.join(S.RU_DIR, FN), lines)
    print("OK:", FN, "|", len(ru), "non-empty lines")


if __name__ == "__main__":
    build()
