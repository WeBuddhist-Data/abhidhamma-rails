"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience), chapter 4-01
(Nikkhepakaṇḍaṃ: the summary of the triads ^1-985 … ^1-1058 and of the pairs of the root, short intermediate,
taint, fetter and tie groups ^1-1059 … ^1-1155).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/4-01-nikkhepakandam.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/notes-4-01.md

Every line is built from the fixed strings below. The earlier rails builders are imported, never edited:
build_rails_sample_ru.py (S: matrix names, question and answer forms, the synonym strings S_ALOBHA, S_ADOSA,
S_PANNA, headings), build_rails_2-04_ru.py (D: the diṭṭhi, moha, dosa and vicikicchā strings), through D the
2-03 builder (C: «фактор пути, входящий в путь», the bojjhaṅga suffixes) and build_rails_3-01_ru.py (T: the
statement ^1-583 pieces, the sense-base names, «и та материальная форма, которая …»).
Question and answer frames are checked against the Pāli line by line («Katame dhammā X?» = S.q_form(name),
«ime dhammā X.» = S.a_form(name)); dash, «?» and «…pe…» counts are checked per line.
Punctuation before the Pāli dash (coordinator 2026-11-14): «X – это …» after a plain noun or list; «…, – это …»
only where the dash closes a participial phrase or a subordinate clause.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.

usage: python -I -X utf8 build_rails_4-01_ru.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)       # importing writes nothing
    return mod


D = _load("build_rails_2_04_ru", "build_rails_2-04_ru.py")
C = D.C
T = _load("build_rails_3_01_ru", "build_rails_3-01_ru.py")

PART = "4-01-nikkhepakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
cap = S.cap
low = S.low
PE, ELL = "…pe…", "…"
NOTES = []          # (pali, russian) new recurring formulas, written to notes-4-01.md


def note(p, r):
    NOTES.append((p, r))
    return r


# =========================================================================================
# 1. Matrix names and the question / answer frames
# =========================================================================================
N = {}
for _items in list(S.TRIADS.values()) + list(S.PAIRS.values()):
    for _p, _r, _v in _items:
        N.setdefault(_p, _r)
for _p, _r in S.EXTRA_NAMES:
    N.setdefault(_p, _r)
# ^1-1022 spells the third item of 1-M1-10 apart (matrix: nevācayagāmināpacayagāmino)
N["neva ācayagāmi na apacayagāmino"] = S.TRIADS["1-M1-10"][2][1]
KEN_A, KEN_B = S.PAIRS["1-M2-13"][0][1], S.PAIRS["1-M2-13"][1][1]
N["kenaci viññeyyā, kenaci na viññeyyā"] = f"{KEN_A}, и {KEN_B}"
assert N["neva dassanena na bhāvanāya pahātabbā"] == "явления, не устраняемые ни видением истины, ни развитием ума"


def Q(p):
    return S.q_form(N[p])


def A(p):
    return S.a_form(N[p])


def ans(body, p, comma):
    """body – ime dhammā p.  comma=True after a participial phrase or a subordinate clause."""
    return f"{body}{', – ' if comma else ' – '}{A(p)}"


def qa(p, body, comma):
    return f"{Q(p)} {ans(body, p, comma)}"


# =========================================================================================
# 2. Recurring pieces of the answers
# =========================================================================================
AGG4 = T.AGGREGATES                    # совокупность чувств, … и совокупность сознания
AGG4_PE = "совокупность чувств… совокупность сознания"
AGG3 = "совокупность восприятия, совокупность формирующих факторов и совокупность сознания"
assert AGG4.endswith(AGG3)
RUPAKKH = "совокупность материальной формы"
AGG5 = f"{RUPAKKH}, {AGG4}"
AGG5_PE = f"{RUPAKKH}… совокупность сознания"
SPH4 = T.SPHERES                       # относящиеся к миру чувственных желаний, …, или не принадлежащие …
SPH3 = "относящиеся к миру чувственных желаний, к миру форм или к миру без форм"
RES = "являющиеся результатом благих и неблагих явлений"
KIR = "и те " + T.KIR_PL.replace("функциональные", "функциональные явления", 1)
SABBA = f"и {T.SABBA_RUPA}, и {T.ASANKHATA_DHATU}"
ASANKH = T.ASANKHATA_DHATU             # необусловленный элемент
assert f"{cap(AGG4)}, {RES}, {SPH4}, {KIR}, {SABBA}, – " in T.UDDESO_R   # 3-01 ^1-583
YANCA = T.YANCA                        # и та материальная форма, которая
YANCA_KAMMA = YANCA + "возникла вследствие совершённых действий"
YANCA_NA_KAMMA = YANCA + "возникла не вследствие совершённых действий"
YANCA_UPP = YANCA + "возникнет вследствие совершённых действий"
YANCA_ANID = YANCA + T.ANID_APP + " и " + T.DHAMMAYATANA
TAMSAMP = "связанные с ними"           # taṃsampayutto (after a plural or the roots)
KILESA = "и омрачения, пребывающие вместе с ними"          # tadekaṭṭhā ca kilesā (termbase)
KAMMA3 = "порождённые ими телесное действие, речевое действие и умственное действие"   # taṃsamuṭṭhānaṃ …
LDM = "жадность, злоба, заблуждение"
ROOTS_K = "Три благих корня – отсутствие жадности, отсутствие злобы, отсутствие заблуждения"
ROOTS_A = f"Три неблагих корня – {LDM}"
LOKUTTARA = f"Пути, не принадлежащие к кругам существования, плоды путей и {ASANKH}"
FOUR_PATHS = "Четыре пути, не принадлежащие к кругам существования"
EXCEPT = "Кроме этих явлений, остальные"                    # Te dhamme ṭhapetvā avasesā
KA = "благие и неблагие явления"
KABY = "благие и этически неопределённые явления"
KAA = "благие, неблагие и этически неопределённые явления"
SAS = "подверженные влечениям"
SAMYOJ3 = "Три оковы – воззрение о самости, колебание, приверженность обрядам и обетам"
LOC = {"k": "в мире чувственных желаний", "r": "в мире форм", "a": "в мире без форм",
       "p": "в том, что не принадлежит к кругам существования"}


def locs(keys):
    xs = [LOC[k] for k in keys]
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " и " + xs[-1]


for _p, _r in [
    ("taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho", f"{TAMSAMP} {AGG4}"),
    ("taṃsampayutto vedanākkhandho…pe… viññāṇakkhandho", f"{TAMSAMP} {AGG4_PE}"),
    ("tadekaṭṭhā ca kilesā", KILESA),
    ("taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ", KAMMA3),
    ("Tīṇi kusalamūlāni – alobho, adoso, amoho", ROOTS_K),
    ("Tīṇi akusalamūlāni – lobho, doso, moho", ROOTS_A),
    ("Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu", LOKUTTARA),
    ("Cattāro maggā apariyāpannā", FOUR_PATHS),
    ("Te dhamme ṭhapetvā avasesā", EXCEPT),
    ("kusalākusalā / kusalābyākatā / kusalākusalābyākatā dhammā", f"{KA} / {KABY} / {KAA}"),
    ("Sāsavā … dhammā", f"{SAS} … явления"),
    ("kāmāvacarā, rūpāvacarā, arūpāvacarā (three spheres)", SPH3),
    ("X dhammā kāmāvacarā …; vedanākkhandho…pe… viññāṇakkhandho (description, then the aggregates)",
     "X явления, относящиеся к …: совокупность чувств… совокупность сознания (colon before the aggregates)"),
    ("Kusalākusalānaṃ dhammānaṃ vipākā … (results: aggregates first, as 3-01 ^1-583)",
     f"Совокупность чувств… совокупность сознания, {RES}, …"),
    ("rūpakkhandho…pe… viññāṇakkhandho", AGG5_PE),
    ("yañca rūpaṃ kammassa katattā", YANCA_KAMMA),
    ("yañca rūpaṃ na kammassa katattā", YANCA_NA_KAMMA),
    ("yañca rūpaṃ kammassa katattā uppajjissati", YANCA_UPP),
    ("yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ", YANCA_ANID),
    ("sabbañca rūpaṃ, asaṅkhatā ca dhātu (after the aggregates)", SABBA),
    ("Tīṇi saṃyojanāni – sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāso", SAMYOJ3),
]:
    note(_p, _r)

# =========================================================================================
# 3. Defilement and root strings
# =========================================================================================
TATTHA = "Что такое здесь {}?"                              # Tattha katamo/katamā/katamaṃ X?
CALLED = "это называется {}."                               # ayaṃ/idaṃ vuccati X.
note("Tattha katamo/katamā/katamaṃ X?", TATTHA.format("X"))
note("– ayaṃ/idaṃ vuccati X.", "– " + CALLED.format("X (instrumental)"))
note("Yo/Yā/Yaṃ S – ayaṃ vuccati X. (no «tasmiṃ samaye»)", "То, что есть S, – это называется X.")
note("Yo/Yā/Yaṃ evarūpo/evarūpā/evarūpaṃ S", "то, что есть такой/такая/такое S")

