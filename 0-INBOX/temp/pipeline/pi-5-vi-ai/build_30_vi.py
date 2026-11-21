# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 30: 30-bavisatimavaggo.md (Bāvīsatimavaggo, ^5-30-0 … ^5-907),
the ten kathā (208)-(217) of the twenty-second vagga and its uddāna (no fifty-group close in this file).

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_10 / 12 / 15 / 21 / 25 (read-only; importing writes nothing) for strings shared with those chapters,
so every repeat is byte-identical. Every string claimed from the pi-1..4 Vietnamese rails is asserted to occur
there, every string taken from a finished pi-5 chapter is asserted to occur in that chapter's output; the sample's
per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli. Every Pāli sentence keeps its
own Vietnamese sentence.

run:  python -I -B -X utf8 build_30_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –, CRIMES)
import build_12_vi as C12    # noqa: E402  (CIVARA)
import build_15_vi as C15    # noqa: E402  (hanci_no / hanci_yes / nanu_l, GIL)
import build_21_vi as C21    # noqa: E402  (CET, PAD, GIFTS)
import build_25_vi as C25    # noqa: E402  (puññābhisaṅkhāra list, ācināti … ṭhito lines)

NAME = "30-bavisatimavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA, ATTHEVA, NANU_VUTTAM = (B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA, B.ATTHEVA,
                                                  B.NANU_VUTTAM)
VAR = B.VAR
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA22 = B.VAGGA[22]                                     # Bāvīsatimavaggo = «Chương thứ hai mươi hai» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
hanci_no, hanci_yes, nanu_l = C15.hanci_no, C15.hanci_yes, C15.nanu_l
AR = "bậc A-la-hán"                                       # arahā (pi-4)
PNB = "nhập Niết-bàn trọn vẹn"                            # parinibbāyati (pi-4 parinibbuto «đã nhập Niết-bàn trọn vẹn»)

# ================================================================ kathā names (headings and closing lines)
KX = {1: "sự nhập Niết-bàn trọn vẹn",                     # Parinibbānakathā (terms file)
      2: "tâm thiện",                                     # Kusalacittakathā (kusalacitta pi-1)
      3: "trạng thái bất động",                           # Āneñjakathā (āneñja pi-2 āneñjābhisaṅkhāra)
      4: "sự thấu hiểu Giáo Pháp",                        # Dhammābhisamayakathā (pi-4, ch4)
      5: "cả ba",                                         # Tissopikathā (tissopi «cả ba» ch19; as written)
      6: "những gì không xác định về mặt đạo đức",        # Abyākatakathā (= ch22 (143), same Pāli)
      7: "điều kiện thực hành",                           # Āsevanapaccayakathā (ch23 āsevanapaccaya)
      8: "những gì kéo dài trong khoảnh khắc"}            # Khaṇikakathā (ch19 ekacittakkhaṇika «kéo dài trong khoảnh khắc …»)
NUMS = {2: "(209) 2.", 3: "(210) 3.", 4: "(211) 4.", 5: "(212-4) 5-7.", 6: "(215) 8.", 7: "(216) 9.", 8: "(217) 10."}


def heads(n):
    """#### Bāvīsatimavaggo ^5-30-n-0 / ##### (…) n. <title> ^5-30-n-1-0"""
    return [(4, VAGGA22, f"5-30-{n}-0"), (5, f"{NUMS[n]} {K(x=KX[n])}", f"5-30-{n}-1-0")]


# ================================================================ (208) Parinibbāna
NB = "sự nhập Niết-bàn trọn vẹn"                          # parinibbāna
APH = "chưa dứt bỏ"                                       # appahāya (ch12 «chưa dứt bỏ xiềng xích của người tại gia»)
T1 = f"có {NB} mà {APH} một xiềng xích nào đó"            # atthi kiñci saṃyojanaṃ appahāya parinibbānaṃ
SKD, ANOT = "quan điểm về tự ngã", "sự không biết ghê sợ tội lỗi"   # sakkāyadiṭṭhi / anottappa (pi-1, ch4, ch2)
T1_LIST = f"có {NB} nào đó mà {APH} {SKD}… mà {APH} {ANOT}"   # atthi kiñci sakkāyadiṭṭhiṃ appahāya…pe… anottappaṃ appahāya …
SARAGA = f"{AR} có tham đắm… có phiền não"                # arahā sarāgo…pe… sakileso (sarāga ch5; kilesa pi-1)
NIRAGA = f"{AR} không có tham đắm… không có phiền não"    # arahā nirāgo…pe… nikkileso (nikkilesa ch11, ch19)
BV = f"{AR} biết toàn bộ phạm vi của Đức Phật"            # arahā sabbaṃ buddhavisayaṃ jānāti (visaya «phạm vi», new)

