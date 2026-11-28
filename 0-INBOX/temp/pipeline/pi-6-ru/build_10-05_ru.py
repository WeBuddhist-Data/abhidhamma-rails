"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-05-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra: (2) Atītavāro and (3) Anāgatavāro).

Members, headings and mūlaka tails come from build_10-01_ru; the person attributes (IN_PERSON_DESC: «с глазом»,
«с невозмутимостью» …) from build_10-03_ru / build_10-02_ru; the Āyatana person parser of the past and future
sections (plane beings «У существ мира форм и существ мира без форм», "ye Xaṃ upapajjitvā parinibbāyissanti",
itaresaṃ …) and the abbreviated "…pe…" questions from build_3-02_ru (3-01 / 3-02 are the same Pāli shapes);
the person / time intros that mix moments («У существ Чистых обителей, когда присутствует второй ум, и у
существ без восприятия») from build_5-01_ru.pv_intro; place answers «В мире форм: там …» from build_3-01_ru
(as 10-02); family B frames from build_2-01_ru; «сразу после данного ума возникнет последний ум» from
build_6-01_ru. build_10-04_ru settles nothing new (checked).

NEW here (listed in notes-10-05.md), exposed for 10-06 … 10-13 as IN5_UNITS / in5_units():
  "ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti"
      = «тех мужчин, которые, пройдя в этом же состоянии несколько существований, достигнут окончательного угасания»
  "yā itthiyo …" = «тех женщин, которые, …»; "… dassetvā upekkhāya upapajjitvā parinibbāyissanti"
      = «…, пройдя в этом же состоянии несколько существований и переродившись с невозмутимостью, достигнут …»
  "ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti" = 2-01's «тех, кто, переродившись {…}, достигнет
      окончательного угасания» with «с глазом и с невозмутимостью»
  "yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati"
      = «тех, у кого сразу после данного ума возникнет последний ум, связанный с невозмутимостью» (6-01 frame)

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-05_ru.py
Import: importlib.import_module("build_10-05_ru")   (importing never writes any file)
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

I = importlib.import_module("build_10-01_ru")    # Indriya members, headings, mūlaka tails
J = importlib.import_module("build_10-02_ru")    # IN_ATTR, IN_ASSOC, IN_HAVE2
P = importlib.import_module("build_10-03_ru")    # IN_PERSON_DESC, pv_norm
S = importlib.import_module("build_5-01_ru")     # pv_intro (mixed person / time intros)
Q2 = importlib.import_module("build_3-02_ru")    # ay2_person_intro (UNITS), pe_question
K6 = importlib.import_module("build_6-01_ru")    # LAST_MIND_ARISES
A, D, C = I.A, I.D, I.C                          # build_3-01_ru, build_2-01_ru, build_7-01_ru
CHAPTER = "10-05-indriyayamaka.md"
cap, lower1 = B.cap, C.lower1
SUBJ = I.IN_PV_SUBJ
SLIP_LOG = []

# =============================================================================================
# New person units (future section)
# =============================================================================================
YE_UNIT = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"ye {P}aṃ upapajjitvā parinibbāyissanti")
assert YE_UNIT == "тех, кто, переродившись {in1}, достигнет окончательного угасания", YE_UNIT
REBORN_GER = YE_UNIT.split(", ")[2].replace(" {in1}", "")            # «переродившись»
FINAL_SG = YE_UNIT.split(", ")[3]                                     # «достигнет окончательного угасания»
FINAL_PL = FINAL_SG.replace("достигнет", "достигнут", 1)             # plural subject («мужчин, которые …»)
assert (REBORN_GER, FINAL_PL) == ("переродившись", "достигнут окончательного угасания"), (REBORN_GER, FINAL_PL)
ETENEVA = "пройдя в этом же состоянии несколько существований"        # eteneva bhāvena katici bhave dassetvā
GENDER_PERSONS = {"purisā": ("ye", I.IN_GEN_PL["purisa"]), "itthiyo": ("yā", I.IN_GEN_PL["itthī"])}   # мужчин / женщин
MOODS = {k: J.IN_ATTR[k] for k in ("upekkhāya", "somanassena")}       # «с невозмутимостью» / «с радостью»
HAVE_NOM = {f"sa{k}ā": P.IN_PERSON_DESC[f"sa{k}ānaṃ"] for k in J.IN_HAVE2}   # sacakkhukā -> «с глазом»
LAST_MIND = K6.LAST_MIND_ARISES                                       # «сразу после данного ума возникнет последний ум»
SAMP_NOM = "связанный"                                                # -sampayutta (pi-1 «связанный со знанием»)

