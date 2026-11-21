"""Builder for the Vietnamese rails SAMPLE of pi-3 (Dhātukathā, «Thảo luận về các yếu tố», plain audience).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/preamble.md
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/1-uddeso.md
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/2-pathamanayo.md
  0-INBOX/temp/pipeline/pi-3-vi-ai/rails/vi-rails-formulas.md

Translated fresh from the Pāli (AI_translation/pali/pi-3_split_chapters) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md and the
pi-1 / pi-2 APPROVED decisions). Every Vietnamese string comes from the fixed constants below, so identical
Pāli gives byte-identical Vietnamese. Strings marked PI1 / PI2 are taken unchanged from the approved pi-1 / pi-2
Vietnamese rails; the build asserts that each of them still occurs there.

Later chapter builders may import the constants and functions (NAMES, DHAMMA_ATTR, counts_vi, answer_in,
answer_out, ...); importing writes nothing.

usage: python -I -X utf8 build_rails_sample_vi.py
"""
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-3_split_chapters"
OUT = ROOT / "AI_translation" / "vietnamese" / "pi-3-vietnamese-plain-rails_split_chapters"
RAILS = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-3-vi-ai" / "rails"
PI1_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
PI2_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-2-vietnamese-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def cap(s):
    """Upper-case the first letter (skipping an opening quote)."""
    for i, ch in enumerate(s):
        if ch.isalpha():
            return s[:i] + ch.upper() + s[i + 1:]
    return s


def low(s):
    for i, ch in enumerate(s):
        if ch.isalpha():
            return s[:i] + ch.lower() + s[i + 1:]
    return s


def spell(sig, word):
    """Spelling-only variant."""
    return f"[khác chính tả ({sig}): {word}]"


def reading(sig, word):
    """Variant with a different word or wording."""
    return f"[dị bản ({sig}): {word}]"


# ================================================================== book frame (user-approved 2026-11-20)
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"      # PI1
H_PITAKA = "Tạng Vi Diệu Pháp"                                               # PI1  Abhidhammapiṭake
H_BOOK = "Thảo luận về các yếu tố"                                           # Dhātukathāpāḷi
BOOK_PI1 = "Liệt kê các hiện tượng"                                          # PI1  dhammasaṅgaṇī (title)
COLOPHON = f"Bộ “{H_BOOK}” đã hoàn tất."                                     # end of ch15 (for later agents)

ORD = {1: "thứ nhất", 2: "thứ hai", 3: "thứ ba", 4: "thứ tư", 5: "thứ năm", 6: "thứ sáu", 7: "thứ bảy",
       8: "thứ tám", 9: "thứ chín", 10: "thứ mười", 11: "thứ mười một", 12: "thứ mười hai",
       13: "thứ mười ba", 14: "thứ mười bốn"}
CH_PALI = ["Paṭhamanayo", "Dutiyanayo", "Tatiyanayo", "Catutthanayo", "Pañcamanayo", "Chaṭṭhanayo",
           "Sattamanayo", "Aṭṭhamanayo", "Navamanayo", "Dasamanayo", "Ekādasamanayo", "Dvādasamanayo",
           "Terasamanayo", "Cuddasamanayo"]
CH_HEADINGS = {"Uddeso": "Phần nêu đề mục"}
CH_HEADINGS.update({p: f"Phương pháp {ORD[i]}" for i, p in enumerate(CH_PALI, 1)})
CH1_SECTIONS = {
    "Nayamātikā": "Ma trận các phương pháp",
    "Abbhantaramātikā": "Ma trận bên trong",
    "Nayamukhamātikā": "Ma trận lối vào các phương pháp",
    "Lakkhaṇamātikā": "Ma trận các đặc tính",
    "Bāhiramātikā": "Ma trận bên ngoài",
}

# the fourteen methods (X of «Giải thích đề mục về X»); key = Pāli as in the ^3-1 list
METHODS = [
    ("saṅgaho asaṅgaho", "Saṅgahāsaṅgaha", "sự gộp vào và sự không gộp vào"),
    ("saṅgahitena asaṅgahitaṃ", "Saṅgahitenaasaṅgahita", "điều không được gộp vào dựa trên điều được gộp vào"),
    ("asaṅgahitena saṅgahitaṃ", "Asaṅgahitenasaṅgahita", "điều được gộp vào dựa trên điều không được gộp vào"),
    ("saṅgahitena saṅgahitaṃ", "Saṅgahitenasaṅgahita", "điều được gộp vào dựa trên điều được gộp vào"),
    ("asaṅgahitena asaṅgahitaṃ", "Asaṅgahitenaasaṅgahita",
     "điều không được gộp vào dựa trên điều không được gộp vào"),
    ("sampayogo vippayogo", "Sampayogavippayoga", "sự gắn liền và sự không gắn liền"),
    ("sampayuttena vippayuttaṃ", "Sampayuttenavippayutta", "điều không gắn liền dựa trên điều gắn liền"),
    ("vippayuttena sampayuttaṃ", "Vippayuttenasampayutta", "điều gắn liền dựa trên điều không gắn liền"),
    ("sampayuttena sampayuttaṃ", "Sampayuttenasampayutta", "điều gắn liền dựa trên điều gắn liền"),
    ("vippayuttena vippayuttaṃ", "Vippayuttenavippayutta", "điều không gắn liền dựa trên điều không gắn liền"),
    ("saṅgahitena sampayuttaṃ vippayuttaṃ", "Saṅgahitenasampayuttavippayutta",
     "điều gắn liền và điều không gắn liền dựa trên điều được gộp vào"),
    ("sampayuttena saṅgahitaṃ asaṅgahitaṃ", "Sampayuttenasaṅgahitāsaṅgahita",
     "điều được gộp vào và điều không được gộp vào dựa trên điều gắn liền"),
    ("asaṅgahitena sampayuttaṃ vippayuttaṃ", "Asaṅgahitenasampayuttavippayutta",
     "điều gắn liền và điều không gắn liền dựa trên điều không được gộp vào"),
    ("vippayuttena saṅgahitaṃ asaṅgahitaṃ", "Vippayuttenasaṅgahitāsaṅgahita",
     "điều được gộp vào và điều không được gộp vào dựa trên điều không gắn liền"),
]
NIDDESO = "Giải thích đề mục về"                                             # X-padaniddeso
SEC_HEADINGS = {f"{stem}padaniddeso": f"{NIDDESO} {vi}" for _, stem, vi in METHODS}
PART = "phần"                                                                # closing line «…, phần thứ N.»
CLOSE_ORD = ["paṭhamo", "dutiyo", "tatiyo", "catuttho", "pañcamo", "chaṭṭho", "sattamo", "aṭṭhamo", "navamo",
             "dasamo", "ekādasamo", "dvādasamo", "terasamo", "cuddasamo"]
CLOSINGS = {f"{stem}padaniddeso {CLOSE_ORD[i]}.": f"{NIDDESO} {vi}, {PART} {ORD[i + 1]}."
            for i, (_, stem, vi) in enumerate(METHODS)}
SUB_HEADINGS = {   # ##### level
    "Khandho": "Các khối",
    "Āyatanaṃ": "Các lĩnh vực nhận biết",
    "Dhātu": "Các yếu tố",
    "Saccaṃ": "Các sự thật",
    "Indriyaṃ": "Các năng lực",
    "Paṭiccasamuppādādi": "Sự sinh khởi tùy thuộc vào điều kiện và các mục khác",
    "Khandhādi": "Các khối và các mục khác",
    "Saccādi": "Các sự thật và các mục khác",
    "Phassādisattakaṃ": "Nhóm bảy mục bắt đầu bằng sự tiếp xúc",
    "Tikaṃ": "Bộ ba",
    "Dukaṃ": "Bộ đôi",
}
ROUND_LABELS = {
    "(Ekamūlakaṃ.)": "(Phần xét từng mục một.)",
    "(Dukamūlakaṃ.)": "(Phần xét từng nhóm hai.)",
    "(Tikamūlakaṃ.)": "(Phần xét từng nhóm ba.)",
    "(Catukkamūlakaṃ.)": "(Phần xét từng nhóm bốn.)",
    "(Pañcakaṃ.)": "(Phần xét cả năm.)",
    # not in the approved list; built on the (Pañcakaṃ.) pattern
    "(Catukkaṃ.)": "(Phần xét cả bốn.)",
    "(Dvādasakaṃ.)": "(Phần xét cả mười hai.)",
    "(Aṭṭhārasakaṃ.)": "(Phần xét cả mười tám.)",
}

