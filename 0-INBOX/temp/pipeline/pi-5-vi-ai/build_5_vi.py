# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 5: 5-sabbamatthitikatha.md (Sabbamatthītikathā, ^5-5-0 … ^5-296).

Imports the approved sample builder (build_sample_vi) for every debate frame; the chapter's own repeated
phrases are fixed strings below, so every repeat is byte-identical. Strings claimed from the pi-1..4
Vietnamese rails are asserted to occur there (and strings claimed from the sample to occur in its output);
the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli.
Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -X utf8 build_5_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "5-sabbamatthitikatha.md"
Q, q, AM, NH, NHP = B.Q, B.q, B.AMANTA, B.NA_HEVAM, B.NA_HEVAM_PE
NANU, NCV = B.NANU, B.NO_CA_VATA


def nanu(x):
    """nanu … ti? after …pe… (lowercase start)."""
    return f"chẳng phải {x} sao?"


# ================================================================ chapter terms
SABBA = "tất cả đều tồn tại"                     # sabbamatthi
CH_X = f"việc cho rằng {SABBA}"                   # Sabbamatthītikathā (terms file heading)
T = {"a": "quá khứ", "f": "tương lai", "p": "hiện tại"}   # atītaṃ / anāgataṃ / paccuppannaṃ (pi-1, pi-2)
ATTHI = "tồn tại"                                # atthi (sample)
PAST5 = "đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn"
# niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ (pi-2 ^2-2)
NPAST5 = "chưa chấm dứt, chưa mất đi, chưa biến đổi, chưa biến mất, chưa biến mất hoàn toàn"
# aniruddhaṃ avigataṃ avipariṇataṃ na atthaṅgataṃ na abbhatthaṅgataṃ
FUT6 = "chưa sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra"
# ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ (pi-2)
PRES6 = "đã sinh ra, đã trở thành, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra"
# jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ (pi-2)
PAST_PE = "đã chấm dứt… đã biến mất hoàn toàn"     # niruddhaṃ…pe… abbhatthaṅgataṃ
NPAST_PE = "chưa chấm dứt… chưa biến mất hoàn toàn"  # aniruddhaṃ…pe… na abbhatthaṅgataṃ
FUT_PE = "chưa sinh ra… chưa hiện ra"              # ajātaṃ…pe… apātubhūtaṃ
PRES_PE = "đã sinh ra… đã hiện ra"                 # jātaṃ…pe… pātubhūtaṃ
NICCA = B.NICCO_DHUVO                            # niccaṃ dhuvaṃ sassataṃ avipariṇāmadhammaṃ (pi-2)
ANICCA4 = "vô thường, không bền vững, không trường tồn, có bản chất biến đổi"
# aniccaṃ adhuvaṃ asassataṃ vipariṇāmadhammaṃ
ANICCA_PE = "vô thường… có bản chất biến đổi"     # aniccaṃ…pe… vipariṇāmadhammaṃ
JAHATI = "dứt bỏ"                                 # jahati (ch4)
NIBBANA = "Niết-bàn"


def tx(t, noun=None):
    """atītaṃ / atītaṃ rūpaṃ = quá khứ / vật chất thuộc quá khứ"""
    return T[t] if noun is None else f"{noun} thuộc {T[t]}"


def bhava(x):
    """X-bhāva = trạng thái X"""
    return f"trạng thái {x}"


# ================================================================ 5-285 (appiyaṃ karitvā, ch1 ^5-67 frame)
SAME = ("khi xem {x} là một không thể tách rời, đó chính là cùng một thứ, cùng một nghĩa, như nhau, ngang nhau, "
        "cùng một loại")   # esese ekaṭṭhe same samabhāge tajjāte (sample build_ch1)


def appiya(a, b, x):
    """"Ati vā B"nti vā, "Bnti vā A"nti vā X appiyaṃ karitvā esese … tajjāteti?"""
    return Q(f"dù gọi là “{a} hay {b}”, hay gọi là “{b} hay {a}”, {SAME.format(x=x)}")


# ================================================================ 5-289 senses
ORG = ["mắt", "tai", "mũi", "lưỡi", "thân", "ý"]                             # cakkhu … mano (pi-2)
OBJS = ["các hình sắc", "các âm thanh", "các mùi", "các vị", "các vật xúc chạm", "các đối tượng của ý"]
OBJ = ["hình sắc", "âm thanh", "mùi", "vị", "vật xúc chạm", "đối tượng của ý"]   # (pi-1 ^1-1354)
CONS = ["thức qua mắt", "thức qua tai", "thức qua mũi", "thức qua lưỡi", "thức qua thân", "ý thức"]   # (pi-2)
COND = ["ánh sáng", "không gian", "gió", "nước", "đất", "chỗ dựa"]
# āloko (new), ākāso, vāyo, āpo, pathavī (pi-1 yếu tố …), vatthu (pi-1 «chỗ dựa»)
VERB = ["thấy", "nghe", "ngửi", "nếm", "chạm", "nhận biết"]   # passati suṇāti ghāyati sāyati phusati vijānāti (pi-1)
MANAS = "sự chú tâm"                                          # manasikāro (core)


def sset(t, i):
    """atītaṃ cakkhuṃ atthi rūpā atthi cakkhuviññāṇaṃ atthi āloko atthi manasikāro atthi"""
    return (f"{ORG[i]} thuộc {T[t]} {ATTHI}, {OBJS[i]} {ATTHI}, {CONS[i]} {ATTHI}, {COND[i]} {ATTHI}, "
            f"{MANAS} {ATTHI}")


def ssee(t, i, neg=False):
    """atītena cakkhunā atītaṃ rūpaṃ passati / na ca …"""
    s = f"dùng {ORG[i]} thuộc {T[t]} mà {VERB[i]} {OBJ[i]} thuộc {T[t]}"
    return f"nhưng không {s}" if neg else s


def schain(t):
    """(X) sotaṃ atthi… ghānaṃ atthi… jivhā atthi… kāyo atthi… mano atthi dhammā atthi … manasikāro atthi"""
    return (f"{ORG[1]} thuộc {T[t]} {ATTHI}… {ORG[2]} {ATTHI}… {ORG[3]} {ATTHI}… {ORG[4]} {ATTHI}… "
            f"{ORG[5]} {ATTHI}, {OBJS[5]} {ATTHI}, {CONS[5]} {ATTHI}, {COND[5]} {ATTHI}, {MANAS} {ATTHI}")


