"""pi-6 Yamaka, G3 (Āyatanayamaka 3-01 … 3-06): Russian RAILS builder.

Built on the frame-setter G2 (build_rails_G2_ru: paṇṇatti, pavatti, pariññā frames); G8 (moment phrases) is
imported for completeness, but the Āyatanayamaka has no moment phrases. Importing this module writes nothing:
    import sys, importlib
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    G3 = importlib.import_module("build_rails_G3_ru")
    G3.translate_line(pali_line)
Exposes: the twelve bases and their bare words (registered in G2.TERMS), ATTR (sa-/a-X-ka persons: «с глазом» /
«без глаза»), the -āvacara planes (G2.PL_ACC / PL_LOC / PL_ABL / BEINGS), place lists («Среди … и в …»),
unlabeled questions, abbreviated (…pe…) fragments, the mūlaka labels and the editorial notes.
Run as a script (python -I -X utf8 -B build_rails_G3_ru.py) to write 3-01 … 3-06 and run the per-line checks;
`--probe <ch> …` prints the sentences without a formula (writes nothing).

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
"""
import importlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

G2 = importlib.import_module("build_rails_G2_ru")
G8 = importlib.import_module("build_rails_G8_ru")   # moment phrases: none occur in the Āyatanayamaka

ROOT, PALI, OUT = S.ROOT, S.PALI, S.OUT
CHAPTERS = [f"3-0{i}-ayatanayamaka.md" for i in range(1, 7)]
cap = S.cap
TERMS = G2.TERMS
SLIPS = G2.SLIPS
_CUR = G2._CUR


def slip(note):
    G2.slip(note)


def lowfirst(s):
    return s[:1].lower() + s[1:]


# =========================================================================== terms (termbase)
BASES = [  # Pāli stem, Russian genitive complement (termbase X-āyatanaṃ = «сфера …»)
    ("cakkhāyatana", "глаза"), ("sotāyatana", "уха"), ("ghānāyatana", "носа"), ("jivhāyatana", "языка"),
    ("kāyāyatana", "тела"), ("rūpāyatana", "видимых форм"), ("saddāyatana", "звуков"),
    ("gandhāyatana", "запахов"), ("rasāyatana", "вкусов"), ("phoṭṭhabbāyatana", "осязаемого"),
    ("manāyatana", "ума"), ("dhammāyatana", "объектов ума"),
]
for _st, _g in BASES:
    G2.register_term(_st + "ṃ", f"сфера {_g}", f"сферы {_g}", f"сферой {_g}", "f", acc=f"сферу {_g}",
                     forms=[_st + "ñca", _st + "ñceva"])
# sotāyananti (^6-3-13): spelling slip for sotāyatananti, rendered as meant (termbase entry sotāyananti)
G2.FORMS["sotāyanaṃ"] = "sotāyatanaṃ"
G2.SPELL_SLIPS["sotāyananti"] = "spelling slip for sotāyatananti, rendered as meant (termbase entry)"

# the bare words of the term-analysis questions (termbase: cakkhu глаз, sotaṃ ухо, ghānaṃ нос, jivhā язык,
# kāyo тело, saddo звук, gandho запах, raso вкус, phoṭṭhabbo осязаемое, mano ум; rūpaṃ «форма» is G2's;
# dhammo has no entry: «явление», the sense of dhammā «явления» (style sheet dhamma = явление); āyatana сфера восприятия)
BARE = [  # key, nom, gen, ins, g, other Pāli forms
    ("cakkhu", "глаз", "глаза", "глазом", "m", ["cakkhū", "cakkhuṃ", "cakkhuñca", "cakkhuñceva"]),
    ("sotaṃ", "ухо", "уха", "ухом", "n", ["sotañca", "sotañceva"]),
    ("ghānaṃ", "нос", "носа", "носом", "m", ["ghānañca", "ghānañceva"]),
    ("jivhā", "язык", "языка", "языком", "m", ["jivhaṃ", "jivhañca", "jivhañceva"]),
    ("kāyo", "тело", "тела", "телом", "n", ["kāyaṃ", "kāyañca", "kāyañceva"]),
    ("saddo", "звук", "звука", "звуком", "m", ["saddaṃ", "saddañca", "saddañceva"]),
    ("gandho", "запах", "запаха", "запахом", "m", ["gandhaṃ", "gandhañca", "gandhañceva"]),
    ("raso", "вкус", "вкуса", "вкусом", "m", ["rasaṃ", "rasañca", "rasañceva"]),
    ("phoṭṭhabbo", "осязаемое", "осязаемого", "осязаемым", "n", ["phoṭṭhabbaṃ", "phoṭṭhabbañca", "phoṭṭhabbañceva"]),
    ("mano", "ум", "ума", "умом", "m", ["manaṃ", "manañca", "manañceva"]),
    ("dhammo", "явление", "явления", "явлением", "n", ["dhammaṃ", "dhammañca", "dhammañceva"]),
    ("āyatanaṃ", "сфера восприятия", "сферы восприятия", "сферой восприятия", "f",
     ["āyatanañca", "āyatanañceva"]),
    ("āyatanā", "сферы восприятия", "сфер восприятия", "сферами восприятия", "pl", []),
]
for _k, _n, _gen, _ins, _g, _f in BARE:
    G2.register_term(_k, _n, _gen, _ins, _g, acc=("сферу восприятия" if _k == "āyatanaṃ" else None), forms=_f)
BARE_KEYS = [b[0] for b in BARE[:-2]] + ["rūpaṃ"]
# jivha ṭhapetvā: termbase entry «jivha» = the source spelling for jivhaṃ, rendered as meant
G2.FORMS["jivha"] = "jivhā"
G2.SPELL_SLIPS["jivha"] = "spelling slip jivha for jivhaṃ, rendered as meant (termbase entry)"

