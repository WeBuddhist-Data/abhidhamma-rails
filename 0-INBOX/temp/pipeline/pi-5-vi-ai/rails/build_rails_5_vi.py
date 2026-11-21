"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 5, Sabbamatthītikathā (^5-5-0 … ^5-296).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/5-sabbamatthitikatha.md from the
fixed strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci_neg, tena_hi …).
Every string marked (pi-N) is asserted to occur in that book's approved Vietnamese rails; strings shared with
the finished pi-5 rails chapters (sample, ch2, ch3, ch4, ch6) are asserted to occur there; S.write runs the
per-line dash / quote / NFC / id checks against the Pāli.
New recurring strings: notes-rails-5.md.

usage: python -I -X utf8 -B build_rails_5_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "5-sabbamatthitikatha.md"
Q, q, NANU, PE, YES, NO, NO_PE, cap = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE, S.cap

# ---------------------------------------------------------------------------------------------------------------
# Core words (termbase; pi-5 ch6 frames)
# ---------------------------------------------------------------------------------------------------------------
EX, NEX = "tồn tại", "không tồn tại"                 # atthi / natthi (sample ^5-55, ch6)
PAST, FUT, PRES = "quá khứ", "tương lai", "hiện tại"  # atītaṃ / anāgataṃ / paccuppannaṃ (subject)
TH = {PAST: "thuộc quá khứ", FUT: "thuộc tương lai", PRES: "thuộc hiện tại"}   # atītaṃ rūpaṃ … (ch6)
RUPA, VEDANA, SANNA, SANKHARA, VINNANA = S.RUPA, S.VEDANA, S.SANNA, S.SANKHARA, S.VINNANA
NB = "Niết-bàn"                                       # nibbānaṃ
ALL = "tất cả đều tồn tại"                            # sabbamatthi
CAI_EX = f"cái {EX}"                                  # atthi (as noun, sample ^5-55 «cái tồn tại»)


def th(x, t):
    return f"{x} {TH[t]}"


# ---------------------------------------------------------------------------------------------------------------
# Headings
# ---------------------------------------------------------------------------------------------------------------
KATHA_NAME = "việc tất cả đều tồn tại"                # Sabbamatthītikathā (sabbaṃ «tất cả», atthi «tồn tại»)
H_KATHA = S.katha(KATHA_NAME)
END_KATHA = S.katha_end(KATHA_NAME)
H = {
    "Vādayutti": "Lập luận dựa trên học thuyết",                    # ch2 Vādayuttiparihāni
    "Kālasaṃsandanā": "Sự đối chiếu theo thời gian",                  # saṃsandanā «Sự đối chiếu», kāla «thời gian»
    "Vacanasodhanā": S.H["Vacanasodhanaṃ"],                           # = sample Vacanasodhanaṃ
    "Atītacakkhurūpādikathā": S.katha("mắt quá khứ, hình sắc và các mục khác"),   # atītacakkhu «mắt … quá khứ»
    "Atītañāṇādikathā": S.katha("hiểu biết quá khứ và các mục khác"),             # atītañāṇa «hiểu biết quá khứ»
    "Arahantādikathā": S.katha("bậc A-la-hán và các mục khác"),
    "Atītahatthādikathā": S.katha("bàn tay quá khứ và các mục khác"),            # atītahattha «bàn tay quá khứ»
    "Atītakkhandhādisamodhānakathā": S.katha("sự gộp chung các khối quá khứ và các mục khác"),  # ch6 «các khối quá khứ»
    "Padasodhanakathā": S.katha("sự làm sáng tỏ thuật ngữ"),                     # sodhana, pada «thuật ngữ»
    "Suttasādhanaṃ": "Chứng cứ từ kinh",                                          # = ch6
}

# ---------------------------------------------------------------------------------------------------------------
# Time formulas (pi-1 ^1-1044 … ^1-1046 / pi-2 khandhavibhaṅga wording)
# ---------------------------------------------------------------------------------------------------------------
PAST5 = "đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn"
#   niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ (pi-1)
NPAST5 = "chưa chấm dứt, chưa mất đi, chưa biến đổi, chưa biến mất, chưa biến mất hoàn toàn"
#   aniruddhaṃ avigataṃ avipariṇataṃ na atthaṅgataṃ na abbhatthaṅgataṃ
FUT6 = "chưa sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra"
#   ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ (pi-1)
PRES6 = "đã sinh ra, đã trở thành, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra"
#   jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ (pi-1)
PAST5_S = f"đã chấm dứt{PE} đã biến mất hoàn toàn"     # niruddhaṃ…pe… abbhatthaṅgataṃ
NPAST5_S = f"chưa chấm dứt{PE} chưa biến mất hoàn toàn"  # aniruddhaṃ…pe… na abbhatthaṅgataṃ
FUT6_S = f"chưa sinh ra{PE} chưa hiện ra"               # ajātaṃ…pe… apātubhūtaṃ
PRES6_S = f"đã sinh ra{PE} đã hiện ra"                  # jātaṃ…pe… pātubhūtaṃ
NICCA = "thường còn, bền vững, trường tồn, có bản chất không biến đổi"   # niccaṃ dhuvaṃ sassataṃ avipariṇāmadhammaṃ (pi-2)
ANICCA4 = "vô thường, không bền vững, không trường tồn, có bản chất biến đổi"   # aniccaṃ adhuvaṃ asassataṃ vipariṇāmadhammaṃ
ANICCA4_S = f"vô thường{PE} có bản chất biến đổi"       # aniccaṃ…pe… vipariṇāmadhammaṃ


def ex2(s, pred):                   # X atthi X <pred>ti
    return f"{s} {EX}, {s} {pred}"


def nj(s, st, neg=True):            # X Y-bhāvaṃ (na) jahati
    return f"{s} {'không ' if neg else ''}dứt bỏ trạng thái {st}"


def exj(s, st, neg=True):           # X atthi X Y-bhāvaṃ (na) jahati
    return f"{s} {EX}, {nj(s, st, neg)}"


def nanu_l(x):                      # …pe… nanu Xti? (lower case)
    return f"chẳng phải {x} sao?"


def appiya(x):                      # X appiyaṃ karitvā esese ekaṭṭhe same samabhāge tajjāte (sample KAYA_K)
    return (f"khi xem {x} như một không thể tách rời, thì đều là một, cùng một nghĩa, như nhau, ngang nhau, "
            f"cùng một loại")


