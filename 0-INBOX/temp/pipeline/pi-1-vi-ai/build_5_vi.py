"""Build the Vietnamese plain zero-shot of pi-1 chapter 5 (5-atthakathakandam.md, Aṭṭhakathākaṇḍaṃ,
^1-4-0 … ^1-1616): the matrix items explained once more by classes of mind.

usage: python -I -X utf8 build_5_vi.py      (checks, then writes the part)

Importing this file does NOT build anything.
Method: build_4-02_4-03_vi (H) is imported unchanged, and through it build_4-01_vi (G), build_matika_vi (M),
build_ch2_01_sample_vi (C), build_3-01_vi (R), build_3-02_3-03_vi (X) and the 2-0x builders (B, D, E, F).
Structure as ../pi-1-ru/build_5_ru.py; the Vietnamese is from the Pāli. Every matrix item named in a question, an
answer, a «siyā» clause or a «na vattabbā» clause comes from M.QUESTION / M.ANSWER / M.BARE / M.PRED; the names of
the defilements, spheres, paths, sense bases, aggregates and material form come from the earlier builders; all
mind-class phrases are fixed constants below, so every repeat is byte-identical. Checks in build():
- block IDs, line counts, per line the Pāli count of «–», «?», «[» and «…pe…» (= «…»);
- every «Katame dhammā X?» opens with the Vietnamese question of the matrix item X;
- every segment whose Pāli equals a segment of an earlier part (or of this part) has the same Vietnamese.
"""
import importlib, pathlib, re, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
H = importlib.import_module("build_4-02_4-03_vi")   # importing does not write
G, M, C, R, X = H.G, H.M, H.C, H.R, H.X
B, D, E, F = H.B, H.D, H.E, H.F

PART = "5-atthakathakandam.md"
PALI = B.PALI_DIR / PART
OUT = B.OUT_DIR / PART
TERMS = HERE / "vi-zeroshot-terms.md"
DASH, ELL = "–", "…"
assert (G.DASH, G.ELL) == (DASH, ELL)


def cap(s):
    return s[0].upper() + s[1:]


# =========================================================================================
# 1. Matrix items
# =========================================================================================
def key(ref):
    """'T1a' -> ('1-M1-1', 'a'); 'P83b' -> ('1-M2-83', 'b')"""
    m = re.fullmatch(r"([TP])(\d+)([abc])", ref)
    return ("1-M1-" if m.group(1) == "T" else "1-M2-") + m.group(2), m.group(3)


def it(ref):
    return M.BARE[key(ref)]


def pred(ref):
    return M.PRED[key(ref)]


def neg(p):
    """'na X' inside a siyā list: «không …» («không phải là …» before «là»)"""
    return ("không phải " if p.startswith("là ") else "không ") + p


def Q(ref):
    return M.QUESTION(key(ref))


def DJ(left, right):
    """left – right (the Pāli dash)"""
    return f"{left} {DASH} {right}"


def QA(ref, answer, tail=""):
    """'Katame dhammā X? <answer> – ime dhammā X. [tail]'"""
    s = f"{Q(ref)} {DJ(cap(answer), M.ANSWER(key(ref)))}"
    return s + (" " + tail if tail else "")


# na vattabbā: the 4-02 frame («Về tâm, không nên nói – rằng nó “…”, cũng không nên nói rằng nó “…”.»)
def NV(refs, pron, dash=False):
    """na vattabbā/-o/-aṃ X-tipi, Y-tipi = không nên nói rằng <pron> “X”, cũng không nên nói rằng <pron> “Y”"""
    return "không nên nói " + (DASH + " " if dash else "") + ", cũng không nên nói ".join(
        f"rằng {pron} “{pred(r)}”" for r in refs)


def SNV(subj, refs, pron, dash=False):
    """<Subj> na vattabbo/-ā/-aṃ (–) X-tipi, Y-tipi."""
    return f"Về {subj}, {NV(refs, pron, dash)}."


THESE = "những hiện tượng này"       # ime dhammā (siyā / na vattabbā clauses)
SOMETIMES = "đôi khi"                # siyā


def ENV(refs):
    """'– ime dhammā na vattabbā X-tipi, …'"""
    return f"về {THESE}, {NV(refs, 'chúng')}."


def SN(refs, pron="chúng"):
    """siyā na vattabbā …"""
    return f"{SOMETIMES} {NV(refs, pron)}"


def S_(ref):
    return f"{SOMETIMES} {pred(ref)}"


def SIYA(*parts):
    return f"{THESE} " + ", ".join(parts)


def _plain(s):
    return re.sub(r"\([^)]*\)", "", s)


def _sep(xs):
    """items with inner commas (outside brackets) are separated by «;» (as 4-01)"""
    return "; " if any(", " in _plain(x) for x in xs) else ", "


def LC(*xs):
    """plain list (no 'ca' in the Pāli)"""
    return _sep(xs).join(xs)


def LA(*xs):
    """list whose last member carries Pāli 'ca': «a, b và c» / «a; b; và c»"""
    if len(xs) == 1:
        return xs[0]
    if _sep(xs) == ", ":
        return ", ".join(xs[:-1]) + " và " + xs[-1]
    return "; ".join(xs[:-1]) + "; và " + xs[-1]


# =========================================================================================
# 2. Headings and closing lines (vi-zeroshot-terms.md)
# =========================================================================================
HEAD = {
    "### Aṭṭhakathākaṇḍaṃ": "### Phần giải thích",
    "#### Tikaatthuddhāro": "#### Giải thích ý nghĩa các bộ ba",
    "#### Dukaatthuddhāro": "#### Giải thích ý nghĩa các bộ đôi",
}
GROUP_PALI = ["Hetu", "Cūḷantara", "Āsava", "Saṃyojana", "Gantha", "Ogha", "Yoga", "Nīvaraṇa", "Parāmāsa",
              "Mahantara", "Upādāna", "Kilesa", "Piṭṭhi"]
for n, g in enumerate(GROUP_PALI, 1):
    HEAD["##### " + g + ("dukaṃ" if g in ("Cūḷantara", "Mahantara", "Piṭṭhi") else "gocchakaṃ")] = \
        M.GROUPS[f"1-M-2-{n}-0"][0]
END_TIKA = G.END_TIKA                                  # Tikaṃ. = Các bộ ba. (4-01)
END_ATTHA = "Phần giải thích ý nghĩa đã hoàn tất."     # Atthuddhāro niṭṭhito. (terms file)
BOOK = "Liệt kê các hiện tượng"                        # ## Dhammasaṅgaṇīpāḷi (terms file)
END_BOOK = f"Bộ sách “{BOOK}” đã hoàn tất."            # Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ.


def check_headings():
    terms, lines = {}, {}
    for line in TERMS.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(#+ .+?) = (#+ .+)", line)
        if m:
            terms.setdefault(m.group(1), m.group(2))
        m = re.fullmatch(r"([^#].+?) = (.+)", line)
        if m:
            lines.setdefault(m.group(1), m.group(2))
    for p, v in HEAD.items():
        assert terms[p] == v, (p, terms.get(p), v)
    assert lines["Atthuddhāro niṭṭhito. (proposed)"] == END_ATTHA
    assert terms["## Dhammasaṅgaṇīpāḷi"] == "## " + BOOK
    assert terms["#### Tebhūmakakusalaṃ"] == "#### " + cap(K3)
    assert terms["#### Dvādasa akusalāni"] == "#### " + cap(AK12)
    assert terms["#### Kāmāvacarakusalaṃ"] == "#### " + cap(KAMK)
    assert terms["##### Catukkanayo"] == "##### " + cap(CATU.removeprefix("theo "))
    assert terms["##### Pañcakanayo"] == "##### " + cap(PANCA.removeprefix("theo "))
    assert terms["##### Kiriyāmanodhātu"] == "##### " + cap(KIRMD)
    assert terms["##### Rūpāvacaravipākā"] == "##### Các " + "quả nghiệp " + G.SPHERE["rūpa"]
    assert terms["##### Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni"].startswith(
        "##### " + cap(ARU4))
    return len(HEAD)


# =========================================================================================
# 3. Classes of mind (notes-5.md)
# =========================================================================================
NUM = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười",
       11: "mười một", 12: "mười hai"}
SPHERE = G.SPHERE                                   # thuộc cõi dục lạc / hình sắc / không hình sắc; không nằm trong …
KUS, AKUS, ABY = G.K["kusala"], G.K["akusala"], G.K["abyākata"]   # thiện / bất thiện / không xác định về mặt đạo đức
TAM = H.TAM                                         # citta = tâm
KIR = "chức năng"                                   # kiriya (2-05 «mang tính chức năng», headings «Tâm chức năng …»)
VIPAKA = "quả nghiệp"                               # vipāka as a class of mind (headings «Các quả nghiệp thuộc …»)
LOAI = "loại"                                       # cittuppāda (countable) = loại tâm (heading «Mười hai loại tâm bất thiện»)
PL4, PL3 = "thuộc bốn cõi", "thuộc ba cõi"          # catūsu / tīsu bhūmīsu (heading «Tâm thiện thuộc ba cõi»)

