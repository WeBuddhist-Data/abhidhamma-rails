"""Russian plain zero-shot of pi-6 (Yamaka): chapter 5-02-saccayamaka.md (Sacca pavattivāra: nirodhavāra and
the start of the uppādanirodhavāra).

Everything recurring comes from build_5-01_ru (Sacca members, SACCA_CFG, pv_intro(), SC_UNITS, the pavatti answer
and question frames), which itself carries families A / B (build_2-01_ru, build_2-02_ru), the person / place shape
(build_7-01_ru) and the moments (build_8_ru). None of those files is edited: the few additions below are applied
only inside units_5_02() (a context manager that restores the imported modules afterwards).

NEW here (listed in notes-5-02.md): three moment phrases (pacchimacittassa / maggassa ca phalassa ca /
aggamaggassa ca phalassa ca bhaṅgakkhaṇe), the single-clause place answer before "…pe…", "Yassa yattha X V…pe…",
the editorial notes of this chapter, the heading "Pavatti 3. uppādanirodhavāro" and one variant tail.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_5-02_ru.py
Import: importlib.import_module("build_5-02_ru")   (importing never writes any file; only __main__ builds)
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

S = importlib.import_module("build_5-01_ru")   # Sacca members and intros (5-01)
A, E, C, D = S.A, S.E, S.C, S.D

CHAPTER = "5-02-saccayamaka.md"
PREV = "5-01-saccayamaka.md"
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Additions to 5-01's intro units (moments; same pattern as 5-01's uppādakkhaṇe / bhaṅgakkhaṇe units)
# =============================================================================================
UNITS_5_02 = [
    (r"pacchimacittassa bhaṅgakkhaṇe", f"{S.BHANGA} последнего ума", "adv", False),     # 8 «В момент распада последнего ума»
    (r"aggamaggassa ca phalassa ca bhaṅgakkhaṇe", f"{S.BHANGA} высшего пути и плода", "adv", False),
    (r"maggassa ca phalassa ca bhaṅgakkhaṇe", f"{S.BHANGA} пути и плода", "adv", False),
]
assert D.WHO["Pacchimacittassa bhaṅgakkhaṇe"][0] == cap(UNITS_5_02[0][1])                 # 8, byte-identical

# Variant tail (after the sigla), as 5-01's VARIANT_TAILS
TAILS_5_02 = {"uppādavāre pana pāṭhantaraṃ natthi": "но в разделе о возникновении другого чтения нет"}


@contextlib.contextmanager
def units_5_02():
    """Prepend the 5-02 units to build_5-01_ru.ALL_UNITS and add the variant tail, for the block only."""
    old_units, old_tails = list(S.ALL_UNITS), dict(S.VARIANT_TAILS)
    S.ALL_UNITS[:0] = UNITS_5_02
    S.VARIANT_TAILS.update(TAILS_5_02)
    try:
        with E.extra_units():
            yield
    finally:
        S.ALL_UNITS[:] = old_units
        S.VARIANT_TAILS.clear()
        S.VARIANT_TAILS.update(old_tails)


# =============================================================================================
# Headings, closings, notes
# =============================================================================================
PROTEKANIE = B.SECTION_HEADINGS["Pavatti 2. nirodhavāro"].split(" 2. ")[0]            # «Протекание» (sample)
assert PROTEKANIE == "Протекание"
H_PAVATTI_3 = C.heading_case(f"{PROTEKANIE} 3. {lower1(B.SECTION_HEADINGS['Uppādanirodhavāro'])}")


def in_varo(key):
    """Section heading «Раздел о …» -> «в разделе о …» (prepositional; E.IN_UPPADAVARE)."""
    h = B.SECTION_HEADINGS[key]
    assert h.startswith("Раздел ")
    return "в разделе " + h[len("Раздел "):]


IN_UPPADA = in_varo("Uppādavāro")                   # в разделе о возникновении
IN_NIRODHA = in_varo("Nirodhavāro")                 # в разделе о прекращении
IN_UPPADANIRODHA = in_varo("Uppādanirodhavāro")     # в разделе о возникновении и прекращении
assert IN_UPPADA == E.IN_UPPADAVARE
# uppāde / nirodhe / uppādanirodhe (without -vāre): «при возникновении / прекращении / возникновении и прекращении»
AT_UPPADA, AT_NIRODHA, AT_UPPADANIRODHA = "при возникновении", "при прекращении", "при возникновении и прекращении"
ANULOMA_PACCANIKA = "и в утвердительной, и в отрицательной форме"        # anulomampi paccanīkampi
NATTHI_NANAKARANAM = "различия нет"                                       # natthi nānākaraṇaṃ
ASAMMOHANTENA = "не допуская путаницы"                                    # asammohantena (3-01)
ATITA_PUCCHA = "вопросы о прошлом"                                        # atītā pucchā (Atītavāro «Раздел о прошлом»)
PACCUPPANNATITA_PUCCHA = "вопросы о настоящем и прошлом"                  # paccuppannaatītā pucchā
SAME_YY = f"И {S.YASSAKA}, и {S.YASSAYATTHAKA} одинаковы"                 # Yassakampi yassayatthakampi sadisaṃ
NIRODHASAMAPANNANAM = "у вошедших в медитативное достижение прекращения"  # SC_UNITS "nirodhasamāpannānaṃ" + «у»
IN_YY = "в разделе с «у кого где»"                                        # yassayatthake


def _in(what):
    """«раздел с «где»» -> «в разделе с «где»»."""
    assert what.startswith("раздел ")
    return "в разделе " + what[len("раздел "):]


assert _in(S.YASSAYATTHAKA) == IN_YY
assert ("у " + dict((u[0], u[1]) for u in S.SC_UNITS)["nirodhasamāpannānaṃ"]) == NIRODHASAMAPANNANAM


def note_samudaya_magga():
    """^6-5-152: the one difference of the (Ca) section, rendered with the answer machinery of 5-01."""
    s = ("Aggamaggassa bhaṅgakkhaṇe arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati "
         "samudayasaccañca nuppajjissati")
    body = lower1(S.pv_sentence(s, CFG)[:-1])
    diff = (f"для {S.SACCA_K['samudaya']['gen']} и {S.SACCA_K['magga']['gen']} есть различие")
    return f"({SAME_YY}, {diff}: {body})."


def line_6_5_148():
    """^6-5-148: two abbreviated answer intros and a note on one line."""
    i1 = S.pv_intro("Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti "
                    "asaññasattānaṃ", True).rstrip()
    i2 = lower1(S.pv_intro("itaresaṃ catuvokārānaṃ pañcavokārānaṃ", True).rstrip())
    return f"{i1} … {i2}… " + NOTES["(Yassakampi yassayatthakampi sadisaṃ)."]


NOTES = {
    "(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ).":
        f"({cap(S.YATTHAKA)} одинаков и {AT_UPPADA}, и {AT_NIRODHA}, и {AT_UPPADANIRODHA}, {NATTHI_NANAKARANAM}).",
    # comma missing before "natthi" (rendered as meant)
    "(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ).":
        f"({cap(S.YATTHAKA)} одинаков и {IN_UPPADA}, и {IN_NIRODHA}, и {IN_UPPADANIRODHA}, {NATTHI_NANAKARANAM}).",
    "(Yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        f"({cap(S.YASSAYATTHAKA)} тоже {C.VITTHARETABBAM} одинаково).",
    "(Yassakampi yassayatthakampi sadisaṃ).": f"({SAME_YY}).",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti cetaṃ na kātabbaṃ).":
        f"({SAME_YY}, но {IN_YY} не следует указывать это: «{NIRODHASAMAPANNANAM}»).",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ).":
        f"({SAME_YY}, но {IN_YY} не следует указывать «{NIRODHASAMAPANNANAM}»).",
    "(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, "
    "natthi nānākaraṇaṃ).":
        f"(Как {IN_UPPADA} разобраны {ATITA_PUCCHA} {ANULOMA_PACCANIKA}, так же следует разбирать и "
        f"{AT_NIRODHA}, {NATTHI_NANAKARANAM}).",
    "(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ).":
        f"({cap(ATITA_PUCCHA)} так же, как они разобраны {IN_UPPADA}, следует разбирать и {IN_UPPADANIRODHA}: "
        f"{ANULOMA_PACCANIKA}).",
    "(Paccuppannaatītā pucchā uppādavārepi uppādanirodhavārepi yassakampi yatthakampi yassayatthakampi "
    "anulomampi paccanīkampi sadisaṃ, asammohantena vibhajitabbā).":
        f"({cap(PACCUPPANNATITA_PUCCHA)} одинаковы и {IN_UPPADA}, и {IN_UPPADANIRODHA}, и {_in(S.YASSAKA)}, "
        f"и {_in(S.YATTHAKA)}, и {_in(S.YASSAYATTHAKA)}, {ANULOMA_PACCANIKA}, их следует разбирать, "
        f"{ASAMMOHANTENA}).",
}

ABBR_YASSA = S.PV_ABBR_HEAD["yassa vā pana"]                              # «А у кого»
FIXED_5_02 = {
    "#### Pavatti 3. uppādanirodhavāro": "#### " + H_PAVATTI_3,
    "Nirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Nirodhavāro"]),
    # "…pe…." closes the abbreviated question (no "?" in the Pāli): «А у кого…», as "Yattha X V…pe…." = «Где …»
    "(Kha) yassa vā pana…pe…. Āmantā.": f"({B.LETTERS['Kha']}) {ABBR_YASSA}… {C.AMANTA}",
    "Yassa vā pana…pe….": f"{ABBR_YASSA}…",
}

# Variants of this chapter: anchor = the Russian the variant follows
ANCHORS_5_02 = {
    "paṭilabhissanti tassa cittassa uppādakkhaṇe (sī. syā.) uppādavāre pana pāṭhantaraṃ natthi":
        "обретёт высший путь сразу после данного ума",
    "yassakampi yatthakampi (sī. syā.)": f"И {S.YASSAKA}",
    "vattamāne, nirodhasamāpannānaṃ asaññasattānaṃ (sī. syā.)": "когда присутствует ум, не связанный с жаждой",
    "paccuppannenātītā (syā.)": cap(PACCUPPANNATITA_PUCCHA),
}

# Plain slips rendered as meant (each must occur exactly once in 5-02, after the variants are removed)
SLIPS_5_02 = [
    ("samudayasaccañca na nirujjhiti.", "samudayasaccañca na nirujjhati.",
     "^6-5-125 'nirujjhiti' = nirujjhati (spelling)"),
    ("tassa tattha samudayasaccaṃ nirujjhitthāti.", "tassa tattha samudayasaccaṃ nirujjhitthāti?",
     "^6-5-130 question ends with '.' (rendered with '?')"),
]

CFG = dict(S.SACCA_CFG)
CFG["slips"] = SLIPS_5_02
CFG["fixed"] = dict(S.SACCA_CFG["fixed"], **FIXED_5_02)
CFG["variant_anchors"] = dict(S.SACCA_CFG["variant_anchors"], **ANCHORS_5_02)

# =============================================================================================
# Pavatti lines (5-01's pv_line, plus the "…pe…" shapes of this chapter)
# =============================================================================================
S_NAMES = S.S_NAMES
# single clause before "…pe…": "Asaññasatte tattha dukkhasaccaṃ nirujjhati"
PV_SINGLE_RE = re.compile(r"(?P<intro>.+?) (?P<t>tesaṃ tattha|tesaṃ|tattha) (?P<x>" + S_NAMES + r") (?P<n>na |n)?"
                          r"(?P<v>" + A.V_RE + r")")
# "Yassa yattha dukkhasaccaṃ nirujjhati…pe…." = «У кого где прекращается истина о страдании…»
PV_ABBR_YY_RE = re.compile(r"Yassa yattha (?P<x>" + S_NAMES + r") (?P<n>na |n)?(?P<v>" + A.V_RE + r")…pe…\.")
ABBR_YY_HEAD = C.Q_PERSON_PLACE.split(",")[0]                              # «У кого где {p1}»


def pred(v, x, neg):
    return A.PV_PRED.format(v=A.verb(v, x["g"], bool(neg)), x=x["nom"])


def pv_sentence(s, cfg):
    """5-01's pv_sentence, plus a trailing "…pe…" and the single place clause."""
    pe = s.endswith("…pe…")
    core = s[: -len("…pe…")] if pe else s
    m = PV_SINGLE_RE.fullmatch(core)
    if m and m.group("t") == "tattha" and ", no ca " not in core and " ca " not in core:
        ru = S.place_intro(m.group("intro")) + pred(m.group("v"), cfg["pv_subj"][m.group("x")], m.group("n")) + "."
    else:
        ru = S.pv_sentence(core, cfg)
    return ru[:-1] + "…" if pe else ru


