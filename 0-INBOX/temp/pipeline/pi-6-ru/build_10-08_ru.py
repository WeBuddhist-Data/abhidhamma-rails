"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-08-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra (4) Paccuppannātītavāro: present + past, all six sections (Ka) … (Ca)).

Nothing is typed here that a finished builder already settles:
  * members, headings, mūlaka tails: build_10-01_ru;
  * person attributes («с глазом», «не женщиной», «с невозмутимостью» …), associated minds: build_10-02_ru;
  * the mixed-tense line driver: build_10-05_ru.tr_line (3-02 person parser ay2_person_intro: 3-02 is the
    Āyatana Paccuppannātītavāro, same shapes; «У остальных, кто перерождается с глазом,»; family B mixed-tense
    frames of build_2-01_ru: «и возникает X, и возникала Y», «не возникает X и не возникала Y»; the "…pe…"
    questions of build_3-02_ru.pe_question; IN5_UNITS);
  * the person / time intros with moments: build_10-03_ru.tr_line (5-01 pv_intro, 10-03 IN_MOMENT_UNITS);
  * the place sections ((Kha), (Ṅa)) come out of the same drivers byte-identical with build_10-02_ru.tr_line.
Every line is run through build_10-05_ru.tr_line and build_10-03_ru.tr_line; where both parse a line, the two
must agree byte for byte (asserted).

Two combinations are joined here (listed in notes-10-08.md; no new wording):
  * the 10-02 gender attribute inside the 3-02 «тех, кто перерождается {desc} {in1}» unit:
    "Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ"
    = «У тех, кто умирает в мире чувственных желаний, и у тех, кто перерождается не женщиной в мире
      чувственных желаний,»;
  * the 2-01 / 3-02 itaresaṃ merge applied to the 10-03 units:
    "Itaresaṃ upekkhāya upapajjantānaṃ pavatte …" = «У остальных, кто перерождается с невозмутимостью, и в
      течение жизни …» (as 5-01 / 3-02 «У остальных, кто перерождается …»).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-08_ru.py
Import: importlib.import_module("build_10-08_ru")   (importing never writes any file)
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
J = importlib.import_module("build_10-02_ru")    # IN_ATTR, IN_HAVE2, IN_ASSOC, place driver
P3 = importlib.import_module("build_10-03_ru")   # persons with moments (5-01 pv_intro), IN_PERSON_DESC
P5 = importlib.import_module("build_10-05_ru")   # past / future driver (3-02 person parser, pe_question)
Q2 = P5.Q2                                       # build_3-02_ru (Āyatana Paccuppannātītavāro)
A, D, C = I.A, I.D, I.C                          # build_3-01_ru, build_2-01_ru, build_7-01_ru
CHAPTER = "10-08-indriyayamaka.md"
lower1 = C.lower1
SLIP_LOG = []

# =============================================================================================
# Source slips
# =============================================================================================
SLIPS = [   # (old, new, note): plain spelling slips rendered as meant; each must occur exactly once
    ("(Ghānandriyamūlakaṃ)", "(Ghānindriyamūlakaṃ)",
     "^6-10-336 '(Ghānandriyamūlakaṃ)' = Ghānindriyamūlakaṃ (spelling slip; ^6-10-346 has it): rendered as meant"),
    ("asaññasattā cavantāna tesaṃ", "asaññasattā cavantānaṃ tesaṃ",
     "^6-10-361 'asaññasattā cavantāna' = cavantānaṃ (missing ṃ; spelling slip): rendered as meant"),
]
AS_WRITTEN = [   # (exact Pāli, note): real words / different readings, translated as written; each occurs once
    ("asaññasattānaṃ arūpānaṃ tesaṃ tattha cakkhundriyañca na uppajjati sotindriyañca na uppajjittha. "
     "(Kha) yassa vā pana yattha somanassindriyaṃ",
     "^6-10-357 (Ka) cakkhu / somanassa: the answer's second sentence has 'sotindriyañca' (question: "
     "somanassindriyaṃ): another member, kept as written, «… и не возникала способность уха»"),
    ("tesaṃ tattha somanassindriyaṃ na uppajjati, no ca tesaṃ tattha jīvitindriyaṃ na uppajjittha",
     "^6-10-361 (Kha) somanassa / jīvita: first answer sentence has the tenses swapped ('somanassindriyaṃ na "
     "uppajjati … jīvitindriyaṃ na uppajjittha'; question: na uppajjittha … na uppajjati): kept as written"),
]


def preprocess(src):
    for old, new, note in SLIPS:
        assert src.count(old) == 1, (old, src.count(old))
        src = src.replace(old, new)
        SLIP_LOG.append(note)
    return src


def check_as_written(src):
    flat = src.replace("\n", " ")
    for pali, note in AS_WRITTEN:
        assert flat.count(pali) == 1, (pali, flat.count(pali))
        SLIP_LOG.append(note)


# =============================================================================================
# Combination 1: the 10-02 gender attribute inside the 3-02 person parser
# =============================================================================================
GENDER = {"na_itthīnaṃ": P3.IN_PERSON_DESC["na itthīnaṃ"], "na_purisānaṃ": P3.IN_PERSON_DESC["na purisānaṃ"],
          "itthīnaṃ": P3.IN_PERSON_DESC["itthīnaṃ"], "purisānaṃ": P3.IN_PERSON_DESC["purisānaṃ"]}
