"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapter 4-01 (the summary chapter: the matrix triads ^1-985 … ^1-1058 and the first pairs: the root, small
intermediate, taint, fetter and tie clusters ^1-1059 … ^1-1155).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/4-01-nikkhepakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-4-01.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never edited:
build_rails_sample_vi.py (S) and build_rails_3-02_3-03_vi.py (Q, which loads 3-01 = R, 2-05 = E, 2-04 = D,
2-03 = T, 2-01/2-02 = B). A check rebuilds 2-01 … 3-03 in memory and requires them to equal the finished files
byte for byte. The question and answer frames are 1-matika's («Những hiện tượng nào X?» / «– những hiện tượng
này X.», S.q_form / S.a_form with S.PREDS); the strings already built in chapters 2 and 3 (the aggregate lists,
the ^1-583 statement, the lobha / dosa / moha / vicikicchā / diṭṭhi / paññā strings, «toàn bộ vật chất» …) are
imported. Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md). Translated fresh from the Pāli.

usage: python -I -X utf8 build_rails_4-01_vi.py
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

_spec = importlib.util.spec_from_file_location("build_rails_3_02_3_03_vi", HERE / "build_rails_3-02_3-03_vi.py")
Q = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(Q)        # importing writes nothing; Q.R = 3-01, R.E = 2-05, R.D = 2-04, R.T, R.B
R = Q.R
E, D, B = R.E, R.D, R.B

PART = "4-01-nikkhepakandam.md"
cap = S.cap
PE, ELL, DASH = "…pe…", "…", "–"
P = S.PREDS                                         # matrix pali (plural) -> predicate (1-matika wording)
NAMES = S.NAMES                                     # matrix pali -> attribute after «các hiện tượng»
SLIPS = []                                          # (segment, note)
CUR = {"sid": ""}


def slip(note):
    SLIPS.append((CUR["sid"], note))


# =========================================================================================
# 1. Building blocks of the answers
# =========================================================================================
N = B.NAMES                                         # chapter-2 names (aggregates, roots …)
RUPAKKHANDHA = "khối vật chất"                      # rūpakkhandho (termbase)
KH4 = R.KHANDHAS                                    # khối cảm giác, khối tri giác, khối tạo tác và khối thức (^1-583)
KH3 = f"{N['saññākkhandho']}, {N['saṅkhārakkhandho']} và {N['viññāṇakkhandho']}"
KH5 = f"{RUPAKKHANDHA}, {KH4}"
KH4_PE = f"{N['vedanākkhandho']}{ELL} {N['viññāṇakkhandho']}"
KH5_PE = f"{RUPAKKHANDHA}{ELL} {N['viññāṇakkhandho']}"
assert KH4 == "khối cảm giác, khối tri giác, khối tạo tác và khối thức"
KH_LISTS = {
    "rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": KH5,
    "vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": KH4,
    "saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": KH3,
    "rūpakkhandho…pe… viññāṇakkhandho": KH5_PE,
    "vedanākkhandho…pe… viññāṇakkhandho": KH4_PE,
}
WITH_THEM = "gắn liền với chúng"                    # taṃsampayutto (sampayutto «gắn liền»)
KAMMA3 = "nghiệp bằng thân, nghiệp bằng lời nói, nghiệp bằng ý"   # kāyakammaṃ, vacīkammaṃ, manokammaṃ
FROM_THEM = "do chúng sinh ra"                      # taṃsamuṭṭhānaṃ (samuṭṭhānaṃ «do … sinh ra»)
KILESA = "và các phiền não cùng hiện diện với chúng"   # tadekaṭṭhā ca kilesā (termbase «và các phiền não cùng hiện diện»)
TOGETHER = "cùng hiện diện với chúng"               # tadekaṭṭho (ekaṭṭhā «cùng hiện diện»)
REMAINING = "còn lại"                               # avaseso / avasesā
SAB = R.SAB                                         # toàn bộ vật chất (sabbañca rūpaṃ, ^1-583)
ASANKHATA = f"yếu tố {P['asaṅkhatā']}"              # asaṅkhatā (ca) dhātu
KIRIYA = f"những hiện tượng {E.KIRIYA_V}"           # ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā
RESULT_OF = R.RESULT_OF                             # Kusalākusalānaṃ dhammānaṃ vipākā (^1-583)
NOT_RIPE = "có quả chưa chín muồi"                  # avipakkavipākānaṃ (termbase)
SAS = P["sāsavā"]                                   # Sāsavā «là đối tượng của ô nhiễm»
RUPA_KIND = f"và loại {R.RUPA}"                     # yañca rūpaṃ (R: «và loại vật chất»)
YANCA = {
    "kammassa katattā uppajjissati": f"sẽ sinh khởi {Q.KAMMA}",   # uppajjissati «sẽ sinh khởi»
    "kammassa katattā": Q.KAMMA,                    # do nghiệp đã được tạo
    "na kammassa katattā": Q.NA_KAMMA,              # không do nghiệp đã được tạo
    "anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ": Q.qpred("anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ"),
}
assert R.U583_V.endswith(f"; {KIRIYA}; {SAB}; và {ASANKHATA} {DASH} {D.A_ABY}.")

QV = {   # kusalā / akusalā / abyākatā compounds after «các hiện tượng»
    "kusalākusalābyākatā": f"{NAMES['kusalā']}, {NAMES['akusalā']} và {NAMES['abyākatā']}",
    "kusalākusalā": f"{NAMES['kusalā']} và {NAMES['akusalā']}",
    "kusalābyākatā": f"{NAMES['kusalā']} và {NAMES['abyākatā']}",
}
SPH_KEY = {}
for _w in ("kāmāvacar", "rūpāvacar", "arūpāvacar", "apariyāpann"):
    SPH_KEY[_w + "ā"] = SPH_KEY[_w + "e"] = _w + "ā"   # nominative pl. and locative sg. (bhūmiyaṃ …)


def sph_vi(text):
    """kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā = «thuộc …, thuộc …, thuộc … hoặc không nằm …» (^1-583)"""
    words = re.split(r",? ", text.strip())
    items = [P[SPH_KEY[w.lower()]] for w in words]
    if len(items) > 1 and text.count(",") < len(items) - 1:
        slip("a missing comma in the list of spheres: rendered as meant (comma)")
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " hoặc " + items[-1]


assert sph_vi("kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā") == R.SPHERES

THOSE = "các hiện tượng ấy"                         # tehi dhammehi / te dhamme (termbase Tehi dhammehi «hiện tượng ấy»)
EXCEPT_THOSE = f"ngoại trừ {THOSE}"                 # te dhamme ṭhapetvā
TEHI = {   # Tehi dhammehi ye dhammā Y = «những hiện tượng Y»
    "sahetukā": f"có {THOSE} làm gốc rễ",
    "ahetukā": f"không có {THOSE} làm gốc rễ",
    "sampayuttā": f"gắn liền với {THOSE}",
    "vippayuttā": f"không gắn liền với {THOSE}",
    "na hetū sahetukā": f"không phải là gốc rễ nhưng có {THOSE} làm gốc rễ",
    "na hetū ahetukā": f"không phải là gốc rễ và không có {THOSE} làm gốc rễ",
    "sāsavā": f"là đối tượng của {THOSE}",
    "saṃyojaniyā": f"là đối tượng của {THOSE}",
    "ganthaniyā": f"là đối tượng của {THOSE}",
}
PATHS = (f"các con đường {P['apariyāpannā']}, các thành quả của con đường và {ASANKHATA}")
# Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu (maggā «con đường», phalāni «thành quả»)
FOUR_PATHS = f"bốn con đường {P['apariyāpannā']}"  # Cattāro maggā apariyāpannā
LOWER_FRUITS = "ba thành quả thấp hơn của đời sống sa-môn"   # heṭṭhimāni ca tīṇi sāmaññaphalāni
SAMANGI = "ở người có được con đường cao quý"       # Ariyamaggasamaṅgissa (samaṅgissa «người có được»)
CITTACETASIKA = "tâm và các yếu tố đồng hành với tâm"   # cittacetasikā dhammā (termbase)


def arise(obj, role="đối tượng"):
    """X ārabbha ye uppajjanti cittacetasikā dhammā = «tâm và … sinh khởi khi lấy X làm đối tượng»"""
    return f"{CITTACETASIKA} sinh khởi khi lấy {obj} làm {role}"


ROOTS_K = f"{N['alobho']}, {N['adoso']}, {N['amoho']}"
ROOTS_A = f"{N['lobho']}, {N['doso']}, {N['moho']}"
FETTERS3 = "quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức"
FIVE_V = "vật chất, cảm giác, tri giác, các sự tạo tác, thức"   # rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ
MN = R.MATTER_NOUN
AYATANA9 = ["cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ", "saddāyatanaṃ",
            "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ"]

# the hetu names
NUM = {"tayo": "ba", "nava": "chín", "cha": "sáu"}
HETU = {
    "kusalahetū": "gốc rễ thiện", "akusalahetū": "gốc rễ bất thiện",
    "abyākatahetū": "gốc rễ không xác định về mặt đạo đức",
    "kāmāvacarahetū": "gốc rễ thuộc cõi dục lạc", "rūpāvacarahetū": "gốc rễ thuộc cõi hình sắc",
    "arūpāvacarahetū": "gốc rễ thuộc cõi không hình sắc",
    "apariyāpannahetū": "gốc rễ không nằm trong các cõi tồn tại",
}


def hetus(text):
    """Tayo kusalahetū, … = «ba gốc rễ thiện, …»"""
    out = []
    for it in re.split(r",? (?=(?:tayo|nava|cha) )", text[0].lower() + text[1:]):
        n, h = it.split(" ")
        out.append(f"{NUM[n]} {HETU[h]}")
    return ", ".join(out)


