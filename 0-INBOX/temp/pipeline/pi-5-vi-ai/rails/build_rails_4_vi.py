"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 4, Jahatikathā (^5-4-0 … ^5-281).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/4-jahatikatha.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, NANU, hanci_neg, tena_hi …).
Every string marked (pi-N) is asserted to occur in that book's approved Vietnamese rails; S.write runs the
per-line dash / quote / NFC / id checks against the Pāli.
New recurring strings: notes-rails-4.md.

usage: python -I -X utf8 -B build_rails_4_vi.py
       python -I -X utf8 -B build_rails_4_vi.py --probe <chapter.md> <regex> [n] [maxchars]   (pi-5 rails lookup)
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
NAME = "4-jahatikatha.md"
Q, NANU, PE, YES, NO, NO_PE = S.Q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE

# ---------------------------------------------------------------------------------------------------------------
# Headings
# ---------------------------------------------------------------------------------------------------------------
KATHA_NAME = "sự dứt bỏ"                              # Jahatikathā (jahati «dứt bỏ»)
H_KATHA = S.katha(KATHA_NAME)                         # ### Jahatikathā
END_KATHA = S.katha_end(KATHA_NAME)                   # Jahatikathā niṭṭhitā.
H_NASUTTA = S.katha("việc không dẫn kinh")            # Nasuttāharaṇakathā
H_SUTTA = S.katha("việc dẫn kinh")                    # Suttāharaṇakathā

# ---------------------------------------------------------------------------------------------------------------
# Terms (termbase; pi-N where identical Pāli exists)
# ---------------------------------------------------------------------------------------------------------------
PU = "người phàm phu"                                 # puthujjano
KRB = "sự tham đắm dục lạc và ác ý"                   # kāmarāgabyāpādaṃ (pi-1 / pi-4)
J, V = "dứt bỏ", "đè nén"                             # jahati / vikkhambheti
ANA = "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại"   # anāgāmiphalasacchikiriyāya paṭipanno puggalo (pi-4)
SACCHI = "trong khi tự mình chứng nghiệm thành quả không trở lại"            # anāgāmiphalaṃ sacchikaronto
MODES = ["một cách hoàn toàn",                        # accantaṃ
         "không còn sót lại",                         # anavasesaṃ (pi-1)
         "không còn tái khởi",                        # appaṭisandhiyaṃ
         "cùng với gốc rễ",                           # samūlaṃ
         "cùng với khao khát",                        # sataṇhaṃ
         "cùng với khuynh hướng tiềm ẩn",             # sānusayaṃ
         "bằng hiểu biết cao quý",                    # ariyena ñāṇena
         "bằng con đường cao quý",                    # ariyena maggena
         "trong khi thấu triệt điều không thể bị lay chuyển",   # akuppaṃ paṭivijjhanto
         SACCHI]
SO_CA = "và người ấy"                                 # so ca (person)
SO_CA_MAGGO = "và con đường ấy"                       # so ca maggo
M_RUPA = "con đường thuộc cõi hình sắc"               # rūpāvacaro maggo / rūpāvacarena maggena
M_ANA = "con đường không trở lại"                     # anāgāmimaggena
M_SOTA = "con đường vào dòng"                         # sotāpattimaggena
M_SAKA = "con đường trở lại một lần"                  # sakadāgāmimaggena
KATAMENA = "Bằng con đường nào?"                      # Katamena maggenāti?

