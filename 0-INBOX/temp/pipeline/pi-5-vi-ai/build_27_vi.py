# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 27: 27-ekunavisatimavaggo.md (Ekūnavīsatimavaggo,
^5-27-0 … ^5-856), the eight kathā (186)-(193) of the nineteenth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_2 / 4 / 5 / 10 / 11 / 12 / 13 / 14 / 15 / 21 / 24 (read-only; importing writes nothing) for strings
shared with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4 Vietnamese
rails is asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur in that
chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the
Pāli. Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_27_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (vicikicchā «sự hoài nghi»)
import build_4_vi as C4      # noqa: E402  (magga names, niyyāniko … asaṃkilesiyo, Katamena maggenāti?)
import build_5_vi as C5      # noqa: E402  (quá khứ / tương lai / hiện tại, anicco…pe… vipariṇāmadhammo)
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –, KILLERS)
import build_11_vi as C11    # noqa: E402  (dvinnaṃ … cittānaṃ samodhānaṃ, suññatā / animitta / appaṇihita nouns)
import build_12_vi as C12    # noqa: E402  (arahattamagga / -phala, sāmaññaphala, L10 list)
import build_13_vi as C13    # noqa: E402  (niyato «người cố định»)
import build_14_vi as C14    # noqa: E402  (asaṅkhata frame, nibbānaṃ tāṇaṃ …, dve tāṇāni…pe… antarikā vā)
import build_15_vi as C15    # noqa: E402  (hanci_no, nanu_l)
import build_21_vi as C21    # noqa: E402  (ratto rāgaṃ jahati …, rāgo cittasampayutto …, suvidūra sutta unit)
import build_24_vi as C24    # noqa: E402  (Sārammaṇā, atthi tāya …; alobho kusalo sārammaṇo …; nv)

NAME = "27-ekunavisatimavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, ATTHEVA, NANU_VUTTAM, VUTTAM = (B.NA_VATTABBAM_Q, B.TENA_HI, B.ATTHEVA, B.NANU_VUTTAM, B.VUTTAM)
NO_CA_VATA = B.NO_CA_VATA
VAR = B.VAR
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA19 = B.VAGGA[19]                                     # Ekūnavīsatimavaggo = «Chương thứ mười chín» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
hanci_no, nanu_l = C15.hanci_no, C15.nanu_l               # Hañci P, no ca vata re vattabbe – "Q"ti. / …pe… nanu Xti?
nv = C24.nv                                               # X na vattabbaṃ – "Y"ti? (ch15 / ch24)

# ================================================================ kathā names (headings and closing lines)
KX = {1: "sự dứt bỏ phiền não",                           # Kilesajahanakathā (terms file)
      2: "sự trống rỗng",                                 # Suññatākathā (suññatā pi-1, ch11)
      3: "thành quả của đời sống sa-môn",                 # Sāmaññaphalakathā (pi-1, ch4, ch12)
      4: "sự đạt đến",                                    # Pattikathā (patti «sự đạt đến» pi-2 ^2-570)
      5: "tính đúng như thật",                            # Tathatākathā (tathatā ch14)
      6: "điều thiện",                                    # Kusalakathā (kusala core)
      7: "sự cố định hoàn toàn",                          # Accantaniyāmakathā (niyāma ch13 / ch14; accantaṃ ch4)
      8: "các năng lực"}                                  # Indriyakathā (indriya core; ch11 «các năng lực của …»)


def heads(n):
    """#### Ekūnavīsatimavaggo ^5-27-n-0 / ##### (185+n) n. <title> ^5-27-n-1-0"""
    return [(4, VAGGA19, f"5-27-{n}-0"), (5, f"({185 + n}) {n}. {K(x=KX[n])}", f"5-27-{n}-1-0")]


# ================================================================ (186) Kilesajahana
J = C4.JAHATI                                             # jahati «dứt bỏ» (ch4)
T_ = C5.T                                                 # quá khứ / tương lai / hiện tại (ch5)
KIL = "các phiền não"                                     # kilese (kilesa «phiền não» pi-1, ch21)


def jk(t):
    """atīte / anāgate / paccuppanne kilese jahati (atītaṃ rūpaṃ «vật chất thuộc quá khứ» ch5)"""
    return f"{J} {KIL} thuộc {T_[t]}"


JA, JF, JP = jk("a"), jk("f"), jk("p")
PAST_V = ("làm chấm dứt điều đã chấm dứt, làm mất đi điều đã mất đi, làm diệt tận điều đã bị diệt tận, làm biến "
          "mất điều đã biến mất, làm biến mất hoàn toàn điều đã biến mất hoàn toàn")
# Niruddhaṃ nirodheti, vigataṃ vigameti, khīṇaṃ khepeti, atthaṅgataṃ atthaṅgameti, abbhatthaṅgataṃ abbhatthaṅgameti
# (niruddha / vigata / atthaṅgata / abbhatthaṅgata ch5 (pi-2); khīṇa «đã bị diệt tận» ch4)
FUT_V = ("làm cho điều chưa sinh ra không sinh ra, làm cho điều chưa sinh thành không sinh thành, làm cho điều chưa "
         "phát sinh không phát sinh, làm cho điều chưa hiện ra không hiện ra")
