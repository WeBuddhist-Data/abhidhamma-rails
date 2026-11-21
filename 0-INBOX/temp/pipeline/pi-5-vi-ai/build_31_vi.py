# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 31: 31-tevisatimavaggo.md (Tevīsatimavaggo, ^5-31-0 … ^5-918),
the kathā (218)-(226) of the twenty-third (last) vagga, its uddāna, the close of the small half-fifty-group, the
uddāna of the fifty-groups and the book end.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_2 / build_10 / build_12 / build_13 / build_15 / build_25 (read-only; importing writes nothing) for
strings shared with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4
Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur
in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against
the Pāli. Every Pāli sentence keeps its own Vietnamese sentence.

run:   python -I -B -X utf8 build_31_vi.py
find:  python -I -B -X utf8 build_31_vi.py --find <regex> …   (Pāli line + Vietnamese line of finished chapters 1-28)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (rāgo doso moho)
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –, CRIMES)
import build_12_vi as C12    # noqa: E402  (Bồ-tát, L10, dukkarakāriyaṃ, aññaṃ satthāraṃ uddisi)
import build_13_vi as C13    # noqa: E402  (Mahāpaṇṇāsako.)
import build_15_vi as C15    # noqa: E402  (hanci_no / nanu_l)
import build_25_vi as C25    # noqa: E402  (yadaniccaṃ taṃ dukkhaṃ, AP2)

NAME = "31-tevisatimavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
VAR, SPELL = B.VAR, B.SPELL
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA23 = B.VAGGA[23]                                     # Tevīsatimavaggo = «Chương thứ hai mươi ba» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte, both times)
hanci_no, nanu_l = C15.hanci_no, C15.nanu_l
NO_CA_VATA = B.NO_CA_VATA
NATTHI = "Không có."                                      # Natthi. (answer, ch11 / ch12 / ch14 / ch28)
SUT_Q = "– có bài kinh như vậy thật không?"               # "…"ti – attheva suttantoti? (ch14, ch28)
SUT_N = "– quả thật không có bài kinh như vậy,"           # Hañci "…"ti – nattheva suttanto, … (new; ch14 «– có bài
# kinh như vậy thật,» for attheva suttanto)

# ================================================================ (218) Ekādhippāya
EK = "với cùng một ý định"                                # ekādhippāyena (terms file heading «cùng một ý định»)
MD = "hành vi dâm dục"                                    # methuno dhammo / methunaṃ dhammaṃ (ch10, ch20)
T1 = f"{EK} thì được phép hưởng thụ {MD}"                 # ekādhippāyena methuno dhammo paṭisevitabbo
NOT4 = ("phải trở thành người không phải sa-môn, phải trở thành người không phải tỳ-khưu, phải trở thành người bị "
        "cắt đứt tận gốc, phải trở thành người phạm tội bị trục xuất")
# assamaṇena hotabbaṃ, abhikkhunā hotabbaṃ, chinnamūlena hotabbaṃ pārājikena hotabbaṃ (samaṇa «sa-môn» pi-2;
# ucchinnamūla «bị cắt đứt tận gốc» ch10; pārājika new; the missing comma before pārājikena rendered as meant)
CR = C10.CRIMES                                           # pāṇo hantabbo … nigamaghātako kātabbo (ch10 list)
T1B = f"{EK} thì được phép {', '.join(CR)}"

# ================================================================ (219) Arahantavaṇṇa
AMV = "những chúng sinh không phải loài người trong hình dạng của các bậc A-la-hán"
# arahantānaṃ vaṇṇena amanussā (amanussa «không phải loài người» ch20; vaṇṇa = appearance, aṭṭhakathā)
T2 = f"{AMV} hưởng thụ {MD}"                              # … methunaṃ dhammaṃ paṭisevanti (ch10, ch20)
T2B = f"{AMV} {CR[0]}… {', '.join(CR[1:-1])}… {CR[-1]}"   # pāṇaṃ hananti…pe… adinnaṃ … gāmaghātakaṃ karonti…pe…

