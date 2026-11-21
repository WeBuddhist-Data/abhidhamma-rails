# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 12: 12-catutthavaggo.md (Catutthavaggo, ^5-12-0 … ^5-417),
the ten kathā (33)-(42) of the fourth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished
chapter builders build_2_vi / build_3_vi / build_4_vi (read-only, importing writes nothing) for the persons,
fruits, paths, defilements and path qualities, so every repeat is byte-identical with those chapters. Every
string claimed from the pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a finished
pi-5 chapter is asserted to occur in that chapter's output; the sample's per-line checks (IDs, dashes, quotes,
NFC, foreign letters) are run against the Pāli.

run:  python -I -B -X utf8 build_12_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402
import build_3_vi as C3      # noqa: E402
import build_4_vi as C4      # noqa: E402
import build_9_vi as C9      # noqa: E402  (vagga close: Tassuddānaṃ –)

NAME = "12-catutthavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA = B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA
VAR, SPELL = B.VAR, B.SPELL


def hanci_no(p, qq):
    """Hañci P, no ca vata re vattabbe – "Q"ti.  (ch2, ch3, ch4)"""
    return f"Nếu {p}, {B.NO_CA_VATA} “{qq}”."


def hanci_yes(p, qq):
    """Hañci P, tena vata re vattabbe – "Q"ti.  (sample)"""
    return B.HANCI.format(p=p, q=qq)


def if_q(x, y):
    """Xti, Yti?  (sample frame, ch8)"""
    return f"Có phải nếu {x}, thì {y} không?"


def like(a, b):
    """Yathā A, evamevaṃ Bti?  (sample ^5-112: «giống như …, cũng vậy, …»)"""
    return Q(f"giống như {a}, cũng vậy, {b}")


# ================================================================ persons, fruits, paths (ch2, ch3, ch4)
AR, SO, SA, AN = C2.AR, C2.SO, C2.SA, C2.AN               # arahā / sotāpanno / sakadāgāmī / anāgāmī (pi-4)
ARAHATTA = C2.FRUIT[AR]                                   # arahattaṃ = «trạng thái A-la-hán»
FR_SO, FR_SA, FR_AN = C2.FRUIT[SO], C2.FRUIT[SA], C2.FRUIT[AN]   # sotāpatti- / sakadāgāmi- / anāgāmiphala
FR_AR = "thành quả A-la-hán"                              # arahattaphalaṃ (pi-2 ^ñāṇavibhaṅga)
MG_SO, MG_SA, MG_AN = C4.SOTAPATTIMAGGA, C4.SAKADAGAMIMAGGA, C4.ANAGAMIMAGGA
MG_AR = "con đường A-la-hán"                              # arahattamaggo (pi-2, pi-1)
PAT_AR, PAT_AN, PAT_SA = C3.PAT["ara"], C3.PAT["ana"], C3.PAT["saka"]   # …sacchikiriyāya paṭipanno puggalo (pi-4)
SOTA4 = ("bậc vào dòng, người tái sinh tối đa bảy lần, người đi từ gia đình này sang gia đình khác, "
         "người có một hạt giống")                        # sotāpanno sattakkhattuparamo, kolaṅkolo, ekabījī (ch3, pi-4)
ANA6 = (f"{AN}, người nhập Niết-bàn trọn vẹn trong khoảng giữa, người nhập Niết-bàn trọn vẹn khi gần mạng chung, "
        "người nhập Niết-bàn trọn vẹn không có sự thúc đẩy, người nhập Niết-bàn trọn vẹn có sự thúc đẩy, "
        f"{C3.UDDHAM}")                                   # anāgāmī, antarā- … uddhaṃsoto akaniṭṭhagāmī (ch3, pi-4)
THREE = C4.THREE_FETTERS                                  # sakkāyadiṭṭhi vicikicchā sīlabbataparāmāsa (pi-1)
AP_R, AP_D, AP_M = C2.AP_R, C2.AP_D, C2.AP_M              # apāyagamanīyo rāgo / doso / moho (ch2)
S3_AP = f"{THREE}, {AP_R}, {AP_D}, {AP_M}"                # sakkāyadiṭṭhiṃ … apāyagamanīyaṃ mohaṃ
S3_AP_PE = f"{C2.SK}… {AP_M}"                             # sakkāyadiṭṭhiṃ…pe… apāyagamanīyaṃ mohaṃ
OLARIKA = C4.OLARIKA                                      # oḷārikaṃ kāmarāgaṃ, oḷārikaṃ byāpādaṃ (ch4)
ANU = f"{C3.KR_A}, {C3.BY_A}"                             # aṇusahagataṃ kāmarāgaṃ, aṇusahagataṃ byāpādaṃ (ch3)
KRB = C4.KRB                                              # kāmarāgabyāpāda (ch4, pi-1)
SING6 = [x[len("các "):] for x in C2.DEV6]                # satipaṭṭhānaṃ … bojjhaṅgo (singular of ch2 / pi-3 list)
FOUR = "hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, tu tập con đường"
FOUR_PE = "hiểu biết trọn vẹn khổ đau… tu tập con đường"  # dukkhaṃ parijānāti…pe… maggaṃ bhāveti (ch5 F, pi-2)
ELDERS = ["Đại Mục-kiền-liên", "Đại Ca-diếp", "Đại Ca-chiên-diên", "Đại Câu-hy-la", "Đại Bàn-đặc"]   # (ch2 ^5-264)
SARI = f"{C2.THERA} Xá-lợi-phất"                          # sāriputto thero (ch2, pi-4)
PUTHU = C4.PUTHUJJANA                                     # puthujjano (pi-1)
SAM = "được trang bị"                                     # samannāgato (pi-2, pi-4)
VIT = "đã vượt qua"                                       # vītivatto (ch5 sabbadukkhavītivatta)
TENA_SAM = f"{SAM} điều ấy"                               # tena samannāgato
NUM = B.NUM


def sam(who, what):
    return f"{who} {SAM} {what}"


L10 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "niềm tin", "sự tinh tấn", "sự tỉnh thức",
       "sự định tâm", "trí tuệ"]                          # phassa … paññā (ch4 SAMODHANA wording)


def ten(n):
    return ", ".join(f"{NUM[n]} {x}" for x in L10)


def ten_pe(n, k=1):
    """the first k items…pe… the last"""
    return f"{', '.join(f'{NUM[n]} {x}' for x in L10[:k])}… {NUM[n]} {L10[-1]}"


# ================================================================ (33) Gihissa arahā
KX1 = "việc cho rằng người tại gia là bậc A-la-hán"       # Gihissa arahātikathā (terms file)
TH1 = "người tại gia là bậc A-la-hán"                     # gihissa arahā
GIHI = "người tại gia"                                    # gihī (pi-2 gahaṭṭha «người tại gia»)
GS = "xiềng xích của người tại gia"                       # gihisaṃyojanaṃ (saṃyojana «xiềng xích» core)
DUK = "người đi đến tận cùng của khổ đau"                 # dukkhassantakaro (pi-4)
NO_GIHI_7 = f"không có {GIHI} nào chưa dứt bỏ {GS} mà ngay trong đời này là {DUK}"
NO_GIHI_8 = f"không có {GIHI} nào chưa dứt bỏ {GS} mà khi thân tan rã là {DUK}"
VACCHA = "Vác-cha-gốt-ta"; VACCHA_V = "Vác-cha"; GOTAMA = "Cồ-đàm"   # vacchagotto / vaccha / gotama (ch4 Cồ-đàm)
GIHI_LIST = ("có thể hưởng thụ hành vi dâm dục, có thể làm phát sinh sự giao hợp, có thể sống trên chiếc giường "
             "chật chội vì con cái, có thể thụ hưởng gỗ đàn hương xứ Ca-thi, có thể mang vòng hoa, hương thơm, dầu "
             "thoa, có thể chấp nhận vàng và bạc, có thể nhận dê và cừu, có thể nhận gà và heo, có thể nhận voi, bò, "
             "ngựa đực và ngựa cái, có thể nhận chim đa đa, chim cút, chim công và chim trĩ "
             f"[{SPELL} (Syā., Kaṃ., Pī.): … kapiñjalaṃ], có thể mang búi tóc có trang sức nhiều màu "
             f"[{VAR} (Syā., Kaṃ., Pī.): pītavaṇṭavālamoḷikaṃ], có thể mặc những tấm vải trắng có viền dài, có thể "
             "suốt đời là người sống trong gia đình")
