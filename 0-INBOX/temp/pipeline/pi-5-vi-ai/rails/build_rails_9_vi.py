"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 9, Hevatthikathā (^5-9-0 … ^5-306), with the close
of the first vagga (Tassuddānaṃ –, the uddāna, Paṭhamavaggo, Mahāvaggo.).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/9-hevatthikatha.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, na_vattabbam, tena_hi, katha,
katha_end, vaggo, var …). Strings shared with finished chapters (ch2, ch3, ch6, ch7) are asserted to occur in
those chapter files; S.write runs the per-line dash / quote / NFC / id checks against the Pāli.
New recurring strings: notes-rails-9.md.

usage: python -I -X utf8 -B build_rails_9_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "9-hevatthikatha.md"
Q, q, PE, YES, NO_PE = S.Q, S.q, S.PE, S.YES, S.NO_PE

# ---------------------------------------------------------------------------------------------------------------
# Terms
# ---------------------------------------------------------------------------------------------------------------
ATTHI, NATTHI = "tồn tại", "không tồn tại"            # atthi / natthi (existence thesis; = ch6, ch7)
HEVA = "theo cách như vậy"                             # heva (= evaṃ, commentary "hevāti evaṃ"; sibling hevaṃ «như vậy»)
HEVATTHI = f"{ATTHI} {HEVA}"                           # hevatthi
HEVA_NATTHI = f"{NATTHI} {HEVA}"                       # heva natthi (also the slip "hevaṃ natthi")
HH = f"{HEVATTHI}, {HEVA_NATTHI}"                      # hevatthi, heva natthi
SEVA = "chính cái ấy"                                  # sā eva (termbase Sevatthi «chính cái ấy tồn tại»)
SS = f"{SEVA} {ATTHI}, {SEVA} {NATTHI}"                # sevatthi, seva natthi
KINTI = f"{S.cap(ATTHI)} theo cách nào, {NATTHI} theo cách nào?"   # Kintatthi, kinti natthīti?
PAST, FUT, PRES = "quá khứ", "tương lai", "hiện tại"   # atītaṃ / anāgataṃ / paccuppannaṃ (= ch6, ch7)
RUPA, VEDANA, SANNA, SANKHARA, VINNANA = S.RUPA, S.VEDANA, S.SANNA, S.SANKHARA, S.VINNANA


def as_(x, y):                      # X Yti (X «as Y»)
    return f"{x} xét như là {y}"


def ex(x, y, neg=False):            # X Yti hevatthi / heva natthi
    return f"{as_(x, y)} thì {HEVA_NATTHI if neg else HEVATTHI}"


