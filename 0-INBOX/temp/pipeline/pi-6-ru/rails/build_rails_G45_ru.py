"""pi-6 Yamaka, G45 (4-dhatuyamaka, 5-01 / 5-02 / 5-03 saccayamaka): Russian RAILS builder.

Imports the frame-setters read-only (importing this file writes nothing):
    G2 = build_rails_G2_ru (paṇṇatti / pavatti / pariññā frames), G8 = build_rails_G8_ru (moment phrases),
    S = build_rails_sample_ru (labels, checks, book strings).
New here (later groups may import them): the element and truth nouns (register_terms), intro_ru() for the
long person / time / place intros of the Saccayamaka («у всех, кто перерождается, и в течение жизни в момент
возникновения ума, не связанного с жаждой,»), pj_question / pj_answer (parijānāti + pajahati), the paṇṇatti
answers with «остальное» (avaseso / avasesaṃ) and multi-word subjects, and the «…pe…» chain translator.

Run: python -I -X utf8 -B build_rails_G45_ru.py           (writes the four chapters + notes-rails-G45.md)
     python -I -X utf8 -B build_rails_G45_ru.py --probe   (prints lines without a formula; writes nothing)

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md
(kāyikaṃ / cetasikaṃ dukkhaṃ = «телесная / душевная боль», user decision).
Coordinator shared phrases (zeroshot-coordinator-rules.md): pavatte «в течение жизни»; uppāda- / bhaṅgakkhaṇe
«в момент возникновения / распада»; citte vattamāne «когда присутствует … ум»; yassa cittassa anantarā aggamaggaṃ
paṭilabhissanti «у тех, кто обретёт высший путь сразу после данного ума»; ye caññe maggaṃ paṭilabhissanti
«у других, кто обретёт путь»; āpāyika «существ низших миров»; groups «A, B и C»; «у них» only with no person.
"""
import importlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

G2 = importlib.import_module("build_rails_G2_ru")
G8 = importlib.import_module("build_rails_G8_ru")

CHAPTERS = ["4-dhatuyamaka.md", "5-01-saccayamaka.md", "5-02-saccayamaka.md", "5-03-saccayamaka.md"]
cap = S.cap
SLIPS = []
_CUR = {"id": None}


def slip(note):
    SLIPS.append((_CUR["id"], note))


def low1(s):
    return s[:1].lower() + s[1:]


def norm(s):
    """-ñca / -ñceva split off (dukkhasaccañca -> dukkhasaccaṃ ca), as G8.norm."""
    return re.sub(r"ñ(ceva|ca)\b", r"ṃ \1", s)


# =========================================================================== nouns (termbase)
T = G2.TERMS


def reg(key, nom, gen, ins, g, acc=None, forms=()):
    G2.register_term(key, nom, gen, ins, g, acc=acc, forms=forms)


def register_terms():
    # --- Saccayamaka (termbase: dukkhasaccaṃ «истина о страдании» …; dukkhaṃ «страдание» in the truths chapter)
    for key, sub in (("dukkhasaccaṃ", "о страдании"), ("samudayasaccaṃ", "о возникновении"),
                     ("nirodhasaccaṃ", "о прекращении"), ("maggasaccaṃ", "о пути")):
        reg(key, f"истина {sub}", f"истины {sub}", f"истиной {sub}", "f", acc=f"истину {sub}")
    reg("dukkhaṃ", "страдание", "страдания", "страданием", "n")
    reg("samudayo", "возникновение", "возникновения", "возникновением", "n", forms=["samudayaṃ"])
    reg("nirodho", "прекращение", "прекращения", "прекращением", "n", forms=["nirodhaṃ"])
    reg("maggo", "путь", "пути", "путём", "m", forms=["maggaṃ"])
    reg("saccaṃ", "истина", "истины", "истиной", "f", acc="истину")
    reg("saccā", "истины", "истин", "истинами", "pl", forms=["saccāni"])
    # --- Dhātuyamaka (termbase: cakkhudhātu «элемент глаза» …; dhātu «элемент», dhātū «элементы»)
    for key, sub in (("cakkhudhātu", "глаза"), ("sotadhātu", "уха"), ("ghānadhātu", "носа"),
                     ("jivhādhātu", "языка"), ("kāyadhātu", "тела"), ("rūpadhātu", "видимых форм"),
                     ("saddadhātu", "звуков"), ("gandhadhātu", "запахов"), ("rasadhātu", "вкусов"),
                     ("phoṭṭhabbadhātu", "осязаемого"), ("cakkhuviññāṇadhātu", "зрительного сознания"),
                     ("sotaviññāṇadhātu", "слухового сознания"), ("ghānaviññāṇadhātu", "обонятельного сознания"),
                     ("jivhāviññāṇadhātu", "вкусового сознания"), ("kāyaviññāṇadhātu", "осязательного сознания"),
                     ("manodhātu", "ума"), ("manoviññāṇadhātu", "умственного сознания"),
                     ("dhammadhātu", "объектов ума")):
        reg(key, f"элемент {sub}", f"элемента {sub}", f"элементом {sub}", "m",
            forms=[key + "ṃ", key[:-1] + "ūti"])
    reg("dhātu", "элемент", "элемента", "элементом", "m", forms=["dhātuṃ", "dhātūti"])   # dhātūti: the sg. quoted
    reg("dhātū", "элементы", "элементов", "элементами", "pl", forms=["dhātuyo"])
    reg("cakkhu", "глаз", "глаза", "глазом", "m", forms=["cakkhuṃ", "cakkhūti"])
    reg("sotaṃ", "ухо", "уха", "ухом", "n")
    reg("ghānaṃ", "нос", "носа", "носом", "m")
    reg("jivhā", "язык", "языка", "языком", "m", forms=["jivhaṃ", "jivha"])   # jivha: source spelling (termbase)
    reg("kāyo", "тело", "тела", "телом", "n", forms=["kāyaṃ"])
    reg("saddo", "звук", "звука", "звуком", "m", forms=["saddaṃ"])
    reg("gandho", "запах", "запаха", "запахом", "m", forms=["gandhaṃ"])
    reg("raso", "вкус", "вкуса", "вкусом", "m", forms=["rasaṃ"])
    reg("phoṭṭhabbo", "осязаемое", "осязаемого", "осязаемым", "n", forms=["phoṭṭhabbaṃ"])
    for key, adj in (("cakkhuviññāṇaṃ", "зрительн"), ("sotaviññāṇaṃ", "слухов"), ("ghānaviññāṇaṃ", "обонятельн"),
                     ("jivhāviññāṇaṃ", "вкусов"), ("kāyaviññāṇaṃ", "осязательн"), ("manoviññāṇaṃ", "умственн")):
        reg(key, f"{adj}ое сознание", f"{adj}ого сознания", f"{adj}ым сознанием", "n")
    reg("mano", "ум", "ума", "умом", "m", forms=["manaṃ"])
    reg("dhammo", "явление", "явления", "явлением", "n", forms=["dhammaṃ"])   # no pi-6 entry: dhamma «явление» (pi-1)


register_terms()
G2.VERB_SLIP["nirujjhiti"] = "nirujjhati"   # ^6-5-125 (termbase entry: rendered as meant)
JIVHA_SLIP = "jivha for jivhaṃ before ṭhapetvā: source spelling, rendered as meant (termbase entry)"


def term(tok, quoted=False):
    k = G2.term(tok, quoted=quoted)
    if k and tok.lower() == "jivha":
        slip(JIVHA_SLIP)
    return k


# multi-word subjects of the paṇṇatti answers: Pāli (lower) -> (nominative, genitive, number)
SUBJ = {
    "kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ": ("телесная боль, душевная боль", "телесной боли, душевной боли", "sg"),  # APPROVED
    "dibbacakkhu paññācakkhu": ("божественный глаз, глаз мудрости", None, "sg"),           # termbase
    "dibbasotaṃ taṇhāsotaṃ": ("божественное ухо, поток жажды", None, "sg"),                 # termbase
    "sīlagandho samādhigandho paññāgandho": ("запах нравственности, запах сосредоточения, запах мудрости", None, "sg"),
    "attharaso dhammaraso vimuttiraso": ("вкус смысла, вкус Учения, вкус освобождения", None, "sg"),
}
REST = {"avasesā": ("остальные", "pl"), "avaseso": ("остальное", "sg"), "avasesaṃ": ("остальное", "sg")}
COP = {"sg": "является", "pl": "являются"}
EXCEPT = G2.EXCEPT   # «Кроме»


