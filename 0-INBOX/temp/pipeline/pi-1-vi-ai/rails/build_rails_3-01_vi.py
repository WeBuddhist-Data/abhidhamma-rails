"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapter 3-01 (opening of the matter chapter: the statement ^1-583, the matter matrix of one- to eleven-fold
classifications ^1-584 … ^1-593, and the exposition of the onefold ^1-594).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/3-01-rupakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-3-01.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never edited:
build_rails_sample_vi.py (S) and build_rails_2-05_vi.py (E, which loads 2-04 = D, 2-03 = T, 2-01/2-02 = B).
Nothing of theirs is changed: this file only reads their tables. A check rebuilds 2-01 … 2-05 in memory and
requires them to equal the finished files byte for byte.
Matrix items keep the 1-matika wording exactly (S.PREDS / S.NAMES), in the singular for «vật chất».
The predicates of matter (MATTER_ADJ, MATTER_NOUN, GEN/HEADS, EKAKA) are clean stand-alone predicates:
«Vật chất nào {pred}?» / «… vật chất này {pred}.» work for 3-02 / 3-03, which import this file.
Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md). Translated fresh from the Pāli.
Later chapter builders may import this file (importing writes nothing).

usage: python -I -X utf8 build_rails_3-01_vi.py
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_2_05_vi", HERE / "build_rails_2-05_vi.py")
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)        # importing writes nothing; E.D = 2-04, E.T = 2-03, E.B = 2-01/2-02
D, T, B = E.D, E.T, E.B

PART = "3-01-rupakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
cap = S.cap
PE, ELL, DASH = "…pe…", "…", "–"
P = S.PREDS                                         # matrix pali (plural) -> predicate
SLIPS = []                                          # (segment, note)

# =========================================================================================
# 1. Matter: «rūpaṃ» = «vật chất» (termbase); classification frames
# =========================================================================================
RUPA = "vật chất"                                   # rūpaṃ (matter)
KIND = "loại"                                       # «atthi … atthi …» = «có loại … có loại …»; yañca = «và loại»
SAB = f"toàn bộ {RUPA}"                             # sabbaṃ rūpaṃ (termbase sabbaṃ «toàn bộ»)
SANGAHO = f"Phân loại {RUPA}"                       # rūpasaṅgaho (termbase «phân loại vật chất»)
BY = "theo nhóm"                                    # -vidhena (termbase «theo nhóm»)
NUM = {   # heading word, -vidhena word, Vietnamese number
    "Ekakaṃ": ("ekavidhena", "một"), "Dukaṃ": ("duvidhena", "hai"), "Tikaṃ": ("tividhena", "ba"),
    "Catukkaṃ": ("catubbidhena", "bốn"), "Pañcakaṃ": ("pañcavidhena", "năm"),
    "Chakkaṃ": ("chabbidhena", "sáu"), "Sattakaṃ": ("sattavidhena", "bảy"),
    "Aṭṭhakaṃ": ("aṭṭhavidhena", "tám"), "Navakaṃ": ("navavidhena", "chín"),
    "Dasakaṃ": ("dasavidhena", "mười"), "Ekādasakaṃ": ("ekādasavidhena", "mười một"),
}
CLASS = {h: f"Phân loại {BY} {n}" for h, (_, n) in NUM.items()}   # Dukaṃ = «phân loại theo nhóm hai» (termbase)
assert CLASS["Dasakaṃ"] == "Phân loại theo nhóm mười" and CLASS["Ekādasakaṃ"] == "Phân loại theo nhóm mười một"
NIDDESO = "Giải thích"                              # -niddeso (termbase «giải thích»)
EXPO = {"Ekakaniddeso": f"{NIDDESO} {CLASS['Ekakaṃ'][0].lower()}{CLASS['Ekakaṃ'][1:]}"}

H = {   # headings and closing lines
    "### Rūpakaṇḍaṃ": f"### {S.CH_HEADINGS['Rūpakaṇḍaṃ']}",
    "#### Uddeso": "#### Phần nêu đề mục",           # termbase Uddeso
    "#### Mātikā": f"#### {S.H_MATIKA}",
    "Mātikā.": f"{S.H_MATIKA}.",
    "#### Rūpavibhatti": f"#### Phân tích {RUPA}",    # termbase vibhatti «phân tích»
    "Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ.": f"{cap(RUPA)} được thấy, được nghe, được cảm nhận, được nhận biết.",
}
for _h, (_vid, _n) in NUM.items():
    H[f"##### {_h}"] = f"##### {CLASS[_h]}"
    H[f"{_h}."] = f"{CLASS[_h]}."
    H[f"{cap(_vid)} rūpasaṅgaho –"] = f"{SANGAHO} {BY} {_n} –"
    H[f"Evaṃ {_vid} rūpasaṅgaho."] = f"Như vậy là {SANGAHO[0].lower()}{SANGAHO[1:]} {BY} {_n}."