# ================================================================ 5-290 knowledge
NANA = "hiểu biết"                                             # ñāṇa (pi-1)
K = f"nhờ {NANA} ấy mà làm được việc của {NANA}"                 # tena ñāṇena ñāṇakaraṇīyaṃ karoti
F = (f"nhờ {NANA} ấy mà hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, "
     f"tu tập con đường")
# tena ñāṇena dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti (pi-2 words)


def nana(t):
    return f"{NANA} thuộc {T[t]} {ATTHI}"


# ================================================================ 5-291/292 persons and defilements
AR, ANA, SAK, SOT, PU = "bậc A-la-hán", "bậc không trở lại", "bậc trở lại một lần", "bậc vào dòng", "người phàm phu"
RAGA, DOSA, MOHA = "sự tham đắm", "sự sân hận", "sự si mê"          # (ch2, pi-1)
SKD = "quan điểm về tự ngã"                                        # sakkāyadiṭṭhi (pi-1)
DITTHI = "quan điểm"                                               # tāya diṭṭhiyā
VIC = "sự hoài nghi"
SBP = "sự hiểu sai lệch về giới hạnh và nghi thức"                  # sīlabbataparāmāso (pi-1)
BYA = "ác ý"
AK, AB = "sự tham đắm dục lạc ở dạng nhỏ nhiệm", "ác ý ở dạng nhỏ nhiệm"   # aṇusahagato … (ch2, ch3)
OK, OB = "sự tham đắm dục lạc ở dạng thô", "ác ý ở dạng thô"                # oḷāriko … (ch2, ch3)
APAYA = "dẫn đến cõi khổ"                                                   # apāyagamanīyo (ch2)
AR_LIST = [  # (noun, adjective) for Arahato atīto X atthi … arahā tena X-ena saX-o
    (RAGA, "có tham đắm"), (DOSA, "có sân hận"), (MOHA, "có si mê"),          # sarāga / sadosa / samoha (pi-2)
    ("sự kiêu mạn", "có kiêu mạn"), (DITTHI, "có quan điểm"), (VIC, "có hoài nghi"),
    ("sự uể oải", "có uể oải"), ("sự xao động", "có xao động"),
    ("sự không biết hổ thẹn", "có sự không biết hổ thẹn"),                  # saahiriko
    ("sự không biết ghê sợ tội lỗi", "có sự không biết ghê sợ tội lỗi"),     # saanottappī
]
AO = "sự không biết ghê sợ tội lỗi"
ANOTTAPPI = "không biết ghê sợ tội lỗi"                                       # anottappī (^5-292)
BYAPANNA = "có tâm ác ý"                                                     # byāpannacitto (pi-2 abyāpannacitta)


def has(noun, who=None):
    """(whoassa) atīto X atthi"""
    return f"{noun} thuộc quá khứ của {who} {ATTHI}" if who else f"{noun} thuộc quá khứ {ATTHI}"


def by(who, noun, adj, neg=False):
    """who tena X-ena adj / na ca who tena X-ena adj"""
    return f"nhưng {who} không vì {noun} ấy mà {adj}" if neg else f"{who} vì {noun} ấy mà {adj}"


# ================================================================ 5-293
HAND = [("các bàn tay", "việc cầm lên và đặt xuống"), ("các bàn chân", "việc đi tới và đi lui"),
        ("các khớp", "việc co và duỗi")]
# hatthā / ādānanikkhepanaṃ; pādā / abhikkamapaṭikkamo; pabbā / samiñjanapasāraṇaṃ (pi-2 «đi tới, đi lui», «co … duỗi»)
KAYA = "thân thuộc quá khứ"                                                  # atīto kāyo


# ================================================================ 5-295 padasodhana
def pada(x):
    pv = f"{x} {ATTHI}, cái {ATTHI} có thể là {x}, có thể không phải là {x}"           # X atthi atthi siyā X, siyā no X
    neg = f"{x} không phải là {x}, cái không phải là {x} là {x}"                      # X no X, no X X
    full = f"{pv}, do đó {neg}"
    yam = f"{B.YAM_TATTHA} – “nên nói – ‘{full}’”."
    return [
        f"{Q(f'{x} {ATTHI}')} {AM} {Q(f'cái {ATTHI} là {x}')} Cái {ATTHI} có thể là {x}, có thể không phải là {x}.",
        f"{B.AJANAHI['n']} Nếu {pv}, thì do đó {neg}. {yam}",
        f"Còn nếu không có chuyện {neg}, {NCV} “{pv}”. {yam}",
    ]


# ================================================================ 5-296 sutta passages
KHANDHA_Q = ("dù thuộc quá khứ, thuộc tương lai hay thuộc hiện tại, ở nơi bản thân hay ở bên ngoài bản thân, "
             "ở dạng thô hay ở dạng vi tế, thấp kém hay ưu việt, ở xa hay ở gần")   # (pi-2 ^2-2)
PATHS = "phạm vi của cách diễn đạt, phạm vi của tên gọi, phạm vi của sự định danh"
# niruttipathā adhivacanapathā paññattipathā (pi-1 ^1-M2-106/107; paññatti «sự định danh» pi-4/sample)
QUAL = ("không lẫn lộn, trước đây chưa từng lẫn lộn, hiện không bị lẫn lộn, sẽ không bị lẫn lộn, "
        "không bị các sa-môn, bà-la-môn có trí phản đối")
# asaṅkiṇṇā asaṅkiṇṇapubbā na saṅkiyanti na saṅkiyissanti appaṭikuṭṭhā samaṇehi brāhmaṇehi viññūhi
AH, AT, BH = "‘đã tồn tại’", "‘tồn tại’", "‘sẽ tồn tại’"                     # ‘ahosī’ / ‘atthī’ / ‘bhavissatī’


