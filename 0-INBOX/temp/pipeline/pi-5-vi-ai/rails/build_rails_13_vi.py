"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 13, Pañcamavaggo (^5-13-0 … ^5-444): ten kathās
(43-52) with the repeated "Pañcamavaggo" sub-headings, the vagga close, the uddāna and the first fifty-group close
(Mahāpaṇṇāsako. / Tassāpi uddānaṃ – / its uddāna), which is set here for all later fifty-groups.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/13-pancamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, katha, katha_end, vaggo, var, var_sp, rq …). Strings taken from pi-1 … pi-4 rails are asserted there
(REUSED13); strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-13.md.

usage: python -I -X utf8 -B build_rails_13_vi.py          (writes the chapter and the adherence copy rails\\adh-13\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "13-pancamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
rq, cap = S.rq, S.cap

# ---------------------------------------------------------------------------------------------------------------
# Persons, fruits, paths (pi-4 / ch2 / ch3 / ch4 / ch12)
# ---------------------------------------------------------------------------------------------------------------
AR, SO, SA, AN = S.PN["arahā"], S.PN["sotāpanno"], S.PN["sakadāgāmī"], S.PN["anāgāmī"]      # (pi-4)
ARAHATTA = "trạng thái A-la-hán"                                       # arahattaṃ (termbase; ch2)
FR = {"so": "thành quả vào dòng", "sa": "thành quả trở lại một lần", "an": "thành quả không trở lại",
      "ar": "thành quả A-la-hán"}                                      # (ch2; arahattaphala ch12)
PATH_SO = "con đường vào dòng"                                         # sotāpattimagge (termbase; ch4)
PRAC = "người đang thực hành để tự mình chứng nghiệm"                  # X-sacchikiriyāya paṭipanno puggalo (pi-4)
P = {"so": f"{PRAC} {FR['so']}", "sa": f"{PRAC} {FR['sa']}", "an": f"{PRAC} {FR['an']}",
     "ar": f"{PRAC} {ARAHATTA}"}                                       # (pi-4; ar: ch3)
GEN = {"so": SO, "sa": SA, "an": AN, "ar": AR}                         # Sotāpannassa … Arahato (termbase)
GOT = "người chuyển đổi dòng dõi"                                      # gotrabhū puggalo (gotra «dòng dõi»)
CHAIN = f"{P['sa']}{PE} {FR['an']}{PE} {ARAHATTA} có hiểu biết về {ARAHATTA}"
#   sakadāgāmiphala… anāgāmiphala… arahattasacchikiriyāya paṭipannassa puggalassa arahatte ñāṇaṃ atthi
GOT_Q = f"{GOT} có hiểu biết về {PATH_SO}"                             # Gotrabhuno puggalassa sotāpattimagge ñāṇaṃ atthi
SO_Q = f"{P['so']} có hiểu biết về {FR['so']}"                         # … sotāpattiphale ñāṇaṃ atthi
AR_Q = f"{P['ar']} có hiểu biết về {ARAHATTA}"                         # arahatta… arahatte ñāṇaṃ atthi
SARI = "trưởng lão Xá-lợi-phất"                                        # Sāriputto thero (termbase, ch2)
MOGG = "trưởng lão Đại Mục-kiền-liên"                                  # Mahāmoggallāno thero (ch2)
F4 = "hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, tu tập con đường"   # (ch5)
PATHS6 = (f"sự thiết lập tỉnh thức{PE} nỗ lực đúng đắn{PE} nền tảng thần thông{PE} năng lực{PE} sức mạnh{PE} "
          f"chi phần giác ngộ")                                        # satipaṭṭhānā… … bojjhaṅgā (ch12)
GIL = "thuốc men và vật dụng chữa bệnh"                                # gilānapaccayabhesajjaparikkhāra (pi-2, ch12)
LIST10 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "niềm tin", "sự tinh tấn", "sự tỉnh thức",
          "sự định tâm", "trí tuệ"]                                     # phassa … paññā (ch4, ch12)
AO = "sự không biết ghê sợ tội lỗi"                                    # anottappa (pi-1, ch5)

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close, fifty-group close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(5)                                                     # Pañcamavaggo «Chương thứ năm» (termbase)
KATHA = {1: "sự giải thoát", 2: "hiểu biết thuộc về người đã hoàn tất tu học", 3: "điều sai lệch",
         4: "sự cố định", 5: "hiểu biết thông suốt", 6: "hiểu biết theo quy ước", 7: "tâm làm đối tượng",
         8: "hiểu biết về tương lai", 9: "hiện tại", 10: "hiểu biết về thành quả"}
