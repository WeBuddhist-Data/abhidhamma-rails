"""Builder for the Russian rails SAMPLE of pi-2 (Vibhaṅga, plain audience).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/preamble.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/sample-1/1-sample.md   (chapter 1 through ^2-33, line-aligned with
                                                             0-INBOX/temp/pipeline/pi-2-ru/ch1-sample-pali.md)
  0-INBOX/temp/pipeline/pi-2-ru/rails/ru-rails-formulas.md

All Russian comes from the fixed strings and functions below, so identical Pāli gives byte-identical Russian.
Terms follow the locked termbase AI_translation/russian/pi-2-pali-russian-termbase-plain.md (+ termbase/APPROVED.md);
sentence shapes follow the approved pi-1 Russian rails (main() asserts that every PI1 string still occurs there).
Later chapter agents import this module read-only; importing writes nothing:
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-2-ru\\rails")
    import build_rails_sample_ru as S

usage: python -I -X utf8 build_rails_sample_ru.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"
OUT = ROOT / "AI_translation" / "russian" / "pi-2-russian-plain-rails_split_chapters"
RAILS = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-2-ru" / "rails"
SAMPLE = RAILS / "sample-1"
SAMPLE_PALI = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-2-ru" / "ch1-sample-pali.md"
PI1_RU = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def cap(s):
    return s[0].upper() + s[1:]


# =========================================================================== book frame and headings
NAMO = "Почтение Благословенному, Достойному, Полностью Пробуждённому Будде"  # PI1
PITAKA = "В корзине Абхидхаммы"                                                  # PI1
BOOK = "Подробный разбор"                                                         # user-approved title
CH_TITLE = {  # ### <X>vibhaṅgo (user-approved chapter headings)
    1: ("Khandhavibhaṅgo", "Разбор совокупностей"),
    2: ("Āyatanavibhaṅgo", "Разбор сфер восприятия"),
    3: ("Dhātuvibhaṅgo", "Разбор элементов"),
    4: ("Saccavibhaṅgo", "Разбор истин"),
    5: ("Indriyavibhaṅgo", "Разбор способностей"),
    6: ("Paṭiccasamuppādavibhaṅgo", "Разбор возникновения в зависимости от условий"),
    7: ("Satipaṭṭhānavibhaṅgo", "Разбор основ осознанности"),
    8: ("Sammappadhānavibhaṅgo", "Разбор правильных усилий"),
    9: ("Iddhipādavibhaṅgo", "Разбор основ сверхспособностей"),
    10: ("Bojjhaṅgavibhaṅgo", "Разбор факторов пробуждения"),
    11: ("Maggaṅgavibhaṅgo", "Разбор факторов пути"),
    12: ("Jhānavibhaṅgo", "Разбор медитативных погружений"),
    13: ("Appamaññāvibhaṅgo", "Разбор безмерных состояний"),
    14: ("Sikkhāpadavibhaṅgo", "Разбор правил обучения"),
    15: ("Paṭisambhidāvibhaṅgo", "Разбор аналитических знаний"),
    16: ("Ñāṇavibhaṅgo", "Разбор знания"),
    17: ("Khuddakavatthuvibhaṅgo", "Разбор малых тем"),
    18: ("Dhammahadayavibhaṅgo", "Разбор сути явлений"),
}
DONE = "завершён"                      # <X>vibhaṅgo niṭṭhito. = «<title> завершён.» (pi-1 pattern «… завершён.»)
SUTTANTA_BH = "Разбор по наставлениям"  # #### Suttantabhājanīyaṃ (Suttanta «наставления» + bhājanīyaṃ «разбор»)
ABHI_BH = "Разбор по Абхидхамме"        # #### Abhidhammabhājanīyaṃ
PANHA = "Раздел вопросов"               # #### Pañhāpucchakaṃ (termbase)
TIKA_H, DUKA_H = "Тройки", "Пары"       # ##### Tikaṃ / Dukaṃ in Pañhāpucchaka (termbase)
TATTHA = "здесь"                        # Tattha (termbase), as pi-1 «Что такое здесь вся материальная форма?»

# =========================================================================== aggregates
ORDER = ["rupa", "vedana", "sanna", "sankhara", "vinnana"]
KH = {  # nominative; instrumental = «совокупностью …»
    "rupa": "совокупность материальной формы",
    "vedana": "совокупность чувств",
    "sanna": "совокупность восприятия",
    "sankhara": "совокупность формирующих факторов",
    "vinnana": "совокупность сознания",
}


def kh_ins(k):
    return KH[k].replace("совокупность", "совокупностью", 1)


FIVE_LIST = ("совокупность материальной формы, совокупность чувств, совокупность восприятия, "
             "совокупность формирующих факторов и совокупность сознания")             # PI1 ^1-1089
FIVE = f"Пять совокупностей – {FIVE_LIST}."                                         # PI1 ^1-1089 «Пять совокупностей – …»

# gender: f (материальная форма), n (чувство, восприятие, сознание), p (формирующие факторы, always plural)
G = {"rupa": "f", "vedana": "n", "sanna": "n", "sankhara": "p", "vinnana": "n"}
NOUN = {  # nom, ins, acc, «с тем или иным X» (comparison)
    "rupa": ("материальная форма", "материальной формой", "материальную форму", "с той или иной материальной формой"),
    "vedana": ("чувство", "чувством", "чувство", "с тем или иным чувством"),
    "sanna": ("восприятие", "восприятием", "восприятие", "с тем или иным восприятием"),
    "sankhara": ("формирующие факторы", "формирующими факторами", "формирующие факторы",
                 "с теми или иными формирующими факторами"),
    "vinnana": ("сознание", "сознанием", "сознание", "с тем или иным сознанием"),
}
# attribute adjectives: nom f/n/p, ins f/n/p, acc f/n/p
ADJ = {
    "atita": ("прошлая", "прошлое", "прошлые", "прошлой", "прошлым", "прошлыми"),
    "anagata": ("будущая", "будущее", "будущие", "будущей", "будущим", "будущими"),
    "paccuppanna": ("настоящая", "настоящее", "настоящие", "настоящей", "настоящим", "настоящими"),
    "ajjhatta": ("внутренняя", "внутреннее", "внутренние", "внутренней", "внутренним", "внутренними"),
    "bahiddha": ("внешняя", "внешнее", "внешние", "внешней", "внешним", "внешними"),
    "olarika": ("грубая", "грубое", "грубые", "грубой", "грубым", "грубыми", "грубую"),
    "sukhuma": ("тонкая", "тонкое", "тонкие", "тонкой", "тонким", "тонкими", "тонкую"),
    "hina": ("низшая", "низшее", "низшие", "низшей", "низшим", "низшими", "низшую"),
    "panita": ("высшая", "высшее", "высшие", "высшей", "высшим", "высшими", "высшую"),
    "dure": ("находящаяся вдали", "находящееся вдали", "находящиеся вдали",
             "находящейся вдали", "находящимся вдали", "находящимися вдали", "находящуюся вдали"),
    "santike": ("находящаяся вблизи", "находящееся вблизи", "находящиеся вблизи",
                "находящейся вблизи", "находящимся вблизи", "находящимися вблизи", "находящуюся вблизи"),
}
GI = {"f": 0, "n": 1, "p": 2}
POSTPOSED = {"dure", "santike"}  # «материальная форма, находящаяся вдали» (pi-1 ^1-676)


def adj(a, k, case="nom"):
    g = GI[G[k]]
    if case == "nom":
        return ADJ[a][g]
    if case == "ins":
        return ADJ[a][3 + g]
    return ADJ[a][6] if g == 0 else ADJ[a][g]  # acc: only feminine differs from nom


def attr_np(a, k, case="nom"):
    """noun phrase «прошлая материальная форма» / «чувство, находящееся вдали» in nom or ins."""
    n = NOUN[k][0 if case == "nom" else 1]
    if a in POSTPOSED:
        return f"{n}, {adj(a, k, case)}"
    return f"{adj(a, k, case)} {n}"


def what_q(a, k):
    """Tattha katamaṃ rūpaṃ atītaṃ? = Что такое здесь прошлая материальная форма?"""
    return f"Что такое {TATTHA} {attr_np(a, k)}?"


def called(a, k):
    """idaṃ/ayaṃ vuccati X / ime vuccanti X = это называется X(ins)."""
    return f"это называется {attr_np(a, k, 'ins')}."


# --- the aggregate formula (Suttantabhājanīya opening of each aggregate)
AGG_BODY = {
    "f": ("Любая {n}, прошлая, будущая или настоящая, внутренняя или внешняя, грубая или тонкая, низшая или высшая, "
          "находящаяся вдали или вблизи, вся вместе, собранная воедино и обобщённая,"),
    "n": ("Любое {n}, прошлое, будущее или настоящее, внутреннее или внешнее, грубое или тонкое, низшее или высшее, "
          "находящееся вдали или вблизи, всё вместе, собранное воедино и обобщённое,"),
    "p": ("Любые {n}, прошлые, будущие или настоящие, внутренние или внешние, грубые или тонкие, низшие или высшие, "
          "находящиеся вдали или вблизи, все вместе, собранные воедино и обобщённые,"),
}


def agg_formula(k):
    """Yaṃ kiñci rūpaṃ / Yā kāci vedanā / Ye keci saṅkhārā … tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā"""
    return AGG_BODY[G[k]].format(n=NOUN[k][0])


def agg_q(k):
    """Tattha katamo rūpakkhandho? = Что такое здесь совокупность материальной формы?"""
    return f"Что такое {TATTHA} {KH[k]}?"


def agg_segment(k):
    return f"{agg_q(k)} {agg_formula(k)} – это называется {kh_ins(k)}."


# --- members listed after the comma (Pāli «, X Y Z – idaṃ vuccati …»), introduced by «:»
MAHABHUTA = "четыре великих элемента и материальная форма, производная от четырёх великих элементов"  # PI1 ^1-584 (capital there)
FEEL3 = "приятное чувство, болезненное чувство и чувство, которое ни болезненно, ни приятно"  # sukhā vedanā dukkhā vedanā adukkhamasukhā vedanā
SENSES = ["глаза", "уха", "носа", "языка", "тела", "ума"]


def contact_list(x):
    """cakkhusamphassajā X … manosamphassajā X = рождённое контактом глаза X, …"""
    items = [f"рождённое контактом {s} {x}" for s in SENSES]
    return ", ".join(items[:-1]) + " и " + items[-1]


VINNANA6 = "зрительное сознание, слуховое сознание, обонятельное сознание, вкусовое сознание, осязательное сознание и умственное сознание"
MEMBERS = {  # (text, needs a comma before the dash: the list ends in a participial/relative clause)
    "rupa": (MAHABHUTA, True),
    "vedana": (FEEL3, True),
    "sanna": (contact_list("восприятие"), False),
    "sankhara": (contact_list("намерение"), False),
    "vinnana": (VINNANA6, False),
}


def close_members(k, members=None):
    text, comma = MEMBERS[k] if members is None else members
    return f"{text}{',' if comma else ''}"


# --- past / future / present (PI1 ^1-1044/1045/1046 plural strings; f and n inflected from them)
TIME_STR = {
    "atita": {  # atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ uppajjitvā vigataṃ atītaṃ atītaṃsena saṅgahitaṃ
        "f": "прошлая, прекратившаяся, исчезнувшая, изменившаяся, угасшая, полностью угасшая, исчезнувшая после возникновения, прошлая, включённая в категорию прошлых",
        "n": "прошлое, прекратившееся, исчезнувшее, изменившееся, угасшее, полностью угасшее, исчезнувшее после возникновения, прошлое, включённое в категорию прошлых",
        "p": "прошлые, прекратившиеся, исчезнувшие, изменившиеся, угасшие, полностью угасшие, исчезнувшие после возникновения, прошлые, включённые в категорию прошлых",
    },
    "anagata": {  # ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ anuppannaṃ asamuppannaṃ anuṭṭhitaṃ asamuṭṭhitaṃ anāgataṃ anāgataṃsena saṅgahitaṃ
        "f": "нерождённая, неставшая, незародившаяся, непоявившаяся, не появившаяся полностью, непроявившаяся, невозникшая, не возникшая полностью, неподнявшаяся, не поднявшаяся полностью, будущая, включённая в категорию будущих",
        "n": "нерождённое, неставшее, незародившееся, непоявившееся, не появившееся полностью, непроявившееся, невозникшее, не возникшее полностью, неподнявшееся, не поднявшееся полностью, будущее, включённое в категорию будущих",
        "p": "нерождённые, неставшие, незародившиеся, непоявившиеся, не появившиеся полностью, непроявившиеся, невозникшие, не возникшие полностью, неподнявшиеся, не поднявшиеся полностью, будущие, включённые в категорию будущих",
    },
    "paccuppanna": {  # jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ uppannaṃ samuppannaṃ uṭṭhitaṃ samuṭṭhitaṃ paccuppannaṃ paccuppannaṃsena saṅgahitaṃ
        "f": "рождённая, ставшая, зародившаяся, появившаяся, полностью появившаяся, проявившаяся, возникшая, полностью возникшая, поднявшаяся, полностью поднявшаяся, настоящая, включённая в категорию настоящих",
        "n": "рождённое, ставшее, зародившееся, появившееся, полностью появившееся, проявившееся, возникшее, полностью возникшее, поднявшееся, полностью поднявшееся, настоящее, включённое в категорию настоящих",
        "p": "рождённые, ставшие, зародившиеся, появившиеся, полностью появившиеся, проявившиеся, возникшие, полностью возникшие, поднявшиеся, полностью поднявшиеся, настоящие, включённые в категорию настоящих",
    },
}
TIME = ["atita", "anagata", "paccuppanna"]


def time_sentence(k, t, members=None):
    """Tattha katamaṃ rūpaṃ atītaṃ? Yaṃ rūpaṃ atītaṃ … atītaṃsena saṅgahitaṃ, <members> – idaṃ vuccati rūpaṃ atītaṃ."""
    return (f"{what_q(t, k)} {cap(NOUN[k][0])}, {TIME_STR[t][G[k]]}: "
            f"{close_members(k, members)} – {called(t, k)}")


# --- internal / external (ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ)
OWN_ATTR = {  # instrumental after «является/являются»; ajjhattaṃ = «внутренний» (pi-2 APPROVED; pi-1 «внутри себя»)
    "f": "внутренней, собственной, закреплённой, индивидуальной и охваченной цеплянием",
    "n": "внутренним, собственным, закреплённым, индивидуальным и охваченным цеплянием",
    "p": "внутренними, собственными, закреплёнными, индивидуальными и охваченными цеплянием",
}
REL = {"f": ("которая", "является"), "n": ("которое", "является"), "p": ("которые", "являются")}
BEINGS = "у тех или иных существ"                                 # tesaṃ tesaṃ sattānaṃ (PI1 ^1-1050)
OTHER_BEINGS = "у тех или иных других существ, других личностей"  # tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ (PI1 ^1-1051)


def own_sentence(k, external, members=None):
    a = "bahiddha" if external else "ajjhatta"
    rel, verb = REL[G[k]]
    who = OTHER_BEINGS if external else BEINGS
    return (f"{what_q(a, k)} {cap(NOUN[k][0])}, {rel} {who} {verb} {OWN_ATTR[G[k]]}: "
            f"{close_members(k, members)} – {called(a, k)}")


# --- comparison sentence: Taṃ taṃ vā pana X upādāyupādāya X … daṭṭhabbaṃ/daṭṭhabbā.
def compare(k, a, b):
    """= Или же X следует рассматривать как A или B в сравнении с тем или иным X."""
    return (f"Или же {NOUN[k][2]} следует рассматривать как {adj(a, k, 'acc')} или {adj(b, k, 'acc')} "
            f"в сравнении {NOUN[k][3]}.")


def compare_far(k):
    """… dūre santike daṭṭhabbaṃ = как находящуюся вдали или вблизи (one participle)"""
    part = adj("dure", k, "acc").replace(" вдали", "")
    return f"Или же {NOUN[k][2]} следует рассматривать как {part} вдали или вблизи в сравнении {NOUN[k][3]}."


# --- rūpa: coarse/subtle, inferior/superior, far/near (Suttantabhājanīya)
EYE_TO_TOUCH = "сфера глаза… сфера осязаемого"           # Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ (PI1 ^1-674)
FOOD_VAR = "[вариант написания (Sī., Syā.): kabaḷiṃkāro]"


def fem_to_food(variant=False):
    """Itthindriyaṃ…pe… kabaḷīkāro [variant] āhāro (PI1 ^1-675)"""
    v = f" {FOOD_VAR}" if variant else ""
    return f"способность женственности… съедаемая{v} пища"


SENSE_OBJECTS = "видимые формы, звуки, запахи, вкусы и осязаемое"  # rūpā saddā gandhā rasā phoṭṭhabbā
FOR_BEINGS = "для тех или иных существ"                            # tesaṃ tesaṃ sattānaṃ (with the two strings below)
HINA_STR = ("пренебрежённой, презренной, осмеянной, униженной, неуважаемой, низшей, считающейся низшей, "
            "признанной низшей, нежеланной, немилой, неприятной")
# uññātaṃ avaññātaṃ hīḷitaṃ paribhūtaṃ acittīkataṃ hīnaṃ hīnamataṃ hīnasammataṃ aniṭṭhaṃ akantaṃ amanāpaṃ
PANITA_STR = ("не пренебрежённой, не презренной, не осмеянной, не униженной, уважаемой, высшей, считающейся высшей, "
              "признанной высшей, желанной, милой, приятной")
# anuññātaṃ anavaññātaṃ ahīḷitaṃ aparibhūtaṃ cittīkataṃ paṇītaṃ paṇītamataṃ paṇītasammataṃ iṭṭhaṃ kantaṃ manāpaṃ
OR_OTHER = "или же какая бы другая материальная форма ни находилась"   # yaṃ vā panaññampi atthi rūpaṃ (PI1 ^1-652 frame)
FAR_STR = "не рядом, не поблизости, вдали, не вблизи"                 # anāsanne anupakaṭṭhe dūre asantike
NEAR_STR = "рядом, поблизости, недалеко, вблизи"                      # āsanne upakaṭṭhe avidūre santike


def rupa_line(a, body, comma=False):
    return f"{what_q(a, 'rupa')} {body}{',' if comma else ''} – {called(a, 'rupa')}"


# --- qualifiers for vedanā / saññā / saṅkhārā / viññāṇa (all neuter nouns or the plural saṅkhārā)
NOUN4 = {  # nom.sg, nom.pl, gen.sg, gen.pl
    "vedana": ("чувство", "чувства", "чувства", "чувств"),
    "sanna": ("восприятие", "восприятия", "восприятия", "восприятий"),
    "sankhara": (None, "формирующие факторы", None, "формирующих факторов"),
    "vinnana": ("сознание", "виды сознания", "сознания", "видов сознания"),  # viññāṇā (pl) = «виды сознания» (termbase viññāṇehi)
}
PRE = {  # pre-posed adjectives: nom.sg (n), nom.pl, gen.sg, gen.pl
    "akusala": ("неблагое", "неблагие", "неблагого", "неблагих"),
    "kusala": ("благое", "благие", "благого", "благих"),
    "abyakata": ("этически неопределённое", "этически неопределённые", "этически неопределённого", "этически неопределённых"),
    "kusalabyakata": (None, "благие и этически неопределённые", None, "благих и этически неопределённых"),
    "kusalakusala": (None, "благие и неблагие", None, "благих и неблагих"),
    "akusalabyakata": (None, "неблагие и этически неопределённые", None, "неблагих и этически неопределённых"),
    "patigha": ("рождённое контактом соударения", None, None, None),      # paṭighasamphassajā
    "adhivacana": ("рождённое контактом наименования", None, None, None),  # adhivacanasamphassajā
}
PRE_FEEL = {  # vedanā itself: dukkhā / sukhā / sukhadukkhā vedanā
    "dukkha": ("болезненное", "болезненные", "болезненного", "болезненных"),
    "sukha": ("приятное", "приятные", "приятного", "приятных"),
    "sukhadukkha": (None, "приятные и болезненные", None, "приятных и болезненных"),
}
END = ("ое", "ые", "ого", "ых")  # n.sg nom, pl nom, n.sg gen, pl gen of the post-posed participles
ADM = "чувство, которое ни болезненно, ни приятно"        # adukkhamasukhā vedanā (PI1 «чувство, которое ни болезненно, ни приятно»)
ADM_GEN = "чувства, которое ни болезненно, ни приятно"
ADM_INS = "чувством, которое ни болезненно, ни приятно"
POST = {  # post-posed phrases, stem + END
    "sasava": ("подверженн", " влечениям"),
    "anasava": ("свободн", " от влечений"),
    "dukkha": ("связанн", " с болезненным чувством"),
    "sukha": ("связанн", " с приятным чувством"),
    "adm": ("связанн", f" с {ADM_INS}"),
    "sukhadukkha": ("связанн", " с приятными и болезненными чувствами"),
    "sukha+adm": ("связанн", f" с приятным чувством и с {ADM_INS}"),
    "dukkha+adm": ("связанн", f" с болезненным чувством и с {ADM_INS}"),
}
SAM = "того, кто вошёл в медитативное достижение"         # samāpannassa (termbase; PI1 ^1-1289)
ASAM = "того, кто не вошёл в медитативное достижение"     # asamāpannassa
SLOT = {("s", "nom"): 0, ("p", "nom"): 1, ("s", "gen"): 2, ("p", "gen"): 3}


def np(k, q, num, case="nom"):
    """Noun phrase for aggregate k, qualifier q, number 's'/'p', case nom/gen.
    Returns (text, postposed): postposed phrases take a closing comma when the sentence goes on."""
    if k == "sankhara":
        num = "p"
    i = SLOT[(num, case)]
    noun = NOUN4[k][i]
    if k == "vedana" and q == "adm":
        return (ADM if case == "nom" else ADM_GEN), True
    if k == "vedana" and q in ("sukha+adm", "dukkha+adm"):
        first = PRE_FEEL[q.split("+")[0]]
        if case == "nom":
            return f"{first[0]} чувство и {ADM}", True
        return f"{first[2]} чувства и от {ADM_GEN}", True
    if k == "vedana" and q in PRE_FEEL:
        return f"{PRE_FEEL[q][i]} {noun}", False
    if q in PRE:
        return f"{PRE[q][i]} {noun}", False
    if q == "sam":
        return f"{noun} {SAM}", True
    if q == "asam":
        return f"{noun} {ASAM}", True
    stem, tail = POST[q]
    return f"{noun}, {stem}{END[i]}{tail}", True


PRED = {"olarika": ("грубое", "грубые"), "sukhuma": ("тонкое", "тонкие"),
        "hina": ("низшее", "низшие"), "panita": ("высшее", "высшие")}


def pnum(k, num):
    return "p" if (k == "sankhara" or num == "p") else "s"


def pair_sentence(k, a, na, b, nb, x, y):
    """A x, B y.  e.g. Akusalā vedanā oḷārikā, kusalābyākatā vedanā sukhumā."""
    ta, pa = np(k, a, na)
    tb, pb = np(k, b, nb)
    px = PRED[x][0 if pnum(k, na) == "s" else 1]
    py = PRED[y][0 if pnum(k, nb) == "s" else 1]
    return f"{cap(ta)}{',' if pa else ''} {px}, а {tb}{',' if pb else ''} {py}."


def which_q(k, x, y):
    """Tattha katamā vedanā oḷārikā sukhumā? = Какое здесь чувство грубое, а какое тонкое?"""
    if k == "sankhara":
        return f"Какие {TATTHA} формирующие факторы {PRED[x][1]}, а какие {PRED[y][1]}?"
    return f"Какое {TATTHA} {NOUN4[k][0]} {PRED[x][0]}, а какое {PRED[y][0]}?"


def coarse_segment(k, pairs, x, y):
    return " ".join([which_q(k, x, y)] + [pair_sentence(k, a, na, b, nb, x, y) for a, na, b, nb in pairs]
                    + [compare(k, x, y)])


def is_verb(k, num):
    return "находятся" if pnum(k, num) == "p" else "находится"


def far_clause(k, a, na, b, nb):
    """A B-ehi/-āya dūre = A находится вдали от B"""
    ta, pa = np(k, a, na)
    tb, pb = np(k, b, nb, "gen")
    return f"{ta}{',' if pa else ''} {is_verb(k, na)} вдали от {tb}", pb


def near_clause(k, a):
    """A A-āya/-ānaṃ/-assa santike = A находится вблизи A(gen)"""
    ta, pa = np(k, a, "s")
    tb, pb = np(k, a, "s", "gen")
    return f"{ta}{',' if pa else ''} {is_verb(k, 's')} вблизи {tb}", pb


def _join(clauses):
    """clauses: list of groups (each a list of (text, postposed)); returns body text and the last post flag."""
    sents = []
    for g in clauses:
        s = "; ".join(t for t, _ in g)
        sents.append(cap(s))
    return ". ".join(sents), clauses[-1][-1][1]


def far_line(k, groups, dash_close):
    body, post = _join([[far_clause(k, *p) for p in g] for g in groups])
    if dash_close:
        return f"{what_q('dure', k)} {body}{',' if post else ''} – {called('dure', k)}"
    return f"{what_q('dure', k)} {body}. {cap(called('dure', k))}"


NEAR_GROUPS = [["akusala", "kusala", "abyakata"], ["dukkha", "sukha", "adm"], ["asam", "sam"], ["sasava", "anasava"]]


def near_line(k, dash_close, closing=True):
    body, post = _join([[near_clause(k, a) for a in g] for g in NEAR_GROUPS])
    end = f" {compare_far(k)}" if closing else ""
    if dash_close:
        return f"{what_q('santike', k)} {body}{',' if post else ''} – {called('santike', k)}{end}"
    return f"{what_q('santike', k)} {body}. {cap(called('santike', k))}{end}"


# pair lists (number per side follows the Pāli; the viññāṇa section shows it explicitly)
BASE_PAIRS = [("akusala", "s", "kusalabyakata", "p"), ("kusalakusala", "p", "abyakata", "s"),
              ("dukkha", "s", "sukha+adm", "p"), ("sukhadukkha", "p", "adm", "s"),
              ("asam", "s", "sam", "s"), ("sasava", "s", "anasava", "s")]
COARSE_PAIRS = {"vedana": BASE_PAIRS, "sanna": [("patigha", "s", "adhivacana", "s")] + BASE_PAIRS,
                "sankhara": BASE_PAIRS, "vinnana": BASE_PAIRS}
HINA_PAIRS = {k: BASE_PAIRS for k in ("vedana", "sanna", "sankhara", "vinnana")}
FAR_KUSALA = [("akusala", "s", "kusalabyakata", "p"), ("kusalabyakata", "p", "akusala", "s"),
              ("kusala", "s", "akusalabyakata", "p"), ("akusalabyakata", "p", "kusala", "s"),
              ("abyakata", "s", "kusalakusala", "p"), ("kusalakusala", "p", "abyakata", "s")]
FAR_FEEL = [("dukkha", "s", "sukha+adm", "p"), ("sukha+adm", "p", "dukkha", "s"),
            ("sukha", "s", "dukkha+adm", "p"), ("dukkha+adm", "p", "sukha", "s"),
            ("adm", "s", "sukhadukkha", "p"), ("sukhadukkha", "p", "adm", "s")]
FAR_SAM = [("asam", "s", "sam", "s"), ("sam", "s", "asam", "s")]
FAR_SASAVA = [("sasava", "s", "anasava", "s"), ("anasava", "s", "sasava", "s")]


def far_groups(k):
    if k == "sanna":  # the saññā section breaks the kusala clauses into two Pāli sentences
        return [FAR_KUSALA[:4], FAR_KUSALA[4:], FAR_FEEL, FAR_SAM, FAR_SASAVA]
    return [FAR_KUSALA, FAR_FEEL, FAR_SAM, FAR_SASAVA]


# =========================================================================== Abhidhammabhājanīya
NUMW = {1: "по одному", 2: "на два вида", 3: "на три вида", 4: "на четыре вида", 5: "на пять видов",
        6: "на шесть видов", 7: "на семь видов", 8: "на восемь видов", 9: "на девять видов",
        10: "на десять видов", 11: "на одиннадцать видов"}  # N-vidhena (termbase; user: no «классификация»)


def vidha(n, k):
    """<N>vidhena <aggregate> – = Совокупность … на N видов –"""
    return f"{cap(KH[k])} {NUMW[n]} –"


def vidha_end(n, k):
    """Evaṃ <N>vidhena <aggregate>. = Такова совокупность … на N видов."""
    return f"Такова {KH[k]} {NUMW[n]}."


RUPA_EKAVIDHA = (  # PI1 ^1-584 (sabbaṃ rūpaṃ na hetu … jarābhibhūtaṃ), without pi-1's [rūpiyaṃ] variant
    "вся материальная форма не является корнем; не имеет корней; не связана с корнями; имеет условия; "
    "является обусловленной; является материальной; является мирской; подвержена влечениям; подвержена оковам; "
    "подвержена узам; подвержена потокам; подвержена ярмам; подвержена помехам; затронута искажениями; "
    "служит объектом цепляния; подвержена омрачению; является этически неопределённой; не имеет объекта; "
    "не сопутствует уму; не связана с умом; не является результатом действий и не способна приносить результаты; "
    "является неомрачённой, но подверженной омрачению; не является явлением с направленной мыслью и удержанием мысли; "
    "не является явлением без направленной мысли, только с удержанием мысли; "
    "является явлением без направленной мысли и без удержания мысли; не сопровождается восторгом; "
    "не сопровождается счастьем; не сопровождается невозмутимостью; не устраняется ни видением истины, ни развитием ума; "
    "относится к явлениям, чьи корни не устраняются ни видением истины, ни развитием ума; "
    "не ведёт ни к накоплению, ни к убыванию; не относится ни к обучающимся, ни к завершившим обучение; "
    "является ограниченной; относится к миру чувственных желаний; не относится к миру форм; не относится к миру без форм; "
    "принадлежит к кругам существования; не относится к явлениям, не принадлежащим к кругам существования; "
    "является непредопределённой; не ведёт к освобождению; является возникшей; познаётся шестью видами сознания; "
    "является непостоянной; подвластна старению."
)

# Atthi rūpaṃ X, atthi rūpaṃ Y.  (PI1 ^1-U1, sentence by sentence)
NOUPADA_VAR = "[вариант написания (Sī., Ka.): nupādā]"
RUPA_DUKA = [  # (X, Y) as in «Есть материальная форма X, есть материальная форма Y.»
    ("производная", "непроизводная"),
    (", охваченная цеплянием", ", не охваченная цеплянием"),
    (", охваченная цеплянием и служащая его объектом", ", не охваченная цеплянием, но служащая его объектом"),
    ("видимая", "невидимая"),
    (", способная к соударению", ", не способная к соударению"),
    (", являющаяся способностью", ", не являющаяся способностью"),
    (", являющаяся великим элементом", ", не являющаяся великим элементом"),
    (", являющаяся внешним выражением", ", не являющаяся внешним выражением"),
    (", порождённая умом", ", не порождённая умом"),
    (", сосуществующая с умом", ", не сосуществующая с умом"),
    (", следующая за умом", ", не следующая за умом"),
    (", относящаяся к внутреннему", ", относящаяся к внешнему"),
    ("грубая", "тонкая"),
    ("вдали", "вблизи"),
]
RUPA_DUKA_FOOD = (", являющаяся съедаемой пищей", ", не являющаяся съедаемой пищей")


def duka(x, y, var=""):
    """Atthi rūpaṃ X, atthi rūpaṃ Y. (x/y starting with «,» are post-posed participles)"""
    sx = x if x.startswith(",") else " " + x
    sy = y if y.startswith(",") else " " + y
    v_ = f" {var}" if var else ""
    return f"Есть материальная форма{sx}, есть материальная форма{sy}{v_}."


INT = "Материальная форма, относящаяся к внутреннему,"   # yaṃ taṃ rūpaṃ ajjhattikaṃ (PI1 ^1-585)
EXT = "Материальная форма, относящаяся к внешнему,"      # yaṃ taṃ rūpaṃ bāhiraṃ


def tika(own, x, y):
    """yaṃ taṃ rūpaṃ ajjhattikaṃ taṃ <own>, yaṃ taṃ rūpaṃ bāhiraṃ taṃ atthi <x>, atthi <y>
    = «Материальная форма, относящаяся к внутреннему, <own>; материальная форма, относящаяся к внешнему, бывает <x>, бывает <y>»"""
    return f"{INT} {own}; {EXT[0].lower()}{EXT[1:]} бывает {x}, бывает {y}"


TIKA = [  # (own, x, y), PI1 ^1-585 sentence by sentence
    ("является производной", "производной", "непроизводной"),
    ("охвачена цеплянием", "охваченной цеплянием", "не охваченной цеплянием"),
    ("охвачена цеплянием и служит его объектом", "охваченной цеплянием и служащей его объектом",
     "не охваченной цеплянием, но служащей его объектом"),
]
TIKA_FOOD = ("не является съедаемой пищей", "съедаемой пищей", "не съедаемой пищей")


def catukka(a, b, x, y):
    """yaṃ taṃ rūpaṃ <a> taṃ atthi <x>, atthi <y>; yaṃ taṃ rūpaṃ <b> taṃ atthi <x>, atthi <y> (PI1 ^1-586)"""
    return f"{a} материальная форма бывает {x}, бывает {y}; {b.lower()} материальная форма бывает {x}, бывает {y}"


CATUKKA = [  # upādā / no upādā × (x, y)
    ("охваченной цеплянием", "не охваченной цеплянием"),
    ("охваченной цеплянием и служащей его объектом", "не охваченной цеплянием, но служащей его объектом"),
    ("способной к соударению", "не способной к соударению"),
    ("грубой", "тонкой"),
    ("вдали", "вблизи"),
]
SEEN_HEARD = "материальная форма увиденная, услышанная, ощущённая, познанная"   # PI1 ^1-586 diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ
ELEMENTS4 = "элемент земли, элемент воды, элемент огня, элемент ветра и та материальная форма, которая является производной"  # PI1 ^1-587
KNOWABLE = [f"материальная форма, познаваемая {s}" for s in ("глазом", "ухом", "носом", "языком", "телом")]
KNOW6 = "; ".join(KNOWABLE + ["материальная форма, познаваемая умом"])                              # PI1 ^1-588
MANODHATU_K = "материальная форма, познаваемая элементом ума"
MANOVINNANADHATU_K = "материальная форма, познаваемая элементом умственного сознания"
KNOW7 = "; ".join(KNOWABLE + [MANODHATU_K, MANOVINNANADHATU_K])                                    # PI1 ^1-589
TOUCH_PAIR = "которая бывает доставляющей удовольствие при контакте, бывает болезненной при контакте"  # atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ
KNOW8 = "; ".join(KNOWABLE[:4] + [f"{KNOWABLE[4]}, {TOUCH_PAIR}", MANODHATU_K, MANOVINNANADHATU_K])  # PI1 ^1-590
FACULTIES8 = ("способность глаза, способность уха, способность носа, способность языка, способность тела, "
              "способность женственности, способность мужественности, жизненная способность")
NINE = f"{FACULTIES8} и та материальная форма, которая не является способностью"                    # PI1 ^1-591
TEN = (f"{FACULTIES8} и материальная форма, не являющаяся способностью, которая бывает способной к соударению, "
       "бывает не способной к соударению")                                                          # PI1 ^1-592
BASES10 = ("сфера глаза, сфера уха, сфера носа, сфера языка, сфера тела, сфера видимых форм, сфера звуков, "
           "сфера запахов, сфера вкусов, сфера осязаемого")
ELEVEN = (f"{BASES10} и та материальная форма, которая является невидимой и не способной к соударению "
          "и принадлежит к сфере объектов ума")                                                     # PI1 ^1-593 (without its variant)
AS_IN_RUPAKANDA = "(Как разобрано в разделе о материальной форме, так же следует разбирать и здесь.)"
# (Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.)

PI1_STRINGS = (
    [NAMO, PITAKA, f"Пять совокупностей – {FIVE_LIST}", TIME_STR["atita"]["p"], TIME_STR["anagata"]["p"], TIME_STR["paccuppanna"]["p"],
     cap(MAHABHUTA), cap(RUPA_EKAVIDHA.replace("является материальной;", "является материальной [вариант чтения (Sī.): rūpiyaṃ];")),
     cap(SEEN_HEARD), cap(ELEMENTS4), cap(KNOW6), cap(KNOW7), cap(KNOW8), cap(NINE), cap(TEN),
     "Сфера глаза… сфера осязаемого", "Способность женственности… съедаемая пища",
     "у тех или иных существ", "у тех или иных других существ, других личностей",
     "собственными, закреплёнными, индивидуальными и охваченными цеплянием",
     "или же какая бы другая материальная форма ни", "это называется всей материальной формой"]
    + [duka(x, y) for x, y in RUPA_DUKA + [RUPA_DUKA_FOOD]]
    + [f"{INT} {own}." for own, _, _ in TIKA + [TIKA_FOOD]]
    + [f"{EXT} бывает {x}, бывает {y}." for _, x, y in TIKA + [TIKA_FOOD]]
    + [f"{a} материальная форма бывает {x}, бывает {y}." for x, y in CATUKKA for a in ("Производная", "Непроизводная")]
)


# =========================================================================== segments
def build_preamble():
    return {"T-1": [NAMO], "0": [f"# {PITAKA}"], "2-0": [f"## {BOOK}"]}


def build_sample():
    h = {}
    h["2-1-0"] = [f"### {CH_TITLE[1][1]}"]
    h["2-1-1-0"] = [f"#### {SUTTANTA_BH}"]
    h["2-1"] = [FIVE]
    # ----- rūpa
    r = "rupa"
    h["2-1-1-1-0"] = [f"##### {cap(KH[r])}"]
    h["2-2"] = [agg_segment(r)]
    h["2-3"] = [time_sentence(r, t) for t in TIME]
    h["2-4"] = [own_sentence(r, False), own_sentence(r, True)]
    h["2-5"] = [rupa_line("olarika", cap(EYE_TO_TOUCH)),
                rupa_line("sukhuma", cap(fem_to_food(True)))]
    h["2-6"] = [rupa_line("hina", f"Материальная форма, которая {FOR_BEINGS} является {HINA_STR}: {SENSE_OBJECTS}"),
                rupa_line("panita", f"Материальная форма, которая {FOR_BEINGS} является {PANITA_STR}: {SENSE_OBJECTS}")
                + " " + compare(r, "hina", "panita")]
    h["2-7"] = [rupa_line("dure", f"{cap(fem_to_food())}, {OR_OTHER} {FAR_STR}", comma=True),
                rupa_line("santike", f"{cap(EYE_TO_TOUCH)}, {OR_OTHER} {NEAR_STR}", comma=True) + " " + compare_far(r)]
    # ----- vedanā, saññā, saṅkhārā, viññāṇa
    ids = {"vedana": (2, 8), "sanna": (3, 14), "sankhara": (4, 20), "vinnana": (5, 26)}
    for k, (hn, s0) in ids.items():
        h[f"2-1-1-{hn}-0"] = [f"##### {cap(KH[k])}"]
        h[f"2-{s0}"] = [agg_segment(k)]
        h[f"2-{s0 + 1}"] = [time_sentence(k, t) for t in TIME]
        h[f"2-{s0 + 2}"] = [own_sentence(k, False), own_sentence(k, True)]
        h[f"2-{s0 + 3}"] = [coarse_segment(k, COARSE_PAIRS[k], "olarika", "sukhuma")]
        h[f"2-{s0 + 4}"] = [coarse_segment(k, HINA_PAIRS[k], "hina", "panita")]
        h[f"2-{s0 + 5}"] = [far_line(k, far_groups(k), dash_close=(k != "sankhara")),
                            near_line(k, dash_close=(k == "vinnana"))]
    h["2-31"].append(f"{SUTTANTA_BH}.")
    # ----- Abhidhammabhājanīya, rūpa
    h["2-1-2-0"] = [f"#### {ABHI_BH}"]
    h["2-32"] = [FIVE]
    h["2-1-2-1-0"] = [f"##### {cap(KH[r])}"]
    duka_body = " ".join([duka(*RUPA_DUKA[0], NOUPADA_VAR)] + [duka(x, y) for x, y in RUPA_DUKA[1:-1]])
    food = duka(*RUPA_DUKA_FOOD)
    last = duka(*RUPA_DUKA[-1])[:-1] + "… " + food[0].lower() + food[1:]
    duka_body += " " + last
    duka_body = duka_body[0].lower() + duka_body[1:]
    tikas = [tika(*t) for t in TIKA]
    tika_body = tikas[0][0].lower() + tikas[0][1:] + ". " + ". ".join(tikas[1:]) + "… " \
        + tika(*TIKA_FOOD)[0].lower() + tika(*TIKA_FOOD)[1:] + "."
    cats = [catukka("Производная", "Непроизводная", x, y) for x, y in CATUKKA]
    cat_body = cats[0][0].lower() + cats[0][1:] + ". " + ". ".join(cats[1:]) + f"… {SEEN_HEARD}."
    h["2-33"] = [
        f"{agg_q(r)} {vidha(1, r)} {RUPA_EKAVIDHA} {vidha_end(1, r)}",
        f"{vidha(2, r)} {duka_body} {vidha_end(2, r)}",
        AS_IN_RUPAKANDA,
        f"{vidha(3, r)} {tika_body} {vidha_end(3, r)}",
        f"{vidha(4, r)} {cat_body} {vidha_end(4, r)}",
        f"{vidha(5, r)} {ELEMENTS4}. {vidha_end(5, r)}",
        f"{vidha(6, r)} {KNOW6}. {vidha_end(6, r)}",
        f"{vidha(7, r)} {KNOW7}. {vidha_end(7, r)}",
        f"{vidha(8, r)} {KNOW8}. {vidha_end(8, r)}",
        f"{vidha(9, r)} {NINE}. {vidha_end(9, r)}",
        f"{vidha(10, r)} {TEN}. {vidha_end(10, r)}",
        f"{vidha(11, r)} {ELEVEN}. {vidha_end(11, r)}",
        f"Это называется {kh_ins(r)}.",
    ]
    return h


# =========================================================================== formulas file
def formulas_md():
    P = {"rupa": ("rūpaṃ", "n"), "vedana": ("vedanā", "f"), "sanna": ("saññā", "f"),
         "sankhara": ("saṅkhārā", "p"), "vinnana": ("viññāṇaṃ", "n")}
    KHP = {"rupa": "rūpakkhandho", "vedana": "vedanākkhandho", "sanna": "saññākkhandho",
           "sankhara": "saṅkhārakkhandho", "vinnana": "viññāṇakkhandho"}

    def end(g, n_, f_, p_):
        return {"n": n_, "f": f_, "p": p_}[g]

    L = ["# pi-2 Vibhaṅga: Russian rails sentence formulas (binding for chapter agents)", "",
         "Format: Pāli = Russian, one per line. Generated by build_rails_sample_ru.py; import its constants and functions",
         "instead of retyping them (importing writes nothing). Termbase: AI_translation/russian/pi-2-pali-russian-termbase-plain.md",
         "with termbase/APPROVED.md. (pi-1) = taken unchanged from the approved pi-1 Russian rails (main() asserts it).",
         "(pi-1 inflected) = the pi-1 string put into another gender or number. (not yet in the sample) = settled frame,",
         "not exercised by the sample.", "",
         "## Book frame and headings", "",
         f"Namo tassa bhagavato arahato sammāsambuddhassa = {NAMO} (pi-1)",
         f"# Abhidhammapiṭake = # {PITAKA} (pi-1)",
         f"## Vibhaṅgapāḷi = ## {BOOK} (mid-sentence: «{BOOK}»)",
         ] + [f"### {p} = ### {ru}" for _, (p, ru) in sorted(CH_TITLE.items())] + [
         f"<X>vibhaṅgo niṭṭhito. = <title> {DONE}. (e.g. «{CH_TITLE[1][1]} {DONE}.»; pi-1 pattern «Раздел о материальной форме завершён.») (not yet in the sample)",
         f"#### Suttantabhājanīyaṃ = #### {SUTTANTA_BH}",
         f"Suttantabhājanīyaṃ. (closing line) = {SUTTANTA_BH}.",
         f"#### Abhidhammabhājanīyaṃ = #### {ABHI_BH}",
         f"Abhidhammabhājanīyaṃ. (closing line) = {ABHI_BH}. (not yet in the sample)",
         f"#### Pañhāpucchakaṃ = #### {PANHA} (not yet in the sample)",
         f"Pañhāpucchakaṃ. (closing line) = {PANHA}. (not yet in the sample)",
         f"##### Tikaṃ / ##### Dukaṃ (Pañhāpucchaka) = ##### {TIKA_H} / ##### {DUKA_H} (not yet in the sample)",
         ] + [f"##### {KHP[k][0].upper() + KHP[k][1:]} = ##### {cap(KH[k])}" for k in ORDER] + [
         "", "## Punctuation, variants, frames", "",
         f"Tattha (opening a question) = {TATTHA} («Что такое здесь …?», «Какое здесь …, а какое …?»)",
         "…pe… = … (same spot); Pāli ';' stays ';'; Pāli '.' stays '.'",
         "– (Pāli dash) = – (same spot, same count). A comma goes before it only where a participial or relative clause closes («…, – это …»); after a plain noun list no comma («… осязаемое – это …»).",
         "[kabaḷiṃkāro (sī. syā.)] = [вариант написания (Sī., Syā.): kabaḷiṃkāro] (after «съедаемая»)",
         f"[nupādā (sī. ka.)] = {NOUPADA_VAR} (after «непроизводная»)",
         "Tattha katamo/katamaṃ/katamā X? = Что такое здесь X? (plural katame X? = Что такое здесь X?, X in the plural)",
         "– idaṃ/ayaṃ vuccati X. / – ime vuccanti X. = – это называется X(instrumental). (singular and plural alike: «это называется формирующими факторами …»)",
         "Ayaṃ/Ime vuccati(-nti) X. as a new sentence (no Pāli dash) = Это называется X(instrumental).",
         "Taṃ taṃ vā pana X upādāyupādāya X A B daṭṭhabbaṃ/-ā. = Или же X(acc) следует рассматривать как A или B в сравнении с тем (той, теми) или иным(-ой, -ыми) X(ins).",
         f"(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.) = {AS_IN_RUPAKANDA}",
         "", "## Aggregate formulas", "",
         f"Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho. = {FIVE} (pi-1)",
         ]
    for k in ORDER:
        p, g = P[k]
        yk = end(g, "Yaṃ kiñci", "Yā kāci", "Ye keci")
        yy = end(g, "yaṃ", "yā", "ye")
        tail = end(g, "atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā",
                   "atītānāgatapaccuppannā ajjhattā vā bahiddhā vā oḷārikā vā sukhumā vā hīnā vā paṇītā vā",
                   "atītānāgatapaccuppannā ajjhattā vā bahiddhā vā oḷārikā vā sukhumā vā hīnā vā paṇītā vā")
        L.append(f"Tattha katamo {KHP[k]}? = {agg_q(k)}")
        L.append(f"{yk} {p} {tail} {yy} dūre santike vā, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā = {agg_formula(k)}")
        L.append(f"– ayaṃ vuccati {KHP[k]}. = – это называется {kh_ins(k)}.")
    L += ["Members after the comma (introduced by «:»):",
          f"cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāyarūpaṃ = {MAHABHUTA} (pi-1, lower-case initial) + «,» before the dash",
          f"sukhā vedanā dukkhā vedanā adukkhamasukhā vedanā = {FEEL3} + «,» before the dash",
          f"cakkhusamphassajā saññā … manosamphassajā saññā = {MEMBERS['sanna'][0]}",
          f"cakkhusamphassajā cetanā … manosamphassajā cetanā = {MEMBERS['sankhara'][0]}",
          f"cakkhuviññāṇaṃ sotaviññāṇaṃ ghānaviññāṇaṃ jivhāviññāṇaṃ kāyaviññāṇaṃ manoviññāṇaṃ = {VINNANA6}",
          "", "## Past / future / present", "",
          f"atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ uppajjitvā vigataṃ atītaṃ atītaṃsena saṅgahitaṃ (rūpaṃ) = {TIME_STR['atita']['f']} (pi-1 inflected)",
          f"… (vedanā, saññā, viññāṇaṃ) = {TIME_STR['atita']['n']} (pi-1 inflected)",
          f"atītā … atītaṃsena saṅgahitā (saṅkhārā) = {TIME_STR['atita']['p']} (pi-1)",
          f"ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ anuppannaṃ asamuppannaṃ anuṭṭhitaṃ asamuṭṭhitaṃ anāgataṃ anāgataṃsena saṅgahitaṃ (rūpaṃ) = {TIME_STR['anagata']['f']} (pi-1 inflected)",
          f"… (vedanā, saññā, viññāṇaṃ) = {TIME_STR['anagata']['n']} (pi-1 inflected)",
          f"ajātā … anāgataṃsena saṅgahitā (saṅkhārā) = {TIME_STR['anagata']['p']} (pi-1)",
          f"jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ uppannaṃ samuppannaṃ uṭṭhitaṃ samuṭṭhitaṃ paccuppannaṃ paccuppannaṃsena saṅgahitaṃ (rūpaṃ) = {TIME_STR['paccuppanna']['f']} (pi-1 inflected)",
          f"… (vedanā, saññā, viññāṇaṃ) = {TIME_STR['paccuppanna']['n']} (pi-1 inflected)",
          f"jātā … paccuppannaṃsena saṅgahitā (saṅkhārā) = {TIME_STR['paccuppanna']['p']} (pi-1)",
          "Full sentences:"]
    for k in ORDER:
        p, g = P[k]
        kt = end(g, "katamaṃ", "katamā", "katame")
        for t, (pt, pv) in zip(TIME, [("atītaṃ", "atītā"), ("anāgataṃ", "anāgatā"), ("paccuppannaṃ", "paccuppannā")]):
            tw = pt if g == "n" else pv
            q = f"Tattha {kt} {p} {tw}? … – {end(g, 'idaṃ vuccati', 'ayaṃ vuccati', 'ime vuccanti')} {p} {tw}."
            L.append(f"{q} = {time_sentence(k, t)}")

    L += ["", "## Internal / external", "",
          f"tesaṃ tesaṃ sattānaṃ = {BEINGS} (pi-1)",
          f"tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ = {OTHER_BEINGS} (pi-1)",
          f"ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ (rūpaṃ, after «которая … является») = {OWN_ATTR['f']}",
          f"… niyakā pāṭipuggalikā upādinnā (vedanā, saññā, viññāṇaṃ) = {OWN_ATTR['n']}",
          f"… (saṅkhārā, after «которые … являются») = {OWN_ATTR['p']} (pi-1 has «находятся внутри себя, являются собственными, …»: ajjhattaṃ = «внутренний» per pi-2 APPROVED)",
          "ajjhatta / bahiddhā (attribute) = внутренний / внешний",
          "Full sentences:"]
    for k in ORDER:
        p, g = P[k]
        kt = end(g, "katamaṃ", "katamā", "katame")
        aj = end(g, "ajjhattaṃ", "ajjhattā", "ajjhattā")
        L.append(f"Tattha {kt} {p} {aj}? … = {own_sentence(k, False)}")
        L.append(f"Tattha {kt} {p} bahiddhā? … = {own_sentence(k, True)}")

    L += ["", "## Gross / subtle", "",
          "oḷārika / sukhuma = грубый / тонкий",
          f"Tattha katamaṃ rūpaṃ oḷārikaṃ? Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ – idaṃ vuccati rūpaṃ oḷārikaṃ. = {rupa_line('olarika', cap(EYE_TO_TOUCH))}",
          f"Tattha katamaṃ rūpaṃ sukhumaṃ? Itthindriyaṃ…pe… kabaḷīkāro āhāro – idaṃ vuccati rūpaṃ sukhumaṃ. = {rupa_line('sukhuma', cap(fem_to_food()))}",
          f"Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ = {cap(EYE_TO_TOUCH)} (pi-1)",
          f"Itthindriyaṃ…pe… kabaḷīkāro āhāro = {cap(fem_to_food())} (pi-1)",
          f"Tattha katamā vedanā oḷārikā sukhumā? = {which_q('vedana', 'olarika', 'sukhuma')}",
          f"Tattha katamā saññā oḷārikā sukhumā? = {which_q('sanna', 'olarika', 'sukhuma')}",
          f"Tattha katame saṅkhārā oḷārikā sukhumā? = {which_q('sankhara', 'olarika', 'sukhuma')}",
          f"Tattha katamaṃ viññāṇaṃ oḷārikaṃ sukhumaṃ? = {which_q('vinnana', 'olarika', 'sukhuma')}",
          "A oḷārikā, B sukhumā. = A грубое, а B тонкое. (number follows the Pāli; plural «грубые/тонкие»; a post-posed qualifier closes with a comma)",
          "Qualifiers (pre-posed, neuter sg / plural):"]
    pq = {"akusala": "akusalā/akusalaṃ", "kusala": "kusalā/kusalaṃ", "abyakata": "abyākatā/abyākataṃ",
          "kusalabyakata": "kusalābyākatā", "kusalakusala": "kusalākusalā", "akusalabyakata": "akusalābyākatā",
          "patigha": "paṭighasamphassajā", "adhivacana": "adhivacanasamphassajā"}
    for q, pali in pq.items():
        L.append(f"{pali} = {' / '.join(x for x in PRE[q] if x)}")
    L += [f"sāsavā / sāsavaṃ X = X, подверженное (-ые) влечениям; anāsavā X = X, свободное (-ые) от влечений",
          f"asamāpannassa X = X {ASAM}; samāpannassa X = X {SAM}",
          f"dukkhā / sukhā / adukkhamasukhā vedanā = болезненное чувство / приятное чувство / {ADM}",
          f"sukhā ca adukkhamasukhā ca vedanā = {np('vedana', 'sukha+adm', 'p')[0]} (plural verb)",
          f"dukkhā ca adukkhamasukhā ca vedanā = {np('vedana', 'dukkha+adm', 'p')[0]} (plural verb)",
          f"sukhadukkhā vedanā = {np('vedana', 'sukhadukkha', 'p')[0]}",
          f"dukkhāya vedanāya sampayuttā saññā = {np('sanna', 'dukkha', 's')[0]}",
          f"sukhāya vedanāya sampayuttā saññā = {np('sanna', 'sukha', 's')[0]}",
          f"adukkhamasukhāya vedanāya sampayuttā saññā = {np('sanna', 'adm', 's')[0]}",
          f"sukhāya ca adukkhamasukhāya ca vedanāhi sampayuttā saññā = {np('sanna', 'sukha+adm', 'p')[0]}",
          f"dukkhāya ca adukkhamasukhāya ca vedanāhi sampayuttā saññā = {np('sanna', 'dukkha+adm', 'p')[0]}",
          f"sukhadukkhāhi vedanāhi sampayuttā saññā = {np('sanna', 'sukhadukkha', 'p')[0]}",
          f"viññāṇā (plural) = виды сознания (termbase viññāṇehi «виды сознания»)",
          f"Taṃ taṃ vā pana vedanaṃ upādāyupādāya vedanā oḷārikā sukhumā daṭṭhabbā. = {compare('vedana', 'olarika', 'sukhuma')}",
          f"Te te vā pana saṅkhāre upādāyupādāya saṅkhārā oḷārikā sukhumā daṭṭhabbā. = {compare('sankhara', 'olarika', 'sukhuma')}",
          "Full segments:"]
    for k in ("vedana", "sanna", "sankhara", "vinnana"):
        L.append(f"{P[k][0]} oḷārika/sukhuma segment = {coarse_segment(k, COARSE_PAIRS[k], 'olarika', 'sukhuma')}")

    L += ["", "## Inferior / superior", "",
          "hīna / paṇīta = низший / высший",
          f"tesaṃ tesaṃ sattānaṃ (with the two strings below) = {FOR_BEINGS}",
          f"uññātaṃ avaññātaṃ hīḷitaṃ paribhūtaṃ acittīkataṃ hīnaṃ hīnamataṃ hīnasammataṃ aniṭṭhaṃ akantaṃ amanāpaṃ (after «является») = {HINA_STR}",
          f"anuññātaṃ anavaññātaṃ ahīḷitaṃ aparibhūtaṃ cittīkataṃ paṇītaṃ paṇītamataṃ paṇītasammataṃ iṭṭhaṃ kantaṃ manāpaṃ (after «является») = {PANITA_STR}",
          f"rūpā saddā gandhā rasā phoṭṭhabbā = {SENSE_OBJECTS}",
          f"Tattha katamaṃ rūpaṃ hīnaṃ? … = {rupa_line('hina', f'Материальная форма, которая {FOR_BEINGS} является {HINA_STR}: {SENSE_OBJECTS}')}",
          f"Taṃ taṃ vā pana rūpaṃ upādāyupādāya rūpaṃ hīnaṃ paṇītaṃ daṭṭhabbaṃ. = {compare('rupa', 'hina', 'panita')}",
          f"Tattha katamā vedanā hīnā paṇītā? = {which_q('vedana', 'hina', 'panita')}",
          f"Tattha katame saṅkhārā hīnā paṇītā? = {which_q('sankhara', 'hina', 'panita')}",
          "Full segments:"]
    for k in ("vedana", "sanna", "sankhara", "vinnana"):
        L.append(f"{P[k][0]} hīna/paṇīta segment = {coarse_segment(k, HINA_PAIRS[k], 'hina', 'panita')}")

    L += ["", "## Far / near", "",
          "dūre / santike (predicate) = находится (-ятся) вдали / вблизи (pi-1); the termbase has santike «вблизи», no entry for dūre",
          "rūpaṃ dūre / santike (attribute) = материальная форма, находящаяся вдали / вблизи (pi-1 ^1-676/677)",
          f"yaṃ vā panaññampi atthi rūpaṃ = {OR_OTHER} (pi-1 frame «или же какая бы другая материальная форма ни …»)",
          f"anāsanne anupakaṭṭhe dūre asantike = {FAR_STR}",
          f"āsanne upakaṭṭhe avidūre santike = {NEAR_STR}",
          f"Tattha katamaṃ rūpaṃ dūre? … = {rupa_line('dure', f'{cap(fem_to_food())}, {OR_OTHER} {FAR_STR}', comma=True)}",
          f"Taṃ taṃ vā pana rūpaṃ upādāyupādāya rūpaṃ dūre santike daṭṭhabbaṃ. = {compare_far('rupa')}",
          "A B-ehi/-āhi/-āya/-ā (abl.) dūre = A находится (находятся) вдали от B(gen)",
          "A A-āya/-ānaṃ/-assa santike = A находится (находятся) вблизи A(gen)",
          f"Tattha katamā vedanā dūre? = {what_q('dure', 'vedana')}",
          f"Tattha katame saṅkhārā santike? = {what_q('santike', 'sankhara')}",
          f"– ayaṃ vuccati vedanā dūre. = – {called('dure', 'vedana')}",
          f"Ime vuccanti saṅkhārā santike. = {cap(called('santike', 'sankhara'))}",
          "Full lines:"]
    for k in ("vedana", "sanna", "sankhara", "vinnana"):
        L.append(f"{P[k][0]} dūre line = {far_line(k, far_groups(k), dash_close=(k != 'sankhara'))}")
        L.append(f"{P[k][0]} santike line = {near_line(k, dash_close=(k == 'vinnana'))}")

    L += ["", "## Classification lines (Abhidhammabhājanīya)", "",
          "Ekavidhena … Ekādasavidhena = " + ", ".join(NUMW[i] for i in range(1, 12)) + " (user: no «классификация»)",
          ] + [f"<N>vidhena {KHP[k]} – = {cap(KH[k])} <N> –" for k in ORDER] + [
          f"Ekavidhena rūpakkhandho – = {vidha(1, 'rupa')}",
          f"Dasavidhena rūpakkhandho – = {vidha(10, 'rupa')}",
          f"Evaṃ <N>vidhena rūpakkhandho. = Такова {KH['rupa']} <N>. (e.g. «{vidha_end(10, 'rupa')}»)",
          f"Ayaṃ vuccati rūpakkhandho. = Это называется {kh_ins('rupa')}.",
          f"sabbaṃ rūpaṃ na hetu … jarābhibhūtaṃ = {RUPA_EKAVIDHA} (pi-1, without pi-1's [rūpiyaṃ] variant; nevācayagāmināpacayagāmī = pi-1 neva ācayagāmi na apacayagāmi)",
          "Atthi rūpaṃ X, atthi rūpaṃ Y. = Есть материальная форма X, есть материальная форма Y. (pi-1, each dyad below)",
          ] + [f"  dyad = {duka(x, y)} (pi-1)" for x, y in RUPA_DUKA + [RUPA_DUKA_FOOD]] + [
          "yaṃ taṃ rūpaṃ ajjhattikaṃ taṃ X, yaṃ taṃ rūpaṃ bāhiraṃ taṃ atthi Y, atthi Z = "
          + tika("X", "Y", "Z") + " («;» for the Pāli comma between the halves; halves = pi-1 ^1-585)",
          ] + [f"  triad = {tika(*t)}." for t in TIKA + [TIKA_FOOD]] + [
          "yaṃ taṃ rūpaṃ upādā taṃ atthi X, atthi Y; yaṃ taṃ rūpaṃ no upādā taṃ atthi X, atthi Y = "
          + catukka("Производная", "Непроизводная", "X", "Y") + " (halves = pi-1 ^1-586)",
          f"diṭṭhaṃ, sutaṃ, mutaṃ, viññātaṃ rūpaṃ = {SEEN_HEARD} (pi-1)",
          f"pathavīdhātu, āpodhātu, tejodhātu, vāyodhātu, yañca rūpaṃ upādā = {ELEMENTS4} (pi-1)",
          f"cakkhuviññeyyaṃ rūpaṃ … manoviññeyyaṃ rūpaṃ = {KNOW6} (pi-1)",
          f"… manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ = {KNOW7} (pi-1)",
          f"… kāyaviññeyyaṃ rūpaṃ atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ, … = {KNOW8} (pi-1)",
          f"cakkhundriyaṃ … jīvitindriyaṃ, yañca rūpaṃ na indriyaṃ = {NINE} (pi-1)",
          f"… na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ = {TEN} (pi-1)",
          f"cakkhāyatanaṃ … phoṭṭhabbāyatanaṃ, yañca rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ = {ELEVEN} (pi-1, without its variant)",
          f"(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.) = {AS_IN_RUPAKANDA}",
          "atthi X, atthi Y (classes of an aggregate) = бывает X, бывает Y (not yet in the sample; pi-1 «бывает …, бывает …»)",
          ]
    return "\n".join(L) + "\n"


# =========================================================================== write + verify
def segs(text):
    out, cur = [], []
    for ln in text.splitlines():
        if not ln.strip():
            continue
        cur.append(ln)
        m = ID.search(ln)
        if m:
            out.append((m.group(1), cur))
            cur = []
    return out


def render(pali_text, h):
    blocks = []
    for sid, plines in segs(pali_text):
        ru = h[sid]
        assert len(ru) == len(plines), (sid, len(ru), len(plines))
        if plines[0].startswith("#"):
            lvl = plines[0].split(" ", 1)[0]
            assert ru[0].split(" ", 1)[0] == lvl, (sid, "heading level")
        lines = list(ru)
        lines[-1] = f"{lines[-1]} ^{sid}"
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + "\n"


def main():
    pi1 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_RU.glob("*.md")))
    missing = [s for s in PI1_STRINGS if s not in pi1]
    assert not missing, f"PI1 strings not found in the pi-1 Russian: {missing}"
    SAMPLE.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    pre = render((PALI / "preamble.md").read_text(encoding="utf-8"), build_preamble())
    (OUT / "preamble.md").write_text(pre, encoding="utf-8", newline="\n")
    smp = render(SAMPLE_PALI.read_text(encoding="utf-8"), build_sample())
    (SAMPLE / "1-sample.md").write_text(smp, encoding="utf-8", newline="\n")
    (RAILS / "ru-rails-formulas.md").write_text(formulas_md(), encoding="utf-8", newline="\n")
    print("wrote preamble.md, sample-1/1-sample.md, ru-rails-formulas.md;", len(PI1_STRINGS), "PI1 strings verified")


if __name__ == "__main__":
    main()
