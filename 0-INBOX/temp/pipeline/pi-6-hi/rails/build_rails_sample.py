"""pi-6 (Yamaka) Pāli -> Hindi plain, RAILS: fixed formula strings and the builder of the sample.

Importable read-only by later agents:
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-hi\\rails")
    import build_rails_sample as S
Importing has no side effects. Running it as a script (python -I -X utf8 build_rails_sample.py) rebuilds
the sample files only: preamble.md, 1-mulayamaka.md and sample-1\\2-01-pali-sample.md / 2-01-sample.md.

Every Pāli line must be matched by a formula; an unknown line raises ValueError (no silent pass-through).
The same strings are listed for people in hi-rails-formulas.md.
"""
import re
import pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
HI_DIR = ROOT / "AI_translation" / "hindi" / "pi-6-hindi-plain-rails_split_chapters"
RAILS = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-6-hi" / "rails"

# =====================================================================================================
# 1. Book frame and chapter titles
# =====================================================================================================
NAMO = "उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन"
ABHIDHAMMA = "अभिधम्म पिटक में"
BOOK_TITLE = "प्रश्नों के जोड़े"
BOOK_END = "“प्रश्नों के जोड़े” ग्रंथ समाप्त।"           # Yamakapāḷi niṭṭhitā

CHAPTER_TITLES = {
    "Mūlayamakaṃ": "मूलों पर प्रश्नों के जोड़े",
    "Khandhayamakaṃ": "समूहों पर प्रश्नों के जोड़े",
    "Āyatanayamakaṃ": "इंद्रिय-क्षेत्रों पर प्रश्नों के जोड़े",
    "Dhātuyamakaṃ": "तत्वों पर प्रश्नों के जोड़े",
    "Saccayamakaṃ": "सत्यों पर प्रश्नों के जोड़े",
    "Saṅkhārayamakaṃ": "रचनाओं पर प्रश्नों के जोड़े",
    "Anusayayamakaṃ": "सुप्त प्रवृत्तियों पर प्रश्नों के जोड़े",
    "Cittayamakaṃ": "मन पर प्रश्नों के जोड़े",
    "Dhammayamakaṃ": "परिघटनाओं पर प्रश्नों के जोड़े",
    "Indriyayamakaṃ": "क्षमताओं पर प्रश्नों के जोड़े",
}
CHAPTER_END = "{title} पूरे हुए।"   # <X>yamakapāḷi niṭṭhitā / <X>yamakaṃ niṭṭhitaṃ

# =====================================================================================================
# 2. Headings (Pāli heading text without '#' and block ID -> Hindi). Keep the #-level of the source.
# =====================================================================================================
HEADINGS = {
    **CHAPTER_TITLES,
    "(Ka) uddeso": "(क) सूची",
    "(Kha) niddeso": "(ख) व्याख्या",
    # Mūlayamaka
    "Mūlavāro": "मूल का खंड",
    "Kusalā dhammā": "हितकर परिघटनाएँ",
    "(1) Mūlanayo": "(1) मूल की विधि",
    "(2) Mūlamūlanayo": "(2) मूल के मूल की विधि",
    "(3) Mūlakanayo": "(3) मूल पर आधारित होने की विधि",
    "(4) Mūlamūlakanayo": "(4) मूल के मूल पर आधारित होने की विधि",
    "Kusalā dhammā (1) mūlanayo": "हितकर परिघटनाएँ (1) मूल की विधि",
    "Akusalā dhammā (1) mūlanayo": "हानिकर परिघटनाएँ (1) मूल की विधि",
    "Abyākatā dhammā (1) mūlanayo": "नैतिक रूप से अनिर्धारित परिघटनाएँ (1) मूल की विधि",
    "Nāmā dhammā (1) mūlanayo": "मानसिक पक्ष की परिघटनाएँ (1) मूल की विधि",
    "2-10. Hetuvārādi": "2-10. हेतु का खंड आदि",
    # Paṇṇattivāra
    "Paṇṇattivāro": "शब्दावली का खंड",
    "Paṇṇattivāraniddesa": "शब्दावली के खंड की व्याख्या",
    "Padasodhanavāro": "शब्दों की जाँच का खंड",
    "Padasodhanamūlacakkavāro": "शब्दों की जाँच पर आधारित चक्र का खंड",
    "Suddhakhandhavāro": "केवल समूहों का खंड",
    "Suddhakhandhamūlacakkavāro": "केवल समूहों पर आधारित चक्र का खंड",
    "Suddhāyatanavāro": "केवल इंद्रिय-क्षेत्रों का खंड",
    "Suddhāyatanamūlacakkavāro": "केवल इंद्रिय-क्षेत्रों पर आधारित चक्र का खंड",
    "Suddhadhātuvāro": "केवल तत्वों का खंड",
    "Suddhadhātumūlacakkavāro": "केवल तत्वों पर आधारित चक्र का खंड",
    "Suddhasaccavāro": "केवल सत्यों का खंड",
    "Suddhasaccamūlacakkavāro": "केवल सत्यों पर आधारित चक्र का खंड",
    "Suddhasaṅkhāravāro": "केवल रचनाओं का खंड",
    "Suddhasaṅkhāramūlacakkavāro": "केवल रचनाओं पर आधारित चक्र का खंड",
    "Suddhadhammavāro": "केवल परिघटनाओं का खंड",
    "Suddhadhammamūlacakkavāro": "केवल परिघटनाओं पर आधारित चक्र का खंड",
    "Suddhindriyavāro": "केवल क्षमताओं का खंड",
    "Suddhindriyamūlacakkavāro": "केवल क्षमताओं पर आधारित चक्र का खंड",
    "(Ka) anulomaṃ": "(क) सकारात्मक",
    "(Kha) paccanīkaṃ": "(ख) नकारात्मक",
    # Pavattivāra
    "Pavattivāro 1. uppādavāro": "प्रक्रिया का खंड 1. उत्पन्न होने का खंड",
    "Pavatti 2. nirodhavāro": "प्रक्रिया 2. समाप्त होने का खंड",
    "Pavatti 3. uppādanirodhavāro": "प्रक्रिया 3. उत्पन्न होने और समाप्त होने का खंड",
    "Uppādavāro": "उत्पन्न होने का खंड",
    "Nirodhavāro": "समाप्त होने का खंड",
    "Uppādanirodhavāro": "उत्पन्न होने और समाप्त होने का खंड",
    "(1) Paccuppannavāro": "(1) वर्तमान का खंड",
    "(2) Atītavāro": "(2) अतीत का खंड",
    "(3) Anāgatavāro": "(3) भविष्य का खंड",
    "(4) Paccuppannātītavāro": "(4) वर्तमान और अतीत का खंड",
    "(5) Paccuppannānāgatavāro": "(5) वर्तमान और भविष्य का खंड",
    "(6) Atītānāgatavāro": "(6) अतीत और भविष्य का खंड",
    "Paccuppannavāro": "वर्तमान का खंड",
    "Atītavāro": "अतीत का खंड",
    "Anāgatavāro": "भविष्य का खंड",
    "Paccuppannātītavāro": "वर्तमान और अतीत का खंड",
    "Paccuppannānāgatavāro": "वर्तमान और भविष्य का खंड",
    "Atītānāgatavāro": "अतीत और भविष्य का खंड",
    "(Ka) anulomapuggalo": "(क) सकारात्मक: व्यक्ति",
    "(Kha) anulomaokāso": "(ख) सकारात्मक: स्थान",
    "(Ga) anulomapuggalokāsā": "(ग) सकारात्मक: व्यक्ति और स्थान",
    "(Gha) paccanīkapuggalo": "(घ) नकारात्मक: व्यक्ति",
    "(Ṅa) paccanīkaokāso": "(ङ) नकारात्मक: स्थान",
    "(Ca) paccanīkapuggalokāsā": "(च) नकारात्मक: व्यक्ति और स्थान",
    "Puggalavāro": "व्यक्ति का खंड",
    "Dhammavāro": "परिघटना का खंड",
    "Puggaladhammavāro": "व्यक्ति और परिघटना का खंड",
    "Pariññāvāro": "पूरी तरह समझने का खंड",
    "Pajahanavāro": "छोड़ने का खंड",
    "Pahīnavāro": "छोड़ा जा चुका होने का खंड",
    "Bhāvanāvāro": "अभ्यास का खंड",
}
LABELS = {"(Ka)": "(क)", "(Kha)": "(ख)", "(Ga)": "(ग)", "(Gha)": "(घ)", "(Ṅa)": "(ङ)", "(Ca)": "(च)"}

