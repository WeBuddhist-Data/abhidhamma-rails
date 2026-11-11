"""Map 4-01-nikkhepakandam keywords to the Hindi translation.

Order of lookup: per-segment OVERRIDES -> context rules (ctx) -> part table T -> matrix names
(also "dhammā X" as the matrix's "X dhammā") -> CH2 (ch2_value).
usage: python -I -X utf8 map_4-01_hi.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import CH2, ch2_value, build_part, verify, lc, matrix_names, GAP  # noqa: E402

PART = "4-01-nikkhepakandam"
MN = {lc(k): v for k, v in matrix_names().items()}

MALA = "मन के मैल"                       # āsava
SAS = "मन के मैलों का विषय बनने वाला"      # sāsavā
VUC = " … कहा जाता है"                   # vuccati X = «X … कहा जाता है» / «X कहा जाता है»
SIL = "सदाचार और व्रतों के बारे में ग़लत धारणा"
IDAM = "“केवल यही सत्य है” के आग्रह रूपी काया की गाँठ"

T = {
    # headings / colophon
    "nikkhepa": "सारांश", "nikkhepaṃ": "सारांश", "kaṇḍe": "अध्याय", "duka": "दो-दो के वर्गीकरण",
    "hetu": "मूल",
    # frames
    "tattha": "यहाँ", "tehi dhammehi": "उन परिघटनाओं", "yeva": "जो", "yañca": "और जो",
    "evarūpā": "इस प्रकार का", "evarūpo": "इस प्रकार का", "evarūpaṃ": "इस प्रकार का",
    "ṭhapetvā": "छोड़कर", "avasesā": "शेष", "avaseso": "शेष", "avasesā kusala": "शेष हितकर",
    "avasesā sāsavā kusala": "शेष मन के मैलों का विषय बनने वाला हितकर",
    "dhammā": "परिघटना", "dasa": "दस", "na": "न", "hoti": "रहना",
    # wholesome / unwholesome / roots
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    "kusalā nākusalā": "हितकर … न हानिकर", "akusalābyākatā": "हानिकर और नैतिक रूप से अनिर्धारित",
    "kusalānaṃ": "हितकर", "kusalānaṃ dhammānaṃ": "हितकर परिघटना", "kusalānaṃ vā dhammānaṃ": "हितकर परिघटना",
    "abyākatesu vā dhammesu": "नैतिक रूप से अनिर्धारित परिघटना",
    "dhammā kusalā": "हितकर परिघटना", "dhammā akusalā": "हानिकर परिघटना",
    "dhammā abyākatā": "नैतिक रूप से अनिर्धारित परिघटना",
    "mūlāni": "मूल", "kusalamūlāni": "हितकर मूल", "akusalamūlāni": "हानिकर मूल",
    "akusalamūlaṃ": "हानिकर मूल", "kusalahetū": "हितकर मूल", "akusalahetū": "हानिकर मूल",
    "abyākatahetū": "नैतिक रूप से अनिर्धारित मूल",
    "kāmāvacarahetū": "इंद्रिय-सुखों के लोक से संबंधित" + GAP + "मूल",
    "rūpāvacarahetū": "सूक्ष्म भौतिक लोक से संबंधित" + GAP + "मूल",
    "arūpāvacarahetū": "अभौतिक लोक से संबंधित" + GAP + "मूल",
    "apariyāpannahetū": "अस्तित्व के लोकों में न समाए हुए" + GAP + "मूल",
    "lobho": "लोभ", "doso": "द्वेष", "moho": "मोह", "mohena": "मोह",
    "kilesā": "मन के क्लेश", "ekaṭṭhā": "साथ रहने वाला",
    "ekaṭṭhā ca kilesā": "और" + GAP + "साथ रहने वाले मन के क्लेश",
    "sampayutto": "जुड़ा", "sampayuttā": "जुड़ा", "vippayuttā": "अलग",
    "samuṭṭhānaṃ": "उत्पन्न", "samuṭṭhānaṃ kāyakammaṃ": "उत्पन्न शारीरिक कर्म",
    "kāyakammaṃ": "शारीरिक कर्म", "vacī": "वाणी", "vacīkammaṃ": "वाणी का कर्म",
    "manokammaṃ": "मानसिक कर्म", "vacīkammaṃ manokammaṃ": "वाणी का कर्म मानसिक कर्म",
    "kammāni": "कर्म", "kammassa": "कर्म", "kammassa katattā": "कर्म किए जाने के कारण",
    # spheres, groups, elements
    "kāmāvacare": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacare": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacare": "अभौतिक लोक से संबंधित", "avacare": "लोक से संबंधित",
    "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacara": "अभौतिक लोक से संबंधित",
    "arūpa": "अभौतिक", "bhūmiyaṃ": "स्तर",
    "rūpaṃ": "भौतिक रूप", "rūpakkhandho": "भौतिक रूप का समूह", "saṅkhārā": "मानसिक रचनाएँ",
    "saṅkhāre": "मानसिक रचनाएँ", "vedanaṃ": "अनुभूति", "saññaṃ": "पहचान", "vedanāya": "अनुभूति",
    "kiriyā": "क्रिया रूपी", "kiriya": "क्रिया रूपी", "vipākato": "कर्म-फल के रूप में",
    "asaṅkhatā ca dhātu": "और अनिर्मित तत्व", "asaṅkhatā dhātu": "अनिर्मित तत्व",
    "maggā": "मार्ग", "apariyāpannā maggā": "अस्तित्व के लोकों में न समाए हुए मार्ग",
    "maggā apariyāpannā": "अस्तित्व के लोकों में न समाए हुए" + GAP + "मार्ग",
    "phalāni": "फल", "phalaṃ": "फल", "sāmañña": "श्रमण-जीवन", "arahatta": "अर्हत्-पद",
    "upariṭṭhimaṃ": "सबसे ऊँचा",
    # matrix items not in the 1-matika table as given here
    "dhammā savitakkasavicārā": "आरंभिक विचार और सतत विचार वाली परिघटना",
    "dhammā avitakkavicāramattā": "आरंभिक विचार से रहित केवल सतत विचार वाली परिघटना",
    "dhammā avitakkaavicārā": "आरंभिक विचार और सतत विचार दोनों से रहित परिघटना",
    "dhammā pītisahagatā": "उल्लास के साथ होने वाली परिघटना",
    "dhammā sukhasahagatā": "सुख के साथ होने वाली परिघटना",
    "dhammā upekkhāsahagatā": "समभाव के साथ होने वाली परिघटना",
    "sukhāya": "सुखद", "sukhāya vedanāya": "सुखद अनुभूति",
    "dhammā dassanena pahātabbahetukā": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली परिघटना",
    "dhammā bhāvanāya pahātabbahetukā": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली परिघटना",
    "pahātabbahetukā": "छोड़े जाने वाले मूलों वाला",
    "dhammā ācayagāmino": "संचय की ओर ले जाने वाली परिघटना",
    "dhammā apacayagāmino": "संचय घटाने की ओर ले जाने वाली परिघटना",
    "dhammā neva ācayagāmi": "न संचय की ओर" + GAP + "ले जाने वाली परिघटना",
    "caya": "संचय",
    "dhammā micchattaniyatā": "ग़लत दिशा में निश्चित परिघटना",
    "dhammā sammattaniyatā": "सही दिशा में निश्चित परिघटना",
    "ānantarikāni": "अगले ही जन्म में निश्चित फल देने वाला",
    "micchā": "ग़लत", "micchādiṭṭhi": "ग़लत दृष्टि",
    "dhammā hetuvippayuttā": "मूलों से अलग परिघटना",
    "dhammā āsavavippayuttā": "मन के मैलों से अलग परिघटना",
    "dhammā saṃyojanavippayuttā": "बंधनों से अलग परिघटना",
    "dhammā ganthavippayuttā": "गाँठों से अलग परिघटना",
    "dhammā saṃyojanā": "बंधन रूपी परिघटना",
    "saṃyojanā ceva saṃyojaniyā": "बंधन रूपी भी और बंधनों का विषय बनने वाला भी",
    "ganthā ceva ganthaniyā": "गाँठ रूपी भी और गाँठों का विषय बनने वाला भी",
    "sāsavā kusalākusalābyākatā dhammā": SAS[:-1] + "ी हितकर हानिकर और नैतिक रूप से अनिर्धारित परिघटना",
    "sāsavā kusalākusalā dhammā": SAS[:-1] + "ी हितकर और हानिकर परिघटना",
    "sāsavā kusalābyākatā dhammā": SAS[:-1] + "ी हितकर और नैतिक रूप से अनिर्धारित परिघटना",
    "āsava": MALA, "āsavo": "मैल", "āsavā": MALA,
    "kāmāsavo": "इंद्रिय-सुखों का मैल", "bhavāsavo": "अस्तित्व का मैल", "diṭṭhāsavo": "दृष्टि का मैल",
    "avijjāsavo": "अज्ञान का मैल", "avijjāsavena": "अज्ञान का मैल",
    "vipākadhamma": "कर्म-फल उत्पन्न करने वाला", "avipakkavipākānaṃ": "अनपके कर्म-फल वाला",
    # arisen / past ... (uppanna strings)
    "uppannā": "उत्पन्न", "jātā": "जन्मा हुआ", "sañjātā": "भली-भाँति जन्मा", "nibbattā": "पैदा हुआ",
    "abhinibbattā": "पूरी तरह पैदा हुआ", "pātubhūtā": "प्रकट हुआ", "samuppannā": "भली-भाँति उत्पन्न",
    "uṭṭhitā": "उठा हुआ", "samuṭṭhitā": "भली-भाँति उठा हुआ", "aṃsena": "के अंतर्गत",
    "niruddhā": "समाप्त हो चुका", "vigatā": "जा चुका", "vipariṇatā": "बदल चुका",
    "abbhatthaṅgatā": "पूरी तरह अस्त हो चुका", "uppajjitvā": "उत्पन्न होकर",
    "tesaṃ tesaṃ": "उन-उन", "paccattaṃ": "अपना", "pāṭipuggalikā": "हर व्यक्ति का निजी",
    "upādiṇṇā": "कर्म से उत्पन्न", "puggalānaṃ": "व्यक्ति",
    # object-taking (ārabbha)
    "uppajjanti": "उत्पन्न होना", "ārabbha ye uppajjanti": "विषय बनाकर जो" + GAP + "उत्पन्न होना",
    "uppajjanti cittacetasikā": "मन और मन का सहचर" + GAP + "उत्पन्न होना",
    "cittacetasikā": "मन और मन का सहचर", "ārammaṇā": "विषय वाला",
    "paritte dhamme": "सीमित परिघटना", "paritte dhamme ārabbha": "सीमित परिघटना को विषय बनाना",
    "mahaggate dhamme": "उन्नत परिघटना", "mahaggate dhamme ārabbha": "उन्नत परिघटना को विषय बनाना",
    "appamāṇe dhamme": "अपरिमित परिघटना", "appamāṇe dhamme ārabbha": "अपरिमित परिघटना को विषय बनाना",
    "atīte dhamme": "अतीत की परिघटना", "atīte dhamme ārabbha": "अतीत की परिघटना को विषय बनाना",
    "anāgate dhamme": "भविष्य की परिघटना", "anāgate dhamme ārabbha": "भविष्य की परिघटना को विषय बनाना",
    "paccuppanne dhamme": "वर्तमान की परिघटना",
    "paccuppanne dhamme ārabbha": "वर्तमान की परिघटना को विषय बनाना",
    "bahiddhā dhamme ārabbha": "दूसरों से संबंधित परिघटना को विषय बनाना",
    "dhamme ārabbha": "परिघटना को विषय बनाना",
    "ariya": "आर्य", "ariyamagga": "आर्य मार्ग", "ariyamaggaṃ": "आर्य मार्ग", "magga": "मार्ग",
    "samaṅgissa": "युक्त व्यक्ति", "aṅgāni": "अंग", "maggahetū": "मार्ग के मूल",
    "bhāvayantassa": "अभ्यास करना", "maggaṃ bhāvayantassa": "मार्ग का अभ्यास करना",
    "vīmaṃsā": "जाँच-परख",
    # āyatanas, sense doors
    "cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ",
    "cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र", "sotāyatanaṃ": "कान का इंद्रिय-क्षेत्र",
    "ghānāyatanaṃ": "नाक का इंद्रिय-क्षेत्र", "jivhāyatanaṃ": "जीभ का इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ": "शरीर का इंद्रिय-क्षेत्र", "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र",
    "saddāyatanaṃ": "ध्वनि का इंद्रिय-क्षेत्र", "gandhāyatanaṃ": "गंध का इंद्रिय-क्षेत्र",
    "rasāyatanaṃ": "स्वाद का इंद्रिय-क्षेत्र", "phoṭṭhabbāyatanaṃ": "स्पर्श का इंद्रिय-क्षेत्र",
    "dhammāyatana": "मन के विषयों का इंद्रिय-क्षेत्र", "appaṭighaṃ": "टकराव से रहित",
    "anidassanaṃ": "दिखाई न देने वाला", "dhammā appaṭighā": "टकराव से रहित परिघटना",
    "dhammā cakkhu": "परिघटना" + GAP + "आँख", "dhammā sota": "परिघटना" + GAP + "कान",
    "dhammā ghāna": "परिघटना" + GAP + "नाक", "dhammā jivhā": "परिघटना" + GAP + "जीभ",
    "dhammā kāya": "परिघटना" + GAP + "शरीर",
    "upādāya": "व्युत्पन्न", "upādāya rūpaṃ": "व्युत्पन्न भौतिक रूप", "mahābhūtā": "महाभूत",
    "bhūtā": "भूत",
    # fetters / view / doubt (three fetters, sakkāyadiṭṭhi body)
    "pahātabba": "छोड़ा जाने वाला", "saṃyojanāni": "बंधन", "saṃyojanaṃ": "बंधन",
    "sakkāya": "स्थायी आत्मा", "sakkāyadiṭṭhi": "स्थायी आत्मा की ग़लत दृष्टि",
    "vicikicchā": "संशय", "parāmāso": "ग़लत धारणा", "parāmāsa": "ग़लत धारणा",
    "sīla": "सदाचार", "vata": "व्रत", "sīlabbata": "सदाचार और व्रत",
    "sīlabbataparāmāso": SIL, "sīlabbataparāmāsa": SIL, "sīlabbataparāmāsaṃ": SIL,
    "diṭṭhi": "दृष्टि",
    "assutavā": "अशिक्षित", "puthujjano": "साधारण व्यक्ति", "ariyānaṃ": "आर्य",
    "dhammassa": "शिक्षा", "akovido": "निपुण नहीं", "avinīto": "प्रशिक्षित नहीं",
    "sappurisānaṃ": "सज्जन", "purisānaṃ": "सज्जन", "attato": "आत्मा के रूप में",
    "samanupassati": "देखना", "rūpavantaṃ": "भौतिक रूप वाला",
    "diṭṭhigataṃ": "दृष्टि में पड़ जाना", "gahanaṃ": "घना जंगल", "kantāro": "बीहड़",
    "visūkāyikaṃ": "टेढ़ापन", "vipphanditaṃ": "छटपटाहट", "diṭṭhisaṃyojanaṃ": "दृष्टि का बंधन",
    "gāho": "पकड़", "paṭiggāho": "कसकर पकड़ना", "patiṭṭhāho": "कसकर पकड़ना", "abhiniveso": "आग्रह",
    "kummaggo": "कुमार्ग", "maggo": "मार्ग", "patho": "रास्ता", "micchāpatho": "ग़लत रास्ता",
    "micchattaṃ": "ग़लतपन", "tittha": "मतवाद", "vipariyāsa": "उलटा", "vipariyāsaggāho": "उलटी पकड़",
    "satthari": "गुरु", "dhamme": "शिक्षा", "sikkhāya": "प्रशिक्षण", "kaṅkhati": "शंका करना",
    "kaṅkhā": "शंका", "vimati": "दुविधा", "dveḷhakaṃ": "दुचित्तापन", "dvedhāpatho": "दोराहा",
    "saṃsayo": "संदेह", "anekaṃsaggāho": "किसी एक बात को पक्का न पकड़ पाना", "ekaṃsa": "पक्का",
    "āsappanā": "हिचकिचाना", "parisappanā": "बार-बार हिचकिचाना",
    "apariyogāhanā": "गहराई में न उतर पाना", "pariyogāhanā": "गहराई में उतर पाना",
    "thambhitattaṃ": "जड़ हो जाना", "vilekho": "खरोंच",
    "samuppannesu": "उत्पन्न", "samuppannesu dhammesu": "उत्पन्न परिघटना",
    "paṭiccasamuppannesu": "परस्पर-आश्रित रूप से उत्पन्न",
    "paṭiccasamuppannesu dhammesu": "परस्पर-आश्रित रूप से उत्पन्न परिघटना",
    "idappaccayatā": "कार्य-कारण का नियम",
    "ito": "इस शिक्षा", "bahiddhā": "बाहर", "samaṇa": "श्रमण", "brāhmaṇānaṃ": "ब्राह्मण",
    "suddhi": "शुद्धि",
    # knowledge / ignorance
    "dukkhe": "दुःख", "dukkha": "दुःख", "samudaye": "उत्पत्ति", "nirodhe": "अंत",
    "dukkhanirodhe": "दुःख का अंत", "dukkhe ñāṇaṃ": "दुःख का ज्ञान", "ñāṇaṃ": "ज्ञान",
    "dukkhe aññāṇaṃ": "दुःख को न जानना", "aññāṇaṃ": "न जानना", "adassanaṃ": "न देखना",
    "dassanaṃ": "देखना", "anabhisamayo": "सत्य तक न पहुँचना", "ananubodho": "बोध न होना",
    "anubodho": "बोध", "asambodho": "पूर्ण बोध न होना", "sambodho": "पूर्ण बोध",
    "appaṭivedho": "भेद न पाना", "asaṃgāhanā": "न समेट पाना",
    "asamapekkhanā": "निष्पक्ष रूप से न देखना", "samapekkhanā": "निष्पक्ष रूप से देखना",
    "apaccavekkhaṇā": "पुनः विचार न करना", "paccavekkhaṇā": "पुनः विचार करना",
    "apaccakkhakammaṃ": "प्रत्यक्ष न करना", "paccakkhakammaṃ": "प्रत्यक्ष करना",
    "dummejjhaṃ": "दुर्बुद्धि", "bālyaṃ": "मूर्खता", "asampajaññaṃ": "स्पष्ट समझ का अभाव",
    "pamoho": "गहरा मोह", "sammoho": "घोर मोह", "avijjā": "अज्ञान", "ogho": "बाढ़",
    "yogo": "जकड़न", "anusayo": "सुप्त प्रवृत्ति", "pariyuṭṭhānaṃ": "आवेश", "laṅgī": "रुकावट",
    "sambojjha": "जागृति", "aṅgo": "अंग", "maggaṅgaṃ": "मार्ग का अंग", "dhammavicayo": "परिघटनाओं की छानबीन",
    # adosa string
    "metti": "मैत्री", "mettāyanā": "मैत्री करना", "anuddā": "दया", "anuddāyanā": "दया करना",
    "hitesitā": "हित की कामना", "hita": "हित", "anukampā": "सहानुभूति",
    # lobha string
    "rāgo": "राग", "sārāgo": "प्रबल राग", "anunayo": "झुकाव", "anurodho": "अनुकूल होना",
    "nandī": "आनंद", "icchā": "इच्छा", "mucchā": "मूर्छा", "gedho": "लालसा", "paligedho": "गहरी लालसा",
    "saṅgo": "लगाव", "paṅko": "कीचड़", "ejā": "हलचल", "māyā": "कपट", "janikā": "जन्म देने वाली",
    "sañjananī": "उत्पन्न करने वाली", "sibbinī": "सिलने वाली", "jālinī": "जाल बुनने वाली",
    "saritā": "धारा", "visattikā": "फँसाने वाली", "suttaṃ": "धागा", "visaṭā": "फैली हुई",
    "āyūhinī": "जुटाने वाली", "dutiyā": "साथिन", "paṇidhi": "आकांक्षा", "netti": "डोर",
    "bhava": "अस्तित्व", "vanaṃ": "वन", "vanatho": "झाड़-झंखाड़", "santhavo": "घनिष्ठता",
    "sineho": "स्नेह", "apekkhā": "अपेक्षा", "paṭibandhu": "नाता", "āsā": "आशा",
    "āsisanā": "आशा करना", "dhana": "धन", "putta": "संतान", "jīvita": "जीवन",
    "jappā": "तड़प", "pajappā": "गहरी तड़प", "abhijappā": "अत्यधिक तड़प", "jappanā": "तड़पना",
    "loluppaṃ": "लोलुपता", "loluppāyanā": "लोलुप होना", "pucchañjikatā": "चापलूसी",
    "sādhu": "बढ़िया", "kamyatā": "चाह", "adhamma": "अनैतिक", "visama": "अनुचित",
    "nikanti": "रुचि", "nikāmanā": "गहरी कामना", "patthanā": "कामना", "pihanā": "ललक",
    "sampatthanā": "प्रबल कामना", "taṇhā": "तृष्णा", "vibhava": "अनस्तित्व", "nirodha": "समाप्ति",
    "gantho": "गाँठ", "upādānaṃ": "आसक्ति", "āvaraṇaṃ": "आवरण", "nīvaraṇaṃ": "बाधा",
    "chādanaṃ": "पर्दा", "bandhanaṃ": "बेड़ी", "upakkileso": "मलिनता", "latā": "लता",
    "vevicchaṃ": "लोभीपन", "nidānaṃ": "स्रोत", "pabhavo": "उद्गम", "pāso": "फंदा",
    "baḷisaṃ": "काँटा", "visayo": "क्षेत्र", "nadī": "नदी", "gaddulaṃ": "पट्टा", "samuddo": "सागर",
    "abhijjhā": "लालच", "mūlaṃ": "मूल",
    # dosa string
    "anatthaṃ": "अहित", "acarīti": "किया", "acarī": "किया", "caratīti": "कर रहा है",
    "āghāto": "आक्रोश", "jāyati": "उत्पन्न होना", "āghāto jāyati": "आक्रोश उत्पन्न होना",
    "piyassa": "प्रिय", "manāpassa": "मनभावन", "aṭṭhāne": "बिना कारण",
    "paṭighāto": "प्रतिघात", "paṭighaṃ": "चिढ़", "paṭivirodho": "प्रतिविरोध", "kopo": "कोप",
    "pakopo": "प्रकोप", "sampakopo": "तीव्र प्रकोप", "padoso": "गहरा द्वेष", "sampadoso": "तीव्र द्वेष",
    "byāpatti": "दुर्भावना", "kodho": "क्रोध", "kujjhanā": "क्रोध करना", "dussitattaṃ": "द्वेष से भरा होना",
    "byāpajjanā": "दुर्भावना रखना", "virodho": "विरोध", "caṇḍikkaṃ": "उग्रता", "asuropo": "कटु वचन",
    "anattamanatā": "अप्रसन्नता",
    # cankers (kāma / bhava strings)
    "kāmesu": "इंद्रिय-सुख", "chando": "चाह", "kāmacchando": "इंद्रिय-सुखों की चाह",
    "kāmarāgo": "इंद्रिय-सुखों का राग", "kāmarāga": "इंद्रिय-सुखों का राग", "pariḷāho": "ताप",
    "rāga": "राग",
    # ten views
    "sassato": "शाश्वत", "jīvaṃ": "जीव", "sarīranti": "शरीर", "sarīraṃ": "शरीर", "aññaṃ": "अलग",
    "maraṇāti": "मृत्यु", "maraṇā": "मृत्यु", "hoti tathāgato": "तथागत रहता है",
    "moghamaññanti": "बाकी सब झूठ", "sacca": "सत्य",
    # vuccati X
    "vuccati kāmāsavo": "इंद्रिय-सुखों का मैल कहा जाता है",
    "vuccati bhavāsavo": "अस्तित्व का मैल कहा जाता है",
    "vuccati diṭṭhāsavo": "दृष्टि का मैल कहा जाता है",
    "vuccati avijjāsavo": "अज्ञान का मैल कहा जाता है",
    "vuccati kāmarāgasaṃyojanaṃ": "इंद्रिय-सुखों के राग का बंधन कहा जाता है",
    "vuccati paṭighasaṃyojanaṃ": "चिढ़ का बंधन कहा जाता है",
    "vuccati mānasaṃyojanaṃ": "अहंकार का बंधन कहा जाता है",
    "vuccati diṭṭhisaṃyojanaṃ": "दृष्टि का बंधन कहा जाता है",
    "vuccati vicikicchāsaṃyojanaṃ": "संशय का बंधन कहा जाता है",
    "vuccati sīlabbataparāmāsasaṃyojanaṃ": SIL + " का बंधन कहा जाता है",
    "vuccati bhavarāgasaṃyojanaṃ": "अस्तित्व के राग का बंधन कहा जाता है",
    "vuccati issāsaṃyojanaṃ": "ईर्ष्या का बंधन कहा जाता है",
    "vuccati macchariyasaṃyojanaṃ": "कंजूसी का बंधन कहा जाता है",
    "vuccati avijjāsaṃyojanaṃ": "अज्ञान का बंधन कहा जाता है",
    "vuccati abhijjhā kāya": "लालच रूपी काया" + VUC,
    "vuccati byāpādo kāya": "दुर्भावना रूपी काया" + VUC,
    "vuccati sīlabbataparāmāso kāya": SIL + " रूपी काया" + VUC,
    "vuccati idaṃsaccābhiniveso kāya": "“केवल यही सत्य है” के आग्रह रूपी काया" + VUC,
    # ten fetters
    "paṭigha": "चिढ़", "māna": "अहंकार", "issā": "ईर्ष्या", "macchariya": "कंजूसी",
    "kāmarāgasaṃyojanaṃ": "इंद्रिय-सुखों के राग का बंधन", "paṭighasaṃyojanaṃ": "चिढ़ का बंधन",
    "mānasaṃyojanaṃ": "अहंकार का बंधन", "vicikicchāsaṃyojanaṃ": "संशय का बंधन",
    "sīlabbataparāmāsasaṃyojanaṃ": SIL + " का बंधन", "bhavarāgasaṃyojanaṃ": "अस्तित्व के राग का बंधन",
    "issāsaṃyojanaṃ": "ईर्ष्या का बंधन", "macchariyasaṃyojanaṃ": "कंजूसी का बंधन",
    "avijjāsaṃyojanaṃ": "अज्ञान का बंधन", "avijjāsaṃyojanena": "अज्ञान का बंधन",
    "saṃyojana": "बंधन", "saṃyojanā": "बंधन",
    # māna / issā / macchariya bodies
    "sadiso": "बराबर", "hīno": "हीन", "maññanā": "मान लेना", "maññitattaṃ": "मान चुका होना",
    "unnati": "ऊँचा उठना", "unnamo": "अकड़", "dhajo": "झंडा", "ketu": "झंडा",
    "ketukamyatā": "झंडा फहराने की इच्छा",
    "issāyanā": "ईर्ष्या करना", "usūyā": "जलन", "usūyanā": "जलना", "para": "दूसरा",
    "sakkāra": "सत्कार", "garukāra": "सम्मान", "mānana": "आदर", "vandana": "वंदना", "pūjanāsu": "पूजा",
    "macchariyāni": "कंजूसी", "maccharāyanā": "कंजूसी करना", "āvāsa": "निवास-स्थान", "kula": "परिवार",
    "vaṇṇa": "प्रशंसा", "kadariyaṃ": "कृपणता", "kaṭukañcukatā": "मुट्ठी भींचे रखना",
    "aggahitattaṃ": "संकुचित होना",
    # ties
    "kāyagantho": "काया की गाँठ", "byāpādo": "दुर्भावना", "ganthā": "गाँठ",
    "abhijjhā kāyagantho": "लालच रूपी काया की गाँठ", "abhijjhākāyaganthena": "लालच रूपी काया की गाँठ",
    "byāpādo kāyagantho": "दुर्भावना रूपी काया की गाँठ",
    "sīlabbataparāmāso kāyagantho": SIL + " रूपी काया की गाँठ",
    "sīlabbataparāmāsaṃ kāyaganthaṃ": SIL + " रूपी काया की गाँठ",
    "idaṃ saccābhiniveso kāyagantho": IDAM, "idaṃsaccābhiniveso kāyagantho": IDAM,
}


def ctx(bid, kw, kws):
    """Context rules; return None to fall through to the tables."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    n = int(bid.split("-")[-1]) if bid.count("-") == 1 else 0
    if k == "rūpa":
        if any(x.startswith("rūpāvacar") for x in s):
            return "सूक्ष्म भौतिक"
        if bid in ("1-1065", "1-1141") or "rūpāyatanaṃ" in s:
            return "दृश्य रूप"
        return "भौतिक रूप"
    if k == "kāya":
        if "kāyakammaṃ" in s:
            return "शारीरिक"
        if bid in ("1-1057", "1-1101"):
            return "शरीर"
        return "काया"                                  # kāyagantho
    if k == "mano":
        return "मानसिक" if "manokammaṃ" in s else "मन"
    if k == "cittassa" or k == "citta":
        return "मन"
    if k == "dhamma":
        return "शिक्षा" if bid == "1-1127" else "मन के विषय"
    if k == "dhamme" and bid == "1-1055":
        return "परिघटना"
    if k == "āsavo" and bid == "1-1114":
        return "मन का मैल"
    # closing pair of each cluster: X-niyā = «उनका विषय (न) बनने वाला»
    if bid in ("1-1116", "1-1117", "1-1138", "1-1139", "1-1154", "1-1155"):
        if k in ("sāsavā", "anāsavā", "saṃyojaniyā", "ganthaniyā") and not (k == "sāsavā" and bid != "1-1116"):
            return "उनका विषय न बनने वाला" if k == "anāsavā" else "उनका विषय बनने वाला"
        if k.startswith("dhammā ") and k.endswith("vippayuttā"):
            return {"āsava": "मन के मैलों", "saṃyojana": "बंधनों", "gantha": "गाँठों"}[
                k[len("dhammā "):-len("vippayuttā")]] + " से अलग" + GAP + "परिघटना"
        if k == "saṃyojanavippayuttā saṃyojaniyā":
            return "बंधनों से अलग" + GAP + "उनका विषय बनने वाला"
        if k == "ganthavippayuttā ganthaniyā":
            return "गाँठों से अलग" + GAP + "उनका विषय बनने वाला"
    if k == "ārammaṇā" and bid == "1-1038":
        return "विषय बनाने वाला"
    if k == "hetukā":
        if bid == "1-1039":
            return "मूल बनाने वाला"
        if bid in ("1-1079", "1-1084"):
            return "मूल वाला"
        if bid == "1-1080":
            return "मूल"                                 # ahetukā = «मूल से रहित»
        return "मूलों वाला"
    if k == "niyatā" and bid in ("1-1050", "1-1051"):
        return "बँधा"
    if k == "patho" and bid in ("1-1008", "1-1123"):
        return "दोराहा"
    if k == "gāho" and bid in ("1-1008", "1-1123"):
        return "पकड़ पाना"
    if k == "ñāṇaṃ" and bid not in ("1-1063", "1-1076"):
        return "जानना"                                   # only inside aññāṇaṃ
    if k == "sampaggāho" and bid == "1-1121":
        return "स्वयं को ऊपर उठाना"
    if k == "kamyatā" and bid == "1-1121":
        return "इच्छा"
    if k == "sekkhā" and bid == "1-1024":
        return "सीखना"                                   # only inside asekkhā
    if k == "bahiddhā" and bid in ("1-1052", "1-1055"):
        return "दूसरों" + GAP + "से संबंधित"            # «स्वयं और दूसरों दोनों से संबंधित»
    if k == "bahiddhā" and bid not in ("1-1009", "1-1124", "1-1143"):
        return "दूसरों से संबंधित"
    if k == "rūpāvacarā" and bid == "1-1027":
        return "सूक्ष्म भौतिक लोक से" + GAP + "संबंधित"   # «सूक्ष्म भौतिक लोक से और अभौतिक लोक से संबंधित»
    return None


OVERRIDES = {
}


def resolver(bid, kw, kws):
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    v = ctx(bid, kw, kws)
    if v is not None:
        return v
    k = lc(kw)
    if k in T:
        return T[k]
    if k in MN:
        return MN[k]
    if k.startswith("dhammā ") and (k[len("dhammā "):] + " dhammā") in MN:
        return MN[k[len("dhammā "):] + " dhammā"]
    return ch2_value(kw, kws)


if __name__ == "__main__":
    build_part(PART, resolver)
    verify(PART, show=200)
