"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-10-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra, (5) Paccuppannānāgatavāro: (Gha) paccanīkapuggalo, (Ṅa) paccanīkaokāso).

Present + future, negative: "yassa X na uppajjati tassa Y na uppajjissatīti?" = «У кого не возникает X, у того не
возникнет Y?». The anuloma parts of the same section are 10-09: its driver is used for every line (imported, never
edited): build_10-09_ru.tr_line / now_fut_units / now_fut_intro / pv_sentence / question (and through it build_10-01_ru
members, headings, mūlaka tails; build_10-02_ru attributes, moments, chain questions, place line; build_10-03_ru
in_units / moments(); build_10-07_ru future units; build_3-03_ru; build_5-01_ru.pv_intro; build_2-01_ru family B).

Units added in front of build_10-09_ru's plane units, for this chapter only (with_units()):
  "ye ca upekkhāya / somanassena upapajjitvā parinibbāyissanti" = «тех, кто, переродившись с невозмутимостью
      (с радостью), достигнет окончательного угасания» (build_10-12_ru.UNITS_12, as 10-06 / 10-12);
  "Xe Ye pacchimabhavikānaṃ" = «тех, кто живёт последней жизнью {in1} и {in2}» (build_3-03_ru.PERSON_UNITS_3_03,
      as 10-12);
  NEW combination: "upekkhāsampayuttapacchimacittasamaṅgīnaṃ" = «обладающих последним умом, связанным с
      невозмутимостью» (5-01 / 8 «обладающих последним умом» + 10-05 / 10-07 «последний ум, связанный с …» in the
      instrumental).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-10_ru.py   [--probe]
Import: importlib.import_module("build_10-10_ru")   (importing never writes any file)
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

N = importlib.import_module("build_10-09_ru")    # section (5) driver (anuloma parts)
T = importlib.import_module("build_10-12_ru")    # UNITS_12 (ye ca upekkhāya … upapajjitvā parinibbāyissanti)
M7 = N.M7                                        # build_10-07_ru: SAMP_NOM «связанный»
F3 = N.F3                                        # build_3-03_ru: PERSON_UNITS_3_03
S = N.S                                          # build_5-01_ru: SC_UNITS
P2 = N.P2                                        # build_10-02_ru: IN_ASSOC
I, D, A3 = N.I, N.D, N.A3
CHAPTER = "10-10-indriyayamaka.md"
FINISHED_10_09 = "10-09-indriyayamaka.md"
SLIP_LOG = []

# =============================================================================================
# Units of this chapter
# =============================================================================================
# "ye ca upekkhāya upapajjitvā parinibbāyissanti" (no gender): build_10-12_ru.UNITS_12 (10-06 / 10-12 wording)
MOOD_UNITS = [(rx, ru, "rel") for rx, ru, rel in T.UNITS_12
              if rx.startswith("ye ") and "purisā" not in rx and "itthiyo" not in rx]
assert len(MOOD_UNITS) == 2 and all(ru.startswith("тех, кто, переродившись с ") for _, ru, _ in MOOD_UNITS), MOOD_UNITS

# "Rūpāvacare arūpāvacare pacchimabhavikānaṃ": build_3-03_ru (as 10-12)
TWO_PLANES_LAST = [(rx, ru, "rel") for rx, ru, rel in F3.PERSON_UNITS_3_03 if rx == r"{P}e {P}e pacchimabhavikānaṃ"]
assert TWO_PLANES_LAST == [(r"{P}e {P}e pacchimabhavikānaṃ", "тех, кто живёт последней жизнью {in1} и {in2}", "rel")]

