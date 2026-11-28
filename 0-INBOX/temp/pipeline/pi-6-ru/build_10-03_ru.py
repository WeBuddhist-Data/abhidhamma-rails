"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-03-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra paccuppanna: (Ga) anulomapuggalokāsā, (Gha) paccanīkapuggalo).

Members, headings and closings come from build_10-01_ru (IN_*); family B frames (questions, partial answers,
«не возникает ни …, ни …») from build_2-01_ru; the Āyatana person clause «у тех, кто перерождается с глазом и без
уха,» from build_3-01_ru; the mixed person / time intros («У всех в момент распада ума, в момент возникновения ума,
не связанного с …, у вошедших в медитативное достижение прекращения и у существ без восприятия») from
build_5-01_ru (pv_intro; moments as build_8_ru); the person / place shape from build_7-01_ru.
The Indriya person attributes (IN_ATTR …) and the associated-mind members come from build_10-02_ru (settled there
with the same Russian); this module joins them with the 5-01 units (sabbesaṃ, nirodhasamāpannānaṃ,
asaññasattānaṃ …) through build_5-01_ru.pv_intro and asserts agreement with build_10-02_ru.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-03_ru.py
Import: P = importlib.import_module("build_10-03_ru")   (importing never writes any file)

Exposed for 10-04 … 10-13
  IN_PERSON_DESC / IN_DESC_GENDER, desc_clause(), in_units(), in_intro(intro, tattha), IN_MOMENT_UNITS, moments(),
  in_pv_sentence(s, subj), in_pv_question(q, subj), tr_line(text), translate_text(src)
