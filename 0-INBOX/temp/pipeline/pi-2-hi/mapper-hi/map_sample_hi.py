"""pi-2 (Vibhaṅga) Pāli->Hindi keyword maps: shared tooling + the sample (preamble, 1-khandhavibhango).

Importing this module writes nothing and prints nothing. Later chapter scripts:

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_sample_hi import *          # PI2, pi2_value, build_part, verify, present, prior, ...

    T = {...}                             # your chapter table (lower-case first letter keys)
    OVR = {"2-xx": {"kw": "हिंदी"}}         # per-segment overrides (exact keyword spelling)
    def resolver(bid, kw, kws):
        if kw in OVR.get(bid, {}): return OVR[bid][kw]
        return pi2_value(kw, kws, {**PI2, **T}, bid)
    build_part("<chapter>", resolver); verify("<chapter>")

Main pieces
- read_keywords(ch) / read_hindi(ch) / read_pali(ch)  (pi-2 paths; segments end with ^id)
- present(value, text)        presence check of pi-1 (map_common_hi), inflection-tolerant
- PI2                         default table settled on the sample (aggregates, classification frames,
                              Pañhāpucchaka frames, Suttanta definitions); CH2 (pi-1) is the last fallback
- pi2_value(kw, kws, table, bid)  table lookup + context rules (see CONTEXT RULES below)
- prior(kw)                   the values the same Pāli keyword got in the pi-1/3/4/5 Hindi maps (lookup aid)
- build_part(ch, resolver)    writes <ch>.mapped.md; stops on unmapped keywords / ", " in a value
- verify(ch)                  the brief's structural check + presence check; prints a report
usage (sample): python -I -X utf8 map_sample_hi.py
"""
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-hi" / "mapper-hi"))
from map_common_hi import CH2, present, lc, NDE, GAP  # noqa: E402  (read-only import)

HI_DIR = ROOT / "AI_translation" / "hindi" / "pi-2-hindi-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"
PRIOR_MAPS = [ROOT / "AI_translation" / "hindi" / f"pi-{n}-keywords-by-reference-pali-hindi-plain.md"
              for n in (1, 3, 4, 5)]
PP_SEGMENTS = set()   # Pañhāpucchaka segments get the negation variants (filled per chapter, see NEG_VARIANTS)


# ---------------------------------------------------------------------------- reading
def read_keywords(ch):
    out = []
    for line in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines():
        if line.strip():
            bid, rest = line.split("] ", 1)
            out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def _segments(path):
    segs = {}
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
        block = block.strip()
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", block)
        if m:
            segs[m.group(1)] = block[: m.start()].strip()
    return segs


def read_hindi(ch):
    return _segments(HI_DIR / f"{ch}.md")


def read_pali(ch):
    return _segments(PI_DIR / f"{ch}.md")


_PRIOR = None


def prior(kw):
    """{book: Counter(values)} for this keyword in the finished pi-1/3/4/5 Hindi maps."""
    global _PRIOR
    if _PRIOR is None:
        _PRIOR = collections.defaultdict(collections.Counter)
        for n, p in zip((1, 3, 4, 5), PRIOR_MAPS):
            for line in p.read_text(encoding="utf-8").splitlines():
                if "] " in line:
                    for pair in line.split("] ", 1)[1].split(", "):
                        if "=" in pair:
                            k, v = pair.split("=", 1)
                            _PRIOR[(n, lc(k.strip()))][v] += 1
    return {n: _PRIOR[(n, lc(kw))] for n in (1, 3, 4, 5) if (n, lc(kw)) in _PRIOR}


# ---------------------------------------------------------------------------- PI2 default table
# Values: dictionary form (nouns direct sg, adjectives/participles masc. sg, verbs infinitive), pi-1 wording
# where the Pāli is the same; the classification labels are the masculine forms the pi-2 builders made from
# the pi-1 mātikā (they agree with समूह). Phrases containing a noun agree with that noun (pi-1 rule).
PI2 = {}

# --- text frame, headings
PI2.update({
    "abhidhamma": "अभिधम्म", "abhidhammapiṭake": "अभिधम्म पिटक",
    "vibhaṅga": "विस्तृत विश्लेषण", "vibhaṅgapāḷi": "विस्तृत विश्लेषण", "pāḷi": NDE,
    "vibhaṅgo": "विश्लेषण", "bhājanīyaṃ": "विश्लेषण", "suttanta": "उपदेश",
    "pañhā": "प्रश्न", "pañhāpucchakaṃ": "प्रश्नोत्तर", "niṭṭhito": "पूरा हुआ",
    "tikaṃ": "तीन-तीन के वर्गीकरण", "dukaṃ": "दो-दो के वर्गीकरण",
    "tika": "तीन-तीन के वर्गीकरण", "duka": "दो-दो के वर्गीकरण",
    "tikā": "तीन-तीन के वर्गीकरण", "tike": "तीन के वर्गीकरण",          # kusalattike «“हितकर” से शुरू होने वाले तीन के वर्गीकरण»
    "mūlakaṃ": "पर आधारित क्रम", "vaḍḍhakaṃ": "बढ़ने वाला क्रम", "ubhato": "दोनों ओर से",
    "vitthāro": "विस्तार", "kaṇḍe": "अध्याय", "vibhattaṃ": "विश्लेषण किया गया",
    "namo": "नमन", "bhagavato": "भगवान", "arahato": "अर्हत्", "sammā": "पूर्ण रूप से",
    "sambuddhassa": "जागृत बुद्ध", "sammāsambuddhassa": "पूर्ण रूप से जागृत बुद्ध",
    "tattha": "यहाँ",
})

