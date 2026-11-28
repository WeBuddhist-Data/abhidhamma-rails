"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-13-indriyayamaka.md (Indriya pariññāvāra, the six time
sections, closing of the Indriyayamaka and of the whole book).

Family E (pariññāvāra) from build_2-02_ru (PJ_RU, PJ_PRED, PJ_NO_CA_FRAME, PJ_NEITHER_FRAME, PJ_NEG_MIXED_FRAME,
PJ_BOTH_FRAME, PJ_SUBJ_UNITS, PJ_GEN), pajahati in all tenses from build_5-03_ru (PJ3_FORMS / PJ3_RU), bhāveti
«развивает» from build_9-03_ru, persons (личность восьмой ступени, обладающий путём невозвращения, «Кроме …,
остальные личности») from build_7-05_ru, «невозвращающийся» / «три личности» from build_7-01_ru, members, headings
and mūlaka tails from build_10-01_ru. NEW here (listed in notes-10-13.md): the past / future of bhāveti, sacchikaroti
in all tenses, feminine past forms (личность восьмой ступени), the persons "yo aggaphalaṃ sacchikaroti / sacchākāsi
so", "ye puthujjanā maggaṃ [na] paṭilabhissanti te", "pañca … aṭṭha puggalā", "tayo maggasamaṅgino", and the
book closing «Парные вопросы завершены.».

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-13_ru.py [--probe]
Import: importlib.import_module("build_10-13_ru")   (importing never writes any file; only __main__ builds)
"""
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

E = importlib.import_module("build_2-02_ru")    # family E (frame-setter)
A = E.A                                          # build_2-01_ru: APART_GROUP, _norm, variants, consistency
C = E.C                                          # build_7-01_ru: Q_WHO, KHA_PREFIX, PERSON_NOM, SIMPLE_ANSWERS
S3 = importlib.import_module("build_5-03_ru")   # pajahati: PJ3_FORMS / PJ3_RU
G = importlib.import_module("build_7-05_ru")    # PERSON_NOM_05, PERSON_FEM_05, APART_GEN_05
H = importlib.import_module("build_9-03_ru")    # bhāveti = «развивает»
I1 = importlib.import_module("build_10-01_ru")  # IN_PALI, IN_K, heading(), TAIL_RE / TAILS (mūlaka tails)

CHAPTER = "10-13-indriyayamaka.md"
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Verbs: family E + pajahati (5-03) + bhāveti (9-03) + sacchikaroti (NEW)
# =============================================================================================
FORMS = dict(S3.PJ3_FORMS)
FORMS.update({
    "bhāveti": ("bhāveti", "pres", "sg"), "bhāventi": ("bhāveti", "pres", "pl"),
    "bhāvittha": ("bhāveti", "past", None),
    "bhāvessati": ("bhāveti", "fut", "sg"), "bhāvessanti": ("bhāveti", "fut", "pl"),
    "sacchikaroti": ("sacchikaroti", "pres", "sg"), "sacchikaronti": ("sacchikaroti", "pres", "pl"),
    "sacchikarittha": ("sacchikaroti", "past", None),
    "sacchikarissati": ("sacchikaroti", "fut", "sg"), "sacchikarissanti": ("sacchikaroti", "fut", "pl"),
    # ^6-10-452 "aññindriyañca bhavissanti" (bhavati "will be", for bhāvessanti): a real word, kept as written
    "bhavissanti": ("bhavati", "fut", "pl"),
})
RU = dict(S3.PJ3_RU)
RU.update({
    # bhāveti = «развивает» (pi-1, pi-5, 9-03); past / future perfective as family E «полностью понял / поймёт»
    ("bhāveti", "pres", "sg"): ("развивает", "не развивает"),
    ("bhāveti", "pres", "pl"): ("развивают", "не развивают"),
    ("bhāveti", "past", "sg"): ("развил", "не развил"),
    ("bhāveti", "past", "pl"): ("развили", "не развили"),
    ("bhāveti", "fut", "sg"): ("разовьёт", "не разовьёт"),
    ("bhāveti", "fut", "pl"): ("разовьют", "не разовьют"),
    # sacchikaroti = «осуществляет» (pi-2, pi-4, pi-5 «осуществляет прекращение», «осуществляет плод …»)
    ("sacchikaroti", "pres", "sg"): ("осуществляет", "не осуществляет"),
    ("sacchikaroti", "pres", "pl"): ("осуществляют", "не осуществляют"),
    ("sacchikaroti", "past", "sg"): ("осуществил", "не осуществил"),
    ("sacchikaroti", "past", "pl"): ("осуществили", "не осуществили"),
    ("sacchikaroti", "fut", "sg"): ("осуществит", "не осуществит"),
    ("sacchikaroti", "fut", "pl"): ("осуществят", "не осуществят"),
    ("bhavati", "fut", "pl"): ("будут", "не будут"),
})
# Feminine singular (subject «личность восьмой ступени»): past tense agrees in gender; present / future = sg
FEM_PAST = {
    "parijānāti": ("полностью поняла", "не поняла полностью"),
    "pajahati": ("устранила", "не устранила"),
    "bhāveti": ("развила", "не развила"),
    "sacchikaroti": ("осуществила", "не осуществила"),
}
for (_lem, _t, _n), _v in list(RU.items()):
    if _n == "sg":
        RU[(_lem, _t, "sgf")] = FEM_PAST[_lem] if _t == "past" else _v
INSTR_LEMMAS = {"bhavati"}                      # «будут {instr}» (predicate noun in the instrumental)

assert all(RU[k] == E.PJ_RU[k] for k in E.PJ_RU)
assert all(RU[k] == S3.PJ3_RU[k] for k in S3.PJ3_RU)
assert RU[("bhāveti", "pres", "sg")][0] == H.BH_VERBS["bhāveti"][0]
assert RU[("pajahati", "pres", "sg")][0] == H.BH_VERBS["pajahati"][0]

# =============================================================================================
# Members (objects in the accusative: «способность …» acc = nom)
# =============================================================================================
MEMBERS = ["cakkhu", "sota", "domanassa", "anaññātaññassāmīti", "añña", "aññātāvī"]
OBJ = {I1.IN_PALI[m]: I1.IN_K[m]["nom"] for m in MEMBERS}
OBJ_INSTR = {I1.IN_PALI[m]: I1.IN_K[m]["instr"] for m in MEMBERS}
assert all(v.startswith("способность ") for v in OBJ.values())

NEG = r"(?:na |nap(?=pajah))"                     # "na parijānāti" / "nappajahati" (5-03)
V_RE = E._alt(FORMS)
X_RE = E._alt(OBJ)


def forms(v, num):
    lemma, tense, _ = FORMS[v]
    return RU[(lemma, tense, num)]


def pred(v, x, num, neg):
    pos, negf = forms(v, num)
    obj = OBJ_INSTR[x] if FORMS[v][0] in INSTR_LEMMAS else OBJ[x]
    return E.PJ_PRED.format(v=negf if neg else pos, obj=obj)


def unti(w):
    """bhāvetīti -> bhāveti; nappajahitthāti -> nappajahittha; sacchikarissatīti -> sacchikarissati."""
    for suf, rep in (("īti", "i"), ("āti", "a")):
        base = w[: -len(suf)] + rep
        if w.endswith(suf) and re.sub(r"^nap(?=pajah)", "", base) in FORMS:
            return base
    return w


# =============================================================================================
# Questions: yo X V so Y V-ti? -> C.Q_WHO «Кто {p1}, тот {p2}?»; vā pana -> «А кто …»
# =============================================================================================
Q_RE = re.compile(r"yo(?P<vp> vā pana)? (?P<x>" + X_RE + r") (?P<n1>" + NEG + r")?(?P<v1>" + V_RE + r")"
                  r"(?P<stop>\.)? (?:so|So) (?P<y>" + X_RE + r") (?P<n2>" + NEG + r")?(?P<v2>" + V_RE + r")")
Q_JOIN = ", тот "
assert Q_JOIN in C.Q_WHO and C.Q_WHO.endswith("?")


def question(body, punct):
    words = body.split(" ")
    words[-1] = unti(words[-1])
    m = Q_RE.fullmatch(" ".join(words))
    if not m:
        raise ValueError(f"pariññā question not parsed: {body!r}")
    q = C.Q_WHO.format(p1=pred(m.group("v1"), m.group("x"), "sg", bool(m.group("n1"))),
                       p2=pred(m.group("v2"), m.group("y"), "sg", bool(m.group("n2"))))
    if m.group("stop"):                         # ^6-10-477 "… bhāvessati. So …": stray full stop, kept as written
        q = q.replace(Q_JOIN, ". " + cap(Q_JOIN[2:]), 1)
        SLIP_LOG.append("stray '.' inside the question kept as written: " + body[:60])
    if punct == ".":                            # ^6-10-455 "…bhāvessatīti." ('.' for '?'), kept as written
        q = q[:-1] + "."
        SLIP_LOG.append("'.' ending a question kept as written: " + body[:60])
    return C.KHA_PREFIX + lower1(q) if m.group("vp") else q


# =============================================================================================
# Persons of the answers (nominative)
# =============================================================================================
PUTH_NOT = next(ru for rx, ru, _, _ in E.PJ_SUBJ_UNITS if rx.startswith("ye ca puthujjanā"))
PUTH_YES = PUTH_NOT.replace("которые не обретут", "которые обретут")
assert PUTH_YES != PUTH_NOT
AGG_NOM = next(ru for rx, ru, _, _ in E.PJ_SUBJ_UNITS if rx == "aggamaggasamaṅgī")
ARAHA_NOM = next(ru for rx, ru, _, _ in E.PJ_SUBJ_UNITS if rx == "arahā")
AGGAPHALA = "высший плод"                       # aggaphala (5-03 «высшего плода»)
NUM_NOM = {   # "N puggalā" (7-01 PERSON_NOM for 2 … 4; pi-5 «пять / семь / восемь личностей»)
    "dve": C.PERSON_NOM["dve puggalā"], "tayo": C.PERSON_NOM["tayo puggalā"],
    "cattāro": C.PERSON_NOM["cattāro puggalā"], "pañca": "пять личностей", "cha": "шесть личностей",
    "satta": "семь личностей", "aṭṭha": "восемь личностей",
}
MAGGASAMANGI = "обладающих путём"               # maggasamaṅgino (pi-1 / pi-2 «обладающий путём»; 7-05 genitive)
assert G.APART_GEN_05["dvinnaṃ maggasamaṅgīnaṃ"] == "двух " + MAGGASAMANGI
NUM_GEN = {"dve": "двух", "tayo": "трёх", "cattāro": "четырёх"}

# (pattern, Russian, Russian number, relative clause -> closing comma)
SUBJ_UNITS = [
    (r"(.+?) ṭhapetvā avasesā puggalā", None, "pl", False),
    (r"ye puthujjanā maggaṃ na paṭilabhissanti te", PUTH_NOT, "pl", True),
    (r"ye puthujjanā maggaṃ paṭilabhissanti te", PUTH_YES, "pl", True),
    (r"yo aggaphalaṃ sacchikaroti so", "тот, кто " + RU[("sacchikaroti", "pres", "sg")][0] + " " + AGGAPHALA,
     "sg", True),
    (r"yo aggaphalaṃ sacchākāsi so", "тот, кто " + RU[("sacchikaroti", "past", "sg")][0] + " " + AGGAPHALA,
     "sg", True),
    (r"(dve|tayo|cattāro|pañca|cha|satta|aṭṭha) puggalā", "NUM", "pl", False),
    (r"tayo maggasamaṅgino", "три " + MAGGASAMANGI, "pl", False),
    (r"aggamaggasamaṅgī", AGG_NOM, "sg", False),
    (r"anāgāmimaggasamaṅgī", G.PERSON_NOM_05["anāgāmimaggasamaṅgī"], "sg", False),
    (r"aṭṭhamako", G.PERSON_NOM_05["aṭṭhamako"], "sgf", False),
    (r"anāgāmī", C.PERSON_NOM["anāgāmī"], "sg", False),
    (r"arahā", ARAHA_NOM, "sg", False),
]
assert "aṭṭhamako" in G.PERSON_FEM_05            # «личность» is feminine (7-05)
APART_GEN = dict(G.APART_GEN_05)
APART_GEN.update({
    "arahantaṃ": E.PJ_GEN["arahantaṃ"],
    **{f"{k} maggasamaṅgino": f"{v} {MAGGASAMANGI}" for k, v in NUM_GEN.items()},
})


def apart(group):
    """'tayo maggasamaṅgino ca arahantañca' -> «Кроме трёх обладающих путём и архата, остальные личности»."""
    t = re.sub(r"ñca(?=\s|$)", "ṃ ca", group)
    parts = [x.strip() for x in re.split(r" ca(?=\s|$)", t) if x.strip()]
    names = [APART_GEN[x] for x in parts]
    a_gen = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " и " + names[-1]
    return A.APART_GROUP.format(a_gen=a_gen, g_nom=G.PUGGALA_PL)


def subject(s):
    """One person unit (the chapter has no lists of persons) -> (Russian with a closing comma if needed, number)."""
    s = lower1(s)
    for rx, ru, num, rel in SUBJ_UNITS:
        m = re.fullmatch(rx, s)
        if m:
            if ru is None:
                ru = apart(m.group(1))
            elif ru == "NUM":
                ru = NUM_NOM[m.group(1)]
            return cap(ru) + ("," if rel else ""), num
    raise ValueError(f"subject not parsed: {s!r}")


# =============================================================================================
# Answer sentences
# =============================================================================================
S1_RE = re.compile(r"(?P<subj>.+?) (?P<x>" + X_RE + r") (?P<n1>" + NEG + r")?(?P<v1>" + V_RE + r"), no ca "
                   r"(?P<y>" + X_RE + r") (?P<n2>" + NEG + r")?(?P<v2>" + V_RE + r")")
S2_RE = re.compile(r"(?P<subj>.+?) (?P<x>" + X_RE + r") ca (?P<n1>" + NEG + r")?(?P<v1>" + V_RE + r")(?P<comma>,)? "
                   r"(?P<y>" + X_RE + r") ca (?P<n2>" + NEG + r")?(?P<v2>" + V_RE + r")")


def _check_num(v, num, s):
    pn = FORMS[v][2]
    if pn is not None and pn != num[:2]:
        # the Russian verb agrees with the subject (Russian grammar); the Pāli number slip is reported
        SLIP_LOG.append(f"verb number: {v} with a {num} subject (Russian follows the subject): {s[:70]}")


def sentence(s):
    """One Pāli answer sentence (final '.' removed) -> Russian (with '.')."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    s = re.sub(r"(?<=driya)ñca\b", "ṃ ca", s)                 # Xindriyañca -> Xindriyaṃ ca (A._norm would
                                                             # also split the numeral "pañca")
    for rx, kind in ((S1_RE, 1), (S2_RE, 2)):
        m = rx.fullmatch(s)
        if not m:
            continue
        subj, num = subject(m.group("subj"))
        _check_num(m.group("v1"), num, s)
        _check_num(m.group("v2"), num, s)
        x, y = m.group("x"), m.group("y")
        n1, n2 = bool(m.group("n1")), bool(m.group("n2"))
        p1 = pred(m.group("v1"), x, num, n1)
        if kind == 1:   # "no ca": the question's predicate is denied for Y (coordinator "Negatives")
            return f"{subj} {p1}{E.PJ_NO_CA_FRAME.format(pred=pred(m.group('v2'), y, num, not n2))}."
        if m.group("comma"):                     # ^6-10-468 stray comma: it falls on the comma of «и …, и …»
            SLIP_LOG.append("stray ',' inside the ca … ca pair kept (the comma of «и …, и …»): " + s[:60])
        if n1 and n2:
            f1, f2 = forms(m.group("v1"), num)[1][3:], forms(m.group("v2"), num)[1][3:]
            both = (E.PJ_NEITHER_FRAME.format(v=f1, x=OBJ[x], y=OBJ[y]) if f1 == f2
                    else E.PJ_NEG_MIXED_FRAME.format(v1=f1, x=OBJ[x], v2=f2, y=OBJ[y]))
            return f"{subj} {both}."
        return f"{subj} {E.PJ_BOTH_FRAME.format(p1=p1, p2=pred(m.group('v2'), y, num, n2))}."
    raise ValueError(f"answer not parsed: {s!r}")


