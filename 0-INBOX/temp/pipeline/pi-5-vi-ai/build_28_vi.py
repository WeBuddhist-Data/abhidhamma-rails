# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 28: 28-visatimavaggo.md (Vīsatimavaggo, ^5-28-0 … ^5-877),
the six kathā (194)-(199) of the twentieth vagga, its uddāna and the close of the fourth fifty-group.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_4 / build_10 / build_12 / build_15 / build_21 (read-only; importing writes nothing) for strings
shared with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4 Vietnamese
rails is asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur in that
chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli.
Every Pāli sentence keeps its own Vietnamese sentence.

run:   python -I -B -X utf8 build_28_vi.py
find:  python -I -B -X utf8 build_28_vi.py --find <regex> …   (Pāli line + Vietnamese line of finished chapters 1-25)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as C4      # noqa: E402  (magga names)
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –, KILLERS, jhāna / arūpa names)
import build_12_vi as C12    # noqa: E402  (dhammacakka passage pieces, CIVARA, MG_AR)
import build_15_vi as C15    # noqa: E402  (hanci_no / hanci_yes / nanu_l, GIL)
import build_21_vi as C21    # noqa: E402  (āpāyiko nerayiko verse)

NAME = "28-visatimavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA, ATTHEVA, NANU_VUTTAM = (B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA, B.ATTHEVA,
                                                   B.NANU_VUTTAM)
VAR, SPELL = B.VAR, B.SPELL
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA20 = B.VAGGA[20]                                     # Vīsatimavaggo = «Chương thứ hai mươi» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
hanci_no, hanci_yes, nanu_l = C15.hanci_no, C15.hanci_yes, C15.nanu_l
NATTHI = "Không có."                                      # Natthi. (answer, ch11 / ch12 / ch14)
SUT_Q = "– có bài kinh như vậy thật không?"               # "…"ti – attheva suttantoti? (ch14, ch23)
SUT_S = "– có bài kinh như vậy thật,"                     # Hañci "…"ti – attheva suttanto, … (ch14)

# ================================================================ (194) Asañcicca
ANT = "người tạo nghiệp có quả không gián đoạn"           # ānantariko (ch16 ānantariyo puggalo; pi-1 ānantarika)
AS, SA = "không cố ý", "cố ý"                             # asañcicca / sañcicca (ch20)
MV = "tước đoạt mạng sống của mẹ"                         # mātaraṃ jīvitā voropetvā (pi-2, ch20)


def who(how, act, res, neg=False):
    """(A)sañcicca X-tvā Y hoti / na hoti = người (không) cố ý X (không) trở thành Y"""
    return f"người {how} {act} {'không ' if neg else ''}trở thành {res}"


A1, A1N = who(AS, MV, ANT), who(AS, MV, ANT, True)
S1 = who(SA, MV, ANT)
PANA = "sát hại sinh mạng"                                # pāṇaṃ hantvā / pāṇātipātī (ch10 CRIMES, pi-4)
P1, P1N = who(AS, PANA, f"người {PANA}"), who(AS, PANA, f"người {PANA}", True)
M_ACT = "lấy của không được cho… nói dối"                 # adinnaṃ ādiyitvā…pe… musā bhaṇitvā (pi-4)
M1, M1N = who(AS, M_ACT, "người nói dối"), who(AS, M_ACT, "người nói dối", True)   # musāvādī (pi-4)
KILLERS = C10.KILLERS                                     # kẻ giết mẹ … kẻ chia rẽ Tăng đoàn (ch10)
DONE = ["mẹ bị tước đoạt mạng sống", "cha bị tước đoạt mạng sống", "bậc A-la-hán bị tước đoạt mạng sống",
        "máu của Như Lai bị làm cho chảy"]
# mātā jīvitā voropitā … tathāgatassa lohitaṃ uppāditaṃ (pi-2 ^2-U55, here without duṭṭhena cittena)
SB = KILLERS[4]


def ant(x):
    """X ānantariko"""
    return f"{x} là {ANT}"


