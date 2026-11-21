# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 6: 6-pancakapuggalapannatti.md (Pañcaka, ^4-191 … ^4-201).

Imports the approved sample builder (names, frames, headings, closers) and the finished chapter-4 builder
(read-only; frames «là những ai?», «Trong số đó», «Giống như … cũng như thế», «đang có mặt, được tìm thấy …»,
the requisites list and the «biết các hiện tượng thiện và bất thiện …» string), and writes ONLY
AI_translation/vietnamese/pi-4-vietnamese-plain-zeroshot_split_chapters/6-pancakapuggalapannatti.md.
Every string taken from pi-1 / pi-2 is asserted to occur in that book's reviewed Vietnamese rails.
run:  python -I -X utf8 build_6_vi.py
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as B4  # noqa: E402  (importing writes nothing)

CH = "6-pancakapuggalapannatti.md"
N = B.NAME
cap, q = B.cap, B.q
IDHE = B.IDHEKACCO                        # Ở đời này, có người
TATRA = B4.TATRA                         # Trong số đó,
SEYYATHA = B4.SEYYATHA                   # Giống như
EVAMEVAM = B4.EVAMEVAM                   # cũng như thế,
tattha_who = B4.tattha_who               # Ở đây, … là những ai?
SANTO_LOKE = B4.SANTO_LOKE               # đang có mặt, được tìm thấy trong thế gian
SANTO_BHIKKHU = B4.SANTO_BHIKKHU         # đang có mặt, được tìm thấy giữa các tỳ-khưu
CIVARA = B4.CIVARA                       # y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh (pi-2)
TYPES5 = B.TYPES_COUNT[5]                # Năm hạng người
KATAME_PANCA = "Năm hạng nào?"           # Katame pañca? (ch4 «Ba hạng nào?»)
PUNA = "Lại nữa,"                        # Puna caparaṃ (pi-2)
ORD = {1: "thứ nhất", 2: "thứ hai", 3: "thứ ba", 4: "thứ tư", 5: "thứ năm"}


def lc(s):
    return s[:1].lower() + s[1:]


def evam(name):                          # Evaṃ puggalo X (hoti).
    return f"Như vậy là {name}."


# ---------------------------------------------------------------- ^4-191 (five persons, matrix ^4-M-11 (1))
LIBER = ("hiểu rõ đúng như thật sự giải thoát của tâm, sự giải thoát nhờ trí tuệ ấy, nơi mà các hiện tượng xấu ác "
         "bất thiện đã sinh khởi nơi người ấy chấm dứt không còn dư sót")              # sample matrix item (1)
LIBER_NO_UPPANNA = LIBER.replace(" đã sinh khởi", "")                                # ^4-191 line 4 (no uppannā)
ARABHA = {  # ārabhati / vippaṭisārī as in the matrix (1)
    (1, 1): "phạm lỗi và ăn năn", (1, 0): "phạm lỗi nhưng không ăn năn",
    (0, 1): "không phạm lỗi nhưng ăn năn", (0, 0): "không phạm lỗi và không ăn năn",
}
AS_ARAMBHA = "các ô nhiễm sinh từ việc phạm lỗi"         # ārambhajā āsavā
AS_VIPPATISARA = "các ô nhiễm sinh từ sự ăn năn"         # vippaṭisārajā āsavā
SAMASAMO = "Như vậy, tôn giả sẽ hoàn toàn ngang bằng với người thứ năm kia"   # Evamāyasmā amunā pañcamena …


def advice(arambha, vip, var=""):
    have = (f"Nơi tôn giả, có {AS_ARAMBHA}{var}" if arambha else f"Nơi tôn giả, không có {AS_ARAMBHA}")
    grow = f"{AS_VIPPATISARA} đang tăng trưởng" if vip else f"{AS_VIPPATISARA} không tăng trưởng"
    steps = []
    if arambha:
        steps.append(f"dứt bỏ {AS_ARAMBHA}")
    if vip:
        steps.append(f"xua tan {AS_VIPPATISARA}")
    sadhu = ("Thật tốt lành thay nếu tôn giả, sau khi " + ", ".join(steps) + ", tu tập tâm và trí tuệ."
             if steps else "Thật tốt lành thay nếu tôn giả tu tập tâm và trí tuệ.")
    return f"“{have}, {grow}. {sadhu} {SAMASAMO}”."


