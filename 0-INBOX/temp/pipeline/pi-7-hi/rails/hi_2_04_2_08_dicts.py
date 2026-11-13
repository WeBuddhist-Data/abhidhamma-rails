"""Phrase tables for build_rails_2-04_2-08.py (pi-7 Hindi plain RAILS, files 2-04 .. 2-08).

Keys are lower-case Pāli with the triad items replaced by § (primary triad) and ¤ (secondary triad: in 2-07 the
-ārammaṇa items, in 2-08 the plain paritta items); a compound member is joined with '+' (§+adhipati).
Hindi templates use ‹nX›: item n of the key, X = f (feminine), m (masculine direct sg), o (masculine oblique / pl),
E (oblique with «एक»), D (direct with «एक»).
"""
import build_rails_sample as S

RUPA_CITTA, RUPA_KATATTA, RUPA_UPADA = S.RUPA_CITTA, S.RUPA_KATATTA, S.RUPA_UPADA

# ---------------------------------------------------------------- headings
HEAD_X = {
    "Dassanenapahātabbahetukattikaṃ": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला तीन का वर्गीकरण",
    "Ācayagāmittikaṃ": "संचय की ओर ले जाने वाला तीन का वर्गीकरण",
    "Sekkhattikaṃ": "सीखने के चरण वाला तीन का वर्गीकरण",
    "Parittattikaṃ": "सीमित वाला तीन का वर्गीकरण",
    "Parittārammaṇattikaṃ": "सीमित विषय वाला तीन का वर्गीकरण",
    "Sahajātavāro": "सह-उत्पत्ति का खंड",
    "Paccayavāro": "कारण का खंड",
    "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड",
    "Sampayuttavāro": "जुड़ाव का खंड",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro": "सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
}

NUM_X = {
    "dasa": "दस", "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह", "cuddasa": "चौदह", "pannarasa": "पंद्रह",
    "soḷasa": "सोलह", "sattarasa": "सत्रह", "sattārasa": "सत्रह", "aṭṭhārasa": "अठारह", "ekūnavīsati": "उन्नीस",
    "vīsati": "बीस", "ekavīsa": "इक्कीस", "ekavīsati": "इक्कीस", "dvāvīsa": "बाईस", "bāvīsa": "बाईस", "tevīsa": "तेईस",
    "ekā": "एक",
    "eka": "एक",  # «avigate eka» (2-07): spelling slip for ekaṃ, rendered as meant
}

# Pāli bracket -> (Hindi bracket, Hindi anchor after which it goes)
VARIANTS_X = {
    "{nevasekhānāsekho (sī.), nevasekkhānāsekkho (syā. ka.)}":
        ("[वर्तनी-भेद (Sī.): nevasekhānāsekho; (Syā., Ka.): nevasekkhānāsekkho]",
         "न सीखने के चरण की, न सीखना पूरा होने के चरण की"),
    "{ācayagāmi (sī. syā.) evamuparipi}":
        ("[वर्तनी-भेद (Sī., Syā.): ācayagāmi evamuparipi]", "संचय की ओर ले जाने वाली"),
    "{paṭhamassa jhānassa (?)}": ("[पाठभेद: paṭhamassa jhānassa (?)]", "उसी के लिए"),
    "{nevasaññānāsaññāyatanassa (?) aññesu tikesu oloketabbaṃ}":
        ("[पाठभेद: nevasaññānāsaññāyatanassa (?) aññesu tikesu oloketabbaṃ]", "उसी के लिए"),
}

# Pāli -> (replacement, note for the report); applied before normalisation
SLIPS_X = {
    "gaṇatabbaṃ": ("gaṇetabbaṃ", "gaṇatabbaṃ for gaṇetabbaṃ (spelling, rendered as meant)"),
    "maggapaccaya ": ("maggapaccayā ", "maggapaccaya for maggapaccayā (spelling, rendered as meant)"),
    "maggapaccaya,": ("maggapaccayā,", "maggapaccaya for maggapaccayā (spelling, rendered as meant)"),
    "maggapaccaya…": ("maggapaccayā…", "maggapaccaya for maggapaccayā (spelling, rendered as meant)"),
    "aññamaññapaccaya ": ("aññamaññapaccayā ", "aññamaññapaccaya for -paccayā (spelling, rendered as meant)"),
    "aññamaññapaccaya…": ("aññamaññapaccayā…", "aññamaññapaccaya for -paccayā (spelling, rendered as meant)"),
}

LINE_X = {}

