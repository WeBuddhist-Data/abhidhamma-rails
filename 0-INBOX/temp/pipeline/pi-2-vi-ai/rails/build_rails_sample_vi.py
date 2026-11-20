"""Builder for the Vietnamese rails SAMPLE of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/preamble.md
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/sample-1/1-sample.md   (chapter 1 up to ##### Vedanākkhandho ^2-1-2-2-0)
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/vi-rails-formulas.md

All Vietnamese comes from the fixed strings below, so identical Pāli gives byte-identical Vietnamese.
Terms: locked termbase AI_translation/vietnamese/pi-2-pali-vietnamese-termbase-plain.md
(+ pi-2-vi-ai/termbase/APPROVED.md, pi-1-vi-ai/termbase/APPROVED.md). Where the Pāli repeats the
Dhammasaṅgaṇī, the approved pi-1 Vietnamese rails wording is reused (marked PI1 below).
Translated fresh from the Pāli. Later chapter builders may import the constants and functions;
importing writes nothing.

usage: python -I -X utf8 build_rails_sample_vi.py
"""
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"
OUT = ROOT / "AI_translation" / "vietnamese" / "pi-2-vietnamese-plain-rails_split_chapters"
PIPE = ROOT / "0-INBOX" / "temp" / "pipeline"
WORK = PIPE / "pi-2-vi-ai"
RAILS = WORK / "rails"
PALI_SAMPLE = WORK / "ch1-sample-pali.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def cap(s):
    return s[0].upper() + s[1:]


def spell(sig, word):
    """Spelling-only variant: [vi (sī. syā.)] -> [khác chính tả (Sī., Syā.): vi]."""
    return f"[khác chính tả ({sig}): {word}]"


def reading(sig, word):
    """Variant with a different word or wording."""
    return f"[dị bản ({sig}): {word}]"


LAB = ["(a)", "(b)", "(c)"]          # (Ka) (Kha) (Ga)

# ================================================================== book frame (user-approved 2026-11-18)
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"      # PI1
H_PITAKA = "Tạng Vi Diệu Pháp"                                               # PI1  Abhidhammapiṭake
H_BOOK = "Phân tích các hiện tượng"                                          # Vibhaṅgapāḷi
CH_HEADINGS = {   # ### level
    "Khandhavibhaṅgo": "Phân tích các khối",
    "Āyatanavibhaṅgo": "Phân tích các lĩnh vực nhận biết",
    "Dhātuvibhaṅgo": "Phân tích các yếu tố",
    "Saccavibhaṅgo": "Phân tích các sự thật",
    "Indriyavibhaṅgo": "Phân tích các năng lực",
    "Paṭiccasamuppādavibhaṅgo": "Phân tích sự sinh khởi tùy thuộc vào điều kiện",
    "Satipaṭṭhānavibhaṅgo": "Phân tích sự thiết lập tỉnh thức",
    "Sammappadhānavibhaṅgo": "Phân tích các nỗ lực đúng đắn",
    "Iddhipādavibhaṅgo": "Phân tích các nền tảng thần thông",
    "Bojjhaṅgavibhaṅgo": "Phân tích các chi phần giác ngộ",
    "Maggaṅgavibhaṅgo": "Phân tích các chi phần của con đường",
    "Jhānavibhaṅgo": "Phân tích các tầng thiền",
    "Appamaññāvibhaṅgo": "Phân tích các trạng thái không thể đo lường",
    "Sikkhāpadavibhaṅgo": "Phân tích các điều tu học",
    "Paṭisambhidāvibhaṅgo": "Phân tích các loại hiểu biết thông suốt",
    "Ñāṇavibhaṅgo": "Phân tích các loại hiểu biết",
    "Khuddakavatthuvibhaṅgo": "Phân tích các chủ đề nhỏ",
    "Dhammahadayavibhaṅgo": "Phân tích cốt lõi của các hiện tượng",
}
SEC_HEADINGS = {  # #### level; the closing line repeats the heading with «.»
    "Suttantabhājanīyaṃ": "Phân tích theo kinh",
    "Abhidhammabhājanīyaṃ": "Phân tích theo Vi Diệu Pháp",
    "Pañhāpucchakaṃ": "Phần hỏi đáp",
}
RUPAKANDA = "Phần về vật chất"                                               # PI1  Rūpakaṇḍaṃ (mid-sentence in “…”)

# N-vidhena = «theo nhóm N» (no «phân loại»)
NUM = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín",
       10: "mười", 11: "mười một"}
VIDHA = {1: "Ekavidhena", 2: "Duvidhena", 3: "Tividhena", 4: "Catubbidhena", 5: "Pañcavidhena",
         6: "Chabbidhena", 7: "Sattavidhena", 8: "Aṭṭhavidhena", 9: "Navavidhena", 10: "Dasavidhena",
         11: "Ekādasavidhena"}


def by_n(n):
    return f"theo nhóm {NUM[n]}"


# ================================================================== the five aggregates
# key: (pali khandha, Vietnamese khandha, unit after «Bất cứ … nào», noun in questions/answers,
#       unit for «từng loại …», closing pronoun ayaṃ/idaṃ vs ime)
TATTHA = "Ở đây,"                                   # PI1  Tattha (opening a question)
IS_WHAT = "là gì?"                                  # PI1  katamo/katamā/katamaṃ … ?
CALLED_SG = "đó được gọi là"                        # PI1  ayaṃ/idaṃ vuccati
CALLED_PL = "những điều này được gọi là"            # ime vuccanti
AGG = {
    "rupa": dict(p="rūpakkhandho", k="khối vật chất", unit="vật chất", n="vật chất", n_pl="vật chất",
                 called=CALLED_SG),
    "vedana": dict(p="vedanākkhandho", k="khối cảm giác", unit="cảm giác", n="cảm giác", n_pl="cảm giác",
                   called=CALLED_SG),
    "sanna": dict(p="saññākkhandho", k="khối tri giác", unit="tri giác", n="tri giác", n_pl="tri giác",
                  called=CALLED_SG),
    "sankhara": dict(p="saṅkhārakkhandho", k="khối tạo tác", unit="sự tạo tác", n="các sự tạo tác",
                     n_pl="các sự tạo tác", called=CALLED_PL),
    "vinnana": dict(p="viññāṇakkhandho", k="khối thức", unit="thức", n="thức", n_pl="các loại thức",
                    called=CALLED_SG),
}
FIVE = ["rupa", "vedana", "sanna", "sankhara", "vinnana"]
# Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.
FIVE_LIST = "Năm khối – " + ", ".join(AGG[a]["k"] for a in FIVE) + "."

