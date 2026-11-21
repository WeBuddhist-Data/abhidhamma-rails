# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 5-catutthanayo.md (Catutthanayo, method 4).

usage: python -I -X utf8 build_5_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\5-catutthanayo.md,
after the pi-1 / pi-2 string checks (B.check_sources(), which also covers the strings registered here) pass.
Reuses the approved sample builder (build_sample_vi) verbatim; formulas new to this chapter are in notes-5.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B

NAME = "5-catutthanayo.md"
METHOD = 4                                  # Catutthanayo = method 4 = file 5

# ---------------------------------------------------------------- shared frames (coordinator)
REL = "đối với {x}, những hiện tượng nào"                     # Xena ye dhammā
MOD_INCL = ", ".join(f"{B.INCL} theo cách gộp vào {n}" for n in B.NOUNS)
# khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā
REL2 = "đối với những hiện tượng ấy, những hiện tượng nào"    # tehi dhammehi ye dhammā
MAIN_Q_INCL = ", thì những hiện tượng đó được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
ANS_SUBJ = "Những hiện tượng đó"                               # Te dhammā (answer)

PALI_TAIL = re.compile(
    r"^ khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā, "
    r"tehi dhammehi ye dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā, "
    r"te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā\? "
    rf"Te dhammā (?P<c>{B.COUNTS_RX}) saṅgahitā\.$")


def tail_vi(pali_tail):
    m = PALI_TAIL.match(pali_tail)
    assert m, pali_tail
    return (f" {MOD_INCL}, {REL2} {MOD_INCL}{MAIN_Q_INCL} "
            f"{ANS_SUBJ} {B.incl(B.parse_counts(m.group('c')))}.")


# ---------------------------------------------------------------- members in the instrumental (Vietnamese: same string)
def _m(p):  # matrix name «các hiện tượng <pred>»
    return B.DHAMMA + " " + B.MATRIX_PRED[p]


INSTR = {
    "samudayasaccena": B.SACCA["samudayasaccaṃ"], "maggasaccena": B.SACCA["maggasaccaṃ"],
    "avijjāya": B.OTHER["avijjā"],
    "avijjāpaccayā saṅkhārena": B.PS_Q["avijjāpaccayā saṅkhārā"],
    "saḷāyatanapaccayā phassena": B.PS_Q["saḷāyatanapaccayā phasso"],
    "vedanāpaccayā taṇhāya": B.PS_Q["vedanāpaccayā taṇhā"],
    "taṇhāpaccayā upādānena": B.PS_Q["taṇhāpaccayā upādānaṃ"],
    "kammabhavena": B.OTHER["kammabhavo"], "sokena": B.OTHER["soko"], "paridevena": B.OTHER["paridevo"],
    "dukkhena": B.OTHER["dukkhaṃ"], "domanassena": B.OTHER["domanassaṃ"], "upāyāsena": B.OTHER["upāyāso"],
    "satipaṭṭhānena": B.OTHER["satipaṭṭhānaṃ"], "sammappadhānena": B.OTHER["sammappadhānaṃ"],
    "appamaññāya": B.OTHER["appamaññā"],
    "pañcahi indriyehi": B.OTHER["pañcindriyāni"], "pañcahi balehi": B.OTHER["pañca balāni"],
    "sattahi bojjhaṅgehi": B.OTHER["satta bojjhaṅgā"],
    "ariyena aṭṭhaṅgikena maggena": B.OTHER["ariyo aṭṭhaṅgiko maggo"],
    "phassena": B.OTHER["phasso"], "cetanāya": B.OTHER["cetanā"], "adhimokkhena": B.OTHER["adhimokkho"],
    "manasikārena": B.OTHER["manasikāro"],
    "hetūhi dhammehi": _m("hetū"),
    "hetūhi ceva sahetukehi ca dhammehi": _m("hetū ceva sahetukā ca"),
    "hetūhi ceva hetusampayuttehi ca dhammehi": _m("hetū ceva hetusampayuttā ca"),
    "kilesehi dhammehi": _m("kilesā"),
    "kilesehi ceva saṃkilesikehi ca dhammehi": _m("kilesā ceva saṃkilesikā ca"),
    "kilesehi ceva saṃkiliṭṭhehi ca dhammehi": _m("kilesā ceva saṃkiliṭṭhā ca"),
    "kilesehi ceva kilesasampayuttehi ca dhammehi": _m("kilesā ceva kilesasampayuttā ca"),
}
for _k, _v in B.INDRIYA.items():                  # itthindriyaṃ -> itthindriyena
    _s = re.sub(r"aṃ$", "ena", unicodedata.normalize("NFC", _k))
    assert _s.endswith("ena"), _k
    INSTR[_s] = _v
