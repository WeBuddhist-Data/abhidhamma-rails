# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot SAMPLE: preamble, 1-uddeso.md, 2-pathamanayo.md.

usage: python -I -X utf8 build_sample_vi.py
Writes (only when run as a script, after the pi-1 / pi-2 string checks pass):
  AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\preamble.md, 1-uddeso.md, 2-pathamanayo.md

Other agents (chapters 3-15): `import build_sample_vi as B` and reuse the constants and functions verbatim:
  HOMAGE, PITAKA, BOOK_TITLE, BOOK_TITLE_Q, BOOK_END, CHAPTER_TITLES, ORDINAL, NIDDESA_TOPIC, niddesa_heading(),
  niddesa_closing(), SUBHEADINGS, LABELS, NUM, KH/AY/DH, count_phrase(), parse_counts(), incl(), excl(),
  Q_INCL, Q_EXCL, ASX, PRON_SG/PRON_PL, KHANDHA, AYATANA, DHATU, SACCA, INDRIYA, OTHER, MATRIX_PRED, VARIANTS,
  vi_item(), vi_subject(), join_ca(), cap(), segment_vi().
Vietnamese has no case or gender: one string per list member serves nominative, instrumental, genitive …;
the case is carried by the frame words (e.g. «với», «của»), which later chapters settle on top of these names.
Block IDs are never typed here: they are copied from the Pāli line at build time.
check_sources() asserts that every string registered with pi1() / pi2() still occurs in the pi-1 / pi-2
Vietnamese rails text (first letter in either case); it runs on import of main() and before writing.
"""
import os, re, sys, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, r"AI_translation\pali\pi-3_split_chapters")
OUT_DIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters")
PI1_DIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
PI2_DIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters")

ID = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")

_PI1, _PI2 = [], []


def pi1(s):
    """Mark a string as taken verbatim from the pi-1 Vietnamese rails text."""
    _PI1.append(s)
    return s


def pi2(s):
    """Mark a string as taken verbatim from the pi-2 Vietnamese rails text."""
    _PI2.append(s)
    return s


def _book_text(d):
    return "\n".join(open(os.path.join(d, f), encoding="utf-8").read() for f in sorted(os.listdir(d)) if f.endswith(".md"))


def check_sources():
    bad = []
    for strings, d, tag in ((_PI1, PI1_DIR, "pi-1"), (_PI2, PI2_DIR, "pi-2")):
        text = _book_text(d)
        for s in strings:
            if s not in text and (s[:1].upper() + s[1:]) not in text and (s[:1].lower() + s[1:]) not in text:
                bad.append(f"[{tag}] {s}")
    assert not bad, "strings no longer in the rails text:\n" + "\n".join(bad)
    return len(_PI1), len(_PI2)


def cap(s):
    """Upper-case the first letter (skipping an opening quote)."""
    i = 1 if s[:1] in "“‘" else 0
    return s[:i] + s[i:i + 1].upper() + s[i + 1:]


# ---------------------------------------------------------------- 1. book frame
HOMAGE = pi1("Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn")
PITAKA = pi1("Tạng Vi Diệu Pháp")
BOOK_TITLE = "Thảo luận về các yếu tố"                     # Dhātukathāpāḷi (proposal)
BOOK_TITLE_ALTERNATIVES = ["Bàn về các yếu tố", "Luận giải về các yếu tố"]
BOOK_TITLE_Q = "“" + BOOK_TITLE + "”"                     # mid-sentence form
PI1_TITLE_Q = "“" + pi1("Liệt kê các hiện tượng") + "”"    # Dhammasaṅgaṇī, mid-sentence
PI2_TITLE = pi2("Phân tích các hiện tượng")                # Vibhaṅga
BOOK_END = "Bộ " + BOOK_TITLE_Q + " đã hoàn tất."          # Dhātukathāpakaraṇaṃ niṭṭhitaṃ. (pi-1 ^1-1616 / pi-2 ^2-1044 pattern)
pi1("Bộ “Liệt kê các hiện tượng” đã hoàn tất.")

# ---------------------------------------------------------------- 2. chapter and section headings
UDDESO = pi1("Phần nêu đề mục")                           # ### Uddeso
ORDINAL = {1: "thứ nhất", 2: "thứ hai", 3: "thứ ba", 4: "thứ tư", 5: "thứ năm", 6: "thứ sáu", 7: "thứ bảy",
           8: "thứ tám", 9: "thứ chín", 10: "thứ mười", 11: "thứ mười một", 12: "thứ mười hai",
           13: "thứ mười ba", 14: "thứ mười bốn"}
NAYA = "Phương pháp"                                      # naya
# ### headings: file 1 = Uddeso, files 2..15 = Paṭhamanayo .. Cuddasamanayo (method n = file n+1)
CHAPTER_TITLES = {1: UDDESO}
CHAPTER_TITLES.update({n + 1: f"{NAYA} {ORDINAL[n]}" for n in range(1, 15)})

INCL_N = "sự gộp vào"            # saṅgaho
EXCL_N = "sự không gộp vào"      # asaṅgaho
ASSOC_N = "sự gắn liền"          # sampayogo   (pi-1 sampayutta «gắn liền với»)
DISS_N = "sự không gắn liền"     # vippayogo
INCL_X = "điều được gộp vào"     # saṅgahitaṃ / saṅgahitena (as a term of the method matrix)
EXCL_X = "điều không được gộp vào"
ASSOC_X = "điều gắn liền"
DISS_X = "điều không gắn liền"
BY = "dựa trên"                  # instrumental of the method names: saṅgahitena = «dựa trên điều được gộp vào»

# (1)..(14) of the Nayamātikā; the same words name the methods in the #### headings
NAYA_ITEMS = [
    f"{INCL_N} và {EXCL_N}",                                  # (1) saṅgaho asaṅgaho
    f"{EXCL_X} {BY} {INCL_X}",                                # (2) saṅgahitena asaṅgahitaṃ
    f"{INCL_X} {BY} {EXCL_X}",                                # (3) asaṅgahitena saṅgahitaṃ
    f"{INCL_X} {BY} {INCL_X}",                                # (4) saṅgahitena saṅgahitaṃ
    f"{EXCL_X} {BY} {EXCL_X}",                                # (5) asaṅgahitena asaṅgahitaṃ
    f"{ASSOC_N} và {DISS_N}",                                 # (6) sampayogo vippayogo
    f"{DISS_X} {BY} {ASSOC_X}",                               # (7) sampayuttena vippayuttaṃ
    f"{ASSOC_X} {BY} {DISS_X}",                               # (8) vippayuttena sampayuttaṃ
    f"{ASSOC_X} {BY} {ASSOC_X}",                              # (9) sampayuttena sampayuttaṃ
    f"{DISS_X} {BY} {DISS_X}",                                # (10) vippayuttena vippayuttaṃ
    f"{ASSOC_X} và {DISS_X} {BY} {INCL_X}",                   # (11) saṅgahitena sampayuttaṃ vippayuttaṃ
    f"{INCL_X} và {EXCL_X} {BY} {ASSOC_X}",                   # (12) sampayuttena saṅgahitaṃ asaṅgahitaṃ
    f"{ASSOC_X} và {DISS_X} {BY} {EXCL_X}",                   # (13) asaṅgahitena sampayuttaṃ vippayuttaṃ
    f"{INCL_X} và {EXCL_X} {BY} {DISS_X}",                    # (14) vippayuttena saṅgahitaṃ asaṅgahitaṃ
]
NIDDESA = "Giải thích đề mục về"                          # …padaniddeso (pi-1 niddeso «giải thích», Uddeso «phần nêu đề mục»)
# method n (1..14) -> words after «Giải thích đề mục về»
NIDDESA_TOPIC = {n: NAYA_ITEMS[n - 1] for n in range(1, 15)}


def niddesa_heading(n):
    """#### <X>padaniddeso of method n (1..14)."""
    return f"{NIDDESA} {NIDDESA_TOPIC[n]}"