K4 = f"{TAM} {KUS} {PL4}"                           # catūsu bhūmīsu kusalaṃ
K3 = f"{TAM} {KUS} {PL3}"                           # tīsu bhūmīsu kusalaṃ
AK = f"{TAM} {AKUS}"                                # akusalaṃ
ALL_AK = f"toàn bộ {AK}"                            # sabbaṃ akusalaṃ (as «toàn bộ vật chất»)
V4 = f"{VIPAKA} {PL4}"                              # catūsu bhūmīsu vipāko
V3 = f"{VIPAKA} {PL3}"                              # tīsu bhūmīsu vipāko
F3 = f"{TAM} {KIR} {ABY} {PL3}"                     # tīsu bhūmīsu kiriyābyākataṃ
RF = R.RF                                           # rūpaṃ = vật chất
ALLR = R.ALL_RF                                     # sabbañca rūpaṃ = toàn bộ vật chất
NB = "Niết-bàn"                                     # nibbānaṃ (core terms)
KAMA = SPHERE["kāma"]
KAMK = f"{TAM} {KUS} {KAMA}"                        # kāmāvacarakusalaṃ / kāmāvacaraṃ kusalaṃ
ALL_KAMV = f"toàn bộ {VIPAKA} {KAMA}"               # sabbo kāmāvacarassa vipāko
KAMKIR = f"{TAM} {KIR} {ABY} {KAMA}"                # kāmāvacarakiriyābyākataṃ
AK12 = f"{NUM[12]} {LOAI} {AK}"                     # dvādasa akusalacittuppādā
assert C.H_KAMA_KUSALA == "#### " + cap(KAMK)


def REST_AK(x):
    """Ṭhapetvā X avasesaṃ akusalaṃ"""
    return f"{AK} còn lại ngoại trừ {x}"


EXCEPT = G.EXCEPT                                   # ṭhapetvā = ngoại trừ
assert EXCEPT == "ngoại trừ"


def ETTH(x):
    """etthuppannaṃ X ṭhapetvā"""
    return f"{EXCEPT} {x} sinh khởi trong đó"


# counted classes («<n> loại …»)
def KAMK_N(n, q=""):
    """kāmāvacarakusalato <n> [<q>-cittuppādā]"""
    return f"{n} {LOAI} {KAMK}" + (f" {q}" if q else "")


def AK_N(n):
    """akusalato <n>"""
    return f"{n} {LOAI} {AK}"


KUS_RESULT = f"quả của nghiệp {KUS} {KAMA}"         # kāmāvacarakusalassa vipāka (2-04 «quả của nghiệp thiện thuộc cõi dục lạc»)
AKUS_RESULT = f"quả của nghiệp {AKUS}"              # akusalassa vipāka


def KAMKV_N(n):
    """kāmāvacarakusalassa vipākato <n> [cittuppādā]"""
    return f"{n} {LOAI} {KUS_RESULT}"


def AKV_N(n):
    """akusalassa vipākato <n>"""
    return f"{n} {LOAI} {AKUS_RESULT}"


def KIR_N(n, q=""):
    """kiriyato <n> [<q>-cittuppādā]"""
    return f"{n} {LOAI} {TAM} {KIR}" + (f" {q}" if q else "")


SOM = E.ACC["somanassa"]                            # có niềm vui đi kèm
UPE = E.ACC["upekkhā"]                              # có sự bình thản đi kèm
DOMS = E.ACC["domanassa"]                           # có nỗi buồn đi kèm
NSAMP = B.NANA                                      # gắn liền với hiểu biết
NVIPP = "không " + B.NANA
DITG = E.DITTHIGATA                                 # sự mắc kẹt trong các quan điểm
DS, DV = f"gắn liền với {DITG}", f"không gắn liền với {DITG}"
assert E.NEW_PH["diṭṭhigatasampayuttaṃ"] == DS and E.NEW_PH["diṭṭhigatavippayuttaṃ"] == DV
LOBHA, DOSA, MOHA = G.ROOTS_A                       # sự tham lam / sự sân hận / sự si mê
VICI, UDDHACCA = G.VICI, H.UDDHACCA                 # sự hoài nghi / sự xao động


def ACC(x):
    """-sahagata = có X đi kèm (matrix triad 7)"""
    return f"có {x} đi kèm"


assert ACC(G.PITI) == pred("T7a")
LOBS, VICS, UDDS = ACC(LOBHA), ACC(VICI), ACC(UDDHACCA)
DIT4 = f"{NUM[4]} {LOAI} {TAM} {DS}"                     # cattāro diṭṭhigatasampayuttacittuppādā
LOBDV4 = f"{NUM[4]} {LOAI} {TAM} {LOBS} và {DV}"         # cattāro diṭṭhigatavippayutta(-)lobhasahagatacittuppādā
LOBDS4 = f"{NUM[4]} {LOAI} {TAM} {LOBS} và {DS}"         # cattāro diṭṭhigatasampayuttalobhasahagatacittuppādā
LOB8 = f"{NUM[8]} {LOAI} {TAM} {LOBS}"                   # aṭṭha lobhasahagatacittuppādā
DOM2 = f"{NUM[2]} {LOAI} {TAM} {DOMS}"                   # dve domanassasahagatacittuppādā
VIC_C = f"{LOAI} {TAM} {VICS}"                           # vicikicchāsahagato cittuppādo
UDD_C = f"{LOAI} {TAM} {UDDS}"                           # uddhaccasahagato cittuppādo
VICMOHA = f"{MOHA} {VICS}"                               # vicikicchāsahagato moho
UDDMOHA = f"{MOHA} {UDDS}"                               # uddhaccasahagato moho
VUMOHA = f"{VICMOHA} và {UDDMOHA}"                       # vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ
UPP = "sinh khởi"                                        # uppajjati / uppanna (matrix «đã sinh khởi»)
assert pred("T17a") == "đã " + UPP
DOMMOHA = f"{MOHA} {UPP} trong {DOM2}"                   # dvīsu domanassasahagatesu cittuppādesu uppanno moho
# locatives (… uppajjati / uppajjanti)
IN = "trong"
VICS_L = f"{IN} các {LOAI} {TAM} {VICS}"                 # vicikicchāsahagatesu cittuppādesu
UDDS_L = f"{IN} các {LOAI} {TAM} {UDDS}"                 # uddhaccasahagatesu cittuppādesu
SASANKH_L = f"{IN} các {LOAI} {AK} {B.PH['sasaṅkhārena']}"   # sasaṅkhārikesu akusalesu (có sự thúc đẩy)
ALL_AK_L = f"{IN} {ALL_AK}"                              # sabbākusalesu
K4_L, V4_L = f"{IN} {K4}", f"{IN} {V4}"                  # catūsu bhūmīsu kusalesu / vipākesu
F3_L = f"{IN} {TAM} {KIR} {PL3}"                         # tīsu bhūmīsu kiriyesu
NO_ROOT = pred("P2b")                                    # không có gốc rễ
KAMV_AHC = f"các {LOAI} {VIPAKA} {KAMA} {NO_ROOT}"       # kāmāvacarassa vipākato ahetuke cittuppāde
KAMKIR_AHC = f"các {LOAI} {TAM} {KIR} {KAMA} {NO_ROOT}"  # kāmāvacarakiriyato ahetuke cittuppāde
V4X = f"{V4} {EXCEPT} {KAMV_AHC}"
F3X = f"{F3} {EXCEPT} {KAMKIR_AHC}"
NVIPP4 = f"{NUM[4]} {LOAI} {TAM} {NVIPP}"                # cattāro ñāṇavippayutte cittuppāde

PV = f"hai nhóm {NUM[5]} {LOAI} thức"                    # dvepañcaviññāṇāni (heading «Năm loại thức …»)
MD = B.NAME["manodhātu"]                                 # yếu tố ý
MVD = B.NAME["manoviññāṇadhātu"]                         # yếu tố ý thức
MD3 = f"ba {MD}"                                         # tisso manodhātuyo
AHM5 = f"{NUM[5]} {MVD} {NO_ROOT}"                       # pañca ahetukamanoviññāṇadhātuyo
KIRMD = f"{MD} mang tính {KIR}"                          # kiriyāmanodhātu (heading)
KIRAH_SOM = f"{MVD} mang tính {KIR}, {NO_ROOT}, {SOM}"   # kiriyāhetukamanoviññāṇadhātu somanassasahagatā
KIRAH_UPE = f"{MVD} mang tính {KIR}, {NO_ROOT}, {UPE}"
AKV_MVD_UPE = f"{MVD} là {AKUS_RESULT}, {UPE}"           # akusalassa vipākato manoviññāṇadhātu upekkhāsahagatā
DUKKHA_KV = f"{E.BODY} {ACC(E.NEW_NAMES['dukkhaṃ'])}"    # dukkhasahagataṃ kāyaviññāṇaṃ (2-05 «có sự đau khổ đi kèm»)

