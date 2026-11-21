# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 4: 4-jahatikatha.md (Jahatikathā, ^5-4-0 … ^5-281).

Imports the approved sample builder (build_sample_vi) for every debate frame; the chapter's own repeated
phrases are fixed strings below, so every repeat is byte-identical. Every string claimed from the pi-1..4
Vietnamese rails is asserted to occur there; the sample's per-line checks (IDs, dashes, quotes, NFC,
foreign letters) are run against the Pāli.

run:  python -I -X utf8 build_4_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "4-jahatikatha.md"

# ================================================================ terms (cross-book where marked)
PUTHUJJANA = "người phàm phu"                                   # puthujjano (pi-1 assutavā puthujjano)
KRB = "sự tham đắm dục lạc và ác ý"                              # kāmarāgabyāpādaṃ (pi-1, pi-4)
JAHATI = "dứt bỏ"                                               # jahati (pahāna «sự dứt bỏ» pi-1)
VIKKHAMBHETI = "đè nén"                                         # vikkhambheti (new)
ANAGAMI_PATIPANNO = "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại"
# anāgāmiphalasacchikiriyāya paṭipanno puggalo (pi-4 ^4-43)
ANAGAMIPHALA = "thành quả không trở lại"                        # anāgāmiphala (pi-2, pi-4)
SACCHIKARONTO = f"trong khi tự mình chứng nghiệm {ANAGAMIPHALA}"  # anāgāmiphalaṃ sacchikaronto (pi-4 sacchikaroti)
# the ten manners (accantaṃ … sacchikaronto)
MANNERS = [
    "một cách hoàn toàn",                                # accantaṃ (new)
    "không còn sót lại",                                 # anavasesaṃ (pi-1 anavasesappahānāya)
    "không còn tái khởi",                                # appaṭisandhiyaṃ (new)
    "cùng với gốc rễ",                                   # samūlaṃ (mūla «gốc rễ» pi-1)
    "cùng với khao khát",                                # sataṇhaṃ (taṇhā «khao khát» pi-1)
    "cùng với khuynh hướng tiềm ẩn",                     # sānusayaṃ (anusaya pi-2)
    "bằng hiểu biết cao quý",                            # ariyena ñāṇena (ñāṇa «hiểu biết» pi-1, ariya «cao quý» pi-2)
    "bằng con đường cao quý",                            # ariyena maggena (ariyamagga pi-1)
    "trong khi thấu triệt điều không thể bị lay chuyển",  # akuppaṃ paṭivijjhanto (pi-4 akuppa, pi-2 paṭivijjhati)
    SACCHIKARONTO,
]
NEG_MANNER = {0: "không {v} một cách hoàn toàn", 1: "không {v} đến mức không còn sót lại",
              9: "không {v} " + SACCHIKARONTO}                  # na accantaṃ / na anavasesaṃ / na … sacchikaronto


def manners_full(v):
    return ", ".join(f"{v} {m}" for m in MANNERS)


def manners_pe(v):
    """so ca accantaṃ V, anavasesaṃ V…pe… anāgāmiphalaṃ sacchikaronto V"""
    return f"{v} {MANNERS[0]}, {v} {MANNERS[1]}… {v} {MANNERS[9]}"


def neg_pe(v, two=True):
    """so ca na accantaṃ V[, na anavasesaṃ V]…pe… na anāgāmiphalaṃ sacchikaronto V"""
    first = NEG_MANNER[0].format(v=v) + (", " + NEG_MANNER[1].format(v=v) if two else "")
    return f"{first}… {NEG_MANNER[9].format(v=v)}"


RUPAVACARA_MAGGA = "con đường thuộc cõi hình sắc"              # rūpāvacara maggo (pi-1 rūpāvacara)
ANAGAMIMAGGA = "con đường không trở lại"                        # anāgāmimagga (pi-2)
SOTAPATTIMAGGA = "con đường vào dòng"                           # sotāpattimagga (pi-2)
SAKADAGAMIMAGGA = "con đường trở lại một lần"                   # sakadāgāmimagga (pi-2)
# the lokuttara qualities of a path (niyyāniko … asaṃkilesiyo) and their opposites
POS = ["dẫn đến giải thoát", "dẫn đến sự diệt tận", "dẫn đến sự giác ngộ", "dẫn đến sự giảm trừ",
       "không phải là đối tượng của ô nhiễm", "không phải là đối tượng của xiềng xích",
       "không phải là đối tượng của nút thắt", "không phải là đối tượng của dòng lũ",
       "không phải là đối tượng của ách", "không phải là đối tượng của chướng ngại",
       "không bị sự hiểu sai lệch nắm giữ", "không phải là đối tượng của sự bám víu",
       "không phải là đối tượng của phiền não"]
