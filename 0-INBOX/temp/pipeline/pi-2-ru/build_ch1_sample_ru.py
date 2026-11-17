# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: preamble + chapter-1 sample (first 77 non-empty lines).

usage: python -I -X utf8 build_ch1_sample_ru.py
Writes (only when run as a script):
  AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\preamble.md
  0-INBOX\\temp\\pipeline\\pi-2-ru\\ch1-sample.md   (Russian of ch1-sample-pali.md, same blank lines)

Other agents: import this module and reuse the constants and frame functions verbatim
(BOOK_TITLE, CHAPTER_TITLES, SECTION_TITLES, AGG, FIVE_AGGREGATES, TIME, SELF_*, MEMBERS,
khandha_def, time_line, self_line, question, answer, np, comp_line, far_line, near_line,
tail, class_open, class_close, RUPA_* strings ...).
Block IDs are never typed here: they are copied from the Pāli line at build time.
main() asserts that every string marked [pi-1] still occurs byte for byte in the pi-1 Russian.
"""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
RU_DIR = os.path.join(ROOT, r"AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters")
PI1_RU_DIR = os.path.join(ROOT, r"AI_translation\russian\pi-1-russian-plain-rails_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-2-ru")

DASH = "–"  # the only dash allowed, and only where the Pāli has one
ID = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")

# ---------------------------------------------------------------- 1. book frame and headings
HOMAGE = "Почтение Благословенному, Достойному, Полностью Пробуждённому Будде"   # [pi-1]
PITAKA = "В корзине Абхидхаммы"                                                    # [pi-1]
BOOK_TITLE = "Подробный разбор"                                                   # Vibhaṅgapāḷi (proposal)
BOOK_TITLE_ALTERNATIVES = ["Разбор", "Разбор явлений"]
BOOK_TITLE_QUOTED = "«" + BOOK_TITLE + "»"                                        # mid-sentence form

CHAPTER_TITLES = {  # ### level; closing line "<X>vibhaṅgo niṭṭhito." = "<title> завершён."
    1: "Разбор совокупностей",                                  # Khandhavibhaṅgo
    2: "Разбор сфер восприятия",                                # Āyatanavibhaṅgo
    3: "Разбор элементов",                                      # Dhātuvibhaṅgo
    4: "Разбор истин",                                          # Saccavibhaṅgo
    5: "Разбор способностей",                                   # Indriyavibhaṅgo
    6: "Разбор возникновения в зависимости от условий",         # Paṭiccasamuppādavibhaṅgo
    7: "Разбор основ осознанности",                             # Satipaṭṭhānavibhaṅgo
    8: "Разбор правильных усилий",                              # Sammappadhānavibhaṅgo
    9: "Разбор основ сверхспособностей",                        # Iddhipādavibhaṅgo
    10: "Разбор факторов пробуждения",                          # Bojjhaṅgavibhaṅgo
    11: "Разбор факторов пути",                                 # Maggaṅgavibhaṅgo
    12: "Разбор медитативных погружений",                       # Jhānavibhaṅgo
    13: "Разбор безмерных состояний",                           # Appamaññāvibhaṅgo
    14: "Разбор правил обучения",                               # Sikkhāpadavibhaṅgo
    15: "Разбор аналитических знаний",                          # Paṭisambhidāvibhaṅgo
    16: "Разбор знания",                                        # Ñāṇavibhaṅgo
    17: "Разбор малых тем",                                     # Khuddakavatthuvibhaṅgo
    18: "Разбор сути явлений",                                  # Dhammahadayavibhaṅgo
}
CHAPTER_CLOSING = "{title} завершён."  # pi-1: «Раздел о материальной форме завершён.»

SECTION_TITLES = {  # #### level; the same words + "." as the closing line ("Suttantabhājanīyaṃ.")
    "Suttantabhājanīyaṃ": "Разбор по наставлениям",
    "Abhidhammabhājanīyaṃ": "Разбор по Абхидхамме",
    "Pañhāpucchakaṃ": "Раздел вопросов",
}

# ---------------------------------------------------------------- 2. aggregates
# g: f / n / pl (grammatical class of the Russian noun phrase)
AGG = {
    "rupa": dict(nom="материальная форма", ins="материальной формой", acc="материальную форму", g="f",
                 khandha="совокупность материальной формы", khandha_ins="совокупностью материальной формы",
                 khandha_gen="совокупности материальной формы", heading="Совокупность материальной формы"),
    "vedana": dict(nom="чувство", ins="чувством", acc="чувство", g="n",
                   sg=("чувство", "чувства"), pl=("чувства", "чувств"),
                   khandha="совокупность чувств", khandha_ins="совокупностью чувств",
                   khandha_gen="совокупности чувств", heading="Совокупность чувств"),
    "sanna": dict(nom="восприятие", ins="восприятием", acc="восприятие", g="n",
                  sg=("восприятие", "восприятия"), pl=("восприятия", "восприятий"),
                  khandha="совокупность восприятия", khandha_ins="совокупностью восприятия",
                  khandha_gen="совокупности восприятия", heading="Совокупность восприятия"),
    "sankhara": dict(nom="формирующие факторы", ins="формирующими факторами", acc="формирующие факторы", g="pl",
                     sg=("формирующие факторы", "формирующих факторов"), pl=("формирующие факторы", "формирующих факторов"),
                     khandha="совокупность формирующих факторов", khandha_ins="совокупностью формирующих факторов",
                     khandha_gen="совокупности формирующих факторов", heading="Совокупность формирующих факторов"),
    "vinnana": dict(nom="сознание", ins="сознанием", acc="сознание", g="n",
                    sg=("сознание", "сознания"), pl=("виды сознания", "видов сознания"),
                    khandha="совокупность сознания", khandha_ins="совокупностью сознания",
                    khandha_gen="совокупности сознания", heading="Совокупность сознания"),
}
# [pi-1 ^1-1089]
FIVE_AGGREGATES = ("Пять совокупностей " + DASH + " совокупность материальной формы, совокупность чувств, "
                   "совокупность восприятия, совокупность формирующих факторов и совокупность сознания")


def cap(s):
    return s[:1].upper() + s[1:]


def is_pl(a):
    return AGG[a]["g"] == "pl"


# attribute adjectives: nom / ins / acc per class f, n, pl; post=True -> placed after the noun with commas
ATTR = {
    "atita": dict(nom=("прошлая", "прошлое", "прошлые"), ins=("прошлой", "прошлым", "прошлыми")),
    "anagata": dict(nom=("будущая", "будущее", "будущие"), ins=("будущей", "будущим", "будущими")),
    "paccuppanna": dict(nom=("настоящая", "настоящее", "настоящие"), ins=("настоящей", "настоящим", "настоящими")),
    "ajjhatta": dict(nom=("внутренняя", "внутреннее", "внутренние"), ins=("внутренней", "внутренним", "внутренними")),
    "bahiddha": dict(nom=("внешняя", "внешнее", "внешние"), ins=("внешней", "внешним", "внешними")),
    "olarika": dict(nom=("грубая", "грубое", "грубые"), ins=("грубой", "грубым", "грубыми"), acc=("грубую", "грубое", "грубые")),
    "sukhuma": dict(nom=("тонкая", "тонкое", "тонкие"), ins=("тонкой", "тонким", "тонкими"), acc=("тонкую", "тонкое", "тонкие")),
    "hina": dict(nom=("низшая", "низшее", "низшие"), ins=("низшей", "низшим", "низшими"), acc=("низшую", "низшее", "низшие")),
    "panita": dict(nom=("высшая", "высшее", "высшие"), ins=("высшей", "высшим", "высшими"), acc=("высшую", "высшее", "высшие")),
    "dure": dict(post=True, nom=("находящаяся вдали", "находящееся вдали", "находящиеся вдали"),
                 ins=("находящейся вдали", "находящимся вдали", "находящимися вдали")),
    "santike": dict(post=True, nom=("находящаяся вблизи", "находящееся вблизи", "находящиеся вблизи"),
                    ins=("находящейся вблизи", "находящимся вблизи", "находящимися вблизи")),
}
GI = {"f": 0, "n": 1, "pl": 2}


def attr(key, a, case="nom"):
    return ATTR[key][case][GI[AGG[a]["g"]]]


def attr_np(key, a, case="nom"):
    """'прошлая материальная форма' / 'чувство, находящееся вдали' (no closing comma)."""
    noun = AGG[a]["nom"] if case == "nom" else AGG[a]["ins"]
    if ATTR[key].get("post"):
        return f"{noun}, {attr(key, a, case)}"
    return f"{attr(key, a, case)} {noun}"


# ---------------------------------------------------------------- 3. question / answer frames
TATTHA = "Что такое здесь"                     # Tattha katamo/katamā/katamaṃ/katame … ?  [pi-1 ^1-584, ^1-1009]
VUCCATI = "это называется"                     # idaṃ / ayaṃ vuccati; ime vuccanti (same Russian)  [pi-1]


def question(a, key):
    """Tattha katamaṃ rūpaṃ atītaṃ?  ->  Что такое здесь прошлая материальная форма?"""
    return f"{TATTHA} {attr_np(key, a)}?"


def question_pair(a, x, y):
    """Tattha katamā vedanā oḷārikā sukhumā?  ->  Что такое здесь грубое и тонкое чувство?"""
    return f"{TATTHA} {attr(x, a)} и {attr(y, a)} {AGG[a]['nom']}?"


def answer(a, key):
    """idaṃ / ayaṃ vuccati rūpaṃ atītaṃ  ->  это называется прошлой материальной формой"""
    return f"{VUCCATI} {attr_np(key, a, 'ins')}"


def khandha_question(a):
    """Tattha katamo rūpakkhandho?"""
    return f"{TATTHA} {AGG[a]['khandha']}?"


def khandha_answer(a):
    """ayaṃ vuccati rūpakkhandho"""
    return f"{VUCCATI} {AGG[a]['khandha_ins']}"


# ---------------------------------------------------------------- 4. aggregate definition (Suttantabhājanīya)
KHANDHA_ANY = {"f": "Любая", "n": "Любое", "pl": "Любые"}
KHANDHA_ATTRS = {  # atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā … yaṃ dūre santike vā
    "f": "прошлая, будущая или настоящая, внутренняя или внешняя, грубая или тонкая, низшая или высшая, находящаяся вдали или вблизи",
    "n": "прошлое, будущее или настоящее, внутреннее или внешнее, грубое или тонкое, низшее или высшее, находящееся вдали или вблизи",
    "pl": "прошлые, будущие или настоящие, внутренние или внешние, грубые или тонкие, низшие или высшие, находящиеся вдали или вблизи",
}
KHANDHA_TOGETHER = {  # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā
    "f": "вся вместе, собранная воедино и обобщённая",
    "n": "всё вместе, собранное воедино и обобщённое",
    "pl": "все вместе, собранные воедино и обобщённые",
}


def khandha_def(a):
    g = AGG[a]["g"]
    return (f"{khandha_question(a)} {KHANDHA_ANY[g]} {AGG[a]['nom']}, {KHANDHA_ATTRS[g]}, {KHANDHA_TOGETHER[g]}, "
            f"{DASH} {khandha_answer(a)}.")


# past / future / present synonym strings; pl = pi-1 ^1-1044/^1-1045/^1-1046 verbatim  [pi-1]
TIME = {
    "atita": {
        "f": "прошлая, прекратившаяся, исчезнувшая, изменившаяся, угасшая, полностью угасшая, исчезнувшая после возникновения, прошлая, включённая в категорию прошлых",
        "n": "прошлое, прекратившееся, исчезнувшее, изменившееся, угасшее, полностью угасшее, исчезнувшее после возникновения, прошлое, включённое в категорию прошлых",
        "pl": "прошлые, прекратившиеся, исчезнувшие, изменившиеся, угасшие, полностью угасшие, исчезнувшие после возникновения, прошлые, включённые в категорию прошлых",
    },
    "anagata": {
        "f": "нерождённая, неставшая, незародившаяся, непоявившаяся, не появившаяся полностью, непроявившаяся, невозникшая, не возникшая полностью, неподнявшаяся, не поднявшаяся полностью, будущая, включённая в категорию будущих",
        "n": "нерождённое, неставшее, незародившееся, непоявившееся, не появившееся полностью, непроявившееся, невозникшее, не возникшее полностью, неподнявшееся, не поднявшееся полностью, будущее, включённое в категорию будущих",
        "pl": "нерождённые, неставшие, незародившиеся, непоявившиеся, не появившиеся полностью, непроявившиеся, невозникшие, не возникшие полностью, неподнявшиеся, не поднявшиеся полностью, будущие, включённые в категорию будущих",
    },
    "paccuppanna": {
        "f": "рождённая, ставшая, зародившаяся, появившаяся, полностью появившаяся, проявившаяся, возникшая, полностью возникшая, поднявшаяся, полностью поднявшаяся, настоящая, включённая в категорию настоящих",
        "n": "рождённое, ставшее, зародившееся, появившееся, полностью появившееся, проявившееся, возникшее, полностью возникшее, поднявшееся, полностью поднявшееся, настоящее, включённое в категорию настоящих",
        "pl": "рождённые, ставшие, зародившиеся, появившиеся, полностью появившиеся, проявившиеся, возникшие, полностью возникшие, поднявшиеся, полностью поднявшиеся, настоящие, включённые в категорию настоящих",
    },
}

# tesaṃ tesaṃ (para)sattānaṃ (parapuggalānaṃ) ajjhattaṃ paccattaṃ niyaka pāṭipuggalika upādinna
# pi-1 ^1-1050/^1-1051 (Pāli there: niyatā = «закреплённый»); pi-2 has niyaka: user 2026-11-14 = pi-1 «закреплённый» [pi-1]
SELF_WHO = {"ajjhatta": "у тех или иных существ",                                   # [pi-1]
            "bahiddha": "у тех или иных других существ, других личностей"}          # [pi-1]
SELF_BODY = {
    "f": "которая {who} находится внутри себя, является собственной, закреплённой, индивидуальной и охваченной цеплянием",
    "n": "которое {who} находится внутри себя, является собственным, закреплённым, индивидуальным и охваченным цеплянием",
    "pl": "которые {who} находятся внутри себя, являются собственными, закреплёнными, индивидуальными и охваченными цеплянием",
}

# the members listed after the definition; close=True -> a comma closes the list before the dash
MAHABHUTA = "четыре великих элемента и материальная форма, производная от четырёх великих элементов"  # [pi-1 ^1-584]
FEELINGS3 = "приятное чувство, болезненное чувство и чувство, которое ни болезненно, ни приятно"       # [pi-1 words]
SIX_DOORS = ("глаза", "уха", "носа", "языка", "тела", "ума")


def six_born(noun):
    """cakkhusamphassajā X … manosamphassajā X  ->  рождённое контактом глаза X, …, и рождённое контактом ума X"""
    items = [f"рождённое контактом {d} {noun}" for d in SIX_DOORS]
    return ", ".join(items[:-1]) + " и " + items[-1]


VINNANA6 = "зрительное сознание, слуховое сознание, обонятельное сознание, вкусовое сознание, осязательное сознание и умственное сознание"  # [pi-1 words]
MEMBERS = {
    "rupa": (MAHABHUTA, True),
    "vedana": (FEELINGS3, True),
    "sanna": (six_born("восприятие"), False),
    "sankhara": (six_born("намерение"), False),
    "vinnana": (VINNANA6, False),
}


def members_dash(a):
    m, close = MEMBERS[a]
    return m + ("," if close else "") + " " + DASH


def time_line(a, key):
    """Tattha katamaṃ rūpaṃ atītaṃ? Yaṃ rūpaṃ atītaṃ … saṅgahitaṃ, <members> – idaṃ vuccati rūpaṃ atītaṃ."""
    g = AGG[a]["g"]
    return f"{question(a, key)} {cap(AGG[a]['nom'])}, {TIME[key][g]}: {members_dash(a)} {answer(a, key)}."


def self_line(a, key):
    """Tattha katamaṃ rūpaṃ ajjhattaṃ / bahiddhā? …"""
    g = AGG[a]["g"]
    body = SELF_BODY[g].format(who=SELF_WHO[key])
    return f"{question(a, key)} {cap(AGG[a]['nom'])}, {body}: {members_dash(a)} {answer(a, key)}."


# ---------------------------------------------------------------- 5. rūpa-only Suttanta strings
EYE_TO_TOUCH = "сфера глаза… сфера осязаемого"                      # Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ  [pi-1 ^1-674]
FEMININITY_TO_FOOD = "способность женственности… съедаемая пища"    # Itthindriyaṃ…pe… kabaḷīkāro āhāro  [pi-1 ^1-675]
VAR_KABALIMKARO = "[вариант написания (Sī., Syā.): kabaḷiṃkāro]"
FIVE_OBJECTS = "видимые формы, звуки, запахи, вкусы и осязаемое"    # rūpā saddā gandhā rasā phoṭṭhabbā  [pi-1 words]
HINA_BODY = ("которая для тех или иных существ является пренебрежённой, презренной, осмеянной, униженной, неуважаемой, "
             "низшей, считающейся низшей, признанной низшей, нежеланной, немилой и неприятной")
PANITA_BODY = ("которая для тех или иных существ является не пренебрежённой, не презренной, не осмеянной, не униженной, уважаемой, "
               "высшей, считающейся высшей, признанной высшей, желанной, милой и приятной")
FAR_OTHER = "а также любая другая материальная форма, которая находится не рядом, не поблизости, вдали, не вблизи"  # yaṃ vā panaññampi atthi rūpaṃ anāsanne anupakaṭṭhe dūre asantike
NEAR_OTHER = "а также любая другая материальная форма, которая находится рядом, поблизости, недалеко, вблизи"      # … āsanne upakaṭṭhe avidūre santike

# Taṃ taṃ vā pana X upādāyupādāya X … daṭṭhabbaṃ
SUCH_INS = {"f": "с той или иной", "n": "с тем или иным", "pl": "с теми или иными"}
PAIR_ACC = {
    ("olarika", "sukhuma"): None, ("hina", "panita"): None,
    ("dure", "santike"): {"f": "находящуюся вдали или вблизи", "n": "находящееся вдали или вблизи", "pl": "находящиеся вдали или вблизи"},
}


def tail(a, x, y):
    """Taṃ taṃ vā pana vedanaṃ upādāyupādāya vedanā oḷārikā sukhumā daṭṭhabbā."""
    g = AGG[a]["g"]
    spec = PAIR_ACC[(x, y)]
    how = spec[g] if spec else f"{ATTR[x]['acc'][GI[g]]} или {ATTR[y]['acc'][GI[g]]}"
    return f"Или же {AGG[a]['acc']} следует рассматривать как {how} в сравнении {SUCH_INS[g]} {AGG[a]['ins']}."


# ---------------------------------------------------------------- 6. comparison qualifiers (feeling … consciousness)
# number of a qualified noun phrase: pair compounds (kusalābyākatā …, sukhā ca adukkhamasukhā ca …) are plural
PRE = {  # prepositive: (sg_nom, sg_gen, pl_nom, pl_gen)
    "akusala": ("неблагое", "неблагого", "неблагие", "неблагих"),
    "kusala": ("благое", "благого", "благие", "благих"),
    "abyakata": ("этически неопределённое", "этически неопределённого", "этически неопределённые", "этически неопределённых"),
    "kusalabyakata": (None, None, "благие и этически неопределённые", "благих и этически неопределённых"),
    "akusalabyakata": (None, None, "неблагие и этически неопределённые", "неблагих и этически неопределённых"),
    "kusalakusala": (None, None, "благие и неблагие", "благих и неблагих"),
    "dukkha": ("болезненное", "болезненного", None, None),          # vedanā only
    "sukha": ("приятное", "приятного", None, None),                 # vedanā only
    "sukhadukkha": (None, None, "приятные и болезненные", "приятных и болезненных"),  # vedanā only
    "patigha": ("рождённое контактом соударения", "рождённого контактом соударения", None, None),          # saññā only
    "adhivacana": ("рождённое контактом наименования", "рождённого контактом наименования", None, None),  # saññā only
}
ADM = "которое ни болезненно, ни приятно"                       # adukkhamasukha  [pi-1 ^1-990]
FEEL_INS = {  # with sampayutta: связанн… с <…>
    "dukkha": "болезненным чувством",
    "sukha": "приятным чувством",
    "adm": "чувством, " + ADM,
    "sukha_adm": "приятным чувством и с чувством, " + ADM,
    "dukkha_adm": "болезненным чувством и с чувством, " + ADM,
    "sukhadukkha": "приятными и болезненными чувствами",
}
SAMAPANNA = {"asamapanna": "того, кто не вошёл в медитативное достижение",   # asamāpannassa [new]
             "samapanna": "того, кто вошёл в медитативное достижение"}       # samāpannassa  [pi-1 ^1-1289]
POSTADJ = {  # postposed: (sg_nom, sg_gen, pl_nom, pl_gen)
    "sasava": ("подверженное влечениям", "подверженного влечениям", "подверженные влечениям", "подверженных влечениям"),
    "anasava": ("свободное от влечений", "свободного от влечений", "свободные от влечений", "свободных от влечений"),
}
SP = ("связанное с", "связанного с", "связанные с", "связанных с")
PLURAL_Q = {"kusalabyakata", "akusalabyakata", "kusalakusala", "sukhadukkha", "sukha_adm", "dukkha_adm",
            "sp_sukha_adm", "sp_dukkha_adm", "sp_sukhadukkha"}


def np(a, q, case):
    """Noun phrase of aggregate a with qualifier q, case 'nom' | 'gen'.
    Returns (text, close) where close=True means a comma must close the phrase before a following verb."""
    pl = is_pl(a) or q in PLURAL_Q
    nom, gen = AGG[a]["pl"] if pl else AGG[a]["sg"]
    noun = nom if case == "nom" else gen
    k = (2 if pl else 0) + (0 if case == "nom" else 1)
    if q in PRE:
        return f"{PRE[q][k]} {noun}", False
    if q == "adm":  # vedanā only
        return f"{noun}, {ADM}", True
    if q in ("sukha_adm", "dukkha_adm"):  # vedanā only: sukhā ca adukkhamasukhā ca vedanā
        first = PRE[q.split("_")[0]][0 if case == "nom" else 1]
        sg_nom, sg_gen = AGG[a]["sg"]
        n1 = sg_nom if case == "nom" else sg_gen
        return f"{first} {n1} и {n1}, {ADM}", True
    if q in SAMAPANNA:
        return f"{noun} {SAMAPANNA[q]}", True
    if q in POSTADJ:
        return f"{noun}, {POSTADJ[q][k]}", True
    if q.startswith("sp_"):
        return f"{noun}, {SP[k]} {FEEL_INS[q[3:]]}", True
    raise KeyError(q)


def number_of(a, q):
    return "pl" if (is_pl(a) or q in PLURAL_Q) else "sg"


PRED = {  # predicate after the subject, sg / pl
    "olarika": ("является грубым", "являются грубыми"),
    "sukhuma": ("является тонким", "являются тонкими"),
    "hina": ("является низшим", "являются низшими"),
    "panita": ("является высшим", "являются высшими"),
    "dure": ("находится вдали от", "находятся вдали от"),
    "santike": ("находится вблизи", "находятся вблизи"),
}


def clause(a, subj_q, pred, obj_q=None, obj_close_comma=False):
    """'A является грубым' / 'A находится вдали от B'."""
    s, close = np(a, subj_q, "nom")
    p = PRED[pred][0 if number_of(a, subj_q) == "sg" else 1]
    out = s + ("," if close else "") + " " + p
    if obj_q is not None:
        o, oclose = np(a, obj_q, "gen")
        out += " " + o + ("," if (oclose and obj_close_comma) else "")
    return out


def comp_line(a, x, y, pairs):
    """Tattha katamā vedanā oḷārikā sukhumā? A oḷārikā, B sukhumā. … Taṃ taṃ vā pana … daṭṭhabbā."""
    sents = [cap(clause(a, s, x)) + ", " + clause(a, t, y) + "." for s, t in pairs]
    return f"{question_pair(a, x, y)} " + " ".join(sents) + " " + tail(a, x, y)


def relation_groups(a, rel, groups, ending):
    """groups: list of lists of (subj_q, obj_q); clauses inside a group joined by '; ', groups end with '.'.
    ending: 'dash' -> last clause + ' – это называется …'; 'sentence' -> '. Это называется …'."""
    out = []
    for gi, grp in enumerate(groups):
        last_group = gi == len(groups) - 1
        cl = []
        for ci, (s, o) in enumerate(grp):
            final = last_group and ci == len(grp) - 1
            cl.append(clause(a, s, rel, o, obj_close_comma=(final and ending == "dash")))
        txt = cap("; ".join(cl))
        if last_group and ending == "dash":
            out.append(txt + " " + DASH + " " + answer(a, rel) + ".")
        else:
            out.append(txt + ".")
    if ending == "sentence":
        out.append(cap(answer(a, rel)) + ".")
    return f"{question(a, rel)} " + " ".join(out)


# ---------------------------------------------------------------- 7. classification frames (Abhidhammabhājanīya)
HOW_MANY = {1: "по одному", 2: "на два вида", 3: "на три вида", 4: "на четыре вида", 5: "на пять видов",
            6: "на шесть видов", 7: "на семь видов", 8: "на восемь видов", 9: "на девять видов",
            10: "на десять видов", 11: "на одиннадцать видов"}  # [pi-1 headings, APPROVED «на N видов»]


def class_open(a, n):
    """Ekavidhena / Duvidhena … rūpakkhandho –"""
    return f"Классификация {AGG[a]['khandha_gen']} {HOW_MANY[n]} {DASH}"


def class_close(a, n):
    """Evaṃ ekavidhena … rūpakkhandho."""
    return f"Такова классификация {AGG[a]['khandha_gen']} {HOW_MANY[n]}."


# rūpa lists, pi-1 ^1-584 … ^1-593 (first letter lowered after the dash)  [pi-1]
RUPA_EKAVIDHA = (
    "вся материальная форма не является корнем; не имеет корней; не связана с корнями; имеет условия; "
    "является обусловленной; является материальной; является мирской; подвержена влечениям; подвержена оковам; "
    "подвержена узам; подвержена потокам; подвержена ярмам; подвержена помехам; затронута искажениями; "
    "служит объектом цепляния; подвержена омрачению; является этически неопределённой; не имеет объекта; "
    "не сопутствует уму; не связана с умом; не является результатом действий и не способна приносить результаты; "
    "является неомрачённой, но подверженной омрачению; не является явлением с направленной мыслью и удержанием мысли; "
    "не является явлением без направленной мысли, только с удержанием мысли; является явлением без направленной мысли "
    "и без удержания мысли; не сопровождается восторгом; не сопровождается счастьем; не сопровождается невозмутимостью; "
    "не устраняется ни видением истины, ни развитием ума; относится к явлениям, чьи корни не устраняются ни видением "
    "истины, ни развитием ума; не ведёт ни к накоплению, ни к убыванию; не относится ни к обучающимся, ни к завершившим "
    "обучение; является ограниченной; относится к миру чувственных желаний; не относится к миру форм; не относится к "
    "миру без форм; принадлежит к кругам существования; не относится к явлениям, не принадлежащим к кругам существования; "
    "является непредопределённой; не ведёт к освобождению; является возникшей; познаётся шестью видами сознания; "
    "является непостоянной; подвластна старению")
RUPA_DUKA = [  # pi-1 ^1-U1 lines 18-31 and 55 (each a full sentence there)
    "Есть материальная форма производная, есть материальная форма непроизводная.",
    "Есть материальная форма, охваченная цеплянием, есть материальная форма, не охваченная цеплянием.",
    "Есть материальная форма, охваченная цеплянием и служащая его объектом, есть материальная форма, не охваченная цеплянием, но служащая его объектом.",
    "Есть материальная форма видимая, есть материальная форма невидимая.",
    "Есть материальная форма, способная к соударению, есть материальная форма, не способная к соударению.",
    "Есть материальная форма, являющаяся способностью, есть материальная форма, не являющаяся способностью.",
    "Есть материальная форма, являющаяся великим элементом, есть материальная форма, не являющаяся великим элементом.",
    "Есть материальная форма, являющаяся внешним выражением, есть материальная форма, не являющаяся внешним выражением.",
    "Есть материальная форма, порождённая умом, есть материальная форма, не порождённая умом.",
    "Есть материальная форма, сосуществующая с умом, есть материальная форма, не сосуществующая с умом.",
    "Есть материальная форма, следующая за умом, есть материальная форма, не следующая за умом.",
    "Есть материальная форма, относящаяся к внутреннему, есть материальная форма, относящаяся к внешнему.",
    "Есть материальная форма грубая, есть материальная форма тонкая.",
    "Есть материальная форма вдали, есть материальная форма вблизи.",
]
RUPA_DUKA_FOOD = "Есть материальная форма, являющаяся съедаемой пищей, есть материальная форма, не являющаяся съедаемой пищей."
VAR_NUPADA = "[вариант написания (Sī., Ka.): nupādā]"
RUPAKANDA_NOTE = "(Как разобрано в разделе о материальной форме, так следует разбирать и здесь.)"  # (Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.)
RUPA_TIKA = [  # pi-1 ^1-585 lines 62-64 and 99: (internal half, external half)
    ("Материальная форма, относящаяся к внутреннему, является производной",
     "Материальная форма, относящаяся к внешнему, бывает производной, бывает непроизводной"),
    ("Материальная форма, относящаяся к внутреннему, охвачена цеплянием",
     "Материальная форма, относящаяся к внешнему, бывает охваченной цеплянием, бывает не охваченной цеплянием"),
    ("Материальная форма, относящаяся к внутреннему, охвачена цеплянием и служит его объектом",
     "Материальная форма, относящаяся к внешнему, бывает охваченной цеплянием и служащей его объектом, бывает не охваченной цеплянием, но служащей его объектом"),
]
RUPA_TIKA_FOOD = ("Материальная форма, относящаяся к внутреннему, не является съедаемой пищей",
                  "Материальная форма, относящаяся к внешнему, бывает съедаемой пищей, бывает не съедаемой пищей")
RUPA_CATU = [  # pi-1 ^1-586 lines 106-110: (derived half, underived half)
    ("Производная материальная форма бывает охваченной цеплянием, бывает не охваченной цеплянием",
     "Непроизводная материальная форма бывает охваченной цеплянием, бывает не охваченной цеплянием"),
    ("Производная материальная форма бывает охваченной цеплянием и служащей его объектом, бывает не охваченной цеплянием, но служащей его объектом",
     "Непроизводная материальная форма бывает охваченной цеплянием и служащей его объектом, бывает не охваченной цеплянием, но служащей его объектом"),
    ("Производная материальная форма бывает способной к соударению, бывает не способной к соударению",
     "Непроизводная материальная форма бывает способной к соударению, бывает не способной к соударению"),
    ("Производная материальная форма бывает грубой, бывает тонкой",
     "Непроизводная материальная форма бывает грубой, бывает тонкой"),
    ("Производная материальная форма бывает вдали, бывает вблизи",
     "Непроизводная материальная форма бывает вдали, бывает вблизи"),
]
RUPA_SEEN = "Материальная форма увиденная, услышанная, ощущённая, познанная"  # diṭṭhaṃ, sutaṃ, mutaṃ, viññātaṃ rūpaṃ  [pi-1]
RUPA_PANCA = "Элемент земли, элемент воды, элемент огня, элемент ветра и та материальная форма, которая является производной"
_K5 = ("Материальная форма, познаваемая глазом; материальная форма, познаваемая ухом; материальная форма, познаваемая носом; "
       "материальная форма, познаваемая языком; материальная форма, познаваемая телом")
RUPA_CHA = _K5 + "; материальная форма, познаваемая умом"
RUPA_SATTA = (_K5 + "; материальная форма, познаваемая элементом ума; "
              "материальная форма, познаваемая элементом умственного сознания")
RUPA_ATTHA = (_K5 + ", которая бывает доставляющей удовольствие при контакте, бывает болезненной при контакте; "
              "материальная форма, познаваемая элементом ума; материальная форма, познаваемая элементом умственного сознания")
_IND8 = ("Способность глаза, способность уха, способность носа, способность языка, способность тела, "
         "способность женственности, способность мужественности, жизненная способность")
RUPA_NAVA = _IND8 + " и та материальная форма, которая не является способностью"
RUPA_DASA = _IND8 + (" и материальная форма, не являющаяся способностью, которая бывает способной к соударению, "
                     "бывает не способной к соударению")
RUPA_EKADASA = ("Сфера глаза, сфера уха, сфера носа, сфера языка, сфера тела, сфера видимых форм, сфера звуков, "
                "сфера запахов, сфера вкусов, сфера осязаемого и та материальная форма, которая является невидимой "
                "и не способной к соударению и принадлежит к сфере объектов ума")
EKADASA_VAR_PI1 = " [вариант написания (Sī., Syā.): anidassanaṃ appaṭighaṃ]"  # pi-1 only; not in the pi-2 Pāli


def low(s):
    return s[:1].lower() + s[1:]


def halves(pairs):
    """pi-1 'A. B.' sentence pairs -> 'A; b' joined with '. ' (the Pāli joins the halves inside one sentence)."""
    return [f"{x}; {low(y)}" for x, y in pairs]


# ---------------------------------------------------------------- 8. the sample, line by line
def sample_lines():
    L = []
    add = L.append
    add("### " + CHAPTER_TITLES[1])
    add("#### " + SECTION_TITLES["Suttantabhājanīyaṃ"])
    add(FIVE_AGGREGATES + ".")
    # ---- rūpa
    a = "rupa"
    add("##### " + AGG[a]["heading"])
    add(khandha_def(a))
    for k in ("atita", "anagata", "paccuppanna"):
        add(time_line(a, k))
    for k in ("ajjhatta", "bahiddha"):
        add(self_line(a, k))
    add(f"{question(a, 'olarika')} {cap(EYE_TO_TOUCH)} {DASH} {answer(a, 'olarika')}.")
    add(f"{question(a, 'sukhuma')} {cap(FEMININITY_TO_FOOD)} {VAR_KABALIMKARO} {DASH} {answer(a, 'sukhuma')}.")
    add(f"{question(a, 'hina')} {cap(AGG[a]['nom'])}, {HINA_BODY}: {FIVE_OBJECTS} {DASH} {answer(a, 'hina')}.")
    add(f"{question(a, 'panita')} {cap(AGG[a]['nom'])}, {PANITA_BODY}: {FIVE_OBJECTS} {DASH} {answer(a, 'panita')}. "
        + tail(a, "hina", "panita"))
    add(f"{question(a, 'dure')} {cap(FEMININITY_TO_FOOD)}, {FAR_OTHER}, {DASH} {answer(a, 'dure')}.")
    add(f"{question(a, 'santike')} {cap(EYE_TO_TOUCH)}, {NEAR_OTHER}, {DASH} {answer(a, 'santike')}. "
        + tail(a, "dure", "santike"))

    # ---- vedanā … viññāṇa
    feel_pairs = [("akusala", "kusalabyakata"), ("kusalakusala", "abyakata"), ("dukkha", "sukha_adm"),
                  ("sukhadukkha", "adm"), ("asamapanna", "samapanna"), ("sasava", "anasava")]
    sp_pairs = [("akusala", "kusalabyakata"), ("kusalakusala", "abyakata"), ("sp_dukkha", "sp_sukha_adm"),
                ("sp_sukhadukkha", "sp_adm"), ("asamapanna", "samapanna"), ("sasava", "anasava")]
    g_eth = [("akusala", "kusalabyakata"), ("kusalabyakata", "akusala"), ("kusala", "akusalabyakata"),
             ("akusalabyakata", "kusala"), ("abyakata", "kusalakusala"), ("kusalakusala", "abyakata")]
    g_feel = [("dukkha", "sukha_adm"), ("sukha_adm", "dukkha"), ("sukha", "dukkha_adm"),
              ("dukkha_adm", "sukha"), ("adm", "sukhadukkha"), ("sukhadukkha", "adm")]
    g_sp = [("sp_dukkha", "sp_sukha_adm"), ("sp_sukha_adm", "sp_dukkha"), ("sp_sukha", "sp_dukkha_adm"),
            ("sp_dukkha_adm", "sp_sukha"), ("sp_adm", "sp_sukhadukkha"), ("sp_sukhadukkha", "sp_adm")]
    g_sam = [("asamapanna", "samapanna"), ("samapanna", "asamapanna")]
    g_sas = [("sasava", "anasava"), ("anasava", "sasava")]
    n_eth = [("akusala", "akusala"), ("kusala", "kusala"), ("abyakata", "abyakata")]
    n_feel = [("dukkha", "dukkha"), ("sukha", "sukha"), ("adm", "adm")]
    n_sp = [("sp_dukkha", "sp_dukkha"), ("sp_sukha", "sp_sukha"), ("sp_adm", "sp_adm")]
    n_sam = [("asamapanna", "asamapanna"), ("samapanna", "samapanna")]
    n_sas = [("sasava", "sasava"), ("anasava", "anasava")]

    for a in ("vedana", "sanna", "sankhara", "vinnana"):
        add("##### " + AGG[a]["heading"])
        add(khandha_def(a))
        for k in ("atita", "anagata", "paccuppanna"):
            add(time_line(a, k))
        for k in ("ajjhatta", "bahiddha"):
            add(self_line(a, k))
        if a == "vedana":
            pairs, far_g, near_g = feel_pairs, [g_eth, g_feel, g_sam, g_sas], [n_eth, n_feel, n_sam, n_sas]
        else:
            pairs = ([("patigha", "adhivacana")] if a == "sanna" else []) + sp_pairs
            if a == "sanna":  # the Pāli splits the ethical group after the fourth clause
                far_g = [g_eth[:4], g_eth[4:], g_sp, g_sam, g_sas]
            else:
                far_g = [g_eth, g_sp, g_sam, g_sas]
            near_g = [n_eth, n_sp, n_sam, n_sas]
        add(comp_line(a, "olarika", "sukhuma", pairs))
        add(comp_line(a, "hina", "panita", pairs))
        far_end = "sentence" if a == "sankhara" else "dash"
        near_end = "dash" if a == "vinnana" else "sentence"
        add(relation_groups(a, "dure", far_g, far_end))
        add(relation_groups(a, "santike", near_g, near_end) + " " + tail(a, "dure", "santike"))
    add(SECTION_TITLES["Suttantabhājanīyaṃ"] + ".")

    # ---- Abhidhammabhājanīya
    add("#### " + SECTION_TITLES["Abhidhammabhājanīyaṃ"])
    add(FIVE_AGGREGATES + ".")
    a = "rupa"
    add("##### " + AGG[a]["heading"])
    add(f"{khandha_question(a)} {class_open(a, 1)} {RUPA_EKAVIDHA}. {class_close(a, 1)}")
    duka = [low(RUPA_DUKA[0][:-1]) + " " + VAR_NUPADA + "."] + RUPA_DUKA[1:-1] + [RUPA_DUKA[-1][:-1] + "… " + low(RUPA_DUKA_FOOD)]
    add(f"{class_open(a, 2)} " + " ".join(duka) + f" {class_close(a, 2)}")
    add(RUPAKANDA_NOTE)
    t = halves(RUPA_TIKA)
    tika = low(". ".join(t)) + "… " + low(halves([RUPA_TIKA_FOOD])[0]) + "."
    add(f"{class_open(a, 3)} {tika} {class_close(a, 3)}")
    c = halves(RUPA_CATU)
    catu = low(". ".join(c)) + "… " + low(RUPA_SEEN) + "."
    add(f"{class_open(a, 4)} {catu} {class_close(a, 4)}")
    for n, s in ((5, RUPA_PANCA), (6, RUPA_CHA), (7, RUPA_SATTA), (8, RUPA_ATTHA), (9, RUPA_NAVA),
                 (10, RUPA_DASA), (11, RUPA_EKADASA)):
        add(f"{class_open(a, n)} {low(s)}. {class_close(a, n)}")
    add(cap(khandha_answer(a)) + ".")
    return L


# ---------------------------------------------------------------- 9. checks against pi-1 and writing
def pi1_text():
    out = []
    for fn in sorted(os.listdir(PI1_RU_DIR)):
        if fn.endswith(".md"):
            out.append(open(os.path.join(PI1_RU_DIR, fn), encoding="utf-8").read())
    return "\n".join(out)


def assert_pi1():
    t = pi1_text()
    must = [HOMAGE, "# " + PITAKA, FIVE_AGGREGATES, TIME["atita"]["pl"], TIME["anagata"]["pl"],
            TIME["paccuppanna"]["pl"], cap(MAHABHUTA), cap(EYE_TO_TOUCH), cap(FEMININITY_TO_FOOD),
            "которые у тех или иных существ находятся внутри себя, являются собственными, ",
            "которые у тех или иных других существ, других личностей находятся внутри себя, являются собственными, ",
            "индивидуальными и охваченными цеплянием", "чувство, " + ADM, SAMAPANNA["samapanna"],
            "– это называется всей материальной формой", "Что такое здесь вся материальная форма?",
            "Раздел о материальной форме", "Классификация материальной формы на два вида –",
            "Такова классификация материальной формы по одному.", "явления, связанные с приятным чувством",
            "подверженные влечениям", "свободные от влечений", "рождённого контактом глаза чувства",
            RUPA_DUKA_FOOD, RUPA_SEEN + ".", RUPA_PANCA + ".", RUPA_CHA + ".", RUPA_SATTA + ".",
            RUPA_ATTHA + ".", RUPA_NAVA + ".", RUPA_DASA + ".",
            RUPA_EKADASA.replace("не способной к соударению и", "не способной к соударению" + EKADASA_VAR_PI1 + " и") + "."]
    must += RUPA_DUKA
    must += [f"{x}. {y}." for x, y in RUPA_TIKA + [RUPA_TIKA_FOOD] + RUPA_CATU]
    eka = cap(RUPA_EKAVIDHA).replace("является материальной;", "является материальной [вариант чтения (Sī.): rūpiyaṃ];")
    must.append(eka + ".")
    for w in ("зрительное сознание", "слуховое сознание", "обонятельное сознание", "вкусовое сознание",
              "осязательное сознание", "умственного сознания", "видимых форм", "сфера звуков", "сфера запахов",
              "сфера вкусов", "сфера осязаемого"):
        must.append(w)
    missing = [m for m in must if m not in t]
    assert not missing, "pi-1 strings not found: " + " | ".join(m[:80] for m in missing)


def attach_ids(pali_lines, ru_lines):
    out, i = [], 0
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        ru = ru_lines[i]
        i += 1
        m = ID.search(pl)
        out.append(ru + (" " + m.group(1) if m else ""))
    assert i == len(ru_lines), (i, len(ru_lines))
    return out


def write(path, lines):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip("\n") + "\n")


def main():
    assert_pi1()
    # preamble
    pre_p = open(os.path.join(PALI_DIR, "preamble.md"), encoding="utf-8").read().rstrip("\n").split("\n")
    pre_ru = [HOMAGE, "# " + PITAKA, "## " + BOOK_TITLE]
    write(os.path.join(RU_DIR, "preamble.md"), attach_ids(pre_p, pre_ru))
    # sample
    pali = open(os.path.join(HERE, "ch1-sample-pali.md"), encoding="utf-8").read().rstrip("\n").split("\n")
    ru = sample_lines()
    nonempty = [l for l in pali if l.strip()]
    assert len(ru) == len(nonempty), (len(ru), len(nonempty))
    for p, r in zip(nonempty, ru):  # dash count per line
        assert p.count(DASH) + p.count("—") == r.count(DASH), (p[:60], r[:60])
    write(os.path.join(HERE, "ch1-sample.md"), attach_ids(pali, ru))
    print("OK: preamble + ch1-sample.md,", len(ru), "non-empty lines")


if __name__ == "__main__":
    main()