def tatra_person(arambha, vip, liber=LIBER, var=""):
    return (f"{TATRA} người nào {ARABHA[(arambha, vip)]}, không {liber}, thì người ấy nên được nói như sau – "
            + advice(arambha, vip, var))


# ---------------------------------------------------------------- ^4-192
KNOW = B4.EYE_DHAMMA.split("có thể ", 1)[1]           # biết các hiện tượng thiện và bất thiện, biết … (ch4 / pi-1)
NOT_KNOW = "không " + KNOW.replace(", biết ", ", không biết ")

# ---------------------------------------------------------------- warriors
FALTER = "chùn bước, nản lòng, không đứng vững{v}, không thể"   # saṃsīdati visīdati na santhambhati na sakkoti
BATTLE = "xông vào trận chiến"                                   # saṅgāmaṃ otarituṃ


def w_falter(v=""):
    return f"{FALTER.format(v=v)} {BATTLE}"


def m_falter(v1="", v2=""):   # … brahmacariyaṃ sandhāretuṃ, sikkhādubbalyaṃ āvikatvā sikkhaṃ paccakkhāya hīnāyāvattati
    return (f"{FALTER.format(v='')} duy trì đời sống tu hành trong sạch{v1}, bày tỏ sự yếu kém trong sự tu học{v2}, "
            "từ bỏ sự tu học và quay về đời sống thấp kém")


BEAR = ["chịu được đám bụi mù", "chịu được ngọn cờ", "chịu được tiếng hò hét", "chịu được cuộc giáp chiến"]
RAJ = "chỉ vừa thấy đám bụi mù thì"                             # rajaggaññeva disvā
DHAJ = "chỉ vừa thấy ngọn cờ thì"                               # dhajaggaññeva disvā
USS = "chỉ vừa nghe tiếng hò hét{v} thì"                        # ussāraṇaññeva sutvā
HIT = "trong cuộc giáp chiến thì bị đánh trúng, bị thương"       # sampahāre haññati byāpajjati
WIN = "chiến thắng trận chiến ấy, là người đã thắng trận, làm chủ chính chiến địa ấy"  # taṃ saṅgāmaṃ abhivijinitvā …


def stage(k, falter, v=""):
    """Behaviour of warrior / monk k (1-5) up to the failure point (k<5) or the bearing of the clash (k=5)."""
    if k == 1:
        return f"{RAJ} {falter}"
    bears = ", ".join(BEAR[:k - 1])
    if k == 2:
        return f"{bears}, nhưng {DHAJ} {falter}"
    if k == 3:
        return f"{bears}, nhưng {USS.format(v=v)} {falter}"
    if k == 4:
        return f"{bears}, nhưng {HIT}"
    return ", ".join(BEAR)


def warrior(k, v="", v_falter=""):
    lead = "ở đời này, có chiến binh" if k == 1 else f"{PUNA} ở đời này, có chiến binh"
    body = stage(k, w_falter(v_falter), v)
    s = f"{lead} {body}."
    if k == 5:
        s += f" Người ấy {WIN}."
    return s + f" Ở đời này, cũng có chiến binh như vậy. Đây là chiến binh {ORD[k]} {SANTO_LOKE}."


def simile(k):
    body = stage(k, w_falter())
    if k == 5:
        body += f", người ấy {WIN}"
    return (f"{SEYYATHA} chiến binh ấy {body}, người này cũng giống như thế. Ở đời này, cũng có người như vậy. "
            f"Đây là người {ORD[k]} giống như chiến binh {SANTO_BHIKKHU}.")


THING = {1: "đám bụi mù", 2: "ngọn cờ", 3: "tiếng hò hét", 4: "cuộc giáp chiến", 5: "sự chiến thắng trong trận chiến"}


def kim(k):            # Kimassa X?
    return f"Đối với vị ấy, {THING[k]} là gì?"


def idam(k):           # Idamassa X.
    return f"Đối với vị ấy, đây là {THING[k]}."


WOMAN = ("người nữ hoặc thiếu nữ xinh đẹp, dễ nhìn, dễ mến, sở hữu vẻ đẹp tuyệt hảo của dung sắc")  # itthī vā kumārī vā …
HEARD = f"“Ở làng hoặc thị trấn tên như thế kia, có {WOMAN}”"
GONE = ("Ở đây, khi vị tỳ-khưu đi đến rừng, hoặc đi đến gốc cây, hoặc đi đến ngôi nhà trống, có phụ nữ đến gần, "
        "{acts} vị ấy.")                                       # Idha bhikkhuṃ araññagataṃ vā … mātugāmo upasaṅkamitvā …
