# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 24: 24-solasamavaggo.md (Soḷasamavaggo, ^5-24-0 … ^5-775),
the ten kathā (156)-(165) of the sixteenth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_5_vi / build_10_vi / build_12_vi / build_13_vi / build_15_vi / build_16_vi / build_17_vi
(read-only; importing writes nothing) for strings shared with those chapters, so every repeat is byte-identical.
Every string claimed from the pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a
finished pi-5 chapter is asserted to occur in that chapter's output; the sample's per-line checks (IDs, dashes,
quotes, NFC, foreign letters) are run against the Pāli. Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_24_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_5_vi as C5      # noqa: E402  (quá khứ / tương lai / hiện tại)
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –)
import build_12_vi as C12    # noqa: E402  (phassa … paññā list, dukkhaṃ parijānāti … maggaṃ bhāveti)
import build_13_vi as C13    # noqa: E402  (tena phassena taṃ phassaṃ phusati … list)
import build_15_vi as C15    # noqa: E402  (vedaniya list, āvaṭṭanā…pe… paṇidhi, sahagata …, two contacts, hanci)
import build_16_vi as C16    # noqa: E402  (Sārammaṇaṃ, atthi tassa … first line; kāyakammaṃ vacīkammaṃ …)
import build_17_vi as C17    # noqa: E402  (rūpaṃ sappaccayaṃ)

NAME = "24-solasamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NHP = B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA, ATTHEVA, NANU_VUTTAM = (B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA, B.ATTHEVA,
                                                   B.NANU_VUTTAM)
NO_CA_VATA = B.NO_CA_VATA
VAR = B.VAR
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA16 = B.VAGGA[16]                                     # Soḷasamavaggo = «Chương thứ mười sáu» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
hanci_no, nanu_l = C15.hanci_no, C15.nanu_l               # Hañci P, no ca vata re vattabbe – "Q"ti. / …pe… nanu Xti?

# ================================================================ kathā names (headings and closing lines)
KX = {1: "sự chế ngự",                                    # Niggahakathā (terms file: restraining the mind)
      2: "sự nâng lên",                                   # Paggahakathā (cittaṃ paggaṇhāti «nâng tâm lên» pi-1/pi-2)
      3: "việc trao sự dễ chịu",                          # Sukhānuppadānakathā (sukha as in the frame, sample ^5-179)
      4: "sự chú tâm bằng cách nắm gộp lại",              # Adhigayhamanasikārakathā (manasikāra «sự chú tâm» core)
      5: "việc cho rằng vật chất là gốc rễ",              # Rūpaṃ hetūtikathā (hetu «gốc rễ» pi-1)
      6: "việc cho rằng vật chất có gốc rễ",              # Rūpaṃ sahetukantikathā (sahetuka «có gốc rễ» pi-1)
      7: "việc cho rằng vật chất là thiện và bất thiện",  # Rūpaṃ kusalākusalantikathā
      8: "việc cho rằng vật chất là quả của nghiệp",      # Rūpaṃ vipākotikathā (ch15 / ch20 frame)
      9: "việc cho rằng vật chất thuộc cõi hình sắc và thuộc cõi không hình sắc",
      # Rūpaṃ rūpāvacarārūpāvacarantikathā (rūpāvacara «thuộc cõi hình sắc» pi-1)
      10: "những gì nằm trong cõi hình sắc và cõi không hình sắc"}
# Rūpārūpadhātupariyāpannakathā (kāmadhātupariyāpanna «nằm trong cõi dục lạc» pi-2; «những gì» ch15 Saṅgahita)


def heads(n):
    """#### Soḷasamavaggo ^5-24-n-0 / ##### (155+n) n. <title> ^5-24-n-1-0"""
    return [(4, VAGGA16, f"5-24-{n}-0"), (5, f"({155 + n}) {n}. {K(x=KX[n])}", f"5-24-{n}-1-0")]


# ================================================================ shared words
RU = B.RUPA                                               # rūpaṃ «vật chất» (pi-2)
UPP = "đã sinh khởi"                                      # uppanna (pi-1, ch19)
L10 = C12.L10                                             # phasso vedanā saññā cetanā cittaṃ saddhā vīriyaṃ sati samādhi paññā
AL, AD, AMO = "sự không tham lam", "sự không sân hận", "sự không si mê"   # alobho adoso amoho (pi-1)
LO, DO, MO = "sự tham lam", "sự sân hận", "sự si mê"      # lobho doso moho (pi-1 ^1-1266)
KIL10 = [LO, DO, MO, "sự kiêu mạn", "quan điểm", "sự hoài nghi", "sự uể oải", "sự xao động",
         "sự không biết hổ thẹn", "sự không biết ghê sợ tội lỗi"]
# lobho doso moho māno diṭṭhi vicikicchā thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ (ch2 words; lobha pi-1)
AO = KIL10[-1]
assert KIL10[3:] == [C10.C2.MANA, C10.C2.DI, C10.C2.VI, C10.C2.TH, C10.C2.UD, C10.C2.AH, C10.C2.AO]
ATT_P, ATT_N = C15.att(pe=True), C15.att(neg=True, pe=True)   # atthi / natthi tassa āvaṭṭanā…pe… paṇidhi (ch15)
assert ATT_P == C16.ATT_P and ATT_N == C16.NATT_P
SAR, ANAR = C15.SAR, C15.ANAR                             # sārammaṇa / anārammaṇa «có / không có đối tượng»