# --- the five aggregates (khandha = समूह)
AGG = {"rūpa": "भौतिक रूप", "vedanā": "अनुभूति", "saññā": "पहचान", "saṅkhāra": "मानसिक रचनाओं",
       "viññāṇa": "चेतना"}
PI2.update({
    "khandha": "समूह", "khandho": "समूह", "khandhā": "समूह", "khandhānaṃ": "समूह",
    "rūpa": "भौतिक रूप", "vedanā": "अनुभूति", "saññā": "पहचान", "saṅkhāra": "मानसिक रचनाएँ",
    "saṅkhārā": "मानसिक रचनाएँ", "viññāṇa": "चेतना", "viññāṇaṃ": "चेतना", "rūpaṃ": "भौतिक रूप",
    "vedanāya": "अनुभूति", "vedanāhi": "अनुभूति", "saññāhi": "पहचान", "viññāṇehi": "चेतना",
    "cetanā": "इरादा",
})
for _p, _h in AGG.items():
    _k = {"rūpa": "rūpakkhandh", "vedanā": "vedanākkhandh", "saññā": "saññākkhandh",
          "saṅkhāra": "saṅkhārakkhandh", "viññāṇa": "viññāṇakkhandh"}[_p]
    for _e in ("o", "aṃ", "assa"):
        PI2[_k + _e] = f"{_h} का समूह"

# --- numbers of ways (Ekavidhena … = एक प्रकार; vidhena = प्रकार, pi-1)
NUMW = {"ekavidhena": "एक", "duvidhena": "दो", "tividhena": "तीन", "catubbidhena": "चार",
        "pañcavidhena": "पाँच", "chabbidhena": "छह", "sattavidhena": "सात", "aṭṭhavidhena": "आठ",
        "navavidhena": "नौ", "dasavidhena": "दस", "ekādasavidhena": "ग्यारह", "catuvīsatividhena": "चौबीस",
        "tiṃsavidhena": "तीस", "tiṃsatividhena": "तीस", "bahuvidhena": "अनेक"}
PI2["vidhena"] = "प्रकार"
for _p, _h in NUMW.items():
    PI2[_p] = f"{_h} प्रकार"
    for _a, _ah in AGG.items():
        _k = {"rūpa": "rūpakkhandho", "vedanā": "vedanākkhandho", "saññā": "saññākkhandho",
              "saṅkhāra": "saṅkhārakkhandho", "viññāṇa": "viññāṇakkhandho"}[_a]
        PI2[f"{_p} {_k}"] = f"{_h} प्रकार से {_ah} का समूह"

# --- Suttanta definitions (atīta/anāgata/paccuppanna, ajjhatta/bahiddhā, oḷārika/sukhuma, hīna/paṇīta,
#     dūre/santike); the participles in masc. sg. (pi-1 / pi-5 wording)
PI2.update({
    "yaṃ kiñci": "जो भी", "yā kāci": "जो भी", "ye keci": "जो भी", "yaṃ vā panaññampi": "या जो भी अन्य",
    "tadekajjhaṃ": "उस सबको एक साथ", "abhisaññūhitvā": "इकट्ठा करके", "abhisaṅkhipitvā": "संक्षेप में समेटकर",
    "vuccati": "कहा जाना", "vuccanti": "कहा जाना",
    "atītaṃ": "अतीत का", "atītā": "अतीत का", "anāgataṃ": "भविष्य का", "anāgatā": "भविष्य का",
    "paccuppannaṃ": "वर्तमान का", "paccuppannā": "वर्तमान का",
    "niruddhaṃ": "समाप्त हो चुका", "vigataṃ": "जा चुका", "vipariṇataṃ": "बदल चुका",
    "abbhatthaṅgataṃ": "पूरी तरह अस्त हो चुका", "uppajjitvā": "उत्पन्न होकर",
    "atītaṃsena": "अतीत के अंतर्गत", "saṅgahitaṃ": "वर्गीकृत", "atītaṃsena saṅgahitaṃ": "अतीत के अंतर्गत वर्गीकृत",
    "jātaṃ": "जन्मा हुआ", "nibbattaṃ": "पैदा हुआ", "abhinibbattaṃ": "पूरी तरह पैदा हुआ",
    "pātubhūtaṃ": "प्रकट हुआ", "uppannaṃ": "उत्पन्न", "uṭṭhitaṃ": "उठा हुआ", "samuṭṭhitaṃ": "भली-भाँति उठा हुआ",
    "upādāya": "व्युत्पन्न", "bhūtā": "महाभूत", "mahābhūtā": "महाभूत", "upādāyarūpaṃ": "व्युत्पन्न भौतिक रूप",
    "ajjhattaṃ": "स्वयं में", "paccattaṃ": "अपना", "pāṭipuggalikaṃ": "हर व्यक्ति का निजी",
    "parapuggalānaṃ": "दूसरा व्यक्ति",
    "oḷārikaṃ": "स्थूल", "sukhumaṃ": "सूक्ष्म", "hīnaṃ": "हीन", "paṇītaṃ": "उत्तम",
    "upādāyupādāya": "तुलना करके", "daṭṭhabbaṃ": "समझना चाहिए", "upakaṭṭhe": "समीप",
    "uññātaṃ": "तुच्छ समझा गया", "avaññātaṃ": "तिरस्कृत", "hīḷitaṃ": "निंदित", "paribhūtaṃ": "अपमानित",
    "acittīkataṃ": "असम्मानित", "cittīkataṃ": "सम्मानित", "hīnamataṃ": "हीन माना गया",
    "aniṭṭhaṃ": "अनचाहा", "akantaṃ": "अप्रिय", "amanāpaṃ": "मन को न भाने वाला",
    "iṭṭhaṃ": "मनचाहा", "kantaṃ": "प्रिय", "manāpaṃ": "मनभावन",
    "rūpā": "दृश्य रूप", "saddā": "ध्वनि", "gandhā": "गंध", "rasā": "स्वाद", "phoṭṭhabbā": "स्पर्श",
    "samāpannassa": "ध्यान-अवस्था में लीन व्यक्ति",
    "paṭighasamphassa": "टकराव वाला संपर्क", "paṭighasamphassajā": "टकराव वाले संपर्क से उत्पन्न",
    "adhivacanasamphassa": "नाम वाला संपर्क", "adhivacanasamphassajā": "नाम वाले संपर्क से उत्पन्न",
    "sukhadukkhā": "सुखद और दुःखद", "sukhadukkhāhi": "सुखद और दुःखद",
    "kusalābyākatā": "हितकर और नैतिक रूप से अनिर्धारित", "kusalākusalā": "हितकर और हानिकर",
})
for _s, _f in (("aṃ", "ā"),):   # feminine / plural surface forms of the same participles
    for _k in ("niruddh", "vigat", "vipariṇat", "abbhatthaṅgat", "saṅgahit", "jāt", "nibbatt", "abhinibbatt",
               "pātubhūt", "uṭṭhit", "samuṭṭhit", "pāṭipuggalik", "oḷārik", "sukhum", "hīn", "paṇīt", "daṭṭhabb"):
        PI2[_k + _f] = PI2[_k + _s]