M4 = G.MAGGA4[0].lower() + G.MAGGA4[1:]                  # cattāro maggā apariyāpannā
P4 = f"{NUM[4]} {G.PHALA} của đời sống sa-môn"           # cattāri sāmaññaphalāni (4-01 «ba thành quả thấp hơn …»)
ARIYA4 = f"{NUM[4]} {G.ARIYAMAGGA}"                      # cattāro ariyamaggā
MPN = LA(M4, P4, NB)
MP = LA(M4, P4)
KAMMA = f"{R.KIND} {X.QUALS['kammassa katattā']}"        # yañca rūpaṃ kammassa katattā
NKAMMA = f"{R.KIND} {X.QUALS['na kammassa katattā']}"
RDH = f"{R.KIND} {X.EXTRA['anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ']}"
assert G.KATATTA == "và " + KAMMA and G.ANID == "và " + RDH

KVK = f"({KUS}, quả của nghiệp và {KIR})"                # kusalato ca vipākato ca kiriyato ca
KV = f"({KUS} và quả của nghiệp)"                        # kusalato ca vipākato ca
KK = f"({KUS} và {KIR})"                                 # kusalato ca kiriyato ca

JHANA = "tầng thiền"
LOK = "vượt thế gian"                                    # lokuttara (2-03 «tầng thiền vượt thế gian»)
CATU, PANCA = "theo phương pháp chia bốn", "theo phương pháp chia năm"   # catukka- / pañcakanaya (headings)
ORD = {1: "thứ nhất", 2: "thứ hai", 4: "thứ tư"}


def J(n, kind, five=False):
    """rūpāvacaraṃ / lokuttaraṃ <n>-th jhānaṃ [pañcakanaye]"""
    return f"{JHANA} {ORD[n]} " + (SPHERE["rūpa"] if kind == "r" else LOK) + (f" {PANCA}" if five else "")


R1J, R4J, L1J, L4J = J(1, "r"), J(4, "r"), J(1, "l"), J(4, "l")
R2J5, L2J5 = J(2, "r", True), J(2, "l", True)
J4V = f"{VIPAKA} của {JHANA} {ORD[4]}"                   # catutthassa jhānassa vipāko


def JH(kind, a, b):
    """rūpāvacara/lokuttara + <a><b>-jjhānā (e.g. tikacatukka = three by the fourfold, four by the fivefold method)"""
    where = SPHERE["rūpa"] if kind == "r" else LOK
    return f"{NUM[a]} {JHANA} {where} {CATU} và {NUM[b]} {JHANA} {PANCA}"


ARU4 = f"{NUM[4]} {JHANA} không hình sắc"                # cattāro āruppā (heading «Bốn tầng thiền không hình sắc»)
ARV4 = f"{NUM[4]} {LOAI} {TAM} {SPHERE['arūpa']}"        # cattāro arūpāvacarā
AKAS, NEVA = H.AKASA, H.NEVA
VINN = "lĩnh vực thức vô tận"                            # viññāṇañcāyatanaṃ (2-02)
AKIN = "lĩnh vực không có gì cả"                         # ākiñcaññāyatanaṃ (2-02)
_T22 = (B.OUT_DIR / "2-02-cittuppadakandam.md").read_text(encoding="utf-8")
assert VINN in _T22 and AKIN in _T22 and f"{JHANA} {ORD[4]}" in _T22

AY = R.N
RUPAYATANA = cap(AY["rūpāyatanaṃ"])                      # Rūpāyatanaṃ
EYE_TOUCH = G.AY_PE                                      # Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ
EYE_TOUCH_SP = f"{AY['cakkhāyatanaṃ']} {ELL} {AY['phoṭṭhabbāyatanaṃ']}"   # … with the stray space, mirrored
NOOBJ = f"{cap(LA(RF, NB))} {pred('P55b')}."             # Rūpañca nibbānañca anārammaṇā.

# recurring answer lists
A4 = LA(K4, AK, V4, F3, RF, NB)
A4_NOAK = LA(K4, V4, F3, RF, NB)
A3R = LA(K3, AK, V3, F3, ALLR)
A3R_NOAK = LA(K3, V3, F3, ALLR)
A4R = LA(K4, AK, V4, F3, ALLR)
A4_INV = LA(K4, AK, V4, F3, RDH, NB)
SAHETU = (K4, AK, V4X, F3X)
SAHETU_A = LC(REST_AK(VUMOHA), K4, V4X, F3X)
AHETU = LA(VICMOHA, UDDMOHA, PV, MD3, AHM5, RF, NB)
SIYA2 = cap(LC(LOBDV4, DOM2))   # cattāro diṭṭhigatavippayuttā lobhasahagatacittuppādā, dve domanassa…

# feeling / rapture / happiness / equanimity lists
I_SUKHA_V = [KAMK_N(NUM[4], SOM), AK_N(NUM[4]), f"{NUM[5]} {LOAI} {KUS_RESULT} và {TAM} {KIR}",
             JH("r", 3, 4) + " " + KVK, JH("l", 3, 4) + " " + KV]
I_UPE = [KAMK_N(NUM[4], UPE), AK_N(NUM[6]), KAMKV_N(NUM[10]), AKV_N(NUM[6]), KIR_N(NUM[6]), R4J + " " + KVK]
I_PITI = [KAMK_N(NUM[4], SOM), AK_N(NUM[4]), KAMKV_N(NUM[5]), KIR_N(NUM[5]),
          JH("r", 2, 3) + " " + KVK, JH("l", 2, 3) + " " + KV]
I_SUKHA = [KAMK_N(NUM[4], SOM), AK_N(NUM[4]), KAMKV_N(NUM[6]), KIR_N(NUM[5]),
           JH("r", 3, 4) + " " + KVK, JH("l", 3, 4) + " " + KV]
I_UPEKKHA = I_UPE + [ARU4 + " " + KVK, L4J + " " + KV]
I_APITI = [KAMK_N(NUM[4], UPE), AK_N(NUM[8]), KAMKV_N(NUM[11]), AKV_N(NUM[7]), KIR_N(NUM[6]),
           JH("r", 2, 2) + " " + KVK, ARU4 + " " + KVK, JH("l", 2, 2) + " " + KV]
I_SAVITAKKA = [KAMK, AK, KAMKV_N(NUM[11]), AKV_N(NUM[2]), KIR_N(NUM[11]), R1J + " " + KVK, L1J + " " + KV]
FEEL, PITI, SUKHA, UPEKKHA, VIT, VIC = G.FEEL, G.PITI, G.SUKHA, G.UPEKKHA, G.VIT, G.VIC

# =========================================================================================
# 4. Segments
# =========================================================================================
P402 = dict(H.pali_segments(H.PARTS[0]))
V402 = dict(H.build_402(P402))
V401 = dict(G.SEGMENTS)
S = {}

S["1-4-0"] = [HEAD["### Aṭṭhakathākaṇḍaṃ"]]
S["1-4-1-0"] = [HEAD["#### Tikaatthuddhāro"]]
S["1-1384"] = [QA("T1a", K4)]
S["1-1385"] = [QA("T1b", AK12)]
S["1-1386"] = [QA("T1c", LA(V4, F3, RF, NB))]
# «akusalato cattāro kāmāvacarakusalassa vipākato ca kiriyato ca pañca»: no comma after «cattāro»; split by sense
S["1-1387"] = [QA("T2a", LC(*I_SUKHA_V, ETTH(FEEL["a"])))]
S["1-1388"] = [QA("T2b", LC(DOM2, DUKKHA_KV, ETTH(FEEL["b"])))]
# «ya vedanāya sampayuttātipi» = a truncated «adukkhamasukhāya …» (spelling slip): written out as T2c
S["1-1389"] = [QA("T2c", LC(*I_UPE, ARV4 + " " + KVK, L4J + " " + KV, ETTH(FEEL["c"])),
                  DJ(cap(LA(f"ba {LOAI} {C.N['vedanā']}", RF, NB)), ENV(["T2a", "T2b", "T2c"])))]