# ---------------------------------------------------------------- editorial notes (inside the parentheses)
_DASS = "सत्य-दर्शन से छोड़े जाने वाले मूलों वाले पद"
_DTIKA = "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं वाले तीन के वर्गीकरण"
_KTIKA = "हितकर वाले तीन के वर्गीकरण"
NOTE_X = {
    "evaṃ gaṇetabbaṃ": "इसी तरह गिनना चाहिए",
    "saṃkhittaṃ": "संक्षिप्त",
    "paṭisandhi natthi": "पुनर्जन्म नहीं है",
    "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान",
    "paṭiccavārasadisā": "निर्भरता के खंड के समान",
    "paṭiccavārasadisā kātabbā": "निर्भरता के खंड के समान करने चाहिए",
    "paṭiccavārasadisā dvādasa pañhā": "निर्भरता के खंड के समान बारह प्रश्न",
    "paripuṇṇaṃ": "परिपूर्ण",
    "paripuṇṇaṃ kātabbaṃ": "परिपूर्ण करना चाहिए",
    "paṭisandhikkhaṇe natthi": "पुनर्जन्म के क्षण में नहीं है",
    "anantarasadisaṃ": "निकटता-कारण के समान",
    "anantarasadisā": "निकटता-कारण के समान",
    "ārammaṇasadisaṃ": "विषय-कारण के समान",
    "sahajātasadisaṃ": "सह-उत्पत्ति-कारण के समान",
    "hetusadisā": "मूल-कारण के समान",
    "hetusadisaṃ kātabbaṃ": "मूल-कारण के समान करना चाहिए",
    "adhipatiyā moho natthi": "प्रधानता-कारण में मोह नहीं है",
    "āhārasadisaṃ": "आहार-कारण के समान",
    "moho kātabbo": "मोह शामिल करना चाहिए",
    "dassanattikasadisaṃ": f"{_DTIKA} के समान",
    "yathā dassanattikaṃ": f"जैसे {_DTIKA} में",
    "vitthāretabbaṃ": "विस्तार करना चाहिए",
    "vitthāretabbaṃ dassanattikasadisaṃ": f"{_DTIKA} के समान विस्तार करना चाहिए",
    "dassanena sadisaṃ": f"{_DASS} के समान",
    "dassanena sadisā": f"{_DASS} के समान",
    "dassanena sadisaṃ gamanaṃ": f"{_DASS} के समान प्रसंग",
    "dassanena sadisaṃ vibhajitabbaṃ": f"{_DASS} के समान विश्लेषण करना चाहिए",
    "dasa pañhā": "दस प्रश्न",
    "aṭṭha pañhā": "आठ प्रश्न",
    "nava pañhā": "नौ प्रश्न",
    "terasa pañhā": "तेरह प्रश्न",
    "satta pañhā": "सात प्रश्न",
    "tisso pañhā": "तीन प्रश्न",
    "dve kātabbā": "दो करने चाहिए",
    "dve kātabbā dassitanayena": "दिखाई गई विधि से दो करने चाहिए",
    "dve pañhā kātabbā": "दो प्रश्न करने चाहिए",
    "tisso pañhā kātabbā": "तीन प्रश्न करने चाहिए",
    "imepi dve kātabbā": "ये दो भी करने चाहिए",
    "ime sahetukā kātabbā": "इन्हें मूल वाला करना चाहिए",
    "mahābhūtā kātabbā": "महाभूत शामिल करने चाहिए",
    "sabbe mahābhūtā kātabbā": "सभी महाभूत शामिल करने चाहिए",
    "sabbepi mahābhūtā kātabbā": "सभी महाभूत भी शामिल करने चाहिए",
    "ekā pañhā sabbe mahābhūtā kātabbā": "एक प्रश्न, सभी महाभूत शामिल करने चाहिए",
    "sabbe mahābhūtā vitthāretabbā": "सभी महाभूतों का विस्तार करना चाहिए",
    "arūpe §+mūlake tisso pañhā": "अभौतिक लोक में ‹0o› पद से शुरू होने वाली शृंखला में तीन प्रश्न",
    "nissayavāro paccayavārasadiso": "आश्रय का खंड कारण के खंड के समान है",
    "sahajātavāro paṭiccavārasadiso": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है",
    "sahajātavāropi paṭiccavārasadiso": "सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान है",
    "sampayuttavāro saṃsaṭṭhavārasadiso": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है",
    "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso":
        "सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी निर्भरता के "
        "खंड के समान हैं",
    "§+mūlake tīṇi": "‹0o› पद से शुरू होने वाली शृंखला में तीन",
    "§+ghaṭanesu tīṇi": "‹0o› पद के संयोजनों में तीन",
    "§+nayena kātabbaṃ": "‹0o› पद की विधि से करना चाहिए",
    "§+sadisaṃ": "‹0o› पद के समान",
    "§+sadisā": "‹0o› पद के समान",
    "§ paṭisandhi natthi": "‹0o› पद में पुनर्जन्म नहीं है",
    "§ ca": "‹0m› भी",
    "tīṇi": "तीन",
    "satta": "सात",
    "nava": "नौ",
    "pañca": "पाँच",
    "ekādasa": "ग्यारह",
    "ekaṃ": "एक",
    "ghaṭanā paripuṇṇā": "संयोजन परिपूर्ण",
    "dvepi kātabbā": "दोनों करने चाहिए",
    "kusalattikasadisā": f"{_KTIKA} के समान",
    "kusalattikasadisā satta pañhā": f"{_KTIKA} के समान सात प्रश्न",
    "cakkaṃ kātabbaṃ": "चक्र बनाना चाहिए",
    "kusalattikasadisaṃ": f"{_KTIKA} के समान",
    "cakkaṃ kātabbaṃ kusalattikasadisaṃ": f"चक्र बनाना चाहिए, {_KTIKA} के समान",
    "cittasamuṭṭhānampi kaṭattārūpampi upādārūpampi natthi":
        f"{RUPA_CITTA}, {RUPA_KATATTA} और {RUPA_UPADA} भी नहीं हैं",
    "avasesā cha pañhā hetupaccayasadisā satta kātabbā":
        "शेष छह प्रश्न मूल-कारण के समान हैं, सात करने चाहिए",
    "paṭisandhi natthi, sattarasa pañhā paripuṇṇā": "पुनर्जन्म नहीं है, सत्रह प्रश्न परिपूर्ण",
    "sattarasa pañhā paripuṇṇā": "सत्रह प्रश्न परिपूर्ण",
    "paṭisandhikkhaṇe tīṇipi kātabbā": "पुनर्जन्म के क्षण में तीनों करने चाहिए",
    "paṭisandhivipākopi natthi": "पुनर्जन्म का कर्म-फल भी नहीं है",
    "vipākopi paṭisandhipi natthi": "कर्म-फल भी नहीं है, पुनर्जन्म भी नहीं है",
    "paṭisandhipi mahābhūtāpi sabbe": "पुनर्जन्म भी, सभी महाभूत भी",
    "vipākoti niddisitabbaṃ cittasamuṭṭhānaṃ rūpaṃ vipākoti na kātabbaṃ":
        f"“कर्म-फल” निर्देश करना चाहिए, {RUPA_CITTA} को “कर्म-फल” नहीं बनाना चाहिए",
    "pavattimeva": "केवल जीवन-काल में",
    "pavattipaṭisandhi": "जीवन-काल और पुनर्जन्म",
    "pavattipaṭisandhi kātabbā": "जीवन-काल और पुनर्जन्म शामिल करने चाहिए",
    "paṭiccavārapaccanīye navippayuttasadisaṃ": "निर्भरता के खंड के नकारात्मक क्रम में अलगाव-कारण के अभाव के समान",
    "ninnānaṃ": "बिना किसी अंतर के",
    "paṭiccavāre aññamaññasadisaṃ": "निर्भरता के खंड में परस्पर-कारण के समान",
    "nissayapaccaye kusalattike nissayapaccayasadisaṃ":
        f"आश्रय-कारण में, {_KTIKA} में आश्रय-कारण के समान",
    "paṭiccavāre paccanīyasadisaṃ": "निर्भरता के खंड में नकारात्मक क्रम के समान",
    "paṭiccavāre sahajātasadisaṃ": "निर्भरता के खंड में सह-उत्पत्ति-कारण के समान",
    "paṭiccavāre sampayuttavārasadisaṃ": "निर्भरता के खंड में जुड़ाव के खंड के समान",
    "paṭiccavāre ārammaṇasadisā": "निर्भरता के खंड में विषय-कारण के समान",
    "paccayavāre nissayavārasadisaṃ": "कारण के खंड में आश्रय के खंड के समान",
    "visuṃ ghaṭanā natthi": "अलग से संयोजन नहीं हैं",
    "sahajātapaccaye paṭiccavāre sahajātavārasadisā nava pañhā":
        "सह-उत्पत्ति-कारण में, निर्भरता के खंड में सह-उत्पत्ति के खंड के समान नौ प्रश्न",
    "aññamaññapaccaye paṭiccavāre aññamaññasadisaṃ tīṇi":
        "परस्पर-कारण में, निर्भरता के खंड में परस्पर-कारण के समान तीन",
    "nissayapaccaye paccayavāre nissayavārasadisaṃ": "आश्रय-कारण में, कारण के खंड में आश्रय के खंड के समान",
    "cattāripi hi visuṃ ghaṭanā natthi": "चारों के भी अलग से संयोजन नहीं हैं",
    "saṃkhittaṃ, sabbe ghaṭanā kātabbā": "संक्षिप्त, सभी संयोजन करने चाहिए",
    "dassanena nayena vibhajitabbā": f"{_DASS} की विधि से विश्लेषण करना चाहिए",
    '"uddhacca"nti niyāmetabbaṃ': "“बेचैनी” निश्चित करना चाहिए",
    "napacchājātapaccayañca naāsevanapaccayañca naadhipatisadisaṃ":
        "पश्चात्-उत्पत्ति-कारण का अभाव और पुनरावृत्ति-कारण का अभाव प्रधानता-कारण के अभाव के समान हैं",
    "naārammaṇapaccayasadisaṃ": "विषय-कारण के अभाव के समान",
    "samanantarapaccayaṃ anantarapaccayasadisaṃ": "पूर्ण निकटता-कारण निकटता-कारण के समान है",
    "idhāpi ghaṭanā hetusadisā": "यहाँ भी संयोजन मूल-कारण के समान हैं",
    "idha sahajātaṃ, purejātaṃ, missagataṃ atthi, pāḷiyaṃ kātabbaṃ":
        "यहाँ सह-उत्पत्ति, पूर्व-उत्पत्ति और मिश्रित रूप है, यह पाठ में करना चाहिए",
    "gaṇanāya upadhāretvā gaṇetabbaṃ": "गणना में ध्यान से देखकर गिनना चाहिए",
    'idhāpi "sahajātaṃ, purejātaṃ" yaṃ missakapañhā atthi':
        "यहाँ भी “सह-उत्पत्ति, पूर्व-उत्पत्ति” वाला जो मिश्रित प्रश्न है",
    'idhāpi "sahajātaṃ, purejātaṃ" yaṃ missakapañhā atthi, pāḷiyaṃ kātabbaṃ':
        "यहाँ भी “सह-उत्पत्ति, पूर्व-उत्पत्ति” वाला जो मिश्रित प्रश्न है, वह पाठ में करना चाहिए",
    "idhāpi sahajātaṃ, purejātaṃ atthi": "यहाँ भी सह-उत्पत्ति, पूर्व-उत्पत्ति है",
    "ye te pañhā na likhitā, te pāḷiyaṃ gaṇentānaṃ byañjanena na samenti":
        "जो प्रश्न नहीं लिखे गए, वे पाठ में गिनने वालों के लिए शब्दों से मेल नहीं खाते",
    "te pāḷiyaṃ na likhitā gaṇanā pākaṭā honti": "पाठ में न लिखे गए वे प्रश्न गणना से स्पष्ट हो जाते हैं",
    "yadi saṃsayo uppajjati, anulome atthipaccaye pekkhitabbaṃ":
        "यदि संदेह उत्पन्न होता है, तो सकारात्मक क्रम में उपस्थिति-कारण में देखना चाहिए",
    "idhāpi ārammaṇapaccayā upanissayapaccayā atthi, pāḷiyaṃ natthi":
        "यहाँ भी विषय-कारण से और प्रबल आश्रय-कारण से (प्रश्न) हैं, पाठ में नहीं हैं",
    "gaṇentena upadhāretvā gaṇetabbaṃ": "गिनने वाले को ध्यान से देखकर गिनना चाहिए",
    "idhāpi ārammaṇaupanissayā atthi": "यहाँ भी विषय-कारण और प्रबल आश्रय-कारण हैं",
    "āsevanamūlake vuṭṭhānassapi āvajjanāyapi pahātabbaṃ":
        "पुनरावृत्ति-कारण से शुरू होने वाली शृंखला में बाहर आने को भी, मन को विषय की ओर मोड़ने को भी छोड़ देना चाहिए",
}