def gen_list(p):
    """'cakkhuṃ ca cakkhudhātuṃ ca' -> «глаза и элемента глаза»; a SUBJ phrase -> its genitive."""
    k = p.lower().strip()
    if k in SUBJ and SUBJ[k][1]:
        return SUBJ[k][1]
    ks = [term(w) for w in k.split() if w != "ca"]
    if not ks or not all(ks):
        return None
    return " и ".join(T[x]["gen"] for x in ks)


def subj(p):
    """Paṇṇatti answer subject -> (Russian, number) or None."""
    k = p.lower().strip()
    if k in SUBJ:
        return cap(SUBJ[k][0]), SUBJ[k][2]
    m = re.match(r"^avasesā (\S+)$", k)
    if m and term(m.group(1)):
        return cap(f"остальные {T[term(m.group(1))]['nom']}"), "pl"
    m = re.match(r"^(.+?) ṭhapetvā (avasesā|avaseso|avasesaṃ)(?: (\S+))?$", k)
    if m:
        g = gen_list(m.group(1))
        if not g:
            return None
        rest, n = REST[m.group(2)]
        noun = ""
        if m.group(3):
            if not term(m.group(3)):
                return None
            noun = " " + T[term(m.group(3))]["nom"]
        return f"{EXCEPT} {g}, {rest}{noun}", n
    t = term(k)
    if t:
        return cap(T[t]["nom"]), G2.num(t)
    return None


def pn_answer(s):
    """Paṇṇatti answers (G2 frames, generalised to «остальное» and multi-word subjects)."""
    s = norm(s)
    # A B ceva C ca. = «A и является B, и является C.»
    m = re.match(r"^(?P<s>.+?) (?P<b>\S+) ceva (?P<c>\S+) ca\.$", s)
    if m and subj(m.group("s")) and term(m.group("b")) and term(m.group("c")):
        ru, n = subj(m.group("s"))
        return f"{ru} и {COP[n]} {T[term(m.group('b'))]['ins']}, и {COP[n]} {T[term(m.group('c'))]['ins']}."
    # X ca Y ca ṭhapetvā REST na ceva B na ca C. = «Кроме X и Y, остальн… не явл… ни B, ни C.»
    m = re.match(r"^(?P<x>.+?) ṭhapetvā (?P<r>avasesā|avaseso|avasesaṃ) na ceva (?P<b>\S+) na ca (?P<c>\S+)\.$", s)
    if m and gen_list(m.group("x")) and term(m.group("b")) and term(m.group("c")):
        rest, n = REST[m.group("r")]
        return (f"{EXCEPT} {gen_list(m.group('x'))}, {rest} не {COP[n]} ни {T[term(m.group('b'))]['ins']}, "
                f"ни {T[term(m.group('c'))]['ins']}.")
    # S B, na C. = «S является B, но не является C.»
    m = re.match(r"^(?P<s>.+?) (?P<b>\S+), na (?P<c>\S+)\.$", s)
    if m and subj(m.group("s")) and term(m.group("b")) and term(m.group("c")):
        ru, n = subj(m.group("s"))
        return f"{ru} {COP[n]} {T[term(m.group('b'))]['ins']}, но не {COP[n]} {T[term(m.group('c'))]['ins']}."
    # S na C, B. = «S не является C, но является B.»
    m = re.match(r"^(?P<s>.+?) na (?P<c>\S+), (?P<b>\S+)\.$", s)
    if m and subj(m.group("s")) and term(m.group("b")) and term(m.group("c")):
        ru, n = subj(m.group("s"))
        return f"{ru} не {COP[n]} {T[term(m.group('c'))]['ins']}, но {COP[n]} {T[term(m.group('b'))]['ins']}."
    # S na C. = «S не является C.»
    m = re.match(r"^(?P<s>.+?) na (?P<c>\S+)\.$", s)
    if m and subj(m.group("s")) and term(m.group("c")):
        ru, n = subj(m.group("s"))
        return f"{ru} не {COP[n]} {T[term(m.group('c'))]['ins']}."
    return None


def pn_question(s):
    """Labelled or unlabelled «(na) X (na) Y?» (G2.pn_question_line); also without the «?» (abbreviated)."""
    m = re.match(r"^(\((?:Ka|Kha)\) )?(.+?)([?.]?)$", s)
    lab, body, end = m.group(1), m.group(2), m.group(3)
    if lab:
        return G2.pn_question_line(s) if end else None
    r = G2.pn_question_line("(Ka) " + low1(body) + "?")
    if not r:
        return None
    r = r[len("(а) "):-1] + end
    return r


# =========================================================================== person / time / place intros
PL_ACC, PL_LOC, PL_ABL, BEINGS = dict(G2.PL_ACC), dict(G2.PL_LOC), dict(G2.PL_ABL), dict(G2.BEINGS)
PL_LOC["apāye"] = "в низших мирах"                          # termbase Apāye «низшие миры»
PL_ABL["asaññattā"] = PL_ABL["asaññasattā"]                 # source spelling (^6-5-76), termbase entry
AVASESE = "в остальном существовании с четырьмя составляющими и с пятью составляющими"  # Avasese catuvokāre pañcavokāre
# moments (G8 «в момент возникновения / распада» + termbase phrases); value: (Russian genitive, closes with a comma?)
MOM_GEN = {
    "cittassa": ("ума", False), "tassa cittassa": ("этого ума", False),
    "pacchimacittassa": ("последнего ума", False), "upapatticittassa": ("ума перерождения", False),
    "taṇhāvippayuttacittassa": ("ума, не связанного с жаждой", True),
    "maggavippayuttacittassa": ("ума, не связанного с путём", True),
    "taṇhāvippayuttamaggavippayuttacittassa": ("ума, не связанного с жаждой и не связанного с путём", True),
    "maggavippayuttataṇhāvippayuttacittassa": ("ума, не связанного с путём и не связанного с жаждой", True),
    "taṇhāya": ("жажды", False), "maggassa": ("пути", False), "aggamaggassa": ("высшего пути", False),
    "phalassa": ("плода", False), "aggaphalassa": ("высшего плода", False),
    "maggassa ca phalassa ca": ("пути и плода", False), "aggamaggassa ca phalassa ca": ("высшего пути и плода", False),
}
KHANA = {"uppādakkhaṇe": "в момент возникновения", "bhaṅgakkhaṇe": "в момент распада"}   # G8, pi-5
PAVATTE = "в течение жизни"                                   # pavatte (coordinator shared phrase)
VATT = {  # X citte vattamāne = «когда присутствует X ум» (coordinator; pi-5)
    "taṇhāvippayuttacitte": ("когда присутствует ум, не связанный с жаждой", True),
    "dutiye citte": ("когда присутствует второй ум", True),
    "dutiye akusale citte": ("когда присутствует второй неблагой ум", True),
}
LOC_T = {"arūpe": "в мире без форм", "pañcavokāre": "в существовании с пятью составляющими"}
ATTR = {  # sa- / a-X-kānaṃ upapajjantānaṃ (termbase: Sacakkhukānaṃ «с глазом», acakkhukānaṃ «без глаза» …)
    "sacakkhukānaṃ": "с глазом", "acakkhukānaṃ": "без глаза", "sasotakānaṃ": "с ухом", "asotakānaṃ": "без уха",
    "saghānakānaṃ": "с носом", "aghānakānaṃ": "без носа",           # no entry: built from ghāna «нос» (as sota)
    "sarūpakānaṃ": "с видимой формой",                             # no entry: as arūpakānaṃ «без видимой формы»
    "sacittakānaṃ": "с умом",
}
DIES, REBORN = G2.DIES, G2.REBORN
WILL_PATH = "кто обретёт путь"                                     # maggaṃ paṭilabhissanti (G2, termbase)
WILL_TOP = "кто обретёт высший путь сразу после данного ума"     # yassa cittassa anantarā aggamaggaṃ paṭilabhissanti
PUTHU = "обычных людей, которые не обретут путь"                  # (ye ca) puthujjanā maggaṃ na paṭilabhissanti (G2)
WHO_PART = {"upapajjantānaṃ": "перерождающихся", "cavantānaṃ": "умирающих"}   # «у тех умирающих, кто …» (G2)
THEY = "у них"