# ================================================================ (220-224) Issariyakāmakārikā
BS = C12.BS                                               # bodhisatto = «Bồ-tát» (ch12)
IK = "vì làm theo ý muốn nhờ quyền uy mà"                 # issariyakāmakārikāhetu (issariya «quyền uy» ch10, ch15)
VIN = "đi đến nơi đọa lạc"                                # vinipātaṃ gacchati (vinipāta «nơi đọa lạc» pi-2)
GAB = "nhập vào bào thai"                                 # gabbhaseyyaṃ okkamati (gabbhaseyyaka «sinh ra từ bào thai»
# pi-2)
DUK = C12.DUKKARA                                         # dukkarakārikaṃ akāsi = «đã làm những việc khổ hạnh khó làm»
TAPA = f"đã làm một khổ hạnh khác [{VAR} (Tương Ưng Bộ Kinh 1.137): amaraṃ tapaṃ]"   # aparantapaṃ akāsi (ch12)
TAPA0 = "đã làm một khổ hạnh khác"                        # (uddāna, without the variant)
SAT = f"đã {C12.OTHER_T}"                                 # aññaṃ satthāraṃ uddisi = «đã tôn xưng một bậc đạo sư khác»
T3V, T3G, T3D, T3S = (f"{BS} {IK} {x}" for x in (VIN, GAB, DUK, SAT))
HELLS = ["địa ngục", "địa ngục Đẳng Hoạt", "địa ngục Hắc Thằng", "địa ngục Thiêu Nhiệt",
         f"địa ngục Đại Thiêu Nhiệt [{VAR} (Sī., Syā., Kaṃ., Pī.): patāpanaṃ]", "địa ngục Chúng Hợp",
         "địa ngục Khiếu Hoán"]
# nirayaṃ, sañjīvaṃ, kālasuttaṃ, tāpanaṃ, mahātāpanaṃ, saṅghātakaṃ, roruvaṃ …pe… avīciṃ (avīci = «địa ngục Vô Gián»
# pi-2; the other names in the same Sino-Vietnamese style, new)
AVICI = "địa ngục Vô Gián"
T3H = f"{BS} {IK} {', '.join('đi đến ' + h for h in HELLS)}… đi đến {AVICI}"
REB = f"{BS} {IK} có thể tái sinh vào địa ngục, có thể tái sinh vào cõi súc sinh"
# nirayaṃ upapajjeyya, tiracchānayoniṃ upapajjeyya (ch20)
IDD = f"{BS} có thần thông"                               # bodhisatto iddhimā (ch21 kappaṭṭho iddhimā)
IP = [f"nền tảng thần thông bằng {x}" for x in ("ý muốn", "tinh tấn", "tâm", "sự thẩm xét")]   # (pi-2, ch21)
IDP = f"{BS} đã tu tập {chain(IP)}"                       # bodhisattena chandiddhipādo bhāvito…pe… vīmaṃsiddhipādo
# bhāvito (ch21 «đã tu tập nền tảng thần thông …»)
V10 = ["thế gian là trường tồn", "thế gian không trường tồn", "thế gian là hữu hạn", "thế gian là vô hạn",
       B.TAM_JIVAM, B.ANNAM_JIVAM, "Như Lai còn tồn tại sau khi chết", "Như Lai không còn tồn tại sau khi chết",
       "Như Lai vừa còn tồn tại vừa không còn tồn tại sau khi chết",
       "Như Lai không phải còn tồn tại cũng không phải không còn tồn tại sau khi chết"]   # (pi-1 ^1 diṭṭhāsava, ch22)
PG = "đã chấp nhận"                                       # paccāgacchi (aṭṭhakathā: gaṇheyya)
VIEWS = (f"{BS} {IK} {PG} “{V10[0]}”, " + chain(f"“{v}”" for v in V10[1:9]) + f"… {PG} “{V10[9]}”")
VIEWS_PE = f"{BS} {IK} {PG} “{V10[0]}”… {PG} “{V10[9]}”"


def sut(t):
    """X-ti? Āmantā. "X"ti – attheva suttantoti? Natthi. Hañci "x"ti – nattheva suttanto, no ca vata re vattabbe – "x"ti."""
    return f"{Q(t)} {AM} “{cap(t)}” {SUT_Q} {NATTHI} Nếu “{t}” {SUT_N} {NO_CA_VATA} “{t}”."


