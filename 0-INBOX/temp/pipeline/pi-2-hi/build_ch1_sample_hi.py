# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Hindi plain zero-shot: preamble + chapter-1 sample (first 77 non-empty lines).

usage: python -I -X utf8 build_ch1_sample_hi.py
Writes (only when run as a script):
  AI_translation\\hindi\\pi-2-hindi-plain-zeroshot_split_chapters\\preamble.md
  0-INBOX\\temp\\pipeline\\pi-2-hi\\ch1-sample.md        (Hindi of lines 1-118 of 1-khandhavibhango.md)
  0-INBOX\\temp\\pipeline\\pi-2-hi\\ch1-sample-pali.md   (the same Pāli lines, for verify_hi.py)

Other agents: import this module and reuse the constants and frame functions verbatim
(BOOK_TITLE, CHAPTER_TITLES, SECTION_TITLES, AGG, SYN_*, MEMBERS, khandha_def, time_line, self_line,
compare_para, far_near_clause, relative, class_open, class_close, RUPA_* strings ...).
Block IDs are never typed here: they are copied from the Pāli line at build time.
"""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
HI_DIR = os.path.join(ROOT, r"AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters")
PI1_HI_DIR = os.path.join(ROOT, r"AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-2-hi")

DASH = "–"  # the only dash allowed, and only where the Pāli has one
ID = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")

# ---------------------------------------------------------------- 1. book frame and headings
HOMAGE = "उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन"          # pi-1
PITAKA = "अभिधम्म पिटक में"                                        # pi-1
BOOK_TITLE = "विस्तृत विश्लेषण"                                      # Vibhaṅgapāḷi (proposal)
BOOK_TITLE_ALTERNATIVES = ["विश्लेषण", "परिघटनाओं का विश्लेषण"]
BOOK_TITLE_QUOTED = "“" + BOOK_TITLE + "”"                          # mid-sentence form

CHAPTER_TITLES = {  # ### level; closing line "<title> पूरा हुआ।" for "...vibhaṅgo niṭṭhito."
    1: "समूहों का विश्लेषण",                       # Khandhavibhaṅgo
    2: "इंद्रिय-क्षेत्रों का विश्लेषण",              # Āyatanavibhaṅgo
    3: "तत्वों का विश्लेषण",                       # Dhātuvibhaṅgo
    4: "सत्यों का विश्लेषण",                       # Saccavibhaṅgo
    5: "क्षमताओं का विश्लेषण",                     # Indriyavibhaṅgo
    6: "परस्पर-आश्रित उत्पत्ति का विश्लेषण",        # Paṭiccasamuppādavibhaṅgo
    7: "सजगता के आधारों का विश्लेषण",              # Satipaṭṭhānavibhaṅgo
    8: "सही प्रयत्नों का विश्लेषण",                 # Sammappadhānavibhaṅgo (pi-1: सही प्रयत्न)
    9: "सिद्धि के आधारों का विश्लेषण",              # Iddhipādavibhaṅgo
    10: "जागृति के अंगों का विश्लेषण",              # Bojjhaṅgavibhaṅgo
    11: "मार्ग के अंगों का विश्लेषण",               # Maggaṅgavibhaṅgo
    12: "ध्यान का विश्लेषण",                       # Jhānavibhaṅgo
    13: "असीम भावों का विश्लेषण",                  # Appamaññāvibhaṅgo
    14: "प्रशिक्षण के नियमों का विश्लेषण",           # Sikkhāpadavibhaṅgo
    15: "विश्लेषणात्मक ज्ञानों का विश्लेषण",         # Paṭisambhidāvibhaṅgo
    16: "ज्ञान का विश्लेषण",                       # Ñāṇavibhaṅgo
    17: "छोटे विषयों का विश्लेषण",                  # Khuddakavatthuvibhaṅgo
    18: "परिघटनाओं के सार का विश्लेषण",             # Dhammahadayavibhaṅgo
}
SECTION_TITLES = {  # #### level; the same words, with «।», as the closing line ("Suttantabhājanīyaṃ.")
    "Suttantabhājanīyaṃ": "उपदेशों के अनुसार विश्लेषण",
    "Abhidhammabhājanīyaṃ": "अभिधम्म के अनुसार विश्लेषण",
    "Pañhāpucchakaṃ": "प्रश्नोत्तर",
}

# ---------------------------------------------------------------- 2. aggregates
# g = grammatical gender of the Hindi noun, num = number used for the aggregate's own noun
AGG = {
    "rupa":     dict(noun="भौतिक रूप", g="m", num="sg", pl="भौतिक रूप", obl_pl="भौतिक रूपों", khandha="भौतिक रूप का समूह"),
    "vedana":   dict(noun="अनुभूति", g="f", num="sg", pl="अनुभूतियाँ", obl_pl="अनुभूतियों", khandha="अनुभूति का समूह"),
    "sanna":    dict(noun="पहचान", g="f", num="sg", pl="पहचानें", obl_pl="पहचानों", khandha="पहचान का समूह"),
    "sankhara": dict(noun="मानसिक रचनाएँ", g="f", num="pl", pl="मानसिक रचनाएँ", obl_pl="मानसिक रचनाओं", khandha="मानसिक रचनाओं का समूह"),
    "vinnana":  dict(noun="चेतना", g="f", num="sg", pl="चेतनाएँ", obl_pl="चेतनाओं", khandha="चेतना का समूह"),
}
FIVE_AGGREGATES = "पाँच समूह " + DASH + " भौतिक रूप का समूह, अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह"  # pi-1 ^1-1089


def _pl(a, num=None):
    return (num or AGG[a]["num"]) == "pl"


def cop(a, num=None):
    return "हैं" if _pl(a, num) else "है"


def yah(a, num=None):
    return "ये" if _pl(a, num) else "यह"


def kaha(a, num=None):
    """'is called' agreeing with the aggregate noun."""
    if AGG[a]["g"] == "m":
        return "कहे जाते हैं" if _pl(a, num) else "कहा जाता है"
    return "कही जाती हैं" if _pl(a, num) else "कही जाती है"


def kaun(a):
    return "कौन-सा" if AGG[a]["g"] == "m" else "कौन-सी"


def noun(a, num=None, obl=False):
    if not _pl(a, num):
        return AGG[a]["noun"]
    return AGG[a]["obl_pl"] if obl else AGG[a]["pl"]


# attribute adjectives used in the question/answer frames ("Tattha katamaṃ rūpaṃ atītaṃ?")
ATTR = {
    "atita": {"m": "अतीत का", "f": "अतीत की"},
    "anagata": {"m": "भविष्य का", "f": "भविष्य की"},
    "paccuppanna": {"m": "वर्तमान का", "f": "वर्तमान की"},
    "ajjhatta": "स्वयं से संबंधित",       # pi-1 ajjhattā dhammā
    "bahiddha": "दूसरों से संबंधित",       # pi-1 bahiddhā dhammā
    "olarika": "स्थूल", "sukhuma": "सूक्ष्म",
    "hina": "हीन", "panita": "उत्तम",
    "dure": {"m": "दूर का", "f": "दूर की"},
    "santike": {"m": "निकट का", "f": "निकट की"},
}


def attr(key, a):
    v = ATTR[key]
    return v[AGG[a]["g"]] if isinstance(v, dict) else v


# ---------------------------------------------------------------- 3. question / answer frames
def question(a, key):
    """Tattha katamaṃ <X> <attr>?  ->  यहाँ <attr> <X> क्या है?"""
    return f"यहाँ {attr(key, a)} {noun(a)} क्या {cop(a)}?"


def answer(a, key):
    """idaṃ / ayaṃ vuccati <X> <attr>; ime vuccanti ...  ->  यह/ये <attr> <X> कहा/कही जाता/जाती है/हैं।"""
    return f"{yah(a)} {attr(key, a)} {noun(a)} {kaha(a)}।"


def question_pair(a, x, y):
    """Tattha katamā vedanā oḷārikā sukhumā?  ->  यहाँ कौन-सी अनुभूति स्थूल है और कौन-सी सूक्ष्म?"""
    return f"यहाँ {kaun(a)} {noun(a)} {ATTR[x]} {cop(a)} और {kaun(a)} {ATTR[y]}?"


def khandha_question(a):
    """Tattha katamo rūpakkhandho?"""
    return f"यहाँ {AGG[a]['khandha']} क्या है?"


def khandha_answer(a):
    """ayaṃ vuccati rūpakkhandho / Ayaṃ vuccati rūpakkhandho."""
    return f"यह {AGG[a]['khandha']} कहा जाता है।"


# ---------------------------------------------------------------- 4. the aggregate definition (Suttantabhājanīya)
def khandha_def(a):
    """Yaṃ kiñci <X> atītānāgatapaccuppannaṃ ... tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā"""
    k = "की" if AGG[a]["g"] == "f" else "का"
    if _pl(a):
        return (f"जो भी {noun(a)} हैं, चाहे अतीत {k}, भविष्य {k} या वर्तमान {k} हों, स्वयं से संबंधित हों या दूसरों से संबंधित, "
                f"स्थूल हों या सूक्ष्म, हीन हों या उत्तम, दूर हों या निकट, उन सबको एक साथ इकट्ठा करके, संक्षेप में समेटकर")
    return (f"जो भी {noun(a)} है, चाहे अतीत {k}, भविष्य {k} या वर्तमान {k} हो, स्वयं से संबंधित हो या दूसरों से संबंधित, "
            f"स्थूल हो या सूक्ष्म, हीन हो या उत्तम, दूर हो या निकट, उस सबको एक साथ इकट्ठा करके, संक्षेप में समेटकर")


def khandha_def_line(a):
    return f"{khandha_question(a)} {khandha_def(a)} {DASH} {khandha_answer(a)}"


# ---------------------------------------------------------------- 5. synonym strings (pi-1 ^1-1044/1045/1046, ^1-1050/1051)
SYN_ATITA = {  # atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ uppajjitvā vigataṃ atītaṃ
    "m": "अतीत का, समाप्त हो चुका, जा चुका, बदल चुका, अस्त हो चुका, पूरी तरह अस्त हो चुका, उत्पन्न होकर जा चुका, अतीत का",
    "f": "अतीत की, समाप्त हो चुकी, जा चुकी, बदल चुकी, अस्त हो चुकी, पूरी तरह अस्त हो चुकी, उत्पन्न होकर जा चुकी, अतीत की",
}
SYN_ANAGATA = {  # ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ anuppannaṃ asamuppannaṃ anuṭṭhitaṃ asamuṭṭhitaṃ anāgataṃ
    "m": "न जन्मा हुआ, न हो चुका, न भली-भाँति जन्मा, न पैदा हुआ, न पूरी तरह पैदा हुआ, न प्रकट हुआ, न उत्पन्न, न भली-भाँति उत्पन्न, न उठा हुआ, न भली-भाँति उठा हुआ, भविष्य का",
    "f": "न जन्मी हुई, न हो चुकी, न भली-भाँति जन्मी, न पैदा हुई, न पूरी तरह पैदा हुई, न प्रकट हुई, न उत्पन्न, न भली-भाँति उत्पन्न, न उठी हुई, न भली-भाँति उठी हुई, भविष्य की",
}
SYN_PACCUPPANNA = {  # jātaṃ bhūtaṃ sañjātaṃ nibbattaṃ abhinibbattaṃ pātubhūtaṃ uppannaṃ samuppannaṃ uṭṭhitaṃ samuṭṭhitaṃ paccuppannaṃ
    "m": "जन्मा हुआ, हो चुका, भली-भाँति जन्मा, पैदा हुआ, पूरी तरह पैदा हुआ, प्रकट हुआ, उत्पन्न, भली-भाँति उत्पन्न, उठा हुआ, भली-भाँति उठा हुआ, वर्तमान का",
    "f": "जन्मी हुई, हो चुकी, भली-भाँति जन्मी, पैदा हुई, पूरी तरह पैदा हुई, प्रकट हुई, उत्पन्न, भली-भाँति उत्पन्न, उठी हुई, भली-भाँति उठी हुई, वर्तमान की",
}
TIME = {"atita": (SYN_ATITA, "अतीत"), "anagata": (SYN_ANAGATA, "भविष्य"), "paccuppanna": (SYN_PACCUPPANNA, "वर्तमान")}

SYN_AJJHATTA = {  # tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ (pi-1 has niyatā)
    "m": "उन-उन प्राणियों के स्वयं में, अपना, उनसे बँधा, हर व्यक्ति का निजी और कर्म से उत्पन्न",
    "f": "उन-उन प्राणियों के स्वयं में, अपनी, उनसे बँधी, हर व्यक्ति की निजी और कर्म से उत्पन्न",
}
SYN_BAHIDDHA = {  # tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ
    "m": "उन-उन दूसरे प्राणियों, दूसरे व्यक्तियों के स्वयं में, अपना, उनसे बँधा, हर व्यक्ति का निजी और कर्म से उत्पन्न",
    "f": "उन-उन दूसरे प्राणियों, दूसरे व्यक्तियों के स्वयं में, अपनी, उनसे बँधी, हर व्यक्ति की निजी और कर्म से उत्पन्न",
}
SELF = {"ajjhatta": SYN_AJJHATTA, "bahiddha": SYN_BAHIDDHA}

# hīna / paṇīta of matter (new; no pi-1 source)
SYN_HINA = {  # uññātaṃ avaññātaṃ hīḷitaṃ paribhūtaṃ acittīkataṃ hīnaṃ hīnamataṃ hīnasammataṃ aniṭṭhaṃ akantaṃ amanāpaṃ
    "m": "तुच्छ समझा गया, तिरस्कृत, निंदित, अपमानित, असम्मानित, हीन, हीन माना गया, आम तौर पर हीन माना गया, अनचाहा, अप्रिय, मन को न भाने वाला",
    "f": "तुच्छ समझी गई, तिरस्कृत, निंदित, अपमानित, असम्मानित, हीन, हीन मानी गई, आम तौर पर हीन मानी गई, अनचाही, अप्रिय, मन को न भाने वाली",
}
SYN_PANITA = {  # anuññātaṃ anavaññātaṃ ahīḷitaṃ aparibhūtaṃ cittīkataṃ paṇītaṃ paṇītamataṃ paṇītasammataṃ iṭṭhaṃ kantaṃ manāpaṃ
    "m": "न तुच्छ समझा गया, न तिरस्कृत, न निंदित, न अपमानित, सम्मानित, उत्तम, उत्तम माना गया, आम तौर पर उत्तम माना गया, मनचाहा, प्रिय, मनभावन",
    "f": "न तुच्छ समझी गई, न तिरस्कृत, न निंदित, न अपमानित, सम्मानित, उत्तम, उत्तम मानी गई, आम तौर पर उत्तम मानी गई, मनचाही, प्रिय, मनभावन",
}
SENSE_OBJECTS = "दृश्य रूप, ध्वनि, गंध, स्वाद और स्पर्श"  # rūpā saddā gandhā rasā phoṭṭhabbā

# dūre / santike of matter
SYN_DURE_RUPA = "पास नहीं है, समीप नहीं है, दूर है, निकट नहीं है"      # anāsanne anupakaṭṭhe dūre asantike
SYN_SANTIKE_RUPA = "पास है, समीप है, दूर नहीं है, निकट है"            # āsanne upakaṭṭhe avidūre santike
ANNAMPI = "या जो भी अन्य भौतिक रूप"                                  # yaṃ vā panaññampi atthi rūpaṃ

# the members listed after "यानी" (Pāli: no "ca"; «और» before the last item for natural Hindi)
CONTACTS = ["आँख", "कान", "नाक", "जीभ", "शरीर", "मन"]
MEMBERS = {
    "rupa": "चार महाभूत और चार महाभूतों से व्युत्पन्न भौतिक रूप",            # pi-1 ^1-1317
    "vedana": "सुखद अनुभूति, दुःखद अनुभूति और न दुःखद, न सुखद अनुभूति",
    "sanna": ", ".join(f"{c} के संपर्क से उत्पन्न पहचान" for c in CONTACTS[:-1]) + " और मन के संपर्क से उत्पन्न पहचान",
    "sankhara": ", ".join(f"{c} के संपर्क से उत्पन्न इरादा" for c in CONTACTS[:-1]) + " और मन के संपर्क से उत्पन्न इरादा",
    "vinnana": ", ".join(f"{c} की चेतना" for c in CONTACTS[:-1]) + " और मन की चेतना",
}


def time_line(a, key):
    syn, word = TIME[key]
    c = cop(a)
    return (f"{question(a, key)} जो {noun(a)} {syn[AGG[a]['g']]} {c} और {word} के अंतर्गत वर्गीकृत {c}, "
            f"यानी {MEMBERS[a]} {DASH} {answer(a, key)}")


def self_line(a, key):
    return (f"{question(a, key)} जो {noun(a)} {SELF[key][AGG[a]['g']]} {cop(a)}, "
            f"यानी {MEMBERS[a]} {DASH} {answer(a, key)}")


def relative(a, x, y):
    """Taṃ taṃ vā pana <X> upādāyupādāya <X> <x> <y> daṭṭhabbaṃ / Te te vā pana saṅkhāre ..."""
    if _pl(a):
        return f"या फिर, उन-उन {noun(a, obl=True)} से तुलना करके {noun(a, obl=True)} को {x} या {y} समझना चाहिए।"
    return f"या फिर, उस-उस {noun(a)} से तुलना करके {noun(a)} को {x} या {y} समझना चाहिए।"


# ---------------------------------------------------------------- 6. qualifiers for the coarse/subtle, inferior/superior, far/near paragraphs
QUAL = {  # prenominal, feminine (all four mental aggregates are feminine in Hindi)
    "akusala": "हानिकर",
    "kusala": "हितकर",
    "abyakata": "नैतिक रूप से अनिर्धारित",
    "kusalabyakata": "हितकर और नैतिक रूप से अनिर्धारित",        # pi-1 kusalābyākatā
    "kusalakusala": "हितकर और हानिकर",                          # pi-1 kusalākusalā
    "akusalabyakata": "हानिकर और नैतिक रूप से अनिर्धारित",
    "sasava": "मन के मैलों का विषय बनने वाली",                  # pi-1 sāsavā
    "anasava": "मन के मैलों का विषय न बनने वाली",               # pi-1 anāsavā
    "patigha": "टकराव वाले संपर्क से उत्पन्न",                   # paṭighasamphassajā (new)
    "adhivacana": "नाम वाले संपर्क से उत्पन्न",                  # adhivacanasamphassajā (new; pi-1 adhivacana = नाम)
}
GEN = {  # genitive of the person
    "asamapanna": "ध्यान-अवस्था में लीन न हुए व्यक्ति की",       # asamāpannassa (new, built on pi-1 samāpannassa)
    "samapanna": "ध्यान-अवस्था में लीन व्यक्ति की",              # samāpannassa (pi-1)
}
FEEL_DIRECT = {  # vedanā itself: dukkhā vedanā, sukhā vedanā ...
    "dukkha": "दुःखद", "sukha": "सुखद", "adm": "न दुःखद, न सुखद", "sukhadukkha": "सुखद और दुःखद",
}
FEEL_JOINED = {  # <feeling> sampayuttā saññā / saṅkhārā / viññāṇaṃ
    "dukkha": "दुःखद अनुभूति से जुड़ी",
    "sukha": "सुखद अनुभूति से जुड़ी",
    "adm": "न दुःखद, न सुखद अनुभूति से जुड़ी",
    "sukhadukkha": "सुखद और दुःखद अनुभूतियों से जुड़ी",
    "sukha_adm": "सुखद अनुभूति और न दुःखद, न सुखद अनुभूति से जुड़ी",
    "dukkha_adm": "दुःखद अनुभूति और न दुःखद, न सुखद अनुभूति से जुड़ी",
}
FEEL_PAIR_DIRECT = {  # sukhā ca adukkhamasukhā ca vedanā (two feelings: plural agreement)
    "sukha_adm": "सुखद अनुभूति और न दुःखद, न सुखद अनुभूति",
    "dukkha_adm": "दुःखद अनुभूति और न दुःखद, न सुखद अनुभूति",
}


def np(a, q, num="sg", obl=False):
    """Noun phrase '<qualifier> <aggregate noun>' and the number it agrees in."""
    if a == "vedana" and q in FEEL_PAIR_DIRECT:
        return FEEL_PAIR_DIRECT[q], "pl"
    n = noun(a, num, obl)
    if q in GEN:
        return f"{GEN[q]} {n}", num
    if a == "vedana" and q in FEEL_DIRECT:
        return f"{FEEL_DIRECT[q]} {n}", num
    if q in FEEL_JOINED:
        return f"{FEEL_JOINED[q]} {n}", num
    return f"{QUAL[q]} {n}", num


def _num(a, num):
    return "pl" if AGG[a]["num"] == "pl" else num


def compare_para(a, x, y, pairs):
    """'A <x>, B <y>.' sentences, e.g. Akusalā vedanā oḷārikā, kusalābyākatā vedanā sukhumā."""
    out = []
    for (qa, na), (qb, nb) in pairs:
        sa, ka = np(a, qa, _num(a, na))
        sb, kb = np(a, qb, _num(a, nb))
        out.append(f"{sa} {ATTR[x]} {'हैं' if ka == 'pl' else 'है'}, {sb} {ATTR[y]} {'हैं' if kb == 'pl' else 'है'}।")
    return " ".join(out)


def far_near_clause(a, subj, obj, near=False):
    """'<A> <B>-से दूर है' / '<A> <B> के निकट है' (Akusalā vedanā kusalābyākatāhi vedanāhi dūre)."""
    (qs, ns), (qo, no) = subj, obj
    s, ks = np(a, qs, _num(a, ns))
    o, _ = np(a, qo, _num(a, no), obl=True)
    rel = "के निकट" if near else "से दूर"
    return f"{s} {o} {rel} {'हैं' if ks == 'pl' else 'है'}"


def far_near_text(a, clauses, near=False):
    """clauses: [(subj, obj, sep)], sep is ';' or '।' (Pāli ';' / '.') or '' for the last before a dash."""
    parts = []
    for subj, obj, sep in clauses:
        parts.append(far_near_clause(a, subj, obj, near) + sep)
    return " ".join(parts)


# ---------------------------------------------------------------- 7. Abhidhammabhājanīya frames (pi-1 Rūpakaṇḍa wording)
NUM_WORDS = {1: "एक", 2: "दो", 3: "तीन", 4: "चार", 5: "पाँच", 6: "छह", 7: "सात", 8: "आठ", 9: "नौ", 10: "दस", 11: "ग्यारह"}


def class_open(n, a):
    """Ekavidhena rūpakkhandho –  ->  एक प्रकार से भौतिक रूप का समूह –"""
    return f"{NUM_WORDS[n]} प्रकार से {AGG[a]['khandha']} {DASH}"


def class_close(n, a):
    """Evaṃ ekavidhena rūpakkhandho.  ->  इस तरह एक प्रकार से भौतिक रूप का समूह बताया गया।"""
    return f"इस तरह {NUM_WORDS[n]} प्रकार से {AGG[a]['khandha']} बताया गया।"


ATTHI = "कुछ"  # atthi X, atthi Y (one class of the aggregate) -> कुछ X है, कुछ Y है (agrees with समूह, masc.)

# pi-1 ^1-584 (variant bracket dropped: pi-2 has none)
RUPA_EKAVIDHA = (
    "सारा भौतिक रूप मूल रूपी न होने वाला, मूल से रहित, मूलों से अलग, कारणों पर निर्भर रहने वाला, निर्मित, भौतिक, लौकिक, "
    "मन के मैलों का विषय बनने वाला, बंधनों का विषय बनने वाला, गाँठों का विषय बनने वाला, बाढ़ों का विषय बनने वाला, "
    "जकड़नों का विषय बनने वाला, बाधाओं का विषय बनने वाला, ग़लत धारणा का विषय बनने वाला, आसक्ति का विषय बनने वाला, "
    "क्लेशों का विषय बनने वाला, नैतिक रूप से अनिर्धारित, विषय से रहित, मन का सहचर न होने वाला, मन से अलग, "
    "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाला, क्लेशों से मलिन न होने वाला, पर क्लेशों का विषय बनने वाला, "
    "न आरंभिक विचार और सतत विचार वाला, न आरंभिक विचार से रहित और केवल सतत विचार वाला, "
    "आरंभिक विचार और सतत विचार दोनों से रहित, उल्लास के साथ न होने वाला, सुख के साथ न होने वाला, "
    "समभाव के साथ न होने वाला, न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला, "
    "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला, न संचय की ओर, न संचय घटाने की ओर ले जाने वाला, "
    "न सीखने के चरण का, न सीखना पूरा होने के चरण का, सीमित, इंद्रिय-सुखों के लोक से संबंधित, "
    "सूक्ष्म भौतिक लोक से संबंधित न होने वाला, अभौतिक लोक से संबंधित न होने वाला, अस्तित्व के लोकों में समाया हुआ, "
    "अस्तित्व के लोकों में न समाया हुआ नहीं, अनिश्चित, मुक्ति की ओर न ले जाने वाला, "
    "उत्पन्न होने पर छह प्रकार की चेतनाओं से जाना जा सकने वाला, अनित्य, बुढ़ापे से ग्रस्त है।"
)

# pi-1 ^1-U1 dyads: (Pāli key, positive, negative) -> "कुछ भौतिक रूप <pos> है, कुछ भौतिक रूप <neg> है।"
RUPA_DUKA = [
    ("upādā", "व्युत्पन्न", "व्युत्पन्न नहीं"),
    ("upādinnaṃ", "कर्म से उत्पन्न", "कर्म से उत्पन्न नहीं"),
    ("upādinnupādāniyaṃ", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला"),
    ("sanidassanaṃ", "दिखाई देने वाला", "दिखाई न देने वाला"),
    ("sappaṭighaṃ", "टकराव वाला", "टकराव से रहित"),
    ("indriyaṃ", "क्षमता", "क्षमता नहीं"),
    ("mahābhūtaṃ", "महाभूत", "महाभूत नहीं"),
    ("viññatti", "प्रकट अभिव्यक्ति", "प्रकट अभिव्यक्ति नहीं"),
    ("cittasamuṭṭhānaṃ", "मन से उत्पन्न", "मन से उत्पन्न नहीं"),
    ("cittasahabhu", "मन के साथ-साथ होने वाला", "मन के साथ-साथ न होने वाला"),
    ("cittānuparivatti", "मन का अनुसरण करने वाला", "मन का अनुसरण न करने वाला"),
    ("ajjhattikaṃ/bāhiraṃ", "आंतरिक", "बाह्य"),
    ("oḷārikaṃ/sukhumaṃ", "स्थूल", "सूक्ष्म"),
    ("dūre/santike", "दूर", "निकट"),
    ("kabaḷīkāro āhāro", "कौर-कौर खाया जाने वाला भोजन", "कौर-कौर खाया जाने वाला भोजन नहीं"),
]
DUKA = {k: (p, n) for k, p, n in RUPA_DUKA}


def duka(key, variant=""):
    p, n = DUKA[key]
    return f"कुछ भौतिक रूप {p} है, कुछ भौतिक रूप {n} है{variant}।"


def tika(inner, outer):
    """Yaṃ taṃ rūpaṃ ajjhattikaṃ taṃ <inner>, yaṃ taṃ rūpaṃ bāhiraṃ taṃ atthi .., atthi .. (pi-1 ^1-585)"""
    return f"जो भौतिक रूप आंतरिक है, वह {inner} है; जो भौतिक रूप बाह्य है, उसमें कुछ {outer[0]} है, कुछ {outer[1]} है"


def catukka(first, second, pair):
    """Yaṃ taṃ rūpaṃ <first> taṃ atthi .., atthi ..; yaṃ taṃ rūpaṃ <second> taṃ atthi .., atthi .. (pi-1 ^1-586)"""
    return (f"जो भौतिक रूप {first} है, उसमें कुछ {pair[0]} है, कुछ {pair[1]} है; "
            f"जो भौतिक रूप {second} है, उसमें कुछ {pair[0]} है, कुछ {pair[1]} है")


DITTHA_SUTA = "देखा हुआ, सुना हुआ, अनुभव किया हुआ और जाना हुआ भौतिक रूप।"   # pi-1 ^1-586
RUPA_PANCA = "पृथ्वी तत्व, जल तत्व, अग्नि तत्व, वायु तत्व और जो भी भौतिक रूप व्युत्पन्न है।"  # pi-1 ^1-587
_KNOW = ["आँख", "कान", "नाक", "जीभ", "शरीर"]
_K5 = ", ".join(f"{s} से जाना जा सकने वाला भौतिक रूप" for s in _KNOW)
RUPA_CHA = _K5 + " और मन से जाना जा सकने वाला भौतिक रूप।"                                                     # pi-1 ^1-588
RUPA_SATTA = _K5 + ", मन के तत्व से जाना जा सकने वाला भौतिक रूप और मन की चेतना के तत्व से जाना जा सकने वाला भौतिक रूप।"  # ^1-589
RUPA_ATTHA = (_K5 + ", जिसमें कुछ सुखद संपर्क वाला है, कुछ दुःखद संपर्क वाला है, मन के तत्व से जाना जा सकने वाला भौतिक रूप "
              "और मन की चेतना के तत्व से जाना जा सकने वाला भौतिक रूप।")                                          # ^1-590
_FAC8 = "आँख की क्षमता, कान की क्षमता, नाक की क्षमता, जीभ की क्षमता, शरीर की क्षमता, स्त्रीत्व की क्षमता, पुरुषत्व की क्षमता, जीवन-क्षमता"
RUPA_NAVA = _FAC8 + " और जो भी भौतिक रूप क्षमता नहीं है।"                                                      # ^1-591
RUPA_DASA = _FAC8 + " और जो भौतिक रूप क्षमता नहीं है, उसमें कुछ टकराव वाला है, कुछ टकराव से रहित है।"              # ^1-592
RUPA_EKADASA = ("आँख का इंद्रिय-क्षेत्र, कान का इंद्रिय-क्षेत्र, नाक का इंद्रिय-क्षेत्र, जीभ का इंद्रिय-क्षेत्र, शरीर का इंद्रिय-क्षेत्र, "
                "दृश्य रूप का इंद्रिय-क्षेत्र, ध्वनि का इंद्रिय-क्षेत्र, गंध का इंद्रिय-क्षेत्र, स्वाद का इंद्रिय-क्षेत्र, स्पर्श का इंद्रिय-क्षेत्र "
                "और जो भी भौतिक रूप दिखाई न देने वाला और टकराव से रहित है और मन के विषयों के इंद्रिय-क्षेत्र में समाया हुआ है।")  # ^1-593
RUPAKANDA_REF = "(जैसे भौतिक रूप के अध्याय में विश्लेषण किया गया है, वैसे ही यहाँ भी विश्लेषण करना चाहिए।)"  # Yathā rūpakaṇḍe vibhattaṃ ...

# pi-1 strings that must stay byte-identical (checked against the pi-1 rails Hindi in main())
PI1_REUSED = [HOMAGE, "# " + PITAKA, FIVE_AGGREGATES, RUPA_EKAVIDHA, DITTHA_SUTA, RUPA_PANCA, RUPA_CHA, RUPA_SATTA,
              RUPA_ATTHA, RUPA_NAVA, RUPA_DASA, RUPA_EKADASA, MEMBERS["rupa"], "आँख के संपर्क से उत्पन्न अनुभूति",
              "मन के संपर्क से उत्पन्न", "आँख की चेतना", "हितकर और नैतिक रूप से अनिर्धारित", "हितकर और हानिकर",
              "मन के मैलों का विषय बनने वाली", "मन के मैलों का विषय न बनने वाली", "सुखद अनुभूति से जुड़ी", "न दुःखद, न सुखद अनुभूति से जुड़ी",
              "ध्यान-अवस्था में लीन व्यक्ति की", "कौर-कौर खाया जाने वाला भोजन",
              "जो परिघटनाएँ " + SYN_ATITA["f"] + " हैं और अतीत के अंतर्गत वर्गीकृत हैं",
              "जो परिघटनाएँ " + SYN_ANAGATA["f"] + " हैं और भविष्य के अंतर्गत वर्गीकृत हैं",
              "जो परिघटनाएँ " + SYN_PACCUPPANNA["f"] + " हैं और वर्तमान के अंतर्गत वर्गीकृत हैं",
              "जो परिघटनाएँ " + SYN_AJJHATTA["f"] + " हैं", "जो परिघटनाएँ " + SYN_BAHIDDHA["f"] + " हैं"] + \
             [duka(k) for k, _, _ in RUPA_DUKA if "/" not in k] + \
             ["कुछ भौतिक रूप आंतरिक है, कुछ भौतिक रूप बाह्य है।", "कुछ भौतिक रूप स्थूल है, कुछ भौतिक रूप सूक्ष्म है।",
              "कुछ भौतिक रूप दूर है, कुछ भौतिक रूप निकट है।"]


# ---------------------------------------------------------------- 8. the sample, line by line (non-empty Pāli lines 1..77)
OL_SU = ("olarika", "sukhuma")
HI_PA = ("hina", "panita")
S, P = "sg", "pl"

# coarse/subtle and inferior/superior sentences (same order in every aggregate)
CMP_BASE = [
    (("akusala", S), ("kusalabyakata", S)),
    (("kusalakusala", S), ("abyakata", S)),
    (("dukkha", S), ("sukha_adm", S)),
    (("sukhadukkha", S), ("adm", S)),
    (("asamapanna", S), ("samapanna", S)),
    (("sasava", S), ("anasava", S)),
]
CMP_VINNANA = [  # Akusalaṃ viññāṇaṃ .., kusalābyākatā viññāṇā .. (the Pāli switches number)
    (("akusala", S), ("kusalabyakata", P)),
    (("kusalakusala", P), ("abyakata", S)),
    (("dukkha", S), ("sukha_adm", P)),
    (("sukhadukkha", P), ("adm", S)),
    (("asamapanna", S), ("samapanna", S)),
    (("sasava", S), ("anasava", S)),
]
CMP = {"vedana": CMP_BASE, "sanna": CMP_BASE, "sankhara": CMP_BASE, "vinnana": CMP_VINNANA}
CMP_SANNA_OLARIKA_PREFIX = [(("patigha", S), ("adhivacana", S))]


def cmp_line(a, x, y):
    pairs = CMP[a]
    if a == "sanna" and x == "olarika":
        pairs = CMP_SANNA_OLARIKA_PREFIX + pairs
    return f"{question_pair(a, x, y)} {compare_para(a, x, y, pairs)} {relative(a, ATTR[x], ATTR[y])}"


def far_clauses(a):
    """dūre clauses of the four mental aggregates; (subject, object, separator) following the Pāli punctuation."""
    v = a == "vinnana"  # viññāṇa: the Pāli subject is plural (viññāṇā) where the others are singular
    c = []
    # group 1: kusala triad
    sep1 = [";", ";", ";", "।" if a == "sanna" else ";", ";", "।"]
    g1 = [
        (("akusala", S), ("kusalabyakata", P)),
        (("kusalabyakata", P if v else S), ("akusala", S)),
        (("kusala", S), ("akusalabyakata", P)),
        (("akusalabyakata", P if v else S), ("kusala", S)),
        (("abyakata", S), ("kusalakusala", P)),
        (("kusalakusala", P if v else S), ("abyakata", S)),
    ]
    # group 2: feeling
    g2 = [
        (("dukkha", S), ("sukha_adm", P)),
        (("sukha_adm", P if v else S), ("dukkha", S)),
        (("sukha", S), ("dukkha_adm", P)),
        (("dukkha_adm", P if v else S), ("sukha", S)),
        (("adm", S), ("sukhadukkha", P)),
        (("sukhadukkha", P if v else S), ("adm", S)),
    ]
    sep2 = [";", ";", ";", ";", ";", "।"]
    g3 = [(("asamapanna", S), ("samapanna", S)), (("samapanna", S), ("asamapanna", S))]
    g4 = [(("sasava", S), ("anasava", S)), (("anasava", S), ("sasava", S))]
    last = "।" if a == "sankhara" else ""
    for (sb, ob), sp in zip(g1, sep1):
        c.append((sb, ob, sp))
    for (sb, ob), sp in zip(g2, sep2):
        c.append((sb, ob, sp))
    c += [(g3[0][0], g3[0][1], ";"), (g3[1][0], g3[1][1], "।")]
    c += [(g4[0][0], g4[0][1], ";"), (g4[1][0], g4[1][1], last)]
    return c


def near_clauses(a):
    last = "" if a == "vinnana" else "।"
    same = lambda q: ((q, S), (q, S))
    c = []
    for q, sp in (("akusala", ";"), ("kusala", ";"), ("abyakata", "।"), ("dukkha", ";"), ("sukha", ";"), ("adm", "।"),
                  ("asamapanna", ";"), ("samapanna", "।"), ("sasava", ";"), ("anasava", last)):
        s, o = same(q)
        c.append((s, o, sp))
    return c


def far_line(a):
    body = far_near_text(a, far_clauses(a))
    if a == "sankhara":  # "... dūre. Ime vuccanti saṅkhārā dūre."
        return f"{question(a, 'dure')} {body} {answer(a, 'dure')}"
    return f"{question(a, 'dure')} {body} {DASH} {answer(a, 'dure')}"


def near_line(a):
    body = far_near_text(a, near_clauses(a), near=True)
    if a == "vinnana":  # "... santike – idaṃ vuccati viññāṇaṃ santike. Taṃ taṃ ..."
        tail = f"{DASH} {answer(a, 'santike')}"
    else:               # "... santike. Ayaṃ vuccati vedanā santike. Taṃ taṃ ..."
        tail = answer(a, "santike")
    return f"{question(a, 'santike')} {body} {tail} {relative(a, 'दूर', 'निकट')}"


def mental_aggregate_lines(a):
    return [
        "##### " + AGG[a]["khandha"],
        khandha_def_line(a),
        time_line(a, "atita"), time_line(a, "anagata"), time_line(a, "paccuppanna"),
        self_line(a, "ajjhatta"), self_line(a, "bahiddha"),
        cmp_line(a, *OL_SU),
        cmp_line(a, *HI_PA),
        far_line(a),
        near_line(a),
    ]


def sample_lines():
    r = "rupa"
    L = [
        "### " + CHAPTER_TITLES[1],
        "#### " + SECTION_TITLES["Suttantabhājanīyaṃ"],
        FIVE_AGGREGATES + "।",
        "##### " + AGG[r]["khandha"],
        khandha_def_line(r),
        time_line(r, "atita"), time_line(r, "anagata"), time_line(r, "paccuppanna"),
        self_line(r, "ajjhatta"), self_line(r, "bahiddha"),
        f"{question(r, 'olarika')} आँख का इंद्रिय-क्षेत्र… स्पर्श का इंद्रिय-क्षेत्र {DASH} {answer(r, 'olarika')}",
        f"{question(r, 'sukhuma')} स्त्रीत्व की क्षमता… कौर-कौर खाया जाने वाला [वर्तनी-भेद (Sī., Syā.): kabaḷiṃkāro] भोजन {DASH} {answer(r, 'sukhuma')}",
        f"{question(r, 'hina')} जो भौतिक रूप उन-उन प्राणियों द्वारा {SYN_HINA['m']} है, यानी {SENSE_OBJECTS} {DASH} {answer(r, 'hina')}",
        f"{question(r, 'panita')} जो भौतिक रूप उन-उन प्राणियों द्वारा {SYN_PANITA['m']} है, यानी {SENSE_OBJECTS} {DASH} {answer(r, 'panita')} {relative(r, 'हीन', 'उत्तम')}",
        f"{question(r, 'dure')} स्त्रीत्व की क्षमता… कौर-कौर खाया जाने वाला भोजन, {ANNAMPI} {SYN_DURE_RUPA} {DASH} {answer(r, 'dure')}",
        f"{question(r, 'santike')} आँख का इंद्रिय-क्षेत्र… स्पर्श का इंद्रिय-क्षेत्र, {ANNAMPI} {SYN_SANTIKE_RUPA} {DASH} {answer(r, 'santike')} {relative(r, 'दूर', 'निकट')}",
    ]
    for a in ("vedana", "sanna", "sankhara", "vinnana"):
        L += mental_aggregate_lines(a)
    L.append(SECTION_TITLES["Suttantabhājanīyaṃ"] + "।")
    # Abhidhammabhājanīya
    L += [
        "#### " + SECTION_TITLES["Abhidhammabhājanīyaṃ"],
        FIVE_AGGREGATES + "।",
        "##### " + AGG[r]["khandha"],
        f"{khandha_question(r)} {class_open(1, r)} {RUPA_EKAVIDHA} {class_close(1, r)}",
        (f"{class_open(2, r)} {duka('upādā', ' [वर्तनी-भेद (Sī., Ka.): nupādā]')} "
         + " ".join(duka(k) for k, _, _ in RUPA_DUKA[1:-2])
         + " " + duka("dūre/santike")[:-1] + "… " + duka("kabaḷīkāro āhāro") + " " + class_close(2, r)),
        RUPAKANDA_REF,
        (f"{class_open(3, r)} "
         + tika("व्युत्पन्न", ("व्युत्पन्न", "व्युत्पन्न नहीं")) + "। "
         + tika("कर्म से उत्पन्न", ("कर्म से उत्पन्न", "कर्म से उत्पन्न नहीं")) + "। "
         + tika("कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
                ("कर्म से उत्पन्न और आसक्ति का विषय बनने वाला", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला")) + "… "
         + tika("कौर-कौर खाया जाने वाला भोजन नहीं", ("कौर-कौर खाया जाने वाला भोजन", "कौर-कौर खाया जाने वाला भोजन नहीं")) + "। "
         + class_close(3, r)),
        (f"{class_open(4, r)} "
         + catukka("व्युत्पन्न", "व्युत्पन्न नहीं", ("कर्म से उत्पन्न", "कर्म से उत्पन्न नहीं")) + "। "
         + catukka("व्युत्पन्न", "व्युत्पन्न नहीं", ("कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
                                                    "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला")) + "। "
         + catukka("व्युत्पन्न", "व्युत्पन्न नहीं", ("टकराव वाला", "टकराव से रहित")) + "। "
         + catukka("व्युत्पन्न", "व्युत्पन्न नहीं", ("स्थूल", "सूक्ष्म")) + "। "
         + catukka("व्युत्पन्न", "व्युत्पन्न नहीं", ("दूर", "निकट")) + "… "
         + DITTHA_SUTA + " " + class_close(4, r)),
        f"{class_open(5, r)} {RUPA_PANCA} {class_close(5, r)}",
        f"{class_open(6, r)} {RUPA_CHA} {class_close(6, r)}",
        f"{class_open(7, r)} {RUPA_SATTA} {class_close(7, r)}",
        f"{class_open(8, r)} {RUPA_ATTHA} {class_close(8, r)}",
        f"{class_open(9, r)} {RUPA_NAVA} {class_close(9, r)}",
        f"{class_open(10, r)} {RUPA_DASA} {class_close(10, r)}",
        f"{class_open(11, r)} {RUPA_EKADASA} {class_close(11, r)}",
        khandha_answer(r),
    ]
    return L


SAMPLE_LAST_PALI_LINE = 118  # last line before "##### Vedanākkhandho ^2-1-2-2-0"


def assemble(pali_lines, hindi_lines):
    """Same blank lines as the Pāli; block IDs copied from the Pāli."""
    out, it = [], iter(hindi_lines)
    for p in pali_lines:
        if not p.strip():
            out.append("")
            continue
        h = next(it)
        m = ID.search(p)
        if m:
            h = h + " " + m.group(1)
        out.append(h)
    rest = list(it)
    assert not rest, f"{len(rest)} Hindi lines left over"
    return "\n".join(out) + "\n"


def _read(path):
    return open(path, encoding="utf-8-sig").read()


def check_pi1():
    corpus = "\n".join(_read(os.path.join(PI1_HI_DIR, f)) for f in os.listdir(PI1_HI_DIR) if f.endswith(".md"))
    corpus = re.sub(r"\s*\[[^\]]*\]", "", corpus)
    missing = [s for s in PI1_REUSED if s.rstrip("।") not in corpus]
    assert not missing, "not found in pi-1 Hindi: " + " | ".join(missing)


def main():
    check_pi1()
    os.makedirs(HI_DIR, exist_ok=True)
    pre_p = _read(os.path.join(PALI_DIR, "preamble.md")).splitlines()
    pre_h = [HOMAGE, "# " + PITAKA, "## " + BOOK_TITLE]
    with open(os.path.join(HI_DIR, "preamble.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(assemble(pre_p, pre_h))

    ch = _read(os.path.join(PALI_DIR, "1-khandhavibhango.md")).splitlines()[:SAMPLE_LAST_PALI_LINE]
    assert ch[-1].endswith("^2-33") and sum(1 for l in ch if l.strip()) == 77, "sample range changed"
    with open(os.path.join(HERE, "ch1-sample-pali.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(ch) + "\n")
    with open(os.path.join(HERE, "ch1-sample.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(assemble(ch, sample_lines()))
    print("written: preamble.md, ch1-sample.md, ch1-sample-pali.md")


if __name__ == "__main__":
    main()