# ================================================================== numbers and the three categories
NUM = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười",
       11: "mười một", 12: "mười hai", 13: "mười ba", 14: "mười bốn", 15: "mười lăm", 16: "mười sáu",
       17: "mười bảy", 18: "mười tám", 22: "hai mươi hai"}
KHANDHA = "khối"                     # khandhehi / khandhena
AYATANA = "lĩnh vực nhận biết"       # āyatanehi / āyatanena
DHATU = "yếu tố"                     # dhātūhi / dhātuyā
CATS = (KHANDHA, AYATANA, DHATU)
IN = "được gộp vào"                  # saṅgahito / -ā / -aṃ / -āni
OUT_ = "không được gộp vào"          # asaṅgahito / -ā / -aṃ / -āni
HOW_MANY = "bao nhiêu"               # katihi
Q_IN = f"{IN} {HOW_MANY} {KHANDHA}, {HOW_MANY} {AYATANA} và {HOW_MANY} {DHATU}?"   # katihi … saṅgahito?
Q_OUT = f"{cap(OUT_)} {HOW_MANY}?"                                                 # Katihi asaṅgahito?
ASANKHATA = "xét theo khối thì ngoại trừ điều không do điều kiện tạo thành"        # asaṅkhataṃ khandhato ṭhapetvā
BUT = "nhưng"                        # joins a «na kehici» part and a counted part (no Pāli word)
PRON = {"o": "nó", "aṃ": "nó", "ā": "chúng", "āni": "chúng"}   # subject pronoun in «… mà nó/chúng không …»

K_NUM = {"ekena": 1, "dvīhi": 2, "tīhi": 3, "catūhi": 4, "pañcahi": 5}
A_NUM = {"eken": 1, "dvīh": 2, "tīh": 3, "pañcah": 5, "chah": 6, "sattah": 7, "navah": 9, "dasah": 10,
         "ekādasah": 11, "dvādasah": 12, "dvādas": 12}
D_NUM = {"ekāya": 1, "dvīhi": 2, "tīhi": 3, "pañcahi": 5, "chahi": 6, "sattahi": 7, "aṭṭhahi": 8, "navahi": 9,
         "dasahi": 10, "ekādasahi": 11, "dvādasahi": 12, "terasahi": 13, "pannarasahi": 15, "soḷasahi": 16,
         "sattarasahi": 17, "aṭṭhārasahi": 18}
CNT = (r"(?:[Nn]a kehici khandhehi|[Ee]kena khandhena|\S+ khandhehi),? "
       r"(?:na kehici āyatanehi|\S+āyatanena|\S+āyatanehi),? "
       r"(?:na kāhici dhātūhi|ekāya dhātuyā|\S+ dhātūhi)")
CNT_G = re.compile(r"(?P<k>na kehici khandhehi|ekena khandhena|\S+ khandhehi),? "
                   r"(?P<a>na kehici āyatanehi|\S+āyatanena|\S+āyatanehi),? "
                   r"(?P<d>na kāhici dhātūhi|ekāya dhātuyā|\S+ dhātūhi)$")


def parse_counts(s):
    """'catūhi khandhehi ekenāyatanena sattahi dhātūhi' -> (4, 1, 7); 0 = na kehici / na kāhici."""
    s = s[0].lower() + s[1:]
    m = CNT_G.match(s)
    assert m, s
    k, a, d = m.group("k"), m.group("a"), m.group("d")
    kn = 0 if k.startswith("na ") else K_NUM[k.split()[0]]
    an = 0 if a.startswith("na ") else A_NUM[re.sub(r"āyatane(?:hi|na)$", "", a)]
    dn = 0 if d.startswith("na ") else D_NUM[d.split()[0]]
    return kn, an, dn


def counts_vi(nums):
    """[(cat, n), ...] -> «một khối, mười một lĩnh vực nhận biết và mười một yếu tố»."""
    parts = [f"{NUM[n]} {c}" for c, n in nums]
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " và " + parts[-1]


def _groups(nums):
    """Split (k, a, d) into runs of zero / non-zero categories, in Pāli order."""
    out = []
    for c, n in zip(CATS, nums):
        z = n == 0
        if out and out[-1][0] == z:
            out[-1][1].append((c, n))
        else:
            out.append((z, [(c, n)]))
    return out


def answer_in(nums):
    """Predicate of a saṅgahito answer: «được gộp vào …» / «không được gộp vào khối nào, nhưng được gộp vào …»."""
    parts = []
    for zero, items in _groups(nums):
        if zero:   # na kehici khandhehi … saṅgahitaṃ
            parts.append(f"{OUT_} " + ", ".join(f"{c} nào" for c, _ in items))
        else:
            parts.append(f"{IN} {counts_vi(items)}")
    return f", {BUT} ".join(parts)


def answer_out(nums, pron):
    """Full asaṅgahito answer sentence (without the final full stop)."""
    parts = []
    for zero, items in _groups(nums):
        if zero:   # na kehici khandhehi na kehici āyatanehi … asaṅgahitā
            parts.append(", ".join(f"không có {c} nào" for c, _ in items) + f" mà {pron} {OUT_}")
        else:
            parts.append(f"{OUT_} {counts_vi(items)}")
    return cap(f", {BUT} ".join(parts))


