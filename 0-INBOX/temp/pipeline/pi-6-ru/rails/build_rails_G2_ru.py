"""pi-6 Yamaka, G2 (Khandhayamaka 2-01, 2-02): Russian RAILS builder and the frame-setter strings for the
paṇṇatti (naming), pavatti (arising / ceasing, every tense and the mixed tenses, person / place answers) and
pariññā (parijānāti) frames.

Later groups import it read-only; importing writes nothing:
    import sys, importlib
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    G2 = importlib.import_module("build_rails_G2_ru")
    G2.register_term("cakkhāyatanaṃ", nom="сфера глаза", gen="сферы глаза", ins="сферой глаза", g="f",
                     forms=["cakkhāyatanaṃ", "cakkhāyatanañca"])     # add your nouns
    G2.translate_line(pali_line)                                       # same frames, same strings
Extension points: TERMS / FORMS (register_term), VERB (verbs by gender), PL_ACC / PL_LOC / PL_ABL / BEINGS
(planes), GROUP_RULES (person groups before «tesaṃ»), PERSONS (pariññā subjects), SUBJ (paṇṇatti subjects),
FIXED (exact lines), HEAD (heading words).
Run as a script (python -I -X utf8 -B build_rails_G2_ru.py) to write 2-01 / 2-02 and run the per-line checks.
`--probe <ch>` prints the Pāli lines it has no formula for (writes nothing).

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
Sample strings: build_rails_sample_ru.py (S). User frames: ru-zeroshot-terms.md, zeroshot-coordinator-rules.md.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

ROOT = S.ROOT
PALI = S.PALI
OUT = S.OUT
CHAPTERS = ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md"]
cap = S.cap
SLIPS = []          # (segment id, note)
_CUR = {"id": None, "g": "f", "n": "sg"}   # current segment; gender / number of the last question's 2nd term


def slip(note):
    SLIPS.append((_CUR["id"], note))


# =========================================================================== terms
TERMS = {}   # key -> {"nom","acc","gen","ins","g"}  g: m / f / n / pl
FORMS = {}   # lower-case Pāli token -> key


def register_term(key, nom, gen, ins, g, acc=None, forms=()):
    """Register a noun: key is its Pāli nominative; forms are other Pāli tokens meaning the same noun
    (accusative, -ñca, -ñceva, -ti forms are derived automatically where regular)."""
    TERMS[key] = {"nom": nom, "acc": acc or nom, "gen": gen, "ins": ins, "g": g}
    for f in (key, *forms):
        FORMS[f.lower()] = key


def khandha(sub_gen, sub_key, stem):
    """X-kkhandho = «совокупность X» (termbase): nom = acc, gen «совокупности X», ins «совокупностью X»."""
    register_term(sub_key, f"совокупность {sub_gen}", f"совокупности {sub_gen}", f"совокупностью {sub_gen}", "f",
                  forms=[stem + "aṃ", stem + "añca"])


khandha("материальной формы", "rūpakkhandho", "rūpakkhandh")        # termbase rūpakkhandho
khandha("чувств", "vedanākkhandho", "vedanākkhandh")                # termbase vedanākkhandho
khandha("восприятия", "saññākkhandho", "saññākkhandh")              # termbase saññākkhandho
khandha("формирующих факторов", "saṅkhārakkhandho", "saṅkhārakkhandh")  # termbase saṅkhārakkhandho
khandha("сознания", "viññāṇakkhandho", "viññāṇakkhandh")            # termbase viññāṇakkhandho
FORMS["vadanākkhandho"] = "vedanākkhandho"   # source slip vadanā- (^6-2-185), rendered as meant (termbase)
SPELL_SLIPS = {"vadanākkhandho": "spelling slip for vedanākkhandho, rendered as meant (termbase entry)"}
# bare words of the term-analysis questions (termbase: rūpaṃ «форма» there, not «материальная форма»)
register_term("rūpaṃ", "форма", "формы", "формой", "f", forms=["rūpañca", "rūpañceva"])
register_term("vedanā", "чувство", "чувства", "чувством", "n", forms=["vedanaṃ", "vedanañca"])
register_term("saññā", "восприятие", "восприятия", "восприятием", "n", forms=["saññaṃ", "saññañca"])
register_term("saṅkhārā", "формирующие факторы", "формирующих факторов", "формирующими факторами", "pl",
              forms=["saṅkhāre"])
register_term("viññāṇaṃ", "сознание", "сознания", "сознанием", "n", forms=["viññāṇañca"])
register_term("khandho", "совокупность", "совокупности", "совокупностью", "f")
register_term("khandhā", "совокупности", "совокупностей", "совокупностями", "pl", forms=["khandhe"])


def term(tok, quoted=False):
    """Pāli token -> term key (None if unknown). quoted: strip the quotation -ti (…oti, …āti, …īti, …nti)."""
    t = tok.lower()
    if t in SPELL_SLIPS:
        slip(f"{t}: {SPELL_SLIPS[t]}")
    if t in FORMS:
        return FORMS[t]
    if quoted and t.endswith("ti"):
        b = t[:-2]
        for c in (b, b[:-1] + "ṃ" if b.endswith("n") else None, b[:-1] + "a" if b.endswith("ā") else None):
            if c and c in FORMS:
                return FORMS[c]
    return None


def T(key):
    return TERMS[key]


# =========================================================================== verbs (pavatti)
# termbase: uppajjati «возникать», uppajjittha «возникать», uppajjissati «возникнуть»; nirujjhati / nirujjhittha
# «прекращаться», nirujjhissati «прекратиться»; nuppajjati «не возникать» …  Past = imperfective by gender.
VERB = {
    "uppajjati": {"sg": "возникает", "pl": "возникают"},
    "uppajjittha": {"m": "возникал", "f": "возникала", "n": "возникало", "pl": "возникали"},
    "uppajjissati": {"sg": "возникнет", "pl": "возникнут"},
    "nirujjhati": {"sg": "прекращается", "pl": "прекращаются"},
    "nirujjhittha": {"m": "прекращался", "f": "прекращалась", "n": "прекращалось", "pl": "прекращались"},
    "nirujjhissati": {"sg": "прекратится", "pl": "прекратятся"},
}
NEG_FORM = {"nuppajjati": "uppajjati", "nuppajjittha": "uppajjittha", "nuppajjissati": "uppajjissati"}
VERB_SLIP = {"nirujjhattha": "nirujjhittha"}   # plain spelling slip (^6-2-111), rendered as meant


def vparse(s, quoted=False):
    """'na nirujjhati' / 'nuppajjatīti' -> (base, negated) or None."""
    s = s.strip()
    neg = False
    if s.startswith("na "):
        neg, s = True, s[3:]
    if quoted:
        for end, rep in (("īti", "i"), ("āti", "a")):
            if s.endswith(end):
                s = s[:-3] + rep
                break
    if s in VERB_SLIP:
        slip(f"{s} for {VERB_SLIP[s]}: spelling slip, rendered as meant")
        s = VERB_SLIP[s]
    if s in NEG_FORM:
        if neg:
            return None
        return NEG_FORM[s], True
    if s in VERB:
        return s, neg
    return None


def vform(base, g):
    d = VERB[base]
    if g in d:
        return d[g]
    return d["pl"] if g == "pl" else d["sg"]


def vru(base, neg, g):
    """Russian finite verb: «возникает» / «не возникала» …"""
    return ("не " if neg else "") + vform(base, g)


# =========================================================================== planes and persons
PL_ACC = {  # X-aṃ upapajjantānaṃ = «… кто перерождается в X» (termbase)
    "pañcavokāraṃ": "в существовании с пятью составляющими",
    "catuvokāraṃ": "в существовании с четырьмя составляющими",
    "arūpaṃ": "в мире без форм",
    "asaññasattaṃ": "среди существ без восприятия",
    "suddhāvāsaṃ": "в Чистых обителях",
}
PL_LOC = {  # X-e (place answers, «X-e parinibbantānaṃ / pacchimabhavikānaṃ»)
    "pañcavokāre": "в существовании с пятью составляющими",
    "catuvokāre": "в существовании с четырьмя составляющими",
    "arūpe": "в мире без форм",
    "asaññasatte": "среди существ без восприятия",
    "suddhāvāse": "в Чистых обителях",
}
PL_ABL = {  # X-ā cavantānaṃ = «… кто умирает в X»
    "pañcavokārā": "в существовании с пятью составляющими",
    "catuvokārā": "в существовании с четырьмя составляющими",
    "arūpā": "в мире без форм",
    "asaññasattā": "среди существ без восприятия",
    "suddhāvāsā": "в Чистых обителях",
}
BEINGS = {  # genitive plural beings
    "asaññasattānaṃ": "существ без восприятия",
    "pañcavokārānaṃ": "существ с пятью составляющими",
    "catuvokārānaṃ": "существ с четырьмя составляющими",
    "arūpānaṃ": "существ мира без форм",
    "suddhāvāsānaṃ": "существ Чистых обителей",
}
DIES = "умирает"                                   # cavantānaṃ «умирать» (termbase; pi-5 умирает)
REBORN = "перерождается"                           # upapajjantānaṃ «перерождаться»
LAST_REBORN = "в последний раз перерождается"      # pacchimabhavikānaṃ … upapajjantānaṃ (APPROVED)
LAST_LIFE = "живёт последней жизнью"               # pacchimabhavikānaṃ «жить последней жизнью»
PARINIB = "достигает окончательного угасания"      # parinibbantānaṃ (termbase; pi-5)
PARINIB_FUT = "достигнет окончательного угасания"  # parinibbāyissanti
REBORN_ABS = "переродившись"                       # upapajjitvā


def _alt(d):
    return "(?:" + "|".join(sorted(map(re.escape, d), key=len, reverse=True)) + ")"


def _places(s, table):
    """'catuvokāraṃ pañcavokāraṃ' -> «в существовании с четырьмя составляющими и в существовании с пятью …»"""
    ws = [table[w] for w in s.split()]
    return ws[0] if len(ws) == 1 else ", ".join(ws[:-1]) + " и " + ws[-1]


def _beings(s):
    ws = [BEINGS[w] for w in s.split()]
    return ws[0] if len(ws) == 1 else ", ".join(ws[:-1]) + " и " + ws[-1]


def _group_rules():
    A, L, B, G = _alt(PL_ACC), _alt(PL_LOC), _alt(PL_ABL), _alt(BEINGS)
    return [  # (regex at the start of the remaining intro, fn(match) -> (Russian «у …», has relative clause))
        (rf"sabbesaṃ cavantānaṃ", lambda m: (f"у всех, кто {DIES}", True)),
        (rf"sabbesaṃ upapajjantānaṃ", lambda m: (f"у всех, кто {REBORN}", True)),
        (rf"itaresaṃ ((?:{A} )+)upapajjantānaṃ",
         lambda m: (f"у остальных, кто {REBORN} {_places(m.group(1), PL_ACC)}", True)),
        (rf"itaresaṃ ((?:{B} )+)cavantānaṃ",
         lambda m: (f"у остальных, кто {DIES} {_places(m.group(1), PL_ABL)}", True)),
        (rf"itaresaṃ ((?:{G} ?)+)(?= |$)", lambda m: (f"у остальных {_beings(m.group(1).strip())}", False)),
        (rf"itaresaṃ", lambda m: ("у остальных", False)),
        (rf"pacchimabhavikānaṃ ((?:{A} )*)upapajjantānaṃ",
         lambda m: (f"у тех, кто {LAST_REBORN}" + (f" {_places(m.group(1), PL_ACC)}" if m.group(1) else ""), True)),
        (rf"((?:{A} )+)upapajjantānaṃ", lambda m: (f"у тех, кто {REBORN} {_places(m.group(1), PL_ACC)}", True)),
        (rf"((?:{B} )+)cavantānaṃ", lambda m: (f"у тех, кто {DIES} {_places(m.group(1), PL_ABL)}", True)),
        (rf"(?:({L}) )?parinibbantānaṃ",
         lambda m: (f"у тех, кто {PARINIB}" + (f" {PL_LOC[m.group(1)]}" if m.group(1) else ""), True)),
        (rf"(?:({L}) )?pacchimabhavikānaṃ",
         lambda m: (f"у тех, кто {LAST_LIFE}" + (f" {PL_LOC[m.group(1)]}" if m.group(1) else ""), True)),
        (rf"ye ca ({A}) upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ",
         lambda m: (f"у тех умирающих, кто, {REBORN_ABS} {PL_ACC[m.group(1)]}, {PARINIB_FUT}", True)),
        (rf"ye(?: ca)? ({A}) upapajjitvā parinibbāyissanti",
         lambda m: (f"у тех, кто, {REBORN_ABS} {PL_ACC[m.group(1)]}, {PARINIB_FUT}", True)),
        (rf"({G})", lambda m: (f"у {BEINGS[m.group(1)]}", False)),
    ]


GROUP_RULES = None   # built lazily so later groups can extend the tables first; or append to it after intro_groups()


def intro_groups(pali):
    """Pāli person intro (before the resumptive «tesaṃ») -> list of (Russian group, has relative clause)."""
    global GROUP_RULES
    if GROUP_RULES is None:
        GROUP_RULES = _group_rules()
    s, out = pali.strip().lower(), []
    while s:
        for rx, fn in GROUP_RULES:
            m = re.match(rx + r"(?= |$)", s)
            if m:
                out.append(fn(m))
                s = s[m.end():].strip()
                break
        else:
            return None
    return out


def join_groups(gs):
    """Groups joined in the Pāli order «A, B и C» (coordinator rule); a relative clause is closed by a comma;
    the resumptive «tesaṃ» is not rendered when a person is named («у них» only when none is: 5-01)."""
    s = ""
    for i, (g, rel) in enumerate(gs):
        if i == 0:
            s = g
        elif i == len(gs) - 1:
            s += ("," if gs[i - 1][1] else "") + " и " + g
        else:
            s += ", " + g
    if gs[-1][1]:
        s += ","
    return cap(s)


def intro(pali):
    gs = intro_groups(pali)
    return join_groups(gs) if gs else None


# =========================================================================== token helpers
def take_term(toks, i, quoted=False):
    """Longest run of 1-3 tokens from i that is a registered term -> (key, next index) or (None, i)."""
    for k in (3, 2, 1):
        if i + k <= len(toks):
            key = term(" ".join(toks[i:i + k]), quoted=quoted and i + k == len(toks))
            if key:
                return key, i + k
    return None, i


def take_verb(toks, i, quoted=False):
    """'na' + verb or verb; a comma glued to the verb is reported. -> ((base, neg), next, comma) or None."""
    for k in (2, 1):
        if i + k <= len(toks):
            w = " ".join(toks[i:i + k])
            comma = w.endswith(",")
            v = vparse(w.rstrip(","), quoted=quoted)
            if v:
                return v, i + k, comma
    return None


def g_of(key):
    return TERMS[key]["g"]


def num(key):
    return "pl" if g_of(key) == "pl" else "sg"


# =========================================================================== pavatti clauses
def flip(v, g):
    """The verb of «no ca …»: a denied negative is said plainly (coordinator rule), a denied positive gets «не»."""
    base, neg = v
    return vru(base, not neg, g)


def pair(x, v1, y, v2, c1=True, c2=True):
    """X ca V1 Y ca V2: «и V1 X, и V2 Y»; same negated verb: «не V ни X, ни Y» (coordinator rules);
    one «ca» missing in the Pāli: «V1 X и V2 Y» (as written)."""
    X, Y = TERMS[x], TERMS[y]
    if c1 and c2 and v1 == v2 and v1[1]:
        g = X["g"] if X["g"] == Y["g"] else "pl"
        return f"не {vform(v1[0], g)} ни {X['nom']}, ни {Y['nom']}"
    r1, r2 = vru(*v1, X["g"]), vru(*v2, Y["g"])
    if c1 and c2:
        return f"и {r1} {X['nom']}, и {r2} {Y['nom']}"
    return f"{r1} {X['nom']} и {r2} {Y['nom']}"


def partial(x, v1, y, v2, there2, who="у них"):
    """X V1, no ca tesaṃ (tattha) Y V2 -> «V1 X, но у них (там) V2' Y»; place answers: who=None -> «но там …»."""
    X, Y = TERMS[x], TERMS[y]
    head = "но" + (f" {who}" if who else "") + (" там" if there2 else "")
    return f"{vru(*v1, X['g'])} {X['nom']}, {head} {flip(v2, Y['g'])} {Y['nom']}"


