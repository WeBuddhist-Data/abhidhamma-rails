# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 9: 9-hevatthikatha.md (Hevatthikathā, ^5-9-0 … ^5-306),
with the uddāna of the first vagga.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame; the chapter's own
repeated phrases are fixed strings below, so every repeat is byte-identical. Every string claimed from the
pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is
asserted to occur in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign
letters) are run against the Pāli.

run:  python -I -X utf8 build_9_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "9-hevatthikatha.md"
Q, q, AM, cap = B.Q, B.q, B.AMANTA, B.cap
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE

# ================================================================ terms
PAST, FUT, PRES = "quá khứ", "tương lai", "hiện tại"   # atītaṃ / anāgataṃ / paccuppannaṃ (ch5, ch6, ch7)
KH5 = [B.RUPA, B.VEDANA, B.SANNA, B.SANKHARA, B.VINNANA]  # rūpaṃ vedanā saññā saṅkhārā viññāṇaṃ (pi-2)
AT = "tồn tại"                                   # atthi (sample, ch5-7)
NAT = "không tồn tại"                            # natthi
HEVA_AT = f"{AT} theo cách này"                  # hevatthi (heva = evaṃ, aṭṭhakathā ^5-241)
HEVA_NAT = f"{NAT} theo cách này"                # heva natthi / hevaṃ natthi (^5-306 line 14, same sense)
HH = f"{HEVA_AT}, {HEVA_NAT}"                    # hevatthi, heva natthi
SEVA = f"chính cái ấy {AT}, chính cái ấy {NAT}"  # sevatthi, seva natthi (soyeva atthi, soyeva natthi, aṭṭhakathā)
KINTI = f"{cap(AT)} theo cách nào, {NAT} theo cách nào?"   # Kintatthi, kinti natthīti?
KATHA_X = "việc cho rằng có tồn tại theo cách này"          # Hevatthikathā (terms file)

# atthaṭṭho … tajjāte (aṭṭhakathā: atthisabhāvo natthisabhāvo nāma hotīti pucchati -> copula «là»)
AN = "ý nghĩa của sự tồn tại là ý nghĩa của sự không tồn tại"     # atthaṭṭho natthaṭṭho
NA_ = "ý nghĩa của sự không tồn tại là ý nghĩa của sự tồn tại"    # natthaṭṭho atthaṭṭho
BH = "trạng thái tồn tại là trạng thái không tồn tại, trạng thái không tồn tại là trạng thái tồn tại"
# atthibhāvo natthibhāvo, natthibhāvo atthibhāvo (bhāva = «trạng thái», ch5)
VA = "gọi là tồn tại hay gọi là không tồn tại, gọi là không tồn tại hay gọi là tồn tại"
# atthīti vā natthīti vā, natthīti vā atthīti vā (sample ^5-67 «gọi là X hay gọi là Y»)
SAME = "đó chính là cùng một thứ, cùng một nghĩa, như nhau, ngang nhau, cùng một loại"
# esese ekaṭṭhe same samabhāge tajjāte (sample ^5-67)
SAME_PE = "như nhau, ngang nhau, cùng một loại"   # …pe… same samabhāge tajjāte
FULL = Q(f"{AN}, {NA_}, {BH}, {VA}, {SAME}")
SHORT1 = Q(f"{AN}… {SAME_PE}")                    # Atthaṭṭho natthaṭṭho…pe… same samabhāge tajjāteti?
SHORT2 = Q(f"{AN}, {NA_}… {SAME_PE}")             # Atthaṭṭho natthaṭṭho, natthaṭṭho atthaṭṭho…pe… …


def as_(a, b):
    """<a> <b>nti  ->  «a xét như là b»"""
    return f"{a} xét như là {b}"


def ex(a, b, neg=False):
    """<a> <b>nti hevatthi / heva natthi  ->  «a xét như là b thì tồn tại / không tồn tại theo cách này»"""
    return f"{as_(a, b)} thì {HEVA_NAT if neg else HEVA_AT}"


