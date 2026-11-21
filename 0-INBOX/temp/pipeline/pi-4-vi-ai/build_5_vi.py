# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 5: 5-catukkapuggalapannatti.md (Catukkapuggalapaññatti).

Imports the approved sample builder (names, frames, headings, closers) and uses fixed strings for every repeated
frame, list and simile, so every repeat is byte-identical.  run:  python -I -X utf8 build_5_vi.py
Follows the finished chapters 3 and 4 for identical Pāli (simile frames, anger lines, arahant formula, sīla strings).
Asserts: every cross-book string still occurs in the pi-1 / pi-2 / pi-3 rails; every string taken from the sample
(1-matika.md) and from chapter 4 still occurs there; every person name used equals B.NAME and appears in the output.
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402

N = B.NAME
cap, q, close = B.cap, B.q, B.close
IDHE = B.IDHEKACCO                        # Ở đời này, có người
IDHA_PANA = "Ở đời này, lại có"           # Idha panekacco (ch4)
EVAMEVAM = "Cũng như thế,"                # Evamevaṃ (sentence-initial; ch4 / pi-2)
SANTO_LOKE = "đang có mặt, được tìm thấy trong thế gian"   # santo saṃvijjamānā lokasmiṃ (ch4)
KATAME4 = "Bốn hạng nào?"                 # Katame cattāro? (ch4 «Ba hạng nào?»)
TINNO_NAME = N["tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo"]


def tattha_who(x):                        # Tattha katame cattāro X? (ch4)
    return f"Ở đây, {x} là những ai?"


def kq(x):                                # Kathañca puggalo X hoti? (new)
    return f"Người như thế nào là {x}?"


def ev(x):                                # Evaṃ puggalo X hoti. (new)
    return f"Như vậy là {x}."


def seyya(thing, qual):                   # Seyyathāpi so N …, tathūpamo ayaṃ puggalo. (ch4)
    return f"Như {thing} ấy {qual}, người này cũng giống như thế."


def close_lc(name):                       # …, ayaṃ vuccati puggalo "X". (comma, no dash)
    return f"người này được gọi là “{name}”."


def close_nq(x):                          # Ayaṃ vuccati puggalo X. (no dash, no quotes)
    return f"Người này được gọi là {x}."


# ---------------------------------------------------------------- strings from ch4 (asserted in its output)
KUJJHATI = f"{IDHE} thường hay nổi giận."
ANUSETI = "Và sự giận dữ ấy của người ấy nằm sẵn trong lòng lâu dài, suốt một thời gian dài."
NA_ANUSETI = "Và sự giận dữ ấy của người ấy không nằm sẵn trong lòng lâu dài, suốt một thời gian dài."
DUSSILA = "phạm giới, có phẩm chất xấu"   # dussīlo (hoti) pāpadhammo (ch3/ch4)
SILAVA = "giữ giới, có phẩm chất tốt"      # sīlavā (hoti) kalyāṇadhammo (ch3/ch4)
ARAHATTA = ("nhờ sự diệt tận các ô nhiễm, ngay trong đời này tự mình hiểu biết trực tiếp, chứng nghiệm, "
            "chứng nhập và an trú sự giải thoát của tâm, sự giải thoát nhờ trí tuệ, không còn ô nhiễm")
ARAHANT_SENT = f"{IDHE}, {ARAHATTA}"
NELA = ("lời nói nào không có lỗi, dễ chịu với tai, dễ mến, thấm vào lòng, lịch sự, được nhiều người yêu mến, "
        "được nhiều người ưa thích")      # yā sā vācā nelā … (pi-1 ^1-135, ch4)
DESANA_BODY = ("Giáo Pháp tốt đẹp ở phần đầu, tốt đẹp ở phần giữa, tốt đẹp ở phần cuối, đúng ý nghĩa và đúng văn "
               "từ, làm sáng tỏ đời sống tu hành trong sạch hoàn toàn đầy đủ, hoàn toàn thanh tịnh")  # ch4
CH4_CHECK = [KUJJHATI, ANUSETI, NA_ANUSETI, DUSSILA, SILAVA, ARAHATTA, NELA, DESANA_BODY, SANTO_LOKE,
             "người này cũng giống như thế.", "Ở đây, ba hạng người giống như", "là những ai?", "Ba hạng nào?",
             "Cũng như thế, ba hạng người giống như", "Đây là ba hạng người giống như",
             "từ bỏ việc nói dối, kiêng tránh việc nói dối", "Ở đời này, lại có", "Giống như"]

# ---------------------------------------------------------------- sample strings (1-matika.md, catukka)
NV = "không xem xét, không tìm hiểu thấu đáo mà"
AV = "xem xét, tìm hiểu thấu đáo rồi"
PRAISE_BLAME = "nói lời khen ngợi người đáng chê trách"
BLAME_PRAISE = "nói lời chê trách người đáng khen ngợi"
BLAME_BLAME = "nói lời chê trách người đáng chê trách"
PRAISE_PRAISE = "nói lời khen ngợi người đáng khen ngợi"
TRUST_NO = "bày tỏ lòng tin trong sáng ở nơi không đáng có lòng tin trong sáng"
DISTRUST_YES = "bày tỏ sự thiếu lòng tin trong sáng ở nơi đáng có lòng tin trong sáng"
DISTRUST_NO = "bày tỏ sự thiếu lòng tin trong sáng ở nơi không đáng có lòng tin trong sáng"
TRUST_YES = "bày tỏ lòng tin trong sáng ở nơi đáng có lòng tin trong sáng"
BTK = "đúng sự thật, chính xác, đúng lúc"
AH = ["thực hành vì lợi ích của bản thân, không vì lợi ích của người khác",
      "thực hành vì lợi ích của người khác, không vì lợi ích của bản thân",
      "thực hành vì lợi ích của bản thân và vì lợi ích của người khác",
      "không thực hành vì lợi ích của bản thân cũng không vì lợi ích của người khác"]
AT = ["tự hành hạ bản thân, chuyên tâm thực hành việc hành hạ bản thân",
      "hành hạ người khác, chuyên tâm thực hành việc hành hạ người khác",
      "vừa tự hành hạ bản thân, chuyên tâm thực hành việc hành hạ bản thân, vừa hành hạ người khác, "
      "chuyên tâm thực hành việc hành hạ người khác",
      "không tự hành hạ bản thân, không chuyên tâm thực hành việc hành hạ bản thân, không hành hạ người khác, "
      "không chuyên tâm thực hành việc hành hạ người khác"]
AT_SO_A = ("Người ấy, không tự hành hạ bản thân, không hành hạ người khác, ngay trong đời này sống không còn đói "
           "khát, đã lắng dịu, đã trở nên mát mẻ")
AT_SO_B = ", cảm nhận hạnh phúc, với bản thân đã trở nên cao thượng."
AT_SO = AT_SO_A + AT_SO_B                 # So anattantapo aparantapo diṭṭheva dhamme … viharati.
SM = ["có được sự tĩnh lặng của tâm ở nơi bản thân, không có được sự thấu suốt các hiện tượng nhờ trí tuệ cao thượng",
      "có được sự thấu suốt các hiện tượng nhờ trí tuệ cao thượng, không có được sự tĩnh lặng của tâm ở nơi bản thân",
      "có được sự tĩnh lặng của tâm ở nơi bản thân và có được sự thấu suốt các hiện tượng nhờ trí tuệ cao thượng",
      "không có được sự tĩnh lặng của tâm ở nơi bản thân, cũng không có được sự thấu suốt các hiện tượng nhờ trí "
      "tuệ cao thượng"]
DHAMMAKATHIKA = "người thuyết giảng Giáo Pháp"
MATIKA = (B.OUT_DIR / "1-matika.md").read_text(encoding="utf-8")
MATIKA_CHECK = [NV, AV, PRAISE_BLAME, BLAME_PRAISE, BLAME_BLAME, PRAISE_PRAISE, TRUST_NO, DISTRUST_YES,
                DISTRUST_NO, TRUST_YES, BTK, "Bốn hạng người thuyết giảng Giáo Pháp.", AT_SO_A, AT_SO_B,
                "Có người " + "; có người ".join(AH) + ".",
                "Có người " + "; có người ".join(AT) + ".",
                "Có người " + "; có người ".join(SM) + "."]

# ---------------------------------------------------------------- cross-book strings (pi-1 / pi-2)
SACCA = B.SACCA_PAJANATI                  # hiểu rõ đúng như thật: “Đây là khổ đau”, … khổ đau”.
SACCA_NEG = SACCA.replace("hiểu rõ", "không hiểu rõ")
SACCA_PE = "hiểu rõ đúng như thật: “Đây là khổ đau”… hiểu rõ đúng như thật: “Đây là cách thực hành dẫn đến sự chấm dứt khổ đau”."
SACCA_PE_NEG = SACCA_PE.replace("hiểu rõ", "không hiểu rõ")
ANGA = ("kinh, văn xuôi xen kệ, lời giải thích, kệ, lời cảm hứng, lời đã được nói như vậy, chuyện tiền thân, "
        "chuyện kỳ diệu chưa từng có, lời vấn đáp")                     # pi-2 ^paṭisambhidā (suttaṃ geyyaṃ …)