def pv_answers(text, cfg):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        out.append(pv_sentence(s[:-1], cfg))
    return " ".join(out)


def pv_line(text, cfg):
    for tail, note in cfg.get("abbr_notes", {}).items():
        if text.endswith(" " + tail):
            head = E.pv_abbr(text[: -len(tail) - 1] + ".", cfg["pv_subj"])
            assert head and head.endswith("…"), text
            return f"{head} {note}."
    r = E.pv_abbr(text, cfg["pv_subj"])
    if r is not None:
        return r
    m = PV_ABBR_YY_RE.fullmatch(text)
    if m:
        return ABBR_YY_HEAD.format(p1=pred(m.group("v"), cfg["pv_subj"][m.group("x")], m.group("n"))) + "…"
    if "?" in text:
        q, _, rest = text.partition("?")
        out = S.pv_question_any(q, cfg)
        rest = rest.strip()
        if rest in ("…Pe….", "…pe…."):
            return out + "…"
        return out + (" " + pv_answers(rest, cfg) if rest else "")
    return pv_answers(text, cfg)


SPECIAL = {}   # filled in translate_text (needs the units): Pāli line -> Russian


def tr(text, cfg):
    """One Pāli line of the pavattivāra (block ID removed)."""
    if not text.strip():
        return ""
    if text in cfg["fixed"] or text in B.FIXED or text.startswith("#"):
        return S.tr(text, cfg, "pv")
    variants, t = S._variants(text, cfg)
    for old, new, note in cfg["slips"]:
        if old in t:
            t = t.replace(old, new)
            SLIP_LOG.append(note)
    if t in SPECIAL:
        return S._insert_variants(SPECIAL[t], variants, cfg)
    if t in NOTES:
        return S._insert_variants(NOTES[t], variants, cfg)
    label = ""
    m = S.LABEL_RE.fullmatch(t)
    if m:
        label, t = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    return S._insert_variants(label + pv_line(t, cfg), variants, cfg)