def niddesa_closing(n):
    """Closing line '<X>padaniddeso paṭhamo.' … 'cuddasamo.'"""
    return f"{NIDDESA} {NIDDESA_TOPIC[n]}, phần {ORDINAL[n]}."


MATIKA = pi1("Ma trận")
UDDESA_SECTIONS = {  # #### headings of 1-uddeso.md
    "Nayamātikā": "Ma trận các phương pháp",
    "Abbhantaramātikā": "Ma trận bên trong",
    "Nayamukhamātikā": "Ma trận lối vào các phương pháp",
    "Lakkhaṇamātikā": "Ma trận các đặc tính",
    "Bāhiramātikā": "Ma trận bên ngoài",
}
SUBHEADINGS = {  # ##### headings inside the methods
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
LABELS = {  # closing labels of the rounds
    "(Ekamūlakaṃ.)": "(Phần xét từng mục một.)",
    "(Dukamūlakaṃ.)": "(Phần xét từng nhóm hai.)",
    "(Tikamūlakaṃ.)": "(Phần xét từng nhóm ba.)",
    "(Catukkamūlakaṃ.)": "(Phần xét từng nhóm bốn.)",
    "(Pañcakaṃ.)": "(Phần xét cả năm.)",
    "(Catukkaṃ.)": "(Phần xét cả bốn.)",
    "(Dvādasakaṃ.)": "(Phần xét cả mười hai.)",
    "(Aṭṭhārasakaṃ.)": "(Phần xét cả mười tám.)",
}

# ---------------------------------------------------------------- 3. numbers and count nouns
NUM = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười",
       11: "mười một", 12: "mười hai", 13: "mười ba", 14: "mười bốn", 15: "mười lăm", 16: "mười sáu",
       17: "mười bảy", 18: "mười tám"}
KH, AY, DH = "khối", "lĩnh vực nhận biết", "yếu tố"   # khandha / āyatana / dhātu as counted nouns
NOUNS = (KH, AY, DH)
_NK = {"ekena": 1, "dvīhi": 2, "tīhi": 3, "catūhi": 4, "pañcahi": 5}
_NA = {"ekenāyatanena": 1, "dvīhāyatanehi": 2, "tīhāyatanehi": 3, "pañcahāyatanehi": 5, "chahāyatanehi": 6,
       "sattahāyatanehi": 7, "navahāyatanehi": 9, "dasahāyatanehi": 10, "ekādasahāyatanehi": 11,
       "dvādasahāyatanehi": 12, "dvādasāyatanehi": 12}
_ND = {"ekāya": 1, "dvīhi": 2, "tīhi": 3, "pañcahi": 5, "chahi": 6, "sattahi": 7, "aṭṭhahi": 8, "navahi": 9,
       "dasahi": 10, "ekādasahi": 11, "dvādasahi": 12, "terasahi": 13, "pannarasahi": 15, "soḷasahi": 16,
       "sattarasahi": 17, "aṭṭhārasahi": 18}
_K = r"(?:na kehici khandhehi|ekena khandhena|(?:dvīhi|tīhi|catūhi|pañcahi) khandhehi)"
_A = r"(?:na kehici āyatanehi|[a-zāīūṃṅñṭḍṇḷ]+āyatane(?:hi|na))"
_D = r"(?:na kāhici dhātūhi|ekāya dhātuyā|[a-zāīūṃṅñṭḍṇḷ]+ dhātūhi)"
COUNTS_RX = rf"{_K},? {_A},? {_D}"


def parse_counts(s):
    """'catūhi khandhehi ekenāyatanena sattahi dhātūhi' -> [4, 1, 7]; 'na kehici …' -> None in that slot."""
    s = s[:1].lower() + s[1:]
    m = re.fullmatch(rf"({_K}),? ({_A}),? ({_D})", s)
    assert m, s
    k, a, d = m.groups()
    out = [None if k.startswith("na ") else _NK[k.split()[0]],
           None if a.startswith("na ") else _NA[a],
           None if d.startswith("na ") else _ND[d.split()[0]]]
    return out


def count_phrase(n, noun):
    return f"{NUM[n]} {noun}"


INCL = "được gộp vào"            # saṅgahita (pi-2 termbase saṅgahitaṃ / saṅgahitā «được gộp vào»)
EXCL = "không được gộp vào"      # asaṅgahita
pi2("được gộp vào")
PRON_SG, PRON_PL = "nó", "chúng"  # used only in the «na kehici …» exclusion frame
THI = "thì"                       # only after a subject ending in «được» (sanidassanā «thấy được»), to avoid «được được»
Q_INCL = "{s} được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"  # katihi … saṅgahito?
Q_EXCL = "Không được gộp vào bao nhiêu?"                                                     # Katihi asaṅgahito?
ASX = "xét theo khối thì ngoại trừ điều không do điều kiện tạo thành"   # asaṅkhataṃ khandhato ṭhapetvā
pi1("không do điều kiện tạo thành")
pi2("ngoại trừ")


