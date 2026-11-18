"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapter 5 (Aṭṭhakathākaṇḍaṃ, the last chapter: every matrix item explained by the classes of mind, the cittuppāda,
and the planes, ^1-1384 … ^1-1616).

Writes (only when run as a script; both files exist already, created with the Write tool):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/5-atthakathakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-5.md

Every line is translated from the Pāli by fixed strings. The 4-02/4-03 builder (G, which loads 4-01 = F and through it
3-02/3-03, 3-01, 2-05, 2-04, 2-01/2-02 and the approved sample S) is imported, never edited. Before building, 2-01 …
3-03 and 4-01 … 4-03 are rebuilt in memory and must equal the finished files byte for byte (importing rewrites
nothing). A Pāli line that repeats a 4-0x line word for word takes that line's Vietnamese unchanged; the question and
answer frames are 1-matika's (S.q_form / S.a_form with S.PREDS, F.pred); the cluster names, the cluster definition
lists, «toàn bộ vật chất», «và loại vật chất do nghiệp đã được tạo», the four paths and the fruits are the 4-0x
strings. Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md). Translated fresh from the Pāli.

usage: python -I -X utf8 build_rails_5_vi.py
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

_spec = importlib.util.spec_from_file_location("build_rails_4_02_4_03_vi", HERE / "build_rails_4-02_4-03_vi.py")
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)        # importing writes nothing; G.F = 4-01, G.Q, G.R, G.E, G.D, G.B
F, Q, R, E, D, B = G.F, G.Q, G.R, G.E, G.D, G.B

PART = "5-atthakathakandam.md"
OUT_FILE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese"
                        r"\pi-1-vietnamese-plain-rails_split_chapters\5-atthakathakandam.md")
NOTES_FILE = HERE / "notes-5.md"
assert OUT_FILE == S.OUT / PART
cap = S.cap
PE, ELL, DASH = "…pe…", "…", "–"
P = S.PREDS
NAMES = S.NAMES
NM = F.NM
SLIPS = []
CUR = {"sid": ""}


def slip(note):
    SLIPS.append((CUR["sid"], note))


# =========================================================================================
# 1. Reuse: a Pāli line that repeats a 4-0x line word for word keeps that line's Vietnamese
# =========================================================================================
REUSE = {}
for _part in ("4-01-nikkhepakandam.md", "4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"):
    _ps, _vs = B.segments(S.PALI / _part), B.segments(S.OUT / _part)
    for (_a, _pl), (_b, _vl) in zip(_ps, _vs):
        assert _a == _b and len(_pl) == len(_vl), (_part, _a)
        for _x, _y in zip(_pl, _vl):
            assert REUSE.get(_x, _y) == _y, _x
            REUSE[_x] = _y
REUSED = []                                          # sids that took a 4-0x line

# =========================================================================================
# 2. Words and building blocks
# =========================================================================================
PLANE = "cõi"                                        # bhūmīsu (termbase «cõi»)
NUMV = {"eko": "một", "dve": "hai", "tayo": "ba", "cattāro": "bốn", "pañca": "năm", "cha": "sáu", "satta": "bảy",
        "aṭṭha": "tám", "nava": "chín", "dasa": "mười", "ekādasa": "mười một"}
KIND = "loại tâm"                                    # cittuppādā / cittuppādo / cittuppāde (termbase «loại tâm»)
KUSALA4 = f"tâm thiện thuộc bốn {PLANE}"             # catūsu bhūmīsu kusalaṃ (kusalaṃ «thiện», the wholesome mind)
KUSALA3 = f"tâm thiện thuộc ba {PLANE}"
AKUSALA = "tâm bất thiện"                            # akusalaṃ
VIPAKA4 = f"quả của nghiệp thuộc bốn {PLANE}"         # catūsu bhūmīsu vipāko (vipāka «quả của nghiệp»)
VIPAKA3 = f"quả của nghiệp thuộc ba {PLANE}"
FUNC = "mang tính chức năng"                         # kiriyā / kiriya (termbase; kiriyato «chức năng» inside it)
KIRIYA_BY = f"tâm {FUNC} không xác định về mặt đạo đức"   # kiriyābyākataṃ (termbase «chức năng không xác định …»)
KIRIYA3 = f"{KIRIYA_BY} thuộc ba {PLANE}"
KAMA = P["kāmāvacarā"]                               # thuộc cõi dục lạc
RUPAV = P["rūpāvacarā"]                              # thuộc cõi hình sắc
ARUPAV = P["arūpāvacarā"]                            # thuộc cõi không hình sắc
LOKUT = P["lokuttarā"]                               # vượt thế gian
NIB = "Niết-bàn"
RUPA_NIB = f"{R.RUPA} và {NIB}"                      # rūpañca, nibbānañca (termbase «vật chất và Niết-bàn»)
SAB = F.SAB                                          # toàn bộ vật chất (sabbañca rūpaṃ)
FOUR_PATHS = F.FOUR_PATHS                            # bốn con đường không nằm trong các cõi tồn tại
FRUITS4 = "bốn thành quả của đời sống sa-môn"        # cattāri ca sāmaññaphalāni
IN_THEM = "sinh khởi trong đó"                       # etthuppanna- (uppanne hetū «gốc rễ sinh khởi», ettha «trong đó»)
EXCEPT = "ngoại trừ"                                 # ṭhapetvā
REMAIN_AK = f"{AKUSALA} còn lại"                     # avasesaṃ akusalaṃ (termbase «bất thiện còn lại»)
NO_ROOT_V = f"các {KIND} không có gốc rễ trong quả của nghiệp {KAMA}"     # kāmāvacarassa vipākato ahetuke cittuppāde
NO_ROOT_K = f"các {KIND} không có gốc rễ trong tâm {FUNC} {KAMA}"      # kāmāvacarakiriyato ahetuke cittuppāde
DITTHI_SAM = "gắn liền với sự mắc kẹt trong các quan điểm"                # diṭṭhigatasampayutta
DITTHI_VIP = "không gắn liền với sự mắc kẹt trong các quan điểm"          # diṭṭhigatavippayutta (termbase)
LOBHA_W = "có sự tham lam đi kèm"                                         # lobhasahagata
DOMAN_W = "có nỗi buồn đi kèm"                                            # domanassasahagata
VICI_W = "có sự hoài nghi đi kèm"                                         # vicikicchāsahagata
UDDH_W = "có sự xao động đi kèm"                                          # uddhaccasahagata
MOHA = NM["moho"]
MOHA_VICI = f"{MOHA} {VICI_W}"
MOHA_UDDH = f"{MOHA} {UDDH_W}"
FOUR_DV_LOBHA = f"bốn {KIND} {LOBHA_W}, {DITTHI_VIP}"   # diṭṭhigatavippayutta(-)lobhasahagata (lobha … vippayutta)
FOUR_DS_LOBHA = f"bốn {KIND} {LOBHA_W}, {DITTHI_SAM}"
FOUR_DS = f"bốn {KIND} {DITTHI_SAM}"
TWO_DOMAN = f"hai {KIND} {DOMAN_W}"
EIGHT_LOBHA = f"tám {KIND} {LOBHA_W}"
TWELVE_AK = f"mười hai {KIND} bất thiện"            # Dvādasa akusalacittuppādā (2-04 ^1-430 «Mười hai loại tâm bất thiện»)
ARUPA = B.ARUPA
ACC = {   # kusalato / vipākato / kiriyato (termbase «thiện», «quả của nghiệp», «chức năng»)
    " kusalato ca vipākato ca kiriyato ca": ", ở dạng thiện, quả của nghiệp và chức năng",
    " kusalato ca vipākato ca": ", ở dạng thiện và quả của nghiệp",
    " kusalato ca kiriyato ca": ", ở dạng thiện và chức năng",
}
COUNT = {"ekaka": "một", "duka": "hai", "tika": "ba", "catukka": "bốn", "pañcaka": "năm"}
JH = "tầng thiền"
ORD = {"paṭhamaṃ": "thứ nhất", "dutiyaṃ": "thứ hai", "catutthaṃ": "thứ tư"}
FIVEFOLD = "theo phương pháp chia năm"               # pañcakanaye (termbase)
CU_ATTR = {"somanassasahagata": "có niềm vui đi kèm", "upekkhāsahagata": "có sự bình thản đi kèm",
           "ñāṇavippayutta": "không gắn liền với hiểu biết", "ñāṇasampayutta": "gắn liền với hiểu biết"}