# the attributes
ATT = dict(
    atita="thuộc quá khứ", anagata="thuộc tương lai", paccuppanna="thuộc hiện tại",   # PI1
    ajjhatta="ở nơi bản thân", bahiddha="ở bên ngoài bản thân",                      # PI1
    olarika="ở dạng thô", sukhuma="ở dạng vi tế",                                      # PI1
    hina="thấp kém", panita="ưu việt",                                                # PI1
    dure="ở xa", santike="ở gần",                                                     # PI1
)


def khandha_def(a):
    """Tattha katamo X-kkhandho? Yaṃ kiñci X atītānāgatapaccuppannaṃ … tadekajjhaṃ abhisaññūhitvā
    abhisaṅkhipitvā – ayaṃ vuccati X-kkhandho."""
    g = AGG[a]
    return (f"{TATTHA} {g['k']} {IS_WHAT} Bất cứ {g['unit']} nào, dù thuộc quá khứ, thuộc tương lai hay "
            f"thuộc hiện tại, ở nơi bản thân hay ở bên ngoài bản thân, ở dạng thô hay ở dạng vi tế, "
            f"thấp kém hay ưu việt, ở xa hay ở gần, gom tất cả lại làm một và thu tóm lại – "
            f"{CALLED_SG} {g['k']}.")


def question(a, att):
    """Tattha katamaṃ X atītaṃ?  ->  «Ở đây, X thuộc quá khứ là gì?»"""
    return f"{TATTHA} {AGG[a]['n']} {ATT[att]} {IS_WHAT}"


def closing(a, att, dash=True):
    """– idaṃ/ayaṃ vuccati X atītaṃ.  /  – ime vuccanti saṅkhārā atītā."""
    g = AGG[a]
    s = f"{g['called']} {g['n']} {ATT[att]}."
    return f"– {s}" if dash else cap(s)


# ---- past / future / present (PI1: ^1-1044, ^1-1045, ^1-1046)
PAST_S = ("đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn, "
          "đã mất đi sau khi sinh khởi")
# atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ uppajjitvā vigataṃ atītaṃ atītaṃsena saṅgahitaṃ
FUT_S = ("chưa sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra, "
         "chưa sinh khởi, chưa sinh khởi trọn vẹn, chưa trỗi dậy, chưa trỗi dậy trọn vẹn")
# ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ anuppannaṃ asamuppannaṃ anuṭṭhitaṃ asamuṭṭhitaṃ
PRES_S = ("đã sinh ra, đã trở thành, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra, "
          "đã sinh khởi, đã sinh khởi trọn vẹn, đã trỗi dậy, đã trỗi dậy trọn vẹn")
# jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ uppannaṃ samuppannaṃ uṭṭhitaṃ samuṭṭhitaṃ
TIME_BODY = {
    "atita": f"thuộc quá khứ, {PAST_S}, thuộc quá khứ, được gộp vào phần thuộc quá khứ",
    "anagata": f"{FUT_S}, thuộc tương lai, được gộp vào phần thuộc tương lai",
    "paccuppanna": f"{PRES_S}, thuộc hiện tại, được gộp vào phần thuộc hiện tại",
}
# ---- internal / external (PI1: ^1-1050, ^1-1051)
INT_BODY = "của từng chúng sinh, ở nơi bản thân, riêng từng người, cố hữu, thuộc về cá nhân, do nghiệp tạo ra"
# tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ
EXT_BODY = ("của từng chúng sinh khác, từng người khác, ở nơi bản thân của họ, riêng từng người, cố hữu, "
            "thuộc về cá nhân, do nghiệp tạo ra")
# tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ

# ---- the member lists after the comma
RUPA_LIST = "bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản"   # PI1 (^1-584)
# cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāyarūpaṃ
DOORS = ["mắt", "tai", "mũi", "lưỡi", "thân", "ý"]
LISTS = {
    "rupa": RUPA_LIST,
    "vedana": "cảm giác dễ chịu, cảm giác khó chịu, cảm giác không khó chịu cũng không dễ chịu",
    "sanna": ", ".join(f"tri giác sinh từ sự tiếp xúc của {d}" for d in DOORS),
    "sankhara": ", ".join(f"chủ ý sinh từ sự tiếp xúc của {d}" for d in DOORS),
    "vinnana": "thức qua mắt, thức qua tai, thức qua mũi, thức qua lưỡi, thức qua thân, ý thức",
}


def time_line(a, att):
    """Tattha katamaṃ X atītaṃ? Yaṃ X atītaṃ … saṅgahitaṃ, LIST – idaṃ vuccati X atītaṃ."""
    return f"{question(a, att)} {cap(AGG[a]['n'])} {TIME_BODY[att]}: {LISTS[a]} {closing(a, att)}"


def self_line(a, att):
    """Tattha katamaṃ X ajjhattaṃ/bahiddhā? Yaṃ X tesaṃ tesaṃ … upādinnaṃ, LIST – idaṃ vuccati …"""
    body = INT_BODY if att == "ajjhatta" else EXT_BODY
    return f"{question(a, att)} {cap(AGG[a]['n'])} {body}: {LISTS[a]} {closing(a, att)}"


def relative(a, pair):
    """Taṃ taṃ vā pana X upādāyupādāya X oḷārikaṃ sukhumaṃ daṭṭhabbaṃ."""
    x, y = pair
    g = AGG[a]
    return (f"Hoặc, khi so với từng loại {g['unit']} tương ứng, {g['n']} nên được xem là "
            f"{ATT[x]} hay {ATT[y]}.")