def sankha(main, n1, n2):
    """‘X’ti tassa saṅkhā, ‘X’ti tassa samaññā, ‘X’ti tassa paññatti; na tassa saṅkhā ‘Y’ti, na … ‘Z’ti"""
    return (f"thì cách gọi của nó là {main}, danh xưng chung của nó là {main}, sự định danh của nó là {main}; "
            f"cách gọi của nó không phải là {n1}, cách gọi của nó không phải là {n2}")


SUTTA_PAST = f"đã chấm dứt, đã mất đi, đã biến đổi, {sankha(AH, AT, BH)}"      # atītaṃ niruddhaṃ vigataṃ vipariṇataṃ
SUTTA_FUT = f"chưa sinh ra, chưa hiện ra, {sankha(BH, AT, AH)}"                # ajātaṃ apātubhūtaṃ
SUTTA_PRES = f"đã sinh ra, đã hiện ra, {sankha(AT, AH, BH)}"                   # jātaṃ pātubhūtaṃ
KHANDHA_PE = "Cảm giác nào… tri giác nào… các tạo tác nào… thức nào"         # Yā vedanā…pe… yā saññā… ye saṅkhārā… yaṃ viññāṇaṃ
PHAGGUNA = "Phả-cầu-na"                                                       # phagguna (new name)
NANDAKA = "Nan-đa-ka"                                                         # nandaka (new name)
BUDDHA_PAST = ("khi mô tả các vị Phật quá khứ đã nhập Niết-bàn trọn vẹn, đã cắt đứt sự suy diễn lan man, đã cắt "
               "đứt lối mòn, đã chấm dứt vòng xoay, đã vượt qua mọi khổ đau, người ta có thể mô tả được")
# atīte buddhe parinibbute chinnapapañce chinnavaṭume pariyādinnavaṭṭe sabbadukkhavītivatte paññāpayamāno paññāpeyya
AF = f"{T['a']} {ATTHI}, {T['f']} {ATTHI}"                                     # atītaṃ atthi, anāgataṃ atthi
AHARA = ["thức ăn trong vai trò dưỡng chất", "sự tiếp xúc trong vai trò dưỡng chất",
         "chủ ý của ý trong vai trò dưỡng chất", "thức trong vai trò dưỡng chất"]   # (pi-1 ^1-70)
NAMARUPA = "phần tinh thần và vật chất"                                          # nāmarūpa (pi-1)
PUNABBHAVA = "sự phát sinh của sự hiện hữu mới trong tương lai"                 # āyatiṃ punabbhavābhinibbatti (ch3, coordinator)
JJM = "sự sinh, sự lão hóa và sự chết trong tương lai"                          # āyatiṃ jātijarāmaraṇaṃ (pi-2)
VUDDHI = "sự tăng trưởng của các tạo tác"                                      # saṅkhārānaṃ vuddhi
AVAK = f"sự hình thành của {NAMARUPA}"                                          # nāmarūpassa avakkanti


def ahara_chain(pos):
    ex, nx = ("tồn tại", "tồn tại") if pos else ("không tồn tại", "không tồn tại")
    if pos:
        head = (f"nếu nơi {AHARA[0]} {ex} sự tham đắm, {ex} sự thích thú, {ex} khao khát, thì thức được thiết lập "
                f"ở đó và phát triển. Ở đâu thức được thiết lập và phát triển, thì ở đó {ex} {AVAK}.")
        end = "Ta nói rằng điều ấy có sầu muộn, có bụi bặm"
    else:
        head = (f"nếu nơi {AHARA[0]} {ex} sự tham đắm, {ex} sự thích thú, {ex} khao khát, thì thức không được thiết "
                f"lập ở đó và không phát triển. Ở đâu thức không được thiết lập và không phát triển, thì ở đó {ex} "
                f"{AVAK}.")
        end = None
    steps = [AVAK, VUDDHI, PUNABBHAVA, JJM]
    mid = " ".join(f"Ở đâu {nx} {steps[i]}, thì ở đó {nx} {steps[i + 1]}." for i in range(3))
    return head, mid, nx