def parse_partial(toks, place=False):
    """[X, V1(,), no, ca, (tesaṃ), (tattha), Y, V2] -> (x, v1, y, v2, there2) or None."""
    x, i = take_term(toks, 0)
    if not x:
        return None
    tv = take_verb(toks, i)
    if not tv or not tv[2]:
        return None
    v1, i, _ = tv
    if toks[i:i + 2] != ["no", "ca"]:
        return None
    i += 2
    if not place:
        if toks[i:i + 1] != ["tesaṃ"]:
            return None
        i += 1
    there2 = toks[i:i + 1] == ["tattha"]
    i += there2
    if place and not there2:
        return None
    y, i = take_term(toks, i)
    if not y:
        return None
    tv = take_verb(toks, i)
    if not tv or tv[1] != len(toks):
        return None
    return x, v1, y, tv[0], there2


def parse_pair(toks):
    """[X, (ca), V1, Y, (ca), V2] -> (x, v1, y, v2, c1, c2) or None; a stray comma after V1 is reported."""
    x, i = take_term(toks, 0)
    if not x:
        return None
    c1 = toks[i:i + 1] == ["ca"]
    i += c1
    tv = take_verb(toks, i)
    if not tv:
        return None
    v1, i, comma = tv
    y, i = take_term(toks, i)
    if not y:
        return None
    c2 = toks[i:i + 1] == ["ca"]
    i += c2
    tv = take_verb(toks, i)
    if not tv or tv[1] != len(toks):
        return None
    if not (c1 and c2) and not (c1 or c2):
        return None
    if comma:
        slip("stray comma between the two members of «X ca … Y ca …»; the Russian «и …, и …» has its comma anyway")
    if not (c1 and c2):
        slip("one «ca» of «X ca … Y ca …» missing; rendered as written with one «и»")
    return x, v1, y, tv[0], c1, c2