ALL_SB = f"tất cả những {SB} đều là {ANT}"                # sabbe saṅghabhedakā ānantarikā
DSB = f"{SB} với tri giác rằng đó là Giáo Pháp"           # dhammasaññī saṅghabhedako (saññā «tri giác» core)
UP, up = "Này Ưu-ba-li", "này Ưu-ba-li"                   # (atthi) upāli
UPALI = (f"{UP}, có {SB} thuộc cõi khổ, thuộc địa ngục, là người tồn tại suốt một kiếp, không thể cứu chữa; "
         f"{up}, có {SB} không thuộc cõi khổ, không thuộc địa ngục, không phải là người tồn tại suốt một kiếp, "
         "không phải không thể cứu chữa")
# atthupāli, saṅghabhedako āpāyiko nerayiko kappaṭṭho atekiccho; atthupāli, … na atekiccho (ch21 verse words)
V21_VAR = f" [{VAR} (Sī., Ka.): bhinditvā]"
VERSE1 = [ln.replace(V21_VAR, "") for ln in C21.VERSE]   # ch21 verse; here bhetvāna has no variant

# ================================================================ (195) Ñāṇa
PJ = "người phàm phu"                                     # puthujjano (pi-1, ch10)
NA = "hiểu biết"                                          # ñāṇa (ch19 Ñāṇakathā «Bàn về hiểu biết»)
T2, T2P = f"{PJ} không có {NA}", f"{PJ} có {NA}"          # (n)atthi puthujjanassa ñāṇaṃ (ch10 «X có Y»)
PL = ("trí tuệ, sự hiểu rõ, sự tìm hiểu, sự tìm hiểu kỹ, sự tìm hiểu các hiện tượng, sự nhận xét, sự nhận diện, "
      "sự nhận diện chính xác")                          # paññā pajānanā … paccupalakkhaṇā (pi-1 ^1-16)
PL_PE = "trí tuệ, sự hiểu rõ, sự tìm hiểu… sự nhận diện chính xác"
J, ARU = C10.J, C10.ARU                                   # tầng thiền thứ nhất … / lĩnh vực không gian vô tận … (ch10)
SAMAP = "có thể nhập"                                     # samāpajjeyya (ch13)
CIV, GIL = C12.CIVARA, C15.GIL
GIVE = (f"có thể thực hiện sự bố thí… có thể cho {CIV}, có thể cho đồ ăn khất thực, có thể cho chỗ ở, "
        f"có thể cho {GIL}")                              # dānaṃ dadeyya …pe… cīvaraṃ dadeyya … (ch21, ch25)
FOUR = "hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, tu tập con đường"
# dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti (ch12)

# ================================================================ (196) Nirayapāla
NP = "kẻ canh giữ địa ngục"                               # nirayapāla (new)
NIR = "trong các địa ngục"                                # nirayesu
T3, T3P = f"{NIR} không có {NP}", f"{NIR} có {NP}"
KK = "các hình phạt"                                      # kammakāraṇā (aṭṭhakathā: kāraṇā)
KR = "những người thi hành hình phạt"                     # kāraṇikā (here: those who inflict the punishments)
MAN = "giữa loài người"                                   # manussesu (ch11)
VERSE3 = ["“Không phải Tỳ-xá-phù, cũng không phải vua của loài ngạ quỷ,",
          "Soma, Yama, và vua Tỳ-sa-môn;",
          f"Chính các nghiệp của mình đánh đập ở đó, người bị đẩy đi khỏi đây [{SPELL} (Syā., Ka.): paṇuṇṇaṃ; "
          "(Sī.): panunnaṃ], đã đến thế gian khác”."]
# Na vessabhū nopi ca pettirājā, / Somo yamo vessavaṇo ca rājā; / Sakāni kammāni hananti tattha, ito paṇunnaṃ …
# paralokapatta"nti. (vessabhū: a deva, aṭṭhakathā; pettirājā: chief of the petas; paro loko «thế gian khác» pi-1)
NPS = f"này các tỳ-khưu, những {NP}"                      # tamenaṃ, bhikkhave, nirayapālā
BURN = "đang bốc cháy, rực lửa, cháy sáng"               # ādittā sampajjalitā sajotibhūtā (āditta ch10)
PAIN = "cảm nhận những cảm giác khó chịu, dữ dội, cay đắng"   # dukkhā tibbā kaṭukā vedanā vedeti / vedayati
DIE = "người ấy không qua đời chừng nào nghiệp xấu ác ấy chưa chấm dứt"
# na ca tāva kālaṃ karoti yāva na taṃ pāpakammaṃ byantīhoti (kālaṃ karoti ch18; byantībhāva ch20)
CITE3 = "[Trung Bộ Kinh 3.250; Tăng Chi Bộ Kinh 3.36]"
SUT3A = (f"{cap(NPS)} bắt người ấy chịu hình phạt gọi là sự trói buộc năm cách [{VAR} (Trung Bộ Kinh 3.250; "
         "Tăng Chi Bộ Kinh 3.36): karonti] – chúng đóng một cây cọc sắt nung đỏ vào một bàn tay, đóng một cây cọc "
         "sắt nung đỏ vào bàn tay thứ hai, đóng một cây cọc sắt nung đỏ vào một bàn chân, đóng một cây cọc sắt nung "
         f"đỏ vào bàn chân thứ hai, đóng một cây cọc sắt nung đỏ vào giữa ngực; ở đó người ấy {PAIN}; và {DIE}")