# =========================================================================== persons and planes
# sa-/a-X-kānaṃ (termbase Sacakkhukānaṃ «с глазом», acakkhukānaṃ «без глаза», sasotakānaṃ «с ухом», asotakānaṃ
# «без уха», arūpakānaṃ «без видимой формы», Sacittakānaṃ «с умом», Acittakānaṃ «без ума»; saghānaka- /
# aghānaka- / sarūpaka- have no entry: built from sa- / a- + ghāna «нос», rūpa «видимая форма» as their siblings)
ATTR = {
    "sacakkhukānaṃ": "с глазом", "acakkhukānaṃ": "без глаза",
    "sasotakānaṃ": "с ухом", "asotakānaṃ": "без уха",
    "saghānakānaṃ": "с носом", "aghānakānaṃ": "без носа",
    "sarūpakānaṃ": "с видимой формой", "arūpakānaṃ": "без видимой формы",
    "sacittakānaṃ": "с умом", "acittakānaṃ": "без ума",
}
# -āvacara planes (termbase Kāmāvacare / Rūpāvacare / arūpāvacare «мир чувственных желаний / форм / без форм»,
# kāmāvacaraṃ …, Kāmāvacarā / Rūpāvacarā …, Kāmāvacarānaṃ «существа мира чувственных желаний» …)
for _p, _ru in (("kāmāvacar", "мире чувственных желаний"), ("rūpāvacar", "мире форм"),
                ("arūpāvacar", "мире без форм")):
    G2.PL_ACC[_p + "aṃ"] = f"в {_ru}"
    G2.PL_LOC[_p + "e"] = f"в {_ru}"
    G2.PL_ABL[_p + "ā"] = f"в {_ru}"
G2.BEINGS["kāmāvacarānaṃ"] = "существ мира чувственных желаний"
G2.BEINGS["rūpāvacarānaṃ"] = "существ мира форм"
G2.BEINGS["arūpāvacarānaṃ"] = "существ мира без форм"


def _attrs(s):
    """'sacakkhukānaṃ asotakānaṃ' -> «с глазом и без уха»"""
    ws = [ATTR[w] for w in s.split()]
    return ws[0] if len(ws) == 1 else ", ".join(ws[:-1]) + " и " + ws[-1]


def _opt(s, table):
    return (" " + G2._places(s.strip(), table)) if s and s.strip() else ""


def _g3_rules():
    A, L, B, T = G2._alt(G2.PL_ACC), G2._alt(G2.PL_LOC), G2._alt(G2.PL_ABL), G2._alt(ATTR)
    RB, DI, LR, LL = G2.REBORN, G2.DIES, G2.LAST_REBORN, G2.LAST_LIFE
    PN, PF, RA = G2.PARINIB, G2.PARINIB_FUT, G2.REBORN_ABS
    return [  # same shapes as G2, with sa-/a-X-ka persons and several planes in one group
        (rf"itaresaṃ ((?:{T} )+)((?:{A} )*)upapajjantānaṃ",
         lambda m: (f"у остальных, кто {RB} {_attrs(m.group(1))}{_opt(m.group(2), G2.PL_ACC)}", True)),
        (rf"itaresaṃ ((?:{T} )+)((?:{B} )*)cavantānaṃ",
         lambda m: (f"у остальных, кто {DI} {_attrs(m.group(1))}{_opt(m.group(2), G2.PL_ABL)}", True)),
        (rf"((?:{T} )+)((?:{A} )*)upapajjantānaṃ",
         lambda m: (f"у тех, кто {RB} {_attrs(m.group(1))}{_opt(m.group(2), G2.PL_ACC)}", True)),
        (rf"((?:{T} )+)((?:{B} )*)cavantānaṃ",
         lambda m: (f"у тех, кто {DI} {_attrs(m.group(1))}{_opt(m.group(2), G2.PL_ABL)}", True)),
        (rf"((?:{L} )+)parinibb[aā]ntānaṃ",
         lambda m: (_parinib_slip(m) + f"у тех, кто {PN} {G2._places(m.group(1).strip(), G2.PL_LOC)}", True)),
        (rf"((?:{L} )+)pacchimabhavikānaṃ",
         lambda m: (f"у тех, кто {LL} {G2._places(m.group(1).strip(), G2.PL_LOC)}", True)),
    ] + _ye_rules(A, RA, PF)


def _ye_rules(A, RA, PF):
    """ye (ca) X-aṃ (Y-aṃ) upapajjitvā parinibbāyissanti (tesaṃ cavantānaṃ / upapajjantānaṃ), several planes allowed;
    G2: «у тех (умирающих), кто, переродившись в X, достигнет окончательного угасания»."""
    who = {"cavantānaṃ": "у тех умирающих", "upapajjantānaṃ": "у тех перерождающихся"}
    return [
        (rf"ye(?: ca)? ((?:{A} )+)upapajjitvā parinibbāyissanti tesaṃ (cavantānaṃ|upapajjantānaṃ)",
         lambda m: (f"{who[m.group(2)]}, кто, {RA} {G2._places(m.group(1).strip(), G2.PL_ACC)}, {PF}", True)),
        (rf"ye(?: ca)? ((?:{A} )+)upapajjitvā parinibbāyissanti",
         lambda m: (f"у тех, кто, {RA} {G2._places(m.group(1).strip(), G2.PL_ACC)}, {PF}", True)),
    ]


def _parinib_slip(m):
    if "parinibbāntānaṃ" in m.group(0):
        slip("parinibbāntānaṃ: spelling slip for parinibbantānaṃ, rendered as meant (termbase entry)")
    return ""


G2.GROUP_RULES = None
G2.intro_groups("")                      # builds G2's rules from the extended tables
G2.GROUP_RULES[:0] = _g3_rules()         # G3 shapes first (they only match sa-/a-X-ka or several planes)

# =========================================================================== paṇṇatti additions
# subjects of the term-analysis answers (lower-case Pāli -> Russian, number); figurative senses from the termbase
G2.SUBJ.update({
    "dibbacakkhu paññācakkhu": ("Божественный глаз, глаз мудрости", "sg"),
    "dibbasotaṃ taṇhāsotaṃ": ("Божественное ухо, поток жажды", "sg"),
    "sīlagandho samādhigandho paññāgandho": ("Запах нравственности, запах сосредоточения, запах мудрости", "sg"),
    "attharaso dhammaraso vimuttiraso": ("Вкус смысла, вкус Учения, вкус освобождения", "sg"),
    "avasesā āyatanā": ("Остальные сферы восприятия", "pl"),
})
REST_SG = "остальное"   # avaseso / avasesaṃ (termbase «остальной»), the generic «the rest» (sg.)


