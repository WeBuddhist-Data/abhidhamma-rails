"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 22, Cuddasamavaggo (^5-22-0 … ^5-710): nine kathās
(136-144) with the repeated "Cuddasamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/22-cuddasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, vattabbo, katha, katha_end, CIT …). Strings taken from pi-1 … pi-4 rails are asserted there (REUSED22);
strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-22.md.

usage: python -I -X utf8 -B build_rails_22_vi.py          (writes the chapter and the adherence copy rails\\adh-22\\)
       python -I -X utf8 -B build_rails_22_vi.py --kw FROM TO      (keywords of the Pāli keyword map + termbase)
       python -I -X utf8 -B build_rails_22_vi.py --word REGEX      (grep the termbase headwords)
       python -I -X utf8 -B build_rails_22_vi.py --find REGEX [N]  (finished pi-5 rails chapters 1-17)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "22-cuddasamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap, RE, CIT = S.cap, S.RE, S.CIT

ROOT = S.ROOT
TB = ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
KW = ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"
FINISHED = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
            "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
            "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
            "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
            "16-atthamavaggo.md", "17-navamavaggo.md"]


def nanu(x):                          # …pe… nanu Xti? (lower case after …pe…)
    return f"chẳng phải {x} sao?"


def pna(p, x, low=False):             # P, na vattabbaṃ – "X"ti?   (ch15 frame; «mà» for a clause P)
    return f"{'có' if low else 'Có'} phải {p}, mà không nên nói – “{x}” không?"


def full(lst):
    return ", ".join(lst)


# ---------------------------------------------------------------------------------------------------------------
# Shared frames (termbase; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
AV = f"sự hướng đến{PE} sự mong cầu"                     # āvaṭṭanā…pe… paṇidhi (ch17 AV2)


def ya(x, y):                         # yā X-assa uppādāya āvaṭṭanā…pe… paṇidhi, sāva Y-assa uppādāya āvaṭṭanā…pe… paṇidhi
    return f"{AV} nào để {x} sinh khởi, thì chính {AV} ấy là để {y} sinh khởi"


VAR686 = " [khác chính tả (Sī., Pī., Ka.): anāvaṭṭantassa; dị bản (Syā., Kaṃ.): anāvajjantassa]"
#   [anāvaṭṭantassa (sī. pī. ka.), anāvajjantassa (syā. kaṃ.)]   (ch15 ^5-484 pattern)


def anav(x, var=""):                  # X anāvaṭṭentassa uppajjati…pe… appaṇidahantassa uppajjati (ch15 «nơi người»)
    return f"{x} sinh khởi nơi người không hướng đến{var}{PE} sinh khởi nơi người không mong cầu"


def av(x):                            # X āvaṭṭentassa uppajjati…pe… paṇidahantassa uppajjati
    return f"{x} sinh khởi nơi người hướng đến{PE} sinh khởi nơi người mong cầu"


def mana(x, how):                     # X (a)yoniso manasikaroto uppajjati
    return f"{x} sinh khởi nơi người chú tâm {how}"


YON, AYON = "đúng cách", "không đúng cách"                # yoniso / ayoniso (termbase; pi-2 «không khôn ngoan»)
BASES = f"đó là vật chất, Niết-bàn, {S.A['cakkhāyatana']}{PE} {S.A['phoṭṭhabbāyatana']}"   # (ch17)
CONJ = ("đi kèm, cùng sinh, hòa lẫn, gắn liền, có cùng một sự sinh khởi, có cùng một sự chấm dứt, "
        "có cùng một chỗ dựa, có cùng một đối tượng")       # sahagato … ekārammaṇo (ch15)
PUTH = "người phàm phu, khi tâm thiện hoặc không xác định về mặt đạo đức đang diễn ra"   # (ch17)
SY_N = ["không phải là đối tượng của xiềng xích", "không phải là đối tượng của nút thắt",
        "không phải là đối tượng của dòng lũ", "không phải là đối tượng của ách",
        "không phải là đối tượng của chướng ngại", "không bị sự hiểu sai lệch nắm giữ",
        "không phải là đối tượng của sự bám víu", "không phải là đối tượng của phiền não"]   # (pi-1, ch8, ch17)
ANAS = "không phải là đối tượng của ô nhiễm"            # anāsava (termbase, ch8)
SAS = "là đối tượng của ô nhiễm"                        # sāsava (pi-1, ch11)
SYJ = "là đối tượng của xiềng xích"                     # saṃyojaniya (pi-1)
SKL = "là đối tượng của phiền não"                      # saṃkilesiya (pi-1)

# ---- (136) Kusalākusalapaṭisandahana --------------------------------------------------------------------------
AKM, KM = "gốc rễ bất thiện", "gốc rễ thiện"            # akusalamūlaṃ / kusalamūlaṃ (termbase)
AK_TH = f"{AKM} nối kết với {KM}"                       # akusalamūlaṃ paṭisandahati kusalamūlaṃ («với» grammar)
KA_TH = f"{KM} nối kết với {AKM}"
AKS, KS = "điều bất thiện", "điều thiện"                # akusalaṃ / kusalaṃ (termbase «điều thiện sinh khởi»)
SANNA = [("tri giác về dục lạc", "tri giác về sự từ bỏ"), ("tri giác về ác ý", "tri giác về sự không ác ý"),
         ("tri giác về sự hãm hại", "tri giác về sự không hãm hại"), ("ác ý", "lòng từ ái"),
         ("sự hãm hại", "lòng trắc ẩn"), ("sự không hoan hỷ", "niềm vui đồng cảm"),
         ("sự ác cảm", "sự bình thản")]
#   kāma- byāpāda- vihiṃsāsaññā (pi-2) / nekkhamma- abyāpāda- avihiṃsāsaññā; byāpāda / mettā, vihiṃsā / karuṇā,
#   arati / muditā, paṭigha / upekkhā (termbase)


