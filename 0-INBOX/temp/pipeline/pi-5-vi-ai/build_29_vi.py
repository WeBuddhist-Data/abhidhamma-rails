# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 29: 29-ekavisatimavaggo.md (Ekavīsatimavaggo,
^5-29-0 … ^5-891), the eight kathā (200)-(207) of the twenty-first vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_2 / 4 / 10 / 11 / 12 / 14 / 15 / 19 / 20 (read-only; importing writes nothing) for strings shared
with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4 Vietnamese rails is
asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur in that chapter's
output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli.
Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_29_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (DEV6, kilesa names, sakkāyadiṭṭhi, sīlabbataparāmāsa)
import build_4_vi as C4      # noqa: E402  (puthujjano, POS: asaṃkilesiya)
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –, requisites, jhāna, deva names)
import build_11_vi as C11    # noqa: E402  (sāsava … saṃkilesiya OBJ, nevasaññānāsaññāyatana, MPN list)
import build_12_vi as C12    # noqa: E402  (phassa … paññā L10)
import build_14_vi as C14    # noqa: E402  (ākāsānañcāyatana)
import build_15_vi as C15    # noqa: E402  (hanci_no, nanu_l)
import build_19_vi as C19    # noqa: E402  (mā nirujjhī / niccaṃ hotu / jātidhammā sattā mā jāyiṃsu)
import build_20_vi as C20    # noqa: E402  (Kammakathā «Bàn về nghiệp»)

NAME = "29-ekavisatimavaggo.md"
Q, q, AM, cap, chain = B.Q, B.q, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_VATA = B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_VATA
VAR = B.VAR
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA21 = B.VAGGA[21]                                     # Ekavīsatimavaggo = «Chương thứ hai mươi mốt» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
hanci_no, nanu_l = C15.hanci_no, C15.nanu_l               # Hañci P, no ca vata re vattabbe – "Q"ti. / …pe… nanu Xti?
RUPA, VEDANA, SANNA, SANKHARA, VINNANA = B.RUPA, B.VEDANA, B.SANNA, B.SANKHARA, B.VINNANA

# ================================================================ kathā names (headings and closing lines)
KX = {1: "giáo huấn",                                     # Sāsanakathā (terms file; sāsana pi-2)
      2: "sự không tách khỏi",                            # Avivittakathā (vivicca «tách khỏi» pi-1 ^1-160)
      3: "xiềng xích",                                    # Saṃyojanakathā (saṃyojana «xiềng xích» pi-1)
      4: "thần thông",                                    # Iddhikathā (iddhi «thần thông» pi-1)
      5: "chư Phật",                                      # Buddhakathā (buddhā «chư Phật» pi-2 ^2-934)
      6: "tất cả các phương",                             # Sabbadisākathā (disā «phương» pi-2 ^2-644)
      7: "các hiện tượng",                                # Dhammakathā (dhamma core)
      8: C20.KX2}                                         # Kammakathā = «Bàn về nghiệp» (ch20)
assert KX[8] == "nghiệp"


def heads(n):
    """#### Ekavīsatimavaggo ^5-29-n-0 / ##### (199+n) n. <title> ^5-29-n-1-0"""
    return [(4, VAGGA21, f"5-29-{n}-0"), (5, f"({199 + n}) {n}. {K(x=KX[n])}", f"5-29-{n}-1-0")]