PI2["uppannā"] = "उत्पन्न"
PI2["atītaṃsena saṅgahitā"] = PI2["atītaṃsena saṅgahitaṃ"]

# --- feeling / contact terms
SENSE = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर", "mano": "मन"}
for _p, _h in SENSE.items():
    PI2[_p + "samphassa"] = f"{_h} का संपर्क"
    PI2[_p + "samphassajā"] = f"{_h} के संपर्क से उत्पन्न"
    PI2[_p + "viññāṇaṃ"] = f"{_h} की चेतना"
    PI2[_p + "viññeyyaṃ"] = f"{_h} से जाना जा सकने वाला"
    for _n, _nh in (("vedanā", "अनुभूति"), ("saññā", "पहचान"), ("cetanā", "इरादा")):
        PI2[f"{_p}samphassajā {_n}"] = f"{_h} के संपर्क से उत्पन्न {_nh}"
PI2.update({
    "phassa": "संपर्क", "samphassa": "संपर्क", "samphassajā": "संपर्क से उत्पन्न", "samphassaṃ": "संपर्क वाला",
    "phassasampayutto": "संपर्क से जुड़ा", "cittasampayutto": "मन से जुड़ा", "cittasampayuttā": "मन से जुड़ा",
    "sukhā": "सुखद", "dukkhā": "दुःखद", "sukhāya": "सुखद", "dukkhāya": "दुःखद", "adukkhamasukhā": "न दुःखद न सुखद",
    "adukkhamasukhāya": "न दुःखद न सुखद", "dukkha": "दुःखद", "sukha": "सुख",
    "sukhā vedanā": "सुखद अनुभूति", "dukkhā vedanā": "दुःखद अनुभूति",
    "sukhāya vedanāya": "सुखद अनुभूति", "dukkhāya vedanāya": "दुःखद अनुभूति", "dukkhāhi vedanāhi": "दुःखद अनुभूति",
    "indriya": "क्षमता", "indriyaṃ": "क्षमता",
    "sukhindriya": "सुख की क्षमता", "dukkhindriya": "दुःख की क्षमता", "somanassindriya": "प्रसन्नता की क्षमता",
    "domanassindriya": "उदासी की क्षमता", "upekkhindriya": "समभाव की क्षमता",
    "sukhindriyaṃ": "सुख की क्षमता", "dukkhindriyaṃ": "दुःख की क्षमता", "somanassindriyaṃ": "प्रसन्नता की क्षमता",
    "domanassindriyaṃ": "उदासी की क्षमता", "upekkhindriyaṃ": "समभाव की क्षमता",
    "sukhindriyasampayutto": "सुख की क्षमता से जुड़ा",
    "dhātu": "तत्व", "viññāṇadhātu": "चेतना का तत्व", "manodhātu": "मन का तत्व",
    "manoviññāṇa": "मन की चेतना", "manoviññāṇadhātu": "मन की चेतना का तत्व", "mano": "मन",
    "paccayā": "के कारण होने वाला",
})

