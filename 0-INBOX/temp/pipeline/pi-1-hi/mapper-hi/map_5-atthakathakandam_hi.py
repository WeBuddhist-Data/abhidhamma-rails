"""Map 5-atthakathakandam keywords to the Hindi translation (part table + context rules + per-segment overrides).

usage: python -I -X utf8 map_5-atthakathakandam_hi.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import (GAP, build_part, lc, present, read_hindi, read_pali,  # noqa: E402
                           verify)

PART = "5-atthakathakandam"
P = "परिघटना"
VJ = "कहा जा सकना"  # vattabba (na vattabbā = «… कहा जा सकता / कहा नहीं जा सकता»)

T = {
    # headings / colophon
    "kaṇḍaṃ": "अध्याय", "aṭṭhakathā": "अर्थ-व्याख्या", "atthuddhāro": "अर्थ-निर्धारण",
    "duka": "दो-दो के वर्गीकरण", "dukaṃ": "दो-दो के वर्गीकरण", "antara": "बीच का",
    "antaradukaṃ": "बीच के … दो-दो के वर्गीकरण", "piṭṭhi": "अंतिम",
    "niṭṭhito": "पूरा हुआ", "saṅgaṇī": "गणना", "dhammasaṅgaṇī": "परिघटनाओं की गणना",
    # cluster terms (gocchaka)
    "hetu": "मूल", "hetū": "मूल", "āsava": "मन के मैल", "āsavā": "मन के मैल", "āsavo": "मैल",
    "saṃyojana": "बंधन", "saṃyojanā": "बंधन", "saṃyojanaṃ": "बंधन",
    "gantha": "गाँठ", "ganthā": "गाँठ", "gantho": "गाँठ", "ogha": "बाढ़", "oghā": "बाढ़",
    "yoga": "जकड़न", "yogā": "जकड़न", "nīvaraṇa": "बाधा", "nīvaraṇā": "बाधा", "nīvaraṇaṃ": "बाधा",
    "parāmāsa": "ग़लत धारणा", "parāmāsā": "ग़लत धारणा", "parāmāso": "ग़लत धारणा",
    "parāmāsaṃ": "ग़लत धारणा", "upādāna": "आसक्ति", "upādānā": "आसक्ति",
    "kilesa": "क्लेश", "kilesā": "मन के क्लेश",
    # -niya / -vippayutta members
    "sāsavā": "मन के मैलों का विषय बनने वाला", "anāsavā": "मन के मैलों का विषय न बनने वाला",
    "saṃyojaniyā": "बंधनों का विषय बनने वाला", "ganthaniyā": "गाँठों का विषय बनने वाला",
    "nīvaraṇiyā": "बाधाओं का विषय बनने वाला", "parāmaṭṭhā": "ग़लत धारणा का विषय बनने वाला",
    "upādāniyā": "आसक्ति का विषय बनने वाला", "saṃkilesikā": "क्लेशों की ओर ले जाने वाला",
    "āsavavippayuttā": "मन के मैलों से अलग", "saṃyojanavippayuttā": "बंधनों से अलग",
    "ganthavippayuttā": "गाँठों से अलग", "nīvaraṇavippayuttā": "बाधाओं से अलग",
    "parāmāsavippayuttā": "ग़लत धारणा से अलग", "upādānavippayuttā": "आसक्ति से अलग",
    "kilesavippayuttā": "क्लेशों से अलग", "cittavippayuttā": "मन से अलग",
    "saṃyojanā ceva saṃyojaniyā": "बंधन रूपी भी और बंधनों का विषय बनने वाला भी",
    "ganthā ceva ganthaniyā": "गाँठ रूपी भी और गाँठों का विषय बनने वाला भी",
    "nīvaraṇā ceva nīvaraṇiyā": "बाधा रूपी भी और बाधाओं का विषय बनने वाला भी",
    "upādānā ceva upādāniyā": "आसक्ति रूपी भी और आसक्ति का विषय बनने वाला भी",
    "saṃyojanāni saṃyojanā": "बंधन बंधन रूपी", "nīvaraṇāni nīvaraṇā": "बाधा बाधा रूपी",
    "upādānāni upādānā": "आसक्ति आसक्ति रूपी", "kilesā kilesā": "मन के क्लेश मन के क्लेश रूपी",
    "saṃyojanavippayuttā saṃyojaniyā": "बंधनों से अलग पर उनका विषय बनने वाला",
    "ganthavippayuttā ganthaniyā": "गाँठों से अलग पर उनका विषय बनने वाला",
    "nīvaraṇavippayuttā nīvaraṇiyā": "बाधाओं से अलग पर उनका विषय बनने वाला",
    "upādānavippayuttā upādāniyā": "आसक्ति से अलग पर उसका विषय बनने वाला",
    "kilesavippayuttā saṃkilesikā": "क्लेशों से अलग पर क्लेशों की ओर ले जाने वाला",
    # triad / dyad item names
    "kusalā": "हितकर", "akusalā": "हानिकर", "abyākatā": "नैतिक रूप से अनिर्धारित",
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    "akusalābyākatā": "हानिकर और नैतिक रूप से अनिर्धारित",
    "sukhāya": "सुखद", "dukkhāya": "दुःखद", "vedanāya": "अनुभूति", "vedanā": "अनुभूति",
    "sukhāya vedanāya": "सुखद अनुभूति", "dukkhāya vedanāya": "दुःखद अनुभूति",
    "adukkhamasukhāya": "न दुःखद न सुखद", "sampayuttā": "जुड़ा", "sampayutta": "जुड़ा",
    "sampayutte": "जुड़ा", "sampayutto": "जुड़ा", "vippayuttā": "अलग", "vippayutta": "अलग",
    "vippayutte": "अलग", "vippayuttā dhammā": f"अलग {P}",
    "vipākadhamma": "कर्म-फल उत्पन्न करने वाला",
    "vipākadhammadhammā": f"कर्म-फल उत्पन्न करने वाली {P}",
    "upādiṇṇa": "कर्म से उत्पन्न", "upādiṇṇā": "कर्म से उत्पन्न",
    "upādiṇṇupādāniyā": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
    "anupādiṇṇupādāniyā": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला",
    "saṃkiliṭṭha": "क्लेशों से मलिन", "saṃkiliṭṭhā": "क्लेशों से मलिन",
    "asaṃkiliṭṭha": "क्लेशों से मलिन न होने वाला", "asaṃkiliṭṭhā": "क्लेशों से मलिन न होने वाला",
    "vitakka": "आरंभिक विचार", "vitakkā": "आरंभिक विचार", "vicāra": "सतत विचार",
    "vicārā": "सतत विचार", "savitakkasavicāro": "आरंभिक विचार और सतत विचार वाला",
    "pīti": "उल्लास", "sukha": "सुख", "upekkhā": "समभाव", "pītikā": "उल्लास वाला",
    "pītisahagatā": "उल्लास के साथ होने वाला", "sukhasahagatā": "सुख के साथ होने वाला",
    "pahātabbā": "छोड़ा जाने वाला", "pahātabba": "छोड़ा जाने वाला", "dassanena": "सत्य-दर्शन",
    "bhāvanāya pahātabbā": "मानसिक अभ्यास से छोड़ा जाने वाला",
    "bhāvanāya pahātabba": "मानसिक अभ्यास से छोड़ा जाने वाला",
    "hetukā": "मूलों वाला", "pahātabbahetukā": "छोड़े जाने वाले मूलों वाला",
    "ācaya": "संचय", "caya": "संचय", "apacaya": "संचय घटाना",
    "sekkhā": "सीखने के चरण का", "sekkha": "सीखने के चरण का", "asekkhā": "सीखना पूरा होने के चरण का",
    "parittā": "सीमित", "mahaggatā": "उन्नत", "appamāṇā": "अपरिमित",
    "paritta": "सीमित", "mahaggata": "उन्नत", "appamāṇa": "अपरिमित",
    "ārammaṇā": "विषय वाला", "parittārammaṇā": "सीमित विषय वाला",
    "mahaggatārammaṇā": "उन्नत विषय वाला", "appamāṇārammaṇā": "अपरिमित विषय वाला",
    "hīnā": "हीन", "majjhimā": "मध्यम", "paṇītā": "उत्तम", "niyatā": "निश्चित",
    "micchatta": "ग़लत दिशा", "sammatta": "सही दिशा", "magga": "मार्ग", "adhipatino": "प्रधानता वाला",
    "uppannā": "उत्पन्न हो चुका", "uppādino": "उत्पन्न होने वाला",
    "atītā": "अतीत का", "anāgatā": "भविष्य का", "paccuppannā": "वर्तमान का",
    "atītārammaṇā": "अतीत के विषय वाला", "anāgatārammaṇā": "भविष्य के विषय वाला",
    "paccuppannārammaṇā": "वर्तमान के विषय वाला", "niyogā": "अनिवार्य रूप से",
    "bahiddhā": "दूसरों से संबंधित", "sanidassana": "दिखाई देने वाला",
    "sanidassanā": "दिखाई देने वाला", "anidassana": "दिखाई न देने वाला",
    "anidassanā": "दिखाई न देने वाला", "anidassanaṃ": "दिखाई न देने वाला",
    "sappaṭighā": "टकराव वाला", "appaṭighaṃ": "टकराव से रहित",
    "saṅkhatā": "निर्मित", "asaṅkhatā": "अनिर्मित", "rūpino": "भौतिक", "arūpino": "अभौतिक",
    "lokiyā": "लौकिक", "uttarā": "लोकोत्तर", "na": "न", "viññeyyā": "जाना जा सकने वाला",
    "cittā": "मन", "cetasikā": "मन का सहचर", "saṃsaṭṭhā": "घुला-मिला", "saṃsaṭṭha": "घुला-मिला",
    "cittasaṃsaṭṭhā": "मन से घुला-मिला", "cittavisaṃsaṭṭhā": "मन से घुला-मिला न होने वाला",
    "samuṭṭhānā": "उत्पन्न", "samuṭṭhāna": "उत्पन्न", "cittasamuṭṭhānā": "मन से उत्पन्न",
    "cittasahabhuno": "मन के साथ-साथ होने वाला", "sahabhuno": "साथ-साथ होने वाला",
    "anuparivattino": "अनुसरण करने वाला", "cittānuparivattino": "मन का अनुसरण करने वाला",
    "cittasaṃsaṭṭhasamuṭṭhānā": "मन से घुला-मिला और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण करने वाला",
    "ajjhattikā": "आंतरिक", "bāhirā": "बाह्य", "upādā": "व्युत्पन्न",
    "apariyāpannā": "अस्तित्व के लोकों में न समाई हुई", "niyyānikā": "मुक्ति की ओर ले जाने वाला",
    "sauttarā": "सर्वोच्च न होने वाला", "anuttarā": "सर्वोच्च", "raṇā": "संघर्ष",
    # mind classes
    "bhūmīsu": "स्तर", "kusalaṃ": "हितकर मन", "akusalaṃ": "हानिकर मन",
    "avasesaṃ": "शेष", "avasesaṃ akusalaṃ": "शेष हानिकर मन", "sabbaṃ": "सारा",
    "kiriyā": "केवल क्रिया रूपी", "kiriya": "केवल क्रिया रूपी", "abyākataṃ": "नैतिक रूप से अनिर्धारित",
    "kiriyābyākataṃ": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन",
    "kusalassa": "हितकर मन", "akusalassa": "हानिकर मन", "akusalato": "हानिकर मन",
    "kusalesu": "हितकर मन", "akusalesu": "हानिकर मन", "kiriyesu": "केवल क्रिया रूपी मन",
    "vipāka": "कर्म-फल रूपी", "vipākato": "कर्म-फल",
    "vipākato ca kiriyato": "कर्म-फल रूपी और केवल क्रिया रूपी",
    "kusalato ca vipākato": "हितकर और कर्म-फल रूपी",
    "kāma": "इंद्रिय-सुख", "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित",
    "kāmāvacaraṃ": "इंद्रिय-सुखों के लोक से संबंधित", "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित",
    "kāmāvacarassa": "इंद्रिय-सुखों के लोक से संबंधित", "avacara": "लोक से संबंधित",
    "avacaraṃ": "लोक से संबंधित", "avacarā": "लोक से संबंधित", "avacarassa": "लोक से संबंधित",
    "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित", "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक से संबंधित",
    "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित", "arūpa": "अभौतिक",
    "arūpāvacarā": "अभौतिक लोक से संबंधित", "lokuttara": "लोकोत्तर", "lokuttaraṃ": "लोकोत्तर",
    "uppādā": "उत्पत्ति", "uppādo": "उत्पत्ति", "uppāde": "उत्पत्ति", "uppādesu": "उत्पत्ति",
    "cittuppādo": "मन की उत्पत्ति", "cittuppādā": "मन की … उत्पत्ति",
    "cittuppādesu": "मन की … उत्पत्ति", "cittuppāde": "मन की उत्पत्ति",
    "citta": "मन", "cittañca": "मन", "akusalacitta": "हानिकर मन",
    "sahagata": "के साथ होने वाला", "sahagatesu": "के साथ होने वाला", "sahagato": "के साथ होने वाला",
    "sahagataṃ": "के साथ होने वाला", "sahagatacitta": "के साथ होने वाला मन",
    "sahagatesu citta": "के साथ होने वाला मन", "sahagato citta": "के साथ होने वाला मन",
    "vippayuttacitta": "अलग मन", "vippayutte citta": "अलग मन", "ahetuke citta": "मूल से रहित मन",
    "somanassa": "प्रसन्नता", "domanassa": "उदासी", "lobha": "लोभ", "vicikicchā": "संशय",
    "uddhacca": "बेचैनी", "dukkha": "दुःख",
    "somanassasahagata": "प्रसन्नता के साथ होने वाला", "domanassasahagata": "उदासी के साथ होने वाला",
    "domanassasahagatesu": "उदासी के साथ होने वाला", "lobhasahagata": "लोभ के साथ होने वाला",
    "lobhasahagatesu": "लोभ के साथ होने वाला", "vicikicchāsahagato": "संशय के साथ होने वाला",
    "vicikicchāsahagataṃ": "संशय के साथ होने वाला", "vicikicchāsahagatesu": "संशय के साथ होने वाला",
    "uddhaccasahagato": "बेचैनी के साथ होने वाला", "uddhaccasahagataṃ": "बेचैनी के साथ होने वाला",
    "uddhaccasahagatesu": "बेचैनी के साथ होने वाला",
    "upekkhāsahagata": "समभाव के साथ होने वाला",
    "sahagato moho": "के साथ होने वाला मोह", "sahagataṃ mohaṃ": "के साथ होने वाला मोह",
    "sahagataṃ uddhaccasahagataṃ mohaṃ": "के साथ होने वाला और बेचैनी के साथ होने वाला मोह",
    "diṭṭhigata": "ग़लत दृष्टि", "diṭṭhigatavippayutta": "ग़लत दृष्टि से अलग",
    "diṭṭhigatavippayuttā": "ग़लत दृष्टि से अलग",
    "vippayuttalobha": "लोभ … अलग", "vippayuttā lobha": "लोभ … अलग",
    "ñāṇa": "ज्ञान", "ñāṇavippayutta": "ज्ञान से अलग", "ñāṇavippayutte": "ज्ञान से अलग",
    "sasaṅkhārikesu": "प्रेरणा सहित होने वाला",
    "dasa": "दस", "dvādasa": "बारह", "ekādasa": "ग्यारह",
    # mind and its elements
    "mano": "मन", "manodhātu": "मन का तत्व", "manodhātuyo": "मन के … तत्व", "dhātu": "तत्व",
    "dhātuyo": "तत्व", "manoviññāṇa": "मन की चेतना", "kiriyāmano": "केवल क्रिया रूपी मन",
    "kiriyāmanodhātu": "केवल क्रिया रूपी मन का तत्व", "hetuka": "मूल",
    "kiriyāhetukamanoviññāṇa": "मूल से रहित केवल क्रिया रूपी मन की चेतना",
    "kiriyāhetukamanoviññāṇadhātu": "मूल से रहित केवल क्रिया रूपी मन की चेतना का … तत्व",
    "viññāṇāni": "इंद्रिय-चेतना", "pañcaviññāṇāni": "पाँच-पाँच इंद्रिय-चेतना",
    "cakkhuviññāṇaṃ": "आँख की चेतना", "sotaviññāṇaṃ": "कान की चेतना",
    "ghānaviññāṇaṃ": "नाक की चेतना", "jivhāviññāṇaṃ": "जीभ की चेतना",
    "kāyaviññāṇaṃ": "शरीर की चेतना",
    "khandho": "समूह", "vedanākkhandho": "अनुभूति का समूह", "saññākkhandho": "पहचान का समूह",
    "saṅkhārakkhandho": "मानसिक रचनाओं का समूह", "saññā": "पहचान", "saṅkhāra": "मानसिक रचनाएँ",
    "asaññā": "अ-पहचान",
    # absorptions
    "jhānaṃ": "ध्यान", "jhānā": "ध्यान", "jhāne": "ध्यान", "jhānassa": "ध्यान",
    "catutthaṃ jhānaṃ": "चौथा ध्यान", "catutthassa jhānassa": "चौथा ध्यान",
    "lokuttaraṃ catutthaṃ jhānaṃ": "लोकोत्तर चौथा ध्यान",
    "lokuttaraṃ paṭhamaṃ jhānaṃ": "लोकोत्तर पहला ध्यान",
    "lokuttarapañcakanaye dutiyaṃ jhānaṃ": "पाँच-पाँच की विधि में लोकोत्तर दूसरा ध्यान",
    "pañcaka": "पाँच-पाँच", "pañcakanaye": "पाँच-पाँच की विधि", "naye": "विधि",
    "āruppā": "अभौतिक अवस्था", "viññāṇañcāyatanaṃ": "अनंत चेतना का क्षेत्र",
    "ānañcāyatanaṃ": "अनंत … का क्षेत्र", "ānañca": "अनंत", "ākāsa": "आकाश",
    "ākiñcañña": "कुछ भी न होना",
    "uppanne vitakkavicāre": "उत्पन्न आरंभिक विचार और सतत विचार",
    "uppannaṃ vicāraṃ": "उत्पन्न सतत विचार", "uppannaṃ vitakkaṃ": "उत्पन्न आरंभिक विचार",
    "uppanno ca vicāro": "उत्पन्न सतत विचार", "sahajāto": "के साथ उत्पन्न",
    # paths, fruits, nibbāna, form
    "maggā": "मार्ग", "maggā apariyāpannā": "अस्तित्व के लोकों में न समाए हुए … मार्ग",
    "sāmañña": "श्रमण-जीवन", "phalāni": "फल", "phalaṃ": "फल",
    "sāmaññaphalāni nibbānañca": "श्रमण-जीवन के … फल और निर्वाण",
    "arahatta": "अर्हत्-पद", "upariṭṭhimaṃ": "सबसे ऊँचा", "ariya": "आर्य",
    "rūpañca": "भौतिक रूप", "rūpañca nibbānañca": "भौतिक रूप और निर्वाण",
    "rūpaṃ": "भौतिक रूप", "rūpaṃ nibbānañca": "भौतिक रूप और निर्वाण",
    "nibbānañca anārammaṇā": "निर्वाण विषय से रहित",
    "avasesañca": "शेष", "avasesañca rūpaṃ": "शेष भौतिक रूप",
    "kammassa": "कर्म", "kammassa katattā": "कर्म किए जाने के कारण", "yañca": "जो भी", "yaṃ": "जो भी",
    "indriya": "इंद्रिय", "baddha": "बँधा",
    "indriyabaddharūpañca nibbānañca": "इंद्रियों से बँधा भौतिक रूप और निर्वाण",
    "upādāya": "व्युत्पन्न", "upādāya rūpaṃ": "व्युत्पन्न भौतिक रूप",
    "bhūtā": "महाभूत", "mahābhūtā": "महाभूत",
    "cakkhu": "आँख", "cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र",
    "phoṭṭhabba": "स्पर्श", "phoṭṭhabbāyatanaṃ": "स्पर्श का इंद्रिय-क्षेत्र",
    "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र", "sadda": "ध्वनि",
    "saddāyatanaṃ": "ध्वनि का इंद्रिय-क्षेत्र", "gandha": "गंध",
    "gandhāyatanaṃ": "गंध का इंद्रिय-क्षेत्र", "rasa": "स्वाद", "rasāyatanaṃ": "स्वाद का इंद्रिय-क्षेत्र",
    "dhamma": "मन के विषय", "dhammāyatana": "मन के विषयों का इंद्रिय-क्षेत्र",
    "dhammāyatanaṃ": "मन के विषयों का इंद्रिय-क्षेत्र", "manāyatanaṃ": "मन का इंद्रिय-क्षेत्र",
    "ākāsadhātu": "आकाश तत्व", "āpo": "जल", "āpodhātu": "जल तत्व",
    "vacī": "वाणी", "viññatti": "प्रकट अभिव्यक्ति",
    "kāyaviññatti": "शरीर द्वारा प्रकट अभिव्यक्ति", "vacīviññatti": "वाणी द्वारा प्रकट अभिव्यक्ति",
    "cittajaṃ": "मन से जन्मा", "hetukaṃ": "कारण", "lahutā": "हल्कापन", "mudutā": "मृदुता",
    "kammaññatā": "कार्य-योग्यता", "santati": "धारा",
    "rūpassa lahutā": "भौतिक रूप का हल्कापन", "rūpassa mudutā": "भौतिक रूप की मृदुता",
    "rūpassa kammaññatā": "भौतिक रूप की कार्य-योग्यता", "rūpassa upacayo": "भौतिक रूप की वृद्धि",
    "rūpassa santati": "भौतिक रूप की धारा",
    "kabaḷīkāro": "कौर-कौर खाया जाने वाला", "āhāro": "भोजन",
    "kabaḷīkāro āhāro": "कौर-कौर खाया जाने वाला भोजन",
    # roots and defilements
    "lobho": "लोभ", "doso": "द्वेष", "moho": "मोह", "mohaṃ": "मोह",
    "alobho": "लोभ का अभाव", "adoso": "द्वेष का अभाव", "amoho": "मोह का अभाव",
    "kusalahetu": "हितकर मूल", "kusalahetū": "हितकर मूल", "akusalahetū": "हानिकर मूल",
    "abyākatahetū": "नैतिक रूप से अनिर्धारित मूल", "vipākahetu": "कर्म-फल रूपी मूल",
    "kiriyahetu": "केवल क्रिया रूपी मूल",
    "uppajjati": "उत्पन्न होना", "uppajjanti": "उत्पन्न होना", "ekato": "एक साथ",
    "hetū ekato uppajjanti": "मूल एक साथ उत्पन्न होना",
    "uppannaṃ": "उत्पन्न", "uppanne": "उत्पन्न", "uppanno": "उत्पन्न", "uppanne hetū": "उत्पन्न मूल",
    "ṭhapetvā": "छोड़कर", "siyā": "कभी",
    "kāmāsavo": "इंद्रिय-सुखों का मैल", "bhavāsavo": "अस्तित्व का मैल", "diṭṭhāsavo": "दृष्टि का मैल",
    "avijjāsavo": "अज्ञान का मैल", "bhava": "अस्तित्व", "avijjā": "अज्ञान", "diṭṭhi": "दृष्टि",
    "kāmarāgasaṃyojanaṃ": "इंद्रिय-सुखों के राग का बंधन", "paṭighasaṃyojanaṃ": "चिढ़ का बंधन",
    "mānasaṃyojanaṃ": "अहंकार का बंधन", "diṭṭhisaṃyojanaṃ": "दृष्टि का बंधन",
    "vicikicchāsaṃyojanaṃ": "संशय का बंधन", "parāmāsasaṃyojanaṃ": "ग़लत धारणा का बंधन",
    "rāgasaṃyojanaṃ": "राग का बंधन", "issāsaṃyojanaṃ": "ईर्ष्या का बंधन",
    "macchariyasaṃyojanaṃ": "कंजूसी का बंधन", "avijjāsaṃyojanaṃ": "अज्ञान का बंधन",
    "kāmarāga": "इंद्रिय-सुखों का राग", "rāga": "राग", "paṭigha": "चिढ़", "paṭighaṃ": "चिढ़",
    "māna": "अहंकार", "māno": "अहंकार", "issā": "ईर्ष्या", "macchariya": "कंजूसी",
    "sīla": "सदाचार", "vata": "व्रत", "sīlabbata": "सदाचार और व्रत",
    "sīlabbataparāmāsa": "सदाचार और व्रतों के बारे में ग़लत धारणा",
    "sīlabbataparāmāso": "सदाचार और व्रतों के बारे में ग़लत धारणा",
    "abhijjhā": "लालच", "abhijjhākāyagantho": "लालच रूपी काया की गाँठ",
    "kāyagantho": "काया की गाँठ", "byāpādo": "दुर्भावना",
    "byāpādo kāyagantho": "दुर्भावना रूपी काया की गाँठ",
    "parāmāso kāyagantho": "ग़लत धारणा रूपी काया की गाँठ", "abhiniveso": "आग्रह",
    "abhiniveso kāyagantho": "आग्रह रूपी काया की गाँठ", "sacca": "सत्य",
    "kāmacchanda": "इंद्रिय-सुखों की चाह", "chanda": "चाह",
    "kāmacchandanīvaraṇaṃ": "इंद्रिय-सुखों की चाह की बाधा", "byāpāda": "दुर्भावना",
    "byāpādanīvaraṇaṃ": "दुर्भावना की बाधा", "thina": "आलस्य", "middha": "तंद्रा",
    "thinamiddhanīvaraṇaṃ": "आलस्य और तंद्रा की बाधा",
    "uddhaccakukkuccanīvaraṇaṃ": "बेचैनी और पछतावे की बाधा", "kukkucca": "पछतावा",
    "kukkuccanīvaraṇaṃ": "पछतावे की बाधा", "vicikicchānīvaraṇaṃ": "संशय की बाधा",
    "avijjānīvaraṇaṃ": "अज्ञान की बाधा",
    "diṭṭhiparāmāso": "दृष्टि रूपी ग़लत धारणा",
    "kāmupādānaṃ": "इंद्रिय-सुखों के प्रति आसक्ति", "diṭṭhupādānaṃ": "दृष्टियों के प्रति आसक्ति",
    "sīlabbatupādānaṃ": "सदाचार और व्रतों के प्रति आसक्ति", "atta": "आत्मा", "vāda": "सिद्धांत",
    "vatthūni": "आधार", "uddhaccaṃ": "बेचैनी", "thinaṃ": "आलस्य", "ahirikaṃ": "निर्लज्जता",
    "anottappaṃ": "बुराई के प्रति निडरता",
    # vattabba clauses
    "vattabbā": VJ, "vattabbaṃ": VJ, "vattabbo": VJ,
    "vattabbo savitakkasavicāro": f"आरंभिक विचार और सतत विचार वाली {P} {VJ}",
    "vattabbaṃ pītisahagatanti": f"उल्लास के साथ होने वाली {P} … {VJ}",
    "vattabbā parittārammaṇā": f"सीमित विषय वाली {P} {VJ}",
    "vattabbā maggārammaṇā": f"मार्ग को विषय बनाने वाली {P} {VJ}",
    "vattabbā atītārammaṇā": f"अतीत के विषय वाली {P} {VJ}",
    "vattabbā anuppannā": f"उत्पन्न न हुई {P} … {VJ}",
    "vattabbaṃ ajjhattārammaṇanti": f"स्वयं से संबंधित विषय वाली {P} {VJ}",
    # bare dhammā
    "dhammā": P,
}

# 'dhammā X' and 'X dhammā': the phrase agrees with परिघटना
DH = {
    "abyākatā": "नैतिक रूप से अनिर्धारित", "aganthaniyā": "गाँठों का विषय न बनने वाली",
    "ahetukā": "मूल से रहित", "ajjhattikā": "आंतरिक", "akusalā": "हानिकर",
    "anidassanā": "दिखाई न देने वाली",
    "anupādiṇṇaanupādāniyā": "न कर्म से उत्पन्न न आसक्ति का विषय बनने वाली",
    "anupādiṇṇupādāniyā": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली",
    "anupādiṇṇā": "कर्म से उत्पन्न न होने वाली", "anupādāniyā": "आसक्ति का विषय न बनने वाली",
    "anuttarā": "सर्वोच्च", "anāsavā": "मन के मैलों का विषय न बनने वाली",
    "anīvaraṇiyā": "बाधाओं का विषय न बनने वाली", "apacayagāmino": "संचय घटाने की ओर ले जाने वाली",
    "apariyāpannā": "अस्तित्व के लोकों में न समाई हुई", "appaccayā": "कारणों पर निर्भर न रहने वाली",
    "appamāṇā": "अपरिमित", "appaṭighā": "टकराव से रहित", "appītikā": "उल्लास से रहित",
    "araṇā": "संघर्ष से रहित", "arūpino": "अभौतिक", "asaṃkilesikā": "क्लेशों की ओर न ले जाने वाली",
    "asaṃkiliṭṭhā": "क्लेशों से मलिन न होने वाली", "asaṃyojaniyā": "बंधनों का विषय न बनने वाली",
    "asaṅkhatā": "अनिर्मित", "avicārā": "सतत विचार से रहित",
    "avitakkaavicārā": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "avitakkavicāramattā": "आरंभिक विचार से रहित केवल सतत विचार वाली",
    "avitakkā": "आरंभिक विचार से रहित",
    "bhāvanāya pahātabbahetukā": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "bāhirā": "बाह्य", "cittasahabhuno": "मन के साथ-साथ होने वाली",
    "cittasamuṭṭhānā": "मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhuno": "मन से घुली-मिली मन से उत्पन्न और मन के साथ-साथ होने वाली",
    "cittasaṃsaṭṭhasamuṭṭhānā": "मन से घुली-मिली और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "मन से घुली-मिली मन से उत्पन्न और मन का अनुसरण करने वाली",
    "cittasaṃsaṭṭhā": "मन से घुली-मिली", "cittavippayuttā": "मन से अलग",
    "cittavisaṃsaṭṭhā": "मन से घुली-मिली न होने वाली", "cittānuparivattino": "मन का अनुसरण करने वाली",
    "dassanena pahātabbahetukā": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली",
    "ganthaniyā": "गाँठों का विषय बनने वाली", "ganthavippayuttā": "गाँठों से अलग",
    "hetuvippayuttā": "मूलों से अलग", "hīnā": "हीन",
    "kenaci viññeyyā": "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    "kilesavippayuttā": "क्लेशों से अलग", "kusalā": "हितकर", "lokiyā": "लौकिक",
    "lokuttarā": "लोकोत्तर", "mahaggatā": "उन्नत", "majjhimā": "मध्यम",
    "micchattaniyatā": "ग़लत दिशा में निश्चित", "na pītisahagatā": "उल्लास के साथ न होने वाली",
    "na sukhasahagatā": "सुख के साथ न होने वाली", "na upekkhāsahagatā": "समभाव के साथ न होने वाली",
    "nevācayagāmināpacayagāmino": "न संचय की ओर न संचय घटाने की ओर ले जाने वाली",
    "niyatā": "निश्चित", "niyyānikā": "मुक्ति की ओर ले जाने वाली",
    "no cittasahabhuno": "मन के साथ-साथ न होने वाली", "no cittasamuṭṭhānā": "मन से उत्पन्न न होने वाली",
    "no cittānuparivattino": "मन का अनुसरण न करने वाली",
    "nīvaraṇavippayuttā": "बाधाओं से अलग", "nīvaraṇiyā": "बाधाओं का विषय बनने वाली",
    "parittā": "सीमित", "pariyāpannā": "अस्तित्व के लोकों में समाई हुई",
    "parāmaṭṭhā": "ग़लत धारणा का विषय बनने वाली", "parāmāsavippayuttā": "ग़लत धारणा से अलग",
    "paṇītā": "उत्तम", "pītisahagatā": "उल्लास के साथ होने वाली", "rūpino": "भौतिक",
    "sahetukā": "मूल वाली", "sammattaniyatā": "सही दिशा में निश्चित",
    "sanidassanā": "दिखाई देने वाली", "sappaṭighā": "टकराव वाली", "sappītikā": "उल्लास वाली",
    "saraṇā": "संघर्ष वाली", "sauttarā": "सर्वोच्च न होने वाली", "savicārā": "सतत विचार वाली",
    "savitakkasavicārā": "आरंभिक विचार और सतत विचार वाली", "savitakkā": "आरंभिक विचार वाली",
    "saṃkilesikā": "क्लेशों की ओर ले जाने वाली", "saṃkiliṭṭhā": "क्लेशों से मलिन",
    "saṃyojanavippayuttā": "बंधनों से अलग", "saṃyojaniyā": "बंधनों का विषय बनने वाली",
    "saṅkhatā": "निर्मित", "sukhasahagatā": "सुख के साथ होने वाली",
    "sāsavā": "मन के मैलों का विषय बनने वाली", "upekkhāsahagatā": "समभाव के साथ होने वाली",
    "uppannā": "उत्पन्न हो चुकी",
    "upādiṇṇupādāniyā": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली",
    "upādiṇṇā": "कर्म से उत्पन्न", "upādā": "व्युत्पन्न", "upādānavippayuttā": "आसक्ति से अलग",
    "upādāniyā": "आसक्ति का विषय बनने वाली", "ācayagāmino": "संचय की ओर ले जाने वाली",
    "āsavavippayuttā": "मन के मैलों से अलग",
}
# «कौन-सी परिघटनाएँ … नहीं हैं» (no cittasaṃsaṭṭha… questions)
NO_CL = {
    "no cittasaṃsaṭṭhasamuṭṭhānā": "मन से घुली-मिली और मन से उत्पन्न",
    "no cittasaṃsaṭṭhasamuṭṭhānasahabhuno": "मन से घुली-मिली मन से उत्पन्न और मन के साथ-साथ होने वाली",
    "no cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "मन से घुली-मिली मन से उत्पन्न और मन का अनुसरण करने वाली",
}
for _k, _v in DH.items():
    T[f"dhammā {_k}"] = f"{_v} {P}"
    T[f"{_k} dhammā"] = f"{_v} {P}"
for _k, _v in NO_CL.items():
    T[f"dhammā {_k}"] = f"{P} {_v} नहीं है"

# per-segment overrides {bid: {kw: value}}
OVERRIDES = {
    # «ahetuke cittuppāde» comes after «cattāro ñāṇavippayutte cittuppāde» (numbered) in this segment
    "1-1441": {"cittuppāde": "मन की … उत्पत्ति"},
    # sekkhā as the fragment of asekkhā: «सीखना पूरा होने के चरण की»
    "1-1415": {"sekkhā": "सीखना … के चरण का"},
    # diṭṭhi as the wrong view in «diṭṭhi ca lobho ca ekato uppajjanti»
    "1-1497": {"diṭṭhi": "ग़लत दृष्टि"},
    "1-1561": {"diṭṭhi": "ग़लत दृष्टि"},
    # kilesa of kilesavatthūni: «मन के क्लेशों के दस आधार»
    "1-1565": {"kilesa": "मन के क्लेश"},
    # ārammaṇā of anārammaṇā: «विषय से रहित»
    "1-1526": {"ārammaṇā": "विषय"},
    # appītikā: «उल्लास से रहित»
    "1-1594": {"pītikā": "उल्लास"},
    # na dassanena / na bhāvanāya pahātabbahetukā: «… छोड़े जाने वाले मूलों से रहित»
    "1-1586": {"pahātabbahetukā": "छोड़े जाने वाले मूल", "hetukā": "मूल"},
    "1-1588": {"pahātabbahetukā": "छोड़े जाने वाले मूल", "hetukā": "मूल"},
    # matrix ārammaṇā in maggārammaṇā: «मार्ग को विषय बनाने वाली»; maggahetukā «मार्ग को मूल बनाने वाली»
    "1-1429": {"ārammaṇā": "विषय बनाने वाला", "hetukā": "मूल बनाने वाला"},
    # sahetukā: «मूल वाली»; ahetukā: «मूल से रहित»
    "1-1443": {"hetukā": "मूल वाला"},
    "1-1444": {"hetukā": "मूल"},
    "1-1448": {"hetukā": "मूल वाला"},
    # headings / colophon
    "1-4-2-12-0": {"Kilesa": "मन के क्लेश"},
    "1-1616": {"Dhamma": P},
}

# closing pair of each cluster: «X से अलग, पर उनका / उसका विषय बनने वाली» / «… और उनका / उसका विषय न बनने वाली»
CLOSING = {
    "1-1475": {"sāsavā": "उनका विषय बनने वाला"},
    "1-1476": {"sāsavā": "उनका विषय बनने वाला", "anāsavā": "उनका विषय न बनने वाला"},
    "1-1487": {"saṃyojaniyā": "उनका विषय बनने वाला"},
    "1-1488": {"saṃyojaniyā": "उनका विषय बनने वाला"},
    "1-1499": {"ganthaniyā": "उनका विषय बनने वाला"},
    "1-1500": {"ganthaniyā": "उनका विषय बनने वाला"},
    "1-1513": {"nīvaraṇiyā": "उनका विषय बनने वाला"},
    "1-1514": {"nīvaraṇiyā": "उनका विषय बनने वाला"},
    "1-1523": {"parāmaṭṭhā": "उसका विषय बनने वाला"},
    "1-1524": {"parāmaṭṭhā": "उसका विषय बनने वाला"},
    "1-1563": {"upādāniyā": "उसका विषय बनने वाला"},
    "1-1564": {"upādāniyā": "उसका विषय बनने वाला"},
}
for _b, _d in CLOSING.items():
    OVERRIDES.setdefault(_b, {}).update(_d)

HI = read_hindi(PART)
PI = read_pali(PART)
FALLBACK = []  # (bid, kw, value) where the contiguous form was absent and the " … " form was used


def sahagata(base, text):
    """X-sahagatā: «X के साथ होने वाली» or, in the dhātu clause, «… जो X के साथ होता है»."""
    v = f"{base}के साथ होने वाला"
    return v if present(v, text) else f"{base}के साथ होना"


def resolve(bid, kw, kws):
    text = HI[bid]
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    k = lc(kw)
    s = set(lc(x) for x in kws)
    # rūpa: दृश्य रूप beside rūpāyatanaṃ, else the sphere name (सूक्ष्म भौतिक)
    if k == "rūpa":
        return "दृश्य रूप" if "rūpāyatanaṃ" in s else "सूक्ष्म भौतिक"
    # sahagatacitta: contiguous «… के साथ होने वाली मन की …» unless its only source is
    # diṭṭhigata(sam|vip)payuttalobhasahagatacittuppādā = «लोभ के साथ होने वाली और ग़लत दृष्टि से जुड़ी / अलग मन की …»
    if k == "sahagatacitta":
        srcs = re.findall(r"(\w*)sahagatacitt", PI[bid])
        if srcs and all(x.endswith("payuttalobha") for x in srcs):
            return "के साथ होने वाला … मन"
        return T[k]
    # kāya: काया in the gantha list, शरीर in kāyaviññatti
    if k == "kāya":
        return "काया" if "kāyagantho" in s else "शरीर"
    # X-sahagatā in the «… का वह तत्व जो X के साथ होता है» clause
    if k in ("sahagatā", "somanassasahagatā", "upekkhāsahagatā"):
        base = {"sahagatā": "", "somanassasahagatā": "प्रसन्नता ", "upekkhāsahagatā": "समभाव "}[k]
        return sahagata(base, text)
    if k == "dhātu upekkhāsahagatā":
        return "तत्व … " + sahagata("समभाव ", text)
    if k == "manoviññāṇadhātu upekkhāsahagatā":
        return "मन की चेतना का … तत्व … " + sahagata("समभाव ", text)
    if k == "manoviññāṇadhātu":
        return "मन की चेतना का तत्व" if present("मन की चेतना का तत्व", text) else "मन की चेतना का … तत्व"
    # kusalato / kiriyato: «… मन में से» (kāmāvacara lists) or the bare adjective in «(हितकर, … केवल क्रिया रूपी)»
    if k == "kusalato":
        return "हितकर मन" if "हितकर मन में से" in text else "हितकर"
    if k == "kiriyato":
        return "केवल क्रिया रूपी मन" if "केवल क्रिया रूपी मन में से" in text else "केवल क्रिया रूपी"
    # vattabba: «कहा जा सकता» or «कहा नहीं जा सकता»
    if k in ("vattabbā", "vattabbaṃ", "vattabbo") and not present(VJ, text):
        return "कहा … जा सकना"
    # the four jhāna-count compounds
    if k.endswith("jjhānā") and k.startswith("lokuttara"):
        nums = {"tikacatukka": ("तीन", "चार"), "tikatika": ("तीन", "तीन"), "dukatika": ("दो", "तीन"),
                "dukaduka": ("दो", "दो"), "ekakaduka": ("एक", "दो")}
        a, b = nums[k[len("lokuttara"):-len("jjhānā")]]
        return f"लोकोत्तर वे ध्यान जो चार-चार की विधि में {a} और पाँच-पाँच की विधि में {b} हैं"
    v = T[k]
    if not present(v, text) and v.endswith(" " + P) and GAP not in v:
        g = v[: -len(P) - 1] + GAP + P
        if present(g, text):
            FALLBACK.append((bid, kw, g))
            return g
    return v


def present_mn(v, text):
    """Presence allowing the oblique plural मनों for मन (the shared check does not inflect 2-letter words)."""
    return present(v, text.replace("मनों", "मन"))


if __name__ == "__main__":
    n = build_part(PART, resolve)
    bad, nde, miss = verify(PART, show=0)
    for f in FALLBACK:
        print("   GAP-FORM", *f)
    rest = [m for m in miss if not present_mn(m[2], HI[m[0]])]
    print("presence misses:", len(miss), "| of which only मनों:", len(miss) - len(rest), "| other:", len(rest))
    for m in miss:
        tag = "MN " if m not in rest else "MISS"
        print("  ", tag, *m)