def _runs(counts):
    runs = []
    for n, noun in zip(counts, NOUNS):
        pos = n is not None
        if runs and runs[-1][0] == pos:
            runs[-1][1].append((n, noun))
        else:
            runs.append((pos, [(n, noun)]))
    return runs


def incl(counts):
    """Predicate of saṅgahito: 'được gộp vào một khối, mười một lĩnh vực nhận biết, mười một yếu tố';
    na kehici khandhehi … : 'không được gộp vào khối nào, nhưng được gộp vào một lĩnh vực nhận biết, một yếu tố'."""
    parts = []
    for pos, items in _runs(counts):
        if pos:
            parts.append(INCL + " " + ", ".join(count_phrase(n, noun) for n, noun in items))
        else:
            parts.append(EXCL + " " + ", ".join(f"{noun} nào" for _, noun in items))
    return ", nhưng ".join(parts)


def excl(counts, pron):
    """Answer sentence of 'Katihi asaṅgahito?' (capitalised, without the final full stop).
    positive: 'Không được gộp vào bốn khối, một lĩnh vực nhận biết, bảy yếu tố'
    na kehici …: 'Không có khối nào, không có lĩnh vực nhận biết nào, không có yếu tố nào mà chúng không được gộp vào'"""
    parts = []
    for pos, items in _runs(counts):
        if pos:
            parts.append(EXCL + " " + ", ".join(count_phrase(n, noun) for n, noun in items))
        else:
            parts.append(", ".join(f"không có {noun} nào" for _, noun in items) + f" mà {pron} {EXCL}")
    return cap(", nhưng ".join(parts))


# ---------------------------------------------------------------- 4. list members (Pāli nominative -> Vietnamese)
FIVE_KHANDHA = pi2("Khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức")   # ^2-979
KHANDHA = {
    "rūpakkhandho": "khối vật chất", "vedanākkhandho": "khối cảm giác", "saññākkhandho": "khối tri giác",
    "saṅkhārakkhandho": "khối tạo tác", "viññāṇakkhandho": "khối thức",
}
TWELVE_AYATANA = pi2("Lĩnh vực mắt, lĩnh vực hình sắc, lĩnh vực tai, lĩnh vực âm thanh, lĩnh vực mũi, lĩnh vực mùi, "
                     "lĩnh vực lưỡi, lĩnh vực vị, lĩnh vực thân, lĩnh vực vật xúc chạm, lĩnh vực ý, "
                     "lĩnh vực đối tượng của ý")   # ^2-980
AYATANA = {
    "cakkhāyatanaṃ": "lĩnh vực mắt", "sotāyatanaṃ": "lĩnh vực tai", "ghānāyatanaṃ": "lĩnh vực mũi",
    "jivhāyatanaṃ": "lĩnh vực lưỡi", "kāyāyatanaṃ": "lĩnh vực thân", "rūpāyatanaṃ": "lĩnh vực hình sắc",
    "saddāyatanaṃ": "lĩnh vực âm thanh", "gandhāyatanaṃ": "lĩnh vực mùi", "rasāyatanaṃ": "lĩnh vực vị",
    "phoṭṭhabbāyatanaṃ": "lĩnh vực vật xúc chạm", "manāyatanaṃ": "lĩnh vực ý",
    "dhammāyatanaṃ": "lĩnh vực đối tượng của ý",
}
EIGHTEEN_DHATU = pi2("Yếu tố mắt, yếu tố hình sắc, yếu tố thức qua mắt, yếu tố tai, yếu tố âm thanh, yếu tố thức qua tai, "
                     "yếu tố mũi, yếu tố mùi, yếu tố thức qua mũi, yếu tố lưỡi, yếu tố vị, yếu tố thức qua lưỡi, "
                     "yếu tố thân, yếu tố vật xúc chạm, yếu tố thức qua thân, yếu tố ý, yếu tố đối tượng của ý, "
                     "yếu tố ý thức")   # ^2-981
DHATU = {
    "cakkhudhātu": "yếu tố mắt", "sotadhātu": "yếu tố tai", "ghānadhātu": "yếu tố mũi", "jivhādhātu": "yếu tố lưỡi",
    "kāyadhātu": "yếu tố thân", "rūpadhātu": "yếu tố hình sắc", "saddadhātu": "yếu tố âm thanh",
    "gandhadhātu": "yếu tố mùi", "rasadhātu": "yếu tố vị", "phoṭṭhabbadhātu": "yếu tố vật xúc chạm",
    "cakkhuviññāṇadhātu": "yếu tố thức qua mắt", "sotaviññāṇadhātu": "yếu tố thức qua tai",
    "ghānaviññāṇadhātu": "yếu tố thức qua mũi", "jivhāviññāṇadhātu": "yếu tố thức qua lưỡi",
    "kāyaviññāṇadhātu": "yếu tố thức qua thân", "manodhātu": "yếu tố ý", "manoviññāṇadhātu": "yếu tố ý thức",
    "dhammadhātu": "yếu tố đối tượng của ý",
}
FOUR_SACCA = pi2("Sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, sự thật về con đường")  # ^2-982
SACCA = {
    "dukkhasaccaṃ": "sự thật về khổ đau", "samudayasaccaṃ": "sự thật về sự phát sinh",
    "nirodhasaccaṃ": "sự thật về sự chấm dứt", "maggasaccaṃ": "sự thật về con đường",
}
TWENTYTWO_INDRIYA = pi2(
    "Năng lực mắt, năng lực tai, năng lực mũi, năng lực lưỡi, năng lực thân, năng lực ý, năng lực nữ tính, "
    "năng lực nam tính, năng lực sống, năng lực dễ chịu, năng lực khó chịu, năng lực niềm vui, năng lực nỗi buồn, "
    "năng lực bình thản, năng lực niềm tin, năng lực tinh tấn, năng lực tỉnh thức, năng lực định tâm, "
    "năng lực trí tuệ, năng lực biết được điều chưa từng biết, năng lực hiểu biết trọn vẹn, "
    "năng lực của người đã hiểu biết trọn vẹn")   # ^2-983
