"""pi-6 Yamaka: Russian RAILS sample builder (preamble + 1-mulayamaka) and the binding formula strings.

Later chapter agents import this module read-only; importing writes nothing:
    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    import build_rails_sample_ru as S
    S.LABEL["(Kha)"], S.A("kusal", "pl_nom"), S.qa("kusal", 1, "eka"), S.translate_line(pali_line) ...
Run as a script (python -I -X utf8 -B build_rails_sample_ru.py) to rewrite the two chapter files and
ru-rails-formulas.md and to run the per-line checks (dash / quote / NFC / «ли» / Latin / ellipsis / id).

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
User-approved frames: pi-6-ru/ru-zeroshot-terms.md and the "User decisions" of pi-6-ru/zeroshot-coordinator-rules.md.
Translated from the Pāli; the English / Hindi pi-6 rails were a cross-check of structure only.
"""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
RU = ROOT / "AI_translation" / "russian"
OUT = RU / "pi-6-russian-plain-rails_split_chapters"
RAILS = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-6-ru" / "rails"
CHAPTERS = ["preamble.md", "1-mulayamaka.md"]
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def cap(s):
    return s[:1].upper() + s[1:]


# =========================================================================== book frame
NAMO = "Почтение Благословенному, Достойному, Полностью Пробуждённому Будде"  # pi-1
PITAKA = "В корзине Абхидхаммы"                                               # pi-1
BOOK = "Парные вопросы"                                                       # Yamakapāḷi (user)
YAMAKA = {  # ### headings and colophon titles (user, 2026-11-27)
    "Mūlayamakaṃ": "Парные вопросы о корнях",
    "Khandhayamakaṃ": "Парные вопросы о совокупностях",
    "Āyatanayamakaṃ": "Парные вопросы о сферах восприятия",
    "Dhātuyamakaṃ": "Парные вопросы об элементах",
    "Saccayamakaṃ": "Парные вопросы об истинах",
    "Saṅkhārayamakaṃ": "Парные вопросы о формирующих факторах",
    "Anusayayamakaṃ": "Парные вопросы о скрытых склонностях",
    "Cittayamakaṃ": "Парные вопросы об уме",
    "Dhammayamakaṃ": "Парные вопросы о явлениях",
    "Indriyayamakaṃ": "Парные вопросы о способностях",
}
DONE = "завершён"      # <X>vāro niṭṭhito. = «<Раздел …> завершён.» (pi-1 pattern)
DONE_PL = "завершены"  # <X>yamakapāḷi niṭṭhitā / <X>yamakaṃ niṭṭhitaṃ = «Парные вопросы о … завершены.» (user)


def yamaka_done(title_pali):
    """«Парные вопросы о корнях завершены.» for Mūlayamakapāḷi niṭṭhitā (any yamaka)."""
    return f"{YAMAKA[title_pali]} {DONE_PL}."


# =========================================================================== labels
_PL = ["Ka", "Kha", "Ga", "Gha", "Ṅa", "Ca", "Cha", "Ja", "Jha", "Ña", "Ṭa", "Ṭha", "Ḍa", "Ḍha",
       "Ṇa", "Ta", "Tha", "Da", "Dha", "Na", "Pa", "Pha", "Ba", "Bha", "Ma", "Ya", "Ra", "La"]
_RL = "а б в г д е ж з и к л м н о п р с т у ф х ц ч ш щ э ю я".split()
assert len(_PL) == len(_RL) == 28
LABEL = {f"({p})": f"({r})" for p, r in zip(_PL, _RL)}  # (Ka) = (а) … (Ja) = (з) pi-1 / pi-2; rest user

# =========================================================================== headings
UDDESO = "Перечень"                       # uddeso (pi-1 «#### Перечень»; user)
NIDDESO = "Разъяснение"                   # niddeso (pi-1; user)
MULAVARA = "Раздел о корнях"              # Mūlavāro (termbase; user)
HETUVARADI = "Раздел о причинах и другие"  # Hetuvārādi (termbase; user)
NAYA = {1: "Метод корней", 2: "Метод корней корней",                # Mūlanayo, Mūlamūlanayo
        3: "Метод основания на корне", 4: "Метод основания на корне корней"}  # Mūlakanayo, Mūlamūlakanayo