def _alt(d):
    return G2._alt(d)


def _mom(m):
    g, rel = MOM_GEN[m.group("g")]
    return f"{KHANA[m.group('k')]} {g}", rel


_MG = "(?P<g>" + "|".join(sorted(map(re.escape, MOM_GEN), key=len, reverse=True)) + ")"
_K = "(?P<k>uppādakkhaṇe|bhaṅgakkhaṇe)"


def _units():
    A, L, B, G, AT = _alt(PL_ACC), _alt(PL_LOC), _alt(PL_ABL), _alt(BEINGS), _alt(ATTR)
    P = "P"
    return [  # (regex, kind, fn(match) -> (Russian, closes with a comma?)); kind P person, T time (attaches to a
        #       person just before it), N time that opens its own group (pavatte …, a plane + moment)
        (rf"pavatte {_MG} {_K}", "N", lambda m: (f"{PAVATTE} {_mom(m)[0]}", _mom(m)[1])),
        (rf"(?P<l>{_alt(LOC_T)}) {_MG} {_K}", "N", lambda m: (f"{LOC_T[m.group('l')]} {_mom(m)[0]}", _mom(m)[1])),
        (rf"{_MG} {_K}", "T", _mom),
        (rf"(?P<v>{_alt(VATT)}) vattamāne", "T", lambda m: VATT[m.group("v")]),
        (r"sabbesaṃ cavantānaṃ", P, lambda m: (f"у всех, кто {DIES}", True)),
        (r"sabbesaṃ upapajjantānaṃ", P, lambda m: (f"у всех, кто {REBORN}", True)),
        (r"sabbesaṃ", P, lambda m: ("у всех", False)),
        (rf"itaresaṃ ((?:{A} )+)upapajjantānaṃ", P,
         lambda m: (f"у остальных, кто {REBORN} {G2._places(m.group(1).strip(), PL_ACC)}", True)),
        (rf"itaresaṃ ((?:{B} )+)cavantānaṃ", P,
         lambda m: (f"у остальных, кто {DIES} {G2._places(m.group(1).strip(), PL_ABL)}", True)),
        (r"itaresaṃ upapajjantānaṃ", P, lambda m: (f"у остальных, кто {REBORN}", True)),
        (r"itaresaṃ cavantānaṃ", P, lambda m: (f"у остальных, кто {DIES}", True)),
        (rf"itaresaṃ ((?:{G} ?)+)(?= |$)", P,
         lambda m: ("у остальных " + G2._places(m.group(1).strip(), BEINGS).replace(" и ", " и "), False)),
        (r"itaresaṃ", P, lambda m: ("у остальных", False)),
        (rf"((?:{A} )+)upapajjantānaṃ", P,
         lambda m: (f"у тех, кто {REBORN} {G2._places(m.group(1).strip(), PL_ACC)}", True)),
        (rf"((?:{B} )+)cavantānaṃ", P,
         lambda m: (f"у тех, кто {DIES} {G2._places(m.group(1).strip(), PL_ABL)}", True)),
        (rf"((?:{AT} )+)upapajjantānaṃ", P,
         lambda m: (f"у тех, кто {REBORN} " + " и ".join(ATTR[w] for w in m.group(1).split()), True)),
        (r"(?P<n>an)?abhisametāvīnaṃ(?: (?P<w>upapajjantānaṃ|cavantānaṃ))?", P,
         lambda m: ("у тех, кто " + ("не " if m.group("n") else "") + "постиг истины"
                    + (f" и {REBORN if m.group('w') == 'upapajjantānaṃ' else DIES}" if m.group("w") else ""), True)),
        (r"aggamaggasamaṅgīnaṃ", P, lambda m: ("у обладающих высшим путём", False)),       # termbase
        (r"arahantānaṃ", P, lambda m: ("у архатов", False)),                               # termbase
        (r"pacchimacittasamaṅgīnaṃ", P, lambda m: ("у обладающих последним умом", False)), # G8
        (r"āpāyikānaṃ", P, lambda m: ("у существ низших миров", False)),                   # coordinator
        (r"nirodhasamāpannānaṃ", P, lambda m: ("у вошедших в медитативное достижение прекращения", False)),  # G8
        (r"yassa cittassa anantarā aggamaggaṃ paṭilabhiss(?P<a>a|ā)nti", P, lambda m: (f"у тех, {WILL_TOP}", True)),
        (r"ye caññe maggaṃ paṭilabhissanti tesaṃ (?P<w>upapajjantānaṃ|cavantānaṃ)", P,
         lambda m: (f"у других {WHO_PART[m.group('w')]}, {WILL_PATH}", True)),
        (r"ye caññe maggaṃ paṭilabhissanti", P, lambda m: (f"у других, {WILL_PATH}", True)),
        (r"ye (?:ca )?puthujjanā maggaṃ na paṭilabhissanti tesaṃ (?P<w>upapajjantānaṃ|cavantānaṃ)", P,
         lambda m: (f"у тех {WHO_PART[m.group('w')]} {PUTHU}", True)),
        (r"ye (?:ca )?puthujjanā maggaṃ na paṭilabhissanti", P, lambda m: (f"у тех {PUTHU}", True)),
        (r"ye maggaṃ paṭilabhissanti", P, lambda m: (f"у тех, {WILL_PATH}", True)),
        (rf"({G})", P, lambda m: (f"у {BEINGS[m.group(1)]}", False)),
    ]


UNITS = None


def units(pali):
    """Pāli intro -> [(kind, Russian, closes with a comma?)] or None."""
    global UNITS
    if UNITS is None:
        UNITS = _units()
    s = re.sub(r"\s+", " ", pali.lower().replace(",", " ")).strip()
    out = []
    while s:
        if s.startswith("tesaṃ ") and out and out[-1][0] == "P":   # resumptive before a moment: not rendered
            s = s[len("tesaṃ "):]
            continue
        for rx, kind, fn in UNITS:
            m = re.match(rx + r"(?= |$)", s)
            if m:
                if "paṭilabhissānti" in m.group(0):
                    slip("paṭilabhissānti for paṭilabhissanti: spelling slip, rendered as meant (termbase entry)")
                if "asaññattā" in m.group(0):
                    slip("asaññattā for asaññasattā: spelling slip, rendered as meant (termbase entry)")
                ru, rel = fn(m)
                out.append((kind, ru, rel))
                s = s[m.end():].strip()
                break
        else:
            return None
    return out


def intro_ru(pali):
    """Groups: a moment (T) right after a person joins that person («у архатов в момент возникновения ума»;
    after a relative clause with a comma); pavatte … and a plane + moment open their own group. Groups are
    joined «A, B и C» (G2.join_groups); «у них» is added only when no person is named."""
    us = units(pali)
    if not us:
        return None
    gs = []
    for kind, ru, rel in us:
        if kind == "T" and gs and gs[-1][2] == "P" and not gs[-1][3]:
            g = gs[-1]
            g[0] += (", " if g[1] or ru.startswith("когда ") else " ") + ru   # «когда …» clause: comma
            g[1], g[3] = rel, True
        else:
            gs.append([ru, rel, "P" if kind == "P" else "T", False])
    s = G2.join_groups([(g[0], g[1]) for g in gs])
    if not any(g[2] == "P" for g in gs):
        s += " " + THEY
    return s


