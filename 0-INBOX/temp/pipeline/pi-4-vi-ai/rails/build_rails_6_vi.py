"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 6, Pañcakapuggalapaññatti (^4-1-5-0, ^4-191 .. ^4-201).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/6-pancakapuggalapannatti.md from fixed strings.
Imports the approved sample constants READ-ONLY (build_rails_sample_vi as S; importing writes nothing).
At build time: every string marked (pi-1) / (pi-2) in REUSED is asserted to occur in that book's approved Vietnamese
rails; every person name used equals S.NAME and occurs verbatim (the pañcaka (1) names without «có người», as the
definition Pāli has no atthi / ekacco there: coordinator rule).
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-6.md.

usage: python -I -X utf8 build_rails_6_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

OUT = S.OUT_DIR / "6-pancakapuggalapannatti.md"


def N(k):
    return S.NAME[k]


# ---------------------------------------------------------------------------------------------------------------
# Variant notes
# ---------------------------------------------------------------------------------------------------------------
V_ARABBHAJA = " [khác chính tả (Ka.): ārabbhajā; Tăng Chi Bộ Kinh 5.142]"
V_AYAM_PANA = " [dị bản (Syā., Ka.): ayaṃ pana; Tăng Chi Bộ Kinh 5.141]"
V_SATTHAMBHATI = " [khác chính tả (Sī.): satthambhati; Tăng Chi Bộ Kinh 5.141]"
V_USSADANA = " [dị bản (Sī.): ussādanaṃyeva; (Syā., Ka.): ussādanaññeva; Tăng Chi Bộ Kinh 5.141]"
V_SANTANETUM = " [dị bản (Sī., Syā.): santānetuṃ; Tăng Chi Bộ Kinh 5.75]"
V_AVIKATVA = " [khác chính tả (Sī.): āvīkatvā]"
V_SAMAM = " [dị bản (Sī.): sāmaṃyeva]"
V_UHASATI = " [khác chính tả (Chú giải): uhasati; Tăng Chi Bộ Kinh 5.75]"
V_APPICCHA = " [dị bản (Syā.): appicchaṃyeva; Tăng Chi Bộ Kinh 5.181]"
V_IDAMATTHITA = " [khác chính tả (Sī.): idamaṭṭhitaṃyeva]"
V_MOKKHO = " [dị bản (Sī.): mokkho]"
V_NONITA = " [khác chính tả (Sī.): nonītaṃ]"

# ---------------------------------------------------------------------------------------------------------------
# ^4-191 (pañcaka 1)
# ---------------------------------------------------------------------------------------------------------------
TATRA = "Trong số đó, người nào"                     # Tatra yvāyaṃ puggalo
VACANIYO = "thì nên nói với người ấy như vầy –"       # so evamassa vacanīyo –
ARAMBHAJA = "các ô nhiễm sinh từ việc phạm lỗi"       # ārambhajā āsavā / ārambhaje āsave
VIPPATISARAJA = "các ô nhiễm sinh từ sự ăn năn"       # vippaṭisārajā āsavā / vippaṭisāraje āsave
SADHU = "Thật tốt lành thay nếu tôn giả"              # Sādhu vatāyasmā
BHAVETU = "tu tập tâm và trí tuệ"                      # cittaṃ paññañca bhāvetu
SAMASAMO = "Như vậy, tôn giả sẽ trở nên hoàn toàn ngang bằng với người thứ năm kia"
#   Evamāyasmā amunā pañcamena puggalena samasamo bhavissati
CATTARO = ("Bốn hạng người này, khi được người thứ năm kia khuyên bảo như vậy, được chỉ dạy như vậy, "
           "dần dần đạt đến sự diệt tận các ô nhiễm.")
#   Ime cattāro puggalā amunā pañcamena puggalena evaṃ ovadiyamānā evaṃ anusāsiyamānā anupubbena āsavānaṃ khayaṃ pāpuṇanti.


def atthi(neg):                     # āyasmato kho ārambhajā āsavā (na) saṃvijjanti
    return f"Tôn giả quả thật {'không ' if neg else ''}có {ARAMBHAJA}"