# the bhūmi phrases: (stem, exclusion) -> attribute after «Ở cấp độ»
LEVEL = "ở cấp độ"                                  # -bhūmiyaṃ (termbase bhūmiyaṃ «cấp độ»)
BHUMI = {
    ("Sukha", "sukhaṃ vedanaṃ"): "có cảm giác dễ chịu",
    ("Dukkha", "dukkhaṃ vedanaṃ"): "có cảm giác khó chịu",
    ("Adukkhamasukha", "adukkhamasukhaṃ vedanaṃ"): "có cảm giác không khó chịu cũng không dễ chịu",
    ("Savitakkasavicāra", "vitakkavicāre"): P["savitakkasavicārā"],
    ("Avitakkavicāramatta", "vicāraṃ"): P["avitakkavicāramattā"],
    ("Avitakkaavicāra", None): P["avitakkaavicārā"],
    ("Pīti", "pītiṃ"): "có sự hân hoan",
    ("Sukha", "sukhaṃ"): "có hạnh phúc",           # the jhāna-factor sense, as the matrix «có hạnh phúc đi kèm»
    ("Upekkhā", "upekkhaṃ"): "có sự bình thản",
}
EXCL = {
    "sukhaṃ vedanaṃ": "cảm giác dễ chịu", "dukkhaṃ vedanaṃ": "cảm giác khó chịu",
    "adukkhamasukhaṃ vedanaṃ": "cảm giác không khó chịu cũng không dễ chịu",
    "vitakkavicāre": f"{S.FN['vitakko']} và {S.FN['vicāro']}", "vicāraṃ": S.FN["vicāro"],
    "pītiṃ": S.FN["pīti"], "sukhaṃ": S.FN["sukhaṃ"], "upekkhaṃ": N["upekkhā"],
}
assert EXCL["sukhaṃ"] == "hạnh phúc" and EXCL["vitakkavicāre"] == "sự hướng tâm và sự duy trì tâm"

# =========================================================================================
# 2. Fixed pieces of the answers: Pāli -> (kind, Vietnamese)
#    kinds: x (an item), kh (aggregates), desc (followed by «: » + the aggregates),
#           vip (the aggregates come first, as ^1-583), excl / lead (joined to the next piece with the Pāli mark)
# =========================================================================================
FIXED = {
    "Tīṇi kusalamūlāni – alobho, adoso, amoho": ("x", f"ba gốc rễ thiện {DASH} {ROOTS_K}"),
    "Tīṇi akusalamūlāni – lobho, doso, moho": ("x", f"ba gốc rễ bất thiện {DASH} {ROOTS_A}"),
    "tadekaṭṭhā ca kilesā": ("x", KILESA),
    "Tadekaṭṭhā ca kilesā": ("x", KILESA),
    "taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ": ("x", f"{KAMMA3} {FROM_THEM}"),
    "taṃsamuṭṭhānaṃ kāyakammaṃ vacīkammaṃ manokammaṃ": ("x", f"{KAMMA3} {FROM_THEM}"),
    "Imāni tīṇi saṃyojanāni": ("x", "ba xiềng xích này"),
    "Tīṇi saṃyojanāni – sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāso": ("x", f"ba xiềng xích {DASH} {FETTERS3}"),
    "Tadekaṭṭho lobho, doso, moho": ("x", f"{ROOTS_A} {TOGETHER}"),
    "Avaseso lobho, doso, moho": ("x", f"{ROOTS_A} {REMAINING}"),
    "ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā": ("x", KIRIYA),
    "Ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā": ("x", KIRIYA),
    "sabbañca rūpaṃ, asaṅkhatā ca dhātu": ("x", f"{SAB}; và {ASANKHATA}"),
    "sabbañca rūpaṃ asaṅkhatā ca dhātu": ("x", f"{SAB}; và {ASANKHATA}"),
    "asaṅkhatā ca dhātu": ("x", f"và {ASANKHATA}"),
    "Asaṅkhatā dhātu": ("x", ASANKHATA),
    "Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu": ("x", PATHS),
    "Apariyāpannā maggā ca maggaphalāni ca, asaṅkhatā ca dhātu": ("x", PATHS),
    "Cattāro maggā apariyāpannā, heṭṭhimāni ca tīṇi sāmaññaphalāni": ("x", f"{FOUR_PATHS} và {LOWER_FRUITS}"),
    "Cattāro maggā apariyāpannā": ("x", FOUR_PATHS),
    "Upariṭṭhimaṃ [uparimaṃ (syā.)] arahattaphalaṃ":
        ("x", f"thành quả A-la-hán cao nhất {S.reading('Syā.', 'uparimaṃ')}"),
    "Pañca kammāni ānantarikāni, yā ca micchādiṭṭhiniyatā":
        ("x", f"năm nghiệp có quả không gián đoạn và {D.NEW_NAMES['micchādiṭṭhi']} {P['niyatā']}"),
    "Cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāya rūpaṃ": ("x", R.SAB_DEF.split(f" {DASH} ")[0]),
    "Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho":
        ("x", f"năm khối {DASH} {KH5}"),
    "Rūpāyatanaṃ": ("x", MN["rūpāyatanaṃ"]),
    "Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ": ("x", f"{MN['cakkhāyatanaṃ']}{ELL} {MN['phoṭṭhabbāyatanaṃ']}"),
    cap(", ".join(AYATANA9)): ("x", ", ".join(MN[a] for a in AYATANA9)),
    "Tadubhayaṃ": ("x", "cả hai loại ấy"),         # ubhaya: no termbase entry
    # the path triad
    "Ariyamaggaṃ ārabbha ye uppajjanti cittacetasikā dhammā": ("x", arise("con đường cao quý")),
    "Ariyamaggaṃ adhipatiṃ karitvā ye uppajjanti cittacetasikā dhammā":
        ("x", arise("con đường cao quý", "yếu tố chủ đạo")),
    "Ariyamaggasamaṅgissa maggaṅgāni ṭhapetvā": ("excl", f"{SAMANGI}, ngoại trừ các chi phần của con đường"),
    "Ariyamaggasamaṅgissa sammādiṭṭhi maggo ceva hetu ca":
        ("lead", f"{SAMANGI}, {S.FN['sammādiṭṭhi']} vừa là con đường vừa là gốc rễ"),
    "sammādiṭṭhiṃ ṭhapetvā": ("excl", f"ngoại trừ {S.FN['sammādiṭṭhi']}"),
    "Ariyamaggasamaṅgissa alobho, adoso, amoho": ("x", f"{SAMANGI}, {ROOTS_K}"),
    "Ariyamaggasamaṅgissa vīmaṃsādhipateyyaṃ maggaṃ bhāvayantassa vīmaṃsaṃ ṭhapetvā":
        ("excl", f"{SAMANGI} và đang tu tập con đường {B.ADHIP['vīmaṃsādhipateyyaṃ']}, ngoại trừ sự thẩm xét"),
    # the hetu cluster
    "Kusalānaṃ vā dhammānaṃ vipākato kiriyābyākatesu vā dhammesu alobho adoso amoho":
        ("x", f"{ROOTS_K} trong quả của các hiện tượng thiện hoặc trong các hiện tượng {NAMES['abyākatā']} "
              "mang tính chức năng"),
    "Kusalānaṃ dhammānaṃ vipākato alobho adoso amoho": ("x", f"{ROOTS_K} trong quả của các hiện tượng thiện"),
    "Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū": ("x", hetus("Tayo kusalahetū, tayo akusalahetū, "
                                                                          "tayo abyākatahetū")),
    "Tayo kusalahetū, tayo abyākatahetū": ("x", hetus("Tayo kusalahetū, tayo abyākatahetū")),
    "Ime cha apariyāpannahetū": ("x", f"đó là {NUM['cha']} {HETU['apariyāpannahetū']}"),
}
assert FIXED["Cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāya rūpaṃ"][1] == (
    "Bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản")
assert B.ADHIP["vīmaṃsādhipateyyaṃ"] == "lấy sự thẩm xét làm yếu tố chủ đạo"
for _x in ("parittā", "mahaggatā", "appamāṇā", "atītā", "anāgatā", "paccuppannā", "ajjhattā", "bahiddhā",
           "ajjhattabahiddhā"):
    _loc = {"parittā": "Paritte", "mahaggatā": "Mahaggate", "appamāṇā": "Appamāṇe", "atītā": "Atīte",
            "anāgatā": "Anāgate", "paccuppannā": "Paccuppanne", "ajjhattā": "Ajjhatte", "bahiddhā": "Bahiddhā",
            "ajjhattabahiddhā": "Ajjhattabahiddhā"}[_x]
    FIXED[f"{_loc} dhamme ārabbha ye uppajjanti cittacetasikā dhammā"] = ("x", arise(f"các hiện tượng {NAMES[_x]}"))

# 2b. the arisen / past / internal triads (whole bodies)
UP_AFF_P = ["jātā", "bhūtā", "sañjātā", "nibbattā", "abhinibbattā", "pātubhūtā", "uppannā", "samuppannā", "uṭṭhitā",
            "samuṭṭhitā"]
UP_AFF_V = ["đã sinh ra", "đã trở thành", "đã sinh thành", "đã phát sinh", "đã phát sinh rõ rệt", "đã hiện ra",
            "đã sinh khởi", "đã sinh khởi trọn vẹn", "đã trỗi dậy", "đã trỗi dậy trọn vẹn"]
UP_NEG_P = ["ajātā", "abhūtā", "asañjātā", "anibbattā", "anabhinibbattā", "apātubhūtā", "anuppannā", "asamuppannā",
            "anuṭṭhitā", "asamuṭṭhitā"]
UP_NEG_V = [v.replace("đã ", "chưa ", 1) for v in UP_AFF_V]
ATI_P = ["atītā", "niruddhā", "vigatā", "vipariṇatā", "atthaṅgatā", "abbhatthaṅgatā", "uppajjitvā vigatā"]
ATI_V = [P["atītā"], "đã chấm dứt", "đã mất đi", "đã biến đổi", "đã biến mất", "đã biến mất hoàn toàn",
         "đã mất đi sau khi sinh khởi"]
GROUPED = "được gộp vào phần"                       # X-aṃsena saṅgahitā (aṃsena «phần»; saṅgahitā: no entry)
FIVE_P = "rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ"
BAHU = S.reading("nhiều ấn bản", "rūpā")           # rūpaṃ [rūpā (bahūsu)]: another form (plural), so «dị bản»


def time_body(lst_p, lst_v, x, five_p=FIVE_P, var=""):
    stem = x[:-1] + "aṃsena"                         # uppannā -> uppannaṃsena
    p = f"Ye dhammā {' '.join(lst_p)} {x} {stem} saṅgahitā, {five_p}"
    v = f"những hiện tượng {', '.join(lst_v)}, {P[x]}, {GROUPED} {P[x]}: vật chất{var}, {FIVE_V[len('vật chất, '):]}"
    return p, v