# ================================================================ (209) Kusalacitta
T2 = f"{AR} {PNB} với tâm thiện"                          # arahā kusalacitto parinibbāyati
KAMMA = [k.split(" [")[0] for k in C25.KAMMA9]            # gati- … manussasobhagyasaṃvattaniyaṃ (ch25, variant dropped)
ABHI10 = [f"{v} {n}" for n, v in C25.SV] + [f"làm nghiệp dẫn đến {x}" for x in KAMMA]
# puññābhisaṅkhāraṃ abhisaṅkharonto … manussasobhagyasaṃvattaniyaṃ kammaṃ karonto (ch25 ^5-777 wording)
assert ", ".join(ABHI10) == C25.ABHI.replace(f" [{B.SPELL} (?): ādhipaccasaṃvattanikaṃ]", "")
ACI8 = ", ".join(["tích lũy", "giảm trừ"] + C25.VERBS6)   # ācinanto … sandhūpento (ch2 / ch25 verbs)
ST1, ST2, ST3, ST4 = C25.ST1, C25.ST2, C25.ST3, C25.ST4   # nevācināti … vidhūpetvā ṭhito (ch2, ch25)
UPS = f"{AR} {PNB} khi có sự tỉnh thức được thiết lập, tỉnh thức và hiểu biết rõ ràng"
# arahā upaṭṭhitassati sato sampajāno parinibbāyati (upaṭṭhitassati / sampajāno pi-4; sato sampajāno pi-2)

# ================================================================ (210) Āneñja
CT = {"an": "trạng thái bất động",                        # āneñje (pi-2 āneñjābhisaṅkhāra)
      "pk": "tâm bình thường",                            # pakaticitte (aṭṭhakathā: bhavaṅgacitte)
      "km": "tâm mang tính chức năng",                    # kiriyamaye citte (kiriyā «mang tính chức năng» pi-1)
      "vp": "tâm thuộc quả của nghiệp",                   # vipākacitte (vipāka «quả của nghiệp» pi-1)
      "ka": "tâm không xác định về mặt đạo đức mang tính chức năng",      # kiriyābyākate citte (pi-1, ch23)
      "va": "tâm không xác định về mặt đạo đức thuộc quả của nghiệp"}     # vipākābyākate citte (ch20)


def st(k):
    """arahā X-e ṭhito parinibbāyati (ṭhito «đứng vững» ch2 / pi-4)"""
    return f"{AR} {PNB} khi đang đứng vững trong {CT[k]}"


T3 = st("an")
BH4 = "Đức Thế Tôn, sau khi xuất khỏi tầng thiền thứ tư, liền sau đó đã nhập Niết-bàn trọn vẹn"
# bhagavā catutthajjhānā vuṭṭhahitvā samanantarā parinibbuto (vuṭṭhahati «xuất khỏi» ch14; samanantarā «liền sau» pi-2)
CITE_DN = "[Trường Bộ Kinh 2.219]"                        # [dī. ni. 2.219] (ch8)

# ================================================================ (211) Dhammābhisamaya, (212-214) Tissopi
GB = "khi nằm trong bào thai"                             # gabbhaseyyāya (pi-2 gabbhaseyyaka «sinh ra từ bào thai»)
DA = "sự thấu hiểu Giáo Pháp"                             # dhammābhisamaya (pi-4, ch4)
AP = "sự đạt đến trạng thái A-la-hán"                     # arahattappatti (patti pi-2 / ch27; arahatta ch11)
SG = "người đang nằm mơ"                                  # supinagata (pi-2 supinaṃ passati «nằm mơ»)
T4, T5 = f"{GB} có {DA}", f"{GB} có {AP}"
T6, T7 = f"{SG} có {DA}", f"{SG} có {AP}"
CAUSES = ["việc thuyết giảng Giáo Pháp", "việc nghe Giáo Pháp", "việc đàm luận Giáo Pháp", "việc hỏi han",
          "việc thọ trì giới hạnh", "sự phòng hộ cửa các giác quan", "sự biết tiết độ trong ăn uống",
          "sự chuyên tâm thực hành việc thức canh vào đầu đêm và cuối đêm"]