# --- material form (Rūpakaṇḍa wording, pi-1)
PI2.update({
    "cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र", "sotāyatanaṃ": "कान का इंद्रिय-क्षेत्र",
    "ghānāyatanaṃ": "नाक का इंद्रिय-क्षेत्र", "jivhāyatanaṃ": "जीभ का इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ": "शरीर का इंद्रिय-क्षेत्र", "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र",
    "saddāyatanaṃ": "ध्वनि का इंद्रिय-क्षेत्र", "gandhāyatanaṃ": "गंध का इंद्रिय-क्षेत्र",
    "rasāyatanaṃ": "स्वाद का इंद्रिय-क्षेत्र", "phoṭṭhabbāyatanaṃ": "स्पर्श का इंद्रिय-क्षेत्र",
    "āyatanaṃ": "इंद्रिय-क्षेत्र", "dhammāyatana": "मन के विषयों का इंद्रिय-क्षेत्र",
    "cakkhundriyaṃ": "आँख की क्षमता", "sotindriyaṃ": "कान की क्षमता", "ghānindriyaṃ": "नाक की क्षमता",
    "jivhindriyaṃ": "जीभ की क्षमता", "kāyindriyaṃ": "शरीर की क्षमता", "itthindriyaṃ": "स्त्रीत्व की क्षमता",
    "purisindriyaṃ": "पुरुषत्व की क्षमता", "jīvitindriyaṃ": "जीवन-क्षमता",
    "kabaḷīkāro": "कौर-कौर खाया जाने वाला", "āhāro": "भोजन", "viññatti": "प्रकट अभिव्यक्ति",
    "pathavī": "पृथ्वी", "āpo": "जल", "tejo": "अग्नि", "vāyo": "वायु",
    "pathavīdhātu": "पृथ्वी तत्व", "āpodhātu": "जल तत्व", "tejodhātu": "अग्नि तत्व", "vāyodhātu": "वायु तत्व",
    "upādā": "व्युत्पन्न", "rūpaṃ upādā": "भौतिक रूप व्युत्पन्न", "rūpaṃ cittasamuṭṭhānaṃ": "भौतिक रूप मन से उत्पन्न",
    "viññeyyaṃ": "जाना जा सकने वाला", "viññeyyaṃ rūpaṃ": "जाना जा सकने वाला भौतिक रूप",
    "sutaṃ": "सुना हुआ", "mutaṃ": "अनुभव किया हुआ", "viññātaṃ": "जाना हुआ",
    "aniccaṃ": "अनित्य", "jarābhibhūtaṃ": "बुढ़ापे से ग्रस्त", "ābhibhūtaṃ": "ग्रस्त",
    "ajjhattikaṃ": "आंतरिक", "ajjhattiko": "आंतरिक", "bāhiraṃ": "बाह्य", "bāhirā": "बाह्य",
    "sanidassanaṃ": "दिखाई देने वाला", "anidassanaṃ": "दिखाई न देने वाला", "sappaṭighaṃ": "टकराव वाला",
    "samuṭṭhānaṃ": "उत्पन्न", "samuṭṭhānā": "उत्पन्न", "sahabhu": "साथ-साथ होने वाला",
    "sahabhuno": "साथ-साथ होने वाला", "ānuparivatti": "अनुसरण करने वाला", "ānuparivattino": "अनुसरण करने वाला",
    "saha": "साथ", "mattaṃ": "केवल",
})