def after(pairs, rev=False):          # Y sinh khởi ngay sau X, … (termbase anantarā uppajjati «sinh khởi ngay sau»)
    return ", ".join(f"{a if rev else b} sinh khởi ngay sau {b if rev else a}" for a, b in pairs)


VATTHU = ("người ta tham đắm nơi chính sự vật nào thì lìa tham đắm nơi chính sự vật ấy, "
          "lìa tham đắm nơi chính sự vật nào thì tham đắm nơi chính sự vật ấy")
#   yasmiṃyeva (yasmiññeva) vatthusmiṃ rajjati tasmiññeva vatthusmiṃ virajjati, … («người ta» supplied)

# ---- (137) Saḷāyatanuppatti -------------------------------------------------------------------------------------
SAL = "sáu lĩnh vực nhận biết"                          # saḷāyatanaṃ (termbase)
WOMB = "trong bụng mẹ"                                  # mātukucchismiṃ
SAL_TH = f"không trước không sau, {SAL} hình thành {WOMB}"   # Saḷāyatanaṃ apubbaṃ acarimaṃ mātukucchismiṃ saṇṭhāti (ch3)
LIMBS = "người đầy đủ mọi bộ phận lớn nhỏ, có các năng lực không kém, nhập vào bụng mẹ"
#   sabbaṅgapaccaṅgī (pi-2) ahīnindriyo (termbase hīna «kém»; pi-2 «không khiếm khuyết») mātukucchismiṃ okkamati
UPC = "bằng tâm tìm cầu sự tái sinh mà"                # Upapattesiyena cittena (ch12)
BODY = ", ".join(f"{x} hình thành" for x in ["bàn tay", "bàn chân", "đầu", "tai", "mũi", "miệng", "răng"])
#   hatthā saṇṭhanti, pādā saṇṭhanti, sīsaṃ saṇṭhāti, kaṇṇo …, nāsikā …, mukhaṃ …, dantā saṇṭhanti
INW = "đối với người ở trong bụng mẹ, về sau"          # Mātukucchigatassa pacchā (termbase; pacchā «sau»)
HAIR = "tóc, lông, móng, răng, xương"                   # kesā lomā nakhā dantā aṭṭhī


def kamma(x):                         # Mātukucchismiṃ X-paṭilābhāya kammaṃ karoti (termbase «làm nghiệp»)
    return f"{WOMB}, người ấy làm nghiệp để có được {x}"


VERSE = [
    "“Trước tiên trở thành giọt phôi, từ giọt phôi trở thành khối bọt;",
    "Từ khối bọt sinh ra miếng thịt [khác chính tả (Syā., Kaṃ., Pī.): pesī], từ miếng thịt phát sinh "
    "[dị bản (Sī., Syā., Tương Ưng Bộ Kinh 1.235): nibbattatī; dị bản (Pī., Ka.): nibbattati] khối cứng;",
    "Từ khối cứng sinh ra các nhánh chi, tóc, lông và cả móng.",
    "“Và cái gì mà mẹ của người ấy ăn, thức ăn, thức uống và bữa ăn;",
    f"Nhờ đó, người ấy duy trì sự sống ở đó, con người ở trong bụng mẹ” [{CIT['saṃ. ni.']} 1.235].",
]
#   Paṭhamaṃ kalalaṃ hoti … mātukucchigato naro (termbase kalala, abbuda, pesi, ghana, pasākhā, yāpeti, naro)

