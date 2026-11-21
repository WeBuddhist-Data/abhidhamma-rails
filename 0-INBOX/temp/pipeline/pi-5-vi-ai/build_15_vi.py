# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 15: 15-sattamavaggo.md (Sattamavaggo, ^5-15-0 … ^5-502),
the ten kathā (63)-(72) of the seventh vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_5_vi / build_9_vi / build_10_vi / build_11_vi / build_12_vi (read-only; importing writes nothing)
for strings shared with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4
Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur
in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run
against the Pāli. Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_15_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_5_vi as C5      # noqa: E402  (QUAL: asaṅkiṇṇā … viññūhi)
import build_9_vi as C9      # noqa: E402  (Tassuddānaṃ –, esese ekaṭṭhe …)
import build_10_vi as C10    # noqa: E402  (iṭṭhaphalaṃ … sukhavipākaṃ / aniṭṭhaphalaṃ … dukkhavipākaṃ)
import build_11_vi as C11    # noqa: E402  (dvinnaṃ phassānaṃ … samodhānaṃ)
import build_12_vi as C12    # noqa: E402  (fruits, cakkavattisatta, L10, PG)

NAME = "15-sattamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA, ATTHEVA, NANU_VUTTAM = (B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA, B.ATTHEVA,
                                                   B.NANU_VUTTAM)
VAR, SPELL = B.VAR, B.SPELL
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA7 = B.VAGGA[7]                                       # Sattamavaggo = «Chương thứ bảy» (terms file)


def hanci_no(p, qq, sep=","):
    """Hañci P, no ca vata re vattabbe – "Q"ti.  (ch2, ch3, ch10, ch12)"""
    return f"Nếu {p}{sep} {B.NO_CA_VATA} “{qq}”."


def hanci_yes(p, qq, sep=","):
    """Hañci P, tena vata re vattabbe – "Q"ti.  (sample; ';' as ch2 ^5-118)"""
    return f"Nếu {p}{sep} {B.TENA_VATA} “{qq}”."


def nanu_l(x):
    """nanu Xti? after …pe… (lowercase)"""
    return f"chẳng phải {x} sao?"


# ================================================================ kathā names (closing lines = «Phần bàn về …»)
KX = {1: "những gì được gộp vào",                         # Saṅgahitakathā (terms file, pi-3 saṅgahita)
      2: "những gì gắn liền",                             # Sampayuttakathā (sampayutta «gắn liền với» pi-1)
      3: "yếu tố đồng hành với tâm",                      # Cetasikakathā (cetasika pi-1)
      4: "sự bố thí",                                     # Dānakathā (dāna «sự bố thí» ch10)
      5: "phước phát sinh từ sự thọ hưởng",               # Paribhogamayapuññakathā (puñña «phước» pi-2; paribhuñjati ch8)
      6: "những gì được cho từ đây",                      # Itodinnakathā / Ito dinnakathā
      7: "việc cho rằng đất là quả của nghiệp",           # Pathavī kammavipākotikathā (kammavipāka pi-1)
      8: "việc cho rằng sự lão hóa và sự chết là quả của nghiệp",   # Jarāmaraṇaṃ vipākotikathā (jarāmaraṇa pi-2)
      9: "quả của hiện tượng cao quý",                    # Ariyadhammavipākakathā
      10: "việc cho rằng quả của nghiệp là hiện tượng có khả năng sinh ra quả"}   # Vipāko vipākadhammadhammotikathā


def heads(n):
    """#### Sattamavaggo ^5-15-n-0 / ##### (62+n) n. <title> ^5-15-n-1-0"""
    return [(4, VAGGA7, f"5-15-{n}-0"), (5, f"({62 + n}) {n}. {K(x=KX[n])}", f"5-15-{n}-1-0")]


# ================================================================ (63) Saṅgahita
SG = "được gộp vào"                                       # saṅgahita (pi-3 «được gộp vào bốn khối …»)
NO_SG = f"không có hiện tượng nào {SG} hiện tượng nào"    # natthi keci dhammā kehici dhammehi saṅgahitā
SOME_SG = f"có một số hiện tượng {SG} một số hiện tượng"  # atthi keci dhammā kehici dhammehi saṅgahitā
GAN = "có một số hiện tượng được tính vào, được kể vào, thuộc về một số hiện tượng"
# atthi keci dhammā kehici dhammehi gaṇanaṃ gacchanti uddesaṃ gacchanti pariyāpannā (pariyāpanna «thuộc về» ch10)
AY = B.AYATANA                                            # lĩnh vực mắt … lĩnh vực vật xúc chạm (pi-2)
RK, VK, SK, KHK, WK = "khối vật chất", "khối cảm giác", "khối tri giác", "khối tạo tác", "khối thức"   # (pi-2)
SUV, DUV = "cảm giác dễ chịu", "cảm giác khó chịu"        # sukhā / dukkhā vedanā (pi-1)
ADV = "cảm giác không khó chịu cũng không dễ chịu"        # adukkhamasukhā vedanā (pi-1)
SJ = "sinh từ sự tiếp xúc của"                            # -samphassaja (pi-2 «tri giác sinh từ sự tiếp xúc của mắt»)


def unit(head, last, k, var=""):
    """X katamakkhandhagaṇanaṃ gacchatīti? K-gaṇanaṃ gacchatīti. Hañci X K-gaṇanaṃ gacchati, tena vata re
    vattabbe – "X K-ena saṅgahita"nti."""
    return (f"{head} được tính vào khối nào{var}? Được tính vào {k}. "
            f"{hanci_yes(f'{last} được tính vào {k}', f'{last} {SG} {k}')}")


OX = ("hai con bò đực được gộp vào bằng dây thừng hay bằng dây ách, đồ ăn khất thực được gộp vào bằng túi treo, "
      "con chó được gộp vào bằng dây xích")
# dāmena vā yottena vā dve balibaddā saṅgahitā, sikkāya piṇḍapāto saṅgahito, sā (= the dog) gaddulena saṅgahito
SK_NOTE = f"[lời của {B.SAKAVADI} (cần xem Chú giải)]"      # [sakavādivacanaṃ (aṭṭhakathā passitabbā)]

# ================================================================ (64) Sampayutta
NO_SP = "không có hiện tượng nào gắn liền với hiện tượng nào"   # natthi keci dhammā kehici dhammehi sampayuttā
ONE4 = "có cùng sự sinh khởi, có cùng sự chấm dứt, có cùng chỗ dựa, có cùng đối tượng"
# ekuppādā ekanirodhā ekavatthukā ekārammaṇā (vatthu «chỗ dựa» pi-1)
SAHA7 = f"đi kèm, cùng sinh, hòa lẫn, {ONE4}"             # sahagatā sahajātā saṃsaṭṭhā … (pi-2 ^2-567)
SAHA8 = f"đi kèm, cùng sinh, hòa lẫn, gắn liền, {ONE4}"   # … saṃsaṭṭhā sampayuttā … (pi-2 ^2-567)
SP7 = f"có một số hiện tượng {SAHA7} với một số hiện tượng"

