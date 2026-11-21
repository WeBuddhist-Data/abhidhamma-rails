"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 3, Dukapuggalapaññatti (^4-1-2-0, ^4-45 .. ^4-90).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/3-dukapuggalapannatti.md from fixed strings.
Imports the approved sample constants READ-ONLY (build_rails_sample_vi as S; importing writes nothing).
At build time: every string marked (pi-1) / (pi-2) in REUSED is asserted to occur in that book's approved Vietnamese
rails; every person name used equals S.NAME.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-3.md.

usage: python -I -X utf8 build_rails_3_vi.py
"""
import pathlib
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

OUT = S.OUT_DIR / "3-dukapuggalapannatti.md"


def N(k):
    return S.NAME[k]


# ---------------------------------------------------------------------------------------------------------------
# Frames of the duka definitions (new for ch3, see notes-rails-3.md)
# ---------------------------------------------------------------------------------------------------------------
def tattha(x):                      # Tattha katamo X?
    return f"Ở đây, {x} là gì?"


def goi(x):                         # – ayaṃ / idaṃ vuccati X.   (no quotes in the Pāli)
    return f"– đó được gọi là {x}."


def yassa_app(x):                   # Yassa puggalassa ayaṃ X appahīno
    return f"Người nào có {x} này chưa được dứt bỏ"


def yassa_pah(x):                   # Yassa puggalassa ayaṃ X pahīno
    return S.YASSA_PAHINA.format(f"{x} này")


def mang(x, name):                  # Iminā X samannāgato puggalo "Y".   (bad state)
    return f"Người mang {x} này là “{name}”."


def trangbi(x, name):               # Imāya X samannāgato puggalo "Y".   (quality)
    return f"Người được trang bị {x} này là “{name}”."


def dash_name(name):                # – ayaṃ vuccati puggalo "X".
    return S.close_dash(name)


# variant notes
V_DUSANA = " [khác chính tả (Syā.): dūsanā dūsitattaṃ]"
V_ATHAPANA = " [khác chính tả (Ka.): āṭhapanā; xem “Phân tích các hiện tượng” 891]"
V_MAKKHI = " [khác chính tả (Sī.): makkhīyanā makkhīyitattaṃ; (Ka.): makkhiyanā makkhiyitattaṃ]"
V_USSUYA = " [khác chính tả (Ka.): ussuyā ussuyanā; xem “Phân tích các hiện tượng” 893]"
V_KAKKHALA = (" [dị bản (Syā.): kakkhaḷatā kakkhaḷiyaṃ; cũng như vậy trong phần giải thích phân loại theo nhóm hai "
              "của “Phân tích các chủ đề nhỏ”]")
V_ASAMGAHANA = " [khác chính tả (Sī., Syā., Ka.): asaṃgāhanā apariyogāhanā]"
V_SUKATA = " [khác chính tả (Sī.): sukaṭadukkaṭānaṃ]"
V_SAMAGGATA = " [dị bản (Ka.): samaggatā]"
V_VIPARIYESA = " [khác chính tả (mọi bản): vipariyesaggāho; cách cấu tạo câu chữ cần xem xét]"
V_PACCEKA = " [dị bản (Sī.): paccekabuddho]"
V_TAPPETA = " [dị bản (Sī.): tappetā ca, ayaṃ vuccati puggalo titto]"

# ---------------------------------------------------------------------------------------------------------------
# Defined qualities (head nouns), from pi-1 / pi-2 rails
# ---------------------------------------------------------------------------------------------------------------
KODHO = "sự giận dữ"
UPANAHO = "sự ôm hận"
MAKKHO = "sự gièm pha"
PALASO = "sự ganh đua"
ISSA = "sự ganh tị"
MACCHARIYA = "sự keo kiệt"
SATHEYYA = "sự gian xảo"
MAYA = "sự xảo trá"
AHIRIKA = "sự không biết hổ thẹn"
ANOTTAPPA = "sự không biết ghê sợ tội lỗi"
HIRI = "sự biết hổ thẹn"
OTTAPPA = "sự biết ghê sợ tội lỗi"
DOVACASSATA = "sự khó dạy bảo"
SOVACASSATA = "sự dễ dạy bảo"
PAPAMITTATA = "sự kết bạn với người xấu"
KALYANAMITTATA = "sự kết bạn với người tốt"
AGUTTADVARATA = "sự không phòng hộ cửa các giác quan"
GUTTADVARATA = "sự phòng hộ cửa các giác quan"
AMATTANNUTA = "sự không biết tiết độ trong ăn uống"
MATTANNUTA = "sự biết tiết độ trong ăn uống"
MUTTHASSACCA = "sự mất tỉnh thức"
SATI = "sự tỉnh thức"
ASAMPAJANNA = "sự thiếu hiểu biết rõ ràng"
SAMPAJANNA = "sự hiểu biết rõ ràng"
SILAVIPATTI = "sự suy đồi về giới hạnh"
DITTHIVIPATTI = "sự suy đồi về quan điểm"
SILASAMPADA = "sự thành tựu về giới hạnh"
DITTHISAMPADA = "sự thành tựu về quan điểm"

# ---------------------------------------------------------------------------------------------------------------
# Synonym lists (pi-1 / pi-2 strings; variant slots as {v})
# ---------------------------------------------------------------------------------------------------------------
KODHA_A = "Điều mà là sự giận dữ, sự khởi giận, trạng thái khởi giận, sự sân hận, sự khởi sân, trạng thái khởi sân"  # (pi-2)
KODHA_B = (", sự thù hằn, sự khởi thù hằn, trạng thái khởi thù hằn, sự chống đối, sự đối nghịch, sự hung dữ, "
           "sự nói năng cộc cằn, sự không hài lòng của tâm")                                                 # (pi-2)
UPANAHA_A = "Lúc trước là sự giận dữ, lúc sau là sự ôm hận."                                                 # (pi-2)
UPANAHA_B = "Điều mà thuộc loại như vậy là sự ôm hận, sự khởi ôm hận, trạng thái khởi ôm hận, sự lưu giữ"     # (pi-2)
UPANAHA_C = (", sự giữ lại, sự giữ chặt, sự nối kết, sự kéo dài liên tục, "
             "sự làm cho sự giận dữ thêm vững chắc")                                                         # (pi-2)
MAKKHA_A = "Điều mà là sự gièm pha, sự khởi gièm pha, trạng thái khởi gièm pha"                              # (pi-2)
MAKKHA_B = ", sự khắc nghiệt, hành động khắc nghiệt"                                                         # (pi-2)
PALASA_A = "Điều mà là sự ganh đua, sự khởi ganh đua"                                                        # (pi-2)
PALASA_B = "sự ôm giữ sự ganh đua, nguyên cớ tranh cãi, sự đòi ngang hàng, sự không chịu buông bỏ"           # (pi-2)
PALASA = PALASA_A + ", trạng thái khởi ganh đua, " + PALASA_B          # + paḷāsāyitattaṃ (not in the pi-2 text)
ISSA_A = ("Điều mà, trước lợi lộc, sự tôn vinh, sự kính trọng, sự quý trọng, sự đảnh lễ và sự cúng dường mà "
          "người khác nhận được, là sự ganh tị, sự khởi ganh tị, trạng thái khởi ganh tị, sự đố kỵ, sự khởi đố kỵ")  # (pi-2)
ISSA_B = ", trạng thái khởi đố kỵ"                                                                         # (pi-2)
MACCHARIYA_A = ("Năm loại keo kiệt – keo kiệt về chỗ ở, keo kiệt về gia đình, keo kiệt về lợi lộc, "
                "keo kiệt về lời khen, keo kiệt về Giáo Pháp.")                                            # (pi-2)
MACCHARIYA_B = ("Điều mà thuộc loại như vậy là sự keo kiệt, sự khởi keo kiệt, trạng thái khởi keo kiệt, "
                "sự bủn xỉn, sự hà tiện, sự bo bo, trạng thái khép chặt")                                  # (pi-2)
SATHEYYA_A = "Ở đời này, có người gian trá, rất gian trá."                                                   # (pi-2)
SATHEYYA_B = ("Điều mà, ở đây, là sự gian trá, tính gian trá, sự gian xảo, sự xảo quyệt, "
              "tính xảo quyệt")                                                                            # (pi-2)
SATHEYYA_C = ", sự quanh co, tính quanh co"                                                                 # (pi-2)
MAYA_A = ("Ở đời này, có người sau khi làm hành vi xấu bằng thân, sau khi làm hành vi xấu bằng lời nói, sau khi "
          "làm hành vi xấu bằng ý, vì muốn che giấu điều đó mà đặt ra ước muốn xấu xa")                    # (pi-2)
JANNA = "“Mong người ta đừng biết về tôi”"                                                                 # (pi-2)
MAYA_B = (f"– người ấy mong muốn {JANNA}, người ấy suy tính {JANNA}, người ấy nói lời {JANNA}, "
          f"người ấy hành động bằng thân {JANNA}.")
MAYA_C = ("Điều mà thuộc loại như vậy là sự xảo trá, tính xảo trá, sự lấn lướt, sự lừa dối, sự gian lận, "
          "sự đánh lạc hướng, sự lảng tránh, sự giấu giếm, sự giấu giếm kỹ, sự che đậy, sự che giấu, "
          "sự không bày tỏ, sự không bộc lộ, sự che đậy hoàn toàn, việc làm xấu ác")                      # (pi-2)
AHIRIKA_D = ("Điều mà là sự không hổ thẹn trước điều đáng hổ thẹn, sự không hổ thẹn nếu để các hiện tượng xấu ác "
             "bất thiện xảy ra nơi mình")                                                                  # (pi-1)
ANOTTAPPA_D = ("Điều mà là sự không ghê sợ trước điều đáng ghê sợ, sự không ghê sợ nếu để các hiện tượng xấu ác "
               "bất thiện xảy ra nơi mình")                                                                # (pi-1)
HIRI_D = ("Điều mà là sự hổ thẹn trước điều đáng hổ thẹn, sự hổ thẹn nếu để các hiện tượng xấu ác bất thiện "
          "xảy ra nơi mình")                                                                               # (pi-1)
OTTAPPA_D = ("Điều mà là sự ghê sợ trước điều đáng ghê sợ, sự ghê sợ nếu để các hiện tượng xấu ác bất thiện "
             "xảy ra nơi mình")                                                                            # (pi-1)
DOVACASSA_D = ("Khi được nhắc nhở đúng theo Giáo Pháp mà có sự khó bảo, tính khó bảo, sự khó dạy bảo, "
               "sự tiếp nhận ngang trái, sự thích thú việc làm trái, sự thiếu tôn trọng, thái độ thiếu tôn trọng, "
               "sự thiếu kính trọng, sự không vâng lời")                                                   # (pi-1)
SOVACASSA_A = ("Khi được nhắc nhở đúng theo Giáo Pháp mà có sự dễ bảo, tính dễ bảo, sự dễ dạy bảo, "
               "sự không tiếp nhận ngang trái, sự không thích thú việc làm trái")                          # (pi-1)
SOVACASSA_D = SOVACASSA_A + ", sự tôn trọng, thái độ tôn trọng, sự kính trọng, sự vâng lời"   # pi-4 order
MITTA_BAD = "Có những người không có niềm tin, phạm giới, ít học hỏi, keo kiệt, kém trí tuệ"                # (pi-1)
MITTA_GOOD = "Có những người có niềm tin, giữ giới, học hỏi nhiều, rộng lượng, có trí tuệ"                   # (pi-1)
SEVANA = ("điều mà là sự giao du với họ, sự thường xuyên giao du, sự giao du mật thiết, sự gần gũi, "
          "sự gần gũi mật thiết, sự gắn bó, sự gắn bó mật thiết, sự nghiêng về phía họ")                    # (pi-1)

# sense doors (pi-1 ^1-1352 / ^1-1354, with the pi-4 semicolons)
SENSES = "Khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân…"  # (pi-1)
NIMITTA = "nắm giữ dấu hiệu tổng quát, nắm giữ các chi tiết"                                                # (pi-1)
NA_NIMITTA = "không nắm giữ dấu hiệu tổng quát, không nắm giữ các chi tiết"                                 # (pi-1)


def sotapatti_flow(organ):          # yatvādhikaraṇamenaṃ X-indriyaṃ asaṃvutaṃ viharantaṃ … anvāssaveyyuṃ
    return (f"nếu sống với năng lực {organ} không được thu thúc thì các hiện tượng xấu ác bất thiện là sự thèm muốn "
            "và nỗi buồn có thể tràn vào người ấy")


def agutta_tail(organ):             # tassa saṃvarāya na paṭipajjati, na rakkhati …, … na saṃvaraṃ āpajjati
    return (f"thế mà người ấy không thực hành để thu thúc năng lực ấy, không bảo vệ năng lực {organ}, "
            f"không thực hiện sự thu thúc nơi năng lực {organ}")


def gutta_tail(organ):              # tassa saṃvarāya paṭipajjati, rakkhati …, … saṃvaraṃ āpajjati
    return (f"vì vậy người ấy thực hành để thu thúc năng lực ấy, bảo vệ năng lực {organ}, "
            f"thực hiện sự thu thúc nơi năng lực {organ}")


AGUTTA_D = (f"{S.IDHEKACCO} khi thấy hình sắc bằng mắt thì {NIMITTA}; {sotapatti_flow('mắt')}, {agutta_tail('mắt')}. "
            f"{SENSES} khi nhận biết đối tượng của ý bằng ý thì {NIMITTA}; {sotapatti_flow('ý')}, "
            f"{agutta_tail('ý')}. Điều mà là sự không canh giữ, sự không bảo vệ, sự không che chở, "
            "sự không thu thúc đối với sáu năng lực này")
GUTTA_D = (f"{S.IDHEKACCO} khi thấy hình sắc bằng mắt thì {NA_NIMITTA}; {sotapatti_flow('mắt')}, {gutta_tail('mắt')}. "
           f"{SENSES} khi nhận biết đối tượng của ý bằng ý thì {NA_NIMITTA}; {sotapatti_flow('ý')}, "
           f"{gutta_tail('ý')}. Điều mà là sự canh giữ, sự bảo vệ, sự che chở, sự thu thúc đối với sáu năng lực này")

AMATTA_A = ("Ở đời này, có người ăn thức ăn mà không suy xét, không đúng cách, để vui đùa, để say sưa, "
            "để trang điểm, để làm đẹp")                                                                   # (pi-1)
AMATTA_B = "điều mà, ở đây, là sự không biết đủ, sự không biết tiết độ, sự không suy xét trong ăn uống"      # (pi-1)
MATTA_A = "Ở đời này, có người suy xét và ăn thức ăn đúng cách"                                             # (pi-1)
MATTA_Q1 = "Không phải để vui đùa, không phải để say sưa, không phải để trang điểm, không phải để làm đẹp"   # (pi-1)
MATTA_Q2 = "mà chỉ để thân này được duy trì và kéo dài, để chấm dứt sự bức bách, để hỗ trợ đời sống tu hành trong sạch"  # (pi-1)
MATTA_Q3 = ("ta sẽ diệt trừ cảm giác cũ, sẽ không làm sinh khởi cảm giác mới, và ta sẽ có sự duy trì mạng sống, "
            "sự không có lỗi và sự an trú thoải mái")                                                      # (pi-1)
MATTA_B = "Điều mà, ở đây, là sự biết đủ, sự biết tiết độ, sự suy xét trong ăn uống"                         # (pi-1)
MATTA_D = f"{MATTA_A} – “{MATTA_Q1}; {MATTA_Q2}. Như vậy, {MATTA_Q3}”. {MATTA_B}"

MUTTHASSACCA_D = ("Điều mà là sự không tỉnh thức, sự không nhớ lại, sự không hồi tưởng, sự không tỉnh thức, "
                  "sự không ghi nhớ, sự không gìn giữ trong trí nhớ, sự hời hợt, sự quên lãng")             # (pi-2)
SATI_D = ("Điều mà là sự tỉnh thức, sự nhớ lại, sự hồi tưởng, sự tỉnh thức, sự ghi nhớ, sự gìn giữ trong trí nhớ, "
          "sự không hời hợt, sự không quên lãng, sự tỉnh thức, năng lực tỉnh thức, sức mạnh tỉnh thức, "
          "tỉnh thức đúng đắn")                                                                            # (pi-1)
MOHA_A = ("sự không biết, sự không thấy, sự không thấu hiểu, sự không hiểu ra, sự không tỉnh ngộ, "
          "sự không thấu triệt, sự không nắm bắt, sự không đi sâu")                                        # (pi-1)
MOHA_B = (", sự không xem xét, sự không xem xét lại, sự không tự mình thấy rõ, sự ngu muội, sự khờ dại, "
          "sự thiếu hiểu biết rõ ràng, sự si mê, sự mê muội, sự mê lầm, vô minh, dòng lũ vô minh, ách vô minh, "
          "khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh, then cài vô minh, sự si mê, "
          "tức gốc rễ bất thiện")                                                                          # (pi-1)
PANNA_FULL = ("Điều mà là trí tuệ, sự hiểu rõ, sự tìm hiểu, sự tìm hiểu kỹ, sự tìm hiểu các hiện tượng, sự nhận xét, "
              "sự nhận diện, sự nhận diện chính xác, sự thông thái, sự khéo léo, sự tinh tường, "
              "sự phân biệt sáng suốt, sự suy tư, sự khảo sát, sự sâu rộng, sự thông minh, sự dẫn dắt, "
              "sự thấu suốt, sự hiểu biết rõ ràng, cây roi thúc, trí tuệ, năng lực trí tuệ, sức mạnh trí tuệ, "
              "thanh gươm trí tuệ, lâu đài trí tuệ, ánh sáng trí tuệ, hào quang trí tuệ, ngọn đuốc trí tuệ, "
              "viên ngọc trí tuệ, sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn")         # (pi-2)
PANNA_PE = "trí tuệ, sự hiểu rõ… sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn"           # (pi-1)
SILAVIPATTI_A = "sự vi phạm bằng thân, sự vi phạm bằng lời nói, sự vi phạm bằng thân và lời nói"            # (pi-1)
SILAVIPATTI_B = "Mọi sự phạm giới đều là sự suy đồi về giới hạnh."                                          # (pi-1)
SILASAMPADA_A = "sự không vi phạm bằng thân, sự không vi phạm bằng lời nói, sự không vi phạm bằng thân và lời nói"  # (pi-1)
SILASAMPADA_B = "Mọi sự thu thúc theo giới hạnh đều là sự thành tựu về giới hạnh."                          # (pi-1)
NATTHI_A = ("“Không có sự bố thí, không có sự cúng tế, không có sự cúng dường, không có quả và kết quả "
            "của các nghiệp làm tốt và làm xấu")                                                           # (pi-1)
NATTHI_B = (", không có thế gian này, không có thế gian khác, không có mẹ, không có cha, không có chúng sinh "
            "hóa sinh, không có các sa-môn và bà-la-môn trong thế gian đã đi đúng đắn")                     # (pi-1)
WORLD_TAIL = (", thực hành đúng đắn, những người đã tự mình hiểu biết trực tiếp, chứng nghiệm thế gian này "
              "và thế gian khác rồi tuyên bố”")                                                            # (pi-1)
ATTHI = ("“Có sự bố thí, có sự cúng tế, có sự cúng dường, có quả và kết quả của các nghiệp làm tốt và làm xấu, "
         "có thế gian này, có thế gian khác, có mẹ, có cha, có chúng sinh hóa sinh, có các sa-môn và bà-la-môn "
         "trong thế gian đã đi đúng đắn" + WORLD_TAIL)                                                     # (pi-1)
DITTHI_LIST = ("quan điểm, sự mắc kẹt trong các quan điểm, rừng rậm quan điểm, hoang mạc quan điểm, "
               "sự quanh co của quan điểm, sự dao động của quan điểm, xiềng xích quan điểm, sự nắm giữ, "
               "sự bám chặt, sự cố chấp, sự hiểu sai lệch, con đường lệch lạc, lối đi sai lầm, sự sai lầm, "
               "lĩnh vực của các học thuyết ngoại đạo, sự nắm giữ điều đảo ngược")                         # (pi-1)
MICCHA_ALL = "Mọi quan điểm sai lầm đều là sự suy đồi về quan điểm."                                         # (pi-1)
SAMMA_ALL = "Mọi quan điểm đúng đắn đều là sự thành tựu về quan điểm."                                       # (pi-1)
ORAM = "năm xiềng xích thuộc phần thấp"                                                                     # (pi-2)
UDDHAM = "năm xiềng xích thuộc phần cao"                                                                    # (pi-2)

# duka 20-26
PUBBAKARI = "Người làm ơn trước, và người biết ơn, đền ơn"           # Yo ca pubbakārī, yo ca kataññū katavedī
LADDHA = "người nhận được thứ gì cũng"                               # yo ca laddhaṃ laddhaṃ …
KUKKUCCA_NA = "hối tiếc về điều không đáng hối tiếc"                 # na kukkuccāyitabbaṃ kukkuccāyati
KUKKUCCA_YES_NA = "không hối tiếc về điều đáng hối tiếc"             # kukkuccāyitabbaṃ na kukkuccāyati
KUKKUCCA_NA_NA = "không hối tiếc về điều không đáng hối tiếc"        # na kukkuccāyitabbaṃ na kukkuccāyati
KUKKUCCA_YES = "hối tiếc về điều đáng hối tiếc"                      # kukkuccāyitabbaṃ kukkuccāyati
SEVATI = "gần gũi, kết giao, thân cận"                               # sevati bhajati payirupāsati

REUSED = [  # (Vietnamese string, book)
    (KODHA_A, "2"), (KODHA_B, "2"), (UPANAHA_A, "2"), (UPANAHA_B, "2"), (UPANAHA_C, "2"), (MAKKHA_A, "2"),
    (MAKKHA_B, "2"), (PALASA_A, "2"), (PALASA_B, "2"), (ISSA_A, "2"), (ISSA_B, "2"), (MACCHARIYA_A, "2"),
    (MACCHARIYA_B, "2"), (SATHEYYA_A, "2"), (SATHEYYA_B, "2"), (SATHEYYA_C, "2"), (MAYA_A, "2"), (JANNA, "2"),
    (MAYA_C, "2"), (AHIRIKA_D, "1"), (ANOTTAPPA_D, "1"), (HIRI_D, "1"), (OTTAPPA_D, "1"), (DOVACASSA_D, "1"),
    (SOVACASSA_A, "1"), (MITTA_BAD, "1"), (MITTA_GOOD, "1"), (SEVANA, "1"), (SENSES, "1"), (NIMITTA, "1"),
    (NA_NIMITTA, "1"), (sotapatti_flow("mắt"), "1"), (sotapatti_flow("ý"), "1"), (agutta_tail("mắt"), "1"),
    (agutta_tail("ý"), "1"), (gutta_tail("mắt"), "1"), (gutta_tail("ý"), "1"),
    ("khi thấy hình sắc bằng mắt thì", "1"), ("khi nhận biết đối tượng của ý bằng ý thì", "1"),
    ("Điều mà là sự không canh giữ, sự không bảo vệ, sự không che chở, sự không thu thúc đối với sáu năng lực này", "1"),
    ("Điều mà là sự canh giữ, sự bảo vệ, sự che chở, sự thu thúc đối với sáu năng lực này", "1"),
    (AMATTA_A, "1"), (AMATTA_B, "1"), (MATTA_A, "1"), (MATTA_Q1, "1"), (MATTA_Q2, "1"), (MATTA_Q3, "1"),
    (MATTA_B, "1"), (MUTTHASSACCA_D, "2"), (SATI_D, "1"), (MOHA_A, "1"), (MOHA_B, "1"), (PANNA_FULL, "2"),
    (PANNA_PE, "1"), (SILAVIPATTI_A, "1"), (SILAVIPATTI_B, "1"), (SILASAMPADA_A, "1"), (SILASAMPADA_B, "1"),
    (NATTHI_A, "1"), (NATTHI_B, "1"), (WORLD_TAIL, "1"), (ATTHI, "1"), (DITTHI_LIST, "1"), (MICCHA_ALL, "1"),
    (SAMMA_ALL, "1"), (ORAM, "2"), (UDDHAM, "2"), (SEVATI, "2"),
    ("Điều mà thuộc loại như vậy là " + DITTHI_LIST, "1"), ("Điều mà thuộc loại như vậy là " + PANNA_PE, "1"),
    ("xem “Liệt kê các hiện tượng”", "2"), ("dị bản (mọi bản)", "2"), ("Phân tích các chủ đề nhỏ", "2"),
    ("Như Lai", "2"), (MITTA_BAD + "; " + SEVANA, "1"), (MITTA_GOOD + "; " + SEVANA, "1"),
] + [(tattha(x), b) for x, b in (
    (KODHO, "2"), (UPANAHO, "2"), (MAKKHO, "2"), (PALASO, "2"), (ISSA, "2"), (MACCHARIYA, "2"), (SATHEYYA, "2"),
    (MAYA, "2"), (AHIRIKA, "1"), (ANOTTAPPA, "1"), (HIRI, "1"), (OTTAPPA, "1"), (DOVACASSATA, "1"),
    (SOVACASSATA, "1"), (PAPAMITTATA, "1"), (KALYANAMITTATA, "1"), (AGUTTADVARATA, "1"), (GUTTADVARATA, "1"),
    (AMATTANNUTA, "1"), (MATTANNUTA, "1"), (MUTTHASSACCA, "2"), (SATI, "1"), (ASAMPAJANNA, "1"),
    (SAMPAJANNA, "1"), (SILAVIPATTI, "1"), (DITTHIVIPATTI, "1"), (SILASAMPADA, "1"), (DITTHISAMPADA, "1"))
] + [(goi(x), "1") for x in (AHIRIKA, ANOTTAPPA, HIRI, OTTAPPA, DOVACASSATA, SOVACASSATA, PAPAMITTATA,
                              KALYANAMITTATA, AGUTTADVARATA, GUTTADVARATA, AMATTANNUTA, MATTANNUTA, SATI,
                              ASAMPAJANNA, SAMPAJANNA, SILAVIPATTI, DITTHIVIPATTI, SILASAMPADA, DITTHISAMPADA)]

# every person name used in this chapter (asserted equal to S.NAME)
NAMES_USED = {k: S.NAME[k] for k in (
    "kodhano", "upanāhī", "makkhī", "paḷāsī", "issukī", "maccharī", "saṭho", "māyāvī", "ahiriko", "anottappī",
    "dubbaco", "pāpamitto", "indriyesu aguttadvāro", "bhojane amattaññū", "muṭṭhassati", "asampajāno",
    "sīlavipanno", "diṭṭhivipanno", "ajjhattasaṃyojano", "bahiddhāsaṃyojano", "akkodhano", "anupanāhī", "amakkhī",
    "apaḷāsī", "anissukī", "amaccharī", "asaṭho", "amāyāvī", "hirimā", "ottappī", "suvaco", "kalyāṇamitto",
    "indriyesu guttadvāro", "bhojane mattaññū", "upaṭṭhitassati", "sampajāno", "sīlasampanno", "diṭṭhisampanno",
    "dve puggalā dullabhā lokasmiṃ", "dve puggalā duttappayā", "dve puggalā sutappayā",
    "dvinnaṃ puggalānaṃ āsavā vaḍḍhanti", "dvinnaṃ puggalānaṃ āsavā na vaḍḍhanti", "hīnādhimutto",
    "paṇītādhimutto", "titto", "tappetā", "sammāsambuddho", "paccekasambuddho")}
EXPECTED = {  # the approved strings, retyped here only to catch drift in the sample
    "kodhano": "người giận dữ", "saṭho": "người gian trá", "titto": "người đã thỏa mãn",
    "tappetā": "người làm cho người khác thỏa mãn", "paccekasambuddho": "bậc Độc Giác",
    "dvinnaṃ puggalānaṃ āsavā vaḍḍhanti": "ô nhiễm của hai hạng người tăng trưởng",
}


# ---------------------------------------------------------------------------------------------------------------
def build():
    q, cd = S.q_katamo, dash_name
    S_ = [S.seg(S.H_CHAPTER[2] + " ^4-1-2-0")]
    a = []

    def kodha(v):
        return KODHA_A + v + KODHA_B + " " + goi(KODHO)

    def upanaha(v):
        # ^4-66: "… aparakālaṃ upanāho yo evarūpo …" (missing full stop, rendered as meant)
        return UPANAHA_A + " " + UPANAHA_B + v + UPANAHA_C + " " + goi(UPANAHO)

    def makkha(v):
        return MAKKHA_A + v + MAKKHA_B + " " + goi(MAKKHO)

    def issa(v):
        return ISSA_A + v + ISSA_B + " " + goi(ISSA)

    def macchariya():
        return MACCHARIYA_A + " " + MACCHARIYA_B + " của tâm " + goi(MACCHARIYA)

    def satheyya(v):
        return SATHEYYA_A + " " + SATHEYYA_B + v + SATHEYYA_C + " " + goi(SATHEYYA)

    def maya():
        return MAYA_A + " " + MAYA_B + " " + MAYA_C + " " + goi(MAYA)

    # 1-10 (negative), appahīna
    neg = [
        ("kodhano", KODHO, kodha(V_DUSANA), "^4-45"),
        ("upanāhī", UPANAHO, upanaha(V_ATHAPANA), "^4-46"),
        ("makkhī", MAKKHO, makkha(V_MAKKHI), "^4-47"),
        ("paḷāsī", PALASO, PALASA + " " + goi(PALASO), "^4-48"),
        ("issukī", ISSA, issa(V_USSUYA), "^4-49"),
        ("maccharī", MACCHARIYA, macchariya(), "^4-50"),
        ("saṭho", SATHEYYA, satheyya(V_KAKKHALA), "^4-51"),
        ("māyāvī", MAYA, maya(), "^4-52"),
    ]
    for key, x, body, bid in neg:
        a.append((f"{q(N(key))} {tattha(x)} {body} {yassa_app(x)} {cd(N(key))}", bid))
    with_dhamma_bad = [
        ("ahiriko", AHIRIKA, AHIRIKA_D, "^4-53"),
        ("anottappī", ANOTTAPPA, ANOTTAPPA_D, "^4-54"),
        ("dubbaco", DOVACASSATA, DOVACASSA_D, "^4-55"),
        ("pāpamitto", PAPAMITTATA, f"{MITTA_BAD}; {SEVANA}", "^4-56"),
        ("indriyesu aguttadvāro", AGUTTADVARATA, AGUTTA_D, "^4-57"),
        ("bhojane amattaññū", AMATTANNUTA, f"{AMATTA_A}; {AMATTA_B}", "^4-58"),
        ("muṭṭhassati", MUTTHASSACCA, MUTTHASSACCA_D, "^4-59"),
        ("asampajāno", ASAMPAJANNA, "Điều mà là " + MOHA_A + V_ASAMGAHANA + MOHA_B, "^4-60"),
        ("sīlavipanno", SILAVIPATTI, cap1(SILAVIPATTI_A), "^4-61"),
    ]
    for key, x, body, bid in with_dhamma_bad:
        extra = (" " + SILAVIPATTI_B) if key == "sīlavipanno" else ""
        a.append((f"{q(N(key))} {tattha(x)} {body} {goi(x)}{extra} {mang(x, N(key))}", bid))
    # ^4-62 diṭṭhivipanno: the Pāli closes the list with ", ayaṃ vuccati" (no dash)
    natthi = NATTHI_A + V_SUKATA + NATTHI_B + V_SAMAGGATA + WORLD_TAIL + "."
    a.append((f"{q(N('diṭṭhivipanno'))} {tattha(DITTHIVIPATTI)} {natthi} Điều mà thuộc loại như vậy là "
              f"{DITTHI_LIST}{V_VIPARIYESA}, đó được gọi là {DITTHIVIPATTI}. {MICCHA_ALL} "
              f"{mang(DITTHIVIPATTI, N('diṭṭhivipanno'))}", "^4-62"))
    a.append((f"{q(N('ajjhattasaṃyojano'))} Người nào có {ORAM} chưa được dứt bỏ {cd(N('ajjhattasaṃyojano'))}",
              "^4-63"))
    a.append((f"{q(N('bahiddhāsaṃyojano'))} Người nào có {UDDHAM} chưa được dứt bỏ {cd(N('bahiddhāsaṃyojano'))}",
              "^4-64"))
    # 11-14 (positive), pahīna
    pos = [
        ("akkodhano", KODHO, kodha(""), "^4-65"),
        ("anupanāhī", UPANAHO, upanaha(""), "^4-66"),
        ("amakkhī", MAKKHO, makkha(""), "^4-67"),
        ("apaḷāsī", PALASO, PALASA + " " + goi(PALASO), "^4-68"),
        ("anissukī", ISSA, issa(""), "^4-69"),
        ("amaccharī", MACCHARIYA, macchariya(), "^4-70"),      # ^4-70 "pugalo" (slip) rendered as puggalo
        ("asaṭho", SATHEYYA, satheyya(""), "^4-71"),
        ("amāyāvī", MAYA, maya(), "^4-72"),
    ]
    for key, x, body, bid in pos:
        a.append((f"{q(N(key))} {tattha(x)} {body} {yassa_pah(x)} {cd(N(key))}", bid))
    with_dhamma_good = [
        ("hirimā", HIRI, HIRI_D, "^4-73"),
        ("ottappī", OTTAPPA, OTTAPPA_D, "^4-74"),
        ("suvaco", SOVACASSATA, SOVACASSA_D, "^4-75"),
        ("kalyāṇamitto", KALYANAMITTATA, f"{MITTA_GOOD}; {SEVANA}", "^4-76"),
        ("indriyesu guttadvāro", GUTTADVARATA, GUTTA_D, "^4-77"),
        ("bhojane mattaññū", MATTANNUTA, MATTA_D, "^4-78"),
        ("upaṭṭhitassati", SATI, SATI_D, "^4-79"),
        ("sampajāno", SAMPAJANNA, PANNA_FULL, "^4-80"),
        ("sīlasampanno", SILASAMPADA, cap1(SILASAMPADA_A), "^4-81"),
    ]
    for key, x, body, bid in with_dhamma_good:
        extra = (" " + SILASAMPADA_B) if key == "sīlasampanno" else ""
        a.append((f"{q(N(key))} {tattha(x)} {body} {goi(x)}{extra} {trangbi(x, N(key))}", bid))
    a.append((f"{q(N('diṭṭhisampanno'))} {tattha(DITTHISAMPADA)} {ATTHI}. Điều mà thuộc loại như vậy là {PANNA_PE} "
              f"{goi(DITTHISAMPADA)} {SAMMA_ALL} {trangbi(DITTHISAMPADA, N('diṭṭhisampanno'))}", "^4-82"))
    # 20-26
    n20 = N("dve puggalā dullabhā lokasmiṃ")
    a.append((f"{S.cap(n20)} là những ai? {PUBBAKARI} – {n20.replace('hai hạng người', 'hai hạng người này', 1)}.",
              "^4-83"))
    n21, n22 = N("dve puggalā duttappayā"), N("dve puggalā sutappayā")
    a.append((f"{S.cap(n21)} là những ai? {S.cap(LADDHA)} cất giữ lại, và {LADDHA} đem cho đi – hai hạng người này "
              f"“{n21.replace('hai hạng người ', '', 1)}”.", "^4-84"))
    a.append((f"{S.cap(n22)} là những ai? {S.cap(LADDHA)} không cất giữ lại, và {LADDHA} không đem cho đi – "
              f"hai hạng người này “{n22.replace('hai hạng người ', '', 1)}”.", "^4-85"))
    n23, n24 = N("dvinnaṃ puggalānaṃ āsavā vaḍḍhanti"), N("dvinnaṃ puggalānaṃ āsavā na vaḍḍhanti")
    a.append((f"{S.cap(n23.replace('hai hạng người', 'hai hạng người nào', 1))}? Người {KUKKUCCA_NA}, và người "
              f"{KUKKUCCA_YES_NA} – {n23.replace('hai hạng người', 'hai hạng người này', 1)}.", "^4-86"))
    a.append((f"{S.cap(n24.replace('hai hạng người', 'hai hạng người nào', 1))}? Người {KUKKUCCA_NA_NA}, và người "
              f"{KUKKUCCA_YES} – {n24.replace('hai hạng người', 'hai hạng người này', 1)}.", "^4-87"))
    a.append((f"{q(N('hīnādhimutto'))} {S.IDHEKACCO} phạm giới, có phẩm chất xấu; người ấy {SEVATI} một người khác "
              f"phạm giới, có phẩm chất xấu {cd(N('hīnādhimutto'))}", "^4-88"))
    a.append((f"{q(N('paṇītādhimutto'))} {S.IDHEKACCO} giữ giới, có phẩm chất tốt; người ấy {SEVATI} một người khác "
              f"giữ giới, có phẩm chất tốt {cd(N('paṇītādhimutto'))}", "^4-89"))
    S_ += [S.seg(t + " " + i) for t, i in a]
    pacceka = N("paccekasambuddho").replace("bậc ", "Các bậc ", 1)
    S_.append(S.seg(f"{q(N('titto'))} {pacceka}{V_PACCEKA} và những đệ tử A-la-hán của Như Lai là những người đã "
                    f"thỏa mãn. {S.cap(N('sammāsambuddho'))} vừa là {N('titto')} vừa là {N('tappetā')}{V_TAPPETA}.",
                    S.CLOSER_CHAPTER[2] + " ^4-90"))
    return S_


def cap1(s):
    return S.cap(s)


def check():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
    bad = [(v, b) for v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails:\n" + "\n".join(map(repr, bad))
    for k, v in EXPECTED.items():
        assert NAMES_USED[k] == v, (k, NAMES_USED[k], v)


def main():
    check()
    segs = build()
    text = "\n\n".join(segs)
    for k, v in NAMES_USED.items():
        if k in ("dvinnaṃ puggalānaṃ āsavā vaḍḍhanti", "dvinnaṃ puggalānaṃ āsavā na vaḍḍhanti"):
            continue  # question form «… hai hạng người nào …» (see notes-rails-3.md); answer keeps the name
        assert v.lower() in text.lower(), ("name not used verbatim", k, v)
    S.write(OUT, segs)


if __name__ == "__main__":
    main()