# ================================================================ (156) Niggaha / (157) Paggaha
OTHER = "của người khác"                                  # parassa (para «người khác» ch10)


def ng(obj):
    """paro parassa X niggaṇhāti (niggaṇhāti = saṃkilesāpattito nivāreti, aṭṭhakathā ^5-655)"""
    return f"một người chế ngự {obj}"


def pg(obj):
    """paro parassa X paggaṇhāti (cittaṃ paggaṇhāti «nâng tâm lên» pi-1 ^1-1377, pi-2)"""
    return f"một người nâng {obj} lên"


MIND = f"tâm {OTHER}"
T1, T2 = ng(MIND), pg(MIND)
NG4 = "“đừng tham đắm”, “đừng sân hận”, “đừng si mê”, “đừng bị phiền não làm ô nhiễm”"
# "mā rajji", "mā dussi", "mā muyhi", "mā kilissī"ti (ratta / duṭṭha / mūḷha / kiliṭṭha words ch11 / ch21)
NZ = "“đừng chấm dứt”"                                    # "mā nirujjhī"ti (ch19)
PH_UP = f"sự tiếp xúc {UPP} {OTHER}"                      # parassa uppanno phasso
CH_UP = f"{L10[1]} {UPP} {OTHER}… " + "… ".join(f"{x} {UPP}" for x in L10[2:])
# uppannā vedanā…pe… uppannā saññā… … uppanno samādhi…pe… uppannā paññā (^5-743)
CH_UP2 = f"{L10[1]} {UPP} {OTHER}… {L10[-1]} {UPP}"       # uppannā vedanā…pe… uppannā paññā (^5-745)
ATTHAYA = f"một người vì lợi ích {OTHER} mà"               # paro parassa atthāya (attha «lợi ích» pi-4 attahitāya)
PAJ = f"{ATTHAYA} dứt bỏ {C10.C2.R}… dứt bỏ {DO}… dứt bỏ {AO}"   # rāgaṃ pajahati… dosaṃ pajahati…pe… anottappaṃ
PAJ3 = f"{ATTHAYA} dứt bỏ {C10.C2.R}… dứt bỏ {DO}… dứt bỏ {MO}… dứt bỏ {AO}"   # … mohaṃ pajahati…pe… (^5-745)
WINGS = C10.C2.DEV6                                       # (plural forms in ch2; singular here)
BHAV = f"{ATTHAYA} tu tập con đường… tu tập sự thiết lập tỉnh thức… tu tập chi phần giác ngộ"
# maggaṃ bhāveti… satipaṭṭhānaṃ bhāveti…pe… bojjhaṅgaṃ bhāveti (ch3 «tu tập con đường», ch21 WINGS)
FOUR, FOUR_PE = f"{ATTHAYA} {C12.FOUR}", f"{ATTHAYA} {C12.FOUR_PE}"   # dukkhaṃ parijānāti … maggaṃ bhāveti (ch12)
AK = ("một người là người làm cho một người khác, sự dễ chịu, sự khó chịu do người khác làm ra, một người làm, "
      "một người khác cảm nhận")
# Añño aññassa kārako, paraṅkataṃ sukhaṃ dukkhaṃ añño karoti añño paṭisaṃvedeti (ch15 «một người là người làm cho
# một người khác»; sample ^5-179 paraṅkataṃ sukhadukkhaṃ «sự dễ chịu và sự khó chịu do người khác làm ra»; here
# sukhaṃ dukkhaṃ are two words without ca: comma; missing commas rendered as meant)
V165 = ["“Điều ác do chính mình làm, chính mình bị ô nhiễm;",
        "Điều ác chính mình không làm, chính mình được trong sạch;",
        "Trong sạch, không trong sạch là việc riêng của mỗi người, không ai có thể làm cho người khác trong sạch” "
        "[Kinh Pháp Cú 165]."]
# Attanāva kataṃ pāpaṃ, attanā saṃkilissati; / Attanā akataṃ pāpaṃ, attanāva visujjhati; / Suddhi asuddhi
# paccattaṃ, nāñño aññaṃ visodhaye (dha. pa. «Kinh Pháp Cú» terms file)
V165_PE = "“điều ác do chính mình làm… không ai có thể làm cho người khác trong sạch”"
BAL = "có những người đã đạt được sức mạnh, có những người đã đạt được sự làm chủ"
# atthi balappattā, atthi vasībhūtā (aṭṭhakathā: balappatti, vasībhāva)
GEN = (f"một người làm sinh khởi cho người khác {AL}, gốc rễ thiện… làm sinh khởi {AD}, gốc rễ thiện… làm sinh "
       f"khởi {AMO}, gốc rễ thiện… " + "… ".join(f"làm sinh khởi {x}" for x in L10[5:]))
# paro parassa alobhaṃ kusalamūlaṃ janeti… … paññaṃ janeti (kusalamūla «gốc rễ thiện» pi-1 ^1-32)