# ---------------------------------------------------------------- prefixes and labels
PREFIX_X = {"nirodhā vuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में"}
LABEL = {"sahajātā": "सह-उत्पत्ति"}
PERSON = {"ariyā": ("आर्य", "p"), "sekkhā": (S.SEKKHA, "p"), "trainees": (S.SEKKHA, "p"),
          "arahā": ("अर्हत्", "s"), "sekkhā vā puthujjanā vā": (S.SEKKHA_PUTHU, "p"),
          "trainees vā puthujjanā vā": (S.SEKKHA_PUTHU, "p")}

# ---------------------------------------------------------------- objects of paṭicca / paccayā / saṃsaṭṭhā (oblique)
_VI, _UD = "संशय के साथ होने वाले", "बेचैनी के साथ होने वाले"
OBJ_X = {
    "§ ekaṃ khandhaṃ": "‹0E› समूह",
    "ahetukaṃ § ekaṃ khandhaṃ": "मूल से रहित, ‹0E› समूह",
    "§ khandhe": "‹0o› समूहों",
    "§ khandhe ca mahābhūte ca": "‹0o› समूहों और महाभूतों",
    "kusale § khandhe ca mahābhūte ca": "हितकर ‹0o› समूहों और महाभूतों",
    "§ ekaṃ khandhañca vatthuñca": "‹0E› समूह और आधार",
    "§ khandhe ca vatthuñca": "‹0o› समूहों और आधार",
    "vipākaṃ § ekaṃ khandhaṃ": "एक कर्म-फल रूपी ‹0o› समूह",
    "vipāke § khandhe": "कर्म-फल रूपी ‹0o› समूहों",
    "vipāke § khandhe ca mahābhūte ca": "कर्म-फल रूपी ‹0o› समूहों और महाभूतों",
    "vipākaṃ § ekaṃ khandhañca vatthuñca": "एक कर्म-फल रूपी ‹0o› समूह और आधार",
    "kusale § khandhe": "हितकर ‹0o› समूहों",
    "kusalaṃ § ekaṃ khandhaṃ": "एक हितकर ‹0o› समूह",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ": f"{_VI} या {_UD} मोह",
    "vicikicchāsahagataṃ mohaṃ": f"{_VI} मोह",
    "uddhaccasahagataṃ mohaṃ": f"{_UD} मोह",
    "vicikicchāsahagataṃ ekaṃ khandhaṃ": f"{_VI} एक समूह",
    "uddhaccasahagataṃ ekaṃ khandhaṃ": f"{_UD} एक समूह",
    "vicikicchāsahagataṃ ekaṃ khandhañca mohañca": f"{_VI} एक समूह और मोह",
    "uddhaccasahagataṃ ekaṃ khandhañca mohañca": f"{_UD} एक समूह और मोह",
    "vicikicchāsahagataṃ ekaṃ khandhañca vatthuñca": f"{_VI} एक समूह और आधार",
    "uddhaccasahagataṃ ekaṃ khandhañca vatthuñca": f"{_UD} एक समूह और आधार",
    "dve khandhe ca mohañca": "दो समूहों और मोह",
    "dve khandhe ca vatthuñca": "दो समूहों और आधार",
    "vicikicchāsahagate khandhe": f"{_VI} समूहों",
    "uddhaccasahagate khandhe": f"{_UD} समूहों",
    "vicikicchāsahagate khandhe ca mohañca": f"{_VI} समूहों और मोह",
    "uddhaccasahagate khandhe ca mohañca": f"{_UD} समूहों और मोह",
    "vicikicchāsahagate khandhe ca vatthuñca": f"{_VI} समूहों और आधार",
    "uddhaccasahagate khandhe ca vatthuñca": f"{_UD} समूहों और आधार",
    "vicikicchāsahagate uddhaccasahagate khandhe ca vatthuñca": f"{_VI} और {_UD} समूहों और आधार",
    "pañcaviññāṇasahagataṃ ekaṃ khandhaṃ": "पाँच प्रकार की चेतना के साथ होने वाले एक समूह",
    "cakkhāyatanaṃ": "आँख के इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ": "शरीर के इंद्रिय-क्षेत्र",
    "asaññasattānaṃ": "पहचान-रहित प्राणियों में",
    "53asaññasattānaṃ": "53पहचान-रहित प्राणियों में",  # footnote digits glued to the word, kept as written
    "ahetukaṃ ekaṃ": "मूल से रहित एक",
    "asaññasattānaṃ ekaṃ": "पहचान-रहित प्राणियों में एक",
    "§": "‹0o›",
}

