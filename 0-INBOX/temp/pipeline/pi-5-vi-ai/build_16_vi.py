# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 16: 16-atthamavaggo.md (Aṭṭhamavaggo, ^5-16-0 … ^5-546),
the eleven kathā (73)-(83) of the eighth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished
chapter builders build_2_vi / build_3_vi / build_9_vi / build_10_vi / build_14_vi (read-only, importing writes
nothing) for the persons and fruits, the Buddhas list, the vagga close, the sense triples, the crimes and the
bhavo gati … attabhāvapaṭilābho list, so every repeat is byte-identical with those chapters. Every string claimed
from the pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is
asserted to occur in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign
letters) are run against the Pāli. Every Pāli sentence keeps its own sentence.

run:  python -I -B -X utf8 build_16_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (persons, fruits, parihāyati, the kilesa words)
import build_3_vi as C3      # noqa: E402  (sammāsambuddhā / paccekasambuddhā / sāvakayugaṃ uppajjanti)
import build_9_vi as C9      # noqa: E402  (vagga close: Tassuddānaṃ –)
import build_10_vi as C10    # noqa: E402  (sense triples, crimes, killers)
import build_14_vi as C14    # noqa: E402  (bhavo gati … attabhāvapaṭilābho, -ūpaga, jāyanti …, catuvokāra)

NAME = "16-atthamavaggo.md"
Q, q, NANU, AM, cap = B.Q, B.q, B.NANU, B.AMANTA, B.cap
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA = B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA
NANU_VUTTAM, ATTHEVA = B.NANU_VUTTAM, B.ATTHEVA
TENA_VATA, NO_CA_VATA = B.TENA_VATA, B.NO_CA_VATA
VAR, SPELL = B.VAR, B.SPELL
VAGGA8 = B.VAGGA[8]                                       # Aṭṭhamavaggo = «Chương thứ tám» (terms file)
K, E = B.KATHA.format, B.KATHA_END.format


def nanu(x):
    """…pe… nanu Xti? (lowercase after …pe…)"""
    return f"chẳng phải {x} sao?"


def Qc(parts, first=True):
    """A…pe… B…pe… Cti? (one question over a …pe… chain)"""
    return ("Có phải " if first else "có phải ") + "… ".join(parts) + " không?"


def katva(x, y, first=True):
    """Xti katvā Yti? (ch11 «Có phải vì cho rằng X, Y không?»)"""
    return f"{'Có' if first else 'có'} phải vì cho rằng {x}, {y} không?"


# ================================================================ shared lists (ch14 wording)
BHAVA7 = C14.BHAVA7     # là sự hiện hữu, cõi tái sinh, nơi cư trú của chúng sinh, vòng luân hồi, cách sinh, chỗ trú
#                         của thức, sự có được sự tồn tại cá nhân  (bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti
#                         attabhāvapaṭilābho)
B7 = BHAVA7[3:].split(", ")
assert BHAVA7.startswith("là ") and len(B7) == 7
BHAVA7_PE = f"là {B7[0]}, {B7[1]}… {B7[-1]}"               # bhavo gati…pe… attabhāvapaṭilābho
S6W = [B7[0], B7[1], B7[2], B7[3], B7[4], B7[6]]          # bhavo gati sattāvāso saṃsāro yoni attabhāvapaṭilābho
UPAGA, LIFE5, FOURK, CATU = C14.UPAGA, C14.LIFE5, C14.FOURK, C14.CATU
FIVEK = f"có {B.RUPA}, {B.VEDANA}, {B.SANNA}, {B.SANKHARA}, {B.VINNANA}"   # atthi rūpaṃ vedanā saññā saṅkhārā viññāṇaṃ
PANCA_N, CATU_N = "sự hiện hữu gồm năm khối", "sự hiện hữu gồm bốn khối"   # pañca- / catuvokārabhavo (pi-2)
PANCA = f"là {PANCA_N}"
assert CATU == f"là {CATU_N}"


def kamma_up(x):
    return f"có nghiệp {UPAGA} {x}"                       # atthi X-ūpagaṃ kammaṃ


def satta_up(x):
    return f"có chúng sinh {UPAGA} {x}"                   # atthi X-ūpagā sattā


def life_in(x):
    return f"trong {x}, {LIFE5}"                          # X-e sattā jāyanti jīyanti mīyanti cavanti upapajjanti


def k5_in(x):
    return f"trong {x} {FIVEK}"                           # X-e atthi rūpaṃ vedanā saññā saṅkhārā viññāṇaṃ


def k4_in(x):
    return f"trong {x} {FOURK}"                           # X-e atthi vedanā saññā saṅkhārā viññāṇaṃ


def bare7(head, pe=False, two=False):
    """<head>bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho (…pe… forms)"""
    if not pe:
        return "là " + ", ".join([head] + B7[1:])
    if two:
        return f"là {head}, {B7[1]}… {B7[-1]}"
    return f"là {head}… {B7[-1]}"


def six(x):
    """X-bhavo X-gati X-sattāvāso X-saṃsāro X-yoni X-attabhāvapaṭilābho (ch11 pattern, ch14 words)"""
    return ", ".join(f"{w} {x}" for w in S6W)


def six_pe(x, two=False):
    if two:
        return f"{S6W[0]} {x}, {S6W[1]} {x}… {S6W[5]} {x}"
    return f"{S6W[0]} {x}… {S6W[5]} {x}"


# ================================================================ (73) Chagati
KX1 = "sáu cõi tái sinh"                                  # Chagatikathā (terms file)
T1 = f"có {KX1}"                                          # cha gatiyo (bare thesis «có», ch10)
G5 = "địa ngục, cõi súc sinh, cõi ngạ quỷ, loài người, chư thiên"
# nirayo, tiracchānayoni, pettivisayo, manussā, devā (pi-2 ^2-811 địa ngục / cõi súc sinh / cõi ngạ quỷ; devā pi-2)
V5 = f"Đức Thế Tôn đã nói rằng có năm cõi tái sinh – {G5}"   # pañca gatiyo vuttā bhagavatā – … (ch10 frame)
PETA, DEVA = "các ngạ quỷ", "chư thiên"


def same(x):
    """X-ānaṃ samānavaṇṇā samānabhogā samānāhārā samānāyukā X-ehi saha āvāhavivāhaṃ gacchanti"""
    return f"có cùng dung sắc, cùng sự hưởng thụ, cùng thức ăn, cùng tuổi thọ với {x}, cưới gả với {x}"


KKC = "các a-tu-la Ka-la-kan-chi-ka"                       # kālakañcikā (a)surā
KKC_V = f"{KKC} [{SPELL} (Sī., Syā., Kaṃ.): kālakañjikā; (Pī.): kāḷakañjakā]"
VP = "hội chúng của Vê-pa-chít-ti"                        # vepacittiparisā
PUBBADEVA = f"{VP} là chư thiên trước kia"                 # vepacittiparisā pubbadevā
ASK = "có nhóm a-tu-la"                                   # atthi asurakāyo (kāya «nhóm», ch10 mārakāyikā)

# ================================================================ (74) Antarābhava
AB = "sự hiện hữu trong khoảng giữa"                      # antarābhava (pi-4 antarāparinibbāyī «trong khoảng giữa»)
KX2 = AB
T2 = f"có {AB}"
KB, RB, ARB = "sự hiện hữu ở cõi dục lạc", "sự hiện hữu ở cõi hình sắc", "sự hiện hữu ở cõi không hình sắc"  # pi-2


def betw(a, b, neg=False):
    """A-assa ca B-assa ca antare (n)atthi antarābhavo"""
    return f"giữa {a} và {b} {'không có' if neg else 'có'} {AB}"


FIFTH = f"đó là {B7[4]} thứ năm, đó là {B7[1]} thứ sáu, đó là {B7[5]} thứ tám, đó là {B7[2]} thứ mười"
# pañcamī sā yoni, chaṭṭhamī sā gati, aṭṭhamī sā viññāṇaṭṭhiti, dasamo so sattāvāso
SB_ALL, SB_NONE = f"tất cả chúng sinh đều có {AB}", f"tất cả chúng sinh đều không có {AB}"
AP = "người tạo nghiệp có quả không gián đoạn"             # ānantariyo puggalo (pi-1 ānantarika «có quả không gián đoạn»)
NAP = "người không tạo nghiệp có quả không gián đoạn"      # na ānantariyo puggalo
NIR_UP = f"người {UPAGA} địa ngục"                        # nirayūpago puggalo
ASN_UP = f"người {UPAGA} cõi chúng sinh Vô Tưởng"          # asaññasattūpago (asaññasattā ch11)
ARU_UP = f"người {UPAGA} cõi không hình sắc"               # arūpūpago
NARU_UP = f"người không {UPAGA} cõi không hình sắc"        # na arūpūpago