#   Vimuttikathā (termbase), Asekhañāṇakathā, Viparītakathā, Niyāmakathā, Paṭisambhidākathā, Sammutiñāṇakathā,
#   Cittārammaṇakathā, Anāgatañāṇakathā (termbase), Paṭuppannakathā (heading), Phalañāṇakathā (termbase)
END9 = "hiểu biết về hiện tại" + S.var("Sī.", "paccuppannakathā")      # Paṭuppannañāṇakathā [paccuppannakathā (sī.)]
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9)
G12 = "người tại gia có thể là bậc A-la-hán"                           # gihissa arahā (ch12 kathā name)
MAHAPANNASA = "Nhóm năm mươi lớn."                                     # Mahāpaṇṇāsako. (paṇṇāsako «Nhóm năm mươi»)
TASSAPI = "Tóm tắt của nhóm này nữa –"                                 # Tassāpi uddānaṃ –
UDD50 = (f"Sự được tìm thấy của chúng sinh, người đưa đến, sức mạnh, và {G12}, với sự giải thoát là thứ năm.")
#   Sattupaladdhiṃ, upaharato, balaṃ, gihissa arahā ca, vimuttipañcamanti.

# ---------------------------------------------------------------------------------------------------------------
# Theses and recurring phrases
# ---------------------------------------------------------------------------------------------------------------
V = "hiểu biết về sự giải thoát"                                       # vimuttiñāṇaṃ (termbase)
VM = "được giải thoát"                                                 # vimuttaṃ (termbase)
T1 = f"{V} {VM}"                                                       # Vimuttiñāṇaṃ vimuttaṃ
SK, ASK = "người còn đang tu học", "người đã hoàn tất tu học"          # sekho / asekho (termbase Sekhassa, asekha)
AK = f"hiểu biết thuộc về {ASK}"                                       # asekhaṃ ñāṇaṃ
AD = f"hiện tượng thuộc về {ASK}"                                      # asekhaṃ dhammaṃ
T2 = f"{SK} có {AK}"                                                   # sekhassa asekhaṃ ñāṇaṃ atthi
K = "thành tựu thiền với đề mục bao trùm là đất"                       # pathavīkasiṇaṃ samāpattiṃ (termbase, pi-1)
SAMP = f"người đang nhập {K}"                                          # … samāpannassa (termbase)
VT = f"{SAMP} có hiểu biết về điều sai lệch"                           # … samāpannassa viparīte ñāṇaṃ
VTA = f"{VT}, và hiểu biết ấy là bất thiện"                            # …, tañca akusalaṃ
SDA = "sự đảo ngược"                                                   # vipariyeso (termbase)
VIP = {"a": "việc xem điều vô thường là thường còn", "d": "việc xem khổ đau là hạnh phúc",
       "n": "việc xem cái không phải tự ngã là tự ngã", "s": "việc xem điều không đẹp là đẹp"}
#   anicce niccanti / dukkhe sukhanti / anattani attāti / asubhe subhanti
AY, NY = "người không cố định", "người cố định"                        # aniyatassa / niyatassa (termbase niyata)
G, AG = "để đi đến sự cố định", "để đi đến sự không cố định"           # niyāmagamanāya / aniyāmagamanāya
T4 = f"{AY} có hiểu biết {G}"                                          # aniyatassa niyāmagamanāya atthi ñāṇaṃ
PS = "hiểu biết thông suốt"                                            # paṭisambhidā (termbase, pi-2)
TS = f"tất cả hiểu biết là {PS}"                                       # sabbaṃ ñāṇaṃ paṭisambhidā (termbase phrase)
SM = "hiểu biết theo quy ước"                                          # sammutiñāṇaṃ (termbase, pi-2)
CT = "hiểu biết bao quát tâm"                                          # cetopariyāye ñāṇaṃ (termbase)
SMT = f"{SM} chỉ có sự thật làm đối tượng, không có điều khác làm đối tượng"
CTT = f"{CT} chỉ có tâm làm đối tượng, không có điều khác làm đối tượng"
#   … saccārammaṇaññeva / cittārammaṇaññeva na aññārammaṇaṃ
AF = "hiểu biết về tương lai tồn tại"                                  # anāgate ñāṇaṃ atthi
PF = "hiểu biết về hiện tại tồn tại"                                   # paṭuppanne ñāṇaṃ atthi
SV = "vị đệ tử"                                                        # sāvako (termbase)
TF = f"{SV} có hiểu biết về thành quả"                                 # sāvakassa phale ñāṇaṃ atthi
UDDANA = (f"{cap(T1)}, {T2}, hiểu biết về điều sai lệch, {T4}, {TS}, {SM}, {CT}, hiểu biết về tương lai, "
          f"hiểu biết về hiện tại, {TF}.")
