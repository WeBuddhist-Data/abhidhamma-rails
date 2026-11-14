"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience), chapter 3-01
(the start of the chapter on material form: the statement ^1-583, the classifications of matter by one,
two … eleven ^1-584 … ^1-593, and the exposition of the set of one ^1-594).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/3-01-rupakandam.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/notes-3-01.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never
edited: build_rails_sample_ru.py (S: matrix names, question/answer frames, headings) and
build_rails_2-05_ru.py (E: the functional formula KIR_M). The matrix items keep the approved 1-matika
wording, inflected for «материальная форма» (feminine singular).
Every sentence is rebuilt in Pāli from the same tables and compared with the source line, so nothing is
guessed silently; unknown Pāli raises KeyError.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.

Later builders may import the tables (NOUN, ADJ, GEN, forms(), NUM, SANGAHA …); importing writes nothing.

usage: python -I -X utf8 build_rails_3-01_ru.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_2_05_ru", HERE / "build_rails_2-05_ru.py")
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)        # importing writes nothing

PART = "3-01-rupakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
cap = S.cap
PE, ELL = "…pe…", "…"

# =========================================================================================
# 1. Core words
# =========================================================================================
RUPA = "материальная форма"                       # rūpaṃ (matter)
RUPA_GEN = "материальной формы"                   # rūpassa
SANGAHA = "классификация материальной формы"     # rūpasaṅgaho
ABY_NAME = S.TRIADS["1-M1-1"][2][1]               # этически неопределённые явления
Q_ABY = S.q_form(ABY_NAME)                        # Katame dhammā abyākatā?
A_ABY = S.a_form(ABY_NAME)                        # ime dhammā abyākatā.
assert Q_ABY == E.Q_ABY

# the counted classifications: heading, «X-vidhena», Russian distributive numeral
NUM = [   # (heading, vidhena, «по N»)
    ("Ekakaṃ", "ekavidhena", "одному"), ("Dukaṃ", "duvidhena", "два"), ("Tikaṃ", "tividhena", "три"),
    ("Catukkaṃ", "catubbidhena", "четыре"), ("Pañcakaṃ", "pañcavidhena", "пять"),
    ("Chakkaṃ", "chabbidhena", "шесть"), ("Sattakaṃ", "sattavidhena", "семь"),
    ("Aṭṭhakaṃ", "aṭṭhavidhena", "восемь"), ("Navakaṃ", "navavidhena", "девять"),
    ("Dasakaṃ", "dasavidhena", "десять"), ("Ekādasakaṃ", "ekādasavidhena", "одиннадцать"),
]
CLASS_N = "Классификация по {}"                   # Ekakaṃ … Ekādasakaṃ (termbase: Dukaṃ, Dasakaṃ, Ekādasakaṃ)
OPEN_N = cap(SANGAHA) + " по {} –"                # X-vidhena rūpasaṅgaho –
CLOSE_N = "Такова " + SANGAHA + " по {}."         # Evaṃ X-vidhena rūpasaṅgaho.
H_UDDESO = "Перечень"                             # Uddeso
H_VIBHATTI = "Классификация материальной формы"   # Rūpavibhatti (vibhatti = классификация)
NIDDESO = "Разъяснение"                           # niddeso
H_EKAKANIDDESO = f"{NIDDESO} классификации по одному"