SURA = "dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"   # pi-2 ^2-703
BAD = {  # agent forms (self) / what others are urged to (samādapeti)
    "pana": "sát hại sinh mạng", "adinna": "lấy của không được cho",
    "kama": "có hành vi sai trái trong các dục lạc", "musa": "nói dối", "sura": SURA,
    "pisuna": "nói lời chia rẽ", "pharusa": "nói lời thô ác", "sampha": "nói lời phù phiếm",
    "abhijjha": "có sự thèm muốn", "byapanna": "có tâm ác ý", "miccha": "có quan điểm sai lầm",
}
OTHERS_BAD = dict(BAD, byapanna="có ác ý")                 # byāpāde samādapeti
GOOD_ABST = {  # refrain-from objects (pi-2 ^2-703 / ^maggaṅga)
    "pana": "việc sát hại sinh mạng", "adinna": "việc lấy của không được cho",
    "kama": "hành vi sai trái trong các dục lạc", "musa": "việc nói dối", "sura": "việc " + SURA,
    "pisuna": "lời nói chia rẽ", "pharusa": "lời nói thô ác", "sampha": "việc nói lời phù phiếm",
}
GOOD_SELF = {k: "kiêng tránh " + v for k, v in GOOD_ABST.items()}
GOOD_SELF.update(abhijjha="không có sự thèm muốn", byapanna="có tâm không ác ý", miccha="có quan điểm đúng đắn")
GOOD_OTHERS = {k: "kiềm chế " + v for k, v in GOOD_ABST.items()}
GOOD_OTHERS.update(abhijjha="không có sự thèm muốn", byapanna="không có ác ý", miccha="có quan điểm đúng đắn")
K5 = ["pana", "adinna", "kama", "musa", "sura"]
K10 = ["pana", "adinna", "kama", "musa", "pisuna", "pharusa", "sampha", "abhijjha", "byapanna", "miccha"]


def bad_pair(k):
    return f"tự mình {BAD[k]} và khuyến khích người khác {OTHERS_BAD[k]}"


def good_pair(k):
    return f"tự mình {GOOD_SELF[k]} và khuyến khích người khác {GOOD_OTHERS[k]}"


# deeds
KAMMA = ["nghiệp bằng thân", "nghiệp bằng lời nói", "nghiệp bằng ý"]   # pi-1 ^1-985
SAV, ANAV = "có lỗi", "không có lỗi"

# the bad / good destinies (pi-2 ^2-830)
DEATH = "khi thân tan rã, sau khi chết,"
APAYA = "tái sinh vào cõi khổ, cõi xấu, nơi đọa lạc, địa ngục"
SUGATI = "tái sinh vào cõi tốt lành, thế giới cõi trời"
DUC = ["hành vi xấu bằng thân", "hành vi xấu bằng lời nói", "hành vi xấu bằng ý"]
SUC = ["hành vi tốt bằng thân", "hành vi tốt bằng lời nói", "hành vi tốt bằng ý"]

# going-forth and monk's training (pi-2 ^2-508 jhānavibhaṅga, pi-1 ^1-1354, pi-2 ^2-829/830)
SAMP_A = ("Vị ấy hành động với sự hiểu biết rõ ràng khi đi tới, khi đi lui; hành động với sự hiểu biết rõ ràng khi "
          "nhìn thẳng, khi nhìn quanh; hành động với sự hiểu biết rõ ràng khi co tay chân")
SAMP_B = (", khi duỗi tay chân; hành động với sự hiểu biết rõ ràng khi mang y ngoài, bình bát và y phục; hành động "
          "với sự hiểu biết rõ ràng khi ăn, khi uống, khi nhai, khi nếm; hành động với sự hiểu biết rõ ràng khi đại "
          "tiện, tiểu tiện; hành động với sự hiểu biết rõ ràng khi đi, khi đứng, khi ngồi, khi ngủ, khi thức, khi "
          "nói, khi im lặng.")
SENASANA = ("vị ấy lui tới chỗ ở thanh vắng: rừng, gốc cây, núi, khe núi, hang núi, bãi tha ma, rừng sâu, khoảng "
            "trời trống, đống rơm")
SITTING = "ngồi xuống, xếp chân kiết già, đặt thân ngay thẳng, thiết lập sự tỉnh thức trước mặt"
NIV = [
    "Sau khi dứt bỏ sự thèm muốn đối với thế gian, vị ấy sống với tâm đã lìa sự thèm muốn, làm trong sạch hoàn "
    "toàn tâm khỏi sự thèm muốn",
    "Sau khi dứt bỏ ác ý và sự sân hận dữ dội, vị ấy sống với tâm không ác ý, thương xót và mong điều lợi ích cho "
    "mọi chúng sinh, muôn loài, làm trong sạch hoàn toàn tâm khỏi ác ý và sự sân hận dữ dội",
    "Sau khi dứt bỏ sự uể oải và đờ đẫn",
    ", vị ấy sống đã lìa sự uể oải và đờ đẫn, có tri giác về ánh sáng, tỉnh thức và hiểu biết rõ ràng, làm trong "
    "sạch hoàn toàn tâm khỏi sự uể oải và đờ đẫn",
    "Sau khi dứt bỏ sự xao động và hối tiếc, vị ấy sống không xao động, có tâm đã lắng dịu hoàn toàn ở nơi bản "
    "thân, làm trong sạch hoàn toàn tâm khỏi sự xao động và hối tiếc",
    "Sau khi dứt bỏ sự hoài nghi, vị ấy sống đã vượt qua sự hoài nghi, không còn băn khoăn đối với các hiện tượng "
    "thiện, làm trong sạch hoàn toàn tâm khỏi sự hoài nghi",
]
JHANA4 = ("Sau khi dứt bỏ năm chướng ngại này, là những thứ làm vẩn đục tâm, làm suy yếu trí tuệ, vị ấy hoàn toàn "
          "tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, chứng nhập và an trú tầng thiền thứ nhất, có sự "
          "hướng tâm và sự duy trì tâm, có sự hân hoan và hạnh phúc sinh từ sự tách biệt; nhờ sự hướng tâm và sự duy "
          "trì tâm lắng xuống, vị ấy chứng nhập và an trú tầng thiền thứ hai, có sự trong sáng ở nơi bản thân, có sự "
          "hợp nhất của tâm, không có sự hướng tâm cũng không có sự duy trì tâm, có sự hân hoan và hạnh phúc sinh từ "
          "định tâm; nhờ sự hân hoan phai nhạt, vị ấy an trú bình thản, tỉnh thức và hiểu biết rõ ràng, cảm nhận hạnh "
          "phúc bằng thân, là trạng thái mà nhờ đó các bậc thánh mô tả người ấy – “Người bình thản, có sự tỉnh thức, "
          "an trú trong hạnh phúc”, chứng nhập và an trú tầng thiền thứ ba; nhờ dứt bỏ sự dễ chịu và dứt bỏ sự khó "
          "chịu, nhờ niềm vui và nỗi buồn đã biến mất từ trước, vị ấy chứng nhập và an trú tầng thiền thứ tư, không "
          "khó chịu cũng không dễ chịu, có sự tỉnh thức hoàn toàn trong sạch nhờ sự bình thản")
INDRIYA_A = ("thì không nắm giữ dấu hiệu tổng quát, không nắm giữ các chi tiết. Nếu sống với năng lực mắt không được "
             "thu thúc thì các hiện tượng xấu ác bất thiện là sự thèm muốn và nỗi buồn có thể tràn vào người ấy, vì "
             "vậy người ấy thực hành để thu thúc năng lực ấy, bảo vệ năng lực mắt, thực hiện sự thu thúc nơi năng "
             "lực mắt")
INDRIYA_B = ("khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng "
             "thân… khi nhận biết đối tượng của ý bằng ý thì không nắm giữ dấu hiệu tổng quát, không nắm giữ các chi "
             "tiết. Nếu sống với năng lực ý không được thu thúc thì các hiện tượng xấu ác bất thiện là sự thèm muốn và "
             "nỗi buồn có thể tràn vào người ấy, vì vậy người ấy thực hành để thu thúc năng lực ấy, bảo vệ năng lực ý, "
             "thực hiện sự thu thúc nơi năng lực ý")
PUBBE_A = ("nhớ lại nhiều đời sống trước theo nhiều cách, cụ thể là – một đời, hai đời, ba đời, bốn đời, năm đời, "
           "mười đời, hai mươi đời, ba mươi đời, bốn mươi đời, năm mươi đời, một trăm đời, một nghìn đời, một trăm "
           "nghìn đời, nhiều kiếp thế giới tan hoại, nhiều kiếp thế giới hình thành, nhiều kiếp thế giới tan hoại và "
           "hình thành")
