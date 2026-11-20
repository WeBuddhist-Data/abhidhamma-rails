"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapter 17 (Khuddakavatthuvibhaṅgo ^2-17-0 … ^2-977, with the ^2-U1 … ^2-U72 blocks).

Writes (only when run as a script, without --dry):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/17-khuddakavatthuvibhango.md
(the new formulas are listed by hand in rails/notes-17.md).

Translated fresh from the Pāli with the locked pi-2 termbase (mado «sự say sưa» vs māno «sự kiêu mạn» / atimāno «sự
ngạo mạn» / omāno «sự tự ti»; vossaggo «sự buông lơi»; bho «thưa ngài»; kamyatā «sự mong muốn»; ānantarika «có quả
không gián đoạn»; dhammā as the sixth sense object «đối tượng của ý»; rūpataṇhā «khao khát hình sắc» among the sense
objects vs «khao khát cõi hình sắc»; the closing labels «Phân loại theo nhóm N.» as ch. 16). Strings reused from the
approved pi-1 Vietnamese rails are marked pi1() and checked against those files by check_pi1(); strings from the
earlier pi-2 chapters are marked pi2() and checked by check_pi2(); a few long ones are read from those files (VI()).
Importing this module writes nothing.

usage: python -I -X utf8 build_rails_17_vi.py [--dry]
"""
import pathlib
import re
import sys
import unicodedata

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)
import build_rails_1_vi as K1      # noqa: E402
import build_rails_7_9_vi as K79   # noqa: E402

PART = "17-khuddakavatthuvibhango.md"
PI1_PALI = S.ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
PI2_DONE = ["1-khandhavibhango.md", "2-ayatanavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md",
            "5-indriyavibhango.md", "6-paticcasamuppadavibhango.md", "7-satipatthanavibhango.md",
            "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md", "10-bojjhangavibhango.md",
            "11-maggangavibhango.md", "12-jhanavibhango.md", "13-appamannavibhango.md", "14-sikkhapadavibhango.md",
            "15-patisambhidavibhango.md", "16-nanavibhango.md"]
cap, low = S.cap, K1.low
SLIPS, MISFITS, PI1_USED, PI2_USED = [], [], [], []
IDRX = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def note(lst, s):
    if s not in lst:
        lst.append(s)


def slip(s):
    note(SLIPS, s)


def misfit(s):
    note(MISFITS, s)


def pi1(s):
    note(PI1_USED, s)
    return s


def pi2(s):
    note(PI2_USED, s)
    return s


def _lines(p):
    return [IDRX.sub("", ln) for ln in p.read_text(encoding="utf-8").split("\n") if ln.strip()]


def VI(book, fname, pali_start, nth=0):
    """the Vietnamese line (read-only) whose Pāli line in the same file starts with pali_start"""
    pd, vd = (PI1_PALI, PI1_VI) if book == 1 else (S.PALI, S.OUT)
    P, V = _lines(pd / fname), _lines(vd / fname)
    hits = [i for i, ln in enumerate(P) if ln.startswith(pali_start)]
    assert len(hits) > nth, (book, fname, pali_start)
    return V[hits[nth]]


def body(v):
    """«Ở đây, X là gì? BODY – đó được gọi là …» -> BODY"""
    return v.split(" là gì? ", 1)[1].rsplit(" – đó được gọi là", 1)[0]


# =========================================================================== frames
LABEL = {"Ka": "a", "Kha": "b", "Ga": "c", "Gha": "d", "Ṅa": "đ", "Ca": "e", "Cha": "g", "Ja": "h"}
NUM = S.NUM
ORD = {1: "thứ nhất", 2: "thứ hai", 3: "thứ ba", 4: "thứ tư", 5: "thứ năm", 6: "thứ sáu", 7: "thứ bảy",
       8: "thứ tám"}


def q(x):
    """Tattha katamo/katamā/katamaṃ X?  ->  «Ở đây, X là gì?»"""
    return f"Ở đây, {x} là gì?"


def qn(x):
    """Tattha katame/katamāni/katamā N X? (counted)  ->  «Ở đây, N X là những gì?» (user decision)"""
    return f"Ở đây, {x} là những gì?"


def called(x, quoted=True):
    """– ayaṃ/idaṃ vuccati "X".  ->  «– đó được gọi là “X”.»"""
    if quoted:
        x = x.replace("“", "‘").replace("”", "’")          # nested quotation marks
        return f"– đó được gọi là “{x}”."
    return f"– đó được gọi là {x}."


def this_is(x, dash=True):
    """(–) imāni/ime/imā N X.  ->  «– đây là N X.» / «Đây là N X.»"""
    return f"– đây là {x}." if dash else f"Đây là {x}."


def lab(k, s):
    return f"({LABEL[k]}) {s}"


CLOSE = {n: f"Phân loại theo nhóm {NUM[n]}." for n in range(1, 11)}      # Ekakaṃ. … Dasakaṃ. (termbase; ch. 16)
pi2(CLOSE[10])
pi1(CLOSE[1])
DHS = "“Liệt kê các hiện tượng”"                                           # dha. sa. (pi-2 ch. 2, ch. 10)
pi2(f"xem {DHS} 9]")
AN = "Tăng Chi Bộ Kinh"                                                    # a. ni.
DN = "Trường Bộ Kinh"                                                      # dī. ni.

# =========================================================================== shared strings (pi-1 / pi-2)
WHICH = pi1("Điều mà là")                                                  # yo / yā / yaṃ (opening a list)
SUCH = pi1("điều mà thuộc loại như vậy là")                                # yo/yā/yaṃ evarūpo/ā/aṃ …
YA_TATTHA = pi1("Điều mà, ở đây, là")                                      # yo/yā/yaṃ tattha …
IDHEKACCO = pi2("Ở đời này, có người")                                     # Idhekacco (pi-2 ch. 3 ^2 vihiṃsādhātu)
MANA = pi1("sự kiêu mạn, sự tự đánh giá mình, trạng thái tự đánh giá mình, sự tự cao, sự vênh vang, ngọn cờ, "
           "sự tự đề cao, sự mong muốn được giương cờ của tâm")             # māno maññanā … ketukamyatā cittassa
MANA_A = "sự kiêu mạn, sự tự đánh giá mình, trạng thái tự đánh giá mình"
MANA_B = "sự mong muốn được giương cờ của tâm"
MADA = "sự say sưa, sự khởi say sưa, trạng thái khởi say sưa, " + MANA      # mado majjanā majjitattaṃ māno …
OMANA = ("sự tự ti, sự tự đánh giá thấp mình, trạng thái tự đánh giá thấp mình, sự tự chê bai, sự tự chê bai thậm "
         "tệ, trạng thái tự chê bai thậm tệ, sự tự coi thường, sự tự xem nhẹ, sự tự khinh miệt")
RAGA3 = "sự tham đắm, sự say đắm, sự say đắm của tâm"                       # rāgo sārāgo cittassa sārāgo
pi1("sự tham đắm, sự say đắm")
THOUGHT = "suy nghĩ, sự hướng tâm, tư duy sai lầm"                          # takko vitakko micchāsaṅkappo
SANNA3 = pi1("tri giác, sự nhận ra, trạng thái đã nhận ra")                 # saññā sañjānanā sañjānitattaṃ
DITTHI_S = pi1("điều mà thuộc loại như vậy là quan điểm, sự mắc kẹt trong các quan điểm… sự nắm giữ điều đảo "
               "ngược")                                                     # yā evarūpā diṭṭhi diṭṭhigataṃ…pe…
DITTHI_ARISES = "điều mà sinh khởi là quan điểm, sự mắc kẹt trong các quan điểm… sự nắm giữ điều đảo ngược"
AVIJJA_S = pi2("Điều mà là sự không biết, sự không thấy… then cài vô minh, sự si mê, tức gốc rễ bất thiện")
AVIJJA_TAIL = "sự không biết, sự không thấy… then cài vô minh, sự si mê, tức gốc rễ bất thiện"
KAMA8 = pi1("Điều mà, đối với các dục lạc, là ý muốn dục lạc, sự tham đắm dục lạc, sự thích thú dục lạc, khao khát "
            "dục lạc, sự luyến ái dục lạc, sự nóng bỏng vì dục lạc, sự mê đắm dục lạc, sự đắm chìm trong dục lạc")
KAMA_S = "Điều mà, đối với các dục lạc, là ý muốn dục lạc… sự đắm chìm trong dục lạc"
BHAVA8 = pi1("Điều mà, đối với sự hiện hữu, là ý muốn hiện hữu") + ", " + pi1(
    "sự tham đắm hiện hữu, sự thích thú hiện hữu, khao khát được hiện hữu, sự luyến ái hiện hữu, "
    "sự nóng bỏng vì hiện hữu, sự mê đắm hiện hữu, sự đắm chìm trong hiện hữu")   # pi-1 ^1-1104 (without its variant)
BHAVA_S = pi1("Điều mà, đối với sự hiện hữu, là ý muốn hiện hữu… sự đắm chìm trong hiện hữu")
TRUTHS = pi1("Sự không biết về khổ đau, sự không biết về sự phát sinh của khổ đau, sự không biết về sự chấm dứt khổ "
             "đau, sự không biết về cách thực hành dẫn đến sự chấm dứt khổ đau, sự không biết về quá khứ, sự không "
             "biết về tương lai, sự không biết về quá khứ và tương lai, sự không biết về quy luật tùy thuộc vào điều "
             "kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện")     # moho (pi-1 ^1-1067)
TRUTHS_S = "Sự không biết về khổ đau… then cài vô minh, sự si mê, tức gốc rễ bất thiện"   # Dukkhe aññāṇaṃ…pe…
VIEWS10 = pi1("“Thế gian là trường tồn”, hoặc “Thế gian không trường tồn”, hoặc “Thế gian là hữu hạn”, hoặc “Thế "
              "gian là vô hạn”, hoặc “Linh hồn và thân thể là một”, hoặc “Linh hồn là khác, thân thể là khác”, hoặc "
              "“Như Lai còn tồn tại sau khi chết”, hoặc “Như Lai không còn tồn tại sau khi chết”, hoặc “Như Lai vừa "
              "còn tồn tại vừa không còn tồn tại sau khi chết”, hoặc “Như Lai không phải còn tồn tại cũng không phải "
              "không còn tồn tại sau khi chết”")
NIHIL = pi1("“Không có sự bố thí, không có sự cúng tế, không có sự cúng dường, không có quả và kết quả của các nghiệp "
            "làm tốt và làm xấu, không có thế gian này, không có thế gian khác, không có mẹ, không có cha, không có "
            "chúng sinh hóa sinh, không có các sa-môn và bà-la-môn trong thế gian đã đi đúng đắn")
NIHIL_END = pi1("thực hành đúng đắn, những người đã tự mình hiểu biết trực tiếp, chứng nghiệm thế gian này và thế "
                "gian khác rồi tuyên bố”")
NIHIL_S = ("“Không có sự bố thí, không có sự cúng tế… những người đã tự mình hiểu biết trực tiếp, chứng nghiệm thế "
           "gian này và thế gian khác rồi tuyên bố”")                      # Natthi dinnaṃ, natthi yiṭṭhaṃ…pe…
SAKKAYA_A = pi1("Ở đời này, người phàm phu không được học hỏi, không thấy các bậc thánh, không thông thạo Giáo Pháp "
                "cao quý, không được rèn luyện trong Giáo Pháp cao quý, không thấy những người chân chính, không thông "
                "thạo Giáo Pháp của những người chân chính, không được rèn luyện trong Giáo Pháp của những người chân "
                "chính")
SAKKAYA_B = pi1("xem vật chất là tự ngã, hoặc tự ngã có vật chất, hoặc vật chất ở trong tự ngã, hoặc tự ngã ở trong "
                "vật chất. Xem cảm giác… tri giác… các sự tạo tác… thức là tự ngã, hoặc tự ngã có thức, hoặc thức ở "
                "trong tự ngã, hoặc tự ngã ở trong thức")
SAKKAYA = f"{SAKKAYA_A} – {SAKKAYA_B}. {cap(DITTHI_S)}"                    # pi-2 has a dash before rūpaṃ attato
SILABBATA = pi1("Các sa-môn và bà-la-môn bên ngoài Giáo Pháp này cho rằng “Trong sạch nhờ giới hạnh, trong sạch nhờ "
                "nghi thức, trong sạch nhờ giới hạnh và nghi thức”")
VICIKICCHA_A = pi1("Nghi ngờ và hoài nghi về Bậc Đạo Sư, nghi ngờ và hoài nghi về Giáo Pháp, nghi ngờ và hoài nghi "
                   "về Tăng đoàn, nghi ngờ và hoài nghi về sự tu học, nghi ngờ và hoài nghi về quá khứ, nghi ngờ và "
                   "hoài nghi về tương lai, nghi ngờ và hoài nghi về quá khứ và tương lai, nghi ngờ và hoài nghi về "
                   "quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện")
VICIKICCHA_B = pi2("Điều mà là sự nghi ngờ, sự khởi nghi ngờ, trạng thái khởi nghi ngờ, trạng thái cứng đờ của tâm, "
                   "sự giằng xé của ý")[len("Điều mà là "):]                # ch. 12
AHIRIKA = pi1("Điều mà là sự không hổ thẹn trước điều đáng hổ thẹn, sự không hổ thẹn nếu để các hiện tượng xấu ác "
              "bất thiện xảy ra nơi mình")
ANOTTAPPA = pi1("Điều mà là sự không ghê sợ trước điều đáng ghê sợ, sự không ghê sợ nếu để các hiện tượng xấu ác bất "
                "thiện xảy ra nơi mình")
DOVACASSA = pi1("Khi được nhắc nhở đúng theo Giáo Pháp mà có sự khó bảo, tính khó bảo, sự khó dạy bảo, sự tiếp nhận "
                "ngang trái, sự thích thú việc làm trái, sự thiếu tôn trọng, thái độ thiếu tôn trọng, sự thiếu kính "
                "trọng, sự không vâng lời")
PAPAMITTA_A = pi1("Có những người không có niềm tin, phạm giới, ít học hỏi, keo kiệt, kém trí tuệ; điều mà là sự "
                  "giao du với họ, sự thường xuyên giao du, sự giao du mật thiết")
PAPAMITTA_B = pi1("sự gần gũi, sự gần gũi mật thiết, sự gắn bó, sự gắn bó mật thiết, sự nghiêng về phía họ")
MUTTHASSACCA = pi1("Điều mà là sự không tỉnh thức, sự không nhớ lại, sự không hồi tưởng, sự không tỉnh thức, sự không "
                   "ghi nhớ, sự không gìn giữ trong trí nhớ, sự hời hợt, sự quên lãng")
ASAMPAJANNA = pi1("Điều mà là sự không biết, sự không thấy… then cài vô minh, sự si mê, tức gốc rễ bất thiện")
VITIKKAMA = pi1("sự vi phạm bằng thân, sự vi phạm bằng lời nói, sự vi phạm bằng thân và lời nói")
ISSA = pi1("Điều mà, trước lợi lộc, sự tôn vinh, sự kính trọng, sự quý trọng, sự đảnh lễ và sự cúng dường mà người "
           "khác nhận được, là sự ganh tị, sự khởi ganh tị, trạng thái khởi ganh tị, sự đố kỵ, sự khởi đố kỵ, trạng "
           "thái khởi đố kỵ")
MACCH5 = pi1("Năm loại keo kiệt – keo kiệt về chỗ ở, keo kiệt về gia đình, keo kiệt về lợi lộc, keo kiệt về lời "
              "khen, keo kiệt về Giáo Pháp")
MACCH_LIST = pi1("Điều mà thuộc loại như vậy là sự keo kiệt, sự khởi keo kiệt, trạng thái khởi keo kiệt, sự bủn xỉn, "
                 "sự hà tiện, sự bo bo, trạng thái khép chặt")
THINA = pi2("Điều mà là sự không khỏe khoắn của tâm, sự không dễ vận dụng, sự chùng xuống, sự chùng xuống hoàn toàn, "
            "sự co rút, sự khởi co rút, trạng thái khởi co rút, sự uể oải, sự khởi uể oải, trạng thái khởi uể oải")
UDDHACCA = pi2("Điều mà là sự xao động của tâm, sự không lắng xuống, sự tán loạn của tâm, trạng thái rối loạn của "
               "tâm")
KODHA14 = pi1("sự giận dữ, sự khởi giận, trạng thái khởi giận, sự sân hận, sự khởi sân, trạng thái khởi sân, sự thù "
              "hằn, sự khởi thù hằn, trạng thái khởi thù hằn, sự chống đối, sự đối nghịch, sự hung dữ, sự nói năng "
              "cộc cằn, sự không hài lòng của tâm")                      # kodho kujjhanā … anattamanatā cittassa
DOSA_LIST = pi1("sự oán giận của tâm, sự phẫn uất, sự ác cảm, sự đối nghịch, sự nổi nóng, sự nổi nóng dữ dội, sự nổi "
                "nóng tột độ, sự sân hận, sự sân hận dữ dội, sự sân hận tột độ, sự thù hằn của tâm, sự sân hận dữ dội "
                "của ý, ") + KODHA14
ARATI = ("sự không hoan hỷ, trạng thái không hoan hỷ, sự không thích thú, sự không ưa thích, sự chán chường, sự bồn "
         "chồn")


def lobha():
    """the greed list of ^2-909 (Ka): the pi-1 Vietnamese (^1-1236, same list) adapted where the pi-2 Pāli differs"""
    v = body(VI(1, "4-02-nikkhepakandam.md", "Tattha katamo lobho?"))
    reps = [  # (pi-1 Vietnamese, pi-2 Vietnamese, why)
        ("sợi chỉ,", "dòng nước,", "sotaṃ (pi-1 suttaṃ «sợi chỉ»; termbase Sotaṃ 'stream, a synonym of craving')"),
        ("sự lan tràn,", f"sự lan tràn [khác chính tả (Sī., Ka.): visadā; xem {DHS} 1141],", "variant"),
        ("kẻ thúc đẩy,", "kẻ thúc đẩy [khác chính tả (Ka.): āyūhinī],", "variant"),
        ("sự thân thiết,", "sự thân thiết [khác chính tả (Ka.): sandhavo],", "variant"),
        ("trạng thái trông mong,", "trạng thái trông mong [khác chính tả (Sī., Syā.): āsiṃsanā āsiṃsitattaṃ],",
         "variant"),
        ("sự thèm thuồng, sự thèm thuồng mãnh liệt, sự thèm thuồng tột độ, sự thèm thuồng, sự khởi thèm thuồng,",
         "sự thèm thuồng, sự thèm thuồng tột độ, sự khởi thèm thuồng,", "jappā abhijappā jappanā (pi-1 has six)"),
        ("khao khát hình sắc, khao khát âm thanh, khao khát mùi,", "khao khát âm thanh, khao khát hình sắc, khao khát mùi,",
         "order saddataṃhā rūpataṇhā as written"),
    ]
    for a, b, _ in reps:
        assert v.count(a) == 1, a
        v = v.replace(a, b)
    return v


slip("^2-909 (Ka) the greed list reads «… nirodhataṇhā saddataṇhā rūpataṇhā gandhataṇhā …» (pi-1 ^1-1065: rūpataṇhā "
     "saddataṇhā): order kept as written («khao khát âm thanh, khao khát hình sắc»)")

# the 27 grounds of intoxication: Pāli accusative (X paṭicca) -> Vietnamese; matrix name «sự say sưa vì …»
MADA_GROUNDS = [  # (matrix compound, accusative in ^2-844, Vietnamese after «dựa vào», Vietnamese in the matrix name)
    ("jāti", "Jātiṃ", "xuất thân", "xuất thân"),
    ("gotta", "Gottaṃ", "dòng họ", "dòng họ"),
    ("ārogya", "ārogyaṃ", "sức khỏe", "sức khỏe"),
    ("yobbana", "yobbanaṃ", "tuổi trẻ", "tuổi trẻ"),
    ("jīvita", "jīvitaṃ", "sự sống", "sự sống"),
    ("lābha", "lābhaṃ", "lợi lộc", "lợi lộc"),
    ("sakkāra", "sakkāraṃ", "sự tôn vinh", "sự tôn vinh"),
    ("garukāra", "garukāraṃ", "sự kính trọng", "sự kính trọng"),
    ("purekkhāra", "purekkhāraṃ", "sự được đề cao", "sự được đề cao"),
    ("parivāra", "parivāraṃ", "đoàn tùy tùng", "đoàn tùy tùng"),
    ("bhoga", "bhogaṃ", "của cải", "tài sản"),
    ("vaṇṇa", "vaṇṇaṃ", "sắc đẹp", "vẻ đẹp"),
    ("suta", "sutaṃ", "sự học hỏi", "sự học hỏi"),
    ("paṭibhāna", "paṭibhānaṃ", "tài ứng đáp", "tài ứng đáp"),
    ("rattaññu", "rattaññutaṃ", "thâm niên", "thâm niên"),
    ("piṇḍapātika", "piṇḍapātikattaṃ", "hạnh khất thực", "hạnh khất thực"),
    ("anavaññāta", "anavaññātaṃ", "việc không bị xem nhẹ", "việc không bị xem nhẹ"),
    ("iriyāpatha", "iriyāpathaṃ", "tư thế", "tư thế"),
    ("iddhi", "iddhiṃ", "thần thông", "thần thông"),
    ("yasa", "yasaṃ", "danh tiếng", "danh tiếng"),
    ("sīla", "sīlaṃ", "giới hạnh", "giới hạnh"),
    ("jhāna", "jhānaṃ", "tầng thiền", "tầng thiền"),
    ("sippa", "sippaṃ", "nghề thủ công", "nghề thủ công"),
    ("āroha", "ārohaṃ", "chiều cao", "chiều cao"),
    ("pariṇāha", "pariṇāhaṃ", "vóc người to lớn", "vóc người to lớn"),
    ("saṇṭhāna", "saṇṭhānaṃ", "hình dáng", "hình dáng"),
    ("pāripūri", "pāripūriṃ", "sự hoàn hảo", "sự hoàn hảo"),
]
misfit("purekkhāraṃ / purekkhāramado and parivāraṃ / parivāramado (^2-832, ^2-844): no termbase entry; «sự được đề "
       "cao» (after the siblings sakkāra «sự tôn vinh», garukāra «sự kính trọng») and «đoàn tùy tùng»")
misfit("vaṇṇamado (^2-832) vs vaṇṇaṃ paṭicca (^2-844): the termbase gives two entries, compound member vaṇṇa «vẻ đẹp» "
       "(«sự say sưa vì vẻ đẹp») and the accusative vaṇṇaṃ «sắc đẹp» («dựa vào sắc đẹp»); both followed")
misfit("lābhaṃ / lābhamado (^2-832, ^2-844): no entry for the ground; «lợi lộc» from the phrases lābhaṃ nijigīsanatā and "
       "Lābhasakkārasiloka- (lābho «sự đạt được» is the event, used in ^2-963)")


def mada_name(i):
    return f"sự say sưa vì {MADA_GROUNDS[i][3]}"


# the onefold matrix: the 73 names (in order); 1-27 the grounds of intoxication
ONE = [mada_name(i) for i in range(27)] + [
    "sự say sưa", "sự buông thả", "sự cứng đầu", "sự tranh hơn", "sự tham muốn quá độ", "sự có nhiều tham muốn",
    "sự có ước muốn xấu xa", "sự kiểu cách", "sự khó tính", "sự phù phiếm", "lối cư xử không thích đáng",
    "sự không hoan hỷ", "sự lười nhác", "sự vươn vai", "sự ngầy ngật sau bữa ăn", "sự co rút của tâm", "sự lừa gạt",
    "sự nói ngọt", "sự ra dấu gợi ý", "sự chèn ép", "sự dùng lợi lộc để tìm kiếm lợi lộc",
    "sự kiêu mạn “Tôi hơn người”", "sự kiêu mạn “Tôi bằng người”", "sự kiêu mạn “Tôi kém người”",
    "sự kiêu mạn “Tôi hơn người” của người vốn hơn người", "sự kiêu mạn “Tôi bằng người” của người vốn hơn người",
    "sự kiêu mạn “Tôi kém người” của người vốn hơn người", "sự kiêu mạn “Tôi hơn người” của người vốn bằng người",
    "sự kiêu mạn “Tôi bằng người” của người vốn bằng người", "sự kiêu mạn “Tôi kém người” của người vốn bằng người",
    "sự kiêu mạn “Tôi hơn người” của người vốn kém người", "sự kiêu mạn “Tôi bằng người” của người vốn kém người",
    "sự kiêu mạn “Tôi kém người” của người vốn kém người", "sự kiêu mạn", "sự ngạo mạn", "sự kiêu mạn chồng chất",
    "sự tự ti", "sự tự đánh giá quá cao", "sự kiêu mạn “Tôi là”", "sự kiêu mạn sai lầm",
    "sự hướng tâm đến người thân", "sự hướng tâm đến xứ sở", "sự hướng tâm đến sự bất tử",
    "sự hướng tâm liên quan đến sự quan tâm đến người khác",
    "sự hướng tâm liên quan đến lợi lộc, sự tôn vinh và tiếng tăm",
    "sự hướng tâm liên quan đến việc không bị xem nhẹ"]
assert len(ONE) == 73
pi1("sự kiêu mạn “Tôi hơn người”")
misfit("asabhāgavutti (^2-832, ^2-855): members Asabhāga «không thích đáng» + vutti «lối cư xử»")
misfit("bhoga in bhogamado (^2-832) «tài sản» (compound member) vs bhogaṃ paṭicca (^2-844) «của cải»: both entries "
       "followed, as for vaṇṇa")
misfit("bhattasammado (^2-832, ^2-859): member sammado «sự ngầy ngật» (not mada «sự say sưa»): «sự ngầy ngật sau bữa "
       "ăn»; "
       "bhattamucchā «sự lịm người vì bữa ăn» (mucchā compound final), bhattakilamatho «sự mệt mỏi vì bữa ăn», "
       "bhattapariḷāho «sự nóng bỏng vì bữa ăn» (pi-1 kāmapariḷāho «sự nóng bỏng vì dục lạc»), kāyaduṭṭhullaṃ «sự nặng "
       "nề của thân»")
misfit("seyyohamasmīti / seyyassa (^2-832, ^2-866 …): no entry; «Tôi hơn người» (pi-1 ^1-1239) and «của người vốn hơn "
       "người» after the entries Sadisassa / Hīnassa")
misfit("ñāti- / janapada- / amaravitakko (^2-832, ^2-885 …): vitakko «sự hướng tâm» + «đến người thân / xứ sở / sự "
       "bất tử» as Kāmavitakko «sự hướng tâm đến dục lạc»")

# the conceit grounds: jātiyā vā gottena vā … aññataraññatarena vatthunā
GROUNDS12 = ("xuất thân, hoặc dòng họ, hoặc gia thế, hoặc vẻ đẹp dung mạo, hoặc tài sản, hoặc việc học tập kinh sách, "
             "hoặc ngành nghề, hoặc ngành thủ công, hoặc lĩnh vực học thuật{v}, hoặc sự học hỏi, hoặc tài ứng đáp, "
             "hoặc một điều nào đó, thứ này hay thứ khác")
GROUNDS_S = "xuất thân, hoặc dòng họ, hoặc gia thế… hoặc một điều nào đó, thứ này hay thứ khác"   # …pe… form


def grounds(v=""):
    return GROUNDS12.format(v=v)


SEYYA = {"seyya": ("hơn người", "hơn người khác"), "sadisa": ("bằng người", "bằng người khác"),
         "hīna": ("kém người", "thấp kém hơn người khác")}


def mana_name(who, thought):
    """seyyassa sadisohamasmīti māno -> «sự kiêu mạn “Tôi bằng người” của người vốn hơn người»"""
    return f"sự kiêu mạn “Tôi {SEYYA[thought][0]}” của người vốn {SEYYA[who][0]}"


# pamādo / kosajjaṃ: Kāyaduccarite vā … ananuyogo pamādo
LAX = ("Sự buông lơi của tâm, sự tiếp tục để mặc buông lơi, trong hành vi xấu bằng thân, hoặc trong hành vi xấu bằng lời "
       "nói, hoặc trong hành vi xấu bằng ý, hoặc trong năm đối tượng của dục lạc; {o}trong việc tu tập các hiện tượng "
       "thiện, sự làm không chu đáo, sự làm không liên tục, sự làm có ngừng nghỉ, sự hành xử chùng xuống, sự buông bỏ "
       "ý muốn, sự buông bỏ gánh nặng, sự không thực hành, sự không tu tập, sự không làm đi làm lại, sự không quyết "
       "tâm, sự không chuyên cần, sự buông thả")


def lax(va=False):
    return LAX.format(o="hoặc " if va else "")


PAMADA_END = "điều mà thuộc loại như vậy là sự buông thả, sự khởi buông thả, trạng thái khởi buông thả"
misfit("vossaggānuppadānaṃ (^2-846 …): «sự tiếp tục để mặc buông lơi» (member ānuppadānaṃ «sự tiếp tục để mặc», "
       "vossaggo «sự buông lơi», user)")
misfit("olīnavuttitā / nikkhittachandatā / nikkhittadhuratā (^2-846 …): no whole-word entries; «sự hành xử chùng "
       "xuống» (olīyanā «sự chùng xuống»), «sự buông bỏ ý muốn» (chanda «ý muốn»), «sự buông bỏ gánh nặng» (member "
       "dhuratā «gánh»)")

# atricchatā / mahicchatā / asantuṭṭhitā
WANT_MORE = ("Sự mong muốn nhiều hơn nữa của người không biết đủ với y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật "
             "dụng chữa bệnh, thế này hay thế khác, hoặc với năm đối tượng của dục lạc; điều mà thuộc loại như vậy là sự mong "
             "muốn, trạng thái bị mong muốn chi phối, {x}, " + RAGA3)
# kuhanā … nippesikatā: Lābhasakkārasilokasannissitassa pāpicchassa icchāpakatassa
LSS = "người bám vào lợi lộc, sự tôn vinh và tiếng tăm, có ước muốn xấu xa, bị ước muốn chi phối"

# requisites, misconduct, views (pi-2 earlier chapters)
KILL = pi2("việc sát hại sinh mạng")
STEAL = pi2("việc lấy của không được cho")
SEX = pi2("hành vi sai trái trong các dục lạc")
LIE = "việc nói dối"
SPEECH4 = "việc nói dối, lời nói chia rẽ, lời nói thô ác, việc nói lời phù phiếm"
MIND3 = "sự thèm muốn, ác ý, quan điểm sai lầm"
DRINK = pi2("việc dùng rượu nấu rượu men và chất gây say dẫn đến sự buông thả")
WRONG8 = ("quan điểm sai lầm, tư duy sai lầm, lời nói sai lầm, hành động sai lầm, sinh kế sai lầm, nỗ lực sai lầm, "
          "tỉnh thức sai lầm, định tâm sai lầm")                              # ch. 11 «… đúng đắn» -> «… sai lầm»
pi2("sinh kế đúng đắn")
FETTER10 = pi1("xiềng xích tham đắm dục lạc, xiềng xích ác cảm, xiềng xích kiêu mạn, xiềng xích quan điểm, xiềng xích "
               "hoài nghi, xiềng xích hiểu sai lệch về giới hạnh và nghi thức, xiềng xích tham đắm hiện hữu, xiềng xích "
               "ganh tị, xiềng xích keo kiệt, xiềng xích vô minh")
ANUSAYA7 = pi2("khuynh hướng tiềm ẩn tham đắm dục lạc, khuynh hướng tiềm ẩn ác cảm, khuynh hướng tiềm ẩn kiêu mạn, "
               "khuynh hướng tiềm ẩn quan điểm, khuynh hướng tiềm ẩn hoài nghi, khuynh hướng tiềm ẩn tham đắm sự hiện "
               "hữu, khuynh hướng tiềm ẩn vô minh")                         # ch. 16 ^2-816
KILESA10 = pi2("sự tham lam, sự sân hận, sự si mê, sự kiêu mạn, quan điểm, sự hoài nghi, sự uể oải, sự xao động, sự "
               "không biết hổ thẹn, sự không biết ghê sợ tội lỗi")          # ch. 16 ^2-819
KILESA8 = "sự tham lam, sự sân hận, sự si mê, sự kiêu mạn, quan điểm, sự hoài nghi, sự uể oải, sự xao động"
NIVARANA5 = pi1("chướng ngại ý muốn dục lạc, chướng ngại ác ý, chướng ngại uể oải và đờ đẫn, chướng ngại xao động và "
                "hối tiếc, chướng ngại hoài nghi")
JOY4 = pi1("sự khoan khoái trong tâm, sự dễ chịu trong tâm")                # pi-1 ^1-10
JOY4B = pi1("cảm nhận khoan khoái và dễ chịu sinh từ sự tiếp xúc của tâm, cảm giác khoan khoái và dễ chịu sinh từ sự "
            "tiếp xúc của tâm")
GRIEF4 = "sự bứt rứt trong tâm, sự khó chịu trong tâm"                     # pi-1 ^1-416 pattern
GRIEF4B = ("cảm nhận bứt rứt và khó chịu sinh từ sự tiếp xúc của tâm, cảm giác bứt rứt và khó chịu sinh từ sự tiếp "
           "xúc của tâm")
NEUTRAL3 = pi1("trạng thái trong tâm không khoan khoái cũng không bứt rứt")    # pi-1 ^1-153
NEUTRAL3B = pi1("cảm nhận không khó chịu cũng không dễ chịu sinh từ sự tiếp xúc của tâm, cảm giác không khó chịu cũng "
                "không dễ chịu sinh từ sự tiếp xúc của tâm")
pi1("sự bứt rứt trong tâm")
SENSES6 = [("hình sắc", "rūpesu"), ("âm thanh", "saddesu"), ("mùi", "gandhesu"), ("vị", "rasesu"),
           ("vật xúc chạm", "phoṭṭhabbesu"), ("đối tượng của ý", "dhammesu")]
SEE6 = [("thấy hình sắc bằng mắt", "hình sắc"), ("nghe âm thanh bằng tai", "âm thanh"), ("ngửi mùi bằng mũi", "mùi"),
        ("nếm vị bằng lưỡi", "vị"), ("chạm vật xúc chạm bằng thân", "vật xúc chạm"),
        ("nhận biết đối tượng của ý bằng ý", "đối tượng của ý")]
pi1("khi nhận biết đối tượng của ý bằng ý")
SAMANA = "Ở đời này, có sa-môn hoặc bà-la-môn có học thuyết như vầy, có quan điểm như vầy"   # samaṇo vā brāhmaṇo vā …
ANOTHER = "Người khác nói với người ấy như vầy"                                             # tamañño evamāha
TRUE_FIRM = "như là sự thật, như là điều chắc chắn"                                         # saccato thetato

# =========================================================================== topic names (lower case)
N = {
    # twos
    "kodho": "sự giận dữ", "upanāho": "sự ôm hận", "makkho": "sự gièm pha", "paḷāso": "sự ganh đua",
    "issā": "sự ganh tị", "macchariyaṃ": "sự keo kiệt", "māyā": "sự xảo trá", "sāṭheyyaṃ": "sự gian xảo",
    "avijjā": "vô minh", "bhavataṇhā": "khao khát được hiện hữu", "bhavadiṭṭhi": "quan điểm về sự hiện hữu",
    "vibhavadiṭṭhi": "quan điểm về sự không còn hiện hữu", "sassatadiṭṭhi": "quan điểm về sự trường tồn",
    "ucchedadiṭṭhi": "quan điểm về sự đoạn diệt", "antavādiṭṭhi": "quan điểm về sự hữu hạn",
    "anantavādiṭṭhi": "quan điểm về sự vô hạn", "pubbantānudiṭṭhi": "quan điểm về quá khứ",
    "aparantānudiṭṭhi": "quan điểm về tương lai", "ahirikaṃ": "sự không biết hổ thẹn",
    "anottappaṃ": "sự không biết ghê sợ tội lỗi", "dovacassatā": "sự khó dạy bảo",
    "pāpamittatā": "sự kết bạn với người xấu", "anajjavo": "sự không ngay thật", "amaddavo": "sự không mềm mỏng",
    "akkhanti": "sự không nhẫn nại", "asoraccaṃ": "sự không hiền hòa", "asākhalyaṃ": "sự không hòa nhã",
    "appaṭisanthāro": "sự không niềm nở tiếp đón",
    "indriyesu aguttadvāratā": "sự không phòng hộ cửa các giác quan",
    "bhojane amattaññutā": "sự không biết tiết độ trong ăn uống", "muṭṭhassaccaṃ": "sự mất tỉnh thức",
    "asampajaññaṃ": "sự thiếu hiểu biết rõ ràng", "sīlavipatti": "sự suy đồi về giới hạnh",
    "diṭṭhivipatti": "sự suy đồi về quan điểm", "ajjhattasaṃyojanaṃ": "xiềng xích ở nơi bản thân",
    "bahiddhāsaṃyojanaṃ": "xiềng xích ở bên ngoài bản thân",
    # threes (members)
    "assādadiṭṭhi": "quan điểm về sự thỏa thích", "attānudiṭṭhi": "quan điểm xem có tự ngã",
    "micchādiṭṭhi": "quan điểm sai lầm", "arati": "sự không hoan hỷ", "vihesā": "sự gây phiền nhiễu",
    "adhammacariyā": "hành vi phi pháp", "nānattasaññā": "tri giác về sự đa dạng", "uddhaccaṃ": "sự xao động",
    "kosajjaṃ": "sự lười biếng", "pamādo": "sự buông thả", "asantuṭṭhitā": "sự không biết đủ",
    "asampajaññatā": "sự thiếu hiểu biết rõ ràng", "mahicchatā": "sự có nhiều tham muốn",
    "anādariyaṃ": "sự thiếu tôn trọng", "assaddhiyaṃ": "sự thiếu niềm tin", "avadaññutā": "sự không rộng lượng",
    "asaṃvaro": "sự không thu thúc", "dussīlyaṃ": "sự phạm giới",
    "ariyānaṃ adassanakamyatā": "sự không mong muốn thấy các bậc thánh",
    "saddhammaṃ asotukamyatā": "sự không muốn nghe Giáo Pháp chân chính",
    "upārambhacittatā": "sự có tâm hay bắt lỗi", "cetaso vikkhepo": "sự tán loạn của tâm",
    "ayoniso manasikāro": "sự chú tâm không khôn ngoan", "kummaggasevanā": "sự đi theo con đường lệch lạc",
    "cetaso ca līnattaṃ": "sự co rút của tâm",
    # fours (members)
    "kāmāsavo": "ô nhiễm dục lạc", "bhavāsavo": "ô nhiễm hiện hữu", "diṭṭhāsavo": "ô nhiễm quan điểm",
    "avijjāsavo": "ô nhiễm vô minh", "kāmupādānaṃ": "sự bám víu vào dục lạc",
    "diṭṭhupādānaṃ": "sự bám víu vào quan điểm", "sīlabbatupādānaṃ": "sự bám víu vào giới hạnh và nghi thức",
    "attavādupādānaṃ": "sự bám víu vào học thuyết về tự ngã",
}
misfit("adassanakamyatā / asametukamyatā (^2-834, ^2-934): no entries; «sự không mong muốn thấy / đến gần» with "
       "kamyatā «sự mong muốn» (user); the compounds that have entries keep them although they say «muốn»: "
       "adaṭṭhukamyatā «sự không muốn nhìn», asamāgantukamyatā, asotukamyatā «sự không muốn nghe» and the others of "
       "^2-U26 (the adherence check flags kamyatā there)")
misfit("pubbantānudiṭṭhi / aparantānudiṭṭhi (^2-833, ^2-899): no entries; «quan điểm về quá khứ / tương lai» (pi-1 "
       "pubbante «quá khứ», aparante «tương lai»)")
misfit("ajjhatta- / bahiddhāsaṃyojanaṃ (^2-833, ^2-908): no phrase entry; «xiềng xích ở nơi bản thân / ở bên ngoài "
       "bản thân» (ajjhatta, bahiddhā as pi-1 / the sample)")

# counted topics: Pāli heading (after the number) -> Vietnamese (lower case)
T = {
    "Tīṇi akusalamūlāni": "ba gốc rễ bất thiện", "Tayo akusalavitakkā": "ba sự hướng tâm bất thiện",
    "Tisso akusalasaññā": "ba tri giác bất thiện", "Tisso akusaladhātuyo": "ba yếu tố bất thiện",
    "Tīṇi duccaritāni": "ba hành vi xấu", "Tayo āsavā": "ba ô nhiễm", "Tīṇi saṃyojanāni": "ba xiềng xích",
    "Tisso taṇhā": "ba loại khao khát", "Aparāpi tisso taṇhā": "ba loại khao khát khác",
    "Tisso esanā": "ba sự tìm cầu", "Tisso vidhā": "ba sự so sánh", "Tīṇi bhayāni": "ba nỗi sợ hãi",
    "Tīṇi tamāni": "ba sự tăm tối", "Tīṇi titthāyatanāni": "ba lĩnh vực của các học thuyết ngoại đạo",
    "Tayo kiñcanā": "ba sự vướng bận", "Tīṇi aṅgaṇāni": "ba vết nhơ", "Tīṇi malāni": "ba sự dơ bẩn",
    "Tīṇi visamāni": "ba sự lệch lạc", "Aparānipi tīṇi visamāni": "ba sự lệch lạc khác", "Tayo aggī": "ba ngọn lửa",
    "Tayo kasāvā": "ba chất cặn bẩn", "Aparepi tayo kasāvā": "ba chất cặn bẩn khác",
    "Cattāro āsavā": "bốn ô nhiễm", "Cattāro ganthādī": "bốn nút thắt và những điều tương tự",
    "Cattāro taṇhuppādā": "bốn nguyên nhân khởi lên khao khát",
    "Cattāri agatigamanāni": "bốn sự đi theo con đường sai trái", "Cattāro vipariyāsā": "bốn sự đảo ngược",
    "Cattāro anariyavohārā": "bốn cách nói không cao quý",
    "Aparepi cattāro anariyavohārā": "bốn cách nói không cao quý khác", "Cattāri duccaritāni": "bốn hành vi xấu",
    "Aparānipi cattāri duccaritāni": "bốn hành vi xấu khác", "Cattāri bhayāni": "bốn nỗi sợ hãi",
    "Aparānipi cattāri bhayāni": "bốn nỗi sợ hãi khác", "Catasso diṭṭhiyo": "bốn quan điểm",
    "Pañcorambhāgiyāni saṃyojanāni": "năm xiềng xích thuộc phần thấp",
    "Pañcuddhambhāgiyāni saṃyojanāni": "năm xiềng xích thuộc phần cao", "Pañca macchariyāni": "năm loại keo kiệt",
    "Pañca saṅgā": "năm sự dính mắc", "Pañca sallā": "năm mũi tên", "Pañca cetokhilā": "năm sự chai cứng của tâm",
    "Pañca cetaso vinibandhā": "năm sự trói buộc của tâm", "Pañca nīvaraṇāni": "năm chướng ngại",
    "Pañca kammāni ānantarikāni": "năm nghiệp có quả không gián đoạn", "Pañca diṭṭhiyo": "năm quan điểm",
    "Pañca verā": "năm điều gây thù địch", "Pañca byasanā": "năm sự tổn hại",
    "Pañca akkhantiyā ādīnavā": "năm điều nguy hại của sự không nhẫn nại", "Pañca bhayāni": "năm nỗi sợ hãi",
    "Pañca diṭṭhadhammanibbānavādā": "năm học thuyết về Niết-bàn ngay trong đời này",
    "Cha vivādamūlāni": "sáu gốc rễ của tranh cãi", "Cha chandarāgā": "sáu sự tham đắm do ý muốn",
    "Cha virodhavatthūni": "sáu chỗ dựa của sự chống đối", "Cha taṇhākāyā": "sáu nhóm khao khát",
    "Cha agāravā": "sáu sự thiếu kính trọng", "Cha parihāniyā dhammā": "sáu hiện tượng dẫn đến suy thoái",
    "Aparepi cha parihāniyā dhammā": "sáu hiện tượng dẫn đến suy thoái khác",
    "Cha somanassupavicārā": "sáu sự lưu tâm gắn với niềm vui",
    "Cha domanassupavicārā": "sáu sự lưu tâm gắn với nỗi buồn",
    "Cha upekkhupavicārā": "sáu sự lưu tâm gắn với sự bình thản",
    "Cha gehasitāni somanassāni": "sáu niềm vui gắn với đời sống thế tục",
    "Cha gehasitāni domanassāni": "sáu nỗi buồn gắn với đời sống thế tục",
    "Cha gehasitā upekkhā": "sáu sự bình thản gắn với đời sống thế tục", "Cha diṭṭhiyo": "sáu quan điểm",
    "Sattānusayā": "bảy khuynh hướng tiềm ẩn", "Satta saṃyojanāni": "bảy xiềng xích",
    "Satta pariyuṭṭhānāni": "bảy sự ám ảnh", "Satta asaddhammā": "bảy điều không chân chính",
    "Satta duccaritāni": "bảy hành vi xấu", "Satta mānā": "bảy loại kiêu mạn", "Satta diṭṭhiyo": "bảy quan điểm",
    "Aṭṭha kilesavatthūni": "tám chỗ dựa của phiền não", "Aṭṭha kusītavatthūni": "tám chỗ dựa của sự lười biếng",
    "Aṭṭhasu lokadhammesu cittassa paṭighāto": "sự va chạm của tâm trước tám hiện tượng thế gian",
    "Aṭṭhaanariyavohārā": "tám cách nói không cao quý", "Aṭṭha micchattā": "tám sự sai lầm",
    "Aṭṭha purisadosā": "tám lỗi của con người", "Aṭṭha asaññīvādā": "tám học thuyết về sự không có tri giác",
    "Aṭṭha nevasaññīnāsaññīvādā": ("tám học thuyết về sự không phải có tri giác cũng không phải không có tri "
                                   "giác"),
    "Nava āghātavatthūni": "chín chỗ dựa của sự oán giận", "Nava purisamalāni": "chín sự dơ bẩn của con người",
    "Navavidhā mānā": "chín loại kiêu mạn", "Nava taṇhāmūlakā dhammā": "chín hiện tượng bắt nguồn từ khao khát",
    "Nava iñjitāni": "chín sự dao động", "Nava maññitādīni": "chín sự tưởng tượng và những điều tương tự",
    "Dasa kilesavatthūni": pi2("mười chỗ dựa của phiền não"), "Dasa āghātavatthūni": "mười chỗ dựa của sự oán giận",
    "Dasa akusalakammapathā": "mười con đường nghiệp bất thiện", "Dasa saṃyojanāni": "mười xiềng xích",
    "Dasa micchattā": "mười sự sai lầm", "Dasavatthukā micchādiṭṭhi": "quan điểm sai lầm có mười chủ đề",
    "Dasavatthukā antaggāhikā diṭṭhi": "quan điểm chấp giữ cực đoan có mười chủ đề",
}
misfit("anariyavohārā (^2-835, ^2-U42 …): «cách nói không cao quý» from the compound entries anariya «không cao quý» "
       "and vohārā «cách nói»")
misfit("orambhāgiya / uddhambhāgiya (^2-836, ^2-940, ^2-U49): no entry; «thuộc phần thấp / thuộc phần cao»")
misfit("cetokhilā (^2-836, ^2-941): no entry; «sự chai cứng của tâm» (khilajāto «trở nên chai cứng»); byasanā «sự tổn "
       "hại» (byasanena «tổn hại»); kammapathā «con đường nghiệp»; taṇhākāyā «nhóm khao khát»; asaññīvādā «học thuyết "
       "về sự không có tri giác» (vāda as attavāda «học thuyết»)")
misfit("somanassaṭṭhāniyaṃ / domanassaṭṭhāniyaṃ (^2-U64, ^2-U65): no entry; «làm khởi lên niềm vui / nỗi buồn» after "
       "upekkhāṭṭhāniyaṃ «làm khởi lên sự bình thản»")

HEAD = {"Khuddakavatthuvibhaṅgo": S.CH_HEADINGS["Khuddakavatthuvibhaṅgo"], "Taṇhāvicaritaniddeso":
        "Giải thích các dòng khao khát", "(1) Ajjhattikassa upādāya": "(1) Dựa vào phần bên trong",
        "(2) Bāhirassa upādāya": "(2) Dựa vào phần bên ngoài"}
BO = {1: "một", 2: "đôi", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười"}
PREF = {1: "Ekaka", 2: "Duka", 3: "Tika", 4: "Catukka", 5: "Pañcaka", 6: "Chakka", 7: "Sattaka", 8: "Aṭṭhaka",
        9: "Navaka", 10: "Dasaka"}
for _n in PREF:
    HEAD[f"{PREF[_n]}mātikā"] = f"Ma trận bộ {BO[_n]}"                       # ch. 16
    HEAD[f"{PREF[_n]}niddeso"] = f"Giải thích phân loại theo nhóm {NUM[_n]}"  # ch. 16
pi2("Ma trận bộ một")
pi1("Giải thích phân loại theo nhóm một")
_ONE_HEADS = ["Jātimado"] + [None] * 26 + [
    "Mado", "Pamādo", "Thambho", "Sārambho", "Atricchatā", "Mahicchatā", "Pāpicchatā", "Siṅgaṃ", "Tintiṇaṃ",
    "Cāpalyaṃ", "Asabhāgavutti", "Arati", "Tandī", "Vijambhitā", "Bhattasammado", "Cetaso ca līnattaṃ", "Kuhanā",
    "Lapanā", "Nemittikatā", "Nippesikatā", "Lābhena lābhaṃ nijigīsanatā", "Seyyohamasmīti māno",
    "Sadisohamasmīti māno", "Hīnohamasmīti māno", "Seyyassa seyyohamasmīti māno", "Seyyassa sadisohamasmīti māno",
    "Seyyassa hīnohamasmīti māno", "Sadisassa seyyohamasmīti māno", "Sadisassa sadisohamasmīti māno",
    "Sadisassa hīnohamasmīti māno", "Hīnassa seyyohamasmīti māno", "Hīnassa sadisohamasmīti māno",
    "Hīnassa hīnohamasmīti māno", "Māno", "Atimāno", "Mānātimāno", "Omāno", "Adhimāno", "Asmimāno", "Micchāmāno",
    "Ñātivitakko", "Janapadavitakko", "Amaravitakko", "Parānuddayatāpaṭisaṃyutto vitakko",
    "Lābhādipaṭisaṃyutto vitakko", "Anavaññattipaṭisaṃyutto vitakko"]
for _i, _p in enumerate(_ONE_HEADS):
    if _p:
        HEAD[f"({_i + 1}) {_p}"] = f"({_i + 1}) {cap(ONE[_i])}"
HEAD["(2-27) Gottamadādī"] = "(2-27) Sự say sưa vì dòng họ và những điều tương tự"           # termbase Gottamadādī
HEAD["(72) Lābhādipaṭisaṃyutto vitakko"] = "(72) Sự hướng tâm liên quan đến lợi lộc và những điều khác"   # ādi
_TWO = [("kodho", "upanāho"), ("makkho", "paḷāso"), ("issā", "macchariyaṃ"), ("māyā", "sāṭheyyaṃ"),
        ("avijjā", "bhavataṇhā"), ("bhavadiṭṭhi", "vibhavadiṭṭhi"), ("sassatadiṭṭhi", "ucchedadiṭṭhi"),
        ("antavādiṭṭhi", "anantavādiṭṭhi"), ("pubbantānudiṭṭhi", "aparantānudiṭṭhi"), ("ahirikaṃ", "anottappaṃ"),
        ("dovacassatā", "pāpamittatā"), ("anajjavo", "amaddavo"), ("akkhanti", "asoraccaṃ"),
        ("asākhalyaṃ", "appaṭisanthāro"), ("indriyesu aguttadvāratā", "bhojane amattaññutā"),
        ("muṭṭhassaccaṃ", "asampajaññaṃ"), ("sīlavipatti", "diṭṭhivipatti"),
        ("ajjhattasaṃyojanaṃ", "bahiddhāsaṃyojanaṃ")]
_TWO_HEADS = ["Kodho ca upanāho ca", "Makkho ca paḷāso ca", "Issā ca macchariyañca", "Māyā ca sāṭheyyañca",
              "Avijjā ca bhavataṇhā ca", "Bhavadiṭṭhi ca vibhavadiṭṭhi ca", "Sassatadiṭṭhi ca ucchedadiṭṭhi ca",
              "Antavādiṭṭhi ca anantavādiṭṭhi ca", "Pubbantānudiṭṭhi ca aparantānudiṭṭhi ca",
              "Ahirikañca anottappañca", "Dovacassatā ca pāpamittatā ca", "Anajjavo ca amaddavo ca",
              "Akkhanti ca asoraccañca", "Asākhalyañca appaṭisanthāro ca",
              "Indriyesu aguttadvāratā ca bhojane amattaññutā ca", "Muṭṭhassaccañca asampajaññañca",
              "Sīlavipatti ca diṭṭhivipatti ca", "Ajjhattasaṃyojanañca bahiddhāsaṃyojanañca"]


def pair(i):
    a, b = _TWO[i]
    return f"{N[a]} và {N[b]}"


for _i, _p in enumerate(_TWO_HEADS):
    HEAD[f"({_i + 1}) {_p}"] = f"({_i + 1}) {cap(pair(_i))}"
_TRI_HEADS = ["Tīṇi akusalamūlāni", "Tayo akusalavitakkā", "Tisso akusalasaññā", "Tisso akusaladhātuyo",
              "Tīṇi duccaritāni", "Tayo āsavā", "Tīṇi saṃyojanāni", "Tisso taṇhā", "Aparāpi tisso taṇhā",
              "Aparāpi tisso taṇhā", "Tisso esanā", "Tisso vidhā", "Tīṇi bhayāni", "Tīṇi tamāni",
              "Tīṇi titthāyatanāni", "Tayo kiñcanā", "Tīṇi aṅgaṇāni", "Tīṇi malāni", "Tīṇi visamāni",
              "Aparānipi tīṇi visamāni", "Tayo aggī", "Tayo kasāvā", "Aparepi tayo kasāvā"]
for _i, _p in enumerate(_TRI_HEADS):
    HEAD[f"({_i + 1}) {_p}"] = f"({_i + 1}) {cap(T[_p])}"
_TRIPLES = [("assādadiṭṭhi", "attānudiṭṭhi", "micchādiṭṭhi"), ("arati", "vihesā", "adhammacariyā"),
            ("dovacassatā", "pāpamittatā", "nānattasaññā"), ("uddhaccaṃ", "kosajjaṃ", "pamādo"),
            ("asantuṭṭhitā", "asampajaññatā", "mahicchatā"), ("ahirikaṃ", "anottappaṃ", "pamādo"),
            ("anādariyaṃ", "dovacassatā", "pāpamittatā"), ("assaddhiyaṃ", "avadaññutā", "kosajjaṃ"),
            ("uddhaccaṃ", "asaṃvaro", "dussīlyaṃ"),
            ("ariyānaṃ adassanakamyatā", "saddhammaṃ asotukamyatā", "upārambhacittatā"),
            ("muṭṭhassaccaṃ", "asampajaññaṃ", "cetaso vikkhepo"),
            ("ayoniso manasikāro", "kummaggasevanā", "cetaso ca līnattaṃ")]
for _i, _tr in enumerate(_TRIPLES):
    HEAD[f"({_i + 24}. Ka) {_tr[0]}"] = f"({_i + 24}. a) {cap(N[_tr[0]])}"
    HEAD[f"(Kha) {_tr[1]}"] = f"(b) {cap(N[_tr[1]])}"
    HEAD[f"(Ga) {_tr[2]}"] = f"(c) {cap(N[_tr[2]])}"
for _k, _a in (("Ka", "kāmāsavo"), ("Kha", "bhavāsavo"), ("Ga", "diṭṭhāsavo"), ("Gha", "avijjāsavo"),
               ("Ka", "kāmupādānaṃ"), ("Kha", "diṭṭhupādānaṃ"), ("Ga", "sīlabbatupādānaṃ"),
               ("Gha", "attavādupādānaṃ")):
    HEAD[f"({_k}) {_a}"] = f"({LABEL[_k]}) {cap(N[_a])}"
_NUMBERED = {  # numbered headings of the fourfold … tenfold expositions: (n) Pāli -> T key
    4: ["Cattāro āsavā", "Cattāro ganthādī", "Cattāro taṇhuppādā", "Cattāri agatigamanāni", "Cattāro vipariyāsā",
        "Cattāro anariyavohārā", "Aparepi cattāro anariyavohārā", "Cattāri duccaritāni",
        "Aparānipi cattāri duccaritāni", "Cattāri bhayāni", "Aparānipi cattāri bhayāni", "Catasso diṭṭhiyo"],
    5: ["Pañcorambhāgiyāni saṃyojanāni", "Pañcuddhambhāgiyāni saṃyojanāni", "Pañca macchariyāni", "Pañca saṅgā",
        "Pañca sallā", "Pañca cetokhilā", "Pañca cetaso vinibandhā", "Pañca nīvaraṇāni",
        "Pañca kammāni ānantarikāni", "Pañca diṭṭhiyo", "Pañca verā", "Pañca byasanā", "Pañca akkhantiyā ādīnavā",
        "Pañca bhayāni", "Pañca diṭṭhadhammanibbānavādā"],
    6: ["Cha vivādamūlāni", "Cha chandarāgā", "Cha virodhavatthūni", "Cha taṇhākāyā", "Cha agāravā",
        "Cha parihāniyā dhammā", "Aparepi cha parihāniyā dhammā", "Cha somanassupavicārā", "Cha domanassupavicārā",
        "Cha upekkhupavicārā", "Cha gehasitāni somanassāni", "Cha gehasitāni domanassāni", "Cha gehasitā upekkhā",
        "Cha diṭṭhiyo"],
    7: ["Sattānusayā", "Satta saṃyojanāni", "Satta pariyuṭṭhānāni", "Satta asaddhammā", "Satta duccaritāni",
        "Satta mānā", "Satta diṭṭhiyo"],
    8: ["Aṭṭha kilesavatthūni", "Aṭṭha kusītavatthūni", "Aṭṭhasu lokadhammesu cittassa paṭighāto",
        "Aṭṭhaanariyavohārā", "Aṭṭha micchattā", "Aṭṭha purisadosā", "Aṭṭha asaññīvādā",
        "Aṭṭha nevasaññīnāsaññīvādā"],
    9: ["Nava āghātavatthūni", "Nava purisamalāni", "Navavidhā mānā", "Nava taṇhāmūlakā dhammā", "Nava iñjitāni",
        "Nava maññitādīni"],
    10: ["Dasa kilesavatthūni", "Dasa āghātavatthūni", "Dasa akusalakammapathā", "Dasa saṃyojanāni",
         "Dasa micchattā", "Dasavatthukā micchādiṭṭhi", "Dasavatthukā antaggāhikā diṭṭhi"],
}
_NUM_LABELS = {4: ["1", "2-5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"],
               9: ["1", "2", "3", "4", "5", "6-9"]}
for _n, _lst in _NUMBERED.items():
    _labs = _NUM_LABELS.get(_n, [str(i + 1) for i in range(len(_lst))])
    for _l, _p in zip(_labs, _lst):
        HEAD[f"({_l}) {_p}"] = f"({_l}) {cap(T[_p])}"

# =========================================================================== the matrix (^2-832 … ^2-842)
SEG = {}


def numbered(items, sep=", "):
    s = sep.join(f"({i + 1}) {x}" for i, x in enumerate(items))
    return s[:4] + cap(s[4:]) + "."


_one = list(ONE)
_one[42] += " [dị bản (Syā.): cetaso līnattaṃ]"
_one[47] += " [khác chính tả (Sī.): nijigiṃsanatā; (Syā.): jigiṃsanatā]"
SEG["2-832"] = [numbered(_one), CLOSE[1]]
_two = [pair(i) for i in range(18)]
_two[1] = f"{N['makkho']} và {N['paḷāso']} [khác chính tả (Sī., Syā.): palāso]"
SEG["2-833"] = [numbered(_two), CLOSE[2]]
_tri = [T[p] for p in _TRI_HEADS] + [", ".join(N[x] for x in tr) for tr in _TRIPLES]
SEG["2-834"] = [numbered(_tri, "; "), CLOSE[3]]
_four = ["bốn ô nhiễm", "bốn nút thắt", "bốn dòng lũ", "bốn ách", "bốn sự bám víu"] + [T[p] for p in _NUMBERED[4][2:]]
_four[7] += " [khác chính tả (Sī., Syā., Ka.): vipariyesā]"
SEG["2-835"] = [numbered(_four), CLOSE[4]]
_five = [T[p] for p in _NUMBERED[5]]
_five[6] += " [khác chính tả (Ka.): cetasovinibaddhā]"
SEG["2-836"] = [numbered(_five), CLOSE[5]]
SEG["2-837"] = [numbered([T[p] for p in _NUMBERED[6]]), CLOSE[6]]
SEG["2-838"] = [numbered([T[p] for p in _NUMBERED[7]]), CLOSE[7]]
SEG["2-839"] = [numbered([T[p] for p in _NUMBERED[8]]), CLOSE[8]]
SEG["2-840"] = [numbered([T[p] for p in _NUMBERED[9][:5]] + ["chín sự tưởng tượng", "chín sự rung động",
                                                              "chín sự suy diễn lan man", "chín điều được tạo tác"]),
                CLOSE[9]]
SEG["2-841"] = [numbered([T[p] for p in _NUMBERED[10]]), CLOSE[10]]
CURRENTS = "dòng khao khát"
SUM36 = "gom tất cả lại làm một, thu tóm lại, thì thành"                 # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā
SEG["2-842"] = [
    f"Mười tám {CURRENTS} dựa vào phần bên trong, mười tám {CURRENTS} dựa vào phần bên ngoài; {SUM36} ba mươi sáu "
    f"{CURRENTS}. Như vậy, ba mươi sáu {CURRENTS} thuộc quá khứ, ba mươi sáu {CURRENTS} thuộc tương lai, ba mươi sáu "
    f"{CURRENTS} thuộc hiện tại; {SUM36} một trăm lẻ tám {CURRENTS}. Và sáu mươi hai sự mắc kẹt trong các quan điểm "
    "đã được Đức Thế Tôn nói đến trong bài giảng “Lưới Phạm Thiên”.",
    "Ma trận."]
misfit("brahmajāle veyyākaraṇe (^2-842, ^2-977): no entry for the name; «bài giảng “Lưới Phạm Thiên”» (veyyākaraṇe "
       "«bài giảng»)")

# =========================================================================== the onefold exposition (^2-843 … ^2-890)


def mada_line(i, start, var=""):
    """X paṭicca mado majjanā … ketukamyatā cittassa – ayaṃ vuccati "Xmado"."""
    return f"{start} mà có {MADA}".replace("sự vênh vang", "sự vênh vang" + var, 1) + f" {called(mada_name(i))}"


SEG["2-843"] = [f"{q(mada_name(0))} " + mada_line(
    0, "Dựa vào xuất thân", f" [khác chính tả (Syā., Ka.): uṇṇati uṇṇāmo; xem {DHS} 1121]")]
_grounds = "… ".join(f"dựa vào {g[2]}" for g in MADA_GROUNDS[1:])
SEG["2-844"] = [f"{q(mada_name(1))} " + mada_line(26, cap(_grounds))]
SEG["2-845"] = [f"{q('sự say sưa')} {WHICH} {MADA} {called('sự say sưa')}"]
SEG["2-846"] = [f"{q(N['pamādo'])} {lax(True)}, {PAMADA_END} {called(N['pamādo'])}"]
SEG["2-847"] = [f"{q('sự cứng đầu')} {WHICH} sự cứng đầu, sự khởi cứng đầu, trạng thái cứng đờ, tính thô cứng, tính "
                f"thô lỗ, sự cao ngạo của tâm, sự không mềm mại {called('sự cứng đầu')}"]
misfit("thambhitattaṃ (^2-847): the termbase senses are «trạng thái căng cứng» (air element) and «trạng thái cứng đờ» "
       "(rigidity of mind); the second is used for the obstinacy list")
SEG["2-848"] = [f"{q('sự tranh hơn')} {WHICH} sự tranh hơn, sự tranh hơn đáp trả, hành động tranh hơn, hành động "
                f"tranh hơn đáp trả, trạng thái tranh hơn đáp trả {called('sự tranh hơn')}"]
SEG["2-849"] = [f"{q('sự tham muốn quá độ')} {WANT_MORE.format(x='sự tham muốn quá độ')} "
                f"{called('sự tham muốn quá độ')}"]
SEG["2-850"] = [f"{q(N['mahicchatā'])} {WANT_MORE.format(x=N['mahicchatā'])} {called(N['mahicchatā'])}"]
_WISH = [("không có niềm tin", "người có niềm tin"), ("phạm giới", "người giữ giới"),
         ("ít học hỏi", "người học rộng"), ("ưa thích tụ tập", "người sống tách biệt"),
         ("lười biếng", "người tinh tấn"), ("mất tỉnh thức", "người có sự tỉnh thức được thiết lập"),
         ("không được định tâm", "người được định tâm"), ("kém trí tuệ", "người có trí tuệ"),
         ("chưa diệt tận các ô nhiễm", "người đã diệt tận các ô nhiễm")]
_wish = "; ".join(f"{a} mà mong muốn “Mong người ta biết tôi là {b}”" for a, b in _WISH)
SEG["2-851"] = [f"{q('sự có ước muốn xấu xa')} {IDHEKACCO} {_wish} – {SUCH} sự mong muốn, trạng thái bị mong muốn "
                f"chi phối, sự có ước muốn xấu xa, {RAGA3} {called('sự có ước muốn xấu xa')}"]
SEG["2-852"] = [f"{q('sự kiểu cách')} {WHICH} sự kiểu cách, sự điệu đà, sự khôn lỏi, tính khôn lỏi, sự quanh co, "
                f"tính quanh co {called('sự kiểu cách')}"]
SEG["2-853"] = [f"{q('sự khó tính')} {WHICH} sự khó tính, sự khởi khó tính, trạng thái khởi khó tính, "
                + pi1("sự ham hố, sự khởi ham hố, trạng thái khởi ham hố, sự xu nịnh, sự mong muốn điều tốt đẹp")
                + f" {called('sự khó tính')}"]
SEG["2-854"] = [f"{q('sự phù phiếm')} Sự trang trí y phục, sự trang trí bình bát, sự trang trí chỗ ở, sự trang trí, sự "
                "tô điểm, sự nâng niu, sự nâng niu quá mức thân hôi thối này hoặc các vật dụng bên ngoài, sự ham thích, "
                f"trạng thái ham thích, sự nhẹ dạ, sự phù phiếm {called('sự phù phiếm')}"]
SEG["2-855"] = [f"{q(ONE[37])} Đối với mẹ, hoặc cha, hoặc người lớn tuổi hơn, hoặc anh em, hoặc các vị thầy, hoặc "
                "thầy tế độ, hoặc Đức Phật, hoặc các đệ tử, hoặc bất kỳ người đáng kính trọng nào, là sự tiếp nhận ngang "
                "trái, sự thích thú việc làm trái, sự thiếu tôn trọng, thái độ thiếu tôn trọng, sự thiếu kính trọng, sự "
                f"không vâng lời {called(ONE[37])}"]
ARATI_LINE = (f"{q(N['arati'])} Đối với những chỗ ở xa vắng, hoặc đối với bất kỳ hiện tượng thiện cao hơn nào, là "
              f"{ARATI} {called(N['arati'])}")
SEG["2-856"] = [ARATI_LINE]
SEG["2-857"] = [f"{q('sự lười nhác')} {WHICH} sự lười nhác, sự khởi lười nhác, tâm trạng lười nhác, sự biếng trễ, sự "
                f"khởi biếng trễ, trạng thái khởi biếng trễ {called('sự lười nhác')}"]
SEG["2-858"] = [f"{q('sự vươn vai')} {WHICH} sự vươn mình của thân, sự vươn vai, sự cúi xuống, sự ngả ra, sự co lại, "
                f"sự nghiêng mình, sự uể oải như bệnh {called('sự vươn vai')}"]
SEG["2-859"] = [f"{q(ONE[41])} Điều mà ở người đã ăn xong là sự lịm người vì bữa ăn, sự mệt mỏi vì bữa ăn, sự nóng "
                f"bỏng vì bữa ăn, sự nặng nề của thân {called(ONE[41])}"]
SEG["2-860"] = [f"{q(N['cetaso ca līnattaṃ'])} {THINA} của tâm {called(N['cetaso ca līnattaṃ'])}"]
SEG["2-861"] = [f"{q('sự lừa gạt')} Ở {LSS}, bằng điều gọi là việc thọ dụng vật dụng [dị bản (Sī.): "
                "paccayapaṭisedhanasaṅkhātena], hoặc bằng lời nói bóng gió, hoặc bằng tư thế, là sự sắp đặt [khác chính "
                "tả (Ka.): āṭhapanā], sự bày đặt, sự dàn dựng, sự nhăn mặt, vẻ nhăn mặt, sự lừa gạt, sự khởi lừa gạt, "
                f"trạng thái khởi lừa gạt {called('sự lừa gạt')}"]
SEG["2-862"] = [f"{q('sự nói ngọt')} Ở {LSS}, điều mà là sự bắt chuyện với người khác, sự nói ngọt, sự trò chuyện thân "
                "mật, sự tâng bốc, sự tâng bốc hết mức, sự bợ đỡ, sự bợ đỡ hết mức, sự gợi lòng, sự gợi lòng hết mức, sự "
                "nói lời chiều lòng, lời nịnh bợ, lời nửa thật nửa giả, việc chăm bẵm con trẻ "
                f"{called('sự nói ngọt')}"]
SEG["2-863"] = [f"{q('sự ra dấu gợi ý')} Ở {LSS}, điều mà là sự ra dấu với người khác, việc ra dấu, sự gợi ý, việc gợi "
                f"ý, lời nói bóng gió, lời nói vòng vo {called('sự ra dấu gợi ý')}"]
SEG["2-864"] = [f"{q('sự chèn ép')} Ở {LSS}, điều mà là sự mắng nhiếc người khác, sự khinh miệt, sự chê trách, sự chế "
                "giễu, sự chế giễu hết mức, sự nhạo báng, sự nhạo báng hết mức, sự bêu xấu, sự bêu xấu hết mức, sự loan "
                f"truyền tiếng xấu, sự nói xấu sau lưng {called('sự chèn ép')}"]
SEG["2-865"] = [f"{q(ONE[47])} {cap(LSS)}, mang vật phẩm nhận được ở đây đến nơi kia, hoặc mang vật phẩm nhận được ở "
                f"nơi kia về đây; {SUCH} sự tìm, sự tìm tòi, sự tìm tòi khắp nơi, sự tìm cầu, sự tìm kiếm, sự tìm kiếm "
                f"khắp nơi đối với vật phẩm {called(ONE[47])}"]
misfit("ullapanā, samukkācanā, avaṇṇahārikā, eṭṭhi / gaveṭṭhi / pariyeṭṭhi / gavesanā / pariyesanā (^2-862 … ^2-865, "
       "^2-963): no entries; built from the sibling entries («sự tâng bốc» after samullapanā, «sự gợi lòng hết mức», «sự "
       "loan truyền điều xấu», «sự tìm / sự tìm tòi / sự tìm tòi khắp nơi / sự tìm kiếm / sự tìm kiếm khắp nơi» beside "
       "esanā «sự tìm cầu»)")


_PL = "Ở đời này, có người dựa vào {g} mà nuôi dưỡng "
SEG["2-866"] = [f"{q(ONE[48])} {_PL.format(g=grounds(' [khác chính tả (Syā.): vijjaṭṭhānena]'))}sự kiêu mạn, {SUCH} "
                f"{MANA} {called(ONE[48])}"]
SEG["2-867"] = [f"{q(ONE[49])} {_PL.format(g=grounds())}sự kiêu mạn, {SUCH} {MANA} {called(ONE[49])}"]
SEG["2-868"] = [f"{q(ONE[50])} {_PL.format(g=grounds())}sự tự ti, {SUCH} {OMANA} {called(ONE[50])}"]


def mana3(i, who, thought, short, as_written=None):
    name = ONE[51 + i]
    th = as_written or thought
    om = thought == "hīna"
    g = GROUNDS_S if short else grounds()
    res = (f"{q(name)} {IDHEKACCO} vốn {SEYYA[who][0]} về {g}, và tự cho mình {SEYYA[th][1]}; dựa vào điều đó, người "
           f"ấy nuôi dưỡng {'sự tự ti' if om else 'sự kiêu mạn'}. ")
    if om:
        res += f"{cap(SUCH)} {OMANA}"
    elif short and i == 3:
        res += f"{cap(SUCH)} {MANA_A}… {MANA_B}"
    else:
        res += f"{cap(SUCH)} {MANA}"
    return res + f" {called(name)}"


_W = ["seyya", "sadisa", "hīna"]
for _i in range(9):
    _who, _th = _W[_i // 3], _W[_i % 3]
    SEG[f"2-{869 + _i}"] = [mana3(_i, _who, _th, _i >= 3, as_written="sadisa" if _i == 8 else None)]
slip("^2-877 (60) hīnassa hīnohamasmīti māno: «parehi sadisaṃ attānaṃ dahati» where hīnaṃ is expected (cf. ^2-871, "
     "^2-874): rendered as written («tự cho mình bằng người khác»)")
SEG["2-878"] = [f"{q('sự kiêu mạn')} {WHICH} {MANA} {called('sự kiêu mạn')}"]
SEG["2-879"] = [f"{q('sự ngạo mạn')} {IDHEKACCO}, dựa vào {GROUNDS_S}, tự cho mình vượt trên người khác. {cap(SUCH)} "
                f"{MANA} {called('sự ngạo mạn')}"]
SEG["2-880"] = [f"{q('sự kiêu mạn chồng chất')} {IDHEKACCO}, dựa vào {GROUNDS_S}, lúc trước tự cho mình bằng người "
                f"khác, lúc sau tự cho mình là hơn. {cap(SUCH)} {MANA} {called('sự kiêu mạn chồng chất')}"]
SEG["2-881"] = [f"{q('sự tự ti')} {_PL.format(g=grounds())}sự tự ti. {cap(SUCH)} {OMANA} {called('sự tự ti')}"]
SEG["2-882"] = [f"{q('sự tự đánh giá quá cao')} Sự có tri giác rằng đã đạt được đối với điều chưa đạt được, sự có tri "
                "giác rằng đã làm xong đối với điều chưa làm xong, sự có tri giác rằng đã chứng đắc đối với điều chưa "
                "chứng đắc, sự có tri giác rằng đã chứng nghiệm đối với điều chưa chứng nghiệm; "
                f"{SUCH} {MANA} {called('sự tự đánh giá quá cao')}"]
_AM = "sự kiêu mạn “Tôi là”, ý muốn “Tôi là”, khuynh hướng tiềm ẩn “Tôi là”"
SEG["2-883"] = [f"{q(ONE[65])} Đối với vật chất là {_AM}; đối với cảm giác… tri giác… các sự tạo tác… thức là {_AM}; "
                f"{SUCH} {MANA} {called(ONE[65])}"]
SEG["2-884"] = [f"{q('sự kiêu mạn sai lầm')} {IDHEKACCO} dựa vào ngành nghề xấu ác, hoặc ngành thủ công xấu ác, hoặc "
                "lĩnh vực học thuật xấu ác, hoặc sự học hỏi xấu ác, hoặc tài ứng đáp xấu ác, hoặc giới hạnh xấu ác, "
                "hoặc nghi thức xấu ác, hoặc giới hạnh và nghi thức xấu ác, hoặc quan điểm xấu xa, một điều nào đó, "
                f"thứ này hay thứ khác, mà nuôi dưỡng sự kiêu mạn, {SUCH} {MANA} {called('sự kiêu mạn sai lầm')}"]
_HOME = "gắn với đời sống thế tục"
SEG["2-885"] = [f"{q(ONE[67])} {cap(THOUGHT)}, {_HOME}, liên quan đến người thân {called(ONE[67])}"]
SEG["2-886"] = [f"{q(ONE[68])} {cap(THOUGHT)}, {_HOME}, liên quan đến xứ sở {called(ONE[68])}"]
SEG["2-887"] = [f"{q(ONE[69])} {cap(THOUGHT)}, {_HOME}, liên quan đến việc thực hành khổ hạnh hoặc liên quan đến "
                f"sự mắc kẹt trong các quan điểm {called(ONE[69])}"]
SEG["2-888"] = [f"{q(ONE[70])} {IDHEKACCO} sống giao du với người tại gia, vui cùng họ, buồn cùng họ, hạnh phúc khi họ "
                "hạnh phúc, khổ khi họ khổ, hoặc khi có những việc cần làm và nên làm thì tự mình dấn thân vào. "
                f"{YA_TATTHA} {THOUGHT} {_HOME} {called(ONE[70])}"]
SEG["2-889"] = [f"{q(ONE[71])} {cap(THOUGHT)}, {_HOME}, liên quan đến lợi lộc, sự tôn vinh và tiếng tăm "
                f"{called(ONE[71])}"]
SEG["2-890"] = [f"{q(ONE[72])} {IDHEKACCO}, dựa vào {grounds()}, nghĩ rằng “Mong người khác đừng xem nhẹ tôi”. "
                f"{YA_TATTHA} {THOUGHT} {_HOME} {called(ONE[72])}", CLOSE[1]]

# =========================================================================== the twofold exposition (^2-891 … ^2-908)
SEG["2-891"] = [
    lab("Ka", f"{q(N['kodho'])} {WHICH} {KODHA14} {called(N['kodho'])}"),
    lab("Kha", f"{q(N['upanāho'])} Lúc trước là sự giận dữ, lúc sau là sự ôm hận. {cap(SUCH)} sự ôm hận, sự khởi ôm "
               "hận, trạng thái khởi ôm hận, sự lưu giữ, sự giữ lại, sự giữ chặt, sự nối kết, sự kéo dài liên tục, sự "
               f"làm cho sự giận dữ thêm vững chắc {called(N['upanāho'])}")]
SEG["2-892"] = [
    lab("Ka", f"{q(N['makkho'])} {WHICH} sự gièm pha, sự khởi gièm pha, trạng thái khởi gièm pha [khác chính tả (Sī., "
              "Ka.): makkhiyanā makkhiyitattaṃ], sự khắc nghiệt, hành động khắc nghiệt "
              f"{called(N['makkho'])}"),
    lab("Kha", f"{q(N['paḷāso'])} {WHICH} sự ganh đua, sự khởi ganh đua [khác chính tả (Syā.): palāsāyanā "
               "palāsāyitattaṃ], sự ôm giữ sự ganh đua, nguyên cớ tranh cãi, sự đòi ngang hàng, sự không chịu buông bỏ "
               f"{called(N['paḷāso'])}")]
SEG["2-893"] = [
    lab("Ka", f"{q(N['issā'])} {ISSA} {called(N['issā'])}"),
    lab("Kha", f"{q(N['macchariyaṃ'])} {MACCH5}. {MACCH_LIST} [dị bản (Sī., Ka.): paggahitattaṃ; xem {DHS} 1127] "
               f"của tâm {called(N['macchariyaṃ'])}")]
_NOT_KNOW = "“Mong người ta đừng biết về tôi”"
SEG["2-894"] = [
    lab("Ka", f"{q(N['māyā'])} {IDHEKACCO} sau khi làm hành vi xấu bằng thân, sau khi làm hành vi xấu bằng lời nói, "
              "sau khi làm hành vi xấu bằng ý, vì muốn che giấu điều đó mà đặt ra ước muốn xấu xa. Người ấy mong muốn "
              f"{_NOT_KNOW}. Người ấy suy tính {_NOT_KNOW}. Người ấy nói lời {_NOT_KNOW}. Người ấy hành động bằng thân "
              f"{_NOT_KNOW}. {cap(SUCH)} sự xảo trá, tính xảo trá, sự lấn lướt, sự lừa dối, sự gian lận, sự đánh lạc "
              "hướng, sự lảng tránh, sự giấu giếm, sự giấu giếm kỹ, sự che đậy, sự che giấu, sự không bày tỏ, sự không "
              f"bộc lộ, sự che đậy hoàn toàn, việc làm xấu ác {called(N['māyā'])}"),
    lab("Kha", f"{q(N['sāṭheyyaṃ'])} {IDHEKACCO} gian trá, rất gian trá. {YA_TATTHA} sự gian trá, tính gian trá, sự gian "
               "xảo, sự xảo quyệt, tính xảo quyệt [dị bản (Syā.): kakkhaḷatā kakkhaḷiyaṃ], sự quanh co, tính quanh co "
               f"{called(N['sāṭheyyaṃ'])}")]
SEG["2-895"] = [lab("Ka", f"{q('vô minh')} {AVIJJA_S} {called('vô minh')}"),
                lab("Kha", f"{q(N['bhavataṇhā'])} {BHAVA8} {called(N['bhavataṇhā'])}")]


def view_line(k, thesis, name, quoted=True):
    return lab(k, f"{q(name)} “{thesis}” – {DITTHI_S} {called(name, quoted)}")


SEG["2-896"] = [view_line("Ka", "Tự ngã và thế gian sẽ tồn tại", N["bhavadiṭṭhi"]),
                view_line("Kha", "Tự ngã và thế gian sẽ không tồn tại", N["vibhavadiṭṭhi"], quoted=False)]
slip("^2-896 (Kha) «ayaṃ vuccati vibhavadiṭṭhi» without quotation marks: kept so")
SEG["2-897"] = [view_line("Ka", "Tự ngã và thế gian là trường tồn", N["sassatadiṭṭhi"]),
                view_line("Kha", "Tự ngã và thế gian sẽ bị đoạn diệt", N["ucchedadiṭṭhi"])]
SEG["2-898"] = [view_line("Ka", "Tự ngã và thế gian là hữu hạn", N["antavādiṭṭhi"]),
                view_line("Kha", "Tự ngã và thế gian là vô hạn", N["anantavādiṭṭhi"])]
SEG["2-899"] = [
    lab("Ka", f"{q(N['pubbantānudiṭṭhi'])} Liên quan đến quá khứ, {DITTHI_ARISES} {called(N['pubbantānudiṭṭhi'])}"),
    lab("Kha", f"{q(N['aparantānudiṭṭhi'])} Liên quan đến tương lai, {DITTHI_ARISES} {called(N['aparantānudiṭṭhi'])}")]
AHIRIKA_LINE = f"{q(N['ahirikaṃ'])} {AHIRIKA} {called(N['ahirikaṃ'])}"
ANOTTAPPA_LINE = f"{q(N['anottappaṃ'])} {ANOTTAPPA} {called(N['anottappaṃ'])}"
SEG["2-900"] = [lab("Ka", AHIRIKA_LINE), lab("Kha", ANOTTAPPA_LINE)]
DOVACASSA_LINE = f"{q(N['dovacassatā'])} {DOVACASSA} {called(N['dovacassatā'])}"


def papamitta(extra="", taṃ=True):
    end = PAPAMITTA_B if taṃ else PAPAMITTA_B[:-len(" họ")]
    return f"{q(N['pāpamittatā'])} {PAPAMITTA_A}{extra}, {end} {called(N['pāpamittatā'])}"


SEG["2-901"] = [lab("Ka", DOVACASSA_LINE), lab("Kha", papamitta(taṃ=False))]
slip("^2-901 (Kha) «bhatti sambhatti sampavaṅkatā» (taṃ- missing, cf. ^2-U12 / pi-1 ^1-1333 taṃsampavaṅkatā): "
     "rendered as written, «sự nghiêng về phía» without «họ»")
SEG["2-902"] = [
    lab("Ka", f"{q(N['anajjavo'])} {WHICH} sự không ngay thật, tính không ngay thật, sự quanh co, sự cong queo, sự "
              f"vặn vẹo {called(N['anajjavo'])}"),
    lab("Kha", f"{q(N['amaddavo'])} {WHICH} sự không mềm mại, sự không mềm mỏng, tính thô cứng, tính thô lỗ, sự thô "
               "cứng, sự cứng nhắc [khác chính tả (Syā., Ka.): kathinatā], sự cao ngạo của tâm, sự không mềm mại "
               f"{called(N['amaddavo'])}")]
SEG["2-903"] = [
    lab("Ka", f"{q(N['akkhanti'])} {WHICH} sự không nhẫn nại, sự không bao dung, sự không chịu đựng, sự hung dữ, sự nói "
              f"năng cộc cằn, sự không hài lòng của tâm {called(N['akkhanti'])}"),
    lab("Kha", f"{q(N['asoraccaṃ'])} {cap(VITIKKAMA)} {called(N['asoraccaṃ'])} Mọi sự phạm giới đều là "
               f"{N['asoraccaṃ']}.")]
SEG["2-904"] = [
    lab("Ka", f"{q(N['asākhalyaṃ'])} Lời nói nào gai góc, cay nghiệt, làm người khác đau lòng, xúc phạm người "
              "khác, gần với sự giận dữ, không đưa đến định tâm, người ấy nói lời như vậy. "
              f"{YA_TATTHA} sự không dịu dàng trong lời nói, sự không hòa nhã trong lời nói, sự thô ác trong lời nói "
              f"{called(N['asākhalyaṃ'])}"),
    lab("Kha", f"Ở đây, {N['appaṭisanthāro']} [khác chính tả (Ka.): appaṭisandhāro] là gì? Hai loại niềm nở tiếp đón – "
               "niềm nở tiếp đón bằng vật phẩm và niềm nở tiếp đón bằng Giáo Pháp. "
               f"{IDHEKACCO} không niềm nở tiếp đón, với sự niềm nở tiếp đón bằng vật phẩm hoặc với sự niềm nở tiếp "
               f"đón bằng Giáo Pháp {called(N['appaṭisanthāro'])}")]
misfit("dhammapaṭisanthāro (^2-904): «niềm nở tiếp đón bằng Giáo Pháp» (dhamma 'the Teaching' sense, beside "
       "āmisapaṭisanthāro «… bằng vật phẩm»)")
_IND = VI(2, "12-jhanavibhango.md", "Tattha katamā indriyesu aguttadvāratā?")
_BHOJ = VI(2, "12-jhanavibhango.md", "Tattha katamā bhojane amattaññutā?")
pi2(_IND)
pi2(_BHOJ)
GUARD_BODY = _IND.split(" là gì? ", 1)[1].split(" Điều mà đối với sáu năng lực này", 1)[0]   # ends «… năng lực ý.»
SEG["2-905"] = [lab("Ka", _IND), lab("Kha", _BHOJ)]
slip("^2-905 (Kha) «ayaṃ vuccati \"bhojane amattaññutā.\"» (full stop inside the quotation): rendered as ch. 12")
SEG["2-906"] = [lab("Ka", f"{q(N['muṭṭhassaccaṃ'])} {MUTTHASSACCA} {called(N['muṭṭhassaccaṃ'])}"),
                lab("Kha", f"{q(N['asampajaññaṃ'])} {ASAMPAJANNA} {called(N['asampajaññaṃ'])}")]
SEG["2-907"] = [
    lab("Ka", f"{q(N['sīlavipatti'])} {WHICH} {VITIKKAMA} {called(N['sīlavipatti'])} Mọi sự phạm giới đều là "
              f"{N['sīlavipatti']}."),
    lab("Kha", f"{q(N['diṭṭhivipatti'])} {NIHIL_S} – {DITTHI_S} {called(N['diṭṭhivipatti'])} Mọi quan điểm sai lầm "
               f"đều là {N['diṭṭhivipatti']}.")]
pi1("Mọi sự phạm giới đều là sự suy đồi về giới hạnh.")
SEG["2-908"] = [
    f"(a) {q(N['ajjhattasaṃyojanaṃ'])} {cap(T['Pañcorambhāgiyāni saṃyojanāni'])} – {N['ajjhattasaṃyojanaṃ']}. (b) "
    f"{cap(T['Pañcuddhambhāgiyāni saṃyojanāni'])} – {N['bahiddhāsaṃyojanaṃ']}.", CLOSE[2]]

# =========================================================================== the threefold exposition (^2-909 … ^2-U31)
DOSA_HEAD = ("Sự oán giận khởi lên với ý nghĩ “Người ấy đã gây hại cho tôi”, sự oán giận khởi lên với ý nghĩ “Người ấy "
             "đang gây hại cho tôi”, sự oán giận khởi lên với ý nghĩ “Người ấy sẽ gây hại cho tôi”, sự oán giận khởi "
             "lên với ý nghĩ “Người ấy đã gây hại cho người yêu quý, ưa thích của tôi”… đang gây hại… “sẽ gây hại”, "
             "sự oán giận khởi lên với ý nghĩ “Người ấy đã làm lợi cho người không yêu quý, không ưa thích của tôi”… "
             "đang làm lợi… “sẽ làm lợi”, hoặc sự oán giận khởi lên một cách vô cớ")
pi1("hoặc sự oán giận khởi lên một cách vô cớ")
SEG["2-909"] = [
    f"{qn(T['Tīṇi akusalamūlāni'])} Sự tham lam, sự sân hận, sự si mê.",
    lab("Ka", f"{q('sự tham lam')} {lobha()} {called('sự tham lam')}"),
    lab("Kha", f"{q('sự sân hận')} {DOSA_HEAD}. {cap(SUCH)} {DOSA_LIST} {called('sự sân hận')}"),
    lab("Ga", f"{q('sự si mê')} {TRUTHS}; {SUCH} {AVIJJA_TAIL} {called('sự si mê')} "
              f"{this_is(T['Tīṇi akusalamūlāni'], False)}")]
_V3 = [("dục lạc", "sự hướng tâm đến dục lạc"), ("ác ý", "sự hướng tâm đến ác ý"),
       ("sự hãm hại", "sự hướng tâm đến sự hãm hại")]


def vitakka_line(k, obj, name):
    return lab(k, f"{q(name)} {cap(THOUGHT)}, liên quan đến {obj} {called(name)}")


SEG["2-910"] = [f"{qn(T['Tayo akusalavitakkā'])} {cap(', '.join(n for _, n in _V3))}."] + [
    vitakka_line(k, o, n) for k, (o, n) in zip(("Ka", "Kha", "Ga"), _V3)]
SEG["2-910"][-1] += f" {this_is(T['Tayo akusalavitakkā'], False)}"
_S3 = [("dục lạc", "tri giác về dục lạc"), ("ác ý", "tri giác về ác ý"), ("sự hãm hại", "tri giác về sự hãm hại")]
SEG["2-911"] = [f"{qn(T['Tisso akusalasaññā'])} {cap(', '.join(n for _, n in _S3))}."] + [
    lab(k, f"{q(n)} {cap(SANNA3)}, liên quan đến {o} {called(n)}") for k, (o, n) in zip(("Ka", "Kha", "Ga"), _S3)]
SEG["2-911"][-1] += f" {this_is(T['Tisso akusalasaññā'], False)}"
SEG["2-912"] = [f"{qn(T['Tisso akusaladhātuyo'])} Yếu tố dục lạc, yếu tố ác ý, yếu tố hãm hại.",
                f"{q('yếu tố dục lạc')} Sự hướng tâm đến dục lạc là yếu tố dục lạc. Sự hướng tâm đến ác ý là yếu tố "
                "ác ý. Sự hướng tâm đến sự hãm hại là yếu tố hãm hại."] + [
    vitakka_line(k, o, n) for k, (o, n) in zip(("Ka", "Kha", "Ga"), _V3)]
SEG["2-912"][-1] += f" {this_is(T['Tisso akusaladhātuyo'], False)}"
pi2("yếu tố dục lạc")
pi2("yếu tố hãm hại")
SEG["2-913"] = [
    f"{qn(T['Tīṇi duccaritāni'])} Hành vi xấu bằng thân, hành vi xấu bằng lời nói, hành vi xấu bằng ý.",
    lab("Ka", f"{q('hành vi xấu bằng thân')} {cap(KILL)}, {STEAL}, {SEX} {called('hành vi xấu bằng thân')}"),
    lab("Kha", f"{q('hành vi xấu bằng lời nói')} {cap(SPEECH4)} {called('hành vi xấu bằng lời nói')}"),
    lab("Ga", f"{q('hành vi xấu bằng ý')} {cap(MIND3)} {called('hành vi xấu bằng ý')}"),
    "(a-c) " + f"{q('hành vi xấu bằng thân')} Nghiệp bất thiện bằng thân là hành vi xấu bằng thân, nghiệp bất thiện "
    "bằng lời nói là hành vi xấu bằng lời nói, nghiệp bất thiện bằng ý là hành vi xấu bằng ý.",
    f"{q('nghiệp bất thiện bằng thân')} Sự cố ý bất thiện bằng thân là nghiệp bất thiện bằng thân, sự cố ý bất thiện "
    "bằng lời nói là nghiệp bất thiện bằng lời nói, sự cố ý bất thiện bằng ý là nghiệp bất thiện bằng ý. "
    + this_is(T['Tīṇi duccaritāni'], False)]
misfit("kāyasañcetanā / vacī- / manosañcetanā (^2-913): no entry; «sự cố ý … bằng thân / bằng lời nói / bằng ý» "
       "(sañcetanā «sự cố ý»)")
SEG["2-914"] = [
    f"{qn(T['Tayo āsavā'])} Ô nhiễm dục lạc, ô nhiễm hiện hữu, ô nhiễm vô minh.",
    lab("Ka", f"{q(N['kāmāsavo'])} {KAMA8} {called(N['kāmāsavo'])}"),
    lab("Kha", f"{q(N['bhavāsavo'])} {BHAVA_S} {called(N['bhavāsavo'])}"),
    lab("Ga", f"{q(N['avijjāsavo'])} {TRUTHS_S} {called(N['avijjāsavo'])} {this_is(T['Tayo āsavā'], False)}")]
SEG["2-915"] = [
    f"{qn(T['Tīṇi saṃyojanāni'])} Quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức.",
    lab("Ka", f"{q('quan điểm về tự ngã')} {SAKKAYA} {called('quan điểm về tự ngã')}"),
    lab("Kha", f"{q('sự hoài nghi')} {VICIKICCHA_A}. {cap(SUCH)} {VICIKICCHA_B} {called('sự hoài nghi')}"),
    lab("Ga", f"{q('sự hiểu sai lệch về giới hạnh và nghi thức')} {SILABBATA} – {DITTHI_S} "
              f"{called('sự hiểu sai lệch về giới hạnh và nghi thức')} {this_is(T['Tīṇi saṃyojanāni'], False)}")]
pi1("sự hiểu sai lệch về giới hạnh và nghi thức")


def rag(obj, how="liên quan đến"):
    """X-paṭisaṃyutto / X-sahagato rāgo sārāgo cittassa sārāgo"""
    return f"{cap(RAGA3)}, {how} {obj}"


_KT, _BT, _VT = "khao khát dục lạc", "khao khát được hiện hữu", "khao khát không còn hiện hữu"
_RT, _AT, _NT = "khao khát cõi hình sắc", "khao khát cõi không hình sắc", "khao khát sự chấm dứt"
_WITH = "đi kèm với"
SEG["2-916"] = [
    f"{qn(T['Tisso taṇhā'])} {cap(_KT)}, {_BT}, {_VT}.",
    f"{q(_BT)} {rag(N['bhavadiṭṭhi'], _WITH)} {called(_BT)}",
    f"{q(_VT)} {rag(N['ucchedadiṭṭhi'], _WITH)} {called(_VT)} Khao khát còn lại là {_KT}.",
    f"{q(_KT)} {rag('cõi dục lạc')} {called(_KT)}",
    f"( ) [(ở đây, {_BT} là gì)] {rag('cõi hình sắc và cõi không hình sắc')} {called(_BT)}",
    f"( ) [(ở đây, {_VT} là gì) (?)] {rag(N['ucchedadiṭṭhi'], _WITH)} {called(_VT)} "
    + this_is(T['Tisso taṇhā'], False)]
pi1("đi kèm")
SEG["2-917"] = [
    f"{qn(T['Aparāpi tisso taṇhā'])} {cap(_KT)}, {_RT}, {_AT}.",
    lab("Ka", f"{q(_KT)} {rag('cõi dục lạc')} {called(_KT)}"),
    lab("Kha", f"{q(_RT)} {rag('cõi hình sắc')} {called(_RT)}"),
    lab("Ga", f"{q(_AT)} {rag('cõi không hình sắc')} {called(_AT)} {this_is(T['Tisso taṇhā'], False)}")]
SEG["2-918"] = [
    f"{qn(T['Aparāpi tisso taṇhā'])} {cap(_RT)}, {_AT}, {_NT}.",
    lab("Ka", f"{q(_RT)} {rag('cõi hình sắc')} {called(_RT)}"),
    lab("Kha", f"{q(_AT)} {rag('cõi không hình sắc')} {called(_AT)}"),
    lab("Ga", f"{q(_NT)} {rag(N['ucchedadiṭṭhi'], _WITH)} {called(_NT)} {this_is(T['Tisso taṇhā'], False)}")]
_E = ("sự tìm cầu dục lạc", "sự tìm cầu sự hiện hữu", "sự tìm cầu đời sống tu hành trong sạch")
_VIEWS10_DASH = VIEWS10.replace("“Thế gian không trường tồn”, hoặc “Thế gian là hữu hạn”", "“Thế gian không trường "
                                "tồn” – hoặc", 1)
_VIEWS10_DASH = _VIEWS10_DASH.split(" – hoặc", 1)[0] + " – hoặc… hoặc “Như Lai không phải còn tồn tại cũng không "\
    "phải không còn tồn tại sau khi chết”"
_KAMMA3 = ("các nghiệp bất thiện cùng hiện diện với nó: nghiệp bằng thân, nghiệp bằng lời nói, nghiệp bằng "
           "ý")
SEG["2-919"] = [
    f"{qn(T['Tisso esanā'])} {cap(', '.join(_E))}.",
    lab("Ka", f"{q(_E[0])} {KAMA_S} {called(_E[0])}"),
    lab("Kha", f"{q(_E[1])} {BHAVA_S} {called(_E[1])}"),
    lab("Ga", f"{q(_E[2])} {_VIEWS10_DASH}; {DITTHI_S} {called(_E[2])}"),
    lab("Ka", f"Ở đây, {_E[0]} là gì, sự tham đắm dục lạc và {_KAMMA3} {called(_E[0])}"),
    lab("Kha", f"Ở đây, {_E[1]} là gì, sự tham đắm hiện hữu và {_KAMMA3} {called(_E[1])}"),
    lab("Ga", f"Ở đây, {_E[2]} là gì, quan điểm chấp giữ cực đoan và {_KAMMA3} {called(_E[2])} "
              + this_is(T['Tisso esanā'], False))]
slip("^2-919 (Ga) «\"asassato loko\"ti – vā…pe…»: stray dash before «vā», kept at the same spot (dash rule)")
slip("^2-919 second (Ka)-(Ga): «tattha katamā kāmesanā, kāmarāgo …» comma where «?» is expected: kept as a comma")
SEG["2-920"] = [f"{qn(T['Tisso vidhā'])} Sự so sánh “Tôi hơn người”, sự so sánh “Tôi bằng người”, sự so sánh “Tôi kém "
                f"người” {this_is(T['Tisso vidhā'])}"]
_FEAR = "mà có nỗi sợ hãi, sự kinh hãi, trạng thái cứng đờ, sự dựng tóc gáy, sự hoảng hốt của tâm"
_B3 = [("sự sinh", "nỗi sợ hãi về sự sinh"), ("sự lão hóa", "nỗi sợ hãi về sự lão hóa"),
       ("sự chết", "nỗi sợ hãi về sự chết")]
SEG["2-921"] = [f"{qn(T['Tīṇi bhayāni'])} {cap(', '.join(n for _, n in _B3))}."] + [
    lab(k, f"{q(n)} Dựa vào {o} {_FEAR} {called(n)}") for k, (o, n) in zip(("Ka", "Kha", "Ga"), _B3)]
SEG["2-921"][-1] += f" {this_is(T['Tīṇi bhayāni'], False)}"
_DOUBT4 = "người ta nghi ngờ, hoài nghi, không quyết định, không có lòng tin trong sáng"
SEG["2-922"] = [f"{qn(T['Tīṇi tamāni'])} Liên quan đến thời quá khứ, {_DOUBT4}; hoặc liên quan đến thời tương lai, "
                f"{_DOUBT4}; hoặc liên quan đến thời hiện tại bây giờ, {_DOUBT4} {this_is(T['Tīṇi tamāni'])}"]
_FEEL3 = "điều dễ chịu, hoặc khó chịu, hoặc không khó chịu cũng không dễ chịu"
_ALL = f"“Bất cứ điều gì con người này cảm nhận, {_FEEL3}, tất cả đều"
SEG["2-923"] = [f"{qn(T['Tīṇi titthāyatanāni'])} {SAMANA} – {_ALL} do việc đã làm trong quá khứ”; ở đời này, lại có "
                f"sa-môn hoặc bà-la-môn có học thuyết như vầy, có quan điểm như vầy – {_ALL} do sự sáng tạo của đấng "
                "Tự Tại”; ở đời này, lại có sa-môn hoặc bà-la-môn có học thuyết như vầy, có quan điểm như vầy – "
                f"{_ALL} không có nguyên nhân, không có điều kiện” {this_is(T['Tīṇi titthāyatanāni'])}"]
misfit("pubbe katahetu / issaranimmānahetu (^2-923): no entries; «do việc đã làm trong quá khứ», «do sự sáng tạo của "
       "đấng Tự Tại» (member issara «đấng Tự Tại»)")
SEG["2-924"] = [f"Ở đây, {T['Tayo kiñcanā']} [dị bản (?): katamāni tīṇi kiñcanāni; {DN} 3.305] là những gì? Sự tham "
                "đắm là sự vướng bận, sự sân hận là sự vướng bận, sự si mê là sự vướng bận "
                f"{this_is(T['Tayo kiñcanā'])}"]


def rdm(word, key):
    return (f"{qn(T[key])} Sự tham đắm là {word}, sự sân hận là {word}, sự si mê là {word} {this_is(T[key])}")


SEG["2-U1"] = [rdm("vết nhơ", "Tīṇi aṅgaṇāni")]
SEG["2-U2"] = [rdm("sự dơ bẩn", "Tīṇi malāni")]
SEG["2-U3"] = [rdm("sự lệch lạc", "Tīṇi visamāni")]
SEG["2-U4"] = [f"{qn(T['Aparānipi tīṇi visamāni'])} Sự lệch lạc của thân, sự lệch lạc của lời nói, sự lệch lạc của ý "
               f"{this_is(T['Tīṇi visamāni'])}"]
SEG["2-U5"] = [f"{qn(T['Tayo aggī'])} Ngọn lửa tham đắm, ngọn lửa sân hận, ngọn lửa si mê {this_is(T['Tayo aggī'])}"]
SEG["2-U6"] = [f"{qn(T['Tayo kasāvā'])} Chất cặn bẩn tham đắm, chất cặn bẩn sân hận, chất cặn bẩn si mê "
               f"{this_is(T['Tayo kasāvā'])}"]
SEG["2-U7"] = [f"{qn(T['Aparepi tayo kasāvā'])} Chất cặn bẩn của thân, chất cặn bẩn của lời nói, chất cặn bẩn của ý "
               f"{this_is(T['Tayo kasāvā'])}"]
SEG["2-925"] = [f"{q(N['assādadiṭṭhi'])} {SAMANA} – “Không có lỗi trong các dục lạc”. Người ấy lao vào sự đắm say "
                f"trong các dục lạc. Đó được gọi là “{N['assādadiṭṭhi']}”."]
SEG["2-U8"] = [f"{q(N['attānudiṭṭhi'])} {SAKKAYA} {called(N['attānudiṭṭhi'])}"]
SEG["2-U9"] = [f"{q(N['micchādiṭṭhi'])} {NIHIL_S} – {DITTHI_S} {called(N['micchādiṭṭhi'])} Quan điểm về sự trường tồn "
               "là quan điểm về sự thỏa thích, quan điểm về tự ngã là quan điểm xem có tự ngã, quan điểm về sự đoạn "
               "diệt là quan điểm sai lầm."]
SEG["2-926"] = [ARATI_LINE]
_VIH = VI(2, "3-dhatuvibhango.md", "Tattha katamā vihiṃsādhātu?")
pi2(_VIH)
_VIH_BODY = _VIH.split("“yếu tố hãm hại”. ", 1)[1].rsplit(" – đó được gọi là", 1)[0]
SEG["2-U10"] = [f"{q(N['vihesā'])} {_VIH_BODY} {called(N['vihesā'])}"]
SEG["2-U11"] = [f"{q(N['adhammacariyā'])} Hành vi phi pháp, hành vi lệch lạc bằng thân; hành vi phi pháp, hành vi lệch "
                f"lạc bằng lời nói; hành vi phi pháp, hành vi lệch lạc bằng ý {called(N['adhammacariyā'])}"]
SEG["2-927"] = [DOVACASSA_LINE]
SEG["2-U12"] = [papamitta()]
SEG["2-U13"] = [f"{q(N['nānattasaññā'])} Tri giác về dục lạc, tri giác về ác ý, tri giác về sự hãm hại "
                f"{called(N['nānattasaññā'])} Mọi tri giác bất thiện đều là {N['nānattasaññā']}."]
UDDHACCA_LINE = f"{q(N['uddhaccaṃ'])} {UDDHACCA} {called(N['uddhaccaṃ'])}"
SEG["2-928"] = [UDDHACCA_LINE]
KOSAJJA_LINE = f"{q(N['kosajjaṃ'])} {lax()} {called(N['kosajjaṃ'])}"
PAMADA_LINE = f"{q(N['pamādo'])} {lax()}, {PAMADA_END} {called(N['pamādo'])}"
SEG["2-U14"] = [KOSAJJA_LINE]
SEG["2-U15"] = [PAMADA_LINE]
SEG["2-929"] = [f"{q(N['asantuṭṭhitā'])} {WANT_MORE.format(x=N['asantuṭṭhitā'])} {called(N['asantuṭṭhitā'])}"]
SEG["2-U16"] = [f"{q(N['asampajaññatā'])} {ASAMPAJANNA} {called(N['asampajaññatā'])}"]
SEG["2-U17"] = SEG["2-850"]
SEG["2-930"] = [AHIRIKA_LINE]
SEG["2-U18"] = [ANOTTAPPA_LINE]
SEG["2-U19"] = [PAMADA_LINE]
SEG["2-931"] = [f"{q(N['anādariyaṃ'])} {WHICH} sự thiếu tôn trọng, thái độ thiếu tôn trọng, sự thiếu kính trọng, sự "
                "không vâng lời, sự coi thường, sự khởi coi thường, trạng thái khởi coi thường [khác chính tả (Syā.): "
                f"anādā anādāyanā anādāyitattaṃ], sự thiếu lễ độ, sự không quý trọng {called(N['anādariyaṃ'])}"]
SEG["2-U20"] = [DOVACASSA_LINE]
SEG["2-U21"] = [papamitta(", sự lui tới")]
slip("^2-U21 pāpamittatā adds «paṭisevanā» to the list (^2-U12 and pi-1 ^1-1333 lack it): rendered as written («sự "
     "lui tới»)")
SEG["2-932"] = [f"{q(N['assaddhiyaṃ'])} {IDHEKACCO} không có niềm tin, không tin Đức Phật, hoặc Giáo Pháp, hoặc Tăng "
                f"đoàn; {SUCH} sự thiếu niềm tin, sự không tin tưởng, sự không tin chắc, sự không có lòng tin trong "
                f"sáng {called(N['assaddhiyaṃ'])}"]
SEG["2-U22"] = [f"{q(N['avadaññutā'])} {MACCH5}. {MACCH_LIST} của tâm {called(N['avadaññutā'])}"]
SEG["2-U23"] = [KOSAJJA_LINE]
slip("^2-U23 kosajjaṃ: extra commas «cittassa vossaggo, vossaggānuppadānaṃ kusalānaṃ dhammānaṃ, bhāvanāya …»: "
     "same wording as ^2-U14")
SEG["2-933"] = [UDDHACCA_LINE]
slip("^2-933 «bhavantattaṃ cittassa» for bhantattaṃ: termbase gives both «trạng thái rối loạn», same wording as ^2-928")
SEG["2-U24"] = [f"{q(N['asaṃvaro'])} {GUARD_BODY[:-1]} {called(N['asaṃvaro'])}"]
SEG["2-U25"] = [f"{q(N['dussīlyaṃ'])} {cap(VITIKKAMA)} {called(N['dussīlyaṃ'])}"]
SEG["2-934"] = [f"{q(N['ariyānaṃ adassanakamyatā'])} Ở đây, các bậc thánh là những ai? Các bậc thánh được gọi là chư "
                "Phật và các đệ tử của Đức Phật. Điều mà là sự không mong muốn thấy, sự không muốn nhìn, sự không mong "
                "muốn đến gần, sự không muốn cùng hội họp với các bậc thánh này "
                f"{called(N['ariyānaṃ adassanakamyatā'])}"]
_SADDHAMMA = ("Bốn sự thiết lập tỉnh thức, bốn nỗ lực đúng đắn, bốn nền tảng thần thông, năm năng lực, năm sức mạnh, "
              "bảy chi phần giác ngộ, con đường cao quý gồm tám chi phần")
SEG["2-U26"] = [f"{q(N['saddhammaṃ asotukamyatā'])} Ở đây, Giáo Pháp chân chính là gì? {_SADDHAMMA} "
                f"{called('Giáo Pháp chân chính')} Điều mà là sự không muốn nghe, sự không muốn lắng nghe, sự không muốn "
                "học hỏi, sự không muốn ghi nhớ Giáo Pháp chân chính này "
                f"{called(N['saddhammaṃ asotukamyatā'])}"]
SEG["2-U27"] = [f"{q(N['upārambhacittatā'])} Ở đây, sự bắt lỗi là gì? {WHICH} sự bắt lỗi, sự bắt lỗi liên tục, hành "
                "động bắt lỗi, hành động bắt lỗi liên tục, trạng thái bắt lỗi liên tục, sự coi thường, sự xem nhẹ, sự "
                f"khinh miệt, sự tìm kẽ hở {called(N['upārambhacittatā'])}"]
SEG["2-935"] = [f"{q(N['muṭṭhassaccaṃ'])} {MUTTHASSACCA} {called(N['muṭṭhassaccaṃ'])}"]
SEG["2-U28"] = [f"{q(N['asampajaññaṃ'])} {ASAMPAJANNA} {called(N['asampajaññaṃ'])}"]
SEG["2-U29"] = [f"{q(N['cetaso vikkhepo'])} {UDDHACCA} {called(N['cetaso vikkhepo'])}"]
_YON = "sự chú tâm không khôn ngoan rằng"
SEG["2-936"] = [f"{q(N['ayoniso manasikāro'])} {cap(_YON)} “thường còn” đối với điều vô thường, {_YON} “hạnh phúc” "
                f"đối với điều khổ đau, {_YON} “tự ngã” đối với điều không phải tự ngã, {_YON} “đẹp” đối với điều "
                "không đẹp; hoặc sự hướng đến, sự hướng đến liên tục, sự chú hướng, sự lưu ý, sự chú tâm của tâm trái "
                f"ngược với sự thật {called(N['ayoniso manasikāro'])}"]
SEG["2-U30"] = [f"{q(N['kummaggasevanā'])} Ở đây, con đường lệch lạc là gì? {cap(WRONG8)} "
                f"{called('con đường lệch lạc')} Điều mà là sự đi theo, sự thường xuyên đi theo, sự đi theo mật thiết, "
                "sự gần gũi, sự gần gũi mật thiết, sự gắn bó, sự gắn bó mật thiết, sự nghiêng về phía con đường lệch "
                f"lạc này {called(N['kummaggasevanā'])}"]
SEG["2-U31"] = [f"{q(N['cetaso ca līnattaṃ'])} {THINA} của tâm {called(N['cetaso ca līnattaṃ'])}", CLOSE[3]]

# =========================================================================== the fourfold exposition (^2-937 … ^2-U48)
SEG["2-937"] = [f"{qn(T['Cattāro āsavā'])} Ô nhiễm dục lạc, ô nhiễm hiện hữu, ô nhiễm quan điểm, ô nhiễm vô minh."]
SEG["2-U32"] = [f"{q(N['kāmāsavo'])} {KAMA8} {called(N['kāmāsavo'])}"]
SEG["2-U33"] = [f"{q(N['bhavāsavo'])} {BHAVA_S} {called(N['bhavāsavo'])}"]
SEG["2-U34"] = [f"{q(N['diṭṭhāsavo'])} {VIEWS10}. {cap(DITTHI_S)} {called(N['diṭṭhāsavo'])} Mọi quan điểm sai lầm đều "
                f"là {N['diṭṭhāsavo']}."]
pi1("Mọi quan điểm sai lầm đều là ô nhiễm quan điểm.")
SEG["2-U35"] = [f"{q(N['avijjāsavo'])} {TRUTHS}. {cap(SUCH)} {AVIJJA_TAIL} {called(N['avijjāsavo'])} "
                f"{this_is(T['Cattāro āsavā'], False)}"]
SEG["2-938"] = [f"Ở đây, bốn nút thắt… bốn dòng lũ… bốn ách… bốn sự bám víu là những gì? {cap(N['kāmupādānaṃ'])}, "
                f"{N['diṭṭhupādānaṃ']}, {N['sīlabbatupādānaṃ']}, {N['attavādupādānaṃ']}."]
SEG["2-U36"] = [f"{q(N['kāmupādānaṃ'])} {KAMA_S} {called(N['kāmupādānaṃ'])}"]
SEG["2-U37"] = [f"{q(N['diṭṭhupādānaṃ'])} {NIHIL_S}. {cap(DITTHI_S)} {called(N['diṭṭhupādānaṃ'])} "
                + pi1("Ngoại trừ sự bám víu vào giới hạnh và nghi thức, và sự bám víu vào học thuyết về tự ngã, mọi "
                      "quan điểm sai lầm đều là sự bám víu vào quan điểm.")]
SEG["2-U38"] = [f"{q(N['sīlabbatupādānaṃ'])} {SILABBATA}. {cap(DITTHI_S)} {called(N['sīlabbatupādānaṃ'])}"]
SEG["2-U39"] = [f"{q(N['attavādupādānaṃ'])} {SAKKAYA} {called(N['attavādupādānaṃ'])} "
                "Đây là bốn sự bám víu."]
_ARISE = "mà khao khát của vị tỳ-khưu, khi sinh khởi, thì sinh khởi"
SEG["2-939"] = [f"{qn(T['Cattāro taṇhuppādā'])} Vì y phục {_ARISE}; vì đồ ăn khất thực {_ARISE}; vì chỗ ở {_ARISE}; vì "
                f"sự hiện hữu này hay sự hiện hữu khác {_ARISE} {this_is(T['Cattāro taṇhuppādā'])}"]
SEG["2-U40"] = [f"{qn(T['Cattāri agatigamanāni'])} Đi theo con đường sai trái vì ưa thích, đi theo con đường sai trái vì "
                "sân hận, đi theo con đường sai trái vì si mê, đi theo con đường sai trái vì sợ hãi. "
                f"{cap(SUCH)} con đường sai trái, sự đi theo con đường sai trái, sự đi theo ý thích, sự đi theo phe "
                f"phái, sự đi theo như nước chảy {this_is(T['Cattāri agatigamanāni'])}"]
misfit("chandagamanaṃ / vaggagamanaṃ / vārigamanaṃ (^2-U40): no entries; «sự đi theo ý thích / phe phái / như nước "
       "chảy»")
_VIP = "sự đảo ngược của tri giác, sự đảo ngược của tâm, sự đảo ngược của quan điểm rằng"
SEG["2-U41"] = [f"{qn(T['Cattāro vipariyāsā'])} {cap(_VIP)} “thường còn” đối với điều vô thường; {_VIP} “hạnh phúc” "
                f"đối với điều khổ đau; {_VIP} “tự ngã” đối với điều không phải tự ngã; {_VIP} “đẹp” đối với điều không "
                f"đẹp {this_is(T['Cattāro vipariyāsā'])}"]
_SAY_YES = ("việc nói là đã thấy đối với điều chưa thấy, việc nói là đã nghe đối với điều chưa nghe, việc nói là đã "
            "cảm nhận đối với điều chưa cảm nhận, việc nói là đã nhận biết đối với điều chưa nhận biết")
_SAY_NO = ("việc nói là chưa thấy đối với điều đã thấy, việc nói là chưa nghe đối với điều đã nghe, việc nói là chưa "
           "cảm nhận đối với điều đã cảm nhận, việc nói là chưa nhận biết đối với điều đã nhận biết")
SEG["2-U42"] = [f"{qn(T['Cattāro anariyavohārā'])} {cap(_SAY_YES)} {this_is(T['Cattāro anariyavohārā'])}"]
SEG["2-U43"] = [f"{qn(T['Aparepi cattāro anariyavohārā'])} {cap(_SAY_NO)} {this_is(T['Cattāro anariyavohārā'])}"]
SEG["2-U44"] = [f"{qn(T['Cattāri duccaritāni'])} {cap(KILL)}, {STEAL}, {SEX}, {LIE} "
                f"{this_is(T['Cattāri duccaritāni'])}"]
SEG["2-U45"] = [f"{qn(T['Aparānipi cattāri duccaritāni'])} {cap(SPEECH4)} {this_is(T['Cattāri duccaritāni'])}"]


def fears(xs):
    return ", ".join(f"nỗi sợ hãi về {x}" for x in xs)


SEG["2-U46"] = [f"{qn(T['Cattāri bhayāni'])} {cap(fears(['sự sinh', 'sự lão hóa', 'bệnh', 'sự chết']))} "
                f"{this_is(T['Cattāri bhayāni'])}"]
_OTHER4 = qn(T['Aparānipi cattāri bhayāni'])
SEG["2-U47"] = [
    f"{_OTHER4} {cap(fears(['vua chúa', 'trộm cướp', 'lửa', 'nước']))} {this_is(T['Cattāri bhayāni'])}",
    f"{_OTHER4} Nỗi sợ hãi về sóng, nỗi sợ hãi về cá sấu [khác chính tả (?): kumbhīrabhayaṃ, kumbhīḷabhayaṃ (kumbha + "
    f"īra + a = bhaya)], nỗi sợ hãi về xoáy nước, nỗi sợ hãi về cá dữ {this_is(T['Cattāri bhayāni'])}",
    f"{_OTHER4} {cap(fears(['sự tự trách', 'sự bị người khác chỉ trích', 'hình phạt', 'cõi xấu']))} "
    f"{this_is(T['Cattāri bhayāni'])}"]
_V4 = "quan điểm khởi lên " + TRUE_FIRM + " rằng"
_SD = "Sự dễ chịu và sự khó chịu"
SEG["2-U48"] = [f"{qn(T['Catasso diṭṭhiyo'])} {cap(_V4)} “{_SD} do chính mình tạo ra”; {_V4} “{_SD} do người khác "
                f"tạo ra”; {_V4} “{_SD} vừa do chính mình tạo ra vừa do người khác tạo ra”; {_V4} “{_SD} không do "
                "chính mình tạo ra, không do người khác tạo ra, mà sinh khởi một cách ngẫu nhiên” "
                f"{this_is(T['Catasso diṭṭhiyo'])}", CLOSE[4]]

# =========================================================================== the fivefold exposition (^2-940 … ^2-943)
SEG["2-940"] = [f"{qn(T['Pañcorambhāgiyāni saṃyojanāni'])} Quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về "
                f"giới hạnh và nghi thức, ý muốn dục lạc, ác ý {this_is(T['Pañcorambhāgiyāni saṃyojanāni'])}"]
SEG["2-U49"] = [f"{qn(T['Pañcuddhambhāgiyāni saṃyojanāni'])} Sự tham đắm cõi hình sắc, sự tham đắm cõi không hình "
                f"sắc, sự kiêu mạn, sự xao động, vô minh {this_is(T['Pañcuddhambhāgiyāni saṃyojanāni'])}"]
SEG["2-U50"] = [f"{qn(T['Pañca macchariyāni'])} {cap(MACCH5.split(' – ', 1)[1])} {this_is(T['Pañca macchariyāni'])}"]
_FIVE = ["tham đắm", "sân hận", "si mê", "kiêu mạn", "quan điểm"]
SEG["2-U51"] = [f"{qn(T['Pañca saṅgā'])} {cap(', '.join(f'sự dính mắc vào {x}' for x in _FIVE))} "
                f"{this_is(T['Pañca saṅgā'])}"]
SEG["2-U52"] = [f"{qn(T['Pañca sallā'])} {cap(', '.join(f'mũi tên {x}' for x in _FIVE))} {this_is(T['Pañca sallā'])}"]
_DOUBT5 = "nghi ngờ, hoài nghi, không quyết định, không có lòng tin trong sáng về"
SEG["2-941"] = [f"{qn(T['Pañca cetokhilā'])} {cap(_DOUBT5)} Bậc Đạo Sư; {_DOUBT5} Giáo Pháp; {_DOUBT5} Tăng đoàn; "
                f"{_DOUBT5} sự tu học; nổi giận, không hài lòng, có tâm bị tổn thương, trở nên chai cứng đối với các "
                f"bạn đồng tu {this_is(T['Pañca cetokhilā'])}"]
_NOTFREE = "chưa lìa tham đắm, chưa lìa ý muốn, chưa lìa sự yêu thích, chưa lìa sự khát khao, chưa lìa sự nóng bỏng, "\
    "chưa lìa khao khát"
SEG["2-U53"] = [f"{qn(T['Pañca cetaso vinibandhā'])} Đối với các dục lạc, {_NOTFREE}; đối với thân, chưa lìa tham "
                "đắm… đối với hình sắc, chưa lìa tham đắm… sau khi ăn no căng bụng như mình cần, sống chuyên tâm vào "
                "thú vui nằm, thú vui trở mình, thú vui ngủ; sống đời tu hành trong sạch với ước nguyện về một cõi chư "
                "thiên nào đó – “Nhờ giới hạnh này, hoặc nghi thức, hoặc khổ hạnh, hoặc đời tu hành trong sạch, tôi "
                "sẽ trở thành một vị trời, hoặc một vị nào đó trong chư thiên” "
                f"{this_is(T['Pañca cetaso vinibandhā'])}"]
SEG["2-U54"] = [f"{qn(T['Pañca nīvaraṇāni'])} {cap(NIVARANA5)} {this_is(T['Pañca nīvaraṇāni'])}"]
_DEPRIVED = "bị tước đoạt mạng sống"
SEG["2-U55"] = [f"{qn(T['Pañca kammāni ānantarikāni'])} Mẹ {_DEPRIVED}, cha {_DEPRIVED}, bậc A-la-hán {_DEPRIVED}, "
                "máu của Như Lai bị làm cho chảy với tâm độc ác, Tăng đoàn bị chia rẽ "
                f"{this_is(T['Pañca kammāni ānantarikāni'])}"]
_SOME = "một số người tuyên bố rằng"
SEG["2-U56"] = [f"{qn(T['Pañca diṭṭhiyo'])} {cap(_SOME)} “Tự ngã có tri giác, không bệnh tật sau khi chết”; {_SOME} "
                f"“Tự ngã không có tri giác, không bệnh tật sau khi chết”; {_SOME} “Tự ngã không phải có tri giác cũng "
                "không phải không có tri giác, không bệnh tật sau khi chết”; hoặc họ trình bày sự đoạn diệt, sự hủy "
                "diệt, sự không còn hiện hữu của chúng sinh đang hiện hữu; hoặc một số người tuyên bố Niết-bàn ngay "
                f"trong đời này {this_is(T['Pañca diṭṭhiyo'])}"]
SEG["2-942"] = [f"{qn(T['Pañca verā'])} {cap(KILL)}, {STEAL}, {SEX}, {LIE}, {DRINK} {this_is(T['Pañca verā'])}"]
SEG["2-U57"] = [f"{qn(T['Pañca byasanā'])} Sự tổn hại về người thân, sự tổn hại về tài sản, sự tổn hại về bệnh tật, sự "
                f"tổn hại về giới hạnh, sự tổn hại về quan điểm {this_is(T['Pañca byasanā'])}"]
SEG["2-U58"] = [f"{qn(T['Pañca akkhantiyā ādīnavā'])} Không được nhiều người yêu quý, không đáng ưa thích, có nhiều "
                "thù địch, có nhiều lỗi lầm, chết trong mê muội, khi thân tan rã, sau khi chết thì tái sinh vào cõi "
                f"khổ, cõi xấu, nơi đọa lạc, địa ngục {this_is(T['Pañca akkhantiyā ādīnavā'])}"]
pi2("khi thân tan rã, sau khi chết")
SEG["2-U59"] = [f"{qn(T['Pañca bhayāni'])} Nỗi sợ hãi về sinh kế, nỗi sợ hãi về tiếng xấu, nỗi sợ hãi vì rụt rè trước "
                f"hội chúng, nỗi sợ hãi về sự chết, nỗi sợ hãi về cõi xấu {this_is(T['Pañca bhayāni'])}"]
_NIB = "Niết-bàn tối thượng ngay trong đời này"
_REACH = f"thì chỉ đến chừng ấy, thưa ngài, tự ngã này đạt đến {_NIB}”"
_DECL = f"Như vậy, một số người trình bày {_NIB} của chúng sinh đang hiện hữu."
_EXISTS = "“Thưa ngài, tự ngã mà ngài nói đó quả có tồn tại"
_NOT_YET = f"Nhưng, thưa ngài, tự ngã này không phải chỉ đến chừng ấy là đạt đến {_NIB}. Vì sao vậy?"
_GROSS = "nên điều đó được xem là ở dạng thô"


def nib(k, why, jhana):
    sep = ", tôi" if k == "Kha" else ". Tôi"
    return lab(k, f"{ANOTHER} – {_EXISTS}{sep} không nói rằng nó không tồn tại. {_NOT_YET} {why} Thưa ngài, khi tự ngã "
                  f"này {jhana}, {_REACH}. {_DECL}")


SEG["2-943"] = [
    f"{qn(T['Pañca diṭṭhadhammanibbānavādā'])}",
    lab("Ka", f"{SAMANA} [khác chính tả (Syā.): evaṃdiṭṭhi] – “Thưa ngài, khi tự ngã này được thỏa mãn, được đầy đủ "
              f"với năm đối tượng của dục lạc và tận hưởng chúng, {_REACH}. {_DECL}"),
    nib("Kha", "Thưa ngài, các dục lạc là vô thường, khổ đau, có bản chất biến đổi. Do chúng biến đổi và trở nên khác "
               "đi mà sinh khởi sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng.",
        "hoàn toàn tách khỏi các dục lạc… chứng nhập và an trú tầng thiền thứ nhất"),
    nib("Ga", f"Bởi vì ở đó có sự hướng tâm, có sự duy trì tâm, {_GROSS}.",
        "nhờ sự hướng tâm và sự duy trì tâm lắng xuống… chứng nhập và an trú tầng thiền thứ hai"),
    nib("Gha", f"Bởi vì ở đó có sự hân hoan, có sự phấn khích của tâm, {_GROSS}.",
        "nhờ sự hân hoan phai nhạt… chứng nhập và an trú tầng thiền thứ ba"),
    nib("Ṅa", f"Bởi vì ở đó có sự chú hướng của tâm vào hạnh phúc và sự hân hoan, {_GROSS}.",
        "nhờ dứt bỏ sự dễ chịu… chứng nhập và an trú tầng thiền thứ tư")
    + f" {this_is(T['Pañca diṭṭhadhammanibbānavādā'], False)}",
    CLOSE[5]]
pi2("chứng nhập và an trú tầng thiền thứ tư")
slip("^2-943 (Ka) «evaṃdiṭṭhi [evaṃdiṭṭhi (syā.)]»: the variant repeats the reading; kept as a bracket")
slip("^2-943 (Ṅa) «sukhapīti cetaso ābhogo» (the sutta reading is «sukhamiti»): rendered as written («sự chú hướng "
     "của tâm vào hạnh phúc và sự hân hoan»)")

# =========================================================================== the sixfold exposition (^2-944 … ^2-948)
SEG["2-944"] = [f"{qn(T['Cha vivādamūlāni'])} Sự giận dữ, sự gièm pha, sự ganh tị, sự gian xảo, sự có ước muốn xấu "
                f"xa, sự hiểu sai lệch về quan điểm của mình {this_is(T['Cha vivādamūlāni'])}"]


def six(adj, what, closing):
    """Manāpiyesu rūpesu X, manāpiyesu saddesu…pe… manāpiyesu dhammesu X – closing"""
    mid = "… ".join(f"đối với những {s} {adj}" for s, _ in SENSES6[1:5])
    return (f"Đối với những {SENSES6[0][0]} {adj}, có {what}; {mid}… đối với những {SENSES6[5][0]} {adj}, có "
            f"{what} {closing}")


SEG["2-U60"] = [f"{qn(T['Cha chandarāgā'])} Các sự tham đắm do ý muốn là những hiện tượng gắn với đời sống thế tục. "
                + six("đáng ưa thích", f"{RAGA3} gắn với đời sống thế tục", this_is(T['Cha chandarāgā']))]
SEG["2-U61"] = [f"{qn(T['Cha virodhavatthūni'])} "
                + six("không đáng ưa thích", "sự oán giận của tâm, sự phẫn uất, sự hung dữ, sự nói năng cộc cằn, sự "
                      "không hài lòng của tâm", this_is(T['Cha virodhavatthūni']))]
SEG["2-U62"] = [f"{qn(T['Cha taṇhākāyā'])} {cap(', '.join('khao khát ' + s for s, _ in SENSES6))} "
                f"{this_is(T['Cha taṇhākāyā'])}"]
pi1("khao khát đối tượng của ý")
_AG = "sống thiếu kính trọng, không vâng lời đối với"
SEG["2-945"] = [f"{qn(T['Cha agāravā'])} {cap(_AG)} Bậc Đạo Sư; {_AG} Giáo Pháp; {_AG} Tăng đoàn; {_AG} sự tu học; "
                f"{_AG} sự không buông thả; {_AG} sự niềm nở tiếp đón {this_is(T['Cha agāravā'])}"]
_DELIGHT4 = "sự ưa thích công việc, sự ưa thích nói chuyện, sự ưa thích ngủ nghỉ, sự ưa thích tụ tập"
SEG["2-U63"] = [f"{qn(T['Cha parihāniyā dhammā'])} {cap(_DELIGHT4)}, sự ưa thích giao du, sự ưa thích suy diễn lan man "
                f"{this_is(T['Cha parihāniyā dhammā'])}"]
SEG["2-946"] = [f"{qn(T['Aparepi cha parihāniyā dhammā'])} {cap(_DELIGHT4)}, {N['dovacassatā']}, {N['pāpamittatā']} "
                f"{this_is(T['Cha parihāniyā dhammā'])}"]
misfit("saṅgaṇikārāmatā / saṅgaṇikārāmo (^2-851, ^2-U63, ^2-946): no entry; «sự ưa thích tụ tập» / «ưa thích tụ tập»")


def linger(gives, key):
    mid = "… ".join(f"khi {a}" for a, _ in SEE6[1:5])
    return (f"{qn(T[key])} Khi {SEE6[0][0]}, người ta lưu tâm đến {SEE6[0][1]} làm khởi lên {gives}; {mid}… khi "
            f"{SEE6[5][0]}, người ta lưu tâm đến {SEE6[5][1]} làm khởi lên {gives} {this_is(T[key])}")


SEG["2-U64"] = [linger("niềm vui", "Cha somanassupavicārā")]
SEG["2-U65"] = [linger("nỗi buồn", "Cha domanassupavicārā")]
SEG["2-U66"] = [linger("sự bình thản", "Cha upekkhupavicārā")]
SEG["2-947"] = [f"{qn(T['Cha gehasitāni somanassāni'])} "
                + six("đáng ưa thích", f"{JOY4} gắn với đời sống thế tục, {JOY4B}",
                      this_is(T['Cha gehasitāni somanassāni']))]
SEG["2-U67"] = [f"{qn(T['Cha gehasitāni domanassāni'])} "
                + six("không đáng ưa thích", f"{GRIEF4} gắn với đời sống thế tục, {GRIEF4B}",
                      this_is(T['Cha gehasitāni domanassāni']))]
SEG["2-U68"] = [f"{qn(T['Cha gehasitā upekkhā'])} "
                + six("làm khởi lên sự bình thản", f"{NEUTRAL3} gắn với đời sống thế tục, {NEUTRAL3B}",
                      this_is(T['Cha gehasitā upekkhā']))]
_V6 = f"khởi lên nơi người ấy {TRUE_FIRM}"
SEG["2-948"] = [f"{qn(T['Cha diṭṭhiyo'])} Quan điểm “Tôi có tự ngã” {_V6}; hoặc quan điểm “Tôi không có tự ngã” {_V6}; "
                f"hoặc quan điểm “Tôi nhận biết tự ngã bằng tự ngã” {_V6}; hoặc quan điểm “Tôi nhận biết cái không "
                f"phải tự ngã bằng tự ngã” {_V6}; hoặc quan điểm “Tôi nhận biết tự ngã bằng cái không phải tự ngã” "
                f"{_V6}; hoặc người ấy có quan điểm như vầy – “Tự ngã này của tôi là cái nói, cái cảm nhận, ở nơi này "
                "nơi kia, trong thời gian dài, trải nghiệm quả của các nghiệp tốt đẹp và xấu ác. Không phải nó đã sinh ra, "
                "không phải trước đây không có; không phải nó đã sinh ra, không phải sẽ không có; nó thường còn, bền "
                f"vững, trường tồn, có bản chất không biến đổi”, hoặc quan điểm ấy sinh khởi nơi người ấy {TRUE_FIRM}. "
                f"{this_is(T['Cha diṭṭhiyo'], False)}", CLOSE[6]]

# =========================================================================== the sevenfold exposition (^2-949 … ^2-951)
SEG["2-949"] = [f"{qn(T['Sattānusayā'])} {cap(ANUSAYA7)} {this_is(T['Sattānusayā'])}"]
_FET7 = FETTER10.replace("xiềng xích hiểu sai lệch về giới hạnh và nghi thức, ", "").replace(
    "xiềng xích ganh tị, xiềng xích keo kiệt, ", "")
SEG["2-U69"] = [f"{qn(T['Satta saṃyojanāni'])} {cap(_FET7)} {this_is(T['Satta saṃyojanāni'])}"]
_OBS = ["tham đắm dục lạc", "ác cảm", "kiêu mạn", "quan điểm", "hoài nghi", "tham đắm hiện hữu", "vô minh"]
SEG["2-U70"] = [f"{qn(T['Satta pariyuṭṭhānāni'])} {cap(', '.join(f'sự ám ảnh của {x}' for x in _OBS))} "
                f"{this_is(T['Satta pariyuṭṭhānāni'])}"]
pi2("sự ám ảnh của vô minh")
SEG["2-950"] = [f"{qn(T['Satta asaddhammā'])} Là người không có niềm tin, là người không biết hổ thẹn, là người không "
                "biết ghê sợ tội lỗi, là người ít học hỏi, là người lười biếng, là người mất tỉnh thức, là người kém "
                f"trí tuệ {this_is(T['Satta asaddhammā'])}"]
SEG["2-U71"] = [f"{qn(T['Satta duccaritāni'])} {cap(KILL)}, {STEAL}, {SEX}, {SPEECH4} "
                f"{this_is(T['Satta duccaritāni'])}"]
SEG["2-U72"] = [f"{qn(T['Satta mānā'])} {cap(', '.join(ONE[60:67]))} {this_is(T['Satta mānā'])}"]
_ANNIH = "Như vậy, một số người trình bày sự đoạn diệt, sự hủy diệt, sự không còn hiện hữu của chúng sinh đang hiện hữu."
_BREAK = "lúc thân tan rã, bị đoạn diệt, bị hủy diệt, không còn tồn tại sau khi chết"
_ANNIH_END = "thì chỉ đến chừng ấy, thưa ngài, tự ngã này hoàn toàn bị đoạn diệt”"


def annih(k, other, bho=True):
    """(Kha)…(Cha) tamañño evamāha – "atthi kho, bho, eso attā … sammā samucchinno hotī"ti. Ittheke …"""
    head = _EXISTS if bho else "“Tự ngã mà ngài nói đó quả có tồn tại"
    other = other.replace("“", "‘").replace("”", "’")       # nested inside the speech
    return lab(k, f"{ANOTHER} – {head}. Tôi không nói rằng ‘Nó không tồn tại’. Nhưng, thưa ngài, tự ngã này không phải "
                  f"chỉ đến chừng ấy là hoàn toàn bị đoạn diệt. Thưa ngài, còn có một tự ngã khác, {other}. Ngài không "
                  "biết, không thấy nó. Tôi biết, thấy nó. Thưa ngài, khi tự ngã ấy, "
                  f"{_BREAK}, {_ANNIH_END}. {_ANNIH}")


_FORMLESS = "nhờ hoàn toàn vượt qua các tri giác về hình sắc, nhờ các tri giác về sự va chạm biến mất, nhờ không chú tâm "\
    "đến các tri giác về sự đa dạng, với ý nghĩ “Không gian là vô tận”, đạt đến lĩnh vực không gian vô tận"
pi2("nhờ hoàn toàn vượt qua các tri giác về hình sắc, nhờ các tri giác về sự va chạm biến mất, nhờ không chú tâm đến "
    "các tri giác về sự đa dạng, với ý nghĩ “Không gian là vô tận”")
SEG["2-951"] = [
    lab("Ka", f"{qn(T['Satta diṭṭhiyo'])} {SAMANA} – “Thưa ngài, khi tự ngã này có hình sắc, được tạo thành từ bốn "
              "yếu tố cơ bản [khác chính tả (Sī., Syā.): cātummahābhūtiko], do cha mẹ sinh ra, khi thân tan rã thì bị "
              f"đoạn diệt, bị hủy diệt, không còn tồn tại sau khi chết, {_ANNIH_END}. {_ANNIH}"),
    annih("Kha", "thuộc cõi trời, có hình sắc, thuộc cõi dục lạc, dùng thức ăn trong vai trò dưỡng chất"),
    annih("Ga", "thuộc cõi trời, có hình sắc, do ý tạo thành, đầy đủ mọi bộ phận lớn nhỏ, có các năng lực không khiếm "
                "khuyết"),
    annih("Gha", _FORMLESS),
    annih("Ṅa", "hoàn toàn vượt qua lĩnh vực không gian vô tận, với ý nghĩ “Thức là vô tận”, đạt đến lĩnh vực thức vô "
                "tận"),
    annih("Ca", "hoàn toàn vượt qua lĩnh vực thức vô tận, với ý nghĩ “Không có gì cả”, đạt đến lĩnh vực không có gì "
                "cả"),
    annih("Cha", "hoàn toàn vượt qua lĩnh vực không có gì cả, đạt đến lĩnh vực không phải tri giác cũng không phải "
                 "không tri giác", bho=False) + f" {this_is(T['Satta diṭṭhiyo'], False)}",
    CLOSE[7]]
pi2(S.FOOD)
slip("^2-951 (Cha) «atthi kho pana eso attā» (pana for «bho»): rendered as written, without «thưa ngài»")

# =========================================================================== the eightfold exposition (^2-952 … ^2-959)
SEG["2-952"] = [f"{qn(T['Aṭṭha kilesavatthūni'])} {cap(KILESA8)} {this_is(T['Aṭṭha kilesavatthūni'])}"]
_NOEFFORT = ("Vị ấy nằm nghỉ; không khởi động tinh tấn để đạt được điều chưa đạt được, để chứng đắc điều chưa chứng "
             "đắc, để chứng nghiệm điều chưa chứng nghiệm.")
_THINKS = "Vị ấy nghĩ như vầy –"
_LIE = "Vậy ta hãy nằm nghỉ”."
_ALMS = "đi khất thực ở làng hoặc thị trấn mà {x} đầy đủ thức ăn thô hoặc ngon như mình cần"


def lazy(k, n, case, thought, close=""):
    return lab(k, f"{case} {_THINKS} “{thought} {_LIE} {_NOEFFORT} Đây là chỗ dựa {ORD[n]} của sự lười biếng."
               + close)


SEG["2-953"] = [
    f"{qn(T['Aṭṭha kusītavatthūni'])}",
    lazy("Ka", 1, "Ở đây, vị tỳ-khưu có việc cần phải làm.", "Ta sẽ phải làm việc. Khi ta làm việc thì thân sẽ mệt "
         "mỏi."),
    lazy("Kha", 2, "Lại nữa, vị tỳ-khưu đã làm xong việc.", "Ta đã làm việc. Khi ta làm việc thì thân đã mệt mỏi."),
    lazy("Ga", 3, "Lại nữa, vị tỳ-khưu có đường cần phải đi.", "Ta sẽ phải đi đường. Khi ta đi đường thì thân sẽ mệt "
         "mỏi."),
    lazy("Gha", 4, "Lại nữa, vị tỳ-khưu đã đi đường xong.", "Ta đã đi đường. Khi ta đi đường thì thân đã mệt mỏi."),
    lazy("Ṅa", 5, f"Lại nữa, vị tỳ-khưu {_ALMS.format(x='không nhận được')}.",
         f"Ta {_ALMS.format(x='đã không nhận được')}. Thân ta mệt mỏi, không dễ vận dụng."),
    lazy("Ca", 6, f"Lại nữa, vị tỳ-khưu {_ALMS.format(x='nhận được')}.",
         f"Ta {_ALMS.format(x='đã nhận được')}. Thân ta mệt mỏi, không dễ vận dụng, nặng nề như hạt đậu ngâm nước, "
         "ta nghĩ vậy."),
    lazy("Cha", 7, "Lại nữa, nơi vị tỳ-khưu có một chứng bệnh nhẹ đã sinh khởi.", "Chứng bệnh nhẹ này đã sinh khởi "
         "nơi ta. Có lý do "
         "chính đáng để nằm nghỉ."),
    lazy("Ja", 8, "Lại nữa, vị tỳ-khưu vừa khỏi bệnh [khác chính tả (Saddanībhi): gilānavuṭṭhito; "
         f"{AN} 6.16, nên tham khảo chú giải phụ của đoạn này], mới khỏi bệnh không lâu.",
         "Ta vừa khỏi bệnh, mới khỏi bệnh không lâu. Thân ta yếu ớt, không dễ vận dụng.",
         f" {this_is(T['Aṭṭha kusītavatthūni'], False)}")]
SEG["2-954"] = [f"{q(T['Aṭṭhasu lokadhammesu cittassa paṭighāto'])} Sự say đắm khi được lợi lộc, sự đối nghịch khi "
                "không được lợi lộc, sự say đắm khi được danh tiếng, sự đối nghịch khi mất danh tiếng, sự say đắm khi "
                "được khen ngợi, sự đối nghịch khi bị chê trách, sự say đắm khi được hạnh phúc, sự đối nghịch khi gặp "
                f"khổ đau – đây là {T['Aṭṭhasu lokadhammesu cittassa paṭighāto']} này."]
SEG["2-955"] = [f"{qn('tám cách nói không cao quý')} {cap(_SAY_YES)}, {_SAY_NO} "
                f"{this_is('tám cách nói không cao quý')}"]
SEG["2-956"] = [f"{qn(T['Aṭṭha micchattā'])} {cap(WRONG8)} {this_is(T['Aṭṭha micchattā'])}"]
_CHARGE = ("các tỳ-khưu buộc tội một tỳ-khưu về lỗi vi phạm. Vị tỳ-khưu ấy, khi bị các tỳ-khưu buộc tội về lỗi vi "
           "phạm{v},")
_AGAIN = "Lại nữa, " + _CHARGE.format(v="")


def fault(k, n, s, close=""):
    return lab(k, f"{s} Đây là lỗi {ORD[n]} của con người.{close}")


SEG["2-957"] = [
    f"{qn(T['Aṭṭha purisadosā'])} " + fault("Ka", 1, "Ở đây, " + _CHARGE.format(
        v=f" [khác chính tả (Sī., Syā.): codiyamāno; {AN} 8.14]") + " chối bỏ với lý do không nhớ: “Tôi không nhớ, "
        "tôi không nhớ”."),
    fault("Kha", 2, f"{_AGAIN} chống lại chính người buộc tội – “Lời nói của ông, kẻ ngu dốt, thiếu hiểu biết, thì có "
                    "ích gì! Ông mà cũng nghĩ là có thể nói tôi sao”!"),
    fault("Ga", 3, f"{_AGAIN} buộc tội ngược lại chính người buộc tội [dị bản (Syā.): codakasseva; {AN} 8.14] – "
                   "“Chính ông cũng đã phạm lỗi có tên như thế này. Trước hết ông hãy sửa lỗi đi”."),
    fault("Gha", 4, f"{_AGAIN} lảng tránh chuyện này sang chuyện khác, đưa câu chuyện ra ngoài, để lộ sự nổi nóng, sự "
                    "sân hận và sự bất mãn."),
    fault("Ṅa", 5, f"{_AGAIN} vừa vung tay vừa nói giữa Tăng đoàn."),
    fault("Ca", 6, f"{_AGAIN} không đếm xỉa đến Tăng đoàn, không đếm xỉa đến người buộc tội, vẫn mang lỗi [dị bản "
                   f"(Ka.): āpattikova; {AN} 8.14] mà bỏ đi đâu tùy ý."),
    fault("Cha", 7, f"{_AGAIN} nói “Tôi không phạm lỗi, cũng không phải không phạm lỗi”, rồi im lặng làm phiền Tăng "
                    "đoàn."),
    fault("Ja", 8, f"{_AGAIN} nói như vầy – “Này các tôn giả, sao các vị quá bận tâm về tôi như vậy. Bây giờ tôi sẽ "
                   "từ bỏ sự tu học và quay về đời sống thấp kém”. Sau khi từ bỏ sự tu học, quay về đời sống thấp kém, "
                   "vị ấy nói như vầy – “Bây giờ thì các tôn giả hãy hài lòng đi”.",
          f" {this_is(T['Aṭṭha purisadosā'], False)}")]
slip("^2-957 (Ja) «kiṃ nu kho tumhe āyasmanto atibāḷhaṃ mayi byāvaṭā.»: question closed with «.», kept")
_AFTER = "không bệnh tật sau khi chết"
_DECL_NS = "họ trình bày rằng nó {x}"
_SELF8 = [("có hình sắc", "Tự ngã có hình sắc"), ("không có hình sắc", "tự ngã không có hình sắc"),
          ("vừa có hình sắc vừa không có hình sắc", "tự ngã vừa có hình sắc vừa không có hình sắc"),
          ("không phải có hình sắc cũng không phải không có hình sắc",
           "tự ngã không phải có hình sắc cũng không phải không có hình sắc"),
          ("hữu hạn", "Tự ngã là hữu hạn"), ("vô hạn", "Tự ngã là vô hạn"),
          ("vừa hữu hạn vừa vô hạn", "Tự ngã vừa hữu hạn vừa vô hạn"),
          ("không phải hữu hạn cũng không phải vô hạn", "Tự ngã không phải hữu hạn cũng không phải vô hạn")]
_NS = "không có tri giác"
SEG["2-958"] = [f"{qn(T['Aṭṭha asaññīvādā'])} “{_SELF8[0][1]}, {_AFTER}” – {_DECL_NS.format(x=_NS)}; "
                + "… ".join(s for _, s in _SELF8[1:4]) + "… "
                + "; ".join(f"“{s}, {_AFTER}” – {_DECL_NS.format(x=_NS)}" for _, s in _SELF8[4:])
                + f". {this_is(T['Aṭṭha asaññīvādā'], False)}"]
misfit("^2-958 the abbreviated items «arūpī attā…pe… rūpī ca arūpī ca…pe… nevarūpīnārūpī…pe…» stay unquoted, as in "
       "the Pāli")
_NNS = "không phải có tri giác cũng không phải không có tri giác"
SEG["2-959"] = ["; ".join(
    f"“{cap(s)}, {_AFTER}” – {_DECL_NS.format(x=_NNS)}" for _, s in _SELF8).join(
    [f"{qn(T['Aṭṭha nevasaññīnāsaññīvādā'])} ", f". {this_is(T['Aṭṭha nevasaññīnāsaññīvādā'], False)}"]),
    CLOSE[8]]

# =========================================================================== the ninefold exposition (^2-960 … ^2-965)
_AG_ = "sự oán giận khởi lên với ý nghĩ"
_HARM9 = (f"{cap(_AG_)} “Người ấy đã gây hại cho tôi”; {_AG_} “Người ấy đang gây hại cho tôi”; {_AG_} “Người ấy sẽ gây "
          f"hại cho tôi”; {_AG_} “Người ấy đã gây hại cho người yêu quý, ưa thích của tôi”… đang gây hại… sẽ gây hại; "
          f"{_AG_} người ấy đã làm lợi cho người không yêu quý, không ưa thích của tôi… đang làm lợi… sẽ làm lợi")
SEG["2-960"] = [f"{qn(T['Nava āghātavatthūni'])} {_HARM9}. {this_is(T['Nava āghātavatthūni'], False)}"]
SEG["2-961"] = [f"{qn(T['Nava purisamalāni'])} Sự giận dữ, sự gièm pha, sự ganh tị, sự keo kiệt, sự xảo trá, sự gian "
                f"xảo, việc nói dối, sự có ước muốn xấu xa, quan điểm sai lầm {this_is(T['Nava purisamalāni'])}"]
SEG["2-962"] = [f"{qn(T['Navavidhā mānā'])} {cap(', '.join(ONE[51:60]))} {this_is(T['Navavidhā mānā'])}"]
_CHAIN = [("khao khát", "sự tìm kiếm khắp nơi"), ("sự tìm kiếm khắp nơi", "sự đạt được"),
          ("sự đạt được", "sự phán định"), ("sự phán định", "sự tham đắm do ý muốn"),
          ("sự tham đắm do ý muốn", "sự đắm chìm"), ("sự đắm chìm", "sự chiếm hữu"), ("sự chiếm hữu", "sự keo kiệt"),
          ("sự keo kiệt", "sự canh giữ")]
SEG["2-963"] = [f"{qn(T['Nava taṇhāmūlakā dhammā'])} "
                + cap(", ".join(f"dựa vào {a} mà có {b}" for a, b in _CHAIN))
                + ", vì sự canh giữ mà nhiều hiện tượng bất thiện xấu ác phát sinh: cầm gậy, cầm dao, cãi cọ, xung "
                  "đột, tranh cãi, gọi nhau mày tao, nói lời đâm thọc, việc nói dối "
                + this_is(T['Nava taṇhāmūlakā dhammā'])]
_9 = ["Tôi là", "Chính tôi là", "Tôi là cái này", "Tôi sẽ là", "Tôi sẽ có hình sắc", "Tôi sẽ không có hình sắc",
      "Tôi sẽ có tri giác", "Tôi sẽ không có tri giác",
      "Tôi sẽ không phải có tri giác cũng không phải không có tri giác"]


def nine(what, key, head=None):
    return (f"{head or qn(T[key])} " + cap(", ".join(f"“{x}” là {what}" for x in _9))
            + f" {this_is(T[key])}")


SEG["2-964"] = [nine("một sự dao động", "Nava iñjitāni")]
SEG["2-965"] = [nine("một điều được tạo tác", "Nava maññitādīni",
                     head="Ở đây, chín sự tưởng tượng… chín sự rung động… chín sự suy diễn lan man… chín điều được tạo "
                          "tác là những gì?").replace(this_is(T["Nava maññitādīni"]), "– đây là chín điều được tạo "
                                                                                       "tác."), CLOSE[9]]

# =========================================================================== the tenfold exposition (^2-966 … ^2-972)
SEG["2-966"] = [f"{qn(T['Dasa kilesavatthūni'])} {cap(KILESA10)} {this_is(T['Dasa kilesavatthūni'])}"]
SEG["2-967"] = [f"{qn(T['Dasa āghātavatthūni'])} {_HARM9}; hoặc sự oán giận khởi lên một cách vô cớ "
                f"{this_is(T['Dasa āghātavatthūni'])}"]
SEG["2-968"] = [f"{qn(T['Dasa akusalakammapathā'])} {cap(KILL)}, {STEAL}, {SEX}, {SPEECH4}, {MIND3} "
                f"{this_is(T['Dasa akusalakammapathā'])}"]
SEG["2-969"] = [f"{qn(T['Dasa saṃyojanāni'])} {cap(FETTER10)} {this_is(T['Dasa saṃyojanāni'])}"]
SEG["2-970"] = [f"{qn(T['Dasa micchattā'])} {cap(WRONG8)}, hiểu biết sai lầm, giải thoát sai lầm "
                f"{this_is(T['Dasa micchattā'])}"]
SEG["2-971"] = [f"{q(T['Dasavatthukā micchādiṭṭhi'])} {NIHIL} [dị bản (Ka.): samaggatā], {NIHIL_END} "
                f"{this_is(T['Dasavatthukā micchādiṭṭhi'])}"]
pi1("đã đi đúng đắn [dị bản (Ka.): samaggatā], thực hành đúng đắn")
SEG["2-972"] = [f"{q(T['Dasavatthukā antaggāhikā diṭṭhi'])} {VIEWS10} {this_is(T['Dasavatthukā antaggāhikā diṭṭhi'])}",
                CLOSE[10]]

# =========================================================================== the currents of craving (^2-973 … ^2-977)
TH = {  # the eighteen thoughts
    "asmi": "Tôi là", "itthasmi": "Tôi là như thế này", "evasmi": "Tôi giống như vậy", "aññathāsmi": "Tôi khác đi",
    "bhavissaṃ": "Tôi sẽ là", "itthaṃ bhavissaṃ": "Tôi sẽ là như thế này", "evaṃ bhavissaṃ": "Tôi sẽ giống như vậy",
    "aññathā bhavissaṃ": "Tôi sẽ khác đi", "asasmi": "Tôi thường còn", "sātasmi": "Tôi đoạn diệt",
    "siyaṃ": "Tôi có thể là", "itthaṃ siyaṃ": "Tôi có thể là như thế này", "evaṃ siyaṃ": "Tôi có thể giống như vậy",
    "aññathā siyaṃ": "Tôi có thể khác đi", "apāhaṃ siyaṃ": "Ước gì tôi cũng là",
    "apāhaṃ itthaṃ siyaṃ": "Ước gì tôi cũng là như thế này", "apāhaṃ evaṃ siyaṃ": "Ước gì tôi cũng giống như vậy",
    "apāhaṃ aññathā siyaṃ": "Ước gì tôi cũng khác đi"}
ORDER18 = list(TH)
misfit("the eighteen currents (^2-973 …): only asasmīti «Tôi thường còn», sātasmīti «Tôi đoạn diệt», aññathāsmīti «Tôi "
       "khác đi» have entries; the rest built alike: asmi «Tôi là» (as asmimāno), itthaṃ «như thế này», evaṃ «giống như "
       "vậy», bhavissaṃ «Tôi sẽ là», siyaṃ «Tôi có thể là», apāhaṃ siyaṃ «Ước gì tôi cũng là»; iminā «do điều này»; "
       "avakāriṃ «tách riêng» (sibling of anavakāriṃ «không tách riêng»)")
KIND13 = ["người thuộc giai cấp quý tộc", "bà-la-môn", "người thuộc giai cấp thương nhân",
          "người thuộc giai cấp lao động", "người tại gia", "người xuất gia", "vị trời", "con người",
          "người có hình sắc", "người không có hình sắc", "người có tri giác", "người không có tri giác",
          "người không phải có tri giác cũng không phải không có tri giác"]
VERB = {"asmi": "tôi là", "bhavissaṃ": "tôi sẽ là", "siyaṃ": "tôi có thể là", "apāhaṃ": "ước gì tôi cũng là"}
NEG = {"asmi": "tôi không là", "bhavissaṃ": "tôi sẽ không là", "siyaṃ": "tôi có thể không là",
       "apāhaṃ": "ước gì tôi cũng không là"}
BY = "do điều này, "                                                      # iminā


def thought(k, ext=False):
    t = TH[k]
    return f"Do điều này, {low(t)}" if ext else t


def having(k, ext=False):
    return f"có ý nghĩ “{thought(k, ext)}”"


def how(k, ext=False):
    return f"Thế nào là {having(k, ext)}?"


def thus(k, ext=False):
    return f"như vậy là {having(k, ext)}"


_FIVE_AGG = "đối với vật chất… cảm giác… tri giác… các sự tạo tác… thức"


def separate(ext, var=""):
    return (f"Tách riêng{var} một hiện tượng nào đó" if ext
            else f"Không tách riêng{var} bất cứ hiện tượng nào")


def root_line(num, k, ks3, ext=False, var=""):
    """(n) Kathañca X hoti? Kañci dhammaṃ anavakāriṃ karitvā rūpaṃ… viññāṇaṃ Xti chandaṃ … Tasmiṃ sati …"""
    t = thought(k, ext)
    pre = f"({num}) " if num else ""
    alts = ", hoặc ".join(f"“{thought(x, ext)}”" for x in ks3)
    return (f"{pre}{how(k, ext)} {separate(ext, var)}, {_FIVE_AGG}, người ta có được ý muốn “{t}”, có được sự kiêu mạn "
            f"“{t}”, có được quan điểm “{t}”. Khi có điều đó thì có những sự suy diễn lan man này – {alts}.")


def kinds_line(num, k, tense, ext=False, short=False):
    """(n) Kathañca itthaṃ X hoti? Khattiyo X vā, … – evaṃ itthaṃ X hoti."""
    def one(x):
        v = VERB[tense]
        s = f"{BY}{v} {x}" if ext else f"{v} {x}"
        return f"“{cap(s)}”"
    if short:  # (6) iminā: khattiyo…pe… arūpī, saññī, asaññī, nevasaññīnāsaññī
        lst = one(KIND13[0]) + "… hoặc " + ", hoặc ".join(one(x) for x in KIND13[9:])
    else:
        lst = ", hoặc ".join(one(x) for x in KIND13)
    return f"({num}) {how(k, ext)} {lst} – {thus(k, ext)}."


def compare_line(num, k, tense, neg, ext=False, short=False, close_k=None):
    """(n) Kathañca evaṃ X hoti? Parapuggalaṃ upanidhāya yathā so khattiyo [iminā] tathāhaṃ … – evaṃ … hoti."""
    v = (NEG if neg else VERB)[tense]

    def one(x):
        return f"“Người ấy là {x} thế nào, {BY if ext else ''}{v} {x} như thế”"
    if short:
        lst = f"{one(KIND13[0])}, hoặc {one(KIND13[1])}… hoặc {one(KIND13[12])}"
    else:
        lst = ", hoặc ".join(one(x) for x in KIND13)
    return f"({num}) {how(k, ext)} So với người khác: {lst} – {thus(close_k or k, ext)}."


def eternal_line(num, k, ext=False, var=""):
    words = ("tôi thường còn, tôi bền vững, tôi trường tồn, tôi có bản chất không biến đổi" if k == "asasmi"
             else "tôi sẽ bị đoạn diệt, tôi sẽ bị hủy diệt, tôi sẽ không còn tồn tại")
    s = f"{BY}{words}" if ext else words
    return f"({num}) {how(k, ext)} {separate(ext, var)}, {_FIVE_AGG}, người ta nghĩ “{cap(s)}” – {thus(k, ext)}."


def currents(ext):
    v_an = " [khác chính tả (Sī., Ka.): anavakārī]"
    v_av = " [khác chính tả (Sī.): avakārī]"
    L = [root_line("" if not ext else 1, "asmi", ["itthasmi", "evasmi", "aññathāsmi"], ext, "" if ext else v_an),
         kinds_line(2, "itthasmi", "asmi", ext),
         compare_line(3, "evasmi", "asmi", False, ext, short=ext),
         compare_line(4, "aññathāsmi", "asmi", True, ext, short=ext),
         root_line(5, "bhavissaṃ", ["itthaṃ bhavissaṃ", "evaṃ bhavissaṃ", "aññathā bhavissaṃ"], ext),
         kinds_line(6, "itthaṃ bhavissaṃ", "bhavissaṃ", ext, short=ext),
         compare_line(7, "evaṃ bhavissaṃ", "bhavissaṃ", False, ext, short=True,
                      close_k=None if ext else "bhavissaṃ"),
         compare_line(8, "aññathā bhavissaṃ", "bhavissaṃ", True, ext, short=True),
         eternal_line(9, "asasmi", ext, v_av if ext else ""),
         eternal_line(10, "sātasmi", ext),
         root_line(11, "siyaṃ", ["itthaṃ siyaṃ", "evaṃ siyaṃ", "aññathā siyaṃ"], ext),
         kinds_line(12, "itthaṃ siyaṃ", "siyaṃ", ext),
         compare_line(13, "evaṃ siyaṃ", "siyaṃ", False, ext, short=True),
         compare_line(14, "aññathā siyaṃ", "siyaṃ", True, ext, short=True),
         root_line(15, "apāhaṃ siyaṃ", ["apāhaṃ itthaṃ siyaṃ", "apāhaṃ evaṃ siyaṃ", "apāhaṃ aññathā siyaṃ"], ext),
         kinds_line(16, "apāhaṃ itthaṃ siyaṃ", "apāhaṃ", ext),
         compare_line(17, "apāhaṃ evaṃ siyaṃ", "apāhaṃ", False, ext, short=True),
         compare_line(18, "apāhaṃ aññathā siyaṃ", "apāhaṃ", True, ext, short=True)]
    return L


slip("^2-974 (7) «… – evaṃ bhavissanti hoti» (the closing lacks the second «evaṃ», cf. (13) «evaṃ evaṃ siyanti "
     "hoti»): rendered as written, «như vậy là có ý nghĩ “Tôi sẽ là”»")
_IN, _EX = "dựa vào phần bên trong", "dựa vào phần bên ngoài"
_c_in, _c_ex = currents(False), currents(True)
SEG["2-973"] = [f"Ở đây, mười tám {CURRENTS} {_IN} là những gì? "
                + cap(", ".join(having(k) for k in ORDER18)) + "."]
SEG["2-974"] = _c_in[:15] + [_c_in[15] + " " + _c_in[16], _c_in[17],
                             f"Đây là mười tám {CURRENTS} {_IN}."]
SEG["2-975"] = [f"Ở đây, mười tám {CURRENTS} {_EX} là những gì? "
                + cap(", ".join(having(k, True) for k in ORDER18)) + "."]
SEG["2-976"] = _c_ex + [
    f"Đây là mười tám {CURRENTS} {_EX}.",
    f"Như vậy, mười tám {CURRENTS} này {_IN}, mười tám {CURRENTS} này {_EX}; {SUM36} ba mươi sáu {CURRENTS}. Như vậy, "
    f"ba mươi sáu {CURRENTS} thuộc quá khứ, thuộc loại như vậy, ba mươi sáu {CURRENTS} thuộc tương lai, ba mươi sáu "
    f"{CURRENTS} thuộc hiện tại; {SUM36} một trăm lẻ tám {CURRENTS}."]
_62 = "sáu mươi hai sự mắc kẹt trong các quan điểm đã được Đức Thế Tôn nói đến trong bài giảng “Lưới Phạm Thiên”"
SEG["2-977"] = [
    f"Ở đây, {_62} là những gì? Bốn học thuyết về sự trường tồn, bốn học thuyết về sự trường tồn một phần, bốn học "
    "thuyết về hữu hạn và vô hạn, bốn học thuyết lẩn tránh như lươn, hai học thuyết về sự sinh khởi ngẫu nhiên, mười "
    "sáu học thuyết về sự có tri giác, tám học thuyết về sự không có tri giác, tám học thuyết về sự không phải có tri "
    "giác cũng không phải không có tri giác, bảy học thuyết về sự đoạn diệt, năm học thuyết về Niết-bàn ngay trong "
    f"đời này – đây là {_62}.",
    f"{S.CH_HEADINGS['Khuddakavatthuvibhaṅgo']} đã hoàn tất."]
pi2("Phân tích các loại hiểu biết đã hoàn tất.")
misfit("amarāvikkhepikā (^2-977): no entry; «học thuyết lẩn tránh như lươn»; ekaccasassatikā «trường tồn một phần», "
       "antānantikā «về hữu hạn và vô hạn» (termbase)")


# =========================================================================== build and checks
def heading(ln):
    lvl, text = ln.split(" ", 1)
    return f"{lvl} {HEAD[text]}"


def check_line(sid, p, v):
    assert K79.dashes(p) == K79.dashes(v), (sid, "dash count", K79.dashes(p), K79.dashes(v), p[:80], v[:300])
    assert ":-" not in v and "—" not in v and "…." not in v and ".." not in v, (sid, v[:160])
    bodyv = re.sub(r"\[[^\]]*\]", "", v)
    assert not K79.FOREIGN.search(bodyv), (sid, K79.FOREIGN.search(bodyv).group(0), v[:200])
    assert "  " not in v and not v.endswith(" "), (sid, v[:160])
    assert "là là" not in v and " ,"not in v and " ." not in v, (sid, v[:160])
    if p.count('"') % 2 == 0:
        assert v.count("“") == v.count("”"), (sid, "quotes", v[:300])
    assert v.count("‘") == v.count("’"), (sid, "single quotes", v[:300])
    depth = 0
    for ch in v:                                       # “…” never nested inside “…” (use ‘…’)
        if ch == "“":
            assert depth == 0, (sid, "nested double quotes", v[:300])
            depth += 1
        elif ch == "”":
            depth -= 1
    if not p.startswith("#"):
        assert v[-1] in ".?", (sid, v[-40:])
        assert p.endswith("?") == v.endswith("?"), (sid, v[-40:])


def build():
    pali = (S.PALI / PART).read_text(encoding="utf-8")
    h = {}
    for sid, lines in K1.segs(pali):
        lines = [K1.ID.sub("", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            h[sid] = [heading(lines[0])]
            continue
        vi = SEG[sid]
        assert len(vi) == len(lines), (sid, len(vi), len(lines))
        h[sid] = [unicodedata.normalize("NFC", x) for x in vi]
        for p, v in zip(lines, h[sid]):
            check_line(sid, p, v)
    missing = set(SEG) - set(h)
    assert not missing, missing
    return pali, h


def render(pali, h):
    blocks = []
    for sid, plines in K1.segs(pali):
        lines = list(h[sid])
        lines[-1] = f"{lines[-1]} ^{sid}"
        blocks.append("\n".join(lines))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


def check_pi1():
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_VI.glob("*.md")))
    missing = [s for s in PI1_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI1_USED)


def check_pi2():
    text = "\n".join((S.OUT / f).read_text(encoding="utf-8") for f in PI2_DONE)
    missing = [s for s in PI2_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI2_USED)


def main():
    dry = "--dry" in sys.argv
    pali, h = build()
    text = render(pali, h)
    if not dry:
        (S.OUT / PART).write_bytes(text.encode("utf-8"))
    print(f"{'built' if dry else 'wrote'} {PART}: {len(h)} segments")
    print(f"pi-1 strings checked: {check_pi1()}; pi-2 strings checked: {check_pi2()}")
    for s in SLIPS:
        print("slip:", s)
    for s in MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()
