# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 13: 13-pancamavaggo.md (Pañcamavaggo, ^5-13-0 … ^5-444),
the kathā (43) Vimutti … (52) Phalañāṇa, the uddāna of the fifth vagga and the uddāna of the Mahāpaṇṇāsaka.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame, and build_10_vi /
build_2_vi (finished, read-only) for the shared vagga strings, kasiṇa / arūpa names, paṭipanna persons and the
uddāna frame, so identical Pāli gets byte-identical Vietnamese. Strings claimed from the pi-1..4 rails are
asserted to occur there; strings taken from finished pi-5 chapters are asserted in those output files; the
sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli. Every Pāli
sentence keeps its own sentence.

run:  python -I -X utf8 build_13_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (ch2: DEV6, FRUIT)
import build_10_vi as C10    # noqa: E402  (ch10: PAT, KAS, ARU, REQ, TASSUDDANAM)

NAME = "13-pancamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP, AM_PE = B.NA_HEVAM, B.NA_HEVAM_PE, B.AMANTA_PE
ATTHEVA, NANU_VUTTAM, TENA_HI = B.ATTHEVA, B.NANU_VUTTAM, B.TENA_HI
NAVQ, TENA_VATA, NO_CA_VATA = B.NA_VATTABBAM_Q, B.TENA_VATA, B.NO_CA_VATA
VAR, SPELL = B.VAR, B.SPELL
KATHA, KATHA_END = B.KATHA, B.KATHA_END
VAGGA5 = B.VAGGA[5]                                    # Pañcamavaggo = «Chương thứ năm» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                          # Tassuddānaṃ – (ch9 / ch10, byte for byte)
nanca, hanci = C10.nanca, C10.hanci                    # Hañci P, no ca / tena vata re vattabbe – "Q"ti.


def pair(a, b, end=NHP, ans=AM):
    return f"{Q(a)} {ans} {Q(b)} {end}"


def nanu_l(x):
    """nanu Xti? after …pe… (lowercase start)"""
    return f"chẳng phải {x} sao?"


# ================================================================ persons, fruits (pi-1, pi-4, ch2, ch10)
AR = C10.AR                                            # arahā = bậc A-la-hán (pi-4)
PAT = C10.PAT                                          # X-sacchikiriyāya paṭipanno (pi-4, ch3, ch10)
FR = {"sota": C2.FRUIT[C2.SO], "saka": C2.FRUIT[C2.SA], "ana": C2.FRUIT[C2.AN], "ara": C2.FRUIT[C2.AR]}
NOBLE = {"sota": C2.SO, "saka": C2.SA, "ana": C2.AN, "ara": C2.AR}   # sotāpanno … arahā (pi-4)
SAMANGI = {"sota": "người có được thành quả vào dòng", "saka": "người có được thành quả trở lại một lần",
           "ana": "người có được thành quả không trở lại", "ara": "người có được thành quả A-la-hán"}
# X-phalasamaṅgī puggalo (pi-1 phalasamaṅgissa ñāṇaṃ «hiểu biết của người có được thành quả»; arahattaphala ch10)
GOTRA = "người chuyển đổi dòng dõi"                    # gotrabhū puggalo (pi-4 ^4-10)
STAGES = ("sota", "saka", "ana", "ara")
ATT = "đã có được, đã chứng đắc, đã tự mình chứng nghiệm"   # paṭiladdhassa adhigatassa sacchikatassa (ch3)
SOTA_MAGGA = "con đường vào dòng"                      # sotāpattimagga (pi-2, ch4)
DEV6 = C2.DEV6                                         # satipaṭṭhānā … bojjhaṅgā (pi-3, ch2)

# ================================================================ (43) Vimuttikathā
VIMUTTI = "sự giải thoát"                              # vimutti (terms file heading)
VM = f"hiểu biết về {VIMUTTI}"                         # vimuttiñāṇaṃ (ñāṇa «hiểu biết» pi-1, ch5)
VD = "được giải thoát"                                 # vimuttaṃ (pi-2 vimuttaṃ cittaṃ «tâm được giải thoát»)
PACC = "hiểu biết xem xét lại"                         # paccavekkhaṇañāṇaṃ (pi-1 apaccavekkhaṇā «sự không xem xét lại»)
PHALA_PATTA = "và nó là hiểu biết của người đã đạt đến thành quả"   # tañca phalaṃ pattassa ñāṇaṃ


def vm(who):
    return f"{VM} của {who} {VD}"


def kn(s):
    """Sotāpannassa ñāṇaṃ, sotāpattiphalaṃ pattassa paṭiladdhassa adhigatassa sacchikatassa ñāṇanti?"""
    return f"là hiểu biết của {NOBLE[s]}, hiểu biết của người đã đạt đến {FR[s]}, {ATT}"