# methunaṃ dhammaṃ paṭiseveyya (pi-4 «hưởng thụ hành vi dâm dục»), methunaṃ uppādeyya («sự giao hợp» pi-4) …
# mālāgandhavilepana / ajeḷaka / kukkuṭasūkara / hatthigavāssavaḷava (pi-4), jātarūparajata «vàng và bạc» (pi-1),
# agāriyabhūto «người sống trong gia đình» (pi-4)
YASA = "người con nhà gia giáo Da-xá, gia chủ Út-ti-da, thanh niên Sê-tu"   # yaso kulaputto, uttiyo gahapati, setu māṇavo
YASA_P = f"{YASA}, với hình tướng người tại gia, đã đạt đến {ARAHATTA}"     # … gihibyañjanena arahattaṃ patto

# ================================================================ (34) Upapatti
KX2 = "sự tái sinh"                                       # Upapattikathā (upapatti «tái sinh», coordinator)
WR = "ngay khi tái sinh"                                  # saha upapattiyā
TH2 = f"là {AR} {WR}"                                     # saha upapattiyā arahā
NTH2 = f"không phải là {AR} {WR}"                         # na saha upapattiyā arahā
UCIT = "tâm tìm cầu sự tái sinh"                          # upapattesiyaṃ cittaṃ (aṭṭhakathā: paṭisandhicitta)
LOKIYA = "thuộc thế gian"                                 # lokiya (pi-1 core)
SAS, ANS = C4.NEG[4], C4.POS[4]                           # sāsava / anāsava: «là / không phải là đối tượng của ô nhiễm»
SKL = C4.NEG_LAST                                         # saṃkilesiya «là đối tượng của phiền não»
FOUR4 = [C2.R, C2.D, C2.M, C2.AO]                         # rāgo doso moho anottappaṃ (ch2, pi-1)

# ================================================================ (35) Anāsava
KX3 = "những gì không phải là đối tượng của ô nhiễm"      # Anāsavakathā
ALL_AN = f"tất cả các hiện tượng của {AR} {ANS}"          # arahato sabbe dhammā anāsavā
L40 = ", ".join(["con đường", "thành quả", "Niết-bàn", MG_SO, FR_SO, MG_SA, FR_SA, MG_AN, FR_AN, MG_AR, FR_AR]
                + SING6)                                  # maggo phalaṃ nibbānaṃ, sotāpattimaggo … bojjhaṅgo
L40_PE = f"con đường, thành quả, Niết-bàn, {MG_SO}, {FR_SO}… {SING6[-1]}"
ANA_ARAHA = "không còn ô nhiễm"                           # arahā anāsavo (pi-2 anāsavaṃ cetovimuttiṃ «không còn ô nhiễm»)
DH_AN = f"hiện tượng {ANS}"                               # anāsavo dhammo
TO_SAS = f"{ANS} rồi trở thành đối tượng của ô nhiễm"     # anāsavaṃ hutvā sāsavaṃ hoti (sample X hutvā Y hoti)
TO_ANS = f"{SAS} rồi trở thành {ANS}"                     # sāsavaṃ hutvā anāsavaṃ hoti
TS_AS = f"chính cái ấy {ANS}, cái ấy {SAS}"               # taññeva anāsavaṃ taṃ sāsavaṃ
TS_SA = f"chính cái ấy {SAS}, cái ấy {ANS}"               # taññeva sāsavaṃ taṃ anāsavaṃ
PG = ("có thể bị nắm giữ và kìm kẹp, có thể bị cắt và bị đập vỡ, là thứ chung cho quạ, kền kền, diều hâu")   # (ch5)
CIVARA = "y phục"                                         # cīvaraṃ (pi-2)
REQ3 = "cho người phàm phu đồ ăn khất thực, cho chỗ ở, cho thuốc men và vật dụng chữa bệnh"   # (pi-2 ^2-929)
REQ3_AR = f"cho {AR} đồ ăn khất thực, cho chỗ ở, cho thuốc men và vật dụng chữa bệnh"


def poison(x):
    """X-e visaṃ kameyya, satthaṃ kameyya, aggi kameyya (ch5 ^5-293)"""
    return f"chất độc có thể tác động lên {x}, dao kiếm có thể tác động, lửa có thể tác động"


def bind(x, compound=False):
    """labbhā X addubandhanena bandhituṃ … kaṇṭhapañcamehi bandhanehi bandhituṃ (ch5 ^5-293)"""
    mid = (["trói bằng sự giam giữ trong làng, thị trấn, thành phố, xứ sở"] if compound else
           ["trói bằng sự giam giữ trong làng", "trói bằng sự giam giữ trong thị trấn",
            "trói bằng sự giam giữ trong thành phố", "trói bằng sự giam giữ trong xứ sở"])
    return "có thể " + ", ".join([f"trói {x} bằng cùm", "trói bằng dây thừng", "trói bằng xích sắt", *mid,
                                  "trói bằng năm dây trói mà dây thứ năm ở cổ"])


# ================================================================ (36) / (41) Samannāgata
KX4 = "sự được trang bị"                                  # Samannāgatakathā
KX9_H = f"Bàn thêm về {KX4}"                              # Aparāpi samannāgatakathā
KX9_END = f"Phần bàn thêm về {KX4} đã hoàn tất."          # Aparāpi samannāgatakathā niṭṭhitā.
SAID = "nên gọi là"                                       # "X"ti vattabbo (sample «nên gọi là “X”»)
GOT = "đã có được"                                        # paṭiladdha (ch3)
NOFALL = "không sa sút khỏi"                              # aparihīna (ch2 parihāyati «sa sút khỏi»)


def got(who, what, comma, pron="chúng"):
    """X-ena Y paṭiladdhāni[,] tehi ca aparihīno"""
    return f"{who} {GOT} {what}{',' if comma else ''} và {NOFALL} {pron}"


# ================================================================ (37) Upekkhā
KX5 = "sự được trang bị sự bình thản"                     # Upekkhāsamannāgatakathā (upekkhā «sự bình thản» core)
UP6 = "sáu sự bình thản"                                  # chahi upekkhāhi / cha upekkhāyo
CHALANGA = f"{AR} có sự bình thản ở sáu phương diện"      # arahā chaḷaṅgupekkho (ṭhāna «phương diện» ch3)
ALWAYS = "thường xuyên, liên tục, liền mạch"              # satataṃ samitaṃ abbokiṇṇaṃ (abbokiṇṇa «liền mạch» pi-2)
SENSES = [("mắt", "thấy", "hình sắc"), ("tai", "nghe", "âm thanh"), ("mũi", "ngửi", "mùi"), ("lưỡi", "nếm", "vị"),
          ("thân", "chạm", "vật xúc chạm"), ("ý", "nhận biết", "đối tượng của ý")]   # (ch5, pi-1)
ACT = [f"dùng {o} mà {v} {x}" for o, v, x in SENSES]      # cakkhunā rūpaṃ passati … (ch5 «dùng … mà …»)