for _lp, _lv, _x in ((UP_AFF_P, UP_AFF_V, "paccuppannā"), (UP_NEG_P, UP_NEG_V, "anuppannā"),
                     (UP_NEG_P, UP_NEG_V, "anāgatā"), (ATI_P, ATI_V, "atītā")):   # «atītā» opens and closes
    _p, _v = time_body(_lp, _lv, _x)
    FIXED[_p] = ("x", _v)
_p, _v = time_body(UP_AFF_P, UP_AFF_V, "uppannā", "rūpaṃ [rūpā (bahūsu)], vedanā, saññā, saṅkhārā, viññāṇaṃ",
                   " " + BAHU)
FIXED[_p] = ("x", _v)
INNER = "ở nơi bản thân, riêng từng người, cố hữu, thuộc về cá nhân, do nghiệp tạo ra"
# ajjhattaṃ «nơi bản thân», paccattaṃ «riêng từng người», niyatā «cố hữu», pāṭipuggalikā «thuộc về cá nhân»,
# upādiṇṇā «do nghiệp tạo ra»
FIXED[f"Ye dhammā tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyatā pāṭipuggalikā upādiṇṇā, {FIVE_P}"] = (
    "x", f"những hiện tượng của từng chúng sinh, {INNER}: {FIVE_V}")
FIXED[f"Ye dhammā tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ ajjhattaṃ paccattaṃ niyatā pāṭipuggalikā upādiṇṇā, "
      f"{FIVE_P}"] = ("x", f"những hiện tượng của từng chúng sinh khác, từng người khác, {INNER}: {FIVE_V}")

# =========================================================================================
# 3. Patterned pieces
# =========================================================================================
SPHW = r"(?:[Kk]āmāvacar[āe]|[Rr]ūpāvacar[āe]|[Aa]rūpāvacar[āe]|apariyāpann[āe])(?![^\s,;])"
SPH = rf"{SPHW}(?:,? {SPHW})*"
QW = r"[Kk]usalākusalābyākatā|[Kk]usalākusalā|[Kk]usalābyākatā"
KHALT = "|".join(re.escape(k) for k in sorted(KH_LISTS, key=len, reverse=True))
PAT = [
    ("vip", re.compile(rf"(?P<sas>Sāsavā )?[Kk]usalākusalānaṃ dhammānaṃ (?P<avi>avipakkavipākānaṃ )?vipākā "
                       rf"(?P<sph>{SPH})")),
    ("tp", re.compile(rf"Tehi dhammehi ye dhammā (?P<y>sāsavā|saṃyojaniyā|ganthaniyā), te dhamme ṭhapetvā avasesā "
                      rf"(?P<sas>sāsavā )(?P<q>{QW}) dhammā (?P<sph>{SPH})")),
    ("tv", re.compile(rf"Tehi dhammehi ye dhammā vippayuttā (?P<sas>sāsavā )(?P<q>{QW}) dhammā (?P<sph>{SPH})")),
    ("tehi", re.compile(r"Tehi dhammehi ye dhammā (?P<y>na hetū sahetukā|na hetū ahetukā|sahetukā|ahetukā|"
                        r"sampayuttā|vippayuttā)(?P<ex>,? te dhamme ṭhapetvā)?")),
    ("desc", re.compile(rf"(?P<te>Te dhamme ṭhapetvā,? avasesā )?(?P<sab>Sabbeva )?(?P<sas>[Ss]āsavā )?"
                        rf"(?:(?P<sph1>{SPH}),? )?(?P<q>{QW}) dhammā(?: (?P<sph2>{SPH}))?")),
    ("kh", re.compile(rf"(?P<tam>[Tt]aṃsampayutto )?(?P<kh>(?i:{KHALT}))")),
    ("bhumi", re.compile(rf"(?P<b>\S+?)bhūmiyaṃ (?P<sph>{SPH})(?:, (?P<ex>[^;,]+?) ṭhapetvā)?")),
    ("yanca", re.compile(r"yañca rūpaṃ (?P<y>" + "|".join(re.escape(k) for k in sorted(YANCA, key=len, reverse=True))
                         + r")")),
]


def piece_vi(kind, m):
    g = m.groupdict()
    if kind == "vip":
        v = RESULT_OF + (f" {NOT_RIPE}" if g["avi"] else "") + (f", {SAS}" if g["sas"] else "")
        return "vip", f"{v}, {sph_vi(g['sph'])}"
    if kind in ("tp", "tv", "desc"):
        core = f"các hiện tượng {QV[g['q'].lower()]}"
        if kind == "tp" or g.get("te"):
            core += f" {REMAINING}"
        if g["sas"]:
            core += f" {SAS}"
        sph = g.get("sph") or g.get("sph1") or g.get("sph2")
        if sph:
            core += f", {sph_vi(sph)}"
        if kind == "tp":
            core = f"trong những hiện tượng {TEHI[g['y']]}, {EXCEPT_THOSE}, {core}"
        elif kind == "tv":
            core = f"những hiện tượng {TEHI['vippayuttā']}, tức {core}"
        elif g["te"]:
            core = f"{EXCEPT_THOSE}, {core}"
        elif g["sab"]:
            core = f"tất cả {core}"
        return "desc", core
    if kind == "tehi":
        if g["ex"]:
            return "desc", f"trong những hiện tượng {TEHI[g['y']]}, {EXCEPT_THOSE}"
        return "desc", f"những hiện tượng {TEHI[g['y']]}"
    if kind == "kh":
        k = g["kh"][0].lower() + g["kh"][1:]
        return "kh", KH_LISTS[k] + (f" {WITH_THEM}" if g["tam"] else "")
    if kind == "bhumi":
        ex = g["ex"]
        head = f"{LEVEL} {BHUMI[(g['b'], ex)]}, {sph_vi(g['sph'])}"
        if ex:
            return "x", f"{head}, ngoại trừ {EXCL[ex]}"
        return "desc", head
    if kind == "yanca":
        return "x", f"{RUPA_KIND} {YANCA[g['y']]}"
    raise KeyError(kind)


FIXED_KEYS = sorted(FIXED, key=len, reverse=True)
SEP_RE = re.compile(r"\s*([;,ः])?\s*")


def body_vi(b):
    """an answer body: pieces separated by «;» or «,» in the Pāli -> Vietnamese pieces joined by «; »"""
    items, rest = [], b
    while rest:
        for k in FIXED_KEYS:
            if rest.startswith(k) and (len(rest) == len(k) or not rest[len(k)].isalpha()):
                kind, v = FIXED[k]
                rest = rest[len(k):]
                break
        else:
            for kind0, rx in PAT:
                m = rx.match(rest)
                if m:
                    kind, v = piece_vi(kind0, m)
                    rest = rest[m.end():]
                    break
            else:
                raise KeyError("piece: " + rest[:90])
        sm = SEP_RE.match(rest)
        sep = sm.group(1)
        if sep == "ः":
            slip("the devanāgarī visarga «ः» stands for a punctuation mark: rendered «;»")
        rest = rest[sm.end():]
        items.append((kind, v, sep))
    out, i = [], 0
    while i < len(items):
        kind, v, sep = items[i]
        while i + 1 < len(items):
            nk, nv, ns = items[i + 1]
            if kind == "desc" and nk == "kh":
                v = f"{v}: {nv}"
            elif kind == "vip" and nk == "kh":
                v = f"{nv}, {v}"
            elif kind in ("excl", "lead"):
                v = f"{v}{', ' if sep == ',' else '; '}{nv}"
            else:
                break
            kind, sep = nk, ns
            i += 1
        out.append(v)
        i += 1
    return cap("; ".join(out))


# =========================================================================================
# 4. The «X Y-ena Z ceva Z-sampayutto ca» runs (^1-1083, 1085, 1114, 1136, 1152)
# =========================================================================================
REL_TO = "đối với"                                   # the instrumental «Y-ena» = «đối với Y»
NM = {   # names used in the definitions and the runs
    "sakkāyadiṭṭhi": "quan điểm về tự ngã", "vicikicchā": N["vicikicchā"],
    "sīlabbataparāmāso": "sự hiểu sai lệch về giới hạnh và nghi thức",
    "alobho": N["alobho"], "adoso": N["adoso"], "amoho": N["amoho"],
    "lobho": N["lobho"], "doso": N["doso"], "moho": N["moho"],
    "kāmāsavo": "ô nhiễm dục lạc", "bhavāsavo": "ô nhiễm hiện hữu", "diṭṭhāsavo": "ô nhiễm quan điểm",
    "avijjāsavo": "ô nhiễm vô minh",
    "kāmarāgasaṃyojanaṃ": "xiềng xích tham đắm dục lạc", "paṭighasaṃyojanaṃ": "xiềng xích ác cảm",
    "mānasaṃyojanaṃ": "xiềng xích kiêu mạn", "diṭṭhisaṃyojanaṃ": "xiềng xích quan điểm",
    "vicikicchāsaṃyojanaṃ": "xiềng xích hoài nghi",
    "sīlabbataparāmāsasaṃyojanaṃ": "xiềng xích hiểu sai lệch về giới hạnh và nghi thức",
    "bhavarāgasaṃyojanaṃ": "xiềng xích tham đắm hiện hữu", "issāsaṃyojanaṃ": "xiềng xích ganh tị",
    "macchariyasaṃyojanaṃ": "xiềng xích keo kiệt", "avijjāsaṃyojanaṃ": "xiềng xích vô minh",
    "abhijjhā kāyagantho": "nút thắt của thân bằng sự thèm muốn",
    "byāpādo kāyagantho": "nút thắt của thân bằng sự ác ý",
    "sīlabbataparāmāso kāyagantho": "nút thắt của thân bằng sự hiểu sai lệch về giới hạnh và nghi thức",
    "idaṃsaccābhiniveso kāyagantho": "nút thắt của thân bằng sự cố chấp rằng chỉ điều này là sự thật",
}
NM["idaṃ saccābhiniveso kāyagantho"] = NM["idaṃsaccābhiniveso kāyagantho"]
NM["abhijjhākāyagantho"] = NM["abhijjhā kāyagantho"]
for _n, _h in NUM.items():
    for _k, _v in HETU.items():
        NM[f"{_n} {_k}"] = f"{NUM[_n]} {_v}"
