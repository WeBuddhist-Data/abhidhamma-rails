# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot SAMPLE builder: preamble.md and 1-mulayamaka.md.

The pair-question formulas of the whole book are module constants / helper functions. Chapter agents import
this module and use them VERBATIM:

    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    import build_sample_vi as S
    S.ka(x, y); S.kha(y, x); S.AMANTA; S.but_not(s, a, b); S.both(s, a, b); S.only(n, x); S.rest_not(x, y) ...

Slots (x, y, a, b, s) are passed lowercase, without final punctuation; the frames add the label, capitals,
the question words and the final punctuation. The Pāli of this chapter has no dash and no quote; the frames
add none (DASH RULE).

Chapter 1 is translated by a sentence parser (translate_line): every Pāli line is split into sentences and
each sentence must match one fixed frame, so the Vietnamese layout is always the Pāli layout. A sentence that
matches no frame stops the build.

Importing writes nothing; run  python -I -X utf8 -B build_sample_vi.py  to rebuild the two files.
At build time every string claimed from pi-1 … pi-5 (CROSS_BOOK) is asserted to occur in those rails files, and
every output line is checked against its Pāli line (IDs, dash count, quote count, "?" count, NFC, Latin letters).
"""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
OUT_DIR = ROOT / "AI_translation/vietnamese/pi-6-vietnamese-plain-zeroshot_split_chapters"
RAILS_DIR = {b: ROOT / f"AI_translation/vietnamese/pi-{b}-vietnamese-plain-rails_split_chapters" for b in (1, 2, 3, 4, 5)}


def cap(s):
    return s[:1].upper() + s[1:]


# ================================================================ book frame
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"   # Namo tassa … (pi-1..5 ^T-1)
PITAKA = "Tạng Vi Diệu Pháp"                                               # Abhidhammapiṭake (pi-1..5 ^0)
BOOK_TITLE = "Các cặp câu hỏi"                                             # Yamakapāḷi (new, proposed)
BOOK_TITLE_ALTERNATIVES = ("Các cặp đối xứng", "Các cặp vấn đề")
BOOK_END = f"Bộ “{BOOK_TITLE}” đã hoàn tất."                               # Yamakapakaraṇaṃ niṭṭhitaṃ (pi-1..5 frame)
YAMAKA = {                                                                 # ### <X>yamakaṃ (chapter titles)
    "Mūlayamakaṃ": "Các cặp câu hỏi về gốc rễ",
    "Khandhayamakaṃ": "Các cặp câu hỏi về các khối",
    "Āyatanayamakaṃ": "Các cặp câu hỏi về các lĩnh vực nhận biết",
    "Dhātuyamakaṃ": "Các cặp câu hỏi về các yếu tố",
    "Saccayamakaṃ": "Các cặp câu hỏi về các sự thật",
    "Saṅkhārayamakaṃ": "Các cặp câu hỏi về các tạo tác",
    "Anusayayamakaṃ": "Các cặp câu hỏi về các khuynh hướng tiềm ẩn",
    "Cittayamakaṃ": "Các cặp câu hỏi về tâm",
    "Dhammayamakaṃ": "Các cặp câu hỏi về các hiện tượng",
    "Indriyayamakaṃ": "Các cặp câu hỏi về các năng lực",
}
YAMAKA_END = "Phần {x} đã hoàn tất."      # <X>yamakapāḷi niṭṭhitā. (x = YAMAKA title, first letter lowercase)


def yamaka_end(pali_title):
    t = YAMAKA[pali_title]
    return YAMAKA_END.format(x=t[:1].lower() + t[1:])


NITTHITA = "đã hoàn tất"                  # niṭṭhito / niṭṭhitā (pi-1)

# ================================================================ section headings (heading text, no final ".")
# Vietnamese alphabet order (no f / j / w / z): a b c d đ e g h (coordinator, 2026-11-22)
LABEL = {"Ka": "(a)", "Kha": "(b)", "Ga": "(c)", "Gha": "(d)", "Ṅa": "(đ)", "Ca": "(e)", "Cha": "(g)", "Ja": "(h)"}
UDDESO = "Phần nêu đề mục"                # (Ka) uddeso (pi-3 Uddeso)
NIDDESO = "Phần giải thích"               # (Kha) niddeso (pi-4 Niddeso)
VARO = "Mục về {x}"                       # <X>vāro (pi-1 / pi-2 vāro «Mục»: Hetuvāro «Mục về nguyên nhân»)
UDDESAVARO = "Mục nêu đề mục"             # Uddesavāro
NIDDESAVARO = "Mục giải thích"            # Niddesavāro
VARA_UDDESO = "Phần nêu đề mục của {v}"   # <X>vārauddeso. (v = VARO lowercased)
VARA_NIDDESO = "Phần giải thích của {v}"  # <X>vāraniddeso / <X>vāraniddesa
ADI = "{x} và các mục khác"               # <X>ādi (ādi «mục khác», pi-3)
NAYO = "Phương pháp về {x}"               # <X>nayo (naya «phương pháp», pi-3)
MULAVARO = VARO.format(x="gốc rễ")        # Mūlavāro
HETUVARADI = ADI.format(x=VARO.format(x="nguyên nhân"))   # Hetuvārādi
MULANAYO = {1: NAYO.format(x="gốc rễ"),                        # Mūlanayo
            2: NAYO.format(x="cội rễ"),                        # Mūlamūlanayo
            3: NAYO.format(x="sự bắt nguồn từ gốc rễ"),        # Mūlakanayo
            4: NAYO.format(x="sự bắt nguồn từ cội rễ")}        # Mūlamūlakanayo
UDDESAVARO_END = f"{UDDESAVARO} {NITTHITA}."    # Uddesavāro niṭṭhito.
NIDDESAVARO_END = f"{NIDDESAVARO} {NITTHITA}."  # Niddesavāro niṭṭhito.


def low(s):
    return s[:1].lower() + s[1:]


# proposed recurring headings of the later chapters (agents use them verbatim)
SECTION = {
    "Paṇṇattivāro": VARO.format(x="sự định danh"),
    "Paṇṇattivāraniddesa": VARA_NIDDESO.format(v=low(VARO.format(x="sự định danh"))),
    "Padasodhanavāro": VARO.format(x="sự làm sáng tỏ thuật ngữ"),
    "Padasodhanamūlacakkavāro": VARO.format(x="vòng luân chuyển dựa trên sự làm sáng tỏ thuật ngữ"),
    "Suddhakhandhavāro": VARO.format(x="các khối thuần túy"),
    "Suddhakhandhamūlacakkavāro": VARO.format(x="vòng luân chuyển dựa trên các khối thuần túy"),
    "Suddhindriyamūlacakkavāro": VARO.format(x="vòng luân chuyển dựa trên các năng lực thuần túy"),
    "anulomaṃ": "Chiều thuận", "paccanīkaṃ": "Chiều nghịch",
    "Pavattivāro": VARO.format(x="sự diễn tiến"), "Pavatti": "Sự diễn tiến",
    "uppādavāro": low(VARO.format(x="sự sinh khởi")), "nirodhavāro": low(VARO.format(x="sự chấm dứt")),
    "Uppādanirodhavāro": VARO.format(x="sự sinh khởi và sự chấm dứt"),
    "Paccuppannavāro": VARO.format(x="hiện tại"), "Atītavāro": VARO.format(x="quá khứ"),
    "Anāgatavāro": VARO.format(x="tương lai"), "Paccuppannātītavāro": VARO.format(x="hiện tại và quá khứ"),
    "Paccuppannānāgatavāro": VARO.format(x="hiện tại và tương lai"),
    "Atītānāgatavāro": VARO.format(x="quá khứ và tương lai"),
    "anulomapuggalo": "Chiều thuận theo người", "anulomaokāso": "Chiều thuận theo nơi chốn",
    "anulomapuggalokāsā": "Chiều thuận theo người và nơi chốn",
    "paccanīkapuggalo": "Chiều nghịch theo người", "paccanīkaokāso": "Chiều nghịch theo nơi chốn",
    "paccanīkapuggalokāsā": "Chiều nghịch theo người và nơi chốn",
    "paṭilomapuggalo": "Chiều ngược theo người", "paṭilomaokāso": "Chiều ngược theo nơi chốn",
    "paṭilomapuggalokāsā": "Chiều ngược theo người và nơi chốn",
    "Pariññāvāro": VARO.format(x="sự hiểu biết trọn vẹn"),
    "Uppattiṭṭhānavāro": VARO.format(x="nơi sinh khởi"),
    "Mahāvāro": "Mục lớn", "anusayavāro": low(VARO.format(x="khuynh hướng tiềm ẩn")),
    "Anusayavāra": VARO.format(x="khuynh hướng tiềm ẩn"),
    "Sānusayavāro": VARO.format(x="sự có khuynh hướng tiềm ẩn"),
    "Pajahanavāro": VARO.format(x="sự dứt bỏ"),
    "Pahīnavāro": VARO.format(x="những gì đã được dứt bỏ"),
    "dhātuvisajjanāvāro": "Mục trả lời theo các yếu tố",
}

# ================================================================ categories (the kusala triad and nāma)
# adj: compound member / attribute; pred: predicate after «Bất cứ hiện tượng nào …» and «… đều …»;
# noun: the bare neuter (kusalaṃ, nāmaṃ); neg: «na kusalaṃ» = «nhưng <neg>»; head: section heading.
CAT = {
    "kusala": dict(adj="thiện", pred="là thiện", noun="hiện tượng thiện", neg="không phải là thiện"),
    "akusala": dict(adj="bất thiện", pred="là bất thiện", noun="hiện tượng bất thiện", neg="không phải là bất thiện"),
    "abyākata": dict(adj="không xác định về mặt đạo đức", pred="không xác định về mặt đạo đức",
                     noun="hiện tượng không xác định về mặt đạo đức",
                     neg="không phải là không xác định về mặt đạo đức"),
    "nāma": dict(adj="thuộc phần tinh thần", pred="thuộc phần tinh thần", noun="phần tinh thần",
                 neg="không thuộc phần tinh thần"),
}
for _k, _v in CAT.items():
    _v["head"] = f"Các hiện tượng {_v['adj']}"          # Kusalā dhammā (pi-1 matrix «Các hiện tượng thiện»)
    _v["root"] = f"gốc rễ {_v['adj']}"                  # kusalamūla (pi-1 «gốc rễ thiện»)
NUM = {"Tīṇ": "ba", "Nav": "chín", "Tay": "ba"}         # Tīṇeva / Naveva / Tayo eva

# ================================================================ the four methods (naya 1-4)
# suffix of the compound -> naya: mūla 1, mūlamūla 2, mūlaka 3, mūlamūlaka 4
ROOT_NOUN = {1: "gốc rễ", 2: "cội rễ"}                                       # kusalamūlāni / kusalamūlamūlāni
Y_ROOT = {1: "là gốc rễ {a}", 2: "là cội rễ {a}",                            # kusalamūlā / kusalamūlamūlā
          3: "bắt nguồn từ gốc rễ {a}", 4: "bắt nguồn từ cội rễ {a}"}          # kusalamūlakā / kusalamūlamūlakā
Y_ROOT_NEG = {1: "không phải là gốc rễ {a}", 2: "không phải là cội rễ {a}",   # na kusalamūlā …
              3: "không bắt nguồn từ gốc rễ {a}", 4: "không bắt nguồn từ cội rễ {a}"}
EKA = {1: "có cùng một gốc rễ", 2: "có cùng một cội rễ",                       # ekamūla / ekamūlamūla
       3: "bắt nguồn từ cùng một gốc rễ", 4: "bắt nguồn từ cùng một cội rễ"}    # ekamūlaka / ekamūlamūlaka
ANNA = {1: "làm gốc rễ cho nhau", 2: "làm cội rễ cho nhau",                    # aññamaññamūla / -mūlamūla
        3: "bắt nguồn từ gốc rễ của nhau", 4: "bắt nguồn từ cội rễ của nhau"}  # aññamaññamūlaka / -mūlamūlaka
INSTR = "xét theo {r}"                                                         # kusalamūlena = xét theo gốc rễ thiện
NEG = "không {x}"                                                              # na ekamūla… / na ca aññamañña…

# ================================================================ answers and question frames
AMANTA = "Đúng vậy."                                          # Āmantā. (pi-5)
KA_Q = "Bất cứ hiện tượng nào {x}, có phải tất cả chúng đều {y} không?"          # ye keci X dhammā, sabbe te Y(ti)?
KHA_Q = "Còn bất cứ gì {y}, có phải tất cả các hiện tượng ấy đều {x} không?"     # ye vā pana Y, sabbe te dhammā X(ti)?
KA_PE = "Bất cứ hiện tượng nào {x}, có phải tất cả chúng đều {y}"                # ye keci X dhammā, sabbe te Y…pe… (no ?)
ONLY = "Chỉ có {n} {x}."                                       # Tīṇeva / Naveva X. (pi-5 «chỉ có ba»)
ONLY_COMMA = "Chỉ có {n} {x},"                                 # Tayo eva X, …
REST_NOT = "Các hiện tượng {a} còn lại {y}."                   # Avasesā X dhammā na Y.
BUT_NOT = "{s} thì {a}, nhưng {b}."                            # S A(,) na B.   (partial answer: which are not)
BOTH = "{s} thì vừa {a} vừa {b}."                              # S Añceva Bañca. (pi-1 «vừa … vừa …»)
AHETUKA = "{s} mà không có gốc rễ thì {y}."                    # Ahetukaṃ S Y. (ahetuka «không có gốc rễ», pi-1)
SAHETUKA = "{s} mà có gốc rễ thì {y}."                         # Sahetukaṃ S Y. (sahetuka «có gốc rễ», pi-1)
SAMUTTHANA = "vật chất do {x} sinh ra"                         # Xsamuṭṭhānaṃ rūpaṃ (pi-1 «vật chất do tâm sinh ra»)
TOGETHER = "Những gốc rễ nào cùng sinh khởi thì những {r} ấy vừa {a} vừa {b}."
# Mūlāni yāni ekato uppajjanti Xmūlāni A ceva B ca. (ekato uppajjanti «cùng sinh khởi», pi-1)
REST_CONASCENT = "Các hiện tượng còn lại cùng sinh với {r} thì {a}, nhưng {b}."
# Avasesā Xmūlasahajātā dhammā A(,) na ca B. (sahajāta «cùng sinh», pi-2 / pi-5)


def ka(x, y, label="Ka"):
    return f"{LABEL[label]} {KA_Q.format(x=x, y=y)}" if label else cap(KA_Q.format(x=x, y=y))


def kha(y, x, label="Kha"):
    return f"{LABEL[label]} {KHA_Q.format(x=x, y=y)}" if label else cap(KHA_Q.format(x=x, y=y))


def only(n, x):
    return ONLY.format(n=n, x=x)


def rest_not(a, y):
    return REST_NOT.format(a=a, y=y)


def but_not(s, a, b):
    return BUT_NOT.format(s=cap(s), a=a, b=b)


def both(s, a, b):
    return BOTH.format(s=cap(s), a=a, b=b)


# ================================================================ the ten terms of the hetuvāra series
# = pi-5 ^5 13-pancamavaggo (mūlato … samudayato jānāti): hetu here «nguyên nhân» (pi-2 Hetuvāro «Mục về nguyên
# nhân»), kept apart from mūla «gốc rễ» in this series.
TEN = ["gốc rễ", "nguyên nhân", "căn nguyên", "sự hình thành", "sự khởi nguồn", "nguồn gốc", "dưỡng chất",
       "đối tượng", "điều kiện", "sự phát sinh"]
# mūla hetu nidāna sambhava pabhava samuṭṭhāna āhāra ārammaṇa paccaya samudaya
HETU_SERIES = TEN[1:]
VAR = "dị bản"                            # word / form variant label (pi-1..5)
SPELL = "khác chính tả"                   # spelling-only variant label (pi-1..5)
VERSE_1 = f"{cap(TEN[0])}, {TEN[1]} và {TEN[2]}, {TEN[3]} cùng với {TEN[4]};"
# Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;
VERSE_2 = f"{cap(TEN[5])}, {TEN[6]}, {TEN[7]}{{v}}, {TEN[8]} cùng với {TEN[9]}."
# Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.


def series(cat, items=HETU_SERIES):
    a = CAT[cat]["adj"]
    return "… ".join(f"{t} {a}" for t in items) + "…"


# ================================================================ phrase parser (Pāli predicate -> Vietnamese)
CAT_RE = "akusala|kusala|abyākata|nāma"
SUF_RE = "mūlamūlak|mūlamūl|mūlak|mūl"
END_RE = "āni|ā|aṃ"
NAYA = {"mūl": 1, "mūlamūl": 2, "mūlak": 3, "mūlamūlak": 4}
CATPL = {"kusalā": "kusala", "akusalā": "akusala", "abyākatā": "abyākata", "nāmā": "nāma"}
CATSG = {"kusalaṃ": "kusala", "akusalaṃ": "akusala", "abyākataṃ": "abyākata", "nāmaṃ": "nāma"}


def P(s):
    """Translate one Pāli predicate phrase of this chapter (plural, singular or neuter plural; optional «na»)."""
    s = s.strip()
    neg = False
    if s.startswith("na "):
        neg, s = True, s[3:]
    if s in CATPL or s in CATSG:
        c = CATPL.get(s) or CATSG[s]
        return CAT[c]["neg"] if neg else CAT[c]["pred"]
    m = re.fullmatch(rf"(?P<c>{CAT_RE})mūlena (?P<n2>na )?(?P<k>eka|aññamañña)(?P<s>{SUF_RE})(?:{END_RE})", s)
    if m:
        n = NAYA[m["s"]]
        core = (EKA if m["k"] == "eka" else ANNA)[n]
        if neg or m["n2"]:
            core = NEG.format(x=core)
        return f"{core} {INSTR.format(r=CAT[m['c']]['root'])}"
    m = re.fullmatch(rf"(?P<k>eka|aññamañña)(?P<s>{SUF_RE})(?:{END_RE})", s)
    if m:
        core = (EKA if m["k"] == "eka" else ANNA)[NAYA[m["s"]]]
        return NEG.format(x=core) if neg else core
    m = re.fullmatch(rf"(?P<c>{CAT_RE})(?P<s>{SUF_RE})(?:{END_RE})", s)
    if m:
        frame = (Y_ROOT_NEG if neg else Y_ROOT)[NAYA[m["s"]]]
        return frame.format(a=CAT[m["c"]]["adj"])
    raise ValueError(f"unparsed predicate: {s!r}")


# ================================================================ sentence frames (Pāli regex -> Vietnamese)
def _cat_of_cap(w):
    return w[:1].lower() + w[1:]


SENTENCES = [
    (rf"\((?P<l>Ka)\) ye keci (?P<x>.+?)(?: dhammā)?, sabbe te (?P<y>.+?)(?:ti)?\?",
     lambda m: ka(P(m["x"]), P(m["y"]), m["l"])),
    (rf"\((?P<l>Kha)\) ye vā pana (?P<y>.+?), sabbe te dhammā (?P<x>.+?)(?:ti)?\?",
     lambda m: kha(P(m["y"]), P(m["x"]), m["l"])),
    (rf"(?P<n>Tīṇ|Nav)eva (?P<c>{CAT_RE})(?P<s>mūlamūl|mūl)āni\.",
     lambda m: only(NUM[m["n"]], f"{ROOT_NOUN[NAYA[m['s']]]} {CAT[m['c']]['adj']}")),
    (rf"Avasesā (?P<c>kusalā|akusalā|abyākatā|nāmā) dhammā (?P<y>na .+)\.",
     lambda m: rest_not(CAT[CATPL[m["c"]]]["adj"], P(m["y"]))),
    (rf"(?P<C>Akusala|Kusala|Abyākata|Nāma)samuṭṭhānaṃ rūpaṃ (?P<y>.+?),? (?P<n>na \S+aṃ)\.",
     lambda m: but_not(SAMUTTHANA.format(x=CAT[_cat_of_cap(m["C"])]["noun"]), P(m["y"]), P(m["n"]))),
    (rf"(?P<C>Akusala|Kusala|Abyākata|Nāma)ṃ (?P<y>.+?)ñceva (?P<c2>\S+)ñca\.",
     lambda m: both(CAT[_cat_of_cap(m["C"])]["noun"], P(m["y"] + "ṃ"), P(m["c2"] + "ṃ"))),
    (rf"(?P<h>Ahetukaṃ|Sahetukaṃ) (?P<c>akusalaṃ|kusalaṃ|abyākataṃ|nāmaṃ) (?P<y>.+)\.",
     lambda m: (AHETUKA if m["h"] == "Ahetukaṃ" else SAHETUKA).format(s=cap(CAT[CATSG[m["c"]]]["noun"]),
                                                                      y=P(m["y"]))),
    (rf"Mūlāni yāni ekato uppajjanti (?P<c>{CAT_RE})mūlāni (?P<a>\S+) ceva (?P<b>\S+) ca\.",
     lambda m: TOGETHER.format(r=CAT[m["c"]]["root"], a=P(m["a"]), b=P(m["b"]))),
    (rf"Avasesā (?P<c>{CAT_RE})mūlasahajātā dhammā (?P<a>.+?),? na ca (?P<b>\S+)\.",
     lambda m: REST_CONASCENT.format(r=CAT[m["c"]]["root"], a=P(m["a"]), b=P("na " + m["b"]))),
    (r"Āmantā\.", lambda m: AMANTA),
]
SENTENCES = [(re.compile(p), f) for p, f in SENTENCES]


def translate_sentence(s):
    for rx, f in SENTENCES:
        m = rx.fullmatch(s)
        if m:
            return f(m)
    raise ValueError(f"unmatched sentence: {s!r}")


def heading_cat_naya(text):
    """Kusalā dhammā / (1) Mūlanayo / Akusalā dhammā (1) mūlanayo / ##### (2) Mūlamūlanayo …"""
    m = re.fullmatch(r"(?:(?P<c>Kusalā|Akusalā|Abyākatā|Nāmā) dhammā)? ?(?:\((?P<n>[1-4])\) (?P<w>\S+))?", text)
    if not m or not (m["c"] or m["n"]):
        return None
    parts = []
    if m["c"]:
        parts.append(CAT[CATPL[_cat_of_cap(m["c"])]]["head"])
    if m["n"]:
        naya = {"mūlanayo": 1, "mūlamūlanayo": 2, "mūlakanayo": 3, "mūlamūlakanayo": 4}[m["w"].lower()]
        h = MULANAYO[naya]
        parts.append(f"({m['n']}) {h if m['w'][0].isupper() else low(h)}")
    return " ".join(parts)


