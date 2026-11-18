"""Shared helpers and tables for the pi-1 Pāli->Vietnamese keyword maps (mapper-vi/).

Importing this module has no side effects (no file is written, nothing printed).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_vi import *

Main pieces
- read_keywords(part)                    -> [(id, [kw, ...]), ...]   from <part>.keywords.md
- read_vietnamese(part) / read_pali(part) -> {id: segment text}      (segments end with ^id)
- present(value, text)                   -> True if the Vietnamese value occurs in text (see below)
- CORE                                   -> preamble / frame terms
- CH2 + ch2_value(kw, kws)               -> default table for the cittuppāda chapters (2-01 ... 2-05)
                                            with the context rules settled on the 2-01 sample
- MATRIX                                 -> matrix item names as settled in 1-matika (default per keyword)
- build_part(part, resolver)             -> writes <part>.mapped.md; resolver(id, kw, kws) returns the value
- verify(part)                           -> the brief's structural check + the presence check; prints a report

Vietnamese has no inflection, so the presence check is literal: NFC, case-insensitive, word-bounded,
with punctuation (, ; : . ? ! quotes, dashes, "…") treated as a space and variant brackets [..] removed
(a word that survives only inside a variant bracket is NOT present). A value split by " … " (a
discontinuous rendering) or " / " is checked part by part, " … " parts in order of appearance.
"""
import pathlib
import re
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
VI_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
NDE = "(no direct equivalent)"
GAP = " … "  # discontinuous Vietnamese (e.g. samaye X = «vào lúc ấy … X»)


# ---------------------------------------------------------------------------- reading
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def _segments(path):
    segs = {}
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
        block = block.strip()
        if not block:
            continue
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", block)
        if m:
            segs[m.group(1)] = block[: m.start()].strip()
    return segs


def read_vietnamese(part):
    return _segments(VI_DIR / f"{part}.md")


def read_pali(part):
    return _segments(PI_DIR / f"{part}.md")


