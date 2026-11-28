"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-12-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra: (6) Atītānāgatavāro, the past + future section).

The line driver, questions, answer frames and person parser are build_10-05_ru's (tr_line / segments /
pv_sentence / in5_person_intro: the 10-05 Atīta / Anāgata chapter is the closest shape: same persons, same places,
"…pe…" chains); the mixed past + future frames are 2-01 family B (build_2-01_ru: «возникала X, но у них не
возникнет Y», «и возникала X, и возникнет Y», PV_NEG_MIXED_FRAME «не возникнет X и не возникала Y»), as the
Atītānāgata sections of 2-01, 3-03, 5-0x, 9-0x already render them. Members, headings, mūlaka tails come from
build_10-01_ru; attributes from build_10-02_ru; IN5_UNITS from build_10-05_ru.

Person units added to build_3-02_ru.UNITS for this chapter only (units_12()):
  build_3-03_ru.PERSON_UNITS_3_03 ("Rūpāvacare arūpāvacare pacchimabhavikānaṃ" = 3-03's «тех, кто живёт последней
      жизнью в мире форм и в мире без форм», "ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti");
  "ye ca upekkhāya / somanassena upapajjitvā parinibbāyissanti" = 2-01's unit with 10-02's attribute (as 10-06);
  "pacchimacittasamaṅgīnaṃ" = build_5-01_ru «обладающих последним умом»;
  NEW: "ye ca purisā / yā ca itthiyo upekkhāya (somanassena) upapajjitvā parinibbāyissanti"
      = «тех мужчин / женщин, которые, переродившись с невозмутимостью (с радостью), достигнут окончательного
      угасания» (10-05's gender frame without "eteneva bhāvena …").

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-12_ru.py   [--probe]
Import: importlib.import_module("build_10-12_ru")   (importing never writes any file)
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

M5 = importlib.import_module("build_10-05_ru")   # line driver, IN5_UNITS, gender frame pieces
I = M5.I                                         # build_10-01_ru: members, headings, mūlaka tails
J = M5.J                                         # build_10-02_ru: IN_ATTR
Q2 = M5.Q2                                       # build_3-02_ru: person parser (UNITS)
S = M5.S                                         # build_5-01_ru: SC_UNITS
G3 = importlib.import_module("build_3-03_ru")    # PERSON_UNITS_3_03
D = M5.D                                         # build_2-01_ru: family B
CHAPTER = "10-12-indriyayamaka.md"
IN_PROGRESS = {"10-08-indriyayamaka.md", "10-09-indriyayamaka.md"}   # translated in parallel: not depended on
SLIP_LOG = []

# =============================================================================================
# Person units of this chapter
# =============================================================================================
YE_UNIT = M5.YE_UNIT                              # тех, кто, переродившись {in1}, достигнет окончательного угасания
LAST_MIND_HOLDERS = dict((u[0], u[1]) for u in S.SC_UNITS)["pacchimacittasamaṅgīnaṃ"]
assert LAST_MIND_HOLDERS == "обладающих последним умом", LAST_MIND_HOLDERS

UNITS_12 = []
for _mood, _mru in M5.MOODS.items():
    # "ye ca upekkhāya upapajjitvā parinibbāyissanti" (as 10-06: «и у тех, кто, переродившись с невозмутимостью, …»)
    UNITS_12.append((rf"ye (?:ca )?{_mood} upapajjitvā parinibbāyissanti", YE_UNIT.format(in1=_mru), True))
    # NEW: "ye ca purisā upekkhāya upapajjitvā parinibbāyissanti" (10-05 gender frame, no "eteneva bhāvena …")
    for _pali, (_rel, _gen) in M5.GENDER_PERSONS.items():
        UNITS_12.append((rf"{_rel} (?:ca )?{_pali} {_mood} upapajjitvā parinibbāyissanti",
                         f"тех {_gen}, которые, {M5.REBORN_GER} {_mru}, {M5.FINAL_PL}", True))
UNITS_12.append((r"pacchimacittasamaṅgīnaṃ", LAST_MIND_HOLDERS, False))


@contextlib.contextmanager
def units_12():
    """build_3-03_ru's and this chapter's units in front of build_3-02_ru.UNITS (10-05's IN5_UNITS go in front of
    these inside build_10-05_ru.in5_units())."""
    old = Q2.UNITS
    Q2.UNITS = UNITS_12 + G3.PERSON_UNITS_3_03 + [u for u in old if u not in G3.PERSON_UNITS_3_03]
    try:
        yield
    finally:
        Q2.UNITS = old


# =============================================================================================
# Lines
# =============================================================================================
PE_TAIL = "…pe…."     # ^6-10-434 "(Paññindriyamūlakaṃ)…pe…." -> «(На основе способности мудрости)…»
E = importlib.import_module("build_2-02_ru")
FIXED = {"Pavattivāro niṭṭhito.": f"{E.PAVATTIVARO} {B.NITTHITO}."}   # «Раздел о протекании завершён.» (2-02)
assert FIXED["Pavattivāro niṭṭhito."] == "Раздел о протекании завершён.", FIXED


def tr_line(text):
    """Translate one Pāli line (block ID removed)."""
    if text in FIXED:
        return FIXED[text]
    with units_12():
        if text.endswith(")" + PE_TAIL):
            return M5.tr_line(text[: -len(PE_TAIL)]) + "…"
        return M5.tr_line(text)


def sentence(seg):
    """One Pāli question or answer sentence (used by the cross-check)."""
    with units_12():
        return M5.segments(seg)


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
    ("2", "мужчин"), ("2", "женщин"), ("5", "окончательного угасания"), ("1", "невозмутимостью"),
]


