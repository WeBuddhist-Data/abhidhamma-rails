"""Russian plain zero-shot of pi-6 (Yamaka): chapter 3-03-ayatanayamaka.md.

Āyatana members, helpers and the driver come from build_3-01_ru / build_3-02_ru (imported, never edited);
families A / B from build_2-01_ru / build_2-02_ru, the person / place shape from build_7-01_ru.  This module adds:
  - person units "ye ca Xaṃ [Yaṃ] upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ / tesaṃ cavantānaṃ" and
    "Xe Ye pacchimabhavikānaṃ" (patched into build_3-02_ru only inside ay3_units());
  - fully abbreviated questions "yassa vā pana [yattha] [X]…pe… V-ti?" = «А у кого [где] [X]… V?»;
  - lines holding several question / answer pairs (split before each new "Yassa / Yattha" sentence);
  - "Uppādavāro." = «Раздел о возникновении.» (7-01 VARO_CLOSING).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_3-03_ru.py [--dry | --probe]
Import: importlib.import_module("build_3-03_ru")   (importing never writes any file)
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

F = importlib.import_module("build_3-02_ru")    # ay2_units, pe_question, AY2_CFG, tr_line
A = F.A                                         # build_3-01_ru: members, AY_CFG
D = A.D                                         # build_2-01_ru: families A + B
C = A.C                                         # build_7-01_ru: person / place shape
E = F.E                                         # build_2-02_ru: PERSON_UNITS_2_02, pv_abbr
CHAPTER = "3-03-ayatanayamaka.md"
PREV_CHAPTERS = ["3-01-ayatanayamaka.md", "3-02-ayatanayamaka.md"]
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Family B: person units of 3-03 (wording copied from the 2-01 / 2-02 / 3-02 units)
# =============================================================================================
# 2-02: "ye ca Xaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ" = «…, когда они умирают»; the same unit with
# "tesaṃ upapajjantānaṃ" (of them, being reborn) = «…, когда они перерождаются» (upapajjati = перерождаться, 2-01).
# Two planes "Xaṃ Yaṃ" / "Xe Ye" = «{in1} и {in2}» as 2-01 "{P}aṃ {P}aṃ upapajjantānaṃ" and 3-02.
_YE2 = "тех, кто, переродившись {in1} и {in2}, достигнет окончательного угасания"
assert (_YE2, True) == next((ru, rel) for rx, ru, rel in F.PERSON_UNITS_3_02
                            if rx == r"ye {P}aṃ {P}aṃ upapajjitvā parinibbāyissanti")
_YE1 = next(ru for rx, ru, _ in E.PERSON_UNITS_2_02 if rx == r"ye ca {P}aṃ upapajjitvā parinibbāyissanti")
_WHEN_DYING = next(ru for rx, ru, _ in E.PERSON_UNITS_2_02
                   if rx.endswith("tesaṃ cavantānaṃ"))[len(_YE1):]            # «, когда они умирают»
assert _WHEN_DYING == ", когда они умирают", _WHEN_DYING
WHEN_REBORN = ", когда они перерождаются"                                     # tesaṃ upapajjantānaṃ
_LAST_LIFE = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"{P}e pacchimabhavikānaṃ")
assert _LAST_LIFE == "тех, кто живёт последней жизнью {in1}"
PERSON_UNITS_3_03 = [
    (r"ye ca {P}aṃ {P}aṃ upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ", _YE2 + WHEN_REBORN, True),
    (r"ye ca {P}aṃ {P}aṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ", _YE2 + _WHEN_DYING, True),
    (r"ye ca {P}aṃ {P}aṃ upapajjitvā parinibbāyissanti", _YE2, True),
    (r"ye ca {P}aṃ upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ", _YE1 + WHEN_REBORN, True),
    (r"{P}e {P}e pacchimabhavikānaṃ", _LAST_LIFE + " и {in2}", True),
]


@contextlib.contextmanager
def ay3_units():
    """build_3-02_ru.ay2_units() plus the 3-03 person units, for the block only."""
    old = F.UNITS
    F.UNITS = PERSON_UNITS_3_03 + [u for u in old if u not in PERSON_UNITS_3_03]
    try:
        with F.ay2_units():
            yield
    finally:
        F.UNITS = old


# =============================================================================================
# Fully abbreviated questions: "yassa vā pana [yattha] [X]…pe… V-ti?"
# =============================================================================================
# 7-02 "(Kha) yattha vā pana…pe…?" = «(б) А где…?»; 8 "Yassa vā pana…pe…?" = «А у кого…?». The quoted verb of the
# second clause stays: "…pe… uppajjitthāti?" = «… возникала?» (its subject is an unnamed sense base: сфера, f).
ABBR_Q_RE = re.compile(r"(?P<rel>yassa vā pana yattha|yassa vā pana|yattha vā pana|yassa yattha|yassa|yattha)"
                       r"(?: (?P<x>\S+))?…pe…(?: (?P<n>na |n)?(?P<v>" + D.VTI_RE + r"))?")
assert {v["g"] for v in A.AY_PV_SUBJ.values()} == {"f"}


def abbr_question(body, subj):
    m = ABBR_Q_RE.fullmatch(lower1(body))
    if not m:
        return None
    rel = m.group("rel")
    kind = "yassa yattha" if ("yassa" in rel and "yattha" in rel) else ("yassa" if "yassa" in rel else "yattha")
    head = D.PV_Q[kind].split(" {p1}")[0]                       # «У кого» / «Где» / «У кого где»
    out = (D.PV_KHA + lower1(head)) if "vā pana" in rel else head
    if m.group("x"):
        out += " " + subj[m.group("x")]["nom"]
    out += "…"
    if m.group("v"):
        out += " " + D.verb(D.PV_VERB_TI[m.group("v")], "f", bool(m.group("n")))
    return out + "?", {"g": "f"}


def abbr_line(text, cfg):
    label = ""
    m = A.LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    q, sep, a = text.partition("?")
    if not sep:
        return None
    r = abbr_question(q, cfg["pv_subj"])
    if r is None:
        return None
    ru, y = r
    return label + ru + (" " + A.ay_answers(a, cfg, y) if a.strip() else "")


# =============================================================================================
# Fixed lines, slips
# =============================================================================================
AY3_FIXED = dict(F.AY2_FIXED)
AY3_FIXED.update({
    "Uppādavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādavāro"]),
})
SLIPS = [   # (old, new, note): normalised for parsing; each must occur exactly once
    ("yassa =93 yattha", "yassa yattha",
     "^6-3-118: stray '=93' between 'yassa' and 'yattha' (not Pāli; dropped, as in the English rails)"),
    ("manāyatanañca uppajjati, dhammāyatanañca uppajjissati",
     "manāyatanañca uppajjati dhammāyatanañca uppajjissati",
     "^6-3-89: comma inside 'X ca uppajjati, Y ca uppajjissati' (parallel lines have none; the Russian frame "
     "«и …, и …» has its comma anyway)"),
    ("tesaṃ tattha manāyatanaṃ nuppajjissati cakkhāyatanañca nuppajjati",
     "tesaṃ tattha manāyatanañca nuppajjissati cakkhāyatanañca nuppajjati",
     "^6-3-100: 'manāyatanaṃ nuppajjissati cakkhāyatanañca nuppajjati': first 'ca' missing (parallel lines have "
     "it); the Russian «не возникнет X и не возникает Y» is the same either way"),
    ("tesaṃ tattha cakkhāyatanañca nuppajjittha dhammāyatanaṃ nuppajjissati",
     "tesaṃ tattha cakkhāyatanañca nuppajjittha dhammāyatanañca nuppajjissati",
     "^6-3-116: 'cakkhāyatanañca nuppajjittha dhammāyatanaṃ nuppajjissati': second 'ca' missing (parallel lines "
     "have it); the Russian «не возникала X и не возникнет Y» is the same either way"),
]


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


AY3_CFG = dict(F.AY2_CFG)
AY3_CFG["fixed"] = AY3_FIXED
SPLIT_RE = re.compile(r"(?<=[.?]) (?=(?:\(\w+\) )?(?:Yassa|Yattha) )")


# =============================================================================================
# Driver
# =============================================================================================
def tr_line(text, cfg=None):
    cfg = AY3_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    text = preprocess(text)
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text.startswith("#"):
        return F.tr_line(text, cfg)
    m = A.TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), cfg) + f" ({A.TAILS[m.group(2)]}){m.group(3)}"
    parts = SPLIT_RE.split(text)
    if len(parts) > 1:                       # several question / answer pairs on one line
        return " ".join(tr_line(p, cfg) for p in parts)
    r = abbr_line(text, cfg)
    if r is not None:
        return r
    return F.tr_line(text, cfg)


def translate_text(src, cfg=None):
    out = []
    with ay3_units():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("1", "в мире чувственных желаний"), ("1", "в мире форм"), ("1", "в мире без форм"),
    ("2", "достигают окончательного угасания"), ("2", "перерождаются"), ("2", "умирают"),
]


def check_previous_unchanged():
    """3-01 and 3-02 must come out unchanged under the 3-03 units and driver."""
    pairs = []
    for name in PREV_CHAPTERS:
        src = (B.PALI_DIR / name).read_text(encoding="utf-8")
        on_disk = (B.OUT_DIR / name).read_text(encoding="utf-8")
        cfg = A.AY_CFG if name.startswith("3-01") else F.AY2_CFG
        with ay3_units():
            again = F.translate_text(src, cfg) if name.startswith("3-02") else A.translate_text(src, cfg)
        assert again == on_disk, f"{name} output would change with the 3-03 person units"
        pairs.append((src, on_disk))
    return pairs


def probe():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    bad = 0
    with ay3_units():
        for n, line in enumerate(src.split("\n"), 1):
            body, _ = B.ID_RE.match(line).groups()
            try:
                tr_line(body)
            except Exception as ex:  # noqa: BLE001
                bad += 1
                print(f"{n}: {type(ex).__name__}: {str(ex)[:300]}")
    print("failing lines:", bad)


def main():
    if "--probe" in sys.argv:
        probe()
        return
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(A.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    prev = check_previous_unchanged()
    SLIP_LOG.clear()
    A.SLIP_LOG.clear()
    F.SLIP_LOG.clear()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    pairs = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
             for n in B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "7-01-anusayayamaka.md"]]
    D.consistency(pairs + prev + [(src, ru)])
    if "--dry" in sys.argv:
        print(ru)
        return
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in dict.fromkeys(SLIP_LOG + F.SLIP_LOG + A.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 3-01, 3-02, 7-01); "
          "3-01 / 3-02 unchanged")


if __name__ == "__main__":
    main()
