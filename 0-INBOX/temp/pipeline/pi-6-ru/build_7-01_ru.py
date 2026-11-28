"""Russian plain zero-shot of pi-6 (Yamaka): 7-01-anusayayamaka.md.

Wave-1 FRAME-SETTER for family C (Anusayayamaka: anuseti, uppattiṭṭhāna, sānusaya, pajahati, pariññā, pahīna,
uppajjati, dhātu) and for the general person / place question shape (yassa … tassa …, yattha … tattha …,
yassa yattha … tassa tattha …). Every frame is listed in notes-7-01.md.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-01_ru.py
Probe:  python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-01_ru.py --probe 7-02-anusayayamaka.md
        (prints, writes nothing: shows which lines of another chapter the frames below already cover)
Import: import importlib; C = importlib.import_module("build_7-01_ru")   (importing never writes any file)

Reuse in 7-02 … 7-11 (and in any yamaka with yassa / yattha questions):
  - names:      ANUSAYA_TAIL, anusaya(key, case), ANUSAYA_HEAD, ANUSAYA_HEAD_PL
  - lists:      parse_list(), ru_list()   («A, B и C»; negative «ни A, ни B»; "…pe…" -> "…")
  - verbs:      VERB (subject verbs: anuseti, uppajjati, pahīna + negatives), TRANSITIVE (pajahati, parijānāti,
                sānusaya: object in the accusative)
  - persons:    PERSON_GEN (yassa-type answers), PERSON_NOM (yo-type answers), RES (tassa / tesaṃ / tattha / ettha)
  - places:     LOCI
  - questions:  Q_PERSON, Q_PLACE, Q_PERSON_PLACE, Q_WHO, Q_WHO_PLACE, KHA_PREFIX, UPPATTI_Q -> question()
  - answers:    NO, NATTHI, B.AMANTA, ANSWER_INTRO_*, BOTH_FRAME, BOTH_NEG_FRAME / both_neg(), NO_CA_FRAME,
                NO_CA_POS_FRAME / no_ca(), RU_PLURAL -> answer_sentence()  (NO_CA_NEG_FRAME: deprecated, do not use)
  - closings:   MULAKA, ANUSAYAVARE_FRAME, VARO_CLOSING, VITTHARETABBAM, TADEKATTHA_FRAME, DHATU_* (proposals)
  - tr_line(), translate_file(), check_crossbook_c()
"""
import importlib
import pathlib
import re
import sys
import unicodedata

PIPE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(PIPE) not in sys.path:
    sys.path.insert(0, str(PIPE))
import build_sample_ru as B   # noqa: E402

CHAPTER = "7-01-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# The seven latent tendencies (pi-2 Vibhaṅga 16 / 17, pi-5 Kathāvatthu: «скрытая склонность к …»)
# ---------------------------------------------------------------------------------------------
ANUSAYA_TAIL = {
    "kāmarāga": "к чувственной страсти",
    "paṭigha": "к неприязни",
    "māna": "к самомнению",
    "diṭṭhi": "к воззрениям",
    "vicikicchā": "к колебанию",
    "bhavarāga": "к страсти к существованию",
    "avijjā": "к неведению",
}
ANUSAYA_HEAD = {"nom": "скрытая склонность", "acc": "скрытую склонность", "gen": "скрытой склонности",
                "dat": "скрытой склонности", "instr": "скрытой склонностью", "prep": "скрытой склонности"}
ANUSAYA_HEAD_PL = {"nom": "скрытые склонности", "acc": "скрытые склонности", "gen": "скрытых склонностей",
                   "dat": "скрытым склонностям", "instr": "скрытыми склонностями", "prep": "скрытых склонностях"}
# compound stem before "-ānusay-" -> key  (kāmārāga: source slip, rendered as meant)
ANUSAYA_STEM = {"kāmarāg": "kāmarāga", "kāmārāg": "kāmarāga", "paṭigh": "paṭigha", "mān": "māna",
                "diṭṭh": "diṭṭhi", "vicikicch": "vicikicchā", "bhavarāg": "bhavarāga", "avijj": "avijjā"}