IN5_UNITS = []   # (regex, Russian, relative clause?) in the shape of build_2-01_ru.PERSON_UNITS (no capture groups)
for _pali, (_rel, _gen) in GENDER_PERSONS.items():
    for _ca in ("", "ca "):
        _head = f"{_rel} {_ca}{_pali} eteneva bhāvena katici bhave dassetvā"
        for _mood, _mru in MOODS.items():
            IN5_UNITS.append((re.escape(f"{_head} {_mood} upapajjitvā parinibbāyissanti"),
                              f"тех {_gen}, которые, {ETENEVA} и {REBORN_GER} {_mru}, {FINAL_PL}", True))
        IN5_UNITS.append((re.escape(f"{_head} parinibbāyissanti"), f"тех {_gen}, которые, {ETENEVA}, {FINAL_PL}", True))
for _have, _hru in HAVE_NOM.items():
    for _ca in ("", "ca "):
        for _mood, _mru in MOODS.items():
            IN5_UNITS.append((re.escape(f"ye {_ca}{_have} {_mood} upapajjitvā parinibbāyissanti"),
                              YE_UNIT.format(in1=A.HAVE_JOIN.join([_hru, _mru])), True))
for _a in ("upekkhā", "somanassa"):
    IN5_UNITS.append((re.escape(f"yassa cittassa anantarā {_a}sampayuttapacchimacittaṃ uppajjissati"),
                      f"тех, у кого {LAST_MIND}, {SAMP_NOM} {A.s_prep(J.IN_ASSOC[_a])}", True))


@contextlib.contextmanager
def in5_units():
    """IN5_UNITS in front of build_3-02_ru.UNITS for the block only."""
    old = Q2.UNITS
    Q2.UNITS = IN5_UNITS + old
    try:
        yield
    finally:
        Q2.UNITS = old


def in5_person_intro(intro, planes=None, have=None):
    """Plane beings, descriptors, 2-01 / 2-02 / 3-02 / IN5 units (build_3-02_ru parser); intros with moments or
    «когда …» clauses go to build_5-01_ru.pv_intro (as 5-01 renders the same intros)."""
    try:
        with in5_units():
            return Q2.ay2_person_intro(intro, I.IN_PLANES, J.IN_HAVE2)
    except ValueError:
        return S.pv_intro(intro, False)


def pv_sentence(body, y):
    """One Pāli answer sentence (no final '.') -> Russian with '.' (build_3-01_ru.ay_pv_sentence frames)."""
    s = P.pv_norm(body)
    old = A.ay_person_intro
    A.ay_person_intro = in5_person_intro
    try:
        return A.ay_pv_sentence(s, SUBJ, I.IN_PLANES, y, J.IN_HAVE2)
    finally:
        A.ay_person_intro = old


