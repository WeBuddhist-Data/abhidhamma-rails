# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 21: 21-terasamavaggo.md (Terasamavaggo, ^5-21-0 … ^5-685),
the ten kathā (126)-(135) of the thirteenth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_4_vi / build_10_vi / build_13_vi / build_14_vi / build_15_vi / build_18_vi (read-only; importing writes nothing)
for strings shared with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4
Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur
in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run
against the Pāli. Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_21_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as C4      # noqa: E402  (magga names)
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –, KILLERS)
import build_13_vi as C13    # noqa: E402  (tena phassena taṃ phassaṃ phusati … list)
import build_14_vi as C14    # noqa: E402  (niyāma names)
import build_15_vi as C15    # noqa: E402  (kusalākusalā …, dvinnaṃ phassānaṃ…pe…, hanci frames)
import build_18_vi as C18    # noqa: E402  (suvidūra sutta, abridged)

NAME = "21-terasamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA, ATTHEVA, NANU_VUTTAM = (B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA, B.ATTHEVA,
                                                   B.NANU_VUTTAM)
VAR = B.VAR
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA13 = B.VAGGA[13]                                     # Terasamavaggo = «Chương thứ mười ba» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
hanci_no, hanci_yes, nanu_l = C15.hanci_no, C15.hanci_yes, C15.nanu_l

# ================================================================ kathā names (headings and closing lines)
KP = "người tồn tại suốt một kiếp"                        # kappaṭṭho (terms file heading (126); kappa «kiếp» core)
AP = "người đã tiến hành nghiệp có quả không gián đoạn"   # anantarāpayutto puggalo (ānantarika kamma pi-1/pi-2)
NIP = C13.NI_P                                            # niyato «người cố định» (ch13)
NIV = "người bị ngăn che"                                 # nivuto (nīvaraṇa «chướng ngại» core)
SMB = "người đang hiện diện đối mặt"                      # sammukhībhūto (sammukhībhāva ch5 / ch15)
SAMP = "người đang nhập thành tựu thiền"                  # samāpanno (ch10)
JN = "sự ưa thích tầng thiền"                             # jhānanikanti (nikanti «sự ưa thích» pi-1; jhāna core)
ASR = "sự tham đắm điều không khoan khoái"                # asātarāgo (asāta «không khoan khoái» pi-2)
DT = "khao khát đối tượng của ý"                          # dhammataṇhā (pi-1 ^1 lobha list)
RT = ["khao khát hình sắc", "khao khát âm thanh", "khao khát mùi", "khao khát vị", "khao khát vật xúc chạm"]
# rūpataṇhā … phoṭṭhabbataṇhā (pi-1)
AB = "là không xác định về mặt đạo đức"                   # abyākata (predicate, ch16 «là không xác định …»)
DS = "sự phát sinh của khổ đau"                           # dukkhasamudayo (pi-2 ^2-189)
KX = {1: KP,                                              # Kappaṭṭhakathā (terms file)
      2: "sự có được điều thiện",                         # Kusalapaṭilābhakathā (paṭilābha «sự có được» ch12)
      3: AP,                                              # Anantarāpayuttakathā
      4: f"sự cố định của {NIP}",                         # Niyatassa niyāmakathā (niyāma ch13 / ch14)
      5: NIV,                                             # Nivutakathā
      6: SMB,                                             # Sammukhībhūtakathā
      7: f"việc {SAMP} thỏa thích",                       # Samāpanno assādetikathā (no -ti: no «cho rằng», ch17)
      8: ASR,                                             # Asātarāgakathā
      9: f"việc cho rằng {DT} {AB}",                      # Dhammataṇhā abyākatātikathā
      10: f"việc cho rằng {DT} không phải là {DS}"}       # Dhammataṇhā na dukkhasamudayotikathā


def heads(n):
    """#### Terasamavaggo ^5-21-n-0 / ##### (125+n) n. <title> ^5-21-n-1-0"""
    return [(4, VAGGA13, f"5-21-{n}-0"), (5, f"({125 + n}) {n}. {K(x=KX[n])}", f"5-21-{n}-1-0")]