ANUSAYA_TOKEN = re.compile(r"(" + "|".join(sorted(ANUSAYA_STEM, key=len, reverse=True)) + r")ānusay(o|aṃ|ena)")


def anusaya(key, case="nom"):
    """anusaya("kāmarāga") -> «скрытая склонность к чувственной страсти»; case: nom/acc/gen/dat/instr/prep."""
    return f"{ANUSAYA_HEAD[case]} {ANUSAYA_TAIL[key]}"


# Sattānusayā – … (pi-2 16-nanavibhango, exact)
SATTANUSAYA = ("Семь скрытых склонностей – " + ", ".join(anusaya(k) for k in list(ANUSAYA_TAIL)[:-1])
               + " и " + anusaya("avijjā") + ".")

# ---------------------------------------------------------------------------------------------
# Lists: "A ca B ca C ca" -> «A, B и C»; negated -> «ни A, ни B, ни C»; "A…pe… B" -> «A… B»;
# "A ca…pe… B ca" -> «A… и B».
# ---------------------------------------------------------------------------------------------
def parse_list(s):
    """-> (keys, joins, has_ca); joins[i] in {"list", "pe"} links keys[i] and keys[i+1]."""
    toks = s.replace("…pe…", " PE ").split()
    keys, joins, has_ca, pending = [], [], False, "list"
    for t in toks:
        m = ANUSAYA_TOKEN.fullmatch(t)
        if m:
            if keys:
                joins.append(pending)
            keys.append(ANUSAYA_STEM[m.group(1)])
            pending = "list"
        elif t == "ca":
            has_ca = True
        elif t == "PE":
            pending = "pe"
        else:
            raise ValueError(f"list token not parsed: {t!r} in {s!r}")
    if not keys:
        raise ValueError(f"empty list: {s!r}")
    return keys, joins, has_ca


def ru_list(parsed, case="nom", neg=False):
    keys, joins, has_ca = parsed
    names = [anusaya(k, case) for k in keys]
    if len(names) == 1:
        return names[0]
    if "pe" in joins:       # "A…pe… B" is a series asked in turn, not a conjunction: never «ни»
        neg = False
    if neg:
        names = ["ни " + n for n in names]
    out = names[0]
    for i, (j, n) in enumerate(zip(joins, names[1:])):
        last = i == len(names) - 2
        if j == "pe":
            sep = "… " + ("и " if has_ca and last and not neg else "")
        else:
            sep = " и " if (last and has_ca and not neg) else ", "
        out += sep + n
    return out


# ---------------------------------------------------------------------------------------------
# Verbs. VERB: the anusaya is the grammatical subject (Russian verb first, then the subject).
# value = (Russian, negative?)
# ---------------------------------------------------------------------------------------------
VERB = {
    "anuseti": ("залегает", False), "anusenti": ("залегают", False),          # pi-5 «залегает»
    "nānuseti": ("залегает", True), "nānusenti": ("залегают", True),
    "uppajjati": ("возникает", False), "uppajjanti": ("возникают", False),
    "nuppajjati": ("возникает", True), "nuppajjanti": ("возникают", True),
    "pahīno": ("устранена", False), "pahīnā": ("устранены", False),           # pi-5 «устранена»
    "appahīno": ("устранена", True), "appahīnā": ("устранены", True),
    "nappahīno": ("устранена", True), "nappahīnā": ("устранены", True),
}
# TRANSITIVE: the person is the subject, the anusaya the object (Russian accusative).
TRANSITIVE = {
    "pajahati": ("устраняет", False), "nappajahati": ("устраняет", True),     # pajahana = устранение
    "parijānāti": ("полностью понимает", False),                               # pariññā = полное понимание
    "sānusayo": ("имеет", False), "sānusayā": ("имеют", False),               # sānusaya = имеющий скрытую склонность
    "niranusayo": ("имеет", True), "niranusayā": ("имеют", True),
}
KNOWN_VERBS = set(VERB) | set(TRANSITIVE)
SLIPS = {"anusanti": "anusenti", "kāmārāgānusay": "kāmarāgānusay"}   # rendered as meant (report)