for _h, _v in EXPO.items():
    H[f"##### {_h}"] = f"##### {_v}"
    H[f"{_h}."] = f"{_v}."

# =========================================================================================
# 2. Predicates of matter (singular; «Vật chất nào {pred}?», «vật chất này {pred}.»)
# =========================================================================================
# 2a. Adjectival predicates; the matrix ones are 1-matika's wording exactly
MATTER_ADJ = {
    "upādā": P["upādā"], "no upādā": P["no upādā"],
    "upādiṇṇaṃ": P["upādiṇṇā"], "anupādiṇṇaṃ": P["anupādiṇṇā"],
    "upādiṇṇupādāniyaṃ": P["upādiṇṇupādāniyā"], "anupādiṇṇupādāniyaṃ": P["anupādiṇṇupādāniyā"],
    "sanidassanaṃ": P["sanidassanā"], "anidassanaṃ": P["anidassanā"],
    "sappaṭighaṃ": P["sappaṭighā"], "appaṭighaṃ": P["appaṭighā"],
    "cittasamuṭṭhānaṃ": P["cittasamuṭṭhānā"], "na cittasamuṭṭhānaṃ": P["no cittasamuṭṭhānā"],
    "cittasahabhu": P["cittasahabhuno"], "na cittasahabhu": P["no cittasahabhuno"],
    "cittānuparivatti": P["cittānuparivattino"], "na cittānuparivatti": P["no cittānuparivattino"],
    "ajjhattikaṃ": P["ajjhattikā"], "bāhiraṃ": P["bāhirā"],
    "anidassanaappaṭighaṃ": P["anidassanaappaṭighā"],
    # not matrix items
    "oḷārikaṃ": "ở dạng thô",                       # termbase
    "sukhumaṃ": "ở dạng vi tế",                     # termbase
    "dūre": "ở xa",                                 # no termbase entry
    "santike": "ở gần",                             # no termbase entry
    "dhammāyatanapariyāpannaṃ": "nằm trong lĩnh vực đối tượng của ý",   # dhammāyatana + pariyāpanna
    "sukhasamphassaṃ": "khi tiếp xúc thì dễ chịu",  # samphassaṃ «tiếp xúc» + sukha (bodily) «dễ chịu»
    "dukkhasamphassaṃ": "khi tiếp xúc thì khó chịu",  # dukkha (bodily pain, APPROVED) «khó chịu»
}
assert MATTER_ADJ["upādā"] == "là phái sinh" and MATTER_ADJ["no upādā"] == "không phải là phái sinh"
ATTR_OVERRIDE = {"upādā": S.NAMES["upādā"]}       # as a modifier: «vật chất phái sinh» (1-matika «Các hiện tượng phái sinh»)
assert ATTR_OVERRIDE["upādā"] == "phái sinh"

