"""Shared tables for the chapters 10-bojjhangavibhango, 12-jhanavibhango, 13-appamannavibhango,
14-sikkhapadavibhango (pi-2 Hindi keyword maps). Extends PI2 of map_sample_hi.py (imported read-only).
Importing writes nothing."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI2, PP_SEGMENTS, pi2_value, NDE  # noqa: E402

T_ALL = {}          # shared by the four chapters
CHAPTER_T = {}      # {chapter: {kw: value}}
OVR = {}            # {chapter: {bid: {kw: value}}}
PP = {}             # {chapter: {bid, ...}} Pañhāpucchaka segments
ALLOWED = {}        # {chapter: {(bid, kw): reason}} presence exceptions

KIYA = "text «किए जाने»: किया ~ किए is regular inflection the checker does not model (pi-1 value kept)"

# ---------------------------------------------------------------- shared (pi-1 wording for identical Pāli)
T_ALL.update({
    "sammā": "सही",                     # sammāsati / sammādiṭṭhi … (PI2 «पूर्ण रूप से» is the preamble's sammāsambuddha)
    "bhikkhu": "भिक्षु", "idha": "यहाँ",
    # the lokuttara-jhāna opening (pi-1 1-277 …)
    "lokuttaraṃ": "लोकोत्तर", "lokuttaraṃ jhānaṃ": "लोकोत्तर ध्यान", "jhānaṃ": "ध्यान",
    "bhāveti": "अभ्यास करना", "jhānaṃ bhāveti": "ध्यान का अभ्यास करना",
    "lokuttaraṃ jhānaṃ bhāveti": "लोकोत्तर ध्यान का अभ्यास करना",
    "niyyānikaṃ": "मुक्ति की ओर ले जाने वाला", "apacayagāmiṃ": "संचय घटाने की ओर ले जाने वाला",
    "niyyānikaṃ apacayagāmiṃ": "मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला",
    "gāmiṃ": "की ओर ले जाने वाला", "apacayagāmino": "संचय घटाने की ओर ले जाने वाला",
    "pahānāya": "छोड़ना", "diṭṭhigatānaṃ": "दृष्टियों में फँसना",
    "diṭṭhigatānaṃ pahānāya": "दृष्टियों में फँसने को छोड़ना",
    "bhūmiyā": "चरण", "pattiyā": "प्राप्ति", "paṭhamāya": "पहला",
    "vivicca": "अलग होकर", "vivicceva": "अलग होकर", "kāmehi": "इंद्रिय-सुख",
    "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर",
    "upasampajja": "प्राप्त करके", "viharati": "रहना", "upasampajja viharati": "प्राप्त करके उसमें रहना",
    "paṭipadaṃ": "प्रगति", "dukkhapaṭipadaṃ": "दुःखद प्रगति", "abhiññaṃ": "उच्च ज्ञान", "ābhiññaṃ": "उच्च ज्ञान",
    "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला", "dandha": "धीमा",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "दुःखद प्रगति और धीमे उच्च ज्ञान वाला",
    "samaye": "उस समय", "suññataṃ": "शून्य",
    "katattā": "किया जाना", "bhāvitattā": "अभ्यास किया जाना",
    "kusalassa jhānassa": "हितकर ध्यान", "dhammā kusalā": "हितकर परिघटना", "dhammā": "परिघटना",
    "avasesā": "शेष", "avasesā dhammā": "शेष परिघटना",
    # factor strings (pi-1)
    "maggaṅgaṃ": "मार्ग का अंग", "upekkhanā": "समभाव रखना",
    "paṭippassambhanā": "पूरी तरह शांत होना", "paṭippassambhitattaṃ": "पूरी तरह शांत हो चुका होना",
    "vīriyārambho": "उत्साह जगाना",
    # Pañhāpucchaka
    "appaṭighā": "टकराव से रहित", "appaṭigho": "टकराव से रहित",
    "anidassanaappaṭighā": "दिखाई न देने वाला और टकराव से रहित",
    "anidassanaappaṭigho": "दिखाई न देने वाला और टकराव से रहित",
    "aniyatā": "अनिश्चित", "saṃkilesikā": "क्लेशों का विषय बनने वाला", "pahātabbā": "छोड़ा जाने वाला",
    "upādāniyā": "आसक्ति का विषय बनने वाला", "sahetukā": "मूल वाला", "na hetū": "मूल रूपी न होने वाला",
    "vicārā": "सतत विचार", "vitakkā": "आरंभिक विचार", "cittā": "मन", "saṃsaṭṭha": "घुला-मिला",
    "lokuttarā": "लोकोत्तर", "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित",
    "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarā": "अभौतिक लोक से संबंधित",
    "āvacarā": "लोक से संबंधित", "vippayuttā": "अलग", "ārammaṇā": "विषय वाला",
    "uppajjati": "उत्पन्न होना", "samannāgato": "युक्त",
})

# ---------------------------------------------------------------- 10-bojjhangavibhango
BOJ = {"sati": "सजगता", "dhammavicaya": "परिघटनाओं की छानबीन", "vīriya": "उत्साह", "pīti": "उल्लास",
       "passaddhi": "प्रशांति", "samādhi": "एकाग्रता", "upekkhā": "समभाव"}
T10 = {
    "bojjhaṅga": "जागृति के अंग", "bojjhaṅgā": "जागृति के … अंग", "bojjhaṅgānaṃ": "जागृति के … अंग",
    "sambojjhaṅgo": "जागृति का अंग", "sambojjhaṅgaṃ": "जागृति का अंग",
    "sambojjhaṅgaṃ bhāveti": "जागृति के अंग का अभ्यास करना",
    "vicaya": "छानबीन", "dhammavicaya": "परिघटनाओं की छानबीन", "dhamma": "परिघटना",
    # 2-467 (Suttanta account)
    "satimā": "सजग", "paramena": "उच्चतम", "nepakkena": "सावधानी", "cirakatampi": "बहुत पहले किया गया",
    "saritā": "याद करने वाला", "anussaritā": "बार-बार याद करने वाला", "viharanto": "रहना",
    "dhammaṃ": "शिक्षा", "paññāya": "प्रज्ञा", "pavicinati": "छानबीन करना", "pavicarati": "गहराई से परखना",
    "parivīmaṃsamāpajjati": "पूरी जाँच-पड़ताल में लग जाना", "āpajjati": "लग जाना",
    "āraddhaṃ": "जाग्रत", "asallīnaṃ": "ढीला नहीं पड़ना", "nirāmisā": "सांसारिक भोग से रहित",
    "pītimanassa": "मन उल्लास से भरा", "kāyopi": "काया", "passambhati": "शांत होना",
    "sukhino": "सुखी", "samāhitaṃ": "एकाग्र हुआ", "ajjhupekkhitā": "समभाव से देखने वाला",
    # 2-469
    "ajjhattaṃ": "स्वयं से संबंधित", "ajjhattaṃ dhammesu": "स्वयं से संबंधित परिघटना",
    "bahiddhā dhammesu": "दूसरों से संबंधित परिघटना", "dhammesu": "परिघटना", "tadapi": "वह भी",
    "abhiññāya": "उच्च ज्ञान", "sambodhāya": "पूर्ण जागृति", "saṃvattati": "की ओर ले जाना",
    "kāyikaṃ": "शारीरिक", "cetasikaṃ": "मानसिक",
    # 2-471
    "viveka": "अलगाव", "virāga": "वैराग्य", "nirodha": "समाप्ति", "vossagga": "त्याग",
    "pariṇāmiṃ": "परिणत होने वाला",
    # 2-474 … upekkhā string (ch10 wording; ch12 has «उदासीन भाव से देखना, मन का संतुलन»)
    "majjhattatā": "तटस्थता", "ajjhupekkhanā": "तटस्थ भाव से देखना",
}
for _p, _h in BOJ.items():
    for _e in ("o", "aṃ", "a"):
        T10[f"{_p}sambojjhaṅg{_e}"] = f"{_h} नामक जागृति का अंग"
CHAPTER_T["10-bojjhangavibhango"] = T10
PP["10-bojjhangavibhango"] = {"2-483", "2-484", "2-485"}
OVR["10-bojjhangavibhango"] = {
    "2-484": {"uppannā": "उत्पन्न हो चुका",          # matrix label (as sample 2-152)
              "dhammā": NDE},                        # only inside vipākadhammadhammā «कर्म-फल उत्पन्न करने वाले»
}
T_ALL.update({
    # the cittuppāda opening (pi-1 wording: sahagataṃ = के साथ होना; sasaṅkhārena = प्रेरणा सहित)
    "sahagataṃ": "के साथ होना", "somanassasahagataṃ": "प्रसन्नता के साथ होना",
    "upekkhāsahagataṃ": "समभाव के साथ होना", "somanassa": "प्रसन्नता",
    "ñāṇa": "ज्ञान", "ñāṇasampayuttaṃ": "ज्ञान से जुड़ा", "ñāṇavippayuttaṃ": "ज्ञान से अलग",
    "sasaṅkhārena": "प्रेरणा सहित", "saṅkhārena": "प्रेरणा",
    "kusalaṃ cittaṃ": "हितकर मन", "uppannaṃ": "उत्पन्न", "paggāho": "तत्परता",
    "sañcetanā": "इरादा करना", "sañcetayitattaṃ": "इरादा कर चुका होना", "cetanāya": "इरादा",
    "chandādhipateyyaṃ": "चाह की प्रधानता वाला", "vīriyādhipateyyaṃ": "उत्साह की प्रधानता वाला",
    "cittādhipateyyaṃ": "मन की प्रधानता वाला", "vīmaṃsādhipateyyaṃ": "जाँच-परख की प्रधानता वाला",
    "ādhipateyyaṃ": "प्रधानता वाला", "hīnaṃ": "हीन", "majjhimaṃ": "मध्यम", "paṇītaṃ": "उत्तम",
    "kāmāvacare": "इंद्रिय-सुखों के लोक से संबंधित", "āvacare": "लोक से संबंधित",
    "rūpārammaṇaṃ": "विषय दृश्य रूप", "dhammārammaṇaṃ": "मन का विषय", "ārammaṇaṃ": "विषय",
    "yaṃ yaṃ vā panārabbha": "जिस किसी को भी … विषय बनाना",
    # rūpa-/arūpa-upapatti magga (pi-1 1-160)
    "maggaṃ": "मार्ग", "maggaṃ bhāveti": "मार्ग का अभ्यास करना", "ūpapattiyā": "जन्म", "upapattiyā": "जन्म",
    "ūpapattiyā maggaṃ": "जन्म की ओर ले जाने वाला मार्ग", "upapattiyā maggaṃ": "जन्म की ओर ले जाने वाला मार्ग",
    "rūpūpapattiyā": "सूक्ष्म भौतिक लोक में जन्म", "arūpūpapattiyā": "अभौतिक लोक में जन्म",
    # Pañhāpucchaka
    "āsekkhā": "सीखना पूरा होने के चरण का", "ācayagāmino": "संचय की ओर ले जाने वाला",
    "pītisahagatā": "उल्लास के साथ होने वाला",
    "parittā": "सीमित", "majjhimā": "मध्यम", "lokiyā": "लौकिक", "kusalāyeva": "केवल हितकर",
})

# ---------------------------------------------------------------- 14-sikkhapadavibhango
T14 = {
    "sikkhā": "प्रशिक्षण", "sikkhāpada": "प्रशिक्षण के नियम", "pada": "नियम",
    "sikkhāpadaṃ": "प्रशिक्षण-नियम", "sikkhāpadāni": "प्रशिक्षण-नियम", "sikkhāpadānaṃ": "प्रशिक्षण-नियम",
    "padaṃ": "नियम", "padāni": "नियम", "padānaṃ": "नियम",
    "veramaṇī sikkhāpadaṃ": "दूर रहने का प्रशिक्षण-नियम", "veramaṇī": "दूर रहना",
    "pāṇātipātā": "जीव-हत्या", "ātipātā": "हत्या", "pāṇātipātā veramaṇī": "जीव-हत्या से दूर रहना",
    "adinnādānā veramaṇī": "बिना दी गई चीज़ लेने से दूर रहना", "ādānā": "लेना",
    "kāmesumicchācārā veramaṇī": "इंद्रिय-सुखों में दुराचार से दूर रहना", "kāmesu": "इंद्रिय-सुख",
    "micchācārā": "दुराचार",
    "musāvādā veramaṇī": "झूठ बोलने से दूर रहना", "musāvādā": "झूठ बोलना", "musā": "झूठ", "vādā": "बोलना",
    "surāmerayamajjapamādaṭṭhānā veramaṇī":
        "लापरवाही का कारण बनने वाली शराब मदिरा और नशीली चीज़ों से दूर रहना",   # comma of the text dropped
    "surā": "शराब", "meraya": "मदिरा", "majja": "नशीली चीज़", "pamāda": "लापरवाही", "ṭṭhānā": "कारण बनने वाला",
    # the abstinence string (pi-1 1-299): ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti
    # velāanatikkamo setughāto
    "ārati": "दूर रहना", "virati": "विरत रहना", "paṭivirati": "पूरी तरह विरत रहना",
    "akiriyā": "न करना", "akaraṇaṃ": "न अपनाना", "anajjhāpatti": "दोष में न पड़ना",
    "velā": "मर्यादा", "anatikkamo": "उल्लंघन न करना", "setu": "पुल", "ghāto": "तोड़ देना",
    "dhammā sikkhā": "परिघटना प्रशिक्षण",
}
CHAPTER_T["14-sikkhapadavibhango"] = T14
PP["14-sikkhapadavibhango"] = {"2-715", "2-716", "2-717"}
OVR["14-sikkhapadavibhango"] = {
    "2-716": {"uppannā": "उत्पन्न हो चुका", "dhammā": NDE},
    "2-717": {"sahabhuno": "साथ-साथ होना"},           # text «मन के साथ-साथ होते हैं» (predicate)
}
# veramaṇī inside the abstinence string (segments with ārati) = बचना (pi-1); in the titles = दूर रहना
for _b in ("2-704", "2-706", "2-709", "2-710", "2-711"):
    OVR["14-sikkhapadavibhango"].setdefault(_b, {})["veramaṇī"] = "बचना"
ALLOWED["14-sikkhapadavibhango"] = {}

T_ALL.update({
    # the four jhāna formulas (pi-1 wording; the pi-2 Hindi «… के शांत होने से», «सुख को छोड़ने से»)
    "vitakka": "आरंभिक विचार", "vicārānaṃ": "सतत विचार",
    "vitakkavicārānaṃ": "आरंभिक विचार और सतत विचार", "vūpasamā": "शांत होना",
    "vitakkavicārānaṃ vūpasamā": "आरंभिक विचार और सतत विचार का शांत होना",
    "pītiyā": "उल्लास", "virāgā": "फीका पड़ना", "viveka": "अलगाव", "vivekajaṃ": "अलगाव से उत्पन्न",
    "sukhaṃ": "सुख", "pītisukhaṃ": "उल्लास और सुख वाला",
    "akusalehi": "हानिकर", "akusalehi dhammehi": "हानिकर परिघटना",
    "sukhassa": "सुख", "dukkhassa": "दुःख", "pahānā": "छोड़ना", "sukhassa ca pahānā": "सुख को छोड़ना",
    "dukkhassa ca pahānā": "दुःख को छोड़ना",
    "paṭhamaṃ jhānaṃ": "पहला ध्यान", "dutiyaṃ jhānaṃ": "दूसरा ध्यान", "tatiyaṃ jhānaṃ": "तीसरा ध्यान",
    "catutthaṃ jhānaṃ": "चौथा ध्यान",
    "rūpūpapattiyā maggaṃ": "सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाला मार्ग",
    "arūpūpapattiyā maggaṃ": "अभौतिक लोक में जन्म की ओर ले जाने वाला मार्ग",
    # kamma / vipāka / kiriya frames (pi-1)
    "upacitattā": "संचित होना", "kusalassa": "हितकर", "kusalassa kammassa": "हितकर कर्म",
    "rūpāvacarassa": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarassa": "अभौतिक लोक से संबंधित",
    "āvacarassa": "लोक से संबंधित", "kiriyaṃ": "केवल क्रिया रूपी", "diṭṭhadhamma": "इसी जीवन",
    "vihāraṃ": "रहना", "ākusalaṃ": "हानिकर", "neva kusalaṃ nākusalaṃ": "न हितकर न हानिकर",
    "nevavipākanavipākadhammadhammā": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "na hetu": "मूल रूपी न होने वाला",
    # the citta string (pi-1): cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ …
    "mānasaṃ": "मानसिक क्रिया", "hadayaṃ": "हृदय", "paṇḍaraṃ": "उज्ज्वलता", "manāyatanaṃ": "मन का इंद्रिय-क्षेत्र",
    "manindriyaṃ": "मन की क्षमता", "tajjā": "उसके अनुरूप",
    # sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ (SAHAGATA_TAIL)
    "jātaṃ": "उत्पन्न होना", "saṃsaṭṭhaṃ": "घुला-मिला", "sampayuttaṃ": "जुड़ा", "tena": "इसीलिए",
})

# ---------------------------------------------------------------- 13-appamannavibhango
APP = {"mettā": "मैत्री", "karuṇā": "करुणा", "muditā": "दूसरों के सुख पर प्रसन्नता", "upekkhā": "समभाव"}
T13 = {
    "appamaññā": "असीम भाव", "appamaññāyo": "असीम भाव", "appamaññānaṃ": "असीम भाव",
    "mettā": "मैत्री", "metti": "मैत्री", "karuṇā": "करुणा", "muditā": "दूसरों के सुख पर प्रसन्नता",
    "upekkhā": "समभाव",
    "mettāyanā": "मैत्री करना", "karuṇāyanā": "करुणा करना", "muditāyanā": "दूसरों के सुख पर प्रसन्न होना",
    "upekkhāyanā": "समभाव रखना",
    "ceto": "मन", "vimutti": "मुक्ति", "cetovimutti": "मन की मुक्ति", "cetasā": "मन",
    "sahagatena": "के साथ होने वाला", "mano": "मानस",
    # 2-642 / 2-699
    "ekaṃ disaṃ pharitvā": "एक दिशा को व्याप्त करके", "pharitvā": "व्याप्त करके", "disaṃ": "दिशा",
    "pharitvā viharati": "व्याप्त करके रहना", "tathā": "उसी तरह", "tathā catutthaṃ": "उसी तरह चौथी",
    "tiriyaṃ": "चारों ओर", "sabbadhi": "हर जगह", "sabbattatāya": "सबको अपने समान मानकर",
    "sabbāvantaṃ": "पूरा", "sabbāvantaṃ lokaṃ": "पूरा लोक", "sabbāvantaṃ loka": "पूरा लोक",
    "vipulena": "विशाल", "mahaggatena": "उन्नत", "appamāṇena": "अपरिमित", "averena": "वैर से रहित",
    "abyāpajjena": "दुर्भावना से रहित",
    # 2-643 …
    "puggalaṃ": "व्यक्ति", "piyaṃ": "प्रिय", "disvā": "देखकर", "pharati": "व्याप्त करना",
    "mettāyeyya": "मैत्री रखना", "karuṇāyeyya": "करुणा करना", "mudito": "प्रसन्न",
    "upekkhako": "समभाव रखना", "duggataṃ": "दुर्दशा में पड़ा", "durūpetaṃ": "दीन-हीन",
    "sattesu": "प्राणी",
    # 2-644 / 2-647
    "puratthimaṃ": "पूर्व", "puratthimaṃ vā disaṃ": "पूर्व दिशा", "pacchimaṃ vā disaṃ": "पश्चिम दिशा",
    "uttaraṃ": "उत्तर", "uttaraṃ vā disaṃ": "उत्तर दिशा", "dakkhiṇaṃ": "दक्षिण",
    "dakkhiṇaṃ vā disaṃ": "दक्षिण दिशा", "vidisaṃ": "बीच की दिशा", "catutthaṃ disaṃ": "चौथी दिशा",
    # 2-645 / 2-646 (VIHARATI_DEF)
    "adhimuccitvā": "मन को दृढ़ता से टिकाकर",
    "pharitvā adhimuccitvā": "व्याप्त करके उस पर मन को दृढ़ता से टिकाकर",
    "viharatī": "रहना", "iriyati": "चलना-फिरना", "vattati": "आचरण करना", "pāleti": "स्वयं को बनाए रखना",
    "yapeti": "निभाना", "yāpeti": "जीवन चलाना", "carati": "विचरना",
    # 2-648 (SABBENA)
    "sabbena sabbaṃ": "सब कुछ पूरी तरह", "sabbathā": "हर प्रकार से", "asesaṃ": "बिना कुछ बचाए",
    "nissesaṃ": "बिना कुछ छोड़े", "pariyādāya": "संपूर्णता को समेटने वाला", "vacana": "कथन",
    # 2-650
    "vipulaṃ": "विशाल", "mahaggataṃ": "उन्नत", "appamāṇaṃ": "अपरिमित", "avero": "वैर से रहित",
    "abyāpajjo": "दुर्भावना से रहित",
}
for _p, _h in APP.items():
    T13[f"{_p}sahagatena"] = T13[f"{_p}sahagataṃ"] = f"{_h} के साथ होने वाला"
    T13[f"{_p}sahagatena cetasā"] = f"{_h} के साथ होने वाला मन"
    T13[f"{_p}cetovimutti"] = f"{_h} द्वारा मन की मुक्ति"
    T13[f"{_p[:-1]}āyitattaṃ"] = f"{_h} से भरा होना"
for _p, _h in APP.items():                                  # X-sahagataṃ: pi-1 form «X के साथ होना»
    T13[f"{_p}sahagataṃ"] = f"{_h} के साथ होना"
CHAPTER_T["13-appamannavibhango"] = T13
PP["13-appamannavibhango"] = {"2-700", "2-701", "2-702"}
OVR["13-appamannavibhango"] = {
    "2-701": {"uppannā": "उत्पन्न हो चुका", "dhammā": NDE},   # dhammā only inside …dhammadhammā
}
for _b in ("2-643", "2-653", "2-663", "2-673"):               # «… व्याप्त करके कैसे रहता है?»
    OVR["13-appamannavibhango"][_b] = {"pharitvā viharati": "व्याप्त करके … रहना"}
ALLOWED["13-appamannavibhango"] = {}   # katattā «किए जाने»: covered by inflect_variant()

ALLOWED["10-bojjhangavibhango"] = {}   # cirakatampi / katattā / bhāvitattā «किए»: covered by inflect_variant()


def inflect_variant(value, text):
    """The checker (pi-1 present()) does not model the perfective participle in -िया ~ -िए (किया/किए,
    दिया/दिए, लिया/लिए) or सा ~ से. Returns a reason when such a variant of value occurs in text."""
    import re
    from map_sample_hi import present
    alt = re.sub(r"िया(?=\s|$)", "िए", value)
    alt2 = re.sub(r"-सा(?=\s|$)", "-से", alt)
    for a, why in ((alt, "किया ~ किए"), (alt2, "किया ~ किए / सा ~ से")):
        if a != value and present(a, text):
            return f"text has «{a}»: {why} is regular inflection the checker does not model"
    return None


def resolve(ch, bid, kw, kws, text=None):
    o = OVR.get(ch, {}).get(bid, {})
    if kw in o:
        return o[kw]
    if ch == "12-jhanavibhango" and kw == "mano" and text is not None:
        # citta string «मन, मानस, मानसिक क्रिया…» = मानस (pi-1); manopadoso / manovilekhā = मन
        return "मानस" if "मानस," in text else "मन"
    PP_SEGMENTS.update(PP.get(ch, ()))
    return pi2_value(kw, kws, {**PI2, **T_ALL, **CHAPTER_T.get(ch, {})}, bid, text)

# ---------------------------------------------------------------- 12-jhanavibhango (table in its own file)
import importlib as _il  # noqa: E402
_t12 = _il.import_module("table_12-jhanavibhango_hi")
T12 = dict(_t12.T12)
for _k in ("iriyati", "vattati", "pāleti", "yapeti", "yāpeti", "carati", "viharatī",   # VIHARATI_DEF (as ch13)
           "sabbena sabbaṃ", "sabbathā", "asesaṃ", "nissesaṃ"):                         # SABBENA (as ch13)
    T12.setdefault(_k, T13[_k])
for _k, _v in T10.items():                                   # bojjhaṅga names (2-522), as ch10
    if "bojjhaṅg" in _k or _k in ("vicaya", "dhammavicaya"):
        T12.setdefault(_k, _v)
CHAPTER_T["12-jhanavibhango"] = T12
OVR["12-jhanavibhango"] = _t12.OVR12
ALLOWED["12-jhanavibhango"] = _t12.ALLOWED12
PP["12-jhanavibhango"] = getattr(_t12, "PP12", set())