# ---------------------------------------------------------------------------- presence check
def _norm(t):
    t = unicodedata.normalize("NFC", t)
    t = re.sub(r"\s*\[[^\]]*\]", " ", t)                    # variant brackets
    t = t.lower()
    t = re.sub(r"[,;:.?!“”‘’\"()–—…#]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def present(value, text):
    if value == NDE:
        return True
    t = _norm(text)
    for alt in value.split(" / "):
        pos, ok = 0, True
        for part in alt.split(GAP):
            p = _norm(part)
            if not p:
                continue
            m = re.compile(r"(?<!\w)" + re.escape(p) + r"(?!\w)").search(t, pos)
            if not m:
                ok = False
                break
            pos = m.end()
        if not ok:
            return False
    return True


def lc(kw):
    return kw[:1].lower() + kw[1:]


# ---------------------------------------------------------------------------- preamble / frame
CORE = {
    "abhidhamma": "Vi Diệu Pháp", "abhidhammapiṭake": "Tạng Vi Diệu Pháp",
    "saṅgaṇī": "liệt kê", "dhammasaṅgaṇī": "Liệt kê các hiện tượng", "dhamma": "hiện tượng",
    "namo": "Kính lễ", "bhagavato": "Đức Thế Tôn", "arahato": "bậc A-la-hán", "sammā": "Hoàn Toàn",
    "sambuddhassa": "bậc Tự Giác Ngộ", "sammāsambuddhassa": "bậc Tự Giác Ngộ Hoàn Toàn",
}

# ---------------------------------------------------------------------------- CH2 default table
# Pāli keyword (lower-case first letter) -> Vietnamese as the 2-01 translation writes it.
CH2 = {
    # frame / opening of each type of mind
    "kusalā": "thiện", "kusalaṃ": "thiện", "kusala": "thiện",
    "kusalaṃ cittaṃ": "tâm thiện", "dhammā kusalā": "hiện tượng thiện",
    "akusalānaṃ": "bất thiện", "akusalānaṃ dhammānaṃ": "hiện tượng … bất thiện",
    "kāma": "dục lạc", "kāmāvacaraṃ": "thuộc cõi dục lạc", "kāmāvacara": "thuộc cõi dục lạc",
    "avacaraṃ": "thuộc cõi", "avacara": "thuộc cõi",
    "cittaṃ": "tâm", "citta": "tâm", "cittassa": "tâm", "cittāni": "tâm",
    "uppannaṃ": "sinh khởi", "uppāda": "sự sinh khởi", "cittuppāda": "sự sinh khởi của tâm",
    "kaṇḍaṃ": "phần",
    "sahagataṃ": "đi kèm", "somanassasahagataṃ": "có niềm vui đi kèm",
    "upekkhāsahagataṃ": "có sự bình thản đi kèm", "somanassa": "niềm vui", "upekkhā": "sự bình thản",
    "somanassindriyaṃ": "năng lực niềm vui", "upekkhindriyaṃ": "năng lực bình thản",
    "ñāṇa": "hiểu biết", "sampayuttaṃ": "gắn liền", "vippayuttaṃ": "không gắn liền",
    "ñāṇavippayuttaṃ": "không gắn liền với hiểu biết", "saṅkhārena": "sự thúc đẩy",
    "rūpa": "hình sắc", "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị",
    "phoṭṭhabba": "vật xúc chạm",
    "ārammaṇaṃ": "đối tượng", "ārabbha": "lấy … làm", "yaṃ yaṃ": "bất cứ thứ gì",
    "samuppannā": "sinh khởi", "samuppannā arūpino": "phi vật chất … sinh khởi",
    "samuppannā arūpino dhammā": "hiện tượng phi vật chất … sinh khởi",
    "paṭicca": "tùy thuộc vào điều kiện",
    "paṭiccasamuppannā": "sinh khởi tùy thuộc vào điều kiện",
    "paṭiccasamuppannā arūpino": "phi vật chất … sinh khởi tùy thuộc vào điều kiện",
    "arūpino": "phi vật chất", "arūpino dhammā": "hiện tượng phi vật chất",
    "arūpīnaṃ": "phi vật chất", "arūpīnaṃ dhammānaṃ": "hiện tượng phi vật chất",
    "yo": "điều", "yā": "điều", "yaṃ": "điều", "ye": "bất cứ … nào",
    "ṭhapetvā": "ngoại trừ",
    # contact, feeling, perception, intention, mind
    "phasso": "sự tiếp xúc", "phassa": "sự tiếp xúc", "phusanā": "sự chạm",
    "saṃphusanā": "sự chạm đến",
    "vedanā": "cảm giác", "vedayitaṃ": "cảm nhận",
    "saññā": "tri giác", "sañjānanā": "sự nhận ra", "sañjānitattaṃ": "trạng thái đã nhận ra",
    "cetanā": "chủ ý", "sañcetanā": "sự cố ý", "cetayitattaṃ": "trạng thái đã cố ý",
    "manosañcetanā": "chủ ý của ý", "mano": "ý",
    "āhāro": "dưỡng chất", "āhārā": "loại dưỡng chất",
    "mānasaṃ": "tâm trí", "hadayaṃ": "tấm lòng", "paṇḍaraṃ": "sự sáng ngời",
    "mana": "ý", "manāyatanaṃ": "lĩnh vực ý", "manindriyaṃ": "năng lực ý",
    "viññāṇaṃ": "thức", "viññāṇa": "thức",
    "khandho": "khối", "khandhā": "khối", "khandhassa": "khối",
    "viññāṇakkhandho": "khối thức", "viññāṇakkhandhaṃ": "khối thức",
    "viññāṇakkhandhassa": "khối thức",
    "vedanākkhandho": "khối cảm giác", "vedanākkhandhaṃ": "khối cảm giác",
    "vedanākkhandhassa": "khối cảm giác",
    "saññākkhandho": "khối tri giác", "saññākkhandhaṃ": "khối tri giác",
    "saññākkhandhassa": "khối tri giác",
    "saṅkhārakkhandho": "khối tạo tác", "saṅkhārakkhandhaṃ": "khối tạo tác",
    "saṅkhārakkhandhassa": "khối tạo tác",
    "saṅkhāra": "tạo tác",
    "tajjā": "tương ứng", "dhātu": "yếu tố", "dhātuyo": "yếu tố",
    "manoviññāṇa": "ý thức", "manoviññāṇadhātu": "yếu tố ý thức",
    "dhamma": "đối tượng của ý",  # stem of dhammārammaṇa / dhammāyatana / dhammadhātu
    "dhammāyatanaṃ": "lĩnh vực đối tượng của ý", "dhammadhātu": "yếu tố đối tượng của ý",
    "āyatanāni": "lĩnh vực nhận biết", "indriyaṃ": "năng lực", "indriyāni": "năng lực",
    # feeling string
    "samphassajaṃ": "sinh từ sự tiếp xúc", "samphassajā": "sinh từ sự tiếp xúc",
    "cetosamphassajaṃ": "sinh từ sự tiếp xúc của tâm",
    "cetosamphassajā": "sinh từ sự tiếp xúc của tâm",
    "cetasikaṃ": "trong tâm", "sātaṃ": "khoan khoái", "asātaṃ": "bứt rứt",
    "cetasikaṃ sātaṃ": "sự khoan khoái trong tâm", "cetasikaṃ sukhaṃ": "sự dễ chịu trong tâm",
    "sukhaṃ": "hạnh phúc", "sukhā": "dễ chịu",
    "sukhaṃ vedayitaṃ": "cảm nhận … dễ chịu", "sukhā vedanā": "cảm giác … dễ chịu",
    "adukkhamasukhaṃ": "không khó chịu cũng không dễ chịu",
    "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ":
        "cảm nhận không khó chịu cũng không dễ chịu sinh từ sự tiếp xúc của tâm",
    "cetosamphassajā adukkhamasukhā vedanā":
        "cảm giác không khó chịu cũng không dễ chịu sinh từ sự tiếp xúc của tâm",
    # vitakka / vicāra / pīti strings
    "vitakko": "sự hướng tâm", "takko": "suy nghĩ", "saṅkappo": "tư duy",
    "appanā": "sự gắn tâm", "cetaso": "tâm", "abhiniropanā": "sự đặt … vào đối tượng",
    "vicāro": "sự duy trì tâm", "cāro": "sự chuyển động của tâm",
    "anusandhānatā": "sự gắn kết liên tục … với đối tượng",
    "anupekkhanatā": "sự theo dõi sát đối tượng",
    "pīti": "sự hân hoan", "pāmojjaṃ": "sự phấn khởi", "āmodanā": "sự vui vẻ",
    "pamodanā": "sự vui thích", "hāso": "sự tươi cười", "pahāso": "sự rạng rỡ",
    "vitti": "sự mãn nguyện", "odagyaṃ": "sự phấn chấn", "attamanatā": "sự hài lòng",
    # samādhi string (Vietnamese fuses citta + ekaggatā into «sự nhất tâm»)
    "ekaggatā": "sự nhất tâm", "cittassekaggatā": "sự nhất tâm",
    "ṭhiti": "sự ổn định", "cittassa ṭhiti": "sự ổn định của tâm", "saṇṭhiti": "sự vững vàng",
    "avaṭṭhiti": "sự vững chãi", "avisāhāro": "sự không phân tán",
    "avikkhepo": "sự không tán loạn", "avisāhaṭa": "không phân tán",
    "avisāhaṭamānasatā": "trạng thái tâm trí không phân tán", "mānasatā": "tâm trí",
    "samatho": "sự tĩnh lặng", "samādhi": "định tâm",
    "samādhindriyaṃ": "năng lực định tâm", "samādhibalaṃ": "sức mạnh định tâm",
    "balaṃ": "sức mạnh", "balāni": "sức mạnh", "sammā": "đúng đắn",
    # saddhā string
    "saddhā": "niềm tin", "saddahanā": "sự tin tưởng", "okappanā": "sự tin chắc",
    "abhippasādo": "lòng tin sâu sắc", "saddhindriyaṃ": "năng lực niềm tin",
    "saddhābalaṃ": "sức mạnh niềm tin",
    # vīriya string
    "cetasiko": "trong tâm", "cetasiko vīriyārambho": "sự khởi động tinh tấn trong tâm",
    "ārambho": "sự khởi động", "nikkamo": "sự dấn bước", "parakkamo": "sự xông pha",
    "uyyāmo": "sự gắng sức", "vāyāmo": "nỗ lực", "ussāho": "sự hăng hái",
    "ussoḷhī": "sự bền chí", "thāmo": "sức bền", "dhiti": "sự kiên trì",
    "asithila": "không lơi lỏng", "nikkhitta": "buông bỏ", "chandatā": "ý muốn",
    "dhuratā": "gánh", "sampaggāho": "sự dốc sức",
    "vīriyindriyaṃ": "năng lực tinh tấn", "vīriyabalaṃ": "sức mạnh tinh tấn",
    "paggāho": "sự dốc sức",
    # sati string
    "sati": "sự tỉnh thức", "anussati": "sự nhớ lại", "paṭissati": "sự hồi tưởng",
    "saraṇatā": "sự ghi nhớ", "dhāraṇatā": "sự gìn giữ trong trí nhớ",
    "pilāpanatā": "hời hợt", "sammussanatā": "quên lãng",
    "satindriyaṃ": "năng lực tỉnh thức", "satibalaṃ": "sức mạnh tỉnh thức",
    # paññā string
    "paññā": "trí tuệ", "pajānanā": "sự hiểu rõ", "vicayo": "sự tìm hiểu",
    "pavicayo": "sự tìm hiểu kỹ", "dhammavicayo": "sự tìm hiểu các hiện tượng",
    "sallakkhaṇā": "sự nhận xét", "upalakkhaṇā": "sự nhận diện",
    "paccupalakkhaṇā": "sự nhận diện chính xác", "paṇḍiccaṃ": "sự thông thái",
    "kosallaṃ": "sự khéo léo", "nepuññaṃ": "sự tinh tường", "vebhabyā": "sự phân biệt sáng suốt",
    "cintā": "sự suy tư", "upaparikkhā": "sự khảo sát", "bhūrī": "sự sâu rộng",
    "medhā": "sự thông minh", "pariṇāyikā": "sự dẫn dắt", "vipassanā": "sự thấu suốt",
    "sampajaññaṃ": "sự hiểu biết rõ ràng", "patodo": "cây roi thúc",
    "paññindriyaṃ": "năng lực trí tuệ", "paññābalaṃ": "sức mạnh trí tuệ",
    "satthaṃ": "thanh gươm", "paññāsatthaṃ": "thanh gươm trí tuệ",
    "pāsādo": "lâu đài", "paññāpāsādo": "lâu đài trí tuệ",
    "āloko": "ánh sáng", "paññāāloko": "ánh sáng trí tuệ",
    "obhāso": "hào quang", "paññāobhāso": "hào quang trí tuệ",
    "pajjoto": "ngọn đuốc", "paññāpajjoto": "ngọn đuốc trí tuệ",
    "ratanaṃ": "viên ngọc", "paññāratanaṃ": "viên ngọc trí tuệ",
    "amoho": "sự không si mê", "diṭṭhi": "quan điểm",
    # jīvita string
    "jīvita": "sống", "jīvitindriyaṃ": "năng lực sống", "āyu": "tuổi thọ",
    "yapanā": "sự tiếp diễn", "yāpanā": "sự kéo dài", "iriyanā": "sự vận động",
    "vattanā": "sự tiến triển", "pālanā": "sự gìn giữ",
    # hiri / ottappa (stem = the form inside «sức mạnh …»; the factor carries «sự»)
    "hirīyati": "hổ thẹn", "hiri": "biết hổ thẹn", "hirī": "sự biết hổ thẹn",
    "hiribalaṃ": "sức mạnh biết hổ thẹn",
    "ottappati": "ghê sợ", "ottappa": "biết ghê sợ tội lỗi", "ottappaṃ": "sự biết ghê sợ tội lỗi",
    "ottappabalaṃ": "sức mạnh biết ghê sợ tội lỗi", "pāpakānaṃ": "xấu ác",
    "samāpattiyā": "để … xảy ra nơi mình",
    # roots (fragments that lost a- keep the positive part)
    "alobho": "sự không tham lam", "lubbhanā": "khởi lòng tham",
    "asārāgo": "sự không say đắm", "sārajjanā": "bị cuốn hút",
    "anabhijjhā": "sự không thèm muốn", "mūlaṃ": "gốc rễ", "kusalamūlaṃ": "gốc rễ thiện",
    "adoso": "sự không sân hận", "dussanā": "khởi sân",
    "abyāpādo": "sự không ác ý", "abyāpajjo": "sự không thù hằn", "byāpajjo": "thù hằn",
    "hetū": "gốc rễ",
    # the six pairs (kāya = the mental body = the three mental aggregates)
    "kāya": "thân tinh thần",
    "passaddhi": "sự an tịnh", "cittapassaddhi": "sự an tịnh của tâm",
    "passambhanā": "sự lắng dịu", "passambhitattaṃ": "trạng thái đã lắng dịu",
    "paṭipassambhitattaṃ": "trạng thái đã lắng dịu hoàn toàn",
    "lahutā": "sự nhẹ nhàng", "cittalahutā": "sự nhẹ nhàng của tâm", "lahu": "nhanh nhẹn",
    "adandhanatā": "sự không chậm chạp", "dandhanatā": "chậm chạp", "vitthanatā": "trì trệ",
    "mudutā": "sự mềm mại", "cittamudutā": "sự mềm mại của tâm", "maddavatā": "sự mềm mỏng",
    "akakkhaḷatā": "sự không thô cứng", "kakkhaḷatā": "thô cứng", "kathinatā": "cứng nhắc",
    "kammaññatā": "sự dễ vận dụng", "cittakammaññatā": "sự dễ vận dụng của tâm",
    "kammaññattaṃ": "trạng thái dễ vận dụng", "bhāvo": "tính chất",
    "pāguññatā": "sự thuần thục", "cittapāguññatā": "sự thuần thục của tâm",
    "paguṇattaṃ": "trạng thái thuần thục",
    "ujutā": "sự thẳng", "ujukatā": "sự ngay thẳng", "cittujukatā": "sự ngay thẳng của tâm",
    "ajimhatā": "sự không quanh co", "jimhatā": "quanh co", "vaṅkatā": "cong queo",
    "kuṭilatā": "vặn vẹo",
    # summaries (koṭṭhāsavāra / suññatavāra)
    "jhānaṃ": "tầng thiền", "maggo": "con đường",
    "pañcaṅgikaṃ": "gồm năm chi phần", "pañcaṅgiko": "gồm năm chi phần",
    "caturaṅgikaṃ": "gồm bốn chi phần", "caturaṅgiko": "gồm bốn chi phần",
    "caturaṅgiko maggo": "con đường gồm bốn chi phần",
    # headings and colophons
    "bhājanī": "phân tích", "bhājanīyaṃ": "phân tích", "bhāṇa": "tụng đọc", "vāro": "mục",
    "koṭṭhāsa": "thành phần", "suññata": "sự trống rỗng",
    "paṭhamaṃ": "thứ nhất", "dutiyaṃ": "thứ hai", "tatiyaṃ": "thứ ba", "catutthaṃ": "thứ tư",
    "pañcamaṃ": "thứ năm", "chaṭṭhaṃ": "thứ sáu", "sattamaṃ": "thứ bảy", "aṭṭhamaṃ": "thứ tám",
}

# The sati word as the segment writes it: the factor «sự tỉnh thức»; but «tỉnh thức» in the summary
# lists where sati occurs only inside năng lực / sức mạnh / … đúng đắn.
SATI_BARE = "tỉnh thức"


def ch2_value(kw, kws, table=CH2):
    """Default value with the context rules settled for the cittuppāda chapters."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k.startswith("samaye "):                        # Yo/Yā/Yaṃ tasmiṃ samaye X …
        return "vào lúc ấy" + GAP + ch2_value(k[len("samaye "):], kws, table)
    if k == "sukhaṃ" and "cetasikaṃ sukhaṃ" in s:      # feeling string: «sự dễ chịu trong tâm»
        return "dễ chịu"                               # (sukha headings 1-10 / 1-87: overrides)
    if k == "ṭhiti" and "āyu" in s:                    # jīvitindriya string
        return "sự tồn tại"
    if k == "jīvita" and "āyu" in s:                   # jīvitaṃ inside the jīvitindriya string
        return "sự sống"
    if k == "cetasikaṃ" and "adukkhamasukhaṃ" in s:    # cetasikaṃ neva sātaṃ nāsātaṃ
        return "trạng thái trong tâm"
    if k == "sañcetanā" and "cetayitattaṃ" not in s:   # only inside manosañcetanā
        return "chủ ý"
    if k == "vāyāmo" and "asithila" in s:              # vīriya string: «sự nỗ lực»
        return "sự nỗ lực"
    if k == "vāro" and "bhāṇa" in s:                   # Paṭhama/Dutiyabhāṇavāro: «Phần tụng đọc …»
        return "phần"
    return table[k]


# ---------------------------------------------------------------------------- MATRIX (1-matika)
# Default per keyword; segment-specific readings are overrides in map_sample_vi.py (OVERRIDES).
# Bare adjective / predicate: without the predicate «là»; a phrase with dhammā: the item name as written
# without the leading «các» (an inner «là» stays: «hiện tượng là đối tượng của ô nhiễm»).
def _group(stem, plural, x, niya, aniya=None):
    d = {stem: x, plural: x,
         niya: f"đối tượng của {x}", f"{niya} dhammā": f"hiện tượng là đối tượng của {x}",
         f"{stem}vippayuttā": f"không gắn liền với {x}"}
    if aniya:
        d[f"{aniya} dhammā"] = f"hiện tượng không phải là đối tượng của {x}"
    return d


MATRIX = {
    "mātikā": "ma trận", "duka": "bộ đôi", "dukaṃ": "bộ đôi", "antara": "xen giữa",
    "antaradukaṃ": "bộ đôi xen giữa", "piṭṭhi": "cuối", "suttantika": "kinh",
    "abhidhamma": "Vi Diệu Pháp",
    "hetu": "gốc rễ", "hetū": "gốc rễ",
    "dhammā": "hiện tượng",
    # triads
    "kusalā": "thiện", "kusalā dhammā": "hiện tượng thiện", "akusalā": "bất thiện",
    "akusalā dhammā": "hiện tượng bất thiện", "abyākatā": "không xác định về mặt đạo đức",
    "abyākatā dhammā": "hiện tượng không xác định về mặt đạo đức",
    "sampayuttā": "gắn liền", "vippayuttā": "không gắn liền",
    "vippayuttā dhammā": "hiện tượng không gắn liền",
    "vedanāya": "cảm giác", "dukkhāya": "khó chịu", "dukkhāya vedanāya": "cảm giác khó chịu",
    "sukhāya": "dễ chịu", "sukhāya vedanāya": "cảm giác dễ chịu",
    "adukkhamasukhāya": "không khó chịu cũng không dễ chịu",
    "vipākadhamma": "có khả năng sinh ra quả",
    "vipākadhammadhammā": "hiện tượng có khả năng sinh ra quả",
    "upādiṇṇa": "do nghiệp tạo ra", "upādiṇṇā": "do nghiệp tạo ra",
    "upādiṇṇā dhammā": "hiện tượng do nghiệp tạo ra",
    "anupādiṇṇā dhammā": "hiện tượng không do nghiệp tạo ra",
    "upādiṇṇupādāniyā": "do nghiệp tạo ra và là đối tượng của sự bám víu",
    "anupādiṇṇupādāniyā": "không do nghiệp tạo ra nhưng là đối tượng của sự bám víu",
    "upādiṇṇupādāniyā dhammā": "hiện tượng do nghiệp tạo ra và là đối tượng của sự bám víu",
    "anupādiṇṇupādāniyā dhammā":
        "hiện tượng không do nghiệp tạo ra nhưng là đối tượng của sự bám víu",
    "anupādiṇṇaanupādāniyā dhammā":
        "hiện tượng không do nghiệp tạo ra và không phải là đối tượng của sự bám víu",
    "saṃkiliṭṭha": "bị phiền não làm vẩn đục", "saṃkiliṭṭhā": "bị phiền não làm vẩn đục",
    "asaṃkiliṭṭha": "không bị phiền não làm vẩn đục",
    "asaṃkiliṭṭhā": "không bị phiền não làm vẩn đục",
    "saṃkiliṭṭhā dhammā": "hiện tượng bị phiền não làm vẩn đục",
    "asaṃkiliṭṭhā dhammā": "hiện tượng không bị phiền não làm vẩn đục",
    "saṃkilesikā": "đối tượng của phiền não",
    "saṃkilesikā dhammā": "hiện tượng là đối tượng của phiền não",
    "asaṃkilesikā dhammā": "hiện tượng không phải là đối tượng của phiền não",
    "vitakka": "sự hướng tâm", "vitakkā": "sự hướng tâm", "vicāra": "sự duy trì tâm",
    "vicārā": "sự duy trì tâm",
    "savitakkasavicārā dhammā": "hiện tượng có sự hướng tâm và sự duy trì tâm",
    "avitakkavicāramattā dhammā": "hiện tượng không có sự hướng tâm chỉ có sự duy trì tâm",
    "savitakkā dhammā": "hiện tượng có sự hướng tâm",
    "avitakkā dhammā": "hiện tượng không có sự hướng tâm",
    "savicārā dhammā": "hiện tượng có sự duy trì tâm",
    "avicārā dhammā": "hiện tượng không có sự duy trì tâm",
    "sahagatā": "đi kèm", "sahagatā dhammā": "hiện tượng có … đi kèm",
    "pītisahagatā": "có sự hân hoan đi kèm", "sukhasahagatā": "có hạnh phúc đi kèm",
    "upekkhāsahagatā": "có sự bình thản đi kèm",
    "na pītisahagatā dhammā": "hiện tượng không có sự hân hoan đi kèm",
    "na sukhasahagatā dhammā": "hiện tượng không có hạnh phúc đi kèm",
    "na upekkhāsahagatā dhammā": "hiện tượng không có sự bình thản đi kèm",
    "pīti": "sự hân hoan", "sukha": "hạnh phúc", "upekkhā": "sự bình thản",
    "pītikā": "có sự hân hoan", "sappītikā dhammā": "hiện tượng có sự hân hoan",
    "appītikā dhammā": "hiện tượng không có sự hân hoan",
    "pahātabbā": "cần dứt bỏ", "bhāvanāya pahātabbā": "cần dứt bỏ bằng sự tu tập",
    "pahātabba": "cần dứt bỏ", "bhāvanāya pahātabba": "cần dứt bỏ bằng sự tu tập",
    "dassanena": "sự thấy chân lý", "hetukā": "có gốc rễ", "hetukā dhammā": "hiện tượng có gốc rễ",
    "ācaya": "sự tích lũy", "apacaya": "sự giảm trừ", "gāmino dhammā": "hiện tượng dẫn đến",
    "sekkhā": "thuộc về người còn đang tu học", "asekkhā": "thuộc về người đã hoàn tất tu học",
    "parittā": "hạn hẹp", "parittā dhammā": "hiện tượng hạn hẹp", "paritta": "hạn hẹp",
    "mahaggatā": "rộng lớn", "mahaggatā dhammā": "hiện tượng rộng lớn", "mahaggata": "rộng lớn",
    "appamāṇā": "không thể đo lường", "appamāṇā dhammā": "hiện tượng không thể đo lường",
    "appamāṇa": "không thể đo lường",
    "ārammaṇā": "có đối tượng", "parittārammaṇā": "có đối tượng hạn hẹp",
    "mahaggatārammaṇā": "có đối tượng rộng lớn",
    "appamāṇārammaṇā": "có đối tượng không thể đo lường",
    "hīnā": "thấp kém", "hīnā dhammā": "hiện tượng thấp kém", "majjhimā": "trung bình",
    "majjhimā dhammā": "hiện tượng trung bình", "paṇītā": "ưu việt",
    "paṇītā dhammā": "hiện tượng ưu việt",
    "micchatta": "hướng sai lầm", "sammatta": "hướng đúng đắn", "niyatā": "cố định",
    "niyatā dhammā": "hiện tượng cố định",
    "magga": "con đường", "adhipatino": "lấy … làm yếu tố chủ đạo",
    "uppannā": "đã sinh khởi", "uppannā dhammā": "hiện tượng đã sinh khởi",
    "uppādino": "sẽ sinh khởi",
    "atītā dhammā": "hiện tượng thuộc quá khứ", "anāgatā dhammā": "hiện tượng thuộc tương lai",
    "paccuppannā dhammā": "hiện tượng thuộc hiện tại",
    "atītārammaṇā": "có đối tượng thuộc quá khứ", "anāgatārammaṇā": "có đối tượng thuộc tương lai",
    "paccuppannārammaṇā": "có đối tượng thuộc hiện tại",
    "bahiddhā": "ở bên ngoài bản thân", "bahiddhā dhammā": "hiện tượng ở bên ngoài bản thân",
    "sanidassana": "thấy được", "anidassana": "không thấy được", "sappaṭighā": "có tính va chạm",
    # short intermediate pairs
    "sahetukā dhammā": "hiện tượng có gốc rễ", "ahetukā dhammā": "hiện tượng không có gốc rễ",
    "appaccayā dhammā": "hiện tượng không có điều kiện",
    "saṅkhatā": "do điều kiện tạo thành", "saṅkhatā dhammā": "hiện tượng do điều kiện tạo thành",
    "asaṅkhatā": "không do điều kiện tạo thành",
    "asaṅkhatā dhammā": "hiện tượng không do điều kiện tạo thành",
    "sanidassanā": "thấy được", "sanidassanā dhammā": "hiện tượng thấy được",
    "anidassanā": "không thấy được", "anidassanā dhammā": "hiện tượng không thấy được",
    "sappaṭighā dhammā": "hiện tượng có tính va chạm",
    "rūpino": "thuộc vật chất", "rūpino dhammā": "hiện tượng thuộc vật chất",
    "arūpino": "phi vật chất", "arūpino dhammā": "hiện tượng phi vật chất",
    "lokiyā": "thuộc thế gian", "lokiyā dhammā": "hiện tượng thuộc thế gian", "uttarā": "vượt",
    "lokuttarā dhammā": "hiện tượng vượt thế gian", "na": "không", "viññeyyā": "có thể nhận biết",
    # clusters (gocchaka): stem = plural form = the core noun
    **_group("āsava", "āsavā", "ô nhiễm", "sāsavā"),
    "anāsavā": "không phải là đối tượng của ô nhiễm",
    "anāsavā dhammā": "hiện tượng không phải là đối tượng của ô nhiễm",
    **_group("saṃyojana", "saṃyojanā", "xiềng xích", "saṃyojaniyā", "asaṃyojaniyā"),
    **_group("gantha", "ganthā", "nút thắt", "ganthaniyā", "aganthaniyā"),
    **_group("ogha", "oghā", "dòng lũ", "oghaniyā", "anoghaniyā"),
    **_group("yoga", "yogā", "ách", "yoganiyā", "ayoganiyā"),
    **_group("nīvaraṇa", "nīvaraṇā", "chướng ngại", "nīvaraṇiyā", "anīvaraṇiyā"),
    **_group("upādāna", "upādānā", "sự bám víu", "upādāniyā", "anupādāniyā"),
    "parāmāsa": "sự hiểu sai lệch", "parāmāsā": "sự hiểu sai lệch",
    "parāmaṭṭhā": "bị sự hiểu sai lệch nắm giữ",
    "parāmaṭṭhā dhammā": "hiện tượng bị sự hiểu sai lệch nắm giữ",
    "parāmāsavippayuttā": "không gắn liền với sự hiểu sai lệch",
    "kilesa": "phiền não", "kilesā": "phiền não", "kilesavippayuttā": "không gắn liền với phiền não",
    # great intermediate pairs
    "cittā": "tâm", "cetasikā": "đồng hành với tâm", "citta": "tâm",
    "cittavippayuttā": "không gắn liền với tâm",
    "saṃsaṭṭhā": "hòa lẫn", "cittasaṃsaṭṭhā": "hòa lẫn với tâm", "saṃsaṭṭha": "hòa lẫn",
    "saṃsaṭṭhā dhammā": "hiện tượng hòa lẫn", "visaṃsaṭṭhā dhammā": "hiện tượng không hòa lẫn",
    "samuṭṭhānā": "do … sinh ra", "samuṭṭhāna": "do … sinh ra", "cittasamuṭṭhānā": "do tâm sinh ra",
    "samuṭṭhānā dhammā": "hiện tượng do … sinh ra",
    "no cittasamuṭṭhānā dhammā": "hiện tượng không do tâm sinh ra",
    "sahabhuno": "cùng tồn tại", "cittasahabhuno": "cùng tồn tại với tâm",
    "cittasahabhuno dhammā": "hiện tượng cùng tồn tại với tâm",
    "no cittasahabhuno dhammā": "hiện tượng không cùng tồn tại với tâm",
    "anuparivattino": "vận hành theo", "cittānuparivattino": "vận hành theo tâm",
    "anuparivattino dhammā": "hiện tượng vận hành theo",
    "cittānuparivattino dhammā": "hiện tượng vận hành theo tâm",
    "no cittānuparivattino dhammā": "hiện tượng không vận hành theo tâm",
    "cittasaṃsaṭṭhasamuṭṭhānā": "vừa hòa lẫn với tâm vừa do tâm sinh ra",
    "saṃsaṭṭhasamuṭṭhānā dhammā": "hiện tượng vừa hòa lẫn … vừa do tâm sinh ra",
    "no cittasaṃsaṭṭhasamuṭṭhānā dhammā":
        "hiện tượng không phải vừa hòa lẫn với tâm vừa do tâm sinh ra",
    "saṃsaṭṭhasamuṭṭhānasahabhuno dhammā":
        "hiện tượng vừa hòa lẫn … vừa do tâm sinh ra vừa cùng tồn tại với tâm",
    "no cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā":
        "hiện tượng không phải vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino":
        "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
    "saṃsaṭṭhasamuṭṭhānānuparivattino dhammā":
        "hiện tượng vừa hòa lẫn … vừa do tâm sinh ra vừa vận hành theo tâm",
    "no cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā":
        "hiện tượng không phải vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
    "ajjhattikā": "thuộc phần bên trong", "ajjhattikā dhammā": "hiện tượng thuộc phần bên trong",
    "bāhirā": "thuộc phần bên ngoài", "bāhirā dhammā": "hiện tượng thuộc phần bên ngoài",
    "upādā": "phái sinh", "upādā dhammā": "hiện tượng phái sinh",
    # closing pairs
    "kāma": "dục lạc", "kāmāvacarā": "thuộc cõi dục lạc", "avacarā": "thuộc cõi",
    "rūpa": "hình sắc", "rūpāvacarā": "thuộc cõi hình sắc",
    "arūpa": "không hình sắc", "arūpāvacarā": "thuộc cõi không hình sắc",
    "pariyāpannā dhammā": "hiện tượng nằm trong các cõi tồn tại",
    "apariyāpannā dhammā": "hiện tượng không nằm trong các cõi tồn tại",
    "niyyānikā": "dẫn đến giải thoát", "niyyānikā dhammā": "hiện tượng dẫn đến giải thoát",
    "sauttarā": "còn có điều cao hơn", "sauttarā dhammā": "hiện tượng còn có điều cao hơn",
    "anuttarā": "không có điều gì cao hơn", "anuttarā dhammā": "hiện tượng không có điều gì cao hơn",
    "raṇā": "xung đột", "saraṇā dhammā": "hiện tượng có xung đột",
    "araṇā dhammā": "hiện tượng không có xung đột",
    # suttanta pairs
    "vijjā": "hiểu biết chân thật", "avijjā": "vô minh", "bhāgino dhammā": "hiện tượng thuộc về phía",
    "vijju": "tia chớp", "vajira": "kim cương", "upamā": "giống như",
    "vijjūpamā dhammā": "hiện tượng giống như tia chớp",
    "bālā": "thuộc về kẻ ngu", "bālā dhammā": "hiện tượng thuộc về kẻ ngu",
    "paṇḍitā": "thuộc về người trí", "paṇḍitā dhammā": "hiện tượng thuộc về người trí",
    "kaṇhā": "đen tối", "kaṇhā dhammā": "hiện tượng đen tối", "sukkā": "trong sáng",
    "sukkā dhammā": "hiện tượng trong sáng", "tapanīyā": "gây dằn vặt",
    "adhivacanā": "tên gọi", "nirutti": "cách diễn đạt", "paññatti": "khái niệm", "pathā": "phạm vi",
    "nāmañca": "phần tinh thần", "rūpañca": "phần vật chất",
    "bhava": "sự hiện hữu", "vibhava": "sự không hiện hữu", "taṇhā": "khao khát",
    "diṭṭhi": "quan điểm",
    "sassata": "sự trường tồn", "sassatadiṭṭhi": "quan điểm về sự trường tồn",
    "uccheda": "sự đoạn diệt", "ucchedadiṭṭhi": "quan điểm về sự đoạn diệt",
    "anudiṭṭhi": "quan điểm về",
    "ahirikañca": "sự không biết hổ thẹn", "anottappañca": "sự không biết ghê sợ tội lỗi",
    "hirī": "sự biết hổ thẹn", "ottappañca": "sự biết ghê sợ tội lỗi",
    "dovacassatā": "sự khó dạy bảo", "vacassatā": "dạy bảo", "sovacassatā": "sự dễ dạy bảo",
    "pāpa": "người xấu", "mittatā": "sự kết bạn",
    "kusalatā": "sự thành thạo", "āpatti": "lỗi vi phạm", "vuṭṭhāna": "việc ra khỏi",
    "vuṭṭhānakusalatā": "sự thành thạo về việc ra khỏi", "samāpatti": "thành tựu thiền",
    "dhātu": "yếu tố", "manasikāra": "sự chú tâm",
    "manasikārakusalatā": "sự thành thạo về sự chú tâm",
    "āyatana": "lĩnh vực nhận biết", "paṭicca": "tùy thuộc vào điều kiện",
    "samuppāda": "sự sinh khởi", "aṭṭhāna": "điều không thể xảy ra",
    "ajjavo": "sự ngay thật", "maddavo": "sự mềm mỏng", "khanti": "sự nhẫn nại",
    "soraccañca": "sự hiền hòa", "sākhalyañca": "sự hòa nhã", "paṭisanthāro": "sự niềm nở tiếp đón",
    "indriyesu": "giác quan", "gutta": "phòng hộ", "dvāratā": "cửa", "bhojane": "ăn uống",
    "mattaññutā": "biết tiết độ",
    "muṭṭhasaccañca": "sự mất tỉnh thức", "asampajaññañca": "sự thiếu hiểu biết rõ ràng",
    "sampajaññañca": "sự hiểu biết rõ ràng", "sati": "sự tỉnh thức",
    "paṭisaṅkhāna": "suy xét", "balañca": "sức mạnh",
    "samatho": "sự tĩnh lặng", "samatha": "sự tĩnh lặng", "vipassanā": "sự thấu suốt",
    "paggāha": "sự dốc sức", "paggāho": "sự dốc sức", "nimittañca": "dấu hiệu",
    "avikkhepo": "sự không tán loạn",
    "sīla": "giới hạnh", "vipatti": "sự suy đồi", "sampadā": "sự thành tựu",
    "visuddhi": "sự trong sạch", "yathā": "theo", "padhānaṃ": "sự nỗ lực",
    "saṃvego": "sự xúc động", "saṃvejaniyesu": "đáng xúc động", "ṭhānesu": "điều",
    "saṃviggassa": "người đã xúc động", "yoniso": "đúng cách",
    "santuṭṭhitā": "tự mãn", "kusalesu": "thiện", "kusalesu dhammesu": "hiện tượng thiện",
    "padhānasmiṃ": "nỗ lực",
    "vimutti": "sự giải thoát", "khaye": "sự diệt tận", "ñāṇaṃ": "hiểu biết",
    "anuppāde": "sự không sinh khởi", "niṭṭhitā": "đã hoàn tất",
}


# ---------------------------------------------------------------------------- build and verify
def build_part(part, resolver):
    """resolver(bid, kw, kws) -> Vietnamese value. Stops on an unmapped keyword."""
    lines, missing = [], []
    for bid, kws in read_keywords(part):
        pairs = []
        for kw in kws:
            try:
                v = resolver(bid, kw, kws)
            except KeyError:
                missing.append((bid, kw))
                v = "???"
            v = unicodedata.normalize("NFC", v)
            assert ", " not in v, (bid, kw, v)
            pairs.append(f"{kw}={v}")
        lines.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        raise SystemExit(f"{part}: unmapped keywords: {missing}")
    (HERE / f"{part}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(part, show=50):
    a = [l.split("] ", 1) for l in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    vi = read_vietnamese(part)
    nde, miss = 0, []
    for bid, rest in b:
        bid = bid[1:]
        text = vi.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
            elif text is None or not present(v, text):
                miss.append((bid, kw, v))
    print(part, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss))
    for m in miss[:show]:
        print("   MISS", *m)
    return bad, nde, miss
