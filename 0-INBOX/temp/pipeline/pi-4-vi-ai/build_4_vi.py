# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 4: 4-tikapuggalapannatti.md (Tikapuggalapaññatti).

Imports the approved sample builder (names, frames, headings, closers) and uses fixed strings for every repeated
frame, list and simile, so every repeat is byte-identical.  run:  python -I -X utf8 build_4_vi.py
Asserts: every cross-book string still occurs in the pi-1 / pi-2 / pi-3 rails; every person name used equals
B.NAME (or the matrix item it comes from in 1-matika.md); the names appear in the output.
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402

N = B.NAME
cap, q, close, close_pl = B.cap, B.q, B.close, B.close_pl
IDHE = B.IDHEKACCO                       # Ở đời này, có người
IDHE_LC = IDHE[:1].lower() + IDHE[1:]    # after «cũng như thế,»
IDHA_PANA = "Ở đời này, lại có"          # Idha panekacco
TATRA = "Trong số đó,"                   # Tatra yvāyaṃ …
SEYYATHA = "Giống như"                   # Seyyathāpi (nāma) … (pi-2)
EVAMEVAM = "cũng như thế,"              # evamevaṃ (pi-2 «cũng như thế»)
KISSA = "Vì sao vậy?"                    # Taṃ kissa hetu? (pi-2)
TASMA = "Vì vậy,"                        # Tasmā
TYPES3 = B.TYPES_COUNT[3]                # Ba hạng người
KATAME_TAYO = "Ba hạng nào?"             # Katame tayo?


def tattha_who(x):                       # Tattha katame tayo X? (persons: «là những ai?», pi-2 «… là những ai?»)
    return f"Ở đây, {x} là những ai?"


SANTO_LOKE = "đang có mặt, được tìm thấy trong thế gian"        # santo saṃvijjamānā lokasmiṃ
SANTO_BHIKKHU = "đang có mặt, được tìm thấy giữa các tỳ-khưu"   # santo saṃvijjamānā bhikkhūsu

# ---------------------------------------------------------------- arahant formula (pi-2 ^ñāṇavibhaṅga (10))
ARAHATTA = ("nhờ sự diệt tận các ô nhiễm, ngay trong đời này tự mình hiểu biết trực tiếp, chứng nghiệm, "
            "chứng nhập và an trú sự giải thoát của tâm, sự giải thoát nhờ trí tuệ, không còn ô nhiễm")
ARAHANT_SENT = f"{IDHE}, {ARAHATTA}"                         # Idhekacco puggalo āsavānaṃ khayā … viharati
SUNATI = f"Người ấy nghe người ta nói – “Vị tỳ-khưu có tên như thế này, {ARAHATTA}”."   # So suṇāti – "itthannāmo kira …"
THINKS_NOT = f"Người ấy không nghĩ như vầy – “Không biết đến bao giờ tôi cũng sẽ, {ARAHATTA}?”"  # kudāssu nāmāhampi …
THINKS = f"Người ấy nghĩ như vầy – “Không biết đến bao giờ tôi cũng sẽ, {ARAHATTA}?”"

# ---------------------------------------------------------------- moral strings
DUSSILA = ("phạm giới, có phẩm chất xấu, không trong sạch, có hành vi đáng ngờ, che giấu việc làm của mình, "
           "không phải sa-môn mà tự xưng là sa-môn, không sống đời sống tu hành trong sạch mà tự xưng là sống "
           "đời sống tu hành trong sạch, mục nát bên trong, rỉ chảy dục vọng, như rác rưởi")
SILAVA = "giữ giới, có phẩm chất tốt"     # sīlavā (hoti) kalyāṇadhammo

# ---------------------------------------------------------------- serviceable / not
SEV = "đáng gần gũi, đáng kết giao, đáng thân cận"                       # sevitabbo bhajitabbo payirupāsitabbo
NSEV = "không đáng gần gũi, không đáng kết giao, không đáng thân cận"    # na sevitabbo …
SAKKATVA = "với lòng tôn kính và trân trọng"                            # sakkatvā garuṃ katvā
JIGUCCHA = "đáng ghê tránh"                                             # jigucchitabbo
AJJHUPEKKHA = "đáng được nhìn với sự bình thản"                         # ajjhupekkhitabbo
EVARUPO = "Người như vậy"                                               # Evarūpo puggalo

# ---------------------------------------------------------------- anger (kodhano hoti upāyāsabahulo …)
def kodha(var=""):
    return ("giận dữ, dễ bực tức, dù chỉ bị nói một chút cũng nổi cáu, nổi giận, khởi thù hằn, trở nên cố chấp"
            f"{var}, để lộ sự nổi nóng, sự sân hận và sự bất mãn")


STRUCK = "khi bị que gỗ hoặc mảnh sành{v} chạm vào"                    # kaṭṭhena vā kaṭhalāya vā ghaṭṭito


def aru(v1="", v2=""):
    return (f"{SEYYATHA} một vết thương lở loét, {STRUCK.format(v=v1)}, lại càng chảy mủ nhiều hơn nữa{v2}, "
            f"{EVAMEVAM} {IDHE_LC} {kodha()}")


TINDUKA = (f"{SEYYATHA} một khúc củi cây thị đang cháy, {STRUCK.format(v='')}, lại càng kêu xèo xèo, nổ lách tách "
           f"nhiều hơn nữa, {EVAMEVAM} {IDHE_LC} {kodha()}")