# niyyāniko (pi-1) khayagāmī (new) bodhagāmī (new) apacayagāmī (pi-1) anāsavo asaṃyojaniyo aganthaniyo anoghaniyo
# ayoganiyo anīvaraṇiyo aparāmaṭṭho anupādāniyo asaṃkilesiyo (pi-1 matrix (b) names)
NEG = ["không dẫn đến giải thoát", "không dẫn đến sự diệt tận", "không dẫn đến sự giác ngộ",
       "không dẫn đến sự giảm trừ", "là đối tượng của ô nhiễm", "là đối tượng của xiềng xích"]
NEG_LAST = "là đối tượng của phiền não"
# aniyyāniko na khayagāmī na bodhagāmī na apacayagāmī sāsavo saṃyojaniyo … saṃkilesiyo
POS_PE = f"{', '.join(POS[:5])}… {POS[-1]}"                     # niyyāniko … anāsavo…pe… asaṃkilesiyo
POS_ALL = ", ".join(POS)                                       # niyyāniko … asaṃkilesiyo (full)
NEG_PE6 = f"{', '.join(NEG[:6])}… {NEG_LAST}"                   # aniyyāniko … sāsavo saṃyojaniyo…pe… saṃkilesiyo
NEG_PE5 = f"{', '.join(NEG[:5])}… {NEG_LAST}"                   # aniyyāniko … sāsavo…pe… saṃkilesiyo
NEG_PE2 = f"{', '.join(NEG[:2])}… {NEG_LAST}"                   # aniyyāniko na khayagāmī…pe… saṃkilesiyo

SO_CA_MAGGO = "và con đường ấy"                                 # so ca maggo
SO_CA = "và người ấy"                                           # so ca

KAMESU_VITARAGO = f"{PUTHUJJANA} đã lìa tham đắm đối với các dục lạc"   # puthujjano kāmesu vītarāgo (pi-2)
SAHA_ABHISAMAYA = "cùng lúc với sự thấu hiểu Giáo Pháp"        # saha dhammābhisamayā (abhisamaya «sự thấu hiểu» pi-4)
SANTHATI = f"đứng vững trong {ANAGAMIPHALA}"                     # anāgāmiphale saṇṭhāti (new)
PV = f"{KAMESU_VITARAGO}, {SAHA_ABHISAMAYA}, {SANTHATI}"
APUBBAM = "cùng một lúc, không trước không sau"                 # apubbaṃ acarimaṃ (new)
TAYO_MAGGE = f"{APUBBAM}, tu tập ba con đường"                   # … tayo magge bhāveti (bhāveti «tu tập» pi-1)
TINI_PHALANI = f"{APUBBAM}, tự mình chứng nghiệm ba thành quả của đời sống sa-môn"  # sāmaññaphala (pi-1)
SAMODHANA = ("có sự tụ hợp của ba sự tiếp xúc, ba cảm giác, ba tri giác, ba chủ ý, ba tâm, ba niềm tin, "
             "ba sự tinh tấn, ba sự tỉnh thức, ba sự định tâm, ba trí tuệ")   # samodhāna «sự tụ hợp» (pi-2)