def translate_text(src, cfg=None):
    cfg = cfg or CFG
    out = []
    with units_5_02():
        SPECIAL.clear()
        SPECIAL.update({
            "(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, aggamaggassa "
            "bhaṅgakkhaṇe, arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati samudayasaccañca "
            "nuppajjissati).": note_samudaya_magga(),
            "Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ "
            "tesaṃ tattha …pe… itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha…pe…. (Yassakampi "
            "yassayatthakampi sadisaṃ).": line_6_5_148(),
        })
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(tr(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# Strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
CROSSBOOK = [
    ("5", "момент распада"), ("1", "плод"), ("5", "медитативное достижение прекращения"),
]


def check_slips(src):
    plain = S.VARIANT_RE.sub("", src)
    for old, _, note in SLIPS_5_02:
        assert plain.count(old) == 1, f"slip pattern must occur once: {note}"


def check_5_01_unchanged():
    """My tr() on every pavatti line of 5-01 gives 5-01's Russian line byte for byte."""
    src = (B.PALI_DIR / PREV).read_text(encoding="utf-8").split("\n")
    ru = (B.OUT_DIR / PREV).read_text(encoding="utf-8").split("\n")
    cfg = dict(S.SACCA_CFG)
    pv, n = False, 0
    with units_5_02():
        for p, r in zip(src, ru):
            body, bid = B.ID_RE.match(p).groups()
            if body.startswith("#") and "Pavatti" in body:
                pv = True
            if not pv:
                continue
            assert tr(body, cfg) + (bid or "") == r, (p, r)
            n += 1
    return n


def main():
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(S.CROSSBOOK)
    A.check_crossbook(CROSSBOOK)
    C.check_crossbook_c()
    assert ASAMMOHANTENA in (B.OUT_DIR / "3-01-ayatanayamaka.md").read_text(encoding="utf-8")
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    check_slips(src)
    n = check_5_01_unchanged()
    SLIP_LOG.clear()
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    prev = [((B.PALI_DIR / f).read_text(encoding="utf-8"), (B.OUT_DIR / f).read_text(encoding="utf-8"))
            for f in B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "7-01-anusayayamaka.md",
                                       "8-cittayamaka.md", PREV]]
    A.consistency(prev + [(src, ru)])
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print(f"5-01 pavatti lines re-translated byte-identical: {n}")
    for s in SLIP_LOG + S.SLIP_LOG + A.SLIP_LOG:
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 7-01, 8, 5-01)")


if __name__ == "__main__":
    main()
