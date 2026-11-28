"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-06-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra, anāgatavāra (future): (Kha) anulomaokāso, (Ga) anulomapuggalokāsā, (Gha) paccanīkapuggalo,
(Ṅa) paccanīkaokāso).

Every frame is imported, never retyped (and no imported file is edited):
  places   build_10-02_ru.tr_line(text, IN6_CFG): yattha … tattha … questions, chained "…pe…" questions,
           «В мире форм: там …» (3-01 ay_place_intro), Uppajjissati. / Natthi., mūlaka tails (10-01).
  persons  questions: build_2-01_ru.pv_question (Q_PERSON_PLACE / Q_PERSON of 7-01) and build_3-02_ru.pe_question
           («У кого где возникнет X, у того там возникнет Y… Z?»); answers: the family B frames of build_2-01_ru
           (PV_PRED, NO_CA_FRAME, PV_NO_CA_POS_FRAME, PV_NEITHER_FRAME, BOTH_FRAME) with the future person units of
           2-01 / 2-02 / 3-02 / 3-03 («тех, кто, переродившись в мире форм, достигнет окончательного угасания», «тех,
           кто живёт последней жизнью», «существ мира форм и существ мира без форм», «остальных …»), joined as
           build_2-01_ru.person_intro / build_3-02_ru.ay2_person_intro; 10-02 person attributes (IN_ATTR, IN_HAVE2,
           IN_ASSOC); 6-01 «сразу после данного ума возникнет последний ум»; 5-01 «обладающих последним умом».
NEW here (notes-10-06.md): FUT_GENDER «тех мужчин / женщин, которые, пройдя несколько существований в этом же
состоянии[ и переродившись с …], достигнут окончательного угасания»; attributes inside 2-01's «переродившись …»
(«с глазом и с невозмутимостью», «с радостью в мире форм»); «тех, у кого сразу после данного ума возникнет последний
ум, связанный с невозмутимостью».

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-06_ru.py
Probe:  python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-06_ru.py --probe
Import: importlib.import_module("build_10-06_ru")   (importing never writes any file)
Exposed for 10-07 …: fut_units(), fut_intro(), fut_sentence(s, subj), person_line(text, subj), tr_line(text),
FUT_GENDER, FUT_PASS, LAST_MIND_ASSOC.
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


def _optional(name):
    """Builders of chapters done in parallel (10-04, 10-05): imported only when they exist."""
    if (HERE / f"{name}.py").exists():
        return importlib.import_module(name)
    return None


I = importlib.import_module("build_10-01_ru")    # members, headings, mūlaka tails
P2 = importlib.import_module("build_10-02_ru")   # place driver, person attributes, associated-mind members
P3 = importlib.import_module("build_10-03_ru")   # (checks only: its sentences must agree with ours)
F = importlib.import_module("build_3-02_ru")     # future person units, pe_question («…, у того там … X… Y?»)
G = importlib.import_module("build_3-03_ru")     # "ye ca Xaṃ Yaṃ upapajjitvā parinibbāyissanti"
K6 = importlib.import_module("build_6-01_ru")    # «сразу после данного ума возникнет последний ум»
S = P2.S                                         # build_5-01_ru: «обладающих последним умом»
D, A3, C, E = I.D, I.A, I.C, F.E                 # build_2-01_ru, build_3-01_ru, build_7-01_ru, build_2-02_ru
CHAPTER = "10-06-indriyayamaka.md"
cap, lower1 = B.cap, C.lower1
SUBJ = I.IN_PV_SUBJ
PLANES = I.IN_PLANES                             # = build_3-01_ru.AY_PLANES
SLIP_LOG = []


# =============================================================================================
# Future person units (Pāli tokens -> Russian, "rel" = relative clause with a closing comma)
# =============================================================================================
def _unit(units, rx):
    return next(ru for r, ru, _ in units if r == rx)