S["1-1390"] = [QA("T3a", V4)]
S["1-1391"] = [QA("T3b", LC(K4, AK))]
S["1-1392"] = [QA("T3c", LA(F3, RF, NB))]
S["1-1393"] = [QA("T4a", LA(V3, KAMMA))]
S["1-1394"] = [QA("T4b", LA(K3, AK, F3, NKAMMA))]
S["1-1395"] = [QA("T4c", MPN)]
S["1-1396"] = [QA("T5a", AK12)]
S["1-1397"] = [QA("T5b", A3R_NOAK)]
S["1-1398"] = [QA("T5c", MPN)]
S["1-1399"] = [QA("T6a", LC(*I_SAVITAKKA, ETTH(f"{VIT} và {VIC}")))]
S["1-1400"] = [QA("T6b", LC(R2J5 + " " + KVK, L2J5 + " " + KV, ETTH(VIC)) + f"; và {VIT}")]
VIC_IN_J2 = (f"{VIC} {UPP} {IN} {JHANA} {ORD[2]}" + M.V("s", "Sī.", "dutiyajjhāne") + f" {PANCA}")
S["1-1401"] = [QA("T6c", LC(PV, JH("r", 3, 3) + " " + KVK, ARU4 + " " + KVK, JH("l", 3, 3) + " " + KV,
                            VIC_IN_J2, LA(RF, NB)),
                  SNV(f"{VIC} cùng {UPP} với {VIT}", ["T6a", "T6b", "T6c"], "nó"))]
S["1-1402"] = [QA("T7a", LC(*I_PITI, ETTH(PITI)))]
S["1-1403"] = [QA("T7b", LC(*I_SUKHA, ETTH(SUKHA)))]
PITI_SUKHA = (f"{cap(PITI)} {neg(pred('T7a'))}, {pred('T7b')}, {neg(pred('T7c'))}. "
              f"{cap(SUKHA)} {neg(pred('T7b'))}, {S_('T7a')}, {neg(pred('T7c'))}, {SN(['T7a'], 'nó')}.")
EQ_FEELING = f"{C.N['vedanā']} là {UPEKKHA}"            # yā ca vedanā upekkhā
S["1-1404"] = [QA("T7c", LC(*I_UPEKKHA, ETTH(UPEKKHA)),
                  PITI_SUKHA + " " + DJ(cap(LA(DOM2, DUKKHA_KV, EQ_FEELING, RF, NB)), ENV(["T7a", "T7b", "T7c"])))]
S["1-1405"] = [QA("T8a", LC(DIT4, VIC_C))]
S["1-1406"] = [QA("T8b", UDD_C, DJ(SIYA2, SIYA(S_("T8a"), S_("T8b")) + "."))]
S["1-1407"] = [QA("T8c", A4_NOAK)]
S["1-1408"] = [QA("T9a", LC(DIT4, VIC_C, ETTH(MOHA)))]
S["1-1409"] = [QA("T9b", LC(UDD_C, ETTH(MOHA)), DJ(SIYA2, SIYA(S_("T9a"), S_("T9b")) + "."))]
S["1-1410"] = [QA("T9c", LA(VICMOHA, UDDMOHA, K4, V4, F3, RF, NB))]
S["1-1411"] = [QA("T10a", LC(K3, AK))]
S["1-1412"] = [QA("T10b", M4)]
S["1-1413"] = [QA("T10c", LA(V4, F3, RF, NB))]
S["1-1414"] = list(V401["1-1023"])                        # same Pāli as 4-01 ^1-1023
S["1-1415"] = [QA("T11b", f"{cap(G.PHALA)} cao nhất, {G.TL} {G.PHALA} A-la-hán")]   # 4-01 ^1-1024 without the variant
S["1-1416"] = [QA("T11c", LA(K3, AK, V3, F3, RF, NB))]
S["1-1417"] = [QA("T12a", LA(KAMK, AK, ALL_KAMV, KAMKIR, ALLR))]
# Rūpāvacarā, arūpāvacarā, kusalābyākatā (sphere words as 4-02 ^1-1288)
S["1-1418"] = [QA("T12b", f"{SPHERE['rūpa']}, {SPHERE['arūpa']}, cả {KUS} lẫn {ABY}")]
S["1-1419"] = [QA("T12c", MPN)]
S["1-1420"] = [QA("T13a", LC(ALL_KAMV, KIRMD, KIRAH_SOM))]
S["1-1421"] = [QA("T13b", LC(VINN, NEVA))]
S["1-1422"] = [QA("T13c", MP,
                  DJ(cap(LC(KAMK_N(NUM[4], NVIPP), KIR_N(NUM[4], NVIPP), ALL_AK)),
                     SIYA(S_("T13a"), S_("T13b"), neg(pred("T13c")), SN(["T13a", "T13b"])) + ". ")
                  + DJ(cap(LC(KAMK_N(NUM[4], NSAMP), KIR_N(NUM[4], NSAMP), R4J + " " + KK, KIRAH_UPE)),
                       SIYA(S_("T13a"), S_("T13b"), S_("T13c"), SN(["T13a", "T13b", "T13c"])) + ". ")
                  + DJ(cap(LC(JH("r", 3, 4) + " " + KVK, J4V, AKAS, AKIN)), ENV(["T13a", "T13b", "T13c"]))
                  + " " + NOOBJ)]
S["1-1423"] = [QA("T14a", AK12)]
S["1-1424"] = [QA("T14b", A3R_NOAK)]
S["1-1425"] = [QA("T14c", MPN)]
S["1-1426"] = [Q("T15a") + " " + DJ(cap(LC(DIT4, DOM2)), SIYA(S_("T15a"), S_("T15c")) + ".")]
S["1-1427"] = [QA("T15b", M4)]
S["1-1428"] = [QA("T15c", LA(LOBDV4, VIC_C, UDD_C, K3, V4, F3, RF, NB))]
S["1-1429"] = [Q("T16a") + " "
               + DJ(cap(LC(KAMK_N(NUM[4], NSAMP), KIR_N(NUM[4], NSAMP))),
                    f"{THESE} {S_('T16a')}, {neg(pred('T16b'))}; {S_('T16c')}, {SN(['T16a', 'T16c'])}. ")
               + f"{cap(ARIYA4)} {neg(pred('T16a'))}, {pred('T16b')}; {S_('T16c')}, {SN(['T16c'])}. "
               + DJ(cap(LC(R4J + " " + KK, KIRAH_UPE)),
                    f"{THESE} {S_('T16a')}; {neg(pred('T16b'))}, {neg(pred('T16c'))}; {SN(['T16a'])}. ")
               + DJ(cap(LA(KAMK_N(NUM[4], NVIPP), ALL_AK, ALL_KAMV, KIR_N(NUM[6]), JH("r", 3, 4) + " " + KVK,
                           J4V, ARU4 + " " + KVK, P4)),
                    ENV(["T16a", "T16b", "T16c"]))
               + " " + NOOBJ]
S["1-1430"] = [Q("T17a") + " "
               + DJ(cap(LA(V4, KAMMA)), f"{SIYA(S_('T17a'), S_('T17c'))}; {NV(['T17b'], 'chúng')}. ")
               + DJ(cap(LA(K4, AK, F3, NKAMMA)), f"{SIYA(S_('T17a'), S_('T17b'))}, {NV(['T17c'], 'chúng')}. ")
               + SNV(NB, ["T17a", "T17b", "T17c"], "nó")]
ALL_DH = f"tất cả {M.DH}"                                 # sabbe dhammā
S["1-1431"] = [f"{cap(EXCEPT)} {NB}, {ALL_DH} {S_('T18a')}, {S_('T18b')}, {S_('T18c')}. "
               + SNV(NB, ["T18a", "T18b", "T18c"], "nó")]
S["1-1432"] = [QA("T19a", LC(VINN, NEVA))]
S["1-1433"] = [f"Không có hiện tượng nào nhất thiết {pred('T19b')}."]   # Niyogā anāgatārammaṇā natthi.
S["1-1434"] = [QA("T19c", LA(PV, MD3),
                  DJ(cap(LC(KAMKV_N(NUM[10]), AKV_MVD_UPE, KIRAH_SOM)),
                     SIYA(S_("T19a"), S_("T19b"), S_("T19c")) + ". ")
                  + DJ(cap(LC(KAMK, AK, KIR_N(NUM[9]), R4J + " " + KK)),
                       SIYA(S_("T19a"), S_("T19b"), S_("T19c")) + "; " + SN(["T19a", "T19b", "T19c"]) + ". ")
                  + DJ(cap(LA(JH("r", 3, 4) + " " + KVK, J4V, AKAS, AKIN, M4, P4)), ENV(["T19a", "T19b", "T19c"]))
                  + " " + NOOBJ)]
