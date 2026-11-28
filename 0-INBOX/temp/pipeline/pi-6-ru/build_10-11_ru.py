"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-11-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra, (5) Paccuppannānāgatavāro, (Ca) paccanīkapuggalokāsā).

Present + future, negative, persons and places ("yassa yattha X na uppajjati tassa tattha Y na uppajjissatīti?").
The anuloma parts of the same section are 10-09: its driver is used unchanged (imported, never edited):
  build_10-09_ru   tr_line / question / pv_sentence / now_fut_units (GENDER_UNITS, the 10-05 / 10-07 future units,
                   «тех, кто в последний раз перерождается женщиной» as one group, the uppajjantānaṃ slip log)
and, for the units 10-09's chapter does not have, these finished units are put in front of its plane units
(_PLANE_RX) for this chapter only (units_11()):
  build_3-03_ru.PERSON_UNITS_3_03  "Rūpāvacare arūpāvacare pacchimabhavikānaṃ" = «тех, кто живёт последней жизнью в
                                   мире форм и в мире без форм» (3-03, the Āyatana (Ca) part of this section)
  build_10-12_ru.UNITS_12          "ye ca upekkhāya / somanassena upapajjitvā parinibbāyissanti" = «тех, кто,
                                   переродившись с невозмутимостью / с радостью, достигнет окончательного угасания»
                                   (10-06, 10-12)
  NEW (notes-10-11.md)             "upekkhāsampayuttapacchimacittasamaṅgīnaṃ" (somanassa-) = «обладающих последним
                                   умом, связанным с невозмутимостью (с радостью)» (5-01 «обладающих последним умом»
                                   + 10-02 «связанный с …» in the instrumental)

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-11_ru.py [--probe]
Import: importlib.import_module("build_10-11_ru")   (importing never writes any file)
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

N = importlib.import_module("build_10-09_ru")    # same section, anuloma: the whole driver
T = importlib.import_module("build_10-12_ru")    # "ye ca upekkhāya upapajjitvā …" units, LAST_MIND_HOLDERS
G3 = N.F3                                        # build_3-03_ru: PERSON_UNITS_3_03
P2 = N.P2                                        # build_10-02_ru: IN_ASSOC
A3 = N.A3                                        # build_3-01_ru: s_prep
D = N.D                                          # build_2-01_ru
CHAPTER = "10-11-indriyayamaka.md"
SLIP_LOG = []

# =============================================================================================
# Units this chapter adds in front of build_10-09_ru._PLANE_RX
# =============================================================================================
_TWO_LAST = [(rx, ru, "rel" if rel else "noun") for rx, ru, rel in G3.PERSON_UNITS_3_03
             if rx == r"{P}e {P}e pacchimabhavikānaṃ"]
assert len(_TWO_LAST) == 1 and _TWO_LAST[0][1] == "тех, кто живёт последней жизнью {in1} и {in2}", _TWO_LAST

_MOOD = [(rx, ru, "rel" if rel else "noun") for rx, ru, rel in T.UNITS_12 if rx.startswith("ye (?:ca )?") and ru.startswith("тех, кто")]
assert sorted(ru for _, ru, _ in _MOOD) == [
    "тех, кто, переродившись с невозмутимостью, достигнет окончательного угасания",
    "тех, кто, переродившись с радостью, достигнет окончательного угасания"], _MOOD

# NEW: "<assoc>sampayuttapacchimacittasamaṅgīnaṃ" = «обладающих последним умом, связанным с <assoc>» ("rel": the
# participle phrase is closed by a comma, «…, связанным с невозмутимостью, и у …»).
LAST_MIND_HOLDERS = T.LAST_MIND_HOLDERS                                  # «обладающих последним умом» (5-01)
SAMP_INS = "связанным"                                                   # instrumental of 10-02 «связанный»
assert P2.SAMP == "связанного"
_HOLDERS = [(rf"{a}sampayuttapacchimacittasamaṅgīnaṃ",
             f"{LAST_MIND_HOLDERS}, {SAMP_INS} {A3.s_prep(P2.IN_ASSOC[a])}", "rel")
            for a in ("somanassa", "upekkhā")]
assert _HOLDERS[1][1] == "обладающих последним умом, связанным с невозмутимостью", _HOLDERS

UNITS_11 = [(re.compile(rx.replace("{P}", N.PLANE_RX)), ru, kind) for rx, ru, kind in _TWO_LAST + _MOOD + _HOLDERS]


@contextlib.contextmanager
def units_11():
    old = N._PLANE_RX
    N._PLANE_RX = UNITS_11 + old
    try:
        yield
    finally:
        N._PLANE_RX = old


# =============================================================================================
# Lines
# =============================================================================================
def tr_line(text):
    """Translate one Pāli line (block ID removed)."""
    with units_11():
        return N.tr_line(text)


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
    ("1", "невозмутимостью"), ("5", "окончательного угасания"), ("1", "в мире без форм"),
]


def check_frames():
    """The added units reproduce the finished chapters' renderings of the same intros (3-03, 10-06 / 10-12)."""
    samples = {
        "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ asaññasattānaṃ":      # 3-03 l. 181
            "У тех, кто достигает окончательного угасания в мире чувственных желаний, у тех, кто живёт последней "
            "жизнью в мире форм и в мире без форм, и у существ без восприятия ",
        "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ":                     # 3-03 l. 185
            "У тех, кто достигает окончательного угасания в мире чувственных желаний, и у тех, кто живёт последней "
            "жизнью в мире форм и в мире без форм, ",
    }
    with units_11():
        for pali, ru in samples.items():
            got = N.now_fut_intro(pali)
            assert got == ru, (pali, got, ru)


def compare_lines(modname, src, ru):
    """Lines another builder of this section translates (10-10, run in parallel) must come out the same."""
    if not (HERE / f"{modname}.py").exists():
        return None
    M = importlib.import_module(modname)
    if not hasattr(M, "tr_line"):
        return "no tr_line yet"
    same = 0
    for p, r in zip(src.split("\n"), ru.split("\n")):
        body, bid = B.ID_RE.match(p).groups()
        if not body.strip():
            continue
        try:
            theirs = M.tr_line(body) + (bid or "")
        except Exception:  # noqa: BLE001  (their parser does not cover this line)
            continue
        assert theirs == r, f"{modname} differs:\n{p}\n  mine:   {r}\n  theirs: {theirs}"
        same += 1
    return same


def probe():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for n, line in enumerate(src.split("\n"), 1):
        body, bid = B.ID_RE.match(line).groups()
        try:
            print(n, tr_line(body) + (bid or ""))
        except Exception as e:  # noqa: BLE001
            print(n, "FAIL", type(e).__name__, str(e)[:300])
    print("slips:", N.SLIP_LOG)


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(N.CROSSBOOK)
    D.check_crossbook(T.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    N.I.check_members()
    N.check_frames()
    check_frames()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    N.CHAPTER = CHAPTER                     # check_against_finished skips this chapter's own output file
    try:
        shared, files, own = N.check_against_finished(src, ru)
    finally:
        N.CHAPTER = "10-09-indriyayamaka.md"
    c10 = compare_lines("build_10-10_ru", src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("lines identical with build_10-10_ru:", "not found" if c10 is None else c10)
    print(f"{own} lines of this chapter occur in finished chapters ({shared} matches), all identical:", files)
    for s in dict.fromkeys(SLIP_LOG + N.SLIP_LOG + N.P3.SLIP_LOG + P2.SLIP_LOG + N.I.SLIP_LOG + D.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; member asserts OK; frame asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    if "--probe" in sys.argv:
        probe()
    else:
        main()