# ================================================================ (38) Bodhi
KX6 = "việc cho rằng là bậc giác ngộ nhờ sự giác ngộ"     # Bodhiyā buddhotikathā
BB = "là bậc giác ngộ nhờ sự giác ngộ"                    # bodhiyā buddho (bodhi «sự giác ngộ» ch4; buddha «bậc giác ngộ»)
PAST, FUT, PRES = "quá khứ", "tương lai", "hiện tại"      # atīta / anāgata / paccuppanna (ch5 «thuộc …»)
K_B = "nhờ sự giác ngộ ấy mà làm được việc của sự giác ngộ"        # tāya bodhiyā bodhikaraṇīyaṃ karoti (ch5 K frame)
F_B = f"nhờ sự giác ngộ ấy mà {FOUR}"                     # tāya bodhiyā dukkhaṃ parijānāti … (ch5 F frame)
F_B_PE = f"nhờ sự giác ngộ ấy mà {FOUR_PE}"
PATILABHA = "là bậc giác ngộ nhờ có được sự giác ngộ"     # bodhipaṭilābhā buddho


def bb(t):
    return f"là bậc giác ngộ nhờ sự giác ngộ thuộc {t}"


# ================================================================ (39) Lakkhaṇa
KX7 = "các tướng"                                         # Lakkhaṇakathā (lakkhaṇa = bodily mark)
BS = "Bồ-tát"                                             # bodhisatto
CVS = "người sẽ làm vua chuyển luân"                      # cakkavattisatto (rājā cakkavattī «vua chuyển luân» pi-2)
LB = f"người {SAM} các tướng là {BS}"                     # lakkhaṇasamannāgato bodhisatto
PREV = "sự tu tập trước đây, hạnh kiểm trước đây, việc giảng nói Giáo Pháp, việc thuyết giảng Giáo Pháp"
# pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā (dhammadesanā «việc thuyết giảng Giáo Pháp» pi-4)


def born(x):
    return f"khi {x} đang ra đời"                         # X-assa jāyamānassa


GODS = "chư thiên đón nhận trước, loài người sau"         # devā paṭhamaṃ paṭiggaṇhanti pacchā manussā
DEVAPUTTA = ("bốn vị thiên tử đón nhận vị ấy rồi đặt trước mặt người mẹ – “Thưa hoàng hậu, hãy hài lòng! "
             "Người con có uy lực lớn của bà đã ra đời”")
WATER = ("hai dòng nước từ không trung hiện ra – một dòng nước lạnh, một dòng nước nóng – nhờ đó việc dùng nước "
         "được thực hiện cho {x} và cho người mẹ")
STEPS = ("{x} vừa mới sinh ra, đứng vững trên hai bàn chân bằng phẳng, hướng mặt về phía bắc, bước đi bảy bước, "
         "trong khi chiếc lọng trắng được che theo, và nhìn khắp tất cả các phương, và nói lên lời nói hùng dũng – "
         "“Ta là bậc cao nhất của thế gian, Ta là bậc lớn nhất của thế gian, Ta là bậc tối thắng của thế gian, "
         "đây là lần sinh cuối cùng, nay không còn sự hiện hữu mới nữa”")
# natthi dāni punabbhavo: punabbhava «sự hiện hữu mới» (pi-2, coordinator; ch4 «sự tái sinh» to be aligned)
LIGHT = "có sự xuất hiện của ánh sáng lớn, hào quang lớn, sự rung chuyển lớn của mặt đất"   # (ch8 «có sự xuất hiện của»)
BODY = "thân bình thường của {x} tỏa sáng xung quanh một sải tay"
DREAM = "{x} thấy giấc mộng lớn"
MAHAPURISA = (
    f"“Này các tỳ-khưu, có ba mươi hai tướng đại nhân này của bậc đại nhân, mà bậc đại nhân {SAM} những tướng ấy "
    f"chỉ có hai hướng đi, không có hướng đi khác [{VAR} (Ka.): na aññā]! Nếu người ấy sống trong gia đình, thì "
    "trở thành vua, vị vua chuyển luân, theo lẽ phải, vị vua của lẽ phải, làm chủ bốn phương, người chiến thắng, "
    f"đã đạt được sự ổn định của đất nước, {SAM} bảy báu vật. Người ấy có bảy báu vật này, tức là – báu vật bánh "
    "xe, báu vật voi, báu vật ngựa, báu vật ngọc, báu vật người nữ, báu vật gia chủ, chính báu vật vị cố vấn là "
    "thứ bảy. Người ấy có hơn một nghìn người con, can đảm, có thân hình của bậc anh hùng, đánh tan quân địch. "
    "Người ấy chinh phục trái đất này đến tận biển cả, không dùng gậy, không dùng dao kiếm, mà bằng lẽ phải, rồi "
    "cai quản nó. Còn nếu người ấy rời bỏ gia đình, xuất gia sống đời không gia đình, thì trở thành bậc A-la-hán, "
    "bậc Tự Giác Ngộ Hoàn Toàn, người đã vén bức màn che trong thế gian” [Trường Bộ Kinh 3.200].")
# ratana names (ch8), sūra «can đảm» (ch3), sattha «dao kiếm» (ch5), agāra / anagāriya (pi-4 ^4-177)

# ================================================================ (40) Niyāmokkanti
KX8 = "việc bước vào sự cố định"                          # Niyāmokkantikathā (okkamati niyāmaṃ pi-4)
KASS = "Đức Thế Tôn Ca-diếp"                              # kassapo bhagavā (Ca-diếp as ch2 Đại Ca-diếp)
BHAG = "Đức Thế Tôn"
ANANDA = "tôn giả A-nan"                                  # āyasmā ānando (ch5, sample)
CITTA = "gia chủ Chít-ta, Hát-tha-ka người xứ A-la-vi"    # citto gahapati hatthako āḷavako


def ok(who, teacher=KASS):
    """X <teacher>-assa pāvacane okkantaniyāmo caritabrahmacariyo"""
    return (f"{who}, trong lời dạy của {teacher}, đã bước vào sự cố định, đã sống đời sống tu hành trong sạch")


BOK = ok(BS)                                              # bodhisatto kassapassa bhagavato pāvacane okkantaniyāmo …
SAV = f"{BS} là đệ tử của {KASS}"                         # bodhisatto kassapassa bhagavato sāvako
ANUS = "là người hiểu biết nhờ nghe từ người khác"        # anussaviyo (aṭṭhakathā: anussavena paṭividdhadhammo)
SAYAMBHU = f"{BHAG} là bậc tự mình giác ngộ"              # bhagavā sayambhū
SAMANNA = "thành quả của đời sống sa-môn"                 # sāmaññaphala (pi-1, ch4)
TREE = f"{BHAG}, dưới gốc cây Bồ-đề, đã giác ngộ hoàn toàn"   # bhagavatā bodhiyā mūle … abhisambuddhāni (ch3)
DUKKARA = "đã làm những việc khổ hạnh khó làm"            # dukkarakāriyaṃ akāsi
DASSANA = "người thành tựu về sự thấy"                    # dassanasampanno puggalo (sampanna «thành tựu về» pi-4)
OTHER_T = "tôn xưng một bậc đạo sư khác"                  # aññaṃ satthāraṃ uddisati (satthā «bậc đạo sư» pi-4)
UNHEARD = "trong những điều chưa từng được nghe trước đây"   # pubbe ananussutesu dhammesu (pi-4)
ME = "nơi Ta, này các tỳ-khưu"                            # me, bhikkhave
ROSE = (f"{UNHEARD}, con mắt đã khởi lên, hiểu biết đã khởi lên, trí tuệ đã khởi lên, hiểu biết chân thật đã "
        "khởi lên, ánh sáng đã khởi lên")                 # cakkhuṃ udapādi … āloko udapādi (vijjā «hiểu biết chân thật» core)
