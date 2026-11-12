"""pi-2 Pāli->Hindi keyword maps for 5-indriyavibhango, 16-nanavibhango, 18-dhammahadayavibhango.

Builds on map_sample_hi.py (imported read-only): OVR[bid][kw] first, then pi2_value with {**PI2, **T}.
usage: python -I -X utf8 map_16_18_5_hi.py [chapter ...]   (imported by draft_16_18_5_hi.py without side effects)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI2, KH_T, PP_SEGMENTS, pi2_value, build_part, verify, read_hindi, present, NDE  # noqa: E402

# ---------------------------------------------------------------------------- shared by the three chapters
NUM = {"eka": "एक", "dv": "दो", "dvi": "दो", "ti": "तीन", "tīṇ": "तीन", "cattār": "चार", "pañc": "पाँच", "cha": "छह",
       "satt": "सात", "aṭṭh": "आठ", "nav": "नौ", "das": "दस", "ekādas": "ग्यारह", "dvādas": "बारह",
       "teras": "तेरह", "cuddas": "चौदह", "pannaras": "पंद्रह", "soḷas": "सोलह", "sattaras": "सत्रह",
       "aṭṭhāras": "अठारह", "ekavīsat": "इक्कीस", "bāvīsat": "बाईस"}
COMMON = {**KH_T,
          "sammā": "सही",                  # sammādiṭṭhi / sammāsati … (PI2 «पूर्ण रूप से» is the homage only)
          }

# ============================================================================ 5-indriyavibhango
# numeral + indriyā (Dasindriyā «दस क्षमताएँ») = numeral + singular noun (pi-3 Dvādasāyatanāni = बारह इंद्रिय-क्षेत्र)
T5 = {**COMMON}
for _n, _h in NUM.items():
    T5[_n + "indriyā"] = f"{_h} क्षमता"
T5.update({
    "no": "नहीं",                                    # «No āsavā» = «मन के मैल रूपी नहीं हैं»
    "bāvīsatindriyāni": "बाईस क्षमता", "bāvīsatīnaṃ": "बाईस", "indriyānaṃ": "क्षमता",
    "bāvīsatīnaṃ indriyānaṃ": "बाईस क्षमता", "indriyā": "क्षमता",
    "indriyā siyā": "क्षमता कभी", "indriyā hetū": "क्षमता मूल", "indriyā sappaṭighā": "क्षमता टकराव वाला",
    "aññindriyaṃ": "पूर्ण ज्ञान की क्षमता", "aññātāvindriyaṃ": "पूर्ण ज्ञान पा चुके की क्षमता",
    "anaññātaññassāmītindriyaṃ": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
    # Abhidhammabhājanīya definitions (2-220): pi-1 Rūpakaṇḍa / cittuppāda strings
    "cakkhu": "आँख", "kāyo": "शरीर", "bhūtānaṃ": "महाभूत", "mahābhūtānaṃ": "महाभूत",
    "pasādo": "संवेदनशीलता", "upādāya pasādo": "व्युत्पन्न संवेदनशीलता", "suñño": "सूना", "gāmopeso": "गाँव",
    "phassasampayuttaṃ": "संपर्क से जुड़ा",
    "itthi": "स्त्री", "itthiyā": "स्त्री", "liṅgaṃ": "आकृति", "nimittaṃ": "चिह्न", "ākappo": "ढंग",
    "itthattaṃ": "स्त्री होना", "purisassa": "पुरुष", "purisa": "पुरुष", "purisattaṃ": "पुरुष होना",
    "rūpajīvitindriyaṃ": "भौतिक जीवन-क्षमता", "arūpajīvitindriyaṃ": "अभौतिक जीवन-क्षमता",
    "rūpīnaṃ": "भौतिक", "jīvitaṃ": "जीवन",
    "kāyikaṃ": "शारीरिक", "kāyasamphassajaṃ": "शरीर के संपर्क से उत्पन्न", "cetosamphassa": "मन का संपर्क",
    "cetasikaṃ asātaṃ": "मानसिक असुहावनापन", "cetasikaṃ dukkhaṃ": "मानसिक दुःख",
    "dukkhaṃ": "दुःख", "dukkhaṃ vedayitaṃ": "दुःखद अनुभव",
    "asithilaparakkamatā": "ढीला न पड़ने वाला प्रयत्न", "anikkhitta": "न छोड़ना", "chanda": "चाह", "dhura": "भार",
    "apilāpanatā": "उथला न होना", "asammussanatā": "भूल न जाना",
    "sambojjhaṅgo": "जागृति का अंग", "dhammavicayasambojjhaṅgo": "परिघटनाओं की छानबीन नामक जागृति का अंग",
    "aṅgaṃ": "अंग", "maggaṅgaṃ": "मार्ग का अंग",
    "ñātānaṃ": "जाना जा चुका", "viditānaṃ": "समझा जा चुका", "sacchikatānaṃ": "प्रत्यक्ष अनुभव किया जा चुका",
    "sacchikiriyāya": "साक्षात्कार",
    # Pañhāpucchaka (2-223, 2-224)
    "pahātabbā": "छोड़ा जाने वाला", "pītisahagatā": "उल्लास के साथ होने वाला",
    "saṃkilesikā": "क्लेशों का विषय बनने वाला", "vattabbaṃ": "कहा जा सकना", "vicāra": "सतत विचार",
    "vicārā": "सतत विचार", "vitakkā": "आरंभिक विचार",
    "anidassanasappaṭighā": "दिखाई न देने वाला पर टकराव वाला", "gāmi": "की ओर ले जाने वाला",
    "parittā": "सीमित", "majjhimā": "मध्यम", "ārammaṇā": "विषय वाला", "sappaṭighā": "टकराव वाला",
    "nevavipākanavipākadhammadhammā": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "sahabhū": "साथ-साथ होने वाला", "vippayuttā": "अलग", "sahetukā": "मूल वाला",
    "kileso ceva kilesasampayuttañcā": "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी",
    "saṃyojanañceva saṃyojanasampayuttañcā": "बंधन रूपी भी और बंधनों से जुड़ा भी",
    "nīvaraṇañceva nīvaraṇasampayuttañcā": "बाधा रूपी भी और बाधाओं से जुड़ा भी",
    "āsavo ceva āsavasampayuttañcā": "मन के मैल रूपी भी और मन के मैलों से जुड़ा भी",
    "gantho ceva ganthasampayutta": "गाँठ रूपी भी और गाँठों से जुड़ा भी",
    "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacarā": "अभौतिक लोक से संबंधित", "āvacarā": "लोक से संबंधित",
    "ajjhattikā": "आंतरिक", "saraṇaṃ": "संघर्ष वाला", "niyyānikaṃ": "मुक्ति की ओर ले जाने वाला",
    "asaṃkiliṭṭhā": "क्लेशों से मलिन न होने वाला", "lokiyā": "लौकिक",
})
PP_SEGMENTS.update({"2-222", "2-223", "2-224"})
OVR5 = {
    "2-220": {"hetukaṃ": "मूल वाला"},                    # sahetukaṃ / ahetukaṃ «मूल वाली» (no pahātabb- here)
    "2-223": {"uppannā": "उत्पन्न हो चुका",              # PP matrix label (as 2-152 of the sample)
              "dhammā": NDE},                         # member of -dhammadhammā: no परिघटना in the Hindi
    "2-224": {"rūpā": "भौतिक", "cetasikaṃ": "मन का सहचर"},  # «Sattindriyā rūpā» = भौतिक; siyā cetasikaṃ = सहचर
}
ALLOWED5 = {
    ("2-224", "apariyāpannā"): "text «न समाई हुई»: समाया ~ समाई is regular inflection the checker does not model (as 2-153)",
    ("2-220", "sacchikatānaṃ"): "text «प्रत्यक्ष अनुभव की जा चुकी»: किया ~ की is regular inflection the checker does not model",
}

# ============================================================================ 16-nanavibhango
T16 = {**COMMON}
T16.update({
    # headings (notes-16-9: Ekakamātikā …, Ekakaniddeso …)
    "mātikā": "मूल सूची", "niddeso": "व्याख्या", "ekaka": "एकल वर्गीकरण",
    "catukka": "चार-चार के वर्गीकरण", "pañcaka": "पाँच-पाँच के वर्गीकरण", "chakka": "छह-छह के वर्गीकरण",
    "sattaka": "सात-सात के वर्गीकरण", "aṭṭhaka": "आठ-आठ के वर्गीकरण", "navaka": "नौ-नौ के वर्गीकरण",
    "dasaka": "दस-दस के वर्गीकरण", "chakkamātikā": "छह-छह के वर्गीकरणों की मूल सूची",
    "dasakamātikā": "दस-दस के वर्गीकरणों की मूल सूची",
    # 2-751 (the five consciousnesses, matrix labels in the feminine of the Hindi; values masc. sg.)
    "ñāṇavatthu": "ज्ञान का आधार", "vatthu": "आधार", "viññāṇā": "चेतना", "pahātabbā": "छोड़ा जाने वाला",
    "pītisahagatā": "उल्लास के साथ होने वाला", "saṃkilesikā": "क्लेशों का विषय बनने वाला",
    "āsekkhā": "सीखना पूरा होने के चरण का", "vippayuttā": "अलग", "vicārā": "सतत विचार",
    "acetasikā": "मन का सहचर न होने वाला", "parittā": "सीमित", "aniyatā": "अनिश्चित", "lokiyā": "लौकिक",
    "ārammaṇā": "विषय वाला", "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित",
    "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarā": "अभौतिक लोक से संबंधित",
    "āvacarā": "लोक से संबंधित",
    "uppanna": "उत्पन्न", "uppannārammaṇā": "उत्पन्न विषय वाला",
    "purejātārammaṇā": "पहले उत्पन्न हो चुके विषय वाला", "ajjhattika": "आंतरिक",
    "ajjhattikavatthukā": "आंतरिक आधार वाला", "bāhirārammaṇā": "बाह्य विषय वाला",
    "asambhinna": "नष्ट न हुआ", "nānā": "अलग-अलग", "gocara": "कार्यक्षेत्र", "gocaravisayaṃ": "कार्यक्षेत्र",
    "paccanubhonti": "अनुभव … करना", "asamannāhārā": "मन को उस ओर ले जाए बिना",
    "amanasikārā": "मनोयोग के बिना", "abbokiṇṇā": "बिना अंतराल के", "apubbaṃ": "आगे", "acarimaṃ": "पीछे",
    "uppajjanti": "उत्पन्न होना", "samanantarā": "ठीक बाद", "anābhogā": "मन लगाने से रहित",
    "paṭivijānāti": "पहचानना", "aññatra": "छोड़कर", "abhinipāta": "टकराना", "mattā": "भर",
    "dhammaṃ": "परिघटना", "iriyāpathaṃ": "मुद्रा", "kappeti": "अपनाना",
    "kāyakammaṃ": "शरीर का कर्म", "vacīkammaṃ": "वाणी का कर्म", "paṭṭhapeti": "आरंभ करना",
    "kusalākusalaṃ": "हितकर … हानिकर", "ākusalaṃ": "हानिकर", "kusalākusalaṃ dhammaṃ": "हितकर … हानिकर परिघटना",
    "samādiyati": "अपनाना", "samāpajjati": "ध्यान-अवस्था में प्रवेश करना", "vuṭṭhāti": "बाहर आना",
    "cavati": "मरना", "uppajjati": "उत्पन्न होना", "supati": "सोना", "paṭibujjhati": "जागना",
    "supinaṃ": "सपना", "passati": "देखना",
    "yāthāvaka": "यथार्थ रूप में", "vibhāvanā": "स्पष्ट करने वाला",
    "vibhāvanā paññā": "स्पष्ट करने वाली प्रज्ञा",
    # 2-752 (X paññā: the attribute agrees with प्रज्ञा, f.)
    "attha": "लक्ष्य", "jāpikā": "सिद्ध करने वाला", "jāpita": "सिद्ध कर चुका",
    "niyyānikā": "मुक्ति की ओर ले जाने वाला", "vitakkā": "आरंभिक विचार",
    "lokiyā paññā": "लौकिक प्रज्ञा", "niyatā paññā": "निश्चित प्रज्ञा", "aniyatā paññā": "अनिश्चित प्रज्ञा",
    "niyyānikā paññā": "मुक्ति की ओर ले जाने वाली प्रज्ञा",
    "sauttarā paññā": "सर्वोच्च न होने वाली प्रज्ञा", "anuttarā paññā": "सर्वोच्च प्रज्ञा",
    "pītisahagatā paññā": "उल्लास के साथ होने वाली प्रज्ञा",
    "na pītisahagatā paññā": "उल्लास के साथ न होने वाली प्रज्ञा",
    "sukhasahagatā paññā": "सुख के साथ होने वाली प्रज्ञा",
    "saṃkilesikā paññā": "क्लेशों का विषय बनने वाली प्रज्ञा",
    "asaṃkilesikā paññā": "क्लेशों का विषय न बनने वाली प्रज्ञा",
    "sāsavā paññā": "मन के मैलों का विषय बनने वाली प्रज्ञा",
    "anāsavā paññā": "मन के मैलों का विषय न बनने वाली प्रज्ञा",
    "āsavavippayuttā sāsavā paññā": "मन के मैलों से अलग पर उनका विषय बनने वाली प्रज्ञा",
    "pariyāpannā paññā": "अस्तित्व के लोकों में समाई हुई प्रज्ञा",
    "apariyāpannā paññā": "अस्तित्व के लोकों में न समाई हुई प्रज्ञा",
    "atthajāpikā paññā": "लक्ष्य को सिद्ध करने वाली प्रज्ञा", "jāpitatthā paññā": "लक्ष्य सिद्ध कर चुकी प्रज्ञा",
    "savitakkā paññā": "आरंभिक विचार वाली प्रज्ञा", "avitakkā paññā": "आरंभिक विचार से रहित प्रज्ञा",
    "savicārā paññā": "सतत विचार वाली प्रज्ञा", "avicārā paññā": "सतत विचार से रहित प्रज्ञा",
    "sappītikā paññā": "उल्लास वाली प्रज्ञा", "appītikā paññā": "उल्लास से रहित प्रज्ञा",
    # 2-753 (three ways)
    "cintāmayā paññā": "चिंतन से बनी प्रज्ञा", "suta": "सुनना", "sutamayā paññā": "सुनने से बनी प्रज्ञा",
    "bhāvanā": "मानसिक अभ्यास", "dāna": "दान", "sīla": "सदाचार", "citte": "मन",
    "adhipaññāya": "उच्च प्रज्ञा", "adhisīle paññā": "उच्च सदाचार में प्रज्ञा",
    "adhipaññāya paññā": "उच्च प्रज्ञा में प्रज्ञा", "upāya": "उपाय",
    "uppādinī": "उत्पन्न होने वाला", "ādhipatinī": "प्रधानता वाला", "anuppannā": "उत्पन्न न हुआ",
    "ācayagāminī": "संचय की ओर ले जाने वाला", "apacayagāminī": "संचय घटाने की ओर ले जाने वाला",
    "uppannā paññā": "उत्पन्न हो चुकी प्रज्ञा", "anuppannā paññā": "उत्पन्न न हुई प्रज्ञा",
    "uppādinī paññā": "उत्पन्न होने वाली प्रज्ञा",
    "parittā paññā": "सीमित प्रज्ञा", "mahaggatā paññā": "उन्नत प्रज्ञा", "appamāṇā paññā": "अपरिमित प्रज्ञा",
    "atītā paññā": "अतीत की प्रज्ञा", "anāgatā paññā": "भविष्य की प्रज्ञा", "paccuppannā paññā": "वर्तमान की प्रज्ञा",
    "ajjhattā paññā": "स्वयं से संबंधित प्रज्ञा", "bahiddhā paññā": "दूसरों से संबंधित प्रज्ञा",
    "ajjhattabahiddhā paññā": "स्वयं और दूसरों दोनों से संबंधित प्रज्ञा",
    "ācayagāminī paññā": "संचय की ओर ले जाने वाली प्रज्ञा",
    "apacayagāminī paññā": "संचय घटाने की ओर ले जाने वाली प्रज्ञा",
    "savitakkasavicārā paññā": "आरंभिक विचार और सतत विचार वाली प्रज्ञा",
    "avitakkavicāramattā paññā": "आरंभिक विचार से रहित केवल सतत विचार वाली प्रज्ञा",
    # 2-754 … 2-759 (four … nine ways)
    "ñāṇaṃ": "ज्ञान", "ānulomikaṃ": "अनुरूप", "saccānulomikaṃ": "सत्यों के अनुरूप",
    "samaṅgissa": "युक्त व्यक्ति", "phala": "फल", "dukkhe": "दुःख", "samudaye": "उत्पत्ति",
    "dukkhasamudaye": "दुःख की उत्पत्ति", "nirodhe": "अंत", "dukkhanirodhe": "दुःख का अंत",
    "paṭipadā": "प्रगति का ढंग", "dhamme": "शिक्षा", "anvaye": "अनुमान", "anvaye ñāṇaṃ": "अनुमान का ज्ञान",
    "pariye": "दूसरों के मन को जानना", "sammuti": "व्यावहारिक",
    "ācayāya": "संचय", "apacayāya": "संचय घटाना", "paññā ācayāya": "प्रज्ञा संचय के लिए",
    "paññā apacayāya": "प्रज्ञा संचय घटाने के लिए", "nibbidāya": "विरक्ति", "paṭivedhāya": "गहरी पैठ",
    "paññā nibbidāya": "प्रज्ञा विरक्ति के लिए",
    "hānabhāginī": "पतन की भागी", "ṭhitibhāginī": "स्थिरता की भागी", "visesa": "विशेष उन्नति",
    "visesabhāginī": "विशेष उन्नति की भागी", "nibbedha": "भेदन", "nibbedhabhāginī": "भेदन की भागी",
    "hānabhāginī paññā": "पतन की भागी प्रज्ञा", "ṭhitibhāginī paññā": "स्थिरता की भागी प्रज्ञा",
    "paṭisambhidā": "विश्लेषणात्मक ज्ञान", "ārammaṇāni": "विषय",
    "jarā": "बुढ़ापा", "maraṇe": "मृत्यु", "jarāmaraṇe": "बुढ़ापा और मृत्यु",
    "jarāmaraṇe ñāṇaṃ": "बुढ़ापे और मृत्यु का ज्ञान", "jarāmaraṇanirodhe": "बुढ़ापे और मृत्यु का अंत",
    "jātiyā": "जन्म", "bhave": "अस्तित्व", "upādāne": "आसक्ति", "taṇhāya": "तृष्णा", "phasse": "संपर्क",
    "āyatane": "इंद्रिय-क्षेत्र", "nāma": "मानसिक पक्ष", "rūpe": "भौतिक रूप",
    "nāmarūpe": "मानसिक पक्ष और भौतिक रूप", "viññāṇe": "चेतना", "viññāṇe ñāṇaṃ": "चेतना का ज्ञान",
    "saṅkhāresu": "मानसिक रचनाएँ", "saṅkhāresu ñāṇaṃ": "मानसिक रचनाओं का ज्ञान",
    "saṅkhāranirodhe": "मानसिक रचनाओं का अंत",
    "pañcañāṇiko": "पाँच ज्ञानों वाला", "abhiññāsu": "उच्च ज्ञान", "vatthūni": "आधार",
    "sattasattati": "सतहत्तर", "maggesu": "मार्ग", "phalesu": "फल",
    "anupubba": "क्रमिक", "vihāra": "ध्यान-अवस्था", "samāpattīsu": "ध्यान-अवस्था",   # pi-5 vihāra = ध्यान-अवस्था
    # 2-760 (the ten Tathāgata powers)
    "tathāgato": "तथागत", "tathāgatabalāni": "तथागत-बल", "dasa": "दस", "samannāgato": "संपन्न",
    "āsabhaṃ": "श्रेष्ठ वृषभ का", "ṭhānaṃ": "स्थान", "paṭijānāti": "दावा करना",
    "ṭhānaṃ paṭijānāti": "स्थान का दावा करना", "parisāsu": "सभा", "sīha": "सिंह", "nādaṃ": "नाद",
    "nadati": "करना", "sīhanādaṃ nadati": "सिंहनाद करना", "cakkaṃ": "चक्र", "brahmacakkaṃ": "श्रेष्ठ चक्र",
    "pavatteti": "चलाना", "brahmacakkaṃ pavatteti": "श्रेष्ठ चक्र चलाना", "āgamma": "सहारा",
    "balaṃ āgamma tathāgato": "बल के सहारे तथागत", "aṭṭhānato": "असंभव के रूप में",
    "yathābhūtaṃ": "यथार्थ रूप में", "pajānāti": "जानना",
    "samādānānaṃ": "अपनाया गया", "kammasamādānānaṃ": "अपनाया गया कर्म", "ṭhānaso": "परिस्थिति",
    "hetuso": "कारण", "sabbattha": "सभी गति", "gāminiṃ": "की ओर ले जाने वाला",
    "sattānaṃ": "प्राणी", "ādhimuttikataṃ": "झुकाव", "jhāna": "ध्यान", "vimokkha": "मुक्ति की अवस्था",
    "samāpattīnaṃ": "ध्यान-अवस्था", "saṃkilesaṃ": "दूषित होना", "vodānaṃ": "शुद्ध होना",
    "vuṭṭhānaṃ": "बाहर आना", "pubbenivāsānussatiṃ": "पूर्व जन्मों का अनुस्मरण", "ānussatiṃ": "अनुस्मरण",
    "cutūpapātaṃ": "मृत्यु और पुनर्जन्म", "ūpapātaṃ": "पुनर्जन्म", "āsavānaṃ": "मन के मैल", "khayaṃ": "क्षय",
    # 2-761 (X-meva = the Hindi of X; pi-1 convention)
    "hetumeva": "मूल", "hetukameva": "मूलों वाला", "vippayuttameva": "अलग", "saṅkhatameva": "निर्मित",
    "arūpameva": "अभौतिक", "lokiyameva": "लौकिक", "sāsavameva": "मन के मैलों का विषय बनने वाला",
    "saṃyojaniyameva": "बंधनों का विषय बनने वाला", "ganthaniyameva": "गाँठों का विषय बनने वाला",
    "oghaniyameva": "बाढ़ों का विषय बनने वाला", "yoganiyameva": "जकड़नों का विषय बनने वाला",
    "nīvaraṇiyameva": "बाधाओं का विषय बनने वाला", "parāmaṭṭhameva": "ग़लत धारणा का विषय बनने वाला",
    "upādāniyameva": "आसक्ति का विषय बनने वाला", "saṃkilesikameva": "क्लेशों का विषय बनने वाला",
    "abyākatameva": "नैतिक रूप से अनिर्धारित", "ārammaṇameva": "विषय वाला",
    "acetasikameva": "मन का सहचर न होने वाला", "vicārameva": "सतत विचार",
    "sahagatameva": "के साथ होने वाला", "pītisahagatameva": "उल्लास के साथ होने वाला",
    "pahātabbameva": "छोड़ा जाने वाला", "āsekkha": "सीखना पूरा होने के चरण का", "parittameva": "सीमित",
    "kāmāvacarameva": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacarameva": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacarameva": "अभौतिक लोक से संबंधित", "āvacarameva": "लोक से संबंधित",
    "apariyāpannameva": "अस्तित्व के लोकों में न समाया हुआ", "aniyatameva": "अनिश्चित",
    "viññeyyameva": "जाना जा सकने वाला", "aniccameva": "अनित्य", "ābhibhūtameva": "ग्रस्त",
    # 2-762 … 2-765 (glosses of the five consciousnesses)
    "uppannasmiṃ": "उत्पन्न हो चुका", "vatthukā": "आधार वाला", "ārammaṇe": "विषय", "ajjhattikā": "आंतरिक",
    "asambhinnasmiṃ": "नष्ट न हुआ", "aññaṃ": "अलग",
    "cakkhuviññāṇassa": "आँख की चेतना", "sotaviññāṇassa": "कान की चेतना", "ghānaviññāṇassa": "नाक की चेतना",
    "jivhāviññāṇassa": "जीभ की चेतना", "kāyaviññāṇassa": "शरीर की चेतना",
    "paccanubhoti": "अनुभव … करना", "gocaravisayaṃ paccanubhontī": "कार्यक्षेत्र का अनुभव … करना",
    "kāyaviññāṇaṃ na paccanubhoti": "अनुभव शरीर की चेतना नहीं करना",
    "cakkhuviññāṇaṃ na paccanubhoti": "अनुभव आँख की चेतना नहीं करना",
    "kāyaviññāṇassa gocaravisayaṃ": "शरीर की चेतना का कार्यक्षेत्र",
    "cakkhuviññāṇassa gocaravisayaṃ": "आँख की चेतना का कार्यक्षेत्र",
    "samannāharantassa": "मन को उस ओर ले जाने वाला", "manasikarontassa": "मनोयोग करने वाला",
    "paṭipāṭiyā": "एक के बाद एक लगातार", "khaṇe": "क्षण", "ekakkhaṇe": "एक ही क्षण",
    "kāyaviññāṇassa uppannasamanantarā": "शरीर की चेतना के उत्पन्न होने के ठीक बाद",
    "cakkhuviññāṇassa uppannasamanantarā": "आँख की चेतना के उत्पन्न होने के ठीक बाद",
    "kāyaviññāṇaṃ na uppajjati": "शरीर की चेतना उत्पन्न नहीं होना",
    "cakkhuviññāṇaṃ na uppajjati": "आँख की चेतना उत्पन्न नहीं होना",
    # 2-766 (glosses, end of the one-fold)
    "āvaṭṭanā": "मन का मुड़ना", "ābhogo": "मन लगाना", "samannāhāro": "मन को उस ओर ले जाना",
    "manasikāro": "मनोयोग", "āpāta": "सामने आना", "dhātuyā": "तत्व", "manodhātuyā": "मन का तत्व",
    "gamanaṃ": "चलना", "nisajjaṃ": "बैठना", "seyyaṃ": "लेटना", "ekakaṃ": "एकल वर्गीकरण",
    # 2-767 (two-fold glosses; notes-16-9: tīsu bhūmīsu kusalābyākate = तीनों स्तरों के … मन में)
    "bhūmīsu": "स्तर", "kusale": "हितकर मन", "ābyākate": "नैतिक रूप से अनिर्धारित मन",
    "kusalābyākate": "हितकर और नैतिक रूप से अनिर्धारित मन",
    "kiriyābyākate": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन",
    "bhūmīsu kusalābyākate paññā": "स्तरों के हितकर और नैतिक रूप से अनिर्धारित मन में प्रज्ञा",
    "kāmāvacarakusalābyākate paññā": "इंद्रिय-सुखों के लोक से संबंधित हितकर और नैतिक रूप से अनिर्धारित मन में प्रज्ञा",
    "maggesu paññā": "मार्गों में प्रज्ञा", "phalesu paññā": "फलों में प्रज्ञा",
    "vitakkasampayuttā paññā": "आरंभिक विचार से जुड़ी प्रज्ञा", "vicārasampayuttā paññā": "सतत विचार से जुड़ी प्रज्ञा",
    "pītisampayuttā paññā": "उल्लास से जुड़ी प्रज्ञा", "sukhasampayuttā paññā": "सुख से जुड़ी प्रज्ञा",
    "upekkhāsampayuttā paññā": "समभाव से जुड़ी प्रज्ञा",
    "abhiññaṃ": "उच्च ज्ञान", "samāpattiṃ": "ध्यान-अवस्था", "uppādentassa": "उत्पन्न करना",
    "uppannāya": "उत्पन्न हो जाना",
    # 2-768 … 2-774 (the three-fold glosses)
    "vihitesu": "रचा गया", "āyatanesu": "क्षेत्र", "sippāyatanesu": "शिल्प का क्षेत्र", "vijjā": "विद्या",
    "ṭṭhānesu": "क्षेत्र", "kammassakataṃ": "कर्म का अपना होना", "anicca": "अनित्य",
    "evarūpiṃ": "इस प्रकार का", "anulomikaṃ": "अनुकूल", "khantiṃ": "स्वीकृति", "diṭṭhiṃ": "दृष्टि",
    "ruciṃ": "रुचि", "mudiṃ": "अनुमोदन", "pekkhaṃ": "परख", "dhamma": "परिघटना", "nijjhāna": "मनन",
    "sutvā": "सुनना", "paṭilabhati": "प्राप्त करना",
    "samāpannassa paññā": "ध्यान-अवस्था में लीन व्यक्ति की … प्रज्ञा",
    "ārabbha": "लेकर", "ādhigaccha": "कारण", "dānaṃ": "दान", "sīlaṃ": "सदाचार", "sammādiṭṭhi": "सही दृष्टि",
    "dānamayā paññā": "दान से बनी प्रज्ञा", "sīlamayā paññā": "सदाचार से बनी प्रज्ञा",
    "pātimokkha": "भिक्षु-नियम", "saṃvaraṃ": "संयम", "saṃvarantassa": "स्वयं को संयमित करने वाला",
    "sīle": "सदाचार", "samāpajjantassa": "प्रवेश करने वाला", "ārūpāvacara": "अभौतिक लोक से संबंधित",
    "rūpāvacarārūpāvacarasamāpattiṃ": "सूक्ष्म भौतिक लोक और अभौतिक लोक से संबंधित ध्यान-अवस्था",
    "manasikaroto": "मनोयोग करने वाला", "pahīyanti": "छूट जाना", "nirujjhanti": "समाप्त होना",
    "vepullāya": "विपुल होना", "pāripūriyā": "परिपूर्ण होना",
    "tatrupāyā": "वहाँ उपाय के रूप में होने वाला",
    "dhammā": "परिघटना", "kusalā dhammā": "हितकर परिघटना", "akusalā dhammā": "हानिकर परिघटना",
    "bhūmīsu vipāke paññā": "स्तरों के कर्म-फल रूपी मन में प्रज्ञा",
    "vicāra": "सतत विचार", "vitakkavicāra": "आरंभिक विचार और सतत विचार",
    "vitakkavicārasampayuttā paññā": "आरंभिक विचार और सतत विचार से जुड़ी प्रज्ञा",
    "vitakkavicāravippayuttā paññā": "आरंभिक विचार और सतत विचार से अलग प्रज्ञा",
    "vitakkavippayuttā vicārasampayuttā paññā": "आरंभिक विचार से अलग और सतत विचार से जुड़ी प्रज्ञा",
    # 2-776 … 2-789
    "bhūmīsu kusale paññā": "स्तरों के हितकर मन में प्रज्ञा",
    "bhūmīsu kiriyābyākate paññā": "स्तरों के केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन में प्रज्ञा",
    "upariṭṭhimā": "सबसे ऊँचा", "arahatta": "अर्हत्-पद", "phale": "फल",
    "rūpāvacarārūpāvacarakusalābyākate":
        "सूक्ष्म भौतिक लोक और अभौतिक लोक से संबंधित हितकर और नैतिक रूप से अनिर्धारित मन",
    "āvacara": "लोक से संबंधित", "dhamme": "परिघटना", "paritte": "सीमित", "mahaggate": "उन्नत",
    "appamāṇe": "अपरिमित", "ariya": "आर्य", "maggaṃ": "मार्ग", "adhipatiṃ": "प्रधान", "karitvā": "बनाकर",
    "ajjhatte": "स्वयं से संबंधित", "ajjhatte dhamme": "स्वयं से संबंधित परिघटना",
    "bahiddhādhamme": "दूसरों से संबंधित परिघटना", "ajjhatta": "स्वयं",
    # 2-793 (kammassakatañāṇa: the right-view formula)
    "hutaṃ": "आहुति", "sukata": "अच्छे … ढंग से किया गया", "dukkaṭānaṃ": "बुरे ढंग से किया गया",
    "kammānaṃ": "कर्म", "phalaṃ": "फल", "mātā": "माता", "pitā": "पिता", "sattā": "प्राणी",
    "opapātikā": "स्वतः जन्म लेने वाला", "samaṇa": "श्रमण", "brāhmaṇā": "ब्राह्मण",
    "sammaggatā": "सही मार्ग पर पहुँचा", "paṭipannā": "साधना करने वाला", "sayaṃ": "स्वयं",
    "abhiññā": "उच्च ज्ञान", "sacchikatvā": "साक्षात्कार करना", "pavedentī": "बताना",
    "evarūpā": "इस प्रकार का", "yā": "जो", "anulomikā": "अनुकूल", "khanti": "स्वीकृति", "ruci": "रुचि",
    "pekkhā": "परख", "kusalā paññā": "हितकर प्रज्ञा",
    # 2-796 (dhamme / anvaye / pariye / sammuti ñāṇa)
    "ñātena": "जाना हुआ", "viditena": "विदित", "pariyogāḷhena": "गहराई से समझा हुआ", "nayaṃ": "निष्कर्ष",
    "neti": "निकालना", "ye hi keci": "जिन किन्हीं", "samaṇā": "श्रमण", "dukkhaṃ": "दुःख",
    "samudayaṃ": "उत्पत्ति", "dukkhasamudayaṃ": "दुःख की उत्पत्ति", "nirodhaṃ": "अंत",
    "dukkhanirodhaṃ": "दुःख का अंत", "abbhaññaṃsu": "पूरी तरह जानना",
    "dukkhaṃ abbhaññaṃsu": "दुःख को पूरी तरह जानना", "abhijānissanti": "पूरी तरह जानना",
    "bhikkhu": "भिक्षु", "puggalānaṃ": "व्यक्ति", "ceto": "मन", "paricca": "घेरकर",
    "pariye ñāṇaṃ": "दूसरों के मन को जानने का ज्ञान",
    "sarāgaṃ": "राग वाला", "sarāgaṃ citta": "राग वाला मन", "vītarāgaṃ citta": "राग से रहित मन",
    "sadosaṃ": "द्वेष वाला", "sadosaṃ citta": "द्वेष वाला मन", "vītadosaṃ citta": "द्वेष से रहित मन",
    "samohaṃ": "मोह वाला", "samohaṃ citta": "मोह वाला मन", "vītamohaṃ citta": "मोह से रहित मन",
    "saṃkhittaṃ": "सिकुड़ा हुआ", "saṃkhittaṃ citta": "सिकुड़ा हुआ मन",
    "vikkhittaṃ": "बिखरा हुआ", "vikkhittaṃ citta": "बिखरा हुआ मन",
    "mahaggataṃ": "उन्नत", "mahaggataṃ citta": "उन्नत मन", "amahaggataṃ": "अनुन्नत",
    "amahaggataṃ citta": "अनुन्नत मन", "sauttaraṃ": "सर्वोच्च न होने वाला",
    "sauttaraṃ citta": "सर्वोच्च न होने वाला मन", "anuttaraṃ": "सर्वोच्च", "anuttaraṃ citta": "सर्वोच्च मन",
    "samāhitaṃ": "एकाग्र", "samāhitaṃ citta": "एकाग्र मन", "asamāhitaṃ": "अनेकाग्र",
    "asamāhitaṃ citta": "अनेकाग्र मन", "vimuttaṃ": "मुक्त", "vimuttaṃ citta": "मुक्त मन",
    "avimuttaṃ": "अमुक्त", "avimuttaṃ citta": "अमुक्त मन",
    "avasesā": "शेष", "avasesā paññā": "शेष प्रज्ञा",
    # 2-797, 2-798
    "rūpāvacarārūpāvacarakusale": "सूक्ष्म भौतिक लोक और अभौतिक लोक से संबंधित हितकर मन",
    "hoti": "होना", "kāmesu": "इंद्रिय-सुख", "vītarāgo": "राग से रहित", "abhiññāyo": "उच्च ज्ञान",
    "paṭivijjhati": "पैठना", "saccāni": "सत्य",
    # 2-799 (hānabhāginī … paññā)
    "jhānassa": "ध्यान", "catutthassa jhānassa": "चौथा ध्यान", "lābhiṃ": "प्राप्त कर चुका व्यक्ति",
    "saññāmanasikārā": "पहचान और मनोयोग", "manasikārā": "मनोयोग", "samudācaranti": "हावी होना",
    "kāmasahagatā saññāmanasikārā": "इंद्रिय-सुखों के साथ होने वाली पहचान और मनोयोग",
    "anudhammatā": "अनुरूप", "tadanudhammatā sati": "उसके अनुरूप सजगता", "santiṭṭhati": "टिकना",
    "tadanudhammatā sati santiṭṭhati": "उसके अनुरूप सजगता टिकना",
    "avitakka": "आरंभिक विचार का अभाव", "nibbidā": "विरक्ति", "nibbidāsahagatā": "विरक्ति के साथ होने वाला",
    "ūpasañhitā": "जुड़ा", "virāgūpasañhitā": "वैराग्य से जुड़ा", "pītisukha": "उल्लास और सुख",
    "pītisukhasahagatā": "उल्लास और सुख के साथ होने वाला", "adukkhamasukha": "न दुःख न सुख",
    "āyatana": "क्षेत्र", "ānañcāyatana": "अनंत … क्षेत्र",
    "ākāsānañcāyatanassa": "अनंत आकाश का क्षेत्र", "viññāṇañcāyatanassa": "अनंत चेतना का क्षेत्र",
    "ākiñcaññāyatanassa": "कुछ भी न होने का क्षेत्र",
    "nevasaññānāsaññāyatanasahagatā": "न पहचान न अ-पहचान के क्षेत्र के साथ होने वाला",
    # 2-800 (the four analytical knowledges)
    "atthe": "अर्थ", "atthapaṭisambhidā": "अर्थ का विश्लेषणात्मक ज्ञान",
    "dhammapaṭisambhidā": "परिघटनाओं का विश्लेषणात्मक ज्ञान", "nirutti": "भाषा",
    "niruttipaṭisambhidā": "भाषा का विश्लेषणात्मक ज्ञान", "ābhilāpe": "अभिव्यक्ति",
    "paṭibhāna": "सूझ-बूझ", "paṭibhānapaṭisambhidā": "सूझ-बूझ का विश्लेषणात्मक ज्ञान", "ñāṇesu": "ज्ञान",
    # 2-801 … 2-803 (paṭipadā, ārammaṇāni, the dependent-arising knowledges)
    "dukkhapaṭipadā": "दुःखद प्रगति", "sukhapaṭipadā": "सुखद प्रगति", "ābhiññā": "उच्च ज्ञान",
    "dandhābhiññā": "धीमे उच्च ज्ञान वाला", "khippābhiññā": "तेज़ उच्च ज्ञान वाला",
    "dukkhapaṭipadā dandhābhiññā": "दुःखद प्रगति और धीमे उच्च ज्ञान वाला",
    "dukkhapaṭipadā khippābhiññā": "दुःखद प्रगति और तेज़ उच्च ज्ञान वाला",
    "dukkhapaṭipadā dandhābhiññā paññā": "दुःखद प्रगति और धीमे उच्च ज्ञान वाली प्रज्ञा",
    "sukhapaṭipadā dandhābhiññā paññā": "सुखद प्रगति और धीमे उच्च ज्ञान वाली प्रज्ञा",
    "kicchena": "कठिनाई", "kasirena": "कष्ट", "samādhiṃ": "एकाग्रता", "dandhaṃ": "धीरे-धीरे",
    "khippaṃ": "जल्दी", "abhijānantassa": "उच्च ज्ञान से जानने वाला",
    "samādhissa": "एकाग्रता", "nikāma": "इच्छा भर", "lābhissa": "प्राप्त कर पाने वाला",
    "pharantassa": "व्याप्त करने वाला", "vipulaṃ": "विस्तार से", "samudaya": "उत्पत्ति",
    "parittā parittārammaṇā paññā": "सीमित और सीमित विषय वाली प्रज्ञा",
    "appamāṇā appamāṇārammaṇā paññā": "अपरिमित और अपरिमित विषय वाली प्रज्ञा",
    "nirodha": "अंत", "saṅkhāranirodhaṃ": "मानसिक रचनाओं का अंत", "saṅkhāre": "मानसिक रचनाएँ",
    "viññāṇepetaṃ ñāṇaṃ": "चेतना का ज्ञान भी", "catukkaṃ": "चार-चार के वर्गीकरण",
    # 2-804 (five-factored / five-knowledge right concentration)
    "pharaṇatā": "व्याप्त होना", "āloka": "प्रकाश", "paracitte": "दूसरों का मन", "dibba": "दिव्य",
    "cakkhu": "आँख", "jhānesu": "ध्यान", "paccavekkhaṇā": "पुनः विचार",
    "paccavekkhaṇāñāṇaṃ": "पुनः विचार का ज्ञान", "nimittaṃ": "चिह्न", "vuṭṭhitassa": "बाहर आया व्यक्ति",
    "sukho": "सुखद", "paccattaññeva": "अपने भीतर ही", "ñāṇaṃ uppajjati": "ज्ञान … उत्पन्न होना",
    "ariyo": "आर्य", "nirāmiso": "सांसारिक भोगों से रहित", "sevito": "अपनाया जाने वाला",
    "akāpurisasevito": "अधम लोगों द्वारा अपनाया जाने वाला नहीं", "santo": "शांत",
    "paṭippassaddha": "प्रशांति", "laddho": "प्राप्त", "ādhigato": "प्राप्त",
    "ekodibhāvādhigato": "मन के एक बिंदु पर टिकने से प्राप्त", "sasaṅkhāra": "बलपूर्वक",
    "niggayha": "दबाकर", "vārita": "रोककर",
    "sasaṅkhāraniggayhavāritagato": "बलपूर्वक दबाकर और रोककर प्राप्त", "sato": "सजग",
    "samāpajjāmi": "प्रवेश करना", "vuṭṭhahāmī": "बाहर आना", "pañcakaṃ": "पाँच-पाँच के वर्गीकरण",
    # 2-805 (six higher knowledges)
    "iddhi": "सिद्धि", "vidhe": "प्रकार", "sota": "कान", "sotadhātu": "कान का तत्व", "visuddhiyā": "विशुद्धि",
    "pubbenivāsānussatiyā": "पूर्व जन्मों का अनुस्मरण", "ānussatiyā": "अनुस्मरण",
    "cutūpapāte": "मृत्यु और पुनर्जन्म", "ūpapāte": "पुनर्जन्म", "khaye": "क्षय",
    "chakkaṃ": "छह-छह के वर्गीकरण",
    # 2-806 (the seventy-seven bases)
    "jāti": "जन्म", "jātipaccayā": "जन्म के कारण", "jarāmaraṇa": "बुढ़ापा और मृत्यु", "maraṇa": "मृत्यु",
    "bhava": "अस्तित्व", "bhavapaccayā": "अस्तित्व के कारण", "upādānapaccayā": "आसक्ति के कारण",
    "taṇhā": "तृष्णा", "taṇhāpaccayā": "तृष्णा के कारण", "vedanāpaccayā": "अनुभूति के कारण",
    "phassapaccayā": "संपर्क के कारण", "saḷāyatanapaccayā": "छह इंद्रिय-क्षेत्रों के कारण",
    "nāmarūpa": "मानसिक पक्ष और भौतिक रूप", "nāmarūpapaccayā": "मानसिक पक्ष और भौतिक रूप के कारण",
    "viññāṇapaccayā": "चेतना के कारण", "saṅkhārapaccayā": "मानसिक रचनाओं के कारण",
    "avijjā": "अज्ञान", "avijjāpaccayā": "अज्ञान के कारण", "ṭṭhiti": "स्थिति", "tampi": "वह भी",
    "khaya": "क्षय", "vaya": "मिटना", "virāga": "फीका पड़ना", "sattakaṃ": "सात-सात के वर्गीकरण",
    # 2-807, 2-808
    "sotāpatti": "धारा में प्रवेश", "sakadāgāmi": "एक बार लौटना", "anāgāmi": "फिर न लौटना", "magge": "मार्ग",
    "aṭṭhakaṃ": "आठ-आठ के वर्गीकरण", "samāpattiyā": "अवस्था", "catutthajjhāna": "चौथा ध्यान",
    "ākāsānañcāyatana": "अनंत आकाश का क्षेत्र",
    "ākāsānañcāyatanasamāpattiyā": "अनंत आकाश के क्षेत्र की अवस्था",
    "viññāṇañcāyatanasamāpattiyā": "अनंत चेतना के क्षेत्र की अवस्था",
    "ākiñcaññāyatanasamāpattiyā": "कुछ भी न होने के क्षेत्र की अवस्था",
    "nevasaññānāsaññāyatanasamāpattiyā": "न पहचान न अ-पहचान के क्षेत्र की अवस्था",
    "vedayita": "अनुभूति", "navakaṃ": "नौ-नौ के वर्गीकरण",
    # 2-809 (first power: possible and impossible; notes-16-9 ṭhāna/aṭṭhāna formula)
    "aṭṭhānametaṃ": "यह असंभव", "anavakāso": "कोई गुंजाइश नहीं", "sampanno": "संपन्न",
    "diṭṭhisampanno": "सही दृष्टि से संपन्न", "puggalo": "व्यक्ति",
    "diṭṭhisampanno puggalo": "सही दृष्टि से संपन्न व्यक्ति", "puthujjano": "साधारण व्यक्ति",
    "saṅkhāraṃ": "निर्मित परिघटना", "niccato": "नित्य के रूप में", "sukhato": "सुख के रूप में",
    "atthato": "सार के रूप में", "mātaraṃ": "माता", "pitaraṃ": "पिता", "jīvitā": "प्राण", "voropeyya": "लेना",
    "arahaṃ": "अर्हत्", "arahanto": "अर्हत्", "paduṭṭhena": "द्वेष से भरा", "cittena": "मन", "lohitaṃ": "खून",
    "uppādeyya": "बहाना", "saṅghaṃ": "संघ", "satthāraṃ": "शास्ता", "uddiseyya": "बताना",
    "bhavaṃ": "जन्म", "nibbatteyya": "उत्पन्न होना", "lokadhātuyā": "विश्व",
    "sambuddho": "जागृत बुद्ध", "sammāsambuddho": "पूर्ण रूप से जागृत बुद्ध",
    "sammāsambuddhā": "पूर्ण रूप से जागृत बुद्ध", "uppajjeyyuṃ": "उत्पन्न होना", "rājā": "राजा",
    "rājāno": "राजा", "cakkavattī": "चक्रवर्ती", "itthī": "स्त्री", "puriso": "पुरुष",
    "sakkattaṃ": "शक्र का पद", "kareyya": "संभालना", "kāya": "शरीर", "vacī": "वाणी", "mano": "मन",
    "duccarita": "दुराचरण", "sucarita": "सदाचरण", "kāyaduccarita": "शरीर का दुराचरण",
    "vacīduccarita": "वाणी का दुराचरण", "manoduccarita": "मन का दुराचरण",
    "kāyasucarita": "शरीर का सदाचरण", "vacīsucarita": "वाणी का सदाचरण", "manosucarita": "मन का सदाचरण",
    "iṭṭho": "मनचाहा", "kanto": "प्रिय", "manāpo": "मनभावन", "aniṭṭho": "अनचाहा", "akanto": "अप्रिय",
    "amanāpo": "मन को न भाने वाला", "manāpo vipāko": "मनभावन कर्म-फल",
    "amanāpo vipāko": "मन को न भाने वाला कर्म-फल",
    "kāyassa": "शरीर", "bhedā": "छूटना", "maraṇā": "मृत्यु", "paraṃ maraṇā": "मृत्यु के बाद",
    "sugatiṃ": "सुगति", "gatiṃ": "गति", "saggaṃ": "स्वर्ग", "saggaṃ lokaṃ": "स्वर्ग लोक",
    "duggatiṃ": "दुर्गति", "vinipātaṃ": "पतन का लोक", "nirayaṃ": "नरक", "upapajjeyya": "उत्पन्न होना",
    "ye ye": "जो-जो",
    # 2-810 … 2-813 (powers 2-5)
    "samādānāni": "अपनाया गया", "kammasamādānāni": "अपनाया गया कर्म", "pāpakāni": "बुरा",
    "pāpakāni kammasamādānāni": "बुरा अपनाया गया कर्म", "kalyāṇāni kammasamādānāni": "अच्छा अपनाया गया कर्म",
    "gati": "गति", "upadhi": "शरीर", "payoga": "पुरुषार्थ", "sampatti": "अनुकूलता", "vipattiṃ": "प्रतिकूलता",
    "paṭibāḷhāni": "रुका रहना", "vipaccanti": "फल देना",
    "niraya": "नरक", "tiracchāna": "पशु", "yoni": "जन्म", "petti": "प्रेत", "visaya": "लोक",
    "manussa": "मनुष्य", "deva": "देव", "nānattaṃ": "विविधता",
    "ādhimuttikā": "झुकाव वाला", "hīnādhimuttikā": "हीन झुकाव वाला", "paṇītādhimuttikā": "उत्तम झुकाव वाला",
    "sevanti": "संगति करना", "seviṃsu": "संगति करना", "sevissanti": "संगति करना",
    "bhajanti": "मेल-जोल रखना", "bhajiṃsu": "मेल-जोल रखना",
    "payirupāsanti": "पास उठना-बैठना", "payirupāsiṃsu": "पास उठना-बैठना",
    # 2-814 … 2-818 (power 6: āsaya, anusaya, carita, adhimutti)
    "āsayaṃ": "आशय", "āsayo": "आशय", "anusayaṃ": "सुप्त प्रवृत्ति", "anusayo": "सुप्त प्रवृत्ति",
    "ānusayā": "सुप्त प्रवृत्ति", "caritaṃ": "आचरण", "adhimuttiṃ": "झुकाव", "adhimutti": "झुकाव",
    "akkhe": "आँख", "rajakkhe": "आँखों में … धूल वाला", "indriye": "क्षमता",
    "tikkhindriye": "तीक्ष्ण क्षमताओं वाला", "mudindriye": "मंद क्षमताओं वाला", "ākāre": "स्वभाव",
    "svākāre": "अच्छे स्वभाव वाला", "dvākāre": "बुरे स्वभाव वाला", "viññāpaye": "समझाए जा सकने वाला",
    "suviññāpaye": "आसानी से समझाए जा सकने वाला", "duviññāpaye": "कठिनाई से समझाए जा सकने वाला",
    "ābhabbe": "असमर्थ", "bhabbābhabbe": "समर्थ और असमर्थ",
    "sassato": "शाश्वत", "antavā": "सीमित", "anantavā": "असीम", "jīvaṃ": "जीव", "sarīra": "शरीर",
    "hoti tathāgato": "तथागत रहना", "bhavadiṭṭhi": "अस्तित्व की दृष्टि", "vibhava": "अनस्तित्व",
    "vibhavadiṭṭhi": "अनस्तित्व की दृष्टि", "sannissitā": "टिका होना", "ante": "अति", "anupagamma": "न अपनाकर",
    "idappaccayatā": "कार्य-कारण का नियम", "paccayatā": "कार्य-कारण का नियम", "samuppannesu": "उत्पन्न",
    "dhammesu": "परिघटना", "paṭiladdhā": "प्राप्त",
    "kāma": "इंद्रिय-सुख", "rāgānusayo": "राग की सुप्त प्रवृत्ति", "paṭighānusayo": "चिढ़ की सुप्त प्रवृत्ति",
    "māno": "अहंकार", "vicikicchā": "संशय", "piyarūpaṃ": "प्रिय लगने वाला",
    "appiyarūpaṃ": "अप्रिय लगने वाला", "sātarūpaṃ": "सुहावना लगने वाला", "asātarūpaṃ": "असुहावना लगने वाला",
    "anuseti": "सोया रहना", "ānupatitā": "पीछे-पीछे चलना", "ekaṭṭho": "एक ही आधार पर रहने वाला",
    "tadekaṭṭho": "उसी के साथ एक ही आधार पर रहने वाला",
    "puññābhisaṅkhāro": "पुण्य की कर्म-रचना", "apuññābhisaṅkhāro": "अपुण्य की कर्म-रचना",
    "āneñjābhisaṅkhāro": "अविचल अवस्था की कर्म-रचना", "ābhisaṅkhāro": "कर्म-रचना",
    "paritta": "सीमित", "bhūmako": "स्तर का",
    # 2-819 … 2-827 (the kinds of beings)
    "akkhā": "आँख", "rajakkhā": "आँखों में … धूल", "kilesavatthūni": "मन के क्लेशों का … आधार",
    "dasa kilesavatthūni": "मन के क्लेशों के … दस आधार", "lobho": "लोभ", "doso": "द्वेष", "moho": "मोह",
    "thinaṃ": "आलस्य", "uddhaccaṃ": "बेचैनी", "ahirikaṃ": "निर्लज्जता", "anottappaṃ": "बुराई के प्रति निडरता",
    "āsevitāni": "निरंतर सेवित", "bhāvitāni": "अभ्यस्त", "bahulīkatāni": "बार-बार किया गया",
    "ussadagatāni": "प्रबल हो चुका", "anāsevitāni": "न निरंतर सेवित", "abhāvitāni": "न अभ्यस्त",
    "abahulīkatāni": "न बार-बार किया गया", "anussadagatāni": "न प्रबल हुआ",
    "mudindriyā": "मंद क्षमताओं वाला", "tikkhindriyā": "तीक्ष्ण क्षमताओं वाला", "indriyā": "क्षमता",
    "ākārā": "स्वभाव", "dvākārā": "बुरे स्वभाव वाला", "svākārā": "अच्छे स्वभाव वाला", "pāpa": "बुरा",
    "āsayā": "आशय वाला", "caritā": "आचरण वाला", "kalyāṇacaritā": "अच्छे आचरण वाला",
    "kalyāṇādhimuttikā": "अच्छे झुकाव वाला", "viññāpayā": "समझाना",
    "suviññāpayā": "आसानी से समझाया जा सकना", "duviññāpayā": "समझाना कठिन",
    "āvaraṇena": "बाधा", "kammāvaraṇena": "कर्म की बाधा", "kilesāvaraṇena": "मन के क्लेशों की बाधा",
    "samannāgatā": "युक्त", "āvaraṇena samannāgatā": "बाधा से युक्त", "assaddhā": "श्रद्धाहीन",
    "acchandikā": "चाह न रखने वाला", "chandikā": "चाह रखने वाला", "duppaññā": "प्रज्ञाहीन",
    "abhabbā": "असमर्थ", "bhabbā": "समर्थ", "niyāmaṃ": "निश्चित मार्ग", "okkamituṃ": "प्रवेश करना",
    "kusalesu": "हितकर", "kusalesu dhammesu": "हितकर परिघटना", "sammattaṃ": "सही",
    # 2-828 (power 7: jhāyī, jhāna, vimokkha, samādhi, samāpatti …)
    "jhāyī": "ध्यान करने वाला", "pacceti": "समझना", "samānaṃ": "होते हुए", "vipatti": "विफलता",
    "dandhaṃ samāpajjati": "धीरे प्रवेश करना", "khippaṃ samāpajjati": "जल्दी प्रवेश करना",
    "samādhismiṃ samādhi": "एकाग्रता में एकाग्र होना", "samādhismiṃ samāpatti": "एकाग्रता में प्रवेश करना",
    "jhānāni": "ध्यान", "catutthaṃ jhānaṃ": "चौथा ध्यान", "vimokkho": "मुक्ति की अवस्था",
    "vimokkhā": "मुक्ति की … अवस्था", "rūpī": "भौतिक रूप वाला", "rūpāni": "दृश्य रूप",
    "saññī": "पहचान रखना", "subhanteva": "सुंदर", "adhimutto": "मन को टिकाए रहना", "sabbaso": "पूरी तरह",
    "saññānaṃ": "पहचान", "rūpasaññānaṃ": "भौतिक रूप की पहचान", "paṭigha": "टकराव",
    "paṭighasaññānaṃ": "टकराव की पहचान", "nānatta": "विविधता", "nānattasaññānaṃ": "विविधता की पहचान",
    "samatikkamma": "पार करना", "atthaṅgamā": "मिट जाना", "ananto": "अनंत", "ākāso": "आकाश",
    "natthi kiñci": "कुछ भी नहीं", "upasampajja": "प्राप्त करना", "viharati": "रहना",
    "upasampajja viharati": "प्राप्त करके उसमें रहना",
    "ākāsānañcāyatanaṃ": "अनंत आकाश का क्षेत्र", "viññāṇañcāyatanaṃ": "अनंत चेतना का क्षेत्र",
    "ākiñcaññāyatanaṃ": "कुछ भी न होने का क्षेत्र",
    "nevasaññānāsaññāyatanaṃ": "न पहचान न अ-पहचान का क्षेत्र",
    "pañcamo": "पाँचवाँ", "chaṭṭho": "छठा", "sattamo": "सातवाँ", "aṭṭhamo": "आठवाँ",
    "samādhī": "एकाग्रता", "samāpatti": "ध्यान-अवस्था", "saṃkilesa": "दूषित होना", "vodāna": "शुद्ध होना",
    "vuṭṭhāna": "बाहर आना", "vuṭṭhānampi": "बाहर आना भी", "hānabhāgiyo": "पतन की भागी",
    "visesabhāgiyo": "विशेष उन्नति की भागी",
    # 2-829 … 2-831 (powers 8-10)
    "anussarati": "याद करना", "anekavihitaṃ": "अनेक प्रकार का", "pubbenivāsaṃ": "पूर्व जन्म",
    "ānussati": "अनुस्मरण", "jātiṃ": "जन्म", "jātiyo": "जन्म", "dasapi": "दस … भी",
    "dasapi jātiyo": "दस जन्म भी", "vīsampi": "बीस … भी", "tiṃsampi": "तीस … भी",
    "cattālīsampi": "चालीस … भी", "paññāsampi": "पचास … भी", "satampi": "सौ … भी", "sahassampi": "हज़ार … भी",
    "saṃvaṭṭa": "सिमटना", "vivaṭṭa": "फैलना", "kappe": "कल्प", "amutra": "अमुक स्थान", "nāmo": "नाम",
    "gotto": "गोत्र", "vaṇṇo": "रंग-रूप", "paṭisaṃvedī": "अनुभव करता हुआ", "pariyanto": "तक",
    "cuto": "जीवन पूरा करना", "udapādiṃ": "उत्पन्न हुआ", "ūpapanno": "उत्पन्न हुआ",
    "sākāraṃ": "आकार-प्रकार … सहित",
    "dibbena": "दिव्य", "cakkhunā": "दृष्टि", "visuddhena": "विशुद्ध", "atikkanta": "परे",
    "mānusakena": "मनुष्य", "cavamāne": "मरता हुआ", "hīne": "हीन", "paṇīte": "उत्तम", "suvaṇṇe": "सुंदर",
    "dubbaṇṇe": "कुरूप", "sugate": "सुगति", "duggate": "दुर्गति", "ūpage": "जाता हुआ",
    "yathākammūpage": "अपने कर्मों के अनुसार जाता हुआ", "vata": "सचमुच",
    "duccaritena": "दुराचरण", "sucaritena": "सदाचरण", "kāyaduccaritena": "शरीर का दुराचरण",
    "vacīduccaritena": "वाणी का दुराचरण", "manoduccaritena": "मन का दुराचरण",
    "kāyasucaritena": "शरीर का सदाचरण", "vacīsucaritena": "वाणी का सदाचरण",
    "manosucaritena": "मन का सदाचरण", "ariyānaṃ": "आर्य", "upavādakā": "निंदा करने वाला",
    "micchā": "ग़लत", "micchādiṭṭhikā": "ग़लत दृष्टि वाला", "samādānā": "अपनाने वाला",
    "upapannā": "उत्पन्न हुआ",
    "cetovimuttiṃ": "मन की मुक्ति", "vimuttiṃ": "मुक्ति", "diṭṭheva dhamme": "इसी जीवन",
    "viharatī": "रहना", "upasampajja viharatī": "प्राप्त करके उसमें रहना", "dasakaṃ": "दस-दस के वर्गीकरण",
})
ALT16 = {"yathābhūtaṃ": ["यथार्थ रूप में", "यथार्थ"]}   # «यथार्थ रूप में जानते हैं» / «यथार्थ ज्ञान»
OVR16 = {
    "2-753": {"uppannā": "उत्पन्न हो चुका",      # matrix label «उत्पन्न हो चुकी प्रज्ञा» (as 2-152)
              "hetukā": "मूल बनाने वाला",         # maggahetukā «मार्ग को मूल बनाने वाली»
              "dhammā": NDE},                     # member of -dhammadhammā: no परिघटना in the Hindi
    "2-751": {"uppajjati": "जन्म लेना"},        # na cavati na uppajjati «न मरता है, न जन्म लेता है»
    "2-766": {"ṭhānaṃ": "खड़ा होना",           # posture: gamanaṃ vā ṭhānaṃ vā … «चलना, खड़ा होना …»
              "uppajjati": "जन्म लेना"},        # na cavati na uppajjati
    "2-768": {"yoga": "कौशल"},                 # yogavihitesu «कौशल से रचे गए» (not the yoga cluster)
    "2-771": {"uppannā": "उत्पन्न हो चुका"},     # «उत्पन्न हो चुकी … परिघटनाएँ»
    "2-772": {"dhammā": NDE},                   # member of -dhammadhammā: no परिघटना in the Hindi
    "2-754": {"Dhamme": "शिक्षा"},              # dhamme ñāṇaṃ «शिक्षा का ज्ञान» (notes-16-9)
    "2-796": {"dhamme": "शिक्षा"},              # dhamme ñāṇaṃ «शिक्षा का ज्ञान»
    "2-799": {"ṭhitibhāginī paññā": "प्रज्ञा स्थिरता की भागी"},   # predicate: «तब प्रज्ञा स्थिरता की भागी होती है»
    "2-801": {"sukha": "सुखद",                  # sukhapaṭipadā «सुखद प्रगति»
              "paṭipadā": "प्रगति … ढंग"},         # catasso paṭipadā «प्रगति के चार ढंग»
    "2-806": {"paccayā": "के कारण",             # X-paccayā Y «X के कारण Y»
              "āyatana": "इंद्रिय-क्षेत्र",        # saḷāyatana «छह इंद्रिय-क्षेत्र»
              "nirodha": "समाप्त होना"},           # nirodhadhammaṃ «समाप्त होने के स्वभाव वाला»
    "2-808": {"nirodha": "समाप्ति"},             # saññāvedayitanirodha «पहचान और अनुभूति की समाप्ति»
    "2-809": {"upādāya": "अपेक्षा"},             # hetū paccayā upādāya «… उनकी अपेक्षा»
    "2-812": {"āyatana": "इंद्रिय-क्षेत्र"},       # āyatananānattaṃ «इंद्रिय-क्षेत्रों की विविधता»
    "2-815": {"hoti": "रहना"},                  # hoti tathāgato paraṃ maraṇā «मृत्यु के बाद तथागत रहते हैं»
    "2-816": {"rūpaṃ": "लगने वाला"},            # piyarūpaṃ / sātarūpaṃ «प्रिय / सुहावना लगने वाला»
    "2-827": {"saddhā": "श्रद्धावान"},           # saddhā (adj.) «श्रद्धावान»
    "2-828": {"amanasikārā": "मनोयोग न करना",   # «… पहचानों पर मनोयोग न करने से»
              "nirodhaṃ": "समाप्ति",             # saññāvedayitanirodhaṃ «… की समाप्ति»
              "sampatti": "सफलता",               # jhāyī: sampatti / vipatti «सफलता / विफलता»
              "dandhaṃ": "धीरे", "bahiddhā": "बाहर", "āyatanaṃ": "क्षेत्र",
              "samāpajjati": "प्रवेश करना",       # «धीरे / जल्दी प्रवेश करता है»
              "kusalo": "कुशल"},                  # samādhikusalo «… में कुशल»
    "2-829": {"dukkha": "दुःख"},                 # sukhadukkhappaṭisaṃvedī «सुख-दुःख का अनुभव»
    "2-831": {"anāsavaṃ": "मन के मैलों से रहित"},  # anāsavaṃ cetovimuttiṃ «मन के मैलों से रहित मन की मुक्ति»
    "2-782": {"hetukā": "मूल बनाने वाला",        # maggahetukā «मार्ग को मूल बनाने वाली»
              "ārammaṇā": "विषय बनाने वाला"},     # maggārammaṇā «मार्ग को विषय बनाने वाली»
    "2-784": {"uppannā": "उत्पन्न हो चुका"},     # matrix label «उत्पन्न हो चुकी होती है»
    "2-792": {"bahiddhā": "दूसरों",              # members of ajjhattabahiddhārammaṇā
              "bahiddhārammaṇā": "दूसरों … से संबंधित विषय वाला"},   # «स्वयं और दूसरों दोनों से संबंधित विषय वाली»
}
ALLOWED16 = {
    ("2-760", "nādaṃ"): "member of the one-word «सिंहनाद» (sīha-nādaṃ); the checker does not match inside a word",
    ("2-809", "gatiṃ"): "member of the one-word «सुगति» / «दुर्गति» (su-/dug-gatiṃ); the checker does not match inside a word",
    ("2-830", "gatiṃ"): "member of the one-word «सुगति» / «दुर्गति» (su-/dug-gatiṃ); the checker does not match inside a word",
}

# ============================================================================ 18-dhammahadayavibhango
SENSE18 = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर"}
T18 = {**COMMON}
for _p, _h in SENSE18.items():
    T18[_p] = _h
    T18[_p + "dhātu"] = f"{_h} का तत्व"
    T18[_p + "viññāṇa"] = f"{_h} की चेतना"
    T18[_p + "viññāṇadhātu"] = f"{_h} की चेतना का तत्व"
    T18[_p + "samphasso"] = f"{_h} का संपर्क"
for _p, _h in (("rasa", "स्वाद"), ("gandha", "गंध"), ("sadda", "ध्वनि"), ("phoṭṭhabba", "स्पर्श")):
    T18[_p + "dhātu"] = f"{_h} का तत्व"
for _n, _h in NUM.items():
    T18[_n + "indriyāni"] = T18[_n + "indriyā"] = f"{_h} क्षमता"
T18.update({
    # headings (notes-8-…-18: section and sub-headings)
    "hadaya": "सार", "dhamma": "परिघटना", "saṅgāhika": "समेटने वाला", "sabba": "सब कुछ",
    "ānuppatti": "न होना", "uppattānuppattivāro": "होने और न होने का खंड",
    "kāmadhātu": "इंद्रिय-सुखों का लोक", "rūpadhātu": "सूक्ष्म भौतिक लोक", "arūpadhātu": "अभौतिक लोक",
    "arūpa": "अभौतिक", "dassana": "दिखाने वाला", "dassanavāro": "दिखाने वाला खंड",
    "sattā": "प्राणी", "asañña": "पहचान-रहित", "antara": "भेद",
    "bhūmantaradassanavāro": "अस्तित्व के स्तरों के भेद को दिखाने वाला खंड",
    "uppādaka": "जन्म देने वाला", "uppādakakamma": "जन्म देने वाला कर्म", "uppādakakammaṃ": "जन्म देने वाला कर्म",
    "pamāṇa": "अवधि", "pamāṇaṃ": "अवधि", "āyuppamāṇa": "आयु की अवधि", "āyuppamāṇaṃ": "आयु की अवधि",
    "abhiññeyyādivāro": "प्रत्यक्ष जानने योग्य आदि का खंड", "ādi": "आदि",
    "sārammaṇānārammaṇavāro": "विषय वाले और विषय से रहित का खंड", "ārammaṇa": "विषय",
    "diṭṭhasutādidassanavāro": "देखे सुने आदि को दिखाने वाला खंड",
    "tikādidassanavāro": "तीन-तीन आदि के वर्गीकरणों को दिखाने वाला खंड",
    "vipākattikaṃ": "कर्म-फल का तीन-तीन वर्गीकरण", "upādinna": "कर्म से उत्पन्न", "lokiya": "लौकिक",
    # 2-978 … 2-998 (the counted lists)
    "phassā": "संपर्क", "samphasso": "संपर्क", "aṭṭhārasa": "अठारह", "aṭṭhārasa dhātuyo": "अठारह तत्व",
    "saccāni": "सत्य", "saccaṃ": "सत्य", "saccā": "सत्य", "dvādasāyatanāni": "बारह इंद्रिय-क्षेत्र",
    "bāvīsatindriyāni": "बाईस क्षमता", "bāvīsatindriyā": "बाईस क्षमता",
    "aññindriyaṃ": "पूर्ण ज्ञान की क्षमता", "aññātāvindriyaṃ": "पूर्ण ज्ञान पा चुके की क्षमता",
    "anaññātaññassāmītindriyaṃ": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
    "kāya": "शरीर", "dukkha": "दुःख", "dukkhasaccaṃ": "दुःख का सत्य", "samudaya": "उत्पत्ति", "nirodha": "अंत",
    "lobho": "लोभ", "doso": "द्वेष", "moho": "मोह", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    "kusalahetu": "हितकर मूल", "kusalahetū": "हितकर मूल", "akusalahetu": "हानिकर मूल", "akusalahetū": "हानिकर मूल",
    "abyākatahetū": "नैतिक रूप से अनिर्धारित मूल",
    "kusalānaṃ": "हितकर", "dhammānaṃ": "परिघटना", "kusalānaṃ vā dhammānaṃ": "हितकर … परिघटना",
    "kusalānaṃ dhammānaṃ": "हितकर … परिघटना", "vipākato": "कर्म के फल रूपी",
    "kiriyābyākatesu": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित",
    "kabaḷīkārāhāro": "कौर-कौर खाया जाने वाला भोजन", "phassāhāro": "संपर्क रूपी आहार",
    "manosañcetanāhāro": "मानसिक इरादा रूपी आहार", "viññāṇāhāro": "चेतना रूपी आहार",
    "manodhātusamphasso": "मन के तत्व का संपर्क", "manoviññāṇadhātusamphasso": "मन की चेतना के तत्व का संपर्क",
    "manodhātusamphassa": "मन के तत्व का संपर्क", "manodhātusamphassajā": "मन के तत्व के संपर्क से उत्पन्न",
    "manoviññāṇadhātusamphassa": "मन की चेतना के तत्व का संपर्क",
    "manoviññāṇadhātusamphassajā": "मन की चेतना के तत्व के संपर्क से उत्पन्न",
    "manoviññāṇadhātusamphassajā vedanā": "मन की चेतना के तत्व के संपर्क से उत्पन्न अनुभूति",
    "manoviññāṇadhātusamphassajā saññā": "मन की चेतना के तत्व के संपर्क से उत्पन्न पहचान",
    "manoviññāṇadhātusamphassajā cetanā": "मन की चेतना के तत्व के संपर्क से उत्पन्न इरादा",
    "kāmadhātuyā": "इंद्रिय-सुखों का लोक", "rūpadhātuyā": "सूक्ष्म भौतिक लोक", "arūpadhātuyā": "अभौतिक लोक",
    "dhātuyā": "लोक", "āyatanā": "इंद्रिय-क्षेत्र", "cittānaṃ": "मन",
    # numerals + noun (2-1000 …): numeral + singular noun (pi-3 Dvādasāyatanāni = बारह इंद्रिय-क्षेत्र)
    "soḷasa": "सोलह", "soḷasa dhātuyo": "सोलह तत्व", "dasāyatanā": "दस इंद्रिय-क्षेत्र",
    "dasāyatanāni": "दस इंद्रिय-क्षेत्र", "ekādasāyatanāni": "ग्यारह इंद्रिय-क्षेत्र",
    "ekādasa": "ग्यारह", "ekādasa dhātuyo": "ग्यारह तत्व", "dasa": "दस", "dasa dhātuyo": "दस तत्व",
    "pannarasa": "पंद्रह", "pannarasa dhātuyo": "पंद्रह तत्व", "terasa": "तेरह",
    "aṭṭhārasannaṃ": "अठारह", "aṭṭhārasannaṃ dhātūnaṃ": "अठारह तत्व", "dhātūnaṃ": "तत्व",
    "dvādasannaṃ": "बारह", "dvādasannaṃ āyatanānaṃ": "बारह इंद्रिय-क्षेत्र", "saccānaṃ": "सत्य",
    "indriyā": "क्षमता", "cittā": "मन",
    "dhātuyo kāmadhātupariyāpannā": "तत्व इंद्रिय-सुखों के लोक में समाया हुआ",
    "dhātuyo pariyāpannā": "तत्व अस्तित्व के लोकों में समाया हुआ",
    # 2-1007 … 2-1019 (birth moment)
    "pātubhavanti": "प्रकट होना", "pātubhavati": "प्रकट होना", "khaṇe": "क्षण", "upapatti": "जन्म",
    "upapattikkhaṇe": "जन्म का क्षण",
    "upapattikkhaṇe ekādasāyatanāni": "जन्म का क्षण … ग्यारह इंद्रिय-क्षेत्र",
    "upapattikkhaṇe dasāyatanāni": "जन्म का क्षण … दस इंद्रिय-क्षेत्र",
    "upapattikkhaṇe ekādasa": "जन्म का क्षण … ग्यारह", "upapattikkhaṇe ekādasa dhātuyo": "जन्म का क्षण … ग्यारह तत्व",
    "upapattikkhaṇe dasa": "जन्म का क्षण … दस", "upapattikkhaṇe dasa dhātuyo": "जन्म का क्षण … दस तत्व",
    "upapattikkhaṇe dasindriyāni": "जन्म का क्षण … दस क्षमता",
    "upapattikkhaṇe terasindriyāni": "जन्म का क्षण … तेरह क्षमता",
    "kāmāvacarānaṃ": "इंद्रिय-सुखों के लोक का", "āvacarānaṃ": "लोक का", "devānaṃ": "देवता",
    "kappikānaṃ": "कल्प के आरंभ का", "manussānaṃ": "मनुष्य", "petānaṃ": "प्रेत", "asurānaṃ": "असुर",
    "tiracchānagatānaṃ": "पशु", "nerayikānaṃ": "नरक का प्राणी", "opapātikānaṃ": "स्वतः जन्म लेने वाला",
    "opapātikānaṃ petānaṃ": "स्वतः जन्म लेने वाला प्रेत", "opapātikānaṃ asurānaṃ": "स्वतः जन्म लेने वाला असुर",
    "opapātikānaṃ tiracchānagatānaṃ": "स्वतः जन्म लेने वाला पशु",
    "paripuṇṇāyatanānaṃ": "पूर्ण इंद्रिय-क्षेत्रों वाला", "āyatanānaṃ": "इंद्रिय-क्षेत्र",
    "jaccandhānaṃ": "जन्म से अंधा", "badhirānaṃ": "बहरा", "gabbhaseyyakānaṃ": "गर्भ में रहने वाला",
    "sattānaṃ": "प्राणी", "sahetukānaṃ": "मूल वाला", "sampayuttānaṃ": "जुड़ा", "vippayuttānaṃ": "अलग",
    "ñāṇavippayuttānaṃ": "ज्ञान से अलग", "napuṃsakānaṃ": "नपुंसक", "avasesānaṃ": "शेष",
    "vipāka": "कर्म-फल रूपी", "vipākahetu": "कर्म-फल रूपी मूल",
    "asaññasattānaṃ": "पहचान-रहित", "asaññasattānaṃ devānaṃ": "पहचान-रहित देवता",
    "rūpajīvitindriyaṃ": "भौतिक जीवन-क्षमता", "ahetukā": "मूल से रहित", "anāhārā": "आहार से रहित",
    "aphassakā": "संपर्क से रहित", "avedanakā": "अनुभूति से रहित", "asaññakā": "पहचान से रहित",
    "acetanakā": "इरादे से रहित", "acittakā": "मन से रहित",
    # 2-1020 (bhūmantara definitions, pi-1 ^1-1287 …)
    "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacarā": "अभौतिक लोक से संबंधित", "āvacarā": "लोक से संबंधित",
    "kāmāvacarā dhammā": "इंद्रिय-सुखों के लोक से संबंधित परिघटना", "dhammā": "परिघटना",
    "apariyāpannā dhammā": "अस्तित्व के लोकों में न समाई हुई परिघटना",
    "nirayaṃ": "नरक", "pariyantaṃ": "सीमा", "karitvā": "बनाकर", "uparito": "ऊपर", "antare": "बीच",
    "deve": "देवता", "deve antokaritvā": "देवता … भीतर रखकर", "akaniṭṭhe deve": "अकनिष्ठ देवता",
    "paranimmitavasavattī": "दूसरों की रची गई चीज़ों पर अधिकार रखने वाला", "vasavattī": "अधिकार रखने वाला",
    "paranimmitavasavattī deve": "दूसरों की रची गई चीज़ों पर अधिकार रखने वाला देवता",
    "upapannassa": "वहाँ जन्मा व्यक्ति", "diṭṭhadhamma": "इसी जीवन", "vihārissa": "रहने वाला",
    "sukhavihārissa": "सुख से रहने वाला", "āyatanūpage": "क्षेत्र में पहुँचा",
    "ākāsānañcāyatanūpage": "अनंत आकाश के क्षेत्र में पहुँचा",
    "nevasaññānāsaññāyatanūpage": "न पहचान न अ-पहचान के क्षेत्र में पहुँचा",
    "kusalākusalabyākatā": "हितकर हानिकर और नैतिक रूप से अनिर्धारित", "maggā": "मार्ग", "phalāni": "फल",
    "asaṅkhatā": "अनिर्मित", "asaṅkhatā ca dhātu": "अनिर्मित तत्व",
    # 2-1021 … 2-1029 (gods, life spans, verses)
    "devā": "देवता", "sammuti": "लोक-मान्यता", "visuddhi": "शुद्धि", "rājāno": "राजा", "deviyo": "रानी",
    "kumārā": "राजकुमार", "mahārājike": "महाराजा", "tadupari": "उनसे ऊपर", "arahanto": "अर्हत्",
    "dānaṃ": "दान", "sīlaṃ": "सदाचार", "samādiyitvā": "ग्रहण करके", "uposatha": "उपवास-व्रत", "katvā": "करके",
    "upapajjanti": "जन्म लेना", "mahāsālānaṃ": "धनी", "khattiya": "क्षत्रिय", "brāhmaṇa": "ब्राह्मण",
    "gahapati": "गृहस्थ", "tāvatiṃsānaṃ": "तैंतीस देवता", "yāmānaṃ devānaṃ": "याम देवता",
    "tusitānaṃ": "तुषित", "tusitānaṃ devānaṃ": "तुषित देवता", "nimmāna": "सृजन", "ratīnaṃ": "आनंद लेने वाला",
    "nimmānaratīnaṃ devānaṃ": "सृजन में आनंद लेने वाला देवता",
    "vasavattīnaṃ": "अधिकार रखने वाला",
    "paranimmitavasavattīnaṃ": "दूसरों की रची गई चीज़ों पर अधिकार रखने वाला",
    "paranimmitavasavattīnaṃ devānaṃ": "दूसरों की रची गई चीज़ों पर अधिकार रखने वाला देवता",
    "sataṃ": "सौ", "mahārājikānaṃ": "महाराजा", "mānusakāni": "मनुष्य", "paññāsa": "पचास", "vassāni": "वर्ष",
    "rattindivo": "दिन-रात", "rattiyo": "रात", "rattiyo māso": "रातों का एक महीना", "tiṃsa": "तीस",
    "māso": "महीना", "saṃvaccharo": "वर्ष", "dvādasamāsiyo saṃvaccharo": "बारह महीनों का एक वर्ष",
    "dvādasa": "बारह", "dibbāni": "दिव्य", "vassasatāni": "सौ वर्ष", "satāni": "सौ", "sahassaṃ": "हज़ार",
    "manussānaṃ gaṇanāya": "मनुष्यों की गणना", "gaṇanāya": "गणना",
    "mānusakaṃ vassasataṃ": "मनुष्यों के … सौ वर्ष", "koṭiyo": "करोड़", "aṭṭhavīsañca": "अट्ठाईस",
    "samiddhino": "भरपूर", "saṅkhāto": "गिना", "pakāsitāti": "बताना",
    "bhāvetvā": "अभ्यास करना", "kappassa": "कल्प", "kappā": "कल्प", "majjhimaṃ": "मध्यम",
    "brahmānaṃ devānaṃ": "ब्रह्मा … देवता", "mahābrahmānaṃ": "महाब्रह्मा", "mahābrahmānaṃ devānaṃ": "महाब्रह्मा देवता",
    "purohitānaṃ": "पुरोहित", "pārisajjānaṃ": "सभा",
    "appamāṇābhānaṃ": "असीम आभा वाला", "ābhānaṃ": "आभा", "ābhassarānaṃ": "दीप्तिमान आभा वाला",
    "subhānaṃ": "शोभा", "kiṇhānaṃ": "पूर्ण", "appamāṇa": "असीम", "catusaṭṭhi": "चौंसठ", "bāttiṃsa": "बत्तीस",
    "catutthaṃ jhānaṃ": "चौथा ध्यान", "nānattatā": "भिन्नता", "manasikāra": "मनोयोग", "chanda": "चाह",
    "paṇidhi": "आकांक्षा", "abhinīhāra": "मन को लक्ष्य की ओर मोड़ना",
    "vehapphalānaṃ": "महान फल वाला", "vehapphalānaṃ devānaṃ": "महान फल वाला देवता",
    "avihānaṃ": "अपने लोक से न डिगने वाला", "avihānaṃ devānaṃ": "अपने लोक से न डिगने वाला देवता",
    "atappānaṃ": "न तपने वाला", "atappānaṃ devānaṃ": "न तपने वाला देवता",
    "sudassānaṃ": "सुंदर दिखने वाला", "sudassānaṃ devānaṃ": "सुंदर दिखने वाला देवता",
    "sudassīnaṃ devānaṃ": "सुंदर देखने वाला देवता", "akaniṭṭhānaṃ devānaṃ": "अकनिष्ठ देवता",
    "āyatanūpagānaṃ": "क्षेत्र में पहुँचा", "ākāsānañcāyatanūpagānaṃ": "अनंत आकाश के क्षेत्र में पहुँचा",
    "viññāṇañcāyatanūpagānaṃ": "अनंत चेतना के क्षेत्र में पहुँचा",
    "ākiñcaññāyatanūpagānaṃ": "कुछ भी न होने के क्षेत्र में पहुँचा",
    "nevasaññānāsaññāyatanūpagānaṃ": "न पहचान न अ-पहचान के क्षेत्र में पहुँचा",
    "kappasahassaṃ": "हज़ार कल्प", "kappasahassāni": "हज़ार कल्प", "sahassāni": "हज़ार",
    "vīsati": "बीस", "cattārīsa": "चालीस", "saṭṭhi": "साठ", "caturāsīti": "चौरासी",
    "ukkhittā": "ऊपर उठना", "puñña": "पुण्य", "tejena": "तेज", "gatiṃ": "गति", "gatā": "प्राप्त होना",
    "bhavaggatampi": "अस्तित्व का शिखर", "punāgacchanti": "फिर … लौट आना", "duggatiṃ": "दुर्गति",
    "dīghāyukā": "लंबी आयु वाला", "cavanti": "मरना", "āyusaṅkhayā": "आयु का क्षय", "saṅkhayā": "क्षय",
    "koci": "कोई", "bhavo": "अस्तित्व", "nicco": "नित्य", "mahesinā": "महान ऋषि", "tasmā": "इसलिए",
    "dhīrā": "धीर", "nipakā": "विवेकी", "nipuṇā": "कुशल", "cintakā": "चिंतन करने वाला",
    "jarā": "बुढ़ापा", "jarāmaraṇa": "बुढ़ापा और मृत्यु", "maraṇa": "मृत्यु", "mokkhāya": "मुक्ति",
    "bhāventi": "अभ्यास करना", "uttamaṃ": "उत्तम", "maggaṃ": "मार्ग", "bhāvayitvā": "अभ्यास करना",
    "suciṃ": "शुद्ध", "nibbānogadhagāminaṃ": "निर्वाण में डुबकी लगाने की ओर ले जाने वाला",
    "āsave": "मन के मैल", "pariññāya": "पूरी तरह समझना", "parinibbanti": "पूर्ण निर्वाण पाना",
    "anāsavāti": "मन के मैलों से रहित",
    # 2-1030 … 2-1044 (abhiññeyya …, sārammaṇa …, diṭṭha …, tika/duka)
    "abhiññeyyā": "प्रत्यक्ष जानने योग्य", "abhiññeyyo": "प्रत्यक्ष जानने योग्य",
    "pariññeyyā": "पूरी तरह समझे जाने योग्य", "pariññeyyo": "पूरी तरह समझे जाने योग्य",
    "pahātabbā": "छोड़े जाने योग्य", "pahātabbo": "छोड़े जाने योग्य",
    "bhāvetabbā": "विकसित किए जाने योग्य", "bhāvetabbo": "विकसित किए जाने योग्य",
    "sacchikātabbā": "साक्षात्कार करने योग्य", "sacchikātabbo": "साक्षात्कार करने योग्य",
    "ārammaṇā": "विषय बनाने वाला",
    "sārammaṇārammaṇā": "विषय वाली परिघटनाओं को विषय बनाने वाला",
    "anārammaṇārammaṇā": "विषय से रहित परिघटनाओं को विषय बनाने वाला",
    "sutā": "सुना हुआ", "suto": "सुना हुआ", "mutā": "अनुभव किया हुआ", "muto": "अनुभव किया हुआ",
    "viññātā": "जाना हुआ", "viññāto": "जाना हुआ",
    "nevavipākanavipākadhammadhammā": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "nevavipākanavipākadhammadhammo": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "vicārā": "सतत विचार", "lokiyā": "लौकिक", "lokuttarā": "लोकोत्तर", "upādinnā": "कर्म से उत्पन्न",
    "vitakkaṃ": "आरंभिक विचार", "abhiññā": "प्रत्यक्ष जानना", "pakaraṇaṃ": "ग्रंथ",
    "vibhaṅgapakaraṇaṃ": "विस्तृत विश्लेषण ग्रंथ",
})
# keywords whose sense the segment decides (realm vs element, matter vs fine-material vs visible form …)
ALT18 = {
    "dhātu": ["तत्व", "लोक"],
    "rūpa": ["भौतिक रूप", "सूक्ष्म भौतिक", "दृश्य रूप", "भौतिक"],
    "rūpadhātu": ["दृश्य रूप का तत्व", "सूक्ष्म भौतिक लोक"],   # the element in the lists, else the realm
    "dhamma": ["परिघटना", "मन के विषय"],
    "tikaṃ": ["तीन-तीन के वर्गीकरण", "तीन-तीन वर्गीकरण"],
    "dukaṃ": ["दो-दो के वर्गीकरण", "दो-दो वर्गीकरण"],
    "āhāro": ["भोजन", "आहार"],
}
OVR18 = {
    "2-1023": {"sabba": "सभी",             # sabbakāmasamiddhino «सभी इंद्रिय-सुखों से भरपूर»
               "kāmāvacarā": "इंद्रिय-सुखों के लोक का"},   # verse: «इंद्रिय-सुखों के लोक के ये छह देवलोक»
    "2-1043": {"rūpā": "भौतिक"},           # «Dasāyatanā rūpā» = «… भौतिक हैं»
}
_INFL = "regular inflection the checker does not model"
ALLOWED18 = {
    ("2-1000", "dhātuyo kāmadhātupariyāpannā"): f"text «तत्व … समाए हुए»: समाया ~ समाए is {_INFL}",
    ("2-1006", "dhātuyo pariyāpannā"): f"text «तत्व … समाए हुए»: समाया ~ समाए is {_INFL}",
    ("2-1029", "punāgacchanti"): f"text «फिर दुर्गति में लौट आते हैं»: आना ~ आते is {_INFL}",
    ("2-1036", "mutā"): f"text «अनुभव किए हुए»: किया ~ किए is {_INFL}",
    ("2-1039", "Kabaḷīkāro"): f"text «कौर-कौर खाए जाने वाले भोजन»: खाया ~ खाए is {_INFL}",
}


def make_resolver(ch, table, ovr, alt=None):
    """alt: {kw (lower-case first letter): [v1, v2, …]} for a keyword whose sense the segment decides
    (dhātu तत्व/लोक, rūpa भौतिक रूप/सूक्ष्म भौतिक/दृश्य रूप …): the first value the segment's Hindi has."""
    full = {**PI2, **table}
    alt = alt or {}
    cache = {}

    def resolver(bid, kw, kws):
        if not cache:
            cache.update(read_hindi(ch))
        o = ovr.get(bid, {})
        if kw in o:
            return o[kw]
        k = kw[:1].lower() + kw[1:]
        if k in alt:
            text = cache.get(bid, "")
            cands = alt[k]
            if kw != k or (k[:1].upper() + k[1:]) not in kws:
                pass
            else:   # both «Rūpa» (Rūpakkhandho, sentence-initial) and «rūpa» (rūpadhātu-…): the lower-case one
                cands = cands[1:]                         # is the other sense
            for v in cands:
                if present(v, text):
                    return v
            return cands[0]
        return pi2_value(kw, kws, full, bid, cache.get(bid))
    return resolver