# ================================================================== matter only (^2-5 … ^2-7)
GROSS_RANGE = "Lĩnh vực mắt… lĩnh vực vật xúc chạm"                  # PI1 (^1-674) Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ
FOOD = "thức ăn trong vai trò dưỡng chất"                              # PI1 kabaḷīkāro āhāro
SUBTLE_RANGE = f"Năng lực nữ tính… {FOOD}"                            # PI1 (^1-675) Itthindriyaṃ…pe… kabaḷīkāro āhāro
SUBTLE_RANGE_VAR = f"Năng lực nữ tính… {FOOD} {spell('Sī., Syā.', 'kabaḷiṃkāro')}"   # ^2-5 only
# uññātaṃ avaññātaṃ hīḷitaṃ paribhūtaṃ acittīkataṃ hīnaṃ hīnamataṃ hīnasammataṃ aniṭṭhaṃ akantaṃ amanāpaṃ
HINA_BODY = ("mà đối với từng chúng sinh thì bị coi thường, bị xem nhẹ, bị chê bai, bị khinh miệt, "
             "không được quý trọng, thấp kém, được xem là thấp kém, được công nhận là thấp kém, "
             "không đáng mong muốn, không đáng yêu mến, không đáng ưa thích")
# anuññātaṃ anavaññātaṃ ahīḷitaṃ aparibhūtaṃ cittīkataṃ paṇītaṃ paṇītamataṃ paṇītasammataṃ iṭṭhaṃ kantaṃ manāpaṃ
PANITA_BODY = ("mà đối với từng chúng sinh thì không bị coi thường, không bị xem nhẹ, không bị chê bai, "
               "không bị khinh miệt, được quý trọng, ưu việt, được xem là ưu việt, được công nhận là ưu việt, "
               "đáng mong muốn, đáng yêu mến, đáng ưa thích")
OBJECTS5 = "hình sắc, âm thanh, mùi, vị, vật xúc chạm"                # rūpā saddā gandhā rasā phoṭṭhabbā
# yaṃ vā panaññampi atthi rūpaṃ anāsanne anupakaṭṭhe dūre asantike
FAR_REST = "hoặc bất cứ vật chất nào khác không ở sát bên, không cận kề, ở xa, không ở gần"
# yaṃ vā panaññampi atthi rūpaṃ āsanne upakaṭṭhe avidūre santike
NEAR_REST = "hoặc bất cứ vật chất nào khác ở sát bên, cận kề, không ở xa, ở gần"


def rupa_range_line(att, rng, rest=""):
    """Tattha katamaṃ rūpaṃ oḷārikaṃ? Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ[, yaṃ vā pana…] – idaṃ vuccati …"""
    mid = f"{rng}, {rest}" if rest else rng
    return f"{question('rupa', att)} {mid} {closing('rupa', att)}"


def rupa_quality_line(att):
    """Tattha katamaṃ rūpaṃ hīnaṃ/paṇītaṃ? Yaṃ rūpaṃ tesaṃ tesaṃ sattānaṃ …, rūpā saddā … – idaṃ vuccati …"""
    body = HINA_BODY if att == "hina" else PANITA_BODY
    return f"{question('rupa', att)} Vật chất {body}: {OBJECTS5} {closing('rupa', att)}"


# ================================================================== the comparisons of the mental aggregates
# A phrase is named by a key; «N» is the aggregate noun (singular or plural form).
ETH = {
    "akusala": "bất thiện", "kusala": "thiện", "abyakata": "không xác định về mặt đạo đức",
    "kusalabyakata": "thiện và không xác định về mặt đạo đức",       # kusalābyākatā
    "kusalakusala": "thiện và bất thiện",                             # kusalākusalā
    "akusalabyakata": "bất thiện và không xác định về mặt đạo đức",   # akusalābyākatā
}
V_DUK = "cảm giác khó chịu"                                           # dukkhā vedanā
V_SUK = "cảm giác dễ chịu"                                            # sukhā vedanā
V_ADM = "cảm giác không khó chịu cũng không dễ chịu"                  # adukkhamasukhā vedanā
FEEL = {   # the feeling itself (vedanā) / what a perception etc. is conjoined with (… vedanāya sampayuttā)
    "dukkha": V_DUK, "sukha": V_SUK, "adm": V_ADM,
    "sukha_adm": f"{V_SUK} và {V_ADM}",                               # sukhā ca adukkhamasukhā ca
    "dukkha_adm": f"{V_DUK} và {V_ADM}",                              # dukkhā ca adukkhamasukhā ca
    "sukhadukkha": "cảm giác dễ chịu và khó chịu",                    # sukhadukkhā
}
OTHER = {
    "asam": "của người chưa chứng nhập",                              # asamāpannassa
    "sam": "của người đã chứng nhập",                                 # samāpannassa
    "sasava": "là đối tượng của ô nhiễm",                             # sāsavā
    "anasava": "không phải là đối tượng của ô nhiễm",                 # anāsavā
    "patigha": "sinh từ sự tiếp xúc có va chạm",                      # paṭighasamphassajā
    "adhivacana": "sinh từ sự tiếp xúc qua tên gọi",                  # adhivacanasamphassajā
}
CONJ = "gắn liền với"                                                 # sampayutta


def cp(a, key, pl=False):
    """The noun phrase for one comparison member, e.g. cp('sanna', 'dukkha') =
    «tri giác gắn liền với cảm giác khó chịu»."""
    n = AGG[a]["n_pl"] if pl else AGG[a]["n"]
    if key in ETH:
        return f"{n} {ETH[key]}"
    if key in FEEL:
        return FEEL[key] if a == "vedana" else f"{n} {CONJ} {FEEL[key]}"
    return f"{n} {OTHER[key]}"