INSTR = {   # instrumental -> nominative key of NM
    "mohena": "moho", "lobhena": "lobho", "dosena": "doso",
    "avijjāsavena": "avijjāsavo", "kāmāsavena": "kāmāsavo", "bhavāsavena": "bhavāsavo",
    "diṭṭhāsavena": "diṭṭhāsavo",
    "abhijjhākāyaganthena": "abhijjhā kāyagantho",
    "sīlabbataparāmāsena kāyaganthena": "sīlabbataparāmāso kāyagantho",
    "idaṃsaccābhinivesena kāyaganthena": "idaṃsaccābhiniveso kāyagantho",
}
for _k in list(NM):
    if _k.endswith("saṃyojanaṃ"):
        INSTR[_k[:-2] + "ena"] = _k                 # kāmarāgasaṃyojanena …

SAM9 = ["kāmarāga", "paṭigha", "māna", "diṭṭhi", "vicikicchā", "sīlabbataparāmāsa", "bhavarāga", "issā", "macchariya"]
RUNS = {   # pred (plural, for the closing) -> (pairs (nominative, instrumental), singular Pāli predicate, tail)
    "hetū ceva sahetukā ca": ([("lobho", "mohena"), ("moho", "lobhena"), ("doso", "mohena"), ("moho", "dosena")],
                              "hetu ceva sahetuko ca", "alobho adoso amoho, te aññamaññaṃ hetū ceva sahetukā ca"),
    "hetū ceva hetusampayuttā ca": ([("lobho", "mohena"), ("moho", "lobhena"), ("doso", "mohena"),
                                     ("moho", "dosena")], "hetu ceva hetusampayutto ca",
                                    "alobho adoso amoho, te aññamaññaṃ hetū ceva hetusampayuttā ca"),
    "āsavā ceva āsavasampayuttā ca": ([("kāmāsavo", "avijjāsavena"), ("avijjāsavo", "kāmāsavena"),
                                       ("bhavāsavo", "avijjāsavena"), ("avijjāsavo", "bhavāsavena"),
                                       ("diṭṭhāsavo", "avijjāsavena"), ("avijjāsavo", "diṭṭhāsavena")],
                                      "āsavo ceva āsavasampayutto ca", None),
    "saṃyojanā ceva saṃyojanasampayuttā ca": (
        [p for s in SAM9 for p in ((f"{s}saṃyojanaṃ", "avijjāsaṃyojanena"),
                                   ("avijjāsaṃyojanaṃ", f"{s}saṃyojanena"))],
        "saṃyojanañceva saṃyojanasampayuttañca", None),
    "ganthā ceva ganthasampayuttā ca": ([("sīlabbataparāmāso kāyagantho", "abhijjhākāyaganthena"),
                                         ("abhijjhākāyagantho", "sīlabbataparāmāsena kāyaganthena"),
                                         ("idaṃsaccābhiniveso kāyagantho", "abhijjhākāyaganthena"),
                                         ("abhijjhākāyagantho", "idaṃsaccābhinivesena kāyaganthena")],
                                        "gantho ceva ganthasampayutto ca", None),
}
MUTUAL = "đối với nhau, chúng"                      # te aññamaññaṃ (no termbase entry for aññamañña)


def runs_fill():
    for pred, (pairs, sg, tail) in RUNS.items():
        p = ", ".join(f"{a} {b} {sg}" for a, b in pairs)
        p = cap(p)
        v = "; ".join(f"{NM[a]}, {REL_TO} {NM[INSTR[b]]}, {P[pred]}" for a, b in pairs)
        if tail:
            p += "; " + tail
            v += f"; {ROOTS_K}: {MUTUAL} {P[pred]}"
        FIXED[p] = ("x", cap(v))


runs_fill()
FIXED_KEYS = sorted(FIXED, key=len, reverse=True)

# =========================================================================================
# 5. Definitions: «Tattha katamo X? [pre] Yo/Yā/Yaṃ [evarūpo] S – ayaṃ vuccati X. [extra]»
# =========================================================================================
REL = S.REL                                         # Điều mà
SUCH = "thuộc loại như vậy"                         # evarūpo / evarūpā / evarūpaṃ (termbase)
HERE_Q = "Ở đây"                                    # Tattha (termbase)
CALLED = "đó được gọi là"                           # ayaṃ / idaṃ vuccati (3-01)


def split_items(s):
    return s.split(", ")


# the strings (after «Điều mà là» / «Điều mà thuộc loại như vậy là»); a value starting «,» carries its own frame
_ADOSA = split_items(S.S_ADOSA)    # sự không sân hận, sự không khởi sân, trạng thái không khởi sân, sự không ác ý, …
METTA_V = ["lòng từ ái", "sự khởi lòng từ ái", "trạng thái khởi lòng từ ái", "lòng thương mến",
           "sự khởi lòng thương mến", "trạng thái khởi lòng thương mến", "sự mong muốn điều lợi ích",
           "lòng thương xót"]
# metti mettāyanā mettāyitattaṃ anuddā anuddāyanā anudāyitattaṃ hitesitā anukampā
LOBHA_ITEMS = [   # (Pāli, Vietnamese, variant)
    ("rāgo", "sự tham đắm", ""), ("sārāgo", "sự say đắm", ""), ("anunayo", "sự chiều theo", ""),
    ("anurodho", "sự xuôi theo", ""), ("nandī", "sự thích thú", ""),
    ("nandīrāgo", "sự tham đắm vì thích thú", "A"), ("cittassa sārāgo", "sự say đắm của tâm", ""),
    ("icchā", "sự mong muốn", ""), ("mucchā", "sự mê đắm", ""), ("ajjhosānaṃ", "sự đắm chìm", ""),
    ("gedho", "sự thèm khát", ""), ("paligedho", "sự thèm khát mãnh liệt", ""), ("saṅgo", "sự dính mắc", ""),
    ("paṅko", "vũng bùn", ""), ("ejā", "sự xao xuyến", ""), ("māyā", "sự huyễn hoặc", ""),
    ("janikā", "kẻ sinh ra", ""), ("sañjananī", "kẻ tạo thành", ""), ("sibbinī", "kẻ khâu nối", "B"),
    ("jālinī", "kẻ giăng lưới", ""), ("saritā", "dòng chảy", ""), ("visattikā", "sự vướng mắc khắp nơi", ""),
    ("suttaṃ", "sợi chỉ", ""), ("visaṭā", "sự lan tràn", ""), ("āyūhinī", "kẻ thúc đẩy", "C"),
    ("dutiyā", "người bạn đồng hành", ""), ("paṇidhi", "sự mong cầu", ""),
    ("bhavanetti", "sợi dây dẫn đến hiện hữu", ""), ("vanaṃ", "rừng", ""), ("vanatho", "bụi rậm", ""),
    ("santhavo", "sự thân thiết", ""), ("sineho", "sự luyến ái", ""), ("apekkhā", "sự quyến luyến", ""),
    ("paṭibandhu", "mối thân thuộc", ""), ("āsā", "sự mong mỏi", ""), ("āsisanā", "sự trông mong", ""),
    ("āsisitattaṃ", "trạng thái trông mong", "D"),
    ("rūpāsā", "sự mong mỏi hình sắc", ""), ("saddāsā", "sự mong mỏi âm thanh", ""),
    ("gandhāsā", "sự mong mỏi mùi", ""), ("rasāsā", "sự mong mỏi vị", ""),
    ("phoṭṭhabbāsā", "sự mong mỏi vật xúc chạm", ""), ("lābhāsā", "sự mong mỏi lợi lộc", ""),
    ("dhanāsā", "sự mong mỏi tài sản", ""), ("puttāsā", "sự mong mỏi con cái", ""),
    ("jīvitāsā", "sự mong mỏi sự sống", ""),
    ("jappā", "sự thèm thuồng", ""), ("pajappā", "sự thèm thuồng mãnh liệt", ""),
    ("abhijappā", "sự thèm thuồng tột độ", ""), ("jappā", "sự thèm thuồng", ""),
    ("jappanā", "sự khởi thèm thuồng", ""), ("jappitattaṃ", "trạng thái khởi thèm thuồng", ""),
    ("loluppaṃ", "sự ham hố", ""), ("loluppāyanā", "sự khởi ham hố", ""),
    ("loluppāyitattaṃ", "trạng thái khởi ham hố", ""), ("pucchañjikatā", "sự xu nịnh", "E"),
    ("sādhukamyatā", "sự mong muốn điều tốt đẹp", ""), ("adhammarāgo", "sự tham đắm phi pháp", ""),
    ("visamalobho", "sự tham lam bất chính", ""), ("nikanti", "sự ưa thích", ""),
    ("nikāmanā", "sự ham muốn", ""), ("patthanā", "sự mong ước", ""), ("pihanā", "sự ước ao", ""),
    ("sampatthanā", "sự mong ước mãnh liệt", ""),
    ("kāmataṇhā", "khao khát dục lạc", ""), ("bhavataṇhā", "khao khát được hiện hữu", ""),
    ("vibhavataṇhā", "khao khát không còn hiện hữu", ""),
    ("rūpataṇhā", "khao khát cõi hình sắc", ""), ("arūpataṇhā", "khao khát cõi không hình sắc", ""),
    ("nirodhataṇhā", "khao khát sự chấm dứt", ""),
    ("rūpataṇhā", "khao khát hình sắc", ""), ("saddataṇhā", "khao khát âm thanh", ""),
    ("gandhataṇhā", "khao khát mùi", ""), ("rasataṇhā", "khao khát vị", ""),
    ("phoṭṭhabbataṇhā", "khao khát vật xúc chạm", ""), ("dhammataṇhā", "khao khát đối tượng của ý", ""),
    ("ogho", "dòng lũ", ""), ("yogo", "ách", ""), ("gantho", "nút thắt", ""), ("upādānaṃ", "sự bám víu", ""),
    ("āvaraṇaṃ", "sự che lấp", ""), ("nīvaraṇaṃ", "chướng ngại", ""), ("chādanaṃ", "sự che đậy", ""),
    ("bandhanaṃ", "sự trói buộc", ""), ("upakkileso", "sự làm ô uế", ""), ("anusayo", "khuynh hướng tiềm ẩn", ""),
    ("pariyuṭṭhānaṃ", "sự ám ảnh", ""), ("latā", "dây leo", ""), ("vevicchaṃ", "sự bủn xỉn", ""),
    ("dukkhamūlaṃ", "gốc rễ của khổ đau", ""), ("dukkhanidānaṃ", "căn nguyên của khổ đau", ""),
    ("dukkhappabhavo", "cội nguồn của khổ đau", ""), ("mārapāso", "bẫy của Ma vương", ""),
    ("mārabaḷisaṃ", "lưỡi câu của Ma vương", ""), ("māravisayo", "lãnh địa của Ma vương", ""),
    ("taṇhānadī", "dòng sông khao khát", ""), ("taṇhājālaṃ", "tấm lưới khao khát", ""),
    ("taṇhāgaddulaṃ", "dây xích khao khát", ""), ("taṇhāsamuddo", "đại dương khao khát", ""),
    ("abhijjhā", N["abhijjhā"], ""), ("lobho", N["lobho"], ""),
]
LOBHA_VAR_P = {"A": " [nandirāgo (sī.)]", "B": " [sibbanī (sī.)]", "C": " [āyūhanī (sī. syā.)]",
               "D": " [āsiṃsanā āsiṃsitattaṃ (sī. syā.)]", "E": " [puñcikatā (syā.) pucchikatā (sī.)]"}
