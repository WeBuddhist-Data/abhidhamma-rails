"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 24, Soḷasamavaggo (^5-24-0 … ^5-775): ten kathās
(156-165) with the repeated "Soḷasamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/24-solasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, katha, katha_end, var_sp …). Strings taken from pi-1 … pi-4 rails are asserted there
(REUSED24); strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-24.md.

usage: python -I -X utf8 -B build_rails_24_vi.py          (writes the chapter and the adherence copy rails\\adh-24\\)
       python -I -X utf8 -B build_rails_24_vi.py --find <regex> [max_hits] [maxchars]
              (helper: the line of the finished pi-5 rails chapters for a Pāli pattern; reads named files only)
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "24-solasamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap = S.cap
CIT = S.CIT

DONE = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
        "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
        "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
        "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
        "16-atthamavaggo.md", "17-navamavaggo.md", "18-dasamavaggo.md", "20-dvadasamavaggo.md"]


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ mười sáu"                                           # Soḷasamavaggo (termbase)
TASSUDDANAM = "Tóm tắt của chương này –"                                # Tassuddānaṃ – (ch9)
RUPA, PH, VIP = "vật chất", "sự tiếp xúc", "quả"                         # rūpaṃ (ch16) / phasso / vipāko (ch15, ch20)

# attention list and feeling lists (ch15 / ch20, byte-identical)
AV7 = ["sự hướng đến", "sự chú hướng", "sự lưu ý", "sự chú tâm", "chủ ý", "sự mong ước", "sự mong cầu"]
AVS = f"{AV7[0]}{PE} {AV7[-1]}"                                          # āvaṭṭanā…pe… paṇidhi
VED3 = ["được cảm nhận là dễ chịu", "được cảm nhận là khó chịu",
        "được cảm nhận là không khó chịu cũng không dễ chịu"]           # sukha- / dukkha- / adukkhamasukhavedaniya
SUKHA_V, DUKKHA_V, UPEKKHA_V = ("cảm giác dễ chịu", "cảm giác khó chịu",
                                "cảm giác không khó chịu cũng không dễ chịu")
SAMP3 = [f"gắn liền với {SUKHA_V}", f"gắn liền với {DUKKHA_V}", f"gắn liền với {UPEKKHA_V}"]
POS_SH = f"{VED3[0]}, {VED3[1]}{PE} có đối tượng"                       # sukhavedaniyo dukkhavedaniyo…pe… sārammaṇo
NEG_SH = f"không {VED3[0]}, không {VED3[1]}{PE} không có đối tượng"     # na sukhavedaniyo na dukkhavedaniyo…pe… anārammaṇo

OBJ, NOBJ = "nó có đối tượng", "nó không có đối tượng"                  # sārammaṇaṃ / anārammaṇaṃ (ch16)
HAS, NHAS = f"nó có {AVS}", f"nó không có {AVS}"                        # (n)atthi tassa āvaṭṭanā…pe… paṇidhi (ch16)

# mental factors (ch16 lists; termbase)
ALOBHO, ADOSO, AMOHO = "sự không tham lam", "sự không sân hận", "sự không si mê"
LOBHO, DOSO, MOHO = "sự tham lam", "sự sân hận", "sự si mê"
SADDHA, VIRIYA, SATI, SAMADHI, PANNA = "niềm tin", "sự tinh tấn", "sự tỉnh thức", "sự định tâm", "trí tuệ"
MANO, DITTHI, VICI, THINA, UDDH, AHIR, ANOT = ("sự kiêu mạn", "quan điểm", "sự hoài nghi", "sự uể oải", "sự xao động",
                                              "sự không biết hổ thẹn", "sự không biết ghê sợ tội lỗi")

# kathā 1-3: niggaha / paggaha / sukhānuppadāna
PARO = "một người"                                                       # Paro (termbase)
NIG = f"{PARO} chế ngự tâm của người khác"                               # paro parassa cittaṃ niggaṇhāti
PAG = f"{PARO} nâng tâm của người khác lên"                              # paro parassa cittaṃ paggaṇhāti
MA4 = "bảo rằng “đừng tham đắm”, “đừng sân hận”, “đừng si mê”, “đừng bị phiền não làm ô nhiễm”"
#   "mā rajji", "mā dussi", "mā muyhi", "mā kilissī"ti (mā «đừng»: termbase, pi-4)
MA_N = "bảo rằng “đừng chấm dứt”"                                        # "mā nirujjhī"ti
UP = "đã sinh khởi"                                                      # uppanna
LIST9 = [f"tri giác {UP}", f"chủ ý {UP}", f"tâm {UP}", f"niềm tin {UP}", f"sự tinh tấn {UP}", f"sự tỉnh thức {UP}",
         f"sự định tâm {UP}"]                                            # uppannā saññā … uppanno samādhi
ATTHAYA = "vì lợi ích của người khác"                                    # parassa atthāya
SACCA4 = "hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, tu tập con đường"  # (ch5)
KARAKO = ("một người là người tạo cho người khác, sự dễ chịu và sự khó chịu do người khác làm ra, một người làm, "
          "một người khác cảm nhận")                                     # Añño aññassa kārako … (ch15)