YE_FUT = _unit(D.PERSON_UNITS, r"ye {P}aṃ upapajjitvā parinibbāyissanti")      # тех, кто, переродившись {in1}, …
YE_FUT2 = _unit(F.PERSON_UNITS_3_02, r"ye {P}aṃ {P}aṃ upapajjitvā parinibbāyissanti")
assert YE_FUT2 == YE_FUT.replace("{in1}", "{in1} и {in2}")
assert _unit(E.PERSON_UNITS_2_02, r"ye ca {P}aṃ upapajjitvā parinibbāyissanti") == YE_FUT          # "ca" = «и»
assert _unit(G.PERSON_UNITS_3_03, r"ye ca {P}aṃ {P}aṃ upapajjitvā parinibbāyissanti") == YE_FUT2
LAST_LIFE = _unit(D.PERSON_UNITS, r"pacchimabhavikānaṃ")                         # тех, кто живёт последней жизнью
LAST_MIND_HOLDERS = dict((u[0], u[1]) for u in S.SC_UNITS)["pacchimacittasamaṅgīnaṃ"]   # обладающих последним умом
ITARESAM = D.ITARESAM                                                            # остальных
REACH_SG = "достигнет окончательного угасания"                                  # 2-01
assert REACH_SG in YE_FUT
REACH_PL = "достигнут окончательного угасания"                                  # plural of 2-01 (ye purisā …)
# "ye purisā / yā itthiyo eteneva bhāvena katici bhave dassetvā [X upapajjitvā] parinibbāyissanti": aṭṭhakathā
# ^6-183 "etena purisabhāveneva … katici paṭisandhiyo gahetvā itthibhāvaṃ appatvāva parinibbāyissanti".
# Shaped like 5-01 "ye puthujjanā maggaṃ na paṭilabhissanti" = «тех обычных людей, которые не обретут путь» and
# 2-01's participle «переродившись …»; the gender nouns are 10-01's IN_GEN_PL (женщин / мужчин).
M5 = _optional("build_10-05_ru")                 # set in parallel by 10-05 (same Pāli): its wording is taken
FUT_PASS = M5.ETENEVA if M5 else "пройдя в этом же состоянии несколько существований"   # eteneva bhāvena katici bhave dassetvā
REBORN_PART = YE_FUT.split(", ")[2].replace(" {in1}", "")                       # «переродившись» (2-01)
assert REBORN_PART == "переродившись", REBORN_PART
FUT_GENDER = "тех {gen}, которые, {pas}, " + REACH_PL                            # no rebirth attribute
FUT_GENDER_ATTR = "тех {gen}, которые, {pas} и " + REBORN_PART + " {desc}, " + REACH_PL
GENDER_NOUN = {"purisā": I.IN_GEN_PL["purisa"], "itthiyo": I.IN_GEN_PL["itthī"]}
# yassa cittassa anantarā <A>sampayuttapacchimacittaṃ uppajjissati (6-01 frame «тех, у кого …»; 10-02 members)
SAMP_NOM = "связанный"                                                           # pi-1 «связанный со знанием»
assert P2.SAMP == "связанного"
LAST_MIND_ASSOC = "тех, у кого " + K6.LAST_MIND_ARISES + ", " + SAMP_NOM + " {instr}"
ANANTARA_RE = re.compile(r"yassa cittassa anantarā (" + "|".join(P2.IN_ASSOC) + r")sampayuttapacchimacittaṃ "
                         r"uppajjissati")
PRE = D._plane_re(PLANES)
PLANE_ACC = re.compile(PRE + "aṃ")
BEINGS = re.compile(PRE + "ānaṃ")
YE_TAIL = "eteneva bhāvena katici bhave dassetvā".split()


def _have(tok):
    """'sacakkhukā' / 'saghānakā' (nominative) -> «с глазом» (3-01 have_desc with 10-02 IN_HAVE2)."""
    if tok.endswith("ā"):
        return A3.have_desc(tok[:-1] + "ānaṃ", P2.IN_HAVE2)
    return None


