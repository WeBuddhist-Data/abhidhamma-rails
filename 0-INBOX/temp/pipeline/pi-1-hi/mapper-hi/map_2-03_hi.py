"""Map 2-03-cittuppadakandam (lokuttara kusala) keywords to the Hindi translation.

CH2 table + own extensions (TABLE) + case-sensitive heading values (EXACT) + per-segment overrides.
usage: python -I -X utf8 map_2-03_hi.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import CH2, NDE, ch2_value, build_part, verify  # noqa: E402

PART = "2-03-cittuppadakandam"

TABLE = {**CH2,
    # headings / colophons
    "lokuttara": "लोकोत्तर", "lokuttarakusalaṃ": "लोकोत्तर हितकर मन",
    "suddhika": "केवल", "suddhikapaṭipadā": "केवल प्रगति का ढंग", "paṭipadā": "प्रगति का ढंग",
    "suññata": "शून्यता", "mūlaka": "पर आधारित", "mūlakapaṭipadā": "पर आधारित प्रगति का ढंग",
    "appaṇihita": "इच्छाओं का अभाव", "nayā": "विधि", "vīsati": "बीस", "adhipati": "प्रधानता",
    # opening formula of the path-consciousness
    "lokuttaraṃ": "लोकोत्तर", "lokuttaraṃ jhānaṃ": "लोकोत्तर ध्यान",
    "bhāveti": "अभ्यास करना", "lokuttaraṃ jhānaṃ bhāveti": "लोकोत्तर ध्यान का अभ्यास करना",
    "niyyānikaṃ": "मुक्ति की ओर ले जाने वाला", "caya": "संचय", "apacaya": "संचय घटाना",
    "gāmiṃ": "की ओर ले जाने वाला",
    "niyyānikaṃ apacayagāmiṃ": "मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला",
    "diṭṭhigatānaṃ": "दृष्टियों में फँसना", "pahānāya": "छोड़ना",
    "diṭṭhigatānaṃ pahānāya": "दृष्टियों में फँसने को छोड़ना",
    "bhūmiyā": "चरण", "pattiyā": "प्राप्ति",
    "vivicca": "अलग होकर", "eva": NDE, "kāmehi": "इंद्रिय-सुख",
    "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर",
    "upasampajja": "प्राप्त करके", "viharati": "रहना", "upasampajja viharati": "प्राप्त करके उसमें रहना",
    "vitakka": "आरंभिक विचार", "vicārānaṃ": "सतत विचार", "vūpasamā": "शांत होना",
    "catutthaṃ jhānaṃ": "चौथा ध्यान",
    # modes of progress
    "dukkha": "दुःखद", "dukkhapaṭipadaṃ": "दुःखद प्रगति", "sukha": "सुखद", "sukhapaṭipadaṃ": "सुखद प्रगति",
    "paṭipadaṃ": "प्रगति", "paṭipadaṃ dandha": "प्रगति और धीमा", "paṭipadaṃ khippa": "प्रगति और शीघ्र",
    "abhiññaṃ": "उच्च ज्ञान", "dandha": "धीमा", "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला",
    "khippa": "शीघ्र", "khippābhiññaṃ": "शीघ्र उच्च ज्ञान वाला",
    "suññataṃ": "शून्य", "appaṇihitaṃ": "इच्छा-रहित",
    # new factors
    "anaññātaññassāmītindriyaṃ": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
    "aññāta": "जाना", "aññindriyaṃ": "पूर्ण ज्ञान की क्षमता", "aññā": "पूर्ण ज्ञान",
    "vācā": "वाणी", "vacī": "वाणी", "ājīvo": "आजीविका", "micchā": "ग़लत",
    "aṭṭhaṅgiko": "आठ अंगों वाला",
    "magga": "मार्ग", "aṅgaṃ": "अंग", "maggaṅgaṃ": "मार्ग का अंग",
    "sambojjhaṅgo": "जागृति का अंग", "samādhisambojjhaṅgo": "एकाग्रता नामक जागृति का अंग",
    "vīriyasambojjhaṅgo": "उत्साह नामक जागृति का अंग", "vicayasambojjhaṅgo": "छानबीन नामक जागृति का अंग",
    "sacchikiriyāya": "साक्षात्कार",
    # abstinence string
    "duccaritehi": "दुराचरण", "ārati": "दूर रहना", "virati": "विरत रहना",
    "paṭivirati": "पूरी तरह विरत रहना", "veramaṇī": "बचना", "kiriyā": "करना", "karaṇaṃ": "अपनाना",
    "ajjhāpatti": "दोष में पड़ना", "velā": "मर्यादा", "atikkamo": "उल्लंघन करना",
    "setu": "पुल", "ghāto": "तोड़ देना",
    "micchāājīvā ārati": "ग़लत आजीविका से दूर रहना", "samaye": "उस समय",
    # twenty great methods
    "maggaṃ": "मार्ग", "paṭṭhānaṃ": "आधार", "padhānaṃ": "परिश्रम", "iddhi": "सिद्धि",
    "bojjhaṅgaṃ": "जागृति का अंग", "saccaṃ": "सत्य", "samathaṃ": "शांति", "khandhaṃ": "समूह",
    "āyatanaṃ": "इंद्रिय-क्षेत्र", "dhātuṃ": "तत्व", "āhāraṃ": "आहार", "phassaṃ": "संपर्क",
    "vedanaṃ": "अनुभूति", "saññaṃ": "पहचान", "cetanaṃ": "इरादा",
    "lokuttaraṃ maggaṃ": "लोकोत्तर मार्ग", "lokuttaraṃ satipaṭṭhānaṃ": "लोकोत्तर सजगता का आधार",
    "lokuttaraṃ iddhipādaṃ": "लोकोत्तर सिद्धि का आधार", "lokuttaraṃ indriyaṃ": "लोकोत्तर क्षमता",
    "lokuttaraṃ balaṃ": "लोकोत्तर बल", "lokuttaraṃ bojjhaṅgaṃ": "लोकोत्तर जागृति का अंग",
    "lokuttaraṃ saccaṃ": "लोकोत्तर सत्य", "lokuttaraṃ samathaṃ": "लोकोत्तर शांति",
    "lokuttaraṃ dhammaṃ": "लोकोत्तर परिघटना", "lokuttaraṃ khandhaṃ": "लोकोत्तर समूह",
    "lokuttaraṃ āyatanaṃ": "लोकोत्तर इंद्रिय-क्षेत्र", "lokuttaraṃ dhātuṃ": "लोकोत्तर तत्व",
    "lokuttaraṃ āhāraṃ": "लोकोत्तर आहार", "lokuttaraṃ phassaṃ": "लोकोत्तर संपर्क",
    "lokuttaraṃ vedanaṃ": "लोकोत्तर अनुभूति", "lokuttaraṃ saññaṃ": "लोकोत्तर पहचान",
    "lokuttaraṃ cetanaṃ": "लोकोत्तर इरादा", "lokuttaraṃ cittaṃ": "लोकोत्तर मन",
    "lokuttaraṃ maggaṃ bhāveti": "लोकोत्तर मार्ग का अभ्यास करना",
    "lokuttaraṃ samathaṃ bhāveti": "लोकोत्तर शांति का अभ्यास करना",
    "lokuttaraṃ phassaṃ bhāveti": "लोकोत्तर संपर्क का अभ्यास करना",
    "lokuttaraṃ vedanaṃ bhāveti": "लोकोत्तर अनुभूति का अभ्यास करना",
    "lokuttaraṃ cetanaṃ bhāveti": "लोकोत्तर इरादे का अभ्यास करना",
    "lokuttaraṃ saññaṃ bhāveti": "लोकोत्तर पहचान का अभ्यास करना",
    # predominance
    "chanda": "चाह", "vīmaṃsā": "जाँच-परख", "ādhipateyyaṃ": "प्रधानता वाला",
    # higher paths
    "kāmarāga": "इंद्रिय-सुखों का राग", "rāga": "राग", "byāpādānaṃ": "दुर्भावना",
    "tanubhāvāya": "क्षीण करना", "avasesa": NDE,
    "arūpa": "अभौतिक लोक", "māna": "अहंकार", "uddhacca": "बेचैनी", "avijjāya": "अज्ञान",
    "ñātānaṃ": "जाना जा चुका",
}

# case-sensitive values (heading / closing vs. qualifier in the body)
EXACT = {
    "Suññataṃ": "शून्यता", "Appaṇihitaṃ": "इच्छाओं का अभाव",
    "Lokuttaraṃ": "लोकोत्तर", "Lokuttaraṃ cittaṃ": "लोकोत्तर मन",
}

# per-segment overrides: {bid: {kw: value}}
OVERRIDES = {
    # anaññātānaṃ … aviditānaṃ asacchikatānaṃ = «न जानी गई … न समझी गई और न प्रत्यक्ष अनुभव की गई»
    "1-296": {"viditānaṃ": "समझा गया", "sacchikatānaṃ": "प्रत्यक्ष अनुभव किया गया"},
    # ñātānaṃ … viditānaṃ sacchikatānaṃ = «जानी जा चुकी … समझी जा चुकी और प्रत्यक्ष अनुभव की जा चुकी»
    "1-364": {"viditānaṃ": "समझा जा चुका", "sacchikatānaṃ": "प्रत्यक्ष अनुभव किया जा चुका"},
    # tīhi kāyaduccaritehi = «शरीर के तीन दुराचरणों»
    "1-300": {"kāya": "शरीर"},
    # rūparāga = «सूक्ष्म भौतिक लोक के राग»
    "1-363": {"rūpa": "सूक्ष्म भौतिक लोक"},
}


def resolver(bid, kw, kws):
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    if kw in EXACT:
        return EXACT[kw]
    return ch2_value(kw, kws, TABLE)


if __name__ == "__main__":
    build_part(PART, resolver)
    verify(PART)