# path qualities (pi-1 / pi-2 wording; termbase)
POS = ["dẫn đến giải thoát",                          # niyyāniko (pi-2)
       "dẫn đến sự diệt tận",                         # khayagāmī
       "dẫn đến sự giác ngộ",                         # bodhagāmī
       "dẫn đến sự giảm trừ",                         # apacayagāmī (pi-1)
       "không phải là đối tượng của ô nhiễm",         # anāsavo (pi-2)
       "không phải là đối tượng của xiềng xích",      # asaṃyojaniyo (pi-2)
       "không phải là đối tượng của nút thắt",        # aganthaniyo (pi-2)
       "không phải là đối tượng của dòng lũ",         # anoghaniyo (pi-2)
       "không phải là đối tượng của ách",             # ayoganiyo
       "không phải là đối tượng của chướng ngại",     # anīvaraṇiyo
       "không bị sự hiểu sai lệch nắm giữ",           # aparāmaṭṭho (pi-1)
       "không phải là đối tượng của sự bám víu",      # anupādāniyo (pi-1)
       "không phải là đối tượng của phiền não"]       # asaṃkilesiyo (pi-2)
NEG = ["không dẫn đến giải thoát",                    # aniyyāniko (pi-2)
       "không dẫn đến sự diệt tận",                   # na khayagāmī
       "không dẫn đến sự giác ngộ",                   # na bodhagāmī
       "không dẫn đến sự giảm trừ",                   # na apacayagāmī (pi-2)
       "là đối tượng của ô nhiễm",                    # sāsavo (pi-2)
       "là đối tượng của xiềng xích",                 # saṃyojaniyo (pi-2)
       "là đối tượng của phiền não"]                  # saṃkilesiyo (pi-2)

TH_ANA = (f"{PU} đã lìa tham đắm đối với các dục lạc, ngay cùng lúc với sự thấu hiểu Giáo Pháp, "
          f"đứng vững nơi thành quả không trở lại")
#   Puthujjano kāmesu vītarāgo saha dhammābhisamayā anāgāmiphale saṇṭhāti
#   («lìa tham đắm đối với các dục lạc»: pi-2; «sự thấu hiểu Giáo Pháp»: pi-4)
APUBBA = "không trước không sau"                      # apubbaṃ acarimaṃ (pi-2)
TINI_PHALA = "ba thành quả của đời sống sa-môn"       # tīṇi sāmaññaphalāni (pi-1 «thành quả … của đời sống sa-môn»)
THREE = ("có sự tụ hợp của ba sự tiếp xúc, ba cảm giác, ba tri giác, ba chủ ý, ba tâm, ba niềm tin, "
         "ba sự tinh tấn, ba sự tỉnh thức, ba sự định tâm, ba trí tuệ")
#   Tiṇṇaṃ phassānaṃ … tissannaṃ paññānaṃ samodhānaṃ hoti
FETTERS3 = "quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức"   # (pi-1)
OLARIKA = "sự tham đắm dục lạc ở dạng thô, ác ý ở dạng thô"   # oḷārikaṃ kāmarāgaṃ oḷārikaṃ byāpādaṃ
VUTTAM_RANG = "Đức Thế Tôn đã nói rằng"               # … vuttaṃ bhagavatā (no quote, no dash)
SOTA_PAHANA = "thành quả vào dòng là do dứt bỏ ba xiềng xích"                    # tiṇṇaṃ saṃyojanānaṃ pahānā sotāpattiphalaṃ
SAKA_TANU = "thành quả trở lại một lần là do sự tham đắm dục lạc và ác ý suy yếu"  # kāmarāgabyāpādānaṃ tanubhāvā sakadāgāmiphalaṃ

# Sutta a. ni. 6.54 (verse)
NIRAMA = "Không còn mùi tanh, hết lòng hướng về lòng trắc ẩn"   # Nirāmagandhā karuṇedhimuttā
KAMASAM = "đã vượt qua xiềng xích của dục lạc"                  # kāmasaṃyojanātigā
VIRAJ = "Sau khi làm phai nhạt sự tham đắm dục lạc, họ đã đi đến cõi Phạm Thiên"   # Kāmarāgaṃ virājetvā, brahmalokūpagā ahu
# Sutta a. ni. 7.66 (Sunetta)
TAM_KISSA = "Vì sao vậy?"                                          # Taṃ kissa hetu? (pi-2)
NA_BODHA = "vì không hiểu ra, không thấu triệt"                    # ananubodhā appaṭivedhā
BHAVANETTI = "sợi dây dẫn đến hiện hữu"                            # bhavanetti (pi-1)
SOKA = "sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng"   # sokehi … upāyāsehi (pi-2)
DUKKHA_ANTA = "người đi đến tận cùng của khổ đau"                  # dukkhassantakaro (pi-4)

