"""pi-2 ch. 4 (Saccavibhaṅga) Pāli->Hindi keyword map.  usage: python -I -X utf8 map_4-saccavibhango_hi.py

Imports map_sample_hi (read-only). Table T extends PI2; OVR holds per-segment exceptions.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI2, PP_SEGMENTS, NDE, pi2_value, build_part, verify, read_hindi  # noqa: E402

CH = "4-saccavibhango"
PP_SEGMENTS.update({"2-217", "2-218"})

T = {
    # truths
    "sacca": "सत्य", "saccaṃ": "सत्य", "saccāni": "सत्य", "saccā": "सत्य", "saccānaṃ": "सत्य",
    "ariya": "आर्य", "ariyā": "आर्य", "ariyasaccaṃ": "आर्य सत्य", "ariyasaccāni": "आर्य सत्य",
    "ariyasaccānaṃ": "आर्य सत्य",
    "dukkhaṃ": "दुःख", "dukkhassa": "दुःख", "dukkhasaccaṃ": "दुःख का सत्य",
    "dukkhaṃ ariyasaccaṃ": "दुःख आर्य सत्य",
    "samudaya": "उत्पत्ति", "samudayaṃ": "उत्पत्ति", "samudayo": "उत्पत्ति", "samudaye": "उत्पत्ति",
    "dukkhasamudayaṃ": "दुःख की उत्पत्ति", "dukkhasamudayo": "दुःख की उत्पत्ति",
    "dukkhasamudaye": "दुःख की उत्पत्ति",
    "dukkhanirodhaṃ": "दुःख का अंत", "dukkhanirodho": "दुःख का अंत", "dukkhanirodha": "दुःख का अंत",
    # dukkha definitions (2-190 … 2-202)
    "jātipi": "जन्म भी", "jarāpi": "बुढ़ापा भी", "maraṇampi": "मृत्यु भी", "upāyāsāpi": "निराशा भी",
    "sokaparidevadukkhadomanassupāyāsāpi": "शोक विलाप दुःख उदासी और निराशा भी",
    "sokaparidevadukkhadomanassupāyāsā": "शोक विलाप दुःख उदासी और निराशा",
    "soka": "शोक", "parideva": "विलाप", "upāyāsā": "निराशा",
    "appiyehi": "अप्रिय", "piyehi": "प्रिय", "vippayogo": "वियोग", "labhati": "मिलना", "picchaṃ": "चाहना",
    "saṃkhittena": "संक्षेप में", "upādāna": "आसक्ति", "dukkho": "दुःख",
    "sattānaṃ": "प्राणी", "nikāye": "प्राणी-वर्ग", "nikāyā": "प्राणी-वर्ग",
    "jāti": "जन्म", "sañjāti": "भली-भाँति जन्म", "okkanti": "गर्भ में उतरना",
    "abhinibbatti": "पूरी तरह पैदा होना", "pātubhāvo": "प्रकट होना", "paṭilābho": "प्राप्ति",
    "āyatanānaṃ": "इंद्रिय-क्षेत्र",
    "jarā": "बुढ़ापा", "jīraṇatā": "जीर्ण होना", "khaṇḍiccaṃ": "दाँतों का टूटना", "pāliccaṃ": "बालों का पकना",
    "vali": "झुर्री", "taca": "त्वचा", "āyuno": "आयु", "indriyānaṃ": "इंद्रिय", "paripāko": "पूरी तरह पक जाना",
    "cuti": "गुज़र जाना", "cavanatā": "गुज़र जाने की अवस्था", "bhedo": "टूटना",
    "antaradhānaṃ": "लुप्त हो जाना", "maccu": "मौत", "maraṇaṃ": "मृत्यु", "maraṇa": "मृत्यु",
    "kālakiriyā": "काल का पूरा होना", "kaḷevarassa": "शरीर", "nikkhepo": "त्याग",
    "jīvitindriyassupacchedo": "जीवन-क्षमता का कट जाना", "jīvitindriya": "जीवन-क्षमता",
    "upacchedo": "कट जाना",
    "ñāti": "संबंधी", "bhoga": "धन-संपत्ति", "roga": "रोग", "sīla": "सदाचार", "byasanena": "हानि",
    "phuṭṭhassa": "पीड़ित", "byasanena vā phuṭṭhassa": "हानि से पीड़ित", "samannāgatassa": "घिरा",
    "dhammena": "परिघटना",
    "soko": "शोक", "socanā": "शोक करना", "anto": "भीतर", "antoparisoko": "भीतर का गहरा शोक",
    "parijjhāyanā": "जलना", "domanassaṃ": "उदासी", "sallaṃ": "काँटा",
    "ādevo": "रोना", "paridevo": "विलाप", "ādevanā": "रोते रहना", "vācā": "शब्दों की झड़ी",
    "palāpo": "प्रलाप", "vippalāpo": "बड़बड़ाना", "lālappo": "बिलखना",
    "kāyikaṃ": "शारीरिक", "kāyasamphassajaṃ": "शरीर के संपर्क से उत्पन्न", "dukkhaṃ vedayitaṃ": "दुःखद अनुभव",
    "cetasikaṃ asātaṃ": "मानसिक असुहावनापन", "cetasikaṃ dukkhaṃ": "मानसिक दुःख",
    "cetosamphassa": "मन का संपर्क",
    "āyāso": "हताशा", "upāyāso": "निराशा",
    "yassa": "जिसके लिए", "aniṭṭhā": "अनचाहा", "akantā": "अप्रिय", "amanāpā": "मन को न भाने वाला",
    "iṭṭhā": "मनचाहा", "kantā": "प्रिय", "manāpā": "मनभावन",
    "rūpā": "दृश्य रूप", "saddā": "ध्वनि", "gandhā": "गंध", "rasā": "स्वाद", "phoṭṭhabbā": "स्पर्श",
    "ye vā panassa": "या जो लोग उसका", "kāmā": "चाहने वाला", "anattha": "अनर्थ", "ahita": "अहित",
    "aphāsuka": "असुविधा", "ayogakkhemakāmā": "कुशल-क्षेम न चाहने वाला", "phāsuka": "सुविधा",
    "yogakkhema": "कुशल-क्षेम",
    "samāgamo": "एक साथ आना", "samodhānaṃ": "साथ रहना", "missībhāvo": "घुल-मिल जाना",
    "asamāgamo": "एक साथ न आना", "asamodhānaṃ": "साथ न रहना", "amissībhāvo": "घुल-मिल न पाना",
    "mātā": "माता", "pitā": "पिता", "bhātā": "भाई", "bhaginī": "बहन", "mittā": "मित्र", "amaccā": "साथी",
    "ñātī": "संबंधी", "sālohitā": "रक्त-संबंधी",
    "byādhi": "रोग", "icchā": "इच्छा", "icchāya": "इच्छा करना", "pattabbaṃ": "मिल सकना",
    "uppajjati": "उत्पन्न होना",
    "seyyathidaṃ": "यानी", "rūpupādānakkhandho": "आसक्ति का विषय बनने वाला भौतिक रूप का समूह",
    "vedanupādānakkhandho": "आसक्ति का विषय बनने वाला अनुभूति का समूह",
    "saññupādānakkhandho": "आसक्ति का विषय बनने वाला पहचान का समूह",
    "saṅkhārupādānakkhandho": "आसक्ति का विषय बनने वाला मानसिक रचनाओं का समूह",
    "viññāṇupādānakkhandho": "आसक्ति का विषय बनने वाला चेतना का समूह",
    # samudaya / nirodha (2-203, 2-204)
    "taṇhā": "तृष्णा", "taṇhāya": "तृष्णा", "ponobhavikā": "बार-बार पुनर्जन्म दिलाने वाला", "nandi": "आनंद",
    "rāga": "राग", "ābhinandinī": "आनंद लेने वाला", "kāma": "इंद्रिय-सुख",
    "kāmataṇhā": "इंद्रिय-सुखों की तृष्णा", "bhava": "अस्तित्व", "bhavataṇhā": "अस्तित्व की तृष्णा",
    "vibhava": "अनस्तित्व", "vibhavataṇhā": "अनस्तित्व की तृष्णा",
    "taṇhā uppajjamānā uppajjati": "तृष्णा उत्पन्न होते समय … उत्पन्न होना", "nivisati": "टिकना",
    "piyarūpaṃ": "प्रिय लगने वाला", "sātarūpaṃ": "सुहावना लगने वाला", "rūpaṃ": "भौतिक रूप",
    "cakkhuṃ": "आँख", "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhā": "जीभ", "kāyo": "शरीर", "mano": "मन",
    "cakkhuviññāṇaṃ": "आँख की चेतना", "manoviññāṇaṃ": "मन की चेतना",
    "cakkhusamphasso": "आँख का संपर्क", "sotasamphasso": "कान का संपर्क", "ghānasamphasso": "नाक का संपर्क",
    "jivhāsamphasso": "जीभ का संपर्क", "kāyasamphasso": "शरीर का संपर्क", "manosamphasso": "मन का संपर्क",
    "cakkhusamphassajā vedanā": "आँख के संपर्क से उत्पन्न अनुभूति", "sañcetanā": "इरादा",
    "phoṭṭhabbataṇhā": "स्पर्श की तृष्णा", "yaṃ": "जो",
    "pahīyati": "छूटना", "taṇhā pahīyamānā pahīyati": "तृष्णा छूटते समय … छूटना", "nirujjhati": "समाप्त होना",
    "asesa": "पूरी तरह", "virāga": "फीका पड़ना", "cāgo": "त्याग", "paṭinissaggo": "छोड़ देना", "mutti": "मुक्ति",
    "anālayo": "लगाव का न रहना",
    # magga (2-205)
    "aṭṭhaṅgiko": "आठ अंगों वाला", "aṭṭhaṅgiko maggo": "आठ अंगों वाला मार्ग", "maggo": "मार्ग",
    "sammā": "सही", "diṭṭhi": "दृष्टि", "saṅkappo": "संकल्प", "ājīvo": "आजीविका", "vāyāmo": "प्रयास",
    "ñāṇaṃ": "ज्ञान", "nekkhamma": "त्याग", "abyāpāda": "दुर्भावना का अभाव", "avihiṃsā": "अहिंसा",
    "musā": "झूठ", "musāvādā": "झूठ बोलना", "veramaṇī": "दूर रहना", "pisuṇāya": "चुगली", "pharusāya": "कठोर",
    "samphappalāpā": "व्यर्थ की बकवास", "pāṇātipātā": "जीव-हत्या", "ātipātā": "हत्या", "ādānā": "लेना",
    "micchācārā": "दुराचार", "kāmesu": "इंद्रिय-सुख", "sāvako": "शिष्य", "micchā": "ग़लत", "pahāya": "छोड़कर",
    "kappeti": "जीवन-यापन करना", "bhikkhu": "भिक्षु", "chandaṃ": "चाह", "janeti": "जगाना",
    "chandaṃ janeti": "चाह जगाना", "vāyamati": "प्रयास करना", "ārabhati": "जगाना", "paggaṇhāti": "तत्पर करना",
    "padahati": "पूरा ज़ोर लगाना", "uppannānaṃ": "उत्पन्न", "pāpakānaṃ": "बुरा", "akusalānaṃ": "हानिकर",
    "akusalānaṃ dhammānaṃ": "हानिकर परिघटना", "kusalānaṃ": "हितकर", "kusalānaṃ dhammānaṃ": "हितकर परिघटना",
    "anuppādāya": "उत्पन्न न होने देना", "pahānāya": "छोड़ना", "uppādāya": "उत्पत्ति", "ṭhitiyā": "स्थिरता",
    "asammosāya": "लुप्त न होना", "vepullāya": "विपुलता", "pāripūriyā": "परिपूर्णता",
    "kāye": "शरीर", "kāye kāyānupassī": "शरीर में शरीर का अवलोकन करते हुए",
    "kāyānupassī viharati": "शरीर का अवलोकन करते हुए रहना", "ānupassī": "अवलोकन करते हुए", "viharati": "रहना",
    "ātāpī": "उद्यमी", "sampajāno": "स्पष्ट समझ रखते हुए", "satimā": "सजग", "vineyya": "दूर करके",
    "abhijjhā": "लालच", "vedanāsu": "अनुभूति", "dhammesu": "मन के विषय",
    "kāmehi": "इंद्रिय-सुख", "vivicca": "अलग होकर", "vivicceva": "अलग होकर",
    "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर", "savitakkaṃ savicāraṃ": "आरंभिक विचार और सतत विचार वाला",
    "vivekajaṃ": "अलगाव से उत्पन्न", "viveka": "अलगाव", "pītisukhaṃ": "उल्लास और सुख", "jhānaṃ": "ध्यान",
    "upasampajja": "प्राप्त करके", "upasampajja viharati": "प्राप्त करके उसमें रहना",
    "vitakkavicārānaṃ vūpasamā": "आरंभिक विचार और सतत विचार का शांत होना", "vūpasamā": "शांत होना",
    "sampasādanaṃ": "निर्मलता", "ekodibhāvaṃ": "एक बिंदु पर टिकना", "virāgā": "फीका पड़ना",
    "upekkhako": "समभाव वाला", "sukhañca": "सुख", "paṭisaṃvedeti": "अनुभव करना", "ācikkhanti": "कहना",
    "sukhavihārī": "सुख से रहने वाला", "sukhassa": "सुख", "atthaṅgamā": "मिट जाना",
    "pārisuddhiṃ": "पूरी तरह शुद्ध", "catutthaṃ jhānaṃ": "चौथा ध्यान", "vitakkaṃ": "आरंभिक विचार",
    "vicāraṃ": "सतत विचार",
    # Abhidhammabhājanīya (2-206 … 2-214)
    "avasesā": "शेष", "avasesā ca kilesā": "शेष मन के क्लेश", "avasesā ca akusalā": "शेष हानिकर",
    "avasesā dhammā": "शेष परिघटना", "kilesā": "मन के क्लेश", "mūlāni": "मूल", "kusalamūlāni": "हितकर मूल",
    "sāsavāni": "मन के मैलों का विषय बनने वाला",
    "mūlāni sāsavāni": "मन के मैलों का विषय बनने वाला … मूल",
    "kusalamūlāni sāsavāni": "मन के मैलों का विषय बनने वाला … हितकर मूल",
    "sāsavā kusalā dhammā": "मन के मैलों का विषय बनने वाली … हितकर परिघटना",
    "kusalā dhammā": "हितकर परिघटना", "akusalā dhammā": "हानिकर परिघटना",
    "kusalākusalānaṃ": "हितकर और हानिकर", "dhammānaṃ": "परिघटना", "dhammā": "परिघटना",
    "kusalākusalānaṃ dhammānaṃ vipākā": "हितकर और हानिकर कर्म के फल रूपी परिघटना",
    "sāsavā kusalākusalānaṃ dhammānaṃ": "मन के मैलों का विषय बनने वाली हितकर और हानिकर … परिघटना",
    "kammavipākā": "कर्म-फल", "kiriyā": "केवल क्रिया रूपी", "neva kusalā nākusalā": "न हितकर न हानिकर",
    "pahānaṃ": "छोड़ देना", "taṇhāya pahānaṃ": "तृष्णा को छोड़ देना",
    "samaye": "उस समय", "uttaraṃ": "लोकोत्तर", "bhāveti": "अभ्यास करना", "jhānaṃ bhāveti": "ध्यान का अभ्यास करना",
    "apacayagāmiṃ": "संचय घटाने की ओर ले जाने वाला", "diṭṭhigatānaṃ": "दृष्टियों में फँसना",
    "diṭṭhigatānaṃ pahānāya": "दृष्टियों में फँसने को छोड़ना", "pattiyā": "प्राप्ति", "bhūmiyā": "चरण",
    "dukkhapaṭipadaṃ": "दुःखद प्रगति", "ābhiññaṃ": "उच्च ज्ञान", "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "दुःखद प्रगति और धीमे उच्च ज्ञान वाला",
    "paññā": "प्रज्ञा", "pajānanā": "जानना", "vicayo": "छानबीन", "dhammavicayo": "परिघटनाओं की छानबीन",
    "sambojjhaṅgo": "जागृति का अंग",
    "dhammavicayasambojjhaṅgo": "परिघटनाओं की छानबीन नामक जागृति का अंग",
    "vīriyasambojjhaṅgo": "उत्साह नामक जागृति का अंग", "satisambojjhaṅgo": "सजगता नामक जागृति का अंग",
    "samādhisambojjhaṅgo": "एकाग्रता नामक जागृति का अंग", "maggaṅgaṃ": "मार्ग का अंग",
    "ārambho": "जगाना", "ārati": "दूर रहना", "virati": "विरत रहना", "paṭivirati": "पूरी तरह विरत रहना",
    "akiriyā": "न करना", "akaraṇaṃ": "न अपनाना", "anajjhāpatti": "दोष में न पड़ना", "velā": "मर्यादा",
    "anatikkamo": "उल्लंघन न करना", "setu": "पुल", "ghāto": "तोड़ देना", "vacī": "वाणी", "kāya": "शरीर",
    "duccaritehi": "दुराचरण", "vacīduccaritehi": "वाणी … दुराचरण", "kāyaduccaritehi": "शरीर … दुराचरण",  # «वाणी के चार दुराचरणों»
    "pañcaṅgiko maggo": "पाँच अंगों वाला मार्ग",
    # Pañhāpucchaka (neuter / plural forms of the PI2 labels)
    "pahātabbā": "छोड़ा जाने वाला", "hetukā": "मूलों वाला", "sahetukā": "मूल वाला",
    "saṃkilesikā": "क्लेशों का विषय बनने वाला", "vattabbaṃ": "कहा जा सकना", "ādhipati": "प्रधानता वाला",
    "vicāra": "सतत विचार", "mahaggataṃ": "उन्नत", "mahaggatārammaṇaṃ": "उन्नत विषय वाला",
    "bahiddhārammaṇaṃ": "दूसरों से संबंधित विषय वाला", "niyataṃ": "निश्चित", "hīnaṃ": "हीन",
    "ajjhattārammaṇaṃ": "स्वयं से संबंधित विषय वाला",
    "ajjhattabahiddhārammaṇaṃ": "स्वयं और दूसरों दोनों से संबंधित विषय वाला",
    "anidassanaappaṭighā": "दिखाई न देने वाला और टकराव से रहित", "appaṭighā": "टकराव से रहित",
    "gāmi": "की ओर ले जाने वाला", "parittārammaṇaṃ": "सीमित विषय वाला", "appamāṇārammaṇaṃ": "अपरिमित विषय वाला",
    "majjhimaṃ": "मध्यम", "ārammaṇaṃ": "विषय वाला", "paṇītā": "उत्तम",
    "savitakkasavicāraṃ": "आरंभिक विचार और सतत विचार वाला", "sekkhaṃ": "सीखने के चरण का",
    "upādānañceva upādānasampayuttañca": "आसक्ति रूपी भी और आसक्ति से जुड़ा भी",
    "kileso ceva kilesasampayuttañca": "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी",
    "saṃyojanañceva saṃyojanasampayuttañca": "बंधन रूपी भी और बंधनों से जुड़ा भी",
    "nīvaraṇañceva nīvaraṇasampayuttañca": "बाधा रूपी भी और बाधाओं से जुड़ा भी",
    "āsavo ceva āsavasampayuttañca": "मन के मैल रूपी भी और मन के मैलों से जुड़ा भी",
    "gantho ceva ganthasampayuttañca": "गाँठ रूपी भी और गाँठों से जुड़ा भी",
    "hetu ceva hetusampayuttañca": "मूल रूपी भी और मूलों से जुड़ा भी",
    "kileso": "मन के क्लेश", "saṃkiliṭṭhaṃ": "क्लेशों से मलिन", "asaṃkiliṭṭhā": "क्लेशों से मलिन न होने वाला",
    "saraṇaṃ": "संघर्ष वाला", "sahabhū": "साथ-साथ होने वाला", "pītisahagatā": "उल्लास के साथ होने वाला",
    "arūpāni": "अभौतिक", "vippayuttā": "अलग", "āsekkhā": "सीखना पूरा होने के चरण का",
    "sukhāya vedanāya sampayuttā": "सुखद अनुभूति से जुड़ा", "niyyānikaṃ": "मुक्ति की ओर ले जाने वाला",
    "ārammaṇā": "विषय वाला", "asaṅkhataṃ": "अनिर्मित", "sanidassanaṃ": "दिखाई देने वाला",
    "lokiyā": "लौकिक", "ogho": "बाढ़", "yogo": "जकड़न", "saṃyojanā": "बंधन",
    "saccā araṇā": "सत्य संघर्ष से रहित", "saccāni appaṭighā": "सत्य टकराव से रहित",
    "parāmaṭṭhā": "ग़लत धारणा का विषय बनने वाला",
}
TABLE = {**PI2, **T}

OVR = {
    "2-4-1-1-0": {"Dukkha": "दुःख"},                       # Dukkhasaccaṃ «दुःख का सत्य»
    "2-190": {"dukkha": "दुःख"},                           # member of sokaparidevadukkha… «शोक, विलाप, दुःख …»
    "2-201": {"dukkha": "दुःख", "Na": "नहीं"},             # «… दुःख …»; «इच्छा करने से नहीं मिल सकता»
    "2-202": {"dukkhā": "दुःख रूपी"},                      # «संक्षेप में दुःख रूपी, आसक्ति का विषय बनने वाले …»
    "2-203": {"dukkha": "दुःख", "sahagatā": "से युक्त", "dhammā": "मन के विषय", "rūpaṃ": "चीज़"},
    "2-204": {"dukkha": "दुःख", "dhammā": "मन के विषय", "rūpaṃ": "चीज़"},  # piya-/sātarūpaṃ «… लगने वाली चीज़»
    "2-205": {"dukkha": "दुःख", "vācā": "वाणी", "bhāvanāya": "अभ्यास", "samādhi": "एकाग्रता",
              "aṭṭhaṅgiko maggo": "आठ अंगों वाला … मार्ग"},   # «आठ अंगों वाला आर्य मार्ग»
    "2-206": {"veramaṇī": "बचना", "vācā": "वाणी"},        # the virati string (pi-1: veramaṇī = बचना)
    "2-217": {"Dukkha": "दुःख", "uppannā": "उत्पन्न हो चुका",  # Dukkhasaccaṃ; matrix label (siyā uppannā)
              "dhammā": NDE},                           # fragment of vipākadhammadhammā: «… करने वाले», no noun
    "2-218": {"Dukkha": "दुःख", "ajjhattaṃ": "स्वयं से संबंधित", "cetasikaṃ": "मन का सहचर",
              "rūpaṃ": "भौतिक"},                        # «कभी भौतिक होता है, कभी अभौतिक»
}
ALLOWED = {("2-218", "apariyāpannā"): "text «न समाए हुए»: समाया ~ समाए is regular inflection the checker does not model (sample precedent)"}
_HI = {}


def resolver(bid, kw, kws):
    if not _HI:
        _HI.update(read_hindi(CH))
    o = OVR.get(bid, {})
    if kw in o:
        return o[kw]
    return pi2_value(kw, kws, TABLE, bid, _HI.get(bid))


if __name__ == "__main__":
    build_part(CH, resolver)
    verify(CH, allowed=ALLOWED)