THREE_FETTERS = "quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức"  # (pi-1 ^1-1006)
AM_3 = f"{JAHATI} {THREE_FETTERS} bằng {ANAGAMIMAGGA}"          # anāgāmimaggena sakkāyadiṭṭhiṃ … jahati
OLARIKA = "sự tham đắm dục lạc ở dạng thô, ác ý ở dạng thô"     # oḷārikaṃ kāmarāgaṃ oḷārikaṃ byāpādaṃ (pi-1 «ở dạng thô»)
AM_OL = f"{JAHATI} {OLARIKA} bằng {ANAGAMIMAGGA}"
VB_SOTA = "Đức Thế Tôn đã nói rằng thành quả vào dòng là nhờ dứt bỏ ba xiềng xích"
# tiṇṇaṃ saṃyojanānaṃ pahānā sotāpattiphalaṃ vuttaṃ bhagavatā
VB_SAKA = "Đức Thế Tôn đã nói rằng thành quả trở lại một lần là nhờ sự tham đắm dục lạc và ác ý suy yếu"
# kāmarāgabyāpādānaṃ tanubhāvā sakadāgāmiphalaṃ vuttaṃ bhagavatā (tanubhāva «suy yếu» pi-1, pi-4)
KATAMENA = "Bằng con đường nào?"                                # Katamena maggenāti?

P_J = f"{PUTHUJJANA} {JAHATI} {KRB}"                            # jahati puthujjano kāmarāgabyāpādaṃ
P_V = f"{PUTHUJJANA} {VIKKHAMBHETI} {KRB}"
A_J = f"{ANAGAMI_PATIPANNO}, {JAHATI} {KRB}"                    # jahati anāgāmi… paṭipanno puggalo kāmarāgabyāpādaṃ
A_V = f"{ANAGAMI_PATIPANNO}, {VIKKHAMBHETI} {KRB}"
P_J_RUPA = f"{P_J} bằng {RUPAVACARA_MAGGA}"                     # … rūpāvacarena maggena kāmarāgabyāpādaṃ
A_J_ANA = f"{A_J} bằng {ANAGAMIMAGGA}"                          # … anāgāmimaggena kāmarāgabyāpādaṃ

# ================================================================ sutta passages
SUNETTA = "Su-nét-ta"   # sunetto (new name form)
AN_6_54 = "Tăng Chi Bộ Kinh 6.54"
AN_7_66 = "Tăng Chi Bộ Kinh 7.66"
NIRAMAGANDHA = "Không còn mùi tanh hôi ô uế, hết lòng hướng về lòng trắc ẩn"   # Nirāmagandhā karuṇedhimuttā
KAMASAMYOJANA = "đã vượt qua xiềng xích dục lạc"                                # kāmasaṃyojanātigā
VIRAJETVA = "Sau khi làm phai nhạt sự tham đắm dục lạc, các vị ấy đã đi đến cõi Phạm Thiên"
# Kāmarāgaṃ virājetvā, brahmalokūpagā ahu (virāga «phai nhạt» pi-1; brahmaloka «cõi Phạm Thiên» pi-1)
SUNETTA_PROSE = (
    f"“Quả thật, này các tỳ-khưu, bậc đạo sư {SUNETTA} ấy, dù sống lâu như vậy, dù tồn tại lâu dài như vậy, "
    "vẫn không thoát khỏi sự sinh, sự lão hóa, sự chết, sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và "
    "sự tuyệt vọng; Ta nói rằng vị ấy không thoát khỏi khổ đau. Vì sao vậy? Do không hiểu ra, không thấu triệt "
    "bốn hiện tượng. Bốn hiện tượng nào? Do không hiểu ra, không thấu triệt giới hạnh cao quý, định tâm cao quý, "
    "trí tuệ cao quý và sự giải thoát cao quý. Này các tỳ-khưu, nay giới hạnh cao quý ấy đã được hiểu ra, đã được "
    "thấu triệt; định tâm cao quý đã được hiểu ra, đã được thấu triệt; trí tuệ cao quý đã được hiểu ra, đã được "
    "thấu triệt; sự giải thoát cao quý đã được hiểu ra, đã được thấu triệt; khao khát được hiện hữu đã bị đoạn "
    "diệt, sợi dây dẫn đến hiện hữu đã bị diệt tận, nay không còn sự tái sinh nữa.")