# =====================================================================================================
# 3. Short answers and closing lines
# =====================================================================================================
AMANTA = "हाँ।"                    # Āmantā.
NO = "नहीं।"                       # No.
NATTHI = "ऐसा कोई नहीं है।"        # Natthi.
CLOSINGS = {
    "Mūlavārauddeso.": "मूल के खंड की सूची।",
    "Mūlavāraniddeso.": "मूल के खंड की व्याख्या।",
    "Uddesavāro niṭṭhito.": "सूची का खंड पूरा हुआ।",
    "Niddesavāro niṭṭhito.": "व्याख्या का खंड पूरा हुआ।",
    "Mūlayamakapāḷi niṭṭhitā.": CHAPTER_END.format(title=CHAPTER_TITLES["Mūlayamakaṃ"]),
    "Khandhayamakapāḷi niṭṭhitā.": CHAPTER_END.format(title=CHAPTER_TITLES["Khandhayamakaṃ"]),
    "Paṇṇattiuddesavāro.": "शब्दावली की सूची का खंड।",
    "Paṇṇattiniddesavāro.": "शब्दावली की व्याख्या का खंड।",
    "Uppādavāro niṭṭhito.": "उत्पन्न होने का खंड पूरा हुआ।",       # (not yet in the sample)
    "Nirodhavāro.": "समाप्त होने का खंड।",                          # (not yet in the sample)
    "Uppādanirodhavāro.": "उत्पन्न होने और समाप्त होने का खंड।",     # (not yet in the sample)
    "Pavattivāro niṭṭhito.": "प्रक्रिया का खंड पूरा हुआ।",           # (not yet in the sample)
    "Pariññāvāro.": "पूरी तरह समझने का खंड।",                        # (not yet in the sample)
    "Namo tassa bhagavato arahato sammāsambuddhassa": NAMO,
    "Āmantā.": AMANTA,
    "No.": NO,
    "Natthi.": NATTHI,
}

# =====================================================================================================
# 4. Mūlayamaka
# =====================================================================================================
MULA_T = {"kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित", "nāma": "मानसिक पक्ष"}
MULA_T_DHAMMA = {  # <T>ā dhammā
    "kusala": "हितकर परिघटनाएँ", "akusala": "हानिकर परिघटनाएँ",
    "abyākata": "नैतिक रूप से अनिर्धारित परिघटनाएँ", "nāma": "मानसिक पक्ष की परिघटनाएँ"}
