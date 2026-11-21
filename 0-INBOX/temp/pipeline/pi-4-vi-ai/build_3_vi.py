# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 3: 3-dukapuggalapannatti.md (Duka, ^4-45 … ^4-90).

Imports the approved sample builder (names, frames, headings, closers) and writes ONLY
AI_translation/vietnamese/pi-4-vietnamese-plain-zeroshot_split_chapters/3-dukapuggalapannatti.md.
Every string taken from pi-1 / pi-2 is asserted to occur in that book's reviewed Vietnamese rails.
run:  python -I -X utf8 build_3_vi.py
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402

CH = "3-dukapuggalapannatti.md"
N = B.NAME
q, close = B.q, B.close


def tq(x):                       # Tattha katamo / katamā / katamaṃ X?
    return B.TATTHA_Q.format(x=x)


def tc(x):                       # – ayaṃ / idaṃ vuccati X.
    return B.THING_CLOSE.format(x=x)


# ---------------------------------------------------------------- person frames of this chapter
def yassa(noun, name, gone=False):
    """Yassa puggalassa ayaṃ X (ap)pahīno – ayaṃ vuccati puggalo "Y"."""
    state = "đã được dứt bỏ" if gone else "chưa được dứt bỏ"
    return f"Người mà {noun} này {state} {close(name)}"


def having(noun, name, bad):
    """Iminā / Imāya X samannāgato puggalo "Y". (no dash in the Pāli)"""
    verb = "mang" if bad else B.SAMANNAGATO   # bad states: «mang» (pi-2 ^2-826), else «được trang bị»
    return f"Người {verb} {noun} này là “{name}”."


# ---------------------------------------------------------------- definitions reused from pi-1 / pi-2
KODHA_A = "Điều mà là sự giận dữ, sự khởi giận, trạng thái khởi giận, sự sân hận, sự khởi sân, trạng thái khởi sân"
KODHA_B = (", sự thù hằn, sự khởi thù hằn, trạng thái khởi thù hằn, sự chống đối, sự đối nghịch, sự hung dữ, "
           "sự nói năng cộc cằn, sự không hài lòng của tâm")                                   # pi-2 Vibhaṅga 17 Duka (1)
UPANAHA_A = ("Lúc trước là sự giận dữ, lúc sau là sự ôm hận. Điều mà thuộc loại như vậy là sự ôm hận, "
             "sự khởi ôm hận, trạng thái khởi ôm hận, sự lưu giữ")
UPANAHA_B = ", sự giữ lại, sự giữ chặt, sự nối kết, sự kéo dài liên tục, sự làm cho sự giận dữ thêm vững chắc"  # pi-2 ^2-891
MAKKHA_A = "Điều mà là sự gièm pha, sự khởi gièm pha, trạng thái khởi gièm pha"
MAKKHA_B = ", sự khắc nghiệt, hành động khắc nghiệt"                                               # pi-2
PALASA = ("Điều mà là sự ganh đua, sự khởi ganh đua, trạng thái khởi ganh đua, sự ôm giữ sự ganh đua, "
          "nguyên cớ tranh cãi, sự đòi ngang hàng, sự không chịu buông bỏ")   # pi-2 ^2-892 (+ paḷāsāyitattaṃ)
ISSA_A = ("Điều mà, trước lợi lộc, sự tôn vinh, sự kính trọng, sự quý trọng, sự đảnh lễ và sự cúng dường mà "
          "người khác nhận được, là sự ganh tị, sự khởi ganh tị, trạng thái khởi ganh tị, sự đố kỵ, sự khởi đố kỵ")
ISSA_B = ", trạng thái khởi đố kỵ"                                                                  # pi-2
MACCHARIYA_LIST = ("Năm loại keo kiệt – keo kiệt về chỗ ở, keo kiệt về gia đình, keo kiệt về lợi lộc, "
                   "keo kiệt về lời khen, keo kiệt về Giáo Pháp.")                                  # pi-2 ^2-893
MACCHARIYA = ("Điều mà thuộc loại như vậy là sự keo kiệt, sự khởi keo kiệt, trạng thái khởi keo kiệt, "
              "sự bủn xỉn, sự hà tiện, sự bo bo, trạng thái khép chặt của tâm")                   # pi-2 ^2-893
SATHEYYA_A = ("Ở đời này, có người gian trá, rất gian trá. Điều mà, ở đây, là sự gian trá, tính gian trá, "
              "sự gian xảo, sự xảo quyệt, tính xảo quyệt")
