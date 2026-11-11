"""Builds the Hindi rails chapters 2-01 and 2-02 of pi-1 (Dhammasaṅgaṇī, plain audience).

Each Pāli line is parsed with strict rules and rendered from fixed strings, so identical Pāli gives identical
Hindi; a line that no rule covers stops the build. 2-01 begins with the approved sample (^1-1 to ^1-57) unchanged.
Writes the two chapters and notes-2-01_2-02.md.

usage: python -I -X utf8 build_rails_2-01_2-02.py
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
RAILS_DIR = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample as sm  # noqa: E402

PALI, OUT = sm.PALI, sm.OUT
CH1, CH2 = "2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md"

# ------------------------------------------------------------------ names
F = dict(sm.F)
F.update({
    "upekkhā": ("समभाव", "m"),
    "upekkhindriyaṃ": ("समभाव की क्षमता", "f"),
    "vedanākkhandho": ("अनुभूति का समूह", "m"),
    "saññākkhandho": ("पहचान का समूह", "m"),
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", "m"),
    "viññāṇakkhandho": ("चेतना का समूह", "m"),
    "manāyatanaṃ": ("मन का इंद्रिय-क्षेत्र", "m"),
    "dhammāyatanaṃ": ("मन के विषयों का इंद्रिय-क्षेत्र", "m"),
    "manoviññāṇadhātu": ("मन की चेतना का तत्व", "m"),
    "dhammadhātu": ("मन के विषयों का तत्व", "m"),
    "phassāhāro": ("संपर्क रूपी आहार", "m"),
    "manosañcetanāhāro": ("मानसिक इरादा रूपी आहार", "m"),
    "viññāṇāhāro": ("चेतना रूपी आहार", "m"),
    "jhānaṃ": ("ध्यान", "m"),
    "maggo": ("मार्ग", "m"),
    "pañcaṅgikaṃ jhānaṃ": ("पाँच अंगों वाला ध्यान", "m"),
    "caturaṅgikaṃ jhānaṃ": ("चार अंगों वाला ध्यान", "m"),
    "tivaṅgikaṃ jhānaṃ": ("तीन अंगों वाला ध्यान", "m"),
    "duvaṅgikaṃ jhānaṃ": ("दो अंगों वाला ध्यान", "m"),
    "pañcaṅgiko maggo": ("पाँच अंगों वाला मार्ग", "m"),
    "caturaṅgiko maggo": ("चार अंगों वाला मार्ग", "m"),
})
PLURAL = {
    "cattāro khandhā": ("चार समूह", "m"),
    "dvāyatanāni": ("दो इंद्रिय-क्षेत्र", "m"),
    "dve dhātuyo": ("दो तत्व", "m"),
    "tayo āhārā": ("तीन आहार", "m"),
    "aṭṭhindriyāni": ("आठ क्षमताएँ", "f"),
    "sattindriyāni": ("सात क्षमताएँ", "f"),
    "satta balāni": ("सात बल", "m"),
    "cha balāni": ("छह बल", "m"),
    "tayo hetū": ("तीन मूल", "m"),
    "dve hetū": ("दो मूल", "m"),
    "dhammā": ("परिघटनाएँ", "f"),
    "khandhā": ("समूह", "m"),
    "āyatanāni": ("इंद्रिय-क्षेत्र", "m"),
    "dhātuyo": ("तत्व", "m"),
    "āhārā": ("आहार", "m"),
    "indriyāni": ("क्षमताएँ", "f"),
    "balāni": ("बल", "m"),
    "hetū": ("मूल", "m"),
}


def low(n):
    return n[0].lower() + n[1:]


def name(n):
    """Returns (Hindi, gender, is_plural) for a Pāli nominative."""
    n = low(n)
    if n in PLURAL:
        return (*PLURAL[n], True)
    m = re.fullmatch(r"(eko|ekā|ekaṃ) (.+)", n)
    if m:
        h, g = F[m.group(2)]
        return (f"एक {h}", g, False)
    h, g = F[n]
    return (h, g, False)


def be(g, plural):
    if plural:
        return "होते हैं" if g == "m" else "होती हैं"
    return "होता है" if g == "m" else "होती है"


def question(n):
    h, g, pl = name(n)
    if pl:
        return f"उस समय {h} कौन-से होते हैं" if g == "m" else f"उस समय {h} कौन-सी होती हैं"
    return f"उस समय {h} क्या {'होता' if g == 'm' else 'होती'} है"


def statement(pron, n):
    h, g, pl = name(n)
    return f"{'ये' if pron in ('ime', 'imāni', 'imā') else 'यह'} उस समय {h} {be(g, pl)}"


# ------------------------------------------------------------------ fixed strings
CO = sm.CLOSE_OTHERS
CK = sm.CLOSE_KUSALA
OTHERS_PALI = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
UPEKKHA_TAIL = ("न मानसिक सुहावनापन, न मानसिक असुहावनापन, मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभव, "
                "मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभूति")
SP = sm.S
J_PLAIN = SP["jīvita_var"].replace(" [वर्तनी-भेद (Sī.): irīyanā]", "")
BODY = {
    "phasso phusanā saṃphusanā saṃphusitattaṃ": SP["phasso"],
    "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā": SP["sukhaṃ"],
    "saññā sañjānanā sañjānitattaṃ": "पहचान, पहचानना, पहचान चुका होना",
    "cetanā sañcetanā cetayitattaṃ": "इरादा, इरादा करना, इरादा कर चुका होना",
    "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu": SP["cittaṃ"],
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo": SP["vitakko"],
    "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā": SP["vicāro"],
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa": SP["pīti"],
    "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ sammāsamādhi": SP["samādhi"],
    "saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ": SP["saddhā"],
    "cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo": SP["vīriya_plain"],
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati": SP["sati"],
    "paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo sammādiṭṭhi": SP["paññā"],
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": "प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि",
    "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ": SP["alobho"],
    "adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ": SP["adoso_plain"],
    "āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ": J_PLAIN,
    "tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā": f"{sm.TAJJA} {UPEKKHA_TAIL}",
    "cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā": UPEKKHA_TAIL,
}
NOJO = {
    "hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": sm.HIRI,
    "ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": sm.OTT,
}
TAILS = {
    ".": "।",
    "?": "?",
    "…pe….": "…।",
    "…pe… ime dhammā kusalā.": f"… {CK}।",
    f"…pe… {OTHERS_PALI} – ime dhammā kusalā…pe….": f"… {CO} – {CK}…।",
}

OPEN_RUPA = "सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग"
OPEN_ARUPA = "अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग"
ABIDE = "प्राप्त करके उसमें रहता है"
ITI = "“उन पर विजय पाकर मैं जानता हूँ, देखता हूँ” इस भाव के साथ, "
ORD = {"paṭhamaṃ": "पहले", "dutiyaṃ": "दूसरे", "tatiyaṃ": "तीसरे", "catutthaṃ": "चौथे", "pañcamaṃ": "पाँचवें"}

# Attributes of the absorption, and the openers left standing before a "…pe…"
JHANA_ATTR = {
    "vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ":
        "इंद्रिय-सुखों से अलग होकर, हानिकर परिघटनाओं से अलग होकर, आरंभिक विचार और सतत विचार वाले, अलगाव से उत्पन्न उल्लास और सुख वाले",
    "vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ":
        "आरंभिक विचार और सतत विचार के शांत होने से, स्वयं में निर्मलता वाले, मन के एक बिंदु पर टिकने वाले, आरंभिक विचार और सतत विचार से रहित, एकाग्रता से उत्पन्न उल्लास और सुख वाले",
    "pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti – \"upekkhako satimā sukhavihārī\"ti":
        "उल्लास के फीका पड़ने से वह समभाव के साथ, सजग और स्पष्ट समझ रखते हुए रहता है और शरीर से सुख का अनुभव करता है, जिसके बारे में आर्य कहते हैं – “समभाव वाला, सजगता वाला, सुख से रहने वाला”, ऐसे",
    "sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ upekkhāsatipārisuddhiṃ":
        "सुख को छोड़ने से और दुःख को छोड़ने से, और पहले ही प्रसन्नता और उदासी के मिट जाने से, न दुःखद, न सुखद, समभाव और सजगता से पूरी तरह शुद्ध",
    "avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ":
        "आरंभिक विचार से रहित, केवल सतत विचार वाले, एकाग्रता से उत्पन्न उल्लास और सुख वाले",
}
OPENER = {
    "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर",
    "vitakkavicārānaṃ vūpasamā": "आरंभिक विचार और सतत विचार के शांत होने से",
    "pītiyā ca virāgā": "उल्लास के फीका पड़ने से",
    "sukhassa ca pahānā": "सुख को छोड़ने से",
}

KASINA = {
    "pathavīkasiṇaṃ": "पृथ्वी के ध्यान-मंडल वाला", "āpokasiṇaṃ": "जल के ध्यान-मंडल वाला",
    "tejokasiṇaṃ": "अग्नि के ध्यान-मंडल वाला", "vāyokasiṇaṃ": "वायु के ध्यान-मंडल वाला",
    "nīlakasiṇaṃ": "नीले ध्यान-मंडल वाला", "pītakasiṇaṃ": "पीले ध्यान-मंडल वाला",
    "lohitakasiṇaṃ": "लाल ध्यान-मंडल वाला", "odātakasiṇaṃ": "सफ़ेद ध्यान-मंडल वाला",
}
CORPSE = {
    "uddhumātaka": "फूली हुई लाश", "vinīlaka": "नीली पड़ चुकी लाश", "vipubbaka": "पीप से भरी लाश",
    "vicchiddaka": "बीच से कटी लाश", "vikkhāyitaka": "जानवरों द्वारा नोची गई लाश", "vikkhittaka": "बिखरी हुई लाश",
    "hatavikkhittaka": "काटकर बिखरी हुई लाश", "lohitaka": "खून से सनी लाश", "puḷavaka": "कीड़ों से भरी लाश",
    "aṭṭhika": "कंकाल",
}
QUAL = {
    "dukkhapaṭipadaṃ": "दुःखद प्रगति वाला", "sukhapaṭipadaṃ": "सुखद प्रगति वाला",
    "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला", "khippābhiññaṃ": "शीघ्र उच्च ज्ञान वाला",
    "parittaṃ": "सीमित", "appamāṇaṃ": "अपरिमित",
    "parittārammaṇaṃ": "सीमित विषय वाला", "appamāṇārammaṇaṃ": "अपरिमित विषय वाला",
    "mettāsahagataṃ": "मैत्री के साथ होने वाला", "karuṇāsahagataṃ": "करुणा के साथ होने वाला",
    "muditāsahagataṃ": "दूसरों के सुख पर प्रसन्नता के साथ होने वाला", "upekkhāsahagataṃ": "समभाव के साथ होने वाला",
    "somanassasahagataṃ": "प्रसन्नता के साथ होने वाला",
    "ñāṇasampayuttaṃ": "ज्ञान से जुड़ा", "ñāṇavippayuttaṃ": "ज्ञान से अलग", "sasaṅkhārena": "प्रेरणा सहित",
    "hīnaṃ": "हीन", "majjhimaṃ": "मध्यम", "paṇītaṃ": "उत्तम",
    "chandādhipateyyaṃ": "चाह की प्रधानता वाला", "vīriyādhipateyyaṃ": "उत्साह की प्रधानता वाला",
    "cittādhipateyyaṃ": "मन की प्रधानता वाला", "vīmaṃsādhipateyyaṃ": "जाँच-परख की प्रधानता वाला",
}
QUAL.update(KASINA)
QUAL.update({f"{k}saññāsahagataṃ": f"{v} की पहचान के साथ होने वाला" for k, v in CORPSE.items()})
LEVELS = ("हीन", "मध्यम", "उत्तम")

COLOUR = {
    "nīl": ("नीले", "नीली"), "pīt": ("पीले", "पीली"), "lohitak": ("लाल", "लाल"), "odāt": ("सफ़ेद", "सफ़ेद"),
}
AK = "स्वयं में भौतिक रूप की पहचान न रखते हुए"
SEE = "दृश्य रूपों को देखता है"
SIZE = {
    "parittāni": "सीमित", "appamāṇāni": "अपरिमित",
    "parittāni suvaṇṇadubbaṇṇāni": "सीमित, सुंदर और कुरूप",
    "appamāṇāni suvaṇṇadubbaṇṇāni": "अपरिमित, सुंदर और कुरूप",
}
SP1 = "भौतिक रूप की पहचानों को पूरी तरह पार कर जाने से, टकराव की पहचानों के मिट जाने से, विविधता की पहचानों पर मनोयोग न करने से"
A1, A2, A3, A4 = ("अनंत आकाश के क्षेत्र", "अनंत चेतना के क्षेत्र", "कुछ भी न होने के क्षेत्र", "न पहचान, न अ-पहचान के क्षेत्र")
ARUPA = {
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā ākāsānañcāyatanasaññāsahagataṃ ": (SP1, A1),
    "sabbaso ākāsānañcāyatanaṃ samatikkamma viññāṇañcāyatanasaññāsahagataṃ ": (f"{A1} को पूरी तरह पार करके", A2),
    "sabbaso viññāṇañcāyatanaṃ samatikkamma ākiñcaññāyatanasaññāsahagataṃ ": (f"{A2} को पूरी तरह पार करके", A3),
    "sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ ": (f"{A3} को पूरी तरह पार करके", A4),
}

TITLES = {
    "Koṭṭhāsavāro": "भागों का खंड",
    "Suññatavāro": "शून्यता का खंड",
    "Paṭhamaṃ cittaṃ": "पहला मन", "Dutiyaṃ cittaṃ": "दूसरा मन", "Tatiyaṃ cittaṃ": "तीसरा मन",
    "Catutthaṃ cittaṃ": "चौथा मन", "Pañcamaṃ cittaṃ": "पाँचवाँ मन", "Chaṭṭhaṃ cittaṃ": "छठा मन",
    "Sattamaṃ cittaṃ": "सातवाँ मन", "Aṭṭhamaṃ cittaṃ": "आठवाँ मन",
    "Aṭṭha kāmāvacaramahākusalacittāni": "इंद्रिय-सुखों के लोक से संबंधित आठ बड़े हितकर मन",
    "Dutiyabhāṇavāro": "दूसरा पाठ-खंड",
    "Kāmāvacarakusalaṃ": "इंद्रिय-सुखों के लोक से संबंधित हितकर मन",
    "Rūpāvacarakusalaṃ": "सूक्ष्म भौतिक लोक से संबंधित हितकर मन",
    "Arūpāvacarakusalaṃ": "अभौतिक लोक से संबंधित हितकर मन",
    "Tebhūmakakusalaṃ": "तीनों लोकों से संबंधित हितकर मन",
    "Catukkanayo": "चार-चार की विधि",
    "Pañcakanayo": "पाँच-पाँच की विधि",
    "Catasso paṭipadā": "प्रगति के चार ढंग",
    "Cattāri ārammaṇāni": "चार विषय",
    "Dve ārammaṇāni": "दो विषय",
    "Soḷasakkhattukaṃ": "सोलह गुना",
    "Aṭṭhakkhattukaṃ": "आठ गुना",
    "Idampi aṭṭhakkhattukaṃ": "यह भी आठ गुना",
    "Aparampi aṭṭhakkhattukaṃ": "एक और आठ गुना",
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": "आठ ध्यान-मंडल, सोलह गुना",
    "Abhibhāyatanāni parittāni": "विजय के सीमित आधार",
    "Appamāṇāni": "अपरिमित",
    "Imānipi abhibhāyatanāni soḷasakkhattukāni": "ये विजय के आधार भी सोलह गुना हैं",
    "Tīṇi vimokkhāni soḷasakkhattukāni": "तीन मुक्ति-अवस्थाएँ, सोलह गुना",
    "Imānipi tīṇi vimokkhāni soḷasakkhattukāni": "ये तीन मुक्ति-अवस्थाएँ भी सोलह गुना हैं",
    "Cattāri brahmavihārajhānāni soḷasakkhattukāni": "ब्रह्म-विहार के चार ध्यान, सोलह गुना",
    "Cattāri brahmavihārajhānāni [brahmavihārajjhānāni (sī. syā.)] soḷasakkhattukāni":
        "ब्रह्म-विहार के चार ध्यान [वर्तनी-भेद (Sī., Syā.): brahmavihārajjhānāni], सोलह गुना",
    "Asubhajhānaṃ soḷasakkhattukaṃ": "असुंदरता का ध्यान, सोलह गुना",
    "Asubhajhānaṃ [asubhajjhānaṃ (sī. syā.)] soḷasakkhattukaṃ": "असुंदरता का ध्यान [वर्तनी-भेद (Sī., Syā.): asubhajjhānaṃ], सोलह गुना",
    "Cattāri arūpajhānāni soḷasakkhattukāni": "अभौतिक लोक के चार ध्यान, सोलह गुना",
    "Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni": "अभौतिक लोक के चार ध्यान [वर्तनी-भेद (Sī., Syā.): arūpajjhānāni], सोलह गुना",
}


# ------------------------------------------------------------------ helpers
def sigla(s):
    if s == "bahūsu":
        return "Bahūsu"
    return ", ".join(p.capitalize() for p in s.split())


def variant(b):
    m = re.fullmatch(r"\[(\S+) \((.+)\)\]", b)
    return f"[वर्तनी-भेद ({sigla(m.group(2))}): {m.group(1)}]"


def chain(items):
    if len(items) >= 2 and items[-1] in LEVELS and items[-2].endswith("की प्रधानता वाला"):
        items = items[:-2] + [f"{items[-2]} {items[-1]}"]
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " और " + items[-1]


def qual_piece(piece, first_extra=None):
    items = [first_extra] if first_extra else []
    for tok in re.findall(r"[^\s\[]+(?: \[[^\]]*\])?", piece):
        word, _, br = tok.partition(" ")
        items.append(QUAL[word] + (" " + variant(br) if br else ""))
    return chain(items)


def quals(text, first_extra=None):
    """Adjective chain, one chain per stretch between "…pe…"."""
    pieces = text.split("…pe…") if text else [""]
    out = []
    for i, p in enumerate(pieces):
        out.append(qual_piece(p.strip(), first_extra if i == 0 else None))
    return "… ".join(out)


def hoti_list(s):
    s = re.sub(r" (hoti|honti) (?=\w)", r" \1, ", s)
    parts = re.split(r"(, |…pe… )", s)
    out = []
    for p in parts:
        if p == ", ":
            out.append(", ")
        elif p == "…pe… ":
            out.append("… ")
        else:
            m = re.fullmatch(r"(.+) (hoti|honti)", p)
            h, g, pl = name(m.group(1))
            out.append(f"{h} {be(g, pl)}")
    return "".join(out)


def facts(s):
    """Text after 'tasmiṃ samaye' or 'kho pana samaye': the factor list and its close."""
    m = re.fullmatch(rf"(.*); {OTHERS_PALI} – ime dhammā kusalā(\.|…pe….)", s)
    if m:
        return f"{hoti_list(m.group(1))}; {CO} – {CK}{'।' if m.group(2) == '.' else '…।'}"
    m = re.fullmatch(r"(.*)…pe… ime dhammā kusalā(\.|…pe….)", s)
    return f"{hoti_list(m.group(1))}… {CK}{'।' if m.group(2) == '.' else '…।'}"


def jhana(mid):
    """'vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ' and the longer forms, ending just before 'prāpta karke'."""
    out = []
    for p in (x.strip() for x in mid.split("…pe…")):
        if p in OPENER:
            out.append(OPENER[p])
            continue
        m = re.fullmatch(r"(?:(.*) )?(paṭhamaṃ|dutiyaṃ|tatiyaṃ|catutthaṃ|pañcamaṃ) jhānaṃ( \[.*\])?", p)
        attr = JHANA_ATTR[m.group(1)] + " " if m.group(1) else ""
        br = " " + variant(m.group(3).strip()) if m.group(3) else ""
        out.append(f"{attr}{ORD[m.group(2)]} ध्यान{br} को")
    return "… ".join(out)


def colours(text):
    out = []
    for p in (x.strip() for x in text.split("…pe…")):
        m = re.fullmatch(r"(\w+?)āni \1avaṇṇāni \1anidassanāni \1anibhāsāni", p)
        pl, fm = COLOUR[m.group(1)]
        out.append(f"{pl}, {pl} रंग वाले, {pl} दिखने वाले, {fm} आभा वाले")
    return "… ".join(out)


def rupa_prefix(mid):
    """Splits what comes before the absorption formula. Returns (seeing clause, thought phrase, jhāna text, extra adj)."""
    m = re.match(r"ajjhattaṃ arūpasaññī bahiddhā rūpāni passati (.*?),? tāni abhibhuyya jānāmi passāmīti (.*)$", mid)
    if m:
        size = SIZE[m.group(1)] if m.group(1) in SIZE else colours(m.group(1))
        return f"{AK} बाहर {size} {SEE}", ITI, m.group(2), None
    m = re.match(r"ajjhattaṃ arūpasaññī bahiddhā rūpāni passati (.*)$", mid)
    if m:
        return f"{AK} बाहर {SEE}", "", m.group(1), None
    m = re.match(r"rūpī rūpāni passati (.*)$", mid)
    if m:
        return f"भौतिक रूप वाला होकर {SEE}", "", m.group(1), None
    m = re.match(r"subhanti (.*)$", mid)
    if m:
        return "", "“सुंदर” इस भाव के साथ, ", m.group(1), None
    for k, (means, a) in ARUPA.items():
        if mid.startswith(k):
            return "", f"{means}, ", mid[len(k):], f"{a} की पहचान के साथ होने वाला"
    return "", "", mid, None


def path_formula(sphere, s):
    """Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti … tasmiṃ samaye …"""
    m = re.fullmatch(r"(.*?) upasampajja viharati ?(.*?)(, | – | )tasmiṃ samaye (.*)", s)
    mid, qual, sep, rest = m.groups()
    see, thought, jh, extra = rupa_prefix(mid)
    head = f"जिस समय कोई {sphere} का अभ्यास करता है"
    head += f", {see} और " if see else ", "
    jh_hi = jhana(jh)
    tail = ""
    if qual or extra:
        tail = f", जो {quals(qual, extra)} है"
    return f"{sm.Q_KUSALA} {head}{thought}{jh_hi} {ABIDE}{tail}{sep if sep == ' – ' else ', '}उस समय {facts(rest)}"


KAMA = "जिस समय इंद्रिय-सुखों के लोक से संबंधित हितकर मन उत्पन्न होता है"
OBJ_FULL = "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"
OBJ_SHORT = "rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"
OBJ_HI = {
    OBJ_FULL: "दृश्य रूप हो, या ध्वनि, या गंध, या स्वाद, या स्पर्श, या मन का विषय, या जिस किसी को भी वह विषय बनाए",
    OBJ_SHORT: "दृश्य रूप हो… या मन का विषय, या जिस किसी को भी वह विषय बनाए",
}


def kama_formula(s):
    m = re.fullmatch(r"(.*?)(?:,)? tasmiṃ samaye (.*)", s)
    left, rest = m.groups()
    for obj, hi in OBJ_HI.items():
        if left.endswith(" " + obj):
            q = left[: -len(obj) - 1]
            return f"{sm.Q_KUSALA} {KAMA}, जो {quals(q)} होता है और जिसका विषय {hi}, उस समय {facts(rest)}"
    return f"{sm.Q_KUSALA} {KAMA}, जो {quals(left)} होता है, उस समय {facts(rest)}"


def sankhara_list(s):
    s = s.replace("…pe…", " …pe… ")
    out = ""
    for tok in s.split():
        if tok == "…pe…":
            out = out.rstrip(", ") + "… "
        else:
            out += name(tok)[0] + ", "
    return out.rstrip(", ")


def others_except(s):
    m = re.fullmatch(r"ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā( \[thapetvā \(ka\.\)\])? vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ", s)
    br = " " + variant("[thapetvā (ka.)]") if m.group(1) else ""
    return f"{CO}, अनुभूति के समूह को छोड़कर{br}, पहचान के समूह को छोड़कर और चेतना के समूह को छोड़कर"


def definition(b):
    if b.startswith("Yo tesaṃ arūpīnaṃ dhammānaṃ "):
        return f"उन अभौतिक परिघटनाओं की जो {BODY[b[len('Yo tesaṃ arūpīnaṃ dhammānaṃ '):]]} है"
    m = re.fullmatch(r"(?:Yo|Yā|Yaṃ) tasmiṃ samaye (.*)", b)
    if m:
        t = m.group(1)
        if t in NOJO:
            return f"उस समय {NOJO[t]}"
        return f"उस समय जो {BODY[t]} है"
    if b.startswith("Phasso cetanā"):
        first, _, second = b.partition("; ")
        return f"{sankhara_list(first)}; {others_except(second)}"
    return ", ".join(name(x)[0] for x in re.split(r",? ", b))


def tr(line):
    head = re.match(r"#+ ", line)
    if head:
        return head.group(0) + TITLES[line[head.end():]]
    if line.endswith(".") and line[:-1] in TITLES:
        return TITLES[line[:-1]] + "।"
    m = re.fullmatch(r"Katame dhammā kusalā\? Yasmiṃ samaye (rūpūpapattiyā|arūpūpapattiyā) maggaṃ bhāveti (.*)", line)
    if m:
        return path_formula(OPEN_RUPA if m.group(1) == "rūpūpapattiyā" else OPEN_ARUPA, m.group(2))
    m = re.fullmatch(r"Katame dhammā kusalā\? Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti (.*)", line)
    if m:
        return kama_formula(m.group(1))
    m = re.fullmatch(r"Tasmiṃ kho pana samaye (.*)", line)
    if m:
        return f"और उस समय {facts(m.group(1))}"
    m = re.fullmatch(r"(Ime|Imāni|Imā|Idaṃ|Ayaṃ) tasmiṃ samaye (.+) (?:hoti|honti)\.", line)
    if m:
        return statement(m.group(1).lower(), m.group(2)) + "।"
    if line == f"Y{OTHERS_PALI[1:]} – ime dhammā kusalā.":
        return f"{CO} – {CK}।"
    m = re.fullmatch(rf"(Y{OTHERS_PALI[1:]} ṭhapetvā.*?) – (ayaṃ|idaṃ) tasmiṃ samaye (.+?) hoti(.*)", line)
    if m:
        return f"{others_except(low(m.group(1)))} – {statement(m.group(2), m.group(3))}{TAILS[m.group(4)]}"
    m = re.fullmatch(r"Katam\w+ tasmiṃ samaye (.+?) (?:hoti|honti)(\?|…pe…) ?(.*)", line)
    if not m:
        raise ValueError("no rule: " + line[:120])
    n, mark, rest = m.groups()
    q = question(n)
    c = re.fullmatch(r"(.*?)(?: – )?(ayaṃ|idaṃ|ime|imāni|imā) tasmiṃ samaye (.+?) (?:hoti|honti)(.*)", rest)
    if mark == "…pe…":
        return f"{q}… {statement(c.group(2), c.group(3))}{TAILS[c.group(4)]}"
    if c is None:
        return f"{q}? {definition(rest[:-1]) if rest.startswith('Phasso') is False else sankhara_list(rest[:-1])}।"
    return f"{q}? {definition(c.group(1))} – {statement(c.group(2), c.group(3))}{TAILS[c.group(4)]}"


def strip_id(sid, line):
    return re.sub(rf" \^{re.escape(sid)}\s*$", "", line)


def build(path, skip=()):
    out = {}
    for sid, lines in sm.segments(path):
        if sid in skip:
            continue
        lines = list(lines)
        lines[-1] = strip_id(sid, lines[-1])
        out[sid] = [tr(l.replace(" …pe…", "…pe…")) for l in lines]
    return out


def check_no_pali(hindi):
    """Only the Pāli inside variant brackets may stay in Roman letters."""
    for sid, lines in hindi.items():
        for l in lines:
            clean = re.sub(r"\[[^\]]*\]", "", l)
            assert not re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", clean), (sid, clean[:100])


NOTES_HEAD = """# Notes for chapters 2-01 and 2-02 (Hindi rails, pi-1)