def _subj_rest():
    for st, _ in BASES:   # «Kāyāyatanaṃ ṭhapetvā avaseso / avasesaṃ» = «Кроме сферы тела, остальное»
        for rest in ("avaseso", "avasesaṃ"):
            G2.SUBJ[f"{st}ṃ ṭhapetvā {rest}"] = (f"{G2.EXCEPT} {TERMS[st + 'ṃ']['gen']}, {REST_SG}", "sg")
    for k in BARE_KEYS:   # «Cakkhuṃ ṭhapetvā avasesā āyatanā» = «Кроме глаза, остальные сферы восприятия»
        for f in [x for x, v in G2.FORMS.items() if v == k and not x.endswith(("ñca", "ñceva"))]:
            G2.SUBJ[f"{f} ṭhapetvā avasesā āyatanā"] = (f"{G2.EXCEPT} {TERMS[k]['gen']}, остальные сферы восприятия", "pl")


_subj_rest()
def unfuse(s):
    """«nāyatanā / nāyatanaṃ / nāyatananti» = na + āyatana- (termbase nāyatanā «не … сферы восприятия»)."""
    return re.sub(r"(?<!\S)([Nn])āyatan", lambda m: ("Na" if m.group(1) == "N" else "na") + " āyatan", s)


def glue_ca(s):
    """«cakkhāyatanañca uppajjati» -> «cakkhāyatanaṃ ca uppajjati» (G2's pair / partial parsers take a separate «ca»)."""
    return re.sub(r"(\w+?)ñca (?=(?:na )?n?(?:uppajj|nirujjh))",
                  lambda m: (m.group(1) + "ṃ ca ") if G2.term(m.group(1) + "ṃ") else m.group(0), s)


G2.FORMS["manāyatana"] = "manāyatanaṃ"   # termbase manāyatana: stem form before an abbreviation (^6-3-186)
# ^6-3-212 «no ca tesaṃ ghānāyatanaṃ upapajjissati»: upapajjati for uppajjati, a one-letter slip that makes another
# real word, stays as written (brief): upapajjissati «переродится» (termbase upapajjantānaṃ «перерождаться»)
G2.VERB["upapajjissati"] = {"sg": "переродится", "pl": "переродятся"}

G2.HEAD.update({k.lower(): v for k, v in {   # termbase headings
    "Suddhāyatanavāro": "раздел о сферах восприятия как таковых",
    "Suddhāyatanamūlacakkavāro": "круговой раздел на основе сфер восприятия как таковых",
}.items()})


def _strip_label(r):
    return re.sub(r"^\([а-я]\) ", "", r)


def pn_question(s):
    """Labeled or unlabeled naming question, with «nāyatanā» unfused: «(б) То, что не является сферами восприятия,
    не является сферой уха?»; unlabeled «Глаз является сферой глаза?»"""
    if not s.endswith(("?", ".")):
        return None
    m = re.match(r"^(\([^)]+\) )?(.+)$", s)
    if m.group(1):
        if "nāyatan" not in s:
            return None
        return G2.pn_question_line(m.group(1) + unfuse(m.group(2)))
    if not s.endswith("?"):
        return None
    r = G2.pn_question_line("(Ka) " + lowfirst(unfuse(m.group(2))))
    return cap(_strip_label(r)) if r else None


def pv_question(s):
    """Unlabeled pavatti question: «Yassa X V tassa Y V?» = «У кого V X, у того V Y?» (as the labeled frame)."""
    if not re.match(r"^(Yassa|Yattha) ", s):
        return None
    lab = "(Kha)" if s.startswith(("Yassa vā pana", "Yattha vā pana")) else "(Ka)"
    r = G2.pv_question_line(f"{lab} {lowfirst(s)}")
    return cap(_strip_label(r)) if r else None


def both_answer(s):
    """«Cakkhāyatanaṃ cakkhu ceva cakkhāyatanañca.» / «Sotāyatanaṃ sotañceva sotāyatanañca.»
    = «Сфера глаза и является глазом, и является сферой глаза.» (G2 «A и является B, и является C.»)"""
    toks = s[:-1].split() if s.endswith(".") else None
    if not toks:
        return None
    if len(toks) == 4 and toks[2] == "ceva":
        a, b, c = toks[0], toks[1], toks[3]
    elif len(toks) == 3 and toks[1].endswith("ñceva"):
        a, b, c = toks
    else:
        return None
    if not c.endswith("ñca"):
        return None
    ka, kb, kc = G2.term(a), G2.term(b), G2.term(c)
    if not (ka and kb and kc):
        return None
    cp = G2.COP[G2.num(ka)]
    return f"{cap(TERMS[ka]['nom'])} и {cp} {TERMS[kb]['ins']}, и {cp} {TERMS[kc]['ins']}."


def neither_sg(s):
    """«Kāyañca kāyāyatanañca ṭhapetvā avasesaṃ na ceva kāyo na ca kāyāyatanaṃ.»
    = «Кроме тела и сферы тела, остальное не является ни телом, ни сферой тела.»"""
    m = re.match(r"^(\S+) (\S+) ṭhapetvā (?:avasesaṃ|avaseso) na ceva (\S+) na ca (\S+)\.$", s)
    if not m:
        return None
    ks = [G2.term(x) for x in m.groups()]
    if not all(ks) or not all(x.lower().endswith("ñca") for x in m.groups()[:2]):
        return None
    x, y, b, c = ks
    return (f"{G2.EXCEPT} {TERMS[x]['gen']} и {TERMS[y]['gen']}, {REST_SG} не является ни {TERMS[b]['ins']}, "
            f"ни {TERMS[c]['ins']}.")