# ================================================================ (44) Asekhañāṇakathā
SE = "người còn đang tu học"                           # sekho (pi-1 sekkhā dhammā)
ASE = "người đã hoàn tất tu học"                       # asekho (pi-1 asekkhā dhammā)
AK = f"hiểu biết thuộc về {ASE}"                       # asekhaṃ ñāṇaṃ (heading)
AD = f"hiện tượng thuộc về {ASE}"                      # asekhaṃ dhammaṃ
T44 = f"{SE} có {AK}"                                  # sekhassa asekhaṃ ñāṇaṃ atthi


def know(w, neg=False):
    """X asekhaṃ dhammaṃ (na) jānāti (na) passati, (a)diṭṭhaṃ (a)viditaṃ (a)sacchikataṃ (na) upasampajja
    viharati, (na) kāyena phusitvā viharati (upasampajja viharati / kāyena phusitvā viharati ch3)"""
    if neg:
        return (f"{w} không biết, không thấy {AD}, không chứng nhập và an trú trong điều chưa thấy, chưa biết, "
                "chưa tự mình chứng nghiệm, không chạm đến bằng thân rồi an trú")
    return (f"{w} biết, thấy {AD}, chứng nhập và an trú trong điều đã thấy, đã biết, đã tự mình chứng nghiệm, "
            "chạm đến bằng thân rồi an trú")


ANANDA = "tôn giả A-nan, người còn đang tu học"         # āyasmā ānando sekho (āyasmā ch5; Ānanda sample)
UL1 = "“Đức Thế Tôn là bậc vĩ đại”"                    # "bhagavā uḷāro"ti
UL2 = "“trưởng lão Xá-lợi-phất, trưởng lão Đại Mục-kiền-liên là bậc vĩ đại”"   # (ch2 names)
KNOW2 = f"biết {UL1}, biết {UL2}"

# ================================================================ (45) Viparītakathā
KAS, ARU = C10.KAS, C10.ARU                            # kasiṇa / arūpa names (pi-1, pi-2, ch10)
K0 = f"người đang nhập thành tựu thiền với {KAS[0]}"   # pathavīkasiṇaṃ samāpattiṃ samāpannassa (ch10)
K0V = f"{K0} [{SPELL} (Sī., Ka.): pathavīkasiṇasamāpattiṃ]"
VIPARITA = "điều sai lệch"                             # viparīta (heading); viparītaṃ hoti = trở thành sai lệch
VK = f"hiểu biết về {VIPARITA}"                        # viparīte ñāṇaṃ (locative = «về», as anāgate / phale ñāṇaṃ)
T45 = f"{K0} có {VK}"
T45A = f"{T45}, và nó là bất thiện"                    # …viparīte ñāṇaṃ, tañca akusalaṃ
VIP = "sự đảo ngược"                                   # vipariyeso (pi-2 vipariyāsā «sự đảo ngược»)
VS = ["thường còn đối với điều vô thường", "hạnh phúc đối với điều khổ đau",
      "tự ngã đối với điều không phải tự ngã", "đẹp đối với điều không đẹp"]
# anicce niccanti / dukkhe sukhanti / anattani attāti / asubhe subhanti (pi-2 ^2-936)
V3 = f"{VIP} về tri giác, {VIP} về tâm, {VIP} về quan điểm"   # saññā- / citta- / diṭṭhivipariyeso
AR_SAM = f"{AR} có thể nhập thành tựu thiền với {KAS[0]}"     # arahā pathavīkasiṇaṃ samāpattiṃ samāpajjeyya
EARTH = "đất tồn tại, và có ai đó nhập vào đất như là đất"   # pathavī atthi, atthi ca koci pathaviṃ pathavito samāpajjati


def vp(i, k=None):
    """X-e Y-nti vipariyeso (, so ca kusalo / akusalo)"""
    s = f"là {VIP} rằng {VS[i]}"
    return f"{s}, và nó là {k}" if k else s


# ================================================================ (46) Niyāmakathā
NIYAMA = "sự cố định"                                  # niyāmo (terms file (53); pi-2 niyāmaṃ okkamati)
AN_P, NI_P = "người không cố định", "người cố định"   # aniyato / niyato (pi-1 aniyatā / niyatā dhammā)
G, AG = f"để đi đến {NIYAMA}", "để đi đến sự không cố định"   # niyāmagamanāya / aniyāmagamanāya
HB = "hiểu biết"                                       # ñāṇaṃ


def ny(w, x, goal, has=True):
    return f"{w} {'có' if has else 'không có'} {x} {goal}"


T46 = ny(AN_P, HB, G)
BJ = ("người này sẽ bước vào sự cố định theo hướng đúng đắn, người này có khả năng thấu hiểu Giáo Pháp")
# ayaṃ puggalo sammattaniyāmaṃ okkamissati, bhabbo ayaṃ puggalo dhammaṃ abhisametuṃ (pi-1, pi-2, ch2, ch4)