LOBHA_VAR_V = {"A": " " + S.spell("Sī.", "nandirāgo"), "B": " " + S.spell("Sī.", "sibbanī"),
               "C": " " + S.spell("Sī., Syā.", "āyūhanī"), "D": " " + S.spell("Sī., Syā.", "āsiṃsanā āsiṃsitattaṃ"),
               "E": " [khác chính tả (Syā.): puñcikatā; (Sī.): pucchikatā]"}


def lobha(with_var):
    p = " ".join(a + (LOBHA_VAR_P[c] if with_var and c else "") for a, _, c in LOBHA_ITEMS) + " akusalamūlaṃ"
    v = ", ".join(b + (LOBHA_VAR_V[c] if with_var and c else "") for _, b, c in LOBHA_ITEMS)
    return p, f"{v}, {D.ROOT_AKUSALA}"


DOSA_HEAD_P = ("cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso "
               "cittassa byāpatti manopadoso kodho kujjhanā kujjhitattaṃ ")
DOSA_HEAD_V = ("sự oán giận của tâm, sự phẫn uất, sự ác cảm, sự đối nghịch, sự nổi nóng, sự nổi nóng dữ dội, "
               "sự nổi nóng tột độ, sự sân hận, sự sân hận dữ dội, sự sân hận tột độ, sự thù hằn của tâm, "
               "sự sân hận dữ dội của ý, sự giận dữ, sự khởi giận, trạng thái khởi giận, ")
DITTHI_PA = D.DITTHI_P.format(A="", B="").replace("patiṭṭhāho", "paṭiggāho")
DITTHI_V0 = D.DITTHI_V.format(A="", B="")           # patiṭṭhāho and paṭiggāho: both «sự bám chặt» (termbase)
KAMA_ITEMS = ["chando", "rāgo", "nandī", "taṇhā", "sineho", "pariḷāho", "mucchā", "jjhosānaṃ"]


def kama_bhava(stem, var=""):
    """Yo kāmesu kāmacchando … kāmajjhosānaṃ / Yo bhavesu bhavachando … bhavajjhosānaṃ"""
    w = "dục lạc" if stem == "kāma" else "hiện hữu"
    obj = "các dục lạc" if stem == "kāma" else "sự hiện hữu"   # kāmesu / bhavesu
    p = f"{stem[:-1]}esu " + " ".join(
        (f"{stem}c{i}" if (i == "chando" and stem == "kāma") else f"{stem}{i}") + (var if i == "chando" else "")
        for i in KAMA_ITEMS)
    tanha = "khao khát dục lạc" if stem == "kāma" else "khao khát được hiện hữu"
    vv = (f"ý muốn {w}" + (" " + S.spell("Sī., Syā.", "bhavacchando") if var else "") +
          f", sự tham đắm {w}, sự thích thú {w}, {tanha}, sự luyến ái {w}, sự nóng bỏng vì {w}, "
          f"sự mê đắm {w}, sự đắm chìm trong {w}")
    return p, f", đối với {obj}, là {vv}"


STRS = {
    B.P_PANNA: S.S_PANNA,
    "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ": S.S_ALOBHA,
    ("adoso adussanā adussitattaṃ metti mettāyanā mettāyitattaṃ anuddā anuddāyanā anudāyitattaṃ hitesitā anukampā "
     "abyāpādo abyāpajjo adoso kusalamūlaṃ"): ", ".join(_ADOSA[:3] + METTA_V + _ADOSA[3:]),
    "adoso adussanā adussitattaṃ…pe… abyāpādo abyāpajjo adoso kusalamūlaṃ":
        ", ".join(_ADOSA[:3]) + ELL + " " + ", ".join(_ADOSA[3:]),
    DOSA_HEAD_P + D.DOSA_P: DOSA_HEAD_V + D.DOSA_V,
    D.MOHA_P: D.MOHA_V,
    D.VICIKICCHA_P: D.VICIKICCHA_V,
    DITTHI_PA: DITTHI_V0,
    D.DITTHI_P.format(A="", B=""): DITTHI_V0,
    DITTHI_PA.replace("diṭṭhivisūkāyikaṃ", "diṭṭhivisūkāyikaṃ [diṭṭhivisūkāyitaṃ (sī.)]"):
        DITTHI_V0.replace("sự quanh co của quan điểm",
                          "sự quanh co của quan điểm " + S.spell("Sī.", "diṭṭhivisūkāyitaṃ"), 1),
    "māno maññanā maññitattaṃ unnati unnamo [uṇṇati uṇṇāmo (syā.)] dhajo sampaggāho ketukamyatā cittassa":
        ("sự kiêu mạn, sự tự đánh giá mình, trạng thái tự đánh giá mình, sự tự cao, sự vênh vang "
         f"{S.spell('Syā.', 'uṇṇati uṇṇāmo')}, ngọn cờ, sự tự đề cao, sự mong muốn được giương cờ của tâm"),
    ("paralābhasakkāragarukāramānanavandanapūjanāsu issā issāyanā issāyitattaṃ usūyā usūyanā usūyitattaṃ "
     "[ussuyā ussuyanā ussuyitattaṃ (ka.)]"):
        (", trước lợi lộc, sự tôn vinh, sự kính trọng, sự quý trọng, sự đảnh lễ và sự cúng dường mà người khác "
         "nhận được, là sự ganh tị, sự khởi ganh tị, trạng thái khởi ganh tị, sự đố kỵ, sự khởi đố kỵ, "
         f"trạng thái khởi đố kỵ {S.spell('Ka.', 'ussuyā ussuyanā ussuyitattaṃ')}"),
    "maccheraṃ maccharāyanā maccharāyitattaṃ vevicchaṃ kadariyaṃ kaṭukañcukatā aggahitattaṃ cittassa":
        ("sự keo kiệt, sự khởi keo kiệt, trạng thái khởi keo kiệt, sự bủn xỉn, sự hà tiện, sự bo bo, "
         "trạng thái khép chặt của tâm"),
}
for _w in (True, False):
    _p, _v = lobha(_w)
    STRS[_p] = _v
for _args in (("kāma",), ("bhava",), ("bhava", " [bhavacchando (sī. syā.)]")):
    _p, _v = kama_bhava(*_args)
    STRS[_p] = _v


def str_vi(s):
    s2 = s.replace("apaccavekkhaṇā", "apaccavekkhanā")   # the 2-04 string has «-nā»: one word, one Vietnamese
    if s2 in STRS:
        return STRS[s2]
    return B.STR[s2]                                 # composed strings (… dhammavicayasambojjhaṅgo maggaṅgaṃ …)


# the openings before «Yo/Yā/Yaṃ …» (Pāli without its final mark -> Vietnamese without its final mark)
AGG = [("rūpaṃ", "rūpavantaṃ", "rūpaṃ", "rūpasmiṃ", "vật chất"),
       ("Vedanaṃ", "vedanāvantaṃ", "vedanaṃ", "vedanāya", "cảm giác"),
       ("Saññaṃ", "saññāvantaṃ", "saññaṃ", "saññāya", "tri giác"),
       ("Saṅkhāre", "saṅkhāravantaṃ", "saṅkhāre", "saṅkhāresu", "các sự tạo tác"),
       ("Viññāṇaṃ", "viññāṇavantaṃ", "viññāṇaṃ", "viññāṇasmiṃ", "thức")]
SELF = "tự ngã"                                     # attato / attānaṃ / attani (termbase atta «tự ngã»)
SAKKAYA_P = ("Idha assutavā puthujjano ariyānaṃ adassāvī ariyadhammassa akovido ariyadhamme avinīto "
             "sappurisānaṃ adassāvī sappurisadhammassa akovido sappurisadhamme avinīto " +
             ". ".join(f"{a} attato samanupassati, {b} vā attānaṃ, attani vā {c}, {d} vā attānaṃ"
                       for a, b, c, d, _ in AGG))
SAKKAYA_V = ("Ở đời này, người phàm phu không được học hỏi, không thấy các bậc thánh, không thông thạo Giáo Pháp "
             "cao quý, không được rèn luyện trong Giáo Pháp cao quý, không thấy những người chân chính, không thông "
             "thạo Giáo Pháp của những người chân chính, không được rèn luyện trong Giáo Pháp của những người chân "
             "chính, " +
             ". ".join(cap(f"xem {n} là {SELF}, hoặc {SELF} có {n}, hoặc {n} ở trong {SELF}, hoặc {SELF} ở trong {n}")
                       if i else f"xem {n} là {SELF}, hoặc {SELF} có {n}, hoặc {n} ở trong {SELF}, hoặc {SELF} "
                                 f"ở trong {n}" for i, (_, _, _, _, n) in enumerate(AGG)))