REUSED4 = [  # (Pāli, Vietnamese, book)
    ("kāmarāgabyāpādānaṃ", KRB, "1"),
    ("anāgāmiphalasacchikiriyāya paṭipanno", ANA, "4"),
    ("anavasesa-", "không còn sót lại", "1"),
    ("niyyāniko", POS[0], "2"), ("apacayagāmī", POS[3], "1"), ("anāsavo", POS[4], "2"),
    ("asaṃyojaniyo", POS[5], "2"), ("aganthaniyo", POS[6], "2"), ("anoghaniyo", POS[7], "2"),
    ("yoganiyā", "là đối tượng của ách", "1"), ("nīvaraṇiyā", "là đối tượng của chướng ngại", "1"),
    ("aparāmaṭṭhā", POS[10], "1"), ("anupādāniyā", POS[11], "1"), ("asaṃkilesiko", POS[12], "2"),
    ("aniyyāniko", NEG[0], "2"), ("na apacayagāmī", NEG[3], "2"), ("sāsavo", NEG[4], "2"),
    ("saṃyojaniyo", NEG[5], "2"), ("saṃkilesiko", NEG[6], "2"),
    ("kāmesu vītarāgo", "lìa tham đắm đối với các dục lạc", "2"),
    ("dhammābhisamayo", "sự thấu hiểu Giáo Pháp", "4"),
    ("apubbaṃ acarimaṃ", APUBBA, "2"),
    ("sāmaññaphalāni", "thành quả của đời sống sa-môn", "1"),
    ("sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāso", FETTERS3, "1"),
    ("tiṇṇaṃ saṃyojanānaṃ", "ba xiềng xích", "4"),
    ("brahmaloka", "cõi Phạm Thiên", "1"),
    ("Taṃ kissa hetu?", TAM_KISSA, "2"),
    ("bhavanetti", BHAVANETTI, "1"),
    ("sokaparidevadukkhadomanassupāyāsā", SOKA, "2"),
    ("dukkhassantakaro", DUKKHA_ANTA, "4"),
    ("jāti jarā … maraṇaṃ", "sự sinh, sự lão hóa", "1"),
    ("satthā", "bậc đạo sư", "4"),
    ("dīghāyukā", "sống lâu", "2"),
]