# =========================================================================== classes
# Pāli stems WITHOUT the final -a: plural «kusal-ā», neuter «kusal-aṃ», compound «kusal-a-mūlā».
CLS = {
    "kusal":    {"stem": "благ", "t": "oy", "n": 3},                 # kusala = благой (pi-1)
    "akusal":   {"stem": "неблаг", "t": "oy", "n": 3},               # akusala = неблагой (pi-1)
    "abyākat":  {"stem": "этически неопределённ", "t": "yy", "n": 3},  # abyākata (pi-1)
    "nām":      {"stem": "умственн", "t": "yy", "n": 9},             # nāma = умственный (termbase; pi-1 «Умственное»)
}
END = {
    "oy": {"m_nom": "ой", "f_nom": "ая", "n_nom": "ое", "pl_nom": "ие", "mn_gen": "ого", "pl_gen": "их",
           "pl_dat": "им", "mn_ins": "им", "f_ins": "ой", "mn_prep": "ом", "pl_ins": "ими"},
    "yy": {"m_nom": "ый", "f_nom": "ая", "n_nom": "ое", "pl_nom": "ые", "mn_gen": "ого", "pl_gen": "ых",
           "pl_dat": "ым", "mn_ins": "ым", "f_ins": "ой", "mn_prep": "ом", "pl_ins": "ыми"},
}
NUM = {3: ("три", "корня"), 9: ("девять", "корней")}  # Tīṇeva / Naveva


def ckey(s):
    """Pāli class token (any case) -> CLS key."""
    k = s.lower()
    assert k in CLS, s
    return k


def A(c, form):
    """Class adjective in a given form: A('kusal','pl_nom') = 'благие'."""
    d = CLS[c]
    return d["stem"] + END[d["t"]][form]


def class_heading(c):
    return cap(A(c, "pl_nom")) + " явления"  # Kusalā dhammā = Благие явления (pi-1)


# =========================================================================== predicates
# method m: 1 mūla, 2 mūlamūla, 3 mūlaka, 4 mūlamūlaka; kind: plain (X-mūlā), eka (X-mūlena eka-), anna (X-mūlena aññamañña-)
METHOD = {"mūl": 1, "mūlamūl": 2, "mūlak": 3, "mūlamūlak": 4}
RR = {1: "", 2: " корней", 3: "", 4: " корней"}   # root of roots: «корень корней»
BASED = {1: False, 2: False, 3: True, 4: True}    # -mūlaka: «основанный на … корне»
SHARE = {"eka": ("общий", "общего", "общем"), "anna": ("взаимный", "взаимного", "взаимном")}  # acc/nom, gen, prep


def pred(c, m, kind):
    """All the forms of the predicate Y of a pair question (user frame + termbase terms).

    keys: fin_pl (они …), fin_n (оно …), fin_f (она …), neg_n, part_pl (явления, …), noun_nom / noun_ins (plain m1/m2)
    """
    rr = RR[m]
    p = {}
    if kind == "plain" and not BASED[m]:          # kusalamūlā = благие корни; -mūlamūlā = благие корни корней
        p["noun_nom"] = f"{A(c, 'pl_nom')} корни{rr}"
        p["noun_ins"] = f"{A(c, 'pl_ins')} корнями{rr}"
        p["fin_pl"] = f"являются {p['noun_ins']}"
        p["neg_pl"] = f"не являются {p['noun_ins']}"
        return p
    if kind == "plain":                           # kusalamūlakā = основанный на благом корне (корней)
        loc = f"на {A(c, 'mn_prep')} корне{rr}"
    else:
        acc, gen, prep = SHARE[kind]
        if not BASED[m]:                          # ekamūlā = имеющий общий корень; kusalamūlena = благой корень
            obj = f"{acc} {A(c, 'm_nom')} корень{rr}"
            gobj = f"{gen} {A(c, 'mn_gen')} корня{rr}"
            p.update(fin_pl=f"имеют {obj}", fin_n=f"имеет {obj}", fin_f=f"имеет {obj}",
                     neg_n=f"не имеет {gobj}", part_pl=f"имеющие {obj}")
            return p
        loc = f"на {prep} {A(c, 'mn_prep')} корне{rr}"   # ekamūlakā = основанный на общем корне
    p.update(fin_pl=f"основаны {loc}", fin_n=f"основано {loc}", fin_f=f"основана {loc}",
             neg_n=f"не основано {loc}", part_pl=f"основанные {loc}")
    return p


# =========================================================================== question frames (user)
def qa(c, m, kind):
    """(Ka) ye keci X dhammā, sabbe te Y? = (а) Все X явления Y?
    (Ka) ye keci X-mūlena eka-M dhammā, sabbe te X-mūlena aññamañña-M? = (а) Все явления, Z, Y?"""
    if kind == "anna":
        z = pred(c, m, "eka")["part_pl"]
        return f"{LABEL['(Ka)']} Все явления, {z}, {pred(c, m, 'anna')['fin_pl']}?"
    return f"{LABEL['(Ka)']} Все {A(c, 'pl_nom')} явления {pred(c, m, kind)['fin_pl']}?"


def qb(c, m, kind):
    """(Kha) ye vā pana Y, sabbe te dhammā X? = (б) А все Y относятся к X явлениям? (noun Y)
    / (б) А всё, что Y (sg.), относится к X явлениям? (predicate Y)"""
    p = pred(c, m, kind)
    tail = f"к {A(c, 'pl_dat')} явлениям?"
    if "noun_nom" in p:
        return f"{LABEL['(Kha)']} А все {p['noun_nom']} относятся {tail}"
    return f"{LABEL['(Kha)']} А всё, что {p['fin_n']}, относится {tail}"