"""
import contextlib
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

I = importlib.import_module("build_10-01_ru")    # Indriya members, headings, closings
D = I.D                                          # build_2-01_ru: family B
A3 = I.A                                         # build_3-01_ru: Āyatana person clause
C = I.C                                          # build_7-01_ru: person / place shape
S = importlib.import_module("build_5-01_ru")     # mixed person / time intros (pv_intro), moments (8)
E = S.E                                          # build_2-02_ru
CHAPTER = "10-03-indriyayamaka.md"
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Person attributes inside «тех, кто перерождается …» (Āyatana clause of 3-01, extended)
# =============================================================================================
# The attributes are 10-02's (build_10-02_ru.IN_ATTR, settled in parallel with identical Russian; imported):
# sa-X-ka / a-X-ka «с глазом» / «без глаза» (3-01 have_desc with 10-02 IN_HAVE2); itthīnaṃ «женщиной», na itthīnaṃ
# «не женщиной», purisānaṃ «мужчиной»; somanassena / vinā somanassena «с радостью» / «без радости»; upekkhāya
# «с невозмутимостью»; sahetukānaṃ / ahetukānaṃ «с корнями» / «без корней»; ñāṇasampayuttānaṃ / ñāṇavippayuttānaṃ
# «со знанием» / «без знания».
P2 = importlib.import_module("build_10-02_ru")
IN_PERSON_DESC = dict(P2.IN_ATTR)                               # Pāli (lower-case) -> Russian after «перерождается»
for _k in P2.IN_HAVE2:                                          # sacakkhukānaṃ / acakkhukānaṃ …
    for _p in ("sa", "a"):
        IN_PERSON_DESC.setdefault(f"{_p}{_k}ānaṃ", A3.have_desc(f"{_p}{_k}ānaṃ", P2.IN_HAVE2))
# Russian order: the gender comes first («перерождается женщиной и с глазом»), so that «с» never governs
# «женщиной» («с глазом и женщиной» would read "with an eye and with a woman"); otherwise the Pāli order (10-02).
IN_DESC_GENDER = P2.IN_ATTR_FRONT
REBORN = A3.REBORN                                             # «тех, кто перерождается {desc}» (3-01)
REBORN_VERBS = {"upapajjantānaṃ": REBORN,
                # ^6-10-204 … ^6-10-212 block, line "Itthīnaṃ ñāṇasampayuttānaṃ uppajjantīnaṃ": uppajjati
                # ("arise") for upapajjati ("be reborn"); a real word with another meaning: kept as written.
                "uppajjantānaṃ": REBORN.replace("перерождается", D.verb("uppajjati", "sg"))}


def _desc_at(toks, j):
    """(Russian, Pāli key, tokens used) for the descriptor at toks[j], or None."""
    two = " ".join(toks[j:j + 2])
    if two in IN_PERSON_DESC:
        return IN_PERSON_DESC[two], two, 2
    if toks[j] in IN_PERSON_DESC:
        return IN_PERSON_DESC[toks[j]], toks[j], 1
    return None


def desc_clause(keys):
    """Pāli descriptor keys (Pāli order) -> «женщиной и с глазом» (gender first, 3-01 HAVE_JOIN)."""
    ordered = [k for k in keys if k in IN_DESC_GENDER] + [k for k in keys if k not in IN_DESC_GENDER]
    return A3.HAVE_JOIN.join(IN_PERSON_DESC[k] for k in ordered)


def in_units(intro):
    """Intro -> 5-01 units; runs of descriptors + upapajjantānaṃ become one «тех, кто перерождается …» unit,
    everything else goes through build_5-01_ru.sc_units (original)."""
    toks = lower1(intro).replace(",", "").split(" ")
    units, rest, i = [], [], 0

    def flush():
        if rest:
            units.extend(_ORIG_SC_UNITS(" ".join(rest)))
            rest.clear()

    while i < len(toks):
        keys, j = [], i
        while j < len(toks):
            d = _desc_at(toks, j)
            if not d:
                break
            keys.append(d[1])
            j += d[2]
        if keys:
            if j >= len(toks) or toks[j] not in REBORN_VERBS:
                raise ValueError(f"person clause not parsed: {intro!r}")
            if toks[j] == "uppajjantānaṃ":
                SLIP_LOG.append("'uppajjantīnaṃ' (arising) for 'upapajjantīnaṃ' (being reborn): kept as written")
            flush()
            units.append([REBORN_VERBS[toks[j]].format(desc=desc_clause(keys)), "rel"])
            i = j + 1
            continue
        rest.append(toks[i])
        i += 1
    flush()
    return units


_ORIG_SC_UNITS = S.sc_units

# =============================================================================================
# Moments: "<A>sampayutta / <A>vippayutta [<B>…]cittassa uppādakkhaṇe / bhaṅgakkhaṇe" (5-01 frame)
# =============================================================================================
ASSOC_MEMBERS = P2.IN_ASSOC                     # compound member -> Russian instrumental (10-02)
VIPP, SAMP = P2.VIPP, P2.SAMP                   # «не связанного» / «связанного» (5-01 «не связанного с»)


def assoc(member, kind):
    return f"{SAMP if kind == 'sampayutta' else VIPP} {A3.s_prep(ASSOC_MEMBERS[member])}"


IN_MOMENT_UNITS = []
for _kh, _mo in (("uppādakkhaṇe", S.UPPADA), ("bhaṅgakkhaṇe", S.BHANGA)):
    for _m1 in ASSOC_MEMBERS:
        for _a1 in ("sampayutta", "vippayutta"):
            for _m2 in ASSOC_MEMBERS:
                if _m2 == _m1:
                    continue
                for _a2 in ("sampayutta", "vippayutta"):
                    IN_MOMENT_UNITS.append((rf"{_m1}{_a1}{_m2}{_a2}cittassa {_kh}",
                                            f"{_mo} {S.CITTA_G}, {assoc(_m1, _a1)} и {assoc(_m2, _a2)}",
                                            "advc", False))
            IN_MOMENT_UNITS.append((rf"{_m1}{_a1}cittassa {_kh}", f"{_mo} {S.CITTA_G}, {assoc(_m1, _a1)}",
                                    "advc", False))


@contextlib.contextmanager
def moments():
    """build_5-01_ru.ALL_UNITS + IN_MOMENT_UNITS and the descriptor clause, for the block only."""
    old = list(S.ALL_UNITS)
    S.ALL_UNITS[:0] = [u for u in IN_MOMENT_UNITS if u not in S.ALL_UNITS]
    S.sc_units = in_units
    try:
        with E.extra_units():
            yield
    finally:
        S.ALL_UNITS[:] = old
        S.sc_units = _ORIG_SC_UNITS


def in_intro(intro, tattha=False):
    with moments():
        return S.pv_intro(intro, tattha)


# =============================================================================================
# Sentences and questions (family B frames of build_2-01_ru, as build_5-01_ru.pv_sentence)
# =============================================================================================
SUBJ = I.IN_PV_SUBJ
NAMES = "(?:" + "|".join(sorted(SUBJ, key=len, reverse=True)) + ")"
S1_RE = re.compile(r"(?P<intro>.+?) " + S._T.format(n="t1") + rf" (?P<x>{NAMES}) (?P<n1>na |n)?(?P<v1>" + D.V_RE
                   + r"), no ca " + S._T.format(n="t2") + rf" (?P<y>{NAMES}) (?P<n2>na |n)?(?P<v2>" + D.V_RE + r")")
S2_RE = re.compile(r"(?P<intro>.+?) " + S._T.format(n="t1") + rf" (?P<x>{NAMES}) ca (?P<n1>na |n)?(?P<v1>" + D.V_RE
                   + rf") (?P<y>{NAMES}) ca (?P<n2>na |n)?(?P<v2>" + D.V_RE + r")")


def pv_norm(s):
    """Feminine forms read as the common ones (Russian has one form): tāsaṃ = tesaṃ, -antīnaṃ = -antānaṃ;
    "Xñca" = "Xṃ ca"."""
    s = re.sub(r"\btāsaṃ\b", "tesaṃ", s)
    s = re.sub(r"antīnaṃ\b", "antānaṃ", s)
    return re.sub(r"ñca\b", "ṃ ca", s)


def _pred(v, x, neg):
    return D.PV_PRED.format(v=D.verb(v, x["g"], bool(neg)), x=x["nom"])


def in_pv_sentence(s, subj=SUBJ):
    """One Pāli answer sentence (no final '.') -> Russian sentence with '.'."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    s = pv_norm(s)
    m = S1_RE.fullmatch(s)
    if m:
        head = (in_intro(m.group("intro"), "tattha" in m.group("t1")) if m.group("t1").startswith("tesaṃ")
                else S.place_intro(m.group("intro")))
        x, y = subj[m.group("x")], subj[m.group("y")]
        v2 = D.verb(m.group("v2"), y["g"], not m.group("n2"))      # "no ca": the predicate is denied for Y
        tail = (D.PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
            res=C.RES[m.group("t2")], **{("pred" if m.group("n2") else "neg_pred"): D.PV_PRED.format(v=v2, x=y["nom"])})
        return head + _pred(m.group("v1"), x, m.group("n1")) + tail + "."
    m = S2_RE.fullmatch(s)
    if m:
        head = (in_intro(m.group("intro"), "tattha" in m.group("t1")) if m.group("t1").startswith("tesaṃ")
                else S.place_intro(m.group("intro")))
        x, y = subj[m.group("x")], subj[m.group("y")]
        if m.group("n1") and m.group("n2"):
            f1, f2 = D.verb(m.group("v1"), x["g"]), D.verb(m.group("v2"), y["g"])
            both = (D.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"]) if f1 == f2
                    else D.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"]))
        else:
            both = C.BOTH_FRAME.format(p1=_pred(m.group("v1"), x, m.group("n1")),
                                       p2=_pred(m.group("v2"), y, m.group("n2")))
        return head + both + "."
    raise ValueError(f"pavatti answer not parsed: {s!r}")


def in_pv_question(q, subj=SUBJ):
    return D.pv_question(lower1(q.strip()), subj)[0]


# =============================================================================================
# Lines
# =============================================================================================
LABEL_RE = re.compile(r"\((Ka|Kha)\) (.*)")


def _answers(text, subj):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        out.append(in_pv_sentence(s[:-1], subj))
    return " ".join(out)


def tr_line(text, subj=SUBJ):
    """Translate one Pāli line (block ID removed)."""
    if not text.strip():
        return ""
    if text.startswith("#"):
        return I.heading(text)
    m = I.TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), subj) + f" ({I.TAILS[m.group(2)]}){m.group(3)}"
    label = ""
    m = LABEL_RE.fullmatch(text)
    if m:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    if "?" in text:
        q, _, rest = text.partition("?")
        out = in_pv_question(q, subj)
        return label + out + (" " + _answers(rest, subj) if rest.strip() else "")
    return label + _answers(text, subj)


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
    ("2", "без корней"), ("2", "имеющих корни"), ("1", "связанный со знанием"), ("1", "не связанный со знанием"),
    ("1", "радостью"), ("1", "невозмутимостью"), ("1", "верой"), ("5", "женщиной"), ("4", "мужчиной"),
    ("2", "без ума"), ("5", "момент возникновения"), ("5", "момент распада"),
    ("5", "медитативное достижение прекращения"), ("2", "перерождаются"), ("2", "умирают"),
]


