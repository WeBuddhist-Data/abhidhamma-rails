"""Build the Vietnamese plain zero-shot of pi-1 part 3-01 (Rūpakaṇḍa: Uddeso, Mātikā, Ekakaniddeso; ^1-2-0 … ^1-594).

usage: python -I -X utf8 build_3-01_vi.py      (checks, then writes the part)

Importing this file does NOT build anything.
Method: the approved builders are imported unchanged (build_matika_vi = M, build_ch2_01_sample_vi = C,
build_2-01_2-02_vi = B, build_2-03_vi = D, build_2-04_vi = E, build_2-05_vi = F). Sentence-level translation with
fixed predicate strings (structure as ../pi-1-ru/build_3-01_ru.py and ../pi-1-ru/ref/en_build_3-01.py), so every
repeat is byte-identical. Every classifying predicate that is a matrix item is taken from M.PRED (or M.BARE inside
«thuộc về …»), never retyped: Vietnamese does not inflect, so «các hiện tượng X» -> «vật chất X» needs no change.

Reusable pieces: RF, ALL_RF, HEAD, CLOSE, N (nouns), P (predicates), GEN, pred(), s_atthi(), s_yam1(), s_yam2(),
EKAKA, EKAKA_V, NIDDESA, LISTS, translate_line().
"""
import importlib, pathlib, re, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402  (importing does not write)
import build_ch2_01_sample_vi as C  # noqa: E402  (importing does not write)
B = importlib.import_module("build_2-01_2-02_vi")  # importing does not write
D = importlib.import_module("build_2-03_vi")       # importing does not write
E = importlib.import_module("build_2-04_vi")       # importing does not write
F = importlib.import_module("build_2-05_vi")       # importing does not write

PART = "3-01-rupakandam.md"
PALI = B.PALI_DIR / PART
OUT = B.OUT_DIR / PART
TERMS = HERE / "vi-zeroshot-terms.md"
DASH, PE, ELL = B.DASH, B.PE, B.ELL
assert (DASH, PE, ELL) == ("–", "…pe…", "…")

RF = "vật chất"            # rūpa (matter), core terms
ALL_RF = "toàn bộ vật chất"  # sabbaṃ rūpaṃ
KIND = "loại vật chất"     # atthi rūpaṃ … = «có loại vật chất …»

# =========================================================================================
# 1. Headings and closing lines (verbatim from vi-zeroshot-terms.md, checked in check_headings())
# =========================================================================================
HEAD = {
    "### Rūpakaṇḍaṃ": "### Phần về vật chất",
    "#### Uddeso": "#### Phần nêu đề mục",
    "#### Mātikā": "#### " + M.H_MATIKA.split(" ", 1)[1],   # «Ma trận» (### Mātikā of 1-matika, one level down)
    "##### Ekakaṃ": "##### Phân loại theo nhóm một",
    "##### Dukaṃ": "##### Phân loại theo nhóm hai",
    "##### Tikaṃ": "##### Phân loại theo nhóm ba",
    "##### Catukkaṃ": "##### Phân loại theo nhóm bốn",
    "##### Pañcakaṃ": "##### Phân loại theo nhóm năm",
    "##### Chakkaṃ": "##### Phân loại theo nhóm sáu",
    "##### Sattakaṃ": "##### Phân loại theo nhóm bảy",
    "##### Aṭṭhakaṃ": "##### Phân loại theo nhóm tám",
    "##### Navakaṃ": "##### Phân loại theo nhóm chín",
    "##### Dasakaṃ": "##### Phân loại theo nhóm mười",
    "##### Ekādasakaṃ": "##### Phân loại theo nhóm mười một",
    "#### Rūpavibhatti": "#### Phân tích vật chất",
    "##### Ekakaniddeso": "##### Giải thích phân loại theo nhóm một",
}
assert HEAD["#### Mātikā"] == "#### Ma trận"