assert GENDER == {"na_itthīnaṃ": "не женщиной", "na_purisānaṃ": "не мужчиной",
                  "itthīnaṃ": "женщиной", "purisānaṃ": "мужчиной"}, GENDER
_ORIG_AY2_UNITS = Q2.ay2_person_units
_ORIG_HAVE_DESC = A.have_desc


def _have_desc(tok, have=None):
    return GENDER[tok] if tok in GENDER else _ORIG_HAVE_DESC(tok, have)


def ay2_units_gender(intro, planes=None, have=None):
    """build_3-02_ru.ay2_person_units with the gender attributes as descriptors. A gender standing next to a
    sa-X-ka / a-X-ka descriptor would need 10-02's gender-first order: not in this chapter (asserted)."""
    intro = re.sub(r"\b([Nn])a (itthīnaṃ|purisānaṃ)\b", lambda m: m.group(1) + "a_" + m.group(2), intro)
    toks = lower1(intro).split()
    for k, t in enumerate(toks):
        if t in GENDER:
            near = toks[max(0, k - 1):k] + toks[k + 1:k + 2]
            assert not any(_ORIG_HAVE_DESC(n, have) for n in near), intro
    A.have_desc = _have_desc
    try:
        return _ORIG_AY2_UNITS(intro, planes, have)
    finally:
        A.have_desc = _ORIG_HAVE_DESC


# =============================================================================================
# Combination 2: itaresaṃ + «тех, кто перерождается …» merged (2-01 / 3-02 rule) in the 10-03 units
# =============================================================================================
_ORIG_IN_UNITS = P3.in_units


def in_units_itaresam(intro):
    units, out, k = _ORIG_IN_UNITS(intro), [], 0
    while k < len(units):
        if units[k][0] == D.ITARESAM and k + 1 < len(units) and units[k + 1][0].startswith("тех, кто"):
            out.append([D.ITARESAM + units[k + 1][0][3:], units[k + 1][1]])     # «остальных, кто …»
            k += 2
            continue
        out.append(units[k])
        k += 1
    return out


@contextlib.contextmanager
def patched():
    Q2.ay2_person_units, P3.in_units = ay2_units_gender, in_units_itaresam
    try:
        yield
    finally:
        Q2.ay2_person_units, P3.in_units = _ORIG_AY2_UNITS, _ORIG_IN_UNITS


# =============================================================================================
# Lines
# =============================================================================================
PARSE_ERRORS = (ValueError, KeyError, AssertionError)
DRIVER_USE = {"10-05": 0, "10-03": 0, "both": 0}


def tr_line(text):
    """Translate one Pāli line (block ID removed): build_10-05_ru and build_10-03_ru drivers, which must agree
    wherever both parse the line."""
    with patched():
        try:
            r5 = P5.tr_line(text)
        except PARSE_ERRORS:
            r5 = None
        try:
            r3 = P3.tr_line(text)
        except PARSE_ERRORS:
            r3 = None
    if r5 is None and r3 is None:
        with patched():
            P5.tr_line(text)                      # re-raise the parse error
    if r5 is not None and r3 is not None:
        assert r5 == r3, f"drivers disagree on {text!r}\n  10-05: {r5!r}\n  10-03: {r3!r}"
        DRIVER_USE["both"] += 1
    else:
        DRIVER_USE["10-05" if r5 is not None else "10-03"] += 1
    return r5 if r5 is not None else r3


def translate_text(src):
    out = []
    for line in preprocess(src).split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("5", "женщиной"), ("4", "мужчиной"), ("2", "перерождаются"), ("2", "умирают"), ("5", "момент распада"),
    ("1", "невозмутимостью"), ("2", "без корней"),
]


def check_places(src, ru):
    """The place sections ((Kha), (Ṅa)) agree with build_10-02_ru.tr_line (10-02 / 10-04 place driver)."""
    n = 0
    for p, r in zip(preprocess(src).split("\n"), ru.split("\n")):
        body, bid = B.ID_RE.match(p).groups()
        if body.startswith("Yattha "):
            assert J.tr_line(body, J.IN2_CFG) + (bid or "") == r, (p, r)
            n += 1
    return n


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, within the chapter and against every finished pi-6
    chapter (and the sample)."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent within {CHAPTER}: {pb!r}"
        mine[pb] = rb
    shared, mine_hit, files = 0, set(), set()
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb and pb in mine:
                assert mine[pb] == rb, f"differs from {f.name}: {pb!r}\n  {rb!r}\n  {mine[pb]!r}"
                shared += 1
                mine_hit.add(pb)
                files.add(f.name)
    return shared, len(mine_hit), sorted(files)


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(CROSSBOOK)
    I.check_members()
    P5.check_frames()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    check_as_written(src)
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    places = check_places(src, ru)
    shared, lines_hit, files = check_against_finished(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    segs = sum(1 for line in src.split("\n") if B.ID_RE.match(line).group(2))
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")), "segments", segs)
    print("driver use:", DRIVER_USE, "| place lines = build_10-02_ru:", places)
    print(f"{lines_hit} of this chapter's lines occur in finished chapters ({shared} matches), all byte-identical:",
          files)
    for s in dict.fromkeys(SLIP_LOG + P5.SLIP_LOG + P3.SLIP_LOG + D.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; frame asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    main()