# =========================================================================================
# 2. Predicates of material form
#    attr: after «материальная форма» (with its own leading «, » or « »)
#    pred: finite predicate («является производной», «охвачена цеплянием»)
#    ins:  after «бывает» (atthi … atthi)
# =========================================================================================
ADJ = {
    "upādā": (" производная", "является производной", "производной"),
    "no upādā": (" непроизводная", "является непроизводной", "непроизводной"),
    "upādiṇṇaṃ": (", охваченная цеплянием", "охвачена цеплянием", "охваченной цеплянием"),
    "anupādiṇṇaṃ": (", не охваченная цеплянием", "не охвачена цеплянием", "не охваченной цеплянием"),
    "upādiṇṇupādāniyaṃ": (", охваченная цеплянием и служащая его объектом",
                          "охвачена цеплянием и служит его объектом",
                          "охваченной цеплянием и служащей его объектом"),
    "anupādiṇṇupādāniyaṃ": (", не охваченная цеплянием, но служащая его объектом",
                            "не охвачена цеплянием, но служит его объектом",
                            "не охваченной цеплянием, но служащей его объектом"),
    "sanidassanaṃ": (" видимая", "является видимой", "видимой"),
    "anidassanaṃ": (" невидимая", "является невидимой", "невидимой"),
    "sappaṭighaṃ": (", способная к соударению", "способна к соударению", "способной к соударению"),
    "appaṭighaṃ": (", не способная к соударению", "не способна к соударению", "не способной к соударению"),
    "cittasamuṭṭhānaṃ": (", порождённая умом", "порождена умом", "порождённой умом"),
    "na cittasamuṭṭhānaṃ": (", не порождённая умом", "не порождена умом", "не порождённой умом"),
    "cittasahabhu": (", сосуществующая с умом", "сосуществует с умом", "сосуществующей с умом"),
    "na cittasahabhu": (", не сосуществующая с умом", "не сосуществует с умом", "не сосуществующей с умом"),
    "cittānuparivatti": (", следующая за умом", "следует за умом", "следующей за умом"),
    "na cittānuparivatti": (", не следующая за умом", "не следует за умом", "не следующей за умом"),
    "ajjhattikaṃ": (", относящаяся к внутреннему", "относится к внутреннему", "относящейся к внутреннему"),
    "bāhiraṃ": (", относящаяся к внешнему", "относится к внешнему", "относящейся к внешнему"),
    "oḷārikaṃ": (" грубая", "является грубой", "грубой"),
    "sukhumaṃ": (" тонкая", "является тонкой", "тонкой"),
    "dūre": (" вдали", "находится вдали", "вдали"),
    "santike": (" вблизи", "находится вблизи", "вблизи"),
}
# the matrix wording behind the attributes (1-matika, plural «явления, …»), here in the feminine singular
_MATRIX = {"upādā": ("1-M2-67", 0), "no upādā": ("1-M2-67", 1), "upādiṇṇaṃ": ("1-M2-68", 0),
           "anupādiṇṇaṃ": ("1-M2-68", 1), "sappaṭighaṃ": ("1-M2-10", 0), "appaṭighaṃ": ("1-M2-10", 1),
           "cittasamuṭṭhānaṃ": ("1-M2-60", 0), "na cittasamuṭṭhānaṃ": ("1-M2-60", 1),
           "cittasahabhu": ("1-M2-61", 0), "na cittasahabhu": ("1-M2-61", 1),
           "cittānuparivatti": ("1-M2-62", 0), "na cittānuparivatti": ("1-M2-62", 1),
           "ajjhattikaṃ": ("1-M2-66", 0), "bāhiraṃ": ("1-M2-66", 1),
           "sanidassanaṃ": ("1-M2-9", 0), "anidassanaṃ": ("1-M2-9", 1)}
_FEM = [("ые явления", "ая"), ("явления, ", ""), ("ые ", "ая "), ("ие ", "ая "), ("ые", "ая"), ("щие", "щая")]
for _p, (_sid, _i) in _MATRIX.items():
    _m = S.PAIRS[_sid][_i][1]
    for _a, _b in _FEM:
        _m = _m.replace(_a, _b)
    assert ADJ[_p][0].lstrip(", ") == _m, (_p, _m)
assert S.TRIADS["1-M1-4"][0][1] == "явления, охваченные цеплянием и служащие его объектом"
assert S.TRIADS["1-M1-4"][1][1] == "явления, не охваченные цеплянием, но служащие его объектом"

NOUN = {   # pali: (nominative, instrumental)
    "indriyaṃ": ("способность", "способностью"),
    "mahābhūtaṃ": ("великий элемент", "великим элементом"),
    "viññatti": ("внешнее выражение", "внешним выражением"),
    "itthindriyaṃ": ("способность женственности", "способностью женственности"),
    "purisindriyaṃ": ("способность мужественности", "способностью мужественности"),
    "jīvitindriyaṃ": ("жизненная способность", "жизненной способностью"),
    "kāyaviññatti": ("телесное внешнее выражение", "телесным внешним выражением"),
    "vacīviññatti": ("речевое внешнее выражение", "речевым внешним выражением"),
    "ākāsadhātu": ("элемент пространства", "элементом пространства"),
    "āpodhātu": ("элемент воды", "элементом воды"),
    "Pathavīdhātu": ("элемент земли", "элементом земли"),
    "tejodhātu": ("элемент огня", "элементом огня"),
    "vāyodhātu": ("элемент ветра", "элементом ветра"),
    "kabaḷīkāro āhāro": ("съедаемая пища", "съедаемой пищей"),
}
ORGANS = [   # (stem, indriya compound, genitive)
    ("cakkhu", "cakkhundriyaṃ", "глаза"), ("sota", "sotindriyaṃ", "уха"), ("ghāna", "ghānindriyaṃ", "носа"),
    ("jivhā", "jivhindriyaṃ", "языка"), ("kāya", "kāyindriyaṃ", "тела")]