# ================================================================ (126) Kappaṭṭha
STAY = "có thể tồn tại suốt"                              # tiṭṭheyya (optative «có thể», ch10 / ch13)
T1 = f"{KP} {STAY} một kiếp"                              # kappaṭṭho kappaṃ tiṭṭheyya
KS = "kiếp hình thành"                                    # kappo saṇṭhāti (saṇṭhāti «hình thành» ch15)
KKM = "nghiệp khiến tồn tại suốt một kiếp"                # kappaṭṭhiyaṃ kammaṃ
SB = C10.KILLERS[4]                                       # saṅghabhedako «kẻ chia rẽ Tăng đoàn» (ch10)
NOTE = (f"[{VAR} (?): vehāsaṃ gacchatīti; vì đây chỉ là lời khẳng định của {B.PARAVADI}, như ở dòng thứ chín "
        f"của {B.BOOK_TITLE} 621-623]")
# [vehāsaṃ gacchatīti (?) ayaṃ hi paravādissa paṭiññāyeva, kathā. 621-623 navamapantiyaṃ viya] (ch5 «(?)» pattern)
IDP = ["nền tảng thần thông bằng ý muốn", "nền tảng thần thông bằng tinh tấn", "nền tảng thần thông bằng tâm",
       "nền tảng thần thông bằng sự thẩm xét"]            # chanda- … vīmaṃsiddhipādo (pi-2 ^2-457)
VERSE = ["“Kẻ chia rẽ Tăng đoàn thuộc cõi khổ, thuộc địa ngục, là người tồn tại suốt một kiếp;",
         "Ưa thích bè phái, đứng trên điều phi pháp, rơi khỏi điều an ổn;",
         f"Sau khi chia rẽ Tăng đoàn đang hòa hợp [{VAR} (Sī., Ka.): bhinditvā], bị nung đốt trong địa ngục suốt "
         "một kiếp” [Tiểu Phẩm 354; Tăng Chi Bộ Kinh 10.39; Kinh Phật Thuyết Như Vậy 18]."]
# Āpāyiko nerayiko, kappaṭṭho saṅghabhedako; / Vaggarato adhammaṭṭho, yogakkhemā padhaṃsati; / Saṅghaṃ samaggaṃ
# bhetvāna, kappaṃ nirayamhi paccatī (apāya «cõi khổ» pi-2; yogakkhema «điều an ổn» pi-2)

# ================================================================ (127) Kusalapaṭilābha
KC = "tâm thiện"                                          # kusalaṃ cittaṃ
T2 = f"{KP} không thể có được {KC}"                       # kappaṭṭho kusalaṃ cittaṃ na paṭilabheyya
DANA = f"{KP} có thể thực hiện sự bố thí"                 # kappaṭṭho dānaṃ dadeyya (dānaṃ deti ch15)
CET = "bảo tháp"                                          # cetiya
PAD = f"có thể đi nhiễu quanh {CET} theo chiều bên phải"  # cetiyaṃ abhidakkhiṇaṃ kareyya
GIFTS = chain([f"có thể cho {x}" for x in ("y phục", "đồ ăn khất thực", "chỗ ở", C15.GIL, "món ăn cứng",
                                            "món ăn mềm", "nước uống")]
              + [f"có thể đảnh lễ {CET}", f"có thể dâng vòng hoa lên {CET}", "có thể dâng hương thơm",
                 "có thể dâng dầu thoa", f"{PAD} [{VAR} (Pī.): padakkhiṇaṃ]"])
# cīvaraṃ dadeyya … pānīyaṃ dadeyya (pi-4 «cho»; ch15 khādanīya …) cetiyaṃ vandeyya … vilepanaṃ āropeyya
VUT = f"có thể có được {KC} của sự xuất khỏi từ đó"       # tato vuṭṭhānaṃ kusalaṃ cittaṃ paṭilabheyya (ch14)
HIGH = f"có thể có được {KC} thuộc cõi hình sắc… thuộc cõi không hình sắc… vượt thế gian"   # (pi-1)