def place_answer(s):
    """Several places before «tattha»: «Asaññasatte arūpe tattha …» = «Среди существ без восприятия и в мире без форм …»
    (one place: G2.place_answer; the resumptive «tattha» is not rendered, «no ca tattha» = «но там»)."""
    m = re.match(rf"^((?:{G2._alt(G2.PL_LOC)} )+)tattha (.+)\.$", s, re.I)
    if not m:
        return None
    place = cap(G2._places(m.group(1).strip().lower(), G2.PL_LOC))
    toks = m.group(2).split()
    p = G2.parse_partial(toks, place=True)
    if p:
        x, v1, y, v2, t2 = p
        return f"{place} {G2.partial(x, v1, y, v2, t2, who=None)}."
    p = G2.parse_pair(toks)
    if p:
        x, v1, y, v2, c1, c2 = p
        return f"{place} {G2.pair(x, v1, y, v2, c1, c2)}."
    return None


MULAKA = "на основе"   # Cakkhāyatanamūlakaṃ «на основе сферы глаза» (termbase)


def mulaka(s):
    """«(Cakkhāyatanamūlakaṃ)» = «(На основе сферы глаза)»; a full stop after it stays as written."""
    m = re.match(r"^\((\w+?)mūlakaṃ\)(\.?)$", s)
    if not m:
        return None
    k = G2.term(m.group(1) + "ṃ")
    if not k:
        return None
    return f"({cap(MULAKA)} {TERMS[k]['gen']}){m.group(2)}"


G3_RULES = [mulaka, pn_question, pv_question, both_answer, neither_sg, place_answer]


NOTES = {}   # exact Pāli sentence or trailing parenthesis -> Russian (editorial notes; filled below)

# --------------------------------------------------------------------------- abbreviated pavatti questions
SEP2 = re.compile(r"\s?(…(?:pe|Pe)…\.?|…\.?)")
MARK = "\x00"
REL_RX = re.compile(r"^(?P<lab>\((?:Ka|Kha)\) )?(?P<rel>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|"
                    r"[Yy]assa|[Yy]attha vā pana|[Yy]attha)(?P<rest>(?:[ …].*)?)$")


def _items(text):
    """Clause body with «…» -> [None | (term key | None, (verb, neg) | None)], one per piece between the «…»."""
    groups = [[]]
    for tok in SEP2.sub(f" {MARK} ", text).split():
        if tok == MARK:
            groups.append([])
        else:
            groups[-1].append(tok)
    out = []
    for g in groups:
        if not g:
            out.append(None)
            continue
        k, i = G2.take_term(g, 0)
        v = None
        if i < len(g):
            tv = G2.take_verb(g, i, quoted=True)
            if not tv or tv[1] != len(g) or tv[2]:
                return None
            v = tv[0]
        if not (k or v):
            return None
        out.append((k, v))
    return out


def _clause_ru(items):
    """The clause verb goes before the first noun (Russian order, as the full frame «у того возникала X»); a noun
    with its own verb in the Pāli keeps it; nouns in a «…» list stand alone."""
    items = list(items)
    first = next((j for j, it in enumerate(items) if it and it[0]), None)
    if first is not None and items[first][1] is None:
        withv = [j for j, it in enumerate(items) if it and it[1] and it[0]]
        if withv:
            j = withv[-1]
            items[first] = (items[first][0], items[j][1])
            items[j] = (items[j][0], None)
    parts = []
    for it in items:
        if not it:
            parts.append("")
            continue
        k, v = it
        g = TERMS[k]["g"] if k else "f"
        w = [G2.vru(*v, g)] if v else []
        parts.append(" ".join(w + ([TERMS[k]["nom"]] if k else [])))
    s = parts[0]
    for p in parts[1:]:
        s += "…" + (" " + p if p else "")
    return s


def abbr_pv(s):
    """Pavatti question with «…pe…» lists or cut short: «Yassa X V tassa Y…pe… Z… W V-ti?»
    = «У кого V X, у того V Y… Z… W?»; «(Kha) yassa vā pana…pe… uppajjitthāti?» = «(б) А у кого… возникала?»"""
    m = REL_RX.match(s)
    if not m:
        return None
    rest, end = m.group("rest"), ""
    if rest.endswith("?"):
        rest, end = rest[:-1], "?"
    elif rest.endswith(".") and not SEP2.search(rest[-6:]):
        rest, end = rest[:-1], "."
    rel_p = m.group("rel")
    vapana = "vā pana" in rel_p
    rel = rel_p.lower().replace(" vā pana", "")
    cor = G2.QCOR[rel]
    parts = rest.split(f" {cor} ", 1)
    ia = _items(parts[0])
    ib = _items(parts[1]) if len(parts) == 2 else None
    if ia is None or (len(parts) == 2 and ib is None):
        return None
    a, b = G2.QREL[rel]
    lead = f"А {a}" if vapana else a
    if m.group("lab") or rel_p[:1].isupper():
        lead = cap(lead)
    ca = _clause_ru(ia)
    r = (S.LABEL[m.group("lab").strip()] + " " if m.group("lab") else "") + lead + ("" if ca.startswith("…") or not ca
                                                                                    else " ") + ca
    if ib is not None:
        cb = _clause_ru(ib)
        r += f", {b}" + ("" if cb.startswith("…") or not cb else " ") + cb
    _CUR["g"] = "f"
    return r + end