SUT3B = (f"{cap(NPS)} đặt người ấy nằm xuống rồi đẽo bằng búa [{SPELL} (tất cả các bản): kudhārīhi]… "
         f"{NPS} dựng người ấy chân lên trên, đầu xuống dưới rồi đẽo bằng rìu… "
         f"{NPS} buộc người ấy vào xe rồi bắt chạy tới, chạy lui trên mặt đất {BURN} "
         f"[{SPELL} (Syā.): sañjotibhūtāya]… "
         f"{NPS} bắt người ấy leo lên và leo xuống một ngọn núi than hồng lớn {BURN}… "
         f"{NPS} nắm người ấy chân lên trên, đầu xuống dưới rồi ném vào một vạc đồng nung nóng {BURN}. "
         "Ở đó người ấy bị nấu sôi sùng sục bọt, ở đó, trong khi bị nấu sôi sùng sục bọt, người ấy có lúc đi lên "
         "trên, có lúc đi xuống dưới, có lúc đi ngang. "
         f"Ở đó người ấy {PAIN}, và {DIE}. "
         f"{cap(NPS)} ném người ấy vào đại địa ngục! "
         "Và này các tỳ-khưu, đại địa ngục ấy –")
VERSE3B = ["“Có bốn góc, có bốn cửa, được phân chia, được đo theo từng phần;",
           "Có tường sắt bao quanh, được che phủ bằng sắt.",
           "“Nền của nó làm bằng sắt, rực cháy, đầy sức nóng;",
           "Tỏa ra khắp mọi phía một trăm do-tuần, luôn luôn tồn tại” "
           "[Trung Bộ Kinh 3.250; Tăng Chi Bộ Kinh 3.36; Ngạ Quỷ Sự 71]."]
# Catukkaṇṇo catudvāro … sabbadā"ti [ma. ni. 3.250; a. ni. 3.36; pe. va. 71] (pe. va. «Ngạ Quỷ Sự» ch15)

# ================================================================ (197) Tiracchāna
TG = "loài súc sinh"                                      # tiracchānagatā (pi-2)
DEV = "giữa chư thiên"                                    # devesu (ch11)
T4, T4N = f"{DEV} có {TG}", f"{DEV} không có {TG}"
BUGS = (f"ở đó có sâu bọ, châu chấu, muỗi, ruồi, rắn, bọ cạp, rết, giun đất [{SPELL} (Syā., Kaṃ., Pī.): "
        "gaṇḍupādāti]")                                  # kīṭā paṭaṅgā makasā makkhikā ahī vicchikā satapadī gaṇḍuppādā
ER = "ở đó có con voi chúa tên là Ê-ra-va-na, cỗ xe cõi trời được thắng một nghìn con"
# erāvaṇo nāma hatthināgo sahassayuttaṃ dibbaṃ yānaṃ (dibba «cõi trời» sample)
KEEP = (f"ở đó có những người giữ voi, những người giữ ngựa [{VAR} (?): hatthibhaṇḍā assabhaṇḍā], những người "
        "cung cấp cỏ, những người huấn luyện, những người nấu thức ăn")
# hatthibandhā assabandhā yāvasikā kāraṇikā bhattakārakā (aṭṭhakathā: yavassa dāyakā; hatthācariyādayo;
# bhattarandhakā)