# ================================================================ (47) Paṭisambhidā / (48) Sammutiñāṇa
PS = "hiểu biết thông suốt"                            # paṭisambhidā (pi-2)
ALLK, ALLP = "tất cả hiểu biết", "tất cả trí tuệ"      # sabbaṃ ñāṇaṃ / sabbā paññā (ch8 «tất cả … là …»)
SAMK = "hiểu biết theo quy ước"                        # sammutiñāṇaṃ (pi-2)
CETO = "hiểu biết bao quát tâm"                        # cetopariyāye ñāṇaṃ (pi-2 pariye ñāṇaṃ)
GM = C10.REQ.split(", ")[-1]                           # gilānapaccayabhesajjaparikkhāra (pi-2, ch10)
GIVE = ["vật bố thí", "y phục", "đồ ăn khất thực", "chỗ ở", GM]   # dānaṃ / cīvaraṃ … dadantassa


def has_p(w):
    """X-assa atthi paññā, sā paññā paṭisambhidā"""
    return f"{w} có trí tuệ, trí tuệ ấy là {PS}"


def sam(x):
    return f"người đang nhập {x}"


def give(x):
    return f"người đang dâng {x}"


SC = f"{SAMK} chỉ có sự thật làm đối tượng, không có điều khác làm đối tượng"
# sammutiñāṇaṃ saccārammaṇaññeva na aññārammaṇaṃ
SCC = "sự thật quy ước"                                # sammutisacca (sammutisaccamhi = thuộc về …)
FOUR = "nhờ hiểu biết ấy mà hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, tu tập con đường"
# tena ñāṇena dukkhaṃ parijānāti … maggaṃ bhāveti (ch5, pi-2)

# ================================================================ (49) Cittārammaṇakathā
CITTAR = "đối tượng là tâm"                            # cittārammaṇa (heading)
CS = f"{CETO} chỉ có tâm làm đối tượng, không có điều khác làm đối tượng"
CIT = ["có tham đắm", "đã lìa tham đắm", "có sân hận", "đã lìa sân hận", "có si mê", "đã lìa si mê", "co rút",
       "tán loạn", "rộng lớn", "không rộng lớn", "còn có điều cao hơn", "không có điều gì cao hơn", "được định tâm",
       "không được định tâm", "được giải thoát", "không được giải thoát"]   # sarāgaṃ … avimuttaṃ cittaṃ (pi-2 ^2-365)
PA = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "niềm tin", "tinh tấn", "sự tỉnh thức", "định tâm",
      "trí tuệ", "sự tham đắm", "sự sân hận", "sự si mê"]   # phassa … moha (core terms, pi-1)
AOT = "sự không biết ghê sợ tội lỗi"                   # anottappa (pi-1, ch2)


def tc(i):
    return f"tâm {CIT[i]}"


def ar(x):
    """X-ārammaṇe ñāṇaṃ"""
    return f"hiểu biết về đối tượng là {x}"


def ceto_called(x, neg=False):
    """X-ārammaṇe ñāṇaṃ (na) vattabbaṃ – "cetopariyāye ñāṇa"nti"""
    return f"{ar(x)} {'không ' if neg else ''}nên được gọi là – “{CETO}”"


# ================================================================ (50) Anāgata / (51) Paṭuppanna / (52) Phala
AF = "hiểu biết về tương lai"                          # anāgate ñāṇaṃ (heading Anāgatañāṇakathā)
T50 = f"có {AF}"
FROM = ["gốc rễ", "nguyên nhân", "căn nguyên", "sự hình thành", "khởi nguồn", "nguồn gốc", "dưỡng chất",
        "đối tượng", "điều kiện", "sự phát sinh"]
# mūlato hetuto nidānato sambhavato pabhavato samuṭṭhānato āhārato ārammaṇato paccayato samudayato
PC = ["tính chất làm điều kiện nguyên nhân", "tính chất làm điều kiện đối tượng", "tính chất làm điều kiện chi phối",
      "tính chất làm điều kiện kế cận", "tính chất làm điều kiện kế cận liền ngay"]
# hetu- / ārammaṇa- / adhipati- / anantara- / samanantarapaccayataṃ (paccayatā «tính chất làm điều kiện» terms file)
SUTTA50 = ("“Này A-nan, thành Ba-liên-phất sẽ gặp ba hiểm họa – hoặc từ lửa, hoặc từ nước, hoặc từ sự chia rẽ lẫn "
           "nhau” [Đại Phẩm 286; Trường Bộ Kinh 2.152; Kinh Phật Tự Thuyết 76]!")