GUTHAKUPA = (f"{SEYYATHA} một hố phân, {STRUCK.format(v='')}, lại càng bốc mùi hôi thối nhiều hơn nữa, "
             f"{EVAMEVAM} {IDHE_LC} {kodha()}")

# ---------------------------------------------------------------- four truths (sample constants)
SACCA = B.SACCA_PAJANATI                  # ends «…khổ đau”.»
SACCA_NP = SACCA[:-1]
TATHAGATA_NP = B.TATHAGATA_DHAMMA[:-1]

# ---------------------------------------------------------------- eyes
EYE_WEALTH = ("loại con mắt mà nhờ con mắt ấy có thể đạt được tài sản chưa đạt được, hoặc làm tăng trưởng tài "
              "sản đã đạt được")
EYE_DHAMMA = ("loại con mắt mà nhờ con mắt ấy có thể biết các hiện tượng thiện và bất thiện, biết các hiện tượng "
              "có lỗi và không có lỗi, biết các hiện tượng thấp kém và ưu việt, biết các hiện tượng đen tối và "
              "trong sáng cùng với những gì đối lập với chúng")

# ---------------------------------------------------------------- listening to the Teaching
def arama(v1="", v2="", lc=False):
    s = f"{IDHE_LC if lc else IDHE} thường xuyên đến tu viện{v1} để nghe Giáo Pháp{v2} nơi các tỳ-khưu."
    return s


DESANA = ("Các tỳ-khưu thuyết giảng cho người ấy Giáo Pháp tốt đẹp ở phần đầu, tốt đẹp ở phần giữa, tốt đẹp ở "
          "phần cuối, đúng ý nghĩa và đúng văn từ, làm sáng tỏ đời sống tu hành trong sạch hoàn toàn đầy đủ, hoàn "
          "toàn thanh tịnh.")
_NEG = ("không chú tâm đến phần đầu của bài giảng ấy, không chú tâm đến phần giữa, "
        "không chú tâm đến phần cuối")
_POS = ("chú tâm đến cả phần đầu của bài giảng ấy, chú tâm đến cả phần giữa, "
        "chú tâm đến cả phần cuối")
_NEG_PI = ("không chú tâm đến cả phần đầu của bài giảng ấy, không chú tâm đến cả phần giữa, "
           "không chú tâm đến cả phần cuối")                               # neva ādimpi … (^4-108, as written)
SEATED_NEG = f"Ngồi ở chỗ ngồi ấy, người ấy {_NEG}."                      # So tasmiṃ āsane nisinno … neva ādiṃ …
SEATED_POS = f"Ngồi ở chỗ ngồi ấy, người ấy {_POS}."                      # … ādimpi …
RISEN_NEG = f"Ngay cả khi đã đứng dậy khỏi chỗ ngồi ấy, người ấy cũng {_NEG}."   # Vuṭṭhitopi … neva ādiṃ …
RISEN_POS = f"Ngay cả khi đã đứng dậy khỏi chỗ ngồi ấy, người ấy cũng {_POS}."   # Vuṭṭhitopi … ādimpi …
RISEN_BUT_NEG = f"Nhưng khi đã đứng dậy khỏi chỗ ngồi ấy, người ấy {_NEG}."       # Vuṭṭhito ca kho … neva ādiṃ …
RISEN_BUT_NEG_PI = f"Nhưng khi đã đứng dậy khỏi chỗ ngồi ấy, người ấy {_NEG_PI}."  # … neva ādimpi … (^4-108 end)

# ---------------------------------------------------------------- anger lines (lekhā)
KUJJHATI = f"{IDHE} thường hay nổi giận."                                 # Idhekacco puggalo abhiṇhaṃ kujjhati.
KUJJHATI_LC = f"{IDHE_LC} thường hay nổi giận."
ANUSETI = "Và sự giận dữ ấy của người ấy nằm sẵn trong lòng lâu dài, suốt một thời gian dài."
NA_ANUSETI = "Và sự giận dữ ấy của người ấy không nằm sẵn trong lòng lâu dài, suốt một thời gian dài."
UDAKA_SPOKEN = "dù bị nói lời gay gắt, dù bị nói lời thô ác, dù bị nói lời không dễ ưa"

# ---------------------------------------------------------------- cloth similes
CIVARA = "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh"   # pi-2 ^2-929
SEVANTI = "Những ai gần gũi, kết giao, thân cận người ấy và noi theo gương người ấy"
NAVO, MAJJHIMO, THERO = "dù mới tu", "dù ở bậc trung", "dù là trưởng lão"
EVARUPO_THERO = "Giả sử một tỳ-khưu trưởng lão như vậy lên tiếng giữa Tăng đoàn"
TAMENAM = "đối với vị ấy, các tỳ-khưu nói như vầy –"                   # tamenaṃ bhikkhū evamāhaṃsu –
BALASSA = "Lời nói của ông, kẻ ngu dốt, thiếu hiểu biết, thì có ích gì"  # pi-2 ^ purisadosa (b)


def cloth_triplet(cloth, pot):
    """pot = (quality words) e.g. «xấu xí, khi tiếp xúc thì khó chịu và ít giá trị»."""
    return "; ".join(f"{cloth} {age} cũng {pot}" for age in ("dù còn mới", "dù đã dùng một thời gian", "dù đã cũ"))