# exact lines (headings without #, closing lines, the hetuvāra lines and the verse)
EXACT = {
    "Mūlayamakaṃ": YAMAKA["Mūlayamakaṃ"],
    "(Ka) uddeso": f"{LABEL['Ka']} {UDDESO}",
    "(Kha) niddeso": f"{LABEL['Kha']} {NIDDESO}",
    "Mūlavāro": MULAVARO,
    "2-10. Hetuvārādi": f"2-10. {HETUVARADI}",
    "Mūlavārauddeso.": VARA_UDDESO.format(v=low(MULAVARO)) + ".",
    "Mūlavāraniddeso.": VARA_NIDDESO.format(v=low(MULAVARO)) + ".",
    "Uddesavāro niṭṭhito.": UDDESAVARO_END,
    "Niddesavāro niṭṭhito.": NIDDESAVARO_END,
    "Mūlayamakapāḷi niṭṭhitā.": yamaka_end("Mūlayamakaṃ"),
    "Namo tassa bhagavato arahato sammāsambuddhassa": HOMAGE,
    "Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;": VERSE_1,
    "Samuṭṭhānāhārārammaṇā [samuṭṭhānāhārārammaṇaṃ (ka.)], paccayo samudayena cāti.":
        VERSE_2.format(v=f" [{VAR} (Ka.): samuṭṭhānāhārārammaṇaṃ]"),
    "Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.": VERSE_2.format(v=""),
    # ^6-1-49 (uddesa): Ye keci kusalā dhammā, sabbe te kusalahetū…pe… kusalanidānā…pe… … kusalasamudayā…pe….
    ("Ye keci kusalā dhammā, sabbe te kusalahetū…pe… kusalanidānā…pe… kusalasambhavā…pe… kusalappabhavā…pe… "
     "kusalasamuṭṭhānā…pe… kusalāhārā…pe… kusalārammaṇā…pe… kusalapaccayā…pe… kusalasamudayā…pe…."):
        KA_PE.format(x=CAT["kusala"]["pred"], y="là " + series("kusala")),
    # ^6-1-98 (niddesa)
    "Ye keci kusalā dhammā, sabbe te kusalahetūti…?":
        KA_Q.format(x=CAT["kusala"]["pred"], y=f"là {HETU_SERIES[0]} {CAT['kusala']['adj']}…"),
    ("Tayo eva kusalahetū, avasesā kusalā dhammā na kusalahetū…pe… kusalanidānā… kusalasambhavā… "
     "kusalappabhavā… kusalasamuṭṭhānā… kusalāhārā… kusalārammaṇā… kusalapaccayā… kusalasamudayā…."):
        ONLY_COMMA.format(n="ba", x=f"{HETU_SERIES[0]} {CAT['kusala']['adj']}") + " "
        + low(REST_NOT.format(a=CAT["kusala"]["adj"],
                              y=f"không phải là {series('kusala')}")).rstrip("."),
    # ^6-1-99 (niddesa)
    ("Ye keci akusalā dhammā… ye keci abyākatā dhammā… ye keci nāmā dhammā, sabbe te nāmahetū ti… nāmanidānā… "
     "nāmasambhavā… nāmappabhavā… nāmasamuṭṭhānā… nāmāhārā… nāmārammaṇā… nāmapaccayā… nāmasamudayā…."):
        "… ".join(f"{'Bất cứ' if i == 0 else 'bất cứ'} hiện tượng nào {CAT[c]['pred']}"
                  for i, c in enumerate(("akusala", "abyākata")))
        + "… " + low(KA_PE.format(x=CAT["nāma"]["pred"], y="là " + series("nāma"))),
}


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if t in EXACT:
        return h + EXACT[t] + sid
    if h:
        v = heading_cat_naya(t)
        if v is None:
            raise ValueError(f"unmatched heading: {line!r}")
        return h + v + sid
    sents = re.split(r"(?<=[?.])\s+(?=\S)", t)
    return h + " ".join(translate_sentence(s) for s in sents) + sid