CROSS = [
    ("người phàm phu", 1), ("sự tham đắm dục lạc và ác ý", 1), ("sự tham đắm dục lạc và ác ý", 4),
    (ANAGAMI_PATIPANNO, 4), ("thành quả không trở lại", 4), ("tự mình chứng nghiệm", 4),
    ("dứt bỏ sự tham đắm dục lạc và ác ý không còn sót lại", 1), ("gốc rễ", 1), ("khao khát", 1),
    ("khuynh hướng tiềm ẩn", 2), ("hiểu biết", 1), ("con đường cao quý", 1), ("không thể bị lay chuyển", 4),
    ("thấu triệt", 2), ("thuộc cõi hình sắc", 1), ("con đường không trở lại", 2), ("con đường vào dòng", 2),
    ("con đường trở lại một lần", 2), ("thành quả vào dòng", 2), ("thành quả trở lại một lần", 2),
    ("dẫn đến giải thoát", 1), ("không dẫn đến giải thoát", 1), ("dẫn đến sự giảm trừ", 1),
    ("sự giác ngộ", 2), ("diệt tận", 1),
] + [(s, 1) for s in POS[4:]] + [(s, 1) for s in NEG[4:]] + [(NEG_LAST, 1)] + [
    ("lìa tham đắm đối với các dục lạc", 2), ("sự không thấu hiểu", 1), ("sự thấu hiểu", 4),
    ("Giáo Pháp", 1), ("tu tập", 1), ("thành quả của đời sống sa-môn", 1), ("sự tụ hợp", 2),
    ("sự tiếp xúc", 1), ("chủ ý", 1), ("niềm tin", 1), ("tinh tấn", 1), ("sự tỉnh thức", 1), ("định tâm", 1),
    ("trí tuệ", 1), (THREE_FETTERS, 1), ("ba xiềng xích", 4), ("ở dạng thô", 1), ("suy yếu", 4),
    ("bậc đạo sư", 4), ("sống lâu", 2), ("sự sinh", 2), ("sự lão hóa", 2), ("sự chết", 2),
    ("sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng", 2), ("Vì sao vậy?", 2),
    ("sự không hiểu ra", 1), ("sự không thấu triệt", 1), ("giới hạnh cao quý", 4), ("sự giải thoát", 1),
    ("hiện hữu", 1), ("sợi dây dẫn đến hiện hữu", 1), ("không có điều gì cao hơn", 1), ("cõi Phạm Thiên", 1),
    ("lòng trắc ẩn", 2), ("xiềng xích", 1), ("phai nhạt", 1), ("người đi đến tận cùng của khổ đau", 4),
    ("có mắt", 4), ("nhập Niết-bàn trọn vẹn", 4), ("hiểu biết trực tiếp", 2), ("Đức Phật", 4),
    ("đệ tử", 4), ("dục lạc", 1),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"ch4 cross-book asserts: {len(CROSS)} strings found in pi-1..4 rails")


