# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 10: 10-dutiyavaggo.md (Dutiyavaggo, ^5-10-0 … ^5-353),
the kathā (10) Parūpahāra … (20) Nirodha and the uddāna of the second vagga.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame, and build_2_vi
(finished, read-only) for the arahant formulas shared with chapter 2, so identical Pāli gets byte-identical
Vietnamese. Strings claimed from the pi-1..4 rails are asserted to occur there; strings taken from finished
pi-5 chapters are asserted to occur in those output files; the sample's per-line checks (IDs, dashes,
quotes, NFC, foreign letters) are run against the Pāli. Every Pāli sentence keeps its own sentence.

run:  python -I -X utf8 build_10_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (ch2 arahant formulas: UC, EP, TR, DEV6, dev …)

NAME = "10-dutiyavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
ATTHEVA, NANU_VUTTAM, TENA_HI, TENA_HI_NA = B.ATTHEVA, B.NANU_VUTTAM, B.TENA_HI, B.TENA_HI_NA
NAVQ, TENA_VATA, NO_CA_VATA = B.NA_VATTABBAM_Q, B.TENA_VATA, B.NO_CA_VATA
VAR, SPELL = B.VAR, B.SPELL
KATHA, KATHA_END = B.KATHA, B.KATHA_END
VAGGA2 = B.VAGGA[2]                                    # Dutiyavaggo = «Chương thứ hai» (terms file)


def nanca(p, qq):
    """Hañci P, no ca vata re vattabbe – "Q"ti."""
    return f"Nếu {p}, {NO_CA_VATA} “{qq}”."


def hanci(p, qq, sep=","):
    """Hañci P, tena vata re vattabbe – "Q"ti."""
    return f"Nếu {p}{sep} {TENA_VATA} “{qq}”."


def pair(a, b, end=NHP, ans=AM):
    return f"{Q(a)} {ans} {Q(b)} {end}"


def ifq(x, y):
    """Xti, Yti? (sample frame «Có phải nếu X, thì Y không?»)"""
    return Q(f"nếu {x}, thì {y}")


# ================================================================ persons, arahant formulas (ch2 / ch3)
AR = "bậc A-la-hán"                     # arahā (pi-4)
PU = "người phàm phu"                   # puthujjano (pi-1, ch4)
TASSA = "người ấy"                      # tassa / so
R, D, M = C2.R, C2.D, C2.M              # rāgo, doso, moho (pi-1, ch2)
AO = C2.AO                              # anottappaṃ
ARA_TEN = C2.ARA_TEN                    # doso … anottappaṃ
PAHINA, PAHANAYA, BHAVITA, DEV6 = C2.PAHINA, C2.PAHANAYA, C2.BHAVITA, C2.DEV6
UC0 = C2.UC.format(v="")                # ucchinnamūlo … anuppādadhammo (ch2)
EP, TR, LAST_EP, EP_SHORT = C2.EP, C2.TR, C2.LAST_EP, C2.EP_SHORT
EP_ALL = f"{', '.join(EP)}, {TR}"       # vītarāgo … suvijitavijayo, dukkhaṃ tassa … sacchikataṃ
EP_K = f"{', '.join(EP[:4])}… {LAST_EP}"      # vītarāgo vītadoso vītamoho katakaraṇīyo…pe… sacchikataṃ
EP_NOPE = f"{', '.join(EP[:3])}, {LAST_EP}"   # vītarāgo vītadoso vītamoho sacchikātabbaṃ sacchikataṃ (^5-323)
KR = C2.KR                              # rāgo kāmarāgo … kāmacchandanīvaraṇaṃ (ch2)
KR_PE = "sự tham đắm, sự tham đắm dục lạc, sự ám ảnh của tham đắm dục lạc… chướng ngại ý muốn dục lạc"
MB = f"{BHAVITA} con đường… {BHAVITA} {DEV6[-1]}"   # maggo bhāvito…pe… bojjhaṅgā bhāvitā


def pah_of(x, w):
    return f"{x} của {w} {PAHINA}"


def pah(x):
    return f"{x} {PAHINA}"


def ph(x):
    return f"{PAHANAYA} {x}"


def ten_uc(w):
    """doso pahīno…pe… moho pahīno… māno … ahirikaṃ pahīnaṃ…pe… anottappaṃ pahīnaṃ ucchinnamūlaṃ … (ch2 ^5-260)"""
    return f"{chain([pah_of(ARA_TEN[0], w)] + [pah(i) for i in ARA_TEN[1:]])}, {UC0}"


def dmao(w):
    """doso pahīno…pe… moho pahīno…pe… anottappaṃ pahīnaṃ"""
    return chain([pah_of(D, w), pah(M), pah(AO)])


def tail(x, neg=False):
    return f"người ấy {'không ' if neg else ''}có {x}"


# ================================================================ the eight objects of doubt (pi-1 ^1-1008)
OBJ8 = ["về Bậc Đạo Sư", "về Giáo Pháp", "về Tăng đoàn", "về sự tu học", "về quá khứ", "về tương lai",
        "về quá khứ và tương lai",
        "về quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện"]
# satthari dhamme saṅghe sikkhāya pubbante aparante pubbantāparante idappaccayatāpaṭiccasamuppannesu dhammesu


def full8(n):
    return ", ".join(f"{n} {o}" for o in OBJ8)


def pe8(n, k):
    """first k items…pe… last item"""
    return f"{', '.join(f'{n} {o}' for o in OBJ8[:k])}… {n} {OBJ8[-1]}"


# ================================================================ (10) Parūpahārakathā
AS = "sự xuất tinh bất tịnh"            # asuci sukkavissaṭṭhi
T10 = f"{AR} có {AS}"                   # atthi arahato asuci sukkavissaṭṭhi
PARUPAHARA = "việc người khác đưa đến"  # parūpahāro (terms file heading)
MK = "các vị thiên thuộc nhóm Ma vương"  # mārakāyikā devatā (Māra = Ma vương, sample)
UPA = f"{MK} đưa {AS} đến cho {AR}"     # mārakāyikā devatā arahato asuciṃ sukkavissaṭṭhiṃ upasaṃharanti
V = "sự phân vân"                       # vimati (pi-1)
TV = f"{AR} có {V}"
EAT = "những gì đã ăn, đã uống, đã nhai, đã nếm"   # asitapītakhāyitasāyita (pi-2)
NIS = f"{AS} của {AR} là thứ tiết ra từ {EAT}"     # arahato asuci … asitapītakhāyitasāyitassa nissando
EAT4 = "ăn, uống, nhai, nếm"            # asanti pivanti khādanti sāyanti
ALL_EAT = f"bất cứ ai {EAT4}, tất cả những người ấy đều có {AS}"
UP = f"phân và nước tiểu của {AR} là thứ tiết ra từ {EAT}"   # arahato uccārapassāvo … nissando
ASAYA = "nó có chỗ chứa"                # atthi tassa āsayo (tassa = of the semen, aṭṭhakathā ^5-309)
NASAYA = "nó không có chỗ chứa"
NOT3 = f"{MK} không đưa đến {AS} của chính mình, cũng không của những người khác, cũng không của người ấy"
# mārakāyikā devatā neva attano na aññesaṃ na tassa asuciṃ sukkavissaṭṭhiṃ upasaṃharanti
YES3 = f"{MK} đưa {AS} của chính mình đến, đưa {AS} của những người khác đến, đưa {AS} của người ấy đến"


def meth(w, neg=False, var=""):
    """methunaṃ dhammaṃ paṭiseveyya … jātarūparajataṃ sādiyeyya (na ca …)"""
    v = "không thể" if neg else "có thể"
    return (f"{w} {v} hưởng thụ hành vi dâm dục, làm phát sinh chuyện dâm dục{var}, sống trên chiếc giường chật "
            "chội vì con cái, hưởng dùng gỗ đàn hương xứ Ca-thi, mang vòng hoa, hương thơm, dầu thoa, nhận vàng bạc")


SK = "bậc A-la-hán thông thạo các hiện tượng của mình"       # sadhammakusalo arahā (aṭṭhakathā: his own arahatta)
PK = "bậc A-la-hán thông thạo các hiện tượng của người khác"  # paradhammakusalo arahā
REQ = "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh"   # cīvara … parikkhāra (pi-2)
FR4 = "thành quả vào dòng, hay thành quả trở lại một lần, hay thành quả không trở lại, hay trạng thái A-la-hán"
FR4_LOC = ("về thành quả vào dòng, hay về thành quả trở lại một lần, hay về thành quả không trở lại, hay về trạng "
           "thái A-la-hán")


def sadhamma(x):
    """the sadhamma / paradhamma opening (^5-312 …): lines 1-2 (x = the noun)"""
    sk_has, pk_has = f"{SK} có {x}", f"{PK} có {x}"
    sk_no, pk_no = f"{SK} không có {x}", f"{PK} không có {x}"
    return [f"{Q(f'{AR} có {x}')} {cap(sk_has)}, {pk_no}. {pair(sk_has, pk_has)}",
            pair(pk_no, sk_no)]


# ================================================================ (11) Aññāṇa / (12) Kaṅkhā / (13) Paravitāraṇā
ANN = "sự không biết"                   # aññāṇaṃ (pi-1)
T11 = f"{AR} có {ANN}"
AV = ("vô minh, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh, xiềng xích "
      "vô minh, chướng ngại vô minh")   # avijjā avijjogho … avijjānīvaraṇaṃ (pi-1, pi-2)
CRIMES = ["sát hại sinh mạng", "lấy của không được cho", "nói dối", "nói lời chia rẽ", "nói lời thô ác",
          "nói lời phù phiếm", "đột nhập nhà", "cướp bóc", "cướp một ngôi nhà", "mai phục bên đường",
          "đi lại với vợ người khác", "cướp phá làng", "cướp phá thị trấn"]
# pāṇaṃ haneyya … nigamaghātaṃ kareyya (the first six as pi-4 / ch3)
APK = "bị sự không biết chi phối"       # aññāṇapakato


def crimes(w, k=None, neg=False):
    lst = ", ".join(CRIMES) if k is None else f"{', '.join(CRIMES[:k])}… {', '.join(CRIMES[-2:])}"
    return f"{w}, {APK}, {'không thể' if neg else 'có thể'} {lst}"


NAMES = ("có thể không biết tên và họ của những người nữ, người nam, có thể không biết đường đúng và đường sai, "
         "có thể không biết tên của cỏ, gỗ và cây rừng")
# itthipurisānaṃ nāmagottaṃ na jāneyya, maggāmaggaṃ na jāneyya, tiṇakaṭṭhavanappatīnaṃ nāmaṃ na jāneyya
KA = "sự nghi ngờ"                      # kaṅkhā (pi-1; terms file heading)
T12 = f"{AR} có {KA}"
VC = "sự hoài nghi, sự ám ảnh của hoài nghi, xiềng xích hoài nghi, chướng ngại hoài nghi"
# vicikicchā vicikicchāpariyuṭṭhānaṃ vicikicchāsaṃyojanaṃ vicikicchānīvaraṇaṃ (pi-1)
KNAMES = ("có thể nghi ngờ về tên và họ của những người nữ, người nam, có thể nghi ngờ về đường đúng và đường sai, "
          "có thể nghi ngờ về tên của cỏ, gỗ và cây rừng")
PV = "việc được người khác giảng giải"  # paravitāraṇā (pare vitaranti … ācikkhanti, aṭṭhakathā ^5-251)
T13 = f"{AR} có {PV}"
PN = ("phải được người khác dẫn dắt, phải tin vào người khác, phải dựa vào người khác, bị lệ thuộc vào người "
      "khác, không biết, không thấy, mê mờ, không hiểu biết rõ ràng")
NPN = ("không phải được người khác dẫn dắt, không phải tin vào người khác, không phải dựa vào người khác, không "
       "bị lệ thuộc vào người khác, biết, thấy, không mê mờ, hiểu biết rõ ràng")
# paraneyyo parapattiyo parapaccayo parapaṭibaddhabhū, na jānāti na passati sammūḷho asampajāno (sampajāna pi-2)
VNAMES = ("người khác có thể giảng giải cho bậc A-la-hán tên và họ của những người nữ, người nam, người khác có "
          "thể giảng giải đường đúng và đường sai, người khác có thể giảng giải tên của cỏ, gỗ và cây rừng")

# ---------------------------------------------------------------- sutta passages (^5-317 …)
JP_HEAD = ("Này các tỳ-khưu, Ta nói sự diệt tận các ô nhiễm là cho người biết{v}, cho người thấy, không phải cho "
           "người không biết, không phải cho người không thấy{e}")
