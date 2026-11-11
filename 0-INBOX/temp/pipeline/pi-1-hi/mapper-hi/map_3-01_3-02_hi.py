"""Map 3-01-rupakandam and 3-02-rupakandam keywords to the Hindi translation.

Own table RUPA (material-form vocabulary, as the builders build_3-01_hi.py / build_3-02_3-03_hi.py
rendered it) + context rules + per-segment overrides, falling back to CH2 (map_common_hi).

usage: python -I -X utf8 map_3-01_3-02_hi.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import CH2, NDE, GAP, ch2_value, lc, build_part, verify  # noqa: E402

PARTS = ["3-01-rupakandam", "3-02-rupakandam"]

R = "भौतिक रूप"
RUPA = {
    # headings, closings
    "kaṇḍaṃ": "अध्याय", "kaṇḍe": "अध्याय", "uddeso": "रूपरेखा", "mātikā": "मूल सूची",
    "dukaṃ": "दो-दो के वर्गीकरण", "duka": "दो-दो के वर्गीकरण",
    "dasakaṃ": "दस-दस के वर्गीकरण", "dasa": "दस",
    "ekādasakaṃ": "ग्यारह-ग्यारह के वर्गीकरण", "ekādasa": "ग्यारह",
    "vibhatti": "वर्गीकरण", "niddeso": "व्याख्या", "bhājanīyaṃ": "विश्लेषण",
    "bhāṇa": "पाठ", "vāro": "खंड",
    "saṅgaho": "वर्गीकरण", "rūpasaṅgaho": f"{R} का वर्गीकरण",
    "vidhena": "प्रकार", "catubbidhena": "चार प्रकार", "chabbidhena": "छह प्रकार",
    "tattha": "इनमें से", "eva": "ही",
    "yo": "जो", "yā": "जो", "yaṃ": "जो",
    # 1-583 uddesa
    "kiriyā": "केवल क्रिया रूपी", "kusala": "हितकर", "kusalā nākusalā": "न हितकर न हानिकर",
    "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    "abyākatā": "नैतिक रूप से अनिर्धारित", "dhammā abyākatā": "नैतिक रूप से अनिर्धारित परिघटना",
    "asaṅkhatā": "अनिर्मित", "asaṅkhatā ca dhātu": "अनिर्मित तत्व",
    "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarā": "अभौतिक लोक से संबंधित",
    "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित", "avacarā": "लोक से संबंधित", "arūpa": "अभौतिक",
    "vedanā": "अनुभूति", "saññā": "पहचान",
    # ekaka list (matrix items, masc. sg.)
    "hetu": "मूल", "hetukaṃ": "मूलों वाला", "vippayuttaṃ": "अलग", "cittavippayuttaṃ": "मन से अलग",
    "saṅkhataṃ": "निर्मित", "lokiyaṃ": "लौकिक",
    "sāsavaṃ": "मन के मैलों का विषय बनने वाला", "āsavaṃ": "मन के मैल",
    "saṃyojaniyaṃ": "बंधनों का विषय बनने वाला", "ganthaniyaṃ": "गाँठों का विषय बनने वाला",
    "oghaniyaṃ": "बाढ़ों का विषय बनने वाला", "yoganiyaṃ": "जकड़नों का विषय बनने वाला",
    "nīvaraṇiyaṃ": "बाधाओं का विषय बनने वाला", "parāmaṭṭhaṃ": "ग़लत धारणा का विषय बनने वाला",
    "upādāniyaṃ": "आसक्ति का विषय बनने वाला", "saṃkilesikaṃ": "क्लेशों की ओर ले जाने वाला",
    "abyākataṃ": "नैतिक रूप से अनिर्धारित", "ārammaṇaṃ": "विषय", "cetasikaṃ": "मन का सहचर",
    "vipākadhamma": "कर्म-फल उत्पन्न करने वाला", "asaṃkiliṭṭha": "क्लेशों से मलिन न होने वाला",
    "vitakka": "आरंभिक विचार", "vicāra": "सतत विचार",
    "sahagataṃ": "के साथ होने वाला", "pītisahagataṃ": "उल्लास के साथ होने वाला",
    "sukhasahagataṃ": "सुख के साथ होने वाला", "upekkhāsahagataṃ": "समभाव के साथ होने वाला",
    "pīti": "उल्लास", "sukha": "सुख", "dukkha": "दुःखद", "upekkhā": "समभाव",
    "dassanena": "सत्य-दर्शन", "pahātabbaṃ": "छोड़ा जाने वाला",
    "ācaya": "संचय", "apacaya": "संचय घटाना", "gāmi": "की ओर ले जाने वाला",
    "sekkha": "सीखने के चरण का", "asekkhaṃ": "सीखना पूरा होने के चरण का",
    "parittaṃ": "सीमित", "kāmāvacaraṃ": "इंद्रिय-सुखों के लोक से संबंधित", "avacaraṃ": "लोक से संबंधित",
    "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacaraṃ": "अभौतिक लोक से संबंधित",
    "apariyāpannaṃ": "अस्तित्व के लोकों में न समाई हुई परिघटना",
    "niyataṃ": "निश्चित",                      # of aniyataṃ «अनिश्चित» (fused negative)
    "niyyānikaṃ": "मुक्ति की ओर ले जाने वाला", "uppannaṃ": "उत्पन्न हो चुका",
    "viññāṇehi": "चेतना", "viññeyyaṃ": "जाना जा सकने वाला", "aniccaṃ": "अनित्य",
    "jarā": "बुढ़ापा", "abhibhūtaṃ": "ग्रस्त",
    "upādāya": "व्युत्पन्न", "upādāya rūpaṃ": f"व्युत्पन्न {R}",
    "bhūtā": "महाभूत", "mahābhūtā": "महाभूत", "bhūtaṃ": "महाभूत", "mahābhūtaṃ": "महाभूत",
    "bhūtānaṃ": "महाभूत", "mahābhūtānaṃ": "महाभूत", "bhūtehi": "महाभूत", "mahābhūtehi": "महाभूत",
    # classification predicates (matrix items, masc. sg.)
    "rūpaṃ": R,
    "upādā": "व्युत्पन्न", "upādiṇṇaṃ": "कर्म से उत्पन्न", "upādiṇṇa": "कर्म से उत्पन्न",
    "upādiṇṇupādāniyaṃ": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
    "anupādiṇṇupādāniyaṃ": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला",
    "sanidassanaṃ": "दिखाई देने वाला", "anidassanaṃ": "दिखाई न देने वाला", "anidassana": "दिखाई न देने वाला",
    "sappaṭighaṃ": "टकराव वाला", "appaṭighaṃ": "टकराव से रहित",
    "anidassanaappaṭighaṃ": "दिखाई न देने वाला और टकराव से रहित",
    "rūpaṃ sappaṭighaṃ": f"{R} टकराव वाला",
    "samuṭṭhānaṃ": "उत्पन्न", "cittasamuṭṭhānaṃ": "मन से उत्पन्न",
    "cittasahabhu": "मन के साथ-साथ होने वाला",
    "anuparivatti": "अनुसरण करने वाला", "cittānuparivatti": "मन का अनुसरण करने वाला",
    "rūpaṃ cittasamuṭṭhānaṃ": f"{R} मन से उत्पन्न", "rūpaṃ cittasahabhu": f"{R} मन के साथ-साथ होने वाला",
    "rūpaṃ cittānuparivatti": f"{R} मन का अनुसरण करने वाला",
    "ajjhattikaṃ": "आंतरिक", "bāhiraṃ": "बाह्य", "oḷārikaṃ": "स्थूल", "sukhumaṃ": "सूक्ष्म",
    "indriyaṃ": "क्षमता", "indriyānaṃ": "इंद्रिय", "viññatti": "प्रकट अभिव्यक्ति",
    "citta": "मन", "cittassa": "मन",
    # sense bases, elements, faculties
    "cakkhu": "आँख", "cakkhuṃ": "आँख", "cakkhunā": "आँख", "cakkhumhi": "आँख",
    "sota": "कान", "sotaṃ": "कान", "sotena": "कान", "sotamhi": "कान",
    "ghāna": "नाक", "ghānaṃ": "नाक", "ghānena": "नाक", "ghānamhi": "नाक",
    "jivhā": "जीभ", "jivhaṃ": "जीभ", "jivhāya": "जीभ",
    "kāya": "शरीर", "kāyo": "शरीर", "kāyaṃ": "शरीर", "kāyena": "शरीर", "kāyamhi": "शरीर", "kāyassa": "शरीर",
    "mano": "मन",
    "rūpamhi": "दृश्य रूप", "sadda": "ध्वनि", "saddaṃ": "ध्वनि", "saddo": "ध्वनि", "saddamhi": "ध्वनि",
    "gandha": "गंध", "gandhaṃ": "गंध", "gandho": "गंध", "gandhamhi": "गंध",
    "rasa": "स्वाद", "rasaṃ": "स्वाद", "raso": "स्वाद", "rasamhi": "स्वाद",
    "phoṭṭhabba": "स्पर्श", "phoṭṭhabbaṃ": "स्पर्श", "phoṭṭhabbo": "स्पर्श", "phoṭṭhabbamhi": "स्पर्श",
    "dhātu": "तत्व", "dhātūnaṃ": "वस्तु", "dhamma": "मन के विषय",
    "dhammāyatana": "मन के विषयों का इंद्रिय-क्षेत्र",
    "manodhātu": "मन का तत्व", "manoviññāṇa": "मन की चेतना", "manoviññāṇadhātu": "मन की चेतना का तत्व",
    "itthindriyaṃ": "स्त्रीत्व की क्षमता", "purisindriyaṃ": "पुरुषत्व की क्षमता",
    "jīvitindriyaṃ": "जीवन-क्षमता", "jīvita": "जीवन",
    "vacī": "वाणी", "kāyaviññatti": "शरीर द्वारा प्रकट अभिव्यक्ति", "vacīviññatti": "वाणी द्वारा प्रकट अभिव्यक्ति",
    "ākāsa": "आकाश", "ākāsadhātu": "आकाश तत्व", "āpo": "जल", "āpodhātu": "जल तत्व",
    "pathavī": "पृथ्वी", "pathavīdhātu": "पृथ्वी तत्व", "tejo": "अग्नि", "tejodhātu": "अग्नि तत्व",
    "vāyo": "वायु", "vāyodhātu": "वायु तत्व",
    "lahutā": "हल्कापन", "rūpassa lahutā": f"{R} का हल्कापन",
    "mudutā": "मृदुता", "rūpassa mudutā": f"{R} की मृदुता",
    "kammaññatā": "कार्य-योग्यता", "rūpassa kammaññatā": f"{R} की कार्य-योग्यता",
    "rūpassa upacayo": f"{R} की वृद्धि", "santati": "धारा", "rūpassa santati": f"{R} की धारा",
    "jaratā": "बुढ़ापा", "rūpassa jaratā": f"{R} का बुढ़ापा",
    "aniccatā": "अनित्यता", "rūpassa aniccatā": f"{R} की अनित्यता",
    "rūpassa na lahutā": f"{R} का हल्कापन नहीं", "rūpassa na mudutā": f"{R} की मृदुता नहीं",
    "rūpassa na kammaññatā": f"{R} की कार्य-योग्यता नहीं", "rūpassa na upacayo": f"{R} की वृद्धि नहीं",
    "rūpassa na santati": f"{R} की धारा नहीं", "rūpassa na jaratā": f"{R} का बुढ़ापा नहीं",
    "rūpassa na aniccatā": f"{R} की अनित्यता नहीं",
    "kabaḷīkāro": "कौर-कौर खाया जाने वाला", "āhāro": "भोजन",
    "kabaḷīkāro āhāro": "कौर-कौर खाया जाने वाला भोजन",
    # contact chains
    "samphassajāya": "संपर्क से उत्पन्न", "vedanāya": "अनुभूति", "samphassajāya vedanāya": "संपर्क से उत्पन्न अनुभूति",
    "saññāya": "पहचान", "cetanāya": "इरादा", "cetanā": "इरादा",
    "samphassaṃ": "संपर्क वाला",
    # lists (^1-586 … ^1-593)
    "sutaṃ": "सुना हुआ", "mutaṃ": "अनुभव किया हुआ", "viññātaṃ": "जाना हुआ",
    "viññeyyaṃ rūpaṃ": f"जाना जा सकने वाला {R}",
    # pasāda formula (3-02)
    "pasādo": "संवेदनशीलता", "upādāya pasādo": "व्युत्पन्न संवेदनशीलता", "attabhāva": "व्यक्तिगत अस्तित्व",
    "anidassano": "दिखाई न देने वाला", "sappaṭigho": "टकराव वाला",
    "anidassano sappaṭigho": "दिखाई न देने वाला और टकराव वाला",
    "anidassanaṃ sappaṭighaṃ": "दिखाई न देने वाला और टकराव वाला",
    "anidassanasappaṭighaṃ": "दिखाई न देने वाला और टकराव वाला",
    "anidassanena": "दिखाई न देने वाला", "anidassanena sappaṭighena": "दिखाई न देने वाला और टकराव वाला",
    "anidassanamhi": "दिखाई न देने वाला", "sappaṭighamhi": "टकराव वाला",
    "anidassanamhi sappaṭighamhi": "दिखाई न देने वाला और टकराव वाला",
    "sanidassanamhi": "दिखाई देने वाला", "sanidassanaṃ sappaṭighaṃ": "दिखाई देने वाला और टकराव वाला",
    "sappaṭighaṃ paṭihaññi": f"टकराव वाला{GAP}टकरा चुका", "sappaṭigho paṭihaññi": f"टकराव वाला{GAP}टकरा चुका",
    "paṭihaññi": "टकरा चुका", "paṭihaññati": "टकराना", "paṭihaññissati": "टकराएगा",
    "suṇi": "सुन चुका", "suṇāti": "सुनना", "suṇissati": "सुनेगा",
    "ghāyi": "सूँघ चुका", "ghāyati": "सूँघना", "ghāyissati": "सूँघेगा",
    "sāyi": "चख चुका", "sāyati": "चखना", "sāyissati": "चखेगा",
    "phusi": "छू चुका", "phusati": "छूना", "phusissati": "छुएगा",
    "uppajji": "उत्पन्न हो चुका", "uppajjati": "उत्पन्न होना", "uppajjissati": "उत्पन्न होगा",
    "nissāya": "सहारा", "ārammaṇo": "विषय वाला",
    "dvārā": "द्वार", "samuddo": "समुद्र", "paṇḍaraṃ": "उज्ज्वलता", "khettaṃ": "खेत",
    "nettaṃ": "नेत्र", "nayanaṃ": "नयन", "tīraṃ": "किनारा",
    "suñño": "सूना", "gāmo": "गाँव", "suñño gāmo": "सूना गाँव",
    # visible form (^1-616 …)
    "vaṇṇa": "रंग", "nibhā": "आभा", "vaṇṇanibhā": "रंग-आभा", "upādāya vaṇṇanibhā": "व्युत्पन्न रंग-आभा",
    "nīlaṃ": "नीला", "pītakaṃ": "पीला", "lohitakaṃ": "लाल", "odātaṃ": "सफ़ेद", "kāḷakaṃ": "काला",
    "mañjiṭṭhakaṃ": "मजीठ जैसा गहरा लाल", "hari": "हरा", "harivaṇṇaṃ": "हरे रंग का",
    "amba": "आम", "aṅkura": "कोंपल", "ambaṅkuravaṇṇaṃ": "आम की कोंपलों के रंग का",
    "vaṭṭaṃ": "गोल", "parimaṇḍalaṃ": "वृत्ताकार", "caturaṃsaṃ": "चौकोर",
    "chaḷaṃsaṃ": "छह कोनों वाला", "aṭṭhaṃsaṃ": "आठ कोनों वाला", "soḷasaṃsaṃ": "सोलह कोनों वाला",
    "chāyā": "छाया", "ātapo": "धूप", "āloko": "प्रकाश", "andhakāro": "अंधकार",
    "abbhā": "बादल", "mahikā": "कोहरा", "dhūmo": "धुआँ", "rajo": "धूल",
    "canda": "चंद्रमा", "sūriya": "सूर्य", "maṇḍalassa": "मंडल", "tārakarūpānaṃ": "तारा", "ādāsa": "दर्पण",
    "maṇi": "मणि", "saṅkha": "शंख", "muttā": "मोती", "veḷuriyassa": "वैदूर्य", "rajatassa": "चाँदी",
    "maṇisaṅkhamuttāveḷuriyassa vaṇṇanibhā": "मणि शंख मोती और वैदूर्य की रंग-आभा",
    "jātarūparajatassa vaṇṇanibhā": "सोने और चाँदी की रंग-आभा",
    # sound (^1-620 …)
    "bheri": "नगाड़ा", "bherisaddo": "नगाड़े की ध्वनि", "mudiṅga": "मृदंग", "mudiṅgasaddo": "मृदंग की ध्वनि",
    "saṅkhasaddo": "शंख की ध्वनि", "paṇava": "ढोलक", "paṇavasaddo": "ढोलक की ध्वनि",
    "gīta": "गाना", "gītasaddo": "गाने की ध्वनि", "vādita": "बाजा", "vāditasaddo": "बाजे की ध्वनि",
    "samma": "मंजीरा", "sammasaddo": "मंजीरे की ध्वनि", "pāṇi": "ताली", "pāṇisaddo": "ताली की ध्वनि",
    "sattānaṃ": "प्राणी", "nigghosasaddo": "शोर",
    "sannighāta": "आपस में टकराना", "dhātūnaṃ sannighātasaddo": "वस्तुओं के आपस में टकराने की ध्वनि",
    "vāta": "हवा", "vātasaddo": "हवा की ध्वनि", "udaka": "पानी", "udakasaddo": "पानी की ध्वनि",
    "manussa": "मनुष्य", "manussasaddo": "मनुष्यों की ध्वनि",
    "amanussa": "अमानवीय प्राणी", "amanussasaddo": "अमानवीय प्राणियों की ध्वनि",
    # smell (^1-624 …)
    "mūla": "जड़", "mūlagandho": "जड़ों की गंध", "sāra": "लकड़ी का सार", "sāragandho": "लकड़ी के सार की गंध",
    "taca": "छाल", "tacagandho": "छाल की गंध", "patta": "पत्ता", "pattagandho": "पत्तों की गंध",
    "puppha": "फूल", "pupphagandho": "फूलों की गंध", "phala": "फल", "phalagandho": "फलों की गंध",
    "āmaka": "कच्चा मांस", "āmakagandho": "कच्चे मांस की गंध", "vissa": "सड़न", "vissagandho": "सड़न की गंध",
    "sugandho": "सुगंध", "duggandho": "दुर्गंध",
    # taste (^1-628 …)
    "mūlaraso": "जड़ों का स्वाद", "khandha": "तना", "khandharaso": "तनों का स्वाद", "tacaraso": "छाल का स्वाद",
    "pattaraso": "पत्तों का स्वाद", "puppharaso": "फूलों का स्वाद", "phalaraso": "फलों का स्वाद",
    "ambilaṃ": "खट्टा", "madhuraṃ": "मीठा", "tittakaṃ": "कड़वा", "kaṭukaṃ": "तीखा", "loṇikaṃ": "नमकीन",
    "khārikaṃ": "खारा", "lambilaṃ": "हल्का खट्टा", "kasāvo": "कसैला", "sādu": "स्वादिष्ट",
    # femininity / masculinity faculty
    "itthiyā": "स्त्री", "liṅgaṃ": "आकृति", "nimittaṃ": "चिह्न", "kuttaṃ": "आचरण", "ākappo": "ढंग",
    "purisassa": "पुरुष",
    # life faculty
    "rūpīnaṃ dhammānaṃ": "भौतिक परिघटना", "āyu": "आयु", "ṭhiti": "टिके रहना", "yapanā": "चलते रहना",
    "yāpanā": "चलाए रखना", "iriyanā": "गतिशील रहना", "vattanā": "बने रहना", "pālanā": "पालन",
    # intimation
    "kusalacittassa": "हितकर मन", "akusalacittassa": "हानिकर मन",
    "abhikkamantassa": "आगे बढ़ना", "paṭikkamantassa": "पीछे हटना", "ālokentassa": "सामने देखना",
    "vilokentassa": "इधर-उधर देखना", "samiñjentassa": "अंग सिकोड़ना", "pasārentassa": "अंग फैलाना",
    "thambhanā": "तनना", "santhambhitattaṃ": "भली-भाँति तना हुआ होना", "viññāpanā": "प्रकट करना",
    "vācā": "वाणी", "girā": "बोल", "byappatho": "बोलने का ढंग", "udīraṇaṃ": "उच्चारण",
    "ghoso": "आवाज़", "ghosakammaṃ": "आवाज़ निकालना",
    # space, water
    "gataṃ": "की प्रकृति वाला", "aghaṃ": "रिक्त स्थान", "vivaro": "छेद", "asamphuṭṭhaṃ": "अछूता",
    "sineho": "नमी", "bandhanattaṃ": "बाँधे रखना", "bandhanattaṃ rūpassa": f"{R} को बाँधे रखना",
    # lightness, pliancy, workability, growth, ageing, impermanence
    "lahupariṇāmatā": "जल्दी बदल पाना", "adandhanatā": "सुस्ती का अभाव", "dandhanatā": "सुस्ती",
    "avitthanatā": "जड़ता का अभाव", "vitthanatā": "जड़ता",
    "maddavatā": "कोमलता", "akakkhaḷatā": "कठोरता का अभाव", "kakkhaḷatā": "कठोरता",
    "akathinatā": "कड़ेपन का अभाव", "kathinatā": "कड़ापन",
    "kammaññattaṃ": "कार्य-योग्य होना", "bhāvo": "भाव",
    "kakkhaḷaṃ": "कठोर", "mudukaṃ": "मुलायम", "saṇhaṃ": "चिकना", "pharusaṃ": "खुरदरा",
    "garukaṃ": "भारी", "lahukaṃ": "हल्का",
    "ācayo": "संचय", "āyatanānaṃ": "इंद्रिय-क्षेत्र",
    "jīraṇatā": "जीर्ण होना", "khaṇḍiccaṃ": "दाँतों का टूटना", "pāliccaṃ": "बालों का पकना",
    "valittacatā": "त्वचा पर झुर्रियाँ पड़ना", "āyuno": "आयु", "saṃhāni": "घटना", "paripāko": "पूरी तरह पक जाना",
    "khayo": "क्षय", "vayo": "नाश", "bhedo": "टूटना", "paribhedo": "बिखर जाना", "antaradhānaṃ": "लुप्त हो जाना",
    # edible food
    "odano": "भात", "kummāso": "दलिया", "sattu": "सत्तू", "maccho": "मछली", "maṃsaṃ": "मांस",
    "khīraṃ": "दूध", "dadhi": "दही", "sappi": "घी", "navanītaṃ": "मक्खन", "madhu": "शहद", "phāṇitaṃ": "गुड़",
    "mukha": "मुँह", "āsiyaṃ": "खाना", "danta": "दाँत", "vikhādanaṃ": "चबाना", "gala": "गला",
    "ajjhoharaṇīyaṃ": "नीचे उतारना", "kucchi": "पेट", "vitthambhanaṃ": "भरना", "ojāya": "पोषक सार",
    "yāpenti": "जीवित रहना",
    # kamma-born, mind-born
    "kammassa": "कर्म", "kammassa katattā": "कर्म किए जाने के कारण",
    "cittajaṃ": "मन से जन्मा",
}

# per-segment overrides {bid: {kw: value}}
OVERRIDES = {
    "1-594": {"uppannaṃ": "उत्पन्न होकर"},           # «उत्पन्न होकर छह प्रकार की चेतना से …»
    "1-658": {"rūpaṃ sappaṭighaṃ": f"{R}{GAP}टकराव वाला"},   # «… भौतिक रूप कौन-सा है जो टकराव वाला है?»
    "1-659": {"rūpaṃ appaṭighaṃ": f"{R}{GAP}टकराव से रहित"},
    "1-666": {"rūpaṃ cittasamuṭṭhānaṃ": f"{R}{GAP}मन से उत्पन्न", "hetukaṃ": "कारण होने वाला"},
    "1-667": {"hetukaṃ": "कारण होने वाला"},
    "1-668": {"rūpaṃ cittasahabhu": f"{R}{GAP}मन के साथ-साथ होने वाला"},
    "1-670": {"rūpaṃ cittānuparivatti": f"{R}{GAP}मन का अनुसरण करने वाला"},
    "1-642": {"rūpassa upacayo": f"{R} की{GAP}वृद्धि"},     # «भौतिक रूप की जो वृद्धि है»
    "1-736": {"rūpassa upacayo": f"{R} की{GAP}वृद्धि"},
}

FELL_TO_CH2 = set()


def resolver(bid, kw, kws):
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    k = lc(kw)
    s = set(lc(x) for x in kws)
    # rūpa (stem): fine-material sphere / visible-form base / material form
    if k == "rūpa":
        if any(x.startswith("rūpāvacar") for x in s):
            return "सूक्ष्म भौतिक"
        if s & {"rūpāyatanaṃ", "rūpadhātu"}:
            return "दृश्य रूप"
        return R
    if k == "rūpāyatanaṃ":
        return "दृश्य रूप का इंद्रिय-क्षेत्र"
    if k == "rūpadhātu":
        return "दृश्य रूप का तत्व"
    # sense bases / elements / faculties / contact by organ: X-āyatanaṃ, X-dhātu, X-indriyaṃ, …
    organs = {"cakkh": "आँख", "sot": "कान", "ghān": "नाक", "jivh": "जीभ", "kāy": "शरीर",
              "sadd": "ध्वनि", "gandh": "गंध", "ras": "स्वाद", "phoṭṭhabb": "स्पर्श"}
    for stem, hi in organs.items():
        if k.startswith(stem):
            rest = k[len(stem):]
            if rest in ("āyatanaṃ", "āyatana"):
                return f"{hi} का इंद्रिय-क्षेत्र"
            if rest in ("udhātu", "adhātu", "ādhātu", "dhātu"):
                return f"{hi} का तत्व"
            if rest in ("usamphassassa", "āsamphassassa", "asamphassassa", "usamphasso", "āsamphasso", "asamphasso"):
                return f"{hi} का संपर्क"
            if rest in ("usamphassajā", "āsamphassajā", "asamphassajā", "usamphassajāya", "āsamphassajāya", "asamphassajāya"):
                return f"{hi} के संपर्क से उत्पन्न"
            if rest in ("usamphassajā vedanā", "āsamphassajā vedanā", "asamphassajā vedanā",
                        "usamphassajāya vedanāya", "āsamphassajāya vedanāya", "asamphassajāya vedanāya"):
                return f"{hi} के संपर्क से उत्पन्न अनुभूति"
            if rest in ("uviññāṇassa", "āviññāṇassa", "aviññāṇassa", "uviññāṇaṃ", "āviññāṇaṃ", "aviññāṇaṃ"):
                return f"{hi} की चेतना"
            if rest in ("uṃ nissāya", "aṃ nissāya"):
                return f"{hi} के सहारे"
    if k == "itthi":
        return "स्त्री" if "itthiyā" in s else "स्त्रीत्व"
    if k == "purisa":
        return "पुरुष" if "purisassa" in s else "पुरुषत्व"
    if k == "bhedo" and "vācā" in s:
        return "फूटना"
    if k == "sukha" and "samphassaṃ" in s:
        return "सुखद"
    if k.endswith("meva") and k != "eva":            # X-meva (Ekakaniddesa): the Hindi of X
        return resolver(bid, k[:-4] + "ṃ", kws)
    if k in RUPA:
        return RUPA[k]
    FELL_TO_CH2.add(k)
    return ch2_value(kw, kws)


if __name__ == "__main__":
    for part in PARTS:
        build_part(part, resolver)
        verify(part)
    print("fell to CH2:", sorted(FELL_TO_CH2))