# ================================================================== item names (subjects)
# aggregates, bases, elements, truths, faculties (PI2: pi-2 lists ^2-1, ^2-155, ^2-183, ^2-219, ^2-982)
NAMES = {
    "rūpakkhandho": "khối vật chất", "vedanākkhandho": "khối cảm giác", "saññākkhandho": "khối tri giác",
    "saṅkhārakkhandho": "khối tạo tác", "viññāṇakkhandho": "khối thức", "pañcakkhandhā": "năm khối",
    "cakkhāyatanaṃ": "lĩnh vực mắt", "sotāyatanaṃ": "lĩnh vực tai", "ghānāyatanaṃ": "lĩnh vực mũi",
    "jivhāyatanaṃ": "lĩnh vực lưỡi", "kāyāyatanaṃ": "lĩnh vực thân", "rūpāyatanaṃ": "lĩnh vực hình sắc",
    "saddāyatanaṃ": "lĩnh vực âm thanh", "gandhāyatanaṃ": "lĩnh vực mùi", "rasāyatanaṃ": "lĩnh vực vị",
    "phoṭṭhabbāyatanaṃ": "lĩnh vực vật xúc chạm", "manāyatanaṃ": "lĩnh vực ý",
    "dhammāyatanaṃ": "lĩnh vực đối tượng của ý", "dvādasāyatanāni": "mười hai lĩnh vực nhận biết",
    "cakkhudhātu": "yếu tố mắt", "sotadhātu": "yếu tố tai", "ghānadhātu": "yếu tố mũi",
    "jivhādhātu": "yếu tố lưỡi", "kāyadhātu": "yếu tố thân", "rūpadhātu": "yếu tố hình sắc",
    "saddadhātu": "yếu tố âm thanh", "gandhadhātu": "yếu tố mùi", "rasadhātu": "yếu tố vị",
    "phoṭṭhabbadhātu": "yếu tố vật xúc chạm", "cakkhuviññāṇadhātu": "yếu tố thức qua mắt",
    "sotaviññāṇadhātu": "yếu tố thức qua tai", "ghānaviññāṇadhātu": "yếu tố thức qua mũi",
    "jivhāviññāṇadhātu": "yếu tố thức qua lưỡi", "kāyaviññāṇadhātu": "yếu tố thức qua thân",
    "manodhātu": "yếu tố ý", "manoviññāṇadhātu": "yếu tố ý thức", "dhammadhātu": "yếu tố đối tượng của ý",
    "aṭṭhārasa dhātuyo": "mười tám yếu tố",
    "dukkhasaccaṃ": "sự thật về khổ đau", "samudayasaccaṃ": "sự thật về sự phát sinh",
    "maggasaccaṃ": "sự thật về con đường", "nirodhasaccaṃ": "sự thật về sự chấm dứt",
    "cattāri saccāni": "bốn sự thật",
    "cakkhundriyaṃ": "năng lực mắt", "sotindriyaṃ": "năng lực tai", "ghānindriyaṃ": "năng lực mũi",
    "jivhindriyaṃ": "năng lực lưỡi", "kāyindriyaṃ": "năng lực thân", "manindriyaṃ": "năng lực ý",
    "itthindriyaṃ": "năng lực nữ tính", "purisindriyaṃ": "năng lực nam tính", "jīvitindriyaṃ": "năng lực sống",
    "sukhindriyaṃ": "năng lực dễ chịu", "dukkhindriyaṃ": "năng lực khó chịu",
    "somanassindriyaṃ": "năng lực niềm vui", "domanassindriyaṃ": "năng lực nỗi buồn",
    "upekkhindriyaṃ": "năng lực bình thản", "saddhindriyaṃ": "năng lực niềm tin",
    "vīriyindriyaṃ": "năng lực tinh tấn", "satindriyaṃ": "năng lực tỉnh thức",
    "samādhindriyaṃ": "năng lực định tâm", "paññindriyaṃ": "năng lực trí tuệ",
    "anaññātaññassāmītindriyaṃ": "năng lực biết được điều chưa từng biết",
    "aññindriyaṃ": "năng lực hiểu biết trọn vẹn", "aññātāvindriyaṃ": "năng lực của người đã hiểu biết trọn vẹn",
    "bāvīsatindriyāni": "hai mươi hai năng lực",
    # dependent origination (PI2 ^2-225; quoted as in pi-2 «Ở đây, thế nào là “…”?»)
    "avijjā": "vô minh",
    "avijjāpaccayā saṅkhārā": "“vô minh làm điều kiện cho các sự tạo tác”",
    "saṅkhārapaccayā viññāṇaṃ": "“các sự tạo tác làm điều kiện cho thức”",
    "viññāṇapaccayā nāmarūpaṃ": "“thức làm điều kiện cho phần tinh thần và vật chất”",
    "nāmarūpapaccayā saḷāyatanaṃ": "“phần tinh thần và vật chất làm điều kiện cho sáu lĩnh vực nhận biết”",
    "saḷāyatanapaccayā phasso": "“sáu lĩnh vực nhận biết làm điều kiện cho sự tiếp xúc”",
    "phassapaccayā vedanā": "“sự tiếp xúc làm điều kiện cho cảm giác”",
    "vedanāpaccayā taṇhā": "“cảm giác làm điều kiện cho khao khát”",
    "taṇhāpaccayā upādānaṃ": "“khao khát làm điều kiện cho sự bám víu”",
    "kammabhavo [upādānapaccayā kammabhavo (sī. syā.)]":
        "sự hiện hữu dưới dạng nghiệp " + reading("Sī., Syā.", "upādānapaccayā kammabhavo"),
    # kinds of existence (PI2 ^2-234; nevasaññānāsaññā per pi-3 APPROVED 1)
    "upapattibhavo": "sự hiện hữu dưới dạng tái sinh", "kāmabhavo": "sự hiện hữu ở cõi dục lạc",
    "saññābhavo": "sự hiện hữu có tri giác", "pañcavokārabhavo": "sự hiện hữu gồm năm khối",
    "rūpabhavo": "sự hiện hữu ở cõi hình sắc", "arūpabhavo": "sự hiện hữu ở cõi không hình sắc",
    "nevasaññānāsaññābhavo": "sự hiện hữu không phải có tri giác cũng không phải không tri giác",
    "catuvokārabhavo": "sự hiện hữu gồm bốn khối", "asaññābhavo": "sự hiện hữu không có tri giác",
    "ekavokārabhavo": "sự hiện hữu gồm một khối",
    "jāti": "sự sinh", "jarā": "sự lão hóa", "maraṇaṃ": "sự chết",
    "soko": "sự sầu muộn", "paridevo": "sự than khóc", "dukkhaṃ": "sự khó chịu", "domanassaṃ": "nỗi buồn",
    "upāyāso": "sự tuyệt vọng",
    # the inner-matrix topics (PI2 ^2-U26, ^2-623, ^2-683)
    "satipaṭṭhānaṃ": "sự thiết lập tỉnh thức", "sammappadhānaṃ": "nỗ lực đúng đắn",
    "iddhipādo": "nền tảng thần thông", "jhānaṃ": "tầng thiền", "appamaññā": "trạng thái không thể đo lường",
    "pañcindriyāni": "năm năng lực", "pañca balāni": "năm sức mạnh", "satta bojjhaṅgā": "bảy chi phần giác ngộ",
    "ariyo aṭṭhaṅgiko maggo": "con đường cao quý gồm tám chi phần",
    "phasso": "sự tiếp xúc", "vedanā": "cảm giác", "saññā": "tri giác", "cetanā": "chủ ý", "cittaṃ": "tâm",
    "adhimokkho": "sự quyết định", "manasikāro": "sự chú tâm",
}