# dhammadesanā (ch11, ch26), dhammassavanaṃ (pi-4), dhammasākacchā (new), paripucchā (pi-4 «hỏi han»),
# sīlasamādānaṃ (pi-2 «thọ trì giới hạnh»), indriyesu guttadvāratā, bhojane mattaññutā (pi-1),
# pubbarattāpararattaṃ jāgariyānuyogo (pi-2 ^2 jhānavibhaṅga)
CAUSES_PE = f"{CAUSES[0]}, {CAUSES[1]}… {CAUSES[-1]}"     # dhammadesanā, dhammassavanaṃ…pe… jāgariyānuyogo
TWO = ("có hai điều kiện để quan điểm đúng đắn sinh khởi – tiếng nói từ người khác, và sự chú tâm đúng cách")
# dve paccayā sammādiṭṭhiyā uppādāya – parato ca ghoso, yoniso ca manasikāro (ghosa «tiếng nói» pi-1;
# yoniso manasikaroto «chú tâm đúng cách» pi-4, ch22)
SUTT = "người đang ngủ, buông thả, mất tỉnh thức, không hiểu biết rõ ràng"
# suttassa pamattassa muṭṭhassatissa asampajānassa (pamāda «sự buông thả» pi-2; muṭṭhassati asampajāno ch11)

# ================================================================ (215) Abyākata
T8 = f"tất cả tâm của {SG} là không xác định về mặt đạo đức"   # sabbaṃ supinagatassa cittaṃ abyākataṃ (ch16 / ch21 predicate)
DREAM = "trong giấc mơ"                                   # supinantena
CR = C10.CRIMES                                           # pāṇaṃ haneyya … nigamaghātakaṃ kareyya (ch10, ch25)
KILL1 = f"{DREAM} có thể {CR[0]}"
CET, PAD = C21.CET, C21.PAD                               # cetiya «bảo tháp»; cetiyaṃ abhidakkhiṇaṃ kareyya
GIFT11 = ([f"có thể cho {x}" for x in (C12.CIVARA, "đồ ăn khất thực", "chỗ ở", C15.GIL, "món ăn cứng", "món ăn mềm",
                                       "nước uống")]
          + [f"có thể đảnh lễ {CET}", f"có thể dâng vòng hoa lên {CET}", "có thể dâng hương thơm", "có thể dâng dầu thoa"])
assert chain(GIFT11 + [PAD]) + f" [{VAR} (Pī.): padakkhiṇaṃ]" == C21.GIFTS, "GIFTS derivation"
DREAM_ALL = (f"{DREAM} có thể {CR[1]}… " + ", ".join(f"có thể {x}" for x in CR[2:])
             + f", {DREAM} có thể hưởng thụ hành vi dâm dục, đồ bất tịnh của {SG} có thể thoát ra, "
             + f"{DREAM} có thể thực hiện sự bố thí, " + ", ".join(GIFT11[:-1]) + f", {GIFT11[-1]}… {PAD}")
# adinnaṃ ādiyeyya…pe… nigamaghātakaṃ kareyya, … methunaṃ dhammaṃ paṭiseveyya (pi-4, ch10), supinagatassa asuci
# mucceyya (asuci «đồ bất tịnh» ch10), … dānaṃ dadeyya (ch21), cīvaraṃ dadeyya … vilepanaṃ āropeyya…pe… (ch21 GIFTS)
ABB = f"Đức Thế Tôn đã nói rằng tâm của {SG} không được tính đến"   # supinagatassa cittaṃ abbohāriyaṃ vuttaṃ bhagavatā
# (abbohārika: aṭṭhakathā «āpattiṃ sandhāya»; «Đức Thế Tôn đã nói rằng» ch16 / ch25)

