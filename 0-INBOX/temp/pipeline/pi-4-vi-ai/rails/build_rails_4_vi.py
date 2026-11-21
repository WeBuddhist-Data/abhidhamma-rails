"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 4 Tikapuggalapaññatti (^4-1-3-0, ^4-91 .. ^4-131).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/4-tikapuggalapannatti.md from fixed
strings, importing the approved sample constants (build_rails_sample_vi as S: NAME, frames, headings, closers).
Every repeat is one constant, so identical Pāli gives byte-identical Vietnamese.
At build time: every string marked (pi-1) / (pi-2) is asserted to occur in that book's approved Vietnamese rails;
every person name used is asserted to be a value of S.NAME; block IDs and per-segment line counts are checked
against the Pāli chapter.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-4.md.

usage: python -I -X utf8 build_rails_4_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (import writes nothing)

ROOT = S.ROOT
SRC = ROOT / "AI_translation/pali/pi-4_split_chapters/4-tikapuggalapannatti.md"
OUT = S.OUT_DIR / "4-tikapuggalapannatti.md"

cap = S.cap
q, cd, cs, cdp = S.q_katamo, S.close_dash, S.close_sentence, S.close_dash_pl
I = S.IDHEKACCO                       # Idhekacco puggalo = Ở đời này, có người
I_LC = "ở" + I[1:]                    # … evamevaṃ idhekacco puggalo (mid-sentence)
USED_NAMES = []


def N(k):
    v = S.NAME[k]
    USED_NAMES.append(v)
    return v


def bare(k):
    """Unquoted closer of an atthekacco name (^4-127..129): the NAME without its leading «có »."""
    v = N(k)
    assert v.startswith("có người "), v
    return v[len("có "):]


def tail(k):
    """The predicate of an atthekacco name: NAME without «có người »."""
    v = N(k)
    assert v.startswith("có người "), v
    return v[len("có người "):]


# ---------------------------------------------------------------------------------------------------------------
# Fixed strings (new ones are listed in notes-rails-4.md)
# ---------------------------------------------------------------------------------------------------------------
KHAYA = "nhờ sự diệt tận các ô nhiễm"                                     # āsavānaṃ khayā   (pi-2)
ARAHATTA_REST = ("ngay trong đời này tự mình hiểu biết trực tiếp, chứng nghiệm, chứng nhập và an trú "
                 "sự giải thoát của tâm, sự giải thoát nhờ trí tuệ, không còn ô nhiễm")      # (pi-2)
#   anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā upasampajja viharati
ARAHATTA = f"{I}, {KHAYA}, {ARAHATTA_REST}"                               # Idhekacco puggalo āsavānaṃ khayā … viharati
ARAHATTA_LC = "ở" + ARAHATTA[1:]
HEARS = f"Người ấy nghe – “Người ta nói rằng {KHAYA}, vị tỳ-khưu có tên như thế này {ARAHATTA_REST}”."
#   So suṇāti – "itthannāmo kira bhikkhu āsavānaṃ khayā … viharatī"ti.
WISH = f"“Đến bao giờ tôi cũng sẽ, {KHAYA}, {ARAHATTA_REST}?”"
#   "kudāssu nāmāhampi āsavānaṃ khayā … viharissāmī"ti
THINK = f"Người ấy nghĩ như vầy – {WISH}"                                 # Tassa evaṃ hoti – "…"ti.
NOT_THINK = f"Người ấy không nghĩ như vầy – {WISH}"                       # Tassa na evaṃ hoti – "…"ti.
WHY = "Vì sao vậy?"                                                        # Taṃ kissa hetu?   (pi-2)
DUSSILA = ("phạm giới, có phẩm chất xấu, không trong sạch, có hành vi đáng ngờ, có việc làm che giấu, "
           "không phải sa-môn mà tự xưng là sa-môn, không sống đời sống tu hành trong sạch mà tự xưng là "
           "sống đời sống tu hành trong sạch, mục nát bên trong, rỉ chảy dục vọng, trở nên như rác rưởi")
#   dussīlo hoti pāpadhammo asuci saṅkassarasamācāro paṭicchannakammanto assamaṇo samaṇapaṭiñño abrahmacārī
#   brahmacāripaṭiñño antopūti avassuto kasambujāto
SILAVA = "giữ giới, có phẩm chất tốt"                                      # sīlavā hoti kalyāṇadhammo
SO_LIKEWISE = "Cũng như vậy"                                               # Evamevaṃ (sentence start)
LIKEWISE = "cũng như vậy"                                                  # evamevaṃ (after a simile clause)
PANA = "Lại nữa, ở đời này, có"                                            # Idha panekacco …   («Lại nữa» pi-2)
AMONG = "Trong số đó"                                                      # Tatra yvāyaṃ …
WORLD = "là có thật, được tìm thấy trên thế gian"                          # santo saṃvijjamānā lokasmiṃ
MONKS = "là có thật, được tìm thấy trong số các vị tỳ-khưu"                 # santo saṃvijjamānā bhikkhūsu
KATAME_TAYO = "Ba hạng người ấy là những ai?"                              # Katame tayo?

# ^4-94 the sick
G_ANY = ("dù có được thức ăn thích hợp hay không có được thức ăn thích hợp, dù có được thuốc men thích hợp hay "
         "không có được thuốc men thích hợp, dù có được người chăm sóc phù hợp hay không có được người chăm sóc "
         "phù hợp")
#   labhanto vā sappāyāni bhojanāni alabhanto vā … patirūpaṃ upaṭṭhākaṃ
G_ONLY = ("khi có được thức ăn thích hợp chứ không phải khi không có được, khi có được thuốc men thích hợp chứ "
          "không phải khi không có được, khi có được người chăm sóc phù hợp chứ không phải khi không có được")