# Ajātaṃ ajaneti, asañjātaṃ asañjaneti, anibbattaṃ anibbatteti, apātubhūtaṃ apātubhāveti (the verbs carry the
# negative prefix: as written; ajāta … apātubhūta «chưa sinh ra … chưa hiện ra» ch5 / ch7 (pi-1, pi-2))
A_NIR, A_NAT = f"{T_['a']} đã chấm dứt", f"{T_['a']} không {C5.ATTHI}"   # atītaṃ niruddhaṃ / natthi
F_AJA, F_NAT = f"{T_['f']} chưa sinh ra", f"{T_['f']} không {C5.ATTHI}"
assert A_NAT == "quá khứ không tồn tại"
RAT, INS = C21.RAT, C21.INS                               # ratto rāgaṃ jahati … / rāgena rāgaṃ jahati … (ch21)
CSP = C21.CSP                                             # cittasampayutta «gắn liền với tâm» (pi-1, ch21)
TWO_C = C11.TWO.replace("hai sự tiếp xúc, ", "")          # dvinnaṃ cittānaṃ samodhānaṃ hoti (ch11 TWO, citta only)
assert TWO_C == "có sự tụ hợp của hai tâm"
KSD_A = C21.KSD_A                                         # kusalākusalā … sammukhībhāvaṃ āgacchanti (pi-4, ch15)
FAR_UNIT = C21.far_unit(C21.KSD_A, C21.KSD_S)             # = ch21 ^5-666 line (identical Pāli)
ALL3 = f"{JA}, {JF}, {JP}"                                # atīte … anāgate … paccuppanne kilese jahati
NO_J = f"không có việc {J} {KIL}"                         # natthi kilese jahati (aṭṭhakathā: natthi kilesapajahanā)

# ================================================================ (187) Suññatā
SUN = C11.SUN                                             # suññatā «sự trống rỗng» (pi-1, ch11)
ANI = "cái không có dấu hiệu"                             # animittaṃ (ch11 «lấy cái không có dấu hiệu làm đối tượng»)
APN = C11.APN                                             # appaṇihito «cái không mong cầu» (ch11)
KH = {"r": "khối vật chất", "v": "khối cảm giác", "s": "khối tri giác", "k": "khối tạo tác", "w": "khối thức"}
# rūpa- … viññāṇakkhandha (pi-2 ^2-1)
IN = "nằm trong"                                          # -pariyāpanna (pi-2 kāmadhātupariyāpanna, ch24)


def inn(k):
    return f"{IN} {KH[k]}"


T2 = f"{SUN} {inn('k')}"                                  # suññatā saṅkhārakkhandhapariyāpannā


def sk(k):
    """X-kkhandhassa suññatā"""
    return f"{SUN} của {KH[k]}"


NEG_ANICCA = ", ".join(f"không {x}" for x in B.ANICCA.split(", "))
# na anicco na saṅkhato … na vipariṇāmadhammo
assert NEG_ANICCA.startswith("không vô thường, không do điều kiện tạo thành, không sinh khởi")
SUNNAM = "Này các tỳ-khưu, các tạo tác này trống rỗng tự ngã hay những gì thuộc về tự ngã"
# suññamidaṃ, bhikkhave, saṅkhārā attena vā attaniyena vā (sample ^5 ATT «tự ngã hay những gì thuộc về tự ngã»)
CITE_ANE = "[Trung Bộ Kinh 3.69, trong Kinh Thích Hợp Với Sự Bất Động]"   # [ma. ni. 3.69 āneñjasappāye] (ch24 pattern)

# ================================================================ (188)-(190) asaṅkhata kathā (ch14 frame)
a, s, NIB = C14.a, C14.s, C14.NIB                         # X asaṅkhata / saṅkhata, Niết-bàn
REFUGE = C14.REFUGE                                       # nibbānaṃ tāṇaṃ leṇaṃ … accutaṃ amataṃ (ch10, ch14)
REF_PE1 = f"là {NIB}… điều bất tử"                        # nibbānaṃ…pe… amataṃ
REF_PE2 = f"là {NIB}… điều bất biến, điều bất tử"         # nibbānaṃ…pe… accutaṃ amataṃ
assert REFUGE.startswith(f"là {NIB}, ") and REFUGE.endswith("điều bất biến, điều bất tử")
n_ask, refuges_pe, two_close = C14.n_ask, C14.refuges_pe, C14.two_close
SP = C12.SAMANNA                                          # sāmaññaphala «thành quả của đời sống sa-môn»
SM = "đời sống sa-môn"                                    # sāmañña (ch15)
MG_SO, MG_SA, MG_AN, MG_AR = C4.SOTAPATTIMAGGA, C4.SAKADAGAMIMAGGA, C4.ANAGAMIMAGGA, C12.MG_AR
FR_SO, FR_SA, FR_AN, FR_AR = C12.FR_SO, C12.FR_SA, C12.FR_AN, C12.FR_AR
PA = "sự đạt đến"                                         # patti (pi-2 ^2-570)


def pa(x):
    return f"{PA} {x}"                                    # X-assa patti


