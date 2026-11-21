# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 6 (6-pancamanayo.md, Pañcamanayo).

usage: python -I -X utf8 build_6_vi.py
Writes AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\6-pancamanayo.md
after the pi-1 / pi-2 string checks (B.check_sources) pass.
Reuses build_sample_vi (B) verbatim; the coordinator's SHARED FRAMES are fixed strings below
(identical to the strings of build_3_vi.py for identical Pāli).
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "6-pancamanayo.md"
PALI = os.path.join(B.PALI_DIR, NAME)
OUT = os.path.join(B.OUT_DIR, NAME)

# ---------------------------------------------------------------- shared frames (coordinator)
REL = "đối với {x}, những hiện tượng nào"                     # Xena / Xāya / Xehi dhammehi ye dhammā
REL2 = "đối với những hiện tượng ấy, những hiện tượng nào"    # tehi dhammehi ye dhammā
MOD_KH_EX = "không được gộp vào theo cách gộp vào khối"        # khandhasaṅgahena asaṅgahitā
MOD_AY_EX = "không được gộp vào theo cách gộp vào lĩnh vực nhận biết"   # āyatanasaṅgahena asaṅgahitā
MOD_DH_EX = "không được gộp vào theo cách gộp vào yếu tố"      # dhātusaṅgahena asaṅgahitā
MODS_EX = f"{MOD_KH_EX}, {MOD_AY_EX}, {MOD_DH_EX}"
Q_MAIN_EX = ", thì những hiện tượng đó không được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
ANS_FULL = "Những hiện tượng đó"                                # Te dhammā (answer)
ANS_SHORT = "… những hiện tượng đó"                            # …pe… te dhammā
B.pi2("những hiện tượng đó")
B.pi2("Đối với")
B.pi1("những hiện tượng nào")
B.pi1("những hiện tượng ấy")

# ---------------------------------------------------------------- relative-clause heads
# instrumental list member -> nominative key of B (explicit where the ending is not regular)
INSTR = {
    "avijjāya": "avijjā",
    "avijjāpaccayā saṅkhārena": "avijjāpaccayā saṅkhārā",
    "saṅkhārapaccayā viññāṇena": "saṅkhārapaccayā viññāṇaṃ",
    "viññāṇapaccayā nāmarūpena": "viññāṇapaccayā nāmarūpaṃ",
    "phassapaccayā vedanāya": "phassapaccayā vedanā",
    "vedanāpaccayā taṇhāya": "vedanāpaccayā taṇhā",
    "taṇhāpaccayā upādānena": "taṇhāpaccayā upādānaṃ",
    "jātiyā": "jāti", "jarāya": "jarā", "maraṇena": "maraṇaṃ",
    "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ",
    "satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ", "jhānena": "jhānaṃ",
    "appamaññāya": "appamaññā",
    "pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
    "sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
    "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā", "cittena": "cittaṃ",
}
SUFFIX = (("āyatanena", "āyatanaṃ"), ("driyena", "driyaṃ"), ("dhātuyā", "dhātu"), ("saccena", "saccaṃ"),
          ("ena", "o"))
# matrix names as written in this chapter -> key of B.MATRIX_PRED (rendered as meant; reported)
ALIAS = {
    "na hetusahetukā": "na hetū sahetukā",               # compound spelling of the dyad name (^3-213)
    "paccupannārammaṇā": "paccuppannārammaṇā",           # single p (^3-210)
}
VARIANTS = {
    "[na hetū sahetukehi (sī.), na hetūhi sahetukehi (syā. ka.)]":
        "[khác chính tả (Sī.): na hetū sahetukehi; dị bản (Syā., Ka.): na hetūhi sahetukehi]",
}


def _nom_word(w):
    if w in ("ca", "ceva", "na", "no", "dassanena") or w.endswith("āya"):   # bhāvanāya, sukhāya vedanāya …
        return w
    if w == "hetūhi":
        return "hetū"
    for suf, nom in (("īhi", "ino"), ("ūhi", "uno"), ("ehi", "ā")):
        if w.endswith(suf):
            return w[:-len(suf)] + nom
    raise AssertionError(w)


def instr_item(p):
    """Instrumental list member (without 'ye dhammā') -> Vietnamese (lower case)."""
    p = p[:1].lower() + p[1:]
    var = ""
    m = re.fullmatch(r"(.*?) (\[[^\]]+\])( dhammehi)", p)
    if m:
        p, var = m.group(1) + m.group(3), " " + VARIANTS[m.group(2)]
    if p.endswith(" dhammehi"):                        # kusalehi dhammehi -> kusalā
        key = " ".join(_nom_word(w) for w in p[:-len(" dhammehi")].split())
    elif p.endswith("dhammehi"):                       # upādādhammehi -> upādā; vipākadhammadhammehi -> vipākadhamma
        key = p[:-len("dhammehi")]
    else:
        key = INSTR.get(p)
        if key is None:
            for suf, nom in SUFFIX:
                if p.endswith(suf):
                    key = p[:-len(suf)] + nom
                    break
        v = B._single(key)
        assert v, (p, key)
        return v + var
    key = ALIAS.get(key, key)
    return B.DHAMMA + " " + B.MATRIX_PRED[key] + var