def vaddhanti(neg):                 # vippaṭisārajā āsavā (na)ppavaḍḍhanti
    return f"{VIPPATISARAJA} {'không tăng trưởng' if neg else 'đang tăng trưởng'}"


# ---------------------------------------------------------------------------------------------------------------
# ^4-192 (pañcaka 2)
# ---------------------------------------------------------------------------------------------------------------
REQUISITES = "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh"   # (pi-2) cīvara…parikkhāra
KUSALA = "các hiện tượng thiện và bất thiện"          # (pi-1) kusalākusalā dhammā

# ---------------------------------------------------------------------------------------------------------------
# ^4-193 .. ^4-198 (pañcaka 3: the warrior simile)
# ---------------------------------------------------------------------------------------------------------------
STAGES = ["đám bụi mù", "ngọn cờ", "tiếng hò hét", "cuộc giáp chiến"]   # rajaggaṃ, dhajaggaṃ, ussāraṇaṃ, sampahāraṃ
TRIGGER = ["chỉ vừa thấy đám bụi mù", "chỉ vừa thấy ngọn cờ", "chỉ vừa nghe tiếng hò hét"]
#   rajaggaññeva disvā / dhajaggaññeva disvā / ussāraṇaññeva sutvā
SINK = "chùn bước, nản lòng, không đứng vững"          # saṃsīdati visīdati na santhambhati
OTARITUM = "không thể bước vào trận chiến"             # na sakkoti saṅgāmaṃ otarituṃ
RETURN = "từ bỏ sự tu học và quay về đời sống thấp kém"                    # (pi-2) sikkhaṃ paccakkhāya hīnāyāvattati
MONK_FAIL = ("không thể duy trì đời sống tu hành trong sạch, bày tỏ sự yếu kém trong sự tu học, " + RETURN)
#   na sakkoti brahmacariyaṃ sandhāretuṃ, sikkhādubbalyaṃ āvikatvā sikkhaṃ paccakkhāya hīnāyāvattati
HATA = "trong cuộc giáp chiến thì bị đánh trúng, bị thương"               # sampahāre haññati byāpajjati
WIN = "sau khi chiến thắng trận chiến ấy, là người đã thắng trận, làm chủ chính chiến địa ấy"
#   taṃ saṅgāmaṃ abhivijinitvā vijitasaṅgāmo tameva saṅgāmasīsaṃ ajjhāvasati
ORD = ["thứ nhất", "thứ hai", "thứ ba", "thứ tư", "thứ năm"]
SANTO_LOKE = "là có thật, được tìm thấy trên thế gian"                     # santo saṃvijjamāno/ā lokasmiṃ
SANTO_BHIKKHU = "là có thật, được tìm thấy trong số các vị tỳ-khưu"        # santo saṃvijjamāno/ā bhikkhūsu
EVARUPO_YODHA = "Ở đời này, cũng có chiến binh như vậy."                  # Evarūpopi idhekacco yodhājīvo hoti.
EVARUPO = "Ở đời này, cũng có người như vậy."                             # Evarūpopi idhekacco puggalo hoti.
TATHUPAMO = "người này cũng giống như vậy"                                # tathūpamo ayaṃ puggalo
SEE = ("người nữ hoặc thiếu nữ đẹp đẽ, dễ nhìn, đáng mến, được trang bị vẻ đẹp dung mạo tuyệt vời")
#   itthī vā kumārī vā abhirūpā dassanīyā pāsādikā paramāya vaṇṇapokkharatāya samannāgatā
HEAR = f"Ở làng hoặc thị trấn tên như thế kia, có {SEE}"   # asukasmiṃ nāma gāme vā nigame vā …
GATA = "đi đến rừng, hoặc đi đến gốc cây, hoặc đi đến ngôi nhà trống"      # (pi-2) araññagata… suññāgāragata
IDHA_GATA = f"Ở đây, khi vị tỳ-khưu {GATA}, có phụ nữ đến gần"            # Idha bhikkhuṃ …gataṃ … mātugāmo upasaṅkamitvā
HASA = "cười cợt, tán tỉnh, cười đùa ầm ĩ, trêu ghẹo"   # ūhasati ullapati ujjagghati uppaṇḍeti (and -iyamāno)
NISI = "ngồi sát bên, nằm sát bên, đè lên"              # abhinisīdati abhinipajjati ajjhottharati (and -iyamāno)

