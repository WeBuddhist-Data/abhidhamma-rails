"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-09-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra, (5) Paccuppannānāgatavāro: (Ka) anulomapuggalo, (Kha) anulomaokāso, (Ga) anulomapuggalokāsā).

Present + future ("yassa X uppajjati tassa Y uppajjissatīti?"). The closest finished shape is 3-03 (Āyatana, the
same section): its person units and wording are reused through the Indriya builders (imported, never edited):
  members, headings, mūlaka tails   build_10-01_ru (IN_PV_SUBJ, TAIL_RE, TAILS, IN_GEN_PL)
  attributes, moments, chain Qs     build_10-02_ru (IN_ATTR, IN_HAVE2, IN_ASSOC, moment(), chain_question(),
                                    tr_line(text, IN2_CFG) for the place section and headings)
  person / place driver             build_10-03_ru (in_units, moments(), pv_norm, S1_RE / S2_RE, in_pv_question)
                                    on build_5-01_ru.pv_intro («A, B и C»; «, когда они перерождаются»; «этого ума»)
  future person units               build_10-07_ru.MY_UNITS (= build_10-05_ru IN5_UNITS wording: «тех мужчин, которые,
                                    пройдя в этом же состоянии несколько существований, …»; «тех, у кого сразу после
                                    данного ума возникнет последний ум, связанный с …»)
  two planes, «когда перерождаются»  build_3-03_ru (_YE2, WHEN_REBORN)
  family B frames                   build_2-01_ru (PV_Q, PV_PRED, verb(), BOTH_FRAME via 7-01)

Exposed for 10-10 / 10-11 (paccanīka parts of the same section):
  NOW_FUT_UNITS (regex, Russian, kind), now_fut_units(intro), now_fut_intro(intro, tattha), pv_sentence(s, subj),
  question(q, subj), tr_line(text, subj), translate_text(src), FIXED_10_09, SADISAM

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-09_ru.py [--probe]
Import: importlib.import_module("build_10-09_ru")   (importing never writes any file)
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

I = importlib.import_module("build_10-01_ru")    # members, headings, mūlaka tails
P2 = importlib.import_module("build_10-02_ru")   # attributes, moments, chain questions, place driver
P3 = importlib.import_module("build_10-03_ru")   # person / place driver
M7 = importlib.import_module("build_10-07_ru")   # future person units (10-05 / 10-07 wording)
F3 = importlib.import_module("build_3-03_ru")    # Āyatana present + future (same section)
D = I.D                                          # build_2-01_ru: family B
A3 = I.A                                         # build_3-01_ru: planes, have_desc, REBORN
C = I.C                                          # build_7-01_ru: person / place shape
S = P3.S                                         # build_5-01_ru: pv_intro
CHAPTER = "10-09-indriyayamaka.md"
cap, lower1 = B.cap, C.lower1
SUBJ = I.IN_PV_SUBJ
PL = A3.AY_PLANES
SLIP_LOG = []

# =============================================================================================
# Person / time units of the present + future section
# =============================================================================================
PLANE_RX = D._plane_re(PL)                       # all Āyatana / Indriya planes (kāmāvacar, rūpāvacar … as 3-03)
ITARESAM = S.A.ITARESAM                          # «остальных»
REBORN = A3.REBORN                               # «тех, кто перерождается {desc}» (3-01)
_LAST_REBORN = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"pacchimabhavikānaṃ {P}aṃ upapajjantānaṃ")
assert _LAST_REBORN == "тех, кто в последний раз перерождается {in1}", _LAST_REBORN
LAST_REBORN_DESC = _LAST_REBORN.replace("{in1}", "{desc}")   # "pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ"
assert REBORN.endswith(" {desc}")