# ================================================================ (200) Sāsana
SAS = "giáo huấn"                                         # sāsanaṃ (pi-2)
TSAS = f"{SAS} của Như Lai"                               # tathāgatassa sāsanaṃ (Như Lai pi-2)
DEV6 = C2.DEV6                                            # satipaṭṭhānā … bojjhaṅgā (pi-3, ch2)
DEV6_PE = "… ".join(DEV6[1:])                             # sammappadhānā…pe… … bojjhaṅgā
KATA = "đã được làm mới"                                  # navaṃ kataṃ / katā
KAROTI = "có ai đó làm mới"                               # atthi koci … navaṃ karoti (koci «ai đó» sample)
KATUM = "có thể làm mới lại"                              # labbhā … puna navaṃ kātuṃ (labbhā «có thể» ch12, ch15)
AKU, KU = "là bất thiện", "thiện"                         # pubbe akusalaṃ / pacchā kusalaṃ
OBJ = C11.OBJ                                             # sāsava … saṃkilesiya (pi-1 matrix, ch4, ch11)
OBJ_LONG = f"{OBJ[0]}… {', '.join(OBJ[1:8])}… {OBJ[8]}"   # sāsavaṃ…pe… saṃyojaniyaṃ … upādāniyaṃ…pe… saṃkilesikaṃ
OBJ_PE = C11.OBJ_PE                                       # sāsavaṃ…pe… saṃkilesikaṃ / saṃkilesiyaṃ
ASK = C4.POS[-1]                                          # asaṃkilesikaṃ / asaṃkilesiyaṃ «không phải là đối tượng của phiền não»
assert OBJ_PE == f"{OBJ[0]}… {OBJ[8]}" and ASK == "không phải là đối tượng của phiền não"


def kata(x, y):
    """pubbe X pacchā Y kataṃ (pubbe … pacchā «trước đó … sau đó» ch21)"""
    return f"điều trước đó {x}, sau đó đã được làm thành điều {y}"


def kar(x, y):
    """atthi koci pubbe X pacchā Y karoti"""
    return f"có ai đó làm cho điều trước đó {x}, sau đó trở thành điều {y}"


def katum(x, y):
    """labbhā pubbe X pacchā Y kātuṃ"""
    return f"có thể làm cho điều trước đó {x}, sau đó trở thành điều {y}"


T1 = f"{SAS} {KATA}"                                      # sāsanaṃ navaṃ kataṃ
T1B = f"{KAROTI} {TSAS}"                                  # atthi koci tathāgatassa sāsanaṃ navaṃ karoti
T1C = f"{KATUM} {TSAS}"                                   # labbhā tathāgatassa sāsanaṃ puna navaṃ kātuṃ

# ================================================================ (201) Avivitta
PU = C4.PUTHUJJANA                                        # puthujjano «người phàm phu» (pi-1, ch4)
AV = "không tách khỏi"                                    # avivitto (vivicca «tách khỏi» pi-1)
TD = "thuộc ba cõi"                                       # tedhātuka (new; kāmadhātu «cõi dục lạc» pi-1)
T2 = f"{PU} {AV} các hiện tượng {TD}"                     # puthujjano tedhātukehi dhammehi avivitto
T2K = f"{PU} {AV} các nghiệp {TD}"                        # puthujjano tedhātukehi kammehi avivitto
L10 = C12.L10                                             # phassa, vedanā … paññā (ch4 / ch12 wording)
AV_CHAIN = (f"{PU} {AV} các {L10[0]} {TD}… các {L10[1]} {TD}… "
            + "… ".join(f"các {x}" for x in L10[2:9]) + f"… các {L10[9]} {TD}")
# puthujjano tedhātukehi phassehi…pe… tedhātukāhi vedanāhi… saññāhi … cetanāhi… … samādhīhi…pe… tedhātukāhi paññāhi
CIV, PIN, SEN, GIL = "y phục", "đồ ăn khất thực", "chỗ ở", "thuốc men và vật dụng chữa bệnh"
assert C10.REQ == f"{CIV}, {PIN}, {SEN}, {GIL}"           # cīvara … gilānapaccayabhesajjaparikkhāra (pi-2, ch10)
JH = C10.J                                                # tầng thiền thứ nhất … thứ tư (pi-1)
AKA = C14.AKA                                             # ākāsānañcāyatana (pi-2, ch14)
NS_A = C11.NS                                             # nevasaññānāsaññāyatana (pi-1, ch11)
UV = "chứng nhập và an trú"                               # upasampajja viharati (pi-1 ^1-160, ch3)
DETI = "cho"                                              # deti (dadāti «cho» pi-4, ch15, ch21)


def khane(x):
    """yasmiṃ khaṇe puthujjano X deti, tasmiṃ khaṇe … (khaṇa «khoảnh khắc» ch10, ch23)"""
    return f"vào khoảnh khắc nào {PU} {DETI} {x}, vào khoảnh khắc ấy"