# jānatohaṃ, bhikkhave, passato āsavānaṃ khayaṃ vadāmi, no ajānato no apassato. / !
KINCA = "Và này các tỳ-khưu, đối với người biết điều gì, người thấy điều gì, thì có sự diệt tận các ô nhiễm?"
JP = "đối với người biết, người thấy, thì có sự diệt tận các ô nhiễm"          # jānato passato āsavānaṃ khayo hoti
EVAM = "này các tỳ-khưu, đối với người biết như vậy, người thấy như vậy, thì có sự diệt tận các ô nhiễm"
# evaṃ kho, bhikkhave, jānato evaṃ passato āsavānaṃ khayo hoti
ITI5 = ("‘Đây là vật chất, đây là sự phát sinh của vật chất, đây là sự biến mất của vật chất, đây là cảm giác… "
        "đây là tri giác… đây là các tạo tác… đây là thức, đây là sự phát sinh của thức, đây là sự biến mất của "
        "thức’")
ITI5_PE = "‘Đây là vật chất’… ‘đây là sự biến mất của thức’"
S4 = ["‘Đây là khổ đau’", "‘đây là sự phát sinh của khổ đau’", "‘đây là sự chấm dứt khổ đau’",
      "‘đây là cách thực hành dẫn đến sự chấm dứt khổ đau’"]   # (pi-2 ^2-189 truth names)
SAB = ("Này các tỳ-khưu, người không hiểu biết trực tiếp, không hiểu biết trọn vẹn, không làm phai nhạt, không "
       "dứt bỏ tất cả thì không thể đi đến sự diệt tận khổ đau{s} và này các tỳ-khưu, người hiểu biết trực tiếp, "
       "hiểu biết trọn vẹn, làm phai nhạt, dứt bỏ tất cả thì có thể đi đến sự diệt tận khổ đau")
SAHAVASSA = ["“Ngay cùng với sự thành tựu thấy chân lý của người ấy,", "Ba hiện tượng được dứt bỏ;",
             "Quan điểm về tự ngã và sự hoài nghi,", "Cùng bất cứ giới hạnh và nghi thức nào còn có;",
             "Người ấy được giải thoát khỏi bốn cõi khổ,", "Không thể làm sáu trọng tội”."]   # ch3 ^5-278
SAHA_PE = "“ngay cùng với sự thành tựu thấy chân lý của người ấy… không thể làm sáu trọng tội”"
DHC = ("“Này các tỳ-khưu, vào lúc mà nơi vị đệ tử cao quý, con mắt Giáo Pháp không bụi bặm, không cấu uế sinh "
       "khởi – ‘bất cứ điều gì có bản chất phát sinh, tất cả điều ấy đều có bản chất chấm dứt’, này các tỳ-khưu, "
       "cùng với sự sinh khởi của sự thấy, nơi vị đệ tử cao quý, ba xiềng xích được dứt bỏ – quan điểm về tự ngã, "
       "sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức”")          # ch3 ^5-278, byte-identical
DHP239 = ["“Người trí, dần dần theo thứ tự, từng chút một, trong từng khoảnh khắc;",
          "Như người thợ luyện bạc, hãy gột sạch cấu uế của chính mình” [Kinh Pháp Cú 239, trong Kinh Pháp Cú]."]

# ================================================================ (14) Vacībhedakathā
SAM = "người đang nhập thành tựu thiền"          # samāpanno (samāpatti «thành tựu thiền» pi-2)
VB = "sự phát ra lời nói"                        # vacībhedo
KB = "sự phát ra cử động thân"                   # kāyabhedo (aṭṭhakathā: kāyaviññatti)
T14 = f"{SAM} có {VB}"
KAS = ["đề mục bao trùm là đất", "đề mục bao trùm là nước", "đề mục bao trùm là lửa", "đề mục bao trùm là gió",
       "đề mục bao trùm màu xanh", "đề mục bao trùm màu vàng", "đề mục bao trùm màu đỏ",
       "đề mục bao trùm màu trắng"]               # pathavī … odātakasiṇa (pi-1)
ARU = ["lĩnh vực không gian vô tận", "lĩnh vực thức vô tận", "lĩnh vực không có gì cả",
       "lĩnh vực không phải tri giác cũng không phải không tri giác"]   # (pi-2)
J = ["tầng thiền thứ nhất", "tầng thiền thứ hai", "tầng thiền thứ ba", "tầng thiền thứ tư"]   # (pi-1)
LKY, LKT = "thuộc thế gian", "vượt thế gian"    # lokiya / lokuttara (pi-1 matrix)
VK = "sự hướng tâm và sự duy trì tâm"            # vitakkavicārā (pi-1)
NIRS = "sự chấm dứt tri giác và cảm giác"        # saññāvedayitanirodha (pi-2)
SV = "tri giác và cảm giác"                      # saññā ca vedanā ca


def sam(x):
    return f"người đang nhập {x}"


def jl(i, lk=LKY):
    return f"{J[i]} {lk}"


VS = f"Đức Thế Tôn đã nói rằng {VK} là các sự tạo tác bằng lời nói"   # vitakkavicārā vacīsaṅkhārā vuttā bhagavatā
VSM = "Đức Thế Tôn đã nói rằng lời nói có nguồn gốc từ sự hướng tâm"  # vitakkasamuṭṭhānā vācā vuttā bhagavatā
SSM = "Đức Thế Tôn đã nói rằng lời nói có nguồn gốc từ tri giác"      # saññāsamuṭṭhānā vācā vuttā bhagavatā
J1V = f"{sam(J[0])} có {VK}"                    # paṭhamaṃ jhānaṃ samāpannassa atthi vitakkavicārā
SN13 = "Tương Ưng Bộ Kinh 4.259, 263"
NIR1 = f"đối với {sam(J[0])}, lời nói đã chấm dứt"     # paṭhamaṃ jhānaṃ samāpannassa vācā niruddhā hoti
KT = "cái gai"                                   # kaṇṭako


def kt(x, j):
    return f"Đức Thế Tôn đã nói rằng {x} là {KT} của {j}"


def kta(a, x):
    return f"Đức Thế Tôn đã nói rằng đối với {sam(a)}, {x} là {KT}"


# ================================================================ (15)-(16)
DK = "việc nêu lên khổ đau"                      # dukkhāhāro
T15 = f"{DK} là chi phần của con đường, thuộc về con đường"   # maggaṅgaṃ maggapariyāpannaṃ
SAY = "nói ra lời là khổ đau"                    # dukkhanti vācaṃ bhāsati
BALA = "những người phàm phu ngu si"             # bālaputhujjanā
KILLERS = ["kẻ giết mẹ", "kẻ giết cha", "kẻ giết bậc A-la-hán", "kẻ làm chảy máu", "kẻ chia rẽ Tăng đoàn"]
# mātughātako … ruhiruppādako … saṅghabhedako (ch3 words; «Như Lai» not added: not in the Pāli, coordinator rule)
CT = "sự duy trì của tâm"                        # cittaṭṭhiti (tiṭṭhati «duy trì» sample)
ONE = "một tâm"                                  # ekaṃ cittaṃ
DUR = ["bốn ngày", "tám ngày", "mười ngày", "hai mươi ngày", "một tháng", "hai tháng", "bốn tháng", "tám tháng",
       "mười tháng", "một năm", "hai năm", "bốn năm", "tám năm", "mười năm", "hai mươi năm", "ba mươi năm",
       "bốn mươi năm", "năm mươi năm", "một trăm năm", "hai trăm năm", "bốn trăm năm", "năm trăm năm",
       "một nghìn năm", "hai nghìn năm", "bốn nghìn năm", "tám nghìn năm", "mười sáu nghìn năm", "một kiếp",
       "hai kiếp", "bốn kiếp", "tám kiếp", "mười sáu kiếp", "ba mươi hai kiếp", "sáu mươi bốn kiếp",
       "năm trăm kiếp", "hàng nghìn kiếp", "hai nghìn kiếp", "bốn nghìn kiếp", "tám nghìn kiếp",
       "mười sáu nghìn kiếp", "hai mươi nghìn kiếp", "bốn mươi nghìn kiếp", "sáu mươi nghìn kiếp",
       "tám mươi bốn nghìn kiếp"]
# cattāro divase … caturāsīti kappasahassāni (^5-335; "kappasahassāni" without a number rendered as written)
DUR2 = ["năm trăm năm", "một nghìn năm", "hai nghìn năm", "bốn nghìn năm", "tám nghìn năm", "mười sáu nghìn năm",
        "một phần ba của kiếp", "nửa kiếp", "một kiếp", "hai kiếp", "bốn kiếp", "tám kiếp", "mười sáu kiếp",
        "ba mươi hai kiếp", "sáu mươi bốn kiếp", "năm trăm kiếp", "một nghìn kiếp", "hai nghìn kiếp",
        "bốn nghìn kiếp", "tám nghìn kiếp"]
# pañca vassasatāni … aṭṭha kappasahassāni (^5-337; kappassa tatiyo bhāgo / upaḍḍhakappo pi-2)


def stay(x):
    return f"duy trì suốt {x}"


DEVAS = ["Tứ Đại Thiên Vương", "Ba Mươi Ba", "Dạ Ma", "Đâu Suất", "Hóa Lạc", "Tha Hóa Tự Tại", "Phạm Chúng",
         "Phạm Phụ", "Đại Phạm", "Thiểu Quang", "Vô Lượng Quang", "Quang Âm", "Thiểu Tịnh", "Vô Lượng Tịnh",
         "Biến Tịnh", "Quảng Quả", "Vô Phiền", "Vô Nhiệt", "Thiện Hiện", "Thiện Kiến", "Sắc Cứu Cánh"]   # (pi-2)
AKD = "chư thiên sinh vào lĩnh vực không gian vô tận"   # ākāsānañcāyatanūpagā devā (pi-2)
AYU = "tuổi thọ"                                         # āyuppamāṇaṃ (pi-2)
SENSES = [("mắt", "thấy", "hình sắc"), ("tai", "nghe", "âm thanh"), ("mũi", "ngửi", "mùi"), ("lưỡi", "nếm", "vị"),
          ("thân", "chạm", "vật xúc chạm"), ("ý", "nhận biết", "đối tượng của ý")]   # (ch5 ORG / VERB / OBJ)


def sense(i):
    o, v, x = SENSES[i]
    return f"dùng {o} {v} {x}"


# ================================================================ (17) Kukkuḷakathā
KUK = "tro nóng"                                 # kukkuḷa
KK = f"tất cả các tạo tác, không trừ ra phần nào, đều là {KUK}"   # sabbe saṅkhārā anodhiṃ katvā kukkuḷā
SUKHA = ["cảm giác dễ chịu", "hạnh phúc thuộc thân", "hạnh phúc thuộc tâm", "hạnh phúc cõi trời",
         "hạnh phúc cõi người", "hạnh phúc do lợi lộc", "hạnh phúc do được kính trọng", "hạnh phúc do xe cộ",
         "hạnh phúc do giường nằm", "hạnh phúc do quyền uy", "hạnh phúc do quyền thống trị",
         "hạnh phúc của người tại gia", "hạnh phúc của đời sống sa-môn", "hạnh phúc còn ô nhiễm",
         "hạnh phúc không còn ô nhiễm", "hạnh phúc còn chấp trước", "hạnh phúc không còn chấp trước",
         "hạnh phúc có tính trần tục", "hạnh phúc không có tính trần tục", "hạnh phúc có sự hân hoan",
         "hạnh phúc không có sự hân hoan", "hạnh phúc của tầng thiền", "hạnh phúc của sự giải thoát",
         "hạnh phúc dục lạc", "hạnh phúc của sự xuất ly", "hạnh phúc của sự tách biệt",
         "hạnh phúc của sự an tịnh", "hạnh phúc của sự giác ngộ"]
# sukhā vedanā, kāyikaṃ sukhaṃ … sambodhasukhaṃ (dibbaṃ / mānusakaṃ sukhaṃ sample; sāmisa pi-2)
SOKA = "sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng"   # (pi-2, ch4)
DNEG = ("có quả không đáng mong muốn, có quả không đáng yêu thích, có quả không vừa ý, có quả bị pha tạp, đưa "
        "đến khổ đau, có kết quả khổ đau")     # aniṭṭhaphalaṃ … dukkhavipākaṃ
DPOS = ("có quả đáng mong muốn, có quả đáng yêu thích, có quả vừa ý, có quả không pha tạp, đưa đến hạnh phúc, "
        "có kết quả hạnh phúc")                 # iṭṭhaphalaṃ … sukhavipākaṃ
MER4 = "giới hạnh… sự hành trì ngày trai giới… sự tu tập… đời sống tu hành trong sạch"   # sīlaṃ … brahmacariyaṃ

