"""pi-2 Pāli->Hindi keyword map: 3-dhatuvibhango.

usage: python -I -X utf8 map_3-dhatuvibhango_hi.py
Imports map_sample_hi (read-only) and the shared table of chapters 2/3/8/9; extends them here only.
"""
import importlib
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PP_SEGMENTS, NDE, build_part, verify, read_hindi, lc  # noqa: E402
C = importlib.import_module("map_2-3-8-9_common_hi")

CH = "3-dhatuvibhango"
PP_SEGMENTS.update({"2-187", "2-188"})

T = {"dhātu": "तत्व", "dhātuyo": "तत्व", "dhātuyā": "तत्व"}

# the eighteen dhātus (Abhidhamma part): «आँख का तत्व», «आँख की चेतना का तत्व» …
SENSE = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर", "mano": "मन"}
OBJ = {"rūpa": "दृश्य रूप", "sadda": "ध्वनि", "gandha": "गंध", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श",
       "dhamma": "मन के विषयों"}
for _p, _h in SENSE.items():
    T[_p] = _h
    T[_p + "dhātu"] = f"{_h} का तत्व"
    if _p != "mano":
        T[_p + "viññāṇa"] = f"{_h} की चेतना"
        T[_p + "viññāṇadhātu"] = f"{_h} की चेतना का तत्व"
for _p, _h in OBJ.items():
    T[_p] = _h if _p != "dhamma" else "मन के विषय"
    T[_p + "dhātu"] = f"{_h} का तत्व"

