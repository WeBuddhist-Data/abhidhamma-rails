"""Build the Vietnamese plain zero-shot of pi-1 part 4-01 (Nikkhepakaṇḍa: summary of the triads and of the root,
short intermediate, taint, fetter and tie groups; ^1-3-0 … ^1-1155).

usage: python -I -X utf8 build_4-01_vi.py      (checks, then writes the part)

Importing this file does NOT build anything.
Method: the approved builders are imported unchanged (build_matika_vi = M, build_ch2_01_sample_vi = C, and through
build_3-01_vi = R and build_3-02_3-03_vi = X the 2-01 … 2-05 builders B, D, E, F). Segment-level translation with
fixed formula strings (structure as ../pi-1-ru/build_4-01_ru.py), so every repeat is byte-identical. Matrix items,
questions and answers come from M.QUESTION / M.ANSWER / M.BARE / M.PRED; the synonym strings of alobha, adosa,
paññā (sample), lobha, dosa, moha, diṭṭhi, vicikicchā (2-04), the kiriya phrase (2-05), the sphere list, the
aggregates, «toàn bộ vật chất», «yếu tố không do điều kiện tạo thành» (3-01) and the dhammāyatana class (3-02)
are taken from those builders, never retyped. ^1-987 is the 3-01 Uddeso line ^1-583 byte for byte.

Reusable pieces: SPH4, SPH3, K3, KA, KAB, VIP, SAS, KH3, KH4, KH4P, KH5, KH5P, SAMP_N, SAMP_1, KAMMA3, TADEK,
KIRIYA, SABBA, ANID, MAGGA3, MAGGA4, TE_TH, NANA4, ANNANA4, S_LOBHA(_V), S_DOSA, S_MOHA, S_DITTHI(_V), S_KANKHA,
S_KAMA, S_BHAVA(_V), ASAVA, FETTER(), GANTHA(), TQ(), TA(), QB(), ARB(), BHUMI(), SEGMENTS.
"""
import importlib, pathlib, re, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402  (importing does not write)
import build_ch2_01_sample_vi as C  # noqa: E402  (importing does not write)
R = importlib.import_module("build_3-01_vi")       # importing does not write
X = importlib.import_module("build_3-02_3-03_vi")  # importing does not write
B, D, E, F = R.B, R.D, R.E, R.F

PART = "4-01-nikkhepakandam.md"
PALI = B.PALI_DIR / PART
OUT = B.OUT_DIR / PART
TERMS = HERE / "vi-zeroshot-terms.md"
DASH, ELL = B.DASH, B.ELL
assert (DASH, ELL) == ("–", "…")


def cap(s):
    return s[0].upper() + s[1:]


def T(n, l):
    return (f"1-M1-{n}", l)


def P2(n, l):
    return (f"1-M2-{n}", l)


Q = M.QUESTION


def ANS(key):
    """'– ime dhammā X.'"""
    return f"{DASH} {M.ANSWER(key)}"


def QB(key, body):
    """'Katame dhammā X? <body> – ime dhammā X.'"""
    return f"{Q(key)} {body} {ANS(key)}"


def TQ(x):
    """'Tattha katamo/katamā/katamaṃ/katame X?' (3-01: «Ở đây, toàn bộ vật chất là gì?»)"""
    return f"Ở đây, {x} là gì?"


def TA(x):
    """'– ayaṃ/idaṃ vuccati X.' (3-01: idaṃ vuccati = đây được gọi là)"""
    return f"{DASH} đây được gọi là {x}."


def TPE(x):
    """'Tattha katamā X…pe… ayaṃ vuccati X.'"""
    return f"{TQ(x)[:-1]}{ELL} đây được gọi là {x}."


assert TQ("toàn bộ vật chất") in R.EKAKA_HEAD_V and "đây được gọi là toàn bộ vật chất." in R.EKAKA_HEAD_V

# =========================================================================================
# 1. Headings and closing lines (headings verbatim from vi-zeroshot-terms.md)
# =========================================================================================
HEAD = {
    "### Nikkhepakaṇḍaṃ": "### Phần tóm lược",
    "#### Tikanikkhepaṃ": "#### Tóm lược các bộ ba",
    "#### Dukanikkhepaṃ": "#### Tóm lược các bộ đôi",
}
GROUP_HEAD = {  # the matrix group headings (1-matika), same level
    "##### Hetugocchakaṃ": M.GROUPS["1-M-2-1-0"][0],
    "##### Cūḷantaradukaṃ": M.GROUPS["1-M-2-2-0"][0],
    "##### Āsavagocchakaṃ": M.GROUPS["1-M-2-3-0"][0],
    "##### Saṃyojanagocchakaṃ": M.GROUPS["1-M-2-4-0"][0],
    "##### Ganthagocchakaṃ": M.GROUPS["1-M-2-5-0"][0],
}
HEAD.update(GROUP_HEAD)
_KANDA = HEAD["### Nikkhepakaṇḍaṃ"].split(" ", 1)[1]                       # Phần tóm lược
# «Tikaṃ.» closes the summary of the triads: «Các bộ ba.» (matrix word «bộ ba», as the heading
# «Tóm lược các bộ ba»; in 3-01 the same word closes the rūpa classification «theo nhóm ba»)
END_TIKA = "Các " + M.H_TIKA.split(" ")[-2] + " " + M.H_TIKA.split(" ")[-1] + "."
assert END_TIKA == "Các bộ ba."
# «Nikkhepakaṇḍe paṭhamabhāṇavāro.»: terms-file pattern «Phần tụng đọc thứ hai của phần tóm lược.»
END_BHANA1 = C.END_BHANA1[:-1] + " của " + _KANDA[0].lower() + _KANDA[1:] + "."
assert END_BHANA1 == "Phần tụng đọc thứ nhất của phần tóm lược."