def contrast(a, pairs, x, y):
    """Akusalā vedanā oḷārikā, kusalābyākatā vedanā sukhumā. …  pairs = [((key, pl), (key, pl)), …]"""
    return " ".join(f"{cap(cp(a, *p))} thì {ATT[x]}, {cp(a, *q)} thì {ATT[y]}." for p, q in pairs)


def relation(a, groups, att):
    """Akusalā vedanā kusalābyākatāhi vedanāhi dūre; … .  groups = list of sentences, each a list of
    ((key, pl), (key, pl)); returns the sentences joined, each ending in «.» except the last."""
    sents = ["; ".join(f"{cp(a, *p)} thì {ATT[att]} {cp(a, *q)}" for p, q in g) for g in groups]
    return ". ".join(cap(s) for s in sents)


def q_pair(a, x, y):
    """Tattha katamā vedanā oḷārikā sukhumā?  ->  «Ở đây, cảm giác ở dạng thô và ở dạng vi tế là gì?»"""
    return f"{TATTHA} {AGG[a]['n']} {ATT[x]} và {ATT[y]} {IS_WHAT}"


def S(*keys):
    """Shorthand: S('akusala', 'kusalabyakata+') -> [('akusala', False), ('kusalabyakata', True)]."""
    return [(k.rstrip("+"), k.endswith("+")) for k in keys]


def P(*pairs):
    out = []
    for x, y in pairs:
        out.append(tuple(S(x, y)))
    return out


# contrast pairs (gross/subtle and inferior/superior), «+» = plural noun (viññāṇā)
CONTRAST = {
    "vedana": P(("akusala", "kusalabyakata"), ("kusalakusala", "abyakata"), ("dukkha", "sukha_adm"),
                ("sukhadukkha", "adm"), ("asam", "sam"), ("sasava", "anasava")),
    "vinnana": P(("akusala", "kusalabyakata+"), ("kusalakusala+", "abyakata"), ("dukkha", "sukha_adm+"),
                 ("sukhadukkha+", "adm"), ("asam", "sam"), ("sasava", "anasava")),
}
CONTRAST["sanna"] = CONTRAST["vedana"]
CONTRAST["sankhara"] = CONTRAST["vedana"]
CONTRAST_GROSS_EXTRA = {"sanna": P(("patigha", "adhivacana"))}   # ^2-17 opens with the contact pair


def _far(pl):
    """The far relations in their four sentences; pl = which members are plural (viññāṇa)."""
    a = "+" if pl else ""
    return [P(("akusala", "kusalabyakata" + a), ("kusalabyakata" + a, "akusala"),
              ("kusala", "akusalabyakata" + a), ("akusalabyakata" + a, "kusala"),
              ("abyakata", "kusalakusala" + a), ("kusalakusala" + a, "abyakata")),
            P(("dukkha", "sukha_adm" + a), ("sukha_adm" + a, "dukkha"), ("sukha", "dukkha_adm" + a),
              ("dukkha_adm" + a, "sukha"), ("adm", "sukhadukkha" + a), ("sukhadukkha" + a, "adm")),
            P(("asam", "sam"), ("sam", "asam")),
            P(("sasava", "anasava"), ("anasava", "sasava"))]


FAR = {"vedana": _far(False), "sankhara": _far(False), "vinnana": _far(True)}
_f = _far(False)
FAR["sanna"] = [_f[0][:4], _f[0][4:]] + _f[1:]                   # ^2-19 puts a full stop after the fourth
NEAR = [P(("akusala", "akusala"), ("kusala", "kusala"), ("abyakata", "abyakata")),
        P(("dukkha", "dukkha"), ("sukha", "sukha"), ("adm", "adm")),
        P(("asam", "asam"), ("sam", "sam")),
        P(("sasava", "sasava"), ("anasava", "anasava"))]


# ================================================================== Abhidhamma section: the matter lists
# ^2-33, from the pi-1 rūpakaṇḍa (^1-584 … ^1-593), with «khối vật chất theo nhóm N»
def vidha_open(n):
    """N-vidhena rūpakkhandho –  ->  «Khối vật chất theo nhóm N –»"""
    return f"Khối vật chất {by_n(n)} –"


def vidha_close(n):
    """Evaṃ N-vidhena rūpakkhandho.  ->  «Như vậy là khối vật chất theo nhóm N.»"""
    return f"Như vậy là khối vật chất {by_n(n)}."


EKAKA = [   # PI1 (^1-584): sabbaṃ rūpaṃ na hetu, ahetukaṃ, … jarābhibhūtaṃ
    "không phải là gốc rễ", "không có gốc rễ", "không gắn liền với gốc rễ", "có điều kiện",
    "do điều kiện tạo thành", "thuộc vật chất", "thuộc thế gian", "là đối tượng của ô nhiễm",
    "là đối tượng của xiềng xích", "là đối tượng của nút thắt", "là đối tượng của dòng lũ",
    "là đối tượng của ách", "là đối tượng của chướng ngại", "bị sự hiểu sai lệch nắm giữ",
    "là đối tượng của sự bám víu", "là đối tượng của phiền não", "không xác định về mặt đạo đức",
    "không có đối tượng", "không phải là yếu tố đồng hành với tâm", "không gắn liền với tâm",
    "không phải là quả của nghiệp cũng không có khả năng sinh ra quả",
    "không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não",
    "không thuộc loại có sự hướng tâm và sự duy trì tâm",
    "không thuộc loại không có sự hướng tâm, chỉ có sự duy trì tâm",
    "không có sự hướng tâm cũng không có sự duy trì tâm", "không có sự hân hoan đi kèm",
    "không có hạnh phúc đi kèm", "không có sự bình thản đi kèm",
    "không cần dứt bỏ bằng sự thấy chân lý cũng không cần dứt bỏ bằng sự tu tập",
    "không có gốc rễ nào cần dứt bỏ bằng sự thấy chân lý, cũng không có gốc rễ nào cần dứt bỏ bằng sự tu tập",
    "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ",
    "không thuộc về người còn đang tu học cũng không thuộc về người đã hoàn tất tu học",
    "hạn hẹp", "thuộc cõi dục lạc", "không thuộc cõi hình sắc", "không thuộc cõi không hình sắc",
    "nằm trong các cõi tồn tại", "không thuộc loại không nằm trong các cõi tồn tại", "không cố định",
    "không dẫn đến giải thoát", "khi đã sinh khởi thì có thể được sáu loại thức nhận biết", "là vô thường",
    "bị sự lão hóa chế ngự",
]
SABBA_RUPA = "toàn bộ vật chất"                                        # PI1 sabbaṃ rūpaṃ