SATHEYYA_B = ", sự quanh co, tính quanh co"                                                        # pi-2 ^2-894
MAYA_A = ("Ở đời này, có người sau khi làm hành vi xấu bằng thân, sau khi làm hành vi xấu bằng lời nói, "
          "sau khi làm hành vi xấu bằng ý, vì muốn che giấu điều đó mà đặt ra ước muốn xấu xa")  # pi-2
MA_MAM = "“Mong người ta đừng biết về tôi”"                                                       # pi-2 "mā maṃ jaññā"ti
MAYA_WISH = (f"người ấy mong muốn {MA_MAM}, suy tính {MA_MAM}, nói lời {MA_MAM}, "
             f"hành động bằng thân {MA_MAM}.")
MAYA_B = ("Điều mà thuộc loại như vậy là sự xảo trá, tính xảo trá, sự lấn lướt, sự lừa dối, sự gian lận, "
          "sự đánh lạc hướng, sự lảng tránh, sự giấu giếm, sự giấu giếm kỹ, sự che đậy, sự che giấu, "
          "sự không bày tỏ, sự không bộc lộ, sự che đậy hoàn toàn, việc làm xấu ác")             # pi-2
AHIRIKA = ("Điều mà là sự không hổ thẹn trước điều đáng hổ thẹn, sự không hổ thẹn nếu để các hiện tượng "
           "xấu ác bất thiện xảy ra nơi mình")                                                      # pi-1 ^1-1328
ANOTTAPPA = ("Điều mà là sự không ghê sợ trước điều đáng ghê sợ, sự không ghê sợ nếu để các hiện tượng "
             "xấu ác bất thiện xảy ra nơi mình")                                                    # pi-1 ^1-1329
HIRI = ("Điều mà là sự hổ thẹn trước điều đáng hổ thẹn, sự hổ thẹn nếu để các hiện tượng xấu ác bất thiện "
        "xảy ra nơi mình")                                                                          # pi-1 ^1-1330
OTTAPPA = ("Điều mà là sự ghê sợ trước điều đáng ghê sợ, sự ghê sợ nếu để các hiện tượng xấu ác bất thiện "
           "xảy ra nơi mình")                                                                       # pi-1 ^1-1331
DOVACASSATA = ("Khi được nhắc nhở đúng theo Giáo Pháp mà có sự khó bảo, tính khó bảo, sự khó dạy bảo, "
               "sự tiếp nhận ngang trái, sự thích thú việc làm trái, sự thiếu tôn trọng, thái độ thiếu tôn "
               "trọng, sự thiếu kính trọng, sự không vâng lời")                                    # pi-1 ^1-1332
SOVACASSATA_A = ("Khi được nhắc nhở đúng theo Giáo Pháp mà có sự dễ bảo, tính dễ bảo, sự dễ dạy bảo, "
                 "sự không tiếp nhận ngang trái, sự không thích thú việc làm trái")               # pi-1 ^1-1334
SOVACASSATA = SOVACASSATA_A + ", sự tôn trọng, thái độ tôn trọng, sự kính trọng, sự vâng lời"  # Pāli order here
ASSOCIATE = ("điều mà là sự giao du với họ, sự thường xuyên giao du, sự giao du mật thiết, sự gần gũi, "
             "sự gần gũi mật thiết, sự gắn bó, sự gắn bó mật thiết, sự nghiêng theo")           # pi-2 ^2-901 (sampavaṅkatā)
PAPAMITTA_PEOPLE = "Có những người không có niềm tin, phạm giới, ít học hỏi, keo kiệt, kém trí tuệ; "   # pi-1/pi-2
KALYANAMITTA_PEOPLE = "Có những người có niềm tin, giữ giới, học hỏi nhiều, rộng lượng, có trí tuệ; "   # pi-1 ^1-1335
INDRIYA_NEG = (
    "Ở đời này, có người khi thấy hình sắc bằng mắt thì nắm giữ dấu hiệu tổng quát, nắm giữ các chi tiết. "
    "Nếu sống với năng lực mắt không được thu thúc thì các hiện tượng xấu ác bất thiện là sự thèm muốn và nỗi "
    "buồn có thể tràn vào người ấy, thế mà người ấy không thực hành để thu thúc năng lực ấy, không bảo vệ năng "
    "lực mắt, không thực hiện sự thu thúc nơi năng lực mắt. Khi nghe âm thanh bằng tai… khi ngửi mùi bằng "
    "mũi… khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân… khi nhận biết đối tượng của ý bằng ý thì "
    "nắm giữ dấu hiệu tổng quát, nắm giữ các chi tiết. Nếu sống với năng lực ý không được thu thúc thì các "
    "hiện tượng xấu ác bất thiện là sự thèm muốn và nỗi buồn có thể tràn vào người ấy, thế mà người ấy không "
    "thực hành để thu thúc năng lực ấy, không bảo vệ năng lực ý, không thực hiện sự thu thúc nơi năng lực ý. "
    "Điều mà là sự không canh giữ, sự không bảo vệ, sự không che chở, sự không thu thúc đối với sáu năng lực "
    "này")                                                                                          # pi-1 ^1-1352