PATU = "hiện tại"                                      # paṭuppanna (heading Paṭuppannakathā; paccuppanna ch5)
PF = f"hiểu biết về {PATU}"                            # paṭuppanne ñāṇaṃ (closing Paṭuppannañāṇakathā)
T51 = f"có {PF}"
K1 = "nhờ hiểu biết ấy mà biết hiểu biết ấy"           # tena ñāṇena taṃ ñāṇaṃ jānāti (ch5 «nhờ hiểu biết ấy mà»)
K2 = "nhờ hiểu biết ấy mà biết hiểu biết ấy là “hiểu biết”"
K3 = "hiểu biết ấy là đối tượng của hiểu biết ấy"      # taṃ ñāṇaṃ tassa ñāṇassa ārammaṇaṃ
SELF = [("sự tiếp xúc", "chạm"), ("cảm giác", "cảm nhận"), ("tri giác", "nhận ra"), ("chủ ý", "cố ý với"),
        ("tâm", "suy nghĩ về"), ("sự hướng tâm", "hướng tâm đến"), ("sự duy trì tâm", "duy trì tâm trên"),
        ("sự hân hoan", "hân hoan với"), ("sự tỉnh thức", "ghi nhớ"), ("trí tuệ", "hiểu rõ"),
        ("thanh kiếm", "chặt"), ("cái rìu", "đẽo"), ("cái rìu nhỏ", "đẽo"), ("cái bào", "đẽo"), ("cây kim", "khâu"),
        ("đầu ngón tay", "chạm vào"), ("chóp mũi", "chạm vào"), ("đỉnh đầu", "chạm vào"), ("phân", "rửa"),
        ("nước tiểu", "rửa"), ("nước bọt", "rửa"), ("mủ", "rửa"), ("máu", "rửa")]
# tena phassena taṃ phassaṃ phusati … tena lohitena taṃ lohitaṃ dhovati (sañjānāti «nhận ra», cetanā «cố ý» pi-1;
# pajānāti «hiểu rõ» pi-2; khagga … lohita: mutta / kheḷa / pubba / lohita pi-2)
SANKH = "khi tất cả các tạo tác đã được thấy là vô thường, hiểu biết ấy cũng đã được thấy là vô thường"
# sabbasaṅkhāre aniccato diṭṭhe tampi ñāṇaṃ aniccato diṭṭhaṃ hoti (ch10 «đã được thấy là vô thường»)
SAV = "đệ tử"                                          # sāvako (ch4)
PHALA_N = "hiểu biết về thành quả"                     # phale ñāṇaṃ (heading Phalañāṇakathā)
T52 = f"{SAV} có {PHALA_N}"
PARO = ("mức độ cao thấp của các thành quả, mức độ cao thấp của các năng lực, mức độ cao thấp của các hạng người")
# phala- / indriya- / puggalaparopariyatti (pi-2 indriyaparopariyatta)
PANN = ("sự định danh về các khối, sự định danh về các lĩnh vực nhận biết, sự định danh về các yếu tố, sự định danh "
        "về các sự thật, sự định danh về các năng lực, sự định danh về các hạng người")   # (pi-4 ^4-M-1)
JINA = ("là bậc chiến thắng, bậc đạo sư, bậc Tự Giác Ngộ Hoàn Toàn, bậc toàn tri, bậc thấy tất cả, bậc làm chủ "
        "Giáo Pháp, nơi nương tựa của Giáo Pháp")
# jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo (satthā, sammāsambuddha, sabbaññutā pi-4)
MAGGA_X = ("là người làm sinh khởi con đường chưa sinh khởi, người làm sinh thành con đường chưa sinh thành, người "
           "tuyên bố con đường chưa được tuyên bố, người biết con đường, người thông hiểu con đường, người tinh thông "
           "con đường")
# anuppannassa maggassa uppādetā asañjātassa maggassa sañjanetā anakkhātassa maggassa akkhātā maggaññū maggavidū
# maggakovido (asañjāta «chưa sinh thành» ch5)
MAHAPANNASAKO = "Nhóm năm mươi lớn."                   # Mahāpaṇṇāsako. (cf. ch9 Mahāvaggo. «Chương lớn.»)
TASSAPI = "Tóm tắt của nhóm năm mươi này nữa –"        # Tassāpi uddānaṃ – (tassa = of the paṇṇāsaka, api = nữa)
UDDANA50 = ("Sự được tìm thấy của chúng sinh, người đưa đến, sức mạnh, người tại gia là bậc A-la-hán, và sự giải "
            "thoát là thứ năm.")
# Sattupaladdhiṃ, upaharato, balaṃ, gihissa arahā ca, vimuttipañcamanti. (upalabbha «sự được tìm thấy» ch9;
# satta «chúng sinh» pi-2; Gihissa arahā «người tại gia là bậc A-la-hán» terms file (33))