def _ye_clause(toks, i):
    """'ye [ca] [purisā|itthiyo eteneva bhāvena katici bhave dassetvā] [attrs] [planes] [upapajjitvā]
    parinibbāyissanti' at toks[i] -> (Russian, next index) or None."""
    if toks[i] not in ("ye", "yā"):
        return None
    j = i + 1
    if j < len(toks) and toks[j] == "ca":
        j += 1
    gender = None
    if j < len(toks) and toks[j] in GENDER_NOUN:
        gender = GENDER_NOUN[toks[j]]
        if toks[j + 1:j + 1 + len(YE_TAIL)] != YE_TAIL:
            return None
        j += 1 + len(YE_TAIL)
    descs, planes = [], []
    while j < len(toks):
        if toks[j] in P2.IN_ATTR and toks[j] in ("upekkhāya", "somanassena"):
            descs.append(P2.IN_ATTR[toks[j]])
        elif _have(toks[j]):
            descs.append(_have(toks[j]))
        elif PLANE_ACC.fullmatch(toks[j]):
            planes.append(PLANES[PLANE_ACC.fullmatch(toks[j]).group(1)]["in"])
        else:
            break
        j += 1
    reborn = j < len(toks) and toks[j] == "upapajjitvā"
    if reborn:
        j += 1
    if j >= len(toks) or toks[j] != "parinibbāyissanti" or (bool(descs or planes) != reborn):
        return None
    where = A3.HAVE_JOIN.join(descs)
    if planes:
        where = (where + " " if where else "") + " и ".join(planes)      # 3-02 «{desc} {in1}», «{in1} и {in2}»
    if gender is None:
        if not planes and not descs:
            return None
        if not descs:                                                    # the 2-01 / 3-02 units themselves
            ru = (YE_FUT if len(planes) == 1 else YE_FUT2).format(in1=planes[0], in2=planes[-1])
            assert ru == YE_FUT.format(in1=where)
        else:
            ru = YE_FUT.format(in1=where)
    elif reborn:
        ru = FUT_GENDER_ATTR.format(gen=gender, pas=FUT_PASS, desc=where)
    else:
        ru = FUT_GENDER.format(gen=gender, pas=FUT_PASS)
    return ru, j + 1


def fut_units(intro):
    """Pāli intro (lower-cased, feminine forms normalised) -> [[Russian, rel], …], itaresaṃ merged as 2-01 / 3-02."""
    toks = lower1(intro).split()
    units, i = [], 0
    while i < len(toks):
        rest = " ".join(toks[i:])
        m = ANANTARA_RE.match(rest)
        if m:
            units.append([LAST_MIND_ASSOC.format(instr=A3.s_prep(P2.IN_ASSOC[m.group(1)])), True])
            i += len(m.group(0).split())
            continue
        if toks[i] == "pacchimacittasamaṅgīnaṃ":
            units.append([LAST_MIND_HOLDERS, False])
            i += 1
            continue
        if toks[i] == "pacchimabhavikānaṃ":
            units.append([LAST_LIFE, True])
            i += 1
            continue
        if toks[i] == "itaresaṃ":
            units.append([ITARESAM, False])
            i += 1
            continue
        y = _ye_clause(toks, i)
        if y:
            units.append([y[0], True])
            i = y[1]
            continue
        beings, j = [], i
        while j < len(toks) and BEINGS.fullmatch(toks[j]):                 # 3-02: one group «A и B»
            beings.append(PLANES[BEINGS.fullmatch(toks[j]).group(1)]["beings"])
            j += 1
        if beings:
            units.append([A3.ru_and(beings), False])
            i = j
            continue
        raise ValueError(f"person intro not parsed at {toks[i:]!r} in {intro!r}")
    out, k = [], 0
    while k < len(units):
        t, rel = units[k]
        if t == ITARESAM and k + 1 < len(units):
            nt, nrel = units[k + 1]
            t = ITARESAM + nt[3:] if nt.startswith("тех, кто") else f"{ITARESAM} {nt}"
            rel = nrel
            k += 1
        out.append([t, rel])
        k += 1
    return out


def fut_intro(intro, tattha=False):
    """Joined exactly as build_2-01_ru.person_intro (+ «там » as its PV_TAM)."""
    units = fut_units(intro)
    s = "У " + units[0][0]
    for i in range(1, len(units)):
        last = i == len(units) - 1
        s += ((", и " if units[i - 1][1] else " и ") if last else ", ") + "у " + units[i][0]
    return s + ("," if units[-1][1] else "") + " " + (D.PV_TAM if tattha else "")