def jset(a, b, sphere):
    """rūpāvacara / lokuttara + <a><b> + jjhānā (termbase lokuttaratikacatukkajjhānā)"""
    return f"{COUNT[a]} {JH} {sphere} theo phương pháp chia bốn và {COUNT[b]} {JH} {FIVEFOLD}"


assert jset("tika", "catukka", LOKUT) == ("ba tầng thiền vượt thế gian theo phương pháp chia bốn và bốn tầng thiền "
                                          "theo phương pháp chia năm")

# =========================================================================================
# 3. Pieces of the answer lists: Pāli (first letter lowered) -> (kind, Vietnamese)
#    kinds: x (an item), xc (an item with «ca»: «và» when it closes the list), pair (carries its own «và»),
#           ex (an exception, joined to the item before it with «, »), pre (an exception that opens the list)
# =========================================================================================
PIECES = {
    "catūsu bhūmīsu kusalaṃ": ("x", KUSALA4),
    "tīsu bhūmīsu kusalaṃ": ("x", KUSALA3),
    "akusalaṃ": ("x", AKUSALA),
    "sabbaṃ akusalaṃ": ("x", f"toàn bộ {AKUSALA}"),         # sabbaṃ «toàn bộ»
    "catūsu bhūmīsu vipāko": ("x", VIPAKA4),
    "tīsu bhūmīsu vipāko": ("x", VIPAKA3),
    "tīsu bhūmīsu kiriyābyākataṃ": ("x", KIRIYA3),
    "rūpañca, nibbānañca": ("pair", RUPA_NIB),
    "rūpañca nibbānañca": ("pair", RUPA_NIB),
    "nibbānañca": ("xc", NIB),
    "nibbānaṃ": ("x", NIB),
    "sabbañca rūpaṃ": ("xc", SAB),
    "kāmāvacarakusalaṃ": ("x", f"tâm thiện {KAMA}"),
    "kāmāvacaraṃ kusalaṃ": ("x", f"tâm thiện {KAMA}"),
    "sabbo kāmāvacarassa vipāko": ("x", f"toàn bộ quả của nghiệp {KAMA}"),
    "kāmāvacarakiriyābyākataṃ": ("x", f"{KIRIYA_BY} {KAMA}"),
    "rūpāvacarā, arūpāvacarā, kusalābyākatā": ("x", f"các hiện tượng {F.QV['kusalābyākatā']}, {RUPAV} và {ARUPAV}"),
    "kiriyāmanodhātu": ("x", "yếu tố ý mang tính chức năng"),   # Kiriyāmanodhātu (termbase)
    "kiriyāhetukamanoviññāṇadhātu somanassasahagatā":
        ("x", f"yếu tố ý thức mang tính chức năng không có gốc rễ, {CU_ATTR['somanassasahagata']}"),
    "kiriyāhetukamanoviññāṇadhātu upekkhāsahagatā":
        ("x", f"yếu tố ý thức mang tính chức năng không có gốc rễ, {CU_ATTR['upekkhāsahagata']}"),
    "akusalassa vipākato manoviññāṇadhātu upekkhāsahagatā":
        ("x", f"yếu tố ý thức là quả của nghiệp bất thiện, {CU_ATTR['upekkhāsahagata']}"),   # as 2-05's heading
    "catutthassa jhānassa vipāko": ("x", f"quả của nghiệp thuộc {JH} thứ tư"),
    "dvādasa akusalacittuppādā": ("x", TWELVE_AK),
    "dvādasākusalacittuppādā": ("x", TWELVE_AK),
    "cattāro diṭṭhigatasampayuttacittuppādā": ("x", FOUR_DS),
    "cattāro diṭṭhigatavippayuttā lobhasahagatacittuppādā": ("x", FOUR_DV_LOBHA),
    "cattāro diṭṭhigatavippayuttalobhasahagatacittuppādā": ("x", FOUR_DV_LOBHA),
    "cattāro diṭṭhigatasampayuttalobhasahagatacittuppādā": ("x", FOUR_DS_LOBHA),
    "dve domanassasahagatacittuppādā": ("x", TWO_DOMAN),
    "aṭṭha lobhasahagatacittuppādā": ("x", EIGHT_LOBHA),
    "vicikicchāsahagato cittuppādo": ("x", f"{KIND} {VICI_W}"),
    "uddhaccasahagato cittuppādo": ("x", f"{KIND} {UDDH_W}"),
    "vicikicchāsahagato moho": ("x", MOHA_VICI),
    "uddhaccasahagato moho": ("x", MOHA_UDDH),
    "dukkhasahagataṃ kāyaviññāṇaṃ": ("x", "thức qua thân có sự khó chịu đi kèm"),   # 2-05 ^1-556 (APPROVED 1)
    "dukkhasahagatakāyaviññāṇaṃ": ("x", "thức qua thân có sự khó chịu đi kèm"),
    "yā ca vedanā upekkhā": ("xc", f"loại cảm giác là {B.NAMES['upekkhā']}"),
    "tisso ca vedanā": ("xc", "ba loại cảm giác"),
    "dvepañcaviññāṇāni": ("x", "hai nhóm năm loại thức"),      # pañcaviññāṇāni «năm loại thức», dve «hai»
    "tisso ca manodhātuyo": ("xc", "ba yếu tố ý"),
    "pañca ca ahetukamanoviññāṇadhātuyo": ("xc", "năm yếu tố ý thức không có gốc rễ"),
    "cattāro maggā apariyāpannā, cattāri ca sāmaññaphalāni, nibbānañca": ("pair", f"{FOUR_PATHS}, {FRUITS4} và {NIB}"),
    "cattāro maggā apariyāpannā, cattāri ca sāmaññaphalāni nibbānañca": ("pair", f"{FOUR_PATHS}, {FRUITS4} và {NIB}"),
    "cattāro maggā apariyāpannā, cattāri ca sāmaññaphalāni": ("pair", f"{FOUR_PATHS} và {FRUITS4}"),
    "cattāro maggā apariyāpannā cattāri ca sāmaññaphalāni": ("pair", f"{FOUR_PATHS} và {FRUITS4}"),
    "cattāro maggā apariyāpannā": ("x", FOUR_PATHS),
    "cattāri ca sāmaññaphalāni": ("xc", FRUITS4),
    "upariṭṭhimaṃ arahattaphalaṃ": ("x", "thành quả A-la-hán cao nhất"),   # 4-01 ^1-1024 without the variant
    "yañca rūpaṃ kammassa katattā": ("pair", f"{F.RUPA_KIND} {F.YANCA['kammassa katattā']}"),
    "yañca rūpaṃ na kammassa katattā": ("pair", f"{F.RUPA_KIND} {F.YANCA['na kammassa katattā']}"),
    "yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ":
        ("pair", f"{F.RUPA_KIND} {F.YANCA['anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ']}"),
    "rūpāyatanaṃ": F.FIXED["Rūpāyatanaṃ"],
    "cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ": F.FIXED["Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ"],
    "cakkhāyatanaṃ …pe… phoṭṭhabbāyatanaṃ": F.FIXED["Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ"],
    "cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ":
        F.FIXED["Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ"],
    "cattāro ca mahābhūtā": ("xc", F.FIXED["cattāro ca mahābhūtā"][1]),
    "vedanākkhandho, saññākkhandho, saṅkhārakkhandho": ("x", G.KH3V),
    "cittañca": ("x", F.FIXED["Cittañca"][1]),
    "avasesañca rūpaṃ": ("x", F.FIXED["avasesañca rūpaṃ"][1]),
    "kāyaviññatti, vacīviññatti": ("x", G.VINNATTI2),
    G.CITTAJA_P.replace("cittasamuṭṭhānaṃ rūpāyatanaṃ", f"cittasamuṭṭhānaṃ {DASH} rūpāyatanaṃ"):
        ("x", G.CITTAJA_V.replace(f"{Q.CITTAJA}: ", f"{Q.CITTAJA} {DASH} ", 1)),   # ^1-1535: a dash before the list
    "vitakko ca": ("xc", S.FN["vitakko"]),
    "vicāro ca": ("xc", S.FN["vicāro"]),
    "pīti ca": ("xc", S.FN["pīti"]),
    "sukhañca": ("xc", S.FN["sukhaṃ"]),
    "upekkhā ca": ("xc", B.NAMES["upekkhā"]),
    "pañcakanaye dutiye jhāne [dutiyajjhāne (sī.)], uppanno ca vicāro":
        ("x", f"{S.FN['vicāro']} sinh khởi trong {JH} thứ hai {S.spell('Sī.', 'dutiyajjhāne')} {FIVEFOLD}"),
    "yattha dve tayo hetū ekato uppajjanti": ("x", "Ở nơi hai hoặc ba gốc rễ cùng sinh khởi"),
    "yattha dve tayo āsavā ekato uppajjanti": ("x", "Ở nơi hai hoặc ba ô nhiễm cùng sinh khởi"),
    "yattha dve tīṇi saṃyojanāni ekato uppajjanti": ("x", "Ở nơi hai hoặc ba xiềng xích cùng sinh khởi"),
    "yattha dve tīṇi nīvaraṇāni ekato uppajjanti": ("x", "Ở nơi hai hoặc ba chướng ngại cùng sinh khởi"),
    "yattha dve tayo kilesā ekato uppajjanti": ("x", "Ở nơi hai hoặc ba phiền não cùng sinh khởi"),
    "yattha diṭṭhi ca lobho ca ekato uppajjanti": ("x", f"Ở nơi {NM['diṭṭhi']} và {NM['lobho']} cùng sinh khởi"),
    "dvīsu domanassasahagatesu cittuppādesu uppanno moho": ("x", f"{MOHA} sinh khởi trong {TWO_DOMAN}"),
    "catūsu diṭṭhigatavippayuttalobhasahagatesu cittuppādesu uppanno lobho":
        ("x", f"{NM['lobho']} sinh khởi trong {FOUR_DV_LOBHA}"),
    "dvīsu domanassasahagatesu cittuppādesu uppannaṃ paṭighaṃ": ("x", f"sự ác cảm sinh khởi trong {TWO_DOMAN}"),
    # exceptions that open the list
    "ṭhapetvā hetū": ("pre", f"{EXCEPT} các gốc rễ"),
    "rūpaṃ ṭhapetvā, sabbeva kāmāvacarā kusalākusalābyākatā dhammā":
        ("x", f"{EXCEPT} {R.RUPA}, tất cả các hiện tượng {F.QV['kusalākusalābyākatā']}, {KAMA}"),   # 4-01 «tất cả …»
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ ṭhapetvā avasesaṃ akusalaṃ":
        ("x", f"{EXCEPT} {MOHA_VICI} và {MOHA_UDDH}, {REMAIN_AK}"),
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ ṭhapetvā, avasesaṃ akusalaṃ":
        ("x", f"{EXCEPT} {MOHA_VICI} và {MOHA_UDDH}, {REMAIN_AK}"),
    "uddhaccasahagataṃ mohaṃ ṭhapetvā avasesaṃ akusalaṃ": ("x", f"{EXCEPT} {MOHA_UDDH}, {REMAIN_AK}"),
    "kāmāvacarassa vipākato ahetuke cittuppāde ṭhapetvā catūsu bhūmīsu vipāko":
        ("x", f"{VIPAKA4}, {EXCEPT} {NO_ROOT_V}"),
    "kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā tīsu bhūmīsu kiriyābyākataṃ":
        ("x", f"{KIRIYA3}, {EXCEPT} {NO_ROOT_K}"),
    "kāmāvacarakusalassa vipākato ca kiriyato ca pañca":
        ("x", f"năm {KIND} là quả của nghiệp thiện {KAMA} và năm {KIND} {FUNC}"),
}
SLIP_PIECES = {
    "kāmāvacarakusalassa vipākato ca kiriyato ca pañca":
        "«kāmāvacarakusalassa vipākato ca kiriyato ca pañca»: five of each (as ^1-1402 «vipākato pañca, kiriyato "
        "pañca»), rendered «năm … và năm …»",
    "cakkhāyatanaṃ …pe… phoṭṭhabbāyatanaṃ": "a space before «…pe…»: rendered as the parallels",
    "cattāro maggā apariyāpannā, cattāri ca sāmaññaphalāni nibbānañca": "a missing comma: rendered as meant",
    "cattāro maggā apariyāpannā cattāri ca sāmaññaphalāni": "a missing comma: rendered as meant",
    "pañcakanaye dutiye jhāne [dutiyajjhāne (sī.)], uppanno ca vicāro":
        "the comma stands after the variant, inside «pañcakanaye dutiye jhāne … uppanno ca vicāro» (the vicāra "
        "arisen in the second jhāna of the fivefold method): rendered as one item",
}
# the ablative counts: «N loại tâm …»
for _n, _nv in NUMV.items():
    for _a, _av in CU_ATTR.items():
        PIECES[f"kāmāvacarakusalato {_n} {_a}cittuppādā"] = ("x", f"{_nv} {KIND} thiện {KAMA} {_av}")
        PIECES[f"kiriyato {_n} {_a}cittuppādā"] = ("x", f"{_nv} {KIND} {FUNC} {_av}")
    PIECES[f"akusalato {_n}"] = ("x", f"{_nv} {KIND} bất thiện")
    for _tail in ("", " cittuppādā"):
        PIECES[f"kāmāvacarakusalassa vipākato {_n}{_tail}"] = ("x", f"{_nv} {KIND} là quả của nghiệp thiện {KAMA}")
        PIECES[f"akusalassa vipākato {_n}{_tail}"] = ("x", f"{_nv} {KIND} là quả của nghiệp bất thiện")
        PIECES[f"kiriyato {_n}{_tail}"] = ("x", f"{_nv} {KIND} {FUNC}")
