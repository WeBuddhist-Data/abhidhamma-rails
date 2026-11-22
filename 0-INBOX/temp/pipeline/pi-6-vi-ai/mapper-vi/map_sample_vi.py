"""Build the SAMPLE Pāli->Vietnamese keyword maps for pi-6 (Yamaka): preamble, 1-mulayamaka.

usage: python -I -X utf8 -B map_sample_vi.py                     (writes the two <part>.mapped.md and verifies them)
       python -I -X utf8 -B map_sample_vi.py dump PART [miss]    (every distinct keyword=value with count, first
                                                                 segments and the pi-1 … pi-5 map values; writes nothing)
       python -I -X utf8 -B map_sample_vi.py show PART lo hi [pi] (segments lo..hi: Vietnamese (and Pāli), every pair
                                                                 with the English value; writes nothing)
       python -I -X utf8 -B map_sample_vi.py look kw ...         (pi-1 … pi-5 map values; writes nothing)

Importing this module builds nothing. Later part scripts (map_2-01_vi.py …, loaded with importlib) import from here:
    from map_sample_vi import FORMULAS, YM, X_ADJ, X_NOUN, root_value, series_value, context6, value6
Resolution order per keyword: OVERRIDES[bid][kw] -> value6(): your table -> context6 (segment rules: the root
compounds, the hetuvāra series, «X dhammā», kusala / akusala / abyākata / nāma as adjective or noun, the frame words
that depend on the segment) -> FORMULAS (the recurring Yamaka frame words and section headings) -> YM (pi-6 terms) ->
two-word composition (Vietnamese order as it stands) -> the pi-5 chain (T2 … T31 -> context5 -> pi-5 FORMULAS -> KV ->
pi-4 … pi-1).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md.
"""
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_common_vi as M  # noqa: E402
from map_common_vi import (CORE, GAP, NDE, build_part, compose, en, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           pi3_map_values, pi4_map_values, pi5_map_values, pi5_value, pick, present, present_strict,
                           read_keywords, read_pali, read_vietnamese, verify)

PARTS = ["preamble", "1-mulayamaka"]

# ---------------------------------------------------------------------------- the four ethical / nāma slots
# adjective (predicate «… là thiện», attribute «gốc rễ thiện») and noun (subject «Hiện tượng thiện thì …»,
# «Vật chất do hiện tượng thiện sinh ra»), as build_sample_vi.py writes them
X_ADJ = {"kusala": "thiện", "akusala": "bất thiện", "abyākata": "không xác định về mặt đạo đức",
         "nāma": "thuộc phần tinh thần"}
X_NOUN = {"kusala": "hiện tượng thiện", "akusala": "hiện tượng bất thiện",
          "abyākata": "hiện tượng không xác định về mặt đạo đức", "nāma": "phần tinh thần"}
_X_ORDER = sorted(X_ADJ, key=len, reverse=True)

# ---------------------------------------------------------------------------- the root compounds (Mūlayamaka)
# kind -> (X-compound «… X», eka- «cùng một», aññamañña- «… nhau», bare noun)
ROOT_KINDS = [
    ("mūlamūlaka", "bắt nguồn từ cội rễ", "bắt nguồn từ cùng một cội rễ", "bắt nguồn từ cội rễ của nhau", None),
    ("mūlaka", "bắt nguồn từ gốc rễ", "bắt nguồn từ cùng một gốc rễ", "bắt nguồn từ gốc rễ của nhau", None),
    ("mūlamūla", "cội rễ", "có cùng một cội rễ", "làm cội rễ cho nhau", "cội rễ"),
    ("mūla", "gốc rễ", "có cùng một gốc rễ", "làm gốc rễ cho nhau", "gốc rễ"),
]
_ENDINGS = ("ānaṃ", "āni", "ena", "āya", "aṃ", "ā", "o", "e", "a")