SEVA_RUN = f"{Q(SEVA)} {NHP} {q(SEVA)} {AM}"     # Sevatthi, seva natthīti? Na hevaṃ vattabbe…pe… sevatthi …? Āmantā.


def thesis(x, tail):
    """X atthīti? Hevatthi, heva natthīti. Sevatthi …? Āmantā. <tail> Na hevaṃ vattabbe…pe…."""
    return f"{Q(f'{x} {AT}')} {cap(HH)}. {SEVA_RUN} {tail} {NHP}"


def kinti(x, answer, tail):
    """X hevatthi, heva natthīti? Āmantā. Kintatthi, kinti natthīti? <answer> Sevatthi …? Āmantā. <tail> …"""
    return f"{Q(f'{x} {HH}')} {AM} {KINTI} {answer} {SEVA_RUN} {tail} {NHP}"


def three(x, others):
    """atītaṃ atītanti hevatthi, atītaṃ anāgatanti heva natthi, atītaṃ paccuppannanti heva natthīti."""
    return cap(", ".join([ex(x, x)] + [ex(x, o, True) for o in others])) + "."


# ================================================================ uddāna of the first vagga
TASSUDDANAM = "Tóm tắt của chương này –"      # Tassuddānaṃ – (tassa = of the vagga)
UDD_1 = "Sự được tìm thấy, sự suy thoái, đời sống tu hành trong sạch, từng phần;"
# Upalabbho parihāni, brahmacariyavāso odhiso;  (upalabbhati «được tìm thấy» sample; parihāni ch2;
#  brahmacariyavāso ch3; odhiso «từng phần» ch3)
UDD_2 = ("Sự hiểu biết trọn vẹn, sự dứt bỏ sự tham đắm dục lạc, học thuyết cho rằng tất cả đều tồn tại, "
         "lĩnh vực nhận biết;")
# Pariññā kāmarāgappahānaṃ, sabbatthivādo āyatanaṃ;  (pariññā pi-2; kāmarāga pi-1, ch4; pahāna «sự dứt bỏ»
#  pi-1; sabbamatthi ch5; vāda «học thuyết» pi-4; āyatana core)
UDD_3 = (f"Quá khứ và tương lai được phân chia khéo léo [{B.VAR} (Syā.): atītānāgatesu bhāgo], "
         "tất cả các hiện tượng là sự thiết lập tỉnh thức.")
# Atītānāgato subhaṅgo [atītānāgatesu bhāgo (syā.)], sabbe dhammā satipaṭṭhānā.  (satipaṭṭhāna pi-1, ch8 heading)
UDD_4 = f"{cap(HH)}."                          # Hevatthi heva natthīti. (= the answer «Hevatthi, heva natthīti.»)
PATHAMAVAGGO = B.VAGGA[1]                      # Paṭhamavaggo (no full stop, as the Pāli)
MAHAVAGGO = "Chương lớn."                      # Mahāvaggo. (name of the first vagga; cf. KALYANAVAGGO_PATHAMO)