#   labhanto sappāyāni bhojanāni no alabhanto, … labhanto patirūpaṃ upaṭṭhākaṃ no alabhanto
T_ANY = ("dù có được dịp thấy Như Lai hay không có được dịp thấy Như Lai, dù có được dịp nghe Giáo Pháp và Giới "
         "Luật do Như Lai tuyên bố hay không có được dịp nghe Giáo Pháp và Giới Luật do Như Lai tuyên bố")
T_ONLY = ("khi có được dịp thấy Như Lai chứ không phải khi không có được, khi có được dịp nghe Giáo Pháp và Giới "
          "Luật do Như Lai tuyên bố chứ không phải khi không có được")
OKKAMATI = S.NIYAMA.replace("có khả năng ", "", 1)
#   okkamati niyāmaṃ kusalesu dhammesu sammattaṃ = bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện
assert OKKAMATI != S.NIYAMA

# ^4-95 .. ^4-97
TRUTH_1 = S.TRUTHS.split(", hiểu rõ")[0]                                  # "idaṃ dukkha"nti yathābhūtaṃ pajānāti
TATHAGATA_LC = "v" + S.TATHAGATA[1:-1]                                     # , tathāgatappaveditā cassa … vocaritā,
assert TATHAGATA_LC.startswith("và Giáo Pháp") and S.TATHAGATA.endswith(".")

# ^4-98 / ^4-99
WITNESS = ("khi được đưa ra trước hội đồng, hoặc trước hội chúng, hoặc giữa những người thân, hoặc giữa phường hội, "
           "hoặc giữa hoàng tộc, và được hỏi để làm chứng")
#   sabhaggato vā parisaggato vā ñātimajjhagato vā pūgamajjhagato vā rājakulamajjhagato vā abhinīto sakkhipuṭṭho
EHI = "“Này ông, hãy đến đây{}, hãy nói điều ông biết”"                     # "ehambho, purisa, yaṃ jānāsi taṃ vadehī"ti
N_EHI = " [dị bản (Syā., Ka.): ehi bho; Trung Bộ Kinh 1.440; Tăng Chi Bộ Kinh 3.28]"
SAYS_BAD = ("người ấy không biết mà nói – “Tôi biết”, biết mà nói – “Tôi không biết”, không thấy mà nói – "
            "“Tôi thấy”, thấy mà nói – “Tôi không thấy”")
SAYS_GOOD = ("người ấy không biết mà nói – “Tôi không biết”, biết mà nói – “Tôi biết”, không thấy mà nói – "
             "“Tôi không thấy”, thấy mà nói – “Tôi thấy”")
HETU = ("vì lợi ích của bản thân, hoặc vì lợi ích của người khác, hoặc vì một chút lợi lộc vật chất nhỏ nhặt")
#   attahetu vā parahetu vā āmisakiñcikkhahetu vā
MADHU = ("không có lỗi, dễ chịu với tai, dễ mến, thấm vào lòng, lịch sự, được nhiều người yêu mến, "
         "được nhiều người ưa thích")                                      # nelā … bahujanamanāpā   (pi-1)

# ^4-101 / ^4-125 the angry one and the similes
KODHANA = ("giận dữ, dễ bực tức; dù chỉ bị nói một chút, người ấy cũng nổi cáu, nổi giận, khởi thù hằn, "
           "trở nên cố chấp{}, bộc lộ sự nổi nóng, sự sân hận và sự bất mãn")
#   kodhano hoti upāyāsabahulo, appampi vutto samāno abhisajjati kuppati byāpajjati patitthīyati, kopañca
#   dosañca appaccayañca pātukaroti
ARUKA = "Giống như vết thương lở loét bị que gỗ hoặc mảnh sành{} chạm vào thì càng chảy mủ{} nhiều hơn nữa"
#   Seyyathāpi nāma duṭṭhāruko kaṭṭhena vā kaṭhalāya vā ghaṭṭito bhiyyoso mattāya āsavaṃ deti
ALATA = ("Giống như khúc củi cây thị đang cháy bị que gỗ hoặc mảnh sành chạm vào thì càng kêu xèo xèo, "
         "nổ lách tách nhiều hơn nữa")
#   Seyyathāpi nāma tindukālātaṃ kaṭṭhena vā kaṭhalāya vā ghaṭṭitaṃ bhiyyoso mattāya cicciṭāyati ciṭiciṭāyati
GUTHAKUPA = "Giống như hố phân bị que gỗ hoặc mảnh sành chạm vào thì càng bốc mùi hôi thối nhiều hơn nữa"
#   Seyyathāpi nāma gūthakūpo kaṭṭhena vā kaṭhalāya vā ghaṭṭito bhiyyoso mattāya duggandho hoti

# ^4-104 .. ^4-106
EYE1 = ("loại con mắt mà nhờ con mắt ấy có thể đạt được tài sản chưa đạt được, hoặc làm cho tài sản đã đạt được "
        "tăng thêm")
#   tathārūpaṃ cakkhu … yathārūpena cakkhunā anadhigataṃ vā bhogaṃ adhigaccheyya, adhigataṃ vā bhogaṃ phātiṃ kareyya
EYE2 = ("loại con mắt mà nhờ con mắt ấy có thể biết các hiện tượng thiện và bất thiện, biết các hiện tượng có lỗi "
        "và không có lỗi, biết các hiện tượng thấp kém và ưu việt, biết các hiện tượng đen tối và trong sáng cùng "
        "với các mặt đối lập của chúng")
