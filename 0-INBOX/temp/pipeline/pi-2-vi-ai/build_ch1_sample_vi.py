# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: preamble + chapter-1 sample (first 77 non-empty lines).

usage: python -I -X utf8 build_ch1_sample_vi.py
Writes (only when run as a script):
  AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\preamble.md
  0-INBOX\\temp\\pipeline\\pi-2-vi-ai\\ch1-sample.md   (Vietnamese of ch1-sample-pali.md, same blank lines)

Other agents: import this module and reuse the constants and frame functions verbatim
(HOMAGE, PITAKA, BOOK_TITLE, CHAPTER_TITLES, CHAPTER_CLOSING, SECTION_TITLES, AGG, ATTR, FIVE_AGGREGATES,
KHANDHA_SPAN, KHANDHA_TOGETHER, TIME, SELF, MEMBERS, QUAL, FEEL, PRED, question, question_pair, answer,
khandha_question, khandha_answer, khandha_def, time_line, self_line, np, clause, comp_line, relation_groups,
tail, class_open, class_close, NUM, RUPA_* strings ...).
Vietnamese has no gender/number agreement: one string per formula serves every aggregate.
Block IDs are never typed here: they are copied from the Pāli line at build time.
main() asserts that every string marked [pi-1] still occurs byte for byte in the reviewed pi-1 Vietnamese rails.
"""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
VI_DIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters")
PI1_VI_DIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-2-vi-ai")

DASH = "–"  # the only dash allowed, and only where the Pāli has one
ID = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")

# ---------------------------------------------------------------- 1. book frame and headings
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"   # [pi-1]
PITAKA = "Tạng Vi Diệu Pháp"                                             # [pi-1]
BOOK_TITLE = "Phân tích các hiện tượng"                                  # Vibhaṅgapāḷi (proposal; pairs with pi-1 «Liệt kê các hiện tượng»)
BOOK_TITLE_ALTERNATIVES = ["Phân tích chi tiết", "Sách phân tích"]
BOOK_TITLE_QUOTED = "“" + BOOK_TITLE + "”"                              # mid-sentence form

CHAPTER_TITLES = {  # ### level; vibhaṅga = «phân tích» (pi-1 vibhatti / bhājanīya = «phân tích»)
    1: "Phân tích các khối",                                    # Khandhavibhaṅgo
    2: "Phân tích các lĩnh vực nhận biết",                      # Āyatanavibhaṅgo
    3: "Phân tích các yếu tố",                                  # Dhātuvibhaṅgo
    4: "Phân tích các sự thật",                                 # Saccavibhaṅgo
    5: "Phân tích các năng lực",                                # Indriyavibhaṅgo
    6: "Phân tích sự sinh khởi tùy thuộc vào điều kiện",        # Paṭiccasamuppādavibhaṅgo
    7: "Phân tích sự thiết lập tỉnh thức",                      # Satipaṭṭhānavibhaṅgo
    8: "Phân tích các nỗ lực đúng đắn",                         # Sammappadhānavibhaṅgo
    9: "Phân tích các nền tảng thần thông",                     # Iddhipādavibhaṅgo
    10: "Phân tích các chi phần giác ngộ",                      # Bojjhaṅgavibhaṅgo
    11: "Phân tích các chi phần của con đường",                 # Maggaṅgavibhaṅgo
    12: "Phân tích các tầng thiền",                             # Jhānavibhaṅgo
    13: "Phân tích các trạng thái không thể đo lường",          # Appamaññāvibhaṅgo
    14: "Phân tích các điều tu học",                            # Sikkhāpadavibhaṅgo
    15: "Phân tích các loại hiểu biết thông suốt",              # Paṭisambhidāvibhaṅgo
    16: "Phân tích các loại hiểu biết",                         # Ñāṇavibhaṅgo
    17: "Phân tích các chủ đề nhỏ",                             # Khuddakavatthuvibhaṅgo
    18: "Phân tích cốt lõi của các hiện tượng",                 # Dhammahadayavibhaṅgo
}
CHAPTER_CLOSING = "{title} đã hoàn tất."  # "<X>vibhaṅgo niṭṭhito."  pi-1: «Ma trận đã hoàn tất.»

SECTION_TITLES = {  # #### level; the closing line repeats the words + "." (pi-1: Padabhājanīyaṃ. = «Phân tích từng từ.»)
    "Suttantabhājanīyaṃ": "Phân tích theo kinh",
    "Abhidhammabhājanīyaṃ": "Phân tích theo Vi Diệu Pháp",
    "Pañhāpucchakaṃ": "Phần hỏi đáp",
}

# ---------------------------------------------------------------- 2. aggregates  [pi-1]
AGG = {
    "rupa": dict(noun="vật chất", khandha="khối vật chất", any="Bất cứ vật chất nào",
                 such="vật chất này hay vật chất kia"),
    "vedana": dict(noun="cảm giác", khandha="khối cảm giác", any="Bất cứ cảm giác nào",
                   such="cảm giác này hay cảm giác kia"),
    "sanna": dict(noun="tri giác", khandha="khối tri giác", any="Bất cứ tri giác nào",
                  such="tri giác này hay tri giác kia"),
    "sankhara": dict(noun="các sự tạo tác", khandha="khối tạo tác", any="Bất cứ những sự tạo tác nào",
                     such="các sự tạo tác này hay các sự tạo tác kia"),
    "vinnana": dict(noun="thức", khandha="khối thức", any="Bất cứ thức nào",
                    such="thức này hay thức kia"),
}
# [pi-1 ^1-1089]
FIVE_AGGREGATES = "Năm khối " + DASH + " khối vật chất, khối cảm giác, khối tri giác, khối tạo tác và khối thức"


def cap(s):
    return s[:1].upper() + s[1:]


def low(s):
    return s[:1].lower() + s[1:]


def heading(a):
    return cap(AGG[a]["khandha"])


# attributes, always after the noun  [pi-1 matrix and Rūpakaṇḍa words]
ATTR = {
    "atita": "thuộc quá khứ", "anagata": "thuộc tương lai", "paccuppanna": "thuộc hiện tại",
    "ajjhatta": "ở nơi bản thân", "bahiddha": "ở bên ngoài bản thân",
    "olarika": "ở dạng thô", "sukhuma": "ở dạng vi tế",
    "hina": "thấp kém", "panita": "ưu việt",
    "dure": "ở xa", "santike": "ở gần",
}

# ---------------------------------------------------------------- 3. question / answer frames  [pi-1 ^1-584, ^1-1008]
TATTHA = "Ở đây,"                 # Tattha katamo/katamā/katamaṃ/katame <X>?  ->  Ở đây, <X> là gì?
VUCCATI = "đó được gọi là"        # idaṃ / ayaṃ vuccati; ime vuccanti (same Vietnamese)


def question(a, key):
    """Tattha katamaṃ rūpaṃ atītaṃ?  ->  Ở đây, vật chất thuộc quá khứ là gì?"""
    return f"{TATTHA} {AGG[a]['noun']} {ATTR[key]} là gì?"


def question_pair(a, x, y):
    """Tattha katamā vedanā oḷārikā sukhumā?  ->  Ở đây, cảm giác ở dạng thô và ở dạng vi tế là gì?"""
    return f"{TATTHA} {AGG[a]['noun']} {ATTR[x]} và {ATTR[y]} là gì?"


def answer(a, key):
    """idaṃ vuccati rūpaṃ atītaṃ  ->  đó được gọi là vật chất thuộc quá khứ"""
    return f"{VUCCATI} {AGG[a]['noun']} {ATTR[key]}"


def khandha_question(a):
    """Tattha katamo rūpakkhandho?  ->  Ở đây, khối vật chất là gì?"""
    return f"{TATTHA} {AGG[a]['khandha']} là gì?"


def khandha_answer(a):
    """ayaṃ vuccati rūpakkhandho  ->  đó được gọi là khối vật chất"""
    return f"{VUCCATI} {AGG[a]['khandha']}"


# ---------------------------------------------------------------- 4. aggregate definition (Suttantabhājanīya)
# atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā yaṃ dūre santike vā
KHANDHA_SPAN = ("thuộc quá khứ, tương lai hay hiện tại, ở nơi bản thân hay ở bên ngoài bản thân, "
                "ở dạng thô hay ở dạng vi tế, thấp kém hay ưu việt, ở xa hay ở gần")
KHANDHA_TOGETHER = "khi gom tất cả lại làm một và thu tóm lại"   # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā


def khandha_def(a):
    return (f"{khandha_question(a)} {AGG[a]['any']}, {KHANDHA_SPAN}, {KHANDHA_TOGETHER} "
            f"{DASH} {khandha_answer(a)}.")


# past / future / present synonym strings, pi-1 ^1-1044 / ^1-1045 / ^1-1046 verbatim  [pi-1]
TIME = {
    "atita": ("thuộc quá khứ, đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn, "
              "đã mất đi sau khi sinh khởi, thuộc quá khứ, được gộp vào phần thuộc quá khứ"),
    "anagata": ("chưa sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra, "
                "chưa sinh khởi, chưa sinh khởi trọn vẹn, chưa trỗi dậy, chưa trỗi dậy trọn vẹn, thuộc tương lai, "
                "được gộp vào phần thuộc tương lai"),
    "paccuppanna": ("đã sinh ra, đã trở thành, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra, "
                    "đã sinh khởi, đã sinh khởi trọn vẹn, đã trỗi dậy, đã trỗi dậy trọn vẹn, thuộc hiện tại, "
                    "được gộp vào phần thuộc hiện tại"),
}

# tesaṃ tesaṃ (para)sattānaṃ (parapuggalānaṃ) ajjhattaṃ paccattaṃ niyaka pāṭipuggalika upādinna
# pi-1 ^1-1050 / ^1-1051 (Pāli there: niyatā «cố hữu»; pi-2 niyaka takes the same word)  [pi-1]
SELF = {
    "ajjhatta": "của từng chúng sinh, ở nơi bản thân, riêng từng người, cố hữu, thuộc về cá nhân, do nghiệp tạo ra",
    "bahiddha": ("của từng chúng sinh khác, từng người khác, ở nơi bản thân của họ, riêng từng người, cố hữu, "
                 "thuộc về cá nhân, do nghiệp tạo ra"),
}

# the members listed after the definition (after ":")
MAHABHUTA = "bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản"          # [pi-1 ^1-584]
FEELINGS3 = "cảm giác dễ chịu, cảm giác khó chịu, cảm giác không khó chịu cũng không dễ chịu"  # [pi-1 words]
DOORS = ("mắt", "tai", "mũi", "lưỡi", "thân", "ý")                                 # [pi-1; «ý» new with samphassa]


def six_born(noun):
    """cakkhusamphassajā X … manosamphassajā X  ->  X sinh từ sự tiếp xúc của mắt, …, X sinh từ sự tiếp xúc của ý"""
    return ", ".join(f"{noun} sinh từ sự tiếp xúc của {d}" for d in DOORS)


VINNANA6 = "thức qua mắt, thức qua tai, thức qua mũi, thức qua lưỡi, thức qua thân, ý thức"  # [pi-1 termbase]
MEMBERS = {
    "rupa": MAHABHUTA,
    "vedana": FEELINGS3,
    "sanna": six_born("tri giác"),
    "sankhara": six_born("chủ ý"),
    "vinnana": VINNANA6,
}


def time_line(a, key):
    """Tattha katamaṃ rūpaṃ atītaṃ? Yaṃ rūpaṃ atītaṃ … saṅgahitaṃ, <members> – idaṃ vuccati rūpaṃ atītaṃ."""
    return f"{question(a, key)} {cap(AGG[a]['noun'])} {TIME[key]}: {MEMBERS[a]} {DASH} {answer(a, key)}."


def self_line(a, key):
    """Tattha katamaṃ rūpaṃ ajjhattaṃ / bahiddhā? …"""
    return f"{question(a, key)} {cap(AGG[a]['noun'])} {SELF[key]}: {MEMBERS[a]} {DASH} {answer(a, key)}."


# ---------------------------------------------------------------- 5. rūpa-only Suttanta strings
EYE_TO_TOUCH = "Lĩnh vực mắt… lĩnh vực vật xúc chạm"                      # Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ  [pi-1 ^1-674]
FEMININITY_TO_FOOD = "Năng lực nữ tính… thức ăn trong vai trò dưỡng chất"  # Itthindriyaṃ…pe… kabaḷīkāro āhāro  [pi-1 ^1-675]
VAR_KABALIMKARO = "[khác chính tả (Sī., Syā.): kabaḷiṃkāro]"
FIVE_OBJECTS = "hình sắc, âm thanh, mùi, vị, vật xúc chạm"                 # rūpā saddā gandhā rasā phoṭṭhabbā  [pi-1 words]
HINA_BODY = ("mà đối với từng chúng sinh thì bị coi thường, bị xem nhẹ, bị chê bai, bị khinh miệt, không được quý trọng, "
             "thấp kém, được xem là thấp kém, được công nhận là thấp kém, không đáng mong muốn, không đáng yêu mến, "
             "không đáng ưa thích")
PANITA_BODY = ("mà đối với từng chúng sinh thì không bị coi thường, không bị xem nhẹ, không bị chê bai, không bị khinh miệt, "
               "được quý trọng, ưu việt, được xem là ưu việt, được công nhận là ưu việt, đáng mong muốn, đáng yêu mến, "
               "đáng ưa thích")
FAR_OTHER = "hoặc còn có bất cứ vật chất nào khác không gần kề, không cận kề, ở xa, không ở gần"   # yaṃ vā panaññampi atthi rūpaṃ anāsanne anupakaṭṭhe dūre asantike
NEAR_OTHER = "hoặc còn có bất cứ vật chất nào khác gần kề, cận kề, không xa, ở gần"                # … āsanne upakaṭṭhe avidūre santike


def tail(a, x, y):
    """Taṃ taṃ vā pana X upādāyupādāya X x y daṭṭhabbaṃ.
    ->  Hoặc nữa, so với X này hay X kia, X nên được xem là x hay y."""
    return f"Hoặc nữa, so với {AGG[a]['such']}, {AGG[a]['noun']} nên được xem là {ATTR[x]} hay {ATTR[y]}."


# ---------------------------------------------------------------- 6. comparison qualifiers (feeling … consciousness)
# Qualifiers follow the noun. Pair compounds (kusalābyākata, akusalābyākata, kusalākusala, sukhadukkha) take «các»
# before the noun; nowhere else is plural marked (saṅkhārā is always «các sự tạo tác», as in pi-1).
ADM = "không khó chịu cũng không dễ chịu"                     # adukkhamasukha  [pi-1 ^1-M1-2]
QUAL = {
    "akusala": "bất thiện", "kusala": "thiện", "abyakata": "không xác định về mặt đạo đức",   # [pi-1 core]
    "kusalabyakata": "thiện và không xác định về mặt đạo đức",
    "akusalabyakata": "bất thiện và không xác định về mặt đạo đức",
    "kusalakusala": "thiện và bất thiện",
    "dukkha": "khó chịu", "sukha": "dễ chịu", "adm": ADM, "sukhadukkha": "dễ chịu và khó chịu",  # vedanā only  [pi-1]
    "patigha": "sinh từ sự tiếp xúc có va chạm",               # paṭighasamphassajā (saññā only)  [new]
    "adhivacana": "sinh từ sự tiếp xúc qua tên gọi",           # adhivacanasamphassajā (saññā only)  [new]
    "asamapanna": "của người chưa chứng nhập",                 # asamāpannassa  [new]
    "samapanna": "của người đã chứng nhập",                    # samāpannassa  [pi-1 termbase]
    "sasava": "là đối tượng của ô nhiễm",                      # [pi-1]
    "anasava": "không phải là đối tượng của ô nhiễm",          # [pi-1]
}
PAIR_Q = {"kusalabyakata", "akusalabyakata", "kusalakusala", "sukhadukkha"}
FEEL = {  # objects of «gắn liền với» (sampayutta, pi-1)
    "dukkha": "cảm giác khó chịu",
    "sukha": "cảm giác dễ chịu",
    "adm": "cảm giác " + ADM,
    "sukha_adm": "cảm giác dễ chịu và cảm giác " + ADM,      # sukhāya ca adukkhamasukhāya ca vedanāhi
    "dukkha_adm": "cảm giác khó chịu và cảm giác " + ADM,    # dukkhāya ca adukkhamasukhāya ca vedanāhi
    "sukhadukkha": "các cảm giác dễ chịu và khó chịu",       # sukhadukkhāhi vedanāhi
}
SAMPAYUTTA = "gắn liền với"   # [pi-1 matrix]


def np(a, q):
    """Noun phrase of aggregate a with qualifier q (no case in Vietnamese)."""
    n = AGG[a]["noun"]
    if q in ("sukha_adm", "dukkha_adm"):  # vedanā only: sukhā ca adukkhamasukhā ca vedanā
        return FEEL[q]
    if q.startswith("sp_"):
        return f"{n} {SAMPAYUTTA} {FEEL[q[3:]]}"
    if q in PAIR_Q and not n.startswith("các "):
        return f"các {n} {QUAL[q]}"
    return f"{n} {QUAL[q]}"


PRED = {"olarika": "ở dạng thô", "sukhuma": "ở dạng vi tế", "hina": "thấp kém", "panita": "ưu việt",
        "dure": "ở xa", "santike": "ở gần"}
THI = "thì"   # topic marker before every predicate: «A thì ở dạng thô», «A thì ở xa B»


def clause(a, subj_q, pred, obj_q=None):
    out = f"{np(a, subj_q)} {THI} {PRED[pred]}"
    if obj_q is not None:
        out += " " + np(a, obj_q)
    return out


def comp_line(a, x, y, pairs):
    """Tattha katamā vedanā oḷārikā sukhumā? A oḷārikā, B sukhumā. … Taṃ taṃ vā pana … daṭṭhabbā."""
    sents = [cap(clause(a, s, x)) + ", " + clause(a, t, y) + "." for s, t in pairs]
    return f"{question_pair(a, x, y)} " + " ".join(sents) + " " + tail(a, x, y)


def relation_groups(a, rel, groups, ending):
    """groups: lists of (subj_q, obj_q); clauses in a group joined by '; ', groups end with '.'.
    ending: 'dash' -> last clause + ' – đó được gọi là ….'; 'sentence' -> '. Đó được gọi là ….'"""
    out = []
    for gi, grp in enumerate(groups):
        txt = cap("; ".join(clause(a, s, rel, o) for s, o in grp))
        if gi == len(groups) - 1 and ending == "dash":
            out.append(txt + " " + DASH + " " + answer(a, rel) + ".")
        else:
            out.append(txt + ".")
    if ending == "sentence":
        out.append(cap(answer(a, rel)) + ".")
    return f"{question(a, rel)} " + " ".join(out)


# ---------------------------------------------------------------- 7. classification frames (Abhidhammabhājanīya)
NUM = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín",
       10: "mười", 11: "mười một"}   # [pi-1 «theo nhóm N»]


def class_open(a, n):
    """Ekavidhena / Duvidhena … rūpakkhandho –  ->  Phân loại khối vật chất theo nhóm một –"""
    return f"Phân loại {AGG[a]['khandha']} theo nhóm {NUM[n]} {DASH}"


def class_close(a, n):
    """Evaṃ ekavidhena rūpakkhandho.  ->  Như vậy là phân loại khối vật chất theo nhóm một."""
    return f"Như vậy là phân loại {AGG[a]['khandha']} theo nhóm {NUM[n]}."


# rūpa lists, pi-1 ^1-584 … ^1-593 (first letter lowered after the dash)  [pi-1]
RUPA_EKAVIDHA = (
    "Toàn bộ vật chất không phải là gốc rễ; không có gốc rễ; không gắn liền với gốc rễ; có điều kiện; "
    "do điều kiện tạo thành; thuộc vật chất; thuộc thế gian; là đối tượng của ô nhiễm; là đối tượng của xiềng xích; "
    "là đối tượng của nút thắt; là đối tượng của dòng lũ; là đối tượng của ách; là đối tượng của chướng ngại; "
    "bị sự hiểu sai lệch nắm giữ; là đối tượng của sự bám víu; là đối tượng của phiền não; "
    "không xác định về mặt đạo đức; không có đối tượng; không phải là yếu tố đồng hành với tâm; không gắn liền với tâm; "
    "không phải là quả của nghiệp cũng không có khả năng sinh ra quả; "
    "không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não; "
    "không thuộc loại có sự hướng tâm và sự duy trì tâm; không thuộc loại không có sự hướng tâm, chỉ có sự duy trì tâm; "
    "không có sự hướng tâm cũng không có sự duy trì tâm; không có sự hân hoan đi kèm; không có hạnh phúc đi kèm; "
    "không có sự bình thản đi kèm; không cần dứt bỏ bằng sự thấy chân lý cũng không cần dứt bỏ bằng sự tu tập; "
    "không có gốc rễ nào cần dứt bỏ bằng sự thấy chân lý, cũng không có gốc rễ nào cần dứt bỏ bằng sự tu tập; "
    "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ; "
    "không thuộc về người còn đang tu học cũng không thuộc về người đã hoàn tất tu học; hạn hẹp; thuộc cõi dục lạc; "
    "không thuộc cõi hình sắc; không thuộc cõi không hình sắc; nằm trong các cõi tồn tại; "
    "không thuộc loại không nằm trong các cõi tồn tại; không cố định; không dẫn đến giải thoát; "
    "khi đã sinh khởi thì có thể được sáu loại thức nhận biết; là vô thường; bị sự lão hóa chế ngự")
EKAVIDHA_VAR_PI1 = " [dị bản (Sī.): rūpiyaṃ]"   # pi-1 only, after «thuộc vật chất»; not in the pi-2 Pāli

RUPA_DUKA = [  # pi-1 ^1-U1 (each a full sentence there)
    "Có loại vật chất phái sinh, có loại vật chất không phải là phái sinh.",
    "Có loại vật chất do nghiệp tạo ra, có loại vật chất không do nghiệp tạo ra.",
    "Có loại vật chất do nghiệp tạo ra và là đối tượng của sự bám víu, có loại vật chất không do nghiệp tạo ra nhưng là đối tượng của sự bám víu.",
    "Có loại vật chất thấy được, có loại vật chất không thấy được.",
    "Có loại vật chất có tính va chạm, có loại vật chất không có tính va chạm.",
    "Có loại vật chất là năng lực, có loại vật chất không phải là năng lực.",
    "Có loại vật chất là yếu tố cơ bản, có loại vật chất không phải là yếu tố cơ bản.",
    "Có loại vật chất là sự biểu lộ, có loại vật chất không phải là sự biểu lộ.",
    "Có loại vật chất do tâm sinh ra, có loại vật chất không do tâm sinh ra.",
    "Có loại vật chất cùng tồn tại với tâm, có loại vật chất không cùng tồn tại với tâm.",
    "Có loại vật chất vận hành theo tâm, có loại vật chất không vận hành theo tâm.",
    "Có loại vật chất thuộc phần bên trong, có loại vật chất thuộc phần bên ngoài.",
    "Có loại vật chất ở dạng thô, có loại vật chất ở dạng vi tế.",
    "Có loại vật chất ở xa, có loại vật chất ở gần.",
]
RUPA_DUKA_FOOD = ("Có loại vật chất là thức ăn trong vai trò dưỡng chất, "
                  "có loại vật chất không phải là thức ăn trong vai trò dưỡng chất.")
VAR_NUPADA = "[khác chính tả (Sī., Ka.): nupādā]"
RUPAKANDA_NOTE = "(Như đã phân tích trong phần về vật chất, ở đây cũng nên phân tích như vậy.)"  # (Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.)

RUPA_TIKA = [  # pi-1 ^1-585: (internal half, external half)
    ("Vật chất nào thuộc phần bên trong thì là phái sinh",
     "Vật chất nào thuộc phần bên ngoài thì có loại là phái sinh, có loại không phải là phái sinh"),
    ("Vật chất nào thuộc phần bên trong thì do nghiệp tạo ra",
     "Vật chất nào thuộc phần bên ngoài thì có loại do nghiệp tạo ra, có loại không do nghiệp tạo ra"),
    ("Vật chất nào thuộc phần bên trong thì do nghiệp tạo ra và là đối tượng của sự bám víu",
     "Vật chất nào thuộc phần bên ngoài thì có loại do nghiệp tạo ra và là đối tượng của sự bám víu, "
     "có loại không do nghiệp tạo ra nhưng là đối tượng của sự bám víu"),
]
RUPA_TIKA_FOOD = ("Vật chất nào thuộc phần bên trong thì không phải là thức ăn trong vai trò dưỡng chất",
                  "Vật chất nào thuộc phần bên ngoài thì có loại là thức ăn trong vai trò dưỡng chất, "
                  "có loại không phải là thức ăn trong vai trò dưỡng chất")
RUPA_CATU = [  # pi-1 ^1-586: (derived half, underived half)
    ("Vật chất nào là phái sinh thì có loại do nghiệp tạo ra, có loại không do nghiệp tạo ra",
     "Vật chất nào không phải là phái sinh thì có loại do nghiệp tạo ra, có loại không do nghiệp tạo ra"),
    ("Vật chất nào là phái sinh thì có loại do nghiệp tạo ra và là đối tượng của sự bám víu, "
     "có loại không do nghiệp tạo ra nhưng là đối tượng của sự bám víu",
     "Vật chất nào không phải là phái sinh thì có loại do nghiệp tạo ra và là đối tượng của sự bám víu, "
     "có loại không do nghiệp tạo ra nhưng là đối tượng của sự bám víu"),
    ("Vật chất nào là phái sinh thì có loại có tính va chạm, có loại không có tính va chạm",
     "Vật chất nào không phải là phái sinh thì có loại có tính va chạm, có loại không có tính va chạm"),
    ("Vật chất nào là phái sinh thì có loại ở dạng thô, có loại ở dạng vi tế",
     "Vật chất nào không phải là phái sinh thì có loại ở dạng thô, có loại ở dạng vi tế"),
    ("Vật chất nào là phái sinh thì có loại ở xa, có loại ở gần",
     "Vật chất nào không phải là phái sinh thì có loại ở xa, có loại ở gần"),
]
RUPA_SEEN = "Vật chất được thấy, được nghe, được cảm nhận, được nhận biết"   # diṭṭhaṃ, sutaṃ, mutaṃ, viññātaṃ rūpaṃ  [pi-1]
RUPA_PANCA = "Yếu tố đất, yếu tố nước, yếu tố lửa, yếu tố gió và loại vật chất phái sinh"
_K5 = ("Vật chất mà mắt có thể nhận biết, vật chất mà tai có thể nhận biết, vật chất mà mũi có thể nhận biết, "
       "vật chất mà lưỡi có thể nhận biết, vật chất mà thân có thể nhận biết")
RUPA_CHA = _K5 + ", vật chất mà ý có thể nhận biết"
RUPA_SATTA = _K5 + ", vật chất mà yếu tố ý có thể nhận biết, vật chất mà yếu tố ý thức có thể nhận biết"
RUPA_ATTHA = (_K5 + ": có loại khi tiếp xúc thì dễ chịu, có loại khi tiếp xúc thì khó chịu; "
              "vật chất mà yếu tố ý có thể nhận biết, vật chất mà yếu tố ý thức có thể nhận biết")
_IND8 = ("Năng lực mắt, năng lực tai, năng lực mũi, năng lực lưỡi, năng lực thân, năng lực nữ tính, "
         "năng lực nam tính, năng lực sống")
RUPA_NAVA = _IND8 + " và loại vật chất không phải là năng lực"
RUPA_DASA = _IND8 + ", vật chất không phải là năng lực: có loại có tính va chạm, có loại không có tính va chạm"
RUPA_EKADASA = ("Lĩnh vực mắt, lĩnh vực tai, lĩnh vực mũi, lĩnh vực lưỡi, lĩnh vực thân, lĩnh vực hình sắc, "
                "lĩnh vực âm thanh, lĩnh vực mùi, lĩnh vực vị, lĩnh vực vật xúc chạm và loại vật chất "
                "không thấy được và không có tính va chạm, nằm trong lĩnh vực đối tượng của ý")
EKADASA_VAR_PI1 = " [khác chính tả (Sī., Syā.): anidassanaṃ appaṭighaṃ]"   # pi-1 only; not in the pi-2 Pāli


def halves(pairs):
    """pi-1 'A. B.' sentence pairs -> 'A; b' (the Pāli joins the halves inside one sentence)."""
    return [f"{x}; {low(y)}" for x, y in pairs]


# ---------------------------------------------------------------- 8. the sample, line by line
FEEL_PAIRS = [("akusala", "kusalabyakata"), ("kusalakusala", "abyakata"), ("dukkha", "sukha_adm"),
              ("sukhadukkha", "adm"), ("asamapanna", "samapanna"), ("sasava", "anasava")]
SP_PAIRS = [("akusala", "kusalabyakata"), ("kusalakusala", "abyakata"), ("sp_dukkha", "sp_sukha_adm"),
            ("sp_sukhadukkha", "sp_adm"), ("asamapanna", "samapanna"), ("sasava", "anasava")]
G_ETH = [("akusala", "kusalabyakata"), ("kusalabyakata", "akusala"), ("kusala", "akusalabyakata"),
         ("akusalabyakata", "kusala"), ("abyakata", "kusalakusala"), ("kusalakusala", "abyakata")]
G_FEEL = [("dukkha", "sukha_adm"), ("sukha_adm", "dukkha"), ("sukha", "dukkha_adm"),
          ("dukkha_adm", "sukha"), ("adm", "sukhadukkha"), ("sukhadukkha", "adm")]
G_SP = [("sp_dukkha", "sp_sukha_adm"), ("sp_sukha_adm", "sp_dukkha"), ("sp_sukha", "sp_dukkha_adm"),
        ("sp_dukkha_adm", "sp_sukha"), ("sp_adm", "sp_sukhadukkha"), ("sp_sukhadukkha", "sp_adm")]
G_SAM = [("asamapanna", "samapanna"), ("samapanna", "asamapanna")]
G_SAS = [("sasava", "anasava"), ("anasava", "sasava")]
N_ETH = [("akusala", "akusala"), ("kusala", "kusala"), ("abyakata", "abyakata")]
N_FEEL = [("dukkha", "dukkha"), ("sukha", "sukha"), ("adm", "adm")]
N_SP = [("sp_dukkha", "sp_dukkha"), ("sp_sukha", "sp_sukha"), ("sp_adm", "sp_adm")]
N_SAM = [("asamapanna", "asamapanna"), ("samapanna", "samapanna")]
N_SAS = [("sasava", "sasava"), ("anasava", "anasava")]


def sample_lines():
    L = []
    add = L.append
    add("### " + CHAPTER_TITLES[1])
    add("#### " + SECTION_TITLES["Suttantabhājanīyaṃ"])
    add(FIVE_AGGREGATES + ".")
    # ---- rūpa
    a = "rupa"
    add("##### " + heading(a))
    add(khandha_def(a))
    for k in ("atita", "anagata", "paccuppanna"):
        add(time_line(a, k))
    for k in ("ajjhatta", "bahiddha"):
        add(self_line(a, k))
    add(f"{question(a, 'olarika')} {EYE_TO_TOUCH} {DASH} {answer(a, 'olarika')}.")
    add(f"{question(a, 'sukhuma')} {FEMININITY_TO_FOOD} {VAR_KABALIMKARO} {DASH} {answer(a, 'sukhuma')}.")
    add(f"{question(a, 'hina')} {cap(AGG[a]['noun'])} {HINA_BODY}: {FIVE_OBJECTS} {DASH} {answer(a, 'hina')}.")
    add(f"{question(a, 'panita')} {cap(AGG[a]['noun'])} {PANITA_BODY}: {FIVE_OBJECTS} {DASH} {answer(a, 'panita')}. "
        + tail(a, "hina", "panita"))
    add(f"{question(a, 'dure')} {FEMININITY_TO_FOOD}, {FAR_OTHER} {DASH} {answer(a, 'dure')}.")
    add(f"{question(a, 'santike')} {EYE_TO_TOUCH}, {NEAR_OTHER} {DASH} {answer(a, 'santike')}. "
        + tail(a, "dure", "santike"))

    # ---- vedanā … viññāṇa
    for a in ("vedana", "sanna", "sankhara", "vinnana"):
        add("##### " + heading(a))
        add(khandha_def(a))
        for k in ("atita", "anagata", "paccuppanna"):
            add(time_line(a, k))
        for k in ("ajjhatta", "bahiddha"):
            add(self_line(a, k))
        if a == "vedana":
            ol_pairs = hi_pairs = FEEL_PAIRS
            far_g, near_g = [G_ETH, G_FEEL, G_SAM, G_SAS], [N_ETH, N_FEEL, N_SAM, N_SAS]
        else:
            # saññā: the paṭigha/adhivacana pair stands only in the coarse/subtle line, not in inferior/superior
            ol_pairs = ([("patigha", "adhivacana")] if a == "sanna" else []) + SP_PAIRS
            hi_pairs = SP_PAIRS
            if a == "sanna":  # the Pāli closes a sentence after the fourth ethical clause
                far_g = [G_ETH[:4], G_ETH[4:], G_SP, G_SAM, G_SAS]
            else:
                far_g = [G_ETH, G_SP, G_SAM, G_SAS]
            near_g = [N_ETH, N_SP, N_SAM, N_SAS]
        add(comp_line(a, "olarika", "sukhuma", ol_pairs))
        add(comp_line(a, "hina", "panita", hi_pairs))
        far_end = "sentence" if a == "sankhara" else "dash"
        near_end = "dash" if a == "vinnana" else "sentence"
        add(relation_groups(a, "dure", far_g, far_end))
        add(relation_groups(a, "santike", near_g, near_end) + " " + tail(a, "dure", "santike"))
    add(SECTION_TITLES["Suttantabhājanīyaṃ"] + ".")

    # ---- Abhidhammabhājanīya
    add("#### " + SECTION_TITLES["Abhidhammabhājanīyaṃ"])
    add(FIVE_AGGREGATES + ".")
    a = "rupa"
    add("##### " + heading(a))
    add(f"{khandha_question(a)} {class_open(a, 1)} {low(RUPA_EKAVIDHA)}. {class_close(a, 1)}")
    duka = ([low(RUPA_DUKA[0][:-1]) + " " + VAR_NUPADA + "."] + RUPA_DUKA[1:-1]
            + [RUPA_DUKA[-1][:-1] + "… " + low(RUPA_DUKA_FOOD)])
    add(f"{class_open(a, 2)} " + " ".join(duka) + f" {class_close(a, 2)}")
    add(RUPAKANDA_NOTE)
    tika = low(". ".join(halves(RUPA_TIKA))) + "… " + low(halves([RUPA_TIKA_FOOD])[0]) + "."
    add(f"{class_open(a, 3)} {tika} {class_close(a, 3)}")
    catu = low(". ".join(halves(RUPA_CATU))) + "… " + low(RUPA_SEEN) + "."
    add(f"{class_open(a, 4)} {catu} {class_close(a, 4)}")
    for n, s in ((5, RUPA_PANCA), (6, RUPA_CHA), (7, RUPA_SATTA), (8, RUPA_ATTHA), (9, RUPA_NAVA),
                 (10, RUPA_DASA), (11, RUPA_EKADASA)):
        add(f"{class_open(a, n)} {low(s)}. {class_close(a, n)}")
    add(cap(khandha_answer(a)) + ".")
    return L


# ---------------------------------------------------------------- 9. checks against pi-1 and writing
def pi1_text():
    out = []
    for fn in sorted(os.listdir(PI1_VI_DIR)):
        if fn.endswith(".md"):
            out.append(open(os.path.join(PI1_VI_DIR, fn), encoding="utf-8").read())
    return "\n".join(out)


def assert_pi1():
    t = pi1_text()
    must = [HOMAGE, "# " + PITAKA, FIVE_AGGREGATES, TIME["atita"], TIME["anagata"], TIME["paccuppanna"],
            SELF["ajjhatta"], SELF["bahiddha"], cap(MAHABHUTA), EYE_TO_TOUCH, FEMININITY_TO_FOOD,
            "– đó được gọi là toàn bộ vật chất.", "Ở đây, toàn bộ vật chất là gì?",
            "cảm giác " + ADM, "gắn liền với cảm giác dễ chịu", "là đối tượng của ô nhiễm",
            "không phải là đối tượng của ô nhiễm", "người đã chứng nhập", "tri giác sinh từ sự tiếp xúc",
            "chủ ý sinh từ sự tiếp xúc", "sự tiếp xúc của mắt", "sự tiếp xúc của thân",
            "Phân loại vật chất theo nhóm hai –", "Như vậy là phân loại vật chất theo nhóm một.",
            "Phần về vật chất", "Ma trận đã hoàn tất.", "Phân tích từng từ.", "theo kinh",
            "có tính va chạm", "phạm vi của tên gọi", "ở dạng thô", "ở dạng vi tế", "thấp kém", "ưu việt",
            "thức qua mắt", "thức qua tai", "thức qua mũi", "thức qua lưỡi", "ý thức", "lĩnh vực âm thanh",
            RUPA_DUKA_FOOD, RUPA_SEEN + ".", RUPA_PANCA + ".", RUPA_CHA + ".", RUPA_SATTA + ".",
            RUPA_ATTHA + ".", RUPA_NAVA + ".", RUPA_DASA + ".",
            RUPA_EKADASA.replace("không có tính va chạm,", "không có tính va chạm" + EKADASA_VAR_PI1 + ",") + ".",
            RUPA_EKAVIDHA.replace("thuộc vật chất;", "thuộc vật chất" + EKAVIDHA_VAR_PI1 + ";") + "."]
    must += RUPA_DUKA
    must += [f"{x}. {y}." for x, y in RUPA_TIKA + [RUPA_TIKA_FOOD] + RUPA_CATU]
    missing = [m for m in must if m not in t]
    assert not missing, "pi-1 strings not found: " + " | ".join(m[:80] for m in missing)


def attach_ids(pali_lines, vi_lines):
    out, i = [], 0
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        vi = vi_lines[i]
        i += 1
        m = ID.search(pl)
        out.append(vi + (" " + m.group(1) if m else ""))
    assert i == len(vi_lines), (i, len(vi_lines))
    return out


def write(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip("\n") + "\n")


def build():
    """Returns {output path: list of lines}."""
    assert_pi1()
    pre_p = open(os.path.join(PALI_DIR, "preamble.md"), encoding="utf-8").read().rstrip("\n").split("\n")
    pre_vi = [HOMAGE, "# " + PITAKA, "## " + BOOK_TITLE]
    pali = open(os.path.join(HERE, "ch1-sample-pali.md"), encoding="utf-8").read().rstrip("\n").split("\n")
    vi = sample_lines()
    nonempty = [l for l in pali if l.strip()]
    assert len(vi) == len(nonempty), (len(vi), len(nonempty))
    for p, v in zip(nonempty, vi):  # dash count per line
        assert p.count(DASH) + p.count("—") == v.count(DASH) and "—" not in v, (p[:60], v[:60])
        assert "là là" not in v and "  " not in v, v[:80]
    return {os.path.join(VI_DIR, "preamble.md"): attach_ids(pre_p, pre_vi),
            os.path.join(HERE, "ch1-sample.md"): attach_ids(pali, vi)}


def main(argv):
    """no option: write the outputs; --print <n>: print output n (0 preamble, 1 sample) to stdout;
    --check: compare the outputs on disk with the build, byte for byte."""
    out = build()
    if argv[:1] == ["--print"]:
        path = list(out)[int(argv[1])]
        print("\n".join(out[path]).rstrip("\n"))
    elif argv[:1] == ["--check"]:
        for path, lines in out.items():
            want = "\n".join(lines).rstrip("\n") + "\n"
            have = open(path, "rb").read().decode("utf-8") if os.path.exists(path) else None
            print(path, "IDENTICAL" if have == want else "DIFFERS")
    else:
        for path, lines in out.items():
            write(path, lines)
        print("OK: preamble + ch1-sample.md,", len(sample_lines()), "non-empty lines")


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