# =============================================================================================
# Questions
# =============================================================================================
def question(body):
    """Pāli question body (no '?') -> (Russian question with '?', y noun)."""
    lb = lower1(body.strip())
    if "…" in lb:
        if " … " in lb:      # ^6-10-261 "jīvitindriyaṃ … somanassindriyaṃ": stray space before "…"
            SLIP_LOG.append("^6-10-261 'jīvitindriyaṃ … somanassindriyaṃ': space before '…' (spacing only; rendered as the other members)")
            lb = lb.replace(" … ", "… ")
        return Q2.pe_question(lb, SUBJ)
    m = D.PV_Q_RE.fullmatch(lb)
    if m and m.group("rel") in ("yassa", "yassa vā pana") and m.group("cor") == "tattha":
        # ^6-10-240 "Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ …": yassa … tattha (the
        # parallels have tassa): kept as written, «А у кого …, там …?»
        SLIP_LOG.append("^6-10-240 'yassa vā pana … tattha …' (parallels: tassa): kept as written, «…, там …?»")
        q, y = D.pv_question(lb.replace(" tattha ", " tassa ", 1), SUBJ)
        q2 = q.replace(", у того ", ", там ", 1)
        assert q2 != q, q
        return q2, y
    return D.pv_question(lb, SUBJ)


# =============================================================================================
# Lines
# =============================================================================================
Q_TOK = re.compile(r"(\s*)((?:[Yy]assa|[Yy]attha)(?: vā pana)?(?: yattha)? \S+?ndriyaṃ[^?]*\?)")
ELL_TOK = re.compile(r"(\s*)(…[Pp]e…\.?)")
S_TOK = re.compile(r"(\s*)([^?.…]+?(?:\.|(?=\s*…)))")


def segments(plain):
    out, pos, y, first = [], 0, None, True
    while pos < len(plain):
        m = Q_TOK.match(plain, pos)
        if m:
            sep, tok = m.groups()
            ru, y = question(tok[:-1])
        else:
            m = ELL_TOK.match(plain, pos)
            if m:
                sep, tok = m.groups()
                ru = "…"
            else:
                m = S_TOK.match(plain, pos)
                if not m or m.end() == pos:
                    raise ValueError(f"line not segmented at {plain[pos:]!r}")
                sep, tok = m.groups()
                body = tok[:-1] if tok.endswith(".") else tok
                ru = I.SHORT[body] if body in I.SHORT else pv_sentence(body, y)
                if not tok.endswith("."):          # runs straight into "…pe…" (as written)
                    assert ru.endswith("."), ru
                    ru = ru[:-1]
        pos = m.end()
        if tok != "…" and not ELL_TOK.fullmatch(tok):
            ru = cap(ru) if (first or tok[0].isupper()) else lower1(ru)
        out.append(sep + ru)
        first = False
    return "".join(out)


def tr_line(text):
    """Translate one Pāli line (block ID removed)."""
    if not text.strip():
        return ""
    if text.startswith("#"):
        return I.heading(text)
    m = I.TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1)) + f" ({I.TAILS[m.group(2)]}){m.group(3)}"
    label = ""
    m = I.LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    assert "[" not in text, text
    return label + segments(text)


def translate_text(src):
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("1", "связанный со знанием"), ("1", "невозмутимостью"), ("2", "мужчин"), ("2", "женщин"),
    ("5", "окончательного угасания"), ("2", "сразу после"), ("5", "Пройдя"), ("2", "существование"),
]


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


def check_frames():
    """The reused frames reproduce the finished chapters' renderings of the same intros (asserted)."""
    samples = {   # Pāli intro -> Russian head in a finished chapter (3-01, 5-01, 3-02)
        "Asaññasattānaṃ arūpānaṃ": "У существ без восприятия и существ мира без форм ",
        "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ":
            "У существ Чистых обителей, когда присутствует второй ум, и у существ без восприятия ",
        "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ": "У остальных существ с четырьмя составляющими и существ с пятью составляющими ",
        "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti":
            "У тех, кто, переродившись в мире форм, достигнет окончательного угасания, ",
        "Itaresaṃ": "У остальных ",
    }
    for pali, ru in samples.items():
        got = in5_person_intro(pali)
        assert got == ru, (pali, got, ru)


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(CROSSBOOK)
    I.check_members()
    check_frames()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    shared, files = check_against_finished(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")),
          "| lines shared with finished chapters:", shared, files)
    for s in dict.fromkeys(SLIP_LOG + D.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; frame asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    main()