# matrix attributes (X dhammā = «các hiện tượng X»; PI1 matrix names)
DHAMMA_N = "các hiện tượng"
DHAMMA_ATTR = {
    "kusalā": "thiện", "akusalā": "bất thiện", "abyākatā": "không xác định về mặt đạo đức",
    "sukhāya vedanāya sampayuttā": "gắn liền với cảm giác dễ chịu",
    "dukkhāya vedanāya sampayuttā": "gắn liền với cảm giác khó chịu",
    "adukkhamasukhāya vedanāya sampayuttā": "gắn liền với cảm giác không khó chịu cũng không dễ chịu",
    "vipākā": "là quả của nghiệp", "vipākadhammadhammā": "có khả năng sinh ra quả",
    "nevavipākanavipākadhammadhammā": "không phải là quả của nghiệp cũng không có khả năng sinh ra quả",
    "upādinnupādāniyā": "do nghiệp tạo ra và là đối tượng của sự bám víu",
    "anupādinnupādāniyā": "không do nghiệp tạo ra nhưng là đối tượng của sự bám víu",
    "anupādinnaanupādāniyā": "không do nghiệp tạo ra và không phải là đối tượng của sự bám víu",
    "saṃkiliṭṭhasaṃkilesikā": "bị phiền não làm vẩn đục và là đối tượng của phiền não",
    "asaṃkiliṭṭhasaṃkilesikā": "không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não",
    "asaṃkiliṭṭhaasaṃkilesikā": "không bị phiền não làm vẩn đục và không phải là đối tượng của phiền não",
    "savitakkasavicārā": "có sự hướng tâm và sự duy trì tâm",
    "avitakkavicāramattā": "không có sự hướng tâm, chỉ có sự duy trì tâm",
    "avitakkaavicārā": "không có sự hướng tâm cũng không có sự duy trì tâm",
    "pītisahagatā": "có sự hân hoan đi kèm", "sukhasahagatā": "có hạnh phúc đi kèm",
    "upekkhāsahagatā": "có sự bình thản đi kèm",
    "dassanena pahātabbā": "cần dứt bỏ bằng sự thấy chân lý",
    "bhāvanāya pahātabbā": "cần dứt bỏ bằng sự tu tập",
    "neva dassanena na bhāvanāya pahātabbā":
        "không cần dứt bỏ bằng sự thấy chân lý cũng không cần dứt bỏ bằng sự tu tập",
    "dassanena pahātabbahetukā": "có gốc rễ cần dứt bỏ bằng sự thấy chân lý",
    "bhāvanāya pahātabbahetukā": "có gốc rễ cần dứt bỏ bằng sự tu tập",
    "neva dassanena na bhāvanāya pahātabbahetukā":
        "không có gốc rễ nào cần dứt bỏ bằng sự thấy chân lý, cũng không có gốc rễ nào cần dứt bỏ bằng sự tu tập",
    "ācayagāmino": "dẫn đến sự tích lũy", "apacayagāmino": "dẫn đến sự giảm trừ",
    "nevācayagāmināpacayagāmino": "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ",
    "sekkhā": "thuộc về người còn đang tu học", "asekkhā": "thuộc về người đã hoàn tất tu học",
    "nevasekkhanāsekkhā": "không thuộc về người còn đang tu học cũng không thuộc về người đã hoàn tất tu học",
    "parittā": "hạn hẹp", "mahaggatā": "rộng lớn", "appamāṇā": "không thể đo lường",
    "parittārammaṇā": "có đối tượng hạn hẹp",
    "parittārammaṇā [parittāramaṇā (?)]": "có đối tượng hạn hẹp " + spell("?", "parittāramaṇā"),
    "mahaggatārammaṇā": "có đối tượng rộng lớn", "appamāṇārammaṇā": "có đối tượng không thể đo lường",
    "hīnā": "thấp kém", "majjhimā": "trung bình", "paṇītā": "ưu việt",
    "micchattaniyatā": "cố định theo hướng sai lầm", "sammattaniyatā": "cố định theo hướng đúng đắn",
    "aniyatā": "không cố định",
    "maggārammaṇā": "lấy con đường làm đối tượng", "maggahetukā": "lấy con đường làm gốc rễ",
    "maggādhipatino": "lấy con đường làm yếu tố chủ đạo",
    "uppannā": "đã sinh khởi", "anuppannā": "chưa sinh khởi", "uppādino": "sẽ sinh khởi",
    "atītā": "thuộc quá khứ", "anāgatā": "thuộc tương lai", "paccuppannā": "thuộc hiện tại",
    "ajjhattā": "ở nơi bản thân", "bahiddhā": "ở bên ngoài bản thân",
    "ajjhattabahiddhā": "ở nơi bản thân và ở bên ngoài bản thân",
    "atītārammaṇā": "có đối tượng thuộc quá khứ", "anāgatārammaṇā": "có đối tượng thuộc tương lai",
    "paccuppannārammaṇā": "có đối tượng thuộc hiện tại", "ajjhattārammaṇā": "có đối tượng ở nơi bản thân",
    "bahiddhārammaṇā": "có đối tượng ở bên ngoài bản thân",
    "ajjhattabahiddhārammaṇā": "có đối tượng ở nơi bản thân và ở bên ngoài bản thân",
    "sanidassanasappaṭighā": "thấy được và có tính va chạm",
    "anidassanasappaṭighā": "không thấy được nhưng có tính va chạm",
    "anidassanaappaṭighā": "không thấy được và không có tính va chạm",
    # dyads
    "hetū": "là gốc rễ", "na hetū": "không phải là gốc rễ", "sahetukā": "có gốc rễ",
    "ahetukā": "không có gốc rễ", "hetusampayuttā": "gắn liền với gốc rễ",
    "hetuvippayuttā": "không gắn liền với gốc rễ",
    "hetū ceva sahetukā ca": "vừa là gốc rễ vừa có gốc rễ",
    "sahetukā ceva na ca hetū": "có gốc rễ nhưng không phải là gốc rễ",
    "hetū ceva hetusampayuttā ca": "vừa là gốc rễ vừa gắn liền với gốc rễ",
    "hetusampayuttā ceva na ca hetū": "gắn liền với gốc rễ nhưng không phải là gốc rễ",
    "na hetū sahetukā": "không phải là gốc rễ nhưng có gốc rễ",
    "na hetū ahetukā": "không phải là gốc rễ và không có gốc rễ",
    "na hetū ahetukā [na hetū ahetukā (syā. ka.) vibha. dukapañhāpucchakepi]":
        "không phải là gốc rễ và không có gốc rễ "
        + reading("Syā., Ka.", "na hetū ahetukā; cũng vậy trong phần hỏi đáp về bộ đôi của Phân tích các hiện tượng"),
    "sappaccayā": "có điều kiện", "appaccayā": "không có điều kiện",
    "saṅkhatā": "do điều kiện tạo thành", "asaṅkhatā": "không do điều kiện tạo thành",
    "sanidassanā": "thấy được", "anidassanā": "không thấy được",
    "sappaṭighā": "có tính va chạm", "appaṭighā": "không có tính va chạm",
    "rūpino": "thuộc vật chất", "arūpino": "phi vật chất",
    "lokiyā": "thuộc thế gian", "lokuttarā": "vượt thế gian",
    "kenaci viññeyyā": "mà một loại thức nào đó có thể nhận biết",
    "kenaci na viññeyyā": "mà một loại thức nào đó không thể nhận biết",
    "āsavā": "là ô nhiễm", "no āsavā": "không phải là ô nhiễm",
    "sāsavā": "là đối tượng của ô nhiễm", "anāsavā": "không phải là đối tượng của ô nhiễm",
    "āsavasampayuttā": "gắn liền với ô nhiễm", "āsavavippayuttā": "không gắn liền với ô nhiễm",
    "āsavā ceva sāsavā ca": "vừa là ô nhiễm vừa là đối tượng của ô nhiễm",
    "sāsavā ceva no ca āsavā": "là đối tượng của ô nhiễm nhưng không phải là ô nhiễm",
    "āsavā ceva āsavasampayuttā ca": "vừa là ô nhiễm vừa gắn liền với ô nhiễm",
    "āsavasampayuttā ceva no ca āsavā": "gắn liền với ô nhiễm nhưng không phải là ô nhiễm",
    "āsavavippayuttā sāsavā": "không gắn liền với ô nhiễm nhưng là đối tượng của ô nhiễm",
    "āsavavippayuttā anāsavā": "không gắn liền với ô nhiễm và không phải là đối tượng của ô nhiễm",
    "saṃyojanā": "là xiềng xích", "ganthā": "là nút thắt", "oghā": "là dòng lũ", "yogā": "là ách",
    "nīvaraṇā": "là chướng ngại", "parāmāsā": "là sự hiểu sai lệch",
    "no parāmāsā": "không phải là sự hiểu sai lệch",
    "parāmaṭṭhā": "bị sự hiểu sai lệch nắm giữ", "aparāmaṭṭhā": "không bị sự hiểu sai lệch nắm giữ",
    "parāmāsasampayuttā": "gắn liền với sự hiểu sai lệch",
    "parāmāsavippayuttā": "không gắn liền với sự hiểu sai lệch",
    "parāmāsā ceva parāmaṭṭhā ca": "vừa là sự hiểu sai lệch vừa bị sự hiểu sai lệch nắm giữ",
    "parāmaṭṭhā ceva no ca parāmāsā": "bị sự hiểu sai lệch nắm giữ nhưng không phải là sự hiểu sai lệch",
    "parāmāsavippayuttā parāmaṭṭhā":
        "không gắn liền với sự hiểu sai lệch nhưng bị sự hiểu sai lệch nắm giữ",
    "parāmāsavippayuttā aparāmaṭṭhā":
        "không gắn liền với sự hiểu sai lệch và không bị sự hiểu sai lệch nắm giữ",
    "sārammaṇā": "có đối tượng", "anārammaṇā": "không có đối tượng",
    "cittā": "là tâm", "no cittā": "không phải là tâm",
    "cetasikā": "là yếu tố đồng hành với tâm", "acetasikā": "không phải là yếu tố đồng hành với tâm",
    "cittasampayuttā": "gắn liền với tâm", "cittavippayuttā": "không gắn liền với tâm",
    "cittasaṃsaṭṭhā": "hòa lẫn với tâm", "cittavisaṃsaṭṭhā": "không hòa lẫn với tâm",
    "cittasamuṭṭhānā": "do tâm sinh ra", "no cittasamuṭṭhānā": "không do tâm sinh ra",
    "cittasahabhuno": "cùng tồn tại với tâm", "no cittasahabhuno": "không cùng tồn tại với tâm",
    "cittānuparivattino": "vận hành theo tâm", "no cittānuparivattino": "không vận hành theo tâm",
    "cittasaṃsaṭṭhasamuṭṭhānā": "vừa hòa lẫn với tâm vừa do tâm sinh ra",
    "no cittasaṃsaṭṭhasamuṭṭhānā": "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhuno": "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm",
    "no cittasaṃsaṭṭhasamuṭṭhānasahabhuno":
        "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
    "no cittasaṃsaṭṭhasamuṭṭhānānuparivattino":
        "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
    "ajjhattikā": "thuộc phần bên trong", "bāhirā": "thuộc phần bên ngoài",
    "upādā": "phái sinh", "no upādā": "không phải là phái sinh",
    "upādinnā": "do nghiệp tạo ra", "anupādinnā": "không do nghiệp tạo ra",
    "upādānā": "là sự bám víu",
    "kilesā": "là phiền não", "no kilesā": "không phải là phiền não",
    "saṃkilesikā": "là đối tượng của phiền não", "asaṃkilesikā": "không phải là đối tượng của phiền não",
    "saṃkiliṭṭhā": "bị phiền não làm vẩn đục", "asaṃkiliṭṭhā": "không bị phiền não làm vẩn đục",
    "kilesasampayuttā": "gắn liền với phiền não", "kilesavippayuttā": "không gắn liền với phiền não",
    "kilesā ceva saṃkilesikā ca": "vừa là phiền não vừa là đối tượng của phiền não",
    "saṃkilesikā ceva no ca kilesā": "là đối tượng của phiền não nhưng không phải là phiền não",
    "kilesā ceva saṃkiliṭṭhā ca": "vừa là phiền não vừa bị phiền não làm vẩn đục",
    "saṃkiliṭṭhā ceva no ca kilesā": "bị phiền não làm vẩn đục nhưng không phải là phiền não",
    "kilesā ceva kilesasampayuttā ca": "vừa là phiền não vừa gắn liền với phiền não",
    "kilesasampayuttā ceva no ca kilesā": "gắn liền với phiền não nhưng không phải là phiền não",
    "kilesavippayuttā saṃkilesikā": "không gắn liền với phiền não nhưng là đối tượng của phiền não",
    "kilesavippayuttā asaṃkilesikā": "không gắn liền với phiền não và không phải là đối tượng của phiền não",
    "na dassanena pahātabbā": "không cần dứt bỏ bằng sự thấy chân lý",
    "na bhāvanāya pahātabbā": "không cần dứt bỏ bằng sự tu tập",
    "na dassanena pahātabbahetukā": "không có gốc rễ nào cần dứt bỏ bằng sự thấy chân lý",
    "na bhāvanāya pahātabbahetukā": "không có gốc rễ nào cần dứt bỏ bằng sự tu tập",
    "savitakkā": "có sự hướng tâm", "avitakkā": "không có sự hướng tâm",
    "savicārā": "có sự duy trì tâm", "avicārā": "không có sự duy trì tâm",
    "sappītikā": "có sự hân hoan", "appītikā": "không có sự hân hoan",
    "na pītisahagatā": "không có sự hân hoan đi kèm", "na sukhasahagatā": "không có hạnh phúc đi kèm",
    "na upekkhāsahagatā": "không có sự bình thản đi kèm",
    "kāmāvacarā": "thuộc cõi dục lạc", "na kāmāvacarā": "không thuộc cõi dục lạc",
    "rūpāvacarā": "thuộc cõi hình sắc", "na rūpāvacarā": "không thuộc cõi hình sắc",
    "arūpāvacarā": "thuộc cõi không hình sắc", "na arūpāvacarā": "không thuộc cõi không hình sắc",
    "pariyāpannā": "nằm trong các cõi tồn tại", "apariyāpannā": "không nằm trong các cõi tồn tại",
    "niyyānikā": "dẫn đến giải thoát", "aniyyānikā": "không dẫn đến giải thoát",
    "niyatā": "cố định",
    "sauttarā": "còn có điều cao hơn", "anuttarā": "không có điều gì cao hơn",
    "saraṇā": "có xung đột", "araṇā": "không có xung đột",
}