# NEW combination: "<A>sampayuttapacchimacittasamaṅgīnaṃ" = «обладающих последним умом, связанным с <A>»
LAST_MIND_HOLDERS = dict((u[0], u[1]) for u in S.SC_UNITS)["pacchimacittasamaṅgīnaṃ"]
assert LAST_MIND_HOLDERS == "обладающих последним умом", LAST_MIND_HOLDERS
assert M7.SAMP_NOM == "связанный"
SAMP_INSTR = "связанным"                          # instrumental of 10-07 SAMP_NOM, agreeing with «умом»
HOLDER_UNITS = [(rf"{m}sampayuttapacchimacittasamaṅgīnaṃ",
                 f"{LAST_MIND_HOLDERS}, {SAMP_INSTR} {A3.s_prep(instr)}", "rel")
                for m, instr in P2.IN_ASSOC.items()]

EXTRA_UNITS = MOOD_UNITS + TWO_PLANES_LAST + HOLDER_UNITS
_EXTRA_RX = [(re.compile(rx.replace("{P}", N.PLANE_RX)), ru, kind) for rx, ru, kind in EXTRA_UNITS]


@contextlib.contextmanager
def with_units():
    """This chapter's units in front of build_10-09_ru's plane units, for the block only."""
    old = list(N._PLANE_RX)
    N._PLANE_RX[:0] = _EXTRA_RX
    try:
        yield
    finally:
        N._PLANE_RX[:] = old


# =============================================================================================
# Source points
# =============================================================================================
SLIPS = [   # (old, new, note): missing punctuation rendered as meant; each must occur exactly once
    ("tesaṃ itthindriyaṃ na uppajjati no ca tesaṃ upekkhindriyaṃ",
     "tesaṃ itthindriyaṃ na uppajjati, no ca tesaṃ upekkhindriyaṃ",
     "^6-10-387 (Ka) itthi / upekkhā: 'na uppajjati no ca tesaṃ': missing comma, rendered with it"),
    ("no ca tesaṃ manindriyaṃ na uppajjissati pacchimacittassa bhaṅgakkhaṇe tesaṃ paññindriyañca",
     "no ca tesaṃ manindriyaṃ na uppajjissati. Pacchimacittassa bhaṅgakkhaṇe tesaṃ paññindriyañca",
     "^6-10-393 (Ka) paññā / mana: no full stop between the two answer sentences ('na uppajjissati "
     "pacchimacittassa'): rendered as two sentences"),
]
# One-letter slip making another real word: kept as written (user rule), reported.
PLURAL_SLIP = ("tesaṃ itthindriyaṃ na uppajjissanti, no ca", "tesaṃ itthindriyaṃ na uppajjissati, no ca")
PLURAL_RU = ("не возникнет способность женственности, но", "не возникнут способность женственности, но")
PLURAL_NOTE = ("^6-10-385 (Kha) itthi / cakkhu: 'itthindriyaṃ na uppajjissanti' (plural verb, singular subject; "
               "parallels: uppajjissati): a one-letter slip that makes another real word, kept as written, "
               "«не возникнут способность женственности»")


def preprocess(src):
    for old, new, note in SLIPS:
        assert src.count(old) == 1, (old, src.count(old))
        src = src.replace(old, new)
        SLIP_LOG.append(note)
    return src


def tr_line(text):
    """Translate one Pāli line (block ID removed)."""
    if PLURAL_SLIP[0] in text:
        ru = tr_line(text.replace(*PLURAL_SLIP))
        assert ru.count(PLURAL_RU[0]) == 1, ru
        SLIP_LOG.append(PLURAL_NOTE)
        return ru.replace(*PLURAL_RU)
    with with_units():
        return N.tr_line(text)


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
    ("2", "связанным с"), ("1", "невозмутимостью"), ("5", "окончательного угасания"), ("2", "перерождаются"),
]


def check_10_09_unchanged():
    """build_10-09_ru's chapter comes out unchanged with this chapter's extra units."""
    src = (B.PALI_DIR / FINISHED_10_09).read_text(encoding="utf-8")
    on_disk = (B.OUT_DIR / FINISHED_10_09).read_text(encoding="utf-8")
    with with_units():
        again = N.translate_text(src)
    assert again == on_disk, "10-09 would change under the 10-10 units"


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, within the chapter and against every finished pi-6 chapter."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent within {CHAPTER}: {pb!r}"
        mine[pb] = rb
    shared, files, distinct, with_10_09 = 0, set(), set(), 0
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
                with_10_09 += f.name == FINISHED_10_09
    n_lines = sum(1 for p in src.split("\n") if B.ID_ANY.sub("", p).strip() in distinct)
    return shared, n_lines, sorted(files), with_10_09


