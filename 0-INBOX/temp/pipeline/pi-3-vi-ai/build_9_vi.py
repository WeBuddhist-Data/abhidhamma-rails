# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 9 (9-atthamanayo.md, Aṭṭhamanayo,
vippayuttena sampayuttaṃ).

usage: python -I -X utf8 build_9_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\9-atthamanayo.md
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's and this file's) still occurs
in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the Pāli at build time.
Reuses build_sample_vi (B) verbatim; the coordinator's SHARED FRAMES are fixed strings below.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "9-atthamanayo.md"
N = 8  # method number (file 9)
PALI = os.path.join(B.PALI_DIR, NAME)
OUT = os.path.join(B.OUT_DIR, NAME)

# ---------------------------------------------------------------- shared frames (coordinator)
REL = "đối với {x}, những hiện tượng nào"                     # Xena / Xehi dhammehi ye dhammā
DISS_SG = "không gắn liền với nó"          # (Xena ye dhammā) vippayuttā
DISS_PL = "không gắn liền với chúng"       # (Xehi dhammehi ye dhammā) vippayuttā: plural head, as «tehi dhammehi»
Q_MAIN_ASSOC = ", thì những hiện tượng đó gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
NATTHI = "Không có."                       # Natthi.
B.pi2("những hiện tượng đó")
B.pi2("Đối với")
B.pi1("những hiện tượng nào")
B.pi1("không gắn liền với")
B.pi1("gắn liền với")

# ---------------------------------------------------------------- relative-clause heads
INSTR = {  # instrumental member -> key of B
    "rūpakkhandhena": "rūpakkhandho", "vedanākkhandhena": "vedanākkhandho",
    "saññākkhandhena": "saññākkhandho", "saṅkhārakkhandhena": "saṅkhārakkhandho",
    "viññāṇakkhandhena": "viññāṇakkhandho",
}
DHAMMEHI = {  # Xehi dhammehi -> key of B.MATRIX_PRED (rendered «các hiện tượng <pred>», chapter 3 pattern)
    "saraṇehi dhammehi": "saraṇā", "araṇehi dhammehi": "araṇā",
}


def head_vi(p):
    """Instrumental head (without 'ye dhammā') -> (Vietnamese, plural?)."""
    p = p[:1].lower() + p[1:]
    if p in DHAMMEHI:
        return B.DHAMMA + " " + B.MATRIX_PRED[DHAMMEHI[p]], True
    v = B._single(INSTR[p])
    assert v, p
    return v, False


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā…pe… Cehi dhammehi ye dhammā' -> «Đối với A, những hiện tượng nào… …»;
    returns the text and whether the last head is plural (pronoun of the shared predicate)."""
    parts = [x.strip() for x in chain.replace("…pe…", "…").split("…")]
    out, plural = [], False
    for x in parts:
        assert x.endswith(" ye dhammā"), x
        v, plural = head_vi(x[:-len(" ye dhammā")])
        out.append(REL.format(x=v))
    return B.cap("… ".join(out)), plural


_SEG = re.compile(
    r"^(?P<chain>.+?) vippayuttā, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttāti\? Natthi\.$")


def segment_vi(line):
    m = _SEG.match(line)
    assert m, line
    chain, plural = chain_vi(m.group("chain"))
    return f"{chain} {DISS_PL if plural else DISS_SG}{Q_MAIN_ASSOC} {NATTHI}"


# ---------------------------------------------------------------- summary verse of ^3-318 (uddāna) and closing
B.pi1("Bộ đôi xen giữa nhỏ")       # antara = phần xen giữa (pi-1 Cūḷantaradukaṃ)
B.pi1("Bộ đôi cuối")               # matthake = ở phần cuối (pi-1 Piṭṭhidukaṃ «Bộ đôi cuối»)
B.pi1("Ma trận bộ ba")             # tike = trong các bộ ba
SALAYATANA = B.pi2("sáu lĩnh vực nhận biết")
NAMARUPA = B.pi2("phần tinh thần và vật chất")
NOT_FOUND = "không tìm thấy"       # na labbhare / na labbhanti
MUC = "mục"                        # implied pada (chapter 4: «hai mục», «tám mục»)
VERSE = {
    "Dhammāyatanaṃ dhammadhātu, atha jīvitaṃ nāmarūpaṃ;":
        f"{B.cap(B.AYATANA['dhammāyatanaṃ'])}, {B.DHATU['dhammadhātu']}, rồi {B.INDRIYA['jīvitindriyaṃ']}, "
        f"{NAMARUPA};",
    "Saḷāyatanaṃ jātijarāmataṃ, dve ca tike na labbhare.":
        f"{B.cap(SALAYATANA)}, {B.OTHER['jāti']}, {B.OTHER['jarā']}, {B.OTHER['maraṇaṃ']}, "
        f"và {B.NUM[2]} {MUC} trong các bộ ba thì {NOT_FOUND}.",
    "Paṭhamantare satta ca, gocchake dasa aparante;":
        f"{B.cap(B.NUM[7])} {MUC} trong phần xen giữa {B.ORDINAL[1]}, {B.NUM[10]} {MUC} trong các nhóm;",
    "Cuddasa cha ca matthake, iccete sattacattālīsa dhammā;":
        f"{B.cap(B.NUM[14])} {MUC} trong phần xen giữa sau, và {B.NUM[6]} {MUC} ở phần cuối, "
        f"như vậy bốn mươi bảy hiện tượng này;",
    "Samucchede na labbhanti, moghapucchakena cāti.":
        f"{B.cap(NOT_FOUND)} trong sự phân tách, và do câu hỏi rỗng.",
    "Vippayuttenasampayuttapadaniddeso aṭṭhamo.": B.niddesa_closing(N),
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
                t = {"Aṭṭhamanayo": B.CHAPTER_TITLES[N + 1],
                     "Vippayuttenasampayuttapadaniddeso": B.niddesa_heading(N)}[title]
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
    assert "—" not in text and "–" not in text and ":-" not in text and "…." not in text and "pe…" not in text
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {OUT}")


if __name__ == "__main__":
    main()