INDRIYA = {
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
}
TOTALS = {  # the whole lists; pi-2 ^2-978 «Năm khối, mười hai lĩnh vực nhận biết, mười tám yếu tố, bốn sự thật, hai mươi hai năng lực»
    "pañcakkhandhā": "năm khối", "dvādasāyatanāni": "mười hai lĩnh vực nhận biết",
    "aṭṭhārasa dhātuyo": "mười tám yếu tố", "cattāri saccāni": "bốn sự thật",
    "bāvīsatindriyāni": "hai mươi hai năng lực",
}
pi2("Năm khối, mười hai lĩnh vực nhận biết, mười tám yếu tố, bốn sự thật, hai mươi hai năng lực")
# dependent origination: the links keep pi-2's «X làm điều kiện cho Y» in quotes, as pi-2 quotes them (^2-226 …)
PS = {
    "avijjāpaccayā saṅkhārā": pi2("vô minh làm điều kiện cho các sự tạo tác"),
    "saṅkhārapaccayā viññāṇaṃ": pi2("các sự tạo tác làm điều kiện cho thức"),
    "viññāṇapaccayā nāmarūpaṃ": pi2("thức làm điều kiện cho phần tinh thần và vật chất"),
    "nāmarūpapaccayā saḷāyatanaṃ": pi2("phần tinh thần và vật chất làm điều kiện cho sáu lĩnh vực nhận biết"),
    "saḷāyatanapaccayā phasso": pi2("sáu lĩnh vực nhận biết làm điều kiện cho sự tiếp xúc"),
    "phassapaccayā vedanā": pi2("sự tiếp xúc làm điều kiện cho cảm giác"),
    "vedanāpaccayā taṇhā": pi2("cảm giác làm điều kiện cho khao khát"),
    "taṇhāpaccayā upādānaṃ": pi2("khao khát làm điều kiện cho sự bám víu"),
}
PS_Q = {k: "“" + v + "”" for k, v in PS.items()}
OTHER = {
    "paṭiccasamuppādo": pi1("sự sinh khởi tùy thuộc vào điều kiện"),
    "avijjā": pi2("vô minh"),
    "kammabhavo": pi2("sự hiện hữu dưới dạng nghiệp"),
    "upapattibhavo": pi2("sự hiện hữu dưới dạng tái sinh"),
    "kāmabhavo": pi2("sự hiện hữu ở cõi dục lạc"),
    "rūpabhavo": pi2("sự hiện hữu ở cõi hình sắc"),
    "arūpabhavo": pi2("sự hiện hữu ở cõi không hình sắc"),
    "saññābhavo": pi2("sự hiện hữu có tri giác"),
    "asaññābhavo": pi2("sự hiện hữu không có tri giác"),
    "nevasaññānāsaññābhavo": pi2("sự hiện hữu không phải có tri giác cũng không phải không có tri giác"),
    "ekavokārabhavo": pi2("sự hiện hữu gồm một khối"),
    "catuvokārabhavo": pi2("sự hiện hữu gồm bốn khối"),
    "pañcavokārabhavo": pi2("sự hiện hữu gồm năm khối"),
    "jāti": pi2("sự sinh"),
    "jarā": pi2("sự lão hóa"),
    "maraṇaṃ": pi2("sự chết"),
    "soko": pi2("sự sầu muộn"),
    "paridevo": pi2("sự than khóc"),
    "dukkhaṃ": pi2("sự khó chịu"),
    "domanassaṃ": pi2("nỗi buồn"),
    "upāyāso": pi2("sự tuyệt vọng"),
    "satipaṭṭhānaṃ": pi2("sự thiết lập tỉnh thức"),
    "sammappadhānaṃ": pi2("nỗ lực đúng đắn"),
    "iddhipādo": pi2("nền tảng thần thông"),
    "jhānaṃ": pi2("tầng thiền"),
    "appamaññā": pi2("trạng thái không thể đo lường"),
    "cattāro satipaṭṭhānā": pi2("bốn sự thiết lập tỉnh thức"),
    "cattāro sammappadhānā": pi2("bốn nỗ lực đúng đắn"),
    "cattāro iddhipādā": pi2("bốn nền tảng thần thông"),
    "cattāri jhānāni": pi2("bốn tầng thiền"),
    "catasso appamaññāyo": pi2("bốn trạng thái không thể đo lường"),
    "pañcindriyāni": pi2("năm năng lực"),
    "pañca balāni": pi2("năm sức mạnh"),
    "satta bojjhaṅgā": pi2("bảy chi phần giác ngộ"),
    "ariyo aṭṭhaṅgiko maggo": pi2("con đường gồm tám chi phần cao quý"),
    "phasso": pi2("sự tiếp xúc"),
    "vedanā": pi2("cảm giác"),
    "saññā": pi2("tri giác"),
    "cetanā": pi2("chủ ý"),
    "cittaṃ": pi1("tâm"),
    "adhimokkho": pi2("sự quyết định"),
    "manasikāro": pi1("sự chú tâm"),
}
pi2("Bốn sự thiết lập tỉnh thức, bốn nỗ lực đúng đắn, bốn nền tảng thần thông, năm năng lực, năm sức mạnh, "
    "bảy chi phần giác ngộ")                         # ^2-U26
pi2("Con đường gồm tám chi phần cao quý")          # ^2-486 (Maggaṅgavibhaṅga)
pi2("Bốn trạng thái không thể đo lường")           # ^2-? (Appamaññāvibhaṅga opening)
pi2("Bốn tầng thiền")                              # ^2-623
pi2("sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng")   # ^2-225
pi2("sự lão hóa và sự chết")
pi2("khao khát làm điều kiện cho sự quyết định")    # adhimokkho, ^2-280 ff.
pi1("có một sự tiếp xúc, có một cảm giác, có một tri giác, có một chủ ý, có một tâm")   # pi-1 ^1-… pentad

