"""pi-7 Pāli->Hindi keyword maps for 2-09 … 2-17 (minus 2-13) and 3-01-hetugocchaka.
Conventions: hi-map-conventions-pi7.md (map_sample_hi.py imported read-only).
usage: python -I -B -X utf8 map_2-09_3-01_hi.py [--missing] [--audit] [file …]
"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: E402,F401,F403
from map_sample_hi import read_keywords, read_hindi, read_pali, pi7_value, present, lc, NDE  # noqa: E402

FILES = ("2-09-hinattika", "2-10-micchattaniyatattika", "2-11-maggarammanattika", "2-12-uppannattika",
         "2-14-atitarammanattika", "2-15-ajjhattattika", "2-16-ajjhattarammanattika",
         "2-17-sanidassanasappatighattika", "3-01-hetugocchaka")

# chapter table: keys with a lower-case first letter
T = {}
# --- knowledges (PI7 has the -assa forms), feelings and states of mind
for _p, _h in (("cetopariya", "दूसरों के मन को जानने का ज्ञान"), ("iddhividha", "अलौकिक शक्तियों का ज्ञान"),
               ("pubbenivāsānussati", "पूर्व जन्मों के अनुस्मरण का ज्ञान"),
               ("yathākammūpaga", "प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान"),
               ("anāgataṃsa", "भविष्य को जानने का ज्ञान")):
    for _e in ("ñāṇaṃ", "ñāṇena", "ñāṇassa"):
        T[_p + _e] = _h
for _p, _h in (("vicikicchā", "संशय"), ("uddhacca", "बेचैनी")):
    for _e in ("gataṃ", "gate", "gato", "gatā", "gatassa", "gatānaṃ"):
        T[_p + "saha" + _e] = f"{_h} के साथ होने वाला"
for _p, _h in (("cakkhu", "आँख"), ("sota", "कान"), ("ghāna", "नाक"), ("jivhā", "जीभ"), ("kāya", "शरीर")):
    T[_p + "viññāṇasahagatānaṃ"] = f"{_h} की चेतना के साथ होने वाला"
for _p, _h in (("lobh", "लोभ"), ("dos", "द्वेष"), ("moh", "मोह")):
    for _e in ("o", "aṃ", "assa", "añca", "e"):
        T[_p + _e] = _h
        T["a" + _p + _e] = f"{_h} का अभाव"
for _p, _h in (("anicc", "अनित्यता का अवलोकन"), ("dukkh", "दुःख का अवलोकन"),
               ("anatt", "आत्मा से रहित होने का अवलोकन")):
    for _e in ("ānupassanā", "ānupassanāya"):
        T[_p + _e] = _h
T.update({
    "pañcaviññāṇaṃ": "पाँच प्रकार की चेतना", "pañcaviññāṇasahagataṃ": "पाँच प्रकार की चेतना के साथ होने वाला",
    "viññāṇānaṃ": "चेतना",
    "bhavaṅgaṃ": "जीवन-धारा", "bhavaṅgassa": "जीवन-धारा", "cuticittaṃ": "मृत्यु का मन",
    "paṭisandhicittaṃ": "पुनर्जन्म का मन", "paṭisandhicittassa": "पुनर्जन्म का मन",
    "upapatticittassa": "जन्म का मन", "āvajjanā": "मन को विषय की ओर मोड़ना",
    "cittasamaṅgissa": "मन से युक्त व्यक्ति",
    "nahetucittasamaṅgissa": "मूल रूपी न होने वाले मन से युक्त व्यक्ति",
    "ajjhattārammaṇabahiddhācittasamaṅgissa": "स्वयं से संबंधित विषय वाला दूसरों से संबंधित मन से युक्त व्यक्ति",
    "paccavekkhaṇā": "पुनः विचार", "tadārammaṇatā": "उसी विषय को लेकर",
    "niruddhe": "समाप्त होना", "kusalākusale": "हितकर और हानिकर",
    "pavattipaṭisandhi": "प्रक्रिया और पुनर्जन्म", "pavatteyeva": "केवल जीवन के दौरान",
    "dibbaṃ": "दिव्य", "sotadhātuṃ": "कान का तत्व", "nibbānaṃ": "निर्वाण", "phalā": "फल",
    "cittena": "मन", "cāgaṃ": "त्याग", "saṅkhāre": "निर्मित परिघटना", "rāgassa": "राग", "dukkhassa": "दुःख",
    "paro": "दूसरा व्यक्ति",
})
# --- the triad / dyad items of these chapters (TRIAD_ITEMS lacks the first item of 2-17)
for _e in ("aṃ", "o", "ā", "assa", "ānaṃ", "e", "añca", "a"):
    T["sanidassanasappaṭigh" + _e] = "दिखाई देने वाला और टकराव वाला"
for _p, _h in (("micchattaniyat", "ग़लत दिशा में निश्चित"), ("sammattaniyat", "सही दिशा में निश्चित"),
               ("aniyat", "अनिश्चित"), ("sahetuk", "मूल वाली")):
    T[_p + "ādhipati"] = f"{_h} प्रधानता"
for _e in ("assa", "e", "ānaṃ", "ānañceva", "ā"):
    T["sahetuk" + _e] = "मूल वाला"
    T["ahetuk" + _e] = "मूल से रहित"
T.update({
    "anuppannaṃ": "उत्पन्न न हुआ", "anuppanno": "उत्पन्न न हुआ", "uppannassa": "उत्पन्न हो चुका",
    "uppādiṃ": "उत्पन्न होने वाला",
    "adhipati": "प्रधानता", "hetūnañca": "मूल", "sampayuttake": "जुड़ा हुआ",
    "mahābhūtesu": "महाभूत", "utusamuṭṭhānā": "तापमान से उत्पन्न", "asaññasattā": "पहचान-रहित प्राणी",
    "āpodhātuṃ": "जल तत्व", "āpodhātuñca": "जल तत्व", "kabaḷīkāraṃ": "कौर-कौर खाया जाने वाला",
    "āhāraṃ": ("आहार", "भोजन"),
    "cakkhāyatanassa": "आँख का इंद्रिय-क्षेत्र", "rasāyatanassa": "स्वाद का इंद्रिय-क्षेत्र",
    "pañcāyatanāni": "पाँच इंद्रिय-क्षेत्र",
    "tividharūpasaṅgahena": "भौतिक रूप का तीन प्रकार का संग्रह",
    "tividharūpasaṅgaho": "भौतिक रूप का तीन प्रकार का संग्रह",
})
# --- the crimes of the micchattaniyata triad (2-10)
for _p, _h in (("mātughāti", "माता की हत्या का कर्म"), ("pitughāti", "पिता की हत्या का कर्म"),
               ("arahantaghāti", "अर्हत् की हत्या का कर्म"), ("ruhiruppāda", "बुद्ध का खून बहाने का कर्म"),
               ("saṅghabheda", "संघ में फूट डालने का कर्म")):
    for _e in ("kammaṃ", "kammassa"):
        T[_p + _e] = _h
T.update({
    "mātaraṃ": "माता", "pitaraṃ": "पिता", "jīvitā": "जान", "voropeti": "लेना", "voropetvā": "लेकर",
    "uppādetvā": "बहाकर", "bhinditvā": "फूट डालकर", "paṭighātatthāya": "निवारण",
    "niyatamicchādiṭṭhiyā": "निश्चित ग़लत दृष्टि", "nigamaghātaṃ": "कस्बे पर डाका",
    "assādenti": "रस लेना", "abhinandanti": "आनंद लेना", "vipassanti": "अंतर्दृष्टि से देखना",
    "uppādenti": "उत्पन्न करना", "samāpajjanti": "प्रवेश करना",
    "parikammaṃ": "प्रारंभिक तैयारी", "tatiyo": "तीसरा", "catutthassa": "चौथा",
    "purimo": "पहले-पहले का", "pacchimassa": "बाद-बाद का",
    "atthappaṭisambhidāya": "अर्थ का विश्लेषणात्मक ज्ञान",
    "ṭhānāṭhānakosallassa": "संभव और असंभव को जानने की कुशलता",
    "vuṭṭhānassa": "बाहर आना",
})
# --- numbers
T.update({
    "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह", "sattarasa": "सत्रह", "ekavīsa": "इक्कीस",
    "bāvīsa": "बाईस", "tevīsa": "तेईस", "catuvīsa": "चौबीस", "pañcavīsa": "पच्चीस", "sattapi": "सात",
})
# --- instructions and editorial notes
T.update({
    "kātabbaṃ": ("बनाना चाहिए", "करना चाहिए", "लेना चाहिए"),
    "kātabbā": ("बनाना चाहिए", "करना चाहिए", "लेना चाहिए"),
    "kātabbo": ("लेना चाहिए", "करना चाहिए"), "kātabbāni": ("करना चाहिए", "बनाना चाहिए"),
    "vibhajitabbaṃ": ("विभाजन करना चाहिए", "अलग-अलग दिखाना चाहिए"),
    "vibhajitabbā": ("विभाजन करना चाहिए", "अलग-अलग दिखाना चाहिए"), "vibhajitvā": "विभाजन करके",
    "vitthāretabbāni": "विस्तार करना चाहिए", "gaṇetabbāni": "गिनना चाहिए", "gaṇetabbo": "गिनती करना चाहिए",
    "vajjetabbā": "छोड़ देना चाहिए",
    "paripuṇṇaṃ": ("परिपूर्ण", "पूर्ण"), "paripuṇṇā": ("परिपूर्ण", "पूर्ण"), "paripuṇṇo": ("परिपूर्ण", "पूर्ण"),
    "cakkaṃ": "चक्र", "gahite": "लेना", "natthi": "नहीं होना",
    "anumajjantena": "ध्यान से देखते हुए", "asammohantena": "बिना भ्रमित हुए",
    "mātikāpadāni": "मूल सूची का पद", "ninnānākaraṇaṃ": "बिना किसी अंतर के",
    "ninnānākaraṇā": "बिना किसी अंतर के", "pariyosānapadā": "अंतिम पद", "ante": "अंत",
    "avasesā": ("शेष", "बाकी"), "kāraṇena": "तरीका", "sādhukaṃ": "भली-भाँति", "yāva": "तक",
    "ghaṭane": "मेल", "ekasadisā": "एक समान", "dutiyagamanasadisaṃ": "दूसरे प्रसंग के समान",
    "gaṇanā": "गणना", "pañhānaṃ": "प्रश्न", "niṭṭhitesu": "पूरा हो जाना",
    "nakammeneva": "कर्म-कारण का अभाव",
    "natthivigatapaccayaṃ": "अनुपस्थिति-कारण और विलीनता-कारण",
    "aññamaññapaccaye": "परस्पर-कारण",
    # members of hyphenated condition lists (headings, gaṇanā combinations): the condition name
    "anantara": "निकटता-कारण", "aññamañña": "परस्पर-कारण", "nissaya": "आश्रय-कारण",
    "atthi": "उपस्थिति-कारण", "avigatanti": "अविलीनता-कारण", "sahajāta": ("सह-उत्पत्ति-कारण", "सह-उत्पत्ति"),
    # the series named after an item (2-17)
    "anidassanaappaṭighamūlake": "दिखाई न देने वाली और टकराव से रहित परिघटना से शुरू होने वाली शृंखला",
    "anidassanaappaṭighamūlakā": "दिखाई न देने वाली और टकराव से रहित परिघटना से शुरू होने वाली शृंखला",
    "anidassanasappaṭighamūlake": "दिखाई न देने वाली पर टकराव वाली परिघटना से शुरू होने वाली शृंखला",
    "anidassanasappaṭighamūlakā": "दिखाई न देने वाली पर टकराव वाली परिघटना से शुरू होने वाली शृंखला",
})
# --- second senses found in these chapters (tuples: the first one present in the segment wins)
T.update({
    "anulomaṃ": ("सकारात्मक क्रम", "अनुरूपता"),                      # «Anulomaṃ gotrabhussa» = अनुरूपता
    "sutaṃ": "सुना-सीखा ज्ञान",                                     # pi-2
    "karoti": ("पालन करना", "डालना"),                               # «nigamaghātaṃ karoti» = डाका डालता है
    "jappeti": ("पालना", "करना"),                                   # «mānaṃ jappeti» = अहंकार करता है (3-01)
    "ajjhattikā": "स्वयं से संबंधित",
    "vipāko": ("कर्म-फल रूपी", "कर्म के फल रूपी", "कर्म-फल"),        # «vipāko alobho» = कर्म-फल और लोभ का अभाव
    "vipākaṃ": ("कर्म-फल रूपी", "कर्म के फल रूपी", "कर्म-फल"),
    "anumajjantena": ("ध्यान से देखते हुए", "क्रम से जाँचते हुए"),
    "pavattipaṭisandhi": ("प्रक्रिया और पुनर्जन्म", "जीवन-काल और पुनर्जन्म"),
    "uppannaṃ": ("उत्पन्न हो चुका", "उत्पन्न"),
})

# per-segment overrides {file: {bid: {kw: value}}}
OVR = {f: {} for f in FILES}
OVR["3-01-hetugocchaka"].update({
    "7-24-48": {"Hetudukaṃ": "मूल वाला दो का वर्गीकरण"},          # colophon «… समाप्त», not a count heading
})
OVR["2-17-sanidassanasappatighattika"].update({
    "7-23-58": {"vippayutta": "अलगाव-कारण"},                       # member of the gaṇanā combinations
    "7-23-52": {"kātabbā": "लेना चाहिए"},                          # «… indriyampi kātabbā» = «… क्षमता भी लेने चाहिए»
})


def resolver_for(f, table):
    """make_resolver + one context rule: rūpaṃ that only occurs in «cakkhunā rūpaṃ passati» = दृश्य रूप."""
    base = make_resolver(f, table, OVR[f])
    pa = read_pali(f)

    def r(bid, kw, kws):
        if kw == "rūpaṃ" and kw not in OVR[f].get(bid, {}):
            p = pa.get(bid, "")
            n_all = len(re.findall(r"(?<![\wāīūṃṅñṭḍṇḷ])rūpaṃ(?![\wāīūṃṅñṭḍṇḷ])", p))
            if n_all and n_all == p.count("rūpaṃ passati"):
                return "दृश्य रूप"
        return base(bid, kw, kws)
    return r


def ambiguous(f, table):
    """Tuple values where two or more alternatives occur in the segment's Hindi: to read by eye."""
    hi = read_hindi(f)
    for bid, kws in read_keywords(f):
        for kw in sorted(set(kws)):
            if kw in OVR[f].get(bid, {}):
                continue
            k = lc(kw)
            v = table.get(k)
            if isinstance(v, tuple):
                alts = [a for a in v if present(a, hi.get(bid, ""))]
                if len(alts) > 1:
                    print(f, bid, kw, "x", kws.count(kw), "->", alts)