# ================================================================ (216) Āsevanapaccaya
APC = "tính chất làm điều kiện thực hành"                 # āsevanapaccayatā (ch13 paccayatā; ch23 āsevanapaccaya)
T9 = f"không có bất kỳ {APC} nào"                         # natthi kāci āsevanapaccayatā
T9_YES = f"có một {APC} nào đó"                           # atthi kāci āsevanapaccayatā
GOES = "dẫn đến địa ngục, dẫn đến cõi súc sinh, dẫn đến cõi ngạ quỷ"   # niraya- tiracchānayoni- pettivisayasaṃvattanika
ASV = "khi được thực hành, được tu tập, được làm đi làm lại"           # āsevito bhāvito bahulīkato (pi-1 āsevanā, pi-2)
BHK = "này các tỳ-khưu"
P_PANA, P_ADIN, P_KAMA, P_MUSA = ("việc sát hại sinh mạng", "việc lấy của không được cho",
                                  "hành vi sai trái trong các dục lạc", "việc nói dối")      # (pi-2)
P_PIS, P_PHA, P_SAM = "lời nói chia rẽ", "lời nói thô ác", "việc nói lời phù phiếm"          # (pi-2)
P_SURA = "việc uống rượu nấu và rượu men"                 # surāmerayapāna (pi-2 rượu nấu, rượu men)
TAKE = {"pana": "tuổi thọ ngắn", "adin": "sự tổn hại về tài sản", "kama": "sự thù địch và oán hận",
        "musa": "sự vu khống điều không có thật", "pis": "sự chia lìa với bạn bè", "pha": "âm thanh không dễ ưa",
        "sam": "lời nói không được tin nhận", "sura": "sự điên loạn"}
# appāyuka / bhogabyasana (pi-2 «sự tổn hại về tài sản») / sapattavera / abbhūtabbhakkhāna / mittehi bhedana /
# amanāpasadda (pi-1 amanāpiya «không dễ ưa») / anādeyyavācā / ummattaka


def lite(x, k):
    """yo sabbalahuso X-assa vipāko manussabhūtassa Y-saṃvattaniko hoti"""
    return f"quả nhẹ nhất của {x}, đối với người sinh làm người, là dẫn đến {TAKE[k]}"


def full(x):
    """X, bhikkhave, āsevito bhāvito bahulīkato niraya- … pettivisayasaṃvattaniko"""
    return f"{x}, {BHK}, {ASV}, thì {GOES}"


SUTTA_1 = f"{cap(full(P_PANA))}, {lite(P_PANA, 'pana')}"
SUTTA_2 = (f"{cap(full(P_ADIN))}, {lite(P_ADIN, 'adin')}… {lite(P_KAMA, 'kama')}… {lite(P_MUSA, 'musa')}… "
           f"{lite(P_PIS, 'pis')}… {lite(P_PHA, 'pha')}… {lite(P_SAM, 'sam')}, {P_SURA}, {BHK}, khi được thực "
           f"hành… {lite(P_SURA, 'sura')}")
CITE_AN = "[Tăng Chi Bộ Kinh 8.40]"                       # [a. ni. 8.40]
MI, SA = B.MICCHA, B.SAMMA                                # micchā- / sammā- path factors (pi-1, pi-2)
AMATA = ("thì thâm nhập vào điều bất tử, lấy điều bất tử làm nơi đến cuối cùng, lấy điều bất tử làm điểm kết thúc")
# amatogadhā hoti amataparāyanā amatapariyosānā (amata «điều bất tử», parāyana «nơi đến cuối cùng» ch10)
S_MI1 = cap(full(MI[0]))
S_MI2 = f"{cap(MI[1])}… {MI[7]}, {BHK}, khi được thực hành, được tu tập… dẫn đến cõi ngạ quỷ"
S_SA1 = f"{cap(SA[0])}, {BHK}, {ASV}, {AMATA}"
S_SA2 = f"{cap(SA[1])}, {BHK}, {ASV}… {SA[7]}, {BHK}, {ASV}, {AMATA}"
ATTHEVA_L = ATTHEVA[0].lower() + ATTHEVA[1:-1]            # attheva suttantoti, (comma for "?", ch23 precedent)