# the jhānas
_JHEADS = {}
for _a, _b in (("tika", "catukka"), ("tika", "tika"), ("duka", "tika"), ("duka", "duka"), ("ekaka", "duka"),
               ("catukka", "pañcaka")):
    _JHEADS[f"rūpāvacara{_a}{_b}jjhānā"] = jset(_a, _b, RUPAV)
    _JHEADS[f"lokuttara{_a}{_b}jjhānā"] = jset(_a, _b, LOKUT)
for _o, _ov in ORD.items():
    _JHEADS[f"rūpāvacaraṃ {_o} jhānaṃ"] = f"{JH} {_ov} {RUPAV}"
    _JHEADS[f"lokuttaraṃ {_o} jhānaṃ"] = f"{JH} {_ov} {LOKUT}"
_JHEADS["rūpāvacaracatutthaṃ jhānaṃ"] = f"{JH} thứ tư {RUPAV}"
_JHEADS["rūpāvacarapañcakanaye dutiyaṃ jhānaṃ"] = f"{JH} thứ hai {RUPAV} {FIVEFOLD}"
_JHEADS["lokuttarapañcakanaye dutiyaṃ jhānaṃ"] = f"{JH} thứ hai {LOKUT} {FIVEFOLD}"
_JHEADS["cattāro arūpāvacarā"] = f"bốn {KIND} {ARUPAV}"
_JHEADS["cattāro āruppā"] = f"bốn {JH} không hình sắc"     # āruppā (termbase «tầng thiền không hình sắc»)
assert _JHEADS["lokuttarapañcakanaye dutiyaṃ jhānaṃ"] == "tầng thiền thứ hai vượt thế gian theo phương pháp chia năm"
for _h, _hv in _JHEADS.items():
    for _m, _mv in ACC.items():
        PIECES[_h + _m] = ("x", _hv + _mv)