ANIND = f"{RF} không gắn kết với các năng lực"           # anindriyabaddharūpaṃ (indriya = năng lực, core)
S["1-1435"] = [f"{cap(EXCEPT)} {ANIND} và {NB}, {ALL_DH} {S_('T20a')}, {S_('T20b')}, {S_('T20c')}. "
               f"{cap(ANIND)} và {NB} {pred('T20b')}."]
S["1-1436"] = [QA("T21a", LC(VINN, NEVA))]
S["1-1437"] = [QA("T21b", LC(JH("r", 3, 4) + " " + KVK, J4V, AKAS, MP),
                  DJ(f"{cap(EXCEPT)} {RF}, tất cả {G.K3}, {KAMA}; {R4J} {KK}",
                     SIYA(S_("T21a"), S_("T21b"), S_("T21c")) + ". ")
                  + SNV(AKIN, ["T21a", "T21b", "T21c"], "nó") + " " + NOOBJ)]
S["1-1438"] = [QA("T22a", RUPAYATANA)]
S["1-1439"] = [QA("T22b", EYE_TOUCH)]
S["1-1440"] = [QA("T22c", A4_INV), END_TIKA]

S["1-4-2-0"] = [HEAD["#### Dukaatthuddhāro"]]
for n in range(1, 14):
    S[f"1-4-2-{n}-0"] = [M.GROUPS[f"1-M-2-{n}-0"][0]]

# -- roots ^1-1441 … ^1-1452
ALOBHA, ADOSA, AMOHA = G.ROOTS_K
ROOT_K, ROOT_A, ROOT_AB = G.ROOT_K, G.ROOT_A, G.ROOT_AB
HETU = M.H                                                # gốc rễ
VH = f"{HETU} là quả của nghiệp"                          # vipākahetu
KRH = f"{HETU} mang tính {KIR}"                           # kiriyahetu
S["1-1441"] = [
    f"{Q('P1a')} Ba {ROOT_K}, ba {ROOT_A}, ba {ROOT_AB}. "
    f"{cap(ALOBHA)}, {ROOT_K}, và {ADOSA}, {ROOT_K}, {UPP} {K4_L}. "
    f"{cap(AMOHA)}, {ROOT_K}, {UPP} {K4_L}, {EXCEPT} {KAMK_N(NUM[4], NVIPP)}.",
    f"{cap(LOBHA)} {UPP} {IN} {LOB8}. {cap(DOSA)} {UPP} {IN} {DOM2}. {cap(MOHA)} {UPP} {ALL_AK_L}.",
    f"{cap(ALOBHA)}, {VH}, và {ADOSA}, {VH}, {UPP} {V4_L}, {EXCEPT} {KAMV_AHC}. "
    f"{cap(AMOHA)}, {VH}, {UPP} {V4_L}, {EXCEPT} {KAMV_AHC}, và {EXCEPT} {NVIPP4}.",
    f"{cap(ALOBHA)}, {KRH}, và {ADOSA}, {KRH}, {UPP} {F3_L}, {EXCEPT} {KAMKIR_AHC}. "
    f"{cap(AMOHA)}, {KRH}, {UPP} " + DJ(f"{F3_L}, {EXCEPT} {KAMKIR_AHC}, và {EXCEPT} {NVIPP4}",
                                        M.ANSWER(key("P1a"))),
]
S["1-1442"] = [QA("P1b", f"{EXCEPT} các {HETU}, {A4}")]
S["1-1443"] = [QA("P2a", SAHETU_A)]
S["1-1444"] = [QA("P2b", AHETU)]
S["1-1445"] = [QA("P3a", SAHETU_A)]
S["1-1446"] = [QA("P3b", AHETU)]


def WHERE(x):
    """Yattha <x> ekato uppajjanti"""
    return f"ở nơi {x} cùng {UPP}"


S["1-1447"] = [QA("P4a", WHERE(f"hai hoặc ba {HETU}"))]
S["1-1448"] = [QA("P4b", LC(*SAHETU, ETTH(f"các {HETU}")), SNV(it("P2b"), ["P4a", "P4b"], "chúng", True))]
S["1-1449"] = [QA("P5a", WHERE(f"hai hoặc ba {HETU}"))]
S["1-1450"] = [QA("P5b", LC(*SAHETU, ETTH(f"các {HETU}")), SNV(it("P3b"), ["P5a", "P5b"], "chúng", True))]
S["1-1451"] = [QA("P6a", LC(*SAHETU, ETTH(f"các {HETU}")))]
S["1-1452"] = [QA("P6b", LA(PV, MD3, AHM5, RF, NB), SNV(it("P1a"), ["P6a", "P6b"], "chúng", True))]

# -- short intermediate pairs ^1-1453 … ^1-1464
S["1-1453"] = [QA("P7a", A4R)]
S["1-1454"] = [QA("P7b", NB)]
S["1-1455"] = [QA("P8a", A4R)]
S["1-1456"] = [QA("P8b", NB)]
S["1-1457"] = [QA("P9a", RUPAYATANA)]
S["1-1458"] = [QA("P9b", LA(EYE_TOUCH_SP, K4, AK, V4, F3, RDH, NB))]
S["1-1459"] = [QA("P10a", EYE_TOUCH)]
S["1-1460"] = [QA("P10b", A4_INV)]
S["1-1461"] = [QA("P11a", G.MAHA)]
S["1-1462"] = [QA("P11b", LA(K4, AK, V4, F3, NB))]
S["1-1463"] = [QA("P12a", A3R)]
KV_B = pred("P13b").removeprefix("mà ")                   # một loại thức nào đó không thể nhận biết (4-01 ^1-1101)
S["1-1464"] = [QA("P12b", MPN, f"Tất cả{M.V('p', 'Syā.', 'sabbeva')} {M.DH} đều là những hiện tượng "
                               f"{pred('P13a')}, {KV_B}.")]

# -- taints ^1-1465 … ^1-1476
ASV = G.ASAVA
ASAVA_N = "ô nhiễm"
assert pred("P14a") == f"là {ASAVA_N}"
S["1-1465"] = [f"{Q('P14a')} Bốn loại {ASAVA_N} {DASH} " + ", ".join(ASV.values()) + ". "
               f"{cap(ASV['kāma'])} {UPP} {IN} {LOB8}, {ASV['bhava']} {UPP} {IN} {LOBDV4}, "
               f"{ASV['diṭṭhi']} {UPP} {IN} {DIT4}. "
               + DJ(f"{cap(ASV['avijjā'])} {UPP} {ALL_AK_L}", M.ANSWER(key("P14a")))]
assert V401["1-1102"][0].startswith(S["1-1465"][0].split(". ", 1)[0] + ".")
S["1-1466"] = [QA("P14b", LA(REST_AK(f"các {ASAVA_N}"), K4, V4, F3, RF, NB))]
S["1-1467"] = [QA("P15a", A3R)]
S["1-1468"] = [QA("P15b", MPN)]
S["1-1469"] = [QA("P16a", LC(f"{DOM2} {ETTH(MOHA)}", REST_AK(VUMOHA)))]
S["1-1470"] = [QA("P16b", LA(DOMMOHA, VICMOHA, UDDMOHA, K4, V4, F3, RF, NB))]
S["1-1471"] = [G.SAME(ASAVA_N, key("P17a"))]
S["1-1472"] = [QA("P17b", LA(REST_AK(f"các {ASAVA_N}"), K3, V3, F3, ALLR),
                  SNV(it("P15b"), ["P17a", "P17b"], "chúng", True))]
S["1-1473"] = [QA("P18a", WHERE(f"hai hoặc ba {ASAVA_N}"))]
S["1-1474"] = [QA("P18b", REST_AK(f"các {ASAVA_N}"), SNV(it("P16b"), ["P18a", "P18b"], "chúng", True))]
S["1-1475"] = [QA("P19a", LA(DOMMOHA, VICMOHA, UDDMOHA, K3, V3, F3, ALLR))]
S["1-1476"] = [QA("P19b", MPN, SNV(it("P16a"), ["P19a", "P19b"], "chúng", True))]

# -- fetters ^1-1477 … ^1-1488
FET, FETTER_N = G.FETTER, "xiềng xích"
assert pred("P20a") == f"là {FETTER_N}"
S["1-1477"] = [f"{Q('P20a')} Mười {FETTER_N} {DASH} " + ", ".join(FET(k) for k in G.FETTER_GEN) + ". "
               f"{cap(FET('kāmarāga'))} {UPP} {IN} {LOB8}. {cap(FET('paṭigha'))} {UPP} {IN} {DOM2}. "
               f"{cap(FET('māna'))} {UPP} {IN} {LOBDV4}. {cap(FET('diṭṭhi'))} {UPP} {IN} {DIT4}. "
               f"{cap(FET('vicikicchā'))} {UPP} {VICS_L}. {cap(FET('sīlabbataparāmāsa'))} {UPP} {IN} {DIT4}. "
               f"{cap(FET('bhavarāga'))} {UPP} {IN} {LOBDV4}. {cap(FET('issā'))} và {FET('macchariya')} "
               f"{UPP} {IN} {DOM2}. "
               + DJ(f"{cap(FET('avijjā'))} {UPP} {ALL_AK_L}", M.ANSWER(key("P20a")))]
