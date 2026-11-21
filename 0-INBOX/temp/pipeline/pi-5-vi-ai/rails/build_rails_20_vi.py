"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 20, Dvādasamavaggo (^5-20-0 … ^5-653): ten kathās
(116-125) with the repeated "Dvādasamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/20-dvadasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, katha, katha_end, var, var_sp …). Strings taken from pi-1 … pi-4 rails are asserted there
(REUSED20); strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-20.md.

usage: python -I -X utf8 -B build_rails_20_vi.py          (writes the chapter and the adherence copy rails\\adh-20\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "20-dvadasamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap = S.cap
CIT = S.CIT


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
BH, bh = "Này các tỳ-khưu", "này các tỳ-khưu"                         # bhikkhave (sample)
VIP = "quả"                                                             # vipāko (ch15)
SV, AVP = "có quả trổ", "không có quả trổ"                              # savipāka / avipāka (ch15)
PH = "sự tiếp xúc"                                                      # phasso (sample)

# feelings / conjunction / attention lists (ch15, byte-identical)
VED3 = ["được cảm nhận là dễ chịu", "được cảm nhận là khó chịu",
        "được cảm nhận là không khó chịu cũng không dễ chịu"]          # sukha- / dukkha- / adukkhamasukhavedaniya
SUKHA_V, DUKKHA_V, UPEKKHA_V = ("cảm giác dễ chịu", "cảm giác khó chịu",
                                "cảm giác không khó chịu cũng không dễ chịu")
SAMP8 = [f"gắn liền với {SUKHA_V}", f"gắn liền với {DUKKHA_V}", f"gắn liền với {UPEKKHA_V}",
         "gắn liền với sự tiếp xúc", "gắn liền với cảm giác", "gắn liền với tri giác", "gắn liền với chủ ý",
         "gắn liền với tâm"]                                            # sukhāya vedanāya sampayutta … cittena sampayutta
AV7 = ["sự hướng đến", "sự chú hướng", "sự lưu ý", "sự chú tâm", "chủ ý", "sự mong ước", "sự mong cầu"]
#   āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi
POS_FULL = ", ".join(VED3 + SAMP8 + ["có đối tượng"])
POS_SH = f"{VED3[0]}, {VED3[1]}{PE} có đối tượng"                       # sukhavedaniyo dukkhavedaniyo…pe… sārammaṇo
NEG_SH = f"không {VED3[0]}, không {VED3[1]}{PE} không có đối tượng"     # na sukhavedaniyo na dukkhavedaniyo…pe… anārammaṇo
POS1 = f"{VED3[0]}{PE} có đối tượng"                                    # sukhavedaniyo…pe… sārammaṇo
NEG1 = f"không {VED3[0]}{PE} không có đối tượng"                        # na sukhavedaniyo…pe… anārammaṇo
AVF = ", ".join(AV7)
AVS = f"{AV7[0]}{PE} {AV7[-1]}"                                         # āvaṭṭanā…pe… paṇidhi

# ---------------------------------------------------------------------------------------------------------------
# Kathā 1: saṃvara (APPROVED: saṃvara «sự thu thúc», asaṃvara «sự không thu thúc», Saṃvaro kammaṃ «… là nghiệp»)
# ---------------------------------------------------------------------------------------------------------------
SAMV, ASAMV = "sự thu thúc", "sự không thu thúc"
KM = {"cakkhundriya": "nghiệp bằng mắt", "kāyindriya": "nghiệp bằng thân", "jivhindriya": "nghiệp bằng lưỡi",
      "manindriya": "nghiệp bằng ý"}                                    # cakkhu- / kāya- / jivhā- / manokammaṃ (termbase)
BOTH = f"cả {SAMV} lẫn {ASAMV} đều là nghiệp"                           # saṃvaropi asaṃvaropi kammaṃ

# Kathā 2: kamma / cetanā
ALLK = f"tất cả nghiệp đều {SV}"                                        # sabbaṃ kammaṃ savipākaṃ
ALLC = f"tất cả chủ ý đều {SV}"                                         # sabbā cetanā savipākā
ABY_V = "không xác định về mặt đạo đức thuộc quả của nghiệp"           # vipākābyākatā (termbase)
ABY_K = "không xác định về mặt đạo đức mang tính chức năng"            # kiriyābyākatā (termbase)
KA, RA, AA = "thuộc cõi dục lạc", "thuộc cõi hình sắc", "thuộc cõi không hình sắc"   # (termbase)
APA = "không nằm trong các cõi tồn tại"                                 # apariyāpanna (ch11)

# Kathās 3-4
SADDO = "âm thanh"
SAL = "sáu lĩnh vực nhận biết"                                          # saḷāyatanaṃ (termbase)
KATATTA = f"{SAL} sinh khởi do nghiệp đã được tạo"                      # saḷāyatanaṃ kammassa katattā uppannaṃ

# Kathās 5-7 (person names: pi-4)
SK7 = "người tái sinh tối đa bảy lần"                                   # sattakkhattuparamo (puggalo) (pi-4)
KOL = "người đi từ gia đình này sang gia đình khác"                     # kolaṅkolo (pi-4)
EKB = "người có một hạt giống"                                          # ekabījī (pi-4)
T5 = f"{SK7} được cố định vào trạng thái tái sinh tối đa bảy lần"       # … sattakkhattuparamatāniyato (termbase)
T6 = f"{KOL} được cố định vào trạng thái đi từ gia đình này sang gia đình khác"   # kolaṅkolatāniyato (termbase)
T7 = f"{EKB} được cố định vào trạng thái có một hạt giống"              # ekabījitāniyato (termbase)
NY = "sự cố định"                                                       # niyamo / niyāmo (termbase; ch14)
BOJ6 = ["các sự thiết lập tỉnh thức", "các nỗ lực đúng đắn", "các nền tảng thần thông", "các năng lực",
        "các sức mạnh", "các chi phần giác ngộ"]                        # satipaṭṭhānā … bojjhaṅgā (ch2)
HEIN = (f"mẹ bị tước đoạt mạng sống{PE} cha bị tước đoạt mạng sống{PE} bậc A-la-hán bị tước đoạt mạng sống{PE} "
        f"máu của Như Lai bị làm cho chảy với tâm độc ác{PE} Tăng đoàn bị chia rẽ")
#   Mātā jīvitā voropitā… pitā … arahā … duṭṭhena cittena tathāgatassa lohitaṃ uppāditaṃ… saṅgho bhinno (pi-2)
ABH = "không có khả năng thấu hiểu Giáo Pháp trong khoảng giữa"        # abhabbo antarā dhammaṃ abhisametuṃ (termbase)

# Kathās 8-10
DS = "người thành tựu về quan điểm"                                     # diṭṭhisampanno puggalo (pi-2; termbase)
T8 = f"{DS} có thể cố ý tước đoạt mạng sống của sinh vật"              # … sañcicca pāṇaṃ jīvitā voropeyya (termbase)
DG = f"đối với {DS}, cõi xấu đã được dứt bỏ"                            # diṭṭhisampannassa puggalassa pahīnā duggati
AG = "đối với bậc A-la-hán, cõi xấu đã được dứt bỏ"                     # arahato pahīnā duggati
SB = "người ở lần hiện hữu thứ bảy"                                     # sattamabhaviko puggalo (termbase)
SG = f"đối với {SB}, cõi xấu đã được dứt bỏ"                            # sattamabhavikassa puggalassa pahīnā duggati
SENSE = f"các âm thanh ở cõi khổ{PE} các mùi{PE} các vị{PE} các vật xúc chạm"   # āpāyike sadde… gandhe… rase… phoṭṭhabbe
SEX = ("hưởng thụ hành vi dâm dục với người nữ không phải loài người, với con cái thuộc loài súc sinh, "
       "với thiếu nữ loài rồng")
#   amanussitthiyā tiracchānagatitthiyā nāgakaññāya methunaṃ dhammaṃ paṭiseveyya
ANIM = ["nhận dê và cừu", "nhận gà và heo", "nhận voi, bò, ngựa đực và ngựa cái"]   # (ch12; pi-4)
BIRDS = "nhận chim đa đa, chim cút, chim công và chim trĩ"              # tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya (ch12)
BV = S.var_sp("Syā., Kaṃ., Pī.", "… kapiñjalaṃ")                        # [… kapiñjalaṃ (syā. kaṃ. pī.)] (ch12)
REALMS = ["tái sinh vào địa ngục", "tái sinh vào cõi súc sinh", "tái sinh vào cõi ngạ quỷ"]
#   nirayaṃ / tiracchānayoniṃ / pettivisayaṃ upapajjeyya (pi-2 names)

VAGGA = "Chương thứ mười hai"                                          # Dvādasamavaggo (termbase)
KATHA = {1: f"việc {SAMV} là nghiệp", 2: "nghiệp", 3: f"việc {SADDO} là {VIP}", 4: SAL, 5: SK7, 6: KOL, 7: EKB,
         8: "việc tước đoạt mạng sống", 9: "cõi xấu", 10: SB}
#   Saṃvaro kammanti-, Kamma-, Saddo vipākoti-, Saḷāyatana-, Sattakkhattuparama-, Kolaṅkola-, Ekabījī-,
#   Jīvitā voropana-, Duggati-, Sattamabhavikakathā («việc» for a -ti thesis: ch5 / ch7 / ch12 / ch14 / ch15)
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9)
ALSO = "cũng vậy với"                                                   # tatheva … (ch12 / ch14)
UDDANA = (f"{cap(SAMV)} là nghiệp, {ALSO} {ASAMV}, {ALLK}, {SADDO} là {VIP}, {SAL} là {VIP}, {T5}, {T6}, {T7}, "
          f"{T8}, {DG}, {ALSO} {SB}.")