# the immaterial bases
for _k, _v in ARUPA.items():
    PIECES[_k + "ṃ"] = ("x", _v)
# etthuppanna- … ṭhapetvā
_EX_OBJ = {
    "etthuppannaṃ sukhaṃ vedanaṃ": F.EXCL["sukhaṃ vedanaṃ"], "etthuppannaṃ dukkhaṃ vedanaṃ": F.EXCL["dukkhaṃ vedanaṃ"],
    "etthuppannaṃ adukkhamasukhaṃ vedanaṃ": F.EXCL["adukkhamasukhaṃ vedanaṃ"],
    "etthuppanne vitakkavicāre": F.EXCL["vitakkavicāre"], "etthuppannaṃ vicāraṃ": F.EXCL["vicāraṃ"],
    "etthuppannaṃ vitakkaṃ": F.EXCL["vitakkaṃ"], "etthuppannaṃ pītiṃ": F.EXCL["pītiṃ"],
    "etthuppannaṃ sukhaṃ": F.EXCL["sukhaṃ"], "etthuppannaṃ upekkhaṃ": F.EXCL["upekkhaṃ"],
    "etthuppannaṃ mohaṃ": MOHA, "etthuppannaṃ lobhaṃ": NM["lobho"], "etthuppannaṃ paṭighaṃ": "sự ác cảm",
    "etthuppannaṃ parāmāsaṃ": "sự hiểu sai lệch", "etthuppanne hetū": "các gốc rễ",
    "etthuppanne ganthe": "các nút thắt", "etthuppanne upādāne": "các sự bám víu",
}
for _k, _v in _EX_OBJ.items():
    PIECES[f"{_k} ṭhapetvā"] = ("ex", f"{EXCEPT} {_v} {IN_THEM}")
# «Ṭhapetvā X avasesaṃ akusalaṃ»
for _k, _v in {"āsave": "các ô nhiễm", "saṃyojane": "các xiềng xích", "ganthe": "các nút thắt",
               "nīvaraṇe": "các chướng ngại", "parāmāsaṃ": "sự hiểu sai lệch", "upādāne": "các sự bám víu",
               "kilese": "các phiền não"}.items():
    for _sep in (" ", ", "):
        PIECES[f"ṭhapetvā {_k}{_sep}avasesaṃ akusalaṃ"] = ("x", f"{EXCEPT} {_v}, {REMAIN_AK}")
PKEYS = sorted(PIECES, key=len, reverse=True)

# =========================================================================================
# 4. The answer lists
# =========================================================================================
END = re.compile(r"(?=$|[ ,\[])")


def items_vi(body):
    """«a, b, c» -> [(kind, Vietnamese, Pāli key)], noting missing commas between items"""
    out, rest, prev_sep = [], body, None
    while rest:
        low = rest[0].lower() + rest[1:]
        for k in PKEYS:
            if low.startswith(k) and END.match(low, len(k)):
                break
        else:
            raise KeyError("piece: " + rest[:90])
        kind, v = PIECES[k]
        if k in SLIP_PIECES:
            slip(SLIP_PIECES[k])
        if prev_sep == " " and kind not in ("ex",) and out and out[-1][0] != "pre":
            slip("missing comma(s) between the items of the list: rendered as meant")
        out.append((kind, v, k))
        rest = rest[len(k):]
        m = re.match(r",? ?", rest)
        prev_sep = "," if rest.startswith(",") else (" " if rest.startswith(" ") else None)
        rest = rest[m.end():]
    return out


def body_vi(body):
    """an answer list -> items joined with «; » (as 4-01 … 4-03), exceptions with «, », «và» before a closing «ca»"""
    if body in FS:
        return FS[body]
    if "uppajja" in body and not body.lower().startswith("yattha"):
        return arise_multi(body)
    its = items_vi(body)
    groups = []
    for kind, v, _ in its:
        if kind == "ex":
            groups[-1][1] = f"{groups[-1][1]}, {v}"
        elif groups and groups[-1][0] == "pre":
            groups[-1] = [kind, f"{groups[-1][1]}, {v}"]
        else:
            groups.append([kind, v])
    if len(groups) > 1 and groups[-1][0] == "xc":
        groups[-1][1] = "và " + groups[-1][1]
    return cap("; ".join(v for _, v in groups))


# =========================================================================================
# 5. «… uppajjati / uppajjanti» (the cluster answers, the roots)
# =========================================================================================
LOC = {
    "aṭṭhasu lobhasahagatesu cittuppādesu": f"trong {EIGHT_LOBHA}",
    "dvīsu domanassasahagatesu cittuppādesu": f"trong {TWO_DOMAN}",
    "catūsu diṭṭhigatavippayuttalobhasahagatesu cittuppādesu": f"trong {FOUR_DV_LOBHA}",
    "catūsu diṭṭhigatasampayuttesu cittuppādesu": f"trong {FOUR_DS}",
    "vicikicchāsahagatesu cittuppādesu": f"trong các {KIND} {VICI_W}",
    "uddhaccasahagatesu cittuppādesu": f"trong các {KIND} {UDDH_W}",
    "sasaṅkhārikesu akusalesu": f"trong các {AKUSALA} có sự thúc đẩy",   # sasaṅkhārikesu «có sự thúc đẩy»
    "sabbākusalesu": f"trong tất cả các {AKUSALA}",
    "catūsu bhūmīsu kusalesu": f"trong các {KUSALA4}",
    "catūsu bhūmīsu vipākesu": f"trong các {VIPAKA4}",
    "tīsu bhūmīsu kiriyesu": f"trong các tâm {FUNC} thuộc ba {PLANE}",   # kiriyesu «chức năng»
}
ARISE = "sinh khởi"                                  # uppajjati / uppajjanti
ARISE_RE = re.compile(r"(?P<s>.+?) (?P<l>" + "|".join(re.escape(k) for k in sorted(LOC, key=len, reverse=True)) +
                      r") (?:uppajjati|uppajjanti)")


def subj_names(s):
    """Kāmāsavo / Issāsaṃyojanañca macchariyasaṃyojanañca / X kāyagantho ca Y kāyagantho ca -> names"""
    s = s[0].lower() + s[1:]
    if s.endswith("ñca"):
        parts = [p + "ṃ" for p in re.findall(r"(\S+?)ñca(?: |$)", s)]
    elif s.endswith(" ca"):
        parts = [p.strip() for p in s.split(" ca") if p.strip()]
    else:
        parts = [s]
    vs = [NM[p] for p in parts]
    last = ", và " if any(" và " in v for v in vs) else " và "   # «giới hạnh và nghi thức, và …»: no «… và … và …»
    return vs[0] if len(vs) == 1 else ", ".join(vs[:-1]) + last + vs[-1]