def item_vi(p):
    """One Pāli subject item (no ellipsis inside) -> Vietnamese (lower-case start)."""
    p = p.strip()
    if p.endswith(" dhammā"):
        attr = p[: -len(" dhammā")]
        key = attr[0].lower() + attr[1:]
        if key not in DHAMMA_ATTR:
            raise KeyError(f"no attribute for {p!r}")
        return f"{DHAMMA_N} {DHAMMA_ATTR[key]}"
    words = p.split()
    if (p[0].lower() + p[1:]) not in NAMES and ("ca" in words or any(w.endswith("ñca") for w in words)):
        mem = [w[:-3] + "ṃ" if w.endswith("ñca") else w for w in words if w != "ca"]
        vi = [NAMES[m[0].lower() + m[1:]] for m in mem]
        return vi[0] if len(vi) == 1 else ", ".join(vi[:-1]) + " và " + vi[-1]
    key = p[0].lower() + p[1:]
    if key.endswith("dhammadhammā") and key in DHAMMA_ATTR:   # «dhammā» fused into the compound
        return f"{DHAMMA_N} {DHAMMA_ATTR[key]}"
    if key not in NAMES:
        raise KeyError(f"no name for {p!r}")
    return NAMES[key]


def subject_vi(p):
    """Pāli subject (items separated by «…», «…pe…» allowed) -> Vietnamese, first letter capital."""
    p = p.replace("…pe…", "…").strip()
    trailing = p.endswith("…")
    items = [x for x in (s.strip() for s in p.split("…")) if x]
    vi = "… ".join(item_vi(x) for x in items) + ("…" if trailing else "")
    return cap(vi)


SEG = re.compile(r"^(?P<pre>.*?)(?P<c1>" + CNT + r") saṅgahit(?P<e1>\w+)\. Katihi asaṅgahit(?P<e2>\w+)\? "
                 r"(?P<c2>" + CNT + r") asaṅgahit(?P<e3>\w+)\.$")
QSPLIT = re.compile(r" katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahit\w+\? ")
ASX_P = "asaṅkhataṃ khandhato ṭhapetvā"


THEN = "thì"   # only after a subject ending in «được» (thấy được), to avoid «được được»


def subj_head(subj_vi):
    return f"{subj_vi} {THEN}" if subj_vi.endswith(" được") else subj_vi


def answer_line(subj_vi, asx, nums_in, nums_out, pron):
    """«S [, xét theo khối …,] được gộp vào …. Không được gộp vào bao nhiêu? Không được gộp vào ….»"""
    head = subj_vi + f", {ASANKHATA}," if asx else subj_head(subj_vi)
    return f"{head} {answer_in(nums_in)}. {Q_OUT} {answer_out(nums_out, pron)}."


def content_line(p):
    """Translate one saṅgaha / asaṅgaha line of chapter 2."""
    q = None
    parts = QSPLIT.split(p)
    if len(parts) == 2:
        q, p = parts
    m = SEG.match(p)
    if not m:
        raise ValueError(f"unparsed: {p}")
    pre = m.group("pre").strip()
    asx = pre.endswith(ASX_P)
    if asx:
        pre = pre[: -len(ASX_P)].strip()
    out = answer_line(subject_vi(pre), asx, parse_counts(m.group("c1")), parse_counts(m.group("c2")),
                      PRON[m.group("e3")])
    if q is not None:
        out = f"{subj_head(subject_vi(q))} {Q_IN} {out}"
    return out


# segment overrides (Pāli shape that the parser does not cover)
OVERRIDE = {
    # Jāti dvīhi khandhehi… jarā dvīhi khandhehi… maraṇaṃ dvīhi khandhehi ekenāyatanena ekāya dhātuyā saṅgahitaṃ.
    "3-71": [f"{cap(NAMES['jāti'])} {IN} {NUM[2]} {KHANDHA}… {NAMES['jarā']} {IN} {NUM[2]} {KHANDHA}… "
             f"{NAMES['maraṇaṃ']} {IN} {counts_vi([(KHANDHA, 2), (AYATANA, 1), (DHATU, 1)])}. {Q_OUT} "
             f"{answer_out((3, 11, 17), 'nó')}."],
}