# matrix items: Pāli predicate (without «dhammā») -> Vietnamese predicate; the item is «các hiện tượng <pred>».
# Tag "m": pi-1 matrix line «(a) Các hiện tượng <pred>.»; tag "w": built only from pi-1 words, the predicate itself
# occurs in pi-1 (Nikkhepa / Aṭṭhakathā questions «Những hiện tượng nào <pred>?»).
_MP = [
    # triads
    ("kusalā", "thiện", "m"), ("akusalā", "bất thiện", "m"),
    ("abyākatā", "không xác định về mặt đạo đức", "m"),
    ("sukhāya vedanāya sampayuttā", "gắn liền với cảm giác dễ chịu", "m"),
    ("dukkhāya vedanāya sampayuttā", "gắn liền với cảm giác khó chịu", "m"),
    ("adukkhamasukhāya vedanāya sampayuttā", "gắn liền với cảm giác không khó chịu cũng không dễ chịu", "m"),
    ("vipākā", "là quả của nghiệp", "m"),
    ("vipākadhamma", "có khả năng sinh ra quả", "m"),                       # vipākadhammadhammā
    ("nevavipākanavipākadhamma", "không phải là quả của nghiệp cũng không có khả năng sinh ra quả", "m"),
    ("upādinnupādāniyā", "do nghiệp tạo ra và là đối tượng của sự bám víu", "m"),
    ("anupādinnupādāniyā", "không do nghiệp tạo ra nhưng là đối tượng của sự bám víu", "m"),
    ("anupādinnaanupādāniyā", "không do nghiệp tạo ra và không phải là đối tượng của sự bám víu", "m"),
    ("saṃkiliṭṭhasaṃkilesikā", "bị phiền não làm vẩn đục và là đối tượng của phiền não", "m"),
    ("asaṃkiliṭṭhasaṃkilesikā", "không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não", "m"),
    ("asaṃkiliṭṭhaasaṃkilesikā", "không bị phiền não làm vẩn đục và không phải là đối tượng của phiền não", "m"),
    ("savitakkasavicārā", "có sự hướng tâm và sự duy trì tâm", "m"),
    ("avitakkavicāramattā", "không có sự hướng tâm, chỉ có sự duy trì tâm", "m"),
    ("avitakkaavicārā", "không có sự hướng tâm cũng không có sự duy trì tâm", "m"),
    ("pītisahagatā", "có sự hân hoan đi kèm", "m"), ("sukhasahagatā", "có hạnh phúc đi kèm", "m"),
    ("upekkhāsahagatā", "có sự bình thản đi kèm", "m"),
    ("dassanena pahātabbā", "cần dứt bỏ bằng sự thấy chân lý", "m"),
    ("bhāvanāya pahātabbā", "cần dứt bỏ bằng sự tu tập", "m"),
    ("neva dassanena na bhāvanāya pahātabbā",
     "không cần dứt bỏ bằng sự thấy chân lý cũng không cần dứt bỏ bằng sự tu tập", "m"),
    ("dassanena pahātabbahetukā", "có gốc rễ cần dứt bỏ bằng sự thấy chân lý", "m"),
    ("bhāvanāya pahātabbahetukā", "có gốc rễ cần dứt bỏ bằng sự tu tập", "m"),
    ("neva dassanena na bhāvanāya pahātabbahetukā",
     "không có gốc rễ nào cần dứt bỏ bằng sự thấy chân lý, cũng không có gốc rễ nào cần dứt bỏ bằng sự tu tập", "m"),
    ("ācayagāmino", "dẫn đến sự tích lũy", "m"), ("apacayagāmino", "dẫn đến sự giảm trừ", "m"),
    ("nevācayagāmināpacayagāmino", "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ", "m"),
    ("sekkhā", "thuộc về người còn đang tu học", "m"), ("asekkhā", "thuộc về người đã hoàn tất tu học", "m"),
    ("nevasekkhanāsekkhā", "không thuộc về người còn đang tu học cũng không thuộc về người đã hoàn tất tu học", "m"),
    ("parittā", "hạn hẹp", "m"), ("mahaggatā", "rộng lớn", "m"), ("appamāṇā", "không thể đo lường", "m"),
    ("parittārammaṇā", "có đối tượng hạn hẹp", "m"), ("mahaggatārammaṇā", "có đối tượng rộng lớn", "m"),
    ("appamāṇārammaṇā", "có đối tượng không thể đo lường", "m"),
    ("hīnā", "thấp kém", "m"), ("majjhimā", "trung bình", "m"), ("paṇītā", "ưu việt", "m"),
    ("micchattaniyatā", "cố định theo hướng sai lầm", "m"), ("sammattaniyatā", "cố định theo hướng đúng đắn", "m"),
    ("aniyatā", "không cố định", "m"),
    ("maggārammaṇā", "lấy con đường làm đối tượng", "m"), ("maggahetukā", "lấy con đường làm gốc rễ", "m"),
    ("maggādhipatino", "lấy con đường làm yếu tố chủ đạo", "m"),
    ("uppannā", "đã sinh khởi", "m"), ("anuppannā", "chưa sinh khởi", "m"), ("uppādino", "sẽ sinh khởi", "m"),
    ("atītā", "thuộc quá khứ", "m"), ("anāgatā", "thuộc tương lai", "m"), ("paccuppannā", "thuộc hiện tại", "m"),
    ("atītārammaṇā", "có đối tượng thuộc quá khứ", "m"), ("anāgatārammaṇā", "có đối tượng thuộc tương lai", "m"),
    ("paccuppannārammaṇā", "có đối tượng thuộc hiện tại", "m"),
    ("ajjhattā", "ở nơi bản thân", "m"), ("bahiddhā", "ở bên ngoài bản thân", "m"),
    ("ajjhattabahiddhā", "ở nơi bản thân và ở bên ngoài bản thân", "m"),
    ("ajjhattārammaṇā", "có đối tượng ở nơi bản thân", "m"),
    ("bahiddhārammaṇā", "có đối tượng ở bên ngoài bản thân", "m"),
    ("ajjhattabahiddhārammaṇā", "có đối tượng ở nơi bản thân và ở bên ngoài bản thân", "m"),
    ("sanidassanasappaṭighā", "thấy được và có tính va chạm", "m"),
    ("anidassanasappaṭighā", "không thấy được nhưng có tính va chạm", "m"),
    ("anidassanaappaṭighā", "không thấy được và không có tính va chạm", "m"),
    # dyads
    ("hetū", "là gốc rễ", "m"), ("na hetū", "không phải là gốc rễ", "m"),
    ("sahetukā", "có gốc rễ", "m"), ("ahetukā", "không có gốc rễ", "m"),
    ("hetusampayuttā", "gắn liền với gốc rễ", "m"), ("hetuvippayuttā", "không gắn liền với gốc rễ", "m"),
    ("hetū ceva sahetukā ca", "vừa là gốc rễ vừa có gốc rễ", "m"),
    ("sahetukā ceva na ca hetū", "có gốc rễ nhưng không phải là gốc rễ", "m"),
    ("hetū ceva hetusampayuttā ca", "vừa là gốc rễ vừa gắn liền với gốc rễ", "m"),
    ("hetusampayuttā ceva na ca hetū", "gắn liền với gốc rễ nhưng không phải là gốc rễ", "m"),
    ("na hetū sahetukā", "không phải là gốc rễ nhưng có gốc rễ", "w"),
    ("na hetū ahetukā", "không phải là gốc rễ và không có gốc rễ", "w"),
    ("sappaccayā", "có điều kiện", "m"), ("appaccayā", "không có điều kiện", "m"),
    ("saṅkhatā", "do điều kiện tạo thành", "m"), ("asaṅkhatā", "không do điều kiện tạo thành", "m"),
    ("sanidassanā", "thấy được", "m"), ("anidassanā", "không thấy được", "m"),
    ("sappaṭighā", "có tính va chạm", "m"), ("appaṭighā", "không có tính va chạm", "m"),
    ("rūpino", "thuộc vật chất", "m"), ("arūpino", "phi vật chất", "m"),
    ("lokiyā", "thuộc thế gian", "m"), ("lokuttarā", "vượt thế gian", "m"),
    ("kenaci viññeyyā", "mà một loại thức nào đó có thể nhận biết", "m"),
    ("kenaci na viññeyyā", "mà một loại thức nào đó không thể nhận biết", "m"),
    ("āsavā", "là ô nhiễm", "m"), ("no āsavā", "không phải là ô nhiễm", "m"),
    ("sāsavā", "là đối tượng của ô nhiễm", "m"), ("anāsavā", "không phải là đối tượng của ô nhiễm", "m"),
    ("āsavasampayuttā", "gắn liền với ô nhiễm", "m"), ("āsavavippayuttā", "không gắn liền với ô nhiễm", "m"),
    ("āsavā ceva sāsavā ca", "vừa là ô nhiễm vừa là đối tượng của ô nhiễm", "m"),
    ("sāsavā ceva no ca āsavā", "là đối tượng của ô nhiễm nhưng không phải là ô nhiễm", "m"),
    ("āsavā ceva āsavasampayuttā ca", "vừa là ô nhiễm vừa gắn liền với ô nhiễm", "m"),
    ("āsavasampayuttā ceva no ca āsavā", "gắn liền với ô nhiễm nhưng không phải là ô nhiễm", "m"),
    ("āsavavippayuttā sāsavā", "không gắn liền với ô nhiễm nhưng là đối tượng của ô nhiễm", "w"),
    ("āsavavippayuttā anāsavā", "không gắn liền với ô nhiễm và không phải là đối tượng của ô nhiễm", "w"),
    ("saṃyojanā", "là xiềng xích", "m"), ("ganthā", "là nút thắt", "m"), ("oghā", "là dòng lũ", "m"),
    ("yogā", "là ách", "m"), ("nīvaraṇā", "là chướng ngại", "m"),
    ("parāmāsā", "là sự hiểu sai lệch", "m"), ("no parāmāsā", "không phải là sự hiểu sai lệch", "m"),
    ("parāmaṭṭhā", "bị sự hiểu sai lệch nắm giữ", "m"), ("aparāmaṭṭhā", "không bị sự hiểu sai lệch nắm giữ", "m"),
    ("parāmāsasampayuttā", "gắn liền với sự hiểu sai lệch", "m"),
    ("parāmāsavippayuttā", "không gắn liền với sự hiểu sai lệch", "m"),
    ("parāmāsā ceva parāmaṭṭhā ca", "vừa là sự hiểu sai lệch vừa bị sự hiểu sai lệch nắm giữ", "m"),
    ("parāmaṭṭhā ceva no ca parāmāsā", "bị sự hiểu sai lệch nắm giữ nhưng không phải là sự hiểu sai lệch", "m"),
    ("parāmāsavippayuttā parāmaṭṭhā", "không gắn liền với sự hiểu sai lệch nhưng bị sự hiểu sai lệch nắm giữ", "w"),
    ("parāmāsavippayuttā aparāmaṭṭhā", "không gắn liền với sự hiểu sai lệch và không bị sự hiểu sai lệch nắm giữ", "w"),
    ("sārammaṇā", "có đối tượng", "m"), ("anārammaṇā", "không có đối tượng", "m"),
    ("cittā", "là tâm", "m"), ("no cittā", "không phải là tâm", "m"),
    ("cetasikā", "là yếu tố đồng hành với tâm", "m"), ("acetasikā", "không phải là yếu tố đồng hành với tâm", "m"),
    ("cittasampayuttā", "gắn liền với tâm", "m"), ("cittavippayuttā", "không gắn liền với tâm", "m"),
    ("cittasaṃsaṭṭhā", "hòa lẫn với tâm", "m"), ("cittavisaṃsaṭṭhā", "không hòa lẫn với tâm", "m"),
    ("cittasamuṭṭhānā", "do tâm sinh ra", "m"), ("no cittasamuṭṭhānā", "không do tâm sinh ra", "m"),
    ("cittasahabhuno", "cùng tồn tại với tâm", "m"), ("no cittasahabhuno", "không cùng tồn tại với tâm", "m"),
    ("cittānuparivattino", "vận hành theo tâm", "m"), ("no cittānuparivattino", "không vận hành theo tâm", "m"),
    ("cittasaṃsaṭṭhasamuṭṭhānā", "vừa hòa lẫn với tâm vừa do tâm sinh ra", "m"),
    ("no cittasaṃsaṭṭhasamuṭṭhānā", "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra", "m"),
    ("cittasaṃsaṭṭhasamuṭṭhānasahabhuno", "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm", "m"),
    ("no cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
     "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm", "m"),
    ("cittasaṃsaṭṭhasamuṭṭhānānuparivattino", "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm", "m"),
    ("no cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
     "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm", "m"),
    ("ajjhattikā", "thuộc phần bên trong", "m"), ("bāhirā", "thuộc phần bên ngoài", "m"),
    ("upādā", "phái sinh", "m"), ("no upādā", "không phải là phái sinh", "m"),
    ("upādinnā", "do nghiệp tạo ra", "m"), ("anupādinnā", "không do nghiệp tạo ra", "m"),
    ("upādānā", "là sự bám víu", "m"),
    ("kilesā", "là phiền não", "m"), ("no kilesā", "không phải là phiền não", "m"),
    ("saṃkilesikā", "là đối tượng của phiền não", "m"), ("asaṃkilesikā", "không phải là đối tượng của phiền não", "m"),
    ("saṃkiliṭṭhā", "bị phiền não làm vẩn đục", "m"), ("asaṃkiliṭṭhā", "không bị phiền não làm vẩn đục", "m"),
    ("kilesasampayuttā", "gắn liền với phiền não", "m"), ("kilesavippayuttā", "không gắn liền với phiền não", "m"),
    ("kilesā ceva saṃkilesikā ca", "vừa là phiền não vừa là đối tượng của phiền não", "m"),
    ("saṃkilesikā ceva no ca kilesā", "là đối tượng của phiền não nhưng không phải là phiền não", "m"),
    ("kilesā ceva saṃkiliṭṭhā ca", "vừa là phiền não vừa bị phiền não làm vẩn đục", "m"),
    ("saṃkiliṭṭhā ceva no ca kilesā", "bị phiền não làm vẩn đục nhưng không phải là phiền não", "m"),
    ("kilesā ceva kilesasampayuttā ca", "vừa là phiền não vừa gắn liền với phiền não", "m"),
    ("kilesasampayuttā ceva no ca kilesā", "gắn liền với phiền não nhưng không phải là phiền não", "m"),
    ("kilesavippayuttā saṃkilesikā", "không gắn liền với phiền não nhưng là đối tượng của phiền não", "w"),
    ("kilesavippayuttā asaṃkilesikā", "không gắn liền với phiền não và không phải là đối tượng của phiền não", "w"),
    ("na dassanena pahātabbā", "không cần dứt bỏ bằng sự thấy chân lý", "m"),
    ("na bhāvanāya pahātabbā", "không cần dứt bỏ bằng sự tu tập", "m"),
    ("na dassanena pahātabbahetukā", "không có gốc rễ nào cần dứt bỏ bằng sự thấy chân lý", "m"),
    ("na bhāvanāya pahātabbahetukā", "không có gốc rễ nào cần dứt bỏ bằng sự tu tập", "m"),
    ("savitakkā", "có sự hướng tâm", "m"), ("avitakkā", "không có sự hướng tâm", "m"),
    ("savicārā", "có sự duy trì tâm", "m"), ("avicārā", "không có sự duy trì tâm", "m"),
    ("sappītikā", "có sự hân hoan", "m"), ("appītikā", "không có sự hân hoan", "m"),
    ("na pītisahagatā", "không có sự hân hoan đi kèm", "m"), ("na sukhasahagatā", "không có hạnh phúc đi kèm", "m"),
    ("na upekkhāsahagatā", "không có sự bình thản đi kèm", "m"),
    ("kāmāvacarā", "thuộc cõi dục lạc", "m"), ("na kāmāvacarā", "không thuộc cõi dục lạc", "m"),
    ("rūpāvacarā", "thuộc cõi hình sắc", "m"), ("na rūpāvacarā", "không thuộc cõi hình sắc", "m"),
    ("arūpāvacarā", "thuộc cõi không hình sắc", "m"), ("na arūpāvacarā", "không thuộc cõi không hình sắc", "m"),
    ("pariyāpannā", "nằm trong các cõi tồn tại", "m"), ("apariyāpannā", "không nằm trong các cõi tồn tại", "m"),
    ("niyyānikā", "dẫn đến giải thoát", "m"), ("aniyyānikā", "không dẫn đến giải thoát", "m"),
    ("niyatā", "cố định", "m"),
    ("sauttarā", "còn có điều cao hơn", "m"), ("anuttarā", "không có điều gì cao hơn", "m"),
    ("saraṇā", "có xung đột", "m"), ("araṇā", "không có xung đột", "m"),
]
MATRIX_PRED = {}
for _p, _v, _t in _MP:
    assert _p not in MATRIX_PRED or MATRIX_PRED[_p] == _v, _p
    MATRIX_PRED[_p] = _v
    pi1(("Các hiện tượng " + _v) if _t == "m" else _v)   # matrix line, before its «.» or variant bracket