DOUBT_ON = [("Satthari", "Bậc Đạo Sư"), ("dhamme", "Giáo Pháp"), ("saṅghe", "Tăng đoàn"), ("sikkhāya", "sự tu học"),
            ("pubbante", "quá khứ"), ("aparante", "tương lai"), ("pubbantāparante", "quá khứ và tương lai"),
            ("idappaccayatā paṭiccasamuppannesu dhammesu",
             "quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện")]
VICI_P = ", ".join(f"{a} kaṅkhati vicikicchati" for a, _ in DOUBT_ON)
VICI_V = cap(", ".join(f"nghi ngờ và hoài nghi về {b}" for _, b in DOUBT_ON))
TRUTHS = [("Dukkhe", "khổ đau"), ("dukkhasamudaye", "sự phát sinh của khổ đau"),
          ("dukkhanirodhe", "sự chấm dứt khổ đau"),
          ("dukkhanirodhagāminiyā paṭipadāya", "cách thực hành dẫn đến sự chấm dứt khổ đau")] + DOUBT_ON[4:]
AMOHA_PRE_P = ", ".join(f"{a} ñāṇaṃ" for a, _ in TRUTHS)
AMOHA_PRE_V = cap(", ".join(f"hiểu biết về {b}" for _, b in TRUTHS))
MOHA_PRE_P = ", ".join(f"{a} aññāṇaṃ" for a, _ in TRUTHS)
MOHA_PRE_V = cap(", ".join(f"sự không biết về {b}" for _, b in TRUTHS))
GROUNDS_P = ("Anatthaṃ me acarīti āghāto jāyati, anatthaṃ me caratīti āghāto jāyati, anatthaṃ me carissatīti "
             "āghāto jāyati, piyassa me manāpassa anatthaṃ acari…pe… anatthaṃ carati…pe… anatthaṃ carissatīti "
             "āghāto jāyati, appiyassa me amanāpassa atthaṃ acari…pe… atthaṃ carati…pe… atthaṃ carissatīti "
             "āghāto jāyati, aṭṭhāne vā pana āghāto jāyati")
ANNOY = "sự oán giận khởi lên với ý nghĩ"           # X-ti āghāto jāyati (āghāto jāyati «sự oán giận khởi lên»)
GROUNDS_V = cap(f"{ANNOY} “Người ấy đã gây hại cho tôi”, {ANNOY} “Người ấy đang gây hại cho tôi”, "
                f"{ANNOY} “Người ấy sẽ gây hại cho tôi”, {ANNOY} “Người ấy đã gây hại cho người yêu quý, ưa thích "
                f"của tôi{ELL} đang gây hại{ELL} sẽ gây hại”, {ANNOY} “Người ấy đã làm lợi cho người không yêu quý, "
                f"không ưa thích của tôi{ELL} đang làm lợi{ELL} sẽ làm lợi”, hoặc sự oán giận khởi lên một cách "
                "vô cớ")
VIEWS = [("Sassato loko", "Thế gian là trường tồn"), ("asassato loko", "Thế gian không trường tồn"),
         ("antavā loko", "Thế gian là hữu hạn"), ("anantavā loko", "Thế gian là vô hạn"),
         ("taṃ jīvaṃ taṃ sarīraṃ", "Linh hồn và thân thể là một"),
         ("aññaṃ jīvaṃ aññaṃ sarīraṃ", "Linh hồn là khác, thân thể là khác"),
         ("hoti tathāgato paraṃ maraṇā", "Như Lai còn tồn tại sau khi chết"),
         ("na hoti tathāgato paraṃ maraṇā", "Như Lai không còn tồn tại sau khi chết"),
         ("hoti ca na ca hoti tathāgato paraṃ maraṇā", "Như Lai vừa còn tồn tại vừa không còn tồn tại sau khi chết"),
         ("neva hoti na na hoti tathāgato paraṃ maraṇā",
          "Như Lai không phải còn tồn tại cũng không phải không còn tồn tại sau khi chết")]


def ti(p):
    return p[:-1] + "nti" if p.endswith("ṃ") else p + "ti"


VIEWS_P = ", ".join(f"{ti(a)} vā" for a, _ in VIEWS)
VIEWS_V = ", hoặc ".join(f"“{b}”" for _, b in VIEWS)
ONLY_TRUE = "chỉ điều này là sự thật, mọi điều khác đều sai"   # idameva saccaṃ moghamaññaṃ (termbase)
VIEWS2_P = "; ".join(f"{a}, idameva saccaṃ moghamaññanti vā" for a, _ in VIEWS)
VIEWS2_V = "; hoặc ".join(f"“{b}, {ONLY_TRUE}”" for _, b in VIEWS)
RITES_V = ("Các sa-môn và bà-la-môn bên ngoài Giáo Pháp này cho rằng “Trong sạch nhờ giới hạnh, trong sạch nhờ "
           "nghi thức, trong sạch nhờ giới hạnh và nghi thức”")
PRE = {
    SAKKAYA_P: SAKKAYA_V,
    VICI_P: VICI_V,
    AMOHA_PRE_P: AMOHA_PRE_V,
    MOHA_PRE_P: MOHA_PRE_V,
    GROUNDS_P: GROUNDS_V,
    GROUNDS_P.replace("acarīti", "acarī ti", 1): GROUNDS_V,
    VIEWS_P: VIEWS_V,
    VIEWS2_P: VIEWS2_V,
    "Ito bahiddhā samaṇabrāhmaṇānaṃ ‘sīlena suddhi, vatena suddhi, sīlabbatena suddhī’ti": RITES_V,
    "Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi vatena suddhi sīlabbatena suddhīti": RITES_V,
    "Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi, vatena suddhi, sīlabbatena suddhīti": RITES_V,
    "Seyyohamasmīti māno, sadisohamasmīti māno, hīnohamasmīti māno":
        "Sự kiêu mạn “Tôi hơn người”, sự kiêu mạn “Tôi bằng người”, sự kiêu mạn “Tôi kém người”",
    ("Pañca macchariyāni – āvāsamacchariyaṃ, kulamacchariyaṃ, lābhamacchariyaṃ, vaṇṇamacchariyaṃ, "
     "dhammamacchariyaṃ"):
        (f"Năm loại keo kiệt {DASH} keo kiệt về chỗ ở, keo kiệt về gia đình, keo kiệt về lợi lộc, "
         "keo kiệt về lời khen, keo kiệt về Giáo Pháp"),
}
EVERY_WRONG = f"mọi {D.NEW_NAMES['micchādiṭṭhi']} đều là"   # sabbāpi micchādiṭṭhi X
EXTRA = {
    "Sabbāpi micchādiṭṭhi diṭṭhāsavo.": f"{cap(EVERY_WRONG)} {NM['diṭṭhāsavo']}.",
    "Ṭhapetvā sīlabbataparāmāsasaṃyojanaṃ sabbāpi micchādiṭṭhi diṭṭhisaṃyojanaṃ.":
        f"Ngoại trừ {NM['sīlabbataparāmāsasaṃyojanaṃ']}, {EVERY_WRONG} {NM['diṭṭhisaṃyojanaṃ']}.",
    "Ṭhapetvā sīlabbataparāmāsaṃ kāyaganthaṃ sabbāpi micchādiṭṭhi idaṃsaccābhiniveso kāyagantho.":
        f"Ngoại trừ {NM['sīlabbataparāmāso kāyagantho']}, {EVERY_WRONG} {NM['idaṃsaccābhiniveso kāyagantho']}.",
}
DEF_RE = re.compile(r"(?P<head>.+) – (?:ayaṃ|idaṃ) vuccati (?P<x>.+?)\.(?: (?P<extra>.+))?$")
REL_RE = re.compile(r"(?:^|(?<=\s))(?P<rel>Yo|Yā|Yaṃ|yo|yā|yaṃ) (?:(?P<ev>evarūpo|evarūpā|evarūpaṃ) )?")


def def_vi(rest):
    m = DEF_RE.fullmatch(rest)
    if not m:
        return rest_vi(rest)
    head, x, extra = m.group("head"), m.group("x"), m.group("extra")
    r = REL_RE.search(head)
    pre, body = head[:r.start()].rstrip(), head[r.end():]
    out = ""
    rel = REL
    if pre:
        mark = ""
        if pre[-1] in ".,;ः":
            pre, mark = pre[:-1], pre[-1]
        if mark == "ः":
            slip("the devanāgarī visarga «ः» stands for a punctuation mark: rendered «;»")
        if "acarī ti" in pre:
            slip("«acarī ti» (a space inside the word): rendered as «acarīti»")
        out = PRE[pre] + ("." if mark == "." else ";") + " "
        if mark != ".":
            rel = REL[0].lower() + REL[1:]
    sv = str_vi(body)
    if sv.startswith(","):
        out += f"{rel}{sv}"
    elif r.group("ev"):
        out += f"{rel} {SUCH} là {sv}"
    else:
        out += f"{rel} là {sv}"
    out += f" {DASH} {CALLED} {NM[x]}."
    if extra:
        out += " " + EXTRA[extra]
    return out


# =========================================================================================
# 6. Sentences, lines
# =========================================================================================
PRED_X = {
    "dassanena pahātabbahetū": "là gốc rễ cần dứt bỏ bằng sự thấy chân lý",   # pahātabba + hetū «gốc rễ»
    "bhāvanāya pahātabbahetū": "là gốc rễ cần dứt bỏ bằng sự tu tập",
    "maggahetū": "là gốc rễ của con đường",          # termbase maggahetū «gốc rễ của con đường»
    "neva ācayagāmi na apacayagāmino": P["nevācayagāmināpacayagāmino"],   # = the matrix item (R.EKAKA alike)
    "kenaci viññeyyā, kenaci na viññeyyā": f"{P['kenaci viññeyyā']}, {P['kenaci na viññeyyā']}",
    "kenaci viññeyyā kenaci na viññeyyā": f"{P['kenaci viññeyyā']}, {P['kenaci na viññeyyā']}",
}
assert PRED_X["dassanena pahātabbahetū"] == "là gốc rễ " + S.T_SEE


def pred(x):
    if x in PRED_X:
        if x == "kenaci viññeyyā kenaci na viññeyyā":
            slip("«kenaci viññeyyā kenaci na viññeyyā» without the comma of the question: the same Vietnamese")
        return PRED_X[x]
    return P[x]