# ================================================================ (198) Magga
MG5 = "con đường gồm năm chi phần"                        # pañcaṅgiko maggo (pi-1 ^1-89)
MG8 = "con đường gồm tám chi phần"                        # aṭṭhaṅgiko maggo (pi-1)
AMG8 = "con đường cao quý gồm tám chi phần"               # ariyo aṭṭhaṅgiko maggo (pi-2 ^2-U26)
S = B.SAMMA                                               # quan điểm đúng đắn … định tâm đúng đắn (pi-1, pi-2)
VB8 = f"Đức Thế Tôn đã nói rằng {MG8}, cụ thể là – {S[0]}… {S[7]}"
# aṭṭhaṅgiko maggo vutto bhagavatā, seyyathidaṃ – sammādiṭṭhi…pe… sammāsamādhi (ch16 «Đức Thế Tôn đã nói rằng …»)
MGA = "chi phần của con đường"                            # maggaṅgaṃ (pi-1)


def mg(x, neg):
    """X maggaṅgaṃ, sā / so ca (na) maggo (ch8 «và nó không phải là», ch23 «và nó là»)"""
    return f"{x} là {MGA}, và nó {'không phải là' if neg else 'là'} con đường"


S1235 = chain([S[1], S[5], S[6], S[7]])                   # sammāsaṅkappo…pe… sammāvāyāmo…pe… sammāsati…pe… sammāsamādhi
S34 = f"{S[3]}… {S[4]}"                                   # sammākammanto…pe… sammāājīvo
S234 = chain([S[2], S[3], S[4]])
DHP = ["“Tối thắng trong các con đường là con đường gồm tám chi phần, trong các sự thật là bốn câu;",
       "Tối thắng trong các hiện tượng là sự lìa tham, và giữa loài hai chân là bậc có mắt” "
       "[Kinh Pháp Cú 273, trong Kinh Pháp Cú]."]
# Maggānaṃ aṭṭhaṅgiko seṭṭho, saccānaṃ caturo padā; / Virāgo seṭṭho dhammānaṃ, dvipadānañca cakkhumā
# (seṭṭho once per line as the Pāli; dvipadānaṃ ch25; dha. pa. … dhammapade ch10)
PUB = (f"Ngay từ trước, nghiệp bằng thân, nghiệp bằng lời nói, sinh kế của người ấy đã hoàn toàn thanh tịnh; như "
       f"vậy, {AMG8} này của người ấy đi đến sự viên mãn của sự tu tập")
# pubbeva kho panassa kāyakammaṃ vacīkammaṃ ājīvo suparisuddho hoti; evamassāyaṃ … bhāvanāpāripūriṃ gacchati
SU, su = "Này Subhadda", "này Subhadda"                   # subhadda (ASCII name kept, as Seniya / Sakka)
DV = "Giáo Pháp và Giới Luật"                             # dhammavinaya (pi-2, ch10)
SUB = (f"{SU}, trong {DV} nào mà {AMG8} không được tìm thấy, thì ở đó sa-môn cũng không được tìm thấy, ở đó "
       "sa-môn thứ hai cũng không được tìm thấy, ở đó sa-môn thứ ba cũng không được tìm thấy, ở đó sa-môn thứ tư "
       f"cũng không được tìm thấy. Và {su}, trong {DV} nào mà {AMG8} được tìm thấy, thì ở đó sa-môn cũng được tìm "
       "thấy, sa-môn thứ hai cũng… sa-môn thứ ba cũng… ở đó sa-môn thứ tư cũng được tìm thấy. "
       f"{SU}, trong {DV} này, {AMG8} được tìm thấy. {SU}, chính ở đây có sa-môn, ở đây có sa-môn thứ hai, ở đây "
       "có sa-môn thứ ba, ở đây có sa-môn thứ tư. Các học thuyết của người khác trống rỗng, không có các sa-môn khác")
# yasmiṃ kho, subhadda, dhammavinaye … suññā parappavādā samaṇebhi aññehi (samaṇa «sa-môn» pi-2; suñña sample)