DHAMMA = "các hiện tượng"   # dhammā in the matrix names (pi-1 matrix)

VARIANTS = {  # variant / editorial brackets of the sample, Pāli kept inside
    "[parittāramaṇā (?)]": "[khác chính tả (?): parittāramaṇā]",
    "[na hetū ahetukā (syā. ka.) vibha. dukapañhāpucchakepi]":
        "[dị bản (Syā., Ka.): na hetū ahetukā; " + PI2_TITLE + ", cả trong phần hỏi đáp về bộ đôi]",
    "[upādānapaccayā kammabhavo (sī. syā.)]": "[dị bản (Sī., Syā.): upādānapaccayā kammabhavo]",
}
pi2("Phần hỏi đáp")

# ^3-71 'Jāti dvīhi khandhehi… jarā dvīhi khandhehi… maraṇaṃ dvīhi khandhehi …': each member keeps its count
SPECIAL_ITEMS = {
    "jāti dvīhi khandhehi": OTHER["jāti"] + " " + INCL + " " + count_phrase(2, KH),
    "jarā dvīhi khandhehi": OTHER["jarā"] + " " + INCL + " " + count_phrase(2, KH),
}


def join_ca(items):
    """X ca Y ca (Z ca) -> 'X và Y' / 'X, Y và Z'."""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " và " + items[-1]