# 2b. Noun predicates: pred = «là N», negated «không phải là N»
MATTER_NOUN = {
    "indriyaṃ": "năng lực", "mahābhūtaṃ": "yếu tố cơ bản", "viññatti": "sự biểu lộ",
    "cakkhāyatanaṃ": "lĩnh vực mắt", "sotāyatanaṃ": "lĩnh vực tai", "ghānāyatanaṃ": "lĩnh vực mũi",
    "jivhāyatanaṃ": "lĩnh vực lưỡi", "kāyāyatanaṃ": "lĩnh vực thân",
    "rūpāyatanaṃ": "lĩnh vực hình sắc", "saddāyatanaṃ": "lĩnh vực âm thanh", "gandhāyatanaṃ": "lĩnh vực mùi",
    "rasāyatanaṃ": "lĩnh vực vị", "phoṭṭhabbāyatanaṃ": "lĩnh vực vật xúc chạm",
    "cakkhudhātu": "yếu tố mắt", "sotadhātu": "yếu tố tai", "ghānadhātu": "yếu tố mũi",
    "jivhādhātu": "yếu tố lưỡi", "kāyadhātu": "yếu tố thân",
    "rūpadhātu": "yếu tố hình sắc", "saddadhātu": "yếu tố âm thanh", "gandhadhātu": "yếu tố mùi",
    "rasadhātu": "yếu tố vị", "phoṭṭhabbadhātu": "yếu tố vật xúc chạm",
    # cakkhundriyaṃ … kāyindriyaṃ: no termbase entry, built from the members (cakkhu «mắt» + indriya «năng lực»)
    "cakkhundriyaṃ": "năng lực mắt", "sotindriyaṃ": "năng lực tai", "ghānindriyaṃ": "năng lực mũi",
    "jivhindriyaṃ": "năng lực lưỡi", "kāyindriyaṃ": "năng lực thân",
    "itthindriyaṃ": "năng lực nữ tính", "purisindriyaṃ": "năng lực nam tính",
    "jīvitindriyaṃ": S.FN["jīvitindriyaṃ"],
    "kāyaviññatti": "sự biểu lộ bằng thân", "vacīviññatti": "sự biểu lộ bằng lời nói",
    "pathavīdhātu": "yếu tố đất", "āpodhātu": "yếu tố nước", "tejodhātu": "yếu tố lửa",
    "vāyodhātu": "yếu tố gió", "ākāsadhātu": "yếu tố không gian",
    "rūpassa lahutā": f"sự nhẹ nhàng của {RUPA}", "rūpassa mudutā": f"sự mềm mại của {RUPA}",
    "rūpassa kammaññatā": f"sự dễ vận dụng của {RUPA}", "rūpassa upacayo": f"sự tăng trưởng của {RUPA}",
    "rūpassa santati": f"sự liên tục của {RUPA}", "rūpassa jaratā": f"sự lão hóa của {RUPA}",
    "rūpassa aniccatā": f"tính vô thường của {RUPA}",
    "kabaḷīkāro āhāro": "thức ăn trong vai trò dưỡng chất",
}
assert MATTER_NOUN["jīvitindriyaṃ"] == "năng lực sống"

# 2c. «G vatthu / G na vatthu / G ārammaṇaṃ / G nārammaṇaṃ» (genitive + head)
GEN = {
    "cakkhusamphassassa": "sự tiếp xúc của mắt", "sotasamphassassa": "sự tiếp xúc của tai",
    "ghānasamphassassa": "sự tiếp xúc của mũi", "jivhāsamphassassa": "sự tiếp xúc của lưỡi",
    "kāyasamphassassa": "sự tiếp xúc của thân",
    "cakkhusamphassajāya vedanāya": "cảm giác sinh từ sự tiếp xúc của mắt",
    "kāyasamphassajāya vedanāya": "cảm giác sinh từ sự tiếp xúc của thân",
    "saññāya": S.FN["saññā"], "cetanāya": S.FN["cetanā"],
    "cakkhuviññāṇassa": D.VIP_SUBJ["vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti"],     # thức qua mắt
    "kāyaviññāṇassa": "thức qua thân",
}
assert GEN["cakkhuviññāṇassa"] == "thức qua mắt" and D.ATTR["kāyaviññāṇaṃ uppannaṃ hoti"].startswith("thức qua thân")
VATTHU = "chỗ dựa"           # vatthu: no termbase entry; closest sibling vatthūni «chỗ dựa»
HEADS = {   # longest first
    "na vatthu": f"không phải là {VATTHU}", "vatthu": f"là {VATTHU}",
    "nārammaṇaṃ": "không phải là đối tượng", "ārammaṇaṃ": "là đối tượng",
}


def _gen_head(s):
    for h in HEADS:
        if s.endswith(" " + h):
            return s[:-len(h) - 1], h
    return None, None


def mpred(s):
    """stand-alone predicate of one Pāli matter expression (no …pe…)"""
    if s in MATTER_ADJ:
        return MATTER_ADJ[s]
    if s in MATTER_NOUN:
        return f"là {MATTER_NOUN[s]}"
    if s.startswith("na ") and s[3:] in MATTER_NOUN:
        return f"không phải là {MATTER_NOUN[s[3:]]}"
    if s.startswith("rūpassa na ") and "rūpassa " + s[11:] in MATTER_NOUN:
        return f"không phải là {MATTER_NOUN['rūpassa ' + s[11:]]}"
    g, h = _gen_head(s)
    if h:
        return f"{HEADS[h]} của {GEN[g]}"
    raise KeyError("matter predicate: " + s)