# ================================================================ chapter builder
def build():
    d = B.Doc()
    d.head(3, VAGGA5, "5-13-0")
    # ------------------------------------------------------------ (43) Vimuttikathā
    d.head(4, f"(43) 1. {KATHA.format(x=VIMUTTI)}", "5-13-1-0")
    l6 = [f"{Q(f'{VM} {VD}')} {AM} {Q(vm(GOTRA))} {NHP}"]
    for s in STAGES:
        l6.append(f"{q(vm(PAT[s]))} {AM} {Q(kn(s))} {NHP}")
    d.seg("5-418",
          f"{Q(f'{VM} {VD}')} {AM} {Q(f'bất cứ {VM} nào, tất cả điều ấy đều {VD}')} {NHP} "
          f"{Q(f'{VM} {VD}')} {AM} {Q(f'{PACC} {VD}')} {NHP}",
          " ".join(l6))
    d.seg("5-419",
          " ".join(f"{(Q if i == 0 else q)(vm(SAMANGI[s]))} {AM} {Q(vm(PAT[s]))} {NHP}"
                   for i, s in enumerate(STAGES)))
    d.seg("5-420",
          " ".join(f"{(Q if i == 0 else q)(f'{vm(SAMANGI[s])}, {PHALA_PATTA}')} {AM} "
                   f"{Q(f'{vm(PAT[s])}, {PHALA_PATTA}')} {NHP}" for i, s in enumerate(STAGES)),
          KATHA_END.format(x=VIMUTTI))
    # ------------------------------------------------------------ (44) Asekhañāṇakathā
    d.head(4, VAGGA5, "5-13-2-0")
    d.head(5, f"(44) 2. {KATHA.format(x=AK)}", "5-13-2-1-0")
    d.seg("5-421",
          f"{Q(T44)} {AM} {Q(know(SE))} {NHP} {nanu_l(know(SE, True))} {AM} {nanca(know(SE, True), T44)}",
          pair(f"{ASE} có {AK}, {know(ASE)}", f"{T44}, {know(SE)}"))
    d.seg("5-422",
          pair(f"{T44}, {know(SE, True)}", f"{ASE} có {AK}, {know(ASE, True)}"),
          f"{Q(T44)} {AM} {Q(f'{GOTRA} có hiểu biết về {SOTA_MAGGA}')} {NHP} "
          f"{q(f'{PAT[STAGES[0]]} có hiểu biết về {FR[STAGES[0]]}')} {NHP} {FR['saka']}… {FR['ana']}… "
          f"{q(f'{PAT[STAGES[3]]} có hiểu biết về {FR[STAGES[3]]}')} {NHP}")
    d.seg("5-423",
          f"{NAVQ(T44)} {AM} Chẳng phải {ANANDA} – {KNOW2} sao? {AM} {hanci(f'{ANANDA} – {KNOW2}', T44)}",
          KATHA_END.format(x=AK))
    # ------------------------------------------------------------ (45) Viparītakathā
    d.head(4, VAGGA5, "5-13-3-0")
    d.head(5, f"(45) 3. {KATHA.format(x=VIPARITA)}", "5-13-3-1-0")
    d.seg("5-424",
          f"{Q(f'{K0V} có {VK}')} {AM} {Q(vp(0))} {NHP} {VS[1]}… {VS[2]}… {q(vp(3))} {NHP}",
          f"{Q(T45)} {AM} {Q('là bất thiện')} {NHP} {nanu_l('là thiện')} {AM} {nanca('là thiện', T45)}",
          f"{Q(vp(0, 'bất thiện'))} {AM} {Q(T45A)} {NHP} {VS[1]}… {VS[2]}… {q(vp(3, 'bất thiện'))} {AM} "
          f"{Q(T45A)} {NHP}")
    d.seg("5-425",
          f"{Q(T45A)} {AM} {Q(vp(0, 'thiện'))} {NHP} {q(T45A)} {AM} {cap(VS[1])}… {VS[2]}… "
          f"{q(vp(3, 'thiện'))} {NHP}")
    d.seg("5-426",
          f"{Q(T45)} {AM} {Q(AR_SAM)} {AM} {nanca(AR_SAM, T45)}",
          pair(f"{T45}, {AR_SAM}", f"{AR} có {VIP}"),
          pair(f"{AR} có {VIP}", f"{AR} có {V3}"),
          f"{Q(f'{AR} không có {V3}')} {AM} {nanca(f'{AR} không có {V3}', f'{AR} có {VIP}')}")
    d.seg("5-427",
          f"Có phải không nên nói – {T45} không? {AM} "
          f"{Q(f'đối với người nhập thành tựu thiền với {KAS[0]}, tất cả đều là đất')} {NH} {TENA_HI(T45)}",
          f"{Q(T45)} {AM} {NANU(EARTH)} {AM} {nanca(EARTH, T45)}",
          f"{Q('đất tồn tại, đối với người nhập vào đất như là đất thì trở thành sai lệch')} {AM} "
          f"{Q('Niết-bàn tồn tại, đối với người nhập vào Niết-bàn như là Niết-bàn thì trở thành sai lệch')} {NHP} "
          f"vậy thì không nên nói – “{T45}”.",
          KATHA_END.format(x=VIPARITA))
    # ------------------------------------------------------------ (46) Niyāmakathā
    d.head(4, VAGGA5, "5-13-4-0")
    d.head(5, f"(46) 4. {KATHA.format(x=NIYAMA)}", "5-13-4-1-0")
    d.seg("5-428",
          pair(ny(AN_P, HB, G), ny(NI_P, HB, AG)),
          pair(ny(NI_P, HB, AG, False), ny(AN_P, HB, G, False)),
          pair(ny(AN_P, HB, G), ny(NI_P, HB, G)),
          pair(ny(NI_P, HB, G, False), ny(AN_P, HB, G, False)),
          pair(ny(AN_P, HB, G), ny(AN_P, HB, AG)),
          pair(ny(AN_P, HB, AG, False), ny(AN_P, HB, G, False)))
    no_niy = ny(AN_P, NIYAMA, G, False)
    d.seg("5-429",
          pair(T46, ny(AN_P, NIYAMA, G)),
          pair(T46, ny(AN_P, chain(DEV6), G)),
          f"{Q(no_niy)} {AM} {nanca(no_niy, T46)}",
          f"{Q(ny(AN_P, f'{DEV6[0]}… {DEV6[-1]}', G, False))} {AM} {nanca(ny(AN_P, DEV6[-1], G, False), T46)}")
    d.seg("5-430",
          f"{Q(T46)} {AM} {Q(f'{GOTRA} có hiểu biết về {SOTA_MAGGA}')} {NHP} "
          f"{q(f'{PAT[STAGES[0]]} có hiểu biết về {FR[STAGES[0]]}')} {NHP} "
          f"{q(f'{PAT[STAGES[3]]} có hiểu biết về {FR[STAGES[3]]}')} {NHP}")
    d.seg("5-431",
          f"{NAVQ(T46)} {AM} Chẳng phải Đức Thế Tôn biết – “{BJ}” sao? {AM} "
          f"{hanci(f'Đức Thế Tôn biết – “{BJ}”', T46)}",
          KATHA_END.format(x=NIYAMA))
    # ------------------------------------------------------------ (47) Paṭisambhidākathā
    d.head(4, VAGGA5, "5-13-5-0")
    d.head(5, f"(47) 5. {KATHA.format(x=PS)}", "5-13-5-1-0")
    all_ps, samk_ps, ceto_ps = f"{ALLK} là {PS}", f"{SAMK} là {PS}", f"{CETO} là {PS}"
    items = KAS[1:] + ARU[:3]
    gives = [give(x) for x in GIVE]
    d.seg("5-432",
          f"{Q(all_ps)} {AM} {Q(samk_ps)} {NHP} {q(samk_ps)} {AM} "
          f"{Q(f'bất cứ ai biết quy ước, tất cả những người ấy đều đã đạt đến {PS}')} {NHP} "
          f"{q(all_ps)} {AM} {Q(ceto_ps)} {NHP} {q(ceto_ps)} {AM} "
          f"{Q(f'bất cứ ai biết tâm người khác, tất cả những người ấy đều đã đạt đến {PS}')} {NHP}",
          f"{Q(all_ps)} {AM} {Q(f'{ALLP} là {PS}')} {NHP} {q(f'{ALLP} là {PS}')} {AM} {Q(has_p(K0))} {NHP} "
          f"{q(chain(items + [sam(ARU[3])] + gives[:-1] + [has_p(gives[-1])]))} {NHP}")
    d.seg("5-433",
          f"{NAVQ(all_ps)} {AM} {Q(f'có trí tuệ vượt thế gian, trí tuệ ấy không phải là {PS}')} {NHP} "
          f"vậy thì {all_ps}.",
          KATHA_END.format(x=PS))
    # ------------------------------------------------------------ (48) Sammutiñāṇakathā
    d.head(4, VAGGA5, "5-13-6-0")
    d.head(5, f"(48) 6. {KATHA.format(x=SAMK)}", "5-13-6-1-0")
    x1 = f"{K0} có hiểu biết, và {KAS[0]} thuộc về {SCC}"
    x2 = f"{give(GM)} có hiểu biết, và {GM} thuộc về {SCC}"
    d.seg("5-434",
          f"{NAVQ(SC)} {AM} {NANU(x1)} {AM} {hanci(x1, SC)}",
          f"{NAVQ(SC)} {AM_PE} {nanu_l(f'{KAS[1]}… {KAS[2]}… {x2}')} {AM} {hanci(x2, SC)}")
    d.seg("5-435",
          f"{Q(SC)} {AM} {Q(FOUR)} {NHP}",
          KATHA_END.format(x=SAMK))
    # ------------------------------------------------------------ (49) Cittārammaṇakathā
    d.head(4, VAGGA5, "5-13-7-0")
    d.head(5, f"(49) 7. {KATHA.format(x=CITTAR)}", "5-13-7-1-0")
    k_first = f"có ai đó hiểu rõ “{tc(0)} là {tc(0)}”"
    k_last = f"có ai đó hiểu rõ “{tc(15)} là {tc(15)}”"
    k_list = f"có ai đó hiểu rõ {chain([tc(i) for i in range(1, 16)])} là “{tc(15)}”"
    d.seg("5-436",
          f"{Q(CS)} {AM} {NANU(k_first)} {AM} {nanca(k_first, CS)}",
          f"{NANU(k_list)} {AM} {nanca(k_last, CS)}")
    d.seg("5-437",
          f"{Q(ceto_called(PA[0]))} {AM} {nanca(f'{ar(PA[0])} nên được gọi là {CETO}', CS)} "
          f"{cap(ar(PA[1]))}… {chain([ar(x) for x in PA[2:]])}… {q(ceto_called(AOT))} {AM} "
          f"{nanca(f'{ar(AOT)} nên được gọi là {CETO}', CS)}",
          f"{Q(ceto_called(PA[0], True))} {AM} {Q(f'là hiểu biết bao quát {PA[0]}')} {NHP} "
          f"{ar(PA[1])}… {ar(PA[2])}… {q(ceto_called(AOT, True))} {AM} {Q(f'là hiểu biết bao quát {AOT}')} {NHP}")
    d.seg("5-438",
          f"{NAVQ(CS)} {AM} {NANU(f'là {CETO}')} {AM} {hanci(f'là {CETO}', CS)}",
          KATHA_END.format(x=CITTAR))
    # ------------------------------------------------------------ (50) Anāgatañāṇakathā
    d.head(4, VAGGA5, "5-13-8-0")
    d.head(5, f"(50) 8. {KATHA.format(x=AF)}", "5-13-8-1-0")
    knows = ", ".join([f"biết tương lai xét theo {FROM[0]}"] + [f"biết xét theo {x}" for x in FROM[1:]])
    knows2 = ", ".join([f"biết {PC[0]} của tương lai"] + [f"biết {x}" for x in PC[1:]])
    d.seg("5-439",
          f"{Q(T50)} {AM} {Q(knows)} {NHP}",
          f"{Q(T50)} {AM} {Q(knows2)} {NHP}",
          f"{Q(T50)} {AM} {Q(f'{GOTRA} có hiểu biết về {SOTA_MAGGA}')} {NHP} "
          f"{Q(f'{PAT[STAGES[0]]} có hiểu biết về {FR[STAGES[0]]}')} {NHP}",
          f"Trở lại một lần… không trở lại… {q(f'{PAT[STAGES[3]]} có hiểu biết về {FR[STAGES[3]]}')} {NHP}")
    d.seg("5-440",
          f"{NAVQ(T50)} {AM} {NANU_VUTTAM} {SUTTA50} {ATTHEVA} {AM} {TENA_HI(T50)}",
          KATHA_END.format(x=AF))
    # ------------------------------------------------------------ (51) Paṭuppannakathā
    d.head(4, VAGGA5, "5-13-9-0")
    d.head(5, f"(51) 9. {KATHA.format(x=PATU)}", "5-13-9-1-0")
    selfs = ", ".join(f"dùng {x} ấy mà {v} {x} ấy" for x, v in SELF)
    d.seg("5-441",
          f"{Q(f'có {PF} [{SPELL} (Sī., Syā.): paccuppanne]')} {AM} {Q(K1)} {NHP} {q(K1)} {AM} {Q(K2)} {NHP} "
          f"{q(K2)} {AM} {Q(K3)} {NHP}",
          f"{Q(K3)} {AM} {Q(selfs)} {NHP}")
    d.seg("5-442",
          f"{NAVQ(T51)} {AM} {NANU(SANKH)} {AM} {hanci(SANKH, T51)}",
          f"Phần bàn về {PF} [{VAR} (Sī.): paccuppannakathā] đã hoàn tất.")
    # ------------------------------------------------------------ (52) Phalañāṇakathā
    d.head(4, VAGGA5, "5-13-10-0")
    d.head(5, f"(52) 10. {KATHA.format(x=PHALA_N)}", "5-13-10-1-0")
    d.seg("5-443",
          pair(T52, f"{SAV} mô tả sự phân định của thành quả"),
          pair(T52, f"{SAV} có {PARO}"),
          pair(T52, f"{SAV} có {PANN}"),
          pair(T52, f"{SAV} {JINA}"),
          pair(T52, f"{SAV} {MAGGA_X}"))
    d.seg("5-444",
          f"{NAVQ(T52)} {AM} {Q(f'{SAV} là người không biết')} {NHP} vậy thì {T52}…",
          KATHA_END.format(x=PHALA_N),
          f"{VAGGA5}.",
          TASSUDDANAM,
          f"{cap(VM)} {VD}, {AK} của {SE}, {VK}, {T46}, {all_ps}, {SAMK}, {CETO}, {AF}, {PF}, "
          f"{PHALA_N} của {SAV}.",
          MAHAPANNASAKO,
          TASSAPI,
          UDDANA50)
    return d.text()