ROSE_PE = f"{UNHEARD}, con mắt đã khởi lên… ánh sáng đã khởi lên"
AS1 = "sự thật cao quý về khổ đau"                        # dukkhaṃ ariyasaccaṃ (pi-2 ^2-189)
AS2 = "sự thật cao quý về sự phát sinh của khổ đau"
AS3 = "sự thật cao quý về sự chấm dứt khổ đau"
AS4 = "sự thật cao quý về cách thực hành dẫn đến sự chấm dứt khổ đau"
DHAMMACAKKA = (
    f"{B.NANU_VUTTAM} “‘Đây là {AS1}’, {ME}, {ROSE}. ‘Và {AS1} này cần được hiểu biết trọn vẹn’, {ME}… "
    f"đã được hiểu biết trọn vẹn, {ME}, {ROSE_PE}. ‘Đây là {AS2}’, {ME}… ‘và {AS2} "
    f"[{SPELL} (Syā., Kaṃ.): dukkhasamudayo] này cần dứt bỏ’, {ME}… đã được dứt bỏ, {ME}… ‘đây là {AS3} "
    f"[{SPELL} (Syā., Kaṃ.): dukkhanirodho]’, {ME}… ‘và {AS3} này cần được tự mình chứng nghiệm’, {ME}… "
    f"đã được tự mình chứng nghiệm, {ME}… ‘đây là {AS4}’, {ME}… ‘và {AS4} này cần được tu tập’, {ME}… "
    f"đã được tu tập, {ME}, {ROSE}” [Đại Phẩm 15; Tương Ưng Bộ Kinh 5.1081; Phân Tích Đạo 2.30].")

# ================================================================ (42) Sabbasaṃyojanappahāna
KX10 = "sự dứt bỏ tất cả các xiềng xích"                  # Sabbasaṃyojanappahānakathā
TH10 = f"{KX10} là {ARAHATTA}"                            # sabbasaṃyojanānaṃ pahānaṃ arahattaṃ
AMS = "bằng con đường A-la-hán, tất cả các xiềng xích được dứt bỏ"   # arahattamaggena sabbe saṃyojanā pahīyanti


def am(x):
    """arahattamaggena X pajahati (ch4 AM_3 order «dứt bỏ X bằng …»)"""
    return f"dứt bỏ {x} bằng {MG_AR}"


def vb(x, fruit):
    """X-ṃ <fruit> vuttaṃ bhagavatā (X nominative; ch4 «Đức Thế Tôn đã nói rằng …»)"""
    return f"Đức Thế Tôn đã nói rằng {x} là {fruit}"


VB_SO = vb("sự dứt bỏ ba xiềng xích", FR_SO)              # tiṇṇaṃ saṃyojanānaṃ pahānaṃ sotāpattiphalaṃ
VB_SA = vb(f"sự suy yếu của {KRB}", FR_SA)                # kāmarāgabyāpādānaṃ tanubhāvaṃ sakadāgāmiphalaṃ
VB_AN = vb(f"sự dứt bỏ {KRB} không còn sót lại", FR_AN)   # … anavasesappahānaṃ anāgāmiphalaṃ (pi-1 order)
VB_AR = vb(f"sự dứt bỏ {C3.R2}, {C3.R3} không còn sót lại", ARAHATTA)
# rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānaṃ arahattaṃ (ch3 R2 / R3, pi-1)

# ================================================================ vagga close (ch9 frame)
VAGGA4 = B.VAGGA[4]                                       # Catutthavaggo = «Chương thứ tư»
UDDANA = (f"{cap(TH1)}, {TH2}, {ALL_AN}, {sam(AR, 'bốn thành quả')}, cũng vậy với {UP6}, {BB}, {SAM} các tướng, "
          f"{BS} đã bước vào sự cố định, đã sống đời sống tu hành trong sạch, người đang thực hành {SAM} thành quả, "
          f"{TH10}.")
# Gihissa arahā, saha upapattiyā arahā, arahato sabbe dhammā anāsavā, arahā catūhi phalehi samannāgato, evamevaṃ
# chahi upekkhāhi, bodhiyā buddho, salakkhaṇasamannāgato, bodhisatto okkantaniyāmo caritabrahmacariyo, paṭipannako
# phalena samannāgato, sabbasaṃyojanānaṃ pahānaṃ arahattanti.


def heads(n, num, title):
    """#### Catutthavaggo ^5-12-n-0 / ##### (num) n. <title> ^5-12-n-1-0"""
    return [(4, VAGGA4, f"5-12-{n}-0"), (5, f"({num}) {n}. {title}", f"5-12-{n}-1-0")]