def pred(verb, parsed, case="nom", neg_extra=False):
    """«(не) залегает A» / «(не) залегают ни A, ни B»."""
    table = VERB if verb in VERB else TRANSITIVE
    ru, neg = table[verb]
    neg = neg != neg_extra
    return f"{'не ' if neg else ''}{ru} {ru_list(parsed, case, neg)}"


# ---------------------------------------------------------------------------------------------
# Persons and places
# ---------------------------------------------------------------------------------------------
PERSON_GEN = {                                     # yassa-type answers: «У X …»
    "anāgāmissa": "у невозвращающегося",           # pi-4/pi-5
    "arahato": "у архата",                         # pi-5
    "puthujjanassa": "у обычного человека",        # pi-4/pi-5
    "dvinnaṃ puggalānaṃ": "у двух личностей",
    "tiṇṇaṃ puggalānaṃ": "у трёх личностей",
    "catunnaṃ puggalānaṃ": "у четырёх личностей",
    "tesaññeva puggalānaṃ": "у этих же личностей",
    "tasseva puggalassa": "у этой же личности",
}
PERSON_FEM = {"tasseva puggalassa", "sveva puggalo"}   # «личность» is feminine: tassa -> «у неё», so -> «она»
PERSON_NOM = {                                  # yo-type answers (7-03 …, proposals)
    "anāgāmī": "невозвращающийся", "arahā": "архат", "puthujjano": "обычный человек",
    "dve puggalā": "две личности", "tayo puggalā": "три личности", "cattāro puggalā": "четыре личности",
    "teva puggalā": "эти же личности", "sveva puggalo": "эта же личность",
}
RES = {                                            # resumptive words after the person / place
    "tassa": "у него", "tesaṃ": "у них",
    "ettha": "там", "tattha": "там",
    "tassa tattha": "у него там", "tesaṃ tattha": "у них там",
    "so": "он", "te": "они", "tato": "там", "so tato": "он там", "te tato": "они там",
}
RES_FEM = {"у него": "у неё", "у него там": "у неё там", "он": "она", "он там": "она там"}
LOCI = {
    "sabbasakkāyapariyāpannesu dhammesu": "во всех явлениях, входящих в самость",   # sakkāya pi-1, pariyāpanna pi-5
    "kāmadhātuyā dvīsu vedanāsu": "в мире чувственных желаний в двух видах чувства",
    "kāmadhātuyā tīsu vedanāsu": "в мире чувственных желаний в трёх видах чувства",
    "dukkhāya vedanāya": "в болезненном чувстве",                                  # pi-1/pi-5
    "kāmadhātuyā": "в мире чувственных желаний",                                   # pi-2
    "rūpadhātuyā": "в мире форм",                                                  # pi-2
    "arūpadhātuyā": "в мире без форм",                                             # pi-2
    "apariyāpanne": "в не принадлежащем к кругам существования",                   # pi-1 apariyāpanna (proposal)
}
LOCI_SEP = ", "            # Pāli lists the places without "ca": «в мире форм, в мире без форм»

# ---------------------------------------------------------------------------------------------
# Question frames (the general person / place shape)
# ---------------------------------------------------------------------------------------------
UPPATTI_Q = "Где {p1}?"                                          # Kattha X anuseti?
Q_PERSON = "У кого {p1}, у того {p2}?"                           # yassa … tassa …
Q_PLACE = "Где {p1}, там {p2}?"                                  # yattha … tattha … (also yato … tato …)
Q_PERSON_PLACE = "У кого где {p1}, у того там {p2}?"             # yassa yattha … tassa tattha …
Q_WHO = "Кто {p1}, тот {p2}?"                                    # yo … so …
Q_WHO_PLACE = "Кто где {p1}, тот там {p2}?"                      # yo yato … so tato …
KHA_PREFIX = "А "                                                # "vā pana": «А у кого …», «А где …»