def check_reused4():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                          for p in sorted(d.glob("*.md")))).lower()
    bad = [(p, v, b) for p, v, b in REUSED4 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def modes(v, neg=False, short=None):
    """X-ṃ jahati list. short = (first, last) indices kept around a …pe… gap; neg puts «không» before each."""
    n = "không " if neg else ""
    items = [f"{n}{v} {m}" for m in MODES]
    if short is None:
        return ", ".join(items)
    k, = short
    return ", ".join(items[:k]) + f"{PE} " + items[-1]


def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    # ---- ### Jahatikathā / #### Nasuttāharaṇakathā --------------------------------------------------------------
    add("5-4-0", f"### {H_KATHA}")
    add("5-4-1-0", f"#### {H_NASUTTA}")

    l5 = f"{Q(f'{PU} {J} {KRB}')} {YES} {Q(modes(J))} {NO_PE}"
    l6 = f"{Q(f'{PU} {V} {KRB}')} {YES} {Q(modes(V))} {NO_PE}"

    def pair(v, s1, s2, k1, k2, neg=False):
        a = f"{s1} {v} {KRB}, {SO_CA} {modes(v, neg, (k1,))}"
        b = f"{s2} {v} {KRB}, {SO_CA} {modes(v, neg, (k2,))}"
        return f"{Q(a)} {YES} {Q(b)} {NO_PE}"

    l7 = pair(J, ANA, PU, 2, 2)
    l8 = pair(V, ANA, PU, 2, 2)
    l9 = pair(J, PU, ANA, 2, 1, neg=True)
    l10 = pair(V, PU, ANA, 2, 2, neg=True)

    pos_full = ", ".join(POS)
    pos_short = ", ".join(POS[:5]) + f"{PE} " + POS[-1]
    neg_l11 = ", ".join(NEG[:6]) + f"{PE} " + NEG[-1]
    neg_short = ", ".join(NEG[:5]) + f"{PE} " + NEG[-1]
    neg_hanci = ", ".join(NEG[:2]) + f"{PE} " + NEG[-1]
    q_rupa = f"{PU} {J} {KRB} bằng {M_RUPA}"
    l11 = (f"{Q(f'{PU} {J} {KRB}')} {YES} {KATAMENA} Bằng {M_RUPA}. {Q(f'{M_RUPA} {pos_full}')} {NO} "
           f"{NANU(f'{M_RUPA} {neg_l11}')} {YES} {S.hanci_neg(f'{M_RUPA} {neg_hanci}', q_rupa)}")
    a = f"{ANA} {J} {KRB} bằng {M_ANA}"
    l12 = f"{Q(f'{a}, {SO_CA_MAGGO} {pos_short}')} {YES} {Q(f'{q_rupa}, {SO_CA_MAGGO} {pos_short}')} {NO_PE}"
    l13 = f"{Q(f'{q_rupa}, {SO_CA_MAGGO} {neg_short}')} {YES} {Q(f'{a}, {SO_CA_MAGGO} {neg_short}')} {NO_PE}"
    add("5-279", l5, l6, l7, l8, l9, l10, l11, l12, l13)

    # ---- ^5-280 ----------------------------------------------------------------------------------------------------
    q_appu_magga = f"{APUBBA}, tu tập ba con đường"            # Apubbaṃ acarimaṃ tayo magge bhāveti
    q_appu_phala = f"{APUBBA}, tự mình chứng nghiệm {TINI_PHALA}"
    q_fett = f"{J} {FETTERS3} bằng {M_ANA}"                   # Anāgāmimaggena sakkāyadiṭṭhiṃ … jahati
    add("5-280",
        f"{Q(TH_ANA)} {YES} {Q('đứng vững nơi trạng thái A-la-hán')} {NO_PE}",
        f"{Q(TH_ANA)} {YES} {Q(q_appu_magga)} {NO_PE}",
        f"{Q(q_appu_magga)} {YES} {Q(q_appu_phala)} {NO_PE}",
        f"{Q(q_appu_phala)} {YES} {Q(THREE)} {NO_PE}",
        f"{Q(TH_ANA)} {YES} {Q(f'bằng {M_SOTA}')} {NO_PE}",
        f"{Q(f'bằng {M_SAKA}')} {NO} {KATAMENA} Bằng {M_ANA}. {Q(q_fett)} {NO_PE}")

    # ---- #### Suttāharaṇakathā --------------------------------------------------------------------------------------
    add("5-4-2-0", f"#### {H_SUTTA}")
    q_olar = f"{J} {OLARIKA} bằng {M_ANA}"
    q_pu = f"{PU} {J} {KRB}"
    l24 = (f"{Q(q_fett)} {YES} {NANU(f'{VUTTAM_RANG} {SOTA_PAHANA}')} {YES} "
           f"{S.hanci_neg(f'{VUTTAM_RANG} {SOTA_PAHANA}', q_fett)} {Q(q_olar)} {NO_PE}")
    l25 = (f"{Q(q_olar)} {YES} {NANU(f'{VUTTAM_RANG} {SAKA_TANU}')} {YES} "
           f"{S.hanci_neg(f'{VUTTAM_RANG} {SAKA_TANU}', q_olar)}")
    l26 = (f"{Q(TH_ANA)} {YES} "
           f"{Q('bất cứ ai thấu hiểu Giáo Pháp, thì tất cả những người ấy, ngay cùng lúc với sự thấu hiểu Giáo Pháp, đều đứng vững nơi thành quả không trở lại')} "
           f"{NO_PE}")
    l27 = f"{S.na_vattabbam(q_pu)} {YES} {S.NANU_VUTTAM}"
    v28 = ("“Thời quá khứ, đã có những vị ấy" + S.var(f"{S.CIT['a. ni.']} 6.54", "ahiṃsakā")
           + ", sáu bậc đạo sư lừng danh;")
    v29 = f"{NIRAMA}" + S.var_sp("Sī., Ka.", "karuṇādhimuttā") + f", {KAMASAM}."
    v30 = f"“{VIRAJ};"
    v31 = "Họ đã có các đệ tử, lên đến nhiều trăm người."
    v32 = f"“{NIRAMA}, {KAMASAM};"
    v33 = f"{VIRAJ}” [{S.CIT['a. ni.']} 6.54]."
    l34 = f"{S.ATTHEVA} {YES} {S.tena_hi(q_pu)}"
    l35 = (f"{Q(q_pu)} {YES} {S.NANU_VUTTAM} “Này các tỳ-khưu, bậc đạo sư Su-nét-ta ấy, dù sống lâu như vậy, "
           f"tồn tại lâu dài như vậy, vẫn không thoát khỏi sự sinh, sự lão hóa, sự chết, {SOKA}; "
           f"Ta nói rằng vị ấy không thoát khỏi khổ đau. {TAM_KISSA} {S.cap(NA_BODHA)} bốn hiện tượng. "
           f"Bốn hiện tượng nào? {S.cap(NA_BODHA)} giới hạnh cao quý, định tâm cao quý, trí tuệ cao quý, "
           f"{NA_BODHA} sự giải thoát cao quý. Này các tỳ-khưu, nay giới hạnh cao quý ấy đã được hiểu ra, "
           f"đã được thấu triệt, định tâm cao quý đã được hiểu ra, đã được thấu triệt, trí tuệ cao quý đã được "
           f"hiểu ra, đã được thấu triệt, sự giải thoát cao quý đã được hiểu ra, đã được thấu triệt, khao khát "
           f"được hiện hữu đã bị đoạn diệt, {BHAVANETTI} đã bị diệt tận, giờ đây không có sự hiện hữu mới.")
    v36 = "“Giới hạnh, định tâm và trí tuệ, cùng sự giải thoát không có điều gì cao hơn;"
    v37 = "Các hiện tượng này đã được bậc Cồ-đàm lừng danh hiểu ra."
    v38 = "“Như vậy, Đức Phật, sau khi hiểu biết trực tiếp, đã giảng Giáo Pháp cho các tỳ-khưu;"
    v39 = f"Bậc đạo sư, {DUKKHA_ANTA}, bậc có mắt, đã nhập Niết-bàn trọn vẹn” [{S.CIT['a. ni.']} 7.66]."
    l40 = f"{S.ATTHEVA} {YES} {S.tena_hi_na(q_pu)}"
    add("5-281", l24, l25, l26, l27, v28, v29, v30, v31, v32, v33, l34, l35, v36, v37, v38, v39, l40, END_KATHA)
    return segs


def probe(ch, pat, n=40, mx=500):
    pl = [x for x in (S.PALI_DIR / ch).read_text(encoding="utf-8").splitlines() if x.strip()]
    vl = [x for x in (S.OUT_DIR / ch).read_text(encoding="utf-8").splitlines() if x.strip()]
    k = 0
    for i, ln in enumerate(pl):
        if re.search(pat, ln):
            print(i + 1, "PI:", ln[:mx])
            print("   VI:", vl[i][:mx])
            k += 1
            if k >= n:
                return


def main():
    check_reused4()
    S.write(NAME, build())


if __name__ == "__main__":
    if sys.argv[1:2] == ["--probe"]:
        probe(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 40,
              int(sys.argv[5]) if len(sys.argv) > 5 else 500)
    else:
        main()