def has(who):
    return f"{who} có {AB}"


def hasnt(who):
    return f"{who} không có {AB}"


PARI_A = "người nhập Niết-bàn trọn vẹn trong khoảng giữa"   # antarāparinibbāyī (pi-4)
PARI_U = "người nhập Niết-bàn trọn vẹn khi gần mạng chung"  # upahaccaparinibbāyī (pi-4)
PARI_AS = "người nhập Niết-bàn trọn vẹn không có sự thúc đẩy"   # asaṅkhāraparinibbāyī (pi-4)
PARI_S = "người nhập Niết-bàn trọn vẹn có sự thúc đẩy"     # sasaṅkhāraparinibbāyī (pi-4)
UB = "sự hiện hữu khi gần mạng chung"                     # upahaccabhavo
SSB_ = "sự hiện hữu có sự thúc đẩy"                       # sasaṅkhārabhavo
TENA_VATA_V = TENA_VATA.replace("thì này bạn,", f"thì này bạn [{VAR} (Sī., Ka.): no ca vata re; (Syā.): no vata re],", 1)

# ================================================================ (75) Kāmaguṇa / (76) Kāma
KG = "các loại dục lạc"                                   # kāmaguṇā (ch10 «năm loại dục lạc»)
KD = "cõi dục lạc"                                        # kāmadhātu (pi-1, pi-2)
KX3 = KG
T3 = f"chỉ năm loại dục lạc là {KD}"                      # pañceva kāmaguṇā kāmadhātu
KX4 = "các dục lạc"                                       # Kāmakathā (kāmā «các dục lạc» pi-2)
T4 = f"chỉ năm lĩnh vực nhận biết là {KX4}"                # pañcevāyatanā kāmā
TP = "liên quan đến chúng"                                # tappaṭisaññutto / tappaṭisaṃyutto (paṭisaṃyutta pi-2)
CH, RA, CR, SKP, SR = "ý muốn", "sự tham đắm", "sự tham đắm do ý muốn", "tư duy", "sự tham đắm do tư duy"   # (pi-2)
PI, SOM, PS = "sự hân hoan", "niềm vui", "sự hân hoan và niềm vui"   # pīti / somanassaṃ / pītisomanassaṃ (pi-1)
RLIST = ", ".join(f"{x} {TP}" for x in (RA, CH, CR, SKP, RA, SR, PI, SOM, PS))   # as the Pāli order


def five_tp(th):
    """^5-510 l.1 / ^5-513: Nanu atthi tappaṭisaññutto chando … pītisomanassanti?"""
    return (f"{Q(th)} {AM} {NANU(f'có {CH} {TP}')} {AM} Nếu có {CH} {TP}, {NO_CA_VATA} “{th}”. "
            f"{NANU(f'có {RLIST}')} {AM} Nếu có {PS} {TP}, {NO_CA_VATA} “{th}”.")


MAN = "của loài người"                                    # manussānaṃ


def nk(o):
    return f"{o} {MAN} không phải là {KD}"                # manussānaṃ X na kāmadhātu


def appear(x):
    """X-e sammāsambuddhā uppajjanti, paccekasambuddhā uppajjanti, sāvakayugaṃ uppajjati (ch3)"""
    return f"trong {x}, {C3.SSB} {C3.APPEAR}, {C3.PCB} {C3.APPEAR}, {C3.SVY} {C3.APPEAR}"


KG_HEAD = "“Này các tỳ-khưu, có năm loại dục lạc này! Năm loại nào? Các hình sắc được nhận biết bằng mắt"
KG_Q = "đáng mong muốn, đáng yêu thích, vừa ý, có vẻ đáng yêu, gắn liền với dục lạc, hấp dẫn"
KG_MID = ("; các âm thanh được nhận biết bằng tai… các mùi được nhận biết bằng mũi… các vị được nhận biết bằng "
          "lưỡi… ")
KG_TOUCH = f"các vật xúc chạm được nhận biết bằng thân, {KG_Q}"
KG_END = "này các tỳ-khưu, đây là năm loại dục lạc"
SUT_FULL = f"{KG_HEAD}, {KG_Q}{KG_MID}{KG_TOUCH} – {KG_END}”"   # ^5-512 (ch10 ^5-302 wording; dash as the Pāli)
SUT_ABBR = f"{KG_HEAD}… {KG_TOUCH} – {KG_END}"                  # ^5-514 (cakkhuviññeyyā rūpā…pe… kāyaviññeyyā …)
CITE_AN663 = "Tăng Chi Bộ Kinh 6.63, trong Kinh Thấu Triệt"     # a. ni. 6.63 nibbedhikasutte

# ================================================================ (77) Rūpadhātu / (78) Arūpadhātu
RU, VE = B.RUPA, B.VEDANA                                 # rūpaṃ «vật chất», vedanā «cảm giác»
RD_, ARD_ = "các hiện tượng thuộc vật chất", "các hiện tượng phi vật chất"   # rūpino / arūpino dhammā (pi-1)
RDH, ARDH = "cõi hình sắc", "cõi không hình sắc"           # rūpadhātu / arūpadhātu (pi-1, pi-2)
KX5, KX6 = RDH, ARDH
T5, T6 = f"{RD_} là {RDH}", f"{ARD_} là {ARDH}"
KDY = f"trong {KD}"                                       # kāmadhātuyā (pi-2 «trong cõi dục lạc»)


def sava(*xs):
    """Sāva kāmadhātu, sā rūpadhātu(, sā arūpadhātu) (ch12 «chính X ấy, người ấy là Y»)"""
    return f"chính {KD} ấy, " + ", ".join(f"cõi ấy là {x}" for x in xs)


SAM2 = f"người được trang bị {KB} thì được trang bị hai sự hiện hữu – {KB} và {RB}"
SAM2A = f"người được trang bị {KB} thì được trang bị hai sự hiện hữu – {KB} và {ARB}"
SAM3 = f"người được trang bị {KB} thì được trang bị ba sự hiện hữu – {KB}, {RB} và {ARB}"
# kāmabhavena samannāgato puggalo dvīhi / tīhi bhavehi samannāgato hoti – … (samannāgata «được trang bị» ch12)

# ================================================================ (79) Rūpadhātuyā āyatana
AT = "các lĩnh vực nhận biết"
KX7 = f"{AT} trong {RDH}"                                 # Rūpadhātuyāāyatanakathā / Rūpadhātuyā āyatanakathā
T7 = f"trong {RDH} có sự tồn tại cá nhân gồm sáu lĩnh vực nhận biết"   # atthi saḷāyataniko attabhāvo rūpadhātuyā
T7Q = f"sự tồn tại cá nhân gồm sáu lĩnh vực nhận biết trong {RDH}"     # saḷāyataniko attabhāvo rūpadhātuyā (no atthi)
EYE, EAR, NOSE, TONG, BODY, FORM, SOUND, SMELL, TASTE, TOUCH, MIND, MOBJ = B.AYATANA
AYP = {0: (EYE, FORM), 1: (EAR, SOUND), 2: (NOSE, SMELL), 3: (TONG, TASTE), 4: (BODY, TOUCH), 5: (MIND, MOBJ)}
SENSES = C10.SENSES                                       # (mắt, thấy, hình sắc) … (ý, nhận biết, đối tượng của ý)


def there(x):
    return f"ở đó có {x}"                                 # atthi tattha X (ch11)


def nthere(x):
    return f"ở đó không có {x}"


def pair(o, x):
    return f"ở đó có {o}, có {x}"                         # atthi tattha X, atthi Y


def npair(o, x):
    return f"ở đó có {o}, không có {x}"                   # atthi tattha X, natthi Y


def pr(i):
    return pair(*AYP[i])


def full(i, neg=False):
    """atthi tattha X atthi Y, (na ca) tena X-ena taṃ Y-aṃ V-ti (ch13 «dùng X ấy mà V Y ấy»)"""
    o, v, x = SENSES[i]
    return f"{pr(i)}, {'nhưng không ' if neg else ''}dùng {o} ấy mà {v} {x} ấy"