#   Vimuttiñāṇaṃ vimuttaṃ, sekhassa asekhaṃ ñāṇaṃ, viparīte ñāṇaṃ, aniyatassa niyāmagamanāya atthi ñāṇaṃ, sabbaṃ ñāṇaṃ
#   paṭisambhidāti, sammutiñāṇaṃ, cetopariyāye ñāṇaṃ, anāgate ñāṇaṃ, paṭuppanne ñāṇaṃ, sāvakassa phale ñāṇanti.

KASINA = ["với đề mục bao trùm là nước", "với đề mục bao trùm là lửa", "với đề mục bao trùm là gió",
          "với đề mục bao trùm màu xanh", "với đề mục bao trùm màu vàng", "với đề mục bao trùm màu đỏ",
          "với đề mục bao trùm màu trắng"]                             # āpokasiṇaṃ … odātakasiṇaṃ (pi-1)
ARUPA = ["lĩnh vực không gian vô tận", "lĩnh vực thức vô tận", "lĩnh vực không có gì cả",
         "lĩnh vực không phải tri giác cũng không phải không tri giác"]   # ākāsānañcāyatanaṃ … (pi-1)
MINDS = ["tâm có tham đắm", "tâm đã lìa tham đắm", "tâm có sân hận", "tâm đã lìa sân hận", "tâm có si mê",
         "tâm đã lìa si mê", "tâm co rút", "tâm tán loạn", "tâm rộng lớn", "tâm không rộng lớn",
         "tâm còn có điều cao hơn", "tâm không có điều gì cao hơn", "tâm được định tâm", "tâm không được định tâm",
         "tâm được giải thoát", "tâm không được giải thoát"]           # sarāgaṃ cittaṃ … avimuttaṃ cittaṃ (pi-2)
PANNATTI6 = ("sự định danh về các khối, sự định danh về các lĩnh vực nhận biết, sự định danh về các yếu tố, "
             "sự định danh về các sự thật, sự định danh về các năng lực, sự định danh về các hạng người")   # (pi-4)

