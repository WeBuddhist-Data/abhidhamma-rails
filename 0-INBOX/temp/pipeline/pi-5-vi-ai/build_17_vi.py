# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 17: 17-navamavaggo.md (Navamavaggo, ^5-17-0 … ^5-570),
the eleven kathā (84)-(94) of the ninth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished
chapter builders build_2_vi / build_4_vi / build_5_vi / build_9_vi / build_11_vi (read-only, importing writes
nothing) for the kilesa / anusaya lists, the asaṃyojaniya … asaṃkilesiya names, the past / future descriptors,
the vagga close and the samodhāna formula, so every repeat is byte-identical with those chapters. Every string
claimed from the pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a finished pi-5
chapter is asserted to occur in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC,
foreign letters) are run against the Pāli. Every Pāli sentence keeps its own sentence.

run:  python -I -B -X utf8 build_17_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (kilesa list, kāmarāga list, anusaya list, Hañci … no ca vata)
import build_4_vi as C4      # noqa: E402  (asaṃyojaniya … asaṃkilesiya)
import build_5_vi as C5      # noqa: E402  (atīta / anāgata descriptors)
import build_9_vi as C9      # noqa: E402  (Tassuddānaṃ –)
import build_11_vi as C11    # noqa: E402  (saṃyojaniya … saṃkilesiya, dvinnaṃ phassānaṃ … samodhānaṃ)

NAME = "17-navamavaggo.md"
Q, q, NANU, AM, cap = B.Q, B.q, B.NANU, B.AMANTA, B.cap
NHP = B.NA_HEVAM_PE
NVQ, TENA_HI = B.NA_VATTABBAM_Q, B.TENA_HI
NCV, TV = B.NO_CA_VATA, B.TENA_VATA
HNO = C2.hanci_no                                          # Hañci P, no ca vata re vattabbe – "Q"ti. (ch2)
VAR = B.VAR
VAGGA9 = B.VAGGA[9]                                        # Navamavaggo = «Chương thứ chín» (terms file)
K, E = B.KATHA.format, B.KATHA_END.format


def nanu_lc(x):
    """…pe… nanu Xti? (lowercase start, ch5)"""
    return f"chẳng phải {x} sao?"


def tena_hi_lc(x):
    """…pe… tena hi Xti. (lowercase start, ch14)"""
    return f"vậy thì {x}."


def heads(n, num, title):
    """#### Navamavaggo ^5-17-n-0 / ##### (num) n. <title> ^5-17-n-1-0"""
    return [(4, VAGGA9, f"5-17-{n}-0"), (5, f"({num}) {n}. {K(x=title)}", f"5-17-{n}-1-0")]


# ================================================================ shared terms
SA, ANA = "có đối tượng", "không có đối tượng"            # sārammaṇa / anārammaṇa (pi-1 sārammaṇā dhammā)
SAMY = "các xiềng xích"                                   # saṃyojanā (core saṃyojana)
NIB = "Niết-bàn"
AMATA = "điều bất tử"                                     # amataṃ (ch10, ch14 amata «điều bất tử»)
RUPA = B.RUPA                                             # rūpaṃ = «vật chất» (pi-2)
TWO_PE = "có sự tụ hợp của hai sự tiếp xúc… hai tâm"      # dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hoti
assert C11.TWO == "có sự tụ hợp của hai sự tiếp xúc, hai tâm"
SKP = "thuộc về khối tạo tác"                             # saṅkhārakkhandhapariyāpanna (pariyāpanna «thuộc về» ch10)
KATAMA = "Thuộc về khối nào?"                             # Katamakkhandhapariyāpanno / -pannanti?
SKP_ANS = "Thuộc về khối tạo tác."                        # Saṅkhārakkhandhapariyāpannoti / -pannanti.
SKK = "khối tạo tác"                                      # saṅkhārakkhandho (pi-2)
VSV = "khối cảm giác, khối tri giác, khối thức"           # vedanākkhandho saññākkhandho viññāṇakkhandho (pi-2)
RN = f"là {RUPA}, {NIB}, {B.AYATANA[0]}… {B.AYATANA[9]}"   # rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ


def part(x):
    """X ekadeso sārammaṇo ekadeso anārammaṇo (ch3 / ch11 ekadesa «một phần»)"""
    return f"{x} một phần {SA}, một phần {ANA}"


def arb(obj, subj):
    """obj ārabbha subj uppajjati / uppajjanti (pi-1 ^1-1047 «sinh khởi khi lấy … làm đối tượng»)"""
    return f"{subj} sinh khởi khi lấy {obj} làm đối tượng"


# ================================================================ (84) Ānisaṃsadassāvī
ANI = "người thấy lợi ích"                                # ānisaṃsadassāvī (terms file heading)
T1 = f"{ANI} có sự dứt bỏ {SAMY}"                         # ānisaṃsadassāvissa saṃyojanānaṃ pahānaṃ (ch13 X-assa Y)
SKH = B.SANKHARA                                          # saṅkhāre = «các tạo tác» (pi-2)
TO = ["là vô thường", "là khổ đau", "là bệnh tật", "là ung nhọt", "là mũi tên", "là điều bất hạnh", "là sự đau ốm",
      "là cái xa lạ", "là cái tan rã", "là tai họa", "là tai ương", "là điều đáng sợ", "là tai nạn",
      "là cái dao động", "là cái dễ vỡ", "là cái không bền vững", "là cái không phải nơi che chở",
      "là cái không phải nơi ẩn náu", "là cái không phải nơi nương tựa", "là cái không trở thành nơi nương tựa",
      "là cái rỗng không", "là cái hư rỗng", "là cái trống rỗng", "không phải là tự ngã", "là sự nguy hại",
      "là có bản chất biến đổi"]