# =========================================================================== answers
YES = "Да."  # Āmantā. (pi-5; user)


def only(c, m):
    """Tīṇeva kusalamūlāni. = Есть только три благих корня. / Naveva nāmamūlāni. = Есть только девять умственных корней."""
    num, noun = NUM[CLS[c]["n"]]
    return f"Есть только {num} {A(c, 'pl_gen')} {noun}{RR[m]}."


def rest(c, m):
    """Avasesā kusalā dhammā na kusalamūlā. = Остальные благие явления не являются благими корнями."""
    return f"Остальные {A(c, 'pl_nom')} явления {pred(c, m, 'plain')['neg_pl']}."


def ahetu(c, m, kind):
    """Ahetukaṃ akusalaṃ (akusalamūlena) na (eka)M. = Неблагое, не имеющее корней, не имеет общего неблагого корня."""
    return f"{cap(A(c, 'n_nom'))}, не имеющее корней, {pred(c, m, kind)['neg_n']}."


def sahetu(c, m, kind):
    """Sahetukaṃ akusalaṃ (akusalamūlena) (eka)M. = Неблагое, имеющее корни, имеет общий неблагой корень."""
    return f"{cap(A(c, 'n_nom'))}, имеющее корни, {pred(c, m, kind)['fin_n']}."


def samut(c, m, kind):
    """Kusalasamuṭṭhānaṃ rūpaṃ kusalamūlena ekamūlaṃ, na kusalaṃ.
    = Материальная форма, порождённая благим, имеет общий благой корень, но не является благой."""
    return (f"Материальная форма, порождённая {A(c, 'mn_ins')}, {pred(c, m, kind)['fin_f']}, "
            f"но не является {A(c, 'f_ins')}.")


def both(c, m, kind):
    """Kusalaṃ kusalamūlena ekamūlañceva kusalañca. = Благое и имеет общий благой корень, и является благим."""
    return f"{cap(A(c, 'n_nom'))} и {pred(c, m, kind)['fin_n']}, и является {A(c, 'mn_ins')}."


def both_roots(m):
    """… ekamūlāni ceva aññamaññamūlāni ca: one verb, then «и A, и B» (user rule)."""
    rr = RR[m]
    if BASED[m]:
        return f"основаны и на общем корне{rr}, и на взаимном корне{rr}"
    return f"имеют и общий корень{rr}, и взаимный корень{rr}"


def together(c, m):
    """Mūlāni yāni ekato uppajjanti kusalamūlāni ekamūlāni ceva aññamaññamūlāni ca.
    = Благие корни, которые возникают вместе, имеют и общий корень, и взаимный корень. (user)"""
    return f"{cap(A(c, 'pl_nom'))} корни, которые возникают вместе, {both_roots(m)}."


def sahajata(c, m):
    """Avasesā kusalamūlasahajātā dhammā kusalamūlena ekamūlā, na ca aññamaññamūlā.
    = Остальные явления, возникшие вместе с благим корнем, имеют общий благой корень, но не имеют взаимного корня."""
    rr = RR[m]
    neg = f"не основаны на взаимном корне{rr}" if BASED[m] else f"не имеют взаимного корня{rr}"
    return f"Остальные явления, возникшие вместе с {A(c, 'mn_ins')} корнем, {pred(c, m, 'eka')['fin_pl']}, но {neg}."


# =========================================================================== Hetuvārādi series and verse
# the ten names of a root (verse) and the series members X-hetū … X-samudayā (instrumental after «являются»)
SERIES = [("hetū", "причинами", True), ("nidānā", "источниками", True), ("sambhavā", "началами", True),
          ("ppabhavā", "истоками", True), ("samuṭṭhānā", "порождающими факторами", True),
          ("āhārā", "питанием", False), ("ārammaṇā", "объектами", True), ("paccayā", "условиями", True),
          ("samudayā", "возникновениями", True)]


def series_pali(c, i):
    suf = SERIES[i][0]
    return c + suf if suf.startswith("ā") else c + "a" + suf


def series_ru(c, i):
    _, noun, pl = SERIES[i]
    return f"{A(c, 'pl_ins' if pl else 'mn_ins')} {noun}"


def series_run(c, start=0):
    """«благими причинами… благими источниками… … благими возникновениями…» (…pe… and … alike = «…»)"""
    return "… ".join(series_ru(c, i) for i in range(start, len(SERIES))) + "…"


VERSE_1 = "Корень, причина и источник, начало вместе с истоком;"   # Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;
VERSE_2 = "Порождающий фактор, питание, объект, условие вместе с возникновением."  # Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.
VAR_SAMUT = "[вариант чтения (Ka.): samuṭṭhānāhārārammaṇaṃ]"
VERSE_2_VAR = f"Порождающий фактор, питание, объект {VAR_SAMUT}, условие вместе с возникновением."
TAYO_HETU = "Есть только три {pl} причины"  # Tayo eva kusalahetū (user)


