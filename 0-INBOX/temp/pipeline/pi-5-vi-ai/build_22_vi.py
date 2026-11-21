# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 22: 22-cuddasamavaggo.md (Cuddasamavaggo, ^5-22-0 … ^5-710),
the nine kathā (136)-(144) of the fourteenth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_2 / build_4 / build_9 / build_11 / build_12 / build_14 / build_15 / build_17 / build_19 (read-only;
importing writes nothing) for strings shared with those chapters, so every repeat is byte-identical. Every string
claimed from the pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a finished pi-5
chapter is asserted to occur in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC,
foreign letters) are run against the Pāli. Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_22_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (kilesa words, anusaya list, kāmarāga list, Hañci … no ca vata)
import build_4_vi as C4      # noqa: E402  (anāsava … asaṃkilesiya, kāmesu vītarāgo)
import build_9_vi as C9      # noqa: E402  (Tassuddānaṃ –)
import build_11_vi as C11    # noqa: E402  (sāsava … saṃkilesiya, maggo phalaṃ nibbānaṃ … bojjhaṅgo)
import build_12_vi as C12    # noqa: E402  (upapattesiyaṃ cittaṃ)
import build_14_vi as C14    # noqa: E402  (cakkhuñca paṭicca rūpe ca … / attheva suttanto frames)
import build_15_vi as C15    # noqa: E402  (hanci_no / hanci_yes / nanu_l, sahagata … ekārammaṇa)
import build_17_vi as C17    # noqa: E402  (āvaṭṭanā…pe… paṇidhi, āvaṭṭenta … paṇidahanta)
import build_19_vi as C19    # noqa: E402  (anusaya / pariyuṭṭhāna words, rūpaṃ nibbānaṃ …, sānusayo / sarāgo)

NAME = "22-cuddasamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA, ATTHEVA, NANU_VUTTAM = (B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA, B.ATTHEVA,
                                                   B.NANU_VUTTAM)
VAR, SPELL = B.VAR, B.SPELL
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA14 = B.VAGGA[14]                                     # Cuddasamavaggo = «Chương thứ mười bốn» (terms file)
hanci_no, hanci_yes, nanu_l = C15.hanci_no, C15.hanci_yes, C15.nanu_l
NATTHI = "Không có."                                      # Natthi. (answer, ch11 / ch12 / ch14)
ATTHEVA_IN = C14.ATTHEVA_IN                               # attheva suttanto (inside a sentence, ch10 / ch14)
ATTHEVA_LC = B.ATTHEVA[0].lower() + B.ATTHEVA[1:]         # "…" – attheva suttantoti? (ch14)
AY = B.AYATANA                                            # lĩnh vực mắt … (pi-2)
AB = C19.AB                                               # abyākata «không xác định về mặt đạo đức» (core)
AKU = C19.AKU                                             # akusala (predicate) «là bất thiện» (ch13, ch19)
KUSP = "là thiện"                                         # kusala (predicate, ch16 «X là thiện»)
CV = C19.CV                                               # cittavippayutta «không gắn liền với tâm» (pi-1)

# ================================================================ kathā names (headings and closing lines)
KX = {1: "sự nối kết giữa thiện và bất thiện",            # Kusalākusalapaṭisandahanakathā (terms file)
      2: "sự sinh khởi của sáu lĩnh vực nhận biết",       # Saḷāyatanuppattikathā (saḷāyatana ch16)
      3: "điều kiện kế cận",                              # Anantarapaccayakathā (ch13 anantarapaccayatā)
      4: "vật chất cao quý",                              # Ariyarūpakathā (ariya «cao quý» ch11)
      5: "việc cho rằng khuynh hướng tiềm ẩn là khác",    # Añño anusayotikathā (sample «X là khác»)
      6: "việc cho rằng sự ám ảnh không gắn liền với tâm",   # Pariyuṭṭhānaṃ cittavippayuttantikathā
      7: "những gì thuộc về",                             # Pariyāpannakathā (pariyāpanna «thuộc về» ch10;
      #                                                     «những gì …» ch12 / ch15 adjective kathā names)
      8: "những gì không xác định về mặt đạo đức",        # Abyākatakathā (core)
      9: "những gì không nằm trong các cõi tồn tại"}      # Apariyāpannakathā (pi-1 apariyāpanna)


def heads(n):
    """#### Cuddasamavaggo ^5-22-n-0 / ##### (135+n) n. <title> ^5-22-n-1-0"""
    return [(4, VAGGA14, f"5-22-{n}-0"), (5, f"({135 + n}) {n}. {K(x=KX[n])}", f"5-22-{n}-1-0")]


def nvq_c(cond, x, low=False, close=True):
    """P, na vattabbaṃ – "X"ti?  (sample ^5 ch1 «Có phải P, không nên nói – “X” không?»)"""
    return f"{'c' if low else 'C'}ó phải {cond}, không nên nói – “{x}{'”' if close else ''} không?"


# ================================================================ (136) Kusalākusalapaṭisandahana
AKM, KM = "gốc rễ bất thiện", "gốc rễ thiện"              # akusalamūla / kusalamūla (pi-2 «ba gốc rễ bất thiện»)
PS = "nối kết với"                                        # paṭisandahati (terms file heading «sự nối kết»)
T1 = f"{AKM} {PS} {KM}"                                   # akusalamūlaṃ paṭisandahati kusalamūlaṃ
T1B = f"{KM} {PS} {AKM}"                                  # kusalamūlaṃ paṭisandahati akusalamūlaṃ
KU, AKU_N = "điều thiện", "điều bất thiện"                # kusalaṃ / akusalaṃ (subject)
AVP = C17.AVP                                             # āvaṭṭanā…pe… paṇidhi «sự hướng đến… sự mong cầu» (ch17)
NAV, NPA, YAV, YPA = C17.NAV, C17.NPA, C17.YAV, C17.YPA   # anāvaṭṭenta / appaṇidahanta / āvaṭṭenta / paṇidahanta
V686 = f" [{SPELL} (Sī., Pī., Ka.): anāvaṭṭantassa; {VAR} (Syā., Kaṃ.): anāvajjantassa]"
# [anāvaṭṭantassa (sī. pī. ka.), anāvajjantassa (syā. kaṃ.)] (labels as ch15 ^5-483; ch17 has dị bản for the first)
YO, AYO = "chú tâm đúng cách", "chú tâm không đúng cách"  # yoniso / ayoniso manasikaroto
# (pi-4 ^4-150 yoniso manasikaroto «chú tâm đúng cách»; the pair kept parallel: pi-2 ^2-936 has the noun
#  ayoniso manasikāro «sự chú tâm không khôn ngoan», reported in notes-22)