OBJECTS = [("rūpa", "видимых форм"), ("sadda", "звуков"), ("gandha", "запахов"), ("rasa", "вкусов"),
           ("phoṭṭhabba", "осязаемого")]
for _st, _ind, _g in ORGANS:
    NOUN[_st[:-1] + "āyatanaṃ"] = (f"сфера {_g}", f"сферой {_g}")
    NOUN[f"{_st}dhātu"] = (f"элемент {_g}", f"элементом {_g}")
    NOUN[_ind] = (f"способность {_g}", f"способностью {_g}")
for _st, _g in OBJECTS:
    NOUN[_st[:-1] + "āyatanaṃ"] = (f"сфера {_g}", f"сферой {_g}")
    NOUN[f"{_st}dhātu"] = (f"элемент {_g}", f"элементом {_g}")
for _p in ("cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ", "rūpāyatanaṃ",
           "phoṭṭhabbāyatanaṃ", "cakkhudhātu", "jivhādhātu", "phoṭṭhabbadhātu", "cakkhundriyaṃ", "jivhindriyaṃ"):
    assert _p in NOUN, _p
RUPASSA = {   # rūpassa X: (nominative, instrumental) of X; the Russian adds «материальной формы»
    "lahutā": ("лёгкость", "лёгкостью"), "mudutā": ("мягкость", "мягкостью"),
    "kammaññatā": ("работоспособность", "работоспособностью"), "upacayo": ("рост", "ростом"),
    "santati": ("непрерывность", "непрерывностью"), "jaratā": ("старение", "старением"),
    "aniccatā": ("непостоянство", "непостоянством"),
}
for _k, (_n, _i) in RUPASSA.items():
    NOUN[f"rūpassa {_k}"] = (f"{_n} {RUPA_GEN}", f"{_i} {RUPA_GEN}")

# genitives governed by vatthu / ārammaṇaṃ
GEN = {}
for _st, _ist, _g in ORGANS:
    GEN[f"{_st}samphassassa"] = f"контакта {_g}"
GEN.update({
    "cakkhusamphassajāya vedanāya": "рождённого контактом глаза чувства",
    "kāyasamphassajāya vedanāya": "рождённого контактом тела чувства",
    "saññāya": "восприятия", "cetanāya": "намерения",
    "cakkhuviññāṇassa": "зрительного сознания", "kāyaviññāṇassa": "осязательного сознания",
})
HEADS = {"vatthu": ("основа", "основой", False), "na vatthu": ("основа", "основой", True),
         "ārammaṇaṃ": ("объект", "объектом", False), "nārammaṇaṃ": ("объект", "объектом", True)}
HEAD_RE = re.compile(r"(.+?) (na vatthu|vatthu|nārammaṇaṃ|ārammaṇaṃ)")


def noun_forms(ins, neg):
    ne = "не " if neg else ""
    return {"attr": f", {ne}являющаяся {ins}", "pred": f"{ne}является {ins}", "ins": f"{ne}{ins}"}


def forms(term):
    """attr / pred / ins / subj of one Pāli predicate (no …pe… inside)"""
    if term in ADJ:
        a, p, i = ADJ[term]
        f = {"attr": a, "pred": p, "ins": i}
    else:
        neg = False
        if term.startswith("na "):
            neg, term = True, term[3:]
        elif term.startswith("rūpassa na "):
            neg, term = True, "rūpassa " + term[len("rūpassa na "):]
        f = noun_forms(NOUN[term][1], neg)
    f["subj"] = (f"{cap(RUPA)}{f['attr']}," if f["attr"].startswith(",")
                 else f"{cap(f['attr'].strip())} {RUPA}")
    return f