# Answers
AMANTA = B.AMANTA          # Āmantā. = Да.
NO = "Нет."                # No. (pi-5 «? Нет.»)
NATTHI = "Такого нет."     # Natthi. (no such person / place / case)
SIMPLE_ANSWERS = {"Āmantā.": AMANTA, "No.": NO, "Natthi.": NATTHI}
# answer sentence = intro + clause [+ ", но " + no-ca clause] + "."
ANSWER_INTRO_PERSON = "{person} "                # «У невозвращающегося залегает …»
ANSWER_INTRO_PLACE = "{loci}: {res} "            # «В мире форм, в мире без форм: там залегает …»
ANSWER_INTRO_PERSON_PLACE = "{person} {loci}: {res} "   # «У X в …: у него там залегает …»
BOTH_FRAME = "и {p1}, и {p2}"                    # "A ca anuseti B ca anuseti": «и залегает A, и залегает B»
BOTH_NEG_FRAME = "не {verb} {items}"             # "A ca nānuseti B ca nānuseti": «не залегает ни A, ни B»
                                                 # (verb once; plural when a Pāli verb is plural or a list follows)
NO_CA_FRAME = ", но {res} {neg_pred}"            # ", no ca tassa B anuseti": «, но у него не залегает B»
NO_CA_POS_FRAME = ", но {res} {pos_pred}"        # ", no ca tassa B nānuseti": «, но у него залегает B» (coordinator)
# DEPRECATED (coordinator 2026-11-27: never «но не так, что»); kept only so that older importers still load.
NO_CA_NEG_FRAME = ", но не так, что {res} {neg_pred}"
# plural of the Russian subject verbs (BOTH_NEG_FRAME)
RU_PLURAL = {"залегает": "залегают", "возникает": "возникают", "устранена": "устранены"}


def no_ca(verb, parsed, res, case="nom"):
    """", no ca <res> B <verb>" for any verb in VERB / TRANSITIVE: "no" negates the verb that follows.
    anuseti -> «, но у него не залегает B»; nānuseti -> «, но у него залегает B»;
    pajahati / nappajahati -> «, но он не устраняет B» / «, но он устраняет B» (case="acc")."""
    table = VERB if verb in VERB else TRANSITIVE
    txt = pred(verb, parsed, case, neg_extra=True)
    return (NO_CA_POS_FRAME if table[verb][1] else NO_CA_FRAME).format(res=res, pos_pred=txt, neg_pred=txt)

# Closings and markers
MULAKA = {   # "(Ekamūlakaṃ)" … closes each block of the cycle
    "Ekamūlakaṃ": "На основе одного", "Dukamūlakaṃ": "На основе двух", "Tikamūlakaṃ": "На основе трёх",
    "Catukkamūlakaṃ": "На основе четырёх", "Pañcakamūlakaṃ": "На основе пяти",
    "Chakkamūlakaṃ": "На основе шести",
    "Kāmadhātumūlakaṃ": "На основе мира чувственных желаний", "Rūpadhātumūlakaṃ": "На основе мира форм",
    "Arūpadhātumūlakaṃ": "На основе мира без форм",
}
ANUSAYAVARE_FRAME = "{form} в разделе о скрытых склонностях."    # Anusayavāre anulomaṃ / paccanīkaṃ.
VARO_CLOSING = "{heading}."                                       # Uppattiṭṭhānavāro. / Pahīnavāro. / …
VITTHARETABBAM = "следует развернуть"                             # (vitthāretabbaṃ) (pi-5)
TADEKATTHA_FRAME = "{Verb} то, что пребывает вместе с ней."       # Tadekaṭṭhaṃ pajahati. (proposal)
EXTRA_HEADINGS = {   # not in the sample's SECTION_HEADINGS (proposals for 7-10 / 7-11)
    "Uppajjanavāro": "Раздел о возникновении",
    "dhātupucchāvāro": "раздел вопросов об элементах",
}
# Dhātu sections (7-10 / 7-11), proposals:
DHATU_CUTA = "у того, кто, уйдя из {src}, перерождается {neg}{dst}"   # Kāmadhātuyā cutassa (na) kāmadhātuṃ upapajjantassa
DHATU_SRC = {"kāmadhātuyā": "мира чувственных желаний", "rūpadhātuyā": "мира форм", "arūpadhātuyā": "мира без форм"}
DHATU_DST = {"kāmadhātuṃ": "в мире чувственных желаний", "rūpadhātuṃ": "в мире форм", "arūpadhātuṃ": "в мире без форм"}
DHATU_KATI = ("сколько скрытых склонностей залегает, сколько скрытых склонностей не залегает, "
              "сколько скрытых склонностей разрушено?")              # kati anusayā anusenti, … nānusenti, … bhaṅgā?