# ^4-198: the training after victory (pi-2 ^2-508 strings)
SENASANA = ("Vị ấy lui tới chỗ ở thanh vắng: rừng, gốc cây, núi, khe núi, hang núi, bãi tha ma, rừng sâu, "
            "khoảng trời trống, đống rơm")                                                              # (pi-2)
NISIDATI = ("Vị ấy đi đến rừng, hoặc đi đến gốc cây, hoặc đi đến ngôi nhà trống, ngồi xuống, xếp chân kiết già, "
            "đặt thân ngay thẳng, thiết lập sự tỉnh thức trước mặt.")                                    # (pi-2)
NIV = [
    "Sau khi dứt bỏ sự thèm muốn đối với thế gian, vị ấy sống với tâm đã lìa sự thèm muốn, làm trong sạch "
    "hoàn toàn tâm khỏi sự thèm muốn",
    "sau khi dứt bỏ ác ý và sự sân hận dữ dội, vị ấy sống với tâm không ác ý, thương xót và mong điều lợi ích "
    "cho mọi chúng sinh, muôn loài, làm trong sạch hoàn toàn tâm khỏi ác ý và sự sân hận dữ dội",
    "sau khi dứt bỏ sự uể oải và đờ đẫn, vị ấy sống đã lìa sự uể oải và đờ đẫn, có tri giác về ánh sáng, "
    "tỉnh thức và hiểu biết rõ ràng, làm trong sạch hoàn toàn tâm khỏi sự uể oải và đờ đẫn",
    "sau khi dứt bỏ sự xao động và hối tiếc, vị ấy sống không xao động, có tâm đã lắng dịu hoàn toàn ở nơi "
    "bản thân, làm trong sạch hoàn toàn tâm khỏi sự xao động và hối tiếc",
    "sau khi dứt bỏ sự hoài nghi, vị ấy sống đã vượt qua sự hoài nghi, không còn băn khoăn đối với các hiện "
    "tượng thiện, làm trong sạch hoàn toàn tâm khỏi sự hoài nghi",
]                                                                                                      # (pi-2)
JHANA = ("Sau khi dứt bỏ năm chướng ngại này, là những thứ làm vẩn đục tâm, làm suy yếu trí tuệ, vị ấy hoàn toàn "
         "tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, chứng nhập và an trú tầng thiền thứ nhất, "
         "có sự hướng tâm và sự duy trì tâm, có sự hân hoan và hạnh phúc sinh từ sự tách biệt; nhờ sự hướng tâm "
         "và sự duy trì tâm lắng xuống, vị ấy chứng nhập và an trú tầng thiền thứ hai")                  # (pi-2)
SAMAHITE = ("Khi tâm đã an định như vậy, trong sạch, trong sáng, không còn vết nhơ, đã lìa những thứ làm vẩn đục, "
            "đã trở nên mềm dẻo, dễ vận dụng, vững vàng, đạt đến sự bất động, vị ấy dẫn tâm đến sự hiểu biết về "
            "sự diệt tận các ô nhiễm.")                                                          # = ch5 SAMAHITA + K_ASAVA
#   So evaṃ samāhite citte parisuddhe pariyodāte anaṅgaṇe vigatūpakkilese mudubhūte kammaniye ṭhite āneñjappatte
#   āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti.
ASAVA_TRUTHS = ("hiểu rõ đúng như thật: “Đây là các ô nhiễm”, hiểu rõ đúng như thật: “Đây là sự phát sinh của các "
                "ô nhiễm”, hiểu rõ đúng như thật: “Đây là sự chấm dứt các ô nhiễm”, hiểu rõ đúng như thật: “Đây là "
                "cách thực hành dẫn đến sự chấm dứt các ô nhiễm”")                                 # = ch5
