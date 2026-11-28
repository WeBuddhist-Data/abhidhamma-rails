"""Russian plain zero-shot of pi-6 (Yamaka): chapter 6-02-sankharayamaka.md (Saṅkhārayamaka, close).

Everything repeated comes from build_6-01_ru (imported, never edited): members, SK_UNITS, sk_intro, sk_place_intro,
pv_line, the pariññāvāra (family E via build_2-02_ru) and 6-01's notes. 6-02 has no paṇṇattivāra, so it is
translated with translate_text(src, cfg, mode="pv"). NEW here (listed in notes-6-02.md): this chapter's notes, the
heading "1-6. Paccuppannavārādi", the closing; "Pavatti 3. uppādanirodhavāro" is 5-02's heading (build_5-02_ru).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_6-02_ru.py
Import: importlib.import_module("build_6-02_ru")   (importing never writes any file; only __main__ builds)
"""
import importlib
import pathlib
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

K = importlib.import_module("build_6-01_ru")    # Saṅkhāra frames (6-01)
T3 = importlib.import_module("build_5-03_ru")   # atītānāgatā pucchā «вопросы о прошлом и будущем»
A, C, S, S2 = K.A, K.C, K.S, K.S2                # 2-01, 7-01, 5-01, 5-02 (as 6-01 loads them)

CHAPTER = "6-02-sankharayamaka.md"
cap, lower1 = K.cap, K.lower1

# =============================================================================================
# Headings and closing
# =============================================================================================
H_PAVATTI_3 = S2.FIXED_5_02["#### Pavatti 3. uppādanirodhavāro"]      # «#### Протекание 3. Раздел о возникновении и прекращении»
# "Paccuppannavārādi" as the sample's "Hetuvārādi" = «Раздел о причинах и другие»
ADI = " и другие"
assert B.SECTION_HEADINGS["Hetuvārādi"].endswith(ADI)
H_PACC_ADI = B.SECTION_HEADINGS["Paccuppannavāro"] + ADI               # «Раздел о настоящем и другие»
SK_CLOSING = B.YAMAKA_CLOSING_FRAME.format(title=B.YAMAKA_TITLES["Saṅkhārayamakaṃ"])
assert SK_CLOSING == "Парные вопросы о формирующих факторах завершены."

# =============================================================================================
# Notes (words of 5-02 / 5-03 / 3-05 / 3-06 / 6-01)
# =============================================================================================
ANULOMA_PACCANIKA = S2.ANULOMA_PACCANIKA        # и в утвердительной, и в отрицательной форме
ATITANAGATA_PUCCHA = T3.ATITANAGATA_PUCCHA      # вопросы о прошлом и будущем
VIBHATTA_PL, VIBHATTA_SG = "разобраны", "разобран"   # vibhattā (pl., 5-02 / 5-03 / 6-01) / vibhattaṃ (sg., 3-06)
VIBHAJITABBA = "следует разбирать"              # vibhajitabbā / vibhajitabbaṃ (2-02, 3-06, 5-02)
assert f"{VIBHATTA_PL} {S2.ATITA_PUCCHA}" in K.NOTES[
    "(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ "
    "nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)"]
# itaresaṃ yatthakānaṃ sadisaṃ = «так же, как остальные разделы с «где»» (3-05 ^6-3-201 words)
ITARE_YATTHAKA = f"так же, как остальные разделы с «где»"
# nirodhavārena sadisaṃ = «одинаково с разделом о прекращении»
_NIRODHA_O = B.SECTION_HEADINGS["Nirodhavāro"][len("Раздел "):]       # «о прекращении»
NIRODHAVARENA_SADISAM = f"одинаково с разделом {_NIRODHA_O}"
# pariññāvāraṃ = «раздел о полном понимании» (acc = nom); khandhayamake / saṅkhārayamake = «в парных вопросах о …»
PARINNAVARAM = lower1(B.SECTION_HEADINGS["Pariññāvāro"])


def in_yamaka(key):
    """'Khandhayamakaṃ' -> «в парных вопросах о совокупностях» (from the approved yamaka title)."""
    t = B.YAMAKA_TITLES[key]
    assert t.startswith("Парные вопросы "), t
    return "в парных вопросах " + t[len("Парные вопросы "):]


