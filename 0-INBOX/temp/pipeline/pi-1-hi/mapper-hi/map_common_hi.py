"""Shared helpers and tables for the pi-1 Pāli->Hindi keyword maps (mapper-hi/).

Importing this module has no side effects (no file is written, nothing printed).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_hi import *

Main pieces
- read_keywords(part)            -> [(id, [kw, ...]), ...]   from <part>.keywords.md
- read_hindi(part) / read_pali(part) -> {id: segment text}   (segments end with ^id)
- present(value, text)           -> True if a Hindi value occurs (regular inflection allowed) in text
- CH2                            -> default Pāli->Hindi table for the cittuppāda chapters (2-01 ... 2-05)
- ch2_value(kw, kws)             -> CH2 lookup with the context rules (samaye X, dhamma, ṭhiti, mano, ...)
- build_part(part, resolver)     -> writes <part>.mapped.md; resolver(id, kw, kws) returns the Hindi
- verify(part)                   -> the brief's structural check + the presence check; prints a report
"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
HI_DIR = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
NDE = "(no direct equivalent)"
GAP = " … "  # discontinuous Hindi (e.g. samaye X = «उस समय … X»)


# ---------------------------------------------------------------------------- reading
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def _segments(path):
    segs = {}
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
        block = block.strip()
        if not block:
            continue
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", block)
        if m:
            segs[m.group(1)] = block[: m.start()].strip()
    return segs


def read_hindi(part):
    return _segments(HI_DIR / f"{part}.md")


def read_pali(part):
    return _segments(PI_DIR / f"{part}.md")


# ---------------------------------------------------------------------------- presence check
DEV = "ऀ-ॿ"
SUFFIXES = sorted(["ियाँ", "ियों", "ाएँ", "ाओं", "ाएं", "एँ", "ओं", "ों", "ें", "ीं", "ाँ",
                   "ना", "ने", "नी", "ा", "ी", "े", "ो"], key=len, reverse=True)
ALT = {"का": "(?:का|की|के)", "की": "(?:का|की|के)", "के": "(?:का|की|के)",
       "गया": "(?:गया|गए|गई|गयी)", "है": "(?:है|हैं)", "हैं": "(?:है|हैं)", "हुआ": "(?:हुआ|हुए|हुई)", "हुई": "(?:हुआ|हुए|हुई)"}


def _norm(t):
    t = re.sub(r"\s*\[[^\]]*\]", "", t)          # variant brackets
    t = t.replace("ेपन", "ापन")                    # कड़ेपन ~ कड़ापन, टेढ़ेपन ~ टेढ़ापन
    t = re.sub(r"[,;:–—…“”‘’?।.()]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _subpart(p):
    if p in ALT:
        return ALT[p]
    if len(p) <= 2:
        return re.escape(p) + f"(?![{DEV}])"
    for s in SUFFIXES:
        if p.endswith(s) and len(p) - len(s) >= 2:
            return re.escape(p[: -len(s)]) + f"[{DEV}]*"
    return re.escape(p) + f"[{DEV}]*"


def _token(tok):
    return "-".join(_subpart(p) for p in tok.split("-"))


def _pattern(phrase):
    toks = _norm(phrase).split()
    body = r"\s+(?:न\s+)?".join(_token(t) for t in toks)   # a dropped negative may intervene
    return re.compile(f"(?<![{DEV}]){body}")


def present(value, text):
    if value == NDE:
        return True
    t = _norm(text)
    for part in re.split(r" … | / ", value):
        if part.strip() and not _pattern(part).search(t):
            return False
    return True


# ---------------------------------------------------------------------------- CH2 default table
# Pāli keyword (as the keyword files spell it, lower-case first letter) -> Hindi dictionary form.
CH2 = {
    # frame / opening of each type of mind
    "kusalā": "हितकर", "kusalaṃ": "हितकर", "kusala": "हितकर",
    "kusalaṃ cittaṃ": "हितकर मन", "dhammā kusalā": "हितकर परिघटना",
    "akusalānaṃ": "हानिकर", "akusalānaṃ dhammānaṃ": "हानिकर परिघटना",
    "kāma": "इंद्रिय-सुख", "kāmāvacaraṃ": "इंद्रिय-सुखों के लोक से संबंधित",
    "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित",
    "avacaraṃ": "लोक से संबंधित", "avacara": "लोक से संबंधित",
    "cittaṃ": "मन", "citta": "मन", "cittassa": "मन", "cittāni": "मन",
    "uppannaṃ": "उत्पन्न", "uppāda": "उत्पत्ति", "cittuppāda": "मन की उत्पत्ति", "kaṇḍaṃ": "अध्याय",
    "sahagataṃ": "के साथ होना", "somanassasahagataṃ": "प्रसन्नता के साथ होना",
    "upekkhāsahagataṃ": "समभाव के साथ होना", "somanassa": "प्रसन्नता", "upekkhā": "समभाव",
    "somanassindriyaṃ": "प्रसन्नता की क्षमता", "upekkhindriyaṃ": "समभाव की क्षमता",
    "ñāṇa": "ज्ञान", "sampayuttaṃ": "जुड़ा", "vippayuttaṃ": "अलग", "ñāṇavippayuttaṃ": "ज्ञान से अलग",
    "saṅkhārena": "प्रेरणा",
    "rūpa": "दृश्य रूप", "sadda": "ध्वनि", "gandha": "गंध", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श",
    "ārammaṇaṃ": "विषय", "ārabbha": "विषय बनाना", "yaṃ yaṃ": "जिस किसी",
    "samuppannā": "उत्पन्न", "samuppannā arūpino": "उत्पन्न अभौतिक",
    "samuppannā arūpino dhammā": "उत्पन्न अभौतिक परिघटना",
    "paṭicca": "परस्पर-आश्रित", "paṭiccasamuppannā": "परस्पर-आश्रित रूप से उत्पन्न",
    "paṭiccasamuppannā arūpino": "परस्पर-आश्रित रूप से उत्पन्न अभौतिक",
    "arūpino": "अभौतिक", "arūpino dhammā": "अभौतिक परिघटना",
    "arūpīnaṃ": "अभौतिक", "arūpīnaṃ dhammānaṃ": "अभौतिक परिघटना",
    "yo": "जो", "yā": "जो", "yaṃ": "जो", "ye": "जो",
    "ṭhapetvā": "छोड़कर",
    # contact, feeling, perception, intention, mind
    "phasso": "संपर्क", "phassa": "संपर्क", "phusanā": "छूना", "saṃphusanā": "भली-भाँति छूना",
    "vedanā": "अनुभूति", "vedayitaṃ": "अनुभव",
    "saññā": "पहचान", "sañjānanā": "पहचानना", "sañjānitattaṃ": "पहचान चुका होना",
    "cetanā": "इरादा", "sañcetanā": "इरादा करना", "cetayitattaṃ": "इरादा कर चुका होना",
    "manosañcetanā": "मानसिक इरादा", "mano": "मानस", "āhāro": "आहार", "āhārā": "आहार",
    "mānasaṃ": "मानसिक क्रिया", "hadayaṃ": "हृदय", "paṇḍaraṃ": "उज्ज्वलता",
    "mana": "मन", "manāyatanaṃ": "मन का इंद्रिय-क्षेत्र", "manindriyaṃ": "मन की क्षमता",
    "viññāṇaṃ": "चेतना", "viññāṇa": "चेतना",
    "khandho": "समूह", "khandhā": "समूह", "khandhassa": "समूह",
    "viññāṇakkhandho": "चेतना का समूह", "viññāṇakkhandhaṃ": "चेतना का समूह",
    "viññāṇakkhandhassa": "चेतना का समूह",
    "vedanākkhandho": "अनुभूति का समूह", "vedanākkhandhaṃ": "अनुभूति का समूह",
    "vedanākkhandhassa": "अनुभूति का समूह",
    "saññākkhandho": "पहचान का समूह", "saññākkhandhaṃ": "पहचान का समूह",
    "saññākkhandhassa": "पहचान का समूह",
    "saṅkhārakkhandho": "मानसिक रचनाओं का समूह", "saṅkhārakkhandhaṃ": "मानसिक रचनाओं का समूह",
    "saṅkhārakkhandhassa": "मानसिक रचनाओं का समूह",
    "saṅkhāra": "मानसिक रचनाएँ",
    "tajjā": "उसके अनुरूप", "dhātu": "तत्व", "dhātuyo": "तत्व",
    "manoviññāṇa": "मन की चेतना", "manoviññāṇadhātu": "मन की चेतना का तत्व",
    "dhammāyatanaṃ": "मन के विषयों का इंद्रिय-क्षेत्र", "dhammadhātu": "मन के विषयों का तत्व",
    "āyatanāni": "इंद्रिय-क्षेत्र", "indriyaṃ": "क्षमता", "indriyāni": "क्षमता",
    # feeling string
    "samphassajaṃ": "संपर्क से उत्पन्न", "samphassajā": "संपर्क से उत्पन्न",
    "cetosamphassajaṃ": "मन के संपर्क से उत्पन्न", "cetosamphassajā": "मन के संपर्क से उत्पन्न",
    "cetasikaṃ": "मानसिक", "sātaṃ": "सुहावना", "asātaṃ": "असुहावना",
    "cetasikaṃ sātaṃ": "मानसिक सुहावनापन", "cetasikaṃ sukhaṃ": "मानसिक सुख",
    "sukhaṃ": "सुख", "sukhā": "सुखद", "sukhaṃ vedayitaṃ": "सुखद अनुभव", "sukhā vedanā": "सुखद अनुभूति",
    "adukkhamasukhaṃ": "न दुःखद न सुखद",
    "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ": "मन के संपर्क से उत्पन्न न दुःखद न सुखद अनुभव",
    "cetosamphassajā adukkhamasukhā vedanā": "मन के संपर्क से उत्पन्न न दुःखद न सुखद अनुभूति",
    # vitakka / vicāra / pīti strings
    "vitakko": "आरंभिक विचार", "takko": "सोचना", "saṅkappo": "संकल्प", "appanā": "टिकाना",
    "cetaso": "मन", "abhiniropanā": "विषय की ओर ले जाना",
    "vicāro": "सतत विचार", "cāro": "विचरण", "anusandhānatā": "विषय से जुड़े रहना",
    "anupekkhanatā": "लगातार निहारते रहना",
    "pīti": "उल्लास", "pāmojjaṃ": "आनंद", "āmodanā": "आनंदित होना", "pamodanā": "प्रमुदित होना",
    "hāso": "हर्ष", "pahāso": "महाहर्ष", "vitti": "तृप्ति", "odagyaṃ": "उमंग", "attamanatā": "खिल उठना",
    # samādhi string
    "ekaggatā": "एकाग्रता", "cittassekaggatā": "मन की एकाग्रता",
    "ṭhiti": "स्थिरता", "cittassa ṭhiti": "मन की स्थिरता", "saṇṭhiti": "ठहराव", "avaṭṭhiti": "दृढ़ता",
    "avisāhāro": "बिखराव का अभाव", "avikkhepo": "भटकाव का अभाव", "avisāhaṭa": "न बिखरा",
    "avisāhaṭamānasatā": "मन का न बिखरा होना", "mānasatā": "मन",
    "samatho": "शांति", "samādhi": "एकाग्रता", "samādhindriyaṃ": "एकाग्रता की क्षमता",
    "samādhibalaṃ": "एकाग्रता का बल", "balaṃ": "बल", "balāni": "बल", "sammā": "सही",
    # saddhā string
    "saddhā": "श्रद्धा", "saddahanā": "श्रद्धा रखना", "okappanā": "भरोसा करना",
    "abhippasādo": "गहरी आस्था", "saddhindriyaṃ": "श्रद्धा की क्षमता", "saddhābalaṃ": "श्रद्धा का बल",
    # vīriya string
    "cetasiko": "मानसिक", "cetasiko vīriyārambho": "मानसिक रूप से उत्साह जगाना", "ārambho": "जगाना",
    "nikkamo": "आगे बढ़ना", "parakkamo": "प्रयत्न", "uyyāmo": "उद्यम", "vāyāmo": "प्रयास",
    "ussāho": "जोश", "ussoḷhī": "लगन", "thāmo": "शक्ति", "dhiti": "धैर्य",
    "asithila": "ढीला न पड़ने वाला", "nikkhitta": "छोड़ना", "chandatā": "चाह", "dhuratā": "भार",
    "sampaggāho": "दृढ़ता से उठाए रखना", "vīriyindriyaṃ": "उत्साह की क्षमता",
    "vīriyabalaṃ": "उत्साह का बल", "paggāho": "तत्परता",
    # sati string
    "sati": "सजगता", "anussati": "बार-बार स्मरण", "paṭissati": "पुनः स्मरण", "saraṇatā": "याद रखना",
    "dhāraṇatā": "धारण करना", "pilāpanatā": "उथला होना", "sammussanatā": "भूल जाना",
    "satindriyaṃ": "सजगता की क्षमता", "satibalaṃ": "सजगता का बल",
    # paññā string
    "paññā": "प्रज्ञा", "pajānanā": "जानना", "vicayo": "छानबीन", "pavicayo": "गहरी छानबीन",
    "dhammavicayo": "परिघटनाओं की छानबीन", "sallakkhaṇā": "पहचानना",
    "upalakkhaṇā": "भली-भाँति पहचानना", "paccupalakkhaṇā": "हर पहलू को पहचानना",
    "paṇḍiccaṃ": "पांडित्य", "kosallaṃ": "कुशलता", "nepuññaṃ": "निपुणता", "vebhabyā": "विवेक",
    "cintā": "चिंतन", "upaparikkhā": "परख", "bhūrī": "व्यापक बुद्धि", "medhā": "मेधा",
    "pariṇāyikā": "मार्गदर्शक बुद्धि", "vipassanā": "अंतर्दृष्टि", "sampajaññaṃ": "स्पष्ट समझ",
    "patodo": "अंकुश", "paññindriyaṃ": "प्रज्ञा की क्षमता", "paññābalaṃ": "प्रज्ञा का बल",
    "satthaṃ": "शस्त्र", "paññāsatthaṃ": "प्रज्ञा रूपी शस्त्र", "pāsādo": "महल",
    "paññāpāsādo": "प्रज्ञा रूपी महल", "āloko": "आलोक", "paññāāloko": "प्रज्ञा रूपी आलोक",
    "obhāso": "आभा", "paññāobhāso": "प्रज्ञा रूपी आभा", "pajjoto": "दीपक",
    "paññāpajjoto": "प्रज्ञा रूपी दीपक", "ratanaṃ": "रत्न", "paññāratanaṃ": "प्रज्ञा रूपी रत्न",
    "amoho": "मोह का अभाव", "diṭṭhi": "दृष्टि",
    # jīvita string
    "jīvita": "जीवन", "jīvitindriyaṃ": "जीवन-क्षमता", "āyu": "आयु", "yapanā": "चलते रहना",
    "yāpanā": "चलाए रखना", "iriyanā": "गतिशील रहना", "vattanā": "बने रहना", "pālanā": "पालन",
    # hiri / ottappa strings
    "hirīyati": "लज्जा आना", "hiri": "लज्जा", "hirī": "लज्जा", "hiribalaṃ": "लज्जा का बल",
    "ottappati": "डरना", "ottappa": "बुराई का डर", "ottappaṃ": "बुराई का डर",
    "ottappabalaṃ": "बुराई के डर का बल", "pāpakānaṃ": "बुरा", "samāpattiyā": "अपनाना",
    # roots
    "alobho": "लोभ का अभाव", "lubbhanā": "लोभ करना", "asārāgo": "राग का अभाव",
    "sārajjanā": "राग करना", "anabhijjhā": "लालच का अभाव", "mūlaṃ": "मूल",
    "kusalamūlaṃ": "हितकर मूल", "adoso": "द्वेष का अभाव", "dussanā": "द्वेष करना",
    "abyāpādo": "दुर्भावना का अभाव", "abyāpajjo": "दुर्भावना न रखना", "byāpajjo": "दुर्भावना रखना",
    "hetū": "मूल",
    # the six pairs (kāya = the mental body = the three mental groups)
    "kāya": "मानसिक काया",
    "passaddhi": "प्रशांति", "cittapassaddhi": "मन की प्रशांति", "passambhanā": "शांत होना",
    "passambhitattaṃ": "शांत हो चुका होना", "paṭipassambhitattaṃ": "पूरी तरह शांत हो चुका होना",
    "lahutā": "हल्कापन", "cittalahutā": "मन का हल्कापन", "lahu": "जल्दी",
    "adandhanatā": "सुस्ती का अभाव", "dandhanatā": "सुस्ती", "vitthanatā": "जड़ता",
    "mudutā": "मृदुता", "cittamudutā": "मन की मृदुता", "maddavatā": "कोमलता",
    "akakkhaḷatā": "कठोरता का अभाव", "kakkhaḷatā": "कठोरता", "kathinatā": "कड़ापन",
    "kammaññatā": "कार्य-योग्यता", "cittakammaññatā": "मन की कार्य-योग्यता",
    "kammaññattaṃ": "कार्य-योग्य होना", "bhāvo": "भाव",
    "pāguññatā": "दक्षता", "cittapāguññatā": "मन की दक्षता", "paguṇattaṃ": "दक्ष होना",
    "ujutā": "सीधाई", "ujukatā": "सीधापन", "cittujukatā": "मन का सीधापन",
    "ajimhatā": "टेढ़ेपन का अभाव", "jimhatā": "टेढ़ापन", "vaṅkatā": "वक्रता", "kuṭilatā": "कुटिलता",
    # summaries (koṭṭhāsavāra / suññatavāra)
    "jhānaṃ": "ध्यान", "maggo": "मार्ग", "pañcaṅgikaṃ": "पाँच अंगों वाला",
    "pañcaṅgiko": "पाँच अंगों वाला", "caturaṅgikaṃ": "चार अंगों वाला", "caturaṅgiko": "चार अंगों वाला",
    "caturaṅgiko maggo": "चार अंगों वाला मार्ग",
    # headings and colophons
    "bhājanī": "विश्लेषण", "bhājanīyaṃ": "विश्लेषण", "bhāṇa": "पाठ", "vāro": "खंड",
    "koṭṭhāsa": "भाग", "suññata": "शून्यता",
    "pañcamaṃ": "पाँचवाँ", "chaṭṭhaṃ": "छठा", "sattamaṃ": "सातवाँ", "aṭṭhamaṃ": "आठवाँ",
}


def lc(kw):
    return kw[:1].lower() + kw[1:]


def ch2_value(kw, kws, table=CH2):
    """Default value with the context rules settled for the cittuppāda chapters."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k.startswith("samaye "):                       # Yo/Yā/Yaṃ tasmiṃ samaye X ...
        return "उस समय" + GAP + ch2_value(k[len("samaye "):], kws, table)
    if k == "dhamma":                                  # stem of dhammārammaṇa / dhammāyatana / dhammadhātu
        return "मन के विषय" if s & {"dhammāyatanaṃ", "dhammadhātu"} else "मन का विषय"
    if k == "ṭhiti" and "āyu" in s:                    # jīvitindriya string
        return "टिके रहना"
    if k == "mano" and "manosañcetanā" in s:           # manosañcetanāhāro
        return "मानसिक"
    if k == "sañcetanā" and "cetayitattaṃ" not in s:   # only inside manosañcetanā
        return "इरादा"
    if k == "cetasikaṃ" and "adukkhamasukhaṃ" in s:    # cetasikaṃ neva sātaṃ nāsātaṃ
        return "मानसिक भाव"
    return table[k]


def matrix_names():
    """Pāli matrix keyword -> Hindi, as settled in 1-matika (first value per keyword).
    Loaded lazily from map_preamble_1-matika_hi.py (importing it writes nothing)."""
    import importlib
    import sys
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    return importlib.import_module("map_preamble_1-matika_hi").MATRIX_NAMES


# ---------------------------------------------------------------------------- build and verify
def build_part(part, resolver):
    """resolver(bid, kw, kws) -> Hindi value. Raises KeyError for an unmapped keyword."""
    lines, missing = [], []
    for bid, kws in read_keywords(part):
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
        raise SystemExit(f"{part}: unmapped keywords: {missing}")
    (HERE / f"{part}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(part, show=50):
    a = [l.split("] ", 1) for l in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    hi = read_hindi(part)
    nde, miss = 0, []
    for bid, rest in b:
        bid = bid[1:]
        text = hi.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
            elif text is None or not present(v, text):
                miss.append((bid, kw, v))
    print(part, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss))
    for m in miss[:show]:
        print("   MISS", *m)
    return bad, nde, miss