def arise_one(c):
    m = ARISE_RE.fullmatch(c)
    if not m:
        raise KeyError("arise: " + c[:90])
    return f"{cap(subj_names(m.group('s')))} {ARISE} {LOC[m.group('l')]}"


def arise_multi(text):
    parts = re.split(r"(?:(?<=uppajjati)|(?<=uppajjanti))(,?) ", text)
    out = arise_one(parts[0])
    for sep, c in zip(parts[1::2], parts[2::2]):
        if sep == ",":
            out += ", " + arise_one(c)[0].lower() + arise_one(c)[1:]
        else:
            slip("a missing full stop between the clauses: rendered as meant")
            out += ". " + arise_one(c)
    return out


# =========================================================================================
# 6. Predicates: «siyā X», «na X», «na vattabbā Xtipi, Ytipi»
# =========================================================================================
SOMETIMES = "đôi khi"                                # siyā (termbase)
NOT_SAY = "không nên nói"                            # na vattabbā / vattabbo / vattabbaṃ (termbase «nên nói»)
THAT, OR_THAT = "rằng", "hay rằng"                   # Xtipi … Ytipi (4-02 «Về tâm thì không nên nói – rằng …, hay rằng …»)
SLIP_ITEMS = {"ya vedanāya sampayuttā": ("adukkhamasukhāya vedanāya sampayuttā",
                                         "«ya vedanāya sampayuttātipi» is a clipped «adukkhamasukhāya vedanāya "
                                         "sampayuttātipi» (the third feeling): rendered as the full matrix item")}


def lookup(x):
    """an item of a predicate (any ending: -ātipi, -otipi, -antipi, -aṃ, -cātipi …) -> its matrix Pāli key"""
    x = x.strip()
    cands = [x]
    for suf in ("tipi", "ti"):
        if x.endswith(suf):
            cands.append(x[:-len(suf)])
    more = []
    for c in cands:
        if c.endswith("cā"):
            more.append(c[:-1] + "a")
        if c.endswith("an") or c.endswith("aṃ"):
            more.append(c[:-2] + "ā")
        if c.endswith("o"):
            more.append(c[:-1] + "ā")
    for c in cands + more:
        if c in SLIP_ITEMS:
            slip(SLIP_ITEMS[c][1])
            return SLIP_ITEMS[c][0]
        if c in P or c in F.PRED_X:
            return c
    raise KeyError("item: " + x)


def neg(key):
    if "na " + key in P:
        return P["na " + key]
    v = F.pred(key)
    return "không phải " + v if v.startswith("là ") else "không " + v


def pred_vi(subject, pred, first_cap=False):
    """subject + the clauses of the predicate; «về <subject> thì không nên nói …» when it opens with na vattabbā"""
    if re.search(r"[^,;] siyā ", pred):
        slip("«siyā … siyā …» without a comma: rendered as meant")
        pred = re.sub(r"(?<=[^,;]) (?=siyā )", ", ", pred)
    parts = re.split(r"(, |; )", pred)
    out, mode, about = [], False, False
    for i, c in enumerate(parts[::2]):
        m = re.match(r"(siyā )?na vattabb(?:ā|o|aṃ) (– )?(.+)$", c)
        if m:
            mode = True
            if i == 0 and not m.group(1):
                about = True
            dash = f" {DASH}" if m.group(2) else ""
            v = f"{SOMETIMES + ' ' if m.group(1) else ''}{NOT_SAY}{dash} {THAT} {F.pred(lookup(m.group(3)))}"
        elif mode and (c.endswith("tipi") or c.endswith("ti")) and not c.startswith("siyā "):
            v = f"{OR_THAT} {F.pred(lookup(c))}"
        elif c.startswith("siyā "):
            mode = False
            c2 = c[len("siyā "):]
            v = f"{SOMETIMES} {neg(lookup(c2[3:])) if c2.startswith('na ') and c2 not in P else F.pred(lookup(c2))}"
        elif c.startswith("na ") and c not in P:
            mode = False
            v = neg(lookup(c[3:]))
        else:
            mode = False
            v = F.pred(lookup(c))
        out.append(v)
    joined = "".join(v + (parts[2 * i + 1] if 2 * i + 1 < len(parts) else "") for i, v in enumerate(out))
    s = f"về {subject} thì {joined}" if about else f"{subject} {joined}"
    return (cap(s) if first_cap else s) + "."


SUBJ = {
    "ime dhammā": "những hiện tượng này",
    "Pīti": S.FN["pīti"],
    "Sukhaṃ": S.FN["sukhaṃ"],
    "Cattāro ariyamaggā": "bốn con đường cao quý",   # Ariyamagga (termbase «con đường cao quý»)
    "Nibbānaṃ ṭhapetvā sabbe dhammā": f"{EXCEPT} {NIB}, tất cả các hiện tượng",
    "Nibbānaṃ": NIB,
    "Anindriyabaddharūpañca nibbānañca ṭhapetvā, sabbe dhammā":
        f"{EXCEPT} {R.RUPA} không gắn kết với các năng lực và {NIB}, tất cả các hiện tượng",
    "Anindriyabaddharūpañca nibbānañca": f"{R.RUPA} không gắn kết với các năng lực và {NIB}",
    "Rūpañca nibbānañca": RUPA_NIB,
    "Ākiñcaññāyatanaṃ": ARUPA["ākiñcaññāyatana"],
    "Vitakkasahajāto vicāro": f"{S.FN['vicāro']} cùng sinh khởi với {S.FN['vitakko']}",   # sahajāto «cùng sinh khởi»
    "Parāmāso": "sự hiểu sai lệch",
    "Parāmāsā ca parāmāsasampayuttā ca dhammā":
        f"các hiện tượng {NAMES['parāmāsā']} và các hiện tượng {NAMES['parāmāsasampayuttā']}",
}
SUBJ_KEYS = sorted(SUBJ, key=len, reverse=True)
X_DHAMMA = re.compile(r"(\S+) dhammā (?=na vattabbā )")


def subject_sentence(s):
    core = s[:-1]
    for k in SUBJ_KEYS:
        if core.startswith(k + " "):
            return pred_vi(SUBJ[k], core[len(k) + 1:], True)
    m = X_DHAMMA.match(core)
    if m:
        return pred_vi(f"các hiện tượng {NAMES[m.group(1).lower()]}", core[m.end():], True)
    raise KeyError("sentence: " + s[:90])


# =========================================================================================
# 7. Fixed sentences (without their final mark)
# =========================================================================================
def names_list(keys):
    return ", ".join(NM[k] for k in keys)