def clause(toks, intro, there, place=False):
    """The verb clause after the intro: G2 partial / pair."""
    p = G2.parse_partial(toks, place=place)
    if p:
        x, v1, y, v2, t2 = p
        return f"{intro}{there} {G2.partial(x, v1, y, v2, t2, who=None if place else THEY)}"
    p = G2.parse_pair(toks)
    if p:
        x, v1, y, v2, c1, c2 = p
        return f"{intro}{there} {G2.pair(x, v1, y, v2, c1, c2)}"
    return None


def person_answer(s):
    """INTRO tesaṃ (tattha) <partial | pair>."""
    body = norm(s[:-1])
    for m in re.finditer(r" tesaṃ(?P<t> tattha)? ", body):
        intro = intro_ru(body[:m.start()])
        if not intro:
            continue
        r = clause(body[m.end():].split(), intro, " там" if m.group("t") else "")
        if r:
            return r + "."
    return None


def place_ru(pali):
    k = pali.lower().strip()
    if k == "avasese catuvokāre pañcavokāre":
        return cap(AVASESE)
    if k and all(w in PL_LOC for w in k.split()):
        return cap(G2._places(k, PL_LOC))
    return None


def place_answer(s):
    """PLACE(S) tattha <partial | pair>: the resumptive «tattha» after the named place is not rendered (G2)."""
    body = norm(s[:-1])
    m = re.match(r"^(.+?) tattha (.+)$", body)
    if not m or not place_ru(m.group(1)):
        return None
    toks = m.group(2).split()
    p = G2.parse_partial(toks, place=True)
    if p:
        x, v1, y, v2, t2 = p
        return f"{place_ru(m.group(1))} {G2.partial(x, v1, y, v2, t2, who=None)}."
    p = G2.parse_pair(toks)
    if p:
        return f"{place_ru(m.group(1))} {G2.pair(*p)}."
    return None


def place_single(s):
    """Abbreviated «Asaññasatte tattha dukkhasaccaṃ nirujjhati» (before …pe…) = «Среди … прекращается …»."""
    m = re.match(r"^(.+?) tattha (.+)$", s)
    if not m or not place_ru(m.group(1)):
        return None
    a = G2.parse_sv(m.group(2))
    if not a:
        return None
    return f"{place_ru(m.group(1))} {G2.vru(*a[1], T[a[0]]['g'])} {T[a[0]]['nom']}"


# =========================================================================== pariññā (parijānāti, pajahati)
# termbase: parijānāti «полностью понимать», parijānittha / parijānissati «полностью понять» (G2: «полностью понял /
# поймёт», negative «не понимает полностью»); pajahati «устранять», pajahittha / pajahissati «устранить».
PJ = {  # base: (sg, pl, neg sg, neg pl, Pāli number)
    "parijānāti": ("полностью понимает", "полностью понимают", "не понимает полностью", "не понимают полностью", "sg"),
    "parijānanti": ("полностью понимает", "полностью понимают", "не понимает полностью", "не понимают полностью", "pl"),
    "parijānittha": ("полностью понял", "полностью поняли", "не понял полностью", "не поняли полностью", "sg"),
    "parijānissati": ("полностью поймёт", "полностью поймут", "не поймёт полностью", "не поймут полностью", "sg"),
    "pajahati": ("устраняет", "устраняют", "не устраняет", "не устраняют", "sg"),
    "pajahittha": ("устранил", "устранили", "не устранил", "не устранили", "sg"),
    "pajahissati": ("устранит", "устранят", "не устранит", "не устранят", "sg"),
    "pajahissanti": ("устранит", "устранят", "не устранит", "не устранят", "pl"),
}


def pjparse(s):
    s = s.strip()
    neg = False
    if s.startswith("na "):
        neg, s = True, s[3:]
    elif s.startswith("nappa"):
        neg, s = True, s[3:]
    if s in PJ:
        return s, neg
    for end, rep in (("īti", "i"), ("āti", "a")):
        if s.endswith(end):
            s = s[:-3] + rep
            break
    return (s, neg) if s in PJ else None


def pjru(v, n):
    f = PJ[v[0]]
    return f[(2 if v[1] else 0) + (1 if n == "pl" else 0)]


def pj_question(s):
    """(Ka) yo X V1 so Y V2? = «(а) Кто V1 X, тот V2 Y?»; vā pana = «А кто»; no label: as written."""
    m = re.match(r"^(?:(?P<lab>\((?:Ka|Kha)\)) )?[Yy]o(?P<vp> vā pana)? (?P<x>\S+) (?P<v1>(?:na )?\S+) so (?P<y>\S+) "
                 r"(?P<v2>(?:na )?\S+?)(?P<end>[?.])$", s)
    if not m:
        return None
    x, y = term(m.group("x")), term(m.group("y"))
    v1, v2 = pjparse(m.group("v1")), pjparse(m.group("v2"))
    if not (x and y and v1 and v2):
        return None
    lead = "А кто" if m.group("vp") else "Кто"
    lab = (S.LABEL[m.group("lab")] + " ") if m.group("lab") else ""
    return f"{lab}{lead} {pjru(v1, 'sg')} {T[x]['acc']}, тот {pjru(v2, 'sg')} {T[y]['acc']}{m.group('end')}"


def pj_answer(s):
    """P X V1, no ca (te) Y V2. = «P V1 X, но (они) V2' Y.»;  P Xñca V1 Yñca V2. = «P и V1 X, и V2 Y.»"""
    body = s[:-1]
    for pk in sorted(G2.PERSONS, key=len, reverse=True):
        if body.lower().startswith(pk + " "):
            ru, n = G2.PERSONS[pk]
            rest = norm(body[len(pk) + 1:])
            break
    else:
        return None
    m = re.match(r"^(?P<x>\S+) (?P<v1>(?:na )?\S+), no ca (?P<te>te )?(?P<y>\S+) (?P<v2>(?:na )?\S+)$", rest)
    if m:
        x, y, v1, v2 = term(m.group("x")), term(m.group("y")), pjparse(m.group("v1")), pjparse(m.group("v2"))
        if x and y and v1 and v2:
            for v in (v1, v2):
                if PJ[v[0]][4] != n:
                    slip(f"{v[0]}: Pāli verb number differs from the subject's; Russian agreement")
            they = "они " if m.group("te") else ""
            return f"{ru} {pjru(v1, n)} {T[x]['acc']}, но {they}{pjru((v2[0], not v2[1]), n)} {T[y]['acc']}."
    m = re.match(r"^(?P<x>\S+) ca (?P<v1>(?:na )?\S+) (?P<y>\S+) ca (?P<v2>(?:na )?\S+)$", rest)
    if m:
        x, y, v1, v2 = term(m.group("x")), term(m.group("y")), pjparse(m.group("v1")), pjparse(m.group("v2"))
        if x and y and v1 and v2:
            for v in (v1, v2):
                if PJ[v[0]][4] != n:
                    slip(f"{v[0]}: Pāli verb number differs from the subject's; Russian agreement")
            if v1 == v2 and v1[1]:
                return f"{ru} {pjru(v1, n)} ни {T[x]['acc']}, ни {T[y]['acc']}."
            return f"{ru} и {pjru(v1, n)} {T[x]['acc']}, и {pjru(v2, n)} {T[y]['acc']}."
    return None