# ================================================================ (225) Patirūpa
R, D, M = C2.R, C2.D, C2.M                                # rāgo, doso, moho (ch2, pi-1)
KIL = "phiền não"                                         # kileso (ch3, ch19)
L10 = C12.L10                                             # phasso … paññā (ch4 / ch12 order = this Pāli's order)


def pr(x):
    """atthi na X X-patirūpako"""
    return f"có cái không phải là {x} nhưng tương tự {x}"


P_R = pr(R)
P_10 = ", ".join(pr(x) for x in L10)
P_10PE = f"{pr(L10[0])}… {pr(L10[-1])}"
P_DMK = ", ".join(pr(x) for x in (D, M, KIL))

# ================================================================ (226) Aparinipphanna
RUPA, ANN = B.RUPA, B.ANNATAVI                            # vật chất / năng lực của người đã hiểu biết trọn vẹn
APN = "không được hình thành trọn vẹn"                    # aparinipphanna (parinipphanna «được hình thành trọn vẹn» ch19)
ANICCA = B.ANICCA                                         # anicca … vipariṇāmadhamma (pi-1, pi-2, sample with «là»)
AP2 = C25.AP2                                             # aniccaṃ saṅkhataṃ…pe… vipariṇāmadhammaṃ (ch25)
NEG = ("không vô thường, không do điều kiện tạo thành, không sinh khởi tùy thuộc vào điều kiện, không có bản chất "
       "diệt tận, không có bản chất suy tàn, không có bản chất phai nhạt, không có bản chất chấm dứt, không có bản chất "
       "biến đổi")                                       # na aniccaṃ … na vipariṇāmadhammaṃ (ch27)
NEG_PE = "không vô thường… không có bản chất biến đổi"    # na aniccaṃ…pe… na vipariṇāmadhammaṃ
DK1 = "chỉ khổ đau mới được hình thành trọn vẹn"          # dukkhaññeva parinipphannaṃ (ch25 «chỉ … mới là khổ đau»)
YAD = C25.YAD                                             # yadaniccaṃ taṃ dukkhaṃ (ch10, ch25)
VY = C25.VY                                               # «Đức Thế Tôn đã nói rằng … [Tương Ưng Bộ Kinh 3.15] –» (ch25)
VY0 = f"Đức Thế Tôn đã nói rằng {YAD} –"                  # the same without the citation (Pāli has none there)
LIST5 = (f"{B.VEDANA}…{B.SANNA}… {B.SANKHARA}… {B.VINNANA}… {B.AYATANA[0]}… {B.AYATANA[-1]}… "
         f"{B.DHATU[0]}… {B.DHATU[-1]}… {B.INDRIYA[0]}… {ANN}")
# Vedanā …pe… saññā… saṅkhārā… viññāṇaṃ… cakkhāyatanaṃ…pe… dhammāyatanaṃ… cakkhudhātu… dhammadhātu…
# cakkhundriyaṃ…pe… aññātāvindriyaṃ (pi-2 names, sample lists)


def dk_line(x, cite):
    """Dukkhaññeva parinipphannanti? Āmantā. Nanu yadaniccaṃ taṃ dukkhaṃ vuttaṃ bhagavatā – "X anicca"nti? Āmantā.
    Hañci yadaniccaṃ taṃ dukkhaṃ vuttaṃ bhagavatā – "X aniccaṃ", no ca vata re vattabbe – "dukkhaññeva …"ti."""
    return (f"{Q(DK1)} {AM} Chẳng phải {VY if cite else VY0} “{x} là vô thường” sao? {AM} "
            f"Nếu {VY0} “{x} là vô thường”, {NO_CA_VATA} “{DK1}”")


# ================================================================ kathā names, uddāna, fifty-groups, book end
KX = {1: "cùng một ý định",                               # Ekādhippāyakathā (terms file)
      2: "hình dạng của các bậc A-la-hán",                # Arahantavaṇṇakathā
      3: "việc làm theo ý muốn nhờ quyền uy",             # Issariyakāmakārikākathā (closing line)
      4: "cái tương tự",                                  # Patirūpakathā
      5: "những gì không được hình thành trọn vẹn"}       # Aparinipphannakathā