REUSED13 = [  # (Pāli, Vietnamese, book)
    ("upasampajja viharati pathavīkasiṇaṃ", "với đề mục bao trùm là đất", "1"),
    *[(f"{p}kasiṇaṃ", v, "1") for p, v in zip(("āpo", "tejo", "vāyo", "nīla", "pīta", "lohita", "odāta"), KASINA)],
    *[(p, v, "1") for p, v in zip(("ākāsānañcāyatanaṃ", "viññāṇañcāyatanaṃ", "ākiñcaññāyatanaṃ",
                                   "nevasaññānāsaññāyatanaṃ"), ARUPA)],
    *[(f"citta {i}", v, "2") for i, v in enumerate(MINDS, 1)],
    ("paṭisambhidā", PS, "2"), ("sammutiñāṇaṃ", SM, "2"),
    ("niyāmaṃ okkamituṃ", "bước vào sự cố định", "2"),
    ("indriyaparopariyattaṃ", "mức độ cao thấp của các năng lực", "2"),
    ("khandhapaññatti … puggalapaññatti", PANNATTI6, "4"),
    ("sotāpattiphalasacchikiriyāya paṭipanno", P["so"], "4"),
    ("sakadāgāmiphalasacchikiriyāya paṭipanno", P["sa"], "4"),
    ("anāgāmiphalasacchikiriyāya paṭipanno", P["an"], "4"),
    ("anadhigate adhigata-", "đã chứng đắc", "2"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "2"),
    ("cīvara … gilānapaccayabhesajjaparikkhāra", GIL, "2"),
    ("dhammaṃ abhisametuṃ / Giáo Pháp", "Giáo Pháp", "1"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Sāriputto thero", SARI, "2-parihanikatha.md"),
    ("Mahāmoggallāno thero", MOGG, "2-parihanikatha.md"),
    ("mahāva. (citation)", "Đại Phẩm", "2-parihanikatha.md"),
    ("arahattasacchikiriyāya paṭipanno", P["ar"], "3-brahmacariyakatha.md"),
    ("dukkhaṃ parijānāti … maggaṃ bhāveti", F4, "5-sabbamatthitikatha.md"),
    ("tena ñāṇena …", "bằng hiểu biết ấy mà", "5-sabbamatthitikatha.md"),
    ("anottappaṃ", AO, "5-sabbamatthitikatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("Upalabbho (uddāna)", "Sự được tìm thấy", "9-hevatthikatha.md"),
    ("Gihissa arahā", G12, "12-catutthavaggo.md"),
    ("satipaṭṭhānaṃ… … bojjhaṅgo", PATHS6, "12-catutthavaggo.md"),
    ("arahattaphalaṃ", FR["ar"], "12-catutthavaggo.md"),
    ("sotāpattimaggo", PATH_SO, "12-catutthavaggo.md"),
    ("sotāpattiphalaṃ / sakadāgāmiphalaṃ / anāgāmiphalaṃ", FR["an"], "12-catutthavaggo.md"),
    ("gilānapaccayabhesajjaparikkhāraṃ deti", f"cho {GIL}", "12-catutthavaggo.md"),
    ("Catutthavaggo. (close)", "Chương thứ tư.", "12-catutthavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED13 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# Small frames
# ---------------------------------------------------------------------------------------------------------------
def vof(who):                       # X-assa vimuttiñāṇaṃ vimuttaṃ
    return f"{V} của {who} {VM}"


def vof2(who):                      # … vimuttaṃ tañca phalaṃ pattassa ñāṇaṃ
    return f"{vof(who)}, và đó là hiểu biết của người đã đạt đến thành quả"


def known(k):                       # Sotāpannassa ñāṇaṃ, sotāpattiphalaṃ pattassa paṭiladdhassa adhigatassa sacchikatassa ñāṇaṃ
    fr = ARAHATTA if k == "ar" else FR[k]
    return (f"đó là hiểu biết của {GEN[k]}, hiểu biết của người đã đạt đến, đã có được, đã chứng đắc, "
            f"đã tự mình chứng nghiệm {fr}")


def samangi(k):                     # X-phalasamaṅgissa puggalassa (termbase)
    return f"người có được {FR[k]}"


def knows(who, neg=False):          # X asekhaṃ dhammaṃ (na) jānāti (na) passati, … (na) kāyena phusitvā viharati
    if not neg:
        return (f"{who} biết, thấy {AD}, chứng nhập và an trú điều đã thấy, đã biết, đã được tự mình chứng nghiệm, "
                f"chạm đến bằng thân và an trú")
    return (f"{who} không biết, không thấy {AD}, không chứng nhập và an trú điều chưa thấy, chưa biết, "
            f"chưa tự mình chứng nghiệm, không chạm đến bằng thân và an trú")


def has(who, g, neg=False, what="hiểu biết"):   # X-assa Y-gamanāya (n)atthi Z
    return f"{who} {'không ' if neg else ''}có {what} {g}"


def va(k, adj):                     # X vipariyeso, so ca (a)kusalo
    return f"{VIP[k]} là {SDA}, và sự đảo ngược ấy là {adj}"


def ob(x):                          # X-ārammaṇe ñāṇaṃ
    return f"hiểu biết về đối tượng là {x}"


CALL = f"nên được gọi là – “{CT}”"          # vattabbaṃ – "cetopariyāye ñāṇa"nti (termbase)
NCALL = f"không nên được gọi là – “{CT}”"   # na vattabbaṃ – "…"


def self_act(x, v):                 # tena X-ena taṃ X-ṃ Y-ti
    return f"bằng {x} ấy mà {v} {x} ấy"


SELF = [("sự tiếp xúc", "chạm vào"), ("cảm giác", "cảm nhận"), ("tri giác", "nhận ra"), ("chủ ý", "cố ý về"),
        ("tâm", "suy nghĩ về"), ("sự hướng tâm", "hướng tâm đến"), ("sự duy trì tâm", "duy trì tâm nơi"),
        ("sự hân hoan", "hân hoan với"), ("sự tỉnh thức", "ghi nhớ"), ("trí tuệ", "hiểu rõ"),
        ("thanh kiếm", "chặt"), ("cái rìu", "đẽo"), ("cái rìu nhỏ", "đẽo"), ("cái bào", "đẽo"), ("cây kim", "khâu"),
        ("đầu ngón tay", "sờ"), ("đầu mũi", "sờ"), ("đỉnh đầu", "sờ"), ("phân", "rửa"), ("nước tiểu", "rửa"),
        ("nước bọt", "rửa"), ("mủ", "rửa"), ("máu", "rửa")]
#   phassena phusati, vedanāya vedeti, saññāya sañjānāti, cetanāya ceteti, cittena cinteti, vitakkena vitakketi,
#   vicārena vicāreti, pītiyā piyāyati, satiyā sarati, paññāya pajānāti, khaggena chindati, pharasunā / kudhāriyā /
#   vāsiyā tacchati, sūciyā sibbeti, aṅgulaggena / nāsikaggena / matthakena parāmasati, gūthena … lohitena dhovati


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    heading("5-13-0", 3, VAGGA)

    # ---- (43) 1. Vimuttikathā -----------------------------------------------------------------------------------
    heading("5-13-1-0", 4, f"(43) 1. {S.katha(KATHA[1])}")
    l2 = [Q(T1), YES, Q(vof(GOT)), NO_PE]
    for k in ("so", "sa", "an", "ar"):
        l2 += [q(vof(P[k])), YES, Q(known(k)), NO_PE]
    add("5-418",
        f"{Q(T1)} {YES} {Q(f'bất cứ {V} nào, tất cả đều {VM}')} {NO_PE} {Q(T1)} {YES} "
        f"{Q(f'hiểu biết xem xét lại {VM}')} {NO_PE}",
        " ".join(l2))
    add("5-419", " ".join(f"{(Q if k == 'so' else q)(vof(samangi(k)))} {YES} {Q(vof(P[k]))} {NO_PE}"
                          for k in ("so", "sa", "an", "ar")))
    add("5-420", " ".join(f"{(Q if k == 'so' else q)(vof2(samangi(k)))} {YES} {Q(vof2(P[k]))} {NO_PE}"
                          for k in ("so", "sa", "an", "ar")),
        S.katha_end(KATHA[1]))

    # ---- (44) 2. Asekhañāṇakathā --------------------------------------------------------------------------------
    heading("5-13-2-0", 4, VAGGA)
    heading("5-13-2-1-0", 5, f"(44) 2. {S.katha(KATHA[2])}")
    NK = knows(SK, True)
    add("5-421",
        f"{Q(T2)} {YES} {Q(knows(SK))} {NO_PE} chẳng phải {NK} sao? {YES} {S.hanci_neg(NK, T2)}",
        f"{Q(f'{ASK} có {AK}, {knows(ASK)}')} {YES} {Q(f'{T2}, {knows(SK)}')} {NO_PE}")
    add("5-422",
        f"{Q(f'{T2}, {NK}')} {YES} {Q(f'{ASK} có {AK}, {knows(ASK, True)}')} {NO_PE}",
        f"{Q(T2)} {YES} {Q(GOT_Q)} {NO_PE} {q(SO_Q)} {NO_PE} {q(CHAIN)} {NO_PE}")
    ANP = (f"tôn giả A-nan, là {SK}, biết – «Đức Thế Tôn là bậc cao cả», biết «{SARI}, {MOGG} là bậc cao cả»")
    add("5-423",
        f"{S.na_vattabbam(T2)} {YES} {NANU(rq(ANP, 0))} {YES} {S.hanci(ANP, T2)}",
        S.katha_end(KATHA[2]))

    # ---- (45) 3. Viparītakathā ----------------------------------------------------------------------------------
    heading("5-13-3-0", 4, VAGGA)
    heading("5-13-3-1-0", 5, f"(45) 3. {S.katha(KATHA[3])}")
    VT0 = f"người đang nhập {K}{S.var_sp('Sī., Ka.', 'pathavīkasiṇasamāpattiṃ')} có hiểu biết về điều sai lệch"
    DNS = f"{VIP['d']}{PE} {VIP['n']}{PE}"
    VA_A, VA_S = f"{VIP['a']} là {SDA}", f"{DNS} {VIP['s']} là {SDA}"
    add("5-424",
        f"{Q(VT0)} {YES} {Q(VA_A)} {NO_PE} {q(VA_S)} {NO_PE}",
        f"{Q(VT)} {YES} {Q('đó là bất thiện')} {NO_PE} chẳng phải đó là thiện sao? {YES} "
        f"{S.hanci_neg('đó là thiện', VT)}",
        f"{Q(va('a', 'bất thiện'))} {YES} {Q(VTA)} {NO_PE} {q(f'{DNS} ' + va('s', 'bất thiện'))} {YES} "
        f"{Q(VTA)} {NO_PE}")
    add("5-425",
        f"{Q(VTA)} {YES} {Q(va('a', 'thiện'))} {NO_PE} {q(VTA)} {YES} {Q(f'{DNS} ' + va('s', 'thiện'))} {NO_PE}")
    ARS = f"{AR} có thể nhập {K}"                                      # arahā … samāpattiṃ samāpajjeyya
    VP3 = "sự đảo ngược của tri giác, sự đảo ngược của tâm, sự đảo ngược của quan điểm"
    #   saññāvipariyeso cittavipariyeso diṭṭhivipariyeso
    AVP = f"{AR} có {SDA}"                                             # atthi arahato vipariyeso
    NVP = f"{AR} không có {VP3}"
    add("5-426",
        f"{Q(VT)} {YES} {Q(ARS)} {YES} {S.hanci_neg(ARS, VT)}",
        f"{Q(f'{VT}, {ARS}')} {YES} {Q(AVP)} {NO_PE}",
        f"{Q(AVP)} {YES} {Q(f'{AR} có {VP3}')} {NO_PE}",
        f"{Q(NVP)} {YES} {S.hanci_neg(NVP, AVP)}")
    EARTH = "đất tồn tại, và có ai đó nhập vào đất như là đất"         # pathavī atthi, atthi ca koci pathaviṃ pathavito …
    add("5-427",
        f"{S.na_vattabbam(VT)} {YES} {Q(f'đối với người nhập {K}, tất cả đều là đất')} {NO} {S.tena_hi(VT)}",
        f"{Q(VT)} {YES} {NANU(EARTH)} {YES} {S.hanci_neg(EARTH, VT)}",
        f"{Q('đất tồn tại, đối với người nhập vào đất như là đất thì điều đó là sai lệch')} {YES} "
        f"{Q('Niết-bàn tồn tại, đối với người nhập vào Niết-bàn như là Niết-bàn thì điều đó là sai lệch')} {NO_PE} "
        f"vậy thì không nên nói – “{VT}”.",
        S.katha_end(KATHA[3]))

    # ---- (46) 4. Niyāmakathā ------------------------------------------------------------------------------------
    heading("5-13-4-0", 4, VAGGA)
    heading("5-13-4-1-0", 5, f"(46) 4. {S.katha(KATHA[4])}")
    add("5-428",
        f"{Q(T4)} {YES} {Q(has(NY, AG))} {NO_PE}",
        f"{Q(has(NY, AG, True))} {YES} {Q(has(AY, G, True))} {NO_PE}",
        f"{Q(T4)} {YES} {Q(has(NY, G))} {NO_PE}",
        f"{Q(has(NY, G, True))} {YES} {Q(has(AY, G, True))} {NO_PE}",
        f"{Q(T4)} {YES} {Q(has(AY, AG))} {NO_PE}",
        f"{Q(has(AY, AG, True))} {YES} {Q(has(AY, G, True))} {NO_PE}")
    NN = has(AY, G, True, "sự cố định")                                # aniyatassa niyāmagamanāya natthi niyāmo
    add("5-429",
        f"{Q(T4)} {YES} {Q(has(AY, G, what='sự cố định'))} {NO_PE}",
        f"{Q(T4)} {YES} {Q(f'{AY} có {PATHS6} {G}')} {NO_PE}",
        f"{Q(NN)} {YES} {S.hanci_neg(NN, T4)}",
        f"{Q(f'{AY} không có sự thiết lập tỉnh thức{PE} chi phần giác ngộ {G}')} {YES} "
        f"{S.hanci_neg(f'{AY} không có chi phần giác ngộ {G}', T4)}")
    add("5-430", f"{Q(T4)} {YES} {Q(GOT_Q)} {NO_PE} {q(SO_Q)} {NO_PE} {q(AR_Q)} {NO_PE}")
    BP = ("Đức Thế Tôn biết – «người này sẽ bước vào sự cố định theo hướng đúng đắn, người này có khả năng "
          "thấu hiểu Giáo Pháp»")
    add("5-431",
        f"{S.na_vattabbam(T4)} {YES} {NANU(rq(BP, 0))} {YES} {S.hanci(BP, T4)}",
        S.katha_end(KATHA[4]))

    # ---- (47) 5. Paṭisambhidākathā ------------------------------------------------------------------------------
    heading("5-13-5-0", 4, VAGGA)
    heading("5-13-5-1-0", 5, f"(47) 5. {S.katha(KATHA[5])}")
    PSP = "đã đạt đến hiểu biết thông suốt"                            # paṭisambhidāpattā (termbase)
    TP = f"tất cả trí tuệ là {PS}"                                     # sabbā paññā paṭisambhidā (termbase phrase)
    GIVE = ["người đang bố thí", "người đang cho y phục", "người đang cho đồ ăn khất thực", "người đang cho chỗ ở",
            f"người đang cho {GIL}"]                                   # dānaṃ / cīvaraṃ / … dadantassa
    CH432 = f"{PE} ".join(KASINA + ARUPA[:3] + [f"người đang nhập {ARUPA[3]}"] + GIVE)
    add("5-432",
        f"{Q(TS)} {YES} {Q(f'{SM} là {PS}')} {NO_PE} {q(f'{SM} là {PS}')} {YES} "
        f"{Q(f'bất cứ ai biết quy ước, tất cả những người ấy đều {PSP}')} {NO_PE} {q(TS)} {YES} "
        f"{Q(f'{CT} là {PS}')} {NO_PE} {q(f'{CT} là {PS}')} {YES} "
        f"{Q(f'bất cứ ai biết tâm của người khác, tất cả những người ấy đều {PSP}')} {NO_PE}",
        f"{Q(TS)} {YES} {Q(TP)} {NO_PE} {q(TP)} {YES} {Q(f'{SAMP} có trí tuệ, trí tuệ ấy là {PS}')} {NO_PE} "
        f"{q(f'{CH432} có trí tuệ, trí tuệ ấy là {PS}')} {NO_PE}")
    add("5-433",
        f"{S.na_vattabbam(TS)} {YES} {Q(f'có trí tuệ vượt thế gian, trí tuệ ấy không phải là {PS}')} {NO_PE} "
        f"vậy thì {TS}.",
        S.katha_end(KATHA[5]))

    # ---- (48) 6. Sammutiñāṇakathā -------------------------------------------------------------------------------
    heading("5-13-6-0", 4, VAGGA)
    heading("5-13-6-1-0", 5, f"(48) 6. {S.katha(KATHA[6])}")
    E1 = f"{SAMP} có hiểu biết, và đề mục bao trùm là đất thuộc về sự thật quy ước"
    E2 = f"người đang cho {GIL} có hiểu biết, và {GIL} thuộc về sự thật quy ước"
    add("5-434",
        f"{S.na_vattabbam(SMT)} {YES} {NANU(E1)} {YES} {S.hanci(E1, SMT)}",
        f"{S.na_vattabbam(SMT)} {YES[:-1]}{PE} chẳng phải {KASINA[0]}{PE} {KASINA[1]}{PE} {E2} sao? {YES} "
        f"{S.hanci(E2, SMT)}")
    add("5-435",
        f"{Q(SMT)} {YES} {Q(f'bằng hiểu biết ấy mà {F4}')} {NO_PE}",
        S.katha_end(KATHA[6]))

    # ---- (49) 7. Cittārammaṇakathā ------------------------------------------------------------------------------
    heading("5-13-7-0", 4, VAGGA)
    heading("5-13-7-1-0", 5, f"(49) 7. {S.katha(KATHA[7])}")
    KP1 = f"có ai đó hiểu rõ «{MINDS[0]} là {MINDS[0]}»"                # atthi koci "sarāgaṃ cittaṃ sarāgaṃ citta"nti pajānāti
    KP2 = f"có ai đó hiểu rõ «{MINDS[-1]} là {MINDS[-1]}»"
    add("5-436",
        f"{Q(CTT)} {YES} {NANU(rq(KP1, 0))} {YES} {S.hanci_neg(KP1, CTT)}",
        f"Chẳng phải có ai đó hiểu rõ {f'{PE} '.join(MINDS[1:-1])}{PE} {MINDS[-1]} là “{MINDS[-1]}” sao? {YES} "
        f"{S.hanci_neg(KP2, CTT)}")
    REST = f"{PE} ".join(ob(x) for x in LIST10[1:] + ["sự tham đắm", "sự sân hận", "sự si mê"])
    #   vedanā … paññā (LIST10), rāga, dosa, moha
    add("5-437",
        f"{Q(f'{ob(LIST10[0])} {CALL}')} {YES} {S.hanci_neg(f'{ob(LIST10[0])} nên được gọi là {CT}', CTT)} "
        f"{Q(f'{REST}{PE} {ob(AO)} {CALL}')} {YES} {S.hanci_neg(f'{ob(AO)} nên được gọi là {CT}', CTT)}",
        f"{Q(f'{ob(LIST10[0])} {NCALL}')} {YES} {Q(f'đó là hiểu biết bao quát {LIST10[0]}')} {NO_PE} "
        f"{q(f'{ob(LIST10[1])}{PE} {ob(LIST10[2])}{PE} {ob(AO)} {NCALL}')} {YES} "
        f"{Q(f'đó là hiểu biết bao quát {AO}')} {NO_PE}")
    add("5-438",
        f"{S.na_vattabbam(CTT)} {YES} {NANU(f'đó là {CT}')} {YES} {S.hanci(f'đó là {CT}', CTT)}",
        S.katha_end(KATHA[7]))

    # ---- (50) 8. Anāgatañāṇakathā -------------------------------------------------------------------------------
    heading("5-13-8-0", 4, VAGGA)
    heading("5-13-8-1-0", 5, f"(50) 8. {S.katha(KATHA[8])}")
    BY10 = ["gốc rễ", "nguyên nhân", "căn nguyên", "sự hình thành", "sự khởi nguồn", "nguồn gốc", "dưỡng chất",
            "đối tượng", "điều kiện", "sự phát sinh"]
    #   mūlato hetuto nidānato sambhavato pabhavato samuṭṭhānato āhārato ārammaṇato paccayato samudayato (termbase;
    #   pabhavato not in the termbase)
    KNOW10 = f"biết tương lai xét theo {BY10[0]}, " + ", ".join(f"biết xét theo {x}" for x in BY10[1:])
    PAC = ("biết tính chất làm điều kiện gốc rễ của tương lai, biết tính chất làm điều kiện đối tượng, "
           "biết tính chất làm điều kiện chủ đạo, biết tính chất làm điều kiện kế cận, "
           "biết tính chất làm điều kiện kế cận liền ngay")
    #   anāgataṃ hetupaccayataṃ … samanantarapaccayataṃ jānāti (termbase)
    add("5-439",
        f"{Q(AF)} {YES} {Q(KNOW10)} {NO_PE}",
        f"{Q(AF)} {YES} {Q(PAC)} {NO_PE}",
        f"{Q(AF)} {YES} {Q(GOT_Q)} {NO_PE} {Q(SO_Q)} {NO_PE}",
        f"{Q(CHAIN)} {NO_PE}")
    SUT = ("“Này A-nan, thành Ba-liên-phất sẽ gặp ba hiểm họa – hoặc từ lửa, hoặc từ nước, hoặc từ sự chia rẽ "
           "lẫn nhau” [Đại Phẩm 286; Trường Bộ Kinh 2.152; Phật Tự Thuyết 76]!")
    add("5-440",
        f"{S.na_vattabbam(AF)} {YES} {S.NANU_VUTTAM} {SUT} {S.ATTHEVA} {YES} {S.tena_hi(AF)}",
        S.katha_end(KATHA[8]))

    # ---- (51) 9. Paṭuppannakathā --------------------------------------------------------------------------------
    heading("5-13-9-0", 4, VAGGA)
    heading("5-13-9-1-0", 5, f"(51) 9. {S.katha(KATHA[9])}")
    PFX = f"hiểu biết về hiện tại{S.var_sp('Sī., Syā.', 'paccuppanne')} tồn tại"
    BY = "bằng hiểu biết ấy mà biết hiểu biết ấy"                      # tena ñāṇena taṃ ñāṇaṃ jānāti
    BYQ = f"{BY} là “hiểu biết”"                                       # … taṃ ñāṇaṃ "ñāṇa"nti jānāti
    OBJ1 = "hiểu biết ấy là đối tượng của hiểu biết ấy"               # taṃ ñāṇaṃ tassa ñāṇassa ārammaṇaṃ
    add("5-441",
        f"{Q(PFX)} {YES} {Q(BY)} {NO_PE} {q(BY)} {YES} {Q(BYQ)} {NO_PE} {q(BYQ)} {YES} {Q(OBJ1)} {NO_PE}",
        f"{Q(OBJ1)} {YES} {Q(', '.join(self_act(x, v) for x, v in SELF))} {NO_PE}")
    SAN = "khi tất cả các tạo tác được thấy là vô thường, hiểu biết ấy cũng được thấy là vô thường"
    #   sabbasaṅkhāre aniccato diṭṭhe tampi ñāṇaṃ aniccato diṭṭhaṃ hoti
    add("5-442",
        f"{S.na_vattabbam(PF)} {YES} {NANU(SAN)} {YES} {S.hanci(SAN, PF)}",
        S.katha_end(END9))

    # ---- (52) 10. Phalañāṇakathā --------------------------------------------------------------------------------
    heading("5-13-10-0", 4, VAGGA)
    heading("5-13-10-1-0", 5, f"(52) 10. {S.katha(KATHA[10])}")
    POP = ("sự biết rõ mức độ cao thấp của các thành quả, sự biết rõ mức độ cao thấp của các năng lực, "
           "sự biết rõ mức độ cao thấp của các hạng người")            # phala- / indriya- / puggalaparopariyatti
    JINA = ("là bậc chiến thắng, bậc đạo sư, bậc Tự Giác Ngộ Hoàn Toàn, bậc toàn tri, bậc thấy tất cả, "
            "bậc làm chủ Giáo Pháp, chỗ nương tựa của Giáo Pháp")
    #   jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo
    MAGGA = ("là người làm sinh khởi con đường chưa sinh khởi, người làm sinh thành con đường chưa sinh thành, "
             "người tuyên thuyết con đường chưa được tuyên thuyết, người biết con đường, người hiểu con đường, "
             "người thông thạo con đường")
    #   anuppannassa maggassa uppādetā … maggaññū maggavidū maggakovido
    add("5-443",
        f"{Q(TF)} {YES} {Q(f'{SV} đề ra sự phân định về thành quả')} {NO_PE}",
        f"{Q(TF)} {YES} {Q(f'{SV} có {POP}')} {NO_PE}",
        f"{Q(TF)} {YES} {Q(f'{SV} có {PANNATTI6}')} {NO_PE}",
        f"{Q(TF)} {YES} {Q(f'{SV} {JINA}')} {NO_PE}",
        f"{Q(TF)} {YES} {Q(f'{SV} {MAGGA}')} {NO_PE}")
    add("5-444",
        f"{S.na_vattabbam(TF)} {YES} {Q(f'{SV} là người không biết')} {NO_PE} vậy thì {TF}{PE}",
        S.katha_end(KATHA[10]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA,
        MAHAPANNASA,
        TASSAPI,
        UDD50)
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
    adh = S.FORMULAS_MD.parent / "adh-13"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