CIV, PIN, SEN, GIL = "y phục", "đồ ăn khất thực", "chỗ ở", "thuốc men và vật dụng chữa bệnh"
assert C10.REQ == f"{CIV}, {PIN}, {SEN}, {GIL}"           # cīvara … gilānapaccayabhesajjaparikkhāra (pi-2, ch10)
JH = C10.J                                                # tầng thiền thứ nhất … thứ tư (pi-1)
AKA = C14.AKA                                             # ākāsānañcāyatana (pi-2, ch14)
VIN_A = "lĩnh vực thức vô tận"                            # viññāṇañcāyatana (pi-1 ^1-266)
AKI_A = "lĩnh vực không có gì cả"                         # ākiñcaññāyatana (pi-1 ^1-267)
NS_A = C11.NS                                             # nevasaññānāsaññāyatana (pi-1, ch11)
VITTH = "(tất cả nên được trình bày chi tiết như vậy)"    # (evaṃ sabbaṃ vitthāretabbaṃ) (pi-2 vitthāretabbā)
FIVE_KH = f"{B.RUPA}… {B.VEDANA}… {B.SANNA}… {B.SANKHARA}… {B.VINNANA}"   # rūpaṃ … vedanā… … viññāṇaṃ
T5 = "tính đúng như thật của tất cả các hiện tượng"       # sabbadhammānaṃ tathatā (ch14 tathatā; ch8 «tất cả các hiện tượng»)
TA = [("vật chất", "vật chất"), ("cảm giác", "cảm giác"), ("tri giác", "tri giác"), ("tạo tác", "các tạo tác"),
      ("thức", "thức")]                                   # rūpatā / vedanatā / saññatā / saṅkhāratā / viññāṇatā


def ta(i):
    """rūpatā = «tính chất vật chất»"""
    return f"tính chất {TA[i][0]}"


def rt(i):
    """rūpassa rūpatā = «tính chất vật chất của vật chất»"""
    return f"{ta(i)} của {TA[i][1]}"


# ================================================================ (191) Kusala
NBD = "yếu tố Niết-bàn"                                   # nibbānadhātu (dhātu «yếu tố» core)
TH, SAR, ANAR = C24.TH, C24.SAR, C24.ANAR                 # kusala «là thiện»; sārammaṇa / anārammaṇa (ch15, ch24)
ATT_P, ATT_N = C24.ATT_P, C24.ATT_N                       # atthi / natthi tāya āvaṭṭanā…pe… paṇidhi (ch15)
AL, AD, AMO, KU_ALL = C24.AL, C24.AD, C24.AMO, C24.KU_ALL
sa, an = C24.sa, C24.an
T6 = f"{NBD} {TH}"                                        # nibbānadhātu kusalā
KU_CHAIN = f"{AD} {TH}… {AMO} {TH}… {chain(KU_ALL[2:-1])}… {KU_ALL[-1]} {TH}, {SAR}, {ATT_P}"   # (= ch24 ^5-761)
KU_CHAIN_N = f"{AD} {TH}… {AMO} {TH}… {chain(KU_ALL[2:-1])}… {KU_ALL[-1]} {TH}, {ANAR}, {ATT_N}"
ANAV = f"{NBD} không có lỗi"                              # nibbānadhātu anavajjā (anavajja «không có lỗi» pi-4)

# ================================================================ (192) Accantaniyāma
PU = C4.PUTHUJJANA                                        # puthujjano «người phàm phu»
T7 = f"{PU} có tính cố định hoàn toàn"                    # atthi puthujjanassa accantaniyāmatā
CN = "cố định hoàn toàn"                                  # accantaniyato (niyata «cố định» pi-1, ch13; accantaṃ ch4)
ACC = f"{C13.NI_P} hoàn toàn"                             # accantaniyato puggalo
assert ACC == f"người {CN}"
FOR_ACC = f"đối với {ACC}"                                # accantaniyatassa puggalassa (ch11 FOR8 «đối với …»)
KILL = C10.KILLERS                                        # mātughātako … saṅghabhedako (ch3 / ch10)
VIC = C2.VI                                               # vicikicchā «sự hoài nghi»
SD, UD = "quan điểm về sự trường tồn", "quan điểm về sự đoạn diệt"   # sassata- / ucchedadiṭṭhi (pi-1 ^1-1322)
FOR_SD, FOR_UD = f"đối với người cố định vào {SD}", f"đối với người cố định vào {UD}"
# sassatadiṭṭhiyā / ucchedadiṭṭhiyā niyatassa puggalassa
UPJ, NUPJ = "có thể sinh khởi", "không thể sinh khởi"     # uppajjeyya / nuppajjeyya
PAH = "đã được dứt bỏ"                                    # pahīnā (ch2, ch11)
KATAMENA = C4.KATAMENA                                    # Katamena maggenāti? «Bằng con đường nào?» (ch4)
AKM = "con đường bất thiện"                               # akusalo maggo
BY_AKM = f"Bằng {AKM}."                                   # Akusalena maggena(ti). (ch4 «Bằng con đường …»)
POS = C4.POS
NEG = C4.NEG
AK_POS = f"{', '.join(POS[:3])}, {POS[4]}… {POS[-1]}"     # niyyāniko khayagāmī bodhagāmī anāsavo…pe… asaṃkilesiko
AK_NEG = f"{NEG[0]}… {C4.NEG_LAST}"                       # aniyyāniko…pe… saṃkilesiko