def pred_expr(s):
    """a predicate, possibly a …pe… run:
    nouns: «X…pe… Y…pe… Z» = «là X… Y… Z», «na X…pe… na Y» = «không phải là X… không phải là Y»;
    genitives: «G1…pe… G2…pe… G3 vatthu» = «là chỗ dựa của G1… của G2… của G3»"""
    parts = [p.strip() for p in s.split(PE)]
    if len(parts) == 1:
        return mpred(parts[0])
    g_last, h = _gen_head(parts[-1])
    if h:
        gens = parts[:-1] + [g_last]
        return f"{HEADS[h]} của {GEN[gens[0]]}" + "".join(f"{ELL} của {GEN[g]}" for g in gens[1:])
    out = mpred(parts[0])
    for p in parts[1:]:
        out += ELL + " " + (mpred(p) if p.startswith("na ") else MATTER_NOUN[p])
    return out


def mattr(s):
    """modifier form after «vật chất» (duka lines, «yañca rūpaṃ …»)"""
    return ATTR_OVERRIDE.get(s) or pred_expr(s)


# =========================================================================================
# 3. The onefold predicates of «Sabbaṃ rūpaṃ» (^1-584) and their «-meva» forms (^1-594)
# =========================================================================================
NOT_KIND = "không thuộc loại"                      # na X / no X of a matrix item whose own wording starts «có» / «không»
EKAKA = {
    "na hetu": P["na hetū"], "ahetukaṃ": P["ahetukā"], "hetuvippayuttaṃ": P["hetuvippayuttā"],
    "sappaccayaṃ": P["sappaccayā"], "saṅkhataṃ": P["saṅkhatā"], "rūpaṃ": P["rūpino"],
    "lokiyaṃ": P["lokiyā"], "sāsavaṃ": P["sāsavā"], "saṃyojaniyaṃ": P["saṃyojaniyā"],
    "ganthaniyaṃ": P["ganthaniyā"], "oghaniyaṃ": P["oghaniyā"], "yoganiyaṃ": P["yoganiyā"],
    "nīvaraṇiyaṃ": P["nīvaraṇiyā"], "parāmaṭṭhaṃ": P["parāmaṭṭhā"], "upādāniyaṃ": P["upādāniyā"],
    "saṃkilesikaṃ": P["saṃkilesikā"], "abyākataṃ": P["abyākatā"], "anārammaṇaṃ": P["anārammaṇā"],
    "acetasikaṃ": P["acetasikā"], "cittavippayuttaṃ": P["cittavippayuttā"],
    "nevavipākanavipākadhammadhammaṃ": P["nevavipākanavipākadhammadhammā"],
    "asaṃkiliṭṭhasaṃkilesikaṃ": P["asaṃkiliṭṭhasaṃkilesikā"],
    "na savitakkasavicāraṃ": f"{NOT_KIND} {P['savitakkasavicārā']}",
    "na avitakkavicāramattaṃ": f"{NOT_KIND} {P['avitakkavicāramattā']}",
    "avitakkaavicāraṃ": P["avitakkaavicārā"],
    "na pītisahagataṃ": P["na pītisahagatā"], "na sukhasahagataṃ": P["na sukhasahagatā"],
    "na upekkhāsahagataṃ": P["na upekkhāsahagatā"],
    "neva dassanena na bhāvanāya pahātabbaṃ": P["neva dassanena na bhāvanāya pahātabbā"],
    "neva dassanena na bhāvanāya pahātabbahetukaṃ": P["neva dassanena na bhāvanāya pahātabbahetukā"],
    "neva ācayagāmi na apacayagāmi": P["nevācayagāmināpacayagāmino"],
    "nevasekkhanāsekkhaṃ": P["nevasekkhanāsekkhā"],
    "parittaṃ": P["parittā"], "kāmāvacaraṃ": P["kāmāvacarā"], "na rūpāvacaraṃ": P["na rūpāvacarā"],
    "na arūpāvacaraṃ": P["na arūpāvacarā"], "pariyāpannaṃ": P["pariyāpannā"],
    "no apariyāpannaṃ": f"{NOT_KIND} {P['apariyāpannā']}",
    "aniyataṃ": P["aniyatā"], "aniyyānikaṃ": P["aniyyānikā"], "uppannaṃ": P["uppannā"],
    "chahi viññāṇehi viññeyyaṃ": "có thể được sáu loại thức nhận biết",   # as PRED «kenaci viññeyyā»
    "aniccaṃ": "là vô thường",                      # termbase aniccameva «chắc chắn là vô thường»
    "jarābhibhūtaṃ": "bị sự lão hóa chế ngự",       # jarā «sự lão hóa» + abhibhūtaṃ «bị … chế ngự»
}
assert EKAKA["rūpaṃ"] == "thuộc vật chất" and EKAKA["na hetu"] == "không phải là gốc rễ"
assert S.PRED["kenaci viññeyyā"].startswith("có thể được ")
SURE = "chắc chắn"                                  # -meva (termbase eva «chắc chắn»)
SURE_IS = {"abyākataṃ", "parittaṃ"}                 # bare adjectives: «chắc chắn là …» (termbase abyākatameva, parittameva)