def intro_piece(p):
    """Answer pieces cut by «…pe…»: «INTRO (tesaṃ (tattha)) (X | X V, no ca tesaṃ (tattha))»."""
    m = re.match(r"^(?P<i>.+?)(?: tesaṃ(?P<t> tattha)?(?: (?P<x>.+))?)?$", p)
    gs = G2.intro_groups(m.group("i"))
    if not gs:
        return None
    if m.group("x") is None:                                   # «Rūpāvacarānaṃ…» / «… cavantānaṃ tesaṃ…»
        r = G2.join_groups(gs)
        if m.group("t"):
            return r + " там"
        return r.rstrip(",")
    there = " там" if m.group("t") else ""
    x = m.group("x")
    k, i = G2.take_term(x.split(), 0)
    if k and i == len(x.split()):                              # «… tesaṃ tattha manāyatanaṃ…»
        return f"{G2.join_groups(gs)}{there} {TERMS[k]['nom']}"
    mm = re.match(r"^(.+?), no ca tesaṃ( tattha)?$", x)       # «… X V, no ca tesaṃ tattha…»
    if mm:
        sv = G2.parse_sv(mm.group(1))
        if sv:
            X = TERMS[sv[0]]
            return (f"{G2.join_groups(gs)}{there} {G2.vru(*sv[1], X['g'])} {X['nom']}, но у них"
                    + (" там" if mm.group(2) else ""))
    return None


def _trailing_note(s):
    """'main (note)' / 'main (note).' with balanced brackets -> (main, '(note)', '.' or '') or None."""
    t = s[:-1] if s.endswith(".") else s
    if not t.endswith(")"):
        return None
    depth = 0
    for i in range(len(t) - 1, -1, -1):
        depth += {")": 1, "(": -1}.get(t[i], 0)
        if depth == 0:
            if i == 0 or t[i - 1] != " ":
                return None
            return t[:i - 1], t[i:], s[len(t):]
    return None


VAR_ANCHOR = {"avasesaṃ": "остальное"}   # Pāli word before a variant bracket -> its Russian rendering


def with_variant(s):
    """«… avasesaṃ [avasesā (syā. pī.)] …» -> the sentence without the bracket, the bracket placed after the
    Russian of its anchor word."""
    m = re.match(r"^(.*?(\S+)) \[([^\]]+?) \(([^)]+)\)\](.*)$", s)
    if not m or m.group(2) not in VAR_ANCHOR:
        return None
    r = core(m.group(1) + m.group(5))
    if not r:
        return None
    anchor = VAR_ANCHOR[m.group(2)]
    assert r.count(anchor) == 1, (r, anchor)
    return r.replace(anchor, f"{anchor} {G2.var_br(m.group(3), m.group(4))}")


def core(s):
    """One full Pāli sentence -> Russian, or None (G3 rules first, then G2's, then the abbreviated frames)."""
    if s in NOTES:
        return NOTES[s]
    m = _trailing_note(s)                                    # sentence + trailing editorial note
    if m and m[1] in NOTES:
        main = m[0]
        r = core(main) if not main.endswith(("?", ".")) else None
        if r is None:
            r = core(main + ".")
            r = r[:-1] if r else None
        if r is None and "…" in main:
            r = abbreviated(main)
        return f"{r} {NOTES[m[1]]}{m[2]}" if r else None
    if "[" in s:
        return with_variant(s)
    if s.endswith("…pe….") and len(s) > 6:                 # «…pe….» at the end = «…»
        r = core(s[:-len("…pe….")] + ".")
        if r:
            return r[:-1] + "…"
    s = glue_ca(s)
    for fn in G3_RULES:
        r = fn(s)
        if r:
            return r
    try:
        return G2.translate_sentence(s)
    except (ValueError, KeyError):
        pass
    return abbr_pv(s)


# =========================================================================== abbreviated (…pe…) sentences
SEP = re.compile(r"(…(?:pe|Pe)…\.?|…\.?)")


def fragment(p):
    """A piece between two «…» (no final punctuation of its own, or with it) -> Russian, or None."""
    for end in ("", "?", "."):
        if end and p.endswith(("?", ".")):
            break
        r = core(p + end)
        if r:
            return r[:-1] if end else r
    toks = p.split()
    k, i = G2.take_term(toks, 0)
    if k and i == len(toks):                               # a bare noun in a list: «сфера носа»
        return TERMS[k]["nom"]
    if len(toks) == 2 and toks[1] == "ṭhapetvā" and G2.term(toks[0]):   # «Sotaṃ ṭhapetvā» = «Кроме уха»
        return f"{G2.EXCEPT} {TERMS[G2.term(toks[0])]['gen']}"
    r = intro_piece(p.rstrip("."))
    if r:
        return r + ("." if p.endswith(".") else "")
    m = re.match(r"^na ca (\S+?)(\.?)$", p)        # tail of «… na ceva X na ca āyatanā.» = «… ни сферами восприятия.»
    if m and G2.term(m.group(1)):
        return f"ни {TERMS[G2.term(m.group(1))]['ins']}{m.group(2)}"
    m = re.match(r"^na (\S+?)(\.?)$", p)           # tail of «Avasesā āyatanā na X.» = «… не являются X.»
    if m and G2.term(m.group(1)) in [b[0] + "ṃ" for b in BASES]:
        return f"не {G2.COP['pl']} {TERMS[G2.term(m.group(1))]['ins']}{m.group(2)}"
    return None


def abbreviated(s):
    """Split at «…pe…» / «…» and translate every piece; «…pe…» = «…» glued to the word before it,
    a final «…pe….» / «….» = «…» (never «….»), the Pāli spacing kept."""
    parts = SEP.split(s)
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append("…")
            continue
        if not p.strip():
            out.append(p)
            continue
        lead = p[:len(p) - len(p.lstrip())]
        body = p.strip()
        r = fragment(body)
        if r is None:
            raise ValueError(f"no formula for piece {body!r} of {s!r} (segment {_CUR['id']})")
        r = cap(r) if body[:1].isupper() else lowfirst(r) if body[:1].islower() else r
        out.append(lead + r)
    return "".join(out)


def translate_sentence(s):
    s = s.strip()
    r = core(s)
    if r:
        return r
    if "…" in s:
        return abbreviated(s)
    raise ValueError(f"no formula for: {s!r} (segment {_CUR['id']})")