T.update({
    # the six elements («पृथ्वी तत्व» … without का; viññāṇadhātu there = «चेतना तत्व»)
    "ākāsa": "आकाश", "ākāso": "आकाश", "ākāsadhātu": "आकाश तत्व", "dhātudvayaṃ": "तत्व दो प्रकार का",
    "dvayaṃ": "दो प्रकार का", "pathavī": "पृथ्वी",
    "ajjhattikā": "आंतरिक", "bāhirā": "बाह्य", "bāhiraṃ": "बाह्य", "paccattaṃ": "अपने भीतर",
    "seyyathidaṃ": "जैसे", "aññampi": "अन्य", "yaṃ vā pana": "या जो कुछ भी", "tadekajjhaṃ": "उस सबको एक साथ",
    # earth
    "kakkhaḷaṃ": "कठोर", "kharigataṃ": "कड़ा", "kakkhaḷattaṃ": "कठोरता",
    "kesā": "सिर के बाल", "lomā": "रोएँ", "nakhā": "नाखून", "dantā": "दाँत", "taco": "त्वचा", "maṃsaṃ": "मांस",
    "nhāru": "नसें", "aṭṭhi": "हड्डी", "miñjaṃ": "मज्जा", "vakkaṃ": "गुर्दा", "hadayaṃ": "हृदय",
    "yakanaṃ": "यकृत", "kilomakaṃ": "झिल्ली", "pihakaṃ": "तिल्ली", "papphāsaṃ": "फेफड़ा", "antaṃ": "आँत",
    "antaguṇaṃ": "आँतों की मेखला", "udariyaṃ": "पेट का भोजन", "karīsaṃ": "मल",
    "ayo": "लोहा", "lohaṃ": "ताँबा", "tipu": "राँगा", "sajjhaṃ": "कच्ची चाँदी", "muttā": "मोती", "maṇi": "मणि",
    "veḷuriyo": "वैदूर्य", "saṅkho": "शंख", "silā": "पत्थर", "pavāḷaṃ": "मूँगा", "rajataṃ": "चाँदी",
    "lohitaṅko": "लाल मणि", "masāragallaṃ": "पन्ना", "tiṇaṃ": "घास", "kaṭṭhaṃ": "लकड़ी", "sakkharā": "कंकड़",
    "kaṭhalaṃ": "ठीकरा", "bhūmi": "भूमि", "pāsāṇo": "चट्टान", "pabbato": "पर्वत",
    # water
    "āpogataṃ": "जल की प्रकृति वाला", "sineho": "नमी", "sinehagataṃ": "नमी की प्रकृति वाला",
    "bandhanattaṃ": "बाँधे रखना", "rūpassa": "भौतिक रूप",
    "pittaṃ": "पित्त", "semhaṃ": "कफ", "pubbo": "पीब", "lohitaṃ": "रक्त", "sedo": "पसीना", "medo": "चर्बी",
    "assu": "आँसू", "vasā": "वसा", "kheḷo": "लार", "siṅghāṇikā": "नाक का मैल", "lasikā": "जोड़ों का तरल",
    "muttaṃ": "मूत्र", "mūla": "जड़", "khandha": "तना", "taca": "छाल", "patta": "पत्ता", "puppha": "फूल",
    "phala": "फल", "raso": "रस", "khīraṃ": "दूध", "dadhi": "दही", "sappi": "घी", "navanītaṃ": "मक्खन",
    "madhu": "शहद", "phāṇitaṃ": "राब", "bhummāni": "धरती का", "udakāni": "जल", "antalikkhāni": "आकाश का",
    # fire
    "tejogataṃ": "अग्नि की प्रकृति वाला", "usmā": "ऊष्मा", "usmāgataṃ": "ऊष्मा की प्रकृति वाला",
    "usumaṃ": "गरमी", "usumagataṃ": "गरमी की प्रकृति वाला", "santappati": "तपना", "jīrīyati": "जीर्ण होना",
    "pariḍayhati": "जलना", "asita": "खाया", "pīta": "पिया", "khāyita": "चबाया", "sāyitaṃ": "चखा गया",
    "pariṇāmaṃ gacchati": "पचना",
    "kaṭṭhaggi": "लकड़ी की आग", "palālaggi": "पुआल की आग", "tiṇaggi": "घास की आग", "gomayaggi": "गोबर की आग",
    "thusaggi": "भूसी की आग", "saṅkāraggi": "कूड़े की आग", "indaggi": "बिजली की आग", "sūriya": "सूर्य",
    "sannicaya": "ढेर",
    "bāhirā tejo": "बाह्य अग्नि", "bāhirā tejodhātu": "बाह्य अग्नि तत्व",
    "ajjhattikā tejo": "आंतरिक अग्नि", "ajjhattikā tejodhātu": "आंतरिक अग्नि तत्व",
    # air
    "vāyogataṃ": "वायु की प्रकृति वाला", "thambhitattaṃ": "तना हुआ होना",
    "uddhaṅgamā": "ऊपर जाने वाला", "adhogamā": "नीचे जाने वाला", "gamā": "जाने वाला", "vātā": "हवा",
    "kucchisayā": "पेट में रहने वाला", "koṭṭhāsayā": "आँतों में रहने वाला",
    "aṅgamaṅgānusārino": "अंग-अंग में फैलने वाला", "ānusārino": "फैलने वाला", "satthaka": "चीरने जैसा",
    "khuraka": "छुरे जैसा", "uppalaka": "उखाड़ने जैसा", "assāso": "साँस लेना",
    "puratthimā": "पूर्वी", "sarajā": "धूल भरा", "arajā": "धूल रहित", "sītā": "ठंडा", "uṇhā": "गरम",
    "parittā": "मंद", "kāḷa": "काला", "verambha": "ऊँचे आकाश का", "pakkha": "पंख", "supaṇṇa": "गरुड़",
    "tālavaṇṭa": "ताड़ का पंखा", "vidhūpana": "पंखा झलना",
    "bāhirā vāyo": "बाह्य वायु", "bāhirā vāyodhātu": "बाह्य वायु तत्व",
    "ajjhattikā vāyo": "आंतरिक वायु", "ajjhattikā vāyodhātu": "आंतरिक वायु तत्व",
    # space
    "ākāsagataṃ": "आकाश की प्रकृति वाला", "aghaṃ": "रिक्त स्थान", "aghagataṃ": "रिक्त स्थान की प्रकृति वाला",
    "vivaro": "छेद", "vivaragataṃ": "छेद की प्रकृति वाला", "asamphuṭṭhaṃ": "अछूता", "maṃsa": "मांस",
    "lohitehi": "रक्त", "mahābhūtehi": "महाभूत", "bhūtehi": "महाभूत", "kaṇṇa": "कान", "nāsa": "नाक",
    "mukha": "मुँह", "dvāraṃ": "द्वार", "ajjhoharati": "निगलना", "santiṭṭhati": "ठहरना",
    "nikkhamati": "बाहर निकलना",
    "bāhirā ākāsa": "बाह्य आकाश", "bāhirā ākāsadhātu": "बाह्य आकाश तत्व",
    "ajjhattikā ākāsa": "आंतरिक आकाश", "ajjhattikā ākāsadhātu": "आंतरिक आकाश तत्व",
    # sukha … avijjā dhātu
    "sukhadhātu": "सुख का तत्व", "dukkhadhātu": "दुःख का तत्व", "somanassadhātu": "प्रसन्नता का तत्व",
    "domanassadhātu": "उदासी का तत्व", "upekkhādhātu": "समभाव का तत्व", "avijjādhātu": "अज्ञान का तत्व",
    "somanassa": "प्रसन्नता", "dukkha": "दुःख", "domanassa": "उदासी", "avijjā": "अज्ञान",
    "kāyikaṃ": "शारीरिक", "kāyasamphassajaṃ": "शरीर के संपर्क से उत्पन्न",
    "kāyasamphassajā": "शरीर के संपर्क से उत्पन्न", "cetosamphassa": "मन का संपर्क",
    "cetasikaṃ asātaṃ": "मानसिक असुहावनापन", "cetasikaṃ dukkhaṃ": "मानसिक दुःख", "dukkhaṃ": "दुःख",
    "dukkhaṃ vedayitaṃ": "दुःखद अनुभव", "dukkhā vedanā": "दुःखद अनुभूति",
    "aññāṇaṃ": "न जानना", "adassanaṃ": "न देखना", "anabhisamayo": "सत्य तक न पहुँचना",
    "ananubodho": "बोध न होना", "asambodho": "पूर्ण बोध न होना", "appaṭivedho": "भेद न पाना",
    "asaṅgāhaṇā": "न समेट पाना", "apariyogāhaṇā": "गहराई में न उतर पाना",
    "asamapekkhanā": "निष्पक्ष रूप से न देखना", "apaccavekkhaṇā": "पुनः विचार न करना",
    "apaccakkhakammaṃ": "प्रत्यक्ष न करना", "dummejjhaṃ": "दुर्बुद्धि", "bālyaṃ": "मूर्खता",
    "asampajaññaṃ": "स्पष्ट समझ का अभाव", "moho": "मोह", "pamoho": "गहरा मोह", "sammoho": "घोर मोह",
    "ogho": "बाढ़", "yogo": "जकड़न", "ānusayo": "सुप्त प्रवृत्ति", "pariyuṭṭhānaṃ": "आवेश",
    "laṅgī": "रुकावट", "akusala": "हानिकर",
    # kāma … avihiṃsā dhātu
    "kāmadhātu": "इंद्रिय-सुखों का तत्व", "byāpādadhātu": "दुर्भावना का तत्व", "vihiṃsādhātu": "हिंसा का तत्व",
    "nekkhammadhātu": "त्याग का तत्व", "abyāpādadhātu": "दुर्भावना के अभाव का तत्व",
    "avihiṃsādhātu": "अहिंसा का तत्व", "kāma": "इंद्रिय-सुख", "byāpāda": "दुर्भावना", "vihiṃsā": "हिंसा",
    "nekkhamma": "त्याग", "abyāpāda": "दुर्भावना का अभाव", "avihiṃsā": "अहिंसा",
    "paṭisaṃyutto": "जुड़ा", "kāmapaṭisaṃyutto": "इंद्रिय-सुखों से जुड़ा", "takko": "सोचना",
    "vitakko": "आरंभिक विचार", "saṅkappo": "संकल्प", "appanā": "टिकाना", "byappanā": "भली-भाँति टिकाना",
    "abhiniropanā": "विषय की ओर ले जाना", "micchā": "ग़लत", "micchāsaṅkappo": "ग़लत संकल्प",
    "nirayaṃ": "नरक", "pariyantaṃ": "सीमा", "karitvā": "बनाकर", "uparito": "ऊपर", "nimmita": "रचा गया",
    "vasavattī": "अधिकार रखने वाला", "deve": "देवता", "vasavattī deve": "अधिकार रखने वाला देवता",
    "āyatanā": "इंद्रिय-क्षेत्र", "viññāṇaṃ": "चेतना",
    "dasasu": "दस", "vatthūsu": "आधार", "cittassa": "मन", "āghāto": "आक्रोश", "paṭighāto": "प्रतिघात",
    "paṭighaṃ": "चिढ़", "paṭivirodho": "प्रतिविरोध", "kopo": "कोप", "pakopo": "प्रकोप",
    "sampakopo": "तीव्र प्रकोप", "doso": "द्वेष", "sampadoso": "तीव्र द्वेष", "byāpatti": "दुर्भावना",
    "manopadoso": "मन का गहरा द्वेष", "kujjhanā": "क्रोध करना", "dussanā": "द्वेष करना",
    "byāpajjanā": "दुर्भावना रखना", "caṇḍikkaṃ": "उग्रता", "asuropo": "कटु वचन", "anattamanatā": "अप्रसन्नता",
    "ekacco": "कोई व्यक्ति", "pāṇinā": "हाथ", "leḍḍunā": "ढेला", "daṇḍena": "डंडा", "satthena": "शस्त्र",
    "rajjuyā": "रस्सी", "aññataraññatarena": "किसी न किसी चीज़", "sattesu": "प्राणी", "viheṭheti": "सताना",
    "heṭhanā": "सताना", "viheṭhanā": "बहुत सताना", "hiṃsanā": "चोट पहुँचाना", "vihiṃsanā": "हिंसा करना",
    "rosanā": "चिढ़ाना", "parūpaghāto": "दूसरों पर आघात करना", "ūpaghāto": "आघात",
    "kusalā dhammā": "हितकर परिघटना", "metti": "मैत्री", "mettāyanā": "मैत्री करना",
    "mettācetovimutti": "मैत्री द्वारा मन की मुक्ति", "karuṇā": "करुणा", "karuṇāyitattaṃ": "करुणा से भरा होना",
    "karuṇācetovimutti": "करुणा द्वारा मन की मुक्ति", "cetovimutti": "मन की मुक्ति", "vimutti": "मुक्ति",
    "aṭṭhārasa": "अठारह", "aṭṭhārasa dhātuyo": "अठारह तत्व", "yaṃ": "जो",
    # Abhidhammabhājanīya
    "upādāya pasādo": "व्युत्पन्न संवेदनशीलता", "pasādo": "संवेदनशीलता", "bhūtānaṃ": "महाभूत",
    "mahābhūtānaṃ": "महाभूत", "suñño": "सूना", "gāmopeso": "गाँव", "vaṇṇa": "रंग", "nibhā": "आभा",
    "anidassano": "दिखाई न देने वाला", "sappaṭigho": "टकराव वाला",
    "anidassano sappaṭigho": "दिखाई न देने वाला और टकराव वाला", "appaṭighaṃ": "टकराव से रहित",
    "anidassanaappaṭighaṃ": "दिखाई न देने वाला और टकराव से रहित",
    "paṭicca": "निर्भर होकर", "rūpe": "दृश्य रूप", "sadde": "ध्वनि", "gandhe": "गंध", "rase": "स्वाद",
    "phoṭṭhabbe": "स्पर्श", "dhamme": "मन के विषय", "saddo": "ध्वनि", "gandho": "गंध", "kāyo": "शरीर",
    "sotaṃ": "कान", "ghānaṃ": "नाक", "uppajjati": "उत्पन्न होना", "uppajjati cittaṃ": "मन … उत्पन्न होना",
    "uppajjitvā": "उत्पन्न होकर", "niruddha": "समाप्त होना", "samanantarā": "ठीक बाद",
    "samannāhāro": "मनोयोग", "dhammesu": "परिघटना", "vā pana": "या", "paṇḍaraṃ": "उज्ज्वलता",
    "manindriyaṃ": "मन की क्षमता", "manāyatanaṃ": "मन का इंद्रिय-क्षेत्र",
    "dasa": "दस", "hetuko": "मूल वाला", "dhammāyatana": "मन के विषयों का इंद्रिय-क्षेत्र",
    "asaṅkhatā": "अनिर्मित", "asaṅkhatā dhātu": "अनिर्मित तत्व", "rāga": "राग", "dosa": "द्वेष", "moha": "मोह",
    "bahuvidhena vedanākkhandho": "अनेक प्रकार से अनुभूति का समूह",
    "bahuvidhena saññākkhandho": "अनेक प्रकार से पहचान का समूह",
    "bahuvidhena saṅkhārakkhandho": "अनेक प्रकार से मानसिक रचनाओं का समूह",
    "saṅkhāra": "मानसिक रचनाएँ", "āhāro": "भोजन", "abyākato": "नैतिक रूप से अनिर्धारित",
    "kusalo": "हितकर", "akusalo": "हानिकर",
    # Pañhāpucchaka
    "dhātuyo siyā": "तत्व कभी", "dhātuyo hetuvippayuttā": "तत्व मूलों से अलग",
    "dhātuyo pariyāpannā": "तत्व अस्तित्व के लोकों में समाया हुआ", "dhātuyo sappaṭighā": "तत्व टकराव वाला",
    "dasa dhātuyo": "दस तत्व", "ekādasa": "ग्यारह", "ekādasa dhātuyo": "ग्यारह तत्व", "dvādasa": "बारह",
    "dvādasa dhātuyo": "बारह तत्व", "pannarasa": "पंद्रह", "pannarasa dhātuyo": "पंद्रह तत्व",
    "soḷasa": "सोलह", "soḷasa dhātuyo": "सोलह तत्व", "sattarasa": "सत्रह", "sattarasa dhātuyo": "सत्रह तत्व",
    "nevavipākanavipākadhammadhammā": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "majjhimā": "मध्यम", "sappaṭighā": "टकराव वाला", "sanidassanā": "दिखाई देने वाला", "lokiyā": "लौकिक", "sahabhuno": "साथ-साथ होना", "sahabhū": "साथ-साथ होना",
    "asaṃkiliṭṭhā": "क्लेशों से मलिन न होने वाला",
    "kileso ceva kilesasampayuttā": "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी",
    "hetu ceva hetusampayuttā": "मूल रूपी भी और मूलों से जुड़ा भी",
    # as in the sample (KH_T)
    "vedanāya sampayuttā": "अनुभूति से जुड़ा", "sukhāya vedanāya sampayuttā": "सुखद अनुभूति से जुड़ा",
    "dukkhāya vedanāya sampayuttā": "दुःखद अनुभूति से जुड़ा",
})
TABLE = {**C.SHARED_TABLE, **T}

