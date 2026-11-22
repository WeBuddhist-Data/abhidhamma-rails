"""pi-6 Yamaka, Vietnamese plain RAILS: sample builder (preamble + 1-mulayamaka) and the shared formula module.

Later chapter agents IMPORT this file for its fixed strings and slot helpers (LABEL, HOMAGE, H_ABHI, H_BOOK,
yamaka_title, yamaka_end, BOOK_END, NITTHITO, LATER_HEADINGS, qa / qb, pred, neg, YES, only, rest_not,
samutthana, both, hetuka, roots_together, rest_conascent, SERIES, series, VERSE …) and its checks
(dash_ok, quotes_ok, nfc_ok, check_against_pali, write). Importing does not rewrite anything: the outputs are
written only under `if __name__ == "__main__":`.

usage: python -I -X utf8 -B build_rails_sample_vi.py
"""
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
OUT_DIR = ROOT / "AI_translation/vietnamese/pi-6-vietnamese-plain-rails_split_chapters"
FORMULAS_MD = ROOT / "0-INBOX/temp/pipeline/pi-6-vi-ai/rails/vi-rails-formulas.md"
RAILS = {b: ROOT / f"AI_translation/vietnamese/pi-{b}-vietnamese-plain-rails_split_chapters" for b in "12345"}


def cap(s):
    return s[:1].upper() + s[1:]


# ---------------------------------------------------------------------------------------------------------------
# Book frame, yamaka titles, labels
# ---------------------------------------------------------------------------------------------------------------
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"   # Namo tassa bhagavato … (pi-1)
H_ABHI = "# Tạng Vi Diệu Pháp"                                           # # Abhidhammapiṭake (pi-1)
H_BOOK = "## Các cặp câu hỏi"                                            # ## Yamakapāḷi
BOOK_END = "Bộ “Các cặp câu hỏi” đã hoàn tất."                           # Yamakapakaraṇaṃ niṭṭhitaṃ.
NITTHITO = "đã hoàn tất"                                                 # niṭṭhito / niṭṭhitā (pi-2)

YAMAKA = {   # <X>yamakaṃ: «Các cặp câu hỏi về …»
    "Mūla": "gốc rễ", "Khandha": "các khối", "Āyatana": "các lĩnh vực nhận biết", "Dhātu": "các yếu tố",
    "Sacca": "các sự thật", "Saṅkhāra": "các tạo tác", "Anusaya": "các khuynh hướng tiềm ẩn", "Citta": "tâm",
    "Dhamma": "các hiện tượng", "Indriya": "các năng lực",
}


def yamaka_title(x):                     # <X>yamakaṃ (heading)
    return f"Các cặp câu hỏi về {YAMAKA[x]}"


def yamaka_end(x):                       # <X>yamakapāḷi niṭṭhitā.
    return f"Phần {yamaka_title(x)[0].lower()}{yamaka_title(x)[1:]} {NITTHITO}."


LABEL = {"Ka": "(a)", "Kha": "(b)", "Ga": "(c)", "Gha": "(d)", "Ṅa": "(đ)", "Ca": "(e)", "Cha": "(g)", "Ja": "(h)"}

# ---------------------------------------------------------------------------------------------------------------
# Chapter-1 headings and the four methods
# ---------------------------------------------------------------------------------------------------------------
UDDESO = "Phần nêu đề mục"               # uddeso (pi-1)
NIDDESO = "Phần giải thích"              # niddeso
UDDESAVARO = "Mục nêu đề mục"            # Uddesavāro
NIDDESAVARO = "Mục giải thích"           # Niddesavāro
MULAVARO = "Mục về gốc rễ"               # Mūlavāro
HETUVARADI = "Mục về nguyên nhân và các mục khác"   # Hetuvārādi
MULAVARA_UDDESO = "Phần nêu đề mục của mục về gốc rễ."   # Mūlavārauddeso.
MULAVARA_NIDDESO = "Phần giải thích của mục về gốc rễ."  # Mūlavāraniddeso.

# method word (M) = the Pāli stem after the kind: mūla, mūlamūla, mūlaka, mūlamūlaka
BASE = {"mūla": "gốc rễ", "mūlamūla": "cội rễ", "mūlaka": "gốc rễ", "mūlamūlaka": "cội rễ"}
NOUN_M = ("mūla", "mūlamūla")            # the root methods name things; the -mūlaka methods say "stemming from"
NAYA = {"mūla": "gốc rễ", "mūlamūla": "cội rễ", "mūlaka": "sự bắt nguồn từ gốc rễ",
        "mūlamūlaka": "sự bắt nguồn từ cội rễ"}
NAYA_PALI = {"Mūla": "mūla", "Mūlamūla": "mūlamūla", "Mūlaka": "mūlaka", "Mūlamūlaka": "mūlamūlaka"}


def nayo(m, lower=False):                # <X>nayo: «Phương pháp về <X>»
    s = f"Phương pháp về {NAYA[m]}"
    return s[0].lower() + s[1:] if lower else s