#   … kusalākusale dhamme jāneyya, sāvajjānavajje …, hīnappaṇīte …, kaṇhasukkasappaṭibhāge dhamme jāneyya

# ^4-107 .. ^4-109
GOES = "thường xuyên đến{} tu viện để nghe Giáo Pháp{} nơi các vị tỳ-khưu"
#   ārāmaṃ gantā hoti abhikkhaṇaṃ bhikkhūnaṃ santike dhammassavaṇāya
TEACH = ("Các vị tỳ-khưu thuyết giảng Giáo Pháp cho người ấy, tốt đẹp ở phần đầu, tốt đẹp ở phần giữa, tốt đẹp ở "
         "phần cuối, có ý nghĩa, có văn từ, và làm sáng tỏ đời sống tu hành trong sạch hoàn toàn đầy đủ, thanh tịnh.")
#   Tassa bhikkhū dhammaṃ desenti ādikalyāṇaṃ … kevalaparipuṇṇaṃ parisuddhaṃ brahmacariyaṃ pakāsenti.
_NEG = "không chú tâm đến {0}phần đầu của bài giảng ấy, không chú tâm đến {0}phần giữa, không chú tâm đến {0}phần cuối"
_POS = "chú tâm đến cả phần đầu của bài giảng ấy, chú tâm đến cả phần giữa, chú tâm đến cả phần cuối"
SIT_NEG = f"Người ấy, khi ngồi ở chỗ ngồi ấy, {_NEG.format('')}."
#   So tasmiṃ āsane nisinno tassā kathāya neva ādiṃ manasi karoti, na majjhaṃ …, na pariyosānaṃ manasi karoti.
SIT_POS = f"Người ấy, khi ngồi ở chỗ ngồi ấy, {_POS}."                     # … ādimpi manasi karoti, majjhampi …
UP_NEG_PI = f"Khi đã đứng dậy khỏi chỗ ngồi ấy, người ấy cũng {_NEG.format('')}."   # Vuṭṭhitopi … neva ādiṃ …
UP_POS_PI = f"Khi đã đứng dậy khỏi chỗ ngồi ấy, người ấy cũng {_POS}."               # Vuṭṭhitopi … ādimpi …
UP_NEG_KHO = f"Nhưng khi đã đứng dậy khỏi chỗ ngồi ấy, người ấy quả thật {_NEG.format('')}."
#   Vuṭṭhito ca kho tamhā āsanā tassā kathāya neva ādiṃ manasi karoti, …
UP_NEG_KHO_PI = f"Nhưng khi đã đứng dậy khỏi chỗ ngồi ấy, người ấy quả thật {_NEG.format('ngay cả ')}."
#   Vuṭṭhito ca kho … neva ādimpi manasi karoti, na majjhampi …, na pariyosānampi … (^4-108, second time)

# ^4-113 .. ^4-115
KUJJHATI = "thường hay nổi giận"                                           # abhiṇhaṃ kujjhati
ANUSETI = "Và sự giận dữ ấy quả thật nằm sẵn nơi người ấy lâu dài suốt một thời gian dài"
#   So ca khvassa kodho ciraṃ dīgharattaṃ anuseti
NA_ANUSETI = "Và sự giận dữ ấy quả thật không nằm sẵn nơi người ấy lâu dài suốt một thời gian dài"
VUCCAMANO = "dù bị nói lời gay gắt, dù bị nói lời thô ác, dù bị nói lời không dễ ưa, vẫn hòa hợp{}, vẫn gắn bó{}, vẫn thân thiện{}"
#   āgāḷhenapi vuccamāno pharusenapi vuccamāno amanāpenapi vuccamāno saṃsandatimeva sandhiyatimeva sammodatimeva
N_CEVA = " [khác chính tả (Syā.): … ceva; Tăng Chi Bộ Kinh 3.133]"

# ^4-116 / ^4-117 the two cloths
LIKE = "người này cũng giống như vậy"                                      # tathūpamo ayaṃ puggalo
SERVE = "Những ai gần gũi, kết giao, thân cận vị ấy, noi theo gương của vị ấy, thì điều đó quả thật đem lại cho họ"
#   Ye kho panassa sevanti bhajanti payirupāsanti diṭṭhānugatiṃ āpajjanti, tesaṃ taṃ hoti …
REQUISITES = "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh"   # (pi-2)
#   cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāraṃ
RECEIVE = "Những người mà từ họ vị ấy{} nhận{} " + REQUISITES + ", thì điều đó"
#   Yesaṃ kho pana so paṭiggaṇhāti …, tesaṃ taṃ …
THERO = "Nếu vị tỳ-khưu trưởng lão như vậy nói giữa Tăng đoàn, thì các vị tỳ-khưu nói {} vị ấy như vầy –"
#   Evarūpo ce thero bhikkhu saṅghamajjhe bhaṇati(.|,) Tamenaṃ bhikkhū evamāhaṃsu –
NAVO = "Nếu một vị tỳ-khưu dù mới tu"                                      # Navo cepi bhikkhu hoti
MAJJHIMO_THERO = "Nếu một vị tỳ-khưu dù thuộc bậc trung… nếu một vị tỳ-khưu dù là trưởng lão"
#   Majjhimo cepi bhikkhu (hoti)…pe… thero cepi bhikkhu hoti