S_ADOSA_HEAD = "отсутствие злобы, отсутствие проявления злобы, отсутствие состояния злобы"
S_ADOSA_TAIL = "отсутствие недоброжелательности, отсутствие неприязни, отсутствие злобы как благой корень"
assert S.S_ADOSA == S_ADOSA_HEAD + ", " + S_ADOSA_TAIL
METTA = ("доброжелательность, проявление доброжелательности, состояние доброжелательности, участие, "
         "проявление участия, состояние участия, желание блага, сострадание")
S_ADOSA_METTA = f"{S_ADOSA_HEAD}, {METTA}, {S_ADOSA_TAIL}"
S_ADOSA_PE = f"{S_ADOSA_HEAD}{ELL} {S_ADOSA_TAIL}"
note("adoso adussanā adussitattaṃ metti mettāyanā mettāyitattaṃ anuddā anuddāyanā anudāyitattaṃ hitesitā "
     "anukampā abyāpādo abyāpajjo adoso kusalamūlaṃ", S_ADOSA_METTA)
note("adoso adussanā adussitattaṃ…pe… abyāpādo abyāpajjo adoso kusalamūlaṃ", S_ADOSA_PE)

TRUTHS = [("Dukkhe", "страдания"), ("dukkhasamudaye", "возникновения страдания"),
          ("dukkhanirodhe", "прекращения страдания"),
          ("dukkhanirodhagāminiyā paṭipadāya", "способа практики, ведущего к прекращению страдания"),
          ("pubbante", "прошлого"), ("aparante", "будущего"), ("pubbantāparante", "прошлого и будущего"),
          ("idappaccayatā paṭiccasamuppannesu dhammesu",
           "закона обусловленности и явлений, возникших в зависимости от условий")]
KNOW = ", ".join(f"знание {g}" for _, g in TRUTHS)
UNKNOW = ", ".join(f"незнание {g}" for _, g in TRUTHS)
note("Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, … idappaccayatā paṭiccasamuppannesu dhammesu ñāṇaṃ", cap(KNOW))
note("Dukkhe aññāṇaṃ, … idappaccayatā paṭiccasamuppannesu dhammesu aññāṇaṃ", cap(UNKNOW))
AMOHA = f"{cap(KNOW)}; то, что есть такая {S.S_PANNA}"
AMOHA_MAGGA = AMOHA + ", " + C.SUFFIX["dhammavicayasambojjhaṅgo"] + ", " + C.MAGGA_R
MOHA = f"{cap(UNKNOW)}; то, что есть такое {D.S_MOHA}"
assert D.S_MOHA.startswith("незнание, ")

# lobha: the long string (^1-1065 with variants, ^1-1141 without)
LOBHA_ITEMS = [
    ("rāgo", "страсть"), ("sārāgo", "пристрастие"), ("anunayo", "расположенность"), ("anurodho", "потакание"),
    ("nandī", "наслаждение"), ("nandīrāgo", "страсть к наслаждению"), ("cittassa sārāgo", "пристрастие ума"),
    ("icchā", "хотение"), ("mucchā", "одурманенность"), ("ajjhosānaṃ", "поглощённость"),
    ("gedho", "жадное стремление"), ("paligedho", "сильное жадное стремление"), ("saṅgo", "привязанность"),
    ("paṅko", "трясина"), ("ejā", "трепет"), ("māyā", "наваждение"), ("janikā", "порождающая сила"),
    ("sañjananī", "производящая сила"), ("sibbinī", "сшивающая сила"), ("jālinī", "опутывающая сила"),
    ("saritā", "увлекающая сила"), ("visattikā", "липкая сила"), ("suttaṃ", "нить"),
    ("visaṭā", "расползающаяся сила"), ("āyūhinī", "побуждающая сила"), ("dutiyā", "спутница"),
    ("paṇidhi", "устремление"), ("bhavanetti", "проводник к существованию"), ("vanaṃ", "лес"),
    ("vanatho", "чаща"), ("santhavo", "близость"), ("sineho", "приязнь"), ("apekkhā", "томление"),
    ("paṭibandhu", "родство"), ("āsā", "надежда"), ("āsisanā", "упование"), ("āsisitattaṃ", "состояние упования"),
    ("rūpāsā", "надежда на видимые формы"), ("saddāsā", "надежда на звуки"), ("gandhāsā", "надежда на запахи"),
    ("rasāsā", "надежда на вкусы"), ("phoṭṭhabbāsā", "надежда на осязаемое"),
    ("lābhāsā", "надежда на приобретения"), ("dhanāsā", "надежда на богатство"), ("puttāsā", "надежда на детей"),
    ("jīvitāsā", "надежда на жизнь"), ("jappā", "тяга"), ("pajappā", "сильная тяга"),
    ("abhijappā", "чрезмерная тяга"), ("jappā", "тяга"), ("jappanā", "проявление тяги"),
    ("jappitattaṃ", "состояние тяги"), ("loluppaṃ", "падкость"), ("loluppāyanā", "проявление падкости"),
    ("loluppāyitattaṃ", "состояние падкости"), ("pucchañjikatā", "угодливость"),
    ("sādhukamyatā", "желание лучшего"), ("adhammarāgo", "неправедная страсть"),
    ("visamalobho", "непомерная жадность"), ("nikanti", "тяготение"), ("nikāmanā", "страстное желание"),
    ("patthanā", "чаяние"), ("pihanā", "вожделение"), ("sampatthanā", "сильное чаяние"),
    ("kāmataṇhā", "чувственная жажда"), ("bhavataṇhā", "жажда существования"),
    ("vibhavataṇhā", "жажда несуществования"), ("rūpataṇhā", "жажда мира форм"),
    ("arūpataṇhā", "жажда мира без форм"), ("nirodhataṇhā", "жажда прекращения"),
    ("rūpataṇhā", "жажда видимых форм"), ("saddataṇhā", "жажда звуков"), ("gandhataṇhā", "жажда запахов"),
    ("rasataṇhā", "жажда вкусов"), ("phoṭṭhabbataṇhā", "жажда осязаемого"), ("dhammataṇhā", "жажда объектов ума"),
    ("ogho", "поток"), ("yogo", "ярмо"), ("gantho", "узы"), ("upādānaṃ", "цепляние"), ("āvaraṇaṃ", "препятствие"),
    ("nīvaraṇaṃ", "помеха"), ("chādanaṃ", "покров"), ("bandhanaṃ", "путы"), ("upakkileso", "загрязнение"),
    ("anusayo", "скрытая склонность"), ("pariyuṭṭhānaṃ", "одержимость"), ("latā", "лиана"),
    ("vevicchaṃ", "скаредность"), ("dukkhamūlaṃ", "корень страдания"), ("dukkhanidānaṃ", "источник страдания"),
    ("dukkhappabhavo", "исток страдания"), ("mārapāso", "силки Мары"), ("mārabaḷisaṃ", "крючок Мары"),
    ("māravisayo", "владения Мары"), ("taṇhānadī", "река жажды"), ("taṇhājālaṃ", "сеть жажды"),
    ("taṇhāgaddulaṃ", "привязь жажды"), ("taṇhāsamuddo", "океан жажды"), ("abhijjhā", "алчность"),
    ("lobho akusalamūlaṃ", "жадность как неблагой корень"),
]
assert D.S_LOBHA.endswith("алчность, жадность как неблагой корень")
LOBHA_VAR = {   # variant after the item (^1-1065 only)
    "nandīrāgo": S.spell("Sī.", "nandirāgo"),
    "sibbinī": S.spell("Sī.", "sibbanī"),
    "āyūhinī": S.spell("Sī., Syā.", "āyūhanī"),
    "āsisitattaṃ": S.spell("Sī., Syā.", "āsiṃsanā āsiṃsitattaṃ"),
    "pucchañjikatā": "[вариант написания (Syā.): puñcikatā; (Sī.): pucchikatā]",
}
LOBHA_P_PLAIN = " ".join(p for p, _ in LOBHA_ITEMS)


def lobha(var):
    return ", ".join(r + (" " + LOBHA_VAR[p] if var and p in LOBHA_VAR else "") for p, r in LOBHA_ITEMS)


note(LOBHA_P_PLAIN, lobha(False))

# dosa: the grounds of annoyance and the long string
AGHATA = ("При мысли «он причинил мне вред» возникает досада, при мысли «он причиняет мне вред» возникает "
          "досада, при мысли «он причинит мне вред» возникает досада, при мысли «он причинил вред дорогому и "
          "приятному мне человеку… причиняет вред… причинит вред» возникает досада, при мысли «он принёс пользу "
          "не дорогому и неприятному мне человеку… приносит пользу… принесёт пользу» возникает досада, или же "
          "досада возникает без повода.")
DOSA_HEAD = ("досада ума, раздражение, неприязнь, противодействие, негодование, сильное негодование, крайнее "
             "негодование, злоба, сильная злоба, крайняя злоба, недоброжелательность ума, сильная злоба ума, гнев, "
             "гневливость, состояние гнева")