# bare abbreviated members inside the chain «hetūhi … dhammehi ye dhammā… āsavehi… saṃyojanehi…»: they stand in
# the slot of the matrix predicate, so they keep the predicate alone (là ô nhiễm… là xiềng xích…)
BARE = {
    "āsavehi": B.MATRIX_PRED["āsavā"], "saṃyojanehi": B.MATRIX_PRED["saṃyojanā"],
    "ganthehi": B.MATRIX_PRED["ganthā"], "oghehi": B.MATRIX_PRED["oghā"], "yogehi": B.MATRIX_PRED["yogā"],
    "nīvaraṇehi": B.MATRIX_PRED["nīvaraṇā"], "parāmāsehi": B.MATRIX_PRED["parāmāsā"],
    "upādānehi": B.MATRIX_PRED["upādānā"],
}


def chain_vi(body):
    """'Xena ye dhammā… Yena ye dhammā [tail]' / '… ye dhammā….' -> Vietnamese line."""
    trail = False
    for end in (" ….", "…."):                 # '…' + sentence stop at the line end -> '…' (never «….»)
        if body.endswith(end):
            body, trail = body[:-len(end)], True
            break
    parts = body.split("…")
    out = []
    for k, p in enumerate(parts):
        p = p.strip() if k < len(parts) - 1 else p.lstrip()
        m = re.match(r"^(.+?) ye dhammā(.*)$", p)
        if m:
            key = m.group(1)[:1].lower() + m.group(1)[1:]
            s = REL.format(x=INSTR[key])
            if m.group(2):
                assert k == len(parts) - 1 and not trail, p
                s += tail_vi(m.group(2))
        else:
            s = BARE[p]
        out.append(s)
    return B.cap("… ".join(out)) + ("…" if trail else "")


# ---------------------------------------------------------------- fixed lines of ^3-192
GOCCHAKA = "nhóm"                     # gocchaka (pi-1 Hetugocchakaṃ «Nhóm về gốc rễ»)
B.pi1("Nhóm về gốc rễ")
PADA = "đề mục"                       # pada (terms file: padaniddeso «Giải thích đề mục về …»)
FIXED = {
    "Dve saccā pannarasindriyā, ekādasa paṭiccapadā;":
        f"Hai sự thật, {B.NUM[15]} năng lực, {B.NUM[11]} {PADA} về {B.OTHER['paṭiccasamuppādo']};",
    "Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti [tiṃsavidhanti (pī.)].":
        f"Tiếp theo lại có {B.NUM[11]}, ở đây các {PADA} thuộc các {GOCCHAKA} có ba mươi loại "
        f"[khác chính tả (Pī.): tiṃsavidhanti].",
    "Saṅgahitenasaṅgahitapadaniddeso catuttho.": B.niddesa_closing(METHOD),
}
B.pi2("sự thật")
B.pi2("năng lực")


# ---------------------------------------------------------------- build
def build():
    out = []
    for seg in B._segments(os.path.join(B.PALI_DIR, NAME)):
        vi = []
        for line in seg:
            idm = B.ID.search(line)
            bid = idm.group(1) if idm else None
            body = B.ID.sub("", line).strip() if bid else line.rstrip()
            h = B._heading(line)
            if h:
                hashes, title, _ = h
                if title == "Catutthanayo":
                    t = B.CHAPTER_TITLES[METHOD + 1]
                elif title == "Saṅgahitenasaṅgahitapadaniddeso":
                    t = B.niddesa_heading(METHOD)
                else:
                    raise AssertionError(line)
                vi.append(f"{hashes} {t} {bid}")
                continue
            t = FIXED[body] if body in FIXED else chain_vi(body)
            vi.append(t + (f" {bid}" if bid else ""))
        out.append("\n".join(vi))
    return "\n\n".join(out) + "\n"


def main():
    n1, n2 = B.check_sources()
    text = build()
    assert unicodedata.normalize("NFC", text) == text
    assert "—" not in text and "–" not in text and ":-" not in text and "…." not in text
    assert "là là" not in text and "được được" not in text
    with open(os.path.join(B.OUT_DIR, NAME), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {NAME}")


if __name__ == "__main__":
    main()