FIXED_SENT = {
    "Tīṇi saṃyojanāni – sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāso.": f"Ba xiềng xích {DASH} {FETTERS3}.",
    "Alobho, adoso, amoho.": cap(ROOTS_K) + ".",
    "Lobho, doso, moho.": cap(ROOTS_A) + ".",
    "Cattāro āsavā – kāmāsavo, bhavāsavo, diṭṭhāsavo, avijjāsavo.":
        f"Bốn ô nhiễm {DASH} " + ", ".join(NM[k] for k in ("kāmāsavo", "bhavāsavo", "diṭṭhāsavo", "avijjāsavo")) + ".",
    ("Dasa saṃyojanāni – " + ", ".join(f"{s}saṃyojanaṃ" for s in SAM9[:7] + ["issā", "macchariya", "avijjā"]) + "."):
        f"Mười xiềng xích {DASH} " + ", ".join(NM[f"{s}saṃyojanaṃ"] for s in SAM9 + ["avijjā"]) + ".",
    ("Cattāro ganthā – abhijjhā kāyagantho, byāpādo kāyagantho, sīlabbataparāmāso kāyagantho, idaṃ saccābhiniveso "
     "kāyagantho."):
        f"Bốn nút thắt {DASH} " + ", ".join(NM[k] for k in ("abhijjhā kāyagantho", "byāpādo kāyagantho",
                                                            "sīlabbataparāmāso kāyagantho",
                                                            "idaṃ saccābhiniveso kāyagantho")) + ".",
    ("Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū, nava kāmāvacarahetū cha rūpāvacarahetū, "
     "cha arūpāvacarahetū, cha apariyāpannahetū."):
        cap(hetus("Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū, nava kāmāvacarahetū, cha rūpāvacarahetū, "
                  "cha arūpāvacarahetū, cha apariyāpannahetū")) + ".",
    "Teyeva āsavā āsavā ceva sāsavā ca.": f"Chính các ô nhiễm ấy {P['āsavā ceva sāsavā ca']}.",
    "Tāneva saṃyojanāni saṃyojanā ceva saṃyojaniyā ca.":
        f"Chính các xiềng xích ấy {P['saṃyojanā ceva saṃyojaniyā ca']}.",
    "Teva ganthā ganthā ceva ganthaniyā ca.": f"Chính các nút thắt ấy {P['ganthā ceva ganthaniyā ca']}.",
    "Yeva te dhammā sappaccayā, teva te dhammā saṅkhatā.":
        f"Những hiện tượng nào {P['sappaccayā']} thì chính những hiện tượng ấy {P['saṅkhatā']}.",
    "Yo eva so dhammo appaccayo, so eva so dhammo asaṅkhato.":
        f"Hiện tượng nào {P['appaccayā']} thì chính hiện tượng ấy {P['asaṅkhatā']}.",
}
SLIP_SENT = {
    ("Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū, nava kāmāvacarahetū cha rūpāvacarahetū, "
     "cha arūpāvacarahetū, cha apariyāpannahetū."): "no comma before «cha rūpāvacarahetū»: rendered as meant (comma)",
}
KENACI_RE = re.compile(r"Ye te dhammā (\S+)viññeyyā, na te dhammā (\S+)viññeyyā; ye vā pana te dhammā (\S+)viññeyyā"
                       r"(,?) na te dhammā (\S+)viññeyyā\.")
ORG = {k[:-len("viññeyyaṃ")]: v for k, v in R.VINN.items()}   # cakkhu -> mắt …


def kenaci_vi(m):
    a, b, b2, comma, a2 = m.groups()
    assert a == a2 and b == b2, m.group(0)
    if not comma:
        slip("no comma before «na te dhammā»: rendered as meant")
    return (f"Những hiện tượng mà {ORG[a]} có thể nhận biết thì {ORG[b]} không thể nhận biết; còn những hiện tượng "
            f"mà {ORG[b]} có thể nhận biết thì {ORG[a]} không thể nhận biết.")


ANS_RE = re.compile(r"(.+) – ime dhammā (.+)\.")
ANS_N_RE = re.compile(r"(.+) – ime (tayo|nava|cha) (\S+)\.")
IME_RE = re.compile(r"Ime dhammā (.+)\.")
IME_N_RE = re.compile(r"Ime (tayo|nava|cha) (\S+)\.")
SENT_SPLIT = re.compile(r"(?<=\.) (?=[A-ZĀĪŪṬḌṆÑ])")


def sentence_vi(s):
    if s in FIXED_SENT:
        if s in SLIP_SENT:
            slip(SLIP_SENT[s])
        return FIXED_SENT[s]
    m = KENACI_RE.fullmatch(s)
    if m:
        return kenaci_vi(m)
    m = IME_RE.fullmatch(s)
    if m:
        return cap(S.a_form(pred(m.group(1))))
    m = IME_N_RE.fullmatch(s)
    if m:
        return f"Đó là {NUM[m.group(1)]} {HETU[m.group(2)]}."
    m = ANS_N_RE.fullmatch(s)
    if m and " – ime dhammā " not in s:
        return f"{body_vi(m.group(1))} {DASH} đó là {NUM[m.group(2)]} {HETU[m.group(3)]}."
    m = ANS_RE.fullmatch(s)
    if m:
        return f"{body_vi(m.group(1))} {DASH} {S.a_form(pred(m.group(2)))}"
    raise KeyError("sentence: " + s[:90])


def rest_vi(rest):
    return " ".join(sentence_vi(s) for s in SENT_SPLIT.split(rest))


H = {
    "### Nikkhepakaṇḍaṃ": f"### {S.CH_HEADINGS['Nikkhepakaṇḍaṃ']}",
    "#### Tikanikkhepaṃ": "#### Tóm lược bộ ba",      # nikkhepaṃ «tóm lược», Tika «bộ ba» (1-matika)
    "#### Dukanikkhepaṃ": "#### Tóm lược bộ đôi",
    "##### Hetugocchakaṃ": f"##### {S.CLUSTERS['hetu']['heading']}",
    "##### Cūḷantaradukaṃ": f"##### {S.CUULANTARA}",
    "##### Āsavagocchakaṃ": f"##### {S.CLUSTERS['asava']['heading']}",
    "##### Saṃyojanagocchakaṃ": f"##### {S.CLUSTERS['samyojana']['heading']}",
    "##### Ganthagocchakaṃ": f"##### {S.CLUSTERS['gantha']['heading']}",
    "Tikaṃ.": "Bộ ba.",
    "Nikkhepakaṇḍe paṭhamabhāṇavāro.": f"{S.BHANAVARA_1} trong {S.CH_HEADINGS['Nikkhepakaṇḍaṃ'][0].lower()}"
                                       f"{S.CH_HEADINGS['Nikkhepakaṇḍaṃ'][1:]}.",
}
assert H["Nikkhepakaṇḍe paṭhamabhāṇavāro."] == "Phần tụng đọc thứ nhất trong phần tóm lược."
KQ_RE = re.compile(r"Katame dhammā (.+?)\? (.+)$")
TQ_RE = re.compile(r"Tattha katam(o|ā|aṃ|e) (.+?)(\?|…pe…) ?(.*)$")


def translate_line(line):
    if line in H:
        return H[line]
    m = KQ_RE.fullmatch(line)
    if m:
        return f"{S.q_form(pred(m.group(1)))} {rest_vi(m.group(2))}"
    m = TQ_RE.fullmatch(line)
    if m:
        g, x, mark, rest = m.groups()
        nm = NM[x]
        if mark == PE:
            m2 = re.fullmatch(r"(?:ayaṃ|idaṃ) vuccati (.+)\.", rest)
            assert m2 and m2.group(1) == x, line
            return f"{HERE_Q}, {nm} là gì{ELL} {CALLED} {nm}."
        return f"{HERE_Q}, {nm} là {'những gì' if g == 'e' else 'gì'}? {def_vi(rest)}"
    return rest_vi(line)


# =========================================================================================
# 7. Render, checks, build
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
            assert v.endswith(".") or v.endswith("?") or v.startswith("#"), ("stop", sid, v[-40:])
            assert "  " not in v and " ," not in v and ",," not in v and "..." not in v and " ;" not in v, (
                "spacing", sid, v)
            assert ", ," not in v and ",:" not in v and ";," not in v and "…." not in v and ";;" not in v, (
                "punct", sid, v)
            assert "đau khổ" not in v and "là là" not in v and "chánh niệm" not in v, sid
            vlines.append(v)
        vlines[-1] += f" ^{sid}"
        blocks.append("\n".join(vlines))
    return blocks


def check_earlier_unchanged():
    """Importing 3-02/3-03 (and through it 3-01 … 2-01) must leave their outputs exactly as finished."""
    Q.check_earlier_unchanged()
    for part in Q.PARTS:
        text, _ = Q.build(part)
        assert unicodedata.normalize("NFC", text) == (S.OUT / part).read_bytes().decode("utf-8"), part
        print(f"{part}: rebuilt in memory, byte-identical to the finished file")


def build():
    segs = B.segments(S.PALI / PART)
    text = "\n\n".join(render(segs)) + "\n"
    i987 = [s for s, _ in segs].index("1-987")
    assert render([segs[i987]])[0] == R.U583_V + " ^1-987", "^1-987 must repeat ^1-583 word for word"
    return text, len(segs)