def chain(p, mode):
    """A predicate, possibly a «…pe…» chain: genitives before vatthu / ārammaṇaṃ, or a run of nouns."""
    m = HEAD_RE.fullmatch(p)
    if m:
        gens = [GEN[g.strip()] for g in m.group(1).split(PE)]
        _, ins, neg = HEADS[m.group(2)]
        return noun_forms(f"{ins} " + f"{ELL} ".join(gens), neg)[mode]
    parts = [x.strip() for x in p.split(PE)]
    first = forms(parts[0])[mode]
    return first + "".join(f"{ELL} " + forms(x)["ins"] for x in parts[1:])


ATTHI_RE = re.compile(r"Atthi rūpaṃ (.+?), atthi rūpaṃ (.+)")
YAM_ATTHI_RE = re.compile(r"Yaṃ taṃ rūpaṃ (.+?), taṃ atthi (.+?), atthi (.+)")
YAM_RE = re.compile(r"Yaṃ taṃ rūpaṃ (.+?), taṃ (.+)")


def sentence(s):
    m = ATTHI_RE.fullmatch(s)
    if m:
        return f"Есть {RUPA}{chain(m.group(1), 'attr')}, есть {RUPA}{chain(m.group(2), 'attr')}"
    m = YAM_ATTHI_RE.fullmatch(s)
    if m:
        return f"{forms(m.group(1))['subj']} бывает {chain(m.group(2), 'ins')}, бывает {chain(m.group(3), 'ins')}"
    m = YAM_RE.fullmatch(s)
    if m:
        return f"{forms(m.group(1))['subj']} {chain(m.group(2), 'pred')}"
    raise KeyError("sentence: " + s[:80])


SLIPS = {   # rendered as meant (reported)
    " " + PE: PE,                                                  # ^1-U1 «cetanāya …pe…»
    "sappaṭighaṃ atthi appaṭighaṃ": "sappaṭighaṃ, atthi appaṭighaṃ",   # ^1-586, missing comma
    "jivhindriyaṃ kāyindriyaṃ": "jivhindriyaṃ, kāyindriyaṃ",           # ^1-591, ^1-592, missing comma
}


def pattern_line(line):
    for a, b in SLIPS.items():
        line = line.replace(a, b)
    assert line.endswith(".")
    sents = re.split(r"(?<=\.) (?=Atthi |Yaṃ )", line)
    return " ".join(sentence(s[:-1]) + "." for s in sents)


# =========================================================================================
# 3. The statement ^1-583
# =========================================================================================
KIR_PL = "функциональные, ни благие, ни неблагие и не являющиеся результатом действий"
assert E.KIR_M == ("функциональный, ни благой, ни неблагой и не являющийся результатом действий")
AGGREGATES = "совокупность чувств, совокупность восприятия, совокупность формирующих факторов и совокупность сознания"
SPHERES = ("относящиеся к миру чувственных желаний, к миру форм, к миру без форм или не принадлежащие к кругам "
           "существования")
SABBA_RUPA = "вся " + RUPA
ASANKHATA_DHATU = "необусловленный элемент"
UDDESO_P = ("Katame dhammā abyākatā? Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā "
            "apariyāpannā vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho, ye ca dhammā kiriyā neva "
            "kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ, asaṅkhatā ca dhātu – ime dhammā abyākatā.")
UDDESO_R = (f"{Q_ABY} {cap(AGGREGATES)}, являющиеся результатом благих и неблагих явлений, {SPHERES}, "
            f"и те {KIR_PL.replace('функциональные', 'функциональные явления', 1)}, и {SABBA_RUPA}, "
            f"и {ASANKHATA_DHATU}, – {A_ABY}")