# ================================================================ (128) Anantarāpayutta
NY, NY_MI, NY_SM = C14.NY, C14.NY_MI, C14.NY_SM          # niyāma / micchatta- / sammattaniyāma (ch14)
OK = "có thể bước vào"                                    # okkameyya (okkamati niyāmaṃ «bước vào» ch12 / ch13)
T3 = f"{AP} {OK} {NY_SM}"
ABH = f"không có khả năng bước vào {NY_SM}"               # abhabbo sammattaniyāmaṃ okkamituṃ (bhabba ch13)
PAY = "nghiệp ấy đã được tiến hành, sự hối tiếc đã được làm sinh khởi, sự ân hận đã được làm sinh ra"
# taṃ kammaṃ payuttaṃ kukkuccaṃ uppāditaṃ vippaṭisāriyaṃ janitaṃ (kukkucca / vippaṭisāra pi-1; ch14 verbs)
WD = "sau khi rút lại nghiệp ấy, xua tan sự hối tiếc, dẹp bỏ sự ân hận"
# taṃ kammaṃ paṭisaṃharitvā kukkuccaṃ paṭivinodetvā vippaṭisāriyaṃ paṭivinetvā
WDN = "nghiệp ấy đã được rút lại, sự hối tiếc đã được xua tan, sự ân hận đã được dẹp bỏ"
KILL = ["mẹ bị tước đoạt mạng sống", "cha bị tước đoạt mạng sống", "bậc A-la-hán bị tước đoạt mạng sống",
        "máu của Như Lai bị làm cho chảy với tâm độc ác", "Tăng đoàn bị chia rẽ"]   # (pi-2 ^2-U55)
PAYA = "đã tiến hành nghiệp ấy"                           # taṃ kammaṃ payutto āsi

# ================================================================ (129) Niyatassa niyāma
T4 = f"{NIP} bước vào {NY}"                               # niyato niyāmaṃ okkamati
MB = "tu tập"                                             # bhāvetvā (maggaṃ bhāveti «tu tập con đường» ch3)


def pre(x, y=NY):
    """pubbe X bhāvetvā pacchā Y okkamati"""
    return f"trước đó {MB} {x} rồi sau đó bước vào {y}"


NY_SO, NY_AR = C14.NY_SO, C14.NY_AR                       # sotāpatti- / arahattaniyāma (ch14)
M4 = [C4.SOTAPATTIMAGGA, C4.SAKADAGAMIMAGGA, C4.ANAGAMIMAGGA, C14.MG_AR]   # (pi-2, ch4, ch12)
WINGS = ["sự thiết lập tỉnh thức", "nỗ lực đúng đắn", "nền tảng thần thông", "năng lực", "sức mạnh",
         "chi phần giác ngộ"]                             # satipaṭṭhāna … bojjhaṅga (pi-1 ^1 lokuttara list)
BODHI = "Bồ-tát có khả năng không thấu hiểu Giáo Pháp trong đời ấy"
# bhabbo bodhisatto tāya jātiyā dhammaṃ nābhisametuṃ (as written; bodhisatta ch12; bhabbo … abhisametuṃ ch13)

# ================================================================ (130)-(131) Nivuta / Sammukhībhūta
T5 = f"{NIV} dứt bỏ chướng ngại"                          # nivuto nīvaraṇaṃ jahati (jahati ch4)
T6 = f"{SMB} dứt bỏ xiềng xích"                           # sammukhībhūto saṃyojanaṃ jahati
RAT = ("người đã tham đắm dứt bỏ sự tham đắm, người đã sân hận dứt bỏ sự sân hận, người đã si mê dứt bỏ sự si mê, "
       "người đã bị phiền não làm ô nhiễm dứt bỏ các phiền não")
# ratto rāgaṃ jahati … kiliṭṭho kilese jahati (ratta «đã tham đắm» ch11; kilissamāna ch11; rāga … ch13)
INS = ("dùng sự tham đắm mà dứt bỏ sự tham đắm, dùng sự sân hận mà dứt bỏ sự sân hận, dùng sự si mê mà dứt bỏ sự "
       "si mê, dùng các phiền não mà dứt bỏ các phiền não")   # rāgena rāgaṃ jahati … (ch13 «dùng X mà V»)
CSP = "gắn liền với tâm"                                  # cittasampayutta (pi-1)
TWO_PE = C15.TWO_PE                                       # dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ (ch15)
KSD_A = C15.KSD_A                                         # kusalākusalā … sammukhībhāvaṃ āgacchanti (pi-4, ch15)
KSD_S = f"{C15.KSD.split(',')[0]}… {KSD_A[len(C15.KSD) + 1:]}"   # kusalākusalā…pe… sammukhībhāvaṃ āgacchanti
FAR4 = C18.FAR4                                           # cattārimāni, bhikkhave, suvidūravidūrāni! … ārakā (ch18)
SAMAHITE = ("Khi tâm đã an định như vậy, trong sạch, trong sáng, không còn vết nhơ, đã lìa những thứ làm vẩn đục, "
            "đã trở nên mềm dẻo, dễ vận dụng, vững vàng, đạt đến sự bất động, vị ấy dẫn tâm đến sự hiểu biết về sự "
            "diệt tận các ô nhiễm")                        # so evaṃ samāhite citte … abhininnāmeti (pi-4 ^4 catukka)
