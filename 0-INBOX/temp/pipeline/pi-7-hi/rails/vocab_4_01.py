"""Vocabulary for build_rails_4-01.py (pi-7 4-01, Hindi plain RAILS). Pāli keys are lower-case-initial."""

RUPA_CITTA = "मन से उत्पन्न भौतिक रूप"
RUPA_KATATTA = "किए गए कर्म से उत्पन्न भौतिक रूप"
RUPA_UPADA = "व्युत्पन्न भौतिक रूप"

# ---------------------------------------------------------------- headings
HEAD_X = {
    "(Catuttho bhāgo)": "(चौथा भाग)",
    "Dhammānulome dukapaṭṭhānaṃ": "परिघटनाओं का सकारात्मक क्रम: दो-दो के वर्गीकरणों के कारण-संबंध",
    "Kilesagocchakaṃ": "मन के क्लेशों का वर्ग",
    "Piṭṭhidukaṃ": "अंतिम दो-दो के वर्गीकरण",
    # dyad names (harmonise-notes.md §1)
    "Kilesadukaṃ": "मन के क्लेश वाला दो का वर्गीकरण",
    "Saṃkilesikadukaṃ": "क्लेशों का विषय बनने वाला दो का वर्गीकरण",
    "Saṃkiliṭṭhadukaṃ": "क्लेशों से मलिन परिघटनाओं वाला दो का वर्गीकरण",
    "Kilesasampayuttadukaṃ": "क्लेशों से जुड़ाव वाला दो का वर्गीकरण",
    "Kilesasaṃkilesikadukaṃ": "मन के क्लेश और क्लेशों का विषय बनने वाला दो का वर्गीकरण",
    "Kilesasaṃkiliṭṭhadukaṃ": "मन के क्लेश और क्लेशों से मलिन परिघटनाओं वाला दो का वर्गीकरण",
    "Kilesakilesasampayuttadukaṃ": "मन के क्लेश और क्लेशों से जुड़ाव वाला दो का वर्गीकरण",
    "Kilesavippayuttasaṃkilesikadukaṃ": "क्लेशों से अलगाव और क्लेशों का विषय बनने वाला दो का वर्गीकरण",
    "Dassanenapahātabbadukaṃ": "सत्य-दर्शन से छोड़े जाने वाला दो का वर्गीकरण",
    "Bhāvanāyapahātabbadukaṃ": "मानसिक अभ्यास से छोड़े जाने वाला दो का वर्गीकरण",
    "Dassanenapahātabbahetukadukaṃ": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण",
    "Bhāvanāyapahātabbahetukadukaṃ": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण",
    "Savitakkadukaṃ": "आरंभिक विचार वाला दो का वर्गीकरण",
    "Savicāradukaṃ": "सतत विचार वाला दो का वर्गीकरण",
    "Sappītikadukaṃ": "उल्लास वाला दो का वर्गीकरण",
    "Pītisahagatadukaṃ": "उल्लास के साथ होने वाला दो का वर्गीकरण",
    "Sukhasahagatadukaṃ": "सुख के साथ होने वाला दो का वर्गीकरण",
    "Upekkhāsahagatadukaṃ": "समभाव के साथ होने वाला दो का वर्गीकरण",
    "Kāmāvacaradukaṃ": "इंद्रिय-सुखों के लोक वाला दो का वर्गीकरण",
    "Rūpāvacaradukaṃ": "सूक्ष्म भौतिक लोक वाला दो का वर्गीकरण",
    "Arūpāvacaradukaṃ": "अभौतिक लोक वाला दो का वर्गीकरण",
    "Pariyāpannadukaṃ": "अस्तित्व के लोकों में समाए होने वाला दो का वर्गीकरण",
    "Niyyānikadukaṃ": "मुक्ति की ओर ले जाने वाला दो का वर्गीकरण",
    "Niyatadukaṃ": "निश्चित वाला दो का वर्गीकरण",
    "Sauttaradukaṃ": "सर्वोच्च न होने वाला दो का वर्गीकरण",
    "Saraṇadukaṃ": "संघर्ष वाला दो का वर्गीकरण",
    # sections
    "Sahajātavāro": "सह-उत्पत्ति का खंड",
    "Paccayavāro": "कारण का खंड",
    "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड",
    "Sampayuttavāro": "जुड़ाव का खंड",
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Paccayānulomādi": "कारणों का सकारात्मक क्रम आदि",
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        "सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "Nissaya-saṃsaṭṭhavāro": "आश्रय और घुले-मिले होने का खंड",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Paccanīyaṃ.": "नकारात्मक क्रम।",
    "Pacchājātāsevanapaccayā": "पश्चात्-उत्पत्ति-कारण और पुनरावृत्ति-कारण",
    "Nahetu-naārammaṇapaccayā": "मूल-कारण का अभाव और विषय-कारण का अभाव",
    "Hetudukaṃ": "मूल-कारण के साथ दो कारणों का मेल",
}

