"""Builder for the Hindi rails SAMPLE of pi-2 (Vibhaṅga, plain audience).

Writes:
  AI_translation/hindi/pi-2-hindi-plain-rails_split_chapters/preamble.md
  0-INBOX/temp/pipeline/pi-2-hi/rails/sample-1/1-pali-sample.md   (first 77 non-empty lines of 1-khandhavibhango.md)
  0-INBOX/temp/pipeline/pi-2-hi/rails/sample-1/1-sample.md        (the Hindi, line-aligned with the excerpt)
  0-INBOX/temp/pipeline/pi-2-hi/rails/hi-rails-formulas.md

All Hindi comes from the fixed strings and functions below, so identical Pāli gives byte-identical Hindi.
Terms follow the locked termbase AI_translation/hindi/pi-2-pali-hindi-termbase-plain.md; sentence shapes follow
the reviewed pi-1 rails Hindi (main() asserts that every string marked PI1 still occurs in it).
Later chapter agents may import this module read-only (importing it writes nothing; only main() writes).

usage: python -I -X utf8 build_rails_sample.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"
OUT = ROOT / "AI_translation" / "hindi" / "pi-2-hindi-plain-rails_split_chapters"
RAILS = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-2-hi" / "rails"
SAMPLE = RAILS / "sample-1"
PI1_HI = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
SAMPLE_LINES = 77  # non-empty lines of 1-khandhavibhango.md in the sample

# =========================================================================== book frame and headings
NAMO = "उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन"
PITAKA = "अभिधम्म पिटक में"
BOOK = "विस्तृत विश्लेषण"
CH_TITLE = {1: "समूहों का विश्लेषण"}           # ### Khandhavibhaṅgo (approved chapter title)
SUTTANTA_BH = "उपदेशों के अनुसार विश्लेषण"     # #### Suttantabhājanīyaṃ / closing line + «।»
ABHI_BH = "अभिधम्म के अनुसार विश्लेषण"         # #### Abhidhammabhājanīyaṃ / closing line + «।»
PANHA = "प्रश्नोत्तर"                            # #### Pañhāpucchakaṃ / closing line + «।»
DONE = "पूरा हुआ"                                # niṭṭhito: "<title> पूरा हुआ।"

# =========================================================================== aggregates
ORDER = ["rupa", "vedana", "sanna", "sankhara", "vinnana"]
KH = {
    "rupa": "भौतिक रूप का समूह",
    "vedana": "अनुभूति का समूह",
    "sanna": "पहचान का समूह",
    "sankhara": "मानसिक रचनाओं का समूह",
    "vinnana": "चेतना का समूह",
}
FIVE = "पाँच समूह – " + ", ".join(KH[k] for k in ORDER) + "।"  # PI1 ^1-1089 list

# noun forms: sg, pl (direct), obl (oblique pl); gender. saṅkhārā is always plural.
N = {
    "rupa": dict(sg="भौतिक रूप", pl="भौतिक रूप", obl="भौतिक रूपों", g="m"),
    "vedana": dict(sg="अनुभूति", pl="अनुभूतियाँ", obl="अनुभूतियों", g="f"),
    "sanna": dict(sg="पहचान", pl="पहचानें", obl="पहचानों", g="f"),
    "sankhara": dict(sg=None, pl="मानसिक रचनाएँ", obl="मानसिक रचनाओं", g="f"),
    "vinnana": dict(sg="चेतना", pl="चेतनाएँ", obl="चेतनाओं", g="f"),
}
PLURAL = {"sankhara"}


def is_pl(k):
    return k in PLURAL


def noun(k):
    return N[k]["pl"] if is_pl(k) else N[k]["sg"]


def ka(k):
    return "का" if N[k]["g"] == "m" else "की"


def hai(k):
    return "हैं" if is_pl(k) else "है"


def yah(k):
    return "ये" if is_pl(k) else "यह"


def called(k):
    """vuccati / vuccanti"""
    if is_pl(k):
        return "कही जाती हैं"
    return "कहा जाता है" if N[k]["g"] == "m" else "कही जाती है"


def what(k):
    """Tattha katamaṃ/katamā …? = यहाँ … क्या है?  (plural: कौन-सी हैं?)"""
    return "कौन-सी हैं?" if is_pl(k) else "क्या है?"


# --- the aggregate formula (Suttantabhājanīya opening of each aggregate)
def agg_formula(k):
    """Yaṃ kiñci rūpaṃ / Yā kāci vedanā / Ye keci saṅkhārā … tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā"""
    k_ = ka(k)
    ho = "हों" if is_pl(k) else "हो"
    us = "उन" if is_pl(k) else "उस"
    return (f"जो भी {noun(k)} {hai(k)}, चाहे अतीत {k_} {ho}, भविष्य {k_} {ho} या वर्तमान {k_}, "
            f"स्वयं से संबंधित {ho} या दूसरों से संबंधित, स्थूल {ho} या सूक्ष्म, हीन {ho} या उत्तम, "
            f"दूर {ho} या पास, {us} सबको एक साथ इकट्ठा करके, संक्षेप में समेटकर")


def agg_segment(k):
    return f"यहाँ {KH[k]} क्या है? {agg_formula(k)} – यह {KH[k]} कहा जाता है।"


# --- members listed after "यानी" (the Pāli list after the comma)
SENSES = ["आँख", "कान", "नाक", "जीभ", "शरीर", "मन"]


def contact_list(x):
    """cakkhusamphassajā X … manosamphassajā X"""
    items = [f"{s} के संपर्क से उत्पन्न {x}" for s in SENSES]
    return ", ".join(items[:-1]) + " और " + items[-1]


VINNANA6 = ", ".join(f"{s} की चेतना" for s in SENSES[:-1]) + " और मन की चेतना"  # cakkhuviññāṇaṃ … manoviññāṇaṃ
FEEL3 = "सुखद अनुभूति, दुःखद अनुभूति और न दुःखद, न सुखद अनुभूति"  # sukhā vedanā dukkhā vedanā adukkhamasukhā vedanā
MAHABHUTA = "चार महाभूत और चार महाभूतों से व्युत्पन्न भौतिक रूप"  # PI1 cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāyarūpaṃ
MEMBERS = {
    "rupa": MAHABHUTA,
    "vedana": FEEL3,
    "sanna": contact_list("पहचान"),
    "sankhara": contact_list("इरादा"),
    "vinnana": VINNANA6,
}

# --- past / future / present
ATITA = {  # atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ uppajjitvā vigataṃ atītaṃ
    "m": "अतीत का, समाप्त हो चुका, जा चुका, बदल चुका, अस्त हो चुका, पूरी तरह अस्त हो चुका, उत्पन्न होकर जा चुका, अतीत का",
    "f": "अतीत की, समाप्त हो चुकी, जा चुकी, बदल चुकी, अस्त हो चुकी, पूरी तरह अस्त हो चुकी, उत्पन्न होकर जा चुकी, अतीत की",  # PI1
}
ANAGATA = {  # ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ anuppannaṃ asamuppannaṃ anuṭṭhitaṃ asamuṭṭhitaṃ anāgataṃ
    "m": "न जन्मा हुआ, न हो चुका, न भली-भाँति जन्मा, न पैदा हुआ, न पूरी तरह पैदा हुआ, न प्रकट हुआ, न उत्पन्न, न भली-भाँति उत्पन्न, न उठा हुआ, न भली-भाँति उठा हुआ, भविष्य का",
    "f": "न जन्मी हुई, न हो चुकी, न भली-भाँति जन्मी, न पैदा हुई, न पूरी तरह पैदा हुई, न प्रकट हुई, न उत्पन्न, न भली-भाँति उत्पन्न, न उठी हुई, न भली-भाँति उठी हुई, भविष्य की",  # PI1
}
PACCUPPANNA = {  # jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ uppannaṃ samuppannaṃ uṭṭhitaṃ samuṭṭhitaṃ paccuppannaṃ
    "m": "जन्मा हुआ, हो चुका, भली-भाँति जन्मा, पैदा हुआ, पूरी तरह पैदा हुआ, प्रकट हुआ, उत्पन्न, भली-भाँति उत्पन्न, उठा हुआ, भली-भाँति उठा हुआ, वर्तमान का",
    "f": "जन्मी हुई, हो चुकी, भली-भाँति जन्मी, पैदा हुई, पूरी तरह पैदा हुई, प्रकट हुई, उत्पन्न, भली-भाँति उत्पन्न, उठी हुई, भली-भाँति उठी हुई, वर्तमान की",  # PI1
}
TIME = {"atita": ("अतीत", ATITA), "anagata": ("भविष्य", ANAGATA), "paccuppanna": ("वर्तमान", PACCUPPANNA)}


def time_sentence(k, t, members=None):
    """Tattha katamaṃ rūpaṃ atītaṃ? Yaṃ rūpaṃ atītaṃ … atītaṃsena saṅgahitaṃ, <members> – idaṃ vuccati rūpaṃ atītaṃ."""
    word, strings = TIME[t]
    attr = f"{word} {ka(k)}"
    np_ = f"{attr} {noun(k)}"
    s = strings[N[k]["g"]]
    members = MEMBERS[k] if members is None else members
    return (f"यहाँ {np_} {what(k)} जो {noun(k)} {s} {hai(k)} और {word} के अंतर्गत वर्गीकृत {hai(k)}, "
            f"यानी {members} – {yah(k)} {np_} {called(k)}।")


# --- internal / external (ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ)
OWN = {
    "m": "उन-उन प्राणियों के स्वयं में, अपना, उन्हीं का, हर व्यक्ति का निजी और कर्म से उत्पन्न",
    "f": "उन-उन प्राणियों के स्वयं में, अपनी, उन्हीं की, हर व्यक्ति की निजी और कर्म से उत्पन्न",
}
OTHERS = {g: s.replace("उन-उन प्राणियों", "उन-उन दूसरे प्राणियों, दूसरे व्यक्तियों") for g, s in OWN.items()}
AJJHATTA = "स्वयं से संबंधित"   # ajjhatta (internal/external pair)
BAHIDDHA = "दूसरों से संबंधित"  # bahiddhā (internal/external pair)


def own_sentence(k, external, members=None):
    attr = BAHIDDHA if external else AJJHATTA
    np_ = f"{attr} {noun(k)}"
    s = (OTHERS if external else OWN)[N[k]["g"]]
    members = MEMBERS[k] if members is None else members
    return f"यहाँ {np_} {what(k)} जो {noun(k)} {s} {hai(k)}, यानी {members} – {yah(k)} {np_} {called(k)}।"


# --- rūpa: coarse/subtle, inferior/superior, far/near (Suttantabhājanīya)
EYE_TO_TOUCH = "आँख का इंद्रिय-क्षेत्र… स्पर्श का इंद्रिय-क्षेत्र"  # Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ
FOOD_VAR = "[वर्तनी-भेद (Sī., Syā.): kabaḷiṃkāro]"


def fem_to_food(variant=False):
    """Itthindriyaṃ…pe… kabaḷīkāro [variant] āhāro"""
    v = f" {FOOD_VAR}" if variant else ""
    return f"स्त्रीत्व की क्षमता… कौर-कौर खाया जाने वाला{v} भोजन"


SENSE_OBJECTS = "दृश्य रूप, ध्वनि, गंध, स्वाद और स्पर्श"  # rūpā saddā gandhā rasā phoṭṭhabbā
HINA_STR = {  # uññātaṃ avaññātaṃ hīḷitaṃ paribhūtaṃ acittīkataṃ hīnaṃ hīnamataṃ hīnasammataṃ aniṭṭhaṃ akantaṃ amanāpaṃ
    "m": "तुच्छ समझा गया, तिरस्कृत, निंदित, अपमानित, असम्मानित, हीन, हीन माना गया, आम तौर पर हीन माना गया, अनचाहा, अप्रिय, मन को न भाने वाला",
}
PANITA_STR = {  # anuññātaṃ anavaññātaṃ ahīḷitaṃ aparibhūtaṃ cittīkataṃ paṇītaṃ paṇītamataṃ paṇītasammataṃ iṭṭhaṃ kantaṃ manāpaṃ
    "m": "न तुच्छ समझा गया, न तिरस्कृत, न निंदित, न अपमानित, सम्मानित, उत्तम, उत्तम माना गया, आम तौर पर उत्तम माना गया, मनचाहा, प्रिय, मनभावन",
}
BY_BEINGS = "उन-उन प्राणियों द्वारा"  # tesaṃ tesaṃ sattānaṃ (with the hīna/paṇīta strings)
OR_OTHER = "या जो भी अन्य"           # yaṃ vā panaññampi atthi
FAR_STR = "निकट नहीं है, समीप नहीं है, दूर है, पास नहीं है"   # anāsanne anupakaṭṭhe dūre asantike
NEAR_STR = "निकट है, समीप है, दूर नहीं है, पास है"            # āsanne upakaṭṭhe avidūre santike
COARSE, SUBTLE = "स्थूल", "सूक्ष्म"
LOW, HIGH = "हीन", "उत्तम"
FAR, NEAR = "दूर", "पास"


def compare(k, pair):
    """Taṃ taṃ vā pana X upādāyupādāya X … daṭṭhabbaṃ/daṭṭhabbā."""
    if is_pl(k):
        return f"या फिर, उन-उन {N[k]['obl']} से तुलना करके {N[k]['obl']} को {pair} समझना चाहिए।"
    return f"या फिर, उस-उस {N[k]['sg']} से तुलना करके {N[k]['sg']} को {pair} समझना चाहिए।"


def rupa_q(attr):
    """Tattha katamaṃ rūpaṃ <attr>? (attr before the noun; dūre/santike as «दूर का»/«पास का»)"""
    return f"यहाँ {attr} भौतिक रूप क्या है?"


def rupa_called(attr):
    return f"यह {attr} भौतिक रूप कहा जाता है।"


# --- qualifiers for vedanā / saññā / saṅkhārā / viññāṇa (feminine nouns)
QUAL = {
    "akusala": "हानिकर",
    "kusala": "हितकर",
    "abyakata": "नैतिक रूप से अनिर्धारित",
    "kusalabyakata": "हितकर और नैतिक रूप से अनिर्धारित",
    "kusalakusala": "हितकर और हानिकर",
    "akusalabyakata": "हानिकर और नैतिक रूप से अनिर्धारित",
    "sasava": "मन के मैलों का विषय बनने वाली",
    "anasava": "मन के मैलों का विषय न बनने वाली",
    "sam": "ध्यान-अवस्था में लीन व्यक्ति की",       # samāpannassa
    "asam": "ध्यान-अवस्था में लीन न हुए व्यक्ति की",  # asamāpannassa
    "patigha": "टकराव वाले संपर्क से उत्पन्न",       # paṭighasamphassajā
    "adhivacana": "नाम वाले संपर्क से उत्पन्न",      # adhivacanasamphassajā
}
ADM = "न दुःखद, न सुखद"  # adukkhamasukha (the termbase's comma-free form gets its normal Hindi comma)
FEEL_V = {  # the feeling qualifiers said of vedanā itself (adjective + noun)
    "dukkha": "दुःखद",
    "sukha": "सुखद",
    "adm": ADM,
    "sukhadukkha": "सुखद और दुःखद",
}
FEEL_S = {  # the same qualifiers for the other three: … vedanāya/vedanāhi sampayuttā X
    "dukkha": "दुःखद अनुभूति से जुड़ी",
    "sukha": "सुखद अनुभूति से जुड़ी",
    "adm": f"{ADM} अनुभूति से जुड़ी",
    "sukhadukkha": "सुखद और दुःखद अनुभूतियों से जुड़ी",
    "sukha+adm": f"सुखद अनुभूति से और {ADM} अनुभूति से जुड़ी",
    "dukkha+adm": f"दुःखद अनुभूति से और {ADM} अनुभूति से जुड़ी",
}


def np(k, q, num, post=""):
    """Noun phrase for aggregate k with qualifier q, number 's'/'p'; post = postposition (से, के पास)."""
    sfx = f" {post}" if post else ""
    if is_pl(k):
        num = "p"
    if k == "vedana" and q in ("sukha+adm", "dukkha+adm"):  # sukhā ca adukkhamasukhā ca vedanā
        first = FEEL_V[q.split("+")[0]]
        return f"{first} अनुभूति{sfx} और {ADM} अनुभूति{sfx}"
    if num == "p":
        nn = N[k]["obl"] if post else N[k]["pl"]
    else:
        nn = N[k]["sg"]
    if k == "vedana" and q in FEEL_V:
        adj = FEEL_V[q]
    elif q in FEEL_S:
        adj = FEEL_S[q]
    else:
        adj = QUAL[q]
    return f"{adj} {nn}{sfx}"


def v(k, num):
    return "हैं" if (is_pl(k) or num == "p") else "है"


def pair_sentence(k, a, na, b, nb, x, y):
    """A x, B y.  e.g. Akusalā vedanā oḷārikā, kusalābyākatā vedanā sukhumā."""
    return f"{np(k, a, na)} {x} {v(k, na)}, {np(k, b, nb)} {y} {v(k, nb)}।"


def far_clause(k, a, na, b, nb):
    """A B-ehi/-āya dūre"""
    return f"{np(k, a, na)} {np(k, b, nb, 'से')} {FAR} {v(k, na)}"


def near_clause(k, a):
    """A A-āya/-ānaṃ/-assa santike"""
    return f"{np(k, a, 's')} {np(k, a, 's', 'के पास')} {v(k, 's')}"


def which_q(k, x, y):
    """Tattha katamā vedanā oḷārikā sukhumā? = यहाँ कौन-सी अनुभूति स्थूल है और कौन-सी सूक्ष्म?"""
    return f"यहाँ कौन-सी {noun(k)} {x} {hai(k)} और कौन-सी {y}?"


def far_q(k, word):
    """Tattha katamā vedanā dūre/santike?"""
    return f"यहाँ {word} {ka(k)} {noun(k)} {what(k)}"


def far_called(k, word):
    return f"{yah(k)} {word} {ka(k)} {noun(k)} {called(k)}।"


# pair lists (number per side follows the Pāli; the viññāṇa section shows it explicitly)
BASE_PAIRS = [("akusala", "s", "kusalabyakata", "p"), ("kusalakusala", "p", "abyakata", "s"),
              ("dukkha", "s", "sukha+adm", "p"), ("sukhadukkha", "p", "adm", "s"),
              ("asam", "s", "sam", "s"), ("sasava", "s", "anasava", "s")]
COARSE_PAIRS = {"vedana": BASE_PAIRS, "sanna": [("patigha", "s", "adhivacana", "s")] + BASE_PAIRS,
                "sankhara": BASE_PAIRS, "vinnana": BASE_PAIRS}
HINA_PAIRS = {k: BASE_PAIRS for k in ("vedana", "sanna", "sankhara", "vinnana")}
FAR_KUSALA = [("akusala", "s", "kusalabyakata", "p"), ("kusalabyakata", "p", "akusala", "s"),
              ("kusala", "s", "akusalabyakata", "p"), ("akusalabyakata", "p", "kusala", "s"),
              ("abyakata", "s", "kusalakusala", "p"), ("kusalakusala", "p", "abyakata", "s")]
FAR_FEEL = [("dukkha", "s", "sukha+adm", "p"), ("sukha+adm", "p", "dukkha", "s"),
            ("sukha", "s", "dukkha+adm", "p"), ("dukkha+adm", "p", "sukha", "s"),
            ("adm", "s", "sukhadukkha", "p"), ("sukhadukkha", "p", "adm", "s")]
FAR_SAM = [("asam", "s", "sam", "s"), ("sam", "s", "asam", "s")]
FAR_SASAVA = [("sasava", "s", "anasava", "s"), ("anasava", "s", "sasava", "s")]
NEAR_GROUPS = [["akusala", "kusala", "abyakata"], ["dukkha", "sukha", "adm"], ["asam", "sam"], ["sasava", "anasava"]]


def coarse_segment(k, pairs, x, y):
    return " ".join([which_q(k, x, y)] + [pair_sentence(k, a, na, b, nb, x, y) for a, na, b, nb in pairs]
                    + [compare(k, f"{x} या {y}")])


def far_line(k, groups, dash_close):
    """groups: list of pair lists, each one Pāli sentence of clauses joined by ';'."""
    sents = ["; ".join(far_clause(k, *p) for p in g) for g in groups]
    body = "। ".join(sents)
    if dash_close:
        return f"{far_q(k, FAR)} {body} – {far_called(k, FAR)}"
    return f"{far_q(k, FAR)} {body}। {far_called(k, FAR)}"


def near_line(k, dash_close, closing=True):
    sents = ["; ".join(near_clause(k, a) for a in g) for g in NEAR_GROUPS]
    body = "। ".join(sents)
    end = f" {compare(k, f'{FAR} या {NEAR}')}" if closing else ""
    if dash_close:
        return f"{far_q(k, NEAR)} {body} – {far_called(k, NEAR)}{end}"
    return f"{far_q(k, NEAR)} {body}। {far_called(k, NEAR)}{end}"


# =========================================================================== Abhidhammabhājanīya
NUM = ["एक", "दो", "तीन", "चार", "पाँच", "छह", "सात", "आठ", "नौ", "दस", "ग्यारह"]
NUM_EXTRA = {24: "चौबीस", 30: "तीस", "bahu": "अनेक"}  # Catuvīsati-, Tiṃsa-, Bahuvidhena (not yet in the sample)


def vidha(n, k):
    """<N>vidhena <aggregate> –"""
    w = NUM[n - 1] if isinstance(n, int) and n <= 11 else NUM_EXTRA[n]
    return f"{w} प्रकार से {KH[k]} –"


def vidha_end(n, k):
    """Evaṃ <N>vidhena <aggregate>."""
    w = NUM[n - 1] if isinstance(n, int) and n <= 11 else NUM_EXTRA[n]
    return f"इस तरह {w} प्रकार से {KH[k]} बताया गया।"


RUPA_EKAVIDHA = (  # PI1 ^1-584 (sabbaṃ rūpaṃ na hetu … jarābhibhūtaṃ), without pi-1's [rūpiyaṃ] variant
    "सारा भौतिक रूप मूल रूपी न होने वाला, मूल से रहित, मूलों से अलग, कारणों पर निर्भर रहने वाला, निर्मित, भौतिक, "
    "लौकिक, मन के मैलों का विषय बनने वाला, बंधनों का विषय बनने वाला, गाँठों का विषय बनने वाला, बाढ़ों का विषय बनने वाला, "
    "जकड़नों का विषय बनने वाला, बाधाओं का विषय बनने वाला, ग़लत धारणा का विषय बनने वाला, आसक्ति का विषय बनने वाला, "
    "क्लेशों का विषय बनने वाला, नैतिक रूप से अनिर्धारित, विषय से रहित, मन का सहचर न होने वाला, मन से अलग, "
    "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाला, क्लेशों से मलिन न होने वाला, पर क्लेशों का विषय बनने वाला, "
    "न आरंभिक विचार और सतत विचार वाला, न आरंभिक विचार से रहित और केवल सतत विचार वाला, "
    "आरंभिक विचार और सतत विचार दोनों से रहित, उल्लास के साथ न होने वाला, सुख के साथ न होने वाला, "
    "समभाव के साथ न होने वाला, न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला, "
    "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला, न संचय की ओर, न संचय घटाने की ओर ले जाने वाला, "
    "न सीखने के चरण का, न सीखना पूरा होने के चरण का, सीमित, इंद्रिय-सुखों के लोक से संबंधित, "
    "सूक्ष्म भौतिक लोक से संबंधित न होने वाला, अभौतिक लोक से संबंधित न होने वाला, अस्तित्व के लोकों में समाया हुआ, "
    "अस्तित्व के लोकों में न समाया हुआ नहीं, अनिश्चित, मुक्ति की ओर न ले जाने वाला, "
    "उत्पन्न होने पर छह प्रकार की चेतनाओं से जाना जा सकने वाला, अनित्य, बुढ़ापे से ग्रस्त है।"
)
RUPA_EKAVIDHA_PI1 = RUPA_EKAVIDHA.replace("निर्मित, भौतिक, ", "निर्मित, भौतिक [पाठभेद (Sī.): rūpiyaṃ], ")

# Atthi rūpaṃ X, atthi rūpaṃ Y.  (PI1 ^1-U1; santike = पास per the pi-2 termbase)
NOUPADA_VAR = "[वर्तनी-भेद (Sī., Ka.): nupādā]"
UPADINNA_UPA = "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला"              # upādinnupādāniyaṃ
ANUPADINNA_UPA = "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला"   # anupādinnupādāniyaṃ
FOOD = "कौर-कौर खाया जाने वाला भोजन"                                       # kabaḷīkāro āhāro
RUPA_DUKA = [  # (X, Y) predicates, each ending in है
    ("व्युत्पन्न है", "व्युत्पन्न नहीं है"),
    ("कर्म से उत्पन्न है", "कर्म से उत्पन्न नहीं है"),
    (f"{UPADINNA_UPA} है", f"{ANUPADINNA_UPA} है"),
    ("दिखाई देने वाला है", "दिखाई न देने वाला है"),
    ("टकराव वाला है", "टकराव से रहित है"),
    ("क्षमता है", "क्षमता नहीं है"),
    ("महाभूत है", "महाभूत नहीं है"),
    ("प्रकट अभिव्यक्ति है", "प्रकट अभिव्यक्ति नहीं है"),
    ("मन से उत्पन्न है", "मन से उत्पन्न नहीं है"),
    ("मन के साथ-साथ होने वाला है", "मन के साथ-साथ न होने वाला है"),
    ("मन का अनुसरण करने वाला है", "मन का अनुसरण न करने वाला है"),
    ("आंतरिक है", "बाह्य है"),
    ("स्थूल है", "सूक्ष्म है"),
    ("दूर है", "पास है"),
]
RUPA_DUKA_FOOD = (f"{FOOD} है", f"{FOOD} नहीं है")


def duka(x, y, var=""):
    v_ = f" {var}" if var else ""
    return f"कुछ भौतिक रूप {x}, कुछ भौतिक रूप {y}{v_}।"


def kuch(x, y):
    """atthi X, atthi Y (after «उसमें»)"""
    return f"कुछ {x}, कुछ {y}"


def tika(own, x, y):
    """yaṃ taṃ rūpaṃ ajjhattikaṃ taṃ <own>, yaṃ taṃ rūpaṃ bāhiraṃ taṃ atthi <x>, atthi <y>"""
    return f"जो भौतिक रूप आंतरिक है, वह {own}; जो भौतिक रूप बाह्य है, उसमें {kuch(x, y)}"


def catukka(a, b, x, y):
    """yaṃ taṃ rūpaṃ <a> taṃ atthi <x>, atthi <y>; yaṃ taṃ rūpaṃ <b> taṃ atthi <x>, atthi <y>"""
    return f"जो भौतिक रूप {a}, उसमें {kuch(x, y)}; जो भौतिक रूप {b}, उसमें {kuch(x, y)}"


SEEN_HEARD = "देखा हुआ, सुना हुआ, अनुभव किया हुआ और जाना हुआ भौतिक रूप"  # PI1 diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ
ELEMENTS4 = "पृथ्वी तत्व, जल तत्व, अग्नि तत्व, वायु तत्व और जो भी भौतिक रूप व्युत्पन्न है"  # PI1 ^1-587
KNOWABLE = [f"{s} से जाना जा सकने वाला भौतिक रूप" for s in SENSES[:5]]
KNOW6 = ", ".join(KNOWABLE) + " और मन से जाना जा सकने वाला भौतिक रूप"  # PI1 ^1-588
MANODHATU_K = "मन के तत्व से जाना जा सकने वाला भौतिक रूप"
MANOVINNANADHATU_K = "मन की चेतना के तत्व से जाना जा सकने वाला भौतिक रूप"
KNOW7 = ", ".join(KNOWABLE) + f", {MANODHATU_K} और {MANOVINNANADHATU_K}"  # PI1 ^1-589
# pi-2 termbase: sukha/dukkha as compound members = सुख/दुःख (pi-1 ^1-590 had सुखद/दुःखद संपर्क वाला)
TOUCH_PAIR = "जिसमें कुछ सुख-संपर्क वाला है, कुछ दुःख-संपर्क वाला है"  # atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ
KNOW8 = ", ".join(KNOWABLE) + f", {TOUCH_PAIR}, {MANODHATU_K} और {MANOVINNANADHATU_K}"
FACULTIES8 = "आँख की क्षमता, कान की क्षमता, नाक की क्षमता, जीभ की क्षमता, शरीर की क्षमता, स्त्रीत्व की क्षमता, पुरुषत्व की क्षमता, जीवन-क्षमता"
NINE = f"{FACULTIES8} और जो भी भौतिक रूप क्षमता नहीं है"                                      # PI1 ^1-591
TEN = f"{FACULTIES8} और जो भौतिक रूप क्षमता नहीं है, उसमें कुछ टकराव वाला है, कुछ टकराव से रहित है"  # PI1 ^1-592
BASES10 = ("आँख का इंद्रिय-क्षेत्र, कान का इंद्रिय-क्षेत्र, नाक का इंद्रिय-क्षेत्र, जीभ का इंद्रिय-क्षेत्र, "
           "शरीर का इंद्रिय-क्षेत्र, दृश्य रूप का इंद्रिय-क्षेत्र, ध्वनि का इंद्रिय-क्षेत्र, गंध का इंद्रिय-क्षेत्र, "
           "स्वाद का इंद्रिय-क्षेत्र, स्पर्श का इंद्रिय-क्षेत्र")
ELEVEN = f"{BASES10} और जो भी भौतिक रूप दिखाई न देने वाला और टकराव से रहित है और मन के विषयों के इंद्रिय-क्षेत्र में समाया हुआ है"  # PI1 ^1-593
AS_IN_RUPAKANDA = "(जैसे भौतिक रूप के अध्याय में विश्लेषण किया गया है, उसी तरह यहाँ विश्लेषण करना चाहिए।)"
# (Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.)

PI1_STRINGS = [FIVE.split(" – ")[1][:-1], ATITA["f"], ANAGATA["f"], PACCUPPANNA["f"], MAHABHUTA, RUPA_EKAVIDHA_PI1,
               SEEN_HEARD, ELEMENTS4, KNOW6, KNOW7, NINE, TEN, FOOD, UPADINNA_UPA, ANUPADINNA_UPA,
               "जो भौतिक रूप आंतरिक है, वह कर्म से उत्पन्न है"] + [x for x, y in RUPA_DUKA[:-1]] + [y for x, y in RUPA_DUKA[:-1]]


# =========================================================================== segments
def build_preamble():
    return {"T-1": [NAMO], "0": [f"# {PITAKA}"], "2-0": [f"## {BOOK}"]}


def build_sample():
    h = {}
    h["2-1-0"] = [f"### {CH_TITLE[1]}"]
    h["2-1-1-0"] = [f"#### {SUTTANTA_BH}"]
    h["2-1"] = [FIVE]
    # ----- rūpa
    h["2-1-1-1-0"] = [f"##### {KH['rupa']}"]
    h["2-2"] = [agg_segment("rupa")]
    h["2-3"] = [time_sentence("rupa", t) for t in TIME]
    h["2-4"] = [own_sentence("rupa", False), own_sentence("rupa", True)]
    h["2-5"] = [f"{rupa_q(COARSE)} {EYE_TO_TOUCH} – {rupa_called(COARSE)}",
                f"{rupa_q(SUBTLE)} {fem_to_food(True)} – {rupa_called(SUBTLE)}"]
    h["2-6"] = [f"{rupa_q(LOW)} जो भौतिक रूप {BY_BEINGS} {HINA_STR['m']} है, यानी {SENSE_OBJECTS} – {rupa_called(LOW)}",
                f"{rupa_q(HIGH)} जो भौतिक रूप {BY_BEINGS} {PANITA_STR['m']} है, यानी {SENSE_OBJECTS} – "
                f"{rupa_called(HIGH)} {compare('rupa', f'{LOW} या {HIGH}')}"]
    h["2-7"] = [f"{rupa_q('दूर का')} {fem_to_food()}, {OR_OTHER} भौतिक रूप {FAR_STR} – {rupa_called('दूर का')}",
                f"{rupa_q('पास का')} {EYE_TO_TOUCH}, {OR_OTHER} भौतिक रूप {NEAR_STR} – {rupa_called('पास का')} "
                f"{compare('rupa', f'{FAR} या {NEAR}')}"]
    # ----- vedanā, saññā, saṅkhārā, viññāṇa
    ids = {"vedana": (2, 8), "sanna": (3, 14), "sankhara": (4, 20), "vinnana": (5, 26)}
    for k, (hn, s0) in ids.items():
        h[f"2-1-1-{hn}-0"] = [f"##### {KH[k]}"]
        h[f"2-{s0}"] = [agg_segment(k)]
        h[f"2-{s0 + 1}"] = [time_sentence(k, t) for t in TIME]
        h[f"2-{s0 + 2}"] = [own_sentence(k, False), own_sentence(k, True)]
        h[f"2-{s0 + 3}"] = [coarse_segment(k, COARSE_PAIRS[k], COARSE, SUBTLE)]
        h[f"2-{s0 + 4}"] = [coarse_segment(k, HINA_PAIRS[k], LOW, HIGH)]
        if k == "sanna":
            groups = [FAR_KUSALA[:4], FAR_KUSALA[4:], FAR_FEEL, FAR_SAM, FAR_SASAVA]
        else:
            groups = [FAR_KUSALA, FAR_FEEL, FAR_SAM, FAR_SASAVA]
        h[f"2-{s0 + 5}"] = [far_line(k, groups, dash_close=(k != "sankhara")),
                            near_line(k, dash_close=(k == "vinnana"))]
    h["2-31"].append(f"{SUTTANTA_BH}।")
    # ----- Abhidhammabhājanīya, rūpa
    h["2-1-2-0"] = [f"#### {ABHI_BH}"]
    h["2-32"] = [FIVE]
    h["2-1-2-1-0"] = [f"##### {KH['rupa']}"]
    r = "rupa"
    duka_body = " ".join([duka(*RUPA_DUKA[0], NOUPADA_VAR)] + [duka(x, y) for x, y in RUPA_DUKA[1:-1]])
    duka_body += " " + duka(*RUPA_DUKA[-1])[:-1] + "… " + duka(*RUPA_DUKA_FOOD)
    t1 = tika("व्युत्पन्न है", "व्युत्पन्न है", "व्युत्पन्न नहीं है")
    t2 = tika("कर्म से उत्पन्न है", "कर्म से उत्पन्न है", "कर्म से उत्पन्न नहीं है")
    t3 = tika(f"{UPADINNA_UPA} है", f"{UPADINNA_UPA} है", f"{ANUPADINNA_UPA} है")
    t_last = tika(f"{FOOD} नहीं है", f"{FOOD} है", f"{FOOD} नहीं है")
    UP, NUP = "व्युत्पन्न है", "व्युत्पन्न नहीं है"
    c = [catukka(UP, NUP, "कर्म से उत्पन्न है", "कर्म से उत्पन्न नहीं है"),
         catukka(UP, NUP, f"{UPADINNA_UPA} है", f"{ANUPADINNA_UPA} है"),
         catukka(UP, NUP, "टकराव वाला है", "टकराव से रहित है"),
         catukka(UP, NUP, "स्थूल है", "सूक्ष्म है"),
         catukka(UP, NUP, "दूर है", "पास है")]
    h["2-33"] = [
        f"यहाँ {KH[r]} क्या है? {vidha(1, r)} {RUPA_EKAVIDHA} {vidha_end(1, r)}",
        f"{vidha(2, r)} {duka_body} {vidha_end(2, r)}",
        AS_IN_RUPAKANDA,
        f"{vidha(3, r)} {t1}। {t2}। {t3}… {t_last}। {vidha_end(3, r)}",
        f"{vidha(4, r)} " + "। ".join(c[:-1]) + f"। {c[-1]}… {SEEN_HEARD}। {vidha_end(4, r)}",
        f"{vidha(5, r)} {ELEMENTS4}। {vidha_end(5, r)}",
        f"{vidha(6, r)} {KNOW6}। {vidha_end(6, r)}",
        f"{vidha(7, r)} {KNOW7}। {vidha_end(7, r)}",
        f"{vidha(8, r)} {KNOW8}। {vidha_end(8, r)}",
        f"{vidha(9, r)} {NINE}। {vidha_end(9, r)}",
        f"{vidha(10, r)} {TEN}। {vidha_end(10, r)}",
        f"{vidha(11, r)} {ELEVEN}। {vidha_end(11, r)}",
        f"यह {KH[r]} कहा जाता है।",
    ]
    return h


# =========================================================================== formulas file
def formulas_md():
    P = {"rupa": ("rūpaṃ", "n"), "vedana": ("vedanā", "f"), "sanna": ("saññā", "f"),
         "sankhara": ("saṅkhārā", "p"), "vinnana": ("viññāṇaṃ", "n")}
    KHP = {"rupa": "rūpakkhandho", "vedana": "vedanākkhandho", "sanna": "saññākkhandho",
           "sankhara": "saṅkhārakkhandho", "vinnana": "viññāṇakkhandho"}

    def end(g, n_, f_, p_):
        return {"n": n_, "f": f_, "p": p_}[g]

    L = ["# pi-2 Vibhaṅga: Hindi rails sentence formulas (read-only for chapter agents)", "",
         "Format: Pāli = Hindi, one per line. Generated by build_rails_sample.py (import it read-only instead of retyping).",
         "Terms follow the locked pi-2 termbase; sentence shapes follow the reviewed pi-1 rails Hindi.",
         "Lines marked (not yet in the sample) are settled for the same frames later in chapter 1 or in later chapters;",
         "the sample did not exercise them.", "",
         "## Headings and frames", "",
         f"Namo tassa bhagavato arahato sammāsambuddhassa = {NAMO}",
         f"# Abhidhammapiṭake = # {PITAKA}",
         f"## Vibhaṅgapāḷi = ## {BOOK} (mid-sentence: “{BOOK}”)",
         f"### Khandhavibhaṅgo = ### {CH_TITLE[1]} (the 18 chapter titles are in hi-zeroshot-terms.md §2, approved)",
         f"Khandhavibhaṅgo niṭṭhito. = {CH_TITLE[1]} {DONE}। (pattern «<title> पूरा हुआ।») (not yet in the sample)",
         f"#### Suttantabhājanīyaṃ = #### {SUTTANTA_BH}",
         f"Suttantabhājanīyaṃ. (closing line) = {SUTTANTA_BH}।",
         f"#### Abhidhammabhājanīyaṃ = #### {ABHI_BH}",
         f"Abhidhammabhājanīyaṃ. (closing line) = {ABHI_BH}। (not yet in the sample)",
         f"#### Pañhāpucchakaṃ = #### {PANHA} (not yet in the sample)",
         f"Pañhāpucchakaṃ. (closing line) = {PANHA}। (not yet in the sample)",
         "##### Tikaṃ / Dukaṃ (Pañhāpucchaka) = ##### तीन-तीन के वर्गीकरण / दो-दो के वर्गीकरण (not yet in the sample)",
         ] + [f"##### {KHP[k][0].upper() + KHP[k][1:]} = ##### {KH[k]}" for k in ORDER] + [
         "Tattha (opening a definition) = यहाँ",
         "Tattha katamo/katamaṃ/katamā X? = यहाँ X क्या है? (plural katame X? = यहाँ X कौन-सी हैं?)",
         "– idaṃ/ayaṃ vuccati X. (m) = – यह X कहा जाता है।; (f) = – यह X कही जाती है।; ime vuccanti X (pl) = – ये X कही जाती हैं।",
         "Ayaṃ/Ime vuccati… starting a new sentence (no dash in the Pāli) = …। यह/ये … कहा जाता है/कही जाती है(हैं)। (no dash)",
         "…pe… = … (same spot); Pāli ';' stays ';'; Pāli '.' becomes «।»",
         "Taṃ taṃ vā pana … (comparison sentence) opens with = या फिर,",
         f"(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.) = {AS_IN_RUPAKANDA}",
         "[kabaḷiṃkāro (sī. syā.)] = [वर्तनी-भेद (Sī., Syā.): kabaḷiṃkāro]; [nupādā (sī. ka.)] = [वर्तनी-भेद (Sī., Ka.): nupādā] (after the Hindi word or clause it qualifies)",
         "", "## Aggregate formulas", "",
         f"Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho. = {FIVE}",
         ]
    for k in ORDER:
        p, g = P[k]
        yk = end(g, "Yaṃ kiñci", "Yā kāci", "Ye keci")
        yy = end(g, "yaṃ", "yā", "ye")
        tail = end(g, "atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā",
                   "atītānāgatapaccuppannā ajjhattā vā bahiddhā vā oḷārikā vā sukhumā vā hīnā vā paṇītā vā",
                   "atītānāgatapaccuppannā ajjhattā vā bahiddhā vā oḷārikā vā sukhumā vā hīnā vā paṇītā vā")
        L.append(f"Tattha katamo {KHP[k]}? = यहाँ {KH[k]} क्या है?")
        L.append(f"{yk} {p} {tail} {yy} dūre santike vā, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā = {agg_formula(k)}")
        L.append(f"– ayaṃ vuccati {KHP[k]}. = – यह {KH[k]} कहा जाता है।")
    L.append("Members after the comma («, यानी …»):")
    L.append(f"cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāyarūpaṃ = {MAHABHUTA}")
    L.append(f"sukhā vedanā dukkhā vedanā adukkhamasukhā vedanā = {FEEL3}")
    L.append(f"cakkhusamphassajā saññā … manosamphassajā saññā = {MEMBERS['sanna']}")
    L.append(f"cakkhusamphassajā cetanā … manosamphassajā cetanā = {MEMBERS['sankhara']}")
    L.append(f"cakkhuviññāṇaṃ sotaviññāṇaṃ ghānaviññāṇaṃ jivhāviññāṇaṃ kāyaviññāṇaṃ manoviññāṇaṃ = {VINNANA6}")

    L += ["", "## Past / future / present", "",
          f"atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ uppajjitvā vigataṃ atītaṃ (m) = {ATITA['m']}",
          f"atītā niruddhā … atītā (f, and pl of saṅkhārā) = {ATITA['f']}",
          f"ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ anuppannaṃ asamuppannaṃ anuṭṭhitaṃ asamuṭṭhitaṃ anāgataṃ (m) = {ANAGATA['m']}",
          f"ajātā … anāgatā (f/pl) = {ANAGATA['f']}",
          f"jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ uppannaṃ samuppannaṃ uṭṭhitaṃ samuṭṭhitaṃ paccuppannaṃ (m) = {PACCUPPANNA['m']}",
          f"jātā … paccuppannā (f/pl) = {PACCUPPANNA['f']}",
          "atītaṃsena / anāgataṃsena / paccuppannaṃsena saṅgahitaṃ = (… है) और अतीत / भविष्य / वर्तमान के अंतर्गत वर्गीकृत है (pl: हैं)",
          "Full sentences (one per aggregate and time):"]
    for k in ORDER:
        p, g = P[k]
        kt = end(g, "katamaṃ", "katamā", "katame")
        for t, (pt, pv) in zip(TIME, [("atītaṃ", "atītā"), ("anāgataṃ", "anāgatā"), ("paccuppannaṃ", "paccuppannā")]):
            tw = pt if g == "n" else pv
            q = f"Tattha {kt} {p} {tw}? … – {end(g, 'idaṃ vuccati', 'ayaṃ vuccati', 'ime vuccanti')} {p} {tw}."
            L.append(f"{q} = {time_sentence(k, t)}")

    L += ["", "## Internal / external", "",
          f"tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ (m) = {OWN['m']}",
          f"… niyakā pāṭipuggalikā upādinnā (f/pl) = {OWN['f']}",
          f"tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ ajjhattaṃ … (m) = {OTHERS['m']}",
          f"tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ ajjhattaṃ … (f/pl) = {OTHERS['f']}",
          f"ajjhatta / bahiddhā (attribute) = {AJJHATTA} / {BAHIDDHA}",
          "Full sentences:"]
    for k in ORDER:
        p, g = P[k]
        kt = end(g, "katamaṃ", "katamā", "katame")
        aj = end(g, "ajjhattaṃ", "ajjhattā", "ajjhattā")
        L.append(f"Tattha {kt} {p} {aj}? … = {own_sentence(k, False)}")
        L.append(f"Tattha {kt} {p} bahiddhā? … = {own_sentence(k, True)}")

    L += ["", "## Coarse / subtle", "",
          f"oḷārika / sukhuma = {COARSE} / {SUBTLE}",
          f"Tattha katamaṃ rūpaṃ oḷārikaṃ? Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ – idaṃ vuccati rūpaṃ oḷārikaṃ. = {rupa_q(COARSE)} {EYE_TO_TOUCH} – {rupa_called(COARSE)}",
          f"Tattha katamaṃ rūpaṃ sukhumaṃ? Itthindriyaṃ…pe… kabaḷīkāro āhāro – idaṃ vuccati rūpaṃ sukhumaṃ. = {rupa_q(SUBTLE)} {fem_to_food()} – {rupa_called(SUBTLE)}",
          f"Tattha katamā vedanā oḷārikā sukhumā? = {which_q('vedana', COARSE, SUBTLE)}",
          f"Tattha katamā saññā oḷārikā sukhumā? = {which_q('sanna', COARSE, SUBTLE)}",
          f"Tattha katame saṅkhārā oḷārikā sukhumā? = {which_q('sankhara', COARSE, SUBTLE)}",
          f"Tattha katamaṃ viññāṇaṃ oḷārikaṃ sukhumaṃ? = {which_q('vinnana', COARSE, SUBTLE)}",
          "A oḷārikā, B sukhumā. = A स्थूल है, B सूक्ष्म है। (number follows the Pāli: singular «है», plural «हैं» with अनुभूतियाँ/पहचानें/चेतनाएँ/मानसिक रचनाएँ)",
          "Qualifiers (feminine nouns):"]
    pq = {"akusala": "akusalā", "kusala": "kusalā", "abyakata": "abyākatā", "kusalabyakata": "kusalābyākatā",
          "kusalakusala": "kusalākusalā", "akusalabyakata": "akusalābyākatā", "sasava": "sāsavā", "anasava": "anāsavā",
          "sam": "samāpannassa", "asam": "asamāpannassa", "patigha": "paṭighasamphassajā", "adhivacana": "adhivacanasamphassajā"}
    for q, pali in pq.items():
        L.append(f"{pali} = {QUAL[q]}")
    L += [f"dukkhā / sukhā / adukkhamasukhā vedanā = दुःखद / सुखद / {ADM} अनुभूति",
          f"sukhā ca adukkhamasukhā ca vedanā = {np('vedana', 'sukha+adm', 'p')} (plural verb)",
          f"dukkhā ca adukkhamasukhā ca vedanā = {np('vedana', 'dukkha+adm', 'p')} (plural verb)",
          f"sukhadukkhā vedanā = {np('vedana', 'sukhadukkha', 'p')}",
          f"dukkhāya vedanāya sampayuttā X = {FEEL_S['dukkha']} X",
          f"sukhāya vedanāya sampayuttā X = {FEEL_S['sukha']} X",
          f"adukkhamasukhāya vedanāya sampayuttā X = {FEEL_S['adm']} X",
          f"sukhāya ca adukkhamasukhāya ca vedanāhi sampayuttā X = {FEEL_S['sukha+adm']} X (X plural)",
          f"dukkhāya ca adukkhamasukhāya ca vedanāhi sampayuttā X = {FEEL_S['dukkha+adm']} X (X plural)",
          f"sukhadukkhāhi vedanāhi sampayuttā X = {FEEL_S['sukhadukkha']} X (X plural)",
          f"Taṃ taṃ vā pana vedanaṃ upādāyupādāya vedanā oḷārikā sukhumā daṭṭhabbā. = {compare('vedana', f'{COARSE} या {SUBTLE}')}",
          f"Te te vā pana saṅkhāre upādāyupādāya saṅkhārā oḷārikā sukhumā daṭṭhabbā. = {compare('sankhara', f'{COARSE} या {SUBTLE}')}",
          "Full segments:"]
    for k in ("vedana", "sanna", "sankhara", "vinnana"):
        L.append(f"{P[k][0]} oḷārika/sukhuma segment = {coarse_segment(k, COARSE_PAIRS[k], COARSE, SUBTLE)}")

    L += ["", "## Inferior / superior", "",
          f"hīna / paṇīta = {LOW} / {HIGH}",
          f"tesaṃ tesaṃ sattānaṃ (with the two strings below) = {BY_BEINGS}",
          f"uññātaṃ avaññātaṃ hīḷitaṃ paribhūtaṃ acittīkataṃ hīnaṃ hīnamataṃ hīnasammataṃ aniṭṭhaṃ akantaṃ amanāpaṃ = {HINA_STR['m']}",
          f"anuññātaṃ anavaññātaṃ ahīḷitaṃ aparibhūtaṃ cittīkataṃ paṇītaṃ paṇītamataṃ paṇītasammataṃ iṭṭhaṃ kantaṃ manāpaṃ = {PANITA_STR['m']}",
          f"rūpā saddā gandhā rasā phoṭṭhabbā = {SENSE_OBJECTS}",
          f"Taṃ taṃ vā pana rūpaṃ upādāyupādāya rūpaṃ hīnaṃ paṇītaṃ daṭṭhabbaṃ. = {compare('rupa', f'{LOW} या {HIGH}')}",
          f"Tattha katamā vedanā hīnā paṇītā? = {which_q('vedana', LOW, HIGH)}",
          "Full segments:"]
    for k in ("vedana", "sanna", "sankhara", "vinnana"):
        L.append(f"{P[k][0]} hīna/paṇīta segment = {coarse_segment(k, HINA_PAIRS[k], LOW, HIGH)}")

    L += ["", "## Far / near", "",
          f"dūre / santike (predicate) = {FAR} / {NEAR} (pi-2 termbase: santike = पास; pi-1 had निकट)",
          "rūpaṃ dūre / santike (attribute) = दूर का / पास का भौतिक रूप; vedanā dūre = दूर की अनुभूति",
          f"yaṃ vā panaññampi atthi rūpaṃ = {OR_OTHER} भौतिक रूप",
          f"anāsanne anupakaṭṭhe dūre asantike = {FAR_STR}",
          f"āsanne upakaṭṭhe avidūre santike = {NEAR_STR}",
          f"Taṃ taṃ vā pana rūpaṃ upādāyupādāya rūpaṃ dūre santike daṭṭhabbaṃ. = {compare('rupa', f'{FAR} या {NEAR}')}",
          "A B-ehi/-āhi/-āya dūre = A B से दूर है (हैं)",
          "A B-āya/-ānaṃ/-assa santike = A B के पास है (हैं)",
          f"Tattha katamā vedanā dūre? = {far_q('vedana', FAR)}",
          f"Tattha katame saṅkhārā santike? = {far_q('sankhara', NEAR)}",
          f"– ayaṃ vuccati vedanā dūre. = – {far_called('vedana', FAR)}",
          f"Ime vuccanti saṅkhārā santike. = {far_called('sankhara', NEAR)}",
          "Full lines:"]
    for k in ("vedana", "sanna", "sankhara", "vinnana"):
        if k == "sanna":
            groups = [FAR_KUSALA[:4], FAR_KUSALA[4:], FAR_FEEL, FAR_SAM, FAR_SASAVA]
        else:
            groups = [FAR_KUSALA, FAR_FEEL, FAR_SAM, FAR_SASAVA]
        L.append(f"{P[k][0]} dūre line = {far_line(k, groups, dash_close=(k != 'sankhara'))}")
        L.append(f"{P[k][0]} santike line = {near_line(k, dash_close=(k == 'vinnana'))}")

    L += ["", "## Classification frames (Abhidhammabhājanīya)", "",
          "Ekavidhena … Ekādasavidhena (… प्रकार से) = " + ", ".join(NUM),
          "Catuvīsatividhena / Tiṃsavidhena (Tiṃsatividhena) / Bahuvidhena = चौबीस / तीस / अनेक प्रकार से (not yet in the sample)",
          ] + [f"<N>vidhena {KHP[k]} – = <N> प्रकार से {KH[k]} –" for k in ORDER] + [
          f"Evaṃ <N>vidhena rūpakkhandho. = {vidha_end(1, 'rupa').replace('एक', '<N>')}",
          f"Ayaṃ vuccati rūpakkhandho. = यह {KH['rupa']} कहा जाता है।",
          f"sabbaṃ rūpaṃ na hetu … jarābhibhūtaṃ = {RUPA_EKAVIDHA}",
          "Atthi rūpaṃ X, atthi rūpaṃ Y. = कुछ भौतिक रूप X है, कुछ भौतिक रूप Y है।",
          ] + [f"  dyad = {duka(x, y)}" for x, y in RUPA_DUKA + [RUPA_DUKA_FOOD]] + [
          f"yaṃ taṃ rūpaṃ ajjhattikaṃ taṃ X, yaṃ taṃ rūpaṃ bāhiraṃ taṃ atthi Y, atthi Z = {tika('X है', 'Y है', 'Z है')} («;» for the Pāli comma between the halves)",
          f"yaṃ taṃ rūpaṃ upādā taṃ atthi X, atthi Y; yaṃ taṃ rūpaṃ no upādā taṃ atthi X, atthi Y = {catukka('व्युत्पन्न है', 'व्युत्पन्न नहीं है', 'X है', 'Y है')}",
          f"diṭṭhaṃ, sutaṃ, mutaṃ, viññātaṃ rūpaṃ = {SEEN_HEARD}",
          f"pathavīdhātu, āpodhātu, tejodhātu, vāyodhātu, yañca rūpaṃ upādā = {ELEMENTS4}",
          f"cakkhuviññeyyaṃ rūpaṃ … manoviññeyyaṃ rūpaṃ = {KNOW6}",
          f"… manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ = {KNOW7}",
          f"kāyaviññeyyaṃ rūpaṃ atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ = शरीर से जाना जा सकने वाला भौतिक रूप, {TOUCH_PAIR}",
          f"cakkhundriyaṃ … jīvitindriyaṃ, yañca rūpaṃ na indriyaṃ = {NINE}",
          f"… na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ = {TEN}",
          f"cakkhāyatanaṃ … phoṭṭhabbāyatanaṃ, yañca rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ = {ELEVEN}",
          "atthi X, atthi Y (classes of an aggregate, X masculine agreeing with समूह) = कुछ X है, कुछ Y है (not yet in the sample)",
          f"Ekavidhena vedanākkhandho – phassasampayutto. = {vidha(1, 'vedana')} संपर्क से जुड़ा है। (not yet in the sample)",
          f"Ekavidhena saṅkhārakkhandho – cittasampayutto. = {vidha(1, 'sankhara')} मन से जुड़ा है। (not yet in the sample)",
          f"Duvidhena vedanākkhandho – atthi sahetuko, atthi ahetuko. = {vidha(2, 'vedana')} कुछ मूल वाला है, कुछ मूल से रहित है। (not yet in the sample)",
          f"Duvidhena saṅkhārakkhandho – atthi hetu, atthi na hetu. = {vidha(2, 'sankhara')} कुछ मूल रूपी है, कुछ मूल रूपी नहीं है। (not yet in the sample)",
          f"Tividhena vedanākkhandho – atthi kusalo, atthi akusalo, atthi abyākato. = {vidha(3, 'vedana')} कुछ हितकर है, कुछ हानिकर है, कुछ नैतिक रूप से अनिर्धारित है। (not yet in the sample)",
          f"Catubbidhena vedanākkhandho – atthi kāmāvacaro, atthi rūpāvacaro, atthi arūpāvacaro, atthi apariyāpanno. = {vidha(4, 'vedana')} कुछ इंद्रिय-सुखों के लोक से संबंधित है, कुछ सूक्ष्म भौतिक लोक से संबंधित है, कुछ अभौतिक लोक से संबंधित है, कुछ अस्तित्व के लोकों में न समाया हुआ है। (not yet in the sample)",
          f"Pañcavidhena vedanākkhandho – atthi sukhindriyaṃ, atthi dukkhindriyaṃ, atthi somanassindriyaṃ, atthi domanassindriyaṃ, atthi upekkhindriyaṃ. = {vidha(5, 'vedana')} कुछ सुख की क्षमता है, कुछ दुःख की क्षमता है, कुछ प्रसन्नता की क्षमता है, कुछ उदासी की क्षमता है, कुछ समभाव की क्षमता है। (not yet in the sample)",
          "atthi sukhindriyasampayutto … atthi upekkhindriyasampayutto = कुछ सुख की क्षमता से जुड़ा है, कुछ दुःख की क्षमता से जुड़ा है, कुछ प्रसन्नता की क्षमता से जुड़ा है, कुछ उदासी की क्षमता से जुड़ा है, कुछ समभाव की क्षमता से जुड़ा है (not yet in the sample)",
          f"cakkhusamphassajā vedanā, … manosamphassajā vedanā (comma list) = {contact_list('अनुभूति')} (not yet in the sample)",
          "manodhātusamphassajā X, manoviññāṇadhātusamphassajā X = मन के तत्व के संपर्क से उत्पन्न X और मन की चेतना के तत्व के संपर्क से उत्पन्न X (not yet in the sample)",
          "kāyasamphassajā vedanā atthi sukhā, atthi dukkhā = शरीर के संपर्क से उत्पन्न अनुभूति, जिसमें कुछ सुखद है, कुछ दुःखद है (not yet in the sample)",
          "kāyasamphassajā saññā/cetanā atthi sukhasahagatā, atthi dukkhasahagatā = शरीर के संपर्क से उत्पन्न पहचान/इरादा, जिसमें कुछ सुख के साथ होने वाली/वाला है, कुछ दुःख के साथ होने वाली/वाला है (not yet in the sample)",
          "… atthi kusalā, atthi akusalā, atthi abyākatā (after a list) = …, जिसमें कुछ हितकर है, कुछ हानिकर है, कुछ नैतिक रूप से अनिर्धारित है (not yet in the sample)",
          "cakkhuviññāṇaṃ … kāyaviññāṇaṃ, manodhātu, manoviññāṇadhātu = आँख की चेतना, कान की चेतना, नाक की चेतना, जीभ की चेतना, शरीर की चेतना, मन का तत्व और मन की चेतना का तत्व (not yet in the sample)",
          "cakkhusamphassapaccayā vedanākkhandho = आँख के संपर्क के कारण अनुभूति का समूह (not yet in the sample)",
          f"Evaṃ dasavidhena vedanākkhandho. = {vidha_end(10, 'vedana')} (not yet in the sample)",
          f"Ayaṃ vuccati vedanākkhandho. = यह {KH['vedana']} कहा जाता है। (not yet in the sample)",
          "Dukamūlakaṃ. = दो-दो के वर्गीकरणों पर आधारित क्रम। (not yet in the sample)",
          "Tikamūlakaṃ. = तीन-तीन के वर्गीकरणों पर आधारित क्रम। (not yet in the sample)",
          "",
          "## Terms fixed in the sample (pi-2 termbase, inflected)", "",
          "upādinna = कर्म से उत्पन्न; upādā / no upādā = व्युत्पन्न / व्युत्पन्न नहीं; mahābhūta = महाभूत",
          "ajjhattika / bāhira (rūpa) = आंतरिक / बाह्य (distinct from ajjhatta / bahiddhā = स्वयं से संबंधित / दूसरों से संबंधित)",
          "paccattaṃ = अपना/अपनी; niyaka = उन्हीं का/की (no termbase entry; pi-1's niyata «उनसे बँधा» is a different word); pāṭipuggalika = हर व्यक्ति का/की निजी",
          "samuppanna / samuṭṭhita = भली-भाँति उत्पन्न / भली-भाँति उठा हुआ (keeps samuppanna apart from uppanna = उत्पन्न)",
          "hīnasammata / paṇītasammata = आम तौर पर हीन / उत्तम माना गया (no termbase entry)",
          "upakaṭṭhe = समीप; āsanne = निकट (no entry); santike = पास; avidūre = दूर नहीं",
          "sukhasamphassaṃ / dukkhasamphassaṃ = सुख-संपर्क वाला / दुःख-संपर्क वाला (sukha/dukkha in compounds = सुख/दुःख)",
          "rūpakaṇḍa = भौतिक रूप का अध्याय; vibhattaṃ = विश्लेषण किया गया; vibhajitabbaṃ = विश्लेषण करना चाहिए; tathā = उसी तरह",
          ]
    return "\n".join(L) + "\n"


# =========================================================================== writing
def segs_of_lines(lines):
    out, buf = [], []
    for line in lines:
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out.append((m.group(1), buf))
            buf = []
    assert not buf, "lines without id"
    return out


def emit(pali_lines, hindi, target):
    segs = segs_of_lines(pali_lines)
    ids = [i for i, _ in segs]
    assert set(ids) == set(hindi), (sorted(set(ids) - set(hindi)), sorted(set(hindi) - set(ids)))
    blocks = []
    for sid, plines in segs:
        hlines = list(hindi[sid])
        assert len(plines) == len(hlines), (sid, len(plines), len(hlines))
        for a, b in zip(plines, hlines):
            assert len(a) - len(a.lstrip("#")) == len(b) - len(b.lstrip("#")), sid
            assert a.count("–") + a.count("—") == b.count("–"), (sid, "dash", b[:80])
            assert a.count("[") == b.count("["), (sid, "bracket")
        hlines[-1] = f"{hlines[-1]} ^{sid}"
        blocks.append("\n".join(hlines))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n\n".join(blocks) + "\n", encoding="utf-8", newline="\n")
    print("wrote", target, len(blocks), "segments")


def main():
    pi1 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_HI.glob("*.md")))
    for s in PI1_STRINGS:
        assert s in pi1, ("not in pi-1 rails Hindi", s[:80])
    # preamble
    pre = (PALI / "preamble.md").read_text(encoding="utf-8").splitlines()
    emit(pre, build_preamble(), OUT / "preamble.md")
    # sample excerpt
    src = (PALI / "1-khandhavibhango.md").read_text(encoding="utf-8").splitlines()
    excerpt, n = [], 0
    for line in src:
        if line.strip():
            n += 1
            if n > SAMPLE_LINES:
                assert line.startswith("##### Vedanākkhandho ^2-1-2-2-0"), line
                break
        excerpt.append(line)
    while excerpt and not excerpt[-1].strip():
        excerpt.pop()
    SAMPLE.mkdir(parents=True, exist_ok=True)
    (SAMPLE / "1-pali-sample.md").write_text("\n".join(excerpt) + "\n", encoding="utf-8", newline="\n")
    print("wrote", SAMPLE / "1-pali-sample.md", n - 1, "non-empty lines")
    emit(excerpt, build_sample(), SAMPLE / "1-sample.md")
    (RAILS / "hi-rails-formulas.md").write_text(formulas_md(), encoding="utf-8", newline="\n")
    print("wrote", RAILS / "hi-rails-formulas.md")


if __name__ == "__main__":
    main()