def _strip(k):
    """Bare stem of an inflected keyword (lower case): -ti of the question dropped («kusalamūlāti»), the particles
    -ñceva / -ñca / ceva / ca dropped («ekamūlañceva», «nidānañca»: ca / ceva have no word of their own; «vừa … vừa»
    is the frame), then the case ending (-ā, -āni, -aṃ, -ena, -o …). Returns (stem ending in -a, ending)."""
    if len(k) > 3 and k.endswith("ti") and k[-3] in "āīū":
        k = k[:-2]
    for p in ("ñceva", "ñca"):
        if k.endswith(p):
            return k[: -len(p)], "aṃ"
    for e in _ENDINGS:
        if k.endswith(e) and len(k) > len(e) + 1:
            return (k[: -len(e)] + "a" if e != "a" else k), e
    return k, ""


def root_value(kw):
    """Candidate values of a root compound (Xmūla, Xmūlena, ekamūla…, aññamaññamūla…, Xmūlasahajāta, bare mūla /
    mūlamūla), best first; None if the keyword is not one. The caller keeps the first candidate present."""
    k = lc(kw).lower()
    if "mūlasahajāt" in k:                         # Xmūlasahajātā «cùng sinh với gốc rễ X»
        x = k.split("mūlasahajāt")[0]
        if x in X_ADJ:
            return ["cùng sinh với gốc rễ " + X_ADJ[x], "cùng sinh"]
        return None
    stem, end = _strip(k)
    for kind, xv, ev, av, bare in ROOT_KINDS:
        if not stem.endswith(kind):
            continue
        pre = stem[: -len(kind)]
        if pre == "":
            return [bare] if bare else None
        if pre == "eka":
            return [ev]
        if pre == "aññamañña":
            return [av]
        if pre in X_ADJ:
            v = xv + " " + X_ADJ[pre]
            if end == "ena":                       # Xmūlena (instrumental): «xét theo gốc rễ X»
                return ["xét theo " + v, v]
            return [v]
        return None
    return None


# ---------------------------------------------------------------------------- the hetuvāra series (2-10)
SERIES = {"het": "nguyên nhân", "nidān": "căn nguyên", "sambhav": "sự hình thành", "pabhav": "sự khởi nguồn",
          "samuṭṭhān": "nguồn gốc", "āhār": "dưỡng chất", "ārammaṇ": "đối tượng", "paccay": "điều kiện",
          "samuday": "sự phát sinh"}
_S_END = ("a", "ā", "u", "ū", "o", "aṃ", "uṃ", "ena", "unā", "e", "āni", "ānaṃ", "avo", "añca")


def series_value(kw):
    """Candidate values of X + series word (kusalahetū «nguyên nhân thiện», nāmārammaṇā «đối tượng thuộc phần tinh
    thần», kusalappabhavā «sự khởi nguồn thiện»); Xsamuṭṭhānaṃ (rūpaṃ) «do <X noun> sinh ra» first where the segment
    has it, else «nguồn gốc X». None if the keyword is not one."""
    k = lc(kw).lower()
    if len(k) > 3 and k.endswith("ti") and k[-3] in "āīū":
        k = k[:-2]
    for x in _X_ORDER:
        if k.startswith(x):
            rest = k[len(x):]
        elif k.startswith(x[:-1] + "ā"):           # sandhi: kusala + āhāra = kusalāhāra
            rest = k[len(x) - 1:]
        else:
            continue
        if len(rest) > 2 and rest[0] == rest[1]:   # kusala + pabhava = kusalappabhava
            rest = rest[1:]
        for s, v in SERIES.items():
            if rest.startswith(s) and rest[len(s):] in _S_END:
                if s == "samuṭṭhān":
                    return ["do " + X_NOUN[x] + " sinh ra", v + " " + X_ADJ[x]]
                return [v + " " + X_ADJ[x]]
        return None
    return None


def x_value(kw, kws):
    """kusala / akusala / abyākata / nāma alone (kusalā, kusalāti, kusalaṃ, kusalañca, nāmā …): the adjective
    («là thiện», «thuộc phần tinh thần»); the noun («Hiện tượng bất thiện mà không có gốc rễ …», «Phần tinh thần mà
    …») for the -aṃ form where the segment's first occurrence is the subject, i.e. in the Ahetukaṃ X-aṃ … segments
    (without Ahetukaṃ the first -aṃ is the predicate «na kusalaṃ» «không phải là thiện»). Candidates, best first."""
    k = lc(kw).lower()
    stem, end = _strip(k)
    if stem not in X_ADJ:
        return None
    s = set(lc(x).lower() for x in kws)
    if end == "aṃ" and not k.endswith(("ñca", "ñceva")) and "ahetukaṃ" in s:
        return [X_NOUN[stem], X_ADJ[stem]]
    return [X_ADJ[stem], X_NOUN[stem]]