# aniccato dukkhato rogato gaṇḍato sallato aghato ābādhato parato palokato ītito upaddavato bhayato upasaggato
# calato pabhaṅguto addhuvato atāṇato aleṇato asaraṇato asaraṇībhūtato rittato tucchato suññato anattato
# ādīnavato vipariṇāmadhammato  (X-to = «là X» ch10 aniccato diṭṭhe; dhuva «bền vững» pi-2; tāṇa / leṇa / saraṇa
# «nơi che chở / nơi ẩn náu / nơi nương tựa» ch10; suñña «trống rỗng» sample; anatta «không phải là tự ngã» pi-2;
# vipariṇāmadhamma «có bản chất biến đổi» pi-1, pi-2)
CHAIN_TO = "… ".join(TO[1:])                              # dukkhato…pe… rogato… … ādīnavato…pe… vipariṇāmadhammato


def mk(a):
    """saṅkhāre X-to manasikaroto saṃyojanā pahīyanti"""
    return f"đối với người chú tâm đến {SKH} {a}, {SAMY} được dứt bỏ"


def both(a):
    """saṅkhāre ca X-to manasi karoti nibbāne ca ānisaṃsadassāvī hoti (ch11 «vừa … vừa …»)"""
    return f"vừa chú tâm đến {SKH} {a}, vừa là {ANI} nơi {NIB}"


SUTTA_AN = ("Ở đây, này các tỳ-khưu, tỳ-khưu sống quán sát hạnh phúc nơi Niết-bàn, có tri giác về hạnh phúc, "
            f"cảm nhận hạnh phúc, {'thường xuyên, liên tục, liền mạch'}, dùng tâm mà dứt khoát hướng đến, "
            "dùng trí tuệ mà đi sâu vào")
# idha, bhikkhave, bhikkhu nibbāne sukhānupassī viharati sukhasaññī sukhapaṭisaṃvedī, satataṃ samitaṃ abbokiṇṇaṃ
# cetasā adhimuccamāno paññāya pariyogāhamāno (kāye kāyānupassī viharati «sống quán sát thân» pi-2;
# satataṃ samitaṃ abbokiṇṇaṃ ch12; pariyogāhanā «sự đi sâu» pi-1)

# ================================================================ (85) Amatārammaṇa
T2 = f"xiềng xích lấy {AMATA} làm đối tượng"              # amatārammaṇaṃ saṃyojanaṃ (ch11 -ārammaṇa «lấy … làm đối tượng»)
KX2 = f"đối tượng là {AMATA}"                             # Amatārammaṇakathā (ch13 Cittārammaṇakathā «đối tượng là tâm»)
OBJ = C11.OBJ[1:]                                         # saṃyojaniya ganthaniya … saṃkilesiya (pi-1, ch4, ch11)
NOBJ = C4.POS[5:]                                         # asaṃyojaniya aganthaniya … asaṃkilesiya (pi-1, ch4)
assert OBJ[0] == "là đối tượng của xiềng xích" and NOBJ[0] == "không phải là đối tượng của xiềng xích"
assert len(OBJ) == len(NOBJ) == 8 and OBJ[-1] == "là đối tượng của phiền não"
OBJ_ALL, NOBJ_ALL = ", ".join(OBJ), ", ".join(NOBJ)
OBJ_2PE, NOBJ_2PE = f"{OBJ[0]}, {OBJ[1]}… {OBJ[-1]}", f"{NOBJ[0]}, {NOBJ[1]}… {NOBJ[-1]}"
OBJ_1PE, NOBJ_1PE = f"{OBJ[0]}… {OBJ[-1]}", f"{NOBJ[0]}… {NOBJ[-1]}"
# the three lists of ch10 ^5-349 (rāgaṭṭhāniya …; dosaṭṭhāniya …; mohaṭṭhāniya …), byte for byte
RG = "khơi dậy sự tham đắm, hấp dẫn, đáng ham muốn, làm say đắm, trói buộc, làm mê mẩn"
NRG = ("không khơi dậy sự tham đắm, không hấp dẫn, không đáng ham muốn, không làm say đắm, không trói buộc, "
       "không làm mê mẩn")
DS = "khơi dậy sự sân hận, khơi dậy sự phẫn nộ, khơi dậy sự ác cảm"
NDS = "không khơi dậy sự sân hận, không khơi dậy sự phẫn nộ, không khơi dậy sự ác cảm"
MH = ("khơi dậy sự si mê, tạo ra sự không biết, làm cho không có mắt, làm chấm dứt trí tuệ, thuộc về phía gây "
      "phiền não, không dẫn đến Niết-bàn")
NMH = ("không khơi dậy sự si mê, không tạo ra sự không biết, không làm cho không có mắt, làm tăng trưởng trí "
       "tuệ, không thuộc về phía gây phiền não, dẫn đến Niết-bàn")
# here paññābuddhiyaṃ (ch10 paññāvuddhiko): b / v spelling, rendered as ch10
RG_PE, NRG_PE = "khơi dậy sự tham đắm… làm mê mẩn", "không khơi dậy sự tham đắm… không làm mê mẩn"
MH_PE = "khơi dậy sự si mê, tạo ra sự không biết… không dẫn đến Niết-bàn"
NMH_PE = "không khơi dậy sự si mê, không tạo ra sự không biết… dẫn đến Niết-bàn"
RAGA, DOSA, MOHA = C2.R, C2.D, C2.M                       # rāgo doso moho (ch2, pi-1)
SUTTA_MN = ("Nhận ra Niết-bàn như là Niết-bàn, sau khi nhận ra Niết-bàn như là Niết-bàn, tưởng tượng về Niết-bàn, "
            "tưởng tượng trong Niết-bàn, tưởng tượng từ Niết-bàn, tưởng tượng Niết-bàn là của tôi, hoan hỷ với "
            "Niết-bàn")
# nibbānaṃ nibbānato sañjānāti … nibbānaṃ meti maññati, nibbānaṃ abhinandati (sañjānāti «nhận ra» pi-1;
# X-to «như là X» ch13 pathaviṃ pathavito; meti has no quote marks in the Pāli)

