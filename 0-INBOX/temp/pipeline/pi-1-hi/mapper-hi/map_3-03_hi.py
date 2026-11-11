"""Map 3-03-rupakandam keywords to the Hindi translation (own table + context rules + per-segment overrides).

usage: python -I -X utf8 map_3-03_hi.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import ch2_value, build_part, verify, read_hindi, present, lc, GAP  # noqa: E402

PART = "3-03-rupakandam"
HI = read_hindi(PART)

# Rūpavibhatti table (keys lower-case first letter, as lc() gives them).
T = {
    # frame and classification predicates
    "rūpaṃ": "भौतिक रूप", "ajjhattikaṃ": "आंतरिक", "bāhiraṃ": "बाह्य",
    "upādā": "व्युत्पन्न", "upādāya": "व्युत्पन्न",
    "upādiṇṇaṃ": "कर्म से उत्पन्न", "upādiṇṇa": "कर्म से उत्पन्न",
    "upādāniyaṃ": "आसक्ति का विषय बनने वाला",
    "upādiṇṇupādāniyaṃ": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
    "anupādiṇṇupādāniyaṃ": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला",
    "sanidassanaṃ": "दिखाई देने वाला", "anidassanaṃ": "दिखाई न देने वाला",
    "sappaṭighaṃ": "टकराव वाला", "appaṭighaṃ": "टकराव से रहित",
    "oḷārikaṃ": "स्थूल", "sukhumaṃ": "सूक्ष्म",
    "mahābhūtaṃ": "महाभूत", "bhūtaṃ": "महाभूत", "mahābhūtānaṃ": "महाभूत", "bhūtānaṃ": "महाभूत",
    "mahābhūtehi": "महाभूत", "bhūtehi": "महाभूत",
    "indriyaṃ": "क्षमता", "viññatti": "प्रकट अभिव्यक्ति",
    "samuṭṭhānaṃ": "उत्पन्न", "cittasamuṭṭhānaṃ": "मन से उत्पन्न", "cittajaṃ": "मन से जन्मा",
    "hetukaṃ": "के कारण होने वाला", "cittasahabhu": "मन के साथ-साथ होने वाला",
    "anuparivatti": "अनुसरण करने वाला", "citta": "मन", "cittassa": "मन",
    "ārammaṇaṃ": "विषय",
    # bodily bases, objects, contact, consciousness
    "cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर", "kāyassa": "शरीर",
    "rūpa": "दृश्य रूप", "sadda": "ध्वनि", "gandha": "गंध", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श",
    "phoṭṭhabbo": "स्पर्श",
    "cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र", "sotāyatanaṃ": "कान का इंद्रिय-क्षेत्र",
    "ghānāyatanaṃ": "नाक का इंद्रिय-क्षेत्र", "jivhāyatanaṃ": "जीभ का इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ": "शरीर का इंद्रिय-क्षेत्र", "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र",
    "saddāyatanaṃ": "ध्वनि का इंद्रिय-क्षेत्र", "gandhāyatanaṃ": "गंध का इंद्रिय-क्षेत्र",
    "rasāyatanaṃ": "स्वाद का इंद्रिय-क्षेत्र", "phoṭṭhabbāyatanaṃ": "स्पर्श का इंद्रिय-क्षेत्र",
    "āyatanānaṃ": "इंद्रिय-क्षेत्र",
    "dhātu": "तत्व", "cakkhudhātu": "आँख का तत्व", "sotadhātu": "कान का तत्व",
    "ghānadhātu": "नाक का तत्व", "jivhādhātu": "जीभ का तत्व", "kāyadhātu": "शरीर का तत्व",
    "rūpadhātu": "दृश्य रूप का तत्व", "saddadhātu": "ध्वनि का तत्व", "gandhadhātu": "गंध का तत्व",
    "rasadhātu": "स्वाद का तत्व", "phoṭṭhabbadhātu": "स्पर्श का तत्व",
    "ākāsa": "आकाश", "ākāsadhātu": "आकाश तत्व", "āpo": "जल", "āpodhātu": "जल तत्व",
    "pathavī": "पृथ्वी", "pathavīdhātu": "पृथ्वी तत्व", "tejo": "अग्नि", "tejodhātu": "अग्नि तत्व",
    "vāyo": "वायु", "vāyodhātu": "वायु तत्व",
    "cakkhusamphassassa": "आँख का संपर्क", "sotasamphassassa": "कान का संपर्क",
    "ghānasamphassassa": "नाक का संपर्क", "jivhāsamphassassa": "जीभ का संपर्क",
    "kāyasamphassassa": "शरीर का संपर्क",
    "cakkhusamphassajāya": "आँख के संपर्क से उत्पन्न",
    "cakkhusamphassajāya vedanāya": "आँख के संपर्क से उत्पन्न अनुभूति",
    "kāyasamphassajāya": "शरीर के संपर्क से उत्पन्न",
    "kāyasamphassajāya vedanāya": "शरीर के संपर्क से उत्पन्न अनुभूति",
    "vedanāya": "अनुभूति", "saññāya": "पहचान", "cetanāya": "इरादा",
    "cakkhuviññāṇassa": "आँख की चेतना", "kāyaviññāṇassa": "शरीर की चेतना",
    # faculties
    "itthi": "स्त्रीत्व", "purisa": "पुरुषत्व", "itthindriyaṃ": "स्त्रीत्व की क्षमता",
    "purisindriyaṃ": "पुरुषत्व की क्षमता", "jīvitindriyaṃ": "जीवन-क्षमता", "jīvita": "जीवन",
    "rūpīnaṃ dhammānaṃ": "भौतिक परिघटना",
    # intimation
    "kāyaviññatti": "शरीर द्वारा प्रकट अभिव्यक्ति", "vacī": "वाणी",
    "vacīviññatti": "वाणी द्वारा प्रकट अभिव्यक्ति", "viññāpanā": "प्रकट करना",
    "thambhanā": "तनना", "santhambhitattaṃ": "भली-भाँति तना हुआ होना",
    "thambhitattaṃ": "तना हुआ होना",
    # qualities of matter
    "rūpassa lahutā": "भौतिक रूप का हल्कापन", "rūpassa mudutā": "भौतिक रूप की मृदुता",
    "rūpassa kammaññatā": "भौतिक रूप की कार्य-योग्यता", "rūpassa upacayo": "भौतिक रूप की वृद्धि",
    "rūpassa santati": "भौतिक रूप की धारा", "rūpassa jaratā": "भौतिक रूप का बुढ़ापा",
    "rūpassa aniccatā": "भौतिक रूप की अनित्यता",
    "rūpassa na lahutā": "भौतिक रूप का हल्कापन नहीं", "rūpassa na mudutā": "भौतिक रूप की मृदुता नहीं",
    "rūpassa na kammaññatā": "भौतिक रूप की कार्य-योग्यता नहीं",
    "rūpassa na upacayo": "भौतिक रूप की वृद्धि नहीं", "rūpassa na santati": "भौतिक रूप की धारा नहीं",
    "rūpassa na jaratā": "भौतिक रूप का बुढ़ापा नहीं", "rūpassa na aniccatā": "भौतिक रूप की अनित्यता नहीं",
    "santati": "धारा", "jaratā": "बुढ़ापा", "aniccatā": "अनित्यता",
    "lahupariṇāmatā": "जल्दी बदल पाना", "avitthanatā": "जड़ता का अभाव",
    "akathinatā": "कड़ेपन का अभाव", "ācayo": "संचय",
    "kammassa": "कर्म",
    "kabaḷīkāro": "कौर-कौर खाया जाने वाला", "āhāro": "भोजन",
    "kabaḷīkāro āhāro": "कौर-कौर खाया जाने वाला भोजन",
    # jarā / aniccatā strings
    "jīraṇatā": "जीर्ण होना", "khaṇḍiccaṃ": "दाँतों का टूटना", "pāliccaṃ": "बालों का पकना",
    "valittacatā": "त्वचा पर झुर्रियाँ पड़ना", "āyuno": "आयु", "saṃhāni": "घटना",
    "indriyānaṃ": "इंद्रिय", "paripāko": "पूरी तरह पक जाना",
    "khayo": "क्षय", "vayo": "नाश", "bhedo": "टूटना", "paribhedo": "बिखर जाना",
    "antaradhānaṃ": "लुप्त हो जाना",
    # elements
    "gataṃ": "की प्रकृति वाला", "aghaṃ": "रिक्त स्थान", "vivaro": "छेद", "asamphuṭṭhaṃ": "अछूता",
    "sineho": "नमी", "bandhanattaṃ": "बाँधे रखना", "bandhanattaṃ rūpassa": "भौतिक रूप को बाँधे रखना",
    "kakkhaḷaṃ": "कठोर", "kakkhaḷattaṃ": "कठोरता", "khara": "कर्कशता",
    "bahiddhā": "दूसरों से संबंधित", "usmā": "ऊष्मा", "usumaṃ": "गरमी",
    # sense-base names list
    "pasādo": "संवेदनशीलता", "upādāya pasādo": "व्युत्पन्न संवेदनशीलता", "suñño": "सूना",
    "suñño gāmo": "सूना गाँव", "gāmo": "गाँव",
    "vaṇṇa": "रंग", "nibhā": "आभा", "vaṇṇanibhā": "रंग-आभा", "upādāya vaṇṇanibhā": "व्युत्पन्न रंग-आभा",
    # sex faculties
    "itthiyā": "स्त्री", "liṅgaṃ": "आकृति", "nimittaṃ": "चिह्न", "kuttaṃ": "आचरण", "ākappo": "ढंग",
    "purisassa": "पुरुष",
    # bodily intimation string
    "abhikkamantassa": "आगे बढ़ना", "paṭikkamantassa": "पीछे हटना", "ālokentassa": "सामने देखना",
    "vilokentassa": "इधर-उधर देखना", "samiñjentassa": "अंग सिकोड़ना", "pasārentassa": "अंग फैलाना",
    "kusalacittassa": "हितकर मन", "akusalacittassa": "हानिकर मन", "akusala": "हानिकर",
    "abyākata": "नैतिक रूप से अनिर्धारित",
    # vocal intimation string
    "vācā": "वाणी", "girā": "बोल", "byappatho": "बोलने का ढंग", "udīraṇaṃ": "उच्चारण",
    "dhoso": "आवाज़", "ghosakammaṃ": "आवाज़ निकालना",
    # edible food
    "odano": "भात", "kummāso": "दलिया", "sattu": "सत्तू", "maccho": "मछली", "maṃsaṃ": "मांस",
    "khīraṃ": "दूध", "dadhi": "दही", "sappi": "घी", "navanītaṃ": "मक्खन", "madhu": "शहद",
    "phāṇitaṃ": "गुड़", "sattānaṃ": "प्राणी", "mukha": "मुँह", "āsiyaṃ": "खाना", "danta": "दाँत",
    "vikhādanaṃ": "चबाना", "gala": "गला", "ajjhoharaṇīyaṃ": "नीचे उतारना", "kucchi": "पेट",
    "vitthambhanaṃ": "भरना", "ojāya": "पोषक सार", "yāpenti": "जीवित रहना",
    # fours ... elevens
    "sutaṃ": "सुना हुआ", "mutaṃ": "अनुभव किया हुआ", "manasā": "मन", "viññātaṃ": "जाना हुआ",
    "viññātaṃ rūpaṃ": "जाना हुआ भौतिक रूप",
    "viññeyyaṃ": "जाना जा सकने वाला", "viññeyyaṃ rūpaṃ": "जाना जा सकने वाला भौतिक रूप",
    "āyatanaṃ cakkhuviññeyyaṃ rūpaṃ": "इंद्रिय-क्षेत्र आँख से जाना जा सकने वाला भौतिक रूप",
    "āyatanaṃ manodhātuviññeyyaṃ rūpaṃ": "इंद्रिय-क्षेत्र मन के तत्व से जाना जा सकने वाला भौतिक रूप",
    "rūpaṃ manoviññeyyaṃ rūpaṃ": "भौतिक रूप मन से जाना जा सकने वाला भौतिक रूप",
    "rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ":
        "भौतिक रूप मन की चेतना के तत्व से जाना जा सकने वाला भौतिक रूप",
    "mano": "मन", "manodhātu": "मन का तत्व", "manoviññāṇa": "मन की चेतना",
    "manoviññāṇadhātu": "मन की चेतना का तत्व",
    "manāpiyo": "मनभावन", "amanāpiyo": "मन को न भाने वाला", "sukha": "सुखद", "dukkha": "दुःखद",
    "samphasso": "संपर्क",
    # headings and colophons
    "niddeso": "व्याख्या", "dasakaṃ": "दस-दस के वर्गीकरण", "ekādasakaṃ": "ग्यारह-ग्यारह के वर्गीकरण",
    "saṅgaho": "वर्गीकरण", "rūpasaṅgaho": "भौतिक रूप का वर्गीकरण", "vidhena": "प्रकार",
    "dasa": "दस", "ekādasa": "ग्यारह", "aṭṭhama": "आठवाँ", "kaṇḍaṃ": "अध्याय", "vibhatti": "वर्गीकरण",
    "niṭṭhitaṃ": "पूरा हुआ", "bhāṇa": "पाठ", "vāro": "खंड",
    "dhamma": "मन के विषय", "dhammāyatana": "मन के विषयों का इंद्रिय-क्षेत्र",
}

# per-segment overrides: {bid: {kw: value}}
OVERRIDES = {
    # itthiliṅgaṃ … itthibhāvo / purisaliṅgaṃ …: the member is the woman / man, not the faculty
    "1-838": {"itthi": "स्त्री"},
    "1-841": {"purisa": "पुरुष"},
    # vacībhedo = «वाणी का फूटना»
    "1-850": {"bhedo": "फूटना"},
    # «Yo rūpassa upacayo» = «भौतिक रूप की जो वृद्धि है»
    "1-871": {"rūpassa upacayo": "भौतिक रूप की" + GAP + "वृद्धि"},
}

PAIR_FIRST = ("bāhiraṃ", "upādā", "upādiṇṇaṃ", "rūpaṃ")


def resolver(bid, kw, kws):
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    k = lc(kw)
    text = HI[bid]
    if k == "kammassa katattā":
        # list lead «Kammassa katattā …:» = «किए गए कर्म के कारण:»; elsewhere «कर्म किए जाने के कारण»
        return "किए गए कर्म के कारण" if "किए गए कर्म के कारण" in text else "कर्म किए जाने के कारण"
    parts = k.split(" ")
    if len(parts) == 2 and parts[0] in PAIR_FIRST and parts[1] in ("sappaṭighaṃ", "appaṭighaṃ"):
        a, b = T[parts[0]], T[parts[1]]
        joined = f"{a} और {b}"
        return joined if present(joined, text) else a + GAP + b   # «… न होने वाला और …» / question frame
    if k in T:
        return T[k]
    return ch2_value(kw, kws)


if __name__ == "__main__":
    build_part(PART, resolver)
    verify(PART)