# Atthaṭṭho natthaṭṭho, natthaṭṭho atthaṭṭho, atthibhāvo natthibhāvo, natthibhāvo atthibhāvo,
# atthīti vā natthīti vā, natthīti vā atthīti vā esese ekaṭṭhe same samabhāge tajjāte
#   (aṭṭho «ý nghĩa», atthibhāvo «trạng thái tồn tại»; "…ti vā …ti vā" and the identity tail as the sample's KAYA_K)
A1 = f"ý nghĩa {ATTHI} và ý nghĩa {NATTHI}"
A2 = f"ý nghĩa {NATTHI} và ý nghĩa {ATTHI}"
A3 = f"trạng thái {ATTHI} và trạng thái {NATTHI}"
A4 = f"trạng thái {NATTHI} và trạng thái {ATTHI}"
A5 = f"gọi là {ATTHI} hay gọi là {NATTHI}"
A6 = f"gọi là {NATTHI} hay gọi là {ATTHI}"
TAIL = "thì đều là một, cùng một nghĩa, như nhau, ngang nhau, cùng một loại"   # esese … tajjāte (sample)
TAIL_SHORT = "như nhau, ngang nhau, cùng một loại"                             # same samabhāge tajjāte
ATTHA_FULL = Q(f"{A1}, {A2}, {A3}, {A4}, {A5}, {A6}, {TAIL}")
ATTHA_SHORT = Q(f"{A1}{PE} {TAIL_SHORT}")                                     # Atthaṭṭho natthaṭṭho…pe… same …
ATTHA_SHORT2 = Q(f"{A1}, {A2}{PE} {TAIL_SHORT}")                              # Atthaṭṭho natthaṭṭho, natthaṭṭho atthaṭṭho…pe…

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā name, vagga close
# ---------------------------------------------------------------------------------------------------------------
KATHA_NAME = f"việc {HEVATTHI}"                        # Hevatthikathā (no headword; built from hevatthi)
H_KATHA = S.katha(KATHA_NAME)                          # ### Hevatthikathā
END_KATHA = S.katha_end(KATHA_NAME)                    # Hevatthikathā niṭṭhitā.
TASSUDDANAM = "Tóm tắt của chương này –"               # Tassuddānaṃ – (user decision, termbase APPROVED.md §4)
UDDANA = [                                             # one Pāli line = one Vietnamese line
    "Sự được tìm thấy, sự suy thoái, việc sống đời sống tu hành trong sạch, từng phần;",
    #   Upalabbho parihāni, brahmacariyavāso odhiso;  (Upalabbho: termbase; parihāni: ch2; brahmacariyavāso: ch3;
    #   odhiso: ch3 Odhisokathā)
    f"Sự hiểu biết trọn vẹn, sự dứt bỏ tham đắm dục lạc, học thuyết cho rằng tất cả {ATTHI}, lĩnh vực nhận biết;",
    #   Pariññā kāmarāgappahānaṃ, sabbatthivādo āyatanaṃ;
    "Quá khứ và tương lai, sự phân chia đúng đắn" + S.var("Syā.", "atītānāgatesu bhāgo")
    + ", tất cả các hiện tượng là các sự thiết lập tỉnh thức.",
    #   Atītānāgato subhaṅgo [atītānāgatesu bhāgo (syā.)], sabbe dhammā satipaṭṭhānā.
    f"{S.cap(HH)}.",
    #   Hevatthi heva natthīti.
]
VAGGA_1 = S.vaggo(1) + "."                             # Paṭhamavaggo (full stop supplied: coordinator rule)
MAHAVAGGO = "Chương lớn."                              # Mahāvaggo. (mahā «lớn», vaggo «chương»)

# Strings shared with finished pi-5 rails chapters (asserted)
SHARED = [  # (Pāli, Vietnamese, chapter file)
    ("Parihānikathā (kathā name)", "Bàn về sự suy thoái", "2-parihanikatha.md"),
    ("brahmacariyavāso", "việc sống đời sống tu hành trong sạch", "3-brahmacariyakatha.md"),
    ("Odhisokathā (kathā name)", "Bàn về từng phần", "3-brahmacariyakatha.md"),
    ("Atītaṃ atthīti?", Q(f"{PAST} {ATTHI}"), "7-ekaccam-atthitikatha.md"),
    ("Anāgataṃ atthīti?", Q(f"{FUT} {ATTHI}"), "7-ekaccam-atthitikatha.md"),
    ("paccuppannaṃ (subject)", f"{PRES} {NATTHI}", "6-atitakkhandhadikatha.md"),
    ("esese ekaṭṭhe same samabhāge tajjāteti?", f"{TAIL} không?", "1-puggalakatha.md"),
]


def check_shared():
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# Frames of the debate
# ---------------------------------------------------------------------------------------------------------------
def opening(subj, attha):
    """X atthīti? Hevatthi, heva natthīti. Sevatthi, seva natthīti? Na hevaṃ vattabbe…pe… sevatthi, seva natthīti?
    Āmantā. Atthaṭṭho … tajjāteti? Na hevaṃ vattabbe…pe…."""
    return (f"{Q(f'{subj} {ATTHI}')} {S.cap(HH)}. {Q(SS)} {NO_PE} {q(SS)} {YES} {attha} {NO_PE}")


def kinti(thesis, answer, attha):
    """X hevatthi, heva natthīti? Āmantā. Kintatthi, kinti natthīti? <answer>. Sevatthi … Na hevaṃ vattabbe…pe…."""
    return f"{Q(thesis)} {YES} {KINTI} {answer} {Q(SS)} {NO_PE} {q(SS)} {YES} {attha} {NO_PE}"