# ================================================================ (158) Sukhānuppadāna
SU, DU = "sự dễ chịu", "sự khó chịu"                      # sukha / dukkha (one word each in this kathā; sample ^5-179)
T3 = f"một người trao {SU} cho người khác"                 # paro parassa sukhaṃ anuppadeti
DU_Y = f"một người trao {DU} cho người khác"
DU_N = f"một người không trao {DU} cho người khác"
SU_N = f"một người không trao {SU} cho người khác"
THREE_Y = (f"một người trao cho người khác {SU} của chính mình, trao {SU} của những người khác, trao {SU} của "
           "người ấy")                                     # attano … aññesaṃ … tassa sukhaṃ anuppadeti (ch10 YES3)
THREE_N = (f"một người không trao cho người khác {SU} của chính mình, cũng không của những người khác, cũng không "
           "của người ấy")                                 # nevattano, na aññesaṃ, na tassa (ch10 NOT3)
UDAYI = ("Đức Thế Tôn quả thật đã loại bỏ cho chúng ta nhiều hiện tượng khó chịu, Đức Thế Tôn quả thật đã mang lại "
         "cho chúng ta nhiều hiện tượng dễ chịu, Đức Thế Tôn quả thật đã loại bỏ cho chúng ta nhiều hiện tượng bất "
         "thiện, Đức Thế Tôn quả thật đã mang lại cho chúng ta nhiều hiện tượng thiện")
# bahūnaṃ vata no bhagavā dukkhadhammānaṃ apahattā … kusalānaṃ dhammānaṃ upahattā (dhamma «hiện tượng» core)
UDAYI_NANU = "Chẳng phải tôn giả Ưu-đà-di đã nói thế này sao –"   # Nanu āyasmā udāyī etadavoca – (āyasmā ch5)
CITE_MN = "[Trung Bộ Kinh 2.148, trong Kinh Ví Dụ Chim Cút]"     # [ma. ni. 2.148 laṭukikopame] (ch21 pattern)

# ================================================================ (159) Adhigayhamanasikāra
T4 = "chú tâm bằng cách nắm gộp lại"                      # adhigayha manasi karoti (aṭṭhakathā: adhigaṇhitvā
#                                                           saṅgaṇhitvā … ekato manasikaroti)
KN = "dùng tâm ấy mà hiểu rõ tâm ấy"                      # tena cittena taṃ cittaṃ pajānāti (ch13 «dùng X mà V»)
KN_C = "dùng tâm ấy mà hiểu rõ tâm ấy là “tâm”"           # … taṃ cittaṃ "citta"nti pajānāti (ch13 X "X"nti)
K3 = "tâm ấy là đối tượng của tâm ấy"                     # taṃ cittaṃ tassa cittassa ārammaṇaṃ (ch13 / ch21 K3)
SELF10 = C13.SELF[:10]
SELF_PE = (f"dùng {SELF10[0][0]} ấy mà {SELF10[0][1]} {SELF10[0][0]} ấy, "
           + "… ".join(f"dùng {x} ấy" for x, _ in SELF10[1:9])
           + f"… dùng {SELF10[9][0]} ấy mà {SELF10[9][1]} {SELF10[9][0]} ấy")
# tena phassena taṃ phassaṃ phusati, tāya vedanāya…pe… … tāya paññāya taṃ paññaṃ pajānāti (ch13 SELF)
T_ = C5.T                                                 # quá khứ / tương lai / hiện tại (ch5)
TWO_PE = C15.TWO_PE                                       # dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hoti
THREE_PE = TWO_PE.replace("hai", "ba")                    # tiṇṇaṃ phassānaṃ…pe… tiṇṇaṃ cittānaṃ samodhānaṃ hoti
assert THREE_PE == "có sự tụ hợp của ba sự tiếp xúc… ba tâm"


def mk(first, rest):
    """X "X"nti manasikaronto, Y "Y"nti manasi karoti (, Z "Z"nti manasi karoti)"""
    return (f"trong khi chú tâm đến {T_[first]} là “{T_[first]}”, "
            + ", ".join(f"chú tâm đến {T_[r]} là “{T_[r]}”" for r in rest))   # (ch4 -onto «trong khi»)


def mk_line(first, rest):
    cl = mk(first, rest)
    return f"{Q(cl)} {NHP} {q(cl)} {AM} {Q(TWO_PE if len(rest) == 1 else THREE_PE)} {NHP}"


VERSE = ["“Khi nhờ trí tuệ mà thấy rằng tất cả các tạo tác đều vô thường;",
         "Thì nhàm chán khổ đau, đây là con đường đến sự thanh tịnh.",
         "“Khi nhờ trí tuệ mà thấy rằng tất cả các tạo tác đều là khổ đau;",
         "Thì nhàm chán khổ đau, đây là con đường đến sự thanh tịnh.",
         "“Khi nhờ trí tuệ mà thấy rằng tất cả các hiện tượng đều không phải là tự ngã;",
         "Thì nhàm chán khổ đau, đây là con đường đến sự thanh tịnh” [Kinh Pháp Cú 277-279]."]
