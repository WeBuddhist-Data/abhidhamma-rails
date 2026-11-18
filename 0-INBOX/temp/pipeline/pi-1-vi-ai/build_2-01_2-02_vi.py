"""Build the Vietnamese plain zero-shot of pi-1 parts 2-01 (after the approved sample) and 2-02.

usage: python -I -X utf8 build_2-01_2-02_vi.py          (runs the self-test, then builds both parts)

Importing this file does NOT build anything.
Method (mirrors the approved Russian builder): every Pāli line is translated by fixed formula strings.
The line translators raise KeyError on any Pāli they do not know, so nothing is guessed silently,
and every repeat is byte-identical by construction. 2-01 starts with the approved sample
(ch2-01-sample.md) byte for byte.

Reusable pieces: NAME / COUNTED / SUNNATA / name_vi(), STR, PH, EXACT, tail_vi(), there_list(),
name_list(), qa_vi(), kusala_vi(), summary_vi(), var_vi().
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402  (importing does not write)
import build_ch2_01_sample_vi as C  # noqa: E402  (importing does not write)

PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-zeroshot_split_chapters"
SAMPLE = HERE / "ch2-01-sample.md"
SAMPLE_PALI = HERE.parent / "pi-1-ru" / "ref" / "ch2-01-pali-1-122.md"  # read-only reference slice

DASH = C.DASH
PE, ELL = "…pe…", "…"
TASMIM = C.TASMIM
KUSALA = C.KUSALA


def cap(s):
    return s[:1].upper() + s[1:]


# =========================================================================================
# 1. Names (Pāli = Vietnamese). The sample's factor names plus new ones.
# =========================================================================================
NAME = dict(C.NAMES)
NAME.update({
    "upekkhā": "sự bình thản",
    "upekkhindriyaṃ": "năng lực bình thản",
    "vedanākkhandho": "khối cảm giác",
    "saññākkhandho": "khối tri giác",
    "saṅkhārakkhandho": "khối tạo tác",
    "viññāṇakkhandho": "khối thức",
    "manāyatanaṃ": "lĩnh vực ý",
    "dhammāyatanaṃ": "lĩnh vực đối tượng của ý",
    "manoviññāṇadhātu": "yếu tố ý thức",
    "dhammadhātu": "yếu tố đối tượng của ý",
    "phassāhāro": "sự tiếp xúc trong vai trò dưỡng chất",
    "manosañcetanāhāro": "chủ ý của ý trong vai trò dưỡng chất",
    "viññāṇāhāro": "thức trong vai trò dưỡng chất",
})
# the khandha names are the ones inside the sample's fixed strings
assert "khối cảm giác, khối tri giác và khối tạo tác" in C.G_KAYA and C.G_CITTA == "nơi khối thức"
assert "lĩnh vực ý" in C.WL["cittaṃ"] and "năng lực ý" in C.WL["cittaṃ"]

# Koṭṭhāsavāra: counted groups
COUNTED = {
    "cattāro khandhā": "bốn khối",
    "dvāyatanāni": "hai lĩnh vực nhận biết",
    "dve dhātuyo": "hai yếu tố",
    "tayo āhārā": "ba loại dưỡng chất",
    "aṭṭhindriyāni": "tám năng lực",
    "sattindriyāni": "bảy năng lực",
    "pañcaṅgikaṃ jhānaṃ": "tầng thiền gồm năm chi phần",
    "caturaṅgikaṃ jhānaṃ": "tầng thiền gồm bốn chi phần",
    "tivaṅgikaṃ jhānaṃ": "tầng thiền gồm ba chi phần",
    "duvaṅgikaṃ jhānaṃ": "tầng thiền gồm hai chi phần",
    "pañcaṅgiko maggo": "con đường gồm năm chi phần",
    "caturaṅgiko maggo": "con đường gồm bốn chi phần",
    "satta balāni": "bảy sức mạnh",
    "cha balāni": "sáu sức mạnh",
    "tayo hetū": "ba gốc rễ",
    "dve hetū": "hai gốc rễ",
}
# Suññatavāra: bare group names
SUNNATA = {
    "dhammā": "các hiện tượng",
    "khandhā": "các khối",
    "āyatanāni": "các lĩnh vực nhận biết",
    "dhātuyo": "các yếu tố",
    "āhārā": "các loại dưỡng chất",
    "indriyāni": "các năng lực",
    "jhānaṃ": "tầng thiền",
    "maggo": "con đường",
    "balāni": "các sức mạnh",
    "hetū": "các gốc rễ",
}
ONE = "một"  # eko / ekā / ekaṃ


def name_vi(p):
    if p in COUNTED:
        return COUNTED[p]
    if p in SUNNATA:
        return SUNNATA[p]
    if p in NAME:
        return NAME[p]
    m = re.fullmatch(r"(eko|ekā|ekaṃ) (\S+)", p)
    if m and m.group(2) in NAME:
        return f"{ONE} {NAME[m.group(2)]}"
    raise KeyError("name: " + p)


def q_vi(p):
    """'Katamo … tasmiṃ samaye X hoti' (without the final '?')"""
    return f"Vào lúc ấy, {name_vi(p)} là gì"


def this_vi(p):
    """'ayaṃ/idaṃ/ime/imāni/imā tasmiṃ samaye X hoti/honti'"""
    return f"đây là {name_vi(p)} {TASMIM}"


def there_vi(p):
    """'X hoti' inside a list"""
    return f"có {name_vi(p)}"


assert q_vi("phasso") + "?" == C.Q("phasso")
assert there_vi("phasso") == C.LIST_ITEM("phasso")

# =========================================================================================
# 2. Synonym strings (Pāli string = Vietnamese). The sample's STRINGS plus new ones.
# =========================================================================================
STR = dict(C.STRINGS)
S_PANNA_P = [k for k in C.STRINGS if k.startswith("paññā ")][0]
S_UPEKKHA_P = ("cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ "
               "cetosamphassajā adukkhamasukhā vedanā")
ADUKKHAM = "không khó chịu cũng không dễ chịu"  # adukkhamasukha, as matrix triad 2 (c)
assert M.BARE[("1-M1-2", "c")].endswith("cảm giác " + ADUKKHAM)
S_UPEKKHA = (f"trạng thái trong tâm không khoan khoái cũng không bứt rứt, "
             f"cảm nhận {ADUKKHAM} sinh từ sự tiếp xúc của tâm, "
             f"cảm giác {ADUKKHAM} sinh từ sự tiếp xúc của tâm")
STR[S_UPEKKHA_P] = S_UPEKKHA
STR[S_PANNA_P + " amoho kusalamūlaṃ"] = C.S_PANNA + ", " + C.N["amoho"] + ", " + C.ROOT
# abbreviated wisdom string (…pe… inside the string)
STR["paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi"] = (
    "trí tuệ, sự hiểu rõ… sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn")
assert C.S_PANNA.startswith("trí tuệ, sự hiểu rõ, ") and C.S_PANNA.endswith(
    ", sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn")

# qualifiers placed between «Điều có mặt vào lúc ấy» and «, tức là»
STR_PREFIX = [
    ("tajjāmanoviññāṇadhātusamphassajaṃ ", " và " + C.TAJJA),
    ("tajjāmanoviññāṇadhātusamphassajā ", " và " + C.TAJJA),
    ("vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa ", " " + C.G_KAYA),
    ("viññāṇakkhandhassa ", " " + C.G_CITTA),
]

# =========================================================================================
# 3. Variant brackets: all variants in these parts are spelling variants
# =========================================================================================
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "bahūsu": "nhiều ấn bản"}


def var_vi(br):
    m = re.fullmatch(r"\[(.+?) \(([^)]*)\)\]", br)
    words, sig = m.groups()
    sig = [sig] if sig in SIGLA else sig.split()
    return M.V("s", ", ".join(SIGLA[s] for s in sig), words).strip()


# =========================================================================================
# 4. Tails: "ye vā pana …", "ayaṃ tasmiṃ samaye X hoti", "ime dhammā kusalā", "…pe…"
# =========================================================================================
YVP_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
YVP_V = "hoặc " + C.YEVAPANA_BODY
assert "Hoặc " + C.YEVAPANA() == cap(YVP_V) + " " + DASH + " " + M.ANSWER(KUSALA)
THAP_P = "ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
EXCEPT = "ngoại trừ"
THAP_V = f"{EXCEPT} khối cảm giác, {EXCEPT} khối tri giác, {EXCEPT} khối thức"
THAP_PV = "ṭhapetvā [thapetvā (ka.)] vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_VV = THAP_V.replace(EXCEPT + " ", EXCEPT + " " + var_vi("[thapetvā (ka.)]") + " ", 1)
KUSALA_P, KUSALA_V = "ime dhammā kusalā", M.ANSWER_BARE(KUSALA)
assert KUSALA_V + "." == M.ANSWER(KUSALA)


def tail_vi(t):
    t = t.replace(YVP_P + " " + THAP_PV + " " + DASH, YVP_V + ", " + THAP_VV + " " + DASH)
    t = t.replace(YVP_P + " " + THAP_P + " " + DASH, YVP_V + ", " + THAP_V + " " + DASH)
    t = t.replace(YVP_P + " " + DASH, YVP_V + " " + DASH)
    assert YVP_P not in t, t
    t = re.sub(r"(?<!\S)(ayaṃ|idaṃ|ime|imāni|imā) tasmiṃ samaye (.+?) (hoti|honti)",
               lambda m: this_vi(m.group(2)), t)
    t = t.replace(KUSALA_P, KUSALA_V)
    t = t.replace(PE, ELL)
    return t


# =========================================================================================
# 5. Lists
# =========================================================================================
def there_list(s):
    """'phasso hoti, vedanā hoti…pe… avikkhepo hoti' -> 'có sự tiếp xúc, có cảm giác… có …'"""
    parts = re.split(r"(?:(?<=hoti)|(?<=honti))(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p.replace(PE, ELL) if PE in p else ", ")
        else:
            m = re.fullmatch(r"(.+) (hoti|honti)", p)
            out.append(there_vi(m.group(1)))
    return "".join(out)


def name_list(s):
    """'Phasso cetanā…pe… avikkhepo' / 'Vedanākkhandho, saññākkhandho' -> Vietnamese names, comma-separated"""
    parts = re.split(r"(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p.replace(PE, ELL) if PE in p else ", ")
        else:
            out.append(name_vi(p[0].lower() + p[1:]))
    return "".join(out)


# =========================================================================================
# 6. Q/A frames
# =========================================================================================
QRE = re.compile(r"Katam(?:o|ā|aṃ|e|āni) tasmiṃ samaye (.+?) (hoti|honti)(\?|…pe…)\s*(.*)$")
ARE = re.compile(r"(?:Yo|Yā|Yaṃ) tasmiṃ samaye (.+?) – ((?:ayaṃ|idaṃ) tasmiṃ samaye .+)$")
JRE = re.compile(r"Yo tesaṃ arūpīnaṃ dhammānaṃ (.+?) – (idaṃ tasmiṃ samaye .+)$")
LRE = re.compile(r"(.+?)(\s–\s.*|;.*|\.)$")


def str_vi(s):
    pre = ""
    for p, r in STR_PREFIX:
        if s.startswith(p):
            s, pre = s[len(p):], r
            break
    return pre, STR[s]


def answer_vi(a):
    m = ARE.fullmatch(a)
    if m:
        s, rest = m.groups()
        pre, sv = str_vi(s)
        if s.startswith(("hirīyati", "ottappati")):
            return f"Việc {TASMIM} {sv} {DASH} " + tail_vi(rest)
        return f"Điều có mặt {TASMIM}{pre}, tức là {sv} {DASH} " + tail_vi(rest)
    m = JRE.fullmatch(a)
    if m:
        s, rest = m.groups()
        return f"Điều có {C.G_JIVITA}, tức là {STR[s]} {DASH} " + tail_vi(rest)
    m = LRE.fullmatch(a)
    names, rest = m.groups()
    return cap(name_list(names)) + tail_vi(rest)


def qa_vi(line):
    m = QRE.fullmatch(line)
    name, verb, mark, rest = m.groups()
    q = q_vi(name)
    if mark == "?":
        return q + "? " + answer_vi(rest)
    return q + ELL + " " + tail_vi(rest)


# =========================================================================================
# 7. "Katame dhammā kusalā? Yasmiṃ samaye …" sentences: fixed phrase table
# =========================================================================================
Q_KUSALA = M.QUESTION(KUSALA)
PERSON = "Vào lúc một người tu tập con đường dẫn đến tái sinh vào"
INTROS = [
    ("rūpūpapattiyā maggaṃ bhāveti ", f"{PERSON} cõi hình sắc, "),
    ("arūpūpapattiyā maggaṃ bhāveti ", f"{PERSON} cõi không hình sắc, "),
    ("kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti ", C.OPEN_KAMA_KUSALA + ", "),
]

J = "tầng thiền"
ENTER = "chứng nhập và an trú trong"   # upasampajja viharati
ORD = {"paṭhamaṃ": "thứ nhất", "dutiyaṃ": "thứ hai", "tatiyaṃ": "thứ ba", "catutthaṃ": "thứ tư",
       "pañcamaṃ": "thứ năm"}
# matrix triad 6 (a)/(b)/(c): savitakka savicāra / avitakka vicāramatta / avitakka avicāra
SAVITAKKA = M.PRED[("1-M1-6", "a")]
VICARAMATTA = M.PRED[("1-M1-6", "b")]
AVITAKKA = M.PRED[("1-M1-6", "c")]
assert (SAVITAKKA, VICARAMATTA, AVITAKKA) == (
    "có sự hướng tâm và sự duy trì tâm", "không có sự hướng tâm, chỉ có sự duy trì tâm",
    "không có sự hướng tâm cũng không có sự duy trì tâm")
PITISUKHA = "có sự hân hoan và hạnh phúc sinh từ"
SEE_FORMS = "không có tri giác về hình sắc nơi bản thân, thấy các hình sắc ở bên ngoài bản thân"
SAHA = "đi kèm"   # -sahagata, as «có X đi kèm» in the matrix
CORPSE = "xác chết"
HINA, MAJJHIMA, PANITA = (M.BARE[("1-M1-14", l)][len("các hiện tượng "):] for l in "abc")
assert (HINA, MAJJHIMA, PANITA) == ("thấp kém", "trung bình", "ưu việt")
ADHIP = "làm yếu tố chủ đạo"
SOMA = M.PRED[("1-M1-7", "a")]   # «có sự hân hoan đi kèm» is pīti; somanassa below is «niềm vui»
UPEKKHA_SAHA = M.PRED[("1-M1-7", "c")]
assert UPEKKHA_SAHA == "có sự bình thản đi kèm"
NANA = "gắn liền với hiểu biết"
assert C.ACC_SOMA_NANA == "có niềm vui đi kèm, " + NANA


def colour(c):
    return f"loại {c}, có màu {c}, trông {c}, tỏa ánh {c}"


def abhinna(mode, speed):
    return f"với cách thực hành {mode}{{V}} và sự hiểu biết trực tiếp {speed}"


# {V} marks where a variant bracket of that phrase goes (else it goes at the end of the phrase)
PH = {
    # --- the absorption formulas (full) -------------------------------------------------
    "vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ "
    "upasampajja viharati":
        f"hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, {ENTER} {J} thứ nhất{{V}}, "
        f"{SAVITAKKA}, {PITISUKHA} sự tách biệt",
    "vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ "
    "pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        f"khi sự hướng tâm và sự duy trì tâm đã lắng xuống, {ENTER} {J} thứ hai{{V}}, có sự trong sáng bên "
        f"trong và sự hợp nhất của tâm, {AVITAKKA}, {PITISUKHA} định tâm",
    "pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti yaṃ taṃ ariyā "
    "ācikkhanti – \"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati":
        f"khi sự hân hoan phai nhạt, an trú bình thản, tỉnh thức và hiểu biết rõ ràng, cảm nhận hạnh phúc bằng "
        f"thân, điều mà các bậc thánh mô tả {DASH} “Người bình thản, tỉnh thức, an trú trong hạnh phúc”, "
        f"{ENTER} {J} thứ ba{{V}}",
    "sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ "
    "upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati":
        f"khi đã dứt bỏ sự dễ chịu và dứt bỏ sự khó chịu, và niềm vui cùng nỗi buồn đã biến mất từ trước, "
        f"{ENTER} {J} thứ tư{{V}}, {ADUKKHAM}, có sự tỉnh thức hoàn toàn trong sạch nhờ sự bình thản",
    "avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        f"{ENTER} {J} thứ hai{{V}}, {VICARAMATTA}, {PITISUKHA} định tâm",
    # --- the absorption formulas (opening words only, before …pe…) ---------------------
    "vivicceva kāmehi": "hoàn toàn tách khỏi các dục lạc",
    "vitakkavicārānaṃ vūpasamā": "khi sự hướng tâm và sự duy trì tâm đã lắng xuống",
    "pītiyā ca virāgā": "khi sự hân hoan phai nhạt",
    "sukhassa ca pahānā": "khi đã dứt bỏ sự dễ chịu",
    # --- modes of practice ---------------------------------------------------------------
    "dukkhapaṭipadaṃ dandhābhiññaṃ": abhinna("khó khăn", "chậm chạp"),
    "dukkhapaṭipadaṃ khippābhiññaṃ": abhinna("khó khăn", "nhanh chóng"),
    "sukhapaṭipadaṃ dandhābhiññaṃ": abhinna("dễ dàng", "chậm chạp"),
    "sukhapaṭipadaṃ khippābhiññaṃ": abhinna("dễ dàng", "nhanh chóng"),
    # --- the absorption and its object (matrix triads 12 and 13) -------------------------
    "parittaṃ parittārammaṇaṃ": "hạn hẹp và có đối tượng hạn hẹp",
    "parittaṃ appamāṇārammaṇaṃ": "hạn hẹp và có đối tượng không thể đo lường",
    "appamāṇaṃ parittārammaṇaṃ": "không thể đo lường và có đối tượng hạn hẹp",
    "appamāṇaṃ appamāṇārammaṇaṃ": "không thể đo lường và có đối tượng không thể đo lường",
    # --- all-encompassing objects (kasiṇa) ------------------------------------------------
    "pathavīkasiṇaṃ": "với đề mục bao trùm là đất",
    "āpokasiṇaṃ": "với đề mục bao trùm là nước",
    "tejokasiṇaṃ": "với đề mục bao trùm là lửa",
    "vāyokasiṇaṃ": "với đề mục bao trùm là gió",
    "nīlakasiṇaṃ": "với đề mục bao trùm là màu xanh",
    "pītakasiṇaṃ": "với đề mục bao trùm là màu vàng",
    "lohitakasiṇaṃ": "với đề mục bao trùm là màu đỏ",
    "odātakasiṇaṃ": "với đề mục bao trùm là màu trắng",
    # --- spheres of mastery (abhibhāyatana) ------------------------------------------------
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati": SEE_FORMS,
    "parittāni": "loại hạn hẹp",
    "appamāṇāni": "loại không thể đo lường",
    "suvaṇṇadubbaṇṇāni": "có màu đẹp và màu xấu",
    "nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni": colour("xanh"),
    "pītāni pītavaṇṇāni pītanidassanāni pītanibhāsāni": colour("vàng"),
    "lohitakāni lohitakavaṇṇāni lohitakanidassanāni lohitakanibhāsāni": colour("đỏ"),
    "odātāni odātavaṇṇāni odātanidassanāni odātanibhāsāni": colour("trắng"),
    "tāni abhibhuyya jānāmi passāmīti": "chế ngự chúng với ý nghĩ: “Tôi biết, tôi thấy”",
    # --- liberations ------------------------------------------------------------------------
    "rūpī rūpāni passati": "có hình sắc, thấy các hình sắc",
    "subhanti": "với ý nghĩ: “Đẹp đẽ”",
    # --- the sublime abidings -----------------------------------------------------------------
    "mettāsahagataṃ": f"có lòng từ ái {SAHA}",
    "karuṇāsahagataṃ": f"có lòng trắc ẩn {SAHA}",
    "muditāsahagataṃ": f"có niềm vui đồng cảm {SAHA}",
    "upekkhāsahagataṃ": UPEKKHA_SAHA,
    # --- the unattractive ------------------------------------------------------------------------
    "uddhumātakasaññāsahagataṃ": f"có tri giác về {CORPSE} trương phình {SAHA}",
    "vinīlakasaññāsahagataṃ": f"có tri giác về {CORPSE} bầm tím {SAHA}",
    "vipubbakasaññāsahagataṃ": f"có tri giác về {CORPSE} mưng mủ {SAHA}",
    "vicchiddakasaññāsahagataṃ": f"có tri giác về {CORPSE} bị cắt đứt {SAHA}",
    "vikkhāyitakasaññāsahagataṃ": f"có tri giác về {CORPSE} bị thú vật ăn dở {SAHA}",
    "vikkhittakasaññāsahagataṃ": f"có tri giác về {CORPSE} bị vương vãi {SAHA}",
    "hatavikkhittakasaññāsahagataṃ": f"có tri giác về {CORPSE} bị chặt và vương vãi {SAHA}",
    "lohitakasaññāsahagataṃ": f"có tri giác về {CORPSE} đẫm máu {SAHA}",
    "puḷavakasaññāsahagataṃ": f"có tri giác về {CORPSE} đầy giòi {SAHA}",
    "aṭṭhikasaññāsahagataṃ": f"có tri giác về bộ xương {SAHA}",
    # --- the absorptions of the formless realm ----------------------------------------------
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā":
        "khi đã vượt qua hoàn toàn các tri giác về hình sắc, các tri giác về sự va chạm đã biến mất, "
        "và không chú tâm đến các tri giác về sự đa dạng",
    "ākāsānañcāyatanasaññāsahagataṃ": f"có tri giác về lĩnh vực không gian vô tận {SAHA}",
    "sabbaso ākāsānañcāyatanaṃ samatikkamma": "khi đã vượt qua hoàn toàn lĩnh vực không gian vô tận",
    "viññāṇañcāyatanasaññāsahagataṃ": f"có tri giác về lĩnh vực thức vô tận {SAHA}",
    "sabbaso viññāṇañcāyatanaṃ samatikkamma": "khi đã vượt qua hoàn toàn lĩnh vực thức vô tận",
    "ākiñcaññāyatanasaññāsahagataṃ": f"có tri giác về lĩnh vực không có gì cả {SAHA}",
    "sabbaso ākiñcaññāyatanaṃ samatikkamma": "khi đã vượt qua hoàn toàn lĩnh vực không có gì cả",
    "nevasaññānāsaññāyatanasaññāsahagataṃ":
        f"có tri giác về lĩnh vực không phải tri giác cũng không phải không tri giác {SAHA}",
    # --- level (matrix triad 14) and dominant factor -----------------------------------------
    "hīnaṃ": HINA,
    "majjhimaṃ": MAJJHIMA,
    "paṇītaṃ": PANITA,
    "chandādhipateyyaṃ": f"với ý muốn {ADHIP}",
    "vīriyādhipateyyaṃ": f"với tinh tấn {ADHIP}",
    "cittādhipateyyaṃ": f"với tâm {ADHIP}",
    "vīmaṃsādhipateyyaṃ": f"với sự thẩm xét {ADHIP}",
    # --- the eight wholesome minds of the sense-pleasure realm -------------------------------
    "somanassasahagataṃ ñāṇasampayuttaṃ": C.ACC_SOMA_NANA,
    "somanassasahagataṃ ñāṇavippayuttaṃ": f"có niềm vui đi kèm, không {NANA}",
    "upekkhāsahagataṃ ñāṇasampayuttaṃ": f"{UPEKKHA_SAHA}, {NANA}",
    "upekkhāsahagataṃ ñāṇavippayuttaṃ": f"{UPEKKHA_SAHA}, không {NANA}",
    "sasaṅkhārena": "có sự thúc đẩy",
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": C.ARAMMANA,
    "rūpārammaṇaṃ vā": "lấy hình sắc",
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": "hoặc đối tượng của ý, hay bất cứ thứ gì làm đối tượng",
}
assert C.ARAMMANA.startswith(PH["rūpārammaṇaṃ vā"] + ", ")
assert C.ARAMMANA.endswith(", " + PH["dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"])
for p, o in ORD.items():
    PH[f"{p} jhānaṃ upasampajja viharati"] = f"{ENTER} {J} {o}{{V}}"
    PH[f"{p} jhānaṃ"] = f"{J} {o}{{V}}"
# the full formulas begin with their opening words (so «…pe…» forms read the same)
for k in ("vivicceva kāmehi", "vitakkavicārānaṃ vūpasamā", "pītiyā ca virāgā", "sukhassa ca pahānā"):
    full = [v for kk, v in PH.items() if kk.startswith(k + " ") and kk.endswith("upasampajja viharati")]
    assert len(full) == 1 and full[0].startswith((PH[k] + ",", PH[k] + " ")), k
PH_MAX = max(len(k.split()) for k in PH)


def chunk_vi(part):
    words = []
    for t in re.findall(r"\[[^\]]*\]|[^\s\[]+", part):
        if t.startswith("["):
            words[-1][1].append(var_vi(t))
        else:
            words.append([t.rstrip(","), []])
    res, i = [], 0
    while i < len(words):
        for L in range(min(PH_MAX, len(words) - i), 0, -1):
            key = " ".join(w for w, _ in words[i:i + L])
            if key in PH:
                break
        else:
            raise KeyError("phrase: " + " ".join(w for w, _ in words[i:]))
        vi = PH[key]
        vs = [v for _, vv in words[i:i + L] for v in vv]
        if vs:
            vt = " " + " ".join(vs)
            vi = vi.replace("{V}", vt) if "{V}" in vi else vi + vt
        res.append(vi.replace("{V}", ""))
        i += L
    return ", ".join(res)


def x_vi(x):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(part.replace(PE, ELL))
        elif part.strip():
            out.append(chunk_vi(part))
    return "".join(out)


def kusala_vi(line):
    body = line[len("Katame dhammā kusalā? Yasmiṃ samaye "):]
    for p, r in INTROS:
        if body.startswith(p):
            body, intro = body[len(p):], r
            break
    else:
        raise KeyError("intro: " + body[:60])
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    if x.endswith(DASH):
        sep, x = " " + DASH, x[:-1].rstrip()
    elif x.endswith(","):
        sep, x = ",", x[:-1]
    else:
        sep = ","  # ^1-189: the Pāli has no comma here; Vietnamese punctuation needs one
    m = re.fullmatch(r"(.*? hoti)(…pe… ime dhammā kusalā.*|; ye vā pana.*)", rest)
    return (Q_KUSALA + " " + intro + x_vi(x) + sep + f" {C.THEN} " + there_list(m.group(1))
            + tail_vi(m.group(2)))


def summary_vi(line):
    """'Tasmiṃ kho pana samaye cattāro khandhā honti, …; ye vā pana …' (Koṭṭhāsa / Suññata summaries)"""
    body = line[len("Tasmiṃ kho pana samaye "):]
    items, rest = body.split(";", 1)
    return f"Và {TASMIM} " + there_list(items) + ";" + tail_vi(rest)


# =========================================================================================
# 8. Headings and closing lines (headings from vi-zeroshot-terms.md, verbatim)
# =========================================================================================
H_KAMA = C.H_KAMA_KUSALA[len("#### "):]   # «Tâm thiện thuộc cõi dục lạc»
H_RUPA = "Tâm thiện thuộc cõi hình sắc"
H_ARUPA = "Tâm thiện thuộc cõi không hình sắc"
SIXTEEN = "phân tích theo mười sáu cách"
EIGHT = "phân tích theo tám cách"
H_BRAHMA = "Bốn tầng thiền của các nơi an trú cao thượng"
H_ASUBHA = "Tầng thiền về sự không đẹp đẽ"
H_ARUPAJ = "Bốn tầng thiền không hình sắc"
CITTA_ORD = ["nhất", "hai", "ba", "tư", "năm", "sáu", "bảy", "tám"]
CITTA_PALI = ["Paṭhamaṃ", "Dutiyaṃ", "Tatiyaṃ", "Catutthaṃ", "Pañcamaṃ", "Chaṭṭhaṃ", "Sattamaṃ", "Aṭṭhamaṃ"]
EXACT = {
    "Padabhājanīyaṃ.": C.END_PADA,
    "Paṭhamabhāṇavāro.": C.END_BHANA1,
    "##### Koṭṭhāsavāro": "##### Mục về các thành phần",
    "Koṭṭhāsavāro.": "Mục về các thành phần.",
    "##### Suññatavāro": "##### Mục về sự trống rỗng",
    "Suññatavāro.": "Mục về sự trống rỗng.",
    "Aṭṭha kāmāvacaramahākusalacittāni.": "Tám tâm thiện lớn thuộc cõi dục lạc.",
    "Dutiyabhāṇavāro.": "Phần tụng đọc thứ hai.",
    # 2-02
    "#### Rūpāvacarakusalaṃ": "#### " + H_RUPA,
    "#### Arūpāvacarakusalaṃ": "#### " + H_ARUPA,
    "#### Tebhūmakakusalaṃ": "#### Tâm thiện thuộc ba cõi",
    "##### Kāmāvacarakusalaṃ": "##### " + H_KAMA,
    "##### Rūpāvacarakusalaṃ": "##### " + H_RUPA,
    "##### Arūpāvacarakusalaṃ": "##### " + H_ARUPA,
    "Kāmāvacarakusalaṃ.": H_KAMA + ".",
    "Rūpāvacarakusalaṃ.": H_RUPA + ".",
    "Arūpāvacarakusalaṃ.": H_ARUPA + ".",
    "##### Catukkanayo": "##### Phương pháp chia bốn",
    "Catukkanayo.": "Phương pháp chia bốn.",
    "##### Pañcakanayo": "##### Phương pháp chia năm",
    "Pañcakanayo.": "Phương pháp chia năm.",
    "##### Catasso paṭipadā": "##### Bốn cách thực hành",
    "Catasso paṭipadā.": "Bốn cách thực hành.",
    "##### Cattāri ārammaṇāni": "##### Bốn loại đối tượng",
    "Cattāri ārammaṇāni.": "Bốn loại đối tượng.",
    "##### Dve ārammaṇāni": "##### Hai loại đối tượng",
    "Dve ārammaṇāni.": "Hai loại đối tượng.",
    "##### Soḷasakkhattukaṃ": "##### " + cap(SIXTEEN),
    "Soḷasakkhattukaṃ.": cap(SIXTEEN) + ".",
    "##### Aṭṭhakkhattukaṃ": "##### " + cap(EIGHT),
    "Aṭṭhakkhattukaṃ.": cap(EIGHT) + ".",
    "##### Idampi aṭṭhakkhattukaṃ": f"##### Đây cũng là {EIGHT}",
    "Idampi aṭṭhakkhattukaṃ.": f"Đây cũng là {EIGHT}.",
    "##### Aparampi aṭṭhakkhattukaṃ": f"##### Thêm một {EIGHT}",
    "Aparampi aṭṭhakkhattukaṃ.": f"Thêm một {EIGHT}.",
    "##### Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": f"##### Tám đề mục bao trùm, {SIXTEEN}",
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ.": f"Tám đề mục bao trùm, {SIXTEEN}.",
    "##### Abhibhāyatanāni parittāni": "##### Các lĩnh vực chế ngự hạn hẹp",
    "##### Appamāṇāni": "##### Loại không thể đo lường",
    "Imānipi abhibhāyatanāni soḷasakkhattukāni.": f"Các lĩnh vực chế ngự này cũng được {SIXTEEN}.",
    "##### Tīṇi vimokkhāni soḷasakkhattukāni": f"##### Ba sự giải thoát, {SIXTEEN}",
    "Imānipi tīṇi vimokkhāni soḷasakkhattukāni.": f"Ba sự giải thoát này cũng được {SIXTEEN}.",
    "##### Cattāri brahmavihārajhānāni soḷasakkhattukāni": f"##### {H_BRAHMA}, {SIXTEEN}",
    "Cattāri brahmavihārajhānāni [brahmavihārajjhānāni (sī. syā.)] soḷasakkhattukāni.":
        H_BRAHMA + M.V("s", "Sī., Syā.", "brahmavihārajjhānāni") + f", {SIXTEEN}.",
    "##### Asubhajhānaṃ soḷasakkhattukaṃ": f"##### {H_ASUBHA}, {SIXTEEN}",
    "Asubhajhānaṃ [asubhajjhānaṃ (sī. syā.)] soḷasakkhattukaṃ.":
        H_ASUBHA + M.V("s", "Sī., Syā.", "asubhajjhānaṃ") + f", {SIXTEEN}.",
    "##### Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni":
        "##### " + H_ARUPAJ + M.V("s", "Sī., Syā.", "arūpajjhānāni") + f", {SIXTEEN}",
    "Cattāri arūpajhānāni soḷasakkhattukāni.": f"{H_ARUPAJ}, {SIXTEEN}.",
}
for p, o in zip(CITTA_PALI, CITTA_ORD):
    EXACT[f"{p} cittaṃ."] = f"Tâm thứ {o}."
assert EXACT["##### Kāmāvacarakusalaṃ"] == "#" + C.H_KAMA_KUSALA

# headings must equal vi-zeroshot-terms.md word for word
TERMS = HERE / "vi-zeroshot-terms.md"


def check_headings():
    terms = {}
    for line in TERMS.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(#+ .+?) = (#+ .+)", line)
        if m:
            terms[m.group(1)] = m.group(2)
    n = 0
    for p, v in EXACT.items():
        if p.startswith("#####"):
            key = "####" + p[5:] if "####" + p[5:] in terms else p
            exp = terms[key]
            if not key == p:
                exp = "#" + exp
            assert exp == v, (p, exp, v)
            n += 1
        elif p.startswith("####"):
            assert terms[p] == v, (p, terms[p], v)
            n += 1
    return n


# =========================================================================================
# 9. Line dispatch, segments, build
# =========================================================================================
IDRE = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def translate_line(line):
    if line in EXACT:
        return EXACT[line]
    if line.startswith("Katame dhammā kusalā? Yasmiṃ samaye "):
        return kusala_vi(line)
    if line.startswith("Tasmiṃ kho pana samaye "):
        return summary_vi(line)
    if QRE.fullmatch(line):
        return qa_vi(line)
    if line.startswith("Ye vā pana ") or re.match(r"(Ime|Imāni|Imā|Idaṃ|Ayaṃ) tasmiṃ samaye ", line):
        return cap(tail_vi(line[0].lower() + line[1:]))
    raise KeyError("line: " + line[:80])


PALI_CHARS = set("āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ")


def check_line(pali, vi):
    bare = re.sub(r"\[[^\]]*\]", "", vi)
    bad = PALI_CHARS & set(bare)
    assert not bad, (bad, vi[:120])
    assert not re.search(r"[fjwzFJWZ]", bare), vi[:120]
    assert "—" not in vi and ":-" not in vi and "chánh niệm" not in vi
    assert pali.count(DASH) == vi.count(DASH), (pali[:80], vi[:120])
    assert pali.count("—") == 0
    assert pali.count("?") == vi.count("?"), (pali[:80], vi[:120])
    assert pali.count("[") == vi.count("["), (pali[:80], vi[:120])


def segments(text):
    segs, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = IDRE.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return segs


def render(segs):
    out = []
    for bid, lines in segs:
        vi = [cap(translate_line(l)) for l in lines]
        for p, r in zip(lines, vi):
            check_line(p, r)
        vi[-1] += f" ^{bid}"
        out.append("\n".join(vi))
    return out


def build_2_01():
    segs = segments((PALI_DIR / "2-01-cittuppadakandam.md").read_text(encoding="utf-8"))
    ids = [b for b, _ in segs]
    k = ids.index("1-57") + 1
    sample = SAMPLE.read_bytes().decode("utf-8")
    assert sample.endswith(" ^1-57\n") and sample == C.TEXT
    return sample + "\n" + "\n\n".join(render(segs[k:])) + "\n", len(segs)


def build_2_02():
    segs = segments((PALI_DIR / "2-02-cittuppadakandam.md").read_text(encoding="utf-8"))
    return "\n\n".join(render(segs)) + "\n", len(segs)


def selftest():
    """Run the translators on the sample's Pāli; every line must equal the approved sample, except
    headings and the segments whose strings carry variant brackets (built by hand in the sample)."""
    pal = segments(SAMPLE_PALI.read_text(encoding="utf-8"))
    vis = segments(SAMPLE.read_text(encoding="utf-8"))
    skip = {"1-1-0", "1-1-1-0", "1-1-1-1-0", "1-1", "1-5", "1-13", "1-19", "1-33", "1-40"}
    ok = bad = 0
    for (b, pl), (b2, rl) in zip(pal, vis):
        assert b == b2
        if b in skip:
            continue
        for p, r in zip(pl, rl):
            got = cap(translate_line(p))
            if got == r:
                ok += 1
            else:
                bad += 1
                print("SELFTEST MISMATCH", b, "\n  got:", got, "\n  exp:", r)
    # ^1-1 without its variant brackets equals the generic kusala line on the bracket-free Pāli
    p11 = re.sub(r" \[[^\]]*\]", "", pal[3][1][0])
    v11 = re.sub(r" \[[^\]]*\]", "", vis[3][1][0])
    if cap(translate_line(p11)) == v11:
        ok += 1
    else:
        bad += 1
        print("SELFTEST MISMATCH 1-1\n  got:", cap(translate_line(p11)), "\n  exp:", v11)
    print(f"selftest: {ok} lines identical to the approved sample, {bad} mismatches;"
          f" {check_headings()} headings equal the terms file")
    return bad == 0


if __name__ == "__main__":
    assert selftest()
    for name, fn in (("2-01-cittuppadakandam.md", build_2_01), ("2-02-cittuppadakandam.md", build_2_02)):
        text, n = fn()
        assert "\r" not in text and "\n\n\n" not in text
        (OUT_DIR / name).write_bytes(text.encode("utf-8"))
        print("wrote", OUT_DIR / name, n, "segments")