GANDHA = ("mùi rễ cây, mùi lõi cây, mùi vỏ cây, mùi lá, mùi hoa, mùi trái cây, mùi tanh, mùi ôi thiu, mùi thơm, "
          "mùi hôi")                                     # mūlagandho … duggandho (pi-1 ^1-624)
RASA = ("vị rễ cây, vị thân cây, vị vỏ cây, vị lá, vị hoa, vị trái cây, vị chua, vị ngọt, vị đắng, vị cay, vị mặn, "
        "vị kiềm, vị chua nhẹ, vị chát, vị ngon, vị không ngon")   # mūlaraso … asādu (pi-1 ^1-629; loṇiyaṃ khāriyaṃ)
PHOT = ("cái cứng, cái mềm, cái mịn, cái thô ráp, cái mà khi tiếp xúc thì dễ chịu, cái mà khi tiếp xúc thì khó chịu, "
        "cái nặng, cái nhẹ")                              # kakkhaḷaṃ … lahukaṃ (pi-1 ^1-647)
NIM = "dấu hiệu của mũi, dấu hiệu của lưỡi, dấu hiệu của thân"   # ghānanimittaṃ jivhānimittaṃ kāyanimittaṃ (nimitta sample)

# ================================================================ (80) Arūpe rūpa
KX8 = f"{RU} trong cõi không hình sắc"                    # Arūpe rūpakathā
T8 = f"có {RU} trong các cõi không hình sắc"              # atthi rūpaṃ arūpesu
OR, OAR = "ở cõi hình sắc", "ở cõi không hình sắc"        # rūpa- / arūpa- prefix (rūpabhavo = RB, pi-2)
assert six(OR).startswith(RB) and six(OAR).startswith(ARB)
RIR = f"có {RU} trong {RDH}"                              # atthi rūpaṃ rūpadhātuyā
SAB = f" [{VAR} (mọi bản): arūpadhātuyā]"                 # [arūpadhātuyā (sabbattha)]
ESC = f"lối thoát khỏi {RU} là cõi không hình sắc"        # rūpānaṃ nissaraṇaṃ arūpaṃ (nissaraṇa «lối thoát» pi-2)
CITE3 = "[Kinh Phật Thuyết Như Vậy 72; Tăng Chi Bộ Kinh 5.200; Trường Bộ Kinh 3.321]"
VESC = f"Đức Thế Tôn đã nói rằng {ESC} {CITE3}"
NEKKH = ("Đức Thế Tôn đã nói rằng lối thoát khỏi các dục lạc là sự từ bỏ, có các dục lạc trong sự từ bỏ, có các ô nhiễm "
         "trong những gì không phải là đối tượng của ô nhiễm, có những gì nằm trong các cõi tồn tại trong những gì "
         "không nằm trong các cõi tồn tại")
# kāmānaṃ nissaraṇaṃ nekkhammaṃ vuttaṃ bhagavatā, atthi nekkhammesu kāmā, atthi anāsavesu āsavā, atthi
# apariyāpannesu pariyāpannā (nekkhamma «sự từ bỏ» pi-2; anāsava ch12; apariyāpanna pi-1)

# ================================================================ (81) Rūpaṃ kammanti
TH, BT, KX = "thiện", "bất thiện", "không xác định về mặt đạo đức"
RK = f"{RU} là nghiệp"                                    # rūpaṃ kammaṃ
KX9 = f"việc cho rằng {RK}"                               # Rūpaṃ kammantikathā (ch14 «việc cho rằng …»)


def kk(c):
    return f"nghiệp bằng thân dưới dạng vật chất do tâm {c} sinh ra"   # X-ena cittena samuṭṭhitaṃ kāyakammaṃ rūpaṃ


def vk(c):
    return f"nghiệp bằng lời nói dưới dạng vật chất do tâm {c} sinh ra"   # … vacīkammaṃ rūpaṃ (pi-1 «do chúng sinh ra»)


def ph(c):
    return f"sự tiếp xúc do tâm {c} sinh ra"


def rf(c):
    return f"{FORM} do tâm {c} sinh ra"                    # X-ena cittena samuṭṭhitaṃ rūpāyatanaṃ


def rest(c, asu=False):
    """saddāyatanaṃ…pe… gandhāyatanaṃ… rasāyatanaṃ… phoṭṭhabbāyatanaṃ…pe… pathavīdhātu… … vāyodhātu (asuci …)"""
    s = (f"{SOUND} do tâm {c} sinh ra… {SMELL}… {TASTE}… {TOUCH}… "
         f"{C14.EARTH}… {C14.WATER}… {C14.FIRE}… {C14.WIND}")
    return s + (f", {ASU}" if asu else "")


ASU = "đồ bất tịnh, nước mắt, máu, mồ hôi"                # asuci assu lohitaṃ sedo (asuci ch10; pi-2 body list)
ATTS = "sự hướng đến, sự chú hướng, sự lưu ý, sự chú tâm, chủ ý, sự ước nguyện, sự mong cầu"
# āvaṭṭanā ābhogo samannāhāro manasikāro (pi-2 ^2-208) cetanā patthanā paṇidhi (paṇidhi ch11)
ATT_F, NATT_F = f"nó có {ATTS}", f"nó không có {ATTS}"
ATT_P, NATT_P = "nó có sự hướng đến… sự mong cầu", "nó không có sự hướng đến… sự mong cầu"
CS_K = f"cảm giác do tâm {TH} sinh ra… tri giác… chủ ý… niềm tin… tinh tấn… sự tỉnh thức… định tâm… trí tuệ"
# vedanā…pe… saññā… cetanā… saddhā… vīriyaṃ… sati… samādhi…pe… paññā (core terms)
CS_A = (f"cảm giác do tâm {BT} sinh ra… tri giác… chủ ý… "
        + "… ".join([C2.R, C2.D, C2.M, C2.MANA, C2.DI, C2.VI, C2.TH, C2.UD, C2.AH, C2.AO]))
# … rāgo… doso… moho… māno… diṭṭhi… vicikicchā… thinaṃ… uddhaccaṃ… ahirikaṃ…pe… anottappaṃ (ch2 words)


def pr_(e, an=False, pv=False):
    """(anārammaṇaṃ) (phassavippayuttaṃ) kusalaṃ / akusalaṃ / abyākataṃ"""
    parts = (["không có đối tượng"] if an else []) + (["không gắn liền với sự tiếp xúc"] if pv else [])
    return ", ".join(parts + [f"là {e}"])


def first_line(subj, e, q_full, n_full, h_full, sep):
    """X e-nti? Sārammaṇaṃ, atthi tassa …? nanu anārammaṇaṃ, natthi tassa …? Hañci anārammaṇaṃ … no ca vata re …"""
    return (f"{Q(f'{subj} là {e}')} {AM} {Q(f'có đối tượng, {ATT_F if q_full else ATT_P}')} {NHP} "
            f"{nanu(f'không có đối tượng, {NATT_F if n_full else NATT_P}')} {AM} "
            f"Nếu không có đối tượng, {NATT_F if h_full else NATT_P}{sep} {NO_CA_VATA} “{subj} là {e}”.")


def sar(s, e):
    return f"{s} là {e}, có đối tượng, {ATT_P}"


def anar(s, e):
    return f"{s} là {e}, không có đối tượng, {NATT_P}"


def second_line(subj, c, e, cs):
    """phasso … sārammaṇo …? Āmantā. X … sārammaṇaṃ …? … vedanā…pe… sārammaṇā …? Āmantā. X …?"""
    return (f"{Q(sar(ph(c), e))} {AM} {Q(sar(subj, e))} {NHP} {q(sar(cs, e))} {AM} {Q(sar(subj, e))} {NHP}")


def third_line(subj, c, e, cs):
    """X … anārammaṇaṃ …? Āmantā. phasso … anārammaṇo …? … X …? Āmantā. vedanā…pe… anārammaṇā …?"""
    return (f"{Q(anar(subj, e))} {AM} {Q(anar(ph(c), e))} {NHP} {q(anar(subj, e))} {AM} {Q(anar(cs, e))} {NHP}")


def all_line(subj, c, e):
    """X e-nti? Āmantā. Yaṃ kiñci c-ena cittena samuṭṭhitaṃ rūpaṃ sabbaṃ taṃ e-nti? (ch13 yaṃ kiñci …)"""
    return f"{Q(f'{subj} là {e}')} {AM} {Q(f'bất cứ vật chất nào do tâm {c} sinh ra, tất cả điều ấy đều là {e}')} {NHP}"