def fixed_lines():
    """Exact Pāli line -> Russian, for one-off lines (colophons, verse, the Hetuvārādi series)."""
    f = {
        "Namo tassa bhagavato arahato sammāsambuddhassa": NAMO,
        "Mūlavārauddeso.": "Перечень раздела о корнях.",
        "Mūlavāraniddeso.": "Разъяснение раздела о корнях.",
        "Uddesavāro niṭṭhito.": f"Раздел перечня {DONE}.",
        "Niddesavāro niṭṭhito.": f"Раздел разъяснения {DONE}.",
        "Mūlayamakapāḷi niṭṭhitā.": yamaka_done("Mūlayamakaṃ"),
        "Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;": VERSE_1,
        "Samuṭṭhānāhārārammaṇā [samuṭṭhānāhārārammaṇaṃ (ka.)], paccayo samudayena cāti.": VERSE_2_VAR,
        "Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.": VERSE_2,
    }
    c = "kusal"
    # uddesa: Ye keci kusalā dhammā, sabbe te kusalahetū…pe… … kusalasamudayā…pe….
    f["Ye keci kusalā dhammā, sabbe te " + "…pe… ".join(series_pali(c, i) for i in range(len(SERIES))) + "…pe…."] = \
        f"Все {A(c, 'pl_nom')} явления являются {series_run(c)}"
    # niddesa ^6-1-98
    f[f"Ye keci kusalā dhammā, sabbe te {series_pali(c, 0)}ti…?"] = f"Все {A(c, 'pl_nom')} явления являются {series_ru(c, 0)}…?"
    f[f"Tayo eva {series_pali(c, 0)}, avasesā kusalā dhammā na {series_pali(c, 0)}…pe… "
      + "… ".join(series_pali(c, i) for i in range(1, len(SERIES))) + "…."] = \
        f"{TAYO_HETU.format(pl=A(c, 'pl_nom'))}, остальные {A(c, 'pl_nom')} явления не являются {series_run(c)}"
    # niddesa ^6-1-99 (nāmahetū ti: a stray space before -ti in the Pāli; -ti is not rendered)
    n = "nām"
    f["Ye keci akusalā dhammā… ye keci abyākatā dhammā… ye keci nāmā dhammā, sabbe te nāmahetū ti… "
      + "… ".join(series_pali(n, i) for i in range(1, len(SERIES))) + "…."] = \
        (f"Все {A('akusal', 'pl_nom')} явления… все {A('abyākat', 'pl_nom')} явления… "
         f"все {A(n, 'pl_nom')} явления являются {series_run(n)}")
    return f


FIXED = fixed_lines()

# =========================================================================== heading translator
HEAD = {k.lower(): v for k, v in {
    "Abhidhammapiṭake": PITAKA, "Yamakapāḷi": BOOK, **YAMAKA,
    "uddeso": UDDESO, "niddeso": NIDDESO, "Mūlavāro": MULAVARA, "Hetuvārādi": HETUVARADI,
    "Mūlanayo": NAYA[1], "Mūlamūlanayo": NAYA[2], "Mūlakanayo": NAYA[3], "Mūlamūlakanayo": NAYA[4],
    **{f"{c}ā dhammā": class_heading(c) for c in CLS},
}.items()}


def heading(text):
    """'#### Akusalā dhammā (1) mūlanayo' -> '#### Неблагие явления (1) Метод корней'.
    Labels (Ka) -> (а); numbers stay; every chunk after a label or number starts with a capital (coordinator rule)."""
    hashes, body = text.split(" ", 1)
    out = []
    for p in re.split(r"(\([^)]+\)|\d+-\d+\.)", body):
        p = p.strip()
        if not p:
            continue
        if p in LABEL:
            out.append(LABEL[p])
        elif re.fullmatch(r"\(\d+\)|\d+-\d+\.", p):
            out.append(p)
        else:
            out.append(cap(HEAD[p.lower()]))
    return f"{hashes} {' '.join(out)}"


# =========================================================================== sentence recognizers
_C = r"(akusal|kusal|abyākat|nām)"
_M = r"(mūlamūlak|mūlamūl|mūlak|mūl)"


def _rx(p):
    return re.compile("^" + p.replace("{C}", _C).replace("{M}", _M) + "$", re.I)


SLIPS = []  # (segment id, note) filled while translating


def _one(vals):
    vals = [v.lower() for v in vals]
    assert len(set(vals)) == 1, vals
    return vals[0]


def _cm(g, ci, mi):
    c = ckey(_one([g[i] for i in ci]))
    m = METHOD[_one([g[i] for i in mi])]
    return c, m