# =============================================================================================
# Answer sentences (family B frames of build_2-01_ru.pv_sentence, with the future person intro)
# =============================================================================================
# ^6-10-309: "no ca tesaṃ somanassindriyaṃ na upapajjissati": upapajjati ("be reborn") for uppajjati ("arise"),
# a one-letter slip that makes another real word: kept as written (user rule), «переродится» (2-01 REBORN).
WRITTEN_VERBS = {"upapajjissati": {"sg": "переродится", "pl": "переродятся"}}
V6_RE = "(?:" + "|".join(WRITTEN_VERBS) + "|" + D.V_RE + ")"
S1_RE = re.compile(r"(?P<intro>.+?) " + D._T.format(n="t1") + r" (?P<x>\S+) (?P<n1>na |n)?(?P<v1>" + V6_RE
                   + r"), no ca " + D._T.format(n="t2") + r" (?P<y>\S+) (?P<n2>na |n)?(?P<v2>" + V6_RE + r")")
S2_RE = re.compile(r"(?P<intro>.+?) " + D._T.format(n="t1") + r" (?P<x>\S+) ca (?P<n1>na |n)?(?P<v1>" + V6_RE
                   + r") (?P<y>\S+) ca (?P<n2>na |n)?(?P<v2>" + V6_RE + r")")


def verb6(v, g, neg=False):
    if v in WRITTEN_VERBS:
        SLIP_LOG.append(f"'{v}' (be reborn) for 'uppajjissati' (arise): kept as written, «{WRITTEN_VERBS[v]['sg']}»")
        return ("не " if neg else "") + WRITTEN_VERBS[v]["pl" if g == "pl" else "sg"]
    return D.verb(v, g, neg)


def _p(v, x, neg):
    return D.PV_PRED.format(v=verb6(v, x["g"], neg), x=x["nom"])