# Sabbe saṅkhārā aniccāti … (ch10 «tất cả các tạo tác đều vô thường»; sample ^5-231 «tất cả các hiện tượng đều
# không phải là tự ngã»; nibbidā «sự nhàm chán» pi-2; visuddhi «sự thanh tịnh» ch11)

# ================================================================ (160)-(162) rūpa hetu / sahetuka / kusala
HE, SH, TH, BT = "là gốc rễ", "có gốc rễ", "là thiện", "là bất thiện"   # hetu / sahetuka (pi-1) / kusala / akusala


def first(t, end="."):
    """Xti? Āmantā. Sārammaṇaṃ, atthi tassa …pe… paṇidhīti? … nanu anārammaṇaṃ … Hañci anārammaṇaṃ … (ch16)"""
    return (f"{Q(t)} {AM} {Q(f'{SAR}, {ATT_P}')} {NHP} {nanu_l(f'{ANAR}, {ATT_N}')} {AM} "
            f"Nếu {ANAR}, {ATT_N}, {NO_CA_VATA} “{t}”{end}")


assert first(f"{RU} {TH}") == C16.first_line(RU, "thiện", False, False, False, ",")


def sa(items, pred):
    """X pred sārammaṇo, atthi tassa āvaṭṭanā…pe… paṇidhi (a …pe… chain of subjects allowed)"""
    return f"{chain([f'{x} {pred}' for x in items])}, {SAR}, {ATT_P}"


def an(items, pred):
    return f"{chain([f'{x} {pred}' for x in items])}, {ANAR}, {ATT_N}"


L5 = [AD, AMO, LO, DO, MO]                                # adoso … moho (^5-754 / ^5-755)
MBH = "các yếu tố cơ bản là gốc rễ mà các vật chất phái sinh{v} dựa vào"
# mahābhūtā upādāyarūpānaṃ upādāyahetu (mahābhūta «yếu tố cơ bản» pi-1; upādāyarūpa «vật chất phái sinh» pi-2;
# upādāya «dựa vào» sample; aṭṭhakathā: paccayaṭṭhena hetubhāvo)
MBH_V = MBH.format(v=f" [{VAR} (Sī., Pī., Ka.): upādārūpānaṃ]")
MBH0 = MBH.format(v="")
HN = ["nhờ gốc rễ không tham lam", "nhờ gốc rễ không sân hận", "nhờ gốc rễ không si mê", "nhờ gốc rễ tham lam",
      "nhờ gốc rễ sân hận", "nhờ gốc rễ si mê"]           # alobhahetunā … mohahetunā (ch19 hetunā «nhờ gốc rễ»)
SAPP = f"{RU} có điều kiện"                               # rūpaṃ sappaccayaṃ (ch17)
SH_ALL = [AD, AMO] + L10[5:] + KIL10                      # adoso…pe… amoho… saddhā… … anottappaṃ (^5-758)
KU_ALL = [AD, AMO] + L10[5:]                              # adoso…pe… amoho…pe… saddhā… … paññā (^5-761)
RKA, KVA = C16.RKA, C16.KVA                               # rūpaṃ / kāyakammaṃ vacīkammaṃ kusalampi akusalampi (ch16)
CLOSE_162 = f"{NVQ(RKA)} {AM} {NANU(KVA)} {AM} Nếu {KVA}, {B.TENA_VATA} “{RKA}”."   # = ch16 ^5-538 line 1

# ================================================================ (163) Rūpaṃ vipāko
VIP = C15.VIP                                             # vipāko «quả của nghiệp» (pi-1, ch15)
RV = f"{RU} là {VIP}"
VED, SAMP = C15.VED, C15.SAMP
POS_PE, NEG_PE = C15.POS_PE, C15.NEG_PE                   # (na) sukhavedaniyo (na) dukkhavedaniyo…pe… (an)ārammaṇo
PH = f"sự tiếp xúc là {VIP}, sự tiếp xúc"                 # phasso vipāko, phasso … (ch15 / ch20)
RVX = f"{RV}, {RU}"
KK = "do nghiệp đã được tạo"                              # kammassa katattā (ch20 «sinh khởi do nghiệp đã được tạo»)
CC = f"tâm và các yếu tố đồng hành với tâm sinh khởi {KK} là {VIP}"
# kammassa katattā uppannā cittacetasikā dhammā vipāko (pi-1 ^1-1029 «Tâm và các yếu tố đồng hành với tâm»)
RKV = f"{RU} sinh khởi {KK} là {VIP}"                     # kammassa katattā uppannaṃ rūpaṃ vipāko