# ================================================================ (65) Cetasika
CET = KX[3]                                               # cetasika (pi-1 «là yếu tố đồng hành với tâm»)
CD = f"hiện tượng là {CET}"                               # cetasiko dhammo (pi-1 «Các hiện tượng là yếu tố …»)
NO_CET = f"không có {CD}"                                 # natthi cetasiko dhammo
SAHA8_C = f"có một số hiện tượng {SAHA8} với tâm"         # atthi keci dhammā cittena sahagatā … ekārammaṇā
R, D, M, AO = C12.C2.R, C12.C2.D, C12.C2.M, C12.C2.AO     # rāgo doso moho anottappaṃ (ch2, pi-1)
L10 = C12.L10                                             # phassa … paññā (ch4 / ch12)
L12 = [L10[1], L10[2], L10[3]] + L10[5:] + [R, D, M, AO]  # vedanā … paññā, rāgo, doso, moho, anottappaṃ


def katva(x):
    """X-ena sahajātāti katvā X-sikāti?  (ch7 «Có phải vì cho rằng chúng …, chúng … không?»)"""
    return f"vì cho rằng chúng cùng sinh với {x}, chúng là yếu tố đồng hành với {x}"


# ================================================================ (66) Dāna
TH4 = f"{CD} là sự bố thí"                                # cetasiko dhammo dānaṃ
DPOS, DNEG = C10.DPOS, C10.DNEG                           # iṭṭhaphalaṃ … sukhavipākaṃ / aniṭṭhaphalaṃ … (ch10)
IT = "Đức Thế Tôn đã nói rằng sự bố thí có quả đáng mong muốn"   # dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā (ch12 frame)
REQ_DANA = "đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh"   # (pi-2, ch10 REQ)
GIL = "thuốc men và vật dụng chữa bệnh"                   # gilānapaccayabhesajjaparikkhāro (pi-2)
CIV = C12.CIVARA                                          # cīvaraṃ «y phục»
DD = "vật để bố thí"                                      # deyyadhammo
TH_DD = f"{DD} là sự bố thí"


def give(x):
    """labbhā X paresaṃ dātuṃ (ch12 «có thể …»)"""
    return f"có thể cho người khác {x}"


NOTE_UP = f"[giống với câu hỏi của {B.PARAVADI} sẽ được nói ở phần sau, cần tham khảo Chú giải]"
# [upari vuccamānāya paravādīpucchāya sadisā, aṭṭhakathā oloketabbā]
AGG = "được biết là bậc nhất, được biết là lâu đời, được biết là thuộc dòng truyền thống, cổ xưa"
# aggañña rattañña vaṃsañña porāṇa
QUAL = C5.QUAL                                            # asaṅkiṇṇā … appaṭikuṭṭhā samaṇehi brāhmaṇehi viññūhi (ch5)
ABH = "sự không sợ hãi, ban sự không thù địch, ban sự không thù hằn"   # abhayaṃ deti averaṃ deti abyābajjhaṃ deti
# (avera / abyāpajja «không thù địch, không thù hằn» pi-2 ^appamaññā)
SURA = "việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"   # (pi-2, pi-4)
PANA = "việc sát hại sinh mạng"                           # (pi-2, pi-4)


def gift(x, var=""):
    """X-ā paṭivirato, bhikkhave, ariyasāvako … bhāgī hoti."""
    return (f"Này các tỳ-khưu, vị đệ tử cao quý, khi kiêng tránh {x}, ban cho vô lượng chúng sinh sự không sợ hãi, "
            f"ban sự không thù địch, ban sự không thù hằn{var}. Sau khi ban cho vô lượng chúng sinh {ABH}, được "
            "hưởng phần trong sự không sợ hãi, sự không thù địch, sự không thù hằn vô lượng.")


DANA5 = (
    f"“Này các tỳ-khưu, có năm sự bố thí này là những sự bố thí lớn, {AGG}, {QUAL}! Năm điều nào? Này các "
    f"tỳ-khưu, ở đây, vị đệ tử cao quý, sau khi dứt bỏ {PANA}, kiêng tránh {PANA}. "
    f"{gift(PANA, f' [{SPELL} (Syā., Ka.): abyāpajjhaṃ]')} "
    f"Này các tỳ-khưu, đây là sự bố thí thứ nhất, sự bố thí lớn, {AGG}, {QUAL}. Lại nữa, này các tỳ-khưu, vị "
    "đệ tử cao quý, sau khi dứt bỏ việc lấy của không được cho… sau khi dứt bỏ hành vi sai trái trong các dục "
    f"lạc… sau khi dứt bỏ việc nói dối… sau khi dứt bỏ {SURA}, kiêng tránh {SURA}. {gift(SURA)} "
    f"Này các tỳ-khưu, đây là sự bố thí thứ năm, sự bố thí lớn, {AGG}, {QUAL}. Này các tỳ-khưu, đây là năm sự "
    f"bố thí, những sự bố thí lớn, {AGG}, {QUAL}” [Tăng Chi Bộ Kinh 8.39].")
GIVE10 = ("“Ở đây, có người cho thức ăn, cho thức uống, cho vải, cho xe cộ, cho vòng hoa, cho hương thơm, cho dầu "
          "thoa, cho giường nằm, cho chỗ ở, cho đèn đuốc”")   # annaṃ … padīpeyyaṃ deti (pi-4 ^4 list)

# ================================================================ (67) Paribhogamaya puñña
TH5 = f"{KX[5]} tăng trưởng"                              # paribhogamayaṃ puññaṃ vaḍḍhati
DAY = "người bố thí, sau khi thực hiện sự bố thí"         # dāyako dānaṃ datvā (dāna «sự bố thí» kept)
VERBS = ["hướng đến", "chú hướng", "lưu ý", "chú tâm", "khởi chủ ý", "ước nguyện", "mong cầu"]
# āvaṭṭeti, ābhoga, samannāharati, manasikaroti, ceteti, pattheti, paṇidahati (pi-2 ^2-936 nouns)
ATT_L = ["sự hướng đến", "sự chú hướng", "sự lưu ý", "sự chú tâm", "chủ ý", "sự ước nguyện", "sự mong cầu"]
# āvaṭṭanā ābhogo samannāhāro manasikāro (pi-2 ^2-936) cetanā (core) patthanā paṇidhi (ch11)
ATT = ", ".join(ATT_L)
ATT_PE = f"{ATT_L[0]}… {ATT_L[-1]}"                       # āvaṭṭanā…pe… paṇidhi
TWO_PE = C11.TWO.replace("tiếp xúc, hai", "tiếp xúc… hai")  # dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ
KSD = ("các hiện tượng thiện và bất thiện, có lỗi và không có lỗi, thấp kém và ưu việt, đen tối và trong sáng "
       "cùng với các mặt đối lập của chúng")              # kusalākusalā … kaṇhasukkasappaṭibhāgā dhammā (pi-4 ^4-104)
