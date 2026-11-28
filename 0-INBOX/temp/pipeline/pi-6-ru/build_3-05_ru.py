"""Russian plain zero-shot of pi-6 (Yamaka): chapter 3-05-ayatanayamaka.md
(nirodhavāra: present-future, past-future; uppādanirodhavāra: present, past).

Āyatana members, helpers and the driver come from build_3-01_ru … build_3-04_ru (imported, never edited);
families A / B from build_2-01_ru / build_2-02_ru, the person / place shape from build_7-01_ru.
This module adds:
  - person unit "Xe Ye parinibbantānaṃ" = «тех, кто достигает окончательного угасания {in1} и {in2}» (2-01 unit
    + " и {in2}", as 3-03's "Xe Ye pacchimabhavikānaṃ"; patched into build_3-02_ru.UNITS only inside ay5_units());
  - abbreviated answers "<persons> tesaṃ [tattha]…pe… <persons> tesaṃ [tattha]…pe…." = «У … [там]… у … [там]…»;
  - abbreviated questions without "?" ("(Kha) yassa vā pana [yattha] X…pe….", "Yassa [yattha] X na V…pe….");
  - "? No." / "? No …pe…." / "? Āmantā …pe…." answers, the uppādanirodhavāra heading and the notes.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_3-05_ru.py [--dry | --probe [--show]]
Import: importlib.import_module("build_3-05_ru")   (importing never writes any file)
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

H = importlib.import_module("build_3-04_ru")    # ay4_units, beings_abbr, AY4_CFG, tr_line, IN_* notes
G = H.G                                         # build_3-03_ru: abbr_question, SPLIT_RE
F = H.F                                         # build_3-02_ru: UNITS, pe_question
A = H.A                                         # build_3-01_ru: members, AY_CFG
D = H.D                                         # build_2-01_ru: families A + B
C = H.C                                         # build_7-01_ru: person / place shape
E = H.E                                         # build_2-02_ru
CHAPTER = "3-05-ayatanayamaka.md"
PREV_CHAPTERS = ["3-01-ayatanayamaka.md", "3-02-ayatanayamaka.md", "3-03-ayatanayamaka.md",
                 "3-04-ayatanayamaka.md"]
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Family B: "Rūpāvacare arūpāvacare parinibbantānaṃ"
# =============================================================================================
_PARINIB = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"{P}e parinibbantānaṃ")
assert _PARINIB == "тех, кто достигает окончательного угасания {in1}", _PARINIB
PERSON_UNITS_3_05 = [
    (r"{P}e {P}e parinibbantānaṃ", _PARINIB + " и {in2}", True),     # as 2-01 "{P}ā {P}ā cavantānaṃ"
]


@contextlib.contextmanager
def ay5_units():
    """build_3-04_ru.ay4_units() plus the 3-05 person unit (in build_3-02_ru.UNITS), for the block only."""
    with H.ay4_units():
        old = F.UNITS
        F.UNITS = PERSON_UNITS_3_05 + [u for u in old if u not in PERSON_UNITS_3_05]
        try:
            yield
        finally:
            F.UNITS = old


# =============================================================================================
# Abbreviated answers: "<persons> tesaṃ [tattha]…pe… <persons> tesaṃ [tattha]…pe…."
# =============================================================================================
# Each part stands for a whole answer sentence; the person intro is the usual one (A.ay_person_intro, patched);
# "tattha" = «там» (2-01 PV_TAM); without "tattha" the closing comma of the intro gives way to the "…" (as 8's
# "Itaresaṃ … tesaṃ…pe…." = «У остальных в момент ……»). Later parts are lower-case in the Pāli and stay so.
PE_ANS_RE = re.compile(r"(?P<intro>.+?) tesaṃ(?P<tt> tattha)?…pe…")


def pe_answer(text):
    if "?" in text or not text.endswith("…pe….") or "tesaṃ" not in text:
        return None
    parts = text[: -len(".")].split("…pe… ")
    parts[-1] = parts[-1][: -len("…pe…")]
    out = []
    for p in parts:
        m = PE_ANS_RE.fullmatch(p + "…pe…")
        if not m:
            return None
        intro = A.ay_person_intro(m.group("intro"))
        ru = intro + D.PV_TAM.rstrip() if m.group("tt") else intro.rstrip().rstrip(",")
        out.append(ru)
    return cap("… ".join(lower1(r) for r in out)) + "…"


# =============================================================================================
# Abbreviated questions with no "?" in the Pāli ("…pe…." closes them: «…», as 2-02 "Yattha X V…pe….")
# =============================================================================================
ABBR_STMT_RE = re.compile(r"(?:\((?P<lab>Ka|Kha)\) )?(?P<body>(?:[Yy]assa|[Yy]attha) .*…pe…)\.")
# "Yassa [yattha] X [na] V…pe…." (verb before the "…pe…"): first clause of C.Q_PERSON / C.Q_PERSON_PLACE
PV_ABBR_Y_RE = re.compile(r"(?P<rel>Yassa yattha|Yassa) (?P<x>\S+) (?P<n>na |n)?(?P<v>" + D.V_RE + r")…pe…\.")


def abbr_stmt(text, subj):
    m = PV_ABBR_Y_RE.fullmatch(text)
    if m:
        x = subj[m.group("x")]
        kind = "yassa yattha" if "yattha" in m.group("rel") else "yassa"
        p1 = D.PV_PRED.format(v=D.verb(m.group("v"), x["g"], bool(m.group("n"))), x=x["nom"])
        return D.PV_Q[kind].split(",")[0].format(p1=p1) + "…"
    m = ABBR_STMT_RE.fullmatch(text)
    if not m or "?" in text:
        return None
    r = G.abbr_question(m.group("body"), subj)
    if r is None:
        return None
    q = r[0]
    assert q.endswith("…?"), q
    return (f"({B.LETTERS[m.group('lab')]}) " if m.group("lab") else "") + q[:-1]


# =============================================================================================
# Headings, closings, notes (composed from the approved headings and the 2-02 / 3-01 … 3-04 / 5-01 frames)
# =============================================================================================
PROTEKANIE = B.SECTION_HEADINGS["Pavatti 2. nirodhavāro"].split(" 2. ")[0]            # «Протекание» (sample)
assert PROTEKANIE == "Протекание"
H_PAVATTI_3 = C.heading_case(f"{PROTEKANIE} 3. {lower1(B.SECTION_HEADINGS['Uppādanirodhavāro'])}")
IN_PACCUPPANNATITA = H._sec("Paccuppannātītavāro")      # в разделе о настоящем и прошлом
YASSAYATTHAKA = H.YASSAYATTHAKA                         # раздел с «у кого где»
NO_WORD = C.NO[:-1]                                     # «Нет» (quoted inside a note)
VITTHARITAM = "развёрнуто"                              # vitthāritaṃ (neuter; 3-04 vitthāritā «развёрнут»)
TIVIDHAM = "тремя способами"                            # tividhaṃ
TIVIDHA_PALI = " (yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ)."
TIVIDHA_RU = (f" (как {IN_PACCUPPANNATITA} {VITTHARITAM} {TIVIDHAM}, так же {C.VITTHARETABBAM} и это).")
TISUPI_VARESU = "во всех трёх разделах"                 # tīsupi vāresu
# "(yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu sadisaṃ)"
# kātabbaṃ = «следует изложить» (2-02 YATTHAKAM_PARIPUNNAM, 5-01 "yassayatthakasadisaṃ kātabbaṃ"); sadisaṃ =
# «одинаков» (3-04); yatthakaṃ repeated three times in the Pāli: kept.
_YK = A.YATTHAKA
YATTHAKA_NOTE = (f"({_YK} не следует излагать с ответом «{NO_WORD}», {_YK} следует изложить так же, как остальные "
                 f"разделы с «где», {_YK} одинаков {TISUPI_VARESU})")
assert _YK == "раздел с «где»" and YATTHAKA_NOTE.count("раздел с «где»") == 3
SAME_YY = f"(И {A.YASSAKA}, и {YASSAYATTHAKA} одинаковы)."      # (Yassakampi yassayatthakampi sadisaṃ).
# "(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ)." 3-04's ATITA_NOTE frame
ATITA_NOTE_2 = (f"({cap(H.ATITA_PUCCHA)} {H.IN_UPPADA}, {H.IN_NIRODHA} и {H.IN_UPPADANIRODHA} одинаков и в "
                f"утвердительной, и в отрицательной форме).")
assert H.ATITA_NOTE.startswith(f"({cap(H.IN_UPPADA)}, {H.IN_NIRODHA} и {H.IN_UPPADANIRODHA} {H.ATITA_PUCCHA} "
                               "одинаков и в утвердительной, и в отрицательной форме")
_pv = A._pv

AY5_FIXED = dict(H.AY4_FIXED)
AY5_FIXED.update({
    "#### Pavatti 3. uppādanirodhavāro": "#### " + H_PAVATTI_3,
    "Nirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Nirodhavāro"]),
    ("Yattha cakkhāyatanaṃ uppajjati…pe… (yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ "
     "kātabbaṃ, yatthakaṃ tīsupi vāresu sadisaṃ)."):
        H.Q_PLACE_HEAD.format(p1=_pv("uppajjati", "cakkhu")) + "… " + YATTHAKA_NOTE + ".",
    "(Yassakampi yassayatthakampi sadisaṃ).": SAME_YY,
    "(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ).": ATITA_NOTE_2,
})
assert AY5_FIXED["Nirodhavāro."] == "Раздел о прекращении."

SLIPS = [   # (old, new, note): plain spelling slips rendered as meant; each must occur exactly once
    ("Kāmāvacare parinibbāntānaṃ tesaṃ tattha…pe….", "Kāmāvacare parinibbantānaṃ tesaṃ tattha…pe….",
     "^6-3-172: 'parinibbāntānaṃ' = parinibbantānaṃ (spelling slip)"),
    ("tassa manāyatana…pe… dhammāyatanaṃ", "tassa manāyatanaṃ…pe… dhammāyatanaṃ",
     "^6-3-186: 'manāyatana…pe…' (final ṃ missing) = manāyatanaṃ"),
]
# A punctuation mark present in the Pāli stays (user rule): the stray comma inside the "ca … ca" pair of ^6-3-195 is
# parsed without it and put back into the Russian at the same joint (asserted: exactly one place).
KEPT_COMMAS = [
    ("tattha manāyatanañca na nirujjhissati, cakkhāyatanañca na nirujjhittha.",
     "tattha manāyatanañca na nirujjhissati cakkhāyatanañca na nirujjhittha.",
     D.PV_NEG_MIXED_FRAME.format(v1="прекратится", x=A.AY_K["mana"]["nom"], v2="прекращалась",
                                 y=A.AY_K["cakkhu"]["nom"]),
     "^6-3-195: comma inside 'manāyatanañca na nirujjhissati, cakkhāyatanañca na nirujjhittha' kept as written "
     "(«не прекратится сфера ума, и не прекращалась сфера глаза»)"),
]


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


AY5_CFG = dict(H.AY4_CFG)
AY5_CFG["fixed"] = AY5_FIXED
ANS_TAIL_RE = re.compile(r"(?P<q>.+\?) (?P<a>No|Āmantā)(?P<pe> …pe…)?\.")


# =============================================================================================
# Driver
# =============================================================================================
def tr_line(text, cfg=None):
    cfg = AY5_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    text = preprocess(text)
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    for old, new, ru_plain, note in KEPT_COMMAS:
        if text.endswith(old):
            ru = tr_line(text[: -len(old)] + new, cfg)
            assert ru.count(ru_plain) == 1, (ru_plain, ru)
            SLIP_LOG.append(note)
            return ru.replace(ru_plain, ru_plain.replace(" и не ", ", и не ", 1))
    if text.startswith("#"):
        return H.tr_line(text, cfg)
    if text.endswith(TIVIDHA_PALI):
        ru = tr_line(text[: -len(TIVIDHA_PALI)] + ".", cfg)
        assert ru.endswith("…"), ru
        return ru + TIVIDHA_RU
    m = A.TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), cfg) + f" ({A.TAILS[m.group(2)]}){m.group(3)}"
    m = ANS_TAIL_RE.fullmatch(text)
    if m and "? " not in m.group("q"):
        a = C.NO if m.group("a") == "No" else B.AMANTA
        return tr_line(m.group("q"), cfg) + " " + (a[:-1] + "…" if m.group("pe") else a)
    r = abbr_stmt(text, cfg["pv_subj"])
    if r is not None:
        return r
    r = pe_answer(text)
    if r is not None:
        return r
    q, sep, a = text.partition("? ")
    if sep and pe_answer(a) is not None:
        return tr_line(q + "?", cfg) + " " + pe_answer(a)
    return H.tr_line(text, cfg)


def translate_text(src, cfg=None):
    out = []
    with ay5_units():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("1", "в мире чувственных желаний"), ("1", "в мире форм"), ("1", "в мире без форм"),
    ("2", "достигают окончательного угасания"), ("2", "умирают"), ("2", "перерождаются"), ("5", "? Нет."),
]


def check_previous_unchanged():
    """3-01 … 3-04 must come out unchanged under the 3-05 person unit."""
    pairs = []
    for name in PREV_CHAPTERS:
        src = (B.PALI_DIR / name).read_text(encoding="utf-8")
        on_disk = (B.OUT_DIR / name).read_text(encoding="utf-8")
        with ay5_units():
            if name.startswith("3-01"):
                again = A.translate_text(src, A.AY_CFG)
            elif name.startswith("3-02"):
                again = F.translate_text(src, F.AY2_CFG)
            elif name.startswith("3-03"):
                again = G.translate_text(src, G.AY3_CFG)
            else:
                again = H.translate_text(src, H.AY4_CFG)
        assert again == on_disk, f"{name} output would change with the 3-05 person unit"
        pairs.append((src, on_disk))
    return pairs


def probe(show=False):
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    bad = 0
    with ay5_units():
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
    for log in (SLIP_LOG, H.SLIP_LOG, G.SLIP_LOG, F.SLIP_LOG, A.SLIP_LOG):
        log.clear()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    for old, _, _, note in KEPT_COMMAS:
        assert src.count(old) == 1, f"kept-comma pattern must occur once: {note}"
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
    for s in dict.fromkeys(SLIP_LOG + H.SLIP_LOG + G.SLIP_LOG + F.SLIP_LOG + A.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 7-01, 3-01 … 3-04); "
          "3-01 … 3-04 unchanged")


if __name__ == "__main__":
    main()