# ================================================================== chapter 1 (Uddeso)
NAYA_LIST = "; ".join(f"({i}) {cap(vi) if i == 1 else vi}" for i, (_, _, vi) in enumerate(METHODS, 1)) + "."
INNER = [  # PI2 names; (16) the seven beginning with contact
    "năm khối", "mười hai lĩnh vực nhận biết", "mười tám yếu tố", "bốn sự thật", "hai mươi hai năng lực",
    "sự sinh khởi tùy thuộc vào điều kiện", "bốn sự thiết lập tỉnh thức", "bốn nỗ lực đúng đắn",
    "bốn nền tảng thần thông", "bốn tầng thiền", "bốn trạng thái không thể đo lường", "năm năng lực",
    "năm sức mạnh", "bảy chi phần giác ngộ", "con đường cao quý gồm tám chi phần",
    "sự tiếp xúc, cảm giác, tri giác, chủ ý, tâm, sự quyết định, sự chú tâm",
]
INNER_LIST = "; ".join(f"({i}) {cap(vi) if i == 1 else vi}" for i, vi in enumerate(INNER, 1)) + "."
NAYAMUKHA = ("Sự gộp vào theo ba cách, sự không gộp vào theo ba cách, sự gắn liền theo bốn cách, "
             "sự không gắn liền theo bốn cách.")                    # Tīhi saṅgaho, tīhi asaṅgaho, catūhi …
LAKKHANA = "Cùng loại, khác loại."                                   # Sabhāgo, visabhāgo.
BAHIRA = f"Toàn bộ “{BOOK_PI1}” là ma trận của “{H_BOOK}”."           # Sabbāpi dhammasaṅgaṇī dhātukathāya mātikāti.
CH1_LINES = {"3-1": [NAYA_LIST], "3-2": [INNER_LIST], "3-3": [NAYAMUKHA], "3-4": [LAKKHANA], "3-5": [BAHIRA]}


# ================================================================== segment machinery
def pali_segments(path):
    segs, buf = [], []
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        m = ID.search(ln)
        buf.append(ID.sub("", ln).rstrip())
        if m:
            segs.append((buf, m.group(1)))
            buf = []
    assert not buf, f"trailing lines without id in {path}"
    return segs


def heading_vi(line):
    hashes, text = line.split(" ", 1)
    level = len(hashes)
    for table in (CH_HEADINGS, CH1_SECTIONS, SEC_HEADINGS, SUB_HEADINGS):
        if text in table:
            return f"{hashes} {table[text]}"
    if text == "Abhidhammapiṭake":
        return f"{hashes} {H_PITAKA}"
    if text == "Dhātukathāpāḷi":
        return f"{hashes} {H_BOOK}"
    raise KeyError(f"heading {level}: {text}")


def translate_segment(lines, bid):
    if bid in CH1_LINES:
        return CH1_LINES[bid]
    if bid in OVERRIDE:
        first = OVERRIDE[bid]
        rest = lines[len(first):]
    else:
        first, rest = None, None
    out = []
    for i, ln in enumerate(lines):
        if first is not None and i < len(first):
            out.append(first[i])
        elif ln.startswith("#"):
            out.append(heading_vi(ln))
        elif ln.startswith("Namo tassa"):
            out.append(HOMAGE)
        elif ln in ROUND_LABELS:
            out.append(ROUND_LABELS[ln])
        elif ln in CLOSINGS:
            out.append(CLOSINGS[ln])
        else:
            out.append(content_line(ln))
    assert rest is None or len(out) == len(lines)
    return out


def render_file(name):
    segs = pali_segments(PALI / name)
    blocks = []
    for lines, bid in segs:
        vi = translate_segment(lines, bid)
        assert len(vi) == len(lines), bid
        vi[-1] = f"{vi[-1]} ^{bid}"
        blocks.append("\n".join(vi))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


# ================================================================== reuse from pi-1 / pi-2 (asserted)
def _strip_q(s):
    return s.replace("“", "").replace("”", "")


REUSE = [  # (Pāli, Vietnamese as reused, book)
    ("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE, 1),
    ("# Abhidhammapiṭake", f"# {H_PITAKA}", 1),
    ("dhammasaṅgaṇī (book title)", BOOK_PI1, 1),
    ("Pañcakkhandhā", "Năm khối", 2),
    ("Dvādasāyatanāni", "Mười hai lĩnh vực nhận biết", 2),
    ("Aṭṭhārasa dhātuyo", "Mười tám yếu tố", 2),
    ("Cattāri saccāni", "Bốn sự thật", 2),
    ("Bāvīsatindriyāni", "Hai mươi hai năng lực", 2),
    ("paṭiccasamuppādo", "sự sinh khởi tùy thuộc vào điều kiện", 1),
    ("cattāro satipaṭṭhānā, cattāro sammappadhānā, cattāro iddhipādā",
     "bốn sự thiết lập tỉnh thức, bốn nỗ lực đúng đắn, bốn nền tảng thần thông", 2),
    ("cattāri jhānāni", "bốn tầng thiền", 2),
    ("catasso appamaññāyo", "bốn trạng thái không thể đo lường", 2),
    ("pañcindriyāni, pañca balāni, satta bojjhaṅgā, ariyo aṭṭhaṅgiko maggo",
     "năm năng lực, năm sức mạnh, bảy chi phần giác ngộ, con đường cao quý gồm tám chi phần", 2),
    ("adhimokkho", "sự quyết định", 2),
    ("manasikāro", "sự chú tâm", 1),
    ("dukkhasaccaṃ, samudayasaccaṃ, nirodhasaccaṃ, maggasaccaṃ",
     "sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, sự thật về con đường", 2),
]
for _k in ["rūpakkhandho", "vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"]:
    REUSE.append((_k, NAMES[_k], 2))
for _k in ["cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ", "rūpāyatanaṃ",
           "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ", "manāyatanaṃ", "dhammāyatanaṃ",
           "cakkhudhātu", "sotadhātu", "ghānadhātu", "jivhādhātu", "kāyadhātu", "rūpadhātu", "saddadhātu",
           "gandhadhātu", "rasadhātu", "phoṭṭhabbadhātu", "cakkhuviññāṇadhātu", "sotaviññāṇadhātu",
           "ghānaviññāṇadhātu", "jivhāviññāṇadhātu", "kāyaviññāṇadhātu", "manodhātu", "manoviññāṇadhātu",
           "dhammadhātu",
           "cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ", "manindriyaṃ",
           "itthindriyaṃ", "purisindriyaṃ", "jīvitindriyaṃ", "sukhindriyaṃ", "dukkhindriyaṃ",
           "somanassindriyaṃ", "domanassindriyaṃ", "upekkhindriyaṃ", "saddhindriyaṃ", "vīriyindriyaṃ",
           "satindriyaṃ", "samādhindriyaṃ", "paññindriyaṃ", "anaññātaññassāmītindriyaṃ", "aññindriyaṃ",
           "aññātāvindriyaṃ",
           "avijjāpaccayā saṅkhārā", "saṅkhārapaccayā viññāṇaṃ", "viññāṇapaccayā nāmarūpaṃ",
           "nāmarūpapaccayā saḷāyatanaṃ", "saḷāyatanapaccayā phasso", "phassapaccayā vedanā",
           "vedanāpaccayā taṇhā", "taṇhāpaccayā upādānaṃ",
           "upapattibhavo", "kāmabhavo", "saññābhavo", "pañcavokārabhavo", "rūpabhavo", "arūpabhavo",
           "catuvokārabhavo", "asaññābhavo", "ekavokārabhavo",
           "jāti", "jarā", "soko", "paridevo", "domanassaṃ", "upāyāso", "iddhipādo", "jhānaṃ"]:
    REUSE.append((_k, NAMES[_k], 2))
REUSE.append(("kammabhavo", "sự hiện hữu dưới dạng nghiệp", 2))
for _k in DHAMMA_ATTR:
    if "[" in _k:
        continue
    REUSE.append((f"{_k} dhammā", DHAMMA_ATTR[_k], 1))      # attribute after «các hiện tượng» / «… nào»
NOT_REUSED = {   # pi-3 wording that differs from, or is absent in, pi-1 / pi-2 (reported)
    "nevasaññānāsaññābhavo": "pi-2 «… không phải không có tri giác»; pi-3 APPROVED 1 aligns nāsaññā to pi-1",
}


def check_reuse():
    t1 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_DIR.glob("*.md"))).lower()
    t2 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI2_DIR.glob("*.md"))).lower()
    missing = []
    for p, v, b in REUSE:
        t = t1 if b == 1 else t2
        v0 = _strip_q(v).lower()
        if p.endswith(" dhammā"):   # matrix attribute: «hiện tượng X» or «hiện tượng nào X»
            ok = f"hiện tượng {v0}" in t or f"hiện tượng nào {v0}" in t
        else:
            ok = v0 in t
        if not ok:
            missing.append(f"(pi-{b}) {p} = {v}")
    assert not missing, "reused strings not found:\n" + "\n".join(missing)
    return len(REUSE)