# duka pairs, PI1 (^1-U1): Atthi rūpaṃ X, atthi rūpaṃ Y.  ->  «Có loại vật chất X, có loại vật chất Y.»
DUKA = [
    ("phái sinh", "không phải là phái sinh"), ("do nghiệp tạo ra", "không do nghiệp tạo ra"),
    ("do nghiệp tạo ra và là đối tượng của sự bám víu", "không do nghiệp tạo ra nhưng là đối tượng của sự bám víu"),
    ("thấy được", "không thấy được"), ("có tính va chạm", "không có tính va chạm"),
    ("là năng lực", "không phải là năng lực"), ("là yếu tố cơ bản", "không phải là yếu tố cơ bản"),
    ("là sự biểu lộ", "không phải là sự biểu lộ"), ("do tâm sinh ra", "không do tâm sinh ra"),
    ("cùng tồn tại với tâm", "không cùng tồn tại với tâm"), ("vận hành theo tâm", "không vận hành theo tâm"),
    ("thuộc phần bên trong", "thuộc phần bên ngoài"), ("ở dạng thô", "ở dạng vi tế"), ("ở xa", "ở gần"),
]
DUKA_FOOD = (f"là {FOOD}", f"không phải là {FOOD}")
KIND = "có loại vật chất"                                              # PI1 atthi rūpaṃ
SOME = "có loại"                                                       # PI1 atthi (after taṃ)


def duka_pair(x, y, var=""):
    return f"{KIND} {x}, {KIND} {y}{(' ' + var) if var else ''}"


def tika_pair(x, ys):
    """yaṃ taṃ rūpaṃ ajjhattikaṃ taṃ X, yaṃ taṃ rūpaṃ bāhiraṃ taṃ atthi Y1, atthi Y2 (PI1 ^1-585)."""
    return (f"vật chất nào thuộc phần bên trong thì {x}; vật chất nào thuộc phần bên ngoài thì "
            f"{SOME} {ys[0]}, {SOME} {ys[1]}")


def catukka_pair(x1, x2, ys):
    """yaṃ taṃ rūpaṃ X1 taṃ atthi Y1, atthi Y2; yaṃ taṃ rūpaṃ X2 taṃ atthi Y1, atthi Y2 (PI1 ^1-586)."""
    tail = f"{SOME} {ys[0]}, {SOME} {ys[1]}"
    return f"vật chất nào {x1} thì {tail}; vật chất nào {x2} thì {tail}"


SEEN = "vật chất được thấy, được nghe, được cảm nhận, được nhận biết"   # PI1 diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ
RUPAKANDA_NOTE = (f"(Như đã được phân tích trong “{RUPAKANDA}”, ở đây cũng nên phân tích như vậy.)")
# (Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.)

COGN = ["mắt", "tai", "mũi", "lưỡi", "thân"]


def cognisable(x):
    return f"vật chất mà {x} có thể nhận biết"                          # PI1 X-viññeyyaṃ rūpaṃ


FIVE_COGN = ", ".join(cognisable(x) for x in COGN)
MANODHATU_COGN = cognisable("yếu tố ý")                                 # PI1 manodhātuviññeyyaṃ rūpaṃ
MANOVINN_COGN = cognisable("yếu tố ý thức")                             # PI1 manoviññāṇadhātuviññeyyaṃ rūpaṃ
FACULTIES8 = ("năng lực mắt, năng lực tai, năng lực mũi, năng lực lưỡi, năng lực thân, năng lực nữ tính, "
              "năng lực nam tính, năng lực sống")                        # PI1
BASES10 = ("lĩnh vực mắt, lĩnh vực tai, lĩnh vực mũi, lĩnh vực lưỡi, lĩnh vực thân, lĩnh vực hình sắc, "
           "lĩnh vực âm thanh, lĩnh vực mùi, lĩnh vực vị, lĩnh vực vật xúc chạm")   # PI1
VIDHA_BODY = {   # n -> the list after the dash (lower-case start)
    5: "yếu tố đất, yếu tố nước, yếu tố lửa, yếu tố gió và loại vật chất phái sinh",            # PI1
    6: f"{FIVE_COGN}, {cognisable('ý')}",                                                        # PI1
    7: f"{FIVE_COGN}, {MANODHATU_COGN}, {MANOVINN_COGN}",                                        # PI1
    8: (f"{FIVE_COGN}: có loại khi tiếp xúc thì dễ chịu, có loại khi tiếp xúc thì khó chịu; "
        f"{MANODHATU_COGN}, {MANOVINN_COGN}"),                                                    # PI1
    9: f"{FACULTIES8} và loại vật chất không phải là năng lực",                                  # PI1
    10: f"{FACULTIES8}, vật chất không phải là năng lực: có loại có tính va chạm, có loại không có tính va chạm",  # PI1
    11: (f"{BASES10} và loại vật chất không thấy được và không có tính va chạm, "
         "nằm trong lĩnh vực đối tượng của ý"),                                                   # PI1
}
UPA_PAIR = ("do nghiệp tạo ra và là đối tượng của sự bám víu",
            "không do nghiệp tạo ra nhưng là đối tượng của sự bám víu")    # PI1 upādinnupādāniyaṃ / anupādinnupādāniyaṃ