def fut_sentence(s, subj=SUBJ):
    """One Pāli person answer sentence (no final '.') -> Russian sentence with '.'."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    s = P2.fem_norm(D._norm(s))
    m = S1_RE.fullmatch(s)
    if m and m.group("t1").startswith("tesaṃ"):
        head = fut_intro(m.group("intro"), "tattha" in m.group("t1"))
        x, y = subj[m.group("x")], subj[m.group("y")]
        tail = (D.PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
            res=C.RES[m.group("t2")],
            **{("pred" if m.group("n2") else "neg_pred"): _p(m.group("v2"), y, not m.group("n2"))})
        return cap(head + _p(m.group("v1"), x, bool(m.group("n1"))) + tail) + "."
    m = S2_RE.fullmatch(s)
    if m and m.group("t1").startswith("tesaṃ"):
        head = fut_intro(m.group("intro"), "tattha" in m.group("t1"))
        x, y = subj[m.group("x")], subj[m.group("y")]
        if m.group("n1") and m.group("n2"):
            f1, f2 = verb6(m.group("v1"), x["g"]), verb6(m.group("v2"), y["g"])
            both = (D.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"]) if f1 == f2
                    else D.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"]))
        else:
            both = C.BOTH_FRAME.format(p1=_p(m.group("v1"), x, bool(m.group("n1"))),
                                       p2=_p(m.group("v2"), y, bool(m.group("n2"))))
        return cap(head + both) + "."
    raise ValueError(f"person answer not parsed: {s!r}")


# ^6-10-301: "… tesaṃ tattha itthindriyañca uppajjissati. Somanassindriyañca uppajjissati." A stray full stop
# inside the «и …, и …» answer: kept as written (user rule) -> «… там и возникнет X. И возникнет Y.»
BOTH_SEP = C.BOTH_FRAME.format(p1="\0", p2="\1").split("\0")[1].split("\1")[0]      # «, и »
assert BOTH_SEP == ", и ", BOTH_SEP
STRAY_STOP_RE = re.compile(r"(?:^|(?<=\. ))(?P<a>[^.]+ tesaṃ tattha \S+ñca (?:na )?uppajjissati)\. (?P<b>[A-ZĀĪŪṬḌṆÑṄ]\S+ñca "
                           r"(?:na )?uppajjissati)")


def answers(text, subj=SUBJ):
    text = text.strip()
    m = STRAY_STOP_RE.search(text)
    if m:
        SLIP_LOG.append("stray full stop inside a «и …, и …» answer (kept as written): " + m.group(0)[-60:])
        whole = fut_sentence(m.group("a") + " " + lower1(m.group("b")), subj)
        assert whole.count(BOTH_SEP) == 1, whole
        first, second = whole.split(BOTH_SEP)
        stray = first + ". " + cap(BOTH_SEP[2:] + second)
        before = text[: m.start()].strip()
        after = text[m.end():].strip()
        assert after == ".", after
        return " ".join(([answers(before, subj)] if before else []) + [stray])
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text):
        assert s.endswith("."), s
        out.append(fut_sentence(s[:-1], subj))
    return " ".join(out)


def person_line(text, subj=SUBJ):
    """One line of a person / person-place section (block ID removed)."""
    m = I.TAIL_RE.fullmatch(text)
    if m:
        return person_line(m.group(1), subj) + f" ({I.TAILS[m.group(2)]}){m.group(3)}"
    label = ""
    m = I.LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
        if (m.group(1) == "Ka") == (" vā pana " in text):
            SLIP_LOG.append(f"label ({m.group(1)}) does not match the question (kept as written): {text[:60]}")
    if "?" not in text:
        return label + answers(text, subj)
    q, _, rest = text.partition("?")
    if "…pe… " in q:
        ru_q = F.pe_question(q, subj)[0]
    else:
        ru_q = D.pv_question(lower1(q.strip()), subj)[0]
    assert ru_q.endswith("?"), ru_q
    return label + ru_q + (" " + answers(rest, subj) if rest.strip() else "")


# =============================================================================================
# Lines and sections
# =============================================================================================
SLIPS = [   # (old, new, note): plain slips rendered as meant; each must occur exactly once in the chapter
    ("Pacchimacittasamaṅgīna tesaṃ", "Pacchimacittasamaṅgīnaṃ tesaṃ",
     "^6-10-314: 'Pacchimacittasamaṅgīna' = Pacchimacittasamaṅgīnaṃ (spelling slip)"),
    ("tattha ghānindriyaṃ na uppajjissati no ca tattha upekkhindriyaṃ",
     "tattha ghānindriyaṃ na uppajjissati, no ca tattha upekkhindriyaṃ",
     "^6-10-318: missing comma before 'no ca' (rendered with it)"),
]
PERSON_SECTIONS = ("anulomapuggalokāsā", "paccanīkapuggalo")
IN6_CFG = dict(P2.IN2_CFG)
IN6_CFG.update({"fixed": dict(P2.IN2_CFG["fixed"]), "variant_anchors": dict(P2.IN2_CFG["variant_anchors"])})


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


def tr_line(text, persons=False):
    if not text.strip():
        return ""
    if text.startswith("#"):
        return I.heading(text)
    text = preprocess(text)
    if persons:
        return person_line(text)
    if text.startswith("(Kha) ") and " vā pana " not in text:
        SLIP_LOG.append(f"label (Kha) on a question without 'vā pana' (kept as written): {text[:60]}")
    return P2.tr_line(text, IN6_CFG)


def translate_text(src):
    out, persons = [], False
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        if body.startswith("#"):
            persons = body.split()[-1] in PERSON_SECTIONS
        out.append(tr_line(body, persons) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("1", "связанный со знанием"), ("1", "радостью"), ("1", "невозмутимостью"), ("2", "женщин"), ("2", "мужчин"),
    ("2", "окончательного угасания"), ("5", "состоянии"),
]
TAIL_ANY = re.compile(r" ?\([^()]*\)\.?$")
SENT_SPLIT = re.compile(r"(?<=[.?]) (?=\S)")


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, within the chapter and against every other finished pi-6
    chapter (and the sample)."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent within {CHAPTER}: {pb!r}"
        mine[pb] = rb
    shared, files = 0, set()
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb and pb in mine:
                assert mine[pb] == rb, f"differs from {f.name}: {pb!r}\n  {rb!r}\n  {mine[pb]!r}"
                shared += 1
                files.add(f.name)
    return shared, sorted(files)


def cross_sentences(name, subj):
    """Every person answer sentence of a finished chapter that fut_sentence() parses must come out byte-identical
    with that chapter's Russian sentence. Returns (agreeing, [differences])."""
    pf, rf = B.PALI_DIR / name, B.OUT_DIR / name
    if not rf.exists():
        return 0, []
    same, diff = 0, []
    log = len(SLIP_LOG)
    for p, r in zip(pf.read_text(encoding="utf-8").split("\n"), rf.read_text(encoding="utf-8").split("\n")):
        pb = TAIL_ANY.sub("", B.ID_ANY.sub("", p).strip())
        rb = TAIL_ANY.sub("", B.ID_ANY.sub("", r).strip())
        ps, rs = SENT_SPLIT.split(pb), SENT_SPLIT.split(rb)
        if len(ps) != len(rs):
            continue
        for a, b in zip(ps, rs):
            if " tesaṃ" not in a and " tāsaṃ" not in a or not a.endswith("."):
                continue
            a = I.LABEL_RE.sub(r"\2", a) if a.startswith("(") else a
            try:
                mine = fut_sentence(a[:-1], subj)
            except (ValueError, KeyError):
                continue
            if mine == b:
                same += 1
            else:
                diff.append((name, a, b, mine))
    del SLIP_LOG[log:]
    return same, diff