def meva_key(k):
    return (k[:-1] if k.endswith("ṃ") else k) + "meva"


EKAKA_MEVA = {meva_key(k): f"{SURE} {'là ' if k in SURE_IS else ''}{v}" for k, v in EKAKA.items()}
UPP_MEVA_P = "uppannaṃ chahi viññāṇehi viññeyyameva"     # ^1-594: one item, «uppannaṃ» without -meva or comma
UPP_MEVA_V = f"{EKAKA['uppannaṃ']} thì {SURE} {EKAKA['chahi viññāṇehi viññeyyaṃ']}"
EKAKA_MEVA[UPP_MEVA_P] = UPP_MEVA_V
EKAKA_SEP = "; "                                    # the items carry inner commas («…, chỉ có …»): «; » between items
RUPIYA_V = S.reading("Sī.", "rūpiyaṃ")              # rūpaṃ [rūpiyaṃ (sī.)]: a different word (adjective), so «dị bản»


def ekaka_list(body, table):
    items = []
    for it in body.split(", "):
        var = ""
        if it == "rūpaṃ [rūpiyaṃ (sī.)]":
            it, var = "rūpaṃ", " " + RUPIYA_V
        items.append(table[it] + var)
    return EKAKA_SEP.join(items)


Q_SAB = f"Ở đây, {SAB} là gì?"                     # Tattha katamaṃ sabbaṃ rūpaṃ? (termbase Tattha «ở đây»)
SAB_DEF = (f"Bốn {MATTER_NOUN['mahābhūtaṃ']} và {RUPA} phái sinh từ bốn {MATTER_NOUN['mahābhūtaṃ']} "
           f"{DASH} đó được gọi là {SAB}.")
# Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – idaṃ vuccati sabbaṃ rūpaṃ.
SAB_DEF_P = "Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – idaṃ vuccati sabbaṃ rūpaṃ."
EK1_RE = re.compile(r"Tattha katamaṃ sabbaṃ rūpaṃ\? (.+?) Sabbaṃ rūpaṃ (.+)\.$")
EK2_RE = re.compile(r"Sabbaṃ rūpaṃ (.+)\.$")


def ekaka_vi(line):
    m = EK1_RE.fullmatch(line)
    if m:
        assert m.group(1) == SAB_DEF_P, m.group(1)
        return f"{Q_SAB} {SAB_DEF} {cap(SAB)} {ekaka_list(m.group(2), EKAKA)}."
    m = EK2_RE.fullmatch(line)
    return f"{cap(SAB)} {ekaka_list(m.group(1), EKAKA_MEVA)}."


# =========================================================================================
# 4. The statement ^1-583
# =========================================================================================
KHANDHAS = ", ".join(B.NAMES[k] for k in ("vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho"))
KHANDHAS += " và " + B.NAMES["viññāṇakkhandho"]
# Kusalākusalānaṃ dhammānaṃ vipākā: «là quả của các hiện tượng thiện và bất thiện» (termbase vipākā «quả của
# nghiệp»: the genitive names the cause, so «của nghiệp» is not repeated; reported)
RESULT_OF = "là quả của các hiện tượng thiện và bất thiện"
SPHERES = (f"{P['kāmāvacarā']}, {P['rūpāvacarā']}, {P['arūpāvacarā']} hoặc {P['apariyāpannā']}")
U583_P = ("Katame dhammā abyākatā? Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā "
          "apariyāpannā vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho, ye ca dhammā kiriyā neva "
          "kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ, asaṅkhatā ca dhātu – ime dhammā abyākatā.")
U583_V = (f"{D.Q_ABY} {cap(KHANDHAS)}, {RESULT_OF}, {SPHERES}; những hiện tượng {E.KIRIYA_V}; {SAB}; "
          f"và yếu tố {P['asaṅkhatā']} {DASH} {D.A_ABY}.")
H[U583_P] = U583_V

# =========================================================================================
# 5. Duka, tika and catukka sentences
# =========================================================================================
SENT_SPLIT = re.compile(r"\.\s+(?=(?:Atthi|Yaṃ) )")
DUKA_RE = re.compile(r"Atthi rūpaṃ (.+), atthi rūpaṃ (.+)")
YAM_RE = re.compile(r"Yaṃ taṃ rūpaṃ (.+?), taṃ (.+)")
ATTHI2_RE = re.compile(r"atthi (.+?)(,?) atthi (.+)")