# ---------------------------------------------------------------------------- the recurring Yamaka frame words
# Values as build_sample_vi.py / vi-zeroshot-terms.md / zeroshot-coordinator-rules.md write the formulas (the
# translation file is the truth; later agents check each value against their segment).
FORMULAS = {
    # ---- book frame (pi-1 CORE)
    "abhidhammapiṭake": CORE["abhidhammapiṭake"], "abhidhamma": CORE["abhidhamma"],
    "namo": CORE["namo"], "bhagavato": CORE["bhagavato"], "arahato": CORE["arahato"],
    "sambuddhassa": CORE["sambuddhassa"], "sammāsambuddhassa": CORE["sammāsambuddhassa"],
    "yamakapāḷi": "Các cặp câu hỏi",               # book title kept whole (as Kathāvatthu «Các vấn đề tranh luận»)
    "yamakapakaraṇaṃ": "Các cặp câu hỏi",          # Bộ “Các cặp câu hỏi” đã hoàn tất (proposal)
    "yamaka": "cặp câu hỏi",                       # member of <X>yamakaṃ / <X>yamakapāḷi
    "pāḷi": NDE,                                   # pi-2 … pi-5
    "niṭṭhito": "đã hoàn tất", "niṭṭhitā": "đã hoàn tất", "niṭṭhitaṃ": "đã hoàn tất",
    # ---- the pair questions (Ka) ye keci X dhammā, sabbe te Y? / (Kha) ye vā pana Y, sabbe te dhammā X?
    # «(a) Bất cứ hiện tượng nào X, có phải tất cả chúng đều Y không? (b) Còn bất cứ gì Y, có phải tất cả các hiện
    # tượng ấy đều X không?» (-ti / the question frame «có phải … không» has no keyword; «đều» = the frame)
    "ye keci": "bất cứ" + GAP + "nào",
    "keci": "nào",                                 # member of ye keci (context6: ye = «bất cứ» beside keci)
    "ye": "bất cứ" + GAP + "nào",                  # pi-1 / pi-2
    "ye vā pana": "còn bất cứ gì",
    "vā pana": "còn",
    "sabbe te": "tất cả chúng",                    # (Ka); «tất cả các hiện tượng ấy» = sabbe te dhammā (Kha)
    "sabbe te dhammā": "tất cả các hiện tượng ấy",
    "sabbe": "tất cả",
    "te": "chúng",                                 # (Ka) «tất cả chúng»; context6: «ấy» where only (Kha)
    # ---- answers
    "āmantā": "Đúng vậy",                          # pi-5
    "no": "không",                                 # No. «Không.» (7-01) / no ca «nhưng … không»
    "na": "không",                                 # pi-1; «không phải là» is the copula frame
    "natthi": "không có",                          # Natthi. «Không có.» (pi-3, 7-01)
    "tīṇeva": "chỉ có ba", "naveva": "chỉ có chín",   # «Chỉ có ba gốc rễ thiện.» (inner «có» kept)
    "tayo eva": "chỉ có ba",                       # Tayo eva kusalahetū «Chỉ có ba nguyên nhân thiện»
    "tayo": "ba", "tīṇi": "ba", "nava": "chín",
    "eva": "chỉ",                                  # Tayo eva kusalahetū «Chỉ có ba nguyên nhân thiện»
    "avasesā": "còn lại",                          # pi-1 … pi-4
    "ceva": "vừa",                                 # A ceva B ca «vừa A vừa B» (pi-2 X ceva X-sampayutto)
    "ekato": "cùng",                               # Mūlāni yāni ekato uppajjanti «Những gốc rễ nào cùng sinh khởi»
    "uppajjanti": "sinh khởi",                     # pi-1
    "sahajātā": "cùng sinh", "sahajāta": "cùng sinh", "sahajātaṃ": "cùng sinh",   # pi-2 / pi-5
    "ahetukaṃ": "không có gốc rễ", "ahetukā": "không có gốc rễ", "ahetuko": "không có gốc rễ",   # pi-1 / pi-2
    "sahetukaṃ": "có gốc rễ", "sahetukā": "có gốc rễ", "sahetuko": "có gốc rễ",   # «có» = having, kept (pi-1)
    "samuṭṭhāna": "do" + GAP + "sinh ra", "samuṭṭhānaṃ": "do" + GAP + "sinh ra",   # pi-1 MATRIX; context6: series
    "rūpaṃ": "vật chất",                           # Xsamuṭṭhānaṃ rūpaṃ «Vật chất do X sinh ra» (pi-1)
    "nāma": "phần tinh thần",                      # bare stem (pi-1 / pi-2); X_ADJ / X_NOUN for the slot
                                                   # (dhammā alone: the pi-5 context5 rule «hiện tượng» / …)
    # ---- section headings of chapter 1 (vi-zeroshot-terms.md)
    "uddeso": "phần nêu đề mục",                   # (Ka) uddeso «(a) Phần nêu đề mục» (pi-3 / pi-4)
    "niddeso": "phần giải thích",                  # (Kha) niddeso «(b) Phần giải thích» (pi-4 heading)
    "uddesavāro": "mục nêu đề mục",                # Uddesavāro niṭṭhito. «Mục nêu đề mục đã hoàn tất.»
    "niddesavāro": "mục giải thích",
    "vāro": "mục", "vāra": "mục",                  # pi-1 «Mục về …»
    "nayo": "phương pháp", "naya": "phương pháp",  # pi-3
    "mūlavāro": "mục về gốc rễ",
    "mūlavārauddeso": "phần nêu đề mục của mục về gốc rễ",
    "mūlavāraniddeso": "phần giải thích của mục về gốc rễ",
    "mūlanayo": "phương pháp về gốc rễ",
    "mūlamūlanayo": "phương pháp về cội rễ",
    "mūlakanayo": "phương pháp về sự bắt nguồn từ gốc rễ",
    "mūlamūlakanayo": "phương pháp về sự bắt nguồn từ cội rễ",
    "hetuvārādi": "mục về nguyên nhân và các mục khác",   # inner «các» kept (pi-3 ādi «mục khác»)
    "hetuvāro": "mục về nguyên nhân",
    "ādi": "mục khác",
    # ---- the ten yamaka titles (vi-zeroshot-terms.md; kept whole, with «Các»)
    "mūlayamakaṃ": "Các cặp câu hỏi về gốc rễ",
    "khandhayamakaṃ": "Các cặp câu hỏi về các khối",
    "āyatanayamakaṃ": "Các cặp câu hỏi về các lĩnh vực nhận biết",
    "dhātuyamakaṃ": "Các cặp câu hỏi về các yếu tố",
    "saccayamakaṃ": "Các cặp câu hỏi về các sự thật",
    "saṅkhārayamakaṃ": "Các cặp câu hỏi về các tạo tác",
    "anusayayamakaṃ": "Các cặp câu hỏi về các khuynh hướng tiềm ẩn",
    "cittayamakaṃ": "Các cặp câu hỏi về tâm",
    "dhammayamakaṃ": "Các cặp câu hỏi về các hiện tượng",
    "indriyayamakaṃ": "Các cặp câu hỏi về các năng lực",
    # <X>yamakapāḷi niṭṭhitā «Phần các cặp câu hỏi về <X> đã hoàn tất» (lower case as the text writes it)
    "mūlayamakapāḷi": "các cặp câu hỏi về gốc rễ",
    # ---- recurring section headings of the later chapters (approved list, zeroshot-coordinator-rules.md)
    # proposals: each later agent checks the value against its segment
    "paṇṇattivāro": "mục về sự định danh", "paṇṇattivāraniddesa": "phần giải thích của mục về sự định danh",
    "paṇṇatti": "sự định danh",
    "padasodhanavāro": "mục về sự làm sáng tỏ thuật ngữ",
    "padasodhanamūlacakkavāro": "mục về vòng luân chuyển dựa trên sự làm sáng tỏ thuật ngữ",
    "suddhakhandhavāro": "mục về các khối thuần túy",
    "suddhakhandhamūlacakkavāro": "mục về vòng luân chuyển dựa trên các khối thuần túy",
    "suddhindriyamūlacakkavāro": "mục về vòng luân chuyển dựa trên các năng lực thuần túy",
    "anulomaṃ": "chiều thuận", "paccanīkaṃ": "chiều nghịch", "paṭilomaṃ": "chiều ngược",   # pi-5 / 7-01
    "pavattivāro": "mục về sự diễn tiến", "pavatti": "sự diễn tiến",
    "uppādavāro": "mục về sự sinh khởi", "nirodhavāro": "mục về sự chấm dứt",
    "uppādanirodhavāro": "mục về sự sinh khởi và sự chấm dứt",
    "pariññāvāro": "mục về sự hiểu biết trọn vẹn",
    "paccuppannavāro": "mục về hiện tại", "atītavāro": "mục về quá khứ", "anāgatavāro": "mục về tương lai",
    "paccuppannātītavāro": "mục về hiện tại và quá khứ", "paccuppannānāgatavāro": "mục về hiện tại và tương lai",
    "atītānāgatavāro": "mục về quá khứ và tương lai",
    "anulomapuggalo": "chiều thuận theo người", "anulomaokāso": "chiều thuận theo nơi chốn",
    "anulomapuggalokāsā": "chiều thuận theo người và nơi chốn",
    "paccanīkapuggalo": "chiều nghịch theo người", "paccanīkaokāso": "chiều nghịch theo nơi chốn",
    "paccanīkapuggalokāsā": "chiều nghịch theo người và nơi chốn",
    "uppattiṭṭhānavāro": "mục về nơi sinh khởi", "mahāvāro": "mục lớn",
    "anusayavāro": "mục về khuynh hướng tiềm ẩn", "sānusayavāro": "mục về sự có khuynh hướng tiềm ẩn",
    "pajahanavāro": "mục về sự dứt bỏ", "pahīnavāro": "mục về những gì đã được dứt bỏ",
    "dhātuvisajjanāvāro": "mục trả lời theo các yếu tố",
    # ---- person / place relatives (families B / C; proposals, see vi-map-conventions-pi6.md)
    # «Ở người nào mà A …, thì ở người ấy có phải B … không?»: the case word «ở» is frame for the pronouns (as pi-3
    # «đối với»), kept for the place adverbs (as pi-1 Tattha «ở đây», pi-5 Sabbattha «ở mọi nơi»)
    "yassa": "người nào", "tassa": "người ấy", "yassa vā pana": "còn" + GAP + "người nào",
    "tesaṃ": "người ấy",                           # «ở những người ấy» (leading «những» dropped, pi-4)
    "yattha": "ở nơi nào", "tattha": "ở nơi ấy",   # context6: pi-1 «ở đây» where the segment has no «ở nơi ấy»
    "yo": "người nào", "so": "người ấy", "yato": "đối với nơi nào", "tato": "đối với nơi ấy",
    "sabbattha": "ở mọi nơi",                      # pi-5
    # ---- verbs and their tense / aspect forms (2-01, 7-01, 8; proposals)
    "uppajjati": "sinh khởi", "uppajjittha": "đã sinh khởi", "uppajjissati": "sẽ sinh khởi",
    "nuppajjati": "không sinh khởi", "nuppajjittha": "chưa từng sinh khởi", "nuppajjissati": "sẽ không sinh khởi",
    "nirujjhati": "chấm dứt", "nirujjhittha": "đã chấm dứt", "nirujjhissati": "sẽ chấm dứt",
    "uppajjamānaṃ": "đang sinh khởi", "uppajjamānānaṃ": "đang sinh khởi",
    "nirujjhamānaṃ": "đang chấm dứt", "nirujjhamānānaṃ": "đang chấm dứt",
    "anuseti": "nằm sẵn", "anusenti": "nằm sẵn", "nānuseti": "không nằm sẵn", "nānusenti": "không nằm sẵn",
    "pajahati": "dứt bỏ", "nappajahati": "không dứt bỏ",
    "parijānāti": "hiểu biết trọn vẹn", "pahīno": "đã được dứt bỏ", "pahīnā": "đã được dứt bỏ",
    "appahīno": "chưa được dứt bỏ", "appahīnā": "chưa được dứt bỏ",
    "upapajjantānaṃ": "đang tái sinh", "cavantānaṃ": "đang chết đi", "parinibbantānaṃ": "đang nhập Niết-bàn trọn vẹn",
    # ---- beings and planes (2-01, 7-01; proposals; the locative «Ở» / «Trong» of the answer is frame)
    "asaññasattānaṃ": "chúng sinh Vô Tưởng", "asaññasatta": "cõi Vô Tưởng",
    "suddhāvāsa": "cõi Tịnh Cư", "suddhāvāsānaṃ": "cõi Tịnh Cư",
    "kāmadhātuyā": "cõi dục lạc", "rūpadhātuyā": "cõi hình sắc", "arūpadhātuyā": "cõi không hình sắc",
    "pañcavokāre": "cõi gồm năm khối", "catuvokāre": "cõi gồm bốn khối", "ekavokāre": "cõi gồm một khối",
    "pacchimabhavikānaṃ": "người thuộc kiếp sống cuối cùng",
    "puthujjanassa": "người phàm phu", "puthujjano": "người phàm phu",
    "anāgāmissa": "bậc không trở lại", "anāgāmī": "bậc không trở lại", "arahā": "bậc A-la-hán",
    "aggamaggasamaṅgī": "người có được con đường tối thượng", "aṭṭhamako": "người thứ tám",
}