def goi(a, b):                      # "Ati vā B"nti vā, "Bti vā A"nti vā
    return f"“gọi là {a} hay gọi là {b}”, “gọi là {b} hay gọi là {a}”"


# editorial variants
VSK = S.var_sp("Sī., Ka.", "na jahati")                                         # [na jahati (sī. ka.)]
VB = S.var(S.CIT["bahūsu"], "na jahatīti")[:-1] + "; cần tham khảo Chú giải]"   # … aṭṭhakathā oloketabbā
VA = S.var(S.CIT["bahūsu"], "na jahatīti")[:-1] + "; chỉ là câu hỏi theo chiều thuận]"   # … anulomapañhoyeva
VP = S.var("?", "na jahatīti")[:-1] + "; cần đối chiếu với các câu hỏi trước]"  # … purimapañhehi saṃsandetabbaṃ

# ---------------------------------------------------------------------------------------------------------------
# Senses (^5-289), knowledge (^5-290)
# ---------------------------------------------------------------------------------------------------------------
ORG = [("mắt", "các hình sắc", "thức qua mắt", "ánh sáng", "thấy", "hình sắc"),
       ("tai", "các âm thanh", "thức qua tai", "không gian", "nghe", "âm thanh"),
       ("mũi", "các mùi", "thức qua mũi", "gió", "ngửi", "mùi"),
       ("lưỡi", "các vị", "thức qua lưỡi", "nước", "nếm", "vị"),
       ("thân", "các vật xúc chạm", "thức qua thân", "đất", "chạm vào", "vật xúc chạm"),
       ("ý", "các đối tượng của ý", "ý thức", "chỗ dựa", "nhận biết", "đối tượng của ý")]
MANAS = "sự chú tâm"                                  # manasikāro


def five(t, k):                     # X cakkhuṃ atthi rūpā atthi cakkhuviññāṇaṃ atthi āloko atthi manasikāro atthi
    o = ORG[k]
    return f"{o[0]} {TH[t]} {EX}, {o[1]} {EX}, {o[2]} {EX}, {o[3]} {EX}, {MANAS} {EX}"


def chain(t):                       # X sotaṃ atthi… ghānaṃ atthi… jivhā atthi… kāyo atthi… mano atthi dhammā atthi …
    o = ORG[5]
    return (f"tai {TH[t]} {EX}{PE} mũi {EX}{PE} lưỡi {EX}{PE} thân {EX}{PE} "
            f"{o[0]} {EX}, {o[1]} {EX}, {o[2]} {EX}, {o[3]} {EX}, {MANAS} {EX}")


def see(t, k, neg=False):           # (na ca) X-ena cakkhunā X-ṃ rūpaṃ passati
    o = ORG[k]
    return f"{'nhưng ' if neg else ''}bằng {o[0]} {TH[t]} mà {'không ' if neg else ''}{o[4]} {o[5]} {TH[t]}"


FN = "làm việc của hiểu biết"                          # ñāṇakaraṇīyaṃ karoti
F4 = "hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, tu tập con đường"
#   dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti


def by_n(x, neg=False):             # (na ca) tena ñāṇena X
    return f"{'nhưng ' if neg else ''}bằng hiểu biết ấy mà {'không ' if neg else ''}{x}"


def nana(t):
    return f"hiểu biết {TH[t]}"


# ---------------------------------------------------------------------------------------------------------------
# Defilements (^5-291, ^5-292)
# ---------------------------------------------------------------------------------------------------------------
AR, AN, SA, SO, PU = (S.PN["arahā"], S.PN["anāgāmī"], S.PN["sakadāgāmī"], S.PN["sotāpanno"],
                      "người phàm phu")              # (pi-4; puthujjano: ch4)
KIL10 = [("sự tham đắm", "có tham đắm"), ("sự sân hận", "có sân hận"), ("sự si mê", "có si mê"),
         ("sự kiêu mạn", "có kiêu mạn"), ("quan điểm", "có quan điểm"), ("sự hoài nghi", "có hoài nghi"),
         ("sự uể oải", "có uể oải"), ("sự xao động", "có xao động"),
         ("sự không biết hổ thẹn", "có sự không biết hổ thẹn"),
         ("sự không biết ghê sợ tội lỗi", "có sự không biết ghê sợ tội lỗi")]
#   rāgo sarāgo, doso sadoso, moho samoho («có tham đắm / sân hận / si mê»: pi-2), māno samāno, diṭṭhi sadiṭṭhiko,
#   vicikicchā savicikiccho, thinaṃ sathino, uddhaccaṃ sauddhacco, ahirikaṃ saahiriko, anottappaṃ saanottappī
SKD = "quan điểm về tự ngã"                           # sakkāyadiṭṭhi (pi-1)
VIC = "sự hoài nghi"                                  # vicikicchā (pi-1)
SBP = "sự hiểu sai lệch về giới hạnh và nghi thức"    # sīlabbataparāmāso (pi-1)
ANU_K, ANU_B = "sự tham đắm dục lạc ở dạng nhỏ nhiệm", "ác ý ở dạng nhỏ nhiệm"   # aṇusahagato kāmarāgo / byāpādo (ch2)
OLA_K, OLA_B = "sự tham đắm dục lạc ở dạng thô", "ác ý ở dạng thô"               # oḷāriko kāmarāgo / byāpādo (ch2)
APA = {"r": "sự tham đắm dẫn đến cõi khổ", "d": "sự sân hận dẫn đến cõi khổ", "m": "sự si mê dẫn đến cõi khổ"}  # ch2
ANOTT = "là người không biết ghê sợ tội lỗi"          # anottappī
ANOTT_N = "không phải là người không biết ghê sợ tội lỗi"
BYAP, BYAP_N = "có tâm ác ý", "không có tâm ác ý"     # byāpannacitto (ch3 abyāpannacittā «có tâm không ác ý»)


def tq(x):                          # atīto X
    return f"{x} {TH[PAST]}"


def has(gen, kil):                  # Y-ssa atīto X atthi
    return f"{tq(kil)} của {gen} {EX}"


def by_k(who, adj, inst, neg=False):   # (na ca) Y tena X-ena adj
    return f"{'nhưng ' if neg else ''}{who} {adj} do {inst} ấy"