def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    add("5-9-0", f"### {H_KATHA}")

    # ---- ^5-304: atītaṃ / anāgataṃ / paccuppannaṃ atthi ---------------------------------------------------------
    add("5-304", opening(PAST, ATTHA_FULL), opening(FUT, ATTHA_FULL), opening(PRES, ATTHA_SHORT))

    # ---- ^5-305: hevatthi, heva natthi; kintatthi ----------------------------------------------------------------
    def ans(x, others):             # X Xnti hevatthi, X Ynti heva natthi, X Znti heva natthīti.
        return S.cap(", ".join([ex(x, x)] + [ex(x, o, True) for o in others])) + "."

    l1 = kinti(f"{PAST} {HH}", ans(PAST, (FUT, PRES)), ATTHA_FULL)
    l2 = kinti(f"{FUT} {HH}", ans(FUT, (PAST, PRES)), ATTHA_SHORT2)
    l3 = kinti(f"{PRES} {HH}", ans(PRES, (PAST, FUT)), ATTHA_SHORT)
    three = "; ".join(f"{t} {HH}" for t in (PAST, FUT, PRES))
    cross = ", ".join(ex(a, b) for a, b in ((PAST, FUT), (PAST, PRES), (FUT, PAST), (FUT, PRES), (PRES, PAST),
                                            (PRES, FUT)))
    l4 = (f"{S.na_vattabbam(three)} {YES} {Q(cross)} {NO_PE} "
          f"{S.tena_hi(', '.join(f'{t} {HH}' for t in (PAST, FUT, PRES)))}")
    #   Na hevaṃ vattabbe.…Pe…. Tena hi atītaṃ hevatthi heva natthi, … (commas supplied in the first two pairs)
    add("5-305", l1, l2, l3, l4)

    # ---- ^5-306: rūpaṃ … viññāṇaṃ ---------------------------------------------------------------------------------
    CHAIN = f"{VEDANA}{PE} {SANNA}{PE} {SANKHARA}{PE} {VINNANA}"   # Vedanā… saññā… saṅkhārā… viññāṇaṃ
    m1 = opening(RUPA, ATTHA_FULL)
    m2 = opening(CHAIN, ATTHA_SHORT)
    ans_r = (S.cap(f"{ex(RUPA, RUPA)}, {ex(RUPA, VEDANA, True)}{PE} {ex(RUPA, SANNA, True)}{PE} "
                   f"{ex(RUPA, SANKHARA, True)}{PE} {ex(RUPA, VINNANA, True)}") + ".")
    #   Rūpaṃ rūpanti hevatthi, rūpaṃ vedanāti hevaṃ natthi…pe… rūpaṃ saññāti heva natthi…pe… …
    m3 = kinti(f"{RUPA} {HH}", ans_r, ATTHA_SHORT)
    ans_v = (S.cap(f"{ex(VINNANA, VINNANA)}. {S.cap(ex(VINNANA, RUPA, True))}{PE} {ex(VINNANA, VEDANA, True)}{PE} "
                   f"{ex(VINNANA, SANNA, True)}{PE} {ex(VINNANA, SANKHARA, True)}") + ".")
    #   Viññāṇaṃ viññāṇanti hevatthi. Viññāṇaṃ rūpanti heva natthi…pe… …
    m4 = kinti(f"{CHAIN} {HH}", ans_v, ATTHA_SHORT)
    two = f"{RUPA} {HH}; {CHAIN} {HH}"
    cross_r = (f"{ex(RUPA, VEDANA)}{PE} {ex(RUPA, SANNA)}{PE} {ex(RUPA, SANKHARA)}{PE} {ex(RUPA, VINNANA)}{PE} "
               f"{VEDANA}{PE} {SANNA}{PE} {SANKHARA}{PE} {ex(VINNANA, RUPA)}{PE} {ex(VINNANA, VEDANA)}{PE} "
               f"{ex(VINNANA, SANNA)}{PE} {ex(VINNANA, SANKHARA)}")
    #   Rūpaṃ vedanāti hevatthi…pe… … rūpaṃ viññāṇanti hevatthi… vedanā… saññā … saṅkhārā… viññāṇaṃ rūpanti …
    m5 = (f"{S.na_vattabbam(two)} {YES} {Q(cross_r)} {NO_PE} vậy thì {two}.")
    #   the quote of "Na vattabbaṃ – "…" has no closing mark in the Pāli: supplied as meant
    add("5-306", m1, m2, m3, m4, m5, END_KATHA, TASSUDDANAM, *UDDANA, VAGGA_1, MAHAVAGGO)
    return segs


def main():
    check_shared()
    S.check_reused()
    S.write(NAME, build())


if __name__ == "__main__":
    main()