# ---------------------------------------------------------------- what arises (direct)
RES_X = {
    "sampayuttakā khandhā": "जुड़े हुए समूह",
    "sampayuttakā khandhā cittasamuṭṭhānañca rūpaṃ": f"जुड़े हुए समूह और {RUPA_CITTA}",
    "sampayuttakā cetanā": "जुड़ा हुआ इरादा",
    "§ khandhā": "‹0o› समूह",
    "ahetukā § khandhā": "मूल से रहित ‹0o› समूह",
    "ahetukā §": "मूल से रहित ‹0o›",
    "vipākā § khandhā": "कर्म-फल रूपी ‹0o› समूह",
    "§ cetanā": "‹0m› इरादा",
    "moho": "मोह",
    "vicikicchāsahagato moho": "संशय के साथ होने वाला मोह",
    "uddhaccasahagato moho": "बेचैनी के साथ होने वाला मोह",
    "vicikicchāsahagato moho cittasamuṭṭhānañca rūpaṃ": f"संशय के साथ होने वाला मोह और {RUPA_CITTA}",
    "uddhaccasahagato moho cittasamuṭṭhānañca rūpaṃ": f"बेचैनी के साथ होने वाला मोह और {RUPA_CITTA}",
    "vicikicchāsahagatā khandhā ca moho ca": f"{_VI} समूह और मोह",
    "uddhaccasahagatā khandhā ca moho ca": f"{_UD} समूह और मोह",
    "tayo khandhā ca moho ca": "तीन समूह और मोह",
    "dve khandhā ca moho ca": "दो समूह और मोह",
    "tayo khandhā moho ca": "तीन समूह और मोह",
    "dve khandhā moho ca": "दो समूह और मोह",
    "moho cittasamuṭṭhānañca rūpaṃ": f"मोह और {RUPA_CITTA}",
    "moho ca cittasamuṭṭhānañca rūpaṃ": f"मोह और {RUPA_CITTA}",
    "tayo khandhā moho ca cittasamuṭṭhānañca rūpaṃ": f"तीन समूह, मोह और {RUPA_CITTA}",
    "dve khandhā moho ca cittasamuṭṭhānañca rūpaṃ": f"दो समूह, मोह और {RUPA_CITTA}",
    "cakkhuviññāṇaṃ": "आँख की चेतना",
    "kāyaviññāṇaṃ": "शरीर की चेतना",
    "§+adhipati": "‹0f› प्रधानता",
    "§ adhipati": "‹0f› प्रधानता",
    "tayo khandhā": "तीन समूह",
    "dve khandhā": "दो समूह",
    "dve khandhā ca vatthu ca": "दो समूह और आधार",
    "upādārūpaṃ": RUPA_UPADA,
    "ekaṃ mahābhūtaṃ": "एक महाभूत",
    "asaññasattānaṃ ekaṃ mahābhūtaṃ": "पहचान-रहित प्राणियों में एक महाभूत",
    "pañcaviññāṇaṃ": "पाँच प्रकार की चेतना",
}

# ---------------------------------------------------------------- nouns: (acc, nom, dat, Hindi, gender)
NOUNS = [
    ("saddhaṃ", "saddhā", "saddhāya", "श्रद्धा", "f"),
    ("sīlaṃ", "sīlaṃ", "sīlassa", "सदाचार", "m"),
    ("sutaṃ", "sutaṃ", "sutassa", "सुना-सीखा ज्ञान", "m"),
    ("cāgaṃ", "cāgo", "cāgassa", "त्याग", "m"),
    ("paññaṃ", "paññā", "paññāya", "प्रज्ञा", "f"),
    ("rāgaṃ", "rāgo", "rāgassa", "राग", "m"),
    ("dosaṃ", "doso", "dosassa", "द्वेष", "m"),
    ("mohaṃ", "moho", "mohassa", "मोह", "m"),
    ("mānaṃ", "māno", "mānassa", "अहंकार", "m"),
    ("diṭṭhiṃ", "diṭṭhi", "diṭṭhiyā", "दृष्टि", "f"),
    ("patthanaṃ", "patthanā", "patthanāya", "कामना", "f"),
    ("kāyikaṃ sukhaṃ", "kāyikaṃ sukhaṃ", "kāyikassa sukhassa", "शारीरिक सुख", "m"),
    ("kāyikaṃ dukkhaṃ", "kāyikaṃ dukkhaṃ", "kāyikassa dukkhassa", "शारीरिक दुःख", "m"),
    ("utuṃ", "utu", "utussa", "तापमान", "m"),
    ("bhojanaṃ", "bhojanaṃ", "bhojanassa", "भोजन", "m"),
    ("senāsanaṃ", "senāsanaṃ", "senāsanassa", "निवास-स्थान", "m"),
    ("maggaṃ", "maggo", "maggassa", "मार्ग", "m"),
    ("phalasamāpattiṃ", "phalasamāpatti", "phalasamāpattiyā", "फल की ध्यान-अवस्था", "f"),
    ("jhānaṃ", "jhānaṃ", "jhānassa", "ध्यान", "m"),
    ("vicikicchaṃ", "vicikicchā", None, "संशय", "m"),
    ("uddhaccaṃ", "uddhaccaṃ", None, "बेचैनी", "f"),
    ("domanassaṃ", "domanassaṃ", None, "उदासी", "f"),
    ("phalaṃ", "phalaṃ", "phalassa", "फल", "m"),
]
NOUN_D_X = {  # bare words in «…pe…» lists (direct)
    "vipassanaṃ": "अंतर्दृष्टि", "abhiññaṃ": "उच्च ज्ञान", "samāpattiṃ": "ध्यान-अवस्था",
    "uposathakammaṃ": "उपवास-व्रत", "uposathaṃ": "उपवास-व्रत", "dānaṃ": "दान",
}
NOUN_O_X = {}