def potthaka_monk(age):
    return (f"Nếu một tỳ-khưu {age} mà phạm giới, có phẩm chất xấu, thì đó là sự xấu xí của người ấy. "
            "Như tấm vải gai thô ấy xấu xí, người này cũng giống như thế. "
            f"{SEVANTI}, thì điều đó đem lại cho họ sự bất lợi và khổ đau trong một thời gian dài. "
            "Đó là sự khó chịu khi tiếp xúc của người ấy. "
            "Như tấm vải gai thô ấy khi tiếp xúc thì khó chịu, người này cũng giống như thế. "
            f"Người ấy nhận {CIVARA} từ những ai, thì điều đó không đem lại cho họ quả lớn, "
            "không đem lại lợi ích lớn. Đó là sự ít giá trị của người ấy. "
            "Như tấm vải gai thô ấy ít giá trị, người này cũng giống như thế.")


def kasika_monk(age, v1="", v2=""):
    return (f"Nếu một tỳ-khưu {age} mà giữ giới, có phẩm chất tốt, thì đó là sự đẹp đẽ của người ấy. "
            "Như tấm vải xứ Ca-thi ấy đẹp, người này cũng giống như thế. "
            f"{SEVANTI}, thì điều đó đem lại cho họ sự lợi ích và hạnh phúc trong một thời gian dài. "
            "Đó là sự dễ chịu khi tiếp xúc của người ấy. "
            "Như tấm vải xứ Ca-thi ấy khi tiếp xúc thì dễ chịu, người này cũng giống như thế. "
            f"Người ấy{v1} nhận{v2} {CIVARA} từ những ai, thì điều đó đem lại cho họ quả lớn, lợi ích lớn. "
            "Đó là sự có giá trị lớn của người ấy. "
            "Như tấm vải xứ Ca-thi ấy có giá trị lớn, người này cũng giống như thế.")


# ---------------------------------------------------------------- sick-person simile
GIL_ANY = ("dù nhận được thức ăn thích hợp hay không nhận được thức ăn thích hợp, dù nhận được thuốc men thích "
           "hợp hay không nhận được thuốc men thích hợp, dù nhận được người chăm sóc phù hợp hay không nhận được "
           "người chăm sóc phù hợp")
GIL_ONLY = ("khi nhận được thức ăn thích hợp chứ không phải khi không nhận được, khi nhận được thuốc men thích hợp "
            "chứ không phải khi không nhận được, khi nhận được người chăm sóc phù hợp chứ không phải khi không "
            "nhận được")
TG_ANY = ("dù có dịp gặp Như Lai hay không có dịp gặp Như Lai, dù có dịp nghe Giáo Pháp và Giới Luật do Như Lai "
          "tuyên bố hay không có dịp nghe Giáo Pháp và Giới Luật do Như Lai tuyên bố")
TG_ONLY = ("khi có dịp gặp Như Lai chứ không phải khi không có dịp, khi có dịp nghe Giáo Pháp và Giới Luật do "
           "Như Lai tuyên bố chứ không phải khi không có dịp")
OKKAMATI = "bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện"   # okkamati niyāmaṃ … (pi-2 NIYAMA)

# ---------------------------------------------------------------- teachers
PARINNA = "đề ra sự hiểu biết trọn vẹn về các {x}"                         # X-ānaṃ pariññaṃ paññapeti
ATTA = "tự ngã như là sự thật, như là điều chắc chắn"                      # attānaṃ saccato thetato (pi-2)
DATTHABBO = "thì cần hiểu bậc đạo sư ấy là {x}"                            # X satthā tena daṭṭhabbo

# ---------------------------------------------------------------- matrix-derived names (1-matika.md, tika)
MATIKA = (B.OUT_DIR / "1-matika.md").read_text(encoding="utf-8")
M8 = ("Có người chưa lìa tham đắm đối với các dục lạc và các sự hiện hữu, có người đã lìa tham đắm đối với các "
      "dục lạc nhưng chưa lìa tham đắm đối với các sự hiện hữu, có người đã lìa tham đắm đối với cả các dục lạc "
      "và các sự hiện hữu.")
KAMA = [p for p in M8[len("Có người "):-1].split(", có người ")]
KAMA_NAME = ["người " + p for p in KAMA]
M15 = ("Có người thực hành trọn vẹn các giới hạnh, thực hành định tâm ở mức độ nhất định, thực hành trí tuệ ở "
       "mức độ nhất định; có người thực hành trọn vẹn các giới hạnh, thực hành trọn vẹn định tâm, thực hành trí "
       "tuệ ở mức độ nhất định; có người thực hành trọn vẹn các giới hạnh, thực hành trọn vẹn định tâm và thực "
       "hành trọn vẹn trí tuệ.")
SIKKHA = [p for p in M15[len("Có người "):-1].split("; có người ")]
SIKKHA_NAME = ["người " + p for p in SIKKHA]
MATRIX_CHECK = [
    "(8) " + M8,
    f"(13) Có người {NSEV}, có người {SEV}, có người {SEV} {SAKKATVA}",
    f"(14) Có người {JIGUCCHA}, {NSEV}, có người {AJJHUPEKKHA}, {NSEV}; có người {SEV}.",
    "(15) Có người thực hành trọn vẹn các giới hạnh [khác chính tả (Syā.): paripūrīkārī], thực hành định tâm ở "
    "mức độ nhất định, thực hành trí tuệ ở mức độ nhất định; có người thực hành trọn vẹn các giới hạnh, thực hành "
    "trọn vẹn định tâm, thực hành trí tuệ ở mức độ nhất định; có người thực hành trọn vẹn các giới hạnh, thực hành "
    "trọn vẹn định tâm và thực hành trọn vẹn trí tuệ.",
    "(16) Ba bậc đạo sư.", "(17) Lại có ba bậc đạo sư khác.",
]
SOTA_SAKA = f"Các {N['sotāpanno']} và các {N['sakadāgāmī']}"          # Sotāpannasakadāgāmino

