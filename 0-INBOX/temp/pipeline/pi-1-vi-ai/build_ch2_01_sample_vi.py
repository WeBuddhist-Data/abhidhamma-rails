"""Build the Vietnamese plain zero-shot SAMPLE of pi-1 ch.2 opening (^1-1-0 ... ^1-57).

usage: python -I -X utf8 build_ch2_01_sample_vi.py
All recurring strings are fixed constants below, so every repeat is byte-identical.
Importing this module does not write the file. Exposes NAMES, STRINGS (Pāli = Vietnamese),
the word lists W_* (one Vietnamese item per Pāli word, for variant insertion), FRAMES and the
frame functions (Q, A, QA, T, KAYA, CITTA, JIVITA, SHAME, LIST_ITEM, YEVAPANA) for later chapters.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_matika_vi import QUESTION, ANSWER, V  # noqa: E402

PALI = HERE.parent / "pi-1-ru" / "ref" / "ch2-01-pali-1-122.md"  # read-only reference slice
OUT = HERE / "ch2-01-sample.md"

DASH = "–"  # the en dash used by the Pāli source; only where the Pāli has one

KUSALA = ("1-M1-1", "a")      # các hiện tượng thiện
AKUSALA = ("1-M1-1", "b")     # các hiện tượng bất thiện
ABYAKATA = ("1-M1-1", "c")    # các hiện tượng không xác định về mặt đạo đức

# ---- headings ------------------------------------------------------------------------
H_CH2 = "### Phần về sự sinh khởi của tâm"
H_KAMA_KUSALA = "#### Tâm thiện thuộc cõi dục lạc"
H_PADA = "##### Phân tích từng từ"
END_PADA = "Phân tích từng từ."
END_BHANA1 = "Phần tụng đọc thứ nhất."

# ---- names of the factors (Pāli = Vietnamese) -------------------------------------------
KAYA_N = "của thân tinh thần"  # kāya- in kāyapassaddhi … kāyujukatā (the three mental aggregates)
CITTA_N = "của tâm"


def pair(head):
    """(kāya-X, citta-X) names from the head noun."""
    return f"{head} {KAYA_N}", f"{head} {CITTA_N}"


_PASS = pair("sự an tịnh")
_LAHU = pair("sự nhẹ nhàng")
_MUDU = pair("sự mềm mại")
_KAMM = pair("sự dễ vận dụng")
_PAGU = pair("sự thuần thục")
_UJU = pair("sự ngay thẳng")

NAMES = {
    "phasso": "sự tiếp xúc",
    "vedanā": "cảm giác",
    "saññā": "tri giác",
    "cetanā": "chủ ý",
    "cittaṃ": "tâm",
    "vitakko": "sự hướng tâm",
    "vicāro": "sự duy trì tâm",
    "pīti": "sự hân hoan",
    "sukhaṃ": "hạnh phúc",
    "cittassekaggatā": "sự nhất tâm",
    "saddhindriyaṃ": "năng lực niềm tin",
    "vīriyindriyaṃ": "năng lực tinh tấn",
    "satindriyaṃ": "năng lực tỉnh thức",
    "samādhindriyaṃ": "năng lực định tâm",
    "paññindriyaṃ": "năng lực trí tuệ",
    "manindriyaṃ": "năng lực ý",
    "somanassindriyaṃ": "năng lực niềm vui",
    "jīvitindriyaṃ": "năng lực sống",
    "sammādiṭṭhi": "quan điểm đúng đắn",
    "sammāsaṅkappo": "tư duy đúng đắn",
    "sammāvāyāmo": "nỗ lực đúng đắn",
    "sammāsati": "tỉnh thức đúng đắn",
    "sammāsamādhi": "định tâm đúng đắn",
    "saddhābalaṃ": "sức mạnh niềm tin",
    "vīriyabalaṃ": "sức mạnh tinh tấn",
    "satibalaṃ": "sức mạnh tỉnh thức",
    "samādhibalaṃ": "sức mạnh định tâm",
    "paññābalaṃ": "sức mạnh trí tuệ",
    "hiribalaṃ": "sức mạnh biết hổ thẹn",
    "ottappabalaṃ": "sức mạnh biết ghê sợ tội lỗi",
    "alobho": "sự không tham lam",
    "adoso": "sự không sân hận",
    "amoho": "sự không si mê",
    "anabhijjhā": "sự không thèm muốn",
    "abyāpādo": "sự không ác ý",
    "hirī": "sự biết hổ thẹn",
    "ottappaṃ": "sự biết ghê sợ tội lỗi",
    "kāyapassaddhi": _PASS[0], "cittapassaddhi": _PASS[1],
    "kāyalahutā": _LAHU[0], "cittalahutā": _LAHU[1],
    "kāyamudutā": _MUDU[0], "cittamudutā": _MUDU[1],
    "kāyakammaññatā": _KAMM[0], "cittakammaññatā": _KAMM[1],
    "kāyapāguññatā": _PAGU[0], "cittapāguññatā": _PAGU[1],
    "kāyujukatā": _UJU[0], "cittujukatā": _UJU[1],
    "sati": "sự tỉnh thức",
    "sampajaññaṃ": "sự hiểu biết rõ ràng",
    "samatho": "sự tĩnh lặng",
    "vipassanā": "sự thấu suốt",
    "paggāho": "sự dốc sức",
    "avikkhepo": "sự không tán loạn",
}
N = NAMES

# ---- fixed synonym strings ------------------------------------------------------------
# Each list has one Vietnamese item per Pāli word, so variant brackets can be attached to the
# right word (see VAR below). The joined form is the string reused verbatim.
TAJJA = "sinh từ sự tiếp xúc của yếu tố ý thức tương ứng"   # tajjāmanoviññāṇadhātusamphassaja-
G_KAYA = "nơi khối cảm giác, khối tri giác và khối tạo tác"   # vedanā-, saññā-, saṅkhārakkhandhassa
G_CITTA = "nơi khối thức"                                     # viññāṇakkhandhassa
G_JIVITA = "ở các hiện tượng phi vật chất ấy"                 # tesaṃ arūpīnaṃ dhammānaṃ
ROOT = "gốc rễ thiện"                                         # kusalamūlaṃ

W = {
    "phasso phusanā saṃphusanā saṃphusitattaṃ":
        ["sự tiếp xúc", "sự chạm", "sự chạm đến", "trạng thái đã chạm đến"],
    "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        ["sự khoan khoái trong tâm", "sự dễ chịu trong tâm",
         "cảm nhận khoan khoái và dễ chịu sinh từ sự tiếp xúc của tâm",
         "cảm giác khoan khoái và dễ chịu sinh từ sự tiếp xúc của tâm"],
    "saññā sañjānanā sañjānitattaṃ":
        ["tri giác", "sự nhận ra", "trạng thái đã nhận ra"],
    "cetanā sañcetanā cetayitattaṃ":
        ["chủ ý", "sự cố ý", "trạng thái đã cố ý"],
    "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu":
        ["tâm", "ý", "tâm trí", "tấm lòng", "sự sáng ngời", "ý", "lĩnh vực ý", "năng lực ý",
         "thức", "khối thức", "yếu tố ý thức tương ứng"],
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo":
        ["suy nghĩ", "sự hướng tâm", "tư duy", "sự gắn tâm", "sự gắn chặt tâm",
         "sự đặt tâm vào đối tượng", "tư duy đúng đắn"],
    "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā":
        ["sự chuyển động của tâm", "sự duy trì tâm", "sự duy trì tâm liên tục", "sự duy trì tâm sát gần",
         "sự gắn kết liên tục của tâm với đối tượng", "sự theo dõi sát đối tượng"],
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa":
        ["sự hân hoan", "sự phấn khởi", "sự vui vẻ", "sự vui thích", "sự tươi cười", "sự rạng rỡ",
         "sự mãn nguyện", "sự phấn chấn", "sự hài lòng của tâm"],
    "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ sammāsamādhi":
        ["sự ổn định của tâm", "sự vững vàng", "sự vững chãi", "sự không phân tán", "sự không tán loạn",
         "trạng thái tâm trí không phân tán", "sự tĩnh lặng", "năng lực định tâm", "sức mạnh định tâm",
         "định tâm đúng đắn"],
    "saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ":
        ["niềm tin", "sự tin tưởng", "sự tin chắc", "lòng tin sâu sắc", "niềm tin", "năng lực niềm tin",
         "sức mạnh niềm tin"],
    "cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā "
    "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo":
        ["sự khởi động tinh tấn trong tâm", "sự dấn bước", "sự xông pha", "sự gắng sức", "sự nỗ lực",
         "sự hăng hái", "sự bền chí", "sức bền", "sự kiên trì", "sự xông pha không lơi lỏng",
         "sự không buông bỏ ý muốn", "sự không buông gánh", "sự dốc sức gánh vác", "sự tinh tấn",
         "năng lực tinh tấn", "sức mạnh tinh tấn", "nỗ lực đúng đắn"],
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati":
        ["sự tỉnh thức", "sự nhớ lại", "sự hồi tưởng", "sự tỉnh thức", "sự ghi nhớ", "sự gìn giữ trong trí nhớ",
         "sự không hời hợt", "sự không quên lãng", "sự tỉnh thức", "năng lực tỉnh thức", "sức mạnh tỉnh thức",
         "tỉnh thức đúng đắn"],
    "paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā "
    "paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
    "amoho dhammavicayo sammādiṭṭhi":
        ["trí tuệ", "sự hiểu rõ", "sự tìm hiểu", "sự tìm hiểu kỹ", "sự tìm hiểu các hiện tượng",
         "sự nhận xét", "sự nhận diện", "sự nhận diện chính xác", "sự thông thái", "sự khéo léo",
         "sự tinh tường", "sự phân biệt sáng suốt", "sự suy tư", "sự khảo sát", "sự sâu rộng",
         "sự thông minh", "sự dẫn dắt", "sự thấu suốt", "sự hiểu biết rõ ràng", "cây roi thúc", "trí tuệ",
         "năng lực trí tuệ", "sức mạnh trí tuệ", "thanh gươm trí tuệ", "lâu đài trí tuệ", "ánh sáng trí tuệ",
         "hào quang trí tuệ", "ngọn đuốc trí tuệ", "viên ngọc trí tuệ", "sự không si mê",
         "sự tìm hiểu các hiện tượng", "quan điểm đúng đắn"],
    "āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        ["tuổi thọ", "sự tồn tại", "sự tiếp diễn", "sự kéo dài", "sự vận động", "sự tiến triển",
         "sự gìn giữ", "sự sống", "năng lực sống"],
    "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ":
        ["sự không tham lam", "sự không khởi lòng tham", "trạng thái không khởi lòng tham",
         "sự không say đắm", "sự không bị cuốn hút", "trạng thái không bị cuốn hút", "sự không thèm muốn",
         "sự không tham lam", ROOT],
    "adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ":
        ["sự không sân hận", "sự không khởi sân", "trạng thái không khởi sân", "sự không ác ý",
         "sự không thù hằn", "sự không sân hận", ROOT],
    "passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ":
        ["sự an tịnh", "sự an tịnh hoàn toàn", "sự lắng dịu", "sự lắng dịu hoàn toàn",
         "trạng thái đã lắng dịu hoàn toàn"],
    "lahutā lahupariṇāmatā adandhanatā avitthanatā":
        ["sự nhẹ nhàng", "sự chuyển đổi nhanh nhẹn", "sự không chậm chạp", "sự không trì trệ"],
    "mudutā maddavatā akakkhaḷatā akathinatā":
        ["sự mềm mại", "sự mềm mỏng", "sự không thô cứng", "sự không cứng nhắc"],
    "kammaññatā kammaññattaṃ kammaññabhāvo":
        ["sự dễ vận dụng", "trạng thái dễ vận dụng", "tính chất dễ vận dụng"],
    "paguṇatā paguṇattaṃ paguṇabhāvo":
        ["sự thuần thục", "trạng thái thuần thục", "tính chất thuần thục"],
    "ujutā ujukatā ajimhatā avaṅkatā akuṭilatā":
        ["sự thẳng", "sự ngay thẳng", "sự không quanh co", "sự không cong queo", "sự không vặn vẹo"],
}
# word lists must match the Pāli word count (the sāta string and «cetaso abhiniropanā» /
# «cittassa anusandhānatā» / «attamanatā cittassa» / «cittassa ṭhiti» are phrase units)
_UNITS = {"cetasikaṃ sātaṃ": 4, "takko": 7, "cāro": 6, "pīti": 9, "cittassa": 10, "cetasiko": 17}
for k, v in W.items():
    n = _UNITS.get(" ".join(k.split()[:2]), _UNITS.get(k.split()[0], len(k.split())))
    assert len(v) == n, (k, len(v), n)

STRINGS = {k: ", ".join(v) for k, v in W.items()}
# hirī / ottappa: a clause, not a list
STRINGS["hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"] = (
    "người ta hổ thẹn với điều đáng hổ thẹn, hổ thẹn khi để các hiện tượng xấu ác, bất thiện xảy ra nơi mình")
STRINGS["ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"] = (
    "người ta ghê sợ điều đáng ghê sợ, ghê sợ khi để các hiện tượng xấu ác, bất thiện xảy ra nơi mình")

S = {k.split()[0] if not k.startswith("cetasikaṃ sātaṃ") else "sāta": v for k, v in STRINGS.items()}
WL = {k.split()[0] if not k.startswith("cetasikaṃ sātaṃ") else "sāta": v for k, v in W.items()}
assert len(S) == len(STRINGS)
S_PHASSA, S_SUKHA, S_SANNA, S_CETANA = S["phasso"], S["sāta"], S["saññā"], S["cetanā"]
S_CITTA, S_VITAKKA, S_VICARA, S_PITI = S["cittaṃ"], S["takko"], S["cāro"], S["pīti"]
S_SAMADHI, S_SADDHA, S_VIRIYA, S_SATI = S["cittassa"], S["saddhā"], S["cetasiko"], S["sati"]
S_PANNA, S_JIVITA, S_HIRI, S_OTTAPPA = S["paññā"], S["āyu"], S["hirīyati"], S["ottappati"]
S_ALOBHA, S_ADOSA, S_PASSADDHI = S["alobho"], S["adoso"], S["passaddhi"]
S_LAHUTA, S_MUDUTA, S_KAMMANNATA, S_PAGUNATA, S_UJUTA = (
    S["lahutā"], S["mudutā"], S["kammaññatā"], S["paguṇatā"], S["ujutā"])


def VAR(key, marks):
    """The string `key` (first Pāli word) with variant brackets after the given word indexes.
    marks: {index: (kind, sigla, text)}"""
    words = list(WL[key])
    for i, (kind, sigla, text) in marks.items():
        words[i] += V(kind, sigla, text)
    return ", ".join(words)


# variant-bearing forms (first occurrences in ^1-5, ^1-13, ^1-19, ^1-33, ^1-40)
S_CETANA_V = VAR("cetanā", {2: ("p", "Syā.", "sañcetayitattaṃ")})
S_VIRIYA_V = VAR("cetasiko", {0: ("s", "Sī., Syā.", "viriyārambho"), 6: ("s", "Sī.", "ussoḷhi")})
S_JIVITA_V = VAR("āyu", {4: ("s", "Sī.", "irīyanā")})
S_ADOSA_V = VAR("adoso", {2: ("s", "Syā.", "adūsanā adūsitattaṃ")})
S_PASSADDHI_V = VAR("passaddhi", {1: ("s", "Sī., Syā.", "paṭippassaddhi"),
                                  3: ("s", "Sī., Syā.", "paṭippassambhanā"),
                                  4: ("s", "Sī., Syā.", "paṭippassambhitattaṃ")})
for a, b, n in ((S_CETANA, S_CETANA_V, 1), (S_VIRIYA, S_VIRIYA_V, 2), (S_JIVITA, S_JIVITA_V, 1),
                (S_ADOSA, S_ADOSA_V, 1), (S_PASSADDHI, S_PASSADDHI_V, 3)):
    assert b.count("[") == n and re.sub(r" \[[^\]]*\]", "", b) == a, b

# ---- frames ----------------------------------------------------------------------------
OPEN_KAMA_KUSALA = "Vào lúc tâm thiện thuộc cõi dục lạc sinh khởi"
ACC_SOMA_NANA = "có niềm vui đi kèm, gắn liền với hiểu biết"
ARAMMANA = ("lấy hình sắc, hoặc âm thanh, hoặc mùi, hoặc vị, hoặc vật xúc chạm, "
            "hoặc đối tượng của ý, hay bất cứ thứ gì làm đối tượng")
TASMIM = "vào lúc ấy"  # tasmiṃ samaye
THEN = "thì vào lúc ấy"  # tasmiṃ samaye after the yasmiṃ samaye clause
YEVAPANA_BODY = ("bất cứ hiện tượng phi vật chất nào khác, sinh khởi tùy thuộc vào điều kiện, "
                 "có mặt vào lúc ấy")


def YEVAPANA(item=KUSALA):
    """'ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā X.'
    (without the opening «hoặc»)"""
    return f"{YEVAPANA_BODY} {DASH} {ANSWER(item)}"


def Q(key):
    """'Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti?'"""
    return f"Vào lúc ấy, {N[key]} là gì?"


def A(s, key, mid=""):
    """'Yo/Yā/Yaṃ tasmiṃ samaye [mid] S – ayaṃ/idaṃ tasmiṃ samaye X hoti.'"""
    return f"Điều có mặt {TASMIM}{mid}, tức là {s} {DASH} đây là {N[key]} {TASMIM}."


def QA(key, s, mid="", end="."):
    a = A(s, key, mid)
    if end != ".":
        a = a[:-1] + end
    return Q(key) + " " + a


def T(key, s):
    """with tajjāmanoviññāṇadhātusamphassaja-"""
    return QA(key, s, " và " + TAJJA)


def KAYA(key, s):
    return QA(key, s, " " + G_KAYA)


def CITTA(key, s):
    return QA(key, s, " " + G_CITTA)


def JIVITA(key, s):
    """'Yo tesaṃ arūpīnaṃ dhammānaṃ S – idaṃ tasmiṃ samaye X hoti.' (no tasmiṃ samaye at the start)"""
    return Q(key) + f" Điều có {G_JIVITA}, tức là {s} {DASH} đây là {N[key]} {TASMIM}."


def SHAME(key, s):
    """'Yaṃ tasmiṃ samaye hirīyati … / ottappati … – idaṃ/ayaṃ tasmiṃ samaye X hoti.'"""
    return Q(key) + f" Việc {TASMIM} {s} {DASH} đây là {N[key]} {TASMIM}."


def LIST_ITEM(key, var=""):
    """'X hoti' inside the list of ^1-1: «có X»."""
    return f"có {N[key]}{var}"


FRAMES = {
    "Katame dhammā kusalā?": QUESTION(KUSALA),
    "ime dhammā kusalā (after the Pāli –)": ANSWER(KUSALA),
    "Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti?": "Vào lúc ấy, X là gì?",
    "Yo/Yā/Yaṃ tasmiṃ samaye S – ayaṃ/idaṃ tasmiṃ samaye X hoti.":
        f"Điều có mặt {TASMIM}, tức là S {DASH} đây là X {TASMIM}.",
    "Yā/Yaṃ tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajā/-jaṃ S – ayaṃ tasmiṃ samaye X hoti.":
        f"Điều có mặt {TASMIM} và {TAJJA}, tức là S {DASH} đây là X {TASMIM}.",
    "Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa S – ayaṃ tasmiṃ samaye X hoti.":
        f"Điều có mặt {TASMIM} {G_KAYA}, tức là S {DASH} đây là X {TASMIM}.",
    "Yā tasmiṃ samaye viññāṇakkhandhassa S – ayaṃ tasmiṃ samaye X hoti.":
        f"Điều có mặt {TASMIM} {G_CITTA}, tức là S {DASH} đây là X {TASMIM}.",
    "Yo tesaṃ arūpīnaṃ dhammānaṃ S – idaṃ tasmiṃ samaye X hoti.":
        f"Điều có {G_JIVITA}, tức là S {DASH} đây là X {TASMIM}.",
    "Yaṃ tasmiṃ samaye hirīyati… / ottappati… – idaṃ/ayaṃ tasmiṃ samaye X hoti.":
        f"Việc {TASMIM} S {DASH} đây là X {TASMIM}.",
    "Ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā.":
        "Hoặc " + YEVAPANA(),
    "Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti": OPEN_KAMA_KUSALA,
    "somanassasahagataṃ ñāṇasampayuttaṃ": ACC_SOMA_NANA,
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": ARAMMANA,
    "tasmiṃ samaye X hoti, Y hoti, … (after the yasmiṃ samaye clause)": f"{THEN} có X, có Y, …",
    "(in ^1-1, after the list) ; ye vā pana …": "; hoặc " + YEVAPANA(),
    "tasmiṃ samaye": TASMIM,
    "ayaṃ / idaṃ / ime (in the answer)": "đây là",
    "kusalamūlaṃ (closing a root string)": ROOT,
}

# ---- ^1-1 ------------------------------------------------------------------------------
LIST_1_1 = [
    ("phasso", ""), ("vedanā", ""), ("saññā", ""), ("cetanā", ""), ("cittaṃ", ""), ("vitakko", ""),
    ("vicāro", ""), ("pīti", ""), ("sukhaṃ", ""), ("cittassekaggatā", ""), ("saddhindriyaṃ", ""),
    ("vīriyindriyaṃ", V("s", "Sī., Syā.", "viriyindriyaṃ")), ("satindriyaṃ", ""), ("samādhindriyaṃ", ""),
    ("paññindriyaṃ", ""), ("manindriyaṃ", ""), ("somanassindriyaṃ", ""), ("jīvitindriyaṃ", ""),
    ("sammādiṭṭhi", ""), ("sammāsaṅkappo", ""), ("sammāvāyāmo", ""), ("sammāsati", ""), ("sammāsamādhi", ""),
    ("saddhābalaṃ", ""), ("vīriyabalaṃ", V("s", "Sī., Syā.", "viriyabalaṃ")), ("satibalaṃ", ""),
    ("samādhibalaṃ", ""), ("paññābalaṃ", ""), ("hiribalaṃ", ""), ("ottappabalaṃ", ""), ("alobho", ""),
    ("adoso", ""), ("amoho", ""), ("anabhijjhā", ""), ("abyāpādo", ""), ("sammādiṭṭhi", ""), ("hirī", ""),
    ("ottappaṃ", ""), ("kāyapassaddhi", V("s", "Syā.", "kāyappassaddhi")),
    ("cittapassaddhi", V("s", "Syā.", "cittappassaddhi")), ("kāyalahutā", ""), ("cittalahutā", ""),
    ("kāyamudutā", ""), ("cittamudutā", ""), ("kāyakammaññatā", ""), ("cittakammaññatā", ""),
    ("kāyapāguññatā", ""), ("cittapāguññatā", ""), ("kāyujukatā", V("s", "Sī., Ka.", "kāyujjukatā")),
    ("cittujukatā", V("s", "Sī., Ka.", "cittujjukatā")), ("sati", ""), ("sampajaññaṃ", ""), ("samatho", ""),
    ("vipassanā", ""), ("paggāho", ""), ("avikkhepo", ""),
]
SEG_1_1 = (
    QUESTION(KUSALA) + " " + OPEN_KAMA_KUSALA + ", " + ACC_SOMA_NANA + ", " + ARAMMANA + ", " + THEN + " "
    + ", ".join(LIST_ITEM(k, v) for k, v in LIST_1_1)
    + "; hoặc " + YEVAPANA()
)

# ---- segments in source order --------------------------------------------------------
SEGMENTS = [
    ("1-1-0", [H_CH2]),
    ("1-1-1-0", [H_KAMA_KUSALA]),
    ("1-1-1-1-0", [H_PADA]),
    ("1-1", [SEG_1_1]),
    ("1-2", [QA("phasso", S_PHASSA)]),
    ("1-3", [T("vedanā", S_SUKHA)]),
    ("1-4", [T("saññā", S_SANNA)]),
    ("1-5", [T("cetanā", S_CETANA_V)]),
    ("1-6", [QA("cittaṃ", S_CITTA)]),
    ("1-7", [QA("vitakko", S_VITAKKA)]),
    ("1-8", [QA("vicāro", S_VICARA)]),
    ("1-9", [QA("pīti", S_PITI)]),
    ("1-10", [QA("sukhaṃ", S_SUKHA)]),
    ("1-11", [QA("cittassekaggatā", S_SAMADHI)]),
    ("1-12", [QA("saddhindriyaṃ", S_SADDHA)]),
    ("1-13", [QA("vīriyindriyaṃ", S_VIRIYA_V)]),
    ("1-14", [QA("satindriyaṃ", S_SATI)]),
    ("1-15", [QA("samādhindriyaṃ", S_SAMADHI)]),
    ("1-16", [QA("paññindriyaṃ", S_PANNA)]),
    ("1-17", [QA("manindriyaṃ", S_CITTA)]),
    ("1-18", [QA("somanassindriyaṃ", S_SUKHA)]),
    ("1-19", [JIVITA("jīvitindriyaṃ", S_JIVITA_V)]),
    ("1-20", [QA("sammādiṭṭhi", S_PANNA)]),
    ("1-21", [QA("sammāsaṅkappo", S_VITAKKA)]),
    ("1-22", [QA("sammāvāyāmo", S_VIRIYA)]),
    ("1-23", [QA("sammāsati", S_SATI)]),
    ("1-24", [QA("sammāsamādhi", S_SAMADHI)]),
    ("1-25", [QA("saddhābalaṃ", S_SADDHA)]),
    ("1-26", [QA("vīriyabalaṃ", S_VIRIYA)]),
    ("1-27", [QA("satibalaṃ", S_SATI)]),
    ("1-28", [QA("samādhibalaṃ", S_SAMADHI)]),
    ("1-29", [QA("paññābalaṃ", S_PANNA)]),
    ("1-30", [SHAME("hiribalaṃ", S_HIRI)]),
    ("1-31", [SHAME("ottappabalaṃ", S_OTTAPPA)]),
    ("1-32", [QA("alobho", S_ALOBHA)]),
    ("1-33", [QA("adoso", S_ADOSA_V, end="?")]),  # the Pāli ends this answer with "?" (source slip, kept)
    ("1-34", [QA("amoho", S_PANNA + ", " + N["amoho"] + ", " + ROOT)]),
    ("1-35", [QA("anabhijjhā", S_ALOBHA)]),
    ("1-36", [QA("abyāpādo", S_ADOSA)]),
    ("1-37", [QA("sammādiṭṭhi", S_PANNA)]),
    ("1-38", [SHAME("hirī", S_HIRI)]),
    ("1-39", [SHAME("ottappaṃ", S_OTTAPPA)]),
    ("1-40", [KAYA("kāyapassaddhi", S_PASSADDHI_V)]),
    ("1-41", [CITTA("cittapassaddhi", S_PASSADDHI)]),
    ("1-42", [KAYA("kāyalahutā", S_LAHUTA)]),
    ("1-43", [CITTA("cittalahutā", S_LAHUTA)]),
    ("1-44", [KAYA("kāyamudutā", S_MUDUTA)]),
    ("1-45", [CITTA("cittamudutā", S_MUDUTA)]),
    ("1-46", [KAYA("kāyakammaññatā", S_KAMMANNATA)]),
    ("1-47", [CITTA("cittakammaññatā", S_KAMMANNATA)]),
    ("1-48", [KAYA("kāyapāguññatā", S_PAGUNATA)]),
    ("1-49", [CITTA("cittapāguññatā", S_PAGUNATA)]),
    ("1-50", [KAYA("kāyujukatā", S_UJUTA)]),
    ("1-51", [CITTA("cittujukatā", S_UJUTA)]),
    ("1-52", [QA("sati", S_SATI)]),
    ("1-53", [QA("sampajaññaṃ", S_PANNA)]),
    ("1-54", [QA("samatho", S_SAMADHI)]),
    ("1-55", [QA("vipassanā", S_PANNA)]),
    ("1-56", [QA("paggāho", S_VIRIYA)]),
    ("1-57", [QA("avikkhepo", S_SAMADHI), "Hoặc " + YEVAPANA(), END_PADA, END_BHANA1]),
]

ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def pali_segments():
    segs, n = [], 0
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        n += 1
        m = ID.search(line)
        if m:
            segs.append((m.group(1), n))
            n = 0
    return segs


def build():
    psegs = pali_segments()
    assert [b for b, _ in psegs] == [b for b, _ in SEGMENTS], "block IDs differ from the Pāli slice"
    out = []
    for (bid, lines), (_, pn) in zip(SEGMENTS, psegs):
        assert len(lines) == pn, (bid, len(lines), pn)
        lines = list(lines)
        lines[-1] += f" ^{bid}"
        out.append("\n".join(lines))
    return "\n\n".join(out) + "\n"


TEXT = build()
assert "—" not in TEXT and ":-" not in TEXT

if __name__ == "__main__":
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT)