Formulas fixed here for the rest of chapter 2. Format: Pāli = Hindi. Strings are generated by build_rails_2-01_2-02.py.

"""
NOTES_TAIL = """
## Termbase misfits

- paṭigha (only sense: aversion, चिढ़), in paṭighasaññānaṃ, ^1-265, ^1-273: the arūpa formula means perception of sensory impact, not aversion. Wrote «टकराव की पहचान», from the sibling entries sappaṭigha/appaṭigha (टकराव).
- mahā-, in kāmāvacaramahākusalacittāni, ^1-159: no entry. Wrote «बड़े हितकर मन», from mahāvipākā (बड़ा कर्म-फल).
- sātaṃ, the noun use in cetasikaṃ neva sātaṃ nāsātaṃ, ^1-152: the sample has «मानसिक सुहावनापन»; wrote «न मानसिक सुहावनापन, न मानसिक असुहावनापन».

## Compounds built from members (no own entry)

ākāsānañcāyatana «अनंत आकाश का क्षेत्र» (as pi-5); nevasaññānāsaññāyatana «न पहचान, न अ-पहचान का क्षेत्र» (pi-5, with the binding comma); ākiñcaññāyatana «कुछ भी न होने का क्षेत्र»; hatavikkhittaka «काटकर बिखरी हुई लाश»; tebhūmaka «तीनों लोकों से संबंधित»; brahmavihāra «ब्रह्म-विहार»; satimā «सजगता वाला»; sasaṅkhārena «प्रेरणा सहित» (from sasaṅkhārikesu); phassāhāro etc. «X रूपी आहार».