UPAGA = C14.UPAGA                                         # -ūpaga «đi đến» (ch14)
PARI = (f"nghiệp {UPAGA} cõi hình sắc và cõi không hình sắc đã được {PU} hiểu biết trọn vẹn")
# puthujjanassa rūpadhātuarūpadhātūpagaṃ kammaṃ pariññātaṃ (genitive agent as ch2 «đã được người ấy hiểu biết
# trọn vẹn»; rūpadhātu / arūpadhātu «cõi hình sắc / cõi không hình sắc» pi-1)

# ================================================================ (202) Saṃyojana
AR = "bậc A-la-hán"                                       # arahā (pi-4)
APP = "chưa dứt bỏ"                                       # appahāya (ch12 «chưa dứt bỏ xiềng xích»)
AP = "sự đạt đến trạng thái A-la-hán"                     # arahattappatti (patti «sự đạt đến» pi-2, ch27; arahatta)
T3 = f"có {AP} khi {APP} xiềng xích nào đó"               # atthi kiñci saṃyojanaṃ appahāya arahattappatti
SAM_CHAIN = (f"có {AP} khi {APP} {C2.SK} nào đó… {APP} {C2.VI}… {APP} {C2.SB}… {APP} {C2.R}… {APP} {C2.D}… "
             f"{APP} {C2.M}… {APP} {C2.AO}")
# atthi kiñci sakkāyadiṭṭhiṃ appahāya…pe… vicikicchaṃ … sīlabbataparāmāsaṃ … rāgaṃ … dosaṃ … mohaṃ …
# anottappaṃ appahāya arahattappatti
SA8 = ["tham đắm", "sân hận", "si mê", "kiêu mạn", "gièm pha", "ganh đua", "tuyệt vọng", "phiền não"]
# rāga dosa moha māna (ch5 sarāga … samāna) makkha paḷāsa (pi-2 «sự gièm pha, sự ganh đua») upāyāsa (ch5
# saupāyāsa «có tuyệt vọng») kilesa (ch11 / ch19 nikkileso «không có phiền não»)
SA_ALL = ", ".join(f"có {x}" for x in SA8)                # sarāgo sadoso … sakileso
NI_ALL = ", ".join(f"không có {x}" for x in SA8)          # nirāgo niddoso … nikkileso
NI_PE = f"không có {SA8[0]}… không có {SA8[-1]}"          # nirāgo…pe… nikkileso
BV = f"{AR} biết toàn bộ phạm vi của Đức Phật"            # arahā sabbaṃ buddhavisayaṃ jānāti (visaya «phạm vi» ch11)

# ================================================================ (203) Iddhi
T4 = "có thần thông theo ý định của chư Phật hay của các đệ tử"
# atthi adhippāyaiddhi buddhānaṃ vā sāvakānaṃ vā (adhippāya «ý định» terms file (218); iddhi pi-1; buddhā «chư
# Phật» pi-2; sāvaka «đệ tử» ch4, ch11)
T4_PE = "có thần thông theo ý định"                       # atthi adhippāyaiddhi… (abridged)
MONG = "mong cho"                                         # -tu / mā -ī (imperative / prohibitive wish)
CAY = "các cây"                                           # rukkhā (rukkha «cây» ch15)
UPP = C19.UPP                                             # uppanna «đã sinh khởi» (pi-1, ch19)
NZ = "đừng chấm dứt"                                      # mā nirujjhī (ch19, ch24)
NICCA = "thường còn"                                      # niccaṃ hotu (ch19 «… thường còn»)
SATTA, J4 = C19.SATTA, C19.J4                             # jāti- … maraṇadhammā sattā mā jāyiṃsu … mīyiṃsu (pi-2, ch19)


def st(i):
    """jātidhammā sattā mā jāyiṃsu (ch19 hold wording)"""
    return f"{SATTA.format(x=J4[i][0])} {J4[i][1]}"