def sentence_vi(s, sid):
    m = DUKA_RE.fullmatch(s)
    if m:
        return f"Có {KIND} {RUPA} {mattr(m.group(1))}, có {KIND} {RUPA} {mattr(m.group(2))}."
    m = YAM_RE.fullmatch(s)
    if m:
        a, rest = m.groups()
        m2 = ATTHI2_RE.fullmatch(rest)
        if m2:
            if not m2.group(2):
                SLIPS.append((sid, f"«{m2.group(1)} atthi {m2.group(3)}» (no comma): rendered as meant (comma)"))
            b = f"có {KIND} {pred_expr(m2.group(1))}, có {KIND} {pred_expr(m2.group(3))}"
        else:
            b = pred_expr(rest)
        return f"{cap(RUPA)} nào {pred_expr(a)} thì {b}."
    raise KeyError("sentence: " + s[:80])


def sentences_vi(line, sid):
    fixed = re.sub(r"\s+…pe…", PE, line)
    for w in re.findall(r"(\S+)\s+…pe…", line):
        SLIPS.append((sid, f"«{w} …pe…» (stray space before «…pe…»): the space is dropped"))
    assert fixed.endswith(".")
    return " ".join(sentence_vi(s, sid) for s in SENT_SPLIT.split(fixed[:-1]))


# =========================================================================================
# 6. The lists of the five- to elevenfold classifications
# =========================================================================================
VINN = {   # X-viññeyyaṃ rūpaṃ: «vật chất mà X có thể nhận biết» (termbase identity frame)
    "cakkhuviññeyyaṃ": "mắt", "sotaviññeyyaṃ": "tai", "ghānaviññeyyaṃ": "mũi", "jivhāviññeyyaṃ": "lưỡi",
    "kāyaviññeyyaṃ": "thân", "manoviññeyyaṃ": "ý", "manodhātuviññeyyaṃ": "yếu tố ý",
    "manoviññāṇadhātuviññeyyaṃ": "yếu tố ý thức",
}
VINN_ATTR = {k: f"mà {v} có thể nhận biết" for k, v in VINN.items()}         # after «vật chất»
VINN_PRED = {k: f"có thể được {v} nhận biết" for k, v in VINN.items()}       # stand-alone (as PRED kenaci viññeyyā)
NA_RUPA_RE = re.compile(r"(.+) rūpaṃ atthi (.+)")


def list_item(it, sid):
    it = it[0].lower() + it[1:]
    if it in MATTER_NOUN:
        return [MATTER_NOUN[it]]
    if it.startswith("yañca rūpaṃ "):
        return [f"và {KIND} {RUPA} {mattr_full(it[len('yañca rūpaṃ '):])}"]
    if it.endswith(" rūpaṃ") and it[:-6] in VINN:
        return [f"{RUPA} {VINN_ATTR[it[:-6]]}"]
    if it.startswith("atthi "):
        return [f"có {KIND} {pred_expr(it[6:])}"]
    m = NA_RUPA_RE.fullmatch(it)
    if m:
        return [f"{RUPA} {mattr(m.group(1))}: có {KIND} {pred_expr(m.group(2))}"]
    ws = it.split(" ")
    if len(ws) > 1 and all(w in MATTER_NOUN for w in ws):
        SLIPS.append((sid, f"«{it}» (no comma): rendered as meant (comma)"))
        return [MATTER_NOUN[w] for w in ws]
    raise KeyError("list item: " + it)


def mattr_full(s):
    """«yañca rūpaṃ X [variant] Y»: modifiers joined, a variant bracket kept after its word"""
    m = re.fullmatch(r"(\S+) \[(\S+) (\S+) \((sī\. syā\.)\)\] (\S+)", s)
    if m:
        w1, v1, v2, _, w2 = m.groups()
        return f"{mattr(w1)} {S.spell('Sī., Syā.', v1 + ' ' + v2)}, {mattr(w2)}"
    return mattr(s)


def list_vi(line, sid):
    assert line.endswith(".")
    items = []
    for it in line[:-1].split(", "):
        items += list_item(it, sid)
    out = items[0]
    for x in items[1:]:
        out += (" " if x.startswith("và ") else ", ") + x
    return cap(out) + "."


LIST_SIDS = {f"1-{i}" for i in range(587, 594)}

# =========================================================================================
# 7. Line dispatch, render, build
# =========================================================================================