# ---------------------------------------------------------------------------------------------------------------
# Body (^5-293), groups (^5-294)
# ---------------------------------------------------------------------------------------------------------------
BAND = ("có thể trói thân thuộc quá khứ bằng sự giam giữ bằng cùm, trói bằng sự giam giữ bằng dây thừng, "
        "trói bằng sự giam giữ bằng xích sắt, trói bằng sự giam giữ trong làng, trói bằng sự giam giữ trong thị trấn, "
        "trói bằng sự giam giữ trong thành phố, trói bằng sự giam giữ trong vùng đất, "
        "trói bằng các dây trói có cổ là thứ năm")
#   labbhā atīto kāyo addubandhanena bandhituṃ … kaṇṭhapañcamehi bandhanehi bandhituṃ («vùng đất»: pi-1 janapada)

# ---------------------------------------------------------------------------------------------------------------
# Suttas (^5-296)
# ---------------------------------------------------------------------------------------------------------------
REST = ("ở nơi bản thân hay ở bên ngoài bản thân, ở dạng thô hay ở dạng vi tế, thấp kém hay ưu việt, "
        "ở xa hay ở gần")                             # ajjhattaṃ vā … yaṃ dūre santike vā (pi-2)
TIME3 = "dù thuộc quá khứ, thuộc tương lai hay thuộc hiện tại"      # atītānāgatapaccuppannaṃ (pi-2)
KHANDHA_DEF = f"bất cứ vật chất nào, {TIME3}, {REST}"               # (pi-2; = ch6)
YA_KACI = ["bất cứ cảm giác nào", "bất cứ tri giác nào", "bất cứ sự tạo tác nào"]   # (pi-2; = ch6)
YAM_VINN = f"bất cứ thức nào, {TIME3}"                              # (pi-2; = ch6)
V_RUPA, V_VINN = "đó được gọi là khối vật chất", "đó được gọi là khối thức"   # ayaṃ vuccati … (pi-2; = ch6)
SUTTA_KHANDHA = (f"Này các tỳ-khưu, {KHANDHA_DEF} – {V_RUPA}. {cap(YA_KACI[0])}{PE} {YA_KACI[1]}{PE} "
                 f"{YA_KACI[2]}{PE} {YAM_VINN}, {REST} – {V_VINN}")
TAYO = "ba phạm vi của cách diễn đạt, phạm vi của tên gọi, phạm vi của sự định danh"
#   tayo niruttipathā adhivacanapathā paññattipathā («phạm vi của cách diễn đạt / tên gọi»: pi-1; paññatti: termbase)
TAYOME = f"Này các tỳ-khưu, đây là {TAYO}"            # tayome, bhikkhave / ime kho, bhikkhave, tayo (ch6 head)
QUAL = ("không lẫn lộn, trước đây chưa từng lẫn lộn, nay không bị lẫn lộn, sẽ không bị lẫn lộn, "
        "không bị phản đối bởi các sa-môn, bà-la-môn có trí")
#   asaṅkiṇṇā asaṅkiṇṇapubbā na saṅkiyanti na saṅkiyissanti appaṭikuṭṭhā samaṇehi brāhmaṇehi viññūhi
WAS, IS, WILL = "đã tồn tại", "tồn tại", "sẽ tồn tại"   # ahosi / atthi / bhavissati


def naming(x, n1, n2):              # ‘x’ti tassa saṅkhā, … samaññā, … paññatti; na tassa saṅkhā ‘n1’ti, … ‘n2’ti
    return (f"thì cách gọi của nó là ‘{x}’, danh xưng chung của nó là ‘{x}’, sự định danh của nó là ‘{x}’; "
            f"cách gọi của nó không phải là ‘{n1}’, cách gọi của nó không phải là ‘{n2}’")


OTHERS = f"Cảm giác nào{PE} tri giác nào{PE} những tạo tác nào{PE} thức nào"   # Yā vedanā…pe… yā saññā… ye saṅkhārā… yaṃ viññāṇaṃ
PASTQ = "thuộc quá khứ, đã chấm dứt, đã mất đi, đã biến đổi"      # atītaṃ niruddhaṃ vigataṃ vipariṇataṃ
PHAG = "Phả-cầu-na"                                   # phagguno / phagguna (termbase)
BUDDHE = ("các vị Phật thuộc quá khứ, đã nhập Niết-bàn trọn vẹn, đã cắt đứt sự suy diễn lan man, "
          "đã cắt đứt lối mòn, đã làm cạn kiệt vòng xoay, đã vượt qua mọi khổ đau")
#   atīte buddhe parinibbute chinnapapañce chinnavaṭume pariyādinnavaṭṭe sabbadukkhavītivatte
DESC = f"khi mô tả {BUDDHE}, có thể mô tả được"       # … paññāpayamāno paññāpeyya
FOOD = "thức ăn trong vai trò dưỡng chất"            # kabaḷīkāre āhāre (pi-1 kabaḷīkāro āhāro)
FOODS3 = ["sự tiếp xúc trong vai trò dưỡng chất", "chủ ý của ý trong vai trò dưỡng chất",
          "thức trong vai trò dưỡng chất"]           # phasse / manosañcetanāya / viññāṇe … āhāre (pi-1)
NR = "sự hình thành của phần tinh thần và vật chất"  # nāmarūpassa avakkanti
VUD = "sự tăng trưởng của các tạo tác"                 # saṅkhārānaṃ vuddhi
PUN = "sự phát sinh rõ rệt của sự hiện hữu mới trong tương lai"   # āyatiṃ punabbhavābhinibbatti
JJM = "sự sinh, sự lão hóa và sự chết trong tương lai"            # āyatiṃ jātijarāmaraṇaṃ
VADAMI = "Ta nói rằng"                                # … vadāmi (ch4)
SADARA = S.var(f"{S.CIT['saṃ. ni.']} 2.64", "sadaraṃ")[:-1] + "; chính cách đọc ấy hợp lý hơn]"
#   [sadaraṃ (saṃ. ni. 2.64) tadeva yuttataraṃ]