SAMAHITE_PE = "Khi tâm đã an định như vậy… vị ấy dẫn tâm đến sự hiểu biết về sự diệt tận các ô nhiễm"
JANATO = ("Khi vị ấy biết như vậy, thấy như vậy, tâm được giải thoát khỏi ô nhiễm dục lạc… tâm được giải thoát "
          "khỏi ô nhiễm vô minh")                         # tassa evaṃ jānato … avijjāsavāpi cittaṃ vimuccati (pi-4)


def far_unit(first, last):
    """Kusalākusalā … āgacchantīti? Āmantā. Nanu vuttaṃ bhagavatā – "cattārimāni …"ti. Attheva suttantoti? Āmantā.
    Tena hi na vattabbaṃ – "…"ti.  (ch18 fourfar)"""
    return f"{Q(first)} {AM} {NANU_VUTTAM} {FAR4} {ATTHEVA} {AM} {TENA_HI_NA(last)}"


def nivuta_block(d, n, t, ids, short):
    """(130) / (131): the same four segments"""
    for lv, tt, sid in heads(n):
        d.head(lv, tt, sid)
    rag = f"{Q(t)} {AM} {Q(RAT)} {NHP} {q(INS)} {NHP}"
    d.seg(ids[0],
          rag,
          f"{Q(f'sự tham đắm {CSP}, con đường {CSP}')} {AM} {Q(TWO_PE)} {NHP} "
          f"{q('sự tham đắm là bất thiện, con đường là thiện')} {AM} {Q(KSD_A)} {NHP}")
    if short:
        sut = (f"{far_unit(KSD_S, KSD_S)}",
               f"{Q(t)} {AM} {NANU_VUTTAM} “{SAMAHITE_PE}”! {ATTHEVA} {AM} {TENA_HI_NA(t)}")
    else:
        sut = (f"{far_unit(KSD_A, KSD_S)}",
               f"{Q(t)} {AM} {NANU_VUTTAM} “{SAMAHITE}”! {ATTHEVA} {AM} Vậy thì không nên nói – “{t}”…")
    d.seg(ids[1], *sut)
    d.seg(ids[2],
          f"{NVQ(t)} {AM} {NANU_VUTTAM} “{JANATO}”! {ATTHEVA} {AM} {TENA_HI(t)}",
          E(x=KX[n]))


# ================================================================ (132) Samāpanno assādeti
T7 = f"{SAMP} thỏa thích, {JN} lấy tầng thiền làm đối tượng"   # samāpanno assādeti, jhānanikanti jhānārammaṇā
# (assāda «sự thỏa thích» pi-2; -ārammaṇa «lấy … làm đối tượng» ch11 / ch17)
K3J = "tầng thiền ấy là đối tượng của tầng thiền ấy"      # taṃ jhānaṃ tassa jhānassa ārammaṇaṃ (ch13 K3 frame)
SELFS = ", ".join(f"dùng {x} ấy mà {v} {x} ấy" for x, v in C13.SELF[:10])   # tena phassena … pajānāti (ch13)
GRAT = "vị ấy thỏa thích với nó, ham muốn nó, và nhờ nó mà đạt đến sự hài lòng"
# so taṃ assādeti taṃ nikāmeti tena ca vittiṃ āpajjati (nikāmanā «sự ham muốn» pi-1)
JHANA = (f"“Này các tỳ-khưu, ở đây, vị tỳ-khưu hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện tượng bất "
         f"thiện, chứng nhập và an trú tầng thiền thứ nhất, {GRAT}; nhờ sự hướng tâm và sự duy trì tâm lắng xuống… "
         f"tầng thiền thứ hai… tầng thiền thứ ba… chứng nhập và an trú tầng thiền thứ tư, {GRAT}” "
         "[Tăng Chi Bộ Kinh 4.123]!")                      # (pi-1 jhāna formula; idha, bhikkhave, bhikkhu ch18)

# ================================================================ (133) Asātarāga
T8 = f"có {ASR}"                                          # atthi asātarāgo


def seek(x):
    """X-ābhinandino sattā, atthi keci X patthenti pihenti esanti gavesanti pariyesanti, X ajjhosāya tiṭṭhanti"""
    return (f"chúng sinh hoan hỷ với {x}, có những người mong ước, ước ao, tìm kiếm, truy tìm, tìm cầu {x}, "
            f"sống bám chặt vào {x}")                     # (patthanā / pihanā pi-1; abhinandati ch17)