def build():
    d = B.Doc()
    K = B.KATHA.format
    E = B.KATHA_END.format
    d.head(3, VAGGA4, "5-12-0")
    # ------------------------------------------------------------ (33) Gihissa arahā
    d.head(4, f"(33) 1. {K(x=KX1)}", "5-12-1-0")
    p6 = f"đối với {AR}, {GS} {C2.PAHINA}, {C2.UC.format(v='')}"
    d.seg("5-387",
          f"{Q(TH1)} {AM} {Q(f'{AR} có {GS}')} {NHP} {q(f'{AR} không có {GS}')} {AM} "
          f"{hanci_no(f'{AR} không có {GS}', TH1)}",
          f"{Q(TH1)} {AM} {NANU(p6)} {AM} {hanci_no(p6, TH1)}",
          f"{Q(TH1)} {AM} Có phải có {GIHI} nào chưa dứt bỏ {GS} mà ngay trong đời này là {DUK} không "
          f"[Trung Bộ Kinh 2.186]? Không có. {hanci_no(NO_GIHI_7, TH1)}",
          f"{Q(TH1)} {AM} Chẳng phải du sĩ {VACCHA} đã nói với Đức Thế Tôn thế này sao – “Thưa ông {GOTAMA}, có "
          f"{GIHI} nào chưa dứt bỏ {GS} mà khi thân tan rã là {DUK} không?” “Này {VACCHA_V}, "
          f"{NO_GIHI_8}”. {B.ATTHEVA} {AM} {TENA_HI_NA(TH1)}",
          f"{Q(TH1)} {AM} {Q(f'{AR} {GIHI_LIST}')} {NHP}",
          f"{NVQ(TH1)} {AM} {NANU(YASA_P)} {AM} {hanci_yes(YASA_P, TH1)}",
          E(x=KX1))
    # ------------------------------------------------------------ (34) Upapatti
    for lv, t, sid in heads(2, 34, K(x=KX2)):
        d.head(lv, t, sid)
    become = {SO: f"trở thành {SO} {WR}", SA: f"trở thành {SA} {WR}", AN: f"trở thành {AN} {WR}"}
    nbecome = {k: f"không {v}" for k, v in become.items()}
    d.seg("5-388",
          *[f"{Q(TH2)} {AM} {Q(become[x])} {NHP}" for x in (SO, SA, AN)],
          *[f"{Q(nbecome[x])} {AM} {hanci_no(nbecome[x], TH2)}" for x in (SO, SA, AN)])
    d.seg("5-389",
          f"{Q(TH2)} {AM} {Q(f'{SARI} {TH2}')} {NH} "
          f"Có phải {chain([f'{C2.THERA} {n}' for n in ELDERS])} {TH2} không? {NHP}",
          f"{Q(f'{SARI} {NTH2}')} {AM} {hanci_no(f'{SARI} {NTH2}', TH2)}",
          f"Có phải {chain([f'{C2.THERA} {n}' for n in ELDERS])} {NTH2} không? {AM} "
          f"{hanci_no(f'{C2.THERA} {ELDERS[-1]} {NTH2}', TH2)}")
    neg5 = f"{UCIT} {C4.NEG_PE5}"
    d.seg("5-390",
          f"{Q(TH2)} {AM} {Q(f'tự mình chứng nghiệm {ARAHATTA} bằng {UCIT}, {LOKIYA}, {SAS}… {SKL}')} {NHP}",
          f"{Q(TH2)} {AM} {Q(f'{UCIT} {C4.POS_PE}')} {NHP}",
          f"{NANU(neg5)} {AM} {hanci_no(neg5, TH2)}",
          f"{Q(TH2)} {AM} {Q(f'bằng {UCIT} mà ' + ', '.join(f'dứt bỏ {x}' for x in FOUR4))} {NHP}",
          f"{Q(TH2)} {AM} Có phải {UCIT} là con đường… {'… '.join(SING6)} không? {NHP}",
          f"{Q(TH2)} {AM} {Q(f'bằng {UCIT} mà {FOUR}')} {NHP} {q(TH2)} {AM} "
          f"{Q(f'tâm lúc chết là tâm con đường, {UCIT} là tâm thành quả')} {NHP}",
          E(x=KX2))
    # ------------------------------------------------------------ (35) Anāsava
    for lv, t, sid in heads(3, 35, K(x=KX3)):
        d.head(lv, t, sid)
    eye, ear, nose, tongue, body = (f"{o} của {AR}" for o in ("mắt", "tai", "mũi", "lưỡi", "thân"))
    d.seg("5-391",
          f"{Q(ALL_AN)} {AM} {Q(f'là {L40}')} {NHP}",
          f"{Q(ALL_AN)} {AM} {Q(f'{eye} {ANS}')} {NHP} {Q(f'{eye} {ANS}')} {AM} {Q(f'là {L40_PE}')} {NHP}",
          f"Có phải {ear}… {nose}… {tongue}… {body} {ANS} không? {NHP} {q(f'{body} {ANS}')} {AM} "
          f"{Q(f'là {L40_PE}')} {NHP}",
          f"{Q(f'{body} {ANS}')} {AM} {Q(f'{body} {PG}')} {AM} {Q(f'{DH_AN} {PG}')} {NHP}",
          f"{Q(poison(body))} {AM} {Q(poison(DH_AN))} {NHP}",
          f"{Q(bind(body))} {AM} {Q(bind(DH_AN, compound=True))} {NHP}")
    sing7 = "… ".join(["thành quả"] + SING6)            # phalaṃ… satipaṭṭhānaṃ… … bojjhaṅgo
    four_pe = "… ".join(FOUR4[1:])                      # doso…pe… moho…pe… anottappaṃ

    def give(cond, to, ts, magga_line):
        return (f"Có phải nếu {cond}, thì {to} không? {NHP} {q(to)} {AM} {Q(ts)} {NHP} {q(ts)} {AM} "
                f"{magga_line}")

    m_as = f"{Q(f'con đường {TO_SAS}')} {NHP} có phải {sing7} {TO_SAS} không? {NHP}"
    m_sa = f"{Q(f'{C2.R} {TO_ANS}')} {NHP} có phải {four_pe} {TO_ANS} không? {NHP}"
    d.seg("5-392",
          give(f"{AR} cho {PUTHU} {CIVARA}", TO_SAS, TS_AS, m_as),
          give(f"{AR} {REQ3}", TO_SAS, TS_AS, m_as),
          give(f"{PUTHU} cho {AR} {CIVARA}", TO_ANS, TS_SA, m_sa),
          give(f"{PUTHU} {REQ3_AR}", TO_ANS, TS_SA, m_sa),
          f"{NVQ(ALL_AN)} {AM} {NANU(f'{AR} {ANA_ARAHA}')} {AM} {hanci_yes(f'{AR} {ANA_ARAHA}', ALL_AN)}",
          E(x=KX3))
    # ------------------------------------------------------------ (36) Samannāgata
    for lv, t, sid in heads(4, 36, K(x=KX4)):
        d.head(lv, t, sid)
    d.seg("5-393",
          f"{Q(sam(AR, 'bốn thành quả'))} {AM} {Q(sam(AR, ten(4)))} {NHP}",
          f"{Q(sam(AN, 'ba thành quả'))} {AM} {Q(sam(AN, ten_pe(3)))} {NHP}",
          f"{Q(sam(SA, 'hai thành quả'))} {AM} {Q(sam(SA, ten_pe(2)))} {NHP}",
          f"{Q(sam(AR, FR_SO))} {AM} {Q(f'{AR} là {SOTA4}')} {NHP} {q(sam(AR, FR_SA))} {AM} "
          f"{Q(f'{AR} là {SA}')} {NHP} {q(sam(AR, FR_AN))} {AM} {Q(f'{AR} là {ANA6}')} {NHP}",
          f"{Q(sam(AN, FR_SO))} {AM} {Q(f'{AN} là {SOTA4}')} {NHP} {q(sam(AN, FR_SA))} {AM} "
          f"{Q(f'{AN} là {SA}')} {NHP}",
          f"{Q(sam(SA, FR_SO))} {AM} {Q(f'{SA} là {SOTA4}')} {NHP}")

    def called(fruit, name, quoted=True):
        nm = f"“{name}”" if quoted else name
        return f"người {SAM} {fruit} {SAID} {nm}"

    def sveva(who, name):
        return f"chính {who} ấy, người ấy là {name}"

    d.seg("5-394",
          *[f"{Q(called(fr, nm))} {AM} {Q(sam(who, fr))} {AM} {Q(sveva(who, nm))} {NHP}"
            for fr, nm, who in ((FR_SO, SO, AR), (FR_SA, SA, AR), (FR_AN, AN, AR), (FR_SO, SO, AN),
                                (FR_SA, SA, AN), (FR_SO, SO, SA))])

    def passed(who, fruit, comma_q=True):
        """Arahā X-phalena samannāgato? Nanu … vītivatto? Hañci … no ca vata re …"""
        return (f"{Q(sam(who, fruit))} {AM} {NANU(f'{who} {VIT} {fruit}')} {AM} "
                f"{hanci_no(f'{who} {VIT} {fruit}', sam(who, fruit))}")

    def passed2(who, fruit, magga, what):
        return (f"{Q(f'{who} {VIT} {fruit}, {TENA_SAM}')} {AM} "
                f"{Q(f'{who} {VIT} {magga}, {VIT} {what}, {TENA_SAM}')} {NHP}")

    d.seg("5-395",
          passed(AR, FR_SO), passed2(AR, FR_SO, MG_SO, S3_AP),
          passed(AR, FR_SA), passed2(AR, FR_SA, MG_SA, OLARIKA),
          passed(AR, FR_AN), passed2(AR, FR_AN, MG_AN, ANU),
          passed(AN, FR_SO), passed2(AN, FR_SO, MG_SO, S3_AP_PE),
          passed(AN, FR_SA), passed2(AN, FR_SA, MG_SA, OLARIKA),
          passed(SA, FR_SO), passed2(SA, FR_SO, MG_SO, S3_AP_PE))

    def keeps(who, n_fr):
        f = f"{NUM[n_fr]} thành quả"
        return (f"{NVQ(sam(who, f))} {AM} {NANU(got(who, f, True))} {AM} {hanci_yes(got(who, f, False), sam(who, f))}")

    def keeps2(who, n, comma2=False):
        f, m = f"{NUM[n]} thành quả", f"{NUM[n]} con đường"
        return (f"{if_q(got(who, f, False), sam(who, f))} {AM} {if_q(got(who, m, comma2), sam(who, m))} {NHP}")

    d.seg("5-396",
          keeps(AR, 4), keeps(AN, 3), keeps(SA, 2),
          keeps2(AR, 4), keeps2(AN, 3), keeps2(SA, 2, comma2=True),
          E(x=KX4))
    # ------------------------------------------------------------ (37) Upekkhā
    for lv, t, sid in heads(5, 37, K(x=KX5)):
        d.head(lv, t, sid)
    six = f"sáu {L10[0]}, sáu {L10[1]}, sáu {L10[2]}… sáu {L10[-1]}"   # chahi phassehi, … saññāhi…pe… paññāhi
    see = (f"{AR}, trong khi {ACT[0]}, thì {', '.join(ACT[1:])}… trong khi {ACT[5]}, thì {', '.join(ACT[:5])}")
    d.seg("5-397",
          f"{Q(sam(AR, UP6))} {AM} {Q(sam(AR, six))} {NHP}",
          f"{Q(sam(AR, UP6))} {AM} {Q(see)} {NHP}",
          f"{Q(sam(AR, UP6))} {AM} "
          f"{Q(f'{ALWAYS}, {SAM}, được kết hợp [{VAR} (Syā.): samāhito] với {UP6}, {UP6} hiện diện')} {NHP}",
          f"{NVQ(sam(AR, UP6))} {AM} {NANU(CHALANGA)} {AM} Nếu {CHALANGA}, {B.TENA_VATA} “{sam(AR, UP6)}”…",
          E(x=KX5))
    # ------------------------------------------------------------ (38) Bodhi
    for lv, t, sid in heads(6, 38, K(x=KX6)):
        d.head(lv, t, sid)
    d.seg("5-398",
          f"{Q(BB)} {AM} {Q('khi sự giác ngộ đã chấm dứt, đã mất đi, đã an tịnh, thì trở thành người không giác ngộ')} "
          f"{NHP}",
          f"{Q(BB)} {AM} {Q(bb(PAST))} {NHP} {q(bb(PAST))} {AM} {Q(K_B)} {NHP}",
          f"{Q(K_B)} {AM} {Q(F_B)} {NHP}",
          f"{Q(BB)} {AM} {Q(bb(FUT))} {NHP}",
          f"{Q(bb(FUT))} {AM} {Q(K_B)} {NHP}",
          f"{Q(K_B)} {AM} {Q(F_B_PE)} {NHP}",
          f"{Q(f'{bb(PRES)}, {K_B}')} {AM} {Q(f'{bb(PAST)}, {K_B}')} {NHP}",
          f"{Q(f'{bb(PRES)}, {F_B}')} {AM} {Q(f'{bb(PAST)}, {F_B_PE}')} {NHP}",
          f"{Q(f'{bb(PRES)}, {K_B}')} {AM} {Q(f'{bb(FUT)}, {K_B}')} {NHP}",
          f"{Q(f'{bb(PRES)}, {F_B_PE}')} {AM} {Q(f'{bb(FUT)}, {F_B_PE}')} {NHP}",
          *[f"{Q(f'{bb(t)}, nhưng không {k}')} {AM} {Q(f'{bb(PRES)}, nhưng không {k}')} {NHP}"
            for t in (PAST, FUT) for k in (K_B, F_B_PE)])
    three = "là bậc giác ngộ nhờ ba sự giác ngộ"                       # tīhi bodhīhi buddho
    d.seg("5-399",
          f"{Q(f'{bb(PAST)}, {bb(FUT)}, {bb(PRES)}')} {AM} {Q(three)} {NHP}",
          f"{Q(three)} {AM} {Q(f'{ALWAYS}, {SAM}, được kết hợp với ba sự giác ngộ, ba sự giác ngộ hiện diện')} {NHP}",
          f"{NVQ(BB)} {AM} {NANU(PATILABHA)} {AM} {hanci_yes(PATILABHA, BB)}",
          f"{if_q(PATILABHA, BB)} {AM} {Q('sự có được sự giác ngộ là sự giác ngộ')} {NHP}",
          E(x=KX6))
    # ------------------------------------------------------------ (39) Lakkhaṇa
    for lv, t, sid in heads(7, 39, K(x=KX7)):
        d.head(lv, t, sid)
    part = {"padesa": ("một phần", "một phần"), "tibhāga": ("một phần ba", "một phần ba"),
            "upaḍḍha": ("một nửa", "một nửa")}
    cv = f"{CVS} {SAM} các tướng, {CVS} là {BS}"
    d.seg("5-400",
          *[f"{Q(LB)} {AM} {Q(f'người {SAM} {a} các tướng là {BS} {b}')} {NHP}" for a, b in part.values()],
          f"{Q(LB)} {AM} {Q(cv)} {NHP}",
          f"{Q(cv)} {AM} {Q(f'{PREV} của {BS} như thế nào, thì {PREV} của {CVS} như thế ấy')} {NHP}")
    cite138 = "[Trường Bộ Kinh 2.27; Trung Bộ Kinh 3.205, hỏi sau khi thấy điều đã được nói]"
    d.seg("5-401",
          f"{like(f'{born(BS)}, {GODS} {cite138}', f'{born(CVS)}, {GODS}')} {NHP}",
          f"{like(f'{born(BS)}, {DEVAPUTTA}', f'{born(CVS)}, {DEVAPUTTA}')} {NHP}",
          f"{like(f'{born(BS)}, {WATER.format(x=BS)}', f'{born(CVS)}, {WATER.format(x=CVS)}')} {NHP}",
          f"{like(STEPS.format(x=BS), STEPS.format(x=CVS))} {NHP}",
          f"{like(f'{born(BS)}, {LIGHT}', f'{born(CVS)}, {LIGHT}')} {NHP}",
          f"{like(BODY.format(x=BS), BODY.format(x=CVS))} {NHP}",
          f"{like(DREAM.format(x=BS), DREAM.format(x=CVS))} {NHP}")
    d.seg("5-402",
          f"{NVQ(LB)} {AM} {B.NANU_VUTTAM} {MAHAPURISA} {B.ATTHEVA} {AM} {TENA_HI(LB)}",
          E(x=KX7))
    # ------------------------------------------------------------ (40) Niyāmokkanti
    for lv, t, sid in heads(8, 40, K(x=KX8)):
        d.head(lv, t, sid)
    SH = "là đệ tử rồi trở thành bậc giác ngộ"                  # sāvako hutvā buddho hoti
    fruits = f"{TREE} bốn {SAMANNA}"
    d.seg("5-403",
          f"Có phải {BOK} không [Trung Bộ Kinh 2.282, hỏi dựa vào Kinh Ga-ti-ka-ra]? {AM} {Q(SAV)} {NHP}",
          f"{Q(SAV)} {AM} {Q(SH)} {NHP}",
          f"{Q(SH)} {AM} {Q(ANUS)} {NHP}",
          f"{Q(ANUS)} {AM} {NANU(SAYAMBHU)} {AM} {hanci_no(SAYAMBHU, ANUS)}",
          f"{Q(BOK)} {AM} {Q(f'{TREE} chỉ ba {SAMANNA}')} {NHP}",
          f"{NANU(fruits)} {AM} {hanci_no(fruits, BOK)}")
    nsav = f"{BOK}, nhưng không phải là đệ tử của {KASS}"        # …, na ca kassapassa bhagavato sāvako
    an_ok = f"{ok(ANANDA, BHAG)}, {ANANDA} là đệ tử của {BHAG}"
    ci_ok = f"{ok(CITTA, BHAG)}, {CITTA} là đệ tử của {BHAG}"
    bs_ok = f"{BOK}, {SAV}"
    d.seg("5-404",
          f"{Q(BOK)} {AM} {Q(f'{BS} {DUKKARA}')} {AM} {Q(f'{DASSANA} có thể làm những việc khổ hạnh khó làm')} "
          f"{NHP}",
          f"{Q(f'{BS} đã làm một khổ hạnh khác [{VAR} (Tương Ưng Bộ Kinh 1.137): amaraṃ tapaṃ], đã {OTHER_T}')} "
          f"{AM} {Q(f'{DASSANA} có thể {OTHER_T}')} {NHP}",
          f"{Q(an_ok)} {AM} {Q(bs_ok)} {NHP}",
          f"{Q(ci_ok)} {AM} {Q(bs_ok)} {NHP}",
          f"{Q(nsav)} {AM} {Q(f'{ok(ANANDA, BHAG)}, nhưng không phải là đệ tử của {BHAG}')} {NHP}",
          f"{Q(nsav)} {AM} {Q(f'{ok(CITTA, BHAG)}, nhưng không phải là đệ tử của {BHAG}')} {NHP}",
          f"{Q(nsav)} {AM} {Q('người đệ tử đã vượt qua lần sinh thì trở thành người không phải là đệ tử')} {NHP}")
    d.seg("5-405",
          f"{NVQ(BOK)} {AM} {B.NANU_VUTTAM} “Này A-nan, Ta đã sống đời sống tu hành trong sạch nơi {KASS} vì sự "
          f"giác ngộ trọn vẹn trong tương lai”! {B.ATTHEVA} {AM} {TENA_HI_NA(BOK)}",
          f"{Q(BOK)} {AM} {B.NANU_VUTTAM}",
          "“Ta là bậc chiến thắng tất cả, bậc biết tất cả,",
          "Không bị vấy bẩn giữa tất cả các hiện tượng;",
          "Đã dứt bỏ tất cả, được giải thoát trong sự diệt tận khao khát,",
          "Sau khi tự mình hiểu biết trực tiếp, Ta sẽ tôn xưng ai?",
          "“Ta không có thầy, người giống như Ta không hiện hữu;",
          "Trong thế gian cùng với chư thiên, không có ai sánh ngang với Ta.",
          "“Thật vậy, Ta là bậc A-la-hán trong thế gian, Ta là bậc đạo sư không có ai cao hơn;",
          "Ta là bậc Tự Giác Ngộ Hoàn Toàn duy nhất, Ta đã trở nên mát mẻ, đã lắng dịu.",
          "“Để chuyển bánh xe Giáo Pháp, Ta đi đến thành của xứ Ca-thi;",
          f"Trong thế gian đã trở nên mù lòa [{SPELL} (Sī., Syā., Kaṃ., Pī.): andhabhūtasmiṃ], Ta sẽ đánh "
          f"[{VAR} (Ka.): āhaññiṃ] tiếng trống bất tử” [{SPELL} (Ka.): dudrabhinti].",
          "“Này hiền giả, theo như ông tự nhận, có phải ông xứng đáng là bậc chiến thắng vô biên không?”",
          "“Những người như Ta quả thật là những bậc chiến thắng, những người đã đạt đến sự diệt tận các ô nhiễm;",
          "Các hiện tượng xấu ác đã bị Ta chiến thắng, vì vậy, này U-pa-ka, Ta là bậc chiến thắng” "
          "[Đại Phẩm 11; Trung Bộ Kinh 1.285; 2.341].",
          f"{B.ATTHEVA} {AM} {TENA_HI_NA(BOK)}",
          f"{Q(BOK)} {AM} {DHAMMACAKKA} {B.ATTHEVA} {AM} {TENA_HI_NA(BOK)}",
          E(x=KX8))
    # ------------------------------------------------------------ (41) Aparāpi samannāgata
    for lv, t, sid in heads(9, 41, KX9_H):
        d.head(lv, t, sid)
    P = {"ar": PAT_AR, "an": PAT_AN, "sa": PAT_SA}

    def ps(k, what):
        return f"{P[k]}, {SAM} {what}"

    d.seg("5-406",
          f"{Q(ps('ar', 'ba thành quả'))} {AM} {Q(ps('ar', ten(4)))} {NHP}",
          f"{Q(ps('an', 'hai thành quả'))} {AM} {Q(ps('an', ten_pe(3, 2)))} {NHP}",
          f"{Q(ps('sa', FR_SO))} {AM} {Q(ps('sa', ten_pe(2, 2)))} {NHP}",
          f"{Q(ps('ar', FR_SO))} {AM} {Q(f'{PAT_AR}, là {SOTA4}')} {NHP}",
          f"{Q(ps('ar', FR_SA))} {AM} {Q(f'{PAT_AR}, là {SA}')} {NHP}",
          f"{Q(ps('ar', FR_AN))} {AM} {Q(f'{PAT_AR}, là {ANA6}')} {NHP}",
          f"{Q(ps('an', FR_SO))} {AM} {Q(f'{PAT_AN}, là {SOTA4}')} {NHP}",
          f"{Q(ps('an', FR_SA))} {AM} {Q(f'{PAT_AN}, là {SA}')} {NHP}",
          f"{Q(ps('sa', FR_SO))} {AM} {Q(f'{PAT_SA}, là {SOTA4}')} {NHP}")
    d.seg("5-407",
          *[f"{Q(called(fr, nm, quoted=False))} {AM} {Q(ps(k, fr))} {AM} {Q(sveva(P[k], nm))} {NHP}"
            for fr, nm, k in ((FR_SO, SO, "ar"), (FR_SA, SA, "ar"), (FR_AN, AN, "ar"), (FR_SO, SO, "an"),
                              (FR_SA, SA, "an"), (FR_SO, SO, "sa"))])

    def ppassed(k, fruit):
        return (f"{Q(ps(k, fruit))} {AM} {NANU(f'{P[k]}, {VIT} {fruit}')} {AM} "
                f"{hanci_no(f'{P[k]}, {VIT} {fruit}', ps(k, fruit))}")

    d.seg("5-408",
          ppassed("ar", FR_SO), passed2(f"{PAT_AR},", FR_SO, MG_SO, S3_AP),
          ppassed("ar", FR_SA), passed2(f"{PAT_AR},", FR_SA, MG_SA, OLARIKA),
          ppassed("ar", FR_AN), passed2(f"{PAT_AR},", FR_AN, MG_AN, ANU))
    d.seg("5-409",
          ppassed("an", FR_SO), passed2(f"{PAT_AN},", FR_SO, MG_SO, S3_AP_PE),
          ppassed("an", FR_SA), passed2(f"{PAT_AN},", FR_SA, MG_SA, OLARIKA))
    d.seg("5-410",
          ppassed("sa", FR_SO), passed2(f"{PAT_SA},", FR_SO, MG_SO, S3_AP_PE))

    def pkeeps(k, what, pron="chúng"):
        return (f"{NVQ(ps(k, what))} {AM} {NANU(got(P[k] + ',', what, True, pron))} {AM} "
                f"{hanci_yes(got(P[k] + ',', what, False, pron), ps(k, what))}")

    d.seg("5-411",
          pkeeps("ar", "ba thành quả"), pkeeps("an", "hai thành quả"), pkeeps("sa", FR_SO, "nó"))

    def pkeeps2(k, fr, m, pron="chúng"):
        return (f"{if_q(got(P[k] + ',', fr, False, pron), ps(k, fr))} {AM} "
                f"{if_q(got(P[k] + ',', m, False), ps(k, m))} {NHP}")

    d.seg("5-412",
          pkeeps2("ar", "ba thành quả", "bốn con đường"),
          pkeeps2("an", "hai thành quả", "ba con đường"),
          pkeeps2("sa", FR_SO, "hai con đường", "nó"),
          KX9_END)
    # ------------------------------------------------------------ (42) Sabbasaṃyojanappahāna
    for lv, t, sid in heads(10, 42, K(x=KX10)):
        d.head(lv, t, sid)
    d.seg("5-413",
          f"{Q(TH10)} {AM} {Q(AMS)} {NHP}",
          f"{Q(AMS)} {AM} {Q(am(THREE))} {NHP}",
          f"{Q(am(THREE))} {AM} {NANU(VB_SO)} {AM} {hanci_no(VB_SO, AMS)}")
    d.seg("5-414", f"{Q(AMS)} {AM} {Q(am(OLARIKA))} {NHP}")
    d.seg("5-415",
          f"{Q(am(OLARIKA))} {AM} {NANU(VB_SA)} {AM} {hanci_no(VB_SA, AMS)}",
          f"{Q(AMS)} {AM} {Q(am(ANU))} {NHP}")
    d.seg("5-416",
          f"{Q(am(ANU))} {AM} {NANU(VB_AN)} {AM} {hanci_no(VB_AN, AMS)}",
          f"{Q(AMS)} {AM} {NANU(VB_AR)} {AM} {hanci_no(VB_AR, AMS)}")
    all_pah = f"đối với {AR}, tất cả các xiềng xích {C2.PAHINA}"   # arahato sabbe saṃyojanā pahīnā (ch3 ANAG frame)
    d.seg("5-417",
          f"{NVQ(TH10)} {AM} {NANU(all_pah)} {AM} {hanci_yes(all_pah, TH10)}",
          E(x=KX10),
          f"{VAGGA4}.",
          C9.TASSUDDANAM,
          UDDANA)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("người tại gia", 2), ("xiềng xích", 1), ("ngay trong đời này", 4), ("đi đến tận cùng của khổ đau", 4),
    ("khi thân tan rã", 2), ("hưởng thụ hành vi dâm dục", 4), ("sự giao hợp", 4), ("vòng hoa, hương thơm, dầu thoa", 4),
    ("vàng và bạc", 1), ("dê và cừu", 4), ("gà và heo", 4), ("voi, bò, ngựa đực và ngựa cái", 4),
    ("sống trong gia đình", 4), ("gia chủ", 2), ("thuộc thế gian", 1), ("con đường A-la-hán", 2),
    ("thành quả A-la-hán", 2), ("y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh", 2),
    ("người phàm phu", 1), ("không còn ô nhiễm", 2), ("được trang bị", 2), ("được trang bị", 4),
    ("sự bình thản", 1), ("liền mạch", 2), ("sự giác ngộ", 2), ("hiện diện", 2),
    ("vua chuyển luân", 2), ("việc thuyết giảng Giáo Pháp", 4), ("chư thiên", 2), ("loài người", 2),
    ("bước vào sự cố định", 4), ("đời sống tu hành trong sạch", 1), ("thành quả của đời sống sa-môn", 1),
    ("bậc đạo sư", 4), ("thành tựu về", 4), ("sự giác ngộ trọn vẹn", 4), ("đã trở nên mát mẻ", 4),
    ("đã lắng dịu", 4), ("sự diệt tận các ô nhiễm", 2), ("các hiện tượng xấu ác", 2), ("khao khát", 1),
    ("hiểu biết trực tiếp", 2), ("rời bỏ gia đình, xuất gia sống đời không gia đình", 4),
    ("những điều chưa từng được nghe trước đây", 4), ("hiểu biết chân thật", 1), ("ánh sáng", 1),
    (B.HOMAGE.split(", ")[2], 1),
    ("Bốn sự thật cao quý – sự thật cao quý về khổ đau, sự thật cao quý về sự phát sinh của khổ đau", 2),
    ("sự thật cao quý về sự chấm dứt khổ đau", 2), ("sự thật cao quý về cách thực hành dẫn đến sự chấm dứt khổ đau", 2),
    ("cần được hiểu biết trọn vẹn", 2), ("cần dứt bỏ", 2), ("cần được tự mình chứng nghiệm", 2),
    ("cần được tu tập", 2), ("không còn sót lại", 1), ("suy yếu", 4), ("sự sinh", 2), ("sự hiện hữu mới", 2),
    ("sự tham đắm cõi hình sắc", 1), ("sự kiêu mạn", 1), ("sự xao động", 1), ("vô minh", 1),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (C2.UC.format(v=""), "2-parihanikatha.md"), (f"{C2.THERA} {ELDERS[0]}", "2-parihanikatha.md"),
    (f"{C2.THERA} {ELDERS[-1]}", "2-parihanikatha.md"), ("trưởng lão Xá-lợi-phất", "2-parihanikatha.md"),
    (AP_M, "2-parihanikatha.md"), (C2.DEV6[-1], "2-parihanikatha.md"),
    ("người tái sinh tối đa bảy lần, người đi từ gia đình này sang gia đình khác, người có một hạt giống",
     "3-brahmacariyakatha.md"),
    (ANA6[len(AN) + 2:], "3-brahmacariyakatha.md"), (PAT_AR, "3-brahmacariyakatha.md"),
    (PAT_SA, "3-brahmacariyakatha.md"), (C3.KR_A, "3-brahmacariyakatha.md"),
    ("cây Bồ-đề", "3-brahmacariyakatha.md"), ("chuyển bánh xe Giáo Pháp", "3-brahmacariyakatha.md"),
    ("can đảm", "3-brahmacariyakatha.md"), ("đã giác ngộ hoàn toàn", "3-brahmacariyakatha.md"),
    (C4.POS_PE, "4-jahatikatha.md"), (C4.NEG_PE5, "4-jahatikatha.md"), (OLARIKA, "4-jahatikatha.md"),
    ("ba sự tiếp xúc, ba cảm giác, ba tri giác, ba chủ ý, ba tâm, ba niềm tin, ba sự tinh tấn, ba sự tỉnh thức, "
     "ba sự định tâm, ba trí tuệ", "4-jahatikatha.md"), ("Cồ-đàm", "4-jahatikatha.md"),
    (f"tự mình chứng nghiệm ba {SAMANNA}", "4-jahatikatha.md"),
    (PG, "5-sabbamatthitikatha.md"), ("trói bằng năm dây trói mà dây thứ năm ở cổ", "5-sabbamatthitikatha.md"),
    ("dao kiếm có thể tác động, lửa có thể tác động", "5-sabbamatthitikatha.md"),
    (f"nhờ hiểu biết ấy mà {FOUR}", "5-sabbamatthitikatha.md"), ("nhờ hiểu biết ấy mà làm được việc của hiểu biết",
                                                                  "5-sabbamatthitikatha.md"),
    ("dùng mắt thuộc quá khứ mà thấy hình sắc thuộc quá khứ", "5-sabbamatthitikatha.md"),
    ("đã vượt qua mọi khổ đau", "5-sabbamatthitikatha.md"), ("tôn giả", "5-sabbamatthitikatha.md"),
    ("được kết hợp với sự tỉnh thức", "8-satipatthanakatha.md"), ("hiện diện", "8-satipatthanakatha.md"),
    ("báu vật bánh xe", "8-satipatthanakatha.md"), ("báu vật vị cố vấn", "8-satipatthanakatha.md"),
    ("có sự xuất hiện của", "8-satipatthanakatha.md"), ("Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("Tóm tắt của chương này –", "9-hevatthikatha.md"),
    ("giống như dựa vào cái cây", "1-puggalakatha.md"), ("Chẳng phải tôn giả A-nan đã nói với Đức Thế Tôn thế này sao",
                                                 "1-puggalakatha.md"),
    ("Đại Phẩm", "2-parihanikatha.md"), ("Tương Ưng Bộ Kinh", "5-sabbamatthitikatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    missing += [(s, f) for s, f in PI5 if s not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch12 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
