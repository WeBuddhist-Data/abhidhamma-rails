"""Russian plain zero-shot of pi-6 (Yamaka): chapter 3-06-ayatanayamaka.md
(uppādanirodhavāra: future, present-past, present-future, past-future; pariññāvāra; Āyatana closing).

Everything comes from build_3-05_ru (imported, never edited; through it build_3-01_ru … build_3-04_ru, families
A / B from build_2-01_ru / build_2-02_ru, the person / place shape from build_7-01_ru) and family E (pariññāvāra)
from build_2-02_ru (pj_line with an Āyatana "pj_obj"). This module adds:
  - person unit "ye Xaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ" (2-01 unit + 2-02 «, когда они умирают»);
  - answers mixing abbreviated and full parts ("<persons> tesaṃ…pe… <persons> tesaṃ X-ñca V Y-ñca V.",
    "<persons> tesaṃ tattha X…pe… …", "…, no ca tesaṃ tattha…pe… …");
  - the two "(Yathā …)" notes, the closings and the Āyatana closing.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_3-06_ru.py [--dry | --probe [--show] | --wide]
Import: importlib.import_module("build_3-06_ru")   (importing never writes any file)
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

M5 = importlib.import_module("build_3-05_ru")   # ay5_units, tr_line, pe_answer, AY5_CFG
H = M5.H                                        # build_3-04_ru: _sec, IN_*, ATITA_PUCCHA
G = M5.G                                        # build_3-03_ru
F = M5.F                                        # build_3-02_ru: UNITS
A = M5.A                                        # build_3-01_ru: members, ay_person_intro
D = M5.D                                        # build_2-01_ru: families A + B
C = M5.C                                        # build_7-01_ru: person / place shape
E = importlib.import_module("build_2-02_ru")    # family E (pariññāvāra), PERSON_UNITS_2_02
assert E is M5.E
CHAPTER = "3-06-ayatanayamaka.md"
PREV_CHAPTERS = ["3-01-ayatanayamaka.md", "3-02-ayatanayamaka.md", "3-03-ayatanayamaka.md",
                 "3-04-ayatanayamaka.md", "3-05-ayatanayamaka.md"]
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Family B: "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ" (no "ca": first in the list)
# =============================================================================================
_YE = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"ye {P}aṃ upapajjitvā parinibbāyissanti")
_YE_CA = next(ru for rx, ru, _ in E.PERSON_UNITS_2_02 if rx == r"ye ca {P}aṃ upapajjitvā parinibbāyissanti")
_YE_CA_DYING = next(ru for rx, ru, _ in E.PERSON_UNITS_2_02
                    if rx == r"ye ca {P}aṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ")
WHEN_DYING = _YE_CA_DYING[len(_YE_CA):]
assert WHEN_DYING == ", когда они умирают" and _YE == "тех, кто, переродившись {in1}, достигнет окончательного угасания"
PERSON_UNITS_3_06 = [
    (r"ye {P}aṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ", _YE + WHEN_DYING, True),
]


@contextlib.contextmanager
def ay6_units():
    """build_3-05_ru.ay5_units() plus the 3-06 person unit (in build_3-02_ru.UNITS), for the block only."""
    with M5.ay5_units():
        old = F.UNITS
        F.UNITS = PERSON_UNITS_3_06 + [u for u in old if u not in PERSON_UNITS_3_06]
        try:
            yield
        finally:
            F.UNITS = old


# =============================================================================================
# Answers mixing abbreviated and full parts (split at "…pe… "; each abbreviated part ends in «…», as 3-05's
# pe_answer; the full last part is an ordinary answer sentence, lower-case as the Pāli)
# =============================================================================================
PE = "…pe…"
PART_TT_X_RE = re.compile(r"(?P<intro>.+?) tesaṃ tattha (?P<x>\S+)")
PART_NO_CA_RE = re.compile(r"(?P<pre>.+), no ca (?P<t>tesaṃ tattha|tesaṃ)")
_DUMMY_Y = A.AY_PALI["mana"]


def pe_part(p, cfg):
    """One abbreviated part (the text before a "…pe…") -> Russian ending in «…»."""
    m = PART_NO_CA_RE.fullmatch(p)                         # "<sentence>, no ca tesaṃ tattha" (the denied Y elided)
    if m:
        full = f"{p} {_DUMMY_Y} nirujjhissati."
        ru = M5.tr_line(full, cfg)
        tail = D.PV_PRED.format(v=D.verb("nirujjhissati", A.AY_K["mana"]["g"], True), x=A.AY_K["mana"]["nom"]) + "."
        assert ru.endswith(tail) and tail.startswith("не "), (ru, tail)
        return ru[: -len(tail)] + "не…"
    m = PART_TT_X_RE.fullmatch(p)                          # "<persons> tesaṃ tattha X"
    if m and m.group("x") in cfg["pv_subj"]:
        return cap(A.ay_person_intro(m.group("intro")) + D.PV_TAM + cfg["pv_subj"][m.group("x")]["nom"]) + "…"
    return M5.pe_answer(p + PE + ".")                      # "<persons> tesaṃ [tattha]"


def _pe_answer_or_none(text):
    try:
        return M5.pe_answer(text)
    except ValueError:                                     # a part that is not "<persons> tesaṃ [tattha]"
        return None


def mixed_answer(text, cfg):
    if "?" in text or PE + " " not in text or "tesaṃ" not in text or _pe_answer_or_none(text) is not None:
        return None
    parts = text.split(PE + " ")
    last = parts.pop()
    out = []
    for p in parts:
        r = pe_part(p, cfg)
        if r is None:
            return None
        out.append(r)
    if last.endswith(PE + "."):
        r = pe_part(last[: -len(PE + ".")], cfg)
        if r is None:
            return None
        out.append(r)
    else:
        out.append(M5.tr_line(cap(last), cfg))
    return cap(" ".join(lower1(r) for r in out))


# =============================================================================================
# Notes, closings (composed from the approved headings and the 2-02 / 3-01 … 3-05 frames)
# =============================================================================================
IN_UPPADA, IN_NIRODHA, IN_UPPADANIRODHA = H.IN_UPPADA, H.IN_NIRODHA, H.IN_UPPADANIRODHA


def _pucchā(key):
    """'Paccuppannātītavāro' -> «вопрос о настоящем и прошлом» (as 3-04 ATITA_PUCCHA from «Раздел о прошлом»)."""
    h = B.SECTION_HEADINGS[key]
    assert h.startswith("Раздел "), h
    return "вопрос " + h[len("Раздел "):]


assert _pucchā("Atītavāro") == H.ATITA_PUCCHA and _pucchā("Anāgatavāro") == H.ANAGATA_PUCCHA
PACCUPPANNATITA_PUCCHA = _pucchā("Paccuppannātītavāro")      # вопрос о настоящем и прошлом
ATITANAGATA_PUCCHA = _pucchā("Atītānāgatavāro")              # вопрос о прошлом и будущем
VIBHATTA = "разобран"                                        # vibhattā / vibhattaṃ (2-02 VIBHAJITABBAM_FRAME)
VIBHAJITABBA = "следует разбирать"                           # vibhajitabbā (2-02)
assert E.VIBHAJITABBAM_FRAME == "(Как {where} " + VIBHATTA + " {what}, так же " + VIBHAJITABBA + " и здесь)."
ANULOMA_PACCANIKA = "и в утвердительной, и в отрицательной форме"   # anulomampi paccanīkampi (3-04, 3-05)
assert ANULOMA_PACCANIKA in H.ATITA_NOTE and ANULOMA_PACCANIKA in M5.ATITA_NOTE_2
# The siglum "(sī syā. ka.)" lacks the full stop after "sī" (missing punctuation, rendered as meant).
NOTE_229_PALI = ("(Yathā uppādavāre paccuppannātītā pucchā vibhattā evaṃ uppādanirodhepi paccuppannātītā pucchā "
                 "anulomampi paccanīkampi vibhajitabbā [vibhajitabbaṃ (sī syā. ka.)] ).")
NOTE_229 = (f"(Как {IN_UPPADA} {VIBHATTA} {PACCUPPANNATITA_PUCCHA}, так же и {IN_UPPADANIRODHA} "
            f"{PACCUPPANNATITA_PUCCHA} {VIBHAJITABBA} {ANULOMA_PACCANIKA} "
            f"{D.variant_ru('vibhajitabbaṃ (sī. syā. ka.)', 'чтения')}).")
# yassakampi yatthakampi yassayatthakampi = «и в разделе с «у кого», и в разделе с «где», и в разделе с «у кого где»»
NOTE_248_PALI = ("(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā yassakampi yatthakampi "
                 "yassayatthakampi anulomampi paccanīkampi vibhattaṃ, evaṃ uppādanirodhepi atītānāgatā pucchā "
                 "vibhajitabbā.)")
NOTE_248 = (f"(Как {IN_NIRODHA} {ATITANAGATA_PUCCHA} {D.variant_ru('atītenānāgatā (syā.)', 'чтения')} {VIBHATTA} "
            f"и в {A.YASSAKA}, и в {A.YATTHAKA}, и в {H.YASSAYATTHAKA}, {ANULOMA_PACCANIKA}, так же и "
            f"{IN_UPPADANIRODHA} {VIBHAJITABBA} {ATITANAGATA_PUCCHA}.)")
NOTE_248 = NOTE_248.replace("и в раздел с", "и в разделе с")
assert NOTE_248.count("и в разделе с «") == 3, NOTE_248

AY6_FIXED = dict(M5.AY5_FIXED)
AY6_FIXED.update({
    NOTE_229_PALI: NOTE_229,
    NOTE_248_PALI: NOTE_248,
    "Uppādanirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādanirodhavāro"]),
    "Pariññāvāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Pariññāvāro"]),
    "Pavattivāro niṭṭhito.": f"{E.PAVATTIVARO} {B.NITTHITO}.",
    "Āyatanayamakaṃ niṭṭhitaṃ.": B.YAMAKA_CLOSING_FRAME.format(title=B.YAMAKA_TITLES["Āyatanayamakaṃ"]),
})
assert AY6_FIXED["Āyatanayamakaṃ niṭṭhitaṃ."] == "Парные вопросы о сферах восприятия завершены."
for _k in ("Uppādanirodhavāro.", "Pariññāvāro.", "Pavattivāro niṭṭhito."):
    assert AY6_FIXED[_k] == E.KH2_CFG["fixed"][_k], _k

SLIPS = [   # (old, new, note): plain spelling slips rendered as meant; each must occur exactly once
    ("no ca tesaṃ ghānāyatanaṃ upapajjissati.", "no ca tesaṃ ghānāyatanaṃ uppajjissati.",
     "^6-3-212: 'ghānāyatanaṃ upapajjissati' (is reborn) = uppajjissati (arises), as every parallel line"),
    ("tassa tattha manāyatanaṃ …pe… dhammāyatanaṃ", "tassa tattha manāyatanaṃ…pe… dhammāyatanaṃ",
     "^6-3-217: stray space before '…pe…' (spacing only, as 3-04 ^6-3-151)"),
    ("arūpānaṃ tasaṃ tattha", "arūpānaṃ tesaṃ tattha", "^6-3-244: 'tasaṃ' = tesaṃ (spelling slip)"),
]


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


AY6_CFG = dict(M5.AY5_CFG)
AY6_CFG["fixed"] = AY6_FIXED
AY6_CFG["pj_obj"] = {A.AY_PALI[m]: "сферу " + A.AY_K_GEN[m] for m in A.AY_ORDER}   # accusative (pi-4 «сферу глаза»)
assert all(A.AY_K[m]["nom"] == "сфера " + A.AY_K_GEN[m] for m in A.AY_ORDER)


# =============================================================================================
# Driver
# =============================================================================================
def tr_line(text, cfg=None):
    cfg = AY6_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    text = preprocess(text)
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if "parijān" in text:
        r = E.pj_line(text, cfg)
        if r is not None:
            return r
    r = mixed_answer(text, cfg)
    if r is not None:
        return r
    return M5.tr_line(text, cfg)


def translate_text(src, cfg=None):
    out = []
    with ay6_units():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("4", "сферу глаза"), ("5", "полностью понимает"), ("5", "не понимает полностью"),
    ("2", "достигают окончательного угасания"), ("2", "умирают"), ("5", "? Нет."), ("5", "Да."),
]


def check_previous_unchanged():
    """3-01 … 3-05 must come out unchanged under the 3-06 person unit."""
    pairs = []
    for name in PREV_CHAPTERS:
        src = (B.PALI_DIR / name).read_text(encoding="utf-8")
        on_disk = (B.OUT_DIR / name).read_text(encoding="utf-8")
        with ay6_units():
            if name.startswith("3-01"):
                again = A.translate_text(src, A.AY_CFG)
            elif name.startswith("3-02"):
                again = F.translate_text(src, F.AY2_CFG)
            elif name.startswith("3-03"):
                again = G.translate_text(src, G.AY3_CFG)
            elif name.startswith("3-04"):
                again = H.translate_text(src, H.AY4_CFG)
            else:
                again = M5.translate_text(src, M5.AY5_CFG)
        assert again == on_disk, f"{name} output would change with the 3-06 person unit"
        pairs.append((src, on_disk))
    return pairs


def probe(show=False):
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    bad = 0
    with ay6_units():
        for n, line in enumerate(src.split("\n"), 1):
            body, _ = B.ID_RE.match(line).groups()
            try:
                r = tr_line(body)
                if show:
                    print(f"{n}: {r}")
            except Exception as ex:  # noqa: BLE001
                bad += 1
                print(f"{n}: {type(ex).__name__}: {str(ex)[:300]}")
    print("failing lines:", bad)


def main():
    if "--probe" in sys.argv:
        probe("--show" in sys.argv)
        return
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(A.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    prev = check_previous_unchanged()
    for log in (SLIP_LOG, M5.SLIP_LOG, H.SLIP_LOG, G.SLIP_LOG, F.SLIP_LOG, A.SLIP_LOG):
        log.clear()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    for k in (NOTE_229_PALI, NOTE_248_PALI):
        assert src.count(k) == 1, k
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    others = B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "7-01-anusayayamaka.md"]
    pairs = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
             for n in others]
    D.consistency(pairs + prev + [(src, ru)])
    if "--wide" in sys.argv:            # informative: identical Pāli lines against every other finished chapter
        for p in sorted(B.OUT_DIR.glob("*.md")):
            if p.name in others + PREV_CHAPTERS + [CHAPTER]:
                continue
            try:
                D.consistency([((B.PALI_DIR / p.name).read_text(encoding="utf-8"), p.read_text(encoding="utf-8")),
                               (src, ru)])
                print("consistent with", p.name)
            except AssertionError as ex:
                print("CHECK", p.name, str(ex)[:400])
        return
    if "--dry" in sys.argv:
        print(ru)
        return
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in dict.fromkeys(SLIP_LOG + M5.SLIP_LOG + H.SLIP_LOG + G.SLIP_LOG + F.SLIP_LOG + A.SLIP_LOG
                           + D.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 7-01, 3-01 … 3-05); "
          "3-01 … 3-05 unchanged")


if __name__ == "__main__":
    main()