# ---------------------------------------------------------------------------- pi-6 terms (sample)
YM = {
    # the hetuvāra verse «Gốc rễ, nguyên nhân và căn nguyên, sự hình thành cùng với sự khởi nguồn; Nguồn gốc, dưỡng
    # chất, đối tượng, điều kiện cùng với sự phát sinh.» («và», «cùng với» = ca / the instrumental: frame)
    "mūlaṃ": "gốc rễ", "nidānañca": "căn nguyên", "sambhavo": "sự hình thành", "pabhavena": "sự khởi nguồn",
    "samuṭṭhānāhārārammaṇā": "nguồn gốc dưỡng chất đối tượng",   # comma dropped (pi-1)
    "samudayena": "sự phát sinh",
    "mūlāni": "gốc rễ",                            # Mūlāni yāni … «Những gốc rễ nào …» («Những» dropped)
}

_VERSE = {"nidānañca", "sambhavo", "pabhavena", "paccayo", "samudayena", "samuṭṭhānāhārārammaṇā"}
_SERIES_BARE = {"hetu": "nguyên nhân", "paccayo": "điều kiện"}
_DHAMMA = ("dhammā", "dhammo", "dhammaṃ", "dhamme", "dhammānaṃ")


def context6(kw, k, kws, text):
    """Segment rules of the pi-6 frame (k: lower-cased first letter). None = no rule."""
    s = set(lc(x).lower() for x in kws)
    kl = k.lower()
    if kl in YM or kl in FORMULAS and " " not in kl and kl not in ("te", "ye", "tattha", "nuppajjati",
                                                                  "samuṭṭhāna", "samuṭṭhānaṃ", "rūpaṃ"):
        return None                                # fixed values: FORMULAS / YM
    if kl in _SERIES_BARE and s & _VERSE:          # the hetuvāra verse: hetu «nguyên nhân», paccayo «điều kiện»
        return _SERIES_BARE[kl]
    words = kl.split()
    if len(words) == 2 and words[1] in _DHAMMA:    # «X dhammā»: (Ka) «Bất cứ hiện tượng nào (là) X» = «hiện tượng … X»
        a = _single(kws, text, None)(words[0])     # (the segment's first occurrence); headings «Các hiện tượng X» /
        if a and a != NDE:                         # «Hiện tượng X thì …» = «hiện tượng X»
            if present("hiện tượng nào " + a, text) or present("hiện tượng nào là " + a, text):
                return "hiện tượng" + GAP + a
            if present_strict("hiện tượng " + a, text):
                return "hiện tượng " + a
            if present("hiện tượng" + GAP + a, text):
                return "hiện tượng" + GAP + a
        return None
    if " " in kl:
        return None
    for fn in (root_value, series_value):
        c = fn(kw)
        if c:
            v = pick(text, *c)
            if v:
                return v
    c = x_value(kw, kws)
    if c:
        v = pick(text, *c)
        if v:
            return v
    if kl == "ye":                                 # ye keci «bất cứ … nào» (ye beside keci = «bất cứ»)
        if "keci" in s:
            return "bất cứ"
        return pick(text, "bất cứ" + GAP + "nào", "bất cứ gì")
    if kl == "te":                                 # (Ka) «tất cả chúng» / (Kha) «tất cả các hiện tượng ấy»
        return pick(text, "chúng", "ấy")
    if kl == "tattha":                             # Yamaka «ở nơi ấy» / pi-1 definitions «ở đây»
        return pick(text, "ở nơi ấy", "ở đây")
    if kl == "nuppajjati":                         # «không sinh khởi» / after no ca «vẫn sinh khởi» (2-01)
        return pick(text, "không sinh khởi", "vẫn sinh khởi")
    if kl in ("samuṭṭhāna", "samuṭṭhānaṃ"):        # pi-1 «do … sinh ra» / hetuvāra series «nguồn gốc»
        return pick(text, "do" + GAP + "sinh ra", "nguồn gốc")
    if kl == "rūpaṃ":                              # matter «vật chất» (pi-2) / visible object «hình sắc» (pi-1)
        return pick(text, "vật chất", "hình sắc")
    return None