# NEW (notes-10-09.md): "ye ca purisā / yā ca itthiyo <upekkhāya | somanassena | Xaṃ [Yaṃ]> upapajjitvā
# parinibbāyissanti" (no "eteneva …") = «тех мужчин / женщин, которые, переродившись <с невозмутимостью | в мире форм
# и в мире без форм>, достигнут окончательного угасания»: 10-05 / 10-07 «тех мужчин, которые, …, достигнут …» with
# the 2-01 / 3-03 «переродившись {in1}[ и {in2}]» and the 10-02 attributes.
GENDER_FRAME = "тех {noun}, которые, " + M7._REBORN_ABS + ", " + M7._PARINIB_PL
assert M7._REBORN_ABS == "переродившись {desc}" and M7._PARINIB_PL == "достигнут окончательного угасания"
assert F3._YE2 == "тех, кто, " + M7._REBORN_ABS.format(desc="{in1} и {in2}") + ", " + M7._PARINIB_SG
GENDER_UNITS = []
for _g, (_rel, _noun) in M7.GENDER_NOUN.items():
    for _attr in ("upekkhāya", "somanassena"):
        GENDER_UNITS.append((rf"{_rel} (?:ca )?{_g} {_attr} upapajjitvā parinibbāyissanti",
                             GENDER_FRAME.format(noun=_noun, desc=P2.IN_ATTR[_attr]), "rel"))
    GENDER_UNITS.append((rf"{_rel} (?:ca )?{_g} {{P}}aṃ {{P}}aṃ upapajjitvā parinibbāyissanti",
                         GENDER_FRAME.format(noun=_noun, desc="{in1} и {in2}"), "rel"))
    GENDER_UNITS.append((rf"{_rel} (?:ca )?{_g} {{P}}aṃ upapajjitvā parinibbāyissanti",
                         GENDER_FRAME.format(noun=_noun, desc="{in1}"), "rel"))

# plane units of build_2-01_ru (D.PERSON_UNITS) and build_3-03_ru (two planes after "ye ca"), on the Āyatana planes
PLANE_UNITS = [(rx, ru, ("rel" if rel else "noun")) for rx, ru, rel in D.PERSON_UNITS if "{P}" in rx]
PLANE_UNITS.insert(0, (r"ye ca {P}aṃ {P}aṃ upapajjitvā parinibbāyissanti", F3._YE2, "rel"))
PLANE_UNITS[:0] = GENDER_UNITS
# "Kāmāvacarā cavantānaṃ …" / "Catuvokārā pañcavokārā cavantānaṃ" / "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ"
_PLANE_RX = [(re.compile(rx.replace("{P}", PLANE_RX)), ru, kind) for rx, ru, kind in PLANE_UNITS]

# future person units of 10-05 / 10-07 (eteneva bhāvena …; ye sacakkhukā upekkhāya …; yassa cittassa anantarā …)
_M7_RX = M7._MY_RX


def _plane_unit(m, ru):
    g = [PL[x] for x in m.groups()] + [{"in": "", "beings": ""}] * 2
    return ru.format(in1=g[0]["in"], in2=g[1]["in"], b1=g[0]["beings"], b2=g[1]["beings"])


def _desc_run(toks, i):
    """Descriptor keys starting at toks[i] (build_10-03_ru._desc_at), and the next index."""
    keys = []
    while i < len(toks):
        d = P3._desc_at(toks, i)
        if not d:
            break
        keys.append(d[1])
        i += d[2]
    return keys, i


def _person_at(toks, i):
    """Descriptor clauses: "[pacchimabhavikānaṃ] <desc …> [<plane>aṃ] upapajjantānaṃ" -> (Russian, next index)."""
    last = toks[i] == "pacchimabhavikānaṃ"
    keys, j = _desc_run(toks, i + 1 if last else i)
    if not keys or j >= len(toks):
        return None
    where = ""
    m = re.fullmatch(PLANE_RX + "aṃ", toks[j])
    if m and j + 1 < len(toks):
        where, j = " " + PL[m.group(1)]["in"], j + 1          # «… без глаза в мире чувственных желаний» (3-03)
    if toks[j] not in P3.REBORN_VERBS:
        return None
    frame = LAST_REBORN_DESC if last else REBORN
    if toks[j] == "uppajjantānaṃ":
        # uppajjati ("arise") for upapajjati ("be reborn"): a real word with another meaning, kept as written
        # (build_10-03_ru.REBORN_VERBS)
        SLIP_LOG.append("'uppajjantānaṃ' (arising) for 'upapajjantānaṃ' (being reborn): kept as written")
        frame = frame.replace("перерождается", D.verb("uppajjati", "sg"))
    desc = P3.desc_clause(keys) + where
    return frame.format(desc=desc), j + 1