# the kinds (X slot) and their roots
KIND = {"kusala": "thiện", "akusala": "bất thiện", "abyākata": "không xác định về mặt đạo đức",
        "nāma": "thuộc phần tinh thần"}
X_SLOT = {"kusala": "là thiện", "akusala": "là bất thiện", "abyākata": "không xác định về mặt đạo đức",
          "nāma": "thuộc phần tinh thần"}          # ye keci X dhammā / sabbe te dhammā X
KIND_HEAD = {"kusala": "Các hiện tượng thiện", "akusala": "Các hiện tượng bất thiện",
             "abyākata": "Các hiện tượng không xác định về mặt đạo đức",
             "nāma": "Các hiện tượng thuộc phần tinh thần"}   # Kusalā dhammā … (heading; pi-3 «Các hiện tượng thiện»)
SUBJ = {"kusala": "hiện tượng thiện", "akusala": "hiện tượng bất thiện",
        "abyākata": "hiện tượng không xác định về mặt đạo đức", "nāma": "phần tinh thần"}   # Kusalaṃ / Akusalaṃ … (subject)
PRED_SG = {"kusala": "là thiện", "akusala": "là bất thiện",
           "abyākata": "là hiện tượng không xác định về mặt đạo đức", "nāma": "thuộc phần tinh thần"}  # (na) kusalaṃ, kusalañca
SAMUT = {"kusala": "hiện tượng thiện", "akusala": "hiện tượng bất thiện",
         "abyākata": "hiện tượng không xác định về mặt đạo đức", "nāma": "phần tinh thần"}   # Xsamuṭṭhānaṃ «do … sinh ra»


def root_noun(k, m="mūla"):              # kusalamūla «gốc rễ thiện», kusalamūlamūla «cội rễ thiện»
    return f"{BASE[m]} {KIND[k]}"


def by_root(k):                          # Xmūlena «xét theo gốc rễ X»
    return f"xét theo {root_noun(k)}"


def root_pred(k, m):                     # kusalamūlā / -mūlamūlā / -mūlakā / -mūlamūlakā (predicate)
    return f"là {root_noun(k, m)}" if m in NOUN_M else f"bắt nguồn từ {root_noun(k, m)}"


def eka(m):                              # ekamūlā … «có cùng một gốc rễ» / «bắt nguồn từ cùng một gốc rễ»
    return f"có cùng một {BASE[m]}" if m in NOUN_M else f"bắt nguồn từ cùng một {BASE[m]}"


def anna(m):                             # aññamaññamūlā … «làm gốc rễ cho nhau» / «bắt nguồn từ gốc rễ của nhau»
    return f"làm {BASE[m]} cho nhau" if m in NOUN_M else f"bắt nguồn từ {BASE[m]} của nhau"


def neg(p):                              # na Y: «là Y» → «không phải là Y»; other predicates → «không Y»
    return "không phải " + p if p.startswith("là ") else "không " + p


# ---------------------------------------------------------------------------------------------------------------
# Pāli predicate parser (kusalā, kusalamūlā, kusalamūlena ekamūlā, aññamaññamūlakāni, ekamūlañceva …)
# ---------------------------------------------------------------------------------------------------------------
K_RE = r"(akusala|kusala|abyākata|nāma)"
M_RE = r"(mūl(?:amūl)?(?:ak)?)"
END_RE = r"(?:ā|āni|aṃ|a)"
M_OF = {"mūl": "mūla", "mūlamūl": "mūlamūla", "mūlak": "mūlaka", "mūlamūlak": "mūlamūlaka"}


def parse_tok(t):
    if t.endswith("āti"):
        t = t[:-2]
    if m := re.fullmatch(K_RE + "mūlena", t):
        return ("by", m.group(1))
    if m := re.fullmatch(K_RE + M_RE + END_RE, t):
        return ("root", m.group(1), M_OF[m.group(2)])
    if m := re.fullmatch("eka" + M_RE + END_RE, t):
        return ("eka", M_OF[m.group(1)])
    if m := re.fullmatch("aññamañña" + M_RE + END_RE, t):
        return ("anna", M_OF[m.group(1)])
    if m := re.fullmatch(r"(akusal|kusal|abyākat|nām)(?:ā|aṃ|a)", t):
        return ("kind", m.group(1) + "a")
    raise ValueError(f"unknown Pāli predicate word {t!r}")


def render1(tok):
    kind = tok[0]
    if kind == "root":
        return root_pred(tok[1], tok[2])
    if kind == "eka":
        return eka(tok[1])
    if kind == "anna":
        return anna(tok[1])
    if kind == "kind":
        return X_SLOT[tok[1]]
    raise ValueError(tok)


def pred(phrase):
    """Vietnamese predicate for a Pāli X / Y slot: 'kusalā', 'kusalamūlā', 'kusalamūlena ekamūlā' …"""
    toks = [parse_tok(t) for t in phrase.split()]
    if len(toks) == 1:
        return render1(toks[0])
    if len(toks) == 2 and toks[0][0] == "by":
        return f"{render1(toks[1])} {by_root(toks[0][1])}"
    raise ValueError(f"unknown Pāli predicate {phrase!r}")