DOSA = f"{AGHATA} То, что есть такая {DOSA_HEAD}, {D.S_DOSA}"
note("Anatthaṃ me acarīti āghāto jāyati, … aṭṭhāne vā pana āghāto jāyati.", AGHATA)
note("Yo evarūpo cittassa āghāto paṭighāto … kodho kujjhanā kujjhitattaṃ doso dussanā … anattamanatā cittassa",
     f"То, что есть такая {DOSA_HEAD}, {D.S_DOSA}")

# diṭṭhi: «paṭiggāho» (цепкость) in ^1-1007, 1009, 1105, 1122; «patiṭṭhāho» (закрепление) as 2-04
DIITHI_TAT = D.S_DIITHI                                   # … хватка, закрепление, …
assert DIITHI_TAT == D.S_DIITHI_HEAD + ", " + D.S_DIITHI_TAIL and D.S_DIITHI_HEAD.endswith(", закрепление")
DIITHI_PAT = D.S_DIITHI_HEAD[:-len("закрепление")] + "цепкость, " + D.S_DIITHI_TAIL
DIITHI_PAT_VAR = DIITHI_PAT.replace("извращённость воззрений",
                                    "извращённость воззрений " + S.spell("Sī.", "diṭṭhivisūkāyitaṃ"), 1)
note("diṭṭhi diṭṭhigataṃ … gāho paṭiggāho abhiniveso … vipariyāsaggāho", DIITHI_PAT)

VIEWS = ["мир вечен", "мир не вечен", "мир конечен", "мир бесконечен", "душа то же самое, что и плоть",
         "душа одно, а плоть другое", "Татхагата существует после смерти", "Татхагата не существует после смерти",
         "Татхагата и существует, и не существует после смерти",
         "Татхагата не существует и не не существует после смерти"]


def views(suffix=""):
    vs = [f"«{v}{suffix}»" for v in VIEWS]
    vs[0] = "«" + cap(vs[0][1:])
    return vs[0] + "".join(f", или {v}" for v in vs[1:])


TEN_VIEWS = views()
TEN_VIEWS_TRUE = views(", только это истинно, всё прочее ложно")
note("Sassato lokoti vā, asassato lokoti vā, … neva hoti na na hoti tathāgato paraṃ maraṇāti vā", TEN_VIEWS)
note("Sassato loko, idameva saccaṃ moghamaññanti vā; … (the ten views)", TEN_VIEWS_TRUE)
ALL_WRONG = "всякое ложное воззрение является {}"         # sabbāpi micchādiṭṭhi X
note("Sabbāpi micchādiṭṭhi X.", cap(ALL_WRONG.format("X (instrumental)")) + ".")

# vicikicchā
DOUBT_OBJ = ["Учителя", "Учения", "Общины", "обучения"] + [g for _, g in TRUTHS[4:]]
DOUBT = cap(", ".join(f"сомневаются и колеблются в отношении {o}" for o in DOUBT_OBJ))
VICIK = f"То, что есть такое {D.S_VICIKICCHA}"
note("Satthari kaṅkhati vicikicchati, dhamme …, saṅghe …, sikkhāya …, pubbante …, aparante …, pubbantāparante …, "
     "idappaccayatā paṭiccasamuppannesu dhammesu kaṅkhati vicikicchati", DOUBT)

# sīlabbataparāmāsa
SUDDHI = "чистота благодаря обрядам, чистота благодаря обетам, чистота благодаря обрядам и обетам"
SILABBATA_HEAD = f"Воззрение отшельников и брахманов вне этого Учения: «{SUDDHI}»; то, что есть такое "
note("Ito bahiddhā samaṇabrāhmaṇānaṃ ‘sīlena suddhi, vatena suddhi, sīlabbatena suddhī’ti yā evarūpā diṭṭhi …",
     SILABBATA_HEAD + "воззрение, …")

# sakkāyadiṭṭhi
SAKKAYA_HEAD = ("Вот обычный человек, не слышавший Учения, не видевший благородных, не сведущий в Учении благородных, "
                "не обученный Учению благородных, не видевший достойных людей, не сведущий в Учении достойных людей, "
                "не обученный Учению достойных людей, ")
KH5 = [  # (accusative, instrumental, prepositional, «находящ-» ending of the accusative)
    ("материальную форму", "материальной формой", "материальной форме", "ейся"),
    ("чувство", "чувством", "чувстве", "имся"),
    ("восприятие", "восприятием", "восприятии", "имся"),
    ("формирующие факторы", "формирующими факторами", "формирующих факторах", "имися"),
    ("сознание", "сознанием", "сознании", "имся"),
]


def regards(acc, ins, prep, end):
    return (f"считает {acc} самостью, или самость обладающей {ins}, или {acc} находящ{end} в самости, "
            f"или самость находящейся в {prep}.")


SAKKAYA = SAKKAYA_HEAD + regards(*KH5[0]) + " " + " ".join(cap(regards(*k)) for k in KH5[1:])
note("Idha assutavā puthujjano … rūpaṃ attato samanupassati, rūpavantaṃ vā attānaṃ, attani vā rūpaṃ, "
     "rūpasmiṃ vā attānaṃ. …", SAKKAYA)

# āsava, fetter, tie names: (nominative, instrumental, genitive, dative)
KAMA_STR = ("чувственное желание, чувственная страсть, чувственное наслаждение, чувственная жажда, чувственная "
            "приязнь, чувственный жар, чувственная одурманенность, чувственная поглощённость")
BHAVA_ITEMS = ["желание существования", "страсть к существованию", "наслаждение существованием",
               "жажда существования", "приязнь к существованию", "жар существования",
               "одурманенность существованием", "поглощённость существованием"]


def bhava(var):
    it = list(BHAVA_ITEMS)
    if var:
        it[0] += " " + S.spell("Sī., Syā.", "bhavacchando")
    return ", ".join(it)


KAMA_BODY = f"То, что есть в отношении чувственных удовольствий {KAMA_STR}"
BHAVA_BODY = "То, что есть в отношении существования {}"
note("Yo kāmesu kāmacchando kāmarāgo kāmanandī kāmataṇhā kāmasineho kāmapariḷāho kāmamucchā kāmajjhosānaṃ",
     KAMA_BODY)
note("Yo bhavesu bhavachando bhavarāgo bhavanandī bhavataṇhā bhavasineho bhavapariḷāho bhavamucchā bhavajjhosānaṃ",
     BHAVA_BODY.format(bhava(False)))

ASAVA = {"kāmāsavo": ("влечение к чувственным удовольствиям", "влечением к чувственным удовольствиям",
                      "влечения к чувственным удовольствиям", "влечению к чувственным удовольствиям"),
         "bhavāsavo": ("влечение к существованию", "влечением к существованию", "влечения к существованию",
                       "влечению к существованию"),
         "diṭṭhāsavo": ("влечение воззрений", "влечением воззрений", "влечения воззрений", "влечению воззрений"),
         "avijjāsavo": ("влечение неведения", "влечением неведения", "влечения неведения", "влечению неведения")}
SAMY_GEN = {"kāmarāga": "чувственной страсти", "paṭigha": "неприязни", "māna": "самомнения", "diṭṭhi": "воззрений",
            "vicikicchā": "колебания", "sīlabbataparāmāsa": "приверженности обрядам и обетам",
            "bhavarāga": "страсти к существованию", "issā": "зависти", "macchariya": "скупости",
            "avijjā": "неведения"}
SAMY = {k: (f"оковы {g}", f"оковами {g}", f"оков {g}", f"оковам {g}") for k, g in SAMY_GEN.items()}
GAN_GEN = {"abhijjhā": "алчности", "byāpādo": "недоброжелательности",
           "sīlabbataparāmāso": "приверженности обрядам и обетам",
           "idaṃsaccābhiniveso": "приверженности убеждению «только это истинно»"}
GAN = {k: (f"телесные узы {g}", f"телесными узами {g}", f"телесных уз {g}", f"телесным узам {g}")
       for k, g in GAN_GEN.items()}
for _k, _v in SAMY.items():
    note(f"{_k}saṃyojanaṃ", _v[0])
for _k, _v in GAN.items():
    note(f"{_k} kāyagantho", _v[0])

MANA = ("Самомнение «я лучше», самомнение «я равный», самомнение «я хуже». То, что есть такое самомнение, "
        "зазнайство, состояние зазнайства, превознесение, надменность " + S.spell("Syā.", "uṇṇati uṇṇāmo")
        + ", знамя, возвеличивание себя, желание ума поднять свой стяг")
ISSA = ("То, что есть в отношении приобретений, почестей, уважения, почитания, поклонов и поклонения, получаемых "
        "другими, зависть, проявление зависти, состояние зависти, ревность, проявление ревности, состояние ревности "
        + S.spell("Ka.", "ussuyā ussuyanā ussuyitattaṃ"))
MACCH = ("Пять видов скупости – скупость в отношении жилища, скупость в отношении семей-покровителей, скупость в "
         "отношении приобретений, скупость в отношении похвалы, скупость в отношении Учения. То, что есть такая "
         "скупость, проявление скупости, состояние скупости, скаредность, прижимистость, мелочность, зажатость ума")