INDRIYA_POS = (
    "Ở đời này, có người khi thấy hình sắc bằng mắt thì không nắm giữ dấu hiệu tổng quát, không nắm giữ các "
    "chi tiết. Nếu sống với năng lực mắt không được thu thúc thì các hiện tượng xấu ác bất thiện là sự thèm "
    "muốn và nỗi buồn có thể tràn vào người ấy, vì vậy người ấy thực hành để thu thúc năng lực ấy, bảo vệ năng "
    "lực mắt, thực hiện sự thu thúc nơi năng lực mắt. Khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… khi "
    "nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân… khi nhận biết đối tượng của ý bằng ý thì không nắm giữ "
    "dấu hiệu tổng quát, không nắm giữ các chi tiết. Nếu sống với năng lực ý không được thu thúc thì các hiện "
    "tượng xấu ác bất thiện là sự thèm muốn và nỗi buồn có thể tràn vào người ấy, vì vậy người ấy thực hành để "
    "thu thúc năng lực ấy, bảo vệ năng lực ý, thực hiện sự thu thúc nơi năng lực ý. Điều mà là sự canh giữ, "
    "sự bảo vệ, sự che chở, sự thu thúc đối với sáu năng lực này")                                # pi-1 ^1-1354
BHOJANA_NEG = ("Ở đời này, có người ăn thức ăn mà không suy xét, không đúng cách, để vui đùa, để say sưa, để "
               "trang điểm, để làm đẹp. Điều mà, ở đây, là sự không biết đủ, sự không biết tiết độ, sự không "
               "suy xét trong ăn uống")                                                             # pi-1 ^1-1353
BHOJANA_POS_LEAD = "Ở đời này, có người suy xét và ăn thức ăn đúng cách"                           # pi-1 ^1-1355
BHOJANA_POS_PURPOSE = ("không phải để vui đùa, không phải để say sưa, không phải để trang điểm, không phải để "
                       "làm đẹp, mà chỉ để thân này được duy trì và kéo dài, để chấm dứt sự bức bách, để hỗ trợ "
                       "đời sống tu hành trong sạch")                                              # pi-1 ^1-1355
BHOJANA_POS_ITI = ("Như vậy, ta sẽ diệt trừ cảm giác cũ, sẽ không làm sinh khởi cảm giác mới, và ta sẽ có sự "
                   "duy trì mạng sống, sự không có lỗi và sự an trú thoải mái")                    # pi-1 ^1-1355
BHOJANA_POS_TAIL = "Điều mà, ở đây, là sự biết đủ, sự biết tiết độ, sự suy xét trong ăn uống"      # pi-1 ^1-1355
BHOJANA_POS = (f"{BHOJANA_POS_LEAD} – “{BHOJANA_POS_PURPOSE}. {BHOJANA_POS_ITI}”. {BHOJANA_POS_TAIL}")
MUTTHASSACCA = ("Điều mà là sự không tỉnh thức, sự không nhớ lại, sự không hồi tưởng, sự không tỉnh thức, "
                "sự không ghi nhớ, sự không gìn giữ trong trí nhớ, sự hời hợt, sự quên lãng")     # pi-1 ^1-1356
SATI = ("Điều mà là sự tỉnh thức, sự nhớ lại, sự hồi tưởng, sự tỉnh thức, sự ghi nhớ, sự gìn giữ trong trí "
        "nhớ, sự không hời hợt, sự không quên lãng, sự tỉnh thức, năng lực tỉnh thức, sức mạnh tỉnh thức, "
        "tỉnh thức đúng đắn")                                                                       # pi-1 ^1-1358
AVIJJA_A = ("sự không biết, sự không thấy, sự không thấu hiểu, sự không hiểu ra, sự không tỉnh ngộ, "
            "sự không thấu triệt, sự không nắm bắt, sự không đi sâu")
AVIJJA_B = (", sự không xem xét, sự không xem xét lại, sự không tự mình thấy rõ, sự ngu muội, sự khờ dại, "
            "sự thiếu hiểu biết rõ ràng, sự si mê, sự mê muội, sự mê lầm, vô minh, dòng lũ vô minh, ách vô minh, "
            "khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh, then cài vô minh, sự si mê, "
            "tức gốc rễ bất thiện")                                                                 # pi-1 ^1-390