def ya(a, b):
    """yā A-ssa uppādāya āvaṭṭanā…pe… paṇidhi, sāva B-ssa uppādāya āvaṭṭanā…pe… paṇidhi"""
    return f"{AVP} nào để {a} sinh khởi, chính điều ấy là {AVP} để {b} sinh khởi"


def arise(x, neg, var=""):
    """X (an)āvaṭṭentassa uppajjati…pe… (ap)paṇidahantassa uppajjati"""
    a, p = (NAV, NPA) if neg else (YAV, YPA)
    return f"{x} sinh khởi nơi người {a}{var}… sinh khởi nơi người {p}"


def mano(x, good):
    """X (a)yoniso manasikaroto uppajjati"""
    return f"{x} sinh khởi nơi người {YO if good else AYO}"


KSAN, BSAN, VSAN = "tri giác về dục lạc", "tri giác về ác ý", "tri giác về sự hãm hại"   # (pi-2 ^2 akusalasaññā)
NSAN, ASAN, AVSAN = "tri giác về sự từ bỏ", "tri giác về sự không ác ý", "tri giác về sự không hãm hại"
# nekkhamma- / abyāpāda- / avihiṃsāsaññā (pi-2 nekkhammadhātu «yếu tố từ bỏ», abyāpāda «sự không ác ý»,
# avihiṃsādhātu «yếu tố không hãm hại»)
BYA, VIH, ARATI, PAT = "ác ý", "sự hãm hại", "sự không hoan hỷ", "sự ác cảm"
# byāpādo (ch2, pi-1) vihiṃsā (pi-2) arati (pi-2 ^2-856) paṭighaṃ (ch19)
METTA, KARUNA, MUDITA, UPEKKHA = "lòng từ ái", "lòng trắc ẩn", "niềm vui đồng cảm", "sự bình thản"
# mettā (pi-2) karuṇā (pi-1 karuṇāsahagata) muditā (pi-1) upekkhā (core)


def after(y, x):
    """X-assa anantarā Y uppajjati (anantarā «ngay sau»; samanantarā «liền sau» pi-2)"""
    return f"{y} sinh khởi ngay sau {x}"


GOOD_AFTER_BAD = ", ".join([after(NSAN, KSAN), after(ASAN, BSAN), after(AVSAN, VSAN), after(METTA, BYA),
                            after(KARUNA, VIH), after(MUDITA, ARATI), after(UPEKKHA, PAT)])
BAD_AFTER_GOOD = ", ".join([after(KSAN, NSAN), after(BSAN, ASAN), after(VSAN, AVSAN), after(BYA, METTA),
                            after(VIH, KARUNA), after(ARATI, MUDITA), after(PAT, UPEKKHA)])
RV = ("tham đắm nơi chính sự vật nào, thì lìa tham đắm nơi chính sự vật ấy, lìa tham đắm nơi chính sự vật nào, "
      "thì tham đắm nơi chính sự vật ấy")
# yasmiṃyeva vatthusmiṃ rajjati tasmiññeva vatthusmiṃ virajjati, … (rajjati ch11 «tham đắm»; vīta- «đã lìa» ch2)


def unit_av(t, a, b, x, var=""):
    """the two lines Xti? Āmantā. Yā …? Na hevaṃ…pe…. / X, na vattabbaṃ – "yā …"ti? Āmantā. … no ca vata re …"""
    return (f"{Q(t)} {AM} {Q(ya(a, b))} {NHP}",
            f"{nvq_c(t, ya(a, b))} {AM} {Q(arise(x, True, var))} {NHP} {nanu_l(arise(x, False))} {AM} "
            f"{hanci_no(arise(x, False), t)}")


def unit_yo(t, own, good_own, x):
    """Xti? Āmantā. OWN (a)yoniso …ti? Āmantā. Y (a)yoniso …ti? Na hevaṃ…pe… nanu Y (a)yoniso …ti? … no ca vata re"""
    return (f"{Q(t)} {AM} {Q(mano(own, good_own))} {AM} {Q(mano(x, good_own))} {NHP} "
            f"{nanu_l(mano(x, not good_own))} {AM} {hanci_no(mano(x, not good_own), t)}")


# ================================================================ (137) Saḷāyatanuppatti
SAL = "sáu lĩnh vực nhận biết"                           # saḷāyatana (ch16 «gồm sáu lĩnh vực nhận biết»)
T2 = f"{SAL} hình thành trong bụng mẹ không trước không sau"
# saḷāyatanaṃ apubbaṃ acarimaṃ mātukucchismiṃ saṇṭhāti (apubbaṃ acarimaṃ pi-2 «không trước không sau»;
# saṇṭhāti «hình thành» ch15)
SAP = "đầy đủ mọi bộ phận lớn nhỏ, có các năng lực không khiếm khuyết"   # sabbaṅgapaccaṅgī ahīnindriyo (pi-2)
UPC = C12.UCIT                                            # upapattesiyaṃ cittaṃ «tâm tìm cầu sự tái sinh» (ch12)
BODY7 = ("bàn tay hình thành, bàn chân hình thành, đầu hình thành, tai hình thành, mũi hình thành, miệng hình "
         "thành, răng hình thành")
# hatthā saṇṭhanti, pādā …, sīsaṃ …, kaṇṇo …, nāsikā …, mukhaṃ …, dantā saṇṭhanti (hattha «bàn tay» sample;
# dantā «răng» pi-2)


def by_upc(x):
    """upapattesiyena cittena X"""
    return f"nhờ {UPC} mà {x}"


MK = "đối với người ở trong bụng mẹ"                      # mātukucchigatassa (mātukucchigato naro, verse)
HAIR5 = "tóc, lông, móng, răng, xương"                    # kesā lomā nakhā dantā aṭṭhī (pi-2 body list)
LATE = f"{MK}, {HAIR5} sinh khởi về sau"                  # mātukucchigatassa pacchā kesā … uppajjanti