def build():
    d = B.Doc()
    d.head(3, B.KATHA.format(x=CH_X), "5-5-0")                              # Sabbamatthītikathā
    # ------------------------------------------------ Vādayutti
    d.head(4, "Lập luận về học thuyết", "5-5-1-0")
    base = f"{Q(SABBA)} {AM}"
    qs = [f"{SABBA} ở mọi nơi", f"{SABBA} vào mọi lúc", f"{SABBA} theo mọi cách", f"{SABBA} trong mọi thứ",
          f"khi coi là không có sự kết hợp, {SABBA}", f"cái gì không {ATTHI} thì cái ấy cũng {ATTHI}"]
    # sabbattha / sabbadā (sample) / sabbena sabbaṃ / sabbesu (sample) / ayoganti katvā / yampi natthi tampatthi
    ditthi = (f"quan điểm cho rằng {SABBA} là {B.MICCHA[0]}, còn quan điểm kia là {B.SAMMA[0]}, điều ấy cũng "
              f"{ATTHI} như vậy")
    # sabbamatthīti yā diṭṭhi sā diṭṭhi micchādiṭṭhīti, yā diṭṭhi sā diṭṭhi sammādiṭṭhīti, hevamatthi
    parts = [f"{base} {Q(x)} {NH}" for x in qs + [ditthi]]
    d.seg("5-282", " ".join(parts) + f" {B.SAMKHITTAM}. Lập luận về học thuyết.")
    # ------------------------------------------------ Kālasaṃsandanā
    d.head(4, "Sự đối chiếu theo thời gian", "5-5-2-0")
    A, Fu, P = T["a"], T["f"], T["p"]
    d.seg("5-283",
          f"{Q(f'{A} {ATTHI}')} {AM} {NANU(f'{A} {PAST5}')} {AM} Nếu {A} {PAST5}, {NCV} “{A} {ATTHI}”.",
          f"{Q(f'{Fu} {ATTHI}')} {AM} {NANU(f'{Fu} {FUT6}')} {AM} Nếu {Fu} {FUT6}, {NCV} “{Fu} {ATTHI}”.",
          f"{Q(f'{P} {ATTHI}, {P} {NPAST5}')} {AM} {Q(f'{A} {ATTHI}, {A} {NPAST5}')} {NHP} "
          f"{q(f'{P} {ATTHI}, {P} {PRES6}')} {AM} {Q(f'{Fu} {ATTHI}, {Fu} {PRES6}')} {NHP}",
          f"{Q(f'{A} {ATTHI}, {A} {PAST5}')} {AM} {Q(f'{P} {ATTHI}, {P} {PAST5}')} {NHP} "
          f"{q(f'{Fu} {ATTHI}, {Fu} {FUT6}')} {AM} {Q(f'{P} {ATTHI}, {P} {FUT6}')} {NH}")

    def kala_block(noun, short=False):
        a, f_, p = tx("a", noun), tx("f", noun), tx("p", noun)
        npast = NPAST_PE if short else NPAST5
        pres = PRES_PE if short else PRES6
        past = PAST_PE if short else PAST5
        fut = FUT_PE if short else FUT6
        return [
            f"{Q(f'{p} {ATTHI}, {p} {npast}')} {AM} {Q(f'{a} {ATTHI}, {a} {npast}')} {NH}",
            f"{Q(f'{p} {ATTHI}, {p} {pres}')} {AM} {Q(f'{f_} {ATTHI}, {f_} {pres}')} {NH}",
            (f"{Q(f'{a} {ATTHI}, {a} {past}')} {AM} {Q(f'{p} {ATTHI}, {p} {past}')} {NH}"),
            (f"{Q(f'{f_} {ATTHI}, {f_} {fut}')} {AM} {Q(f'{p} {ATTHI}, {p} {fut}')} {NH}"),
        ]

    R, V = B.RUPA, B.VINNANA
    ra, rf = tx("a", R), tx("f", R)
    va, vf, vp = tx("a", V), tx("f", V), tx("p", V)
    kr = kala_block(R)
    kv = kala_block(V, short=True)
    d.seg("5-284",
          f"{Q(f'{ra} {ATTHI}')} {AM} {NANU(f'{ra} {PAST5}')} {AM} Nếu {ra} {PAST_PE}, {NCV} “{ra} {ATTHI}”.",
          f"{Q(f'{rf} {ATTHI}')} {AM} {NANU(f'{rf} {FUT6}')} {AM} Nếu {rf} {FUT_PE}, {NCV} “{rf} {ATTHI}”.",
          *kr,
          f"Có phải {tx('a', B.VEDANA)} {ATTHI}… {B.SANNA} {ATTHI}, {B.SANKHARA} {ATTHI}, {V} {ATTHI} không? {AM} "
          f"{NANU(f'{va} {PAST5}')} {AM} Nếu {va} {PAST_PE}, {NCV} “{va} {ATTHI}”.",
          f"{Q(f'{vf} {ATTHI}')} {AM} {NANU(f'{vf} {FUT6}')} {AM} Nếu {vf} {FUT_PE}, {NCV} “{vf} {ATTHI}”.",
          kv[0], kv[1],
          f"{kv[2]} {Q(f'{vf} {ATTHI}, {vf} {FUT_PE}')} {AM}",
          f"{Q(f'{vp} {ATTHI}, {vp} {FUT_PE}')} {NH}")
    # 5-285
    rp = tx("p", R)
    VATTHA = "tấm vải trắng"                                            # odātaṃ vatthaṃ
    r_app = appiya(P, R, rp)
    o_app = appiya("trắng", "vải", VATTHA)
    nir = f"{rp}, khi đang chấm dứt,"                                    # paccuppannaṃ rūpaṃ nirujjhamānaṃ
    raj = f"{VATTHA}, khi đang được nhuộm,"                              # odātaṃ vatthaṃ rajjamānaṃ
    d.seg("5-285",
          f"{r_app} {AM} {Q(f'{nir} {JAHATI} {bhava(P)}')} {AM} {Q(f'{JAHATI} {bhava(R)}')} {NHP}",
          f"{r_app} {AM} {Q(f'{nir} không {JAHATI} {bhava(R)}')} {AM} {Q(f'không {JAHATI} {bhava(P)}')} {NHP}",
          f"{o_app} {AM} {Q(f'{raj} {JAHATI} {bhava('trắng')}')} {AM} {Q(f'{JAHATI} {bhava('vải')}')} {NH}",
          f"{o_app} {AM} {Q(f'{raj} không {JAHATI} {bhava('vải')}')} {AM} "
          f"{Q(f'không {JAHATI} {bhava('trắng')}')} {NHP}")
    # 5-286
    rr = f"{R} không {JAHATI} {bhava(R)}"                                  # rūpaṃ rūpabhāvaṃ na jahati
    nn = f"{NIBBANA} không {JAHATI} {bhava(NIBBANA)}"
    v_sk = f" [{B.VAR} (Sī., Ka.): na jahati]"
    v_at = f" [{B.VAR} (nhiều bản): na jahatīti; cần tham khảo Chú giải]"

    def tj(t, neg=True, noun=None, var=""):
        """atītaṃ atthi atītaṃ atītabhāvaṃ (na) jahati"""
        x = tx(t, noun)
        return f"{x} {ATTHI}, {x} {'không ' if neg else ''}{JAHATI} {bhava(T[t])}{var}"

    nb = f"{NIBBANA} {ATTHI}, {nn}"                                        # nibbānaṃ atthi nibbānaṃ … na jahati
    d.seg("5-286",
          f"{Q(rr)} {AM} {Q(f'{R} {NICCA}')} {NH} {NANU(f'{rr}, {R} {ANICCA4}')} {AM} "
          f"Nếu {R} {ANICCA4}, {NCV} “{rr}”.",
          f"{Q(f'{nn}, {NIBBANA} {NICCA}')} {AM} {Q(f'{rr}{v_sk}, {R} {NICCA}')} {NHP} "
          f"{q(f'{rr}, {R} {ANICCA4}')} {AM} {Q(f'{nn}, {NIBBANA} {ANICCA4}')} {NHP}",
          f"{Q(tj('a'))} {AM} {Q(tj('f'))} {NH} {Q(tj('a'))} {AM} {Q(tj('p'))} {NHP}",
          f"{Q(tj('f', False, var=v_at))} {AM} {Q(tj('a', False, var=v_at))} {NHP}",
          f"{Q(tj('p', False, var=v_at))} {AM} {Q(tj('a', False, var=v_at))} {NH}",
          f"{Q(tj('a'))} {AM} {Q(f'{A} {NICCA}')} {NHP} {nanu(f'{A} {ANICCA4}')} {AM} "
          f"Nếu {A} {ANICCA4}, {NCV} “{tj('a')}”.",
          f"{Q(f'{nb}, {NIBBANA} {NICCA}')} {AM} {Q(f'{tj(chr(97))}, {A} {NICCA}')} {NHP}",
          f"{Q(f'{tj(chr(97))}, {A} {ANICCA4}')} {AM} {Q(f'{nb}, {NIBBANA} {ANICCA4}')} {NHP}")
    # 5-287
    v_an = f" [{B.VAR} (nhiều bản): na jahatīti; đây chỉ là câu hỏi theo chiều thuận]"
    v_pu = f" [{B.VAR} (?): na jahatīti; cần đối chiếu với các câu hỏi trước]"
    nbv = f"{NIBBANA} {ATTHI}, {nn}{v_pu}"

    def khandha_287(noun, lead, var_f, short_anicca):
        xa = tx("a", noun)
        an = ANICCA_PE if short_anicca else ANICCA4
        return [
            f"{lead} {AM} {Q(tj('f', noun=noun))} {NHP} {q(tj('a', noun=noun))} {AM} {Q(tj('p', noun=noun))} {NHP}",
            f"{Q(tj('f', False, noun, var_f))} {AM} {Q(tj('a', False, noun, var_f))} {NHP}",
            f"{Q(tj('p', False, noun, v_an))} {AM} {Q(tj('a', False, noun, v_an))} {NHP}",
            f"{Q(tj('a', noun=noun))} {AM} {Q(f'{xa} {NICCA}')} {NHP} {nanu(f'{xa} {ANICCA4}')} {AM} "
            f"Nếu {xa} {an}, {NCV} “{tj('a', noun=noun)}”.",
            f"{Q(f'{nbv}, {NIBBANA} {NICCA}')} {AM} {Q(f'{tj(chr(97), noun=noun, var=v_pu)}, {xa} {NICCA}')} {NHP}",
            f"{Q(f'{tj(chr(97), noun=noun)}, {xa} {ANICCA4}')} {AM} {Q(f'{nb}, {NIBBANA} {ANICCA4}')} {NHP}",
        ]

    kr7 = khandha_287(R, Q(tj("a", noun=R)), v_an, True)
    lead_v = (f"Có phải {tx('a', B.VEDANA)} {ATTHI}… {tx('a', B.SANNA)} {ATTHI}… {tx('a', B.SANKHARA)} {ATTHI}… "
              f"{tj('a', noun=V)} không?")
    kv7 = khandha_287(V, lead_v, "", False)
    d.seg("5-287", *kr7, *kv7)
    # ------------------------------------------------ Vacanasodhanā
    d.head(4, "Sự làm sáng tỏ từ ngữ", "5-5-3-0")
    H1 = "đã có rồi lại có, đã có rồi lại có"                            # hutvā hoti hutvā hoti
    H0 = "chưa có thì không có, chưa có thì không có"                    # na hutvā na hoti na hutvā na hoti

    def nv(x):
        return (f"{Q(f'{x} không {ATTHI}')} {AM} Nếu {x} không {ATTHI}, thì nói rằng {x} {ATTHI} là sai. "
                f"Hoặc nếu cái {ATTHI} không phải là {x}, thì nói rằng cái {ATTHI} là {x} là sai.")

    def hutva(first, same):
        return (f"{Q(first)} {AM} {Q(same)} {NHP} {q(same)} {AM} {Q(H1)} {NHP} {q(H1)} {AM} {Q(H0)}")

    fp = f"là {Fu} rồi trở thành {P}"                                    # anāgataṃ hutvā paccuppannaṃ hoti
    pa = f"là {P} rồi trở thành {A}"
    d.seg("5-288",
          f"{nv(A)} {nv(Fu)}",
          f"{hutva(fp, f'chính {Fu} ấy là {P} ấy')} {NHP}",
          f"{hutva(pa, f'chính {P} ấy là {A} ấy')} {NHP}",
          f"{hutva(f'{fp}, {pa}', f'chính {Fu} ấy là {P} ấy, là {A} ấy')} {NH}")
    # ------------------------------------------------ Atītacakkhurūpādikathā
    d.head(4, "Bàn về mắt, hình sắc quá khứ và các mục khác", "5-5-4-0")
    l63 = [f"{Q(sset('a', 0))} {AM} {Q(ssee('a', 0))} {NHP}"]
    l63 += [f"{q(sset('a', i))} {AM} {Q(ssee('a', i))} {NHP}" for i in range(1, 6)]

    def pair(t1, t2, neg=False):
        """X-set, (na ca) X-see? Āmantā. Y-set, (na ca) Y-see? Na hevaṃ…pe…"""
        return (f"Có phải {sset(t1, 0)}, {ssee(t1, 0, neg)} không? {AM} "
                f"Có phải {sset(t2, 0)}, {ssee(t2, 0, neg)} không? {NHP}")

    def pair_m(t1, t2, neg=False, cap=False):
        first = f"{'Có' if cap else 'có'} phải {schain(t1)}, {ssee(t1, 5, neg)} không?"
        return f"{first} {AM} Có phải {sset(t2, 5)}, {ssee(t2, 5, neg)} không? {NHP}"

    d.seg("5-289",
          " ".join(l63),
          f"{Q(sset('f', 0))} {AM} {Q(ssee('f', 0))} {NHP} có phải {schain('f')} không? {AM} {Q(ssee('f', 5))} {NHP}",
          f"{pair('p', 'a')} {pair_m('p', 'a', cap=True)}",
          f"{pair('p', 'f')} {pair_m('p', 'f')}",
          f"{pair('a', 'p', True)} {pair_m('a', 'p', True)}",
          f"{pair('f', 'p', True)} {pair_m('f', 'p', True)}")
    # ------------------------------------------------ Atītañāṇādikathā
    d.head(4, "Bàn về hiểu biết quá khứ và các mục khác", "5-5-5-0")
    Kn, Fn = f"nhưng không {K}", f"nhưng không {F}"
    d.seg("5-290",
          f"{Q(nana('a'))} {AM} {Q(K)} {NHP} {q(K)} {AM} {Q(F)} {NHP}",
          f"{Q(nana('f'))} {AM} {Q(K)} {NHP} {q(K)} {AM} {Q(F)} {NHP}",
          " ".join(f"{(Q if i == 0 else q)(f'{nana(chr(112))}, {x}')} {AM} {Q(f'{nana(t)}, {x}')} {NHP}"
                   for i, (t, x) in enumerate((("a", K), ("a", F), ("f", K), ("f", F)))),
          f"{Q(f'{nana(chr(97))}, {Kn}')} {AM} {Q(f'{nana(chr(112))}, {Kn}')} {NHP} "
          f"{q(f'{nana(chr(97))}, {Fn}')} {AM} {Q(f'{nana(chr(112))}, {Fn}')} {NHP}",
          f"{Q(f'{nana(chr(102))}, {Kn}')} {AM} {Q(f'{nana(chr(112))}, {Kn}')} {NHP} "
          f"{Q(f'{nana(chr(102))}, {Fn}')} {AM} {Q(f'{nana(chr(112))}, {Fn}')} {NHP}")
    # ------------------------------------------------ Arahantādikathā
    d.head(4, "Bàn về bậc A-la-hán và các mục khác", "5-5-6-0")
    l80 = []
    for i, (n, a) in enumerate(AR_LIST):
        l80.append(f"{(Q if i == 0 else q)(has(n, AR))} {AM} {Q(by(AR, n, a))} {NHP}")

    def ariya3(who, third, fourth, last_noun, last_adj):
        """Whoassa atītā sakkāyadiṭṭhi atthīti? … whoassa atītā vicikicchā atthi… atīto sīlabbata… atthi… X… Y atthīti?"""
        chain = "… ".join([has(VIC, who), has(SBP)] + [has(x) for x in third])
        return (f"{Q(has(SKD, who))} {AM} {Q(by(who, DITTHI, 'có quan điểm'))} {NHP} "
                f"có phải {chain} không? {AM} {Q(by(who, last_noun, last_adj))} {NHP}")

    d.seg("5-291",
          " ".join(l80),
          ariya3(ANA, [AK, AB], None, BYA, BYAPANNA),
          ariya3(SAK, [OK, OB], None, BYA, BYAPANNA),
          ariya3(SOT, [f"{RAGA} {APAYA}", f"{DOSA} {APAYA}", f"{MOHA} {APAYA}"], None, MOHA, "có si mê"))

    def cmp(w1, w2, first, last, neg=False):
        """w1assa atīto X atthi, (na ca) w1 tena X-ena adj? Āmantā. w2assa … ? Na hevaṃ…pe… w1assa … Y …
        first = (has-noun, tena-noun, adjective); last = (middle has-noun, has-noun, tena-noun, adjective)"""
        (h0, b0, a0), (mid, hl, bl, al) = first, last
        s1 = f"{has(h0, w1)}, {by(w1, b0, a0, neg)}"
        s2 = f"{has(h0, w2)}, {by(w2, b0, a0, neg)}"
        e1 = f"{has(hl)}, {by(w1, bl, al, neg)}"
        e2 = f"{has(hl, w2)}, {by(w2, bl, al, neg)}"
        return f"{Q(s1)} {AM} {Q(s2)} {NHP} có phải {has(mid, w1)}… {e1} không? {AM} {Q(e2)} {NHP}"

    R1 = (RAGA, RAGA, "có tham đắm")
    S1 = (SKD, DITTHI, "có quan điểm")
    L_AR = (DOSA, AO, AO, ANOTTAPPI)
    L_ANA = (VIC, AB, BYA, BYAPANNA)
    L_SAK = (VIC, OB, BYA, BYAPANNA)
    L_SOT = (VIC, f"{MOHA} {APAYA}", MOHA, "có si mê")
    d.seg("5-292",
          cmp(PU, AR, R1, L_AR), cmp(PU, ANA, S1, L_ANA), cmp(PU, SAK, S1, L_SAK), cmp(PU, SOT, S1, L_SOT),
          cmp(AR, PU, R1, L_AR, True), cmp(ANA, PU, S1, L_ANA, True), cmp(SAK, PU, S1, L_SAK, True),
          cmp(SOT, PU, S1, L_SOT, True))
    # ------------------------------------------------ Atītahatthādikathā
    d.head(4, "Bàn về bàn tay quá khứ và các mục khác", "5-5-7-0")
    l96 = []
    for i, (n, act) in enumerate(HAND + [("bụng", "sự đói và sự khát")]):
        x = f"{n} thuộc quá khứ"
        l96.append(f"{(Q if i == 0 else q)(f'{x} {ATTHI}')} {AM} "
                   f"{Q(f'khi {x} {ATTHI}, {act} được nhận ra')} {NHP}")
    # atītesu hatthesu sati … paññāyati (sati = locative of atthi «khi … tồn tại»; paññāyati «được nhận ra» sample)
    bind = ", ".join([f"trói {KAYA} bằng cùm", "trói bằng dây thừng", "trói bằng xích sắt",
                      "trói bằng sự giam giữ trong làng", "trói bằng sự giam giữ trong thị trấn",
                      "trói bằng sự giam giữ trong thành phố", "trói bằng sự giam giữ trong xứ sở",
                      "trói bằng năm dây trói mà dây thứ năm ở cổ"])
    el = [("nước", "nước"), ("lửa", "lửa"), ("gió", "gió")]                  # āpo / tejo / vāyo (pi-1)
    l98 = []
    for i, (e, w) in enumerate(el):
        l98.append(f"{(Q if i == 0 else q)(f'{e} thuộc quá khứ {ATTHI}')} {AM} "
                   f"{Q(f'nhờ {e} ấy mà làm được việc của {w}')} {NHP}")
    d.seg("5-293",
          " ".join(l96),
          f"{Q(f'{KAYA} {ATTHI}')} {AM} "
          f"{Q(f'{KAYA} có thể bị nắm giữ và kìm kẹp, có thể bị cắt và bị đập vỡ, là thứ chung cho quạ, kền kền, diều hâu')} "
          f"{NHP} {q(f'chất độc có thể tác động lên {KAYA}, dao kiếm có thể tác động, lửa có thể tác động')} {NHP} "
          f"{q('có thể ' + bind)} {NHP}",
          " ".join(l98))
    # ------------------------------------------------ Atītakkhandhādisamodhānakathā
    d.head(4, "Bàn về sự gộp chung các khối quá khứ và các mục khác", "5-5-8-0")

    def tri(x, verb=ATTHI):
        return ", ".join(f"{x} thuộc {T[t]} {verb}" for t in "afp")

    d.seg("5-294",
          f"{Q(tri('khối vật chất'))} {AM} {Q('có ba khối vật chất')} {NHP} {q(tri('năm khối'))} {AM} "
          f"{Q('có mười lăm khối')} {NHP}",
          f"{Q(tri('lĩnh vực mắt'))} {AM} {Q('có ba lĩnh vực mắt')} {NHP} {q(tri('mười hai lĩnh vực nhận biết'))} "
          f"{AM} {Q('có ba mươi sáu lĩnh vực nhận biết')} {NHP}",
          f"{Q(tri('yếu tố mắt'))} {AM} {Q('có ba yếu tố mắt')} {NHP} {q(tri('mười tám yếu tố'))} {AM} "
          f"{Q('có năm mươi bốn yếu tố')} {NHP}",
          f"{Q(tri('năng lực mắt'))} {AM} {Q('có ba năng lực mắt')} {NHP} {q(tri('hai mươi hai năng lực'))} {AM} "
          f"{Q('có sáu mươi sáu năng lực')} {NHP}",
          f"{Q(tri('vua chuyển luân'))} {AM} {Q('ba vị vua chuyển luân cùng hiện diện đối mặt nhau')} {NHP}",
          f"{Q(tri('bậc Tự Giác Ngộ Hoàn Toàn'))} {AM} "
          f"{Q('ba bậc Tự Giác Ngộ Hoàn Toàn cùng hiện diện đối mặt nhau')} {NHP}")
    # ------------------------------------------------ Padasodhanakathā
    d.head(4, "Bàn về sự làm sáng tỏ thuật ngữ", "5-5-9-0")
    d.seg("5-295", *pada(A), *pada(Fu), *pada(P), *pada(NIBBANA))
    # ------------------------------------------------ Suttasādhanaṃ
    d.head(4, "Chứng cứ từ kinh", "5-5-10-0")
    nanu_a = f"{Q(f'{A} {ATTHI}')} {AM}"
    ah_pos, ah_mid, _ = ahara_chain(True)
    ah_neg, ah_mid_n, _ = ahara_chain(False)
    d.seg("5-296",
          f"{B.NA_VATTABBAM_Q(AF)} {AM} {B.NANU_VUTTAM} “Này các tỳ-khưu, bất cứ vật chất nào, {KHANDHA_Q} – đó "
          f"được gọi là khối vật chất. Bất cứ cảm giác nào… bất cứ tri giác nào… bất cứ các tạo tác nào… bất cứ "
          f"thức nào, {KHANDHA_Q} – đó được gọi là khối thức” [Tương Ưng Bộ Kinh 3.48]. {B.ATTHEVA} {AM} "
          f"{B.TENA_HI(AF)}",
          f"{Q(AF)} {AM} {B.NANU_VUTTAM} “Này các tỳ-khưu, có ba {PATHS} sau đây, {QUAL}. Ba điều nào? "
          f"Này các tỳ-khưu, vật chất nào thuộc quá khứ, {SUTTA_PAST}. {KHANDHA_PE} thuộc quá khứ, {SUTTA_PAST}.",
          f"“Này các tỳ-khưu, vật chất nào {SUTTA_FUT}. {KHANDHA_PE} {SUTTA_FUT}.",
          f"“Này các tỳ-khưu, vật chất nào {SUTTA_PRES}. {KHANDHA_PE} {SUTTA_PRES}. Này các tỳ-khưu, đây chính là "
          f"ba {PATHS}, {QUAL}.",
          f"“Này các tỳ-khưu, ngay cả những người ở xứ Úc-ca-la là Vát-sa và Bhan-nha, những người theo học thuyết "
          f"không có nguyên nhân, theo học thuyết không có hành động, theo học thuyết hư vô, cũng đã cho rằng ba "
          f"{PATHS} này là không nên chê trách, không nên phản đối. Vì sao vậy? Vì sợ bị chê bai, bị công kích, bị "
          f"chỉ trích” [trong Tương Ưng Bộ Kinh]. {B.ATTHEVA} {AM} {B.TENA_HI_NA(AF)}",
          f"{nanu_a} Chẳng phải tôn giả {PHAGGUNA} đã nói với Đức Thế Tôn thế này sao – “Bạch Thế Tôn, có con mắt "
          f"nào mà nhờ con mắt ấy, {BUDDHA_PAST} không? Bạch Thế Tôn, có cái lưỡi nào… bạch Thế Tôn, có ý nào mà "
          f"nhờ ý ấy, {BUDDHA_PAST} không?”",
          f"“Này {PHAGGUNA}, quả thật không có con mắt nào mà nhờ con mắt ấy, {BUDDHA_PAST}. Này {PHAGGUNA}, quả "
          f"thật không có cái lưỡi nào… này {PHAGGUNA}, thật vậy, không có ý nào mà nhờ ý ấy, {BUDDHA_PAST}” "
          f"[Tương Ưng Bộ Kinh 4.83]. {B.ATTHEVA} {AM} {B.TENA_HI_NA(f'{A} {ATTHI}')}",
          f"{nanu_a} Chẳng phải tôn giả {NANDAKA} đã nói thế này sao – “Trước đây đã có sự tham lam, điều ấy đã là "
          f"bất thiện; nay nó không {ATTHI}, như vậy điều này là thiện. Trước đây đã có sự sân hận… trước đây đã có "
          f"sự si mê, điều ấy đã là bất thiện; nay nó không {ATTHI}, như vậy điều này là thiện” [trong Tăng Chi Bộ "
          f"Kinh]. {B.ATTHEVA} {AM} {B.TENA_HI_NA(f'{A} {ATTHI}')}",
          f"{B.NA_VATTABBAM_Q(f'{Fu} {ATTHI}')} {AM} {B.NANU_VUTTAM} “Này các tỳ-khưu, {ah_pos} {ah_mid} Ở đâu "
          f"{ATTHI} {JJM}, này các tỳ-khưu, Ta nói rằng điều ấy có sầu muộn, có bụi bặm "
          f"[{B.VAR} (Tương Ưng Bộ Kinh 2.64): sadaraṃ; cách đọc ấy hợp lý hơn], có tuyệt vọng.",
          f"“Này các tỳ-khưu, nếu nơi {AHARA[1]}… này các tỳ-khưu, nếu nơi {AHARA[2]}… này các tỳ-khưu, nếu nơi "
          f"{AHARA[3]} {ATTHI} sự tham đắm, {ATTHI} sự thích thú… Ta nói rằng điều ấy có bụi bặm, có tuyệt vọng” "
          f"[Tương Ưng Bộ Kinh 2.64]. {B.ATTHEVA} {AM} {B.TENA_HI(f'{Fu} {ATTHI}')}",
          f"{Q(f'{Fu} {ATTHI}')} {AM} {B.NANU_VUTTAM} “Này các tỳ-khưu, {ah_neg} {ah_mid_n} Ở đâu không {ATTHI} "
          f"{JJM}, này các tỳ-khưu, Ta nói rằng điều ấy không sầu muộn, không bụi bặm, không tuyệt vọng.",
          f"“Này các tỳ-khưu, nếu nơi {AHARA[1]}… này các tỳ-khưu, nếu nơi {AHARA[2]}… này các tỳ-khưu, nếu nơi "
          f"{AHARA[3]} không {ATTHI} sự tham đắm, không {ATTHI} sự thích thú… Ta nói rằng điều ấy không bụi bặm, "
          f"không tuyệt vọng” [Tương Ưng Bộ Kinh 2.64]. {B.ATTHEVA} {AM} {B.TENA_HI_NA(f'{Fu} {ATTHI}')}",
          B.KATHA_END.format(x=CH_X))
    return d.text()