def el_line(subj, c, e, an=False, pv=False, asu=False):
    """X e? Āmantā. rūpāyatanaṃ e? … X e? Āmantā. saddāyatanaṃ…pe… vāyodhātu (asuci …) e?"""
    p = pr_(e, an, pv)
    return (f"{Q(f'{subj} {p}')} {AM} {Q(f'{rf(c)} {p}')} {NHP} {q(f'{subj} {p}')} {AM} "
            f"{Q(f'{rest(c, asu)} {p}')} {NHP}")


def ab_line(subj, c, an=False, pv=False, asu=False):
    """rūpāyatanaṃ abyākataṃ? Āmantā. X abyākataṃ? … saddāyatanaṃ…pe… abyākatā? Āmantā. X abyākataṃ?"""
    p = pr_(KX, an, pv)
    return (f"{Q(f'{rf(c)} {p}')} {AM} {Q(f'{subj} {p}')} {NHP} {q(f'{rest(c, asu)} {p}')} {AM} "
            f"{Q(f'{subj} {p}')} {NHP}")


TV = "vừa là thiện vừa là bất thiện"                      # kusalampi akusalampi
RKA = f"{RU} {TV}"
KVA = f"nghiệp bằng thân, nghiệp bằng lời nói {TV}"        # kāyakammaṃ vacīkammaṃ kusalampi akusalampi
REST11 = (f"{EAR}… {NOSE}… {TONG}… {BODY}… {FORM}… {SOUND}… {SMELL}… {TASTE}… {TOUCH}… {C14.EARTH}… "
          f"{C14.WATER}… {C14.FIRE}… {C14.WIND}, {ASU}")
VINN5 = [(EYE, "thức qua mắt"), (EAR, "thức qua tai"), (NOSE, "thức qua mũi"), (TONG, "thức qua lưỡi"),
         (BODY, "thức qua thân")]                         # cakkhuviññāṇa … kāyaviññāṇa (pi-2)
KR_ = "nếu thân là vật chất, thì nghiệp bằng thân là vật chất"   # kāyo rūpanti, kāyakammaṃ rūpanti (sample Xti, Yti?)
CETANA_S = ("“Này các tỳ-khưu, Ta nói chủ ý là nghiệp; sau khi có chủ ý, người ta làm nghiệp bằng thân, bằng lời "
            "nói, bằng ý”")
# cetanāhaṃ, bhikkhave, kammaṃ vadāmi; cetayitvā kammaṃ karoti kāyena vācāya manasā
HA = f"[{VAR} (Tương Ưng Bộ Kinh 2.25): hānanda]"         # [hānanda (saṃ. ni. 2.25)] (hi ānanda: particle)


def door(x):
    """X-e vā, ānanda, sati X-sañcetanāhetu uppajjati ajjhattaṃ sukhadukkhaṃ"""
    return (f"này A-nan {HA}, hoặc khi có {x}, do chủ ý bằng {x}, sự dễ chịu và sự khó chịu sinh khởi ở nơi bản "
            "thân")


SUT_DOOR = (f"“N{door('thân')[1:]}; {door('lời nói')}; {door('ý')}” "
            "[Tương Ưng Bộ Kinh 2.25; Tăng Chi Bộ Kinh 4.171]!")
UD_BAD, UD_GOOD = "đưa đến sự khó chịu, có quả trổ khó chịu", "đưa đến sự dễ chịu, có quả trổ dễ chịu"
# dukkhudrayaṃ dukkhavipākaṃ / sukhudrayaṃ sukhavipākaṃ (sample ^5-97 GOOD / BAD)


def sc(n, d, e, ud):
    """tividhā, bhikkhave, kāyasañcetanā akusalaṃ kāyakammaṃ dukkhudrayaṃ dukkhavipākaṃ"""
    return f"này các tỳ-khưu, chủ ý bằng {d} gồm {n} loại là nghiệp bằng {d} {e}, {ud}"


SUT_10 = ("“N" + "; ".join([sc("ba", "thân", BT, UD_BAD), sc("bốn", "lời nói", BT, UD_BAD), sc("ba", "ý", BT, UD_BAD),
                             sc("ba", "thân", TH, UD_GOOD), sc("bốn", "lời nói", TH, UD_GOOD),
                             sc("ba", "ý", TH, UD_GOOD)])[1:]
          + "” [Tăng Chi Bộ Kinh 10.217, nhưng hơi khác một chút]!")
ADS = "không khó chịu cũng không dễ chịu"                 # adukkhamasukha (pi-1)
PAT = "Ba-liên-phất"                                    # pāṭaliputta (ch13 Pāṭaliputta «Ba-liên-phất»)
SAM = "kẻ rồ dại Sa-mít-thi"                              # samiddhi moghapuriso


def vd(kind, felt):
    return (f"này hiền giả {PAT}, sau khi làm nghiệp có chủ ý bằng thân, bằng lời nói, bằng ý, đưa đến cảm giác "
            f"{kind}, người ấy cảm nhận {felt}")


SUT_SAM = (f"“Này A-nan, nếu {SAM} này, khi được du sĩ {PAT} [{VAR} (Trung Bộ Kinh 3.300): potaliputtassa] hỏi "
           f"như vậy, trả lời như thế này – ‘N{vd('dễ chịu', 'sự dễ chịu')[1:]}; {vd('khó chịu', 'sự khó chịu')}; "
           f"{vd(ADS, 'điều ' + ADS)}’, thì "
           f"khi trả lời như vậy, này A-nan, {SAM} sẽ trả lời một cách đúng đắn cho du sĩ {PAT}” "
           "[Trung Bộ Kinh 3.300]!")

# ================================================================ (82) Jīvitindriya
JI = B.INDRIYA[6]                                         # jīvitindriyaṃ = «năng lực sống» (pi-1)
KX10 = JI
RJ, AJ = f"{JI} thuộc vật chất", f"{JI} phi vật chất"      # rūpa- / arūpajīvitindriyaṃ
RD2, AD2 = "những hiện tượng thuộc vật chất", "những hiện tượng phi vật chất"   # rūpīnaṃ / arūpīnaṃ dhammānaṃ (pi-1)
BOTH = "những hiện tượng thuộc vật chất và phi vật chất"   # rūpīnañca arūpīnañca dhammānaṃ
LIFE7 = "tuổi thọ, sự tồn tại, sự tiếp diễn, sự kéo dài, sự vận động, sự tiến triển, sự gìn giữ"
# āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā (pi-1 ^1-634)
NRJ = f"không có {RJ}"


def life(d, neg=False):
    return f"{'không ' if neg else ''}có {LIFE7} của {d}"


def ayu(d):
    return f"tuổi thọ của {d}"


def nv(x, y):
    """X na vattabbaṃ – "Y"nti (ch13 «X không nên được gọi là – “Y”»)"""
    return f"{x} không nên được gọi là – “{y}”"


NIRS = "người đang nhập sự chấm dứt"                      # nirodhaṃ samāpanno (ch14)
ASS = "chúng sinh Vô Tưởng"                               # asaññasattā (ch11)
KH_PE = "khối cảm giác… khối tri giác… khối thức"         # vedanākkhandho…pe… saññākkhandho…pe… viññāṇakkhandho
WHICH = "Thuộc về khối nào? Thuộc về khối tạo tác."       # Katamakkhandhapariyāpannanti? Saṅkhārakkhandhapariyāpannanti.
UPC = "tâm tìm cầu sự tái sinh"                           # upapattesiyaṃ cittaṃ (ch12)


def br(subj, how):
    """upapattesiyena cittena samuṭṭhitaṃ X upapattesiye citte bhijjamāne ekadesaṃ / anavasesaṃ bhijjati"""
    return f"{subj} do {UPC} sinh ra, khi {UPC} đang tan rã, thì tan rã {how}"


# ================================================================ (83) Kammahetu
KX11 = "nghiệp làm nguyên nhân"                           # Kammahetukathā
KH = "do nghiệp"                                          # kammahetu / X-kammassa hetu


def kh(x, neg=False):
    return f"{KH}, {C2.P(x, neg)}"                        # kammahetu X X-phalā (na) parihāyati (ch2)


CR = C10.CRIMES
MV = (f" [{VAR} (Syā.): mātughātakakammassa; (Ka.): mātughātikammassa; cũng vậy ở các từ pitughāta-, "
      "arahantaghātakammassa]")