# ---------------------------------------------------------------- cross-book strings (asserted)
CROSS = [
    (2, ARAHATTA.replace("nhờ sự diệt tận các ô nhiễm, ", "")), (2, "nhờ sự diệt tận các ô nhiễm"),
    (2, "Vì sao vậy?"), (2, "Giống như"), (2, "cũng như thế,"), (2, "nghĩ như vầy –"),
    (2, "đời sống tu hành trong sạch"), (1, "phạm giới"), (2, "người giữ giới"), (1, "sa-môn"),
    (1, "không có lỗi, dễ chịu với tai, dễ mến, thấm vào lòng, lịch sự, được nhiều người yêu mến, "
        "được nhiều người ưa thích"),
    (2, "để lộ sự nổi nóng, sự sân hận và sự bất mãn"), (1, "sự thù hằn"),
    (1, "Các hiện tượng thấp kém"), (1, "Các hiện tượng ưu việt"), (1, "Các hiện tượng đen tối"),
    (1, "Các hiện tượng trong sáng"), (1, "các hiện tượng thiện và bất thiện"),
    (2, "Giáo Pháp và Giới Luật"), (2, OKKAMATI), (2, "Đức Thế Tôn"), (2, "Như Lai"),
    (2, "chú tâm đến"), (2, "nằm sẵn"), (1, "thô ác"), (1, "không dễ ưa"),
    (1, "khi tiếp xúc thì dễ chịu"), (1, "khi tiếp xúc thì khó chịu"), (2, CIVARA), (2, "gần gũi, kết giao, thân cận"),
    (2, BALASSA), (2, "Tăng đoàn"), (2, "Này các tôn giả"), (2, "không xao động"), (2, "sự nhẹ dạ"),
    (2, "mất tỉnh thức"), (1, "thiếu hiểu biết rõ ràng"), (2, "không được định tâm"), (2, "được định tâm"),
    (2, "người có sự tỉnh thức được thiết lập"), (2, "thu thúc"), (1, "lòng thương mến"), (1, "lòng thương xót"),
    (1, "sự kết bạn với người xấu"), (1, "sự kết bạn với người tốt"), (1, "sự nghiêng về phía họ"),
    (2, "hay mắng nhiếc và lăng mạ"), (2, "lìa tham đắm đối với các dục lạc"),
    (2, "thành tựu thiền thuộc cõi hình sắc và cõi không hình sắc"), (2, "hiểu biết trọn vẹn"),
    (1, "cảm giác"), (2, ATTA[len("tự ngã "):]), (2, "tự ngã"), (2, "học thuyết về sự trường tồn"),
    (2, "học thuyết về sự đoạn diệt"), (2, "Trung Bộ Kinh"), (2, "Tăng Chi Bộ Kinh"), (2, "(mọi bản)"),
    (2, "Tự Giác Ngộ Hoàn Toàn"), (1, "thế gian"), (2, "tỳ-khưu"),
]