# ================================================================ (86) Rūpaṃ sārammaṇaṃ
T3 = f"{RUPA} {SA}"
AV7 = "sự hướng đến, sự chú hướng, sự lưu ý, sự chú tâm, chủ ý, sự mong muốn, sự mong cầu"
# āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi (pi-2 ^2 «sự hướng đến, sự chú hướng, sự lưu ý
# hay sự chú tâm»; patthanā «sự mong muốn» pi-1; paṇidhi «sự mong cầu» ch11)
AV_PE = "sự hướng đến, sự chú hướng… sự mong cầu"         # āvaṭṭanā ābhogo…pe… paṇidhi
AVP = "sự hướng đến… sự mong cầu"                         # āvaṭṭanā…pe… paṇidhi
PHASSA = "sự tiếp xúc"
L19 = (f"{B.VEDANA}… {B.SANNA}, chủ ý, tâm, niềm tin, sự tinh tấn, sự tỉnh thức, sự định tâm, trí tuệ, "
       f"{C2.R}, {C2.D}, {C2.M}, {C2.MANA}, {C2.DI}, {C2.VI}, {C2.TH}, {C2.UD}, {C2.AH}… {C2.AO}")
# vedanā…pe… saññā cetanā cittaṃ saddhā vīriyaṃ sati samādhi paññā rāgo … ahirikaṃ…pe… anottappaṃ (ch12 counted
# list «… chủ ý, … tâm, … niềm tin, … sự tinh tấn, … sự tỉnh thức, … sự định tâm, … trí tuệ»; ch2 kilesa list)
L19_PE = f"{B.VEDANA}… {C2.AO}"                            # vedanā…pe… anottappaṃ

# ================================================================ (87) Anusayā anārammaṇā
T4 = f"{C2.ANUSAYA} {ANA}"                                # anusayā anārammaṇā
KRA = C2.AN7.split(", ")[0]                               # kāmarāgānusayo (ch2, pi-2)
AN_REST = ", ".join(C2.AN7.split(", ")[1:])               # paṭighānusayo … avijjānusayo
AVA = C2.AN7.split(", ")[-1]                              # avijjānusayo
assert C2.KR.startswith(f"{C2.R}, ")
KR6 = C2.KR[len(f"{C2.R}, "):]                            # kāmarāgo kāmarāgapariyuṭṭhānaṃ … kāmacchandanīvaraṇaṃ (ch2)
KR1 = KR6.split(", ")[0]                                  # kāmarāgo = «sự tham đắm dục lạc»
AVJ = "vô minh"
AVJ7 = ("vô minh, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh, xiềng xích vô "
        "minh, chướng ngại vô minh")                     # avijjā avijjogho … avijjānīvaraṇaṃ (ch10, pi-1, pi-2)
AVJ_PE = "vô minh, dòng lũ vô minh… chướng ngại vô minh"   # avijjā avijjogho…pe… avijjānīvaraṇaṃ
KUS = "khi tâm thiện hay không xác định về mặt đạo đức đang diễn ra"   # kusalābyākate citte vattamāne (pi-1)
PU = C4.PUTHUJJANA                                        # puthujjano = «người phàm phu» (pi-1, ch4)


def anusaya_block(an, kil):
    """the three lines Katamakkhandhapariyāpanno … ekadeso anārammaṇoti? (^5-554 lines 3-5 / ^5-555 lines 2-4)"""
    return (
        f"{Q(f'{an} {ANA}')} {AM} {KATAMA} {SKP_ANS} {Q(f'{SKK} {ANA}')} {NHP} {q(f'{SKK} {ANA}')} {AM} "
        f"{Q(f'{VSV} {ANA}')} {NHP}",
        f"{Q(f'{an} {SKP} {ANA}')} {AM} {Q(f'{kil} {SKP} {ANA}')} {NHP} {q(f'{kil} {SKP} {SA}')} {AM} "
        f"{Q(f'{an} {SKP} {SA}')} {NHP}",
        f"{Q(f'{an} {SKP} {ANA}, {kil} {SKP} {SA}')} {AM} {Q(part(SKK))} {NHP} {q(part(SKK))} {AM} "
        f"{Q(part(VSV))} {NHP}",
    )


# ================================================================ (88) Ñāṇaṃ anārammaṇaṃ
NANA = "hiểu biết"                                        # ñāṇa (pi-1)
PANNA = "trí tuệ"
T5 = f"{NANA} {ANA}"
PN5 = "trí tuệ, năng lực trí tuệ, sức mạnh trí tuệ, quan điểm đúng đắn, chi phần giác ngộ là sự tìm hiểu các hiện tượng"
# paññā paññindriyaṃ paññābalaṃ sammādiṭṭhi dhammavicayasambojjhaṅgo (pi-1 ^1-292)
ARAHA_C = "bậc A-la-hán có được thức qua mắt"             # arahā cakkhuviññāṇasamaṅgī (samaṅgī «có được» ch13, pi-1)

# ================================================================ (89) Atītānāgatārammaṇa
T_ = C5.T                                                 # quá khứ / tương lai / hiện tại (ch5)
ARM = {k: f"có đối tượng thuộc {v}" for k, v in T_.items()}   # atīt- / anāgat- / paccuppannārammaṇa (pi-1 ^1-1047)
CIT = {k: f"tâm {v}" for k, v in ARM.items()}             # X-ārammaṇaṃ cittaṃ
KX6 = f"đối tượng thuộc {T_['a']} và {T_['f']}"           # Atītānāgatārammaṇakathā
T6 = f"tâm có đối tượng thuộc {T_['a']} và {T_['f']} {ANA}"   # atītānāgatārammaṇaṃ cittaṃ anārammaṇaṃ


def arb_av(t):
    """X ārabbha atthi āvaṭṭanā…pe… paṇidhi"""
    return f"khi lấy {T_[t]} làm đối tượng, có {AVP}"


def micchā_line(t):
    """^5-559 / ^5-560 first line (the ch5 «nói rằng … là sai» verdict)"""
    th = f"{CIT[t]} {ANA}"
    return (f"{Q(th)} {AM} {NANU(ARM[t])} {AM} {HNO(ARM[t], th)} Nói rằng {th} là sai. Hoặc nếu {ANA}, {NCV} "
            f"“{ARM[t]}”. Nói rằng cái {ANA} {ARM[t]} là sai.")