REUSED5 = [  # (Pāli, Vietnamese, book)
    ("niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ", PAST5, "1"),
    ("ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ", FUT6, "1"),
    ("jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ", PRES6, "1"),
    ("nicco dhuvo sassato avipariṇāmadhammo", NICCA, "2"),
    ("yaṃ kiñci rūpaṃ atītānāgatapaccuppannaṃ … yaṃ dūre santike vā", KHANDHA_DEF, "2"),
    ("ayaṃ vuccati rūpakkhandho", V_RUPA, "2"), ("ayaṃ vuccati viññāṇakkhandho", V_VINN, "2"),
    ("yā kāci vedanā", YA_KACI[0], "2"), ("yā kāci saññā", YA_KACI[1], "2"),
    ("ye keci saṅkhārā", YA_KACI[2], "2"), ("yaṃ kiñci viññāṇaṃ atītānāgatapaccuppannaṃ", YAM_VINN, "2"),
    ("kabaḷīkāro āhāro", FOOD, "1"), ("phassāhāro", FOODS3[0], "1"), ("manosañcetanāhāro", FOODS3[1], "1"),
    ("viññāṇāhāro", FOODS3[2], "1"),
    ("niruttipathā", "phạm vi của cách diễn đạt", "1"), ("adhivacanapathā", "phạm vi của tên gọi", "1"),
    ("samaññā", "danh xưng chung", "1"),
    ("pañcakkhandhā", "năm khối", "2"), ("dvādasāyatanāni", "mười hai lĩnh vực nhận biết", "2"),
    ("aṭṭhārasa dhātuyo", "mười tám yếu tố", "2"), ("bāvīsatindriyāni", "hai mươi hai năng lực", "2"),
    ("sarāgaṃ", "có tham đắm", "2"), ("sadosaṃ", "có sân hận", "2"), ("samohaṃ", "có si mê", "2"),
    ("ahirikaṃ", "sự không biết hổ thẹn", "1"), ("anottappaṃ", "sự không biết ghê sợ tội lỗi", "1"),
    ("sakkāyadiṭṭhi", SKD, "1"), ("vicikicchā", VIC, "1"), ("sīlabbataparāmāso", SBP, "1"),
    ("rājā cakkavattī", "vua chuyển luân", "2"),
    ("Taṃ kissa hetu?", "Vì sao vậy?", "2"),
    ("siyā", "đôi khi", "2"),
    ("janapade", "vùng đất", "1"),
    ("natthi (neso natthīti)", "không tồn tại", "2"),
]
CH = {  # strings shared with finished pi-5 rails chapters: (file, Vietnamese)
    "1-puggalakatha.md": ["cái tồn tại", "cái không tồn tại", S.KAYA_K],
    "2-parihanikatha.md": ["lập luận dựa trên học thuyết", APA["r"], ANU_K, ANU_B, OLA_K, OLA_B],
    "3-brahmacariyakatha.md": ["có tâm không ác ý"],
    "4-jahatikatha.md": [PU, VADAMI, "Vì sao vậy?"],
    "6-atitakkhandhadikatha.md": [f"{TAYOME[:-len('phạm vi của sự định danh')]}", KHANDHA_DEF, V_RUPA, V_VINN,
                                  YA_KACI[2], YAM_VINN, f"{SANKHARA} {TH[PAST]}", f"{th(RUPA, PAST)} {EX}",
                                  f"{th(VINNANA, PAST)} {EX}", "Chứng cứ từ kinh", "các khối quá khứ"],
}