SENT_SPLIT = re.compile(r"(?<=[.?]) (?=\S)")
LABEL_RU = re.compile(r"^\([а-я]\) ")
TAIL_RU = re.compile(r" \(На основе [^()]*\)\.?$")


def _sentences(pali_line, ru_line):
    pb, rb = B.ID_ANY.sub("", pali_line).strip(), B.ID_ANY.sub("", ru_line).strip()
    if not pb or pb.startswith("#"):
        return []
    m = I.TAIL_RE.fullmatch(pb)
    if m:
        pb, rb = m.group(1), TAIL_RU.sub("", rb)
    m = I.LABEL_RE.fullmatch(pb)
    if m:
        pb, rb = m.group(2), LABEL_RU.sub("", rb)
    ps, rs = SENT_SPLIT.split(pb), SENT_SPLIT.split(rb)
    return list(zip(ps, rs)) if len(ps) == len(rs) else []


def check_sentences(src, ru):
    """Every Pāli sentence of this chapter that also occurs in a finished Indriya chapter (10-01 … 10-12, 10-09
    included) has the same Russian sentence there. Returns {file: matches}."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        for ps, rs in _sentences(p, r):
            mine.setdefault(ps, rs)
    hits = {}
    for f in sorted(B.OUT_DIR.glob("10-*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            for ps, rs in _sentences(p, r):
                if ps in mine:
                    assert mine[ps] == rs, f"{f.name}: {ps!r}\n  theirs: {rs!r}\n  mine:   {mine[ps]!r}"
                    hits[f.name] = hits.get(f.name, 0) + 1
    return hits


def check_new_units(ru):
    """Every unit added here is used in the chapter."""
    assert "у обладающих последним умом, связанным с невозмутимостью," in ru
    assert "у обладающих последним умом, связанным с радостью," in ru
    assert "у тех, кто живёт последней жизнью в мире форм и в мире без форм" in ru
    assert "у тех, кто, переродившись с невозмутимостью, достигнет окончательного угасания, когда они умирают" in ru


def probe():
    src = preprocess((B.PALI_DIR / CHAPTER).read_text(encoding="utf-8"))
    for n, line in enumerate(src.split("\n"), 1):
        body, bid = B.ID_RE.match(line).groups()
        try:
            print(n, tr_line(body) + (bid or ""))
        except Exception as e:  # noqa: BLE001
            print(n, "FAIL", type(e).__name__, str(e)[:400])


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(CROSSBOOK)
    I.check_members()
    check_10_09_unchanged()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    nn, nd = len(N.SLIP_LOG), len(D.SLIP_LOG)
    ru = translate_text(src)
    my_slips = SLIP_LOG + N.SLIP_LOG[nn:] + D.SLIP_LOG[nd:]
    B.check_pair(src, ru, CHAPTER)
    check_new_units(ru)
    shared, n_lines, files, with_10_09 = check_against_finished(src, ru)
    sent_hits = check_sentences(preprocess(src), ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")),
          "| segments:", sum(1 for ln in src.split("\n") if B.ID_ANY.search(ln) and not ln.startswith("#")),
          f"| {n_lines} lines of this chapter occur in finished chapters ({shared} matches, {with_10_09} in 10-09; "
          "all byte-identical):", files)
    print("identical Pāli sentences in finished Indriya chapters, all byte-identical:", sent_hits)
    for s in dict.fromkeys(my_slips):
        print("slip:", s)
    print("cross-book asserts OK; 10-09 unchanged; per-line checks OK; consistency OK")


if __name__ == "__main__":
    if "--probe" in sys.argv:
        probe()
    else:
        main()