def check_frames():
    """The reused units reproduce the finished chapters' renderings of the same intros (asserted)."""
    samples = {   # Pāli intro -> Russian head in a finished chapter
        "Rūpāvacare arūpāvacare pacchimabhavikānaṃ asaññasattānaṃ":        # 3-03
            "У тех, кто живёт последней жизнью в мире форм и в мире без форм, и у существ без восприятия ",
        "Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ":                            # 10-05
            "У существ Чистых обителей, существ без восприятия и существ мира без форм ",
        "Suddhāvāsānaṃ arūpe pacchimabhavikānaṃ":                           # 2-01
            "У существ Чистых обителей и у тех, кто живёт последней жизнью в мире без форм, ",
        "Pacchimabhavikānaṃ ye ca upekkhāya upapajjitvā parinibbāyissanti":  # 10-06
            "У тех, кто живёт последней жизнью, и у тех, кто, переродившись с невозмутимостью, "
            "достигнет окончательного угасания, ",
    }
    with units_12():
        for pali, ru in samples.items():
            got = M5.in5_person_intro(pali)
            assert got == ru, (pali, got, ru)


SENT_SPLIT = re.compile(r"(?<=[.?]) (?=\S)")
RU_TAIL = re.compile(r" \(На основе [^()]*\)\.?$")


def cross_sentences():
    """Every Pāli sentence of a finished Indriya chapter (10-01 … 10-07) that this builder translates comes out
    byte-identical with that chapter's Russian sentence."""
    same, diff = 0, []
    for f in sorted(B.OUT_DIR.glob("10-*.md")):
        if f.name == CHAPTER or f.name in IN_PROGRESS or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if not pb or pb.startswith("#") or "…" in pb:
                continue
            m = I.TAIL_RE.fullmatch(pb)
            if m:
                pb, rb = m.group(1), RU_TAIL.sub("", rb)
            m = I.LABEL_RE.fullmatch(pb)
            if m:
                pb, rb = m.group(2), re.sub(r"^\([а-я]\) ", "", rb)
            ps, rs = SENT_SPLIT.split(pb), SENT_SPLIT.split(rb)
            if len(ps) != len(rs):
                continue
            for ps1, rs1 in zip(ps, rs):
                try:
                    mine = sentence(ps1)
                except (ValueError, KeyError, AttributeError, AssertionError, TypeError):
                    continue
                if mine == rs1:
                    same += 1
                else:
                    diff.append((f.name, ps1, rs1, mine))
    return same, diff


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
        if f.name == CHAPTER or f.name in IN_PROGRESS or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb and pb in mine:
                assert mine[pb] == rb, f"differs from {f.name}: {pb!r}\n  {rb!r}\n  {mine[pb]!r}"
                shared += 1
                files.add(f.name)
                distinct.add(pb)
    n_lines = sum(1 for p in src.split("\n") if B.ID_ANY.sub("", p).strip() in distinct)
    return shared, n_lines, sorted(files)


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
    D.check_crossbook(M5.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    I.check_members()
    M5.check_frames()
    check_frames()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    n5, nd = len(M5.SLIP_LOG), len(D.SLIP_LOG)
    ru = translate_text(src)
    my_slips = SLIP_LOG + M5.SLIP_LOG[n5:] + D.SLIP_LOG[nd:]      # logged while translating this chapter only
    B.check_pair(src, ru, CHAPTER)
    shared, n_lines, files = check_against_finished(src, ru)
    same, diff = cross_sentences()
    assert not diff, "\n".join(f"{n}: {p}\n  theirs: {r}\n  mine:   {m}" for n, p, r, m in diff[:8])
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")),
          "| segments:", sum(1 for ln in src.split("\n") if B.ID_ANY.search(ln) and not ln.startswith("#")),
          f"| {n_lines} lines of this chapter occur in finished chapters ({shared} matches, all byte-identical):",
          files, "| sentences identical with finished Indriya chapters 10-01 … 10-07:", same)
    for s in dict.fromkeys(my_slips):
        print("slip:", s)
    print("cross-book asserts OK; frame asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    if "--probe" in sys.argv:
        probe()
    else:
        main()