# ================================================================ (164)-(165) rūpāvacara / dhātupariyāpanna
S3 = ["tìm kiếm sự thành tựu thiền", "tìm kiếm sự tái sinh", "an trú trong hạnh phúc ngay trong đời này"]
# samāpattesiya (samāpatti «thành tựu thiền» pi-1; esati «tìm kiếm» ch21) / upapattesiya (upapatti «tái sinh»
# coordinator) / diṭṭhadhammasukhavihāra (pi-1 «để an trú trong hạnh phúc ngay trong đời này»)
POS3 = ", ".join(S3)
NEG3 = ", ".join(f"không {x}" for x in S3)
NEG3_PE = f"không {S3[0]}, không {S3[1]}"                  # na samāpattesiyaṃ na upapattesiyaṃ…pe…
SAHA7 = C15.SAHA8[len("đi kèm, "):]                       # sahajātaṃ … ekārammaṇaṃ (ch15 / pi-2 ^2-567)
assert C15.SAHA8 == f"đi kèm, {SAHA7}"
ONE2 = "có cùng chỗ dựa, có cùng đối tượng"               # ekavatthukaṃ ekārammaṇaṃ
assert SAHA7.endswith(ONE2)
MIND_POS = f"đi kèm với tâm {S3[0]}, với tâm {S3[1]}, với tâm {S3[2]}, {SAHA7}"
# samāpattesiyena cittena upapattesiyena cittena diṭṭhadhammasukhavihārena cittena sahagataṃ … ekārammaṇaṃ
MIND_NEG = f"không đi kèm với tâm {S3[0]}, không với tâm {S3[1]}, không với tâm {S3[2]}, {SAHA7}"
MIND_NEG_PE1 = f"không đi kèm với tâm {S3[0]}… có cùng đối tượng"   # na samāpattesiyena cittena…pe… ekārammaṇaṃ
MIND_NEG_PE2 = f"không đi kèm với tâm {S3[0]}… {ONE2}"    # … …pe… ekavatthuko ekārammaṇo
CORE = f"{POS3}, {MIND_POS}"
RA_K, RA_R, RA_A = "thuộc cõi dục lạc", "thuộc cõi hình sắc", "thuộc cõi không hình sắc"   # (pi-1)
T9, T9A = f"có {RU} {RA_R}", f"có {RU} {RA_A}"           # atthi rūpaṃ rūpāvacaraṃ / arūpāvacaraṃ


def kk(x):
    """X-kammassa katattā rūpaṃ X"""
    return f"do nghiệp {x} đã được tạo, {RU} {x}"


RR, AR = "sự tham đắm cõi hình sắc", "sự tham đắm cõi không hình sắc"   # rūparāgo / arūparāgo (pi-1, pi-2)
IN = "nằm trong"                                          # -pariyāpanna (pi-2 kāmadhātupariyāpanna)
RD, AD_ = "cõi hình sắc", "cõi không hình sắc"            # rūpadhātu / arūpadhātu (realms, pi-1)
T10 = f"{RR} {IN} {RD}"
T10A = f"{AR} {IN} {AD_}"
SR = ["sự tham đắm âm thanh", "sự tham đắm mùi", "sự tham đắm vị", "sự tham đắm vật xúc chạm"]
# saddarāgo gandharāgo rasarāgo phoṭṭhabbarāgo (rāga «sự tham đắm» pi-1; āyatana objects pi-2)
SD = ["yếu tố âm thanh", "yếu tố mùi", "yếu tố vị", "yếu tố vật xúc chạm"]
# saddadhātu … phoṭṭhabbadhātu (pi-2 ^2-981: here dhātu = element, the pun of rūpadhātu cannot be kept)
KRK = f"sự tham đắm dục lạc {IN} cõi dục lạc"             # kāmarāgo kāmadhātupariyāpanno (pi-1, pi-2)


def nv(x, y, first_q=True):
    """X na vattabbaṃ – "Y"ti? (ch15 «đối với X, không nên nói –»)"""
    return f"{'Có' if first_q else 'có'} phải đối với {x}, không nên nói – “{y}” không?"


def dhatu_lines(r, t, rd):
    """^5-772 / ^5-774: the sound … tangible element analogy"""
    l1 = (f"{Q(t)} {AM} {Q(f'{SR[0]} {IN} {SD[0]}')} {NHP} {q(t)} {AM} "
          f"{Q(f'{SR[1]}… {SR[2]}… {SR[3]} {IN} {SD[3]}')} {NHP}")
    l2 = (f"{nv(SR[0], f'{IN} {SD[0]}')} {AM} {nv(r, f'{IN} {rd}')} {NHP} "
          f"{nv(f'{SR[1]}… {SR[2]}… {SR[3]}', f'{IN} {SD[3]}', False)} {AM} {nv(r, f'{IN} {rd}')} {NHP}")
    return l1, l2


# ================================================================ uddāna
UDD = (f"Sự chế ngự tâm, sự nâng tâm lên, {KX[3]}, {KX[4]}, {RU} {HE}, {RU} {SH}, {RKA}, {RV}, {T9}, {T9A}, "
       "tất cả các phiền não đều nằm trong cõi dục lạc.")
# Cittaniggaho, cittapaggaho, sukhānuppadānaṃ, adhigayha manasikāro, rūpaṃ hetu, rūpaṃ sahetukaṃ, rūpaṃ kusalampi
# akusalampi, rūpaṃ vipāko, atthi rūpaṃ rūpāvacaraṃ [no comma] atthi rūpaṃ arūpāvacaraṃ, sabbe kilesā
# kāmadhātupariyāpannāti. (kilesa «phiền não» pi-1; last item as written, it is not the kathā name)