def check_headings():
    terms = {}
    for line in TERMS.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(#+ .+?) = (#+ .+)", line)
        if m:
            terms.setdefault(m.group(1), m.group(2))
    for p, v in HEAD.items():
        assert terms[p] == v, (p, terms.get(p), v)
    return len(HEAD)


# =========================================================================================
# 2. Recurring lists (from the earlier builders)
# =========================================================================================
SPHERE = {k: M.PRED[key] for k, key in (("kāma", ("1-M2-93", "a")), ("rūpa", ("1-M2-94", "a")),
                                         ("arūpa", ("1-M2-95", "a")), ("apar", ("1-M2-96", "b")))}
SPH4 = R.SPHERES                                   # kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā
SPH3 = ", ".join(SPHERE[k] for k in ("kāma", "rūpa", "arūpa"))
assert SPH4 == SPH3 + ", " + SPHERE["apar"]
KHN = {k: B.NAME[k] for k in ("vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho")}
RUPAKKHANDHA = "khối " + R.RF                      # rūpakkhandho = khối vật chất (khandha = khối, rūpa = vật chất)
KH4 = R.KHANDHAS                                   # khối cảm giác, khối tri giác, khối tạo tác, khối thức
KH3 = ", ".join(KHN[k] for k in ("saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"))
KH5 = f"{RUPAKKHANDHA}, {KH4}"
KH4P = f"{KHN['vedanākkhandho']}{ELL} {KHN['viññāṇakkhandho']}"   # vedanākkhandho…pe… viññāṇakkhandho
KH5P = f"{RUPAKKHANDHA}{ELL} {KHN['viññāṇakkhandho']}"            # rūpakkhandho…pe… viññāṇakkhandho
TL = "tức là"                                      # before the aggregates (3-01 ^1-583)
assert f", {TL} {KH4};" in R.UDDESO_V

K = {w: M.BARE[key].removeprefix(M.DH + " ") for w, key in (("kusala", C.KUSALA), ("akusala", C.AKUSALA),
                                                            ("abyākata", C.ABYAKATA))}
K3 = f"{M.DH} {K['kusala']}, {K['akusala']} và {K['abyākata']}"    # kusalākusalābyākatā dhammā
KA = f"{M.DH} {K['kusala']} và {K['akusala']}"                     # kusalākusalā dhammā
KAB = f"{M.DH} {K['kusala']} và {K['abyākata']}"                   # kusalābyākatā dhammā
VIP = f"các quả của {KA}"                                          # kusalākusalānaṃ dhammānaṃ vipākā
assert R.UDDESO_V.split("? ", 1)[1].startswith(cap(VIP) + ", " + SPH4 + ", ")
SAS = M.PRED[("1-M2-15", "a")]                                    # sāsavā = là đối tượng của ô nhiễm
KIRIYA = f"và những hiện tượng {F.KIRIYA_V}"   # ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā
ASD = R.ASANKHATA_DHATU                         # asaṅkhatā dhātu = yếu tố không do điều kiện tạo thành
SABBA = f"và {R.ALL_RF}; và {ASD}"              # sabbañca rūpaṃ, asaṅkhatā ca dhātu
assert f"; {KIRIYA}; {SABBA} {DASH}" in R.UDDESO_V
ANID = f"và {R.KIND} {X.EXTRA['anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ']}"
# yañca rūpaṃ (na) kammassa katattā (uppajjissati)
KATATTA = f"và {R.KIND} {X.QUALS['kammassa katattā']}"
NA_KATATTA = f"và {R.KIND} {X.QUALS['na kammassa katattā']}"
KATATTA_FUT = f"và {R.KIND} sẽ sinh khởi {X.KAMMA}"
assert X.QUALS["kammassa katattā"] == "sinh ra " + X.KAMMA

PRONOUN_N, PRONOUN_1 = "chúng", "nó"
SAMP_N = f"những gì {M.PRED[('1-M2-3', 'a')].replace(M.H, PRONOUN_N)}, {TL}"   # taṃsampayutto (plural antecedent)
SAMP_1 = f"những gì {M.PRED[('1-M2-3', 'a')].replace(M.H, PRONOUN_1)}, {TL}"   # (singular antecedent)
assert SAMP_N == "những gì gắn liền với chúng, tức là"
KAMMA3 = f"những gì do chúng sinh ra, {TL} nghiệp bằng thân, nghiệp bằng lời nói, nghiệp bằng ý"  # taṃsamuṭṭhānaṃ …
assert M.PRED[("1-M2-60", "a")] == "do tâm sinh ra"      # samuṭṭhāna = do … sinh ra
TOGETHER = "cùng hiện diện với chúng"                    # tad-ekaṭṭha
TADEK = f"và các phiền não {TOGETHER}"                   # tadekaṭṭhā ca kilesā
ROOTS_K = [C.N["alobho"], C.N["adoso"], C.N["amoho"]]
ROOTS_A = [E.NEW_NAMES["lobho"], E.NEW_NAMES["doso"], E.NEW_NAMES["moho"]]
HETU = M.H                                               # gốc rễ
ROOT_K, ROOT_A, ROOT_AB = C.ROOT, E.UNROOT, E.ABY_ROOT   # gốc rễ thiện / bất thiện / không xác định về mặt đạo đức
KUS_ROOTS = f"Ba {ROOT_K} {DASH} " + ", ".join(ROOTS_K)
AKUS_ROOTS = f"Ba {ROOT_A} {DASH} " + ", ".join(ROOTS_A)
AVASESA = cap(", ".join(ROOTS_A)) + " còn lại"           # avaseso lobho, doso, moho
AKUS_BLOCK = f"{AKUS_ROOTS}; {TADEK}; {SAMP_N} {KH4P}; {KAMMA3}"
MAGGA = "con đường"
PHALA = "thành quả"
MAGGA3 = f"Các {MAGGA} {SPHERE['apar']}, các {PHALA} của {MAGGA}, và {ASD}"   # apariyāpannā maggā ca, …
MAGGA4 = f"Bốn {MAGGA} {SPHERE['apar']}"                                    # cattāro maggā apariyāpannā
TE_TH = "Ngoại trừ những hiện tượng ấy,"                                    # te dhamme ṭhapetvā (avasesā)
LEFT = "còn lại"


def NO_X(key):
    """'Te dhamme ṭhapetvā avasesā kusalākusalābyākatā … apariyāpannā; vedanākkhandho…pe…; sabbañca rūpaṃ …'"""
    return QB(key, f"{TE_TH} {K3} {LEFT}, {SPH4}, {TL} {KH4P}; {SABBA}")


def NIYA(key):
    """'Sāsavā kusalākusalābyākatā dhammā kāmāvacarā, rūpāvacarā, arūpāvacarā; rūpakkhandho…pe…'"""
    return QB(key, f"{cap(K3)}, {SAS}, {SPH3}, {TL} {KH5P}")


# relative phrases of the pairs (tehi dhammehi ye dhammā …)
THOSE = "những hiện tượng ấy"
REL_SAH = f"Những hiện tượng có {THOSE} làm {HETU}"
REL_AHE = f"Những hiện tượng không có {THOSE} làm {HETU}"
REL_SAMP = f"Những hiện tượng gắn liền với {THOSE}"
REL_VIPP = f"Những hiện tượng không gắn liền với {THOSE}"
AMONG_SAH = f"Trong số {REL_SAH[0].lower() + REL_SAH[1:]}, ngoại trừ {THOSE},"
AMONG_SAMP = f"Trong số {REL_SAMP[0].lower() + REL_SAMP[1:]}, ngoại trừ {THOSE},"
AMONG_NIYA = f"Trong số những hiện tượng là đối tượng của {THOSE}, ngoại trừ {THOSE},"


def AMONG_NIYA_SEG(key):
    """'Tehi dhammehi ye dhammā sāsavā (saṃyojaniyā, ganthaniyā), te dhamme ṭhapetvā avasesā sāsavā …'"""
    return QB(key, f"{AMONG_NIYA} {K3} {LEFT}, {SAS}, {SPH3}, {TL} {KH5P}")


def VIPP_SAS(key):
    """'Tehi dhammehi ye dhammā vippayuttā sāsavā kusalākusalābyākatā dhammā …; rūpakkhandho…pe…'"""
    return QB(key, f"{cap(K3)}, không gắn liền với {THOSE}, {SAS}, {SPH3}, {TL} {KH5P}")


# =========================================================================================
# 3. Frames of the triads
# =========================================================================================
def BHUMI(level, *spheres):
    """'<X>bhūmiyaṃ kāmāvacare, rūpāvacare, …' = «Ở cấp độ <có X>, thuộc cõi dục lạc, …»"""
    return f"Ở cấp độ {level}, " + ", ".join(SPHERE[s] for s in spheres)


EXCEPT = "ngoại trừ"   # ṭhapetvā (2-01)
FEEL = {l: M.PRED[T(2, l)].removeprefix("gắn liền với ") for l in "abc"}   # cảm giác dễ chịu / khó chịu / …
assert FEEL["a"] == "cảm giác dễ chịu"
ACC7 = {l: M.PRED[T(7, l)] for l in "abc"}                                  # có sự hân hoan đi kèm …
PITI, SUKHA, UPEKKHA = C.N["pīti"], C.N["sukhaṃ"], B.NAME["upekkhā"]
assert ACC7["a"] == f"có {PITI} đi kèm" and ACC7["c"] == f"có {UPEKKHA} đi kèm"
VIT, VIC = C.N["vitakko"], C.N["vicāro"]


def ARB(obj):
    """'<obj> ārabbha ye uppajjanti cittacetasikā dhammā' (ārabbha as the sample's «… làm đối tượng»)"""
    return f"Tâm và các yếu tố đồng hành với tâm sinh khởi khi lấy {obj} làm đối tượng"


ARIYAMAGGA = f"{MAGGA} cao quý"                     # ariyamagga
ARIYA = f"Ở người có được {ARIYAMAGGA},"           # ariyamaggasamaṅgissa
FIVE = ", ".join([R.RF, C.N["vedanā"], C.N["saññā"], "các sự tạo tác", "thức"])   # rūpaṃ, vedanā, … viññāṇaṃ
UPP_POS = ["đã sinh ra", "đã thành", "đã sinh thành", "đã phát sinh", "đã phát sinh rõ rệt", "đã hiện ra",
           M.PRED[T(17, "a")], M.PRED[T(17, "a")] + " trọn vẹn", "đã trỗi dậy", "đã trỗi dậy trọn vẹn"]
assert UPP_POS[6] == "đã sinh khởi"
UPP_NEG = [w.replace("đã ", "chưa ", 1) for w in UPP_POS]
assert UPP_NEG[6] == M.PRED[T(17, "b")] == "chưa sinh khởi"
ATITA_L = [M.PRED[T(18, "a")], "đã chấm dứt", "đã mất đi", "đã biến đổi", "đã biến mất", "đã biến mất hoàn toàn",
           "đã mất đi sau khi sinh khởi"]


def UPP(words, pred, part):
    """'Ye dhammā <words> <pred> <pred>aṃsena saṅgahitā, rūpaṃ, vedanā, …'"""
    return f"Những hiện tượng {', '.join(words)}, {pred}, được xếp vào phần {part}"


OWN = "vốn ở bên trong, riêng từng người, cố hữu, thuộc về cá nhân, " + M.PRED[P2(68, "a")]   # … upādiṇṇā
AY = R.N
AY9 = ", ".join(AY[k] for k in ("cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ",
                                "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ"))
AY_PE = f"{cap(AY['cakkhāyatanaṃ'])}{ELL} {AY['phoṭṭhabbāyatanaṃ']}"     # cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ
MAHA = f"{cap(R.MAHA4)} và {R.RF} phái sinh từ {R.MAHA4}"   # cattāro ca mahābhūtā catunnañca … upādāya rūpaṃ
assert MAHA in R.EKAKA_HEAD_V

# =========================================================================================
# 4. Defilements and synonym strings
# =========================================================================================
YO = "Bất cứ điều gì là"                                   # yo / yā / yaṃ S – ayaṃ vuccati X
EVA = "bất cứ điều gì thuộc loại như vậy, tức là"          # yo / yā / yaṃ evarūpo / evarūpā / evarūpaṃ S


def join(items):
    return ", ".join(w + v for w, v in items)


SILA_N = "sự hiểu sai lệch về giới hạnh và nghi thức"    # sīlabbataparāmāsa (parāmāsa = sự hiểu sai lệch)
assert SILA_N.startswith(M.PARA)
SAKKAYA = "quan điểm về tự ngã"                           # sakkāyadiṭṭhi
VICI = E.NEW_NAMES["vicikicchā"]                          # sự hoài nghi
THREE_FETTERS = f"Ba xiềng xích {DASH} {SAKKAYA}, {VICI}, {SILA_N}"

S_ALOBHA, S_PANNA = C.S_ALOBHA, C.S_PANNA
S_PANNA_MAGGA = D.compose(
    "paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā "
    "paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
    "amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ")
assert S_PANNA_MAGGA == f"{S_PANNA}, {D.TOKENS['dhammavicayasambojjhaṅgo']}, {D.MAGGA}"

# adosa with mettā (^1-1062) and the abbreviated form (^1-1075): the sample's adosa words
_AD = C.WL["adoso"]
_METTA = ["lòng từ ái", "sự khởi lòng từ ái", "trạng thái khởi lòng từ ái",          # metti … (mettā = lòng từ ái)
          "lòng thương mến", "sự khởi lòng thương mến", "trạng thái khởi lòng thương mến",  # anuddā …
          "sự mong muốn điều lợi ích", "lòng thương xót"]                             # hitesitā, anukampā
S_ADOSA_METTA = ", ".join(_AD[:3] + _METTA + _AD[3:])
S_ADOSA_PE = ", ".join(_AD[:3]) + ELL + " " + ", ".join(_AD[3:])
assert len(_AD) == 7 and _AD[3] == C.N["abyāpādo"]

# knowledge / non-knowledge of the truths (amoha, moha, avijjā); dukkha (truth) = khổ đau
TRUTH_OBJ = ["khổ đau", "sự phát sinh của khổ đau", "sự chấm dứt khổ đau",
             "cách thực hành dẫn đến sự chấm dứt khổ đau", "quá khứ", "tương lai", "cả quá khứ lẫn tương lai",
             "quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện"]
NANA4 = ", ".join(f"hiểu biết về {o}" for o in TRUTH_OBJ)
ANNANA4 = ", ".join(f"{E.W_MOHA[0]} về {o}" for o in TRUTH_OBJ)   # aññāṇaṃ = sự không biết
assert "sự sinh khởi tùy thuộc vào điều kiện" in M.BARE[P2(122, "b")]
S_MOHA = ", ".join(E.W_MOHA)

# lobha (^1-1065 with the variant brackets; ^1-1141 without)
LOBHA_ITEMS = [
    ("sự tham đắm", ""), (E.W_LOBHA[3], ""), ("sự chiều theo", ""), ("sự xuôi theo", ""), ("sự thích thú", ""),
    ("sự tham đắm thích thú", M.V("s", "Sī.", "nandirāgo")), (f"{E.W_LOBHA[3]} của tâm", ""),
    ("sự mong muốn", ""), ("sự mê đắm", ""), ("sự đắm chìm", ""), ("sự thèm khát", ""),
    ("sự thèm khát mãnh liệt", ""), ("sự dính mắc", ""), ("vũng bùn", ""), ("sự xao xuyến", ""),
    ("sự huyễn hoặc", ""), ("kẻ sinh ra", ""), ("kẻ tạo thành", ""), ("kẻ khâu nối", M.V("s", "Sī.", "sibbanī")),
    ("kẻ giăng lưới", ""), ("dòng chảy", ""), ("sự vướng mắc khắp nơi", ""), ("sợi chỉ", ""),
    ("sự lan tràn", ""), ("kẻ thúc đẩy", M.V("s", "Sī., Syā.", "āyūhanī")), ("người bạn đồng hành", ""),
    ("sự mong cầu", ""), ("sợi dây dẫn đến hiện hữu", ""), ("rừng", ""), ("bụi rậm", ""), ("sự thân thiết", ""),
    ("sự luyến ái", ""), ("sự quyến luyến", ""), ("mối thân thuộc", ""), ("sự mong mỏi", ""), ("sự trông mong", ""),
    ("trạng thái trông mong", M.V("s", "Sī., Syā.", "āsiṃsanā āsiṃsitattaṃ")),
    ("sự mong mỏi hình sắc", ""), ("sự mong mỏi âm thanh", ""), ("sự mong mỏi mùi", ""), ("sự mong mỏi vị", ""),
    ("sự mong mỏi vật xúc chạm", ""), ("sự mong mỏi lợi lộc", ""), ("sự mong mỏi tài sản", ""),
    ("sự mong mỏi con cái", ""), ("sự mong mỏi mạng sống", ""),
    ("sự thèm thuồng", ""), ("sự thèm thuồng mãnh liệt", ""), ("sự thèm thuồng tột độ", ""), ("sự thèm thuồng", ""),
    ("sự khởi thèm thuồng", ""), ("trạng thái khởi thèm thuồng", ""), ("sự ham hố", ""), ("sự khởi ham hố", ""),
    ("trạng thái khởi ham hố", ""), ("sự xu nịnh", " [khác chính tả (Syā.): puñcikatā; (Sī.): pucchikatā]"),
    ("sự ham điều tốt đẹp", ""), ("sự tham đắm phi pháp", ""), ("sự tham lam bất chính", ""), ("sự ưa thích", ""),
    ("sự ham muốn", ""), ("sự mong ước", ""), ("sự ước ao", ""), ("sự mong ước mãnh liệt", ""),
    ("khao khát dục lạc", ""), (M.BARE[P2(110, "b")], ""), ("khao khát không còn hiện hữu", ""),
    ("khao khát hình sắc", ""), ("khao khát không hình sắc", ""), ("khao khát sự chấm dứt", ""),
    ("khao khát hình sắc", ""), ("khao khát âm thanh", ""), ("khao khát mùi", ""), ("khao khát vị", ""),
    ("khao khát vật xúc chạm", ""), ("khao khát đối tượng của ý", ""),
    ("dòng lũ", ""), ("ách", ""), ("nút thắt", ""), ("sự bám víu", ""), ("sự che lấp", ""), ("chướng ngại", ""),
    ("sự che đậy", ""), ("sự trói buộc", ""), ("sự làm ô uế", ""), (E.W_MOHA[20].removesuffix(" của vô minh"), ""),
    (E.W_MOHA[21].removesuffix(" của vô minh"), ""), ("dây leo", ""), ("sự bủn xỉn", ""),
    (f"{HETU} của khổ đau", ""), ("căn nguyên của khổ đau", ""), ("cội nguồn của khổ đau", ""),
    ("bẫy của Ma vương", ""), ("lưỡi câu của Ma vương", ""), ("lãnh địa của Ma vương", ""),
    ("dòng sông khao khát", ""), ("lưới khao khát", ""), ("dây xích khao khát", ""), ("biển khao khát", ""),
    (E.NEW_NAMES["abhijjhā"], ""), (E.NEW_NAMES["lobho"], ""), (ROOT_A, ""),
]
assert len(LOBHA_ITEMS) == 102, len(LOBHA_ITEMS)   # 103 Pāli words, «cittassa sārāgo» is one item
assert M.BARE[P2(110, "b")] == "khao khát được hiện hữu"
_LW = [w for w, _ in LOBHA_ITEMS]
assert _LW[_LW.index("sự làm ô uế") + 1:_LW.index("dây leo")] == ["khuynh hướng tiềm ẩn", "sự ám ảnh"]
VEVICCHA = _LW[_LW.index("dây leo") + 1]   # vevicchaṃ (also in the macchariya string)
assert VEVICCHA == "sự bủn xỉn"
S_LOBHA_V = join(LOBHA_ITEMS)
S_LOBHA = join((w, "") for w, _ in LOBHA_ITEMS)
assert S_LOBHA_V.count("[") == 5

# dosa (^1-1066, ^1-1120, ^1-1142): opening sentence + 15 words + the 2-04 dosa string
GRUDGE = "sự oán giận"   # āghāto
_HE = "Người ấy"


def _grudge(thought):
    return f"{GRUDGE} khởi lên khi nghĩ “{thought}”"


DOSA_OPEN = cap(", ".join([
    _grudge(f"{_HE} đã gây hại cho ta"), _grudge(f"{_HE} đang gây hại cho ta"), _grudge(f"{_HE} sẽ gây hại cho ta"),
    _grudge(f"{_HE} đã gây hại cho người mà ta yêu quý và ưa thích{ELL} đang gây hại{ELL} sẽ gây hại"),
    _grudge(f"{_HE} đã giúp ích cho người mà ta không yêu quý và không ưa thích{ELL} đang giúp ích{ELL} "
            "sẽ giúp ích"),
    f"hoặc {GRUDGE} khởi lên một cách vô cớ"])) + "."
_DOSA_HEAD = [f"{GRUDGE} của tâm", "sự phẫn uất", "sự ác cảm", E.W_DOSA[7], "sự nổi nóng", "sự nổi nóng dữ dội",
              "sự nổi nóng tột độ", E.W_DOSA[0], f"{E.W_DOSA[0]} dữ dội", f"{E.W_DOSA[0]} tột độ",
              f"{E.W_DOSA[3]} của tâm", f"{E.W_DOSA[0]} dữ dội trong ý", "sự giận dữ", "sự khởi giận",
              "trạng thái khởi giận"]
assert len(_DOSA_HEAD) == 15 and E.NEW_PH["paṭighasampayuttaṃ"].endswith("sự ác cảm")
S_DOSA = ", ".join(_DOSA_HEAD + E.W_DOSA)

# views
S_DITTHI = ", ".join(E.W_DITTHI)
S_DITTHI_V = ", ".join(w + (M.V("s", "Sī.", "diṭṭhivisūkāyitaṃ") if i == 4 else "")
                       for i, w in enumerate(E.W_DITTHI))
VIEWS = ["Thế giới là trường tồn", "Thế giới không trường tồn", "Thế giới là hữu hạn", "Thế giới là vô hạn",
         "Linh hồn và thân thể là một", "Linh hồn là một, thân thể là khác",
         "Như Lai còn tồn tại sau khi chết", "Như Lai không còn tồn tại sau khi chết",
         "Như Lai vừa còn tồn tại vừa không còn tồn tại sau khi chết",
         "Như Lai không phải còn tồn tại cũng không phải không còn tồn tại sau khi chết"]
TEN_VIEWS = ", hoặc ".join(f"“{v}”" for v in VIEWS)
ONLY_TRUE = "chỉ điều này là sự thật"                     # idameva saccaṃ
IDAM_VIEWS = "; hoặc ".join(f"“{v}, {ONLY_TRUE}, mọi điều khác đều sai”" for v in VIEWS)
WRONG_VIEW = E.NEW_NAMES["micchādiṭṭhi"]                  # quan điểm sai lầm
ALL_WRONG = f"mọi {WRONG_VIEW} đều là"                    # sabbāpi micchādiṭṭhi X

# identity view (^1-1007)
SELF = "tự ngã"   # attā
_AGGS = [R.RF, C.N["vedanā"], C.N["saññā"], "các sự tạo tác", "thức"]
_SAKK = [f"xem {a} là {SELF}, hoặc xem {SELF} là có {a}, hoặc xem {a} ở trong {SELF}, "
         f"hoặc xem {SELF} ở trong {a}." for a in _AGGS]
NOBLE, GOOD = "các bậc thánh", "những người chân chính"   # ariyā, sappurisā
SAKKAYA_OPEN = (
    f"Ở đời này, người phàm phu không được học hỏi, không gặp gỡ {NOBLE}, không thông thạo Giáo Pháp của {NOBLE}, "
    f"không được rèn luyện trong Giáo Pháp của {NOBLE}, không gặp gỡ {GOOD}, không thông thạo Giáo Pháp của {GOOD}, "
    f"không được rèn luyện trong Giáo Pháp của {GOOD}, " + " ".join([_SAKK[0]] + [f"Người ấy {s}" for s in _SAKK[1:]]))

# doubt (^1-1008, ^1-1123)
VICI_OPEN = "Người ta " + ", ".join(
    f"nghi ngờ và hoài nghi về {o}" for o in ["Bậc Đạo Sư", "Giáo Pháp", "Tăng đoàn", "sự tu học"] + TRUTH_OBJ[4:])
S_KANKHA = ", ".join(E.W_VICIKICCHA)

# rules and observances (^1-1009, ^1-1124, ^1-1143)
SILA_OPEN = ("Các sa-môn và bà-la-môn bên ngoài Giáo Pháp này cho rằng “Trong sạch nhờ giới hạnh, "
             "trong sạch nhờ nghi thức, trong sạch nhờ giới hạnh và nghi thức”")

# taints of sensual pleasure / existence (^1-1103, 1104, 1119, 1125)
KAMA = "dục lạc"   # kāma (2-01)
BHAVA = "hiện hữu"  # bhava (matrix «khao khát được hiện hữu», «quan điểm về sự hiện hữu»)


def _desire(x, taṇhā):
    return [f"ý muốn {x}", f"sự tham đắm {x}", f"sự thích thú {x}", taṇhā, f"sự luyến ái {x}",
            f"sự nóng bỏng của {x}", f"sự mê đắm {x}", f"sự đắm chìm trong {x}"]


S_KAMA = ", ".join(_desire(KAMA, f"khao khát {KAMA}"))
_BH = _desire(BHAVA, M.BARE[P2(110, "b")])
S_BHAVA = ", ".join(_BH)
S_BHAVA_V = ", ".join([_BH[0] + M.V("s", "Sī., Syā.", "bhavacchando")] + _BH[1:])
KAMESU = f"{YO[:-3]}, đối với các {KAMA}, là"             # yo kāmesu …
BHAVESU = f"{YO[:-3]}, đối với sự {BHAVA}, là"            # yo bhavesu …
assert KAMESU == "Bất cứ điều gì, đối với các dục lạc, là"

# conceit, envy, stinginess (^1-1121, 1126, 1127)
MANA_N = "sự kiêu mạn"   # māna (core terms)
MANA = (f"{cap(MANA_N)} “Ta hơn người”, {MANA_N} “Ta bằng người”, {MANA_N} “Ta kém người”. "
        f"{cap(EVA)} {MANA_N}, sự tự đánh giá mình, trạng thái tự đánh giá mình, sự tự cao, sự vênh vang"
        + M.V("s", "Syā.", "uṇṇati uṇṇāmo")
        + ", ngọn cờ, sự tự đề cao, sự mong muốn của tâm được giương cờ")
ISSA_N, MACCH_N = "sự ganh tị", "sự keo kiệt"
ISSA = (f"{YO} {ISSA_N} đối với lợi lộc, sự tôn vinh, sự kính trọng, sự quý trọng, sự đảnh lễ và sự cúng dường "
        "mà người khác nhận được, sự khởi ganh tị, trạng thái khởi ganh tị, sự đố kỵ, sự khởi đố kỵ, "
        "trạng thái khởi đố kỵ" + M.V("s", "Ka.", "ussuyā ussuyanā ussuyitattaṃ"))
_M = MACCH_N.removeprefix("sự ")
MACCH = (f"Năm loại {_M} {DASH} {_M} về chỗ ở, {_M} về gia đình, {_M} về lợi lộc, {_M} về lời khen, "
         f"{_M} về Giáo Pháp. {cap(EVA)} {MACCH_N}, sự khởi {_M}, trạng thái khởi {_M}, "
         f"{VEVICCHA}, sự hà tiện, sự bo bo, trạng thái khép chặt của tâm")

# group names
ASAVA_N = "ô nhiễm"   # āsava (core terms)
ASAVA = {"kāma": f"{ASAVA_N} {KAMA}", "bhava": f"{ASAVA_N} {BHAVA}", "diṭṭhi": f"{ASAVA_N} quan điểm",
         "avijjā": f"{ASAVA_N} {M.BARE[P2(110, 'a')]}"}
FETTER_N = "xiềng xích"
FETTER_GEN = {
    "kāmarāga": f"tham đắm {KAMA}", "paṭigha": "ác cảm", "māna": MANA_N.removeprefix("sự "),
    "diṭṭhi": "quan điểm", "vicikicchā": VICI.removeprefix("sự "), "sīlabbataparāmāsa": SILA_N.removeprefix("sự "),
    "bhavarāga": f"tham đắm {BHAVA}", "issā": ISSA_N.removeprefix("sự "), "macchariya": _M,
    "avijjā": M.BARE[P2(110, "a")],
}
assert E.W_DITTHI[6] == f"{FETTER_N} quan điểm"   # diṭṭhisaṃyojanaṃ inside the 2-04 diṭṭhi string


def FETTER(k):
    return f"{FETTER_N} {FETTER_GEN[k]}"


GANTHA_N = "nút thắt"
IDAM = f"sự cố chấp rằng “{ONLY_TRUE}”"   # idaṃsaccābhiniveso (abhinivesa = sự cố chấp, 2-04)
assert E.W_DITTHI[9] == "sự cố chấp"
GANTHA_GEN = {"abhijjhā": E.NEW_NAMES["abhijjhā"], "byāpāda": E.NEW_NAMES["byāpādo"],
              "sīlabbataparāmāsa": SILA_N, "idaṃsacca": IDAM}


def GANTHA(k):
    """X kāyagantho = «nút thắt của thân bằng X»"""
    return f"{GANTHA_N} của thân bằng {GANTHA_GEN[k]}"


# "X is both a Y and associated with a Y through Z"
_R4, _R5 = M.PRED[P2(4, "a")], M.PRED[P2(5, "a")]   # vừa là gốc rễ vừa có gốc rễ / … vừa gắn liền với gốc rễ
_PAIRS_LDM = [(ROOTS_A[0], ROOTS_A[2]), (ROOTS_A[2], ROOTS_A[0]), (ROOTS_A[1], ROOTS_A[2]), (ROOTS_A[2], ROOTS_A[1])]
_EACH = "đối với nhau, chúng"   # te aññamaññaṃ
ROOT_SAH = cap(", ".join(f"{a} {_R4} là {b}" for a, b in _PAIRS_LDM)) + "; " + ", ".join(ROOTS_K) + f", {_EACH} {_R4}"
ROOT_SAMP = cap(", ".join(f"{a} {_R5} là {b}" for a, b in _PAIRS_LDM)) + "; " + ", ".join(ROOTS_K) + f", {_EACH} {_R5}"


def _both(a, x, b):
    """'A B-ena x ceva x-sampayutto ca' = «A vừa là x vừa gắn liền với B» (B names the x already)"""
    return f"{a} vừa là {x} vừa gắn liền với {b}"


assert M.PRED[P2(18, "a")] == f"vừa là {ASAVA_N} vừa gắn liền với {ASAVA_N}"
ASAVA_PAIRS = cap(", ".join(_both(ASAVA[a], ASAVA_N, ASAVA[b])
                            for a, b in [("kāma", "avijjā"), ("avijjā", "kāma"), ("bhava", "avijjā"),
                                         ("avijjā", "bhava"), ("diṭṭhi", "avijjā"), ("avijjā", "diṭṭhi")]))
_F9 = ["kāmarāga", "paṭigha", "māna", "diṭṭhi", "vicikicchā", "sīlabbataparāmāsa", "bhavarāga", "issā", "macchariya"]
FETTER_PAIRS = cap(", ".join(_both(FETTER(a), FETTER_N, FETTER(b))
                             for x in _F9 for a, b in [(x, "avijjā"), ("avijjā", x)]))
GANTHA_PAIRS = cap(", ".join(_both(GANTHA(a), GANTHA_N, GANTHA(b))
                             for a, b in [("sīlabbataparāmāsa", "abhijjhā"), ("abhijjhā", "sīlabbataparāmāsa"),
                                          ("idaṃsacca", "abhijjhā"), ("abhijjhā", "idaṃsacca")]))

# the same X are X and objects of X (^1-1112, 1134, 1150)


def SAME(noun, key):
    return f"{Q(key)} Chính những {noun} ấy {M.PRED[key]}."


# =========================================================================================
# 5. Roots
# =========================================================================================
def ROOTS(n, kind):
    return f"{n} {kind}"


H3K, H3A, H3AB = f"ba {ROOT_K}", f"ba {ROOT_A}", f"ba {ROOT_AB}"
H9 = f"chín {HETU} {SPHERE['kāma']}"
H6R, H6AR, H6AP = f"sáu {HETU} {SPHERE['rūpa']}", f"sáu {HETU} {SPHERE['arūpa']}", f"sáu {HETU} {SPHERE['apar']}"


def these(x):
    """'Ime X.' (own line) / '– ime X.'"""
    return f"đây là {x}"


IN_KUSALA_VIP = f"trong các quả của {M.DH} {K['kusala']}"   # kusalānaṃ dhammānaṃ vipākato
IN_KIRIYA = f"trong {M.DH} {K['abyākata']}, mang tính chức năng"   # kiriyābyākatesu dhammesu
assert "Loại không xác định về mặt đạo đức, mang tính chức năng" in B.OUT_DIR.joinpath(
    "2-05-cittuppadakandam.md").read_text(encoding="utf-8")
ROOTS3K = cap(", ".join(ROOTS_K))

# =========================================================================================
# 6. kenaci viññeyyā (^1-1101): sense organs as in 3-01 («vật chất mà mắt có thể nhận biết»)
# =========================================================================================
KV_A, KV_B = P2(13, "a"), P2(13, "b")
_KV_B = M.PRED[KV_B].removeprefix("mà ")
KV_Q = f"Những hiện tượng nào {M.PRED[KV_A]}, {_KV_B}?"
KV_END = f"Đây là {M.BARE[KV_A]}, {_KV_B}."
assert R.WHICH.format("mắt") == "mà mắt có thể nhận biết"


def kenaci(pali_line):
    pairs = re.findall(r"Ye te dhammā (\w+)viññeyyā, na te dhammā (\w+)viññeyyā;", pali_line)
    assert len(pairs) == 20, pairs
    s = R.SENSE
    sents = [f"Những hiện tượng mà {s[a]} có thể nhận biết thì {s[b]} không thể nhận biết; còn những hiện tượng "
             f"mà {s[b]} có thể nhận biết thì {s[a]} không thể nhận biết." for a, b in pairs]
    return f"{KV_Q} {' '.join(sents)} {KV_END}"


# =========================================================================================
# 7. Segments in source order
# =========================================================================================
D1 = P2(1, "a")
SEGMENTS = [
    ("1-3-0", [HEAD["### Nikkhepakaṇḍaṃ"]]),
    ("1-3-1-0", [HEAD["#### Tikanikkhepaṃ"]]),
    ("1-985", [QB(T(1, "a"), f"{KUS_ROOTS}; {SAMP_N} {KH4}; {KAMMA3}")]),
    ("1-986", [QB(T(1, "b"), f"{AKUS_ROOTS}; {TADEK}; {SAMP_N} {KH4}; {KAMMA3}")]),
    ("1-987", [R.UDDESO_V]),   # = 3-01 ^1-583 (same Pāli but for the punctuation)
    ("1-988", [QB(T(2, "a"), f"{BHUMI('có ' + FEEL['a'], 'kāma', 'rūpa', 'apar')}, {EXCEPT} {FEEL['a']}; "
                             f"{SAMP_1} {KH3}")]),
    ("1-989", [QB(T(2, "b"), f"{BHUMI('có ' + FEEL['b'], 'kāma')}, {EXCEPT} {FEEL['b']}; {SAMP_1} {KH3}")]),
    ("1-990", [QB(T(2, "c"), f"{BHUMI('có ' + FEEL['c'], 'kāma', 'rūpa', 'arūpa', 'apar')}, {EXCEPT} {FEEL['c']}; "
                             f"{SAMP_1} {KH3}")]),
    ("1-991", [QB(T(3, "a"), f"{cap(VIP)}, {SPH4}, {TL} {KH4P}")]),
    ("1-992", [QB(T(3, "b"), f"{cap(KA)}, {SPH4}, {TL} {KH4P}")]),
    ("1-993", [QB(T(3, "c"), f"{cap(KIRIYA)}; {SABBA}")]),
    ("1-994", [QB(T(4, "a"), f"{cap(VIP)}, {SAS}, {SPH3}, {TL} {KH4P}; {KATATTA}")]),
    ("1-995", [QB(T(4, "b"), f"{cap(KA)}, {SAS}, {SPH3}, {TL} {KH4P}; {KIRIYA}; {NA_KATATTA}")]),
    ("1-996", [QB(T(4, "c"), MAGGA3)]),
    ("1-997", [QB(T(5, "a"), AKUS_BLOCK)]),
    ("1-998", [QB(T(5, "b"), f"{cap(KAB)}, {SAS}, {SPH3}, {TL} {KH5}")]),
    ("1-999", [QB(T(5, "c"), MAGGA3)]),
    ("1-1000", [QB(T(6, "a"), f"{BHUMI(M.PRED[T(6, 'a')], 'kāma', 'rūpa', 'apar')}, {EXCEPT} {VIT} và {VIC}; "
                              f"{SAMP_N} {KH4P}")]),
    ("1-1001", [QB(T(6, "b"), f"{BHUMI(M.PRED[T(6, 'b')], 'rūpa', 'apar')}, {EXCEPT} {VIC}; {SAMP_1} {KH4P}")]),
    ("1-1002", [QB(T(6, "c"), f"{BHUMI(M.PRED[T(6, 'c')], 'kāma', 'rūpa', 'arūpa', 'apar')}; {KH4P}; {SABBA}")]),
    ("1-1003", [QB(T(7, "a"), f"{BHUMI('có ' + PITI, 'kāma', 'rūpa', 'apar')}, {EXCEPT} {PITI}; {SAMP_1} {KH4P}")]),
    # «Sukhabhūmiyaṃ» = «Ở cấp độ có hạnh phúc» here (sukha as the factor of triad 7), «có cảm giác dễ chịu» at
    # ^1-988 (sukhā vedanā of triad 2), as the approved English («plane of happiness» / «of pleasant feeling»)
    ("1-1004", [QB(T(7, "b"), f"{BHUMI('có ' + SUKHA, 'kāma', 'rūpa', 'apar')}, {EXCEPT} {SUKHA}; {SAMP_1} {KH3}")]),
    ("1-1005", [QB(T(7, "c"), f"{BHUMI('có ' + UPEKKHA, 'kāma', 'rūpa', 'arūpa', 'apar')}, {EXCEPT} {UPEKKHA}; "
                              f"{SAMP_1} {KH3}")]),
    ("1-1006", [f"{Q(T(8, 'a'))} {THREE_FETTERS}."]),
    ("1-1007", [f"{TQ(SAKKAYA)} {SAKKAYA_OPEN} {cap(EVA)} {S_DITTHI_V} {TA(SAKKAYA)}"]),
    ("1-1008", [f"{TQ(VICI)} {VICI_OPEN}. {cap(EVA)} {S_KANKHA} {TA(VICI)}"]),
    ("1-1009", [f"{TQ(SILA_N)} {SILA_OPEN}; {EVA} {S_DITTHI} {TA(SILA_N)}"]),
    ("1-1010", [f"Ba {FETTER_N} này; {TADEK}; {SAMP_N} {KH4P}; {KAMMA3} {ANS(T(8, 'a'))}"]),
    ("1-1011", [QB(T(8, "b"), f"{AVASESA}; {TADEK}; {SAMP_N} {KH4P}; {KAMMA3}")]),
    ("1-1012", [QB(T(8, "c"), f"{cap(KAB)}, {SPH4}, {TL} {KH4P}; {SABBA}")]),
    ("1-1013", [f"{Q(T(9, 'a'))} {THREE_FETTERS}."]),
    ("1-1014", [TPE(SAKKAYA)]),
    ("1-1015", [TPE(VICI)]),
    ("1-1016", [TPE(SILA_N)]),
    ("1-1017", [f"Ba {FETTER_N} này; {TADEK}; {SAMP_N} {KH4P}; {KAMMA3} {ANS(T(9, 'a'))} "
                f"{THREE_FETTERS} {ANS(T(8, 'a'))} "
                f"{cap(', '.join(ROOTS_A))} {TOGETHER} {DASH} "
                f"{these(M.DH + ' là ' + HETU + ' cần dứt bỏ bằng ' + M.SEE)}. "
                f"{cap(TADEK)}; {SAMP_N} {KH4P}; {KAMMA3} {ANS(T(9, 'a'))}"]),
    ("1-1018", [f"{Q(T(9, 'b'))} {AVASESA} {DASH} {these(M.DH + ' là ' + HETU + ' cần dứt bỏ bằng ' + M.DEV)}. "
                f"{cap(TADEK)}; {SAMP_N} {KH4P}; {KAMMA3} {ANS(T(9, 'b'))}"]),
    ("1-1019", [QB(T(9, "c"), f"{TE_TH} {K3} {LEFT}, {SPH4}, {TL} {KH4}; {SABBA}")]),
    ("1-1020", [QB(T(10, "a"), f"{cap(KA)}, {SAS}, {SPH3}, {TL} {KH4P}")]),
    ("1-1021", [QB(T(10, "b"), MAGGA4)]),
    # the Pāli question reads «neva ācayagāmi na apacayagāmino»; the matrix question (triad 10 (c)) is used
    ("1-1022", [QB(T(10, "c"), f"{cap(VIP)}, {SPH4}, {TL} {KH4P}; {KIRIYA}; {SABBA}")]),
    ("1-1023", [QB(T(11, "a"), f"{MAGGA4}, và ba {PHALA} thấp hơn của đời sống sa-môn")]),
    ("1-1024", [QB(T(11, "b"), f"{cap(PHALA)} cao nhất{M.V('p', 'Syā.', 'uparimaṃ')}, {TL} {PHALA} A-la-hán")]),
    ("1-1025", [QB(T(11, "c"), f"{TE_TH} {K3} {LEFT}, {SPH3}, {TL} {KH4P}; {SABBA}")]),
    ("1-1026", [QB(T(12, "a"), f"Tất cả {K3}, {SPHERE['kāma']}, {TL} {KH5P}")]),
    ("1-1027", [QB(T(12, "b"), f"{cap(KAB)}, {SPHERE['rūpa']}, {SPHERE['arūpa']}, {TL} {KH4P}")]),
    ("1-1028", [QB(T(12, "c"), MAGGA3)]),
    ("1-1029", [QB(T(13, "a"), ARB(M.BARE[T(12, "a")]))]),
    ("1-1030", [QB(T(13, "b"), ARB(M.BARE[T(12, "b")]))]),
    ("1-1031", [QB(T(13, "c"), ARB(M.BARE[T(12, "c")]))]),
    ("1-1032", [QB(T(14, "a"), AKUS_BLOCK)]),
    ("1-1033", [QB(T(14, "b"), f"{cap(KAB)}, {SAS}, {SPH3}, {TL} {KH5P}")]),
    ("1-1034", [QB(T(14, "c"), MAGGA3)]),
    ("1-1035", [QB(T(15, "a"), f"Năm nghiệp có quả không gián đoạn, và {WRONG_VIEW} cố định")]),
    ("1-1036", [QB(T(15, "b"), MAGGA4)]),
    ("1-1037", [QB(T(15, "c"), f"{TE_TH} {K3} {LEFT}, {SPH4}, {TL} {KH4P}; {SABBA}")]),
    ("1-1038", [QB(T(16, "a"), ARB(ARIYAMAGGA))]),
    ("1-1039", [f"{Q(T(16, 'b'))} {ARIYA} {EXCEPT} các chi phần của {MAGGA}; {SAMP_N} {KH4P} {ANS(T(16, 'b'))} "
                f"{ARIYA} {C.N['sammādiṭṭhi']} vừa là {MAGGA} vừa là {HETU}, {EXCEPT} {C.N['sammādiṭṭhi']}, "
                f"{SAMP_1} {KH4P} {ANS(T(16, 'b'))} "
                f"{ARIYA} {', '.join(ROOTS_K)} {DASH} {these(M.DH + ' là ' + HETU + ' của ' + MAGGA)}. "
                f"{cap(SAMP_N)} {KH4P} {ANS(T(16, 'b'))}"]),
    ("1-1040", [f"{Q(T(16, 'c'))} Tâm và các yếu tố đồng hành với tâm sinh khởi khi lấy {ARIYAMAGGA} làm "
                f"yếu tố chủ đạo {ANS(T(16, 'c'))} "
                f"{ARIYA[:-1]} và đang tu tập {MAGGA} với sự thẩm xét làm yếu tố chủ đạo, {EXCEPT} sự thẩm xét; "
                f"{SAMP_1} {KH4P} {ANS(T(16, 'c'))}"]),
    ("1-1041", [QB(T(17, "a"), f"{UPP(UPP_POS, M.PRED[T(17, 'a')], M.PRED[T(17, 'a')])}, {TL} "
                               f"{FIVE.replace(R.RF, R.RF + M.V('p', 'nhiều ấn bản', 'rūpā'), 1)}")]),
    ("1-1042", [QB(T(17, "b"), f"{UPP(UPP_NEG, M.PRED[T(17, 'b')], M.PRED[T(17, 'b')])}, {TL} {FIVE}")]),
    ("1-1043", [QB(T(17, "c"), f"{cap(VIP)} có quả chưa chín muồi, {SPH4}, {TL} {KH4P}; {KATATTA_FUT}")]),
    ("1-1044", [QB(T(18, "a"), f"{UPP(ATITA_L, M.PRED[T(18, 'a')], 'quá khứ')}, {TL} {FIVE}")]),
    ("1-1045", [QB(T(18, "b"), f"{UPP(UPP_NEG, M.PRED[T(18, 'b')], 'tương lai')}, {TL} {FIVE}")]),
    ("1-1046", [QB(T(18, "c"), f"{UPP(UPP_POS, M.PRED[T(18, 'c')], 'hiện tại')}, {TL} {FIVE}")]),
    ("1-1047", [QB(T(19, "a"), ARB(M.BARE[T(18, "a")]))]),
    ("1-1048", [QB(T(19, "b"), ARB(M.BARE[T(18, "b")]))]),
    ("1-1049", [QB(T(19, "c"), ARB(M.BARE[T(18, "c")]))]),
    ("1-1050", [QB(T(20, "a"), f"Những hiện tượng của từng chúng sinh, {OWN}, {TL} {FIVE}")]),
    ("1-1051", [QB(T(20, "b"), f"Những hiện tượng của từng chúng sinh khác, từng người khác, {OWN}, {TL} {FIVE}")]),
    ("1-1052", [QB(T(20, "c"), "Cả hai loại ấy")]),
    ("1-1053", [QB(T(21, "a"), ARB(M.BARE[T(20, "a")]))]),
    ("1-1054", [QB(T(21, "b"), ARB(M.BARE[T(20, "b")]))]),
    ("1-1055", [QB(T(21, "c"), ARB(M.BARE[T(20, "c")]))]),
    ("1-1056", [QB(T(22, "a"), cap(AY["rūpāyatanaṃ"]))]),
    ("1-1057", [QB(T(22, "b"), cap(AY9))]),
    ("1-1058", [QB(T(22, "c"), f"{cap(KH4)}; {ANID}; và {ASD}"), END_TIKA]),
    # ---- pairs ----
    ("1-3-2-0", [HEAD["#### Dukanikkhepaṃ"]]),
    ("1-3-2-1-0", [GROUP_HEAD["##### Hetugocchakaṃ"]]),
    ("1-1059", [f"{Q(D1)} {cap(H3K)}, {H3A}, {H3AB}, {H9}, {H6R}, {H6AR}, {H6AP}."]),
    ("1-1060", [f"{TQ(H3K)} {ROOTS3K}."]),
    ("1-1061", [f"{TQ(ROOTS_K[0])} {YO} {S_ALOBHA} {TA(ROOTS_K[0])}"]),
    ("1-1062", [f"{TQ(ROOTS_K[1])} {YO} {S_ADOSA_METTA} {TA(ROOTS_K[1])}"]),
    ("1-1063", [f"{TQ(ROOTS_K[2])} {cap(NANA4)}, {EVA} {S_PANNA} {TA(ROOTS_K[2])}", f"{cap(these(H3K))}."]),
    ("1-1064", [f"{TQ(H3A)} {cap(', '.join(ROOTS_A))}."]),
    ("1-1065", [f"{TQ(ROOTS_A[0])} {YO} {S_LOBHA_V} {TA(ROOTS_A[0])}"]),
    ("1-1066", [f"{TQ(ROOTS_A[1])} {DOSA_OPEN} {cap(EVA)} {S_DOSA} {TA(ROOTS_A[1])}"]),
    ("1-1067", [f"{TQ(ROOTS_A[2])} {cap(ANNANA4)}, {EVA} {S_MOHA} {TA(ROOTS_A[2])}", f"{cap(these(H3A))}."]),
    ("1-1068", [f"{TQ(H3AB)} {ROOTS3K} {IN_KUSALA_VIP} hoặc {IN_KIRIYA} {DASH} {these(H3AB)}."]),
    ("1-1069", [f"{TQ(H9)} {cap(H3K)}, {H3A}, {H3AB} {DASH} {these(H9)}."]),
    ("1-1070", [f"{TQ(H6R)} {cap(H3K)}, {H3AB} {DASH} {these(H6R)}."]),
    ("1-1071", [f"{TQ(H6AR)} {cap(H3K)}, {H3AB} {DASH} {these(H6AR)}."]),
    ("1-1072", [f"{TQ(H6AP)} {cap(H3K)}, {H3AB} {DASH} {these(H6AP)}."]),
    ("1-1073", [f"{TQ(H3K)} {ROOTS3K}."]),
    ("1-1074", [f"{TQ(ROOTS_K[0])} {YO} {S_ALOBHA} {TA(ROOTS_K[0])}"]),
    ("1-1075", [f"{TQ(ROOTS_K[1])} {YO} {S_ADOSA_PE} {TA(ROOTS_K[1])}"]),
    ("1-1076", [f"{TQ(ROOTS_K[2])} {cap(NANA4)}, {EVA} {S_PANNA_MAGGA} {TA(ROOTS_K[2])}", f"{cap(these(H3K))}."]),
    ("1-1077", [f"{TQ(H3AB)} {ROOTS3K} {IN_KUSALA_VIP} {DASH} {these(H3AB)}. "
                f"{cap(H6AP)} này {ANS(D1)}"]),
    ("1-1078", [NO_X(P2(1, "b"))]),
    ("1-1079", [QB(P2(2, "a"), f"{REL_SAH}, {TL} {KH4P}")]),
    ("1-1080", [QB(P2(2, "b"), f"{REL_AHE}, {TL} {KH4P}; {SABBA}")]),
    ("1-1081", [QB(P2(3, "a"), f"{REL_SAMP}, {TL} {KH4P}")]),
    ("1-1082", [QB(P2(3, "b"), f"{REL_VIPP}, {TL} {KH4P}; {SABBA}")]),
    ("1-1083", [QB(P2(4, "a"), ROOT_SAH)]),
    ("1-1084", [QB(P2(4, "b"), f"{AMONG_SAH} {KH4P}")]),
    ("1-1085", [QB(P2(5, "a"), ROOT_SAMP)]),
    ("1-1086", [QB(P2(5, "b"), f"{AMONG_SAMP} {KH4P}")]),
    ("1-1087", [QB(P2(6, "a"), f"Những hiện tượng không phải là {HETU} nhưng có {THOSE} làm {HETU}, {TL} {KH4P}")]),
    ("1-1088", [QB(P2(6, "b"), f"Những hiện tượng không phải là {HETU} và không có {THOSE} làm {HETU}, {TL} {KH4P}; "
                               f"{SABBA}")]),
    ("1-3-2-2-0", [GROUP_HEAD["##### Cūḷantaradukaṃ"]]),
    ("1-1089", [QB(P2(7, "a"), f"Năm khối {DASH} {KH5}")]),
    ("1-1090", [QB(P2(7, "b"), cap(ASD))]),
    ("1-1091", [f"{Q(P2(8, 'a'))} Những hiện tượng nào {M.PRED[P2(7, 'a')]} thì chính những hiện tượng ấy "
                f"{M.PRED[P2(8, 'a')]}."]),
    ("1-1092", [f"{Q(P2(8, 'b'))} Hiện tượng nào {M.PRED[P2(7, 'b')]} thì chính hiện tượng ấy "
                f"{M.PRED[P2(8, 'b')]}."]),
    ("1-1093", [QB(P2(9, "a"), cap(AY["rūpāyatanaṃ"]))]),
    ("1-1094", [QB(P2(9, "b"), f"{AY_PE}; {KH4P}; {ANID}; và {ASD}")]),
    ("1-1095", [QB(P2(10, "a"), AY_PE)]),
    ("1-1096", [QB(P2(10, "b"), f"{cap(KH4P)}; {ANID}; và {ASD}")]),
    ("1-1097", [QB(P2(11, "a"), MAHA)]),
    ("1-1098", [QB(P2(11, "b"), f"{cap(KH4P)}; và {ASD}")]),
    ("1-1099", [QB(P2(12, "a"), f"{cap(K3)}, {SAS}, {SPH3}, {TL} {KH5P}")]),
    ("1-1100", [QB(P2(12, "b"), MAGGA3)]),
    ("1-1101", None),  # filled from the Pāli line (order of the sense pairs)
    ("1-3-2-3-0", [GROUP_HEAD["##### Āsavagocchakaṃ"]]),
    ("1-1102", [f"{Q(P2(14, 'a'))} Bốn loại {ASAVA_N} {DASH} " + ", ".join(ASAVA.values()) + "."]),
    ("1-1103", [f"{TQ(ASAVA['kāma'])} {KAMESU} {S_KAMA} {TA(ASAVA['kāma'])}"]),
    ("1-1104", [f"{TQ(ASAVA['bhava'])} {BHAVESU} {S_BHAVA_V} {TA(ASAVA['bhava'])}"]),
    ("1-1105", [f"{TQ(ASAVA['diṭṭhi'])} {TEN_VIEWS}; {EVA} {S_DITTHI} {TA(ASAVA['diṭṭhi'])} "
                f"{cap(ALL_WRONG)} {ASAVA['diṭṭhi']}."]),
    # «aññāṇaṃः yaṃ»: Devanāgarī visarga in the Pāli where a punctuation mark belongs; rendered as «;»
    ("1-1106", [f"{TQ(ASAVA['avijjā'])} {cap(ANNANA4)}; {EVA} {S_MOHA} {TA(ASAVA['avijjā'])}",
                cap(M.ANSWER(P2(14, "a")))]),
    ("1-1107", [NO_X(P2(14, "b"))]),
    ("1-1108", [QB(P2(15, "a"), f"{cap(K3)}, {SPH3}, {TL} {KH5P}")]),
    ("1-1109", [QB(P2(15, "b"), MAGGA3)]),
    ("1-1110", [QB(P2(16, "a"), f"{REL_SAMP}, {TL} {KH4P}")]),
    ("1-1111", [QB(P2(16, "b"), f"{REL_VIPP}, {TL} {KH4P}; {SABBA}")]),
    ("1-1112", [SAME(ASAVA_N, P2(17, "a"))]),
    ("1-1113", [AMONG_NIYA_SEG(P2(17, "b"))]),
    ("1-1114", [QB(P2(18, "a"), ASAVA_PAIRS)]),
    ("1-1115", [QB(P2(18, "b"), f"{AMONG_SAMP} {KH4P}")]),
    ("1-1116", [VIPP_SAS(P2(19, "a"))]),
    ("1-1117", [QB(P2(19, "b"), MAGGA3), END_BHANA1]),
    ("1-3-2-4-0", [GROUP_HEAD["##### Saṃyojanagocchakaṃ"]]),
    ("1-1118", [f"{Q(P2(20, 'a'))} Mười {FETTER_N} {DASH} " + ", ".join(FETTER(k) for k in FETTER_GEN) + "."]),
    ("1-1119", [f"{TQ(FETTER('kāmarāga'))} {KAMESU} {S_KAMA} {TA(FETTER('kāmarāga'))}"]),
    ("1-1120", [f"{TQ(FETTER('paṭigha'))} {DOSA_OPEN} {cap(EVA)} {S_DOSA} {TA(FETTER('paṭigha'))}"]),
    ("1-1121", [f"{TQ(FETTER('māna'))} {MANA} {TA(FETTER('māna'))}"]),
    ("1-1122", [f"{TQ(FETTER('diṭṭhi'))} {TEN_VIEWS}; {EVA} {S_DITTHI} {TA(FETTER('diṭṭhi'))} "
                f"Ngoại trừ {FETTER('sīlabbataparāmāsa')}, {ALL_WRONG} {FETTER('diṭṭhi')}."]),
    ("1-1123", [f"{TQ(FETTER('vicikicchā'))} {VICI_OPEN}; {EVA} {S_KANKHA} {TA(FETTER('vicikicchā'))}"]),
    # «patiṭṭhāho» in the diṭṭhi string (for paṭiggāho): the 2-04 string, which renders it «sự bám chặt»
    ("1-1124", [f"{TQ(FETTER('sīlabbataparāmāsa'))} {SILA_OPEN}; {EVA} {S_DITTHI} "
                f"{TA(FETTER('sīlabbataparāmāsa'))}"]),
    ("1-1125", [f"{TQ(FETTER('bhavarāga'))} {BHAVESU} {S_BHAVA} {TA(FETTER('bhavarāga'))}"]),
    ("1-1126", [f"{TQ(FETTER('issā'))} {ISSA} {TA(FETTER('issā'))}"]),
    ("1-1127", [f"{TQ(FETTER('macchariya'))} {MACCH} {TA(FETTER('macchariya'))}"]),
    ("1-1128", [f"{TQ(FETTER('avijjā'))} {cap(ANNANA4)}; {EVA} {S_MOHA} {TA(FETTER('avijjā'))}",
                cap(M.ANSWER(P2(20, "a")))]),
    ("1-1129", [NO_X(P2(20, "b"))]),
    ("1-1130", [NIYA(P2(21, "a"))]),
    ("1-1131", [QB(P2(21, "b"), MAGGA3)]),
    ("1-1132", [QB(P2(22, "a"), f"{REL_SAMP}, {TL} {KH4P}")]),
    ("1-1133", [QB(P2(22, "b"), f"{REL_VIPP}, {TL} {KH4P}; {SABBA}")]),
    ("1-1134", [SAME(FETTER_N, P2(23, "a"))]),
    ("1-1135", [AMONG_NIYA_SEG(P2(23, "b"))]),
    ("1-1136", [QB(P2(24, "a"), FETTER_PAIRS)]),
    ("1-1137", [QB(P2(24, "b"), f"{AMONG_SAMP} {KH4P}")]),
    ("1-1138", [VIPP_SAS(P2(25, "a"))]),
    ("1-1139", [QB(P2(25, "b"), MAGGA3)]),
    ("1-3-2-5-0", [GROUP_HEAD["##### Ganthagocchakaṃ"]]),
    ("1-1140", [f"{Q(P2(26, 'a'))} Bốn {GANTHA_N} {DASH} " + ", ".join(GANTHA(k) for k in GANTHA_GEN) + "."]),
    ("1-1141", [f"{TQ(GANTHA('abhijjhā'))} {YO} {S_LOBHA} {TA(GANTHA('abhijjhā'))}"]),
    ("1-1142", [f"{TQ(GANTHA('byāpāda'))} {DOSA_OPEN} {cap(EVA)} {S_DOSA} {TA(GANTHA('byāpāda'))}"]),
    ("1-1143", [f"{TQ(GANTHA('sīlabbataparāmāsa'))} {SILA_OPEN}; {EVA} {S_DITTHI} "
                f"{TA(GANTHA('sīlabbataparāmāsa'))}"]),
    ("1-1144", [f"{TQ(GANTHA('idaṃsacca'))} {IDAM_VIEWS}; {EVA} {S_DITTHI} {TA(GANTHA('idaṃsacca'))} "
                f"Ngoại trừ {GANTHA('sīlabbataparāmāsa')}, {ALL_WRONG} {GANTHA('idaṃsacca')}.",
                cap(M.ANSWER(P2(26, "a")))]),
    ("1-1145", [NO_X(P2(26, "b"))]),
    ("1-1146", [NIYA(P2(27, "a"))]),
    ("1-1147", [QB(P2(27, "b"), MAGGA3)]),
    ("1-1148", [QB(P2(28, "a"), f"{REL_SAMP}, {TL} {KH4P}")]),
    ("1-1149", [QB(P2(28, "b"), f"{REL_VIPP}, {TL} {KH4P}; {SABBA}")]),
    ("1-1150", [SAME(GANTHA_N, P2(29, "a"))]),
    ("1-1151", [AMONG_NIYA_SEG(P2(29, "b"))]),
    ("1-1152", [QB(P2(30, "a"), GANTHA_PAIRS)]),
    ("1-1153", [QB(P2(30, "b"), f"{AMONG_SAMP} {KH4P}")]),
    ("1-1154", [VIPP_SAS(P2(31, "a"))]),
    ("1-1155", [QB(P2(31, "b"), MAGGA3)]),
]

ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def pali_segments():
    segs, buf = [], []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf, "trailing lines without id"
    return segs


def ndash(s):
    return s.count("–") + s.count("—")


def build():
    psegs = pali_segments()
    assert [b for b, _ in psegs] == [b for b, _ in SEGMENTS], "block IDs differ from the Pāli"
    out = []
    for (bid, lines), (_, plines) in zip(SEGMENTS, psegs):
        if lines is None:
            assert bid == "1-1101"
            lines = [kenaci(plines[0])]
        assert len(lines) == len(plines), (bid, len(lines), len(plines))
        for p, r in zip(plines, lines):
            assert ndash(p) == ndash(r), (bid, ndash(p), ndash(r), r)
            assert p.count("[") == r.count("["), (bid, p.count("["), r.count("["))
            assert p.count("…pe…") == r.count(ELL), (bid, p.count("…pe…"), r.count(ELL))
            assert p.count("?") == r.count("?"), (bid, p.count("?"), r.count("?"))
            assert p.startswith("#") == r.startswith("#"), (bid, p, r)
            if p.startswith("#"):
                assert HEAD[p] == r, (bid, p, r)
        lines = list(lines)
        lines[-1] += f" ^{bid}"
        out.append("\n".join(lines))
    text = "\n\n".join(out) + "\n"
    assert "—" not in text and ":-" not in text and "pe…" not in text and "\n\n\n" not in text
    assert unicodedata.normalize("NFC", text) == text
    return text


if __name__ == "__main__":
    print("headings checked:", check_headings())
    t = build()
    OUT.write_text(t, encoding="utf-8", newline="\n")
    print("wrote", OUT, "segments", len(SEGMENTS))