RA, PA = "khuynh hướng tiềm ẩn tham đắm", "khuynh hướng tiềm ẩn ác cảm"   # rāgānusayo / paṭighānusayo (pi-2)
SUV, DUV = C15.SUV, C15.DUV                               # sukhā / dukkhā vedanā (pi-1, ch15)
FEEL = "dễ chịu, hoặc khó chịu, hoặc không khó chịu cũng không dễ chịu"   # sukhaṃ vā dukkhaṃ vā … (pi-2)
VED = (f"“Người ấy, đã rơi vào sự thuận theo và sự chống đối như vậy, cảm nhận bất cứ cảm giác nào, {FEEL}, người "
       "ấy hoan hỷ với cảm giác ấy, tán thán nó, sống bám chặt vào nó” [Trung Bộ Kinh 3.409, trong Kinh Lớn về Sự "
       "Diệt Tận Khao Khát]!")
# so evaṃ anurodhavirodhaṃ samāpanno … abhinandati abhivadati ajjhosāya tiṭṭhati [ma. ni. 3.409 mahātaṇhāsaṅkhaye]

# ================================================================ (134)-(135) Dhammataṇhā
T9 = f"{DT} {AB}"
T10 = f"{DT} không phải là {DS}"
VIPAB = "quả của nghiệp không xác định về mặt đạo đức"   # vipākābyākata (vipāka pi-1; lesson: keep both words)
KIRAB = "điều không xác định về mặt đạo đức mang tính chức năng"   # kiriyābyākata (pi-1 ^1-1068)
LB = "sự tham lam"                                        # lobho (pi-1 core)
TANHA = ("“Đó là khao khát dẫn đến sự hiện hữu mới, đi kèm với sự thích thú và tham đắm, tìm vui thích chỗ này "
         "chỗ kia, cụ thể là – khao khát dục lạc, khao khát được hiện hữu, khao khát không còn hiện hữu”")
# yāyaṃ taṇhā ponobbhavikā … vibhavataṇhā (pi-2 ^2 Saccavibhaṅga, verbatim)


def lb(x):
    """X-taṇhā lobho (apposition)"""
    return f"{x}, {LB},"


def dt_block(d, n, ids, neg_pred, pos_pred, both_pe):
    """(134) / (135)"""
    for lv, tt, sid in heads(n):
        d.head(lv, tt, sid)
    t = f"{DT} {neg_pred}"
    first = []
    if n == 9:
        first.append(f"{Q(t)} {AM} {Q(f'là {VIPAB}, {KIRAB}, vật chất, Niết-bàn, lĩnh vực mắt… lĩnh vực vật xúc chạm')} "
                     f"{NHP}")
    first.append(f"{Q(t)} {AM} {Q(f'{RT[0]} {neg_pred}')} {NHP} {q(t)} {AM} {Q(f'{chain(RT[1:])} {neg_pred}')} {NHP}")
    first.append(f"{Q(f'{RT[0]} {pos_pred}')} {AM} {Q(f'{DT} {pos_pred}')} {NHP} "
                 f"{q(f'{both_pe} {pos_pred}')} {AM} {Q(f'{DT} {pos_pred}')} {NHP}")
    d.seg(ids[0], *first)
    said = f"Đức Thế Tôn đã nói rằng khao khát {pos_pred}"
    said_l = f"Đức Thế Tôn đã nói rằng {LB} {pos_pred}, {DT} là {LB}"
    u1 = f"{Q(t)} {AM} {NANU(said)} {AM} {hanci_no(said, t)}"
    u2 = f"{Q(t)} {AM} {NANU(said_l)} {AM} {hanci_no(said_l, t)}"
    if n == 9:
        d.seg(ids[1], u1, u2)
    else:
        d.seg(ids[1], f"{u1} {u2}")
    neg_l = f"{lb(DT)} {neg_pred}"
    d.seg(ids[2],
          f"{Q(neg_l)} {AM} {Q(f'{lb(RT[0])} {neg_pred}')} {NHP} {q(neg_l)} {AM} "
          f"{Q(f'{lb(both_pe)} {neg_pred}')} {NHP}",
          f"{Q(f'{lb(RT[0])} {pos_pred}')} {AM} {Q(f'{lb(DT)} {pos_pred}')} {NHP} "
          f"{q(f'{lb(f'{RT[1]}… {RT[4]}')} {pos_pred}')} {AM} {Q(f'{lb(DT)} {pos_pred}')} {NHP}")
    cite = " [Đại Phẩm 14; Trường Bộ Kinh 2.400]" if n == 9 else ""
    d.seg(ids[3], f"{Q(t)} {AM} {NANU_VUTTAM} {TANHA}{cite}! {ATTHEVA} {AM} {TENA_HI_NA(t)}")
    sa = f"đó là {DT}"
    return t, f"{NVQ(t)} {AM} {NANU(sa)} {AM} {hanci_yes(sa, t)}"