PUBBE_Q = ("“Ở nơi kia, tôi có tên như vậy, thuộc dòng họ như vậy, có dung mạo như vậy, ăn thức ăn như vậy, cảm nhận "
           "dễ chịu và khó chịu như vậy, có tuổi thọ đến mức như vậy; chết từ nơi ấy, tôi đã sinh ra ở nơi kia; ở nơi "
           "kia, tôi cũng có tên như vậy, thuộc dòng họ như vậy, có dung mạo như vậy, ăn thức ăn như vậy, cảm nhận dễ "
           "chịu và khó chịu như vậy, có tuổi thọ đến mức như vậy; chết từ nơi ấy, tôi đã tái sinh ở đây”")
PUBBE_END = "nhớ lại nhiều đời sống trước theo nhiều cách, với các nét đặc trưng và chi tiết"
DIBBA = "bằng thiên nhãn thanh tịnh, vượt quá mắt người,"
DIBBA_SEE = ("thấy chúng sinh đang chết đi, đang tái sinh, thấp kém, ưu việt, đẹp đẽ, xấu xí, ở cõi tốt lành, ở cõi "
             "xấu, và hiểu rõ các chúng sinh đi theo nghiệp của mình")
DIBBA_Q = ("“Quả thật, những chúng sinh đáng kính này mang hành vi xấu bằng thân, mang hành vi xấu bằng lời nói, mang "
           "hành vi xấu bằng ý, phỉ báng các bậc thánh, có quan điểm sai lầm, thực hiện nghiệp theo quan điểm sai lầm. "
           "Khi thân tan rã, sau khi chết, họ đã tái sinh vào cõi khổ, cõi xấu, nơi đọa lạc, địa ngục. Hoặc những "
           "chúng sinh đáng kính này mang hành vi tốt bằng thân, mang hành vi tốt bằng lời nói, mang hành vi tốt bằng "
           "ý, không phỉ báng các bậc thánh, có quan điểm đúng đắn, thực hiện nghiệp theo quan điểm đúng đắn. Khi thân "
           "tan rã, sau khi chết, họ đã tái sinh vào cõi tốt lành, thế giới cõi trời”")
SAMAHITE = ("Khi tâm đã an định như vậy, trong sạch, trong sáng, không còn vết nhơ, đã lìa các thứ làm vẩn đục, "
            "trở nên mềm dẻo, dễ vận dụng, vững vàng, đạt đến sự bất động, vị ấy hướng tâm đến")
VIJJA = ["sự hiểu biết về sự nhớ lại các đời sống trước", "sự hiểu biết về sự chết và sự tái sinh của chúng sinh",
         "sự hiểu biết về sự diệt tận các ô nhiễm"]                   # pi-1 ^1-1380
AGARA = "khoác những tấm y màu vàng đất, rời bỏ gia đình mà xuất gia sống đời không gia đình"
SAMAPATTI = B.SAMAPATTI_LABHI             # có được các thành tựu thiền đi kèm với hình sắc hoặc …
LOKUTTARA = "có được con đường hoặc thành quả vượt thế gian"           # pi-1 «vượt thế gian»

CROSS = [
    (2, SURA), (2, "việc sát hại sinh mạng"), (2, "việc lấy của không được cho"),
    (2, "hành vi sai trái trong các dục lạc"), (2, "việc nói dối"), (2, "lời nói chia rẽ"), (2, "lời nói thô ác"),
    (2, "việc nói lời phù phiếm"), (2, "Sự thèm muốn, ác ý, quan điểm sai lầm"),
    (2, "Sự kiềm chế việc sát hại sinh mạng"), (2, "sự kiềm chế lời nói chia rẽ"), (2, "đang kiêng tránh việc"),
    (2, "quan điểm đúng đắn"), (2, "với tâm không ác ý"), (1, ", ".join(KAMMA)), (2, ANGA),
    (2, "khi đi tới, khi đi lui"), (2, "khi nhìn thẳng, khi nhìn quanh"), (2, "khi mang y ngoài, bình bát và y phục"),
    (2, "hội chúng"), (2, "với các đạo sĩ ngoại đạo, với đệ tử của các đạo sĩ ngoại đạo"),
    (2, "cách thực hành dẫn đến sự chấm dứt khổ đau"), (2, "chư thiên Tha Hóa Tự Tại"), (2, "chúng sinh địa ngục"),
    (2, DEATH + " " + APAYA), (2, DEATH + " " + SUGATI), (2, DUC[0]), (2, DUC[1]), (2, DUC[2]),
    (2, SUC[0]), (2, SUC[1]), (2, SUC[2]), (2, "quý tộc giàu có"), (2, "bà-la-môn giàu có"),
    (2, "gia chủ giàu có"), (1, "phạm giới"), (2, "người giữ giới"), (2, "gần gũi, kết giao, thân cận"),
    (2, "Sự chú tâm không khôn ngoan"), (1, "sự không thấu hiểu"), (2, SAMP_A), (2, SAMP_B), (2, SENASANA[len("vị ấy "):]),
    (2, SITTING), (2, NIV[0]), (2, NIV[1]), (2, NIV[2] + NIV[3]), (2, NIV[4]), (2, NIV[5]), (2, JHANA4),
    (1, INDRIYA_A), (1, INDRIYA_B[len("khi "):]), (2, PUBBE_A),
    (2, PUBBE_Q), (2, PUBBE_END), (2, DIBBA), (2, DIBBA_SEE), (2, DIBBA_Q), (1, VIJJA[0][4:]), (1, VIJJA[1][4:]),
    (1, VIJJA[2][4:]), (1, "ô nhiễm dục lạc"), (1, "ô nhiễm hiện hữu"), (1, "ô nhiễm vô minh"),
    (2, ARAHATTA.replace("nhờ sự diệt tận các ô nhiễm, ", "")), (2, "an trú bình thản, tỉnh thức và hiểu biết rõ ràng"),
    (1, "vượt thế gian"), (1, "đời sống tu hành trong sạch"), (2, "Giới Luật"),
    (2, "tự mình hiểu biết trực tiếp, chứng nghiệm"), (2, "Như Lai"), (2, "Trung Bộ Kinh"), (2, "Trường Bộ Kinh"),
    (2, "Tăng Chi Bộ Kinh"), (2, "khoảng trời trống"), (1, "sự biết đủ"), (1, "dễ vận dụng"), (2, "sự khó chịu"),
    (1, "nỗi buồn"), (1, "Sự thành tựu về giới hạnh"), (2, "thành tựu thiền"), (1, "Đức Thế Tôn"),
    (1, "bậc Tự Giác Ngộ Hoàn Toàn"), (2, "bậc đạo sư"), (2, "chư thiên"), (2, "loài người"), (2, "Phạm"),
    (1, "sự tham đắm"), (1, "sự sân hận"), (1, "sự si mê"), (1, "sự kiêu mạn"), (2, "nỗ lực"),
    (1, "hiểu biết về sự diệt tận các ô nhiễm"), (2, "sự giải thoát của tâm"), (2, "nhờ trí tuệ"),
]


# ---------------------------------------------------------------- simile block
def simile(key, kind, thing, items, bodies, first_items=None, kind_var="", inline_end=True, q_items=None):
    types = f"bốn hạng người giống như {B.SIMILE[key]}"
    q_items = q_items or items
    L = [f"{tattha_who(types)} Bốn loại {kind}{kind_var} – {', '.join(first_items or items)}. "
         f"{EVAMEVAM} {types} này {SANTO_LOKE}. {KATAME4} {cap(', '.join(items))}."]
    for i in range(4):
        pn = "người " + q_items[i]
        L.append(f"{kq(pn)} {bodies[i]} {ev(pn)} {seyya(thing, q_items[i])}")
    end = f"Đây là {types} {SANTO_LOKE}."
    if inline_end:
        L[-1] += " " + end
    else:
        L.append(end)
    return L


PAS = ("có dáng vẻ đáng mến khi đi tới, khi đi lui, khi nhìn thẳng, khi nhìn quanh, khi co tay chân{v}, khi duỗi "
       "tay chân, khi mang y ngoài, bình bát và y phục")


def pas(neg, v=""):
    return f"{IDHE} {'không ' if neg else ''}{PAS.format(v=v)}."


def truths(neg, pe):
    s = (SACCA_PE_NEG if neg else SACCA_PE) if pe else (SACCA_NEG if neg else SACCA)
    return "Người ấy " + s