def person_answer(s):
    """INTRO tesaṃ (tattha) <partial | pair>."""
    body = s[:-1]
    for m in re.finditer(r" tesaṃ(?P<t> tattha)? ", body):
        gs = intro_groups(body[:m.start()])
        if not gs:
            continue
        toks = body[m.end():].split()
        there = " там" if m.group("t") else ""
        p = parse_partial(toks)
        if p:
            x, v1, y, v2, t2 = p
            return f"{join_groups(gs)}{there} {partial(x, v1, y, v2, t2)}."
        p = parse_pair(toks)
        if p:
            x, v1, y, v2, c1, c2 = p
            return f"{join_groups(gs)}{there} {pair(x, v1, y, v2, c1, c2)}."
    return None


def place_answer(s):
    """PLACE tattha <partial | pair>: the resumptive «tattha» after the named place is not rendered
    (as «tesaṃ» after a named person); «no ca tattha» = «но там»."""
    m = re.match(rf"^({_alt(PL_LOC)}) tattha (.+)\.$", s, re.I)
    if not m:
        return None
    place = cap(PL_LOC[m.group(1).lower()])
    toks = m.group(2).split()
    p = parse_partial(toks, place=True)
    if p:
        x, v1, y, v2, t2 = p
        return f"{place} {partial(x, v1, y, v2, t2, who=None)}."
    p = parse_pair(toks)
    if p:
        x, v1, y, v2, c1, c2 = p
        return f"{place} {pair(x, v1, y, v2, c1, c2)}."
    return None


# =========================================================================== pavatti questions
QREL = {"yassa": ("у кого", "у того"), "yattha": ("где", "там"), "yassa yattha": ("у кого где", "у того там")}
QCOR = {"yassa": "tassa", "yattha": "tattha", "yassa yattha": "tassa tattha"}


def pv_question(lab, rel, vapana, x, v1, y, v2, end="?"):
    """(Ka) yassa X V1 tassa Y V2? = (а) У кого V1 X, у того V2 Y?
    (Kha) yassa vā pana … = (б) А у кого …; yattha … tattha = где … там; yassa yattha … tassa tattha = у кого где … у того там."""
    a, b = QREL[rel]
    X, Y = TERMS[x], TERMS[y]
    _CUR["g"] = Y["g"]
    lead = f"А {a}" if vapana else cap(a)
    return f"{S.LABEL[lab]} {lead} {vru(*v1, X['g'])} {X['nom']}, {b} {vru(*v2, Y['g'])} {Y['nom']}{end}"


def parse_sv(s, quoted=False):
    """'rūpakkhandho uppajjati' -> (key, (base, neg))."""
    toks = s.split()
    k, i = take_term(toks, 0)
    if not k:
        return None
    tv = take_verb(toks, i, quoted=quoted)
    if not tv or tv[1] != len(toks) or tv[2]:
        return None
    return k, tv[0]


def pv_question_line(s):
    m = re.match(r"^\((?P<lab>[^)]+)\) (?P<rel>yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|"
                 r"yattha vā pana|yattha) (?P<body>.+?)(?P<end>[?.])$", s)
    if not m:
        return None
    vapana = "vā pana" in m.group("rel")
    rel = m.group("rel").replace(" vā pana", "")
    parts = m.group("body").split(f" {QCOR[rel]} ", 1)
    if len(parts) != 2:
        return None
    a, b = parse_sv(parts[0]), parse_sv(parts[1], quoted=True)
    if not (a and b):
        return None
    lab = f"({m.group('lab')})"
    if (lab == "(Ka)") == vapana:
        slip(f"label {lab} on a question {'with' if vapana else 'without'} «vā pana»; label kept as written")
    if m.group("end") == ".":
        slip("question ends with «.»; kept as written")
    return pv_question(lab, rel, vapana, a[0], a[1], b[0], b[1], m.group("end"))


def pv_fragment(s):
    """Yattha X V…pe…. = «Где V X…»; Yattha X V (yatthakaṃ paripuṇṇaṃ kātabbaṃ). = «Где V X (раздел с «где»
    следует изложить полностью).»"""
    m = re.match(r"^Yattha (.+?)(…pe…\.| \(yatthakaṃ paripuṇṇaṃ kātabbaṃ\)\.)$", s)
    if not m:
        return None
    a = parse_sv(m.group(1))
    if not a:
        return None
    X = TERMS[a[0]]
    tail = "…" if m.group(2).startswith("…") else f" ({YATTHAKA_FULL})."
    return f"Где {vru(*a[1], X['g'])} {X['nom']}{tail}"