# =========================================================================================
# 4. The set of one (^1-584) and its exposition with «-meva» (^1-594)
# =========================================================================================
EKAKA = [   # (pali item, russian predicate of «вся материальная форма»)
    ("na hetu", "не является корнем"),
    ("ahetukaṃ", "не имеет корней"),
    ("hetuvippayuttaṃ", "не связана с корнями"),
    ("sappaccayaṃ", "имеет условия"),
    ("saṅkhataṃ", "является обусловленной"),
    ("rūpaṃ", "является материальной"),
    ("lokiyaṃ", "является мирской"),
    ("sāsavaṃ", "подвержена влечениям"),
    ("saṃyojaniyaṃ", "подвержена оковам"),
    ("ganthaniyaṃ", "подвержена узам"),
    ("oghaniyaṃ", "подвержена потокам"),
    ("yoganiyaṃ", "подвержена ярмам"),
    ("nīvaraṇiyaṃ", "подвержена помехам"),
    ("parāmaṭṭhaṃ", "затронута искажениями"),
    ("upādāniyaṃ", "служит объектом цепляния"),
    ("saṃkilesikaṃ", "подвержена омрачению"),
    ("abyākataṃ", "является этически неопределённой"),
    ("anārammaṇaṃ", "не имеет объекта"),
    ("acetasikaṃ", "не сопутствует уму"),
    ("cittavippayuttaṃ", "не связана с умом"),
    ("nevavipākanavipākadhammadhammaṃ", "не является результатом действий и не способна приносить результаты"),
    ("asaṃkiliṭṭhasaṃkilesikaṃ", "является неомрачённой, но подверженной омрачению"),
    ("na savitakkasavicāraṃ", "не является явлением с направленной мыслью и удержанием мысли"),
    ("na avitakkavicāramattaṃ", "не является явлением без направленной мысли, только с удержанием мысли"),
    ("avitakkaavicāraṃ", "является явлением без направленной мысли и без удержания мысли"),
    ("na pītisahagataṃ", "не сопровождается восторгом"),
    ("na sukhasahagataṃ", "не сопровождается счастьем"),
    ("na upekkhāsahagataṃ", "не сопровождается невозмутимостью"),
    ("neva dassanena na bhāvanāya pahātabbaṃ", "не устраняется ни видением истины, ни развитием ума"),
    ("neva dassanena na bhāvanāya pahātabbahetukaṃ",
     "относится к явлениям, чьи корни не устраняются ни видением истины, ни развитием ума"),
    ("neva ācayagāmi na apacayagāmi", "не ведёт ни к накоплению, ни к убыванию"),
    ("nevasekkhanāsekkhaṃ", "не относится ни к обучающимся, ни к завершившим обучение"),
    ("parittaṃ", "является ограниченной"),
    ("kāmāvacaraṃ", "относится к миру чувственных желаний"),
    ("na rūpāvacaraṃ", "не относится к миру форм"),
    ("na arūpāvacaraṃ", "не относится к миру без форм"),
    ("pariyāpannaṃ", "принадлежит к кругам существования"),
    ("no apariyāpannaṃ", "не относится к явлениям, не принадлежащим к кругам существования"),
    ("aniyataṃ", "является непредопределённой"),
    ("aniyyānikaṃ", "не ведёт к освобождению"),
    ("uppannaṃ", "является возникшей"),
    ("chahi viññāṇehi viññeyyaṃ", "познаётся шестью видами сознания"),
    ("aniccaṃ", "является непостоянной"),
    ("jarābhibhūtaṃ", "подвластна старению"),
]
RUPIYA = S.reading("Sī.", "rūpiyaṃ")                # rūpaṃ [rūpiyaṃ (sī.)]
EKAKA_VAR = {"rūpaṃ": ("rūpaṃ [rūpiyaṃ (sī.)]", "является материальной " + RUPIYA)}
CERT = "несомненно"                                # -meva
UPPANNA_MEVA = ("uppannaṃ chahi viññāṇehi viññeyyameva", f"будучи возникшей, {CERT} познаётся шестью видами сознания")
# the matrix names the predicates come from (1-matika wording, plural): spot checks
assert S.TRIADS["1-M1-3"][2][1] == "явления, не являющиеся результатом действий и не способные приносить результаты"
assert S.TRIADS["1-M1-8"][2][1] == "явления, не устраняемые ни видением истины, ни развитием ума"
assert S.TRIADS["1-M1-9"][2][1] == "явления, чьи корни не устраняются ни видением истины, ни развитием ума"
assert S.TRIADS["1-M1-10"][2][1] == "явления, не ведущие ни к накоплению, ни к убыванию"
assert S.TRIADS["1-M1-11"][2][1] == "явления, не относящиеся ни к обучающимся, ни к завершившим обучение"
assert S.TRIADS["1-M1-6"][1][1] == "явления без направленной мысли, только с удержанием мысли"
assert S.PAIRS["1-M2-96"][1][1] == "явления, не принадлежащие к кругам существования"

EKAKA_Q_P = ("Tattha katamaṃ sabbaṃ rūpaṃ? Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – "
             "idaṃ vuccati sabbaṃ rūpaṃ.")