PANNA_LIST = ("trí tuệ, sự hiểu rõ, sự tìm hiểu, sự tìm hiểu kỹ, sự tìm hiểu các hiện tượng, sự nhận xét, "
              "sự nhận diện, sự nhận diện chính xác, sự thông thái, sự khéo léo, sự tinh tường, sự phân biệt "
              "sáng suốt, sự suy tư, sự khảo sát, sự sâu rộng, sự thông minh, sự dẫn dắt, sự thấu suốt, sự hiểu "
              "biết rõ ràng, cây roi thúc, trí tuệ, năng lực trí tuệ, sức mạnh trí tuệ, thanh gươm trí tuệ, "
              "lâu đài trí tuệ, ánh sáng trí tuệ, hào quang trí tuệ, ngọn đuốc trí tuệ, viên ngọc trí tuệ, "
              "sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn")                   # pi-1 ^1-16
PANNA_PE = "trí tuệ, sự hiểu rõ… sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn"  # pi-1 paññā …pe…
VITIKKAMA = "Sự vi phạm bằng thân, sự vi phạm bằng lời nói, sự vi phạm bằng thân và lời nói"     # pi-2 ^2-903
AVITIKKAMA = ("sự không vi phạm bằng thân, sự không vi phạm bằng lời nói, "
              "sự không vi phạm bằng thân và lời nói")                                              # pi-1 ^1-1370
DUSSILYA = "Mọi sự phạm giới đều là sự suy đồi về giới hạnh."                                       # pi-1 ^1-1368
SILASAMVARA = "Mọi sự thu thúc theo giới hạnh đều là sự thành tựu về giới hạnh."                    # pi-1 ^1-1370
MICCHADITTHI_ALL = "Mọi quan điểm sai lầm đều là sự suy đồi về quan điểm."                          # pi-1 ^1-1369
SAMMADITTHI_ALL = "Mọi quan điểm đúng đắn đều là sự thành tựu về quan điểm."                         # pi-1 ^1-1371
NATTHI_A = ("Không có sự bố thí, không có sự cúng tế, không có sự cúng dường, không có quả và kết quả của các "
            "nghiệp làm tốt và làm xấu")
NATTHI_B = (", không có thế gian này, không có thế gian khác, không có mẹ, không có cha, không có chúng sinh "
            "hóa sinh, không có các sa-môn và bà-la-môn trong thế gian đã đi đúng đắn")
NATTHI_C = (", thực hành đúng đắn, những người đã tự mình hiểu biết trực tiếp, chứng nghiệm thế gian này và "
            "thế gian khác rồi tuyên bố")                                                           # pi-1 ^1-1369
ATTHI = ("Có sự bố thí, có sự cúng tế, có sự cúng dường, có quả và kết quả của các nghiệp làm tốt và làm xấu, "
         "có thế gian này, có thế gian khác, có mẹ, có cha, có chúng sinh hóa sinh, có các sa-môn và bà-la-môn "
         "trong thế gian đã đi đúng đắn, thực hành đúng đắn, những người đã tự mình hiểu biết trực tiếp, "
         "chứng nghiệm thế gian này và thế gian khác rồi tuyên bố")                                # pi-1 ^1-1371
DITTHI_LIST = ("quan điểm, sự mắc kẹt trong các quan điểm, rừng rậm quan điểm, hoang mạc quan điểm, sự quanh co "
               "của quan điểm, sự dao động của quan điểm, xiềng xích quan điểm, sự nắm giữ, sự bám chặt, sự cố "
               "chấp, sự hiểu sai lệch, con đường lệch lạc, lối đi sai lầm, sự sai lầm, lĩnh vực của các học "
               "thuyết ngoại đạo, sự nắm giữ điều đảo ngược")                                       # pi-1 ^1-392
LOWER5 = "năm xiềng xích thuộc phần thấp"     # pañcorambhāgiyāni saṃyojanāni (pi-2)
UPPER5 = "năm xiềng xích thuộc phần cao"      # pañcuddhambhāgiyāni saṃyojanāni (pi-2)
SEVATI = "gần gũi, kết giao, thân cận"        # sevati bhajati payirupāsati (pi-2)

# nouns of the qualities (pi-1 / pi-2 rails)
KODHA, UPANAHA, MAKKHA, PALASA_N, ISSA, MACCH, SATH, MAYA = (
    "sự giận dữ", "sự ôm hận", "sự gièm pha", "sự ganh đua", "sự ganh tị", "sự keo kiệt", "sự gian xảo", "sự xảo trá")