def translate_file(name):
    src = (PALI_DIR / name).read_text(encoding="utf-8")
    out = []
    for line in src.splitlines():
        out.append(translate_line(line) if line.strip() else "")
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def build_preamble():
    return (f"{HOMAGE} ^T-1\n\n# {PITAKA} ^0\n\n## {BOOK_TITLE} ^6-0\n")


def build_ch1():
    return translate_file("1-mulayamaka.md")


# ================================================================ cross-book asserts
TEN_PI5 = ("xét theo gốc rễ, biết xét theo nguyên nhân, biết xét theo căn nguyên, biết xét theo sự hình thành, "
           "biết xét theo sự khởi nguồn, biết xét theo nguồn gốc, biết xét theo dưỡng chất, biết xét theo đối tượng, "
           "biết xét theo điều kiện, biết xét theo sự phát sinh")
CROSS_BOOK = [
    (HOMAGE, 1), (PITAKA, 1), (HOMAGE, 5), (PITAKA, 5),
    ("Các hiện tượng thiện", 1), ("Các hiện tượng bất thiện", 1),
    ("Các hiện tượng không xác định về mặt đạo đức", 1), ("Phần tinh thần", 1), ("phần tinh thần", 1),
    ("Ba gốc rễ thiện", 1), ("ba gốc rễ bất thiện", 1), ("ba gốc rễ không xác định về mặt đạo đức", 1),
    ("chín gốc rễ", 1), ("Ba gốc rễ bất thiện", 2),
    ("vật chất do tâm sinh ra", 1), ("Vật chất nào do tâm sinh ra", 1),
    ("Những gốc rễ cùng sinh khởi", 1), ("vừa là gốc rễ vừa có gốc rễ", 1),
    ("Các hiện tượng có gốc rễ", 1), ("không có gốc rễ", 1), ("có loại có gốc rễ, có loại không có gốc rễ", 2),
    ("các hiện tượng thiện, bất thiện và không xác định về mặt đạo đức còn lại", 1),
    ("các hiện tượng cùng sinh", 5), ("cùng sinh", 2), ("bắt nguồn từ khao khát", 2),
    ("Đúng vậy.", 5), ("chỉ có ba", 5), (TEN_PI5, 5), ("Mục về nguyên nhân", 2), ("Mục về", 1),
    ("Phần nêu đề mục", 3), ("Phương pháp thứ", 3), ("Phần giải thích", 4), ("mục khác", 3), ("đã hoàn tất", 1),
    ("Ma trận đã hoàn tất.", 1), ("Bộ “Các vấn đề tranh luận” đã hoàn tất.", 5),
    ("dị bản", 1), ("khác chính tả", 1),
    # book / chapter / section vocabulary used in the proposed headings
    ("khối", 1), ("lĩnh vực nhận biết", 1), ("yếu tố", 1), ("sự thật", 1), ("các tạo tác", 5),
    ("khuynh hướng tiềm ẩn", 2), ("tâm", 1), ("hiện tượng", 1), ("năng lực", 1),
    ("sự định danh", 4), ("sự làm sáng tỏ thuật ngữ", 5), ("thuần túy", 5), ("chiều thuận", 5), ("chiều nghịch", 5),
    ("sự sinh khởi", 1), ("sự chấm dứt", 1), ("hiểu biết trọn vẹn", 2), ("nơi chốn", 5),
    ("hiện tại", 5), ("quá khứ", 5), ("tương lai", 5), ("đã được dứt bỏ", 4), ("dứt bỏ", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))) for b, d in RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts: {len(CROSS_BOOK)} strings found in pi-1..5 rails")