def _single(kws, text, table):
    def single(w):
        k = lc(w)
        if table and k in table:
            return table[k]
        v = context6(w, k, kws, text)
        if v is not None:
            return v
        if k.lower() in FORMULAS:
            return FORMULAS[k.lower()]
        if k.lower() in YM:
            return YM[k.lower()]
        try:
            return pi5_value(w, kws, text)
        except KeyError:
            return None
    return single


def value6(kw, kws, table=None, text=None):
    """table -> context6 -> FORMULAS -> YM -> two-word composition -> the pi-5 chain."""
    k = lc(kw)
    t = text or ""
    if table and k in table:
        return table[k]
    v = context6(kw, k, kws, t)
    if v is not None:
        return v
    if k.lower() in FORMULAS:
        return FORMULAS[k.lower()]
    if k.lower() in YM:
        return YM[k.lower()]
    if " " in kw:
        v = compose(kw, kws, t, _single(kws, t, table))
        if v is not None:
            return v
    return pi5_value(kw, kws, t)


# part-specific values (everything recurring lives in FORMULAS / YM / the rules)
SAMPLE = {}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver_for(part):
    vi = read_vietnamese(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value6(kw, kws, SAMPLE, vi.get(bid, ""))
    return resolve


def dump(part, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        ps = []
        for i, f in ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values), (4, pi4_map_values),
                     (5, pi5_map_values)):
            p = [x for x, _ in f(kw).most_common(2) if x != v]
            if p:
                ps.append(f"pi{i}:{p}")
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + ("  " + " ".join(ps) if ps else "")
              + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(part, lo, hi, with_pali=False):
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            e = en(bid)
            out = []
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v} [{e.get(kw, '')}]{flag}")
            print("   " + " | ".join(out))


def look(kws):
    """the pi-1 … pi-5 map values of each keyword (exact keyword and lower-case first letter)."""
    for kw in kws:
        for k in dict.fromkeys((kw, lc(kw), kw[:1].upper() + kw[1:])):
            out = [f"pi{i}:{dict(f(k).most_common(4))}" for i, f in
                   ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values), (4, pi4_map_values),
                    (5, pi5_map_values)) if f(k)]
            if out:
                print(k, " ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], sys.argv[3:4] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), "pi" in sys.argv[5:])
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p, ALLOWED)
