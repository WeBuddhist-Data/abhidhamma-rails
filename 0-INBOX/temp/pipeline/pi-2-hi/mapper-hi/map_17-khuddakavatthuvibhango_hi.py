"""pi-2 chapter 17 (Khuddakavatthuvibhaṅga): Pāli->Hindi keyword map.

usage: python -I -X utf8 map_17-khuddakavatthuvibhango_hi.py
Writes 17-khuddakavatthuvibhango.mapped.md and prints the verify report.

Resolution order: OVR[bid][kw] -> T (a value, or a list of candidates: the first one present in that
segment's Hindi wins, so one Pāli word gets the reading its segment actually has) -> pi2_value (PI2 / CH2).
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import (PI2, NDE, pi2_value, build_part, verify, present, lc,  # noqa: E402
                           read_hindi, read_keywords)

CH = "17-khuddakavatthuvibhango"
G = " … "

T = {}

# ---------------------------------------------------------------- headings, matrix, list names
T.update({
    "khuddaka": "छोटा", "vatthu": "विषय", "mātikā": "मूल सूची", "niddeso": "व्याख्या",
    "ekaka": "एकल वर्गीकरण", "ekakaṃ": "एकल वर्गीकरण",
    "duka": "दो-दो के वर्गीकरण", "dukaṃ": "दो-दो के वर्गीकरण", "tika": "तीन-तीन के वर्गीकरण",
    "tikaṃ": "तीन-तीन के वर्गीकरण", "catukka": "चार-चार के वर्गीकरण", "catukkaṃ": "चार-चार के वर्गीकरण",
    "pañcaka": "पाँच-पाँच के वर्गीकरण", "pañcakaṃ": "पाँच-पाँच के वर्गीकरण",
    "chakka": "छह-छह के वर्गीकरण", "chakkaṃ": "छह-छह के वर्गीकरण",
    "chakkamātikā": "छह-छह के वर्गीकरणों की मूल सूची",
    "sattaka": "सात-सात के वर्गीकरण", "sattakaṃ": "सात-सात के वर्गीकरण",
    "aṭṭhaka": "आठ-आठ के वर्गीकरण", "aṭṭhakaṃ": "आठ-आठ के वर्गीकरण",
    "navaka": "नौ-नौ के वर्गीकरण", "navakaṃ": "नौ-नौ के वर्गीकरण",
    "dasaka": "दस-दस के वर्गीकरण", "dasakaṃ": "दस-दस के वर्गीकरण",
    "dasakamātikā": "दस-दस के वर्गीकरणों की मूल सूची",
    "ādī": "आदि", "ādi": "आदि", "ādīni": "आदि",
})

# ---------------------------------------------------------------- the ones: mada, names 28-48
T.update({
    "jāti": "जन्म", "jātiṃ": "जन्म", "jātiṃ paṭicca": "जन्म के कारण",
    "mado": ["मद", "नशा"], "jātimado": "जन्म का मद", "gotta": "गोत्र", "gottaṃ": "गोत्र",
    "gottamadādī": "गोत्र आदि का मद", "gottamado": "गोत्र का मद", "pāripūrimado": "अंगों की परिपूर्णता का मद",
    "majjanā": "मदमस्त होना", "majjitattaṃ": "मद से भरा होना",
    "ārogya": "स्वास्थ्य", "ārogyaṃ": "स्वास्थ्य", "yobbana": "जवानी", "yobbanaṃ": "जवानी",
    "jīvita": "जीवन", "jīvitaṃ": "जीवन", "sakkāra": ["सत्कार", "सम्मान"], "sakkāraṃ": "सत्कार",
    "garukāra": ["सम्मान", "आदर"], "garukāraṃ": "सम्मान",
    "bhoga": "धन-संपत्ति", "bhogaṃ": "धन-संपत्ति", "vaṇṇa": ["सुंदरता", "प्रशंसा", "रूप-रंग"],
    "vaṇṇaṃ": "सुंदरता", "suta": ["सुना-सीखा ज्ञान", "सुना-सीखा", "सुना"], "sutaṃ": ["सुना-सीखा ज्ञान", "सुना हुआ"],
    "paṭibhāna": "हाज़िरजवाबी", "paṭibhānaṃ": "हाज़िरजवाबी", "rattaññu": "वरिष्ठता",
    "rattaññutaṃ": "वरिष्ठता", "piṇḍapātika": "भिक्षा के भोजन पर ही रहना",
    "piṇḍapātikattaṃ": "भिक्षा के भोजन पर ही रहना", "anavaññāta": "तिरस्कृत न होना",
    "anavaññātaṃ": "तिरस्कृत न होना", "iriyāpatha": "चाल-ढाल", "iriyāpathaṃ": "चाल-ढाल",
    "iddhi": "सिद्धि", "iddhiṃ": "सिद्धि", "yasa": "यश", "yasaṃ": "यश", "sīla": "सदाचार", "sīlaṃ": "सदाचार",
    "jhāna": "ध्यान", "jhānaṃ": "ध्यान", "sippa": "कला-कौशल", "sippaṃ": "कला-कौशल",
    "āroha": "ऊँचा क़द", "ārohaṃ": "ऊँचा क़द", "pariṇāha": "डील-डौल", "pariṇāhaṃ": "डील-डौल",
    "saṇṭhāna": "शरीर की बनावट", "saṇṭhānaṃ": "शरीर की बनावट",
    "pāripūri": "अंगों की परिपूर्णता", "pāripūriṃ": "अंगों की परिपूर्णता",
    "pamādo": "लापरवाही", "thambho": "हठ", "sārambho": "प्रतिद्वंद्विता", "icchatā": "इच्छा",
    "atricchatā": "अतृप्त इच्छा", "mahicchatā": "अत्यधिक इच्छा", "pāpicchatā": "बुरी इच्छा",
    "siṅgaṃ": "बनावटीपन", "tintiṇaṃ": "लालच भरी कुड़कुड़ाहट", "cāpalyaṃ": "चंचलता", "vutti": "व्यवहार",
    "asabhāga": "अशोभनीय", "arati": "अरुचि", "tandī": "सुस्ती", "vijambhitā": "अंगड़ाई",
    "sammado": "भारीपन", "bhatta": "भोजन", "līnattaṃ": "शिथिलता", "cetaso ca līnattaṃ": "मन की शिथिलता",
    "kuhanā": "पाखंड", "lapanā": "चिकनी-चुपड़ी बातें", "nemittikatā": "इशारेबाज़ी",
    "nippesikatā": "ताने मारकर वसूलना", "nijigīsanatā": "पाने की चाह",
    "lābhaṃ nijigīsanatā": "लाभ से लाभ पाने की चाह",
})

# ---------------------------------------------------------------- māna
T.update({
    "māno": "अहंकार", "sadisohamasmīti": "मैं बराबर हूँ", "hīnohamasmīti": "मैं हीन हूँ",
    "sadisassa": "बराबर वाला व्यक्ति", "hīnassa": "हीन व्यक्ति",
    "atimāno": "अति-अहंकार", "ātimāno": "पर अहंकार", "mānātimāno": "अहंकार पर अहंकार",
    "omāno": "हीनता का अहंकार", "adhimāno": "उपलब्धि का झूठा अहंकार", "asmimāno": "मैं हूँ का अहंकार",
    "micchāmāno": "ग़लत अहंकार",
    # MANA formula (pi-1): अहंकार, मान लेना, मान चुका होना, ऊँचा उठना, अकड़, ध्वजा, स्वयं को ऊपर उठाना,
    # मन की झंडा फहराने की चाह
    "maññanā": "मान लेना", "maññitattaṃ": "मान चुका होना", "unnati": "ऊँचा उठना", "unnāmo": "अकड़",
    "dhajo": "ध्वजा", "sampaggāho": "स्वयं को ऊपर उठाना", "ketu": "झंडा",
    "kamyatā": ["झंडा फहराने की चाह", "इच्छा", "चाह"],
})

# ---------------------------------------------------------------- vitakka names (68-73)
T.update({
    "ñāti": "रिश्तेदार", "janapada": "अपना देश", "amara": "अमरता",
    "vitakko": ["आरंभिक विचार", "विचार"], "paṭisaṃyutto": "जुड़ा", "paṭisaṃyutto vitakko": "जुड़ा विचार",
    "parānuddayatāpaṭisaṃyutto": "दूसरों के प्रति सहानुभूति से जुड़ा", "ānuddayatā": "सहानुभूति",
    "anavaññatti": "तिरस्कृत न होना", "siloka": "प्रसिद्धि",
})

# ---------------------------------------------------------------- the twos (names)
T.update({
    "kodho": "क्रोध", "upanāho": "बैर", "makkho": "दूसरों को नीचा दिखाना", "paḷāso": "बराबरी की होड़",
    "issā": "ईर्ष्या", "macchariyañca": "कंजूसी", "māyā": "कपट", "sāṭheyyañca": "धूर्तता",
    "taṇhā": "तृष्णा", "bhavataṇhā": "अस्तित्व की तृष्णा", "bhava": "अस्तित्व", "avijjā": "अज्ञान",
    "vibhava": "अनस्तित्व", "bhavadiṭṭhi": "अस्तित्व की दृष्टि", "vibhavadiṭṭhi": "अनस्तित्व की दृष्टि",
    "uccheda": "विनाश", "ucchedadiṭṭhi": "विनाश की दृष्टि", "sassata": "शाश्वतता",
    "sassatadiṭṭhi": "शाश्वतता की दृष्टि", "antavā": ["सीमितता", "सीमित"], "antavādiṭṭhi": "सीमितता की दृष्टि",
    "anantavā": ["असीमता", "असीम"], "anantavādiṭṭhi": "असीमता की दृष्टि", "ānudiṭṭhi": "के बारे में दृष्टि",
    "anottappañca": "बुराई के प्रति निडरता", "ahirikañca": "निर्लज्जता",
    "dovacassatā": "सलाह न मानने की प्रवृत्ति", "pāpa": "बुरा", "pāpamittatā": "बुरे मित्रों की संगति",
    "mittatā": "मित्रों की संगति", "anajjavo": "सरलता का अभाव", "amaddavo": "कोमलता का अभाव",
    "akkhanti": "सहनशीलता का अभाव", "asoraccañca": "सौम्यता का अभाव",
    "appaṭisanthāro": "आदर-सत्कार का अभाव", "asākhalyañca": "मधुर व्यवहार का अभाव",
    "aguttadvāratā": "द्वारों की रक्षा न करने की प्रवृत्ति", "indriyesu": "इंद्रिय", "bhojane": "भोजन",
    "amattaññutā": "मात्रा के ज्ञान का अभाव", "bhojane amattaññutā": "भोजन में मात्रा के ज्ञान का अभाव",
    "asampajaññañca": "स्पष्ट समझ का अभाव", "muṭṭhassaccañca": "सजगता की कमी",
    "vipatti": "विफलता", "diṭṭhivipatti": "दृष्टि में विफलता",
    "bahiddhā": ["बाहरी", "बाहर", "दूसरों से संबंधित"], "saṃyojanañca": "बंधन", "ajjhatta": "भीतरी",
})

# ---------------------------------------------------------------- the threes ... tens (names)
T.update({
    "mūlāni": "मूल", "akusala": "हानिकर", "akusalamūlāni": "हानिकर मूल", "vitakkā": "विचार",
    "akusalavitakkā": "हानिकर विचार", "akusalasaññā": "हानिकर पहचान", "akusaladhātuyo": "हानिकर तत्व",
    "duccaritāni": "दुराचरण", "āsavā": "मन के मैल", "saṃyojanāni": "बंधन", "esanā": "खोज",
    "vidhā": "ढंग", "bhayāni": "भय", "tamāni": "अंधकार", "āyatanāni": "आधार",
    "titthāyatanāni": "मतवादों का आधार", "kiñcanā": "बोझ", "aṅgaṇāni": "दाग़", "malāni": "कलुष",
    "visamāni": "विषमता", "aggī": "अग्नि", "kasāvā": "कड़वाहट", "assāda": "भोग-स्वाद",
    "assādadiṭṭhi": "भोग-स्वाद की दृष्टि", "attānudiṭṭhi": "आत्मा को मानने वाली दृष्टि",
    "micchā": "ग़लत", "micchādiṭṭhi": "ग़लत दृष्टि", "vihesā": "उत्पीड़न", "cariyā": "आचरण",
    "adhamma": "अनुचित", "adhammacariyā": "अनुचित आचरण", "nānatta": "विविधता",
    "nānattasaññā": "विविधता की पहचान", "uddhaccaṃ": "बेचैनी", "kosajjaṃ": "आलसीपन",
    "asantuṭṭhitā": "असंतोष", "asampajaññatā": "स्पष्ट समझ का अभाव", "ahirikaṃ": "निर्लज्जता",
    "anottappaṃ": "बुराई के प्रति निडरता", "anādariyaṃ": "अनादर", "assaddhiyaṃ": "श्रद्धा का अभाव",
    "avadaññutā": "उदारता का अभाव", "asaṃvaro": "असंयम", "dussīlyaṃ": "दुराचार", "ariyānaṃ": "आर्य",
    "saddhammaṃ": "सच्ची शिक्षा", "asotukamyatā": "न सुनने की इच्छा", "upārambha": "दोष ढूँढना",
    "upārambhacittatā": "दोष ढूँढने वाला मन", "cittatā": "मन", "muṭṭhassaccaṃ": "सजगता की कमी",
    "asampajaññaṃ": "स्पष्ट समझ का अभाव", "vikkhepo": "भटकाव", "cetaso vikkhepo": "मन का भटकाव",
    "manasikāro": "मनोयोग", "ayoniso": "अनुचित", "ayoniso manasikāro": "अनुचित मनोयोग",
    "kummagga": "कुमार्ग",
    "kāmāsavo": "इंद्रिय-सुखों का मैल", "āsavo": ["मन का मैल", "मैल"], "bhavāsavo": "अस्तित्व का मैल",
    "diṭṭhāsavo": "दृष्टि का मैल", "avijjāsavo": "अज्ञान का मैल", "ganthādī": "गाँठ आदि",
    "upādānaṃ": "आसक्ति", "kāmupādānaṃ": "इंद्रिय-सुखों के प्रति आसक्ति",
    "diṭṭhupādānaṃ": "दृष्टियों के प्रति आसक्ति", "sīlabbatupādānaṃ": "सदाचार और व्रतों के प्रति आसक्ति",
    "attavādupādānaṃ": "आत्मा के सिद्धांत के प्रति आसक्ति", "uppādā": "उत्पन्न होने का कारण",
    "taṇhuppādā": "तृष्णा के उत्पन्न होने का कारण", "agati": "ग़लत राह", "gamanāni": "जाना",
    "vipariyāsā": "उलटापन", "anariya": "अनार्य", "vohārā": "कथन", "diṭṭhiyo": "दृष्टि",
    "macchariyāni": "कंजूसी", "saṅgā": "लगाव", "sallā": "काँटा", "khilā": "कठोरता", "ceto": "मन",
    "vinibandhā": "बेड़ी", "nīvaraṇāni": "बाधा", "kammāni": "कर्म",
    "ānantarikāni": "अगले ही जन्म में निश्चित फल देने वाला", "verā": "वैर", "ādīnavā": "दुष्परिणाम",
    "akkhantiyā": "सहनशीलता का अभाव", "vādā": "मत", "nibbānavādā": "निर्वाण का मत",
    "diṭṭhadhamma": "इसी जीवन", "vivāda": "विवाद", "chandarāgā": "चाह भरा राग", "vatthūni": "आधार",
    "virodha": "विरोध", "kāyā": "वर्ग", "agāravā": "अनादर", "parihāniyā": "पतन की ओर ले जाने वाला",
    "dhammā": "परिघटना", "parihāniyā dhammā": "पतन की ओर ले जाने वाली परिघटना",
    "upavicārā": "मानसिक विचरण", "somanassupavicārā": "प्रसन्नता वाला मानसिक विचरण",
    "domanassupavicārā": "उदासी वाला मानसिक विचरण", "upekkhupavicārā": "समभाव वाला मानसिक विचरण",
    "gehasitāni": "सांसारिक", "somanassāni": "प्रसन्नता", "gehasitāni somanassāni": "सांसारिक प्रसन्नता",
    "domanassāni": "उदासी", "gehasitāni domanassāni": "सांसारिक उदासी", "gehasitā": "सांसारिक",
    "gehasitā upekkhā": "सांसारिक समभाव", "ānusayā": "सुप्त प्रवृत्ति", "anusayā": "सुप्त प्रवृत्ति",
    "pariyuṭṭhānāni": "आवेश", "asaddhammā": "बुरा गुण", "mānā": "अहंकार",
    "kilesa": ["मन के क्लेश", "क्लेश"], "kilesavatthūni": "मन के क्लेशों का आधार",
    "kusītavatthūni": "आलसीपन का आधार", "kusīta": "आलसीपन", "paṭighāto": "प्रतिघात",
    "lokadhammesu": "सांसारिक परिघटना", "micchattā": "ग़लतपन", "dosā": "दोष", "purisa": "व्यक्ति",
    "asaññī": "पहचान से रहित", "asaññi": "पहचान से रहित",
    "nevasaññīnāsaññī": "न पहचान वाली न पहचान से रहित", "nevasaññināsaññi": "न पहचान वाली न पहचान से रहित",
    "āghāta": "आक्रोश", "navavidhā": "नौ प्रकार", "mūlakā": "उपजा", "mūlakā dhammā": "उपजी परिघटना",
    "iñjitāni": "हलचल", "maññitādīni": "मान्यता आदि", "maññitāni": "मान्यता", "phanditāni": "छटपटाहट",
    "papañcitāni": "मानसिक फैलाव", "saṅkhatāni": "निर्मिति",
    "dasa": "दस", "pathā": "कर्म-पथ", "dasa saṃyojanāni": "दस बंधन", "dasa micchattā": "दस ग़लतपन",
    "vatthukā": "आधारों वाला", "dasavatthukā": "दस आधारों वाला",
    "dasavatthukā micchādiṭṭhi": "दस आधारों वाली ग़लत दृष्टि", "antaggāhikā": "अतिवादी",
    "antaggāhikā diṭṭhi": "अतिवादी दृष्टि", "dasavatthukā antaggāhikā diṭṭhi": "दस आधारों वाली अतिवादी दृष्टि",
    "vicarita": "विचरण", "taṇhāvicarita": "तृष्णा का विचरण", "vicaritāni": "विचरण",
    "taṇhāvicaritāni": "तृष्णा का विचरण", "ajjhattikassa": "आंतरिक", "bāhirassa": "बाह्य",
    "upādāya": ["आधार बनाकर", "व्युत्पन्न"],
    "aṭṭhārasa": "अठारह", "chattiṃsa": "छत्तीस", "sataṃ": "सौ", "dvāsaṭṭhi": "बासठ",
    "veyyākaraṇe": "व्याख्यान", "bhagavatā": "भगवान", "vuttāni": "कहा गया", "gatāni": "दृष्टि",
    "tadekajjhaṃ": "उन सबको एक साथ",
})

# ---------------------------------------------------------------- pamāda (2-846)
T.update({
    "kāya": ["शारीरिक", "शरीर", "वर्ग"], "kāyaduccarite": "शारीरिक दुराचरण", "vacī": ["वाचिक", "वाणी"],
    "vacīduccarite": "वाचिक दुराचरण", "mano": ["मानसिक", "मन"], "manoduccarite": "मानसिक दुराचरण",
    "duccarite": "दुराचरण", "guṇesu": "भोग", "kāmaguṇesu": "इंद्रिय-सुखों के" + G + "भोग",
    "vossaggo": "खुला छोड़ देना", "cittassa vossaggo": "मन को खुला छोड़ देना",
    "ānuppadānaṃ": "खुला छोड़ते जाना", "kusalānaṃ": "हितकर", "dhammānaṃ": "परिघटना",
    "kusalānaṃ vā dhammānaṃ": "हितकर परिघटना", "asakkaccakiriyatā": "लापरवाही से काम करना",
    "kiriyatā": "करना", "asātaccakiriyatā": "लगातार न करना", "anaṭṭhitakiriyatā": "टिककर न करना",
    "anaṭṭhita": "टिककर न", "olīna": "ढीला", "vuttitā": "बर्ताव", "chandatā": ["चाह", "लगन"],
    "dhuratā": ["भार", "ज़िम्मेदारी"], "anāsevanā": "अभ्यास न करना", "abhāvanā": "विकास न करना",
    "abahulīkammaṃ": "बार-बार न करना", "anadhiṭṭhānaṃ": "दृढ़ निश्चय न करना", "ananuyogo": "जुटे न रहना",
    "pamajjanā": "लापरवाही करना", "evarūpo": "इस प्रकार का", "evarūpā": "इस प्रकार का",
    "evarūpaṃ": "इस प्रकार का",
})

# ---------------------------------------------------------------- the ones: definitions (2-847 ... 2-868)
T.update({
    "tattha": "यहाँ", "yo": "जो", "yā": "जो", "yaṃ": "जो",
    "thambhanā": "हठ करना", "kakkhaḷiyaṃ": "कठोरता", "phārusiyaṃ": "रूखापन",
    "ujucittatā": "मन का तना रहना", "amudutā": "मृदुता का अभाव",
    "sārambhanā": "प्रतिद्वंद्विता करना", "paṭisārambho": "जवाबी प्रतिद्वंद्विता",
    "paṭisārambhanā": "जवाबी प्रतिद्वंद्विता करना",
    # REQ / icchā string
    "itarītara": "जैसे भी", "cīvara": "वस्त्र", "piṇḍapāta": "भिक्षा का भोजन", "senāsana": "निवास-स्थान",
    "gilāna": "रोगी", "paccaya": NDE, "bhesajja": "दवा", "guṇehi": "भोग",
    "kāmaguṇehi": "इंद्रिय-सुखों के" + G + "भोग", "asantuṭṭhassa": "असंतुष्ट व्यक्ति",
    "bhiyyokamyatā": "और अधिक पाने की चाह", "icchā": "इच्छा", "icchāgatā": "इच्छा में पड़ना",
    "rāgo": "राग", "sārāgo": "प्रबल राग", "cittassa": "मन",
    # pāpicchatā
    "assaddho": "श्रद्धाहीन", "dussīlo": "दुराचारी", "sīlavāti": "सदाचारी", "appassuto": "कम सुना-सीखा",
    "bahussutoti": "बहुत सुना-सीखा", "ārāmo": "रमने वाला", "pavivittoti": "एकांतप्रिय", "kusīto": "आलसी",
    "āraddhavīriyoti": "उत्साही", "muṭṭhassatī": "सजगता खोया हुआ", "upaṭṭhitassatīti": "सजग",
    "asamāhito": "एकाग्रता से रहित", "samāhitoti": "एकाग्र", "duppañño": "प्रज्ञाहीन",
    "paññavāti": "प्रज्ञावान", "akhīṇāsavo": "मन के मैलों को नष्ट न कर चुका", "jano": "लोग",
    "jānātū": "जानना", "icchati": "चाहना", "ekacco": "कोई व्यक्ति",
    # siṅga, tintiṇa (LOLUPPA), cāpalya
    "siṅgāratā": "सजधज", "cāturatā": "चतुराई", "cāturiyaṃ": "चतुरता", "parikkhattatā": "चालाकी",
    "tintiṇāyanā": "कुड़कुड़ाना", "loluppaṃ": "लोलुपता", "loluppāyanā": "लोलुप होना",
    "pucchañjikatā": "चापलूसी", "sādhu": "बढ़िया चीज़",
    "maṇḍanā": "सजाना", "vibhūsanā": "सँवारना", "kāyassa": "शरीर", "patta": "भिक्षा-पात्र",
    "pūti": "सड़ने वाला", "bāhirānaṃ": "बाहरी", "parikkhārānaṃ": "सामान", "keḷanā": "लाड़ करना",
    "giddhikatā": "लालायित रहना", "capalatā": "चपलता",
    # asabhāgavutti
    "mātari": "माता", "pitari": "पिता", "jeṭṭhe": "बड़ा", "bhātari": "भाई", "ācariyesu": "आचार्य",
    "upajjhāye": "उपाध्याय", "buddhe": "बुद्ध", "sāvakesu": "शिष्य", "aññataraññataresu": "किसी और",
    "garu": "आदरणीय", "ṭhāniyesu": "आदरणीय", "vippaṭikūla": "उलटा", "ggāhitā": "बात पकड़ना",
    "vipaccanīka": "विरोध", "sātatā": "रस लेना", "anādariyatā": "अनादर का भाव", "agāravatā": "अगौरव",
    "appatissavatā": "बात पर कान न देना",
    # arati
    "pantesu": "दूर-दराज़", "senāsanesu": "निवास-स्थान", "kusalesu": "हितकर", "dhammesu": "परिघटना",
    "kusalesu dhammesu": "हितकर परिघटना", "aratitā": "अरुचि का भाव", "anabhirati": "मन न लगना",
    "anabhiramaṇā": "मन न रमना", "ukkaṇṭhitā": "ऊब", "paritassitā": "व्याकुलता",
    # tandī, vijambhitā, bhattasammada, cetaso līnatta (THINA)
    "tandiyanā": "सुस्त होना", "tandimanakatā": "मन का सुस्त होना", "ālasyaṃ": "काहिली",
    "ālasyāyanā": "काहिली करना", "jambhanā": "जम्हाई लेना", "ānamanā": "आगे झुकना",
    "vinamanā": "पीछे झुकना", "sannamanā": "सिकोड़ना", "byādhiyakaṃ": "अस्वस्थ-सी दशा",
    "bhuttāvissa": "भोजन कर चुका व्यक्ति", "mucchā": ["बेसुधी", "मूर्छा"], "kilamatho": "थकान",
    "pariḷāho": ["तपन", "ताप", "जलन"], "duṭṭhullaṃ": "भारीपन",
    "akalyatā": "अस्वस्थता", "akammaññatā": "कार्य-अयोग्यता", "olīyanā": "ढीला पड़ना",
    "sallīyanā": "सिकुड़ जाना", "līnaṃ": "शिथिलता", "līyanā": "शिथिल होना",
    "līyitattaṃ": "शिथिलता से भरा होना", "thinaṃ": "आलस्य", "thīyanā": "आलसी होना",
    # kuhanā, lapanā, nemittikatā, nippesikatā, nijigīsanatā (LSS_GEN / LSS_NOM)
    "lābhasakkārasilokasannissitassa": "लाभ सत्कार और प्रसिद्धि पर टिका", "sannissitassa": "टिका",
    "lābhasakkārasilokasannissito": "लाभ सत्कार और प्रसिद्धि पर टिका", "sannissito": "टिका",
    "pāpicchassa": "बुरी इच्छा वाला", "pāpiccho": "बुरी इच्छा वाला",
    "icchāpakatassa": "इच्छा के वश में पड़ा", "pakatassa": "वश में पड़ा",
    "icchāpakato": "इच्छा के वश में पड़ा", "pakato": "वश में पड़ा",
    "saṅkhātena": "दिखावा", "sāmantajappitena": "घुमा-फिराकर कही गई बात", "jappitena": "कही गई बात",
    "iriyāpathassa": "चाल-ढाल", "aṭhapanā": "जमाना", "ṭhapanā": "टिकाना", "saṇṭhapanā": "अच्छी तरह सँवारना",
    "bhākuṭitā": "भौंहें चढ़ाना", "bhākuṭiyaṃ": "त्योरी चढ़ाना", "kuhāyanā": "पाखंड करना",
    "paresaṃ": "दूसरा", "ālapanā": "बात छेड़ना", "sallapanā": "मीठी बातें करना",
    "samullapanā": "बहुत बढ़ा-चढ़ाकर बोलना", "unnahanā": "फुसलाना", "samunnahanā": "बहुत फुसलाना",
    "ukkācanā": "उकसाना", "anuppiyabhāṇitā": "प्रिय लगने वाली बातें बोलना", "cāṭukamyatā": "चाटुकारिता",
    "muggasūpyatā": "आधा सच आधा झूठ बोलना", "pāribhaṭayatā": "आया की तरह खुशामद करना",
    "nimittaṃ": "संकेत", "nimittakammaṃ": "संकेत करना", "obhāso": "इशारा", "obhāsakammaṃ": "इशारा करना",
    "sāmantajappā": "घुमा-फिराकर बात करना", "jappā": "बात करना", "parikathā": "बात को घुमाना",
    "akkosanā": "गाली देना", "vambhanā": "तिरस्कार करना", "garahaṇā": "निंदा करना",
    "ukkhepanā": "उछालना", "samukkhepanā": "पूरी तरह उछालना", "khipanā": "ताना मारना",
    "saṅkhipanā": "ताने कसना", "pāpanā": "बदनाम करना", "sampāpanā": "पूरी तरह बदनाम करना",
    "avaṇṇa": "अपयश", "hārikā": "फैलाना", "parapiṭṭhimaṃsikatā": "पीठ पीछे बुराई करना",
    "harati": "ले जाना", "āharati": "लाना",
    # BASES (jātiyā vā gottena vā … vatthunā), mānaṃ jappeti, OMANA
    "jātiyā": "जन्म", "gottena": "गोत्र", "kolaputtiyena": "कुलीन परिवार में जन्म",
    "vaṇṇapokkharatāya": "रूप-रंग की सुंदरता", "pokkharatāya": "सुंदरता", "dhanena": "धन",
    "ajjhenena": "अध्ययन", "kammāyatanena": "व्यवसाय", "sippāyatanena": "कला-कौशल", "āyatanena": NDE,
    "vijjāṭṭhānena": "विद्या की" + G + "शाखा", "ṭṭhānena": "शाखा", "sutena": "सुना-सीखा ज्ञान",
    "paṭibhānena": "हाज़िरजवाबी", "vatthunā": "आधार", "mānaṃ": "अहंकार", "jappeti": "पालना",
    "mānaṃ jappeti": "अहंकार पालना", "omānaṃ jappeti": "हीनता का अहंकार पालना",
    "omaññanā": "स्वयं को छोटा मानना", "omaññitattaṃ": "स्वयं को छोटा मान चुका होना", "hīḷanā": "निंदा",
    "ohīḷanā": "स्वयं की निंदा", "attuññā": "स्वयं को तुच्छ समझना", "attavaññā": "स्वयं का तिरस्कार",
    "attaparibhavo": "स्वयं का अपमान",
    # the nine conceits, atimāna … micchāmāna
    "attānaṃ": "स्वयं", "parehi": "दूसरा", "dahati": "मानना", "nissāya": "सहारा", "sadiso": "बराबर",
    "sadisaṃ": "बराबर", "hīno": "हीन", "atimaññati": "बढ़कर मानना",
    "adhigata": "पाया हुआ", "kata": ["किया हुआ", "किया"], "sacchikata": "साक्षात्कार हुआ",
    "saññitā": "मानना", "chando": "चाह", "anusayo": "सुप्त प्रवृत्ति", "pāpakena": "बुरा",
    "pāpakena vā kammāyatanena": "बुरा व्यवसाय", "sīlena": ["नियम-आचरण", "सदाचार"], "vatena": "व्रत",
    "sīlabbatena": "नियम-आचरण और व्रत", "diṭṭhiyā": "दृष्टि",
    # vitakka definitions (68-73)
    "ārabbha": ["लेकर", "विषय बनाना"], "ñātake": "रिश्तेदार", "janapadaṃ": "अपना देश",
    "gehasito": "सांसारिक", "geha": "सांसारिक", "dukkara": "कठोर", "kāritā": "तपस्या",
    "gata": "फँसना", "diṭṭhigata": "दृष्टियों में फँसना",
    "gihīhi": "गृहस्थ", "saṃsaṭṭho": "घुल-मिलकर", "viharati": "रहना", "sahanandī": "साथ आनंदित होना",
    "sahasokī": "साथ शोक करना", "sukhitesu": "सुखी", "dukkhito": "दुःखी", "uppannesu": "आ पड़ना",
    "kicca": "काम-काज", "karaṇīyesu": "काम-काज", "attanā": "स्वयं", "yogaṃ": "जुट जाना",
    "āpajjati": "जुट जाना", "pare": "दूसरा", "avajāniṃsūti": "तिरस्कार करना",
    # the twos: definitions (2-891 … 2-896)
    "kujjhanā": "क्रोध करना", "doso": "द्वेष", "byāpatti": "दुर्भावना", "byāpajjanā": "दुर्भावना रखना",
    "virodho": "विरोध", "paṭivirodho": "प्रतिविरोध", "caṇḍikkaṃ": "उग्रता", "asuropo": "कटु वचन",
    "anattamanatā": "अप्रसन्नता", "aparakālaṃ": "बाद में", "upanayhanā": "बैर रखना",
    "aṭṭhapanā": "मन में जमाए रखना", "anusaṃsandanā": "बार-बार जोड़ते रहना",
    "anuppabandhanā": "लगातार बनाए रखना",
    "makkhāyanā": "नीचा दिखाने की क्रिया", "niṭṭhuriyaṃ": "निष्ठुरता",
    "niṭṭhuriyakammaṃ": "निष्ठुर व्यवहार करना", "paḷāsāhāro": "होड़ का रवैया", "vivāda": ["विवाद", "झगड़ा"],
    "yugaggāho": "बराबरी पर अड़ना", "appaṭinissaggo": "अपनी बात न छोड़ना",
    "para": "दूसरा", "mānana": "आदर", "vandana": "वंदना", "pūjanāsu": "पूजा", "issāyanā": "ईर्ष्या करना",
    "usūyā": "जलन", "usūyanā": "जलना", "āvāsa": "निवास-स्थान", "kula": "परिवार", "dhamma": ["शिक्षा", "मन के विषय"],
    "macchariyaṃ": "कंजूसी", "maccharāyanā": "कंजूसी करना", "vevicchaṃ": "लोभीपन", "kadariyaṃ": "कृपणता",
    "kaṭukañcukatā": "मुट्ठी भींचे रखना", "aggahitattaṃ": "संकुचित होना",
    "kāyena": "शरीर", "vācāya": "वाणी", "manasā": "मन", "duccaritaṃ": "दुराचरण", "caritvā": "करके",
    "paṭicchādanahetuṃ": "छिपाने के लिए", "pāpikaṃ": "बुरा", "icchaṃ": "इच्छा", "paṇidahati": "ठान लेना",
    "jaññā": "जान पाना", "saṅkappeti": "संकल्प करना", "vācaṃ": "बात", "bhāsati": "बोलना",
    "parakkamati": "प्रयत्न करना", "māyāvitā": "कपटीपन", "accāsarā": "अति-चालाकी", "vañcanā": "ठगी",
    "nikati": "छल", "vikiraṇā": "बात घुमाना", "pariharaṇā": "टालमटोल", "gūhanā": "छिपाना",
    "parigūhanā": "पूरी तरह छिपाना", "chādanā": "ढकना", "anuttānīkammaṃ": "साफ़-साफ़ न बताना",
    "anāvikammaṃ": "प्रकट न करना", "vocchādanā": "अच्छी तरह ढक देना", "kiriyā": "कर्म",
    "saṭho": "धूर्त", "parisaṭho": "पूरी तरह धूर्त", "saṭhaṃ": "धूर्तपन", "sāṭheyyaṃ": "धूर्तता",
    "kakkaratā": "कुटिलता", "kakkariyaṃ": "कुटिल व्यवहार",
    "aññāṇaṃ": "न जानना", "adassanaṃ": "न देखना", "laṅgī": "रुकावट", "moho": "मोह", "mūlaṃ": "मूल",
    "akusalamūlaṃ": "हानिकर मूल", "nandī": "आनंद", "sineho": "स्नेह", "ajjhosānaṃ": "चिपके रहना",
    "bhavissati": "बने रहना", "attā": "आत्मा", "diṭṭhigataṃ": "दृष्टियों में फँसना", "gataṃ": "फँसना",
    "vipariyāsaggāho": "उलटी पकड़", "vipariyāsa": "उलटा", "ggāho": "पकड़",
})
# ---------------------------------------------------------------- the twos: 2-897 … 2-908
T.update({
    "sassato": "शाश्वत", "uppajjati": "उत्पन्न होना", "uppajjati diṭṭhi": "दृष्टि" + G + "उत्पन्न होना",
    "sahadhammike": "शिक्षा के अनुसार", "vuccamāne": "कहा जाना", "dovacassāyaṃ": "सलाह न मानना",
    "dovacassiyaṃ": "सलाह न मानने का भाव", "vippaṭikula": "उलटा", "anādaratā": "अनादर का भाव",
    "puggalā": "व्यक्ति", "assaddhā": "श्रद्धाहीन", "dussīlā": "दुराचारी", "appassutā": "कम सुना-सीखा",
    "maccharino": "कंजूस", "duppaññā": "प्रज्ञाहीन", "sevanā": "संगति", "nisevanā": "लगातार संगति",
    "bhajanā": "मेल-जोल", "sambhajanā": "घनिष्ठ मेल-जोल", "bhatti": "लगाव", "sampavaṅkatā": "झुकाव",
    "anajjavatā": "सरल न होना", "amaddavatā": "कोमलता का अभाव",
    "akkhamanatā": "क्षमा न करना", "anadhivāsanatā": "सह न पाना", "kāyiko": "शरीर", "vācasiko": "वाणी",
    "vītikkamo": "उल्लंघन", "asoraccaṃ": "सौम्यता का अभाव",
    "vācā": "वाणी", "kaṇḍakā": "काँटेदार", "kakkasā": "कठोर", "kaṭukā": "कड़वा लगने वाला",
    "ābhisajjanī": "चुभने वाला", "kodha": "क्रोध", "sāmantā": "निकट",
    "asamādhisaṃvattanikā": "एकाग्रता की ओर न ले जाने वाला", "saṃvattanikā": "की ओर ले जाने वाला",
    "bhāsitā": "बोलने वाला", "asaṇhavācatā": "कोमल न होने वाली वाणी",
    "asakhilavācatā": "मधुर न होने वाली वाणी", "pharusavācatā": "कठोर वाणी",
    "asākhalyaṃ": "मधुर व्यवहार का अभाव", "paṭisanthārā": "आदर-सत्कार", "āmisa": "भौतिक वस्तु",
    "appaṭisanthārako": "आदर-सत्कार न करने वाला",
    # indriyesu aguttadvāratā (pi-1 INDRIYA_AGUTTA), bhojane amattaññutā
    "cakkhunā": "आँख", "rūpaṃ": ["भौतिक रूप", "दृश्य रूप"], "nimitta": "समग्र छवि", "ggāhī": "पकड़ना",
    "cakkhundriyaṃ": ["आँख की इंद्रिय", "आँख की क्षमता"], "indriyaṃ": ["इंद्रिय", "क्षमता"],
    "indriyaṃ asaṃvutaṃ": "इंद्रिय को असंयमित छोड़कर", "asaṃvutaṃ": "असंयमित", "viharantaṃ": "रहना",
    "abhijjhādomanassā": "लालच और उदासी", "abhijjhā": "लालच", "domanassā": "उदासी", "pāpakā": "बुरा",
    "akusalā": "हानिकर", "akusalā dhammā": "हानिकर परिघटना", "anvāssaveyyuṃ": "घुस आ सकना",
    "saṃvarāya": "संयम", "paṭipajjati": "प्रयत्न" + G + "करना", "rakkhati": "रक्षा" + G + "करना",
    "saṃvaraṃ āpajjati": "संयम" + G + "रखना", "sotena": "कान", "saddaṃ": "ध्वनि", "sutvā": "सुनकर",
    "ghānena": "नाक", "gandhaṃ": "गंध", "ghāyitvā": "सूँघकर", "jivhāya": "जीभ", "rasaṃ": "स्वाद",
    "sāyitvā": "चखकर", "phoṭṭhabbaṃ": "स्पर्श", "phusitvā": "अनुभव करके", "dhammaṃ": "मन का विषय",
    "viññāya": "जानकर", "manindriyaṃ": ["मन की इंद्रिय", "मन की क्षमता"],
    "manindriyaṃ asaṃvutaṃ": "मन की इंद्रिय को असंयमित छोड़कर", "indriyānaṃ": "इंद्रिय",
    "agutti": "रक्षा न करना", "agopanā": "न सँभालना", "anārakkho": "चौकसी न करना",
    "appaṭisaṅkhā": "बिना सोचे-विचारे", "ayoniso": ["अनुचित ढंग से", "अनुचित"], "āhāraṃ": "भोजन",
    "āhāreti": "भोजन करना", "davāya": "मौज", "madāya": "मद", "maṇḍanāya": "शरीर सुडौल बनाना",
    "vibhūsanāya": "सुंदर दिखना", "asantuṭṭhitā": ["असंतोष", "संतुष्ट न होना"],
    # muṭṭhassacca (pi-1), sīla-/diṭṭhivipatti, ajjhatta-/bahiddhāsaṃyojana
    "assati": "सजगता का अभाव", "ananussati": "बार-बार स्मरण का अभाव", "appaṭissati": "पुनः स्मरण का अभाव",
    "adhāraṇatā": "धारण न करना", "sammusanatā": "भूल जाना",
    "natthi": ["व्यर्थ", "नहीं"], "sayaṃ": "स्वयं", "abhiññā": "उच्च ज्ञान", "sacchikatvā": "साक्षात्कार करके",
    "pavedentī": "बताना", "saṃyojanaṃ": "बंधन",
})

# ---------------------------------------------------------------- the threes: 2-909 … 2-918
T.update({
    # lobha (LOBHA_SYN_1 … 5, pi-1 order)
    "anunayo": "झुकाव", "anurodho": "अनुकूल होना", "nandirāgo": "आनंद का राग", "parigedho": "गहरी लालसा",
    "saṅgo": "लगाव", "paṅko": "कीचड़", "ejā": "हलचल", "janikā": "जन्म देने वाली",
    "sañjananī": "उत्पन्न करने वाली", "sibbinī": "सिलने वाली", "jālinī": "जाल बुनने वाली",
    "saritā": "धारा", "visattikā": "फँसाने वाली", "sotaṃ": "प्रवाह", "visaṭā": "फैली हुई",
    "āyūhanī": "जुटाने वाली", "dutiyā": "साथिन", "paṇidhi": "आकांक्षा", "netti": "डोर", "vanaṃ": "वन",
    "vanatho": "झाड़-झंखाड़", "santhavo": "घनिष्ठता", "apekkhā": "अपेक्षा", "paṭibandhu": "नाता",
    "āsā": "आशा", "āsīsanā": "आशा करना", "rūpāsā": "दृश्य रूप की आशा", "saddāsā": "ध्वनि की आशा",
    "gandhāsā": "गंध की आशा", "rasāsā": "स्वाद की आशा", "phoṭṭhabbāsā": "स्पर्श की आशा",
    "dhanāsā": "धन की आशा", "puttāsā": "संतान की आशा", "jīvitāsā": "जीवन की आशा",
    "jappā": ["तड़प", "बात करना"], "abhijappā": "अत्यधिक तड़प", "adhamma": ["अनैतिक", "अनुचित"],
    "visama": "अनुचित", "lobho": "लोभ", "nikanti": "रुचि", "pihanā": "ललक",
    "kāmataṇhā": "इंद्रिय-सुखों की तृष्णा", "vibhavataṇhā": "अनस्तित्व की तृष्णा",
    "rūpataṇhā": "सूक्ष्म भौतिक लोक की तृष्णा", "nirodhataṇhā": "समाप्ति की तृष्णा",
    "rūpa": ["भौतिक रूप", "सूक्ष्म भौतिक", "दृश्य रूप"], "arūpa": "अभौतिक",
    "ogho": "बाढ़", "yogo": "जकड़न", "gantho": "गाँठ", "āvaraṇaṃ": "आवरण", "nīvaraṇaṃ": "बाधा",
    "chadanaṃ": "पर्दा", "bandhanaṃ": "बेड़ी", "upakkileso": "मलिनता", "pariyuṭṭhānaṃ": "आवेश",
    "latā": "लता", "dukkha": ["दुःखद", "दुःख"], "nidānaṃ": "स्रोत", "pabhavo": "उद्गम",
    "dukkhappabhavo": "दुःख का उद्गम", "pāso": "फंदा", "baḷisaṃ": "काँटा", "gaddulaṃ": "पट्टा",
    "samuddo": "सागर",
    # dosa (DOSA_1/2, KODHA_SYN)
    "anatthaṃ": "अहित", "acarī": "किया", "carati": "करना", "āghāto": "आक्रोश", "jāyati": "उत्पन्न होना",
    "āghāto jāyati": "आक्रोश उत्पन्न होना", "piyassa": "प्रिय", "manāpassa": "मनभावन",
    "appiyassa": "अप्रिय", "amanāpassa": "मन को न भाने वाला", "aṭṭhāne": "बिना कारण",
    "paṭighaṃ": "चिढ़", "kopo": "कोप", "pakopo": "प्रकोप", "padoso": "गहरा द्वेष",
    "manopadoso": "मन का गहरा द्वेष", "kujjhitattaṃ": "क्रोध से भरा होना",
    # moha (MOHA_KNOW)
    "dukkhe": "दुःख", "dukkhanirodhe": "दुःख का अंत", "nirodha": ["समाप्ति", "अंत"],
    "idappaccayatā": "कार्य-कारण का नियम", "samuppannesu": "उत्पन्न", "akusalamūlāni": "हानिकर मूल",
    # vitakka / saññā / dhātu / duccarita
    "kāmapaṭisaṃyutto": "इंद्रिय-सुखों से जुड़ा", "kāmapaṭisaṃyuttā": "इंद्रिय-सुखों से जुड़ा",
    "paṭisaṃyuttā": "जुड़ा", "kāmavitakko": "इंद्रिय-सुखों का विचार", "byāpādavitakko": "दुर्भावना का विचार",
    "vihiṃsāvitakko": "हिंसा का विचार", "byāpāda": "दुर्भावना", "vihiṃsā": "हिंसा",
    "kāmasaññā": "इंद्रिय-सुखों की पहचान",
    "kāmadhātu": ["इंद्रिय-सुखों का तत्व", "इंद्रिय-सुखों का लोक"], "dhātu": ["तत्व", "लोक"],
    "byāpādadhātu": "दुर्भावना का तत्व", "vihiṃsādhātu": "हिंसा का तत्व",
    "pāṇātipāto": "जीवों की हत्या", "ātipāto": "हत्या", "ādānaṃ": "लेना", "kāmesu": "इंद्रिय-सुख",
    "musāvādo": "झूठ बोलना", "musā": "झूठ", "pisuṇā": "चुगली", "pharusā": "कठोर",
    "samphappalāpo": "व्यर्थ की बकवास", "byāpādo": "दुर्भावना", "kāyaduccaritaṃ": "शारीरिक दुराचरण",
    "vacīduccaritaṃ": "वाचिक दुराचरण", "manoduccaritaṃ": "मानसिक दुराचरण",
    "kāyakammaṃ": "शारीरिक कर्म", "vacīkammaṃ": "वाचिक कर्म", "manokammaṃ": "मानसिक कर्म",
    "akusalaṃ": "हानिकर", "akusalaṃ kāyakammaṃ": "हानिकर शारीरिक कर्म",
    "akusalaṃ vacīkammaṃ": "हानिकर वाचिक कर्म", "akusalaṃ manokammaṃ": "हानिकर मानसिक कर्म",
    "sañcetanā": "इरादा",
    # sakkāyadiṭṭhi (PUTHUJJANA), vicikicchā, sīlabbataparāmāsa
    "sakkāya": "स्थायी आत्मा", "assutavā": "अशिक्षित", "puthujjano": "साधारण व्यक्ति",
    "adassāvī": "दर्शन नहीं करना", "akovido": "निपुण नहीं", "avinīto": "प्रशिक्षित नहीं",
    "dhammassa": "शिक्षा", "purisānaṃ": "सज्जन", "attato": "आत्मा के रूप में", "samanupassati": "देखना",
    "rūpaṃ attato samanupassati": "भौतिक रूप को आत्मा के रूप में देखना", "vantaṃ": "वाला",
    "vedanaṃ": "अनुभूति", "saññaṃ": "पहचान", "saṅkhāre": "मानसिक रचनाएँ",
    "satthari": "गुरु", "saṅghe": "संघ", "sikkhāya": "प्रशिक्षण", "kaṅkhati": "शंका करना",
    "vicikicchati": "संशय करना", "vicikicchā": "संशय", "kaṅkhāyanā": "शंका करना",
    "thambhitattaṃ": "जड़ हो जाना", "manovilekho": "मन की खरोंच", "samaṇa": "श्रमण",
    "brāhmaṇānaṃ": "ब्राह्मण", "suddhi": "शुद्धि", "sīlabbatena": ["नियम-आचरण और व्रत", "सदाचार और व्रत"],
    # taṇhā triads
    "sahagato": "के साथ होने वाला", "avasesā": "बाकी",
})
# ---------------------------------------------------------------- the threes: 2-919 … 2-936
T.update({
    "kāmesanā": "इंद्रिय-सुखों की खोज", "bhavesanā": "अस्तित्व की खोज", "brahmacariyesanā": "पवित्र जीवन की खोज",
    "maraṇā": "मृत्यु", "paraṃ maraṇā": "मृत्यु के बाद", "hoti": ["रहना", "होना"],
    "tadekaṭṭhaṃ": "उसके साथ जुड़ा", "ekaṭṭhaṃ": "साथ जुड़ा",
    "sadisohamasmī": "मैं बराबर हूँ", "hīnohamasmī": "मैं हीन हूँ",
    "jarā": "बुढ़ापा", "maraṇa": "मृत्यु", "bhayaṃ": "भय", "bhayānakaṃ": "डर", "chambhitattaṃ": "घबराहट",
    "lomahaṃso": "रोंगटे खड़े होना", "utrāso": "दहल जाना", "cetaso utrāso": "मन का दहल जाना",
    "nādhimuccati": "निश्चय नहीं कर पाना", "sampasīdati": "आश्वस्त" + G + "होना",
    "samaṇo": "श्रमण", "brāhmaṇo": "ब्राह्मण", "evaṃvādī": "ऐसा कहने वाला", "evaṃdiṭṭhī": "ऐसी दृष्टि वाला",
    "diṭṭhī": "दृष्टि", "yaṃ kiñcāyaṃ": "जो कुछ भी", "purisapuggalo": "व्यक्ति",
    "paṭisaṃvedeti": "अनुभव करना", "sukhaṃ": "सुख", "dukkhaṃ": "दुःख",
    "adukkhamasukhaṃ": ["न दुःखद न सुखद", "न दुःख न सुख"], "hetū": ["मूल", "कारण"],
    "issara": "ईश्वर", "nimmāna": "रचना", "ahetu": "बिना किसी कारण", "appaccayā": "बिना किसी आधार",
    "kiñcanaṃ": "बोझ", "doso": ["द्वेष", "दोष"], "pātabyataṃ āpajjati": "डूब जाना",
    "avūpasamo": "अशांति", "bhantattaṃ": "डाँवाडोल होना", "bhavantattaṃ": "डाँवाडोल होना",
    "anaddā": "उपेक्षा", "anaddāyanā": "उपेक्षा करना", "asīlyaṃ": "अशिष्टता", "acittīkāro": "सम्मान न करना",
    "buddhaṃ": "बुद्ध", "saṅghaṃ": "संघ", "saddahati": "श्रद्धा" + G + "रखना",
    "assaddahanā": "श्रद्धा न रखना", "anokappanā": "भरोसा न करना",
    "buddhā": "बुद्ध", "sāvakā": "शिष्य", "adaṭṭhukamyatā": "न देखने की इच्छा",
    "asamāgantukamyatā": "न मिलने की इच्छा",
    "anicce": "अनित्य", "nicca": "नित्य", "sukha": "सुख", "asubhe": "अशुभ", "subha": "शुभ", "sacca": "सत्य",
    "vippaṭikulena": "विपरीत", "āvaṭṭanā": "मुड़ना", "anāvaṭṭanā": "बार-बार मुड़ना", "ābhogo": "ध्यान देना",
    "samannāhāro": "ध्यान में लाना",
})
# ---------------------------------------------------------------- the fours … eights: 2-937 … 2-956
T.update({
    "upādānāni": "आसक्ति", "uppādā": "उत्पन्न होने का" + G + "कारण",
    "taṇhuppādā": "तृष्णा के उत्पन्न होने का" + G + "कारण", "bhikkhuno": "भिक्षु",
    "sīlabbata": "सदाचार और व्रत", "kāmacchando": "इंद्रिय-सुखों की चाह",
    "sabrahmacārīsu": "साथी साधक", "kupito": "कुपित", "anattamano": "अप्रसन्न",
    "āhatacitto": "आहत मन वाला", "khilajāto": "कठोर हो जाना", "dhamme": ["शिक्षा", "परिघटना"],
    "surā": "शराब", "meraya": "शराब", "majja": "नशीली चीज़", "pamāda": "लापरवाही", "ṭṭhānā": "कारण",
    "micchācāro": "दुराचार", "vādo": "बोलना",
    # diṭṭhadhammanibbānavāda (2-943)
    "evaṃdiṭṭhi": ["ऐसी दृष्टि वाला", "ऐसी दृष्टि"], "bho": "मित्र", "samappito": "युक्त",
    "samaṅgībhūto": "घिरा हुआ", "paricāreti": "आनंद लेना", "ettāvatā": "इतने से", "parama": "परम",
    "paramadiṭṭhadhammanibbāna": "इसी जीवन में परम निर्वाण",
    "paramadiṭṭhadhammanibbānappatto": "इसी जीवन में परम निर्वाण पा लेना",
    "paramadiṭṭhadhammanibbānaṃ paññapenti": "इसी जीवन में परम निर्वाण की घोषणा करना",
    "paññapenti": "घोषणा करना", "sato": "विद्यमान", "vadesi": "बात करना", "natthīti": "नहीं है",
    "kissa hetu": "किस कारण", "kāmā": "इंद्रिय-सुख", "aniccā": "अनित्य", "dukkhā": "दुःखद",
    "vipariṇāmadhammā": "बदलने के स्वभाव वाला", "aññathābhāvā": "कुछ और हो जाना",
    "uppajjanti": "उत्पन्न होना", "sokaparidevadukkhadomanassupāyāsā": "शोक विलाप दुःख उदासी और निराशा",
    "soka": "शोक", "parideva": "विलाप", "upāyāsā": "निराशा", "vivicceva": "अलग होकर",
    "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर", "upasampajja": "प्राप्त करके",
    "upasampajja viharati": "प्राप्त करके उसमें रहना", "yadeva": "जो कुछ", "vitakkitaṃ": "आरंभिक विचार",
    "vicāritaṃ": "सतत विचार", "vitakkitaṃ vicāritaṃ": "आरंभिक विचार और सतत विचार",
    "oḷārikaṃ": "स्थूल", "akkhāyati": "कहा जाना",
    "vitakkavicārānaṃ vūpasamā": "आरंभिक विचार और सतत विचार का शांत होना", "vūpasamā": "शांत होना",
    "uppilāvitaṃ": "उछाह", "virāgā": "फीका पड़ना", "ābhogo": ["ध्यान देना", "झुकाव"],
    "sukhassa ca pahānā": "सुख को छोड़ना", "pahānā": "छोड़ना", "catutthaṃ jhānaṃ": "चौथा ध्यान",
    # sixes
    "sandiṭṭhi": "अपनी दृष्टि", "appatisso": "बात पर कान न देना", "agāravo": "अनादर",
    "agāravo viharati": "अनादर के साथ" + G + "रहना", "appamāde": "लापरवाही न करना",
    "paṭisanthāre": "आदर-सत्कार", "kammārāmatā": "काम-काज में रमना", "ārāmatā": "रमना",
    "bhassārāmatā": "बातचीत में रमना", "niddārāmatā": "नींद में रमना",
    "manāpiyesu": "मनभावन", "rūpesu": "दृश्य रूप", "saddesu": "ध्वनि", "gandhesu": "गंध",
    "rasesu": "स्वाद", "phoṭṭhabbesu": "स्पर्श", "gehasitaṃ": "सांसारिक",
    "gehasitaṃ cetasikaṃ sātaṃ": "सांसारिक मानसिक सुहावनापन", "cetosamphassa": "मन का संपर्क",
    "sātaṃ sukhaṃ": "सुहावना सुखद", "sātaṃ sukhaṃ vedayitaṃ": "सुहावना सुखद अनुभव",
    "sātā sukhā vedanā": "सुहावनी सुखद अनुभूति",
    "me": "मेरा", "saccato": "सत्य", "thetato": "पक्का", "saccato thetato": "सत्य और पक्का",
    "diṭṭhi uppajjati": "दृष्टि उत्पन्न होना", "sañjānāmī": "पहचानना", "anattānaṃ": "अनात्म",
    "vado": "बोलने वाला", "vedeyyo": "अनुभव करने वाला", "kammānaṃ": "कर्म", "paccanubhoti": "भोगना",
    "jāto": "उत्पन्न", "nāhosi": "न रहना", "nicco": "नित्य", "dhuvo": "स्थिर",
    "avipariṇāmadhammo": "न बदलने वाला",
    # sevens
    "kāmarāgānusayo": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति", "paṭighānusayo": "चिढ़ की सुप्त प्रवृत्ति",
    "mānānusayo": "अहंकार की सुप्त प्रवृत्ति", "diṭṭhānusayo": "दृष्टि की सुप्त प्रवृत्ति",
    "vicikicchānusayo": "संशय की सुप्त प्रवृत्ति", "avijjānusayo": "अज्ञान की सुप्त प्रवृत्ति",
    "ānusayo": "सुप्त प्रवृत्ति", "ahiriko": "निर्लज्ज", "anottappī": "बुराई के प्रति निडर",
    # seven annihilationist views (2-951)
    "rūpī": "भौतिक रूप वाला", "mahābhūtiko": "महाभूतों से बना", "bhūtiko": "महाभूतों से बना",
    "mātā": "माता", "pettika": "पिता", "sambhavo": "उत्पन्न", "bhedā": "छूटना",
    "vinassati": "विनष्ट हो जाना", "hoti paraṃ maraṇā": "मृत्यु के बाद" + G + "रहना",
    "sammā": ["पूरी तरह", "पूर्ण रूप से", "सही"], "sammā samucchinno": "पूरी तरह मिट जाना",
    "ettāvatā sammā": "इतने से" + G + "पूरी तरह", "ettāvatā sammā samucchinno": "इतने से" + G + "पूरी तरह मिट जाना",
    "ucchedaṃ": "पूर्ण नाश", "vināsaṃ": "विनाश", "vibhavaṃ": "मिट जाना", "dibbo": "दिव्य",
    "kāmāvacaro": ["इंद्रिय-सुखों के लोक से संबंधित", "इंद्रिय-सुखों के लोक का"],
    "āvacaro": ["लोक से संबंधित", "लोक का"], "kabaḷīkāra": "कौर-कौर खाया जाने वाला",
    "bhakkho": "खाने वाला", "jānāsi": "जानना", "manomayo": "मन से बना",
    "sabbaṅgapaccaṅgī": "सभी बड़े-छोटे अंगों से युक्त", "ahīnindriyo": "पूर्ण इंद्रियों वाला",
    "indriyo": "इंद्रिय", "sabbaso": "पूरी तरह", "rūpasaññānaṃ": "भौतिक रूप की पहचान",
    "saññānaṃ": "पहचान", "samatikkamā": "पार कर जाना", "paṭighasaññānaṃ": "टकराव की पहचान",
    "paṭigha": ["टकराव", "चिढ़"], "atthaṅgamā": "मिट जाना", "nānattasaññānaṃ": "विविधता की पहचान",
    "amanasikārā": "मनोयोग न करना", "ananto": "अनंत", "ākāso": "आकाश",
    "ākāsānañcāyatanaṃ": "अनंत आकाश का क्षेत्र", "viññāṇañcāyatanaṃ": "अनंत चेतना का क्षेत्र",
    "ākiñcaññāyatanaṃ": "कुछ भी न होने का क्षेत्र", "natthi kiñcīti": "कुछ भी नहीं है",
    "āyatanūpago": "क्षेत्र तक पहुँचा हुआ", "ākiñcaññāyatanūpago": "कुछ भी न होने के क्षेत्र तक पहुँचा हुआ",
    "nevasaññānāsaññāyatanūpago": "न पहचान न अ-पहचान के क्षेत्र तक पहुँचा हुआ",
    "āyatanaṃ": ["इंद्रिय-क्षेत्र", "क्षेत्र"], "viññāṇa": "चेतना",
    # eights
    "lobho": "लोभ", "bhikkhunā": "भिक्षु", "kataṃ": "कर लिया", "tassa evaṃ hoti": "उसे ऐसा होना",
    "karontassa": "करते हुए", "kāyo": "शरीर", "kilamissati": "थक जाना", "handāhaṃ": "चलो मैं",
    "nipajjāmī": "लेट जाना", "nipajjati": "लेट जाना", "vīriyaṃ": "उत्साह", "ārabhati": "जगाना",
    "vīriyaṃ ārabhati": "उत्साह" + G + "जगाना", "appattassa": "प्राप्त नहीं हुआ", "pattiyā": "प्राप्ति",
    "appattassa pattiyā": "प्राप्त नहीं हुआ उसकी प्राप्ति", "anadhigatassa": "पाया नहीं",
    "adhigamāya": "पाना", "anadhigatassa adhigamāya": "पाया नहीं उसे पाना",
    "asacchikatassa": "साक्षात्कार नहीं हुआ", "sacchikiriyāya": "साक्षात्कार",
    "asacchikatassa sacchikiriyāya": "साक्षात्कार नहीं हुआ उसका साक्षात्कार",
    "kappo": "ठीक", "maggo": ["मार्ग", "रास्ता"], "gāmaṃ": "गाँव", "nigamaṃ": "कस्बा", "piṇḍāya": "भिक्षा",
    "caranto": "घूमना", "piṇḍāya caranto": "भिक्षा के लिए घूमना", "labhati": "पाना", "alatthaṃ": "पाया",
    "lūkhassa": "रूखा-सूखा", "paṇītassa": "बढ़िया", "bhojanassa": "भोजन", "yāvadatthaṃ": "जितना चाहिए उतना",
    "kilanto": "थका हुआ", "akammañño": "काम के लायक़ नहीं", "māsācitaṃ": "भीगे उड़द-सा भारी",
    "uppanno": ["उत्पन्न हो चुका", "हो जाना"], "appamattako": "छोटा-सा", "ābādho": "रोग", "gelaññā": "रोग",
    "vuṭṭhito": "उठा", "dubbalo": "दुर्बल", "kusītavatthu": "आलसीपन का आधार",
    "yase": "यश", "ayase": "अपयश", "pasaṃsāya": "प्रशंसा", "nindāya": "निंदा", "sukhe": "सुख",
    "viññāta": "जाना हुआ", "muta": "अनुभव किया हुआ",
    "ājīvo": "आजीविका",
})
# ---------------------------------------------------------------- eights (purisadosa, the 2×8 vāda) … tens
T.update({
    "bhikkhū": "भिक्षु", "bhikkhuṃ": "भिक्षु", "bhikkhu": "भिक्षु", "āpattiyā": "अपराध",
    "codenti": "आरोप लगाना", "codiyamāno": "आरोप लगाए जाना", "sarāmi": "याद",
    "assatiyāva": "भूलने का बहाना", "nibbeṭheti": "टाल देना", "codakaṃyeva": "आरोप लगाने वाला",
    "paṭippharati": "पलटवार करना", "kiṃ nu kho": "क्या", "bālassa": "मूर्ख", "abyattassa": "अनाड़ी",
    "bhaṇitena": "कहना", "bhaṇitabbaṃ": "कुछ कहना", "nāma": NDE, "paccāropeti": "उलटा आरोप लगाना",
    "itthannāmaṃ": "अमुक", "āpanno": "किया", "paṭikarohī": "प्रायश्चित्त करना",
    "aññenāññaṃ": "एक बात से दूसरी बात", "paṭicarati": "टाल देना", "apanāmeti": "मोड़ देना",
    "kopañca": "क्रोध", "dosañca": "द्वेष", "appaccayañca": "असंतोष", "pātukaroti": "प्रकट करना",
    "majjhe": "बीच", "bāhā": "हाथ", "vikkhepakaṃ": "फेंक-फेंककर", "bhaṇati": "बोलना",
    "anādiyitvā": "परवाह न करके", "sāpattikova": "अपराधी", "yenakāmaṃ": "जहाँ मन हो",
    "pakkamati": "चला जाना", "tuṇhībhūto": "चुप रहकर", "viheseti": "परेशान करना",
    "āyasmanto": "आयुष्मान", "atibāḷhaṃ": "इतना", "byāvaṭā": "पीछे" + G + "पड़ना", "sikkhaṃ": "प्रशिक्षण",
    "paccakkhāya": "छोड़कर", "hīnāyāvattissāmī": "गृहस्थ जीवन में लौट जाना", "āvattissāmī": "लौट जाना",
    "āvattitvā": "लौटकर", "attamanā": "प्रसन्न", "pañcamo": "पाँचवाँ", "chaṭṭho": "छठा",
    "sattamo": "सातवाँ", "aṭṭhamo": "आठवाँ",
    "rūpī": "भौतिक रूप वाला", "arūpī": "भौतिक रूप से रहित", "arogo": "विकार-रहित",
    "arogo paraṃ maraṇā": "मृत्यु के बाद" + G + "विकार-रहित",
    "asaññīti naṃ paññapenti": "उसे पहचान से रहित बताना", "saññī": "पहचान वाला",
    "nāsaññī": "न पहचान से रहित", "saññīnāsaññī": "पहचान वाला न पहचान से रहित",
    "taṇhaṃ": "तृष्णा", "vinicchayo": "निर्णय", "chandarāgo": "चाह भरा राग", "pariggaho": "अपना बना लेना",
    "ārakkho": "रखवाली", "ādhikaraṇaṃ": "कारण", "daṇḍādāna": "डंडा उठाना", "satthādāna": "शस्त्र उठाना",
    "ādāna": "उठाना", "kalaha": "कलह", "viggaha": "झगड़ा", "tuvaṃtuvaṃ": "तू-तू मैं-मैं",
    "pesuñña": "चुगली", "musāvādā": "झूठ बोलना",
    "iñjitametaṃ": "यह हलचल", "saṅkhatametaṃ": "यह निर्मित",
    "māna": "अहंकार", "rāga": "राग", "macchariya": "कंजूसी", "ñāṇaṃ": "ज्ञान", "vimutti": "मुक्ति",
    "hutaṃ": "आहुति", "sukata": "अच्छा", "dukkaṭānaṃ": "बुरा", "phalaṃ": "फल", "pitā": "पिता",
    "sattā": "प्राणी", "opapātikā": "स्वतः जन्म लेने वाला", "brāhmaṇā": "ब्राह्मण",
    "sammaggatā": "सही मार्ग पर पहुँचा हुआ", "paṭipannā": "साधना करने वाला", "pavedentīti": "बताना",
    "jīvaṃ": "जीव", "sarīra": "शरीर", "hoti tathāgato": "तथागत रहना",
})
# ---------------------------------------------------------------- the 2-U.. definitions (threes … sevens)
T.update({
    "pāṇinā": "हाथ", "leḍḍunā": "ढेला", "daṇḍena": "डंडा", "satthena": "शस्त्र", "rajjuyā": "रस्सी",
    "aññataraññatarena": "किसी और", "satte": "प्राणी", "viheṭheti": "सताना", "heṭhanā": "सताना",
    "viheṭhanā": "बहुत सताना", "hiṃsanā": "चोट पहुँचाना", "vihiṃsanā": "बहुत चोट पहुँचाना",
    "rosanā": "चिढ़ाना", "virosanā": "बहुत चिढ़ाना", "parūpaghāto": "दूसरों को हानि पहुँचाना",
    "ūpaghāto": "हानि पहुँचाना", "visamacariyā": "विषम आचरण", "visama": ["विषम", "अनुचित"],
    "akusalā saññā": "हानिकर पहचान", "paṭisevanā": "बार-बार संगति", "malaṃ": "कलुष",
    "satipaṭṭhānā": "सजगता के आधार", "sati": "सजगता", "paṭṭhānā": "आधार", "sammappadhānā": "सही प्रयत्न",
    "padhānā": "प्रयत्न", "iddhipādā": "सिद्धि के आधार", "pādā": "आधार", "indriyāni": "क्षमता",
    "bojjhaṅgā": "जागृति के" + G + "अंग", "aṭṭhaṅgiko": "आठ अंगों वाला",
    "aṭṭhaṅgiko maggo": "आठ अंगों वाला" + G + "मार्ग", "ariyo": "आर्य",
    "asavanakamyatā": "कान न देने की इच्छा", "anuggahetukamyatā": "ग्रहण न करने की इच्छा",
    "adhāretukamyatā": "धारण न करने की इच्छा",
    "upārambho": "दोष ढूँढना", "anupārambho": "बार-बार दोष ढूँढना", "upārambhanā": "दोष निकालना",
    "anupārambhanā": "बार-बार दोष निकालना", "uññā": "तुच्छ समझना", "avaññā": "तिरस्कार",
    "paribhavo": "अपमान", "randha": "छिद्र", "visamaṃ": "विषमता", "taṃsampavaṅkatā": "उसकी ओर झुकाव",
    "kummaggo": "कुमार्ग", "thiyanā": "आलसी होना",
    "nirodhe": "अंत", "samudaye": "उत्पत्ति", "dukkhasamudaye": "दुःख की उत्पत्ति",
    "sīlabbatupādānañca": "सदाचार और व्रतों के प्रति आसक्ति",
    "attavādupādānañca": "आत्मा के सिद्धांत के प्रति आसक्ति",
    "chandāgatiṃ": "चाह के कारण ग़लत राह", "dosāgatiṃ": "द्वेष के कारण ग़लत राह",
    "mohāgatiṃ": "मोह के कारण ग़लत राह", "bhayāgatiṃ": "भय के कारण ग़लत राह", "āgatiṃ": "ग़लत राह",
    "gacchati": "जाना", "agatigamanaṃ": "ग़लत राह पर जाना", "vagga": "गुटबाज़ी", "vāri": "पानी",
    "vipariyāso": "उलटापन", "saññāvipariyāso": "पहचान का उलटापन", "cittavipariyāso": "मन का उलटापन",
    "diṭṭhivipariyāso": "दृष्टि का उलटापन", "aviññātavāditā": "जाने को न जाना हुआ कहना",
    "amutavāditā": "अनुभव किए को अनुभव न किया हुआ कहना", "byādhi": "रोग",
    "rāja": "राजा", "cora": "चोर", "aggi": ["आग", "अग्नि"], "udaka": "पानी", "ūmi": "लहर",
    "kumbhīla": "मगरमच्छ", "āvaṭṭa": "भँवर", "susukā": "सूँस", "attānuvāda": "आत्म-निंदा",
    "parānuvādabhayaṃ": "दूसरों द्वारा निंदा का भय", "ānuvāda": "निंदा", "daṇḍa": "दंड", "duggati": "दुर्गति",
    "sayaṅkataṃ": "स्वयं का किया हुआ", "sukhadukkha": "सुख और दुःख", "adhicca": "संयोग",
    "samuppannaṃ": "उत्पन्न", "rāgaggi": "राग की अग्नि", "dosaggi": "द्वेष की अग्नि",
    "mohaggi": "मोह की अग्नि", "dosa": "द्वेष", "moha": "मोह", "sallaṃ": "काँटा",
    # cetovinibandha (2-U53)
    "kāme": "इंद्रिय-सुख", "avītarāgo": "राग से मुक्त नहीं", "avigatacchando": "चाह से मुक्त नहीं",
    "avigatapemo": "प्रेम से मुक्त नहीं", "avigatapipāso": "प्यास से मुक्त नहीं",
    "avigatapariḷāho": "ताप से मुक्त नहीं", "avigatataṇho": "तृष्णा से मुक्त नहीं", "kāye": "शरीर",
    "rūpe": "भौतिक रूप", "udarāvadehakaṃ": "पेट भरकर", "bhuñjitvā": "खाकर", "seyyasukhaṃ": "सोने का सुख",
    "passasukhaṃ": "करवटें बदलने का सुख", "middhasukhaṃ": "ऊँघने का सुख", "anuyutto": "लगा रहना",
    "deva": "देव", "nikāyaṃ": "लोक", "paṇidhāya": "कामना करके", "brahmacariyaṃ": "पवित्र जीवन",
    "tapena": "तप", "devo": "देवता",
    # nīvaraṇa, ānantariya, five views, byasana, akkhanti, bhaya
    "kāmacchanda": "इंद्रिय-सुखों की चाह", "chanda": "चाह", "thinamiddha": "आलस्य और तंद्रा",
    "thina": "आलस्य", "middha": "तंद्रा", "uddhaccakukkucca": "बेचैनी और पछतावा", "uddhacca": "बेचैनी",
    "kukkucca": "पछतावा", "arahanto": "अर्हत्", "jīvitā": "जान", "voropitā": "लिया गया",
    "duṭṭhena": "दुष्ट", "cittena": "मन", "lohitaṃ": "रक्त", "uppāditaṃ": "बहाया गया", "saṅgho": "संघ",
    "abhivadanti": "कहना", "paññāpenti": "घोषणा करना", "diṭṭhadhammanibbānaṃ": "इसी जीवन में निर्वाण",
    "roga": "रोग", "bhoga": ["धन-संपत्ति", "धन"], "janassa": "लोग", "appiyo": "अप्रिय",
    "amanāpo": "मन को न भाने वाला", "vera": "वैर", "vajja": "दोष", "sammūḷho": "मोह में पड़ा हुआ",
    "kālaṅkaroti": "मरना", "duggatiṃ": "दुर्गति", "vinipātaṃ": "पतन का लोक", "nirayaṃ": "नरक",
    "upapajjati": "उत्पन्न होना", "ājīvaka": "जीविका", "asiloka": "अपयश", "parisa": "सभा", "sārajja": "झिझक",
    "kasāvo": "कड़वाहट",
    # sixes (2-U60 … 2-U68)
    "amanāpiyesu": "मन को न भाने वाला", "saṃsaggārāmatā": "मेल-जोल में रमना",
    "papañcārāmatā": "मानसिक फैलाव में रमना", "upavicarati": "मन से विचरण करना",
    "domanassa": "उदासी", "upekkhāṭṭhāniyaṃ": "समभाव का कारण बनने वाला",
    "upekkhāṭṭhāniyesu": "समभाव का कारण बनने वाला", "cetasikaṃ asātaṃ": "मानसिक असुहावनापन",
    "gehasitaṃ cetasikaṃ asātaṃ": "सांसारिक मानसिक असुहावनापन", "cetasikaṃ dukkhaṃ": "मानसिक दुःख",
    "asātaṃ dukkhaṃ": "असुहावना दुःखद", "asātaṃ dukkhaṃ vedayitaṃ": "असुहावना दुःखद अनुभव",
    "asātā dukkhā vedanā": "असुहावनी दुःखद अनुभूति", "dukkhaṃ vedayitaṃ": "दुःखद अनुभव",
    "gehasitaṃ cetasikaṃ": "सांसारिक मानसिक", "nāsātaṃ": "न" + G + "असुहावनापन",
    "adukkhamasukhā vedanā": "न दुःखद न सुखद अनुभूति",
})
# ---------------------------------------------------------------- taṇhāvicarita (2-973 … 2-976), the 62 views (2-977)
T.update({
    "micchāsaṅkappo": "ग़लत संकल्प", "kusalānaṃ dhammānaṃ": "हितकर परिघटना", "aṅgaṇaṃ": "दाग़",
    "asasmīti": "मैं शाश्वत हूँ", "sātasmīti": "मैं नश्वर हूँ", "aññathāsmīti": "मैं अलग तरह का हूँ",
    "kañci dhammaṃ anavakāriṃ": "किसी परिघटना को" + G + "अलग किए बिना", "anavakāriṃ": "अलग किए बिना",
    "chandaṃ": "चाह", "paṭilabhati": "पाना", "chandaṃ paṭilabhati": "चाह पाना",
    "mānaṃ paṭilabhati": "अहंकार पाना", "diṭṭhiṃ paṭilabhati": "दृष्टि पाना", "diṭṭhiṃ": "दृष्टि",
    "sati": ["सजगता", "होने पर"], "khattiyo": "क्षत्रिय", "vesso": "वैश्य", "suddo": "शूद्र",
    "gahaṭṭho": "गृहस्थ", "pabbajito": "गृहत्यागी", "manusso": "मनुष्य",
    "parapuggalaṃ": "दूसरा व्यक्ति", "upanidhāya": "तुलना करके", "niccosmi": "मैं नित्य हूँ",
    "dhuvosmi": "स्थिर हूँ", "sassatosmi": "शाश्वत हूँ", "avipariṇāmadhammosmīti": "न बदलने वाला हूँ",
    "vinassissāmi": "विनष्ट हो जाऊँगा",
    "ekaccasassatikā": "आंशिक शाश्वतता", "antānantikā": "सीमित और असीम", "ānantikā": "असीम",
    "amarā": "गोलमोल", "vikkhepikā": "जवाब देना", "samuppannikā": "उत्पत्ति", "soḷasa": "सोलह",
})
T["dhammaṃ"] = ["मन का विषय", "शिक्षा", "परिघटना"]
T["ānudiṭṭhi"] = ["के बारे में दृष्टि", "मानने वाली दृष्टि"]
T["carati"] = ["करना", "जीना"]
T["paññapenti"] = ["घोषणा करना", "बताना"]
T["vādā"] = ["मत", "बोलना"]
T["vatthu"] = ["विषय", "आधार"]
T["pāripūriṃ"] = ["अंगों की परिपूर्णता", "भरपूर"]
T["suta"] = ["सुना-सीखा ज्ञान", "सुना हुआ"]
T["dhammesu"] = ["परिघटना", "शिक्षा", "मन के विषय"]
T["kata"] = ["किया हुआ", "किया गया"]
T["ṭhapanā"] = ["टिकाए रखना", "टिकाना"]
T["saṇṭhapanā"] = ["अच्छी तरह टिकाए रखना", "अच्छी तरह सँवारना"]

# per-segment overrides {bid: {kw (exact spelling): value}}
OVR = {
    "2-17-3-8-0": {"Antavā": "सीमितता", "anantavā": "असीमता"},          # names «सीमितता की दृष्टि …»
    "2-833": {"antavā": "सीमितता", "anantavā": "असीमता"},
    "2-898": {"Antavā": "सीमित", "Anantavā": "असीम"},                    # «आत्मा और लोक सीमित हैं»
    "2-902": {"kakkhaḷatā": "कठोर होना", "kaṭhinatā": "कड़ापन"},          # amudutā amaddavatā kakkhaḷiyaṃ
                                                                          # phārusiyaṃ kakkhaḷatā kaṭhinatā
    "2-943": {"dukkha": "दुःख"},                                          # soka-parideva-dukkha-… «शोक, विलाप, दुःख»
    "2-957": {"doso": "दोष"},                                             # purisadoso «व्यक्ति का … दोष»
    "2-U53": {"carati": "जीना"},                                          # brahmacariyaṃ carati «पवित्र जीवन जीता है»
    "2-U60": {"dhammesu": "मन के विषय"},                                  # manāpiyesu dhammesu «मनभावन मन के विषयों में»
    "2-861": {"paccaya": "आवश्यक वस्तु"},
    "2-923": {"kata": "किया गया"},                                         # pubbekata «पहले किए गए कर्मों»                                 # paccayapaṭisevana «आवश्यक वस्तुओं के उपयोग»
}


def _gapped(v, text):
    """v absent as one string: the Hindi may split it (a number or a word in between, as in
    «मन के तीन मैल»): try «a … b» at each word boundary (pi-1 convention for discontinuous Hindi)."""
    if G in v:
        return None
    w = v.split(" ")
    for i in range(len(w) - 1, 0, -1):          # longest head first: «मन के … मैल», not «मन … के मैल»
        c = " ".join(w[:i]) + G + " ".join(w[i:])
        if present(c, text):
            return c
    return None


def resolver(bid, kw, kws, _hi={}):
    if not _hi:
        _hi.update(read_hindi(CH))
    text = _hi.get(bid, "")
    o = OVR.get(bid, {})
    if kw in o:
        v = o[kw]
        return v if v == NDE or present(v, text) else (_gapped(v, text) or v)
    k = lc(kw)
    if k in T:
        cands = T[k] if isinstance(T[k], list) else [T[k]]
    else:
        cands = [pi2_value(kw, kws, PI2, bid, text)]
    for c in cands:
        if c == NDE or present(c, text):
            return c
    for c in cands:
        g = _gapped(c, text)
        if g:
            GAPPED.append((bid, kw, g))
            return g
    return cands[0]


GAPPED = []


T["āpajjati"] = ["जुट जाना", "रखना"]
T["gatāni"] = NDE                                    # diṭṭhigatāni = «दृष्टियाँ» as one word; diṭṭhi has its own entry
T["kamyatā"] = ["चाह", "इच्छा"]                     # ketukamyatā cittassa «मन की झंडा फहराने की चाह» (pi-1: चाह)
T["āsavo"] = ["मन के मैल", "मैल"]                   # fixed plural term; «मैल» as the member of kāmāsavo …

# presence exceptions (bid, kw) -> reason
_KIYA = "regular participle inflection किया ~ किए that the checker does not model"
ALLOWED = {
    ("2-17-4-58-0", "magga"): "member of kummagga: «मार्ग» only inside the word «कुमार्ग»",
    ("2-834", "magga"): "member of kummagga: «मार्ग» only inside the word «कुमार्ग»",
    ("2-U30", "magga"): "member of kummagga: «मार्ग» only inside the word «कुमार्ग»",
    ("2-923", "kata"): "text «पहले किए गए कर्मों»: " + _KIYA,
    ("2-U48", "Sayaṅkataṃ"): "text «स्वयं के किए हुए»: " + _KIYA,
    ("2-U55", "voropitā"): "text «जान ली गई» (feminine with जान): लिया ~ ली is regular inflection the checker "
                           "does not model",
}

if __name__ == "__main__":
    build_part(CH, resolver)
    verify(CH, show=400, allowed=ALLOWED)
    if "gaps" in sys.argv:
        for g in GAPPED:
            print("   GAP ", *g)
    if "defaults" in sys.argv:                  # keywords resolved by the PI2 / CH2 defaults
        seen = {}
        for bid, kws in read_keywords(CH):
            for kw in kws:
                if lc(kw) not in T and kw not in OVR.get(bid, {}):
                    seen.setdefault(lc(kw), set()).add(resolver(bid, kw, kws))
        for k, v in sorted(seen.items()):
            print("   DEF ", k, "=", " | ".join(sorted(v)))