# ---------------------------------------------------------------- actions after «… upanissāya»
ACTIONS = {
    "dānaṃ deti": "दान देता है",
    "sīlaṃ samādiyati": "सदाचार ग्रहण करता है",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है",
    "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है",
    "§ jhānaṃ uppādeti": "‹0m› ध्यान उत्पन्न करता है",
    "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है",
    "maggaṃ uppādeti": "मार्ग उत्पन्न करता है",
    "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "phalasamāpattiṃ uppādeti": "फल की ध्यान-अवस्था उत्पन्न करता है",
    "mānaṃ jappeti": "अहंकार पालता है",
    "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "pāṇaṃ hanati": "जीव की हत्या करता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "attānaṃ ātāpeti paritāpeti pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti":
        "स्वयं को तपाता है, कष्ट देता है, खोज के कारण होने वाला दुःख भोगता है",
    "attānaṃ ātāpeti paritāpeti": "स्वयं को तपाता है, कष्ट देता है",
    "anuppannaṃ kiriyasamāpattiṃ uppādeti": "उत्पन्न न हुई केवल क्रिया रूपी ध्यान-अवस्था उत्पन्न करता है",
    "anuppannaṃ kusalasamāpattiṃ uppādenti": "उत्पन्न न हुई हितकर ध्यान-अवस्था उत्पन्न करते हैं",
    "anuppannaṃ samāpattiṃ uppādenti": "उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं",
    "uppannaṃ samāpajjanti": "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं",
    "uppannaṃ samāpajjati": "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करता है",
    "saṅkhāre aniccato": "निर्मित परिघटनाओं को अनित्य",
    "saṅkhāre aniccato dukkhato anattato vipassanti":
        f"निर्मित परिघटनाओं को {S.ANICCA} अंतर्दृष्टि से देखते हैं",
}

# ---------------------------------------------------------------- objects of review / insight: (direct, oblique, number)
_NANA = [("iddhividhañāṇ", "अलौकिक शक्तियों क{a} ज्ञान"), ("cetopariyañāṇ", "दूसरों के मन को जानने क{a} ज्ञान"),
         ("pubbenivāsānussatiñāṇ", "पूर्व जन्मों के अनुस्मरण क{a} ज्ञान"),
         ("yathākammūpagañāṇ", "प्राणियों के अपने कर्मों के अनुसार जाने क{a} ज्ञान"),
         ("anāgataṃsañāṇ", "भविष्य को जानने क{a} ज्ञान")]
_REVD = [("paṭhamajjhāna", "पहले ध्यान"), ("nevasaññānāsaññāyatana", "न पहचान न अ-पहचान के क्षेत्र"),
         ("dibbacakkhu", "दिव्य आँख"), ("dibbasotadhātu", "दिव्य कान के तत्व"),
         ("magga", "मार्ग"), ("phala", "फल"), ("nibbāna", "निर्वाण")] + \
        [(p + "a", h.format(a="े")) for p, h in _NANA]
ROBJ = {
    "§ khandhe": ("‹0o› समूह", "‹0o› समूहों", "p"),
    "§ ¤ khandhe": ("‹0o› ‹1o› समूह", "‹0o› ‹1o› समूहों", "p"),
    "khandhe": ("समूह", "समूहों", "p"),
    "vatthuṃ § khandhe": ("आधार और ‹0o› समूह", "आधार और ‹0o› समूहों", "p"),
    "§ khandhe ca mohañca": ("‹0o› समूह और मोह", "‹0o› समूहों और मोह", "p"),
    "vicikicchāsahagate khandhe ca mohañca": (f"{_VI} समूह और मोह", f"{_VI} समूहों और मोह", "p"),
    "uddhaccasahagate khandhe ca mohañca": (f"{_UD} समूह और मोह", f"{_UD} समूहों और मोह", "p"),
    "cakkhuṃ": ("आँख", "आँख", "s"), "sotaṃ": ("कान", "कान", "s"), "vatthuṃ": ("आधार", "आधार", "s"),
    "saṅkhāre": ("निर्मित परिघटनाएँ", "निर्मित परिघटनाओं", "p"),
    "dibbaṃ cakkhuṃ": ("दिव्य आँख", "दिव्य आँख", "s"),
    "dibbaṃ sotadhātuṃ": ("दिव्य कान का तत्व", "दिव्य कान के तत्व", "s"),
    "paṭhamaṃ jhānaṃ": ("पहला ध्यान", "पहले ध्यान", "s"),
    "ākāsānañcāyatanaṃ": ("अनंत आकाश का क्षेत्र", "अनंत आकाश के क्षेत्र", "s"),
    "viññāṇañcāyatanaṃ": ("अनंत चेतना का क्षेत्र", "अनंत चेतना के क्षेत्र", "s"),
    "ākiñcaññāyatanaṃ": ("कुछ भी न होने का क्षेत्र", "कुछ भी न होने के क्षेत्र", "s"),
    "nevasaññānāsaññāyatanaṃ": ("न पहचान न अ-पहचान का क्षेत्र", "न पहचान न अ-पहचान के क्षेत्र", "s"),
    "gotrabhuṃ": ("गोत्र-परिवर्तन", "गोत्र-परिवर्तन", "s"), "vodānaṃ": ("शुद्धि", "शुद्धि", "s"),
    "maggaṃ": ("मार्ग", "मार्ग", "s"), "phalaṃ": ("फल", "फल", "s"), "nibbānaṃ": ("निर्वाण", "निर्वाण", "s"),
    "jhānaṃ": ("ध्यान", "ध्यान", "s"),
    "§ phalaṃ": ("‹0m› फल", "‹0o› फल", "s"),
    "pubbe suciṇṇāni": ("पहले भली-भाँति किए गए कार्य", S.DEEDS, "p"),
    "pahīne kilese": ("छोड़े जा चुके मन के क्लेश", S.KILESA["pahīne"], "p"),
    "§ pahīne kilese": ("छोड़े जा चुके ‹0o› मन के क्लेश", "छोड़े जा चुके ‹0o› मन के क्लेशों", "p"),
    "vikkhambhite kilese": ("दबाए जा चुके मन के क्लेश", S.KILESA["vikkhambhite"], "p"),
    "pubbe samudāciṇṇe kilese": ("पहले बार-बार उठे मन के क्लेश", S.KILESA["pubbe samudāciṇṇe"], "p"),
}
for _p, _h in _NANA:
    ROBJ[_p + "aṃ"] = (_h.format(a="ा"), _h.format(a="े"), "s")
    ROBJ["§ " + _p + "aṃ"] = ("‹0m› " + _h.format(a="ा"), "‹0o› " + _h.format(a="े"), "s")
for _p, _h in _REVD:
    ROBJ[_p + "paccavekkhaṇaṃ"] = (f"{_h} पर हुआ पुनर्विचार", f"{_h} पर हुए पुनर्विचार", "s")