def by4():
    """Sotāpattimaggenāti? Na hevaṃ vattabbe…pe… sakadāgāmimaggena…pe… anāgāmimaggena…pe… arahattamaggenāti? …"""
    return (f"{Q(f'bằng {MG_SO}')} {NHP} có phải bằng {MG_SA}… bằng {MG_AN}… bằng {MG_AR} không? {NHP}")


def pahina_line(who, x):
    """X nuppajjeyyāti? Āmantā. Pahīnāti? … arahattamaggenāti? Na hevaṃ vattabbe…pe…."""
    return (f"Có phải {who}, {x} {NUPJ} không? {AM} {Q(PAH)} {NHP} {q(PAH)} {AM} {by4()}")


def gone(who, x):
    """who, x akusalena maggena pahīnā"""
    return f"{who}, {x} {PAH} bằng {AKM}"


SUTTA_1 = "Này các tỳ-khưu, ở đời này, có người mang các hiện tượng bất thiện hoàn toàn đen tối, người ấy{v} một lần chìm thì chìm luôn"
# idha, bhikkhave, ekacco puggalo samannāgato hoti ekantakāḷakehi akusalehi dhammehi, so … sakiṃ nimuggo nimuggova
# hoti (pi-4 ^4 sattaka «Ở đời này, có người mang các hiện tượng bất thiện hoàn toàn đen tối»; «người một lần chìm
# thì chìm luôn»; ch15 «Ở đời này, có người»)
S1V = SUTTA_1.format(v=f" [{VAR} (Tăng Chi Bộ Kinh 7.15): evaṃ kho bhikkhave puggalo]")
S1 = SUTTA_1.format(v="")
S2 = "Này các tỳ-khưu, ở đời này, có người trồi lên rồi lại chìm"   # … ummujjitvā nimujjati (pi-4)
S3 = ("Này các tỳ-khưu, ở đời này, có người trồi lên rồi đứng yên, trồi lên rồi nhìn thấy rõ, nhìn quanh, trồi lên "
      "rồi bơi qua, trồi lên rồi đạt đến chỗ chân chạm đáy")
# … ummujjitvā ṭhito hoti, ummujjitvā vipassati viloketi, ummujjitvā patarati, ummujjitvā patigādhappatto hoti (pi-4)
CITE_AN = "[Tăng Chi Bộ Kinh 7.15]"                       # [a. ni. 7.15]
ALL_T = "vào mọi lúc đều"                                 # sabbakālaṃ (sabbadā «vào mọi lúc» sample)

# ================================================================ (193) Indriya
LK, LT = "thuộc thế gian", "vượt thế gian"                # lokiya / lokuttara (pi-1, ch10)
F = {"sa": "niềm tin", "vi": C12.L10[6], "st": C12.L10[7], "sm": C12.L10[8], "pa": C12.L10[9],
     "mn": C11.MANO[0], "so": C11.SOMA[0], "ji": C11.JIVI[0]}
# saddhā / vīriyaṃ / sati / samādhi / paññā (ch12 L10) ; mano / somanassaṃ / jīvitaṃ (ch11, pi-1)
I = {"sa": B.INDRIYA[14], "vi": B.INDRIYA[15], "st": B.INDRIYA[16], "sm": B.INDRIYA[17], "pa": B.INDRIYA[18],
     "mn": C11.MANO[1], "so": C11.SOMA[1], "ji": C11.JIVI[1]}
# saddhindriya … paññindriya (pi-2), manindriya / somanassindriya / jīvitindriya (ch11)
assert F["sa"] == C12.L10[5] and I["mn"] == B.INDRIYA[5] and I["ji"] == B.INDRIYA[6]


def lk(x, w=LK):
    return f"{x} {w}"


def pr(k, neg=False, w=LK):
    """atthi lokiyā saddhā, atthi / natthi lokiyaṃ saddhindriyaṃ"""
    return f"có {lk(F[k], w)}, {'không có' if neg else 'có'} {lk(I[k], w)}"


FIVE = C11.FIVE                                           # pañcindriyāni «năm năng lực»
T8 = f"không có {lk(FIVE)}"                               # natthi lokiyāni pañcindriyāni
BUDDHA = ("Này các tỳ-khưu, khi quan sát thế gian bằng con mắt của Đức Phật, Ta đã thấy các chúng sinh có ít bụi "
          "trong mắt, có nhiều bụi trong mắt, có các năng lực sắc bén, có các năng lực non yếu, có phẩm chất tốt, dễ "
          "hướng dẫn, một số sống thấy sự đáng sợ của thế gian khác và của lỗi lầm")
# addasaṃ kho ahaṃ, bhikkhave, buddhacakkhunā lokaṃ volokento satte apparajakkhe mahārajakkhe, tikkhindriye
# mudindriye, svākāre, suviññāpaye, appekacce paralokavajjabhayadassāvino viharante (pi-2 ^2-814 words; paraloka
# «thế gian khác» sample; vajja «lỗi» pi-4; aṭṭhakathā of the sutta: paralokañca vajjañca bhayato passanti)
CITE_MN = "[Trung Bộ Kinh 1.283; ở đó cũng thấy các từ như “dvākāre duviññāpaye”]"
# [ma. ni. 1.283 tattha "dvākāre duviññāpaye" iccādīnipi padāni dissanti]