# ================================================================ cross-book asserts
CROSS_BOOK = [
    ("thuộc về người còn đang tu học", 1), ("thuộc về người đã hoàn tất tu học", 1),
    ("cố định theo hướng đúng đắn", 1), ("Các hiện tượng không cố định", 1), ("Các hiện tượng cố định", 1),
    ("hiểu biết của người có được thành quả", 1), ("sự không xem xét lại", 1), ("có sự bố thí", 1),
    ("sự nhận ra", 1), ("sự cố ý", 1), ("chủ ý", 1), ("sự không biết ghê sợ tội lỗi", 1),
    ("hiểu biết thông suốt", 2), ("sự hiểu biết theo quy ước", 2), ("sự hiểu biết bao quát tâm", 2),
    ("sự hiểu biết về tâm người khác", 2), ("trí tuệ vượt thế gian", 2), ("mức độ cao thấp của các năng lực", 2),
    ("bước vào sự cố định", 2), ("bốn sự đảo ngược", 2), ("đối với điều vô thường", 2),
    ("đối với điều khổ đau", 2), ("đối với điều không phải tự ngã", 2), ("đối với điều không đẹp", 2),
    ("nước bọt", 2), ("mủ, máu", 2), ("nước tiểu", 2), ("hiểu rõ", 2), (ARU[3], 2), (GM, 2), ("chúng sinh", 2),
    ("người chuyển đổi dòng dõi", 4), (PANN, 4), ("sự toàn tri", 4), ("bậc đạo sư", 4),
    ("bậc Tự Giác Ngộ Hoàn Toàn", 4), ("sự định danh về các hạng người", 4),
] + [(f"“Tâm {x}”", 2) for x in CIT]