assert V401["1-1118"][0].startswith(S["1-1477"][0].split(". ", 1)[0] + ".")
# the Pāli question ends with «.» («Katame dhammā no saṃyojanā.»): kept
S["1-1478"] = [Q("P20b")[:-1] + ". " + DJ(cap(LA(REST_AK(f"các {FETTER_N}"), K4, V4, F3, RF, NB)),
                                          M.ANSWER(key("P20b")))]
S["1-1479"] = [QA("P21a", A3R)]
S["1-1480"] = [QA("P21b", MPN)]
S["1-1481"] = [QA("P22a", REST_AK(UDDMOHA))]
S["1-1482"] = [QA("P22b", LA(UDDMOHA, K4, V4, F3, RF, NB))]
S["1-1483"] = [G.SAME(FETTER_N, key("P23a"))]
S["1-1484"] = [QA("P23b", LA(REST_AK(f"các {FETTER_N}"), K3, V3, F3, ALLR),
                  SNV(it("P21b"), ["P23a", "P23b"], "chúng", True))]
S["1-1485"] = [QA("P24a", WHERE(f"hai hoặc ba {FETTER_N}"))]
S["1-1486"] = [QA("P24b", REST_AK(f"các {FETTER_N}"), SNV(it("P22b"), ["P24a", "P24b"], "chúng", True))]
S["1-1487"] = [QA("P25a", LA(UDDMOHA, K3, V3, F3, ALLR))]
S["1-1488"] = [QA("P25b", MPN, SNV(it("P22a"), ["P25a", "P25b"], "chúng", True))]

# -- ties ^1-1489 … ^1-1500
GAN, GANTHA_N = G.GANTHA, "nút thắt"
assert pred("P26a") == f"là {GANTHA_N}"
S["1-1489"] = [f"{Q('P26a')} Bốn {GANTHA_N} {DASH} " + ", ".join(GAN(k) for k in G.GANTHA_GEN) + ". "
               f"{cap(GAN('abhijjhā'))} {UPP} {IN} {LOB8}. {cap(GAN('byāpāda'))} {UPP} {IN} {DOM2}. "
               + DJ(f"{cap(GAN('sīlabbataparāmāsa'))} và {GAN('idaṃsacca')} {UPP} {IN} {DIT4}",
                    M.ANSWER(key("P26a")))]
assert V401["1-1140"][0].startswith(S["1-1489"][0].split("”. ", 1)[0] + "”.")
PATIGHA = E.NEW_PH["paṭighasampayuttaṃ"].removeprefix("gắn liền với ")   # paṭigha (mental) = sự ác cảm (2-04)
assert PATIGHA == "sự ác cảm"
S["1-1490"] = [QA("P26b", LA(REST_AK(f"các {GANTHA_N}"), K4, V4, F3, RF, NB))]
S["1-1491"] = [QA("P27a", A3R)]
S["1-1492"] = [QA("P27b", MPN)]
S["1-1493"] = [QA("P28a", LC(DIT4, LOBDV4, ETTH(LOBHA), DOM2, ETTH(PATIGHA)))]
GV = [f"{LOBHA} {UPP} {IN} {LOBDV4}", f"{PATIGHA} {UPP} {IN} {DOM2}", VIC_C, UDD_C]
S["1-1494"] = [QA("P28b", LA(*GV, K4, V4, F3, RF, NB))]
S["1-1495"] = [G.SAME(GANTHA_N, key("P29a"))]
S["1-1496"] = [QA("P29b", LA(REST_AK(f"các {GANTHA_N}"), K3, V3, F3, ALLR),
                  SNV(it("P27b"), ["P29a", "P29b"], "chúng", True))]
DL = f"{E.W_DITTHI[0]} và {LOBHA}"                        # diṭṭhi ca lobho ca
S["1-1497"] = [QA("P30a", WHERE(DL))]
S["1-1498"] = [QA("P30b", LC(LOB8, DOM2, ETTH(f"các {GANTHA_N}")),
                  SNV(it("P28b"), ["P30a", "P30b"], "chúng", True))]
S["1-1499"] = [QA("P31a", LA(*GV, K3, V3, F3, ALLR))]
S["1-1500"] = [QA("P31b", MPN, SNV(it("P28a"), ["P31a", "P31b"], "chúng", True))]

# -- floods, yokes (abridged in the Pāli: «Katame dhammā oghā…pe….»)
S["1-1501"] = [Q("P32a")[:-1] + ELL + "."]
S["1-1502"] = [Q("P38a")[:-1] + ELL + "."]

# -- hindrances ^1-1503 … ^1-1514
NIV, NIV_N = H.NIV, "chướng ngại"
S["1-1503"] = [f"{Q('P44a')} Sáu {NIV_N} {DASH} " + ", ".join(H.SIX_NIV) + ". "
               f"{cap(NIV['kāmacchandanīvaraṇaṃ'])} {UPP} {IN} {LOB8}, {NIV['byāpādanīvaraṇaṃ']} {UPP} {IN} {DOM2}, "
               f"{NIV['thinamiddhanīvaraṇaṃ']} {UPP} {SASANKH_L}, {NIV['uddhaccanīvaraṇaṃ']} {UPP} {UDDS_L}, "
               f"{NIV['kukkuccanīvaraṇaṃ']} {UPP} {IN} {DOM2}, {NIV['vicikicchānīvaraṇaṃ']} {UPP} {VICS_L}, "
               + DJ(f"{NIV['avijjānīvaraṇaṃ']} {UPP} {ALL_AK_L}", M.ANSWER(key("P44a")))]
S["1-1504"] = [QA("P44b", LA(REST_AK(f"các {NIV_N}"), K4, V4, F3, RF, NB))]
S["1-1505"] = [QA("P45a", A3R)]
S["1-1506"] = [QA("P45b", MPN)]
S["1-1507"] = [QA("P46a", AK12)]
S["1-1508"] = [QA("P46b", A4_NOAK)]
S["1-1509"] = [G.SAME(NIV_N, key("P47a"))]
S["1-1510"] = [QA("P47b", LA(REST_AK(f"các {NIV_N}"), K3, V3, F3, ALLR),
                  SNV(it("P45b"), ["P47a", "P47b"], "chúng", True))]
S["1-1511"] = [QA("P48a", WHERE(f"hai hoặc ba {NIV_N}"))]
S["1-1512"] = [QA("P48b", REST_AK(f"các {NIV_N}"), SNV(it("P46b"), ["P48a", "P48b"], "chúng", True))]
S["1-1513"] = [QA("P49a", A3R_NOAK)]
S["1-1514"] = [QA("P49b", MPN, SNV(it("P46a"), ["P49a", "P49b"], "chúng", True))]

# -- misapprehension ^1-1515 … ^1-1524
PARA = M.PARA                                             # sự hiểu sai lệch
S["1-1515"] = [QA("P50a", f"{H.DP} {UPP} {IN} {DIT4}")]
S["1-1516"] = [QA("P50b", LA(REST_AK(PARA), K4, V4, F3, RF, NB))]
S["1-1517"] = [QA("P51a", A3R)]
S["1-1518"] = [QA("P51b", MPN)]
S["1-1519"] = [QA("P52a", LC(DIT4, ETTH(PARA)))]
PV4 = [LOBDV4, DOM2, VIC_C, UDD_C]
S["1-1520"] = [QA("P52b", LA(*PV4, K4, V4, F3, RF, NB), SNV(PARA, ["P52a", "P52b"], "nó", True))]
S["1-1521"] = [f"{Q('P53a')} Chính {PARA} ấy {pred('P53a')}."]   # So eva parāmāso … (4-02 ^1-1187 «Sveva …»)
assert V402["1-1187"][0] == S["1-1521"][0]
S["1-1522"] = [QA("P53b", LA(REST_AK(PARA), K3, V3, F3, ALLR), SNV(it("P51b"), ["P53a", "P53b"], "chúng", True))]
S["1-1523"] = [QA("P54a", LA(*PV4, K3, V3, F3, ALLR))]
S["1-1524"] = [QA("P54b", MPN, SNV(f"{it('P50a')} và {it('P52a')}", ["P54a", "P54b"], "chúng", True))]