# ---------------------------------------------------------------------------------------------------------------
# Pair questions and answers
# ---------------------------------------------------------------------------------------------------------------
def qa(x, y, label="Ka", end=" không?"):   # (Ka) Ye keci X dhammā, sabbe te Y(ti)?
    return f"{LABEL[label]} Bất cứ hiện tượng nào {x}, có phải tất cả chúng đều {y}{end}"


def qb(y, x, label="Kha", end=" không?"):  # (Kha) Ye vā pana Y, sabbe te dhammā X(ti)?
    return f"{LABEL[label]} Còn bất cứ gì {y}, có phải tất cả các hiện tượng ấy đều {x}{end}"


YES = "Đúng vậy."                          # Āmantā. (pi-5)
PE = "…"                                   # …pe… (never «.…» / «….»; a final «.» after …pe… is absorbed)
NUM = {"Tīṇeva": "ba", "Tayo eva": "ba", "Naveva": "chín"}
AHETUKA, SAHETUKA = "mà không có gốc rễ", "mà có gốc rễ"   # Ahetukaṃ / Sahetukaṃ X (pi-1 ahetuka / sahetuka)


def only(num, noun):                       # Tīṇeva Xmūlāni. / Naveva nāmamūlāni.
    return f"Chỉ có {NUM[num]} {noun}."


def rest_not(k, p):                        # Avasesā X dhammā na Y.
    return f"Các hiện tượng {KIND[k]} còn lại {neg(p)}."


def samutthana(k, p, comma=True):          # Xsamuṭṭhānaṃ rūpaṃ P(,) na Xaṃ.
    return f"Vật chất do {SAMUT[k]} sinh ra thì {p}{',' if comma else ''} nhưng {neg(PRED_SG[k])}."


def both(k, p):                            # Xaṃ Pñceva Xañca.  («vừa A vừa B» for A ceva B ca)
    return f"{cap(SUBJ[k])} vừa {p} vừa {PRED_SG[k]}."


def hetuka(k, p, sahetuka):                # Ahetukaṃ / Sahetukaṃ Xaṃ (Xmūlena) (na) P.
    return f"{cap(SUBJ[k])} {SAHETUKA if sahetuka else AHETUKA} thì {p}."


ROOTS_TOGETHER = "Những gốc rễ nào cùng sinh khởi"   # Mūlāni yāni ekato uppajjanti (ekato uppajjanti, pi-1)


def roots_together(k, m_root, m):          # Mūlāni yāni ekato uppajjanti Xmūlāni ekaMāni ceva aññamaññaMāni ca.
    return f"{ROOTS_TOGETHER}, các {root_noun(k, m_root)} ấy vừa {eka(m)} vừa {anna(m)}."


def rest_conascent(k, p, p_neg, comma=True):  # Avasesā Xmūlasahajātā dhammā P(,) na ca Q.
    return (f"Các hiện tượng còn lại cùng sinh với {root_noun(k)} thì {p}{',' if comma else ''} "
            f"nhưng {neg(p_neg)}.")


# ---------------------------------------------------------------------------------------------------------------
# Hetuvāra: the ten-term series and its verse
# ---------------------------------------------------------------------------------------------------------------
SERIES = [("mūla", "gốc rễ"), ("hetu", "nguyên nhân"), ("nidāna", "căn nguyên"), ("sambhava", "sự hình thành"),
          ("pabhava", "sự khởi nguồn"), ("samuṭṭhāna", "nguồn gốc"), ("āhāra", "dưỡng chất"),
          ("ārammaṇa", "đối tượng"), ("paccaya", "điều kiện"), ("samudaya", "sự phát sinh")]   # (pi-5)


def series(k, i):                          # kusalahetū «nguyên nhân thiện» … (noun + adjective)
    return f"{SERIES[i][1]} {KIND[k]}"


def series_run(k, start=1, stop=10):       # X-hetū…pe… X-nidānā…pe… … X-samudayā…pe….  /  … X-nidānā… …
    return f"{PE} ".join(series(k, i) for i in range(start, stop)) + PE


VERSE = ("Gốc rễ, nguyên nhân và căn nguyên, sự hình thành cùng với sự khởi nguồn;",   # Mūlaṃ hetu nidānañca, …
         "Nguồn gốc, dưỡng chất, đối tượng{var}, điều kiện cùng với sự phát sinh.")    # Samuṭṭhānāhārārammaṇā, …


def var(sigla, word):                      # [X (ka.)] form variant
    return f"[dị bản ({sigla}): {word}]"


def var_sp(sigla, word):                   # spelling-only variant
    return f"[khác chính tả ({sigla}): {word}]"