def late(x):
    return f"{MK}, {x} sinh khởi về sau"


def gain(x):
    """mātukucchismiṃ X-paṭilābhāya kammaṃ karoti (paṭilābha «sự có được» pi-2; no subject added)"""
    return f"trong bụng mẹ làm nghiệp để có được {x}"


VERSE = [
    "“Đầu tiên có giọt phôi, từ giọt phôi có khối bọt;",
    f"Từ khối bọt sinh ra miếng thịt [{SPELL} (Syā., Kaṃ., Pī.): pesī], từ miếng thịt phát sinh [{VAR} (Sī., "
    f"Syā., Tương Ưng Bộ Kinh 1.235): nibbattatī; (Pī., Ka.): nibbattati] khối cứng;",
    "Từ khối cứng sinh ra các nhánh chi, tóc, lông và cả móng.",
    "“Và những gì mẹ của người ấy ăn, thức ăn, thức uống và món ăn;",
    "Nhờ đó người ấy duy trì sự sống ở đó, con người ở trong bụng mẹ” [Tương Ưng Bộ Kinh 1.235].",
]
# Paṭhamaṃ kalalaṃ hoti … mātukucchigato naro (yāpeti «duy trì sự sống» ch15; annaṃ / pānaṃ ch15; nibbattati
# «phát sinh» ch5; naro «con người» pi-2)

# ================================================================ (138) Anantarapaccaya
VN = {"cakkhu": "thức qua mắt", "sota": "thức qua tai", "ghana": "thức qua mũi", "jivha": "thức qua lưỡi",
      "kaya": "thức qua thân"}                            # cakkhuviññāṇa … kāyaviññāṇa (pi-2)
T3 = after(VN["sota"], VN["cakkhu"])                      # cakkhuviññāṇassa anantarā sotaviññāṇaṃ uppajjati
T3B = after(VN["kaya"], VN["jivha"])                      # jivhāviññāṇassa anantarā kāyaviññāṇaṃ uppajjati
SUTTA_EYE = C14.SUTTA_EYE                                 # cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ (pi-2)
EYE_SOTA = SUTTA_EYE.replace("thức qua mắt", "thức qua tai")   # … uppajjati sotaviññāṇaṃ
TONGUE = "tùy thuộc vào lưỡi và các vị, sinh khởi thức qua lưỡi"   # jivhañca paṭicca rase ca … (SUTTA_EYE frame)
TONGUE_KAYA = TONGUE.replace("thức qua lưỡi", "thức qua thân")
P5 = "năm loại thức"                                      # pañcaviññāṇā (pi-1, pi-2, ch18)
T_P5 = f"{P5} sinh khởi liền sau nhau"                    # pañcaviññāṇā aññamaññassa samanantarā uppajjanti (pi-2)
DANCE = ("có ai đó múa, hát, chơi nhạc, vừa thấy hình sắc, vừa nghe âm thanh, vừa ngửi mùi, vừa nếm vị, vừa chạm "
         "vật xúc chạm")
# atthi koci naccati gāyati vādeti, rūpañca passati, saddañca suṇāti … phoṭṭhabbañca phusati
# (atthi koci «có ai đó» sample; nacca gīta vādita «múa, hát, nhạc» pi-4; Xñca … Yñca «vừa … vừa» ch11)


def nim(v, obj):
    """V-viññāṇaṃ X-nimittaṃ manasikaroto uppajjati (nimitta «dấu hiệu của …» ch16)"""
    return f"{v} sinh khởi nơi người chú tâm đến dấu hiệu của {obj}"


def only(v, obj):
    """V-viññāṇaṃ X-ārammaṇaññeva na aññārammaṇaṃ (ch13)"""
    return f"{v} chỉ có {obj} làm đối tượng, không có điều khác làm đối tượng"


def same(a, b):
    """taññeva A taṃ B (ch11 «chính X ấy là Y ấy»)"""
    return f"chính {a} ấy là {b} ấy"


def sutta_tail(no, yes):
    """Q(no) Āmantā. "no"nti – attheva suttantoti? Natthi. "yes"nti – attheva suttantoti? Āmantā. Hañci "yes"nti –
    attheva suttanto, no ca vata re vattabbe – "no"nti. (ch14 third line)"""
    return (f"{Q(no)} {AM} “{cap(no)}” – {ATTHEVA_IN} không? {NATTHI} “{cap(yes)}” – {ATTHEVA_LC} {AM} "
            f"Nếu “{yes}” – {ATTHEVA_IN}, {B.NO_CA_VATA} “{no}”.")


# ================================================================ (139) Ariyarūpa
MB = "các yếu tố cơ bản"                                  # mahābhūtā (pi-1 «bốn yếu tố cơ bản»)
AR = "vật chất cao quý"                                   # ariyarūpaṃ
T4 = f"{AR} phái sinh từ {MB}"                            # ariyarūpaṃ mahābhūtānaṃ upādāya (pi-1 «phái sinh từ»)
ANAS9 = C4.POS[4:]                                        # anāsava asaṃyojaniya … asaṃkilesiya (pi-1, ch4)
SAS9 = C11.OBJ                                            # sāsava saṃyojaniya … saṃkilesiya (pi-1, ch11)
SUTTA_RUPA = ("“Này các tỳ-khưu, bất cứ vật chất nào cũng là bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu "
              "tố cơ bản” [Trung Bộ Kinh 1.347; Tăng Chi Bộ Kinh 11.15]!")
# yaṃ kiñci, bhikkhave, rūpaṃ cattāri mahābhūtāni catunnañca mahābhūtānaṃ upādāyarūpaṃ (pi-1 ^1 sabbaṃ rūpaṃ)

# ================================================================ (140) Añño anusayo
AN7 = C19.AN7                                             # kāmarāgānusayo … avijjānusayo (pi-2, ch2)
KIL7 = [C19.KR1, C19.PAT3.split(", ")[0], C19.MAN3.split(", ")[0], C19.DIT5.split(", ")[0],
        C19.VIC4.split(", ")[0], C19.BHA3.split(", ")[0], C19.AVJ]