def check_with_10_05():
    """Every future person unit settled by build_10-05_ru (IN5_UNITS) comes out byte-identical here."""
    if not M5:
        return 0
    n = 0
    for rx, ru, rel in M5.IN5_UNITS:
        pali = re.sub(r"\\(.)", r"\1", rx)
        assert fut_units(pali) == [[ru, rel]], (pali, fut_units(pali), ru)
        n += 1
    assert (M5.FINAL_PL, M5.REBORN_GER, M5.SAMP_NOM) == (REACH_PL, REBORN_PART, SAMP_NOM)
    return n


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(A3.CROSSBOOK)
    D.check_crossbook(I.CROSSBOOK)
    D.check_crossbook(P2.CROSSBOOK)
    D.check_crossbook(F.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    I.check_members()
    n5 = check_with_10_05()
    # the frames must agree with the finished chapters that have the same Pāli sentences
    report = []
    for name, subj, strict in (("3-02-ayatanayamaka.md", A3.AY_PV_SUBJ, True),
                               ("3-03-ayatanayamaka.md", A3.AY_PV_SUBJ, True),
                               ("10-03-indriyayamaka.md", SUBJ, True),
                               ("10-04-indriyayamaka.md", SUBJ, False),
                               ("10-05-indriyayamaka.md", SUBJ, False)):
        same, diff = cross_sentences(name, subj)
        report.append(f"{name}: {same} sentences identical, {len(diff)} different")
        for d in diff[:6]:
            print("DIFF", d[0], "\n  pali:", d[1], "\n  theirs:", d[2], "\n  mine:  ", d[3])
        assert not (strict and diff), f"frames differ from {name}"
    for mod in ("build_10-04_ru", "build_10-05_ru"):
        report.append(f"{mod}: {'imported' if _optional(mod) else 'not present'}")
    report.append(f"build_10-05_ru.IN5_UNITS: {n5} units identical")
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    shared, files = check_against_finished(src, ru)
    if "--dry" in sys.argv:
        print(ru)
        return
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")),
          "| lines shared with finished chapters:", shared, files)
    for r in report:
        print(r)
    for s in dict.fromkeys(SLIP_LOG + P2.SLIP_LOG + I.SLIP_LOG + D.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; member asserts OK; per-line checks OK; consistency OK")


def probe():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ok = bad = 0
    persons = False
    for n, line in enumerate(src.split("\n"), 1):
        body, _ = B.ID_RE.match(line).groups()
        if body.startswith("#"):
            persons = body.split()[-1] in PERSON_SECTIONS
        try:
            tr_line(body, persons)
            ok += 1
        except Exception as e:   # noqa: BLE001
            bad += 1
            print(n, "--", type(e).__name__, str(e)[:220])
    print(f"{CHAPTER}: {ok} lines translated, {bad} not covered")


if __name__ == "__main__":
    if "--probe" in sys.argv:
        probe()
    else:
        main()