KILL = [k.replace("kẻ ", "", 1) for k in C10.KILLERS]     # giết mẹ … chia rẽ Tăng đoàn (ch10)
ACTS = [CR[0], CR[1], "có hành vi sai trái trong các dục lạc", CR[2], CR[3], CR[4], CR[5],
        KILL[0] + MV, KILL[1], KILL[2], KILL[3], KILL[4]]
# pāṇātipāta, adinnādāna, kāmesumicchācāra (ch11), musāvāda, pisuṇavācā, pharusavācā, samphappalāpa, mātughāta …
# saṅghabheda
ABB = "vu khống các bậc A-la-hán"                         # arahantānaṃ abbhācikkhati

# ================================================================ vagga close (ch9 frame)
UDDANA = (f"{cap(KX1)}, {AB}, {T3}, {T4}, {T5}, {T6}, {T7Q}, {T8}, {RK}, {RU} là sự sống, sa sút {KH}.")
# Cha gatiyo, antarābhavo, pañceva kāmaguṇā kāmadhātu, pañceva āyatanā kāmā, rūpino dhammā rūpadhātu, arūpino
# dhammā arūpadhātu, saḷāyataniko attabhāvo rūpadhātuyā, atthi rūpaṃ arūpesu, rūpaṃ kammaṃ, rūpaṃ jīvitaṃ
# (jīvita «sự sống» ch11), kammahetukā parihāyatīti.


def heads(n, num, title):
    """#### Aṭṭhamavaggo ^5-16-n-0 / ##### (num) n. <title> ^5-16-n-1-0"""
    return [(4, VAGGA8, f"5-16-{n}-0"), (5, f"({num}) {n}. {K(x=title)}", f"5-16-{n}-1-0")]