# ---------------------------------------------------------------------------------------------------------------
# Approved headings of the later chapters (user 2026-11-22): use verbatim
# ---------------------------------------------------------------------------------------------------------------
LATER_HEADINGS = [
    ("(Ka) anulomaṃ / (Kha) paccanīkaṃ", "(a) Chiều thuận / (b) Chiều nghịch"),
    ("paṭiloma", "chiều ngược"),
    ("Paṇṇattivāro", "Mục về sự định danh"),
    ("Padasodhanavāro", "Mục về sự làm sáng tỏ thuật ngữ"),
    ("Padasodhanamūlacakkavāro", "Mục về vòng luân chuyển dựa trên sự làm sáng tỏ thuật ngữ"),
    ("Suddha<X>vāro", "Mục về các <X> thuần túy"),
    ("Pavattivāro", "Mục về sự diễn tiến"),
    ("uppādavāro", "mục về sự sinh khởi"),
    ("nirodhavāro", "mục về sự chấm dứt"),
    ("Pariññāvāro", "Mục về sự hiểu biết trọn vẹn"),
    ("Paccuppannavāro / Atītavāro / Anāgatavāro", "Mục về hiện tại / Mục về quá khứ / Mục về tương lai"),
    ("anulomapuggalo / anulomaokāso / anulomapuggalokāsā",
     "Chiều thuận theo người / Chiều thuận theo nơi chốn / Chiều thuận theo người và nơi chốn"),
    ("paccanīkapuggalo / paccanīkaokāso / paccanīkapuggalokāsā",
     "Chiều nghịch theo người / Chiều nghịch theo nơi chốn / Chiều nghịch theo người và nơi chốn"),
    ("Pajahanavāro", "Mục về sự dứt bỏ"),
    ("Pahīnavāro", "Mục về những gì đã được dứt bỏ"),
    ("dhātupucchāvāro", "Mục hỏi theo các cõi"),
    ("dhātuvisajjanāvāro / Dhātuvisajjavāro", "Mục trả lời theo các cõi"),
]