# ================================================================ (18) Anupubbābhisamayakathā
AB = "sự thấu hiểu tuần tự"                      # anupubbābhisamayo (abhisamaya «sự thấu hiểu» ch4)
T18 = f"có {AB}"                                 # (ch5 «có» for the bare noun thesis)
TUAN = "một cách tuần tự"                        # anupubbena
PAT = {"sota": "người đang thực hành để tự mình chứng nghiệm thành quả vào dòng",
       "saka": "người đang thực hành để tự mình chứng nghiệm thành quả trở lại một lần",
       "ana": "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại",
       "ara": "người đang thực hành để tự mình chứng nghiệm trạng thái A-la-hán"}   # (pi-4, ch3)
DS = {"dukkha": "bằng việc thấy khổ đau", "samudaya": "bằng việc thấy sự phát sinh",
      "nirodha": "bằng việc thấy sự chấm dứt", "magga": "bằng việc thấy con đường"}   # (ch3)
KIM = "người ấy dứt bỏ điều gì?"
JA = "Người ấy dứt bỏ"
TDK = "các phiền não cùng hiện diện với chúng"   # (pi-1, ch3)
S3 = "quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức"
CB = "một phần tư"                               # catubhāgaṃ
SILA = "có các giới hạnh được các bậc thánh yêu quý"
NA_SILA = "không có các giới hạnh được các bậc thánh yêu quý"
UDDHAM = "người theo dòng đi lên đến cõi Sắc Cứu Cánh"   # (pi-4, ch3)
PARI4 = ("người nhập Niết-bàn trọn vẹn trong khoảng giữa… người nhập Niết-bàn trọn vẹn khi gần mạng chung… "
         "người nhập Niết-bàn trọn vẹn không có sự thúc đẩy… người nhập Niết-bàn trọn vẹn có sự thúc đẩy")


def ask(stage, ds):
    return f"{cap(PAT[stage])}, {ds}, dứt bỏ điều gì?"


def part_a(name):
    return f"{CB} là {name}, {CB} không phải là {name}"


def part_b(phala):
    return (f"{CB} đã đạt đến {phala}, đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an trú, "
            f"chạm đến bằng thân rồi an trú, {CB} không chạm đến bằng thân rồi an trú")


SOTA_X = (f"{CB} là người tái sinh tối đa bảy lần, người đi từ gia đình này sang gia đình khác, người có một hạt "
          f"giống, có niềm tin trong sáng không lay chuyển nơi Đức Phật, nơi Giáo Pháp… nơi Tăng đoàn… {SILA}, "
          f"{CB} {NA_SILA}")   # (ch3 SOTA_X with «một phần tư»)
PP = "người đang thực hành"                      # paṭipannako
PHT = "người đã đứng vững trong thành quả"       # phale ṭhito (ṭhita pi-4)
DK2 = "trong khi thấy sự phát sinh… trong khi thấy sự chấm dứt, nên được gọi là người đang thực hành"
# samudayaṃ dakkhanto…pe… nirodhaṃ dakkhanto paṭipannakoti vattabbo


def dk(x):
    return f"trong khi thấy {x}, nên được gọi là {PP}"


def phx(x):
    return f"khi {x} đã được thấy, nên được gọi là {PHT}"


def nph(x):
    return f"khi {x} đã được thấy, không nên nói – “nên được gọi là {PHT}”"


PSK = "[dấu hiệu câu hỏi của người theo học thuyết của chúng ta]"   # [sakavādīpucchālakkhaṇaṃ]
PPK = "[dấu hiệu câu hỏi của người theo học thuyết khác]"           # [paravādīpucchālakkhaṇaṃ]

# ================================================================ (19) Vohārakathā / (20) Nirodhakathā
VOHARA = "lời nói"                               # vohāro (heading)
VH = "lời nói của Đức Phật, Đức Thế Tôn"         # buddhassa bhagavato vohāro
T19 = f"{VH} {LKT}"
VL = f"{VH} khi nói về điều {LKY} thì {LKY}, khi nói về điều {LKT} thì {LKT}"
# vohāro lokiyaṃ voharantassa lokiyo hoti, lokuttaraṃ voharantassa lokuttaro hoti
LD = f"hiện tượng {LKT}"                         # lokuttaro dhammo
BOTH = f"cả hiện tượng {LKY} lẫn hiện tượng {LKT}"   # lokiyampi lokuttarampi dhammaṃ
NIR = "sự chấm dứt"                              # nirodho
T20 = f"có hai {NIR}"                            # dve nirodhā
PS = "do suy xét"                                # paṭisaṅkhā
NPS = "không do suy xét"                         # appaṭisaṅkhā
TASSUDDANAM = "Tóm tắt của chương này –"         # Tassuddānaṃ – (ch9, coordinator: byte for byte)