def _moment_at(toks, i):
    """"<assoc>…pacchimacittassa uppādakkhaṇe" (build_10-02_ru.moment: «в момент возникновения последнего ума,
    связанного с …»)."""
    if i + 1 < len(toks) and "pacchimacittassa" in toks[i] and toks[i + 1] in P2.KHANA:
        mo = P2.moment(toks[i], toks[i + 1])
        if mo:
            return list(mo), i + 2
    return None


def now_fut_units(intro):
    """Intro -> build_5-01_ru units: this section's units first, the stretches between them through
    build_10-03_ru.in_units (attributes, then build_5-01_ru.sc_units); itaresaṃ merged as build_5-01_ru.sc_units."""
    toks = lower1(intro).replace(",", "").split(" ")
    units, rest, i = [], [], 0

    def flush():
        if rest:
            units.extend(P3.in_units(" ".join(rest)))
            rest.clear()

    while i < len(toks):
        s = " ".join(toks[i:])
        hit = None
        for rx, ru, kind in _M7_RX:
            m = rx.match(s)
            if m and (m.end() == len(s) or s[m.end()] == " "):
                hit = ([ru, kind], i + len(s[:m.end()].split(" ")))
                break
        if hit is None:
            for rx, ru, kind in _PLANE_RX:
                m = rx.match(s)
                if m and (m.end() == len(s) or s[m.end()] == " "):
                    hit = ([_plane_unit(m, ru), kind], i + len(s[:m.end()].split(" ")))
                    break
        if hit is None:
            p = _person_at(toks, i)
            if p:
                hit = ([p[0], "rel"], p[1])
        if hit is None:
            mo = _moment_at(toks, i)
            if mo:
                hit = mo
        if hit is None:
            rest.append(toks[i])
            i += 1
            continue
        flush()
        units.append(hit[0])
        i = hit[1]
    flush()
    out = []
    for ru, kind in units:                          # build_5-01_ru.sc_units: «остальных, кто …»
        prev = out[-1] if out else None
        if prev and prev[0] == ITARESAM and prev[1] == "noun":
            if kind == "rel" and ru.startswith("тех, кто"):
                prev[:] = [ITARESAM + ru[3:], "rel"]
                continue
            if kind == "noun":
                prev[:] = [f"{ITARESAM} {ru}", "noun"]
                continue
            if kind == "part":
                prev[:] = [f"{ITARESAM}, {ru[1]}", "rel"]
                continue
        out.append([ru, kind])
    return out


def now_fut_intro(intro, tattha=False):
    """build_5-01_ru.pv_intro with build_10-03_ru's moments / attributes and this section's units."""
    with P3.moments():
        S.sc_units = now_fut_units          # restored by moments() on exit
        return S.pv_intro(intro, tattha)


NOW_FUT_UNITS = PLANE_UNITS + [(rx.pattern, ru, kind) for rx, ru, kind in _M7_RX]


# =============================================================================================
# Sentences (build_10-07_ru.pv_sentence with now_fut_intro)
# =============================================================================================
def norm(s):
    """build_10-03_ru.pv_norm (tāsaṃ, -antīnaṃ, Xñca) and itarāsaṃ = itaresaṃ (one Russian form)."""
    return P3.pv_norm(re.sub(r"\b([Ii])tarāsaṃ\b", r"\1taresaṃ", s))


def _pred(v, x, neg):
    return D.PV_PRED.format(v=D.verb(v, x["g"], bool(neg)), x=x["nom"])