# ================================================================ (199) Ñāṇa (twelve)
T6 = f"{NA} có mười hai chủ đề là vượt thế gian"          # dvādasavatthukaṃ ñāṇaṃ lokuttaraṃ (pi-2 dasavatthukā «có
# mười chủ đề»; lokuttara predicate «là vượt thế gian» ch23)
LN12 = f"có mười hai {NA} vượt thế gian"                   # dvādasa lokuttarañāṇāni (ch14 «có mười hai X»)
SOM, SOP = C4.SOTAPATTIMAGGA, "thành quả vào dòng"        # sotāpattimaggā / sotāpattiphalāni (pi-2, ch10)
SAM, ANM, ARM = C4.SAKADAGAMIMAGGA, C4.ANAGAMIMAGGA, C12.MG_AR
ARP = "thành quả A-la-hán"                                # arahattaphalāni (ch10)
ME, ROSE, ROSE_PE = C12.ME, C12.ROSE, C12.ROSE_PE
AS1, AS2, AS3, AS4 = C12.AS1, C12.AS2, C12.AS3, C12.AS4
DC = (f"“Đây là {AS1}”, {ME}, {ROSE}. ‘Và {AS1} này cần được hiểu biết trọn vẹn’, {ME}… "
      f"đã được hiểu biết trọn vẹn, {ME}… ‘đây là {AS2} [{SPELL} (Syā., Kaṃ., Pī.): dukkhasamudayo]’, {ME}… "
      f"‘và {AS2} này cần dứt bỏ’, {ME}… đã được dứt bỏ, {ME}… ‘đây là {AS3} [{SPELL} (Syā., Kaṃ., Pī.): "
      f"dukkhanirodhā]’, {ME}… ‘và {AS3} này cần được tự mình chứng nghiệm’, {ME}… đã được tự mình chứng nghiệm, "
      f"{ME}… ‘đây là {AS4}’, {ME}… ‘và {AS4} này cần được tu tập’, {ME}… đã được tu tập, {ME}, {ROSE_PE}” "
      "[Đại Phẩm 15; Tương Ưng Bộ Kinh 5.1081; Phân Tích Đạo 2.30]!")
# ch12 ^5-? wording; here the first statement is closed with " (no outer quote level), as the Pāli

# ================================================================ kathā names, uddāna, fifty-group
KX = {1: "việc không cố ý",                               # Asañciccakathā (terms file)
      2: NA,                                              # Ñāṇakathā (ch19)
      3: f"những {NP}",                                   # Nirayapālakathā
      4: TG,                                              # Tiracchānakathā
      5: "con đường",                                     # Maggakathā
      6: NA}                                              # Ñāṇakathā (as (195))


def heads(n):
    """#### Vīsatimavaggo ^5-28-n-0 / ##### (193+n) n. <title> ^5-28-n-1-0"""
    return [(4, VAGGA20, f"5-28-{n}-0"), (5, f"({193 + n}) {n}. {K(x=KX[n])}", f"5-28-{n}-1-0")]


UDDANA = (", ".join([cap(ant(KILLERS[0]))] + [ant(k) for k in KILLERS[1:]])
          + f", {T2}, {T3}, {T4}, {MG5}, {T6}.")
# Mātughātako ānantariko pitughātako ānantariko … saṅghabhedako ānantariko, natthi puthujjanassa ñāṇaṃ, …
CATUTTHO_PANNASAKO = "Nhóm năm mươi thứ tư."              # Catuttho paṇṇāsako. (coordinator pattern)
UDDANA50 = f"Sự chế ngự, sự tích lũy phước, đã ở lại, với quá khứ, và {KILLERS[0]}."
# Niggaho, puññasañcayo, aṭṭhāsi, atītena ca mātughātako. (first kathā of vaggas 16-20: ch24 niggaha «sự chế ngự»,
# ch25 puññūpacaya «sự tích lũy phước», ch26 aṭṭhāsi, ch27 atīte kilese, mātughātaka ch10; ca = và as ch23)