# ================================================================ (90) Vitakkānupatita
VIT = "sự hướng tâm"                                      # vitakka (core)


def anup(x):
    """X-ānupatita = «có X đi theo»"""
    return f"có {x} đi theo"


T7 = f"tất cả tâm đều {anup(VIT)}"                         # sabbaṃ cittaṃ vitakkānupatitaṃ
KX7 = f"điều {anup(VIT)}"                                 # Vitakkānupatitakathā
L95 = ["sự duy trì tâm", "sự hân hoan", "hạnh phúc", "khổ đau", "niềm vui", "nỗi buồn", "sự bình thản", "niềm tin",
       "sự tinh tấn", "sự tỉnh thức", "sự định tâm", "trí tuệ", C2.R, C2.D]
# vicāra pīti sukha dukkha somanassa domanassa upekkhā saddhā vīriya sati samādhi paññā rāga dosa (pi-1)
S1 = "định tâm có sự hướng tâm và sự duy trì tâm"         # savitakko savicāro samādhi (pi-2)
S2 = "định tâm không có sự hướng tâm, chỉ có sự duy trì tâm"   # avitakko vicāramatto samādhi (pi-1 matrix)
S3 = "định tâm không có sự hướng tâm cũng không có sự duy trì tâm"   # avitakko avicāro samādhi (pi-2)
BS3 = f"Đức Thế Tôn đã nói đến ba sự định tâm – {S1}, {S2}, {S3}"   # tayo samādhī vuttā bhagavatā – … (ch11 BS)

# ================================================================ (91) Vitakkavipphārasadda


def vipp(act, x):
    """sabbaso X-ayato X-vipphāro saddo"""
    return f"trong mọi trường hợp khi {act}, sự lan tỏa của {x} là âm thanh"


T8 = vipp("hướng tâm, duy trì tâm", VIT)                  # sabbaso vitakkayato vicārayato vitakkavipphāro saddo
VS_ = f"âm thanh lan tỏa của {VIT}"                       # vitakkavipphāro saddo (subject) / Vitakkavipphārasaddakathā
V7 = [("tiếp xúc", PHASSA), ("cảm nhận", B.VEDANA), ("nhận ra", B.SANNA), ("cố ý", "chủ ý"), ("suy nghĩ", "tâm"),
      ("nhớ", "sự tỉnh thức"), ("hiểu rõ", PANNA)]
# phusayato vedayato sañjānato cetayato cintayato sarato pajānato (sañjānāti «nhận ra» pi-1; ceteti «cố ý» ch13;
# pajānāti «hiểu rõ» ch13)
LD_EAR = "được nhận biết bằng tai, va chạm vào tai, đi vào tầm của tai"            # (ch10 ^5-348)
NLD_EAR = "không được nhận biết bằng tai, không va chạm vào tai, không đi vào tầm của tai"

# ================================================================ (92)-(93) Na yathācittassa
T9 = "lời nói không tùy theo tâm"                         # na yathācittassa vācā
KK = "nghiệp bằng thân"                                   # kāyakammaṃ (pi-1, ch14)
T10 = f"{KK} không tùy theo tâm"                          # na yathācittassa kāyakammaṃ
F5 = [PHASSA, B.VEDANA, B.SANNA, "chủ ý", "tâm"]          # (a)phassaka (a)vedanaka (a)saññaka (a)cetanaka (a)cittaka


def of(what, who):
    return f"{what} của người {who}"


VARN = f" [{VAR} (Pī.): anāvaṭṭantassa; (Sī., Syā., Ka.): anāvajjantassa; cần xem Các vấn đề tranh luận 484]"
# [anāvaṭṭantassa (pī.), anāvajjantassa (sī. syā. ka.) kathā. 484 passitabbaṃ] (passitabbaṃ «cần xem» ch10;
# kathā. = this book)
NAV, NAB, NPA = "không hướng đến", "không có sự chú hướng", "không mong cầu"   # anāvaṭṭentassa anābhogassa appaṇidahantassa
YAV, YAB, YPA = "hướng đến", "có sự chú hướng", "mong cầu"                      # āvaṭṭentassa ābhogassa paṇidahantassa
SAM = "do tâm sinh ra, cùng sinh với tâm, sinh khởi cùng một lúc với tâm"
# cittasamuṭṭhāna cittena sahajāta cittena saha ekuppāda (pi-1 «do tâm sinh ra»; sahajāta «cùng sinh với» ch11)
SP4 = ["phát biểu", "kể", "trò chuyện", "nói"]             # bhaṇati katheti ālapati voharati (voharati «nói» ch10)
NEGW = ", ".join(f"người không muốn {v} mà {v}" for v in SP4)
POSW = ", ".join(f"người muốn {v} thì {v}" for v in SP4)
SP4_OBJ = ["phát biểu", "kể", "trò chuyện về", "nói"]


def other(v):
    """"aññaṃ V-issāmī"ti aññaṃ V-ti"""
    return f"nghĩ “tôi sẽ {v} điều này” rồi {v} điều khác"


MV = ["đi tới", "đi lui", "nhìn thẳng", "nhìn quanh", "co lại", "duỗi ra"]    # abhikkamati … pasāreti (ch14, pi-2)
NEGM = ", ".join(f"người không muốn {v} mà {v}" for v in MV)
POSM = ", ".join(f"người muốn {v} thì {v}" for v in MV)
POSM_PE = f"người muốn {MV[0]} thì {MV[0]}… người muốn {MV[-1]} thì {MV[-1]}"
GO = "nghĩ “tôi sẽ đi đến chỗ này” rồi đi đến chỗ khác"   # "aññatra gacchissāmī"ti aññatra gacchati
ST = "nghĩ “tôi sẽ duỗi cái này” rồi duỗi cái khác"       # "aññaṃ pasāressāmī"ti aññaṃ pasāreti

