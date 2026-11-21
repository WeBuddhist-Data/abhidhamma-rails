# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 9: 9-atthakapuggalapannatti.md (Aṭṭhakapuggalapaññatti, ^4-207).

Imports the approved sample builder (names, headings, closers, MAGGASAMANGI / PHALASAMANGI, PATIPANNO_FOR) and the
finished ch4 builder (tattha_who: Tattha katame … puggalā? = «Ở đây, … là những ai?»). The group name repeats the
approved matrix item ^4-M-14 (1-matika.md, Aṭṭhakauddeso (1)) byte for byte; the eight person names are B.NAME.
Writes ONLY AI_translation/vietnamese/pi-4-vietnamese-plain-zeroshot_split_chapters/9-atthakapuggalapannatti.md.
run:  python -I -X utf8 build_9_vi.py
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as C4  # noqa: E402  (import only reads 1-matika.md, writes nothing)

CH = "9-atthakapuggalapannatti.md"
N = B.NAME
cap = B.cap
FOUR_MAGGA = f"bốn {B.MAGGASAMANGI}"          # cattāro maggasamaṅgino (matrix ^4-M-14)
FOUR_PHALA = f"bốn {B.PHALASAMANGI}"          # cattāro phalasamaṅgino (matrix ^4-M-14)
GROUP = f"{FOUR_MAGGA}, {FOUR_PHALA}"          # cattāro maggasamaṅgino, cattāro phalasamaṅgino puggalā
IME = "đây là {x}"                              # ime … puggalā (closing list; ch4 «Đây là ba hạng người …»)
V_ARAHATTA = " [dị bản (Syā., Ka.): arahattāya; Tăng Chi Bộ Kinh 8.59]"   # [arahattāya (syā. ka.) a. ni. 8.59]

PAIRS = [  # (attainer, practiser) in the Pāli order of ^4-207
    ("sotāpanno", "sotāpattiphalasacchikiriyāya paṭipanno"),
    ("sakadāgāmī", "sakadāgāmiphalasacchikiriyāya paṭipanno"),
    ("anāgāmī", "anāgāmiphalasacchikiriyāya paṭipanno"),
    ("arahā", "arahattaphalasacchikiriyāya paṭipanno"),
]

MATRIX_CHECK = [
    "#### " + B.UDDESA_HEADING[8] + " ",
    f"(1) {cap(GROUP)}.",
    B.MATIKA_GROUP_CLOSER[8],
]

CROSS = [
    (1, B.MAGGASAMANGI), (1, B.PHALASAMANGI), (2, "thành quả vào dòng"), (2, "thành quả trở lại một lần"),
    (2, "thành quả không trở lại"), (2, "thành quả A-la-hán"), (2, "Tăng Chi Bộ Kinh"), (1, "tự mình chứng nghiệm"),
    (2, "là những ai?"),
]


def lines():
    items = []
    for i, (a, p) in enumerate(PAIRS):
        var = V_ARAHATTA if a == "arahā" else ""
        items.append(f"{N[a]}, {N[p]}{var}")
    body = (C4.tattha_who(GROUP) + " " + cap("; ".join(items)) + "; "
            + IME.format(x=FOUR_MAGGA) + ", " + IME.format(x=FOUR_PHALA) + ".")
    return ["#### " + B.CHAPTER_HEADING[9], body, B.NIDDESA_CLOSER[8]]


def main():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    B.check_cross_book()
    matika = (B.OUT_DIR / "1-matika.md").read_text(encoding="utf-8")
    for s in MATRIX_CHECK:
        assert s in matika, "matrix string not found: " + s
    # person names = B.NAME (sample) and PATIPANNO_FOR
    for a, p in PAIRS:
        assert p in N and a in N, (a, p)
    for x, p in (("vào dòng", PAIRS[0][1]), ("trở lại một lần", PAIRS[1][1]), ("không trở lại", PAIRS[2][1]),
                 ("A-la-hán", PAIRS[3][1])):
        assert N[p] == B.PATIPANNO_FOR.format(x=x), p
    assert B.CHAPTER_HEADING[9] == "Định danh các hạng người theo nhóm tám"
    assert B.NIDDESA_CLOSER[8] == "Giải thích phân loại theo nhóm tám."
    L = lines()
    text = B.assemble(CH, L)
    for a, p in PAIRS:
        assert (f"; {N[a]}, " in text or f"? {cap(N[a])}, " in text) and N[p] in text, (a, p)
    assert text.count(B.MAGGASAMANGI) == 2 and text.count(B.PHALASAMANGI) == 2
    for bad in ("—", "–", ":-", "….", "chánh niệm", "  "):
        assert bad not in text, bad
    (B.OUT_DIR / CH).write_bytes(text.encode("utf-8"))
    print(f"OK: cross-book strings {len(CROSS)} (+ sample {len(B.CROSS_BOOK)}); matrix strings {len(MATRIX_CHECK)}; "
          f"wrote {CH} ({len(L)} lines)")


if __name__ == "__main__":
    main()