#   Saṃvaro kammaṃ tatheva asaṃvaro, sabbakammaṃ savipākaṃ, saddo vipāko, saḷāyatanaṃ vipāko, …, tatheva
#   sattamabhavikassāti.

REUSED20 = [  # (Pāli, Vietnamese, book)
    ("cakkhunā rūpaṃ disvā nimittaggāhī hoti", "khi thấy hình sắc bằng mắt thì nắm giữ dấu hiệu tổng quát", "1"),
    ("na nimittaggāhī hoti", "không nắm giữ dấu hiệu tổng quát", "1"),
    ("Sotena saddaṃ sutvā…pe…", "khi nghe âm thanh bằng tai…", "1"),
    ("manasā dhammaṃ viññāya", "khi nhận biết đối tượng của ý bằng ý", "1"),
    ("cakkhundriye saṃvaraṃ", "sự thu thúc nơi năng lực mắt", "1"),
    ("kammassa katattā upacitattā", "đã được tạo và tích lũy", "1"),
    ("Mātā jīvitā voropitā hoti … saṅgho bhinno hoti",
     "mẹ bị tước đoạt mạng sống, cha bị tước đoạt mạng sống, bậc A-la-hán bị tước đoạt mạng sống, máu của Như Lai "
     "bị làm cho chảy với tâm độc ác, Tăng đoàn bị chia rẽ", "2"),
    ("diṭṭhisampanno puggalo", DS, "2"),
    ("pitaraṃ jīvitā voropeyya", "tước đoạt mạng sống của cha", "2"),
    ("duṭṭhena cittena tathāgatassa lohitaṃ uppādeyya", "với tâm độc ác làm cho máu của Như Lai chảy", "2"),
    ("saṅghaṃ bhindeyya", "chia rẽ Tăng đoàn", "2"),
    ("sikkhāpadesu", "các điều tu học", "2"),
    ("nirayagāmī", "dẫn đến địa ngục", "2"),
    ("tiracchānayonigāmī", "dẫn đến cõi súc sinh", "2"),
    ("pettivisayagāmī", "dẫn đến cõi ngạ quỷ", "2"),
    ("sattakkhattuparamo", SK7, "4"),
    ("kolaṅkolo", KOL, "4"),
    ("ekabījī", EKB, "4"),
    ("ajeḷaka-", "nhận dê và cừu", "4"),
    ("kukkuṭasūkara-", "nhận gà và heo", "4"),
    ("hatthigavāssavaḷava-", "nhận voi, bò, ngựa đực và ngựa cái", "4"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("[… (a. ni. N)] variant label", "[dị bản (Tăng Chi Bộ Kinh 3.47): ", "1-puggalakatha.md"),
] + [("satipaṭṭhānā … bojjhaṅgā", x, "2-parihanikatha.md") for x in BOJ6] + [
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("methunaṃ dhammaṃ paṭiseveyya (optative)", "có thể hưởng thụ hành vi dâm dục", "10-dutiyavaggo.md"),
    ("na ca arahā … paṭiseveyya", "nhưng bậc A-la-hán không thể hưởng thụ", "10-dutiyavaggo.md"),
    ("satthari / sikkhāya", "về Bậc Đạo Sư", "10-dutiyavaggo.md"),
    ("sikkhāya", "về sự tu học", "10-dutiyavaggo.md"),
    ("udā. (citation)", "Kinh Phật Tự Thuyết", "10-dutiyavaggo.md"),
    ("apariyāpannaṃ", APA, "11-tatiyavaggo.md"),
    ("rūpāvacaraṃ / arūpāvacaraṃ", f"{RA} rồi trở thành {AA}", "11-tatiyavaggo.md"),
    ("nirayaṃ upapannā", "đã tái sinh vào cõi khổ", "11-tatiyavaggo.md"),
    ("ajeḷakaṃ … tittiravaṭṭakamorakapiñjaraṃ [… kapiñjalaṃ (syā. kaṃ. pī.)] paṭiggaṇheyya",
     f"{', '.join(ANIM)}, {BIRDS}{BV}", "12-catutthavaggo.md"),
    ("ye keci …, sabbe te …", "tất cả những người ấy đều", "13-pancamavaggo.md"),
    ("sotāpattiniyāmo", f"{NY} vào dòng", "14-chatthavaggo.md"),
    ("sakadāgāmi- / anāgāmi- / arahattaniyāmo", f"{NY} trở lại một lần… {NY} không trở lại… {NY} A-la-hán",
     "14-chatthavaggo.md"),
    ("tatheva …", ALSO, "14-chatthavaggo.md"),
    ("sukha- … sārammaṇa (full list)", POS_FULL, "15-sattamavaggo.md"),
    ("āvaṭṭanā ābhogo … paṇidhi", AVF, "15-sattamavaggo.md"),
    ("sukhavedaniyo dukkhavedaniyo…pe… sārammaṇo", POS_SH, "15-sattamavaggo.md"),
    ("na sukhavedaniyo na dukkhavedaniyo…pe… anārammaṇo", NEG_SH, "15-sattamavaggo.md"),
    ("āvaṭṭanā…pe… paṇidhi", AVS, "15-sattamavaggo.md"),
    ("Phasso vipāko, phasso …", f"{PH} là {VIP}, {PH}", "15-sattamavaggo.md"),
    ("avipākaṃ", AVP, "15-sattamavaggo.md"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "15-sattamavaggo.md"),
    ("Xti-kathā", "Bàn về việc ", "15-sattamavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED20 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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
def sv(ind, neg):                   # (cakkhu-)indriya(a)saṃvaro
    return f"{ASAMV if neg else SAMV} {S.I[ind]}"


def svk(ind, neg):                  # X-indriya(a)saṃvaro X-kammaṃ
    return f"{sv(ind, neg)} là {KM[ind]}"


def cet(kind, quals=""):            # (Kāmāvacarā …) vipākābyākatā / kiriyābyākatā cetanā
    return f"chủ ý {quals + ', ' if quals else ''}{kind}"


def isvip(x):                       # X vipāko
    return f"{x} là {VIP}"


def pos(x, lst, sep=","):           # X vipāko, X sukhavedaniyo…pe… sārammaṇo, atthi tassa āvaṭṭanā…pe… paṇidhi
    return f"{isvip(x)}, {x} {lst}{sep} nó có {AVS}"


def neg(x, lst, sep=","):           # X vipāko, X na sukhavedaniyo…pe… anārammaṇo, natthi tassa āvaṭṭanā…pe… paṇidhi
    return f"{isvip(x)}, {x} {lst}{sep} nó không có {AVS}"


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

    heading("5-20-0", 3, VAGGA)

    # ---- (116) 1. Saṃvaro kammantikathā ------------------------------------------------------------------------
    heading("5-20-1-0", 4, f"(116) 1. {S.katha(KATHA[1])}")
    for i, ng in (("5-630", False), ("5-631", True)):
        def s(k):
            return sv(k, ng)

        def sk(k):
            return svk(k, ng)
        thesis = f"{ASAMV if ng else SAMV} là nghiệp"
        add(i,
            f"{Q(thesis)} {YES} {Q(sk('cakkhundriya'))} {NO_PE} có phải {s('sotindriya')}{PE} {s('ghānindriya')}{PE} "
            f"{s('jivhindriya')}{PE} {sk('kāyindriya')} không? {NO_PE}",
            f"{Q(sk('kāyindriya'))} {YES} {Q(sk('cakkhundriya'))} {NO_PE} {q(sk('kāyindriya'))} {YES} "
            f"Có phải {s('sotindriya')}{PE} {s('ghānindriya')}{PE} {sk('jivhindriya')} không? {NO_PE} "
            f"{q(sk('manindriya'))} {NO_PE}",
            f"{Q(sk('manindriya'))} {YES} {Q(sk('cakkhundriya'))} {NO_PE} {q(sk('manindriya'))} {YES} "
            f"Có phải {s('sotindriya')}{PE} {s('ghānindriya')}{PE} {s('jivhindriya')}{PE} {sk('kāyindriya')} không? "
            f"{NO_PE}")
    NIM, NNIM = "nắm giữ dấu hiệu tổng quát", "không nắm giữ dấu hiệu tổng quát"   # (na) nimittaggāhī hoti (pi-1)
    add("5-632",
        f"{S.na_vattabbam(BOTH)} {YES} {S.NANU_VUTTAM} “Ở đây, {bh}, vị tỳ-khưu khi thấy hình sắc bằng mắt thì {NIM}"
        f"{PE} {NNIM}, khi nghe âm thanh bằng tai{PE} khi nhận biết đối tượng của ý bằng ý thì {NIM}{PE} {NNIM}”! "
        f"{S.ATTHEVA} {YES} {S.tena_hi(BOTH)}",
        S.katha_end(KATHA[1]))

    # ---- (117) 2. Kammakathā ------------------------------------------------------------------------------------
    heading("5-20-2-0", 4, VAGGA)
    heading("5-20-2-1-0", 5, f"(117) 2. {S.katha(KATHA[2])}")
    RAA = f"{RA}, {AA}"
    RAAP = f"{RAA}, {APA}"
    KRAA = f"{KA}, {RAA}"
    KRAAP = f"{KA}, {RAAP}"

    def has(c, p=SV):               # X cetanā savipākā / avipākā
        return f"{c}, {p}"
    add("5-633",
        f"{Q(ALLK)} {YES} {Q(ALLC)} {NO_PE} {q(ALLC)} {YES} {Q(has(cet(ABY_V)))} {NO_PE} {q(ALLC)} {YES} "
        f"{Q(has(cet(ABY_K)))} {NO_PE}",
        f"{Q(ALLC)} {YES} {Q(has(cet(ABY_V, KA)))} {NO_PE} {q(ALLC)} {YES} {Q(has(cet(ABY_V, RAAP)))} {NO_PE}",
        f"{Q(ALLC)} {YES} {Q(has(cet(ABY_K, KA)))} {NO_PE} {q(ALLC)} {YES} {Q(has(cet(ABY_K, RAA)))} {NO_PE}")
    add("5-634",
        f"{Q(has(cet(ABY_V), AVP))} {YES} {S.hanci_neg(has(cet(ABY_V), AVP), ALLC)}",
        f"{Q(has(cet(ABY_K), AVP))} {YES} {S.hanci_neg(has(cet(ABY_K), AVP), ALLC)}",
        f"{Q(has(cet(ABY_V, KRAAP), AVP))} {YES} {S.hanci_neg(has(cet(ABY_V, APA), AVP), ALLC)}",
        f"{Q(has(cet(ABY_K, KRAA), AVP))} {YES} {S.hanci_neg(has(cet(ABY_K, AA), AVP), ALLC)}")
    SUT_K = (f"“{BH}, Ta không nói rằng có sự chấm dứt của các nghiệp có chủ ý đã làm, đã được tích lũy, khi chúng "
             f"chưa được cảm nhận, và điều ấy là {S.DITTHE}, hoặc trong lần tái sinh kế tiếp"
             f"{S.var(CIT['a. ni.'] + ' 10.17', 'upapajjaṃ')}, hoặc trong một lượt khác về sau” "
             f"[{CIT['a. ni.']} 10.217]!")
    #   nāhaṃ, bhikkhave, sañcetanikānaṃ kammānaṃ katānaṃ upacitānaṃ appaṭisaṃviditvā byantibhāvaṃ vadāmi, tañca kho
    #   diṭṭheva dhamme upapajje vā apare vā pariyāye
    add("5-635",
        f"{S.na_vattabbam(ALLK)} {YES} {S.NANU_VUTTAM} {SUT_K} {S.ATTHEVA} {YES} {S.tena_hi(ALLK)}",
        S.katha_end(KATHA[2]))

    # ---- (118) 3. Saddo vipākotikathā ---------------------------------------------------------------------------
    heading("5-20-3-0", 4, VAGGA)
    heading("5-20-3-1-0", 5, f"(118) 3. {S.katha(KATHA[3])}")
    T3 = isvip(SADDO)
    NEG_IF = f"nó {NEG1}, nó không có {AVS}"                            # na sukhavedaniyo…pe… anārammaṇo, natthi …
    add("5-636",
        f"{Q(T3)} {YES} Có phải nó {POS_FULL}; nó có {AVF} không? {NO_PE} {nanu_l(f'nó {NEG_SH}, nó không có {AVS}')} "
        f"{YES} {S.hanci_neg(NEG_IF, T3)}",
        f"{Q(pos(PH, POS1))} {YES} {Q(pos(SADDO, POS1))} {NO_PE}",
        f"{Q(neg(SADDO, NEG1))} {YES} {Q(neg(PH, NEG_SH))} {NO_PE}")
    SUT_S = ("“Người ấy, do nghiệp ấy đã được tạo, đã được tích lũy, đã được tăng thêm, đã được mở rộng, có giọng nói "
             "trong sạch, nói như chim ca-lăng-tần-già” [trong Trường Bộ Kinh]!")
    #   so tassa kammassa katattā upacitattā ussannattā vipulattā brahmassaro hoti karavikabhāṇī [dīghanikāye]
    add("5-637",
        f"{S.na_vattabbam(T3)} {YES} {S.NANU_VUTTAM} {SUT_S} {S.ATTHEVA} {YES} {S.tena_hi(T3)}",
        S.katha_end(KATHA[3]))

    # ---- (119) 4. Saḷāyatanakathā -------------------------------------------------------------------------------
    heading("5-20-4-0", 4, VAGGA)
    heading("5-20-4-1-0", 5, f"(119) 4. {S.katha(KATHA[4])}")
    CA, KY = S.A["cakkhāyatana"], S.A["kāyāyatana"]
    add("5-638",
        f"{Q(isvip(CA))} {YES} Có phải nó {POS_SH}, nó có {AVS} không? {NO_PE} {nanu_l(NEG_IF)} {YES} "
        f"{S.hanci_neg(NEG_IF, isvip(CA))[:-1]}{PE}",
        f"{Q(pos(PH, POS1))} {YES} {Q(pos(CA, POS1))} {NO_PE}",
        f"{Q(neg(CA, NEG1))} {YES} {Q(neg(PH, NEG1))} {NO_PE}")
    add("5-639",
        f"Có phải {S.A['sotāyatana']}{PE} {S.A['ghānāyatana']}{PE} {S.A['jivhāyatana']}{PE} {isvip(KY)} không? {YES} "
        f"Có phải nó {POS1}, nó có {AVS} không? {NO_PE} {nanu_l(NEG_IF)} {YES} {S.hanci_neg(NEG_IF, isvip(KY))}",
        f"{Q(pos(PH, POS1))} {YES} {Q(pos(KY, POS1))} {NO_PE} {q(neg(KY, NEG1))} {YES} {Q(neg(PH, NEG1))} {NO_PE}")
    add("5-640",
        f"{S.na_vattabbam(isvip(SAL))} {YES} {NANU(KATATTA)} {YES} {S.hanci(KATATTA, isvip(SAL))}",
        S.katha_end(KATHA[4]))

    # ---- (120) 5. Sattakkhattuparamakathā -----------------------------------------------------------------------
    heading("5-20-5-0", 4, VAGGA)
    heading("5-20-5-1-0", 5, f"(120) 5. {S.katha(KATHA[5])}")
    add("5-641",
        f"{Q(T5)} {YES} {Q(HEIN)} {NO_PE}",
        f"{Q(T5)} {YES} {Q(ABH)} {NO_PE} {Q(ABH)} {YES} {Q(HEIN)} {NO_PE}")   # "…pe…. Abhabbo": sentence break
    NIY_TAIL = f"nhờ {NY} mà {T5}"                                     # yena niyamena …
    BOJ_TAIL = f"nhờ {BOJ6[-1]} mà {T5}"                               # yehi bojjhaṅgehi …
    NIY = f"có {NY} ấy, {NIY_TAIL}"                                     # atthi so niyamo yena niyamena …
    BOJ = f"có {f'{PE} '.join(BOJ6)} ấy, {BOJ_TAIL}"                    # atthi te satipaṭṭhānā…pe… bojjhaṅgā yehi …
    add("5-642", f"{Q(T5)} {YES} {Q(NIY)} {NO_PE} {q(BOJ)} {NO_PE}")
    NNIY = f"không {NIY}"
    NBOJ = f"không có {BOJ6[0]}{PE} {BOJ6[-1]} ấy, {BOJ_TAIL}"         # natthi te satipaṭṭhānā… bojjhaṅgā yehi …
    NBOJ1 = f"không có {BOJ6[-1]} ấy, {BOJ_TAIL}"                       # natthi te bojjhaṅgā yehi …
    add("5-643",
        f"{Q(NNIY)} {YES} {S.hanci_neg(NNIY, T5)}",
        f"{Q(NBOJ)} {YES} {S.hanci_neg(NBOJ1, T5)}")
    add("5-644",
        f"{Q(T5)} {YES} {Q(f'nhờ {NY} trở lại một lần')} {NO_PE} {q(f'nhờ {NY} không trở lại')} {NO_PE} "
        f"{q(f'nhờ {NY} A-la-hán')} {NO_PE}",
        f"Nhờ {NY} nào? Nhờ {NY} vào dòng. {Q(T5)} {YES} Có phải bất cứ ai bước vào {NY} vào dòng, tất cả những người "
        f"ấy đều được cố định vào trạng thái tái sinh tối đa bảy lần không? {NO_PE}")
    add("5-645",
        f"{S.na_vattabbam(T5)} {YES} {NANU(f'người ấy là {SK7}')} {YES} {S.hanci(f'người ấy là {SK7}', T5)}",
        S.katha_end(KATHA[5]))

    # ---- (121) 6. Kolaṅkolakathā; (122) 7. Ekabījīkathā -----------------------------------------------------------
    for n, (hid, num, name, t, i) in enumerate((("5-20-6", 121, KOL, T6, "5-646"),
                                                 ("5-20-7", 122, EKB, T7, "5-647")), 6):
        heading(f"{hid}-0", 4, VAGGA)
        heading(f"{hid}-1-0", 5, f"({num}) {n}. {S.katha(KATHA[n])}")
        add(i,
            f"{S.na_vattabbam(t)} {YES} {NANU(f'người ấy là {name}')} {YES} {S.hanci(f'người ấy là {name}', t)}",
            S.katha_end(KATHA[n]))

    # ---- (123) 8. Jīvitā voropanakathā --------------------------------------------------------------------------
    heading("5-20-8-0", 4, VAGGA)
    heading("5-20-8-1-0", 5, f"(123) 8. {S.katha(KATHA[8])}")
    KILL5 = (f"{DS} có thể cố ý tước đoạt mạng sống của mẹ{PE} tước đoạt mạng sống của cha{PE} tước đoạt mạng sống "
             f"của bậc A-la-hán{PE} với tâm độc ác làm cho máu của Như Lai chảy{PE} chia rẽ Tăng đoàn")
    AGA = f"{DS} không kính trọng Bậc Đạo Sư"                           # satthari agāravo
    SAGA = f"{DS} kính trọng Bậc Đạo Sư"                                 # satthari sagāravo
    add("5-648",
        f"{Q(T8)} {YES} {Q(KILL5)} {NO_PE}",
        f"{Q(T8)} {YES} {Q(AGA)} {NO_PE} có phải không kính trọng Giáo Pháp{PE} Tăng đoàn{PE} sự tu học không? "
        f"{NO_PE}",
        f"{NANU(SAGA)} {YES} {S.hanci_neg(SAGA, T8)} {NANU(f'{DS} kính trọng Giáo Pháp{PE} Tăng đoàn{PE} sự tu học')} "
        f"{YES} {S.hanci_neg(f'{DS} kính trọng sự tu học', T8)}")
    STUPA = "bảo tháp của Đức Phật"                                     # buddhathūpe
    SUT_D = (f"“{BH}, ví như đại dương có bản chất ổn định, không tràn qua bờ; cũng y như vậy, {bh}, điều tu học nào "
             f"Ta đã đặt ra cho các đệ tử, các đệ tử của Ta không vi phạm điều ấy, ngay cả vì mạng sống” "
             f"[Tiểu Phẩm 385; {CIT['a. ni.']} 8.20; Kinh Phật Tự Thuyết 45]!")
    #   seyyathāpi, bhikkhave, mahāsamuddo ṭhitadhammo velaṃ nātivattati; evameva kho, bhikkhave, yaṃ mayā sāvakānaṃ
    #   sikkhāpadaṃ paññattaṃ taṃ mama sāvakā jīvitahetupi nātikkamanti [cūḷava. 385; a. ni. 8.20; udā. 45]
    add("5-649",
        f"{Q(AGA)} {YES} Có phải {DS} có thể đại tiện, tiểu tiện, khạc nhổ lên {STUPA}, đi nhiễu quanh {STUPA} về phía "
        f"bên trái{S.var('Sī., Ka.', 'asabyākato')} không? {NO_PE}",
        f"{Q(T8)} {YES} {S.NANU_VUTTAM} {SUT_D} {S.ATTHEVA} {YES} {S.tena_hi_na(T8)}",
        S.katha_end(KATHA[8]))

    # ---- (124) 9. Duggatikathā ----------------------------------------------------------------------------------
    heading("5-20-9-0", 4, VAGGA)
    heading("5-20-9-1-0", 5, f"(124) 9. {S.katha(KATHA[9])}")
    RUPE = "tham đắm các hình sắc ở cõi khổ"                            # āpāyike rūpe rajjeyya (termbase)
    D_RUPE = f"{DS} có thể {RUPE}"
    ANIM3 = ", ".join(ANIM)
    add("5-650",
        f"{Q(DG)} {YES} {Q(D_RUPE)} {YES} {S.hanci_neg(D_RUPE, DG)}",
        f"{Q(DG)} {YES} Có phải {DS} có thể tham đắm {SENSE}{PE} {SEX}, {ANIM3}{PE} {BIRDS}{BV} không? {YES} "
        f"{S.hanci_neg(f'{DS} có thể {BIRDS}', DG)}")
    add("5-651",
        f"Có phải {DG}, {D_RUPE} không? {YES} Có phải {AG}, bậc A-la-hán có thể {RUPE} không? {NO_PE} "
        f"có phải {DG}, {DS} có thể tham đắm {SENSE}{PE} {BIRDS} không? {YES} "
        f"Có phải {AG}, bậc A-la-hán có thể {BIRDS} không? {NO_PE}",
        f"Có phải {AG}, nhưng bậc A-la-hán không thể {RUPE} không? {YES} "
        f"Có phải {DG}, nhưng {DS} không thể {RUPE} không? {NO_PE} "
        f"có phải {AG}, nhưng bậc A-la-hán không thể tham đắm {SENSE}{PE} {SEX}, {ANIM3}{PE} {BIRDS} không? {YES} "
        f"Có phải {DG}, nhưng {DS} không thể {BIRDS} không? {NO_PE}")
    NOTE = ("[dấu hiệu câu hỏi của người theo học thuyết khác, phù hợp với Chú giải. Tuy vậy, câu hỏi này dường như "
            "nên được hiểu là của người theo học thuyết của chúng ta, và các câu hỏi trước trong phần bàn về cõi xấu "
            "này là của người theo học thuyết khác]")
    #   [aṭṭhakathānulomaṃ paravādīpucchālakkhaṇaṃ. tathāpāyaṃ pucchā sakavādissa, purimāyo ca imissaṃ
    #   duggatikathāyaṃ paravādissāti gahetabbā viya dissanti]
    add("5-652",
        f"{NOTE} {S.na_vattabbam(DG)} {YES} Có phải {DS} có thể {f'{PE} '.join(REALMS)} không? {NO} "
        f"{S.tena_hi(DG)}",
        S.katha_end(KATHA[9]))

    # ---- (125) 10. Sattamabhavikakathā --------------------------------------------------------------------------
    heading("5-20-10-0", 4, VAGGA)
    heading("5-20-10-1-0", 5, f"(125) 10. {S.katha(KATHA[10])}")
    add("5-653",
        f"Có phải không nên nói “{SG}” không? {YES} Có phải {SB} có thể {', '.join(REALMS)} không? {NO} "
        f"{S.tena_hi(SG)}",                                              # Na vattabbaṃ "…"ti? (no dash in the Pāli)
        S.katha_end(KATHA[10]),
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
    adh = S.FORMULAS_MD.parent / "adh-20"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