TEASE = "cười cợt{v}, tán tỉnh, cười đùa ầm ĩ, trêu ghẹo"        # ūhasati ullapati ujjagghati uppaṇḍeti
PRESS = "ngồi sát bên, nằm sát bên, đè lên"                      # abhinisīdati abhinipajjati ajjhottharati

# ---------------------------------------------------------------- ^4-198 (pi-2 Jhānavibhaṅga ^2-508 wording)
SECLUDE = ("Vị ấy lui tới chỗ ở thanh vắng: rừng, gốc cây, núi, khe núi, hang núi, bãi tha ma, rừng sâu, "
           "khoảng trời trống, đống rơm")
SIT = ("Vị ấy đi đến rừng, hoặc đi đến gốc cây, hoặc đi đến ngôi nhà trống, ngồi xuống, xếp chân kiết già, "
       "đặt thân ngay thẳng, thiết lập sự tỉnh thức trước mặt.")
HIND = [
    "Sau khi dứt bỏ sự thèm muốn đối với thế gian, vị ấy sống với tâm đã lìa sự thèm muốn, làm trong sạch hoàn "
    "toàn tâm khỏi sự thèm muốn",
    "Sau khi dứt bỏ ác ý và sự sân hận dữ dội, vị ấy sống với tâm không ác ý, thương xót và mong điều lợi ích cho "
    "mọi chúng sinh, muôn loài, làm trong sạch hoàn toàn tâm khỏi ác ý và sự sân hận dữ dội",
    "Sau khi dứt bỏ sự uể oải và đờ đẫn, vị ấy sống đã lìa sự uể oải và đờ đẫn, có tri giác về ánh sáng, tỉnh "
    "thức và hiểu biết rõ ràng, làm trong sạch hoàn toàn tâm khỏi sự uể oải và đờ đẫn",
    "Sau khi dứt bỏ sự xao động và hối tiếc, vị ấy sống không xao động, có tâm đã lắng dịu hoàn toàn ở nơi bản "
    "thân, làm trong sạch hoàn toàn tâm khỏi sự xao động và hối tiếc",
    "Sau khi dứt bỏ sự hoài nghi, vị ấy sống đã vượt qua sự hoài nghi, không còn băn khoăn đối với các hiện tượng "
    "thiện, làm trong sạch hoàn toàn tâm khỏi sự hoài nghi",
]
JHANA1 = ("Sau khi dứt bỏ năm chướng ngại này, là những thứ làm vẩn đục tâm, làm suy yếu trí tuệ, vị ấy hoàn toàn "
          "tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, chứng nhập và an trú tầng thiền thứ nhất, có "
          "sự hướng tâm và sự duy trì tâm, có sự hân hoan và hạnh phúc sinh từ sự tách biệt")
VUPASAMA = "nhờ sự hướng tâm và sự duy trì tâm lắng xuống"           # vitakkavicārānaṃ vūpasamā (pi-2)
JHANA_PE = "tầng thiền thứ hai… tầng thiền thứ ba…"                  # dutiyaṃ jhānaṃ…pe… tatiyaṃ jhānaṃ…pe… (pi-1)
JHANA4 = "chứng nhập và an trú tầng thiền thứ tư"                     # catutthaṃ jhānaṃ upasampajja viharati (pi-2)
SAMAHITE = ("Khi tâm đã an định như vậy, trong sạch, sáng tỏ, không vết nhơ, đã lìa những thứ làm vẩn đục, mềm mại, "
            "dễ vận dụng, vững vàng, đạt đến trạng thái bất động, vị ấy dẫn tâm đến sự hiểu biết về sự diệt tận các "
            "ô nhiễm.")
ASAVA_PAJANATI = ("hiểu rõ đúng như thật: “Đây là các ô nhiễm”, hiểu rõ đúng như thật: “Đây là sự phát sinh của các "
                  "ô nhiễm”, hiểu rõ đúng như thật: “Đây là sự chấm dứt các ô nhiễm”, hiểu rõ đúng như thật: “Đây là "
                  "cách thực hành dẫn đến sự chấm dứt các ô nhiễm”.")