# ================================================================ line checks against the Pāli
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def _strip(line):
    return ID.sub("", re.sub(r"\[[^\]]*\]", "", line))


def check_lines(pali_text, vi_text, name):
    pl = [l for l in pali_text.splitlines() if l.strip()]
    vl = [l for l in vi_text.splitlines() if l.strip()]
    probs = []
    if len(pl) != len(vl):
        probs.append(f"{name}: line count {len(pl)} vs {len(vl)}")
    for i, (p, v) in enumerate(zip(pl, vl), 1):
        pid, vid = re.search(r"\^([0-9A-Za-z-]+)\s*$", p), re.search(r"\^([0-9A-Za-z-]+)\s*$", v)
        if (pid and pid.group(1)) != (vid and vid.group(1)):
            probs.append(f"{name} line {i}: ID {pid and pid.group(1)} vs {vid and vid.group(1)}")
        if (p.count("–") + p.count("—")) != (v.count("–") + v.count("—")):
            probs.append(f"{name} line {i}: dash count differs")
        sp, sv = _strip(p), _strip(v)
        qp = (sp.count('"') + sp.count("“") + sp.count("”"), sp.count("‘") + sp.count("’"))
        qv = (sv.count("“") + sv.count("”"), sv.count("‘") + sv.count("’"))
        if qp != qv:
            probs.append(f"{name} line {i}: quotes pali {qp} vs vi {qv}")
        if sp.count("?") != sv.count("?"):
            probs.append(f"{name} line {i}: '?' count {sp.count('?')} vs {sv.count('?')}")
        if p.startswith("#") != v.startswith("#") or (p.split(" ")[0] if p.startswith("#") else "") != \
                (v.split(" ")[0] if v.startswith("#") else ""):
            probs.append(f"{name} line {i}: heading level differs")
        if FOREIGN.search(sv):
            probs.append(f"{name} line {i}: foreign letter {FOREIGN.search(sv).group(0)!r}")
        if any(s in v for s in ("là là", ". .", "….", ".…", "?…", ",…", "  ", ":-", '"', "'", " ,", " .", "—")):
            probs.append(f"{name} line {i}: bad sequence")
        if v != unicodedata.normalize("NFC", v):
            probs.append(f"{name} line {i}: not NFC")
    return probs


def main():
    check_cross_book()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    allprobs = []
    for name, builder in (("preamble.md", build_preamble), ("1-mulayamaka.md", build_ch1)):
        text = unicodedata.normalize("NFC", builder())
        allprobs += check_lines((PALI_DIR / name).read_text(encoding="utf-8"), text, name)
        with open(OUT_DIR / name, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
        print(f"wrote {name}: {len([l for l in text.splitlines() if l.strip()])} lines, {segs} segments")
    for p in allprobs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not allprobs else f"{len(allprobs)} problems")
    sys.exit(1 if allprobs else 0)


if __name__ == "__main__":
    main()