AHIRIKA_N, ANOTTAPPA_N, HIRI_N, OTTAPPA_N = (
    "sự không biết hổ thẹn", "sự không biết ghê sợ tội lỗi", "sự biết hổ thẹn", "sự biết ghê sợ tội lỗi")
DOVAC_N, SOVAC_N = "sự khó dạy bảo", "sự dễ dạy bảo"
PAPAM_N, KALYM_N = "sự kết bạn với người xấu", "sự kết bạn với người tốt"
AGUTTA_N, GUTTA_N = "sự không phòng hộ cửa các giác quan", "sự phòng hộ cửa các giác quan"
AMATTA_N, MATTA_N = "sự không biết tiết độ trong ăn uống", "sự biết tiết độ trong ăn uống"
MUTTH_N, SATI_N = "sự mất tỉnh thức", "sự tỉnh thức"
ASAMP_N, SAMP_N = "sự thiếu hiểu biết rõ ràng", "sự hiểu biết rõ ràng"
SILAV_N, SILAS_N = "sự suy đồi về giới hạnh", "sự thành tựu về giới hạnh"
DITTHIV_N, DITTHIS_N = "sự suy đồi về quan điểm", "sự thành tựu về quan điểm"

# variant brackets of this chapter
V45 = " [khác chính tả (Syā.): dūsanā dūsitattaṃ]"
V46 = " [khác chính tả (Ka.): āṭhapanā; “Phân tích các hiện tượng” 891]"
V47 = " [khác chính tả (Sī.): makkhīyanā makkhīyitattaṃ; (Ka.): makkhiyanā makkhiyitattaṃ]"
V49 = " [khác chính tả (Ka.): ussuyā ussuyanā; “Phân tích các hiện tượng” 893]"
V51 = (" [dị bản (Syā.): kakkhaḷatā kakkhaḷiyaṃ; cũng vậy trong phần giải thích phân loại theo nhóm hai "
       "của “Phân tích các chủ đề nhỏ”]")
V60 = " [khác chính tả (Sī., Syā., Ka.): asaṃgāhanā apariyogāhanā]"
V62A = " [khác chính tả (Sī.): sukaṭadukkaṭānaṃ]"
V62B = " [dị bản (Ka.): samaggatā]"
V62C = " [khác chính tả (mọi bản): vipariyesaggāho; cần xem xét cách cấu tạo của từ]"
V90A = " [dị bản (Sī.): paccekabuddho]"
V90B = " [dị bản (Sī.): tappetā ca, ayaṃ vuccati puggalo titto]"

CROSS = [
    (2, KODHA_A + KODHA_B), (2, UPANAHA_A + UPANAHA_B), (2, MAKKHA_A), (2, MAKKHA_B),
    (2, "sự ôm giữ sự ganh đua, nguyên cớ tranh cãi, sự đòi ngang hàng, sự không chịu buông bỏ"),
    (2, ISSA_A + ISSA_B), (2, MACCHARIYA_LIST), (2, "trạng thái khởi keo kiệt, sự bủn xỉn, sự hà tiện, sự bo bo, "
                                                    "trạng thái khép chặt"),
    (2, SATHEYYA_A), (2, SATHEYYA_B), (2, MAYA_A), (2, "Người ấy mong muốn “Mong người ta đừng biết về tôi”"),
    (2, "suy tính “Mong người ta đừng biết về tôi”"), (2, "nói lời “Mong người ta đừng biết về tôi”"),
    (2, "hành động bằng thân “Mong người ta đừng biết về tôi”"), (2, MAYA_B),
    (1, AHIRIKA), (1, ANOTTAPPA), (1, HIRI), (1, OTTAPPA), (1, DOVACASSATA), (1, SOVACASSATA_A),
    (2, PAPAMITTA_PEOPLE + ASSOCIATE), (1, KALYANAMITTA_PEOPLE + ASSOCIATE[:-len(", sự nghiêng theo")]),
    (1, INDRIYA_NEG), (1, INDRIYA_POS), (1, BHOJANA_NEG), (1, BHOJANA_POS_LEAD), (1, BHOJANA_POS_PURPOSE),
    (1, BHOJANA_POS_ITI), (1, BHOJANA_POS_TAIL), (1, MUTTHASSACCA), (1, SATI), (1, AVIJJA_A + AVIJJA_B),
    (1, PANNA_LIST), (1, PANNA_PE), (2, VITIKKAMA), (1, AVITIKKAMA), (1, DUSSILYA), (1, SILASAMVARA),
    (1, MICCHADITTHI_ALL), (1, SAMMADITTHI_ALL), (1, NATTHI_A + NATTHI_B + NATTHI_C), (1, ATTHI),
    (1, DITTHI_LIST), (2, "Năm xiềng xích thuộc phần thấp"), (2, "Năm xiềng xích thuộc phần cao"), (2, SEVATI),
    (2, "hối tiếc"), (2, "đệ tử"), (2, "Như Lai"), (1, "phạm giới"), (1, "giữ giới"),
    (2, "Phân tích các chủ đề nhỏ"), (2, "## Phân tích các hiện tượng"), (2, "(mọi bản)"),
]
NOUNS_PI = [(2, x) for x in (KODHA, UPANAHA, MAKKHA, PALASA_N, ISSA, MACCH, SATH, MAYA, AHIRIKA_N, ANOTTAPPA_N,
                             MUTTH_N, ASAMP_N, SILAV_N, DITTHIV_N, DOVAC_N, PAPAM_N, AGUTTA_N, AMATTA_N)] + \
           [(1, x) for x in (HIRI_N, OTTAPPA_N, SOVAC_N, KALYM_N, GUTTA_N, MATTA_N, SATI_N, SAMP_N, SILAS_N,
                             DITTHIS_N)]