# ================================================================ uddāna
UDD = (f"{cap(JA)}, {JF}, {JP}, {T2}, {a(SP)}, {a(PA)}, {a(T5)}, {T6}, {T7}, {T8}.")
# Atīte kilese jahati anāgate kilese jahati paccuppanne kilese jahati [no commas: rendered as meant], suññatā
# saṅkhārakkhandhapariyāpannā, sāmaññaphalaṃ asaṅkhataṃ, patti asaṅkhatā, sabbadhammānaṃ tathatā asaṅkhatā,
# nibbānadhātu kusalā, atthi puthujjanassa accantaniyāmatā, natthi lokiyāni pañcindriyānīti.


def build():
    d = B.Doc()
    d.head(3, VAGGA19, "5-27-0")
    # ------------------------------------------------------------ (186) Kilesajahana
    d.head(4, f"(186) 1. {K(x=KX[1])}", "5-27-1-0")
    d.seg("5-828",
          f"{Q(JA)} {AM} {Q(PAST_V)} {NHP} {q(JA)} {AM} {NANU(A_NIR)} {AM} {hanci_no(A_NIR, JA)} "
          f"{Q(JA)} {AM} {NANU(A_NAT)} {AM} {hanci_no(A_NAT, JA)}")
    d.seg("5-829",
          f"{Q(JF)} {AM} {Q(FUT_V)} {NHP} {q(JF)} {AM} {NANU(F_AJA)} {AM} {hanci_no(F_AJA, JF)} "
          f"{Q(JF)} {AM} {NANU(F_NAT)} {AM} {hanci_no(F_NAT, JF)}")
    d.seg("5-830",
          f"{Q(JP)} {AM} {Q(RAT)} {NHP} {q(INS)} {NHP}",
          f"{Q(f'sự tham đắm {CSP}, con đường {CSP}')} {AM} {Q(TWO_C)} {NHP}",
          f"{Q('sự tham đắm là bất thiện, con đường là thiện')} {AM} {Q(KSD_A)} {NHP}",
          FAR_UNIT)
    d.seg("5-831",
          f"{NVQ(ALL3)} {AM} {Q(NO_J)} {NHP} vậy thì {ALL3}.",
          E(x=KX[1]))
    # ------------------------------------------------------------ (187) Suññatā
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    in_k, in_r, in_w = inn("k"), inn("r"), inn("w")
    kk = KH["k"]
    sk_r, sk_k = sk("r"), sk("k")
    d.seg("5-832",
          f"{Q(T2)} {AM} {Q(f'{ANI} {in_k}')} {NHP} {q(T2)} {AM} {Q(f'{APN} {in_k}')} {NHP} "
          f"{nv(ANI, in_k, False)} {AM} {nv(SUN, in_k)} {NHP} {nv(APN, in_k, False)} {AM} "
          f"{nv(SUN, in_k)} {NHP}",
          f"{Q(T2)} {AM} {Q(f'{kk} {NEG_ANICCA}')} {NHP} {nanu_l(f'{kk} {B.ANICCA}')} {AM} "
          f"{hanci_no(f'{kk} {C5.ANICCA_PE}', T2)}")
    in_vsw = f"{inn('v')}… {inn('s')}… {in_w}"
    d.seg("5-833",
          f"{Q(f'{sk_r} {in_k}')} {AM} {Q(f'{sk_k} {in_r}')} {NHP} "
          f"có phải {SUN} của {KH['v']}… {KH['s']}… {KH['w']} {in_k} không? {AM} "
          f"{Q(f'{sk_k} {in_w}')} {NHP}",
          f"{nv(sk_k, in_r)} {AM} {nv(sk_r, in_k)} {NHP} "
          f"{nv(sk_k, in_vsw, False)} {AM} "
          f"{nv(sk('w'), in_k)} {NHP}")
    d.seg("5-834",
          f"Có phải không nên nói – {T2}” không? {AM} {NANU_VUTTAM} “{SUNNAM}” {CITE_ANE}! {ATTHEVA} {AM} "
          f"{TENA_HI(T2)}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (188) Sāmaññaphala
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-835", f"{Q(a(SP))} {AM} {Q(REFUGE)} {NHP} {two_close(SP)}")
    d.seg("5-836",
          f"{Q(a(SP))} {AM} {Q(a(SM))} {NHP} {q(s(SM))} {AM} {Q(s(SP))} {NHP}",
          f"{Q(a(FR_SO))} {AM} {Q(a(MG_SO))} {NHP} {q(s(MG_SO))} {AM} {Q(s(FR_SO))} {NHP}",
          f"Có phải {FR_SA}… {FR_AN}… {a(FR_AR)} không? {AM} {Q(a(MG_AR))} {NHP} {q(s(MG_AR))} {AM} "
          f"{Q(s(FR_AR))} {NHP}",
          f"Có phải {a(FR_SO)}, {FR_SA}… {FR_AN}… {a(FR_AR)}, {a(NIB)} không? {AM} {Q(n_ask('năm'))} {NHP} "
          f"{q(n_ask('năm'))} {AM} {Q(refuges_pe('năm'))} {NHP}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (189) Patti
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-837", f"{Q(a(PA))} {AM} {Q(REFUGE)} {NHP} {two_close(PA)}")
    d.seg("5-838",
          f"{Q(a(pa(CIV)))} {AM} {Q(REF_PE1)} {NHP} {two_close(pa(CIV))} "
          f"{q(a(pa(f'{PIN}… {SEN}… {GIL}')))} {AM} {Q(REF_PE2)} {NHP} {two_close(pa(GIL))}",
          f"Có phải {a(pa(CIV))}… {PIN}… {SEN}… {a(pa(GIL))}, {a(NIB)} không? {AM} {Q(n_ask('năm'))} {NHP} "
          f"{q(n_ask('năm'))} {AM} {Q(refuges_pe('năm'))} {NHP}")
    seq = [JH[1], JH[2], JH[3], AKA, VIN_A, AKI_A, NS_A, MG_SO, FR_SO, MG_SA, FR_SA, MG_AN, FR_AN, MG_AR]
    d.seg("5-839",
          f"Có phải {a(pa(JH[0]))} {VITTH} {chain(seq)}… {a(pa(FR_AR))} không? {AM} {Q(REF_PE2)} {NHP} "
          f"{two_close(pa(FR_AR))}",
          f"Có phải {chain([a(pa(x)) for x in (MG_SO, FR_SO, MG_AR, FR_AR)])}… {a(NIB)} không? {AM} "
          f"{Q(n_ask('chín'))} {NHP} {q(n_ask('chín'))} {AM} {Q(refuges_pe('chín'))} {NHP}")
    d.seg("5-840",
          f"Có phải không nên nói – {a(PA)} không? {AM} Có phải {PA} là {FIVE_KH} không? {NH} {TENA_HI(a(PA))}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (190) Tathatā
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    d.seg("5-841", f"{Q(a(T5))} {AM} {Q(REF_PE1)} {NHP} {two_close(T5)}")
    d.seg("5-842",
          f"{cap(rt(0))}, chẳng phải {a(ta(0))} sao? {AM} {Q(REF_PE1)} {NHP} "
          f"{rt(0)}, chẳng phải {a(ta(0))}, {a(NIB)} sao? {AM} {Q(n_ask('hai'))} {NHP} {q(n_ask('hai'))} {AM} "
          f"{Q(refuges_pe('hai'))} {NHP}",
          f"{cap(rt(1))}, chẳng phải {ta(1)}… {rt(2)}, chẳng phải {ta(2)}… {rt(3)}, chẳng phải {ta(3)}… "
          f"{rt(4)}, chẳng phải {a(ta(4))} sao? {AM} {Q(REF_PE1)} {NHP}",
          f"{cap(rt(0))}, chẳng phải {ta(0)}… {rt(4)}, chẳng phải {a(ta(4))}, {a(NIB)} sao? {AM} "
          f"{Q(n_ask('sáu'))} {NHP} {q(n_ask('sáu'))} {AM} {Q(refuges_pe('sáu'))} {NHP}")
    d.seg("5-843",
          f"{NVQ(a(T5))} {AM} Có phải {T5} là {FIVE_KH} không? {NH} {TENA_HI(a(T5))}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (191) Kusala
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    d.seg("5-844", C24.first(T6))
    d.seg("5-845",
          f"{Q(sa([AL], TH))} {AM} {Q(sa([NBD], TH))} {NHP} {q(KU_CHAIN)} {AM} {Q(sa([NBD], TH))} {NHP}",
          f"{Q(an([NBD], TH))} {AM} {Q(an([AL], TH))} {NHP} {q(an([NBD], TH))} {AM} {Q(KU_CHAIN_N)} {NHP}")
    d.seg("5-846",
          f"{NVQ(T6)} {AM} {NANU(ANAV)} {AM} {B.hanci(ANAV, T6)}",
          E(x=KX[6]))
    # ------------------------------------------------------------ (192) Accantaniyāma
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    d.seg("5-847",
          f"{Q(T7)} {AM} Có phải {KILL[0]} {CN}, {KILL[1]}… {KILL[2]}… {KILL[3]}… {KILL[4]} {CN} không? {NHP}")
    d.seg("5-848",
          f"{Q(T7)} {AM} Có phải {FOR_ACC}, {VIC} {UPJ} không? {AM} {hanci_no(f'{FOR_ACC}, {VIC} {UPJ}', T7)}",
          pahina_line(FOR_ACC, VIC),
          f"{KATAMENA} {BY_AKM} Có phải {AKM} {AK_POS} không? {NHP} {nanu_l(f'{AKM} {AK_NEG}')} {AM} "
          f"{hanci_no(f'{AKM} {AK_NEG}', gone(FOR_ACC, VIC))}")
    for sid, who, x in (("5-849", FOR_SD, UD), ("5-850", FOR_UD, SD)):
        d.seg(sid,
              f"Có phải {who}, {x} {UPJ} không? {AM} {hanci_no(f'{who}, {x} {UPJ}', T7)}",
              pahina_line(who, x),
              f"{KATAMENA} {BY_AKM} {cap(AKM)}… {NO_CA_VATA} “{gone(who, x)}”.")
    d.seg("5-851",
          f"{NVQ(T7)} {AM} {NANU_VUTTAM} “{S1V}” {CITE_AN}! {ATTHEVA} {AM} {TENA_HI(T7)}")
    d.seg("5-852",
          f"{B.KATVA(f'{VUTTAM} “{S1}”', T7)} {AM} {VUTTAM} “{S2}” {CITE_AN}! {ATTHEVA} {AM} "
          f"Có phải {ALL_T} trồi lên rồi lại chìm không? {NHP}",
          f"Có phải vì cho rằng {VUTTAM} “{S1}” – và vì lý do ấy, {T7} không? {AM} {VUTTAM} “{S3}” {CITE_AN}! "
          f"{ATTHEVA} {AM} Có phải {ALL_T} trồi lên rồi đạt đến chỗ chân chạm đáy không? {NHP}",
          E(x=KX[7]))
    # ------------------------------------------------------------ (193) Indriya
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    isa, fsa, ipa, fpa = lk(I["sa"]), lk(F["sa"]), lk(I["pa"]), lk(F["pa"])
    d.seg("5-853",
          f"{Q(f'không có {isa}')} {AM} {Q(f'không có {fsa}')} {NHP} "
          f"có phải không có {lk(I['vi'])}… {I['st']}… {I['sm']}… {I['pa']} không? {AM} "
          f"{Q(f'không có {fpa}')} {NHP}",
          f"{Q(f'có {fsa}')} {AM} {Q(f'có {isa}')} {NHP} "
          f"có phải có {lk(F['vi'])}… {F['st']}… {F['sm']}… {F['pa']} không? {AM} "
          f"{Q(f'có {ipa}')} {NHP}",
          f"{Q(pr('mn'))} {AM} {Q(pr('sa'))} {NHP} {q(pr('mn'))} {AM} {Q(pr('pa'))} {NHP}",
          f"Có phải {pr('so')}… {pr('ji')} không? {AM} {Q(pr('sa'))} {NHP} {q(pr('ji'))} {AM} {Q(pr('pa'))} {NHP}")
    d.seg("5-854",
          f"{Q(pr('sa', True))} {AM} {Q(pr('mn', True))} {NHP} {q(pr('pa', True))} {AM} {Q(pr('mn', True))} {NHP}",
          f"{Q(pr('sa', True))} {AM} Có phải {pr('so', True)}… {pr('ji', True)} không? {NHP} "
          f"{q(pr('pa', True))} {AM} Có phải {pr('mn', True)}… {pr('ji', True)} không? {NHP}")
    d.seg("5-855",
          f"{Q(pr('sa', w=LT))} {AM} {Q(pr('sa'))} {NHP} có phải có {lk(F['vi'], LT)}… {pr('pa', w=LT)} không? "
          f"{AM} {Q(pr('pa'))} {NHP}",
          f"{Q(pr('sa', True))} {AM} {Q(pr('sa', True, LT))} {NHP} có phải có {lk(F['vi'])}… {pr('pa', True)} "
          f"không? {AM} {Q(pr('pa', True, LT))} {NHP}")
    d.seg("5-856",
          f"{Q(T8)} {AM} {NANU_VUTTAM} “{BUDDHA}” {CITE_MN}! {ATTHEVA} {AM} {TENA_HI(f'có {lk(FIVE)}')}",
          E(x=KX[8]),
          f"{VAGGA19}.",
          TASSUDDANAM,
          UDD)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("lĩnh vực thức vô tận", 1), ("lĩnh vực không có gì cả", 1), (NS_A, 1), (AKA, 1), ("tầng thiền thứ nhất", 1),
    ("sự đạt đến", 2), ("nên được trình bày chi tiết", 2), ("thành quả của đời sống sa-môn", 1),
    ("Ở đời này, có người mang các hiện tượng bất thiện hoàn toàn đen tối", 4),
    ("một lần chìm thì chìm luôn", 4), ("người trồi lên rồi lại chìm", 4), ("người trồi lên rồi đứng yên", 4),
    ("người trồi lên rồi nhìn thấy rõ, nhìn quanh", 4), ("người trồi lên rồi bơi qua", 4),
    ("người trồi lên rồi đạt đến chỗ chân chạm đáy", 4),
    ("có ít bụi trong mắt, có nhiều bụi trong mắt, có các năng lực sắc bén, có các năng lực non yếu, có phẩm chất "
     "tốt", 2), ("dễ hướng dẫn", 2), ("trí tuệ thuộc thế gian", 2), ("trí tuệ vượt thế gian", 2),
    (SD, 1), (UD, 1), ("không có lỗi", 4), ("khối tạo tác", 1), ("khối vật chất, khối cảm giác, khối tri giác, khối "
                                                               "tạo tác, khối thức", 2),
    ("thế gian khác", 1), ("sự hoài nghi", 1), ("năng lực niềm vui", 2),
    ("năng lực sống", 2), ("năng lực ý", 2), ("năng lực niềm tin", 2), ("năng lực trí tuệ", 2), ("phiền não", 1),
    ("nằm trong cõi dục lạc", 2), ("sự trống rỗng", 1), ("không có dấu hiệu", 1), ("không mong cầu", 1),
    ("Niết-bàn", 1), ("Trung Bộ Kinh", 4), ("Tăng Chi Bộ Kinh", 4), ("đã chấm dứt", 2), ("chưa sinh ra", 1),
    ("thuộc thế gian", 1), ("vượt thế gian", 1), ("thuộc quá khứ", 1), ("thuộc tương lai", 1), ("thuộc hiện tại", 1),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (FAR_UNIT, "21-terasamavaggo.md"),
    (f"{Q(RAT)} {NHP} {q(INS)} {NHP}", "21-terasamavaggo.md"),
    (f"{Q(f'sự tham đắm {CSP}, con đường {CSP}')} {AM}", "21-terasamavaggo.md"),
    (f"{q('sự tham đắm là bất thiện, con đường là thiện')} {AM} {Q(KSD_A)} {NHP}", "21-terasamavaggo.md"),
    ("có sự tụ hợp của", "4-jahatikatha.md"), (KATAMENA, "4-jahatikatha.md"), (AK_POS.split("… ")[0][:60],
                                                                              "4-jahatikatha.md"),
    (POS[-1], "4-jahatikatha.md"), (AK_NEG.split("… ")[0], "4-jahatikatha.md"), (C4.NEG_LAST, "4-jahatikatha.md"),
    ("đã bị diệt tận", "4-jahatikatha.md"), ("Bằng con đường không trở lại.", "4-jahatikatha.md"),
    ("đã chấm dứt, đã mất đi", "5-sabbamatthitikatha.md"), ("đã biến mất hoàn toàn", "5-sabbamatthitikatha.md"),
    ("đã biến mất", "5-sabbamatthitikatha.md"), ("chưa sinh ra", "5-sabbamatthitikatha.md"),
    ("chưa sinh thành", "5-sabbamatthitikatha.md"), ("chưa phát sinh", "5-sabbamatthitikatha.md"),
    ("chưa hiện ra", "5-sabbamatthitikatha.md"), ("vật chất thuộc quá khứ", "5-sabbamatthitikatha.md"),
    (C5.ANICCA_PE, "5-sabbamatthitikatha.md"), ("quá khứ không tồn tại", "6-atitakkhandhadikatha.md"),
    (f"{a(NIB)}", "14-chatthavaggo.md"), (REFUGE, "14-chatthavaggo.md"), (two_close("x")[-80:], "14-chatthavaggo.md"),
    (refuges_pe("năm"), "14-chatthavaggo.md"), (n_ask("năm"), "14-chatthavaggo.md"),
    ("tính đúng như thật", "14-chatthavaggo.md"), (AKA, "14-chatthavaggo.md"),
    ("lấy sự trống rỗng làm đối tượng", "11-tatiyavaggo.md"), (f"lấy {ANI} làm đối tượng", "11-tatiyavaggo.md"),
    (APN, "11-tatiyavaggo.md"), (C11.TWO, "11-tatiyavaggo.md"), (NS_A, "11-tatiyavaggo.md"),
    (f"{I['mn']}", "11-tatiyavaggo.md"), (f"{I['so']}", "11-tatiyavaggo.md"), (FIVE, "11-tatiyavaggo.md"),
    ("đối với người thứ tám", "11-tatiyavaggo.md"), (PAH, "11-tatiyavaggo.md"),
    ("bốn niềm tin, bốn sự tinh tấn, bốn sự tỉnh thức, bốn sự định tâm, bốn trí tuệ", "12-catutthavaggo.md"), (SP, "12-catutthavaggo.md"), (FR_AR, "12-catutthavaggo.md"),
    (MG_AR, "12-catutthavaggo.md"), (GIL, "12-catutthavaggo.md"),
    (C10.REQ, "10-dutiyavaggo.md"), (C10.J[0], "10-dutiyavaggo.md"),
    (f"{KILL[0]}… {KILL[1]}… {KILL[2]}… {KILL[3]}", "10-dutiyavaggo.md"), (TASSUDDANAM, "10-dutiyavaggo.md"),
    (f"{LK}", "10-dutiyavaggo.md"), (f"{LT}", "10-dutiyavaggo.md"),
    (C13.NI_P, "13-pancamavaggo.md"), (SM, "15-sattamavaggo.md"), (KSD_A, "15-sattamavaggo.md"),
    ("Có phải đối với", "15-sattamavaggo.md"),
    (KU_CHAIN, "24-solasamavaggo.md"), (sa([AL], TH), "24-solasamavaggo.md"), (an([AL], TH), "24-solasamavaggo.md"),
    (ATT_P, "24-solasamavaggo.md"), (ATT_N, "24-solasamavaggo.md"), (f"Nếu {ANAR}, {ATT_N}, {NO_CA_VATA}",
                                                                    "24-solasamavaggo.md"),
    (", trong Kinh", "24-solasamavaggo.md"), (f"{IN} cõi hình sắc", "24-solasamavaggo.md"),
    ("tự ngã hay những gì thuộc về tự ngã", "1-puggalakatha.md"), ("vào mọi lúc", "1-puggalakatha.md"),
    ("trống rỗng", "1-puggalakatha.md"), ("Có phải vì cho rằng Đức Thế Tôn đã nói – “", "1-puggalakatha.md"),
    ("thế gian khác", "1-puggalakatha.md"), ("người phàm phu", "4-jahatikatha.md"),
    (VIC, "2-parihanikatha.md"),
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
    print(f"ch27 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