def translate_line(line, sid=""):
    if line in H:
        return H[line]
    if line.startswith("Tattha katamaṃ sabbaṃ rūpaṃ? ") or line.startswith("Sabbaṃ rūpaṃ "):
        return ekaka_vi(line)
    if line.startswith("Atthi rūpaṃ ") or line.startswith("Yaṃ taṃ rūpaṃ "):
        return sentences_vi(line, sid)
    if sid in LIST_SIDS:
        return list_vi(line, sid)
    raise KeyError("line: " + line[:80])


def render(segs):
    blocks = []
    for sid, plines in segs:
        vlines = []
        for p in plines:
            v = unicodedata.normalize("NFC", cap(translate_line(p, sid)))
            B.check_vi(v)
            assert len(p) - len(p.lstrip("#")) == len(v) - len(v.lstrip("#")), sid
            assert p.count("–") + p.count("—") == v.count("–"), ("dash", sid, p[:60], v[:60])
            assert p.count("…pe…") <= v.count("…"), ("pe", sid)
            assert p.endswith("?") == v.endswith("?"), ("question", sid)
            assert v.endswith(".") or v.endswith("–") or v.startswith("#"), ("stop", sid, v[-40:])
            assert "  " not in v and " ," not in v and ",," not in v and "..." not in v and " ;" not in v, (
                "spacing", sid, v)
            assert "đau khổ" not in v and "khổ đau" not in v and "là là" not in v, sid
            vlines.append(v)
        vlines[-1] += f" ^{sid}"
        blocks.append("\n".join(vlines))
    return blocks


def check_earlier_unchanged():
    """Importing 2-05 (and through it 2-04 … 2-01) must leave their outputs exactly as finished."""
    E.check_earlier_unchanged()
    text, _ = E.build()
    assert unicodedata.normalize("NFC", text) == (S.OUT / "2-05-cittuppadakandam.md").read_bytes().decode("utf-8")
    print("2-05: rebuilt in memory, byte-identical to the finished file")