YATTHAKA_FULL = "раздел с «где» следует изложить полностью"   # yatthakaṃ paripuṇṇaṃ kātabbaṃ (termbase yatthakaṃ)


def short_answer(s):
    """Āmantā. / No. / Natthi. / Uppajjati. (the verb of the question's 2nd term, said positively)."""
    if s == "Āmantā.":
        return S.YES
    if s == "No.":
        return NO
    if s == "Natthi.":
        return NATTHI
    m = re.match(r"^(\w+)\.$", s)
    if m:
        v = vparse(m.group(1).lower())
        if v and not v[1]:
            return cap(vform(v[0], _CUR["g"])) + "."
    return None


NO = "Нет."             # No.
NATTHI = "Такого нет."  # Natthi (termbase «такого нет»)


# =========================================================================== pariññā
TVERB = {  # transitive verbs with a person subject: Pāli -> ({sg, pl}, Pāli number)
    "parijānāti": ({"sg": "понимает", "pl": "понимают"}, "sg"),
    "parijānanti": ({"sg": "понимает", "pl": "понимают"}, "pl"),
    "parijānittha": ({"sg": "понял", "pl": "поняли"}, "sg"),
    "parijānissati": ({"sg": "поймёт", "pl": "поймут"}, "sg"),
    "parijānissanti": ({"sg": "поймёт", "pl": "поймут"}, "pl"),
}
TV_POS = "полностью {v}"   # parijānāti «полностью понимать» (termbase; pi-5 «полностью понимают»)
TV_NEG = "не {v} полностью"  # na parijānāti: «не понимает полностью» (never «полностью не …»)


def tparse(s, quoted=False):
    s = s.strip()
    neg = s.startswith("na ")
    if neg:
        s = s[3:]
    if quoted:
        for end, rep in (("īti", "i"), ("āti", "a")):
            if s.endswith(end):
                s = s[:-3] + rep
                break
    return (s, neg) if s in TVERB else None


def tru(v, n):
    forms, _ = TVERB[v[0]]
    return (TV_NEG if v[1] else TV_POS).format(v=forms[n])


def take_tverb(toks, i, quoted=False):
    for k in (2, 1):
        if i + k <= len(toks):
            w = " ".join(toks[i:i + k])
            comma = w.endswith(",")
            v = tparse(w.rstrip(","), quoted=quoted)
            if v:
                return v, i + k, comma
    return None


PERSONS = {  # pariññā subjects (lower-case Pāli) -> (Russian, number)
    "arahā": ("Архат", "sg"),                                       # termbase Arahā
    "aggamaggasamaṅgī": ("Обладающий высшим путём", "sg"),          # termbase Aggamaggasamaṅgī
    "aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā":
        ("Кроме обладающего высшим путём и архата, остальные личности", "pl"),
    "ye maggaṃ paṭilabhissanti te": ("Те, кто обретёт путь,", "pl"),
    "arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te":
        ("Архат и те обычные люди, которые не обретут путь,", "pl"),
    "aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te":
        ("Обладающий высшим путём и те обычные люди, которые не обретут путь,", "pl"),
}


def pr_question_line(s):
    """(Ka) yo X V1 so Y V2? = (а) Кто V1 X, тот V2 Y?  (Kha) yo vā pana … = (б) А кто …"""
    m = re.match(r"^\((?P<lab>[^)]+)\) yo(?P<vp> vā pana)? (?P<a>.+?) so (?P<b>.+?)(?P<end>[?.])$", s)
    if not m:
        return None
    ta, tb = m.group("a").split(), m.group("b").split()
    x, i = take_term(ta, 0)
    y, j = take_term(tb, 0)
    if not (x and y):
        return None
    va, vb = take_tverb(ta, i), take_tverb(tb, j, quoted=True)
    if not (va and vb) or va[1] != len(ta) or vb[1] != len(tb):
        return None
    lead = "А кто" if m.group("vp") else "Кто"
    return (f"{S.LABEL['(' + m.group('lab') + ')']} {lead} {tru(va[0], 'sg')} {TERMS[x]['acc']}, "
            f"тот {tru(vb[0], 'sg')} {TERMS[y]['acc']}{m.group('end')}")


def pr_answer(s):
    """P X V1, no ca Y V2. = «P V1 X, но V2' Y.»;  P Xñca V1 Yñca V2. = «P и V1 X, и V2 Y.»"""
    body = s[:-1]
    for pk in sorted(PERSONS, key=len, reverse=True):
        if body.lower().startswith(pk + " "):
            ru, n = PERSONS[pk]
            toks = body[len(pk) + 1:].split()
            break
    else:
        return None
    x, i = take_term(toks, 0)
    if not x:
        return None
    ca1 = toks[i - 1].lower().endswith("ñca")
    tv = take_tverb(toks, i)
    if not tv:
        return None
    v1, i, comma = tv
    for v in (v1,):
        if TVERB[v[0]][1] != n:
            slip(f"{v[0]}: Pāli number differs from the subject's; Russian agreement")
    if comma and toks[i:i + 2] == ["no", "ca"]:
        y, j = take_term(toks, i + 2)
        tv2 = take_tverb(toks, j) if y else None
        if not tv2 or tv2[1] != len(toks):
            return None
        v2 = tv2[0]
        return f"{ru} {tru(v1, n)} {TERMS[x]['acc']}, но {tru((v2[0], not v2[1]), n)} {TERMS[y]['acc']}."
    y, j = take_term(toks, i)
    if not (y and ca1 and toks[j - 1].lower().endswith("ñca")):
        return None
    tv2 = take_tverb(toks, j)
    if not tv2 or tv2[1] != len(toks):
        return None
    v2 = tv2[0]
    if TVERB[v2[0]][1] != n:
        slip(f"{v2[0]}: Pāli number differs from the subject's; Russian agreement")
    X, Y = TERMS[x]["acc"], TERMS[y]["acc"]
    if v1 == v2 and v1[1]:
        return f"{ru} {tru(v1, n)} ни {X}, ни {Y}."
    return f"{ru} и {tru(v1, n)} {X}, и {tru(v2, n)} {Y}."


# =========================================================================== paṇṇatti (naming)
COP = {"sg": "является", "pl": "являются"}   # «X является Y» (dash rule: never «X – Y»)
WHAT_NOT = "То, что не является"             # na X na Y? = «То, что не является X, не является Y?»
SUBJ = {  # paṇṇatti answer subjects (lower-case Pāli) -> (Russian, number)
    "piyarūpaṃ sātarūpaṃ": ("Привлекательная форма, отрадная форма", "sg"),  # piya / sāta as pi-2 («привлекательно и отрадно»)
    "diṭṭhisaññā": ("Восприятие-воззрение", "sg"),                            # termbase Diṭṭhisaññā
    "avasesā khandhā": ("Остальные совокупности", "pl"),                       # termbase Avasesā khandhā
}
REST = "остальные"   # avasesā (termbase «остальной»; pi-1)
EXCEPT = "Кроме"     # ṭhapetvā (termbase «кроме»)


def pn_subject(p):
    """'Saṅkhārakkhandhaṃ ṭhapetvā avasesā (khandhā)' -> («Кроме совокупности формирующих факторов, остальные (совокупности)», 'pl')."""
    k = p.lower()
    if k in SUBJ:
        return SUBJ[k]
    m = re.match(r"^(\S+) ṭhapetvā avasesā( khandhā)?$", k)
    if m and term(m.group(1)):
        return f"{EXCEPT} {TERMS[term(m.group(1))]['gen']}, {REST}" + (" совокупности" if m.group(2) else ""), "pl"
    return None