# ================================================================ chapter builder
def build():
    d = B.Doc()
    d.head(3, VAGGA2, "5-10-0")
    # ------------------------------------------------------------ (10) Parūpahārakathā
    d.head(4, f"(10) 1. {KATHA.format(x=PARUPAHARA)}", "5-10-1-0")
    d.seg("5-307",
          pair(T10, f"{AR} có {KR}"),
          f"{Q(f'{AR} không có {KR}')} {AM} {nanca(f'{AR} không có {KR}', T10)}",
          pair(f"{PU} có {AS}, {tail(KR)}", f"{AR} có {AS}, {tail(KR_PE)}"),
          pair(f"{AR} có {AS}, {tail(KR_PE, True)}", f"{PU} có {AS}, {tail(KR_PE, True)}"),
          f"{Q(T10)} {AM} Theo nghĩa nào? Vì {UPA}.",
          f"{Q(UPA)} {AM} {Q(f'{MK} có {AS}')} {NHP}",
          f"{Q(f'{MK} không có {AS}')} {AM} {nanca(f'{MK} không có {AS}', UPA)}",
          pair(UPA, YES3),
          f"{Q(NOT3)} {AM} {nanca(NOT3, UPA)}",
          pair(UPA, "đưa đến qua các lỗ chân lông"))
    d.seg("5-308",
          f"{Q(UPA)} {AM} Vì lý do gì? Vì chúng ta sẽ gieo {V}. {Q(TV)} {NHP}",
          pair(TV, f"{AR} có {full8(V)}"),
          f"{Q(f'{AR} không có {full8(V)}')} {AM} {nanca(f'{AR} không có {pe8(V, 1)}', TV)}",
          pair(f"{PU} có {V}, {tail(pe8(V, 1))}", f"{AR} có {V}, {tail(pe8(V, 1))}"),
          pair(f"{AR} có {V}, {tail(pe8(V, 1), True)}", f"{PU} có {V}, {tail(pe8(V, 1), True)}"),
          f"{Q(T10)} {AM} {cap(AS)} của {AR} là thứ tiết ra từ cái gì? Là thứ tiết ra từ {EAT}. "
          f"{Q(NIS)} {AM} {Q(ALL_EAT)} {NHP}",
          pair(ALL_EAT, f"trẻ em {EAT4}, trẻ em có {AS}", NH),
          f"{Q(f'những người ái nam ái nữ {EAT4}, những người ái nam ái nữ có {AS}')} {NHP}",
          f"{Q(f'chư thiên {EAT4}, các vị thiên có {AS}')} {NHP}")
    d.seg("5-309",
          pair(NIS, ASAYA),
          pair(f"{UP}, {ASAYA}", f"{NIS}, {ASAYA}"),
          pair(f"{NIS}, {NASAYA}", f"{UP}, {NASAYA}"))
    d.seg("5-310",
          pair(T10, meth(AR, var=f" [{VAR} (Sī., Syā.): methunaṃ dhammaṃ uppādeyya]"), NH),
          pair(f"{PU} có {AS}, {meth(PU)}", f"{AR} có {AS}, {meth(AR)}"),
          pair(f"{AR} có {AS}, nhưng {meth(AR, True)}", f"{PU} có {AS}, nhưng {meth(PU, True)}", NH),
          f"{Q(T10)} {AM} {NANU(f'{pah_of(R, AR)}, {UC0}')} {AM} {nanca(f'{pah_of(R, AR)}, {UC0}', T10)}",
          f"{Q(T10)} {AM} {NANU(ten_uc(AR))} {AM} {nanca(f'{pah_of(AO, AR)}, {UC0}', T10)}")
    d1 = C2.dev(AR, [R], ["con đường"])
    d6 = C2.dev(AR, [R], DEV6)
    d6b = C2.dev(AR, [R], [DEV6[-1]])
    dx = C2.dev(AR, [D, M, AO], ["con đường", DEV6[-1]])
    dxb = C2.dev(AR, [AO], [DEV6[-1]])
    d.seg("5-311",
          f"{Q(T10)} {AM} {NANU(d1)} {AM} {nanca(d1, T10)}",
          f"{Q(T10)} {AM} {NANU(d6)} {AM} {nanca(d6b, T10)}",
          f"{Q(T10)} {AM} {NANU(dx)} {AM} {nanca(dxb, T10)}",
          f"{Q(T10)} {AM} {NANU(f'{AR} {EP_ALL}')} {AM} {nanca(f'{AR} {EP_K}', T10)}")
    sk_dev = f"{ph(R)}, {SK} {MB}… {ph(D)}… {ph(M)}… {ph(AO)}, {MB}"
    pk_dev = f"{ph(R)}, {PK} {MB}… {ph(D)}… {ph(M)}… {ph(AO)}, {MB}"
    d.seg("5-312",
          *sadhamma(AS),
          pair(f"{pah_of(R, SK)}, {tail(AS)}", f"{pah_of(R, PK)}, {tail(AS)}"),
          pair(f"{dmao(SK)}, {tail(AS)}", f"{pah_of(AO, PK)}, {tail(AS)}"),
          pair(f"{sk_dev}, {tail(AS)}", f"{C2.dev(PK, [AO], [DEV6[-1]])}, {tail(AS)}"),
          pair(f"{SK} {EP_SHORT}, {tail(AS)}", f"{PK} {EP_SHORT}, {tail(AS)}"),
          pair(f"{pah_of(R, PK)}, {tail(AS, True)}", f"{pah_of(R, SK)}, {tail(AS, True)}"),
          pair(f"{dmao(PK)}, {tail(AS, True)}", f"{pah_of(AO, SK)}, {tail(AS, True)}"),
          pair(f"{pk_dev}, {tail(AS, True)}", f"{C2.dev(SK, [AO], [DEV6[-1]])}, {tail(AS, True)}"),
          pair(f"{PK} {EP_SHORT}, {tail(AS, True)}", f"{SK} {EP_SHORT}, {tail(AS, True)}"))
    sutta = ("“Này các tỳ-khưu, những vị [dị bản (Sī.): ye keci] tỳ-khưu là người phàm phu, thành tựu giới hạnh, "
             "tỉnh thức và hiểu biết rõ ràng mà đi vào giấc ngủ, thì đồ bất tịnh của họ không thoát ra. Này các "
             "tỳ-khưu, ngay cả những vị ẩn sĩ bên ngoài đã lìa tham đắm đối với các dục lạc, thì đồ bất tịnh của họ "
             "cũng không thoát ra. Này các tỳ-khưu, đây là điều không thể xảy ra, không có cơ hội, rằng đồ bất tịnh "
             "của bậc A-la-hán có thể thoát ra” [Đại Phẩm 353, tương đồng về ý nghĩa; cần xem Tăng Chi Bộ Kinh 5.210].")
    upa_req = f"người khác có thể đưa đến cho {AR} {REQ}"
    has_pu = f"{AR} có {PARUPAHARA}"
    d.seg("5-313",
          f"{Q(T10)} {AM} {NANU_VUTTAM} {sutta} {ATTHEVA} {AM} {TENA_HI_NA(T10)}",
          f"{NAVQ(has_pu)} {AM} {NANU(upa_req)} {AM} {hanci(upa_req, has_pu)}",
          f"{ifq(upa_req, has_pu)} {AM} {Q(f'người khác có thể đưa đến cho {AR} {FR4}')} {NHP}",
          KATHA_END.format(x=PARUPAHARA))
    # ------------------------------------------------------------ (11) Aññāṇakathā
    d.head(4, VAGGA2, "5-10-2-0")
    d.head(5, f"(11) 2. {KATHA.format(x=ANN)}", "5-10-2-1-0")
    d.seg("5-314",
          f"{pair(T11, f'{AR} có {AV}', NH)} {Q(f'{AR} không có {AV}')} {AM} {nanca(f'{AR} không có {AV}', T11)}",
          pair(f"{PU} có {ANN}, {tail(AV)}", f"{AR} có {ANN}, {tail(AV)}", NH),
          pair(f"{AR} có {ANN}, {tail(AV, True)}", f"{PU} có {ANN}, {tail(AV, True)}", NH),
          pair(T11, crimes(AR), NH),
          pair(f"{PU} có {ANN}, {crimes(PU, 3)}", f"{AR} có {ANN}, {crimes(AR, 2)}", NH),
          pair(f"{AR} có {ANN}, nhưng {crimes(AR, 2, True)}", f"{PU} có {ANN}, nhưng {crimes(PU, 2, True)}", NH),
          pair(T11, f"{AR} có {full8(ANN)}", NH),
          f"{Q(f'{AR} không có {full8(ANN)}')} {AM} {nanca(f'{AR} không có {pe8(ANN, 3)}', T11)}",
          pair(f"{PU} có {ANN}, {tail(pe8(ANN, 3))}", f"{AR} có {ANN}, {tail(pe8(ANN, 3))}", NH),
          pair(f"{AR} có {ANN}, {tail(pe8(ANN, 3), True)}", f"{PU} có {ANN}, {tail(pe8(ANN, 3), True)}", NH))
    d6r = C2.dev(AR, [R], ["con đường", DEV6[-1]])
    d.seg("5-315",
          f"{Q(T11)} {AM} {NANU(f'{pah_of(R, AR)}, {UC0}')} {AM} {nanca(f'{pah_of(R, AR)}, {UC0}', T11)}",
          f"{Q(T11)} {AM} {NANU(f'{dmao(AR)}, {UC0}')} {AM} {nanca(f'{pah_of(AO, AR)}, {UC0}', T11)}",
          f"{Q(T11)} {AM} {NANU(d6r)} {AM} {nanca(d6b, T11)}",
          f"{Q(T11)} {AM} {NANU(dx)} {AM} {nanca(dxb, T11)}",
          f"{Q(T11)} {AM} {NANU(f'{AR} {EP_SHORT}')} {AM} {nanca(f'{AR} {EP[0]}… {LAST_EP}', T11)}")
    sk_r = C2.dev(SK, [R], ["con đường", DEV6[-1]])
    sk_x = C2.dev(SK, [D, M, AO], ["con đường", DEV6[-1]])
    pk_x87 = f"{ph(R)}, {PK} {MB}… {ph(D)}, {ph(M)}… {ph(AO)}, {MB}"
    d.seg("5-316",
          *sadhamma(ANN),
          pair(f"{pah_of(R, SK)}, {tail(ANN)}", f"{pah_of(R, PK)}, {tail(ANN)}"),
          pair(f"{dmao(SK)}, {tail(ANN)}", f"{pah_of(AO, PK)}, {tail(ANN)}"),
          pair(f"{sk_r}, {tail(ANN)}", f"{C2.dev(PK, [R], [DEV6[-1]])}, {tail(ANN)}"),
          pair(f"{sk_x}, {tail(ANN)}", f"{C2.dev(PK, [AO], [DEV6[-1]])}, {tail(ANN)}"),
          pair(f"{SK} {EP_SHORT}, {tail(ANN)}", f"{PK} {EP_SHORT}, {tail(ANN)}"),
          pair(f"{pah_of(R, PK)}, {tail(ANN, True)}", f"{pah_of(R, SK)}, {tail(ANN, True)}"),
          pair(f"{dmao(PK)}, {tail(ANN, True)}", f"{pah_of(AO, SK)}, {tail(ANN, True)}"),
          pair(f"{pk_x87}, {tail(ANN, True)}", f"{C2.dev(SK, [AO], [DEV6[-1]])}, {tail(ANN, True)}"),
          pair(f"{PK} {EP_SHORT}, {tail(ANN, True)}", f"{SK} {EP_SHORT}, {tail(ANN, True)}"))
    v_jan = f" [{SPELL} (Sī.): jānatāhaṃ; {VAR} (Syā., Pī., Ka.): jānatvāhaṃ]"
    s1 = (f"“{JP_HEAD.format(v=v_jan, e='.')} {KINCA} {ITI5} – {EVAM}” "
          "[Tương Ưng Bộ Kinh 3.101; Kinh Phật Thuyết Như Vậy 102; Tương Ưng Bộ Kinh 5.1095].")
    s2 = (f"“{JP_HEAD.format(v='', e='.')} {KINCA} {S4[0]} – này các tỳ-khưu, {JP}, {S4[1]} – {JP}, "
          f"{S4[2]} – {JP}, {S4[3]} – {JP}. {cap(EVAM)}” [Tương Ưng Bộ Kinh 5.1095].")
    s3 = (f"“{SAB.format(s=',')}” [Tương Ưng Bộ Kinh 4.26; Kinh Phật Thuyết Như Vậy 7, cũng trong Kinh Phật "
          "Thuyết Như Vậy]!")
    c11 = f"{ATTHEVA} {AM} {TENA_HI_NA(T11)}"
    d.seg("5-317",
          f"{Q(T11)} {AM} {NANU_VUTTAM} {s1} {c11}",
          f"{Q(T11)} {AM} {NANU_VUTTAM} {s2} {c11}",
          f"{Q(T11)} {AM} {NANU_VUTTAM} {s3} {c11}",
          f"{Q(T11)} {AM} {NANU_VUTTAM}",
          *SAHAVASSA,
          c11,
          f"{Q(T11)} {AM} {NANU_VUTTAM} {DHC}. {c11}",
          f"{NAVQ(T11)} {AM} {NANU(f'{AR} {NAMES}')} {AM} {hanci(f'{AR} {NAMES}', T11)}",
          f"{ifq(f'{AR} {NAMES}', T11)} {AM} {Q(f'{AR} có thể không biết {FR4}')} {NHP}",
          KATHA_END.format(x=ANN))
    # ------------------------------------------------------------ (12) Kaṅkhākathā
    d.head(4, VAGGA2, "5-10-3-0")
    d.head(4, f"(12) 3. {KATHA.format(x=KA)}", "5-10-4-0")
    d.seg("5-318",
          pair(T12, f"{AR} có {VC}"),
          f"{Q(f'{AR} không có {VC}')} {AM} {nanca(f'{AR} không có {VC}', T12)}",
          pair(f"{PU} có {KA}, {tail(VC)}", f"{AR} có {KA}, {tail(VC)}"),
          pair(f"{AR} có {KA}, {tail(VC, True)}", f"{PU} có {KA}, {tail(VC, True)}"),
          pair(T12, f"{AR} có {full8(KA)}", NH),
          f"{Q(f'{AR} không có {pe8(KA, 2)}')} {AM} {nanca(f'{AR} không có {pe8(KA, 2)}', T12)}",
          pair(f"{PU} có {KA}, {tail(pe8(KA, 2))}", f"{AR} có {KA}, {tail(pe8(KA, 2))}", NH),
          pair(f"{AR} có {KA}, {tail(pe8(KA, 2), True)}", f"{PU} có {KA}, {tail(pe8(KA, 2), True)}", NH))
    big_ar = (f"{dmao(AR)}… {ph(R)}, {AR} {MB}… {ph(D)}… {ph(AO)}, {MB}; chẳng phải {AR} {EP_SHORT}")
    d.seg("5-319",
          f"{Q(T12)} {AM} {NANU(f'{pah_of(R, AR)}, {UC0}')} {AM} {nanca(f'{pah_of(R, AR)}, {UC0}', T12)}",
          f"{Q(T12)} {AM} {NANU(big_ar)} {AM} {nanca(f'{AR} {EP_SHORT}', T12)}")

    def big(w, x, neg=False, moha=True, first_sep="… "):
        """doso pahīno…pe… moho … anottappaṃ pahīnaṃ…pe… rāgappahānāya … bojjhaṅgā bhāvitā…pe… <w> vītarāgo …"""
        dm = f"… {ph(M)}" if moha else ""
        return (f"{pah_of(D, w)}{first_sep}{pah(M)}… {pah(AO)}… {ph(R)}, {MB}… {ph(D)}{dm}… {ph(AO)}, {MB}… "
                f"{w} {EP_SHORT}, {tail(x, neg)}")

    d.seg("5-320",
          *sadhamma(KA),
          pair(f"{pah_of(R, SK)}, {tail(KA)}", f"{pah_of(R, PK)}, {tail(KA)}"),
          f"{pair(big(SK, KA), f'{PK} {EP_SHORT}, {tail(KA)}')} "
          f"{q(f'{pah_of(R, PK)}, {tail(KA, True)}')} {AM} {Q(f'{pah_of(R, SK)}, {tail(KA, True)}')} {NHP}",
          pair(big(PK, KA, True), f"{SK} {EP_SHORT}, {tail(KA, True)}"))
    s1b = f"“{JP_HEAD.format(v='', e='!')} {KINCA} {ITI5_PE} – {EVAM}”."
    s2b = f"“{JP_HEAD.format(v='', e='!')} {KINCA} {S4[0]}, này các tỳ-khưu… {S4[3]} {JP}. {cap(EVAM)}”."
    s3b = f"“{SAB.format(s=';')}”!"
    c12 = f"{ATTHEVA} {AM} {TENA_HI_NA(T12)}"
    d.seg("5-321",
          f"{Q(T12)} {AM} {NANU_VUTTAM} {s1b} {c12}",
          f"{Q(T12)} {AM} {NANU_VUTTAM} {s2b} {c12}",
          f"{Q(T12)} {AM} {NANU_VUTTAM} {s3b} {c12}",
          f"{Q(T12)} {AM} {NANU_VUTTAM} {SAHA_PE}. {c12}",
          f"{Q(T12)} {AM} {NANU_VUTTAM} {DHC}! {c12}",
          f"{Q(T12)} {AM} {NANU_VUTTAM}",
          "“Khi các hiện tượng thật sự hiện rõ,",
          "Nơi vị bà-la-môn nhiệt tâm, đang thiền định;",
          "Thì mọi nghi ngờ của vị ấy đều tan biến,",
          "Vì vị ấy hiểu rõ hiện tượng cùng với nguyên nhân.",
          "“Khi các hiện tượng thật sự hiện rõ,",
          "Nơi vị bà-la-môn nhiệt tâm, đang thiền định;",
          "Thì mọi nghi ngờ của vị ấy đều tan biến,",
          "Vì vị ấy đã biết sự diệt tận của các điều kiện.",
          "“Khi các hiện tượng thật sự hiện rõ,",
          "Nơi vị bà-la-môn nhiệt tâm, đang thiền định;",
          "Vị ấy đứng vững, xua tan đạo quân của Ma vương,",
          f"Như mặt trời [{SPELL} (Sī., Syā., Kaṃ., Pī.): suriyova] chiếu sáng bầu trời [Đại Phẩm 3; Kinh Phật "
          "Tự Thuyết 3].",
          "“Bất cứ nghi ngờ nào, ở đời này hay ở đời sau,",
          "Thuộc về mình hay thuộc về người khác;",
          f"Những người thiền định [{VAR} (Kinh Phật Tự Thuyết): ye jhāyino] đều dứt bỏ tất cả,",
          "Những người nhiệt tâm, sống đời sống tu hành trong sạch [Kinh Phật Tự Thuyết 47, cũng trong Kinh Phật "
          "Tự Thuyết].",
          "“Những ai đã vượt qua nghi ngờ, giữa các chúng sinh đầy nghi ngờ;",
          "Không còn ngờ vực, đã thoát khỏi trói buộc, vật cúng dường cho họ có quả lớn.",
          "“Sự công bố Giáo Pháp ở đây là như vậy,",
          "Ở đó không có đệ tử nào nghi ngờ điều gì;",
          f"Đấng đã vượt qua dòng lũ [{SPELL} (Sī., Ka.): nitiṇṇaoghaṃ; {SPELL} (Syā., Kaṃ.): nittiṇṇaoghaṃ], đã "
          "cắt đứt hoài nghi,",
          "Chúng tôi đảnh lễ Đức Phật, bậc Chiến Thắng, bậc chúa tể của loài người” [Trường Bộ Kinh 2.354].",
          c12,
          f"{NAVQ(T12)} {AM} Chẳng phải {AR} {KNAMES}” sao? {AM} {hanci(f'{AR} {KNAMES}', T12, sep=';')}",
          f"{ifq(f'{AR} {KNAMES}', T12)} {AM} {Q(f'{AR} có thể nghi ngờ {FR4_LOC}')} {NHP}",
          KATHA_END.format(x=KA))
    # ------------------------------------------------------------ (13) Paravitāraṇakathā
    d.head(4, VAGGA2, "5-10-5-0")
    d.head(5, f"(13) 4. {KATHA.format(x=PV)}", "5-10-5-1-0")
    d.seg("5-322",
          pair(T13, f"{AR} {PN}"),
          f"{NANU(f'{AR} {NPN}')} {AM} {nanca(f'{AR} {NPN}', T13)}",
          pair(f"{PU} có {PV}, và {TASSA} {PN}", f"{AR} có {PV}, và {TASSA} {PN}"),
          pair(f"{AR} có {PV}, và {TASSA} {NPN}", f"{PU} có {PV}, và {TASSA} {NPN}"),
          pair(T13, f"{AR} có {full8(PV)}"),
          f"{Q(f'{AR} không có {pe8(PV, 2)}')} {AM} {nanca(f'{AR} không có {pe8(PV, 2)}', T13)}",
          pair(f"{PU} có {PV}, {tail(pe8(PV, 2))}", f"{AR} có {PV}, {tail(pe8(PV, 2))}"),
          pair(f"{AR} có {PV}, {tail(pe8(PV, 2), True)}", f"{PU} có {PV}, {tail(pe8(PV, 2), True)}"))
    big13 = (f"{dmao(AR)}, {UC0}… {ph(R)}, {AR} {MB}… {ph(D)}… {ph(AO)}, {MB}… chẳng phải {AR} {EP_SHORT}")
    d.seg("5-323",
          f"{Q(T13)} {AM} {NANU(f'{pah_of(R, AR)}, {UC0}')} {AM} {nanca(f'{pah_of(R, AR)}, {UC0}', T13)}",
          f"{Q(T13)} {AM} {NANU(big13)} {AM} {nanca(f'{AR} {EP_NOPE}', T13)}")
    d.seg("5-324",
          *sadhamma(PV),
          pair(f"{pah_of(R, SK)}, {tail(PV)}", f"{pah_of(R, PK)}, {tail(PV)}", NH),
          pair(big(SK, PV, moha=False), f"{PK} {EP_SHORT}, {tail(PV)}"),
          pair(f"{pah_of(R, PK)}, {tail(PV, True)}", f"{pah_of(R, SK)}, {tail(PV, True)}", NH),
          pair(big(PK, PV, True, moha=False, first_sep=", "), f"{SK} {EP_SHORT}, {tail(PV, True)}"))
    s2c = (f"“{JP_HEAD.format(v='', e='!')} {KINCA} {S4[0]} – này các tỳ-khưu, {JP}, {S4[1]}… {S4[2]}… "
           f"{S4[3]} – {JP}. {cap(EVAM)}”.")
    c13 = f"{ATTHEVA} {AM} {TENA_HI_NA(T13)}"
    d.seg("5-325",
          f"{Q(T13)} {AM} {NANU_VUTTAM} {s1b} {c13}",
          f"{Q(T13)} {AM} {NANU_VUTTAM} {s2c} {c13}",
          f"{Q(T13)} {AM} {NANU_VUTTAM} {s3b} {c13}",
          f"{Q(T13)} {AM} {NANU_VUTTAM} {SAHA_PE}. {c13}",
          f"{Q(T13)} {AM} {NANU_VUTTAM} {DHC}! {c13}",
          f"{Q(T13)} {AM} {NANU_VUTTAM}",
          f"“Ta sẽ không có khả năng [{VAR} (Sī., Syā., Ka.): gamissāmi; {VAR} (Pī.): samīhāmi] giải thoát",
          f"Bất cứ người còn nghi hoặc nào [{VAR} (Ka.): kiñci] ở đời, này Đô-ta-ca;",
          "Và khi hiểu biết trực tiếp Giáo Pháp tối thượng,",
          "Như vậy, con sẽ vượt qua dòng lũ này” [Kinh Tập 1070, trong Kinh Tập; Tiểu Nghĩa Thích 33, phần giải "
          "thích câu hỏi của thanh niên Đô-ta-ca].",
          c13,
          f"{NAVQ(T13)} {AM} {NANU(VNAMES)} {AM} {hanci(VNAMES, T13)}",
          f"{ifq(VNAMES, T13)} {AM} {Q(f'người khác có thể giảng giải cho {AR} {FR4}')} {NHP}",
          KATHA_END.format(x=PV))
    # ------------------------------------------------------------ (14) Vacībhedakathā
    d.head(4, VAGGA2, "5-10-6-0")
    d.head(5, f"(14) 5. {KATHA.format(x=VB)}", "5-10-6-1-0")
    d.seg("5-326",
          pair(T14, f"ở mọi nơi, những người đang nhập thành tựu thiền đều có {VB}"),
          pair(T14, f"vào mọi lúc, những người đang nhập thành tựu thiền đều có {VB}"),
          pair(T14, f"tất cả những người đang nhập thành tựu thiền đều có {VB}"),
          pair(T14, f"trong mọi thành tựu thiền đều có {VB}"),
          pair(T14, f"{SAM} có {KB}"),
          pair(f"{SAM} không có {KB}", f"{SAM} không có {VB}"),
          pair(f"{SAM} có lời nói, có {VB}", f"{SAM} có thân, có {KB}"),
          pair(f"{SAM} có thân, không có {KB}", f"{SAM} có lời nói, không có {VB}"))

    def say(x, neg=False):
        return f"trong khi biết là {x}, {'nhưng không ' if neg else ''}nói ra lời là {x}"

    d.seg("5-327",
          pair(say("khổ đau"), say("sự phát sinh")),
          pair(say("khổ đau"), say("sự chấm dứt")),
          pair(say("khổ đau"), say("con đường")),
          pair(say("sự phát sinh", True), say("khổ đau", True)),
          pair(say("sự chấm dứt", True), say("khổ đau", True)),
          pair(say("con đường", True), say("khổ đau", True)))
    nsg = "hiểu biết có phạm vi đối tượng là sự thật, tai có phạm vi đối tượng là âm thanh"
    d.seg("5-328",
          f"{Q(T14)} {AM} Hiểu biết có phạm vi đối tượng là gì? Hiểu biết có phạm vi đối tượng là sự thật. "
          f"{Q('tai có phạm vi đối tượng là sự thật')} {NHP}",
          f"{Q(T14)} {AM} Tai có phạm vi đối tượng là gì? Tai có phạm vi đối tượng là âm thanh. "
          f"{Q('hiểu biết có phạm vi đối tượng là âm thanh')} {NH}",
          f"{Q(f'{T14}, {nsg}')} {AM} {nanca(nsg, T14)}",
          f"{Q(f'{T14}, {nsg}')} {AM} "
          f"{Q('có sự tụ hợp của hai sự tiếp xúc, hai cảm giác, hai tri giác, hai chủ ý, hai tâm')} {NH}")
    k0 = f"người đang nhập thành tựu thiền với {KAS[0]}"
    rest = chain(KAS[1:] + ARU)
    lk_sam = f"người đang nhập thành tựu thiền {LKY}"
    j234 = f"{jl(1)}… {J[2]}… {J[3]}"
    d.seg("5-329",
          pair(T14, f"{k0} có {VB}", NH),
          pair(T14, f"{sam(rest)} có {VB}"),
          f"{Q(f'{k0} không có {VB}')} {AM} {nanca(f'{k0} không có {VB}', T14)}",
          f"{Q(f'{sam(rest)} không có {VB}')} {AM} {nanca(f'{sam(ARU[-1])} không có {VB}', T14)}",
          pair(T14, f"{lk_sam} có {VB}"),
          f"{pair(T14, f'{sam(jl(0))} có {VB}')} {pair(T14, f'{sam(j234)} có {VB}')}",
          f"{Q(f'{lk_sam} không có {VB}')} {AM} {nanca(f'{lk_sam} không có {VB}', T14)}",
          f"{Q(f'{sam(jl(0))} không có {VB}')} {AM} {nanca(f'{sam(jl(0))} không có {VB}', T14)}",
          f"{Q(f'{sam(j234)} không có {VB}')} {AM} {nanca(f'{sam(jl(3))} không có {VB}', T14)}")
    t0 = sam(jl(0, LKT))
    d.seg("5-330",
          pair(f"{t0} có {VB}", f"{sam(jl(0))} có {VB}"),
          pair(f"{t0} có {VB}", f"{sam(j234)} có {VB}"),
          pair(f"{sam(jl(0))} không có {VB}", f"{t0} không có {VB}"),
          pair(f"{sam(j234)} không có {VB}", f"{t0} không có {VB}"))
    j234t = f"{jl(1, LKT)}… {J[2]}… {J[3]}"
    d.seg("5-331",
          pair(f"{t0} có {VB}", f"{sam(jl(1, LKT))} có {VB}"),
          pair(f"{t0} có {VB}", f"{sam(jl(2, LKT))}… {J[3]} có {VB}"),
          pair(f"{sam(jl(1, LKT))} không có {VB}", f"{t0} không có {VB}"),
          pair(f"{sam(j234t)} không có {VB}", f"{t0} không có {VB}"))
    v_sya = f" [{VAR} (Syā.): atthi vitakkavicārā, cũng vậy ở các chỗ sau]"
    has_vb = tail(VB)
    d.seg("5-332",
          f"{NAVQ(T14)} {AM} Chẳng phải {VS} – “{J1V}” sao? {AM} Nếu {VS} – “{J1V}”, {TENA_VATA} “{T14}”.",
          f"{ifq(f'{VS} – “{J1V}”{v_sya}', has_vb)} {AM} "
          f"{Q(f'{sam(J[0])} với {KAS[0]} có {VK}, {has_vb}')} {NHP}",
          f"{ifq(f'{VS} – “{J1V}”', has_vb)} {AM} "
          f"{Q(f'{sam(J[0])} với {chain(KAS[1:])} có {VK}, {has_vb}')} {NHP}",
          f"{NAVQ(T14)} {AM} Chẳng phải {VSM} – “{J1V}” sao? {AM} Nếu {VSM} – “{J1V}”, {TENA_VATA} “{T14}”.",
          f"{ifq(f'{VSM} – “{J1V}”', has_vb)} {AM} "
          f"{Q(f'{SSM} – “{sam(J[1])} có tri giác, {tail(VK)}”')} {NHP}",
          f"{ifq(f'{VSM} – “{J1V}”', has_vb)} {AM} "
          f"{Q(f'{SSM} – {sam(J[2])}… {J[3]}… {ARU[0]}… {ARU[1]}… {ARU[2]} có tri giác, {tail(VK)}')} {NHP}")
    n1 = f"“{NIR1}” [{SN13}]"
    nir_list = (f"đối với {sam(J[2])}, sự hân hoan đã chấm dứt, đối với {sam(J[3])}, hơi thở vào và hơi thở ra đã "
                f"chấm dứt, đối với {sam(ARU[0])}, tri giác về hình sắc đã chấm dứt, đối với {sam(ARU[1])}, tri giác "
                f"về {ARU[0]} đã chấm dứt, đối với {sam(ARU[2])}, tri giác về {ARU[1]} đã chấm dứt, đối với "
                f"{sam(ARU[3])}, tri giác về {ARU[2]} đã chấm dứt, đối với {sam(NIRS)}, {SV} đã chấm dứt")
    kts = chain([kt(VK, J[1]), kt("sự hân hoan", J[2]),
                 kt("hơi thở vào và hơi thở ra", J[3]) + " [Tăng Chi Bộ Kinh 10.72]",
                 kta(ARU[0], "tri giác về hình sắc"), kta(ARU[1], f"tri giác về {ARU[0]}"),
                 kta(ARU[2], f"tri giác về {ARU[1]}"), kta(ARU[3], f"tri giác về {ARU[2]}"),
                 kta(NIRS, SV) + " [Tăng Chi Bộ Kinh 10.72]"])
    sikhi = (f"{NAVQ(T14)} {AM} {NANU_VUTTAM} “Này A-nan, vị đệ tử tên là A-tỳ-phù của Đức Thế Tôn Thi-khí, bậc "
             "A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn, đứng ở cõi Phạm Thiên, đã dùng giọng nói làm cho mười nghìn thế "
             "giới nghe biết –")
    rb = "có bài kinh như vậy thật"                    # attheva suttanto (inside a sentence)
    d.seg("5-333",
          f"{Q(T14)} {AM} Chẳng phải {n1} sao! {ATTHEVA} {AM} Nếu “{NIR1}”, {rb}, {NO_CA_VATA} “{T14}”.",
          f"{ifq(f'{n1}, {rb}', has_vb)} {AM} "
          f"{ifq(f'“đối với {sam(J[1])}, {VK} đã chấm dứt” [{SN13}], {rb}', tail(VK))} {NHP}",
          f"{ifq(f'{n1}, {rb}', has_vb)} {AM} "
          f"{ifq(f'“{nir_list}” [{SN13}; Tăng Chi Bộ Kinh 9.31; Trường Bộ Kinh 3.344], {rb}', tail(SV))} {NHP}",
          f"{NAVQ(T14)} {AM} Chẳng phải Đức Thế Tôn đã nói rằng âm thanh là {KT} [{SPELL} (Syā.): kaṇṭako; Tăng Chi "
          f"Bộ Kinh 10.72] của {J[0]} [câu hỏi dựa trên Kinh Cái Gai, Tăng Chi Bộ Kinh 10.72] sao? {AM} "
          f"{hanci(kt('âm thanh', J[0]), T14)}",
          f"{ifq(kt('âm thanh', J[0]), T14)} {AM} {Q(f'{kts}, {tail(SV)}')} {NHP}",
          sikhi,
          "‘Hãy khởi sự, hãy tiến bước, hãy chuyên chú vào giáo huấn của Đức Phật;",
          "Hãy đánh tan đạo quân của Thần Chết, như voi phá ngôi nhà bằng lau sậy.",
          f"‘Ai trong Giáo Pháp và Giới Luật này, sẽ sống không buông lung [{SPELL} (Sī., Syā., Kaṃ.): vihessati; "
          f"{VAR} (Ka.): viharissati];",
          "Sau khi dứt bỏ vòng luân hồi của sự sinh, sẽ đi đến tận cùng của khổ đau’” [Tăng Chi Bộ Kinh 1, trong "
          "Chương Ba Pháp; Tương Ưng Bộ Kinh 1.285].",
          f"{ATTHEVA} {AM} {TENA_HI(T14)}",
          KATHA_END.format(x=VB))
    # ------------------------------------------------------------ (15) Dukkhāhārakathā
    d.head(4, VAGGA2, "5-10-7-0")
    d.head(5, f"(15) 6. {KATHA.format(x=DK)}", "5-10-7-1-0")
    allsay = f"bất cứ ai {SAY}, tất cả họ đều tu tập con đường"
    kill = (f"{KILLERS[0]}… {KILLERS[1]}… {KILLERS[2]}… {KILLERS[3]} [{VAR} (Sī., Ka.): lohituppādako; nhưng ở "
            f"những chỗ khác chỉ thấy ruhiruppādako]… {KILLERS[4]}")
    d.seg("5-334",
          pair(T15, allsay, NH),
          f"{pair(allsay, f'{BALA} {SAY}, {BALA} tu tập con đường', NH)} "
          f"{Q(f'{kill} {SAY}, {KILLERS[4]} tu tập con đường')} {NHP}",
          KATHA_END.format(x=DK))
    # ------------------------------------------------------------ (16) Cittaṭṭhitikathā
    d.head(4, VAGGA2, "5-10-8-0")
    d.head(5, f"(16) 7. {KATHA.format(x=CT)}", "5-10-8-1-0")
    day = f"{ONE} {stay('một ngày')}"
    lp = "những hiện tượng ấy thay đổi nhanh hơn tâm"
    d.seg("5-335",
          pair(day, "nửa ngày là khoảnh khắc sinh khởi, nửa ngày là khoảnh khắc suy tàn", NH),
          pair(f"{ONE} {stay('hai ngày')}", "một ngày là khoảnh khắc sinh khởi, một ngày là khoảnh khắc suy tàn", NH),
          pair(f"{ONE} {chain([stay(x) for x in DUR])}",
               "bốn mươi hai nghìn kiếp là khoảnh khắc sinh khởi, bốn mươi hai nghìn kiếp là khoảnh khắc suy tàn", NH),
          f"{pair(day, 'có những hiện tượng khác, trong một ngày, sinh khởi rồi chấm dứt nhiều lần', AM)} "
          f"{Q(lp)} {NH}",
          f"{Q(lp)} {AM} {NANU_VUTTAM} “Này các tỳ-khưu, Ta không thấy một hiện tượng nào khác thay đổi nhanh như "
          "tâm này. Này các tỳ-khưu, tâm thay đổi nhanh đến mức ngay cả một ví dụ cũng không dễ đưa ra” [Tăng Chi Bộ "
          f"Kinh 1.48]. {ATTHEVA} {AM} {TENA_HI_NA(lp)}",
          f"{Q(lp)} {AM} {NANU_VUTTAM} “Này các tỳ-khưu, ví như con khỉ đi lang thang trong rừng, giữa khu rừng rậm, "
          "nắm lấy một cành cây, buông cành ấy ra rồi nắm lấy cành khác, buông cành ấy ra rồi nắm lấy cành khác; "
          f"cũng vậy, này các tỳ-khưu, cái [{VAR} (nhiều bản): yadidaṃ] được gọi là tâm, cũng gọi là ý, cũng gọi là "
          "thức, ngày cũng như đêm, sinh khởi là cái này, chấm dứt là cái khác” [Tương Ưng Bộ Kinh 2.61]. "
          f"{ATTHEVA} {AM} {TENA_HI_NA(lp)}")
    unw = ["thức qua tai", "thức qua mũi", "thức qua lưỡi", "thức qua thân", "tâm bất thiện"] + \
          [f"đi kèm với {x}" for x in [R, D, M, "sự kiêu mạn", "quan điểm", "sự hoài nghi", "sự uể oải",
                                       "sự xao động", "sự không biết hổ thẹn"]] + [f"tâm đi kèm với {AO}"]
    same = (f"với chính tâm mà người ta {sense(0)}, với chính tâm ấy người ta {sense(1)}… {sense(2)}… {sense(3)}… "
            f"{sense(4)}… {sense(5)}… với chính tâm mà người ta {sense(5)}, với chính tâm ấy người ta {sense(0)}… "
            f"{sense(1)}… {sense(2)}… {sense(3)}… {sense(4)}")
    moves = [("đi tới", "đi lui"), ("nhìn thẳng", "nhìn quanh"), ("co", "duỗi")]   # (pi-2 ^2-519; ch5)
    mv = "; ".join(f"với chính tâm mà người ta {a}, với chính tâm ấy người ta {b}; với chính tâm mà người ta {b}, "
                   f"với chính tâm ấy người ta {a}" for a, b in moves)
    d.seg("5-336",
          f"{pair(day, 'thức qua mắt ' + stay('một ngày'), NH)} {Q(chain(unw) + ' ' + stay('một ngày'))} {NHP}",
          pair(day, same),
          pair(day, mv))
    akd1 = f"{ONE} của {AKD} {stay(AYU)}"
    dl = chain([f"của chư thiên {x}" for x in DEVAS])
    akd20 = f"{AYU} của {AKD} là hai mươi nghìn kiếp, {ONE} của {AKD} {stay('hai mươi nghìn kiếp')}"
    d.seg("5-337",
          pair(akd1, f"{ONE} của loài người {stay(AYU)}", NH),
          pair(akd1, f"{ONE} {dl} {stay(AYU)}", NH),
          pair(akd20, f"{AYU} của loài người là một trăm năm, {ONE} của loài người {stay('một trăm năm')}", NH),
          pair(akd20, f"{AYU} của chư thiên {DEVAS[0]} là năm trăm năm, {ONE} của chư thiên {DEVAS[0]} "
                      f"{chain([stay(x) for x in DUR2])}… {AYU} của chư thiên {DEVAS[-1]} là mười sáu nghìn kiếp, "
                      f"{ONE} của chư thiên {DEVAS[-1]} {stay('mười sáu nghìn kiếp')}", NH),
          pair(f"tâm của {AKD} chốc chốc lại sinh khởi, chốc chốc lại chấm dứt",
               f"{AKD} chốc chốc lại chết đi, chốc chốc lại sinh ra", NH),
          pair(akd1, f"{AKD} sinh ra với tâm nào thì chết đi với chính tâm ấy"),
          KATHA_END.format(x=CT))
    # ------------------------------------------------------------ (17) Kukkuḷakathā
    d.head(4, VAGGA2, "5-10-9-0")
    d.head(5, f"(17) 8. {KATHA.format(x=KUK)}", "5-10-9-1-0")
    fire = ("‘Bốc cháy bởi lửa tham đắm, lửa sân hận, lửa si mê; bốc cháy bởi sự sinh, sự lão hóa, sự chết, bởi sự "
            "sầu muộn, sự than khóc, sự khó chịu, nỗi buồn, sự tuyệt vọng’")
    aditta = ("“Này các tỳ-khưu, tất cả đều đang bốc cháy! Và này các tỳ-khưu, tất cả cái gì đang bốc cháy? Này các "
              "tỳ-khưu, mắt đang bốc cháy, các hình sắc đang bốc cháy, thức qua mắt đang bốc cháy, sự tiếp xúc của "
              f"mắt đang bốc cháy; điều được cảm nhận nào [{VAR} (Tương Ưng Bộ Kinh 4.28): yampidaṃ] sinh khởi do sự "
              "tiếp xúc của mắt làm điều kiện, dù dễ chịu, khó chịu hay không khó chịu cũng không dễ chịu, điều ấy "
              f"cũng đang bốc cháy. Bốc cháy bởi cái gì? {fire}, Ta nói như vậy. Tai đang bốc cháy, các âm thanh đang "
              "bốc cháy… mũi đang bốc cháy, các mùi đang bốc cháy… lưỡi đang bốc cháy, các vị đang bốc cháy… thân "
              "đang bốc cháy, các vật xúc chạm đang bốc cháy… ý đang bốc cháy, các đối tượng của ý đang bốc cháy, "
              "ý thức đang bốc cháy, sự tiếp xúc của ý đang bốc cháy; điều được cảm nhận nào sinh khởi do sự tiếp "
              "xúc của ý làm điều kiện, dù dễ chịu, khó chịu hay không khó chịu cũng không dễ chịu, điều ấy cũng "
              f"đang bốc cháy. Bốc cháy bởi cái gì? {fire}, Ta nói như vậy” [Đại Phẩm 54; Tương Ưng Bộ Kinh 4.28].")
    kama = ("“Này các tỳ-khưu, có năm loại dục lạc này! Năm loại nào? Các hình sắc được nhận biết bằng mắt, đáng mong "
            "muốn, đáng yêu thích, vừa ý, có vẻ đáng yêu, gắn liền với dục lạc, hấp dẫn; các âm thanh được nhận biết "
            "bằng tai… các mùi được nhận biết bằng mũi… các vị được nhận biết bằng lưỡi… các vật xúc chạm được nhận "
            "biết bằng thân, đáng mong muốn, đáng yêu thích, vừa ý, có vẻ đáng yêu, gắn liền với dục lạc, hấp dẫn. "
            "Này các tỳ-khưu, đây là năm loại dục lạc” [Trung Bộ Kinh 1.166; Tương Ưng Bộ Kinh 4.268].")

    def six(place, neg, var=""):
        w = ("không đáng mong muốn", "đáng mong muốn", "không đáng yêu thích", "đáng yêu thích", "không vừa ý",
             "vừa ý")
        a, b, c, e, f, g = w if neg else (w[1], w[0], w[3], w[2], w[5], w[4])
        v = f" [{var}]" if var else ""
        return (f"“Này các tỳ-khưu, đó là lợi ích cho các ông, này các tỳ-khưu, các ông đã khéo được lợi, thời cơ{v} "
                f"để sống đời sống tu hành trong sạch đã được các ông nắm lấy! Này các tỳ-khưu, Ta đã thấy {place} "
                "có tên gọi là sáu lĩnh vực tiếp xúc. Ở đó, bất cứ hình sắc nào người ta thấy bằng mắt, người ta chỉ "
                f"thấy hình sắc {a}, không thấy hình sắc {b}; chỉ thấy hình sắc {c}, không thấy hình sắc {e}; chỉ "
                f"thấy hình sắc {f}, không thấy hình sắc {g}. Bất cứ âm thanh nào người ta nghe bằng tai… mùi nào "
                "người ta ngửi bằng mũi… vị nào người ta nếm bằng lưỡi… vật xúc chạm nào người ta chạm bằng thân… "
                f"đối tượng của ý nào người ta nhận biết bằng ý, người ta chỉ nhận biết điều {a}, không nhận biết "
                f"điều {b}; chỉ nhận biết điều {c}, không nhận biết điều {e}; chỉ nhận biết điều {f}, không nhận "
                f"biết điều {g}” [Tương Ưng Bộ Kinh 4.135].")

    yad = "“cái gì vô thường thì cái ấy là khổ đau"
    sabba = "“tất cả các tạo tác đều vô thường”"
    d.seg("5-338",
          f"{Q(KK)} {AM} {NANU('có ' + ', '.join(SUKHA))} {AM} {nanca(f'có {SUKHA[0]}… {SUKHA[-1]}', KK)}",
          pair(KK, f"tất cả các tạo tác là cảm giác khó chịu, khổ đau thuộc thân, khổ đau thuộc tâm, {SOKA}", NH),
          f"{NAVQ(KK)} {AM} {NANU_VUTTAM} {aditta} {ATTHEVA} {AM} Vậy thì nên nói [{VAR} (Sī., Syā.): tena hi; "
          f"{VAR} (Ka.): tena hi na vattabbaṃ] – “{KK}”.",
          f"{Q(KK)} {AM} {NANU_VUTTAM} {kama} {ATTHEVA} {AM} {TENA_HI_NA(KK)}",
          f"{NAVQ(KK)} {AM} {NANU_VUTTAM} {six('các địa ngục', True, f'{VAR} (nhiều bản): paṭividdho')} {ATTHEVA} "
          f"{AM} Vậy thì nên nói [{VAR} (Syā., Ka.): tena hi na vattabbaṃ] – “{KK}”.",
          f"{Q(KK)} {AM} {NANU_VUTTAM} {six('các cõi trời', False)} {ATTHEVA} {AM} {TENA_HI_NA(KK)}",
          f"{NAVQ(KK)} {AM} Chẳng phải Đức Thế Tôn đã nói {yad} [Tương Ưng Bộ Kinh 3.15]”, {sabba} [Kinh Pháp Cú "
          f"277; Trung Bộ Kinh 1.356] sao? {AM} Nếu Đức Thế Tôn đã nói {yad}”, {sabba}, {TENA_VATA} “{KK}”.",
          pair(KK, f"sự bố thí {DNEG}", NH),
          f"{Q(f'{MER4} {DNEG}')} {NH}",
          f"{NANU(f'sự bố thí {DPOS}')} {AM} {nanca(f'sự bố thí {DPOS}', KK)}",
          f"{NANU(f'{MER4} {DPOS}')} {AM} {nanca(f'đời sống tu hành trong sạch {DPOS}', KK)}",
          f"{Q(KK)} {AM} {NANU_VUTTAM}",
          "“Hạnh phúc là sự tách biệt của người biết đủ, người đã nghe Giáo Pháp, người thấy rõ;",
          "Hạnh phúc là không ác ý ở đời, là sự chế ngự đối với các loài hữu tình.",
          "“Hạnh phúc là sự lìa tham ở đời, là sự vượt qua các dục lạc;",
          "Sự điều phục kiêu mạn cho rằng có tôi, đó thật là hạnh phúc tối thượng [Đại Phẩm 5; Kinh Phật Tự Thuyết "
          "11, và trong Kinh Phật Tự Thuyết].",
          "“Hạnh phúc ấy đạt được nhờ hạnh phúc, đó là hạnh phúc tuyệt đối;",
          "Ba loại hiểu biết chân thật đã được chứng đạt, đó thật là hạnh phúc tối thượng”.",
          f"{ATTHEVA} {AM} {TENA_HI_NA(KK)}",
          KATHA_END.format(x=KUK))
    # ------------------------------------------------------------ (18) Anupubbābhisamayakathā
    d.head(4, VAGGA2, "5-10-10-0")
    d.head(5, f"(18) 9. {KATHA.format(x=AB)}", "5-10-10-1-0")

    def mp(m, p):
        return (f"{pair(T18, f'tu tập con đường {m} {TUAN}', NH)} "
                f"{pair(f'tu tập con đường {m} {TUAN}', f'tự mình chứng nghiệm {p} {TUAN}', NH)}")

    d.seg("5-339",
          mp("vào dòng", "thành quả vào dòng"), mp("trở lại một lần", "thành quả trở lại một lần"),
          mp("không trở lại", "thành quả không trở lại"), mp("A-la-hán", "thành quả A-la-hán"))
    so_q = f"Có phải người ấy {part_a('bậc vào dòng')}, {part_b('thành quả vào dòng')}, {SOTA_X} không?"
    so_ans = f"{JA} {CB} {S3}, và {TDK}."
    ds3 = f"{DS['samudaya']}… {DS['nirodha']}… {DS['magga']}, {KIM}"
    d.seg("5-340",
          f"{ask('sota', DS['dukkha'])} {so_ans} {so_q} {NH}",
          f"{cap(ds3)} {so_ans} {so_q} {NHP}")
    sa_ans = f"{JA} {CB} sự tham đắm dục lạc ở dạng thô, ác ý ở dạng thô, và {TDK}."
    sa_q = f"Có phải người ấy {part_a('bậc trở lại một lần')}, {part_b('thành quả trở lại một lần')} không?"
    d.seg("5-341",
          f"{ask('saka', DS['dukkha'])} {sa_ans} {sa_q} {NHP} {ds3} {sa_ans} {sa_q} {NHP}")
    an_ans = f"{JA} {CB} sự tham đắm dục lạc ở dạng nhỏ nhiệm, ác ý ở dạng nhỏ nhiệm, và {TDK}."
    an_base = f"{part_a('bậc không trở lại')}, {part_b('thành quả không trở lại')}, {CB} là {PARI4}… {UDDHAM}"
    d.seg("5-342",
          f"{ask('ana', DS['dukkha'])} {an_ans} Có phải người ấy {an_base}, {CB} không theo dòng đi lên, không đi "
          f"đến cõi Sắc Cứu Cánh không? {NHP}",
          f"{cap(ds3)} {an_ans} Có phải người ấy {an_base}, {CB} không phải là {UDDHAM} không? {NHP}")
    ar_ans = (f"{JA} {CB} sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao động, vô "
              f"minh, và {TDK}.")
    tr_pe = TR.replace(f", {LAST_EP}", f"… {LAST_EP}")
    epi = f"{CB} {EP[0]}… {EP[1]}… {EP[2]}… {', '.join(EP[3:])}, {tr_pe}"
    sac_not = f"{CB} điều cần được tự mình chứng nghiệm chưa được tự mình chứng nghiệm"
    ar_base = f"{part_a(AR)}, {part_b('trạng thái A-la-hán')}"
    d.seg("5-343",
          f"{ask('ara', DS['dukkha'])} {ar_ans} Có phải người ấy {ar_base}, {epi}, {sac_not} không? {NHP}",
          f"{cap(ds3)} {ar_ans} Có phải người ấy {ar_base}, {epi}, {sac_not} không? {NHP}")
    sp = PAT["sota"]
    kd, cd = "khổ đau", "con đường"
    d.seg("5-344",
          f"{pair(f'{sp}, {dk(kd)}', phx(kd), NH)} {pair(DK2, phx('sự chấm dứt'), NH)}",
          f"{pair(f'{sp}, {dk(cd)}, {phx(cd)}', f'{dk(kd)}, {phx(kd)}')} "
          f"{q(f'{dk(cd)}, {phx(cd)}')} {AM} {Q(DK2 + ', ' + phx('sự chấm dứt'))} {NHP}",
          f"{pair(f'{sp}, {dk(kd)}, {nph(kd)}', f'{dk(cd)}, {nph(cd)}')} "
          f"{q(f'{DK2}, {nph('sự chấm dứt')}')} {AM} "
          f"{Q(f'trong khi thấy con đường, nên được gọi là “{PP}”, {nph(cd)}')} {NHP}",
          f"{PSK} {pair(f'{sp}, {dk(kd)}, {nph(kd)}', 'việc thấy khổ đau là vô ích')} "
          f"{q(f'{DK2}, {nph('sự chấm dứt')}')} {AM} {Q('việc thấy sự chấm dứt là vô ích')} {NHP}")
    nums = ["bốn", "tám", "mười hai", "bốn mươi bốn", "bảy mươi bảy"]
    fr = []
    for i, n in enumerate(nums):
        qq = (Q if i == 0 else q)(f"tự mình chứng nghiệm thành quả vào dòng bằng {n} hiểu biết")
        fr.append(f"{qq} {AM} {Q(f'có {n} thành quả vào dòng')} {NHP}")
    d.seg("5-345",
          f"{PPK} {pair('khi khổ đau đã được thấy, bốn sự thật đã được thấy', 'sự thật về khổ đau là bốn sự thật')}",
          f"{PSK} {pair('khi khối vật chất đã được thấy là vô thường, năm khối đã được thấy là vô thường', 'khối vật chất là năm khối')}",
          f"{PSK} {pair('khi lĩnh vực mắt đã được thấy là vô thường, mười hai lĩnh vực nhận biết đã được thấy là vô thường', 'lĩnh vực mắt là mười hai lĩnh vực nhận biết')}",
          f"{PSK} {pair('khi yếu tố mắt đã được thấy là vô thường, mười tám yếu tố đã được thấy là vô thường', 'yếu tố mắt là mười tám yếu tố')}",
          f"{PSK} {pair('khi năng lực mắt đã được thấy là vô thường, hai mươi hai năng lực đã được thấy là vô thường', 'năng lực mắt là hai mươi hai năng lực')}",
          f"{PSK} {' '.join(fr)}")
    c18 = f"{ATTHEVA} {AM} {TENA_HI(T18)}"
    c18n = f"{ATTHEVA} {AM} {TENA_HI_NA(T18)}"
    gav = ("Chẳng phải tôn giả trưởng lão Kiều-phạm-ba-đề đã nói với các tỳ-khưu thế này sao – “Này các hiền giả, "
           "điều này tôi đã được nghe trực tiếp từ Đức Thế Tôn, đã được nhận trực tiếp – ‘Này các tỳ-khưu, ai thấy "
           "khổ đau thì người ấy cũng thấy sự phát sinh của khổ đau, cũng thấy sự chấm dứt khổ đau, cũng thấy cách "
           "thực hành dẫn đến sự chấm dứt khổ đau; ai thấy sự phát sinh của khổ đau thì người ấy cũng thấy khổ đau, "
           "cũng thấy sự chấm dứt khổ đau, cũng thấy cách thực hành dẫn đến sự chấm dứt khổ đau; ai thấy sự chấm dứt "
           "khổ đau thì người ấy cũng thấy khổ đau, cũng thấy sự phát sinh của khổ đau, cũng thấy cách thực hành dẫn "
           "đến sự chấm dứt khổ đau; ai thấy cách thực hành dẫn đến sự chấm dứt khổ đau thì người ấy cũng thấy khổ "
           "đau, cũng thấy sự phát sinh của khổ đau, cũng thấy sự chấm dứt khổ đau’” [Tương Ưng Bộ Kinh 5.1100]!")
    d.seg("5-346",
          f"{NAVQ(T18)} {AM} {NANU_VUTTAM} “Này các tỳ-khưu, ví như đại dương dần dần thấp xuống, dần dần nghiêng "
          "xuống, dần dần dốc xuống, không đột ngột là vực thẳm; cũng vậy, này các tỳ-khưu, trong Giáo Pháp và Giới "
          "Luật này, có sự tu học tuần tự, việc làm tuần tự, cách thực hành tuần tự, không có sự thấu triệt hiểu "
          "biết trọn vẹn một cách đột ngột” [Tiểu Phẩm 385; Tăng Chi Bộ Kinh 8.20; Kinh Phật Tự Thuyết 45, và trong "
          f"Kinh Phật Tự Thuyết]. {c18}",
          f"{NAVQ(T18)} {AM} {NANU_VUTTAM}",
          *DHP239,
          c18,
          f"{Q(T18)} {AM} {gav} {c18n}",
          f"{Q(T18)} {AM} {NANU_VUTTAM}",
          *SAHAVASSA,
          c18n,
          f"{Q(T18)} {AM} {NANU_VUTTAM} {DHC}! {c18n}",
          KATHA_END.format(x=AB))
    # ------------------------------------------------------------ (19) Vohārakathā
    d.head(4, VAGGA2, "5-10-11-0")
    d.head(5, f"(19) 10. {KATHA.format(x=VOHARA)}", "5-10-11-1-0")
    t_ear = f"{VH} va chạm vào tai {LKY}"
    t_vin = f"người ta nhận biết {VH} bằng thức {LKY}"
    t_pu = f"những người phàm phu nhận biết {VH}"
    d.seg("5-347",
          pair(T19, f"va chạm vào tai {LKT}, không phải vào tai {LKY}, người ta nhận biết bằng thức {LKT}, không phải "
                    f"bằng thức {LKY}, các đệ tử nhận biết, không phải những người phàm phu"),
          f"{NANU(t_ear)} {AM} {nanca(t_ear, T19)}",
          f"{NANU(t_vin)} {AM} {nanca(t_vin, T19)}",
          f"{NANU(t_pu)} {AM} {nanca(t_pu, T19)}")
    ld_ear = "được nhận biết bằng tai, va chạm vào tai, đi vào tầm của tai"
    nld_ear = "không được nhận biết bằng tai, không va chạm vào tai, không đi vào tầm của tai"
    d.seg("5-348",
          pair(T19, f"là con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng, con đường trở lại "
                    "một lần, thành quả trở lại một lần, con đường không trở lại, thành quả không trở lại, con đường "
                    "A-la-hán, thành quả A-la-hán, sự thiết lập tỉnh thức, nỗ lực đúng đắn, nền tảng thần thông, "
                    "năng lực, sức mạnh, chi phần giác ngộ"),
          f"{pair(T19, f'có những người nghe {VH}', AM)} {Q(f'{LD} {ld_ear}')} {NHP}",
          f"{NANU(f'{LD} {nld_ear}')} {AM} {nanca(f'{LD} {nld_ear}', T19)}")
    rg = "khơi dậy sự tham đắm, hấp dẫn, đáng ham muốn, làm say đắm, trói buộc, làm mê mẩn"
    nrg = ("không khơi dậy sự tham đắm, không hấp dẫn, không đáng ham muốn, không làm say đắm, không trói buộc, "
           "không làm mê mẩn")
    ds_ = "khơi dậy sự sân hận, khơi dậy sự phẫn nộ, khơi dậy sự ác cảm"
    nds = "không khơi dậy sự sân hận, không khơi dậy sự phẫn nộ, không khơi dậy sự ác cảm"
    mh = ("khơi dậy sự si mê, tạo ra sự không biết, làm cho không có mắt, làm chấm dứt trí tuệ, thuộc về phía gây "
          "phiền não, không dẫn đến Niết-bàn")
    nmh = ("không khơi dậy sự si mê, không tạo ra sự không biết, không làm cho không có mắt, làm tăng trưởng trí "
           "tuệ, không thuộc về phía gây phiền não, dẫn đến Niết-bàn")
    d.seg("5-349",
          f"{pair(T19, f'có những người có thể tham đắm vào {VH}', AM)} {Q(f'{LD} {rg}')} {NHP}",
          f"{NANU(f'{LD} {nrg}')} {AM} {nanca(f'{LD} {nrg}', T19)}",
          f"{pair(T19, f'có những người có thể sân hận với {VH}', AM)} {Q(f'{LD} {ds_}')} {NHP}",
          f"{NANU(f'{LD} {nds}')} {AM} {nanca(f'{LD} {nds}', T19)}",
          f"{pair(T19, f'có những người có thể si mê với {VH}', AM)} {Q(f'{LD} {mh}')} {NHP}",
          f"{NANU(f'{LD} {nmh}')} {AM} {nanca(f'{LD} {nmh}', T19)}")
    hear = f"bất cứ ai nghe {VH}, tất cả họ đều tu tập con đường"
    kill2 = f"{KILLERS[0]} tu tập con đường… {KILLERS[1]}… {KILLERS[2]}… {KILLERS[3]}… {KILLERS[4]}"
    d.seg("5-350",
          pair(T19, hear),
          f"{pair(hear, f'{BALA} nghe {VH}, {BALA} tu tập con đường')} "
          f"{q(f'{kill2} nghe {VH}, {KILLERS[4]} tu tập con đường')} {NHP}")
    d.seg("5-351",
          f"{Q('có thể dùng cây gậy bằng vàng để chỉ cả đống lúa lẫn đống vàng')} {AM} Cũng vậy, Đức Thế Tôn dùng "
          f"lời nói {LKT} để nói về {BOTH}.",
          f"{Q('có thể dùng cây gậy bằng gỗ thầu dầu để chỉ cả đống lúa lẫn đống vàng')} {AM} Cũng vậy, Đức Thế Tôn "
          f"dùng lời nói {LKY} để nói về {BOTH}.")
    obj = [("con đường", "cái không phải con đường"), ("thành quả", "cái không phải thành quả"),
           ("Niết-bàn", "cái không phải Niết-bàn"), ("điều do điều kiện tạo thành", "điều không do điều kiện tạo thành"),
           ("vật chất", "cái không phải vật chất"), ("cảm giác", "cái không phải cảm giác"),
           ("tri giác", "cái không phải tri giác"), ("các tạo tác", "những cái không phải tạo tác"),
           ("thức", "cái không phải thức")]
    vo = ", ".join(f"khi nói về {a} thì là {a}, khi nói về {b} thì là {b}" for a, b in obj)
    bh = f"Đức Thế Tôn nói về {BOTH}"
    d.seg("5-352",
          pair(VL, f"khi nói về điều {LKY} thì va chạm vào tai {LKY}, khi nói về điều {LKT} thì va chạm vào tai "
                   f"{LKT}; khi nói về điều {LKY} thì người ta nhận biết bằng thức {LKY}, khi nói về điều {LKT} thì "
                   f"người ta nhận biết bằng thức {LKT}; khi nói về điều {LKY} thì những người phàm phu nhận biết, "
                   f"khi nói về điều {LKT} thì các đệ tử nhận biết"),
          f"Có phải không nên nói – “{VL} không? {AM} {NANU(bh)} {AM} {hanci(bh, VL)}",
          pair(VL, vo),
          KATHA_END.format(x=VOHARA))
    # ------------------------------------------------------------ (20) Nirodhakathā
    d.head(4, VAGGA2, "5-10-12-0")
    d.head(5, f"(20) 11. {KATHA.format(x=NIR)}", "5-10-12-1-0")
    seq = [("có hai sự chấm dứt", "có hai sự chấm dứt khổ đau"),
           ("có hai sự chấm dứt khổ đau", "có hai sự thật về sự chấm dứt"),
           ("có hai sự thật về sự chấm dứt", "có hai sự thật về khổ đau"),
           ("có hai sự thật về sự chấm dứt", "có hai sự thật về sự phát sinh"),
           ("có hai sự thật về sự chấm dứt", "có hai sự thật về con đường")]
    l1 = " ".join(f"{(Q if i == 0 else q)(a)} {AM} {Q(b)} {NHP}" for i, (a, b) in enumerate(seq))
    ref = ("có hai nơi che chở… hai nơi ẩn náu… hai nơi nương tựa… hai nơi đến cuối cùng… hai điều bất biến… hai điều "
           "bất tử… hai Niết-bàn")
    ps_n = f"người ta làm chấm dứt {PS} những tạo tác đã chấm dứt {NPS}"
    acc = f"các tạo tác chấm dứt {NPS} cũng bị phá vỡ hoàn toàn, các tạo tác chấm dứt {PS} cũng bị phá vỡ hoàn toàn"
    d.seg("5-353",
          l1,
          pair("có hai sự thật về sự chấm dứt", ref),
          pair("có hai Niết-bàn", "giữa hai Niết-bàn có sự cao thấp, sự thấp kém và ưu việt, sự hơn kém, hoặc ranh "
                                  "giới, hoặc sự phân chia, hoặc đường vạch, hoặc khoảng cách"),
          f"{Q(T20)} {AM} {NANU(ps_n)} {AM} {nanca(ps_n, T20)}",
          f"{NAVQ(T20)} {AM} {NANU(acc)} {AM} {hanci(acc, T20)}",
          f"{Q(T20)} {AM} {Q(f'các tạo tác chấm dứt {PS} cũng [{VAR} (?): paṭisaṅkhāniruddhā] chấm dứt nhờ con đường cao quý')} "
          f"{AM} {Q(f'các tạo tác chấm dứt {NPS} chấm dứt nhờ con đường cao quý')} {NHP}",
          f"{Q(T20)} {AM} {Q(f'các tạo tác chấm dứt {PS} không sinh khởi lại')} {AM} "
          f"{Q(f'các tạo tác chấm dứt {NPS} không sinh khởi lại')} {NHP} vậy thì không nên nói – “{T20}”.",
          KATHA_END.format(x=NIR),
          f"{VAGGA2}.",
          TASSUDDANAM,
          f"{cap(PARUPAHARA)}, {ANN}, {KA}, {PV};",
          f"{cap(VB)}, {DK}, {CT} và {KUK};",
          f"{cap(AB)}, {VOHARA} và {NIR}.")
    return d.text()