# ================================================================ (217) Khaṇika
T10 = "tất cả các hiện tượng kéo dài trong khoảnh khắc của một tâm"   # ekacittakkhaṇikā sabbe dhammā (ch19)
ST_ = "đứng vững"                                         # saṇṭhāti (ch4 «đứng vững trong»)
WORLD = [("đại địa", ST_), ("đại dương", ST_), ("núi Tu-di, vua của các ngọn núi,", ST_), ("nước", ST_),
         ("lửa", ST_), ("gió", ST_), ("cỏ, gỗ và cây rừng", ST_)]
# mahāpathavī … tiṇakaṭṭhavanappatayo (sample ^5-128 … ^5-191)
W_LINE = "trong một tâm, " + ", ".join(f"{x} {v}" for x, v in WORLD)   # citte mahāpathavī saṇṭhāti … saṇṭhahanti
AY = B.AYATANA                                            # lĩnh vực mắt … (pi-2)


def sj(i, w):
    """X-āyatanaṃ X-viññāṇena sahajātaṃ (sahajāta «cùng sinh với» ch15)"""
    return f"{AY[i]} cùng sinh với thức qua {w}"


SJ_E, SJ_K = sj(0, "mắt"), sj(4, "thân")
SARI = "Chẳng phải tôn giả Xá-lợi-phất đã nói thế này sao –"   # nanu āyasmā sāriputto etadavoca – (ch11)
AV = "này các hiền giả"                                   # āvuso (ch10)
TAJ = "thì vẫn chưa có sự xuất hiện của phần thức tương ứng"   # neva tāva tajjassa viññāṇabhāgassa pātubhāvo hoti
TAJ_YES = "thì như vậy có sự xuất hiện của phần thức tương ứng"   # evaṃ tajjassa viññāṇabhāgassa pātubhāvo hoti
# (pātubhāva «sự xuất hiện» pi-2; samannāhāra «sự lưu ý» pi-2; tajja «tương ứng», viññāṇabhāga «phần thức» new)
INT_E, EXT_E = "mắt thuộc phần bên trong", "các hình sắc thuộc phần bên ngoài"   # ajjhattika / bāhira (pi-1)
INT_K, EXT_K = "thân thuộc phần bên trong", "các vật xúc chạm thuộc phần bên ngoài"
INTACT = "không bị hư hoại"                               # aparibhinna
COME, NCOME = "đi vào tầm", "không đi vào tầm"            # āpāthaṃ āgacchanti (ch10 «đi vào tầm của …»)
NSAM, SAM = "và không có sự lưu ý tương ứng", "và có sự lưu ý tương ứng"   # no ca / tajjo ca samannāhāro hoti
VAR_E = f" [{VAR} (nhiều bản): viññāṇabhāvassa]"          # [viññāṇabhāvassa (bahūsu)]
EYE = (f"“{cap(INT_E)}, {AV}, {INTACT}, và {EXT_E} {NCOME}, {NSAM}, {TAJ}{VAR_E}. "
       f"{cap(INT_E)}, {AV}, {INTACT}, và {EXT_E} {COME}, {NSAM}, {TAJ}. "
       f"Nhưng khi, {AV}, {INT_E} {INTACT}, và {EXT_E} {COME}, {SAM}, {TAJ_YES}”")
BODY = (f"“{cap(INT_K)}, {AV}, {INTACT}, và {EXT_K} {NCOME}, và không… "
        f"{INT_K}, {AV}, {INTACT}, và {EXT_K} {COME}, và không… "
        f"nhưng khi, {AV}, {INT_K} {INTACT}, và {EXT_K} {COME}, {SAM}, {TAJ_YES}”")
CITE_MN = "[Trung Bộ Kinh 1.306]"                         # [ma. ni. 1.306]

# ================================================================ uddāna
UDD = f"{cap(T1)}, {T2}, {T3}, {T4}, {T5}, {T6}, {T7}, {T8}, {T9}, {T10}."