def build():
    d = B.Doc()
    d.head(3, VAGGA16, "5-24-0")
    # ------------------------------------------------------------ (156) Niggaha
    d.head(4, f"(156) 1. {K(x=KX[1])}", "5-24-1-0")
    d.seg("5-743",
          f"{Q(T1)} {AM} {Q(f'{T1} {NG4}')} {NHP} {q(T1)} {AM} {Q(f'{ng(PH_UP)} {NZ}')} {NHP} "
          f"{q(f'{ng(CH_UP)} {NZ}')} {NHP}",
          f"{Q(T1)} {AM} {Q(PAJ)} {NHP}",
          f"{Q(T1)} {AM} {Q(BHAV)} {NHP}",
          f"{Q(T1)} {AM} {Q(FOUR)} {NHP}",
          f"{Q(T1)} {AM} {Q(AK)} {NHP}",
          f"{Q(T1)} {AM} {NANU_VUTTAM}",
          *V165,
          f"{ATTHEVA} {AM} {TENA_HI_NA(T1)}")
    d.seg("5-744",
          f"{NVQ(T1)} {AM} {NANU(BAL)} {AM} {B.hanci(BAL, T1)}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (157) Paggaha
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-745",
          f"{Q(T2)} {AM} {Q(f'{T2} {NG4}')} {NHP} {q(T2)} {AM} {Q(GEN)} {NHP} {q(T2)} {AM} "
          f"{Q(f'{pg(PH_UP)} {NZ}')} {NHP} {q(f'{pg(CH_UP2)} {NZ}')} {NHP}",
          f"{Q(T2)} {AM} {Q(PAJ3)} {NHP}",
          f"{Q(T2)} {AM} {Q(BHAV)} {NHP}",
          f"{Q(T2)} {AM} {Q(FOUR_PE)} {NHP}",
          f"{Q(T2)} {AM} {Q(AK)} {NHP}",
          f"{Q(T2)} {AM} {NANU_VUTTAM} {V165_PE}. {ATTHEVA} {AM} {TENA_HI_NA(T2)}")
    d.seg("5-746",
          f"{NVQ(T2)} {AM} {NANU(BAL)} {AM} {B.hanci(BAL, T2)}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (158) Sukhānuppadāna
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-747",
          f"{Q(T3)} {AM} {Q(DU_Y)} {NHP} {q(DU_N)} {AM} {Q(SU_N)} {NHP} {q(T3)} {AM} {Q(THREE_Y)} {NHP} "
          f"{q(THREE_N)} {AM} {hanci_no(THREE_N, T3)}",
          f"{Q(T3)} {AM} {Q(AK)} {NHP}")
    d.seg("5-748",
          f"{NVQ(T3)} {AM} {UDAYI_NANU} “{UDAYI}” {CITE_MN}! {ATTHEVA} {AM} {TENA_HI(T3)}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (159) Adhigayhamanasikāra
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-749",
          f"{Q(T4)} {AM} {Q(KN)} {NHP} {q(KN)} {AM} {Q(KN_C)} {NHP} {q(KN_C)} {AM} {Q(K3)} {NHP}",
          f"{Q(K3)} {AM} {Q(SELF_PE)} {NHP}")
    for sid, a, others in (("5-750", "a", ("f", "p")), ("5-751", "f", ("a", "p")), ("5-752", "p", ("a", "f"))):
        d.seg(sid, mk_line(a, [others[0]]), mk_line(a, [others[1]]), mk_line(a, list(others)))
    d.seg("5-753",
          f"{NVQ(T4)} {AM} {NANU_VUTTAM}",
          *VERSE,
          f"{ATTHEVA} {AM} {TENA_HI(T4)}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (160) Rūpaṃ hetu
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    th5 = f"{RU} {HE}"
    d.seg("5-754",
          f"{Q(th5)} {AM} {Q(f'{AL} {HE}')} {NHP} {q(chain([f'{x} {HE}' for x in L5]))} {NHP}",
          first(th5))
    d.seg("5-755",
          f"{Q(sa([AL], HE))} {AM} {Q(sa([RU], HE))} {NHP} {q(sa(L5, HE))} {AM} {Q(sa([RU], HE))} {NHP}",
          f"{Q(an([RU], HE))} {AM} {Q(an([AL], HE))} {NHP} {q(an([RU], HE))} {AM} {Q(an(L5, HE))} {NHP}")
    d.seg("5-756",
          f"{NVQ(th5)} {AM} {NANU(MBH_V)} {AM} {B.hanci(MBH0, th5)}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (161) Rūpaṃ sahetuka
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    th6 = f"{RU} {SH}"
    d.seg("5-757",
          f"{Q(th6)} {AM} {Q(HN[0])} {NHP} {q(chain(HN[1:]))} {NHP}",
          first(th6))
    sh_chain = f"{AD} {SH}… {chain(SH_ALL[1:-1])}… {AO} {SH}, {SAR}, {ATT_P}"
    d.seg("5-758",
          f"{Q(sa([AL], SH))} {AM} {Q(sa([RU], SH))} {NHP} {q(sh_chain)} {AM} {Q(sa([RU], SH))} {NHP}",
          f"{Q(an([RU], SH))} {AM} {Q(an([AL], SH))} {NHP} {q(an([RU], SH))} {AM} "
          f"{Q(f'{AD} {SH}… {AO} {SH}, {ANAR}, {ATT_N}')} {NHP}")
    d.seg("5-759",
          f"{NVQ(th6)} {AM} {NANU(SAPP)} {AM} {B.hanci(SAPP, th6)}",
          E(x=KX[6]))
    # ------------------------------------------------------------ (162) Rūpaṃ kusalākusala
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    th7, th7a = f"{RU} {TH}", f"{RU} {BT}"
    d.seg("5-760", first(th7))
    ku_chain = f"{AD} {TH}… {AMO} {TH}… {chain(KU_ALL[2:-1])}… {KU_ALL[-1]} {TH}, {SAR}, {ATT_P}"
    d.seg("5-761",
          f"{Q(sa([AL], TH))} {AM} {Q(sa([RU], TH))} {NHP}",
          f"{Q(ku_chain)} {AM} {Q(sa([RU], TH))} {NHP}",
          f"{Q(an([RU], TH))} {AM} {Q(an([AL], TH))} {NHP}",
          f"{Q(an([RU], TH))} {AM} {Q(f'{AD} {TH}… {KU_ALL[-1]} {TH}, {ANAR}, {ATT_N}')} {NHP}")
    d.seg("5-762", first(th7a, end="…"))
    d.seg("5-763",
          f"{Q(sa([LO], BT))} {AM} {Q(sa([RU], BT))} {NHP} "
          f"{q(f'{DO}… {MO}… {KIL10[3]}… {AO} {BT}, {SAR}, {ATT_P}')} {AM} {Q(sa([RU], BT))} {NHP}",
          f"{Q(an([RU], BT))} {AM} {Q(an([LO], BT))} {NHP} {q(an([RU], BT))} {AM} "
          f"{Q(f'{DO}… {MO}… {AO} {BT}, {ANAR}, {ATT_N}')} {NHP}")
    d.seg("5-764", CLOSE_162, E(x=KX[7]))
    # ------------------------------------------------------------ (163) Rūpaṃ vipāko
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    pos_l = f"{', '.join(VED)}, {', '.join(SAMP[:4])}… {SAMP[7]}, {SAR}"
    d.seg("5-765",
          f"{Q(RV)} {AM} Có phải {RU} {pos_l}, {ATT_P} không? {NHP} {nanu_l(f'{NEG_PE}, {ATT_N}')} {AM} "
          f"{hanci_no(f'{NEG_PE}, {ATT_N}', RV)}")
    d.seg("5-766",
          f"Có phải {PH} {POS_PE}, {ATT_P} không? {AM} Có phải {RVX} {POS_PE}, {ATT_P} không? {NHP}",
          f"Có phải {RVX} {NEG_PE}, {ATT_N} không? {AM} Có phải {PH} {NEG_PE}, {ATT_N} không? {NHP}")
    d.seg("5-767",
          f"{NVQ(RV)} {AM} {NANU(CC)} {AM} {B.hanci(CC, RKV)}",
          E(x=KX[8]))
    # ------------------------------------------------------------ (164) Rūpaṃ rūpāvacarārūpāvacara
    for lv, t, sid in heads(9):
        d.head(lv, t, sid)
    d.seg("5-768",
          f"{Q(T9)} {AM} {Q(CORE)} {NHP} {nanu_l(f'{NEG3}, {MIND_NEG}')} {AM} "
          f"{hanci_no(f'{NEG3}, {MIND_NEG_PE1}', T9)}")
    d.seg("5-769",
          f"{Q(T9A)} {AM} {Q(CORE)} {NHP} {nanu_l(f'{NEG3}, {MIND_NEG_PE1}')} {AM} "
          f"{hanci_no(f'{NEG3_PE}… {ONE2}', T9A)}")
    both = f"{T9}, {T9A}"
    d.seg("5-770",
          f"{NVQ(both)} {AM} {NANU(kk(RA_K))} {AM} {B.hanci(kk(RA_K), f'{kk(RA_R)}, {kk(RA_A)}')}",
          E(x=KX[9]))
    # ------------------------------------------------------------ (165) Rūpārūpadhātupariyāpanna
    for lv, t, sid in heads(10):
        d.head(lv, t, sid)
    d.seg("5-771",
          f"{Q(T10)} {AM} {Q(CORE)} {NHP} {nanu_l(f'{NEG3}, {MIND_NEG_PE2}')} {AM} "
          f"{hanci_no(f'{NEG3}, {MIND_NEG_PE2}', T10)}")
    d.seg("5-772", *dhatu_lines(RR, T10, RD))
    d.seg("5-773",
          f"{Q(T10A)} {AM} {nv(AR, f'{IN} {AD_}')} {NHP} {q(T10A)} {AM} {Q(CORE)} {NHP} "
          f"{nanu_l(f'{NEG3}, {MIND_NEG_PE2}')} {AM} {hanci_no(f'{NEG3}, {MIND_NEG}', T10A)}")
    d.seg("5-774", *dhatu_lines(AR, T10A, AD_))
    both10 = f"{T10}, {T10A}"
    d.seg("5-775",
          f"{NVQ(both10)} {AM} {NANU(KRK)} {AM} {B.hanci(KRK, both10)}",
          E(x=f"việc cho rằng {both10}"),
          E(x=KX[10]),
          f"{VAGGA16}.",
          TASSUDDANAM,
          UDD)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("nâng tâm lên", 1), ("gốc rễ thiện", 1), (f"{AL}, {AD}, {AMO}", 1), (f"{cap(LO)}, {DO}, {MO}", 1),
    ("vật chất phái sinh", 2), ("yếu tố cơ bản", 1), ("Tâm và các yếu tố đồng hành với tâm", 1),
    ("an trú trong hạnh phúc ngay trong đời này", 1), ("thành tựu thiền", 1), ("nằm trong cõi dục lạc", 2),
    (f"{cap(RR)}, {AR}", 2), (", ".join(SD[:1]), 2), ("yếu tố mùi", 2), ("yếu tố vị", 2), ("yếu tố vật xúc chạm", 2),
    ("Các hiện tượng là gốc rễ", 1), ("Các hiện tượng có gốc rễ", 1), (RA_K, 1), (RA_R, 1), (RA_A, 1),
    ("sự tham đắm dục lạc", 1), ("sự nhàm chán", 2), ("Trung Bộ Kinh", 4), ("hiểu biết trọn vẹn", 2),
    ("phiền não", 1), ("không có gốc rễ", 1), ("cõi hình sắc", 1), ("cõi không hình sắc", 1), ("cõi dục lạc", 1),
    ("sự tham lam", 1), ("sự không biết ghê sợ tội lỗi", 1), ("vì lợi ích của bản thân", 4), ("tự ngã", 2),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (ATT_P, "15-sattamavaggo.md"), (ATT_N, "15-sattamavaggo.md"), (POS_PE, "15-sattamavaggo.md"),
    (NEG_PE, "15-sattamavaggo.md"), (f"{', '.join(VED)}, {', '.join(SAMP[:4])}", "15-sattamavaggo.md"),
    (SAMP[7], "15-sattamavaggo.md"), (SAHA7, "15-sattamavaggo.md"), (TWO_PE, "15-sattamavaggo.md"),
    ("Có phải một người là người làm cho một người khác", "15-sattamavaggo.md"), (PH, "15-sattamavaggo.md"),
    ("Có phải đối với", "15-sattamavaggo.md"), (f"là {VIP}", "15-sattamavaggo.md"),
    ("một người làm, một người khác cảm nhận", "1-puggalakatha.md"),
    ("sự dễ chịu và sự khó chịu do người khác làm ra", "1-puggalakatha.md"),
    ("tất cả các hiện tượng đều không phải là tự ngã", "1-puggalakatha.md"), ("dựa vào", "1-puggalakatha.md"),
    (C12.FOUR, "12-catutthavaggo.md"), (C12.FOUR_PE, "12-catutthavaggo.md"),
    (", ".join(L10), "15-sattamavaggo.md"),
    (", ".join(f"dùng {x} ấy mà {v} {x} ấy" for x, v in SELF10), "13-pancamavaggo.md"),
    (CLOSE_162, "16-atthamavaggo.md"), (C16.first_line(C16.kk(C16.TH), C16.TH, True, True, False, ",")[:60],
                                        "16-atthamavaggo.md"),
    (f"Nếu {ANAR}, {ATT_N}, {NO_CA_VATA}", "16-atthamavaggo.md"),
    (NANU(SAPP), "17-navamavaggo.md"),
    (TASSUDDANAM, "10-dutiyavaggo.md"), ("tất cả các tạo tác đều vô thường", "10-dutiyavaggo.md"),
    ("của chính mình, cũng không của những người khác, cũng không của người ấy", "10-dutiyavaggo.md"),
    ("Kinh Pháp Cú", "3-brahmacariyakatha.md"), ("tôn giả", "5-sabbamatthitikatha.md"),
    ("sinh khởi do nghiệp đã được tạo", "20-dvadasamavaggo.md"), ("người đã bị phiền não làm ô nhiễm",
                                                                "21-terasamavaggo.md"),
    ("đừng chấm dứt", "19-ekadasamavaggo.md"), (f"{L10[1]} {UPP}", "19-ekadasamavaggo.md"),
    ("nhờ gốc rễ ấy", "19-ekadasamavaggo.md"), ("tu tập con đường", "3-brahmacariyakatha.md"),
    ("là đối tượng của", "21-terasamavaggo.md"), ("trong khi tự mình chứng nghiệm", "4-jahatikatha.md"),
    ("Trung Bộ Kinh 3.409, trong Kinh", "21-terasamavaggo.md"), ("tìm kiếm", "21-terasamavaggo.md"),
    ("người đang nhập thành tựu thiền", "10-dutiyavaggo.md"), (RKA, "16-atthamavaggo.md"),
    ("làm sinh khởi", "21-terasamavaggo.md"), ("sự thanh tịnh", "11-tatiyavaggo.md"),
    (f"{T_['a']}", "5-sabbamatthitikatha.md"), (f"{T_['p']}", "5-sabbamatthitikatha.md"),
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
    print(f"ch24 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