# --- classification labels (pi-1 mātikā wording, masc. sg.; = LEX of build_1-khandhavibhango_hi.py)
LABELS = {
    "kusala": "हितकर", "kusalo": "हितकर", "kusalā": "हितकर", "kusalaṃ": "हितकर",
    "akusalo": "हानिकर", "akusalā": "हानिकर", "akusalaṃ": "हानिकर",
    "abyākato": "नैतिक रूप से अनिर्धारित", "abyākatā": "नैतिक रूप से अनिर्धारित", "abyākataṃ": "नैतिक रूप से अनिर्धारित",
    "vipākadhammadhammo": "कर्म-फल उत्पन्न करने वाला", "vipākadhammadhammā": "कर्म-फल उत्पन्न करने वाला",
    "vipākadhammadhammaṃ": "कर्म-फल उत्पन्न करने वाला",
    "upādāniyo": "आसक्ति का विषय बनने वाला", "upādāniyaṃ": "आसक्ति का विषय बनने वाला",
    "saṃkiliṭṭha": "क्लेशों से मलिन", "asaṃkiliṭṭha": "क्लेशों से मलिन न होने वाला",
    "saṃkiliṭṭho": "क्लेशों से मलिन", "saṃkiliṭṭhā": "क्लेशों से मलिन", "asaṃkiliṭṭho": "क्लेशों से मलिन न होने वाला",
    "saṃkilesiko": "क्लेशों का विषय बनने वाला", "saṃkilesikaṃ": "क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhasaṃkilesiko": "क्लेशों से मलिन न होने वाला पर क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhaasaṃkilesiko": "क्लेशों से मलिन न होने वाला और क्लेशों का विषय न बनने वाला",
    "vitakka": "आरंभिक विचार", "vitakko": "आरंभिक विचार", "vicāro": "सतत विचार", "vicāraṃ": "सतत विचार",
    "savitakkasavicāro": "आरंभिक विचार और सतत विचार वाला", "savitakkasavicārā": "आरंभिक विचार और सतत विचार वाला",
    "savitakkasavicāraṃ": "आरंभिक विचार और सतत विचार वाला",
    "avitakkavicāramatto": "आरंभिक विचार से रहित केवल सतत विचार वाला",
    "avitakko": "आरंभिक विचार से रहित", "savicāro": "सतत विचार वाला", "avicāro": "सतत विचार से रहित",
    "pīti": "उल्लास", "upekkhā": "समभाव",
    "sahagato": "के साथ होने वाला", "sahagatā": "के साथ होने वाला", "sahagataṃ": "के साथ होने वाला",
    "pītisahagato": "उल्लास के साथ होने वाला", "pītisahagataṃ": "उल्लास के साथ होने वाला",
    "sukhasahagato": "सुख के साथ होने वाला", "sukhasahagatā": "सुख के साथ होने वाला",
    "sukhasahagataṃ": "सुख के साथ होने वाला",
    "upekkhāsahagato": "समभाव के साथ होने वाला", "upekkhāsahagatā": "समभाव के साथ होने वाला",
    "upekkhāsahagataṃ": "समभाव के साथ होने वाला", "na pītisahagato": "उल्लास के साथ न होने वाला",
    "dassanena": "सत्य-दर्शन", "bhāvanāya": "मानसिक अभ्यास",
    "pahātabbo": "छोड़ा जाने वाला", "pahātabba": "छोड़ा जाने वाला", "pahātabbaṃ": "छोड़ा जाने वाला",
    "pahātabbahetuko": "छोड़े जाने वाले मूलों वाला", "hetukā": "मूलों वाला", "hetukaṃ": "मूलों वाला",
    "ācaya": "संचय", "apacaya": "संचय घटाना", "āpacaya": "संचय घटाना", "gāmī": "की ओर ले जाने वाला",
    "ācayagāmī": "संचय की ओर ले जाने वाला", "apacayagāmī": "संचय घटाने की ओर ले जाने वाला",
    "sekkha": "सीखने के चरण का", "sekkho": "सीखने के चरण का", "sekkhā": "सीखने के चरण का",
    "asekkho": "सीखना पूरा होने के चरण का", "asekkhā": "सीखना पूरा होने के चरण का",
    "āsekkhaṃ": "सीखना पूरा होने के चरण का",
    "paritto": "सीमित", "parittaṃ": "सीमित", "mahaggato": "उन्नत", "mahaggatā": "उन्नत",
    "appamāṇo": "अपरिमित", "appamāṇā": "अपरिमित",
    "ārammaṇo": "विषय वाला", "parittārammaṇo": "सीमित विषय वाला", "parittārammaṇā": "सीमित विषय वाला",
    "mahaggatārammaṇo": "उन्नत विषय वाला", "mahaggatārammaṇā": "उन्नत विषय वाला",
    "appamāṇārammaṇo": "अपरिमित विषय वाला", "appamāṇārammaṇā": "अपरिमित विषय वाला",
    "hīno": "हीन", "majjhimo": "मध्यम", "paṇīto": "उत्तम",
    "micchatta": "ग़लत दिशा", "sammatta": "सही दिशा", "micchattaniyato": "ग़लत दिशा में निश्चित",
    "niyato": "निश्चित", "niyatā": "निश्चित", "aniyato": "अनिश्चित", "aniyataṃ": "अनिश्चित",
    "magga": "मार्ग", "ādhipati": "प्रधानता वाला", "ādhipatino": "प्रधानता वाला",
    "uppanno": "उत्पन्न हो चुका", "uppādī": "उत्पन्न होने वाला", "uppādino": "उत्पन्न होने वाला",
    "atīto": "अतीत का", "anāgato": "भविष्य का", "paccuppanno": "वर्तमान का",
    "atītārammaṇo": "अतीत के विषय वाला", "atītārammaṇā": "अतीत के विषय वाला",
    "anāgatārammaṇo": "भविष्य के विषय वाला", "anāgatārammaṇā": "भविष्य के विषय वाला",
    "paccuppannārammaṇo": "वर्तमान के विषय वाला", "paccuppannārammaṇā": "वर्तमान के विषय वाला",
    "ajjhatto": "स्वयं से संबंधित", "ajjhattā": "स्वयं से संबंधित", "bahiddho": "दूसरों से संबंधित",
    "bahiddhā": "दूसरों से संबंधित", "ajjhattabahiddho": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattabahiddhā": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattārammaṇo": "स्वयं से संबंधित विषय वाला", "ajjhattārammaṇā": "स्वयं से संबंधित विषय वाला",
    "bahiddhārammaṇo": "दूसरों से संबंधित विषय वाला", "bahiddhārammaṇā": "दूसरों से संबंधित विषय वाला",
    "ajjhattabahiddhārammaṇo": "स्वयं और दूसरों दोनों से संबंधित विषय वाला",
    "ajjhattabahiddhārammaṇā": "स्वयं और दूसरों दोनों से संबंधित विषय वाला",
    "sanidassana": "दिखाई देने वाला", "sanidassano": "दिखाई देने वाला", "anidassana": "दिखाई न देने वाला",
    "anidassanā": "दिखाई न देने वाला", "sappaṭigho": "टकराव वाला",
    "anidassanasappaṭigho": "दिखाई न देने वाला पर टकराव वाला",
    # roots
    "hetu": "मूल", "hetū": "मूल", "sahetuko": "मूल वाला", "ahetuko": "मूल से रहित",
    "hetusampayutto": "मूलों से जुड़ा", "hetusampayuttā": "मूलों से जुड़ा", "hetuvippayutto": "मूलों से अलग",
    "hetu ceva hetusampayutto": "मूल रूपी भी और मूलों से जुड़ा भी",
    "hetū ceva hetusampayuttā": "मूल रूपी भी और मूलों से जुड़ा भी",
    # small intermediate pairs
    "sappaccayaṃ": "कारणों पर निर्भर रहने वाला", "saṅkhataṃ": "निर्मित", "saṅkhatā": "निर्मित",
    "arūpā": "अभौतिक", "lokiyo": "लौकिक", "lokiyaṃ": "लौकिक", "uttaro": "लोकोत्तर", "uttarā": "लोकोत्तर",
    "kenaci": "किसी एक प्रकार की चेतना", "viññeyyo": "जाना जा सकने वाला", "viññeyyā": "जाना जा सकने वाला",
    "kenaci viññeyyo": "किसी एक प्रकार की चेतना से जाना जा सकने वाला",
    "kenaci na viññeyyo": "किसी एक प्रकार की चेतना से न जाना जा सकने वाला",
    # big intermediate pairs
    "sārammaṇā": "विषय वाला", "anārammaṇo": "विषय से रहित", "anārammaṇaṃ": "विषय से रहित",
    "cittaṃ": "मन", "citta": "मन", "cetasikā": "मन का सहचर", "acetasikaṃ": "मन का सहचर न होने वाला",
    "saṃsaṭṭhā": "घुला-मिला", "cittasaṃsaṭṭhā": "मन से घुला-मिला",
    "vippayutto": "अलग", "vippayutta": "अलग", "vippayuttaṃ": "अलग",
    "sampayutto": "जुड़ा", "sampayuttā": "जुड़ा", "sampayuttaṃ": "जुड़ा",
    # later pairs
    "kāmāvacaro": "इंद्रिय-सुखों के लोक से संबंधित", "kāmāvacaraṃ": "इंद्रिय-सुखों के लोक से संबंधित",
    "rūpāvacaro": "सूक्ष्म भौतिक लोक से संबंधित", "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacaro": "अभौतिक लोक से संबंधित", "arūpāvacaraṃ": "अभौतिक लोक से संबंधित",
    "āvacaro": "लोक से संबंधित", "āvacaraṃ": "लोक से संबंधित",
    "na kāmāvacaro": "इंद्रिय-सुखों के लोक से संबंधित न होने वाला",
    "pariyāpanno": "अस्तित्व के लोकों में समाया हुआ",
    "apariyāpanno": "अस्तित्व के लोकों में न समाया हुआ", "apariyāpannā": "अस्तित्व के लोकों में न समाया हुआ",
    "apariyāpannaṃ": "अस्तित्व के लोकों में न समाया हुआ",
    "niyyāniko": "मुक्ति की ओर ले जाने वाला", "sauttaro": "सर्वोच्च न होने वाला", "sauttarā": "सर्वोच्च न होने वाला",
    "anuttarā": "सर्वोच्च", "saraṇo": "संघर्ष वाला", "saraṇā": "संघर्ष वाला", "araṇo": "संघर्ष से रहित",
    "araṇā": "संघर्ष से रहित",
    # the defilement clusters (noun = term, «X रूपी» in the Hindi)
    "kilesa": "क्लेश", "kilesā": "मन के क्लेश",
    "kilesasampayutto": "क्लेशों से जुड़ा", "kilesavippayutto": "क्लेशों से अलग",
    "kileso ceva kilesasampayutto": "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी",
    "kilesā ceva kilesasampayuttā": "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी",
    "na": "न",
    "vattabbo": "कहा जा सकना", "vattabbā": "कहा जा सकना",
}
PI2.update(LABELS)