note("Seyyohamasmīti māno, … Yo evarūpo māno … ketukamyatā cittassa", MANA)
note("Yā paralābhasakkāragarukāramānanavandanapūjanāsu issā … usūyitattaṃ", ISSA)
note("Pañca macchariyāni – … Yaṃ evarūpaṃ maccheraṃ … aggahitattaṃ cittassa", MACCH)

# =========================================================================================
# 4. Relational frames of the pairs («Tehi dhammehi …», «X Y-ena Z ceva Z-sampayutto ca»)
# =========================================================================================
REL = "по отношению к этим явлениям"                         # Tehi dhammehi
THOSE = "Те явления, которые {}:"                           # Tehi dhammehi ye dhammā X
AMONG = "Среди явлений, которые {}, кроме этих явлений"      # Tehi dhammehi ye dhammā X, te dhamme ṭhapetvā
note("Tehi dhammehi ye dhammā sahetukā / ahetukā", THOSE.format(f"{REL} имеют корни / не имеют корней"))
note("Tehi dhammehi ye dhammā sampayuttā / vippayuttā", THOSE.format("связаны / не связаны с этими явлениями"))
note("Tehi dhammehi ye dhammā X, te dhamme ṭhapetvā", AMONG.format("…"))
note("X Y-ena Z ceva Z-sampayutto ca", "X по отношению к Y является Z и связан(а/о) с Z")
note("Lobho mohena hetu ceva sahetuko ca", "жадность по отношению к заблуждению является корнем и имеет корни")
note("Teyeva āsavā āsavā ceva sāsavā ca. (likewise Tāneva saṃyojanāni …, Teva ganthā …)",
     "Те самые влечения и есть явления, являющиеся влечениями и подверженные влечениям.")


def rel_pairs(pairs, pred):
    return ", ".join(f"{a} по отношению к {b} {pred(a)}" for a, b in pairs)


# =========================================================================================
# 5. Headings and closing lines
# =========================================================================================
EXACT = {
    "### Nikkhepakaṇḍaṃ": "### " + S.CH_HEADINGS["Nikkhepakaṇḍaṃ"],
    "#### Tikanikkhepaṃ": "#### Сводка троек",
    "#### Dukanikkhepaṃ": "#### Сводка пар",
    "##### Hetugocchakaṃ": "##### " + S.CLUSTERS["hetu"]["heading"],
    "##### Cūḷantaradukaṃ": "##### " + S.CUULANTARA,
    "##### Āsavagocchakaṃ": "##### " + S.CLUSTERS["asava"]["heading"],
    "##### Saṃyojanagocchakaṃ": "##### " + S.CLUSTERS["samyojana"]["heading"],
    "##### Ganthagocchakaṃ": "##### " + S.CLUSTERS["gantha"]["heading"],
    "Tikaṃ.": "Тройки.",
    "Nikkhepakaṇḍe paṭhamabhāṇavāro.": f"{S.BHANAVARA_1} в разделе {low(S.CH_HEADINGS['Nikkhepakaṇḍaṃ'])[7:]}.",
    "Ime tayo kusalahetū.": "Это три благих корня.",
    "Ime tayo akusalahetū.": "Это три неблагих корня.",
    "Ime dhammā āsavā.": "Это " + N["āsavā"] + ".",
    "Ime dhammā saṃyojanā.": "Это " + N["saṃyojanā"] + ".",
    "Ime dhammā ganthā.": "Это " + N["ganthā"] + ".",
}
assert EXACT["Nikkhepakaṇḍe paṭhamabhāṇavāro."] == "Первый раздел для чтения вслух в разделе сводки."
for _p, _r in EXACT.items():
    note(_p, _r)

# =========================================================================================
# 6. The segments
# =========================================================================================
R = {}


def seg(sid, *lines):
    assert sid not in R, sid
    R[sid] = list(lines)


# ---------------------------------------------------------------- triads
seg("1-985", qa("kusalā", f"{ROOTS_K}; {TAMSAMP} {AGG4}; {KAMMA3}", False))
seg("1-986", qa("akusalā", f"{ROOTS_A}; {KILESA}; {TAMSAMP} {AGG4}; {KAMMA3}", False))
seg("1-987", qa("abyākatā", f"{cap(AGG4)}, {RES}, {SPH4}, {KIR}, {SABBA}", False))
seg("1-988", qa("sukhāya vedanāya sampayuttā",
                f"На уровне счастья {locs('krp')}, кроме приятного чувства, связанные с ним {AGG3}", False))
seg("1-989", qa("dukkhāya vedanāya sampayuttā",
                f"На уровне боли {locs('k')}, кроме болезненного чувства, связанные с ним {AGG3}", False))
seg("1-990", qa("adukkhamasukhāya vedanāya sampayuttā",
                f"На уровне того, что ни болезненно, ни приятно, {locs('krap')}, кроме чувства, которое ни "
                f"болезненно, ни приятно, связанные с ним {AGG3}", False))
seg("1-991", qa("vipākā", f"{cap(AGG4_PE)}, {RES}, {SPH4}", True))
seg("1-992", qa("vipākadhammadhammā", f"{cap(KA)}, {SPH4}: {AGG4_PE}", False))
seg("1-993", qa("nevavipākanavipākadhammadhammā", f"{cap(KIR[2:])}, {SABBA}", False))
seg("1-994", qa("upādiṇṇupādāniyā", f"{cap(AGG4_PE)}, {RES}, {SAS} и {SPH3}, {YANCA_KAMMA}", True))
seg("1-995", qa("anupādiṇṇupādāniyā", f"{cap(SAS)} {KA}, {SPH3}: {AGG4_PE}; {KIR}; {YANCA_NA_KAMMA}", True))
seg("1-996", qa("anupādiṇṇaanupādāniyā", LOKUTTARA, False))
seg("1-997", qa("saṃkiliṭṭhasaṃkilesikā", f"{ROOTS_A}; {KILESA}; {TAMSAMP} {AGG4_PE}; {KAMMA3}", False))
seg("1-998", qa("asaṃkiliṭṭhasaṃkilesikā", f"{cap(SAS)} {KABY}, {SPH3}: {AGG5}", False))
seg("1-999", qa("asaṃkiliṭṭhaasaṃkilesikā", LOKUTTARA, False))
seg("1-1000", qa("savitakkasavicārā",
                 f"На уровне с направленной мыслью и удержанием мысли {locs('krp')}, кроме направленной мысли и "
                 f"удержания мысли, связанные с ними {AGG4_PE}", False))
seg("1-1001", qa("avitakkavicāramattā",
                 f"На уровне без направленной мысли, только с удержанием мысли, {locs('rp')}, кроме удержания "
                 f"мысли, связанные с ним {AGG4_PE}", False))
seg("1-1002", qa("avitakkaavicārā",
                 f"На уровне без направленной мысли и без удержания мысли {locs('krap')}: {AGG4_PE}; {SABBA}", False))
seg("1-1003", qa("pītisahagatā", f"На уровне восторга {locs('krp')}, кроме восторга, связанные с ним {AGG4_PE}",
                 False))
seg("1-1004", qa("sukhasahagatā", f"На уровне счастья {locs('krp')}, кроме счастья, связанные с ним {AGG3}", False))
seg("1-1005", qa("upekkhāsahagatā",
                 f"На уровне невозмутимости {locs('krap')}, кроме невозмутимости, связанные с ней {AGG3}", False))
seg("1-1006", f"{Q('dassanena pahātabbā')} {SAMYOJ3}.")
SAKK, VICI, SILA = "воззрение о самости", "колебание", "приверженность обрядам и обетам"
SAKK_I, VICI_I, SILA_I = "воззрением о самости", "колебанием", "приверженностью обрядам и обетам"
seg("1-1007", f"{TATTHA.format(SAKK)} {SAKKAYA} То, что есть такое {DIITHI_PAT_VAR}, – {CALLED.format(SAKK_I)}")
seg("1-1008", f"{TATTHA.format(VICI)} {DOUBT}. {VICIK}, – {CALLED.format(VICI_I)}")
seg("1-1009", f"{TATTHA.format(SILA)} {SILABBATA_HEAD}{DIITHI_PAT}, – {CALLED.format(SILA_I)}")
DASS_BODY = f"Эти три оковы; {KILESA}; {TAMSAMP} {AGG4_PE}; {KAMMA3}"
seg("1-1010", ans(DASS_BODY, "dassanena pahātabbā", False))
seg("1-1011", qa("bhāvanāya pahātabbā", f"Остальные {LDM}; {KILESA}; {TAMSAMP} {AGG4_PE}; {KAMMA3}", False))
seg("1-1012", qa("neva dassanena na bhāvanāya pahātabbā", f"{cap(KABY)}, {SPH4}: {AGG4_PE}; {SABBA}", False))
seg("1-1013", f"{Q('dassanena pahātabbahetukā')} {SAMYOJ3}.")
seg("1-1014", f"Что такое здесь {SAKK}{ELL} {CALLED.format(SAKK_I)}")
seg("1-1015", f"Что такое здесь {VICI}{ELL} {CALLED.format(VICI_I)}")
seg("1-1016", f"Что такое здесь {SILA}{ELL} {CALLED.format(SILA_I)}")
ROOTS_D = "это корни, устраняемые видением истины."          # ime dhammā dassanena pahātabbahetū
ROOTS_B = "это корни, устраняемые развитием ума."            # ime dhammā bhāvanāya pahātabbahetū
note("– ime dhammā dassanena / bhāvanāya pahātabbahetū.", f"– {ROOTS_D} / – {ROOTS_B}")
TAIL_KB = f"{cap(KILESA)}; {TAMSAMP} {AGG4_PE}; {KAMMA3}"
seg("1-1017", f"{ans(DASS_BODY, 'dassanena pahātabbahetukā', False)} {ans(SAMYOJ3, 'dassanena pahātabbā', False)} "
              f"Пребывающие вместе с ними {LDM} – {ROOTS_D} {ans(TAIL_KB, 'dassanena pahātabbahetukā', False)}")