DHATU_KASSACI = "у некоторых залегают {num} скрытых склонностей"       # kassaci satta / pañca anusayā anusenti (pi-2 kassaci)
DHATU_BHANGA_NATTHI = "разрушенных скрытых склонностей нет"            # anusayā bhaṅgā natthi


# ---------------------------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------------------------
def lower1(s):
    return s[:1].lower() + s[1:]


def preprocess(s):
    s = s.replace(" …pe…", "…pe…")          # "diṭṭhānusayo …pe…" spacing slip
    for a, b in SLIPS.items():
        s = s.replace(a, b)
    return s


def unti(w):
    """anusetīti -> anuseti; anusentīti -> anusenti; pahīnoti -> pahīno; sānusayoti -> sānusayo."""
    if w.endswith("īti") and w[:-3] + "i" in KNOWN_VERBS:
        return w[:-3] + "i"
    if w.endswith("ti") and w[:-2] in KNOWN_VERBS:
        return w[:-2]
    return w


def split_clause(s, verbs):
    """'A ca anuseti B ca C ca anusenti' -> [('A ca', 'anuseti'), ('B ca C ca', 'anusenti')]."""
    segs, cur = [], []
    for w in s.split(" "):
        if w in verbs:
            segs.append((" ".join(cur), w))
            cur = []
        else:
            cur.append(w)
    if cur or not segs:
        raise ValueError(f"clause not parsed: {s!r}")
    return segs


def both_neg(segs, parsed, table, case="nom"):
    """"A ca nānuseti B ca C ca nānusenti" -> «не залегают ни A, ни B, ни C» (BOTH_NEG_FRAME).
    Subject verbs (VERB): plural when a Pāli verb is plural or a list follows; TRANSITIVE: the person's number."""
    rus = [table[v][0] for _, v in segs]
    verb = rus[0]
    if table is VERB and (any(r in RU_PLURAL.values() for r in rus) or any(len(p[0]) > 1 for p in parsed)):
        verb = RU_PLURAL.get(verb, verb)
    items = []
    for p in parsed:
        t = ru_list(p, case, True)
        items.append(t if t.startswith("ни ") else "ни " + t)
    return BOTH_NEG_FRAME.format(verb=verb, items=", ".join(items))


def clause(s, verbs=VERB, case="nom"):
    """One predicate, or the both-form «и P1, и P2»."""
    segs = split_clause(s, verbs)
    if len(segs) == 1:
        lst, v = segs[0]
        return pred(v, parse_list(lst), case)
    if len(segs) == 2 and all(l.endswith(" ca") for l, _ in segs):
        table = VERB if segs[0][1] in VERB else TRANSITIVE
        parsed = [parse_list(l[:-3]) for l, _ in segs]
        if all(table[v][1] for _, v in segs):      # both negated: «не залегает ни A, ни B»
            return both_neg(segs, parsed, table, case)
        p = [pred(v, pl, case) for (_, v), pl in zip(segs, parsed)]
        return BOTH_FRAME.format(p1=p[0], p2=p[1])
    raise ValueError(f"clause shape not parsed: {s!r}")


def _alt(keys):
    return "|".join(re.escape(k) for k in sorted(keys, key=len, reverse=True))


QV = _alt(VERB)
TV = _alt(TRANSITIVE)
Q_YASSA = re.compile(rf"(yassa|yattha)( vā pana)?( yattha)? (.+?) ({QV}) (tassa tattha|tassa|tattha) (.+) ({QV})")
Q_YO = re.compile(rf"(yo)( vā pana)?( yato)? (.+?) ({TV}) (so tato|so) (.+) ({TV})")
Q_KATTHA = re.compile(rf"kattha (.+) ({QV})")