BALA = "có những người đã đạt đến sức mạnh, có những người đã đạt được sự làm chủ"   # atthi balappattā, atthi vasībhūtā
#   (termbase pattā «đã đạt đến», bhūtā «đã đạt được», vasī «sự làm chủ»)
DHP165 = ["“Điều ác đã được làm bởi chính mình, chính mình bị phiền não làm ô nhiễm;",
          "Điều ác chính mình không làm, chính mình được thanh tịnh;",
          "Trong sạch hay không trong sạch là việc riêng của mỗi người, không ai có thể làm cho người khác trong sạch” "
          f"[{CIT['dha. pa.']} 165]."]
DHP165_SH = "“điều ác đã được làm bởi chính mình… không ai có thể làm cho người khác trong sạch”."
SUKHA = f"{PARO} trao sự dễ chịu cho người khác"                         # paro parassa sukhaṃ anuppadeti
UDAYI = "Ưu-đà-di"                                                       # Udāyī (no termbase entry: new name)
SUT_U = ("“Quả thật, Đức Thế Tôn đã loại bỏ khỏi chúng ta nhiều hiện tượng khó chịu, quả thật, Đức Thế Tôn đã mang "
         "lại cho chúng ta nhiều hiện tượng dễ chịu, quả thật, Đức Thế Tôn đã loại bỏ khỏi chúng ta nhiều hiện tượng "
         "bất thiện, quả thật, Đức Thế Tôn đã mang lại cho chúng ta nhiều hiện tượng thiện” "
         f"[{CIT['ma. ni.']} 2.148, trong kinh Ví Dụ Chim Cút]!")
#   bahūnaṃ vata no bhagavā dukkhadhammānaṃ apahattā, … kusalānaṃ dhammānaṃ upahattā [ma. ni. 2.148 laṭukikopame]

# kathā 4: adhigayha manasikāra
T4 = "chú tâm bằng cách nắm gộp lại"                                     # adhigayha manasi karoti (termbase)
TT = {"a": "quá khứ", "n": "tương lai", "p": "hiện tại"}                 # atītaṃ / anāgataṃ / paccuppannaṃ
DHP277 = ["“Tất cả các tạo tác đều vô thường, khi thấy như vậy bằng trí tuệ;",
          "Khi ấy nhàm chán khổ đau, đây là con đường đến sự thanh tịnh.",
          "“Tất cả các tạo tác đều là khổ đau, khi thấy như vậy bằng trí tuệ;",
          "Khi ấy nhàm chán khổ đau, đây là con đường đến sự thanh tịnh.",
          "“Tất cả các hiện tượng đều không phải là tự ngã, khi thấy như vậy bằng trí tuệ;",
          f"Khi ấy nhàm chán khổ đau, đây là con đường đến sự thanh tịnh” [{CIT['dha. pa.']} 277-279]."]

# kathās 5-8: rūpa
GR = "gốc rễ"                                                            # hetu (termbase core «gốc rễ»)
T5 = f"{RUPA} là {GR}"                                                   # rūpaṃ hetu (termbase)
T6 = f"{RUPA} có {GR}"                                                   # rūpaṃ sahetukaṃ (termbase)
T7K, T7A = f"{RUPA} là thiện", f"{RUPA} là bất thiện"                    # rūpaṃ kusalaṃ / akusalaṃ (termbase)
RK = "vật chất vừa là thiện vừa là bất thiện"                            # rūpaṃ kusalampi akusalampi (ch16)
T8 = f"{RUPA} là {VIP}"                                                  # rūpaṃ vipāko
MB = "các yếu tố cơ bản là gốc rễ mà vật chất phái sinh dựa vào"          # mahābhūtā upādāyarūpānaṃ upādāyahetu
MB_V = ("các yếu tố cơ bản là gốc rễ mà vật chất phái sinh"
        f"{S.var_sp('Sī., Pī., Ka.', 'upādārūpānaṃ')} dựa vào")
KATATTA = "sinh khởi do nghiệp đã được tạo"                              # kammassa katattā uppanna (ch20)
CC = f"tâm và các yếu tố đồng hành với tâm {KATATTA}"                    # kammassa katattā uppannā cittacetasikā dhammā

# kathās 9-10: spheres
RA, AA, KA = "thuộc cõi hình sắc", "thuộc cõi không hình sắc", "thuộc cõi dục lạc"   # (termbase; ch11)
T9R, T9A = f"có {RUPA} {RA}", f"có {RUPA} {AA}"                          # atthi rūpaṃ rūpāvacaraṃ / arūpāvacaraṃ
S3 = ["tìm cầu sự thành tựu thiền", "tìm cầu sự tái sinh", "an trú trong hạnh phúc ngay trong đời này"]
#   samāpattesiya / upapattesiya / diṭṭhadhammasukhavihāra (termbase; ch12 «tâm tìm cầu sự tái sinh»; pi-1)
C8 = ["đi kèm", "cùng sinh", "hòa lẫn", "gắn liền", "có cùng một sự sinh khởi", "có cùng một sự chấm dứt",
      "có cùng một chỗ dựa", "có cùng một đối tượng"]                    # sahagata … ekārammaṇa (ch15)