IN_KHANDHAYAMAKA, IN_SANKHARAYAMAKA = in_yamaka("Khandhayamakaṃ"), in_yamaka("Saṅkhārayamakaṃ")

NOTES_6_02 = {
    # ^6-6-135 (full stop outside the bracket, as written)
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati).":
        f"({S2.SAME_YY}, но {S2.IN_YY} не встречается {K.NIRODHA_Q}).",
    # ^6-6-136
    "(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā).":
        (f"({cap(S2.ATITA_PUCCHA)} {C.VITTHARETABBAM} одинаково и {S2.IN_UPPADA}, и {S2.IN_NIRODHA}, и "
         f"{S2.IN_UPPADANIRODHA})."),
    # ^6-6-147: "uppādavāranirodhavārepi" read as the uppādanirodhavāra (the section it stands in; English rails too)
    ("(Yathā uppādavāre paccuppannātītā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādavāranirodhavārepi "
     "paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā.)"):
        (f"(Как {S2.IN_UPPADA} {VIBHATTA_PL} {S2.PACCUPPANNATITA_PUCCHA} {ANULOMA_PACCANIKA}, так же и "
         f"{S2.IN_UPPADANIRODHA} {S2.PACCUPPANNATITA_PUCCHA} {VIBHAJITABBA} {ANULOMA_PACCANIKA}.)"),
    # ^6-6-158 group: the first clause has no verb in the Pāli (no "vibhattā"): none added
    ("(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi evaṃ uppādanirodhavārepi atītānāgatā pucchā "
     "anulomampi paccanīkampi vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.)"):
        (f"(Как {S2.IN_NIRODHA} {ATITANAGATA_PUCCHA} {ANULOMA_PACCANIKA}, так же и {S2.IN_UPPADANIRODHA} "
         f"{ATITANAGATA_PUCCHA} {VIBHAJITABBA} {ANULOMA_PACCANIKA}, {S2.ASAMMOHANTENA}, {NIRODHAVARENA_SADISAM}, "
         f"{S2.NATTHI_NANAKARANAM}.)"),
    # ^6-6-159 group
    "(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)":
        (f"(Как {IN_KHANDHAYAMAKA} {VIBHATTA_SG} {PARINNAVARAM}, так же и {IN_SANKHARAYAMAKA} {VIBHAJITABBA} "
         f"{PARINNAVARAM}.)"),
}
NOTES = dict(K.NOTES)
NOTES.update(NOTES_6_02)

FIXED = dict(K.FIXED)
FIXED.update({
    "#### Pavatti 3. uppādanirodhavāro": H_PAVATTI_3,
    "##### 1-6. Paccuppannavārādi": "##### 1-6. " + H_PACC_ADI,
    "Saṅkhārayamakaṃ niṭṭhitaṃ.": SK_CLOSING,
    # ^6-6-130: place answer cut by "…pe…" + note
    "Dutiyajjhāne tatiyajjhāne tattha…pe… (itaresaṃ yatthakānaṃ sadisaṃ).":
        K.sk_place_intro("Dutiyajjhāne tatiyajjhāne").rstrip() + f"… ({ITARE_YATTHAKA}).",
    # ^6-6-131: abbreviated question + note (lower case as in the Pāli)
    "Yassa yattha kāyasaṅkhāro uppajjati…pe… (yassakampi yassayatthakampi sadisaṃ).":
        K.pv_abbr("Yassa yattha kāyasaṅkhāro uppajjati…pe…", K.SK_CFG) + f" ({lower1(S2.SAME_YY)}).",
})

# Missing "ca" rendered as meant (the Russian «и не прекращался X, и прекратится Y» reads the same as «не
# прекращался X, и прекратится Y»; 2-02 ^6-2-134 / 163, 3-03 ^6-3-100 / 116 do the same). Must occur exactly once.
SLIPS = [
    ("tesaṃ tattha kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati",
     "tesaṃ tattha kāyasaṅkhāro ca na nirujjhittha vacīsaṅkhāro ca nirujjhissati",
     "^6-6-121 group (Ga, Atītānāgata): 'kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati': first 'ca' "
     "missing (^6-6-121 (Kha) answer has it), rendered as meant"),
]