def build():
    Q, AM, NH, NHP = B.Q, B.AMANTA, B.NA_HEVAM, B.NA_HEVAM_PE
    d = B.Doc()
    d.head(3, B.KATHA.format(x="sự dứt bỏ"), "5-4-0")                 # Jahatikathā
    d.head(4, "Phần không dẫn kinh", "5-4-1-0")                        # Nasuttāharaṇakathā
    d.seg("5-279",
          f"{Q(P_J)} {AM} {Q(manners_full(JAHATI))} {NHP}",
          f"{Q(P_V)} {AM} {Q(manners_full(VIKKHAMBHETI))} {NHP}",
          f"{Q(f'{A_J}, {SO_CA} {manners_pe(JAHATI)}')} {AM} {Q(f'{P_J}, {SO_CA} {manners_pe(JAHATI)}')} {NHP}",
          f"{Q(f'{A_V}, {SO_CA} {manners_pe(VIKKHAMBHETI)}')} {AM} "
          f"{Q(f'{P_V}, {SO_CA} {manners_pe(VIKKHAMBHETI)}')} {NHP}",
          f"{Q(f'{P_J}, {SO_CA} {neg_pe(JAHATI)}')} {AM} {Q(f'{A_J}, {SO_CA} {neg_pe(JAHATI, two=False)}')} {NHP}",
          f"{Q(f'{P_V}, {SO_CA} {neg_pe(VIKKHAMBHETI)}')} {AM} {Q(f'{A_V}, {SO_CA} {neg_pe(VIKKHAMBHETI)}')} {NHP}",
          f"{Q(P_J)} {AM} {KATAMENA} Bằng {RUPAVACARA_MAGGA}. "
          f"{Q(f'{RUPAVACARA_MAGGA} {POS_ALL}')} {NH} "
          f"{B.NANU(f'{RUPAVACARA_MAGGA} {NEG_PE6}')} {AM} "
          f"Nếu {RUPAVACARA_MAGGA} {NEG_PE2}, {B.NO_CA_VATA} “{P_J_RUPA}”.",
          f"{Q(f'{A_J_ANA}, {SO_CA_MAGGO} {POS_PE}')} {AM} {Q(f'{P_J_RUPA}, {SO_CA_MAGGO} {POS_PE}')} {NHP}",
          f"{Q(f'{P_J_RUPA}, {SO_CA_MAGGO} {NEG_PE5}')} {AM} {Q(f'{A_J_ANA}, {SO_CA_MAGGO} {NEG_PE5}')} {NHP}")
    d.seg("5-280",
          f"{Q(PV)} {AM} {Q('đứng vững trong trạng thái A-la-hán')} {NHP}",
          f"{Q(PV)} {AM} {Q(TAYO_MAGGE)} {NHP}",
          f"{Q(TAYO_MAGGE)} {AM} {Q(TINI_PHALANI)} {NHP}",
          f"{Q(TINI_PHALANI)} {AM} {Q(SAMODHANA)} {NHP}",
          f"{Q(PV)} {AM} {Q('bằng ' + SOTAPATTIMAGGA)} {NHP}",
          f"{Q('bằng ' + SAKADAGAMIMAGGA)} {NH} {KATAMENA} Bằng {ANAGAMIMAGGA}. {Q(AM_3)} {NHP}")
    d.head(4, "Phần dẫn kinh", "5-4-2-0")                              # Suttāharaṇakathā
    d.seg("5-281",
          f"{Q(AM_3)} {AM} {B.NANU(VB_SOTA)} {AM} Nếu {VB_SOTA}, {B.NO_CA_VATA} “{AM_3}”. {Q(AM_OL)} {NHP}",
          f"{Q(AM_OL)} {AM} {B.NANU(VB_SAKA)} {AM} Nếu {VB_SAKA}, {B.NO_CA_VATA} “{AM_OL}”.",
          f"{Q(PV)} {AM} {Q('bất cứ ai thấu hiểu Giáo Pháp, tất cả những người ấy, ' + SAHA_ABHISAMAYA + ', đều ' + SANTHATI)} {NHP}",
          f"{B.NA_VATTABBAM_Q(P_J)} {AM} {B.NANU_VUTTAM}",
          f"“Đã có các vị ấy [{B.VAR} ({AN_6_54}): ahiṃsakā] trong thời quá khứ, sáu bậc đạo sư lừng danh;",
          f"{NIRAMAGANDHA} [{B.SPELL} (Sī., Ka.): karuṇādhimuttā], {KAMASAMYOJANA}.",
          f"“{VIRAJETVA};",
          "Các vị ấy có những đệ tử, đến nhiều trăm người.",
          f"“{NIRAMAGANDHA}, {KAMASAMYOJANA};",
          f"{VIRAJETVA}” [{AN_6_54}].",
          f"{B.ATTHEVA} {AM} {B.TENA_HI(P_J)}",
          f"{Q(P_J)} {AM} {B.NANU_VUTTAM} {SUNETTA_PROSE}",
          "“Giới hạnh, định tâm và trí tuệ, cùng sự giải thoát không có điều gì cao hơn;",
          "Những hiện tượng này đã được bậc Cồ-đàm lừng danh hiểu ra.",
          "“Như vậy, Đức Phật, sau khi hiểu biết trực tiếp, đã giảng Giáo Pháp cho các tỳ-khưu;",
          f"Bậc đạo sư, người đi đến tận cùng của khổ đau, bậc có mắt, đã nhập Niết-bàn trọn vẹn” [{AN_7_66}].",
          f"{B.ATTHEVA} {AM} {B.TENA_HI_NA(P_J)}",
          B.KATHA_END.format(x="sự dứt bỏ"))
    return d.text()


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
    (B.OUT_DIR / NAME).write_bytes(text.encode("utf-8"))
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