def question(q):
    """Pāli question without the final '?' (label already removed) -> Russian with '?'."""
    words = lower1(q.strip()).split(" ")
    words[-1] = unti(words[-1])
    t = " ".join(words)
    m = Q_KATTHA.fullmatch(t)
    if m:
        return UPPATTI_Q.format(p1=pred(m.group(2), parse_list(m.group(1))))
    m = Q_YASSA.fullmatch(t)
    if m:
        first, vapana, yattha, l1, v1, res2, l2, v2 = m.groups()
        p1, p2 = pred(v1, parse_list(l1)), pred(v2, parse_list(l2))
        if first == "yattha":
            assert not yattha and res2 == "tattha", q
            frame = Q_PLACE
        elif yattha:
            assert res2 == "tassa tattha", q
            frame = Q_PERSON_PLACE
        else:
            assert res2 == "tassa", q
            frame = Q_PERSON
        out = frame.format(p1=p1, p2=p2)
        return KHA_PREFIX + lower1(out) if vapana else out
    m = Q_YO.fullmatch(t)
    if m:
        _, vapana, yato, l1, v1, res2, l2, v2 = m.groups()
        p1, p2 = pred(v1, parse_list(l1), "acc"), pred(v2, parse_list(l2), "acc")
        assert bool(yato) == (res2 == "so tato"), q
        out = (Q_WHO_PLACE if yato else Q_WHO).format(p1=p1, p2=p2)
        return KHA_PREFIX + lower1(out) if vapana else out
    raise ValueError(f"question not parsed: {q!r}")


def _take(body, table):
    for k in sorted(table, key=len, reverse=True):
        if body.startswith(k + " "):
            return k, body[len(k) + 1:]
    return None, body


def answer_sentence(s):
    """One Pāli answer sentence (ends with '.') -> Russian."""
    if s in SIMPLE_ANSWERS:
        return SIMPLE_ANSWERS[s]
    assert s.endswith("."), s
    body = lower1(s[:-1])
    person, body = _take(body, PERSON_GEN)
    loci = []
    while True:
        loc, body = _take(body, LOCI)
        if not loc:
            break
        loci.append(loc)
    res, body = _take(body, {k: 0 for k in ("tassa tattha", "tesaṃ tattha", "ettha", "tattha")})
    main, _, neg = body.partition(", no ca ")

    def res_ru(k):
        r = RES[k]
        return RES_FEM.get(r, r) if person in PERSON_FEM else r

    if person and loci:
        assert res in ("tassa tattha", "tesaṃ tattha"), s
        head = ANSWER_INTRO_PERSON_PLACE.format(person=PERSON_GEN[person], loci=LOCI_SEP.join(LOCI[x] for x in loci),
                                                res=res_ru(res))
    elif loci:
        assert res in ("ettha", "tattha"), s
        head = ANSWER_INTRO_PLACE.format(loci=LOCI_SEP.join(LOCI[x] for x in loci), res=RES[res])
    elif person:
        assert res is None, s
        head = ANSWER_INTRO_PERSON.format(person=PERSON_GEN[person])
    else:
        raise ValueError(f"answer intro not parsed: {s!r}")
    out = head + clause(main)
    if neg:
        nres, neg = _take(neg, {k: 0 for k in ("tassa tattha", "tesaṃ tattha", "tassa", "tesaṃ", "tattha")})
        exp = {(True, True): ("tassa tattha", "tesaṃ tattha"), (False, True): ("tattha",),
               (True, False): ("tassa", "tesaṃ")}[(bool(person), bool(loci))]
        assert nres in exp, s
        segs = split_clause(neg, VERB)
        assert len(segs) == 1, s
        lst, v = segs[0]
        out += no_ca(v, parse_list(lst), res_ru(nres))
    return cap(out) + "."


def answers(a):
    sents = re.split(r"(?<=\.) (?=\S)", a.strip())
    return " ".join(answer_sentence(x) for x in sents)


# ---------------------------------------------------------------------------------------------
# Lines
# ---------------------------------------------------------------------------------------------
ALL_HEADINGS = dict(B.SECTION_HEADINGS, **EXTRA_HEADINGS)
HEAD_RE = re.compile(r"(#+) (?:\((\w+)\) )?(.+)")