# ^6-10-452 "…pajahissanti, pañca puggalā …": a comma where a full stop belongs, kept as written («…, пять …»)
COMMA_JOIN_RE = re.compile(r", (?=(?:dve|tayo|cattāro|pañca|cha|satta|aṭṭha) puggalā )")


def answers(text):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        parts = COMMA_JOIN_RE.split(s[:-1])
        if len(parts) > 1:
            SLIP_LOG.append("',' for '.' between two answer sentences kept as written: " + s[:60])
        ru = [sentence(p)[:-1] for p in parts]
        out.append(", ".join([ru[0]] + [lower1(r) for r in ru[1:]]) + ".")
    return " ".join(out)


QA_RE = re.compile(r"\((Ka|Kha)\) (yo .+?(?:īti|āti))([?.])(?: (.+))?")


def pj_line(text):
    m = QA_RE.fullmatch(text)
    if m:
        lab, body, punct, ans = m.groups()
        out = f"({B.LETTERS[lab]}) {question(body, punct)}"
        return out + (" " + answers(ans) if ans else "")
    return answers(text)


# =============================================================================================
# Slips (plain spelling slips / missing punctuation, rendered as meant; each occurs exactly once)
# =============================================================================================
SLIPS = [
    ("domanassindriyaṃ nappajjahittha so", "domanassindriyaṃ nappajahittha so",
     "^6-10-480 'nappajjahittha' = nappajahittha (spelling)"),
    ("domanassindriyaṃ pajahanti anāgāmimaggasamaṅgi aññindriyañca",
     "domanassindriyaṃ pajahanti. Anāgāmimaggasamaṅgī aññindriyañca",
     "^6-10-468 missing full stop before 'anāgāmimaggasamaṅgi', and -gi = -gī (spelling)"),
    ("aññindriyaṃ bhāvessanti no ca domanassindriyaṃ pajahissanti",
     "aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahissanti",
     "^6-10-452 missing comma before 'no ca'"),
    ("aññindriyaṃ bhāvessanti no ca anaññātaññassāmītindriyaṃ bhāvittha",
     "aññindriyaṃ bhāvessanti, no ca anaññātaññassāmītindriyaṃ bhāvittha",
     "^6-10-477 missing comma before 'no ca'"),
]
KEPT = [   # real-word slips kept as written (reported); each occurs exactly once
    ("aññindriyañca bhavissanti", "^6-10-452 'bhavissanti' (will be) for 'bhāvessanti' (will develop): kept, "
                                  "«и будут способностью окончательного знания»"),
]


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append("rendered as meant: " + note)
    for old, note in KEPT:
        if old in text:
            SLIP_LOG.append("kept as written: " + note)
    return text