PIL = "tôn giả Pi-lin-đa-vác-cha"                         # āyasmā pilindavaccho (āyasmā ch5; Vaccha «Vác-cha» ch12)
KING = "vua Seniya Tần-bà-sa-la xứ Ma-kiệt-đà"            # rañño māgadhassa seniyassa bimbisārassa (Seniya sample;
# Magadha «xứ Ma-kiệt-đà» ch3; Bimbisāra new)
ADHI = "đã dứt khoát hướng tâm rằng cung điện của"        # pāsādaṃ … adhimucci (adhimuccati ch17 «dứt khoát hướng»)
GOLD_Q = f"{PIL} {ADHI} {KING} chính là “vàng”, và nó quả thật đã là vàng"   # "suvaṇṇa"ntveva … suvaṇṇo ca pana āsi
GOLD = f"{PIL} {ADHI} {KING} chính là vàng, và nó quả thật đã là vàng"       # suvaṇṇantveva (no quotes)
CITE_VIN = "[Ba-la-di 621; Đại Phẩm 271]"                 # [pārā. 621; mahāva. 271] (mahāva. «Đại Phẩm» ch2)

# ================================================================ (204) Buddha
T5 = "giữa chư Phật với chư Phật có sự thấp kém và vượt trội"
# atthi buddhānaṃ buddhehi hīnātirekatā (hīna «thấp kém» pi-1, ch10; atireka «vượt trội» new)
XV = "xét về"                                             # -to (ablative of respect)
MPN6 = ["sự thiết lập tỉnh thức", "nỗ lực đúng đắn", "nền tảng thần thông", "năng lực", "sức mạnh",
        "chi phần giác ngộ"]                              # satipaṭṭhāna … bojjhaṅga (ch11 MPN, pi-1)
assert ", ".join(MPN6) in C11.MPN
VASI = "sự làm chủ"                                       # vasibhāva (pi-4 vasībhāva «sự làm chủ»)
SABB = "sự hiểu biết và thấy rõ về sự toàn tri"           # sabbaññutañāṇadassana (pi-4 sabbaññutā «sự toàn tri»;
# vimuttiñāṇadassana «sự hiểu biết và thấy rõ về sự giải thoát» pi-4)

# ================================================================ (205) Sabbadisā
T6 = "chư Phật tồn tại ở tất cả các phương"               # sabbā disā buddhā tiṭṭhanti (tiṭṭhati of a being
# «tồn tại» ch19; aṭṭhakathā: sabbalokadhātūsu ca buddhā atthi)
DIRS = {"e": "phương đông", "s": "phương nam", "w": "phương tây", "n": "phương bắc", "d": "phương dưới",
        "u": "phương trên"}                                # puratthimā … uttarā (pi-2 ^2-644); heṭṭhimā / uparimā disā


def bt(k):
    """X-āya disāya buddho tiṭṭhati"""
    return f"Đức Phật tồn tại ở {DIRS[k]}"


KIN = ("Đức Thế Tôn ấy tên gì, thuộc giai cấp nào, thuộc họ nào, cha mẹ của Đức Thế Tôn ấy tên gì, cặp đệ tử chính "
       "của Đức Thế Tôn ấy tên gì, người thị giả của Đức Thế Tôn ấy tên gì, mặc y phục như thế nào, mang bình bát như "
       "thế nào, ở làng, hay thị trấn, hay thành phố, hay vương quốc, hay xứ sở nào?")
# kinnāmo so bhagavā, kiṃjacco, kiṃgotto, kinnāmā tassa bhagavato mātāpitaro, kinnāmaṃ … sāvakayugaṃ, konāmo …
# upaṭṭhāko, kīdisaṃ cīvaraṃ dhāreti, kīdisaṃ pattaṃ dhāreti, katarasmiṃ gāme vā nigame vā nagare vā raṭṭhe vā
# janapade vā (gotta «họ» ch10 nāmagotta; sāvakayuga «cặp đệ tử chính» ch3; patta «bình bát» pi-2; gāma / nigama /
# nagara / janapada «làng / thị trấn / thành phố / xứ sở» ch5; jacca, upaṭṭhāka, raṭṭha new)
KIN_PE = "Đức Thế Tôn ấy tên gì… hay xứ sở nào?"         # Kinnāmo so bhagavā…pe… janapade vāti?
assert KIN.startswith("Đức Thế Tôn ấy tên gì,") and KIN.endswith("hay xứ sở nào?")
REALMS = [f"cõi {x}" for x in C10.DEVAS[:6]] + ["cõi Phạm Thiên"]
# cātumahārājike … paranimmitavasavattiyā (ch10 DEVAS, pi-2), brahmaloke (brahmaloka «cõi Phạm Thiên» pi-1)
TT = "tồn tại ở"                                          # tiṭṭhati (locative)