# =========================================================================== line translator
FIXED = {}
LINE_SLIPS = {  # plain spelling slips, rendered as meant (termbase entries)
    "uppajjittharūpāyatanañca": ("uppajjittha rūpāyatanañca", "uppajjittharūpāyatanañca: words run together in the "
                                 "source (termbase entry), rendered as two words"),
    " tasaṃ tattha ": (" tesaṃ tattha ", "tasaṃ: spelling slip for tesaṃ, rendered as meant"),
    "yassa =93 yattha": ("yassa yattha", "«=93» after yassa: a stray encoding mark (not Pāli), not rendered"),
    "nirujjhatī ti…": ("nirujjhatīti…", "«nirujjhatī ti»: -ti written apart (termbase nirujjhatī), rendered as meant"),
    "ghānāyatanaṃ upapajjissati.": ("ghānāyatanaṃ upapajjissati.", "«upapajjissati» (will be reborn) for "
                                    "uppajjissati: a one-letter slip that makes another word; kept as written "
                                    "(«переродится»)"),
}

# --------------------------------------------------------------------------- editorial notes (termbase words:
# yatthakaṃ / yatthakānaṃ «раздел(ы) с «где»», Yassakampi «раздел с «у кого»», Yassa yatthakampi «раздел с «у кого
# где»», yassakasadisaṃ «такой же как раздел с «у кого»», vārasaṅkhepo «разделы … сокращённо», pucchā «вопросы»,
# anulomampi / paccanīkampi «утвердительная / отрицательная форма», uppādepi / nirodhepi / uppādanirodhepi «раздел о
# возникновении / прекращении / возникновении и прекращении», paccuppannepi … «настоящее …»; Cakkaṃ «круг»)
UPP3 = "и в разделе о возникновении, и в разделе о прекращении, и в разделе о возникновении и прекращении"
ANUPAC = "и в утвердительной форме, и в отрицательной форме"
YATTHAKA = "раздел с «где»"
YASSAKA = "раздел с «у кого»"
YASSAYATTHAKA = "раздел с «у кого где»"
CAKKA = "(Круг следует замкнуть.)"   # (Cakkaṃ bandhitabbaṃ): «круг» (termbase Cakkaṃ); missing full stop added
NOTES.update({
    "(Cakkaṃ bandhitabbaṃ)": CAKKA,
    "(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena).":
        "(Круг на основе каждого отдельного слова следует замкнуть, не допуская путаницы.)",
    "(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ).": "(Замыкая круг, везде следует отвечать «Да».)",
    "(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana "
    "vārasaṅkhepo [uparivāre saṅkhepo (syā.), uparivāre saṅkhepaṃ (sī. ka.)] tīti jānitabbaṃ.)":
        "(Где возникает сфера носа, там сфера ума и сфера объектов ума одинаковы, различия нет, а далее разделы "
        "даны сокращённо [вариант чтения (Syā.): uparivāre saṅkhepo, (Sī., Ka.): uparivāre saṅkhepaṃ], так следует "
        "понимать.)",
    "(saṃkhittaṃ yassakasadisaṃ [yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)] )":
        f"(сокращено, такой же, как {YASSAKA} [вариант чтения (Sī.): yassakampi sadisaṃ, (Syā.): yassekasadisaṃ])",
    "(Saṃkhittaṃ).": "(Сокращено).",
    "(yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi paccuppannānāgatepi atītānāgatepi sabbattha "
    "sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ)":
        f"({YATTHAKA} и в настоящем, и в прошлом, и в будущем, и в настоящем и прошлом, и в настоящем и будущем, "
        "и в прошлом и будущем везде одинаков, названия «возникает», «возникала» следует добавить)",
    "(tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti)":
        "(у того сфера ума и сфера объектов ума одинаковы, эти две одинаковы)",
    "(uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ)": f"({YATTHAKA} {UPP3} везде одинаков)",
    "(Yassa yatthakampi sadisaṃ vitthāretabbaṃ).": f"({cap(YASSAYATTHAKA)} тоже следует подробно изложить так же.)",
    "(yassa yatthakampi yassakasadisaṃ)": f"({YASSAYATTHAKA} тоже такой же, как {YASSAKA})",
    "(Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi [paccaniyampi "
    "(sī. syā. ka.)] sadisaṃ.)":
        f"({cap(UPP3)} вопросы о прошлом одинаковы {ANUPAC} [вариант чтения (Sī., Syā., Ka.): paccaniyampi].)",
    "(Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi vitthāretabbā).":
        f"(Как в разделе о возникновении в разделе с «у кого где» подробно изложены вопросы о будущем, так их "
        "следует подробно изложить и в разделе о прекращении.)",
    "(yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ)":
        "(как и в разделе о настоящем и прошлом подробно изложено тремя способами, так следует подробно изложить "
        "и это)",
    "(yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu sadisaṃ)":
        f"(в разделе с «где» не следует отвечать «Нет», {YATTHAKA} следует изложить так же, как остальные разделы "
        f"с «где», {YATTHAKA} во всех трёх разделах одинаков)",
    "(Yassakampi yassayatthakampi sadisaṃ).": f"({cap(YASSAKA)} и {YASSAYATTHAKA} тоже одинаковы.)",
    "(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ).":
        f"(Вопросы о прошлом одинаковы {UPP3}, {ANUPAC}.)",
    "(Yathā uppādavāre paccuppannātītā pucchā vibhattā evaṃ uppādanirodhepi paccuppannātītā pucchā anulomampi "
    "paccanīkampi vibhajitabbā [vibhajitabbaṃ (sī syā. ka.)] ).":
        f"(Как в разделе о возникновении разобраны вопросы о настоящем и прошлом, так и в разделе о возникновении и "
        f"прекращении следует разобрать вопросы о настоящем и прошлом {ANUPAC} "
        "[вариант чтения (Sī., Syā., Ka.): vibhajitabbaṃ].)",
    "(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā yassakampi yatthakampi yassayatthakampi "
    "anulomampi paccanīkampi vibhattaṃ, evaṃ uppādanirodhepi atītānāgatā pucchā vibhajitabbā.)":
        f"(Как в разделе о прекращении разобраны вопросы о прошлом и будущем [вариант чтения (Syā.): atītenānāgatā] "
        f"и в разделе с «у кого», и в разделе с «где», и в разделе с «у кого где», {ANUPAC}, так и в разделе о "
        "возникновении и прекращении следует разобрать вопросы о прошлом и будущем.)",
    "Āyatanayamakaṃ niṭṭhitaṃ.": S.yamaka_done("Āyatanayamakaṃ"),
})