# ================================================================ (94) Atītānāgatasamannāgata
SMN = "được trang bị"                                     # samannāgato (ch12)
T11 = f"{SMN} {T_['a']} và {T_['f']}"                     # atītānāgatehi samannāgato
KX11 = f"sự {T11}"                                        # Atītānāgatasamannāgatakathā (ch12 «sự được trang bị»)
ROWS = [("khối vật chất", "năm khối", "mười lăm khối"),
        (B.AYATANA[0], "mười hai lĩnh vực nhận biết", "ba mươi sáu lĩnh vực nhận biết"),
        (B.DHATU[0], "mười tám yếu tố", "năm mươi bốn yếu tố"),
        (B.INDRIYA[0], "hai mươi hai năng lực", "sáu mươi sáu năng lực")]
# rūpakkhandha / pañca khandhā / pannarasa; cakkhāyatana / dvādasa / chattiṃsa; cakkhudhātu / aṭṭhārasa /
# catupaññāsa; cakkhundriya / bāvīsati / chasaṭṭhi (ch5 ^5-287 counts)


def three(sg, pl, total):
    a = ", ".join(f"{SMN} {sg} thuộc {T_[t]}" for t in "afp")
    c = ", ".join(f"{SMN} {pl} thuộc {T_[t]}" for t in "afp")
    return f"{Q(a)} {AM} {Q(f'{SMN} ba {sg}')} {NHP} {q(c)} {AM} {Q(f'{SMN} {total}')} {NHP}"


LABHI = ("có người tu thiền với tám sự giải thoát, đạt được bốn tầng thiền theo ý muốn, đạt được chín thành tựu "
         "thiền an trú tuần tự")
# atthi aṭṭhavimokkhajhāyī catunnaṃ jhānānaṃ nikāmalābhī navannaṃ anupubbavihārasamāpattīnaṃ lābhī (aṭṭha vimokkhā
# «tám sự giải thoát» pi-4; nikāmalābhī «đạt được … theo ý muốn» pi-2; «chín thành tựu thiền an trú tuần tự» pi-2)

# ================================================================ vagga close (ch9 frame)
UDDANA = (f"{cap(f'sự dứt bỏ {SAMY} của {ANI}')}, {T2}, {T3}, {T4}, cũng vậy, {NANA}, "
          f"tâm có đối tượng thuộc {T_['a']} và {T_['f']}, {T7}, {T8}, {T9}, {KK} cũng vậy, {T11}.")
# Ānisaṃsadassāvissa saṃyojanānaṃ pahānaṃ, amatārammaṇaṃ saṃyojanaṃ, rūpaṃ sārammaṇaṃ, anusayā anārammaṇā,
# evamevaṃ ñāṇaṃ, atītānāgatārammaṇaṃ cittaṃ, sabbaṃ cittaṃ vitakkānupatitaṃ, sabbaso … saddo, na yathācittassa
# vācā, tatheva kāyakammaṃ [missing comma] atītānāgatehi samannāgatoti.  (evameva «cũng vậy» ch11; tatheva
# kāyakammaṃ = «nghiệp bằng thân cũng vậy» ch14; uddāna X-assa Y = «Y của X» ch13)