def build():
    d = B.Doc()
    d.head(3, VAGGA8, "5-16-0")
    # ------------------------------------------------------------ (73) Chagati
    d.head(4, f"(73) 1. {K(x=KX1)}", "5-16-1-0")
    d.seg("5-503",
          f"{Q(T1)} {AM} {NANU(f'{V5} [Trung Bộ Kinh 1.153]')} {AM} Nếu {V5}; {NO_CA_VATA} “{T1}”.",
          f"{Q(T1)} {AM} {NANU(f'{KKC_V} {same(PETA)}')} {AM} Nếu {KKC} {same(PETA)}, {NO_CA_VATA} “{T1}”.",
          f"{Q(T1)} {AM} {NANU(f'{VP} {same(DEVA)}')} {AM} Nếu {VP} {same(DEVA)}, {NO_CA_VATA} “{T1}”.",
          f"{Q(T1)} {AM} {NANU(PUBBADEVA)} {AM} Nếu {PUBBADEVA}, {NO_CA_VATA} “{T1}”.")
    d.seg("5-504",
          # "Nanu atthi asurakāyoti, āmantā." – comma and lowercase as the Pāli (punctuation kept, reported)
          f"{NVQ(T1)} {AM} Chẳng phải {ASK} sao, đúng vậy. Nếu {ASK}, {TENA_VATA} “{T1}”.",
          E(x=KX1))
    # ------------------------------------------------------------ (74) Antarābhava
    for lv, t, sid in heads(2, 74, KX2):
        d.head(lv, t, sid)
    d.seg("5-505",
          f"{Q(T2)} {AM} {Q('là ' + KB)} {NHP} {q(T2)} {AM} {Q('là ' + RB)} {NHP} {q(T2)} {AM} {Q('là ' + ARB)} "
          f"{NHP} {q(T2)} {AM} {Q(betw(KB, RB))} {NHP} {q(T2)} {AM} {Q(betw(RB, ARB))} {NHP}",
          f"{Q(betw(KB, RB, True))} {AM} Nếu {betw(KB, RB, True)}, {NO_CA_VATA} “{T2}”. "
          f"{Q(betw(RB, ARB, True))} {AM} Nếu {betw(RB, ARB, True)}, {NO_CA_VATA} “{T2}”.")
    d.seg("5-506",
          f"{Q(T2)} {AM} {Q(FIFTH)} {NHP} {q(T2)} {AM} {Q(f'{AB} {BHAVA7}')} {NHP} {q(kamma_up(AB))} {NHP} "
          f"{q(satta_up(AB))} {NHP} {q(life_in(AB))} {NHP} {q(k5_in(AB))} {NHP} {q(f'{AB} {PANCA}')} {NHP}")

    def pairs(x, four=False):
        kin, bhv = (k4_in, CATU) if four else (k5_in, PANCA)
        return (f"{Q(f'có {x}, {x} {BHAVA7}')} {AM} {Q(f'có {AB}, {AB} {BHAVA7}')} {NHP} "
                f"{q(kamma_up(x))} {AM} {Q(kamma_up(AB))} {NHP} {q(satta_up(x))} {AM} {Q(satta_up(AB))} {NHP} "
                f"{q(life_in(x))} {AM} {Q(life_in(AB))} {NHP} {q(kin(x))} {AM} {Q(kin(AB))} {NHP} "
                f"{q(f'{x} {bhv}')} {AM} {Q(f'{AB} {bhv}')} {NHP}")
    d.seg("5-507", pairs(KB), pairs(RB), pairs(ARB, four=True))
    d.seg("5-508",
          f"{Q(T2)} {AM} {Q(SB_ALL)} {NHP} {q(SB_NONE)} {AM} Nếu {SB_NONE}, {NO_CA_VATA} “{T2}”.",
          f"{Q(T2)} {AM} {Q(has(AP))} {NHP} {q(hasnt(AP))} {AM} Nếu {hasnt(AP)}, {NO_CA_VATA} “{T2}”.",
          f"{Q(has(NAP))} {AM} {Q(has(AP))} {NHP} {q(hasnt(AP))} {AM} {Q(hasnt(NAP))} {NHP} "
          f"{q(f'{NIR_UP}… {ASN_UP}… {has(ARU_UP)}')} {NHP} {q(hasnt(ARU_UP))} {AM} Nếu {hasnt(ARU_UP)}, "
          f"{NO_CA_VATA} “{T2}”.",
          f"{Q(has(NARU_UP))} {AM} {Q(has(ARU_UP))} {NHP} {q(hasnt(ARU_UP))} {AM} {Q(hasnt(NARU_UP))} {NHP}")
    d.seg("5-509",
          # "Na vattabbaṃ atthi antarābhavoti?" – no dash, no quotes in the Pāli: kept as written
          f"Có phải không nên nói {T2} không? {AM} {NANU(f'có {PARI_A}')} {AM} Nếu có {PARI_A}, {TENA_VATA_V} "
          f"“{T2}”.",
          f"{katva(f'có {PARI_A}', T2)} {AM} {katva(f'có {PARI_U}', f'có {UB}')} {NHP} "
          f"{katva(f'có {PARI_A}', T2, False)} {AM} {katva(f'có {PARI_AS}… có {PARI_S}', f'có {SSB_}')} {NHP}",
          E(x=KX2))
    # ------------------------------------------------------------ (75) Kāmaguṇa
    for lv, t, sid in heads(3, 75, KX3):
        d.head(lv, t, sid)
    d.seg("5-510",
          five_tp(T3),
          f"{Q(T3)} {AM} {Q(nk('mắt'))} {NHP} "
          f"{q('… '.join(f'{o} {MAN}' for o in ('tai', 'mũi', 'lưỡi', 'thân')) + '… ' + nk('ý'))} {NHP}",
          f"{Q(nk('ý'))} {AM} {NANU_VUTTAM}",
          "“Năm loại dục lạc ở đời, cùng với ý là thứ sáu, đã được tuyên bố;",
          "Sau khi làm phai nhạt ý muốn ở đây, như vậy được giải thoát khỏi khổ đau” "
          "[Kinh Tập 173; Tương Ưng Bộ Kinh 1.30].",
          f"{ATTHEVA} {AM} {TENA_HI_NA(nk('ý'))}")
    d.seg("5-511",
          f"{Q(T3)} {AM} {Q(f'{KG} {BHAVA7}')} {NHP} {q(kamma_up(KG))} {NHP} {q(satta_up(KG))} {NHP} "
          f"{q(life_in(KG))} {NHP} {q(k5_in(KG))} {NHP} {q(f'{KG} {PANCA}')} {NHP} {q(appear(KG))} {NHP}",
          f"{Q(f'{KD} {BHAVA7}')} {AM} {Q(f'{KG} {BHAVA7}')} {NHP} {q(kamma_up(KD))} {AM} {Q(kamma_up(KG))} "
          f"{NHP} {q(satta_up(KD))} {AM} {Q(satta_up(KG))} {NHP}",
          # "paccekasabuddhā" (l.3) = paccekasambuddhā: plain spelling slip, rendered as meant
          f"{Q(life_in(KD))} {AM} {Q(life_in(KG))} {NHP} {q(k5_in(KD))} {AM} {Q(k5_in(KG))} {NHP} "
          f"{q(f'{KD} {PANCA}')} {AM} {Q(f'{KG} {PANCA}')} {NHP} {q(appear(KD))} {AM} {Q(appear(KG))} {NHP}")
    d.seg("5-512",
          f"{NVQ(T3)} {AM} {NANU_VUTTAM} {SUT_FULL}. {ATTHEVA} {AM} {TENA_HI(T3)}",
          E(x=KX3))
    # ------------------------------------------------------------ (76) Kāma
    for lv, t, sid in heads(4, 76, KX4):
        d.head(lv, t, sid)
    d.seg("5-513", five_tp(T4))
    d.seg("5-514",
          f"{NVQ(T4)} {AM} {NANU_VUTTAM} {SUT_ABBR}”. {ATTHEVA} {AM} {TENA_HI(T4)}",
          f"{Q(T4)} {AM} {NANU_VUTTAM} {SUT_ABBR}. Tuy nhiên, này các tỳ-khưu, những thứ ấy không phải là các dục "
          "lạc, trong giới luật của bậc thánh, chúng được gọi là các loại dục lạc” –",
          f"“{cap(SR)} là dục lạc của con người,",
          "Những thứ muôn màu ở đời không phải là các dục lạc;",
          f"{cap(SR)} là dục lạc của con người,",
          "Những thứ muôn màu vẫn đứng vững y như vậy ở đời;",
          f"Thế nên, ở đây người trí dẹp bỏ {CH}” [{CITE_AN663}].",
          f"{ATTHEVA} {AM} {TENA_HI_NA(T4)}",
          E(x=KX4))
    # ------------------------------------------------------------ (77) Rūpadhātu
    for lv, t, sid in heads(5, 77, KX5):
        d.head(lv, t, sid)
    d.seg("5-515",
          f"{Q(T5)} {AM} {Q(f'{RU} {BHAVA7}')} {NHP} {q(kamma_up(RU))} {NHP} {q(satta_up(RU))} {NHP} "
          f"{q(life_in(RU))} {NHP} {q(k5_in(RU))} {NHP} {q(f'{RU} {PANCA}')} {NHP}",
          f"{Q(f'{RDH} {BHAVA7_PE}')} {AM} {Q(f'{RU} {BHAVA7_PE}')} {NHP} {q(kamma_up(RDH))} {AM} "
          f"{Q(kamma_up(RU))} {NHP} {q(satta_up(RDH))} {AM} {Q(satta_up(RU))} {NHP}",
          f"{Q(life_in(RDH))} {AM} {Q(life_in(RU))} {NHP} {q(k5_in(RDH))} {AM} {Q(k5_in(RU))} {NHP} "
          f"{q(f'{RDH} {PANCA}')} {AM} {Q(f'{RU} {PANCA}')} {NHP}")
    d.seg("5-516",
          f"{Q(f'{T5}, {KDY} có {RU}')} {AM} {Q(sava(RDH))} {NHP} {q(sava(RDH))} {AM} {Q(SAM2)} {NH}",
          E(x=KX5))
    # ------------------------------------------------------------ (78) Arūpadhātu
    for lv, t, sid in heads(6, 78, KX6):
        d.head(lv, t, sid)
    d.seg("5-517",
          f"{Q(T6)} {AM} {Q(f'{VE} {BHAVA7}')} {NHP} {q(kamma_up(VE))} {NHP} {q(satta_up(VE))} {NHP} "
          f"{q(life_in(VE))} {NHP} {q(k4_in(VE))} {NHP} {q(f'{VE} {CATU}')} {NHP}",
          f"{Q(f'{ARDH} {BHAVA7_PE}')} {AM} {Q(f'{VE} {BHAVA7_PE}')} {NHP} {q(kamma_up(ARDH))} {AM} "
          f"{Q(kamma_up(VE))} {NHP} {q(satta_up(ARDH))} {AM} {Q(satta_up(VE))} {NHP}",
          f"{Q(life_in(ARDH))} {AM} {Q(life_in(VE))} {NHP} {q(k4_in(ARDH))} {AM} {Q(k4_in(VE))} {NHP} "
          f"{q(f'{ARDH} {CATU}')} {AM} {Q(f'{VE} {CATU}')} {NHP}")
    d.seg("5-518",
          f"{Q(f'{T6}, {KDY} {FOURK}')} {AM} {Q(sava(ARDH))} {NHP} {q(sava(ARDH))} {AM} {Q(SAM2A)} {NHP}",
          f"{Q(f'{T5}, {T6}, {KDY} {FIVEK}')} {AM} {Q(sava(RDH, ARDH))} {NHP} {q(sava(RDH, ARDH))} {AM} "
          f"{Q(SAM3)} {NHP}",
          E(x=KX6))
    # ------------------------------------------------------------ (79) Rūpadhātuyā āyatana
    for lv, t, sid in heads(7, 79, KX7):
        d.head(lv, t, sid)
    d.seg("5-519",
          f"{Q(T7)} {AM} {Q(there(NOSE))} {AM} {Q(there(SMELL))} {NHP} {q(there(TONG))} {AM} {Q(there(TASTE))} "
          f"{NHP} {q(there(BODY))} {AM} {Q(there(TOUCH))} {NHP}",
          f"{Q(nthere(SMELL))} {AM} {Q(nthere(NOSE))} {NHP} {q(nthere(TASTE))} {AM} {Q(nthere(TONG))} {NHP} "
          f"{q(nthere(TOUCH))} {AM} {Q(nthere(BODY))} {NHP}")
    d.seg("5-520",
          f"{Q(pair(EYE, FORM))} {AM} {Q(pair(NOSE, SMELL))} {NHP} {q(pair(EYE, FORM))} {AM} "
          f"{Qc([pair(TONG, TASTE), pair(BODY, TOUCH)])} {NHP} {Qc([pair(EAR, SOUND), pair(MIND, MOBJ)], False)} "
          f"{AM} {Q(pair(NOSE, SMELL))} {NHP} {q(pair(MIND, MOBJ))} {AM} "
          f"{Qc([pair(TONG, TASTE), pair(BODY, TOUCH)])} {NHP}",
          f"{Q(npair(NOSE, SMELL))} {AM} {Q(npair(EYE, FORM))} {NHP} {q(npair(NOSE, SMELL))} {AM} "
          f"{Qc([npair(EAR, SOUND), npair(MIND, MOBJ)])} {NHP} {Qc([npair(TONG, TASTE), npair(BODY, TOUCH)], False)} "
          f"{AM} {Q(npair(EYE, FORM))} {NHP} {q(npair(BODY, TOUCH))} {AM} "
          f"{Qc([npair(EAR, SOUND), npair(MIND, MOBJ)])} {NHP}")
    d.seg("5-521",
          # "atthi tattha cakkhāyatanaṃ atthi rūpāyatanaṃ, …" – the missing comma rendered as meant
          f"{Q(full(0))} {AM} {Q(full(2))} {NHP} {q(full(0))} {AM} {Qc([full(3), full(4)])} {NHP}",
          f"{Qc([pr(1), full(5)])} {AM} {Q(full(2))} {NHP} {q(full(5))} {AM} {Qc([pr(3), full(4)])} {NHP}",
          f"{Q(full(2, True))} {AM} {Q(full(0, True))} {NHP} {q(full(2, True))} {AM} "
          f"{Qc([pr(1), full(5, True)])} {NHP}",
          f"{Qc([pr(3), full(4, True)])} {AM} {Qc([pr(1), full(5, True)])} {NHP}")
    d.seg("5-522",
          f"{Q(full(2))} {AM} {Q(there(GANDHA))} {NHP}",
          f"{Q(full(3))} {AM} {Q(there(RASA))} {NHP}",
          f"{Q(full(4))} {AM} {Q(there(PHOT))} {NHP}")
    d.seg("5-523",
          f"{NVQ(T7Q)} {AM} {NANU(there(NIM))} {AM} Nếu {there(NIM)}, {TENA_VATA} “{T7Q}”.",
          E(x=KX7))
    # ------------------------------------------------------------ (80) Arūpe rūpa
    for lv, t, sid in heads(8, 80, KX8):
        d.head(lv, t, sid)
    d.seg("5-524",
          f"{Q(T8)} {AM} {Q('là ' + six(OR))} {NHP} {nanu('là ' + six(OAR))} {AM} Nếu là {six_pe(OAR)}, "
          f"{NO_CA_VATA} “{T8}”.",
          f"{Q(T8)} {AM} {Q(bare7(PANCA_N))} {NHP} {nanu(bare7(CATU_N, pe=True))} {AM} "
          f"Nếu {bare7(CATU_N, True, True)}, {NO_CA_VATA} “{T8}”.")
    d.seg("5-525",
          # [arūpadhātuyā (sabbattha)]: the text reads rūpadhātuyā; translated as written, the variant kept
          f"{Q(f'{RIR}, và đó là {six(OR)}')} {AM} {Q(f'{T8}, và đó là {six_pe(OR, True)}')} {NHP} "
          f"{q(f'{RIR}, và đó {bare7(PANCA_N, True, True)}')} {AM} {Q(f'{T8}, và đó {bare7(PANCA_N, True, True)}')} "
          f"{NHP} {Q(f'{T8}, và đó là {six(OAR)}')} {AM} {Q(f'{RIR}{SAB}, và đó là {six_pe(OAR, True)}')} {NHP} "
          f"{q(f'{T8}, và đó {bare7(CATU_N, True, True)}')} {AM} {Q(f'{RIR}{SAB}, và đó {bare7(CATU_N, True, True)}')} "
          f"{NHP}")
    d.seg("5-526",
          f"{Q(T8)} {AM} {NANU(VESC)} {AM} Nếu {VESC}, {NO_CA_VATA} “{T8}”.",
          f"{Q(f'Đức Thế Tôn đã nói rằng {ESC}, {T8}')} {AM} {Q(NEKKH)} {NHP}",
          E(x=KX8))
    # ------------------------------------------------------------ (81) Rūpaṃ kammanti
    for lv, t, sid in heads(9, 81, KX9):
        d.head(lv, t, sid)
    KK, KA, VKK, VKA = kk(TH), kk(BT), vk(TH), vk(BT)
    d.seg("5-527",
          first_line(KK, TH, True, True, False, ","),
          second_line(KK, TH, TH, CS_K),
          third_line(KK, TH, TH, CS_K))
    d.seg("5-528",
          all_line(KK, TH, TH),
          el_line(KK, TH, TH),
          ab_line(KK, TH))
    d.seg("5-529", el_line(KK, TH, TH, an=True), ab_line(KK, TH, an=True))
    d.seg("5-530", el_line(KK, TH, TH, pv=True), ab_line(KK, TH, pv=True))
    d.seg("5-531", el_line(KK, TH, TH, an=True, pv=True), ab_line(KK, TH, an=True, pv=True))
    d.seg("5-532",
          first_line(VKK, TH, False, False, False, ";"),
          second_line(VKK, TH, TH, CS_K),
          third_line(VKK, TH, TH, CS_K),
          f"{all_line(VKK, TH, TH)} giống như nghiệp bằng thân, nghiệp bằng lời nói cũng vậy.")
    d.seg("5-533",
          first_line(KA, BT, True, True, True, ";"),
          second_line(KA, BT, BT, CS_A),
          third_line(KA, BT, BT, CS_A),
          all_line(KA, BT, BT))
    d.seg("5-534",
          first_line(VKA, BT, False, False, False, ";"),
          second_line(VKA, BT, BT, CS_A),
          third_line(VKA, BT, BT, CS_A),
          all_line(VKA, BT, BT))
    d.seg("5-535", el_line(VKA, BT, BT, asu=True), ab_line(VKA, BT, asu=True))
    d.seg("5-536", el_line(VKA, BT, BT, an=True, asu=True), ab_line(VKA, BT, an=True, asu=True))
    p_pv, p_anpv = pr_(KX, pv=True), pr_(KX, an=True, pv=True)
    d.seg("5-537",
          el_line(VKA, BT, BT, pv=True, asu=True),
          # l.2: the second question adds anārammaṇaṃ (the pattern has phassavippayuttaṃ only): as written
          f"{Q(f'{rf(BT)} {p_pv}')} {AM} {Q(f'{VKA} {p_anpv}')} {NHP} {q(f'{rest(BT, True)} {p_anpv}')} {AM} "
          f"{Q(f'{VKA} {p_anpv}')} {NHP}",
          el_line(VKA, BT, BT, an=True, pv=True, asu=True),
          ab_line(VKA, BT, an=True, pv=True, asu=True))
    d.seg("5-538",
          f"{NVQ(RKA)} {AM} {NANU(KVA)} {AM} Nếu {KVA}, {TENA_VATA} “{RKA}”.",
          f"{Q(RKA)} {AM} {Q(f'{EYE} {TV}')} {NHP} {q(RKA)} {AM} {Q(f'{REST11} {TV}')} {NHP}",
          f"{Q('thân là vật chất, nghiệp bằng thân là vật chất')} {AM} "
          f"{Q('ý là vật chất, nghiệp bằng ý là vật chất')} {NHP} "
          f"{q('ý là phi vật chất, nghiệp bằng ý là phi vật chất')} {AM} "
          f"{Q('thân là phi vật chất, nghiệp bằng thân là phi vật chất')} {NHP}",
          " ".join(f"{Q(KR_) if i == 0 else q(KR_)} {AM} {Q(f'nếu {o} là vật chất, thì {v} là vật chất')} {NHP}"
                   for i, (o, v) in enumerate(VINN5)))
    d.seg("5-539",
          f"{Q(RK)} {AM} {NANU_VUTTAM} {CETANA_S} [{CITE_AN663}]! {ATTHEVA} {AM} {TENA_HI_NA(RK)}",
          f"{Q(RK)} {AM} {NANU_VUTTAM} {SUT_DOOR} {ATTHEVA} {AM} {TENA_HI_NA(RK)}",
          f"{Q(RK)} {AM} {NANU_VUTTAM} {SUT_10} {ATTHEVA} {AM} {TENA_HI_NA(RK)}",
          f"{Q(RK)} {AM} {NANU_VUTTAM} {SUT_SAM} {ATTHEVA} {AM} {TENA_HI_NA(RK)}",
          E(x=KX9))
    # ------------------------------------------------------------ (82) Jīvitindriya
    for lv, t, sid in heads(10, 82, KX10):
        d.head(lv, t, sid)
    d.seg("5-540",
          f"{Q(NRJ)} {AM} {Q(life(RD2, True))} {NHP} {q(life(RD2))} {AM} Nếu {life(RD2)}, {NO_CA_VATA} “{NRJ}”.",
          f"{Q(f'{life(AD2)}, có {AJ}')} {AM} {Q(f'{life(RD2)}, có {RJ}')} {NHP} "
          f"{q(f'{life(RD2)}, không có {RJ}')} {AM} {Q(f'{life(AD2)}, không có {AJ}')} {NHP}",
          f"{Q(f'{ayu(AD2)} là {AJ}')} {AM} {Q(f'{ayu(RD2)} là {RJ}')} {NHP} {q(nv(ayu(RD2), RJ))} {AM} "
          f"{Q(nv(ayu(AD2), AJ))} {NHP}")
    d.seg("5-541",
          f"{Q(f'{ayu(RD2)} là {AJ}')} {AM} {Q(f'{ayu(AD2)} là {RJ}')} {NHP}",
          f"{Q(nv(ayu(AD2), RJ))} {AM} {Q(nv(ayu(RD2), AJ))} {NHP}",
          f"{Q(f'{ayu(BOTH)} là {AJ}')} {AM} {Q(f'{ayu(BOTH)} là {RJ}')} {NHP}",
          f"{Q(nv(ayu(BOTH), RJ))} {AM} {Q(nv(ayu(BOTH), AJ))} {NHP} {q(NRJ)} {AM} {Q(f'{NIRS} không có {JI}')} {NHP}")
    d.seg("5-542",
          f"{Q(f'{NIRS} có {JI}')} {AM} Nếu {NIRS} có {JI}, {NO_CA_VATA} “{NRJ}”.",
          f"{Q(f'{NIRS} có {JI}')} {AM} {WHICH} {Q(f'{NIRS} có khối tạo tác')} {NHP}",
          f"{Q(f'{NIRS} có khối tạo tác')} {AM} {Q(f'{NIRS} có {KH_PE}')} {NHP}",
          f"{Q(f'{NIRS} có {KH_PE}')} {AM} {Q('không phải là ' + NIRS)} {NHP}")
    d.seg("5-543",
          f"{Q(NRJ)} {AM} {Q(f'{ASS} không có {JI}')} {NHP}",
          f"{Q(f'{ASS} có {JI}')} {AM} Nếu {ASS} có {JI}, {NO_CA_VATA} “{NRJ}”. {Q(f'{ASS} có {JI}')} {AM} "
          f"{WHICH} {Q(f'{ASS} có khối tạo tác')} {NHP}",
          f"{Q(f'{ASS} có khối tạo tác')} {AM} {Q(f'{ASS} có {KH_PE}')} {NHP}",
          f"{Q(f'{ASS} có {KH_PE}')} {AM} {Q(PANCA)} {NHP}")
    d.seg("5-544",
          f"{Q(br(JI, 'một phần'))} {AM} {Q(br('sự tiếp xúc', 'một phần'))} {NHP}",
          f"{Q(br('sự tiếp xúc', 'không còn sót lại'))} {AM} {Q(br(JI, 'không còn sót lại'))} {NHP}")
    d.seg("5-545",
          f"{Q(f'có hai {JI}')} {AM} {Q('sống bằng hai sự sống, qua đời bằng hai sự chết')} "
          f"Đúng vậy [{VAR} (Syā., Kaṃ., Pī.): na hevaṃ vattabbe].",
          E(x=KX10))
    # ------------------------------------------------------------ (83) Kammahetu
    for lv, t, sid in heads(11, 83, KX11):
        d.head(lv, t, sid)
    d.seg("5-546",
          f"{Q(kh(C2.AR))} {AM} {Q(kh(C2.SO))} {NHP} {q(kh(C2.AR))} {AM} "
          f"Có phải {KH}, {C2.SA}… {C2.P(C2.AN)} không? {NHP}",
          f"{Q(kh(C2.SO, True))} {AM} {Q(kh(C2.AR, True))} {NHP} có phải {KH}, {C2.SA}… {C2.P(C2.AN, True)} "
          f"không? {AM} {Q(kh(C2.AR, True))} {NHP}",
          f"{Q(kh(C2.AR))} {AM} {Q(f'{KH} {ACTS[0]}')} {NHP} {q('… '.join(f'{KH} {a}' for a in ACTS[1:]))} {NHP}",
          f"Do nghiệp nào? Vì {ABB}. {Q(f'{KH} {ABB}, {C2.P(C2.AR)}')} {AM} "
          f"{Q(f'bất cứ ai {ABB}, tất cả những người ấy đều tự mình chứng nghiệm {C2.FRUIT[C2.AR]}')} {NHP}",
          E(x=KX11),
          f"{VAGGA8}.",
          C9.TASSUDDANAM,
          UDDANA)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    (LIFE7, 1), (RD2, 1), (AD2, 1), (GANDHA, 1), (RASA, 1), (PHOT, 1), ("năng lực sống", 1),
    ("nghiệp bằng thân, nghiệp bằng lời nói, nghiệp bằng ý do chúng sinh ra", 1),
    ("Các hiện tượng có đối tượng", 1), ("Các hiện tượng không có đối tượng", 1), ("không gắn liền với tâm", 1),
    ("nghiệp có quả không gián đoạn", 1), ("không nằm trong các cõi tồn tại", 1), (KX, 1), ("sự hân hoan", 1),
    ("niềm vui", 1), ("sự tồn tại cá nhân", 1), ("Các hiện tượng thuộc vật chất", 1), ("Các hiện tượng phi vật chất", 1),
    ("chủ ý", 1), ("sự tiếp xúc", 1), ("không khó chịu cũng không dễ chịu", 1), ("ô nhiễm", 1),
    ("Sự hiện hữu ở cõi dục lạc, sự hiện hữu ở cõi hình sắc, sự hiện hữu ở cõi không hình sắc", 2),
    ("sự hiện hữu gồm năm khối", 2), ("sự hiện hữu gồm bốn khối", 2),
    ("dẫn đến địa ngục", 2), ("cõi súc sinh", 2), ("cõi ngạ quỷ", 2), ("chư thiên", 2),
    ("Ý muốn là dục lạc, sự tham đắm là dục lạc, sự tham đắm do ý muốn là dục lạc, tư duy là dục lạc, sự tham đắm là "
     "dục lạc, sự tham đắm do tư duy là dục lạc", 2),
    ("liên quan đến", 2), ("sự hướng đến, sự chú hướng, sự lưu ý hay sự chú tâm", 2), ("lối thoát", 2),
    ("yếu tố từ bỏ", 2), ("liên quan đến sự từ bỏ", 2), ("trong cõi dục lạc", 2), ("nước mắt", 2),
    ("máu, mồ hôi", 2), ("việc nói lời phù phiếm", 2), ("khối tạo tác", 2), ("ở nơi bản thân", 2),
    ("thức qua tai", 2), ("thức qua thân", 2),
    ("sự hiện hữu ở cõi dục lạc", 3),
    (PARI_A, 4), (PARI_U, 4), (PARI_AS, 4), (PARI_S, 4), ("sa sút khỏi", 4), ("bậc Độc Giác", 4),
    ("Tăng Chi Bộ Kinh", 4), ("Trung Bộ Kinh", 4),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (f"{KG_HEAD[1:]}, {KG_Q}{KG_MID}{KG_TOUCH}", "10-dutiyavaggo.md"), ("Này các tỳ-khưu, đây là năm loại dục lạc",
                                                                       "10-dutiyavaggo.md"),
    ("Đức Thế Tôn đã nói rằng", "10-dutiyavaggo.md"), ("nói lời phù phiếm", "10-dutiyavaggo.md"),
    ("lấy của không được cho", "10-dutiyavaggo.md"), ("kẻ làm chảy máu", "10-dutiyavaggo.md"),
    ("kẻ chia rẽ Tăng đoàn", "10-dutiyavaggo.md"), ("đồ bất tịnh", "10-dutiyavaggo.md"),
    ("tất cả những người ấy đều", "10-dutiyavaggo.md"), ("dùng mũi", "10-dutiyavaggo.md"),
    (BHAVA7, "14-chatthavaggo.md"), (f"có nghiệp {UPAGA}", "14-chatthavaggo.md"), (LIFE5, "14-chatthavaggo.md"),
    (CATU, "14-chatthavaggo.md"), (NIRS, "14-chatthavaggo.md"), ("nghiệp bằng thân", "14-chatthavaggo.md"),
    (FOURK, "14-chatthavaggo.md"), ("yếu tố đất", "14-chatthavaggo.md"),
    (f"{C3.SSB} xuất hiện, {C3.PCB} xuất hiện, {C3.SVY} xuất hiện", "3-brahmacariyakatha.md"),
    (UPC, "12-catutthavaggo.md"), ("được trang bị", "12-catutthavaggo.md"), ("chính", "12-catutthavaggo.md"),
    (ASS, "11-tatiyavaggo.md"), ("sự mong cầu", "11-tatiyavaggo.md"), ("Có phải vì cho rằng", "11-tatiyavaggo.md"),
    ("có hành vi sai trái trong các dục lạc", "11-tatiyavaggo.md"), ("và đó là", "11-tatiyavaggo.md"),
    ("ở đó có", "11-tatiyavaggo.md"), ("sự sống", "11-tatiyavaggo.md"),
    ("sa sút khỏi trạng thái A-la-hán", "2-parihanikatha.md"), ("sa sút khỏi thành quả vào dòng", "2-parihanikatha.md"),
    (UD_BAD, "1-puggalakatha.md"), (UD_GOOD, "1-puggalakatha.md"), ("hơi khác một chút", "1-puggalakatha.md"),
    ("[dị bản (Trung Bộ Kinh 1.244): ", "1-puggalakatha.md"), ("Kinh Phật Thuyết Như Vậy", "11-tatiyavaggo.md"),
    ("Kinh Tập", "1-puggalakatha.md"), ("Trường Bộ Kinh", "13-pancamavaggo.md"), ("ấy mà", "13-pancamavaggo.md"),
    ("không nên được gọi là – “", "13-pancamavaggo.md"), (PAT, "13-pancamavaggo.md"),
    ("Tóm tắt của chương này –", "9-hevatthikatha.md"), ("tất cả điều ấy đều", "13-pancamavaggo.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(st, f"pi-{b}") for st, b in CROSS if st not in texts[b]]
    missing += [(st, f) for st, f in PI5 if st not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for st, w in missing:
        print(f"CROSS MISSING in {w}: {st}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch16 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