def build():
    d = B.Doc()
    d.head(3, VAGGA22, "5-30-0")
    # ------------------------------------------------------------ (208) Parinibbāna
    d.head(4, f"(208) 1. {K(x=KX[1])}", "5-30-1-0")
    d.seg("5-892",
          f"{Q(T1)} {AM} {Q(T1_LIST)} {NHP}",
          f"{Q(T1)} {AM} {Q(SARAGA)} {NHP} {nanu_l(NIRAGA)} {AM} {hanci_no(NIRAGA, T1)}")
    d.seg("5-893",
          f"{NVQ(T1)} {AM} {Q(BV)} {NH} {TENA_HI(T1)}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (209) Kusalacitta
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-894",
          f"{Q(T2)} {AM} Có phải {AR} {PNB} trong khi {chain(ABHI10)} không? {NHP}",
          f"{Q(T2)} {AM} Có phải {AR} {PNB} trong khi {ACI8} không? {NHP} {nanu_l(f'{AR} {ST1}')} {AM} "
          f"{hanci_no(f'{AR} {ST1}', T2)} Chẳng phải {AR} {ST2}, {ST3}; chẳng phải {AR} {ST4} sao? {AM} "
          f"{hanci_no(f'{AR} {ST4}', T2)}")
    d.seg("5-895",
          f"{NVQ(T2)} {AM} {NANU(UPS)} {AM} {hanci_yes(UPS, T2)}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (210) Āneñja
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-896",
          f"{Q(T3)} {AM} {NANU(st('pk'))} {AM} {hanci_no(st('pk'), T3)}",
          f"{Q(T3)} {AM} {Q(st('km'))} {NHP} {nanu_l(st('vp'))} {AM} {hanci_no(st('vp'), T3)}",
          f"{Q(T3)} {AM} {Q(st('ka'))} {NHP} {nanu_l(st('va'))} {AM} {hanci_no(st('va'), T3)}",
          f"{Q(T3)} {AM} Chẳng phải {BH4} {CITE_DN} sao? {AM} {hanci_no(BH4, T3)}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (211) Dhammābhisamaya
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-897",
          f"{Q(T4)} {AM} {Q(f'{GB} có ' + ', '.join(CAUSES))} {NHP} {q(f'{GB} không có {CAUSES_PE}')} {AM} "
          f"{hanci_no(f'{GB} không có {CAUSES_PE}', T4)}",
          f"{Q(T4)} {AM} {NANU(TWO)} {AM} {hanci_no(TWO, T4)}",
          f"{Q(T4)} {AM} {Q(f'{SUTT} có {DA}')} {NHP}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (212-214) Tissopi
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    d.seg("5-898", f"{Q(T5)} {AM} {Q(f'{SUTT} có {AP}')} {NHP}")
    d.seg("5-899", f"{Q(T6)} {AM} {Q(f'{SUTT} có {DA}')} {NHP}")
    d.seg("5-900",
          f"{Q(T7)} {AM} {Q(f'{SUTT} có {AP}')} {NHP}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (215) Abyākata
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    d.seg("5-901",
          f"{Q(T8)} {AM} {Q(KILL1)} {AM} {hanci_no(KILL1, T8)}",
          f"{Q(DREAM_ALL)} {AM} {hanci_no(f'{DREAM} {PAD}', T8)}")
    d.seg("5-902",
          f"{NVQ(T8)} {AM} {NANU(ABB)} {AM} {hanci_yes(ABB, T8)}",
          E(x=KX[6]))
    # ------------------------------------------------------------ (216) Āsevanapaccaya
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    d.seg("5-903",
          f"{Q(T9)} {AM} {NANU_VUTTAM} “{SUTTA_1}” {CITE_AN}. {ATTHEVA} {AM} {TENA_HI(T9_YES)}",
          f"{Q(T9)} {AM} {NANU_VUTTAM} “{SUTTA_2}” {CITE_AN}! {ATTHEVA} {AM} {TENA_HI(T9_YES)}")
    d.seg("5-904",
          f"{Q(T9)} {AM} {NANU_VUTTAM} “{S_MI1}”. {ATTHEVA} {AM} {TENA_HI(T9_YES)}",
          f"{Q(T9)} {AM} {NANU_VUTTAM} “{S_MI2}”! {ATTHEVA} {AM} {TENA_HI(T9_YES)}")
    d.seg("5-905",
          f"{Q(T9)} {AM} {NANU_VUTTAM} “{S_SA1}”! {ATTHEVA} {AM} {TENA_HI(T9_YES)}",
          f"{Q(T9)} {AM} {NANU_VUTTAM} “{S_SA2}” {ATTHEVA_L}, {AM[0].lower()}{AM[1:]} {TENA_HI(T9_YES)}",
          E(x=KX[7]))
    # ------------------------------------------------------------ (217) Khaṇika
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    d.seg("5-906",
          f"{Q(T10)} {AM} {Q(W_LINE)} {NHP}",
          f"{Q(T10)} {AM} {Q(SJ_E)} {NHP} {q(SJ_E)} {AM} {SARI} {EYE} {CITE_MN}! {ATTHEVA} {AM} {TENA_HI_NA(SJ_E)}",
          f"Có phải {AY[1]}… {AY[2]}… {AY[3]}… {SJ_K} không? {NHP} {q(SJ_K)} {AM} {SARI} {BODY} {CITE_MN}! "
          f"{ATTHEVA} {AM} {TENA_HI_NA(SJ_K)}")
    d.seg("5-907",
          f"{NVQ(T10)} {AM} Có phải tất cả các hiện tượng {B.NICCO_DHUVO} không? {NH} {TENA_HI(T10)}",
          E(x=KX[8]),
          f"{VAGGA22}.",
          TASSUDDANAM,
          UDD)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("xiềng xích", 1), (SKD, 1), ("sự không biết ghê sợ tội lỗi", 1), ("phiền não", 1),
    ("sự tạo tác dẫn đến trạng thái bất động", 2), ("Sự tạo tác thuộc về phước", 2),
    ("có sự tỉnh thức được thiết lập", 4), ("hiểu biết rõ ràng", 4), ("tỉnh thức và hiểu biết rõ ràng", 2),
    ("nhập Niết-bàn trọn vẹn", 4), ("mang tính chức năng", 1), ("quả của nghiệp", 1), ("tầng thiền thứ tư", 1),
    ("liền sau", 2), ("Trường Bộ Kinh", 4), ("bào thai", 2), ("sự thấu hiểu Giáo Pháp", 4), ("nghe Giáo Pháp", 4),
    ("hỏi han", 4), ("thọ trì giới hạnh", 2), ("Sự phòng hộ cửa các giác quan", 1),
    ("Sự biết tiết độ trong ăn uống", 1), ("thực hành việc thức canh vào đầu đêm và cuối đêm", 2),
    ("tiếng nói", 1), ("chú tâm đúng cách", 4), ("quan điểm đúng đắn", 1), ("nằm mơ", 2), ("sự buông thả", 2),
    ("hưởng thụ hành vi dâm dục", 4), ("vòng hoa, hương thơm, dầu thoa", 4),
    ("dẫn đến địa ngục", 2), ("dẫn đến cõi súc sinh", 2), ("sự tổn hại về tài sản", 2), ("không dễ ưa", 1),
    ("Việc sát hại sinh mạng, việc lấy của không được cho, hành vi sai trái trong các dục lạc, việc nói dối", 2),
    ("lời nói chia rẽ, lời nói thô ác, việc nói lời phù phiếm", 2), ("rượu nấu, rượu men", 2),
    ("được tu tập", 2), ("sự thực hành", 1), ("thuộc phần bên trong", 1), ("thuộc phần bên ngoài", 1),
    ("sự lưu ý", 2), ("sự xuất hiện", 2), ("thức qua thân", 2), ("thức qua mắt", 2), ("vật xúc chạm", 1),
    ("Tăng Chi Bộ Kinh", 4), ("Trung Bộ Kinh", 4),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (f"{AR} {ST1}", "25-sattarasamavaggo.md"), (f"{AR} {ST2}, {ST3}, {ST4}", "25-sattarasamavaggo.md"),
    (C25.ABHI.split(", làm nghiệp dẫn đến quyền thống trị")[0], "25-sattarasamavaggo.md"),
    ("làm nghiệp dẫn đến của cải lớn, làm nghiệp dẫn đến đoàn tùy tùng lớn, làm nghiệp dẫn đến sự vinh hiển cõi trời, "
     "làm nghiệp dẫn đến sự vinh hiển cõi người", "25-sattarasamavaggo.md"),
    ("bậc A-la-hán dứt bỏ… bậc A-la-hán bám víu… bậc A-la-hán phân tán… bậc A-la-hán gom tụ… bậc A-la-hán dập tắt… "
     "bậc A-la-hán nhen nhóm", "25-sattarasamavaggo.md"),
    (C21.GIFTS, "21-terasamavaggo.md"), ("có thể thực hiện sự bố thí", "21-terasamavaggo.md"),
    (", ".join(CR), "10-dutiyavaggo.md"), ("có thể hưởng thụ hành vi dâm dục", "10-dutiyavaggo.md"),
    ("đồ bất tịnh", "10-dutiyavaggo.md"), (cap(AV), "10-dutiyavaggo.md"),
    ("đã nhập Niết-bàn trọn vẹn", "4-jahatikatha.md"), ("Đức Thế Tôn đã nhập Niết-bàn trọn vẹn", "26-attharasamavaggo.md"), ("đi vào tầm của", "10-dutiyavaggo.md"),
    ("điều bất tử", "10-dutiyavaggo.md"), ("nơi đến cuối cùng", "10-dutiyavaggo.md"), (TASSUDDANAM, "10-dutiyavaggo.md"),
    ("trạng thái A-la-hán", "10-dutiyavaggo.md"),
    ("chưa dứt bỏ xiềng xích", "12-catutthavaggo.md"), ("có tham đắm", "5-sabbamatthitikatha.md"),
    ("không có phiền não", "19-ekadasamavaggo.md"), ("không có phiền não", "11-tatiyavaggo.md"),
    ("mất tỉnh thức, không hiểu biết rõ ràng", "11-tatiyavaggo.md"), ("đã đạt đến trạng thái A-la-hán", "11-tatiyavaggo.md"),
    (SARI, "11-tatiyavaggo.md"), ("xuất khỏi", "14-chatthavaggo.md"),
    (K(x=KX[6]), "22-cuddasamavaggo.md"), ("chú tâm đúng cách", "22-cuddasamavaggo.md"),
    ("tính chất làm điều kiện", "13-pancamavaggo.md"), ("điều kiện thực hành", "23-pannarasamavaggo.md"),
    ("không xác định về mặt đạo đức mang tính chức năng", "23-pannarasamavaggo.md"),
    (", đúng vậy.", "23-pannarasamavaggo.md"),
    ("không xác định về mặt đạo đức thuộc quả của nghiệp", "20-dvadasamavaggo.md"),
    ("là không xác định về mặt đạo đức", "21-terasamavaggo.md"),
    ("kéo dài trong khoảnh khắc của một tâm", "19-ekadasamavaggo.md"), ("cả ba loại khuynh hướng tiềm ẩn", "19-ekadasamavaggo.md"),
    ("đại địa", "1-puggalakatha.md"), ("đại dương", "1-puggalakatha.md"),
    ("núi Tu-di, vua của các ngọn núi,", "1-puggalakatha.md"), ("cỏ, gỗ và cây rừng", "1-puggalakatha.md"),
    ("nếu nước được tìm thấy… nếu lửa được tìm thấy… nếu gió được tìm thấy", "1-puggalakatha.md"),
    (B.NICCO_DHUVO, "1-puggalakatha.md"),
    ("địa ngục, cõi súc sinh, cõi ngạ quỷ", "16-atthamavaggo.md"), ("Đức Thế Tôn đã nói rằng", "16-atthamavaggo.md"),
    (DA, "4-jahatikatha.md"), ("việc thuyết giảng Giáo Pháp", "26-attharasamavaggo.md"),
    ("sự đạt đến", "27-ekunavisatimavaggo.md"), ("cùng sinh với", "15-sattamavaggo.md"),
    ("Trường Bộ Kinh", "8-satipatthanakatha.md"), ("được tu tập, được làm đi làm lại", "19-ekadasamavaggo.md"),
    ("đứng vững trong", "4-jahatikatha.md"), ("đứng vững sau khi đã", "2-parihanikatha.md"),
    ("Phần bàn về cả ba loại khuynh hướng tiềm ẩn đã hoàn tất.", "19-ekadasamavaggo.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s_, f"pi-{b}") for s_, b in CROSS if s_ not in texts[b]]
    cache = {}
    for s_, f in PI5:
        if f not in cache:
            cache[f] = (B.OUT_DIR / f).read_text(encoding="utf-8")
        if s_ not in cache[f]:
            missing.append((s_, f))
    for s_, w in missing:
        print(f"CROSS MISSING in {w}: {s_}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch30 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
    main()