I3 = [f"tâm {x}" for x in S3]                                            # samāpattesiyena cittena …
RDH, ARDH, KDH = "cõi hình sắc", "cõi không hình sắc", "cõi dục lạc"     # rūpa- / arūpa- / kāmadhātu (termbase; ch16)
NT = "nằm trong"                                                         # pariyāpanna (APPROVED)
RAGA = {"rūpa": "sự tham đắm cõi hình sắc", "arūpa": "sự tham đắm cõi không hình sắc",
        "kāma": "sự tham đắm dục lạc", "sadda": "sự tham đắm âm thanh", "gandha": "sự tham đắm mùi",
        "rasa": "sự tham đắm vị", "phoṭṭhabba": "sự tham đắm vật xúc chạm"}   # X-rāgo (termbase; ch3 / ch10)
YT = {"sadda": "yếu tố âm thanh", "phoṭṭhabba": "yếu tố vật xúc chạm"}  # sadda- / phoṭṭhabbadhātu (termbase)
RR = f"{RAGA['rūpa']} {NT} {RDH}"                                        # rūparāgo rūpadhātupariyāpanno (termbase)
ARR = f"{RAGA['arūpa']} {NT} {ARDH}"                                     # arūparāgo arūpadhātupariyāpanno (termbase)
KRR = f"{RAGA['kāma']} {NT} {KDH}"                                       # kāmarāgo kāmadhātupariyāpanno (termbase)

KATHA = {1: "sự chế ngự", 2: "sự nâng lên", 3: "việc trao sự dễ chịu", 4: "sự chú tâm bằng cách nắm gộp lại",
         5: f"việc {T5}", 6: f"việc {T6}", 7: f"việc {T7K} và bất thiện", 8: f"việc {T8}", 9: f"việc {RUPA} {RA} và {AA}",
         10: f"những gì {NT} {RDH} và {ARDH}"}
#   Niggaha-, Paggaha-, Sukhānuppadāna- (termbase headings), Adhigayhamanasikāra-, Rūpaṃ hetūti-, Rūpaṃ sahetukanti-,
#   Rūpaṃ kusalākusalanti-, Rūpaṃ vipākoti-, Rūpaṃ rūpāvacarārūpāvacaranti-, Rūpārūpadhātupariyāpannakathā (termbase)
KATHA10B = f"việc {RR}, {ARR}"                     # Rūparāgo rūpadhātupariyāpanno arūparāgo arūpadhātupariyāpannotikathā
UDDANA = ("Sự chế ngự tâm, sự nâng tâm lên, việc trao sự dễ chịu, sự chú tâm bằng cách nắm gộp lại, "
          f"{T5}, {T6}, {RK}, {T8}, {T9R}, {T9A}, tất cả các phiền não đều {NT} {KDH}.")
#   Cittaniggaho, cittapaggaho, sukhānuppadānaṃ, adhigayha manasikāro, rūpaṃ hetu, rūpaṃ sahetukaṃ, rūpaṃ kusalampi
#   akusalampi, rūpaṃ vipāko, atthi rūpaṃ rūpāvacaraṃ atthi rūpaṃ arūpāvacaraṃ, sabbe kilesā kāmadhātupariyāpannāti.