RULES = [
    # questions (а)
    (_rx(r"\(Ka\) ye keci {C}ā dhammā, sabbe te {C}a{M}ā(?:ti)?\?"),
     lambda g: qa(*_cm(g, [0, 1], [2]), "plain")),
    (_rx(r"\(Ka\) ye keci {C}ā dhammā, sabbe te {C}amūlena eka{M}ā(?:ti)?\?"),
     lambda g: qa(*_cm(g, [0, 1], [2]), "eka")),
    (_rx(r"\(Ka\) ye keci {C}amūlena eka{M}ā dhammā, sabbe te {C}amūlena aññamañña{M}ā(?:ti)?\?"),
     lambda g: qa(*_cm(g, [0, 2], [1, 3]), "anna")),
    # questions (б)
    (_rx(r"\(Kha\) ye vā pana {C}a{M}ā, sabbe te dhammā {C}ā(?:ti)?\?"),
     lambda g: qb(*_cm(g, [0, 2], [1]), "plain")),
    (_rx(r"\(Kha\) ye vā pana {C}amūlena eka{M}ā, sabbe te dhammā {C}ā(?:ti)?\?"),
     lambda g: qb(*_cm(g, [0, 2], [1]), "eka")),
    (_rx(r"\(Kha\) ye vā pana {C}amūlena aññamañña{M}ā, sabbe te dhammā {C}ā(?:ti)?\?"),
     lambda g: qb(*_cm(g, [0, 2], [1]), "anna")),
    # answers
    (_rx(r"Āmantā\."), lambda g: YES),
    (_rx(r"(Tīṇ|Nav)eva {C}a{M}āni\."),
     lambda g: (lambda c, m: (assert_num(g[0], c), only(c, m))[1])(*_cm(g, [1], [2]))),
    (_rx(r"Avasesā {C}ā dhammā na {C}a{M}ā\."), lambda g: rest(*_cm(g, [0, 1], [2]))),
    (_rx(r"Ahetukaṃ {C}aṃ {C}amūlena na eka{M}aṃ\."), lambda g: ahetu(*_cm(g, [0, 1], [2]), "eka")),
    (_rx(r"Sahetukaṃ {C}aṃ {C}amūlena eka{M}aṃ\."), lambda g: sahetu(*_cm(g, [0, 1], [2]), "eka")),
    (_rx(r"Ahetukaṃ {C}aṃ na {C}a{M}aṃ\."), lambda g: ahetu(*_cm(g, [0, 1], [2]), "plain")),
    (_rx(r"Sahetukaṃ {C}aṃ {C}a{M}aṃ\."), lambda g: sahetu(*_cm(g, [0, 1], [2]), "plain")),
    (_rx(r"{C}asamuṭṭhānaṃ rūpaṃ {C}amūlena eka{M}aṃ(,?) na {C}aṃ\."),
     lambda g: (_comma(g[3], "Csamuṭṭhānaṃ rūpaṃ … ekaM, na …"), samut(*_cm(g, [0, 1, 4], [2]), "eka"))[1]),
    (_rx(r"{C}asamuṭṭhānaṃ rūpaṃ {C}a{M}aṃ(,?) na {C}aṃ\."),
     lambda g: (_comma(g[3], "Csamuṭṭhānaṃ rūpaṃ CM, na …"), samut(*_cm(g, [0, 1, 4], [2]), "plain"))[1]),
    (_rx(r"{C}aṃ {C}amūlena eka{M}añceva {C}añca\."), lambda g: both(*_cm(g, [0, 1, 3], [2]), "eka")),
    (_rx(r"{C}aṃ {C}a{M}añceva {C}añca\."), lambda g: both(*_cm(g, [0, 1, 3], [2]), "plain")),
    (_rx(r"Mūlāni yāni ekato uppajjanti {C}amūlāni eka{M}āni ceva aññamañña{M}āni ca\."),
     lambda g: together(*_cm(g, [0], [1, 2]))),
    (_rx(r"Avasesā {C}amūlasahajātā dhammā {C}amūlena eka{M}ā(,?) na ca aññamañña{M}ā\."),
     lambda g: (_comma(g[3], "… ekaM, na ca aññamaññaM"), sahajata(*_cm(g, [0, 1], [2, 4])))[1]),
]

_CUR = {"id": None}


def assert_num(tok, c):
    assert {"tīṇ": 3, "nav": 9}[tok.lower()] == CLS[c]["n"], (tok, c)


def _comma(found, what):
    if not found:
        SLIPS.append((_CUR["id"], f"missing comma ({what}); rendered with the comma"))