MULA_T_PRED = {  # sabbe te dhammā <T>ā  -> क्या वे सब परिघटनाएँ <..> हैं
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित", "nāma": "मानसिक पक्ष की"}
MULA_R = {  # <T>mūla (root phrase, plural / oblique)
    "kusala": "हितकर मूल", "akusala": "हानिकर मूल",
    "abyākata": "नैतिक रूप से अनिर्धारित मूल", "nāma": "मानसिक पक्ष के मूल"}
MULA_SAMUTTHANA = {  # <T>samuṭṭhānaṃ rūpaṃ
    t: f"{MULA_T[t]} से उत्पन्न भौतिक रूप" for t in MULA_T}
MULA_KIND = {  # what the root word says: mūla / mūlamūla / mūlaka / mūlamūlaka
    "mūla": "", "mūlamūla": " के मूल", "mūlaka": " पर आधारित", "mūlamūlaka": " के मूल पर आधारित"}
MULA_REL = {"eka": "एक ही", "aññamañña": "परस्पर"}
VALA = {"f": "वाली", "m": "वाला", "mpl": "वाले"}   # agreement of «वाला»
MULA_COUNT = {"Tīṇeva": "तीन ही", "Naveva": "नौ ही"}
EKATO = "जो मूल एक साथ उत्पन्न होते हैं, वे"     # Mūlāni yāni ekato uppajjanti
AHETUKA = "मूल से रहित"                           # Ahetukaṃ
SAHETUKA = "मूल वाला"                             # Sahetukaṃ

# Ten names of a root (Hetuvārādi); hetu = हेतु only here.
TEN_NAMES = [("mūla", "मूल"), ("hetu", "हेतु"), ("nidāna", "स्रोत"), ("sambhava", "उद्भव"), ("pabhava", "उद्गम"),
             ("samuṭṭhāna", "उत्पादक"), ("āhāra", "आहार"), ("ārammaṇa", "विषय"), ("paccaya", "कारण"),
             ("samudaya", "उत्पत्ति")]
TEN_NAMES_VERSE_1 = "मूल, हेतु और स्रोत, उद्भव और उद्गम;"        # Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;
TEN_NAMES_VERSE_2 = "उत्पादक, आहार और विषय, कारण और उत्पत्ति।"   # Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.


def mula_pred(t, kind, rel=None, agr="f"):
    """Hindi predicate for <t>mūla.. (rel=None), <t>mūlena <rel>mūla.. (t and rel), or bare <rel>mūla.. (t=None).
    kind: mūla | mūlamūla | mūlaka | mūlamūlaka; agr: f (परिघटनाएँ), m (neuter sg), mpl (the roots)."""
    if rel is None:
        return MULA_R[t] + MULA_KIND[kind]
    core = MULA_REL[rel] + " मूल" + MULA_KIND[kind]
    if kind in ("mūla", "mūlamūla"):
        core += " " + VALA[agr]
    return (MULA_R[t] + " के साथ " + core) if t else core


# =====================================================================================================
# 5. Paṇṇattivāra (term-checking pairs): bare words stay bare, aggregate names take the full term
# =====================================================================================================
# key (nominative) -> (direct, oblique, number)
PANNATTI_WORDS = {
    "rūpaṃ": ("रूप", "रूप", "sg"),
    "vedanā": ("अनुभूति", "अनुभूति", "sg"),
    "saññā": ("पहचान", "पहचान", "sg"),
    "saṅkhārā": ("रचनाएँ", "रचनाओं", "pl"),
    "viññāṇaṃ": ("चेतना", "चेतना", "sg"),
    "khandho": ("समूह", "समूह", "sg"),
    "khandhā": ("समूह", "समूहों", "pl"),
    "rūpakkhandho": ("भौतिक रूप का समूह", "भौतिक रूप के समूह", "sg"),
    "vedanākkhandho": ("अनुभूति का समूह", "अनुभूति के समूह", "sg"),
    "saññākkhandho": ("पहचान का समूह", "पहचान के समूह", "sg"),
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", "मानसिक रचनाओं के समूह", "sg"),
    "viññāṇakkhandho": ("चेतना का समूह", "चेतना के समूह", "sg"),
}
# accusative forms (also before -ñca / ca) -> nominative key
PANNATTI_ACC = {
    "rūpaṃ": "rūpaṃ", "vedanaṃ": "vedanā", "saññaṃ": "saññā", "saṅkhāre": "saṅkhārā", "viññāṇaṃ": "viññāṇaṃ",
    "khandhe": "khandhā", "rūpakkhandhaṃ": "rūpakkhandho", "vedanākkhandhaṃ": "vedanākkhandho",
    "saññākkhandhaṃ": "saññākkhandho", "saṅkhārakkhandhaṃ": "saṅkhārakkhandho",
    "viññāṇakkhandhaṃ": "viññāṇakkhandho",
}
# special subjects of the "A B, na C" / "A na C, B" answers
PANNATTI_SUBJECTS = {
    "piyarūpaṃ sātarūpaṃ": ("प्रिय और सुहावना लगने वाला रूप", "sg"),
    "diṭṭhisaññā": ("दृष्टि के अर्थ में पहचान", "sg"),
}
COP = {"sg": "है", "pl": "हैं"}
PRON = {"sg": "वह", "pl": "वे"}
CHHODKAR = "{x} को छोड़कर शेष"   # X ṭhapetvā avasesā
AVASESA = "शेष"


# =====================================================================================================
# 6. Pavattivāra: process verbs, question frames, beings, places
# =====================================================================================================
# (stem, gender) -> (positive, negative). gender: m (समूह, इंद्रिय-क्षेत्र, तत्व, सत्य, मन), f (क्षमता, सुप्त
# प्रवृत्ति, स्त्री-लिंग subjects), mpl (plural subjects).
VERBS = {
    ("uppajjati", "m"): ("उत्पन्न होता है", "उत्पन्न नहीं होता"),
    ("uppajjittha", "m"): ("उत्पन्न हुआ था", "उत्पन्न नहीं हुआ था"),
    ("uppajjissati", "m"): ("उत्पन्न होगा", "उत्पन्न नहीं होगा"),
    ("nirujjhati", "m"): ("समाप्त होता है", "समाप्त नहीं होता"),
    ("nirujjhittha", "m"): ("समाप्त हुआ था", "समाप्त नहीं हुआ था"),
    ("nirujjhissati", "m"): ("समाप्त होगा", "समाप्त नहीं होगा"),
    ("uppajjati", "f"): ("उत्पन्न होती है", "उत्पन्न नहीं होती"),
    ("uppajjittha", "f"): ("उत्पन्न हुई थी", "उत्पन्न नहीं हुई थी"),
    ("uppajjissati", "f"): ("उत्पन्न होगी", "उत्पन्न नहीं होगी"),
    ("nirujjhati", "f"): ("समाप्त होती है", "समाप्त नहीं होती"),
    ("nirujjhittha", "f"): ("समाप्त हुई थी", "समाप्त नहीं हुई थी"),
    ("nirujjhissati", "f"): ("समाप्त होगी", "समाप्त नहीं होगी"),
    ("uppajjati", "mpl"): ("उत्पन्न होते हैं", "उत्पन्न नहीं होते"),
    ("uppajjittha", "mpl"): ("उत्पन्न हुए थे", "उत्पन्न नहीं हुए थे"),
    ("uppajjissati", "mpl"): ("उत्पन्न होंगे", "उत्पन्न नहीं होंगे"),
    ("nirujjhati", "mpl"): ("समाप्त होते हैं", "समाप्त नहीं होते"),
    ("nirujjhittha", "mpl"): ("समाप्त हुए थे", "समाप्त नहीं हुए थे"),
    ("nirujjhissati", "mpl"): ("समाप्त होंगे", "समाप्त नहीं होंगे"),
}
# Pāli verb token -> (stem, negative?)
VERB_FORMS = {
    "uppajjati": ("uppajjati", False), "nuppajjati": ("uppajjati", True),
    "uppajjittha": ("uppajjittha", False), "nuppajjittha": ("uppajjittha", True),
    "uppajjissati": ("uppajjissati", False), "nuppajjissati": ("uppajjissati", True),
    "nirujjhati": ("nirujjhati", False), "nirujjhittha": ("nirujjhittha", False),
    "nirujjhissati": ("nirujjhissati", False),
    "uppajjanti": ("uppajjati", False), "nuppajjanti": ("uppajjati", True),
    "uppajjissanti": ("uppajjissati", False), "nuppajjissanti": ("uppajjissati", True),
    "nirujjhanti": ("nirujjhati", False), "nirujjhissanti": ("nirujjhissati", False),
}
VERB_SLIPS = {"nirujjhattha": "nirujjhittha"}   # 2-01 ^6-2-111: source slip, read as nirujjhittha

# Aggregate (process subjects) -> (Hindi, gender)
AGGREGATES = {
    "rūpakkhandho": ("भौतिक रूप का समूह", "m"),
    "vedanākkhandho": ("अनुभूति का समूह", "m"),
    "saññākkhandho": ("पहचान का समूह", "m"),
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", "m"),
    "viññāṇakkhandho": ("चेतना का समूह", "m"),
}

# relative frames of the questions: Pāli -> (Hindi relative, Hindi correlative)
REL_FRAMES = {
    ("yassa", "tassa"): ("जिस व्यक्ति में", "उसमें"),
    ("yassa vā pana", "tassa"): ("और जिस व्यक्ति में", "उसमें"),
    ("yattha", "tattha"): ("जिस स्थान पर", "वहाँ"),
    ("yattha vā pana", "tattha"): ("और जिस स्थान पर", "वहाँ"),
    ("yassa yattha", "tassa tattha"): ("जिस व्यक्ति में जिस स्थान पर", "उसमें वहाँ"),
    ("yassa vā pana yattha", "tassa tattha"): ("और जिस व्यक्ति में जिस स्थान पर", "उसमें वहाँ"),
}
Q_FRAME = "{label} {rel} {k1} {v1}, क्या {corr} {k2} {v2}?"
BUT_BEINGS = "{who} {k1} {v1}, पर उनमें {k2} {v2}।"               # <who> tesaṃ K1 V1, no ca tesaṃ K2 V2
BUT_BEINGS_T = "{who} वहाँ {k1} {v1}, पर उनमें वहाँ {k2} {v2}।"   # … tesaṃ tattha …, no ca tesaṃ tattha …
BUT_PLACE = "{place} {k1} {v1}, पर वहाँ {k2} {v2}।"              # <place> tattha K1 V1, no ca tattha K2 V2
BOTH_BEINGS = "{who} {k1} भी {v1} और {k2} भी {v2}।"              # <who> tesaṃ K1 ca V1 K2 ca V2
BOTH_BEINGS_T = "{who} वहाँ {k1} भी {v1} और {k2} भी {v2}।"
BOTH_PLACE = "{place} {k1} भी {v1} और {k2} भी {v2}।"

# Places (oblique noun; the case postposition is added by the frame)
PLACE_NOUN = {
    "asaññasatta": "पहचान-रहित प्राणियों के लोक",
    "pañcavokāra": "पाँच समूहों वाले अस्तित्व",
    "catuvokāra": "चार समूहों वाले अस्तित्व",
    "catupañcavokāra": "चार या पाँच समूहों वाले अस्तित्व",   # catuvokāraṃ pañcavokāraṃ (one chunk, «या»)
    "ekavokāra": "एक समूह वाले अस्तित्व",
    "arūpa": "अभौतिक लोक",
    "suddhāvāsa": "शुद्ध निवास लोक",
    "kāmāvacara": "इंद्रिय-सुखों के लोक",
    "rūpāvacara": "सूक्ष्म भौतिक लोक",
    "arūpāvacara": "अभौतिक लोक",
    "apāya": "दुर्गति के लोक",
}
PLACE_FORMS = {  # Pāli form -> (place key, case) ; case: acc (upapajjati into), abl (cavati from), loc (in)
    "asaññasattaṃ": ("asaññasatta", "acc"), "asaññasattā": ("asaññasatta", "abl"),
    "asaññasatte": ("asaññasatta", "loc"),
    "pañcavokāraṃ": ("pañcavokāra", "acc"), "pañcavokārā": ("pañcavokāra", "abl"),
    "pañcavokāre": ("pañcavokāra", "loc"),
    "catuvokāraṃ": ("catuvokāra", "acc"), "catuvokārā": ("catuvokāra", "abl"),
    "catuvokāre": ("catuvokāra", "loc"),
    "ekavokāraṃ": ("ekavokāra", "acc"), "ekavokārā": ("ekavokāra", "abl"), "ekavokāre": ("ekavokāra", "loc"),
    "arūpaṃ": ("arūpa", "acc"), "arūpā": ("arūpa", "abl"), "arūpe": ("arūpa", "loc"),
    "suddhāvāsaṃ": ("suddhāvāsa", "acc"), "suddhāvāsā": ("suddhāvāsa", "abl"),
    "suddhāvāse": ("suddhāvāsa", "loc"),
    "kāmāvacaraṃ": ("kāmāvacara", "acc"), "kāmāvacarā": ("kāmāvacara", "abl"),
    "kāmāvacare": ("kāmāvacara", "loc"),
    "rūpāvacaraṃ": ("rūpāvacara", "acc"), "rūpāvacarā": ("rūpāvacara", "abl"),
    "rūpāvacare": ("rūpāvacara", "loc"),
    "arūpāvacaraṃ": ("arūpāvacara", "acc"), "arūpāvacarā": ("arūpāvacara", "abl"),
    "arūpāvacare": ("arūpāvacara", "loc"),
    "apāye": ("apāya", "loc"),
}
CASE_POST = {"acc": "में", "abl": "से", "loc": "में"}
# Beings in the genitive (stand alone as a chunk)
BEINGS = {
    "asaññasattānaṃ": "पहचान-रहित प्राणियों में",
    "pañcavokārānaṃ": "पाँच समूहों वाले अस्तित्व के प्राणियों में",
    "catuvokārānaṃ": "चार समूहों वाले अस्तित्व के प्राणियों में",
    "arūpānaṃ": "अभौतिक लोक के प्राणियों में",
    "suddhāvāsānaṃ": "शुद्ध निवास लोक के प्राणियों में",
    "kāmāvacarānaṃ": "इंद्रिय-सुखों के लोक के प्राणियों में",
    "rūpāvacarānaṃ": "सूक्ष्म भौतिक लोक के प्राणियों में",
    "arūpāvacarānaṃ": "अभौतिक लोक के प्राणियों में",
    "āpāyikānaṃ": "दुर्गति के प्राणियों में",
}
# Participles closing a chunk
PARTICIPLES = {
    "upapajjantānaṃ": "जन्म लेने वालों में",
    "cavantānaṃ": "मरने वालों में",
    "parinibbantānaṃ": "पूर्ण निर्वाण पाने वालों में",
    "pacchimabhavikānaṃ": "अंतिम जन्म वालों में",
    "upapajjantīnaṃ": "जन्म लेने वाली स्त्रियों में",   # with itthīnaṃ (not yet in the sample)
    "cavantīnaṃ": "मरने वाली स्त्रियों में",
}
PACCHIMA_UPAPAJJ = "अंतिम जन्म लेने वालों में"   # pacchimabhavikānaṃ [X] upapajjantānaṃ, one chunk
SABBESAM = "सभी"           # Sabbesaṃ + participle
ITARESAM = "बाकी"          # Itaresaṃ + chunk
ITARESAM_ALONE = "बाकी सबमें"  # Itaresaṃ tesaṃ
YE_PARINIBBAYISSANTI = "जो {place} में जन्म लेकर पूर्ण निर्वाण पाएँगे, उनमें"  # Ye X upapajjitvā parinibbāyissanti tesaṃ
JOIN_LAST = " और "         # last chunk of a chain
JOIN = ", "

# Pariññā / pajahana / bhāvanā frames (not yet in the sample; harmonise B10)
YO_Q_PRESENT = "{label} जो व्यक्ति {o1} को {v1}, क्या वह {o2} को {v2}?"
YO_Q_PAST = "{label} जिस व्यक्ति ने {o1} को {v1}, क्या उसने {o2} को {v2}?"
YO_Q_FUTURE = "{label} जो व्यक्ति {o1} को {v1}, क्या वह {o2} को {v2}?"
PARIJANATI = {"parijānāti": ("पूरी तरह समझता है", "पूरी तरह नहीं समझता"),
              "parijānittha": ("पूरी तरह समझा था", "पूरी तरह नहीं समझा था"),
              "parijānissati": ("पूरी तरह समझेगा", "पूरी तरह नहीं समझेगा")}

# Abbreviation notes (harmonise N-notes; not yet in the sample)
NOTES = {
    "yassakaṃ": "व्यक्ति वाला भाग", "yatthakaṃ": "स्थान वाला भाग", "yassayatthakaṃ": "व्यक्ति और स्थान वाला भाग",
    "sadisaṃ": "समान", "vitthāretabbaṃ": "का विस्तार करना चाहिए", "vibhajitabbaṃ": "का विभाजन करना चाहिए",
    "vibhattaṃ": "का विभाजन किया गया है", "cakkaṃ bandhitabbaṃ": "चक्र पूरा करना चाहिए",
    "saṃkhittaṃ": "संक्षिप्त किया गया है", "anulomampi paccanīkampi": "सकारात्मक भी और नकारात्मक भी",
    "asammohantena": "बिना भ्रम के",
}

# =====================================================================================================
# 7. Fixed lines (unique lines of the sample, translated one by one)
# =====================================================================================================
FIXED_LINES = {
    # 1-mulayamaka ^6-1-49
    "Ye keci kusalā dhammā, sabbe te kusalahetū…pe… kusalanidānā…pe… kusalasambhavā…pe… kusalappabhavā…pe… "
    "kusalasamuṭṭhānā…pe… kusalāhārā…pe… kusalārammaṇā…pe… kusalapaccayā…pe… kusalasamudayā…pe….":
        "जो भी हितकर परिघटनाएँ हैं, क्या वे सब हितकर हेतु हैं… हितकर स्रोत… हितकर उद्भव… हितकर उद्गम… "
        "हितकर उत्पादक… हितकर आहार… हितकर विषय… हितकर कारण… हितकर उत्पत्ति…?",
    "Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;": TEN_NAMES_VERSE_1,
    "Samuṭṭhānāhārārammaṇā [samuṭṭhānāhārārammaṇaṃ (ka.)], paccayo samudayena cāti.":
        "उत्पादक, आहार और विषय [वर्तनी-भेद (Ka.): samuṭṭhānāhārārammaṇaṃ], कारण और उत्पत्ति।",
    "Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.": TEN_NAMES_VERSE_2,
    # ^6-1-98
    "Ye keci kusalā dhammā, sabbe te kusalahetūti…?":
        "जो भी हितकर परिघटनाएँ हैं, क्या वे सब हितकर हेतु हैं…?",
    "Tayo eva kusalahetū, avasesā kusalā dhammā na kusalahetū…pe… kusalanidānā… kusalasambhavā… "
    "kusalappabhavā… kusalasamuṭṭhānā… kusalāhārā… kusalārammaṇā… kusalapaccayā… kusalasamudayā….":
        "हितकर हेतु तीन ही हैं, शेष हितकर परिघटनाएँ हितकर हेतु नहीं हैं… हितकर स्रोत… हितकर उद्भव… "
        "हितकर उद्गम… हितकर उत्पादक… हितकर आहार… हितकर विषय… हितकर कारण… हितकर उत्पत्ति…।",
    # ^6-1-99
    "Ye keci akusalā dhammā… ye keci abyākatā dhammā… ye keci nāmā dhammā, sabbe te nāmahetū ti… "
    "nāmanidānā… nāmasambhavā… nāmappabhavā… nāmasamuṭṭhānā… nāmāhārā… nāmārammaṇā… nāmapaccayā… "
    "nāmasamudayā….":
        "जो भी हानिकर परिघटनाएँ हैं… जो भी नैतिक रूप से अनिर्धारित परिघटनाएँ हैं… जो भी मानसिक पक्ष की "
        "परिघटनाएँ हैं, क्या वे सब मानसिक पक्ष के हेतु हैं… मानसिक पक्ष के स्रोत… मानसिक पक्ष के उद्भव… "
        "मानसिक पक्ष के उद्गम… मानसिक पक्ष के उत्पादक… मानसिक पक्ष के आहार… मानसिक पक्ष के विषय… "
        "मानसिक पक्ष के कारण… मानसिक पक्ष की उत्पत्ति…?",
    # 2-01 ^6-2-1
    "Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.":
        "पाँच समूह – भौतिक रूप का समूह, अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह।",
    # 2-01 ^6-2-28 line 3 (variant bracket with an editorial note)
    "Avasesā khandhā [avasesā khandhā khandhā (syā.) evamuparipi] na vedanākkhandho.":
        "शेष समूह [पाठभेद (Syā.): avasesā khandhā khandhā; आगे भी इसी प्रकार], अनुभूति का समूह नहीं हैं।",
}
# Fixed sentences inside longer lines
FIXED_SENTENCES = {
    "Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā [avasesā saṅkhārā saṅkhārā (syā.)], na saṅkhārakkhandho.":
        "मानसिक रचनाओं के समूह को छोड़कर शेष, रचनाएँ हैं [पाठभेद (Syā.): avasesā saṅkhārā saṅkhārā], "
        "पर मानसिक रचनाओं का समूह नहीं हैं।",
}


# =====================================================================================================
# 8. The builder
# =====================================================================================================
ID_RE = re.compile(r"\s(\^[0-9A-Za-z-]+)\s*$")
_LAB = r"\((Ka|Kha|Ga|Gha|Ṅa|Ca)\)"


def strip_ti(word, vocab):
    """Remove the quotative -ti from the last word of a question (kusalāti, rūpanti, uppajjatīti, ...)."""
    if word in vocab:
        return word
    for cand in (word[:-2], word[:-3] + "ṃ", word[:-3] + "i", word[:-3] + "a", word[:-3] + "ā"):
        if cand in vocab:
            return cand
    raise ValueError(f"unknown word with -ti: {word}")


# ---------------- Mūlayamaka ----------------
# Pāli stems without the final -a (kusal-ā, kusal-aṃ, mūl-āni); t = stem + "a", kind = stem + "a".
_T = "kusal|akusal|abyākat|nām"
_K = "mūlamūlak|mūlamūl|mūlak|mūl"
_END = "āni|añceva|añca|aṃ|ā"
_MULA_VOCAB = set()
for _t in ("kusal", "akusal", "abyākat", "nām"):
    for _k in ("mūlamūlak", "mūlamūl", "mūlak", "mūl"):
        _MULA_VOCAB.add(f"{_t}a{_k}ā")
        for _r in MULA_REL:
            _MULA_VOCAB.add(f"{_r}{_k}ā")
    _MULA_VOCAB.add(_t + "ā")


def _mula_parse(s):
    """'kusalamūlā' -> (t, kind, None); 'kusalamūlena ekamūlā' -> (t, kind, rel); 'ekamūlāni' -> (None, kind, rel)."""
    m = re.fullmatch(rf"({_T})a({_K})({_END})", s)
    if m:
        return m.group(1) + "a", m.group(2) + "a", None
    m = re.fullmatch(rf"(?:({_T})amūlena )?(eka|aññamañña)({_K})({_END})", s)
    if m:
        return (m.group(1) + "a" if m.group(1) else None), m.group(3) + "a", m.group(2)
    raise ValueError(f"mūla predicate: {s}")


def _mula_hi(s, agr):
    t, kind, rel = _mula_parse(s)
    return mula_pred(t, kind, rel, agr)


def mula_question(line):
    m = re.fullmatch(rf"\(Ka\) ye keci (.+?) dhammā, sabbe te (.+?)\?", line)
    if m:
        subj, pred = m.group(1), m.group(2)
        *head, last = pred.split(" ")
        pred = " ".join(head + [strip_ti(last, _MULA_VOCAB)])
        if subj in ("kusalā", "akusalā", "abyākatā", "nāmā"):
            subj_hi = MULA_T_DHAMMA[subj[:-1] + "a"]
        else:
            subj_hi = _mula_hi(subj, "f") + " परिघटनाएँ"
        return f"(क) जो भी {subj_hi} हैं, क्या वे सब {_mula_hi(pred, 'f')} हैं?"
    m = re.fullmatch(rf"\(Kha\) ye vā pana (.+?), sabbe te dhammā (\S+?)\?", line)
    if m:
        t = strip_ti(m.group(2), _MULA_VOCAB)[:-1] + "a"
        return f"(ख) और जो {_mula_hi(m.group(1), 'f')} हैं, क्या वे सब परिघटनाएँ {MULA_T_PRED[t]} हैं?"
    return None


_TC = "Kusal|Akusal|Abyākat|Nām"


def mula_sentence(s):
    m = re.fullmatch(rf"(Tīṇeva|Naveva) ({_T})a({_K})āni\.", s)
    if m:
        return f"{mula_pred(m.group(2) + 'a', m.group(3) + 'a')} {MULA_COUNT[m.group(1)]} हैं।"
    m = re.fullmatch(rf"Avasesā ({_T})ā dhammā na (\S+)\.", s)
    if m:
        return f"{AVASESA} {MULA_T_DHAMMA[m.group(1) + 'a']} {_mula_hi(m.group(2), 'f')} नहीं हैं।"
    m = re.fullmatch(rf"({_TC})asamuṭṭhānaṃ rūpaṃ (.+?),? na ({_T})aṃ\.", s)
    if m:
        t = m.group(1).lower() + "a"
        return f"{MULA_SAMUTTHANA[t]}, {_mula_hi(m.group(2), 'm')} है, पर {MULA_T[t]} नहीं है।"
    m = re.fullmatch(rf"({_TC})aṃ (.+?)ñceva ({_T})añca\.", s)
    if m:
        t = m.group(1).lower() + "a"
        return f"{MULA_T[t]}, {_mula_hi(m.group(2) + 'ñceva', 'm')} भी है और {MULA_T[t]} भी।"
    m = re.fullmatch(rf"Mūlāni yāni ekato uppajjanti ({_T})amūlāni (\S+) ceva (\S+) ca\.", s)
    if m:
        return (f"{EKATO} {MULA_R[m.group(1) + 'a']} {_mula_hi(m.group(2), 'mpl')} भी हैं और "
                f"{_mula_hi(m.group(3), 'mpl')} भी।")
    m = re.fullmatch(rf"Avasesā ({_T})amūlasahajātā dhammā (\S+ \S+?),? na ca (\S+)\.", s)
    if m:
        return (f"{MULA_R[m.group(1) + 'a']} के साथ उत्पन्न {AVASESA} परिघटनाएँ, {_mula_hi(m.group(2), 'f')} हैं, "
                f"पर {_mula_hi(m.group(3), 'f')} नहीं हैं।")
    m = re.fullmatch(rf"(Ahetukaṃ|Sahetukaṃ) ({_T})aṃ (?:({_T})amūlena )?(na )?(\S+)\.", s)
    if m:
        t = m.group(2) + "a"
        pred = (f"{m.group(3)}amūlena " if m.group(3) else "") + m.group(5)
        mod = AHETUKA if m.group(1) == "Ahetukaṃ" else SAHETUKA
        neg = "नहीं " if m.group(4) else ""
        return f"{mod} {MULA_T[t]}, {_mula_hi(pred, 'm')} {neg}है।"
    return None


# ---------------- Paṇṇattivāra ----------------
_PW_TI = set(PANNATTI_WORDS)


def _pw(word):
    return PANNATTI_WORDS[word]


def pannatti_question(line):
    m = re.fullmatch(rf"{_LAB} (na )?(\S+) (na )?(\S+?)[?.]", line)
    if not m or bool(m.group(2)) != bool(m.group(4)):
        return None
    a = m.group(3)
    b = strip_ti(m.group(5), _PW_TI)
    if a not in PANNATTI_WORDS:
        return None
    lab = LABELS[f"({m.group(1)})"]
    (ad, _, an), (bd, _, bn) = _pw(a), _pw(b)
    n2 = "pl" if "pl" in (an, bn) else "sg"   # a plural predicate («रचनाएँ») takes «हैं»
    if m.group(2):  # paccanīka
        return f"{lab} जो {ad} नहीं {COP[an]}, क्या {PRON[an]} {bd} नहीं {COP[n2]}?"
    return f"{lab} क्या {ad}, {bd} {COP[n2]}?"


def _subject(s):
    """Subjects of the A-B-C answers -> (Hindi, number)."""
    if s.lower() in PANNATTI_SUBJECTS:
        return PANNATTI_SUBJECTS[s.lower()]
    m = re.fullmatch(r"(\S+) ṭhapetvā avasesā( khandhā)?", s)
    if m:
        x = PANNATTI_WORDS[PANNATTI_ACC[m.group(1).lower()]][1]
        return CHHODKAR.format(x=x) + (" समूह" if m.group(2) else ""), "pl"
    raise ValueError(f"subject: {s}")


def _acc_ca(w):
    """'Rūpañca' / 'rūpakkhandhañca' -> key; 'Saṅkhāre' (before ' ca') -> key."""
    w = w.lower()
    if w.endswith("ñca"):
        w = w[:-3] + "ṃ"
    return PANNATTI_ACC[w]


def pannatti_sentence(s):
    if s in FIXED_SENTENCES:
        return FIXED_SENTENCES[s]
    m = re.fullmatch(r"(.+?) (\S+), na (\S+)\.", s)            # A B, na C.
    if m and m.group(2) in PANNATTI_WORDS and m.group(3) in PANNATTI_WORDS:
        a, n = _subject(m.group(1))
        return f"{a}, {_pw(m.group(2))[0]} {COP[n]}, पर {_pw(m.group(3))[0]} नहीं {COP[n]}।"
    m = re.fullmatch(r"(.+?) na (\S+), (\S+)\.", s)            # A na C, B.
    if m and m.group(2) in PANNATTI_WORDS and m.group(3) in PANNATTI_WORDS:
        a, n = _subject(m.group(1))
        return f"{a}, {_pw(m.group(2))[0]} नहीं {COP[n]}, पर {_pw(m.group(3))[0]} {COP[n]}।"
    m = re.fullmatch(r"(\S+) (\S+?)(?:ñceva| ceva) (\S+) ca\.", s)   # C B ceva C ca.
    if m and m.group(1).lower() == m.group(3):
        c = _pw(m.group(3))
        b = m.group(2).lower()
        b = PANNATTI_WORDS.get(b) or _pw(_acc_ca(b + "ñca"))
        n = "pl" if "pl" in (b[2], c[2]) else "sg"
        return f"{c[0]}, {b[0]} भी {COP[n]} और {c[0]} भी।"
    m = re.fullmatch(r"(\S+?)(ñca| ca) (\S+?)(ñca| ca) ṭhapetvā avasesā na ceva (\S+) na ca (\S+)\.", s)
    if m:
        b = _pw(_acc_ca(m.group(1) + ("ñca" if m.group(2) == "ñca" else "")))
        c = _pw(_acc_ca(m.group(3) + ("ñca" if m.group(4) == "ñca" else "")))
        return (f"{b[1]} और {c[1]} को छोड़कर {AVASESA} न तो {_pw(m.group(5))[0]} हैं, "
                f"न {_pw(m.group(6))[0]}।")
    m = re.fullmatch(r"Avasesā khandhā na (\S+)\.", s)
    if m:
        return f"{AVASESA} समूह, {_pw(m.group(1))[0]} नहीं हैं।"
    return None


# ---------------- Pavattivāra ----------------
def _verb(tok):
    """'uppajjati' / 'nuppajjati' / 'na nirujjhati' -> (stem, neg)."""
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    w = VERB_SLIPS.get(w, w)
    stem, n = VERB_FORMS[w]
    return stem, (neg or n)


def verb_hi(tok, gender, flip=False):
    stem, neg = _verb(tok)
    pos_s, neg_s = VERBS[(stem, gender)]
    return neg_s if (neg != flip) else pos_s


_VERB_TI = set(VERB_FORMS) | set(VERB_SLIPS)
_REL = r"(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha)"
_COR = r"(tassa tattha|tassa|tattha)"
_V = r"((?:na )?\S+)"


def pavatti_question(line):
    m = re.fullmatch(rf"{_LAB} {_REL} (\S+) {_V} {_COR} (\S+) {_V}\?", line)
    if not m:
        return None
    lab, rel, k1, v1, cor, k2, v2 = m.groups()
    if k1 not in AGGREGATES or k2 not in AGGREGATES:
        return None
    neg2 = v2.startswith("na ")
    v2w = strip_ti(v2[3:] if neg2 else v2, _VERB_TI)
    v2 = ("na " if neg2 else "") + v2w
    rel_hi, cor_hi = REL_FRAMES[(rel, cor)]
    (k1h, g1), (k2h, g2) = AGGREGATES[k1], AGGREGATES[k2]
    return Q_FRAME.format(label=LABELS[f"({lab})"], rel=rel_hi, k1=k1h, v1=verb_hi(v1, g1),
                          corr=cor_hi, k2=k2h, v2=verb_hi(v2, g2))


def who(s):
    """Pāli being-phrase chain (before 'tesaṃ') -> Hindi, every chunk ending in «में», last joined with «और»."""
    s = s[0].lower() + s[1:]
    if s == "itaresaṃ":
        return ITARESAM_ALONE
    m = re.fullmatch(r"ye (\S+) upapajjitvā parinibbāyissanti", s)
    if m:
        key, case = PLACE_FORMS[m.group(1)]
        return YE_PARINIBBAYISSANTI.format(place=PLACE_NOUN[key])
    # «ye ca X upapajjitvā parinibbāyissanti [tesaṃ upapajjantānaṃ / cavantānaṃ]» as one chunk (harmonise B3)
    ye_chunks = {}

    def _ye(mm):
        key, _ = PLACE_FORMS[mm.group(1)]
        txt = YE_PARINIBBAYISSANTI.format(place=PLACE_NOUN[key])
        if mm.group(2):
            txt += " से " + PARTICIPLES[mm.group(2)]
        tok = f"§{len(ye_chunks)}"
        ye_chunks[tok] = txt
        return tok
    s = re.sub(r"ye ca (\S+) upapajjitvā parinibbāyissanti(?: tesaṃ (cavantānaṃ|upapajjantānaṃ))?", _ye, s)
    toks = s.split(" ")
    chunks, pre, places, i = [], [], [], 0
    while i < len(toks):
        w = toks[i]
        if w in ye_chunks:
            chunks.append(ye_chunks[w])
        elif w == "sabbesaṃ":
            pre.append(SABBESAM)
        elif w == "itaresaṃ":
            pre.append(ITARESAM)
        elif w in PLACE_FORMS:
            places.append(PLACE_FORMS[w])
        elif w in BEINGS and not places:
            chunks.append(" ".join(pre + [BEINGS[w]]))
            pre = []
        elif w == "pacchimabhavikānaṃ" and i + 1 < len(toks) and (
                toks[i + 1] == "upapajjantānaṃ" or (toks[i + 1] in PLACE_FORMS and i + 2 < len(toks)
                                                    and toks[i + 2] == "upapajjantānaṃ")):
            # pacchimabhavikānaṃ [X] upapajjantānaṃ = «[X में] अंतिम जन्म लेने वालों में» (harmonise B2)
            if toks[i + 1] in PLACE_FORMS:
                key, _ = PLACE_FORMS[toks[i + 1]]
                chunks.append(" ".join(pre + [f"{PLACE_NOUN[key]} में {PACCHIMA_UPAPAJJ}"]))
                i += 2
            else:
                chunks.append(" ".join(pre + [PACCHIMA_UPAPAJJ]))
                i += 1
            pre = []
        elif w in PARTICIPLES:
            if places:
                keys = [k for k, _ in places]
                case = places[0][1]
                key = "catupañcavokāra" if keys == ["catuvokāra", "pañcavokāra"] else keys[0]
                if len(keys) > 1 and key != "catupañcavokāra":
                    raise ValueError(f"who: several places in one chunk: {s}")
                chunks.append(" ".join(pre + [f"{PLACE_NOUN[key]} {CASE_POST[case]} {PARTICIPLES[w]}"]))
            else:
                chunks.append(" ".join(pre + [PARTICIPLES[w]]))
            pre, places = [], []
        else:
            raise ValueError(f"who: unknown token {w!r} in {s!r}")
        i += 1
    if pre or places:
        raise ValueError(f"who: dangling tokens in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return JOIN.join(chunks[:-1]) + JOIN_LAST + chunks[-1]


def place(s):
    """Place phrase of the okāsa answers (locative) -> Hindi with «में»."""
    toks = [t.lower() if j == 0 else t for j, t in enumerate(s.split(" "))]
    keys = [PLACE_FORMS[t][0] for t in toks]
    if keys == ["catuvokāra", "pañcavokāra"]:
        keys = ["catupañcavokāra"]
    parts = [f"{PLACE_NOUN[k]} में" for k in keys]
    return parts[0] if len(parts) == 1 else JOIN.join(parts[:-1]) + JOIN_LAST + parts[-1]


def pavatti_sentence(s):
    m = re.fullmatch(r"(.+?) (tesaṃ tattha|tesaṃ|tattha) (\S+) ((?:na )?\S+), no ca (?:tesaṃ tattha|tesaṃ|tattha) "
                     r"(\S+) ((?:na )?\S+)\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        (k1h, g1), (k2h, g2) = AGGREGATES[k1], AGGREGATES[k2]
        v1h, v2h = verb_hi(v1, g1), verb_hi(v2, g2, flip=True)
        if t == "tattha":
            return BUT_PLACE.format(place=place(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
        frame = BUT_BEINGS_T if t == "tesaṃ tattha" else BUT_BEINGS
        return frame.format(who=who(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
    m = re.fullmatch(r"(.+?) (tesaṃ tattha|tesaṃ|tattha) (\S+) ca ((?:na )?\S+) (\S+) ca ((?:na )?\S+)\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        (k1h, g1), (k2h, g2) = AGGREGATES[k1], AGGREGATES[k2]
        v1h, v2h = verb_hi(v1, g1), verb_hi(v2, g2)
        if t == "tattha":
            return BOTH_PLACE.format(place=place(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
        frame = BOTH_BEINGS_T if t == "tesaṃ tattha" else BOTH_BEINGS
        return frame.format(who=who(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
    return None


def short_answer(s, gender="m"):
    """Āmantā. / No. / Natthi. / Uppajjati. / Nuppajjati. / Nirujjhittha. … (gender of the asked subject)."""
    if s in ("Āmantā.", "No.", "Natthi."):
        return CLOSINGS[s]
    w = s[:-1]
    w = w[0].lower() + w[1:]
    if w in VERB_FORMS or w.startswith("na "):
        return verb_hi(w, gender) + "।"
    return None


# ---------------- line driver ----------------
_SENT_SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")


def _split_sentences(text):
    """Split at '. ' / '? ' before a capital or '(' (variant brackets have lower-case sigla, so they stay whole)."""
    return _SENT_SPLIT.split(text)


AGG_OBL = {k: v[0].replace(" का समूह", " के समूह") for k, v in AGGREGATES.items()}
AGG_ACC = {k[:-1] + "aṃ": k for k in AGGREGATES}   # rūpakkhandhaṃ -> rūpakkhandho
ABBR_Q = {"yattha": "जिस स्थान पर", "yassa": "जिस व्यक्ति में", "yassa yattha": "जिस व्यक्ति में जिस स्थान पर"}


def abbreviated_question(s):
    """'Yattha rūpakkhandho uppajjittha…pe….' -> «जिस स्थान पर भौतिक रूप का समूह उत्पन्न हुआ था…।» (not yet in the sample)"""
    m = re.fullmatch(r"(Yassa yattha|Yattha|Yassa) (\S+) ((?:na )?\S+)…pe…\.", s)
    if m and m.group(2) in AGGREGATES:
        k, g = AGGREGATES[m.group(2)]
        return f"{ABBR_Q[m.group(1).lower()]} {k} {verb_hi(m.group(3), g)}…।"
    return None


def parinna_question(s):
    """(Ka) yo X parijānāti so Y parijānātīti? (not yet in the sample; harmonise B10).
    Relative by the first verb (past: «जिस व्यक्ति ने»), correlative by the second (past: «उसने»)."""
    m = re.fullmatch(rf"{_LAB} yo( vā pana)? (\S+) ((?:na )?\S+) so (\S+) ((?:na )?\S+)\?", s)
    if not m or m.group(3) not in AGG_ACC or m.group(5) not in AGG_ACC:
        return None
    lab, vp, o1, v1, o2, v2 = m.groups()
    neg2 = v2.startswith("na ")
    v2 = ("na " if neg2 else "") + strip_ti(v2[3:] if neg2 else v2, set(PARIJANATI))

    def vh(v):
        neg = v.startswith("na ")
        w = v[3:] if neg else v
        return PARIJANATI[w][1 if neg else 0], w.endswith("ittha")
    v1h, past1 = vh(v1)
    v2h, past2 = vh(v2)
    rel = ("और " if vp else "") + ("जिस व्यक्ति ने" if past1 else "जो व्यक्ति")
    cor = "उसने" if past2 else "वह"
    return (f"{LABELS[f'({lab})']} {rel} {AGG_OBL[AGG_ACC[o1]]} को {v1h}, "
            f"क्या {cor} {AGG_OBL[AGG_ACC[o2]]} को {v2h}?")


def translate_sentence(s, last_gender="m"):
    if s in CLOSINGS:
        return CLOSINGS[s]
    if s.endswith("…pe….") and not s.startswith(("Yattha ", "Yassa ")):
        return translate_sentence(s[:-len("…pe….")] + ".", last_gender)[:-1] + "…।"
    r = abbreviated_question(s)
    if r:
        return r
    for fn in (mula_question, pannatti_question, pavatti_question, parinna_question):
        if s.startswith("(") and s.endswith(("?", ".")):
            r = fn(s)
            if r:
                return r
    for fn in (mula_sentence, pannatti_sentence, pavatti_sentence):
        r = fn(s)
        if r:
            return r
    r = short_answer(s, last_gender)
    if r:
        return r
    raise ValueError(f"no formula for: {s}")


def _q_gender(q):
    """Gender of the second subject of a process question (for the short answer)."""
    m = re.fullmatch(rf"{_LAB} {_REL} (\S+) {_V} {_COR} (\S+) {_V}\?", q)
    if m and m.group(6) in AGGREGATES:
        return AGGREGATES[m.group(6)][1]
    return "m"


def translate_text_line(line):
    if line in FIXED_LINES:
        return FIXED_LINES[line]
    sents = _split_sentences(line)
    out, gender = [], "m"
    for s in sents:
        if s.startswith("(") and s.endswith(("?", ".")) and (" " in s):
            gender = _q_gender(s)
        out.append(translate_sentence(s, gender))
    return " ".join(out)


def translate_line(line):
    """One Pāli line (heading or text, block ID optional) -> Hindi line."""
    if not line.strip():
        return ""
    bid = ""
    m = ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        if text not in HEADINGS:
            raise ValueError(f"unknown heading: {text}")
        return f"{hashes} {HEADINGS[text]}{bid}"
    return translate_text_line(line.strip()) + bid


def translate_text(pali_text):
    """Whole Pāli text -> Hindi text: one Hindi line per non-empty Pāli line, single blank lines, final newline."""
    out, prev_blank = [], True
    for line in pali_text.splitlines():
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        out.append(translate_line(line))
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


PREAMBLE = f"{NAMO} ^T-1\n\n# {ABHIDHAMMA} ^0\n\n## {BOOK_TITLE} ^6-0\n"
SAMPLE_2_01_LAST_LINE = 638   # Pāli lines 1-638 of 2-01-khandhayamaka.md, ending with ^6-2-55


def build():
    HI_DIR.mkdir(parents=True, exist_ok=True)
    (RAILS / "sample-1").mkdir(parents=True, exist_ok=True)
    (HI_DIR / "preamble.md").write_text(PREAMBLE, encoding="utf-8", newline="\n")
    mula = (PALI_DIR / "1-mulayamaka.md").read_text(encoding="utf-8")
    (HI_DIR / "1-mulayamaka.md").write_text(translate_text(mula), encoding="utf-8", newline="\n")
    raw = (PALI_DIR / "2-01-khandhayamaka.md").read_bytes().decode("utf-8")
    part = raw.splitlines(keepends=True)[:SAMPLE_2_01_LAST_LINE]   # byte-exact prefix (the source has CRLF)
    assert part[-1].rstrip().endswith("^6-2-55"), part[-1]
    pali = "".join(part)
    (RAILS / "sample-1" / "2-01-pali-sample.md").write_bytes(pali.encode("utf-8"))
    (RAILS / "sample-1" / "2-01-sample.md").write_text(translate_text(pali), encoding="utf-8", newline="\n")
    print("built: preamble.md, 1-mulayamaka.md, sample-1/2-01-pali-sample.md, sample-1/2-01-sample.md")


if __name__ == "__main__":
    build()