# ================================================================ cross-book asserts
CROSS_BOOK = [
    ("về Bậc Đạo Sư", 1), ("về Giáo Pháp", 1), ("về Tăng đoàn", 1), ("về sự tu học", 1), ("về quá khứ", 1),
    ("về tương lai", 1), ("về quá khứ và tương lai", 1), (OBJ8[-1], 1), ("sự phân vân", 1), ("sự nghi ngờ", 1),
    ("sự không biết", 1), ("xiềng xích hoài nghi", 1), ("dòng lũ vô minh", 1), ("ách vô minh", 1),
    ("khuynh hướng tiềm ẩn vô minh", 2), ("chướng ngại vô minh", 1), (EAT, 2), ("người ái nam ái nữ", 2),
    ("hưởng thụ hành vi dâm dục", 4), ("xứ Ca-thi", 4), ("vòng hoa, hương thơm, dầu thoa", 4), (REQ, 2),
    ("tỉnh thức và hiểu biết rõ ràng", 2), ("sự diệt tận các ô nhiễm", 1), ("sự phát sinh của khổ đau", 2),
    ("sự chấm dứt khổ đau", 2), ("cách thực hành dẫn đến sự chấm dứt khổ đau", 2), ("với đề mục bao trùm là đất", 1),
    ("với đề mục bao trùm là nước", 1), ("với đề mục bao trùm là lửa", 1), ("với đề mục bao trùm là gió", 1),
    ("đề mục bao trùm màu xanh", 1), ("đề mục bao trùm màu vàng", 1), ("đề mục bao trùm màu đỏ", 1),
    ("đề mục bao trùm màu trắng", 1), (J[0], 1), (J[1], 1), (J[2], 1), (J[3], 1),
    ("Các hiện tượng thuộc thế gian", 1), ("Các hiện tượng vượt thế gian", 1),
    (ARU[0], 2), (ARU[1], 2), (ARU[2], 2), (ARU[3], 2), ("chấm dứt tri giác và cảm giác", 2),
    ("sự tạo tác bằng lời nói", 2), ("có sự hướng tâm và sự duy trì tâm", 1), (AKD, 2), ("Một phần ba của kiếp", 2),
    ("Nửa kiếp", 2), ("khi đi tới, khi đi lui", 2), ("khi nhìn thẳng, khi nhìn quanh", 2), ("có tính trần tục", 2),
    ("hiểu biết chân thật", 1), ("đại dương", 1), ("việc hành trì ngày trai giới", 2), ("sự hân hoan", 1),
    ("sự tách biệt", 1), ("thức qua mắt", 2), ("sự tiếp xúc của mắt", 1), ("sự tụ hợp", 2), ("Tuổi thọ", 2),
    ("thành tựu thiền", 2), ("đi kèm với", 2), ("đã chấm dứt", 2), ("cõi Phạm Thiên", 1), ("giáo huấn", 2),
    ("đi đến tận cùng của khổ đau", 4), ("đã đứng vững", 4), ("Như Lai", 2),
] + [(f"chư thiên {x}", 2) for x in DEVAS]