def check_with_10_02(src):
    """Every moment unit = build_10-02_ru.moment(); every answer sentence that build_10-02_ru parses comes out
    byte-identical there and here."""
    for rx, ru, kind, _ in IN_MOMENT_UNITS:
        word, kh = rx.split(" ")
        assert P2.moment(word, kh) == (ru, kind), (rx, ru, P2.moment(word, kh))
    same = 0
    for line in src.split("\n"):
        body, _ = B.ID_RE.match(line).groups()
        m = I.TAIL_RE.fullmatch(body)
        body = m.group(1) if m else body
        rest = body.partition("?")[2] if "?" in body else ("" if body.startswith("#") else body)
        for s in re.split(r"(?<=\.) (?=\S)", rest.strip()) if rest.strip() else []:
            try:
                theirs = P2.in_pv_sentence(s[:-1])
            except (ValueError, KeyError):
                continue
            assert theirs == in_pv_sentence(s[:-1]), (s, theirs, in_pv_sentence(s[:-1]))
            same += 1
    return same


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, within the chapter and against every finished pi-6 chapter
    (as build_10-02_ru.check_against_finished, for this chapter)."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent within {CHAPTER}: {pb!r}"
        mine[pb] = rb
    shared = 0
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb and pb in mine:
                assert mine[pb] == rb, f"differs from {f.name}: {pb!r}\n  {rb!r}\n  {mine[pb]!r}"
                shared += 1
    return shared


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(CROSSBOOK)
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    same = check_with_10_02(src)
    shared = check_against_finished(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in dict.fromkeys(SLIP_LOG + D.SLIP_LOG):
        print("slip:", s)
    print(f"cross-book asserts OK; per-line checks OK; {same} sentences identical with build_10-02_ru; "
          f"{shared} lines shared with finished chapters, all identical")


if __name__ == "__main__":
    main()