EKAKA_Q_R = (f"Что такое здесь {SABBA_RUPA}? Четыре великих элемента и {RUPA}, производная от четырёх великих "
             f"элементов, – это называется всей материальной формой.")


def ekaka_line(meva):
    pali, ru = [], []
    for p, r in EKAKA:
        if meva:
            if p == "uppannaṃ":
                continue
            if p == "chahi viññāṇehi viññeyyaṃ":
                pali.append(UPPANNA_MEVA[0])
                ru.append(UPPANNA_MEVA[1])
                continue
            pali.append((p[:-1] if p.endswith("ṃ") else p) + "meva")
            ru.append(f"{CERT} {r}")
        else:
            p, r = EKAKA_VAR.get(p, (p, r))
            pali.append(p)
            ru.append(r)
    # several predicates contain commas of their own: «; » between the predicates keeps the list readable
    return "Sabbaṃ rūpaṃ " + ", ".join(pali) + ".", cap(SABBA_RUPA) + " " + "; ".join(ru) + "."


EKAKA_P, EKAKA_R = ekaka_line(False)
NIDDESA_P, NIDDESA_R = ekaka_line(True)

# =========================================================================================
# 5. Lists (^1-586 … ^1-593)
# =========================================================================================
YANCA = f"и та {RUPA}, которая "                   # yañca rūpaṃ …
VIÑÑEYYA = [("Cakkhu", "глазом"), ("sota", "ухом"), ("ghāna", "носом"), ("jivhā", "языком"), ("kāya", "телом")]
VIÑÑEYYA_MANO = {"mano": "умом", "manodhātu": "элементом ума", "manoviññāṇadhātu": "элементом умственного сознания"}


def vin(by):
    return f"{RUPA}, познаваемая {by}"


FIVE_P = ", ".join(f"{s}viññeyyaṃ rūpaṃ" for s, _ in VIÑÑEYYA)
FIVE_R = "; ".join(vin(b) for _, b in VIÑÑEYYA)
SUKHA_DUKKHA_P = "atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ"
SUKHA_DUKKHA_R = "которая бывает доставляющей удовольствие при контакте, бывает болезненной при контакте"
INDRIYAS = ["Cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ", "itthindriyaṃ",
            "purisindriyaṃ", "jīvitindriyaṃ"]
INDRIYAS_P = ", ".join(INDRIYAS)
INDRIYAS_R = ", ".join(NOUN[p[0].lower() + p[1:]][0] for p in INDRIYAS)
AYATANAS = ["Cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ", "rūpāyatanaṃ",
            "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ"]
AYATANAS_R = ", ".join(NOUN[p[0].lower() + p[1:]][0] for p in AYATANAS)
DHAMMAYATANA = "принадлежит к сфере объектов ума"   # dhammāyatanapariyāpannaṃ
ANID_APP = "является невидимой и не способной к соударению"   # anidassanaappaṭighaṃ (1-M1-22 (в))
DITTHA = f"{cap(RUPA)} увиденная, услышанная, ощущённая, познанная."   # Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ.

LISTS = {
    "Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ.": DITTHA,
    "Pathavīdhātu, āpodhātu, tejodhātu, vāyodhātu, yañca rūpaṃ upādā.":
        cap(", ".join(NOUN[p][0] for p in ("Pathavīdhātu", "āpodhātu", "tejodhātu", "vāyodhātu")))
        + f" {YANCA}{ADJ['upādā'][1]}.",
    FIVE_P + ", manoviññeyyaṃ rūpaṃ.": cap(FIVE_R) + f"; {vin(VIÑÑEYYA_MANO['mano'])}.",
    FIVE_P + ", manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        cap(FIVE_R) + f"; {vin(VIÑÑEYYA_MANO['manodhātu'])}; {vin(VIÑÑEYYA_MANO['manoviññāṇadhātu'])}.",
    FIVE_P + f", {SUKHA_DUKKHA_P}, manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        cap(FIVE_R) + f", {SUKHA_DUKKHA_R}; {vin(VIÑÑEYYA_MANO['manodhātu'])}; "
                      f"{vin(VIÑÑEYYA_MANO['manoviññāṇadhātu'])}.",
    INDRIYAS_P + ", yañca rūpaṃ na indriyaṃ.": cap(INDRIYAS_R) + f" {YANCA}{forms('na indriyaṃ')['pred']}.",
    INDRIYAS_P + ", na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ.":
        cap(INDRIYAS_R) + f" и {RUPA}{forms('na indriyaṃ')['attr']}, которая бывает {ADJ['sappaṭighaṃ'][2]}, "
                          f"бывает {ADJ['appaṭighaṃ'][2]}.",
    ", ".join(AYATANAS) + ", yañca rūpaṃ anidassanaappaṭighaṃ [anidassanaṃ appaṭighaṃ (sī. syā.)] "
                          "dhammāyatanapariyāpannaṃ.":
        cap(AYATANAS_R) + f" {YANCA}{ANID_APP} "
        + S.spell("Sī., Syā.", "anidassanaṃ appaṭighaṃ") + f" и {DHAMMAYATANA}.",
}