def build():
    d = B.Doc()
    d.head(3, VAGGA20, "5-28-0")
    # ------------------------------------------------------------ (194) Asañcicca
    d.head(4, f"(194) 1. {K(x=KX[1])}", "5-28-1-0")
    d.seg("5-857",
          f"{Q(A1)} {AM} {Q(P1)} {NHP} {q(A1)} {AM} {Q(M1)} {NHP}",
          f"{Q(P1N)} {AM} {Q(A1N)} {NHP} {q(M1N)} {AM} {Q(A1N)} {NHP}")
    d.seg("5-858",
          f"{Q(A1)} {AM} “{cap(A1)}” {SUT_Q} {NATTHI} “{cap(S1)}” {SUT_Q} {AM} "
          f"Nếu “{S1}” {SUT_S} {B.NO_CA_VATA} “{A1}”.")
    d.seg("5-859", *[f"{NVQ(ant(k))} {AM} {NANU(v)} {AM} {hanci_yes(v, ant(k))}"
                     for k, v in zip(KILLERS[:4], DONE)])
    d.seg("5-860", f"{Q(ant(SB))} {AM} {Q(ALL_SB)} {NHP} {q(ALL_SB)} {AM} {Q(ant(DSB))} {NHP}")
    d.seg("5-861", f"{Q(ant(DSB))} {AM} {NANU_VUTTAM} “{UPALI}”! {ATTHEVA} {AM} {TENA_HI_NA(ant(DSB))}")
    d.seg("5-862",
          f"{NVQ(ant(DSB))} {AM} {NANU_VUTTAM}",
          *VERSE1,
          f"{ATTHEVA} {AM} {TENA_HI(ant(SB))}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (195) Ñāṇa
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    pl_pe = f"{PJ} có {PL_PE}"
    d.seg("5-863",
          f"{Q(T2)} {AM} {Q(f'{PJ} không có {PL}')} {NHP} {nanu_l(pl_pe)} {AM} {hanci_no(pl_pe, T2)}")
    j1 = f"{PJ} {SAMAP} {J[0]}"
    d.seg("5-864",
          f"{Q(T2)} {AM} {Q(j1)} {AM} {hanci_no(j1, T2)}",
          f"{Q(f'{PJ} {SAMAP} {chain(J[1:])}… {ARU[0]}, {SAMAP} {ARU[1]}, {ARU[2]}, {ARU[3]}, {PJ} {GIVE}')} {AM} "
          f"Nếu {PJ} có thể cho {GIL}, {B.NO_CA_VATA} {T2}”.")
    d.seg("5-865",
          f"{Q(T2P)} {AM} {Q(f'{PJ} nhờ {NA} ấy mà {FOUR}')} {NHP}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (196) Nirayapāla
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-866",
          f"{Q(T3)} {AM} {Q(f'{NIR} không có {KK}')} {NHP} {q(f'{NIR} có {KK}')} {AM} {Q(T3P)} {NHP}",
          f"{Q(f'{MAN} có {KK}, và có {KR}')} {AM} {Q(f'{NIR} có {KK}, và có {KR}')} {NHP} "
          f"{q(f'{NIR} có {KK}, và không có {KR}')} {AM} {Q(f'{MAN} có {KK}, và không có {KR}')} {NHP}")
    d.seg("5-867",
          f"{Q(T3P)} {AM} {NANU_VUTTAM}",
          *VERSE3,
          f"{ATTHEVA} {AM} {TENA_HI(T3)}")
    d.seg("5-868",
          f"{Q(T3)} {AM} {NANU_VUTTAM} “{SUT3A}” {CITE3}! {ATTHEVA} {AM} {TENA_HI(T3P)}",
          f"{Q(T3)} {AM} {NANU_VUTTAM} “{SUT3B}",
          *VERSE3B,
          f"{ATTHEVA} {AM} {TENA_HI(T3P)}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (197) Tiracchāna
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-869",
          f"{Q(T4)} {AM} {Q(f'giữa {TG} có chư thiên')} {NHP} {q(T4)} {AM} "
          f"{Q('thế giới chư thiên là cõi súc sinh')} {NHP} {q(T4)} {AM} {Q(BUGS)} {NHP}")
    d.seg("5-870", f"{Q(T4N)} {AM} {NANU(ER)} {AM} {hanci_yes(ER, T4)}")
    d.seg("5-871",
          f"{Q(T4)} {AM} {Q(KEEP)} {NH} {TENA_HI(T4N)}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (198) Magga
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    d.seg("5-872",
          f"{Q(MG5)} {AM} {NANU(VB8)} {AM} {hanci_no(VB8, MG5)}",
          f"{Q(MG5)} {AM} {NANU_VUTTAM}",
          *DHP,
          f"{ATTHEVA} {AM} {TENA_HI(MG8)}")
    d.seg("5-873",
          f"{Q(mg(S[2], 1))} {AM} {Q(mg(S[0], 1))} {NHP} {q(mg(S[2], 1))} {AM} {Q(mg(S1235, 1))} {NHP}",
          f"{Q(mg(S34, 1))} {AM} {Q(mg(f'{S[0]}… {S[7]}', 1))} {NHP}",
          f"{Q(mg(S[0], 0))} {AM} {Q(mg(S[2], 0))} {NHP} {q(mg(S[0], 0))} {AM} {Q(mg(S34, 0))} {NHP}",
          f"{Q(mg(S1235, 0))} {AM} {Q(mg(S234, 0))} {NHP}")
    d.seg("5-874", f"{Q(AMG8)} {AM} {NANU_VUTTAM} “{PUB}” [Trung Bộ Kinh 3.431]! {ATTHEVA} {AM} {TENA_HI(MG5)}")
    d.seg("5-875",
          f"{Q(MG5)} {AM} {NANU_VUTTAM} “{SUB}” [Trường Bộ Kinh 2.214]! {ATTHEVA} {AM} {TENA_HI(MG8)}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (199) Ñāṇa (twelve)
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    d.seg("5-876",
          f"{Q(T6)} {AM} {Q(LN12)} {NHP} {q(LN12)} {AM} {Q(f'có mười hai {SOM}')} {NHP} {q(f'có mười hai {SOM}')} "
          f"{AM} {Q(f'có mười hai {SOP}')} {NHP} {q(f'có mười hai {SAM}… {ANM}… {ARM}')} {NHP} "
          f"{q(f'có mười hai {ARM}')} {AM} {Q(f'có mười hai {ARP}')} {NHP}")
    d.seg("5-877",
          f"{NVQ(T6)} {AM} {NANU_VUTTAM} {DC} {ATTHEVA} {AM} {TENA_HI(T6)}",
          E(x=KX[6]),
          f"{VAGGA20}.",
          TASSUDDANAM,
          UDDANA,
          CATUTTHO_PANNASAKO,
          TASSUDDANAM,
          UDDANA50)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    (PL, 1), (MG5, 1), (MG8, 1), (AMG8, 2), ("cụ thể là –", 2), (MGA, 1), ("nghiệp có quả không gián đoạn", 1),
    ("Mẹ bị tước đoạt mạng sống, cha bị tước đoạt mạng sống, bậc A-la-hán bị tước đoạt mạng sống, máu của Như Lai "
     "bị làm cho chảy", 2), ("tước đoạt mạng sống của cha", 2), ("quan điểm sai lầm có mười chủ đề", 2),
    (f"trong {DV} này", 2), ("sa-môn", 2), ("cõi súc sinh", 2), ("thế giới chư thiên", 2), (TG, 2), ("ngạ quỷ", 2),
    ("cõi khổ", 2), ("điều an ổn", 2), *[(x, 2) for x in ARU], (J[0], 1), ("nghiệp bằng thân, nghiệp bằng lời nói", 1),
    ("sinh kế", 2), ("những điều chưa từng được nghe trước đây", 4), ("sát hại sinh mạng, lấy của không được cho", 4),
    ("nói dối", 4), ("cảm giác khó chịu", 1), ("thế gian khác", 1), ("tri giác", 1), ("Giáo Pháp", 1),
    ("Trung Bộ Kinh", 4), ("Tăng Chi Bộ Kinh", 4), ("Trường Bộ Kinh", 4), ("người phàm phu", 1),
    (", ".join(S), 2), ("tỉnh thức đúng đắn", 1),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (ANT, "16-atthamavaggo.md"), ("cố ý tước đoạt mạng sống", "20-dvadasamavaggo.md"),
    *[(k, "10-dutiyavaggo.md") for k in KILLERS + ARU],
    ("sát hại sinh mạng, lấy của không được cho, nói dối", "10-dutiyavaggo.md"),
    (f"” {SUT_Q} {NATTHI} “", "14-chatthavaggo.md"), (f"” {SUT_S} {B.NO_CA_VATA} “", "14-chatthavaggo.md"),
    ("\n".join(VERSE1[:2]), "21-terasamavaggo.md"), (VERSE1[2].split(", bị nung")[0], "21-terasamavaggo.md"),
    ("bị nung đốt trong địa ngục suốt một kiếp” [Tiểu Phẩm 354; Tăng Chi Bộ Kinh 10.39; Kinh Phật Thuyết Như Vậy 18].",
     "21-terasamavaggo.md"),
    ("người tồn tại suốt một kiếp", "21-terasamavaggo.md"), ("Ưu-đà-di", "24-solasamavaggo.md"),
    (E(x=NA), "19-ekadasamavaggo.md"), (K(x=NA), "19-ekadasamavaggo.md"), (PJ, "10-dutiyavaggo.md"),
    ("có thể nhập thành tựu thiền", "13-pancamavaggo.md"), (f"mà {FOUR}", "12-catutthavaggo.md"),
    ("có thể thực hiện sự bố thí", "21-terasamavaggo.md"), (f"có thể cho {CIV}", "21-terasamavaggo.md"),
    ("có thể cho đồ ăn khất thực… có thể cho chỗ ở", "21-terasamavaggo.md"), (GIL, "15-sattamavaggo.md"),
    (f"{DEV} có sự phòng hộ", "11-tatiyavaggo.md"), (f"{MAN} có sự phòng hộ", "11-tatiyavaggo.md"),
    ("qua đời", "18-dasamavaggo.md"), ("Ngạ Quỷ Sự", "15-sattamavaggo.md"), ("đang bốc cháy", "10-dutiyavaggo.md"),
    ("sự chấm dứt của các nghiệp có chủ ý", "25-sattarasamavaggo.md"), ("nghiệp xấu ác", "19-ekadasamavaggo.md"),
    ("Đức Thế Tôn đã nói rằng có năm cõi tái sinh –", "16-atthamavaggo.md"),
    ("và nó không phải là", "8-satipatthanakatha.md"), ("và nó là chi phần của con đường", "23-pannarasamavaggo.md"),
    ("trong Kinh Pháp Cú].", "10-dutiyavaggo.md"), ("giữa loài hai chân", "25-sattarasamavaggo.md"),
    (f"trong {DV} này", "10-dutiyavaggo.md"), ("là vượt thế gian", "23-pannarasamavaggo.md"),
    ("Có phải có mười hai", "14-chatthavaggo.md"), (SOP, "10-dutiyavaggo.md"), (ARP, "10-dutiyavaggo.md"),
    (ARM, "10-dutiyavaggo.md"), (SAM, "10-dutiyavaggo.md"), (ANM, "10-dutiyavaggo.md"),
    (f"{ROSE}. ‘Và {AS1} này cần được hiểu biết trọn vẹn’, {ME}… đã được hiểu biết trọn vẹn, {ME}",
     "12-catutthavaggo.md"),
    (f"‘và {AS2} [{SPELL} (Syā., Kaṃ.): dukkhasamudayo] này cần dứt bỏ’, {ME}… đã được dứt bỏ, {ME}… ‘đây là {AS3}",
     "12-catutthavaggo.md"),
    (f"‘và {AS3} này cần được tự mình chứng nghiệm’, {ME}… đã được tự mình chứng nghiệm, {ME}… ‘đây là {AS4}’, {ME}… "
     f"‘và {AS4} này cần được tu tập’, {ME}… đã được tu tập, {ME}, ", "12-catutthavaggo.md"),
    (ROSE_PE, "12-catutthavaggo.md"), ("[Đại Phẩm 15; Tương Ưng Bộ Kinh 5.1081; Phân Tích Đạo 2.30]",
                                       "12-catutthavaggo.md"),
    ("trống rỗng", "1-puggalakatha.md"), ("được tìm thấy", "1-puggalakatha.md"), ("cõi trời", "1-puggalakatha.md"),
    ("Nhóm năm mươi thứ ba.", "23-pannarasamavaggo.md"), ("Sự chế ngự tâm", "24-solasamavaggo.md"),
    ("sự tích lũy phước", "25-sattarasamavaggo.md"), (TASSUDDANAM, "10-dutiyavaggo.md"),
    ("gốc rễ, và điều được xác định riêng biệt.", "23-pannarasamavaggo.md"), ("Không có.", "12-catutthavaggo.md"),
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
    assert VERSE1 != C21.VERSE and V21_VAR in C21.VERSE[2] and V21_VAR not in VERSE1[2], "VERSE1 derivation"
    print(f"ch28 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


def find(pats, maxhits=2, maxc=600):
    names = [f.name for f in sorted(B.PALI_DIR.glob("*.md")) if not re.match(r"(26|27|28|29|30|31)-", f.name)]
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
                    s = max(0, m.start() - 60)
                    print(f"== {pat} [{n} {i + 1}]\n PI: {ln[s:s + 240]}\n VI: {vl[i][:maxc] if i < len(vl) else '-'}")


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text and "chánh niệm" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len([ln for ln in text.splitlines() if ln.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--find":
        find(sys.argv[2:])
    else:
        main()