for _p, _h in [("rāgaṃ", "राग"), ("diṭṭhiṃ", "दृष्टि"), ("vicikicchaṃ", "संशय"), ("uddhaccaṃ", "बेचैनी"),
               ("domanassaṃ", "उदासी")]:
    ROBJ[_p] = (_h, _h, "s")
ROBJ["§ rāgaṃ"] = ("‹0m› राग", "‹0o› राग", "s")
ROBJ["§ domanassaṃ"] = ("‹0f› उदासी", "‹0f› उदासी", "s")
ROBJ["§ diṭṭhiṃ"] = ("‹0f› दृष्टि", "‹0f› दृष्टि", "s")

RVERB = {
    "paccavekkhati": ("review", "करता है"), "paccavekkhanti": ("review", "करते हैं"),
    "assādeti abhinandati": ("savour", "लेता है"), "assādenti abhinandanti": ("savour", "लेते हैं"),
    "assādeti": ("savour1", "लेता है"), "assādenti": ("savour1", "लेते हैं"),
    "aniccato dukkhato anattato vipassati": ("insight", "देखता है"),
    "aniccato dukkhato anattato vipassanti": ("insight", "देखते हैं"),
    "aniccato dukkhato anattato vippassati": ("insight", "देखता है"),
    "aniccato dukkhato anattato vippassanti": ("insight", "देखते हैं"),
    "aniccato": ("anicca", ""),
    "jānāti": ("know", "जानता है"), "jānanti": ("know", "जानते हैं"),
}

# ---------------------------------------------------------------- vippayutta short sentences
SHORT_SUBJ = {"khandhā": "समूह", "cittasamuṭṭhānaṃ rūpaṃ": RUPA_CITTA, "kaṭattārūpaṃ": RUPA_KATATTA,
              "vatthu": "आधार", "moho": "मोह", "khandhā ca moho ca": "समूह और मोह", "§ khandhā": "‹0o› समूह"}
SHORT_ON = {"vatthuṃ": "आधार", "khandhe": "समूहों", "mohaṃ": "मोह", "khandhe ca mohañca": "समूहों और मोह",
            "§ khandhe": "‹0o› समूहों"}

# ---------------------------------------------------------------- subjects and datives
_ORD = [("paṭham", "पहल"), ("dutiy", "दूसर"), ("tatiy", "तीसर"), ("catutth", "चौथ")]
SUBJ_P_X = {
    "§ dhammo": ("‹0f› परिघटना,", "fs"),
    "§ ca § ca dhammā": ("‹0f› और ‹1f› परिघटनाएँ,", "fp"),
}
SUBJ_U_X = {
    "khandhā": ("समूह", "mp"),
    "§ khandhā": ("‹0o› समूह", "mp"),
    "§ ¤ khandhā": ("‹0o› ‹1o› समूह", "mp"),
    "vipākā khandhā": ("कर्म-फल रूपी समूह", "mp"),
    "vipākā § khandhā": ("कर्म-फल रूपी ‹0o› समूह", "mp"),
    "sampayuttakā khandhā": ("जुड़े हुए समूह", "mp"),
    "vicikicchāsahagatā khandhā": (f"{_VI} समूह", "mp"),
    "uddhaccasahagatā khandhā": (f"{_UD} समूह", "mp"),
    "pacchājātā vicikicchāsahagatā khandhā": (f"बाद में उत्पन्न, {_VI} समूह", "mp"),
    "pacchājātā uddhaccasahagatā khandhā": (f"बाद में उत्पन्न, {_UD} समूह", "mp"),
    "pacchājātā § khandhā": ("बाद में उत्पन्न ‹0o› समूह", "mp"),
    "vicikicchāsahagato moho": ("संशय के साथ होने वाला मोह", "ms"),
    "uddhaccasahagato moho": ("बेचैनी के साथ होने वाला मोह", "ms"),
    "vicikicchāsahagato uddhaccasahagato moho": ("संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह", "ms"),
    "vatthu": ("आधार", "ms"),
    "mahābhūtā": ("महाभूत", "mp"),
    "rūpajīvitindriyañca": ("भौतिक जीवन-क्षमता", "fs"),
    "eko khandho": ("एक समूह", "ms"),
    "§ eko khandho": ("‹0D› समूह", "ms"),
    "vicikicchāsahagato eko khandho": ("संशय के साथ होने वाला एक समूह", "ms"),
    "uddhaccasahagato eko khandho": ("बेचैनी के साथ होने वाला एक समूह", "ms"),
    "vipāko § eko khandho": ("एक कर्म-फल रूपी ‹0m› समूह", "ms"),
    "dve khandhā": ("दो समूह", "mp"),
    "tayo khandhā": ("तीन समूह", "mp"),
    "§ cetanā": ("‹0m› इरादा", "ms"),
    "sampayuttakā cetanā": ("जुड़ा हुआ इरादा", "ms"),
    "§ hetū": ("‹0o› मूल", "mp"),
    "§+adhipati": ("‹0f› प्रधानता", "fs"),
    "§ adhipati": ("‹0f› प्रधानता", "fs"),
    "§ āhārā": ("‹0o› आहार", "mp"),
    "§ indriyā": ("‹0f› क्षमताएँ", "fp"),
    "purimā purimā § khandhā": ("पहले-पहले के ‹0o› समूह", "mp"),
    "purimā purimā vicikicchāsahagatā khandhā": (f"पहले-पहले के {_VI} समूह", "mp"),
    "purimā purimā uddhaccasahagatā khandhā": (f"पहले-पहले के {_UD} समूह", "mp"),
    "purimo purimo vicikicchāsahagato moho": ("पहले-पहले का संशय के साथ होने वाला मोह", "ms"),
    "purimo purimo uddhaccasahagato moho": ("पहले-पहले का बेचैनी के साथ होने वाला मोह", "ms"),
    "purimo purimo vicikicchāsahagato uddhaccasahagato moho":
        ("पहले-पहले का संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह", "ms"),
    "cuticittaṃ": ("मृत्यु का मन", "ms"),
    "§ cuticittaṃ": ("‹0m› मृत्यु का मन", "ms"),
    "bhavaṅgaṃ": ("जीवन-धारा", "fs"),
    "§ bhavaṅgaṃ": ("‹0f› जीवन-धारा", "fs"),
    "anulomaṃ": ("अनुरूपता", "fs"),
    "§ anulomaṃ": ("‹0f› अनुरूपता", "fs"),
    "arahato anulomaṃ": ("अर्हत् की अनुरूपता", "fs"),
    "sekkhānaṃ anulomaṃ": ("सीखने के चरण वाले व्यक्तियों की अनुरूपता", "fs"),
    "traineesgen anulomaṃ": ("सीखने के चरण वाले व्यक्तियों की अनुरूपता", "fs"),
    "gotrabhu": ("गोत्र-परिवर्तन", "ms"),
    "vodānaṃ": ("शुद्धि", "fs"),
    "§ phalaṃ": ("‹0m› फल", "ms"),
    "āvajjanā": ("मन को विषय की ओर मोड़ना", "ms"),
    "kiriyaṃ": ("केवल क्रिया रूपी मन", "ms"),
    "§ phalasamāpatti": ("‹0f› फल की ध्यान-अवस्था", "fs"),
    "ākāsānañcāyatanaṃ": ("अनंत आकाश का क्षेत्र", "ms"),
    "ākiñcaññāyatanaṃ": ("कुछ भी न होने का क्षेत्र", "ms"),
    "nevasaññānāsaññāyatanaṃ": ("न पहचान न अ-पहचान का क्षेत्र", "ms"),
    "nevasaññānāsaññāyatanakusalaṃ": ("न पहचान न अ-पहचान के क्षेत्र का हितकर मन", "ms"),
    "nevasaññānāsaññāyatanakiriyaṃ": ("न पहचान न अ-पहचान के क्षेत्र का केवल क्रिया रूपी मन", "ms"),
    "pāṇātipāto": ("जीव-हत्या", "fs"),
    "mātughātikammaṃ": ("माता की हत्या का कर्म", "ms"),
    "sakabhaṇḍe chandarāgo": ("अपनी वस्तुओं के प्रति चाह-राग", "ms"),
    "sakapariggahe chandarāgo": ("अपने परिग्रह के प्रति चाह-राग", "ms"),
    "paṭhamassa jhānassa parikammaṃ": ("पहले ध्यान की प्रारंभिक तैयारी", "fs"),
    "nevasaññānāsaññāyatanassa parikammaṃ": ("न पहचान न अ-पहचान के क्षेत्र की प्रारंभिक तैयारी", "fs"),
    "dibbassa cakkhussa parikammaṃ": ("दिव्य आँख की प्रारंभिक तैयारी", "fs"),
    "51anantarūpanissayo": ("51निकटता रूपी प्रबल आश्रय", "ms"),
}
for _p, _h in _ORD:
    SUBJ_U_X[f"{_p}aṃ jhānaṃ"] = (f"{_h}ा ध्यान", "ms")
    SUBJ_U_X[f"{_p}o maggo"] = (f"{_h}ा मार्ग", "ms")
    SUBJ_U_X[f"{_p}assa jhānassa parikammaṃ"] = (f"{_h}े ध्यान की प्रारंभिक तैयारी", "fs")
    SUBJ_U_X[f"{_p}assa maggassa parikammaṃ"] = (f"{_h}े मार्ग की प्रारंभिक तैयारी", "fs")