def pn_question_line(s):
    """(Ka) rūpaṃ rūpakkhandho? = (а) Форма является совокупностью материальной формы?
    (Ka) na rūpaṃ na rūpakkhandho? = (а) То, что не является формой, не является совокупностью материальной формы?"""
    m = re.match(r"^\((?P<lab>[^)]+)\) (?P<n1>na )?(?P<a>\S+) (?P<n2>na )?(?P<b>\S+?)(?P<end>[?.])$", s)
    if not m or bool(m.group("n1")) != bool(m.group("n2")):
        return None
    a, b = term(m.group("a")), term(m.group("b"), quoted=True)
    if not (a and b):
        return None
    if m.group("end") == ".":
        slip("question ends with «.»; kept as written")
    lab = S.LABEL[f"({m.group('lab')})"]
    if m.group("n1"):
        return f"{lab} {WHAT_NOT} {TERMS[a]['ins']}, не является {TERMS[b]['ins']}{m.group('end')}"
    return f"{lab} {cap(TERMS[a]['nom'])} {COP[num(a)]} {TERMS[b]['ins']}{m.group('end')}"


def pn_answer(s):
    # A ceva B ca: «X и является A, и является B.» (user rule: no relative clause -> subject + «и …, и …»)
    m = re.match(r"^(?P<a>\S+) (?P<b>\S+?)(?: ceva)? (?P<c>\S+) ca\.$", s)
    if m and all(term(m.group(k)) for k in "abc"):
        a, b, c = (term(m.group(k)) for k in "abc")
        cp = COP[num(a)]
        return f"{cap(TERMS[a]['nom'])} и {cp} {TERMS[b]['ins']}, и {cp} {TERMS[c]['ins']}."
    # X ca Y ca ṭhapetvā avasesā na ceva A na ca B: «Кроме X и Y, остальные не являются ни A, ни B.»
    m = re.match(r"^(?P<x>.+?) ṭhapetvā avasesā na ceva (?P<b>\S+) na ca (?P<c>\S+)\.$", s)
    if m:
        xs = [w[:-3] + "ṃ" if w.endswith("ñca") and not term(w) else w for w in m.group("x").split() if w != "ca"]
        ks = [term(w) for w in xs]
        b, c = term(m.group("b")), term(m.group("c"))
        if all(ks) and b and c:
            g = " и ".join(TERMS[k]["gen"] for k in ks)
            return f"{EXCEPT} {g}, {REST} не являются ни {TERMS[b]['ins']}, ни {TERMS[c]['ins']}."
    # S B, na C: «S является B, но не является C.»
    m = re.match(r"^(?P<s>.+?) (?P<b>\S+), na (?P<c>\S+)\.$", s)
    if m and pn_subject(m.group("s")) and term(m.group("b")) and term(m.group("c")):
        ru, n = pn_subject(m.group("s"))
        cp = COP[n]
        return f"{ru} {cp} {TERMS[term(m.group('b'))]['ins']}, но не {cp} {TERMS[term(m.group('c'))]['ins']}."
    # S na C, B: «S не является C, но является B.»
    m = re.match(r"^(?P<s>.+?) na (?P<c>\S+), (?P<b>\S+)\.$", s)
    if m and pn_subject(m.group("s")) and term(m.group("b")) and term(m.group("c")):
        ru, n = pn_subject(m.group("s"))
        cp = COP[n]
        return f"{ru} не {cp} {TERMS[term(m.group('c'))]['ins']}, но {cp} {TERMS[term(m.group('b'))]['ins']}."
    # S na C: «S не является C.»
    m = re.match(r"^(?P<s>.+?) na (?P<c>\S+)\.$", s)
    if m and pn_subject(m.group("s")) and term(m.group("c")):
        ru, n = pn_subject(m.group("s"))
        return f"{ru} не {COP[n]} {TERMS[term(m.group('c'))]['ins']}."
    return None


# =========================================================================== headings and colophons
HEAD = dict(S.HEAD)
HEAD.update({k.lower(): v for k, v in {   # ru-zeroshot-terms.md (user-approved headings) + termbase
    "Paṇṇattivāro": "раздел об обозначениях",
    "Padasodhanavāro": "раздел уточнения слов",
    "Padasodhanamūlacakkavāro": "круговой раздел на основе уточнения слов",
    "Suddhakhandhavāro": "раздел о совокупностях как таковых",
    "Suddhakhandhamūlacakkavāro": "круговой раздел на основе совокупностей как таковых",
    "Paṇṇattivāraniddesa": "разъяснение раздела об обозначениях",
    "anulomaṃ": "утвердительная форма", "paccanīkaṃ": "отрицательная форма",
    "anulomapuggalo": "утвердительная форма по личности",
    "anulomaokāso": "утвердительная форма по месту",
    "anulomapuggalokāsā": "утвердительная форма по личности и месту",
    "paccanīkapuggalo": "отрицательная форма по личности",
    "paccanīkaokāso": "отрицательная форма по месту",
    "paccanīkapuggalokāsā": "отрицательная форма по личности и месту",
    "Pavattivāro": "раздел о протекании", "Pavatti": "протекание",
    "uppādavāro": "раздел о возникновении", "nirodhavāro": "раздел о прекращении",
    "Uppādanirodhavāro": "раздел о возникновении и прекращении",
    "Paccuppannavāro": "раздел о настоящем", "Atītavāro": "раздел о прошлом", "Anāgatavāro": "раздел о будущем",
    "Paccuppannātītavāro": "раздел о настоящем и прошлом",
    "Paccuppannānāgatavāro": "раздел о настоящем и будущем",
    "Atītānāgatavāro": "раздел о прошлом и будущем",
    "Pariññāvāro": "раздел о полном понимании",
}.items()})
COLO = {k.lower(): cap(v) for k, v in {   # closing labels «<X>vāro.» / «<X>vāro niṭṭhito.»
    "Paṇṇattiuddesavāro": "раздел перечня обозначений",      # termbase
    "Paṇṇattiniddesavāro": "раздел разъяснения обозначений",  # termbase
    "Uppādavāro": "раздел о возникновении", "Nirodhavāro": "раздел о прекращении",
    "Uppādanirodhavāro": "раздел о возникновении и прекращении", "Pavattivāro": "раздел о протекании",
    "Pariññāvāro": "раздел о полном понимании",
}.items()}


def heading(text):
    """'#### Pavattivāro 1. uppādavāro' -> '#### Раздел о протекании 1. Раздел о возникновении'
    (labels from S.LABEL; numbers kept; first word after a label / number capitalised: coordinator rule)."""
    hashes, body = text.split(" ", 1)
    out = []
    for p in re.split(r"(\([^)]+\)|(?<!\S)\d+(?:-\d+)?\.(?=\s|$))", body):
        p = p.strip()
        if not p:
            continue
        if p in S.LABEL:
            out.append(S.LABEL[p])
        elif re.fullmatch(r"\(\d+\)|\d+(?:-\d+)?\.", p):
            out.append(p)
        else:
            out.append(cap(HEAD[p.lower()]))
    return f"{hashes} {' '.join(out)}"


def colophon(s):
    m = re.match(r"^(\S+?)(?: (niṭṭhito|niṭṭhitā|niṭṭhitaṃ))?\.$", s)
    if not m:
        return None
    k = m.group(1).lower()
    if k.endswith("yamakapāḷi") and m.group(2):
        for t in S.YAMAKA:
            if t.lower()[:-len("yamakaṃ")] == k[:-len("yamakapāḷi")]:
                return S.yamaka_done(t)
    if k in COLO:
        return COLO[k] + (f" {S.DONE}." if m.group(2) == "niṭṭhito" else ".")
    return None


