# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 3 (3-dutiyanayo.md, Dutiyanayo).

usage: python -I -X utf8 build_3_vi.py
Writes AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\3-dutiyanayo.md
after the pi-1 / pi-2 string checks (B.check_sources) pass.
Reuses build_sample_vi (B) verbatim; the coordinator's SHARED FRAMES are fixed strings below.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "3-dutiyanayo.md"
PALI = os.path.join(B.PALI_DIR, NAME)
OUT = os.path.join(B.OUT_DIR, NAME)

# ---------------------------------------------------------------- shared frames (coordinator)
REL = "đối với {x}, những hiện tượng nào"                     # Xena / Xāya ye dhammā
MOD_KH_IN = "được gộp vào theo cách gộp vào khối"              # khandhasaṅgahena saṅgahitā
MOD_AY_EX = "không được gộp vào theo cách gộp vào lĩnh vực nhận biết"   # āyatanasaṅgahena asaṅgahitā
MOD_DH_EX = "không được gộp vào theo cách gộp vào yếu tố"      # dhātusaṅgahena asaṅgahitā
Q_MAIN_EX = ", thì những hiện tượng đó không được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
ANS_FULL = "Những hiện tượng đó"                                # Te dhammā (answer)
ANS_SHORT = "… những hiện tượng đó"                            # …pe… te dhammā
B.pi2("những hiện tượng đó")
B.pi2("Đối với")
B.pi1("những hiện tượng nào")

# ---------------------------------------------------------------- relative-clause heads (instrumental -> nominative key)
def instr_item(p):
    """Instrumental list member -> Vietnamese (lower case)."""
    p = p[:1].lower() + p[1:]
    m = re.fullmatch(r"(\w+?)ehi dhammehi", p)
    if m:                                              # sanidassanehi dhammehi -> sanidassanā
        return B.DHAMMA + " " + B.MATRIX_PRED[m.group(1) + "ā"]
    if p.endswith("dhammehi"):                         # upādādhammehi -> upādā
        return B.DHAMMA + " " + B.MATRIX_PRED[p[:-len("dhammehi")]]
    for suf, nom in (("āyatanena", "āyatanaṃ"), ("driyena", "driyaṃ"), ("dhātuyā", "dhātu"), ("ena", "o")):
        if p.endswith(suf):
            key = p[:-len(suf)] + nom
            v = B._single(key)
            assert v, (p, key)
            return v
    raise AssertionError(p)


def chain_vi(chain):
    """'Cakkhāyatanena ye dhammā… phoṭṭhabbāyatanena ye dhammā' -> «Đối với …, những hiện tượng nào… đối với …»"""
    parts = [x.strip() for x in chain.split("…")]
    out = []
    for x in parts:
        assert x.endswith(" ye dhammā"), x
        out.append(REL.format(x=instr_item(x[:-len(" ye dhammā")])))
    return B.cap("… ".join(out))


def counts_vi(c):
    """Answer counts, all positive here: 'bốn khối, hai lĩnh vực nhận biết, tám yếu tố'."""
    assert None not in c, c
    return ", ".join(B.count_phrase(n, noun) for n, noun in zip(c, B.NOUNS))


_SEG = re.compile(
    r"^(?P<chain>.+?) khandhasaṅgahena saṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā"
    r"(?:, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi asaṅgahitā\? Te dhammā (?P<a1>"
    + B.COUNTS_RX + r") asaṅgahitā\.|…pe… te dhammā (?P<a2>" + B.COUNTS_RX + r") asaṅgahitā\.)$")


def segment_vi(line):
    m = _SEG.match(line)
    assert m, line
    head = f"{chain_vi(m.group('chain'))} {MOD_KH_IN}, {MOD_AY_EX}, {MOD_DH_EX}"
    if m.group("a1"):
        return f"{head}{Q_MAIN_EX} {ANS_FULL} {B.EXCL} {counts_vi(B.parse_counts(m.group('a1')))}."
    return f"{head}{ANS_SHORT} {B.EXCL} {counts_vi(B.parse_counts(m.group('a2')))}."


# ---------------------------------------------------------------- summary verse of ^3-178 (uddāna) and closing
VERSE = {
    "Dasāyatanā sattarasa dhātuyo,":
        f"{B.cap(B.NUM[10])} {B.AY}, {B.NUM[17]} {B.DH},",
    "Sattindriyā asaññābhavo ekavokārabhavo;":
        f"{B.cap(B.pi1('bảy năng lực'))}, {B.OTHER['asaññābhavo']}, {B.OTHER['ekavokārabhavo']};",
    "Paridevo sanidassanasappaṭighaṃ,":
        f"{B.cap(B.OTHER['paridevo'])}, điều {B.MATRIX_PRED['sanidassanasappaṭighā']},",
    "Anidassanaṃ punadeva [punareva (pī.)] sappaṭighaṃ upādāti.":
        f"Điều {B.MATRIX_PRED['anidassanā']}, rồi lại [khác chính tả (Pī.): punareva] "
        f"điều {B.MATRIX_PRED['sappaṭighā']} và điều {B.MATRIX_PRED['upādā']}.",
    "Saṅgahitenaasaṅgahitapadaniddeso dutiyo.": B.niddesa_closing(2),
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
                t = {"Dutiyanayo": B.CHAPTER_TITLES[3],
                     "Saṅgahitenaasaṅgahitapadaniddeso": B.niddesa_heading(2)}[title]
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