ROOT_K = "gốc rễ thiện"                              # kusalahetu
ROOT_V = "gốc rễ là quả của nghiệp"                  # vipākahetu (termbase)
ROOT_F = "gốc rễ mang tính chức năng"                # kiriyahetu (termbase)
NO_KNOW4 = f"bốn {KIND} không gắn liền với hiểu biết"          # cattāro ñāṇavippayutte cittuppāde
NO_KNOW4_K = f"bốn {KIND} thiện {KAMA} không gắn liền với hiểu biết"   # kāmāvacarakusalato cattāro …
A_, D_, M_ = NM["alobho"], NM["adoso"], NM["amoho"]
FS = {
    "Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū":
        cap(F.hetus("Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū")),
    "Alobho kusalahetu, adoso kusalahetu, catūsu bhūmīsu kusalesu uppajjanti":
        f"{cap(A_)}, {ROOT_K}, và {D_}, {ROOT_K}, {ARISE} {LOC['catūsu bhūmīsu kusalesu']}",
    ("Amoho kusalahetu, kāmāvacarakusalato cattāro ñāṇavippayutte cittuppāde ṭhapetvā, catūsu bhūmīsu kusalesu "
     "uppajjati"):
        f"{cap(M_)}, {ROOT_K}, {ARISE} {LOC['catūsu bhūmīsu kusalesu']}, {EXCEPT} {NO_KNOW4_K}",
    ("Alobho vipākahetu adoso vipākahetu, kāmāvacarassa vipākato ahetuke cittuppāde ṭhapetvā, catūsu bhūmīsu "
     "vipākesu uppajjanti"):
        f"{cap(A_)}, {ROOT_V}, và {D_}, {ROOT_V}, {ARISE} {LOC['catūsu bhūmīsu vipākesu']}, {EXCEPT} {NO_ROOT_V}",
    ("Amoho vipākahetu, kāmāvacarassa vipākato ahetuke cittuppāde ṭhapetvā, cattāro ñāṇavippayutte cittuppāde "
     "ṭhapetvā, catūsu bhūmīsu vipākesu uppajjati"):
        (f"{cap(M_)}, {ROOT_V}, {ARISE} {LOC['catūsu bhūmīsu vipākesu']}, {EXCEPT} {NO_ROOT_V}, "
         f"{EXCEPT} {NO_KNOW4}"),
    ("Alobho kiriyahetu adoso kiriyahetu, kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā, tīsu bhūmīsu kiriyesu "
     "uppajjanti"):
        f"{cap(A_)}, {ROOT_F}, và {D_}, {ROOT_F}, {ARISE} {LOC['tīsu bhūmīsu kiriyesu']}, {EXCEPT} {NO_ROOT_K}",
    ("Amoho kiriyahetu, kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā, cattāro ñāṇavippayutte cittuppāde "
     "ṭhapetvā, tīsu bhūmīsu kiriyesu uppajjati"):
        (f"{cap(M_)}, {ROOT_F}, {ARISE} {LOC['tīsu bhūmīsu kiriyesu']}, {EXCEPT} {NO_ROOT_K}, "
         f"{EXCEPT} {NO_KNOW4}"),
    "Cattāro ganthā – abhijjhākāyagantho, byāpādo kāyagantho, sīlabbataparāmāso kāyagantho, idaṃsaccābhiniveso "
    "kāyagantho":
        f"Bốn nút thắt {DASH} " + names_list(["abhijjhākāyagantho", "byāpādo kāyagantho",
                                              "sīlabbataparāmāso kāyagantho", "idaṃsaccābhiniveso kāyagantho"]),
    ("Cha nīvaraṇā – kāmacchandanīvaraṇaṃ, byāpādanīvaraṇaṃ, thinamiddhanīvaraṇaṃ, uddhaccakukkuccanīvaraṇaṃ, "
     "vicikicchānīvaraṇaṃ, avijjānīvaraṇaṃ"):
        f"Sáu chướng ngại {DASH} " + names_list(["kāmacchandanīvaraṇaṃ", "byāpādanīvaraṇaṃ", "thinamiddhanīvaraṇaṃ",
                                                 "uddhaccakukkuccanīvaraṇaṃ", "vicikicchānīvaraṇaṃ",
                                                 "avijjānīvaraṇaṃ"]),
    "Cattāri upādānāni – kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ":
        f"Bốn sự bám víu {DASH} " + names_list(["kāmupādānaṃ", "diṭṭhupādānaṃ", "sīlabbatupādānaṃ",
                                                "attavādupādānaṃ"]),
    "Dasa kilesavatthūni – lobho, doso, moho, māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirikaṃ, anottappaṃ":
        f"Mười chỗ dựa của phiền não {DASH} " + names_list(["lobho", "doso", "moho", "māno", "diṭṭhi", "vicikicchā",
                                                             "thinaṃ", "uddhaccaṃ", "ahirikaṃ", "anottappaṃ"]),
    "Teva āsavā āsavā ceva sāsavā ca": F.FIXED_SENT["Teyeva āsavā āsavā ceva sāsavā ca."][:-1],
    "So eva parāmāso parāmāso ceva parāmaṭṭho ca": F.FIXED_SENT["Sveva parāmāso parāmāso ceva parāmaṭṭho ca."][:-1],
    "Niyogā anāgatārammaṇā natthi": f"Không có hiện tượng nào nhất thiết {P['anāgatārammaṇā']}",
    "Sabbe [sabbeva (syā.)] dhammā kenaci viññeyyā, kenaci na viññeyyā":
        f"Tất cả các hiện tượng {S.reading('Syā.', 'sabbeva')} đều {F.PRED_X['kenaci viññeyyā, kenaci na viññeyyā']}",
}
# the 4-02 nīvaraṇa / kilesa lists end in the same names: check them against 4-02's sentences
assert FS["Dasa kilesavatthūni – lobho, doso, moho, māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirikaṃ, "
          "anottappaṃ"] + "." == G.NEW_SENT["Dasa kilesavatthūni – lobho, doso, moho, māno, diṭṭhi, vicikicchā, "
                                             "thinaṃ, uddhaccaṃ, ahirīkaṃ, anottappaṃ."]
assert G.NEW_SENT[("Cha nīvaraṇā [nīvaraṇāni (syā.)] – kāmacchandanīvaraṇaṃ, byāpādanīvaraṇaṃ, thinamiddhanīvaraṇaṃ, "
                   "uddhaccakukkuccanīvaraṇaṃ, vicikicchānīvaraṇaṃ, avijjānīvaraṇaṃ.")].replace(
    " " + S.reading("Syā.", "nīvaraṇāni"), "") == FS[
    "Cha nīvaraṇā – kāmacchandanīvaraṇaṃ, byāpādanīvaraṇaṃ, thinamiddhanīvaraṇaṃ, uddhaccakukkuccanīvaraṇaṃ, "
    "vicikicchānīvaraṇaṃ, avijjānīvaraṇaṃ"] + "."
SLIP_FS = {
    "Alobho vipākahetu adoso vipākahetu, kāmāvacarassa vipākato ahetuke cittuppāde ṭhapetvā, catūsu bhūmīsu "
    "vipākesu uppajjanti": "no comma between «alobho vipākahetu» and «adoso vipākahetu»: as the kusala sentence",
    "Alobho kiriyahetu adoso kiriyahetu, kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā, tīsu bhūmīsu kiriyesu "
    "uppajjanti": "no comma between «alobho kiriyahetu» and «adoso kiriyahetu»: as the kusala sentence",
}

# =========================================================================================
# 8. Lines
# =========================================================================================
H5 = {
    "### Aṭṭhakathākaṇḍaṃ": f"### {S.CH_HEADINGS['Aṭṭhakathākaṇḍaṃ']}",
    "#### Tikaatthuddhāro": "#### Giải thích ý nghĩa bộ ba",      # atthuddhāro «giải thích ý nghĩa», Tika «bộ ba»
    "#### Dukaatthuddhāro": "#### Giải thích ý nghĩa bộ đôi",
    "Katame dhammā oghā…pe….": f"{S.q_form(P['oghā'])[:-1]}{ELL}",
    "Katame dhammā yogā…pe….": f"{S.q_form(P['yogā'])[:-1]}{ELL}",
    "Atthuddhāro niṭṭhito.": "Phần giải thích ý nghĩa đã hoàn tất.",      # niṭṭhito «đã hoàn tất»
    "Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ.": f"Bộ “{S.H_BOOK}” đã hoàn tất.",   # the book title in “…”
}
assert S.CH_HEADINGS["Aṭṭhakathākaṇḍaṃ"] == "Phần giải thích" and S.H_BOOK == "Liệt kê các hiện tượng"
SLIP_LINES = {
    "Katame dhammā oghā…pe….": "the flood cluster abridged to «Katame dhammā oghā…pe….»: kept, «…» closes the line",
    "Katame dhammā yogā…pe….": "the yoke cluster abridged to «Katame dhammā yogā…pe….»: kept, «…» closes the line",
}
ANS_RE = re.compile(r"(.+) – ime dhammā (.+)\.")
KQ_RE = re.compile(r"Katame dhammā (.+?)([?.]) (.+)$")
SENT_SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑ])")


