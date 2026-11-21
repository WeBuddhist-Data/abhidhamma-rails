"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 16, Aṭṭhamavaggo (^5-16-0 … ^5-546): eleven kathās
(73-83) with the repeated "Aṭṭhamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/16-atthamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, katha, katha_end, vaggo, var, var_sp …). Strings taken from pi-1 … pi-4 rails are asserted
there (REUSED16); strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-16.md.

usage: python -I -X utf8 -B build_rails_16_vi.py          (writes the chapter and the adherence copy rails\\adh-16\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "16-atthamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
RE, CIT, A = S.RE, S.CIT, S.A


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(8)                                     # Aṭṭhamavaggo «Chương thứ tám» (termbase)
AB = "sự hiện hữu trong khoảng giữa"                   # antarābhavo (termbase)
KG, KD = "các loại dục lạc", "cõi dục lạc"             # kāmaguṇā / kāmadhātu (termbase)
RDH, ARDH = "cõi hình sắc", "cõi không hình sắc"       # rūpadhātu / arūpadhātu (termbase)
KATHA = {1: "sáu cõi tái sinh", 2: AB, 3: KG, 4: "các dục lạc", 5: RDH, 6: ARDH,
         7: f"các lĩnh vực nhận biết ở {RDH}", 8: f"vật chất trong {ARDH}", 9: "việc vật chất là nghiệp",
         10: "năng lực sống", 11: "nghiệp làm nguyên nhân"}
#   Chagati-, Antarābhava-, Kāmaguṇa-, Kāma- (termbase «Bàn về các dục lạc»), Rūpadhātu-, Arūpadhātu-,
#   Rūpadhātuyāāyatana-, Arūpe rūpa-, Rūpaṃ kammanti- (termbase «vật chất là nghiệp»), Jīvitindriya-, Kammahetukathā
TASSUDDANAM = "Tóm tắt của chương này –"               # Tassuddānaṃ – (ch9)

# ---------------------------------------------------------------------------------------------------------------
# Recurring phrases
# ---------------------------------------------------------------------------------------------------------------
VR = "Đức Thế Tôn đã nói rằng"                         # … vuttā / vuttaṃ bhagavatā (ch4, ch14)
KB, RB, ARB = "sự hiện hữu ở cõi dục lạc", "sự hiện hữu ở cõi hình sắc", "sự hiện hữu ở cõi không hình sắc"  # (pi-2)
GATI6 = "cõi tái sinh, nơi cư trú của chúng sinh, vòng luân hồi, cách sinh, chỗ trú của thức, sự có được sự tồn tại cá nhân"
BHAVO7 = f"sự hiện hữu, {GATI6}"                       # bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho
BH_PE = f"sự hiện hữu, cõi tái sinh{PE} sự có được sự tồn tại cá nhân"   # bhavo gati…pe… attabhāvapaṭilābho
BORN = "sinh ra, già đi, qua đời, chết đi, tái sinh"   # jāyanti jīyanti mīyanti cavanti upapajjanti (termbase)
K5 = "vật chất, cảm giác, tri giác, các tạo tác, thức"  # rūpaṃ vedanā saññā saṅkhārā viññāṇaṃ
K4 = "cảm giác, tri giác, các tạo tác, thức"
PV5, PV4 = "sự hiện hữu gồm năm khối", "sự hiện hữu gồm bốn khối"         # (pi-2)
RUPA, VED = "vật chất", "cảm giác"
BUD_L = "các bậc Tự Giác Ngộ Hoàn Toàn xuất hiện, các bậc Độc Giác xuất hiện, cặp đệ tử chính xuất hiện"  # (ch3)


def kam(x):                         # atthi X-ūpagaṃ kammaṃ
    return f"có nghiệp đi đến {x}"


def sat(x):                         # atthi X-ūpagā sattā
    return f"có chúng sinh đi đến {x}"


def born(x):                        # X-e sattā jāyanti … upapajjanti
    return f"trong {x}, chúng sinh {BORN}"


def khs(x, k=K5):                   # X-e atthi rūpaṃ vedanā …
    return f"trong {x} có {k}"


def isbh(x):                        # X bhavo gati … attabhāvapaṭilābho
    return f"{x} là {BHAVO7}"


def bud(x):                         # X-e sammāsambuddhā uppajjanti, … sāvakayugaṃ uppajjati
    return f"trong {x}, {BUD_L}"


def six(where):                     # rūpabhavo rūpagati … rūpattabhāvapaṭilābho
    items = ["sự hiện hữu", "cõi tái sinh", "nơi cư trú của chúng sinh", "vòng luân hồi", "cách sinh",
             "sự có được sự tồn tại cá nhân"]
    return ", ".join(f"{x} ở {where}" for x in items)


def six_pe(where):                  # rūpabhavo rūpagati…pe… rūpattabhāvapaṭilābho
    return f"sự hiện hữu ở {where}, cõi tái sinh ở {where}{PE} sự có được sự tồn tại cá nhân ở {where}"


# (73) Chagatikathā
T1 = "có sáu cõi tái sinh"                             # cha gatiyo
FIVE = "địa ngục, cõi súc sinh, cõi ngạ quỷ, loài người, chư thiên"   # nirayo … devā (pi-2, termbase)
P5 = f"{VR} có năm cõi tái sinh – {FIVE}"
KALA = "các a-tu-la Ka-la-kan-chi-ka"                  # kālakañcikā asurā
KALA_V = " [khác chính tả (Sī., Syā., Kaṃ.): kālakañjikā; (Pī.): kāḷakañjakā]"
VEPA = "hội chúng của Vê-pa-chít-ti"                   # vepacittiparisā (termbase Vê-pa-chít-ti, parisā)


def same(x):                        # X-ānaṃ samānavaṇṇā … X-ehi saha āvāhavivāhaṃ gacchanti
    return (f"có dung sắc tương đồng, có sự hưởng thụ tương đồng, có thức ăn tương đồng, có tuổi thọ tương đồng "
            f"với {x}, cưới gả cùng với {x}")


PETA = "các ngạ quỷ"                                   # petānaṃ / petehi (termbase)
ASURA = "có nhóm a-tu-la"                            # atthi asurakāyo

# (74) Antarābhavakathā
T2 = f"{AB} tồn tại"                                   # atthi antarābhavo (existence thesis)


def between(a, b, neg=False):       # A-assa ca B-assa ca antare (n)atthi antarābhavo
    return f"giữa {a} và {b}, {AB} {'không ' if neg else ''}tồn tại"


def ab(who, neg=False):             # X-assa (n)atthi antarābhavo
    return f"đối với {who}, {AB} {'không ' if neg else ''}tồn tại"


ORD5 = ("đó là cách sinh thứ năm, cõi tái sinh thứ sáu, chỗ trú của thức thứ tám, "
        "nơi cư trú của chúng sinh thứ mười")          # Pañcamī sā yoni, chaṭṭhamī sā gati, aṭṭhamī … dasamo so sattāvāso
ALL = "tất cả chúng sinh"                              # sabbesaññeva sattānaṃ
ANA, NANA = "người tạo nghiệp có quả không gián đoạn", "người không tạo nghiệp có quả không gián đoạn"
NIRU, ASAU = "người đi đến địa ngục", "người đi đến cõi chúng sinh Vô Tưởng"   # nirayūpaga / asaññasattūpaga
ARUU, NARUU = "người đi đến cõi không hình sắc", "người không đi đến cõi không hình sắc"   # (na) arūpūpaga
APN = "người nhập Niết-bàn trọn vẹn trong khoảng giữa"                # (pi-4)
UPN = "người nhập Niết-bàn trọn vẹn khi gần mạng chung"               # (pi-4)
ASN = "người nhập Niết-bàn trọn vẹn không có sự thúc đẩy"             # (pi-4)
SSN = "người nhập Niết-bàn trọn vẹn có sự thúc đẩy"                   # (pi-4)


def kv(x, y, low=False):            # Xti katvā Yti? (ch5)
    return f"{'c' if low else 'C'}ó phải vì cho rằng {x}, {y} không?"


# (75) Kāmaguṇakathā, (76) Kāmakathā
T3 = f"chỉ năm loại dục lạc là {KD}"                   # pañceva kāmaguṇā kāmadhātu
T4 = "chỉ năm lĩnh vực nhận biết là các dục lạc"       # pañcevāyatanā kāmā (termbase)
TP = "liên quan đến chúng"                             # tappaṭisaññutto / tappaṭisaṃyutto (termbase)
LIST9 = ["sự tham đắm", "ý muốn", "sự tham đắm do ý muốn", "tư duy", "sự tham đắm", "sự tham đắm do tư duy",
         "sự hân hoan", "niềm vui", "sự hân hoan và niềm vui"]
#   rāgo chando chandarāgo saṅkappo rāgo saṅkapparāgo pīti somanassaṃ pītisomanassaṃ (pi-2 chandarāga, saṅkapparāga)
CH_TP = f"có ý muốn {TP}"
LIST9_TP = "có " + ", ".join(f"{x} {TP}" for x in LIST9)
PS_TP = f"có sự hân hoan và niềm vui {TP}"
Q7 = "đáng mong muốn, đáng yêu mến, đáng ưa thích, có vẻ đáng yêu, gắn liền với dục lạc, hấp dẫn"
#   iṭṭhā kantā manāpā piyarūpā kāmūpasaṃhitā rajanīyā (termbase)
OPEN5 = "“Này các tỳ-khưu, có năm loại dục lạc này! Năm loại nào? Các hình sắc được nhận biết bằng mắt"
CLOSE5 = f"các vật xúc chạm được nhận biết bằng thân, {Q7} – này các tỳ-khưu, đây là năm loại dục lạc"
FIVE_FULL = (f"{OPEN5}, {Q7}, các âm thanh được nhận biết bằng tai{PE} các mùi được nhận biết bằng mũi{PE} "
             f"các vị được nhận biết bằng lưỡi{PE} {CLOSE5}”")
FIVE_SHORT = f"{OPEN5}{PE} {CLOSE5}"
VERSE1 = ["“Năm loại dục lạc trong thế gian, với ý là thứ sáu, đã được tuyên bố;",
          f"Ở đây, sau khi làm phai nhạt ý muốn, như vậy được giải thoát khỏi khổ đau” "
          f"[{CIT['su. ni.']} 173; {CIT['saṃ. ni.']} 1.30]."]
NIBB = f"{CIT['a. ni.']} 6.63, trong kinh Thấu Triệt"   # a. ni. 6.63 nibbedhikasutte (termbase nibbedhika)
VERSE2 = ["“Sự tham đắm do tư duy là dục lạc của con người,",
          "Những thứ muôn màu trong thế gian không phải là các dục lạc;",
          "Sự tham đắm do tư duy là dục lạc của con người,",
          "Những thứ muôn màu kéo dài cũng y như vậy trong thế gian;",
          f"Rồi ở đây, người trí dẹp bỏ ý muốn” [{NIBB}]."]


def eyes(x):                        # manussānaṃ X
    return f"{x} của loài người"


ORG = ["mắt", "tai", "mũi", "lưỡi", "thân", "ý"]       # cakkhu sotaṃ ghānaṃ jivhā kāyo mano (termbase)
NOT_KD = [f"{eyes(x)} không phải là {KD}" for x in ORG]   # manussānaṃ X na kāmadhātu


# (77) Rūpadhātukathā, (78) Arūpadhātukathā
RD, AD = "các hiện tượng thuộc vật chất", "các hiện tượng phi vật chất"   # rūpino / arūpino dhammā (termbase)
T5, T6 = f"{RD} là {RDH}", f"{AD} là {ARDH}"
SAVA2 = f"chính {KD} ấy là {RDH} ấy"                   # sāva kāmadhātu, sā rūpadhātu
SAVA2A = f"chính {KD} ấy là {ARDH} ấy"
SAVA3 = f"chính {KD} ấy là {RDH} ấy, là {ARDH} ấy"
SAM = f"người được trang bị {KB} thì được trang bị"    # kāmabhavena samannāgato puggalo … samannāgato hoti

# (79) Rūpadhātuyā āyatanakathā
SAL = "sự tồn tại cá nhân gồm sáu lĩnh vực nhận biết"  # saḷāyataniko attabhāvo
T7 = f"ở {RDH} có {SAL}"                               # atthi saḷāyataniko attabhāvo rūpadhātuyā
T7Q = f"{SAL} ở {RDH}"                                 # "saḷāyataniko attabhāvo rūpadhātuyā" (no atthi)
E, NO_, TO, BO = ("cakkhāyatana", "rūpāyatana"), ("ghānāyatana", "gandhāyatana"), ("jivhāyatana", "rasāyatana"), \
    ("kāyāyatana", "phoṭṭhabbāyatana")
SO_, MA = ("sotāyatana", "saddāyatana"), ("manāyatana", "dhammāyatana")
SENSE = {"cakkhāyatana": ("mắt", "thấy", "hình sắc"), "ghānāyatana": ("mũi", "ngửi", "mùi"),
         "jivhāyatana": ("lưỡi", "nếm", "vị"), "kāyāyatana": ("thân", "chạm", "vật xúc chạm"),
         "manāyatana": ("ý", "nhận biết", "đối tượng của ý")}
#   tena cakkhunā taṃ rūpaṃ passati / ghānena gandhaṃ ghāyati / jivhāya rasaṃ sāyati / kāyena phoṭṭhabbaṃ phusati /
#   manena dhammaṃ vijānāti (termbase)


def at(x, neg=False):               # atthi / natthi tattha X
    return f"ở đó {'không ' if neg else ''}có {A[x]}"


def pr(p, neg=False):               # atthi tattha X, (n)atthi Y
    return f"ở đó có {A[p[0]]}, {'không ' if neg else ''}có {A[p[1]]}"


def use(p, neg=False):              # atthi tattha X atthi Y, (na ca) tena X-ena taṃ Y-ṃ Z-ti
    i, v, o = SENSE[p[0]]
    tail = f"nhưng bằng {i} ấy mà không {v} {o} ấy" if neg else f"bằng {i} ấy mà {v} {o} ấy"
    return f"{pr(p)}, {tail}"


GANDHA10 = ("mùi rễ cây, mùi lõi cây, mùi vỏ cây, mùi lá, mùi hoa, mùi trái cây, mùi tanh, mùi ôi thiu, "
            "mùi thơm, mùi hôi")                       # mūlagandho … duggandho (pi-1)
RASA16 = ("vị rễ cây, vị thân cây, vị vỏ cây, vị lá, vị hoa, vị trái cây, vị chua, vị ngọt, vị đắng, vị cay, "
          "vị mặn, vị kiềm, vị chua nhẹ, vị chát, vị ngon, vị không ngon")   # mūlaraso … asādu (pi-1)
TOUCH8 = ("cái cứng, cái mềm, cái mịn, cái thô ráp, cái mà khi tiếp xúc thì dễ chịu, cái mà khi tiếp xúc thì khó chịu, "
          "cái nặng, cái nhẹ")                         # kakkhaḷaṃ … lahukaṃ (pi-1)
NIM = "dấu hiệu của mũi, dấu hiệu của lưỡi, dấu hiệu của thân"   # ghāna- / jivhā- / kāyanimittaṃ (termbase nimittaṃ)

# (80) Arūpe rūpakathā
ARS = "các cõi không hình sắc"                         # arūpesu (termbase)
T8 = f"trong {ARS} có {RUPA}"                          # atthi rūpaṃ arūpesu
RIN = f"trong {RDH} có {RUPA}"                         # atthi rūpaṃ rūpadhātuyā
RIN_V = f"trong {RDH}{S.var('Mọi bản', 'arūpadhātuyā')} có {RUPA}"   # rūpadhātuyā [arūpadhātuyā (sabbattha)]
V5_PE, V4_PE = f"{PV5}, cõi tái sinh{PE} sự có được sự tồn tại cá nhân", f"{PV4}, cõi tái sinh{PE} sự có được sự tồn tại cá nhân"
CIT3 = f" [{CIT['itivu.']} 72; {CIT['a. ni.']} 5.200; Trường Bộ Kinh 3.321]"
NIS = f"{VR} lối thoát khỏi vật chất là phi vật chất"   # rūpānaṃ nissaraṇaṃ arūpaṃ vuttaṃ bhagavatā
NEKK = (f"{VR} lối thoát khỏi các dục lạc là sự từ bỏ, trong các sự từ bỏ có các dục lạc, trong những điều không phải "
        f"là đối tượng của ô nhiễm có các ô nhiễm, trong những điều không nằm trong các cõi tồn tại có những điều "
        f"nằm trong các cõi tồn tại")
#   kāmānaṃ nissaraṇaṃ nekkhammaṃ vuttaṃ bhagavatā, atthi nekkhammesu kāmā, atthi anāsavesu āsavā, atthi
#   apariyāpannesu pariyāpannā (pi-1 apariyāpannā «không nằm trong các cõi tồn tại»)


def so_ca(a, b):                    # atthi rūpaṃ X, so ca Y
    return f"{a}, và đó là {b}"


# (81) Rūpaṃ kammantikathā
CT, ACT = "tâm thiện", "tâm bất thiện"                 # kusalena / akusalena cittena (termbase)
KK, VK, MK = "nghiệp bằng thân", "nghiệp bằng lời nói", "nghiệp bằng ý"   # kāya- / vacī- / manokammaṃ (termbase)
ATT7 = "sự hướng đến, sự chú hướng, sự lưu ý, sự chú tâm, chủ ý, sự mong ước, sự mong cầu"
#   āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi (pi-2, termbase)
ATT_PE = f"sự hướng đến{PE} sự mong cầu"
ANR, PVP = "không có đối tượng", "không gắn liền với sự tiếp xúc"          # anārammaṇaṃ / phassavippayuttaṃ
ABY = "không xác định về mặt đạo đức"                  # abyākataṃ
IMP = "chất bất tịnh, nước mắt, máu, mồ hôi"           # asuci assu lohitaṃ sedo (termbase)
ELEM = f"yếu tố đất{PE} yếu tố nước{PE} yếu tố lửa{PE} yếu tố gió"


def kr(kk, c):                      # X-ena cittena samuṭṭhitaṃ kāyakammaṃ rūpaṃ
    return f"{kk}, là vật chất do {c} sinh ra"


def X(subj, mods, adj, comma=False):  # … (anārammaṇaṃ) (phassavippayuttaṃ) kusalaṃ / akusalaṃ / abyākataṃ
    if mods:
        return f"{subj}, {', '.join(mods)}, là {adj}"
    return f"{subj}{',' if comma else ''} là {adj}"


def has(full, neg=False):           # (n)atthi tassa āvaṭṭanā … paṇidhi
    return f"nó {'không ' if neg else ''}có {ATT7 if full else ATT_PE}"


def obj(neg=False):                 # sārammaṇaṃ / anārammaṇaṃ
    return f"nó {'không ' if neg else ''}có đối tượng"


def ph(c, adj, neg=False):          # X-ena cittena samuṭṭhito phasso X-o (an)ārammaṇo, (n)atthi tassa …
    return f"sự tiếp xúc do {c} sinh ra là {adj}, {'không ' if neg else ''}có đối tượng, {has(0, neg)}"


def kro(kk, c, adj, neg=False):     # … kāyakammaṃ rūpaṃ kusalaṃ (an)ārammaṇaṃ, (n)atthi tassa …
    return f"{kr(kk, c)}, là {adj}, {'không ' if neg else ''}có đối tượng, {has(0, neg)}"


def lst(c, adj, neg=False):         # X-ena cittena samuṭṭhitā vedanā…pe… paññā / anottappaṃ …
    if c == CT:
        items = ["tri giác", "chủ ý", "niềm tin", "sự tinh tấn", "sự tỉnh thức", "sự định tâm", "trí tuệ"]
    else:
        items = ["tri giác", "chủ ý", "sự tham đắm", "sự sân hận", "sự si mê", "sự kiêu mạn", "quan điểm",
                 "sự hoài nghi", "sự uể oải", "sự xao động", "sự không biết hổ thẹn",
                 "sự không biết ghê sợ tội lỗi"]
    head = f"cảm giác do {c} sinh ra{PE} " + f"{PE} ".join(items)
    return f"{head} là {adj}, {'không ' if neg else ''}có đối tượng, {has(0, neg)}"


def rlist(c, imp=False):            # X-ena cittena samuṭṭhitaṃ saddāyatanaṃ…pe… vāyodhātu (asuci assu lohitaṃ sedo)
    s = (f"lĩnh vực âm thanh do {c} sinh ra{PE} lĩnh vực mùi{PE} lĩnh vực vị{PE} lĩnh vực vật xúc chạm{PE} "
         f"{ELEM}")
    return s + (f", {IMP}" if imp else "")


def yam_kinci(c, adj):              # Yaṃ kiñci X-ena cittena samuṭṭhitaṃ rūpaṃ sabbaṃ taṃ X-anti (ch13 frame)
    return f"bất cứ vật chất nào do {c} sinh ra, tất cả đều là {adj}"


RK = "vật chất vừa là thiện vừa là bất thiện"          # rūpaṃ kusalampi akusalampi
KV2 = f"{KK}, {VK} vừa là thiện vừa là bất thiện"
LIST13 = (f"lĩnh vực tai{PE} lĩnh vực mũi{PE} lĩnh vực lưỡi{PE} lĩnh vực thân{PE} lĩnh vực hình sắc{PE} "
          f"lĩnh vực âm thanh{PE} lĩnh vực mùi{PE} lĩnh vực vị{PE} lĩnh vực vật xúc chạm{PE} {ELEM}, {IMP}")
KR2 = f"thân là vật chất, {KK} là vật chất"            # kāyo rūpaṃ, kāyakammaṃ rūpaṃ
VIN5 = [("lĩnh vực mắt", "thức qua mắt"), ("lĩnh vực tai", "thức qua tai"), ("lĩnh vực mũi", "thức qua mũi"),
        ("lĩnh vực lưỡi", "thức qua lưỡi"), ("lĩnh vực thân", "thức qua thân")]   # (pi-1 / pi-2)
T9 = "vật chất là nghiệp"                              # rūpaṃ kammaṃ (termbase)
SUT1 = (f"“Này các tỳ-khưu, Ta nói chủ ý là nghiệp; sau khi có chủ ý, người ta làm nghiệp bằng thân, bằng lời nói, "
        f"bằng ý” [{NIBB}]!")
#   cetanāhaṃ, bhikkhave, kammaṃ vadāmi; cetayitvā kammaṃ karoti kāyena vācāya manasā
HAN = S.var_sp(f"{CIT['saṃ. ni.']} 2.25", "hānanda")
SUT2 = (f"“Hoặc khi có thân, này A-nan{HAN}, do chủ ý bằng thân làm nguyên nhân mà sinh khởi sự dễ chịu và sự khó "
        f"chịu ở nơi bản thân; hoặc khi có lời nói, này A-nan{HAN}, do chủ ý bằng lời nói làm nguyên nhân mà sinh "
        f"khởi sự dễ chịu và sự khó chịu ở nơi bản thân; hoặc khi có ý, này A-nan{HAN}, do chủ ý bằng ý làm nguyên "
        f"nhân mà sinh khởi sự dễ chịu và sự khó chịu ở nơi bản thân” [{CIT['saṃ. ni.']} 2.25; {CIT['a. ni.']} 4.171]!")
#   kāye vā, ānanda, sati kāyasañcetanāhetu uppajjati ajjhattaṃ sukhadukkhaṃ …
BAD = "đưa đến sự khó chịu, có quả trổ khó chịu"       # dukkhudrayaṃ dukkhavipākaṃ (sample)
GOOD = "đưa đến sự dễ chịu, có quả trổ dễ chịu"        # sukhudrayaṃ sukhavipākaṃ (sample)
SUT3 = ("“" + "; ".join(
    f"{'Này' if k == 0 else 'này'} các tỳ-khưu, chủ ý bằng {w} gồm {n} loại là nghiệp {g} bằng {w}, {r}"
    for k, (n, w, g, r) in enumerate([("ba", "thân", "bất thiện", BAD), ("bốn", "lời nói", "bất thiện", BAD),
                                      ("ba", "ý", "bất thiện", BAD), ("ba", "thân", "thiện", GOOD),
                                      ("bốn", "lời nói", "thiện", GOOD), ("ba", "ý", "thiện", GOOD)]))
    + f"” [{CIT['a. ni.']} 10.217, nhưng hơi khác một chút]!")
#   tividhā, bhikkhave, kāyasañcetanā akusalaṃ kāyakammaṃ dukkhudrayaṃ dukkhavipākaṃ; … [a. ni. 10.217 thokaṃ pana visadisaṃ]
BLP = "Ba-liên-phất"                                   # pāṭaliputta (termbase hiền giả Ba-liên-phất)
SAMI = "người đàn ông rồ dại Sa-mít-thi"               # samiddhi moghapuriso (termbase mogha, puriso)


def sanc(feel, felt, first=False):  # sañcetaniyaṃ, āvuso pāṭaliputta, kammaṃ katvā … X-vedaniyaṃ X-ṃ so vedayati
    return (f"{'Này' if first else 'này'} hiền giả {BLP}, sau khi làm nghiệp có chủ ý, được cảm nhận là {feel}, bằng thân, bằng lời nói, "
            f"bằng ý, người ấy cảm nhận {felt}")


SUT4 = (f"“Này A-nan, nếu {SAMI} này, khi được du sĩ {BLP}{S.var(CIT['ma. ni.'] + ' 3.300', 'potaliputtassa')} "
        f"hỏi như vậy, trả lời như vậy – ‘"
        + "; ".join([sanc("dễ chịu", "sự dễ chịu", True), sanc("khó chịu", "sự khó chịu"),
                     sanc("không khó chịu cũng không dễ chịu", "sự không khó chịu cũng không dễ chịu")])
        + f"’, thì, này A-nan, khi trả lời như vậy, {SAMI} sẽ trả lời du sĩ {BLP} một cách đúng đắn” "
          f"[{CIT['ma. ni.']} 3.300]!")

# (82) Jīvitindriyakathā
RJ, AJ = "năng lực sống thuộc vật chất", "năng lực sống phi vật chất"   # rūpa- / arūpajīvitindriyaṃ (termbase)
T10 = f"{RJ} không tồn tại"                            # natthi rūpajīvitindriyaṃ
RL = "tuổi thọ, sự tồn tại, sự tiếp diễn, sự kéo dài, sự vận động, sự tiến triển, sự gìn giữ"
#   āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā (pi-1)
RA, AA = f"tuổi thọ của {RD}", f"tuổi thọ của {AD}"
BA = "tuổi thọ của các hiện tượng thuộc vật chất và phi vật chất"     # rūpīnañca arūpīnañca dhammānaṃ āyu
NSA = "người đang nhập sự chấm dứt"                    # nirodhaṃ samāpannassa (termbase)
ASA = "các chúng sinh Vô Tưởng"                        # asaññasattānaṃ (ch11)
KHA = "Nó nằm trong khối nào? Nằm trong khối tạo tác."   # Katamakkhandhapariyāpannanti? Saṅkhārakkhandhapariyāpannanti.
KH3 = f"khối cảm giác{PE} khối tri giác{PE} khối thức"
UPC = "tâm tìm cầu sự tái sinh"                        # upapattesiyaṃ cittaṃ (termbase)


def jv(who, neg=False):             # X-assa (n)atthi jīvitindriyaṃ
    return f"đối với {who}, năng lực sống {'không ' if neg else ''}tồn tại"


def call_n(x, j):                   # X na vattabbaṃ – "Y"nti
    return f"{x} không nên được gọi là – “{j}”"


def br(subj, how):                  # upapattesiyena cittena samuṭṭhitaṃ X upapattesiye citte bhijjamāne Y bhijjati
    return f"{subj} do {UPC} sinh ra, khi {UPC} đang tan rã, thì tan rã {how}"


# (83) Kammahetukathā
KH = "do nghiệp làm nguyên nhân"                       # kammahetu (termbase hetu «nguyên nhân»)
AR, ARH = S.PN["arahā"], "trạng thái A-la-hán"         # (pi-4; ch2)
SO, SA, AN = S.PN["sotāpanno"], S.PN["sakadāgāmī"], S.PN["anāgāmī"]
FRSO, FRAN = "thành quả vào dòng", "thành quả không trở lại"           # (ch2, termbase)
KM = ["nghiệp sát hại sinh mạng", "nghiệp lấy của không được cho", "nghiệp có hành vi sai trái trong các dục lạc",
      "nghiệp nói dối", "nghiệp nói lời chia rẽ", "nghiệp nói lời thô ác", "nghiệp nói lời phù phiếm",
      "nghiệp giết mẹ" + S.var_sp("Syā.", "mātughātakakammassa; (Ka.): mātughātikammassa, cũng vậy ở các từ "
                                          "pitughātaarahantaghātakammassa"),
      "nghiệp giết cha", "nghiệp giết bậc A-la-hán", "nghiệp làm chảy máu", "nghiệp chia rẽ Tăng đoàn"]
#   pāṇātipāta- … saṅghabhedakammassa (pi-2 / pi-4 / ch3 wording; termbase Pāṇātipātakammassa)
ABB = "vu khống các bậc A-la-hán"                      # arahantānaṃ abbhācikkhati (termbase)


def fall(who, frm, neg=False):      # kammahetu X Y-ā (na) parihāyati
    return f"{KH}, {who} {'không ' if neg else ''}sa sút khỏi {frm}"


UDDANA = (f"Sáu cõi tái sinh, {AB}, {T3}, {T4}, {T5}, {T6}, {T7Q}, {T8}, {T9}, vật chất là sự sống, "
          f"sa sút do nghiệp làm nguyên nhân.")
#   Cha gatiyo, antarābhavo, pañceva kāmaguṇā kāmadhātu, pañceva āyatanā kāmā, rūpino dhammā rūpadhātu, arūpino
#   dhammā arūpadhātu, saḷāyataniko attabhāvo rūpadhātuyā, atthi rūpaṃ arūpesu, rūpaṃ kammaṃ, rūpaṃ jīvitaṃ,
#   kammahetukā parihāyatīti.

REUSED16 = [  # (Pāli, Vietnamese, book)
    ("kāmabhavo, rūpabhavo, arūpabhavo", f"{KB}, {RB}, {ARB}", "2"),
    ("chandarāgo", "sự tham đắm do ý muốn", "2"), ("saṅkapparāgo", "sự tham đắm do tư duy", "2"),
    ("pettivisaya-", "cõi ngạ quỷ", "2"), ("tiracchānayoni-", "cõi súc sinh", "2"),
    ("āvaṭṭanā ābhogo samannāhāro", "sự hướng đến, sự chú hướng, sự lưu ý", "2"),
    ("adinnādānā", "lấy của không được cho", "2"), ("kāmesumicchācārā", "hành vi sai trái trong các dục lạc", "2"),
    ("pisuṇāvācā / pharusāvācā / samphappalāpa", "nói lời chia rẽ", "4"), ("pharusāvācā", "nói lời thô ác", "4"),
    ("samphappalāpino", "nói lời phù phiếm", "4"),
    ("antarāparinibbāyī", APN, "4"), ("upahaccaparinibbāyī", UPN, "4"), ("asaṅkhāraparinibbāyī", ASN, "4"),
    ("sasaṅkhāraparinibbāyī", SSN, "4"),
    ("mūlagandho … duggandho", GANDHA10, "1"),
    ("mūlaraso … lambilaṃ", "vị rễ cây, vị thân cây, vị vỏ cây, vị lá, vị hoa, vị trái cây, vị chua, vị ngọt, "
     "vị đắng, vị cay, vị mặn, vị kiềm, vị chua nhẹ", "1"),
    ("kasāvo sādu asādu", "vị chát, vị ngon, vị không ngon", "1"),
    ("kakkhaḷaṃ … lahukaṃ", TOUCH8, "1"),
    ("āyu ṭhiti yapanā yāpanā iriyanā", "tuổi thọ, sự tồn tại, sự tiếp diễn, sự kéo dài, sự vận động", "1"),
    ("vattanā pālanā", "sự tiến triển, sự gìn giữ", "1"),
    ("apariyāpannā", "không nằm trong các cõi tồn tại", "1"),
    ("sārammaṇā / anārammaṇā", "có đối tượng", "1"), ("anārammaṇā", "không có đối tượng", "1"),
    ("cittasamuṭṭhānā", "do tâm sinh ra", "1"),
    ("pañcavokārabhavo", PV5, "2"), ("catuvokārabhavo", PV4, "2"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "2"),
    ("rūpakkhandha … viññāṇakkhandha", "khối tạo tác", "2"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Nanu … vuttaṃ bhagavatāti?", f"Chẳng phải {VR}", "4-jahatikatha.md"),
    ("… sammāsambuddhā uppajjanti, paccekasambuddhā uppajjanti, sāvakayugaṃ uppajjati", BUD_L,
     "3-brahmacariyakatha.md"),
    ("mātughātakā … saṅghabhedakā", "kẻ giết mẹ, kẻ giết cha, kẻ giết bậc A-la-hán, kẻ làm chảy máu, kẻ chia rẽ "
     "Tăng đoàn", "3-brahmacariyakatha.md"),
    ("pāṇātipātino … kāmesumicchācārino", "có hành vi sai trái trong các dục lạc", "3-brahmacariyakatha.md"),
    ("arahā arahattā parihāyati", f"{AR} sa sút khỏi {ARH}", "2-parihanikatha.md"),
    ("sotāpattiphalaṃ", FRSO, "2-parihanikatha.md"),
    ("Xti katvā Yti?", "Có phải vì cho rằng", "5-sabbamatthitikatha.md"),
    ("…ti, āmantā.", "không, đúng vậy.", "5-sabbamatthitikatha.md"),
    ("bhavo gati sattāvāso saṃsāro yoni … attabhāvapaṭilābho",
     "cõi tái sinh, nơi cư trú của chúng sinh, vòng luân hồi, cách sinh", "11-tatiyavaggo.md"),
    ("attabhāvapaṭilābho", "sự có được sự tồn tại cá nhân", "11-tatiyavaggo.md"),
    ("asaññasatta", "chúng sinh Vô Tưởng", "11-tatiyavaggo.md"),
    ("Yaṃ kiñci X sabbaṃ taṃ Y", "nào, tất cả đều", "13-pancamavaggo.md"),
    ("ye keci X, sabbe te", "tất cả những người ấy đều", "13-pancamavaggo.md"),
    ("vīriyaṃ / sati / samādhi", "sự tinh tấn", "13-pancamavaggo.md"),
    ("vattabbaṃ – '…'nti", "nên được gọi là – “", "13-pancamavaggo.md"),
    ("anottappaṃ", "sự không biết ghê sợ tội lỗi", "5-sabbamatthitikatha.md"),
    ("… thokaṃ visadisaṃ (citation)", "hơi khác một chút", "1-puggalakatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED16 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        if i:
            lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    def kh(n, sub):                  # #### Aṭṭhamavaggo + ##### (N) k. X-kathā
        heading(f"5-16-{sub}-0", 4, VAGGA)
        heading(f"5-16-{sub}-1-0", 5, f"({72 + sub}) {sub}. {S.katha(KATHA[sub])}")

    heading("5-16-0", 3, VAGGA)

    # ---- (73) 1. Chagatikathā -----------------------------------------------------------------------------------
    heading("5-16-1-0", 4, f"(73) 1. {S.katha(KATHA[1])}")
    PK = f"{KALA} {same(PETA)}"
    PK_V = f"{KALA}{KALA_V} {same(PETA)}"
    PV = f"{VEPA} {same('chư thiên')}"
    PP = f"{VEPA} là chư thiên trước đây"
    add("5-503",
        f"{Q(T1)} {YES} {NANU(P5 + ' [' + CIT['ma. ni.'] + ' 1.153]')} {YES} {S.hanci_neg(P5, T1, ';')}",
        f"{Q(T1)} {YES} {NANU(PK_V)} {YES} {S.hanci_neg(PK, T1)}",
        f"{Q(T1)} {YES} {NANU(PV)} {YES} {S.hanci_neg(PV, T1)}",
        f"{Q(T1)} {YES} {NANU(PP)} {YES} {S.hanci_neg(PP, T1)}")
    add("5-504",
        f"{S.na_vattabbam(T1)} {YES} Chẳng phải {ASURA} sao, đúng vậy. {S.hanci(ASURA, T1)}",
        S.katha_end(KATHA[1]))

    # ---- (74) 2. Antarābhavakathā -------------------------------------------------------------------------------
    kh(2, 2)
    add("5-505",
        f"{Q(T2)} {YES} {Q(f'đó là {KB}')} {NO_PE} {q(T2)} {YES} {Q(f'đó là {RB}')} {NO_PE} {q(T2)} {YES} "
        f"{Q(f'đó là {ARB}')} {NO_PE} {q(T2)} {YES} {Q(between(KB, RB))} {NO_PE} {q(T2)} {YES} "
        f"{Q(between(RB, ARB))} {NO_PE}",
        f"{Q(between(KB, RB, True))} {YES} {S.hanci_neg(between(KB, RB, True), T2)} "
        f"{Q(between(RB, ARB, True))} {YES} {S.hanci_neg(between(RB, ARB, True), T2)}")
    add("5-506",
        f"{Q(T2)} {YES} {Q(ORD5)} {NO_PE} {q(T2)} {YES} {Q(isbh(AB))} {NO_PE} {q(kam(AB))} {NO_PE} "
        f"{q(sat(AB))} {NO_PE} {q(born(AB))} {NO_PE} {q(khs(AB))} {NO_PE} {q(f'{AB} là {PV5}')} {NO_PE}")

    def cmp(x, k, pv):
        return (f"{Q(f'{x} tồn tại, {isbh(x)}')} {YES} {Q(f'{AB} tồn tại, {isbh(AB)}')} {NO_PE} "
                f"{q(kam(x))} {YES} {Q(kam(AB))} {NO_PE} {q(sat(x))} {YES} {Q(sat(AB))} {NO_PE} "
                f"{q(born(x))} {YES} {Q(born(AB))} {NO_PE} {q(khs(x, k))} {YES} {Q(khs(AB, k))} {NO_PE} "
                f"{q(f'{x} là {pv}')} {YES} {Q(f'{AB} là {pv}')} {NO_PE}")
    add("5-507", cmp(KB, K5, PV5), cmp(RB, K5, PV5), cmp(ARB, K4, PV4))
    add("5-508",
        f"{Q(T2)} {YES} {Q(ab(ALL))} {NO_PE} {q(ab(ALL, True))} {YES} {S.hanci_neg(ab(ALL, True), T2)}",
        f"{Q(T2)} {YES} {Q(ab(ANA))} {NO_PE} {q(ab(ANA, True))} {YES} {S.hanci_neg(ab(ANA, True), T2)}",
        f"{Q(ab(NANA))} {YES} {Q(ab(ANA))} {NO_PE} {q(ab(ANA, True))} {YES} {Q(ab(NANA, True))} {NO_PE} "
        f"{q(f'đối với {NIRU}{PE} {ASAU}{PE} {ARUU}, {AB} tồn tại')} {NO_PE} {q(ab(ARUU, True))} {YES} "
        f"{S.hanci_neg(ab(ARUU, True), T2)}",
        f"{Q(ab(NARUU))} {YES} {Q(ab(ARUU))} {NO_PE} {q(ab(ARUU, True))} {YES} {Q(ab(NARUU, True))} {NO_PE}")
    add("5-509",
        f"Có phải không nên nói rằng {T2} không? {YES} {NANU(f'có {APN}')} {YES} Nếu có {APN}, thì {RE}"
        f"{S.var('Sī., Ka.', 'no ca vata re; (Syā.): no vata re')}, chắc chắn nên nói – “{T2}”.",
        f"{kv(f'có {APN}', T2)} {YES} {kv(f'có {UPN}', 'sự hiện hữu khi gần mạng chung tồn tại')} {NO_PE} "
        f"{kv(f'có {APN}', T2, True)} {YES} {kv(f'có {ASN}{PE} {SSN}', 'sự hiện hữu có sự thúc đẩy tồn tại')} "
        f"{NO_PE}",
        S.katha_end(KATHA[2]))

    # ---- (75) 3. Kāmaguṇakathā ----------------------------------------------------------------------------------
    kh(3, 3)
    add("5-510",
        f"{Q(T3)} {YES} {NANU(CH_TP)} {YES} {S.hanci_neg(CH_TP, T3)} {NANU(LIST9_TP)} {YES} {S.hanci_neg(PS_TP, T3)}",
        f"{Q(T3)} {YES} {Q(NOT_KD[0])} {NO_PE} {q(f'{PE} '.join(eyes(x) for x in ORG[1:]) + f' không phải là {KD}')} {NO_PE}",
        f"{Q(NOT_KD[5])} {YES} {S.NANU_VUTTAM}",
        *VERSE1,
        f"{S.ATTHEVA} {YES} {S.tena_hi_na(NOT_KD[5])}")
    add("5-511",
        f"{Q(T3)} {YES} {Q(isbh(KG))} {NO_PE} {q(kam(KG))} {NO_PE} {q(sat(KG))} {NO_PE} {q(born(KG))} {NO_PE} "
        f"{q(khs(KG))} {NO_PE} {q(f'{KG} là {PV5}')} {NO_PE} {q(bud(KG))} {NO_PE}",
        f"{Q(isbh(KD))} {YES} {Q(isbh(KG))} {NO_PE} {q(kam(KD))} {YES} {Q(kam(KG))} {NO_PE} {q(sat(KD))} {YES} "
        f"{Q(sat(KG))} {NO_PE}",
        f"{Q(born(KD))} {YES} {Q(born(KG))} {NO_PE} {q(khs(KD))} {YES} {Q(khs(KG))} {NO_PE} "
        f"{q(f'{KD} là {PV5}')} {YES} {Q(f'{KG} là {PV5}')} {NO_PE} {q(bud(KD))} {YES} {Q(bud(KG))} {NO_PE}")
    add("5-512",
        f"{S.na_vattabbam(T3)} {YES} {S.NANU_VUTTAM} {FIVE_FULL}. {S.ATTHEVA} {YES} {S.tena_hi(T3)}",
        S.katha_end(KATHA[3]))

    # ---- (76) 4. Kāmakathā --------------------------------------------------------------------------------------
    kh(4, 4)
    add("5-513",
        f"{Q(T4)} {YES} {NANU(CH_TP)} {YES} {S.hanci_neg(CH_TP, T4)} {NANU(LIST9_TP)} {YES} {S.hanci_neg(PS_TP, T4)}")
    add("5-514",
        f"{S.na_vattabbam(T4)} {YES} {S.NANU_VUTTAM} {FIVE_SHORT}”. {S.ATTHEVA} {YES} {S.tena_hi(T4)}",
        f"{Q(T4)} {YES} {S.NANU_VUTTAM} {FIVE_SHORT}. Tuy nhiên, này các tỳ-khưu, những thứ này không phải là "
        f"các dục lạc; trong Giới Luật của bậc thánh, chúng được gọi là các loại dục lạc” –",
        *VERSE2,
        f"{S.ATTHEVA} {YES} {S.tena_hi_na(T4)}",
        S.katha_end(KATHA[4]))

    # ---- (77) 5. Rūpadhātukathā ---------------------------------------------------------------------------------
    def dh_block(thesis, x, k, pv, dh):
        l1 = (f"{Q(thesis)} {YES} {Q(isbh(x))} {NO_PE} {q(kam(x))} {NO_PE} {q(sat(x))} {NO_PE} {q(born(x))} "
              f"{NO_PE} {q(khs(x, k))} {NO_PE} {q(f'{x} là {pv}')} {NO_PE}")
        l2 = (f"{Q(f'{dh} là {BH_PE}')} {YES} {Q(f'{x} là {BH_PE}')} {NO_PE} {q(kam(dh))} {YES} {Q(kam(x))} "
              f"{NO_PE} {q(sat(dh))} {YES} {Q(sat(x))} {NO_PE}")
        l3 = (f"{Q(born(dh))} {YES} {Q(born(x))} {NO_PE} {q(khs(dh, k))} {YES} {Q(khs(x, k))} {NO_PE} "
              f"{q(f'{dh} là {pv}')} {YES} {Q(f'{x} là {pv}')} {NO_PE}")
        return l1, l2, l3

    kh(5, 5)
    add("5-515", *dh_block(T5, RUPA, K5, PV5, RDH))
    add("5-516",
        f"{Q(f'{T5}, trong {KD} có {RUPA}')} {YES} {Q(SAVA2)} {NO_PE} {q(SAVA2)} {YES} "
        f"{Q(f'{SAM} hai sự hiện hữu – {KB} và {RB}')} {NO}",
        S.katha_end(KATHA[5]))

    # ---- (78) 6. Arūpadhātukathā --------------------------------------------------------------------------------
    kh(6, 6)
    add("5-517", *dh_block(T6, VED, K4, PV4, ARDH))
    add("5-518",
        f"{Q(f'{T6}, trong {KD} có {K4}')} {YES} {Q(SAVA2A)} {NO_PE} {q(SAVA2A)} {YES} "
        f"{Q(f'{SAM} hai sự hiện hữu – {KB} và {ARB}')} {NO_PE}",
        f"{Q(f'{T5}, {T6}, trong {KD} có {K5}')} {YES} {Q(SAVA3)} {NO_PE} {q(SAVA3)} {YES} "
        f"{Q(f'{SAM} ba sự hiện hữu – {KB}, {RB} và {ARB}')} {NO_PE}",
        S.katha_end(KATHA[6]))

    # ---- (79) 7. Rūpadhātuyāāyatanakathā ------------------------------------------------------------------------
    kh(7, 7)
    add("5-519",
        f"{Q(T7)} {YES} {Q(at('ghānāyatana'))} {YES} {Q(at('gandhāyatana'))} {NO_PE} {q(at('jivhāyatana'))} "
        f"{YES} {Q(at('rasāyatana'))} {NO_PE} {q(at('kāyāyatana'))} {YES} {Q(at('phoṭṭhabbāyatana'))} {NO_PE}",
        f"{Q(at('gandhāyatana', True))} {YES} {Q(at('ghānāyatana', True))} {NO_PE} "
        f"{q(at('rasāyatana', True))} {YES} {Q(at('jivhāyatana', True))} {NO_PE} "
        f"{q(at('phoṭṭhabbāyatana', True))} {YES} {Q(at('kāyāyatana', True))} {NO_PE}")

    def two(a, b):
        return f"{a}{PE} {b}"

    add("5-520",
        f"{Q(pr(E))} {YES} {Q(pr(NO_))} {NO_PE} {q(pr(E))} {YES} {Q(two(pr(TO), pr(BO)))} {NO_PE} "
        f"{q(two(pr(SO_), pr(MA)))} {YES} {Q(pr(NO_))} {NO_PE} {q(pr(MA))} {YES} {Q(two(pr(TO), pr(BO)))} {NO_PE}",
        f"{Q(pr(NO_, 1))} {YES} {Q(pr(E, 1))} {NO_PE} {q(pr(NO_, 1))} {YES} {Q(two(pr(SO_, 1), pr(MA, 1)))} "
        f"{NO_PE} {q(two(pr(TO, 1), pr(BO, 1)))} {YES} {Q(pr(E, 1))} {NO_PE} {q(pr(BO, 1))} {YES} "
        f"{Q(two(pr(SO_, 1), pr(MA, 1)))} {NO_PE}")
    add("5-521",
        f"{Q(use(E))} {YES} {Q(use(NO_))} {NO_PE} {q(use(E))} {YES} {Q(two(use(TO), use(BO)))} {NO_PE}",
        f"{Q(two(pr(SO_), use(MA)))} {YES} {Q(use(NO_))} {NO_PE} {q(use(MA))} {YES} {Q(two(pr(TO), use(BO)))} "
        f"{NO_PE}",
        f"{Q(use(NO_, 1))} {YES} {Q(use(E, 1))} {NO_PE} {q(use(NO_, 1))} {YES} {Q(two(pr(SO_), use(MA, 1)))} "
        f"{NO_PE}",
        f"{Q(two(pr(TO), use(BO, 1)))} {YES} {Q(two(pr(SO_), use(MA, 1)))} {NO_PE}")
    add("5-522",
        f"{Q(use(NO_))} {YES} {Q(f'ở đó có {GANDHA10}')} {NO_PE}",
        f"{Q(use(TO))} {YES} {Q(f'ở đó có {RASA16}')} {NO_PE}",
        f"{Q(use(BO))} {YES} {Q(f'ở đó có {TOUCH8}')} {NO_PE}")
    add("5-523",
        f"{S.na_vattabbam(T7Q)} {YES} {NANU(f'ở đó có {NIM}')} {YES} {S.hanci(f'ở đó có {NIM}', T7Q)}",
        S.katha_end(KATHA[7]))

    # ---- (80) 8. Arūpe rūpakathā --------------------------------------------------------------------------------
    kh(8, 8)
    AB_PE = f"sự hiện hữu ở {ARDH}{PE} sự có được sự tồn tại cá nhân ở {ARDH}"
    add("5-524",
        f"{Q(T8)} {YES} {Q(f'đó là {six(RDH)}')} {NO_PE} {nanu_l(f'đó là {six(ARDH)}')} {YES} "
        f"{S.hanci_neg(f'đó là {AB_PE}', T8)}",
        f"{Q(T8)} {YES} {Q(f'đó là {PV5}, {GATI6}')} {NO_PE} {nanu_l(f'đó là {PV4}{PE} sự có được sự tồn tại cá nhân')} "
        f"{YES} {S.hanci_neg(f'đó là {V4_PE}', T8)}")
    add("5-525",
        f"{Q(so_ca(RIN, six(RDH)))} {YES} {Q(so_ca(T8, six_pe(RDH)))} {NO_PE} {q(so_ca(RIN, V5_PE))} {YES} "
        f"{Q(so_ca(T8, V5_PE))} {NO_PE} {Q(so_ca(T8, six(ARDH)))} {YES} {Q(so_ca(RIN_V, six_pe(ARDH)))} {NO_PE} "
        f"{q(so_ca(T8, V4_PE))} {YES} {Q(so_ca(RIN_V, V4_PE))} {NO_PE}")
    add("5-526",
        f"{Q(T8)} {YES} {NANU(NIS + CIT3)} {YES} {S.hanci_neg(NIS + CIT3, T8)}",
        f"{Q(f'{NIS}, {T8}')} {YES} {Q(NEKK)} {NO_PE}",
        S.katha_end(KATHA[8]))

    # ---- (81) 9. Rūpaṃ kammantikathā ----------------------------------------------------------------------------
    kh(9, 9)

    def first(kk, c, adj, full, sep):   # thesis; sārammaṇaṃ …? nanu anārammaṇaṃ …? hañci anārammaṇaṃ …
        t = X(kr(kk, c), [], adj, True)
        return (f"{Q(t)} {YES} {Q(f'{obj()}, {has(full)}')} {NO_PE} {nanu_l(f'{obj(True)}, {has(full, True)}')} "
                f"{YES} {S.hanci_neg(f'{obj(True)}, {has(full and sep == ';', True)}', t, sep)}")

    def obj2(kk, c, adj):
        return f"{Q(ph(c, adj))} {YES} {Q(kro(kk, c, adj))} {NO_PE} {q(lst(c, adj))} {YES} {Q(kro(kk, c, adj))} {NO_PE}"

    def obj3(kk, c, adj):
        return (f"{Q(kro(kk, c, adj, True))} {YES} {Q(ph(c, adj, True))} {NO_PE} {q(kro(kk, c, adj, True))} {YES} "
                f"{Q(lst(c, adj, True))} {NO_PE}")

    def yk(kk, c, adj, tail=""):
        return f"{Q(X(kr(kk, c), [], adj, True))} {YES} {Q(yam_kinci(c, adj))} {NO_PE}{tail}"

    def lineA(kk, c, adj, mods, imp=False):
        t = X(kr(kk, c), mods, adj, True)
        return (f"{Q(t)} {YES} {Q(X(f'lĩnh vực hình sắc do {c} sinh ra', mods, adj))} {NO_PE} {q(t)} {YES} "
                f"{Q(X(rlist(c, imp), mods, adj))} {NO_PE}")

    def lineB(kk, c, mods, imp=False, mods2=None):
        m2 = mods if mods2 is None else mods2
        t = X(kr(kk, c), m2, ABY, True)
        return (f"{Q(X(f'lĩnh vực hình sắc do {c} sinh ra', mods, ABY))} {YES} {Q(t)} {NO_PE} "
                f"{q(X(rlist(c, imp), m2, ABY))} {YES} {Q(t)} {NO_PE}")

    add("5-527", first(KK, CT, "thiện", True, ","), obj2(KK, CT, "thiện"), obj3(KK, CT, "thiện"))
    add("5-528", yk(KK, CT, "thiện"), lineA(KK, CT, "thiện", []), lineB(KK, CT, []))
    add("5-529", lineA(KK, CT, "thiện", [ANR]), lineB(KK, CT, [ANR]))
    add("5-530", lineA(KK, CT, "thiện", [PVP]), lineB(KK, CT, [PVP]))
    add("5-531", lineA(KK, CT, "thiện", [ANR, PVP]), lineB(KK, CT, [ANR, PVP]))
    add("5-532", first(VK, CT, "thiện", False, ";"), obj2(VK, CT, "thiện"), obj3(VK, CT, "thiện"),
        yk(VK, CT, "thiện", f" như đối với {KK}, cũng vậy đối với {VK}."))
    add("5-533", first(KK, ACT, "bất thiện", True, ";"), obj2(KK, ACT, "bất thiện"), obj3(KK, ACT, "bất thiện"),
        yk(KK, ACT, "bất thiện"))
    add("5-534", first(VK, ACT, "bất thiện", False, ";"), obj2(VK, ACT, "bất thiện"), obj3(VK, ACT, "bất thiện"),
        yk(VK, ACT, "bất thiện"))
    add("5-535", lineA(VK, ACT, "bất thiện", [], True), lineB(VK, ACT, [], True))
    add("5-536", lineA(VK, ACT, "bất thiện", [ANR], True), lineB(VK, ACT, [ANR], True))
    add("5-537", lineA(VK, ACT, "bất thiện", [PVP], True), lineB(VK, ACT, [PVP], True, [ANR, PVP]),
        lineA(VK, ACT, "bất thiện", [ANR, PVP], True), lineB(VK, ACT, [ANR, PVP], True))
    l177 = []
    for k, (a, v) in enumerate(VIN5):
        l177.append(f"{Q(KR2) if k == 0 else q(KR2)} {YES} {Q(f'{a} là vật chất, {v} là vật chất')} {NO_PE}")
    add("5-538",
        f"{S.na_vattabbam(RK)} {YES} {NANU(KV2)} {YES} {S.hanci(KV2, RK)}",
        f"{Q(RK)} {YES} {Q(f'lĩnh vực mắt vừa là thiện vừa là bất thiện')} {NO_PE} {q(RK)} {YES} "
        f"{Q(f'{LIST13} vừa là thiện vừa là bất thiện')} {NO_PE}",
        f"{Q(KR2)} {YES} {Q(f'ý là vật chất, {MK} là vật chất')} {NO_PE} "
        f"{q(f'ý là phi vật chất, {MK} là phi vật chất')} {YES} {Q(f'thân là phi vật chất, {KK} là phi vật chất')} "
        f"{NO_PE}",
        " ".join(l177))
    add("5-539",
        *[f"{Q(T9)} {YES} {S.NANU_VUTTAM} {s} {S.ATTHEVA} {YES} {S.tena_hi_na(T9)}"
          for s in (SUT1, SUT2, SUT3, SUT4)],
        S.katha_end(KATHA[9]))

    # ---- (82) 10. Jīvitindriyakathā -----------------------------------------------------------------------------
    kh(10, 10)
    add("5-540",
        f"{Q(T10)} {YES} {Q(f'{RD} không có {RL}')} {NO_PE} {q(f'{RD} có {RL}')} {YES} "
        f"{S.hanci_neg(f'{RD} có {RL}', T10)}",
        f"{Q(f'{AD} có {RL}, {AJ} tồn tại')} {YES} {Q(f'{RD} có {RL}, {RJ} tồn tại')} {NO_PE} "
        f"{q(f'{RD} có {RL}, {RJ} không tồn tại')} {YES} {Q(f'{AD} có {RL}, {AJ} không tồn tại')} {NO_PE}",
        f"{Q(f'{AA} là {AJ}')} {YES} {Q(f'{RA} là {RJ}')} {NO_PE} {q(call_n(RA, RJ))} {YES} "
        f"{Q(call_n(AA, AJ))} {NO_PE}")
    add("5-541",
        f"{Q(f'{RA} là {AJ}')} {YES} {Q(f'{AA} là {RJ}')} {NO_PE}",
        f"{Q(call_n(AA, RJ))} {YES} {Q(call_n(RA, AJ))} {NO_PE}",
        f"{Q(f'{BA} là {AJ}')} {YES} {Q(f'{BA} là {RJ}')} {NO_PE}",
        f"{Q(call_n(BA, RJ))} {YES} {Q(call_n(BA, AJ))} {NO_PE} {q(T10)} {YES} {Q(jv(NSA, True))} {NO_PE}")
    add("5-542",
        f"{Q(jv(NSA))} {YES} {S.hanci_neg(jv(NSA), T10)}",
        f"{Q(jv(NSA))} {YES} {KHA} {Q(f'{NSA} có khối tạo tác')} {NO_PE}",
        f"{Q(f'{NSA} có khối tạo tác')} {YES} {Q(f'{NSA} có {KH3}')} {NO_PE}",
        f"{Q(f'{NSA} có {KH3}')} {YES} {Q(f'đó không phải là {NSA}')} {NO_PE}")
    add("5-543",
        f"{Q(T10)} {YES} {Q(jv(ASA, True))} {NO_PE}",
        f"{Q(jv(ASA))} {YES} {S.hanci_neg(jv(ASA), T10)} {Q(jv(ASA))} {YES} {KHA} {Q(f'{ASA} có khối tạo tác')} "
        f"{NO_PE}",
        f"{Q(f'{ASA} có khối tạo tác')} {YES} {Q(f'{ASA} có {KH3}')} {NO_PE}",
        f"{Q(f'{ASA} có {KH3}')} {YES} {Q(f'đó là {PV5}')} {NO_PE}")
    add("5-544",
        f"{Q(br('năng lực sống', 'một phần'))} {YES} {Q(br('sự tiếp xúc', 'một phần'))} {NO_PE}",
        f"{Q(br('sự tiếp xúc', 'không còn sót lại'))} {YES} {Q(br('năng lực sống', 'không còn sót lại'))} {NO_PE}")
    add("5-545",
        f"{Q('có hai năng lực sống')} {YES} {Q('người ta sống bằng hai sự sống, qua đời bằng hai sự chết')} "
        f"Đúng vậy{S.var('Syā., Kaṃ., Pī.', 'na hevaṃ vattabbe')}.",
        S.katha_end(KATHA[10]))

    # ---- (83) 11. Kammahetukathā --------------------------------------------------------------------------------
    kh(11, 11)
    CHAIN = f"{PE} ".join(f"do {k} làm nguyên nhân" for k in KM[1:])
    add("5-546",
        f"{Q(fall(AR, ARH))} {YES} {Q(fall(SO, FRSO))} {NO_PE} {q(fall(AR, ARH))} {YES} "
        f"{Q(f'{KH}, {SA}{PE} {AN} sa sút khỏi {FRAN}')} {NO_PE}",
        f"{Q(fall(SO, FRSO, True))} {YES} {Q(fall(AR, ARH, True))} {NO_PE} "
        f"{q(f'{KH}, {SA}{PE} {AN} không sa sút khỏi {FRAN}')} {YES} {Q(fall(AR, ARH, True))} {NO_PE}",
        f"{Q(fall(AR, ARH))} {YES} {Q(f'do {KM[0]} làm nguyên nhân')} {NO_PE} {q(CHAIN)} {NO_PE}",
        f"Do nghiệp nào làm nguyên nhân? Này, vì người ấy {ABB}. "
        f"{Q(f'do nghiệp {ABB} làm nguyên nhân, {AR} sa sút khỏi {ARH}')} {YES} "
        f"{Q(f'bất cứ ai {ABB}, tất cả những người ấy đều tự mình chứng nghiệm {ARH}')} {NO_PE}",
        S.katha_end(KATHA[11]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-16"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