VIMUCCATI = ("Khi vị ấy biết như vậy, thấy như vậy, tâm được giải thoát khỏi cả ô nhiễm dục lạc, tâm được giải thoát "
             "khỏi cả ô nhiễm hiện hữu, tâm được giải thoát khỏi cả ô nhiễm vô minh. Khi đã được giải thoát, có sự "
             "hiểu biết: “Đã được giải thoát”. Vị ấy hiểu rõ: “Sự sinh đã được diệt tận, đời sống tu hành trong sạch "
             "đã được sống trọn, việc cần làm đã được làm xong, không còn gì khác cho trạng thái này nữa”.")

# ---------------------------------------------------------------- ^4-199 … ^4-201 ascetic practices
FEW = ("chỉ dựa vào sự ít ham muốn{v1}, chỉ dựa vào sự biết đủ, chỉ dựa vào sự giảm trừ phiền não, chỉ dựa vào sự "
       "thấy chừng này là đủ{v2}")       # appicchataṃyeva nissāya santuṭṭhiṃyeva … sallekhaṃyeva … idamatthitaṃyeva …
AGGA = "người đứng đầu, cao quý nhất, dẫn đầu{v}, tối thượng và ưu tú nhất"   # aggo ca seṭṭho ca pāmokkho ca …
MILK = ("{s} từ bò có sữa, từ sữa có sữa đông, từ sữa đông có bơ tươi{v}, từ bơ tươi có bơ lỏng, từ bơ lỏng có "
        "phần tinh túy của bơ lỏng, phần tinh túy của bơ lỏng được xem là đứng đầu trong số ấy;")  # pi-1 milk products


def practice(key, var=None):
    """^4-199 / ^4-201: the five X-ikas (two lines). var: dict of variant brackets (first occurrence only)."""
    v = var or {}
    name = N[key]
    verb = name[len("người "):]
    group = f"{lc(TYPES5)} {verb}"                    # năm hạng người chỉ ăn thức ăn khất thực
    few1 = FEW.format(v1=v.get("few1", ""), v2=v.get("few2", ""))
    few = FEW.format(v1="", v2="")
    l1 = (f"{tattha_who(group)} Có {name} vì chậm hiểu, vì mê muội; có {name} vì có ước muốn xấu xa, bị ước muốn "
          f"chi phối; có {name} vì điên loạn, vì tâm tán loạn; có {name} với ý nghĩ “Được chư Phật và các đệ tử của "
          f"chư Phật khen ngợi”; nhưng cũng có {name} {few1}. "
          f"{TATRA} {name} nào {few} mà {verb}, thì người này là {AGGA.format(v=v.get('agga', ''))} trong "
          f"{group} này.")
    l2 = (f"{MILK.format(s=SEYYATHA, v=v.get('milk', ''))} {EVAMEVAM} {name} nào {few} mà {verb}, thì người này là "
          f"{AGGA.format(v='')} trong {group} này. Đây là {group}.")
    return [l1, l2]


PRACTICE_PE = ["khalupacchābhattiko", "ekāsaniko", "paṃsukūliko", "tecīvariko", "āraññiko", "rukkhamūliko",
               "abbhokāsiko", "nesajjiko", "yathāsanthatiko"]

# ---------------------------------------------------------------- variant brackets of this chapter
V191 = " [khác chính tả (Ka.): ārabbhajā; Tăng Chi Bộ Kinh 5.142]"
V192 = " [dị bản (Syā., Ka.): ayaṃ pana; Tăng Chi Bộ Kinh 5.141]"
V193A = " [khác chính tả (Sī.): satthambhati; Tăng Chi Bộ Kinh 5.141]"
V193B = " [dị bản (Sī.): ussādanaṃyeva; (Syā., Ka.): ussādanaññeva; Tăng Chi Bộ Kinh 5.141]"
V194A = " [dị bản (Sī., Syā.): santānetuṃ; Tăng Chi Bộ Kinh 5.75]"
V194B = " [khác chính tả (Sī.): āvīkatvā]"
V195 = " [dị bản (Sī.): sāmaṃyeva]"
V196 = " [khác chính tả (Chú giải): uhasati; Tăng Chi Bộ Kinh 5.75]"
V199 = {"few1": " [dị bản (Syā.): appicchaṃyeva; Tăng Chi Bộ Kinh 5.181]",
        "few2": " [khác chính tả (Sī.): idamaṭṭhitaṃyeva]",
        "agga": " [dị bản (Sī.): mokkho]",
        "milk": " [khác chính tả (Sī.): nonītaṃ]"}