def sentence_vi(s):
    if s in F.FIXED_SENT:
        return F.FIXED_SENT[s]
    core = s[:-1]
    if core in FS:
        if core in SLIP_FS:
            slip(SLIP_FS[core])
        return FS[core] + "."
    m = ANS_RE.fullmatch(s)
    if m:
        body, pred = m.groups()
        if body in SLIP_FS:
            slip(SLIP_FS[body])
        b = body_vi(body)
        if pred in P or pred in F.PRED_X:
            return f"{b} {DASH} {S.a_form(F.pred(pred))}"
        return f"{b} {DASH} {pred_vi(SUBJ['ime dhammā'], pred)}"
    if "uppajja" in core:
        return arise_multi(core) + "."
    return subject_sentence(s)


def rest_vi(rest):
    return " ".join(sentence_vi(s) for s in SENT_SPLIT.split(rest))


def translate_line(line):
    if line in H5:
        if line in SLIP_LINES:
            slip(SLIP_LINES[line])
        return H5[line]
    if line in REUSE:
        REUSED.append(CUR["sid"])
        return REUSE[line]
    m = KQ_RE.fullmatch(line)
    if m:
        x, mark, rest = m.groups()
        q = S.q_form(F.pred(x))
        if mark == ".":
            slip("the question ends with «.» (a source slip): kept as written")
            q = q[:-1] + "."
        return f"{q} {rest_vi(rest)}"
    return rest_vi(line)


# =========================================================================================
# 9. Render, checks, build
# =========================================================================================
def render(segs):
    blocks = []
    for sid, plines in segs:
        CUR["sid"] = sid
        vlines = []
        for p in plines:
            v = unicodedata.normalize("NFC", cap(translate_line(p)))
            B.check_vi(v)
            assert len(p) - len(p.lstrip("#")) == len(v) - len(v.lstrip("#")), sid
            assert p.count("–") + p.count("—") == v.count("–"), ("dash", sid, p[:60], v[:60])
            assert p.count("…pe…") <= v.count("…"), ("pe", sid)
            assert p.endswith("?") == v.endswith("?"), ("question", sid)
            assert v.endswith(".") or v.endswith("?") or v.endswith(ELL) or v.startswith("#"), ("stop", sid, v[-40:])
            assert "  " not in v and " ," not in v and ",," not in v and "..." not in v and " ;" not in v, (
                "spacing", sid, v)
            assert ", ," not in v and ",:" not in v and ";," not in v and "…." not in v and ";;" not in v, (
                "punct", sid, v)
            assert "đau khổ" not in v and "là là" not in v and "chánh niệm" not in v, sid
            assert "Pāli" not in v and "ṭ" not in re.sub(r"\[[^\]]*\]", "", v), sid
            vlines.append(v)
        blocks.append("\n".join(vlines[:-1] + [f"{vlines[-1]} ^{sid}"]))
    return blocks


def check_earlier_unchanged():
    """Importing 4-02/4-03 (and through it 4-01 … 2-01) must leave their outputs exactly as finished."""
    F.check_earlier_unchanged()                      # 2-01 … 3-03
    G.check_401()                                    # 4-01
    for part in G.PARTS:                             # 4-02, 4-03
        text, _ = G.build(part)
        assert unicodedata.normalize("NFC", text) == (S.OUT / part).read_bytes().decode("utf-8"), part
        print(f"{part}: rebuilt in memory, byte-identical to the finished file")


def build():
    segs = B.segments(S.PALI / PART)
    text = "\n\n".join(render(segs)) + "\n"
    return unicodedata.normalize("NFC", text), len(segs)


