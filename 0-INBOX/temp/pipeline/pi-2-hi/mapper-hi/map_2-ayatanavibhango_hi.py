"""pi-2 Pāli->Hindi keyword map: 2-ayatanavibhango.

usage: python -I -X utf8 map_2-ayatanavibhango_hi.py
Imports map_sample_hi (read-only) and the shared table of chapters 2/3/8/9; extends them here only.
"""
import importlib
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PP_SEGMENTS, NDE, build_part, verify, read_hindi, lc  # noqa: E402
C = importlib.import_module("map_2-3-8-9_common_hi")

CH = "2-ayatanavibhango"
PP_SEGMENTS.update({"2-170", "2-171"})

T = {}
SENSE = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर", "mano": "मन"}
for _p, _h in SENSE.items():
    T[_p] = _h
    T[_p + "dhātu"] = f"{_h} का तत्व"
    T[_p + "viññāṇaṃ"] = f"{_h} की चेतना"
OBJ = {"rūpa": "दृश्य रूप", "sadda": "ध्वनि", "gandha": "गंध", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श"}
for _p, _h in OBJ.items():
    T[_p] = _h
    T[_p + "dhātu"] = f"{_h} का तत्व"

T.update({
    "āyatana": "इंद्रिय-क्षेत्र", "āyatanāni": "इंद्रिय-क्षेत्र", "āyatanā": "इंद्रिय-क्षेत्र",
    "āyatanānaṃ": "इंद्रिय-क्षेत्र", "dvādasāyatanāni": "बारह इंद्रिय-क्षेत्र", "dvādasannaṃ": "बारह",
    "dvādasannaṃ āyatanānaṃ": "बारह इंद्रिय-क्षेत्र",
    "manāyatanaṃ": "मन का इंद्रिय-क्षेत्र", "dhammāyatanaṃ": "मन के विषयों का इंद्रिय-क्षेत्र",
    # Suttanta: «Cakkhuṃ aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ …»
    "cakkhuṃ": "आँख", "sotaṃ": "कान", "ghānaṃ": "नाक", "kāyo": "शरीर", "dhammā": "मन के विषय",
    "aniccaṃ": "अनित्य", "dukkhaṃ": "दुःख", "anattā": "आत्मा से रहित", "vipariṇāmadhammaṃ": "बदल जाने वाला",
    # the sense bases (pi-1 ^1-600 wording)
    "upādāya": "व्युत्पन्न", "pasādo": "संवेदनशीलता", "upādāya pasādo": "व्युत्पन्न … संवेदनशीलता",
    "bhūtānaṃ": "महाभूत", "mahābhūtānaṃ": "महाभूत", "attabhāva": "व्यक्तिगत अस्तित्व",
    "anidassano": "दिखाई न देने वाला", "sappaṭigho": "टकराव वाला", "sappaṭighaṃ": "टकराव वाला",
    "sappaṭighena": "टकराव वाला", "sappaṭighāya": "टकराव वाला", "sappaṭigha": "टकराव वाला",
    "anidassanaṃ": "दिखाई न देने वाला", "anidassanena": "दिखाई न देने वाला",
    "anidassano sappaṭigho": "दिखाई न देने वाला और टकराव वाला",
    "anidassanaṃ sappaṭighaṃ": "दिखाई न देने वाला और टकराव वाला",
    "anidassanena sappaṭighena": "दिखाई न देने वाला और टकराव वाला",
    "anidassanāya sappaṭighāya": "दिखाई न देने वाला और टकराव वाला",
    "sanidassanaṃ": "दिखाई देने वाला", "sanidassanaṃ sappaṭighaṃ": "दिखाई देने वाला और टकराव वाला",
    "cakkhundriya": "आँख की क्षमता", "sotindriya": "कान की क्षमता", "ghānindriya": "नाक की क्षमता",
    "jīvhindriya": "जीभ की क्षमता", "kāyindriya": "शरीर की क्षमता", "indriya": "क्षमता",
    "dvārā": "द्वार", "samuddo": "सागर", "paṇḍara": "उज्ज्वलता", "khetta": "खेत", "netta": "नेत्र",
    "tīra": "किनारा", "suñño": "सूना", "gāmo": "गाँव", "rūpaṃ": "दृश्य रूप",
    "saddaṃ": "ध्वनि", "gandhaṃ": "गंध", "rasaṃ": "स्वाद", "phoṭṭhabbaṃ": "स्पर्श",
    "suṇi": "सुन चुका", "suṇāti": "सुनना", "suṇissati": "सुनेगा", "ghāyi": "सूँघ चुका", "ghāyati": "सूँघना",
    "sāyi": "चख चुका", "sāyati": "चखना", "phusi": "छू चुका", "phusati": "छूना", "phusissati": "छुएगा",
    "cakkhunā": "आँख", "sotena": "कान", "ghānena": "नाक", "jivhāya": "जीभ", "kāyena": "शरीर",
    # manāyatana
    "hetukaṃ": "मूल वाला", "sampayuttaṃ": "जुड़ा", "phassasampayuttaṃ": "संपर्क से जुड़ा",
    "vedanāya sampayuttaṃ": "अनुभूति से जुड़ा", "sukhāya vedanāya sampayuttaṃ": "सुखद अनुभूति से जुड़ा",
    "dukkhāya vedanāya sampayuttaṃ": "दुःखद अनुभूति से जुड़ा", "sahagataṃ": "के साथ होने वाला",
    "manoviññāṇaṃ": "मन की चेतना", "dukkha": "दुःख", "sukha": "सुख",
    "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacaraṃ": "अभौतिक लोक से संबंधित",
    # rūpāyatana
    "vaṇṇa": "रंग", "nibhā": "आभा", "vaṇṇanibhā": "रंग-आभा", "nīlaṃ": "नीला", "pītakaṃ": "पीला",
    "lohitakaṃ": "लाल", "odātaṃ": "सफ़ेद", "kāḷakaṃ": "काला", "mañjiṭṭhakaṃ": "मजीठ जैसा गहरा लाल",
    "hari": "हरा", "harivaṇṇaṃ": "हरे रंग का", "amba": "आम", "aṅkura": "कोंपल", "vaṭṭaṃ": "गोल",
    "parimaṇḍalaṃ": "वृत्ताकार", "caturassaṃ": "चौकोर", "chaḷaṃsaṃ": "छह कोनों वाला",
    "aṭṭhaṃsaṃ": "आठ कोनों वाला", "soḷasaṃsaṃ": "सोलह कोनों वाला", "chāyā": "छाया", "ātapo": "धूप",
    "āloko": "प्रकाश", "andhakāro": "अंधकार", "abbhā": "बादल", "mahikā": "कोहरा", "dhūmo": "धुआँ",
    "rajo": "धूल", "canda": "चंद्र", "maṇḍalassa": "मंडल", "sūriya": "सूर्य", "tārakarūpānaṃ": "तारा",
    "ādāsa": "दर्पण", "maṇi": "मणि", "saṅkha": "शंख", "mutta": "मोती", "veḷuriyassa": "वैदूर्य",
    "rajatassa": "चाँदी", "yaṃ vā pana": "या जो भी",
    # saddāyatana
    "saddo": "ध्वनि", "bheri": "नगाड़ा", "paṇava": "ढोलक", "gīta": "गाना", "vādita": "बाजा", "samma": "मंजीरा",
    "pāṇi": "ताली", "sattānaṃ": "प्राणी", "nigghosa": "शोर", "dhātūnaṃ": "वस्तु", "sannighāta": "आपस में टकराना",
    "vāta": "हवा", "udaka": "पानी", "manussa": "मनुष्य", "amanussa": "अमानवीय प्राणी", "yo vā pana": "या जो भी",
    # gandhāyatana / rasāyatana
    "gandho": "गंध", "mūla": "जड़", "sāra": "सार", "taca": "छाल", "patta": "पत्ता", "puppha": "फूल",
    "phala": "फल", "āma": "कच्चा मांस", "vissa": "सड़न", "sugandho": "सुगंध", "duggandho": "दुर्गंध",
    "raso": "स्वाद", "khandha": "तना", "ambilaṃ": "खट्टा", "madhuraṃ": "मीठा", "tittakaṃ": "कड़वा",
    "kaṭukaṃ": "तीखा", "loṇikaṃ": "नमकीन", "khārikaṃ": "खारा", "lambikaṃ": "हल्का खट्टा",
    "kasāvo": "कसैला", "sādu": "स्वादिष्ट", "asādu": "बेस्वाद",
    # phoṭṭhabbāyatana
    "kakkhaḷaṃ": "कठोर", "mudukaṃ": "मुलायम", "saṇhaṃ": "चिकना", "pharusaṃ": "खुरदरा", "garukaṃ": "भारी",
    "lahukaṃ": "हल्का", "pathavī": "पृथ्वी",
    # dhammāyatana (as 3-dhatuvibhango ^2-184)
    "itthi": "स्त्रीत्व", "āhāro": "भोजन", "saṅkhāra": "मानसिक रचनाएँ", "hetuko": "मूल वाला",
    "anidassana": "दिखाई न देने वाला", "anidassanaappaṭighaṃ": "दिखाई न देने वाला और टकराव से रहित",
    "appaṭighaṃ": "टकराव से रहित", "asaṅkhatā": "अनिर्मित", "asaṅkhatā dhātu": "अनिर्मित तत्व",
    "rāga": "राग", "dosa": "द्वेष", "moha": "मोह", "dasa": "दस", "abyākato": "नैतिक रूप से अनिर्धारित",
    "kusalo": "हितकर", "akusalo": "हानिकर",
    "bahuvidhena vedanākkhandho": "अनेक प्रकार से अनुभूति का समूह",
    "bahuvidhena saññākkhandho": "अनेक प्रकार से पहचान का समूह",
    "bahuvidhena saṅkhārakkhandho": "अनेक प्रकार से मानसिक रचनाओं का समूह",
    # Pañhāpucchaka
    "dasāyatanā": "दस इंद्रिय-क्षेत्र", "ekādasāyatanā": "ग्यारह इंद्रिय-क्षेत्र",
    "āyatanā siyā": "इंद्रिय-क्षेत्र कभी", "āyatanā anidassana": "इंद्रिय-क्षेत्र दिखाई न देने वाला",
    "āyatanā anidassanā": "इंद्रिय-क्षेत्र दिखाई न देने वाला", "āyatanā sappaṭighā": "इंद्रिय-क्षेत्र टकराव वाला",
    "dasāyatanā sappaṭighā": "दस इंद्रिय-क्षेत्र टकराव वाला",
    "anidassanasappaṭighā": "दिखाई न देने वाला पर टकराव वाला", "sanidassana": "दिखाई देने वाला",
    "nevavipākanavipākadhammadhammā": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "vattabbaṃ": "कहा जा सकना", "majjhimā": "मध्यम", "parittā": "सीमित", "sappaṭighā": "टकराव वाला",
    "sanidassanaṃ": "दिखाई देने वाला", "lokiyā": "लौकिक", "ajjhattikā": "आंतरिक", "asaṅkhataṃ": "अनिर्मित", "arūpaṃ": "अभौतिक",
    "anārammaṇā": "विषय से रहित", "cetasikaṃ": "मन का सहचर", "acetasikā": "मन का सहचर न होने वाला",
    "cittasampayuttaṃ": "मन से जुड़ा", "saṃsaṭṭhaṃ": "घुला-मिला", "cittasaṃsaṭṭhaṃ": "मन से घुला-मिला",
    "asaṃkiliṭṭhā": "क्लेशों से मलिन न होने वाला", "vedanāya sampayuttā": "अनुभूति से जुड़ा",
    "sukhāya vedanāya sampayuttā": "सुखद अनुभूति से जुड़ा", "dukkhāya vedanāya sampayuttā": "दुःखद अनुभूति से जुड़ा",
    "kilesā ceva kilesasampayuttā": "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी",
    "kileso ceva kilesasampayuttañca": "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी",
    "hetu ceva hetusampayuttañca": "मूल रूपी भी और मूलों से जुड़ा भी",
    "saṃyojanañceva saṃyojanasampayuttañca": "बंधन रूपी भी और बंधनों से जुड़ा भी",
    "nīvaraṇañceva nīvaraṇasampayuttañca": "बाधा रूपी भी और बाधाओं से जुड़ा भी",
    "āsavo ceva āsavasampayuttañca": "मन के मैल रूपी भी और मन के मैलों से जुड़ा भी",
    "gantho ceva ganthasampayuttañca": "गाँठ रूपी भी और गाँठों से जुड़ा भी",
})
TABLE = {**C.SHARED_TABLE, **T}

OVR = {
    "2-154": {"dukkhaṃ": "दुःख"},
    # «sukhasamphassaṃ dukkhasamphassaṃ» = «सुखद संपर्क वाला, दुःखद संपर्क वाला»
    "2-166": {"sukha": "सुखद", "dukkha": "दुःखद"},
    # only «rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ» = «वह भौतिक रूप जो …»
    "2-167": {"rūpaṃ": "भौतिक रूप", "hetu": "मूल"},
    # «Vipākadhammadhammā / nevavipākanavipākadhammadhammā»: the dhammā fragment has no word of its own
    "2-170": {"dhammā": NDE, "uppannā": "उत्पन्न हो चुका"},
    "2-171": {"rūpā": "भौतिक"},   # «Dasāyatanā rūpā» = «दस इंद्रिय-क्षेत्र भौतिक हैं»
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


_PH = "text «फलों की गंध / फलों का स्वाद»: फल ~ फलों, the checker does not inflect a two-letter word"
ALLOWED = {
    ("2-164", "phala"): _PH, ("2-165", "phala"): _PH,
    ("2-171", "apariyāpannā"): "text «न समाए हुए»: समाया ~ समाए is regular inflection the checker does not model (as the sample, 2-153)",
}

if __name__ == "__main__":
    build_part(CH, resolver)
    verify(CH, allowed=ALLOWED)