# kāmarāgo paṭighaṃ māno diṭṭhi vicikicchā bhavarāgo avijjā (ch2, ch19)
PAR7 = [C19.KR6L[1], C19.PAT3.split(", ")[1], C19.MAN3.split(", ")[1], C19.DIT5.split(", ")[3],
        C19.VIC4.split(", ")[1], C19.BHA3.split(", ")[1], C19.AVJ7.split(", ")[4]]
# kāmarāga- … avijjāpariyuṭṭhānaṃ «sự ám ảnh của …» (ch2, ch10, ch19)
ANUS, PARI = "khuynh hướng tiềm ẩn", "sự ám ảnh"          # anusayo / pariyuṭṭhānaṃ (pi-2, ch2)
T5 = f"{ANUS} là khác, {PARI} là khác"                    # añño anusayo aññaṃ pariyuṭṭhānaṃ (sample «X là khác, Y là khác»)


def other(a, b):
    return f"{a} là khác, {b} là khác"


def anus_line(an, kil, par):
    return (f"{Q(other(an, par))} {AM} {Q(other(kil, par))} {NHP} {q(same(kil, par))} {AM} "
            f"{Q(same(an, par))} {NHP}")


SANU, SARA = C19.SANU, C19.SARA                           # "sānusayo" / "sarāgo"ti vattabbo (ch19)
PARI_Q = Q("nên gọi là “bị ám ảnh”")                      # "Pariyuṭṭhito"ti vattabboti?

# ================================================================ (141) Pariyuṭṭhānaṃ cittavippayuttaṃ
T6 = f"{PARI} {CV}"                                       # pariyuṭṭhānaṃ cittavippayuttaṃ
RN, RN2 = C19.RN, C19.RN2                                 # rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… / vipākābyākataṃ … (ch17, ch19)
CIT = ("tâm có tham đắm, tâm có sân hận, tâm có si mê… tâm bất thiện, tâm bị phiền não làm vẩn đục")
# sarāgaṃ cittaṃ sadosaṃ cittaṃ samohaṃ cittaṃ…pe… akusalaṃ cittaṃ saṃkiliṭṭhaṃ cittaṃ (ch13 «tâm có tham đắm»;
# saṃkiliṭṭha «bị phiền não làm vẩn đục» pi-1)

# ================================================================ (142) Pariyāpanna
DH = {"rupa": "hình sắc", "arupa": "không hình sắc", "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị",
      "photth": "vật xúc chạm", "kama": "dục lạc"}
# rūpadhātu / arūpadhātu / kāmadhātu = «cõi hình sắc / cõi không hình sắc / cõi dục lạc» (pi-1, pi-2);
# rūparāgo / arūparāgo = «sự tham đắm cõi hình sắc / cõi không hình sắc» (pi-1 ^1-363, pi-2 ^2-U49). The argument
# turns on dhātu (sadda- / gandha- … dhātu set beside rūpadhātu), so «cõi» throughout and the rāga names built
# on the pi-1 rūparāga pattern (reported in notes-22).
KR1 = C19.KR1                                             # kāmarāgo = «sự tham đắm dục lạc» (ch2)


def raga(k):
    return KR1 if k == "kama" else f"sự tham đắm cõi {DH[k]}"


def lat(k):
    """X-rāgo X-dhātuṃ anuseti"""
    return f"{raga(k)} tiềm ẩn trong cõi {DH[k]}"


def inc(k):
    """X-dhātupariyāpanno (pariyāpanna «thuộc về» ch10, ch17)"""
    return f"thuộc về cõi {DH[k]}"


def lp(k):
    """X-rāgo X-dhātuṃ anuseti, X-dhātupariyāpanno"""
    return f"{lat(k)}, {inc(k)}"


T7 = lp("rupa")
T7A = lp("arupa")
SAHA8 = C15.SAHA8                                         # sahagato sahajāto … ekārammaṇo (pi-2, ch15)
SAHA8_PE = "đi kèm… có cùng đối tượng"                    # sahagato…pe… ekārammaṇo
ES3 = "tìm cầu sự thành tựu thiền, tìm cầu sự tái sinh, an trú trong hạnh phúc ngay trong đời này"
# samāpattesiyo upapattesiyo diṭṭhadhammasukhavihāro (upapattesiya ch12; samāpatti «thành tựu thiền» pi-2;
# diṭṭhadhammasukhavihāra pi-1 «an trú trong hạnh phúc ngay trong đời này»)
NES3 = "không tìm cầu sự thành tựu thiền, không tìm cầu sự tái sinh, không an trú trong hạnh phúc ngay trong đời này"
NES2 = "không tìm cầu sự thành tựu thiền, không tìm cầu sự tái sinh"
EC3 = ("tâm tìm cầu sự thành tựu thiền, tâm tìm cầu sự tái sinh, tâm an trú trong hạnh phúc ngay trong đời này")
EC1 = "tâm tìm cầu sự thành tựu thiền"
POS_A = f"{ES3}, {SAHA8} với {EC3}"
NEG_A = f"{NES3}, không {SAHA8} với {EC3}"
NEG_A_PE = f"{NES3}, không {SAHA8_PE} với {EC1}"           # na samāpattesiyena cittena…pe… ekārammaṇo
NEG_H_PE = f"{NES3}… có cùng đối tượng"                    # Hañci na … na diṭṭhadhammasukhavihāro…pe… ekārammaṇo
NEG_H2_PE = f"{NES2}… có cùng đối tượng"                   # Hañci na samāpattesiyo na upapattesiyo…pe… ekārammaṇo
GRP = f"{raga('gandha')}… {raga('rasa')}… {lp('photth')}"  # gandharāgo…pe… rasarāgo…pe… phoṭṭhabbarāgo … -pariyāpanno
GRL = f"{raga('gandha')}… {raga('rasa')}… {lat('photth')}"  # … phoṭṭhabbarāgo phoṭṭhabbadhātuṃ anuseti