seg("1-1018", f"{Q('bhāvanāya pahātabbahetukā')} Остальные {LDM} – {ROOTS_B} "
              f"{ans(TAIL_KB, 'bhāvanāya pahātabbahetukā', False)}")
EXC4 = f"{EXCEPT} {KAA}, {SPH4}"
EXC3 = f"{EXCEPT} {KAA}, {SPH3}"
seg("1-1019", qa("neva dassanena na bhāvanāya pahātabbahetukā", f"{EXC4}: {AGG4}; {SABBA}", False))
seg("1-1020", qa("ācayagāmino", f"{cap(SAS)} {KA}, {SPH3}: {AGG4_PE}", False))
seg("1-1021", qa("apacayagāmino", FOUR_PATHS, True))
seg("1-1022", qa("neva ācayagāmi na apacayagāmino", f"{cap(AGG4_PE)}, {RES}, {SPH4}, {KIR}, {SABBA}", False))
seg("1-1023", qa("sekkhā", f"{FOUR_PATHS}, и три низших плода отшельничества", False))
seg("1-1024", qa("asekkhā", f"Высший {S.reading('Syā.', 'uparimaṃ')} плод состояния архата", False))
seg("1-1025", qa("nevasekkhanāsekkhā", f"{EXC3}: {AGG4_PE}; {SABBA}", False))
seg("1-1026", qa("parittā", f"Все {KAA}, относящиеся к миру чувственных желаний: {AGG5_PE}", False))
seg("1-1027", qa("mahaggatā", f"{cap(KABY)}, относящиеся к миру форм или к миру без форм: {AGG4_PE}", False))
seg("1-1028", qa("appamāṇā", LOKUTTARA, False))
OBJ = "Ум и сопутствующие уму явления, которые возникают, имея объектом {}"   # X ārabbha ye uppajjanti cittacetasikā
note("X dhamme ārabbha ye uppajjanti cittacetasikā dhammā", OBJ.format("X явления"))
seg("1-1029", qa("parittārammaṇā", OBJ.format("ограниченные явления"), True))
seg("1-1030", qa("mahaggatārammaṇā", OBJ.format("возвышенные явления"), True))
seg("1-1031", qa("appamāṇārammaṇā", OBJ.format("безмерные явления"), True))
seg("1-1032", qa("hīnā", f"{ROOTS_A}; {KILESA}; {TAMSAMP} {AGG4_PE}; {KAMMA3}", False))
seg("1-1033", qa("majjhimā", f"{cap(SAS)} {KABY}, {SPH3}: {AGG5_PE}", False))
seg("1-1034", qa("paṇītā", LOKUTTARA, False))
seg("1-1035", qa("micchattaniyatā", "Пять действий с немедленным воздаянием и то ложное воззрение, которое "
                                    "предопределено", True))