def build():
    d = B.Doc()
    d.head(3, VAGGA9, "5-17-0")
    # ------------------------------------------------------------ (84) Ānisaṃsadassāvī
    d.head(4, f"(84) 1. {K(x=ANI)}", "5-17-1-0")
    v0, vl = TO[0], TO[-1]
    d.seg("5-547",
          f"{Q(T1)} {AM} {NANU(mk(v0))} {AM} {HNO(mk(v0), T1)}",
          f"{NANU(mk(CHAIN_TO))} {AM} {HNO(mk(vl), T1)}",
          f"{Q(both(v0))} {NHP} {q(both(v0))} {AM} {Q(TWO_PE)} {NHP} {q(both(f'{TO[1]}… {vl}'))} {NHP} "
          f"{q(both(vl))} {AM} {Q(TWO_PE)} {NHP}")
    d.seg("5-548",
          f"{NVQ(T1)} {AM} {B.NANU_VUTTAM} “{SUTTA_AN}” [Tăng Chi Bộ Kinh 7.19]! {B.ATTHEVA} {AM} {TENA_HI(T1)}",
          E(x=ANI))
    # ------------------------------------------------------------ (85) Amatārammaṇa
    for lv, t, sid in heads(2, 85, KX2):
        d.head(lv, t, sid)

    def amata_line(subj, pos, neg, neg_pe):
        th = arb(AMATA, subj)
        return (f"{Q(th)} {AM} {Q(f'{AMATA} {pos}')} {NHP} {nanu_lc(f'{AMATA} {neg}')} {AM} "
                f"{HNO(f'{AMATA} {neg_pe}', th)}")

    d.seg("5-549",
          f"{Q(T2)} {AM} {Q(f'{AMATA} {OBJ_ALL}')} {NHP} {nanu_lc(f'{AMATA} {NOBJ_2PE}')} {AM} "
          f"{HNO(f'{AMATA} {NOBJ_1PE}', T2)}",
          amata_line(RAGA, RG, NRG, NRG),
          amata_line(DOSA, DS, NDS, NDS),
          amata_line(MOHA, MH, NMH, NMH_PE))

    def pair2(o1, o2, subj, p1, p2):
        return (f"{Q(f'{arb(o1, subj)}, {o1} {p1}')} {AM} {Q(f'{arb(o2, subj)}, {o2} {p2}')} {NHP}")

    d.seg("5-550",
          pair2(RUPA, AMATA, SAMY, OBJ_2PE, OBJ_1PE),
          pair2(RUPA, AMATA, RAGA, RG, RG_PE),
          pair2(RUPA, AMATA, DOSA, DS, DS),
          pair2(RUPA, AMATA, MOHA, MH_PE, MH_PE),
          pair2(AMATA, RUPA, SAMY, NOBJ_ALL, NOBJ_2PE),
          pair2(AMATA, RUPA, RAGA, NRG, NRG_PE),
          pair2(AMATA, RUPA, DOSA, NDS, NDS),
          pair2(AMATA, RUPA, MOHA, NMH_PE, NMH_PE))
    d.seg("5-551",
          f"{NVQ(T2)} {AM} {B.NANU_VUTTAM} “{SUTTA_MN}” [Trung Bộ Kinh 1.6]! {B.ATTHEVA} {AM} {TENA_HI(T2)}",
          E(x=KX2))
    # ------------------------------------------------------------ (86) Rūpaṃ sārammaṇaṃ
    for lv, t, sid in heads(3, 86, f"việc cho rằng {T3}"):
        d.head(lv, t, sid)
    d.seg("5-552",
          f"{Q(T3)} {AM} {Q(f'nó có {AV7}')} {NHP} {nanu_lc(f'nó không có {AV_PE}')} {AM} "
          f"Nếu nó không có {AV_PE}, {NCV} “{T3}”.",
          f"{Q(f'{PHASSA} {SA}, nó có {AV_PE}')} {AM} {Q(f'{T3}, nó có {AV_PE}')} {NHP}",
          f"{Q(f'{L19} {SA}, nó có {AV_PE}')} {AM} {Q(f'{T3}, nó có {AV_PE}')} {NHP}",
          f"{Q(f'{T3}, nó không có {AV_PE}')} {AM} {Q(f'{PHASSA} {SA}, nó không có {AV_PE}')} {NHP}",
          f"{Q(f'{T3}, nó không có {AV_PE}')} {AM} {Q(f'{L19_PE} {SA}, nó không có {AV_PE}')} {NHP}")
    d.seg("5-553",
          f"{NVQ(T3)} {AM} {NANU(f'{RUPA} có điều kiện')} {AM} {B.hanci(f'{RUPA} có điều kiện', T3)}",
          E(x=f"việc cho rằng {T3}"))
    # ------------------------------------------------------------ (87) Anusayā anārammaṇā
    for lv, t, sid in heads(4, 87, T4):                   # heading as written (no -ti); closing has -ti
        d.head(lv, t, sid)
    d.seg("5-554",
          f"{Q(T4)} {AM} {Q(RN)} {NHP}",
          f"{Q(f'{KRA} {ANA}')} {AM} {Q(f'{KR6} {ANA}')} {NHP} {q(f'{KR6} {SA}')} {AM} {Q(f'{KRA} {SA}')} {NHP}",
          *anusaya_block(KRA, KR1))
    d.seg("5-555",
          f"{Q(f'{AN_REST} {ANA}')} {AM} {Q(f'{AVJ7} {ANA}')} {NHP} {q(f'{AVJ_PE} {SA}')} {AM} "
          f"{Q(f'{AVA} {SA}')} {NHP}",
          *anusaya_block(AVA, AVJ))
    d.seg("5-556",
          f"{NVQ(T4)} {AM} {Q(f'{KUS}, {PU} nên được gọi là có khuynh hướng tiềm ẩn')} {AM} "
          f"{Q(f'{C2.ANUSAYA} ấy {SA}')} {NHP} {tena_hi_lc(T4)} "
          f"{Q(f'{KUS}, {PU} nên được gọi là có tham đắm')} {AM} {Q(f'{RAGA} ấy {SA}')} {NHP} "
          f"{TENA_HI(f'{RAGA} {ANA}')}",
          E(x=f"việc cho rằng {T4}"))
    # ------------------------------------------------------------ (88) Ñāṇaṃ anārammaṇaṃ
    for lv, t, sid in heads(5, 88, f"việc cho rằng {T5}"):
        d.head(lv, t, sid)
    d.seg("5-557",
          f"{Q(T5)} {AM} {Q(RN)} {NHP} {q(T5)} {AM} {Q(f'{PN5} {ANA}')} {NHP} {q(f'{PN5} {SA}')} {AM} "
          f"{Q(f'{NANA} {SA}')} {NHP}",
          f"{Q(T5)} {AM} {KATAMA} {SKP_ANS} {Q(f'{SKK} {ANA}')} {NHP} {q(f'{SKK} {ANA}')} {AM} "
          f"{Q(f'{VSV} {ANA}')} {NHP} {q(f'{NANA} {SKP} {ANA}')} {AM} {Q(f'{PANNA} {SKP} {ANA}')} {NHP} "
          f"{q(f'{PANNA} {SKP} {SA}')} {AM} {Q(f'{NANA} {SKP} {SA}')} {NHP}",
          f"{Q(f'{NANA} {SKP} {ANA}, {PANNA} {SKP} {SA}')} {AM} {Q(part(SKK))} {NHP} {q(part(SKK))} {AM} "
          f"{Q(part(VSV))} {NHP}")
    d.seg("5-558",
          f"{NVQ(T5)} {AM} {Q(f'{ARAHA_C} nên được gọi là người có {NANA}')} {AM} {Q(f'{NANA} ấy {SA}')} {NHP} "
          f"{tena_hi_lc(T5)} {Q(f'{ARAHA_C} nên được gọi là người có {PANNA}')} {AM} {Q(f'{PANNA} ấy {SA}')} "
          f"{NHP} {TENA_HI(f'{PANNA} {ANA}')}",
          E(x=f"việc cho rằng {T5}"))
    # ------------------------------------------------------------ (89) Atītānāgatārammaṇa
    for lv, t, sid in heads(6, 89, KX6):
        d.head(lv, t, sid)

    def av_line(t):
        th = f"{CIT[t]} {ANA}"
        return f"{Q(th)} {AM} {NANU(arb_av(t))} {AM} {HNO(arb_av(t), th)}"

    def cross(t1, t2, sa):
        return f"{arb_av(t1)}, {CIT[t1]} {sa}"

    d.seg("5-559", micchā_line("a"), av_line("a"))
    d.seg("5-560",
          micchā_line("f"),
          av_line("f"),
          f"{Q(cross('p', 0, SA))} {AM} {Q(cross('a', 0, SA))} {NHP} {q(cross('p', 0, SA))} {AM} "
          f"{Q(cross('f', 0, SA))} {NHP}",
          f"{Q(cross('a', 0, ANA))} {AM} {Q(cross('p', 0, ANA))} {NHP}",
          f"{Q(cross('f', 0, ANA))} {AM} {Q(cross('p', 0, ANA))} {NHP}")
    af_none = f"{T_['a']} và {T_['f']} không tồn tại"     # atītānāgataṃ natthi (atthi «tồn tại» sample, ch5)
    d.seg("5-561",
          f"{NVQ(T6)} {AM} {NANU(af_none)} {AM} Nếu {af_none}, {TV} “{T6}”…",
          E(x=KX6))
    # ------------------------------------------------------------ (90) Vitakkānupatita
    for lv, t, sid in heads(7, 90, KX7):
        d.head(lv, t, sid)
    l95 = ", ".join(anup(x) for x in L95) + f"… {anup(C2.AO)}"
    d.seg("5-562",
          f"{Q(T7)} {AM} {Q(f'tất cả tâm đều {l95}')} {NHP}",
          f"{Q(T7)} {AM} {NANU(f'có {S2}')} {AM} {HNO(f'có {S2}', T7)}",
          f"{Q(T7)} {AM} {NANU(f'có {S3}')} {AM} {HNO(f'có {S3}', T7)} {Q(T7)} {AM} "
          f"{NANU(f'{BS3} [Trường Bộ Kinh 3.305, 353]')} {AM} {HNO(BS3, T7)}",
          E(x=KX7))
    # ------------------------------------------------------------ (91) Vitakkavipphārasadda
    for lv, t, sid in heads(8, 91, VS_):
        d.head(lv, t, sid)
    d.seg("5-563",
          f"{Q(T8)} {AM} {Q(', '.join(vipp(a, x) for a, x in V7))} {NHP}",
          f"{Q(T8)} {AM} {Q(f'{VS_} {LD_EAR}')} {NHP} {NANU(f'{VS_} {NLD_EAR}')} {AM} "
          f"{HNO(f'{VS_} {NLD_EAR}', T8)}",
          E(x=VS_))
    # ------------------------------------------------------------ (92) Na yathācittassa vācā
    for lv, t, sid in heads(9, 92, f"việc cho rằng {T9}"):
        d.head(lv, t, sid)
    neg5 = ", ".join(of("lời nói", f"không có {x}") for x in F5)
    pos5 = ", ".join(of("lời nói", f"có {x}") for x in F5)
    pos5_pe = f"{of('lời nói', f'có {F5[0]}')}… {of('lời nói', f'có {F5[-1]}')}"
    av_neg = f"{of('lời nói', NAV)}{VARN}… {of('lời nói', NAB)}… {of('lời nói', NPA)}"
    av_pos_pe = f"{of('lời nói', YAV)}, {of('lời nói', YAB)}… {of('lời nói', YPA)}"
    av_pos = f"{of('lời nói', YAV)}, {of('lời nói', YAB)}, {of('lời nói', YPA)}"
    oth = [other(v) for v in SP4_OBJ]
    d.seg("5-564",
          f"{Q(T9)} {AM} {Q(f'có {neg5}')} {NHP} {nanu_lc(f'có {pos5}')} {AM} {HNO(f'có {pos5_pe}', T9)}",
          f"{Q(T9)} {AM} {Q(f'có {av_neg}')} {NHP} {nanu_lc(f'có {av_pos_pe}')} {AM} {HNO(f'có {av_pos}', T9)}",
          f"{Q(T9)} {AM} {NANU(f'lời nói {SAM}')} {AM} {HNO(f'lời nói {SAM}', T9)}",
          f"{Q(T9)} {AM} {Q(NEGW)} {NHP} {nanu_lc(POSW)} {AM} {HNO(POSW, T9)}")
    d.seg("5-565",
          f"{NVQ(T9)} {AM} {NANU('có ai đó ' + ', '.join(oth))} {AM} Nếu có ai đó {oth[0]}… {oth[-1]}, "
          f"{TV} “{T9}”.",
          E(x=f"việc cho rằng {T9}"))
    # ------------------------------------------------------------ (93) Na yathācittassa kāyakammaṃ
    for lv, t, sid in heads(10, 93, f"việc cho rằng {T10}"):
        d.head(lv, t, sid)
    k_neg = f"{of(KK, f'không có {F5[0]}')}… {of(KK, f'không có {F5[-1]}')}"
    k_pos = f"{of(KK, f'có {F5[0]}')}… {of(KK, f'có {F5[-1]}')}"
    k_avn = f"{of(KK, NAV)}… {of(KK, NPA)}"
    k_avp = f"{of(KK, YAV)}… {of(KK, YPA)}"
    d.seg("5-566",
          f"{Q(T10)} {AM} {Q(f'có {k_neg}')} {NHP} {nanu_lc(f'có {k_pos}')} {AM} {HNO(f'có {k_pos}', T10)}",
          f"{Q(T10)} {AM} {Q(f'có {k_avn}')} {NHP} {nanu_lc(f'có {k_avp}')} {AM} {HNO(f'có {k_avp}', T10)}",
          f"{Q(T10)} {AM} {NANU(f'{KK} {SAM}')} {AM} {HNO(f'{KK} {SAM}', T10)}",
          f"{Q(T10)} {AM} {Q(NEGM)} {NHP} {NANU(POSM)} {AM} {HNO(POSM_PE, T10)}")
    d.seg("5-567",
          f"{NVQ(T10)} {AM} {NANU(f'có ai đó {GO}… {ST}')} {AM} Nếu có ai đó {GO}… {ST}, {TV} “{T10}”.",
          E(x=f"việc cho rằng {T10}"))
    # ------------------------------------------------------------ (94) Atītānāgatasamannāgata
    for lv, t, sid in heads(11, 94, KX11):
        d.head(lv, t, sid)
    ta, tf = f"{SMN} {T_['a']}", f"{SMN} {T_['f']}"
    pa, pf = f"{T_['a']} {C5.PAST5}", f"{T_['f']} {C5.FUT6}"
    d.seg("5-568",
          f"{Q(ta)} {AM} {NANU(pa)} {AM} {HNO(pa, ta)}",
          f"{Q(tf)} {AM} {NANU(pf)} {AM} {HNO(pf, tf)}")
    d.seg("5-569", *(three(*r) for r in ROWS))
    d.seg("5-570",
          f"{NVQ(T11)} {AM} {NANU(LABHI)} {AM} Nếu {LABHI}, {TV} “{T11}”.",
          E(x=KX11),
          f"{VAGGA9}.",
          C9.TASSUDDANAM,
          UDDANA)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("Các hiện tượng có đối tượng", 1), ("không có đối tượng", 1), ("có đối tượng thuộc quá khứ", 1),
    ("lấy các hiện tượng thuộc quá khứ làm đối tượng", 1), ("sinh khởi khi lấy", 1),
    ("không có sự hướng tâm, chỉ có sự duy trì tâm", 1), (S1, 2), (S3, 2), ("do tâm sinh ra", 1),
    ("sự hướng đến, sự chú hướng, sự lưu ý hay sự chú tâm", 2), ("sự mong muốn", 1),
    ("trí tuệ, năng lực trí tuệ, sức mạnh trí tuệ", 1), ("chi phần giác ngộ là sự tìm hiểu các hiện tượng", 1),
    ("tám sự giải thoát", 4), ("đạt được định tâm theo ý muốn", 2), ("chín thành tựu thiền an trú tuần tự", 2),
    ("khi đi tới, khi đi lui", 2), ("khi nhìn thẳng, khi nhìn quanh", 2), ("người có trí tuệ", 2),
    ("thiện và không xác định về mặt đạo đức", 1), ("khối tạo tác", 2), ("khối cảm giác", 2), ("khối thức", 2),("sự không đi sâu", 1),
    ("không phải là tự ngã", 2), ("có bản chất biến đổi", 2), ("bền vững", 2), ("người phàm phu", 1),
    ("sống quán sát thân", 2), ("sự hân hoan", 1), ("có hạnh phúc", 1),
    ("năng lực niềm vui, năng lực nỗi buồn, năng lực bình thản", 2), ("sự tìm hiểu các hiện tượng", 1),
    ("Tăng Chi Bộ Kinh", 4), ("Trung Bộ Kinh", 4), ("Trường Bộ Kinh", 4), ("nhận ra", 1), ("có cảm giác", 1),
    ("có tri giác", 1), ("có chủ ý", 1), ("có tâm", 1), ("thức qua mắt", 2), ("tầng thiền", 2),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (RG, "10-dutiyavaggo.md"), (NRG, "10-dutiyavaggo.md"), (DS, "10-dutiyavaggo.md"), (NDS, "10-dutiyavaggo.md"),
    (MH, "10-dutiyavaggo.md"), (NMH, "10-dutiyavaggo.md"), (LD_EAR, "10-dutiyavaggo.md"),
    (NLD_EAR, "10-dutiyavaggo.md"), (AVJ7, "10-dutiyavaggo.md"), ("đã được thấy là vô thường", "10-dutiyavaggo.md"),
    ("nên được gọi là", "10-dutiyavaggo.md"), ("thuộc về con đường", "10-dutiyavaggo.md"),
    ("điều bất tử", "10-dutiyavaggo.md"), ("nơi che chở, nơi ẩn náu, nơi nương tựa", "14-chatthavaggo.md"),
    ("cần xem", "10-dutiyavaggo.md"), ("Có phải có hai", "10-dutiyavaggo.md"),
    ("lấy sự trống rỗng làm đối tượng", "11-tatiyavaggo.md"), ("vừa chú tâm đến", "11-tatiyavaggo.md"),
    ("có sự tụ hợp của hai sự tiếp xúc, hai tâm", "11-tatiyavaggo.md"), ("cùng sinh với", "11-tatiyavaggo.md"),
    ("Đức Thế Tôn đã nói đến ba mắt", "11-tatiyavaggo.md"), ("một phần đã được giải thoát", "11-tatiyavaggo.md"),
    ("có sự tiếp xúc", "11-tatiyavaggo.md"), ("Trường Bộ Kinh", "11-tatiyavaggo.md"),
    ("thường xuyên, liên tục, liền mạch", "12-catutthavaggo.md"), ("Bàn về sự được trang bị", "12-catutthavaggo.md"),
    ("bốn chủ ý, bốn tâm, bốn niềm tin, bốn sự tinh tấn, bốn sự tỉnh thức, bốn sự định tâm, bốn trí tuệ",
     "12-catutthavaggo.md"),
    ("Bàn về đối tượng là tâm", "13-pancamavaggo.md"), ("nhập vào đất như là đất", "13-pancamavaggo.md"),
    ("người có được thành quả", "13-pancamavaggo.md"), ("cố ý", "13-pancamavaggo.md"),
    ("hiểu rõ", "13-pancamavaggo.md"),
    ("đang đi tới, đang đi lui, đang nhìn thẳng, đang nhìn quanh, đang co lại, đang duỗi ra", "14-chatthavaggo.md"),
    ("nghiệp bằng thân", "14-chatthavaggo.md"), ("cũng vậy.", "14-chatthavaggo.md"),
    ("Có phải có mười lăm khối không?", "5-sabbamatthitikatha.md"), ("năm mươi bốn yếu tố", "5-sabbamatthitikatha.md"),
    ("sáu mươi sáu năng lực", "5-sabbamatthitikatha.md"), ("mười hai lĩnh vực nhận biết thuộc quá khứ", "5-sabbamatthitikatha.md"),
    ("thì nói rằng", "5-sabbamatthitikatha.md"), (C5.PAST5, "5-sabbamatthitikatha.md"),
    (C5.FUT6, "5-sabbamatthitikatha.md"),
    (C2.KR, "2-parihanikatha.md"), (C2.AN7, "2-parihanikatha.md"),
    ("Tóm tắt của chương này –", "9-hevatthikatha.md"),
    ("lấy tất cả các hiện tượng làm đối tượng", "8-satipatthanakatha.md"),
    ("[Tương Ưng Bộ Kinh 2.124]! Có bài kinh như vậy thật không?", "1-puggalakatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(st, f"pi-{b}") for st, b in CROSS if st not in texts[b]]
    missing += [(st, f) for st, f in PI5 if st not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for st, w in missing:
        print(f"CROSS MISSING in {w}: {st}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch17 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