# =========================================================================== headings, notes, fixed lines
G2.HEAD.update({k.lower(): v for k, v in {   # termbase
    "Suddhadhātuvāro": "раздел об элементах как таковых",
    "Suddhadhātumūlacakkavāro": "круговой раздел на основе элементов как таковых",
    "Suddhasaccavāro": "раздел об истинах как таковых",
    "Suddhasaccamūlacakkavāro": "круговой раздел на основе истин как таковых",
    "Paṇṇattivāra": "раздел об обозначениях",
}.items()})
# Editorial notes: G3 (build_rails_G3_ru, finished first) set the Āyatana / Dhātu note wording; its strings are
# imported, and the same Pāli note gets G3's Russian (coordinator). G3 convention: the full stop goes inside the
# parenthesis; sadisaṃ «одинаков(ы)», vitthāretabbaṃ «подробно изложить», kātabbaṃ «изложить», asammohantena «не
# допуская путаницы», anulomampi paccanīkampi = G3.ANUPAC, uppādepi nirodhepi uppādanirodhepi = G3.UPP3.
G3 = importlib.import_module("build_rails_G3_ru")
CAKKA = G3.CAKKA                                      # (Cakkaṃ bandhitabbaṃ) = «(Круг следует замкнуть.)»
CAKKA_S = CAKKA[1:-2]                                 # «Круг следует замкнуть»
Y, YY, YT = G3.YASSAKA, G3.YASSAYATTHAKA, G3.YATTHAKA
ANUPAC, UPP3 = G3.ANUPAC, G3.UPP3
NIRODHA_SAM = "«у вошедших в медитативное достижение прекращения»"
YATTHAKA_SAME = f"({cap(YT)} {UPP3} одинаков, различия нет.)"
NOT_CONFUSING = "не допуская путаницы"   # asammohantena (G3)
FIXED_S = {  # exact sentences / pieces
    "(Cakkaṃ bandhitabbaṃ).": CAKKA,
    "(Jivhāpi ghānadhātusadisā).": "(Язык тоже такой же, как элемент носа.)",   # ghānadhātusadisā (termbase)
    "(Saddo ghānasadiso).": "(Звук такой же, как нос.)",                        # ghānasadiso (termbase)
    "(Phoṭṭhabbo ghānasadiso).": "(Осязаемое такое же, как нос.)",
    "(Yathā āyatanayamake cakkaṃ bandhitaṃ evamidha cakkaṃ bandhitabbaṃ.)":
        "(Как в парных вопросах о сферах восприятия замкнут круг, так и здесь круг следует замкнуть.)",
    "(Cakkaṃ bandhitabbaṃ, sabbe āmantā ubhatopi sesepi).":
        f"({CAKKA_S}, все ответы «Да», и с обеих сторон, и в остальных.)",
    "(Yathā āyatanayamakassa paṇṇatti evaṃ dhātuyamakassa paṇṇatti vitthāretabbā)":
        "(Как обозначения парных вопросов о сферах восприятия, так следует подробно изложить и обозначения парных "
        "вопросов об элементах)",
    "(Yathā āyatanayamakaṃ vibhattaṃ evaṃ dhātuyamakampi vibhajitabbaṃ, sadisaṃ kātabbaṃ).":
        "(Как разобраны парные вопросы о сферах восприятия, так следует разобрать и парные вопросы об элементах, "
        "изложить одинаково.)",
    "(dhātuyamakaṃ paripuṇṇaṃ peyyālena).": "(парные вопросы об элементах даны полностью, с сокращениями.)",
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,
    "Dhātuyamakaṃ niṭṭhitaṃ.": S.yamaka_done("Dhātuyamakaṃ"),
    "Saccayamakaṃ niṭṭhitaṃ.": S.yamaka_done("Saccayamakaṃ"),
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        f"({cap(Y)} и {YY} тоже следует подробно изложить так же.)",
    "(Yassayatthakampi sadisaṃ vitthāretabbaṃ).": G3.NOTES["(Yassa yatthakampi sadisaṃ vitthāretabbaṃ)."],
    "(Yassakampi yassayatthakampi sadisaṃ).": G3.NOTES["(Yassakampi yassayatthakampi sadisaṃ)."],
    "(yatthakā sadisā sabbe).": "(все разделы с «где» одинаковы.)",
    "(yatthakampi yassayatthakasadisaṃ kātabbaṃ).": f"({YT} тоже следует изложить так же, как {YY}.)",
    "(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ).": YATTHAKA_SAME,
    "(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ).": YATTHAKA_SAME,
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ).":
        f"({cap(Y)} и {YY} тоже одинаковы, а в разделе с «у кого где» {NIRODHA_SAM} приводить не следует.)",
    "(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, natthi "
    "nānākaraṇaṃ).":
        f"(Как в разделе о возникновении разобраны вопросы о прошлом {ANUPAC}, так их следует разобрать и в "
        "разделе о прекращении, различия нет.)",
    "(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ).":
        f"(Как в разделе о возникновении разобраны вопросы о прошлом, так и в разделе о возникновении и прекращении "
        f"следует разобрать {ANUPAC}.)",
}
FIXED = {}
VB = G2.var_br


def ins_after(ru, anchor, br, last=False):
    i = ru.rfind(anchor) if last else ru.find(anchor)
    assert i >= 0, (anchor, ru)
    j = i + len(anchor)
    return ru[:j] + " " + br + ru[j:]