# "tesaṃ tattha manindriyaṃ uppajjissati cakkhundriyañca uppajjati" (^6-10-376): the first "ca" is missing; kept
# as written: «там возникнет X и возникает Y» (no «и …, и …»).
S3_RE = re.compile(r"(?P<intro>.+?) " + S._T.format(n="t1") + rf" (?P<x>{P3.NAMES}) (?P<v1>" + D.V_RE
                   + rf") (?P<y>{P3.NAMES}) ca (?P<v2>" + D.V_RE + r")")
ONE_CA_FRAME = "{p1} и {p2}"


def _head(m):
    if m.group("t1").startswith("tesaṃ"):
        return now_fut_intro(m.group("intro"), "tattha" in m.group("t1"))
    return S.place_intro(m.group("intro"))


def pv_sentence(s, subj=SUBJ):
    """One Pāli answer sentence (no final '.') -> Russian sentence with '.'."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    s = norm(s)
    m = P3.S1_RE.fullmatch(s)
    if m:
        x, y = subj[m.group("x")], subj[m.group("y")]
        v2 = D.verb(m.group("v2"), y["g"], not m.group("n2"))      # "no ca": the predicate is denied for Y
        tail = (D.PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
            res=C.RES[m.group("t2")], **{("pred" if m.group("n2") else "neg_pred"): D.PV_PRED.format(v=v2, x=y["nom"])})
        return _head(m) + _pred(m.group("v1"), x, m.group("n1")) + tail + "."
    m = P3.S2_RE.fullmatch(s)
    if m:
        x, y = subj[m.group("x")], subj[m.group("y")]
        if m.group("n1") and m.group("n2"):
            f1, f2 = D.verb(m.group("v1"), x["g"]), D.verb(m.group("v2"), y["g"])
            both = (D.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"]) if f1 == f2
                    else D.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"]))
        else:
            both = C.BOTH_FRAME.format(p1=_pred(m.group("v1"), x, m.group("n1")),
                                       p2=_pred(m.group("v2"), y, m.group("n2")))
        return _head(m) + both + "."
    m = S3_RE.fullmatch(s)
    if m:
        SLIP_LOG.append("^6-10-376 'manindriyaṃ uppajjissati cakkhundriyañca uppajjati': first 'ca' missing; "
                        "kept as written, «возникнет X и возникает Y»")
        x, y = subj[m.group("x")], subj[m.group("y")]
        return _head(m) + ONE_CA_FRAME.format(p1=_pred(m.group("v1"), x, None), p2=_pred(m.group("v2"), y, None)) + "."
    raise ValueError(f"pavatti answer not parsed: {s!r}")


# =============================================================================================
# Questions
# =============================================================================================
def question(q, subj=SUBJ):
    """Pāli question (no '?') -> Russian question with '?'."""
    body = q.strip()
    if ", tassa " in body:
        # ^6-10-369 "yassa vā pana somanassindriyaṃ uppajjissati, tassa …": a comma the parallels lack; the Russian
        # frame «А у кого …, у того …?» has a comma in that place anyway, so the line reads the same.
        SLIP_LOG.append("^6-10-369 'uppajjissati, tassa': stray comma (the Russian frame has a comma there anyway)")
        body = body.replace(", tassa ", " tassa ")
    m = P2.CHAIN_RE.fullmatch(body + "?")
    if m:
        return P2.chain_question(m, subj)
    m = M7.CHAIN_PP_RE.fullmatch(lower1(body))
    if m:
        return M7.question(body, subj)
    return P3.in_pv_question(body, subj)


# =============================================================================================
# Lines
# =============================================================================================
SADISAM = "Так же"                                # "(Sadisaṃ)": the same as the line before (English rails "The same")
FIXED_10_09 = {
    "Yassa cakkhundriyaṃ uppajjati tassa purisindriyaṃ uppajjissatīti? (Sadisaṃ )": None,   # filled below
}
SENT_RE = M7.SENT_RE


def tr_line(text, subj=SUBJ):
    """Translate one Pāli line (block ID removed)."""
    if not text.strip():
        return ""
    if text.startswith("#") or "…Pe…" in text:
        return P2.tr_line(text, P2.IN2_CFG)
    if text in FIXED_10_09:
        return FIXED_10_09[text]
    m = I.TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), subj) + f" ({I.TAILS[m.group(2)]}){m.group(3)}"
    label = ""
    m = P3.LABEL_RE.fullmatch(text)
    if m:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    out, pos = [], 0
    while pos < len(text):
        ms = SENT_RE.match(text, pos)
        if not ms:
            raise ValueError(f"line not segmented at {text[pos:]!r}")
        seg = ms.group(1)
        pos = ms.end()
        out.append(question(seg[:-1], subj) if seg.endswith("?") else pv_sentence(seg[:-1], subj))
    return label + " ".join(out)


# "(Sadisaṃ )": a stray space before ")" (spacing only): «(Так же)».
_q15 = "Yassa cakkhundriyaṃ uppajjati tassa purisindriyaṃ uppajjissatīti?"
FIXED_10_09[_q15 + " (Sadisaṃ )"] = tr_line(_q15) + f" ({SADISAM})"


def translate_text(src, subj=SUBJ):
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body, subj) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("4", "мужчин"), ("4", "женщин"), ("2", "перерождаются"), ("1", "связанный со знанием"),
    ("5", "окончательного угасания"), ("2", "сразу после"), ("1", "в мире чувственных желаний"),
    ("1", "в мире форм"), ("1", "в мире без форм"), ("5", "момент возникновения"), ("5", "момент распада"),
]


def _segments(body):
    m = I.TAIL_RE.fullmatch(body)
    body = m.group(1) if m else body
    m = P3.LABEL_RE.fullmatch(body)
    body = m.group(2) if m else body
    return SENT_RE.findall(body)


# Units the earlier Indriya parsers split, read here as one person group (no finished chapter has these intros):
#  - "Itaresaṃ sacakkhukānaṃ upapajjantānaṃ": theirs «У остальных и у тех, кто перерождается с глазом,»; here
#    «У остальных, кто перерождается с глазом,» (build_5-01_ru.sc_units merge; 3-03 l. 6 for the same Pāli shape);
#  - "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ": theirs «У тех, кто живёт последней жизнью, и у тех, кто
#    перерождается женщиной,»; here «У тех, кто в последний раз перерождается женщиной,» (one group, as 2-01
#    "pacchimabhavikānaṃ Xaṃ upapajjantānaṃ" «тех, кто в последний раз перерождается {in}»; English rails "women in
#    their final existence being reborn").
KNOWN_SPLIT_PALI = re.compile(r"[Pp]acchimabhavikānaṃ (?:na )?(?:itthīnaṃ|purisānaṃ) ")
KNOWN_SPLIT_RU = (f"{ITARESAM} и у тех, кто", f"{ITARESAM}, у тех, кто")


def _known_split(seg, theirs, mine):
    """The only accepted difference: their unmerged groups, everything else identical."""
    if KNOWN_SPLIT_PALI.search(seg):
        return True
    fixed = theirs
    for a in KNOWN_SPLIT_RU:
        fixed = fixed.replace(a, f"{ITARESAM}, кто")
    return fixed == mine


def check_with_builders(src):
    """Every sentence / question that build_10-07_ru or build_10-03_ru parses comes out byte-identical here."""
    same, merged = {}, {}
    for name, qf, sf in (("build_10-07_ru", M7.question, M7.pv_sentence),
                         ("build_10-03_ru", P3.in_pv_question, P3.in_pv_sentence)):
        n = 0
        for line in src.split("\n"):
            body, _ = B.ID_RE.match(line).groups()
            if not body.strip() or body.startswith("#") or "…Pe…" in body or body in FIXED_10_09:
                continue
            for seg in _segments(body):
                try:
                    theirs = qf(seg[:-1]) if seg.endswith("?") else sf(seg[:-1])
                except (ValueError, KeyError):
                    continue
                mine = question(seg[:-1]) if seg.endswith("?") else pv_sentence(seg[:-1])
                if theirs != mine:
                    assert _known_split(seg, theirs, mine), (name, seg, theirs, mine)
                    merged[name] = merged.get(name, 0) + 1
                    continue
                n += 1
        same[name] = n
    return same, merged


def compare_lines(modname, src, ru):
    """Lines that another Indriya builder (10-08, run in parallel) translates must come out the same."""
    if not (HERE / f"{modname}.py").exists():
        return None
    M = importlib.import_module(modname)
    same, known = 0, 0
    for p, r in zip(src.split("\n"), ru.split("\n")):
        body, bid = B.ID_RE.match(p).groups()
        if not body.strip():
            continue
        try:
            theirs = M.tr_line(body) + (bid or "")
        except Exception:  # noqa: BLE001  (their parser does not cover this line)
            continue
        if theirs != r and KNOWN_SPLIT_PALI.search(p):     # a unit their chapter does not have (see KNOWN_SPLIT_PALI)
            known += 1
            continue
        assert theirs == r, f"{modname} differs:\n{p}\n  mine:   {r}\n  theirs: {theirs}"
        same += 1
    return same, known


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, within the chapter and against every other finished pi-6
    chapter (and the sample)."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent within {CHAPTER}: {pb!r}"
        mine[pb] = rb
    shared, files, distinct = 0, set(), set()
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
                distinct.add(pb)
    lines = sum(1 for p in src.split("\n") if B.ID_ANY.sub("", p).strip() in distinct)
    return shared, sorted(files), lines


def check_frames():
    """The reused frames reproduce the finished chapters' renderings (3-03, 5-01, 9-01) of the same intros."""
    samples = {
        "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
        "upapajjantānaṃ": "У тех, кто в последний раз перерождается в существовании с пятью составляющими, и у тех, "
                          "кто, переродившись в мире без форм, достигнет окончательного угасания, когда они "
                          "перерождаются, ",                                                            # 3-03 l. 6
        "Kāmāvacarā cavantānaṃ aghānakānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ":
            "У тех, кто умирает в мире чувственных желаний, у тех, кто перерождается без носа в мире чувственных "
            "желаний, и у существ мира форм и существ мира без форм ",                                 # 3-03 l. 87
        "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacaraṃ upapajjantānaṃ":
            "У тех, кто в последний раз перерождается в мире чувственных желаний, и у тех, кто перерождается в мире "
            "форм, ",                                                                                   # 3-03 l. 64
        "Itaresaṃ sacakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ":
            "У остальных, кто перерождается с глазом в мире чувственных желаний, ",                    # 3-03 l. 64
        "Itaresaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe":
            "У остальных, кто перерождается, и в течение жизни в момент возникновения ума ",           # 5-01 l. 579
    }
    for pali, ru in samples.items():
        got = now_fut_intro(pali)
        assert got == ru, (pali, got, ru)