def chapter():
    L = ["#### " + B.CHAPTER_HEADING[5]]

    # ^4-132 … ^4-139 bad / good persons
    L.append(f"{q(N['asappuriso'])} {IDHE} {', '.join(BAD[k] for k in K5)} {close(N['asappuriso'])}")
    L.append(f"{q(N['asappurisena asappurisataro'])} {IDHE} {', '.join(bad_pair(k) for k in K5)} "
             f"{close(N['asappurisena asappurisataro'])}")
    L.append(f"{q(N['sappuriso'])} {IDHE} {', '.join(GOOD_SELF[k] for k in K5)} {close(N['sappuriso'])}")
    L.append(f"{q(N['sappurisena sappurisataro'])} {IDHE} {', '.join(good_pair(k) for k in K5)} "
             f"{close(N['sappurisena sappurisataro'])}")
    bad10 = [BAD[k] for k in K10]
    bad10[4] += " [khác chính tả: pisuṇāvāco]"
    bad10[5] += " [khác chính tả (Sī.): pharusāvāco; Trường Bộ Kinh 3.115]"
    bad10[9] += " [khác chính tả (Ka.): micchādiṭṭhī]"
    L.append(f"{q(N['pāpo'])} {IDHE} {', '.join(bad10)} {close(N['pāpo'])}")
    L.append(f"{q(N['pāpena pāpataro'])} {IDHE} {', '.join(bad_pair(k) for k in K10)} {close(N['pāpena pāpataro'])}")
    good10 = [GOOD_SELF[k] for k in K10]
    good10[9] += " [khác chính tả (Ka.): sammādiṭṭhī]"
    L.append(f"{q(N['kalyāṇo'])} {IDHE} {', '.join(good10)} {close(N['kalyāṇo'])}")
    L.append(f"{q(N['kalyāṇena kalyāṇataro'])} {IDHE} {', '.join(good_pair(k) for k in K10)} "
             f"{close(N['kalyāṇena kalyāṇataro'])}")

    # ^4-140 … ^4-143 (…pe…)
    L.append(f"{q(N['pāpadhammo'])} {IDHE} {BAD['pana']}, {BAD['adinna']}… {BAD['miccha']} {close(N['pāpadhammo'])}")
    L.append(f"{q(N['pāpadhammena pāpadhammataro'])} {IDHE} {bad_pair('pana')}, {bad_pair('adinna')}… "
             f"{bad_pair('miccha')} {close(N['pāpadhammena pāpadhammataro'])}")
    L.append(f"{q(N['kalyāṇadhammo'])} {IDHE} {GOOD_SELF['pana']}, {GOOD_SELF['adinna']}… {GOOD_SELF['miccha']} "
             f"{close(N['kalyāṇadhammo'])}")
    L.append(f"{q(N['kalyāṇadhammena kalyāṇadhammataro'])} {IDHE} {good_pair('pana')}… {good_pair('miccha')} "
             f"{close(N['kalyāṇadhammena kalyāṇadhammataro'])}")

    # ^4-144 … ^4-147 blame
    L.append(f"{q(N['sāvajjo'])} {IDHE} {', '.join(f'mang {k} {SAV}' for k in KAMMA)} {close(N['sāvajjo'])}")
    L.append(f"{q(N['vajjabahulo'])} {IDHE} "
             + ", ".join(f"mang nhiều {k} {SAV} mà ít nghiệp {ANAV}" for k in KAMMA) + f" {close(N['vajjabahulo'])}")
    L.append(f"{q(N['appavajjo'])} {IDHE} "
             + ", ".join(f"mang nhiều {k} {ANAV} mà ít nghiệp {SAV}" for k in KAMMA) + f" {close(N['appavajjo'])}")
    L.append(f"{q(N['anavajjo'])} {IDHE} {', '.join(f'mang {k} {ANAV}' for k in KAMMA)} {close(N['anavajjo'])}")

    # ^4-148 … ^4-151 understanding
    ab = "có sự thấu hiểu Giáo Pháp"                          # dhammābhisamayo hoti
    L.append(f"{q(N['ugghaṭitaññū'])} Người mà ngay vào lúc lời dạy vừa được nêu ra đã {ab} "
             f"{close(N['ugghaṭitaññū'])}")
    L.append(f"{q(N['vipañcitaññū'])} Người mà khi ý nghĩa của điều được nói vắn tắt được phân tích chi tiết thì "
             f"{ab} {close(N['vipañcitaññū'])}")
    L.append(f"{q(N['neyyo'])} Người mà nhờ học thuộc, nhờ hỏi han, nhờ chú tâm một cách khôn ngoan, nhờ gần gũi, "
             f"kết giao, thân cận với những người bạn tốt, như vậy dần dần {ab} {close(N['neyyo'])}")
    L.append(f"{q(N['padaparamo'])} Người mà dù nghe nhiều, nói nhiều, ghi nhớ nhiều, dạy người khác tụng đọc nhiều, "
             f"nhưng trong đời sống ấy vẫn không {ab} {close(N['padaparamo'])}")

    # ^4-152 … ^4-155 ready speech
    asked = "khi được hỏi một câu hỏi thì trả lời"
    yq = N['yuttappaṭibhāno no muttappaṭibhāno'].replace(
        "xác đáng", "xác đáng [khác chính tả (Syā.): yuttapaṭibhāṇo; Tăng Chi Bộ Kinh 4.132]", 1)
    L.append(f"Thế nào là {yq}? {IDHE} {asked} xác đáng nhưng không nhanh "
             f"{close(N['yuttappaṭibhāno no muttappaṭibhāno'])}")
    L.append(f"{q(N['muttappaṭibhāno no yuttappaṭibhāno'])} {IDHE} {asked} nhanh nhưng không xác đáng "
             f"{close(N['muttappaṭibhāno no yuttappaṭibhāno'])}")
    L.append(f"{q(N['yuttappaṭibhāno ca muttappaṭibhāno ca'])} {IDHE} {asked} vừa xác đáng vừa nhanh "
             f"{close(N['yuttappaṭibhāno ca muttappaṭibhāno ca'])}")
    L.append(f"{q(N['neva yuttappaṭibhāno no muttappaṭibhāno'])} {IDHE} {asked} không xác đáng cũng không nhanh "
             f"{close(N['neva yuttappaṭibhāno no muttappaṭibhāno'])}")

    # ^4-156 Dhamma speakers (4 lines)
    aud = "còn hội chúng của người ấy {n}thông thạo trong việc phân biệt điều mạch lạc với điều không mạch lạc"
    evr = (f"{cap(DHAMMAKATHIKA)} như vậy, đối với hội chúng như vậy, được kể là {DHAMMAKATHIKA}.")
    L.append(f"{tattha_who('bốn hạng người thuyết giảng Giáo Pháp')} {IDHE} thuyết giảng Giáo Pháp nói ít và không "
             f"mạch lạc, {aud.format(n='không ')}. {evr}")
    L.append(f"{IDHA_PANA} người thuyết giảng Giáo Pháp nói ít và mạch lạc, {aud.format(n='')}. {evr}")
    L.append(f"{IDHA_PANA} người thuyết giảng Giáo Pháp nói nhiều và không mạch lạc, {aud.format(n='không ')}. {evr}")
    L.append(f"{IDHA_PANA} người thuyết giảng Giáo Pháp nói nhiều và mạch lạc, {aud.format(n='')}. {evr} "
             "Đây là bốn “hạng người thuyết giảng Giáo Pháp”.")

    # ^4-157 clouds
    L += simile("valāhaka", "mây mưa", "đám mây mưa",
                ["gầm sấm nhưng không mưa", "mưa nhưng không gầm sấm", "vừa gầm sấm vừa mưa",
                 "không gầm sấm cũng không mưa"],
                [f"{IDHE} nói nhưng không làm.", f"{IDHE} làm nhưng không nói.", f"{IDHE} vừa nói vừa làm.",
                 f"{IDHE} không nói cũng không làm."], inline_end=False)

    # ^4-158 mice
    learn = f"{IDHE} học thuộc Giáo Pháp – {ANGA}."
    nlearn = f"{IDHE} không học thuộc Giáo Pháp – {ANGA}."
    L += simile("mūsika", "chuột", "con chuột",
                ["đào hang nhưng không ở hang", "ở hang nhưng không đào hang", "vừa đào hang vừa ở hang",
                 "không đào hang cũng không ở hang"],
                [f"{learn} {truths(True, False)}", f"{nlearn} {truths(False, False)}",
                 f"{learn} {truths(False, False)}", f"{nlearn} {truths(True, False)}"], inline_end=False)

    # ^4-159 mangoes
    amba = ["xanh mà trông như chín", "chín mà trông như xanh", "xanh và trông như xanh", "chín và trông như chín"]
    amba_first = [amba[0] + " [khác chính tả: pakkavaṇṇī]",
                  amba[1] + " [khác chính tả (Syā., Ka.): āmavaṇṇī; Tăng Chi Bộ Kinh 4.105]", amba[2], amba[3]]
    L += simile("amba", "xoài", "quả xoài", amba,
                [f"{pas(False, ' [khác chính tả (Sī., Syā.): sammiñjitaṃ]')} {truths(True, False)}",
                 f"{pas(True)} {truths(False, False)}", f"{pas(True)} {truths(True, True)}",
                 f"{pas(False)} {truths(False, True)}"], first_items=amba_first, inline_end=False)

    # ^4-160 pots
    L += simile("kumbha", "chum", "cái chum",
                ["rỗng mà được đậy kín", "đầy mà để mở", "rỗng và để mở", "đầy và được đậy kín"],
                [f"{pas(False)} {truths(True, True)}", f"{pas(True)} {truths(False, True)}",
                 f"{pas(True)} {truths(True, True)}", f"{pas(False)} {truths(False, True)}"])

    # ^4-161 pools
    L += simile("udakarahada", "hồ nước", "hồ nước",
                ["cạn mà trông như sâu", "sâu mà trông như cạn", "cạn và trông như cạn", "sâu và trông như sâu"],
                [f"{pas(False)} {truths(True, True)}", f"{pas(True)} {truths(False, True)}",
                 f"{pas(True)} {truths(True, True)}", f"{pas(False)} {truths(False, True)}"])

    # ^4-162 bulls
    own, oth = "hung dữ với đàn của mình", "hung dữ với đàn khác"
    bull = [f"{own} nhưng không {oth}", f"{oth} nhưng không {own}", f"vừa {own} vừa {oth}",
            f"không {own} cũng không {oth}"]
    bull_first = [f"{own} [khác chính tả (Ka., Sī.): sagavacaṇḍo; Tăng Chi Bộ Kinh 4.108] nhưng không {oth}"] + bull[1:]
    so, sp = "làm cho hội chúng của mình sợ hãi", "làm cho hội chúng của người khác sợ hãi"
    L += simile("balībadda", "bò đực", "con bò đực", bull,
                [f"{IDHE} {so}, nhưng không {sp}.", f"{IDHE} {sp}, nhưng không {so}.",
                 f"{IDHE} vừa {so}, vừa {sp}.", f"{IDHE} không {so} cũng không {sp}."],
                first_items=bull_first, kind_var=" [khác chính tả (Syā.): balibaddhā]")

    # ^4-163 snakes
    fast, fierce = "phát nhanh", "dữ dội"
    snake = [f"có nọc độc {fast} nhưng không {fierce}", f"có nọc độc {fierce} nhưng không {fast}",
             f"có nọc độc vừa {fast} vừa {fierce}", f"có nọc độc không {fast} cũng không {fierce}"]
    nk = f"{IDHE} quả thật không{{v}} thường hay nổi giận."
    L += simile("āsīvisa", "rắn độc", "con rắn độc", snake,
                [f"{KUJJHATI} {NA_ANUSETI}",
                 f"{nk.format(v=' [khác chính tả (Sī.): neva kho; Tăng Chi Bộ Kinh 4.110]')} {ANUSETI}",
                 f"{KUJJHATI} {ANUSETI}", f"{nk.format(v='')} {NA_ANUSETI}"],
                kind_var=" [khác chính tả (Syā.): āsivisā]")

    # ^4-164 / ^4-165 praise and blame
    for adv, items, eff in (
        (NV, [PRAISE_BLAME, BLAME_PRAISE, TRUST_NO, DISTRUST_YES], 0),
        (AV, [BLAME_BLAME, PRAISE_PRAISE, DISTRUST_NO, TRUST_YES], 1),
    ):
        bad_p = "các đạo sĩ ngoại đạo và các đệ tử của các đạo sĩ ngoại đạo, là những người thực hành tồi tệ, thực hành sai lầm"
        good_p = "các vị Phật và các đệ tử của Phật, là những người thực hành tốt đẹp, thực hành đúng đắn"
        good_q = "rằng họ là “những người thực hành tốt đẹp”, là “những người thực hành đúng đắn”."
        bad_q = "rằng họ là “những người thực hành tồi tệ”, là “những người thực hành sai lầm”."
        bad_w = "cách thực hành tồi tệ, cách thực hành sai lầm"
        good_w = "cách thực hành tốt đẹp, cách thực hành đúng đắn"
        good_wq = "rằng đó là “cách thực hành tốt đẹp”, là “cách thực hành đúng đắn”."
        bad_wq = "rằng đó là “cách thực hành tồi tệ”, là “cách thực hành sai lầm”."
        if eff == 0:
            bodies = [f"nói lời khen ngợi {bad_p} – {good_q}", f"nói lời chê trách {good_p} – {bad_q}",
                      f"làm phát sinh lòng tin trong sáng đối với {bad_w} – {good_wq}",
                      f"làm phát sinh sự thiếu lòng tin trong sáng đối với {good_w} – {bad_wq}"]
        else:
            bodies = [f"nói lời chê trách {bad_p} – {bad_q}", f"nói lời khen ngợi {good_p} – {good_q}",
                      f"làm phát sinh sự thiếu lòng tin trong sáng đối với {bad_w} – {bad_wq}",
                      f"làm phát sinh lòng tin trong sáng đối với {good_w} – {good_wq}"]
        for it, body in zip(items, bodies):
            pn = f"người {adv} {it}"
            L.append(f"{kq(pn)} {IDHE} {body} {ev(pn)}")

    # ^4-166 truthful speech
    found = f"{IDHE} nhận thấy có điều đáng khen và cũng có điều đáng chê."
    say = "điều {w} nào ở đó thì người ấy {neg}nói ra, " + BTK
    q1 = f"người {BLAME_BLAME}, {BTK}, nhưng không {PRAISE_PRAISE}, {BTK}"
    q2 = f"người {PRAISE_PRAISE}, {BTK}, nhưng không {BLAME_BLAME}, {BTK}"
    q3 = f"người vừa {BLAME_BLAME}, {BTK}, vừa {PRAISE_PRAISE}, {BTK}"
    q4 = f"người không {BLAME_BLAME}, {BTK}, cũng không {PRAISE_PRAISE}, {BTK}"
    L.append(f"{kq(q1)} {found} {cap(say.format(w='đáng chê', neg=''))}; {say.format(w='đáng khen', neg='không ')}. "
             f"{ev(q1)}")
    L.append(f"{kq(q2)} {found} {cap(say.format(w='đáng khen', neg=''))}; {say.format(w='đáng chê', neg='không ')}. "
             f"{ev(q2)}")
    L.append(f"{kq(q3)} {found} {cap(say.format(w='đáng chê', neg=''))}; {say.format(w='đáng khen', neg='cũng ')}. "
             f"Ở đó, người ấy biết đúng lúc để trả lời câu hỏi ấy. {ev(q3)}")
    L.append(f"{kq(q4)} {found} {cap(say.format(w='đáng chê', neg='không '))}; "
             f"{say.format(w='đáng khen', neg='cũng không ')}. Người ấy an trú bình thản, tỉnh thức và hiểu biết rõ "
             f"ràng. {ev(q4)}")

    # ^4-167 livelihood
    u1, u2, u3, u4 = (N[k] for k in ("uṭṭhānaphalūpajīvī no puññaphalūpajīvī", "puññaphalūpajīvī no uṭṭhānaphalūpajīvī",
                                     "uṭṭhānaphalūpajīvī ca puññaphalūpajīvī ca",
                                     "neva uṭṭhānaphalūpajīvī no puññaphalūpajīvī"))
    eff = "Người mà sinh kế phát sinh nhờ ra sức, cố gắng, nỗ lực"
    L.append(f"{q(u1)} {eff}, chứ không nhờ phước {close(u1)}")
    L.append(f"{q(u2)} Chư thiên Tha Hóa Tự Tại [khác chính tả (Sī., Syā.): paranimmitavasavattideve] và chư thiên ở "
             f"các cõi cao hơn là những {u2}.")
    L.append(f"{q(u3)} {eff} và cả nhờ phước {close(u3)}")
    L.append(f"{q(u4)} Chúng sinh địa ngục là những {u4}.")

    # ^4-168 darkness and light
    low = (f"{IDHE} tái sinh trong gia đình thấp kém – gia đình hạ tiện, hoặc gia đình thợ săn, hoặc gia đình thợ "
           "đan tre{v1}, hoặc gia đình thợ đóng xe, hoặc gia đình người dọn rác, nghèo khổ{v2}, thiếu thức ăn thức "
           "uống, sống chật vật, nơi mà cơm ăn áo mặc chỉ có được một cách khó khăn. Và người ấy xấu xí, khó coi, "
           "thấp lùn, nhiều bệnh tật, hoặc chột mắt, hoặc cụt tay, hoặc què chân, hoặc bại liệt, không có được thức "
           "ăn, thức uống, y phục, xe cộ, vòng hoa, hương thơm, dầu thoa, giường nằm, chỗ ở và đèn đuốc.")
    high = (f"{IDHE} tái sinh trong gia đình cao quý – gia đình quý tộc giàu có, hoặc gia đình bà-la-môn giàu có, "
            "hoặc gia đình gia chủ giàu có, sung túc, nhiều tài sản, nhiều của cải, nhiều vàng bạc, nhiều vật dụng, "
            "nhiều tiền bạc và lúa gạo. Và người ấy đẹp đẽ, dễ nhìn, đáng mến, mang vẻ đẹp tuyệt vời của nước da, có "
            "được thức ăn, thức uống, y phục, xe cộ, vòng hoa, hương thơm, dầu thoa, giường nằm, chỗ ở và đèn đuốc.")

    def conduct(acts, dest):
        a = ", ".join(f"thực hiện {x}" for x in acts)
        return f"Người ấy {a}. Sau khi {a}, {DEATH} người ấy {dest}."

    t1, t2, t3, t4 = (N[k] for k in ("tamo tamaparāyano", "tamo jotiparāyano", "joti tamaparāyano",
                                     "joti jotiparāyano"))
    L.append(f"{kq(t1)} {low.format(v1=' [khác chính tả (Sī., Syā.): veṇakule]', v2=' [khác chính tả (Sī.): daḷidde; xem Tăng Chi Bộ Kinh]')} "
             f"{conduct(DUC, APAYA)} {ev(t1)}")
    L.append(f"{kq(t2)} {low.format(v1='', v2='')} {conduct(SUC, SUGATI)} {ev(t2)}")
    L.append(f"{kq(t3)} {high} {conduct(DUC, APAYA)} {ev(t3)}")
    L.append(f"{kq(t4)} {high} {conduct(SUC, SUGATI)} {ev(t4)}")

    # ^4-169 (…pe…)
    for k in ("oṇatoṇato", "oṇatuṇṇato", "uṇṇatoṇato", "uṇṇatuṇṇato"):
        L.append(f"Người như thế nào là {N[k]}… như vậy là {N[k]}.")

    # ^4-170 trees
    tree = ["không có lõi nhưng xung quanh có lõi", "có lõi nhưng xung quanh không có lõi",
            "không có lõi và xung quanh không có lõi", "có lõi và xung quanh có lõi"]
    L += simile("rukkha", "cây", "cái cây", tree,
                [f"{IDHE} {DUSSILA}, nhưng hội chúng của người ấy {SILAVA}.",
                 f"{IDHE} {SILAVA}, nhưng hội chúng của người ấy {DUSSILA}.",
                 f"{IDHE} {DUSSILA}, và hội chúng của người ấy cũng {DUSSILA}.",
                 f"{IDHE} {SILAVA}, và hội chúng của người ấy cũng {SILAVA}."])

    # ^4-171 / ^4-172 measures
    std = "lấy đó làm thước đo rồi làm phát sinh lòng tin trong sáng"
    for k, body in (
        ("rūpappamāṇo rūpappasanno", "sau khi thấy chiều cao, hoặc sau khi thấy bề ngang, hoặc sau khi thấy hình "
                                     "dáng, hoặc sau khi thấy sự tròn đầy"),
        ("ghosappamāṇo ghosappasanno", "dựa vào lời khen ngợi của người khác, lời tán dương của người khác, lời ca "
                                       "ngợi của người khác, lời truyền tụng tiếng tốt của người khác "
                                       "[khác chính tả (Sī.): paravaṇṇahāriyā]"),
        ("lūkhappamāṇo lūkhappasanno", "sau khi thấy sự đạm bạc của y phục, hoặc sau khi thấy sự đạm bạc của bình "
                                       "bát, hoặc sau khi thấy sự đạm bạc của chỗ ở, hoặc sau khi thấy các loại khổ "
                                       "hạnh khó làm khác nhau"),
        ("dhammappamāṇo dhammappasanno", "sau khi thấy giới hạnh, hoặc sau khi thấy định tâm, hoặc sau khi thấy "
                                         "trí tuệ"),
    ):
        L.append(f"{q(N[k])} {IDHE}, {body}, {std}. {close_nq(N[k])}")

    # ^4-173 own / others' welfare
    five = ["giới hạnh", "định tâm", "trí tuệ", "sự giải thoát", "sự hiểu biết và thấy rõ về sự giải thoát"]
    pat = {0: "tự mình thành tựu về {x}, nhưng không khuyến khích người khác thành tựu về {x}",
           1: "tự mình không thành tựu về {x}, nhưng khuyến khích người khác thành tựu về {x}",
           2: "tự mình thành tựu về {x} và khuyến khích người khác thành tựu về {x}",
           3: "tự mình không thành tựu về {x} và không khuyến khích người khác thành tựu về {x}"}
    for i in range(4):
        pn = "người " + AH[i]
        L.append(f"{kq(pn)} {IDHE} {'; '.join(pat[i].format(x=x) for x in five)}. {ev(pn)}")

    # ^4-174 self-tormentor
    a1 = "người " + AT[0]
    L.append(
        f"{kq(a1)} {IDHE} sống lõa thể, buông thả các lề lối, liếm tay [khác chính tả (Syā.): hatthāvalekhano], "
        "không đến khi được mời đến, không dừng lại khi được mời dừng lại, không nhận thức ăn được mang đến, không "
        "nhận thức ăn được làm riêng cho mình, không nhận lời mời thọ thực; người ấy không nhận thức ăn từ miệng "
        "nồi, không nhận từ miệng chảo [khác chính tả (Sī., Syā.): kalopimukhā; Trung Bộ Kinh 2.7], không nhận qua "
        "ngưỡng cửa, không nhận qua cây gậy, không nhận qua chày giã gạo, không nhận từ hai người đang ăn, không "
        "nhận từ người phụ nữ mang thai, không nhận từ người phụ nữ đang cho con bú, không nhận từ người phụ nữ đang "
        "gần gũi đàn ông, không nhận thức ăn quyên góp, không nhận ở nơi có con chó đang chực chờ, không nhận ở nơi "
        "có ruồi bu thành đàn, không nhận cá, không nhận thịt, không uống rượu mạnh, không uống rượu men, không uống "
        "nước cám lên men. Người ấy hoặc chỉ đến một nhà, chỉ nhận một miếng, hoặc chỉ đến hai nhà, chỉ nhận hai "
        "miếng… hoặc chỉ đến bảy nhà, chỉ nhận bảy miếng; sống nhờ một phần thức ăn được cho, sống nhờ hai phần "
        "thức ăn được cho… sống nhờ bảy phần thức ăn được cho; ăn một ngày một lần, ăn hai ngày một lần "
        "[khác chính tả (Sī.): dvāhikampi]… ăn bảy ngày một lần. Như vậy, người ấy sống chuyên tâm thực hành việc "
        "ăn theo định kỳ như thế, cho đến nửa tháng một lần. Người ấy hoặc ăn rau, hoặc ăn kê, hoặc ăn lúa hoang, "
        "hoặc ăn vụn da, hoặc ăn rêu, hoặc ăn cám, hoặc ăn cơm cháy, hoặc ăn bã vừng, hoặc ăn cỏ, hoặc ăn phân bò, "
        "sống nhờ rễ cây và trái cây trong rừng, ăn trái cây tự rụng. Người ấy mặc vải gai, mặc vải sợi pha, mặc vải "
        "liệm tử thi, mặc vải bỏ đi, mặc vải vỏ cây, mặc da linh dương, mặc dải da linh dương, mặc áo bện bằng cỏ, "
        "mặc áo sợi vỏ cây, mặc áo ván gỗ, mặc chăn bằng tóc người, mặc chăn bằng lông đuôi thú, mặc lông cánh chim "
        "cú [khác chính tả (Sī., Syā.): ulukapakkhampi], là người nhổ tóc và râu, chuyên tâm thực hành việc nhổ tóc "
        "và râu, là người đứng mãi, từ chối chỗ ngồi, là người ngồi chồm hổm, chuyên tâm nỗ lực trong tư thế ngồi "
        "chồm hổm, là người nằm trên gai, làm chỗ nằm trên giường gai, sống chuyên tâm thực hành việc xuống nước "
        "ba lần một ngày, lần thứ ba vào buổi chiều [khác chính tả (Syā., Ka.): sāyaṃtatiyakampi; Trung Bộ Kinh "
        "2.7]. Như vậy, người ấy sống chuyên tâm thực hành nhiều cách hành xác, hành hạ thân như thế. " + ev(a1))

    # ^4-175 tormentor of others
    a2 = "người " + AT[1]
    L.append(f"{kq(a2)} {IDHE} là kẻ giết cừu, kẻ giết heo, kẻ bẫy chim, kẻ săn nai, thợ săn, kẻ giết cá, kẻ trộm, "
             "đao phủ giết kẻ trộm, kẻ giết bò, cai ngục, hoặc bất kỳ những người nào khác làm nghề tàn ác. " + ev(a2))

    # ^4-176 both
    a3 = "người " + AT[2]
    L.append(
        f"{kq(a3)} {IDHE} là vua thuộc dòng quý tộc đã làm lễ đăng quang [dị bản (Syā., Ka.): muddhābhisitto], "
        "hoặc là bà-la-môn giàu có. Người ấy cho xây một hội trường mới [khác chính tả (Syā.): santāgāraṃ; dị bản "
        "(Sī.): yaññāgāraṃ] ở phía đông thành phố, cạo bỏ tóc và râu, khoác tấm da thú thô ráp [khác chính tả (Syā., "
        "Ka.): khurājinaṃ], xoa bơ lỏng và dầu lên thân, vừa gãi lưng bằng sừng nai [khác chính tả (Sī.): "
        "kaṇḍūyamāno] vừa đi vào hội trường cùng với hoàng hậu và vị bà-la-môn tế sư. Ở đó, người ấy nằm trên mặt "
        "đất trống được rải cỏ xanh. Từ một con bò cái có con bê cùng màu lông, sữa ở núm vú thứ nhất thì nhà vua "
        "dùng để sống, sữa ở núm vú thứ hai thì hoàng hậu dùng để sống, sữa ở núm vú thứ ba thì vị bà-la-môn tế sư "
        "dùng để sống, sữa ở núm vú thứ tư thì người ấy dùng để cúng tế lửa, phần còn lại thì con bê dùng để sống. "
        "Người ấy nói như sau – “Hãy giết chừng này con bò mộng để tế lễ, hãy giết chừng này con bò tơ đực để tế "
        "lễ, hãy giết chừng này con bò tơ cái để tế lễ, hãy giết chừng này con dê để tế lễ, hãy giết chừng này con "
        "cừu để tế lễ, (hãy giết chừng này con ngựa để tế lễ) [phần trong ngoặc ( ) không có trong bản chép tay "
        "Tích Lan. Trong kinh Kandaraka thuộc Trung Bộ Kinh cũng như vậy] hãy chặt chừng này cây để làm cột tế, hãy "
        "cắt chừng này cỏ để rải nơi tế lễ” [dị bản (Sī., Syā., Ka.): parihiṃsatthāyāti; Trung Bộ Kinh 2.9]. Những "
        "người là nô lệ, người hầu hay người làm công của người ấy, họ cũng bị đe dọa bằng roi gậy, bị đe dọa bằng "
        "sự sợ hãi, mặt đẫm nước mắt, vừa khóc vừa làm các công việc. " + ev(a3))

    # ^4-177 neither (2 lines)
    a4 = "người " + AT[3]
    L.append(f"{kq(a4)} {AT_SO}")
    L.append(
        "Ở đây, Như Lai xuất hiện trong thế gian, là bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn, bậc thành tựu hiểu "
        "biết chân thật và hạnh kiểm, bậc đã khéo đi đến đích, bậc hiểu biết thế gian, bậc dẫn dắt vô song những "
        "người cần được rèn luyện, bậc đạo sư của chư thiên và loài người, bậc Giác Ngộ, Đức Thế Tôn. Ngài tự mình "
        "hiểu biết trực tiếp, chứng nghiệm rồi tuyên bố về thế gian này cùng với chư thiên, Ma vương và Phạm thiên, "
        "về chúng sinh cùng với các sa-môn và bà-la-môn, chư thiên và loài người. Ngài thuyết giảng "
        f"{DESANA_BODY}. Một gia chủ, hoặc con trai của gia chủ, hoặc người sinh ra trong một gia đình nào đó, nghe "
        "Giáo Pháp ấy. Sau khi nghe Giáo Pháp ấy, người ấy có được niềm tin nơi Như Lai. Được trang bị niềm tin có "
        "được ấy, người ấy suy xét như sau – “Đời sống gia đình chật hẹp, là con đường đầy bụi bặm; đời sống xuất "
        "gia rộng mở như khoảng trời trống. Người sống trong gia đình không dễ gì sống đời sống tu hành trong sạch "
        "hoàn toàn đầy đủ, hoàn toàn thanh tịnh, trắng tinh như vỏ ốc được đánh bóng. Hay là tôi hãy cạo bỏ tóc và "
        f"râu, {AGARA}”! Một thời gian sau, người ấy từ bỏ khối tài sản nhỏ hoặc từ bỏ khối tài sản lớn, từ bỏ vòng "
        f"thân quyến nhỏ hoặc từ bỏ vòng thân quyến lớn, cạo bỏ tóc và râu, {AGARA}.")

    # ^4-178 moral conduct (7 lines)
    L.append("Khi đã xuất gia như vậy, có được sự tu học và nếp sống của các tỳ-khưu, vị ấy từ bỏ việc sát hại sinh "
             "mạng, kiêng tránh việc sát hại sinh mạng, sống đã bỏ gậy, đã bỏ dao, biết hổ thẹn, có lòng nhân hậu, "
             "thương xót và mong điều lợi ích cho mọi chúng sinh, muôn loài.")
    L.append("Từ bỏ việc lấy của không được cho, vị ấy kiêng tránh việc lấy của không được cho, chỉ lấy những gì "
             "được cho, chỉ mong đợi những gì được cho, sống với bản thân không trộm cắp, đã trở nên trong sạch.")
    L.append("Từ bỏ lối sống không trong sạch, vị ấy sống đời sống trong sạch, sống tránh xa [dị bản (Ka.): "
             "anācārī], kiêng tránh sự giao hợp, thói tục của người thế tục.")
    L.append("Từ bỏ việc nói dối, kiêng tránh việc nói dối, vị ấy nói lời chân thật, gắn bó với sự thật, đáng tin "
             "cậy, đáng tin tưởng, không lừa dối thế gian.")
    L.append("Từ bỏ lời nói chia rẽ, vị ấy kiêng tránh lời nói chia rẽ; nghe điều gì ở đây, không nói lại ở kia để "
             "chia rẽ những người này; hoặc nghe điều gì ở kia, không nói lại với những người này để chia rẽ những "
             "người kia. Như vậy, vị ấy hòa giải những người bị chia rẽ, củng cố tình thân của những người đang hòa "
             "hợp, ưa thích sự hòa hợp, vui thích sự hòa hợp, hoan hỷ trong sự hòa hợp, nói những lời tạo nên sự hòa "
             "hợp.")
    L.append(f"Từ bỏ lời nói thô ác, vị ấy kiêng tránh lời nói thô ác. {cap(NELA)}, thì vị ấy nói loại lời như vậy.")
    L.append("Từ bỏ việc nói lời phù phiếm, vị ấy kiêng tránh việc nói lời phù phiếm, nói đúng lúc, nói đúng sự thật, "
             "nói điều có ý nghĩa, nói về Giáo Pháp, nói về Giới Luật, nói những lời đáng ghi nhớ, đúng lúc, có lý "
             "lẽ, có giới hạn, gắn liền với lợi ích.")

    # ^4-179 (2 lines)
    L.append("Vị ấy kiêng tránh việc làm hại hạt giống và cây cỏ, chỉ ăn một bữa, không ăn ban đêm, tránh xa việc ăn "
             "sai giờ, kiêng tránh việc xem múa, hát, nhạc và các trò giải trí, kiêng tránh việc đeo vòng hoa, dùng "
             "hương thơm, dầu thoa, trang sức và tô điểm, kiêng tránh giường cao và giường lớn, kiêng tránh việc "
             "nhận vàng bạc.")
    L.append("Vị ấy kiêng tránh việc nhận ngũ cốc chưa nấu, kiêng tránh việc nhận thịt sống, kiêng tránh việc nhận "
             "phụ nữ và thiếu nữ, kiêng tránh việc nhận nô tỳ nữ và nô lệ nam, kiêng tránh việc nhận dê và cừu, kiêng "
             "tránh việc nhận gà và heo, kiêng tránh việc nhận voi, bò, ngựa đực và ngựa cái, kiêng tránh việc nhận "
             "ruộng đất và đất đai, kiêng tránh việc làm người đưa tin và chạy việc vặt, kiêng tránh việc mua bán, "
             "kiêng tránh việc gian lận bằng cân, gian lận bằng tiền đồng, gian lận bằng thước đo, kiêng tránh những "
             "thủ đoạn quanh co như hối lộ, lừa đảo và gian trá [khác chính tả (Syā., Ka.): … sāviyogā], kiêng tránh "
             "việc chặt chém, giết hại, giam cầm, cướp đường, cướp bóc và bạo lực.")

    # ^4-180 contentment
    cont = "vị ấy biết đủ với y phục để che thân, với thức ăn khất thực để nuôi bụng"
    go = "Đi đến bất cứ nơi đâu, vị ấy cũng chỉ mang theo những thứ ấy mà đi"
    L.append(f"{cap(cont)}. {go}, giống như con chim có cánh, bay đến bất cứ nơi đâu cũng chỉ mang theo đôi cánh của "
             f"mình mà bay. {EVAMEVAM} vị tỳ-khưu biết đủ với y phục để che thân, với thức ăn khất thực để nuôi bụng. "
             f"{go}. Được trang bị khối giới hạnh cao quý này, vị ấy cảm nhận ở nơi bản thân niềm hạnh phúc không "
             "có lỗi.")

    # ^4-181 sense restraint
    L.append(f"Vị ấy khi thấy hình sắc bằng mắt {INDRIYA_A}; {INDRIYA_B}. Được trang bị sự thu thúc các giác quan cao "
             "quý này, vị ấy cảm nhận ở nơi bản thân niềm hạnh phúc không bị vẩn đục.")

    # ^4-182 (2 lines)
    L.append(SAMP_A + SAMP_B)
    L.append("Được trang bị khối giới hạnh cao quý này, được trang bị sự thu thúc các giác quan cao quý này, được "
             "trang bị sự tỉnh thức và hiểu biết rõ ràng cao quý này, được trang bị sự biết đủ cao quý này [xem "
             "Trung Bộ Kinh 2, kinh Kandaraka; Tăng Chi Bộ Kinh 1, kinh Attantapa], "
             f"{SENASANA}. Sau bữa ăn, khi đã đi khất thực trở về, vị ấy {SITTING}. "
             + "; ".join([NIV[0], NIV[1].replace("Sau", "sau", 1),
                          NIV[2].replace("Sau", "sau", 1) + " [khác chính tả (Sī., Syā.): thīnamiddhaṃ]" + NIV[3],
                          NIV[4].replace("Sau", "sau", 1), NIV[5].replace("Sau", "sau", 1)]) + ".")

    # ^4-183 (2 lines)
    L.append(JHANA4 + ".")
    L.append(f"{SAMAHITE} {VIJJA[0]}. Vị ấy {PUBBE_A} – {PUBBE_Q}. Như vậy, vị ấy {PUBBE_END}.")

    # ^4-184
    L.append(f"{SAMAHITE} {VIJJA[1]}. {cap(DIBBA)} vị ấy {DIBBA_SEE} – {DIBBA_Q}. Như vậy, {DIBBA} vị ấy "
             f"{DIBBA_SEE}.")

    # ^4-185
    asava = ("hiểu rõ đúng như thật: “Đây là các ô nhiễm”, hiểu rõ đúng như thật: “Đây là sự phát sinh của các ô "
             "nhiễm”, hiểu rõ đúng như thật: “Đây là sự chấm dứt các ô nhiễm”, hiểu rõ đúng như thật: “Đây là cách "
             "thực hành dẫn đến sự chấm dứt các ô nhiễm”.")
    L.append(f"{SAMAHITE} {VIJJA[2]}. Vị ấy {SACCA[:-1]}, {asava} Khi vị ấy biết như vậy, thấy như vậy, tâm được "
             "giải thoát khỏi ô nhiễm dục lạc, tâm được giải thoát khỏi ô nhiễm hiện hữu, tâm được giải thoát khỏi ô "
             "nhiễm vô minh. Khi tâm đã được giải thoát, có sự hiểu biết rằng đã được giải thoát. Vị ấy hiểu rõ: "
             "“Sự sinh đã diệt tận, đời sống tu hành trong sạch đã được sống trọn, việc cần làm đã làm xong, không "
             f"còn trở lại trạng thái này nữa”. {ev(a4)} {AT_SO}")

    # ^4-186 passion etc.
    for k, noun in (("sarāgo", "sự tham đắm"), ("sadoso", "sự sân hận"), ("samoho", "sự si mê"),
                    ("samāno", "sự kiêu mạn")):
        L.append(f"{q(N[k])} Người mà {noun} chưa được dứt bỏ, {close_lc(N[k])}")

    # ^4-187 calm and insight
    bodies = [f"{SAMAPATTI}, không {LOKUTTARA}", f"{LOKUTTARA}, không {SAMAPATTI}",
              f"{SAMAPATTI}, {LOKUTTARA}", f"không {SAMAPATTI}, cũng không {LOKUTTARA}"]
    for i in range(4):
        pn = "người " + SM[i]
        L.append(f"{kq(pn)} {IDHE} {bodies[i]}. {ev(pn)}")

    # ^4-188 streams
    L.append(f"{q(N['anusotagāmī'])} {IDHE} hưởng thụ các dục lạc và làm nghiệp ác. {close(N['anusotagāmī'], dash=False)}")
    L.append(f"{q(N['paṭisotagāmī'])} {IDHE} không hưởng thụ các dục lạc và không làm nghiệp ác. Người ấy, dù phải "
             "chịu sự khó chịu, dù phải chịu nỗi buồn, dù mặt đẫm nước mắt, khóc lóc, vẫn sống đời sống tu hành trong "
             f"sạch đầy đủ, thanh tịnh. {close(N['paṭisotagāmī'], dash=False)}")
    L.append(f"{q(N['ṭhitatto'])} {B.ANAGAMI_BASE} {close(N['ṭhitatto'], dash=False)}")
    L.append(f"{q(TINNO_NAME)} {ARAHANT_SENT}. {close_nq(TINNO_NAME)}")

    # ^4-189 learning
    ap = [N[k] for k in ("appassuto sutena anupapanno", "appassuto sutena upapanno", "bahussuto sutena anupapanno",
                         "bahussuto sutena upapanno")]
    pos = "Người ấy hiểu ý nghĩa, hiểu Giáo Pháp của điều {a} đã học ấy, và thực hành theo Giáo Pháp một cách phù hợp với Giáo Pháp{v}."
    neg = ("Người ấy không hiểu ý nghĩa, không hiểu Giáo Pháp của điều {a} đã học ấy, và không thực hành theo Giáo "
           "Pháp một cách phù hợp với Giáo Pháp{v}.")
    v = (" [dị bản (Syā.): na dhammamaññāya na dhammānudhammapaṭipanno; dị bản (Ka.): na dhammamaññāya "
         "dhammānudhammappaṭipanno]")
    few, many = f"{IDHE} chỉ học được ít điều: {ANGA}.", f"{IDHE} học được nhiều điều: {ANGA}."
    L.append(f"{kq(ap[0])} {few} {neg.format(a='ít ỏi', v=v)} {ev(ap[0])}")
    L.append(f"{kq(ap[1])} {few} {pos.format(a='ít ỏi', v='')} {ev(ap[1])}")
    L.append(f"{kq(ap[2])} {many} {neg.format(a='nhiều', v='')} {ev(ap[2])}")
    L.append(f"{kq(ap[3])} {many} {pos.format(a='nhiều', v='')} {ev(ap[3])}")

    # ^4-190 recluses
    L.append(f"{q(N['samaṇamacalo'])} {B.SOTAPANNA_BASE}. {close(N['samaṇamacalo'], dash=False)}")
    L.append(f"{q(N['samaṇapadumo'])} {IDHE}, nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham đắm, "
             f"sân hận và si mê, là {N['sakadāgāmī']}, chỉ trở lại thế gian này một lần rồi đi đến tận cùng của khổ "
             f"đau. {close(N['samaṇapadumo'], dash=False)}")
    L.append(f"{q(N['samaṇapuṇḍarīko'])} {B.ANAGAMI_BASE} {close(N['samaṇapuṇḍarīko'], dash=False)}")
    L.append(f"{q(N['samaṇesu samaṇasukhumālo'])} {ARAHANT_SENT}. {close(N['samaṇesu samaṇasukhumālo'], dash=False)}")
    L.append(B.NIDDESA_CLOSER[4])
    return L