# ================================================================ (143) Abyākata
DG = "sự mắc kẹt trong các quan điểm"                     # diṭṭhigata (pi-1 ^1-381)
DGS = f"gắn liền với {DG}"                                # diṭṭhigatasampayutta (pi-1 ^1-399)
T8 = f"{DG} {AB}"
PH = "sự tiếp xúc"                                        # phasso (core)
APV, SPV = "không có kết quả, không có quả trổ", "có kết quả, có quả trổ"   # aphalaṃ avipākaṃ / saphalaṃ savipākaṃ (ch18)
VAJJA = "Đức Thế Tôn đã nói rằng các lỗi mà đứng đầu là quan điểm sai lầm"
# micchādiṭṭhiparamāni vajjāni vuttāni bhagavatā (vajja «lỗi» pi-2; ch10 «Đức Thế Tôn đã nói rằng …»)
VAJJA_N = ("Chẳng phải Đức Thế Tôn đã nói rằng các lỗi mà đứng đầu là quan điểm sai lầm [trong Tăng Chi Bộ Kinh] "
           "sao?")                                        # … vajjāni [aṅguttaranikāye] vuttāni bhagavatāti?
MD, SD = B.MICCHA[0], B.SAMMA[0]                          # micchādiṭṭhi / sammādiṭṭhi (pi-1, pi-2)
VACCHA, PUNNA = "Vác-cha", "Pun-na"                       # vaccha (ch12 Vacchagotta «Vác-cha-gốt-ta») / puṇṇa
SUTTA_V1 = (f"“Này {VACCHA}, {MD} {AKU} [{VAR} (Trung Bộ Kinh 2.194): akusalaṃ], {SD} {KUSP}” [{VAR} (Trung Bộ "
            f"Kinh 2.104): kusalaṃ] [Trung Bộ Kinh 2.194]!")
# micchādiṭṭhi kho, vaccha, akusalā [akusalaṃ (ma. ni. 2.194)], sammādiṭṭhi kusalā" [kusalaṃ (ma. ni. 2.104)] ti
SUTTA_P = (f"“Này {PUNNA}, đối với người có {MD}, Ta nói đến một trong hai cõi tái sinh – địa ngục hoặc cõi súc "
           "sinh” [Trung Bộ Kinh 2.79]!")
# micchādiṭṭhissa kho ahaṃ, puṇṇa, dvinnaṃ gatīnaṃ aññataraṃ gatiṃ vadāmi – nirayaṃ vā tiracchānayoniṃ vā
# (gati «cõi tái sinh» sample; niraya / tiracchānayoni pi-2, ch16; «Ta» ch10)
VIEWS = ["thế gian là trường tồn", "thế gian không trường tồn", "thế gian là hữu hạn", "thế gian là vô hạn",
         "linh hồn và thân thể là một", "linh hồn là khác, thân thể là khác", "Như Lai còn tồn tại sau khi chết",
         "Như Lai không còn tồn tại sau khi chết", "Như Lai vừa còn tồn tại vừa không còn tồn tại sau khi chết",
         "Như Lai không phải còn tồn tại cũng không phải không còn tồn tại sau khi chết"]
# sassato loko … neva hoti na na hoti tathāgato paraṃ maraṇā (pi-1 ^1-1105 wording)
VC = f"này {VACCHA}"
ABE = f"điều này {AB}"                                    # abyākatametaṃ (the debate word abyākata kept: notes-22)
SUTTA_V2 = (f"“‘{cap(VIEWS[0])}’, {VC}, {ABE}, ‘{VIEWS[1]}’, {VC}, {ABE}, ‘{VIEWS[2]}’, {VC}, {ABE}, "
            f"‘{VIEWS[3]}’, {VC}… ‘{VIEWS[4]}’, {VC}… ‘{VIEWS[5]}’, {VC}… ‘{VIEWS[6]}’, {VC}… "
            f"‘{VIEWS[7]}’, {VC}… ‘{VIEWS[8]}’, {VC}… ‘{VIEWS[9]}’, {VC}, {ABE}"
            "” [Tương Ưng Bộ Kinh 4.416, nhưng hơi khác một chút]!")
# "‘sassato loko’ti kho, vaccha, abyākatametaṃ, … abyākatameta"nti [saṃ. ni. 4.416, thokaṃ pana visadisaṃ]
# (thokaṃ pana visadisaṃ «nhưng hơi khác một chút» ch16)
SUTTA_AN = ("“Này các tỳ-khưu, đối với con người có quan điểm sai lầm, bất cứ nghiệp bằng thân nào tương xứng với "
            "quan điểm, được thực hiện trọn vẹn, được thọ trì, bất cứ nghiệp bằng lời nói nào… bất cứ nghiệp bằng ý "
            "nào, bất cứ chủ ý nào, bất cứ sự mong ước nào, bất cứ sự mong cầu nào, bất cứ những tạo tác nào, tất "
            "cả những hiện tượng ấy đều đưa đến điều không đáng mong muốn, không đáng yêu thích, không đáng ưa thích, "
            "đến điều không lợi ích, đến khổ đau” [Tăng Chi Bộ Kinh 1.306]!")
# micchādiṭṭhikassa, bhikkhave, purisapuggalassa yañceva kāyakammaṃ yathādiṭṭhisamattaṃ samādinnaṃ, yañca
# vacīkammaṃ…pe… yañca manokammaṃ, yā ca cetanā, yā ca patthanā, yo ca paṇidhi, ye ca saṅkhārā, sabbe te dhammā
# aniṭṭhāya akantāya amanāpāya ahitāya dukkhāya saṃvattanti (purisapuggala «con người» pi-2; yathādiṭṭhi «tương
# xứng» pi-1; samādinna «thọ trì» pi-2; patthanā «sự mong ước» pi-1 ^1-1065; paṇidhi «sự mong cầu» pi-1, ch11;
# iṭṭhāya kantāya manāpāya hitāya sukhāya ch15 LEAD, here negated)

# ================================================================ (144) Apariyāpanna
T9 = f"{DG} không nằm trong các cõi tồn tại"              # diṭṭhigataṃ apariyāpannaṃ (pi-1 apariyāpanna)
MPN = C11.MPN                                             # maggo phalaṃ nibbānaṃ … bojjhaṅgo (ch11)
PU = C4.PUTHUJJANA                                        # puthujjano «người phàm phu» (pi-1, ch4)
VITA = f"{PU} nên gọi là “đã lìa tham đắm đối với các dục lạc”"   # puthujjano "kāmesu vītarāgo"ti vattabbo (ch4)
VIGATA = Q("nên gọi là “có quan điểm đã mất đi”")         # "Vigatadiṭṭhiyo"ti vattabboti? (vigata «đã mất đi» ch19)