OVR = {
    # the six elements: «… आकाश तत्व, चेतना तत्व» (no का)
    "2-172": {"viññāṇadhātu": "चेतना तत्व"},
    "2-178": {"viññāṇadhātu": "चेतना तत्व"},
    # «khandharaso» = «तनों का रस»; but «khandhadhātuāyatanā» = «समूह, तत्व, इंद्रिय-क्षेत्र»
    "2-182": {"khandha": "समूह", "rūpā": "भौतिक रूप", "tadekajjhaṃ": "एक साथ", "sammā": "सही"},
    # «sammā pariṇāmaṃ gacchati» = «ठीक से पचती हैं»
    "2-175": {"sammā": "ठीक से"},
    # «Yaṃ rūpaṃ … vaṇṇanibhā» (दृश्य रूप; also «yañca rūpaṃ anidassanaappaṭighaṃ» भौतिक रूप); raso = rasadhātu
    "2-184": {"rūpaṃ": "दृश्य रूप", "raso": "स्वाद", "hetu": "मूल", "rūpa": "दृश्य रूप"},
    # «Vipākadhammadhammā / nevavipākanavipākadhammadhammā»: the dhammā fragment has no word of its own
    "2-187": {"dhammā": NDE, "uppannā": "उत्पन्न हो चुका", "parittā": "सीमित"},
    "2-188": {"rūpā": "भौतिक"},   # «Dasa dhātuyo rūpā» = «दस तत्व भौतिक हैं»
}


