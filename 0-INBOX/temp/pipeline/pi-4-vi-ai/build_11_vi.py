# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 11: 11-dasakapuggalapannatti.md (Dasakapuggalapaññatti, ^4-209).

Imports the approved sample builder (names, headings, closers, DESIGNATION_Q / DESIGNATION_A, BOOK_END,
DITTHEVA_DHAMME) and the finished ch4 builder (tattha_who: «… là những ai?»). The two groups repeat the approved
matrix item ^4-M-16 (1-matika.md, Dasakauddeso (1)) byte for byte; the ten person names are B.NAME.
Writes ONLY AI_translation/vietnamese/pi-4-vietnamese-plain-zeroshot_split_chapters/11-dasakapuggalapannatti.md.
run:  python -I -X utf8 build_11_vi.py
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as C4  # noqa: E402  (import only reads 1-matika.md, writes nothing)

CH = "11-dasakapuggalapannatti.md"
N = B.NAME
cap = B.cap

IDHA = "năm người đạt đến đích ngay ở đây"                       # pañcannaṃ idha niṭṭhā (matrix ^4-M-16)
VIHAYA = "năm người đạt đến đích sau khi rời khỏi nơi đây"       # pañcannaṃ idha vihāya niṭṭhā (matrix ^4-M-16)
IMESAM = "năm người này"                                         # imesaṃ pañcannaṃ (after a dash: lowercase)
WHO = "{x} là những ai?"                                         # Katamesaṃ … ? (ch4 tattha_who without «Ở đây,»: no tattha)
PUGGALANAM = "các hạng người"                                    # puggalānaṃ (matrix ^4-M-7 question)
ETTAVATA = "sự định danh về {x} bao quát đến mức ấy."            # ettāvatā X-ānaṃ X-paññatti (sample DESIGNATION_A tail)
YO_CA_ARAHA = f"và người nào là {N['arahā']} {B.DITTHEVA_DHAMME}"  # yo ca diṭṭheva dhamme arahā

IDHA_KEYS = ["sattakkhattuparamo", "kolaṅkolo", "ekabījī", "sakadāgāmī"]
VIHAYA_KEYS = ["antarāparinibbāyī", "upahaccaparinibbāyī", "asaṅkhāraparinibbāyī", "sasaṅkhāraparinibbāyī",
               "uddhaṃsoto akaniṭṭhagāmī"]

MATRIX_CHECK = [
    "#### " + B.UDDESA_HEADING[10] + " ",
    f"(1) {cap(IDHA)}, {VIHAYA}.",
    B.MATIKA_GROUP_CLOSER[10],
    B.DESIGNATION_Q.format(x=PUGGALANAM),
    B.BOOK_TITLE,
]

CROSS = [
    (2, B.DITTHEVA_DHAMME), (2, "là những ai?"), (1, "Bộ “Liệt kê các hiện tượng” đã hoàn tất."),
    (2, "nhập Niết-bàn trọn vẹn"),
]


def lines():
    L = ["#### " + B.CHAPTER_HEADING[11]]
    L.append(f"{WHO.format(x=cap(IDHA))} "
             f"{cap(', '.join(N[k] for k in IDHA_KEYS))}, {YO_CA_ARAHA} – {IMESAM} đạt đến đích ngay ở đây.")
    L.append(f"{WHO.format(x=cap(VIHAYA))} "
             f"{cap(', '.join(N[k] for k in VIHAYA_KEYS))} – {IMESAM} đạt đến đích sau khi rời khỏi nơi đây.")
    L.append(cap(ETTAVATA.format(x=PUGGALANAM)))
    L.append(B.NIDDESA_CLOSER[10])
    L.append(B.BOOK_END)
    return L


def main():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    B.check_cross_book()
    matika = (B.OUT_DIR / "1-matika.md").read_text(encoding="utf-8")
    for s in MATRIX_CHECK:
        assert s in matika, "matrix string not found: " + s
    # frames = sample constants
    assert B.DESIGNATION_A.endswith("; " + ETTAVATA), "ettāvatā tail differs from DESIGNATION_A"
    assert C4.tattha_who("X") == "Ở đây, " + WHO.format(x="X")
    assert B.CHAPTER_HEADING[11] == "Định danh các hạng người theo nhóm mười"
    assert B.NIDDESA_CLOSER[10] == "Giải thích phân loại theo nhóm mười."
    assert B.BOOK_END == "Bộ “Định danh các hạng người” đã hoàn tất."
    # person names = B.NAME (sample)
    expect = {
        "sattakkhattuparamo": "người tái sinh tối đa bảy lần",
        "kolaṅkolo": "người đi từ gia đình này sang gia đình khác",
        "ekabījī": "người chỉ còn một hạt giống",
        "sakadāgāmī": "bậc trở lại một lần",
        "arahā": "bậc A-la-hán",
        "antarāparinibbāyī": "bậc nhập Niết-bàn trọn vẹn trong khoảng giữa",
        "upahaccaparinibbāyī": "bậc nhập Niết-bàn trọn vẹn khi gần mạng chung",
        "asaṅkhāraparinibbāyī": "bậc nhập Niết-bàn trọn vẹn không có sự thúc đẩy",
        "sasaṅkhāraparinibbāyī": "bậc nhập Niết-bàn trọn vẹn có sự thúc đẩy",
        "uddhaṃsoto akaniṭṭhagāmī": "bậc ngược dòng đi đến cõi Sắc Cứu Cánh",
    }
    for k, v in expect.items():
        assert N[k] == v, k
    assert N["uddhaṃsoto akaniṭṭhagāmī"] == N["uddhaṃsotoakaniṭṭhagāmī"]
    L = lines()
    text = B.assemble(CH, L)
    for k in expect:
        assert N[k] in text or f"? {cap(N[k])}, " in text, k
    assert text.count(WHO.format(x=cap(IDHA))) == 1 and text.count(WHO.format(x=cap(VIHAYA))) == 1   # questions
    assert text.count("đạt đến đích ngay ở đây") == 2 and text.count("đạt đến đích sau khi rời khỏi nơi đây") == 2
    assert text.count("–") == 2
    for bad in ("—", ":-", "….", "chánh niệm", "  ", "là là"):
        assert bad not in text, bad
    (B.OUT_DIR / CH).write_bytes(text.encode("utf-8"))
    print(f"OK: cross-book strings {len(CROSS)} (+ sample {len(B.CROSS_BOOK)}); matrix strings {len(MATRIX_CHECK)}; "
          f"wrote {CH} ({len(L)} lines)")


if __name__ == "__main__":
    main()