#   "ime āsavā"ti yathābhūtaṃ pajānāti, … "ayaṃ āsavanirodhagāminī paṭipadā"ti yathābhūtaṃ pajānāti
VIMUCCATI = ("Khi vị ấy biết như vậy, thấy như vậy, tâm được giải thoát khỏi ô nhiễm dục lạc, tâm được giải thoát "
             "khỏi ô nhiễm hiện hữu, tâm được giải thoát khỏi ô nhiễm vô minh. Khi đã được giải thoát, có sự "
             "hiểu biết: “Đã được giải thoát”. Vị ấy hiểu rõ: “Sự sinh đã được diệt tận, đời sống tu hành trong sạch "
             "đã được sống trọn, việc cần làm đã được làm xong, không còn gì khác cho trạng thái hiện hữu này nữa”.")
#   = ch5 ^4-185 wording
#   Tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati, … Vimuttasmiṃ vimuttamiti ñāṇaṃ hoti.
#   "Khīṇā jāti, vusitaṃ brahmacariyaṃ, kataṃ karaṇīyaṃ, nāparaṃ itthattāyā"ti pajānāti.

# ---------------------------------------------------------------------------------------------------------------
# ^4-199 .. ^4-201 (the ascetic practices)
# ---------------------------------------------------------------------------------------------------------------
PRAISED = "với ý nghĩ “Điều này được chư Phật và các đệ tử của Đức Phật khen ngợi”"   # "vaṇṇitaṃ buddhehi buddhasāvakehī"ti
BUDDHA_SAVAKA = "chư Phật và các đệ tử của Đức Phật"                                   # (pi-2)
PAPICCHO = "có ước muốn xấu xa, bị mong muốn chi phối"   # pāpiccho icchāpakato (pi-2 «có ước muốn xấu xa»; icchā termbase)
REASONS = ("chỉ dựa vào sự ít ước muốn{0}, chỉ dựa vào sự biết đủ, chỉ dựa vào sự giảm trừ phiền não, "
           "chỉ dựa vào việc lấy điều này làm mục đích{1}")
#   appicchataṃyeva nissāya santuṭṭhiṃyeva nissāya sallekhaṃyeva nissāya idamatthitaṃyeva nissāya
AGGO = "hàng đầu, cao quý nhất, đứng đầu{0}, tối thượng và ưu tú nhất"   # aggo ca seṭṭho ca pāmokkho ca uttamo ca pavaro ca
MILK = ("Giống như từ bò có sữa, từ sữa có sữa đông, từ sữa đông có bơ tươi{0}, từ bơ tươi có bơ lỏng, từ bơ lỏng "
        "có phần tinh túy của bơ lỏng, phần tinh túy của bơ lỏng được gọi là hàng đầu trong số ấy")
#   Seyyathāpi nāma gavā khīraṃ, khīramhā dadhi, … sappimaṇḍaṃ tattha aggamakkhāyati

REUSED = [  # (Vietnamese string, book)
    (REQUISITES, "2"), (KUSALA, "1"), (RETURN, "2"), (GATA, "2"), (SENASANA, "2"), (NISIDATI, "2"),
    (JHANA, "2"), (BUDDHA_SAVAKA, "2"), ("có ước muốn xấu xa", "2"),
    ("ô nhiễm dục lạc", "1"), ("ô nhiễm hiện hữu", "1"), ("ô nhiễm vô minh", "1"),
    ("các hiện tượng thấp kém", "1"), ("các hiện tượng ưu việt", "1"), ("các hiện tượng đen tối", "1"),
    ("các hiện tượng trong sáng", "1"), ("sữa, sữa đông, bơ lỏng, bơ tươi", "1"),
    ("tầng thiền thứ ba", "1"), ("tầng thiền thứ tư", "1"), ("với ý nghĩ “", "1"),
    ("Đây là tám lỗi của con người.", "2"),
] + [(x, "2") for x in NIV]