# ================================================================ (206) Dhamma / (207) Kamma
NY = "cố định"                                            # niyata (pi-1)
MN, SN = f"{NY} theo hướng sai lầm", f"{NY} theo hướng đúng đắn"   # micchatta- / sammattaniyata (pi-1 ^1-M)
T7 = f"tất cả các hiện tượng đều {NY}"                    # sabbe dhammā niyatā
T8 = f"tất cả các nghiệp đều {NY}"                        # sabbe kammā niyatā
RASI = "nhóm"                                             # rāsi (new; khandha = «khối»)
NO_ANI = f"không có {RASI} không {NY}"                    # natthi aniyato rāsi
ANI = f"có {RASI} không {NY}"                             # atthi aniyato rāsi
R3 = f"{RASI} {MN}, {RASI} {SN}, {RASI} không {NY}"       # micchattaniyato rāsi, sammattaniyato rāsi, aniyato rāsi
TAYO = f"Đức Thế Tôn đã nói đến ba {RASI} – {R3}"         # tayo rāsī vuttā bhagavatā – …
CITE_DS = "[Liệt kê các hiện tượng, ma trận bộ ba 15]"    # [dha. sa. tikamātikā 15] (pi-1 title; Tikamātikā pi-1)


def ny(x, sense):
    """X X-ṭṭhena niyata (kenaṭṭhena «theo nghĩa …» ch3, ch25)"""
    return f"{x} {NY} theo nghĩa {sense}"


R_NY, V_NY = ny(RUPA, RUPA), ny(VINNANA, VINNANA)         # rūpaṃ rūpaṭṭhena niyataṃ / viññāṇaṃ viññāṇaṭṭhena …
VSS = f"{VEDANA}… {SANNA}… {SANKHARA}"                    # vedanā…pe… saññā…pe… saṅkhārā…pe…
TR_ = "trở thành"                                         # hoti / honti (sample «… rồi trở thành Y»)
DD = "được cảm nhận ngay trong đời này"                   # diṭṭhadhammavedanīya (diṭṭhe va dhamme «ngay trong đời
# này» pi-4; vedanīya «được cảm nhận» ch15)
UPV = "được cảm nhận khi tái sinh"                        # upapajjavedanīya (upapajjati «tái sinh» coordinator)
APV = "được cảm nhận trong các đời kế tiếp"               # aparāpariyavedanīya (ch21 aparāpariyavepakka «chín muồi
# trong các đời kế tiếp»)
K_DD, K_UP, K_AP = f"nghiệp {DD}", f"nghiệp {UPV}", f"nghiệp {APV}"
DD_NY, AP_NY = ny(K_DD, DD), ny(K_AP, APV)

# ================================================================ uddāna
UDD = f"{cap(T1)}, {T1B}, {T1C}, {T2}, {T3}, {T4}, {T5}, {T6}, {T7}, {T8}."
# Sāsanaṃ navaṃ kataṃ atthi koci … karoti labbhā … kātuṃ [no commas: rendered as meant], puthujjano … avivitto,
# atthi kiñci saṃyojanaṃ appahāya arahattappatti, atthi adhippāyiddhi [= adhippāyaiddhi] buddhānaṃ vā sāvakānaṃ vā,
# atthi buddhānaṃ buddhehi hīnātirekatā, sabbā disā buddhā tiṭṭhanti, sabbe dhammā niyatā, sabbe kammā niyatāti.