REUSED24 = [  # (Pāli, Vietnamese, book)
    ("upādāyarūpaṃ", "vật chất phái sinh", "2"),
    ("mahābhūtā", "yếu tố cơ bản", "2"),
    ("sappaccayaṃ", "có điều kiện", "1"),
    ("sahetukā", "có gốc rễ", "1"),
    ("cittacetasikā dhammā", "tâm và các yếu tố đồng hành với tâm", "1"),
    ("sahagataṃ sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ", "đi kèm, cùng sinh, hòa lẫn, gắn liền", "2"),
    ("diṭṭhadhammasukhavihāraṃ", "an trú trong hạnh phúc ngay trong đời này", "1"),
    ("alobho … kusalamūlaṃ", "sự không tham lam, tức gốc rễ thiện", "1"),
    ("adoso", "sự không sân hận", "1"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("dha. pa. (citation)", "[Kinh Pháp Cú ", "3-brahmacariyakatha.md"),
    ("sabbe dhammā anattā", "tất cả các hiện tượng đều không phải là tự ngã", "1-puggalakatha.md"),
    ("dukkhaṃ parijānāti, … maggaṃ bhāveti", SACCA4, "5-sabbamatthitikatha.md"),
    ("Nanu āyasmā X etadavoca –", "Chẳng phải tôn giả Nan-đa-ka đã nói thế này sao –", "5-sabbamatthitikatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("attano / aññesaṃ / tassa; neva … na … na", "của chính mình, cũng không của người khác, cũng không của người ấy",
     "10-dutiyavaggo.md"),
    ("sabbe saṅkhārā aniccā", "tất cả các tạo tác đều vô thường", "10-dutiyavaggo.md"),
    ("yadaniccaṃ taṃ dukkhaṃ", "là khổ đau", "10-dutiyavaggo.md"),
    ("Rūparāgaṃ arūparāgaṃ", f"{RAGA['rūpa']}, {RAGA['arūpa']}", "10-dutiyavaggo.md"),
    ("manasi karoti", "chú tâm đến", "11-tatiyavaggo.md"),
    ("upapattesiyena cittena", "tâm tìm cầu sự tái sinh", "12-catutthavaggo.md"),
    ("rāgaṃ pajahati, dosaṃ pajahati, mohaṃ pajahati, anottappaṃ pajahati",
     "dứt bỏ sự tham đắm, dứt bỏ sự sân hận, dứt bỏ sự si mê, dứt bỏ sự không biết ghê sợ tội lỗi",
     "12-catutthavaggo.md"),
    ("Tena phassena taṃ phassaṃ phusati, tāya vedanāya",
     "Có phải bằng sự tiếp xúc ấy mà chạm vào sự tiếp xúc ấy, bằng cảm giác ấy", "13-pancamavaggo.md"),
    ("tāya paññāya taṃ paññaṃ pajānāti", "bằng trí tuệ ấy mà hiểu rõ trí tuệ ấy", "13-pancamavaggo.md"),
    ("Taṃ ñāṇaṃ tassa ñāṇassa ārammaṇanti?", "Có phải hiểu biết ấy là đối tượng của hiểu biết ấy không?",
     "13-pancamavaggo.md"),
    ("Añño aññassa kārako …", KARAKO, "15-sattamavaggo.md"),
    ("sahagatā … ekārammaṇā (cittena)", ", ".join(C8) + " với tâm", "15-sattamavaggo.md"),
    ("Dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hotīti?",
     "Có phải có sự tụ hợp của hai sự tiếp xúc… hai tâm không?", "15-sattamavaggo.md"),
    ("sukhavedaniyo … sārammaṇo (full list)", ", ".join(VED3 + SAMP3) + ", gắn liền với sự tiếp xúc",
     "15-sattamavaggo.md"),
    ("sārammaṇaṃ …? nanu anārammaṇaṃ …? Hañci anārammaṇaṃ …",
     f"Có phải {OBJ}, {HAS} không? {NO_PE} {nanu_l(f'{NOBJ}, {NHAS}')} {YES} Nếu {NOBJ}, {NHAS}",
     "16-atthamavaggo.md"),
    ("Na vattabbaṃ – rūpaṃ kusalampi akusalampī … (^5-538 line 1)",
     "Có phải không nên nói – “vật chất vừa là thiện vừa là bất thiện” không? Đúng vậy. Chẳng phải nghiệp bằng thân, "
     "nghiệp bằng lời nói vừa là thiện vừa là bất thiện sao? Đúng vậy. Nếu nghiệp bằng thân, nghiệp bằng lời nói vừa "
     "là thiện vừa là bất thiện, thì này bạn, chắc chắn nên nói – “vật chất vừa là thiện vừa là bất thiện”.",
     "16-atthamavaggo.md"),
    ("saddhā, vīriyaṃ, sati, samādhi, paññā; lobho … anottappaṃ (lists)",
     "sự tinh tấn… sự tỉnh thức… sự định tâm… trí tuệ", "16-atthamavaggo.md"),
    ("māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirikaṃ, anottappaṃ",
     "sự kiêu mạn… quan điểm… sự hoài nghi… sự uể oải… sự xao động… sự không biết hổ thẹn… "
     "sự không biết ghê sợ tội lỗi", "16-atthamavaggo.md"),
    ("rūpadhātu (kathā name)", "Bàn về cõi hình sắc", "16-atthamavaggo.md"),
    ("[… sutte] citation", ", trong kinh Thấu Triệt]", "16-atthamavaggo.md"),
    ("kammassa katattā uppannaṃ", KATATTA, "20-dvadasamavaggo.md"),
    ("Xti-kathā", "Bàn về việc sự thu thúc là nghiệp", "20-dvadasamavaggo.md"),
    ("āvaṭṭanā…pe… paṇidhi", AVS, "20-dvadasamavaggo.md"),
    ("sukhavedaniyo dukkhavedaniyo…pe… sārammaṇo", POS_SH, "20-dvadasamavaggo.md"),
    ("na sukhavedaniyo na dukkhavedaniyo…pe… anārammaṇo", NEG_SH, "20-dvadasamavaggo.md"),
    ("Phasso vipāko, phasso …", f"{PH} là {VIP}, {PH}", "20-dvadasamavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED24 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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
def obj_frame(t, end="."):          # T? Āmantā. Sārammaṇaṃ, atthi …? nanu anārammaṇaṃ, natthi …? Hañci …, no ca … "T"
    h = S.hanci_neg(f"{NOBJ}, {NHAS}", t)
    if end != ".":
        h = h[:-1] + end
    return f"{Q(t)} {YES} {Q(f'{OBJ}, {HAS}')} {NO_PE} {nanu_l(f'{NOBJ}, {NHAS}')} {YES} {h}"


def ob(x, neg=False):               # X (an)ārammaṇo, (n)atthi tassa āvaṭṭanā…pe… paṇidhi
    return f"{x}, không có đối tượng, {NHAS}" if neg else f"{x}, có đối tượng, {HAS}"


def esi(neg=False):                 # (na) samāpattesiyaṃ (na) upapattesiyaṃ (na) diṭṭhadhammasukhavihāraṃ
    return ", ".join(("không " if neg else "") + x for x in S3)


def full(neg=False):                # … , (na) samāpattesiyena cittena … sahagataṃ … ekārammaṇaṃ (all spelled out)
    if not neg:
        return f"nó {esi()}, {', '.join(C8)} với {I3[0]}, với {I3[1]}, với {I3[2]}"
    return f"nó {esi(True)}, không {', '.join(C8)} với {I3[0]}, không với {I3[1]}, không với {I3[2]}"


def short(k):                       # na samāpattesiyena cittena…pe… <the last k items of C8>
    return f"không{PE} {', '.join(C8[-k:])} với {I3[0]}"


def att(x):                         # X "X"nti manasi karoti
    return f"chú tâm đến {TT[x]} như là “{TT[x]}”"


def mk(a, *bs):                     # A "A"nti manasikaronto, B "B"nti manasi karoti(, C …)
    return f"trong khi {att(a)}, thì " + ", ".join(att(b) for b in bs)


def sam(n):                         # Dvinnaṃ / Tiṇṇaṃ phassānaṃ…pe… cittānaṃ samodhānaṃ hoti
    return f"có sự tụ hợp của {n} sự tiếp xúc{PE} {n} tâm"


def isvip(x):                       # X vipāko
    return f"{x} là {VIP}"


def pos(x, lst):                    # X vipāko, X sukhavedaniyo…pe… sārammaṇo, atthi tassa āvaṭṭanā…pe… paṇidhi
    return f"{isvip(x)}, {x} {lst}, {HAS}"


def neg(x, lst):                    # X vipāko, X na sukhavedaniyo…pe… anārammaṇo, natthi tassa āvaṭṭanā…pe… paṇidhi
    return f"{isvip(x)}, {x} {lst}, {NHAS}"


def nv_dhatu(raga_key, pred):       # X-rāgo na vattabbaṃ – "Y-pariyāpanno"ti?
    return f"đối với {RAGA[raga_key]}, không nên nói – “{NT} {pred}”"


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

    def sub(n, num):
        heading(f"5-24-{n}-0", 4, VAGGA)
        heading(f"5-24-{n}-1-0", 5, f"({num}) {n}. {S.katha(KATHA[n])}")

    heading("5-24-0", 3, VAGGA)

    # ---- (156) 1. Niggahakathā; (157) 2. Paggahakathā ----------------------------------------------------------
    def np_block(t, verb, lst_tail, janeti, moha, sacca_pe, short_sutta):
        """Lines of ^5-743 / ^5-745; verb(x) = 'chế ngự x' / 'nâng x lên'."""
        def act(obj):
            return f"{PARO} {verb(obj)}"
        l1 = (f"{Q(t)} {YES} {Q(f'{t}, {MA4}')} {NO_PE} {q(t)} {YES} ")
        if janeti:
            JAN = (f"{PARO} làm sinh khởi nơi người khác {ALOBHO}, tức gốc rễ thiện{PE} làm sinh khởi {ADOSO}, tức gốc "
                   f"rễ thiện{PE} làm sinh khởi {AMOHO}, tức gốc rễ thiện{PE} làm sinh khởi {SADDHA}{PE} làm sinh khởi "
                   f"{VIRIYA}{PE} làm sinh khởi {SATI}{PE} làm sinh khởi {SAMADHI}{PE} làm sinh khởi {PANNA}")
            l1 += f"{Q(JAN)} {NO_PE} {q(t)} {YES} "
        l1 += (f"{Q(act(f'{PH} {UP} của người khác') + ', ' + MA_N)} {NO_PE} "
               f"{q(act(lst_tail) + ', ' + MA_N)} {NO_PE}")
        pj = f"dứt bỏ sự tham đắm{PE} dứt bỏ sự sân hận{PE} " + (f"dứt bỏ sự si mê{PE} " if moha else "")
        l2 = f"{Q(t)} {YES} {Q(f'{PARO}, {ATTHAYA}, {pj}dứt bỏ sự không biết ghê sợ tội lỗi')} {NO_PE}"
        l3 = (f"{Q(t)} {YES} {Q(f'{PARO}, {ATTHAYA}, tu tập con đường{PE} tu tập sự thiết lập tỉnh thức{PE} tu tập chi phần giác ngộ')} "
              f"{NO_PE}")
        s4 = f"hiểu biết trọn vẹn khổ đau{PE} tu tập con đường" if sacca_pe else SACCA4
        l4 = f"{Q(t)} {YES} {Q(f'{PARO}, {ATTHAYA}, {s4}')} {NO_PE}"
        l5 = f"{Q(t)} {YES} {Q(KARAKO)} {NO_PE}"
        if short_sutta:
            return [l1, l2, l3, l4, l5,
                    f"{Q(t)} {YES} {S.NANU_VUTTAM} {DHP165_SH} {S.ATTHEVA} {YES} {S.tena_hi_na(t)}"]
        return [l1, l2, l3, l4, l5, f"{Q(t)} {YES} {S.NANU_VUTTAM}", *DHP165,
                f"{S.ATTHEVA} {YES} {S.tena_hi_na(t)}"]

    heading("5-24-1-0", 4, f"(156) 1. {S.katha(KATHA[1])}")
    NIG_LIST = (f"cảm giác {UP} của người khác{PE} " + f"{PE} ".join(LIST9) + f"{PE} trí tuệ {UP}")
    add("5-743", *np_block(NIG, lambda x: f"chế ngự {x}", NIG_LIST, False, False, False, False))
    add("5-744",
        f"{S.na_vattabbam(NIG)} {YES} {NANU(BALA)} {YES} {S.hanci(BALA, NIG)}",
        S.katha_end(KATHA[1]))

    sub(2, 157)
    PAG_LIST = f"cảm giác {UP} của người khác{PE} trí tuệ {UP}"
    add("5-745", *np_block(PAG, lambda x: f"nâng {x} lên", PAG_LIST, True, True, True, True))
    add("5-746",
        f"{S.na_vattabbam(PAG)} {YES} {NANU(BALA)} {YES} {S.hanci(BALA, PAG)}",
        S.katha_end(KATHA[2]))

    # ---- (158) 3. Sukhānuppadānakathā ---------------------------------------------------------------------------
    sub(3, 158)
    DUK = f"{PARO} trao sự khó chịu cho người khác"
    NDUK = f"{PARO} không trao sự khó chịu cho người khác"
    NSUK = f"{PARO} không trao sự dễ chịu cho người khác"
    OWN = (f"{PARO} trao cho người khác sự dễ chịu của chính mình, trao sự dễ chịu của người khác, "
           f"trao sự dễ chịu của người ấy")
    NOWN = (f"{PARO} không trao cho người khác sự dễ chịu của chính mình, cũng không của người khác, "
            f"cũng không của người ấy")
    add("5-747",
        f"{Q(SUKHA)} {YES} {Q(DUK)} {NO_PE} {q(NDUK)} {YES} {Q(NSUK)} {NO_PE} {q(SUKHA)} {YES} {Q(OWN)} {NO_PE} "
        f"{q(NOWN)} {YES} {S.hanci_neg(NOWN, SUKHA)}",
        f"{Q(SUKHA)} {YES} {Q(KARAKO)} {NO_PE}")
    add("5-748",
        f"{S.na_vattabbam(SUKHA)} {YES} Chẳng phải tôn giả {UDAYI} đã nói thế này sao – {SUT_U} {S.ATTHEVA} {YES} "
        f"{S.tena_hi(SUKHA)}",
        S.katha_end(KATHA[3]))

    # ---- (159) 4. Adhigayhamanasikārakathā ----------------------------------------------------------------------
    sub(4, 159)
    C1 = "bằng tâm ấy mà hiểu rõ tâm ấy"
    C2 = "bằng tâm ấy mà hiểu rõ tâm ấy là “tâm”"
    C3 = "tâm ấy là đối tượng của tâm ấy"
    TOUCH = (f"bằng sự tiếp xúc ấy mà chạm vào sự tiếp xúc ấy, bằng cảm giác ấy{PE} bằng tri giác ấy{PE} bằng chủ ý "
             f"ấy{PE} bằng tâm ấy{PE} bằng sự hướng tâm ấy{PE} bằng sự duy trì tâm ấy{PE} bằng sự hân hoan ấy{PE} bằng "
             f"sự tỉnh thức ấy{PE} bằng trí tuệ ấy mà hiểu rõ trí tuệ ấy")
    add("5-749",
        f"{Q(T4)} {YES} {Q(C1)} {NO_PE} {q(C1)} {YES} {Q(C2)} {NO_PE} {q(C2)} {YES} {Q(C3)} {NO_PE}",
        f"{Q(C3)} {YES} {Q(TOUCH)} {NO_PE}")

    def tl(a, *bs):
        m = mk(a, *bs)
        n = "ba" if len(bs) == 2 else "hai"
        return f"{Q(m)} {NO_PE} {q(m)} {YES} {Q(sam(n))} {NO_PE}"
    add("5-750", tl("a", "n"), tl("a", "p"), tl("a", "n", "p"))
    add("5-751", tl("n", "a"), tl("n", "p"), tl("n", "a", "p"))
    add("5-752", tl("p", "a"), tl("p", "n"), tl("p", "a", "n"))
    add("5-753",
        f"{S.na_vattabbam(T4)} {YES} {S.NANU_VUTTAM}",
        *DHP277,
        f"{S.ATTHEVA} {YES} {S.tena_hi(T4)}",
        S.katha_end(KATHA[4]))

    # ---- (160) 5. Rūpaṃ hetūtikathā -----------------------------------------------------------------------------
    sub(5, 160)
    G = {"a": f"{GR} không tham lam", "d": f"{GR} không sân hận", "m": f"{GR} không si mê",
         "l": f"{GR} tham lam", "o": f"{GR} sân hận", "h": f"{GR} si mê"}  # alobho / adoso / … hetu (as a kind of root)
    add("5-754",
        f"{Q(T5)} {YES} {Q(f'nó là {G['a']}')} {NO_PE} "
        f"{q(f'nó là {G['d']}{PE} {G['m']}{PE} {G['l']}{PE} {G['o']}{PE} {G['h']}')} {NO_PE}",
        obj_frame(T5))
    H5 = [f"{x} là {GR}" for x in (ADOSO, AMOHO, LOBHO, DOSO, MOHO)]
    H5L = f"{PE} ".join(H5)
    add("5-755",
        f"{Q(ob(f'{ALOBHO} là {GR}'))} {YES} {Q(ob(T5))} {NO_PE} {q(ob(H5L))} {YES} {Q(ob(T5))} {NO_PE}",
        f"{Q(ob(T5, True))} {YES} {Q(ob(f'{ALOBHO} là {GR}', True))} {NO_PE} {q(ob(T5, True))} {YES} "
        f"{Q(ob(H5L, True))} {NO_PE}")
    add("5-756",
        f"{S.na_vattabbam(T5)} {YES} {NANU(MB_V)} {YES} {S.hanci(MB, T5)}",
        S.katha_end(KATHA[5]))

    # ---- (161) 6. Rūpaṃ sahetukantikathā ------------------------------------------------------------------------
    sub(6, 161)
    add("5-757",
        f"{Q(T6)} {YES} {Q(f'nó có {G['a']}')} {NO_PE} "
        f"{q(f'nó có {G['d']}{PE} có {G['m']}{PE} có {G['l']}{PE} có {G['o']}{PE} có {G['h']}')} {NO_PE}",
        obj_frame(T6))
    L17 = f"{PE} ".join([f"{ADOSO} có {GR}", AMOHO, SADDHA, VIRIYA, SATI, SAMADHI, PANNA, LOBHO, DOSO, MOHO, MANO,
                         DITTHI, VICI, THINA, UDDH, AHIR, f"{ANOT} có {GR}"])
    L2_ = f"{ADOSO} có {GR}{PE} {ANOT} có {GR}"
    add("5-758",
        f"{Q(ob(f'{ALOBHO} có {GR}'))} {YES} {Q(ob(T6))} {NO_PE} {q(ob(L17))} {YES} {Q(ob(T6))} {NO_PE}",
        f"{Q(ob(T6, True))} {YES} {Q(ob(f'{ALOBHO} có {GR}', True))} {NO_PE} {q(ob(T6, True))} {YES} "
        f"{Q(ob(L2_, True))} {NO_PE}")
    add("5-759",
        f"{S.na_vattabbam(T6)} {YES} {NANU(f'{RUPA} có điều kiện')} {YES} {S.hanci(f'{RUPA} có điều kiện', T6)}",
        S.katha_end(KATHA[6]))

    # ---- (162) 7. Rūpaṃ kusalākusalantikathā --------------------------------------------------------------------
    sub(7, 162)
    add("5-760", obj_frame(T7K))
    K7 = f"{ADOSO} là thiện{PE} {AMOHO} là thiện{PE} {SADDHA}{PE} {VIRIYA}{PE} {SATI}{PE} {SAMADHI}{PE} {PANNA} là thiện"
    add("5-761",
        f"{Q(ob(f'{ALOBHO} là thiện'))} {YES} {Q(ob(T7K))} {NO_PE}",
        f"{Q(ob(K7))} {YES} {Q(ob(T7K))} {NO_PE}",
        f"{Q(ob(T7K, True))} {YES} {Q(ob(f'{ALOBHO} là thiện', True))} {NO_PE}",
        f"{Q(ob(T7K, True))} {YES} {Q(ob(f'{ADOSO} là thiện{PE} {PANNA} là thiện', True))} {NO_PE}")
    add("5-762", obj_frame(T7A, PE))
    A7 = f"{DOSO}{PE} {MOHO}{PE} {MANO}{PE} {ANOT} là bất thiện"
    A7N = f"{DOSO}{PE} {MOHO}{PE} {ANOT} là bất thiện"
    add("5-763",
        f"{Q(ob(f'{LOBHO} là bất thiện'))} {YES} {Q(ob(T7A))} {NO_PE} {q(ob(A7))} {YES} {Q(ob(T7A))} {NO_PE}",
        f"{Q(ob(T7A, True))} {YES} {Q(ob(f'{LOBHO} là bất thiện', True))} {NO_PE} {q(ob(T7A, True))} {YES} "
        f"{Q(ob(A7N, True))} {NO_PE}")
    KV2 = "nghiệp bằng thân, nghiệp bằng lời nói vừa là thiện vừa là bất thiện"   # kāyakammaṃ vacīkammaṃ … (ch16)
    add("5-764",
        f"{S.na_vattabbam(RK)} {YES} {NANU(KV2)} {YES} {S.hanci(KV2, RK)}",
        S.katha_end(KATHA[7]))

    # ---- (163) 8. Rūpaṃ vipākotikathā ---------------------------------------------------------------------------
    sub(8, 163)
    P765 = ", ".join(VED3 + SAMP3) + f", gắn liền với {PH}{PE} gắn liền với tâm, có đối tượng"
    NIF = f"nó {NEG_SH}, {NHAS}"
    add("5-765",
        f"{Q(T8)} {YES} {Q(f'{RUPA} {P765}, {HAS}')} {NO_PE} {nanu_l(NIF)} {YES} {S.hanci_neg(NIF, T8)}")
    add("5-766",
        f"{Q(pos(PH, POS_SH))} {YES} {Q(pos(RUPA, POS_SH))} {NO_PE}",
        f"{Q(neg(RUPA, NEG_SH))} {YES} {Q(neg(PH, NEG_SH))} {NO_PE}")
    add("5-767",
        f"{S.na_vattabbam(T8)} {YES} {NANU(isvip(CC))} {YES} {S.hanci(isvip(CC), isvip(f'{RUPA} {KATATTA}'))}",
        S.katha_end(KATHA[8]))

    # ---- (164) 9. Rūpaṃ rūpāvacarārūpāvacarantikathā ------------------------------------------------------------
    sub(9, 164)
    N1 = f"nó {esi(True)}, {short(1)}"                                  # na … , na samāpattesiyena cittena…pe… ekārammaṇaṃ
    N2 = f"nó không {S3[0]}, không {S3[1]}{PE} {', '.join(C8[-2:])}"      # na … na upapattesiyaṃ…pe… ekavatthukaṃ ekārammaṇaṃ
    add("5-768", f"{Q(T9R)} {YES} {Q(full())} {NO_PE} {nanu_l(full(True))} {YES} {S.hanci_neg(N1, T9R)}")
    add("5-769", f"{Q(T9A)} {YES} {Q(full())} {NO_PE} {nanu_l(N1)} {YES} {S.hanci_neg(N2, T9A)}")
    KR = f"do nghiệp {KA} đã được tạo, {RUPA} {KA}"                       # kāmāvacarakammassa katattā rūpaṃ kāmāvacaraṃ
    RRA = f"do nghiệp {RA} đã được tạo, {RUPA} {RA}, do nghiệp {AA} đã được tạo, {RUPA} {AA}"
    add("5-770",
        f"{S.na_vattabbam(f'{T9R}, {T9A}')} {YES} {NANU(KR)} {YES} {S.hanci(KR, RRA)}",
        S.katha_end(KATHA[9]))

    # ---- (165) 10. Rūpārūpadhātupariyāpannakathā ----------------------------------------------------------------
    sub(10, 165)
    N3 = f"nó {esi(True)}, {short(2)}"                                  # na … , na samāpattesiyena cittena…pe… ekavatthuko ekārammaṇo
    add("5-771", f"{Q(RR)} {YES} {Q(full())} {NO_PE} {nanu_l(N3)} {YES} {S.hanci_neg(N3, RR)}")
    SR = f"{RAGA['sadda']} {NT} {YT['sadda']}"
    GRP = f"{RAGA['gandha']}{PE} {RAGA['rasa']}{PE} {RAGA['phoṭṭhabba']} {NT} {YT['phoṭṭhabba']}"
    NVS = nv_dhatu("sadda", YT["sadda"])
    NVG = (f"đối với {RAGA['gandha']}{PE} {RAGA['rasa']}{PE} {RAGA['phoṭṭhabba']}, không nên nói – "
           f"“{NT} {YT['phoṭṭhabba']}”")

    def lines_sense(main, key, dh):
        nv = nv_dhatu(key, dh)
        return (f"{Q(main)} {YES} {Q(SR)} {NO_PE} {q(main)} {YES} {Q(GRP)} {NO_PE}",
                f"{Q(NVS)} {YES} {Q(nv)} {NO_PE} {q(NVG)} {YES} {Q(nv)} {NO_PE}")
    add("5-772", *lines_sense(RR, "rūpa", RDH))
    NVA = nv_dhatu("arūpa", ARDH)
    add("5-773",
        f"{Q(ARR)} {YES} {Q(NVA)} {NO_PE} {q(ARR)} {YES} {Q(full())} {NO_PE} {nanu_l(N3)} {YES} "
        f"{S.hanci_neg(full(True), ARR)}")
    add("5-774", *lines_sense(ARR, "arūpa", ARDH))
    BOTH = f"{RR}, {ARR}"
    add("5-775",
        f"{S.na_vattabbam(BOTH)} {YES} {NANU(KRR)} {YES} {S.hanci(KRR, BOTH)}",
        S.katha_end(KATHA10B),
        S.katha_end(KATHA[10]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# Helper: look up identical Pāli in the finished pi-5 rails chapters (named files only)
# ---------------------------------------------------------------------------------------------------------------
def _lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def find(pat, maxhits=8, maxc=700):
    pat = re.compile(pat)
    hits = 0
    for name in DONE:
        pl, vl = _lines(S.PALI_DIR / name), _lines(S.OUT_DIR / name)
        for i, ln in enumerate(pl):
            m = pat.search(ln)
            if not m:
                continue
            s = max(0, m.start() - 150)
            print(f"[{name} line {i + 1}]")
            print("  PI:", ln[s:s + 400])
            print("  VI:", (vl[i] if i < len(vl) else "<missing>")[:maxc])
            hits += 1
            if hits >= maxhits:
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
    adh = S.FORMULAS_MD.parent / "adh-24"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--find"]:
        find(sys.argv[2], *(int(x) for x in sys.argv[3:5]))
    else:
        main()