# =========================================================================================
# 10. Notes
# =========================================================================================
def notes():
    L = ["# pi-1 Vietnamese rails: new formulas of 5 (Aṭṭhakathākaṇḍaṃ)", "",
         "Generated by build_rails_5_vi.py from its fixed strings; import that file instead of retyping (PIECES, LOC, "
         "FS, SUBJ, H5, pred_vi). Strings already in vi-rails-formulas.md or the notes of chapters 2 … 4 are not "
         "repeated: the cluster names, «Chính các … ấy vừa là …», «Về tâm thì không nên nói – …», «toàn bộ vật chất», "
         "«và loại vật chất do nghiệp đã được tạo», the four paths and the cluster headings come from the 4-0x "
         "builders, and a Pāli line that repeats a 4-0x line keeps its Vietnamese. The question and answer frames are "
         "1-matika's (S.q_form / S.a_form with S.PREDS) verbatim. Format: Pāli = tiếng Việt.", "",
         "## Frames", "",
         "List items are joined with «; » (as 4-01 … 4-03); an etthuppanna- exception is joined to the item before it "
         "with «, »; an item that closes the list with «ca» takes «và».",
         f"ime dhammā siyā X, siyā Y = những hiện tượng này {SOMETIMES} X, {SOMETIMES} Y",
         "ime dhammā … na X (inside a siyā list) = … không X («không phải là X» for a «là» name; the matrix «na X» "
         "name where there is one)",
         f"ime dhammā na vattabbā Xtipi, Ytipi, Ztipi = về những hiện tượng này thì {NOT_SAY} {THAT} X, {OR_THAT} Y, "
         f"{OR_THAT} Z",
         f"siyā na vattabbā Xtipi, Ytipi / na vattabbā Xti = {SOMETIMES} {NOT_SAY} {THAT} X, {OR_THAT} Y / "
         f"{NOT_SAY} {THAT} X",
         f"X dhammā na vattabbā – Ytipi, Ztipi. = Về các hiện tượng X thì {NOT_SAY} {DASH} {THAT} Y, {OR_THAT} Z.",
         f"X na vattabbo / vattabbaṃ Ytipi, … = Về X thì {NOT_SAY} {THAT} Y, …",
         f"X Y-loc. uppajjati / uppajjanti = X {ARISE} trong Y",
         f"X kusalahetu, Y kusalahetu, … uppajjanti = X, {ROOT_K}, và Y, {ROOT_K}, {ARISE} …  "
         f"(vipākahetu «{ROOT_V}», kiriyahetu «{ROOT_F}»)",
         "… ṭhapetvā …, … uppajjati = … sinh khởi trong …, ngoại trừ …  (the exception after the place)", "",
         "## Pieces of the answer lists", ""]
    seen = set()
    for k, (kind, v) in PIECES.items():
        if re.match(r"(kāmāvacarakusalato|kiriyato|akusalato|kāmāvacarakusalassa vipākato|akusalassa vipākato) "
                    r"(eko|dve|tayo|cattāro|pañca|cha|satta|aṭṭha|nava|dasa|ekādasa)\b", k):
            continue
        if any(k.startswith(h) and k != h for h in _JHEADS) and not k.endswith(" kusalato ca vipākato ca kiriyato ca"):
            continue
        if v in seen and kind != "pre":
            pass
        seen.add(v)
        L.append(f"{k} = {v}")
    L += [f"kāmāvacarakusalato N X-cittuppādā = N {KIND} thiện {KAMA} X  (X: " +
          ", ".join(f"{a} «{b}»" for a, b in CU_ATTR.items()) + ")",
          f"kiriyato N X-cittuppādā = N {KIND} {FUNC} X",
          f"akusalato N = N {KIND} bất thiện",
          f"kāmāvacarakusalassa vipākato N [cittuppādā] = N {KIND} là quả của nghiệp thiện {KAMA}",
          f"akusalassa vipākato N [cittuppādā] = N {KIND} là quả của nghiệp bất thiện",
          f"kiriyato N [cittuppādā] = N {KIND} {FUNC}",
          "N: " + ", ".join(f"{a} {b}" for a, b in NUMV.items()),
          "JHĀNA + kusalato ca vipākato ca = JHĀNA, ở dạng thiện và quả của nghiệp; + kusalato ca kiriyato ca = "
          "JHĀNA, ở dạng thiện và chức năng"]
    for h, hv in _JHEADS.items():
        L.append(f"{h} = {hv}")
    L += ["", "## Places (uppajjati / uppajjanti)", ""] + [f"{k} = {v}" for k, v in LOC.items()]
    L += ["", "## Sentences", ""] + [f"{k}. = {v}." for k, v in FS.items()]
    L += [f"{k} … = {cap(v)} …" for k, v in SUBJ.items() if k != "ime dhammā"]
    L += ["", "## Headings and closing lines", ""] + [f"{k} = {v}" for k, v in H5.items()]
    L += ["", "## Reused word for word from 4-01 … 4-03 (identical Pāli lines)", "",
          ", ".join(f"^{s}" for s in dict.fromkeys(REUSED))]
    L += ["", "## Source slips and marks (translated as written; punctuation rendered as meant)", ""]
    by_note = {}
    for sid, note in dict.fromkeys(SLIPS):
        by_note.setdefault(note, []).append(f"^{sid}")
    for note, sids in by_note.items():
        L.append(f"{', '.join(sids)}: {note}")
    L += ["", "## Termbase notes", "",
          "bhūmīsu «cõi»: catūsu / tīsu bhūmīsu kusalaṃ = «tâm thiện thuộc bốn / ba cõi»; kusalaṃ / akusalaṃ "
          "(«thiện» / «bất thiện», standing for the wholesome / unwholesome mind) take «tâm», as the chapter-2 heading "
          "«Tâm thiện thuộc ba cõi»; vipāko (no entry; vipāka «quả của nghiệp») = «quả của nghiệp thuộc bốn cõi»; "
          "kiriyābyākataṃ (termbase «chức năng không xác định về mặt đạo đức») = «tâm mang tính chức năng không xác "
          "định về mặt đạo đức thuộc ba cõi»: kiriyā «mang tính chức năng» (the keyword of these segments, as the "
          "chapter-2 headings «Tâm mang tính chức năng …») contains the entry's «chức năng không xác định …».",
          "cittuppādā / cittuppādo / cittuppāde / cittuppādesu = «loại tâm»; kusalato / vipākato / kiriyato = «thiện» / "
          "«quả của nghiệp» / «chức năng»: «N loại tâm thiện thuộc cõi dục lạc …», «N loại tâm là quả của nghiệp thiện "
          "thuộc cõi dục lạc», «N loại tâm mang tính chức năng», and after a jhāna «…, ở dạng thiện, quả của nghiệp và "
          "chức năng» (the termbase vipākato ca kiriyato «quả của nghiệp và chức năng»).",
          "kusalesu / vipākesu / kiriyesu / akusalesu = «trong các tâm thiện / các quả của nghiệp / các tâm mang tính "
          "chức năng / "
          "các tâm bất thiện …»; sabbākusalesu «trong tất cả các tâm bất thiện»; sasaṅkhārikesu akusalesu «trong các "
          "tâm bất thiện có sự thúc đẩy».",
          "rūpāvacara-<a><b>-jjhānā (no entries) built on the termbase lokuttaratikacatukkajjhānā: «ba tầng thiền thuộc "
          "cõi hình sắc theo phương pháp chia bốn và bốn tầng thiền theo phương pháp chia năm» (ekaka «một», duka "
          "«hai», tika «ba», catukka «bốn», pañcaka «năm»).",
          "diṭṭhigatavippayuttalobhasahagata = «có sự tham lam đi kèm, không gắn liền với sự mắc kẹt trong các quan "
          "điểm» (the termbase pieces «sự tham lam … không gắn liền» in that order, as chapter 2 «có niềm vui đi kèm, "
          "gắn liền với …»).",
          "Dvepañcaviññāṇāni = «hai nhóm năm loại thức» (pañcaviññāṇāni «năm loại thức»; dve «hai»).",
          "catutthassa jhānassa vipāko = «quả của nghiệp thuộc tầng thiền thứ tư»; cattāro arūpāvacarā = «bốn loại "
          "tâm thuộc cõi không hình sắc» (the noun is implied), cattāro āruppā = «bốn tầng thiền không hình sắc».",
          "etthuppannaṃ / etthuppanne X ṭhapetvā = «ngoại trừ X sinh khởi trong đó» (termbase uppanne hetū «gốc rễ "
          "sinh khởi», uppannaṃ vicāraṃ «sự duy trì tâm sinh khởi»).",
          "sukhaṃ vedanaṃ (^1-1387) = «cảm giác dễ chịu» (feeling triad); etthuppannaṃ sukhaṃ (^1-1403, 1597) = "
          "«hạnh phúc» (the matrix «có hạnh phúc đi kèm», as 4-01); dukkhasahagata(ṃ) kāyaviññāṇaṃ = «thức qua thân "
          "có sự khó chịu đi kèm» (APPROVED decision 1, 2-05 ^1-556).",
          "yā ca vedanā upekkhā (^1-1404) = «loại cảm giác là sự bình thản»: Yā «điều» does not fit a relative "
          "inside a list of kinds.",
          "na vattabbā = «không nên nói» (termbase vattabbā «nên nói»), its items «rằng X, hay rằng Y» as 4-02 «Về tâm "
          "thì không nên nói – rằng …, hay rằng …»; siyā = «đôi khi».",
          "Niyogā anāgatārammaṇā natthi (^1-1433) = «Không có hiện tượng nào nhất thiết có đối tượng thuộc tương lai.» "
          "(Niyogā «nhất thiết», natthi «không có»).",
          "Anindriyabaddharūpa = «vật chất không gắn kết với các năng lực» (termbase indriyabaddharūpañca nibbānañca "
          "«vật chất … gắn kết với các năng lực và Niết-bàn»).",
          "Yattha … ekato uppajjanti = «Ở nơi … cùng sinh khởi» (termbase hetū ekato uppajjanti «gốc rễ cùng sinh "
          "khởi»); dve tayo / dve tīṇi = «hai hoặc ba».",
          "Headings: Tikaatthuddhāro / Dukaatthuddhāro = «Giải thích ý nghĩa bộ ba / bộ đôi» (termbase atthuddhāro "
          "«giải thích ý nghĩa»); Atthuddhāro niṭṭhito. = «Phần giải thích ý nghĩa đã hoàn tất.»; "
          "Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ. = «Bộ “Liệt kê các hiện tượng” đã hoàn tất.» (pakaraṇa: no entry).",
          "Variants: [dutiyajjhāne (sī.)] = «khác chính tả»; [sabbeva (syā.)] = «dị bản» (adds eva)."]
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    check_earlier_unchanged()
    text, n = build()
    OUT_FILE.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT_FILE, n, "segments;", len(dict.fromkeys(REUSED)), "segments with reused 4-0x lines")
    NOTES_FILE.write_text(notes(), encoding="utf-8", newline="\n")
    print("wrote", NOTES_FILE)


if __name__ == "__main__":
    main()