SK2_CFG = dict(K.SK_CFG)
SK2_CFG.update({"fixed": FIXED, "notes": NOTES, "slips": SLIPS})


# Two bare planes before a moment ("Rūpāvacare arūpāvacare savitakkasavicārapacchimacittassa bhaṅgakkhaṇe …", ^6-6-126
# group): one place «в мире форм и в мире без форм» (K._TWO, 3-02 / 3-03), not two stacked «в мире форм в мире без форм».
# Added for this chapter only, right before 6-01's single-plane "loc" unit (6-01's list is restored afterwards).
TWO_PLANES_LOC = (r"({P})e ({P})e", lambda m: K._TWO.format(in1=K._in(m.group(1)), in2=K._in(m.group(2))), "loc")
assert K.SK_UNITS[-1][0] == r"({P})e"


def translate(src):
    saved = list(K.SK_UNITS)
    K.SK_UNITS.insert(len(K.SK_UNITS) - 1, TWO_PLANES_LOC)
    try:
        return unicodedata.normalize("NFC", K.translate_text(src, SK2_CFG, mode="pv"))
    finally:
        K.SK_UNITS[:] = saved


# =============================================================================================
# Checks
# =============================================================================================
OTHER_RU = {   # strings this builder composes that finished pi-6 chapters already print
    "5-02-saccayamaka.md": [H_PAVATTI_3, f"{S2.SAME_YY}, но {S2.IN_YY} не следует указывать", S2.ASAMMOHANTENA],
    "3-05-ayatanayamaka.md": [H_PAVATTI_3, ITARE_YATTHAKA],
    "5-03-saccayamaka.md": [f"{S2.IN_NIRODHA} {VIBHATTA_PL} {ATITANAGATA_PUCCHA} ",
                            f"{ANULOMA_PACCANIKA}, так же следует разбирать и {S2.IN_UPPADANIRODHA}"],
    "3-06-ayatanayamaka.md": [f"так же и {S2.IN_UPPADANIRODHA} вопрос", VIBHATTA_SG],
    "6-01-sankharayamaka.md": [f"не встречается {K.NIRODHA_Q}", S2.SAME_YY],
    "1-mulayamaka.md": [B.SECTION_HEADINGS["Hetuvārādi"]],
    "2-02-khandhayamaka.md": [B.SECTION_HEADINGS["Paccuppannavāro"], B.SECTION_HEADINGS["Pariññāvāro"]],
}


def check_other_ru():
    for name, strings in OTHER_RU.items():
        txt = (B.OUT_DIR / name).read_text(encoding="utf-8")
        for s in strings:
            assert s in txt, (name, s)
    return True


def consistency_all(src, ru):
    """Identical Pāli line -> identical Russian line: within this chapter and with every finished pi-6 chapter."""
    seen = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb:
            assert seen.setdefault(pb, rb) == rb, f"inconsistent within chapter: {pb!r}"
    bad, shared = [], 0
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb in seen:
                shared += 1
                if seen[pb] != rb:
                    bad.append((f.name, pb, seen[pb], rb))
    if bad:
        raise AssertionError("inconsistent with finished chapters:\n" + "\n".join(map(repr, bad[:10])))
    return shared


def main():
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(K.CROSSBOOK)
    C.check_crossbook_c()
    K.check_other_ru()
    check_other_ru()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, _ in SLIPS:
        assert src.count(old) == 1, old
    for key in list(NOTES_6_02) + [k for k in FIXED if k not in K.FIXED]:
        assert key in src, key
    K.SLIP_LOG.clear()
    ru = translate(src)
    B.check_pair(src, ru, CHAPTER)
    shared = consistency_all(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in sorted(set(K.SLIP_LOG)):
        print("slip:", s)
    print(f"cross-book asserts OK; per-line checks OK; consistency OK ({shared} identical Pāli lines in other chapters)")


if __name__ == "__main__":
    main()
