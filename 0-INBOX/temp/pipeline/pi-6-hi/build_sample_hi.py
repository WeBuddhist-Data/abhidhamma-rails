r"""pi-6 Yamaka: Hindi plain zero-shot, SAMPLE builder with fixed formula strings.

usage: python -I -X utf8 build_sample_hi.py
Writes the four sample pairs into the sample folder and the preamble into
AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\preamble.md.

Importing this module only defines the constants and translator functions;
nothing is written unless it is run as a script. Later chapter builders should
import the constants (or copy them verbatim) so identical Pali stays identical Hindi.
Every line is translated by a rule or a fixed string; an unknown line raises an error.
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
HI_DIR = ROOT / "AI_translation" / "hindi" / "pi-6-hindi-plain-zeroshot_split_chapters"
SAMPLE_DIR = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-6-hi" / "sample"

ID_RE = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")

# ---------------------------------------------------------------- book frame
NAMO = "उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन"   # pi-1/pi-2
ABHIDHAMMAPITAKE = "अभिधम्म पिटक में"                       # pi-1/pi-2
BOOK_TITLE = "प्रश्नों के जोड़े"                              # Yamakapāḷi (new)
BOOK_TITLE_ALTERNATIVES = ["जोड़ों में पूछे गए प्रश्न", "युग्मों की पुस्तक"]
BOOK_END = "“प्रश्नों के जोड़े” ग्रंथ समाप्त।"                # Yamakapāḷi niṭṭhitā

# chapter headings (### level); chapter end: "<title> पूरे हुए।"
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
CHAPTER_END = "{title} पूरे हुए।"        # e.g. Mūlayamakapāḷi niṭṭhitā

# question labels
LABELS = {"(Ka)": "(क)", "(Kha)": "(ख)", "(Ga)": "(ग)", "(Gha)": "(घ)",
          "(Ṅa)": "(ङ)", "(Ca)": "(च)", "(Cha)": "(छ)", "(Ja)": "(ज)"}

# ---------------------------------------------------------------- section headings
VARO = "खंड"            # vāro (pi-1/pi-2)
NAYO = "विधि"           # nayo (pi-1/pi-2)
UDDESO = "सूची"         # uddeso (pi-4/pi-5)
NIDDESO = "व्याख्या"     # niddeso (pi-1..pi-5)
ANULOMAM = "सकारात्मक"   # anulomaṃ (Yamaka: positive statements)
PACCANIKAM = "नकारात्मक"  # paccanīkaṃ (negative statements)
PATILOMAM = "विपरीत"     # paṭiloma (Anusayayamaka)
PUGGALO = "व्यक्ति"       # puggala (pi-1..pi-5)
OKASO = "स्थान"          # okāsa
PUGGALOKASA = "व्यक्ति और स्थान"

HEADINGS = {
    # Mūlayamaka
    "Mūlavāro": "मूल का खंड",
    "Kusalā dhammā": "हितकर परिघटनाएँ",
    "(1) Mūlanayo": "(1) मूल की विधि",
    "(2) Mūlamūlanayo": "(2) मूल के मूल की विधि",
    "(3) Mūlakanayo": "(3) मूल पर आधारित होने की विधि",
    "(4) Mūlamūlakanayo": "(4) मूल के मूल पर आधारित होने की विधि",
    "Akusalā dhammā (1) mūlanayo": "हानिकर परिघटनाएँ (1) मूल की विधि",
    "Abyākatā dhammā (1) mūlanayo": "नैतिक रूप से अनिर्धारित परिघटनाएँ (1) मूल की विधि",
    "Nāmā dhammā (1) mūlanayo": "मानसिक पक्ष की परिघटनाएँ (1) मूल की विधि",
    "Kusalā dhammā (1) mūlanayo": "हितकर परिघटनाएँ (1) मूल की विधि",
    "2-10. Hetuvārādi": "2-10. हेतु का खंड आदि",
    "(Ka) uddeso": "(क) सूची",
    "(Kha) niddeso": "(ख) व्याख्या",
    # paṇṇattivāra
    "Paṇṇattivāro": "शब्दावली का खंड",
    "Paṇṇattivāraniddesa": "शब्दावली के खंड की व्याख्या",
    "Padasodhanavāro": "शब्दों की जाँच का खंड",
    "Padasodhanamūlacakkavāro": "शब्दों की जाँच पर आधारित चक्र का खंड",
    "Suddhakhandhavāro": "केवल समूहों का खंड",
    "Suddhakhandhamūlacakkavāro": "केवल समूहों पर आधारित चक्र का खंड",
    "(Ka) anulomaṃ": "(क) सकारात्मक",
    "(Kha) paccanīkaṃ": "(ख) नकारात्मक",
    # pavattivāra
    "Pavattivāro 1. uppādavāro": "प्रक्रिया का खंड 1. उत्पन्न होने का खंड",
    "Pavatti 2. nirodhavāro": "प्रक्रिया 2. समाप्त होने का खंड",
    "Pavatti 3. uppādanirodhavāro": "प्रक्रिया 3. उत्पन्न होने और समाप्त होने का खंड",
    "(1) Paccuppannavāro": "(1) वर्तमान का खंड",
    "(2) Atītavāro": "(2) अतीत का खंड",
    "(3) Anāgatavāro": "(3) भविष्य का खंड",
    "(4) Paccuppannātītavāro": "(4) वर्तमान और अतीत का खंड",
    "(5) Paccuppannānāgatavāro": "(5) वर्तमान और भविष्य का खंड",
    "(6) Atītānāgatavāro": "(6) अतीत और भविष्य का खंड",
    "(Ka) anulomapuggalo": "(क) सकारात्मक: व्यक्ति",
    "(Kha) anulomaokāso": "(ख) सकारात्मक: स्थान",
    "(Ga) anulomapuggalokāsā": "(ग) सकारात्मक: व्यक्ति और स्थान",
    "(Gha) paccanīkapuggalo": "(घ) नकारात्मक: व्यक्ति",
    "(Ṅa) paccanīkaokāso": "(ङ) नकारात्मक: स्थान",
    "(Ca) paccanīkapuggalokāsā": "(च) नकारात्मक: व्यक्ति और स्थान",
}
for _p, _h in CHAPTER_TITLES.items():
    HEADINGS[_p] = _h

# ---------------------------------------------------------------- answers
AMANTA = "हाँ।"                                   # Āmantā (pi-5)

# ---------------------------------------------------------------- Mūlayamaka
# root-type: Pāli stem -> (Hindi adjective of the phenomena, Hindi root phrase)
MULA_TYPES = {
    "akusala": ("हानिकर", "हानिकर मूल"),
    "abyākata": ("नैतिक रूप से अनिर्धारित", "नैतिक रूप से अनिर्धारित मूल"),
    "kusala": ("हितकर", "हितकर मूल"),
    "nāma": ("मानसिक पक्ष की", "मानसिक पक्ष के मूल"),
}
MULA_ADJ_PALI = {"akusala": "akusalā", "abyākata": "abyākatā", "kusala": "kusalā", "nāma": "nāmā"}
# kind of root-word -> Hindi, standing alone after the root phrase ("<R> …")
MULA_KIND_ALONE = {
    "mūla": "{R}",                          # kusalamūlā = हितकर मूल
    "mūlamūla": "{R} के मूल",               # kusalamūlamūlā
    "mūlaka": "{R} पर आधारित",              # kusalamūlakā
    "mūlamūlaka": "{R} के मूल पर आधारित",   # kusalamūlamūlakā
}
# after "<R> के साथ एक ही / परस्पर"
MULA_KIND_REL = {
    "mūla": "मूल वाली",
    "mūlamūla": "मूल के मूल वाली",
    "mūlaka": "मूल पर आधारित",
    "mūlamūlaka": "मूल के मूल पर आधारित",
}
MULA_REL = {"eka": "{R} के साथ एक ही {K}",          # kusalamūlena ekamūlā
            "aññamañña": "{R} के साथ परस्पर {K}"}    # kusalamūlena aññamaññamūlā

MULA_Q_KA = "जो भी {S} परिघटनाएँ हैं, क्या वे सब {P} हैं?"      # ye keci S dhammā, sabbe te P?
MULA_Q_KHA = "और जो {P} हैं, क्या वे सब परिघटनाएँ {A} हैं?"     # ye vā pana P, sabbe te dhammā A?

# the ten names for a root (Hetuvārādi)
ROOT_SYNONYMS = {
    "mūla": "मूल", "hetu": "हेतु", "nidāna": "स्रोत", "sambhava": "उद्भव",
    "pabhava": "उद्गम", "samuṭṭhāna": "उत्पादक", "āhāra": "आहार",
    "ārammaṇa": "विषय", "paccaya": "कारण", "samudaya": "उत्पत्ति",
}

_TYPE_ALT = "akusala|abyākata|kusala|nāma"
_KIND_ALT = "mūlamūlak|mūlamūl|mūlak|mūl"   # + "ā": the stem-final a merges (mūlā, mūlakā)


def _mula_phrase(tok):
    """'kusalamūlā' / 'kusalamūlena ekamūlā' -> (type, Hindi phrase)."""
    m = re.fullmatch(rf"({_TYPE_ALT})mūlena (eka|aññamañña)({_KIND_ALT})ā", tok)
    if m:
        t, rel, kind = m.groups()
        r = MULA_TYPES[t][1]
        return t, MULA_REL[rel].format(R=r, K=MULA_KIND_REL[kind + "a"])
    m = re.fullmatch(rf"({_TYPE_ALT})({_KIND_ALT})ā", tok)
    if m:
        t, kind = m.groups()
        return t, MULA_KIND_ALONE[kind + "a"].format(R=MULA_TYPES[t][1])
    return None


def tr_mula_question(body):
    """body without label; may end in 'ti?' (niddesa) or '?' (uddesa)."""
    m = re.fullmatch(r"ye keci (.+?) dhammā, sabbe te (.+?)(?:ti)?\?", body)
    if m:
        subj, pred = m.groups()
        t_p = _mula_phrase(pred)
        if subj in MULA_ADJ_PALI.values():
            s = {v: k for k, v in MULA_ADJ_PALI.items()}[subj]
            s_hi = MULA_TYPES[s][0]
        else:
            s_p = _mula_phrase(subj)
            s_hi = s_p and s_p[1]
        if t_p and s_hi:
            return MULA_Q_KA.format(S=s_hi, P=t_p[1])
    m = re.fullmatch(r"ye vā pana (.+?), sabbe te dhammā (\S+?)(?:ti)?\?", body)
    if m:
        pred, adj = m.groups()
        t_p = _mula_phrase(pred)
        inv = {v: k for k, v in MULA_ADJ_PALI.items()}
        if t_p and adj in inv:
            return MULA_Q_KHA.format(P=t_p[1], A=MULA_TYPES[inv[adj]][0])
    return None


# ---------------------------------------------------------------- Khandhayamaka terms
# aggregates (pi-1/pi-2); masculine singular
KHANDHA = {
    "rūpakkhandho": "भौतिक रूप का समूह",
    "vedanākkhandho": "अनुभूति का समूह",
    "saññākkhandho": "पहचान का समूह",
    "saṅkhārakkhandho": "मानसिक रचनाओं का समूह",
    "viññāṇakkhandho": "चेतना का समूह",
}
KHANDHA_OBL = {k: v.replace(" का समूह", " के समूह") for k, v in KHANDHA.items()}
# the bare word in the paṇṇattivāra word-pairs; (Hindi, plural?)
# rūpa and saṅkhārā are taken in their wide word-sense here (रूप, रचनाएँ),
# because the answers name things that are "rūpa"/"saṅkhārā" but outside the aggregate.
BARE = {
    "rūpaṃ": ("रूप", False),
    "vedanā": ("अनुभूति", False),
    "saññā": ("पहचान", False),
    "saṅkhārā": ("रचनाएँ", True),
    "viññāṇaṃ": ("चेतना", False),
}
BARE_OBL = {"rūpaṃ": "रूप", "vedanā": "अनुभूति", "saññā": "पहचान",
            "saṅkhārā": "रचनाओं", "viññāṇaṃ": "चेतना"}

PANNATTI_Q_ANU = "क्या {X}, {Y} {V}?"                     # X Y?
PANNATTI_Q_PACC = "जो {X} नहीं {V}, क्या {P} {Y} नहीं {V}?"  # na X na Y?

# qualified-answer frames (paṇṇattivāra niddesa)
QA_ANU_1 = "{A}, {B} है, पर {C} नहीं है।"                    # A B, na C.
QA_ANU_2 = "{C}, {B} भी है और {C} भी।"                      # C B ceva C ca.
QA_PACC_1 = "{A}, {C} नहीं {V}, पर {B} {V}।"                # A na C, B.
QA_PACC_2 = "{B} और {C} को छोड़कर शेष न तो {Bn} हैं, न {Cn}।"  # Bañca Cañca ṭhapetvā avasesā na ceva B na ca C.
EXCEPT = "{C} को छोड़कर"                                     # C ṭhapetvā
PIYARUPAM_SATARUPAM = "प्रिय और सुहावना लगने वाला रूप"       # Piyarūpaṃ sātarūpaṃ (pi-2: प्रिय/सुहावना लगने वाला)
DITTHISANNA = "दृष्टि के अर्थ में पहचान"                       # Diṭṭhisaññā
AVASESA = "शेष"                                              # avasesā (pi-1/pi-2)


def _var(label, sigla, pali):
    return f"[{label} ({sigla}): {pali}]"


VAR_SPELL = "वर्तनी-भेद"
VAR_READ = "पाठभेद"

# ---------------------------------------------------------------- pavattivāra
# Hindi verb forms: (positive, negative); masculine singular subject (समूह, इंद्रिय-क्षेत्र, तत्व, सत्य, मन)
VERBS_M = {
    "uppajjati": ("उत्पन्न होता है", "उत्पन्न नहीं होता"),
    "uppajjittha": ("उत्पन्न हुआ था", "उत्पन्न नहीं हुआ था"),
    "uppajjissati": ("उत्पन्न होगा", "उत्पन्न नहीं होगा"),
    "nirujjhati": ("समाप्त होता है", "समाप्त नहीं होता"),
    "nirujjhittha": ("समाप्त हुआ था", "समाप्त नहीं हुआ था"),
    "nirujjhissati": ("समाप्त होगा", "समाप्त नहीं होगा"),
}
# feminine singular subject (क्षमता, सुप्त प्रवृत्ति)
VERBS_F = {
    "uppajjati": ("उत्पन्न होती है", "उत्पन्न नहीं होती"),
    "uppajjittha": ("उत्पन्न हुई थी", "उत्पन्न नहीं हुई थी"),
    "uppajjissati": ("उत्पन्न होगी", "उत्पन्न नहीं होगी"),
    "nirujjhati": ("समाप्त होती है", "समाप्त नहीं होती"),
    "nirujjhittha": ("समाप्त हुई थी", "समाप्त नहीं हुई थी"),
    "nirujjhissati": ("समाप्त होगी", "समाप्त नहीं होगी"),
}
# plural subject (uppajjanti, nirujjhanti …), masculine
VERBS_PL = {
    "uppajjanti": ("उत्पन्न होते हैं", "उत्पन्न नहीं होते"),
    "uppajjiṃsu": ("उत्पन्न हुए थे", "उत्पन्न नहीं हुए थे"),
    "uppajjissanti": ("उत्पन्न होंगे", "उत्पन्न नहीं होंगे"),
    "nirujjhanti": ("समाप्त होते हैं", "समाप्त नहीं होते"),
    "nirujjhiṃsu": ("समाप्त हुए थे", "समाप्त नहीं हुए थे"),
    "nirujjhissanti": ("समाप्त होंगे", "समाप्त नहीं होंगे"),
}


def verb(tok, verbs=VERBS_M):
    """Pāli verb ('uppajjati', 'nuppajjati', 'na nirujjhati') -> (Hindi, negative?)."""
    neg = False
    if tok.startswith("na "):
        neg, tok = True, tok[3:]
    elif tok.startswith("n") and tok[1:] in verbs and tok[1:].startswith("u"):
        neg, tok = True, tok[1:]
    if tok not in verbs:
        raise KeyError(tok)
    return verbs[tok][1 if neg else 0], neg


def verb_flip(tok, verbs=VERBS_M):
    """'no ca … V' = the opposite polarity: no ca … nuppajjati -> उत्पन्न होता है."""
    neg = tok.startswith("na ") or (tok.startswith("n") and tok[1:] in verbs)
    base = tok[3:] if tok.startswith("na ") else (tok[1:] if neg else tok)
    return verbs[base][0 if neg else 1]


# question frames: who/where  ->  correlate
Q_REL = {"yassa": "जिस व्यक्ति में", "yattha": "जिस स्थान पर",
         "yassa yattha": "जिस व्यक्ति में जिस स्थान पर"}
Q_COR = {"tassa": "उसमें", "tattha": "वहाँ", "tassa tattha": "उसमें वहाँ"}
VA_PANA = "और "                     # (Kha) … vā pana …
PAVATTI_Q = "{AND}{REL} {X} {V1}, क्या {COR} {Y} {V2}?"

# beings and places in the answers
WHO = {   # genitive plural of beings in the answers (… tesaṃ)
    "Asaññasattaṃ upapajjantānaṃ": "पहचान-रहित प्राणियों के लोक में जन्म लेने वालों में",
    "Pañcavokāraṃ upapajjantānaṃ": "पाँच समूहों वाले अस्तित्व में जन्म लेने वालों में",
    "Arūpaṃ upapajjantānaṃ": "अभौतिक लोक में जन्म लेने वालों में",
    "Sabbesaṃ cavantānaṃ": "सभी मरने वालों में",
}
WHERE = {  # locatives of place (… tattha)
    "Asaññasatte": "पहचान-रहित प्राणियों के लोक में",
    "Pañcavokāre": "पाँच समूहों वाले अस्तित्व में",
    "Arūpe": "अभौतिक लोक में",
}
# answer loci: first mention (merged with the being/place phrase) / after "no ca"
LOC1 = {"tesaṃ": "", "tattha": "", "tesaṃ tattha": " वहाँ"}
LOC2 = {"tesaṃ": "उनमें", "tattha": "वहाँ", "tesaṃ tattha": "उनमें वहाँ"}
ANS_BUT = "{WHO}{L1} {X} {V1}, पर {L2} {Y} {V2}।"          # … X V, no ca tesaṃ Y V.
ANS_BOTH = "{WHO}{L1} {X} भी {V1} और {Y} भी {V2}।"         # … X ca V Y ca V.

_LOC_ALT = "tesaṃ tattha|tesaṃ|tattha"
_V = r"(?:na )?\S+"


def tr_pavatti_question(body):
    m = re.fullmatch(rf"(yassa|yattha)( vā pana)?( yattha)? (\S+) ({_V}) (tassa tattha|tassa|tattha) (\S+) ({_V})\?", body)
    if not m:
        return None
    rel, vp, rel2, x, v1, cor, y, v2 = m.groups()
    rel = rel + (rel2 or "")
    return PAVATTI_Q.format(AND=VA_PANA if vp else "", REL=Q_REL[rel], X=KHANDHA[x],
                            V1=verb(v1)[0], COR=Q_COR[cor], Y=KHANDHA[y], V2=verb(v2)[0])


def tr_pavatti_sentence(s):
    m = re.fullmatch(rf"(.+?) ({_LOC_ALT}) (\S+) ({_V}), no ca ({_LOC_ALT}) (\S+) ({_V})", s)
    if m:
        who, l1, x, v1, l2, y, v2 = m.groups()
        w = WHO.get(who) or WHERE[who]
        return ANS_BUT.format(WHO=w, L1=LOC1[l1], X=KHANDHA[x], V1=verb(v1)[0],
                              L2=LOC2[l2], Y=KHANDHA[y], V2=verb_flip(v2))
    m = re.fullmatch(rf"(.+?) ({_LOC_ALT}) (\S+) ca ({_V}) (\S+) ca ({_V})", s)
    if m:
        who, l1, x, v1, y, v2 = m.groups()
        w = WHO.get(who) or WHERE[who]
        return ANS_BOTH.format(WHO=w, L1=LOC1[l1], X=KHANDHA[x], V1=verb(v1)[0],
                               Y=KHANDHA[y], V2=verb(v2)[0])
    return None


SHORT_ANSWERS = {"Āmantā.": AMANTA}
for _p, (_pos, _neg) in VERBS_M.items():
    SHORT_ANSWERS[_p[0].upper() + _p[1:] + "."] = _pos + "।"
    SHORT_ANSWERS["N" + _p + "." if _p.startswith("u") else "Na " + _p + "."] = _neg + "।"

# ---------------------------------------------------------------- fixed lines
FIXED = {
    # Mūlayamaka, Hetuvārādi (uddesa)
    "Ye keci kusalā dhammā, sabbe te kusalahetū…pe… kusalanidānā…pe… kusalasambhavā…pe… kusalappabhavā…pe… kusalasamuṭṭhānā…pe… kusalāhārā…pe… kusalārammaṇā…pe… kusalapaccayā…pe… kusalasamudayā…pe….":
        "जो भी हितकर परिघटनाएँ हैं, क्या वे सब हितकर हेतु हैं… हितकर स्रोत… हितकर उद्भव… हितकर उद्गम… हितकर उत्पादक… हितकर आहार… हितकर विषय… हितकर कारण… हितकर उत्पत्ति…।",
    "Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;":
        "मूल, हेतु और स्रोत, उद्भव और उद्गम;",
    "Samuṭṭhānāhārārammaṇā [samuṭṭhānāhārārammaṇaṃ (ka.)], paccayo samudayena cāti.":
        "उत्पादक, आहार और विषय " + _var(VAR_SPELL, "Ka.", "samuṭṭhānāhārārammaṇaṃ") + ", कारण और उत्पत्ति।",
    "Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.":
        "उत्पादक, आहार और विषय, कारण और उत्पत्ति।",
    "Uddesavāro niṭṭhito.": "सूची का खंड पूरा हुआ।",
    "Niddesavāro niṭṭhito.": "व्याख्या का खंड पूरा हुआ।",
    "Mūlavārauddeso.": "मूल के खंड की सूची।",
    "Mūlavāraniddeso.": "मूल के खंड की व्याख्या।",
    "Paṇṇattiuddesavāro.": "शब्दावली की सूची का खंड।",
    "Paṇṇattiniddesavāro.": "शब्दावली की व्याख्या का खंड।",
    "Mūlayamakapāḷi niṭṭhitā.": CHAPTER_END.format(title=CHAPTER_TITLES["Mūlayamakaṃ"]),
    "Namo tassa bhagavato arahato sammāsambuddhassa": NAMO,
    # Khandhayamaka, paṇṇattivāra uddesa (identical Pāli in pi-2 ^2-1: reused verbatim)
    "Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.":
        "पाँच समूह – भौतिक रूप का समूह, अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह।",
    # paṇṇattivāra niddesa, qualified answers
    "Piyarūpaṃ sātarūpaṃ rūpaṃ, na rūpakkhandho. Rūpakkhandho rūpañceva rūpakkhandho ca.":
        QA_ANU_1.format(A=PIYARUPAM_SATARUPAM, B="रूप", C=KHANDHA["rūpakkhandho"]) + " "
        + QA_ANU_2.format(B="रूप", C=KHANDHA["rūpakkhandho"]),
    "Diṭṭhisaññā saññā, na saññākkhandho. Saññākkhandho saññā ceva saññākkhandho ca.":
        QA_ANU_1.format(A=DITTHISANNA, B="पहचान", C=KHANDHA["saññākkhandho"]) + " "
        + QA_ANU_2.format(B="पहचान", C=KHANDHA["saññākkhandho"]),
    "Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā [avasesā saṅkhārā saṅkhārā (syā.)], na saṅkhārakkhandho. Saṅkhārakkhandho saṅkhārā ceva saṅkhārakkhandho ca.":
        EXCEPT.format(C=KHANDHA_OBL["saṅkhārakkhandho"]) + " " + AVASESA + " रचनाएँ "
        + _var(VAR_READ, "Syā.", "avasesā saṅkhārā saṅkhārā") + ", "
        + KHANDHA["saṅkhārakkhandho"] + " नहीं हैं। "
        + QA_ANU_2.format(B="रचनाएँ", C=KHANDHA["saṅkhārakkhandho"]),
    "Piyarūpaṃ sātarūpaṃ na rūpakkhandho, rūpaṃ. Rūpañca rūpakkhandhañca ṭhapetvā avasesā na ceva rūpaṃ na ca rūpakkhandho.":
        QA_PACC_1.format(A=PIYARUPAM_SATARUPAM, C=KHANDHA["rūpakkhandho"], B="रूप", V="है") + " "
        + QA_PACC_2.format(B=BARE_OBL["rūpaṃ"], C=KHANDHA_OBL["rūpakkhandho"], Bn="रूप", Cn=KHANDHA["rūpakkhandho"]),
    "Diṭṭhisaññā na saññākkhandho, saññā. Saññañca saññākkhandhañca ṭhapetvā avasesā na ceva saññā na ca saññākkhandho.":
        QA_PACC_1.format(A=DITTHISANNA, C=KHANDHA["saññākkhandho"], B="पहचान", V="है") + " "
        + QA_PACC_2.format(B=BARE_OBL["saññā"], C=KHANDHA_OBL["saññākkhandho"], Bn="पहचान", Cn=KHANDHA["saññākkhandho"]),
    "Saṅkhārakkhandhaṃ ṭhapetvā avasesā na saṅkhārakkhandho, saṅkhārā. Saṅkhāre ca saṅkhārakkhandhañca ṭhapetvā avasesā na ceva saṅkhārā na ca saṅkhārakkhandho.":
        QA_PACC_1.format(A=EXCEPT.format(C=KHANDHA_OBL["saṅkhārakkhandho"]) + " " + AVASESA,
                         C=KHANDHA["saṅkhārakkhandho"], B="रचनाएँ", V="हैं") + " "
        + QA_PACC_2.format(B=BARE_OBL["saṅkhārā"], C=KHANDHA_OBL["saṅkhārakkhandho"], Bn="रचनाएँ", Cn=KHANDHA["saṅkhārakkhandho"]),
}

# all Pāli words a "…ti?" may hide (for undoing the quotative)
_KNOWN = set(KHANDHA) | set(BARE) | set(VERBS_M) | {"n" + v for v in VERBS_M}


def _untie(word):
    """Remove the quotative -ti from the last word of a question: rūpanti -> rūpaṃ."""
    for cand in (word[:-2], word[:-3] + "a", word[:-3] + "i", word[:-3] + "ṃ", word[:-3] + "ā"):
        if cand in _KNOWN:
            return cand
    return word


def tr_pannatti_question(body):
    m = re.fullmatch(r"(na )?(\S+) (na )?(\S+?)\?", body)
    if not m:
        return None
    n1, x, n2, y = m.groups()
    if bool(n1) != bool(n2):
        return None
    if x in BARE and y in KHANDHA:
        xh, pl = BARE[x]
        yh = KHANDHA[y]
    elif x in KHANDHA and y in BARE:
        xh, pl = KHANDHA[x], False
        yh = BARE[y][0]
    else:
        return None
    v = "हैं" if pl else "है"
    if n1:
        return PANNATTI_Q_PACC.format(X=xh, Y=yh, V=v, P="वे" if pl else "वह")
    return PANNATTI_Q_ANU.format(X=xh, Y=yh, V=v)


def tr_question(body):
    for f in (tr_mula_question, tr_pavatti_question, tr_pannatti_question):
        try:
            r = f(body)
        except KeyError:
            r = None
        if r:
            return r
    return None


def tr_body(text):
    """Translate one line without its block ID."""
    if text in FIXED:
        return FIXED[text]
    m = re.match(r"^(\((?:Ka|Kha)\)) (.*)$", text)
    if m:
        label, rest = m.groups()
        q, ans = rest, None
        if "? " in rest:
            q, ans = rest.split("? ", 1)
            q += "?"
        # undo the quotative -ti on the last word before "?" (rūpanti, uppajjatīti …);
        # unknown words are left as they are (the Mūla regexes strip -ti themselves)
        words = q[:-1].split(" ")
        if words[-1].endswith("ti") and words[-1] not in _KNOWN:
            words[-1] = _untie(words[-1])
        q2 = " ".join(words) + "?"
        hq = tr_question(q2)
        if hq is None:
            raise ValueError("untranslated question: " + text)
        out = LABELS[label] + " " + hq
        if ans:
            out += " " + tr_body(ans)
        return out
    if text in SHORT_ANSWERS:
        return SHORT_ANSWERS[text]
    # pavatti answers: one or two sentences
    sents = [s for s in re.split(r"(?<=\.) ", text)]
    if all(s.endswith(".") for s in sents):
        outs = [tr_pavatti_sentence(s[:-1]) for s in sents]
        if all(outs):
            return " ".join(outs)
    raise ValueError("untranslated line: " + text)


def tr_line(line):
    if not line.strip():
        return ""
    m = ID_RE.search(line)
    bid = m.group(1) if m else None
    text = ID_RE.sub("", line) if m else line
    if text.startswith("#"):
        level = len(text) - len(text.lstrip("#"))
        h = text[level:].strip()
        if h not in HEADINGS:
            raise ValueError("untranslated heading: " + h)
        out = "#" * level + " " + HEADINGS[h]
    else:
        out = tr_body(text)
    return out + (" " + bid if bid else "")


# ---------------------------------------------------------------- samples
SAMPLES = [
    ("s1-mula", "1-mulayamaka.md", 1, 122),
    ("s2-khandha-uddesa", "2-01-khandhayamaka.md", 1, 27),
    ("s3-khandha-niddesa", "2-01-khandhayamaka.md", 219, 248),
    ("s4-khandha-pavatti", "2-01-khandhayamaka.md", 518, 547),
]

PREAMBLE = (f"{NAMO} ^T-1\n\n# {ABHIDHAMMAPITAKE} ^0\n\n## {BOOK_TITLE} ^6-0\n")


def excerpt(fname, a, b):
    """Raw lines from the a-th to the b-th non-empty line (1-based, inclusive), blank lines kept."""
    raw = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
    idx = [i for i, l in enumerate(raw) if l.strip()]
    return raw[idx[a - 1]: idx[b - 1] + 1]


def main():
    HI_DIR.mkdir(parents=True, exist_ok=True)
    (HI_DIR / "preamble.md").write_text(PREAMBLE, encoding="utf-8", newline="\n")
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)
    for name, fname, a, b in SAMPLES:
        lines = excerpt(fname, a, b)
        (SAMPLE_DIR / f"{name}-pali.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        hi = [tr_line(l) for l in lines]
        (SAMPLE_DIR / f"{name}.md").write_text("\n".join(hi) + "\n", encoding="utf-8", newline="\n")
        print(name, len([l for l in lines if l.strip()]), "lines")


if __name__ == "__main__":
    main()