def _single(p):
    for d in (KHANDHA, AYATANA, DHATU, SACCA, INDRIYA, TOTALS, PS_Q, OTHER, SPECIAL_ITEMS):
        if p in d:
            return d[p]
    return None


def vi_item(pali):
    """One list member as it stands in the Pāli (any first-letter case), lower-case Vietnamese."""
    p = pali.strip()
    p = p[:1].lower() + p[1:]
    m = re.fullmatch(r"(.*?) (\[[^\]]+\])( dhammā)?", p)
    if m:   # variant bracket inside the member
        base = m.group(1) + (m.group(3) or "")
        return vi_item(base) + " " + VARIANTS[m.group(2)]
    v = _single(p)
    if v is not None:
        return v
    if p.endswith("dhammā"):
        pred = p[:-len(" dhammā")] if p.endswith(" dhammā") else p[:-len("dhammā")]
        return DHAMMA + " " + MATRIX_PRED[pred]
    # X ca Y ca … / Xañca Yañca …
    toks, items = p.split(), []
    for t in toks:
        if t == "ca":
            continue
        items.append(t[:-3] + "ṃ" if t.endswith("ñca") else t)
    vs = [_single(t) for t in items]
    assert all(vs) and len(vs) > 1, f"unknown member: {pali}"
    return join_ca(vs)


def vi_subject(pali):
    """A subject as it stands in the Pāli: members separated by '…' / '…pe…'; a trailing '…pe…' stays '…'."""
    s = pali.replace("…pe…", "…").strip()
    trail = s.endswith("…")
    parts = [x.strip() for x in s.split("…") if x.strip()]
    out = "… ".join(vi_item(x) for x in parts) + ("…" if trail else "")
    return cap(out)