KSD_A = f"{KSD} đi đến chỗ cùng hiện diện đối mặt nhau"   # … sammukhībhāvaṃ āgacchanti (ch5 sammukhībhāvo)
FAR = "điều rất xa cách nhau"                             # suvidūravidūra
Q4 = ("dòng chảy thiện, là dưỡng chất của hạnh phúc, thuộc về cõi trời, có kết quả hạnh phúc, dẫn đến cõi trời")
# kusalābhisandā sukhassāhārā sovaggikā sukhavipākā (ch10 «có kết quả hạnh phúc») saggasaṃvattanikā
LEAD = "đưa đến điều đáng mong muốn, đáng yêu thích, đáng ưa thích, đến lợi ích, đến hạnh phúc"
# iṭṭhāya kantāya (ch10) manāpāya (pi-2 «đáng ưa thích») hitāya sukhāya saṃvattati
CS = "sự định tâm không thể đo lường của tâm"             # appamāṇaṃ cetosamādhiṃ (appamāṇa pi-1)
AB4 = (
    f"“Này các tỳ-khưu, có bốn dòng chảy phước này, {Q4}, {LEAD}! Bốn điều nào? Này các tỳ-khưu, khi vị tỳ-khưu "
    f"thọ hưởng {CIV} của người nào mà chứng nhập và an trú {CS}, thì dòng chảy phước của người ấy không thể đo "
    f"lường, {Q4}, {LEAD}. Này các tỳ-khưu, khi vị tỳ-khưu thọ hưởng đồ ăn khất thực của người nào… thọ hưởng "
    f"chỗ ở… thọ hưởng {GIL} mà chứng nhập và an trú {CS}, thì dòng chảy phước của người ấy không thể đo lường, "
    f"{Q4}, {LEAD}. Này các tỳ-khưu, đây là bốn dòng chảy phước, {Q4}, {LEAD}” [Tăng Chi Bộ Kinh 4.51].")
R1 = "người bố thí thực hiện sự bố thí, người nhận, sau khi nhận, không thọ hưởng, vứt bỏ, cho đi"
R2 = ("người bố thí thực hiện sự bố thí, khi người nhận đã nhận, hoặc vua chúa lấy đi, hoặc kẻ trộm lấy đi, hoặc "
      "lửa thiêu đốt, hoặc nước cuốn trôi, hoặc những người thừa kế không ưa thích lấy đi")

# ================================================================ (68) Ito dinna
TH6 = "nhờ những gì được cho từ đây mà ở đó duy trì sự sống"   # ito dinnena tattha yāpenti
PETA = ("các ngạ quỷ tùy hỷ với người đang thực hiện sự bố thí vì lợi ích của họ, làm cho tâm trong sáng, làm sinh "
        "khởi sự hân hoan, có được niềm vui")             # petā (sample) … anumodenti … somanassaṃ paṭilabhanti
UPAK = "Cũng vậy, những gì được cho từ đây đem lại lợi ích cho các ngạ quỷ."   # Evameva ito dinnaṃ, petānaṃ upakappati.
PK = "các ngạ quỷ, những người đã qua đời"                # petā kālaṅkatā / petānaṃ kālaṅkatānaṃ
SON = "cha mẹ mong muốn có người con trai sinh ra trong gia đình"   # mātāpitaro puttaṃ icchanti kule jāyamānaṃ

# ================================================================ (69)-(70) kammavipāka
VIP = "quả của nghiệp"                                    # vipāko / kammavipāko (pi-1 vipākā, kammavipāka)
TH7 = f"đất là {VIP}"                                     # pathavī kammavipāko (pathavī «đất» pi-1)
JM = "sự lão hóa và sự chết"                              # jarāmaraṇaṃ (pi-2)
TH8 = f"{JM} là {VIP}"
VED = ["được cảm nhận là dễ chịu", "được cảm nhận là khó chịu", "được cảm nhận là không khó chịu cũng không dễ chịu"]
# sukhavedaniya / dukkhavedaniya / adukkhamasukhavedaniya
SAMP = [f"gắn liền với {SUV}", f"gắn liền với {DUV}", f"gắn liền với {ADV}", "gắn liền với sự tiếp xúc",
        "gắn liền với cảm giác", "gắn liền với tri giác", "gắn liền với chủ ý", "gắn liền với tâm"]   # (pi-1)
SAR, ANAR = "có đối tượng", "không có đối tượng"          # sārammaṇa / anārammaṇa (pi-3)
POS = ", ".join(VED + SAMP + [SAR])
NEG = ", ".join([f"không {x}" for x in VED + SAMP] + [ANAR])
POS_PE2 = (f"{', '.join(VED)}, gắn liền với {SUV}, khó chịu… {', '.join(SAMP[2:])}, {SAR}")
# sukhāya vedanāya sampayutto dukkhāya…pe… adukkhamasukhāya vedanāya sampayutto … sārammaṇo (^5-492 l.2)
POS_PE = f"{VED[0]}, {VED[1]}… {SAR}"                     # sukhavedaniyo dukkhavedaniyo…pe… sārammaṇo
NEG_PE = f"không {VED[0]}, không {VED[1]}… {ANAR}"        # na sukhavedaniyo na dukkhavedaniyo…pe… anārammaṇo
PG2 = "có thể bị nắm giữ và kìm kẹp, có thể bị cắt và bị đập vỡ"   # paggahaniggahupaga chedanabhedanupaga (ch5)
BUY = "có thể mua, bán, cầm cố, thu gom, chọn lựa"        # labbhā ketuṃ vikketuṃ āṭhapetuṃ ocinituṃ vicinituṃ
COMMON = "là thứ chung cho người khác"                    # paresaṃ sādhāraṇa (ch5 «là thứ chung cho …»)
CVS = C12.CVS                                             # cakkavattisatto (ch12)
ISS = "có nghiệp dẫn đến quyền uy, nghiệp dẫn đến quyền thống trị"   # issariya- / adhipaccasaṃvattaniyaṃ kammaṃ (ch10)
DUB = "có nghiệp dẫn đến sự xấu xí, nghiệp dẫn đến tuổi thọ ngắn"   # dubbaṇṇa- (pi-4 «xấu xí») / appāyuka-
KU, AK = "các hiện tượng thiện", "các hiện tượng bất thiện"
KA = "các hiện tượng thiện và bất thiện"                  # kusalānañca akusalānañca dhammānaṃ