def build():
    segs = B.segments(PALI)
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    L = ["# pi-1 Vietnamese rails: new formulas of 3-01", "",
         "Generated by build_rails_3-01_vi.py from its fixed strings; import that file instead of retyping "
         "(MATTER_ADJ, MATTER_NOUN, GEN, HEADS, mpred, pred_expr, mattr, EKAKA, EKAKA_MEVA, VINN_ATTR, VINN_PRED, "
         "CLASS, H). Strings already in vi-rails-formulas.md or the chapter-2 notes are not repeated. Matrix items "
         "keep the 1-matika wording exactly, said of «vật chất» (singular). Format: Pāli = tiếng Việt.", "",
         "## Frames", "",
         f"rūpaṃ (matter) = {RUPA}",
         f"Atthi rūpaṃ X, atthi rūpaṃ Y. = Có {KIND} {RUPA} attr(X), có {KIND} {RUPA} attr(Y).",
         f"Yaṃ taṃ rūpaṃ A, taṃ X. = {cap(RUPA)} nào pred(A) thì pred(X).",
         f"Yaṃ taṃ rūpaṃ A, taṃ atthi X, atthi Y. = {cap(RUPA)} nào pred(A) thì có {KIND} pred(X), "
         f"có {KIND} pred(Y).",
         "attr(X) = pred(X), except upādā: attr «phái sinh», pred «là phái sinh» (as 1-matika)",
         "Noun run «X…pe… Y…pe… Z» = «là X… Y… Z»; negated «na X…pe… na Y» = «không phải là X… không phải là Y»",
         f"Genitive run «G1…pe… G2…pe… G3 vatthu» = «là {VATTHU} của G1… của G2… của G3» "
         f"(na vatthu «không phải là {VATTHU} của …», ārammaṇaṃ «là đối tượng của …», nārammaṇaṃ "
         "«không phải là đối tượng của …»)",
         f"X-vidhena rūpasaṅgaho – = {SANGAHO} {BY} N –",
         f"Evaṃ X-vidhena rūpasaṅgaho. = Như vậy là {SANGAHO[0].lower()}{SANGAHO[1:]} {BY} N.",
         f"Tattha katamaṃ sabbaṃ rūpaṃ? = {Q_SAB}",
         f"{SAB_DEF_P} = {SAB_DEF}",
         f"idaṃ vuccati X = đó được gọi là X",
         f"Sabbaṃ rūpaṃ X, Y, … = {cap(SAB)} pred(X){EKAKA_SEP}pred(Y){EKAKA_SEP}… (items joined with «{EKAKA_SEP.strip()}»)",
         f"X-meva (^1-594) = {SURE} pred(X); bare adjectives (abyākataṃ, parittaṃ) = {SURE} là pred(X)",
         f"{UPP_MEVA_P} = {UPP_MEVA_V}",
         f"yañca rūpaṃ X = và {KIND} {RUPA} attr(X)",
         f"na indriyaṃ rūpaṃ atthi X, atthi Y = {RUPA} {mattr('na indriyaṃ')}: có {KIND} pred(X), có {KIND} pred(Y)",
         f"X-viññeyyaṃ rūpaṃ = {RUPA} mà X có thể nhận biết (stand-alone pred: có thể được X nhận biết)",
         f"rūpaṃ [rūpiyaṃ (sī.)] (^1-584) = {EKAKA['rūpaṃ']} {RUPIYA_V}",
         "", "## The statement ^1-583", "",
         f"{U583_P} = {U583_V}",
         f"Kusalākusalānaṃ dhammānaṃ vipākā = {RESULT_OF}",
         f"ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā = những hiện tượng {E.KIRIYA_V}",
         f"sabbañca rūpaṃ = {SAB}",
         f"asaṅkhatā ca dhātu = và yếu tố {P['asaṅkhatā']}",
         "", "## Predicates of matter: adjectives (pred; attr where it differs)", ""]
    for k, v in MATTER_ADJ.items():
        L.append(f"{k} = {v}" + (f" | attr: {ATTR_OVERRIDE[k]}" if k in ATTR_OVERRIDE else ""))
    for k in VINN:
        L.append(f"{k} = {VINN_PRED[k]} | attr: {VINN_ATTR[k]}")
    L += ["", "## Predicates of matter: nouns (X = là N; na X = không phải là N; rūpassa na X = không phải là N)", ""]
    for k, v in MATTER_NOUN.items():
        L.append(f"{k} = là {v} | na: không phải là {v}")
    L += ["", "## Predicates of matter: genitive + vatthu / ārammaṇaṃ", ""]
    for g, v in GEN.items():
        for h in ("vatthu", "na vatthu", "ārammaṇaṃ", "nārammaṇaṃ"):
            L.append(f"{g} {h} = {mpred(g + ' ' + h)}")
    L += ["", "## Predicates of «Sabbaṃ rūpaṃ» (^1-584) and their -meva forms (^1-594)", ""]
    for k, v in EKAKA.items():
        L.append(f"{k} = {v} | {meva_key(k)} = {EKAKA_MEVA[meva_key(k)]}")
    L += ["", "## Headings and closing lines", ""]
    for k, v in H.items():
        if k != U583_P:
            L.append(f"{k} = {v}")
    L += ["", "## Source slips (rendered as meant)", ""]
    for sid, note in dict.fromkeys(SLIPS):
        L.append(f"^{sid}: {note}")
    L += ["", "## Termbase notes", "",
          "vatthu (cakkhusamphassassa vatthu …): no entry; closest sibling vatthūni «chỗ dựa» = «chỗ dựa»",
          "dūre / santike: no entry = «ở xa» / «ở gần»",
          "Diṭṭhaṃ: no entry = «được thấy» (as sutaṃ «được nghe», mutaṃ «được cảm nhận», viññātaṃ «được nhận biết»)",
          "cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ, kāyindriyaṃ: no entry, built from the members "
          "= «năng lực mắt / tai / mũi / lưỡi / thân»",
          f"Kusalākusalānaṃ dhammānaṃ vipākā (^1-583): vipākā «quả của nghiệp»; the genitive names the cause, "
          f"written «{RESULT_OF}»",
          "jarābhibhūtaṃ: built from jarā «sự lão hóa» + abhibhūtaṃ «bị … chế ngự» = «bị sự lão hóa chế ngự»",
          "sukhasamphassaṃ / dukkhasamphassaṃ: samphassaṃ «tiếp xúc» + sukha (bodily) «dễ chịu» / dukkha (bodily "
          "pain, APPROVED) «khó chịu» = «khi tiếp xúc thì dễ chịu / khó chịu»",
          "na savitakkasavicāraṃ, na avitakkavicāramattaṃ, no apariyāpannaṃ: the negation of a whole matrix item "
          f"= «{NOT_KIND} …» + the 1-matika wording"]
    (HERE / "notes-3-01.md").write_text(unicodedata.normalize("NFC", "\n".join(L) + "\n"), encoding="utf-8",
                                        newline="\n")
    print("wrote", HERE / "notes-3-01.md")


def main():
    text, n = build()
    check_earlier_unchanged()
    OUT.write_text(unicodedata.normalize("NFC", text), encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
    notes()


if __name__ == "__main__":
    main()