def potthaka_body(subject):
    p = "vải gai thô"
    return (f"{subject} mà phạm giới, có phẩm chất xấu, thì đây là sự xấu xí của vị ấy. Giống như {p} ấy xấu xí, "
            f"{LIKE}. {SERVE} sự bất lợi và khổ đau trong một thời gian dài. Đây là sự khó chịu khi tiếp xúc của vị "
            f"ấy. Giống như {p} ấy khó chịu khi tiếp xúc, {LIKE}. {RECEIVE.format('', '')} không đem lại cho họ quả "
            f"lớn, không đem lại lợi ích lớn. Đây là sự ít giá trị của vị ấy. Giống như {p} ấy ít giá trị, {LIKE}.")


def kasika_body(subject, n1="", n2=""):
    k = "vải xứ Ca-thi"
    return (f"{subject} mà giữ giới, có phẩm chất tốt, thì đây là sự đẹp đẽ của vị ấy. Giống như {k} ấy đẹp, "
            f"{LIKE}. {SERVE} sự lợi ích và hạnh phúc trong một thời gian dài. Đây là sự dễ chịu khi tiếp xúc của "
            f"vị ấy. Giống như {k} ấy dễ chịu khi tiếp xúc, {LIKE}. {RECEIVE.format(n1, n2)} đem lại cho họ quả "
            f"lớn, đem lại lợi ích lớn. Đây là sự có giá trị lớn của vị ấy. Giống như {k} ấy có giá trị lớn, {LIKE}.")


# ^4-121 .. ^4-126 the ones to be associated with
SIMILAR_TO = "về giới hạnh, định tâm và trí tuệ"                          # sīlena samādhinā paññāya
EVARUPO = "Người như vậy"                                                  # Evarūpo puggalo
TASMA = "Vì thế, người như vậy"                                            # Tasmā evarūpo puggalo
KINCAPI = "Dù một người không noi theo gương của người như vậy, nhưng quả thật tiếng {} vẫn lan truyền về người ấy"
#   Kiñcāpi evarūpassa puggalassa na diṭṭhānugatiṃ āpajjati, atha kho naṃ pāpako / kalyāṇo kittisaddo abbhuggacchati
REPUTE_BAD = "“Con người kết bạn với người xấu, có bạn đồng hành xấu, nghiêng về phía điều xấu”"
#   "pāpamitto purisapuggalo pāpasahāyo pāpasampavaṅko"ti
REPUTE_GOOD = "“Con người kết bạn với người tốt, có bạn đồng hành tốt, nghiêng về phía điều tốt”"
SOTA_SAKA = "Bậc vào dòng và bậc trở lại một lần"                          # Sotāpannasakadāgāmino
ANAGAMI = cap(S.NAME["anāgāmī"])                                           # Anāgāmī
ARAHA = cap(S.NAME["arahā"])                                               # Arahā

# ^4-130 / ^4-131 the teachers
SATTHA_I = "Ở đời này, có bậc đạo sư"                                      # Idhekacco satthā
SATTHA_PANA = "Lại nữa, ở đời này, có bậc đạo sư"                          # Idha panekacco satthā
SATTHA_TATRA = "Trong số đó, bậc đạo sư nào {}, thì cần hiểu bậc đạo sư ấy là {}."
#   Tatra yvāyaṃ satthā …, X satthā tena daṭṭhabbo.
P_K = "đề ra{} sự hiểu biết trọn vẹn về các dục lạc"                        # kāmānaṃ pariññaṃ paññapeti
P_R = "đề ra sự hiểu biết trọn vẹn về các hình sắc"                        # rūpānaṃ pariññaṃ paññapeti
P_V = "đề ra sự hiểu biết trọn vẹn về các cảm giác"                        # vedanānaṃ pariññaṃ paññapeti
ATTA_D = "đề ra tự ngã như là sự thật, như là điều chắc chắn ngay trong đời này"
#   diṭṭhe ceva dhamme attānaṃ saccato thetato paññapeti
ATTA_A = "đề ra tự ngã như là sự thật, như là điều chắc chắn trong đời sau"
#   abhisamparāyaṃ attānaṃ saccato thetato paññapeti

# ---------------------------------------------------------------------------------------------------------------
# Strings taken unchanged from the approved pi-1 / pi-2 Vietnamese rails (asserted at build time)
# ---------------------------------------------------------------------------------------------------------------
REUSED = [
    ("āsavānaṃ khayā", KHAYA, "2"),
    ("anāsavaṃ cetovimuttiṃ … upasampajja viharati", ARAHATTA_REST, "2"),
    ("itthannāma-", "có tên như thế này", "2"),
    ("Tassa evaṃ hoti", "nghĩ như vầy", "2"),
    ("Taṃ kissa hetu?", WHY, "2"),
    ("Puna caparaṃ / pana", "Lại nữa", "2"),
    ("dussīlo / sīlavā", "phạm giới", "2"),
    ("sīlavā", "giữ giới", "2"),
    ("dussīlaṃ pāpadhammaṃ sevati bhajati payirupāsati (pi-4 ch3)", "gần gũi, kết giao, thân cận", "2"),
    ("cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāra", REQUISITES, "2"),
    ("musāvāda", "việc nói dối", "2"),
    ("nelā kaṇṇasukhā pemaniyā hadayaṅgamā porī bahujanakantā bahujanamanāpā", MADHU, "1"),
    ("kopo", "sự nổi nóng", "1"),
    ("dosa", "sự sân hận", "1"),
    ("anattamano / anattamanatā", "không hài lòng", "1"),
    ("muṭṭhassati", "mất tỉnh thức", "2"),
    ("upaṭṭhitassati", "có sự tỉnh thức được thiết lập", "2"),
    ("asamāhito", "không được định tâm", "2"),
    ("kāmesu vītarāgo", "lìa tham đắm đối với các dục lạc", "2"),
    ("manasi karoti", "chú tâm đến", "2"),
    ("rūpāvacara(arūpāvacara)samāpatti", "thành tựu thiền thuộc cõi hình sắc", "2"),
    ("arūpāvacara", "cõi không hình sắc", "2"),
    ("saccato thetato", "như là sự thật, như là điều chắc chắn", "2"),
    ("sassatavāda", "học thuyết về sự trường tồn", "2"),
    ("ucchedavāda", "học thuyết về sự đoạn diệt", "2"),
    ("ma. ni. (citation)", "Trung Bộ Kinh", "2"),
    ("a. ni. (citation)", "Tăng Chi Bộ Kinh", "2"),
    ("(sabbattha) variant", "dị bản (mọi bản)", "2"),
]