def _alts(tok):
    """Regular inflected forms the shared checker does not model: short-stem infinitives (आना ~ आता/आते/आकर),
    -या participles (समाया ~ समाए/समाई, किया ~ किए/की, खाया ~ खाए)."""
    out = [tok]
    if len(tok) <= 2:                                  # फल ~ फलों, सब ~ सबकी (two-letter words are matched exactly)
        out += [tok + e for e in ("ों", "ो", "े", "ें", "ी", "की", "के", "का")]
    if tok.endswith("ना"):
        st = tok[:-2]
        out += [st] + [st + e for e in ("ता", "ते", "ती", "तीं", "कर", "ए", "ई", "या", "ने", "ओ", "एँ",
                                        "ेंगे", "ेगा", "ेगी", "ें", "े")]
        if tok == "करना":
            out += ["की", "किया", "किए"]
    if tok.endswith("या"):
        out += [tok[:-2] + "ए", tok[:-2] + "ई", tok[:-2] + "ये", tok[:-2] + "यी"]
        if tok == "किया":
            out += ["की", "किए"]
    return out


def present_ext(v, text):
    """(matched form) when v is present up to the regular inflection of _alts, else None."""
    import itertools
    found = []
    for part in [p for p in v.replace(" / ", " … ").split(" … ") if p.strip()]:
        toks = part.split()
        if len(toks) > 14:
            return None
        for combo in itertools.product(*[_alts(t) for t in toks]):
            cand = " ".join(combo)
            if present(cand, text):
                found.append(cand)
                break
        else:
            return None
    return " … ".join(found)


def auto_allowed(ch, base):
    """Presence misses that are regular inflection (present_ext) become listed exceptions with a reason."""
    from map_sample_hi import HERE
    hi = read_hindi(ch)
    allowed = dict(base)
    for line in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v != NDE and not present(v, hi.get(bid, "")) and (bid, kw) not in allowed:
                m = present_ext(v, hi.get(bid, ""))
                if m:
                    allowed[(bid, kw)] = f"text «{m}»: regular inflection the checker does not model"
    return allowed


RESOLVERS = {
    "5-indriyavibhango": make_resolver("5-indriyavibhango", T5, OVR5),
    "16-nanavibhango": make_resolver("16-nanavibhango", T16, OVR16, ALT16),
    "18-dhammahadayavibhango": make_resolver("18-dhammahadayavibhango", T18, OVR18, ALT18),
}
ALLOWED = {"5-indriyavibhango": ALLOWED5, "16-nanavibhango": ALLOWED16, "18-dhammahadayavibhango": ALLOWED18}

if __name__ == "__main__":
    for ch in (sys.argv[1:] or list(RESOLVERS)):
        build_part(ch, RESOLVERS[ch])
        verify(ch, allowed=auto_allowed(ch, ALLOWED[ch]))