# ---------------------------------------------------------------------------------------------------------------
# Strings taken unchanged from the pi-1 … pi-5 Vietnamese rails (asserted at build time)
# ---------------------------------------------------------------------------------------------------------------
REUSED = [
    ("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE, "1"),
    ("# Abhidhammapiṭake", H_ABHI, "1"),
    ("Uddeso (heading)", UDDESO, "1"),
    ("Āmantā.", YES, "5"),
    ("Khandhavibhaṅgo niṭṭhito. (niṭṭhito / niṭṭhitā)", NITTHITO + ".", "2"),
    ("Kusalā dhammā… akusalā dhammā", "Các hiện tượng thiện… các hiện tượng bất thiện", "3"),
    ("Avasesā dhammā …", "Các hiện tượng còn lại", "2"),
    ("dve tayo hetū ekato uppajjanti", "cùng sinh khởi", "1"),
    ("sahajātaṃ", "cùng sinh", "2"),
    ("hetū ceva dhammā sahetukā ca (A ceva B ca)", "vừa là gốc rễ vừa có gốc rễ", "1"),
    ("sahetukā ceva dhammā na ca hetū (na ca)", "nhưng không phải là gốc rễ", "1"),
    ("ahetukaṃ", "không có gốc rễ", "1"),
    ("cittasamuṭṭhānaṃ (X-samuṭṭhāna)", "do tâm sinh ra", "1"),
    ("Tīṇeva ariyasaccānīti? (Tīṇeva)", "chỉ có ba", "5"),
    ("mūlato … samudayato (the ten-term series)",
     "xét theo gốc rễ, biết xét theo nguyên nhân, biết xét theo căn nguyên, biết xét theo sự hình thành, "
     "biết xét theo sự khởi nguồn, biết xét theo nguồn gốc, biết xét theo dưỡng chất, biết xét theo đối tượng, "
     "biết xét theo điều kiện, biết xét theo sự phát sinh", "5"),
    ("[X (ka.)] form variant", "[dị bản (", "1"),
    ("[X (ka.)] spelling variant", "[khác chính tả (Ka.):", "1"),
]


def check_reused():
    texts = {}
    for b, d in RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# Chapter 1: line translator (the Pāli line structure is kept 1:1)
# ---------------------------------------------------------------------------------------------------------------
KIND_PALI = {"Kusalā": "kusala", "Akusalā": "akusala", "Abyākatā": "abyākata", "Nāmā": "nāma"}


def heading(text):
    """Heading text without #s and block ID."""
    fixed = {"Mūlayamakaṃ": yamaka_title("Mūla"), "(Ka) uddeso": f"{LABEL['Ka']} {UDDESO}",
             "(Kha) niddeso": f"{LABEL['Kha']} {NIDDESO}", "Mūlavāro": MULAVARO,
             "2-10. Hetuvārādi": f"2-10. {HETUVARADI}"}
    if text in fixed:
        return fixed[text]
    if m := re.fullmatch(r"(Kusalā|Akusalā|Abyākatā|Nāmā) dhammā", text):
        return KIND_HEAD[KIND_PALI[m.group(1)]]
    if m := re.fullmatch(r"(?:(Kusalā|Akusalā|Abyākatā|Nāmā) dhammā )?\((\d)\) ([Mm]ūl\w*?)nayo", text):
        word = m.group(3)
        lower = word[0] == "m"
        mm = NAYA_PALI[cap(word)]
        head = f"({m.group(2)}) {nayo(mm, lower)}"
        return f"{KIND_HEAD[KIND_PALI[m.group(1)]]} {head}" if m.group(1) else head
    raise ValueError(f"unknown heading {text!r}")


def sentence(s):
    """One answer sentence (ends with «.»)."""
    exact = {"Āmantā.": YES, "Mūlavārauddeso.": MULAVARA_UDDESO, "Mūlavāraniddeso.": MULAVARA_NIDDESO,
             "Uddesavāro niṭṭhito.": f"{UDDESAVARO} {NITTHITO}.", "Niddesavāro niṭṭhito.": f"{NIDDESAVARO} {NITTHITO}.",
             "Mūlayamakapāḷi niṭṭhitā.": yamaka_end("Mūla")}
    if s in exact:
        return exact[s]
    if m := re.fullmatch(r"(Tīṇeva|Naveva) (\S+)\.", s):
        t = parse_tok(m.group(2))
        return only(m.group(1), root_noun(t[1], t[2]))
    if m := re.fullmatch(r"Avasesā (\S+) dhammā na (\S+)\.", s):
        return rest_not(parse_tok(m.group(1))[1], pred(m.group(2)))
    if m := re.fullmatch(r"(\S+)samuṭṭhānaṃ rūpaṃ (.+?)(,?) na (\S+)\.", s):
        k = KIND_PALI[m.group(1)[:-1] + "ā"]
        return samutthana(k, pred(m.group(2)), comma=bool(m.group(3)))
    if m := re.fullmatch(r"(Kusalaṃ|Akusalaṃ|Abyākataṃ|Nāmaṃ) (.+)ñceva (\S+)ñca\.", s):
        k = parse_tok(m.group(1).lower())[1]
        return both(k, pred(m.group(2) + "ṃ"))
    if m := re.fullmatch(r"(Ahetukaṃ|Sahetukaṃ) (\S+) (.+)\.", s):
        k = parse_tok(m.group(2))[1]
        words = m.group(3).split()
        negated = "na" in words
        p = pred(" ".join(w for w in words if w != "na"))
        if negated:   # «na» sits before the last word: negate the method predicate, keep «xét theo …» after it
            p = neg(p)
        return hetuka(k, p, m.group(1) == "Sahetukaṃ")
    if m := re.fullmatch(r"Mūlāni yāni ekato uppajjanti (\S+) (\S+) ceva (\S+) ca\.", s):
        r, e, a = parse_tok(m.group(1)), parse_tok(m.group(2)), parse_tok(m.group(3))
        assert e[1] == a[1], s
        return roots_together(r[1], "mūla", e[1])
    if m := re.fullmatch(r"Avasesā (\S+)mūlasahajātā dhammā (.+?)(,?) na ca (\S+)\.", s):
        k = parse_tok(m.group(1)[:-1] + "ā")[1]
        return rest_conascent(k, pred(m.group(2)), pred(m.group(4)), comma=bool(m.group(3)))
    raise ValueError(f"unknown sentence {s!r}")


def sentences(rest):
    parts = [x for x in re.split(r"(?<=\.) ", rest.strip()) if x]
    return " ".join(sentence(x) for x in parts)


QA_RE = re.compile(r"\(Ka\) ye keci (.+?) dhammā, sabbe te (.+?)(?:ti)?\?(.*)")
QB_RE = re.compile(r"\(Kha\) ye vā pana (.+?), sabbe te dhammā (.+?)(?:ti)?\?(.*)")

# hetuvāra lines (fixed)
K = "kusala"
HETU_LINES = {
    "Ye keci kusalā dhammā, sabbe te kusalahetū…pe… kusalanidānā…pe… kusalasambhavā…pe… kusalappabhavā…pe… "
    "kusalasamuṭṭhānā…pe… kusalāhārā…pe… kusalārammaṇā…pe… kusalapaccayā…pe… kusalasamudayā…pe….":
        f"Bất cứ hiện tượng nào {X_SLOT[K]}, có phải tất cả chúng đều là {series_run(K)}",
    "Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;": VERSE[0],
    "Samuṭṭhānāhārārammaṇā [samuṭṭhānāhārārammaṇaṃ (ka.)], paccayo samudayena cāti.":
        VERSE[1].format(var=" " + var("Ka.", "samuṭṭhānāhārārammaṇaṃ")),
    "Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.": VERSE[1].format(var=""),
    "Ye keci kusalā dhammā, sabbe te kusalahetūti…?":
        f"Bất cứ hiện tượng nào {X_SLOT[K]}, có phải tất cả chúng đều là {series(K, 1)}{PE} không?",
    "Tayo eva kusalahetū, avasesā kusalā dhammā na kusalahetū…pe… kusalanidānā… kusalasambhavā… "
    "kusalappabhavā… kusalasamuṭṭhānā… kusalāhārā… kusalārammaṇā… kusalapaccayā… kusalasamudayā….":
        f"Chỉ có {NUM['Tayo eva']} {series(K, 1)}, các hiện tượng {KIND[K]} còn lại không phải là {series_run(K)}",
    "Ye keci akusalā dhammā… ye keci abyākatā dhammā… ye keci nāmā dhammā, sabbe te nāmahetū ti… nāmanidānā… "
    "nāmasambhavā… nāmappabhavā… nāmasamuṭṭhānā… nāmāhārā… nāmārammaṇā… nāmapaccayā… nāmasamudayā….":
        (f"Bất cứ hiện tượng nào {X_SLOT['akusala']}{PE} bất cứ hiện tượng nào {X_SLOT['abyākata']}{PE} "
         f"bất cứ hiện tượng nào {X_SLOT['nāma']}, có phải tất cả chúng đều là {series_run('nāma')}"),
    "Namo tassa bhagavato arahato sammāsambuddhassa": HOMAGE,
}


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    elif body in HETU_LINES:
        out = HETU_LINES[body]
    elif mm := QA_RE.fullmatch(body):
        out = qa(pred(mm.group(1)), pred(mm.group(2)))
        if mm.group(3).strip():
            out += " " + sentences(mm.group(3))
    elif mm := QB_RE.fullmatch(body):
        out = qb(pred(mm.group(1)), pred(mm.group(2)))
        if mm.group(3).strip():
            out += " " + sentences(mm.group(3))
    else:
        out = sentences(body)
    return f"{out} {bid}" if bid else out


def segments_of(name):
    """Pāli file → list of segments (lists of non-empty lines)."""
    segs, cur = [], []
    for ln in (PALI_DIR / name).read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        cur.append(ln)
        if re.search(r"\^\S+$", ln):
            segs.append(cur)
            cur = []
    assert not cur, (name, cur)
    return segs


def build(name):
    return [[tr_line(ln) for ln in seg] for seg in segments_of(name)]


def build_preamble():
    return [[f"{HOMAGE} ^T-1"], [f"{H_ABHI} ^0"], [f"{H_BOOK} ^6-0"]]


# ---------------------------------------------------------------------------------------------------------------
# Checks (per line: dash count vs the Pāli line, balanced quotes per segment, NFC; plus the reuse assertion)
# ---------------------------------------------------------------------------------------------------------------
DASHES = ("–", "—")


def dash_count(t):
    return sum(t.count(d) for d in DASHES)


def dash_ok(pali_line, vi_line):
    return dash_count(pali_line) == dash_count(vi_line)


def quotes_ok(text):
    return text.count("“") == text.count("”") and text.count("‘") == text.count("’")


def nfc_ok(t):
    return unicodedata.normalize("NFC", t) == t


def check_against_pali(name, segs):
    pl = [x for x in (PALI_DIR / name).read_text(encoding="utf-8").splitlines() if x.strip()]
    vl = [x for s in segs for x in s]
    assert len(pl) == len(vl), (name, len(pl), len(vl))
    probs = []
    for k, (p, v) in enumerate(zip(pl, vl), 1):
        if not dash_ok(p, v):
            probs.append(f"line {k}: dashes pali {dash_count(p)} vi {dash_count(v)}")
        if not nfc_ok(v):
            probs.append(f"line {k}: not NFC")
        pid, vid = re.search(r"\^\S+$", p), re.search(r"\^\S+$", v)
        if (pid and pid.group(0)) != (vid and vid.group(0)):
            probs.append(f"line {k}: id {pid and pid.group(0)} vs {vid and vid.group(0)}")
        for bad in ("—", ":-", "….", ".…", "  ", "chánh niệm", " là là "):
            if bad in v:
                probs.append(f"line {k}: {bad!r}")
        if re.search(r"[āīūṃṅñṭḍṇḷfjwzFJWZ]", re.sub(r"\[[^\]]*\]", "", re.sub(r"\^\S+$", "", v))):
            probs.append(f"line {k}: foreign letter")
        if p.rstrip().endswith("?") or re.search(r"\?\s+\^", p):
            if "?" not in v:
                probs.append(f"line {k}: question mark lost")
    for s in segs:
        if not quotes_ok("\n".join(s)):
            probs.append(f"unbalanced quotes in segment ending {s[-1][-12:]}")
    assert not probs, f"{name}:\n" + "\n".join(probs[:40])


def write(name, segs):
    check_against_pali(name, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (OUT_DIR / name).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT_DIR / name, f"({len(segs)} segments)")


# ---------------------------------------------------------------------------------------------------------------
# Formula file
# ---------------------------------------------------------------------------------------------------------------
def formulas():
    tagged = {v: b for _, v, b in REUSED}
    out = []

    def row(p, v, b=None):
        b = b or tagged.get(v)
        out.append(f"{p} = {v}" + (f" (pi-{b})" if b else ""))

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += ["# pi-6 Yamaka: Vietnamese rails formulas and fixed strings (binding for chapters 2-01 … 10-13)", "",
            "Format: Pāli = tiếng Việt, one per line; (pi-1) … (pi-5) = taken unchanged from that book's approved "
            "Vietnamese rails (asserted by the builder). Generated by build_rails_sample_vi.py: import its constants "
            "and slot helpers (LABEL, yamaka_title, yamaka_end, qa, qb, pred, neg, only, rest_not, samutthana, both, "
            "hetuka, roots_together, rest_conascent, series, VERSE, var, var_sp, LATER_HEADINGS …) rather than "
            "retyping. X / Y are predicate slots (a «là» is part of the slot where Vietnamese needs it). "
            "Termbase: AI_translation/vietnamese/pi-6-pali-vietnamese-termbase-plain.md (+ pi-6-vi-ai/termbase/APPROVED.md). "
            "Style: 0-INBOX/temp/pipeline/vietnamese-style.md."]
    h("Book frame, yamaka titles, labels")
    row("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE)
    row("# Abhidhammapiṭake", H_ABHI)
    row("## Yamakapāḷi", H_BOOK)
    row("Yamakapakaraṇaṃ niṭṭhitaṃ.", BOOK_END)
    row("<X>yamakaṃ (heading)", "Các cặp câu hỏi về <X>")
    row("<X>yamakapāḷi niṭṭhitā.", "Phần các cặp câu hỏi về <X> đã hoàn tất.")
    for x in YAMAKA:
        row(f"{x}yamakaṃ / {x}yamakapāḷi niṭṭhitā.", f"{yamaka_title(x)} / {yamaka_end(x)}")
    row("niṭṭhito / niṭṭhitā (closing)", "… đã hoàn tất.", "2")
    row("(Ka) (Kha) (Ga) (Gha) (Ṅa) (Ca) (Cha) (Ja)", " ".join(LABEL.values()) + "  (never f / j / w / z)")
    h("Chapter 1 headings")
    row("uddeso", UDDESO)
    row("niddeso", NIDDESO)
    row("<X>vāro", "Mục về <X>")
    row("Mūlavāro", MULAVARO)
    row("Hetuvārādi", HETUVARADI)
    row("Uddesavāro niṭṭhito. / Niddesavāro niṭṭhito.", f"{UDDESAVARO} {NITTHITO}. / {NIDDESAVARO} {NITTHITO}.")
    row("Mūlavārauddeso.", MULAVARA_UDDESO)
    row("Mūlavāraniddeso.", MULAVARA_NIDDESO)
    row("<X>nayo", "Phương pháp về <X>  (a lowercase method word as written stays lowercase: «phương pháp về …»)")
    for p, m in NAYA_PALI.items():
        row(f"{p}nayo", nayo(m))
    row("Kusalā dhammā (heading)", KIND_HEAD["kusala"], "3")
    for p, k in list(KIND_PALI.items())[1:]:
        row(f"{p} dhammā (heading)", KIND_HEAD[k])
    row("<Kind> dhammā (1) mūlanayo", "<Các hiện tượng …> (1) phương pháp về gốc rễ")
    row("2-10. Hetuvārādi", f"2-10. {HETUVARADI}  (hyphen kept: not a dash)")
    h("Later-chapter headings (approved 2026-11-22; use verbatim, do not invent others)")
    for p, v in LATER_HEADINGS:
        row(p, v)
    h("Pair questions")
    row("(Ka) ye keci X dhammā, sabbe te Y(ti)?", qa("X", "Y"))
    row("(Kha) ye vā pana Y, sabbe te dhammā X(ti)?", qb("Y", "X"))
    row("question cut by …pe… (no «?» in the Pāli)", "keeps its shape and ends «…»; «không?» only where the Pāli has «?»")
    row("Xti…? (6-1-98)", "… X… không?")
    def pf(stem, end):                   # Pāli form: kusala + ā = kusalā, mūlaka + āni = mūlakāni
        return stem[:-1] + end

    h("Slot terms (X / Y predicates)")
    for k in KIND:
        row(f"{pf(k, 'ā')} (X slot)", X_SLOT[k])
    for k in KIND:
        row(f"{k}mūla / {k}mūlamūla (noun)", f"{root_noun(k)} / {root_noun(k, 'mūlamūla')}")
    for k in KIND:
        row(f"{k}mūlena", by_root(k))
    for m in BASE:
        row(f"kusala{pf(m, 'ā')} (Y slot)", root_pred("kusala", m))
    for m in BASE:
        row(f"eka{pf(m, 'ā')} / aññamañña{pf(m, 'ā')}", f"{eka(m)} / {anna(m)}")
    row("kusalamūlena ekamūlā (two-word slot)", pred("kusalamūlena ekamūlā"))
    row("kusalamūlena aññamaññamūlamūlakā", pred("kusalamūlena aññamaññamūlamūlakā"))
    row("na Y (Y = «là …»)", "không phải là …")
    row("na Y (other Y) / na ca Y", "không … / nhưng không …")
    h("Answers")
    row("Āmantā.", YES)
    row("Tīṇeva Xmūlāni.", "Chỉ có ba gốc rễ X.")
    row("Tīṇeva Xmūlamūlāni.", "Chỉ có ba cội rễ X.")
    row("Naveva nāmamūlāni.", only("Naveva", root_noun("nāma")))
    row("Tayo eva kusalahetū, …", f"Chỉ có ba {series('kusala', 1)}, …")
    row("Avasesā X dhammā na Y.", "Các hiện tượng X còn lại không phải là Y.")
    row("Avasesā kusalā dhammā na kusalamūlā.", rest_not("kusala", pred("kusalamūlā")))
    row("Xsamuṭṭhānaṃ rūpaṃ P, na Xaṃ.", "Vật chất do <X> sinh ra thì P, nhưng không phải là X.  (no comma where the Pāli has none)")
    for k in ("kusala", "akusala", "nāma"):
        row(f"{cap(k)}samuṭṭhānaṃ rūpaṃ {k}mūlena ekamūlaṃ, na {pf(k, 'aṃ')}.",
            samutthana(k, pred(f"{k}mūlena ekamūlaṃ")))
    row("Kusalasamuṭṭhānaṃ rūpaṃ kusalamūlakaṃ na kusalaṃ. (no comma)",
        samutthana("kusala", pred("kusalamūlakaṃ"), comma=False))
    row("A ceva B ca", "vừa A vừa B")
    for k in ("kusala", "akusala", "nāma"):
        row(f"{cap(pf(k, 'aṃ'))} {k}mūlena ekamūlañceva {pf(k, 'añca')}.", both(k, pred(f"{k}mūlena ekamūlaṃ")))
    row("Ahetukaṃ / Sahetukaṃ X", "X mà không có gốc rễ / X mà có gốc rễ")
    row("Ahetukaṃ akusalaṃ akusalamūlena na ekamūlaṃ.",
        hetuka("akusala", neg(pred("akusalamūlena ekamūlaṃ")), False))
    row("Sahetukaṃ abyākataṃ abyākatamūlakaṃ.", hetuka("abyākata", pred("abyākatamūlakaṃ"), True))
    row("Ahetukaṃ nāmaṃ na nāmamūlakaṃ.", hetuka("nāma", neg(pred("nāmamūlakaṃ")), False))
    row("Mūlāni yāni ekato uppajjanti", ROOTS_TOGETHER + "  (ekato uppajjanti «cùng sinh khởi»)", "1")
    for m in BASE:
        row(f"Mūlāni yāni ekato uppajjanti kusalamūlāni eka{pf(m, 'āni')} ceva aññamañña{pf(m, 'āni')} ca.",
            roots_together("kusala", "mūla", m))
    row("sahajāta", "cùng sinh", "2")
    row("Avasesā kusalamūlasahajātā dhammā kusalamūlena ekamūlā, na ca aññamaññamūlā.",
        rest_conascent("kusala", pred("kusalamūlena ekamūlā"), pred("aññamaññamūlā")))
    row("Avasesā nāmamūlasahajātā dhammā nāmamūlena ekamūlamūlakā, na ca aññamaññamūlamūlakā.",
        rest_conascent("nāma", pred("nāmamūlena ekamūlamūlakā"), pred("aññamaññamūlamūlakā")))
    row("…pe…", PE + "  (same spot; never «.…» / «….»; a final «.» after …pe… is absorbed)", "5")
    h("Hetuvāra: the ten-term series and its verse")
    row("mūla, hetu, nidāna, sambhava, pabhava, samuṭṭhāna, āhāra, ārammaṇa, paccaya, samudaya",
        ", ".join(v for _, v in SERIES) + "  (pi-5, 13-pancamavaggo: «xét theo gốc rễ, … sự phát sinh»)")
    row("hetu (in this series) / sahetuka, ahetuka", "nguyên nhân / có gốc rễ, không có gốc rễ")
    row("kusalahetū / nāmārammaṇā (noun + adjective)", f"{series('kusala', 1)} / {series('nāma', 7)}")
    row("Ye keci kusalā dhammā, sabbe te kusalahetū…pe… … kusalasamudayā…pe….",
        f"Bất cứ hiện tượng nào là thiện, có phải tất cả chúng đều là {series_run('kusala')}")
    row("Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;", VERSE[0])
    row("Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.", VERSE[1].format(var=""))
    h("Variants")
    row("[X (ka.)] form variant", var("Ka.", "X"), "1")
    row("[X (ka.)] spelling-only variant", var_sp("Ka.", "X"), "1")
    out.append("")
    return "\n".join(out)


def main():
    check_reused()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write("preamble.md", build_preamble())
    write("1-mulayamaka.md", build("1-mulayamaka.md"))
    FORMULAS_MD.write_text(unicodedata.normalize("NFC", formulas()), encoding="utf-8", newline="\n")
    print("wrote", FORMULAS_MD)


if __name__ == "__main__":
    main()