def build():
    d = B.Doc()
    d.head(3, VAGGA21, "5-29-0")
    # ------------------------------------------------------------ (200) Sāsana
    d.head(4, f"(200) 1. {K(x=KX[1])}", "5-29-1-0")
    d.seg("5-878",
          f"{Q(T1)} {AM} {Q(f'{DEV6[0]} {KATA}')} {NHP} {q(T1)} {AM} Có phải {DEV6_PE} {KATA} không? {NHP} "
          f"{q(kata(AKU, KU))} {NHP} {q(kata(OBJ_LONG, ASK))} {NHP}",
          f"{Q(T1B)} {AM} {Q(f'{KAROTI} {DEV6[0]}')} {NHP} có phải {KAROTI} {DEV6_PE} không? {NHP} "
          f"{q(kar(AKU, KU))} {NHP} {q(kar(OBJ_PE, ASK))} {NHP}",
          f"{Q(T1C)} {AM} {Q(f'{KATUM} {DEV6[0]}')} {NHP} có phải {KATUM} {DEV6_PE} không? {NHP} "
          f"{q(katum(AKU, KU))} {NHP} {q(katum(OBJ_PE, ASK))} {NHP}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (201) Avivitta
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-879",
          f"{Q(T2)} {AM} {Q(AV_CHAIN)} {NHP}",
          f"{Q(T2K)} {AM} Có phải {khane(CIV)} {UV} {JH[0]}… {UV} {AKA} không? {NHP} "
          f"có phải {khane(f'{PIN}… {DETI} {SEN}… {DETI} {GIL}')} {UV} {JH[3]}… {UV} {NS_A} không? {NHP}")
    d.seg("5-880",
          f"{NVQ(T2K)} {AM} {Q(PARI)} {NH} Vậy thì {T2K}…",
          E(x=KX[2]))
    # ------------------------------------------------------------ (202) Saṃyojana
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-881",
          f"{Q(T3)} {AM} {Q(SAM_CHAIN)} {NHP}",
          f"{Q(T3)} {AM} {Q(f'{AR} {SA_ALL}')} {NHP} {nanu_l(f'{AR} {NI_ALL}')} {AM} "
          f"{hanci_no(f'{AR} {NI_PE}', T3)}")
    d.seg("5-882",
          f"{NVQ(T3)} {AM} {Q(BV)} {NH} {TENA_HI(T3)}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (203) Iddhi
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-883",
          f"{Q(T4)} {AM} “{cap(MONG)} {CAY} luôn có lá” – {q(T4)} {NHP} {MONG} {CAY} luôn có hoa… {MONG} {CAY} "
          f"luôn có quả… {MONG} luôn có ánh trăng… {MONG} luôn an ổn… {MONG} luôn no đủ… “{MONG} luôn an lành "
          f"[{VAR} (Syā.): suvuṭṭhikaṃ]” – {q(T4)} {NHP}",
          f"{Q(T4)} {AM} “{cap(MONG)} sự tiếp xúc {UPP} {NZ}” – {q(T4)} {NHP}",
          f"{cap(MONG)} {VEDANA} {UPP}… {'… '.join(L10[2:])} {NZ} – {q(T4)} {NHP}",
          f"{Q(T4)} {AM} “{cap(MONG)} {RUPA} {NICCA}” – có phải {T4_PE}… {VSS}… “{MONG} {VINNANA} {NICCA}” – "
          f"{q(T4)} {NHP}",
          f"{Q(T4)} {AM} “{cap(MONG)} {st(0)}” có phải có… “{MONG} {st(1)}”… “{MONG} {st(2)}”… "
          f"“{MONG} {st(3)}” – {q(T4)} {NHP}")
    d.seg("5-884",
          f"{NVQ(T4)} {AM} Chẳng phải {GOLD_Q} {CITE_VIN} sao? {AM} Nếu {GOLD}, {TENA_VATA} “{T4}”.",
          E(x=KX[4]))
    # ------------------------------------------------------------ (204) Buddha
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    d.seg("5-885",
          f"{Q(T5)} {AM} {Q(f'{XV} {MPN6[0]}')} {NHP} có phải {'… '.join(f'{XV} {x}' for x in MPN6[1:])}… "
          f"{XV} {VASI}… {XV} {SABB} không? {NHP}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (205) Sabbadisā
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    d.seg("5-886",
          f"{Q(T6)} {AM} {Q(bt('e'))} {NHP} {q(bt('e'))} {AM} {KIN} {NHP}",
          f"Có phải Đức Phật {TT} {DIRS['s']}… ở {DIRS['w']}… ở {DIRS['n']}… ở {DIRS['d']} không? {NHP} "
          f"{q(bt('d'))} {AM} {KIN_PE} {NHP}",
          f"{Q(bt('u'))} {NHP} {Q(bt('u'))} {AM} Có phải {'… '.join(f'{TT} {x}' for x in REALMS)} không? {NHP}",
          E(x=KX[6]))
    # ------------------------------------------------------------ (206) Dhamma
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    d.seg("5-887",
          f"{Q(T7)} {AM} {Q(MN)} {NHP} {q(SN)} {NHP} {q(NO_ANI)} {NHP} {nanu_l(ANI)} {AM} {hanci_no(ANI, T7)}",
          f"{Q(T7)} {AM} Chẳng phải {TAYO} {CITE_DS} sao? {AM} {hanci_no(TAYO, T7)}",
          f"{Q(R_NY)} {AM} {Q(MN)} {NHP} {q(SN)} {NHP} có phải {VSS}… {V_NY} không? {AM} {Q(MN)} {NHP} "
          f"{q(SN)} {NHP}")
    d.seg("5-888",
          f"Có phải không nên nói – {R_NY}… {VSS}… {V_NY} không? {AM} "
          f"Có phải {RUPA} {TR_} {VEDANA}… {TR_} {SANNA}… {TR_} {SANKHARA}… {TR_} {VINNANA}… {VSS}… "
          f"{VINNANA} {TR_} {RUPA}… {TR_} {VEDANA}… {TR_} {SANNA}… {TR_} {SANKHARA} không? {NH} "
          f"Vậy thì {R_NY}, {VSS}… {V_NY}.",
          E(x=KX[7]))
    # ------------------------------------------------------------ (207) Kamma
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    d.seg("5-889",
          f"{Q(T8)} {AM} {Q(MN)} {NHP} {q(SN)} {NHP} {q(NO_ANI)} {NHP} {nanu_l(ANI)} {AM} {hanci_no(ANI, T8)}",
          f"{Q(T8)} {AM} Chẳng phải {TAYO} sao? {AM} {hanci_no(TAYO, T8)}")
    d.seg("5-890",
          f"{Q(DD_NY)} {AM} {Q(MN)} {NHP} {q(SN)} {NHP} Có phải {K_UP}… {AP_NY} không? {AM} {Q(MN)} {NHP} "
          f"{q(SN)} {NHP}")
    d.seg("5-891",
          f"Có phải không nên nói – {DD_NY}, {K_UP}… {AP_NY} không? {AM} "
          f"Có phải {K_DD} {TR_} {UPV}, {TR_} {APV}… {K_UP} {TR_} {DD}, {TR_} {APV}… "
          f"{K_AP} {TR_} {DD}, {TR_} {UPV} không? {NH} Vậy thì {DD_NY}, {K_UP}… {AP_NY}.",
          E(x=KX[8]),
          f"{VAGGA21}.",
          TASSUDDANAM,
          UDD)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("Như Lai", 2), ("giáo huấn", 2), ("tách khỏi các dục lạc", 1), ("chứng nhập và an trú tầng thiền thứ nhất", 1),
    ("chư Phật và các đệ tử của Đức Phật", 2), ("sự gièm pha", 2), ("sự ganh đua", 2), ("sự tuyệt vọng", 2),
    ("Ma trận bộ ba", 1), ("Các hiện tượng cố định theo hướng sai lầm", 1),
    ("Các hiện tượng cố định theo hướng đúng đắn", 1), ("phương đông", 2), ("phương tây", 2), ("phương bắc", 2),
    ("phương nam", 2), ("chư thiên Tứ Đại Thiên Vương", 2), ("cõi Phạm Thiên", 1), ("sự toàn tri", 4),
    ("sự làm chủ", 4), ("sự hiểu biết và thấy rõ về sự giải thoát", 4), ("bình bát", 2), ("y phục", 2),
    ("là đối tượng của ô nhiễm", 1), ("là đối tượng của phiền não", 1), ("ngay trong đời này", 4),
    ("sự đạt đến", 2), ("thần thông", 1), ("cõi hình sắc", 1), ("cõi không hình sắc", 1), ("thấp kém", 1),
    ("đã sinh khởi", 1), ("lĩnh vực không gian vô tận", 2), (NS_A, 1), ("tầng thiền thứ tư", 1),
    ("Liệt kê các hiện tượng", 3), ("hiểu biết trọn vẹn", 2), ("có bản chất phải", 2), ("người phàm phu", 1),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    *[(x, "2-parihanikatha.md") for x in DEV6], (", ".join(MPN6), "11-tatiyavaggo.md"),
    (", ".join(OBJ[1:8]), "11-tatiyavaggo.md"), (OBJ_PE, "11-tatiyavaggo.md"), (ASK, "4-jahatikatha.md"),
    (C2.SK, "2-parihanikatha.md"), (C2.SB, "2-parihanikatha.md"), (C2.AO, "2-parihanikatha.md"),
    ("chưa dứt bỏ xiềng xích", "12-catutthavaggo.md"), ("có tham đắm", "5-sabbamatthitikatha.md"),
    ("có kiêu mạn", "5-sabbamatthitikatha.md"), ("có tuyệt vọng", "5-sabbamatthitikatha.md"),
    ("không có phiền não", "19-ekadasamavaggo.md"), ("phạm vi", "11-tatiyavaggo.md"),
    (f"sự tiếp xúc {UPP} {NZ}", "19-ekadasamavaggo.md"), (f"{RUPA} {NICCA}", "19-ekadasamavaggo.md"),
    (st(0), "19-ekadasamavaggo.md"), (st(1), "19-ekadasamavaggo.md"), (st(3), "19-ekadasamavaggo.md"),
    (f"{VEDANA} {UPP}… {SANNA} {UPP}… chủ ý {UPP}", "19-ekadasamavaggo.md"),
    ("tôn giả", "5-sabbamatthitikatha.md"), ("Đại Phẩm", "2-parihanikatha.md"),
    ("xứ Ma-kiệt-đà", "3-brahmacariyakatha.md"), ("Seniya", "1-puggalakatha.md"), ("Vác-cha", "12-catutthavaggo.md"),
    ("dứt khoát hướng", "17-navamavaggo.md"), (UV, "10-dutiyavaggo.md"), (AKA, "14-chatthavaggo.md"),
    (NS_A, "11-tatiyavaggo.md"), (C10.REQ, "10-dutiyavaggo.md"), (JH[3], "10-dutiyavaggo.md"),
    ("Theo nghĩa vô thường.", "25-sattarasamavaggo.md"), ("cặp đệ tử chính", "3-brahmacariyakatha.md"),
    ("tên và họ", "10-dutiyavaggo.md"), ("làng", "5-sabbamatthitikatha.md"), ("thị trấn", "5-sabbamatthitikatha.md"),
    ("thành phố", "5-sabbamatthitikatha.md"), ("xứ sở", "5-sabbamatthitikatha.md"),
    (TASSUDDANAM, "10-dutiyavaggo.md"), ("Bàn về nghiệp", "20-dvadasamavaggo.md"),
    (f"người {MN}", "21-terasamavaggo.md"), (f"người {SN}", "21-terasamavaggo.md"),
    ("chín muồi trong các đời kế tiếp", "21-terasamavaggo.md"), ("được cảm nhận là dễ chịu", "15-sattamavaggo.md"),
    ("Như Lai", "14-chatthavaggo.md"), ("khoảnh khắc", "23-pannarasamavaggo.md"), ("ai đó", "1-puggalakatha.md"),
    ("trước đó tu tập", "21-terasamavaggo.md"), ("rồi sau đó", "21-terasamavaggo.md"),
    ("đệ tử", "11-tatiyavaggo.md"), ("cây", "15-sattamavaggo.md"), ("sự thấp kém và ưu việt", "10-dutiyavaggo.md"),
    (f"{UPAGA} lĩnh vực", "14-chatthavaggo.md"), ("đã được người ấy hiểu biết trọn vẹn", "2-parihanikatha.md"),
    ("Có phải có thể", "12-catutthavaggo.md"),
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
    print(f"ch29 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