def att(neg=False, pe=False, var=""):
    a = ATT_PE if pe else ATT.replace(ATT_L[0], ATT_L[0] + var, 1)
    return f"nó {'không ' if neg else ''}có {a}"


def jm(x):
    return f"{JM} của {x}"


def vp(x):
    return f"quả của {x}"


def nv(x, y):
    """X-ānaṃ dhammānaṃ jarāmaraṇaṃ, na vattabbaṃ – "Y-ānaṃ dhammānaṃ vipāko"ti? (ch11 «đối với X, không nên nói –»)"""
    return f"Có phải đối với {jm(x)}, không nên nói – “{vp(y)}” không?"


# ================================================================ (71) Ariyadhammavipāka
NAV = f"không có {KX[9]}"                                 # natthi ariyadhammavipāko
SAM_BR = "đời sống sa-môn có quả lớn, đời sống bà-la-môn có quả lớn"   # mahapphalaṃ sāmaññaṃ mahapphalaṃ brahmaññaṃ
FR_SO, FR_SA, FR_AN, FR_AR = C12.FR_SO, C12.FR_SA, C12.FR_AN, C12.FR_AR   # (pi-2, ch2, ch12)
FR_3 = f"{FR_SA}… {FR_AN}… {FR_AR}"
DP, SP, BP = "quả của sự bố thí", "quả của giới hạnh", "quả của sự tu tập"   # dāna- / sīla- / bhāvanāphala
SB = f"{SP}… {BP}"


def nvip(x):
    return f"{x} không phải là {VIP}"


def isvip(x):
    return f"{x} là {VIP}"


KUS = {k: f"điều thiện {v}" for k, v in (("kama", "thuộc cõi dục lạc"), ("rupa", "thuộc cõi hình sắc"),
                                         ("arupa", "thuộc cõi không hình sắc"), ("lok", "vượt thế gian"))}
RA = f"{KUS['rupa']}… thuộc cõi không hình sắc"           # rūpāvacaraṃ…pe… arūpāvacaraṃ kusalaṃ
RA2 = f"{KUS['rupa']}… {KUS['arupa']}"                    # rūpāvacaraṃ kusalaṃ…pe… arūpāvacaraṃ kusalaṃ
ACAYA, APACAYA = "dẫn đến sự tích lũy", "dẫn đến sự giảm trừ"   # ācayagāmī / apacayagāmī (pi-1)

# ================================================================ (72) Vipāko vipākadhammadhammo
VDD = "hiện tượng có khả năng sinh ra quả"                # vipākadhammadhammo (pi-1 «có khả năng sinh ra quả»)
TH10 = f"{VIP} là {VDD}"
AN4 = f"bốn khối không có hình sắc, là {VIP}, làm điều kiện cho nhau"   # vipākā cattāro khandhā arūpino aññamaññapaccayā

# ================================================================ uddāna
UDD = (f"Sự gộp vào, điều gắn liền, {CD}, sự bố thí là {CET}, {TH5}, {TH6}, {TH7}, {TH8}, {NAV}, {TH10}.")
# Saṅgaho, sampayutto, cetasiko dhammo, cetasikaṃ dānaṃ, paribhogamayaṃ puññaṃ vaḍḍhati, ito dinnena tattha
# yāpenti, pathavī kammavipāko, jarāmaraṇaṃ vipāko, natthi ariyadhammavipāko, vipāko vipākadhammadhammoti.