# ---------------------------------------------------------------- dyad items: [(specA, hindiA), (specB, hindiB)]
# hindi = feminine form agreeing with «परिघटना»; masculine forms are derived (वाली → वाला/वाले …)
KIL = "मन के क्लेश रूपी"
ITEMS_D = [
    (("kilesa", KIL), ("nokilesa", KIL + " न होने वाली")),
    (("saṃkilesika", "क्लेशों का विषय बनने वाली"), ("asaṃkilesika", "क्लेशों का विषय न बनने वाली")),
    (("saṃkiliṭṭha", "क्लेशों से मलिन"), ("asaṃkiliṭṭha", "क्लेशों से मलिन न होने वाली")),
    (("kilesasampayutta", "क्लेशों से जुड़ी"), ("kilesavippayutta", "क्लेशों से अलग")),
    ((("both", "kilesa", "saṃkilesika"), KIL + " भी और क्लेशों का विषय बनने वाली भी"),
     (("butnot", "saṃkilesika", "kilesa"), "क्लेशों का विषय बनने वाली, पर स्वयं " + KIL + " न होने वाली")),
    ((("both", "kilesa", "saṃkiliṭṭha"), KIL + " भी और क्लेशों से मलिन भी"),
     (("butnot", "saṃkiliṭṭha", "kilesa"), "क्लेशों से मलिन, पर स्वयं " + KIL + " न होने वाली")),
    ((("both", "kilesa", "kilesasampayutta"), KIL + " भी और क्लेशों से जुड़ी भी"),
     (("butnot", "kilesasampayutta", "kilesa"), "क्लेशों से जुड़ी, पर स्वयं " + KIL + " न होने वाली")),
    (("kilesavippayutta saṃkilesika", "क्लेशों से अलग, पर क्लेशों का विषय बनने वाली"),
     ("kilesavippayutta asaṃkilesika", "क्लेशों से अलग और क्लेशों का विषय न बनने वाली")),
    (("=dassanena pahātabba", "सत्य-दर्शन से छोड़ी जाने वाली"), ("=nadassanena pahātabba", "सत्य-दर्शन से न छोड़ी जाने वाली")),
    (("=bhāvanāya pahātabba", "मानसिक अभ्यास से छोड़ी जाने वाली"),
     ("=nabhāvanāya pahātabba", "मानसिक अभ्यास से न छोड़ी जाने वाली")),
    (("=dassanena pahātabbahetuka", "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली"),
     ("=nadassanena pahātabbahetuka", "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित")),
    (("=bhāvanāya pahātabbahetuka", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
     ("=nabhāvanāya pahātabbahetuka", "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित")),
    (("savitakka", "आरंभिक विचार वाली"), ("avitakka", "आरंभिक विचार से रहित")),
    (("savicāra", "सतत विचार वाली"), ("avicāra", "सतत विचार से रहित")),
    (("sappītika", "उल्लास वाली"), ("appītika", "उल्लास से रहित")),
    (("pītisahagata", "उल्लास के साथ होने वाली"), ("napītisahagata", "उल्लास के साथ न होने वाली")),
    (("sukhasahagata", "सुख के साथ होने वाली"), ("nasukhasahagata", "सुख के साथ न होने वाली")),
    (("upekkhāsahagata", "समभाव के साथ होने वाली"), ("naupekkhāsahagata", "समभाव के साथ न होने वाली")),
    (("kāmāvacara", "इंद्रिय-सुखों के लोक से संबंधित"), ("nakāmāvacara", "इंद्रिय-सुखों के लोक से संबंधित न होने वाली")),
    (("rūpāvacara", "सूक्ष्म भौतिक लोक से संबंधित"), ("narūpāvacara", "सूक्ष्म भौतिक लोक से संबंधित न होने वाली")),
    (("arūpāvacara", "अभौतिक लोक से संबंधित"), ("naarūpāvacara", "अभौतिक लोक से संबंधित न होने वाली")),
    (("pariyāpanna", "अस्तित्व के लोकों में समाई हुई"), ("apariyāpanna", "अस्तित्व के लोकों में न समाई हुई")),
    (("niyyānika", "मुक्ति की ओर ले जाने वाली"), ("aniyyānika", "मुक्ति की ओर न ले जाने वाली")),
    (("niyata", "निश्चित"), ("aniyata", "अनिश्चित")),
    (("sauttara", "सर्वोच्च न होने वाली"), ("anuttara", "सर्वोच्च")),
    (("saraṇa", "संघर्ष वाली"), ("araṇa", "संघर्ष से रहित")),
]
# single adjectives used like items (not dyad pairs)
EXTRA_ITEMS = [
    ("vicikicchāsahagata", "संशय के साथ होने वाली"),
    ("uddhaccasahagata", "बेचैनी के साथ होने वाली"),
    ("ahetuka", "मूल से रहित"),
    ("vipāka", "कर्म-फल रूपी"),
]
ITEMS = [x for pair in ITEMS_D for x in pair] + EXTRA_ITEMS

# nouns: (pāli nom, acc, dat, pāli gender, hindi direct, hindi oblique, hindi gender)
NOUNS = [
    ("rāgo", "rāgaṃ", "rāgassa", "m", "राग", "राग", "m"),
    ("doso", "dosaṃ", "dosassa", "m", "द्वेष", "द्वेष", "m"),
    ("moho", "mohaṃ", "mohassa", "m", "मोह", "मोह", "m"),
    ("māno", "mānaṃ", "mānassa", "m", "अहंकार", "अहंकार", "m"),
    ("diṭṭhi", "diṭṭhiṃ", "diṭṭhiyā", "f", "दृष्टि", "दृष्टि", "f"),
    ("vicikicchā", "vicikicchaṃ", "vicikicchāya", "f", "संशय", "संशय", "m"),
    ("uddhaccaṃ", "uddhaccaṃ", "uddhaccassa", "n", "बेचैनी", "बेचैनी", "f"),
    ("domanassaṃ", "domanassaṃ", "domanassassa", "n", "उदासी", "उदासी", "f"),
    ("patthanā", "patthanaṃ", "patthanāya", "f", "कामना", "कामना", "f"),
    ("saddhā", "saddhaṃ", "saddhāya", "f", "श्रद्धा", "श्रद्धा", "f"),
    ("sīlaṃ", "sīlaṃ", "sīlassa", "n", "सदाचार", "सदाचार", "m"),
    ("paññā", "paññaṃ", "paññāya", "f", "प्रज्ञा", "प्रज्ञा", "f"),
    ("pīti", "pītiṃ", "pītiyā", "f", "उल्लास", "उल्लास", "m"),
    ("vitakko", "vitakkaṃ", "vitakkassa", "m", "आरंभिक विचार", "आरंभिक विचार", "m"),
    ("vicāro", "vicāraṃ", "vicārassa", "m", "सतत विचार", "सतत विचार", "m"),
    ("sukhaṃ", "sukhaṃ", "sukhassa", "n", "सुख", "सुख", "m"),
    ("upekkhā", "upekkhaṃ", "upekkhāya", "f", "समभाव", "समभाव", "m"),
    ("jhānaṃ", "jhānaṃ", "jhānassa", "n", "ध्यान", "ध्यान", "m"),
    ("maggo", "maggaṃ", "maggassa", "m", "मार्ग", "मार्ग", "m"),
    ("phalaṃ", "phalaṃ", "phalassa", "n", "फल", "फल", "m"),
    ("cuticittaṃ", "cuticittaṃ", "cuticittassa", "n", "मृत्यु का मन", "मृत्यु के मन", "m"),
    ("upapatticittaṃ", "upapatticittaṃ", "upapatticittassa", "n", "जन्म का मन", "जन्म के मन", "m"),
    ("bhavaṅgaṃ", "bhavaṅgaṃ", "bhavaṅgassa", "n", "जीवन-धारा", "जीवन-धारा", "f"),
    ("kusalākusalaṃ", "kusalākusalaṃ", "kusalākusalassa", "n", "हितकर और हानिकर मन", "हितकर और हानिकर मन", "m"),
    ("vuṭṭhānaṃ", "vuṭṭhānaṃ", "vuṭṭhānassa", "n", "बाहर आने वाला मन", "मन के बाहर आने", "m"),
    ("kāyaviññāṇaṃ", "kāyaviññāṇaṃ", "kāyaviññāṇassa", "n", "शरीर की चेतना", "शरीर की चेतना", "f"),
    ("vipākamanodhātu", "vipākamanodhātuṃ", "vipākamanodhātuyā", "f",
     "कर्म-फल रूपी मन का तत्व", "कर्म-फल रूपी मन के तत्व", "m"),
    ("vipākamanoviññāṇadhātu", "vipākamanoviññāṇadhātuṃ", "vipākamanoviññāṇadhātuyā", "f",
     "कर्म-फल रूपी मन की चेतना का तत्व", "कर्म-फल रूपी मन की चेतना के तत्व", "m"),
    ("kiriyamanoviññāṇadhātu", "kiriyamanoviññāṇadhātuṃ", "kiriyamanoviññāṇadhātuyā", "f",
     "केवल क्रिया रूपी मन की चेतना का तत्व", "केवल क्रिया रूपी मन की चेतना के तत्व", "m"),
    ("phalasamāpatti", "phalasamāpattiṃ", "phalasamāpattiyā", "f", "फल की ध्यान-अवस्था", "फल की ध्यान-अवस्था", "f"),
    ("cetanā", "cetanaṃ", "cetanāya", "f", "इरादा", "इरादे", "m"),
    ("gotrabhu", "gotrabhuṃ", "gotrabhussa", "m", "गोत्र-परिवर्तन", "गोत्र-परिवर्तन", "m"),
    ("ākāsānañcāyatanaṃ", "ākāsānañcāyatanaṃ", "ākāsānañcāyatanassa", "n",
     "अनंत आकाश का क्षेत्र", "अनंत आकाश के क्षेत्र", "m"),
    ("viññāṇañcāyatanaṃ", "viññāṇañcāyatanaṃ", "viññāṇañcāyatanassa", "n",
     "अनंत चेतना का क्षेत्र", "अनंत चेतना के क्षेत्र", "m"),
    ("ākiñcaññāyatanaṃ", "ākiñcaññāyatanaṃ", "ākiñcaññāyatanassa", "n",
     "कुछ भी न होने का क्षेत्र", "कुछ भी न होने के क्षेत्र", "m"),
    ("nevasaññānāsaññāyatanaṃ", "nevasaññānāsaññāyatanaṃ", "nevasaññānāsaññāyatanassa", "n",
     "न पहचान न अ-पहचान का क्षेत्र", "न पहचान न अ-पहचान के क्षेत्र", "m"),
    ("vipassanā", "vipassanaṃ", "vipassanāya", "f", "अंतर्दृष्टि", "अंतर्दृष्टि", "f"),
    ("abhiññā", "abhiññaṃ", "abhiññāya", "f", "उच्च ज्ञान", "उच्च ज्ञान", "m"),
    ("samāpatti", "samāpattiṃ", "samāpattiyā", "f", "ध्यान-अवस्था", "ध्यान-अवस्था", "f"),
]
# ordinals with jhāna and magga
for _o, _hd, _ho in (("paṭham", "पहला", "पहले"), ("dutiy", "दूसरा", "दूसरे"), ("tatiy", "तीसरा", "तीसरे"),
                     ("catutth", "चौथा", "चौथे")):
    NOUNS.append((f"{_o}aṃ jhānaṃ", f"{_o}aṃ jhānaṃ", f"{_o}assa jhānassa", "n", f"{_hd} ध्यान", f"{_ho} ध्यान", "m"))
    NOUNS.append((f"{_o}o maggo", f"{_o}aṃ maggaṃ", f"{_o}assa maggassa", "m", f"{_hd} मार्ग", f"{_ho} मार्ग", "m"))

# ---------------------------------------------------------------- nominative NPs: pali -> (hindi, gender)
NOM_X = {
    "moho": ("मोह", "ms"), "diṭṭhi": ("दृष्टि", "fs"), "thinaṃ": ("आलस्य", "ms"), "uddhaccaṃ": ("बेचैनी", "fs"),
    "ahirikaṃ": ("निर्लज्जता", "fs"), "anottappaṃ": ("बुराई के प्रति निडरता", "fs"), "māno": ("अहंकार", "ms"),
    "lobho": ("लोभ", "ms"), "doso": ("द्वेष", "ms"), "vicikicchā": ("संशय", "ms"), "rāgo": ("राग", "ms"),
    "kilesā": ("मन के क्लेश", "mp"), "kileso": ("मन के क्लेश", "ms"),
    "khandhā": ("समूह", "mp"), "tayo khandhā": ("तीन समूह", "mp"), "dve khandhā": ("दो समूह", "mp"),
    "eko khandho": ("एक समूह", "ms"), "sampayuttakā khandhā": ("जुड़े हुए समूह", "mp"),
    "cittasamuṭṭhānaṃ rūpaṃ": (RUPA_CITTA, "ms"), "kaṭattārūpaṃ": (RUPA_KATATTA, "ms"),
    "kaṭattā rūpaṃ": (RUPA_KATATTA, "ms"), "kaṭattā ca rūpaṃ": (RUPA_KATATTA, "ms"), "upādārūpaṃ": (RUPA_UPADA, "ms"),
    "vatthu": ("आधार", "ms"), "mahābhūtā": ("महाभूत", "mp"), "tayo mahābhūtā": ("तीन महाभूत", "mp"),
    "dve mahābhūtā": ("दो महाभूत", "mp"), "ekaṃ mahābhūtaṃ": ("एक महाभूत", "ms"),
    "sampayuttakā cetanā": ("जुड़ा हुआ इरादा", "ms"), "cetanā": ("इरादा", "ms"),
    "vicikicchāsahagato moho": ("संशय के साथ होने वाला मोह", "ms"),
    "uddhaccasahagato moho": ("बेचैनी के साथ होने वाला मोह", "ms"),
    "vicikicchāsahagato uddhaccasahagato moho": ("संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह", "ms"),
    "cakkhuviññāṇaṃ": ("आँख की चेतना", "fs"), "sotaviññāṇaṃ": ("कान की चेतना", "fs"),
    "ghānaviññāṇaṃ": ("नाक की चेतना", "fs"), "jivhāviññāṇaṃ": ("जीभ की चेतना", "fs"),
    "kāyaviññāṇaṃ": ("शरीर की चेतना", "fs"),
    "rūpajīvitindriyaṃ": ("भौतिक जीवन-क्षमता", "fs"),
    "kabaḷīkāro āhāro": ("कौर-कौर खाया जाने वाला भोजन", "ms"),
    "purimā purimā kilesā": ("पहले-पहले के मन के क्लेश", "mp"),
    "āvajjanā": ("मन को विषय की ओर मोड़ना", "ms"), "anulomaṃ": ("अनुरूपता", "fs"),
    "nibbānaṃ": ("निर्वाण", "ms"), "vodānaṃ": ("शुद्धि", "fs"), "gotrabhu": ("गोत्र-परिवर्तन", "ms"),
    "saddhā": ("श्रद्धा", "fs"), "senāsanaṃ": ("निवास-स्थान", "ms"), "patthanā": ("कामना", "fs"),
    "kilesā hetū": (KIL + " मूल", "mp"),
    "rūpāyatanaṃ": ("दृश्य रूप का इंद्रिय-क्षेत्र", "ms"), "saddāyatanaṃ": ("ध्वनि का इंद्रिय-क्षेत्र", "ms"),
    "gandhāyatanaṃ": ("गंध का इंद्रिय-क्षेत्र", "ms"), "rasāyatanaṃ": ("स्वाद का इंद्रिय-क्षेत्र", "ms"),
    "phoṭṭhabbāyatanaṃ": ("स्पर्श का इंद्रिय-क्षेत्र", "ms"),
    "cakkhāyatanaṃ": ("आँख का इंद्रिय-क्षेत्र", "ms"), "sotāyatanaṃ": ("कान का इंद्रिय-क्षेत्र", "ms"),
    "ghānāyatanaṃ": ("नाक का इंद्रिय-क्षेत्र", "ms"), "jivhāyatanaṃ": ("जीभ का इंद्रिय-क्षेत्र", "ms"),
    "kāyāyatanaṃ": ("शरीर का इंद्रिय-क्षेत्र", "ms"),
}

# ---------------------------------------------------------------- accusative NPs (object of paṭicca …): hindi oblique
OBL_X = {
    "lobhaṃ": "लोभ", "dosaṃ": "द्वेष", "mohaṃ": "मोह", "vicikicchaṃ": "संशय", "uddhaccaṃ": "बेचैनी",
    "kilesaṃ": "मन के क्लेश", "kilese": "मन के क्लेशों", "rāgaṃ": "राग", "diṭṭhiṃ": "दृष्टि", "mānaṃ": "अहंकार",
    "sampayuttake khandhe": "जुड़े हुए समूहों", "khandhe": "समूहों", "tayo khandhe": "तीन समूहों",
    "dve khandhe": "दो समूहों", "ekaṃ khandhaṃ": "एक समूह",
    "vatthuṃ": "आधार", "mahābhūte": "महाभूतों", "ekaṃ mahābhūtaṃ": "एक महाभूत", "tayo mahābhūte": "तीन महाभूतों",
    "dve mahābhūte": "दो महाभूतों",
    "vicikicchāsahagate khandhe": "संशय के साथ होने वाले समूहों",
    "uddhaccasahagate khandhe": "बेचैनी के साथ होने वाले समूहों",
    "vicikicchāsahagate uddhaccasahagate khandhe": "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों",
    "cakkhāyatanaṃ": "आँख के इंद्रिय-क्षेत्र", "sotāyatanaṃ": "कान के इंद्रिय-क्षेत्र",
    "ghānāyatanaṃ": "नाक के इंद्रिय-क्षेत्र", "jivhāyatanaṃ": "जीभ के इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ": "शरीर के इंद्रिय-क्षेत्र",
    "bāhiraṃ ekaṃ mahābhūtaṃ": "एक बाह्य महाभूत", "āhārasamuṭṭhānaṃ ekaṃ mahābhūtaṃ": "आहार से उत्पन्न एक महाभूत",
    "utusamuṭṭhānaṃ ekaṃ mahābhūtaṃ": "तापमान से उत्पन्न एक महाभूत",
    "asaññasattānaṃ ekaṃ mahābhūtaṃ": "पहचान-रहित प्राणियों में एक महाभूत",
    "bāhiraṃ": "बाह्य", "āhārasamuṭṭhānaṃ": "आहार से उत्पन्न", "utusamuṭṭhānaṃ": "तापमान से उत्पन्न",
    "saddhaṃ": "श्रद्धा", "sīlaṃ": "सदाचार", "paññaṃ": "प्रज्ञा", "patthanaṃ": "कामना",
    "kāyikaṃ sukhaṃ": "शारीरिक सुख", "kāyikaṃ dukkhaṃ": "शारीरिक दुःख", "utuṃ": "तापमान", "bhojanaṃ": "भोजन",
    "senāsanaṃ": "निवास-स्थान", "cakkhuṃ": "आँख", "dānaṃ": "दान",
}

# ---------------------------------------------------------------- dative NPs: hindi oblique without «के लिए»
DAT_X = {
    "kilesānaṃ": "मन के क्लेशों", "sampayuttakānaṃ kilesānaṃ": "जुड़े हुए मन के क्लेशों",
    "sampayuttakānaṃ khandhānaṃ": "जुड़े हुए समूहों", "khandhānaṃ": "समूहों",
    "cittasamuṭṭhānānaṃ rūpānaṃ": "मन से उत्पन्न भौतिक रूपों", "kaṭattā rūpānaṃ": "किए गए कर्म से उत्पन्न भौतिक रूपों",
    "kaṭattā ca rūpānaṃ": "किए गए कर्म से उत्पन्न भौतिक रूपों",
    "kaṭattārūpānaṃ": "किए गए कर्म से उत्पन्न भौतिक रूपों", "vipākānaṃ khandhānaṃ": "कर्म-फल रूपी समूहों",
    "tiṇṇannaṃ khandhānaṃ": "तीन समूहों", "dvinnaṃ khandhānaṃ": "दो समूहों",
    "pacchimānaṃ pacchimānaṃ kilesānaṃ": "बाद-बाद के मन के क्लेशों",
    "vuṭṭhānassa": "बाहर आने", "phalasamāpattiyā": "फल की ध्यान-अवस्था",
    "mohassa": "मोह", "diṭṭhiyā": "दृष्टि", "thinassa": "आलस्य", "uddhaccassa": "बेचैनी", "ahirikassa": "निर्लज्जता",
    "anottappassa": "बुराई के प्रति निडरता", "rāgassa": "राग", "dosassa": "द्वेष", "mānassa": "अहंकार",
    "patthanāya": "कामना", "saddhāya": "श्रद्धा", "paññāya": "प्रज्ञा",
    "kāyikassa sukhassa": "शारीरिक सुख", "kāyikassa dukkhassa": "शारीरिक दुःख",
    "imassa kāyassa": "इस शरीर", "purejātassa imassa kāyassa": "पहले उत्पन्न इस शरीर",
    "iddhividhañāṇassa": "अलौकिक शक्तियों के ज्ञान", "cetopariyañāṇassa": "दूसरों के मन को जानने के ज्ञान",
    "pubbenivāsānussatiñāṇassa": "पूर्व जन्मों के अनुस्मरण के ज्ञान",
    "yathākammūpagañāṇassa": "प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान",
    "anāgataṃsañāṇassa": "भविष्य को जानने के ज्ञान", "āvajjanāya": "मन को विषय की ओर मोड़ने",
    "gotrabhussa": "गोत्र-परिवर्तन", "vodānassa": "शुद्धि", "maggassa": "मार्ग", "phalassa": "फल",
    "cakkhuviññāṇassa": "आँख की चेतना", "sotaviññāṇassa": "कान की चेतना", "ghānaviññāṇassa": "नाक की चेतना",
    "jivhāviññāṇassa": "जीभ की चेतना", "kāyaviññāṇassa": "शरीर की चेतना",
}

PREFIX_X = {
    "arūpe": "अभौतिक लोक में",
}

# ---------------------------------------------------------------- whole pieces
_REVIEW = "पुनः विचार करता है"
_SAV1 = "उसका रस लेता है, उसमें आनंद लेता है"
CLAUSE_X = {
    "ekaṃ": "एक", "dve": "दो", "tīṇi": "तीन", "cattāri": "चार", "pañca": "पाँच", "cha": "छह", "satta": "सात",
    "aṭṭha": "आठ", "nava": "नौ", "nava pañhā": "नौ प्रश्न",
    "ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय",
    "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय",
    "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति", "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति",
    "sahajātaṃ": "सह-उत्पत्ति", "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति", "āhāraṃ": "आहार",
    "indriyaṃ": "क्षमता", "sahajātā": "सह-उत्पत्ति", "sahajāto": "सह-उत्पत्ति", "pacchājātā": "पश्चात्-उत्पत्ति",
    "nānākkhaṇikā": "भिन्न क्षण",
    "dānaṃ": "दान", "sīlaṃ": "सदाचार", "uposathakammaṃ": "उपवास-व्रत", "pubbe suciṇṇāni": "पहले भली-भाँति किए गए कार्य",
    "pubbe": "पहले", "jhānā": "ध्यान से", "jhānaṃ": "ध्यान",
    "jhānā vuṭṭhahitvā jhānaṃ paccavekkhati assādeti abhinandati":
        f"ध्यान से उठकर ध्यान पर {_REVIEW}, {_SAV1}",
    "jhānā vuṭṭhahitvā jhānaṃ paccavekkhati": f"ध्यान से उठकर ध्यान पर {_REVIEW}",
    "jhānā vuṭṭhahitvā": "ध्यान से उठकर",
    "taṃ ārabbha rāgo": "उसे विषय बनाकर राग",
    "ariyā maggā vuṭṭhahitvā": "आर्य मार्ग से उठकर",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti": "आर्य मार्ग से उठकर मार्ग को महत्व देकर पुनः विचार करते हैं",
    "ariyā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": "आर्य मार्ग से उठकर मार्ग पर पुनः विचार करते हैं",
    "uppajjati": "उत्पन्न होता है",
    "uddhaccaṃ uppajjati": "बेचैनी उत्पन्न होती है",
    "saddhaṃ upanissāya dānaṃ deti": "श्रद्धा के प्रबल आश्रय से दान देता है",
    "dānaṃ deti": "दान देता है", "mānaṃ jappeti": "अहंकार पालता है", "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "pāṇaṃ hanati": "जीव की हत्या करता है", "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati assādeti abhinandati":
        f"उपवास-व्रत का पालन करके उसे महत्व देकर {_REVIEW}, {_SAV1}",
    "taṃ garuṃ katvā rāgo uppajjati": "उसे महत्व देकर राग उत्पन्न होता है",
    "diṭṭhi uppajjati": "दृष्टि उत्पन्न होती है",
    "rāgo uppajjati": "राग उत्पन्न होता है",
    "cakkhuṃ": "आँख",
    "kilesā vuṭṭhānassa": "मन के क्लेश बाहर आने के लिए",
}

# ---------------------------------------------------------------- notes (exact content inside the parentheses)
NOTE_X = {
    "Mūlaṃ kātabbaṃ.": "मूल वाक्य से शुरू करना चाहिए।",
    "Mūlaṃ kātabbaṃ": "मूल वाक्य से शुरू करना चाहिए",
    "mūlaṃ kātabbaṃ": "मूल वाक्य से शुरू करना चाहिए",
    "mūlaṃ kātabbaṃ.": "मूल वाक्य से शुरू करना चाहिए।",
    "Mūlaṃ pucchitabbaṃ.": "मूल वाक्य से पूछना चाहिए।",
    "saṃkhittaṃ": "संक्षिप्त",
    "Saṃkhittaṃ.": "संक्षिप्त।",
    "yāva asaññasattā": "पहचान-रहित प्राणियों तक",
    "Yāva asaññasattā": "पहचान-रहित प्राणियों तक",
    "yāva ajjhattikā mahābhūtā": "आंतरिक महाभूतों तक",
    "cakkaṃ": "चक्र",
    "cakkaṃ, saṃkhittaṃ": "चक्र, संक्षिप्त",
    "sabbattha nava": "हर जगह नौ",
    "sabbattha dve": "हर जगह दो",
    "sabbattha cha": "हर जगह छह",
    "sabbattha cattāri": "हर जगह चार",
    "Evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo.":
        "इसी तरह बाकी दो गणनाएँ और सह-उत्पत्ति का खंड भी करना चाहिए।",
    "Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.":
        "इसी तरह बाकी दो गणनाएँ और आश्रय का खंड भी करना चाहिए।",
    "Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.":
        "इसी तरह बाकी दो गणनाएँ और जुड़ाव का खंड भी करना चाहिए।",
    "paṭiccasadisaṃ": "निर्भरता के खंड के समान",
    "paṭiccasadisā": "निर्भरता के खंड के समान",
    "Cakkaṃ. Evaṃ nava pañhā kātabbā.": "चक्र। इसी तरह नौ प्रश्न करने चाहिए।",
    "evaṃ nahetupañhā cattāri kātabbā.": "इसी तरह मूल-कारण के अभाव वाले चार प्रश्न करने चाहिए।",
    "arūpe dosamūlakaṃ natthi": "अभौतिक लोक में द्वेष से शुरू होने वाली शृंखला नहीं है",
    "evaṃ navapi pañhā kātabbā": "इसी तरह नौ के नौ प्रश्न करने चाहिए",
    "Evaṃ sabbe paccayā kātabbā.": "इसी तरह सभी कारण करने चाहिए।",
    "Ārammaṇapaccaye nokilesamūle pañca viññāṇā kātabbā.":
        "विषय-कारण में, मन के क्लेश रूपी न होने वाले पद से शुरू होने वाली शृंखला में पाँच प्रकार की चेतना शामिल करनी चाहिए।",
    "ārammaṇādhipatiyeva": "केवल विषय रूपी प्रधानता",
    "saṃkhittaṃ. Vitthāretabbaṃ.": "संक्षिप्त। विस्तार करना चाहिए।",
    "saṃkhittaṃ. Sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.":
        "संक्षिप्त। सह-उत्पत्ति सह-उत्पत्ति के समान है, पूर्व-उत्पत्ति पूर्व-उत्पत्ति के समान है।",
    "sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.":
        "सह-उत्पत्ति सह-उत्पत्ति के समान है, पूर्व-उत्पत्ति पूर्व-उत्पत्ति के समान है।",
    "anulomamātikā kātabbā": "सकारात्मक क्रम की मूल सूची करनी चाहिए",
    "Yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.":
        "जैसे लौकिक परिघटनाओं वाला दो का वर्गीकरण है, वैसे ही, बिना किसी अंतर के।",
    "yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.":
        "जैसे लौकिक परिघटनाओं वाला दो का वर्गीकरण है, वैसे ही, बिना किसी अंतर के।",
}

_KD = "मन के क्लेश वाले दो के वर्गीकरण के समान"
_DD = "सत्य-दर्शन से छोड़े जाने वाले दो के वर्गीकरण के समान"
_DHD = "सत्य-दर्शन से छोड़े जाने वाले मूलों वाले दो के वर्गीकरण के समान"
_SVD = "आरंभिक विचार वाले दो के वर्गीकरण"
_SPD = "उल्लास वाले दो के वर्गीकरण"
_ARD = "अभौतिक लोक वाले दो के वर्गीकरण के समान"
_NN = "बिना किसी अंतर के"
_SIX = "निर्भरता का खंड, सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड"
NOTE_X.update({
    "anulomamātikā kātabbā": "सकारात्मक क्रम की मूल सूची के अनुसार करना चाहिए",
    "anulomamātikā vitthāretabbā": "सकारात्मक क्रम की मूल सूची का विस्तार करना चाहिए",
    "anulomamātikā": "सकारात्मक क्रम की मूल सूची",
    "anulomamātikā gahetabbā": "सकारात्मक क्रम की मूल सूची लेनी चाहिए",
    "anulomaṃ": "सकारात्मक क्रम", "paccanīyaṃ": "नकारात्मक क्रम",
    "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान", "paṭiccavārasadisā": "निर्भरता के खंड के समान",
    "Sahajātavāro paṭiccavārasadiso.": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।",
    "Vatthupurejātaṃ saṃkhittaṃ.": "आधार रूपी पूर्व-उत्पत्ति संक्षिप्त है।",
    "Saṃkhittaṃ. Vatthupurejātaṃ saṃkhittaṃ.": "संक्षिप्त। आधार रूपी पूर्व-उत्पत्ति संक्षिप्त है।",
    "yāva asaññasattā kātabbā": "पहचान-रहित प्राणियों तक करना चाहिए",
    "yāva asaññasattāpi": "पहचान-रहित प्राणियों तक भी",
    "yāva asaññasattā, itare pañcapi pañhā, anulomaṃ kātabbaṃ":
        "पहचान-रहित प्राणियों तक, बाकी पाँचों प्रश्न, सकारात्मक क्रम करना चाहिए",
    "yāva ajjhattikaṃ mahābhūtaṃ": "आंतरिक महाभूत तक",
    "paṭisandhiyāpi dve": "पुनर्जन्म में भी दो",
    "tīṇi upanissayā": "तीन प्रबल आश्रय", "tīṇipi upanissayā": "तीनों प्रबल आश्रय",
    "tīṇi upanissayā dutiyagamanasadisā": "तीन प्रबल आश्रय, दूसरे प्रसंग के समान",
    "tīṇipi upanissayā sabbattha kātabbā": "तीनों प्रबल आश्रय हर जगह करने चाहिए",
    "Kilesasampayuttadukaṃ saṃkiliṭṭhadukasadisaṃ, ninnānākaraṇaṃ.":
        f"क्लेशों से जुड़ाव वाला दो का वर्गीकरण क्लेशों से मलिन परिघटनाओं वाले दो के वर्गीकरण के समान है, {_NN}।",
    "Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kilesadukasadisā. Ninnānākaraṇaṃ. Āmasanaṃ nānaṃ.":
        f"इसी तरह {_SIX} भी {_KD} हैं। {_NN}। केवल उल्लेख भिन्न है।",
    "evaṃ cattāri, kilesadukasadisaṃ.": f"इसी तरह चार, {_KD}।",
    "itare dve kilesadukasadisā, ghaṭanārammaṇāpi kilesadukasadisā":
        f"बाकी दो {_KD} हैं, विषय-कारण के संयोजन भी {_KD} हैं",
    "Itare dvepi kilesadukasadisā. Ghaṭanādhipatipi.": f"बाकी दोनों भी {_KD} हैं। प्रधानता-कारण के संयोजन भी।",
    "kilesadukasadisā": _KD,
    "Itare dve anantarā kilesadukasadisā, ninnānākaraṇā. Ghaṭanānantarampi sabbe paccayā kilesadukasadisā, ninnānākaraṇā. Upanissaye lokuttaraṃ natthi, idaṃ dukaṃ kilesadukasadisaṃ, ninnānākaraṇaṃ.":
        f"निकटता-कारण के बाकी दो प्रश्न {_KD} हैं, {_NN}। निकटता-कारण के संयोजन और सभी कारण भी {_KD} हैं, {_NN}। "
        f"प्रबल आश्रय-कारण में लोकोत्तर नहीं है, यह दो का वर्गीकरण {_KD} है, {_NN}।",
    "Evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.":
        "इसी तरह बाकी दो गणनाएँ, सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी "
        "निर्भरता के खंड के समान हैं।",
    "Itarepi tīṇi kātabbā.": "बाकी तीन भी करने चाहिए।",
    "Dve adhipati tīṇipi kātabbā, itare dvepi tīṇi kātabbā.":
        "दोनों प्रधानताओं के तीनों प्रश्न करने चाहिए, बाकी दोनों के भी तीन करने चाहिए।",
    "navapi kātabbā, āvajjanāpi vuṭṭhānampi natthi":
        "नौ के नौ करने चाहिए, मन को विषय की ओर मोड़ना भी और बाहर आना भी नहीं है",
    "purejātapaccayo pacchājātapaccayopi natthi": "पूर्व-उत्पत्ति-कारण और पश्चात्-उत्पत्ति-कारण भी नहीं है",
    "Navapi, tīṇiyeva padā kātabbā.": "नौ के नौ, केवल तीन ही पद करने चाहिए।",
    "Kilesasaṃkiliṭṭhadukasadisaṃ ninnānākaraṇaṃ, sabbe vārā.":
        f"मन के क्लेश और क्लेशों से मलिन परिघटनाओं वाले दो के वर्गीकरण के समान, {_NN}, सभी खंड।",
    "Itare dve gaṇanāpi sahajātavāropi kātabbo.": "बाकी दो गणनाएँ और सह-उत्पत्ति का खंड भी करना चाहिए।",
    "Itare dve gaṇanāpi nissayavāropi kātabbo.": "बाकी दो गणनाएँ और आश्रय का खंड भी करना चाहिए।",
    "saṃkhittaṃ, purejātasadisaṃ": "संक्षिप्त, पूर्व-उत्पत्ति के समान",
    "yathā dassanadukaṃ, evaṃ vitthāretabbaṃ, ninnānākaraṇaṃ":
        f"जैसे सत्य-दर्शन से छोड़े जाने वाला दो का वर्गीकरण है, वैसे ही विस्तार करना चाहिए, {_NN}",
    "Paccayavārapaccanīye nahetupaccaye uddhaccasahagate tīṇi, moho uddharitabbo. Sabbepi vārā dassanadukasadisā, uddhaccapaccanīyampi nānaṃ.":
        "कारण के खंड के नकारात्मक क्रम में, मूल-कारण के अभाव में, बेचैनी के साथ होने वाले में तीन, मोह को निकालना चाहिए। "
        f"सभी खंड भी {_DD} हैं, बेचैनी वाला नकारात्मक क्रम भी भिन्न है।",
    "dassanadukasadisā bhāvanā ninnānākaraṇā": f"{_DD}, मानसिक अभ्यास वाला {_NN}",
    "Sabbapaccayā dassanadukasadisā, bhāvanā ninnānākaraṇā.":
        f"सभी कारण {_DD} हैं, मानसिक अभ्यास वाला {_NN}।",
    "Paccanīyavibhaṅgo dassanadukasadiso vibhajitabbo. Evaṃ tīṇi gaṇanāpi gaṇetabbā.":
        f"नकारात्मक क्रम में {_DD} विश्लेषण करना चाहिए। इसी तरह तीनों गणनाएँ भी गिननी चाहिए।",
    "paṭiccasadisaṃ, saṃkhittaṃ": "निर्भरता के खंड के समान, संक्षिप्त",
    "Sampayuttavāro saṃsaṭṭhavārasadiso.": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है।",
    "Avasesesu dvīsu anantarūpanissayo, pakatūpanissayo.":
        "बाकी दो में निकटता रूपी प्रबल आश्रय, स्वाभाविक प्रबल आश्रय।",
    "dassanena pahātabbahetukadukasadisā": _DHD,
    "ārabbha dassanena pahātabbahetukadukasadisā": f"विषय बनाने के मामले में {_DHD}",
    "Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi dassanena pahātabbahetukadukasadisā. Uddhaccasahagato moho vicikicchāsahagatamohaṭṭhāne ṭhapetabbo.":
        f"इसी तरह {_SIX} भी {_DHD} हैं। बेचैनी के साथ होने वाले मोह को संशय के साथ होने वाले मोह के स्थान पर रखना चाहिए।",
    "Anantarapaccaye nabhāvanāya pahātabbahetukakāraṇā vicikicchāsahagato moho na kātabbo, uddhaccasahagato moho kātabbo.":
        "निकटता-कारण में, मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित होने के कारण, संशय के साथ होने वाला मोह नहीं करना चाहिए, "
        "बेचैनी के साथ होने वाला मोह करना चाहिए।",
    "nabhāvanāya pahātabbabhājanakāraṇe nānākkhaṇikā labbhati ":
        "मानसिक अभ्यास से न छोड़े जाने वाले के विभाजन के कारण भिन्न क्षण लागू होता है",
    "Saṃkhittaṃ. Yathā dassanena pahātabbahetukadukaṃ evaṃ bhāvanāya pahātabbahetukapaccayāpi paccanīyāpi vibhāgopi gaṇanāpi ninnānākaraṇā.":
        "संक्षिप्त। जैसे सत्य-दर्शन से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण है, वैसे ही मानसिक अभ्यास से छोड़े जाने वाले मूलों वाले "
        f"वर्गीकरण के कारण भी, नकारात्मक क्रम भी, विभाजन भी और गणनाएँ भी {_NN} हैं।",
    "Parantena sakabhaṇḍachandarāgopi kātabbo.": "आगे “अपनी वस्तु के प्रति चाह-राग” भी करना चाहिए।",
    'Parantena "sakabhaṇḍachandarāgo"ti kātabbaṃ.': "आगे “अपनी वस्तु के प्रति चाह-राग” करना चाहिए।",
    "Savitakkamūlakā avasesā dve pañhā kātabbā, ahetukaṃ ninnānaṃ.":
        f"आरंभिक विचार वाले पद से शुरू होने वाले शेष दो प्रश्न करने चाहिए, मूल से रहित, {_NN}।",
    'Saṃkhittaṃ. Hetupaccayasadisaṃ. "Ahetuka"nti niyāmetabbaṃ.':
        "संक्षिप्त। मूल-कारण के समान। “मूल से रहित” निश्चित करना चाहिए।",
    "Avasesā dve pañhā hetupaccayasadisā ninnānā, ahetukanti niyāmetabbaṃ.":
        f"शेष दो प्रश्न मूल-कारण के समान हैं, {_NN}, “मूल से रहित” निश्चित करना चाहिए।",
    "paṭisandhiyāpi pavattisadisāyeva": "पुनर्जन्म में भी जीवन-काल के समान ही",
    "paṭisandhikkhaṇe dve kātabbā": "पुनर्जन्म के क्षण में दो करने चाहिए",
    "tīṇi, paṭisandhiyāpi": "तीन, पुनर्जन्म में भी",
    'Nava pañhā kātabbā. "Ahetukā"ti niyāmetabbā tīṇiyeva. Moho uddharitabbo, yathā paṭiccavāre hetupaccayasadisāyeva pañhā pañcaviññāṇā atirekā moho vitakkaṃ.':
        "नौ प्रश्न करने चाहिए। “मूल से रहित” केवल तीन में निश्चित करना चाहिए। मोह को निकालना चाहिए, जैसे निर्भरता के खंड में "
        "मूल-कारण के समान ही प्रश्न हैं, पाँच प्रकार की चेतना अतिरिक्त है, मोह, आरंभिक विचार।",
    "Evaṃ cha pañhā kātabbā anulomasadisā, ahetukāti niyāmetabbā, tīṇiyeva, moho uddharitabbo.":
        "इसी तरह छह प्रश्न सकारात्मक क्रम के समान करने चाहिए, “मूल से रहित” निश्चित करना चाहिए, तीन ही, मोह को निकालना चाहिए।",
    "heṭṭhā likhitaṃ lekhaṃ iminā kāraṇena daṭṭhabbaṃ": "नीचे लिखे गए लेख को इसी कारण से देखना चाहिए",
    "dutiyavāre likhitapadā sabbe kātabbā": "दूसरे खंड में लिखे गए सभी पद करने चाहिए",
    "tīṇi, pacchājātā": "तीन, पश्चात्-उत्पत्ति",
    "Evaṃ cattāri, sahajātāpi nānākkhaṇikāpi kātabbā.":
        "इसी तरह चार, सह-उत्पत्ति वाले भी और भिन्न क्षण वाले भी करने चाहिए।",
    "ekaṃ, paṭiccasadisaṃ": "एक, निर्भरता के खंड के समान",
    "paṭisandhikkhaṇe sahajātāpi dvepi kātabbā": "पुनर्जन्म के क्षण में सह-उत्पत्ति वाले दोनों भी करने चाहिए",
    "paṭisandhikkhaṇe, tīṇi": "पुनर्जन्म के क्षण में, तीन",
    "Yathā savitakkadukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ. Idha magge cattāri kātabbāni. Savicāraduke imaṃ nānākaraṇaṃ.":
        f"जैसे आरंभिक विचार वाला दो का वर्गीकरण है, वैसे ही करना चाहिए, {_NN}। यहाँ मार्ग-कारण में चार करने चाहिए। "
        "सतत विचार वाले दो के वर्गीकरण में यही अंतर है।",
    "Yathā savitakkadukaṃ sabbattha, evaṃ sappītikadukaṃ kātabbaṃ, sabbattha pavattipaṭisandhi navapi pañhā.":
        "जैसे हर जगह आरंभिक विचार वाला दो का वर्गीकरण है, वैसे ही उल्लास वाला दो का वर्गीकरण करना चाहिए, "
        "हर जगह जीवन-काल और पुनर्जन्म में नौ के नौ प्रश्न।",
    "Saṃkhittaṃ. Yathā savitakkaduke anulomapaccayavāraṃ, evaṃ pavattipaṭisandhi nava pañhā paripuṇṇā pīti ninnānākaraṇā.":
        f"संक्षिप्त। जैसे {_SVD} में सकारात्मक क्रम का कारण का खंड है, वैसे ही जीवन-काल और पुनर्जन्म में नौ प्रश्न परिपूर्ण हैं, "
        f"उल्लास {_NN}।",
    "Pavattipaṭisandhi kātabbā paṭiccavārasadisā, yāva asaññasattā.":
        "जीवन-काल और पुनर्जन्म निर्भरता के खंड के समान करने चाहिए, पहचान-रहित प्राणियों तक।",
    "Anulomasadisā nava pañhā, pavattiyeva paṭisandhi natthi, ekoyeva moho.":
        "सकारात्मक क्रम के समान नौ प्रश्न, केवल जीवन-काल में, पुनर्जन्म नहीं है, केवल एक ही मोह।",
    "evaṃ pītisahagatadukaṃ vitthāretabbaṃ, sappītikadukasadisaṃ ninnānākaraṇaṃ, āmasanaṃ ninnānaṃ.":
        f"इसी तरह उल्लास के साथ होने वाले दो के वर्गीकरण का विस्तार करना चाहिए, {_SPD} के समान, {_NN}, उल्लेख भी {_NN}।",
    "Evaṃ sukhasahagatadukaṃ vitthāretabbaṃ, yathā sappītikadukassa anulomapaṭiccavāro.":
        f"इसी तरह सुख के साथ होने वाले दो के वर्गीकरण का विस्तार करना चाहिए, जैसे {_SPD} का सकारात्मक क्रम वाला निर्भरता का खंड है।",
    "Yathā sappītike nahetupaccayasadisaṃ, ninnānaṃ sabbatthameva nava pañhā.":
        f"जैसे उल्लास वाले में, मूल-कारण के अभाव के समान, {_NN}, हर जगह नौ प्रश्न।",
    "Evaṃ itare dve gaṇanāpi sahajātavāropi paṭiccavārasadisā. Paccayavāre pavattipi paṭisandhipi vitthāretabbā, yathā sappītikadukapaccayavārapaccanīyepi pavatte vatthu ca vitthāretabbaṃ, yathā sappītikaduke ekoyeva moho, evaṃ itare dve gaṇanāpi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi yathā sappītikadukaṃ, evaṃ kātabbaṃ.":
        "इसी तरह बाकी दो गणनाएँ और सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान हैं। कारण के खंड में जीवन-काल का भी और पुनर्जन्म का भी "
        f"विस्तार करना चाहिए, जैसे {_SPD} के कारण के खंड के नकारात्मक क्रम में भी जीवन-काल में आधार का भी विस्तार करना चाहिए, "
        f"जैसे {_SPD} में केवल एक ही मोह है, वैसे ही बाकी दो गणनाएँ, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी, "
        "जैसे उल्लास वाला दो का वर्गीकरण है, वैसे ही करना चाहिए।",
    "Mūlaṃ. Tīṇipi sappītikadukasadisā.": f"मूल वाक्य। तीनों भी {_SPD} के समान हैं।",
    "Ārammaṇepi adhipatiyāpi sappītikadukasadisā, sukhanti nānākaraṇaṃ.":
        f"विषय-कारण में भी और प्रधानता-कारण में भी {_SPD} के समान, “सुख” यही अंतर है।",
    "Cha kammāni cattāri sahajātāpi nānākkhaṇikāpi kātabbā, dve nānākkhaṇikā.":
        "छह कर्म-कारण, चार सह-उत्पत्ति वाले भी और भिन्न क्षण वाले भी करने चाहिए, दो भिन्न क्षण वाले।",
    "sahajātāpi nānākkhaṇikāpi kātabbā… dve nānākkhaṇikā":
        "सह-उत्पत्ति वाले भी और भिन्न क्षण वाले भी करने चाहिए… दो भिन्न क्षण वाले",
    "saṃkhittaṃ. Savitakkadukasadisaṃ kātabbaṃ.": f"संक्षिप्त। {_SVD} के समान करना चाहिए।",
    "dutiyavārasadisaṃ": "दूसरे खंड के समान",
    "dutiyagamanasadisaṃ": "दूसरे प्रसंग के समान",
    "Evaṃ paccanīyavibhaṅgopi gaṇanāpi sappītikadukasadisaṃ kātabbaṃ, yadipi vimati atthi anulomaṃ passitvā gaṇetabbaṃ.":
        f"इसी तरह नकारात्मक क्रम का विश्लेषण भी और गणनाएँ भी {_SPD} के समान करना चाहिए, "
        "यदि कोई संदेह हो तो सकारात्मक क्रम को देखकर गिनना चाहिए।",
    "Paccanīyavibhaṅgagaṇanāpi savitakkadukasadisā. Yadipi na sameti imaṃ anulomaṃ paccavekkhitvā gaṇetabbaṃ, itare dve gaṇanā gaṇetabbā.":
        f"नकारात्मक क्रम का विश्लेषण और गणनाएँ भी {_SVD} के समान हैं। यदि मेल न खाए तो इस सकारात्मक क्रम को जाँचकर गिनना चाहिए, "
        "बाकी दो गणनाएँ गिननी चाहिए।",
    "Imāni paccayāni sappītikakaraṇena vibhajitabbāni.": "इन कारणों का उल्लास वाले की तरह विश्लेषण करना चाहिए।",
    "Evaṃ cattāri pañhā yathā savitakkadukassa.": f"इसी तरह चार प्रश्न, जैसे {_SVD} के हैं।",
    "Evaṃ navapi pañhā pavattipaṭisandhiyo yathā savitakkadukassa evaṃ kātabbā. Tīṇiyeva moho, pavatte vatthupi kātabbā.":
        f"इसी तरह नौ के नौ प्रश्न, जीवन-काल और पुनर्जन्म, जैसे {_SVD} के हैं, वैसे ही करने चाहिए। "
        "तीन में ही मोह, जीवन-काल में आधार भी करना चाहिए।",
    "Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo, saṃsaṭṭhavārepi dve pañhā kātabbā sabbattha.":
        "इसी तरह बाकी दो गणनाएँ और आश्रय का खंड भी करना चाहिए, घुले-मिले होने के खंड में भी हर जगह दो प्रश्न करने चाहिए।",
    "Evaṃ pañca pañhā yathā savitakkaduke evaṃ kātabbā.": f"इसी तरह पाँच प्रश्न, जैसे {_SVD} में हैं, वैसे ही करने चाहिए।",
    "Avasesā gaṇanāpi sahajātavāropi kātabbo.": "शेष गणनाएँ और सह-उत्पत्ति का खंड भी करना चाहिए।",
    "Avasesā tīṇi pākatikā. Saṃkhittaṃ.": "शेष तीन सामान्य हैं। संक्षिप्त।",
    "Cattāri sahajātā nānākkhaṇikā kātabbā, dve nānākkhaṇikā ca.":
        "चार सह-उत्पत्ति वाले और भिन्न क्षण वाले करने चाहिए, और दो भिन्न क्षण वाले।",
    "Yathā cūḷantaraduke lokiyadukaṃ. Evaṃ imampi dukaṃ kātabbaṃ, ninnānākaraṇaṃ.":
        "जैसे बीच के छोटे दो-दो के वर्गीकरणों में लौकिक परिघटनाओं वाला दो का वर्गीकरण है। इसी तरह इस दो के वर्गीकरण को भी "
        f"करना चाहिए, {_NN}।",
    "Yāva ajjhattikā mahābhūtā. Yathā cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.":
        "आंतरिक महाभूतों तक। जैसे बीच के छोटे दो-दो के वर्गीकरणों में, लौकिक परिघटनाओं वाले दो के वर्गीकरण के समान, "
        f"{_NN}।",
    "Nakāmāvacaraṃ paṭiccavārasadisaṃ ninnānaṃ, idha sabbe mahābhūtā kātabbā.":
        f"इंद्रिय-सुखों के लोक से संबंधित न होने वाला निर्भरता के खंड के समान, {_NN}, यहाँ सभी महाभूत करने चाहिए।",
    "Pañca pañhā arūpāvacaradukasadisā, anulomapaṭiccasadisā.":
        f"पाँच प्रश्न {_ARD}, सकारात्मक क्रम वाले निर्भरता के खंड के समान।",
    'Yathā sappītikadukaṃ evaṃ ārammaṇampi adhipatipi vitthāretabbā, "upekkhā"ti nānaṃ.':
        "जैसे उल्लास वाला दो का वर्गीकरण है, वैसे ही विषय-कारण का भी और प्रधानता-कारण का भी विस्तार करना चाहिए, “समभाव” भिन्न है।",
    'yathā savitakkadukasadisaṃ paccayavāre nānākaraṇaṃ. "Upekkha"nti navapi pañhā kātabbā, paṭisandhipavattipi vatthupi.':
        f"जैसे {_SVD} के समान, कारण के खंड में अंतर है। “समभाव” के साथ नौ के नौ प्रश्न करने चाहिए, "
        "पुनर्जन्म और जीवन-काल भी, आधार भी।",
    "Yathā savitakkadukaṃ sampayuttavāro evaṃ kātabbo.": f"जैसे {_SVD} का जुड़ाव का खंड है, वैसे ही करना चाहिए।",
    "yathā arūpāvacaradukassa paccayavāropi evaṃ kātabbo":
        "जैसे अभौतिक लोक वाले दो के वर्गीकरण का कारण का खंड है, वैसे ही करना चाहिए",
    'suddhake arūpamissake ca "vipāka"nti niyāmetabbaṃ, rūpamissake natthi. Saṃkhittaṃ':
        "शुद्ध पद में और अभौतिक-मिश्रित पद में “कर्म-फल रूपी” निश्चित करना चाहिए, भौतिक-मिश्रित में नहीं है। संक्षिप्त",
    'suddhike arūpe ca missake ca "vipāka"nti niyāmetabbaṃ':
        "शुद्ध पद में, अभौतिक लोक में और मिश्रित में “कर्म-फल रूपी” निश्चित करना चाहिए",
    "arūpadukasadisaṃ": _ARD, "arūpadukasadisā": _ARD, "arūpāvacaradukasadisaṃ": _ARD,
    "arūpadukasadisaṃ, cattāri": f"{_ARD}, चार",
    "arūpadukasadisā kātabbā": f"{_ARD} करने चाहिए",
    "arūpadukasadisā kātabbā, āmasanā nānāpadāyeva": f"{_ARD} करने चाहिए, केवल पदों का उल्लेख भिन्न है",
    "niyyānikadukasadisā ninnānākaraṇā": f"मुक्ति की ओर ले जाने वाले दो के वर्गीकरण के समान, {_NN}",
    "saṃkhittaṃ. Pañcapi pañhā kātabbā. Yathā niyyānikadukaṃ evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kātabbā, ninnānākaraṇaṃ āmasanaṃ nānaṃ":
        f"संक्षिप्त। पाँचों प्रश्न करने चाहिए। जैसे मुक्ति की ओर ले जाने वाला दो का वर्गीकरण है, वैसे ही {_SIX} भी करना चाहिए, "
        f"{_NN}, उल्लेख भिन्न है",
    "saṃkhittaṃ. Mūlaṃ. Itarepi pañhā kātabbā": "संक्षिप्त। मूल वाक्य। बाकी प्रश्न भी करने चाहिए",
    "paṭiccasadisā. Mūlaṃ kātabbaṃ.": "निर्भरता के खंड के समान। मूल वाक्य से शुरू करना चाहिए।",
    "ghaṭanārammaṇā tīṇipi kātabbā": "विषय-कारण के संयोजन तीनों करने चाहिए",
    "ghaṭanūpanissayāpi tīṇipi kātabbā": "प्रबल आश्रय-कारण के संयोजन भी तीनों करने चाहिए",
    "itare dve pākatikā": "बाकी दो सामान्य हैं",
    "kusalattikasadisaṃ": "हितकर वाले तीन के वर्गीकरण के समान",
    "vippayuttasadisaṃ": "अलगाव-कारण के समान", "purejātasadisaṃ": "पूर्व-उत्पत्ति के समान",
    "sappītikadukasadisā": f"{_SPD} के समान",
    "Sappītikadukasadisaṃ, anulome navapi pañhā.": f"{_SPD} के समान, सकारात्मक क्रम में नौ के नौ प्रश्न।",
    "Evaṃ paccanīyavibhaṅgopi itare tīṇi gaṇanāpi sappītikadukasadisā kātabbā.":
        f"इसी तरह नकारात्मक क्रम का विश्लेषण भी और बाकी तीन गणनाएँ भी {_SPD} के समान करनी चाहिए।",
})

# extra noun phrases
NOM_X.update({
    "kiriyaṃ": ("केवल क्रिया रूपी मन", "ms"),
    "dibbaṃ cakkhuṃ": ("दिव्य आँख", "fs"), "dibbaṃ sotadhātuṃ": ("दिव्य कान का तत्व", "ms"),
    "iddhividhañāṇaṃ": ("अलौकिक शक्तियों का ज्ञान", "ms"), "cetopariyañāṇaṃ": ("दूसरों के मन को जानने का ज्ञान", "ms"),
    "pubbenivāsānussatiñāṇaṃ": ("पूर्व जन्मों के अनुस्मरण का ज्ञान", "ms"),
    "yathākammūpagañāṇaṃ": ("प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान", "ms"),
    "anāgataṃsañāṇaṃ": ("भविष्य को जानने का ज्ञान", "ms"),
    "kāyikaṃ sukhaṃ": ("शारीरिक सुख", "ms"), "kāyikaṃ dukkhaṃ": ("शारीरिक दुःख", "ms"),
    "utu": ("तापमान", "ms"), "bhojanaṃ": ("भोजन", "ms"),
    "nevasaññānāsaññāyatanaṃ": ("न पहचान न अ-पहचान का क्षेत्र", "ms"),
})
OBL_X.update({
    "taṃ": "उस",
    "pahīne kilese": "छोड़े जा चुके मन के क्लेशों", "vikkhambhite kilese": "दबाए जा चुके मन के क्लेशों",
    "pubbe samudāciṇṇe kilese": "पहले बार-बार उठे मन के क्लेशों", "pubbe samudāciṇṇe": "पहले बार-बार उठे",
    "dibbaṃ cakkhuṃ": "दिव्य आँख", "dibbaṃ sotadhātuṃ": "दिव्य कान के तत्व",
    "iddhividhañāṇaṃ": "अलौकिक शक्तियों के ज्ञान", "cetopariyañāṇaṃ": "दूसरों के मन को जानने के ज्ञान",
    "pubbenivāsānussatiñāṇaṃ": "पूर्व जन्मों के अनुस्मरण के ज्ञान",
    "yathākammūpagañāṇaṃ": "प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान",
    "anāgataṃsañāṇaṃ": "भविष्य को जानने के ज्ञान",
    "pubbe suciṇṇāni": "पहले भली-भाँति किए गए कार्यों", "nibbānaṃ": "निर्वाण", "vodānaṃ": "शुद्धि",
    "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhaṃ": "जीभ", "kāyaṃ": "शरीर", "rūpe": "दृश्य रूपों",
    "sadde": "ध्वनियों", "gandhe": "गंधों", "rase": "स्वादों", "phoṭṭhabbe": "स्पर्शों",
})
DAT_X.update({
    "dibbassa cakkhussa": "दिव्य आँख", "dibbāya sotadhātuyā": "दिव्य कान के तत्व",
    "pañcannaṃ viññāṇānaṃ": "पाँच प्रकार की चेतना", "ariyānaṃ": "आर्यों",
})
PREFIX_X.update({
    "nirodhā vuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में",
    "paṭisandhikkhaṇe": "पुनर्जन्म के क्षण में", "ahetukapaṭisandhikkhaṇe": "मूल से रहित पुनर्जन्म के क्षण में",
})
_GIFT = "दान देकर, सदाचार ग्रहण करके, उपवास-व्रत का पालन करके"
CLAUSE_X.update({
    "paccanīyaṃ": "नकारात्मक क्रम",
    "vipassati": "अंतर्दृष्टि से देखता है", "vipassanti": "अंतर्दृष्टि से देखते हैं",
    "vipassati assādeti abhinandati": "अंतर्दृष्टि से देखता है, उनका रस लेता है, उनमें आनंद लेता है",
    "assādeti abhinandati": "उसका रस लेता है, उसमें आनंद लेता है",
    "abhiññaṃ": "उच्च ज्ञान", "vipassanaṃ": "अंतर्दृष्टि", "maggaṃ": "मार्ग", "phalaṃ": "फल", "paññā": "प्रज्ञा",
    "maggā": "मार्ग से", "jhānaṃ": "ध्यान",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है", "sīlaṃ samādiyati": "सदाचार ग्रहण करता है",
    "uposathakammaṃ katvā": "उपवास-व्रत का पालन करके", "dānaṃ datvā": "दान देकर",
    "dānaṃ datvā sīlaṃ": "दान देकर, सदाचार",
    "uposathakammaṃ katvā taṃ paccavekkhati": "उपवास-व्रत का पालन करके उस पर पुनः विचार करता है",
    "uposathakammaṃ katvā taṃ paccavekkhati assādeti abhinandati":
        "उपवास-व्रत का पालन करके उस पर पुनः विचार करता है, उसका रस लेता है, उसमें आनंद लेता है",
    "pubbe suciṇṇāni paccavekkhati assādeti abhinandati":
        "पहले भली-भाँति किए गए कार्यों पर पुनः विचार करता है, उनका रस लेता है, उनमें आनंद लेता है",
    "pubbe suciṇṇāni garuṃ katvā paccavekkhati assādeti abhinandati":
        "पहले भली-भाँति किए गए कार्यों को महत्व देकर पुनः विचार करता है, उनका रस लेता है, उनमें आनंद लेता है",
    "paccavekkhati assādeti abhinandati": "पुनः विचार करता है, उसका रस लेता है, उसमें आनंद लेता है",
    "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है", "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है",
    "maggaṃ uppādeti": "मार्ग उत्पन्न करता है", "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "adinnaṃ ādiyati": "बिना दिया हुआ लेता है", "nigamaghātaṃ karoti": "कस्बे पर हमला करता है",
    "musā": "झूठ", "pisuṇaṃ": "चुगली", "samphaṃ": "व्यर्थ", "sandhiṃ": "सेंध", "nillopaṃ": "डाका",
    "ekāgārikaṃ": "एक ही घर में डाका", "paripanthe": "राह में घात", "paradāraṃ": "पराई स्त्री",
    "gāmaghātaṃ": "गाँव पर हमला",
    "ariyā maggaṃ upanissāya anuppannaṃ samāpattiṃ uppādenti":
        "आर्य मार्ग के प्रबल आश्रय से उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं",
    "uppannaṃ samāpajjanti": "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं",
    "ārammaṇādhipati sahajātādhipati": "विषय रूपी प्रधानता, सह-उत्पत्ति रूपी प्रधानता",
    "taṃ ārabbha": "उसे विषय बनाकर", "taṃ garuṃ katvā": "उसे महत्व देकर",
    "sekkhā gotrabhuṃ garuṃ katvā paccavekkhanti": "सीखने के चरण वाले व्यक्ति गोत्र-परिवर्तन को महत्व देकर पुनः विचार करते हैं",
    "dibbena": "दिव्य", "ariyā": "आर्य",
})

_CR = {"mātughātikamm": "माता की हत्या", "pitughātikamm": "पिता की हत्या", "arahantaghātikamm": "अर्हत् की हत्या",
       "ruhiruppādakamm": "बुद्ध का खून बहाने", "saṅghabhedakamm": "संघ में फूट डालने"}
for _p, _h in _CR.items():
    DAT_X[_p + "assa"] = _h + " के कर्म"
    NOM_X[_p + "aṃ"] = (_h + " का कर्म", "ms")
DAT_X.update({
    "niyatamicchādiṭṭhiyā": "निश्चित ग़लत दृष्टि",
    "micchattaniyatānaṃ khandhānaṃ": "ग़लत दिशा में निश्चित समूहों",
    "atthapaṭisambhidāya": "अर्थ के विश्लेषणात्मक ज्ञान", "dhammapaṭisambhidāya": "शिक्षा के विश्लेषणात्मक ज्ञान",
    "niruttipaṭisambhidāya": "भाषा के विश्लेषणात्मक ज्ञान", "paṭibhānapaṭisambhidāya": "सूझ-बूझ के विश्लेषणात्मक ज्ञान",
    "ṭhānāṭhānakosallassa": "संभव और असंभव को जानने की कुशलता",
})
NOM_X.update({
    "taṃ vatthu": ("वह आधार", "ms"), "aniyatā micchādiṭṭhi": ("अनिश्चित ग़लत दृष्टि", "fs"),
    "rūpāvacarādhipati vipākaṃ": ("कर्म-फल रूपी, सूक्ष्म भौतिक लोक से संबंधित प्रधानता", "fs"),
    "kāyaviññāṇadhātu": ("शरीर की चेतना का तत्व", "ms"), "cittasamuṭṭhānaṃ": ("मन से उत्पन्न", "ms"),
    "parikammaṃ": ("प्रारंभिक तैयारी", "fs"), "purimā purimā nasukhasahagatā": ("पहले-पहले के सुख के साथ न होने वाले", "mp"),
})
OBL_X.update({
    "saṅkhāre": "निर्मित परिघटनाओं", "vikkhambhite": "दबाए जा चुके",
    "vicikicchāsahagataṃ uddhaccasahagataṃ upekkhaṃ": "संशय के साथ होने वाले या बेचैनी के साथ होने वाले समभाव",
})
PREFIX_X.update({"asaññasattānaṃ": "पहचान-रहित प्राणियों में"})
CLAUSE_X.update({
    "ekaṃyeva": "केवल एक", "uddhacca": "बेचैनी", "diṭṭhiṃ assādeti": "दृष्टि का रस लेता है",
    "paccavekkhati": "पुनः विचार करता है", "musā bhaṇati": "झूठ बोलता है",
    "saṅkhāre aniccato": "निर्मित परिघटनाओं को अनित्य",
    "yaṃ vatthuṃ āmasantassa micchattaniyatā khandhā uppajjanti":
        "जिस आधार को छूते हुए व्यक्ति में ग़लत दिशा में निश्चित समूह उत्पन्न होते हैं",
    "mātaraṃ jīvitā voropetvā": "माता की जान लेकर", "mātaraṃ jīvitā voropeti": "माता की जान लेता है",
    "saṅghaṃ bhinditvā tassa paṭighātatthāya dānaṃ deti": "संघ में फूट डालकर उसके प्रतिकार के लिए दान देता है",
    "maggo ariyānaṃ atthapaṭisambhidāya": "मार्ग आर्यों के अर्थ के विश्लेषणात्मक ज्ञान के लिए",
    "uposathakammaṃ katvā taṃ assādeti abhinandati": "उपवास-व्रत का पालन करके उसका रस लेता है, उसमें आनंद लेता है",
    "uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati": "उपवास-व्रत का पालन करके उसे महत्व देकर पुनः विचार करता है",
    "uposathakammaṃ katvā taṃ garuṃ katvā assādeti abhinandati":
        "उपवास-व्रत का पालन करके उसे महत्व देकर उसका रस लेता है, उसमें आनंद लेता है",
    # Pāli pieces where the source runs two clauses together without punctuation (rendered with a comma)
    "samāpattiṃ uppādeti dassanena pahātabbaṃ dosaṃ":
        "ध्यान-अवस्था उत्पन्न करता है, सत्य-दर्शन से छोड़े जाने वाले द्वेष",
    "samāpattiṃ uppādeti mānaṃ jappeti": "ध्यान-अवस्था उत्पन्न करता है, अहंकार पालता है",
    "sukhasahagataṃ cuticittañca sukhañca nasukhasahagatassa upapatticittassa sukhasahagataṃ bhavaṅgañca sukhañca āvajjanāya":
        "सुख के साथ होने वाला मृत्यु का मन और सुख, सुख के साथ न होने वाले जन्म के मन के लिए, सुख के साथ होने वाली "
        "जीवन-धारा और सुख, मन को विषय की ओर मोड़ने के लिए",
    "senāsanaṃ sukhañca sukhasahagatāya": "निवास-स्थान और सुख, सुख के साथ होने वाली",
    "ākāsānañcāyatanaṃ garuṃ katvā paccavekkhati viññāṇañcāyatanaṃ":
        "अनंत आकाश के क्षेत्र को महत्व देकर पुनः विचार करता है, अनंत चेतना का क्षेत्र",
    "nakāmāvacare khandhe garuṃ katvā assādeti abhinandati taṃ garuṃ katvā rāgo uppajjati":
        "इंद्रिय-सुखों के लोक से संबंधित न होने वाले समूहों को महत्व देकर उनका रस लेता है, उनमें आनंद लेता है, "
        "उसे महत्व देकर राग उत्पन्न होता है",
    "diṭṭhi uppajjati appītike khandhe ca pītiñca garuṃ katvā sappītikā khandhā ca pīti ca uppajjanti":
        "दृष्टि उत्पन्न होती है, उल्लास से रहित समूहों और उल्लास को महत्व देकर उल्लास वाले समूह और उल्लास उत्पन्न होते हैं",
    # Pāli comma slip inside one phrase (paññāya nabhāvanāya pahātabbassa, rāgassa)
    "paññāya nabhāvanāya pahātabbassa ¦ rāgassa": "प्रज्ञा के लिए और मानसिक अभ्यास से न छोड़े जाने वाले राग के लिए",
    "sakabhaṇḍe chandarāgo parabhaṇḍe chandarāgassa upanissayapaccayena paccayo":
        "अपनी वस्तु के प्रति चाह-राग, पराई वस्तु के प्रति चाह-राग के लिए प्रबल आश्रय-कारण के रूप में कारण होता है",
    "sakapariggahe chandarāgo parapariggahe chandarāgassa upanissayapaccayena paccayo":
        "अपने अधिकार की चीज़ों के प्रति चाह-राग, दूसरों के अधिकार की चीज़ों के प्रति चाह-राग के लिए "
        "प्रबल आश्रय-कारण के रूप में कारण होता है",
})

SLIPS_X = {"na sahajāte": "nasahajāte"}

LINE_X = {}

VARIANTS_X = {
    "{thīnaṃ (sī. syā.)}": ("वर्तनी-भेद", "आलस्य"),
}