# =========================================================================================
# 6. Headings and fixed lines
# =========================================================================================
EXACT = {
    "### Rūpakaṇḍaṃ": "### " + S.CH_HEADINGS["Rūpakaṇḍaṃ"],
    "#### Uddeso": f"#### {H_UDDESO}",
    "#### Mātikā": f"#### {S.H_MATIKA}",
    "Mātikā.": f"{S.H_MATIKA}.",
    "#### Rūpavibhatti": f"#### {H_VIBHATTI}",
    "##### Ekakaniddeso": f"##### {H_EKAKANIDDESO}",
    "Ekakaniddeso.": f"{H_EKAKANIDDESO}.",
    UDDESO_P: UDDESO_R,
    EKAKA_Q_P + " " + EKAKA_P: EKAKA_Q_R + " " + EKAKA_R,
    NIDDESA_P: NIDDESA_R,
}
for _h, _v, _n in NUM:
    EXACT[f"##### {_h}"] = "##### " + CLASS_N.format(_n)
    EXACT[f"{_h}."] = CLASS_N.format(_n) + "."
    EXACT[f"{cap(_v)} rūpasaṅgaho –"] = OPEN_N.format(_n)
    EXACT[f"Evaṃ {_v} rūpasaṅgaho."] = CLOSE_N.format(_n)
for _k, _v in LISTS.items():
    EXACT[_k] = _v
EXACT_NORM = {}
for _k, _v in EXACT.items():
    _kk = _k
    for _a, _b in SLIPS.items():
        _kk = _kk.replace(_a, _b)
    EXACT_NORM[_kk] = _v


def translate_line(line):
    norm = line
    for a, b in SLIPS.items():
        norm = norm.replace(a, b)
    if norm in EXACT_NORM:
        return EXACT_NORM[norm]
    return pattern_line(line)


PALI_CHARS = set("āīūṃṅñṭḍṇḷ") | set("abcdefghijklmnopqrstuvwxyz")


def check_ru(r):
    bare = re.sub(r"\[[^\]]*\]", "", r).lower()
    assert not (PALI_CHARS & set(bare)), r[:160]
    assert "—" not in r and ":-" not in r, r[:80]
    assert not re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", r), r[:80]


def render(segs):
    blocks = []
    for sid, plines in segs:
        rlines = []
        for p in plines:
            r = translate_line(p)
            assert r == cap(r), r[:40]
            check_ru(r)
            assert len(p) - len(p.lstrip("#")) == len(r) - len(r.lstrip("#")), sid
            assert p.count("–") + p.count("—") == r.count("–"), ("dash", sid, p[:60], r[:60])
            assert p.count(PE) <= r.count(ELL), ("pe", sid)
            assert p.endswith("?") == r.endswith("?") and p.count("?") == r.count("?"), ("question", sid)
            assert "  " not in r and " ," not in r and ",," not in r and " … " not in r and "..." not in r, r
            rlines.append(r)
        rlines[-1] += f" ^{sid}"
        blocks.append("\n".join(rlines))
    return blocks


def segments(path):
    out, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = S.ID.search(line)
        if m:
            buf.append(line[:m.start()].rstrip())
            out.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return out