def abhidhamma_rupa():
    """The 13 lines of ^2-33 (without the block id)."""
    L = []
    L.append(f"{TATTHA} {AGG['rupa']['k']} {IS_WHAT} {vidha_open(1)} {SABBA_RUPA} "
             + "; ".join(EKAKA) + f". {vidha_close(1)}")
    parts = [duka_pair(*DUKA[0], var=spell("Sī., Ka.", "nupādā"))] + [duka_pair(*d) for d in DUKA[1:]]
    L.append(f"{vidha_open(2)} {parts[0]}. " + ". ".join(cap(p) for p in parts[1:])
             + f"… {duka_pair(*DUKA_FOOD)}. {vidha_close(2)}")
    L.append(RUPAKANDA_NOTE)
    t = [tika_pair("là phái sinh", ("là phái sinh", "không phải là phái sinh")),
         tika_pair("do nghiệp tạo ra", DUKA[1]),
         tika_pair(UPA_PAIR[0], UPA_PAIR),
         tika_pair(f"không phải là {FOOD}", (f"là {FOOD}", f"không phải là {FOOD}"))]
    L.append(f"{vidha_open(3)} {t[0]}. {cap(t[1])}. {cap(t[2])}… {t[3]}. {vidha_close(3)}")
    up = ("là phái sinh", "không phải là phái sinh")
    c = [catukka_pair(*up, DUKA[1]), catukka_pair(*up, UPA_PAIR), catukka_pair(*up, DUKA[4]),
         catukka_pair(*up, DUKA[12]), catukka_pair(*up, DUKA[13])]
    L.append(f"{vidha_open(4)} {c[0]}. " + ". ".join(cap(x) for x in c[1:]) + f"… {SEEN}. {vidha_close(4)}")
    for n in range(5, 12):
        L.append(f"{vidha_open(n)} {VIDHA_BODY[n]}. {vidha_close(n)}")
    L.append(f"{cap(CALLED_SG)} {AGG['rupa']['k']}.")                 # Ayaṃ vuccati rūpakkhandho.
    return L


# ================================================================== assembly
def suttanta_rupa():
    """[(lines, id)] for ^2-2 … ^2-7."""
    a = "rupa"
    return [
        ([khandha_def(a)], "2-2"),
        ([time_line(a, t) for t in ("atita", "anagata", "paccuppanna")], "2-3"),
        ([self_line(a, t) for t in ("ajjhatta", "bahiddha")], "2-4"),
        ([rupa_range_line("olarika", GROSS_RANGE), rupa_range_line("sukhuma", SUBTLE_RANGE_VAR)], "2-5"),
        ([rupa_quality_line("hina"), rupa_quality_line("panita") + " " + relative(a, ("hina", "panita"))], "2-6"),
        ([rupa_range_line("dure", SUBTLE_RANGE, FAR_REST),
          rupa_range_line("santike", GROSS_RANGE, NEAR_REST) + " " + relative(a, ("dure", "santike"))], "2-7"),
    ]


def suttanta_mental(a, ids, last_extra=None):
    """[(lines, id)] for one mental aggregate; ids = the six block ids in order."""
    gross_pairs = CONTRAST_GROSS_EXTRA.get(a, []) + CONTRAST[a]
    gross = (f"{q_pair(a, 'olarika', 'sukhuma')} {contrast(a, gross_pairs, 'olarika', 'sukhuma')} "
             f"{relative(a, ('olarika', 'sukhuma'))}")
    low = (f"{q_pair(a, 'hina', 'panita')} {contrast(a, CONTRAST[a], 'hina', 'panita')} "
           f"{relative(a, ('hina', 'panita'))}")
    far_rel = relation(a, FAR[a], "dure")
    near_rel = relation(a, NEAR, "santike")
    if a == "sankhara":          # «… dūre. Ime vuccanti saṅkhārā dūre.»
        far = f"{question(a, 'dure')} {cap(far_rel)}. {closing(a, 'dure', dash=False)}"
    else:                        # «… dūre – ayaṃ/idaṃ vuccati … dūre.»
        far = f"{question(a, 'dure')} {cap(far_rel)} {closing(a, 'dure')}"
    if a == "vinnana":           # «… santike – idaṃ vuccati viññāṇaṃ santike. Taṃ taṃ …»
        near = f"{question(a, 'santike')} {cap(near_rel)} {closing(a, 'santike')} {relative(a, ('dure', 'santike'))}"
    else:                        # «… santike. Ayaṃ vuccati … santike. Taṃ taṃ …»
        near = (f"{question(a, 'santike')} {cap(near_rel)}. {closing(a, 'santike', dash=False)} "
                f"{relative(a, ('dure', 'santike'))}")
    fn = [far, near] + (last_extra or [])
    return [
        ([khandha_def(a)], ids[0]),
        ([time_line(a, t) for t in ("atita", "anagata", "paccuppanna")], ids[1]),
        ([self_line(a, t) for t in ("ajjhatta", "bahiddha")], ids[2]),
        ([gross], ids[3]),
        ([low], ids[4]),
        (fn, ids[5]),
    ]


def H(level, text, bid):
    return ([f"{'#' * level} {text}"], bid)


def sample_segments():
    segs = [H(3, CH_HEADINGS["Khandhavibhaṅgo"], "2-1-0"),
            H(4, SEC_HEADINGS["Suttantabhājanīyaṃ"], "2-1-1-0"),
            ([FIVE_LIST], "2-1"),
            H(5, cap(AGG["rupa"]["k"]), "2-1-1-1-0")]
    segs += suttanta_rupa()
    ids = {"vedana": 8, "sanna": 14, "sankhara": 20, "vinnana": 26}
    for k, a in enumerate(["vedana", "sanna", "sankhara", "vinnana"], start=2):
        segs.append(H(5, cap(AGG[a]["k"]), f"2-1-1-{k}-0"))
        n = ids[a]
        extra = [f"{SEC_HEADINGS['Suttantabhājanīyaṃ']}."] if a == "vinnana" else None
        segs += suttanta_mental(a, [f"2-{n + i}" for i in range(6)], extra)
    segs += [H(4, SEC_HEADINGS["Abhidhammabhājanīyaṃ"], "2-1-2-0"),
             ([FIVE_LIST], "2-32"),
             H(5, cap(AGG["rupa"]["k"]), "2-1-2-1-0"),
             (abhidhamma_rupa(), "2-33")]
    return segs