# ---- (138) Anantarapaccaya --------------------------------------------------------------------------------------
CV = {k: S.D[k + "viññāṇadhātu"].replace("yếu tố ", "") for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya")}
#   thức qua mắt / tai / mũi / lưỡi / thân (pi-2 names without «yếu tố»; termbase)


def nxt(a, b):                        # A-assa anantarā B-ṃ uppajjati (termbase «B sinh khởi ngay sau A»)
    return f"{CV[b]} sinh khởi ngay sau {CV[a]}"


def nim(x, obj):                      # X-viññāṇaṃ Y-nimittaṃ manasikaroto uppajjati
    return f"{CV[x]} sinh khởi nơi người chú tâm đến dấu hiệu {obj}"


def only(x, obj):                     # X rūpārammaṇaññeva na aññārammaṇaṃ (ch13)
    return f"{CV[x]} chỉ có {obj} làm đối tượng, không có điều khác làm đối tượng"


def dep(organ, objs, x):              # Cakkhuñca paṭicca rūpe ca uppajjati X (ch14)
    return f"tùy thuộc vào {organ} và các {objs}, sinh khởi {CV[x]}"


def sutta_line(organ, objs, a, b):    # the ch14 "attheva suttanto" line (^5-694 / ^5-696)
    wrong, right = dep(organ, objs, b), dep(organ, objs, a)
    return (f"{Q(wrong)} {YES} “{cap(wrong)}” – {S.ATTHEVA[0].lower()}{S.ATTHEVA[1:]} Không có. "
            f"“{cap(right)}” – {S.ATTHEVA[0].lower()}{S.ATTHEVA[1:]} {YES} "
            f"{S.hanci_neg(f'«{right}» – có bài kinh như vậy thật', wrong)}")


def same(a, b):                       # Taññeva A taṃ B
    return f"chính {CV[a]} ấy là {CV[b]} ấy"


FIVE = "năm loại thức sinh khởi liền sau nhau"         # pañcaviññāṇā aññamaññassa samanantarā uppajjanti (termbase)
DANCE = ("có ai đó múa, hát, chơi nhạc, vừa thấy hình sắc, vừa nghe âm thanh, vừa ngửi mùi, vừa nếm vị, "
         "vừa chạm vật xúc chạm")
#   atthi koci naccati gāyati vādeti, rūpañca passati, saddañca suṇāti, … phoṭṭhabbañca phusati (ch11 «vừa … vừa»)

# ---- (139) Ariyarūpa ---------------------------------------------------------------------------------------------
AR = "vật chất cao quý"                                 # ariyarūpaṃ (termbase)
AR_TH = f"{AR} phái sinh từ các yếu tố cơ bản"          # ariyarūpaṃ mahābhūtānaṃ upādāya (termbase, pi-1)
MB = "các yếu tố cơ bản"                                # mahābhūtā
SUT_MB = ("Này các tỳ-khưu, bất cứ vật chất nào cũng đều là bốn yếu tố cơ bản và vật chất phái sinh từ "
          "bốn yếu tố cơ bản")
#   yaṃ kiñci, bhikkhave, rūpaṃ cattāri mahābhūtāni catunnañca mahābhūtānaṃ upādāyarūpaṃ (pi-1)

# ---- (140) Añño anusayo --------------------------------------------------------------------------------------------
ANU = [("khuynh hướng tiềm ẩn tham đắm dục lạc", "sự tham đắm dục lạc", "sự ám ảnh của tham đắm dục lạc"),
       ("khuynh hướng tiềm ẩn ác cảm", "sự ác cảm", "sự ám ảnh của ác cảm"),
       ("khuynh hướng tiềm ẩn kiêu mạn", "sự kiêu mạn", "sự ám ảnh của kiêu mạn"),
       ("khuynh hướng tiềm ẩn quan điểm", "quan điểm", "sự ám ảnh của quan điểm"),
       ("khuynh hướng tiềm ẩn hoài nghi", "sự hoài nghi", "sự ám ảnh của hoài nghi"),
       ("khuynh hướng tiềm ẩn tham đắm hiện hữu", "sự tham đắm hiện hữu", "sự ám ảnh của tham đắm hiện hữu"),
       ("khuynh hướng tiềm ẩn vô minh", "vô minh", "sự ám ảnh của vô minh")]
#   X-ānusayo (pi-2) / X (termbase) / X-pariyuṭṭhānaṃ (pi-1, termbase)


def other(a, b):                      # Añño A aññaṃ B (S.anna)
    return S.anna(a, b)


def sveva(a, b):                      # Sveva / Taññeva / Sāva A taṃ B (ch5 «chính … ấy là … ấy»)
    return f"chính {a} ấy là {b} ấy"


ANU0, PAR0, RAGA0 = "khuynh hướng tiềm ẩn", "sự ám ảnh", "sự tham đắm"   # anusayo / pariyuṭṭhānaṃ / rāgo
SANU, SARA, PARI = "có khuynh hướng tiềm ẩn", "có tham đắm", "bị ám ảnh"  # sānusayo / sarāgo (ch17) / pariyuṭṭhito

# ---- (141) Pariyuṭṭhānaṃ cittavippayuttaṃ -------------------------------------------------------------------------
PC = "sự ám ảnh không gắn liền với tâm"                 # Pariyuṭṭhānaṃ cittavippayuttaṃ (termbase)
MINDS = f"tâm có tham đắm, tâm có sân hận, tâm có si mê{PE} tâm bất thiện, tâm bị phiền não làm vẩn đục"
#   sarāgaṃ cittaṃ sadosaṃ cittaṃ samohaṃ cittaṃ…pe… akusalaṃ cittaṃ saṃkiliṭṭhaṃ cittaṃ (termbase)

# ---- (142) Pariyāpanna --------------------------------------------------------------------------------------------
RR, ARR, KR = "sự tham đắm cõi hình sắc", "sự tham đắm cõi không hình sắc", "sự tham đắm dục lạc"
#   rūparāgo / arūparāgo / kāmarāgo (termbase)
RD, ARD, KD = "cõi hình sắc", "cõi không hình sắc", "cõi dục lạc"   # rūpa- / arūpa- / kāmadhātuṃ (termbase)
SR = {"sadda": ("sự tham đắm âm thanh", "yếu tố âm thanh"), "gandha": ("sự tham đắm mùi", "yếu tố mùi"),
      "rasa": ("sự tham đắm vị", "yếu tố vị"), "phoṭṭhabba": ("sự tham đắm vật xúc chạm", "yếu tố vật xúc chạm")}
#   saddarāgo saddadhātuṃ … (termbase; dhātu as element: pi-2 names)


def lies(r, d):                       # X-rāgo X-dhātuṃ anuseti (anuseti «nằm sẵn», APPROVED)
    return f"{r} nằm sẵn trong {d}"


def incl(d):                          # X-dhātupariyāpanno (pariyāpanna «nằm trong», APPROVED)
    return f"nằm trong {d}"


def li(r, d):                         # X-rāgo X-dhātuṃ anuseti, X-dhātupariyāpanno
    return f"{lies(r, d)}, {incl(d)}"


SEEK = ["tìm cầu sự thành tựu thiền", "tìm cầu sự tái sinh", "an trú trong hạnh phúc ngay trong đời này"]
#   samāpattesiyo upapattesiyo diṭṭhadhammasukhavihāro (termbase; pi-1 «an trú trong hạnh phúc ngay trong đời này»)
MIND3 = [f"tâm {x}" for x in SEEK]                      # samāpattesiyena / upapattesiyena / … cittena (termbase)


def seek(neg=False):                  # (na) samāpattesiyo (na) upapattesiyo (na) diṭṭhadhammasukhavihāro
    return ", ".join(("không " if neg else "") + x for x in SEEK)


def withm(neg=False, short=False):    # (na) X cittena … sahagato … ekārammaṇo («mà nó» cleft; Pāli order kept)
    w = "không phải với " if neg else "với "
    if short:                         # na samāpattesiyena cittena…pe… ekārammaṇo
        return f"{w}{MIND3[0]}{PE} có cùng một đối tượng"
    return ", ".join(w + m for m in MIND3) + f" mà nó {CONJ}"


# ---- (143) Abyākata -----------------------------------------------------------------------------------------------
DG = "sự mắc kẹt trong các quan điểm"                   # diṭṭhigataṃ (termbase)
ABY = "không xác định về mặt đạo đức"                   # abyākata (core term; one word throughout, see notes)
DG_TH = f"{DG} {ABY}"                                   # Diṭṭhigataṃ abyākataṃ (termbase)
DG_AK = f"{DG} là bất thiện"                            # Diṭṭhigataṃ akusalaṃ (termbase)
DGS = f"gắn liền với {DG}"                              # diṭṭhigatasampayutto
VIPKIR = (f"đó là điều {ABY} thuộc quả của nghiệp, điều {ABY} mang tính chức năng, vật chất, Niết-bàn, "
          f"{S.A['cakkhāyatana']}{PE} {S.A['phoṭṭhabbāyatana']}")
#   Vipākābyākataṃ kiriyābyākataṃ rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ (termbase; «đó là», «điều»)
FRUIT_N, FRUIT = "nó không có kết quả, không có quả trổ", "nó có kết quả, có quả trổ"   # (a)phalaṃ (a)vipākaṃ
VAJJA = "Đức Thế Tôn đã nói đến các lỗi có quan điểm sai lầm đứng đầu"
#   micchādiṭṭhiparamāni vajjāni vuttāni bhagavatā (ch11 «đã nói đến»; termbase vajjāni «lỗi», paramāni «đứng đầu»)
VACCHA = "Vác-cha"                                      # (termbase, ch12)
PUNNA = "Pun-na"                                        # Puṇṇa (not in the termbase: reported)
VIEWS = ["Thế gian là trường tồn", "Thế gian không trường tồn", "Thế gian là hữu hạn", "Thế gian là vô hạn",
         "Linh hồn và thân thể là một", "Linh hồn là khác, thân thể là khác", "Như Lai còn tồn tại sau khi chết",
         "Như Lai không còn tồn tại sau khi chết", "Như Lai vừa còn tồn tại vừa không còn tồn tại sau khi chết",
         "Như Lai không phải còn tồn tại cũng không phải không còn tồn tại sau khi chết"]   # (pi-1 ^1-1105)
UNDECL = f"điều này {ABY}"                              # abyākatametaṃ


def views_sutta():                    # ^5-708 line 1 sutta (…pe… after the 4th to the 9th view)
    parts = []
    for k, v in enumerate(VIEWS):
        if k < 3 or k == 9:
            parts.append(f"‘{v}’, này {VACCHA}, {UNDECL}")
        else:
            parts.append(f"‘{v}’, này {VACCHA}{PE}")
    return ", ".join(parts[:4]) + " " + " ".join(parts[4:])


SUT_MICCHA = ("Này các tỳ-khưu, đối với hạng người có quan điểm sai lầm, cả nghiệp bằng thân nào được thực hiện "
              f"trọn vẹn, được thọ trì tùy theo quan điểm, và nghiệp bằng lời nói nào{PE} và nghiệp bằng ý nào, "
              "và chủ ý nào, và sự mong ước nào, và sự mong cầu nào, và các tạo tác nào, tất cả các hiện tượng ấy "
              "đều dẫn đến điều không đáng mong muốn, không đáng yêu mến, không đáng ưa thích, điều không lợi ích, "
              "khổ đau")
#   micchādiṭṭhikassa, bhikkhave, purisapuggalassa yañceva kāyakammaṃ yathādiṭṭhisamattaṃ samādinnaṃ, yañca
#   vacīkammaṃ…pe… yañca manokammaṃ, yā ca cetanā, yā ca patthanā, yo ca paṇidhi, ye ca saṅkhārā, sabbe te dhammā
#   aniṭṭhāya akantāya amanāpāya ahitāya dukkhāya saṃvattanti (termbase words)

# ---- (144) Apariyāpanna -------------------------------------------------------------------------------------------
DG_AP = f"{DG} là điều không nằm trong"                 # diṭṭhigataṃ apariyāpannaṃ («là điều» for readability)
MAGGA = ("Có phải là con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng, con đường trở lại "
         "một lần, thành quả trở lại một lần, con đường không trở lại, thành quả không trở lại, con đường A-la-hán, "
         "thành quả A-la-hán, sự thiết lập tỉnh thức, nỗ lực đúng đắn, nền tảng thần thông, năng lực, sức mạnh, "
         "chi phần giác ngộ không?")   # Maggo phalaṃ nibbānaṃ, … bojjhaṅgoti? (ch10 = ch12; ch11 «đó là»: clash)

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ mười bốn"                          # Cuddasamavaggo (termbase)
KATHA = {1: "sự nối kết giữa thiện và bất thiện", 2: f"sự sinh khởi của {SAL}", 3: "điều kiện kế cận",
         4: AR, 5: f"việc {ANU0} là khác", 6: f"việc {PC}", 7: "điều nằm trong", 8: f"điều {ABY}",
         9: "điều không nằm trong"}
#   Kusalākusalapaṭisandahana- (paṭisandahana «sự nối kết»), Saḷāyatanuppatti- (uppatti «sinh khởi»),
#   Anantarapaccaya- (termbase), Ariyarūpa- (termbase), Añño anusayoti-, Pariyuṭṭhānaṃ cittavippayuttanti-,
#   Pariyāpanna-, Abyākata-, Apariyāpannakathā («việc» for a -ti thesis, ch17)
TASSUDDANAM = "Tóm tắt của chương này –"               # Tassuddānaṃ – (ch9)
UDDANA = full([cap(AK_TH), KA_TH, SAL, "sáu nhóm thức", AR_TH, sveva(ANU0, PAR0), PC,
               "chính điều ấy nằm sẵn tùy theo cõi", DG_TH, DG_AP]) + "."
#   Akusalamūlaṃ paṭisandahati kusalamūlaṃ, kusalamūlaṃ paṭisandahati akusalamūlaṃ, saḷāyatanaṃ chaviññāṇakāyā,
#   ariyarūpaṃ mahābhūtānaṃ upādāya, sveva anusayo taṃ pariyuṭṭhānaṃ, pariyuṭṭhānaṃ cittavippayuttaṃ, yathādhātu
#   taññeva anuseti, diṭṭhigataṃ abyākataṃ, diṭṭhigataṃ apariyāpannanti.

REUSED22 = [  # (Pāli, Vietnamese, book)
    ("Kāmasaññā, byāpādasaññā, vihiṃsāsaññā", "tri giác về dục lạc, tri giác về ác ý, tri giác về sự hãm hại", "2"),
    ("sabbaṅgapaccaṅgī", "đầy đủ mọi bộ phận lớn nhỏ", "2"),
    ("cakkhuviññāṇa … kāyaviññāṇa (in the dhātu names)", "yếu tố thức qua lưỡi", "2"),
    ("diṭṭhadhammasukhavihāraṃ", "an trú trong hạnh phúc ngay trong đời này", "1"),
    ("Cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāya rūpaṃ",
     "bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản", "1"),
    ("sāsavaṃ", SAS, "1"), ("saṃyojaniyaṃ", SYJ, "1"), ("saṃkilesikaṃ", SKL, "1"),
    ("aparāmaṭṭhā", "không bị sự hiểu sai lệch nắm giữ", "1"),
    ("kiriyābyākataṃ", "không xác định về mặt đạo đức mang tính chức năng", "1"),
] + [("Sassato loko … neva hoti na na hoti tathāgato paraṃ maraṇā (one by one)", v, "1") for v in VIEWS]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Anāvaṭṭentassa [anāvaṭṭantassa (sī. pī. ka.), …] hoti", "nơi người không hướng đến [khác chính tả (Sī., Pī., Ka.): "
     "anāvaṭṭantassa; dị bản (Syā.)", "15-sattamavaggo.md"),
    ("appaṇidahantassa / paṇidahantassa hoti", "nơi người không mong cầu", "15-sattamavaggo.md"),
    ("nanu āvaṭṭentassa hoti", "nơi người hướng đến", "15-sattamavaggo.md"),
    ("āvaṭṭanā…pe… paṇidhi", "sự hướng đến… sự mong cầu", "17-navamavaggo.md"),
    ("sahagatā sahajātā saṃsaṭṭhā sampayuttā ekuppādā ekanirodhā ekavatthukā ekārammaṇā", CONJ, "15-sattamavaggo.md"),
    ("Kusalānaṃ dhammānaṃ jarāmaraṇaṃ, na vattabbaṃ – …ti?", ", không nên nói – “", "15-sattamavaggo.md"),
    ("Rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatananti?", Q(BASES), "17-navamavaggo.md"),
    ("Puthujjano kusalābyākate citte vattamāne", PUTH, "17-navamavaggo.md"),
    ("sānusayo / sarāgo (ti vattabbo)", "nên gọi là có khuynh hướng tiềm ẩn", "17-navamavaggo.md"),
    ("asaṃyojaniyaṃ … asaṃkilesiyaṃ", full(SY_N), "17-navamavaggo.md"),
    ("anāsavaṃ", ANAS, "8-satipatthanakatha.md"),
    ("sāsavaṃ saṃyojaniyaṃ", f"{SAS}, {SYJ}", "11-tatiyavaggo.md"),
    ("Cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ", dep("mắt", "hình sắc", "cakkhu"), "14-chatthavaggo.md"),
    ('"…"nti – attheva suttantoti? Natthi.', "– có bài kinh như vậy thật không? Không có.", "14-chatthavaggo.md"),
    ('Hañci "…"nti – attheva suttanto, no ca vata re', "– có bài kinh như vậy thật, thì này bạn", "14-chatthavaggo.md"),
    ("…ārammaṇaññeva na aññārammaṇaṃ", ", không có điều khác làm đối tượng", "13-pancamavaggo.md"),
    ("Maggo phalaṃ nibbānaṃ, sotāpattimaggo … bojjhaṅgoti?", MAGGA, "10-dutiyavaggo.md"),
    ("apubbaṃ acarimaṃ", "không trước không sau", "3-brahmacariyakatha.md"),
    ("Upapattesiyena cittena", "bằng tâm tìm cầu sự tái sinh", "12-catutthavaggo.md"),
    ("vaccha (vocative)", f"Này {VACCHA}", "12-catutthavaggo.md"),
    ("saṇṭhāti (of the earth)", "đất hình thành", "15-sattamavaggo.md"),
    ("…, thokaṃ pana visadisaṃ]", ", nhưng hơi khác một chút]", "16-atthamavaggo.md"),
    ("vuttāni bhagavatā (X vuttāni)", "Đức Thế Tôn đã nói đến ba loại", "11-tatiyavaggo.md"),
    ("Xñca …, Yñca …", "vừa chú tâm đến", "11-tatiyavaggo.md"),
    ("Sarāgaṃ cittaṃ", "tâm có tham đắm", "11-tatiyavaggo.md"),
    ("Taññeva X taṃ Y", "chính cái tương lai ấy là cái hiện tại ấy", "5-sabbamatthitikatha.md"),
    ("vadāmi (the Buddha)", "Ta nói", "5-sabbamatthitikatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED22 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        if i:
            lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    heading("5-22-0", 3, VAGGA)

    # ---- (136) 1. Kusalākusalapaṭisandahanakathā ---------------------------------------------------------------
    heading("5-22-1-0", 4, f"(136) 1. {S.katha(KATHA[1])}")

    def root_seg(th, bad, good, var=""):
        """^5-686 / ^5-688: the adverting argument (bad = the root's own kind, good = the other kind)."""
        l1 = f"{Q(th)} {YES} {Q(ya(bad, good))} {NO_PE}"
        l2 = (f"{pna(th, ya(bad, good))} {YES} {Q(anav(good, var))} {NO_PE} {nanu(av(good))} {YES} "
              f"{S.hanci_neg(av(good), th)}")
        return l1, l2

    add("5-686", *root_seg(AK_TH, AKS, KS, VAR686))
    add("5-687",
        f"{Q(AK_TH)} {YES} {Q(mana(AKM, AYON))} {YES} {Q(mana(KS, AYON))} {NO_PE} {nanu(mana(KS, YON))} {YES} "
        f"{S.hanci_neg(mana(KS, YON), AK_TH)}",
        f"{Q(AK_TH)} {YES} {Q(after(SANNA))} {NO_PE}")
    add("5-688", *root_seg(KA_TH, KS, AKS))
    add("5-689",
        f"{Q(KA_TH)} {YES} {Q(mana(KS, YON))} {YES} {Q(mana(AKS, YON))} {NO_PE} {nanu(mana(AKS, AYON))} {YES} "
        f"{S.hanci_neg(mana(AKS, AYON), KA_TH)}",
        f"{Q(KA_TH)} {YES} {Q(after(SANNA, rev=True))} {NO_PE}")
    BOTH = f"{AK_TH}, {KA_TH}"
    add("5-690",
        f"{S.na_vattabbam(BOTH)} {YES} {NANU(VATTHU)} {YES} {S.hanci(VATTHU, BOTH)}",
        S.katha_end(KATHA[1]))

    # ---- (137) 2. Saḷāyatanuppattikathā ---------------------------------------------------------------------------
    heading("5-22-2-0", 4, VAGGA)
    heading("5-22-2-1-0", 5, f"(137) 2. {S.katha(KATHA[2])}")
    EYE = S.A["cakkhāyatana"]
    STJ = f"{S.A['sotāyatana']}{PE} {S.A['ghānāyatana']}{PE} {S.A['jivhāyatana']}"   # sota-…pe… ghāna-…pe… jivhā-
    BODY_Q = Q(f"{UPC} {BODY}")
    add("5-691",
        f"{Q(SAL_TH)} {YES} {Q(LIMBS)} {NO_PE}",
        f"{Q(f'{UPC} {EYE} hình thành')} {YES} {BODY_Q} {NO_PE}",
        f"{Q(f'{UPC} {STJ} hình thành')} {YES} {BODY_Q} {NO_PE}")
    HAIR_TH = f"{INW} {HAIR} sinh khởi"
    add("5-692",
        f"{Q(f'{INW} {EYE} sinh khởi')} {YES} {Q(kamma('mắt'))} {NO_PE} "
        f"{q(f'{INW} {STJ} sinh khởi')} {YES} {Q(kamma('lưỡi'))} {NO_PE}",
        f"{Q(HAIR_TH)} {YES} {Q(kamma('xương'))} {NO_PE}",
        f"{S.na_vattabbam(HAIR_TH)} {YES} {S.NANU_VUTTAM}",
        *VERSE,
        f"{S.ATTHEVA} {YES} {S.tena_hi(HAIR_TH)}",
        S.katha_end(KATHA[2]))

    # ---- (138) 3. Anantarapaccayakathā ----------------------------------------------------------------------------
    heading("5-22-3-0", 4, VAGGA)
    heading("5-22-3-1-0", 5, f"(138) 3. {S.katha(KATHA[3])}")
    CS = nxt("cakkhu", "sota")
    add("5-693",
        f"{Q(CS)} {YES} {Q(ya(CV['cakkhu'], CV['sota']))} {NO_PE}",
        f"{pna(CS, ya(CV['cakkhu'], CV['sota']))} {YES} {Q(anav(CV['sota']))} {NO_PE} "
        f"{cap(nanu(av(CV['sota'])))[:-1]}, {YES[0].lower()}{YES[1:]} {S.hanci_neg(av(CV['sota']), CS)}")
    #   "…uppajjatīti, āmantā." (comma, lower case: kept as written); the unclosed quote is closed (repair)

    def five_lines(a, b, organ, objs, nimobj, obj):
        th = nxt(a, b)
        return (f"{Q(th)} {YES} {Q(nim(a, nimobj))} {YES} {Q(nim(b, nimobj))} {NO_PE}",
                f"{Q(only(a, obj))} {YES} {Q(only(b, obj))} {NO_PE}",
                f"{Q(dep(organ, objs, a))} {YES} {Q(dep(organ, objs, b))} {NO_PE}",
                sutta_line(organ, objs, a, b),
                f"{Q(th)} {YES} {Q(same(a, b))} {NO_PE}")

    add("5-694", *five_lines("cakkhu", "sota", "mắt", "hình sắc", "hình sắc", "hình sắc"))
    JK = nxt("jivhā", "kāya")
    CHAIN = f"{nxt('sota', 'ghāna')}{PE} {nxt('ghāna', 'jivhā')}{PE} {JK}"
    YJK = ya(CV["jivhā"], CV["kāya"])
    add("5-695",
        f"{Q(CHAIN)} {YES} {Q(YJK)} {NO_PE} {pna(JK, YJK, low=True)} {YES} "
        f"{Q(anav(CV['kāya']))} {NO_PE} {nanu(av(CV['kāya']))} {YES} {S.hanci_neg(av(CV['kāya']), JK)}")
    add("5-696", *five_lines("jivhā", "kāya", "lưỡi", "vị", "vị", "vị"))
    add("5-697",
        f"{S.na_vattabbam(FIVE)} {YES} {NANU(DANCE)} {YES} {S.hanci(DANCE, FIVE)}",
        S.katha_end(KATHA[3]))

    # ---- (139) 4. Ariyarūpakathā ----------------------------------------------------------------------------------
    heading("5-22-4-0", 4, VAGGA)
    heading("5-22-4-1-0", 5, f"(139) 4. {S.katha(KATHA[4])}")
    ANAS9 = full([ANAS] + SY_N)
    add("5-698",
        f"{Q(AR_TH)} {YES} {Q(f'{AR} là thiện')} {YES} {Q(f'{MB} là thiện')} {NO_PE} {q(f'{MB} {ABY}')} {YES} "
        f"{Q(f'{AR} {ABY}')} {NO_PE} {q(AR_TH)} {YES} {Q(f'{AR} {ANAS9}')} {YES} "
        f"{Q(f'{MB} {ANAS}{PE} {SY_N[-1]}')} {NO_PE} {q(f'{MB} {SAS}, {SYJ}{PE} {SKL}')} {YES} "
        f"{Q(f'{AR} {SAS}, {SYJ}{PE} {SKL}')} {NO_PE}")
    add("5-699",
        f"{S.na_vattabbam(AR_TH)} {YES} {S.NANU_VUTTAM} “{SUT_MB}” [{CIT['ma. ni.']} 1.347; {CIT['a. ni.']} 11.15]! "
        f"{S.ATTHEVA} {YES} {S.tena_hi(AR_TH)}",
        S.katha_end(KATHA[4]))

    # ---- (140) 5. Añño anusayotikathā -----------------------------------------------------------------------------
    heading("5-22-5-0", 4, VAGGA)
    heading("5-22-5-1-0", 5, f"(140) 5. {S.katha(KATHA[5])}")
    lines = []
    for anu, kil, par in ANU:
        lines.append(f"{Q(other(anu, par))} {YES} {Q(other(kil, par))} {NO_PE} {q(sveva(kil, par))} {YES} "
                     f"{Q(sveva(anu, par))} {NO_PE}")
    add("5-700", *lines)
    add("5-701",
        f"{S.na_vattabbam(other(ANU0, PAR0))} {YES} {Q(f'{PUTH}, {S.vattabbo(SANU)}')} {YES} "
        f"{Q(S.vattabbo(PARI))} {NO} {S.tena_hi(other(ANU0, PAR0))} {Q(f'{PUTH}, {S.vattabbo(SARA)}')} {YES} "
        f"{Q(S.vattabbo(PARI))} {NO} {S.tena_hi(other(RAGA0, PAR0))}",
        S.katha_end(KATHA[5]))

    # ---- (141) 6. Pariyuṭṭhānaṃ cittavippayuttantikathā ----------------------------------------------------------
    heading("5-22-6-0", 4, VAGGA)
    heading("5-22-6-1-0", 5, f"(141) 6. {S.katha(KATHA[6])}")
    add("5-702",
        f"{Q(PC)} {YES} {Q(BASES)} {NO_PE} {q(PC)} {YES} {Q(f'không có {MINDS}')} {NO_PE} "
        f"{nanu(f'có {MINDS}')} {YES} {S.hanci_neg(f'có {MINDS}', PC)}",
        S.katha_end(KATHA[6]))

    # ---- (142) 7. Pariyāpannakathā --------------------------------------------------------------------------------
    heading("5-22-7-0", 4, VAGGA)
    heading("5-22-7-1-0", 5, f"(142) 7. {S.katha(KATHA[7])}")

    S_R, S_D = SR["sadda"]
    PH_R, PH_D = SR["phoṭṭhabba"]
    GRP = f"{SR['gandha'][0]}{PE} {SR['rasa'][0]}{PE} {PH_R}"          # gandharāgo…pe… rasarāgo…pe… phoṭṭhabbarāgo

    def plane_seg(r, d, short=False):
        """^5-703 (rūparāgo) / ^5-704 (arūparāgo, short = the second, abridged form as written)."""
        th = li(r, d)
        pos = f"nó {seek()}, {withm()}"
        neg = f"nó {seek(True)}, {withm(True, short)}"
        if short:                     # …pe…. Nanu … (capital); Hañci na samāpattesiyo na upapattesiyo…pe… ekārammaṇo
            hneg = f"nó không {SEEK[0]}, không {SEEK[1]}{PE} có cùng một đối tượng"
            l1 = f"{Q(th)} {YES} {Q(pos)} {NO_PE} {NANU(neg)} {YES} {S.hanci_neg(hneg, th)}"
        else:                         # …pe… nanu … ; Hañci na … na diṭṭhadhammasukhavihāro…pe… ekārammaṇo …"ti…pe….
            hneg = f"nó {seek(True)}{PE} có cùng một đối tượng"
            l1 = f"{Q(th)} {YES} {Q(pos)} {NO_PE} {nanu(neg)} {YES} {S.hanci_neg(hneg, th)[:-1]}{PE}"
        l2 = f"{Q(th)} {YES} {Q(li(S_R, S_D))} {NO_PE} {q(th)} {YES} {Q(f'{GRP} nằm sẵn trong {PH_D}, {incl(PH_D)}')} {NO_PE}"
        own = pna(lies(r, d), incl(d))
        if short:                     # "…pariyāpanno"ti, na hevaṃ vattabbe…pe… (comma, lower case: kept as written)
            mid = f"{own[:-len(' không?')]} không, {NO[0].lower()}{NO[1:-1]}{PE}"
        else:
            mid = f"{own} {NO_PE}"
        l3 = (f"{pna(lies(S_R, S_D), incl(S_D))} {YES} {mid} "
              f"{pna(f'{GRP} nằm sẵn trong {PH_D}', incl(PH_D), low=True)} {YES} {own} {NO_PE}")
        return l1, l2, l3

    add("5-703", *plane_seg(RR, RD))
    add("5-704", *plane_seg(ARR, ARD, short=True))
    LI2 = f"{lies(RR, RD)}, {incl(RD)}, {lies(ARR, ARD)}, {incl(ARD)}"
    KLI = f"{lies(KR, KD)}, {incl(KD)}"
    add("5-705",
        f"{S.na_vattabbam(LI2)} {YES} {NANU(KLI)} {YES} {S.hanci(KLI, LI2)}",
        S.katha_end(KATHA[7]))

    # ---- (143) 8. Abyākatakathā -----------------------------------------------------------------------------------
    heading("5-22-8-0", 4, VAGGA)
    heading("5-22-8-1-0", 5, f"(143) 8. {S.katha(KATHA[8])}")
    add("5-706",
        f"{Q(DG_TH)} {YES} {Q(VIPKIR)} {NO_PE} {q(DG_TH)} {YES} {Q(f'sự tiếp xúc {DGS} thì {ABY}')} {NO_PE} "
        f"{q(DG_TH)} {YES} {Q(f'cảm giác{PE} tri giác{PE} chủ ý{PE} tâm {DGS} thì {ABY}')} {NO_PE}",
        #   diṭṭhigatasampayutto phasso abyākato («thì» for readability, as ch17 «… thì không có đối tượng»)
        f"{Q(f'sự tiếp xúc {DGS} là bất thiện')} {YES} {Q(DG_AK)} {NO_PE} "
        f"{q(f'cảm giác, tri giác, chủ ý, tâm {DGS} là bất thiện')} {YES} {Q(DG_AK)} {NO_PE}")
    add("5-707",
        f"{Q(DG_TH)} {YES} {Q(FRUIT_N)} {NO_PE} {nanu(FRUIT)} {YES} {S.hanci_neg(FRUIT, DG_TH)}",
        f"{Q(DG_TH)} {YES} Chẳng phải {VAJJA} [{CIT['a. ni.']}] sao? {YES} {S.hanci_neg(VAJJA, DG_TH)}",
        f"{Q(DG_TH)} {YES} {S.NANU_VUTTAM} “Này {VACCHA}, quan điểm sai lầm là bất thiện "
        f"[dị bản ({CIT['ma. ni.']} 2.194): akusalaṃ], quan điểm đúng đắn là thiện” "
        f"[dị bản ({CIT['ma. ni.']} 2.104): kusalaṃ] [{CIT['ma. ni.']} 2.194]! {S.ATTHEVA} {YES} "
        f"{S.tena_hi_na(DG_TH)}",
        f"{Q(DG_TH)} {YES} {S.NANU_VUTTAM} “Này {PUNNA}, đối với người có quan điểm sai lầm, Ta nói đến một cõi "
        f"tái sinh trong hai cõi tái sinh – địa ngục hoặc cõi súc sinh” [{CIT['ma. ni.']} 2.79]! {S.ATTHEVA} {YES} "
        f"{S.tena_hi_na(DG_TH)}")
    add("5-708",
        f"{S.na_vattabbam(DG_TH)} {YES} {S.NANU_VUTTAM} “{views_sutta()}” "
        f"[{CIT['saṃ. ni.']} 4.416, nhưng hơi khác một chút]! {S.ATTHEVA} {YES} {S.tena_hi(DG_TH)}",
        f"{Q(DG_TH)} {YES} {S.NANU_VUTTAM} “{SUT_MICCHA}” [{CIT['a. ni.']} 1.306]! {S.ATTHEVA} {YES} "
        f"{S.tena_hi_na(DG_TH)}",
        S.katha_end(KATHA[8]))

    # ---- (144) 9. Apariyāpannakathā -------------------------------------------------------------------------------
    heading("5-22-9-0", 4, VAGGA)
    heading("5-22-9-1-0", 5, f"(144) 9. {S.katha(KATHA[9])}")
    add("5-709", f"{Q(DG_AP)} {YES} {MAGGA} {NO_PE}")
    KAMESU = S.vattabbo("đã lìa tham đắm đối với các dục lạc")     # "kāmesu vītarāgo"ti vattabbo
    add("5-710",
        f"{S.na_vattabbam(DG_AP)} {YES} {Q(f'người phàm phu {KAMESU}')} "
        f"{YES} {Q(S.vattabbo('đã lìa quan điểm'))} {NO} {S.tena_hi(DG_AP)}",
        S.katha_end(KATHA[9]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# Helper modes (read-only lookups; no files written)
# ---------------------------------------------------------------------------------------------------------------
def termbase():
    tb = {}
    for ln in TB.read_text(encoding="utf-8").splitlines():
        if ": {" in ln:
            tb[ln.split(": {", 1)[0]] = ln
    return tb


def nel(p):
    return [x for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def helper(args):
    if args[0] == "--word":
        pat = re.compile(args[1], re.I)
        for h, ln in termbase().items():
            if pat.search(h):
                print(ln[:700])
    elif args[0] == "--kw":
        lo, hi = int(args[1]), int(args[2])
        tb = termbase()
        tbl = {k.lower(): v for k, v in tb.items()}
        seen = set()
        for line in KW.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\[5-(\d+)\] (.*)", line)
            if not m or not lo <= int(m.group(1)) <= hi:
                continue
            for k in m.group(2).split(", "):
                if k.lower() in seen:
                    continue
                seen.add(k.lower())
                e = tb.get(k) or tbl.get(k.lower())
                print(f"[{m.group(1)}] {e[:500] if e else k + ': <NOT IN TERMBASE>'}")
    elif args[0] == "--find":
        pat = re.compile(args[1])
        mx = int(args[2]) if len(args) > 2 else 6
        mc = int(args[3]) if len(args) > 3 else 700
        hits = 0
        for f in FINISHED:
            pl, vl = nel(S.PALI_DIR / f), nel(S.OUT_DIR / f)
            for i, ln in enumerate(pl):
                m = pat.search(ln)
                if m:
                    s = max(0, m.start() - 100)
                    print(f"[{f} line {i + 1}]\n  PI: {ln[s:s + 400]}\n  VI: {vl[i][:mc] if i < len(vl) else '<missing>'}")
                    hits += 1
                    if hits >= mx:
                        return


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-22"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].startswith("--"):
        helper(sys.argv[1:])
    else:
        main()
