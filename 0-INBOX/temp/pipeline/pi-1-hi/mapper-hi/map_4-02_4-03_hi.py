"""Map 4-02-nikkhepakandam and 4-03-nikkhepakandam keywords to the Hindi translation.

usage: python -I -X utf8 map_4-02_4-03_hi.py
Resolution order: per-segment SEG overrides -> cluster tables (by id range) -> context rules
(vuccati X, rūpa, dhamma, mano, kāya) -> BASE -> CH2 (shared table).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import CH2, NDE, GAP, lc, build_part, verify  # noqa: E402

P = "परिघटना"

# ---------------------------------------------------------------------------- base table
BASE = {
    # question frames, particles
    "tattha": "यहाँ", "yo": "जो", "yā": "जो", "yaṃ": "जो", "ye": "जो", "ye ye": "जो-जो", "taṃ taṃ": "वह-वह",
    "dhammā": P, "evarūpā": "इस प्रकार का", "evarūpo": "इस प्रकार का", "evarūpaṃ": "इस प्रकार का",
    "ṭhapetvā": "छोड़कर", "avasesā": "शेष", "avaseso": "शेष", "yañca": "और जो", "tehi dhammehi": "उन परिघटनाओं के संबंध में",
    # the khandha / plane frame
    "khandho": "समूह", "khandhā": "समूह", "khandha": "समूह",
    "rūpakkhandho": "भौतिक रूप का समूह", "rūpaṃ": "भौतिक रूप",
    "vedanā": "अनुभूति", "saññā": "पहचान", "saṅkhāra": "मानसिक रचनाएँ", "saṅkhārā": "मानसिक रचनाएँ",
    "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित", "kāmāvacare": "इंद्रिय-सुखों के लोक से संबंधित",
    "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित", "rūpāvacare": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpa": "अभौतिक", "arūpāvacarā": "अभौतिक लोक से संबंधित", "arūpāvacare": "अभौतिक लोक से संबंधित",
    "avacarā": "लोक से संबंधित", "avacare": "लोक से संबंधित", "bhūmiyaṃ": "स्तर",
    "abyākatā": "नैतिक रूप से अनिर्धारित", "abyākatā dhammā": f"नैतिक रूप से अनिर्धारित {P}",
    "akusala": "हानिकर", "akusalā": "हानिकर", "akusalā dhammā": f"हानिकर {P}",
    "kusalā": "हितकर", "kusalā dhammā": f"हितकर {P}", "kusalānaṃ": "हितकर", "kusalānaṃ dhammānaṃ": f"हितकर {P}",
    "akusalābyākatā": "हानिकर और नैतिक रूप से अनिर्धारित",
    "avasesā kusala": "शेष हितकर", "avasesā sāsavā kusala": "शेष मन के मैलों का विषय बनने वाला हितकर",
    "sāsavā": "मन के मैलों का विषय बनने वाला", "āsavā": "मन के मैल",
    "sāsavā kusalākusalābyākatā dhammā": f"मन के मैलों का विषय बनने वाली हितकर हानिकर और नैतिक रूप से अनिर्धारित {P}",
    "sāsavā kusalābyākatā dhammā": f"मन के मैलों का विषय बनने वाली हितकर और नैतिक रूप से अनिर्धारित {P}",
    "sāsavā kusalākusalā dhammā": f"मन के मैलों का विषय बनने वाली हितकर और हानिकर {P}",
    "asaṅkhatā": "अनिर्मित", "asaṅkhatā ca dhātu": "अनिर्मित तत्व",
    "phalāni": "फल", "phala": "फल", "maggā": "मार्ग", "magga": "मार्ग",
    "apariyāpannā maggā": "अस्तित्व के लोकों में न समाए हुए मार्ग",
    "maggā apariyāpannā": "अस्तित्व के लोकों में न समाए हुए" + GAP + "मार्ग",
    "apariyāpannā": "अस्तित्व के लोकों में न समाई हुई",
    "sampayuttā": "जुड़ा", "sampayutto": "जुड़ा", "sampayuttakā": "जुड़ा", "vippayuttā": "अलग",
    # matrix / cluster names
    "ogha": "बाढ़", "yoga": "जकड़न", "nīvaraṇa": "बाधा", "parāmāsa": "ग़लत धारणा", "upādāna": "आसक्ति",
    "kilesa": "क्लेश", "piṭṭhi": "अंतिम", "antara": "बीच का", "antaradukaṃ": "बीच के" + GAP + "दो-दो के वर्गीकरण",
    "dukaṃ": "दो-दो के वर्गीकरण", "duka": "दो-दो के वर्गीकरण", "suttantika": "उपदेश", "nikkhepaṃ": "सारांश",
    "nikkhepa": "सारांश", "kaṇḍe": "अध्याय", "kaṇḍaṃ": "अध्याय", "niṭṭhitaṃ": "पूरा हुआ", "abhidhamma": "अभिधम्म",
    # hindrances
    "nīvaraṇaṃ": "बाधा", "nīvaraṇā": "बाधा", "nīvaraṇāni": "बाधा",
    "kāmacchandanīvaraṇaṃ": "इंद्रिय-सुखों की चाह की बाधा", "byāpādanīvaraṇaṃ": "दुर्भावना की बाधा",
    "thinamiddhanīvaraṇaṃ": "आलस्य और तंद्रा की बाधा", "uddhaccakukkuccanīvaraṇaṃ": "बेचैनी और पछतावे की बाधा",
    "vicikicchānīvaraṇaṃ": "संशय की बाधा", "avijjānīvaraṇaṃ": "अज्ञान की बाधा", "avijjānīvaraṇena": "अज्ञान की बाधा",
    "uddhaccanīvaraṇaṃ": "बेचैनी की बाधा", "kukkuccanīvaraṇaṃ": "पछतावे की बाधा",
    "kāmacchanda": "इंद्रिय-सुखों की चाह", "kāmacchando": "इंद्रिय-सुखों की चाह", "chanda": "चाह", "chando": "चाह",
    "byāpāda": "दुर्भावना", "thina": "आलस्य", "middha": "तंद्रा", "uddhacca": "बेचैनी", "kukkucca": "पछतावा",
    "vicikicchā": "संशय", "avijjā": "अज्ञान", "kāmesu": "इंद्रिय-सुख", "kāmarāgo": "इंद्रिय-सुखों का राग",
    "rāgo": "राग", "nandī": "आनंद", "taṇhā": "तृष्णा", "sineho": "स्नेह", "pariḷāho": "ताप", "mucchā": "मूर्छा",
    # dosa string
    "āghāto": "आक्रोश", "āghāto jāyati": "आक्रोश उत्पन्न होना", "jāyati": "उत्पन्न होना", "anatthaṃ": "अहित",
    "acarīti": "किया", "caratīti": "कर रहा", "piyassa": "प्रिय", "manāpassa": "मनभावन", "aṭṭhāne": "बिना कारण",
    "paṭighāto": "प्रतिघात", "paṭighaṃ": "चिढ़", "paṭivirodho": "प्रतिविरोध", "kopo": "कोप", "pakopo": "प्रकोप",
    "sampakopo": "तीव्र प्रकोप", "doso": "द्वेष", "padoso": "गहरा द्वेष", "sampadoso": "तीव्र द्वेष",
    "byāpatti": "दुर्भावना", "kodho": "क्रोध", "kujjhanā": "क्रोध करना", "dussanā": "द्वेष करना",
    "dussitattaṃ": "द्वेष से भरा होना", "byāpajjanā": "दुर्भावना रखना", "virodho": "विरोध", "caṇḍikkaṃ": "उग्रता",
    "asuropo": "कटु वचन", "anattamanatā": "अप्रसन्नता",
    # thina / middha / uddhacca / kukkucca strings
    "akallatā": "अस्वस्थता", "akammaññatā": "कार्य-अयोग्यता", "olīyanā": "ढीला पड़ना", "sallīyanā": "सिकुड़ जाना",
    "līnaṃ": "शिथिलता", "līyanā": "शिथिल होना", "thinaṃ": "आलस्य", "thiyanā": "आलसी होना",
    "thiyitattaṃ": "आलस्य से भरा होना", "onāho": "ढक जाना", "antosamorodho": "भीतर ही भीतर घिर जाना",
    "middhaṃ": "तंद्रा", "soppaṃ": "नींद", "pacalāyikā": "ऊँघ", "supanā": "सोना", "supitattaṃ": "सोया हुआ होना",
    "uddhaccaṃ": "बेचैनी", "avūpasamo": "अशांति", "vikkhepo": "भटकाव", "bhantattaṃ": "डाँवाडोल होना",
    "kappiye": "उचित", "avajje": "निर्दोष", "vajja": "निंदनीय", "saññitā": "समझना", "kukkuccaṃ": "पछतावा",
    "kukkuccāyanā": "पछताना", "vippaṭisāro": "ग्लानि",
    # vicikicchā string
    "satthari": "गुरु", "dhamme": "शिक्षा", "sikkhāya": "प्रशिक्षण", "kaṅkhati": "शंका करना", "kaṅkhā": "शंका",
    "vimati": "दुविधा", "dveḷhakaṃ": "दुचित्तापन", "dvedhāpatho": "दोराहा", "saṃsayo": "संदेह",
    "anekaṃsaggāho": "किसी एक बात को पक्का न पकड़ पाना", "ekaṃsa": "पक्का", "āsappanā": "हिचकिचाना",
    "parisappanā": "बार-बार हिचकिचाना", "apariyogāhanā": "गहराई में न उतर पाना", "pariyogāhanā": "गहराई में उतरना",
    "thambhitattaṃ": "जड़ हो जाना",
    "idappaccayatā": "कार्य-कारण का नियम", "samuppannesu": "उत्पन्न", "samuppannesu dhammesu": f"उत्पन्न {P}",
    "paṭiccasamuppannesu": "परस्पर-आश्रित रूप से उत्पन्न",
    "paṭiccasamuppannesu dhammesu": f"परस्पर-आश्रित रूप से उत्पन्न {P}",
    # moha string
    "dukkhe": "दुःख", "samudaye": "उत्पत्ति", "nirodhe": "अंत", "dukkhanirodhe": "दुःख का अंत",
    "ñāṇaṃ": "जानना", "aññāṇaṃ": "न जानना", "dassanaṃ": "देखना", "adassanaṃ": "न देखना",
    "anabhisamayo": "सत्य तक न पहुँचना", "anubodho": "बोध", "ananubodho": "बोध न होना",
    "sambodho": "पूर्ण बोध", "asambodho": "पूर्ण बोध न होना", "appaṭivedho": "भेद न पाना",
    "asaṃgāhanā": "न समेट पाना", "samapekkhanā": "निष्पक्ष रूप से देखना", "asamapekkhanā": "निष्पक्ष रूप से न देखना",
    "paccavekkhaṇā": "पुनः विचार करना", "apaccavekkhaṇā": "पुनः विचार न करना",
    "paccakkhakammaṃ": "प्रत्यक्ष करना", "apaccakkhakammaṃ": "प्रत्यक्ष न करना", "dummejjhaṃ": "दुर्बुद्धि",
    "bālyaṃ": "मूर्खता", "sampajaññaṃ": "स्पष्ट समझ", "asampajaññaṃ": "स्पष्ट समझ का अभाव", "moho": "मोह",
    "pamoho": "गहरा मोह", "sammoho": "घोर मोह", "ogho": "बाढ़", "yogo": "जकड़न", "anusayo": "सुप्त प्रवृत्ति",
    "pariyuṭṭhānaṃ": "आवेश", "laṅgī": "रुकावट", "mūlaṃ": "मूल", "akusalamūlaṃ": "हानिकर मूल",
    "mūlāni": "मूल", "akusalamūlāni": "हानिकर मूल",
    # diṭṭhi string
    "abhiniveso": "आग्रह", "visūkāyikaṃ": "टेढ़ापन", "vipariyāsa": "उलटा", "vipariyāsaggāho": "उलटी पकड़",
    "tittha": "मतवाद", "saṃyojanaṃ": "बंधन", "diṭṭhisaṃyojanaṃ": "दृष्टि का बंधन", "patiṭṭhāho": "कसकर पकड़ना",
    "gāho": "पकड़", "diṭṭhigataṃ": "दृष्टि में पड़ जाना", "parāmāso": "ग़लत धारणा", "parāmāsā": "ग़लत धारणा",
    "patho": "रास्ता", "maggo": "कुमार्ग", "gahanaṃ": "घना जंगल", "vipphanditaṃ": "छटपटाहट", "diṭṭhi": "दृष्टि",
    "kantāro": "बीहड़", "kummaggo": "कुमार्ग", "micchā": "ग़लत", "micchāpatho": "ग़लत रास्ता",
    "micchādiṭṭhi": "ग़लत दृष्टि", "micchattaṃ": "ग़लतपन", "attā": "आत्मा", "atta": "आत्मा",
    "sassato": "शाश्वत", "sarīranti": "शरीर", "maraṇāti": "मृत्यु", "jīvaṃ": "जीव", "aññaṃ": "अलग",
    "hoti": "रहना", "hoti tathāgato": "तथागत रहना",
    # natthi / atthi string (pi-4 ^4-62 / ^4-82)
    "natthi": "व्यर्थ / नहीं", "atthi": "होना", "hutaṃ": "आहुति", "dukkaṭānaṃ": "बुरा", "kammānaṃ": "कर्म",
    "phalaṃ": "फल", "mātā": "माता", "pitā": "पिता", "sattā": "प्राणी", "opapātikā": "स्वतः जन्म लेने वाला",
    "samaṇa": "श्रमण", "brāhmaṇā": "ब्राह्मण", "brāhmaṇānaṃ": "ब्राह्मण", "gatā": "पहुँचा हुआ",
    "paṭipannā": "साधना करने वाला", "abhiññā": "उच्च ज्ञान", "sacchikatvā": "साक्षात्कार करके",
    "pavedentīti": "बताना", "sammā": "सही",
    # sakkāya string
    "assutavā": "अशिक्षित", "puthujjano": "साधारण व्यक्ति", "ariyānaṃ": "आर्य", "dhammassa": "शिक्षा",
    "akovido": "निपुण नहीं", "avinīto": "प्रशिक्षित नहीं", "sappurisānaṃ": "सज्जन", "purisānaṃ": "सज्जन",
    "attato": "आत्मा के रूप में", "samanupassati": "देखना", "rūpavantaṃ": "भौतिक रूप वाला",
    "vedanaṃ": "अनुभूति", "saññaṃ": "पहचान", "saṅkhāre": "मानसिक रचनाएँ", "viññāṇaṃ": "चेतना",
    # sīlabbata, clinging
    "sīla": "सदाचार", "vata": "व्रत", "sīlabbata": "सदाचार और व्रत", "suddhi": "शुद्धि", "bahiddhā": "बाहर",
    "ito": "इस शिक्षा", "vāda": "सिद्धांत", "upādānaṃ": "आसक्ति", "upādānā": "आसक्ति",
    "kāmupādānaṃ": "इंद्रिय-सुखों के प्रति आसक्ति", "kāmupādānena": "इंद्रिय-सुखों के प्रति आसक्ति",
    "diṭṭhupādānaṃ": "दृष्टियों के प्रति आसक्ति", "sīlabbatupādānaṃ": "सदाचार और व्रतों के प्रति आसक्ति",
    "sīlabbatupādānañca": "सदाचार और व्रतों के प्रति आसक्ति", "attavādupādānaṃ": "आत्मा के सिद्धांत के प्रति आसक्ति",
    "sakkāya": "स्थायी आत्मा", "sakkāyadiṭṭhi": "स्थायी आत्मा की ग़लत दृष्टि", "saṃyojanāni": "बंधन",
    "sīlabbataparāmāso": "सदाचार और व्रतों के बारे में ग़लत धारणा",
    # defilements
    "kilesā": "मन के क्लेश", "kileso": "मन का क्लेश", "lobho": "लोभ", "māno": "अहंकार",
    "ahirīkaṃ": "निर्लज्जता", "ahirikaṃ": "निर्लज्जता", "anottappaṃ": "बुराई के प्रति निडरता",
    "hirīyati": "लज्जा आना", "ottappati": "डरना", "ottappitabbena": "डरना चाहिए", "pāpakānaṃ": "बुरा",
    "samāpattiyā": "अपनाना", "akusalānaṃ": "हानिकर", "akusalānaṃ dhammānaṃ": f"हानिकर {P}",
    "saṃkilesikā": "क्लेशों की ओर ले जाने वाला", "saṃkiliṭṭhā": "क्लेशों से मलिन",
    "asaṃkiliṭṭhā": "क्लेशों से मलिन न होने वाला", "kilesavippayuttā": "क्लेशों से अलग",
    "dhammā saṃkiliṭṭhā": f"क्लेशों से मलिन {P}", "dhammā asaṃkiliṭṭhā": f"क्लेशों से मलिन न होने वाली {P}",
    "dhammā saṃkilesikā": f"क्लेशों की ओर ले जाने वाली {P}", "dhammā asaṃkilesikā": f"क्लेशों की ओर न ले जाने वाली {P}",
    "dhammā kilesavippayuttā": f"क्लेशों से अलग {P}",
    "kilesavippayuttā saṃkilesikā": "क्लेशों से अलग पर क्लेशों की ओर ले जाने वाला",
    "ekaṭṭhā": "साथ रहने वाला", "ekaṭṭhā ca kilesā": "साथ रहने वाले मन के क्लेश",
    "samuṭṭhānaṃ": "उत्पन्न", "samuṭṭhānaṃ kāyakammaṃ": "उत्पन्न शारीरिक कर्म", "kāyakammaṃ": "शारीरिक कर्म",
    "vacī": "वाणी", "vacīkammaṃ": "वाणी का कर्म", "manokammaṃ": "मानसिक कर्म",
    "vacīkammaṃ manokammaṃ": "वाणी का कर्म मानसिक कर्म",
    # closing pairs
    "pahātabbā": "छोड़ा जाने वाला", "pahātabba": "छोड़ा जाने वाला", "dassanena": "सत्य-दर्शन",
    "bhāvanāya pahātabbā": "मानसिक अभ्यास से छोड़ा जाने वाला", "bhāvanāya pahātabba": "मानसिक अभ्यास से छोड़ा जाने वाला",
    "hetukā": "मूलों वाला", "pahātabbahetukā": "छोड़ा जाने वाला मूल",
    "dhammā dassanena pahātabbahetukā": f"सत्य-दर्शन से छोड़े जाने वाले मूलों वाली {P}",
    "dhammā bhāvanāya pahātabbahetukā": f"मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली {P}",
    "vitakkā": "आरंभिक विचार", "vicārā": "सतत विचार", "pītikā": "उल्लास वाला", "pīti": "उल्लास",
    "sukha": "सुख", "upekkhā": "समभाव", "sahagatā": "के साथ होने वाला",
    "pītisahagatā": "उल्लास के साथ होने वाला", "sukhasahagatā": "सुख के साथ होने वाला",
    "upekkhāsahagatā": "समभाव के साथ होने वाला",
    "dhammā savitakkā": f"आरंभिक विचार वाली {P}", "dhammā avitakkā": f"आरंभिक विचार से रहित {P}",
    "dhammā savicārā": f"सतत विचार वाली {P}", "dhammā avicārā": f"सतत विचार से रहित {P}",
    "dhammā sappītikā": f"उल्लास वाली {P}", "dhammā appītikā": f"उल्लास से रहित {P}",
    "dhammā pītisahagatā": f"उल्लास के साथ होने वाली {P}", "dhammā na pītisahagatā": f"उल्लास के साथ न होने वाली {P}",
    "dhammā sukhasahagatā": f"सुख के साथ होने वाली {P}", "dhammā na sukhasahagatā": f"सुख के साथ न होने वाली {P}",
    "dhammā upekkhāsahagatā": f"समभाव के साथ होने वाली {P}",
    "dhammā na upekkhāsahagatā": f"समभाव के साथ न होने वाली {P}",
    "pariyantaṃ": "सीमा", "karitvā": "बनाकर", "deve": "देवता", "samāpannassa": "ध्यान-अवस्था में लीन व्यक्ति",
    "upapannassa": "वहाँ जन्मा व्यक्ति", "vihārissa": "रहने वाला", "diṭṭhadhamma": "इसी जीवन",
    "cetasikā": "मन का सहचर", "cittacetasikā": "मन और मन का सहचर", "dhammā pariyāpannā": f"अस्तित्व के लोकों में समाई हुई {P}",
    "dhammā apariyāpannā": f"अस्तित्व के लोकों में न समाई हुई {P}",
    "niyyānikā": "मुक्ति की ओर ले जाने वाला", "dhammā niyyānikā": f"मुक्ति की ओर ले जाने वाली {P}",
    "niyatā": "निश्चित", "dhammā niyatā": f"निश्चित {P}", "kammāni": "कर्म",
    "ānantarikāni": "अगले ही जन्म में निश्चित फल देने वाला",
    "sauttarā": "सर्वोच्च न होने वाला", "dhammā sauttarā": f"सर्वोच्च न होने वाली {P}",
    "anuttarā": "सर्वोच्च", "dhammā anuttarā": f"सर्वोच्च {P}",
    "raṇā": "संघर्ष", "dhammā saraṇā": f"संघर्ष वाली {P}", "dhammā araṇā": f"संघर्ष से रहित {P}",
    # intermediate pairs
    "ārammaṇā": "विषय वाला", "cittā": "मन", "cittañca": "मन", "cittavippayuttā": "मन से अलग",
    "dhammā cittavippayuttā": f"मन से अलग {P}", "sampayuttanti": "जुड़ा", "vattabbaṃ": "कहा" + GAP + "जा सकना",
    "saṃsaṭṭhā": "घुला-मिला", "saṃsaṭṭha": "घुला-मिला", "cittasaṃsaṭṭhā": "मन से घुला-मिला",
    "dhammā cittasaṃsaṭṭhā": f"मन से घुली-मिली {P}", "cittavisaṃsaṭṭhā": "मन से घुला-मिला न होने वाला",
    "dhammā cittavisaṃsaṭṭhā": f"मन से घुली-मिली न होने वाली {P}",
    "samuṭṭhānā": "उत्पन्न", "samuṭṭhāna": "उत्पन्न", "cittasamuṭṭhānā": "मन से उत्पन्न",
    "dhammā cittasamuṭṭhānā": f"मन से उत्पन्न {P}", "dhammā no cittasamuṭṭhānā": f"मन से उत्पन्न न होने वाली {P}",
    "kāyaviññatti": "शरीर द्वारा प्रकट अभिव्यक्ति", "vacīviññatti": "वाणी द्वारा प्रकट अभिव्यक्ति",
    "viññatti": "प्रकट अभिव्यक्ति", "cittajaṃ": "मन से जन्मा", "cittahetukaṃ": "मन के कारण",
    "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र", "saddāyatanaṃ": "ध्वनि का इंद्रिय-क्षेत्र",
    "gandhāyatanaṃ": "गंध का इंद्रिय-क्षेत्र", "rasāyatanaṃ": "स्वाद का इंद्रिय-क्षेत्र",
    "phoṭṭhabbāyatanaṃ": "स्पर्श का इंद्रिय-क्षेत्र", "ākāsa": "आकाश", "ākāsadhātu": "आकाश तत्व",
    "āpo": "जल", "āpodhātu": "जल तत्व", "lahutā": "हल्कापन", "rūpassa lahutā": "भौतिक रूप का हल्कापन",
    "mudutā": "मृदुता", "rūpassa mudutā": "भौतिक रूप की मृदुता", "kammaññatā": "कार्य-योग्यता",
    "rūpassa kammaññatā": "भौतिक रूप की कार्य-योग्यता", "rūpassa upacayo": "भौतिक रूप की वृद्धि",
    "santati": "धारा", "rūpassa santati": "भौतिक रूप की धारा", "kabaḷīkāro": "कौर-कौर खाया जाने वाला",
    "kabaḷīkāro āhāro": "कौर-कौर खाया जाने वाला भोजन", "āhāro": "भोजन",
    "avasesañca": "शेष", "avasesañca rūpaṃ": "शेष भौतिक रूप",
    "cittasahabhuno": "मन के साथ-साथ होने वाला", "sahabhuno": "साथ-साथ होने वाला",
    "dhammā cittasahabhuno": f"मन के साथ-साथ होने वाली {P}", "dhammā no cittasahabhuno": f"मन के साथ-साथ न होने वाली {P}",
    "anuparivattino": "अनुसरण करने वाला", "cittānuparivattino": "मन का अनुसरण करने वाला",
    "dhammā cittānuparivattino": f"मन का अनुसरण करने वाली {P}",
    "dhammā no cittānuparivattino": f"मन का अनुसरण न करने वाली {P}",
    "cittasaṃsaṭṭhasamuṭṭhānā": "मन से घुला-मिला और मन से उत्पन्न",
    "dhammā cittasaṃsaṭṭhasamuṭṭhānā": f"मन से घुली-मिली और मन से उत्पन्न {P}",
    "dhammā no cittasaṃsaṭṭhasamuṭṭhānā": f"{P} मन से घुली-मिली और मन से उत्पन्न नहीं",
    "dhammā cittasaṃsaṭṭhasamuṭṭhānasahabhuno": f"मन से घुली-मिली मन से उत्पन्न और मन के साथ-साथ होने वाली {P}",
    "dhammā no cittasaṃsaṭṭhasamuṭṭhānasahabhuno": f"{P} मन से घुली-मिली मन से उत्पन्न और मन के साथ-साथ होने वाली नहीं",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण करने वाला",
    "dhammā cittasaṃsaṭṭhasamuṭṭhānānuparivattino": f"मन से घुली-मिली मन से उत्पन्न और मन का अनुसरण करने वाली {P}",
    "dhammā no cittasaṃsaṭṭhasamuṭṭhānānuparivattino": f"{P} मन से घुली-मिली मन से उत्पन्न और मन का अनुसरण करने वाली नहीं",
    "kāyāyatanaṃ": "शरीर का इंद्रिय-क्षेत्र", "sotāyatanaṃ": "कान का इंद्रिय-क्षेत्र",
    "ghānāyatanaṃ": "नाक का इंद्रिय-क्षेत्र",
    "cakkhu": "आँख", "cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र", "ajjhattikā": "आंतरिक",
    "dhammā ajjhattikā": f"आंतरिक {P}", "bāhirā": "बाह्य", "dhammā bāhirā": f"बाह्य {P}",
    "upādā": "व्युत्पन्न", "dhammā upādā": f"व्युत्पन्न {P}", "bhūtā": "महाभूत", "mahābhūtā": "महाभूत",
    "cakkhuviññāṇaṃ": "आँख की चेतना", "sotaviññāṇaṃ": "कान की चेतना", "ghānaviññāṇaṃ": "नाक की चेतना",
    "jivhāviññāṇaṃ": "जीभ की चेतना", "kāyaviññāṇaṃ": "शरीर की चेतना", "manodhātu": "मन का तत्व",
    "kammassa katattā": "कर्म किए जाने के कारण", "upādiṇṇā": "कर्म से उत्पन्न",
    "dhammā upādiṇṇā": f"कर्म से उत्पन्न {P}", "dhammā anupādiṇṇā": f"कर्म से उत्पन्न न होने वाली {P}",
    "kiriyā": "क्रिया", "kusalā nākusalā": "न हितकर हैं न हानिकर",
    # headings of 4-02 parts
    "bhāṇa": "पाठ", "vāro": "खंड",
}

# ---------------------------------------------------------------------------- cluster tables
def cluster(term, obl, pron, stem, niya, aniya):
    d = {
        stem: term, f"{stem}vippayuttā": f"{obl} से अलग",
        niya: f"{obl} का विषय बनने वाला",
        f"dhammā {niya}": f"{obl} का विषय बनने वाली {P}",
        f"dhammā {aniya}": f"{obl} का विषय न बनने वाली {P}",
        f"dhammā {stem}vippayuttā": f"{obl} से अलग {P}",
        f"{stem}vippayuttā {niya}": f"{obl} से अलग पर {pron} विषय बनने वाला",
    }
    closing = {niya: f"{pron} विषय बनने वाला", f"dhammā {stem}vippayuttā": f"{obl} से अलग{GAP}{P}"}
    return d, closing


NIV, NIV_C = cluster("बाधा", "बाधाओं", "उनका", "nīvaraṇa", "nīvaraṇiyā", "anīvaraṇiyā")
NIV["nīvaraṇā ceva nīvaraṇiyā"] = "बाधा रूपी भी और बाधाओं का विषय बनने वाला भी"
PAR, PAR_C = cluster("ग़लत धारणा", "ग़लत धारणा", "उसका", "parāmāsa", "parāmaṭṭhā", "aparāmaṭṭhā")
UPA, UPA_C = cluster("आसक्ति", "आसक्ति", "उसका", "upādāna", "upādāniyā", "anupādāniyā")
UPA["upādānā ceva upādāniyā"] = "आसक्ति रूपी भी और आसक्ति का विषय बनने वाला भी"
UPA["upādānāni"] = "आसक्ति"
UPA["upādānañceva"] = "आसक्ति"

CLUSTERS = [  # (first id, last id, table, closing ids)
    (1169, 1179, NIV, {1178, 1179}), (1182, 1190, PAR, {1189, 1190}), (1224, 1234, UPA, {1233, 1234}),
]
CLOSING = {1178: NIV_C, 1179: NIV_C, 1189: PAR_C, 1190: PAR_C, 1233: UPA_C, 1234: UPA_C,
           1259: {"dhammā kilesavippayuttā": f"क्लेशों से अलग{GAP}{P}"},
           1260: {"dhammā kilesavippayuttā": f"क्लेशों से अलग{GAP}{P}"}}

# ---------------------------------------------------------------------------- per-segment overrides
SEG_TEXT = """
1-3-2-10-0 | dukaṃ=दो-दो के वर्गीकरण
1-3-2-12-0 | Kilesa=मन के क्लेश
1-1156 | dhammā oghavippayuttā=बाढ़ों से अलग … परिघटना | oghaniyā=उनका विषय बनने वाला
1-1157 | dhammā yogavippayuttā=जकड़नों से अलग … परिघटना | yoganiyā=उनका विषय बनने वाला
1-1159 | vuccati kāmacchandanīvaraṇaṃ=इंद्रिय-सुखों की चाह की बाधा कहा जाता है
1-1160 | mano=मन
1-1163 | kāyassa=मानसिक काया
1-1166 | mano=मन | cetaso=मन | vilekho=कुरेदना
1-1167 | mano=मन | patho=दोराहा | vilekho=खरोंच | gāho=पकड़ना
1-1168 | ogho=बाढ़
1-1174 | nīvaraṇāni=बाधा
1-1180 | Diṭṭhi=दृष्टि
1-1187 | parāmaṭṭhā=ग़लत धारणा का विषय बनने वाला
1-1191 | Vedanā=अनुभूति
1-1192 | ārammaṇā=विषय
1-1193 | mano=मन
1-1198 | citta=मन
1-1201 | kāya=शरीर
1-1203 | kāya=शरीर
1-1205 | kāya=शरीर
1-1213 | mano=मन | manāyatanaṃ=मन का इंद्रिय-क्षेत्र
1-1219 | kāma=इंद्रिय-सुख | diṭṭhi=दृष्टि
1-1221 | Ṭhapetvā=छोड़कर | upādānaṃ=आसक्ति
1-1223 | upādānā=आसक्ति
1-1231 | Diṭṭhupādānaṃ=दृष्टियों के प्रति आसक्ति | kāmupādānaṃ diṭṭhupādānena=इंद्रिय-सुखों के प्रति आसक्ति दृष्टियों के प्रति आसक्ति के साथ | Diṭṭhi=दृष्टि
1-1235 | vatthūni=आधार | kilesa=मन के क्लेश | Dasa=दस
1-1239 | ketu=झंडा | maññitattaṃ=मान चुका होना | maññanā=मान लेना | sadiso=बराबर | dhajo=झंडा | ketukamyatā=झंडा फहराने की इच्छा | unnamo=अकड़ | hīno=हीन | unnati=ऊँचा उठना | sampaggāho=स्वयं को ऊपर उठाना | kamyatā=इच्छा
1-1241 | mano=मन | patho=दोराहा | vilekho=खरोंच | gāho=पकड़ना
1-1245 | kilesā=मन के क्लेश
1-1257 | uddhaccaṃ anottappena=बेचैनी बुराई के प्रति निडरता के साथ | uddhaccaṃ ahirikena=बेचैनी निर्लज्जता के साथ | ahirikaṃ anottappena=निर्लज्जता बुराई के प्रति निडरता के साथ | ahirikaṃ uddhaccena=निर्लज्जता बेचैनी के साथ | anottappaṃ uddhaccena=बुराई के प्रति निडरता बेचैनी के साथ | anottappaṃ ahirikena=बुराई के प्रति निडरता निर्लज्जता के साथ
1-1263 | mano=मन | vilekho=खरोंच
1-1266 | Avaseso=शेष
1-1270 | mano=मन | vilekho=खरोंच
1-1272 | hetukā=मूल
1-1273 | Avaseso=शेष
1-1274 | hetukā=मूल
1-1276 | vitakkā=आरंभिक विचार
1-1280 | pītikā=उल्लास
1-1287 | nimmita=रचा गया | para=दूसरा | vasavattī=अधिकार रखने वाला | avicinirayaṃ=अवीचि नरक | āyatanā=इंद्रिय-क्षेत्र | viññāṇaṃ=चेतना
1-1289 | brahma=ब्रह्मलोक | yaṃ=(no direct equivalent)
1-1291 | ānañcāyatana=अनंत आकाश का क्षेत्र | ānañca=अनंत | asaññā=अ-पहचान | yaṃ=(no direct equivalent)
1-1294 | Maggā=मार्ग
1-1302 | raṇā=संघर्ष | Kusala=हितकर
"""

SEG_TEXT_403 = """
1-3-3-0 | Suttantika=उपदेश | duka=दो-दो के वर्गीकरण | nikkhepaṃ=सारांश
1-1303 | vijjā=विद्या | dhammā vijjābhāgino=विद्या की भागी परिघटना
1-1304 | avijjā=अज्ञान | dhammā avijjābhāgino=अज्ञान की भागी परिघटना
1-1305 | vijju=बिजली | upamā=जैसा | ariya=आर्य | maggesu=मार्ग | dhammā vijjūpamā=बिजली जैसी परिघटना | paññā=प्रज्ञा
1-1306 | arahatta=अर्हत्-पद | vajira=वज्र | Upariṭṭhime=सबसे ऊपर का | upamā=जैसा | magge=मार्ग | paññā=प्रज्ञा
1-1307 | anottappañca=बुराई के प्रति निडरता | bālā=मूर्खतापूर्ण | dhammā bālā=मूर्खतापूर्ण परिघटना | Ahirīkañca=निर्लज्जता
1-1308 | ottappañca=बुराई का डर | Hirī=लज्जा | paṇḍitā=बुद्धिमत्तापूर्ण | dhammā paṇḍitā=बुद्धिमत्तापूर्ण परिघटना
1-1309 | kaṇhā=काला | dhammā kaṇhā=काली परिघटना | anottappañca=बुराई के प्रति निडरता | Ahirīkañca=निर्लज्जता
1-1310 | sukkā=उजला | dhammā sukkā=उजली परिघटना | ottappañca=बुराई का डर | Hirī=लज्जा
1-1311 | Kāya=शरीर | tapanīyā=संताप देने वाला | mano=मन | duccaritaṃ=दुराचरण | vacī=वाणी
1-1312 | Kāya=शरीर | tapanīyā=संताप देने वाला | caritaṃ=सदाचरण | mano=मन | dhammā atapanīyā=संताप न देने वाली परिघटना | vacī=वाणी
1-1313 | nāmadheyyaṃ=अभिधान | paññatti=नामकरण | nirutti=अभिव्यक्ति | samaññā=संज्ञा | adhivacanā=नाम | nāmakammaṃ=नाम देना | pathā=मार्ग | saṅkhā=गणना | dhammā adhivacanapathā=परिघटना … नाम के मार्ग रूपी | vohāro=व्यवहार | abhilāpo=उच्चारण
1-1314 | nāmadheyyaṃ=अभिधान | paññatti=नामकरण | nirutti=अभिव्यक्ति | samaññā=संज्ञा | nāmakammaṃ=नाम देना | pathā=मार्ग | saṅkhā=गणना | dhammā niruttipathā=परिघटना … अभिव्यक्ति के मार्ग रूपी | vohāro=व्यवहार | abhilāpo=उच्चारण
1-1315 | nāmadheyyaṃ=अभिधान | paññatti=नामकरण | nirutti=अभिव्यक्ति | samaññā=संज्ञा | nāmakammaṃ=नाम देना | pathā=मार्ग | saṅkhā=गणना | dhammā paññattipathā=परिघटना … नामकरण के मार्ग रूपी | vohāro=व्यवहार | abhilāpo=उच्चारण
1-1316 | nāmaṃ=मानसिक पक्ष | Vedanā=अनुभूति
1-1317 | upādāya=व्युत्पन्न | upādāya rūpaṃ=व्युत्पन्न भौतिक रूप
1-1319 | bhava=अस्तित्व
1-1320 | bhava=अस्तित्व | Bhavissati=रहना
1-1321 | bhavissati=रहना | vibhava=अनस्तित्व
1-1322 | sassata=शाश्वतता
1-1323 | Ucchijjissati=विनाश हो जाना | uccheda=विनाश
1-1326 | uppajjati=उत्पन्न होना | anudiṭṭhi=के बारे में दृष्टि | ārabbha=विषय बनाना | uppajjati diṭṭhi=दृष्टि उत्पन्न होना
1-1327 | uppajjati=उत्पन्न होना | anudiṭṭhi=के बारे में दृष्टि | ārabbha=विषय बनाना | uppajjati diṭṭhi=दृष्टि उत्पन्न होना
1-1330 | hirī=लज्जा
1-1331 | ottappaṃ=बुराई का डर
1-1332 | Sahadhammike=शिक्षा के अनुसार | vacassatā=सलाह मानने की प्रवृत्ति | paṭissavatā=बात पर कान देना | sātatā=रस लेना | anādariyaṃ=अनादर | anādaratā=अनादर का भाव | agāravatā=अगौरव | dovacassatā=सलाह न मानने की प्रवृत्ति | dovacassāyaṃ=सलाह न मानना | appaṭissavatā=बात पर कान न देना | vipaccanīka=विरोध | vippaṭikūla=उलटा | vuccamāne=कहा जाना | gāhitā=पकड़ना | dovacassiyaṃ=सलाह न मानने का भाव
1-1333 | sevanā=संगति | pāpa=बुरा | sambhajanā=घनिष्ठ मेल-जोल | bhatti=लगाव | saddhā=श्रद्धा | nisevanā=लगातार संगति | mittatā=मित्रों की संगति | dussīlā=दुराचारी | saṃsevanā=घनिष्ठ संगति | sampavaṅkatā=झुकाव | sutā=सुना-सीखा | puggalā=व्यक्ति | bhajanā=मेल-जोल | maccharino=कंजूस | duppaññā=प्रज्ञाहीन
1-1334 | Sahadhammike=शिक्षा के अनुसार | sovacassiyaṃ=सलाह मानने का भाव | vacassatā=सलाह मानने की प्रवृत्ति | sappaṭissavatā=बात पर कान देना | sātatā=रस लेना | sovacassatā=सलाह मानने की प्रवृत्ति | vipaccanīka=विरोध | paṭikūla=उलटा | sādariyaṃ=आदर | sādaratā=आदर का भाव | sagāravatā=गौरव | vuccamāne=कहा जाना | gāhitā=पकड़ना | sovacassāyaṃ=सलाह मानना
1-1335 | sevanā=संगति | sambhajanā=घनिष्ठ मेल-जोल | bhatti=लगाव | saddhā=श्रद्धावान | nisevanā=लगातार संगति | mittatā=मित्रों की संगति | cāgavanto=उदार | saṃsevanā=घनिष्ठ संगति | sampavaṅkatā=झुकाव | sutā=सुना-सीखा | sīlavanto=सदाचारी | puggalā=व्यक्ति | bhajanā=मेल-जोल | paññavanto=प्रज्ञावान
1-1336 | khandhā=श्रेणी | āpatti=दोष | kusalatā=कुशलता
1-1337 | vuṭṭhāna=उबरना | āpatti=दोष | kusalatā=कुशलता | vuṭṭhānakusalatā=उबरने में कुशलता
1-1338 | vitakka=आरंभिक विचार | samāpatti=ध्यान-अवस्था | kusalatā=कुशलता | vicārā=सतत विचार
1-1339 | samāpatti=ध्यान-अवस्था | vuṭṭhāna=बाहर आना | kusalatā=कुशलता | vuṭṭhānakusalatā=बाहर आने में कुशलता
1-1340 | Aṭṭhārasa=अठारह | kusalatā=कुशलता
1-1341 | manasikāra=मनोयोग | dhātūnaṃ=तत्व | kusalatā=कुशलता | manasikārakusalatā=मनोयोग के विषय में कुशलता
1-1342 | āyatana=इंद्रिय-क्षेत्र | Dvādasa=बारह | kusalatā=कुशलता
1-1343 | jarā=बुढ़ापा | samudayo=उत्पत्ति | āyatanaṃ=इंद्रिय-क्षेत्र | jāti=जन्म | upādānaṃ=आसक्ति | paccayā=कारण | viññāṇaṃ=चेतना | phasso=संपर्क | maraṇaṃ=मृत्यु | paṭicca=परस्पर-आश्रित | upāyāsā=निराशा | bhavo=अस्तित्व | rūpaṃ=भौतिक रूप | saṅkhārā=मानसिक रचनाएँ | Avijjā=अज्ञान | parideva=विलाप | khandhassa=पुंज | nāma=मानसिक पक्ष | samuppāda=उत्पत्ति | dukkha=दुःख | domanassa=उदासी | kusalatā=कुशलता | soka=शोक | kevalassa=पूरा
1-1344 | uppādāya=उत्पत्ति | hetū=मूल | kusalatā=कुशलता
1-1345 | uppādāya=उत्पत्ति | aṭṭhāna=असंभव बात | hetū=मूल | kusalatā=कुशलता
1-1346 | vaṅkatā=वक्रता | jimhatā=टेढ़ापन | ajimhatā=टेढ़ेपन का अभाव | avaṅkatā=वक्रता का अभाव | akuṭilatā=कुटिलता का अभाव | ajjavo=सरलता | kuṭilatā=कुटिलता
1-1347 | akakkhaḷatā=कठोरता का अभाव | akathinatā=कड़ेपन का अभाव | kakkhaḷatā=कठोरता | nīca=विनम्रता | maddavo=कोमलता | cittatā=मन | mudutā=मृदुता | kathinatā=कड़ापन | maddavatā=कोमलता
1-1348 | attamanatā=खिल उठना | adhivāsanatā=सह लेना | khamanatā=क्षमा करना | cittassa=मन | anasuropo=कटु वचन का अभाव | acaṇḍikkaṃ=उग्रता का अभाव | khanti=सहनशीलता
1-1349 | kāyiko=शरीर | soraccaṃ=सौम्यता | avītikkamo=उल्लंघन न करना | saṃvaro=संयम | vācasiko=वाणी | Yo=(no direct equivalent)
1-1350 | kodha=क्रोध | neḷā=निर्दोष | sāmantā=निकट | samādhi=एकाग्रता | saṃvattanikā=की ओर ले जाने वाला | sakhila=मधुरता | sākhalyaṃ=मधुर व्यवहार | kaṇṇa=कान | gamā=छूने वाला | kakkasā=कठोर | hadaya=हृदय | kaṭukā=कड़वा लगने वाला | tathārūpiṃ=वैसा | kantā=प्रिय | pemanīyā=प्रेमपूर्ण | apharusa=कठोर न होना | abhisajjanī=चुभने वाला | para=दूसरा | sukhā=सुख | manāpā=मनभावन | porī=शिष्ट | aṇḍakā=रूखा | saṇha=कोमलता | bhāsitā hoti=बोलने वाला होना | vācā=वाणी
1-1351 | paṭisanthārako=आदर-सत्कार करने वाला | paṭisanthāro=आदर-सत्कार | paṭisanthārā=आदर-सत्कार | āmisa=भौतिक वस्तु | ekacco=कोई | dhamma=शिक्षा
1-1352 | pāpakā=बुरा | kāyena=शरीर | viññāya=जानकर | abhijjhā=लालच | dvāratā=द्वार | Sotena=कान | cakkhunā=आँख | indriyānaṃ=इंद्रिय | indriyaṃ=इंद्रिय | manindriyaṃ=मन की इंद्रिय | nimitta=समग्र छवि | anvāssaveyyuṃ=घुस आ सकना | rūpaṃ=दृश्य रूप | gāhī=पकड़ लेना | rakkhati=रक्षा करना | gutta=रक्षा करना | sutvā=सुनकर | viharantaṃ=रहना | dhammaṃ=मन का विषय | manasā=मन | agutti=रक्षा न करना | agopanā=न सँभालना | asaṃvaro=संयम न रखना | anārakkho=चौकसी न करना | ghānena=नाक | paṭipajjati=प्रयत्न … करना | saṃvarāya=संयम | domanassā=उदासी | disvā=देखकर | indriyesu=इंद्रिय | gandhaṃ=गंध | ghāyitvā=सूँघकर | ekacco=कोई | saddaṃ=ध्वनि | abhijjhādomanassā=लालच और उदासी | rasaṃ=स्वाद | sāyitvā=चखकर | jivhāya=जीभ | phoṭṭhabbaṃ=स्पर्श | phusitvā=अनुभव करके | āpajjati=रखना | asaṃvutaṃ=असंयमित | Yā=(no direct equivalent)
1-1353 | maṇḍanāya=शरीर सुडौल बनाना | davāya=मौज | vibhūsanāya=सुंदर दिखना | santuṭṭhitā=संतोष | bhojane=भोजन | āhāraṃ=भोजन | madāya=मद | mattaññutā=मात्रा का ज्ञान | appaṭisaṅkhā=बिना सोचे-विचारे | paṭisaṅkhā=सोच-विचार | ekacco=कोई | āhāreti=भोजन करना | ayoniso=अनुचित ढंग से
1-1354 | pāpakā=बुरा | kāyena=शरीर | viññāya=जानकर | abhijjhā=लालच | dvāratā=द्वार | Sotena=कान | cakkhunā=आँख | indriyānaṃ=इंद्रिय | indriyaṃ=इंद्रिय | manindriyaṃ=मन की इंद्रिय | nimitta=समग्र छवि | anvāssaveyyuṃ=घुस आ सकना | rūpaṃ=दृश्य रूप | gāhī=पकड़ना | gutta=रक्षा करना | rakkhati=रक्षा करना | sutvā=सुनकर | viharantaṃ=रहना | dhammaṃ=मन का विषय | manasā=मन | ghānena=नाक | paṭipajjati=प्रयत्न करना | gopanā=सँभालना | saṃvarāya=संयम | domanassā=उदासी | disvā=देखकर | indriyesu=इंद्रिय | gandhaṃ=गंध | ghāyitvā=सूँघकर | ekacco=कोई | saddaṃ=ध्वनि | abhijjhādomanassā=लालच और उदासी | rasaṃ=स्वाद | sāyitvā=चखकर | jivhāya=जीभ | phoṭṭhabbaṃ=स्पर्श | phusitvā=अनुभव करके | āpajjati=रखना | asaṃvutaṃ=असंयमित | ārakkho=चौकसी करना | Yā=(no direct equivalent)
1-1355 | maṇḍanāya=शरीर सुडौल बनाना | davāya=मौज | anuggahāya=सहायता | vibhūsanāya=सुंदर दिखना | anavajjatā=निर्दोषता | kāyassa=शरीर | santuṭṭhitā=संतोष | vihiṃsā=कष्ट | phāsu=सुख | bhojane=भोजन | vedanaṃ=अनुभूति | āhāraṃ=भोजन | brahmacariya=पवित्र जीवन | madāya=मद | mattaññutā=मात्रा का ज्ञान | yātrā=जीवन-निर्वाह | vihāro=रहना | yāpanāya=चलाए रखना | purāṇañca=पुराना | paṭisaṅkhā=सोच-विचार | ekacco=कोई | āhāreti=भोजन करना | cāti=(no direct equivalent) | yoniso=उचित ढंग से
1-1356 | muṭṭhasaccaṃ=सजगता की कमी | sammusanatā=भूल जाना | asati=सजगता का अभाव | ananussati=बार-बार स्मरण का अभाव | appaṭissati=पुनः स्मरण का अभाव
1-1358 | sammusanatā=भूल जाना | indriyaṃ=क्षमता
1-1360 | paṭisaṅkhāna=सोच-विचार
1-1361 | bojjhaṅgā=जागृति के … अंग | āsevanā=निरंतर सेवन | bahulīkammaṃ=बार-बार करना
1-1364 | samatha=शांति | nimittaṃ=चिह्न
1-1365 | paggāha=तत्परता | nimittaṃ=चिह्न
1-1368 | kāyiko=शरीर | vipatti=विफलता | dussilyaṃ=दुराचार | vācasiko=वाणी | vītikkamo=उल्लंघन | Yo=(no direct equivalent)
1-1369 | vipatti=विफलता
1-1370 | sampadā=संपन्नता | kāyiko=शरीर | avītikkamo=उल्लंघन न करना | saṃvaro=संयम | vācasiko=वाणी | Yo=(no direct equivalent)
1-1371 | sampadā=संपन्नता
1-1372 | kāyiko=शरीर | avītikkamo=उल्लंघन न करना | visuddhi=शुद्धि | saṃvaro=संयम | vācasiko=वाणी | Yo=(no direct equivalent)
1-1373 | anulomika=अनुरूप | ñāṇaṃ=ज्ञान | Kammassakata=कर्म ही अपनी संपत्ति | samaṅgissa=से युक्त व्यक्ति | visuddhi=शुद्धि | sacca=सत्य
1-1374 | Diṭṭhi=दृष्टि | visuddhi=शुद्धि
1-1375 | padhānanti=प्रयास | Yathā=के अनुरूप | diṭṭhissa=दृष्टि
1-1376 | jarā=बुढ़ापा | jāti=जन्म | maraṇa=मृत्यु | bhayaṃ=भय | Saṃvego=मन का झकझोरा जाना | byādhi=रोग | Saṃvejaniyaṃ=झकझोर देने वाला | ṭhānanti=बात
1-1377 | pahānāya=छोड़ना | vepullāya=विपुलता | uppannānaṃ=उत्पन्न | uppādāya=उत्पन्न करना | ārabhati=जगाना | bhikkhu=भिक्षु | ṭhitiyā=स्थिरता | chandaṃ=चाह | padhānanti=प्रयास | vāyamati=प्रयास करना | paggaṇhāti=तत्पर करना | cittaṃ paggaṇhāti=मन को तत्पर करना | pāripūriyā=परिपूर्णता | janeti=जगाना | cittaṃ=मन | cittaṃ paggaṇhāti padahati=मन को तत्पर करना … पूरा ज़ोर लगाना | anuppādāya=उत्पन्न न होने देना | asammosāya=लुप्त न होना | Saṃviggassa=झकझोरा गया व्यक्ति | padahati=पूरा ज़ोर लगाना | yoniso=उचित ढंग से
1-1378 | santuṭṭhitā=संतुष्ट होना | kusalesu=हितकर | kusalesu dhammesūti=हितकर परिघटना | kamyatā=चाह
1-1379 | kiriyatā=करना | dhuratā=भार | sakkacca=सावधानी से | chandatā=चाह | padhānasminti=प्रयास | sātacca=लगातार | āsevanā=निरंतर सेवन | nikkhitta=छोड़ना | bahulīkammaṃ=बार-बार करना | olīna=ढीला पड़ना | ṭhita=रुकना
1-1380 | cuti=मरना | sattānaṃ=प्राणी | khaye=क्षय | vijjā=विद्या | Vijjā=विद्या | ñāṇaṃ=ज्ञान | nivāsa=पूर्व जन्म | upapāte=जन्म लेना | anussati=स्मरण | āsavānaṃ=मन के मैल
1-1381 | vimuttiyo=मुक्ति | Vimuttīti=मुक्ति | cittassa=मन | adhimutti=छुटकारा
1-1382 | Khaye=क्षय | ñāṇanti=ज्ञान | samaṅgissa=से युक्त व्यक्ति
1-1383 | kaṇḍaṃ=अध्याय | niṭṭhitaṃ=पूरा हुआ | ñāṇanti=ज्ञान | Anuppāde=उत्पन्न न होना | samaṅgissa=से युक्त व्यक्ति | Nikkhepa=सारांश
"""

# lobha string (1-1236): Pāli items in order ↔ the Hindi list of the translation, keyword -> value
LOBHA = """
anurodho=अनुकूल होना | āyūhinī=जुटाने वाली | jappanā=तड़पना | sineho=स्नेह | ejā=हलचल | paṇidhi=आकांक्षा |
saṅgo=लगाव | janikā=जन्म देने वाली | bandhanaṃ=बेड़ी | nirodha=समाप्ति | putta=संतान | upādānaṃ=आसक्ति |
dutiyā=साथिन | anunayo=झुकाव | apekkhā=अपेक्षा | netti=डोर | bhava=अस्तित्व | upakkileso=मलिनता |
chādanaṃ=पर्दा | abhijjhā=लालच | taṇhā=तृष्णा | latā=लता | māyā=कपट | nandī=आनंद | nikāmanā=गहरी कामना |
visayo=क्षेत्र | gedho=लालसा | sampatthanā=प्रबल कामना | visattikā=फँसाने वाली | pihanā=ललक |
abhijappā=अत्यधिक तड़प | pucchañjikatā=चापलूसी | sādhu=बढ़िया चीज़ | rūpa=दृश्य रूप | ogho=बाढ़ | vanaṃ=वन |
lobho=लोभ | jappā=तड़प | nīvaraṇaṃ=बाधा | baḷisaṃ=काँटा | āsā=आशा | āsisanā=आशा करना | arūpa=अभौतिक |
mucchā=मूर्छा | paligedho=गहरी लालसा | pajappā=गहरी तड़प | santhavo=घनिष्ठता | paṭibandhu=नाता |
visama=अनुचित | gaddulaṃ=पट्टा | jīvita=जीवन | nikanti=रुचि | patthanā=कामना | rāgo=राग |
vevicchaṃ=लोभीपन | dhamma=मन का विषय | cittassa=मन | paṅko=कीचड़ | jālinī=जाल बुनने वाली |
vibhava=अनस्तित्व | pariyuṭṭhānaṃ=आवेश | āvaraṇaṃ=आवरण | samuddo=सागर | pabhavo=उद्गम |
sārāgo=प्रबल राग | sañjananī=उत्पन्न करने वाली | nadī=नदी | mūlaṃ=मूल | sibbinī=सिलने वाली |
kāma=इंद्रिय-सुख | gandha=गंध | pāso=फंदा | sadda=ध्वनि | nidānaṃ=स्रोत | visaṭā=फैली हुई | saritā=धारा |
dukkha=दुःख | rasa=स्वाद | anusayo=सुप्त प्रवृत्ति | suttaṃ=धागा | gantho=गाँठ | phoṭṭhabba=स्पर्श |
vanatho=झाड़-झंखाड़ | adhamma=अनैतिक | loluppāyanā=लोलुप होना | loluppaṃ=लोलुपता | icchā=इच्छा |
dhana=धन | kamyatā=चाह | yogo=जकड़न
"""


def parse(block):
    m = {}
    for line in block.strip().splitlines():
        bid, *pairs = [x.strip() for x in line.split(" | ")]
        d = m.setdefault(bid, {})
        for p in pairs:
            k, v = p.split("=", 1)
            d[k] = v
    return m


SEG = parse(SEG_TEXT)
SEG.update(parse(SEG_TEXT_403))
SEG["1-1236"] = {k.strip(): v.strip() for k, v in (p.split("=", 1) for p in
                 " ".join(LOBHA.split()).replace(" |  ", " | ").split(" | ") if p.strip())}

# names used by "vuccati X"
NAMES = {
    "sassatadiṭṭhi": "शाश्वतता की दृष्टि", "ucchedadiṭṭhi": "विनाश की दृष्टि",
    "bhavadiṭṭhi": "अस्तित्व की दृष्टि", "vibhavadiṭṭhi": "अनस्तित्व की दृष्टि",
    "antavā diṭṭhi": "सीमित होने की दृष्टि", "anantavā diṭṭhi": "असीम होने की दृष्टि",
    "pubbantānudiṭṭhi": "अतीत के बारे में दृष्टि", "aparantānudiṭṭhi": "भविष्य के बारे में दृष्टि",
    "āpattikusalatā": "दोषों के विषय में कुशलता", "āpattivuṭṭhānakusalatā": "दोषों से उबरने में कुशलता",
    "samāpattikusalatā": "ध्यान-अवस्थाओं के विषय में कुशलता",
    "samāpattivuṭṭhānakusalatā": "ध्यान-अवस्थाओं से बाहर आने में कुशलता",
    "dhātukusalatā": "तत्वों के विषय में कुशलता", "manasikārakusalatā": "मनोयोग के विषय में कुशलता",
    "āyatanakusalatā": "इंद्रिय-क्षेत्रों के विषय में कुशलता",
    "paṭiccasamuppādakusalatā": "परस्पर-आश्रित उत्पत्ति के विषय में कुशलता",
    "ṭhānakusalatā": "संभव बातों के विषय में कुशलता", "aṭṭhānakusalatā": "असंभव बातों के विषय में कुशलता",
}
SENSE = {  # sense-base stems (dhātukusalatā / āyatanakusalatā lists)
    "cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर", "mano": "मन",
    "rūpa": "दृश्य रूप", "sadda": "ध्वनि", "gandha": "गंध", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श",
    "dhamma": "मन के विषय",
}


def sense_compound(k):
    for stem, hi in sorted(SENSE.items(), key=lambda x: -len(x[0])):
        if not k.startswith(stem):
            continue
        rest = k[len(stem):]
        if rest == "dhātu":
            return f"{hi} का तत्व" if stem != "dhamma" else "मन के विषयों का तत्व"
        if rest == "viññāṇa":
            return f"{hi} की चेतना"
        if rest == "viññāṇadhātu":
            return f"{hi} की चेतना का तत्व"
        if rest in ("āyatanaṃ", "yatanaṃ"):
            return f"{hi} का इंद्रिय-क्षेत्र" if stem != "dhamma" else "मन के विषयों का इंद्रिय-क्षेत्र"
    if k in ("cakkhāyatanaṃ", "manāyatanaṃ"):
        return {"cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र", "manāyatanaṃ": "मन का इंद्रिय-क्षेत्र"}[k]
    return None


def num(bid):
    try:
        return int(bid.split("-")[1])
    except (IndexError, ValueError):
        return 0


def resolver(bid, kw, kws):
    k = lc(kw)
    s = set(lc(x) for x in kws)
    seg = SEG.get(bid, {})
    if kw in seg:
        return seg[kw]
    if k in seg:
        return seg[k]
    n = num(bid) if bid.count("-") == 1 else 0
    if n in CLOSING and k in CLOSING[n]:
        return CLOSING[n][k]
    for a, b, table, _ in CLUSTERS:
        if a <= n <= b and k in table:
            return table[k]
    if k.startswith("vuccati "):
        rest = k[len("vuccati "):]
        return (NAMES[rest] if rest in NAMES else resolver(bid, rest, kws)) + " कहा जाता है"
    if k in NAMES:
        return NAMES[k]
    # context rules
    if k == "rūpa":
        if any(x.startswith("rūpāvacar") for x in s):
            return "सूक्ष्म भौतिक"
        if s & {"rūpāyatanaṃ", "rūpadhātu"}:
            return "दृश्य रूप"
        return "भौतिक रूप"
    if k == "dhamma":
        return "मन के विषय"
    if k == "mano":
        return "मानसिक" if "manokammaṃ" in s else "मन"
    if k == "kāya":
        return "शारीरिक" if "kāyakammaṃ" in s else "शरीर"
    sc = sense_compound(k)
    if sc:
        return sc
    if k in SENSE:
        return SENSE[k]
    if k in BASE:
        return BASE[k]
    return CH2[k]


if __name__ == "__main__":
    for part in ("4-02-nikkhepakandam", "4-03-nikkhepakandam"):
        build_part(part, resolver)
        verify(part, show=200)
