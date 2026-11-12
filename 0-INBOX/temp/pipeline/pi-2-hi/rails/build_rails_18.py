"""Builder for the Hindi rails translation of pi-2 chapter 18 (Dhammahadayavibhaṅga), plain audience.

Imports the approved sample builder read-only (constants and emit()); writes only
AI_translation/hindi/pi-2-hindi-plain-rails_split_chapters/18-dhammahadayavibhango.md

usage: python -I -X utf8 build_rails_18.py
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only import)

NAME = "18-dhammahadayavibhango.md"
TITLE = "परिघटनाओं के सार का विश्लेषण"  # approved chapter title


def lst(items):
    """A, B, C और D"""
    items = list(items)
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " और " + items[-1]


# =========================================================================== names
KH = [S.KH[k] for k in S.ORDER]
_AY = ["आँख", "दृश्य रूप", "कान", "ध्वनि", "नाक", "गंध", "जीभ", "स्वाद", "शरीर", "स्पर्श", "मन", "मन के विषयों"]
AY = {k: f"{v} का इंद्रिय-क्षेत्र" for k, v in zip(
    ["cakkhu", "rupa", "sota", "sadda", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana", "dhamma"], _AY)}
AY12 = list(AY.values())
DH = {}
for org, obj, s in [("cakkhu", "rupa", "आँख"), ("sota", "sadda", "कान"), ("ghana", "gandha", "नाक"),
                    ("jivha", "rasa", "जीभ"), ("kaya", "photthabba", "शरीर")]:
    DH[org] = f"{s} का तत्व"
    DH[obj] = AY[obj].replace("इंद्रिय-क्षेत्र", "तत्व")
    DH[org + "v"] = f"{s} की चेतना का तत्व"
DH["mano"] = "मन का तत्व"
DH["dhamma"] = "मन के विषयों का तत्व"
DH["manov"] = "मन की चेतना का तत्व"
DH18 = [DH[k] for k in ["cakkhu", "rupa", "cakkhuv", "sota", "sadda", "sotav", "ghana", "gandha", "ghanav",
                        "jivha", "rasa", "jivhav", "kaya", "photthabba", "kayav", "mano", "dhamma", "manov"]]
SC = {"dukkha": "दुःख का सत्य", "samudaya": "उत्पत्ति का सत्य", "nirodha": "दुःख के अंत का सत्य",
      "magga": "मार्ग का सत्य"}
IN = {"cakkhu": "आँख की क्षमता", "sota": "कान की क्षमता", "ghana": "नाक की क्षमता", "jivha": "जीभ की क्षमता",
      "kaya": "शरीर की क्षमता", "mana": "मन की क्षमता", "itthi": "स्त्रीत्व की क्षमता",
      "purisa": "पुरुषत्व की क्षमता", "jivita": "जीवन-क्षमता", "sukha": "सुख की क्षमता", "dukkha": "दुःख की क्षमता",
      "somanassa": "प्रसन्नता की क्षमता", "domanassa": "उदासी की क्षमता", "upekkha": "समभाव की क्षमता",
      "saddha": "श्रद्धा की क्षमता", "viriya": "उत्साह की क्षमता", "sati": "सजगता की क्षमता",
      "samadhi": "एकाग्रता की क्षमता", "panna": "प्रज्ञा की क्षमता",
      "anannata": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता", "anna": "पूर्ण ज्ञान की क्षमता",
      "annatavi": "पूर्ण ज्ञान पा चुके की क्षमता"}
IN22 = list(IN.values())
FOOD = "कौर-कौर खाया जाने वाला भोजन"
AH3 = ["संपर्क रूपी आहार", "मानसिक इरादा रूपी आहार", "चेतना रूपी आहार"]
SENSE5 = ["आँख", "कान", "नाक", "जीभ", "शरीर"]
PH7 = [f"{s} का संपर्क" for s in SENSE5] + ["मन के तत्व का संपर्क", "मन की चेतना के तत्व का संपर्क"]
MANOV_PH = "मन की चेतना के तत्व का संपर्क"


def born7(x):
    return [f"{s} के संपर्क से उत्पन्न {x}" for s in SENSE5] + [
        f"मन के तत्व के संपर्क से उत्पन्न {x}", f"मन की चेतना के तत्व के संपर्क से उत्पन्न {x}"]


CI7 = [f"{s} की चेतना" for s in SENSE5] + [DH["mano"], DH["manov"]]
ABY_HETU = ("हितकर कर्म के फल रूपी परिघटनाओं में, या केवल क्रिया रूपी, नैतिक रूप से अनिर्धारित परिघटनाओं में "
            "लोभ का अभाव, द्वेष का अभाव, मोह का अभाव – ये तीन नैतिक रूप से अनिर्धारित मूल हैं।")  # pi-1 ^1-1068

# category: (count noun sg, count noun pl, gender, kati word)
CAT = {
    "kh": ("समूह", "समूह", "m"), "ay": ("इंद्रिय-क्षेत्र", "इंद्रिय-क्षेत्र", "m"), "dh": ("तत्व", "तत्व", "m"),
    "sc": ("सत्य", "सत्य", "m"), "in": ("क्षमता", "क्षमताएँ", "f"), "he": ("मूल", "मूल", "m"),
    "ah": ("आहार", "आहार", "m"), "ph": ("संपर्क", "संपर्क", "m"), "ve": ("अनुभूति", "अनुभूतियाँ", "f"),
    "sa": ("पहचान", "पहचानें", "f"), "ce": ("इरादा", "इरादे", "m"), "ci": ("मन", "मन", "m"),
}
OBL = {"kh": "समूहों", "ay": "इंद्रिय-क्षेत्रों", "dh": "तत्वों", "sc": "सत्यों", "in": "क्षमताओं", "he": "मूलों",
       "ah": "आहारों", "ph": "संपर्कों", "ve": "अनुभूतियों", "sa": "पहचानों", "ce": "इरादों", "ci": "मनों"}
ORDER12 = ["kh", "ay", "dh", "sc", "in", "he", "ah", "ph", "ve", "sa", "ce", "ci"]
NUMW = {1: "एक", 2: "दो", 3: "तीन", 4: "चार", 5: "पाँच", 6: "छह", 7: "सात", 8: "आठ", 9: "नौ", 10: "दस",
        11: "ग्यारह", 12: "बारह", 13: "तेरह", 14: "चौदह", 15: "पंद्रह", 16: "सोलह", 18: "अठारह", 22: "बाईस"}


def cnt(c, n):
    sg, pl, _ = CAT[c]
    return f"{NUMW[n]} {sg if n == 1 else pl}"


def kati(c):
    sg, pl, g = CAT[c]
    return f"{'कितनी' if g == 'f' else 'कितने'} {pl}"


def g_of(c, n):
    return CAT[c][2] + ("s" if n == 1 else "p")


# =========================================================================== agreement
TOK = {
    "{a}": {"ms": "ा", "mp": "े", "fs": "ी", "fp": "ी"},
    "{u}": {"ms": "आ", "mp": "ए", "fs": "ई", "fp": "ई"},
    "{ya}": {"ms": "या", "mp": "ए", "fs": "ई", "fp": "ई"},
    "{kiya}": {"ms": "किया", "mp": "किए", "fs": "की", "fp": "की"},
    "{ka}": {"ms": "का", "mp": "के", "fs": "की", "fp": "की"},
}
HAI = {"ms": "है", "mp": "हैं", "fs": "है", "fp": "हैं"}
HOTA = {"ms": "होता है", "mp": "होते हैं", "fs": "होती है", "fp": "होती हैं"}
HOTA_NEG = {"ms": "नहीं होता", "mp": "नहीं होते", "fs": "नहीं होती", "fp": "नहीं होतीं"}
PRON = {"ms": "उसे", "fs": "उसे", "mp": "इन्हें", "fp": "इन्हें"}


def agr(t, g):
    for k, v in TOK.items():
        t = t.replace(k, v[g])
    return t


def pred(kind, payload, g):
    if kind == "is":
        return f"{agr(payload, g)} {HAI[g]}"
    if kind == "not":
        return f"{agr(payload, g)} नहीं {HAI[g]}"
    if kind == "neg":  # na X na Y na Z
        ps = [agr(p, g) for p in payload]
        return f"न {ps[0]} {HAI[g]}" + "".join(f", न {p}" for p in ps[1:])
    if kind == "siya":
        return f"कभी {agr(payload, g)} {HOTA[g]}"
    if kind == "siyanot":
        return f"कभी {agr(payload, g)} {HOTA_NEG[g]}"
    if kind == "siyaneg":  # siyā na X na Y na Z
        ps = [agr(p, g) for p in payload]
        return f"कभी न {ps[0]} {HOTA[g]}" + "".join(f", न {p}" for p in ps[1:])
    if kind in ("nv", "siyanv"):
        return nv(PRON[g], payload, g, siya=(kind == "siyanv"))
    raise ValueError(kind)


def nv(obj, items, g, siya=False):
    """na vattabbā X-tipi, Y-tipi, Z-tipi"""
    ps = [agr(p, g) for p in items]
    pre = "कभी " if siya else ""
    if len(ps) == 1:
        return f"{pre}{obj} {ps[0]} नहीं कहा जा सकता"
    if ps[-1].startswith("न "):  # the third member itself starts with न (pi-1 ^1-1389 shape)
        mid = "".join(f", न {p}" for p in ps[1:-1])
        return f"{pre}{obj} न {ps[0]} कहा जा सकता है{mid}, और {PRON[g]} {ps[-1]} भी नहीं कहा जा सकता"
    return f"{pre}{obj} न {ps[0]} कहा जा सकता है" + "".join(f", न {p}" for p in ps[1:])


def sent(subj, g, *parts, obl=None):
    """One Pāli sentence: subject + predicates joined by commas. A leading nv uses the oblique subject."""
    if parts and parts[0][0] == "nv":
        first = nv(f"{obl} को", parts[0][1], g)
        rest = [pred(k, p, g) for k, p in parts[1:]]
        return ", ".join([first] + rest)
    return f"{subj} " + ", ".join(pred(k, p, g) for k, p in parts)


# subjects: (text, gender, oblique)
def subj(c, n, text=None):
    g = g_of(c, n)
    t = text or cnt(c, n)
    o = None if n == 1 else f"{NUMW[n]} {OBL[c]}"
    return t, g, o


def one(text, g):
    obl = None
    if g[1] == "s":
        obl = text
        if text == FOOD:
            obl = "कौर-कौर खाए जाने वाले भोजन"
        elif g == "ms" and " का " in text:
            i = text.rfind(" का ")
            obl = text[:i] + " के " + text[i + 4:]
    return text, g, obl


R_KH = one(S.KH["rupa"], "ms")
SAN_KH = one(S.KH["sankhara"], "ms")
MANAY = one(AY["mana"], "ms")
DHAY = one(AY["dhamma"], "ms")
SADDAY = one(AY["sadda"], "ms")
DHDH = one(DH["dhamma"], "ms")
MANODH = one(DH["mano"], "ms")
MANOVDH = one(DH["manov"], "ms")
KAYAVDH = one(DH["kayav"], "ms")
SADDADH = one(DH["sadda"], "ms")
FOOD_S = one(FOOD, "ms")
MANOV_PH_S = one(MANOV_PH, "ms")
MANO_PH_S = one("मन के तत्व का संपर्क", "ms")
KAYAV_PH_S = one("शरीर की चेतना के तत्व का संपर्क", "ms")
JIVITA = one(IN["jivita"], "fs")
DUK_SC = one(SC["dukkha"], "ms")
SAM_SC = one(SC["samudaya"], "ms")
NIR_SC = one(SC["nirodha"], "ms")
MAG_SC = one(SC["magga"], "ms")


def chain(first_items, last_g):
    """Cha vedanā…pe… cha saññā… cha cetanā… cha cittā (subject chain; agreement with the last member)"""
    return "… ".join(first_items), last_g, None


def S_(sb, *parts):
    t, g, o = sb
    return sent(t, g, *parts, obl=o)


# =========================================================================== section 1 + 2: counts and lists
def kati_q(prefix="", verb="", pe=None):
    """Kati khandhā, kati āyatanāni, … kati cittāni?  pe = index after which …pe… stands (list cut)"""
    def item(i, c):
        return f"{kati(c)}{verb}"
    cats = ORDER12
    if pe is None:
        parts = [item(i, c) for i, c in enumerate(cats)]
        parts[0] = f"{kati(cats[0])} {'हैं' if not verb else verb.strip()}" if not verb else parts[0]
        return f"{prefix}{', '.join(parts)}?"
    raise NotImplementedError


def counts(nums, prefix="", verb=""):
    parts = [cnt(c, n) for c, n in zip(ORDER12, nums)]
    return f"{prefix}{lst(parts)}{verb}।"


def what_q(np_, c, n):
    g = g_of(c, n)
    if n == 1:
        return f"यहाँ {np_} क्या है?"
    return f"यहाँ {np_} {'कौन-सी' if g == 'fp' else 'कौन-से'} हैं?"


def called(np_, c, n, quote=True):
    g = g_of(c, n)
    q = f"“{np_}”" if quote else np_
    if n == 1:
        return f"यह {q} {'कही जाती है' if g == 'fs' else 'कहा जाता है'}।"
    return f"ये {q} {'कही जाती हैं' if g == 'fp' else 'कहे जाते हैं'}।"


def define(np_, c, n, items, dash=True):
    return f"{what_q(np_, c, n)} {lst(items)} – {called(np_, c, n)}"


def gen(loc, c, n):
    """genitive of a realm before the counted noun: X के/की/का"""
    g = g_of(c, n)
    return f"{loc} {'का' if g == 'ms' else 'के' if g == 'mp' else 'की'}"


# realms
KAMA = "इंद्रिय-सुखों के लोक"
RUPA = "सूक्ष्म भौतिक लोक"
ARUPA = "अभौतिक लोक"
APAR = "अस्तित्व के लोकों में न समाई हुई परिघटनाओं"

KATI_ALL = ("कितने समूह हैं, कितने इंद्रिय-क्षेत्र, कितने तत्व, कितने सत्य, कितनी क्षमताएँ, कितने मूल, कितने आहार, "
            "कितने संपर्क, कितनी अनुभूतियाँ, कितनी पहचानें, कितने इरादे, कितने मन?")


def hetu_lines(realm, n_ak, kusala_vip_only=False, total=None, quote=True):
    """the hetu sub-block (several lines)"""
    pass


def realm_list_line(realm, c, n, items, pe_items=None, quote=True):
    np_ = f"{gen(realm, c, n)} {cnt(c, n)}"
    body = lst(items) if pe_items is None else pe_items
    return f"{what_q(np_, c, n)} {body} – {called(np_, c, n, quote)}"


# =========================================================================== predicates (pi-1 matika item names)
KUS, AKUS, ABY = "हितकर", "हानिकर", "नैतिक रूप से अनिर्धारित"
SUKHA_S = "सुखद अनुभूति से जुड़{a}"
DUKKHA_S = "दुःखद अनुभूति से जुड़{a}"
ADM_S = "न दुःखद, न सुखद अनुभूति से जुड़{a}"
VIP = "कर्म-फल रूपी"
VIPD = "कर्म-फल उत्पन्न करने वाल{a}"
NVIP = "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाल{a}"
UU = "कर्म से उत्पन्न और आसक्ति का विषय बनने वाल{a}"
AU = "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाल{a}"
AA = "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाल{a}"
SVSV = "आरंभिक विचार और सतत विचार वाल{a}"
AVVM = "आरंभिक विचार से रहित, केवल सतत विचार वाल{a}"
AVAV = "आरंभिक विचार और सतत विचार दोनों से रहित"
SAR = "विषय वाल{a}"
ANAR = "विषय से रहित"
SARAR = "विषय वाली परिघटनाओं को विषय बनाने वाल{a}"
ANARAR = "विषय से रहित परिघटनाओं को विषय बनाने वाल{a}"
DIT, SUT, MUT, VINN = "देख{a} हु{u}", "सुन{a} हु{u}", "अनुभव {kiya} हु{u}", "जान{a} हु{u}"
ABH, PAR = "प्रत्यक्ष जानने योग्य", "पूरी तरह समझे जाने योग्य"
PAH, BHAV, SACC = "छोड़{a} जाने वाल{a}", "अभ्यास किए जाने योग्य", "साक्षात्कार करने योग्य"


def inr(realm):
    return f"{realm} में समा{{ya}} हु{{u}}"


PARI = inr("अस्तित्व के लोकों")
APARI = "अस्तित्व के लोकों में न समा{ya} हु{u}"


# =========================================================================== build
def build():
    h = {}
    h["2-18-0"] = [f"### {TITLE}"]

    # ------------------------------------------------ 1. Sabbasaṅgāhikavāra
    h["2-18-1-0"] = ["#### सब कुछ समेटने वाला खंड"]
    h["2-978"] = [KATI_ALL, counts([5, 12, 18, 4, 22, 9, 4, 7, 7, 7, 7, 7])]
    h["2-979"] = [define("पाँच समूह", "kh", 5, KH)]
    h["2-980"] = [define("बारह इंद्रिय-क्षेत्र", "ay", 12, AY12)]
    h["2-981"] = [define("अठारह तत्व", "dh", 18, DH18)]
    h["2-982"] = [define("चार सत्य", "sc", 4, list(SC.values()))]
    h["2-983"] = [define("बाईस क्षमताएँ", "in", 22, IN22)]
    h["2-984"] = [
        "यहाँ नौ मूल कौन-से हैं? तीन हितकर मूल, तीन हानिकर मूल, तीन नैतिक रूप से अनिर्धारित मूल।",
        "यहाँ तीन हितकर मूल कौन-से हैं? लोभ का अभाव हितकर मूल, द्वेष का अभाव हितकर मूल, मोह का अभाव हितकर मूल – "
        "ये तीन हितकर मूल हैं।",
        "यहाँ तीन हानिकर मूल कौन-से हैं? लोभ हानिकर मूल, द्वेष हानिकर मूल, मोह हानिकर मूल – ये तीन हानिकर मूल हैं।",
        f"यहाँ तीन नैतिक रूप से अनिर्धारित मूल कौन-से हैं? {ABY_HETU} ये “नौ मूल” कहे जाते हैं।",
    ]
    h["2-985"] = [define("चार आहार", "ah", 4, [f"{FOOD} [वर्तनी-भेद (Sī., Syā.): kabaḷiṃkāro āhāro]"] + AH3)]
    h["2-986"] = [define("सात संपर्क", "ph", 7, PH7)]
    h["2-987"] = [define("सात अनुभूतियाँ", "ve", 7, born7("अनुभूति"))]
    h["2-988"] = [define("सात पहचानें", "sa", 7, born7("पहचान"))]
    h["2-989"] = [define("सात इरादे", "ce", 7, born7("इरादा"))]
    h["2-990"] = [define("सात मन", "ci", 7, CI7)]

    # ------------------------------------------------ 2. Uppattānuppattivāra
    h["2-18-2-0"] = ["#### होने और न होने का खंड"]

    def L(realm, c, n, items, quote=True):
        return realm_list_line(realm, c, n, items, quote=quote)

    # Kāmadhātu
    h["2-18-2-1-0"] = ["##### इंद्रिय-सुखों का लोक"]
    h["2-991"] = [f"{KAMA} में {KATI_ALL}", counts([5, 12, 18, 3, 22, 9, 4, 7, 7, 7, 7, 7], f"{KAMA} में ", " हैं")]
    k = KAMA
    h["2-992"] = [
        L(k, "kh", 5, KH), L(k, "ay", 12, AY12), L(k, "dh", 18, DH18),
        L(k, "sc", 3, [SC["dukkha"], SC["samudaya"], SC["magga"]]),
        f"{what_q(gen(k, 'in', 22) + ' बाईस क्षमताएँ', 'in', 22)} {IN['cakkhu']}, {IN['sota']}… {IN['annatavi']} – "
        f"{called(gen(k, 'in', 22) + ' बाईस क्षमताएँ', 'in', 22)}",
        f"{what_q(gen(k, 'he', 9) + ' नौ मूल', 'he', 9)} तीन हितकर मूल, तीन हानिकर मूल, तीन नैतिक रूप से अनिर्धारित मूल… "
        f"{called(gen(k, 'he', 9) + ' नौ मूल', 'he', 9)}",
        L(k, "ah", 4, [FOOD] + AH3), L(k, "ph", 7, PH7), L(k, "ve", 7, born7("अनुभूति")),
        L(k, "sa", 7, born7("पहचान")), L(k, "ce", 7, born7("इरादा")), L(k, "ci", 7, CI7),
    ]
    # Rūpadhātu
    h["2-18-2-2-0"] = [f"##### {RUPA}"]
    r = RUPA
    h["2-993"] = [f"{r} में कितने समूह हैं, कितने इंद्रिय-क्षेत्र, कितने तत्व, कितने सत्य, कितनी क्षमताएँ… कितने मन?",
                  counts([5, 6, 9, 3, 14, 8, 3, 4, 4, 4, 4, 4], f"{r} में ", " हैं")]
    h["2-994"] = [
        L(r, "kh", 5, KH),
        L(r, "ay", 6, [AY["cakkhu"], AY["rupa"], AY["sota"], AY["sadda"], AY["mana"], AY["dhamma"]]),
        L(r, "dh", 9, [DH[x] for x in ["cakkhu", "rupa", "cakkhuv", "sota", "sadda", "sotav", "mano", "dhamma", "manov"]]),
        L(r, "sc", 3, [SC["dukkha"], SC["samudaya"], SC["magga"]]),
        L(r, "in", 14, [IN[x] for x in ["cakkhu", "sota", "mana", "jivita", "somanassa", "upekkha", "saddha", "viriya",
                                         "sati", "samadhi", "panna", "anannata", "anna", "annatavi"]]),
        f"{what_q(gen(r, 'he', 8) + ' आठ मूल', 'he', 8)} तीन हितकर मूल, दो हानिकर मूल, तीन नैतिक रूप से अनिर्धारित मूल।",
        "यहाँ तीन हितकर मूल कौन-से हैं? लोभ का अभाव हितकर मूल, द्वेष का अभाव हितकर मूल, मोह का अभाव हितकर मूल – "
        "ये तीन हितकर मूल हैं।",
        "यहाँ दो हानिकर मूल कौन-से हैं? लोभ हानिकर मूल, मोह हानिकर मूल – ये दो हानिकर मूल हैं।",
        f"यहाँ तीन नैतिक रूप से अनिर्धारित मूल कौन-से हैं? {ABY_HETU} "
        f"{called(gen(r, 'he', 8) + ' आठ मूल', 'he', 8, quote=False)}",
        L(r, "ah", 3, AH3),
        L(r, "ph", 4, [PH7[0], PH7[1], PH7[5], PH7[6]]),
        f"यहाँ {r} की चार अनुभूतियाँ… चार पहचानें… चार इरादे… चार मन कौन-से हैं? "
        f"{lst([CI7[0], CI7[1], CI7[5], CI7[6]])} – {called(gen(r, 'ci', 4) + ' चार मन', 'ci', 4)}",
    ]
    # Arūpadhātu
    h["2-18-2-3-0"] = [f"##### {ARUPA}"]
    a = ARUPA
    h["2-995"] = [f"{a} में कितने समूह हैं… कितने मन?",
                  counts([4, 2, 2, 3, 11, 8, 3, 1, 1, 1, 1, 1], f"{a} में ", " हैं")]
    IN11 = [IN[x] for x in ["mana", "jivita", "somanassa", "upekkha", "saddha", "viriya", "sati", "samadhi", "panna",
                            "anna", "annatavi"]]
    h["2-996"] = [
        L(a, "kh", 4, KH[1:]),
        L(a, "ay", 2, [AY["mana"], AY["dhamma"]]),
        L(a, "dh", 2, [DH["manov"], DH["dhamma"]]),
        L(a, "sc", 3, [SC["dukkha"], SC["samudaya"], SC["magga"]]),
        L(a, "in", 11, IN11),
        f"{what_q(gen(a, 'he', 8) + ' आठ मूल', 'he', 8)} तीन हितकर मूल, दो हानिकर मूल, तीन नैतिक रूप से अनिर्धारित मूल… "
        f"{called(gen(a, 'he', 8) + ' आठ मूल', 'he', 8)}",
        L(a, "ah", 3, AH3),
        L(a, "ph", 1, [MANOV_PH]),
        f"यहाँ {a} की एक अनुभूति… एक पहचान… एक इरादा… एक मन क्या है? {DH['manov']} – "
        f"{called(gen(a, 'ci', 1) + ' एक मन', 'ci', 1)}",
    ]
    # Apariyāpanna
    h["2-18-2-4-0"] = ["##### अस्तित्व के लोकों में न समाया हुआ"]
    p = APAR
    h["2-997"] = [f"{p} में कितने समूह हैं… कितने मन?",
                  counts([4, 2, 2, 2, 12, 6, 3, 1, 1, 1, 1, 1], f"{p} में ", " हैं")]
    h["2-998"] = [
        L(p, "kh", 4, KH[1:]),
        L(p, "ay", 2, [AY["mana"], AY["dhamma"]]),
        L(p, "dh", 2, [DH["manov"], DH["dhamma"]]),
        L(p, "sc", 2, [SC["magga"], SC["nirodha"]]),
        L(p, "in", 12, IN11[:9] + [IN["anannata"], IN["anna"], IN["annatavi"]]),
        f"{what_q(gen(p, 'he', 6) + ' छह मूल', 'he', 6)} तीन हितकर मूल, तीन नैतिक रूप से अनिर्धारित मूल।",
        "यहाँ तीन हितकर मूल कौन-से हैं? लोभ का अभाव हितकर मूल, द्वेष का अभाव हितकर मूल, मोह का अभाव हितकर मूल – "
        "ये तीन हितकर मूल हैं।",
        "यहाँ तीन नैतिक रूप से अनिर्धारित मूल कौन-से हैं? हितकर कर्म के फल रूपी परिघटनाओं में लोभ का अभाव, "
        "द्वेष का अभाव, मोह का अभाव – ये तीन नैतिक रूप से अनिर्धारित मूल हैं। "
        f"{called(gen(p, 'he', 6) + ' छह मूल', 'he', 6)}",
        L(p, "ah", 3, AH3),
        L(p, "ph", 1, [MANOV_PH]),
        f"यहाँ {p} की एक अनुभूति… एक पहचान… एक इरादा… एक मन क्या है? {DH['manov']} – "
        f"{called(gen(p, 'ci', 1) + ' एक मन', 'ci', 1)}",
    ]

    # ------------------------------------------------ 3. Pariyāpannāpariyāpannavāra
    h["2-18-3-0"] = ["#### समाए हुए और न समाए हुए का खंड"]

    def kq(x, y):
        return (f"पाँच समूहों में से कितने {x} हैं, कितने {y} हैं… सात मनों में से कितने {x} हैं, "
                f"कितने {y} हैं?")

    def realm_block(realm, neg_first):
        IN_ = agr  # alias
        pr = inr(realm)
        first = "not" if neg_first else "is"
        sy = [("siya", pr), ("siyanot", pr)]
        return pr, first, sy

    for hid, qid, aid, realm in [("2-18-3-1-0", "2-999", "2-1000", KAMA), ("2-18-3-2-0", "2-1001", "2-1002", RUPA),
                                 ("2-18-3-3-0", "2-1003", "2-1004", ARUPA)]:
        pr = inr(realm)
        h[hid] = [{"2-999": "##### इंद्रिय-सुखों का लोक", "2-1001": f"##### {RUPA}", "2-1003": f"##### {ARUPA}"}[qid]]
        yes_s, no_s = agr(pr, "mp"), agr(pr, "mp") + " नहीं"
        h[qid] = [kq(yes_s, no_s)]
        sy = [("siya", pr), ("siyanot", pr)]
        f = "is" if realm == KAMA else "not"  # the first member: included (kāma) / not included (rūpa, arūpa)
        lines = [
            f"{S_(R_KH, (f, pr))}; {S_(subj('kh', 4), *sy)}।",
            f"{S_(subj('ay', 10), (f, pr))}; {S_(subj('ay', 2), *sy)}।",
            f"{S_(subj('dh', 16), (f, pr))}; {S_(subj('dh', 2), *sy)}।",
        ]
        if realm == KAMA:
            lines.append(f"{S_(SAM_SC, ('is', pr))}; {S_(subj('sc', 2), ('not', pr))}; {S_(DUK_SC, *sy)}।")
            lines.append(f"{S_(subj('in', 10), ('is', pr))}; {S_(subj('in', 3), ('not', pr))}; "
                         f"{S_(subj('in', 9), *sy)}।")
        elif realm == RUPA:
            lines.append(f"{S_(subj('sc', 3), ('not', pr))}; {S_(DUK_SC, *sy)}।")
            lines.append(f"{S_(subj('in', 13), ('not', pr))}; {S_(subj('in', 9), *sy)}।")
        else:
            lines.append(f"{S_(subj('sc', 3), ('not', pr))}।")
            lines.append(f"{S_(DUK_SC, *sy)}।")
            lines.append(f"{S_(subj('in', 14), ('not', pr))}; {S_(subj('in', 8), *sy)}।")
        lines += [
            f"{S_(subj('he', 3, 'तीन हानिकर मूल'), (f, pr))}; {S_(subj('he', 6), *sy)}।",
            f"{S_(FOOD_S, (f, pr))}; {S_(subj('ah', 3), *sy)}।",
            f"{S_(subj('ph', 6), (f, pr))}; {S_(MANOV_PH_S, *sy)}।",
            f"{S_(chain(['छह अनुभूतियाँ', 'छह पहचानें', 'छह इरादे', 'छह मन'], 'mp'), (f, pr))}; {S_(MANOVDH, *sy)}।",
        ]
        h[aid] = lines
    # Pariyāpanna / apariyāpanna
    h["2-18-3-4-0"] = ["##### समाया हुआ और न समाया हुआ"]
    h["2-1005"] = [kq(agr(PARI, "mp"), agr(APARI, "mp"))]
    sy = [("siya", PARI), ("siya", APARI)]
    h["2-1006"] = [
        f"{S_(R_KH, ('is', PARI))}; {S_(subj('kh', 4), *sy)}।",
        f"{S_(subj('ay', 10), ('is', PARI))}; {S_(subj('ay', 2), *sy)}।",
        f"{S_(subj('dh', 16), ('is', PARI))}; {S_(subj('dh', 2), *sy)}।",
        f"{S_(subj('sc', 2), ('is', PARI))}; {S_(subj('sc', 2), ('is', APARI))}।",
        f"{S_(subj('in', 10), ('is', PARI))}, {S_(subj('in', 3), ('is', APARI))}; {S_(subj('in', 9), *sy)}।",
        f"{S_(subj('he', 3, 'तीन हानिकर मूल'), ('is', PARI))}; {S_(subj('he', 6), *sy)}।",
        f"{S_(FOOD_S, ('is', PARI))}; {S_(subj('ah', 3), *sy)}।",
        f"{S_(subj('ph', 6), ('is', PARI))}; {S_(MANOV_PH_S, *sy)}।",
        f"{S_(chain(['छह अनुभूतियाँ', 'छह पहचानें', 'छह इरादे', 'छह मन'], 'mp'), ('is', PARI))}; {S_(MANOVDH, *sy)}।",
    ]

    # ------------------------------------------------ 4. Dhammadassanavāra
    h["2-18-4-0"] = ["#### परिघटनाओं को दिखाने वाला खंड"]
    h["2-18-4-1-0"] = ["##### इंद्रिय-सुखों का लोक"]
    KU = f"{KAMA} में जन्म के क्षण"
    APP = "प्रकट होते हैं"

    def appear(c, n):
        g = g_of(c, n)
        return {"ms": "प्रकट होता है", "mp": "प्रकट होते हैं", "fs": "प्रकट होती है", "fp": "प्रकट होती हैं"}[g]

    def kas(c, n, other=False):
        o = ("दूसरी " if CAT[c][2] == "f" else "दूसरे ") if other else ""
        return f"किसी के लिए {o}{cnt(c, n)} {appear(c, n)}"

    parts = [f"सबके लिए पाँच समूह {APP}"]
    parts += [kas("ay", 11), kas("ay", 10), kas("ay", 10, True), kas("ay", 9), kas("ay", 7)]
    parts += [kas("dh", 11), kas("dh", 10), kas("dh", 10, True), kas("dh", 9), kas("dh", 7)]
    parts += ["सबके लिए एक सत्य प्रकट होता है"]
    parts += [kas("in", 14), kas("in", 13), kas("in", 13, True), kas("in", 12), kas("in", 10), kas("in", 9),
              kas("in", 9, True), kas("in", 8), kas("in", 8, True), kas("in", 7), kas("in", 5), kas("in", 4)]
    parts += [kas("he", 3), kas("he", 2),
              "किसी के लिए [पाठभेद (Syā.): keci] मूल से रहित परिघटनाएँ प्रकट होती हैं",
              f"सबके लिए चार आहार {APP}", "सबके लिए एक संपर्क प्रकट होता है",
              "सबके लिए एक अनुभूति… एक पहचान… एक इरादा… एक मन प्रकट होता है"]
    h["2-1007"] = [f"{KU} कितने समूह {APP}… कितने मन {APP}?", f"{KU} " + "; ".join(parts) + "।"]
    h["2-1008"] = [f"{KU} सबके लिए कौन-से पाँच समूह {APP}? {KH[0]}… {KH[-1]} – {KU} सबके लिए ये पाँच समूह {APP}।"]

    DEVA = "इंद्रिय-सुखों के लोक से संबंधित देवताओं"
    FIRST = "कल्प के आरंभ के मनुष्यों"
    OPA4 = "स्वतः जन्म लेने वाले प्रेतों, स्वतः जन्म लेने वाले असुरों, स्वतः जन्म लेने वाले पशुओं और नरक के प्राणियों"
    WOMB = "गर्भ में रहने वाले प्राणियों"

    def who(groups, qual=None):
        g = lst(groups)
        if qual:
            return f"{g} में से जो {qual} हों, उनके लिए"
        return f"{g} के लिए"

    def birth(c, n, other, whom, items, ):
        o = ("दूसरी " if CAT[c][2] == "f" else "दूसरे ") if other else ""
        q = f"{KU} किसके लिए {o}{cnt(c, n)} {appear(c, n)}?"
        a = f"{whom} जन्म के क्षण {cnt(c, n)} {appear(c, n)} – {lst(items)}।"
        z = f"{KU} इनके लिए ये {cnt(c, n)} {appear(c, n)}।"
        return f"{q} {a} {z}"

    FULL = "पूर्ण इंद्रिय-क्षेत्रों वाले"
    BL, DF, BD = "जन्म से अंधे", "जन्म से बहरे", "जन्म से अंधे और बहरे"
    ay = AY
    h["2-1009"] = [
        birth("ay", 11, False, who([DEVA, FIRST, OPA4], FULL),
              [ay[x] for x in ["cakkhu", "rupa", "sota", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana", "dhamma"]]),
        birth("ay", 10, False, who([OPA4], BL),
              [ay[x] for x in ["rupa", "sota", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana", "dhamma"]]),
        birth("ay", 10, True, who([OPA4], DF),
              [ay[x] for x in ["cakkhu", "rupa", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana", "dhamma"]]),
        birth("ay", 9, False, who([OPA4], BD),
              [ay[x] for x in ["rupa", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana", "dhamma"]]),
        birth("ay", 7, False, who([WOMB]),
              [ay[x] for x in ["rupa", "gandha", "rasa", "kaya", "photthabba", "mana", "dhamma"]]),
    ]
    dh = DH
    h["2-1010"] = [
        birth("dh", 11, False, who([DEVA, FIRST, OPA4], FULL),
              [dh[x] for x in ["cakkhu", "rupa", "sota", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "manov", "dhamma"]]),
        birth("dh", 10, False, who([OPA4], BL),
              [dh[x] for x in ["rupa", "sota", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "manov", "dhamma"]]),
        birth("dh", 10, True, who([OPA4], DF),
              [dh[x] for x in ["cakkhu", "rupa", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "manov", "dhamma"]]),
        birth("dh", 9, False, who([OPA4], BD),
              [dh[x] for x in ["rupa", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "manov", "dhamma"]]),
        birth("dh", 7, False, who([WOMB]),
              [dh[x] for x in ["rupa", "gandha", "rasa", "kaya", "photthabba", "manov", "dhamma"]]),
    ]
    h["2-1011"] = [f"{KU} सबके लिए कौन-सा एक सत्य प्रकट होता है? {SC['dukkha']} – "
                   f"{KU} सबके लिए यह एक सत्य प्रकट होता है।"]
    SEX = "स्त्रीत्व की क्षमता या पुरुषत्व की क्षमता"
    FEEL = "प्रसन्नता की क्षमता या समभाव की क्षमता"
    i = IN
    SENSES5 = [i["cakkhu"], i["sota"], i["ghana"], i["jivha"], i["kaya"]]
    FAITH4 = [i["saddha"], i["viriya"], i["sati"], i["samadhi"]]
    RN, RF = "मूल वाले और ज्ञान से जुड़े", "मूल वाले और ज्ञान से अलग"
    h["2-1012"] = [
        birth("in", 14, False, who([DEVA], RN), SENSES5 + [i["mana"], SEX, i["jivita"], FEEL] + FAITH4 + [i["panna"]]),
        birth("in", 13, False, who([DEVA], RF), SENSES5 + [i["mana"], SEX, i["jivita"], FEEL] + FAITH4),
        birth("in", 13, True, who([FIRST], RN), SENSES5 + [i["mana"], i["jivita"], FEEL] + FAITH4 + [i["panna"]]),
        birth("in", 12, False, who([FIRST], RF), SENSES5 + [i["mana"], i["jivita"], FEEL] + FAITH4),
        birth("in", 10, False, who([WOMB], RN), [i["kaya"], i["mana"], SEX, i["jivita"], FEEL] + FAITH4 + [i["panna"]]),
        birth("in", 9, False, who([WOMB], RF), [i["kaya"], i["mana"], SEX, i["jivita"], FEEL] + FAITH4),
        birth("in", 9, True, who([OPA4], FULL), SENSES5 + [i["mana"], SEX, i["jivita"], i["upekkha"]]),
        birth("in", 8, False, who([OPA4], BL), SENSES5[1:] + [i["mana"], SEX, i["jivita"], i["upekkha"]]),
        birth("in", 8, True, who([OPA4], DF), [SENSES5[0]] + SENSES5[2:] + [i["mana"], SEX, i["jivita"], i["upekkha"]]),
        birth("in", 7, False, who([OPA4], BD), SENSES5[2:] + [i["mana"], SEX, i["jivita"], i["upekkha"]]),
        birth("in", 5, False, f"{WOMB} में से जो मूल से रहित हों, उनके लिए, नपुंसकों को छोड़कर,",
              [i["kaya"], i["mana"], SEX, i["jivita"], i["upekkha"]]),
        birth("in", 4, False, who([WOMB], "मूल से रहित और नपुंसक"),
              [i["kaya"], i["mana"], i["jivita"], i["upekkha"]]),
    ]
    VH = "कर्म-फल रूपी मूल"
    h["2-1013"] = [
        birth("he", 3, False, who([DEVA, FIRST, WOMB], RN),
              [f"लोभ का अभाव {VH}", f"द्वेष का अभाव {VH}", f"मोह का अभाव {VH}"]),
        birth("he", 2, False, who([DEVA, FIRST, WOMB], RF), [f"लोभ का अभाव {VH}", f"द्वेष का अभाव {VH}"])
        + " शेष प्राणियों के लिए [पाठभेद (?): avasesā sattā] मूल से रहित परिघटनाएँ प्रकट होती हैं।",
    ]
    h["2-1014"] = [
        f"{KU} सबके लिए कौन-से चार आहार {APP}? {lst([FOOD] + AH3)} – {KU} सबके लिए ये चार आहार {APP}।",
        f"{KU} सबके लिए कौन-सा एक संपर्क प्रकट होता है? {MANOV_PH} – {KU} सबके लिए यह एक संपर्क प्रकट होता है।",
        f"{KU} सबके लिए कौन-सी एक अनुभूति… एक पहचान… एक इरादा… एक मन प्रकट होता है? {DH['manov']} – "
        f"{KU} सबके लिए यह एक मन प्रकट होता है।",
    ]
    # Rūpadhātu
    h["2-18-4-2-0"] = [f"##### {RUPA}"]
    RU = f"{RUPA} में जन्म के क्षण"
    h["2-1015"] = [
        f"{RU} कितने समूह {APP}… कितने मन {APP}?",
        f"{RU}, पहचान-रहित देवताओं को छोड़कर, पाँच समूह {APP}, पाँच इंद्रिय-क्षेत्र {APP}, पाँच तत्व {APP}, "
        f"एक सत्य प्रकट होता है, दस क्षमताएँ प्रकट होती हैं, तीन मूल {APP}, तीन आहार {APP}, एक संपर्क प्रकट होता है, "
        f"एक अनुभूति… एक पहचान… एक इरादा… एक मन प्रकट होता है।",
    ]

    def which(prefix, c, n, items):
        np_ = cnt(c, n)
        g = g_of(c, n)
        kw = {"ms": "कौन-सा", "mp": "कौन-से", "fs": "कौन-सी", "fp": "कौन-सी"}[g]
        ye = "यह" if n == 1 else "ये"
        return f"{prefix} {kw} {np_} {appear(c, n)}? {lst(items)} – {prefix} {ye} {np_} {appear(c, n)}।"

    h["2-1016"] = [
        which(RU, "kh", 5, KH),
        which(RU, "ay", 5, [AY["cakkhu"], AY["rupa"], AY["sota"], AY["mana"], AY["dhamma"]]),
        which(RU, "dh", 5, [DH["cakkhu"], DH["rupa"], DH["sota"], DH["manov"], DH["dhamma"]]),
        which(RU, "sc", 1, [SC["dukkha"]]),
        which(RU, "in", 10, [i["cakkhu"], i["sota"], i["mana"], i["jivita"], FEEL] + FAITH4 + [i["panna"]]),
        which(RU, "he", 3, [f"लोभ का अभाव {VH}", f"द्वेष का अभाव {VH}", f"मोह का अभाव {VH}"]),
        which(RU, "ah", 3, AH3),
        which(RU, "ph", 1, [MANOV_PH]),
        f"{RU} कौन-सी एक अनुभूति… एक पहचान… एक इरादा… एक मन प्रकट होता है? {DH['manov']} – "
        f"{RU} यह एक मन प्रकट होता है।",
    ]
    # Asaññasattā
    h["2-18-4-3-0"] = ["##### पहचान-रहित प्राणी"]
    AS = "पहचान-रहित देवताओं के जन्म के क्षण"
    h["2-1017"] = [
        f"{AS} कितने समूह {APP}… कितने मन {APP}?",
        f"{AS} एक समूह प्रकट होता है – {KH[0]}; दो इंद्रिय-क्षेत्र {APP} – {lst([AY['rupa'], AY['dhamma']])}; "
        f"दो तत्व {APP} – {lst([DH['rupa'], DH['dhamma']])}; एक सत्य प्रकट होता है – {SC['dukkha']}; "
        f"एक क्षमता प्रकट होती है – भौतिक जीवन-क्षमता। पहचान-रहित देवता मूल से रहित, आहार से रहित, संपर्क से रहित, "
        f"अनुभूति से रहित, पहचान से रहित, इरादे से रहित और मन से रहित प्रकट होते हैं।",
    ]
    # Arūpadhātu
    h["2-18-4-4-0"] = [f"##### {ARUPA}"]
    AU_ = f"{ARUPA} में जन्म के क्षण"
    h["2-1018"] = [
        f"{AU_} कितने समूह {APP}… कितने मन {APP}?",
        f"{AU_} चार समूह {APP}, दो इंद्रिय-क्षेत्र {APP}, दो तत्व {APP}, एक सत्य प्रकट होता है, "
        f"आठ क्षमताएँ प्रकट होती हैं, तीन मूल {APP}, तीन आहार {APP}, एक संपर्क प्रकट होता है, "
        f"एक अनुभूति… एक पहचान… एक इरादा… एक मन प्रकट होता है।",
    ]
    h["2-1019"] = [
        which(AU_, "kh", 4, KH[1:]),
        which(AU_, "ay", 2, [AY["mana"], AY["dhamma"]]),
        which(AU_, "dh", 2, [DH["manov"], DH["dhamma"]]),
        which(AU_, "sc", 1, [SC["dukkha"]]),
        which(AU_, "in", 8, [i["mana"], i["jivita"], i["upekkha"]] + FAITH4 + [i["panna"]]),
        which(AU_, "he", 3, [f"लोभ का अभाव {VH}", f"द्वेष का अभाव {VH}", f"मोह का अभाव {VH}"]),
        which(AU_, "ah", 3, AH3),
        which(AU_, "ph", 1, [MANOV_PH]),
        f"{AU_} कौन-सी एक अनुभूति… एक पहचान… एक इरादा… एक मन प्रकट होता है? {DH['manov']} – "
        f"{AU_} यह एक मन प्रकट होता है।",
    ]

    # ------------------------------------------------ 5. Bhūmantaradassanavāra (pi-1 ^1-1287 … ^1-1294)
    h["2-18-5-0"] = ["#### अस्तित्व के स्तरों के भेद को दिखाने वाला खंड"]
    K_ = "इंद्रिय-सुखों के लोक से संबंधित"
    R_ = "सूक्ष्म भौतिक लोक से संबंधित"
    A_ = "अभौतिक लोक से संबंधित"
    P_, NP_ = "अस्तित्व के लोकों में समाई हुई", "अस्तित्व के लोकों में न समाई हुई"
    NOT = "न होने वाली"
    PERS = ("इस सीमा के बीच जो इसी लोक से संबंधित, इसी में समाई हुई, ध्यान-अवस्था में लीन व्यक्ति की, या वहाँ जन्मे "
            "व्यक्ति की, या इसी जीवन में सुख से रहने वाले व्यक्ति की, मन और मन की सहचर परिघटनाएँ हैं")
    h["2-1020"] = [
        lst([f"{K_} परिघटनाएँ", f"{K_} {NOT} परिघटनाएँ", f"{R_} परिघटनाएँ", f"{R_} {NOT} परिघटनाएँ",
             f"{A_} परिघटनाएँ", f"{A_} {NOT} परिघटनाएँ", f"{P_} परिघटनाएँ", f"{NP_} परिघटनाएँ"]) + "।",
        f"{K_} परिघटनाएँ कौन-सी हैं? नीचे अवीचि नरक को सीमा बनाकर, ऊपर दूसरों की रची गई चीज़ों पर अधिकार रखने वाले "
        f"देवताओं को भीतर रखकर, इस सीमा के बीच जो इसी लोक से संबंधित, इसी में समाए हुए समूह, तत्व, इंद्रिय-क्षेत्र; "
        f"भौतिक रूप, अनुभूति, पहचान, मानसिक रचनाएँ, चेतना हैं – ये {K_} परिघटनाएँ हैं।",
        f"{K_} {NOT} परिघटनाएँ कौन-सी हैं? {R_}, {A_} और {NP_} परिघटनाएँ – ये {K_} {NOT} परिघटनाएँ हैं।",
        f"{R_} परिघटनाएँ कौन-सी हैं? नीचे ब्रह्मलोक को सीमा बनाकर, ऊपर अकनिष्ठ देवताओं को भीतर रखकर, {PERS} – "
        f"ये {R_} परिघटनाएँ हैं।",
        f"{R_} {NOT} परिघटनाएँ कौन-सी हैं? {K_}, {A_} और {NP_} परिघटनाएँ – ये {R_} {NOT} परिघटनाएँ हैं।",
        f"{A_} परिघटनाएँ कौन-सी हैं? नीचे अनंत आकाश के क्षेत्र में पहुँचे देवताओं को सीमा बनाकर, ऊपर न पहचान, "
        f"न अ-पहचान के क्षेत्र में पहुँचे देवताओं को भीतर रखकर, {PERS} – ये {A_} परिघटनाएँ हैं।",
        f"{A_} {NOT} परिघटनाएँ कौन-सी हैं? {K_}, {R_} और {NP_} परिघटनाएँ – ये {A_} {NOT} परिघटनाएँ हैं।",
        f"{P_} परिघटनाएँ कौन-सी हैं? मन के मैलों का विषय बनने वाली हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ, "
        f"जो {K_}, {R_} या {A_} हैं; {lst(KH)} – ये {P_} परिघटनाएँ हैं।",
        f"{NP_} परिघटनाएँ कौन-सी हैं? मार्ग, मार्गों के फल और अनिर्मित तत्व – ये {NP_} परिघटनाएँ हैं।",
    ]

    # ------------------------------------------------ 6. Uppādakakamma-āyuppamāṇavāra
    h["2-18-6-0"] = ["#### जन्म देने वाले कर्म और आयु की अवधि का खंड"]
    h["2-18-6-1-0"] = ["##### जन्म देने वाला कर्म"]
    GIFT = "दान देकर, सदाचार ग्रहण करके, उपवास-व्रत का कर्म करके"
    AMONG = "के बीच जन्म लेते हैं"
    CMR = "चार महाराजाओं के देवताओं"
    gods6 = [CMR, "तैंतीस देवताओं", "याम देवताओं", "तुषित देवताओं", "सृजन में आनंद लेने वाले देवताओं",
             "दूसरों की रची गई चीज़ों पर अधिकार रखने वाले देवताओं"]
    groups = ["धनी क्षत्रियों", "धनी ब्राह्मणों", "धनी गृहस्थों"] + gods6
    h["2-1021"] = [
        "“देवता”। तीन प्रकार के देवता – लोक-मान्यता से देवता [वर्तनी-भेद (Syā.): sammatidevā], जन्म से देवता और "
        "शुद्धि से देवता।",
        "लोक-मान्यता से देवता कहलाते हैं – राजा, रानियाँ और राजकुमार।",
        "जन्म से देवता कहलाते हैं – चार महाराजाओं के [वर्तनी-भेद (Sī., Syā.): cātummahārājike] देवताओं से लेकर "
        "उनसे ऊपर के देवता।",
        "शुद्धि से देवता कहलाते हैं – अर्हतों को ऐसा कहा जाता है।",
        f"{GIFT} लोग कहाँ जन्म लेते हैं? {GIFT} " + ", ".join(
            f"{'कुछ लोग' if j == 0 else 'कुछ'} {x} {AMONG}" for j, x in enumerate(groups)) + "।",
    ]
    h["2-18-6-2-0"] = ["##### आयु की अवधि"]
    LIFE = "की आयु की अवधि कितनी है?"
    h["2-1022"] = [f"मनुष्यों {LIFE} सौ वर्ष, थोड़ा कम या अधिक [पाठभेद (Syā., Ka.): appaṃ vā bhiyyo vā; "
                   f"दीघ निकाय 2.7]।"]

    def heaven(name, human, divine, total, var=""):
        return (f"{name} {LIFE} मनुष्यों के जो {human} हैं, वह {name} का एक दिन-रात{var} है। "
                f"ऐसी तीस रातों का एक महीना होता है। ऐसे बारह महीनों का एक वर्ष होता है। "
                f"ऐसे वर्षों से दिव्य {divine} {name} की आयु की अवधि है। "
                f"मनुष्यों की गणना से यह कितनी होती है? {total}।")

    h["2-1023"] = [
        heaven(CMR, "पचास वर्ष", "पाँच सौ वर्ष", "नब्बे लाख वर्ष",
               " [वर्तनी-भेद (Ka.): rattidivo; अंगुत्तर निकाय 3.71]"),
        heaven("तैंतीस देवताओं", "सौ वर्ष", "एक हज़ार वर्ष", "तीन करोड़ साठ लाख वर्ष"),
        heaven("याम देवताओं", "दो सौ वर्ष", "दो हज़ार वर्ष", "चौदह करोड़ चालीस लाख वर्ष"),
        heaven("तुषित देवताओं", "चार सौ वर्ष", "चार हज़ार वर्ष", "सत्तावन करोड़ साठ लाख वर्ष"),
        heaven("सृजन में आनंद लेने वाले देवताओं", "आठ सौ वर्ष", "आठ हज़ार वर्ष", "दो सौ तीस करोड़ चालीस लाख वर्ष"),
        heaven("दूसरों की रची गई चीज़ों पर अधिकार रखने वाले देवताओं", "सोलह सौ वर्ष", "सोलह हज़ार वर्ष",
               "नौ सौ इक्कीस करोड़ साठ लाख वर्ष"),
        "ये छह [पाठभेद (Syā.): chapi te] इंद्रिय-सुखों के लोक से संबंधित हैं, सभी इंद्रिय-सुखों से भरपूर;",
        "इन सबकी आयु एक साथ गिनी जाए, तो वह कितनी होती है?",
        "बारह सौ करोड़ और अट्ठाईस करोड़;",
        "और पचास लाख वर्ष, वर्षों की गणना से ऐसा बताया गया है।",
    ]

    def jh(nth, level, gods, life):
        lv = {"p": "सीमित", "m": "मध्यम", "u": "उत्तम"}[level]
        x = f"{nth} ध्यान का {lv} रूप में अभ्यास करके"
        return f"{x} लोग कहाँ जन्म लेते हैं? {x} वे {gods} {AMONG}। उनकी आयु की अवधि कितनी है? {life}।"

    h["2-1024"] = [jh("पहले", "p", "ब्रह्मा की सभा के देवताओं", "कल्प का तीसरा भाग"),
                   jh("पहले", "m", "ब्रह्मा के पुरोहित देवताओं", "आधा कल्प"),
                   jh("पहले", "u", "महाब्रह्मा देवताओं", "एक कल्प [पाठभेद (Syā.): eko kappo]")]
    h["2-1025"] = [jh("दूसरे", "p", "सीमित आभा वाले देवताओं", "दो कल्प"),
                   jh("दूसरे", "m", "असीम आभा वाले देवताओं", "चार कल्प"),
                   jh("दूसरे", "u", "दीप्तिमान आभा वाले देवताओं", "आठ कल्प")]
    h["2-1026"] = [jh("तीसरे", "p", "सीमित शोभा वाले देवताओं", "सोलह कल्प"),
                   jh("तीसरे", "m", "असीम शोभा वाले देवताओं", "बत्तीस कल्प"),
                   jh("तीसरे", "u", "पूर्ण शोभा वाले देवताओं", "चौंसठ कल्प")]
    G4 = ["पहचान-रहित देवताओं", "महान फल वाले देवताओं", "अपने लोक से न डिगने वाले देवताओं", "न तपने वाले देवताओं",
          "सुंदर दिखने वाले देवताओं", "सुंदर देखने वाले देवताओं", "अकनिष्ठ देवताओं",
          "अनंत आकाश के क्षेत्र में पहुँचे देवताओं", "अनंत चेतना के क्षेत्र में पहुँचे देवताओं",
          "कुछ भी न होने के क्षेत्र में पहुँचे देवताओं", "न पहचान, न अ-पहचान के क्षेत्र में पहुँचे देवताओं"]
    DIV = lst([f"{x} की भिन्नता" for x in ["विषय", "मनोयोग", "चाह", "आकांक्षा", "निश्चय",
                                           "मन को लक्ष्य की ओर मोड़ने", "प्रज्ञा"]])
    h["2-1027"] = [
        f"चौथे ध्यान का अभ्यास करके, {DIV} के कारण " + ", ".join(
            f"{'कुछ लोग' if j == 0 else 'कुछ,' if x.startswith('कुछ') else 'कुछ'} {x} {AMONG}"
            for j, x in enumerate(G4)) + "।",
        f"पहचान-रहित देवताओं और महान फल वाले देवताओं {LIFE} पाँच सौ कल्प।",
        f"अपने लोक से न डिगने वाले देवताओं {LIFE} एक हज़ार कल्प।",
        f"न तपने वाले देवताओं {LIFE} दो हज़ार कल्प।",
        f"सुंदर दिखने वाले देवताओं {LIFE} चार हज़ार कल्प।",
        f"सुंदर देखने वाले देवताओं {LIFE} आठ हज़ार कल्प।",
        f"अकनिष्ठ देवताओं {LIFE} सोलह हज़ार कल्प।",
    ]
    h["2-1028"] = [f"{G4[7]} {LIFE} बीस हज़ार कल्प।", f"{G4[8]} {LIFE} चालीस हज़ार कल्प।",
                   f"{G4[9]} {LIFE} साठ हज़ार कल्प।", f"{G4[10]} {LIFE} चौरासी हज़ार कल्प।"]
    h["2-1029"] = [
        "पुण्य के तेज से ऊपर उठे, इंद्रिय-सुखों के लोक और सूक्ष्म भौतिक लोक की गति को प्राप्त हुए प्राणी,",
        "अस्तित्व के शिखर [पाठभेद (Syā.): bhavaggaṃ vāpi] तक भी पहुँचकर फिर दुर्गति में लौट आते हैं "
        "[पाठभेद (Syā.): puna gacchanti]।",
        "इतनी लंबी आयु वाले प्राणी भी आयु का क्षय होने पर मरते हैं;",
        "कोई भी अस्तित्व नित्य नहीं है, ऐसा महान ऋषि ने कहा है।",
        "इसलिए धीर, विवेकी, कुशल और अर्थ पर चिंतन करने वाले लोग;",
        "बुढ़ापे और मृत्यु से मुक्ति के लिए उत्तम मार्ग का अभ्यास करते हैं।",
        "निर्वाण में डुबकी लगाने की ओर ले जाने वाले शुद्ध मार्ग का अभ्यास करके;",
        "सभी मन के मैलों को पूरी तरह समझकर, मन के मैलों से रहित होकर वे पूर्ण निर्वाण पाते हैं।",
    ]

    # ------------------------------------------------ 7. Abhiññeyyādivāra
    h["2-18-7-0"] = ["#### प्रत्यक्ष जानने योग्य आदि का खंड"]
    six = (f"कितने {ABH} हैं, कितने {PAR} हैं, कितने छोड़े जाने वाले हैं, कितने {BHAV} हैं, कितने {SACC} हैं, "
           f"कितने न छोड़े जाने वाले हैं, न {BHAV}, न {SACC}")
    h["2-1030"] = [f"पाँच समूहों में से {six}… सात मनों में से {six}?"]
    AP = [("is", ABH), ("is", PAR)]
    NONE3 = ("neg", [PAH, BHAV, SACC])
    MIX4 = [("siya", PAH), ("siya", BHAV), ("siya", SACC), ("siyaneg", [PAH, BHAV, SACC])]

    def ab(sb, *parts):
        return S_(sb, *parts) + "।"

    h["2-1031"] = [
        ab(R_KH, *AP, NONE3) + " " + ab(subj("kh", 4), *AP, *MIX4),
        ab(subj("ay", 10), *AP, NONE3) + " " + ab(subj("ay", 2), *AP, *MIX4),
        ab(subj("dh", 16), *AP, NONE3) + " " + ab(subj("dh", 2), *AP, *MIX4),
        " ".join([ab(SAM_SC, *AP, ("is", PAH), ("neg", [BHAV, SACC])),
                  ab(MAG_SC, *AP, ("neg", [PAH]), ("is", BHAV), ("neg", [SACC])),
                  ab(NIR_SC, *AP, ("neg", [PAH, BHAV]), ("is", SACC)),
                  ab(DUK_SC, *AP, ("siya", PAH), ("neg", [BHAV]), ("neg", [SACC]), ("siyanot", PAH))]),
        " ".join([ab(subj("in", 9), *AP, NONE3),
                  ab(one(IN["domanassa"], "fs"), *AP, ("is", PAH), ("neg", [BHAV, SACC])),
                  ab(one(IN["anannata"], "fs"), *AP, ("neg", [PAH]), ("is", BHAV), ("neg", [SACC])),
                  ab(one(IN["anna"], "fs"), *AP, ("neg", [PAH]), ("siya", BHAV), ("siya", SACC)),
                  ab(one(IN["annatavi"], "fs"), *AP, ("neg", [PAH, BHAV]), ("is", SACC)),
                  ab(subj("in", 3), *AP, ("neg", [PAH]), ("siya", BHAV), ("siya", SACC), ("siyanot", BHAV),
                     ("is", SACC)),
                  ab(subj("in", 6), *AP, *MIX4)]),
        " ".join([ab(subj("he", 3, "तीन हानिकर मूल"), *AP, ("is", PAH), ("neg", [BHAV, SACC])),
                  ab(subj("he", 3, "तीन हितकर मूल"), *AP, ("neg", [PAH]), ("siya", BHAV), ("neg", [SACC]),
                     ("siyanot", BHAV)),
                  ab(subj("he", 3, "तीन नैतिक रूप से अनिर्धारित मूल"), *AP, ("neg", [PAH, BHAV]), ("siya", SACC),
                     ("siyanot", SACC))]),
        ab(FOOD_S, *AP, NONE3) + " " + ab(subj("ah", 3), *AP, *MIX4),
        ab(subj("ph", 6), *AP, NONE3) + " " + ab(MANOV_PH_S, *AP, *MIX4),
        ab(chain(["छह अनुभूतियाँ", "छह पहचानें", "छह इरादे", "छह मन"], "mp"), *AP, NONE3) + " "
        + ab(MANOVDH, *AP, *MIX4),
    ]

    # ------------------------------------------------ 8. Sārammaṇānārammaṇavāra
    h["2-18-8-0"] = ["#### विषय वाले और विषय से रहित का खंड"]
    h["2-1032"] = [f"पाँच समूहों में से कितने {agr(SAR, 'mp')} हैं, कितने {ANAR} हैं… "
                   f"सात मनों में से कितने {agr(SAR, 'mp')} हैं, कितने {ANAR} हैं?"]

    def s1(sb, *parts):
        return S_(sb, *parts) + "।"

    def ss(*xs):
        return " ".join(xs)

    sar2 = [("siya", SAR), ("siya", ANAR)]
    h["2-1033"] = [
        ss(s1(R_KH, ("is", ANAR)), s1(subj("kh", 4), ("is", SAR))),
        ss(s1(subj("ay", 10), ("is", ANAR)), s1(MANAY, ("is", SAR)), s1(DHAY, *sar2)),
        ss(s1(subj("dh", 10), ("is", ANAR)), s1(subj("dh", 7), ("is", SAR)), s1(DHDH, *sar2)),
        ss(s1(subj("sc", 2), ("is", SAR)), s1(NIR_SC, ("is", ANAR)), s1(DUK_SC, *sar2)),
        ss(s1(subj("in", 7), ("is", ANAR)), s1(subj("in", 14), ("is", SAR)), s1(JIVITA, *sar2),
           s1(subj("he", 9), ("is", SAR)), s1(FOOD_S, ("is", ANAR)), s1(subj("ah", 3), ("is", SAR)),
           s1(chain(["सात संपर्क", "सात अनुभूतियाँ", "सात पहचानें", "सात इरादे", "सात मन"], "mp"), ("is", SAR))),
    ]
    h["2-1034"] = [f"पाँच समूहों में से कितने {agr(SARAR, 'mp')} हैं, कितने {agr(ANARAR, 'mp')} हैं… "
                   f"सात मनों में से कितने {agr(SARAR, 'mp')} हैं, कितने {agr(ANARAR, 'mp')} हैं?"]
    ar2 = [("siya", SARAR), ("siya", ANARAR)]
    ar3 = ar2 + [("siya", ANAR)]
    h["2-1035"] = [
        ss(s1(R_KH, ("is", ANAR)), s1(subj("kh", 4), *ar2)),
        ss(s1(subj("ay", 10), ("is", ANAR)), s1(MANAY, *ar2), s1(DHAY, *ar3)),
        ss(s1(subj("dh", 10), ("is", ANAR)), s1(subj("dh", 6), ("is", ANARAR)), s1(MANOVDH, *ar2), s1(DHDH, *ar3)),
        ss(s1(NIR_SC, ("is", ANAR)), s1(MAG_SC, ("is", ANARAR)), s1(SAM_SC, *ar2), s1(DUK_SC, *ar3)),
        ss(s1(subj("in", 7), ("is", ANAR)), s1(subj("in", 5), ("is", ANARAR)), s1(subj("in", 9), *ar2),
           s1(JIVITA, *ar3)),
        ss(s1(subj("he", 9), *ar2), s1(FOOD_S, ("is", ANAR)), s1(subj("ah", 3), *ar2),
           s1(subj("ph", 6), ("is", ANARAR)), s1(MANOV_PH_S, *ar2),
           s1(chain(["छह अनुभूतियाँ", "छह पहचानें", "छह इरादे", "छह मन"], "mp"), ("is", ANARAR)),
           s1(MANOVDH, *ar2)),
    ]

    # ------------------------------------------------ 9. Diṭṭhasutādidassanavāra
    h["2-18-9-0"] = ["#### देखे, सुने आदि को दिखाने वाला खंड"]
    dq = (f"कितने देखे हुए हैं, कितने सुने हुए, कितने अनुभव किए हुए, कितने जाने हुए, "
          f"कितने न देखे हुए हैं, न सुने हुए, न अनुभव किए हुए, न जाने हुए")
    h["2-1036"] = [f"पाँच समूहों में से {dq}… सात मनों में से {dq}?"]

    def onlyv(sb):
        """na diṭṭhā na sutā na mutā, viññātā"""
        t, g, _ = sb
        return f"{t} न {agr(DIT, g)} {HAI[g]}, न {agr(SUT, g)}, न {agr(MUT, g)}, पर {agr(VINN, g)} {HAI[g]}।"

    def pattern(sb, d, s, m):
        """X diṭṭhaṃ/na diṭṭhaṃ, sutaṃ/na sutaṃ, mutaṃ/na mutaṃ, viññātaṃ"""
        t, g, _ = sb
        bits = []
        for flag, w in ((d, DIT), (s, SUT), (m, MUT)):
            bits.append(f"{'' if flag else 'न '}{agr(w, g)}")
        out = f"{t} " + ", ".join(bits) + f", पर {agr(VINN, g)} {HAI[g]}।"
        return out

    def siya_all(sb):
        t, g, _ = sb
        return (f"{t} कभी {agr(DIT, g)} {HOTA[g]}, कभी {agr(SUT, g)} {HOTA[g]}, कभी {agr(MUT, g)} {HOTA[g]}, "
                f"कभी {agr(VINN, g)} {HOTA[g]}, कभी न {agr(DIT, g)} {HOTA[g]}, न {agr(SUT, g)}, "
                f"न {agr(MUT, g)}, पर {agr(VINN, g)}।")

    h["2-1037"] = [
        ss(siya_all(R_KH), onlyv(subj("kh", 4))),
        ss(pattern(one(AY["rupa"], "ms"), True, False, False), pattern(SADDAY, False, True, False),
           pattern(chain([AY["gandha"], AY["rasa"], AY["photthabba"]], "ms"), False, False, True),
           onlyv(subj("ay", 7))),
        ss(pattern(one(DH["rupa"], "ms"), True, False, False), pattern(SADDADH, False, True, False),
           pattern(chain([DH["gandha"], DH["rasa"], DH["photthabba"]], "ms"), False, False, True),
           onlyv(subj("dh", 13))),
        ss(onlyv(subj("sc", 3)), siya_all(DUK_SC)),
        ss(onlyv(subj("in", 22)), onlyv(subj("he", 9)), onlyv(subj("ah", 4)), onlyv(subj("ph", 7)),
           onlyv(chain(["सात अनुभूतियाँ", "सात पहचानें", "सात इरादे", "सात मन"], "mp"))),
    ]

    # ------------------------------------------------ 10. Tikādidassanavāra
    h["2-18-10-0"] = ["#### तीन-तीन आदि के वर्गीकरणों को दिखाने वाला खंड"]

    def tq(preds):
        ks = ", ".join(f"कितने {agr(p, 'mp')}" for p in preds)
        ks = ks.replace(", कितने", " हैं, कितने", 1)
        return f"पाँच समूहों में से {ks}… सात मनों में से {ks}?"

    # Kusalattika
    h["2-18-10-1-0"] = ["##### हितकर का तीन-तीन वर्गीकरण"]
    k3 = [("siya", KUS), ("siya", AKUS), ("siya", ABY)]
    kb = [("siya", KUS), ("siya", ABY)]
    h["2-1038"] = [
        tq([KUS, AKUS, ABY]),
        ss(s1(R_KH, ("is", ABY)), s1(subj("kh", 4), *k3), s1(subj("ay", 10), ("is", ABY)),
           s1(subj("ay", 2), *k3), s1(subj("dh", 16), ("is", ABY)), s1(subj("dh", 2), *k3),
           s1(SAM_SC, ("is", AKUS)), s1(MAG_SC, ("is", KUS)), s1(NIR_SC, ("is", ABY)), s1(DUK_SC, *k3)),
        ss(s1(subj("in", 10), ("is", ABY)), s1(one(IN["domanassa"], "fs"), ("is", AKUS)),
           s1(one(IN["anannata"], "fs"), ("is", KUS)), s1(subj("in", 4), *kb), s1(subj("in", 6), *k3)),
        ss(s1(subj("he", 3, "तीन हितकर मूल"), ("is", KUS)), s1(subj("he", 3, "तीन हानिकर मूल"), ("is", AKUS)),
           s1(subj("he", 3, "तीन नैतिक रूप से अनिर्धारित मूल"), ("is", ABY)), s1(FOOD_S, ("is", ABY)),
           s1(subj("ah", 3), *k3), s1(subj("ph", 6), ("is", ABY)), s1(MANOV_PH_S, *k3),
           s1(chain(["छह अनुभूतियाँ", "छह पहचानें", "छह इरादे", "छह मन"], "mp"), ("is", ABY)),
           s1(MANOVDH, *k3)),
    ]
    # Vedanāttika
    h["2-18-10-2-0"] = ["##### अनुभूति का तीन-तीन वर्गीकरण"]
    V3 = [SUKHA_S, DUKKHA_S, ADM_S]
    v3 = [("siya", p) for p in V3]
    v2a = [("siya", SUKHA_S), ("siya", ADM_S)]
    v2b = [("siya", SUKHA_S), ("siya", DUKKHA_S)]
    NV3 = ("nv", V3)
    SNV3 = ("siyanv", V3)
    h["2-1039"] = [
        tq(V3),
        ss(s1(subj("kh", 2), NV3), s1(subj("kh", 3), *v3)),
        ss(s1(subj("ay", 10), NV3), s1(MANAY, *v3), s1(DHAY, *v3, SNV3)),
        ss(s1(subj("dh", 10), NV3), S_(subj("dh", 5), ("is", ADM_S)) + ", " + S_(KAYAVDH, *v2b) + "।",
           s1(MANOVDH, *v3), s1(DHDH, *v3, SNV3)),
        ss(s1(subj("sc", 2), *v2a), s1(NIR_SC, NV3), s1(DUK_SC, *v3, SNV3)),
        ss(s1(subj("in", 12), NV3), s1(subj("in", 6), *v2a), s1(subj("in", 3), *v3), s1(JIVITA, *v3, SNV3)),
        ss(s1(one("द्वेष हानिकर मूल", "ms"), ("is", DUKKHA_S)), s1(subj("he", 7), *v2a),
           s1(one("मोह हानिकर मूल", "ms"), *v3)),
        ss(s1(FOOD_S, NV3), s1(subj("ah", 3), *v3)),
        ss(s1(subj("ph", 5), ("is", ADM_S)), s1(KAYAV_PH_S, *v2b), s1(MANOV_PH_S, *v3)),
        ss(s1(subj("ve", 7), NV3),
           S_(chain(["पाँच पहचानें", "पाँच इरादे", "पाँच मन"], "mp"), ("is", ADM_S)) + ", " + S_(KAYAVDH, *v2b) + "।",
           s1(MANOVDH, *v3)),
    ]
    # Vipākattika
    h["2-18-10-3-0"] = ["##### कर्म-फल का तीन-तीन वर्गीकरण"]
    p3 = [("siya", VIP), ("siya", VIPD), ("siya", NVIP)]
    p2 = [("siya", VIP), ("siya", NVIP)]
    h["2-1040"] = [
        tq([VIP, VIPD, NVIP]),
        ss(s1(R_KH, ("is", NVIP)), s1(subj("kh", 4), *p3)),
        ss(s1(subj("ay", 10), ("is", NVIP)), s1(subj("ay", 2), *p3)),
        ss(s1(subj("dh", 10), ("is", NVIP)), s1(subj("dh", 5), ("is", VIP)), s1(MANODH, *p2), s1(subj("dh", 2), *p3)),
        ss(s1(subj("sc", 2), ("is", VIPD)), s1(NIR_SC, ("is", NVIP)), s1(DUK_SC, *p3)),
        ss(s1(subj("in", 7), ("is", NVIP)), s1(subj("in", 3), ("is", VIP)), s1(subj("in", 2), ("is", VIPD)),
           s1(one(IN["anna"], "fs"), ("siya", VIP), ("siya", VIPD)), s1(subj("in", 9), *p3)),
        ss(s1(subj("he", 6), ("is", VIPD)), s1(subj("he", 3, "तीन नैतिक रूप से अनिर्धारित मूल"), *p2)),
        ss(s1(FOOD_S, ("is", NVIP)), s1(subj("ah", 3), *p3), s1(subj("ph", 5), ("is", VIP)), s1(MANO_PH_S, *p2),
           s1(MANOV_PH_S, *p3), s1(chain(["पाँच अनुभूतियाँ", "पाँच पहचानें", "पाँच इरादे", "पाँच मन"], "mp"),
                                   ("is", VIP)), s1(MANODH, *p2), s1(MANOVDH, *p3)),
    ]
    # Upādinnattika
    h["2-18-10-4-0"] = ["##### कर्म से उत्पन्न का तीन-तीन वर्गीकरण"]
    u3 = [("siya", UU), ("siya", AU), ("siya", AA)]
    u2 = [("siya", UU), ("siya", AU)]
    h["2-1041"] = [
        tq([UU, AU, AA]),
        ss(s1(R_KH, *u2).replace("।", " 4।"), s1(subj("kh", 4), *u3)),
        ss(s1(subj("ay", 5), ("is", UU)), s1(SADDAY, ("is", AU)), s1(subj("ay", 4), *u2), s1(subj("ay", 2), *u3)),
        ss(s1(subj("dh", 10), ("is", UU)), s1(SADDADH, ("is", AU)), s1(subj("dh", 5), *u2), s1(subj("dh", 2), *u3)),
        ss(s1(SAM_SC, ("is", AU)), s1(subj("sc", 2), ("is", AA)), s1(DUK_SC, *u2)),
        ss(s1(subj("in", 9), ("is", UU)), s1(one(IN["domanassa"], "fs"), ("is", AU)), s1(subj("in", 3), ("is", AA)),
           s1(subj("in", 9), *u3), s1(subj("he", 3, "तीन हानिकर मूल"), ("is", AU)),
           s1(subj("he", 3, "तीन हितकर मूल"), ("siya", AU), ("siya", AA)),
           s1(subj("he", 3, "तीन नैतिक रूप से अनिर्धारित मूल"), *u3)),
        ss(s1(FOOD_S, *u2), s1(subj("ah", 3), *u3)),
        ss(s1(subj("ph", 5), ("is", UU)), s1(MANO_PH_S, *u2), s1(MANOV_PH_S, *u3),
           s1(chain(["पाँच अनुभूतियाँ", "पाँच पहचानें", "पाँच इरादे", "पाँच मन"], "mp"), ("is", UU)),
           s1(MANODH, *u2), s1(MANOVDH, *u3)),
    ]
    # Vitakkattika
    h["2-18-10-5-0"] = ["##### आरंभिक विचार का तीन-तीन वर्गीकरण"]
    t3 = [("siya", SVSV), ("siya", AVVM), ("siya", AVAV)]
    TNV = ("siyanv", [SVSV, AVVM, AVAV])
    h["2-1042"] = [
        tq([SVSV, AVVM, AVAV]),
        ss(s1(R_KH, ("is", AVAV)), s1(subj("kh", 3), *t3), s1(SAN_KH, *t3, TNV)),
        ss(s1(subj("ay", 10), ("is", AVAV)), s1(MANAY, *t3), s1(DHAY, *t3, TNV)),
        ss(s1(subj("dh", 15), ("is", AVAV)), s1(MANODH, ("is", SVSV)), s1(MANOVDH, *t3), s1(DHDH, *t3, TNV)),
        ss(s1(SAM_SC, ("is", SVSV)), s1(NIR_SC, ("is", AVAV)), s1(MAG_SC, *t3), s1(DUK_SC, *t3, TNV)),
        ss(s1(subj("in", 9), ("is", AVAV)), s1(one(IN["domanassa"], "fs"), ("is", SVSV)),
           s1(one(IN["upekkha"], "fs"), ("siya", SVSV), ("siya", AVAV)), s1(subj("in", 11), *t3)),
        ss(s1(subj("he", 3, "तीन हानिकर मूल"), ("is", SVSV)), s1(subj("he", 6), *t3), s1(FOOD_S, ("is", AVAV)),
           s1(subj("ah", 3), *t3), s1(subj("ph", 5), ("is", AVAV)), s1(MANO_PH_S, ("is", SVSV)),
           s1(MANOV_PH_S, *t3),
           S_(chain(["पाँच अनुभूतियाँ", "पाँच पहचानें", "पाँच इरादे", "पाँच मन"], "mp"), ("is", AVAV)) + "; "
           + S_(MANODH, ("is", SVSV)) + ", " + S_(MANOVDH, *t3) + "।"),
    ]
    # Rūpaduka
    h["2-18-10-6-0"] = ["##### (1) भौतिक रूप का दो-दो वर्गीकरण"]
    RP, ARP = "भौतिक", "अभौतिक"
    r2 = [("siya", RP), ("siya", ARP)]
    h["2-1043"] = [
        f"पाँच समूहों में से कितने {RP} हैं, कितने {ARP}… सात मनों में से कितने {RP} हैं, कितने {ARP}?",
        ss(s1(R_KH, ("is", RP)), s1(subj("kh", 4), ("is", ARP)), s1(subj("ay", 10), ("is", RP)),
           s1(MANAY, ("is", ARP)), s1(DHAY, *r2), s1(subj("dh", 10), ("is", RP)), s1(subj("dh", 7), ("is", ARP)),
           s1(DHDH, *r2), s1(subj("sc", 3), ("is", ARP)), s1(DUK_SC, *r2), s1(subj("in", 7), ("is", RP)),
           s1(subj("in", 14), ("is", ARP)), s1(JIVITA, *r2), s1(subj("he", 9), ("is", ARP)), s1(FOOD_S, ("is", RP)),
           s1(subj("ah", 3), ("is", ARP)), s1(subj("ph", 7), ("is", ARP)),
           s1(chain(["सात अनुभूतियाँ", "सात पहचानें", "सात इरादे", "सात मन"], "mp"), ("is", ARP))),
    ]
    # Lokiyaduka
    h["2-18-10-7-0"] = ["##### (2) लौकिक का दो-दो वर्गीकरण"]
    LO, LU = "लौकिक", "लोकोत्तर"
    l2 = [("siya", LO), ("siya", LU)]
    lq = lambda x: f"{x} में से कितने {LO} हैं, कितने {LU}?"  # noqa: E731
    h["2-1044"] = [
        " ".join([lq("पाँच समूहों"), lq("बारह इंद्रिय-क्षेत्रों"), lq("अठारह तत्वों")])
        + f" चार सत्यों में से कितने {LO} हैं, कितने {LU}… सात मनों में से कितने {LO} हैं, कितने {LU}?",
        ss(s1(R_KH, ("is", LO)), s1(subj("kh", 4), *l2), s1(subj("ay", 10), ("is", LO)), s1(subj("ay", 2), *l2),
           s1(subj("dh", 16), ("is", LO)), s1(subj("dh", 2), *l2), s1(subj("sc", 2), ("is", LO)),
           s1(subj("sc", 2), ("is", LU))),
        ss(s1(subj("in", 10), ("is", LO)), s1(subj("in", 3), ("is", LU)), s1(subj("in", 9), *l2),
           s1(subj("he", 3, "तीन हानिकर मूल"), ("is", LO)), s1(subj("he", 6), *l2), s1(FOOD_S, ("is", LO)),
           s1(subj("ah", 3), *l2), s1(subj("ph", 6), ("is", LO)), s1(MANOV_PH_S, *l2),
           s1(subj("ve", 6), ("is", LO)), s1(one(born7("अनुभूति")[6], "fs"), *l2),
           s1(subj("sa", 6), ("is", LO)), s1(one(born7("पहचान")[6], "fs"), *l2),
           s1(subj("ce", 6), ("is", LO)), s1(one(born7("इरादा")[6], "ms"), *l2),
           s1(subj("ci", 6), ("is", LO)), s1(MANOVDH, *l2)),
        "प्रत्यक्ष जानना, विषय वाले के दो खंड, देखा हुआ, हितकर, अनुभूति;",
        "कर्म-फल, कर्म से उत्पन्न, आरंभिक विचार, भौतिक रूप और लौकिक।",
        f"{TITLE} {S.DONE}।",
        "“विस्तृत विश्लेषण” ग्रंथ समाप्त।",
    ]
    return h


def main():
    pi1 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI1_HI.glob("*.md")))
    for s in [ABY_HETU, "मार्ग, मार्गों के फल और अनिर्मित तत्व", "नीचे अवीचि नरक को सीमा बनाकर",
              "इस सीमा के बीच जो इसी लोक से संबंधित, इसी में समाई हुई, ध्यान-अवस्था में लीन व्यक्ति की"]:
        assert s in pi1, ("not in pi-1", s[:60])
    src = (S.PALI / NAME).read_text(encoding="utf-8").splitlines()
    S.emit(src, build(), S.OUT / NAME)


if __name__ == "__main__":
    main()