def lines():
    L = ["#### " + B.CHAPTER_HEADING[3]]
    # ^4-45 … ^4-52: qualities not abandoned
    L.append(f"{q(N['kodhano'])} {tq(KODHA)} {KODHA_A}{V45}{KODHA_B} {tc(KODHA)} {yassa(KODHA, N['kodhano'])}")
    L.append(f"{q(N['upanāhī'])} {tq(UPANAHA)} {UPANAHA_A}{V46}{UPANAHA_B} {tc(UPANAHA)} "
             f"{yassa(UPANAHA, N['upanāhī'])}")
    L.append(f"{q(N['makkhī'])} {tq(MAKKHA)} {MAKKHA_A}{V47}{MAKKHA_B} {tc(MAKKHA)} {yassa(MAKKHA, N['makkhī'])}")
    L.append(f"{q(N['paḷāsī'])} {tq(PALASA_N)} {PALASA} {tc(PALASA_N)} {yassa(PALASA_N, N['paḷāsī'])}")
    L.append(f"{q(N['issukī'])} {tq(ISSA)} {ISSA_A}{V49}{ISSA_B} {tc(ISSA)} {yassa(ISSA, N['issukī'])}")
    L.append(f"{q(N['maccharī'])} {tq(MACCH)} {MACCHARIYA_LIST} {MACCHARIYA} {tc(MACCH)} "
             f"{yassa(MACCH, N['maccharī'])}")
    L.append(f"{q(N['saṭho'])} {tq(SATH)} {SATHEYYA_A}{V51}{SATHEYYA_B} {tc(SATH)} {yassa(SATH, N['saṭho'])}")
    L.append(f"{q(N['māyāvī'])} {tq(MAYA)} {MAYA_A} – {MAYA_WISH} {MAYA_B} {tc(MAYA)} {yassa(MAYA, N['māyāvī'])}")
    # ^4-53 … ^4-62: Iminā … samannāgato
    L.append(f"{q(N['ahiriko'])} {tq(AHIRIKA_N)} {AHIRIKA} {tc(AHIRIKA_N)} {having(AHIRIKA_N, N['ahiriko'], True)}")
    L.append(f"{q(N['anottappī'])} {tq(ANOTTAPPA_N)} {ANOTTAPPA} {tc(ANOTTAPPA_N)} "
             f"{having(ANOTTAPPA_N, N['anottappī'], True)}")
    L.append(f"{q(N['dubbaco'])} {tq(DOVAC_N)} {DOVACASSATA} {tc(DOVAC_N)} {having(DOVAC_N, N['dubbaco'], True)}")
    L.append(f"{q(N['pāpamitto'])} {tq(PAPAM_N)} {PAPAMITTA_PEOPLE}{ASSOCIATE} {tc(PAPAM_N)} "
             f"{having(PAPAM_N, N['pāpamitto'], True)}")
    L.append(f"{q(N['indriyesu aguttadvāro'])} {tq(AGUTTA_N)} {INDRIYA_NEG} {tc(AGUTTA_N)} "
             f"{having(AGUTTA_N, N['indriyesu aguttadvāro'], True)}")
    L.append(f"{q(N['bhojane amattaññū'])} {tq(AMATTA_N)} {BHOJANA_NEG} {tc(AMATTA_N)} "
             f"{having(AMATTA_N, N['bhojane amattaññū'], True)}")
    L.append(f"{q(N['muṭṭhassati'])} {tq(MUTTH_N)} {MUTTHASSACCA} {tc(MUTTH_N)} "
             f"{having(MUTTH_N, N['muṭṭhassati'], True)}")
    L.append(f"{q(N['asampajāno'])} {tq(ASAMP_N)} Điều mà là {AVIJJA_A}{V60}{AVIJJA_B} {tc(ASAMP_N)} "
             f"{having(ASAMP_N, N['asampajāno'], True)}")
    L.append(f"{q(N['sīlavipanno'])} {tq(SILAV_N)} {VITIKKAMA} {tc(SILAV_N)} {DUSSILYA} "
             f"{having(SILAV_N, N['sīlavipanno'], True)}")
    L.append(f"{q(N['diṭṭhivipanno'])} {tq(DITTHIV_N)} “{NATTHI_A}{V62A}{NATTHI_B}{V62B}{NATTHI_C}”. "
             f"Điều mà thuộc loại như vậy là {DITTHI_LIST}{V62C}, đó được gọi là {DITTHIV_N}. {MICCHADITTHI_ALL} "
             f"{having(DITTHIV_N, N['diṭṭhivipanno'], True)}")
    # ^4-63 / ^4-64
    L.append(f"{q(N['ajjhattasaṃyojano'])} Người mà {LOWER5} chưa được dứt bỏ {close(N['ajjhattasaṃyojano'])}")
    L.append(f"{q(N['bahiddhāsaṃyojano'])} Người mà {UPPER5} chưa được dứt bỏ {close(N['bahiddhāsaṃyojano'])}")
    # ^4-65 … ^4-72: the same qualities abandoned
    L.append(f"{q(N['akkodhano'])} {tq(KODHA)} {KODHA_A}{KODHA_B} {tc(KODHA)} {yassa(KODHA, N['akkodhano'], True)}")
    L.append(f"{q(N['anupanāhī'])} {tq(UPANAHA)} {UPANAHA_A}{UPANAHA_B} {tc(UPANAHA)} "
             f"{yassa(UPANAHA, N['anupanāhī'], True)}")
    L.append(f"{q(N['amakkhī'])} {tq(MAKKHA)} {MAKKHA_A}{MAKKHA_B} {tc(MAKKHA)} {yassa(MAKKHA, N['amakkhī'], True)}")
    L.append(f"{q(N['apaḷāsī'])} {tq(PALASA_N)} {PALASA} {tc(PALASA_N)} {yassa(PALASA_N, N['apaḷāsī'], True)}")
    L.append(f"{q(N['anissukī'])} {tq(ISSA)} {ISSA_A}{ISSA_B} {tc(ISSA)} {yassa(ISSA, N['anissukī'], True)}")
    L.append(f"{q(N['amaccharī'])} {tq(MACCH)} {MACCHARIYA_LIST} {MACCHARIYA} {tc(MACCH)} "
             f"{yassa(MACCH, N['amaccharī'], True)}")
    L.append(f"{q(N['asaṭho'])} {tq(SATH)} {SATHEYYA_A}{SATHEYYA_B} {tc(SATH)} {yassa(SATH, N['asaṭho'], True)}")
    L.append(f"{q(N['amāyāvī'])} {tq(MAYA)} {MAYA_A} – {MAYA_WISH} {MAYA_B} {tc(MAYA)} "
             f"{yassa(MAYA, N['amāyāvī'], True)}")
    # ^4-73 … ^4-82
    L.append(f"{q(N['hirimā'])} {tq(HIRI_N)} {HIRI} {tc(HIRI_N)} {having(HIRI_N, N['hirimā'], False)}")
    L.append(f"{q(N['ottappī'])} {tq(OTTAPPA_N)} {OTTAPPA} {tc(OTTAPPA_N)} {having(OTTAPPA_N, N['ottappī'], False)}")
    L.append(f"{q(N['suvaco'])} {tq(SOVAC_N)} {SOVACASSATA} {tc(SOVAC_N)} {having(SOVAC_N, N['suvaco'], False)}")
    L.append(f"{q(N['kalyāṇamitto'])} {tq(KALYM_N)} {KALYANAMITTA_PEOPLE}{ASSOCIATE} {tc(KALYM_N)} "
             f"{having(KALYM_N, N['kalyāṇamitto'], False)}")
    L.append(f"{q(N['indriyesu guttadvāro'])} {tq(GUTTA_N)} {INDRIYA_POS} {tc(GUTTA_N)} "
             f"{having(GUTTA_N, N['indriyesu guttadvāro'], False)}")
    L.append(f"{q(N['bhojane mattaññū'])} {tq(MATTA_N)} {BHOJANA_POS} {tc(MATTA_N)} "
             f"{having(MATTA_N, N['bhojane mattaññū'], False)}")
    L.append(f"{q(N['upaṭṭhitassati'])} {tq(SATI_N)} {SATI} {tc(SATI_N)} "
             f"{having(SATI_N, N['upaṭṭhitassati'], False)}")
    L.append(f"{q(N['sampajāno'])} {tq(SAMP_N)} Điều mà là {PANNA_LIST} {tc(SAMP_N)} "
             f"{having(SAMP_N, N['sampajāno'], False)}")
    L.append(f"{q(N['sīlasampanno'])} {tq(SILAS_N)} {B.cap(AVITIKKAMA)} {tc(SILAS_N)} {SILASAMVARA} "
             f"{having(SILAS_N, N['sīlasampanno'], False)}")
    L.append(f"{q(N['diṭṭhisampanno'])} {tq(DITTHIS_N)} “{ATTHI}”. Điều mà thuộc loại như vậy là {PANNA_PE} "
             f"{tc(DITTHIS_N)} {SAMMADITTHI_ALL} {having(DITTHIS_N, N['diṭṭhisampanno'], False)}")
    # ^4-83 … ^4-87: sentence items of the matrix
    rare = "khó tìm gặp trong thế gian"
    L.append(f"Hai hạng người nào {rare}? Người làm ơn trước, và người biết ơn, đền ơn – hai hạng người này {rare}.")
    kept, given = "nhận được thứ gì cũng cất giữ lại", "nhận được thứ gì cũng đem cho đi"
    nkept, ngiven = "nhận được thứ gì cũng không cất giữ lại", "nhận được thứ gì cũng không đem cho đi"
    hard, easy = "khó làm cho thỏa mãn", "dễ làm cho thỏa mãn"
    L.append(f"Hai hạng người nào {hard}? Người {kept}, và người {given} – hai hạng người này “{hard}”.")
    L.append(f"Hai hạng người nào {easy}? Người {nkept}, và người {ngiven} – hai hạng người này “{easy}”.")
    regret_not_due = "hối tiếc về điều không đáng hối tiếc"
    regret_due = "hối tiếc về điều đáng hối tiếc"
    grow, nogrow = "tăng trưởng", "không tăng trưởng"
    L.append(f"Các ô nhiễm của hai hạng người nào {grow}? Người {regret_not_due}, và người không {regret_due} "
             f"– các ô nhiễm của hai hạng người này {grow}.")
    L.append(f"Các ô nhiễm của hai hạng người nào {nogrow}? Người không {regret_not_due}, và người {regret_due} "
             f"– các ô nhiễm của hai hạng người này {nogrow}.")
    # ^4-88 / ^4-89
    L.append(f"{q(N['hīnādhimutto'])} {B.IDHEKACCO} phạm giới, có phẩm chất xấu; người ấy {SEVATI} với người "
             f"khác phạm giới, có phẩm chất xấu {close(N['hīnādhimutto'])}")
    L.append(f"{q(N['paṇītādhimutto'])} {B.IDHEKACCO} giữ giới, có phẩm chất tốt; người ấy {SEVATI} với người "
             f"khác giữ giới, có phẩm chất tốt {close(N['paṇītādhimutto'])}")
    # ^4-90 (two lines)
    L.append(f"{q(N['titto'])} Các {N['paccekasambuddho']}{V90A} và những đệ tử A-la-hán của Như Lai là những "
             f"{N['titto']}. {B.cap(N['sammāsambuddho'])} vừa là {N['titto']}, vừa là {N['tappetā']}{V90B}.")
    L.append(B.NIDDESA_CLOSER[2])
    return L


def main():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS + NOUNS_PI if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    B.check_cross_book()
    L = lines()
    text = B.assemble(CH, L)
    # every Duka person name of the matrix (B.NAME) is the question and the quoted name of its definition
    for it in B.DUKA:
        if isinstance(it, tuple):
            for p in (it[0], it[2]):
                if p == "tappetā":          # defined inside the titto answer (^4-90), no question of its own
                    assert f"vừa là {B.NAME[p]}" in text, p
                    continue
                assert B.q(B.NAME[p]) in text, p
                if p != "titto":            # ^4-90 has no closing quote of the name
                    assert f"“{B.NAME[p]}”" in text, p
    for s in ("—", ":-", "….", "chánh niệm"):
        assert s not in text, s
    (B.OUT_DIR / CH).write_bytes(text.encode("utf-8"))
    print(f"OK: cross-book strings {len(CROSS) + len(NOUNS_PI)} (+ sample {len(B.CROSS_BOOK)}); "
          f"wrote {CH} ({len(L)} lines)")


if __name__ == "__main__":
    main()