def build():
    d = B.Doc()
    d.head(3, VAGGA7, "5-15-0")
    # ------------------------------------------------------------ (63) Saṅgahita
    d.head(4, f"(63) 1. {K(x=KX[1])}", "5-15-1-0")
    sj = {s: f"tri giác {SJ} {s}" for s in ("mắt", "tai", "ý")}
    cj = {s: f"chủ ý {SJ} {s}" for s in ("mắt", "ý")}
    d.seg("5-471",
          f"Có phải {NO_SG} không [{SPELL} (Pī.): saṅgahītāti]? {AM} {NANU(GAN)} {AM} {hanci_no(GAN, NO_SG)}",
          f"{unit(cap(AY[0]), AY[0], RK, f' [{SPELL} (Sī., Pī., Ka.): katamaṃ khandhagaṇanaṃ]')} "
          f"{unit(cap(chain(AY[1:5])), AY[4], RK)}",
          unit(cap(chain(AY[5:10])), AY[9], RK),
          f"{unit(cap(SUV), SUV, VK)} {unit(cap(chain([DUV, ADV])), ADV, VK)}",
          f"{unit(cap(sj['mắt']), sj['mắt'], SK)} {unit(cap(chain([sj['tai'], sj['ý']])), sj['ý'], SK)}",
          unit(cap(chain([cj['mắt'], cj['ý']])), cj['ý'], KHK),
          unit(cap(chain(["thức qua mắt", "ý thức"])), "ý thức", WK))
    d.seg("5-472",
          f"Có phải giống như {OX}; cũng vậy, những hiện tượng ấy {SG} những hiện tượng kia không {SK_NOTE}? "
          f"Nếu {OX}, {B.TENA_VATA} “{SOME_SG}” {SK_NOTE}.",
          E(x=KX[1]))
    # ------------------------------------------------------------ (64) Sampayutta
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)

    def cs(a, b):
        return f"{a} cùng sinh với {b}"

    def gl(a, b):
        return f"{a} gắn liền với {b}"

    d.seg("5-473",
          f"{Q(NO_SP)} {AM} {NANU(SP7)} {AM} {hanci_no(SP7, NO_SP)}",
          f"{Q(cs(VK, SK))} {AM} {hanci_yes(cs(VK, SK), gl(VK, SK))}",
          f"Có phải {VK} cùng sinh với {KHK}… với {WK} không? {AM} {hanci_yes(cs(VK, WK), gl(VK, WK))}",
          f"Có phải {SK}… {KHK}… {WK} cùng sinh với {VK}… với {SK}… với {KHK} không? {AM} "
          f"{hanci_yes(cs(WK, KHK), gl(WK, KHK))}")
    d.seg("5-474",
          "Có phải giống như dầu thấm vào, thâm nhập vào trong hạt mè, nước ép thấm vào, thâm nhập vào trong cây mía; "
          f"cũng vậy, những hiện tượng ấy thấm vào, thâm nhập vào trong những hiện tượng kia không? {NHP}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (65) Cetasika
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    pc = cs("sự tiếp xúc", "tâm")
    ao = cs(AO, "tâm")
    d.seg("5-475",
          f"{Q(NO_CET)} {AM} {NANU(SAHA8_C)} {AM} {hanci_no(SAHA8_C, NO_CET)}",
          f"{Q(pc)} {AM} {hanci_yes(pc, f'sự tiếp xúc là {CET}')} Có phải {chain(L12)} cùng sinh với tâm không? "
          f"{AM} {hanci_yes(ao, f'{AO} là {CET}')}")
    d.seg("5-476",
          f"{Q(katva('tâm'))} {AM} "
          f"Có phải vì cho rằng chúng cùng sinh với sự tiếp xúc, chúng là yếu tố đồng hành với sự tiếp xúc "
          f"[{VAR} (Pī., Chú giải): phassikāti] không? {AM} {Q(katva('tâm'))} {AM} "
          f"Có phải vì cho rằng chúng cùng sinh {chain(['với ' + x for x in L12])}, chúng là yếu tố đồng hành với "
          f"{AO} [{VAR} (?): anottappikāti] không? {AM}")
    d.seg("5-477",
          f"{Q(NO_CET)} {AM} {NANU_VUTTAM}",
          f"“Vì tâm này và các {CD},",
          "Đối với người đã hiểu rõ, chúng không phải là tự ngã;",
          "Sau khi biết cả hai điều ấy, thấp kém và ưu việt,",
          "Người thấy đúng đắn đã biết điều có bản chất tan rã”.",
          f"{ATTHEVA} {AM} {TENA_HI(f'có {CD}')}",
          f"{Q(NO_CET)} {AM} {NANU_VUTTAM} “Này Kê-vát-ta, ở đây, vị tỳ-khưu chỉ ra cả tâm của các chúng sinh "
          f"khác, của những người khác, chỉ ra cả những gì là {CET}, chỉ ra cả điều được hướng tâm đến, chỉ ra cả "
          "điều được duy trì tâm vào – ‘ý của ông là như thế này, ý của ông là như thế kia, tâm của ông là như "
          f"vậy’” [Trường Bộ Kinh 1.485]. {ATTHEVA} {AM} {TENA_HI(f'có {CD}')}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (66) Dāna
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-478",
          f"{Q(TH4)} {AM} {Q(give(CD))} {NHP} {q(give(CD))} {AM} {Q(give('sự tiếp xúc'))} {NHP} "
          f"{q(give(chain([L10[1], L10[2], L10[3]] + L10[5:])))} {NHP}")
    d_pos = f"sự bố thí {DPOS}"
    d.seg("5-479",
          f"Có phải không nên nói – {TH4} không? {AM} {Q(f'sự bố thí {DNEG}')} {NHP} {nanu_l(d_pos)} {AM} "
          f"{hanci_yes(d_pos, TH4)}",
          f"Có phải {IT}, {CIV} là sự bố thí không {NOTE_UP}? {AM} {Q(f'{CIV} {DPOS}')} {NHP} "
          f"có phải {IT}, {REQ_DANA} là sự bố thí không? {AM} {Q(f'{GIL} {DPOS}')} {NHP}")
    d.seg("5-480",
          f"{NVQ(TH4)} {AM} {NANU_VUTTAM}",
          "“Niềm tin, sự biết hổ thẹn và sự bố thí thiện,",
          "Những hiện tượng này được những người chân chính noi theo;",
          "Vì người ta nói đây là con đường thuộc cõi trời,",
          "Vì nhờ điều này mà người ta đi đến thế giới chư thiên” [Tăng Chi Bộ Kinh 8.32].",
          f"{ATTHEVA} {AM} {TENA_HI(TH4)}",
          f"{NVQ(TH4)} {AM} {NANU_VUTTAM} {DANA5} {ATTHEVA} {AM} {TENA_HI(TH4)}")
    d.seg("5-481",
          f"{NVQ(TH_DD)} {AM} {NANU_VUTTAM} {GIVE10} [Tương Ưng Bộ Kinh 3.362-391, hơi khác một chút]! "
          f"{ATTHEVA} {AM} {TENA_HI(TH_DD)}")
    d.seg("5-482",
          f"{Q(TH_DD)} {AM} {Q(f'{DD} {DPOS}')} {NHP} có phải {IT}, {CIV} là sự bố thí không? {AM} "
          f"{Q(f'{CIV} {DPOS}')} {NHP} có phải {IT}, đồ ăn khất thực là sự bố thí… chỗ ở là sự bố thí… {GIL} là "
          f"sự bố thí không? {AM} {Q(f'{GIL} {DPOS}')} {NHP} vậy thì không nên nói – “{TH_DD}”.",
          E(x=KX[4]))
    # ------------------------------------------------------------ (67) Paribhogamaya puñña
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    grow = ", ".join(f"{x} tăng trưởng" for x in [f"{L10[0]} phát sinh từ sự thọ hưởng"] + L10[1:])
    d.seg("5-483",
          f"{Q(TH5)} {AM} {Q(grow)} {NHP}",
          f"{Q(TH5)} {AM} Có phải tăng trưởng như dây leo, tăng trưởng như dây quấn, tăng trưởng như cây, tăng "
          f"trưởng như cỏ, tăng trưởng như đám cỏ lau không? {NHP}")
    v484 = f" [{SPELL} (Sī., Pī., Ka.): anāvaṭṭantassa; {VAR} (Syā.): anāvajjhantassa]"
    negs = chain([f"có đối với người không {v}" + (v484 if i == 0 else "") for i, v in enumerate(VERBS)])
    pos = chain([f"có đối với người {v}" for v in VERBS])
    d.seg("5-484",
          f"{Q(TH5)} {AM} {Q(f'{DAY}, không lưu ý, có phước')} {AM} Có phải {negs} không? {NHP} "
          f"{nanu_l(pos)} {AM} {hanci_no(pos, TH5)}")
    vit = (f"{DAY}, khởi lên sự hướng tâm đến dục lạc, khởi lên sự hướng tâm đến ác ý, khởi lên sự hướng tâm "
           "đến sự hãm hại, có phước")                      # kāma- / byāpāda- / vihiṃsāvitakkaṃ vitakketi (pi-2)
    d.seg("5-485",
          f"{Q(TH5)} {AM} {Q(vit)} {AM} {Q(TWO_PE)} {NHP} {q(TWO_PE)} {AM} {Q(KSD_A)} {NHP} {q(KSD_A)} {AM} "
          f"{NANU_VUTTAM} “Này các tỳ-khưu, có bốn {FAR} này! Bốn điều nào? Này các tỳ-khưu, bầu trời và mặt "
          f"đất – đây là {FAR} thứ nhất. Này các tỳ-khưu, bờ bên này của biển và bờ bên kia – đây là {FAR} thứ "
          f"hai. Này các tỳ-khưu, nơi mặt trời mọc lên và nơi lặn xuống – đây là {FAR} thứ ba. Này các tỳ-khưu, "
          f"giáo pháp của người hiền thiện và giáo pháp của kẻ không hiền thiện – đây là {FAR} thứ tư. Này các "
          f"tỳ-khưu, đây là bốn {FAR}.",
          "“Bầu trời thì xa, mặt đất thì xa,",
          "Bờ bên kia của biển, người ta cũng nói là xa;",
          "Nơi mặt trời mọc lên,",
          "Và nơi vầng sáng lặn xuống.",
          "“Người ta nói rằng còn xa hơn thế nữa,",
          "Là giáo pháp của người hiền thiện và giáo pháp của kẻ không hiền thiện;",
          "Sự gặp gỡ với người hiền thiện không bị hao mòn,",
          "Dù kéo dài bao lâu, vẫn y như vậy.",
          f"“Vì sự gặp gỡ với kẻ không hiền thiện nhanh chóng tàn phai [{VAR} (nhiều bản): khippaṃhaveti];",
          "Vì vậy, giáo pháp của người hiền thiện ở xa kẻ không hiền thiện” [Tăng Chi Bộ Kinh 4.47].",
          f"{ATTHEVA} {AM} {TENA_HI_NA(KSD_A)}")
    d.seg("5-486",
          f"{NVQ(TH5)} {AM} {NANU_VUTTAM}",
          "“Những người trồng vườn cây, trồng rừng, những người làm cầu;",
          "Những người cho trạm nước uống và giếng nước, cho chỗ trú ngụ.",
          "“Đối với họ, cả ngày lẫn đêm, phước luôn luôn tăng trưởng;",
          "Đứng vững trong Giáo Pháp, thành tựu về giới hạnh, những người ấy đi đến cõi trời” "
          "[Tương Ưng Bộ Kinh 1.47].",
          f"{ATTHEVA} {AM} {TENA_HI(TH5)}",
          f"{NVQ(TH5)} {AM} {NANU_VUTTAM} {AB4} {ATTHEVA} {AM} {TENA_HI(TH5)}")
    d.seg("5-487",
          f"{Q(TH5)} {AM} {Q(f'{R1}, có phước')} {AM} {hanci_no(f'{R1}, có phước', TH5, sep=';')}",
          f"{Q(TH5)} {AM} {Q(f'{R2}, có phước')} {AM} {hanci_no(f'{R2}, có phước', TH5, sep=';')}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (68) Ito dinna
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    d.seg("5-488",
          f"{Q(TH6)} {AM} Có phải từ đây cho {CIV}, ở đó thọ hưởng {CIV} ấy không? {NHP} có phải từ đây cho đồ ăn "
          f"khất thực, từ đây cho chỗ ở, từ đây cho {GIL}, từ đây cho món ăn cứng, từ đây cho món ăn mềm, từ đây "
          f"cho nước uống; ở đó thọ hưởng nước uống ấy không? {NHP}",
          f"{Q(TH6)} {AM} Có phải một người là người làm cho một người khác, hạnh phúc và khổ đau do người khác "
          f"làm, một người làm, một người khác cảm nhận không? {NHP}")
    d.seg("5-489", f"{NVQ(TH6)} {AM} {NANU(PETA)} {AM} {hanci_yes(PETA, TH6, sep=';')}")
    d.seg("5-490",
          f"{NVQ(TH6)} {AM} {NANU_VUTTAM}",
          "“Nước mưa rơi xuống chỗ cao, chảy xuôi về chỗ thấp;",
          UPAK,
          "“Như những dòng sông đầy nước làm đầy biển cả;",
          UPAK,
          "“Vì ở đó không có việc cày cấy, việc chăn bò không hiện hữu ở đó;",
          f"Không có việc buôn bán như thế, hay việc mua bán bằng vàng [{SPELL} (Sī., Pī.): kayakkayaṃ];",
          f"Nhờ những gì được cho từ đây, {PK}, duy trì sự sống ở đó” [Tiểu Tụng 7.6; Ngạ Quỷ Sự 19].",
          f"{ATTHEVA} {AM} {TENA_HI(TH6)}")
    d.seg("5-491",
          f"{NVQ(TH6)} {AM} {NANU_VUTTAM} “Này các tỳ-khưu, thấy rõ năm lý do này, {SON}! Năm điều nào? Được nuôi "
          "dưỡng, nó sẽ nuôi dưỡng chúng ta, hoặc nó sẽ làm công việc cho chúng ta, dòng dõi gia đình sẽ tồn tại "
          f"lâu dài, nó sẽ nhận lấy gia tài, hoặc nữa, nó sẽ dâng phần cúng dường cho {PK} – này các tỳ-khưu, thấy "
          f"rõ năm lý do này, {SON}”.",
          "“Thấy rõ năm lý do, những người sáng suốt mong muốn có người con trai;",
          "Được nuôi dưỡng, nó sẽ nuôi dưỡng chúng ta, hoặc nó sẽ làm công việc cho chúng ta.",
          "“Dòng dõi gia đình có thể tồn tại lâu dài, nó nhận lấy gia tài;",
          "Hoặc nữa, nó sẽ dâng phần cúng dường cho các ngạ quỷ.",
          "“Thấy rõ những lý do này, những người sáng suốt mong muốn có người con trai;",
          "Vì vậy những người hiền thiện, những người chân chính, biết ơn và ghi nhớ ơn.",
          "“Nuôi dưỡng cha mẹ, nhớ lại những gì đã được làm trước đây;",
          "Làm các công việc của họ, như đối với những người đã làm ơn trước.",
          "“Làm theo lời khuyên dạy, nuôi dưỡng những người đã nuôi mình, không làm suy tàn dòng dõi gia đình;",
          "Có niềm tin, thành tựu về giới hạnh, người con trai ấy đáng được khen ngợi” [Tăng Chi Bộ Kinh 5.31].",
          f"{ATTHEVA} {AM} {TENA_HI(TH6)}",
          E(x=KX[6]))
    # ------------------------------------------------------------ (69) Pathavī kammavipāka
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    pv = f"đất là {VIP}, đất"
    ph = f"sự tiếp xúc là {VIP}, sự tiếp xúc"
    d.seg("5-492",
          f"{Q(TH7)} {AM} Có phải {POS}; {att(var=f' [{VAR} (Syā., Kaṃ.): āvajjanā]')} không? {NHP} "
          f"{nanu_l(f'{NEG}; {att(neg=True)}')} {AM} "
          f"{hanci_no(f'{NEG_PE}; {att(neg=True, pe=True)}', TH7)}",
          f"Có phải {ph} {POS_PE2}; {att(pe=True)} không? {AM} Có phải {pv} {POS}; {att()} không? {NHP} "
          f"có phải {pv} {NEG_PE}; {att(neg=True, pe=True)} không? {AM} "
          f"Có phải {ph} {NEG_PE}; {att(neg=True, pe=True)} không? {NHP}",
          f"{Q(TH7)} {AM} {Q(f'đất {PG2}')} {AM} {Q(f'{VIP} {PG2}')} {NHP}",
          f"Có phải {BUY} đất không? {AM} Có phải {BUY} {VIP} không? {NHP}")
    c_vip = f"{VIP} {COMMON}"
    oth = f"các chúng sinh khác thọ hưởng {VIP} của {CVS}"
    d.seg("5-493",
          f"{Q(f'đất {COMMON}')} {AM} {Q(c_vip)} {NHP}",
          f"{Q(c_vip)} {AM} {NANU_VUTTAM}",
          "“Không chung cho những người khác, là kho báu kẻ trộm không lấy đi được;",
          "Con người hãy làm các việc phước, nếu thực hành hành vi tốt” "
          "[Tiểu Tụng 8.9, trong Tiểu Tụng, hơi khác một chút].",
          f"{ATTHEVA} {AM} {TENA_HI_NA(c_vip)}",
          f"{Q(TH7)} {AM} {Q('đất hình thành trước, chúng sinh xuất hiện sau')} {AM} "
          f"{Q(f'{VIP} xuất hiện trước, sau đó tạo nghiệp để có được {VIP}')} {NHP}",
          f"{Q(f'đất là {VIP} của tất cả chúng sinh')} {AM} {Q('tất cả chúng sinh thọ hưởng đất')} {NHP} "
          f"{q('tất cả chúng sinh thọ hưởng đất')} {AM} "
          f"{Q('có những người không thọ hưởng đất mà nhập Niết-bàn trọn vẹn')} {AM} "
          f"{Q(f'có những người chưa làm cạn kiệt {VIP} mà nhập Niết-bàn trọn vẹn')} {NHP}",
          f"{Q(f'đất là {VIP} của {CVS}')} {AM} {Q('các chúng sinh khác thọ hưởng đất')} {AM} {Q(oth)} {NHP} "
          f"{q(oth)} {AM} {Q(f'các chúng sinh khác thọ hưởng {chain(L10, sep=chr(44) + chr(32))} của {CVS}')} {NHP}")
    d.seg("5-494",
          f"{NVQ(TH7)} {AM} {NANU(ISS)} {AM} {hanci_yes(ISS, TH7)}",
          E(x=KX[7]))
    # ------------------------------------------------------------ (70) Jarāmaraṇa
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    pj = f"{JM} là {VIP}, {JM}"
    d.seg("5-495",
          f"{Q(TH8)} {AM} Có phải {POS}; {att()} không? {NHP} {nanu_l(f'{NEG_PE}; {att(neg=True, pe=True)}')} "
          f"{AM} {hanci_no(f'{NEG_PE}; {att(neg=True, pe=True)}', TH8)}",
          f"Có phải {ph} {POS_PE}; {att(pe=True)} không? {AM} Có phải {pj} {POS_PE}; {att(pe=True)} không? {NHP}",
          f"Có phải {pj} {NEG_PE}; {att(neg=True, pe=True)} không? {AM} "
          f"Có phải {ph} {NEG_PE}; {att(neg=True, pe=True)} không? {NHP}")
    d.seg("5-496",
          f"{Q(f'{jm(AK)}, là {vp(AK)}')} {AM} {Q(f'{jm(KU)}, là {vp(KU)}')} {NHP}",
          f"{nv(KU, KU)} {AM} {nv(AK, AK)} {NHP}",
          f"{Q(f'{jm(KU)}, là {vp(AK)}')} {AM} {Q(f'{jm(AK)}, là {vp(KU)}')} {NHP}",
          f"{nv(AK, KU)} {AM} {nv(KU, AK)} {NHP}",
          f"{Q(f'{jm(KA)}, là {vp(AK)}')} {AM} {Q(f'{jm(KA)}, là {vp(KU)}')} {NHP}",
          f"{nv(KA, KU)} {AM} {nv(KA, AK)} {NHP}")
    d.seg("5-497",
          f"{NVQ(TH8)} {AM} {NANU(DUB)} {AM} {hanci_yes(DUB, TH8)}",
          E(x=KX[8]))
    # ------------------------------------------------------------ (71) Ariyadhammavipāka
    for lv, t, sid in heads(9):
        d.head(lv, t, sid)
    d.seg("5-498",
          f"{Q(NAV)} {AM} {NANU(SAM_BR)} {AM} {hanci_no(SAM_BR, NAV)}",
          f"{Q(NAV)} {AM} {NANU(f'có {FR_SO}')} {AM} {hanci_no(f'có {FR_SO}', NAV)} {NANU(f'có {FR_3}')} {AM} "
          f"{hanci_no(f'có {FR_AR}', NAV)}",
          f"{Q(nvip(FR_SO))} {AM} {Q(nvip(DP))} {NHP} {q(nvip(FR_SO))} {AM} {Q(nvip(SB))} {NHP}",
          f"{Q(nvip(FR_3))} {AM} {Q(nvip(DP))} {NHP} {q(nvip(FR_AR))} {AM} {Q(nvip(SB))} {NHP} "
          f"{q(isvip(DP))} {AM} {Q(isvip(FR_SO))} {NHP}",
          f"{Q(isvip(DP))} {AM} {Q(isvip(FR_3))} {NHP} {q(isvip(SB))} {AM} {Q(isvip(FR_SO))} {NHP} "
          f"{q(isvip(BP))} {AM} {Q(isvip(FR_3))} {NHP}")
    d.seg("5-499",
          f"{Q(KUS['kama'] + ' có quả')} {AM} {Q(KUS['lok'] + ' có quả')} {NHP} {q(RA2 + ' có quả')} {AM} "
          f"{Q(KUS['lok'] + ' có quả')} {NHP}",
          f"{Q(KUS['lok'] + ' không có quả')} {AM} {Q(KUS['kama'] + ' không có quả')} {NHP} "
          f"{q(KUS['lok'] + ' không có quả')} {AM} {Q(RA + ' không có quả')} {NHP}")
    ac = {k: f"{v} có quả, {ACAYA}" for k, v in KUS.items()}
    apc = {k: f"{v} có quả, {APACAYA}" for k, v in KUS.items()}
    d.seg("5-500",
          f"{Q(ac['kama'])} {AM} {Q(ac['lok'])} {NHP} {q(f'{RA} có quả, {ACAYA}')} {AM} {Q(ac['lok'])} {NHP}",
          f"{Q(apc['lok'])} {AM} {Q(apc['kama'])} {NHP} {Q(apc['lok'])} {AM} {Q(f'{RA} có quả, {APACAYA}')} {NHP}",
          E(x=KX[9]))
    # ------------------------------------------------------------ (72) Vipāko vipākadhammadhammo
    for lv, t, sid in heads(10):
        d.head(lv, t, sid)
    its = f"quả của nó là {VDD}"
    d.seg("5-501",
          f"{Q(TH10)} {AM} {Q(its)} {NHP} {q(its)} {AM} Có phải đối với từng cái một, không có việc đi đến tận "
          "cùng của khổ đau, không có sự cắt đứt vòng xoay, không có sự nhập Niết-bàn trọn vẹn không còn bám víu "
          f"không? {NHP}",
          f"{Q(TH10)} {AM} Có phải gọi là {VIP} hay gọi là {VDD}, gọi là {VDD} hay gọi là {VIP}, {C9.SAME} "
          f"không? {NHP}",
          f"{Q(TH10)} {AM} Có phải {VIP} và {VDD}, {VDD} và {VIP}, {SAHA8} không? {NHP}",
          f"{Q(TH10)} {AM} Có phải chính cái ấy là bất thiện, nó là quả của điều bất thiện, chính cái ấy là thiện, "
          f"nó là quả của điều thiện không? {NHP}",
          f"{Q(TH10)} {AM} Có phải với chính tâm nào mà giết hại sinh mạng thì với chính tâm ấy bị thiêu đốt trong "
          "địa ngục, với chính tâm nào mà thực hiện sự bố thí thì với chính tâm ấy vui hưởng ở cõi trời không? "
          f"{NHP}")
    d.seg("5-502",
          f"{NVQ(TH10)} {AM} {NANU(AN4)} {AM} {hanci_yes(AN4, TH10)}",
          E(x=KX[10]),
          f"{VAGGA7}.",
          C9.TASSUDDANAM,
          UDD)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("Các hiện tượng có đối tượng được gộp vào bốn khối", 3), ("gắn liền với cảm giác dễ chịu", 1),
    ("Các hiện tượng là yếu tố đồng hành với tâm", 1), ("đi kèm, cùng sinh, hòa lẫn, gắn liền với", 2),
    ("tri giác sinh từ sự tiếp xúc của mắt", 2), ("tri giác sinh từ sự tiếp xúc của ý", 2),
    ("chủ ý sinh từ sự tiếp xúc của mắt", 2), ("chủ ý sinh từ sự tiếp xúc của ý", 2),
    ("thức qua mắt, thức qua tai, thức qua mũi, thức qua lưỡi, thức qua thân, ý thức", 2),
    ("khối vật chất", 2), ("khối tạo tác", 2), ("khối thức", 2), ("chỗ dựa", 1),
    ("sự hướng đến, sự hướng đến liên tục, sự chú hướng, sự lưu ý, sự chú tâm", 2),
    ("sự hướng tâm đến dục lạc", 2), ("sự hướng tâm đến ác ý", 2), ("sự hướng tâm đến sự hãm hại", 2),
    ("có lỗi và không có lỗi", 4), ("thấp kém và ưu việt", 4),
    ("đen tối và trong sáng cùng với các mặt đối lập của chúng", 4), ("người chân chính", 4),
    ("thức ăn, thức uống, vải, xe cộ, vòng hoa, hương thơm, dầu thoa, giường nằm, chỗ ở, đèn đuốc", 4),
    ("sau khi dứt bỏ việc sát hại sinh mạng, kiêng tránh việc sát hại sinh mạng", 4),
    ("việc lấy của không được cho", 2), ("hành vi sai trái trong các dục lạc", 2), ("việc nói dối", 2),
    ("việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả", 2), ("không thể đo lường", 1),
    ("thuộc về phước", 2), ("đáng ưa thích", 2), ("chúng sinh khác", 2),
    ("Các hiện tượng là quả của nghiệp", 1), ("cũng không phải quả của nghiệp", 1),
    ("Các hiện tượng có khả năng sinh ra quả", 1), ("là quả của các hiện tượng thiện và bất thiện", 1),
    ("Các hiện tượng dẫn đến sự tích lũy", 1), ("dẫn đến sự giảm trừ", 1), ("sự lão hóa và sự chết", 2),
    ("thuộc cõi dục lạc", 1), ("thuộc cõi hình sắc", 1), ("thuộc cõi không hình sắc", 1), ("vượt thế gian", 1),
    ("chứng nhập và an trú", 1), ("hành vi tốt", 1), ("địa ngục", 2), ("thế giới cõi trời", 2), ("Lại nữa", 4),
    ("Ở đời này, có người", 4), ("không phải là tự ngã", 2), ("thế giới chư thiên", 2), ("xấu xí", 4),
    ("nhập Niết-bàn trọn vẹn", 4), ("sự hân hoan", 1), ("sự không biết ghê sợ tội lỗi", 1), ("thành tựu về", 4),
    ("bà-la-môn", 2), ("có đối tượng", 3), ("cảm giác không khó chịu cũng không dễ chịu", 2),
    ("thành quả vào dòng", 2), ("thành quả A-la-hán", 2), ("sự tạo tác", 2), ("không thù địch, không thù hằn", 2),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (DPOS, "10-dutiyavaggo.md"), (DNEG, "10-dutiyavaggo.md"), ("sự bố thí", "10-dutiyavaggo.md"),
    ("hạnh phúc do quyền uy", "10-dutiyavaggo.md"), ("hạnh phúc do quyền thống trị", "10-dutiyavaggo.md"),
    ("thuộc về con đường", "10-dutiyavaggo.md"), (QUAL, "5-sabbamatthitikatha.md"),
    (PG2, "5-sabbamatthitikatha.md"), ("là thứ chung cho quạ", "5-sabbamatthitikatha.md"),
    ("cùng hiện diện đối mặt nhau", "5-sabbamatthitikatha.md"), ("Tương Ưng Bộ Kinh", "5-sabbamatthitikatha.md"),
    (C11.TWO, "11-tatiyavaggo.md"), ("một người làm, một người khác cảm nhận", "1-puggalakatha.md"),
    (C9.SAME, "1-puggalakatha.md"), ("hơi khác một chút]", "1-puggalakatha.md"), ("ngạ quỷ", "1-puggalakatha.md"),
    (CVS, "12-catutthavaggo.md"), (FR_AR, "12-catutthavaggo.md"), (f"{CIV}, đồ ăn khất thực", "10-dutiyavaggo.md"),
    ("Có phải vì cho rằng chúng", "7-ekaccam-atthitikatha.md"), ("không có quả", "7-ekaccam-atthitikatha.md"),
    (C9.TASSUDDANAM, "9-hevatthikatha.md"), ("vị đệ tử cao quý", "3-brahmacariyakatha.md"),
    ("Tiểu Tụng", "3-brahmacariyakatha.md"), ("Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("thọ hưởng", "8-satipatthanakatha.md"), (FR_SO, "2-parihanikatha.md"), ("sự tụ hợp", "4-jahatikatha.md"),
    ("dẫn đến sự giảm trừ", "4-jahatikatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    missing += [(s, f) for s, f in PI5 if s not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch15 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