# -- long intermediate pairs ^1-1525 … ^1-1552
KH3V = H.KH3V                                             # khối cảm giác, khối tri giác, khối tạo tác
AGG = KH3V.split(", ")
VINNATTI2 = f"{AY['kāyaviññatti']}, {AY['vacīviññatti']}"
VIN7 = [E.EYE, E.EAR, E.NOSE, E.TONGUE, E.BODY, MD, MVD]
CITTAJA = (f"{X.ANY_OTHER} {X.QUALS['cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ']} {DASH} "
           + ", ".join(X.ITEMS[i] for i in ("rūpāyatanaṃ", "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ",
                                            "phoṭṭhabbāyatanaṃ", "ākāsadhātu", "āpodhātu", "rūpassa lahutā",
                                            "rūpassa mudutā", "rūpassa kammaññatā", "rūpassa upacayo",
                                            "rūpassa santati", "kabaḷīkāro āhāro")))
assert CITTAJA.replace(f" {DASH} ", ": ", 1) in V402["1-1201"][0]   # 4-02 has no dash there
S["1-1525"] = [QA("P55a", LC(K4, AK, V4, F3))]
S["1-1526"] = [QA("P55b", LA(RF, NB))]
S["1-1527"] = [QA("P56a", ", ".join(VIN7))]
S["1-1528"] = [QA("P56b", LA(*AGG, RF, NB))]
S["1-1529"] = [QA("P57a", KH3V)]
S["1-1530"] = [QA("P57b", LA(TAM, RF, NB))]
S["1-1531"] = [QA("P58a", KH3V)]
S["1-1532"] = [QA("P58b", LA(RF, NB), SNV(TAM, ["P58a", "P58b"], "nó", True))]
S["1-1533"] = [QA("P59a", KH3V)]
S["1-1534"] = [QA("P59b", LA(RF, NB), SNV(TAM, ["P59a", "P59b"], "nó", True))]
for a, b in (("1-1532", "1-1198"), ("1-1534", "1-1200")):   # same «Cittaṃ na vattabbaṃ …» sentence as 4-02
    assert S[a][0].split(". ", 2)[-1] == V402[b][0].split(". ", 2)[-1], (a, b)
S["1-1535"] = [QA("P60a", f"{KH3V}, {VINNATTI2}, {CITTAJA}")]
NOT_CS = LA(TAM, f"{RF} còn lại", NB)                     # cittañca, avasesañca rūpaṃ, nibbānañca
assert H.REST_RF == f"và {RF} còn lại"
S["1-1536"] = [QA("P60b", NOT_CS)]
S["1-1537"] = [QA("P61a", f"{KH3V}, {VINNATTI2}")]
S["1-1538"] = [QA("P61b", NOT_CS)]
S["1-1539"] = [QA("P62a", f"{KH3V}, {VINNATTI2}")]
S["1-1540"] = [QA("P62b", NOT_CS)]
MRN = LA(TAM, RF, NB)
for bid, nn in (("1-1541", 63), ("1-1543", 64), ("1-1545", 65)):
    S[bid] = [QA(f"P{nn}a", KH3V)]
    S[f"1-{int(bid.split('-')[1]) + 1}"] = [QA(f"P{nn}b", MRN)]
S["1-1547"] = list(V402["1-1213"])                        # same Pāli as 4-02 ^1-1213 … ^1-1215
S["1-1548"] = list(V402["1-1214"])
S["1-1549"] = list(V402["1-1215"])
S["1-1550"] = [QA("P67b", LA(K4, AK, V4, F3, R.MAHA4, NB))]
S["1-1551"] = [QA("P68a", LA(V3, KAMMA))]
S["1-1552"] = [QA("P68b", LA(K3, AK, F3, NKAMMA, M4, P4, NB))]

# -- clinging ^1-1553 … ^1-1564
UPA, UPA_N = H.UPA, "sự bám víu"
assert pred("P69a") == f"là {UPA_N}"
S["1-1553"] = [f"{Q('P69a')} Bốn {UPA_N} {DASH} " + ", ".join(UPA.values()) + ". "
               f"{cap(UPA['kāmupādānaṃ'])} {UPP} {IN} {LOB8}. "
               + DJ(f"{cap(UPA['diṭṭhupādānaṃ'])}, {UPA['sīlabbatupādānaṃ']} và {UPA['attavādupādānaṃ']} "
                    f"{UPP} {IN} {DIT4}", M.ANSWER(key("P69a")))]
S["1-1554"] = [QA("P69b", LA(REST_AK(f"các {UPA_N}"), K4, V4, F3, RF, NB))]
S["1-1555"] = [QA("P70a", A3R)]
S["1-1556"] = [QA("P70b", MPN)]
S["1-1557"] = [QA("P71a", LC(LOBDS4, LOBDV4, ETTH(LOBHA)))]
UV = [f"{LOBHA} {UPP} {IN} {LOBDV4}", DOM2, VIC_C, UDD_C]
S["1-1558"] = [QA("P71b", LA(*UV, K4, V4, F3, RF, NB))]
S["1-1559"] = [G.SAME(UPA_N, key("P72a"))]
S["1-1560"] = [QA("P72b", LA(REST_AK(f"các {UPA_N}"), K3, V3, F3, ALLR),
                  SNV(it("P70b"), ["P72a", "P72b"], "chúng", True))]
S["1-1561"] = [QA("P73a", WHERE(DL))]
S["1-1562"] = [QA("P73b", LC(LOB8, ETTH(f"các {UPA_N}")), SNV(it("P71b"), ["P73a", "P73b"], "chúng", True))]
S["1-1563"] = [QA("P74a", LA(*UV, K3, V3, F3, ALLR))]
S["1-1564"] = [QA("P74b", MPN, SNV(it("P71a"), ["P74a", "P74b"], "chúng", True))]

# -- defilements ^1-1565 … ^1-1580
KIL, KILESA_N = H.KIL, "phiền não"
assert pred("P75a") == f"là {KILESA_N}"
S["1-1565"] = [f"{Q('P75a')} Mười {H.VATTHU} của {KILESA_N} {DASH} " + ", ".join(KIL.values()) + ". "
               f"{cap(KIL['lobho'])} {UPP} {IN} {LOB8}. {cap(KIL['doso'])} {UPP} {IN} {DOM2}. "
               f"{cap(KIL['moho'])} {UPP} {ALL_AK_L}. {cap(KIL['māno'])} {UPP} {IN} {LOBDV4}. "
               f"{cap(KIL['diṭṭhi'])} {UPP} {IN} {DIT4}. {cap(KIL['vicikicchā'])} {UPP} {VICS_L}. "
               f"{cap(KIL['thinaṃ'])} {UPP} {SASANKH_L}. "
               + DJ(f"{cap(KIL['uddhaccaṃ'])}, {KIL['ahirikaṃ']} và {KIL['anottappaṃ']} {UPP} {ALL_AK_L}",
                    M.ANSWER(key("P75a")))]
S["1-1566"] = [QA("P75b", LA(REST_AK(f"các {KILESA_N}"), K4, V4, F3, RF, NB))]
S["1-1567"] = [QA("P76a", A3R)]
S["1-1568"] = [QA("P76b", MPN)]
S["1-1569"] = [QA("P77a", AK12)]
S["1-1570"] = [QA("P77b", A4_NOAK)]
S["1-1571"] = [QA("P78a", AK12)]
S["1-1572"] = [QA("P78b", A4_NOAK)]
S["1-1573"] = [G.SAME(KILESA_N, key("P79a"))]
S["1-1574"] = [QA("P79b", LA(REST_AK(f"các {KILESA_N}"), K3, V3, F3, ALLR),
                  SNV(it("P76b"), ["P79a", "P79b"], "chúng", True))]
S["1-1575"] = [G.SAME(KILESA_N, key("P80a"))]
S["1-1576"] = [QA("P80b", REST_AK(f"các {KILESA_N}"), SNV(it("P77b"), ["P80a", "P80b"], "chúng", True))]
S["1-1577"] = [QA("P81a", WHERE(f"hai hoặc ba {KILESA_N}"))]
S["1-1578"] = [QA("P81b", REST_AK(f"các {KILESA_N}"), SNV(it("P78b"), ["P81a", "P81b"], "chúng", True))]
S["1-1579"] = [QA("P82a", A3R_NOAK)]
S["1-1580"] = [QA("P82b", MPN, SNV(it("P78a"), ["P82a", "P82b"], "chúng", True))]