# =============================================================================================
# Lines and chapter
# =============================================================================================
FIXED = {
    "Pariññāvāro.": E.KH2_CFG["fixed"]["Pariññāvāro."],                                   # 2-02
    "Indriyayamakaṃ niṭṭhitaṃ.": B.YAMAKA_CLOSING_FRAME.format(title=B.YAMAKA_TITLES["Indriyayamakaṃ"]),
    "Yamakapakaraṇaṃ niṭṭhitaṃ.": B.YAMAKA_CLOSING_FRAME.format(title=B.BOOK_TITLE),
}
assert FIXED["Pariññāvāro."] == "Раздел о полном понимании."
assert FIXED["Indriyayamakaṃ niṭṭhitaṃ."] == "Парные вопросы о способностях завершены."
assert FIXED["Yamakapakaraṇaṃ niṭṭhitaṃ."] == "Парные вопросы завершены."

# Variants (all «вариант чтения»: a word differs): Pāli content -> the Russian it follows
VARIANT_ANCHORS = {
    "tayo puggalā (pī.)": cap("три " + MAGGASAMANGI),
    "aṭṭhamakañca tayo maggasamaṅgino ca (pī.)": "Кроме четырёх " + MAGGASAMANGI,
    "satta (sī. syā. ka.)": cap(NUM_NOM["aṭṭha"].split(" ")[0]),
    "pañca (sī. syā. ka.)": cap(NUM_NOM["cha"].split(" ")[0]),
}