def render(segs):
    out = []
    for lines, bid in segs:
        lines = list(lines)
        lines[-1] = f"{lines[-1]} ^{bid}"
        out.append("\n".join(lines))
    return unicodedata.normalize("NFC", "\n\n".join(out) + "\n")


PREAMBLE = [([HOMAGE], "T-1"), H(1, H_PITAKA, "0"), H(2, H_BOOK, "2-0")]


# ================================================================== formulas file
def formulas():
    F = []   # (pāli, tiếng Việt, from pi-1?)
    add = lambda p, v, pi1=False: F.append((p, v, pi1))
    F.append("## Book frame and headings")
    add("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE, True)
    add("# Abhidhammapiṭake", f"# {H_PITAKA}", True)
    add("## Vibhaṅgapāḷi", f"## {H_BOOK}")
    for p, v in CH_HEADINGS.items():
        add(f"### {p}", f"### {v}")
    for p, v in SEC_HEADINGS.items():
        add(f"#### {p} / {p}. (closing line)", f"#### {v} / {v}.")
    for a in FIVE:
        add(f"##### {cap(AGG[a]['p'])}", f"##### {cap(AGG[a]['k'])}")
    add("Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.",
        FIVE_LIST)
    F.append("## Question and closing frames")
    add("Tattha katamo/katamā/katamaṃ/katame X?", f"{TATTHA} X {IS_WHAT}", True)
    add("– ayaṃ/idaṃ vuccati X.", f"– {CALLED_SG} X.", True)
    add("– ime vuccanti X. / Ime vuccanti X.", f"– {CALLED_PL} X. / {cap(CALLED_PL)} X.")
    add("Ayaṃ vuccati X. (own sentence)", f"{cap(CALLED_SG)} X.", True)
    add("X atītaṃ / anāgataṃ / paccuppannaṃ", "X thuộc quá khứ / thuộc tương lai / thuộc hiện tại", True)
    add("X ajjhattaṃ / bahiddhā", "X ở nơi bản thân / ở bên ngoài bản thân", True)
    add("X oḷārikaṃ / sukhumaṃ", "X ở dạng thô / ở dạng vi tế", True)
    add("X hīnaṃ / paṇītaṃ", "X thấp kém / ưu việt", True)
    add("X dūre / santike", "X ở xa / ở gần", True)
    add("Tattha katamā vedanā oḷārikā sukhumā?", q_pair("vedana", "olarika", "sukhuma"))
    add("Tattha katamā vedanā hīnā paṇītā?", q_pair("vedana", "hina", "panita"))
    add("aggregate nouns: rūpaṃ / vedanā / saññā / saṅkhārā / viññāṇaṃ (pl. viññāṇā)",
        "vật chất / cảm giác / tri giác / các sự tạo tác / thức (pl. các loại thức)")
    F.append("## The aggregate definition")
    add("Tattha katamo rūpakkhandho? Yaṃ kiñci rūpaṃ atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā "
        "oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā yaṃ dūre santike vā, tadekajjhaṃ abhisaññūhitvā "
        "abhisaṅkhipitvā – ayaṃ vuccati rūpakkhandho.", khandha_def("rupa"))
    for a in FIVE[1:]:
        add(f"(same for {AGG[a]['p']})", khandha_def(a))
    F.append("## Past, future, present; internal, external")
    add("Yaṃ rūpaṃ atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ uppajjitvā vigataṃ "
        "atītaṃ atītaṃsena saṅgahitaṃ, …", f"Vật chất {TIME_BODY['atita']}: …", True)
    add("Yaṃ rūpaṃ ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ anuppannaṃ asamuppannaṃ "
        "anuṭṭhitaṃ asamuṭṭhitaṃ anāgataṃ anāgataṃsena saṅgahitaṃ, …", f"Vật chất {TIME_BODY['anagata']}: …", True)
    add("Yaṃ rūpaṃ jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ uppannaṃ samuppannaṃ uṭṭhitaṃ "
        "samuṭṭhitaṃ paccuppannaṃ paccuppannaṃsena saṅgahitaṃ, …", f"Vật chất {TIME_BODY['paccuppanna']}: …", True)
    add("Yaṃ rūpaṃ tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ, …",
        f"Vật chất {INT_BODY}: …", True)
    add("Yaṃ rūpaṃ tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ "
        "upādinnaṃ, …", f"Vật chất {EXT_BODY}: …", True)
    add("cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāyarūpaṃ", RUPA_LIST, True)
    for a in FIVE[1:]:
        add(f"member list ({AGG[a]['p']})", LISTS[a])
    add("full example ^2-3 line 1", time_line("rupa", "atita"))
    F.append("## Matter: gross, subtle, inferior, superior, far, near")
    add("Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ", GROSS_RANGE, True)
    add("Itthindriyaṃ…pe… kabaḷīkāro āhāro", SUBTLE_RANGE, True)
    add("kabaḷīkāro [kabaḷiṃkāro (sī. syā.)] āhāro", f"{FOOD} {spell('Sī., Syā.', 'kabaḷiṃkāro')}")
    add("Yaṃ rūpaṃ tesaṃ tesaṃ sattānaṃ uññātaṃ avaññātaṃ hīḷitaṃ paribhūtaṃ acittīkataṃ hīnaṃ hīnamataṃ "
        "hīnasammataṃ aniṭṭhaṃ akantaṃ amanāpaṃ, rūpā saddā gandhā rasā phoṭṭhabbā",
        f"Vật chất {HINA_BODY}: {OBJECTS5}")
    add("Yaṃ rūpaṃ tesaṃ tesaṃ sattānaṃ anuññātaṃ anavaññātaṃ ahīḷitaṃ aparibhūtaṃ cittīkataṃ paṇītaṃ "
        "paṇītamataṃ paṇītasammataṃ iṭṭhaṃ kantaṃ manāpaṃ, rūpā saddā gandhā rasā phoṭṭhabbā",
        f"Vật chất {PANITA_BODY}: {OBJECTS5}")
    add("yaṃ vā panaññampi atthi rūpaṃ anāsanne anupakaṭṭhe dūre asantike", FAR_REST)
    add("yaṃ vā panaññampi atthi rūpaṃ āsanne upakaṭṭhe avidūre santike", NEAR_REST)
    add("Taṃ taṃ vā pana rūpaṃ upādāyupādāya rūpaṃ hīnaṃ paṇītaṃ daṭṭhabbaṃ.", relative("rupa", ("hina", "panita")))
    add("Taṃ taṃ vā pana vedanaṃ upādāyupādāya vedanā oḷārikā sukhumā daṭṭhabbā.",
        relative("vedana", ("olarika", "sukhuma")))
    add("Te te vā pana saṅkhāre upādāyupādāya saṅkhārā dūre santike daṭṭhabbā.",
        relative("sankhara", ("dure", "santike")))
    F.append("## Mental aggregates: the comparison members (N = cảm giác / tri giác / các sự tạo tác / thức)")
    for k, v in ETH.items():
        add(f"{k} (akusalā / kusalābyākatā … ) N", f"N {v}")
    for k, v in FEEL.items():
        add(f"{k} vedanā / {k} vedanāya(-hi) sampayuttā N", f"{v} / N {CONJ} {v}")
    for k, v in OTHER.items():
        add(f"{k} N", f"N {v}")
    add("A oḷārikā, B sukhumā.", "A thì ở dạng thô, B thì ở dạng vi tế.")
    add("A hīnā, B paṇītā.", "A thì thấp kém, B thì ưu việt.")
    add("A B-hi dūre; … / A B-ya santike; …", "A thì ở xa B; … / A thì ở gần B; …")
    add("example ^2-11", " ".join([q_pair("vedana", "olarika", "sukhuma"),
                                   contrast("vedana", CONTRAST["vedana"][:2], "olarika", "sukhuma"), "…"]))
    F.append("## Abhidhamma section: the matter classifications")
    for n in range(1, 12):
        add(f"{VIDHA[n]} rūpakkhandho – … / Evaṃ {VIDHA[n].lower()} rūpakkhandho.",
            f"{vidha_open(n)} … / {vidha_close(n)}")
    add("sabbaṃ rūpaṃ na hetu, ahetukaṃ, … jarābhibhūtaṃ",
        f"{SABBA_RUPA} " + "; ".join(EKAKA), True)
    add("Atthi rūpaṃ X, atthi rūpaṃ Y.", f"{cap(KIND)} X, {KIND} Y.", True)
    add("yaṃ taṃ rūpaṃ ajjhattikaṃ taṃ X, yaṃ taṃ rūpaṃ bāhiraṃ taṃ atthi Y, atthi Z",
        "vật chất nào thuộc phần bên trong thì X; vật chất nào thuộc phần bên ngoài thì có loại Y, có loại Z", True)
    add("yaṃ taṃ rūpaṃ X taṃ atthi Y, atthi Z", "vật chất nào X thì có loại Y, có loại Z", True)
    add("diṭṭhaṃ, sutaṃ, mutaṃ, viññātaṃ rūpaṃ", SEEN, True)
    add("(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.)", RUPAKANDA_NOTE)
    for n in range(5, 12):
        add(f"{VIDHA[n]} list", VIDHA_BODY[n], True)
    add("Ayaṃ vuccati rūpakkhandho.", f"{cap(CALLED_SG)} {AGG['rupa']['k']}.")
    F.append("## Punctuation and variants")
    add("…pe…", "… (same spot; never «….»)", True)
    add("– (Pāli dash)", "– (same spot, same count; never added)", True)
    add("[word (sī. ka.)] spelling only", "[khác chính tả (Sī., Ka.): word]", True)
    add("[word (syā.)] other word", "[dị bản (Syā.): word]", True)
    add("(Ka) / (Kha) / (Ga)", "(a) / (b) / (c)", True)
    out = ["# pi-2 Vibhaṅga: Vietnamese rails sentence formulas (binding for chapter agents)", "",
           "Format: Pāli = tiếng Việt, one per line; (pi-1) = taken unchanged from the approved pi-1 Vietnamese "
           "rails. Generated by build_rails_sample_vi.py; import its constants rather than retyping. Termbase: "
           "AI_translation/vietnamese/pi-2-pali-vietnamese-termbase-plain.md (+ pi-2-vi-ai/termbase/APPROVED.md). "
           "Style: 0-INBOX/temp/pipeline/vietnamese-style.md.", ""]
    for f in F:
        if isinstance(f, str):
            out += ["", f, ""]
        else:
            p, v, pi1 = f
            out.append(f"{p} = {v}{' (pi-1)' if pi1 else ''}")
    return unicodedata.normalize("NFC", "\n".join(out).replace("\n\n\n", "\n\n") + "\n")


def check_against_pali(text, pali_path):
    """Same block ids in order and same non-empty line count per segment."""
    def segs(t):
        res, cur = [], 0
        for ln in t.splitlines():
            if not ln.strip():
                continue
            cur += 1
            m = ID.search(ln)
            if m:
                res.append((m.group(1), cur))
                cur = 0
        return res
    a, b = segs(pali_path.read_text(encoding="utf-8")), segs(text)
    assert a == b, f"segment mismatch:\n{a}\n{b}"
    return len(a)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    (RAILS / "sample-1").mkdir(parents=True, exist_ok=True)
    pre = render(PREAMBLE)
    n0 = check_against_pali(pre, PALI / "preamble.md")
    (OUT / "preamble.md").write_text(pre, encoding="utf-8", newline="\n")
    smp = render(sample_segments())
    n1 = check_against_pali(smp, PALI_SAMPLE)
    (RAILS / "sample-1" / "1-sample.md").write_text(smp, encoding="utf-8", newline="\n")
    (RAILS / "vi-rails-formulas.md").write_text(formulas(), encoding="utf-8", newline="\n")
    print(f"preamble: {n0} segments; sample: {n1} segments; formulas written")