H3 = f"{KX[3]} và các mục khác"                           # Issariyakāmakārikādikathā (ādi «các mục khác» pi-3)
NUMS = {1: "(218) 1.", 2: "(219) 2.", 3: "(220-4) 3-7.", 4: "(225) 8.", 5: "(226) 9."}


def heads(n):
    """#### Tevīsatimavaggo ^5-31-n-0 / ##### (nnn) n. <title> ^5-31-n-1-0"""
    return [(4, VAGGA23, f"5-31-{n}-0"), (5, f"{NUMS[n]} {K(x=H3 if n == 3 else KX[n])}", f"5-31-{n}-1-0")]


UDDANA = (f"{cap(EK)} thì được phép hưởng thụ {MD}, {T2}, {T3V}, {GAB}, {DUK}, {TAPA0}, {SAT}, "
          f"{', '.join(pr(x) for x in (R, D, M, KIL))}, {RUPA} {APN}, {ANN} {APN}.")
# Ekādhippāyena methuno dhammo paṭisevitabbo, … atthi na rāgo rāgapatirūpako atthi na doso … (no commas between
# the four patirūpaka items: rendered as meant), rūpaṃ aparinipphannaṃ aññātāvindriyaṃ aparinipphannanti.
KHUDDAKO = "Nhóm nửa năm mươi nhỏ."                       # Khuddako aḍḍhapaṇṇāsako. (ch13 «Nhóm năm mươi lớn.» pattern)
UDD_H = "Điều mới, sự nhập Niết-bàn, cùng một ý định."     # Navaṃ, nibbuti, ekādhippāyoti. (first kathā of vaggas
# 21-23: sāsanaṃ navaṃ kataṃ ch29, parinibbāna ch30, ekādhippāya here)
PANNASAKUDDANAM = "Tóm tắt của các nhóm năm mươi –"       # Paṇṇāsakuddānaṃ – (ch13 «Tóm tắt của nhóm năm mươi này nữa –»)
BOOK = B.BOOK_TITLE                                       # «Các vấn đề tranh luận»
VERSE = ["Nhóm lớn, sự cố định, các khuynh hướng tiềm ẩn, sự chế ngự, nhóm nhỏ là thứ năm;",
         "Nghiền nát các học thuyết của người khác, được thiết lập vững chắc trên gốc rễ là kinh;",
         f"Soi sáng giáo thuyết của bậc đạo sư, trong bộ “{BOOK}”."]
# Mahāniyāmo, anusayā, niggaho, khuddakapañcamo; / Parappavādamaddanā, suttamūlasamāhitā; / Ujjotanā satthusamaye,
# kathāvatthupakaraṇeti. (the five fifty-groups by their first kathā: mahā(paṇṇāsaka) ch13, niyāma ch14, anusaya
# ch19 / ch23, niggaha ch24 / ch28, khuddaka; parappavāda ch28; satthā «bậc đạo sư» pi-4; book title in “…” as the
# pi-1..4 book ends)
BHANAVARA = "Gồm ba mươi lăm phần tụng đọc"               # Pañcattiṃsabhāṇavāraṃ (bhāṇavāra «phần tụng đọc» pi-1; no
# full stop, as the Pāli)
BOOK_END = f"Bộ “{BOOK}” đã hoàn tất."                     # Kathāvatthupakaraṇaṃ niṭṭhitaṃ. (pi-1..4 «Bộ “…” đã hoàn tất.»)