def translate_sentence(s):
    for rx, fn in RULES:
        mt = rx.match(s)
        if mt:
            return fn(mt.groups())
    raise ValueError(f"no formula for: {s!r} (segment {_CUR['id']})")


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian, from the fixed formulas only."""
    if pali.startswith("#"):
        return heading(pali)
    if pali in FIXED:
        return FIXED[pali]
    return " ".join(translate_sentence(s) for s in re.split(r"(?<=[.?])\s+", pali.strip()))


# =========================================================================== build + checks
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
    assert not cur, "trailing lines without an id"
    return out


DASHES = ("–", "—")
LATIN = re.compile(r"[A-Za-zÀ-ɏḀ-ỿ]")


def check_line(sid, p, r):
    """Per-line checks; returns a list of problems."""
    e = []
    if sum(p.count(d) for d in DASHES) != sum(r.count(d) for d in DASHES):
        e.append("dash count differs from the Pāli")
    if "—" in r:
        e.append("em dash")
    if ":-" in r:
        e.append("':-'")
    if r != unicodedata.normalize("NFC", r):
        e.append("not NFC")
    if '"' in r or r.count("„") != r.count("“") or r.count("«") != r.count("»"):
        e.append("quotes")
    if re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", r):
        e.append("«ли»")
    if "…." in r or " …" in r or "pe" in r:
        e.append("ellipsis")
    if p.count("?") != r.count("?"):
        e.append("question-mark count differs")
    if LATIN.search(re.sub(r"\[[^\]]*\]", "", ID.sub("", r))):
        e.append("Latin outside brackets")
    if p.startswith("#") and p.split(" ", 1)[0] != r.split(" ", 1)[0]:
        e.append("heading level")
    if r.strip() != r or "  " in r:
        e.append("spacing")
    return [f"{sid}: {x}: {r}" for x in e]


def render(pali_text):
    blocks, problems = [], []
    for sid, plines in segs(pali_text):
        _CUR["id"] = sid
        ru = []
        for i, pl in enumerate(plines):
            body = ID.sub("", pl) if i == len(plines) - 1 else pl
            r = translate_line(body.strip())
            problems += check_line(sid, body.strip(), r)
            ru.append(r)
        assert len(ru) == len(plines)
        ru[-1] = f"{ru[-1]} ^{sid}"
        blocks.append("\n".join(ru))
    return "\n\n".join(blocks) + "\n", problems


def check_file(pali_text, ru_text):
    """Whole-file checks: ids in order, per-segment line counts, blank lines, CR."""
    e = []
    ps, rs = segs(pali_text), segs(ru_text)
    if [i for i, _ in ps] != [i for i, _ in rs]:
        e.append("block IDs differ")
    if [len(x) for _, x in ps] != [len(x) for _, x in rs]:
        e.append("line counts differ")
    if "\r" in ru_text or "\n\n\n" in ru_text:
        e.append("CR or double blank line")
    return e, len(rs)


# strings taken unchanged from the approved Russian rails of earlier books (asserted in main)
PI1_STRINGS = [NAMO, PITAKA, f"#### {UDDESO}", NIDDESO, "Четверичный метод", "(а) Благие явления",
               "(б) Неблагие явления", "(в) Этически неопределённые явления", "(а) Умственное.",
               "имеющие корни", "не имеющие корней", "возникают вместе", "возникшее вместе с",
               "материальная форма, порождённая", "Раздел о материальной форме завершён."]
PI2_STRINGS = [NAMO, PITAKA]
PI5_STRINGS = ["? Да."]


# =========================================================================== formulas file
def formulas_md():
    ks = list(CLS)
    pal = {"kusal": "kusala", "akusal": "akusala", "abyākat": "abyākata", "nām": "nāma"}
    msuf = {1: "mūl", 2: "mūlamūl", 3: "mūlak", 4: "mūlamūlak"}
    L = ["# pi-6 Yamaka: Russian rails sentence formulas (binding for chapter agents)", "",
         "Format: Pāli = Russian, one per line. Generated by build_rails_sample_ru.py (import its constants and",
         "functions: LABEL, A(), pred(), qa(), qb(), only(), rest(), ahetu(), sahetu(), samut(), both(), together(),",
         "sahajata(), series_run(), heading(), translate_line(); importing writes nothing).",
         "Termbase: AI_translation/russian/pi-6-pali-russian-termbase-plain.md with pi-6-ru/termbase/APPROVED.md.",
         "(pi-1) / (pi-2) / (pi-5) = string taken unchanged from that book's approved Russian rails (main() asserts it);",
         "(user) = frame or string the user approved on 2026-11-27 (ru-zeroshot-terms.md, coordinator rules).", "",
         "## Book frame, titles, closing lines", "",
         f"Namo tassa bhagavato arahato sammāsambuddhassa = {NAMO} (pi-1) (pi-2)",
         f"# Abhidhammapiṭake = # {PITAKA} (pi-1) (pi-2)",
         f"## Yamakapāḷi = ## {BOOK} (user; mid-sentence «{BOOK}»)"]
    L += [f"### {p} = ### {r} (user)" for p, r in YAMAKA.items()]
    L += [f"Mūlayamakapāḷi niṭṭhitā. = {yamaka_done('Mūlayamakaṃ')} (user; every yamaka: «<title> {DONE_PL}.»)",
          f"Uddesavāro niṭṭhito. = Раздел перечня {DONE}. (user; «… {DONE}.» pi-1)",
          f"Niddesavāro niṭṭhito. = Раздел разъяснения {DONE}. (user)",
          "Mūlavārauddeso. = Перечень раздела о корнях. (user)",
          "Mūlavāraniddeso. = Разъяснение раздела о корнях. (user)",
          f"Namo tassa … (closing line of the chapter) = {NAMO} (pi-1)",
          "", "## Labels, numbers, punctuation", "",
          " ".join(LABEL) + " = " + " ".join(LABEL.values())
          + " (pi-1 / pi-2 up to (Ja) = (з); the rest user: Russian alphabet without ё, й, ъ, ы, ь)",
          "(1) (2) (3) (4), 2-10. = unchanged digits; the hyphen stays a hyphen (no dash: none in the Pāli)",
          "…pe… / … = «…» glued to the word before it, a space after it; a final «…pe….» / «….» = «…» (never «….»)",
          "-ti? / -ti…? (quotation ending) = not rendered; «?» stays",
          "Statements end with «.», questions with «?», never «ли». No dash anywhere in this chapter (none in the Pāli).",
          f"[samuṭṭhānāhārārammaṇaṃ (ka.)] = {VAR_SAMUT} (ending differs: reading, not spelling)",
          "missing comma before «na» / «na ca» in a partial answer = rendered with the comma (missing punctuation)",
          "", "## Headings (first word after a label or number capitalised)", "",
          f"uddeso = {UDDESO} (pi-1) (user); #### (Ka) uddeso = #### {heading('#### (Ka) uddeso')[5:]}",
          f"niddeso = {NIDDESO} (pi-1) (user); ##### (Kha) niddeso = ##### {heading('##### (Kha) niddeso')[6:]}",
          "-vāro = Раздел … (pi-1, pi-2) (user); -nayo = метод (pi-1 «Четверичный метод») (user)",
          f"Mūlavāro = {MULAVARA} (user)",
          f"2-10. Hetuvārādi = {heading('#### 2-10. Hetuvārādi')[5:]} (user)",
          f"(1) Mūlanayo = (1) {NAYA[1]} (user)",
          f"(2) Mūlamūlanayo = (2) {NAYA[2]} (user)",
          f"(3) Mūlakanayo = (3) {NAYA[3]} (user)",
          f"(4) Mūlamūlakanayo = (4) {NAYA[4]} (user)"]
    for c in ks:
        tag = "(pi-1)" if c != "nām" else "(user)"
        L.append(f"{cap(c)}ā dhammā = {class_heading(c)} {tag}")
    L += [f"Akusalā dhammā (1) mūlanayo = {heading('#### Akusalā dhammā (1) mūlanayo')[5:]} (order as in the Pāli; capital after the number: coordinator rule)",
          "", "## Class forms (A(c, form)); termbase kusala благой, akusala неблагой, abyākata этически неопределённый, nāma умственный", ""]
    for c in ks:
        L.append(f"{pal[c]}: " + ", ".join(f"{f} {A(c, f)}" for f in END['oy']))
    L += ["", "## Pair questions (user frames; Y slot from the termbase, inflected)", "",
          "(Ka) ye keci X dhammā, sabbe te Y? = (а) Все X явления Y? (user)",
          "(Ka) ye keci X-mūlena eka-M dhammā, sabbe te X-mūlena aññamañña-M? = (а) Все явления, имеющие/основанные …, Y? (user)",
          "(Kha) ye vā pana Y (noun), sabbe te dhammā X? = (б) А все Y относятся к X явлениям? (user)",
          "(Kha) ye vā pana Y (predicate), sabbe te dhammā X? = (б) А всё, что Y (sg.), относится к X явлениям? (user)",
          "Y slots: X-mūlā = являются X корнями; X-mūlena ekamūlā = имеют общий X корень; X-mūlena aññamaññamūlā = имеют взаимный X корень;",
          "  -mūlamūla- = … корни корней / корень корней; X-mūlakā = основаны на X корне; X-mūlena eka-/aññamaññamūlakā = основаны на общем / взаимном X корне (user; termbase)",
          ""]
    for c in ks:
        X = pal[c]
        for m in (1, 2, 3, 4):
            s = msuf[m]
            L += [f"(Ka) ye keci {X[:-1]}ā dhammā, sabbe te {X}{s}ā? = {qa(c, m, 'plain')}",
                  f"(Kha) ye vā pana {X}{s}ā, sabbe te dhammā {X[:-1]}ā? = {qb(c, m, 'plain')}",
                  f"(Ka) ye keci {X[:-1]}ā dhammā, sabbe te {X}mūlena eka{s}ā? = {qa(c, m, 'eka')}",
                  f"(Kha) ye vā pana {X}mūlena eka{s}ā, sabbe te dhammā {X[:-1]}ā? = {qb(c, m, 'eka')}",
                  f"(Ka) ye keci {X}mūlena eka{s}ā dhammā, sabbe te {X}mūlena aññamañña{s}ā? = {qa(c, m, 'anna')}",
                  f"(Kha) ye vā pana {X}mūlena aññamañña{s}ā, sabbe te dhammā {X[:-1]}ā? = {qb(c, m, 'anna')}"]
        L.append("")
    L += ["## Answers", "",
          f"Āmantā. = {YES} (pi-5) (user)"]
    for c in ks:
        X = pal[c]
        num = "Tīṇeva" if CLS[c]["n"] == 3 else "Naveva"
        for m in (1, 2):
            s = msuf[m]
            L += [f"{num} {X}{s}āni. = {only(c, m)} (user)",
                  f"Avasesā {X[:-1]}ā dhammā na {X}{s}ā. = {rest(c, m)} (user)"]
    L += ["", "### Partial answers (say which are and which are not; user frames)", ""]
    for c in ks:
        X = pal[c]
        N = X[:-1] + "aṃ"
        for m in (1, 2, 3, 4):
            s = msuf[m]
            if c != "kusal":
                L += [f"Ahetukaṃ {N} {X}mūlena na eka{s}aṃ. = {ahetu(c, m, 'eka')} (user)",
                      f"Sahetukaṃ {N} {X}mūlena eka{s}aṃ. = {sahetu(c, m, 'eka')} (user)"]
                if BASED[m]:
                    L += [f"Ahetukaṃ {N} na {X}{s}aṃ. = {ahetu(c, m, 'plain')} (user)",
                          f"Sahetukaṃ {N} {X}{s}aṃ. = {sahetu(c, m, 'plain')} (user)"]
            if c != "abyākat":
                L += [f"{cap(X)}samuṭṭhānaṃ rūpaṃ {X}mūlena eka{s}aṃ, na {N}. = {samut(c, m, 'eka')} (user)",
                      f"{cap(N)} {X}mūlena eka{s}añceva {N[:-1]}ñca. = {both(c, m, 'eka')} (user)"]
                if BASED[m]:
                    L += [f"{cap(X)}samuṭṭhānaṃ rūpaṃ {X}{s}aṃ, na {N}. = {samut(c, m, 'plain')} (user)",
                          f"{cap(N)} {X}{s}añceva {N[:-1]}ñca. = {both(c, m, 'plain')} (user)"]
            L += [f"Mūlāni yāni ekato uppajjanti {X}mūlāni eka{s}āni ceva aññamañña{s}āni ca. = {together(c, m)} (user)",
                  f"Avasesā {X}mūlasahajātā dhammā {X}mūlena eka{s}ā, na ca aññamañña{s}ā. = {sahajata(c, m)} (user)"]
        L.append("")
    L += ["Rule (user): «X ceva … Y ca» after a relative clause = one verb, then «и X, и Y»; without a relative clause",
          "the subject + «и <verb> …, и <verb> …» stays («Благое и имеет общий благой корень, и является благим.»).",
          "ahetuka / sahetuka = не имеющий корней / имеющий корни (pi-1); ekato uppajjanti = возникают вместе (pi-1);",
          "sahajāta = возникший вместе с (pi-1); X-samuṭṭhānaṃ rūpaṃ = материальная форма, порождённая X (pi-1 «порождённая умом»).",
          "", "## Hetuvārādi (2-10)", ""]
    for p, r in FIXED.items():
        if p.startswith(("Ye keci", "Tayo", "Mūlaṃ", "Samuṭṭhān")):
            L.append(f"{p} = {r}")
    L += ["series members (instrumental after «являются»): hetū причинами, nidānā источниками, sambhavā началами,",
          "  pabhavā истоками, samuṭṭhānā порождающими факторами, āhārā питанием (sg.), ārammaṇā объектами,",
          "  paccayā условиями, samudayā возникновениями (termbase; hetu = «причина» here, mūla = «корень»: user)",
          f"Tayo eva X-hetū = {TAYO_HETU.format(pl='X(pl.)')} (user)", ""]
    return "\n".join(L) + "\n"


def main():
    pi1 = (RU / "pi-1-russian-plain.md").read_text(encoding="utf-8")
    pi2 = (RU / "pi-2-russian-plain.md").read_text(encoding="utf-8")
    pi5 = (RU / "pi-5-russian-plain.md").read_text(encoding="utf-8")
    for name, txt, lst in (("pi-1", pi1, PI1_STRINGS), ("pi-2", pi2, PI2_STRINGS), ("pi-5", pi5, PI5_STRINGS)):
        miss = [s for s in lst if s not in txt]
        assert not miss, f"{name} strings not found: {miss}"
    problems = []
    OUT.mkdir(parents=True, exist_ok=True)
    for ch in CHAPTERS:
        pt = (PALI / ch).read_text(encoding="utf-8")
        ru, pr = render(pt)
        problems += pr
        e, n = check_file(pt, ru)
        problems += [f"{ch}: {x}" for x in e]
        (OUT / ch).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {ch}: {n} segments")
    (RAILS / "ru-rails-formulas.md").write_text(formulas_md(), encoding="utf-8", newline="\n")
    print("wrote ru-rails-formulas.md;", len(PI1_STRINGS) + len(PI2_STRINGS) + len(PI5_STRINGS), "earlier-book strings verified")
    for sid, note in SLIPS:
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