def tr(text):
    """One Pāli line (block ID removed)."""
    if not text.strip():
        return ""
    if text in FIXED:
        return FIXED[text]
    if text.startswith("#"):
        return I1.heading(text)
    text = preprocess(text)
    m = I1.TAIL_RE.fullmatch(text)
    if m:
        return tr(m.group(1)) + f" ({I1.TAILS[m.group(2)]}){m.group(3)}"
    variants = A.VARIANT_RE.findall(text)
    ru = pj_line(A.VARIANT_RE.sub("", text))
    for v in variants:
        anchor = VARIANT_ANCHORS[v]
        assert ru.count(anchor) == 1, (anchor, ru)
        ru = ru.replace(anchor, anchor + " " + A.variant_ru(v), 1)
    return ru


def translate_text(src):
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr(body) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("5", "развивает"), ("5", "развивают"), ("5", "не развивает"), ("1", "развивает путь"),
    ("5", "осуществляет"), ("5", "осуществляют"), ("5", "не осуществляет"), ("5", "осуществляет прекращение"),
    ("5", "полностью понимает страдание, устраняет возникновение, осуществляет прекращение, развивает путь"),
    ("5", "восьмой ступени"), ("5", "пять личностей"), ("5", "семь личностей"), ("5", "восемь личностей"),
    ("5", "Невозвращающийся"), ("5", "путь невозвращения"), ("5", "архат"),
    ("2", "Способность познания непознанного следует постичь высшим знанием и полностью понять"),
]