def value(bid, kw, kws, text):
    return C.shared_value(kw, kws, TABLE, bid, text)


def resolver(bid, kw, kws, _hi={}):
    if not _hi:
        _hi.update(read_hindi(CH))
    o = OVR.get(bid, {})
    if kw in o:
        return o[kw]
    return value(bid, kw, kws, _hi.get(bid))


_EAT = "text «खाई, पी, चबाई और चखी गई चीज़ें»: masculine dictionary form (खाया ~ खाई, पिया ~ पी, चबाया ~ चबाई); regular inflection the checker does not model"
_SAM = "text «समाए हुए»: समाया ~ समाए is regular inflection the checker does not model (as the sample, 2-153)"
_HO = "text «साथ-साथ होता है / नहीं होते»: होना ~ होता/होते, the checker does not inflect the two-letter stem"
ALLOWED = {
    ("2-174", "phala"): "text «फलों का रस»: फल ~ फलों, the checker does not inflect a two-letter word",
    ("2-175", "asita"): _EAT, ("2-175", "pīta"): _EAT, ("2-175", "khāyita"): _EAT,
    ("2-177", "asita"): _EAT, ("2-177", "pīta"): _EAT, ("2-177", "khāyita"): _EAT,
    ("2-188", "dhātuyo pariyāpannā"): _SAM, ("2-188", "apariyāpannā"): _SAM,
    ("2-188", "sahabhuno"): _HO, ("2-188", "sahabhū"): _HO,
}

if __name__ == "__main__":
    build_part(CH, resolver)
    verify(CH, allowed=ALLOWED)