# ---------------------------------------------------------------- chapter
def chapter():
    L = ["#### " + B.CHAPTER_HEADING[4]]

    # ^4-91 … ^4-93
    L.append(f"{q(N['nirāso'])} {IDHE} {DUSSILA}. {SUNATI} {THINKS_NOT} {close(N['nirāso'], dash=False)}")
    L.append(f"{q(N['āsaṃso'])} {IDHE} {SILAVA}. {SUNATI} {THINKS} {close(N['āsaṃso'], dash=False)}")
    L.append(f"{q(N['vigatāso'])} {ARAHANT_SENT}. {SUNATI} {THINKS_NOT} {KISSA} Vì niềm mong cầu giải thoát mà "
             "trước đây người ấy có, khi chưa được giải thoát, nay đã lắng xuống. "
             f"{close(N['vigatāso'], dash=False)}")

    # ^4-94 sick persons (8 lines)
    gil = f"{TYPES3} giống như {B.SIMILE['gilāna']}"
    gil_lc = gil[:1].lower() + gil[1:]
    L.append(f"{tattha_who(gil_lc)} Ba người bệnh – {IDHE_LC} bệnh, {GIL_ANY}, vẫn không khỏi bệnh ấy. (1)")
    L.append(f"{IDHA_PANA} người bệnh, {GIL_ANY}, vẫn khỏi bệnh ấy. (2)")
    L.append(f"{IDHA_PANA} người bệnh, {GIL_ONLY}, thì khỏi bệnh ấy. (3)")
    L.append(f"{TATRA} người bệnh nào {GIL_ONLY}, thì khỏi bệnh ấy, chính vì người bệnh này mà Đức Thế Tôn đã cho "
             "phép thức ăn dành cho người bệnh, đã cho phép thuốc men dành cho người bệnh, đã cho phép người chăm "
             "sóc người bệnh. Và cũng vì người bệnh này mà những người bệnh khác cũng cần được chăm sóc.")
    L.append(f"{cap(EVAMEVAM[:-1])} [khác chính tả (Sī.): evameva], {gil_lc} {SANTO_LOKE}. {KATAME_TAYO} "
             f"{IDHE}, {TG_ANY}, vẫn không {OKKAMATI}. (1)")
    L.append(f"{IDHA_PANA} người, {TG_ANY}, vẫn {OKKAMATI}. (2)")
    L.append(f"{IDHA_PANA} người, {TG_ONLY}, thì {OKKAMATI}. (3)")
    L.append(f"{TATRA} người nào {TG_ONLY}, thì {OKKAMATI}, chính vì người này mà Đức Thế Tôn đã cho phép việc "
             "thuyết giảng Giáo Pháp, và cũng vì người này mà Giáo Pháp cần được thuyết giảng cho cả những người "
             f"khác. Đây là {gil_lc} {SANTO_LOKE}.")

    # ^4-95 … ^4-97
    L.append(f"{q(N['kāyasakkhī'])} {IDHE} {B.VIMOKKHA}, {B.PANNAYA_SOME} {close(N['kāyasakkhī'])}")
    L.append(f"{q(N['diṭṭhippatto'])} {IDHE} {SACCA_NP}, {TATHAGATA_NP}, {B.PANNAYA_SOME} "
             f"{close(N['diṭṭhippatto'])}")
    L.append(f"{q(N['saddhāvimutto'])} {IDHE} hiểu rõ đúng như thật: “Đây là khổ đau”… {TATHAGATA_NP}, "
             f"{B.PANNAYA_SOME}, nhưng không được như ở {N['diṭṭhippatto']} {close(N['saddhāvimutto'])}")

    # ^4-98 … ^4-100 speech
    places = ("khi đến hội đồng, hoặc đến hội chúng, hoặc đến giữa họ hàng, hoặc đến giữa phường hội, hoặc đến "
              "giữa hoàng tộc, được đưa ra làm chứng và được hỏi như sau")
    come = "“Này ông, hãy đến đây{v}, hãy nói điều ông biết”"
    L.append(f"{q(N['gūthabhāṇī'])} {IDHE} nói dối, {places} – "
             + come.format(v=" [dị bản (Syā., Ka.): ehi bho; Trung Bộ Kinh 1.440; Tăng Chi Bộ Kinh 3.28]")
             + ", thì người ấy, không biết lại nói – “Tôi biết”, biết lại nói – “Tôi không biết”, không thấy lại "
             "nói – “Tôi thấy”, thấy lại nói – “Tôi không thấy”. Như vậy, vì lợi ích của bản thân, hoặc vì lợi ích "
             "của người khác, hoặc vì một chút lợi lộc vật chất, người ấy cố ý nói dối "
             + close(N['gūthabhāṇī']))
    L.append(f"{q(N['pupphabhāṇī'])} {IDHE} từ bỏ việc nói dối, kiêng tránh việc nói dối, {places} – "
             + come.format(v="")
             + ", thì người ấy, không biết thì nói – “Tôi không biết”, biết thì nói – “Tôi biết”, không thấy thì "
             "nói – “Tôi không thấy”, thấy thì nói – “Tôi thấy”. Như vậy, dù vì lợi ích của bản thân, hoặc vì lợi "
             "ích của người khác, hoặc vì một chút lợi lộc vật chất, người ấy cũng không cố ý nói dối "
             + close(N['pupphabhāṇī']))
    L.append(f"{q(N['madhubhāṇī'])} {IDHE}, lời nói nào không có lỗi, dễ chịu với tai, dễ mến, thấm vào lòng, lịch "
             "sự, được nhiều người yêu mến, được nhiều người ưa thích, thì nói loại lời như vậy "
             + close(N['madhubhāṇī']))

    # ^4-101 … ^4-103 minds
    L.append(f"{q(N['arukūpamacitto'])} {IDHE} "
             + kodha(" [khác chính tả (Syā., Ka.): patiṭṭhīyati; Tăng Chi Bộ Kinh 3.25]") + ". "
             + aru(" [khác chính tả (Ka.): kathalāya; dị bản (Chú giải): kathalena; Tăng Chi Bộ Kinh 3.25]",
                   " [dị bản (Sī.): assavanoti]")
             + " " + close(N['arukūpamacitto']))
    L.append(f"{q(N['vijjūpamacitto'])} {IDHE} {SACCA} {SEYYATHA} một người có mắt, trong bóng tối dày đặc của "
             "đêm đen, có thể thấy các hình sắc nhờ một tia chớp lóe lên, "
             f"{EVAMEVAM} {IDHE_LC} {SACCA_NP} {close(N['vijjūpamacitto'])}")
    L.append(f"{q(N['vajirūpamacitto'])} {ARAHANT_SENT}. {SEYYATHA} đối với kim cương, không có gì mà nó không "
             f"thể cắt đứt, dù là ngọc hay đá, {EVAMEVAM} {IDHE_LC}, {ARAHATTA} {close(N['vajirūpamacitto'])}")

    # ^4-104 … ^4-106 eyes
    L.append(f"{q(N['andho'])} {IDHE} không có {EYE_WEALTH}; còn {EYE_DHAMMA}, thì người ấy không có "
             + close(N['andho']))
    L.append(f"{q(N['ekacakkhu'])} {IDHE} có {EYE_WEALTH}; còn {EYE_DHAMMA}, thì người ấy không có "
             + close(N['ekacakkhu']))
    L.append(f"{q(N['dvicakkhu'])} {IDHE} có {EYE_WEALTH}; còn {EYE_DHAMMA}, thì người ấy cũng có "
             + close(N['dvicakkhu']))

    # ^4-107 … ^4-109 wisdom
    L.append(f"{q(N['avakujjapañño'])} "
             + arama(" [dị bản (Sī.): gato; dị bản (Syā.): gantvā]", " [khác chính tả (Syā.): dhammassavanāya]")
             + f" {DESANA} {SEATED_NEG} {RISEN_NEG} {SEYYATHA} một cái chum bị úp ngược "
             "[khác chính tả (Syā.): nikujjo; Tăng Chi Bộ Kinh 3.30], nước đổ vào đó thì chảy tràn đi, không đọng "
             f"lại; {EVAMEVAM} {arama(lc=True)} {DESANA} {SEATED_NEG} {RISEN_NEG[:-1]} "
             + close(N['avakujjapañño']))
    L.append(f"{q(N['ucchaṅgapañño'])} {arama()} {DESANA} {SEATED_POS} {RISEN_BUT_NEG} {SEYYATHA} trong vạt áo của "
             "một người có đựng nhiều loại đồ ăn khác nhau – mè, gạo [khác chính tả (Ka.): tilataṇḍulā; Tăng Chi Bộ "
             "Kinh 3.30], bánh ngọt, táo ta. Khi đứng dậy khỏi chỗ ngồi ấy, vì mất tỉnh thức, người ấy có thể làm "
             f"chúng rơi vãi. {cap(EVAMEVAM)} {arama(lc=True)} {DESANA} {SEATED_POS} {RISEN_BUT_NEG_PI[:-1]} "
             + close(N['ucchaṅgapañño']))
    L.append(f"{q(N['puthupañño'])} {arama()} {DESANA} {SEATED_POS} {RISEN_POS} {SEYYATHA} một cái chum được đặt "
             "ngửa, nước đổ vào đó thì đọng lại, không chảy tràn đi; "
             f"{EVAMEVAM} {arama(lc=True)} {DESANA} {SEATED_POS} {RISEN_POS[:-1]} " + close(N['puthupañño']))

    # ^4-110 … ^4-112 passion
    L.append(f"{q(KAMA_NAME[0])} {SOTA_SAKA} {close_pl('những ' + KAMA_NAME[0])}")
    L.append(f"{q(KAMA_NAME[1])} {cap(N['anāgāmī'])} {close(KAMA_NAME[1])}")
    L.append(f"{q(KAMA_NAME[2])} {cap(N['arahā'])} {close(KAMA_NAME[2])}")

    # ^4-113 … ^4-115 lines
    L.append(f"{q(N['pāsāṇalekhūpamo'])} {KUJJHATI} {ANUSETI} {SEYYATHA} đường vạch trên đá không mau bị xóa mờ "
             "bởi gió hay bởi nước, mà tồn tại lâu dài; "
             f"{EVAMEVAM} {KUJJHATI_LC} {ANUSETI[:-1]} {close(N['pāsāṇalekhūpamo'])}")
    L.append(f"{q(N['pathavilekhūpamo'])} {KUJJHATI} {NA_ANUSETI} {SEYYATHA} đường vạch trên đất "
             "[khác chính tả (Sī., Syā.): paṭhaviyā] mau bị xóa mờ bởi gió hay bởi nước, không tồn tại lâu dài; "
             f"{EVAMEVAM} {KUJJHATI_LC} {NA_ANUSETI[:-1]} {close(N['pathavilekhūpamo'])}")
    v = " [dị bản (Syā.): … ceva; Tăng Chi Bộ Kinh 3.133]"
    L.append(f"{q(N['udakalekhūpamo'])} {IDHE} {UDAKA_SPOKEN}, vẫn hòa hợp{v}, vẫn gắn bó{v}, vẫn thân thiện{v}. "
             f"{SEYYATHA} đường vạch trên nước mau bị xóa mờ, không tồn tại lâu dài; "
             f"{EVAMEVAM} {IDHE_LC} {UDAKA_SPOKEN}, vẫn hòa hợp, vẫn gắn bó, vẫn thân thiện "
             + close(N['udakalekhūpamo']))

    # ^4-116 coarse cloth (3 lines)
    pot = f"{TYPES3} giống như {B.SIMILE['potthaka']}"
    pot_lc = pot[:1].lower() + pot[1:]
    L.append(f"{tattha_who(pot_lc)} Ba loại vải gai thô – "
             + cloth_triplet("vải gai thô", "xấu xí, khi tiếp xúc thì khó chịu và ít giá trị")
             + ". Ngay cả vải gai thô đã cũ, người ta cũng dùng làm giẻ lau nồi, hoặc vứt nó lên đống rác. "
             f"{cap(EVAMEVAM)} {pot_lc} này {SANTO_BHIKKHU}. {KATAME_TAYO} {potthaka_monk(NAVO)}")
    L.append(f"Nếu một tỳ-khưu {MAJJHIMO}… nếu một tỳ-khưu {THERO} mà phạm giới, có phẩm chất xấu, thì đó là sự "
             "xấu xí của người ấy." + potthaka_monk("X").split("thì đó là sự xấu xí của người ấy.", 1)[1])
    L.append(f"{EVARUPO_THERO}. {cap(TAMENAM)} “{BALASSA}, ông mà cũng nghĩ là mình nên nói sao”! Vị ấy nổi giận, "
             "không hài lòng, thốt ra loại lời nói mà vì loại lời nói như vậy Tăng đoàn trục xuất vị ấy, như tấm "
             f"vải gai thô bị vứt lên đống rác. Đây là {pot_lc} {SANTO_BHIKKHU}.")

    # ^4-117 Kāsi cloth (4 lines)
    kas = f"{TYPES3} giống như {B.SIMILE['kāsikavattha']}"
    kas_lc = kas[:1].lower() + kas[1:]
    L.append(f"{tattha_who(kas_lc)} Ba loại vải xứ Ca-thi – "
             + cloth_triplet("vải xứ Ca-thi", "đẹp, khi tiếp xúc thì dễ chịu và có giá trị lớn")
             + ". Ngay cả vải xứ Ca-thi đã cũ, người ta cũng dùng để gói châu báu, hoặc cất nó vào hộp đựng hương "
             "thơm.")
    L.append(f"{cap(EVAMEVAM)} {kas_lc} này {SANTO_BHIKKHU}. {KATAME_TAYO} "
             + kasika_monk(NAVO, " [dị bản (mọi bản): yesaṃ kho pana; Tăng Chi Bộ Kinh 3.100]",
                           " [khác chính tả (Sī.): patigaṇhāti; nhưng phù hợp với Phụ chú giải Rūpasiddhi]"))
    L.append(f"Nếu một tỳ-khưu {MAJJHIMO}… nếu một tỳ-khưu {THERO} mà giữ giới, có phẩm chất tốt, thì đó là sự "
             "đẹp đẽ của người ấy." + kasika_monk("X").split("thì đó là sự đẹp đẽ của người ấy.", 1)[1])
    L.append(f"{EVARUPO_THERO}, {TAMENAM} “Này các tôn giả, hãy giữ im lặng, vị tỳ-khưu trưởng lão đang nói về "
             "Giáo Pháp và Giới Luật”. Lời nói ấy của vị ấy được ghi nhớ, như tấm vải xứ Ca-thi được cất trong hộp "
             f"đựng hương thơm. Đây là {kas_lc} {SANTO_BHIKKHU}.")

    # ^4-118 … ^4-120 measure
    L.append(f"{q(N['suppameyyo'])} {IDHE} xao động, kiêu căng, nhẹ dạ, lắm lời, ăn nói tản mạn, mất tỉnh thức, "
             "thiếu hiểu biết rõ ràng, không được định tâm, có tâm rối loạn, có các giác quan buông lỏng "
             + close(N['suppameyyo']))
    L.append(f"{q(N['duppameyyo'])} {IDHE} không xao động, không kiêu căng, không nhẹ dạ, không lắm lời, không ăn "
             "nói tản mạn, có sự tỉnh thức được thiết lập, có hiểu biết rõ ràng, được định tâm, có tâm hợp nhất, có "
             "các giác quan được thu thúc " + close(N['duppameyyo']))
    L.append(f"{q(N['appameyyo'])} {ARAHANT_SENT} {close(N['appameyyo'])}")

    # ^4-121 … ^4-126 association
    L.append(f"{q('người ' + NSEV)} {IDHE} kém hơn mình về giới hạnh, định tâm và trí tuệ. {EVARUPO} {NSEV}, "
             "ngoại trừ vì lòng thương mến, ngoại trừ vì lòng thương xót.")
    saman = ("khi chúng ta ngang bằng nhau về {x}, giữa chúng ta sẽ có cuộc trò chuyện về {x}, cuộc trò chuyện ấy "
             "sẽ thoải mái đối với chúng ta, và sẽ được tiếp diễn{v} giữa chúng ta")
    L.append(f"{q('người ' + SEV)} {IDHE} ngang bằng mình về giới hạnh, định tâm và trí tuệ. {EVARUPO} {SEV}. "
             f"{KISSA} “{cap(saman.format(x='giới hạnh', v=''))}; "
             f"{saman.format(x='định tâm', v=' [khác chính tả (Sī.): pavattanī; Tăng Chi Bộ Kinh 3.26]')}; "
             f"{saman.format(x='trí tuệ', v='')}”. {TASMA} {EVARUPO.lower()} {SEV}.")
    kh = ("khối {x} nào chưa đầy đủ, tôi sẽ làm cho đầy đủ, hoặc khối {x} nào đã đầy đủ, tôi sẽ dùng trí tuệ mà "
          "hỗ trợ cho nó ở chỗ này chỗ kia")
    L.append(f"{q('người ' + SEV + ' ' + SAKKATVA)} {IDHE} hơn mình về giới hạnh, định tâm và trí tuệ. "
             f"{EVARUPO} {SEV} {SAKKATVA}. {KISSA} “{cap(kh.format(x='giới hạnh'))}; {kh.format(x='định tâm')}; "
             f"{kh.format(x='trí tuệ')}”. {TASMA} {EVARUPO.lower()} {SEV} {SAKKATVA}.")
    rep_bad = "“Con người này kết bạn với người xấu, có bạn đồng hành xấu, nghiêng về phía cái xấu”"
    rep_good = "“Con người này kết bạn với người tốt, có bạn đồng hành tốt, nghiêng về phía cái tốt”"
    follow = "dù mình không noi theo gương của người như vậy, nhưng tiếng {x} về mình vẫn lan truyền –"
    L.append(f"{q('người ' + JIGUCCHA + ', ' + NSEV)} {IDHE} {DUSSILA}. {EVARUPO} {JIGUCCHA}, {NSEV}. {KISSA} "
             f"{cap(follow.format(x='xấu'))} {rep_bad}. {SEYYATHA} con rắn đã rơi vào phân, dù không cắn, nhưng vẫn "
             f"làm vấy bẩn người ta; {EVAMEVAM} {follow.format(x='xấu')} {rep_bad}! "
             f"{TASMA} {EVARUPO.lower()} {JIGUCCHA}, {NSEV}.")
    L.append(f"{q('người ' + AJJHUPEKKHA + ', ' + NSEV)} {IDHE} {kodha()}. {aru()}. {TINDUKA}. {GUTHAKUPA}; "
             f"{EVARUPO.lower()} {AJJHUPEKKHA}, {NSEV}. {KISSA} “Người ấy có thể mắng nhiếc tôi, có thể lăng mạ "
             f"tôi, có thể gây điều bất lợi cho tôi”! {TASMA} {EVARUPO.lower()} {AJJHUPEKKHA}, {NSEV}.")
    L.append(f"{q('người ' + SEV)} {IDHE} {SILAVA} – {EVARUPO.lower()} {SEV}. {KISSA} "
             f"{cap(follow.format(x='tốt'))} {rep_good}! {TASMA} {EVARUPO.lower()} {SEV}.")

    # ^4-127 … ^4-129 training (names as in matrix item (15); unquoted in the Pāli)
    L.append(f"{q(SIKKHA_NAME[0])} {SOTA_SAKA} – những người này được gọi là những {SIKKHA_NAME[0]}.")
    L.append(f"{q(SIKKHA_NAME[1])} {cap(N['anāgāmī'])} – người này được gọi là {SIKKHA_NAME[1]}.")
    L.append(f"{q(SIKKHA_NAME[2])} {cap(N['arahā'])} – người này được gọi là {SIKKHA_NAME[2]}.")

    # ^4-130 three teachers (2 lines)
    k, r, ve = (PARINNA.format(x=x) for x in ("dục lạc", "hình sắc", "cảm giác"))
    t1 = f"{k}, không {r}, không {ve}"
    t2 = f"{k}, {r}, không {ve}"
    t3 = f"{k}, {r}, {ve}"
    L.append(f"{tattha_who('ba bậc đạo sư')} Ở đời này, có bậc đạo sư {k} [khác chính tả (Sī., Syā.): paññāpeti], "
             f"không {r}, không {ve}. Ở đời này, lại có bậc đạo sư {t2}. Ở đời này, lại có bậc đạo sư {t3}.")
    L.append(f"{TATRA} bậc đạo sư nào {t1}, {DATTHABBO.format(x='bậc đạo sư có được thành tựu thiền thuộc cõi hình sắc')}. "
             f"{TATRA} bậc đạo sư nào {t2}, "
             f"{DATTHABBO.format(x='bậc đạo sư có được thành tựu thiền thuộc cõi không hình sắc')}. "
             f"{TATRA} bậc đạo sư nào {t3}, {DATTHABBO.format(x='bậc đạo sư Tự Giác Ngộ Hoàn Toàn')}. "
             "Đây là ba bậc đạo sư.")

    # ^4-131 another three teachers (3 lines)
    a1 = f"đề ra {ATTA} trong đời này, và đề ra {ATTA} trong đời sau"
    a2 = f"đề ra {ATTA} trong đời này, nhưng không đề ra {ATTA} trong đời sau"
    a3 = f"không đề ra {ATTA} trong đời này, và không đề ra {ATTA} trong đời sau"
    L.append(f"{tattha_who('ba bậc đạo sư khác nữa')} Ở đời này, có bậc đạo sư {a1}. Ở đời này, lại có bậc đạo sư "
             f"{a2}. Ở đời này, lại có bậc đạo sư {a3}.")
    L.append(f"{TATRA} bậc đạo sư nào {a1}, "
             f"{DATTHABBO.format(x='bậc đạo sư theo học thuyết về sự trường tồn')}. {TATRA} bậc đạo sư nào {a2}, "
             f"{DATTHABBO.format(x='bậc đạo sư theo học thuyết về sự đoạn diệt')}. {TATRA} bậc đạo sư nào {a3}, "
             f"{DATTHABBO.format(x='bậc đạo sư Tự Giác Ngộ Hoàn Toàn')}. Đây là ba bậc đạo sư khác nữa.")
    L.append(B.NIDDESA_CLOSER[3])
    return L


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    return len(CROSS)