## Source slips (kept as in the Pāli)

- ^1-135 ends with «?» after a statement (kept, as ^1-33 in the sample).
- ^1-150, ^1-165: a comma is missing in the factor list (Hindi has it).
- ^1-189: no comma before tasmiṃ samaye (Hindi has it).
- ^1-259, ^1-261: the -pe- run gives dutiyaṃ, tatiyaṃ, paṭhamaṃ, catutthaṃ, in that odd order (kept).
- ^1-204: no comma before tāni, unlike ^1-205 and the rest (same Hindi).
"""


def write_notes():
    fm = [
        f"Tasmiṃ kho pana samaye = और उस समय",
        f"Katame tasmiṃ samaye cattāro khandhā honti? = {question('cattāro khandhā')}?",
        f"Katamāni tasmiṃ samaye aṭṭhindriyāni honti? = {question('aṭṭhindriyāni')}?",
        f"Ime tasmiṃ samaye cattāro khandhā honti. = {statement('ime', 'cattāro khandhā')}।",
        f"Katamo tasmiṃ samaye phasso hoti…pe… ayaṃ tasmiṃ samaye phasso hoti. = {question('phasso')}… {statement('ayaṃ', 'phasso')}।",
        f"ime dhammā kusalā…pe…. = {CK}…।",
        f"{OTHERS_PALI} ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ = {others_except(OTHERS_PALI + ' ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ')}",
        f"Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho = अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह",
        f"cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā = {UPEKKHA_TAIL}",
        f"tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ neva sātaṃ … vedanā = {sm.TAJJA} {UPEKKHA_TAIL}",
        f"saññā sañjānanā sañjānitattaṃ = {BODY['saññā sañjānanā sañjānitattaṃ']}",
        f"cetanā sañcetanā cetayitattaṃ = {BODY['cetanā sañcetanā cetayitattaṃ']}",
        f"Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti Q1 Q2 Q3 rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha, = {KAMA}, जो Q1, Q2 और Q3 होता है और जिसका विषय {OBJ_HI[OBJ_SHORT]},",
        f"Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti Q… (no object list) = {KAMA}, जो Q… होता है,",
        "Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti = जिस समय कोई सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है, (a following clause with its own verb, as in passati, closes with «और»)",
        "Yasmiṃ samaye arūpūpapattiyā maggaṃ bhāveti = जिस समय कोई अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है,",
        "(frame) … jhānaṃ upasampajja viharati Q, tasmiṃ samaye = … ध्यान को प्राप्त करके उसमें रहता है, जो Q है, उस समय (Q = adjectives joined with commas and a final «और», one chain per stretch between «…»; a dash in the Pāli before tasmiṃ samaye stays: … जो Q है – उस समय)",
        "(chain) A B C D = A, B, C और D; X-adhipateyyaṃ hīnaṃ = X की प्रधानता वाला हीन",
    ]
    fm += [f"{k} = {v}" for k, v in JHANA_ATTR.items()]
    fm += [f"{k} … = {v} …" for k, v in OPENER.items()]
    fm += [f"{k} jhānaṃ (+ upasampajja viharati) = {v} ध्यान को (प्राप्त करके उसमें रहता है)" for k, v in ORD.items()]
    fm += [f"[paṭhamajjhānaṃ (sī.)] after paṭhamaṃ jhānaṃ = पहले ध्यान [वर्तनी-भेद (Sī.): paṭhamajjhānaṃ] को"]
    fm += [f"{k} = {v}" for k, v in QUAL.items()]
    fm += [
        f"ajjhattaṃ arūpasaññī bahiddhā rūpāni passati parittāni, tāni abhibhuyya jānāmi passāmīti = {AK} बाहर सीमित {SEE} और {ITI.rstrip(', ')},",
        f"… appamāṇāni … = {AK} बाहर अपरिमित {SEE} और {ITI.rstrip(', ')},",
        f"parittāni suvaṇṇadubbaṇṇāni = {SIZE['parittāni suvaṇṇadubbaṇṇāni']} ({SEE})",
        f"nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni = {colours('nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni')} ({SEE})",
        f"pītāni pītavaṇṇāni pītanidassanāni pītanibhāsāni = {colours('pītāni pītavaṇṇāni pītanidassanāni pītanibhāsāni')}",
        f"lohitakāni lohitakavaṇṇāni lohitakanidassanāni lohitakanibhāsāni = {colours('lohitakāni lohitakavaṇṇāni lohitakanidassanāni lohitakanibhāsāni')}",
        f"odātāni odātavaṇṇāni odātanidassanāni odātanibhāsāni = {colours('odātāni odātavaṇṇāni odātanidassanāni odātanibhāsāni')}",
        f"rūpī rūpāni passati = भौतिक रूप वाला होकर {SEE} और",
        f"ajjhattaṃ arūpasaññī bahiddhā rūpāni passati = {AK} बाहर {SEE} और",
        "subhanti = “सुंदर” इस भाव के साथ,",
    ]
    fm += [f"{k.strip()} = {m}, … जो {a} की पहचान के साथ होने वाला … है" for k, (m, a) in ARUPA.items()]
    fm += [f"{k} (heading; closing line adds «।») = {v}" for k, v in TITLES.items()]
    fm += ["Lokuttarakusalaṃ (heading at the start of 2-03, from the termbase; closing line adds «।») = लोकोत्तर हितकर मन"]
    fm += [f"{k} = {v[0]} ({v[1]})" for k, v in F.items() if k not in sm.F]
    fm += [f"{k} = {v[0]} ({v[1]} pl.)" for k, v in PLURAL.items()]
    text = NOTES_HEAD + "\n".join(fm) + "\n" + NOTES_TAIL
    (RAILS_DIR / "notes-2-01_2-02.md").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    sample_ids = set(sm.s)
    h1 = build(PALI / CH1, skip=sample_ids)
    h1.update(sm.s)
    h2 = build(PALI / CH2)
    check_no_pali(h1)
    check_no_pali(h2)
    sm.emit(PALI / CH1, h1, OUT / CH1)
    sm.emit(PALI / CH2, h2, OUT / CH2)
    sample = (RAILS_DIR / "sample-2-01" / "2-01-sample.md").read_text(encoding="utf-8")
    assert (OUT / CH1).read_text(encoding="utf-8").startswith(sample), "sample prefix changed"
    assert f"{KAMA}, जो प्रसन्नता के साथ होने वाला और ज्ञान से जुड़ा होता है और जिसका विषय {OBJ_HI[OBJ_FULL]}," == sm.OPEN_KAMA
    write_notes()