# =========================================================================== variants and fixed lines
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "pī.": "Pī.", "kaṃ.": "Kaṃ.", "i.": "I.", "ma.": "Ma."}


def var_br(text, sig, kind="чтения", note=None):
    """[avesesā … (sī. syā.)] -> «[вариант чтения (Sī., Syā.): …]»; kind «написания» for spelling-only variants."""
    sigs = ", ".join(SIGLA[x] for x in sig.split())
    return f"[вариант {kind} ({sigs}): {text}" + (f"; {note}" if note else "") + "]"


EVAMUPARIPI = "так же и далее"   # evamuparipi (editorial note in a variant bracket)
FIXED = {}


def _fixed():
    f = {"Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO}
    ks = ["rūpakkhandho", "vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"]
    f["Pañcakkhandhā – " + ", ".join(ks) + "."] = "Пять совокупностей – " + ", ".join(TERMS[k]["nom"] for k in ks) + "."
    # ^6-2-26: variant after «saṅkhārā»
    a = translate_sentence("Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā, na saṅkhārakkhandho.")
    a = a.replace(", но не", f" {var_br('avasesā saṅkhārā saṅkhārā', 'syā.')}, но не", 1)
    b = translate_sentence("Saṅkhārakkhandho saṅkhārā ceva saṅkhārakkhandho ca.")
    f["Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā [avasesā saṅkhārā saṅkhārā (syā.)], na saṅkhārakkhandho. "
      "Saṅkhārakkhandho saṅkhārā ceva saṅkhārakkhandho ca."] = f"{a} {b}"
    # ^6-2-28: variant after «avasesā khandhā» with the editorial note evamuparipi
    a = translate_sentence("Avasesā khandhā na vedanākkhandho.")
    a = a.replace("Остальные совокупности", "Остальные совокупности "
                  + var_br("avasesā khandhā khandhā", "syā.", note=EVAMUPARIPI), 1)
    f["Avasesā khandhā [avasesā khandhā khandhā (syā.) evamuparipi] na vedanākkhandho."] = a
    # ^6-2-87: variant after the person group
    p = ("Pacchimabhavikānaṃ upapajjantānaṃ tesaṃ saññākkhandho nuppajjissati, no ca tesaṃ vedanākkhandho nuppajjati. "
         "Parinibbantānaṃ tesaṃ saññākkhandho ca nuppajjissati vedanākkhandho ca nuppajjati.")
    r = _translate_plain(p)
    anchor = f"{LAST_REBORN},"
    assert anchor in r
    r = r.replace(anchor, f"{LAST_REBORN} {var_br('pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ', 'sī. syā.')},", 1)
    f[p.replace("upapajjantānaṃ tesaṃ", "upapajjantānaṃ [pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ (sī. syā.)] "
                "tesaṃ", 1)] = r
    # ^6-2-185: abbreviation note
    f["(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ)."] = \
        "(Как в разделе о возникновении разобрано настоящее и прошлое, так и здесь следует разобрать.)"
    return f


# =========================================================================== line translator
SENTENCE_RULES = [short_answer, pv_question_line, pr_question_line, pn_question_line, pv_fragment,
                  person_answer, place_answer, pr_answer, pn_answer, colophon]


def translate_sentence(s):
    s = s.strip()
    if s.endswith("…pe….") and not s.startswith("Yattha "):
        return translate_sentence(s[:-len("…pe….")] + ".")[:-1] + "…"
    for fn in SENTENCE_RULES:
        r = fn(s)
        if r:
            return r
    raise ValueError(f"no formula for: {s!r} (segment {_CUR['id']})")


def _translate_plain(pali):
    return " ".join(translate_sentence(x) for x in re.split(r"(?<=[.?])\s+", pali.strip()))


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian, from the fixed formulas only."""
    global FIXED
    if not FIXED:
        FIXED = _fixed()
    if pali.startswith("#"):
        return heading(pali)
    if pali in FIXED:
        return FIXED[pali]
    return _translate_plain(pali)


# =========================================================================== build + checks
def render(pali_text):
    blocks, problems = [], []
    for sid, plines in S.segs(pali_text):
        _CUR["id"] = sid
        ru = []
        for i, pl in enumerate(plines):
            body = S.ID.sub("", pl) if i == len(plines) - 1 else pl
            r = translate_line(body.strip())
            problems += S.check_line(sid, body.strip(), r)
            ru.append(r)
        ru[-1] = f"{ru[-1]} ^{sid}"
        blocks.append("\n".join(ru))
    return "\n\n".join(blocks) + "\n", problems


# strings taken unchanged from approved earlier Russian rails (asserted in main)
PI5_STRINGS = ["существ без восприятия", "окончательного угасания", "обычные люди", "полностью понимают",
               "умирает", "перерождается", "Да."]
PI2_STRINGS = ["привлекательно и отрадно"]


def probe(ch):
    """Print the Pāli sentences of chapter ch with no formula (writes nothing)."""
    bad = 0
    for sid, plines in S.segs((PALI / ch).read_text(encoding="utf-8")):
        _CUR["id"] = sid
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            try:
                translate_line(body)
            except (ValueError, KeyError, AssertionError) as e:
                bad += 1
                print(sid, "|", e)
    print(ch, "lines without a formula:", bad)


# =========================================================================== notes (frames for later groups)
def notes_md():
    L = ["# notes-rails-G2: Khandhayamaka frames (paṇṇatti, pavatti, pariññā)", "",
         "Format: Pāli = Russian, one per line. Builder: build_rails_G2_ru.py (import with importlib; importing writes",
         "nothing). Later groups register their nouns with G2.register_term(...) and call G2.translate_line(...), or use",
         "the frame functions directly: pn_question_line, pn_answer, pv_question, partial, pair, person_answer,",
         "place_answer, intro, short_answer, pv_fragment, pr_question_line, pr_answer, heading, colophon, var_br.",
         "X / Y = any registered noun (nom / acc / gen / ins / gender); verbs agree with their noun.",
         "New planes / persons: add to PL_ACC / PL_LOC / PL_ABL / BEINGS, then set G2.GROUP_RULES = None (rebuilt on",
         "the next call); or append (regex, fn) pairs to G2.GROUP_RULES after G2.intro_groups('') has built it.",
         "New pariññā-type verbs: TVERB; new subjects: PERSONS (pariññā), SUBJ (paṇṇatti).", "",
         "## Paṇṇatti (naming) frames", ""]
    ex = [
        "(Ka) rūpaṃ rūpakkhandho?", "(Kha) rūpakkhandho rūpaṃ?", "(Ka) saṅkhārā saṅkhārakkhandho?",
        "(Kha) khandhā vedanākkhandho?", "(Ka) rūpaṃ khandho?", "(Kha) khandhā rūpaṃ?",
        "(Ka) na rūpaṃ na rūpakkhandho?", "(Kha) na khandhā na vedanākkhandho?", "(Ka) na saṅkhārā na khandho?",
        "(Ka) rūpaṃ rūpakkhandhoti?",
        "Piyarūpaṃ sātarūpaṃ rūpaṃ, na rūpakkhandho.", "Rūpakkhandho rūpañceva rūpakkhandho ca.",
        "Diṭṭhisaññā saññā, na saññākkhandho.", "Saññākkhandho saññā ceva saññākkhandho ca.",
        "Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā, na saṅkhārakkhandho.",
        "Piyarūpaṃ sātarūpaṃ na rūpakkhandho, rūpaṃ.",
        "Rūpañca rūpakkhandhañca ṭhapetvā avasesā na ceva rūpaṃ na ca rūpakkhandho.",
        "Saṅkhārakkhandhaṃ ṭhapetvā avasesā na saṅkhārakkhandho, saṅkhārā.",
        "Vedanākkhandho khandho ceva vedanākkhandho ca.", "Avasesā khandhā na vedanākkhandho.",
        "Rūpaṃ ṭhapetvā avasesā khandhā na rūpaṃ, khandhā.",
        "Rūpañca khandhe ca ṭhapetvā avasesā na ceva rūpaṃ na ca khandhā.",
    ]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["X Y? = X является Y? (Y instrumental; plural X: являются); na X na Y? = То, что не является X, не является Y?",
          "S B, na C. = S является B, но не является C.;  S na C, B. = S не является C, но является B.",
          "A B ceva C ca. = A и является B, и является C. (user rule: no relative clause -> «и …, и …» with the verb twice)",
          "X ṭhapetvā avasesā = Кроме X(gen), остальные (pl.);  X-ñca Y-ñca ṭhapetvā avasesā na ceva A na ca B = "
          "Кроме X и Y, остальные не являются ни A, ни B.",
          "piyarūpaṃ sātarūpaṃ = привлекательная форма, отрадная форма (piya / sāta as pi-2 «привлекательно и отрадно»; "
          "rūpa = форма: termbase bare-word sense)", "",
          "## Pavatti frames: questions", ""]
    ex = ["(Ka) yassa rūpakkhandho uppajjati tassa vedanākkhandho uppajjatīti?",
          "(Kha) yassa vā pana vedanākkhandho uppajjati tassa rūpakkhandho uppajjatīti?",
          "(Ka) yattha rūpakkhandho uppajjati tattha vedanākkhandho uppajjatīti?",
          "(Kha) yattha vā pana vedanākkhandho uppajjati tattha rūpakkhandho uppajjatīti?",
          "(Ka) yassa yattha rūpakkhandho uppajjati tassa tattha vedanākkhandho uppajjatīti?",
          "(Kha) yassa vā pana yattha vedanākkhandho uppajjati tassa tattha rūpakkhandho uppajjatīti?",
          "(Ka) yassa rūpakkhandho nuppajjati tassa vedanākkhandho nuppajjatīti?",
          "(Ka) yassa rūpakkhandho uppajjittha tassa vedanākkhandho uppajjitthāti?",
          "(Ka) yassa rūpakkhandho nuppajjittha tassa vedanākkhandho nuppajjitthāti?",
          "(Ka) yassa rūpakkhandho uppajjissati tassa vedanākkhandho uppajjissatīti?",
          "(Ka) yassa rūpakkhandho nuppajjissati tassa vedanākkhandho nuppajjissatīti?",
          "(Ka) yassa rūpakkhandho nirujjhati tassa vedanākkhandho nirujjhatīti?",
          "(Ka) yassa rūpakkhandho na nirujjhati tassa vedanākkhandho na nirujjhatīti?",
          "(Ka) yassa rūpakkhandho nirujjhittha tassa vedanākkhandho nirujjhitthāti?",
          "(Ka) yassa rūpakkhandho na nirujjhittha tassa vedanākkhandho na nirujjhitthāti?",
          "(Ka) yassa rūpakkhandho nirujjhissati tassa vedanākkhandho nirujjhissatīti?",
          "(Ka) yassa rūpakkhandho na nirujjhissati tassa vedanākkhandho na nirujjhissatīti?",
          "(Ka) yassa rūpakkhandho uppajjati tassa vedanākkhandho uppajjitthāti?",
          "(Ka) yassa rūpakkhandho uppajjati tassa vedanākkhandho uppajjissatīti?",
          "(Ka) yassa rūpakkhandho uppajjittha tassa vedanākkhandho uppajjissatīti?",
          "(Ka) yassa rūpakkhandho uppajjati tassa vedanākkhandho nirujjhatīti?",
          "(Ka) yassa rūpakkhandho nuppajjati tassa vedanākkhandho na nirujjhatīti?",
          "(Ka) yassa rūpakkhandho nuppajjittha tassa vedanākkhandho na nirujjhissatīti?"]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["verbs (termbase; by the gender of their noun): uppajjati возникает / возникают; uppajjittha возникал(а, о, и);",
          "  uppajjissati возникнет / возникнут; nirujjhati прекращается; nirujjhittha прекращался(ась, ось, ись);",
          "  nirujjhissati прекратится; nuppajjati / na nirujjhati … = не + the same form", "",
          "## Pavatti frames: answers", ""]
    ex = ["Āmantā.", "No.", "Natthi."]
    L += [f"{p} = {translate_sentence(p)}" for p in ex]
    L += ["Uppajjati. / Uppajjittha. / Uppajjissati. / Nirujjhati. / Nirujjhittha. / Nirujjhissati. = Возникает. / "
          "Возникала. / Возникнет. / Прекращается. / Прекращалась. / Прекратится. (gender of the question's 2nd noun)"]
    ex = ["Asaññasattaṃ upapajjantānaṃ tesaṃ rūpakkhandho uppajjati, no ca tesaṃ vedanākkhandho uppajjati.",
          "Pañcavokāraṃ upapajjantānaṃ tesaṃ rūpakkhandho ca uppajjati vedanākkhandho ca uppajjati.",
          "Arūpaṃ upapajjantānaṃ tesaṃ rūpakkhandho nuppajjati, no ca tesaṃ vedanākkhandho nuppajjati.",
          "Sabbesaṃ cavantānaṃ tesaṃ rūpakkhandho ca nuppajjati vedanākkhandho ca nuppajjati.",
          "Asaññasatte tattha rūpakkhandho uppajjati, no ca tattha vedanākkhandho uppajjati.",
          "Pañcavokāre tattha rūpakkhandho ca uppajjati vedanākkhandho ca uppajjati.",
          "Asaññasattaṃ upapajjantānaṃ tesaṃ tattha rūpakkhandho uppajjati, no ca tesaṃ tattha vedanākkhandho uppajjati.",
          "Asaññasattānaṃ tesaṃ tattha rūpakkhandho uppajjittha, no ca tesaṃ tattha vedanākkhandho uppajjittha.",
          "Suddhāvāsānaṃ tesaṃ tattha rūpakkhandho ca nuppajjittha vedanākkhandho ca nuppajjittha.",
          "Ye arūpaṃ upapajjitvā parinibbāyissanti tesaṃ vedanākkhandho uppajjissati, no ca tesaṃ rūpakkhandho uppajjissati.",
          "Itaresaṃ tesaṃ vedanākkhandho ca uppajjissati rūpakkhandho ca uppajjissati.",
          "Pacchimabhavikānaṃ tesaṃ rūpakkhandho ca nuppajjissati vedanākkhandho ca nuppajjissati.",
          "Sabbesaṃ cavantānaṃ arūpaṃ upapajjantānaṃ tesaṃ vedanākkhandho uppajjittha, no ca tesaṃ rūpakkhandho uppajjati.",
          "Itaresaṃ pañcavokāraṃ upapajjantānaṃ tesaṃ tattha rūpakkhandho ca uppajjati vedanākkhandho ca uppajjittha.",
          "Pañcavokārā cavantānaṃ arūpānaṃ tesaṃ tattha vedanākkhandho uppajjittha, no ca tesaṃ tattha rūpakkhandho uppajjati.",
          "Catuvokāraṃ pañcavokāraṃ upapajjantānaṃ tesaṃ saññākkhandho ca uppajjittha vedanākkhandho ca uppajjati.",
          "Suddhāvāse parinibbantānaṃ asaññasattā cavantānaṃ tesaṃ tattha rūpakkhandho ca nuppajjati vedanākkhandho ca nuppajjittha.",
          "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ tesaṃ rūpakkhandho uppajjati, no ca tesaṃ vedanākkhandho uppajjissati.",
          "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ asaññasattā cavantānaṃ tesaṃ tattha rūpakkhandho ca nuppajjati vedanākkhandho ca nuppajjissati.",
          "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha vedanākkhandho ca uppajjittha saññākkhandho ca uppajjissati.",
          "Pacchimabhavikānaṃ arūpaṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ vedanākkhandho nirujjhissati, no ca tesaṃ rūpakkhandho nirujjhissati.",
          "Catuvokārā pañcavokārā cavantānaṃ tesaṃ rūpakkhandho nuppajjati, no ca tesaṃ vedanākkhandho na nirujjhati.",
          "Arūpaṃ upapajjantānaṃ asaññasattā cavantānaṃ tesaṃ rūpakkhandho ca nuppajjati vedanākkhandho ca na nirujjhati."]
    L += [f"{p} = {translate_sentence(p)}" for p in ex]
    L += ["no ca tesaṃ (tattha) Y V = но у них (там) не V Y; no ca tesaṃ Y na V / nuppajjati = но у них V Y (coordinator)",
          "X ca V Y ca V (positive) = и V X, и V Y; X ca na V Y ca na V (same verb) = не V ни X, ни Y (coordinator);",
          "  different verbs / tenses: и V1 X, и V2 Y (each with its own «не» where negated)",
          "person intro + tesaṃ: the resumptive tesaṃ is not rendered; place + tattha: the resumptive tattha is not",
          "  rendered; tesaṃ tattha after a person intro = «… там»; several groups joined «A, B и C» (Pāli order)",
          "person groups: sabbesaṃ cavantānaṃ / upapajjantānaṃ = у всех, кто умирает / перерождается;",
          "  X-aṃ upapajjantānaṃ = у тех, кто перерождается в X; X-ā cavantānaṃ = у тех, кто умирает в X;",
          "  pacchimabhavikānaṃ (X-aṃ) upapajjantānaṃ = у тех, кто в последний раз перерождается (в X) (APPROVED);",
          "  (X-e) pacchimabhavikānaṃ = у тех, кто живёт последней жизнью (в X); (X-e) parinibbantānaṃ = у тех, кто",
          "  достигает окончательного угасания (в X); X-ānaṃ = у существ X; itaresaṃ = у остальных; itaresaṃ X-aṃ",
          "  upapajjantānaṃ = у остальных, кто перерождается в X (APPROVED); itaresaṃ X-ānaṃ = у остальных существ X;",
          "  ye X-aṃ upapajjitvā parinibbāyissanti = у тех, кто, переродившись в X, достигнет окончательного угасания;",
          "  ye ca X-aṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ = у тех умирающих, кто, переродившись в X, …",
          "planes (termbase): pañcavokāra в существовании с пятью составляющими / существ с пятью составляющими;",
          "  catuvokāra … с четырьмя составляющими; arūpa в мире без форм / существ мира без форм; asaññasatta",
          "  среди существ без восприятия / существ без восприятия; suddhāvāsa в Чистых обителях / существ Чистых обителей"]
    ex = ["Yattha rūpakkhandho nirujjhati…pe….", "Yattha rūpakkhandho na nirujjhati (yatthakaṃ paripuṇṇaṃ kātabbaṃ).",
          "(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ)."]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["", "## Pariññā frames", ""]
    ex = ["(Ka) yo rūpakkhandhaṃ parijānāti so vedanākkhandhaṃ parijānātīti?",
          "(Kha) yo vā pana vedanākkhandhaṃ parijānāti so rūpakkhandhaṃ parijānātīti?",
          "(Ka) yo rūpakkhandhaṃ na parijānāti so vedanākkhandhaṃ na parijānātīti?",
          "(Ka) yo rūpakkhandhaṃ parijānittha so vedanākkhandhaṃ parijānitthāti?",
          "(Ka) yo rūpakkhandhaṃ parijānissati so vedanākkhandhaṃ parijānissatīti?",
          "(Ka) yo rūpakkhandhaṃ na parijānāti so vedanākkhandhaṃ na parijānitthāti?",
          "Arahā rūpakkhandhaṃ na parijānāti, no ca vedanākkhandhaṃ na parijānittha.",
          "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānittha.",
          "Ye maggaṃ paṭilabhissanti te rūpakkhandhaṃ na parijānanti, no ca vedanākkhandhaṃ na parijānissanti.",
          "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānissanti.",
          "Aggamaggasamaṅgī vedanākkhandhaṃ na parijānittha, no ca rūpakkhandhaṃ na parijānāti."]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["parijānāti полностью понимает / понимают; parijānittha полностью понял / поняли; parijānissati полностью поймёт /",
          "  поймут; na … = не понимает полностью / не понял полностью / не поймёт полностью (never «полностью не …»);",
          "  same negated verb on both objects: не V полностью ни X, ни Y", "",
          "## Headings and closing labels", ""]
    ex = ["#### Paṇṇattivāro", "##### (Ka) uddeso", "#### Padasodhanavāro", "##### (Ka) anulomaṃ", "##### (Kha) paccanīkaṃ",
          "#### Padasodhanamūlacakkavāro", "#### Suddhakhandhavāro", "#### Suddhakhandhamūlacakkavāro",
          "##### (Kha) niddeso", "#### Paṇṇattivāraniddesa", "#### Pavattivāro 1. uppādavāro", "#### (1) Paccuppannavāro",
          "##### (Ka) anulomapuggalo", "##### (Kha) anulomaokāso", "##### (Ga) anulomapuggalokāsā",
          "##### (Gha) paccanīkapuggalo", "##### (Ṅa) paccanīkaokāso", "##### (Ca) paccanīkapuggalokāsā",
          "#### (2) Atītavāro", "#### (3) Anāgatavāro", "#### (4) Paccuppannātītavāro", "#### (5) Paccuppannānāgatavāro",
          "#### (6) Atītānāgatavāro", "#### Pavatti 2. nirodhavāro", "#### Uppādanirodhavāro", "#### Pariññāvāro",
          "#### Paccuppannavāro"]
    L += [f"{p} = {heading(p)}" for p in ex]
    ex = ["Paṇṇattiuddesavāro.", "Paṇṇattiniddesavāro.", "Uppādavāro niṭṭhito.", "Nirodhavāro.", "Uppādanirodhavāro.",
          "Pavattivāro niṭṭhito.", "Pariññāvāro.", "Khandhayamakapāḷi niṭṭhitā."]
    L += [f"{p} = {translate_line(p)}" for p in ex]
    L += ["Pañcakkhandhā – rūpakkhandho, … = " + translate_line(
        "Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho."),
          "variants: [X (syā.)] = [вариант чтения (Syā.): X]; (sī. syā.) = (Sī., Syā.); evamuparipi = «; так же и далее»"]
    return "\n".join(L) + "\n"


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        for ch in sys.argv[2:]:
            probe(ch)
        return
    RU = ROOT / "AI_translation" / "russian"
    for name, fn, lst in (("pi-5", "pi-5-russian-plain.md", PI5_STRINGS), ("pi-2", "pi-2-russian-plain.md", PI2_STRINGS)):
        txt = (RU / fn).read_text(encoding="utf-8")
        miss = [s for s in lst if s not in txt]
        assert not miss, f"{name} strings not found: {miss}"
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
    (S.RAILS / "notes-rails-G2.md").write_text(notes_md(), encoding="utf-8", newline="\n")
    print("wrote notes-rails-G2.md")
    for sid, note in dict.fromkeys(slips):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