def main():
    n = check_cross()
    for m in MATRIX_CHECK:
        assert m in MATIKA, "matrix item not found: " + m[:60]
    assert len(KAMA) == 3 and len(SIKKHA) == 3
    lines = chapter()
    name = "4-tikapuggalapannatti.md"
    text = B.assemble(name, lines)
    (B.OUT_DIR / name).write_bytes(text.encode("utf-8"))
    # every Tika name of B.NAME is asked and quoted; matrix-derived names are asked
    for p in B.TIKA_NAMES:
        assert f"Thế nào là {B.NAME[p]}?" in text, p
        assert f"“{B.NAME[p]}”" in text, p
        assert B.TIKA_NAMES[p] == B.NAME[p], p
    for p in ("kāyasakkhī", "diṭṭhippatto", "saddhāvimutto"):
        assert f"Thế nào là {N[p]}?" in text and f"“{N[p]}”" in text, p
    for nm in KAMA_NAME + SIKKHA_NAME:
        assert f"Thế nào là {nm}?" in text, nm
    for s in ("gilāna", "potthaka", "kāsikavattha"):
        assert f"{B.TYPES_COUNT[3].lower()} giống như {B.SIMILE[s]}" in text, s
    for bad in ("—", ":-", "chánh niệm", "…."):
        assert bad not in text, bad
    print(f"OK: cross-book strings {n}; matrix items {len(MATRIX_CHECK)}; wrote {name} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