def check_verbs(src, ru):
    assert "не полностью" not in ru, "negated parijānāti = «не понимает полностью» (2-02)"
    for p, r in zip(src.split("\n"), ru.split("\n")):
        for pali, rus in (("parijān", "полностью"), ("pajah", "устран"), ("bhāve", "разв|разовь"),
                          ("bhāvi", "разв"), ("sacchikar", "осуществ")):
            if pali in p:
                assert re.search(rus, r), (pali, p, r)


def finished_pairs():
    """(name, Pāli text, Russian text) of every other pi-6 chapter on disk with equal line counts."""
    out, skipped = [], []
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        p, r = (B.PALI_DIR / f.name).read_text(encoding="utf-8"), f.read_text(encoding="utf-8")
        (out if len(p.split("\n")) == len(r.split("\n")) else skipped).append((f.name, p, r))
    return out, [s[0] for s in skipped]


def shared_lines(src, ru, pairs):
    """Every Pāli line of this chapter that occurs in a finished chapter must come out byte-identical."""
    seen = {}
    for _, p, r in pairs:
        for a, b in zip(p.split("\n"), r.split("\n")):
            pa, rb = B.ID_ANY.sub("", a).strip(), B.ID_ANY.sub("", b).strip()
            if pa:
                seen.setdefault(pa, set()).add(rb)
    n, lines = 0, set()
    for a, b in zip(src.split("\n"), ru.split("\n")):
        pa, rb = B.ID_ANY.sub("", a).strip(), B.ID_ANY.sub("", b).strip()
        if pa in seen:
            assert seen[pa] == {rb}, f"shared line differs: {pa!r}\n  here {rb!r}\n  there {sorted(seen[pa])}"
            n += 1
            lines.add(pa)
    return n, len(lines)