# clusters: (stem, noun forms, adjective, Hindi noun, Hindi oblique plural, pronoun)
CLUSTERS = [
    ("āsava", ("āsavo", "āsavā", "āsavaṃ"), "sāsav", "मन के मैल", "मन के मैलों", "उनका"),
    ("saṃyojana", ("saṃyojanaṃ", "saṃyojanā"), "saṃyojaniy", "बंधन", "बंधनों", "उनका"),
    ("gantha", ("gantho", "ganthā"), "ganthaniy", "गाँठ", "गाँठों", "उनका"),
    ("ogha", ("ogho", "oghā"), "oghaniy", "बाढ़", "बाढ़ों", "उनका"),
    ("yoga", ("yogo", "yogā"), "yoganiy", "जकड़न", "जकड़नों", "उनका"),
    ("nīvaraṇa", ("nīvaraṇaṃ", "nīvaraṇā"), "nīvaraṇiy", "बाधा", "बाधाओं", "उनका"),
    ("parāmāsa", ("parāmāso", "parāmāsā"), "parāmaṭṭh", "ग़लत धारणा", "ग़लत धारणा", "उसका"),
    ("upādāna", ("upādānaṃ", "upādānā"), "upādāniy", "आसक्ति", "आसक्ति", "उसका"),
]
for _st, _nouns, _adj, _h, _obl, _pr in CLUSTERS:
    PI2[_st] = _h
    for _n in _nouns:
        PI2[_n] = _h
    _a = _adj if _st not in ("āsava",) else "sāsav"
    _na = {"āsava": "anāsav", "upādāna": "anupādāniy", "ogha": "anoghaniy"}.get(_st, "a" + _adj)
    for _e in ("o", "ā", "aṃ"):
        PI2[_a + _e] = f"{_obl} का विषय बनने वाला"
        PI2[_na + _e] = f"{_obl} का विषय न बनने वाला"
    PI2[_st + "sampayutto"] = PI2[_st + "sampayuttā"] = f"{_obl} से जुड़ा"
    PI2[_st + "vippayutto"] = PI2[_st + "vippayuttā"] = f"{_obl} से अलग"
    _adj_o = (_a + "o") if _st != "parāmāsa" else "parāmaṭṭho"
    PI2[f"{_st}vippayutta{_adj_o}"] = f"{_obl} से अलग पर {_pr} विषय बनने वाला"
    PI2[f"{_st}vippayutta{_na}o"] = f"{_obl} से अलग और {_pr} विषय न बनने वाला"
    for _n in _nouns:
        _nb = _n[:-2] + "añceva" if _n.endswith("aṃ") else _n + " ceva"
        PI2[f"{_nb} {_st}sampayutto"] = PI2[f"{_nb} {_st}sampayuttā"] = f"{_h} रूपी भी और {_obl} से जुड़ा भी"
PI2["parāmaṭṭhaṃ"] = "ग़लत धारणा का विषय बनने वाला"

# Pañhāpucchaka frames (subject + siyā)
PI2.update({
    "khandhā siyā": "समूह कभी", "khandhā cittasaṃsaṭṭhā": "समूह मन से घुला-मिला",
    "rūpakkhandho hetuvippayutto": "भौतिक रूप का समूह मूलों से अलग",
})


