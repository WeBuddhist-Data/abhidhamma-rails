"""Build the Russian plain zero-shot of pi-1 part 3-01 (Rūpakaṇḍa: Uddeso, Mātikā, Ekakaniddeso).

usage: python -I -X utf8 build_3-01_ru.py
Sentence-level translation with fixed predicate strings, so every repeat is byte-identical
(structure as ref/en_build_3-01.py and ref/hi_build_3-01_hi.py). Classifying predicates reuse the
matrix wording (build_matika_ru.PRED / BARE), changed only from the plural «явления» to the singular
feminine «материальная форма»; check_matrix() verifies that mechanically.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_ru as M  # noqa: E402

ROOT = HERE.parents[3]
PART = "3-01-rupakandam.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / PART
OUT = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters" / PART

DASH = "–"
RF = "материальная форма"
RF_C = "Материальная форма"

# ---- headings and closing lines (ru-zeroshot-terms.md §1, verbatim) ------------------------------
HEAD = {
    "Rūpakaṇḍaṃ": "Раздел о материальной форме",
    "Uddeso": "Перечень",
    "Mātikā": "Матрица",
    "Ekakaṃ": "Классификация по одному",
    "Dukaṃ": "Классификация по два",
    "Tikaṃ": "Классификация по три",
    "Catukkaṃ": "Классификация по четыре",
    "Pañcakaṃ": "Классификация по пять",
    "Chakkaṃ": "Классификация по шесть",
    "Sattakaṃ": "Классификация по семь",
    "Aṭṭhakaṃ": "Классификация по восемь",
    "Navakaṃ": "Классификация по девять",
    "Dasakaṃ": "Классификация по десять",
    "Ekādasakaṃ": "Классификация по одиннадцать",
    "Rūpavibhatti": "Классификация материальной формы",
    "Ekakaniddeso": "Разъяснение классификации по одному",
}
WAYS = {"ekavidhena": "по одному", "duvidhena": "по два", "tividhena": "по три", "catubbidhena": "по четыре",
        "pañcavidhena": "по пять", "chabbidhena": "по шесть", "sattavidhena": "по семь",
        "aṭṭhavidhena": "по восемь", "navavidhena": "по девять", "dasavidhena": "по десять",
        "ekādasavidhena": "по одиннадцать"}
CLOSE = {h + ".": HEAD[h] + "." for h in HEAD if h not in ("Rūpakaṇḍaṃ", "Uddeso", "Rūpavibhatti")}
for k, v in WAYS.items():
    CLOSE[f"Evaṃ {k} rūpasaṅgaho."] = f"Такова классификация материальной формы {v}."
    CLOSE[f"{k[0].upper() + k[1:]} rūpasaṅgaho {DASH}"] = f"Классификация материальной формы {v} {DASH}"

# ---- predicates: Pāli -> verbal predicate with «материальная форма» as subject -------------------
P = {}


def pair(pos_pali, neg_pali, pos_ru, neg_ru):
    P[pos_pali], P[neg_pali] = pos_ru, neg_ru


def is_pair(pos_pali, neg_pali, ins):
    """noun/adjective predicates: «является X» / «не является X» (X instrumental)."""
    pair(pos_pali, neg_pali, f"является {ins}", f"не является {ins}")


# matrix wording (^1-M2-67, 68, 1-M1-4, 1-M2-9, 10, 1, 60, 61, 62, 66), singular feminine
is_pair("upādā", "no upādā", "производной")
pair("upādiṇṇaṃ", "anupādiṇṇaṃ", "охвачена цеплянием", "не охвачена цеплянием")
pair("upādiṇṇupādāniyaṃ", "anupādiṇṇupādāniyaṃ", "охвачена цеплянием и служит его объектом",
     "не охвачена цеплянием, но служит его объектом")
pair("sanidassanaṃ", "anidassanaṃ", "является видимой", "является невидимой")
pair("sappaṭighaṃ", "appaṭighaṃ", "способна к соударению", "не способна к соударению")
is_pair("indriyaṃ", "na indriyaṃ", "способностью")
is_pair("mahābhūtaṃ", "na mahābhūtaṃ", "великим элементом")
is_pair("viññatti", "na viññatti", "внешним выражением")
pair("cittasamuṭṭhānaṃ", "na cittasamuṭṭhānaṃ", "порождена умом", "не порождена умом")
pair("cittasahabhu", "na cittasahabhu", "сосуществует с умом", "не сосуществует с умом")
pair("cittānuparivatti", "na cittānuparivatti", "следует за умом", "не следует за умом")
pair("ajjhattikaṃ", "bāhiraṃ", "относится к внутреннему", "относится к внешнему")
# not matrix items
pair("oḷārikaṃ", "sukhumaṃ", "является грубой", "является тонкой")
pair("dūre", "santike", "находится далеко", "находится близко")

SENSE = {"cakkhu": "глаза", "sota": "уха", "ghāna": "носа", "jivhā": "языка", "kāya": "тела"}
VINNANA = {"cakkhu": "зрительного сознания", "sota": "слухового сознания", "ghāna": "обонятельного сознания",
           "jivhā": "вкусового сознания", "kāya": "осязательного сознания"}
GEN = {"saññāya": "восприятия", "cetanāya": "намерения"}  # genitive fragments inside '…pe…' chains
for s, e in SENSE.items():
    GEN[f"{s}samphassassa"] = f"контакта {e}"
    GEN[f"{s}samphassajāya vedanāya"] = f"чувства, рождённого контактом {e}"
    GEN[f"{s}viññāṇassa"] = VINNANA[s]
    for what in ("samphassassa", "viññāṇassa"):
        g = GEN[s + what]
        is_pair(f"{s}{what} vatthu", f"{s}{what} na vatthu", f"основой {g}")
        is_pair(f"{s}{what} ārammaṇaṃ", f"{s}{what} nārammaṇaṃ", f"объектом {g}")

INS = {  # nominal predicates, instrumental
    "cakkhāyatanaṃ": "сферой глаза", "sotāyatanaṃ": "сферой уха", "ghānāyatanaṃ": "сферой носа",
    "jivhāyatanaṃ": "сферой языка", "kāyāyatanaṃ": "сферой тела",
    "rūpāyatanaṃ": "сферой видимых форм", "saddāyatanaṃ": "сферой звуков", "gandhāyatanaṃ": "сферой запахов",
    "rasāyatanaṃ": "сферой вкусов", "phoṭṭhabbāyatanaṃ": "сферой осязаемого",
    "cakkhudhātu": "элементом глаза", "sotadhātu": "элементом уха", "ghānadhātu": "элементом носа",
    "jivhādhātu": "элементом языка", "kāyadhātu": "элементом тела",
    "rūpadhātu": "элементом видимых форм", "saddadhātu": "элементом звуков", "gandhadhātu": "элементом запахов",
    "rasadhātu": "элементом вкусов", "phoṭṭhabbadhātu": "элементом осязаемого",
    "cakkhundriyaṃ": "способностью глаза", "sotindriyaṃ": "способностью уха", "ghānindriyaṃ": "способностью носа",
    "jivhindriyaṃ": "способностью языка", "kāyindriyaṃ": "способностью тела",
    "itthindriyaṃ": "способностью женственности", "purisindriyaṃ": "способностью мужественности",
    "jīvitindriyaṃ": "жизненной способностью",
    "kāyaviññatti": "телесным внешним выражением", "vacīviññatti": "речевым внешним выражением",
    "ākāsadhātu": "элементом пространства", "āpodhātu": "элементом воды",
    "kabaḷīkāro āhāro": "съедаемой пищей",
}
for k, v in INS.items():
    is_pair(k, "na " + k, v)
RUPASSA = {"lahutā": "лёгкостью", "mudutā": "мягкостью", "kammaññatā": "работоспособностью", "upacayo": "ростом",
           "santati": "непрерывностью", "jaratā": "старением", "aniccatā": "непостоянством"}
for k, v in RUPASSA.items():
    is_pair(f"rūpassa {k}", f"rūpassa na {k}", f"{v} материальной формы")

PE = "…pe…"
RE_BASE = re.compile(r"^(\S+) (na )?vatthu$|^(\S+) (n)?ārammaṇaṃ$")


def pred(a):
    """Predicate for a Pāli phrase; '…pe…' chains are written out from the fixed strings above."""
    if PE not in a:
        return P[a]
    parts = [x.strip() for x in a.split(PE)]
    last = parts[-1]
    m = RE_BASE.match(last)
    if m:  # '… X-assa (na) vatthu' / '… X-assa (n)ārammaṇaṃ': one head noun, genitive chain
        if m.group(1):
            key, neg, head = m.group(1), bool(m.group(2)), "основой"
        else:
            key, neg, head = m.group(3), bool(m.group(4)), "объектом"
        gens = [GEN[x] for x in parts[:-1]] + [GEN[key]]
        return ("не " if neg else "") + f"является {head} " + "… ".join(gens)
    negs = [x.startswith("na ") for x in parts]
    keys = [x[3:] if x.startswith("na ") else x for x in parts]
    if all(negs):  # 'na X…pe… na Y': «не является X… не является Y»
        return "… ".join(f"не является {INS[k]}" for k in keys)
    assert not any(negs), a
    return "является " + "… ".join(INS[k] for k in keys)


# ---- sentence frames ------------------------------------------------------------------------------
RE_ATTHI = re.compile(r"^Atthi rūpaṃ (.+?), atthi rūpaṃ (.+?)\.$")
RE_YAM2 = re.compile(r"^Yaṃ taṃ rūpaṃ (.+?), taṃ atthi (.+?),? atthi (.+?)\.$")
RE_YAM1 = re.compile(r"^Yaṃ taṃ rūpaṃ (.+?), taṃ (?!atthi )(.+?)\.$")


def s_atthi(a, b):
    """Atthi rūpaṃ A, atthi rūpaṃ B."""
    return f"Есть {RF}, которая {pred(a)}, и есть {RF}, которая {pred(b)}."


def s_yam1(a, p):
    """Yaṃ taṃ rūpaṃ A, taṃ P."""
    return f"Та {RF}, которая {pred(a)}, {pred(p)}."


def s_yam2(a, p, q):
    """Yaṃ taṃ rūpaṃ A, taṃ atthi P, atthi Q."""
    return f"Та {RF}, которая {pred(a)}, отчасти {pred(p)}, отчасти {pred(q)}."


# ---- Uddeso ^1-583 ----------------------------------------------------------------------------------
ABY = ("1-M1-1", "в")
UDDESO_P = ("Katame dhammā abyākatā? Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā "
            "apariyāpannā vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho, ye ca dhammā kiriyā "
            "neva kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ, asaṅkhatā ca dhātu – ime dhammā abyākatā.")
UDDESO_R = (f"{M.QUESTION(ABY)} Результаты благих и неблагих явлений, относящиеся к миру чувственных желаний, "
            "к миру форм, к миру без форм и не принадлежащие к кругам существования: совокупность чувств, "
            "совокупность восприятия, совокупность формирующих факторов, совокупность сознания; и те явления, "
            "которые являются функциональными, не являются ни благими, ни неблагими и не являются результатами "
            f"действий; и вся {RF}; и необусловленный элемент, {DASH} {M.ANSWER(ABY)}")

# ---- Ekaka ^1-584 and Ekakaniddeso ^1-594 -------------------------------------------------------------
# (Pāli item, Russian predicate, matrix key whose PRED it adapts or None)
EKAKA = [
    ("na hetu", "не является корнем", ("1-M2-1", "б")),
    ("ahetukaṃ", "не имеет корней", ("1-M2-2", "б")),
    ("hetuvippayuttaṃ", "не связана с корнями", ("1-M2-3", "б")),
    ("sappaccayaṃ", "имеет условия", ("1-M2-7", "а")),
    ("saṅkhataṃ", "является обусловленной", ("1-M2-8", "а")),
    ("rūpaṃ [rūpiyaṃ (sī.)]", "является материальной" + M.V("p", "Sī.", "rūpiyaṃ"), ("1-M2-11", "а")),
    ("lokiyaṃ", "является мирской", ("1-M2-12", "а")),
    ("sāsavaṃ", "подвержена влечениям", ("1-M2-15", "а")),
    ("saṃyojaniyaṃ", "подвержена оковам", ("1-M2-21", "а")),
    ("ganthaniyaṃ", "подвержена узам", ("1-M2-27", "а")),
    ("oghaniyaṃ", "подвержена потокам", ("1-M2-33", "а")),
    ("yoganiyaṃ", "подвержена ярмам", ("1-M2-39", "а")),
    ("nīvaraṇiyaṃ", "подвержена помехам", ("1-M2-45", "а")),
    ("parāmaṭṭhaṃ", "затронута искажениями", ("1-M2-51", "а")),
    ("upādāniyaṃ", "служит объектом цепляния", ("1-M2-70", "а")),
    ("saṃkilesikaṃ", "подвержена омрачению", ("1-M2-76", "а")),
    ("abyākataṃ", "является этически неопределённой", ("1-M1-1", "в")),
    ("anārammaṇaṃ", "не имеет объекта", ("1-M2-55", "б")),
    ("acetasikaṃ", "не сопутствует уму", ("1-M2-57", "б")),
    ("cittavippayuttaṃ", "не связана с умом", ("1-M2-58", "б")),
    ("nevavipākanavipākadhammadhammaṃ", "не является результатом действий и не способна приносить результаты",
     ("1-M1-3", "в")),
    ("asaṃkiliṭṭhasaṃkilesikaṃ", "не омрачена, но подвержена омрачению", ("1-M1-5", "б")),
    # 'na X' of a triad item: «не относится к <matrix item, dative>»
    ("na savitakkasavicāraṃ", "не относится к явлениям с направленной мыслью и удержанием мысли", None),
    ("na avitakkavicāramattaṃ", "не относится к явлениям без направленной мысли, только с удержанием мысли", None),
    ("avitakkaavicāraṃ", "не содержит ни направленной мысли, ни удержания мысли", ("1-M1-6", "в")),
    ("na pītisahagataṃ", "не сопровождается восторгом", ("1-M2-90", "б")),
    ("na sukhasahagataṃ", "не сопровождается счастьем", ("1-M2-91", "б")),
    ("na upekkhāsahagataṃ", "не сопровождается невозмутимостью", ("1-M2-92", "б")),
    ("neva dassanena na bhāvanāya pahātabbaṃ", "не устраняется ни видением истины, ни развитием ума",
     ("1-M1-8", "в")),
    # material form has no roots: «относится к явлениям, чьи корни …» (matrix bare item, dative)
    ("neva dassanena na bhāvanāya pahātabbahetukaṃ",
     "относится к явлениям, чьи корни не устраняются ни видением истины, ни развитием ума", None),
    ("neva ācayagāmi na apacayagāmi", "не ведёт ни к накоплению, ни к убыванию", ("1-M1-10", "в")),
    ("nevasekkhanāsekkhaṃ", "не относится ни к обучающимся, ни к завершившим обучение", ("1-M1-11", "в")),
    ("parittaṃ", "является ограниченной", ("1-M1-12", "а")),
    ("kāmāvacaraṃ", "относится к миру чувственных желаний", ("1-M2-93", "а")),
    ("na rūpāvacaraṃ", "не относится к миру форм", ("1-M2-94", "б")),
    ("na arūpāvacaraṃ", "не относится к миру без форм", ("1-M2-95", "б")),
    ("pariyāpannaṃ", "принадлежит к кругам существования", ("1-M2-96", "а")),
    ("no apariyāpannaṃ", "не относится к явлениям, не принадлежащим к кругам существования", None),
    ("aniyataṃ", "является непредопределённой", ("1-M1-15", "в")),
    ("aniyyānikaṃ", "не ведёт к освобождению", ("1-M2-97", "б")),
    ("uppannaṃ", "является возникшей", ("1-M1-17", "а")),
    ("chahi viññāṇehi viññeyyaṃ", "познаётся шестью видами сознания", None),
    ("aniccaṃ", "является непостоянной", None),
    ("jarābhibhūtaṃ", "подвластна старению", None),
]
# items given with the matrix bare name in the dative: (Russian, matrix key, dative of the bare name)
DATIVE = {
    "na savitakkasavicāraṃ": (("1-M1-6", "а"), "явлениям с направленной мыслью и удержанием мысли"),
    "na avitakkavicāramattaṃ": (("1-M1-6", "б"), "явлениям без направленной мысли, только с удержанием мысли"),
    "neva dassanena na bhāvanāya pahātabbahetukaṃ":
        (("1-M1-9", "в"), "явлениям, чьи корни не устраняются ни видением истины, ни развитием ума"),
    "no apariyāpannaṃ": (("1-M2-96", "б"), "явлениям, не принадлежащим к кругам существования"),
}

SING = {  # plural predicate word -> singular feminine (only the forms grammar forces)
    "являются": "является", "имеют": "имеет", "связаны": "связана", "подвержены": "подвержена",
    "затронуты": "затронута", "служат": "служит", "сопутствуют": "сопутствует", "способны": "способна",
    "омрачены": "омрачена", "сопровождаются": "сопровождается", "устраняются": "устраняется",
    "ведут": "ведёт", "относятся": "относится", "принадлежат": "принадлежит", "содержат": "содержит",
    "обусловленными": "обусловленной",
    "материальными": "материальной", "мирскими": "мирской", "неопределёнными": "неопределённой",
    "ограниченными": "ограниченной", "непредопределёнными": "непредопределённой", "возникшими": "возникшей",
    "видимыми": "видимой", "невидимыми": "невидимой", "производными": "производной",
    "охвачены": "охвачена", "порождены": "порождена", "сосуществуют": "сосуществует", "следуют": "следует",
    "невидимы": "невидима",
}


SING_PHRASE = {"являются корнями": "является корнем", "являются результатами": "является результатом"}


def sing(text):
    for a, b in SING_PHRASE.items():
        text = text.replace(a, b)
    out = []
    for w in text.split(" "):
        tail = "," if w.endswith(",") else ""
        w = w.rstrip(",")
        out.append(SING.get(w, w) + tail)
    return " ".join(out)


def check_matrix():
    for p, r, key in EKAKA:
        r0 = re.sub(r" \[.*?\]", "", r)
        if key:
            assert sing(M.PRED[key]) == r0, (p, M.PRED[key], r0)
    for p, (key, dat) in DATIVE.items():
        bare = M.BARE[key]
        exp = bare.replace("явления", "явлениям", 1).replace("принадлежащие", "принадлежащим")
        assert exp == dat, (p, bare, dat)
        r = dict((x, y) for x, y, _ in EKAKA)[p]
        assert r.endswith(dat), (p, r)
    for a, b in [("upādā", ("1-M2-67", "а")), ("no upādā", ("1-M2-67", "б")),
                 ("upādiṇṇaṃ", ("1-M2-68", "а")), ("anupādiṇṇaṃ", ("1-M2-68", "б")),
                 ("upādiṇṇupādāniyaṃ", ("1-M1-4", "а")), ("anupādiṇṇupādāniyaṃ", ("1-M1-4", "б")),
                 ("sanidassanaṃ", ("1-M2-9", "а")), ("anidassanaṃ", ("1-M2-9", "б")),
                 ("sappaṭighaṃ", ("1-M2-10", "а")), ("appaṭighaṃ", ("1-M2-10", "б")),
                 ("cittasamuṭṭhānaṃ", ("1-M2-60", "а")), ("cittasahabhu", ("1-M2-61", "а")),
                 ("cittānuparivatti", ("1-M2-62", "а")),
                 ("ajjhattikaṃ", ("1-M2-66", "а")), ("bāhiraṃ", ("1-M2-66", "б"))]:
        assert sing(M.PRED[b]) == P[a], (a, M.PRED[b], P[a])


check_matrix()

EKAKA_HEAD_P = ("Tattha katamaṃ sabbaṃ rūpaṃ? Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – "
                "idaṃ vuccati sabbaṃ rūpaṃ. ")
EKAKA_HEAD_R = (f"Что здесь является всей материальной формой? Четыре великих элемента и {RF}, производная "
                f"от четырёх великих элементов, {DASH} это называется всей материальной формой. ")
EKAKA_P = EKAKA_HEAD_P + "Sabbaṃ rūpaṃ " + ", ".join(p for p, _, _ in EKAKA) + "."
# items are separated by «;» because several of them contain commas of their own
EKAKA_R = EKAKA_HEAD_R + f"Вся {RF} " + "; ".join(r for _, r, _ in EKAKA) + "."

EMPH = "несомненно"  # the emphatic '-meva' of ^1-594


def meva(p):
    p = re.sub(r" \[.*?\]", "", p)
    return (p[:-1] if p.endswith("ṃ") else p) + "meva"


NIDDESA = []
for p, r, _ in EKAKA:
    if p == "uppannaṃ":
        continue
    if p == "chahi viññāṇehi viññeyyaṃ":  # one item in ^1-594: 'uppannaṃ chahi viññāṇehi viññeyyameva'
        NIDDESA.append(("uppannaṃ chahi viññāṇehi viññeyyameva",
                        f"{EMPH} познаётся, возникнув, шестью видами сознания"))
        continue
    NIDDESA.append((meva(p), f"{EMPH} " + re.sub(r" \[.*?\]", "", r)))
NIDDESA_P = "Sabbaṃ rūpaṃ " + ", ".join(p for p, _ in NIDDESA) + "."
NIDDESA_R = f"Вся {RF} " + "; ".join(r for _, r in NIDDESA) + "."

# ---- lists (^1-586 … ^1-593) --------------------------------------------------------------------------
VINN = ["Познаваемая глазом", "познаваемая ухом", "познаваемая носом", "познаваемая языком", "познаваемая телом"]
VINN5 = ", ".join(f"{v} {RF}" for v in VINN)
MANODHATU = f"познаваемая элементом ума {RF}, познаваемая элементом умственного сознания {RF}"
INDR8 = ("Способность глаза, способность уха, способность носа, способность языка, способность тела, "
         "способность женственности, способность мужественности, жизненная способность")
LISTS = {
    "Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ.": f"Увиденная, услышанная, ощущённая, познанная {RF}.",
    "Pathavīdhātu, āpodhātu, tejodhātu, vāyodhātu, yañca rūpaṃ upādā.":
        f"Элемент земли, элемент воды, элемент огня, элемент ветра и {RF}, которая {P['upādā']}.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "manoviññeyyaṃ rūpaṃ.":
        f"{VINN5}, познаваемая умом {RF}.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        f"{VINN5}, {MANODHATU}.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ, manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        f"{VINN5}, отчасти приятная при контакте, отчасти болезненная при контакте, {MANODHATU}.",
    # the Pāli lacks a comma after jivhindriyaṃ in ^1-591 and ^1-592
    "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, "
    "jīvitindriyaṃ, yañca rūpaṃ na indriyaṃ.":
        f"{INDR8} и {RF}, которая {P['na indriyaṃ']}.",
    "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, "
    "jīvitindriyaṃ, na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ.":
        f"{INDR8}, а {RF}, которая {P['na indriyaṃ']}, отчасти {P['sappaṭighaṃ']}, отчасти {P['appaṭighaṃ']}.",
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, "
    "gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, yañca rūpaṃ anidassanaappaṭighaṃ "
    "[anidassanaṃ appaṭighaṃ (sī. syā.)] dhammāyatanapariyāpannaṃ.":
        "Сфера глаза, сфера уха, сфера носа, сфера языка, сфера тела, сфера видимых форм, сфера звуков, "
        f"сфера запахов, сфера вкусов, сфера осязаемого и {RF}, которая невидима и не способна к соударению"
        f"{M.V('s', 'Sī., Syā.', 'anidassanaṃ appaṭighaṃ')} и входит в сферу объектов ума.",
}
# ^1-M1-22 (в) «невидимые и не способные к соударению», predicate form singular
assert sing(M.PRED[("1-M1-22", "в")]) == "невидима и не способна к соударению"

WHOLE = {UDDESO_P: UDDESO_R, EKAKA_P: EKAKA_R, NIDDESA_P: NIDDESA_R}
WHOLE.update(LISTS)
WHOLE.update(CLOSE)


def tr_sentence(s):
    m = RE_ATTHI.match(s)
    if m:
        return s_atthi(m[1], m[2])
    m = RE_YAM2.match(s)
    if m:
        return s_yam2(m[1], m[2], m[3])
    m = RE_YAM1.match(s)
    if m:
        return s_yam1(m[1], m[2])
    raise KeyError(f"no rule for sentence: {s!r}")


def split_sentences(line):
    return re.split(r"(?<=\.) (?=(?:Atthi rūpaṃ|Yaṃ taṃ rūpaṃ) )", line)


def tr_line(line):
    if line in WHOLE:
        return WHOLE[line]
    return " ".join(tr_sentence(s) for s in split_sentences(line))


def build():
    out = []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            out.append("")
            continue
        m = re.match(r"^(.*?)(\s*\^[0-9A-Za-z-]+)?$", line)
        body, bid = m.group(1), m.group(2) or ""
        if body.startswith("#"):
            hashes, title = body.split(" ", 1)
            out.append(f"{hashes} {HEAD[title]}{bid}")
        else:
            r = tr_line(body)
            assert r.count(DASH) == body.count(DASH), (body, r)
            out.append(r + bid)
    text = "\n".join(out).rstrip("\n") + "\n"
    assert "—" not in text and ":-" not in text
    return text


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8", newline="\n")
    print("wrote", OUT)