def check_headings():
    terms = {}
    for line in TERMS.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(#+ .+?) = (#+ .+)", line)
        if m:
            terms.setdefault(m.group(1), m.group(2))
    n = 0
    for p, v in HEAD.items():
        if p == "#### Mātikā":
            assert terms["### Mātikā"] == v[1:] == "### Ma trận"
        else:
            assert terms[p] == v, (p, terms.get(p), v)
        n += 1
    return n


# closing lines: heading + «.» (terms file rule); «Mātikā.» = «Ma trận.»
CLOSE = {p.split(" ", 1)[1] + ".": v.split(" ", 1)[1] + "." for p, v in HEAD.items()
         if p.split(" ", 1)[1] not in ("Rūpakaṇḍaṃ", "Uddeso", "Rūpavibhatti")}
assert CLOSE["Mātikā."] == "Ma trận." and CLOSE["Ekakaniddeso."] == "Giải thích phân loại theo nhóm một."
# «<N>vidhena rūpasaṅgaho –» / «Evaṃ <N>vidhena rūpasaṅgaho.»: the group words of the headings
WAYS = {"ekavidhena": "Ekakaṃ", "duvidhena": "Dukaṃ", "tividhena": "Tikaṃ", "catubbidhena": "Catukkaṃ",
        "pañcavidhena": "Pañcakaṃ", "chabbidhena": "Chakkaṃ", "sattavidhena": "Sattakaṃ",
        "aṭṭhavidhena": "Aṭṭhakaṃ", "navavidhena": "Navakaṃ", "dasavidhena": "Dasakaṃ",
        "ekādasavidhena": "Ekādasakaṃ"}
for k, h in WAYS.items():
    grp = HEAD["##### " + h].split("Phân loại ", 1)[1]          # «theo nhóm hai»
    CLOSE[f"Evaṃ {k} rūpasaṅgaho."] = f"Như vậy là phân loại {RF} {grp}."
    CLOSE[f"{k[0].upper() + k[1:]} rūpasaṅgaho {DASH}"] = f"Phân loại {RF} {grp} {DASH}"

# =========================================================================================
# 2. Predicates (subject «vật chất»); matrix items from M.PRED verbatim
# =========================================================================================
P = {}


def pair(pos_pali, neg_pali, pos_vi, neg_vi):
    assert pos_pali not in P and neg_pali not in P
    P[pos_pali], P[neg_pali] = pos_vi, neg_vi


def mpair(pos_pali, neg_pali, pos_key, neg_key):
    pair(pos_pali, neg_pali, M.PRED[pos_key], M.PRED[neg_key])


mpair("upādā", "no upādā", ("1-M2-67", "a"), ("1-M2-67", "b"))                       # là phái sinh
mpair("upādiṇṇaṃ", "anupādiṇṇaṃ", ("1-M2-68", "a"), ("1-M2-68", "b"))                # do nghiệp tạo ra
mpair("upādiṇṇupādāniyaṃ", "anupādiṇṇupādāniyaṃ", ("1-M1-4", "a"), ("1-M1-4", "b"))
mpair("sanidassanaṃ", "anidassanaṃ", ("1-M2-9", "a"), ("1-M2-9", "b"))               # thấy được
mpair("sappaṭighaṃ", "appaṭighaṃ", ("1-M2-10", "a"), ("1-M2-10", "b"))               # có tính va chạm
mpair("cittasamuṭṭhānaṃ", "na cittasamuṭṭhānaṃ", ("1-M2-60", "a"), ("1-M2-60", "b"))  # do tâm sinh ra
mpair("cittasahabhu", "na cittasahabhu", ("1-M2-61", "a"), ("1-M2-61", "b"))         # cùng tồn tại với tâm
mpair("cittānuparivatti", "na cittānuparivatti", ("1-M2-62", "a"), ("1-M2-62", "b"))  # vận hành theo tâm
mpair("ajjhattikaṃ", "bāhiraṃ", ("1-M2-66", "a"), ("1-M2-66", "b"))                  # thuộc phần bên trong
# not matrix items
pair("oḷārikaṃ", "sukhumaṃ", "ở dạng thô", "ở dạng vi tế")
pair("dūre", "santike", "ở xa", "ở gần")


def is_pair(pos_pali, neg_pali, noun):
    """noun predicates: «là N» / «không phải là N» (as the matrix «là gốc rễ» / «không phải là gốc rễ»)"""
    pair(pos_pali, neg_pali, f"là {noun}", f"không phải là {noun}")


SENSE = {"cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân"}
VINNANA = {"cakkhu": E.EYE, "sota": E.EAR, "ghāna": E.NOSE, "jivhā": E.TONGUE, "kāya": E.BODY}  # thức qua mắt …
assert VINNANA["kāya"] == "thức qua thân"
BASIS = "chỗ dựa cho"   # vatthu
OBJ = "đối tượng của"   # ārammaṇa
# fragments inside the '…pe…' chains (dative / genitive in the Pāli)
GEN = {"saññāya": C.N["saññā"], "cetanāya": C.N["cetanā"]}   # tri giác, chủ ý
assert (GEN["saññāya"], GEN["cetanāya"]) == ("tri giác", "chủ ý")
CONTACT = "sự tiếp xúc của"   # as «sự tiếp xúc của thân / của tâm» (2-04 strings)
assert f"sinh từ {CONTACT} thân" in E.S_KAYASUKHA
for s, e in SENSE.items():
    GEN[f"{s}samphassassa"] = f"{CONTACT} {e}"
    GEN[f"{s}samphassajāya vedanāya"] = f"{C.N['vedanā']} sinh từ {CONTACT} {e}"   # cảm giác sinh từ …
    GEN[f"{s}viññāṇassa"] = VINNANA[s]
    for what in ("samphassassa", "viññāṇassa"):
        g = GEN[s + what]
        is_pair(f"{s}{what} vatthu", f"{s}{what} na vatthu", f"{BASIS} {g}")
        is_pair(f"{s}{what} ārammaṇaṃ", f"{s}{what} nārammaṇaṃ", f"{OBJ} {g}")

AY = "lĩnh vực"   # āyatana in compounds (manāyatanaṃ = lĩnh vực ý)
assert B.NAME["manāyatanaṃ"] == f"{AY} ý"
YT = "yếu tố"     # dhātu (manodhātu = yếu tố ý)
NL = "năng lực"   # indriya (manindriyaṃ = năng lực ý, jīvitindriyaṃ = năng lực sống)
OBJS = {"rūpa": "hình sắc", "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm"}
# the object words of the sample's «lấy hình sắc, hoặc âm thanh, hoặc mùi, hoặc vị, hoặc vật xúc chạm …»
assert C.ARAMMANA.startswith("lấy " + ", hoặc ".join(OBJS.values()) + ", ")
N = {
    "cakkhāyatanaṃ": f"{AY} mắt", "sotāyatanaṃ": f"{AY} tai", "ghānāyatanaṃ": f"{AY} mũi",
    "jivhāyatanaṃ": f"{AY} lưỡi", "kāyāyatanaṃ": f"{AY} thân",
    "rūpāyatanaṃ": f"{AY} {OBJS['rūpa']}", "saddāyatanaṃ": f"{AY} {OBJS['sadda']}",
    "gandhāyatanaṃ": f"{AY} {OBJS['gandha']}", "rasāyatanaṃ": f"{AY} {OBJS['rasa']}",
    "phoṭṭhabbāyatanaṃ": f"{AY} {OBJS['phoṭṭhabba']}",
    "cakkhudhātu": f"{YT} mắt", "sotadhātu": f"{YT} tai", "ghānadhātu": f"{YT} mũi",
    "jivhādhātu": f"{YT} lưỡi", "kāyadhātu": f"{YT} thân",
    "rūpadhātu": f"{YT} {OBJS['rūpa']}", "saddadhātu": f"{YT} {OBJS['sadda']}",
    "gandhadhātu": f"{YT} {OBJS['gandha']}", "rasadhātu": f"{YT} {OBJS['rasa']}",
    "phoṭṭhabbadhātu": f"{YT} {OBJS['phoṭṭhabba']}",
    "cakkhundriyaṃ": f"{NL} mắt", "sotindriyaṃ": f"{NL} tai", "ghānindriyaṃ": f"{NL} mũi",
    "jivhindriyaṃ": f"{NL} lưỡi", "kāyindriyaṃ": f"{NL} thân",
    "itthindriyaṃ": f"{NL} nữ tính", "purisindriyaṃ": f"{NL} nam tính",
    "jīvitindriyaṃ": B.NAME["jīvitindriyaṃ"],                              # năng lực sống
    "kāyaviññatti": "sự biểu lộ bằng thân", "vacīviññatti": "sự biểu lộ bằng lời nói",
    "ākāsadhātu": f"{YT} không gian", "āpodhātu": f"{YT} nước",
    "pathavīdhātu": f"{YT} đất", "tejodhātu": f"{YT} lửa", "vāyodhātu": f"{YT} gió",
    # āhāra = dưỡng chất, pattern of «sự tiếp xúc trong vai trò dưỡng chất» (2-01)
    "kabaḷīkāro āhāro": "thức ăn trong vai trò dưỡng chất",
}
assert N["jīvitindriyaṃ"] == "năng lực sống"
assert B.NAME["phassāhāro"] == "sự tiếp xúc trong vai trò dưỡng chất"
# kasiṇa words: đất / nước / lửa / gió (2-02)
for k, w in (("pathavī", "đất"), ("āpo", "nước"), ("tejo", "lửa"), ("vāyo", "gió")):
    assert B.PH[k + "kasiṇaṃ"].endswith(" là " + w) and N[k + "dhātu"] == f"{YT} {w}", k
MAHABHUTA = "yếu tố cơ bản"     # mahābhūta (cattāro mahābhūtā = bốn yếu tố cơ bản)
INDRIYA = NL                     # indriyaṃ (the class word)
VINNATTI = "sự biểu lộ"          # viññatti
is_pair("indriyaṃ", "na indriyaṃ", INDRIYA)
is_pair("mahābhūtaṃ", "na mahābhūtaṃ", MAHABHUTA)
is_pair("viññatti", "na viññatti", VINNATTI)
for k in ("cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ", "rūpāyatanaṃ",
          "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ", "cakkhudhātu", "sotadhātu",
          "ghānadhātu", "jivhādhātu", "kāyadhātu", "rūpadhātu", "saddadhātu", "gandhadhātu", "rasadhātu",
          "phoṭṭhabbadhātu", "cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ",
          "itthindriyaṃ", "purisindriyaṃ", "jīvitindriyaṃ", "kāyaviññatti", "vacīviññatti", "ākāsadhātu",
          "āpodhātu", "kabaḷīkāro āhāro"):
    is_pair(k, "na " + k, N[k])
# rūpassa lahutā / mudutā / kammaññatā: the sample's words (lahutā … string, kāyalahutā = sự nhẹ nhàng của …)
RUPASSA = {"lahutā": C.N["kāyalahutā"].split(" của ")[0],          # sự nhẹ nhàng
           "mudutā": C.N["kāyamudutā"].split(" của ")[0],          # sự mềm mại
           "kammaññatā": C.N["kāyakammaññatā"].split(" của ")[0],  # sự dễ vận dụng
           "upacayo": "sự tăng trưởng",   # not «sự tích lũy» (ācaya, matrix triad 10)
           "santati": "sự liên tục",
           "jaratā": "sự lão hóa",
           "aniccatā": "tính vô thường"}
assert (RUPASSA["lahutā"], RUPASSA["mudutā"], RUPASSA["kammaññatā"]) == (
    "sự nhẹ nhàng", "sự mềm mại", "sự dễ vận dụng")
assert "sự tích lũy" in M.PRED[("1-M1-10", "a")]
for k, v in RUPASSA.items():
    is_pair(f"rūpassa {k}", f"rūpassa na {k}", f"{v} của {RF}")

RE_BASE = re.compile(r"^(\S+) (na )?vatthu$|^(\S+) (n)?ārammaṇaṃ$")
SEP = re.compile(r"(\s*…pe…\s*)")


def weave(items, seps):
    out = [items[0]]
    for s, it in zip(seps, items[1:]):
        out.append(s + it)
    return "".join(out)


def pred(a):
    """Predicate for a Pāli phrase; '…pe…' chains are written out from the fixed strings above,
    '…pe…' -> '…' with the Pāli spacing (a stray space before '…pe…' is mirrored)."""
    if PE not in a:
        return P[a]
    parts = SEP.split(a)
    items, seps = [x.strip() for x in parts[0::2]], [s.replace(PE, ELL) for s in parts[1::2]]
    m = RE_BASE.match(items[-1])
    if m:  # '… X-assa (na) vatthu' / '… X-assa (n)ārammaṇaṃ': one head noun, then the chain
        if m.group(1):
            key, neg, head = m.group(1), bool(m.group(2)), BASIS
        else:
            key, neg, head = m.group(3), bool(m.group(4)), OBJ
        frags = [GEN[x] for x in items[:-1]] + [GEN[key]]
        return ("không phải là " if neg else "là ") + head + " " + weave(frags, seps)
    negs = [x.startswith("na ") for x in items]
    keys = [x[3:] if x.startswith("na ") else x for x in items]
    if all(negs):  # 'na X…pe… na Y': «không phải là X… không phải là Y»
        return weave([f"không phải là {N[k]}" for k in keys], seps)
    assert not any(negs), a
    return "là " + weave([N[k] for k in keys], seps)


# =========================================================================================
# 3. Sentence frames
# =========================================================================================
RE_ATTHI = re.compile(r"^Atthi rūpaṃ (.+?), atthi rūpaṃ (.+?)\.$")
RE_YAM2 = re.compile(r"^Yaṃ taṃ rūpaṃ (.+?), taṃ atthi (.+?),? atthi (.+?)\.$")
RE_YAM1 = re.compile(r"^Yaṃ taṃ rūpaṃ (.+?), taṃ (?!atthi )(.+?)\.$")


def s_atthi(a, b):
    """Atthi rūpaṃ A, atthi rūpaṃ B."""
    return f"Có {KIND} {pred(a)}, có {KIND} {pred(b)}."


def s_yam1(a, p):
    """Yaṃ taṃ rūpaṃ A, taṃ P."""
    return f"{RF[0].upper() + RF[1:]} nào {pred(a)} thì {pred(p)}."


def s_yam2(a, p, q):
    """Yaṃ taṃ rūpaṃ A, taṃ atthi P, atthi Q."""
    return f"{RF[0].upper() + RF[1:]} nào {pred(a)} thì có loại {pred(p)}, có loại {pred(q)}."


# =========================================================================================
# 4. Uddeso ^1-583
# =========================================================================================
ABY = C.ABYAKATA
assert ABY == ("1-M1-1", "c")
UDDESO_P = ("Katame dhammā abyākatā? Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā "
            "apariyāpannā vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho, ye ca dhammā kiriyā "
            "neva kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ, asaṅkhatā ca dhātu – ime dhammā abyākatā.")
KHANDHAS = ", ".join(B.NAME[k] for k in ("vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"))
SPHERES = ", ".join(M.PRED[k] for k in (("1-M2-93", "a"), ("1-M2-94", "a"), ("1-M2-95", "a"), ("1-M2-96", "b")))
ASANKHATA_DHATU = f"{YT} {M.PRED[('1-M2-8', 'b')]}"   # yếu tố không do điều kiện tạo thành
assert ASANKHATA_DHATU == "yếu tố không do điều kiện tạo thành"
UDDESO_V = (f"{M.QUESTION(ABY)} Các quả của các hiện tượng thiện và bất thiện, {SPHERES}, tức là {KHANDHAS}; "
            f"và những hiện tượng {F.KIRIYA_V}; và {ALL_RF}; và {ASANKHATA_DHATU} {DASH} {M.ANSWER(ABY)}")
assert M.QUESTION(ABY) == "Những hiện tượng nào là không xác định về mặt đạo đức?"

# =========================================================================================
# 5. Ekaka ^1-584 and Ekakaniddeso ^1-594
# =========================================================================================
# (Pāli item, kind, value): kind "m" = M.PRED[key]; "in" / "notin" = «(không) thuộc về» + M.BARE[key]
# (the item is the negation of / membership in a matrix class); "t" = own text
EKAKA = [
    ("na hetu", "m", ("1-M2-1", "b")),
    ("ahetukaṃ", "m", ("1-M2-2", "b")),
    ("hetuvippayuttaṃ", "m", ("1-M2-3", "b")),
    ("sappaccayaṃ", "m", ("1-M2-7", "a")),
    ("saṅkhataṃ", "m", ("1-M2-8", "a")),
    ("rūpaṃ [rūpiyaṃ (sī.)]", "m", ("1-M2-11", "a")),
    ("lokiyaṃ", "m", ("1-M2-12", "a")),
    ("sāsavaṃ", "m", ("1-M2-15", "a")),
    ("saṃyojaniyaṃ", "m", ("1-M2-21", "a")),
    ("ganthaniyaṃ", "m", ("1-M2-27", "a")),
    ("oghaniyaṃ", "m", ("1-M2-33", "a")),
    ("yoganiyaṃ", "m", ("1-M2-39", "a")),
    ("nīvaraṇiyaṃ", "m", ("1-M2-45", "a")),
    ("parāmaṭṭhaṃ", "m", ("1-M2-51", "a")),
    ("upādāniyaṃ", "m", ("1-M2-70", "a")),
    ("saṃkilesikaṃ", "m", ("1-M2-76", "a")),
    ("abyākataṃ", "m", ("1-M1-1", "c")),
    ("anārammaṇaṃ", "m", ("1-M2-55", "b")),
    ("acetasikaṃ", "m", ("1-M2-57", "b")),
    ("cittavippayuttaṃ", "m", ("1-M2-58", "b")),
    ("nevavipākanavipākadhammadhammaṃ", "m", ("1-M1-3", "c")),
    ("asaṃkiliṭṭhasaṃkilesikaṃ", "m", ("1-M1-5", "b")),
    ("na savitakkasavicāraṃ", "notin", ("1-M1-6", "a")),
    ("na avitakkavicāramattaṃ", "notin", ("1-M1-6", "b")),
    ("avitakkaavicāraṃ", "m", ("1-M1-6", "c")),
    ("na pītisahagataṃ", "m", ("1-M2-90", "b")),
    ("na sukhasahagataṃ", "m", ("1-M2-91", "b")),
    ("na upekkhāsahagataṃ", "m", ("1-M2-92", "b")),
    ("neva dassanena na bhāvanāya pahātabbaṃ", "m", ("1-M1-8", "c")),
    # material form has no roots: it belongs to the class «có gốc rễ không cần dứt bỏ …» (triad 9 (c))
    ("neva dassanena na bhāvanāya pahātabbahetukaṃ", "in", ("1-M1-9", "c")),
    ("neva ācayagāmi na apacayagāmi", "m", ("1-M1-10", "c")),
    ("nevasekkhanāsekkhaṃ", "m", ("1-M1-11", "c")),
    ("parittaṃ", "m", ("1-M1-12", "a")),
    ("kāmāvacaraṃ", "m", ("1-M2-93", "a")),
    ("na rūpāvacaraṃ", "m", ("1-M2-94", "b")),
    ("na arūpāvacaraṃ", "m", ("1-M2-95", "b")),
    ("pariyāpannaṃ", "m", ("1-M2-96", "a")),
    ("no apariyāpannaṃ", "notin", ("1-M2-96", "b")),
    ("aniyataṃ", "m", ("1-M1-15", "c")),
    ("aniyyānikaṃ", "m", ("1-M2-97", "b")),
    ("uppannaṃ", "m", ("1-M1-17", "a")),
    ("chahi viññāṇehi viññeyyaṃ", "t", "có thể được sáu loại thức nhận biết"),
    ("aniccaṃ", "t", "là vô thường"),
    ("jarābhibhūtaṃ", "t", f"bị {RUPASSA['jaratā']} chế ngự"),   # jarā as jaratā; abhibhū = chế ngự (2-02)
]
VAR_RUPIYA = M.V("p", "Sī.", "rūpiyaṃ")


def ekaka_vi(kind, val):
    if kind == "m":
        return M.PRED[val]
    if kind == "in":
        return "thuộc về " + M.BARE[val]
    if kind == "notin":
        return "không thuộc về " + M.BARE[val]
    return val


EKAKA_V = [(p, ekaka_vi(k, v) + (VAR_RUPIYA if p.startswith("rūpaṃ [") else "")) for p, k, v in EKAKA]
assert dict(EKAKA_V)["na hetu"] == "không phải là gốc rễ"
assert dict(EKAKA_V)["rūpaṃ [rūpiyaṃ (sī.)]"] == "thuộc vật chất [dị bản (Sī.): rūpiyaṃ]"

MAHA4 = f"bốn {MAHABHUTA}"   # cattāro mahābhūtā / catunnaṃ mahābhūtānaṃ
EKAKA_HEAD_P = ("Tattha katamaṃ sabbaṃ rūpaṃ? Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – "
                "idaṃ vuccati sabbaṃ rūpaṃ. ")
EKAKA_HEAD_V = (f"Ở đây, {ALL_RF} là gì? {MAHA4[0].upper() + MAHA4[1:]} và {RF} phái sinh từ {MAHA4} {DASH} "
                f"đây được gọi là {ALL_RF}. ")
EKAKA_P = EKAKA_HEAD_P + "Sabbaṃ rūpaṃ " + ", ".join(p for p, _, _ in EKAKA) + "."
# items separated by «;» because some of them contain commas of their own
ALL_RF_C = ALL_RF[0].upper() + ALL_RF[1:]
EKAKA_LIST_V = f"{ALL_RF_C} " + "; ".join(v for _, v in EKAKA_V) + "."
EKAKA_V_LINE = EKAKA_HEAD_V + EKAKA_LIST_V

EMPH = "chắc chắn"   # the emphatic '-meva' of ^1-594


def meva(p):
    p = re.sub(r" \[.*?\]", "", p)
    return (p[:-1] if p.endswith("ṃ") else p) + "meva"


NIDDESA = []
for p, v in EKAKA_V:
    if p == "uppannaṃ":
        continue
    v0 = re.sub(r" \[.*?\]", "", v)
    if p == "chahi viññāṇehi viññeyyaṃ":  # one item in ^1-594: 'uppannaṃ chahi viññāṇehi viññeyyameva'
        NIDDESA.append(("uppannaṃ chahi viññāṇehi viññeyyameva",
                        f"khi {M.PRED[('1-M1-17', 'a')]}, {EMPH} {v0}"))   # khi đã sinh khởi, chắc chắn …
        continue
    NIDDESA.append((meva(p), f"{EMPH} {v0}"))
NIDDESA_P = "Sabbaṃ rūpaṃ " + ", ".join(p for p, _ in NIDDESA) + "."
NIDDESA_V = f"{ALL_RF_C} " + "; ".join(v for _, v in NIDDESA) + "."

# =========================================================================================
# 6. Lists ^1-586 … ^1-593
# =========================================================================================
WHICH = "mà {} có thể nhận biết"   # X-viññeyya, as the matrix «mà một loại thức nào đó có thể nhận biết»
assert M.PRED[("1-M2-13", "a")] == WHICH.format("một loại thức nào đó")
VINN5 = ", ".join(f"{RF} {WHICH.format(e)}" for e in SENSE.values())
VINN5 = VINN5[0].upper() + VINN5[1:]
MANO2 = (f"{RF} {WHICH.format(B.NAME['manodhātu'])}, {RF} {WHICH.format(B.NAME['manoviññāṇadhātu'])}")
INDR8 = ", ".join(N[k] for k in ("cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ",
                                 "itthindriyaṃ", "purisindriyaṃ", "jīvitindriyaṃ"))
INDR8 = INDR8[0].upper() + INDR8[1:]
AY10 = ", ".join(N[k] for k in ("cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ",
                                "rūpāyatanaṃ", "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ"))
AY10 = AY10[0].upper() + AY10[1:]
DHAMMAYATANA = B.NAME["dhammāyatanaṃ"]   # lĩnh vực đối tượng của ý
assert DHAMMAYATANA == "lĩnh vực đối tượng của ý"
INCL = M.PRED[("1-M2-96", "a")].split(" ", 2)[:2]   # «nằm trong» (pariyāpanna)
assert " ".join(INCL) == "nằm trong"
LISTS = {
    "Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ.":
        f"{RF[0].upper() + RF[1:]} được thấy, được nghe, được cảm nhận, được nhận biết.",
    "Pathavīdhātu, āpodhātu, tejodhātu, vāyodhātu, yañca rūpaṃ upādā.":
        f"{N['pathavīdhātu'][0].upper() + N['pathavīdhātu'][1:]}, {N['āpodhātu']}, {N['tejodhātu']}, "
        f"{N['vāyodhātu']}, và {KIND} {P['upādā']}.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "manoviññeyyaṃ rūpaṃ.":
        f"{VINN5}, {RF} {WHICH.format('ý')}.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        f"{VINN5}, {MANO2}.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ, manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        f"{VINN5}, có loại tiếp xúc dễ chịu, có loại tiếp xúc khó chịu, {MANO2}.",
    # the Pāli lacks a comma after jivhindriyaṃ in ^1-591 and ^1-592
    "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, "
    "jīvitindriyaṃ, yañca rūpaṃ na indriyaṃ.":
        f"{INDR8}, và {KIND} {P['na indriyaṃ']}.",
    "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, "
    "jīvitindriyaṃ, na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ.":
        f"{INDR8}, còn {RF} {P['na indriyaṃ']} thì có loại {P['sappaṭighaṃ']}, có loại {P['appaṭighaṃ']}.",
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, "
    "gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, yañca rūpaṃ anidassanaappaṭighaṃ "
    "[anidassanaṃ appaṭighaṃ (sī. syā.)] dhammāyatanapariyāpannaṃ.":
        f"{AY10}, và {KIND} {M.PRED[('1-M1-22', 'c')]}{M.V('s', 'Sī., Syā.', 'anidassanaṃ appaṭighaṃ')}, "
        f"{' '.join(INCL)} {DHAMMAYATANA}.",
}

WHOLE = {UDDESO_P: UDDESO_V, EKAKA_P: EKAKA_V_LINE, NIDDESA_P: NIDDESA_V}
WHOLE.update(LISTS)
WHOLE.update(CLOSE)


def tr_sentence(s):
    m = RE_ATTHI.match(s)
    if m:
        return s_atthi(m[1], m[2])
    m = RE_YAM2.match(s)
    if m:
        return s_yam2(m[1], m[2], m[3])
    m = RE_YAM1.match(s)
    if m:
        return s_yam1(m[1], m[2])
    raise KeyError(f"no rule for sentence: {s!r}")


def split_sentences(line):
    return re.split(r"(?<=\.) (?=(?:Atthi rūpaṃ|Yaṃ taṃ rūpaṃ) )", line)


def translate_line(line):
    if line in WHOLE:
        return WHOLE[line]
    return " ".join(tr_sentence(s) for s in split_sentences(line))


def build():
    out = []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            out.append("")
            continue
        m = re.match(r"^(.*?)(\s*\^[0-9A-Za-z-]+)?$", line)
        body, bid = m.group(1), m.group(2) or ""
        if body.startswith("#"):
            v = HEAD[body]
        else:
            v = translate_line(body)
            assert v.count(DASH) == body.count(DASH), (body, v)
            assert v.count("?") == body.count("?"), (body, v)
            assert ("[" in v) == ("[" in body), (body, v)
        out.append(v + bid)
    text = "\n".join(out).rstrip("\n") + "\n"
    assert "—" not in text and ":-" not in text and "pe…" not in text and "\n\n\n" not in text
    assert unicodedata.normalize("NFC", text) == text
    return text


if __name__ == "__main__":
    print("headings checked:", check_headings())
    t = build()
    OUT.write_text(t, encoding="utf-8", newline="\n")
    print("wrote", OUT, "segments", sum(1 for l in t.splitlines() if re.search(r"\^[0-9A-Za-z-]+$", l)))