def chain_vi(chain):
    """'Vedanākkhandhena ye dhammā… saññākkhandhena ye dhammā' -> «Đối với …, những hiện tượng nào… đối với …»"""
    parts = [x.strip() for x in chain.replace("…pe…", "…").split("…")]
    out = []
    for x in parts:
        assert x.endswith(" ye dhammā"), x
        out.append(REL.format(x=instr_item(x[:-len(" ye dhammā")])))
    return B.cap("… ".join(out))


def counts_vi(c):
    """Answer counts, all positive here: 'một khối, mười lĩnh vực nhận biết, mười yếu tố'."""
    assert None not in c, c
    return ", ".join(B.count_phrase(n, noun) for n, noun in zip(c, B.NOUNS))


_MODS = "khandhasaṅgahena asaṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā"
_SEG = re.compile(
    rf"^(?P<chain>.+?) {_MODS},? tehi dhammehi ye dhammā"     # ^3-225 has no comma before tehi (rendered as meant)
    rf"(?: {_MODS}, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi asaṅgahitā\? Te dhammā (?P<a1>"
    + B.COUNTS_RX + r") asaṅgahitā\.|…pe… te dhammā (?P<a2>" + B.COUNTS_RX + r") asaṅgahitā\.)$")


def segment_vi(line):
    m = _SEG.match(line)
    assert m, line
    head = f"{chain_vi(m.group('chain'))} {MODS_EX}, {REL2}"
    if m.group("a1"):
        return f"{head} {MODS_EX}{Q_MAIN_EX} {ANS_FULL} {B.EXCL} {counts_vi(B.parse_counts(m.group('a1')))}."
    return f"{head}{ANS_SHORT} {B.EXCL} {counts_vi(B.parse_counts(m.group('a2')))}."


# ---------------------------------------------------------------- summary verse of ^3-227 (uddāna) and closing
MP = B.MATRIX_PRED
VERSE = {
    "Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ;":
        f"Vật chất, {B.AYATANA['dhammāyatanaṃ']}, {B.DHATU['dhammadhātu']}, {B.INDRIYA['itthindriyaṃ']}, "
        f"{B.INDRIYA['purisindriyaṃ']}, {B.INDRIYA['jīvitindriyaṃ']}, {B.pi2('phần tinh thần và vật chất')};",
    "Dve bhavā jāti jarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ.":
        f"Hai loại hiện hữu, {B.OTHER['jāti']}, {B.OTHER['jarā']}, {B.OTHER['maraṇaṃ']}, điều {MP['rūpino']}, "
        f"điều {MP['anārammaṇā']}, điều {MP['no cittā']}, điều {MP['cittavippayuttā']}.",
    "Visaṃsaṭṭhaṃ samuṭṭhāna-sahabhu anuparivatti;":
        f"Điều {MP['cittavisaṃsaṭṭhā']}, điều {MP['cittasamuṭṭhānā']}, điều {MP['cittasahabhuno']}, "
        f"điều {MP['cittānuparivattino']};",
    "Bāhiraṃ upādā dve, visayo [dvevīsati (syā.)] esanayo subuddho.":
        f"Điều {MP['bāhirā']} và điều {MP['upādā']}, hai điều; phạm vi [dị bản (Syā.): dvevīsati] "
        f"của phương pháp này đã được hiểu rõ.",
    "Asaṅgahitenaasaṅgahitapadaniddeso pañcamo.": B.niddesa_closing(5),
}


def build():
    out = []
    for seg in B._segments(PALI):
        vi = []
        for i, line in enumerate(seg):
            idm = B.ID.search(line)
            bid = idm.group(1) if idm else None
            body = B.ID.sub("", line).strip()
            h = B._heading(line)
            if h:
                hashes, title, _ = h
                t = {"Pañcamanayo": B.CHAPTER_TITLES[6],
                     "Asaṅgahitenaasaṅgahitapadaniddeso": B.niddesa_heading(5)}.get(title) or B.SUBHEADINGS[title]
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            else:
                assert i == 0, line
                t = segment_vi(body)
            vi.append(t + (f" {bid}" if bid else ""))
        out.append("\n".join(vi))
    return "\n\n".join(out) + "\n"


def main():
    n1, n2 = B.check_sources()
    text = build()
    assert unicodedata.normalize("NFC", text) == text
    assert "—" not in text and "–" not in text and ":-" not in text and "…." not in text
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {OUT}")


if __name__ == "__main__":
    main()