# ================================================================ cross-book / sample asserts
CROSS = [
    (PAST5, 2), (FUT6, 2), (PRES6, 2), ("vật chất thuộc quá khứ", 2), ("thức thuộc hiện tại", 2),
    (KHANDHA_Q, 2), ("đó được gọi là khối vật chất", 2), ("đó được gọi là khối thức", 2),
    ("thuộc quá khứ", 1), ("thuộc tương lai", 1), ("thuộc hiện tại", 1),
    ("có tham đắm", 2), ("có sân hận", 2), ("có si mê", 2), ("với tâm không ác ý", 2),
    ("vua chuyển luân", 2), ("khi đi tới, khi đi lui", 2), ("khi co tay chân", 2), ("sự suy diễn lan man", 2),
    ("hiểu biết trọn vẹn", 2), ("tự mình chứng nghiệm", 2), ("sự phát sinh của khổ đau", 2),
    ("sự chấm dứt khổ đau", 2), ("sầu muộn", 2), ("sự tuyệt vọng", 2), ("sự sinh", 2), ("sự lão hóa", 2),
    ("sự chết", 2), ("Vì sao vậy?", 2), ("sự hiện hữu mới", 2), ("cõi khổ", 2), ("ở dạng vi tế", 2),
    ("mười hai lĩnh vực nhận biết", 3), ("mười tám yếu tố", 3), ("năm khối", 3),
    ("yếu tố đất", 1), ("yếu tố nước", 1), ("yếu tố lửa", 1), ("yếu tố gió", 1), ("yếu tố không gian", 1),
    ("sự chú tâm", 1), ("chỗ dựa", 1), ("khi nhận biết đối tượng của ý bằng ý", 1), ("người ta đã thấy", 1),
    ("nghe âm thanh bằng tai", 1), ("khi ngửi mùi bằng mũi", 1), ("khi nếm vị bằng lưỡi", 1),
    ("khi chạm vật xúc chạm bằng thân", 1), ("ý thức", 1),
    ("sự uể oải", 1), ("sự xao động", 1), ("sự không biết hổ thẹn", 1), ("sự không biết ghê sợ tội lỗi", 1),
    ("sự kiêu mạn", 2), ("sự hoài nghi", 1), (SKD, 1), (SBP, 1), ("sự tham đắm dục lạc", 1), ("ác ý", 1),
    ("ở dạng thô", 1), (NAMARUPA, 1), (AHARA[0], 1), (AHARA[1], 1), (AHARA[2], 1), (AHARA[3], 1),
    ("sự thích thú", 1), ("sự tham lam", 1), ("người phàm phu", 1), ("phạm vi của cách diễn đạt", 1),
    ("phạm vi của tên gọi", 1), ("danh xưng chung", 1), ("sa-môn", 1), ("bà-la-môn", 1), ("vô thường", 1),
    ("hiểu biết", 1), ("tu tập", 1), ("khổ đau", 1), ("Niết-bàn", 1), ("sự định danh", 4), ("Chú giải", 4),
    ("Tăng Chi Bộ Kinh", 4), ("tôn giả", 4), ("bậc Tự Giác Ngộ Hoàn Toàn", 4),
    ("khối vật chất", 2), ("lĩnh vực mắt", 2), ("yếu tố mắt", 2), ("năng lực mắt", 2), ("thiện", 1),
    ("bất thiện", 1), ("khao khát", 1),
]
SAMPLE_STRINGS = [SAME.format(x="thân"), "bạch Thế Tôn", "Bạch Thế Tôn", "Này A-nan", "được nhận ra",
                  "ở mọi nơi", "vào mọi lúc", "trong mọi thứ", "là khác", "dị bản (nhiều bản)",
                  "Tương Ưng Bộ Kinh", "chiều thuận"]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    sample = (B.OUT_DIR / "1-puggalakatha.md").read_text(encoding="utf-8")
    smiss = [s for s in SAMPLE_STRINGS if s not in sample]
    for s in smiss:
        print(f"SAMPLE MISSING: {s}")
    assert not missing and not smiss, f"{len(missing)} cross-book / {len(smiss)} sample strings not found"
    print(f"ch5 asserts: {len(CROSS)} strings found in pi-1..4 rails, {len(SAMPLE_STRINGS)} in the sample")


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