for _p, _h in _NANA:
    SUBJ_U_X[_p + "aṃ"] = (_h.format(a="ा"), "ms")
    SUBJ_U_X["§ " + _p + "aṃ"] = ("‹0m› " + _h.format(a="ा"), "ms")
    SUBJ_U_X[_p + "assa parikammaṃ"] = (_h.format(a="े") + " की प्रारंभिक तैयारी", "fs")
for _p, _h in _REVD:
    SUBJ_U_X[_p + "paccavekkhaṇaṃ"] = (f"{_h} पर हुआ पुनर्विचार", "ms")

DAT_P_X = {
    "§ dhammassa": "‹0f› परिघटना के लिए",
    "§ ca § ca dhammassa": "‹0f› परिघटना और ‹1f› परिघटना के लिए",
    "tasseva": "उसी के लिए",
}
DAT_U_X = {
    "tiṇṇannaṃ khandhānaṃ": ("तीन समूहों", False),
    "dvinnaṃ khandhānaṃ": ("दो समूहों", False),
    "khandhānaṃ": ("समूहों", False),
    "§ khandhānaṃ": ("‹0o› समूहों", False),
    "sampayuttakānaṃ khandhānaṃ": ("जुड़े हुए समूहों", False),
    "vicikicchāsahagatānaṃ khandhānaṃ": (f"{_VI} समूहों", False),
    "uddhaccasahagatānaṃ khandhānaṃ": (f"{_UD} समूहों", False),
    "pacchimānaṃ pacchimānaṃ § khandhānaṃ": ("बाद-बाद के ‹0o› समूहों", False),
    "pacchimānaṃ pacchimānaṃ vicikicchāsahagatānaṃ khandhānaṃ": (f"बाद-बाद के {_VI} समूहों", False),
    "pacchimānaṃ pacchimānaṃ uddhaccasahagatānaṃ khandhānaṃ": (f"बाद-बाद के {_UD} समूहों", False),
    "pacchimassa pacchimassa mohassa": ("बाद-बाद के मोह", False),
    "pacchimassa pacchimassa vicikicchāsahagatassa uddhaccasahagatassa mohassa":
        (f"बाद-बाद के {_VI} या {_UD} मोह", False),
    "vipākānaṃ § khandhānaṃ": ("कर्म-फल रूपी ‹0o› समूहों", False),
    "vipākānaṃ khandhānaṃ": ("कर्म-फल रूपी समूहों", False),
    "cittasamuṭṭhānānaṃ rūpānaṃ": ("मन से उत्पन्न भौतिक रूपों", False),
    "cittasamuṭṭhānānañca rūpānaṃ": ("मन से उत्पन्न भौतिक रूपों", True),
    "kaṭattā ca rūpānaṃ": ("किए गए कर्म से उत्पन्न भौतिक रूपों", True),
    "vatthussa": ("आधार", False),
    "upapatticittassa": ("जन्म के मन", False),
    "§ upapatticittassa": ("‹0o› जन्म के मन", False),
    "§ āvajjanāya": ("‹0o› मन को विषय की ओर मोड़ने", False),
    "vuṭṭhānassa": ("बाहर आने", False),
    "§ vuṭṭhānassa": ("‹0o› बाहर आने", False),
    "§ phalassa": ("‹0o› फल", False),
    "§ phalasamāpattiyā": ("‹0f› फल की ध्यान-अवस्था", False),
    "viññāṇañcāyatanassa": ("अनंत चेतना के क्षेत्र", False),
    "nevasaññānāsaññāyatanassa": ("न पहचान न अ-पहचान के क्षेत्र", False),
    "viññāṇañcāyatanavipākassa": ("अनंत चेतना के क्षेत्र के कर्म-फल रूपी मन", False),
    "nevasaññānāsaññāyatanavipākassa": ("न पहचान न अ-पहचान के क्षेत्र के कर्म-फल रूपी मन", False),
    "kiriyassa": ("केवल क्रिया रूपी मन", False),
    "vipākassa": ("कर्म-फल", False),
    "pāṇātipātassa": ("जीव-हत्या", False),
    "mātughātikammassa": ("माता की हत्या के कर्म", False),
    "parabhaṇḍe chandarāgassa": ("पराई वस्तुओं के प्रति चाह-राग", False),
    "parapariggahe chandarāgassa": ("पराए परिग्रह के प्रति चाह-राग", False),
    "atthappaṭisambhidāya": ("अर्थ के विश्लेषणात्मक ज्ञान", False),
    "ariyānaṃ atthappaṭisambhidāya": ("आर्यों के अर्थ के विश्लेषणात्मक ज्ञान", False),
    "sekkhānaṃ atthappaṭisambhidāya": ("सीखने के चरण वाले व्यक्तियों के अर्थ के विश्लेषणात्मक ज्ञान", False),
    "traineesgen atthappaṭisambhidāya": ("सीखने के चरण वाले व्यक्तियों के अर्थ के विश्लेषणात्मक ज्ञान", False),
    "paṭibhānapaṭisambhidāya": ("सूझ-बूझ के विश्लेषणात्मक ज्ञान", False),
    "paṭibhānappaṭisambhidāya": ("सूझ-बूझ के विश्लेषणात्मक ज्ञान", False),
    "ṭhānāṭhānakosallassa": ("संभव और असंभव को जानने की कुशलता", False),
    "maggassa": ("मार्ग", False),
    "phalassa": ("फल", False),
    "gotrabhussa": ("गोत्र-परिवर्तन", False),
    "vodānassa": ("शुद्धि", False),
}
for _p, _h in _ORD:
    DAT_U_X[f"{_p}assa jhānassa"] = (f"{_h}े ध्यान", False)
    DAT_U_X[f"{_p}assa maggassa"] = (f"{_h}े मार्ग", False)