def check_sources():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    cross = CROSS
    missing = [(b, s[:60]) for b, s in cross if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    ch2 = (B.OUT_DIR / "2-ekakapuggalapannatti.md").read_text(encoding="utf-8")
    for s in (B.SOTAPANNA_BASE, B.ANAGAMI_BASE, "nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham "
              "đắm, sân hận và si mê, là bậc trở lại một lần, chỉ trở lại thế gian này một lần rồi đi đến tận cùng "
              "của khổ đau"):
        assert s in ch2, "ch2 string not found: " + s[:60]
    for m in MATIKA_CHECK:
        assert m in MATIKA, "matrix string not found: " + m[:60]
    ch4 = (B.OUT_DIR / "4-tikapuggalapannatti.md").read_text(encoding="utf-8")
    for s in CH4_CHECK:
        assert s in ch4, "ch4 string not found: " + s[:60]
    return len(cross)


def main():
    n = check_sources()
    lines = chapter()
    name = "5-catukkapuggalapannatti.md"
    text = B.assemble(name, lines)
    (B.OUT_DIR / name).write_bytes(text.encode("utf-8"))
    # every Catukka name of B.NAME is used verbatim in the chapter
    for p, v in B.CATUKKA_NAMES.items():
        assert v == B.NAME[p], p
        assert v in text, p
    quoted = [k for k in B.CATUKKA_NAMES if k not in (
        "tamo tamaparāyano", "tamo jotiparāyano", "joti tamaparāyano", "joti jotiparāyano", "oṇatoṇato",
        "oṇatuṇṇato", "uṇṇatoṇato", "uṇṇatuṇṇato", "rūpappamāṇo rūpappasanno", "ghosappamāṇo ghosappasanno",
        "lūkhappamāṇo lūkhappasanno", "dhammappamāṇo dhammappasanno", "tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo",
        "puññaphalūpajīvī no uṭṭhānaphalūpajīvī", "neva uṭṭhānaphalūpajīvī no puññaphalūpajīvī",
        "appassuto sutena anupapanno", "appassuto sutena upapanno", "bahussuto sutena anupapanno",
        "bahussuto sutena upapanno")]
    for k in quoted:
        assert f"“{N[k]}”" in text, k
    for s in ("valāhaka", "mūsika", "amba", "kumbha", "udakarahada", "balībadda", "āsīvisa", "rukkha"):
        assert f"bốn hạng người giống như {B.SIMILE[s]}" in text, s
    for bad in ("—", ":-", "chánh niệm", "….", "seed"):
        assert bad not in text, bad
    print(f"OK: cross-book strings {n}; matrix {len(MATIKA_CHECK)}; ch4 {len(CH4_CHECK)}; wrote {name} "
          f"({len(lines)} lines)")


if __name__ == "__main__":
    main()