def seg(*lines):
    return "\n".join(lines)


def build():
    S_ = [seg(S.H_CHAPTER[3] + " ^4-1-3-0")]
    a = []
    # ^4-91 .. ^4-93
    a.append(seg(f"{q(N('nirāso'))} {I} {DUSSILA}. {HEARS} {NOT_THINK} {cs(N('nirāso'))} ^4-91"))
    a.append(seg(f"{q(N('āsaṃso'))} {I} {SILAVA}. {HEARS} {THINK} {cs(N('āsaṃso'))} ^4-92"))
    a.append(seg(f"{q(N('vigatāso'))} {ARAHATTA}. {HEARS} {NOT_THINK} {WHY} Vì trước đây, khi người ấy chưa được "
                 f"giải thoát, có sự mong cầu được giải thoát, thì sự mong cầu ấy đã lắng xuống. "
                 f"{cs(N('vigatāso'))} ^4-93"))
    # ^4-94 the three like the sick
    sick = N("tayo gilānūpamā puggalā")
    a.append(seg(
        f"Ở đây, {sick} là những ai? Có ba người bệnh – ở đời này, có người bệnh, {G_ANY}, vẫn không khỏi bệnh ấy. (1)",
        f"{PANA} người bệnh, {G_ANY}, vẫn khỏi bệnh ấy. (2)",
        f"{PANA} người bệnh {G_ONLY}, thì khỏi bệnh ấy. (3)",
        f"{AMONG}, người bệnh nào {G_ONLY} thì khỏi bệnh ấy, chính vì người bệnh này mà Đức Thế Tôn đã cho phép bữa ăn "
        "cho người bệnh, đã cho phép thuốc men cho người bệnh, đã cho phép người chăm sóc người bệnh. Và cũng vì người "
        "bệnh này mà những người bệnh khác cũng cần được chăm sóc.",
        f"{SO_LIKEWISE} [khác chính tả (Sī.): evameva], {sick} {WORLD}. {KATAME_TAYO} {I}, {T_ANY}, vẫn không "
        f"{OKKAMATI}. (1)",
        f"{PANA} người, {T_ANY}, vẫn {OKKAMATI}. (2)",
        f"{PANA} người {T_ONLY}, thì {OKKAMATI}. (3)",
        f"{AMONG}, người nào {T_ONLY} thì {OKKAMATI}, chính vì người này mà Đức Thế Tôn đã cho phép việc thuyết giảng "
        f"Giáo Pháp, và cũng vì người này mà Giáo Pháp cần được thuyết giảng cho cả những người khác. "
        f"{cap(sick)} này {WORLD}. ^4-94"))
    # ^4-95 .. ^4-97
    a.append(seg(f"{q(N('kāyasakkhī'))} {I} {S.VIMOKKHA}, và {S.DISVA_EKACCE} {cd(N('kāyasakkhī'))} ^4-95"))
    a.append(seg(f"{q(N('diṭṭhippatto'))} {I} {S.TRUTHS}, {TATHAGATA_LC}, và {S.DISVA_EKACCE} "
                 f"{cd(N('diṭṭhippatto'))} ^4-96"))
    a.append(seg(f"{q(N('saddhāvimutto'))} {I} {TRUTH_1}… {TATHAGATA_LC}, và {S.DISVA_EKACCE}, nhưng quả thật không "
                 f"như ở {N('diṭṭhippatto')} {cd(N('saddhāvimutto'))} ^4-97"))
    # ^4-98 .. ^4-100 speech
    a.append(seg(f"{q(N('gūthabhāṇī'))} {I} nói dối: {WITNESS} – {EHI.format(N_EHI)}, {SAYS_BAD}. Như vậy, {HETU}, "
                 f"người ấy cố ý nói dối {cd(N('gūthabhāṇī'))} ^4-98"))
    a.append(seg(f"{q(N('pupphabhāṇī'))} {I} sau khi dứt bỏ việc nói dối, kiêng tránh việc nói dối: {WITNESS} – "
                 f"{EHI.format('')}, {SAYS_GOOD}. Như vậy, dù {HETU}, người ấy cũng không cố ý nói dối "
                 f"{cd(N('pupphabhāṇī'))} ^4-99"))
    a.append(seg(f"{q(N('madhubhāṇī'))} {I} nói loại lời nói như sau: lời nói {MADHU} {cd(N('madhubhāṇī'))} ^4-100"))
    # ^4-101 .. ^4-103 minds
    k_n = KODHANA.format(" [khác chính tả (Syā., Ka.): patiṭṭhīyati; Tăng Chi Bộ Kinh 3.25]")
    k_0 = KODHANA.format("")
    aruka_n = ARUKA.format(" [khác chính tả (Ka.): kathalāya, (Chú giải): kathalena; Tăng Chi Bộ Kinh 3.25]",
                           " [dị bản (Sī.): assavanoti]")
    aruka_0 = ARUKA.format("", "")
    nm = N("arukūpamacitto puggalo")
    a.append(seg(f"{q(nm)} {I} {k_n}. {aruka_n}, {LIKEWISE}, {I_LC} {k_0} {cd(nm)} ^4-101"))
    nm = N("vijjūpamacitto puggalo")
    a.append(seg(f"{q(nm)} {I} {S.TRUTHS}. Giống như một người có mắt, trong bóng tối dày đặc của đêm đen, khi tia "
                 f"chớp lóe lên, có thể thấy các hình sắc, {LIKEWISE}, {I_LC} {S.TRUTHS} {cd(nm)} ^4-102"))
    nm = N("vajirūpamacitto puggalo")
    a.append(seg(f"{q(nm)} {ARAHATTA}. Giống như đối với kim cương, không có gì không thể cắt đứt, dù là ngọc hay "
                 f"đá, {LIKEWISE}, {ARAHATTA_LC} {cd(nm)} ^4-103"))
    # ^4-104 .. ^4-106 eyes
    a.append(seg(f"{q(N('andho'))} {I} không có {EYE1}; người ấy cũng không có {EYE2} {cd(N('andho'))} ^4-104"))
    a.append(seg(f"{q(N('ekacakkhu'))} {I} có {EYE1}; nhưng người ấy không có {EYE2} {cd(N('ekacakkhu'))} ^4-105"))
    a.append(seg(f"{q(N('dvicakkhu'))} {I} có {EYE1}; người ấy cũng có {EYE2} {cd(N('dvicakkhu'))} ^4-106"))
    # ^4-107 .. ^4-109 wisdoms
    g_n = GOES.format(" [dị bản (Sī.): gato, (Syā.): gantvā]", " [khác chính tả (Syā.): dhammassavanāya]")
    g_0 = GOES.format("", "")
    nm = N("avakujjapañño puggalo")
    a.append(seg(f"{q(nm)} {I} {g_n}. {TEACH} {SIT_NEG} {UP_NEG_PI} Giống như một cái chum bị úp ngược [khác chính tả "
                 f"(Syā.): nikujjo; Tăng Chi Bộ Kinh 3.30], nước đổ vào đó thì chảy tràn đi, không đọng lại; "
                 f"{LIKEWISE}, {I_LC} {g_0}. {TEACH} {SIT_NEG} {UP_NEG_PI[:-1]} {cd(nm)} ^4-107"))
    nm = N("ucchaṅgapañño puggalo")
    a.append(seg(f"{q(nm)} {I} {g_0}. {TEACH} {SIT_POS} {UP_NEG_KHO} Giống như trong vạt áo của một người có đựng các "
                 "loại đồ ăn khác nhau – mè, gạo [khác chính tả (Ka.): tilataṇḍulā; Tăng Chi Bộ Kinh 3.30], bánh ngọt, "
                 "táo ta. Khi đứng dậy khỏi chỗ ngồi ấy, vì mất tỉnh thức, người ấy có thể làm chúng rơi vãi. "
                 f"{SO_LIKEWISE}, {I_LC} {g_0}. {TEACH} {SIT_POS} {UP_NEG_KHO_PI[:-1]} {cd(nm)} ^4-108"))
    nm = N("puthupañño puggalo")
    a.append(seg(f"{q(nm)} {I} {g_0}. {TEACH} {SIT_POS} {UP_POS_PI} Giống như một cái chum được đặt ngửa, nước đổ vào "
                 f"đó thì đọng lại, không chảy tràn đi; {LIKEWISE}, {I_LC} {g_0}. {TEACH} {SIT_POS} {UP_POS_PI[:-1]} "
                 f"{cd(nm)} ^4-109"))
    # ^4-110 .. ^4-112 passion
    nm = N("kāmesu ca bhavesu ca avītarāgo")
    a.append(seg(f"{q(nm)} {SOTA_SAKA} {cdp(nm)} ^4-110"))
    nm = N("kāmesu vītarāgo bhavesu avītarāgo")
    a.append(seg(f"{q(nm)} {ANAGAMI} {cd(nm)} ^4-111"))
    nm = N("kāmesu ca bhavesu ca vītarāgo")
    a.append(seg(f"{q(nm)} {ARAHA} {cd(nm)} ^4-112"))
    # ^4-113 .. ^4-115 lines
    nm = N("pāsāṇalekhūpamo puggalo")
    a.append(seg(f"{q(nm)} {I} {KUJJHATI}. {ANUSETI}. Giống như đường vạch trên đá không nhanh chóng bị xóa mờ bởi "
                 f"gió hoặc bởi nước, mà tồn tại lâu dài; {LIKEWISE}, {I_LC} {KUJJHATI}. {ANUSETI} {cd(nm)} ^4-113"))
    nm = N("pathavilekhūpamo puggalo")
    a.append(seg(f"{q(nm)} {I} {KUJJHATI}. {NA_ANUSETI}. Giống như đường vạch trên đất [khác chính tả (Sī., Syā.): "
                 f"paṭhaviyā] nhanh chóng bị xóa mờ bởi gió hoặc bởi nước, không tồn tại lâu dài; {LIKEWISE}, {I_LC} "
                 f"{KUJJHATI}. {NA_ANUSETI} {cd(nm)} ^4-114"))
    nm = N("udakalekhūpamo puggalo")
    a.append(seg(f"{q(nm)} {I} {VUCCAMANO.format(N_CEVA, N_CEVA, N_CEVA)}. Giống như đường vạch trên nước nhanh chóng "
                 f"bị xóa mờ, không tồn tại lâu dài; {LIKEWISE}, {I_LC} {VUCCAMANO.format('', '', '')} {cd(nm)} ^4-115"))
    # ^4-116 sackcloth
    pot = N("tayo potthakūpamā puggalā")
    a.append(seg(
        f"Ở đây, {pot} là những ai? Có ba loại vải gai thô – vải gai thô dù mới cũng xấu xí, khó chịu khi tiếp xúc và "
        "ít giá trị; vải gai thô dù đã dùng một thời gian cũng xấu xí, khó chịu khi tiếp xúc và ít giá trị; vải gai thô "
        "dù đã cũ cũng xấu xí, khó chịu khi tiếp xúc và ít giá trị. Ngay cả vải gai thô đã cũ, người ta hoặc dùng làm "
        f"giẻ lau nồi, hoặc vứt nó trên đống rác. {SO_LIKEWISE}, {pot} này {MONKS}. {KATAME_TAYO} "
        + potthaka_body(NAVO),
        potthaka_body(MAJJHIMO_THERO),
        f"{THERO.format('với')} “Lời nói của kẻ ngu dốt, thiếu hiểu biết như ông thì có ích gì, ông mà cũng nghĩ rằng "
        "mình nên nói sao”! Vị ấy nổi giận, không hài lòng, thốt ra loại lời nói khiến Tăng đoàn trục xuất vị ấy, "
        f"giống như người ta vứt vải gai thô trên đống rác. {cap(pot)} này {MONKS}. ^4-116"))
    # ^4-117 Kāsi cloth
    kas = N("tayo kāsikavatthūpamā puggalā")
    a.append(seg(
        f"Ở đây, {kas} là những ai? Có ba loại vải xứ Ca-thi – vải xứ Ca-thi dù mới cũng đẹp, dễ chịu khi tiếp xúc và "
        "có giá trị lớn; vải xứ Ca-thi dù đã dùng một thời gian cũng đẹp, dễ chịu khi tiếp xúc và có giá trị lớn; vải "
        "xứ Ca-thi dù đã cũ cũng đẹp, dễ chịu khi tiếp xúc và có giá trị lớn. Ngay cả vải xứ Ca-thi đã cũ, người ta "
        "hoặc dùng làm vải gói châu báu, hoặc cất nó trong hộp hương thơm.",
        f"{SO_LIKEWISE}, {kas} này {MONKS}. {KATAME_TAYO} "
        + kasika_body(NAVO, " [dị bản (mọi bản): yesaṃ kho pana; Tăng Chi Bộ Kinh 3.100]",
                      " [khác chính tả (Sī.): patigaṇhāti; nhưng phù hợp với Phụ chú giải về cách cấu tạo hình thức "
                      "từ]"),
        kasika_body(MAJJHIMO_THERO),
        f"{THERO.format('về')} “Thưa các tôn giả, hãy giữ im lặng, vị tỳ-khưu trưởng lão đang nói về Giáo Pháp và "
        "Giới Luật”. Lời nói ấy của vị ấy được ghi nhớ, giống như vải xứ Ca-thi được cất trong hộp hương thơm. "
        f"{cap(kas)} này {MONKS}. ^4-117"))
    # ^4-118 .. ^4-120 measure
    a.append(seg(f"{q(N('suppameyyo'))} {I} xao động, kiêu căng, nhẹ dạ, lắm lời, nói lời tản mạn, mất tỉnh thức, "
                 "không hiểu biết rõ ràng, không được định tâm, có tâm rối loạn, có giác quan buông lỏng "
                 f"{cd(N('suppameyyo'))} ^4-118"))
    a.append(seg(f"{q(N('duppameyyo'))} {I} không xao động, không kiêu căng, không nhẹ dạ, không lắm lời, không nói "
                 "lời tản mạn, có sự tỉnh thức được thiết lập, hiểu biết rõ ràng, được định tâm, có tâm hợp nhất, có "
                 f"giác quan được thu thúc {cd(N('duppameyyo'))} ^4-119"))
    a.append(seg(f"{q(N('appameyyo'))} {ARAHATTA} {cd(N('appameyyo'))} ^4-120"))
    # ^4-121 .. ^4-126 association
    k_na = "na sevitabbo na bhajitabbo na payirupāsitabbo"
    k_se = "sevitabbo bhajitabbo payirupāsitabbo"
    k_sa = "sakkatvā garuṃ katvā sevitabbo bhajitabbo payirupāsitabbo"
    k_ji = "jigucchitabbo na sevitabbo na bhajitabbo na payirupāsitabbo"
    k_aj = "ajjhupekkhitabbo na sevitabbo na bhajitabbo na payirupāsitabbo"
    a.append(seg(f"{q(N(k_na))} {I} kém hơn mình {SIMILAR_TO}. {EVARUPO} {tail(k_na)}, ngoại trừ vì lòng thương mến, "
                 "ngoại trừ vì lòng thương xót. ^4-121"))
    talk = "; ".join(
        f"khi chúng ta ngang bằng nhau về {x}, sẽ có cuộc trò chuyện về {x} giữa chúng ta, cuộc trò chuyện ấy sẽ "
        f"thoải mái với chúng ta, và sẽ được tiếp diễn{n} giữa chúng ta"
        for x, n in (("giới hạnh", ""), ("định tâm", " [khác chính tả (Sī.): pavattanī; Tăng Chi Bộ Kinh 3.26]"),
                     ("trí tuệ", "")))
    a.append(seg(f"{q(N(k_se))} {I} ngang bằng mình {SIMILAR_TO}. {EVARUPO} {tail(k_se)}. {WHY} “{cap(talk)}”. "
                 f"{TASMA} {tail(k_se)}. ^4-122"))
    fulfil = "; ".join(
        f"tôi sẽ làm cho đầy đủ khối {x} chưa đầy đủ, hoặc sẽ dùng trí tuệ hỗ trợ khối {x} đã đầy đủ ở chỗ này chỗ kia"
        for x in ("giới hạnh", "định tâm", "trí tuệ"))
    a.append(seg(f"{q(N(k_sa))} {I} hơn mình {SIMILAR_TO}. {EVARUPO} {tail(k_sa)}. {WHY} “{cap(fulfil)}”. "
                 f"{TASMA} {tail(k_sa)}. ^4-123"))
    a.append(seg(f"{q(N(k_ji))} {I} {DUSSILA}. {EVARUPO} {tail(k_ji)}. {WHY} {KINCAPI.format('xấu')} – {REPUTE_BAD}. "
                 "Giống như con rắn đã rơi vào phân, dù không cắn, nhưng quả thật vẫn làm vấy bẩn người ta; "
                 f"{LIKEWISE}, {KINCAPI.format('xấu')[0].lower()}{KINCAPI.format('xấu')[1:]} – {REPUTE_BAD}! "
                 f"{TASMA} {tail(k_ji)}. ^4-124"))
    a.append(seg(f"{q(N(k_aj))} {I} {k_0}. {aruka_0}, {LIKEWISE}, {I_LC} {k_0}. {ALATA}, {LIKEWISE}, {I_LC} {k_0}. "
                 f"{GUTHAKUPA}, {LIKEWISE}, {I_LC} {k_0}; {EVARUPO[0].lower()}{EVARUPO[1:]} {tail(k_aj)}. {WHY} "
                 "“Người ấy có thể mắng nhiếc tôi, có thể lăng mạ tôi, có thể làm điều bất lợi cho tôi”! "
                 f"{TASMA} {tail(k_aj)}. ^4-125"))
    a.append(seg(f"{q(N(k_se))} {I} {SILAVA} – {EVARUPO[0].lower()}{EVARUPO[1:]} {tail(k_se)}. {WHY} "
                 f"{KINCAPI.format('tốt')} – {REPUTE_GOOD}! {TASMA} {tail(k_se)}. ^4-126"))
    # ^4-127 .. ^4-129 practice
    k1 = "sīlesu paripūrakārī, samādhismiṃ mattaso kārī, paññāya mattaso kārī"
    k2 = "sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya mattaso kārī"
    k3 = "sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya ca paripūrakārī"
    a.append(seg(f"{q(N(k1))} {SOTA_SAKA} – những người này được gọi là {bare(k1)}. ^4-127"))
    a.append(seg(f"{q(N(k2))} {ANAGAMI} – người này được gọi là {bare(k2)}. ^4-128"))
    a.append(seg(f"{q(N(k3))} {ARAHA} – người này được gọi là {bare(k3)}. ^4-129"))
    # ^4-130 teachers
    s1 = f"{P_K}, không {P_R}, không {P_V}"
    s2 = f"{P_K}, {P_R}, nhưng không {P_V}"
    s3 = f"{P_K}, {P_R}, và {P_V}"
    note = " [khác chính tả (Sī., Syā.): paññāpeti]"
    sb = N("sammāsambuddho")
    a.append(seg(
        f"Ở đây, {N('tayo satthāro')} là những ai? {SATTHA_I} {s1.format(note)}. {SATTHA_PANA} {s2.format('')}. "
        f"{SATTHA_PANA} {s3.format('')}.",
        " ".join([SATTHA_TATRA.format(s1.format(''), "bậc đạo sư có được thành tựu thiền thuộc cõi hình sắc"),
                  SATTHA_TATRA.format(s2.format(''), "bậc đạo sư có được thành tựu thiền thuộc cõi không hình sắc"),
                  SATTHA_TATRA.format(s3.format(''), sb), "Đây là ba bậc đạo sư. ^4-130"])))
    t1 = f"{ATTA_D}, và {ATTA_A}"
    t2 = f"{ATTA_D}, nhưng quả thật không {ATTA_A}"
    t3 = f"không {ATTA_D}, và không {ATTA_A}"
    a.append(seg(
        f"Ở đây, {N('aparepi tayo satthāro')} là những ai? {SATTHA_I} {t1}. {SATTHA_PANA} {t2}. {SATTHA_PANA} {t3}.",
        " ".join([SATTHA_TATRA.format(t1, "bậc đạo sư theo học thuyết về sự trường tồn"),
                  SATTHA_TATRA.format(t2, "bậc đạo sư theo học thuyết về sự đoạn diệt"),
                  SATTHA_TATRA.format(t3, sb), "Đây là ba bậc đạo sư khác."]),
        S.CLOSER_CHAPTER[3] + " ^4-131"))
    return S_ + a


# ---------------------------------------------------------------------------------------------------------------
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def structure(text):
    out, n = [], 0
    for line in text.splitlines():
        if not line.strip():
            continue
        n += 1
        m = ID.search(line)
        if m:
            out.append((m.group(1), n))
            n = 0
    return out


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                        for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def main():
    check_reused()
    segs = build()
    names = set(S.NAME.values())
    assert all(n in names for n in USED_NAMES)
    text = unicodedata.normalize("NFC", "\n\n".join(segs) + "\n")
    assert "\n\n\n" not in text and "—" not in text and ":-" not in text and "…." not in text
    src = SRC.read_text(encoding="utf-8")
    assert structure(src) == structure(text), (structure(src), structure(text))
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, len(structure(text)), "segments")


if __name__ == "__main__":
    main()