# ---------------------------------------------------------------- other clauses
CLAUSE_X = {
    ".": "।",
    "anulomaṃ": "सकारात्मक क्रम",
    "paccanīyaṃ": "नकारात्मक क्रम",
    "anulomapaccanīyaṃ": "सकारात्मक-नकारात्मक क्रम",
    "paccanīyānulomaṃ": "नकारात्मक-सकारात्मक क्रम",
    "paṭiccavāro": "निर्भरता का खंड",
    "pañhāvāro": "प्रश्नों का खंड",
    "paccayavāro": "कारण का खंड",
    "saṃsaṭṭhavāro": "घुले-मिले होने का खंड",
    "tīṇi": "तीन",
    "ekaṃ": "एक",
    "satta": "सात",
    "§": "‹0f›",
    "dve khandhe": "दो समूहों",
    "dve khandhe ca": "दो समूहों और",
    "dve khandhā": "दो समूह",
    "cittasamuṭṭhānañca rūpaṃ": "और " + RUPA_CITTA,
    "paṭisandhikkhaṇe §": "पुनर्जन्म के क्षण में ‹0o›",
    "ahetukapaṭisandhikkhaṇe ekaṃ": "मूल से रहित पुनर्जन्म के क्षण में एक",
    "arūpe bhāvanāya": "अभौतिक लोक में मानसिक अभ्यास से",
    "§ dhammaṃ paccayā nevadassanena nabhāvanāya": "‹0f› परिघटना के कारण न सत्य-दर्शन से, न मानसिक अभ्यास से",
    # labels
    "sahajātaṃ": "सह-उत्पत्ति", "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति",
    "āhāraṃ": "आहार", "indriyaṃ": "क्षमता", "sahajātā": "सह-उत्पत्ति", "pacchājātā": "पश्चात्-उत्पत्ति",
    "nānākkhaṇikā": "भिन्न क्षण", "sahajāto": "सह-उत्पत्ति",
    "ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय",
    "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय", "51anantarūpanissayo": "51निकटता रूपी प्रबल आश्रय",
    "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति", "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति",
    "ārammaṇādhipati": "विषय रूपी प्रधानता", "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
    # bare verbs and fragments
    "vipassati": S.VIPASSATI["s"],
    "vipassanti": S.VIPASSATI["p"],
    "assādeti abhinandati": "रस लेता है, आनंद लेता है",
    "assādenti abhinandanti": "रस लेते हैं, आनंद लेते हैं",
    "assādenti": "रस लेते हैं",
    "vipassati assādeti abhinandati": S.VIPASSATI["s"] + ", रस लेता है, आनंद लेता है",
    "vippassati assādeti abhinandati": S.VIPASSATI["s"] + ", रस लेता है, आनंद लेता है",
    "vipassanti assādenti abhinandanti": S.VIPASSATI["p"] + ", रस लेते हैं, आनंद लेते हैं",
    "dānaṃ datvā": "दान देकर",
    "cetopariyañāṇena": S.CETOPARIYA,
    "vatthuṃ ārabbha": "आधार को विषय बनाकर",
    "taṃ ārabbha rāgo": "उसे विषय बनाकर राग",
    "taṃ ārabbha § rāgo": "उसे विषय बनाकर ‹0m› राग",
    "uddhaccaṃ ārabbha diṭṭhi uppajjati": "बेचैनी को विषय बनाकर दृष्टि उत्पन्न होती है",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati":
        f"{S.GIFT} उसे महत्व देकर पुनः विचार करता है",
    "pubbe suciṇṇāni": "पहले भली-भाँति किए गए कार्य",
    "ariyā pahīne kilese paccavekkhanti vikkhambhite kilese paccavekkhanti":
        f"आर्य {S.KILESA['pahīne']} पर पुनः विचार करते हैं, {S.KILESA['vikkhambhite']} पर पुनः विचार करते हैं",
    "nevasaññānāsaññāyatanaṃ nirodhā vuṭṭhahantassa phalasamāpattiyā":
        "न पहचान न अ-पहचान का क्षेत्र, समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में फल की ध्यान-अवस्था के लिए",
    "samāpattiṃ uppādeti § saddhā": "ध्यान-अवस्था उत्पन्न करता है ‹0f› श्रद्धा",
    "§ ca": "‹0f› और",
    "cittasamuṭṭhānaṃ rūpaṃ": RUPA_CITTA,
    "§ ca § ca dhammā § dhammassa sahajātaṃ": "‹0f› और ‹1f› परिघटनाएँ, ‹2f› परिघटना के लिए सह-उत्पत्ति",
    "nirodhā vuṭṭhahantassa": PREFIX_X["nirodhā vuṭṭhahantassa"],
    "nevasaññānāsaññāyatanaṃ nirodhā vuṭṭhahantassa":
        "न पहचान न अ-पहचान का क्षेत्र, समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में",
    "ariyā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": "आर्य मार्ग से उठकर मार्ग पर पुनः विचार करते हैं",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti":
        "आर्य मार्ग से उठकर मार्ग को महत्व देकर पुनः विचार करते हैं",
    "maggapaccayā,": "मार्ग-कारण से,",
    "pakatūpanissayo § saddhaṃ upanissāya § jhānaṃ uppādeti":
        "स्वाभाविक प्रबल आश्रय ‹0f› श्रद्धा के प्रबल आश्रय से ‹1m› ध्यान उत्पन्न करता है",
    "trainees": S.SEKKHA,
}
for _p, _h in _ORD:
    DAT_U_X[f"{_p}assa"] = (f"{_h}े", False)