# ---------------------------------------------------------------------------- context rules
# Pañhāpucchaka negation: where a «… न होने वाला» label is said as a predicate the Hindi has «… नहीं»
# (harmonise rule PP3); the value then follows the Hindi.
def _variants(v):
    """Fallbacks tried, in order, when v is absent from the segment's Hindi:
    - Pañhāpucchaka predicate negation: «X न होने वाला» -> «X नहीं» (harmonise rule PP3);
    - the second member of «Y-vippayutta-X-niya» pairs: «Yों का विषय (न) बनने वाला» -> «उनका/उसका विषय …»
      (pi-1 closing-pair rule: «… से अलग, पर उनका विषय बनने वाला»)."""
    out = []
    if v.endswith(" न होने वाला"):
        out.append(v[: -len(" न होने वाला")] + " नहीं")
    m = re.match(r"^.+ का (विषय (?:न )?बनने वाला)$", v)
    if m:
        out += ["उनका " + m.group(1), "उसका " + m.group(1)]
    return out


def pi2_value(kw, kws, table=PI2, bid=None, text=None):
    """Default Hindi for a keyword: table lookup + context rules. With text (the segment's Hindi), a value
    that is absent there falls back to its Pañhāpucchaka negation variant when that one is present."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k == "hetuko":                                   # pahātabbahetuko / maggahetuko vs sahetuko / ahetuko
        v = ("मूलों वाला" if any(x.startswith("pahātabb") for x in s)
             else "मूल बनाने वाला" if "magga" in s else "मूल वाला")
    elif k == "ārammaṇo" and "magga" in s and not any(x.endswith("ārammaṇo") and x != k for x in s):
        v = "विषय बनाने वाला"                            # only maggārammaṇo: «मार्ग को विषय बनाने वाला» (pi-1 1-M1-16)
    elif k == "na" and bid in PP_SEGMENTS:              # na vattabbo / na hetū …: «नहीं …»
        v = "नहीं"
    elif k in table:
        v = table[k]
    elif k in CH2:
        v = CH2[k]
    else:
        raise KeyError(kw)
    if text is not None and v != NDE and not present(v, text):
        for alt in _variants(v):
            if present(alt, text):
                return alt
    return v


# ---------------------------------------------------------------------------- build and verify
def build_part(ch, resolver):
    """resolver(bid, kw, kws) -> Hindi value. Raises SystemExit listing unmapped keywords."""
    lines, missing = [], []
    for bid, kws in read_keywords(ch):
        pairs = []
        for kw in kws:
            try:
                v = resolver(bid, kw, kws)
            except KeyError:
                missing.append((bid, kw))
                v = "???"
            assert ", " not in v, (bid, kw, v)
            pairs.append(f"{kw}={v}")
        lines.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        raise SystemExit(f"{ch}: unmapped keywords: {missing}")
    (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(ch, show=60, allowed=None):
    """allowed: {(bid, kw)} presence exceptions with a reason (listed, not counted as misses)."""
    allowed = allowed or {}
    a = [l.split("] ", 1) for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    hi = read_hindi(ch)
    nde, miss, exc = 0, [], []
    for bid, rest in b:
        bid = bid[1:]
        text = hi.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
            elif text is None or not present(v, text):
                (exc if (bid, kw) in allowed else miss).append((bid, kw, v))
    print(ch, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss),
          "| listed exceptions", len(exc))
    for m in miss[:show]:
        print("   MISS", *m)
    for e in exc:
        print("   EXC ", *e, "--", allowed[(e[0], e[1])])
    return bad, nde, miss


# ============================================================================ the sample
# ---- preamble
PREAMBLE_OVR = {}

# ---- 1-khandhavibhango
PP_SEGMENTS.update({"2-151", "2-152", "2-153"})
KH_T = {
    # phrases of the Suttanta definitions (noun + attribute: the Hindi agrees with the noun)
    "vuccati rūpaṃ": "भौतिक रूप कहा जाता है", "vuccati vedanā": "अनुभूति कही जाती है",
    "vuccati saññā": "पहचान कही जाती है", "vuccati viññāṇaṃ": "चेतना कही जाती है",
    "vuccanti saṅkhārā": "मानसिक रचनाएँ कही जाती हैं",
    "vuccati vedanā atītā": "अतीत की अनुभूति कही जाती है",
    "rūpaṃ atītaṃ": "अतीत का भौतिक रूप", "rūpaṃ anāgataṃ": "भविष्य का भौतिक रूप",
    "rūpaṃ paccuppannaṃ": "वर्तमान का भौतिक रूप", "rūpaṃ oḷārikaṃ": "स्थूल भौतिक रूप",
    "rūpaṃ sukhumaṃ": "सूक्ष्म भौतिक रूप", "rūpaṃ hīnaṃ": "हीन भौतिक रूप", "rūpaṃ paṇītaṃ": "उत्तम भौतिक रूप",
    "vedanā atītā": "अतीत की अनुभूति", "vedanā anāgatā": "भविष्य की अनुभूति",
    "vedanā paccuppannā": "वर्तमान की अनुभूति", "vedanā oḷārikā": "अनुभूति स्थूल",
    "vedanā hīnā": "अनुभूति हीन", "vedanā paṇītā": "अनुभूति उत्तम",
    "saññā atītā": "अतीत की पहचान", "saññā anāgatā": "भविष्य की पहचान", "saññā paccuppannā": "वर्तमान की पहचान",
    "saṅkhārā oḷārikā": "मानसिक रचनाएँ स्थूल",
    "viññāṇaṃ atītaṃ": "अतीत की चेतना", "viññāṇaṃ anāgataṃ": "भविष्य की चेतना",
    "viññāṇaṃ paccuppannaṃ": "वर्तमान की चेतना", "viññāṇaṃ oḷārikaṃ": "चेतना स्थूल",
    "viññāṇaṃ sukhumaṃ": "चेतना सूक्ष्म",
    "vuccati rūpakkhandho": "भौतिक रूप का समूह कहा जाता है",
    "vuccati vedanākkhandho": "अनुभूति का समूह कहा जाता है",
    "vuccati saññākkhandho": "पहचान का समूह कहा जाता है",
    "vuccati saṅkhārakkhandho": "मानसिक रचनाओं का समूह कहा जाता है",
    "vuccati viññāṇakkhandho": "चेतना का समूह कहा जाता है",
    # «हानिकर अनुभूति», «मन के मैलों का विषय बनने वाली पहचान» …
    "akusalā vedanā": "हानिकर अनुभूति", "kusalā vedanā": "हितकर अनुभूति",
    "abyākatā vedanā": "नैतिक रूप से अनिर्धारित अनुभूति", "sāsavā vedanā": "मन के मैलों का विषय बनने वाली अनुभूति",
    "anāsavā vedanā": "मन के मैलों का विषय न बनने वाली अनुभूति",
    "ābyākatāhi vedanāhi": "नैतिक रूप से अनिर्धारित अनुभूति",
    "akusalā saññā": "हानिकर पहचान", "kusalā saññā": "हितकर पहचान",
    "abyākatā saññā": "नैतिक रूप से अनिर्धारित पहचान", "sāsavā saññā": "मन के मैलों का विषय बनने वाली पहचान",
    "anāsavā saññā": "मन के मैलों का विषय न बनने वाली पहचान", "sampayuttā saññā": "जुड़ी पहचान",
    "sampayuttāhi saññāhi": "जुड़ी पहचान", "ābyākatāhi saññāhi": "नैतिक रूप से अनिर्धारित पहचान",
    "akusalābyākatāhi saññāhi": "हानिकर और नैतिक रूप से अनिर्धारित पहचान",
    "paṭighasamphassajā saññā": "टकराव वाले संपर्क से उत्पन्न पहचान",
    "adhivacanasamphassajā saññā": "नाम वाले संपर्क से उत्पन्न पहचान",
    "akusalā saṅkhārā": "हानिकर मानसिक रचनाएँ", "kusalā saṅkhārā": "हितकर मानसिक रचनाएँ",
    "abyākatā saṅkhārā": "नैतिक रूप से अनिर्धारित मानसिक रचनाएँ",
    "sāsavā saṅkhārā": "मन के मैलों का विषय बनने वाली मानसिक रचनाएँ",
    "anāsavā saṅkhārā": "मन के मैलों का विषय न बनने वाली मानसिक रचनाएँ",
    "sampayuttā saṅkhārā": "जुड़ी मानसिक रचनाएँ",
    "akusalaṃ viññāṇaṃ": "हानिकर चेतना", "kusalaṃ viññāṇaṃ": "हितकर चेतना",
    "abyākataṃ viññāṇaṃ": "नैतिक रूप से अनिर्धारित चेतना",
    "sāsavaṃ viññāṇaṃ": "मन के मैलों का विषय बनने वाली चेतना",
    "anāsavaṃ viññāṇaṃ": "मन के मैलों का विषय न बनने वाली चेतना", "sampayuttaṃ viññāṇaṃ": "जुड़ी चेतना",
    "vedanāya sampayutto": "अनुभूति से जुड़ा", "vedanāya sampayuttā": "अनुभूति से जुड़ा",
    "vedanāya sampayuttaṃ": "अनुभूति से जुड़ा",
    "sukhāya vedanāya sampayutto": "सुखद अनुभूति से जुड़ा", "sukhāya vedanāya sampayuttā": "सुखद अनुभूति से जुड़ा",
    "sukhāya vedanāya sampayuttaṃ": "सुखद अनुभूति से जुड़ा",
    "dukkhāya vedanāya sampayutto": "दुःखद अनुभूति से जुड़ा", "dukkhāya vedanāya sampayuttā": "दुःखद अनुभूति से जुड़ा",
    "dukkhāya vedanāya sampayuttaṃ": "दुःखद अनुभूति से जुड़ा",
}
KH_TABLE = {**PI2, **KH_T}

# per-segment overrides {bid: {kw (exact spelling): value}}; reasons in hi-map-conventions-pi2.md
KH_OVR = {
    "2-20": {"tadekajjhaṃ": "उन सबको एक साथ"},        # plural subject (मानसिक रचनाएँ): «उन सबको»
    "2-152": {"uppannā": "उत्पन्न हो चुका"},           # matrix label (siyā uppannā «उत्पन्न हो चुके होते हैं»),
}                                                       # not the Suttanta participle «उत्पन्न» of 2-9/2-15/2-21


def kh_resolver(bid, kw, kws, _hi={}):
    if not _hi:
        _hi.update(read_hindi("1-khandhavibhango"))
    o = KH_OVR.get(bid, {})
    if kw in o:
        return o[kw]
    return pi2_value(kw, kws, KH_TABLE, bid, _hi.get(bid))


def pre_resolver(bid, kw, kws):
    o = PREAMBLE_OVR.get(bid, {})
    if kw in o:
        return o[kw]
    return pi2_value(kw, kws, PI2, bid)


# presence exceptions (bid, kw) -> reason
KH_ALLOWED = {
    ("2-153", "apariyāpannā"): "text «न समाए हुए»: समाया ~ समाए is regular inflection the checker does not model",
}

if __name__ == "__main__":
    build_part("preamble", pre_resolver)
    verify("preamble")
    build_part("1-khandhavibhango", kh_resolver)
    verify("1-khandhavibhango", allowed=KH_ALLOWED)