def reuse_tag(v):
    for p, rv, b in REUSE:
        if rv == v or (p.endswith(" dhammā") and f"{DHAMMA_N} {rv}" == v):
            return f" (pi-{b})"
    return ""


# ================================================================== formulas file
def formulas():
    F = []
    add = lambda p, v, tag="": F.append(f"{p} = {v}{tag or reuse_tag(v)}")
    sec = lambda t: F.extend(["", f"## {t}", ""])
    sec("Book frame and headings")
    add("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE)
    add("# Abhidhammapiṭake", f"# {H_PITAKA}")
    add("## Dhātukathāpāḷi", f"## {H_BOOK} (mid-sentence: “{H_BOOK}”)")
    add("dhammasaṅgaṇī (book title, ^3-5)", f"“{BOOK_PI1}”", " (pi-1)")
    add("Colophon (end of ch15)", COLOPHON)
    for p, v in CH_HEADINGS.items():
        add(f"### {p}", f"### {v}")
    for p, v in CH1_SECTIONS.items():
        add(f"#### {p}", f"#### {v}")
    for p, v in SEC_HEADINGS.items():
        add(f"#### {p}", f"#### {v}")
    for p, v in CLOSINGS.items():
        add(f"{p} (closing line)", v)
    for p, v in SUB_HEADINGS.items():
        add(f"##### {p}", f"##### {v}")
    for p, v in ROUND_LABELS.items():
        add(p, v)
    sec("Chapter 1 (Uddeso)")
    for p, _, v in METHODS:
        add(f"({METHODS.index((p, _, v)) + 1}) {p} (method name X)", v)
    add("^3-1 list layout", "(1) … ; (2) … ; … (14) … . (items joined with «; »; «(7)sampayuttena» rendered as meant)")
    add("^3-2 (1)…(16)", INNER_LIST)
    add("Tīhi saṅgaho, tīhi asaṅgaho, catūhi sampayogo, catūhi vippayogo.", NAYAMUKHA)
    add("Sabhāgo, visabhāgo.", LAKKHANA)
    add("Sabbāpi dhammasaṅgaṇī dhātukathāya mātikāti.", BAHIRA)
    sec("Comprising questions and answers (chapter 2)")
    add("katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahito/-ā/-aṃ/-āni?", Q_IN)
    add("X … saṅgahito. (answer)", f"X {IN} N {KHANDHA}, N {AYATANA} và N {DHATU}.")
    add("Katihi asaṅgahito/-ā/-aṃ/-āni?", Q_OUT)
    add("N khandhehi N āyatanehi N dhātūhi asaṅgahito.", f"{cap(OUT_)} N {KHANDHA}, N {AYATANA} và N {DHATU}.")
    add("katihi (question word)", HOW_MANY)
    add("saṅgahito / saṅgahitā / saṅgahitaṃ / saṅgahitāni", IN)
    add("asaṅgahito / asaṅgahitā / asaṅgahitaṃ / asaṅgahitāni", OUT_)
    add("khandhehi / khandhena (counted)", KHANDHA)
    add("āyatanehi / āyatanena (counted)", AYATANA)
    add("dhātūhi / dhātuyā (counted)", DHATU)
    add("numerals 1-18 (ekena/ekāya … aṭṭhārasahi)", ", ".join(f"{k}={v}" for k, v in NUM.items() if k < 19))
    add("dvādasāyatanehi = dvādasahāyatanehi", f"{NUM[12]} {AYATANA}")
    add("X asaṅkhataṃ khandhato ṭhapetvā N … saṅgahitā.", f"X, {ASANKHATA}, {IN} N ….")
    add("X na kehici khandhehi ekenāyatanena ekāya dhātuyā saṅgahitaṃ.",
        f"X {answer_in((0, 1, 1))}.")
    add("Na kehici khandhehi na kehici āyatanehi na kāhici dhātūhi asaṅgahitā.",
        answer_out((0, 0, 0), PRON["ā"]) + ".")
    add("Na kehici khandhehi na kehici āyatanehi na kāhici dhātūhi asaṅgahitaṃ / asaṅgahito.",
        answer_out((0, 0, 0), PRON["aṃ"]) + ".")
    add("Tīhi khandhehi, na kehici āyatanehi na kāhici dhātūhi asaṅgahitā. (comma or not)",
        answer_out((3, 0, 0), PRON["ā"]) + ".")
    add("Na kehici khandhehi ekenāyatanena ekāya dhātuyā asaṅgahito.", answer_out((0, 1, 1), PRON["o"]) + ".")
    add("Na kehici khandhehi, dasahāyatanehi dasahi dhātūhi asaṅgahitā. (comma or not)",
        answer_out((0, 10, 10), PRON["ā"]) + ".")
    add("Na kehici khandhehi na kehici āyatanehi pañcahi dhātūhi asaṅgahitā.",
        answer_out((0, 0, 5), PRON["ā"]) + ".")
    add("pronoun in the «na kehici» answers", "nó (sg. -o / -aṃ), chúng (pl. -ā / -āni)")
    add("Sanidassanā dhammā ekena khandhena … saṅgahitā. (subject ending in «được»)",
        f"{cap(DHAMMA_N)} thấy được {THEN} {IN} một {KHANDHA}, … (never «được được»)")
    add("X…pe… N khandhehi … saṅgahitā.",f"X… {IN} N … (the «…» stays after the last named item)")
    add("X ca Y ca / Xñca Yñca", "X và Y; three or more: X, Y và Z")
    add("example ^3-6", content_line(
        "Rūpakkhandho katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahito? Rūpakkhandho ekena khandhena "
        "ekādasahāyatanehi ekādasahi dhātūhi saṅgahito. Katihi asaṅgahito? Catūhi khandhehi ekenāyatanena "
        "sattahi dhātūhi asaṅgahito."))
    add("example ^3-25", content_line(
        "Dhammāyatanaṃ asaṅkhataṃ khandhato ṭhapetvā catūhi khandhehi ekenāyatanena ekāya dhātuyā saṅgahitaṃ. "
        "Katihi asaṅgahitaṃ? Ekena khandhena ekādasahāyatanehi sattarasahi dhātūhi asaṅgahitaṃ."))
    sec("List members (subjects)")
    for k, v in NAMES.items():
        add(k, v)
    sec("Matrix names as subjects (X dhammā = «các hiện tượng X»; capital «Các» at sentence start)")
    for k, v in DHAMMA_ATTR.items():
        add(f"{k} dhammā", f"{DHAMMA_N} {v}")
    sec("Variants and punctuation")
    add("…pe…", "… (same spot; never «….»)", " (pi-1)")
    add("[word (sī. syā.)] spelling only", "[khác chính tả (Sī., Syā.): word]", " (pi-1)")
    add("[word (syā.)] other word", "[dị bản (Syā.): word]", " (pi-1)")
    add("[word (?)] spelling only", "[khác chính tả (?): word]", " (pi-2)")
    add("vibha. (citation in a variant note)", "Phân tích các hiện tượng (book title, no quotes inside the bracket)")
    add("dashes", "none (pi-3 has no «–» / «—»; never add one)")
    sec("Proposed for ch3-15 (built from the termbase; binding for the chapter agents)")
    P = lambda p, v: F.append(f"{p} = {v} (proposed for ch3-15)")
    P("X-ena ye dhammā (with X)", "những hiện tượng nào … cùng với X …")
    P("khandhasaṅgahena / āyatanasaṅgahena / dhātusaṅgahena",
      "theo cách gộp vào khối / theo cách gộp vào lĩnh vực nhận biết / theo cách gộp vào yếu tố")
    P("Xena ye dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā, te dhammā "
      "katihi khandhehi katihāyatanehi katihi dhātūhi asaṅgahitā? Te dhammā N … asaṅgahitā. (ch3)",
      "Những hiện tượng nào được gộp vào cùng với X theo cách gộp vào khối, nhưng không được gộp vào cùng với nó "
      "theo cách gộp vào lĩnh vực nhận biết và theo cách gộp vào yếu tố, thì những hiện tượng ấy không được gộp vào "
      "bao nhiêu khối, bao nhiêu lĩnh vực nhận biết và bao nhiêu yếu tố? Những hiện tượng ấy không được gộp vào "
      "N khối, N lĩnh vực nhận biết và N yếu tố.")
    P("Xena ye dhammā khandhasaṅgahena asaṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā, te dhammā "
      "katihi … saṅgahitā? Te dhammā asaṅkhataṃ khandhato ṭhapetvā N … saṅgahitā. (ch4)",
      "Những hiện tượng nào không được gộp vào cùng với X theo cách gộp vào khối, nhưng được gộp vào cùng với nó "
      "theo cách gộp vào lĩnh vực nhận biết và theo cách gộp vào yếu tố, thì những hiện tượng ấy được gộp vào bao "
      "nhiêu khối, bao nhiêu lĩnh vực nhận biết và bao nhiêu yếu tố? Những hiện tượng ấy, xét theo khối thì ngoại "
      "trừ điều không do điều kiện tạo thành, được gộp vào N khối, N lĩnh vực nhận biết và N yếu tố.")
    P("Xena ye dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā, tehi dhammehi "
      "ye dhammā khandhasaṅgahena saṅgahitā … , te dhammā katihi … saṅgahitā? (ch5)",
      "Những hiện tượng nào được gộp vào cùng với X theo cách gộp vào khối, theo cách gộp vào lĩnh vực nhận biết và "
      "theo cách gộp vào yếu tố; những hiện tượng nào được gộp vào cùng với các hiện tượng đó theo cách gộp vào "
      "khối, theo cách gộp vào lĩnh vực nhận biết và theo cách gộp vào yếu tố, thì những hiện tượng ấy được gộp vào "
      "bao nhiêu khối, bao nhiêu lĩnh vực nhận biết và bao nhiêu yếu tố?")
    P("… khandhasaṅgahena asaṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā (ch6, ch14)",
      "… không được gộp vào cùng với X theo cách gộp vào khối, theo cách gộp vào lĩnh vực nhận biết hay theo cách "
      "gộp vào yếu tố")
    P("tehi dhammehi ye dhammā …", "những hiện tượng nào … cùng với các hiện tượng đó …")
    P("…pe… te dhammā N … (a)saṅgahitā. (abridged)", "…, những hiện tượng ấy (không) được gộp vào N khối, …")
    P("te dhammā (answer subject)", "những hiện tượng ấy")
    P("X katihi khandhehi katihāyatanehi katihi dhātūhi sampayutto(ti)? Natthi. (ch7)",
      "X gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết và bao nhiêu yếu tố? Không có.")
    P("X…pe… sampayuttanti? Natthi. (abridged)", "X… gắn liền với bao nhiêu? Không có.")
    P("Katihi vippayutto? N khandhehi N āyatanehi N dhātūhi vippayutto.",
      "Không gắn liền với bao nhiêu? Không gắn liền với N khối, N lĩnh vực nhận biết và N yếu tố.")
    P("X tīhi khandhehi … sampayutto.", "X gắn liền với ba khối, ….")
    P("; ekenāyatanena ekāya dhātuyā kehici vippayutto.",
      "; không gắn liền với một số hiện tượng thuộc một lĩnh vực nhận biết và một yếu tố.")
    P("; ekena khandhena ekenāyatanena ekāya dhātuyā kehici sampayutto.",
      "; gắn liền với một số hiện tượng thuộc một khối, một lĩnh vực nhận biết và một yếu tố.")
    P("na kehici khandhehi na kehici āyatanehi N dhātūhi vippayuttā",
      "không có khối nào, không có lĩnh vực nhận biết nào mà chúng không gắn liền với, nhưng không gắn liền với "
      "N yếu tố")
    P("Xena ye dhammā sampayuttā, tehi dhammehi ye dhammā vippayuttā, te dhammā katihi … vippayuttā? (ch8)",
      "Những hiện tượng nào gắn liền với X; những hiện tượng nào không gắn liền với các hiện tượng đó, thì những "
      "hiện tượng ấy không gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết và bao nhiêu yếu tố?")
    P("Xena ye dhammā vippayuttā, te dhammā katihi … sampayuttāti? Natthi. (ch9)",
      "Những hiện tượng nào không gắn liền với X thì những hiện tượng ấy gắn liền với bao nhiêu khối, bao nhiêu "
      "lĩnh vực nhận biết và bao nhiêu yếu tố? Không có.")
    P("Xena ye dhammā sampayuttā, tehi dhammehi ye dhammā sampayuttā, te dhammā … sampayuttā? (ch10)",
      "Những hiện tượng nào gắn liền với X; những hiện tượng nào gắn liền với các hiện tượng đó, thì những hiện "
      "tượng ấy gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết và bao nhiêu yếu tố?")
    P("Xena ye dhammā khandhasaṅgahena saṅgahitā … , te dhammā katihi … sampayuttā? (ch12)",
      "Những hiện tượng nào được gộp vào cùng với X theo cách gộp vào khối, theo cách gộp vào lĩnh vực nhận biết và "
      "theo cách gộp vào yếu tố, thì những hiện tượng ấy gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết "
      "và bao nhiêu yếu tố?")
    P("Xena ye dhammā sampayuttā, te dhammā katihi … saṅgahitā? (ch13)",
      "Những hiện tượng nào gắn liền với X thì những hiện tượng ấy được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực "
      "nhận biết và bao nhiêu yếu tố?")
    P("Xena ye dhammā vippayuttā, te dhammā katihi … saṅgahitā? (ch15)",
      "Những hiện tượng nào không gắn liền với X thì những hiện tượng ấy được gộp vào bao nhiêu khối, bao nhiêu "
      "lĩnh vực nhận biết và bao nhiêu yếu tố?")
    P("pronoun for X", "nó (one named X or a list of singulars); chúng (X … dhammehi)")
    P("X in the instrumental (Cakkhāyatanena, cakkhudhātuyā, Cakkhundriyena, avijjāya, Dukkhasaccena, "
      "Kusalehi dhammehi …)", "the subject names above (NAMES / «các hiện tượng X»), unchanged")
    out = ["# pi-3 Dhātukathā: Vietnamese rails sentence formulas (binding for chapter agents)", "",
           "Format: Pāli = tiếng Việt, one per line; (pi-1) / (pi-2) = taken unchanged from the approved pi-1 / pi-2 "
           "Vietnamese rails (asserted by the builder). Generated by build_rails_sample_vi.py; import its constants "
           "rather than retyping. Termbase: AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md "
           "(+ pi-3-vi-ai/termbase/APPROVED.md). Style: 0-INBOX/temp/pipeline/vietnamese-style.md."] + F
    return unicodedata.normalize("NFC", "\n".join(out).replace("\n\n\n", "\n\n") + "\n")


def check_against_pali(text, pali_path):
    """Same block ids in order and same non-empty line count per segment."""
    def segs(t):
        res, cur = [], 0
        for ln in t.splitlines():
            if not ln.strip():
                continue
            cur += 1
            m = ID.search(ln)
            if m:
                res.append((m.group(1), cur))
                cur = 0
        return res
    a, b = segs(pali_path.read_text(encoding="utf-8")), segs(text)
    assert a == b, f"segment mismatch in {pali_path.name}"
    return len(a)


FILES = ["preamble.md", "1-uddeso.md", "2-pathamanayo.md"]

if __name__ == "__main__":
    n_reuse = check_reuse()
    OUT.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        txt = render_file(name)
        n = check_against_pali(txt, PALI / name)
        (OUT / name).write_text(txt, encoding="utf-8", newline="\n")
        print(f"{name}: {n} segments")
    (RAILS / "vi-rails-formulas.md").write_text(formulas(), encoding="utf-8", newline="\n")
    print(f"formulas written; {n_reuse} pi-1/pi-2 strings asserted")