# presence exceptions {file: {(bid, kw): reason}}
ALLOWED = {f: {} for f in FILES}
ALLOWED["2-15-ajjhattattika"].update({
    ("7-21-45", "mātikāpadāni"): "text «मूल सूची के पदों», oblique plural of पद (2-letter token, checker allows no ending)",
    ("7-21-47", "mātikāpadāni"): "text «मूल सूची के पदों», oblique plural of पद (2-letter token, checker allows no ending)",
})


def natthi_allowed(f):
    """natthi = नहीं होना (pi-5); the text has the present tense «नहीं है(ं)» or «न … है»."""
    hi, out = read_hindi(f), {}
    for bid, kws in read_keywords(f):
        if "natthi" in kws:
            t = hi.get(bid, "")
            if re.search(r"नहीं हैं?(?![ऀ-ॿ])", t):
                out[(bid, "natthi")] = "text «नहीं है», present tense of नहीं होना"
            elif re.search(r"(?<![ऀ-ॿ])न [^।]* है(?![ऀ-ॿ])", t):
                out[(bid, "natthi")] = "text «न … है» (न पुनर्जन्म है, न …), present tense of नहीं होना"
    return out


def missing(f, table):
    hi, pa = read_hindi(f), read_pali(f)
    miss = collections.Counter()
    for bid, kws in read_keywords(f):
        for kw in kws:
            if kw in OVR[f].get(bid, {}):
                continue
            try:
                pi7_value(kw, kws, table, pa.get(bid), hi.get(bid))
            except KeyError:
                miss[kw] += 1
    print("=====", f, len(miss))
    for kw, c in sorted(miss.items()):
        print(f"  {c:3} {kw}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = args or FILES
    table = {**PI7, **T}
    for f in files:
        if "--missing" in sys.argv:
            missing(f, table)
            continue
        if "--ambig" in sys.argv:
            ambiguous(f, table)
            continue
        build_part(f, resolver_for(f, table))
        verify(f, allowed={**ALLOWED[f], **natthi_allowed(f)})
        if "--audit" in sys.argv:
            print("-" * 10, "fallback audit", f)
            audit(f, table, OVR[f], only_fallback=True)