def probe():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for n, line in enumerate(src.split("\n"), 1):
        body, _ = B.ID_RE.match(line).groups()
        try:
            print(f"{n}: {tr(body)}")
        except Exception as ex:  # noqa: BLE001
            print(f"{n}: {type(ex).__name__}: {str(ex)[:300]}")


def main():
    if "--probe" in sys.argv:
        probe()
        return
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(E.CROSSBOOK)
    A.check_crossbook(S3.CROSSBOOK)
    A.check_crossbook(I1.CROSSBOOK)
    A.check_crossbook(CROSSBOOK)
    C.check_crossbook_c()
    I1.check_members()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    for old, note in KEPT:
        assert src.count(old) == 1, f"kept pattern must occur once: {note}"
    SLIP_LOG.clear()
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    check_verbs(src, ru)
    nnum = sum(1 for s in SLIP_LOG if s.startswith("verb number"))
    assert nnum == 5, f"expected 5 verb-number slips (^6-10-454 x2, ^6-10-459, ^6-10-468 x2), got {nnum}"
    pairs, skipped = finished_pairs()
    sample = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
              for n in B.SAMPLE_FILES]
    A.consistency(sample + [(src, ru)])
    nshared, nuniq = shared_lines(src, ru, pairs)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    nseg = sum(1 for ln in ru.split("\n") if B.ID_ANY.search(ln))
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")), "segments", nseg)
    print(f"shared with finished chapters: {nshared} lines ({nuniq} distinct), all byte-identical; "
          f"{len(pairs)} chapters compared; skipped (line counts differ): {skipped}")
    for s in dict.fromkeys(SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; verb checks OK; consistency OK")


if __name__ == "__main__":
    main()