PI5_DONE = [   # strings taken from finished pi-5 chapters (asserted in their output files)
    ("2-parihanikatha.md", UC0), ("2-parihanikatha.md", EP_SHORT), ("2-parihanikatha.md", KR),
    ("3-brahmacariyakatha.md", DHC), ("3-brahmacariyakatha.md", DHP239[0]),
    ("3-brahmacariyakatha.md", DHP239[1]), ("3-brahmacariyakatha.md", ", ".join(EP) + ", " + TR),
    ("3-brahmacariyakatha.md", SOTA_X.replace(CB, "một phần")),
    ("3-brahmacariyakatha.md", PARI4.replace("… ", ", ")),
    ("9-hevatthikatha.md", TASSUDDANAM),
] + [("3-brahmacariyakatha.md", s) for s in SAHAVASSA[:-1]] + [("3-brahmacariyakatha.md", "Không thể [")]


def check_asserts():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    done = {}
    miss5 = []
    for f, s in PI5_DONE:
        if f not in done:
            done[f] = (B.OUT_DIR / f).read_text(encoding="utf-8")
        if s not in done[f]:
            miss5.append((f, s))
    for f, s in miss5:
        print(f"PI-5 MISSING in {f}: {s}")
    assert not missing and not miss5, f"{len(missing)} cross-book / {len(miss5)} pi-5 strings not found"
    print(f"cross-book asserts: {len(CROSS_BOOK)} strings in pi-1..4 rails; {len(PI5_DONE)} strings in pi-5 chapters")


def main():
    B.check_cross_book()
    check_asserts()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs[:120]:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line-check problems"
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines, {text.count(' ^')} IDs; "
          f"odd closing order repaired: {len(repaired)}")
    print("line checks: OK")


if __name__ == "__main__":
    main()