def probe():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for n, line in enumerate(src.split("\n"), 1):
        body, bid = B.ID_RE.match(line).groups()
        try:
            print(n, tr_line(body) + (bid or ""))
        except Exception as e:  # noqa: BLE001
            print(n, "FAIL", type(e).__name__, str(e)[:300])


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(I.A.CROSSBOOK)
    D.check_crossbook(I.CROSSBOOK)
    D.check_crossbook(P2.CROSSBOOK)
    D.check_crossbook(P3.CROSSBOOK)
    D.check_crossbook(M7.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    I.check_members()
    check_frames()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    same, merged = check_with_builders(src)
    shared, files, own = check_against_finished(src, ru)
    c8 = compare_lines("build_10-08_ru", src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("segments identical with the Indriya builders that parse them:", same,
          "| differing only by the «У остальных, кто …» merge:", merged)
    print("lines identical with build_10-08_ru:", "not found" if c8 is None else c8)
    print(f"{own} lines of this chapter occur in finished chapters ({shared} matches), all identical:", files)
    for s in dict.fromkeys(SLIP_LOG + P3.SLIP_LOG + P2.SLIP_LOG + I.SLIP_LOG + D.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; member asserts OK; frame asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    if "--probe" in sys.argv:
        probe()
    else:
        main()