def build():
    d = B.Doc()
    d.head(3, VAGGA23, "5-31-0")
    # ------------------------------------------------------------ (218) Ekādhippāya
    d.head(4, f"{NUMS[1]} {K(x=KX[1])}", "5-31-1-0")
    d.seg("5-908",
          f"{Q(T1)} {AM} {Q(f'{EK} thì {NOT4}')} {NHP} {q(T1)} {AM} {Q(T1B)} {NHP}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (219) Arahantavaṇṇa
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-909",
          f"{Q(T2)} {AM} {Q(T2B)} {NHP}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (220-224) Issariyakāmakārikā
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-910",
          f"{Q(T3V)} {AM} {Q(T3H)} {NHP}",
          sut(T3V))
    d.seg("5-911",
          f"{Q(T3G)} {AM} {Q(REB)} {NHP}",
          f"{Q(T3G)} {AM} {Q(IDD)} {NHP} {q(IDD)} {AM} {Q(IDP)} {NHP}",
          sut(T3G))
    d.seg("5-912",
          f"{Q(T3D)} {AM} {Q(VIEWS)} {NHP}",
          sut(T3D))
    d.seg("5-913",
          f"{Q(f'{BS} {IK} {TAPA}, {SAT}')} {AM} {Q(VIEWS_PE)} {NHP}")
    d.seg("5-914",
          sut(T3S),
          E(x=KX[3]))
    # ------------------------------------------------------------ (225) Patirūpa
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-915", f"{Q(P_R)} {AM} {Q(P_10)} {NHP}")
    d.seg("5-916",
          f"{Q(P_DMK)} {AM} {Q(P_10PE)} {NHP}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (226) Aparinipphanna
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    t5 = f"{RUPA} {APN}"
    d.seg("5-917",
          f"{Q(t5)} {AM} {Q(f'{RUPA} {NEG}')} {NHP} {nanu_l(f'{RUPA} là {ANICCA}')} {AM} "
          f"{hanci_no(f'{RUPA} là {AP2}', t5)}",
          f"{dk_line(RUPA, True)}…")
    t6 = f"{ANN} {APN}"
    d.seg("5-918",
          f"Có phải {LIST5} {APN} không? {AM} {Q(f'{ANN} {NEG_PE}')} {NHP} {nanu_l(f'{ANN} là {AP2}')} {AM} "
          f"{hanci_no(f'{ANN} là {ANICCA}', t6)}",
          f"{dk_line(ANN, False)}.",
          E(x=KX[5]),
          f"{VAGGA23}.",
          TASSUDDANAM,
          UDDANA,
          KHUDDAKO,
          TASSUDDANAM,
          UDD_H,
          PANNASAKUDDANAM,
          *VERSE,
          BHANAVARA,
          BOOK_END)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("nơi đọa lạc", 2), (AVICI, 2), ("cõi súc sinh", 2), ("sinh ra từ bào thai", 2), (", ".join(IP), 2),
    ("sa-môn", 2), ("tỳ-khưu", 2), ("Thế gian là trường tồn", 1), ("Thế gian không trường tồn", 1),
    ("Thế gian là hữu hạn", 1), ("Thế gian là vô hạn", 1), *[(v, 1) for v in V10[6:]],
    ("khổ hạnh khó làm", 4), ("bậc đạo sư", 4), ("Phần tụng đọc thứ nhất", 1),
    ("Bộ “Liệt kê các hiện tượng” đã hoàn tất.", 1), ("Bộ “Phân tích các hiện tượng” đã hoàn tất.", 2),
    ("Bộ “Thảo luận về các yếu tố” đã hoàn tất.", 3), ("Bộ “Định danh các hạng người” đã hoàn tất.", 4),
    ("các mục khác", 3), ("chư thiên Tha Hóa Tự Tại", 2),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (", ".join(CR), "10-dutiyavaggo.md"), (f"hưởng thụ {MD}", "10-dutiyavaggo.md"),
    (f"hưởng thụ {MD} với người nữ không phải loài người", "20-dvadasamavaggo.md"),
    ("đã bị cắt đứt tận gốc", "10-dutiyavaggo.md"), ("hạnh phúc do quyền uy", "10-dutiyavaggo.md"),
    ("nghiệp dẫn đến quyền uy", "15-sattamavaggo.md"),
    ("có thể tái sinh vào địa ngục, có thể tái sinh vào cõi súc sinh", "20-dvadasamavaggo.md"),
    (f"{BS} {DUK}", "12-catutthavaggo.md"), (f"{BS} {TAPA}, {SAT}", "12-catutthavaggo.md"),
    ("có thần thông không?", "21-terasamavaggo.md"),
    (", ".join("đã tu tập " + x for x in IP), "21-terasamavaggo.md"),
    *[(f"‘{v}’", "22-cuddasamavaggo.md") for v in V10[1:9]],
    (f"” {SUT_Q} {NATTHI} “", "14-chatthavaggo.md"), (f"” – có bài kinh như vậy thật, {NO_CA_VATA} “", "14-chatthavaggo.md"),
    (R, "2-parihanikatha.md"), (D, "2-parihanikatha.md"), (M, "2-parihanikatha.md"), (KIL, "19-ekadasamavaggo.md"),
    (f"{L10[0]}, " + ", ".join("bốn " + x for x in L10[1:]), "12-catutthavaggo.md"),
    ("được hình thành trọn vẹn", "19-ekadasamavaggo.md"), (f"Có phải {RUPA} là {ANICCA}", "1-puggalakatha.md"),
    (NEG, "27-ekunavisatimavaggo.md"), (f"Chẳng phải {VY} “", "25-sattarasamavaggo.md"),
    (f"Nếu {VY} ", "25-sattarasamavaggo.md"), ("mới là khổ đau", "25-sattarasamavaggo.md"),
    (f"là {AP2}", "25-sattarasamavaggo.md"),
    (C13.MAHAPANNASAKO, "13-pancamavaggo.md"), ("Nhóm năm mươi thứ ba.", "23-pannarasamavaggo.md"),
    ("Tóm tắt của nhóm năm mươi này nữa –", "13-pancamavaggo.md"), (TASSUDDANAM, "10-dutiyavaggo.md"),
    ("Bàn về sự cố định", "14-chatthavaggo.md"), ("Các khuynh hướng tiềm ẩn, sự phòng hộ", "23-pannarasamavaggo.md"),
    ("Sự chế ngự, sự tích lũy phước", "28-visatimavaggo.md"),
    ("Các học thuyết của người khác trống rỗng", "28-visatimavaggo.md"),
    ("và sự giải thoát là thứ năm.", "13-pancamavaggo.md"), (KHUDDAKO.replace("nửa ", "").replace("nhỏ", "lớn"),
                                                            "13-pancamavaggo.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(st, f"pi-{b}") for st, b in CROSS if st not in texts[b]]
    cache = {}
    for st, f in PI5:
        if f not in cache:
            cache[f] = (B.OUT_DIR / f).read_text(encoding="utf-8")
        if st not in cache[f]:
            missing.append((st, f))
    for st, w in missing:
        print(f"CROSS MISSING in {w}: {st}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch31 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


def find(pats, maxhits=3, maxc=700):
    names = [f.name for f in sorted(B.PALI_DIR.glob("*.md")) if not re.match(r"(29|30|31)-", f.name)]
    for pat in pats:
        rx = re.compile(pat)
        hits = 0
        for n in names:
            if not (B.OUT_DIR / n).exists():
                continue
            pl = [x for x in (B.PALI_DIR / n).read_text(encoding="utf-8").splitlines() if x.strip()]
            vl = [x for x in (B.OUT_DIR / n).read_text(encoding="utf-8").splitlines() if x.strip()]
            for i, ln in enumerate(pl):
                m = rx.search(ln)
                if m and hits < maxhits:
                    hits += 1
                    s = max(0, m.start() - 80)
                    print(f"== {pat} [{n} {i + 1}]\n PI: {ln[s:s + 300]}\n VI: {vl[i][:maxc] if i < len(vl) else '-'}")
        if not hits:
            print(f"== {pat}: no hit")


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    # The two book-title lines carry “…” as the pi-1..4 book ends do (the Pāli has no quotes there): expected.
    vl = [ln for ln in text.splitlines() if ln.strip()]
    title_lines = [i for i, ln in enumerate(vl, 1) if f"“{BOOK}”" in ln]
    assert len(title_lines) == 2, title_lines
    expected = {f"{NAME} line {i}: quotes pali (0, 0) vs vi (2, 0)" for i in title_lines}
    assert expected <= set(probs), "title-line quote exception not as expected"
    probs = [p for p in probs if p not in expected]
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text and "chánh niệm" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len(vl)} lines; odd closing order repaired: {len(repaired)}; "
          f"line checks: OK (title-line quotes: lines {title_lines})")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--find":
        find(sys.argv[2:])
    else:
        main()
