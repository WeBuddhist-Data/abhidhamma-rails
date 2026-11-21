"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 5, Catukkapuggalapaññatti (^4-1-4-0, ^4-132 .. ^4-190).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/5-catukkapuggalapannatti.md from fixed strings.
Imports the approved sample constants READ-ONLY (build_rails_sample_vi as S; importing writes nothing).
At build time: every string in REUSED is asserted to occur in that book's approved Vietnamese rails (pi-1 / pi-2);
every person name taken from S.NAME is asserted to occur verbatim in the output.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-5.md.

usage: python -I -X utf8 build_rails_5_vi.py
"""
import pathlib
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

OUT = S.OUT_DIR / "5-catukkapuggalapannatti.md"
NAMES_USED = {}


def N(k):
    NAMES_USED[k] = S.NAME[k]
    return S.NAME[k]


def P(k):
    """Predicate of an «có người …» matrix name, as a person name «người …» (frame «Người như thế nào là X?»)."""
    v = N(k)
    assert v.startswith("có người "), v
    return "người " + v[len("có người "):]


cap = S.cap
IDH = S.IDHEKACCO
q, cd, cs, qk, ev = S.q_katamo, S.close_dash, S.close_sentence, S.q_kathanca, S.evam


def lc(s):
    return s[:1].lower() + s[1:]


# ---------------------------------------------------------------------------------------------------------------
# Variant notes (sigla and Pāli kept, label translated)
# ---------------------------------------------------------------------------------------------------------------
V_PISUNA = " [khác chính tả: pisuṇāvāco]"
V_PHARUSA = " [khác chính tả (Sī.): pharusāvāco; Trường Bộ Kinh 3.115]"
V_MICCHA = " [khác chính tả (Ka.): micchādiṭṭhī]"
V_SAMMA = " [khác chính tả (Ka.): sammādiṭṭhī]"
V_YUTTA = " [khác chính tả (Syā.): yuttapaṭibhāṇo; Tăng Chi Bộ Kinh 4.132]"
V_PAKKA = " [khác chính tả: pakkavaṇṇī]"
V_AMA = " [khác chính tả (Syā., Ka.): āmavaṇṇī; Tăng Chi Bộ Kinh 4.105]"
V_SAMMINJ = " [khác chính tả (Sī., Syā.): sammiñjitaṃ]"
V_BALI = " [khác chính tả (Syā.): balibaddhā]"
V_SAGAVA = " [dị bản (Ka., Sī.): sagavacaṇḍo; Tăng Chi Bộ Kinh 4.108]"
V_ASIVISA = " [khác chính tả (Syā.): āsivisā]"
V_NEVA = " [dị bản (Sī.): neva kho; Tăng Chi Bộ Kinh 4.110]"
V_PARANIMMITA = " [khác chính tả (Sī., Syā.): paranimmitavasavattideve]"
V_VENA = " [khác chính tả (Sī., Syā.): veṇakule]"
V_DALIDDA = " [khác chính tả (Sī.): daḷidde; xem Tăng Chi Bộ Kinh]"
V_VANNAHARI = " [dị bản (Sī.): paravaṇṇahāriyā]"
V_HATTHA = " [khác chính tả (Syā.): hatthāvalekhano]"
V_KALOPI = " [khác chính tả (Sī., Syā.): kalopimukhā; Trung Bộ Kinh 2.7]"
V_DVAHIKA = " [khác chính tả (Sī.): dvāhikampi]"
V_ULUKA = " [khác chính tả (Sī., Syā.): ulukapakkhampi]"
V_SAYA = " [khác chính tả (Syā., Ka.): sāyaṃtatiyakampi; Trung Bộ Kinh 2.7]"
V_MUDDHA = " [dị bản (Syā., Ka.): muddhābhisitto]"
V_SANDHA = " [khác chính tả (Syā.): santāgāraṃ; dị bản (Sī.): yaññāgāraṃ]"
V_KHARA = " [dị bản (Syā., Ka.): khurājinaṃ]"
V_KANDU = " [khác chính tả (Sī.): kaṇḍūyamāno]"
V_ASSA = (" [phần trong ( ) không có trong bản chép tay Tích Lan. Trong kinh Kandaraka của Trung Bộ Kinh "
          "cũng như vậy]")
V_BARIHISA = " [dị bản (Sī., Syā., Ka.): parihiṃsatthāyāti; Trung Bộ Kinh 2.9]"
V_ARACARI = " [dị bản (Ka.): anācārī]"
V_SAVIYOGA = " [dị bản (Syā., Ka.): … sāviyogā]"
V_PASSA = " [xem Trung Bộ Kinh 2, kinh Kandaraka; và Tăng Chi Bộ Kinh 1, kinh Attantapa]"
V_THINA = " [khác chính tả (Sī., Syā.): thīnamiddhaṃ]"
V_DHAMMANU = (" [dị bản (Syā.): na dhammamaññāya na dhammānudhammapaṭipanno; dị bản (Ka.): na dhammamaññāya "
              "dhammānudhammappaṭipanno]")

# ---------------------------------------------------------------------------------------------------------------
# Courses of action (^4-132 .. ^4-143); objects as pi-2 ^2-703 / ^2-U45
# ---------------------------------------------------------------------------------------------------------------
SURA = "dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"     # surāmerayamajjapamādaṭṭhāyī
ACT10 = ["sát hại sinh mạng", "lấy của không được cho", "có hành vi sai trái trong các dục lạc", "nói dối",
         "nói lời chia rẽ", "nói lời thô ác", "nói lời phù phiếm", "có sự thèm muốn", "có tâm ác ý",
         "có quan điểm sai lầm"]                                       # pāṇātipātī … micchādiṭṭhi (hoti)
ACT5 = ACT10[:4] + [SURA]
INC10 = (ACT10[:4] + ["dùng lời nói chia rẽ", "dùng lời nói thô ác"] + ACT10[6:8]
         + ["có ác ý", "có quan điểm sai lầm"])   # parañca X-e / X-āya samādapeti (pisuṇāya vācāya, byāpāde)
INC5 = ACT5
ABST5 = ["việc sát hại sinh mạng", "việc lấy của không được cho", "hành vi sai trái trong các dục lạc",
         "việc nói dối", "việc " + SURA]                               # X-ā paṭivirato / veramaṇiyā   (pi-2)
ABST7 = ABST5[:4] + ["lời nói chia rẽ", "lời nói thô ác", "việc nói lời phù phiếm"]   # (pi-2)
GOOD10 = ["kiêng tránh " + x for x in ABST7] + ["không có sự thèm muốn", "có tâm không ác ý", "có quan điểm đúng đắn"]
GOODINC10 = (["kiềm chế " + x for x in ABST7]
             + ["không có sự thèm muốn", "không có ác ý", "có quan điểm đúng đắn"])  # veramaṇiyā / anabhijjhāya …


def self_and(own, other):            # attanā ca X hoti parañca Y samādapeti
    return f"tự mình {own} và khuyến khích người khác {other}"


# ---------------------------------------------------------------------------------------------------------------
# Strings reused from pi-1 / pi-2 rails (asserted) and new strings of this chapter (notes-rails-5.md)
# ---------------------------------------------------------------------------------------------------------------
NINE = ("kinh, văn xuôi xen kệ, lời giải thích, kệ, lời cảm hứng, lời đã được nói như vậy, chuyện tiền thân, "
        "chuyện kỳ diệu chưa từng có, lời vấn đáp")                                                  # (pi-2)
GAIT_A = "khi đi tới, khi đi lui, khi nhìn thẳng, khi nhìn quanh, khi co tay chân"
GAIT_B = ", khi duỗi tay chân, khi mang y ngoài, bình bát và y phục"
TRUTHS = S.TRUTHS
NEG_TRUTHS = TRUTHS.replace("hiểu rõ", "không hiểu rõ")


def truths_pe(neg):                  # "idaṃ dukkha"nti … …pe… "… paṭipadā"ti yathābhūtaṃ (na)ppajānāti
    h = "không hiểu rõ" if neg else "hiểu rõ"
    return (f"{h} đúng như thật: “Đây là khổ đau”… {h} đúng như thật: "
            "“Đây là cách thực hành dẫn đến sự chấm dứt khổ đau”")


DUC_BAD = ("sau khi làm hành vi xấu bằng thân, sau khi làm hành vi xấu bằng lời nói, "
           "sau khi làm hành vi xấu bằng ý")                                                     # (pi-2)
DUC_GOOD = DUC_BAD.replace("xấu", "tốt")
APAYA = "khi thân tan rã, sau khi chết, tái sinh vào cõi khổ, cõi xấu, nơi đọa lạc, địa ngục"     # (pi-2)
SUGATI = "tái sinh vào cõi tốt lành, thế giới cõi trời"                                          # (pi-2)
NEEDS = ("thức ăn, thức uống, vải, xe cộ, vòng hoa, hương thơm, dầu thoa, giường nằm, chỗ ở, đèn đuốc")
SAMPAJANNA = ("hành động với sự hiểu biết rõ ràng khi đi tới, khi đi lui; hành động với sự hiểu biết rõ ràng khi "
              "nhìn thẳng, khi nhìn quanh; hành động với sự hiểu biết rõ ràng khi co tay chân, khi duỗi tay chân; "
              "hành động với sự hiểu biết rõ ràng khi mang y ngoài, bình bát và y phục; hành động với sự hiểu biết "
              "rõ ràng khi ăn, khi uống, khi nhai, khi nếm; hành động với sự hiểu biết rõ ràng khi đại tiện, tiểu "
              "tiện; hành động với sự hiểu biết rõ ràng khi đi, khi đứng, khi ngồi, khi ngủ, khi thức, khi nói, "
              "khi im lặng")                                                                     # (pi-2)
SENASANA = ("lui tới chỗ ở thanh vắng: rừng, gốc cây, núi, khe núi, hang núi, bãi tha ma, rừng sâu, "
            "khoảng trời trống, đống rơm")                                                       # (pi-2)
PALLANKA = "ngồi xuống, xếp chân kiết già, đặt thân ngay thẳng, thiết lập sự tỉnh thức trước mặt"  # (pi-2)
NIV1 = ("dứt bỏ sự thèm muốn đối với thế gian, vị ấy sống với tâm đã lìa sự thèm muốn, "
        "làm trong sạch hoàn toàn tâm khỏi sự thèm muốn")                                         # (pi-2)
NIV2 = ("dứt bỏ ác ý và sự sân hận dữ dội, vị ấy sống với tâm không ác ý, thương xót và mong điều lợi ích "
        "cho mọi chúng sinh, muôn loài, làm trong sạch hoàn toàn tâm khỏi ác ý và sự sân hận dữ dội")  # (pi-2)
NIV3A = "dứt bỏ sự uể oải và đờ đẫn"
NIV3B = (", vị ấy sống đã lìa sự uể oải và đờ đẫn, có tri giác về ánh sáng, tỉnh thức và hiểu biết rõ ràng, "
         "làm trong sạch hoàn toàn tâm khỏi sự uể oải và đờ đẫn")                                 # (pi-2)
NIV4 = ("dứt bỏ sự xao động và hối tiếc, vị ấy sống không xao động, có tâm đã lắng dịu hoàn toàn ở nơi bản thân, "
        "làm trong sạch hoàn toàn tâm khỏi sự xao động và hối tiếc")                              # (pi-2)
NIV5 = ("dứt bỏ sự hoài nghi, vị ấy sống đã vượt qua sự hoài nghi, không còn băn khoăn đối với các hiện tượng "
        "thiện, làm trong sạch hoàn toàn tâm khỏi sự hoài nghi")                                  # (pi-2)
JHANA = ("Sau khi dứt bỏ năm chướng ngại này, là những thứ làm vẩn đục tâm, làm suy yếu trí tuệ, vị ấy hoàn toàn "
         "tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, chứng nhập và an trú tầng thiền thứ nhất, "
         "có sự hướng tâm và sự duy trì tâm, có sự hân hoan và hạnh phúc sinh từ sự tách biệt; nhờ sự hướng tâm "
         "và sự duy trì tâm lắng xuống, vị ấy chứng nhập và an trú tầng thiền thứ hai, có sự trong sáng ở nơi bản "
         "thân, có sự hợp nhất của tâm, không có sự hướng tâm cũng không có sự duy trì tâm, có sự hân hoan và "
         "hạnh phúc sinh từ định tâm; nhờ sự hân hoan phai nhạt, vị ấy an trú bình thản, tỉnh thức và hiểu biết "
         "rõ ràng, cảm nhận hạnh phúc bằng thân, là trạng thái mà nhờ đó các bậc thánh mô tả người ấy – “Người "
         "bình thản, có sự tỉnh thức, an trú trong hạnh phúc”, chứng nhập và an trú tầng thiền thứ ba; nhờ dứt bỏ "
         "sự dễ chịu và dứt bỏ sự khó chịu, nhờ niềm vui và nỗi buồn đã biến mất từ trước, vị ấy chứng nhập và an "
         "trú tầng thiền thứ tư, không khó chịu cũng không dễ chịu, có sự tỉnh thức hoàn toàn trong sạch nhờ sự "
         "bình thản")                                                                            # (pi-2)
SAMAHITA = ("Khi tâm đã an định như vậy, trong sạch, trong sáng, không còn vết nhơ, đã lìa những thứ làm vẩn đục, "
            "đã trở nên mềm dẻo, dễ vận dụng, vững vàng, đạt đến sự bất động, vị ấy dẫn tâm đến")
PUBBE_A = ("nhớ lại nhiều đời sống trước theo nhiều cách, cụ thể là – một đời, hai đời, ba đời, bốn đời, năm đời, "
           "mười đời, hai mươi đời, ba mươi đời, bốn mươi đời, năm mươi đời, một trăm đời, một nghìn đời, một trăm "
           "nghìn đời, nhiều kiếp thế giới tan hoại, nhiều kiếp thế giới hình thành, nhiều kiếp thế giới tan hoại "
           "và hình thành")                                                                      # (pi-2)
PUBBE_Q = ("Ở nơi kia, tôi có tên như vậy, thuộc dòng họ như vậy, có dung mạo như vậy, ăn thức ăn như vậy, cảm "
           "nhận dễ chịu và khó chịu như vậy, có tuổi thọ đến mức như vậy; chết từ nơi ấy, tôi đã sinh ra ở nơi "
           "kia; ở nơi kia, tôi cũng có tên như vậy, thuộc dòng họ như vậy, có dung mạo như vậy, ăn thức ăn như "
           "vậy, cảm nhận dễ chịu và khó chịu như vậy, có tuổi thọ đến mức như vậy; chết từ nơi ấy, tôi đã tái "
           "sinh ở đây")                                                                         # (pi-2)
PUBBE_B = "nhớ lại nhiều đời sống trước theo nhiều cách, với các nét đặc trưng và chi tiết"       # (pi-2)
DIBBA_EYE = "bằng thiên nhãn thanh tịnh, vượt quá mắt người"                                    # (pi-2)
DIBBA_A = ("thấy chúng sinh đang chết đi, đang tái sinh, thấp kém, ưu việt, đẹp đẽ, xấu xí, ở cõi tốt lành, "
           "ở cõi xấu, và hiểu rõ các chúng sinh đi theo nghiệp của mình")                       # (pi-2)
DIBBA_Q = ("Quả thật, những chúng sinh đáng kính này mang hành vi xấu bằng thân, mang hành vi xấu bằng lời nói, "
           "mang hành vi xấu bằng ý, phỉ báng các bậc thánh, có quan điểm sai lầm, thực hiện nghiệp theo quan "
           "điểm sai lầm. Khi thân tan rã, sau khi chết, họ đã tái sinh vào cõi khổ, cõi xấu, nơi đọa lạc, địa "
           "ngục. Hoặc những chúng sinh đáng kính này mang hành vi tốt bằng thân, mang hành vi tốt bằng lời nói, "
           "mang hành vi tốt bằng ý, không phỉ báng các bậc thánh, có quan điểm đúng đắn, thực hiện nghiệp theo "
           "quan điểm đúng đắn. Khi thân tan rã, sau khi chết, họ đã tái sinh vào cõi tốt lành, thế giới cõi "
           "trời")                                                                               # (pi-2)
K_PUBBE = "sự hiểu biết về sự nhớ lại các đời sống trước"                                       # (pi-2)
K_CUTI = "sự hiểu biết về sự chết và sự tái sinh của chúng sinh"                                # (pi-2)
K_ASAVA = "sự hiểu biết về sự diệt tận các ô nhiễm"                                             # (pi-2)
ASAVA3 = ("tâm được giải thoát khỏi ô nhiễm dục lạc, tâm được giải thoát khỏi ô nhiễm hiện hữu, "
          "tâm được giải thoát khỏi ô nhiễm vô minh")                    # items «ô nhiễm dục lạc» … (pi-1 ^1-1102)
ASAVA_TRUTHS = ("hiểu rõ đúng như thật: “Đây là các ô nhiễm”, hiểu rõ đúng như thật: “Đây là sự phát sinh của các "
                "ô nhiễm”, hiểu rõ đúng như thật: “Đây là sự chấm dứt các ô nhiễm”, hiểu rõ đúng như thật: “Đây là "
                "cách thực hành dẫn đến sự chấm dứt các ô nhiễm”")
KHAYA_A = "nhờ sự diệt tận các ô nhiễm"                                                         # (pi-2)
KHAYA_B = ("ngay trong đời này tự mình hiểu biết trực tiếp, chứng nghiệm, chứng nhập và an trú sự giải thoát của "
           "tâm, sự giải thoát nhờ trí tuệ, không còn ô nhiễm")                                  # (pi-2)
INDRIYA_FLOW = ("không được thu thúc thì các hiện tượng xấu ác bất thiện là sự thèm muốn và nỗi buồn có thể tràn "
                "vào người ấy, vì vậy người ấy thực hành để thu thúc năng lực ấy, bảo vệ năng lực")  # (pi-2)
SENSES = "khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân…"
NA_NIMITTA = "không nắm giữ dấu hiệu tổng quát, không nắm giữ các chi tiết"                       # (pi-1, pi-2)
SO25_FULL = S.CATUKKA_25_SO                                                     # matrix ^4-M-10 (25), approved
V_SITI = " [khác chính tả (Sī., Ka.): sītibhūto]"
assert V_SITI in SO25_FULL
SO25 = SO25_FULL.replace(V_SITI, "")         # ch5 Pāli has no variant here

REUSED = [
    (NINE, "2"), ("khi co tay chân", "2"), ("khi duỗi tay chân; hành động", "2"), ("khi nhìn thẳng, khi nhìn quanh", "2"),
    ("khi mang y ngoài, bình bát và y phục", "2"), (DUC_BAD, "2"),
    (APAYA, "2"), (SUGATI, "2"), (SAMPAJANNA, "2"), (SENASANA, "2"), (PALLANKA, "2"), (NIV1, "2"), (NIV2, "2"),
    (NIV3A + NIV3B, "2"), (NIV4, "2"), (NIV5, "2"), (JHANA, "2"), (PUBBE_A, "2"), (PUBBE_Q, "2"), (PUBBE_B, "2"),
    (DIBBA_EYE, "2"), (DIBBA_A, "2"), (DIBBA_Q, "2"), (K_PUBBE, "2"), (K_CUTI, "2"), (K_ASAVA, "2"),
    ("ô nhiễm dục lạc, ô nhiễm hiện hữu, ô nhiễm quan điểm, ô nhiễm vô minh", "1"), (KHAYA_A, "2"), (KHAYA_B, "2"),
    (INDRIYA_FLOW, "2"), (SENSES, "2"), (NA_NIMITTA, "1"), (NA_NIMITTA, "2"),
    ("điều tu học về sự kiềm chế " + ABST5[4], "2"), ("sự kiềm chế " + ABST5[0], "2"), ("sự kiềm chế " + ABST5[1], "2"),
    ("sự kiềm chế " + ABST5[2], "2"), ("sự kiềm chế " + ABST5[3], "2"), ("sự kiềm chế " + ABST7[4], "2"),
    ("sự kiềm chế " + ABST7[5], "2"), ("sự kiềm chế " + ABST7[6], "2"),
    ("hành vi xấu bằng thân", "2"), ("hành vi tốt bằng thân", "2"), ("Trường Bộ Kinh", "2"), ("Trung Bộ Kinh", "2"),
    ("Tăng Chi Bộ Kinh", "2"), ("phòng hộ cửa các giác quan", "2"), ("sự tỉnh thức và hiểu biết rõ ràng", "2"),
]

# ---------------------------------------------------------------------------------------------------------------
# Similes (^4-157 .. ^4-163, ^4-170): new strings (notes-rails-5.md)
# ---------------------------------------------------------------------------------------------------------------
LOKA = "là có thật, được tìm thấy trên thế gian"     # = ch4 WORLD            # santo saṃvijjamānā lokasmiṃ


def four(x, y, mid="nhưng"):         # X no Y, Y no X, X ca Y ca, neva X no Y
    return [f"{x} {mid} không {y}", f"{y} {mid} không {x}", f"vừa {x} vừa {y}", f"không {x} cũng không {y}"]


CLOUD = four("gầm sấm", "mưa")
MOUSE = four("đào hang", "ở hang")
MANGO = ["còn xanh mà trông như đã chín", "đã chín mà trông như còn xanh", "còn xanh và trông như còn xanh",
         "đã chín và trông như đã chín"]
POT = ["rỗng mà được đậy kín", "đầy mà để mở", "rỗng và để mở", "đầy và được đậy kín"]
LAKE = ["cạn mà trông như sâu", "sâu mà trông như cạn", "cạn và trông như cạn", "sâu và trông như sâu"]
_SAKA, _PARA = "hung dữ với đàn bò của mình", "hung dữ với đàn bò khác"
BULL = [f"{_SAKA} nhưng không {_PARA}", f"{_PARA} nhưng không {_SAKA}", f"vừa {_SAKA} vừa {_PARA}",
        f"không {_SAKA} cũng không {_PARA}"]
_AGATA, _GHORA = "có nọc độc phát nhanh", "có nọc độc dữ dội"
SNAKE = [f"{_AGATA} nhưng không {_GHORA}", f"{_GHORA} nhưng không {_AGATA}", f"vừa {_AGATA} vừa {_GHORA}",
         f"không {_AGATA} cũng không {_GHORA}"]
TREE = ["không có lõi mà xung quanh có lõi", "có lõi mà xung quanh không có lõi",
        "không có lõi và xung quanh không có lõi", "có lõi và xung quanh có lõi"]


def simile_open(name, kind, items, persons):
    return (f"Ở đây, {name} là những ai? Có bốn loại {kind} – {', '.join(items)}. Cũng như vậy, {name} này {LOKA}. "
            f"Bốn hạng người ấy là những ai? {cap(', '.join(persons))}.")


def simile_def(pred, body, thing):
    pn = "người " + pred
    return f"{qk(pn)} {body} {ev(pn)} Giống như {thing} ấy {pred}, người này cũng giống như vậy."


def simile_close(name):
    return f"{cap(name)} này {LOKA}."


def ppl(preds):
    return ["người " + p for p in preds]


# ---------------------------------------------------------------------------------------------------------------
def build():
    out = [S.seg(S.H_CHAPTER[4] + " ^4-1-4-0")]
    a = []
    # 1-3: courses of action
    a.append((f"{q(N('asappuriso'))} {IDH} {', '.join(ACT5)} {cd(N('asappuriso'))}", "^4-132"))
    a.append((f"{q(N('asappurisena asappurisataro'))} {IDH} "
              f"{', '.join(self_and(x, y) for x, y in zip(ACT5, INC5))} {cd(N('asappurisena asappurisataro'))}",
              "^4-133"))
    a.append((f"{q(N('sappuriso'))} {IDH} {', '.join('kiêng tránh ' + x for x in ABST5)} {cd(N('sappuriso'))}",
              "^4-134"))
    a.append((f"{q(N('sappurisena sappurisataro'))} {IDH} "
              + ", ".join(f"tự mình kiêng tránh {x} và khuyến khích người khác kiềm chế {x}" for x in ABST5)
              + f" {cd(N('sappurisena sappurisataro'))}", "^4-135"))
    bad = list(ACT10)
    bad[4] += V_PISUNA
    bad[5] += V_PHARUSA
    bad[9] += V_MICCHA
    a.append((f"{q(N('pāpo'))} {IDH} {', '.join(bad)} {cd(N('pāpo'))}", "^4-136"))
    a.append((f"{q(N('pāpena pāpataro'))} {IDH} {', '.join(self_and(x, y) for x, y in zip(ACT10, INC10))} "
              f"{cd(N('pāpena pāpataro'))}", "^4-137"))
    good = list(GOOD10)
    good[9] += V_SAMMA
    a.append((f"{q(N('kalyāṇo'))} {IDH} {', '.join(good)} {cd(N('kalyāṇo'))}", "^4-138"))
    goodinc = [f"tự mình {x} và khuyến khích người khác {y}" for x, y in zip(GOOD10, GOODINC10)]
    a.append((f"{q(N('kalyāṇena kalyāṇataro'))} {IDH} {', '.join(goodinc)} {cd(N('kalyāṇena kalyāṇataro'))}",
              "^4-139"))
    a.append((f"{q(N('pāpadhammo'))} {IDH} {ACT10[0]}, {ACT10[1]}… {ACT10[9]} {cd(N('pāpadhammo'))}", "^4-140"))
    inc = [self_and(x, y) for x, y in zip(ACT10, INC10)]
    a.append((f"{q(N('pāpadhammena pāpadhammataro'))} {IDH} {inc[0]}, {inc[1]}… {inc[9]} "
              f"{cd(N('pāpadhammena pāpadhammataro'))}", "^4-141"))
    # ^4-142 samādiṭṭhi: spelling slip for sammādiṭṭhi, rendered as meant
    a.append((f"{q(N('kalyāṇadhammo'))} {IDH} {GOOD10[0]}, {GOOD10[1]}… {GOOD10[9]} {cd(N('kalyāṇadhammo'))}",
              "^4-142"))
    a.append((f"{q(N('kalyāṇadhammena kalyāṇadhammataro'))} {IDH} {goodinc[0]}… {goodinc[9]} "
              f"{cd(N('kalyāṇadhammena kalyāṇadhammataro'))}", "^4-143"))
    # 4: faults
    door = ["thân", "lời nói", "ý"]
    a.append((f"{q(N('sāvajjo'))} {IDH} {', '.join(f'mang nghiệp có lỗi bằng {d}' for d in door)} "
              f"{cd(N('sāvajjo'))}", "^4-144"))
    a.append((f"{q(N('vajjabahulo'))} {IDH} "
              f"{', '.join(f'mang nhiều nghiệp có lỗi bằng {d}, ít nghiệp không có lỗi' for d in door)} "
              f"{cd(N('vajjabahulo'))}", "^4-145"))
    a.append((f"{q(N('appavajjo'))} {IDH} "
              f"{', '.join(f'được trang bị nhiều nghiệp không có lỗi bằng {d}, ít nghiệp có lỗi' for d in door)} "
              f"{cd(N('appavajjo'))}", "^4-146"))
    a.append((f"{q(N('anavajjo'))} {IDH} {', '.join(f'được trang bị nghiệp không có lỗi bằng {d}' for d in door)} "
              f"{cd(N('anavajjo'))}", "^4-147"))
    # 5: understanding
    a.append((f"{q(N('ugghaṭitaññū'))} Người nào có sự thấu hiểu Giáo Pháp ngay vào lúc điều ấy được nêu ra "
              f"{cd(N('ugghaṭitaññū'))}", "^4-148"))
    a.append((f"{q(N('vipañcitaññū'))} Người nào có sự thấu hiểu Giáo Pháp khi ý nghĩa của điều được nói vắn tắt "
              f"được phân tích chi tiết {cd(N('vipañcitaññū'))}", "^4-149"))
    a.append((f"{q(N('neyyo'))} Người nào học thuộc, hỏi han, chú tâm đúng cách, gần gũi, kết giao, thân cận những "
              f"người bạn tốt, và như vậy dần dần có sự thấu hiểu Giáo Pháp {cd(N('neyyo'))}", "^4-150"))
    a.append((f"{q(N('padaparamo'))} Người nào dù nghe nhiều, nói nhiều, ghi nhớ nhiều, dạy người khác tụng đọc "
              f"nhiều, cũng không có sự thấu hiểu Giáo Pháp trong đời sống ấy {cd(N('padaparamo'))}", "^4-151"))
    # 6: ready response
    asked = f"{IDH} khi được hỏi một câu hỏi thì trả lời"
    n1 = N("yuttappaṭibhāno, no muttappaṭibhāno")
    a.append((f"{q(n1.replace('xác đáng', 'xác đáng' + V_YUTTA, 1))} {asked} xác đáng nhưng không nhanh {cd(n1)}",
              "^4-152"))
    n2 = N("muttappaṭibhāno, no yuttappaṭibhāno")
    a.append((f"{q(n2)} {asked} nhanh nhưng không xác đáng {cd(n2)}", "^4-153"))
    n3 = N("yuttappaṭibhāno ca muttappaṭibhāno ca")
    a.append((f"{q(n3)} {asked} vừa xác đáng vừa nhanh {cd(n3)}", "^4-154"))
    n4 = N("neva yuttappaṭibhāno no muttappaṭibhāno")
    a.append((f"{q(n4)} {asked} không xác đáng cũng không nhanh {cd(n4)}", "^4-155"))   # ^4-155 "vuccati, puggalo"
    out += [S.seg(t + " " + i) for t, i in a]

    # 7: Dhamma speakers
    dk = "có người thuyết giảng Giáo Pháp nói"
    evr = "Người thuyết giảng Giáo Pháp như vậy, đối với hội chúng như vậy, được kể là người thuyết giảng Giáo Pháp."
    par_no = "và hội chúng của người ấy không thông thạo về điều mạch lạc và điều không mạch lạc."
    par_ok = "và hội chúng của người ấy thông thạo về điều mạch lạc và điều không mạch lạc."
    nd = N("cattāro dhammakathikā puggalā")
    out.append(S.seg(
        f"Ở đây, {nd} là những ai? Ở đời này, {dk} ít và không mạch lạc, {par_no} {evr}",
        f"Lại nữa, ở đời này, {dk} ít và mạch lạc, {par_ok} {evr}",
        f"Lại nữa, ở đời này, {dk} nhiều và không mạch lạc, {par_no} {evr}",
        f"Lại nữa, ở đời này, {dk} nhiều và mạch lạc, {par_ok} {evr} "
        f"Đây là bốn “{nd.replace('bốn ', '', 1)}”. ^4-156"))

    # 8: clouds
    nv = N("cattāro valāhakūpamā puggalā")
    bodies = [f"{IDH} nói nhưng không làm.", f"{IDH} làm nhưng không nói.", f"{IDH} vừa nói vừa làm.",
              f"{IDH} không nói cũng không làm."]
    out.append(S.seg(simile_open(nv, "mây mưa", ["loại " + p for p in CLOUD], ppl(CLOUD)),
                     *[simile_def(p, b, "đám mây mưa") for p, b in zip(CLOUD, bodies)],
                     simile_close(nv) + " ^4-157"))

    # 9: mice
    nm = N("cattāro mūsikūpamā puggalā")
    learn = [True, False, True, False]
    know = [False, True, True, False]
    bodies = [f"{IDH} {'' if l else 'không '}học thuộc Giáo Pháp – {NINE}. Người ấy {TRUTHS if k else NEG_TRUTHS}."
              for l, k in zip(learn, know)]
    out.append(S.seg(simile_open(nm, "chuột", ["loại " + p for p in MOUSE], ppl(MOUSE)),
                     *[simile_def(p, b, "con chuột") for p, b in zip(MOUSE, bodies)],
                     simile_close(nm) + " ^4-158"))

    # 10-12: mangoes, pots, lakes (deportment + truths)
    def gait(pleasing, variant=""):
        return f"{IDH} {'' if pleasing else 'không '}có dáng vẻ đáng mến {GAIT_A}{variant}{GAIT_B}."

    na = N("cattāro ambūpamā puggalā")
    items = ["quả " + p for p in MANGO]
    items[0] += V_PAKKA
    items[1] += V_AMA
    mango_bodies = [f"{gait(True, V_SAMMINJ)} Người ấy {NEG_TRUTHS}.", f"{gait(False)} Người ấy {TRUTHS}.",
                    f"{gait(False)} Người ấy {truths_pe(True)}.", f"{gait(True)} Người ấy {truths_pe(False)}."]
    out.append(S.seg(simile_open(na, "quả xoài", items, ppl(MANGO)),
                     *[simile_def(p, b, "quả xoài") for p, b in zip(MANGO, mango_bodies)],
                     simile_close(na) + " ^4-159"))

    def pe_bodies(pattern):          # pattern: (pleasing, knows) per line, abbreviated truths
        return [f"{gait(pl)} Người ấy {truths_pe(not kn)}." for pl, kn in pattern]

    nk = N("cattāro kumbhūpamā puggalā")
    lines = [simile_def(p, b, "cái chum") for p, b in
             zip(POT, pe_bodies([(True, False), (False, True), (False, False), (True, True)]))]
    lines[-1] += " " + simile_close(nk)
    out.append(S.seg(simile_open(nk, "chum", ["chum " + p for p in POT], ppl(POT)), *lines[:-1],
                     lines[-1] + " ^4-160"))

    nu = N("cattāro udakarahadūpamā puggalā")
    lines = [simile_def(p, b, "hồ nước") for p, b in
             zip(LAKE, pe_bodies([(True, False), (False, True), (False, False), (True, True)]))]
    lines[-1] += " " + simile_close(nu)
    out.append(S.seg(simile_open(nu, "hồ nước", ["hồ " + p for p in LAKE], ppl(LAKE)), *lines[:-1],
                     lines[-1] + " ^4-161"))

    # 13: bulls
    nb = N("cattāro balībaddūpamā puggalā")
    items = ["loại " + p for p in BULL]
    items[0] = items[0].replace(_SAKA, _SAKA + V_SAGAVA, 1)
    first = simile_open(nb, "bò đực", items, ppl(BULL)).replace("bò đực –", "bò đực" + V_BALI + " –", 1)
    own, other = "hội chúng của mình", "hội chúng của người khác"
    bodies = [f"{IDH} làm cho {own} sợ hãi, không làm cho {other} sợ hãi.",
              f"{IDH} làm cho {other} sợ hãi, không làm cho {own} sợ hãi.",
              f"{IDH} làm cho cả {own} lẫn {other} sợ hãi.",
              f"{IDH} không làm cho {own} sợ hãi, cũng không làm cho {other} sợ hãi."]
    lines = [simile_def(p, b, "con bò đực") for p, b in zip(BULL, bodies)]
    lines[-1] += " " + simile_close(nb)
    out.append(S.seg(first, *lines[:-1], lines[-1] + " ^4-162"))

    # 14: snakes
    ns = N("cattāro āsīvisūpamā puggalā")
    first = simile_open(ns, "rắn độc", ["loại " + p for p in SNAKE], ppl(SNAKE)).replace(
        "rắn độc –", "rắn độc" + V_ASIVISA + " –", 1)
    often, not_often = f"{IDH} thường hay nổi giận.", f"{IDH} quả thật không{V_NEVA} thường hay nổi giận."
    lasts = "Và sự giận dữ ấy quả thật {}nằm sẵn nơi người ấy lâu dài suốt một thời gian dài."   # = ch4
    bodies = [f"{often} {lasts.format('không ')}", f"{not_often} {lasts.format('')}",
              f"{often} {lasts.format('')}",
              f"{IDH} quả thật không thường hay nổi giận. {lasts.format('không ')}"]
    lines = [simile_def(p, b, "con rắn độc") for p, b in zip(SNAKE, bodies)]
    lines[-1] += " " + simile_close(ns)
    out.append(S.seg(first, *lines[:-1], lines[-1] + " ^4-163"))

    # 15-16: praise and blame without / after investigation
    def praise_lines(keys, bodies, bid):
        ls = [f"{qk(P(k))} {IDH} {b} {ev(P(k))}" for k, b in zip(keys, bodies)]
        ls[-1] += " " + bid
        return S.seg(*ls)

    tith = "các đạo sĩ ngoại đạo và các đệ tử của đạo sĩ ngoại đạo, những người thực hành tồi tệ, thực hành sai lầm"
    budd = "các vị Phật và các đệ tử của các vị Phật, những người thực hành tốt đẹp, thực hành đúng đắn"
    wrong_p = "cách thực hành tồi tệ, cách thực hành sai lầm"
    right_p = "cách thực hành tốt đẹp, cách thực hành đúng đắn"
    say_good = "rằng họ “thực hành tốt đẹp”, rằng họ “thực hành đúng đắn”."
    say_bad = "rằng họ “thực hành tồi tệ”, rằng họ “thực hành sai lầm”."
    is_good = "rằng đó là “cách thực hành tốt đẹp”, rằng đó là “cách thực hành đúng đắn”."
    is_bad = "rằng đó là “cách thực hành tồi tệ”, rằng đó là “cách thực hành sai lầm”."
    k15 = ["ananuvicca apariyogāhetvā avaṇṇārahassa vaṇṇaṃ bhāsitā hoti",
           "ananuvicca apariyogāhetvā vaṇṇārahassa avaṇṇaṃ bhāsitā hoti",
           "ananuvicca apariyogāhetvā appasādanīye ṭhāne pasādaṃ upadaṃsitā hoti",
           "ananuvicca apariyogāhetvā pasādanīye ṭhāne appasādaṃ upadaṃsitā hoti"]
    out.append(praise_lines(k15, [f"nói lời khen ngợi {tith} – {say_good}", f"nói lời chê trách {budd} – {say_bad}",
                                  f"làm phát sinh lòng tin trong sáng nơi {wrong_p} – {is_good}",
                                  f"làm phát sinh sự thiếu lòng tin trong sáng nơi {right_p} – {is_bad}"], "^4-164"))
    k16 = ["anuvicca pariyogāhetvā avaṇṇārahassa avaṇṇaṃ bhāsitā hoti",
           "anuvicca pariyogāhetvā vaṇṇārahassa vaṇṇaṃ bhāsitā hoti",
           "anuvicca pariyogāhetvā appasādanīye ṭhāne appasādaṃ upadaṃsitā hoti",
           "anuvicca pariyogāhetvā pasādanīye ṭhāne pasādaṃ upadaṃsitā hoti"]
    out.append(praise_lines(k16, [f"nói lời chê trách {tith} – {say_bad}", f"nói lời khen ngợi {budd} – {say_good}",
                                  f"làm phát sinh sự thiếu lòng tin trong sáng nơi {wrong_p} – {is_bad}",
                                  f"làm phát sinh lòng tin trong sáng nơi {right_p} – {is_good}"], "^4-165"))

    # 17: truthfully, accurately, at the right time
    btk = S.BTK
    both = f"{IDH} thấy có điều đáng khen và cũng có điều đáng chê."
    blame, praise = "Điều nào ở đó là điều đáng chê, người ấy", "điều nào ở đó là điều đáng khen, người ấy"
    k17 = ["avaṇṇārahassa avaṇṇaṃ bhāsitā hoti bhūtaṃ tacchaṃ kālena, no ca kho vaṇṇārahassa vaṇṇaṃ …",
           "vaṇṇārahassa vaṇṇaṃ bhāsitā hoti bhūtaṃ tacchaṃ kālena, no ca kho avaṇṇārahassa avaṇṇaṃ …",
           "avaṇṇārahassa ca avaṇṇaṃ … ; vaṇṇārahassa ca vaṇṇaṃ …",
           "neva avaṇṇārahassa avaṇṇaṃ … no ca vaṇṇārahassa vaṇṇaṃ …"]
    b17 = [f"{blame} nói ra điều ấy {btk}, {praise} không nói ra điều ấy {btk}.",
           f"{blame.replace('chê', 'khen', 1)} nói ra điều ấy {btk}, {praise.replace('khen', 'chê', 1)} không nói ra "
           f"điều ấy {btk}.",
           f"{blame} nói ra điều ấy {btk}, {praise} cũng nói ra điều ấy {btk}. "
           "Ở đó, người ấy biết đúng lúc để trả lời câu hỏi ấy.",
           f"{blame} không nói ra điều ấy {btk}, {praise} cũng không nói ra điều ấy {btk}. "
           "Người ấy sống bình thản, tỉnh thức và hiểu biết rõ ràng."]
    ls = [f"{qk(P(k))} {both} {b} {ev(P(k))}" for k, b in zip(k17, b17)]
    out.append(S.seg(*ls[:-1], ls[-1] + " ^4-166"))

    # 18: effort and merit
    work = "Người nào có sinh kế phát sinh nhờ ra sức, cố gắng, nỗ lực"
    m1, m2 = N("uṭṭhānaphalūpajīvī no puññaphalūpajīvī"), N("puññaphalūpajīvī no uṭṭhānaphalūpajīvī")
    m3, m4 = N("uṭṭhānaphalūpajīvī ca puññaphalūpajīvī ca"), N("neva uṭṭhānaphalūpajīvī no puññaphalūpajīvī")
    out.append(S.seg(
        f"{q(m1)} {work}, chứ không phải nhờ phước {cd(m1)}",
        f"{q(m2)} Kể từ chư thiên Tha Hóa Tự Tại{V_PARANIMMITA}, chư thiên ở cao hơn đó "
        f"{m2.replace('người ', '', 1)}.",
        f"{q(m3)} {work}, và cả nhờ phước {cd(m3)}",
        f"{q(m4)} Chúng sinh địa ngục {m4.replace('người ', '', 1)}. ^4-167"))

    # 19: darkness and light
    low = (f"{IDH} tái sinh vào gia đình thấp hèn – vào gia đình hạ tiện, hoặc gia đình thợ săn, hoặc gia đình thợ "
           "đan tre{v1}, hoặc gia đình thợ đóng xe, hoặc gia đình người dọn rác, nghèo khổ{v2}, ít thức ăn, thức uống "
           "và đồ ăn, sống vất vả, nơi mà thức ăn và y phục có được một cách vất vả. Và người ấy xấu xí, khó coi, "
           f"thấp lùn, nhiều bệnh tật, hoặc chột mắt, hoặc cụt tay, hoặc què chân, hoặc bại liệt, không có được {NEEDS}.")
    high = (f"{IDH} tái sinh vào gia đình cao sang – vào gia đình quý tộc giàu có, hoặc gia đình bà-la-môn giàu có, "
            "hoặc gia đình gia chủ giàu có, sung túc, có tài sản lớn, có của cải lớn, có nhiều vàng và bạc, có nhiều "
            "tiền của và vật dụng, có nhiều tài sản và lúa gạo. Và người ấy đẹp đẽ, dễ nhìn, đáng mến, được trang bị "
            f"vẻ đẹp dung mạo tuyệt vời, có được {NEEDS}.")

    def conduct(good):
        w = "tốt" if good else "xấu"
        d = DUC_GOOD if good else DUC_BAD
        end = f"khi thân tan rã, sau khi chết, {SUGATI}" if good else APAYA
        return (f"Người ấy thực hiện hành vi {w} bằng thân, thực hiện hành vi {w} bằng lời nói, thực hiện hành vi "
                f"{w} bằng ý. Người ấy, {d}, {end}.")

    keys = ["tamo tamaparāyano", "tamo jotiparāyano", "joti tamaparāyano", "joti jotiparāyano"]
    births = [low.format(v1=V_VENA, v2=V_DALIDDA), low.format(v1="", v2=""), high, high]
    goods = [False, True, False, True]
    ls = [f"{qk(N(k))} {b} {conduct(g)} {ev(N(k))}" for k, b, g in zip(keys, births, goods)]
    out.append(S.seg(*ls[:-1], ls[-1] + " ^4-168"))

    # 20: low and high
    keys = ["oṇatoṇato", "oṇatuṇṇato", "uṇṇatoṇato", "uṇṇatuṇṇato"]
    ls = [f"{qk(N(k))[:-1]}… {lc(ev(N(k)))}" for k in keys]
    out.append(S.seg(*ls[:-1], ls[-1] + " ^4-169"))

    # 21: trees
    nr = N("cattāro rukkhūpamā puggalā")
    bad_q, good_q = "phạm giới, có phẩm chất xấu", "giữ giới, có phẩm chất tốt"
    bodies = [f"{IDH} {bad_q}, nhưng quả thật hội chúng của người ấy {good_q}.",
              f"{IDH} {good_q}, nhưng quả thật hội chúng của người ấy {bad_q}.",
              f"{IDH} {bad_q}, và hội chúng của người ấy cũng {bad_q}.",
              f"{IDH} {good_q}, và hội chúng của người ấy cũng {good_q}."]
    lines = [simile_def(p, b, "cái cây") for p, b in zip(TREE, bodies)]
    lines[-1] += " " + simile_close(nr)
    out.append(S.seg(simile_open(nr, "cây", ["cây " + p for p in TREE], ppl(TREE)), *lines[:-1],
                     lines[-1] + " ^4-170"))

    # 22-23: measure and confidence (no quotes, no dash in the Pāli)
    def measure(k1, k2, body):
        nm_ = f"{N(k1)}, {N(k2)}"
        return f"{q(nm_)} {IDH} {body} thì lấy điều ấy làm thước đo và làm phát sinh lòng tin trong sáng. " \
               f"Người này được gọi là {nm_}."

    seen = "sau khi thấy {}"
    out.append(S.seg(
        measure("rūpappamāṇo", "rūpappasanno", ", hoặc ".join(seen.format(x) for x in
                                                                 ("chiều cao", "bề ngang", "hình dáng",
                                                                  "sự tròn đầy")) + ","),
        measure("ghosappamāṇo", "ghosappasanno",
                "dựa vào lời khen ngợi của người khác, lời tán dương của người khác, lời ca ngợi của người khác, "
                f"lời truyền tụng tiếng tốt của người khác{V_VANNAHARI},") + " ^4-171"))
    out.append(S.seg(
        measure("lūkhappamāṇo", "lūkhappasanno",
                ", hoặc ".join(seen.format(x) for x in ("sự đạm bạc của y phục", "sự đạm bạc của bình bát",
                                                        "sự đạm bạc của chỗ ở",
                                                        "các khổ hạnh khó làm khác nhau")) + ","),
        measure("dhammappamāṇo", "dhammappasanno",
                ", hoặc ".join(seen.format(x) for x in ("giới hạnh", "định tâm", "trí tuệ")) + ",") + " ^4-172"))

    # 24: own and others' welfare
    five = ["giới hạnh", "định tâm", "trí tuệ", "sự giải thoát", "sự hiểu biết và thấy rõ về sự giải thoát"]
    pats = [("tự mình thành tựu về {x}, nhưng không khuyến khích người khác thành tựu về {x}"),
            ("tự mình không thành tựu về {x}, nhưng khuyến khích người khác thành tựu về {x}"),
            ("tự mình thành tựu về {x}, và khuyến khích người khác thành tựu về {x}"),
            ("tự mình không thành tựu về {x}, cũng không khuyến khích người khác thành tựu về {x}")]
    keys = ["attahitāya paṭipanno hoti, no parahitāya", "parahitāya paṭipanno hoti, no attahitāya",
            "attahitāya ceva paṭipanno hoti parahitāya ca", "neva attahitāya paṭipanno hoti no parahitāya"]
    ls = [f"{qk(P(k))} {IDH} {'; '.join(pt.format(x=x) for x in five)}. {ev(P(k))}" for k, pt in zip(keys, pats)]
    out.append(S.seg(*ls[:-1], ls[-1] + " ^4-173"))

    # 25: tormentors
    t1 = P("attantapo hoti attaparitāpanānuyogamanuyutto")
    acelaka = (
        f"{IDH} sống lõa thể, buông thả lề lối, liếm tay{V_HATTHA}, không đến khi được gọi “Hãy đến đây, thưa ngài”, "
        "không dừng lại khi được gọi “Hãy dừng lại, thưa ngài”, không nhận thức ăn được mang đến, không nhận thức ăn "
        "được làm riêng cho mình, không nhận lời mời thọ thực; người ấy không nhận thức ăn từ miệng nồi, không nhận "
        f"thức ăn từ miệng chảo{V_KALOPI}, không nhận thức ăn đưa qua ngưỡng cửa, không nhận thức ăn đưa qua cây gậy, "
        "không nhận thức ăn đưa qua chày giã gạo, không nhận từ hai người đang ăn, không nhận từ người phụ nữ mang "
        "thai, không nhận từ người phụ nữ đang cho con bú, không nhận từ người phụ nữ đang ở với đàn ông, không nhận "
        "thức ăn quyên góp, không nhận ở nơi có con chó đang chực chờ, không nhận ở nơi có ruồi bu thành đàn, không "
        "nhận cá, không nhận thịt, không uống rượu mạnh, không uống rượu men, không uống nước cám lên men. Người ấy "
        "hoặc chỉ đến một nhà, chỉ nhận một miếng, hoặc chỉ đến hai nhà, chỉ nhận hai miếng… hoặc chỉ đến bảy nhà, "
        "chỉ nhận bảy miếng; sống nhờ chỉ một phần thức ăn được cho, sống nhờ hai phần thức ăn được cho… sống nhờ bảy "
        "phần thức ăn được cho; ăn thức ăn một ngày một lần, ăn thức ăn hai ngày một lần"
        f"{V_DVAHIKA}… ăn thức ăn bảy ngày một lần. Như vậy, người ấy sống chuyên tâm thực hành việc ăn bữa ăn theo "
        "định kỳ như thế, cho đến nửa tháng một lần. Người ấy ăn rau, hoặc ăn kê, hoặc ăn lúa hoang, hoặc ăn vụn da, "
        "hoặc ăn rêu, hoặc ăn cám, hoặc ăn cơm cháy, hoặc ăn bã vừng, hoặc ăn cỏ, hoặc ăn phân bò, sống nhờ thức ăn "
        "là rễ cây và trái cây trong rừng, ăn trái cây tự rụng. Người ấy mặc vải gai, mặc vải sợi pha, mặc vải liệm "
        "tử thi, mặc vải bỏ đi, mặc vải vỏ cây, mặc da linh dương, mặc dải da linh dương, mặc áo bằng cỏ, mặc áo bằng "
        "sợi vỏ cây, mặc áo bằng ván gỗ, mặc chăn bằng tóc, mặc chăn bằng lông đuôi thú, mặc lông cánh chim cú"
        f"{V_ULUKA}, là người nhổ tóc và râu, chuyên tâm thực hành việc nhổ tóc và râu, là người đứng mãi, từ chối "
        "chỗ ngồi, là người ngồi chồm hổm, chuyên tâm nỗ lực trong tư thế ngồi chồm hổm, là người nằm trên gai, nằm "
        "trên chỗ nằm bằng gai, sống chuyên tâm thực hành việc xuống nước đến lần thứ ba vào buổi chiều"
        f"{V_SAYA}. Như vậy, người ấy sống chuyên tâm thực hành việc làm khổ và hành hạ thân theo nhiều cách như thế.")
    out.append(S.seg(f"{qk(t1)} {acelaka} {ev(t1)} ^4-174"))
    t2 = P("parantapo hoti paraparitāpanānuyogamanuyutto")
    out.append(S.seg(f"{qk(t2)} {IDH} là kẻ giết cừu, kẻ giết heo, kẻ bẫy chim, kẻ săn nai, thợ săn, kẻ giết cá, kẻ "
                     f"trộm, kẻ giết kẻ trộm, kẻ giết bò, cai ngục, hoặc bất cứ ai khác làm nghề tàn ác. {ev(t2)} ^4-175"))
    t3 = P("attantapo ca … parantapo ca …")
    kill = "hãy giết chừng này {} để tế lễ"
    sacrifice = (
        f"{IDH} là vua, một vị quý tộc đã làm lễ đăng quang{V_MUDDHA}, hoặc là một bà-la-môn giàu có. Người ấy cho "
        f"xây một hội trường{V_SANDHA} mới ở phía đông của một người, cạo bỏ tóc và râu, mặc tấm da linh dương thô "
        f"ráp{V_KHARA}, xoa thân bằng bơ lỏng và dầu, vừa gãi lưng bằng sừng nai{V_KANDU} vừa đi vào hội trường cùng "
        "với hoàng hậu và vị bà-la-môn tế sư. Ở đó, người ấy nằm trên mặt đất trống được rải cỏ xanh. Với một con bò "
        "cái có con bê cùng hình sắc, sữa nào có ở núm vú thứ nhất thì nhà vua dùng để sống, sữa nào có ở núm vú thứ hai "
        "thì hoàng hậu dùng để sống, sữa nào có ở núm vú thứ ba thì vị bà-la-môn tế sư dùng để sống, sữa nào có ở "
        "núm vú thứ tư thì người ấy dùng để dâng cúng vào lửa, con bê sống nhờ phần còn lại. Người ấy nói như sau – "
        "“" + cap(", ".join(kill.format(x) for x in ("con bò mộng", "con bò tơ đực", "con bò tơ cái", "con dê",
                                                       "con cừu")))
        + f", ({kill.format('con ngựa')}){V_ASSA}, hãy chặt chừng này cây để làm cột tế, hãy cắt chừng này cỏ để "
        f"rải nơi tế lễ”{V_BARIHISA}. Những người là nô lệ, người hầu hay người làm công của người ấy, họ cũng bị đe "
        "dọa bằng cây gậy, bị đe dọa bằng sự sợ hãi, mặt đầy nước mắt, vừa khóc vừa làm các công việc chuẩn bị.")
    out.append(S.seg(f"{qk(t3)} {sacrifice} {ev(t3)} ^4-176"))

    t4 = P("neva attantapo … na parantapo …")
    tathagata = (
        "Ở đây, Như Lai xuất hiện ở thế gian, là bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn, bậc thành tựu hiểu biết "
        "chân thật và hạnh kiểm, bậc đã khéo đi đến đích, bậc hiểu biết thế gian, bậc vô song, bậc dẫn dắt những "
        "người đàn ông cần được rèn luyện, bậc đạo sư của chư thiên và loài người, Đức Phật, Đức Thế Tôn. Ngài tự "
        "mình hiểu biết trực tiếp, chứng nghiệm rồi tuyên bố về thế gian này cùng với chư thiên, Ma vương và Phạm "
        "thiên, về chúng sinh cùng với các sa-môn và bà-la-môn, cùng với chư thiên và loài người. Ngài thuyết giảng "
        "Giáo Pháp tốt đẹp ở phần đầu, tốt đẹp ở phần giữa, tốt đẹp ở phần cuối, có ý nghĩa, có văn từ, và làm sáng tỏ "
        "đời sống tu hành trong sạch hoàn toàn đầy đủ, thanh tịnh. Gia chủ, hoặc con trai của gia chủ, hoặc người "
        "tái sinh trong một gia đình nào đó nghe Giáo Pháp ấy. Sau khi nghe Giáo Pháp ấy, người ấy có được niềm tin "
        "nơi Như Lai. Được trang bị niềm tin đã có được ấy, người ấy suy xét như sau – “Đời sống gia đình chật hẹp, "
        "là con đường của bụi mù; đời sống xuất gia là khoảng trời trống. Thật không dễ cho người sống trong gia "
        "đình mà sống đời sống tu hành trong sạch hoàn toàn đầy đủ, hoàn toàn thanh tịnh, trắng sạch như vỏ ốc được "
        "đánh bóng. Hay là tôi cạo bỏ tóc và râu, khoác những tấm y màu vàng đất, rời bỏ gia đình, xuất gia sống "
        "đời không gia đình”! Sau một thời gian, người ấy, sau khi dứt bỏ khối tài sản nhỏ hoặc sau khi dứt bỏ khối "
        "tài sản lớn, sau khi dứt bỏ vòng người thân nhỏ hoặc sau khi dứt bỏ vòng người thân lớn, cạo bỏ tóc và râu, "
        "khoác những tấm y màu vàng đất, rời bỏ gia đình, xuất gia sống đời không gia đình.")
    out.append(S.seg(f"{qk(t4)} {SO25}", tathagata + " ^4-177"))

    out.append(S.seg(
        "Đã xuất gia như vậy, vị ấy, có được sự tu học và nếp sống của các tỳ-khưu, sau khi dứt bỏ việc sát hại sinh "
        "mạng, kiêng tránh việc sát hại sinh mạng, đã bỏ gậy, đã bỏ dao, biết hổ thẹn, có lòng nhân hậu, sống thương "
        "xót và mong điều lợi ích cho mọi chúng sinh, muôn loài.",
        "Sau khi dứt bỏ việc lấy của không được cho, vị ấy kiêng tránh việc lấy của không được cho, lấy những gì được "
        "cho, mong đợi những gì được cho, sống với bản thân không trộm cắp, đã trở nên trong sạch.",
        "Sau khi dứt bỏ lối sống không trong sạch, vị ấy sống đời sống tu hành trong sạch, sống tránh xa"
        f"{V_ARACARI}, kiêng tránh sự giao hợp, là việc của người thế tục.",
        "Sau khi dứt bỏ việc nói dối, vị ấy kiêng tránh việc nói dối, nói sự thật, gắn bó với sự thật, đáng tin cậy, "
        "đáng tin tưởng, không lừa dối thế gian.",
        "Sau khi dứt bỏ lời nói chia rẽ, vị ấy kiêng tránh lời nói chia rẽ, nghe ở đây thì không nói lại ở nơi kia "
        "để chia rẽ những người này, hoặc nghe ở nơi kia thì không nói lại với những người này để chia rẽ những người "
        "kia. Như vậy, vị ấy hòa giải những người bị chia rẽ, cổ vũ những người đã hòa thuận, ưa thích sự hòa hợp, "
        "vui thích sự hòa hợp, hoan hỷ trong sự hòa hợp, nói lời tạo nên sự hòa hợp.",
        "Sau khi dứt bỏ lời nói thô ác, vị ấy kiêng tránh lời nói thô ác. Lời nói nào không có lỗi, dễ chịu với tai, "
        "dễ mến, thấm vào lòng, lịch sự, được nhiều người yêu mến, được nhiều người ưa thích, vị ấy nói lời nói như "
        "vậy.",
        "Sau khi dứt bỏ việc nói lời phù phiếm, vị ấy kiêng tránh việc nói lời phù phiếm, nói đúng lúc, nói đúng sự "
        "thật, nói điều có ý nghĩa, nói về Giáo Pháp, nói về Giới Luật, nói lời đáng ghi nhớ, đúng lúc, có lý lẽ, có "
        "giới hạn, gắn liền với ý nghĩa. ^4-178"))

    out.append(S.seg(
        "Vị ấy kiêng tránh việc làm hại các loại hạt giống và cây cỏ, ăn một bữa, không ăn vào ban đêm, tránh xa việc "
        "ăn sai giờ, kiêng tránh việc xem múa, hát, nhạc và các trò giải trí, kiêng tránh việc đeo vòng hoa, dùng "
        "hương thơm, dầu thoa, trang sức và tô điểm, kiêng tránh giường cao và giường lớn, kiêng tránh việc nhận vàng "
        "và bạc.",
        "Vị ấy kiêng tránh việc nhận lúa gạo chưa nấu, kiêng tránh việc nhận thịt chưa nấu, kiêng tránh việc nhận phụ "
        "nữ và thiếu nữ, kiêng tránh việc nhận nô tỳ nữ và nô lệ nam, kiêng tránh việc nhận dê và cừu, kiêng tránh "
        "việc nhận gà và heo, kiêng tránh việc nhận voi, bò, ngựa đực và ngựa cái, kiêng tránh việc nhận ruộng đất và "
        "đất đai, kiêng tránh việc làm người đưa tin, chạy việc vặt, kiêng tránh việc mua bán, kiêng tránh việc gian "
        "lận bằng cân, gian lận bằng tiền đồng, gian lận bằng đồ đo lường, kiêng tránh các thủ đoạn hối lộ, lừa đảo, "
        f"gian lận, quanh co{V_SAVIYOGA}, kiêng tránh việc chặt chém, giết hại, giam cầm, cướp đường, cướp bóc và "
        "bạo lực. ^4-179"))

    content = "biết đủ với y phục để che thân, với thức ăn khất thực để nuôi bụng"
    go = "Bất cứ nơi đâu vị ấy ra đi, vị ấy chỉ mang theo những thứ ấy mà ra đi"
    out.append(S.seg(
        f"Vị ấy {content}. {go}, giống như con chim có cánh, bất cứ nơi đâu nó bay, nó chỉ mang theo đôi cánh của mình "
        f"mà bay. Cũng như vậy, vị tỳ-khưu {content}. {go}. Được trang bị khối giới hạnh cao quý này, vị ấy cảm nhận "
        "ở nơi bản thân hạnh phúc không có lỗi. ^4-180"))

    def flow(organ):
        return (f"Nếu sống với năng lực {organ} {INDRIYA_FLOW} {organ}, thực hiện sự thu thúc nơi năng lực {organ}")

    out.append(S.seg(
        f"Vị ấy khi thấy hình sắc bằng mắt thì {NA_NIMITTA}. {flow('mắt')}; {SENSES} khi nhận biết đối tượng của ý "
        f"bằng ý thì {NA_NIMITTA}. {flow('ý')}. Được trang bị sự thu thúc các giác quan cao quý này, vị ấy cảm nhận ở "
        "nơi bản thân hạnh phúc không bị vẩn đục. ^4-181"))

    niv = "; ".join(["Sau khi " + NIV1, "sau khi " + NIV2, "sau khi " + NIV3A + V_THINA + NIV3B, "sau khi " + NIV4,
                     "sau khi " + NIV5]) + "."
    out.append(S.seg(
        f"Vị ấy {SAMPAJANNA}.",
        "Được trang bị khối giới hạnh cao quý này, được trang bị sự thu thúc các giác quan cao quý này, được trang "
        "bị sự tỉnh thức và hiểu biết rõ ràng cao quý này, được trang bị sự biết đủ cao quý này"
        f"{V_PASSA}, vị ấy {SENASANA}. Sau bữa ăn, khi đã đi khất thực trở về, vị ấy {PALLANKA}. {niv} ^4-182"))

    out.append(S.seg(
        f"{JHANA}.",
        f"{SAMAHITA} {K_PUBBE}. Vị ấy {PUBBE_A} – “{PUBBE_Q}”. Như vậy, vị ấy {PUBBE_B}. ^4-183"))
    out.append(S.seg(
        f"{SAMAHITA} {K_CUTI}. {cap(DIBBA_EYE)}, vị ấy {DIBBA_A} – “{DIBBA_Q}”. Như vậy, {DIBBA_EYE}, vị ấy "
        f"{DIBBA_A}. ^4-184"))
    out.append(S.seg(
        f"{SAMAHITA} {K_ASAVA}. Vị ấy {TRUTHS}, {ASAVA_TRUTHS}. Khi vị ấy biết như vậy, thấy như vậy, {ASAVA3}. Khi "
        "đã được giải thoát, có sự hiểu biết: “Đã được giải thoát”. Vị ấy hiểu rõ: “Sự sinh đã được diệt tận, đời "
        "sống tu hành trong sạch đã được sống trọn, việc cần làm đã được làm xong, không còn gì khác cho trạng thái "
        f"hiện hữu này nữa”. {ev(t4)} {SO25} ^4-185"))

    # 26: lust, hate, delusion, conceit (comma, no dash)
    pairs = [("sarāgo", "sự tham đắm"), ("sadoso", "sự sân hận"), ("samoho", "sự si mê"), ("samāno", "sự kiêu mạn")]
    ls = [f"{q(N(k))} Người nào có {x} chưa được dứt bỏ, người này được gọi là “{N(k)}”." for k, x in pairs]
    out.append(S.seg(*ls[:-1], ls[-1] + " ^4-186"))

    # 27: calm and insight
    jh = "các thành tựu thiền đi kèm với hình sắc hoặc đi kèm với không hình sắc"
    assert S.LABHI == f"{IDH} có được {jh}."
    lk = "con đường hoặc thành quả vượt thế gian"
    keys = ["lābhī … cetosamathassa, na lābhī … vipassanāya", "lābhī … vipassanāya, na lābhī … cetosamathassa",
            "lābhī ceva … cetosamathassa, lābhī ca … vipassanāya", "neva lābhī … cetosamathassa, na lābhī … vipassanāya"]
    bodies = [f"{IDH} có được {jh}, nhưng không có được {lk}.", f"{IDH} có được {lk}, nhưng không có được {jh}.",
              f"{IDH} có được {jh}, và có được {lk}.", f"{IDH} không có được {jh}, cũng không có được {lk}."]
    ls = [f"{qk(P(k))} {b} {ev(P(k))}" for k, b in zip(keys, bodies)]
    out.append(S.seg(*ls[:-1], ls[-1] + " ^4-187"))

    # 28: stream
    arahant = f"{IDH}, {KHAYA_A}, {KHAYA_B}."
    tinno = N("tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo")
    out.append(S.seg(
        f"{q(N('anusotagāmī puggalo'))} {IDH} vừa hưởng thụ các dục lạc vừa làm nghiệp ác. "
        f"{cs(N('anusotagāmī puggalo'))}",
        f"{q(N('paṭisotagāmī puggalo'))} {IDH} không hưởng thụ các dục lạc và không làm nghiệp ác. Người ấy, dù với "
        "sự khó chịu, dù với nỗi buồn, dù mặt đầy nước mắt khóc lóc, vẫn sống đời sống tu hành trong sạch đầy đủ, "
        f"thanh tịnh. {cs(N('paṭisotagāmī puggalo'))}",
        f"{q(N('ṭhitatto puggalo'))} {S.ANAGAMI_INTRO}. {cs(N('ṭhitatto puggalo'))}",
        f"{q(tinno)} {arahant} Người này được gọi là {tinno}. ^4-188"))

    # 29: learning
    keys = ["appassuto sutena anupapanno", "appassuto sutena upapanno", "bahussuto sutena anupapanno",
            "bahussuto sutena upapanno"]
    amount = ["ít", "ít", "nhiều", "nhiều"]
    ok = [False, True, False, True]
    ls = []
    for i, (k, am, o) in enumerate(zip(keys, amount, ok)):
        learned = "ít ỏi" if am == "ít" else "nhiều"
        core = (f"hiểu ý nghĩa, hiểu Giáo Pháp của điều đã học {learned} ấy rồi thực hành Giáo Pháp theo đúng Giáo "
                "Pháp")
        so = (f"Người ấy {core}{V_DHAMMANU if i == 0 else ''}." if o else
              f"Người ấy không phải là người {core}{V_DHAMMANU if i == 0 else ''}.")
        ls.append(f"{qk(N(k))} {IDH} học được {am} điều: {NINE}. {so} {ev(N(k))}")
    out.append(S.seg(*ls[:-1], ls[-1] + " ^4-189"))

    # 30: recluses
    sakad = (f"{IDH} nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham đắm, sân hận và si mê mà trở "
             f"thành {N('sakadāgāmī')}, và sau khi trở lại thế gian này chỉ một lần, người ấy {S.DUKKHASSANTA}")  # = ^4-34
    out.append(S.seg(
        f"{q(N('samaṇamacalo'))} {S.SOTAPANNA_INTRO}. {cs(N('samaṇamacalo'))}",
        f"{q(N('samaṇapadumo'))} {sakad}. {cs(N('samaṇapadumo'))}",
        f"{q(N('samaṇapuṇḍarīko'))} {S.ANAGAMI_INTRO}. {cs(N('samaṇapuṇḍarīko'))}",
        f"{q(N('samaṇesu samaṇasukhumālo'))} {arahant} {cs(N('samaṇesu samaṇasukhumālo'))}",
        S.CLOSER_CHAPTER[4] + " ^4-190"))
    return out


def check():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
    bad = [(v, b) for v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails:\n" + "\n".join(map(repr, bad))
    # the samaṇapadumo string equals the approved ch2 ^4-34 wording
    ch2 = (S.OUT_DIR / "2-ekakapuggalapannatti.md").read_text(encoding="utf-8")
    assert "nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham đắm, sân hận và si mê mà trở thành" in ch2
    # identical Pāli in ch4 (Tika, finished by another agent): same Vietnamese
    ch4p = S.OUT_DIR / "4-tikapuggalapannatti.md"
    if ch4p.exists():
        ch4 = unicodedata.normalize("NFC", ch4p.read_text(encoding="utf-8"))
        for s in (LOKA, "người ấy là những ai?", "người này cũng giống như vậy", "thường hay nổi giận",
                  "Và sự giận dữ ấy quả thật nằm sẵn nơi người ấy lâu dài suốt một thời gian dài",
                  "Và sự giận dữ ấy quả thật không nằm sẵn nơi người ấy lâu dài suốt một thời gian dài",
                  "dễ chịu với tai, dễ mến, thấm vào lòng, lịch sự, được nhiều người yêu mến, được nhiều người ưa thích",
                  "có văn từ, và làm sáng tỏ đời sống tu hành trong sạch hoàn toàn đầy đủ, thanh tịnh",
                  "phạm giới, có phẩm chất xấu", "giữ giới, có phẩm chất tốt", KHAYA_A + ", " + KHAYA_B):
            assert s in ch4, ("ch4 string differs", s)


def main():
    check()
    segs = build()
    text = unicodedata.normalize("NFC", "\n\n".join(segs))
    for k, v in NAMES_USED.items():
        assert v in text or S.cap(v) in text or v[len("có người "):] in text, ("name not used verbatim", k, v)
    S.write(OUT, segs)
    if "--adh" in sys.argv:          # byte-identical copy for termbase_adherence_vi.py (rails/adh-5/)
        adh = pathlib.Path(__file__).parent / "adh-5"
        adh.mkdir(exist_ok=True)
        S.write(adh / OUT.name, segs)


if __name__ == "__main__":
    main()