def build():
    segs = segments(PALI)
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    L = ["# pi-1 Russian rails: new formulas of 3-01", "",
         "Generated by build_rails_3-01_ru.py from its fixed strings; import that file instead of retyping. "
         "Strings already in ru-rails-formulas.md or the notes of chapter 2 are not repeated. Matrix items keep "
         "the 1-matika wording, inflected for «материальная форма» (feminine singular).", "",
         "## Frames", "",
         f"Atthi rūpaṃ X, atthi rūpaṃ Y. = Есть {RUPA}[ attr X], есть {RUPA}[ attr Y].",
         "Yaṃ taṃ rūpaṃ A, taṃ X. = [subject A] [predicate X].",
         "Yaṃ taṃ rūpaṃ A, taṃ atthi X, atthi Y. = [subject A] бывает [X instr.], бывает [Y instr.].",
         "  subject: «Материальная форма, охваченная цеплянием,» / «Производная материальная форма»",
         "  nouns: attr «, являющаяся N-instr.», pred «является N-instr.», after «бывает» «N-instr.»; "
         "na N = «не являющаяся / не является / не N-instr.»",
         "X…pe… Y…pe… Z (a run of nouns) = first in full, the rest in the instrumental: "
         "«являющаяся сферой уха… сферой носа…», «не является сферой уха… не сферой носа…»",
         "G1…pe… G2 vatthu / ārammaṇaṃ = являющаяся основой / объектом G1… G2 (genitives); na vatthu / "
         "nārammaṇaṃ = не являющаяся основой / объектом …",
         f"X-vidhena rūpasaṅgaho – = {OPEN_N.format('N')}",
         f"Evaṃ X-vidhena rūpasaṅgaho. = {CLOSE_N.format('N')}",
         "Tattha katamaṃ sabbaṃ rūpaṃ? … – idaṃ vuccati sabbaṃ rūpaṃ. = " + EKAKA_Q_R,
         f"Sabbaṃ rūpaṃ X, Y, … = {cap(SABBA_RUPA)} [predicate X]; [predicate Y]; …",
         f"X-meva (Ekakaniddeso) = {CERT} [predicate X]",
         f"{UPPANNA_MEVA[0]} = {UPPANNA_MEVA[1]}",
         f"yañca rūpaṃ X = {YANCA}[predicate X]",
         "", "## The statement ^1-583", "", f"{UDDESO_P} = {UDDESO_R}",
         f"ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā = и те "
         f"{KIR_PL.replace('функциональные', 'функциональные явления', 1)}",
         f"Kusalākusalānaṃ dhammānaṃ vipākā … = являющиеся результатом благих и неблагих явлений",
         f"kāmāvacarā rūpāvacarā arūpāvacarā apariyāpannā (of the results) = {SPHERES}",
         f"sabbañca rūpaṃ = и {SABBA_RUPA}",
         f"asaṅkhatā ca dhātu = и {ASANKHATA_DHATU}",
         "", "## Predicates of material form (attr | pred | after «бывает»)", ""]
    for p, (a, pr, i) in ADJ.items():
        L.append(f"{p} = {a.lstrip(', ')} | {pr} | {i}")
    L += ["", "## Nouns (nominative | instrumental)", ""]
    for p, (n, i) in NOUN.items():
        L.append(f"{p} = {n} | {i}")
    L += ["", "## Genitives before vatthu / ārammaṇaṃ", ""]
    for p, r in GEN.items():
        L.append(f"{p} = {r}")
    L += ["vatthu = основа (not in the termbase)", "ārammaṇaṃ = объект", "",
          "## Predicates of «Sabbaṃ rūpaṃ» (^1-584; with -meva in ^1-594 «несомненно …»)", ""]
    for p, r in EKAKA:
        L.append(f"{EKAKA_VAR.get(p, (p, r))[0]} = {EKAKA_VAR.get(p, (p, r))[1]}")
    L += ["", "## Lists", ""]
    for p, r in LISTS.items():
        L.append(f"{p} = {r}")
    L += [f"{SUKHA_DUKKHA_P} = {SUKHA_DUKKHA_R}",
          f"dhammāyatanapariyāpannaṃ = {DHAMMAYATANA}", "",
          "## Headings and closing lines", ""]
    for p, r in EXACT.items():
        if p.startswith("#") or len(p) < 40:
            L.append(f"{p} = {r}")
    L += ["", "## Slips rendered as meant", "",
          "«cetanāya …pe…» (^1-U1, stray space) = as «cetanāya…pe…»",
          "«sappaṭighaṃ atthi appaṭighaṃ» (^1-586, missing comma) = comma",
          "«jivhindriyaṃ kāyindriyaṃ» (^1-591, ^1-592, missing comma) = comma"]
    (HERE / "notes-3-01.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-3-01.md")


def main():
    text, n = build()
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
    notes()


if __name__ == "__main__":
    main()