FIXED = {
    "Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, bhavarāgānusayo, "
    "avijjānusayo.": SATTANUSAYA,
    "Uppattiṭṭhānavāro.": VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppattiṭṭhānavāro"]),
    "Anusayavāre anulomaṃ.": ANUSAYAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["anulomaṃ"])),
    "Anusayavāre paccanīkaṃ.": ANUSAYAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["paccanīkaṃ"])),
}


def heading(body):
    """'(Ka) anulomapuggalo' -> '(а) Утвердительная форма по личности' (see heading_case)."""
    m = HEAD_RE.fullmatch(body)
    hashes, lab, text = m.groups()
    if text in B.YAMAKA_TITLES:
        ru = B.YAMAKA_TITLES[text]
    else:
        ru = heading_case(ALL_HEADINGS[text])
    return f"{hashes} " + (f"({B.LETTERS[lab]}) " if lab else "") + ru


def heading_case(ru):
    """Coordinator rule: in headings the first word, and the first word after a label or a number, is capitalised
    («(а) Утвердительная форма по личности», «Большой раздел 1. Раздел о скрытых склонностях»)."""
    return re.sub(r"(\d+\. )(\w)", lambda m: m.group(1) + m.group(2).upper(), cap(ru))


MULAKA_RE = re.compile(r"(.*?) ?\((\w+mūlakaṃ) ?\)")
LABEL_RE = re.compile(r"\((\w+)\) (.*)")


def tr_line(body):
    if not body.strip():
        return ""
    if body in FIXED:
        return FIXED[body]
    if body.startswith("#"):
        return heading(body)
    text = preprocess(body)
    tail = ""
    m = MULAKA_RE.fullmatch(text)
    if m:
        text, tail = m.group(1), f" ({MULAKA[m.group(2)]})"
    label = ""
    m = LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    if "?" in text:
        q, _, a = text.partition("?")
        out = label + question(q)
        if a.strip():
            out += " " + answers(a)
    else:
        out = label + answers(text)
    return out + tail


def translate_file(src_text):
    out = []
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
CROSSBOOK_C = [   # strings taken from the approved pi-1 … pi-5 Russian rails
    ("2", SATTANUSAYA),
    ("5", "В болезненном чувстве залегает скрытая склонность к страсти"),     # anuseti = залегает
    ("5", "скрытая склонность к страсти к существованию"),
    ("1", "в мире чувственных желаний"), ("2", "в мире форм"), ("2", "в мире без форм"),
    ("1", "болезненным чувством"), ("2", "видов контакта"),
    ("1", "воззрение о самости"), ("5", "входит в мир форм"),
    ("5", "у невозвращающегося"), ("5", "У обычного человека"), ("5", "у архата страсть устранена"),
    ("4", "невозвращающийся"), ("5", "архат"),
    ("5", "? Нет."), ("5", "так следует развернуть всё"), ("2", "у некоторых"), ("2", "перерождаются"),
    ("4", "уйдя из мира"), ("1", "пребывающие вместе с ними"), ("1", "не принадлежащие к кругам существования"),
]


def check_crossbook_c():
    cache, missing = {}, []
    for b, s in CROSSBOOK_C:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def check_consistency(src, ru, seen):
    """Identical Pāli line -> identical Russian line (within the chapter and with `seen`)."""
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in seen:
            assert seen[pb] == rb, f"inconsistent: {pb!r}"
        seen[pb] = rb


def probe(name):
    """Print the lines of another chapter that the frames already translate; count the rest. Writes nothing."""
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    ok = bad = 0
    for line in src.split("\n"):
        body, _ = B.ID_RE.match(line).groups()
        try:
            r = tr_line(body)
            ok += 1
            if body.strip():
                print("OK ", r[:200])
        except Exception as e:   # noqa: BLE001
            bad += 1
            print("-- ", type(e).__name__, str(e)[:160])
    print(f"{name}: {ok} lines translated, {bad} not covered")


def main():
    B.check_crossbook()
    check_crossbook_c()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_consistency(src, ru, {})
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        probe(sys.argv[2])
    else:
        main()