# -- closing pairs ^1-1581 … ^1-1616
S["1-1581"] = [QA("P83a", LC(DIT4, VIC_C), DJ(SIYA2, SIYA(S_("P83a"), S_("P83b")) + "."))]
S["1-1582"] = [QA("P83b", LA(UDD_C, K4, V4, F3, RF, NB))]
S["1-1583"] = [QA("P84a", UDD_C, DJ(SIYA2, SIYA(S_("P84a"), S_("P84b")) + "."))]
S["1-1584"] = [QA("P84b", LA(DIT4, VIC_C, K4, V4, F3, RF, NB))]
S["1-1585"] = [QA("P85a", LC(DIT4, VIC_C, ETTH(MOHA)), DJ(SIYA2, SIYA(S_("P85a"), S_("P85b")) + "."))]
S["1-1586"] = [QA("P85b", LA(VICMOHA, UDD_C, K4, V4, F3, RF, NB))]
S["1-1587"] = [QA("P86a", LC(UDD_C, ETTH(MOHA)), DJ(SIYA2, SIYA(S_("P86a"), S_("P86b")) + "."))]
S["1-1588"] = [QA("P86b", LA(DIT4, VIC_C, UDDMOHA, K4, V4, F3, RF, NB))]
S["1-1589"] = [QA("P87a", LC(*I_SAVITAKKA, ETTH(VIT)))]
S["1-1590"] = [QA("P87b", LA(PV, JH("r", 3, 4) + " " + KVK, ARV4 + " " + KVK, JH("l", 3, 4) + " " + KV, VIT, RF, NB))]
S["1-1591"] = [QA("P88a", LC(KAMK, AK, KAMKV_N(NUM[11]), AKV_N(NUM[2]), KIR_N(NUM[11]), JH("r", 1, 2) + " " + KVK,
                             JH("l", 1, 2) + " " + KV, ETTH(VIC)))]
S["1-1592"] = [QA("P88b", LA(PV, JH("r", 3, 3) + " " + KVK, ARU4 + " " + KVK, JH("l", 3, 3) + " " + KV, VIC, RF, NB))]
S["1-1593"] = [QA("P89a", LC(*I_PITI, ETTH(PITI)))]
S["1-1594"] = [QA("P89b", LA(*I_APITI, PITI, RF, NB))]
S["1-1595"] = [QA("P90a", LC(*I_PITI, ETTH(PITI)))]
S["1-1596"] = [QA("P90b", LA(*I_APITI, PITI, RF, NB))]
S["1-1597"] = [QA("P91a", LC(*I_SUKHA, ETTH(SUKHA)))]
S["1-1598"] = [QA("P91b", LA(KAMK_N(NUM[4], UPE), AK_N(NUM[8]), KAMKV_N(NUM[10]), AKV_N(NUM[7]), KIR_N(NUM[6]),
                             R4J + " " + KVK, ARU4 + " " + KVK, L4J + " " + KV, SUKHA, RF, NB))]
S["1-1599"] = [QA("P92a", LC(*I_UPEKKHA, ETTH(UPEKKHA)))]
S["1-1600"] = [QA("P92b", LA(KAMK_N(NUM[4], SOM), AK_N(NUM[6]), KAMKV_N(NUM[6]), AKV_N(NUM[1]), KIR_N(NUM[5]),
                             JH("r", 3, 4) + " " + KVK, JH("l", 3, 4) + " " + KV, UPEKKHA, RF, NB))]
S["1-1601"] = [QA("P93a", LA(KAMK, AK, ALL_KAMV, KAMKIR, ALLR))]
S["1-1602"] = list(V402["1-1288"])                        # same Pāli as 4-02 ^1-1288 / 1290 / 1292
S["1-1603"] = [QA("P94a", JH("r", 4, 5) + " " + KVK)]
S["1-1604"] = list(V402["1-1290"])
S["1-1605"] = [QA("P95a", ARU4 + " " + KVK)]
S["1-1606"] = list(V402["1-1292"])
S["1-1607"] = [QA("P96a", A3R)]
S["1-1608"] = [QA("P96b", MPN)]
S["1-1609"] = [QA("P97a", M4)]
S["1-1610"] = [QA("P97b", LA(K3, AK, V4, F3, RF, NB))]
S["1-1611"] = [Q("P98a") + " " + DJ(cap(LC(DIT4, DOM2)), SIYA(S_("P98a"), S_("P98b")) + ". ")
               + DJ(cap(M4), M.ANSWER(key("P98a")))]
S["1-1612"] = [QA("P98b", LA(LOBDV4, VIC_C, UDD_C, K3, V4, F3, RF, NB))]
S["1-1613"] = [QA("P99a", A3R)]
S["1-1614"] = [QA("P99b", MPN)]
S["1-1615"] = [QA("P100a", AK12)]
S["1-1616"] = [QA("P100b", A4_NOAK), END_ATTHA, END_BOOK]

# =========================================================================================
# 5. Build and checks
# =========================================================================================
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def pali_segments(path=PALI):
    segs, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
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


def vi_segments(path):
    """Vietnamese segments of a published part: block id -> lines without the id"""
    return {b: lines for b, lines in pali_segments(path)}


def norm_item(p):
    p = re.sub(r"\s*\[[^\]]*\]", "", p).rstrip(".").replace("kho pana ", "")
    ws = [w for w in p.split() if w != "dhammā"]
    if ws and ws[-1].endswith("āpi"):
        ws[-1] = ws[-1][:-2]
    return " ".join(ws)


def check_questions(segs):
    """Each 'Katame dhammā X?' must open with the Vietnamese question of a matrix item whose Pāli is X."""
    qs, prev = {}, {}
    for bid, letter, pali, _vi in M.MATRIX_ITEMS_VI:
        n = norm_item(pali)
        if letter == "b" and " " not in n and pali.rstrip(".").endswith("pi"):
            n = " ".join(prev[bid].split()[:-1] + [n])     # elliptical (b) line: na hetū … ahetukāpi
        prev[bid] = n
        if M.PRED[(bid, letter)]:
            qs.setdefault(n, set()).add(M.QUESTION((bid, letter))[:-1])
    bad = []
    for bid, plines in segs:
        pm = re.match(r"Katame dhammā (.+?)(\?|\.|…)", plines[0])
        if not pm:
            continue
        cands = qs.get(pm.group(1), set())
        if not any(S[bid][0].startswith(c) for c in cands):
            bad.append((bid, pm.group(1), S[bid][0][:80]))
    return bad


def check_same_pali(segs):
    """identical Pāli segment = identical Vietnamese, within this part and against the earlier parts"""
    seen = {}
    for name in sorted(p.name for p in B.OUT_DIR.glob("*.md")):
        if name == PART or not (B.PALI_DIR / name).exists():
            continue
        try:
            vi = vi_segments(B.OUT_DIR / name)
            psegs = pali_segments(B.PALI_DIR / name)
        except AssertionError:      # a file without block IDs on its last line (preamble)
            continue
        for bid, plines in psegs:
            if bid in vi:
                seen.setdefault(tuple(plines), (f"{name} ^{bid}", vi[bid]))
    n = 0
    for bid, plines in segs:
        k = tuple(plines)
        if k in seen:
            assert seen[k][1] == S[bid], (bid, seen[k][0], S[bid], seen[k][1])
            n += 1
        else:
            seen[k] = (f"^{bid}", S[bid])
    return n


def ndash(s):
    return s.count("–") + s.count("—")


def build():
    segs = pali_segments()
    assert len(segs) == len(S) and {b for b, _ in segs} == set(S), set(S) ^ {b for b, _ in segs}
    bad = check_questions(segs)
    assert not bad, bad
    out = []
    for bid, plines in segs:
        lines = S[bid]
        assert len(lines) == len(plines), (bid, len(plines), len(lines))
        for p, r in zip(plines, lines):
            assert ndash(p) == ndash(r), (bid, ndash(p), ndash(r), r)
            assert p.count("?") == r.count("?"), (bid, p.count("?"), r.count("?"))
            assert p.count("[") == r.count("["), (bid, p, r)
            assert p.count("…pe…") == r.count(ELL), (bid, p.count("…pe…"), r.count(ELL), r)
            assert "—" not in r and ":-" not in r and "  " not in r and ",," not in r and " ," not in r, (bid, r)
            assert ".." not in r and ", ;" not in r and "; ;" not in r and ";," not in r, (bid, r)
            assert p.startswith("#") == r.startswith("#"), (bid, p, r)
            if p.startswith("#"):
                assert HEAD[p] == r, (bid, p, r)
        lines = list(lines)
        lines[-1] += f" ^{bid}"
        out.append("\n".join(lines))
    text = "\n\n".join(out) + "\n"
    assert "—" not in text and ":-" not in text and "pe…" not in text and "\n\n\n" not in text
    assert "chánh niệm" not in text.lower()
    assert unicodedata.normalize("NFC", text) == text
    return text, segs


if __name__ == "__main__":
    print("headings checked:", check_headings())
    t, segs = build()
    print("segments with the same Pāli as an earlier or repeated segment (Vietnamese equal):", check_same_pali(segs))
    OUT.write_text(t, encoding="utf-8", newline="\n")
    print("wrote", OUT, "segments", len(S))