def _fixed():
    f = {}
    tl = translate_line
    ks = ["cakkhudhātu", "sotadhātu", "ghānadhātu", "jivhādhātu", "kāyadhātu", "rūpadhātu", "saddadhātu",
          "gandhadhātu", "rasadhātu", "phoṭṭhabbadhātu", "cakkhuviññāṇadhātu", "sotaviññāṇadhātu",
          "ghānaviññāṇadhātu", "jivhāviññāṇadhātu", "kāyaviññāṇadhātu", "manodhātu", "manoviññāṇadhātu", "dhammadhātu"]
    f["Aṭṭhārasa dhātuyo – " + ", ".join(ks) + "."] = \
        "Восемнадцать элементов – " + ", ".join(T[k]["nom"] for k in ks) + "."   # Aṭṭhārasa «восемнадцать»
    f["Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ."] = \
        "Четыре истины – " + ", ".join(T[k]["nom"] for k in ("dukkhasaccaṃ", "samudayasaccaṃ", "nirodhasaccaṃ",
                                                              "maggasaccaṃ")) + "."
    f["(Kha) dhātū [dhātu (sī. ka.) aññehi yamakehi saṃsanditabbaṃ] sotadhātu?…Pe…"] = \
        ins_after(tl("(Kha) dhātū sotadhātu?…Pe…"), "(б) Элементы",
                  VB("dhātu", "sī. ka.", note="следует сверить с другими парными вопросами"))
    f["(Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti. Cakkaṃ bandhitabbaṃ)."] = \
        f"(Как обозначения в парных вопросах о сферах восприятия, так и обозначения в парных вопросах об элементах. {CAKKA_S}.)"
    f["Kāyadhātuṃ ṭhapetvā avaseso kāyo [avaseso kāyo kāyo (syā.)], na kāyadhātu. Kāyadhātu kāyo ceva kāyadhātu ca."] = \
        ins_after(tl("Kāyadhātuṃ ṭhapetvā avaseso kāyo, na kāyadhātu. Kāyadhātu kāyo ceva kāyadhātu ca."),
                  "является телом", VB("avaseso kāyo kāyo", "syā."))
    f["Na jivhā… (saṃkhittaṃ [yaṃ saṃkhittaṃ (syā.)], ubhato āmantā)."] = \
        f"{tl('Na jivhā…')} (сокращено {VB('yaṃ saṃkhittaṃ', 'syā.')}, на оба вопроса ответ «Да».)"
    f["Kāyadhātuṃ ṭhapetvā avaseso na kāyadhātu, kāyo. Kāyañca kāyadhātuñca ṭhapetvā avaseso [avaseso kāyo (syā.)] "
      "na ceva kāyo na ca kāyadhātu."] = \
        ins_after(tl("Kāyadhātuṃ ṭhapetvā avaseso na kāyadhātu, kāyo. Kāyañca kāyadhātuñca ṭhapetvā avaseso na ceva "
                     "kāyo na ca kāyadhātu."), "элемента тела, остальное", VB("avaseso kāyo", "syā."))
    f["Sotadhātu dhātu ceva sotadhātu ca. Avasesā dhātū [avasesā dhātū dhātū (syā.)] na sotadhātu."] = \
        ins_after(tl("Sotadhātu dhātu ceva sotadhātu ca. Avasesā dhātū na sotadhātu."), "Остальные элементы",
                  VB("avasesā dhātū dhātū", "syā."))
    f["Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ dukkhasaccaṃ [avasesaṃ dukkhasaccaṃ dukkhasaccaṃ (syā.) "
      "evamuparipi], na dukkhaṃ. Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ dukkhañceva dukkhasaccañca."] = \
        ins_after(tl("Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ dukkhasaccaṃ, na dukkhaṃ. Kāyikaṃ dukkhaṃ "
                     "cetasikaṃ dukkhaṃ dukkhañceva dukkhasaccañca."), "является истиной о страдании",
                  VB("avasesaṃ dukkhasaccaṃ dukkhasaccaṃ", "syā.", note=G2.EVAMUPARIPI))
    f["Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ na dukkhaṃ [avasesaṃ dukkhasaccaṃ na dukkhaṃ (sī. syā. ka.) "
      "evaṃ avasesesu tīsu saccesu] dukkhasaccaṃ. Dukkhañca dukkhasaccañca ṭhapetvā avasesaṃ na ceva dukkhaṃ na ca "
      "dukkhasaccaṃ."] = \
        ins_after(tl("Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ na dukkhaṃ, dukkhasaccaṃ. Dukkhañca "
                     "dukkhasaccañca ṭhapetvā avasesaṃ na ceva dukkhaṃ na ca dukkhasaccaṃ."), "не является страданием",
                  VB("avasesaṃ dukkhasaccaṃ na dukkhaṃ", "sī. syā. ka.", note="так же в остальных трёх истинах"))
    f["Samudayasaccaṃ saccañceva samudayasaccañca. Avasesā saccā [avasesā saccā saccā (syā.)] na samudayasaccaṃ."] = \
        ins_after(tl("Samudayasaccaṃ saccañceva samudayasaccañca. Avasesā saccā na samudayasaccaṃ."), "Остальные истины",
                  VB("avasesā saccā saccā", "syā."))
    f["(Yatthakampi sabbattha sadisaṃ. Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ)."] = \
        f"({cap(YT)} тоже везде одинаков. Различие в тексте такое же, как выше в разделе с «где».)"
    f["(Yassakampi [yassakampi yatthakampi (sī. syā.)] yassayatthakampi sadisaṃ, yassayatthakepi "
      "nirodhasamāpannānanti cetaṃ na kātabbaṃ)."] = \
        (f"({cap(Y)} {VB('yassakampi yatthakampi', 'sī. syā.')} и {YY} тоже одинаковы, а в разделе с «у кого где» "
         f"и это {NIRODHA_SAM} приводить не следует.)")
    # ^6-5-148 / ^6-5-157: person intros with the clause cut by …pe… (the space before «…pe…» glued: house rule)
    f["Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ tesaṃ "
      "tattha …pe… itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha…pe…. (Yassakampi yassayatthakampi sadisaṃ)."] = \
        (intro_ru("Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti "
                  "asaññasattānaṃ") + " там… "
         + low1(intro_ru("itaresaṃ catuvokārānaṃ pañcavokārānaṃ")) + " там… "
         + FIXED_S["(Yassakampi yassayatthakampi sadisaṃ)."])
    a = ("Aggamaggassa uppādakkhaṇe arahantānaṃ cittassa uppādakkhaṇe yassa cittassa anantarā aggamaggaṃ "
         "paṭilabhissanti tassa cittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ")
    b = "itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe"
    d = T["dukkhasaccaṃ"]["nom"]
    f[f"{a} tesaṃ tattha dukkhasaccaṃ…pe… {b} tesaṃ tattha dukkhasaccaṃ…pe…."] = \
        f"{intro_ru(a)} там {d}… {low1(intro_ru(b))} там {d}…"
    c = person_answer("Aggamaggassa bhaṅgakkhaṇe, arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na "
                      "nirujjhissati samudayasaccañca nuppajjissati.")
    f["(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, aggamaggassa bhaṅgakkhaṇe, "
      "arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati samudayasaccañca nuppajjissati)."] = \
        (f"({cap(Y)} и {YY} тоже одинаковы, различие в истине о возникновении и истине о пути, {low1(c[:-1])}.)")
    f["(Paccuppannaatītā [paccuppannenātītā (syā.)] pucchā uppādavārepi uppādanirodhavārepi yassakampi yatthakampi "
      "yassayatthakampi anulomampi paccanīkampi sadisaṃ, asammohantena vibhajitabbā)."] = \
        (f"(Вопросы о настоящем и прошлом {VB('paccuppannenātītā', 'syā.')} и в разделе о возникновении, и в разделе "
         f"о возникновении и прекращении, и в разделе с «у кого», и в разделе с «где», и в разделе с «у кого где», "
         f"{ANUPAC} одинаковы, их следует разобрать, {NOT_CONFUSING}.)")
    f["(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā anulomampi paccanīkampi vibhattā evaṃ "
      "uppādanirodhavārepi asammohantena vibhajitabbaṃ)."] = \
        (f"(Как в разделе о прекращении разобраны вопросы о прошлом и будущем {VB('atītenānāgatā', 'syā.')} "
         f"{ANUPAC}, так и в разделе о возникновении и прекращении следует разобрать, {NOT_CONFUSING}.)")
    return f


# =========================================================================== sentence / fragment translators
SHORT_EXTRA = {"Āmantā": S.YES[:-1]}   # «Āmantā» cut by …pe… = «Да»


def q_unlabelled(s):
    """Unlabelled pavatti question (G2 frame without the label)."""
    m = re.match(r"^(Yassa|Yattha)( vā pana)? ", s)
    if not m:
        return None
    r = G2.pv_question_line(("(Kha) " if m.group(2) else "(Ka) ") + low1(s))
    return r[len("(а) "):] if r else None


SENTENCE_RULES = None


def translate_sentence(s):
    """One complete Pāli sentence (with its final «.» or «?») -> Russian, or None."""
    global SENTENCE_RULES
    if SENTENCE_RULES is None:
        SENTENCE_RULES = [G2.short_answer, G2.pv_question_line, q_unlabelled, pj_question, pn_question,
                          person_answer, place_answer, pj_answer, pn_answer, G2.colophon]
    if s in FIXED_S:
        return FIXED_S[s]
    for fn in SENTENCE_RULES:
        r = fn(s)
        if r:
            return r
    return None


def frag(s, ctx):
    """A piece cut by «…pe…» (no final punctuation, or a bare «?»)."""
    end = s[-1] if s[-1] in "?." else ""
    core = s[:-1] if end else s
    k = core.lower()
    if core in SHORT_EXTRA:
        return SHORT_EXTRA[core] + end
    if k == "yo vā pana":   # pariññā (б) cut by …pe… (G2 «А кто …»)
        return "А кто" + end
    # yassa / yattha heads, with or without a clause: «А у кого где возникнет истина о возникновении»
    m = re.match(r"^(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha)(?: (.+))?$", k)
    if m:
        rel = m.group(1).replace(" vā pana", "")
        head = ("А " if "vā pana" in m.group(1) else "") + G2.QREL[rel][0]
        if m.group(2):
            a = G2.parse_sv(m.group(2))
            if not a:
                return None
            head += f" {G2.vru(*a[1], T[a[0]]['g'])} {T[a[0]]['nom']}"
        return cap(head) + end
    # the bare verb after «yassa vā pana…pe…» (gender of the last question's 2nd term)
    v = G2.vparse(k, quoted=True)
    if v:
        return G2.vru(v[0], v[1], G2._CUR["g"]) + end
    # «X ṭhapetvā» and the bare nouns that follow it in the same chain (genitive after «кроме»)
    m = re.match(r"^(\S+) ṭhapetvā$", k)
    if m and term(m.group(1)):
        ctx["gen"] = True
        return f"{EXCEPT} {T[term(m.group(1))]['gen']}" + end
    m = re.match(r"^(na )?(\S+)$", k)
    if m and term(m.group(2)):
        t = T[term(m.group(2))]
        noun = t["gen"] if ctx.get("gen") else t["nom"]
        return cap(("не " if m.group(1) else "") + noun) + end
    r = place_single(core)
    if r:
        return r + end
    r = pn_question(core + ("?" if end == "?" else ""))
    if r:
        return r if end == "?" else r
    r = translate_sentence(core + ".")
    if r:
        return r[:-1] + end
    return None