# =========================================================================================
# 8. Notes
# =========================================================================================
def notes():
    L = ["# pi-1 Vietnamese rails: new formulas of 4-01", "",
         "Generated by build_rails_4-01_vi.py from its fixed strings; import that file instead of retyping "
         "(FIXED, PAT/piece_vi, body_vi, STRS, PRE, NM, RUNS, H). Strings already in vi-rails-formulas.md, the "
         "chapter-2 notes or the chapter-3 notes are not repeated. The question and answer frames are 1-matika's "
         "(S.q_form / S.a_form with S.PREDS) verbatim. Format: Pāli = tiếng Việt.", "",
         "## Frames", "",
         f"Katame dhammā X? … – ime dhammā X. = Những hiện tượng nào pred(X)? … – những hiện tượng này pred(X).",
         f"^1-987 (= ^1-583, punctuation aside) = {R.U583_V}",
         f"Tattha katamo/katamā/katamaṃ X? = {HERE_Q}, X là gì?   (katame: «là những gì?»)",
         f"Tattha katamā X…pe… ayaṃ vuccati X. = {HERE_Q}, X là gì{ELL} {CALLED} X.",
         f"Yo/Yā/Yaṃ S – ayaṃ/idaṃ vuccati X. = {REL} là S {DASH} {CALLED} X.",
         f"Yo/Yā/Yaṃ evarūpo/evarūpā/evarūpaṃ S = {REL} {SUCH} là S",
         f"PRE. Yo evarūpo S … = PRE. {REL} {SUCH} là S …;  PRE, / PRE; / PREः yā evarūpā S = PRE; "
         f"{REL.lower()} {SUCH} là S",
         f"Ime dhammā X. (own sentence) = {cap(S.a_form('pred(X)'))}",
         f"Ime tayo X. / – ime nava X. = Đó là ba X. / – đó là chín X.",
         f"X Y-ena Z ceva Z-sampayutto ca = X, {REL_TO} Y, vừa là Z vừa …  (pairs joined with «; »)",
         f"alobho adoso amoho, te aññamaññaṃ … = {ROOTS_K}: {MUTUAL} …",
         "Answer pieces are joined with «; »; a description is followed by «: » and its aggregates; the results "
         "(Kusalākusalānaṃ dhammānaṃ vipākā …) put the aggregates first, as ^1-583.", "",
         "## Pieces of the answers", ""]
    for p, (k, v) in FIXED.items():
        if len(p) < 400:
            L.append(f"{p} = {v}")
    L += [f"taṃsampayutto KH = KH {WITH_THEM}",
          f"KH lists: " + "; ".join(f"{p} = {v}" for p, v in KH_LISTS.items()),
          f"Kusalākusalānaṃ dhammānaṃ vipākā SPH; KH = KH, {RESULT_OF}, SPH",
          f"Sāsavā kusalākusalānaṃ dhammānaṃ vipākā SPH; KH = KH, {RESULT_OF}, {SAS}, SPH",
          f"Kusalākusalānaṃ dhammānaṃ avipakkavipākānaṃ vipākā SPH; KH = KH, {RESULT_OF} {NOT_RIPE}, SPH",
          f"[Sāsavā] kusalākusalā / kusalābyākatā / kusalākusalābyākatā dhammā SPH; KH = "
          f"Các hiện tượng {QV['kusalākusalā']} / {QV['kusalābyākatā']} / {QV['kusalākusalābyākatā']} [{SAS}], SPH: KH",
          f"Te dhamme ṭhapetvā avasesā … dhammā SPH; KH = {cap(EXCEPT_THOSE)}, các hiện tượng … {REMAINING}, SPH: KH",
          f"Sabbeva kāmāvacarā … dhammā = {cap('tất cả')} các hiện tượng …, {P['kāmāvacarā']}",
          f"SPH (kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā) = {R.SPHERES}",
          f"X-bhūmiyaṃ SPH(loc.), Y ṭhapetvā; taṃsampayutto KH = {cap(LEVEL)} attr(X), SPH, ngoại trừ Y; KH {WITH_THEM}"]
    for (b, ex), v in BHUMI.items():
        L.append(f"  {b}bhūmiyaṃ{' (… ' + ex + ' ṭhapetvā)' if ex else ''} = {cap(LEVEL)} {v}")
    for p, v in EXCL.items():
        L.append(f"  {p} ṭhapetvā = ngoại trừ {v}")
    for y, v in TEHI.items():
        L.append(f"Tehi dhammehi ye dhammā {y} = những hiện tượng {v}")
    L += [f"Tehi dhammehi ye dhammā Y, te dhamme ṭhapetvā = trong những hiện tượng Y, {EXCEPT_THOSE}",
          f"Tehi dhammehi ye dhammā vippayuttā sāsavā … dhammā SPH = những hiện tượng {TEHI['vippayuttā']}, tức các "
          f"hiện tượng … {SAS}, SPH",
          f"yañca rūpaṃ X = {RUPA_KIND} X: " + "; ".join(f"{p} = {v}" for p, v in YANCA.items()),
          f"Ye te dhammā A-viññeyyā, na te dhammā B-viññeyyā; ye vā pana … = Những hiện tượng mà A có thể nhận "
          f"biết thì B không thể nhận biết; còn những hiện tượng mà B có thể nhận biết thì A không thể nhận biết.",
          "", "## Definitions: the strings", ""]
    for p, v in STRS.items():
        L.append(f"{p} = {v}")
    L += ["", "## Definitions: the openings", ""]
    for p, v in PRE.items():
        L.append(f"{p} = {v}")
    for p, v in EXTRA.items():
        L.append(f"{p} = {v}")
    L += ["", "## Sentences", ""]
    for p, v in FIXED_SENT.items():
        L.append(f"{p} = {v}")
    for p, v in PRED_X.items():
        L.append(f"pred «{p}» = {v}")
    L += ["", "## Names", ""]
    for p, v in NM.items():
        L.append(f"{p} = {v}")
    L += ["", "## Headings and closing lines", ""]
    for p, v in H.items():
        L.append(f"{p} = {v}")
    L += ["", "## Source slips and marks (translated as written; punctuation rendered as meant)", ""]
    by_note = {}
    for sid, note in dict.fromkeys(SLIPS):
        by_note.setdefault(note, []).append(f"^{sid}")
    for note, sids in by_note.items():
        L.append(f"{', '.join(sids)}: {note}")
    L += ["^1-1010: «kāyakammaṃ vacīkammaṃ manokammaṃ» without commas: the same Vietnamese as the parallels",
          "^1-1124, ^1-1143, ^1-1144: «patiṭṭhāho» (as 2-04) where ^1-1007, 1009, 1105, 1122 have «paṭiggāho»: "
          "both are «sự bám chặt» in the termbase, so the Vietnamese is the same",
          "^1-1022: «neva ācayagāmi na apacayagāmino» (the matrix has nevācayagāmināpacayagāmino) = the matrix "
          "wording", "^1-1009 ‘…’ti, ^1-1124 no quotation marks, ^1-1143 commas: one Vietnamese, in “…”",
          "^1-1067, 1106, 1128 «apaccavekkhaṇā» = 2-04's «apaccavekkhanā» (one word, the same Vietnamese)",
          "", "## Termbase notes", "",
          "taṃsampayutto: sampayutto «gắn liền» + taṃ = «gắn liền với chúng» (one rendering everywhere, also where "
          "taṃ points to one feeling: the feelings of the several spheres)",
          "taṃsamuṭṭhānaṃ: samuṭṭhānaṃ «do … sinh ra» = «do chúng sinh ra»; tadekaṭṭhā ca kilesā = the termbase "
          "«và các phiền não cùng hiện diện» + «với chúng»",
          "Sukhabhūmiyaṃ: «ở cấp độ có cảm giác dễ chịu» in ^1-988 (feeling triad, as Dukkha- / Adukkhamasukha-, "
          "«cảm giác» added for clarity) but «ở cấp độ có hạnh phúc» in ^1-1004 (sukhaṃ ṭhapetvā, the matrix "
          "«có hạnh phúc đi kèm»): the same Pāli, two senses of the termbase sukha",
          "bhūtā / abhūtā (^1-1041 …): termbase only bhūtā «yếu tố» (the elements) = «đã trở thành» / «chưa trở thành»",
          "samuppannā «sinh khởi» = uppannā: written «đã sinh khởi trọn vẹn» (asamuppannā «chưa sinh khởi trọn vẹn»), "
          "like samuṭṭhitā «đã trỗi dậy trọn vẹn»",
          "atthaṃ acari / carati / carissati (^1-1066, 1120, 1142): acarīti «đã gây» covers harm only = «làm lợi»",
          "Idha «Ở đời này», adassāvī «không thấy», saṅghe «Tăng đoàn», pubbante / aparante «quá khứ» / «tương lai» "
          "(as 1-matika pubbantānudiṭṭhi), vicikicchati «hoài nghi», Māra «Ma vương», lābha «lợi lộc», "
          "heṭṭhimāni «thấp hơn», seyyo «hơn», loko «thế gian» (3-02), saṅgahitā «được gộp vào», ubhaya «cả hai», "
          "aññamaññaṃ «đối với nhau», maccheraṃ «sự keo kiệt», ajjhosānaṃ «sự đắm chìm», nandīrāgo «sự tham đắm vì "
          "thích thú», manopadoso «sự sân hận dữ dội của ý», kujjhitattaṃ «trạng thái khởi giận», issāyitattaṃ / "
          "usūyitattaṃ / maccharāyitattaṃ / jappitattaṃ / loluppāyitattaṃ / āsisitattaṃ «trạng thái …»: no entries, "
          "built from the members",
          "ariyadhammassa / ariyadhamme: Ariya (stem) «cao quý» + dhammassa «Giáo Pháp» = «Giáo Pháp cao quý»; "
          "sappurisadhamma = «Giáo Pháp của những người chân chính»",
          "rūpataṇhā twice in the lobha string: first with arūpataṇhā nirodhataṇhā (the spheres) «khao khát cõi hình "
          "sắc», then with saddataṇhā … (the sense objects) «khao khát hình sắc»",
          "Kusalānaṃ dhammānaṃ vipākato (^1-1068, 1077): vipākato «quả của nghiệp» = «trong quả của các hiện tượng "
          "thiện» (as ^1-583 «là quả của các hiện tượng thiện và bất thiện»)",
          "kāyakammaṃ «nghiệp bằng thân», vacīkammaṃ «nghiệp bằng lời nói», manokammaṃ «nghiệp bằng ý» (termbase)"]
    (HERE / "notes-4-01.md").write_text(unicodedata.normalize("NFC", "\n".join(L) + "\n"), encoding="utf-8",
                                       newline="\n")
    print("wrote", HERE / "notes-4-01.md")


def main():
    check_earlier_unchanged()
    text, n = build()
    (S.OUT / PART).write_text(unicodedata.normalize("NFC", text), encoding="utf-8", newline="\n")
    print("wrote", S.OUT / PART, n, "segments")
    notes()


if __name__ == "__main__":
    main()