seg("1-1036", qa("sammattaniyatā", FOUR_PATHS, True))
seg("1-1037", qa("aniyatā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1038", qa("maggārammaṇā", OBJ.format("благородный путь"), True))
SAMANGI = "У обладающего благородным путём"                   # Ariyamaggasamaṅgissa
MH = "maggahetukā"
seg("1-1039", f"{Q(MH)} {ans(f'{SAMANGI}, кроме факторов пути, связанные с ними {AGG4_PE}', MH, False)} "
              f"{ans(f'{SAMANGI} правильное воззрение является и путём, и корнем; кроме правильного воззрения, связанные с ним {AGG4_PE}', MH, False)} "
              f"{SAMANGI} отсутствие жадности, отсутствие злобы, отсутствие заблуждения – это корни пути. "
              f"{ans(f'{cap(TAMSAMP)} {AGG4_PE}', MH, False)}")
MA = "maggādhipatino"
seg("1-1040", f"{Q(MA)} "
              f"{ans('Ум и сопутствующие уму явления, которые возникают, взяв благородный путь в качестве главенствующего', MA, True)} "
              f"{ans(f'{SAMANGI}, развивающего путь с преобладанием пытливости, кроме пытливости, связанные с ней {AGG4_PE}', MA, False)}")
note("Ariyamaggasamaṅgissa", SAMANGI)
note("Ariyamaggaṃ adhipatiṃ karitvā ye uppajjanti cittacetasikā dhammā",
     "Ум и сопутствующие уму явления, которые возникают, взяв благородный путь в качестве главенствующего")
KH5_NOM = "материальная форма, чувство, восприятие, формирующие факторы, сознание"
KH5_NOM_VAR = KH5_NOM.replace("материальная форма", "материальная форма [вариант чтения (во многих изданиях): rūpā]")
POS = ["рождённые", "ставшие", "зародившиеся", "появившиеся", "полностью появившиеся", "проявившиеся",
       "возникшие", "полностью возникшие", "поднявшиеся", "полностью поднявшиеся"]
NEG = ["не рождённые", "не ставшие", "не зародившиеся", "не появившиеся", "не появившиеся полностью",
       "не проявившиеся", "невозникшие", "не возникшие полностью", "не поднявшиеся", "не поднявшиеся полностью"]


def time_list(parts, last, cat, nom=KH5_NOM):
    return f"Явления, {', '.join(parts)}, {last}, включённые в категорию {cat}: {nom}"


note("Ye dhammā jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā uppannā samuppannā uṭṭhitā samuṭṭhitā",
     "Явления, " + ", ".join(POS))
note("ajātā abhūtā asañjātā anibbattā anabhinibbattā apātubhūtā anuppannā asamuppannā anuṭṭhitā asamuṭṭhitā",
     ", ".join(NEG))
note("X Xaṃsena saṅgahitā", "X, включённые в категорию X (genitive plural)")
note("rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ", KH5_NOM)
seg("1-1041", qa("uppannā", time_list(POS, "возникшие", "возникших", KH5_NOM_VAR), False))
seg("1-1042", qa("anuppannā", time_list(NEG, "невозникшие", "невозникших"), False))
seg("1-1043", qa("uppādino", f"{cap(AGG4_PE)}, являющиеся результатом благих и неблагих явлений, чьи результаты "
                             f"ещё не созрели, {SPH4}, {YANCA_UPP}", True))
PAST = ["прошлые", "прекратившиеся", "исчезнувшие", "изменившиеся", "угасшие", "полностью угасшие",
        "исчезнувшие после возникновения"]
note("atītā niruddhā vigatā vipariṇatā atthaṅgatā abbhatthaṅgatā uppajjitvā vigatā", ", ".join(PAST))
seg("1-1044", qa("atītā", time_list(PAST, "прошлые", "прошлых"), False))
seg("1-1045", qa("anāgatā", time_list(NEG, "будущие", "будущих"), False))
seg("1-1046", qa("paccuppannā", time_list(POS, "настоящие", "настоящих"), False))
seg("1-1047", qa("atītārammaṇā", OBJ.format("прошлые явления"), True))
seg("1-1048", qa("anāgatārammaṇā", OBJ.format("будущие явления"), True))
seg("1-1049", qa("paccuppannārammaṇā", OBJ.format("настоящие явления"), True))
INNER = ("Явления, которые у {} находятся внутри себя, являются собственными, закреплёнными, индивидуальными и "
         "охваченными цеплянием: " + KH5_NOM)
note("Ye dhammā tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyatā pāṭipuggalikā upādiṇṇā",
     INNER.format("тех или иных существ")[:-len(": " + KH5_NOM)])
seg("1-1050", qa("ajjhattā", INNER.format("тех или иных существ"), False))
seg("1-1051", qa("bahiddhā", INNER.format("тех или иных других существ, других личностей"), False))
seg("1-1052", qa("ajjhattabahiddhā", "И то и другое", False))
seg("1-1053", qa("ajjhattārammaṇā", OBJ.format("внутренние явления"), True))
seg("1-1054", qa("bahiddhārammaṇā", OBJ.format("внешние явления"), True))
seg("1-1055", qa("ajjhattabahiddhārammaṇā", OBJ.format("внутренние и внешние явления"), True))
RUPAYATANA = cap(T.NOUN["rūpāyatanaṃ"][0])                   # Сфера видимых форм
SENSE9 = [T.NOUN[p][0] for p in ("cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ",
                                 "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ")]
SENSE9_R = cap(", ".join(SENSE9[:-1]) + " и " + SENSE9[-1])
SENSE_PE = f"{cap(SENSE9[0])}{ELL} {SENSE9[-1]}"
seg("1-1056", qa("sanidassanasappaṭighā", RUPAYATANA, False))
seg("1-1057", qa("anidassanasappaṭighā", SENSE9_R, False))
seg("1-1058", qa("anidassanaappaṭighā", f"{cap(AGG4)}; {YANCA_ANID}; и {ASANKH}", False), EXACT["Tikaṃ."])

# ---------------------------------------------------------------- the root group
HK, HA, HAB = "благих корня", "неблагих корня", "этически неопределённых корня"
SPH_H = {"kāmāvacara": "относящихся к миру чувственных желаний", "rūpāvacara": "относящихся к миру форм",
         "arūpāvacara": "относящихся к миру без форм", "apariyāpanna": "не принадлежащих к кругам существования"}
NINE = f"девять корней, {SPH_H['kāmāvacara']}"
SIX = {k: f"шесть корней, {v}" for k, v in SPH_H.items() if k != "kāmāvacara"}
THREE_ROOTS = f"Три {HK}, три {HA}, три {HAB}"
seg("1-1059", f"{Q('hetū')} {THREE_ROOTS}, {NINE}, {SIX['rūpāvacara']}, {SIX['arūpāvacara']}, "
              f"{SIX['apariyāpanna']}.")
ALOBHA = "отсутствие жадности"
ADOSA = "отсутствие злобы"
AMOHA_N = "отсутствие заблуждения"
ROOTS_KN = f"{cap(ALOBHA)}, {ADOSA}, {AMOHA_N}"
seg("1-1060", f"{TATTHA.format('три ' + HK)} {ROOTS_KN}.")
seg("1-1061", f"{TATTHA.format(ALOBHA)} То, что есть {S.S_ALOBHA}, – {CALLED.format('отсутствием жадности')}")
seg("1-1062", f"{TATTHA.format(ADOSA)} То, что есть {S_ADOSA_METTA}, – {CALLED.format('отсутствием злобы')}")
seg("1-1063", f"{TATTHA.format(AMOHA_N)} {AMOHA}, – {CALLED.format('отсутствием заблуждения')}",
    EXACT["Ime tayo kusalahetū."])
seg("1-1064", f"{TATTHA.format('три ' + HA)} {cap(LDM)}.")
seg("1-1065", f"{TATTHA.format('жадность')} То, что есть {lobha(True)}, – {CALLED.format('жадностью')}")
seg("1-1066", f"{TATTHA.format('злоба')} {DOSA}, – {CALLED.format('злобой')}")
seg("1-1067", f"{TATTHA.format('заблуждение')} {MOHA}, – {CALLED.format('заблуждением')}",
    EXACT["Ime tayo akusalahetū."])
VIPAKATO = "в виде результатов благих явлений"                 # kusalānaṃ dhammānaṃ vipākato
KIRIYA_LOC = "в этически неопределённых функциональных явлениях"   # kiriyābyākatesu dhammesu
seg("1-1068", f"{TATTHA.format('три ' + HAB)} {ROOTS_KN} {VIPAKATO} или {KIRIYA_LOC} – это три {HAB}.")
seg("1-1069", f"{TATTHA.format(NINE)} {THREE_ROOTS} – это {NINE}.")
for _sid, _k in (("1-1070", "rūpāvacara"), ("1-1071", "arūpāvacara"), ("1-1072", "apariyāpanna")):
    seg(_sid, f"{TATTHA.format(SIX[_k])} Три {HK}, три {HAB} – это {SIX[_k]}.")
seg("1-1073", f"{TATTHA.format('три ' + HK)} {ROOTS_KN}.")
seg("1-1074", f"{TATTHA.format(ALOBHA)} То, что есть {S.S_ALOBHA}, – {CALLED.format('отсутствием жадности')}")
seg("1-1075", f"{TATTHA.format(ADOSA)} То, что есть {S_ADOSA_PE}, – {CALLED.format('отсутствием злобы')}")
seg("1-1076", f"{TATTHA.format(AMOHA_N)} {AMOHA_MAGGA}, – {CALLED.format('отсутствием заблуждения')}",
    EXACT["Ime tayo kusalahetū."])
seg("1-1077", f"{TATTHA.format('три ' + HAB)} {ROOTS_KN} {VIPAKATO} – это три {HAB}. "
              f"{ans('Эти ' + SIX['apariyāpanna'], 'hetū', True)}")
seg("1-1078", qa("na hetū", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1079", qa("sahetukā", f"{THOSE.format(REL + ' имеют корни')} {AGG4_PE}", False))
seg("1-1080", qa("ahetukā", f"{THOSE.format(REL + ' не имеют корней')} {AGG4_PE}, {SABBA}", False))
seg("1-1081", qa("hetusampayuttā", f"{THOSE.format('связаны с этими явлениями')} {AGG4_PE}", False))
seg("1-1082", qa("hetuvippayuttā", f"{THOSE.format('не связаны с этими явлениями')} {AGG4_PE}, {SABBA}", False))
NOM = {"lobho": "жадность", "moho": "заблуждение", "doso": "злоба"}
DAT = {"mohena": "заблуждению", "lobhena": "жадности", "dosena": "злобе"}
LMD_PAIRS = [("lobho", "mohena"), ("moho", "lobhena"), ("doso", "mohena"), ("moho", "dosena")]
GEND = {"жадность": "а", "заблуждение": "о", "злоба": "а"}
THREE_GOOD = f"{ALOBHA}, {ADOSA} и {AMOHA_N} по отношению друг к другу"
seg("1-1083", qa("hetū ceva sahetukā ca",
                 cap(rel_pairs([(NOM[a], DAT[b]) for a, b in LMD_PAIRS], lambda n: "является корнем и имеет корни"))
                 + f"; {THREE_GOOD} являются корнями и имеют корни", False))
seg("1-1084", qa("sahetukā ceva na ca hetū", f"{AMONG.format(REL + ' имеют корни')}: {AGG4_PE}", False))
seg("1-1085", qa("hetū ceva hetusampayuttā ca",
                 cap(rel_pairs([(NOM[a], DAT[b]) for a, b in LMD_PAIRS],
                               lambda n: f"является корнем и связан{GEND[n]} с корнями"))
                 + f"; {THREE_GOOD} являются корнями и связаны с корнями", False))
seg("1-1086", qa("hetusampayuttā ceva na ca hetū", f"{AMONG.format('связаны с этими явлениями')}: {AGG4_PE}", False))
seg("1-1087", qa("na hetū sahetukā", f"{THOSE.format(REL + ' не являются корнями, но имеют корни')} {AGG4_PE}",
                 False))
seg("1-1088", qa("na hetū ahetukā",
                 f"{THOSE.format(REL + ' не являются корнями и не имеют корней')} {AGG4_PE}, {SABBA}", False))

# ---------------------------------------------------------------- the short intermediate pairs
seg("1-1089", qa("sappaccayā", f"Пять совокупностей – {RUPAKKH}, {AGG4}", False))
seg("1-1090", qa("appaccayā", cap(ASANKH), False))
seg("1-1091", f"{Q('saṅkhatā')} Те самые явления, которые имеют условия, и есть {N['saṅkhatā']}.")
seg("1-1092", f"{Q('asaṅkhatā')} То самое явление, которое не имеет условий, и есть необусловленное явление.")
seg("1-1093", qa("sanidassanā", RUPAYATANA, False))
seg("1-1094", qa("anidassanā", f"{SENSE_PE}, {AGG4_PE}, {YANCA_ANID}, и {ASANKH}", False))
seg("1-1095", qa("sappaṭighā", SENSE_PE, False))
seg("1-1096", qa("appaṭighā", f"{cap(AGG4_PE)}, {YANCA_ANID}, и {ASANKH}", False))
FOUR_GREAT = T.EKAKA_Q_R.split("? ", 1)[1].split(", – ", 1)[0]  # Четыре великих элемента и … элементов
assert FOUR_GREAT == "Четыре великих элемента и материальная форма, производная от четырёх великих элементов"
seg("1-1097", qa("rūpino", FOUR_GREAT, True))
seg("1-1098", qa("arūpino", f"{cap(AGG4_PE)} и {ASANKH}", False))
seg("1-1099", qa("lokiyā", f"{cap(SAS)} {KAA}, {SPH3}: {AGG5_PE}", False))
seg("1-1100", qa("lokuttarā", LOKUTTARA, False))
VN = {"cakkhu": "зрительным", "sota": "слуховым", "ghāna": "обонятельным", "jivhā": "вкусовым", "kāya": "осязательным"}
KEN_RE = re.compile(r"Ye te dhammā (\w+)viññeyyā, na te dhammā (\w+)viññeyyā; ye vā pana te dhammā (\w+)viññeyyā,? "
                    r"na te dhammā (\w+)viññeyyā\.")


def kenaci_ru(pali):
    body = pali.split("? ", 1)[1]
    sents = KEN_RE.findall(body)
    out = []
    for x, y, y2, x2 in sents:
        assert (x, y) == (x2, y2), (x, y, x2, y2)
        out.append(f"Те явления, которые познаваемы {VN[x]} сознанием, не познаваемы {VN[y]} сознанием; а те "
                   f"явления, которые познаваемы {VN[y]} сознанием, не познаваемы {VN[x]} сознанием.")
    assert len(sents) == 20, len(sents)
    return f"{Q('kenaci viññeyyā, kenaci na viññeyyā')} {' '.join(out)} Это {N['kenaci viññeyyā, kenaci na viññeyyā']}."


note("Ye te dhammā cakkhuviññeyyā, na te dhammā sotaviññeyyā; ye vā pana te dhammā sotaviññeyyā, na te dhammā "
     "cakkhuviññeyyā.", "Те явления, которые познаваемы зрительным сознанием, не познаваемы слуховым сознанием; а те "
     "явления, которые познаваемы слуховым сознанием, не познаваемы зрительным сознанием.")

# ---------------------------------------------------------------- the taint group
AS4 = ", ".join(ASAVA[k][0] for k in ("kāmāsavo", "bhavāsavo", "diṭṭhāsavo", "avijjāsavo"))
seg("1-1102", f"{Q('āsavā')} Четыре влечения – {AS4}.")
seg("1-1103", f"{TATTHA.format(ASAVA['kāmāsavo'][0])} {KAMA_BODY}, – {CALLED.format(ASAVA['kāmāsavo'][1])}")
seg("1-1104", f"{TATTHA.format(ASAVA['bhavāsavo'][0])} {BHAVA_BODY.format(bhava(True))}, – "
              f"{CALLED.format(ASAVA['bhavāsavo'][1])}")
seg("1-1105", f"{TATTHA.format(ASAVA['diṭṭhāsavo'][0])} {TEN_VIEWS}; то, что есть такое {DIITHI_PAT}, – "
              f"{CALLED.format(ASAVA['diṭṭhāsavo'][1])} {cap(ALL_WRONG.format(ASAVA['diṭṭhāsavo'][1]))}.")
seg("1-1106", f"{TATTHA.format(ASAVA['avijjāsavo'][0])} {MOHA}, – {CALLED.format(ASAVA['avijjāsavo'][1])}",
    EXACT["Ime dhammā āsavā."])
seg("1-1107", qa("no āsavā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1108", qa("sāsavā", f"{cap(KAA)}, {SPH3}: {AGG5_PE}", False))
seg("1-1109", qa("anāsavā", LOKUTTARA, False))
seg("1-1110", qa("āsavasampayuttā", f"{THOSE.format('связаны с этими явлениями')} {AGG4_PE}", False))
seg("1-1111", qa("āsavavippayuttā", f"{THOSE.format('не связаны с этими явлениями')} {AGG4_PE}; {SABBA}", False))
seg("1-1112", f"{Q('āsavā ceva sāsavā ca')} Те самые влечения и есть {N['āsavā ceva sāsavā ca']}.")
AMONG_REST = "{}, остальные " + SAS + " " + KAA + ", " + SPH3 + ": " + AGG5_PE
seg("1-1113", qa("sāsavā ceva no ca āsavā", AMONG_REST.format(AMONG.format(REL + " подвержены влечениям")), False))
AS_PAIRS = [("kāmāsavo", "avijjāsavo"), ("avijjāsavo", "kāmāsavo"), ("bhavāsavo", "avijjāsavo"),
            ("avijjāsavo", "bhavāsavo"), ("diṭṭhāsavo", "avijjāsavo"), ("avijjāsavo", "diṭṭhāsavo")]
seg("1-1114", qa("āsavā ceva āsavasampayuttā ca",
                 cap(rel_pairs([(ASAVA[a][0], ASAVA[b][3]) for a, b in AS_PAIRS],
                               lambda n: "является влечением и связано с влечениями")), False))
seg("1-1115", qa("āsavasampayuttā ceva no ca āsavā", f"{AMONG.format('связаны с этими явлениями')}: {AGG4_PE}",
                 False))
DISS_SAS = (f"Те явления, которые не связаны с этими явлениями и являются подверженными влечениям благими, "
            f"неблагими и этически неопределёнными явлениями, относящимися к миру чувственных желаний, к миру форм "
            f"или к миру без форм: {AGG5_PE}")
note("Tehi dhammehi ye dhammā vippayuttā sāsavā kusalākusalābyākatā dhammā kāmāvacarā, rūpāvacarā, arūpāvacarā; "
     "rūpakkhandho…pe… viññāṇakkhandho", DISS_SAS)
seg("1-1116", qa("āsavavippayuttā sāsavā", DISS_SAS, False))
seg("1-1117", qa("āsavavippayuttā anāsavā", LOKUTTARA, False), EXACT["Nikkhepakaṇḍe paṭhamabhāṇavāro."])

# ---------------------------------------------------------------- the fetter group
SAMY10 = ["kāmarāga", "paṭigha", "māna", "diṭṭhi", "vicikicchā", "sīlabbataparāmāsa", "bhavarāga", "issā",
          "macchariya", "avijjā"]
seg("1-1118", f"{Q('saṃyojanā')} Десять оков – {', '.join(SAMY[k][0] for k in SAMY10)}.")
seg("1-1119", f"{TATTHA.format(SAMY['kāmarāga'][0])} {KAMA_BODY}, – {CALLED.format(SAMY['kāmarāga'][1])}")
seg("1-1120", f"{TATTHA.format(SAMY['paṭigha'][0])} {DOSA}, – {CALLED.format(SAMY['paṭigha'][1])}")
seg("1-1121", f"{TATTHA.format(SAMY['māna'][0])} {MANA}, – {CALLED.format(SAMY['māna'][1])}")
seg("1-1122", f"{TATTHA.format(SAMY['diṭṭhi'][0])} {TEN_VIEWS}; то, что есть такое {DIITHI_PAT}, – "
              f"{CALLED.format(SAMY['diṭṭhi'][1])} Кроме {SAMY['sīlabbataparāmāsa'][2]}, "
              f"{ALL_WRONG.format(SAMY['diṭṭhi'][1])}.")
seg("1-1123", f"{TATTHA.format(SAMY['vicikicchā'][0])} {DOUBT}; {low(VICIK)}, – {CALLED.format(SAMY['vicikicchā'][1])}")
seg("1-1124", f"{TATTHA.format(SAMY['sīlabbataparāmāsa'][0])} {SILABBATA_HEAD}{DIITHI_TAT}, – "
              f"{CALLED.format(SAMY['sīlabbataparāmāsa'][1])}")
seg("1-1125", f"{TATTHA.format(SAMY['bhavarāga'][0])} {BHAVA_BODY.format(bhava(False))}, – "
              f"{CALLED.format(SAMY['bhavarāga'][1])}")
seg("1-1126", f"{TATTHA.format(SAMY['issā'][0])} {ISSA}, – {CALLED.format(SAMY['issā'][1])}")
seg("1-1127", f"{TATTHA.format(SAMY['macchariya'][0])} {MACCH}, – {CALLED.format(SAMY['macchariya'][1])}")
seg("1-1128", f"{TATTHA.format(SAMY['avijjā'][0])} {MOHA}, – {CALLED.format(SAMY['avijjā'][1])}",
    EXACT["Ime dhammā saṃyojanā."])
seg("1-1129", qa("no saṃyojanā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1130", qa("saṃyojaniyā", f"{cap(SAS)} {KAA}, {SPH3}: {AGG5_PE}", False))
seg("1-1131", qa("asaṃyojaniyā", LOKUTTARA, False))
seg("1-1132", qa("saṃyojanasampayuttā", f"{THOSE.format('связаны с этими явлениями')} {AGG4_PE}", False))
seg("1-1133", qa("saṃyojanavippayuttā", f"{THOSE.format('не связаны с этими явлениями')} {AGG4_PE}; {SABBA}", False))
seg("1-1134", f"{Q('saṃyojanā ceva saṃyojaniyā ca')} Те самые оковы и есть {N['saṃyojanā ceva saṃyojaniyā ca']}.")
seg("1-1135", qa("saṃyojaniyā ceva no ca saṃyojanā",
                 AMONG_REST.format(AMONG.format(REL + " подвержены оковам")), False))
SAMY_PAIRS = []
for _k in SAMY10[:-1]:
    SAMY_PAIRS += [(_k, "avijjā"), ("avijjā", _k)]
seg("1-1136", qa("saṃyojanā ceva saṃyojanasampayuttā ca",
                 cap(rel_pairs([(SAMY[a][0], SAMY[b][3]) for a, b in SAMY_PAIRS],
                               lambda n: "являются оковами и связаны с оковами")), False))
seg("1-1137", qa("saṃyojanasampayuttā ceva no ca saṃyojanā", f"{AMONG.format('связаны с этими явлениями')}: {AGG4_PE}",
                 False))
seg("1-1138", qa("saṃyojanavippayuttā saṃyojaniyā", DISS_SAS, False))
seg("1-1139", qa("saṃyojanavippayuttā asaṃyojaniyā", LOKUTTARA, False))

# ---------------------------------------------------------------- the tie group
GAN4 = ["abhijjhā", "byāpādo", "sīlabbataparāmāso", "idaṃsaccābhiniveso"]
seg("1-1140", f"{Q('ganthā')} Четыре узы – {', '.join(GAN[k][0] for k in GAN4)}.")
seg("1-1141", f"{TATTHA.format(GAN['abhijjhā'][0])} То, что есть {lobha(False)}, – {CALLED.format(GAN['abhijjhā'][1])}")
seg("1-1142", f"{TATTHA.format(GAN['byāpādo'][0])} {DOSA}, – {CALLED.format(GAN['byāpādo'][1])}")
seg("1-1143", f"{TATTHA.format(GAN['sīlabbataparāmāso'][0])} {SILABBATA_HEAD}{DIITHI_TAT}, – "
              f"{CALLED.format(GAN['sīlabbataparāmāso'][1])}")
seg("1-1144", f"{TATTHA.format(GAN['idaṃsaccābhiniveso'][0])} {TEN_VIEWS_TRUE}; то, что есть такое {DIITHI_TAT}, – "
              f"{CALLED.format(GAN['idaṃsaccābhiniveso'][1])} Кроме {GAN['sīlabbataparāmāso'][2]}, "
              f"{ALL_WRONG.format(GAN['idaṃsaccābhiniveso'][1])}.", EXACT["Ime dhammā ganthā."])
seg("1-1145", qa("no ganthā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1146", qa("ganthaniyā", f"{cap(SAS)} {KAA}, {SPH3}: {AGG5_PE}", False))
seg("1-1147", qa("aganthaniyā", LOKUTTARA, False))
seg("1-1148", qa("ganthasampayuttā", f"{THOSE.format('связаны с этими явлениями')} {AGG4_PE}", False))
seg("1-1149", qa("ganthavippayuttā", f"{THOSE.format('не связаны с этими явлениями')} {AGG4_PE}, {SABBA}", False))
seg("1-1150", f"{Q('ganthā ceva ganthaniyā ca')} Те самые узы и есть {N['ganthā ceva ganthaniyā ca']}.")
seg("1-1151", qa("ganthaniyā ceva no ca ganthā", AMONG_REST.format(AMONG.format(REL + " подвержены узам")), False))
GAN_PAIRS = [("sīlabbataparāmāso", "abhijjhā"), ("abhijjhā", "sīlabbataparāmāso"),
             ("idaṃsaccābhiniveso", "abhijjhā"), ("abhijjhā", "idaṃsaccābhiniveso")]
seg("1-1152", qa("ganthā ceva ganthasampayuttā ca",
                 cap(rel_pairs([(GAN[a][0], GAN[b][3]) for a, b in GAN_PAIRS],
                               lambda n: "являются узами и связаны с узами")), False))
seg("1-1153", qa("ganthasampayuttā ceva no ca ganthā", f"{AMONG.format('связаны с этими явлениями')}: {AGG4_PE}",
                 False))
seg("1-1154", qa("ganthavippayuttā ganthaniyā", DISS_SAS, False))
seg("1-1155", qa("ganthavippayuttā aganthaniyā", LOKUTTARA, False))


# =========================================================================================
# 7. Line dispatch, checks, build
# =========================================================================================
Q_RE = re.compile(r"^Katame dhammā (.+?)\? ")
A_RE = re.compile(r"ime dhammā ([^–?]+?)\.$")
LATIN = re.compile(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]")


def check_line(sid, p, r):
    assert p.count("–") + p.count("—") == r.count("–") and "—" not in r, ("dash", sid, p.count("–"), r.count("–"))
    assert p.count(PE) == r.count(ELL), ("pe", sid, p.count(PE), r.count(ELL))
    assert p.count("?") == r.count("?"), ("question", sid, p.count("?"), r.count("?"))
    assert p.endswith("?") == r.endswith("?"), ("end", sid)
    assert "  " not in r and " ," not in r and ",," not in r and " ." not in r and ";;" not in r, ("spacing", sid, r)
    assert ":-" not in r and not re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", r), ("li", sid)
    stripped = re.sub(r"\[[^\]]*\]", "", r)
    assert not LATIN.search(stripped), ("latin", sid, LATIN.search(stripped).group(0))
    m = Q_RE.match(p)
    if m:
        assert r.startswith(Q(m.group(1)) + " "), ("q-frame", sid, m.group(1))
    m = A_RE.search(p)
    if m and m.group(1) in N and not p.startswith("Ime dhammā kenaci"):
        assert r.endswith(A(m.group(1))), ("a-frame", sid, m.group(1), r[-80:])


def translate(sid, plines):
    if sid in R:
        return R[sid]
    assert len(plines) == 1, sid
    p = plines[0]
    if p in EXACT:
        return [EXACT[p]]
    if sid == "1-1101":
        return [kenaci_ru(p)]
    raise KeyError(f"no translation for ^{sid}: {p[:80]}")


def build():
    segs = S.segments(PALI)
    ru = {}
    for sid, plines in segs:
        plines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x) for x in plines]
        rlines = translate(sid, plines)
        assert len(rlines) == len(plines), (sid, len(plines), len(rlines))
        for p, r in zip(plines, rlines):
            check_line(sid, p, r)
        ru[sid] = rlines
    unused = set(R) - {s for s, _ in segs}
    assert not unused, unused
    return ru, len(segs)


def notes():
    L = ["# pi-1 Russian rails: new formulas of 4-01", "",
         "Generated by build_rails_4-01_ru.py from its fixed strings; import that file instead of retyping. "
         "Strings already in ru-rails-formulas.md or the notes of chapters 2 and 3 are not repeated. "
         "Matrix names in the question and answer frames come verbatim from build_rails_sample_ru.py "
         "(«Что такое X?» / «– это X.»).", "",
         "Punctuation before the Pāli dash: «X – это …» after a plain noun or list; «…, – это …» only where the dash "
         "closes a participial phrase or a subordinate clause (coordinator 2026-11-14).", "",
         "The devanāgarī visarga «ः» that stands for a punctuation mark in ^1-1106, 1123, 1128, 1143, 1144 = «;».", "",
         "## Formulas (Pāli = Russian)", ""]
    for p, r in NOTES:
        L.append(f"{p} = {r}")
    L += ["", "## Decisions and termbase misfits (reported)", "",
          "^1-987 = 3-01 ^1-583 (same Pāli, punctuation aside), reused word for word; only the comma before the "
          "dash is dropped (it follows the plain noun «необусловленный элемент»).",
          "Sukhabhūmiyaṃ (^1-988 and ^1-1004, identical Pāli) = «На уровне счастья» in both, although ^1-988 is "
          "about pleasant feeling.",
          "samuppannā = «возникший» in the termbase, the same as uppannā; after «возникшие» it is written "
          "«полностью возникшие» (asamuppannā «не возникшие полностью»), like abhinibbattā / samuṭṭhitā.",
          "bhūtā (^1-1041, 1046; abhūtā 1042, 1045) = «ставшие» / «не ставшие»: the termbase has only "
          "«элементы» (the great elements).",
          "atthaṃ carati / acari / carissati (^1-1066, 1120, 1142) = «приносит / принёс / принесёт пользу»: "
          "caratīti / acarīti «причинять» covers harm only.",
          "kusalānaṃ dhammānaṃ vipākato (^1-1068, 1077) = «в виде результатов благих явлений» (termbase vipākato "
          "«в виде результатов действий»).",
          "neva hoti na na hoti tathāgato paraṃ maraṇā = «Татхагата не существует и не не существует после "
          "смерти» (coordinator: «ни … ни» with a verb needs «не»; pi-5 had «ни существует, ни не существует»).",
          "Terms the termbase lacks: ajjhosānaṃ «поглощённость», nandīrāgo «страсть к наслаждению», "
          "āsisitattaṃ «состояние упования», jappitattaṃ «состояние тяги», loluppāyitattaṃ «состояние падкости», "
          "kāmataṇhā «чувственная жажда», manopadoso «сильная злоба ума», kujjhitattaṃ «состояние гнева», "
          "atthaṅgatā «угасшие», heṭṭhimāni «низшие», adassāvī «не видевший», Idha «Вот», saṅgha «Община», "
          "loko «мир», Māra «Мара», lābha «приобретения», maggaphalāni «плоды путей».",
          "Source slips kept as written: ^1-1124, 1143, 1144 «patiṭṭhāho» (закрепление, as 2-04) where ^1-1007, "
          "1009, 1105, 1122 have «paṭiggāho» (цепкость); ^1-1130, 1146 «Sāsavā» in the fetter and tie groups; "
          "^1-1022 «neva ācayagāmi na apacayagāmino» = the matrix item."]
    (HERE / "notes-4-01.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-4-01.md")


def main():
    ru, n = build()
    S.emit(PALI, ru, OUT)
    notes()


if __name__ == "__main__":
    main()