# ================================================================ uddāna
UDD = f"{cap(T1)}, {T2}, {T3}, {T4}, {T5}, {T6}, {JN}, {ASR}, {T9}, {T10}."
# Kappaṭṭho kappaṃ tiṭṭheyya, … jhānanikanti, asātarāgo, dhammataṇhā abyākatā, dhammataṇhā na dukkhasamudayoti.


def build():
    d = B.Doc()
    d.head(3, VAGGA13, "5-21-0")
    # ------------------------------------------------------------ (126) Kappaṭṭha
    d.head(4, f"(126) 1. {K(x=KX[1])}", "5-21-1-0")
    d.seg("5-654",
          f"{Q(T1)} {AM} {Q(f'{KS} và Đức Phật xuất hiện trong thế gian')} {NHP} "
          f"{Q(T1)} {AM} {Q(f'{KS} và Tăng đoàn bị chia rẽ')} {NHP} "
          f"{q(T1)} {AM} {Q(f'{KS} và {KP} làm {KKM}')} {NHP} "
          f"{q(T1)} {AM} {Q(f'{KS} và {KP} qua đời')} {NHP}")
    d.seg("5-655",
          f"{Q(T1)} {AM} {Q(f'{STAY} kiếp quá khứ, {STAY} kiếp tương lai')} {NHP} "
          f"{q(T1)} {AM} {Q(chain([f'{STAY} {n} kiếp' for n in ('hai', 'ba', 'bốn')]))} {NHP}")
    d.seg("5-656",
          f"{Q(T1)} {AM} Khi kiếp đang bị thiêu đốt, {KP} đi đến đâu? Đi đến một thế giới khác. "
          f"Đi khi đã chết, hay đi qua không trung? Đi khi đã chết. "
          f"{Q(f'{KKM} chín muồi trong các đời kế tiếp')} {NHP} {NOTE} {q('đi qua không trung')} "
          f"{AM[:-1]} {NOTE}. {Q(f'{KP} có thần thông')} {NHP} {q(f'{KP} có thần thông')} {AM} "
          f"{Q(f'{KP} ' + ', '.join(f'đã tu tập {x}' for x in IDP))} {NHP}")
    d.seg("5-657",
          f"{NVQ(T1)} {AM} {NANU_VUTTAM}",
          *VERSE,
          f"{ATTHEVA} {AM} {TENA_HI(T1)}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (127) Kusalapaṭilābha
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-658",
          f"{Q(T2)} {AM} {Q(DANA)} {AM} {hanci_no(DANA, T2)}",
          f"{Q(T2)} {AM} {Q(f'{KP} {GIFTS}')} {AM} Nếu {KP} {PAD}, {B.NO_CA_VATA} “{T2}”…")
    d.seg("5-659",
          f"{Q(f'{KP} có thể có được {KC}')} {AM} {Q(VUT)} {AM} {Q(HIGH)} {NHP}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (128) Anantarāpayutta
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-660",
          f"{Q(T3)} {AM} {Q(f'{OK} cả {NY_MI} và {NY_SM}, cả hai')} {NHP} {q(T3)} {AM} {NANU(PAY)} {AM} "
          f"{hanci_no(PAY, T3)}")
    abh_wd = f"{AP}, {WD} [{VAR} (Sī., Pī., Ka.): paṭivinodetvā], {ABH}"
    abh_wd2 = f"{AP}, {WD}, {ABH}"
    d.seg("5-661",
          f"{Q(f'{AP} {ABH}')} {AM} {Q(chain(KILL))} {NHP}",
          f"{Q(abh_wd)} {AM} {Q(f'{KILL[0]}… {KILL[1]}… {KILL[4]}')} {NHP}",
          f"{Q(abh_wd2)} {AM} {NANU(WDN)} {AM} {hanci_no(WDN, abh_wd2)}")
    d.seg("5-662",
          f"{Q(T3)} {AM} {NANU(PAYA)} {AM} {hanci_no(PAYA, T3)}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (129) Niyatassa niyāma
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-663",
          f"{Q(T4)} {AM} {Q(f'{NIP} theo hướng sai lầm bước vào {NY_SM}, {NIP} theo hướng đúng đắn bước vào {NY_MI}')} "
          f"{NHP}",
          f"{Q(T4)} {AM} {Q(pre('con đường'))} {NHP} {q(pre(M4[0], NY_SO))} {NHP} "
          f"{q(pre(chain(M4[1:]), NY_AR))} {NHP}",
          f"{Q(pre(chain(WINGS)))} {NHP}")
    d.seg("5-664",
          f"{NVQ(T4)} {AM} {Q(BODHI)} {NH} {TENA_HI(T4)}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (130) Nivuta / (131) Sammukhībhūta
    nivuta_block(d, 5, T5, ("5-665", "5-666", "5-667"), short=False)
    nivuta_block(d, 6, T6, ("5-668", "5-669", "5-670"), short=True)
    # ------------------------------------------------------------ (132) Samāpanno assādeti
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    d.seg("5-671",
          f"{Q(T7)} {AM} {Q(K3J)} {NHP} {q(K3J)} {AM} {Q(SELFS)} {NHP}",
          f"{Q(f'{JN} {CSP}, tầng thiền {CSP}')} {AM} {Q(TWO_PE)} {NHP}",
          f"{Q(f'{JN} là bất thiện, tầng thiền là thiện')} {AM} {Q(KSD_A)} {NHP}")
    d.seg("5-672", far_unit(KSD_A, KSD_A))
    d.seg("5-673",
          f"{NVQ(T7)} {AM} {NANU_VUTTAM} {JHANA} {ATTHEVA} {AM} {TENA_HI(T7)}",
          E(x=KX[7]))
    # ------------------------------------------------------------ (133) Asātarāga
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    hap = seek("hạnh phúc")
    feel_pos = f"{RA} nằm sẵn trong {SUV}, {PA} nằm sẵn trong {DUV}"
    d.seg("5-674",
          f"{Q(T8)} {AM} {Q(seek('khổ đau'))} {NHP} {nanu_l(hap)} {AM} {hanci_no(hap, T8)}",
          f"{Q(T8)} {AM} {Q(f'{RA} nằm sẵn trong {DUV}, {PA} nằm sẵn trong {SUV}')} {NHP} {nanu_l(feel_pos)} {AM} "
          f"{hanci_no(feel_pos, T8)}")
    d.seg("5-675",
          f"{NVQ(T8)} {AM} {NANU_VUTTAM} {VED} {ATTHEVA} {AM} {TENA_HI(T8)}",
          E(x=KX[8]))
    # ------------------------------------------------------------ (134) / (135) Dhammataṇhā
    _, last9 = dt_block(d, 9, ("5-676", "5-677", "5-678", "5-679"), AB, "là bất thiện", f"{RT[1]}… {RT[4]}")
    d.seg("5-680", last9, E(x=KX[9]))
    _, last10 = dt_block(d, 10, ("5-681", "5-682", "5-683", "5-684"), f"không phải là {DS}", f"là {DS}",
                         chain(RT[1:]))
    d.seg("5-685", last10, E(x=KX[10]), f"{VAGGA13}.", TASSUDDANAM, UDD)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    (", ".join(IDP), 2), (", ".join(cap(x) if i == 0 else x for i, x in enumerate(KILL)), 2),
    ("sự hối tiếc", 1), ("sự ân hận", 1), ("chướng ngại", 1), ("xiềng xích", 1), (CSP, 1), ("cõi khổ", 2),
    ("chúng sinh địa ngục", 2), ("trong một thế giới", 2), ("thần thông", 1), ("điều an ổn", 2),
    ("tu tập sự thiết lập tỉnh thức vượt thế gian… tu tập nỗ lực đúng đắn vượt thế gian… tu tập nền tảng thần "
     "thông vượt thế gian… tu tập năng lực vượt thế gian… tu tập sức mạnh vượt thế gian… tu tập chi phần giác ngộ", 1),
    (SAMAHITE, 4), ("Khi vị ấy biết như vậy, thấy như vậy, tâm được giải thoát khỏi ô nhiễm dục lạc", 4),
    ("tâm được giải thoát khỏi ô nhiễm vô minh", 4),
    ("Đó là khao khát dẫn đến sự hiện hữu mới", 2), (TANHA[TANHA.index("đi kèm"):-1], 2), (DS, 2),
    (", ".join(RT + [DT]), 1), ("sự ưa thích, sự ham muốn, sự mong ước, sự ước ao", 1),
    ("hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, chứng nhập và an trú tầng thiền thứ nhất",
     1), ("nhờ sự hướng tâm và sự duy trì tâm lắng xuống", 1), ("tầng thiền thứ tư", 1),
    ("thuộc cõi hình sắc", 1), ("thuộc cõi không hình sắc", 1), ("vượt thế gian", 1),
    ("không xác định về mặt đạo đức mang tính chức năng", 1), ("Quả của nghiệp", 1), (LB, 1),
    (f"thì ở đó {RA} của chúng sinh nằm sẵn", 2), (f"thì ở đó {PA} của chúng sinh nằm sẵn", 2), ("không khoan khoái", 2),
    ("Quan điểm về sự thỏa thích", 2), (f"điều {FEEL}", 2), ("tìm cầu", 2),
    ("Trung Bộ Kinh", 4), ("Tăng Chi Bộ Kinh", 4), ("Trường Bộ Kinh", 4), ("mang tính chức năng", 1),
    ("lĩnh vực mắt", 2), ("lĩnh vực vật xúc chạm", 2), ("Niết-bàn", 1), ("vật chất", 2),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (KSD_A, "15-sattamavaggo.md"), (TWO_PE, "15-sattamavaggo.md"), (C15.SUV, "15-sattamavaggo.md"),
    (C15.DUV, "15-sattamavaggo.md"), ("thực hiện sự bố thí", "15-sattamavaggo.md"),
    ("món ăn cứng", "15-sattamavaggo.md"), ("món ăn mềm", "15-sattamavaggo.md"), ("nước uống", "15-sattamavaggo.md"),
    (C15.GIL, "15-sattamavaggo.md"), ("hình thành", "15-sattamavaggo.md"),
    (FAR4[1:-2], "18-dasamavaggo.md"), ("người đã qua đời", "18-dasamavaggo.md"),
    ("người đã chết", "18-dasamavaggo.md"), ("Này các tỳ-khưu, ở đây, vị tỳ-khưu", "18-dasamavaggo.md"),
    (SELFS, "13-pancamavaggo.md"), (K3J.replace("tầng thiền", "hiểu biết"), "13-pancamavaggo.md"),
    (f"bước vào {NY_SM}", "13-pancamavaggo.md"), ("có khả năng thấu hiểu Giáo Pháp", "13-pancamavaggo.md"),
    (NIP, "13-pancamavaggo.md"), (NY_SO, "14-chatthavaggo.md"), (NY_AR, "14-chatthavaggo.md"),
    (NY_MI, "14-chatthavaggo.md"), ("sự xuất khỏi", "14-chatthavaggo.md"),
    (SAMP, "10-dutiyavaggo.md"), (SB, "10-dutiyavaggo.md"), (TASSUDDANAM, "10-dutiyavaggo.md"),
    ("Tiểu Phẩm", "10-dutiyavaggo.md"), ("Đại Phẩm", "12-catutthavaggo.md"), ("Bồ-tát", "12-catutthavaggo.md"),
    ("sự có được", "12-catutthavaggo.md"), ("Kinh Phật Thuyết Như Vậy", "16-atthamavaggo.md"),
    ("đã tham đắm", "11-tatiyavaggo.md"), ("bị phiền não làm ô nhiễm", "11-tatiyavaggo.md"),
    ("cả hai", "11-tatiyavaggo.md"), ("hoan hỷ với", "17-navamavaggo.md"),
    ("là không xác định về mặt đạo đức", "16-atthamavaggo.md"), ("Đức Phật", "3-brahmacariyakatha.md"),
    ("tu tập con đường", "3-brahmacariyakatha.md"), ("dứt bỏ", "4-jahatikatha.md"),
    ("[dị bản (?): na jahatīti;", "5-sabbamatthitikatha.md"), ("đã tu tập", "11-tatiyavaggo.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    cache = {}
    for s, f in PI5:
        if f not in cache:
            cache[f] = (B.OUT_DIR / f).read_text(encoding="utf-8")
        if s not in cache[f]:
            missing.append((s, f))
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch21 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