CROSS = [
    (2, CIVARA), (2, "có ước muốn xấu xa, bị ước muốn chi phối"), (2, "từ bỏ sự tu học và quay về đời sống thấp kém"),
    (2, "đời sống tu hành trong sạch"), (2, PUNA), (2, SECLUDE), (2, SIT), (2, VUPASAMA), (1, JHANA_PE),
    (2, JHANA4), (2, JHANA1), (2, "tâm đã an định"), (2, "trong sạch, sáng tỏ"), (1, "sự mềm mại"),
    (1, "dễ vận dụng"), (2, "trạng thái bất động"), (2, "sự hiểu biết về sự diệt tận các ô nhiễm"),
    (1, "ô nhiễm dục lạc, ô nhiễm hiện hữu"), (1, "ô nhiễm vô minh"), (1, "sự sinh"),
    (1, "sữa, sữa đông, bơ lỏng, bơ tươi"), (2, "tôn giả"), (1, "tu tập"), (2, "một người nữ"), (2, "thiếu nữ"),
    (2, "Ở đây, vị tỳ-khưu"), (1, "sự không tán loạn"), (2, "với ý nghĩ “"), (2, "hiểu rõ:"), (2, "cũng như thế,"),
    (2, "Giống như"), (1, "sự diệt tận các ô nhiễm"), (2, "Tăng Chi Bộ Kinh"), (1, "Các hiện tượng đen tối"),
    (1, "Các hiện tượng trong sáng"), (1, "Các hiện tượng thấp kém"), (1, "Các hiện tượng ưu việt"),
    (2, "là những ai?"), (2, "đệ tử"),
] + [(2, h) for h in HIND]


def lines():
    L = ["#### " + B.CHAPTER_HEADING[6]]
    # ^4-191 (4 lines)
    L.append(tatra_person(1, 1, var=V191))
    L.append(tatra_person(1, 0))
    L.append(tatra_person(0, 1))
    L.append(tatra_person(0, 0, liber=LIBER_NO_UPPANNA) + " Bốn hạng người này, khi được người thứ năm kia khuyên "
             "bảo như vậy, chỉ dạy như vậy, dần dần đạt đến sự diệt tận các ô nhiễm.")
    # ^4-192 (5 lines)
    k = N["datvā avajānāti"]
    L.append(f"{q(k)} {IDHE} cho ai đó {CIVARA}, rồi người ấy nghĩ như vầy – “Tôi cho, người này{V192} nhận”, và "
             f"sau khi cho, người ấy khinh thường người kia. {evam(k)}")
    k = N["saṃvāsena avajānāti"]
    L.append(f"{q(k)} {IDHE} sống chung với ai đó hai hoặc ba năm, rồi khinh thường người kia vì sống chung. "
             f"{evam(k)}")
    k = N["ādheyyamukho"]
    L.append(f"{q(k)} {IDHE}, khi lời khen hoặc lời chê về người khác được nói ra, thì nhanh chóng tin ngay. "
             f"{evam(k)}")
    k = N["lolo"]
    L.append(f"{q(k)} {IDHE} có niềm tin chóng qua, lòng sùng kính chóng qua, lòng quý mến chóng qua, lòng tin trong "
             f"sáng chóng qua. {evam(k)}")
    k = N["mando momūho"]
    L.append(f"{q(k)} {IDHE} {NOT_KNOW}. {evam(k)}")
    # ^4-193 (5 lines)
    yodha = f"{lc(TYPES5)} giống như {B.SIMILE['yodhājīva']}"
    L.append(f"{tattha_who(yodha)} Năm chiến binh – " + warrior(1, v_falter=V193A))
    L.append(cap(warrior(2)))
    L.append(cap(warrior(3, v=V193B)))
    L.append(cap(warrior(4)))
    L.append(cap(warrior(5)) + f" Đây là năm chiến binh {SANTO_LOKE}.")
    # ^4-194 … ^4-197 (2 lines each)
    L.append(f"{cap(EVAMEVAM)} {yodha} này {SANTO_BHIKKHU}. {KATAME_PANCA} Ở đời này, có vị tỳ-khưu {RAJ} "
             f"{m_falter(V194A, V194B)}. {kim(1)} Ở đây, vị tỳ-khưu nghe người ta nói – {HEARD}. Vị ấy nghe vậy rồi "
             f"{m_falter()}. {idam(1)}")
    L.append(simile(1))
    L.append(f"{PUNA} ở đời này, có vị tỳ-khưu {stage(2, m_falter())}. {kim(2)} Ở đây, vị tỳ-khưu quả thật không "
             f"nghe người ta nói – {HEARD}, nhưng chính mình{V195} thấy {WOMAN}. Vị ấy thấy vậy rồi {m_falter()}. "
             f"{idam(2)}")
    L.append(simile(2))
    L.append(f"{PUNA} ở đời này, có vị tỳ-khưu {stage(3, m_falter())}. {kim(3)} "
             + GONE.format(acts=TEASE.format(v=V196))
             + f" Vị ấy, khi bị phụ nữ {TEASE.format(v='')}, thì {m_falter()}. {idam(3)}")
    L.append(simile(3))
    L.append(f"{PUNA} ở đời này, có vị tỳ-khưu {stage(4, '')}. {kim(4)} " + GONE.format(acts=PRESS)
             + f" Vị ấy, khi bị phụ nữ {PRESS}, thì không từ bỏ sự tu học, không bày tỏ sự yếu kém, mà hành dâm. "
             f"{idam(4)}")
    L.append(simile(4))
    # ^4-198 (5 lines)
    L.append(f"{PUNA} ở đời này, có vị tỳ-khưu {stage(5, '')}. Vị ấy {WIN}. {kim(5)} " + GONE.format(acts=PRESS)
             + f" Vị ấy, khi bị phụ nữ {PRESS}, thì gỡ mình ra, thoát ra, rồi đi đến nơi mình muốn.")
    L.append(f"{SECLUDE}. {SIT} " + "; ".join([HIND[0]] + [lc(h) for h in HIND[1:]]) + ".")
    L.append(f"{JHANA1}; {VUPASAMA}, {JHANA_PE} vị ấy {JHANA4}.")
    L.append(SAMAHITE + f" Vị ấy {B.SACCA_PAJANATI[:-1]}, {ASAVA_PAJANATI}")
    L.append(f"{VIMUCCATI} {idam(5)} " + simile(5) + f" Đây là {yodha} {SANTO_BHIKKHU}.")
    # ^4-199 (2 lines)
    L += practice("piṇḍapātiko", V199)
    # ^4-200 (1 line)
    first = f"{lc(TYPES5)} {N[PRACTICE_PE[0]][len('người '):]}"
    rest = "… ".join(f"{lc(TYPES5)} {N[p][len('người '):]}" for p in PRACTICE_PE[1:])
    L.append(f"Ở đây, {first} là những ai… {rest}…")
    # ^4-201 (3 lines)
    L += practice("sosāniko")
    L.append(B.NIDDESA_CLOSER[5])
    return L