def build():
    d = B.Doc()
    d.head(3, B.KATHA.format(x=KATHA_X), "5-9-0")
    # ------------------------------------------------------------ ^5-304
    d.seg("5-304",
          thesis(PAST, FULL),
          thesis(FUT, FULL),
          thesis(PRES, SHORT1))
    # ------------------------------------------------------------ ^5-305
    L3 = f"{HH}; ".join(f"{t} " for t in (PAST, FUT, PRES)) + HH
    # atītaṃ hevatthi, heva natthi; anāgataṃ hevatthi, heva natthi; paccuppannaṃ hevatthi, heva natthī
    L3c = f"{HH}, ".join(f"{t} " for t in (PAST, FUT, PRES)) + HH
    # Tena hi atītaṃ hevatthi heva natthi, anāgataṃ … , paccuppannaṃ hevatthi, heva natthīti. (commas as meant)
    cross = ", ".join(ex(a, b) for a, b in ((PAST, FUT), (PAST, PRES), (FUT, PAST), (FUT, PRES),
                                             (PRES, PAST), (PRES, FUT)))
    d.seg("5-305",
          kinti(PAST, three(PAST, (FUT, PRES)), FULL),
          kinti(FUT, three(FUT, (PAST, PRES)), SHORT2),
          kinti(PRES, three(PRES, (PAST, FUT)), SHORT1),
          f"{B.NA_VATTABBAM_Q(L3)} {AM} {Q(cross)} {NHP} {B.TENA_HI(L3c)}")
    # ------------------------------------------------------------ ^5-306
    R, V, S, K, W = KH5
    rest = f"{V}… {S}… {K}… {W}"                      # vedanā… saññā… saṅkhārā… viññāṇaṃ
    ans_r = (f"{cap(ex(R, R))}, {ex(R, V, True)}… {ex(R, S, True)}… {ex(R, K, True)}… {ex(R, W, True)}.")
    # Rūpaṃ rūpanti hevatthi, rūpaṃ vedanāti hevaṃ natthi…pe… rūpaṃ saññāti heva natthi…pe… … viññāṇanti heva natthīti.
    ans_w = (f"{cap(ex(W, W))}. {cap(ex(W, R, True))}… {ex(W, V, True)}… {ex(W, S, True)}… {ex(W, K, True)}.")
    # Viññāṇaṃ viññāṇanti hevatthi. Viññāṇaṃ rūpanti heva natthi…pe… … saṅkhārāti heva natthīti. (full stop kept)
    r_rest = f"{R} {HH}; {rest} {HH}"                 # rūpaṃ hevatthi, heva natthi(ti); vedanā… viññāṇaṃ hevatthi, heva natthi
    cross5 = (f"{ex(R, V)}… {ex(R, S)}… {ex(R, K)}… {ex(R, W)}… "
              f"{V}… {S}… {K}… {ex(W, R)}… {ex(W, V)}… {ex(W, S)}… {ex(W, K)}")
    d.seg("5-306",
          thesis(R, FULL),
          thesis(rest, SHORT1),
          kinti(R, ans_r, SHORT1),
          kinti(rest, ans_w, SHORT1),
          # Na vattabbaṃ – "rūpaṃ … natthīti; vedanā… viññāṇaṃ hevatthi, heva natthīti? (opening quote never closed)
          f"Có phải không nên nói – “{r_rest} không? {AM} {Q(cross5)} {NHP} vậy thì {r_rest}.",
          B.KATHA_END.format(x=KATHA_X),
          TASSUDDANAM, UDD_1, UDD_2, UDD_3, UDD_4,
          PATHAMAVAGGO, MAHAVAGGO)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("tồn tại", 1), ("vật chất", 2), ("cảm giác", 2), ("tri giác", 2), ("thức", 2),   # saṅkhārā: sample SANKHARA
    ("hiểu biết trọn vẹn", 2), ("Sự dứt bỏ khao khát", 2), ("sự tham đắm dục lạc", 1), ("lĩnh vực nhận biết", 2),
    ("đời sống tu hành trong sạch", 1), ("sự thiết lập tỉnh thức", 1), ("học thuyết", 4),
    ("Các hiện tượng thuộc quá khứ", 1), ("Các hiện tượng thuộc tương lai", 1), ("Các hiện tượng thuộc hiện tại", 1),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (SAME, "1-puggalakatha.md"), ("gọi là thân hay gọi là thân thể, gọi là thân thể hay gọi là thân", "1-puggalakatha.md"),
    ("Sự suy thoái", "2-parihanikatha.md"), ("đời sống tu hành trong sạch", "3-brahmacariyakatha.md"),
    ("từng phần", "3-brahmacariyakatha.md"), ("sự tham đắm dục lạc", "4-jahatikatha.md"),
    ("tất cả đều tồn tại", "5-sabbamatthitikatha.md"), ("Có phải quá khứ tồn tại không?", "5-sabbamatthitikatha.md"),
    ("trạng thái", "5-sabbamatthitikatha.md"), ("lĩnh vực nhận biết", "6-atitakkhandhadikatha.md"),
    ("Có phải quá khứ tồn tại không?", "7-ekaccam-atthitikatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    missing += [(s, f) for s, f in PI5 if s not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch9 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