def piece(text, ctx):
    """Text between two «…pe…»: one or more sentences, the last maybe cut."""
    out = []
    for sent in re.split(r"(?<=[.?])\s+", text.strip()):
        lab = ""
        m = re.match(r"^(\((?:Ka|Kha)\)) (.*)$", sent)
        if m and not translate_sentence(sent):
            lab, sent = S.LABEL[m.group(1)] + " ", m.group(2)
        r = translate_sentence(sent) if not lab else None
        if r is None:
            r = frag(sent, ctx)
        if r is None:
            raise ValueError(f"no formula for: {sent!r} (segment {_CUR['id']})")
        if lab:
            r = lab + cap(r)
        elif sent[:1].islower():
            r = low1(r)
        out.append(r)
    return " ".join(out)


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian, from the fixed formulas only."""
    global FIXED
    if not FIXED:
        FIXED = {"__building__": None}
        FIXED = _fixed()
    if pali.startswith("#"):
        return G2.heading(pali)
    if pali in FIXED:
        if pali.startswith("Cattāri saccāni"):
            slip("missing comma between «samudayasaccaṃ» and «nirodhasaccaṃ» in the list: rendered with the comma")
        if pali.startswith("Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ na dukkhaṃ ["):
            slip("no comma before «dukkhasaccaṃ» (the variant bracket stands there): rendered as the parallel "
                 "«…, dukkhasaccaṃ» of ^6-5-16")
        if " …pe…" in pali:
            slip("a space before «…pe…» in the Pāli: «…» glued to the word (house rule)")
        return FIXED[pali]
    r = var_line(pali)
    if r:
        return r
    if pali in FIXED_S:
        return FIXED_S[pali]
    if "Yatthakaṃ uppādavārepi" in pali:
        slip("no comma before «natthi nānākaraṇaṃ»: rendered with the comma, as the parallel note of ^6-5-90")
    line = pali.replace("…Pe…", "…pe…")
    if re.search(r"[?.] …", line):
        slip("a space between «?» / «.» and «…» in the Pāli: «…» glued (house rule; the check forbids « …»)")
    parts = re.split(r"(…(?:pe…)?)", line)
    out, ctx = "", {"gen": False}
    for i, p in enumerate(parts):
        if i % 2:
            out = out.rstrip() + "…"
            continue
        lead = " " if p.startswith(" ") and out else ""
        p = p.strip()
        if i > 0 and p.startswith("."):   # «…pe….»: the full stop after the ellipsis is dropped (never «….»)
            p = p[1:].strip()
            lead = " " if p else ""
        while p.startswith("?"):
            out += "?"
            p = p[1:].strip()
            lead = " " if p else ""
        if not p:
            continue
        out += lead + piece(p, ctx)
    return out


# =========================================================================== build + checks
def render(pali_text):
    blocks, problems = [], []
    for sid, plines in S.segs(pali_text):
        _CUR["id"] = G2._CUR["id"] = sid
        ru = []
        for i, pl in enumerate(plines):
            body = S.ID.sub("", pl) if i == len(plines) - 1 else pl
            r = translate_line(body.strip())
            problems += S.check_line(sid, body.strip(), r)
            ru.append(r)
        ru[-1] = f"{ru[-1]} ^{sid}"
        blocks.append("\n".join(ru))
    return "\n\n".join(blocks) + "\n", problems


def probe():
    bad = 0
    for ch in CHAPTERS:
        for sid, plines in S.segs((S.PALI / ch).read_text(encoding="utf-8")):
            _CUR["id"] = G2._CUR["id"] = sid
            for i, pl in enumerate(plines):
                body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
                try:
                    translate_line(body)
                except (ValueError, KeyError, AssertionError, TypeError) as e:
                    bad += 1
                    print(sid, "|", e)
    print("lines without a formula:", bad)


# strings reused unchanged from earlier approved Russian rails (asserted in main)
PI_STRINGS = {
    "pi-5": ["в момент возникновения", "в момент распада", "медитативное достижение прекращения", "существ без восприятия",
             "окончательного угасания", "Да."],
    "pi-2": ["элемент глаза", "элемент умственного сознания", "сфера объектов ума", "истина о страдании",
             "истина о пути", "телесная боль", "душевная боль"],
    "pi-1": ["зрительное сознание", "элемент ума"],
}


def notes_md():
    L = ["# notes-rails-G45: Dhātuyamaka + Saccayamaka (4, 5-01 … 5-03)", "",
         "Builder: build_rails_G45_ru.py (importlib.import_module(\"build_rails_G45_ru\"); importing writes nothing).",
         "Frames from G2 (paṇṇatti, pavatti, pariññā: register_term + parse_partial / parse_pair / partial / pair /",
         "pn_question_line / pv_question_line / heading / colophon / var_br) and G8 (moment phrases). New here:",
         "intro_ru() for long person / time / place intros, pn_answer() with «остальное» and multi-word subjects,",
         "pj_question() / pj_answer() for parijānāti + pajahati, translate_line() for «…pe…» chains.",
         "Format: Pāli = Russian, one per line.", "", "## Nouns (termbase)", ""]
    for k in ("dukkhasaccaṃ", "samudayasaccaṃ", "nirodhasaccaṃ", "maggasaccaṃ", "dukkhaṃ", "samudayo", "nirodho",
              "maggo", "saccaṃ", "saccā", "cakkhudhātu", "dhammadhātu", "dhātu", "dhātū", "cakkhu", "sotaṃ", "ghānaṃ",
              "jivhā", "kāyo", "phoṭṭhabbo", "cakkhuviññāṇaṃ", "mano", "dhammo"):
        t = T[k]
        L.append(f"{k} = {t['nom']} (gen {t['gen']}, ins {t['ins']}, acc {t['acc']})")
    L += ["kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ = телесная боль, душевная боль (APPROVED; gen телесной боли, душевной боли)",
          "dhammo = явление (no pi-6 entry; dhamma «явление» pi-1)", "", "## Paṇṇatti answers", ""]
    ex = ["Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ dukkhasaccaṃ, na dukkhaṃ.",
          "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ dukkhañceva dukkhasaccañca.",
          "Samudayasaccaṃ ṭhapetvā avaseso samudayo, na samudayasaccaṃ.",
          "Samudayasaccaṃ ṭhapetvā avaseso na samudayasaccaṃ, samudayo.",
          "Dukkhañca dukkhasaccañca ṭhapetvā avasesaṃ na ceva dukkhaṃ na ca dukkhasaccaṃ.",
          "Dukkhaṃ ṭhapetvā avasesā saccā na dukkhaṃ, saccā.",
          "Maggañca saccañca ṭhapetvā avasesā na ceva maggo na ca saccā.",
          "Samudayasaccaṃ saccañceva samudayasaccañca.", "Avasesā saccā na samudayasaccaṃ.",
          "Dibbacakkhu paññācakkhu cakkhu, na cakkhudhātu.", "Dibbasotaṃ taṇhāsotaṃ na sotadhātu, sotaṃ.",
          "Kāyadhātuṃ ṭhapetvā avaseso kāyo, na kāyadhātu.", "Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhu, dhātu.",
          "Cakkhuñca dhātuñca ṭhapetvā avasesā na ceva cakkhu na ca dhātū.",
          "(Ka) cakkhu dhātūti?", "(Kha) dhātū cakkhūti?", "(Ka) na dukkhaṃ na saccanti?"]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["avaseso / avasesaṃ = остальное (sg. «является»); avasesā = остальные (pl.); X ṭhapetvā = Кроме X (gen.)",
          "", "## Intros (person / time / place groups before «tesaṃ»)", ""]
    ex = ["Sabbesaṃ upapajjantānaṃ pavatte taṇhāvippayuttacittassa uppādakkhaṇe",
          "Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe arūpe maggassa ca phalassa ca uppādakkhaṇe",
          "Sabbesaṃ cittassa bhaṅgakkhaṇe taṇhāvippayuttamaggavippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ "
          "asaññasattānaṃ", "Arūpe maggassa uppādakkhaṇe", "Maggassa uppādakkhaṇe", "Taṇhāya bhaṅgakkhaṇe",
          "Anabhisametāvīnaṃ", "Abhisametāvīnaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe",
          "Abhisametāvīnaṃ taṇhāya bhaṅgakkhaṇe taṇhāvippayuttacitte vattamāne nirodhasamāpannānaṃ",
          "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ", "Suddhāvāsānaṃ dutiye akusale citte vattamāne",
          "Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ",
          "Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti",
          "Aggamaggasamaṅgīnaṃ arahantānaṃ ye ca puthujjanā maggaṃ na paṭilabhissanti āpāyikānaṃ asaññasattānaṃ",
          "Yassa cittassa anantarā aggamaggaṃ paṭilabhissanti ye caññe maggaṃ paṭilabhissanti",
          "Ye puthujjanā maggaṃ na paṭilabhissanti tesaṃ taṇhāya uppādakkhaṇe", "Ye maggaṃ paṭilabhissanti",
          "Aggamaggassa uppādakkhaṇe arahantānaṃ cittassa uppādakkhaṇe yassa cittassa anantarā aggamaggaṃ "
          "paṭilabhissanti tassa cittassa uppādakkhaṇe",
          "Yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa bhaṅgakkhaṇe ye caññe maggaṃ "
          "paṭilabhissanti tesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe",
          "Arahantānaṃ cittassa uppādakkhaṇe ye ca puthujjanā maggaṃ na paṭilabhissanti tesaṃ upapajjantānaṃ",
          "Pacchimacittasamaṅgīnaṃ", "Pacchimacittassa bhaṅgakkhaṇe", "Itaresaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe",
          "Arūpe aggamaggassa ca phalassa ca uppādakkhaṇe", "Arūpe aggaphalassa uppādakkhaṇe",
          "Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ", "Sarūpakānaṃ acakkhukānaṃ upapajjantānaṃ",
          "Sacittakānaṃ acakkhukānaṃ upapajjantānaṃ", "Acakkhukānaṃ upapajjantānaṃ"]
    L += [f"{p} tesaṃ = {intro_ru(p)}" for p in ex]
    L += ["rule: a moment right after a person joins it («у архатов в момент возникновения ума»; after a relative",
          "  clause with a comma); «pavatte …» and a plane + moment («arūpe maggassa …») open their own group;",
          "  groups «A, B и C» (G2.join_groups); «у них» only when no person is named; an inner «tesaṃ» before a",
          "  moment is not rendered; X-vippayutta-cittassa = «ума, не связанного с X,» (closing comma)", "",
          "## Places", ""]
    ex = ["Apāye asaññasatte tattha dukkhasaccaṃ uppajjati, no ca tattha maggasaccaṃ uppajjati.",
          "Avasese catuvokāre pañcavokāre tattha dukkhasaccañca uppajjati maggasaccañca uppajjati."]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["", "## Pariññā (parijānāti + pajahati)", ""]
    ex = ["(Ka) yo dukkhasaccaṃ parijānāti so samudayasaccaṃ pajahatīti?",
          "(Ka) yo dukkhasaccaṃ na parijānittha so samudayasaccaṃ nappajahissatīti?",
          "Arahā dukkhasaccaṃ na parijānāti, no ca samudayasaccaṃ nappajahittha.",
          "Ye maggaṃ paṭilabhissanti te dukkhasaccaṃ na parijānittha, no ca te samudayasaccaṃ nappajahissanti.",
          "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā dukkhasaccañca na parijānanti samudayasaccañca "
          "nappajahittha.",
          "Yo cakkhudhātuṃ parijānāti so sotadhātuṃ parijānātīti?"]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["pajahati устраняет; pajahittha устранил / устранили; pajahissati устранит / устранят; negatives «не …»",
          "", "## Abbreviations, notes, headings", ""]
    ex = ["(Kha) yassa vā pana…pe… uppajjitthāti? Āmantā.", "(Kha) yattha vā pana…pe…? Āmantā.",
          "Yattha dukkhasaccaṃ uppajjittha…pe….", "Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe…",
          "Na saddo…pe… na gandho na gandhadhātūti? Āmantā.", "Samudayo saccanti? Āmantā…pe….",
          "Asaññasatte tattha dukkhasaccaṃ nirujjhati…pe…."]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += [f"{k} = {v}" for k, v in FIXED_S.items()]
    ex = ["#### Suddhadhātuvāro", "#### Suddhadhātumūlacakkavāro", "#### Suddhasaccavāro",
          "#### Suddhasaccamūlacakkavāro", "#### Paṇṇattivāra", "#### Pavatti 3. uppādanirodhavāro"]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    return "\n".join(L) + "\n"


def main():
    if "--probe" in sys.argv:
        probe()
        return
    for book, lst in PI_STRINGS.items():
        txt = (S.RU / f"{book}-russian-plain.md").read_text(encoding="utf-8")
        miss = [x for x in lst if x not in txt]
        if miss:
            print(f"note: {book} strings not found: {miss}")
    problems = []
    for ch in CHAPTERS:
        pt = (S.PALI / ch).read_text(encoding="utf-8")
        ru, pr = render(pt)
        problems += pr
        e, n = S.check_file(pt, ru)
        problems += [f"{ch}: {x}" for x in e]
        (S.OUT / ch).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {ch}: {n} segments")
    slips = SLIPS + G2.SLIPS
    (S.RAILS / "notes-rails-G45.md").write_text(notes_md(), encoding="utf-8", newline="\n")
    print("wrote notes-rails-G45.md")
    for sid, note in dict.fromkeys(slips):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


VARS = [  # (Pāli bracket as written, anchor in the Russian, Russian bracket, after the last anchor?)
    ("maggavippayuttataṇhāvippayuttacittassa [taṇhāvippayuttamaggavippayuttacittassa (sī.) evaṃ puggalokāsepi "
     "nirodhavārepi]", "не связанного с путём и не связанного с жаждой",
     VB("taṇhāvippayuttamaggavippayuttacittassa", "sī.", note="так же и в разделе о личности и месте, и в разделе о "
                                                              "прекращении"), False),
    ("upapatticittassa [uppatticittassa (syā.)]", "ума перерождения", VB("uppatticittassa", "syā."), False),
    ("paṭilabhissanti ye [paṭilabhissanti tassa cittassa uppādakkhaṇe ye (sī. syā.) puggalokāsavārepi] caññe",
     "сразу после данного ума", VB("paṭilabhissanti tassa cittassa uppādakkhaṇe ye", "sī. syā.",
                                    note="и в разделе о личности и месте"), False),
    ("paṭilabhissanti [paṭilabhissanti tassa cittassa uppādakkhaṇe (sī. syā.) uppādavāre pana pāṭhantaraṃ natthi] tesaṃ",
     "сразу после данного ума", VB("paṭilabhissanti tassa cittassa uppādakkhaṇe", "sī. syā.",
                                    note="в разделе о возникновении же другого чтения нет"), False),
    ("vattamāne [vattamāne, nirodhasamāpannānaṃ asaññasattānaṃ (sī. syā.)] tesaṃ", "не связанный с жаждой",
     VB("vattamāne, nirodhasamāpannānaṃ asaññasattānaṃ", "sī. syā."), True),
    ("asaññasattā [apāyā asaññasattā (syā.)] cavantānaṃ", "среди существ без восприятия",
     VB("apāyā asaññasattā", "syā."), True),
    ("asaññasattaṃ [apāyaṃ asaññasattaṃ (syā.)] upapajjantānaṃ", "среди существ без восприятия",
     VB("apāyaṃ asaññasattaṃ", "syā."), False),
]


def var_line(pali):
    """A line with one variant bracket inside a long answer: translate without it, then put the Russian bracket
    after the anchor (the word the variant replaces)."""
    for pal, anchor, br, last in VARS:
        if pal in pali:
            clean = pali.replace(pal, re.sub(r" \[[^\]]*\]", "", pal))
            return ins_after(translate_line(clean), anchor, br, last=last)
    return None


if __name__ == "__main__":
    main()