NAMES_USED = {k: S.NAME[k] for k in (
    "ārabhati ca vippaṭisārī ca hoti … nappajānāti", "ārabhati na vippaṭisārī ca hoti … nappajānāti",
    "nārabhati vippaṭisārī ca hoti … nappajānāti", "nārabhati na vippaṭisārī hoti … nappajānāti",
    "datvā avajānāti", "saṃvāsena avajānāti", "ādheyyamukho hoti", "lolo hoti", "mando momūho hoti",
    "pañca yodhājīvūpamā puggalā", "pañca piṇḍapātikā", "pañca khalupacchābhattikā", "pañca ekāsanikā",
    "pañca paṃsukūlikā", "pañca tecīvarikā", "pañca āraññikā", "pañca rukkhamūlikā", "pañca abbhokāsikā",
    "pañca nesajjikā", "pañca yathāsanthatikā", "pañca sosānikā")}
EXPECTED = {  # the approved strings, retyped here only to catch drift in the sample
    "datvā avajānāti": "người cho rồi khinh thường", "mando momūho hoti": "người chậm hiểu, mê muội",
    "pañca yodhājīvūpamā puggalā": "năm hạng người giống như chiến binh",
    "pañca piṇḍapātikā": "năm hạng người chỉ ăn thức ăn khất thực",
    "pañca sosānikā": "năm hạng người sống ở bãi tha ma",
}
PANCAKA1 = ["ārabhati ca vippaṭisārī ca hoti … nappajānāti", "ārabhati na vippaṭisārī ca hoti … nappajānāti",
            "nārabhati vippaṭisārī ca hoti … nappajānāti", "nārabhati na vippaṭisārī hoti … nappajānāti"]


def bare(name):
    """Pañcaka (1) name without «có người»: the definition Pāli has no atthi / ekacco (coordinator rule)."""
    assert name.startswith("có người "), name
    return name[len("có người "):]


def pred(i, fail):
    """Stage i (0-4) of the warrior / monk: what he endures and where he fails."""
    endured = ", ".join(f"chịu được {x}" for x in STAGES[:i])
    if i == 4:
        return endured
    failpart = HATA if i == 3 else f"{TRIGGER[i]} đã {SINK}, {fail}"
    return failpart if i == 0 else f"{endured}, nhưng {failpart}"


# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = [S.seg(S.H_CHAPTER[5] + " ^4-1-5-0")]

    # ^4-191
    speech = [
        (f"{atthi(False)}{V_ARABBHAJA}, và {vaddhanti(False)}. {SADHU}, sau khi dứt bỏ {ARAMBHAJA}, sau khi xua tan "
         f"{VIPPATISARAJA}, {BHAVETU}."),
        f"{atthi(False)}, và {vaddhanti(True)}. {SADHU}, sau khi dứt bỏ {ARAMBHAJA}, {BHAVETU}.",
        f"{atthi(True)}, và {vaddhanti(False)}. {SADHU}, sau khi xua tan {VIPPATISARAJA}, {BHAVETU}.",
        f"{atthi(True)}, và {vaddhanti(True)}. {SADHU} {BHAVETU}.",
    ]
    lines = []
    for n, (key, sp) in enumerate(zip(PANCAKA1, speech)):
        who = bare(N(key))
        if n == 3:  # ^4-191 line 4: "yatthassa te pāpakā akusalā dhammā" (no uppannā), translated as written
            who = who.replace("bất thiện đã sinh khởi của", "bất thiện của", 1)
        lines.append(f"{TATRA} {who}, {VACANIYO} “{sp} {SAMASAMO}”.")
    lines[3] += " " + CATTARO
    lines[3] += " ^4-191"
    segs.append(S.seg(*lines))

    # ^4-192
    qk, ev = S.q_kathanca, S.evam
    n1, n2, n3, n4, n5 = (N(k) for k in ("datvā avajānāti", "saṃvāsena avajānāti", "ādheyyamukho hoti",
                                          "lolo hoti", "mando momūho hoti"))
    segs.append(S.seg(
        f"{qk(n1)} {S.IDHEKACCO} cho một người nào đó {REQUISITES}, rồi người ấy nghĩ như vầy – “Tôi cho, "
        f"người này{V_AYAM_PANA} nhận”, và sau khi cho, người ấy khinh thường người kia. {ev(n1)}",
        f"{qk(n2)} {S.IDHEKACCO} sống chung cùng với một người nào đó hai hoặc ba năm, rồi vì sống chung mà khinh "
        f"thường người kia. {ev(n2)}",
        f"{qk(n3)} {S.IDHEKACCO}, khi lời khen hoặc lời chê về người khác đang được nói ra, thì nhanh chóng tin ngay. "
        f"{ev(n3)}",
        f"{qk(n4)} {S.IDHEKACCO} có niềm tin chóng qua, lòng sùng kính chóng qua, lòng quý mến chóng qua, lòng tin "
        f"trong sáng chóng qua. {ev(n4)}",
        f"{qk(n5)} {S.IDHEKACCO} không biết {KUSALA}, không biết các hiện tượng có lỗi và không có lỗi, không biết "
        f"các hiện tượng thấp kém và ưu việt, không biết các hiện tượng đen tối và trong sáng đối lập nhau. "
        f"{ev(n5)} ^4-192"))

    # ^4-193: the five warriors
    yodha = N("pañca yodhājīvūpamā puggalā")
    w = []
    for i in range(5):
        p = pred(i, OTARITUM)
        if i == 0:
            p = p.replace("không đứng vững", "không đứng vững" + V_SATTHAMBHATI, 1)
        if i == 2:
            p = p.replace("nghe tiếng hò hét", "nghe tiếng hò hét" + V_USSADANA, 1)
        head = (f"Ở đây, {yodha} là những ai? Có năm loại chiến binh – ở đời này, có chiến binh" if i == 0
                else "Lại nữa, ở đời này, có chiến binh")
        win = f". Người ấy, {WIN}." if i == 4 else "."
        t = f"{head} {p}{win} {EVARUPO_YODHA} Chiến binh {ORD[i]} này {SANTO_LOKE}."
        if i == 4:
            t += f" Năm loại chiến binh này {SANTO_LOKE}. ^4-193"
        w.append(t)
    segs.append(S.seg(*w))

    # ^4-194 .. ^4-198: the five monks
    person = yodha.replace("năm hạng người", "người {}", 1)       # «người thứ N giống như chiến binh»

    def simile(i, extra=""):
        p = pred(i, OTARITUM)
        if i == 4:
            p += ", và " + WIN
        return (f"Giống như chiến binh ấy {p}, {TATHUPAMO}. {EVARUPO} {S.cap(person.format(ORD[i]))} này "
                f"{SANTO_BHIKKHU}.{extra}")

    # ^4-194
    p0 = pred(0, MONK_FAIL).replace("duy trì", "duy trì" + V_SANTANETUM, 1).replace("bày tỏ", "bày tỏ" + V_AVIKATVA, 1)
    segs.append(S.seg(
        f"Cũng như vậy, {yodha} này {SANTO_BHIKKHU}. Năm hạng người ấy là những ai? Ở đời này, có vị tỳ-khưu {p0}. "
        f"Điều gì là {STAGES[0]} đối với vị ấy? Ở đây, vị tỳ-khưu nghe nói – “{HEAR}”. Sau khi nghe điều ấy, vị ấy "
        f"{SINK}, {MONK_FAIL}. Đây là {STAGES[0]} đối với vị ấy.",
        simile(0) + " ^4-194"))
    # ^4-195
    segs.append(S.seg(
        f"Lại nữa, ở đời này, có vị tỳ-khưu {pred(1, MONK_FAIL)}. Điều gì là {STAGES[1]} đối với vị ấy? Ở đây, vị "
        f"tỳ-khưu {S.NA_HEVA_KHO} nghe nói – “{HEAR}”, nhưng tự mình{V_SAMAM} thấy {SEE}. Sau khi thấy người nữ ấy, "
        f"vị ấy {SINK}, {MONK_FAIL}. Đây là {STAGES[1]} đối với vị ấy.",
        simile(1) + " ^4-195"))
    # ^4-196
    hasa1 = HASA.replace("cười cợt", "cười cợt" + V_UHASATI, 1)
    segs.append(S.seg(
        f"Lại nữa, ở đời này, có vị tỳ-khưu {pred(2, MONK_FAIL)}. Điều gì là {STAGES[2]} đối với vị ấy? "
        f"{IDHA_GATA}, {hasa1} vị ấy. Khi bị phụ nữ {HASA}, vị ấy {SINK}, {MONK_FAIL}. Đây là {STAGES[2]} đối với "
        "vị ấy.",
        simile(2) + " ^4-196"))
    # ^4-197
    segs.append(S.seg(
        f"Lại nữa, ở đời này, có vị tỳ-khưu {pred(3, MONK_FAIL)}. Điều gì là {STAGES[3]} đối với vị ấy? "
        f"{IDHA_GATA}, {NISI} vị ấy. Khi bị phụ nữ {NISI}, vị ấy không từ bỏ sự tu học, không bày tỏ sự yếu kém, mà "
        f"hưởng thụ hành vi dâm dục. Đây là {STAGES[3]} đối với vị ấy.",
        simile(3) + " ^4-197"))
    # ^4-198
    vijaya = "sự chiến thắng trong trận chiến"
    segs.append(S.seg(
        f"Lại nữa, ở đời này, có vị tỳ-khưu {pred(4, MONK_FAIL)}. Vị ấy, {WIN}. Điều gì là {vijaya} đối với vị ấy? "
        f"{IDHA_GATA}, {NISI} vị ấy. Khi bị phụ nữ {NISI}, vị ấy gỡ mình ra, thoát ra, rồi bỏ đi đến nơi nào mình "
        "muốn.",
        f"{SENASANA}. {NISIDATI} " + "; ".join(NIV) + ".",
        f"{JHANA}… tầng thiền thứ ba… tầng thiền thứ tư.",
        f"{SAMAHITE} Vị ấy {S.TRUTHS}, {ASAVA_TRUTHS}.",
        f"{VIMUCCATI} Đây là {vijaya} đối với vị ấy. "
        + simile(4, f" {S.cap(yodha)} này {SANTO_BHIKKHU}.") + " ^4-198"))

    # ^4-199 .. ^4-201
    def dhuta(key, variants, closer):
        name = N(key)
        vp = name.replace("năm hạng người ", "", 1)
        va, vi, vm, vn = variants
        r1, r0 = REASONS.format(va, vi), REASONS.format("", "")
        best = (f"người {vp} nào {r0} mà {vp}, thì người này là {{}} trong {name} này")
        l1 = (f"Ở đây, {name} là những ai? Có người do chậm hiểu, do mê muội mà {vp}; có người {PAPICCHO} mà {vp}; "
              f"có người do điên loạn, do tâm tán loạn mà {vp}; có người {PRAISED} mà {vp}; nhưng cũng có người {r1} "
              f"mà {vp}. Trong số đó, " + best.format(AGGO.format(vm)) + ".")
        l2 = (MILK.format(vn) + "; cũng như vậy, " + best.format(AGGO.format("")) + f". Đây là {name}.")
        return [l1, l2 + ("" if closer else " ^4-199")]

    segs.append(S.seg(*dhuta("pañca piṇḍapātikā", (V_APPICCHA, V_IDAMATTHITA, V_MOKKHO, V_NONITA), False)))
    rest = [N(k) for k in ("pañca khalupacchābhattikā", "pañca ekāsanikā", "pañca paṃsukūlikā", "pañca tecīvarikā",
                           "pañca āraññikā", "pañca rukkhamūlikā", "pañca abbhokāsikā", "pañca nesajjikā",
                           "pañca yathāsanthatikā")]
    # ^4-200: "rukkhamūlikā …pe…" has a stray space before …pe… (rendered without it); final "…pe…." = "…"
    segs.append(S.seg(f"Ở đây, {rest[0]} là những ai… " + "… ".join(rest[1:]) + "… ^4-200"))
    segs.append(S.seg(*dhuta("pañca sosānikā", ("", "", "", ""), True), S.CLOSER_CHAPTER[5] + " ^4-201"))
    return segs


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
        if k in PANCAKA1:
            v = bare(v)
            if k.startswith("nārabhati na"):
                v = v.replace("bất thiện đã sinh khởi của", "bất thiện của", 1)
        assert v.lower() in text.lower(), ("name not used verbatim", k, v)
    S.write(OUT, segs)


if __name__ == "__main__":
    main()