# ---------------------------------------------------------------- 5. the saṅgaha / asaṅgaha segment
_SEG = re.compile(
    rf"^(?P<subj>.+?)(?: katihi khandhehi katihāyatanehi katihi dhātūhi (?P<qv>saṅgahit\w+)\? (?P<subj2>.+?))?"
    rf"(?P<asx> asaṅkhataṃ khandhato ṭhapetvā)? (?P<inc>{COUNTS_RX}) (?P<v>saṅgahit\w+)\. "
    rf"Katihi asaṅgahit\w+\? (?P<exc>{COUNTS_RX}) asaṅgahit\w+\.$", re.I)


def segment_vi(line):
    """Translate one saṅgaha / asaṅgaha line of the first method (without its block ID)."""
    m = _SEG.match(line)
    assert m, line
    v = m.group("v")
    pron = PRON_SG if v.endswith(("o", "aṃ")) else PRON_PL
    subj = vi_subject(m.group("subj"))
    out = []
    if m.group("qv"):
        out.append(Q_INCL.format(s=subj))
        subj = vi_subject(m.group("subj2"))
    pred = incl(parse_counts(m.group("inc")))
    if m.group("asx"):
        out.append(f"{subj}, {ASX}, {pred}.")
    elif subj.endswith(" được") and pred.startswith(INCL):
        out.append(f"{subj} {THI} {pred}.")      # «Các hiện tượng thấy được thì được gộp vào …» (no «được được»)
    else:
        out.append(f"{subj} {pred}.")
    out.append(Q_EXCL)
    out.append(excl(parse_counts(m.group("exc")), pron) + ".")
    return " ".join(out)


# ---------------------------------------------------------------- 6. chapter 1 (Uddeso)
NAYA_MATRIX_LINE = " ".join(f"({i}) {cap(t) if i == 1 else t}" for i, t in enumerate(NAYA_ITEMS, 1)) + "."
INNER_ITEMS = [
    TOTALS["pañcakkhandhā"], TOTALS["dvādasāyatanāni"], TOTALS["aṭṭhārasa dhātuyo"], TOTALS["cattāri saccāni"],
    TOTALS["bāvīsatindriyāni"], OTHER["paṭiccasamuppādo"], OTHER["cattāro satipaṭṭhānā"],
    OTHER["cattāro sammappadhānā"], OTHER["cattāro iddhipādā"], OTHER["cattāri jhānāni"],
    OTHER["catasso appamaññāyo"], OTHER["pañcindriyāni"], OTHER["pañca balāni"], OTHER["satta bojjhaṅgā"],
    OTHER["ariyo aṭṭhaṅgiko maggo"],
    ", ".join(OTHER[k] for k in ("phasso", "vedanā", "saññā", "cetanā", "cittaṃ", "adhimokkho", "manasikāro")),
]
INNER_MATRIX_LINE = " ".join(f"({i}) {cap(t) if i == 1 else t}" for i, t in enumerate(INNER_ITEMS, 1)) + "."
NAYAMUKHA_LINE = (f"{cap(INCL_N)} theo ba phương diện, {EXCL_N} theo ba phương diện, "
                  f"{ASSOC_N} theo bốn phương diện, {DISS_N} theo bốn phương diện.")
SABHAGA, VISABHAGA = "cùng loại", "khác loại"
LAKKHANA_LINE = f"{cap(SABHAGA)}, {VISABHAGA}."
BAHIRA_LINE = f"Toàn bộ {PI1_TITLE_Q} là {MATIKA.lower()} của {BOOK_TITLE_Q}."

UDDESO_TEXT = {
    "Nayamātikā": NAYA_MATRIX_LINE, "Abbhantaramātikā": INNER_MATRIX_LINE, "Nayamukhamātikā": NAYAMUKHA_LINE,
    "Lakkhaṇamātikā": LAKKHANA_LINE, "Bāhiramātikā": BAHIRA_LINE,
}


# ---------------------------------------------------------------- 7. build
def _segments(path):
    text = open(path, encoding="utf-8").read()
    return [b.split("\n") for b in text.strip("\n").split("\n\n")]


def _heading(line):
    m = re.match(r"^(#+) (.+?)\s+(\^\S+)$", line)
    return m.groups() if m else None


def build_preamble():
    return f"{HOMAGE} ^T-1\n\n# {PITAKA} ^0\n\n## {BOOK_TITLE} ^3-0\n"


def build_uddeso():
    out, last = [], None
    for seg in _segments(os.path.join(PALI_DIR, "1-uddeso.md")):
        assert len(seg) == 1, seg
        line = seg[0]
        h = _heading(line)
        bid = ID.search(line).group(1)
        if h:
            hashes, title, _ = h
            vi = UDDESO if title == "Uddeso" else UDDESA_SECTIONS[title]
            out.append(f"{hashes} {vi} {bid}")
            last = title
        else:
            out.append(f"{UDDESO_TEXT[last]} {bid}")
    return "\n\n".join(out) + "\n"


def build_pathamanayo():
    out = []
    for seg in _segments(os.path.join(PALI_DIR, "2-pathamanayo.md")):
        vi = []
        for i, line in enumerate(seg):
            idm = ID.search(line)
            bid = idm.group(1) if idm else None
            body = ID.sub("", line).strip()
            h = _heading(line)
            if h:
                hashes, title, _ = h
                if title == "Paṭhamanayo":
                    t = CHAPTER_TITLES[2]
                elif title == "Saṅgahāsaṅgahapadaniddeso":
                    t = niddesa_heading(1)
                else:
                    t = SUBHEADINGS[title]
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in LABELS:
                t = LABELS[body]
            elif body == "Saṅgahāsaṅgahapadaniddeso paṭhamo.":
                t = niddesa_closing(1)
            else:
                assert i == 0, line
                t = segment_vi(body)
            vi.append(t + (f" {bid}" if bid else ""))
        out.append("\n".join(vi))
    return "\n\n".join(out) + "\n"


def main():
    n1, n2 = check_sources()
    files = {"preamble.md": build_preamble(), "1-uddeso.md": build_uddeso(), "2-pathamanayo.md": build_pathamanayo()}
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, text in files.items():
        assert unicodedata.normalize("NFC", text) == text, name
        assert "—" not in text and ":-" not in text and "…." not in text, name
        with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {', '.join(files)} to {OUT_DIR}")


if __name__ == "__main__":
    main()