# ================================================================ vagga close (ch9 frame)
UDDANA = (f"{cap(T1)}, {T1B}, {SAL}, sáu nhóm thức, {T4}, chính {ANUS} ấy là {PARI} ấy, {T6}, tùy theo cõi mà "
          f"tiềm ẩn trong chính cõi ấy, {T8}, {T9}.")
# Akusalamūlaṃ paṭisandahati kusalamūlaṃ, kusalamūlaṃ paṭisandahati akusalamūlaṃ, saḷāyatanaṃ chaviññāṇakāyā,
# ariyarūpaṃ mahābhūtānaṃ upādāya, sveva anusayo taṃ pariyuṭṭhānaṃ, pariyuṭṭhānaṃ cittavippayuttaṃ, yathādhātu
# taññeva anuseti, diṭṭhigataṃ abyākataṃ, diṭṭhigataṃ apariyāpannanti. (uddāna = the phrases as written, ch13
# rule; comma after saḷāyatanaṃ added; kāya «nhóm» ch16)


def build():
    d = B.Doc()
    d.head(3, VAGGA14, "5-22-0")
    # ------------------------------------------------------------ (136) Kusalākusalapaṭisandahana
    d.head(4, f"(136) 1. {K(x=KX[1])}", "5-22-1-0")
    d.seg("5-686", *unit_av(T1, AKU_N, KU, KU, V686))
    d.seg("5-687",
          unit_yo(T1, AKM, False, KU),
          f"{Q(T1)} {AM} {Q(GOOD_AFTER_BAD)} {NHP}")
    d.seg("5-688", *unit_av(T1B, KU, AKU_N, AKU_N))
    d.seg("5-689",
          unit_yo(T1B, KU, True, AKU_N),
          f"{Q(T1B)} {AM} {Q(BAD_AFTER_GOOD)} {NHP}")
    d.seg("5-690",
          f"{NVQ(f'{T1}, {T1B}')} {AM} {NANU(RV)} {AM} {hanci_yes(RV, f'{T1}, {T1B}')}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (137) Saḷāyatanuppatti
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-691",
          f"{Q(T2)} {AM} {Q(f'người {SAP}, đi vào bụng mẹ')} {NHP}",
          f"{Q(by_upc(f'{AY[0]} hình thành'))} {AM} {Q(by_upc(BODY7))} {NHP}",
          f"{Q(by_upc(f'{AY[1]}… {AY[2]}… {AY[3]} hình thành'))} {AM} {Q(by_upc(BODY7))} {NHP}")
    d.seg("5-692",
          f"{Q(late(AY[0]))} {AM} {Q(gain('mắt'))} {NHP} {q(late(f'{AY[1]}… {AY[2]}… {AY[3]}'))} {AM} "
          f"{Q(gain('lưỡi'))} {NHP}",
          f"{Q(LATE)} {AM} {Q(gain('xương'))} {NHP}",
          f"{NVQ(LATE)} {AM} {NANU_VUTTAM}",
          *VERSE,
          f"{ATTHEVA} {AM} {TENA_HI(LATE)}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (138) Anantarapaccaya
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    c, s = VN["cakkhu"], VN["sota"]
    d.seg("5-693",
          f"{Q(T3)} {AM} {Q(ya(c, s))} {NHP}",
          f"{nvq_c(T3, ya(c, s), close=False)} {AM} {Q(arise(s, True))} {NHP} "
          f"Chẳng phải {arise(s, False)} sao, đúng vậy. {hanci_no(arise(s, False), T3)}")
    # ^5-693 l.2 as written: the quote "yā … paṇidhīti? is not closed; "… uppajjatīti, āmantā." (comma, lowercase)
    d.seg("5-694",
          f"{Q(T3)} {AM} {Q(nim(c, 'hình sắc'))} {AM} {Q(nim(s, 'hình sắc'))} {NHP}",
          f"{Q(only(c, 'hình sắc'))} {AM} {Q(only(s, 'hình sắc'))} {NHP}",
          f"{Q(SUTTA_EYE)} {AM} {Q(EYE_SOTA)} {NHP}",
          sutta_tail(EYE_SOTA, SUTTA_EYE),
          f"{Q(T3)} {AM} {Q(same(c, s))} {NHP}")
    j, k = VN["jivha"], VN["kaya"]
    d.seg("5-695",
          f"{Q(chain([after(VN['ghana'], s), after(j, VN['ghana']), T3B]))} {AM} {Q(ya(j, k))} {NHP} "
          f"{nvq_c(T3B, ya(j, k), low=True)} {AM} {Q(arise(k, True))} {NHP} {nanu_l(arise(k, False))} {AM} "
          f"{hanci_no(arise(k, False), T3B)}")
    d.seg("5-696",
          f"{Q(T3B)} {AM} {Q(nim(j, 'vị'))} {AM} {Q(nim(k, 'vị'))} {NHP}",
          f"{Q(only(j, 'vị'))} {AM} {Q(only(k, 'vị'))} {NHP}",
          f"{Q(TONGUE)} {AM} {Q(TONGUE_KAYA)} {NHP}",
          sutta_tail(TONGUE_KAYA, TONGUE),           # ^5-696 l.4 Hañci … attheva suttantoti, (ti as written: no word)
          f"{Q(T3B)} {AM} {Q(same(j, k))} {NHP}")
    d.seg("5-697",
          f"{NVQ(T_P5)} {AM} {NANU(DANCE)} {AM} {hanci_yes(DANCE, T_P5)}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (139) Ariyarūpa
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-698",
          f"{Q(T4)} {AM} {Q(f'{AR} {KUSP}')} {AM} {Q(f'{MB} {KUSP}')} {NHP} {q(f'{MB} {AB}')} {AM} "
          f"{Q(f'{AR} {AB}')} {NHP} {q(T4)} {AM} {Q(f'{AR} ' + ', '.join(ANAS9))} {AM} "
          f"{Q(f'{MB} {ANAS9[0]}… {ANAS9[-1]}')} {NHP} {q(f'{MB} {SAS9[0]}, {SAS9[1]}… {SAS9[-1]}')} {AM} "
          f"{Q(f'{AR} {SAS9[0]}, {SAS9[1]}… {SAS9[-1]}')} {NHP}")
    d.seg("5-699",
          f"{NVQ(T4)} {AM} {NANU_VUTTAM} {SUTTA_RUPA} {ATTHEVA} {AM} {TENA_HI(T4)}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (140) Añño anusayo
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    d.seg("5-700", *[anus_line(a, kk, p) for a, kk, p in zip(AN7, KIL7, PAR7)])
    d.seg("5-701",
          f"{NVQ(T5)} {AM} {Q(SANU)} {AM} {PARI_Q} {NH} {TENA_HI(T5)} {Q(SARA)} {AM} {PARI_Q} {NH} "
          f"{TENA_HI(other(C2.R, PARI))}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (141) Pariyuṭṭhānaṃ cittavippayuttaṃ
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    d.seg("5-702",
          f"{Q(T6)} {AM} {Q(RN)} {NHP} {q(T6)} {AM} {Q(f'không có {CIT}')} {NHP} {nanu_l(f'có {CIT}')} {AM} "
          f"{hanci_no(f'có {CIT}', T6)}",
          E(x=KX[6]))
    # ------------------------------------------------------------ (142) Pariyāpanna
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    d.seg("5-703",
          f"{Q(T7)} {AM} {Q(POS_A)} {NHP} {nanu_l(NEG_A)} {AM} Nếu {NEG_H_PE}, {B.NO_CA_VATA} “{T7}”…",
          f"{Q(T7)} {AM} {Q(lp('sadda'))} {NHP} {q(T7)} {AM} {Q(GRP)} {NHP}",
          f"{nvq_c(lat('sadda'), inc('sadda'))} {AM} {nvq_c(lat('rupa'), inc('rupa'))} {NHP} "
          f"{nvq_c(GRL, inc('photth'), low=True)} {AM} {nvq_c(lat('rupa'), inc('rupa'))} {NHP}")
    d.seg("5-704",
          f"{Q(T7A)} {AM} {Q(POS_A)} {NHP} Chẳng phải {NEG_A_PE} sao? {AM} "
          f"{hanci_no(NEG_H2_PE, T7A)}",
          f"{Q(T7A)} {AM} {Q(lp('sadda'))} {NHP} {q(T7A)} {AM} {Q(GRP)} {NHP}",
          f"{nvq_c(lat('sadda'), inc('sadda'))} {AM} Có phải {lat('arupa')}, không nên nói – “{inc('arupa')}” "
          f"không, {NHP[0].lower()}{NHP[1:]} {nvq_c(GRL, inc('photth'), low=True)} {AM} "
          f"{nvq_c(lat('arupa'), inc('arupa'))} {NHP}")
    # ^5-704 l.3 as written: "… arūpadhātupariyāpanno"ti, na hevaṃ vattabbe…pe… (comma, lowercase)
    d.seg("5-705",
          f"{NVQ(f'{T7}, {T7A}')} {AM} {NANU(lp('kama'))} {AM} {hanci_yes(lp('kama'), f'{T7}, {T7A}')}",
          E(x=KX[7]))
    # ^5-705: "anuseti rūpadhātupariyāpanno" without comma in the quote and the Hañci clause: comma rendered
    # ------------------------------------------------------------ (143) Abyākata
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    d.seg("5-706",
          f"{Q(T8)} {AM} {Q(RN2)} {NHP} {q(T8)} {AM} {Q(f'{PH} {DGS} {AB}')} {NHP} {q(T8)} {AM} "
          f"{Q(f'{B.VEDANA} {DGS}… {B.SANNA}… chủ ý… tâm {AB}')} {NHP}",
          f"{Q(f'{PH} {DGS} {AKU}')} {AM} {Q(f'{DG} {AKU}')} {NHP} "
          f"{q(f'{B.VEDANA}, {B.SANNA}, chủ ý, tâm {DGS} {AKU}')} {AM} {Q(f'{DG} {AKU}')} {NHP}")
    d.seg("5-707",
          f"{Q(T8)} {AM} {Q(APV)} {NHP} {nanu_l(SPV)} {AM} Nếu {SPV}, {B.NO_CA_VATA} “{T8}”.",
          f"{Q(T8)} {AM} {VAJJA_N} {AM} {hanci_no(VAJJA, T8)}",
          f"{Q(T8)} {AM} {NANU_VUTTAM} {SUTTA_V1} {ATTHEVA} {AM} {TENA_HI_NA(T8)}",
          f"{Q(T8)} {AM} {NANU_VUTTAM} {SUTTA_P} {ATTHEVA} {AM} {TENA_HI_NA(T8)}")
    d.seg("5-708",
          f"{NVQ(T8)} {AM} {NANU_VUTTAM} {SUTTA_V2} {ATTHEVA} {AM} {TENA_HI(T8)}",
          f"{Q(T8)} {AM} {NANU_VUTTAM} {SUTTA_AN} {ATTHEVA} {AM} {TENA_HI_NA(T8)}",
          E(x=KX[8]))
    # ------------------------------------------------------------ (144) Apariyāpanna
    for lv, t, sid in heads(9):
        d.head(lv, t, sid)
    d.seg("5-709", f"{Q(T9)} {AM} {Q(f'là {MPN}')} {NHP}")
    d.seg("5-710",
          f"{NVQ(T9)} {AM} {Q(VITA)} {AM} {VIGATA} {NH} {TENA_HI(T9)}",
          E(x=KX[9]),
          f"{VAGGA14}.",
          C9.TASSUDDANAM,
          UDDANA)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("gốc rễ bất thiện", 2), ("gốc rễ thiện", 1), ("chú tâm đúng cách", 4), ("sự chú tâm không khôn ngoan", 2),
    ("tri giác về dục lạc", 2), ("tri giác về ác ý", 2), ("tri giác về sự hãm hại", 2), ("yếu tố từ bỏ", 2),
    ("sự không ác ý", 2), ("yếu tố không hãm hại", 2), ("lòng từ ái", 2), ("lòng trắc ẩn", 1),
    ("niềm vui đồng cảm", 1), ("sự không hoan hỷ", 2), ("sự bình thản", 1), ("liền sau nhau", 2),
    ("không trước không sau", 2), (SAP, 2), ("tóc, lông, móng, răng", 2), ("xương", 2), ("sự có được", 2),
    ("thức qua tai", 2), ("thức qua mũi", 2), ("thức qua lưỡi", 2), ("thức qua thân", 2), ("tùy thuộc vào ý và các đối tượng của ý", 2),
    ("múa, hát, nhạc", 4), ("Bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản", 1),
    ("phái sinh từ bốn yếu tố cơ bản", 1), ("bị phiền não làm vẩn đục", 1), ("sự tham đắm cõi hình sắc", 1),
    ("sự tham đắm cõi không hình sắc", 2), ("cõi hình sắc", 1), ("cõi không hình sắc", 1), ("cõi dục lạc", 1),
    ("an trú trong hạnh phúc ngay trong đời này", 1), ("gắn liền với sự mắc kẹt trong các quan điểm", 1),
    ("“Thế gian là trường tồn”, hoặc “Thế gian không trường tồn”, hoặc “Thế gian là hữu hạn”, hoặc “Thế gian là "
     "vô hạn”, hoặc “Linh hồn và thân thể là một”, hoặc “Linh hồn là khác, thân thể là khác”, hoặc “Như Lai còn tồn "
     "tại sau khi chết”, hoặc “Như Lai không còn tồn tại sau khi chết”, hoặc “Như Lai vừa còn tồn tại vừa không còn "
     "tồn tại sau khi chết”, hoặc “Như Lai không phải còn tồn tại cũng không phải không còn tồn tại sau khi chết”", 1),
    ("những lỗi", 2), ("sự mong ước", 1), ("sự mong cầu", 1), ("không nằm trong các cõi tồn tại", 1),
    ("con người", 2), ("tương xứng", 1), ("thọ trì", 2), ("địa ngục", 2), ("cõi súc sinh", 2),
    ("quan điểm sai lầm", 1), ("quan điểm đúng đắn", 1), ("đáng ưa thích", 2), ("thành tựu thiền", 2),
    ("có tâm ác ý", 4), ("khuynh hướng tiềm ẩn", 2), ("người phàm phu", 1), ("Trung Bộ Kinh", 4),
    ("Tăng Chi Bộ Kinh", 4),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (C2.AN7, "2-parihanikatha.md"), ("sự ám ảnh của tham đắm dục lạc", "2-parihanikatha.md"),
    ("cùng một lúc, không trước không sau", "4-jahatikatha.md"), (", ".join(ANAS9), "4-jahatikatha.md"),
    ("đã lìa tham đắm đối với các dục lạc", "4-jahatikatha.md"), ("Tóm tắt của chương này –", "9-hevatthikatha.md"),
    (", ".join(SAS9), "11-tatiyavaggo.md"), (f"Có phải là {MPN} không?", "11-tatiyavaggo.md"),
    ("chính", "11-tatiyavaggo.md"), ("vừa chú tâm đến", "11-tatiyavaggo.md"), ("tâm có tham đắm", "13-pancamavaggo.md"),
    (UPC, "12-catutthavaggo.md"), ("chỉ có tâm làm đối tượng, không có điều khác làm đối tượng", "13-pancamavaggo.md"),
    ("tính chất làm điều kiện kế cận", "13-pancamavaggo.md"),
    (f"– {ATTHEVA_IN} không? Không có. “{cap(SUTTA_EYE)}”", "14-chatthavaggo.md"),
    (f"Nếu “{SUTTA_EYE}” – {ATTHEVA_IN}, {B.NO_CA_VATA}", "14-chatthavaggo.md"),
    (SAHA8, "15-sattamavaggo.md"), ("cho thức ăn, cho thức uống", "15-sattamavaggo.md"), ("duy trì sự sống", "15-sattamavaggo.md"),
    ("đưa đến điều đáng mong muốn, đáng yêu thích, đáng ưa thích, đến lợi ích, đến hạnh phúc", "15-sattamavaggo.md"),
    ("hình thành", "15-sattamavaggo.md"), ("không hướng đến", "15-sattamavaggo.md"),
    ("dấu hiệu của mũi", "16-atthamavaggo.md"), ("nhưng hơi khác một chút", "16-atthamavaggo.md"),
    ("sáu lĩnh vực nhận biết", "16-atthamavaggo.md"), ("cõi súc sinh", "16-atthamavaggo.md"),
    ("là thiện", "16-atthamavaggo.md"),
    (AVP, "17-navamavaggo.md"), (f"người {NAV}", "17-navamavaggo.md"), (f"người {YPA}", "17-navamavaggo.md"),
    (f"{Q(RN)} {NHP}", "17-navamavaggo.md"),
    (f"{Q(APV)} {NHP} {nanu_l(SPV)} {AM} Nếu {SPV}, {B.NO_CA_VATA}", "18-dasamavaggo.md"),
    ("không sinh khởi liền sau nhau", "18-dasamavaggo.md"), (SUTTA_EYE, "14-chatthavaggo.md"), ("người có được năm loại thức", "18-dasamavaggo.md"),
    (Q(SANU), "19-ekadasamavaggo.md"), (Q(SARA), "19-ekadasamavaggo.md"), (Q(RN2), "19-ekadasamavaggo.md"),
    (C19.PAT3, "19-ekadasamavaggo.md"), (C19.MAN3, "19-ekadasamavaggo.md"), (C19.DIT5, "19-ekadasamavaggo.md"),
    (C19.BHA3, "19-ekadasamavaggo.md"), ("khi sự không biết đã mất đi", "19-ekadasamavaggo.md"),
    ("Có phải nếu", "1-puggalakatha.md"), ("không nên nói – “", "1-puggalakatha.md"), ("có ai đó", "1-puggalakatha.md"),
    ("có kết quả, có quả trổ", "1-puggalakatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(st, f"pi-{b}") for st, b in CROSS if st not in texts[b]]
    missing += [(st, f) for st, f in PI5 if st not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for st, w in missing:
        print(f"CROSS MISSING in {w}: {st}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch22 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