def _fixed():
    f = {"Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO}
    # ^6-3-1: the list (the missing comma after sotāyatanaṃ is rendered as meant)
    ks = [st + "ṃ" for st, _ in BASES]
    f["Dvādasāyatanāni – cakkhāyatanaṃ, sotāyatanaṃ ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, "
      "saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ."] = \
        "Двенадцать сфер восприятия – " + ", ".join(TERMS[k]["nom"] for k in ks) + "."
    return f


def _sent_fixed():
    # ^6-3-148: two answers joined by a comma in the Pāli (wrong punctuation stays as written)
    a = ("Rūpāvacarānaṃ arūpāvacarānaṃ tesaṃ tattha ghānāyatanaṃ na nirujjhissati, no ca tesaṃ tattha manāyatanaṃ "
         "na nirujjhissati")
    b = "parinibbantānaṃ asaññasattānaṃ tesaṃ tattha ghānāyatanañca na nirujjhissati manāyatanañca na nirujjhissati."
    NOTES[f"{a}, {b}"] = f"{core(a + '.')[:-1]}, {lowfirst(core(cap(b)))}"


LINE_SLIPS["na nirujjhissati, parinibbantānaṃ asaññasattānaṃ"] = (
    "na nirujjhissati, parinibbantānaṃ asaññasattānaṃ",
    "two answers joined by a comma where a full stop belongs; kept as written (one sentence)")


def split_sentences(pali):
    """Split after «.» / «?» + space, never inside [...] or (...)."""
    out, cur, depth = [], "", 0
    s = pali.strip()
    for i, ch in enumerate(s):
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        if ch == " " and depth == 0 and cur[-1:] in (".", "?"):
            out.append(cur)
            cur = ""
            continue
        cur += ch
    out.append(cur)
    return [x for x in out if x]


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian."""
    if pali.startswith("#"):
        return G2.heading(pali)
    if pali in FIXED:
        return FIXED[pali]
    for a, (b, note) in LINE_SLIPS.items():
        if a in pali:
            slip(note)
            pali = pali.replace(a, b)
    return " ".join(translate_sentence(x) for x in split_sentences(pali))


# =========================================================================== build + checks
def render(pali_text):
    blocks, problems = [], []
    for sid, plines in S.segs(pali_text):
        _CUR["id"] = sid
        ru = []
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            r = translate_line(body)
            # «? …Pe…» spaced so in the Pāli keeps its space («as the Pāli spaces it»): not an ellipsis error
            problems += [x for x in S.check_line(sid, body, r)
                         if not (": ellipsis:" in x and " …" in body and "…." not in r)]
            ru.append(r)
        ru[-1] = f"{ru[-1]} ^{sid}"
        blocks.append("\n".join(ru))
    return "\n\n".join(blocks) + "\n", problems


def probe(ch):
    bad = 0
    for sid, plines in S.segs((PALI / ch).read_text(encoding="utf-8")):
        _CUR["id"] = sid
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            if body.startswith("#") or body in FIXED:
                try:
                    translate_line(body)
                except (ValueError, KeyError) as e:
                    bad += 1
                    print(sid, "|", e)
                continue
            for a, (b, _) in LINE_SLIPS.items():
                body = body.replace(a, b)
            for x in split_sentences(body):
                try:
                    translate_sentence(x)
                except (ValueError, KeyError, AssertionError) as e:
                    bad += 1
                    print(sid, "|", x)
    print(ch, "sentences without a formula:", bad)


FIXED.update(_fixed())
_sent_fixed()


# =========================================================================== notes (new frames for later groups)
def notes_md():
    L = ["# notes-rails-G3: Āyatanayamaka (3-01 … 3-06) frames",
         "",
         "Format: Pāli = Russian, one per line. Builder: build_rails_G3_ru.py (importlib.import_module(\"build_rails_G3_ru\");",
         "importing writes nothing). Built on G2 (all G2 frames apply unchanged; see notes-rails-G2.md). G8 has nothing",
         "to add here: the Āyatanayamaka has no moment phrases. New here: the bases and their bare words, sa-/a-X-ka",
         "persons, the -āvacara planes, several places / planes in one group, unlabeled and abbreviated («…pe…»)",
         "questions, answer pieces cut by «…pe…», the mūlaka labels and the editorial notes.",
         "", "## Terms (termbase)", ""]
    L += [f"{st}ṃ = {TERMS[st + 'ṃ']['nom']} (acc. {TERMS[st + 'ṃ']['acc']}, gen. {TERMS[st + 'ṃ']['gen']}, "
          f"ins. {TERMS[st + 'ṃ']['ins']})" for st, _ in BASES]
    L += [f"{k} = {TERMS[k]['nom']} (ins. {TERMS[k]['ins']})" for k in BARE_KEYS + ["āyatanaṃ", "āyatanā"]]
    L += ["dhammo (no termbase entry) = явление, the sense of dhammā «явления»",
          "nāyatanā / nāyatanaṃ = na + āyatana-: «То, что не является сферами восприятия / сферой восприятия»",
          "avaseso / avasesaṃ (sg.) = остальное; avasesā = остальные (G2)"]
    L += [f"{k} = {v}" for k, v in ATTR.items()]
    L += ["kāmāvacaraṃ / -e / -ā = (в) мире чувственных желаний; rūpāvacara- = (в) мире форм; arūpāvacara- = (в) мире без форм;",
          "  -āvacarānaṃ = существ мира чувственных желаний / форм / без форм",
          "", "## Paṇṇatti", ""]
    ex = ["(Ka) cakkhu cakkhāyatanaṃ?", "(Kha) āyatanā sotāyatanaṃ?", "(Kha) nāyatanā na sotāyatanaṃ?",
          "(Ka) na cakkhu nāyatanaṃ?", "Cakkhu cakkhāyatananti?", "Nāyatanā na dhammāyatananti?",
          "Dibbacakkhu paññācakkhu cakkhu, na cakkhāyatanaṃ.", "Dibbasotaṃ taṇhāsotaṃ na sotāyatanaṃ, sotaṃ.",
          "Sīlagandho samādhigandho paññāgandho gandho, na gandhāyatanaṃ.",
          "Attharaso dhammaraso vimuttiraso raso, na rasāyatanaṃ.",
          "Cakkhāyatanaṃ cakkhu ceva cakkhāyatanañca.", "Sotāyatanaṃ sotañceva sotāyatanañca.",
          "Kāyāyatanaṃ ṭhapetvā avaseso kāyo, na kāyāyatanaṃ.", "Kāyāyatanaṃ ṭhapetvā avaseso na kāyāyatanaṃ, kāyo.",
          "Rūpañca rūpāyatanañca ṭhapetvā avasesaṃ na ceva rūpaṃ na ca rūpāyatanaṃ.",
          "Cakkhuñca cakkhāyatanañca ṭhapetvā avasesaṃ [avasesā (syā. pī.)] na ceva cakkhu na ca cakkhāyatanaṃ.",
          "Sotāyatanaṃ āyatanañceva sotāyatanañca.", "Avasesā āyatanā na sotāyatanaṃ.",
          "Cakkhuṃ ṭhapetvā avasesā āyatanā na cakkhu, āyatanā.",
          "Cakkhuñca āyatanañca ṭhapetvā avasesā na ceva cakkhu na ca āyatanā.",
          "Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe… na ca āyatanā.",
          "Āyatanā cakkhāyatananti?…Pe… na cakkhāyatanaṃ…pe….",
          "Āmantā.…Pe… ghānaṃ… jivhā… dhammo āyatananti?"]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["", "## Pavatti: persons, places, labels", ""]
    ex = ["Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhāyatanaṃ uppajjati, no ca tesaṃ sotāyatanaṃ uppajjati.",
          "Sacakkhukānaṃ sasotakānaṃ upapajjantānaṃ tesaṃ cakkhāyatanañca uppajjati sotāyatanañca uppajjati.",
          "Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhāyatanañca nuppajjati sotāyatanañca nuppajjati.",
          "Rūpāvacare tattha cakkhāyatanaṃ uppajjati, no ca tattha ghānāyatanaṃ uppajjati.",
          "Asaññasatte arūpe tattha dhammāyatanaṃ uppajjati, no ca tattha cakkhāyatanaṃ uppajjati.",
          "Rūpāvacarānaṃ tesaṃ tattha cakkhāyatanaṃ uppajjittha, no ca tesaṃ tattha ghānāyatanaṃ uppajjittha.",
          "Rūpāvacare arūpāvacare parinibbantānaṃ tesaṃ ghānāyatanañca na nirujjhati dhammāyatanañca na nirujjhissati.",
          "(Cakkhāyatanamūlakaṃ)", "(Rūpāyatanamūlakaṃ)."]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    for p in ["itaresaṃ sacakkhukānaṃ upapajjantānaṃ", "sacakkhukānaṃ cavantānaṃ",
              "itaresaṃ sacakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ",
              "kāmāvacaraṃ upapajjantānaṃ acakkhukānaṃ kāmāvacarā cavantānaṃ",
              "rūpāvacare arūpāvacare pacchimabhavikānaṃ",
              "pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
              "parinibbāyissanti tesaṃ upapajjantānaṃ",
              "ye rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ"]:
        L.append(f"{p} tesaṃ = {G2.intro(p)}")
    L += ["", "## Abbreviated (…pe…) questions and answers", "",
          "The clause verb goes before the first noun of a «…» list (Russian order); a noun with its own verb keeps it.",
          "«…pe…» / «…» = «…» glued to the word before; a final «…pe….» = «…»; the Pāli spacing after «?» / «.» is kept."]
    ex = ["Yassa cakkhāyatanaṃ uppajjittha tassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ… dhammāyatanaṃ uppajjitthāti?",
          "Yassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ uppajjittha tassa dhammāyatanaṃ uppajjitthāti?",
          "(Kha) yassa vā pana…pe… uppajjitthāti?", "(Kha) yassa vā pana yattha…pe…?",
          "(Kha) yassa vā pana ghānāyatanaṃ…pe….", "Yassa vā pana dhammāyatanaṃ…pe…?",
          "Rūpāvacarānaṃ…pe… kāmāvacarānaṃ…pe….",
          "Sabbesaṃ upapajjantānaṃ acakkhukānaṃ cavantānaṃ tesaṃ…pe… sacakkhukānaṃ cavantānaṃ tesaṃ…pe….",
          "Kāmāvacare parinibbantānaṃ tesaṃ tattha…pe…."]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["", "## Editorial notes and closing lines", ""]
    L += [f"{p} = {r}" for p, r in NOTES.items() if p.startswith("(")]
    L += ["Dvādasāyatanāni – cakkhāyatanaṃ, … = " + FIXED[[k for k in FIXED if k.startswith("Dvādas")][0]],
          f"Āyatanayamakaṃ niṭṭhitaṃ. = {NOTES['Āyatanayamakaṃ niṭṭhitaṃ.']}",
          "variant brackets with two readings: [X (syā.), Y (sī. ka.)] = [вариант чтения (Syā.): X, (Sī., Ka.): Y]"]
    return "\n".join(L) + "\n"


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        for ch in sys.argv[2:]:
            probe(ch)
        return
    problems = []
    for ch in CHAPTERS:
        pt = (PALI / ch).read_text(encoding="utf-8")
        ru, pr = render(pt)
        problems += pr
        e, n = S.check_file(pt, ru)
        problems += [f"{ch}: {x}" for x in e]
        (OUT / ch).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {ch}: {n} segments")
    slips = list(SLIPS)
    (S.RAILS / "notes-rails-G3.md").write_text(notes_md(), encoding="utf-8", newline="\n")
    print("wrote notes-rails-G3.md")
    for sid, note in dict.fromkeys(slips):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