def main():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    B.check_cross_book()
    B4.check_cross()
    matika = (B.OUT_DIR / "1-matika.md").read_text(encoding="utf-8")
    for s in ("Có người phạm lỗi [khác chính tả (Sī., Syā.): ārambhati] và ăn năn, không " + LIBER + ".",f"Có người {ARABHA[(1, 0)]}, không {LIBER}.",
              f"Có người {ARABHA[(0, 1)]}, không {LIBER}.", f"Có người {ARABHA[(0, 0)]}, không {LIBER}.",
              "(3) " + B.TYPES_COUNT[5] + " giống như " + B.SIMILE["yodhājīva"] + "."):
        assert s in matika, "matrix string not found: " + s[:60]
    L = lines()
    text = B.assemble(CH, L)
    # every Pañcaka person name of the matrix (B.NAME) appears; the five defined ones are asked
    for p in ("datvā avajānāti", "saṃvāsena avajānāti", "ādheyyamukho", "lolo", "mando momūho"):
        assert B.q(B.NAME[p]) in text and evam(B.NAME[p]) in text, p
    for p in ["piṇḍapātiko", "sosāniko"] + PRACTICE_PE:
        assert B.NAME[p][len("người "):] in text and B.PANCAKA_NAMES[p] == B.NAME[p], p
    for p in ("piṇḍapātiko", "sosāniko"):
        assert f"Có {B.NAME[p]} vì chậm hiểu" in text, p
    assert text.count(SECLUDE) == 1 and text.count(WIN) == 3
    for bad in ("—", ":-", "….", "chánh niệm"):
        assert bad not in text, bad
    (B.OUT_DIR / CH).write_bytes(text.encode("utf-8"))
    print(f"OK: cross-book strings {len(CROSS)} (+ sample {len(B.CROSS_BOOK)}, ch4 {len(B4.CROSS)}); "
          f"wrote {CH} ({len(L)} lines)")


if __name__ == "__main__":
    main()