def check_reused5():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                          for p in sorted(d.glob("*.md")))).lower()
    bad = [(p, v, b) for p, v, b in REUSED5 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for f, vs in CH.items():
        matches = sorted(S.OUT_DIR.glob(f))
        assert matches, f"finished chapter missing: {f}"
        t = unicodedata.normalize("NFC", matches[0].read_text(encoding="utf-8")).lower()
        bad += [(f, v) for v in vs if unicodedata.normalize("NFC", v).lower() not in t]
    assert not bad, "strings not found in finished pi-5 chapters: " + repr(bad)
    assert S.KAYA_K.endswith(appiya("thân")), "appiya frame differs from the sample"


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def head(i, level, text):
        add(i, "#" * level + " " + text)

    head("5-5-0", 3, H_KATHA)

    # ---- Vādayutti ^5-282 -------------------------------------------------------------------------------------
    head("5-5-1-0", 4, H["Vādayutti"])
    ditthi = (f"quan điểm nào cho rằng {ALL}, quan điểm ấy là quan điểm sai lầm, quan điểm nào, quan điểm ấy là "
              f"quan điểm đúng đắn, điều ấy {EX} như vậy")
    qs = [f"{ALL} ở mọi nơi", f"{ALL} vào mọi lúc", f"{ALL} theo mọi cách", f"{ALL} trong mọi thứ",
          f"vì cho rằng không có sự kết hợp, {ALL}", f"cái gì {NEX}, cái ấy cũng {EX}", ditthi]
    l5 = " ".join(f"{Q(ALL)} {YES} {Q(x)} {NO}" for x in qs) + f" {S.SAMKHITTAM}. {H['Vādayutti']}."
    add("5-282", l5)

    # ---- Kālasaṃsandanā ^5-283 … ^5-287 ---------------------------------------------------------------------
    head("5-5-2-0", 4, H["Kālasaṃsandanā"])
    add("5-283",
        f"{Q(f'{PAST} {EX}')} {YES} {NANU(f'{PAST} {PAST5}')} {YES} {S.hanci_neg(f'{PAST} {PAST5}', f'{PAST} {EX}')}",
        f"{Q(f'{FUT} {EX}')} {YES} {NANU(f'{FUT} {FUT6}')} {YES} {S.hanci_neg(f'{FUT} {FUT6}', f'{FUT} {EX}')}",
        f"{Q(ex2(PRES, NPAST5))} {YES} {Q(ex2(PAST, NPAST5))} {NO_PE} {q(ex2(PRES, PRES6))} {YES} "
        f"{Q(ex2(FUT, PRES6))} {NO_PE}",
        f"{Q(ex2(PAST, PAST5))} {YES} {Q(ex2(PRES, PAST5))} {NO_PE} {q(ex2(FUT, FUT6))} {YES} "
        f"{Q(ex2(PRES, FUT6))} {NO}")

    r = {t: th(RUPA, t) for t in TH}
    v = {t: th(VINNANA, t) for t in TH}
    lead = f"{th(VEDANA, PAST)} {EX}{PE} {SANNA} {EX}, {SANKHARA} {EX}, {VINNANA} {EX}"
    #   Atītā vedanā atthi…pe… saññā atthi, saṅkhārā atthi, viññāṇaṃ atthi
    add("5-284",
        f"{Q(f'{r[PAST]} {EX}')} {YES} {NANU(f'{r[PAST]} {PAST5}')} {YES} "
        f"{S.hanci_neg(f'{r[PAST]} {PAST5_S}', f'{r[PAST]} {EX}')}",
        f"{Q(f'{r[FUT]} {EX}')} {YES} {NANU(f'{r[FUT]} {FUT6}')} {YES} "
        f"{S.hanci_neg(f'{r[FUT]} {FUT6_S}', f'{r[FUT]} {EX}')}",
        f"{Q(ex2(r[PRES], NPAST5))} {YES} {Q(ex2(r[PAST], NPAST5))} {NO}",
        f"{Q(ex2(r[PRES], PRES6))} {YES} {Q(ex2(r[FUT], PRES6))} {NO}",
        f"{Q(ex2(r[PAST], PAST5))} {YES} {Q(ex2(r[PRES], PAST5))} {NO}",
        f"{Q(ex2(r[FUT], FUT6))} {YES} {Q(ex2(r[PRES], FUT6))} {NO}",
        f"{Q(lead)} {YES} {NANU(f'{v[PAST]} {PAST5}')} {YES} "
        f"{S.hanci_neg(f'{v[PAST]} {PAST5_S}', f'{v[PAST]} {EX}')}",
        f"{Q(f'{v[FUT]} {EX}')} {YES} {NANU(f'{v[FUT]} {FUT6}')} {YES} "
        f"{S.hanci_neg(f'{v[FUT]} {FUT6_S}', f'{v[FUT]} {EX}')}",
        f"{Q(ex2(v[PRES], NPAST5_S))} {YES} {Q(ex2(v[PAST], NPAST5_S))} {NO}",
        f"{Q(ex2(v[PRES], PRES6_S))} {YES} {Q(ex2(v[FUT], PRES6_S))} {NO}",
        f"{Q(ex2(v[PAST], PAST5_S))} {YES} {Q(ex2(v[PRES], PAST5_S))} {NO} {Q(ex2(v[FUT], FUT6_S))} {YES}",
        f"{Q(ex2(v[PRES], FUT6_S))} {NO}")

    def odata(a, b, subj, prt, s1, s2, neg, end):
        q1 = f"{subj}, {prt}, {'không ' if neg else ''}dứt bỏ trạng thái {s1}"
        q2 = f"{'không ' if neg else ''}dứt bỏ trạng thái {s2}"
        return f"Có phải {goi(a, b)}, {appiya(subj)} không? {YES} {Q(q1)} {YES} {Q(q2)} {end}"

    add("5-285",
        odata(PRES, RUPA, r[PRES], "khi đang chấm dứt", PRES, RUPA, False, NO_PE),
        odata(PRES, RUPA, r[PRES], "khi đang chấm dứt", RUPA, PRES, True, NO_PE),
        odata("màu trắng", "vải", "vải màu trắng", "khi đang được nhuộm", "màu trắng", "vải", False, NO),
        odata("màu trắng", "vải", "vải màu trắng", "khi đang được nhuộm", "vải", "màu trắng", True, NO_PE))
    #   last line: "Na hevaṃ vattabbe.…Pe…." rendered as …pe… (no «.…»)

    njr, njn = nj(RUPA, RUPA), nj(NB, NB)
    add("5-286",
        f"{Q(njr)} {YES} {Q(f'{RUPA} {NICCA}')} {NO} {NANU(f'{njr}, {RUPA} {ANICCA4}')} {YES} "
        f"{S.hanci_neg(f'{RUPA} {ANICCA4}', njr)}",
        f"{Q(f'{njn}, {NB} {NICCA}')} {YES} {Q(f'{njr}{VSK}, {RUPA} {NICCA}')} {NO_PE} "
        f"{q(f'{njr}, {RUPA} {ANICCA4}')} {YES} {Q(f'{njn}, {NB} {ANICCA4}')} {NO_PE}",
        f"{Q(exj(PAST, PAST))} {YES} {Q(exj(FUT, FUT))} {NO} {Q(exj(PAST, PAST))} {YES} "
        f"{Q(exj(PRES, PRES))} {NO_PE}",
        f"{Q(exj(FUT, FUT, False) + VB)} {YES} {Q(exj(PAST, PAST, False) + VB)} {NO_PE}",
        f"{Q(exj(PRES, PRES, False) + VB)} {YES} {Q(exj(PAST, PAST, False) + VB)} {NO}",
        f"{Q(exj(PAST, PAST))} {YES} {Q(f'{PAST} {NICCA}')} {NO_PE} {nanu_l(f'{PAST} {ANICCA4}')} {YES} "
        f"{S.hanci_neg(f'{PAST} {ANICCA4}', exj(PAST, PAST))}",
        f"{Q(f'{exj(NB, NB)}, {NB} {NICCA}')} {YES} {Q(f'{exj(PAST, PAST)}, {PAST} {NICCA}')} {NO_PE}",
        f"{Q(f'{exj(PAST, PAST)}, {PAST} {ANICCA4}')} {YES} {Q(f'{exj(NB, NB)}, {NB} {ANICCA4}')} {NO_PE}")

    def blk287(s, lead_q, var42, short44):
        sP, sF, sR = s[PAST], s[FUT], s[PRES]
        hanci_p = f"{sP} {ANICCA4_S if short44 else ANICCA4}"
        return [
            f"{Q(lead_q + exj(sP, PAST))} {YES} {Q(exj(sF, FUT))} {NO_PE} {q(exj(sP, PAST))} {YES} "
            f"{Q(exj(sR, PRES))} {NO_PE}",
            f"{Q(exj(sF, FUT, False) + var42)} {YES} {Q(exj(sP, PAST, False) + var42)} {NO_PE}",
            f"{Q(exj(sR, PRES, False) + VA)} {YES} {Q(exj(sP, PAST, False) + VA)} {NO_PE}",
            f"{Q(exj(sP, PAST))} {YES} {Q(f'{sP} {NICCA}')} {NO_PE} {nanu_l(f'{sP} {ANICCA4}')} {YES} "
            f"{S.hanci_neg(hanci_p, exj(sP, PAST))}",
            f"{Q(f'{exj(NB, NB)}{VP}, {NB} {NICCA}')} {YES} {Q(f'{exj(sP, PAST)}{VP}, {sP} {NICCA}')} {NO_PE}",
            f"{Q(f'{exj(sP, PAST)}, {sP} {ANICCA4}')} {YES} {Q(f'{exj(NB, NB)}, {NB} {ANICCA4}')} {NO_PE}"]

    lead47 = (f"{th(VEDANA, PAST)} {EX}{PE} {th(SANNA, PAST)} {EX}{PE} {th(SANKHARA, PAST)} {EX}{PE} ")
    #   Atītā vedanā atthi… atītā saññā atthi… atītā saṅkhārā atthi…
    add("5-287", *blk287(r, "", VA, True), *blk287(v, lead47, "", False))

    # ---- Vacanasodhanā ^5-288 ---------------------------------------------------------------------------------
    head("5-5-3-0", 4, H["Vacanasodhanā"])

    def nvatthi(x):
        return (f"{Q(f'{x} {NEX}')} {YES} Nếu {x} {NEX}, thì sai khi nói rằng {x} {EX}. "
                f"Hoặc nếu {CAI_EX} không phải là {x}, thì sai khi nói rằng {CAI_EX} là {x}.")

    HH = "là rồi trở thành, là rồi trở thành"                       # hutvā hoti hutvā hoti
    NHH = "không là rồi không trở thành, không là rồi không trở thành"   # na hutvā na hoti na hutvā na hoti

    def hutva(a, b, end):
        return (f"{Q(a)} {YES} {Q(b)} {NO_PE} {q(b)} {YES} {Q(HH)} {NO_PE} {q(HH)} {YES} {Q(NHH)} {end}")

    add("5-288",
        f"{nvatthi(PAST)} {nvatthi(FUT)}",
        hutva(f"là {FUT} rồi trở thành {PRES}", f"chính cái {FUT} ấy là cái {PRES} ấy", NO_PE),
        hutva(f"là {PRES} rồi trở thành {PAST}", f"chính cái {PRES} ấy là cái {PAST} ấy", NO_PE),
        hutva(f"là {FUT} rồi trở thành {PRES}, là {PRES} rồi trở thành {PAST}",
              f"chính cái {FUT} ấy là cái {PRES} ấy, là cái {PAST} ấy", NO))

    # ---- Atītacakkhurūpādikathā ^5-289 ------------------------------------------------------------------------
    head("5-5-4-0", 4, H["Atītacakkhurūpādikathā"])
    l63 = " ".join(f"{(Q if k == 0 else q)(five(PAST, k))} {YES} {Q(see(PAST, k))} {NO_PE}" for k in range(6))
    l64 = f"{Q(five(FUT, 0))} {YES} {Q(see(FUT, 0))} {NO_PE} {q(chain(FUT))} {YES} {Q(see(FUT, 5))} {NO_PE}"

    def pair289(t1, t2, neg, low3):
        return (f"{Q(f'{five(t1, 0)}, {see(t1, 0, neg)}')} {YES} {Q(f'{five(t2, 0)}, {see(t2, 0, neg)}')} {NO_PE} "
                f"{(q if low3 else Q)(f'{chain(t1)}, {see(t1, 5, neg)}')} {YES} "
                f"{Q(f'{five(t2, 5)}, {see(t2, 5, neg)}')} {NO_PE}")

    add("5-289", l63, l64, pair289(PRES, PAST, False, False), pair289(PRES, FUT, False, True),
        pair289(PAST, PRES, True, True), pair289(FUT, PRES, True, True))
    #   line 3: "…pe…. Paccuppannaṃ sotaṃ" (capital) → Q; lines 4-6: "…pe… paccuppannaṃ / atītaṃ / anāgataṃ" → q

    # ---- Atītañāṇādikathā ^5-290 ------------------------------------------------------------------------------
    head("5-5-5-0", 4, H["Atītañāṇādikathā"])

    def one(t):
        return (f"{Q(f'{nana(t)} {EX}')} {YES} {Q(by_n(FN))} {NO_PE} {q(by_n(FN))} {YES} {Q(by_n(F4))} {NO_PE}")

    def pn(t1, t2, x, neg, low=True):
        return (f"{(q if low else Q)(f'{nana(t1)} {EX}, {by_n(x, neg)}')} {YES} "
                f"{Q(f'{nana(t2)} {EX}, {by_n(x, neg)}')} {NO_PE}")

    add("5-290", one(PAST), one(FUT),
        " ".join([pn(PRES, PAST, FN, False, False), pn(PRES, PAST, F4, False), pn(PRES, FUT, FN, False),
                  pn(PRES, FUT, F4, False)]),
        f"{pn(PAST, PRES, FN, True, False)} {pn(PAST, PRES, F4, True)}",
        f"{pn(FUT, PRES, FN, True, False)} {pn(FUT, PRES, F4, True, False)}")
    #   last line: "…pe…. Anāgataṃ ñāṇaṃ" (capital) → Q

    # ---- Arahantādikathā ^5-291, ^5-292 -----------------------------------------------------------------------
    head("5-5-6-0", 4, H["Arahantādikathā"])
    l80 = " ".join(f"{(Q if k == 0 else q)(has(AR, kil))} {YES} {Q(by_k(AR, adj, kil))} {NO_PE}"
                   for k, (kil, adj) in enumerate(KIL10))

    def ariya(gen, who, items, adj, inst):
        rest = f"{PE} ".join(f"{tq(x)} {EX}" for x in items[1:])
        return (f"{Q(has(gen, SKD))} {YES} {Q(by_k(who, 'có quan điểm', 'quan điểm'))} {NO_PE} "
                f"{q(f'{has(gen, VIC)}{PE} {rest}')} {YES} {Q(by_k(who, adj, inst))} {NO_PE}")

    add("5-291", l80,
        ariya(AN, AN,[VIC, SBP, ANU_K, ANU_B], BYAP, "ác ý"),
        ariya(SA, SA, [VIC, SBP, OLA_K, OLA_B], BYAP, "ác ý"),
        ariya(SO, SO, [VIC, SBP, APA["r"], APA["d"], APA["m"]], "có si mê", "sự si mê"))

    def hp(gen, kil, who, adj, inst, neg=False):
        return f"{has(gen, kil)}, {by_k(who, adj, inst, neg)}"

    def cmp(g1, g2, first, last, neg):
        """first = (kil, adj, adj_neg, inst); last = (kil, adj, adj_neg, inst) after the …pe… chain."""
        k1, a1, n1, i1 = first
        k2, a2, n2, i2 = last
        A1, A2 = (n1, n2) if neg else (a1, a2)
        mid = VIC if k1 == SKD else "sự sân hận"
        return (f"{Q(hp(g1, k1, g1, A1, i1, neg))} {YES} {Q(hp(g2, k1, g2, A1, i1, neg))} {NO_PE} "
                f"{q(f'{has(g1, mid)}{PE} {tq(k2)} {EX}, {by_k(g1, A2, i2, neg)}')} {YES} "
                f"{Q(hp(g2, k2, g2, A2, i2, neg))} {NO_PE}")

    RAGA = ("sự tham đắm", "có tham đắm", "không có tham đắm", "sự tham đắm")
    ANOT = ("sự không biết ghê sợ tội lỗi", ANOTT, ANOTT_N, "sự không biết ghê sợ tội lỗi")
    SKDT = (SKD, "có quan điểm", "không có quan điểm", "quan điểm")
    B_AN = (ANU_B, BYAP, BYAP_N, "ác ý")
    B_OL = (OLA_B, BYAP, BYAP_N, "ác ý")
    M_AP = (APA["m"], "có si mê", "không có si mê", "sự si mê")
    lines292 = []
    for neg in (False, True):
        for other, first, last in ((AR, RAGA, ANOT), (AN, SKDT, B_AN), (SA, SKDT, B_OL), (SO, SKDT, M_AP)):
            lines292.append(cmp(other, PU, first, last, True) if neg else cmp(PU, other, first, last, False))
    add("5-292", *lines292)

    # ---- Atītahatthādikathā ^5-293 ----------------------------------------------------------------------------
    head("5-5-7-0", 4, H["Atītahatthādikathā"])
    limbs = [("các bàn tay", "việc cầm lên và đặt xuống"), ("các bàn chân", "việc đi tới và đi lui"),
             ("các khớp", "việc co và duỗi"), ("bụng", "sự đói, sự khát")]
    #   hatthā ādānanikkhepanaṃ, pādā abhikkamapaṭikkamo, pabbā samiñjanapasāraṇaṃ, kucchi jighacchā pipāsā
    l96 = " ".join(f"{(Q if k == 0 else q)(f'{tq(x)} {EX}')} {YES} "
                   f"{Q(f'khi {tq(x)} {EX}, {y} được nhận ra')} {NO_PE}" for k, (x, y) in enumerate(limbs))
    kaya = tq("thân")
    l97 = (f"{Q(f'{kaya} {EX}')} {YES} "
           f"{Q(f'{kaya} có thể bị nhấc lên và bị đè xuống, có thể bị cắt và bị đập vỡ, là thứ chung cho quạ, kền kền, diều hâu')} "
           f"{NO_PE} {q(f'chất độc có thể tác động lên {kaya}, dao kiếm có thể tác động, lửa có thể tác động')} "
           f"{NO_PE} {q(BAND)} {NO_PE}")
    l98 = " ".join(f"{(Q if k == 0 else q)(f'{tq(x)} {EX}')} {YES} {Q(f'bằng {x} ấy mà làm việc của {x}')} {NO_PE}"
                   for k, x in enumerate(("nước", "lửa", "gió")))
    add("5-293", l96, l97, l98)

    # ---- Atītakkhandhādisamodhānakathā ^5-294 ----------------------------------------------------------------
    head("5-5-8-0", 4, H["Atītakkhandhādisamodhānakathā"])

    def three(x):
        return ", ".join(f"{th(x, t)} {EX}" for t in (PAST, FUT, PRES))

    def grp(one_, n3, all_, n_all):
        return (f"{Q(three(one_))} {YES} {Q(f'có ba {n3}')} {NO_PE} {q(three(all_))} {YES} "
                f"{Q(f'có {n_all}')} {NO_PE}")

    add("5-294",
        grp("khối vật chất", "khối vật chất", "năm khối", "mười lăm khối"),
        grp(S.A["cakkhāyatana"], S.A["cakkhāyatana"], "mười hai lĩnh vực nhận biết",
            "ba mươi sáu lĩnh vực nhận biết"),
        grp(S.D["cakkhudhātu"], S.D["cakkhudhātu"], "mười tám yếu tố", "năm mươi bốn yếu tố"),
        grp(S.I["cakkhundriya"], S.I["cakkhundriya"], "hai mươi hai năng lực", "sáu mươi sáu năng lực"),
        f"{Q(three('vua chuyển luân'))} {YES} "
        f"{Q('có sự cùng hiện diện đối mặt nhau của ba vị vua chuyển luân')} {NO_PE}",
        f"{Q(three('bậc Tự Giác Ngộ Hoàn Toàn'))} {YES} "
        f"{Q('có sự cùng hiện diện đối mặt nhau của ba bậc Tự Giác Ngộ Hoàn Toàn')} {NO_PE}")
    #   line 1: stray space in "vattabbe …pe…"; line 6: "sammāsammuddho" (slip for sammāsambuddho)

    # ---- Padasodhanakathā ^5-295 ------------------------------------------------------------------------------
    head("5-5-9-0", 4, H["Padasodhanakathā"])

    def pada(x, first=None):
        nx = f"không phải là {x}"
        siya = f"{CAI_EX} đôi khi là {x}, đôi khi {nx}"
        tena = f"do đó {x} {nx}, cái {nx} là {x}"
        yam = f"Điều bạn nói ở đây là sai – “nên nói – ‘{x} {EX}, {siya}, {tena}’”."
        l1 = first or f"{Q(f'{x} {EX}')} {YES}"
        return [f"{l1} {Q(f'{CAI_EX} là {x}')} {cap(siya)}.",
                f"{S.ADMIT['niggaha']} Nếu {x} {EX}, {siya}, thì {tena}. {yam}",
                f"Còn nếu không phải rằng {x} {nx}, cái {nx} là {x}, thì {S.RE}, chắc chắn không nên nói – "
                f"“{x} {EX}, {siya}”. {yam}"]

    add("5-295", *pada(PAST), *pada(FUT), *pada(PRES, first=f"Có phải {PRES} {EX} không, đúng vậy."), *pada(NB))
    #   line 7: "Paccuppannaṃ atthīti, āmantā." kept as written (comma, lower case)

    # ---- Suttasādhanaṃ ^5-296 ---------------------------------------------------------------------------------
    head("5-5-10-0", 4, H["Suttasādhanaṃ"])
    pf = f"{PAST} {EX}, {FUT} {EX}"                   # atītaṃ atthi, anāgataṃ atthi
    cit = S.CIT["saṃ. ni."]
    l126 = (f"{S.na_vattabbam(pf)} {YES} {S.NANU_VUTTAM} “{SUTTA_KHANDHA}” [{cit} 3.48]. {S.ATTHEVA} {YES} "
            f"{S.tena_hi(pf)}")
    l127 = (f"{Q(pf)} {YES} {S.NANU_VUTTAM} “{TAYOME}, {QUAL}. Ba phạm vi nào? Này các tỳ-khưu, vật chất nào "
            f"{PASTQ}, {naming(WAS, IS, WILL)}. {OTHERS} {PASTQ}, {naming(WAS, IS, WILL)}.")
    l128 = (f"“Này các tỳ-khưu, vật chất nào chưa sinh ra, chưa hiện ra, {naming(WILL, IS, WAS)}. {OTHERS} "
            f"chưa sinh ra, chưa hiện ra, {naming(WILL, IS, WAS)}.")
    l129 = (f"“Này các tỳ-khưu, vật chất nào đã sinh ra, đã hiện ra, {naming(IS, WAS, WILL)}. {OTHERS} "
            f"đã sinh ra, đã hiện ra, {naming(IS, WAS, WILL)}. {TAYOME}, {QUAL}.")
    l130 = ("“Này các tỳ-khưu, ngay cả những người Vát-sa và Băn-nha ở Ục-ca-la trước kia, những người theo "
            "học thuyết không có nguyên nhân, những người theo học thuyết không có hành động, những người theo "
            f"học thuyết hư vô, họ cũng đã nghĩ rằng {TAYO} này không nên chê trách, không nên phản đối. "
            f"Vì sao vậy? Vì sợ bị chê bai, bị công kích, bị chỉ trích” [{cit}]. {S.ATTHEVA} {YES} "
            f"{S.tena_hi_na(pf)}")
    l131 = (f"{Q(f'{PAST} {EX}')} {YES} Chẳng phải tôn giả {PHAG} đã nói với Đức Thế Tôn thế này sao – "
            f"“Bạch Thế Tôn, có tồn tại con mắt mà bằng con mắt ấy, {DESC} không. Bạch Thế Tôn, có tồn tại "
            f"cái lưỡi{PE} bạch Thế Tôn, có tồn tại cái ý mà bằng cái ý ấy, {DESC} không”.")
    l132 = (f"“Này {PHAG}, không tồn tại con mắt mà bằng con mắt ấy, {DESC}. Này {PHAG}, không tồn tại cái lưỡi"
            f"{PE} này {PHAG}, không tồn tại cái ý mà bằng cái ý ấy, {DESC}” [{cit} 4.83]. {S.ATTHEVA} {YES} "
            f"{S.tena_hi_na(f'{PAST} {EX}')}")
    nand = "điều ấy đã là bất thiện, nay nó không tồn tại, như vậy đó là thiện"
    l133 = (f"{Q(f'{PAST} {EX}')} {YES} Chẳng phải tôn giả Nan-đa-ka đã nói thế này sao – “Trước đây sự tham lam "
            f"đã tồn tại, {nand}. Trước đây sự sân hận đã tồn tại{PE} trước đây sự si mê đã tồn tại, {nand}” "
            f"[{S.CIT['a. ni.']}]. {S.ATTHEVA} {YES} {S.tena_hi_na(f'{PAST} {EX}')}")

    def food_chain(e, pt, gr, end):
        """e = «tồn tại» / «không tồn tại»; pt / gr = «được thiết lập» / «phát triển» (or negated)."""
        return (f"Này các tỳ-khưu, nếu đối với {FOOD} mà sự tham đắm {e}, sự thích thú {e}, khao khát {e}; "
                f"ở đó thức {pt} và {gr}. Nơi nào thức {pt} và {gr}, ở đó {NR} {e}. Nơi nào {NR} {e}, "
                f"ở đó {VUD} {e}. Nơi nào {VUD} {e}, ở đó {PUN} {e}. Nơi nào {PUN} {e}, ở đó {JJM} {e}. "
                f"Nơi nào {JJM} {e}, này các tỳ-khưu, {VADAMI} {end}.")

    def foods(e, tail):
        return (f"“Này các tỳ-khưu, nếu đối với {FOODS3[0]}{PE} này các tỳ-khưu, nếu đối với {FOODS3[1]}{PE} "
                f"này các tỳ-khưu, nếu đối với {FOODS3[2]} mà sự tham đắm {e}, sự thích thú {e}{PE} "
                f"{VADAMI} {tail}” [{cit} 2.64].")

    l134 = (f"{S.na_vattabbam(f'{FUT} {EX}')} {YES} {S.NANU_VUTTAM} “"
            + food_chain(EX, "được thiết lập", "phát triển",
                         f"điều ấy có sầu muộn, có bụi bặm{SADARA}, có tuyệt vọng"))
    l135 = f"{foods(EX, 'có bụi bặm, có tuyệt vọng')} {S.ATTHEVA} {YES} {S.tena_hi(f'{FUT} {EX}')}"
    l136 = (f"{Q(f'{FUT} {EX}')} {YES} {S.NANU_VUTTAM} “"
            + food_chain(NEX, "không được thiết lập", "không phát triển",
                         "điều ấy không có sầu muộn, không có bụi bặm, không có tuyệt vọng"))
    l137 = (f"{foods(NEX, 'không có bụi bặm, không có tuyệt vọng')} {S.ATTHEVA} {YES} "
            f"{S.tena_hi_na(f'{FUT} {EX}')}")
    add("5-296", l126, l127, l128, l129, l130, l131, l132, l133, l134, l135, l136, l137, END_KATHA)
    return segs


def main():
    check_reused5()
    segs = build()
    # S.quotes_ok counts a stanza re-opening “ by raw totals, so a NEW quote that opens at a line start after a
    # closed multi-paragraph quote (^5-296 line 7, the Buddha's reply to Phagguna) is miscounted. Run S's own
    # checks with ^5-296 split there (the flat line list, hence the per-line checks, is unchanged), then write as
    # S.write does.
    last = segs[-1]
    cut = next(k for k, ln in enumerate(last) if ln.startswith(f"“Này {PHAG}"))
    S.check_against_pali(NAME, segs[:-1] + [last[:cut], last[cut:]])
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    if "--adh" in sys.argv:          # byte-identical copy for termbase_adherence_vi.py (rails\adh-5\)
        adh = S.FORMULAS_MD.parent / "adh-5"
        adh.mkdir(exist_ok=True)
        (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
        print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