PI5_DONE = [   # strings taken from finished pi-5 chapters (asserted in their output files)
    ("1-puggalakatha.md", "A-nan"), ("1-puggalakatha.md", "có ai đó"),
    ("2-parihanikatha.md", "trưởng lão Xá-lợi-phất"), ("2-parihanikatha.md", "trưởng lão Đại Mục-kiền-liên"),
    ("2-parihanikatha.md", "có khả năng"), ("2-parihanikatha.md", DEV6[0]),
    ("3-brahmacariyakatha.md", f"{ATT}, chứng nhập và an trú, chạm đến bằng thân rồi an trú"),
    ("3-brahmacariyakatha.md", "không chạm đến bằng thân rồi an trú"),
    ("4-jahatikatha.md", SOTA_MAGGA), ("4-jahatikatha.md", "thấu hiểu Giáo Pháp"), ("4-jahatikatha.md", "đệ tử"),
    ("5-sabbamatthitikatha.md", FOUR), ("5-sabbamatthitikatha.md", "tôn giả"),
    ("5-sabbamatthitikatha.md", "hiện tại"),
    ("9-hevatthikatha.md", TASSUDDANAM), ("9-hevatthikatha.md", "Chương lớn."),
    ("10-dutiyavaggo.md", K0), ("10-dutiyavaggo.md", C10.REQ), ("10-dutiyavaggo.md", "Kinh Phật Tự Thuyết"),
    ("10-dutiyavaggo.md", "Trường Bộ Kinh"), ("10-dutiyavaggo.md", "Đại Phẩm"),
    ("10-dutiyavaggo.md", "đã được thấy là vô thường"), ("10-dutiyavaggo.md", "tất cả những người ấy đều"),
    ("10-dutiyavaggo.md", "thành quả A-la-hán"), ("10-dutiyavaggo.md", TASSUDDANAM),
    ("10-dutiyavaggo.md", C2.FRUIT[C2.AR]),
] + [("10-dutiyavaggo.md", s) for s in KAS + ARU] + [("3-brahmacariyakatha.md", PAT[s]) for s in ("sota", "saka", "ara")] + [("4-jahatikatha.md", PAT["ana"])]


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
