"""Hindi builder for pi-7 Paṭṭhāna, 3-09-mahantaraduka.md (plain zero-shot).

Composes every Hindi line from fixed frames (imported from build_sample_hi.py) plus a small
phrase grammar for the example clauses, so identical Pāli always gets identical Hindi.

    python -I -B -X utf8 build_3-09_hi.py          # write + check
    python -I -B -X utf8 build_3-09_hi.py --check  # check only (no write)
    python -I -B -X utf8 build_3-09_hi.py --unk    # list untranslated words with context
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402  (import only)

FNAME = "3-09-mahantaraduka.md"
SRC = S.PALI_DIR / FNAME
OUT = S.HI_DIR / FNAME

UNK = []      # (line no, word) not translated
SLIPS = []    # (line no, note)
CUR_LINE = [0]


def unk(w):
    UNK.append((CUR_LINE[0], w))
    return "<<" + w + ">>"


# =====================================================================================
# 1. Hindi agreement helpers
# =====================================================================================
def inflect(tpl, g, n, obl):
    """'~' = inflecting vowel (ा / े / ी); 'हु~' = हुआ / हुए / हुई; '{या}' = या (sg) / और (pl)."""
    if g == "f":
        v, hu = "ी", "हुई"
    elif n == "pl" or obl:
        v, hu = "े", "हुए"
    else:
        v, hu = "ा", "हुआ"
    out = tpl.replace("हु~", hu).replace("~", v)
    return out.replace("{या}", "और" if n == "pl" else "या")


def BE(g, n):
    if n == "pl":
        return "होती हैं" if g == "f" else "होते हैं"
    return "होती है" if g == "f" else "होता है"


# Hindi nouns: (sg dir, sg obl, pl dir, pl obl, gender)
def HN(sg, g="m", pl_dir=None, pl_obl=None, sg_obl=None):
    if pl_dir is None:
        pl_dir = sg
    if pl_obl is None:
        pl_obl = pl_dir + "ों" if not pl_dir.endswith("ा") else pl_dir[:-1] + "ों"
    return (sg, sg_obl or sg, pl_dir, pl_obl, g)


HNOUN = {
    "khandha": HN("समूह"),
    "mahābhūta": HN("महाभूत"),
    "citta": HN("मन"),
    "vatthu": HN("आधार"),
    "rūpa": HN("भौतिक रूप"),
    "kaṭattārūpa": HN("किए गए कर्म से उत्पन्न भौतिक रूप"),
    "upādārūpa": HN("व्युत्पन्न भौतिक रूप"),
    "hetu": HN("मूल"),
    "cetanā": HN("इरादा", "m", "इरादे", "इरादों", "इरादे"),
    "moha": HN("मोह"),
    "dhamma": HN("परिघटना", "f", "परिघटनाएँ", "परिघटनाओं"),
    "adhipati": HN("प्रधानता", "f", "प्रधानताएँ", "प्रधानताओं"),
    "cittādhipati": HN("प्रधान बना हुआ मन", "m", "प्रधान बने हुए मन", "प्रधान बने हुए मनों", "प्रधान बने हुए मन"),
    "āhāra": HN("आहार"),
    "kabaḷīkāra": HN("कौर-कौर खाया जाने वाला भोजन", "m", "कौर-कौर खाए जाने वाले भोजन",
                     "कौर-कौर खाए जाने वाले भोजनों", "कौर-कौर खाए जाने वाले भोजन"),
    "indriya": HN("क्षमता", "f", "क्षमताएँ", "क्षमताओं"),
    "kāya": HN("शरीर"),
    "nibbāna": HN("निर्वाण"),
    "phala": HN("फल"),
    "magga": HN("मार्ग"),
    "jhāna": HN("ध्यान"),
    "ariya": HN("आर्य"),
    "rāga": HN("राग"),
    "diṭṭhi": HN("दृष्टि", "f", "दृष्टियाँ", "दृष्टियों"),
    "domanassa": HN("उदासी", "f"),
    "cakkhu": HN("आँख", "f", "आँखें", "आँखों"),
    "rūpa_obj": HN("दृश्य रूप"),
    "sadda": HN("ध्वनि", "f", "ध्वनियाँ", "ध्वनियों"),
    "gandha": HN("गंध", "f", "गंधें", "गंधों"),
    "rasa": HN("स्वाद"),
    "phoṭṭhabba": HN("स्पर्श"),
    "kilesa": HN("मन का क्लेश", "m", "मन के क्लेश", "मन के क्लेशों", "मन के क्लेश"),
    "gotrabhu": HN("गोत्र-परिवर्तन"),
    "vodāna": HN("शुद्धि", "f"),
    "phalasamāpatti": HN("फल की ध्यान-अवस्था", "f"),
    "vuṭṭhāna": HN("बाहर आना", "m", "बाहर आना", "बाहर आने", "बाहर आने"),
    "āvajjanā": HN("मन को विषय की ओर मोड़ना", "m", "मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ने",
                   "मन को विषय की ओर मोड़ने"),
    "iddhividhañāṇa": HN("अलौकिक शक्तियों का ज्ञान", "m", sg_obl="अलौकिक शक्तियों के ज्ञान"),
    "cetopariyañāṇa": HN("दूसरों के मन को जानने का ज्ञान", "m", sg_obl="दूसरों के मन को जानने के ज्ञान"),
    "pubbenivāsānussatiñāṇa": HN("पूर्व जन्मों के अनुस्मरण का ज्ञान", "m",
                                sg_obl="पूर्व जन्मों के अनुस्मरण के ज्ञान"),
    "yathākammūpagañāṇa": HN("प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान", "m",
                             sg_obl="प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान"),
    "anāgataṃsañāṇa": HN("भविष्य को जानने का ज्ञान", "m", sg_obl="भविष्य को जानने के ज्ञान"),
    "nevasaññānāsaññāyatana": HN("न पहचान न अ-पहचान का क्षेत्र", "m",
                                 sg_obl="न पहचान न अ-पहचान के क्षेत्र"),
    "ākāsānañcāyatana": HN("अनंत आकाश का क्षेत्र", "m", sg_obl="अनंत आकाश के क्षेत्र"),
    "viññāṇañcāyatana": HN("अनंत चेतना का क्षेत्र", "m", sg_obl="अनंत चेतना के क्षेत्र"),
    "ākiñcaññāyatana": HN("कुछ भी न होने का क्षेत्र", "m", sg_obl="कुछ भी न होने के क्षेत्र"),
    "anuloma_c": HN("अनुलोम मन"),
    "bhavaṅga": HN("भवांग"),
    "utu": HN("तापमान"),
    "bhojana": HN("भोजन"),
    "senāsana": HN("निवास-स्थान"),
    "saddhā": HN("श्रद्धा", "f"),
    "sīla": HN("सदाचार"),
    "paññā": HN("प्रज्ञा", "f"),
    "patthanā": HN("कामना", "f"),
    "sukha": HN("सुख"),
    "dukkha": HN("दुःख"),
    "vipākamanodhātu": HN("कर्म के फल रूपी मन का तत्व", "m", sg_obl="कर्म के फल रूपी मन के तत्व"),
    "vipākamanoviññāṇadhātu": HN("कर्म के फल रूपी मन की चेतना का तत्व", "m",
                                 sg_obl="कर्म के फल रूपी मन की चेतना के तत्व"),
    "kiriyamanoviññāṇadhātu": HN("केवल क्रिया रूपी मन की चेतना का तत्व", "m",
                                 sg_obl="केवल क्रिया रूपी मन की चेतना के तत्व"),
}
for s, h in S.SENSE.items():
    HNOUN[s + "viññāṇa"] = HN(f"{h} की चेतना", "f", f"{h} की चेतनाएँ", f"{h} की चेतनाओं")
    HNOUN[s + "āyatana"] = HN(f"{h} का इंद्रिय-क्षेत्र", "m", f"{h} के इंद्रिय-क्षेत्र", f"{h} के इंद्रिय-क्षेत्रों",
                              f"{h} के इंद्रिय-क्षेत्र")
    HNOUN[s + "indriya"] = HN(f"{h} की क्षमता", "f", f"{h} की क्षमताएँ", f"{h} की क्षमताओं")
for o, h in S.OBJECT.items():
    HNOUN[o + "āyatana_o"] = HN(f"{h} का इंद्रिय-क्षेत्र", "m", f"{h} के इंद्रिय-क्षेत्र",
                                f"{h} के इंद्रिय-क्षेत्रों", f"{h} के इंद्रिय-क्षेत्र")
HNOUN["rūpajīvitindriya"] = HN("भौतिक जीवन-क्षमता", "f", "भौतिक जीवन-क्षमताएँ", "भौतिक जीवन-क्षमताओं")
HNOUN["sukhindriya"] = HN("सुख की क्षमता", "f")
HNOUN["dukkhindriya"] = HN("दुःख की क्षमता", "f")
HNOUN["upekkhindriya"] = HN("समभाव की क्षमता", "f")
HNOUN["pañcaviññāṇa"] = HN("पाँच प्रकार की चेतना", "f")
HNOUN["anuloma_c"] = HN("अनुरूपता", "f")
for _k, _h in [("cakkhusampadā", "आँख"), ("kāyasampadā", "शरीर"), ("vaṇṇasampadā", "रूप-रंग"),
               ("saddasampadā", "आवाज़"), ("gandhasampadā", "गंध"), ("rasasampadā", "स्वाद")]:
    HNOUN[_k] = HN(f"{_h} की संपन्नता", "f")
HNOUN["ākāsānañcāyatanakusala"] = HN("अनंत आकाश के क्षेत्र का हितकर मन", "m",
                                     sg_obl="अनंत आकाश के क्षेत्र के हितकर मन")
HNOUN["ākiñcaññāyatanakusala"] = HN("कुछ भी न होने के क्षेत्र का हितकर मन", "m",
                                    sg_obl="कुछ भी न होने के क्षेत्र के हितकर मन")
HNOUN["viññāṇañcāyatanavipāka"] = HN("अनंत चेतना के क्षेत्र का कर्म के फल रूपी मन", "m",
                                     sg_obl="अनंत चेतना के क्षेत्र के कर्म के फल रूपी मन")

# Hindi adjective templates (see inflect); NOCOMMA: joined with a space, not a comma
HADJ = {
    # ---- the matrix dyad items (pi-1 1-matika.md, singular, inflected) ----
    "sārammaṇa": "विषय वाल~",
    "anārammaṇa": "विषय से रहित",
    "citta_i": "मन रूपी",
    "nocitta": "मन रूपी न होने वाल~",
    "cetasika": "मन क~ सहचर",
    "acetasika": "मन क~ सहचर न होने वाल~",
    "cittasampayutta": "मन से जुड़~",
    "cittavippayutta": "मन से अलग",
    "cittasaṃsaṭṭha": "मन से घुल~-मिल~",
    "cittavisaṃsaṭṭha": "मन से घुल~-मिल~ न होने वाल~",
    "cittasamuṭṭhāna": "मन से उत्पन्न",
    "nocittasamuṭṭhāna": "मन से उत्पन्न न होने वाल~",
    "cittasahabhū": "मन के साथ-साथ होने वाल~",
    "nocittasahabhū": "मन के साथ-साथ न होने वाल~",
    "cittānuparivatti": "मन का अनुसरण करने वाल~",
    "nocittānuparivatti": "मन का अनुसरण न करने वाल~",
    "cssam": "मन से घुल~-मिल~ और मन से उत्पन्न",
    "nocssam": "मन से घुल~-मिल~ और मन से उत्पन्न न होने वाल~",
    "cssah": "मन से घुल~-मिल~, मन से उत्पन्न और मन के साथ-साथ होने वाल~",
    "nocssah": "मन से घुल~-मिल~, मन से उत्पन्न और मन के साथ-साथ न होने वाल~",
    "csanu": "मन से घुल~-मिल~, मन से उत्पन्न और मन का अनुसरण करने वाल~",
    "nocsanu": "मन से घुल~-मिल~, मन से उत्पन्न और मन का अनुसरण न करने वाल~",
    "ajjhattika": "आंतरिक",
    "bāhira": "बाह्य",
    "upādā": "व्युत्पन्न",
    "noupādā": "व्युत्पन्न न होने वाल~",
    "upādinna": "कर्म से उत्पन्न",
    "anupādinna": "कर्म से उत्पन्न न होने वाल~",
    # ---- other attributes ----
    "ahetuka": "मूल से रहित",
    "vu": "संशय के साथ होने वाल~ {या} बेचैनी के साथ होने वाल~",
    "sampayuttaka": "जुड़~ हु~",
    "vipāka": "कर्म के फल रूपी",
    "kāyika": "शारीरिक",
    "utusamuṭṭhāna": "तापमान से उत्पन्न",
    "āhārasamuṭṭhāna": "आहार से उत्पन्न",
    "kaṭattā": "किए गए कर्म से उत्पन्न",
    "purima": "पहले-पहले क~",
    "pacchima": "बाद-बाद क~",
    "ima": "इस",
    "purejāta_a": "पहले उत्पन्न",
    "sahajāta_a": "साथ उत्पन्न",
    "pacchājāta_a": "बाद में उत्पन्न",
    "pahīna": "छोड़े जा चुके",
    "vikkhambhita": "दबाए जा चुके",
    "samudāciṇṇa": "बार-बार उठे",
    "pañcaviññāṇasahagata": "पाँच प्रकार की चेतना के साथ होने वाल~",
}
for s, h in S.SENSE.items():
    HADJ[s + "viññāṇasahagata"] = f"{h} की चेतना के साथ होने वाल~"
NOCOMMA = {"purima", "pacchima", "ima", "purejāta_a", "pacchājāta_a", "kaṭattā"}

# Labels of the condition sub-kinds (Sahajātaṃ – … / Purejātaṃ – …)
HLABEL = {
    "sahajāta": "सह-उत्पत्ति रूपी", "purejāta": "पूर्व-उत्पत्ति रूपी", "pacchājāta": "पश्चात्-उत्पत्ति रूपी",
    "āhāra": "आहार रूपी", "indriya": "क्षमता रूपी", "nānākkhaṇika": "भिन्न क्षणों वाला",
    "ārammaṇapurejāta": S.ARAMMANAPUREJATA, "vatthupurejāta": S.VATTHUPUREJATA,
    "ārammaṇādhipati": S.ARAMMANADHIPATI, "sahajātādhipati": S.SAHAJATADHIPATI,
    "ārammaṇūpanissaya": S.ARAMMANUPANISSAYA, "anantarūpanissaya": S.ANANTARUPANISSAYA,
    "pakatūpanissaya": S.PAKATUPANISSAYA,
}

NUMW = {1: "एक", 2: "दो", 3: "तीन"}

# =====================================================================================
# 2. Pāli lexicon: surface form -> list of word analyses
#    analysis = (pos, key, cls, num); pos N (noun) / A (adjective) / U (numeral) / L (label)
#    cls: N nominative, A accusative, X nom-or-acc, D dative/genitive, W any
# =====================================================================================
LEX = {}


def add(form, *words):
    LEX[form] = list(words)


A_END = {"o": ("N", "sg"), "aṃ": ("X", "sg"), "ā": ("N", "pl"), "e": ("A", "pl"), "assa": ("D", "sg"),
         "ānaṃ": ("D", "pl"), "āya": ("D", "sg")}
U_END = {"ū": ("N", None), "u": ("N", None), "uṃ": ("X", "sg"), "ussa": ("D", "sg"), "ūnaṃ": ("D", "pl")}
I_END = {"i": ("N", None), "iṃ": ("X", "sg"), "issa": ("D", "sg"), "īnaṃ": ("D", "pl"), "ino": ("N", "pl")}


def decl(stem, key, pos="A", kind="a", acc_sg="X"):
    ends = {"a": A_END, "u": U_END, "i": I_END}[kind]
    for e, (c, n) in ends.items():
        if kind == "a" and e == "aṃ":
            c = acc_sg
        add(stem + e, (pos, key, c, n))


ITEM_STEMS = [  # key, Pāli stem, declension
    ("sārammaṇa", "sārammaṇ", "a"), ("anārammaṇa", "anārammaṇ", "a"),
    ("nocitta", "nocitt", "a"), ("cetasika", "cetasik", "a"), ("acetasika", "acetasik", "a"),
    ("cittasampayutta", "cittasampayutt", "a"), ("cittasampayutta", "cittasampayuttak", "a"),
    ("cittavippayutta", "cittavippayutt", "a"),
    ("cittasaṃsaṭṭha", "cittasaṃsaṭṭh", "a"), ("cittavisaṃsaṭṭha", "cittavisaṃsaṭṭh", "a"),
    ("cittasamuṭṭhāna", "cittasamuṭṭhān", "a"), ("nocittasamuṭṭhāna", "nocittasamuṭṭhān", "a"),
    ("cittasahabhū", "cittasahabh", "u"), ("nocittasahabhū", "nocittasahabh", "u"),
    ("cittānuparivatti", "cittānuparivatt", "i"), ("nocittānuparivatti", "nocittānuparivatt", "i"),
    ("cssam", "cittasaṃsaṭṭhasamuṭṭhān", "a"), ("nocssam", "nocittasaṃsaṭṭhasamuṭṭhān", "a"),
    ("cssah", "cittasaṃsaṭṭhasamuṭṭhānasahabh", "u"), ("nocssah", "nocittasaṃsaṭṭhasamuṭṭhānasahabh", "u"),
    ("csanu", "cittasaṃsaṭṭhasamuṭṭhānānuparivatt", "i"),
    ("nocsanu", "nocittasaṃsaṭṭhasamuṭṭhānānuparivatt", "i"),
    ("ajjhattika", "ajjhattik", "a"), ("bāhira", "bāhir", "a"),
    ("upādinna", "upādinn", "a"), ("anupādinna", "anupādinn", "a"),
]
for key, stem, kind in ITEM_STEMS:
    decl(stem, key, "A", kind)
add("upādā", ("A", "upādā", "W", None))
add("noupādā", ("A", "noupādā", "W", None))

for key, stem in [("ahetuka", "ahetuk"), ("sampayuttaka", "sampayuttak"), ("vipāka", "vipāk"),
                  ("kāyika", "kāyik"), ("utusamuṭṭhāna", "utusamuṭṭhān"),
                  ("āhārasamuṭṭhāna", "āhārasamuṭṭhān"), ("pañcaviññāṇasahagata", "pañcaviññāṇasahagat"),
                  ("pahīna", "pahīn"), ("vikkhambhita", "vikkhambhit"), ("samudāciṇṇa", "samudāciṇṇ")]:
    decl(stem, key)
for s in S.SENSES:
    decl(s + "viññāṇasahagat", s + "viññāṇasahagata")
add("kaṭattā", ("A", "kaṭattā", "W", None))
add("imassa", ("A", "ima", "D", "sg"))
add("purejātassa", ("A", "purejāta_a", "D", "sg"))

# nouns
decl("khandh", "khandha", "N", acc_sg="A")
decl("mahābhūt", "mahābhūta", "N")
decl("citt", "citta", "N")
add("citaṃ", ("N", "citta", "X", "sg"))  # spelling slip handled in tokenizer
add("vatthu", ("N", "vatthu", "N", "sg"))
add("vatthuṃ", ("N", "vatthu", "A", "sg"))
add("vatthussa", ("N", "vatthu", "D", "sg"))
decl("rūp", "rūpa", "N")
add("rūpe", ("N", "rūpa_obj", "A", "pl"))
add("sadde", ("N", "sadda", "A", "pl"))
add("gandhe", ("N", "gandha", "A", "pl"))
add("rase", ("N", "rasa", "A", "pl"))
add("phoṭṭhabbe", ("N", "phoṭṭhabba", "A", "pl"))
decl("kaṭattārūp", "kaṭattārūpa", "N")
decl("upādārūp", "upādārūpa", "N")
add("hetū", ("N", "hetu", "N", "pl"))
add("cetanā", ("N", "cetanā", "N", "sg"))
add("moho", ("N", "moha", "N", "sg"))
add("mohaṃ", ("N", "moha", "A", "sg"))
decl("āhār", "āhāra", "N", acc_sg="A")
add("indriyā", ("N", "indriya", "N", "pl"))
add("kabaḷīkāro", ("A", "kabaḷī", "W", None))
add("kāyassa", ("N", "kāya", "D", "sg"))
add("kāyaṃ", ("N", "kāya", "A", "sg"))
add("cakkhuṃ", ("N", "cakkhu", "A", "sg"))
add("nibbānaṃ", ("N", "nibbāna", "X", "sg"))
add("phalaṃ", ("N", "phala", "X", "sg"))
add("maggaṃ", ("N", "magga", "X", "sg"))
add("jhānaṃ", ("N", "jhāna", "X", "sg"))
add("maggassa", ("N", "magga", "D", "sg"))
add("phalassa", ("N", "phala", "D", "sg"))
add("gotrabhussa", ("N", "gotrabhu", "D", "sg"))
add("vodānassa", ("N", "vodāna", "D", "sg"))
add("phalasamāpattiyā", ("N", "phalasamāpatti", "D", "sg"))
add("vuṭṭhānassa", ("N", "vuṭṭhāna", "D", "sg"))
add("āvajjanāya", ("N", "āvajjanā", "D", "sg"))
add("ariyā", ("N", "ariya", "N", "pl"))
add("rāgo", ("N", "rāga", "N", "sg"))
add("diṭṭhi", ("N", "diṭṭhi", "N", "sg"))
add("domanassaṃ", ("N", "domanassa", "N", "sg"))
add("kilese", ("N", "kilesa", "A", "pl"))
for k in ["iddhividhañāṇ", "cetopariyañāṇ", "pubbenivāsānussatiñāṇ", "yathākammūpagañāṇ", "anāgataṃsañāṇ"]:
    add(k + "assa", ("N", k + "a", "D", "sg"))
for s in S.SENSES:
    decl(s + "viññāṇ", s + "viññāṇa", "N")
    decl({"cakkhu": "cakkh", "sota": "sot", "ghāna": "ghān", "jivhā": "jivh", "kāya": "kāy"}[s] + "āyatan",
         s + "āyatana", "N")
    decl({"cakkhu": "cakkhund", "sota": "sotind", "ghāna": "ghānind", "jivhā": "jivhind", "kāya": "kāyind"}[s]
         + "riy", s + "indriya", "N")
for o, st_ in zip(S.OBJECTS, ["rūpāyatan", "saddāyatan", "gandhāyatan", "rasāyatan", "phoṭṭhabbāyatan"]):
    decl(st_, o + "āyatana_o", "N")
for k, st_ in [("cakkhusampadā", "cakkhusampad"), ("kāyasampadā", "kāyasampad"), ("vaṇṇasampadā", "vaṇṇasampad"),
               ("saddasampadā", "saddasampad"), ("gandhasampadā", "gandhasampad"), ("rasasampadā", "rasasampad")]:
    add(st_ + "aṃ", ("N", k, "A", "sg"))
    add(st_ + "ā", ("N", k, "N", "sg"))
add("vicikicchāsahagato uddhaccasahagato", ("A", "vu", "N", "sg"))
add("vicikicchāsahagate uddhaccasahagate", ("A", "vu", "A", "pl"))
add("vicikicchāsahagataṃ uddhaccasahagataṃ", ("A", "vu", "X", "sg"))
add("eka", ("U", 1, "X", "sg"))   # spelling slip for ekaṃ (line 1517)
add("āvajjanā", ("N", "āvajjanā", "N", "sg"))
add("anulomaṃ", ("N", "anuloma_c", "X", "sg"))
add("ākāsānañcāyatanakusalaṃ", ("N", "ākāsānañcāyatanakusala", "X", "sg"))
add("ākiñcaññāyatanakusalaṃ", ("N", "ākiñcaññāyatanakusala", "X", "sg"))
add("viññāṇañcāyatanavipākassa", ("N", "viññāṇañcāyatanavipāka", "D", "sg"))
decl("rūpajīvitindriy", "rūpajīvitindriya", "N")
decl("sukhindriy", "sukhindriya", "N")
decl("dukkhindriy", "dukkhindriya", "N")
decl("upekkhindriy", "upekkhindriya", "N")
decl("pañcaviññāṇ", "pañcaviññāṇa", "N")
add("nevasaññānāsaññāyatanaṃ", ("N", "nevasaññānāsaññāyatana", "X", "sg"))
add("nevasaññānāsaññāyatanassa", ("N", "nevasaññānāsaññāyatana", "D", "sg"))
add("ākāsānañcāyatanaṃ", ("N", "ākāsānañcāyatana", "X", "sg"))
add("ākiñcaññāyatanaṃ", ("N", "ākiñcaññāyatana", "X", "sg"))
add("viññāṇañcāyatanassa", ("N", "viññāṇañcāyatana", "D", "sg"))
add("vipākamanodhātu", ("N", "vipākamanodhātu", "N", "sg"))
add("vipākamanodhātuyā", ("N", "vipākamanodhātu", "D", "sg"))
add("vipākamanoviññāṇadhātu", ("N", "vipākamanoviññāṇadhātu", "N", "sg"))
add("vipākamanoviññāṇadhātuyā", ("N", "vipākamanoviññāṇadhātu", "D", "sg"))
add("kiriyamanoviññāṇadhātuyā", ("N", "kiriyamanoviññāṇadhātu", "D", "sg"))
add("bhavaṅgaṃ", ("N", "bhavaṅga", "X", "sg"))
add("utuṃ", ("N", "utu", "A", "sg"))
add("utu", ("N", "utu", "N", "sg"))
add("bhojanaṃ", ("N", "bhojana", "X", "sg"))
add("senāsanaṃ", ("N", "senāsana", "X", "sg"))
add("saddhaṃ", ("N", "saddhā", "A", "sg"))
add("saddhā", ("N", "saddhā", "N", "sg"))
add("saddhāya", ("N", "saddhā", "D", "sg"))
add("sīlaṃ", ("N", "sīla", "X", "sg"))
add("paññaṃ", ("N", "paññā", "A", "sg"))
add("paññā", ("N", "paññā", "N", "sg"))
add("paññāya", ("N", "paññā", "D", "sg"))
add("patthanaṃ", ("N", "patthanā", "A", "sg"))
add("patthanā", ("N", "patthanā", "N", "sg"))
add("patthanāya", ("N", "patthanā", "D", "sg"))
add("rāgaṃ", ("N", "rāga", "A", "sg"))
add("rāgassa", ("N", "rāga", "D", "sg"))
add("sukhaṃ", ("N", "sukha", "X", "sg"))
add("dukkhaṃ", ("N", "dukkha", "X", "sg"))
add("sukhassa", ("N", "sukha", "D", "sg"))
add("dukkhassa", ("N", "dukkha", "D", "sg"))

# numerals
add("eko", ("U", 1, "N", "sg"))
add("ekaṃ", ("U", 1, "X", "sg"))
add("dve", ("U", 2, "X", "pl"))
add("tayo", ("U", 3, "N", "pl"))
add("dvinnaṃ", ("U", 2, "D", "pl"))
add("tiṇṇannaṃ", ("U", 3, "D", "pl"))

# adhipati compounds: <item>ādhipati
for key, stem, kind in ITEM_STEMS:
    base = {"a": stem + "a", "u": stem + "ū", "i": stem + "i"}[kind]
    if kind == "a":
        add(stem + "ādhipati", ("A", key, "N", "sg"), ("N", "adhipati", "N", "sg"))
add("noupādādhipati", ("A", "noupādā", "W", None), ("N", "adhipati", "N", "sg"))
add("cittādhipati", ("N", "cittādhipati", "N", "sg"))

# labels (condition sub-kinds)
for f in ["sahajātaṃ", "sahajātā", "sahajāto"]:
    add(f, ("L", "sahajāta", "W", None))
for f in ["purejātaṃ"]:
    add(f, ("L", "purejāta", "W", None))
for f in ["pacchājātaṃ", "pacchājātā"]:
    add(f, ("L", "pacchājāta", "W", None))
add("āhāraṃ", ("L", "āhāra", "W", None))
add("indriyaṃ", ("L", "indriya", "W", None))
add("nānākkhaṇikā", ("L", "nānākkhaṇika", "W", None))
for k in ["ārammaṇapurejāta", "vatthupurejāta"]:
    add(k + "ṃ", ("L", k, "W", None))
for k in ["ārammaṇādhipati", "sahajātādhipati"]:
    add(k, ("L", k, "W", None))
for k in ["ārammaṇūpanissaya", "anantarūpanissaya", "pakatūpanissaya"]:
    add(k[:-1] + "o", ("L", k, "W", None))

# =====================================================================================
# 3. Function words and fixed phrases (token sequences, longest match)
#    unit kinds: post (needs a preceding NP, oblique), fix (fixed Hindi), adv (fixed, keeps subject),
#    verb (uppajjati...), sepw (word-like separator)
# =====================================================================================
PHR = {}


def phr(pali, kind, hi, **kw):
    PHR[tuple(pali.split())] = (kind, hi, kw)


phr("paṭicca", "post", "पर निर्भर होकर")
phr("paccayā", "post", "के कारण")
phr("nissāya", "post", "के आश्रय से")
for w in ["saṃsaṭṭho", "saṃsaṭṭhā", "saṃsaṭṭhaṃ"]:
    phr(w, "post", "से घुल-मिलकर")
phr("ārabbha", "post", "को विषय बनाकर")
phr("garuṃ katvā", "post", "को महत्व देकर")
phr("garuṃ", "post", "को महत्व")
phr("upanissāya", "post", "के प्रबल आश्रय से")
phr("paccavekkhati", "post", "पर पुनः विचार करता है")
phr("paccavekkhanti", "post", "पर पुनः विचार करते हैं")
phr("jānāti", "post", "को जानता है")
phr("jānanti", "post", "को जानते हैं")
phr("aniccato", "post", "को अनित्य")
phr("garuṃ katvā paccavekkhati", "post", "को महत्व देकर उस पर पुनः विचार करता है",
    pl="को महत्व देकर उन पर पुनः विचार करता है")
phr("garuṃ katvā paccavekkhanti", "post", "को महत्व देकर उस पर पुनः विचार करते हैं",
    pl="को महत्व देकर उन पर पुनः विचार करते हैं")
phr("garuṃ katvā assādeti abhinandati", "post", "को महत्व देकर उसका रस लेता है, उसमें आनंद लेता है",
    pl="को महत्व देकर उनका रस लेता है, उनमें आनंद लेता है")
phr("assādeti abhinandati", "fix", "उसका रस लेता है, उसमें आनंद लेता है")
phr("vipassati assādeti abhinandati", "fix", "अंतर्दृष्टि से देखता है, उसका रस लेता है, उसमें आनंद लेता है")
phr("vipassati", "fix", "अंतर्दृष्टि से देखता है")
phr("taṃ ārabbha", "fix", "उसे विषय बनाकर")
phr("taṃ garuṃ katvā", "fix", "उसे महत्व देकर")
phr("taṃ garuṃ", "fix", "उसे महत्व")
phr("taṃ paccavekkhati assādeti abhinandati", "fix",
    "उस पर पुनः विचार करता है, उसका रस लेता है, उसमें आनंद लेता है")
phr("taṃ garuṃ katvā paccavekkhati assādeti abhinandati", "fix",
    "उसे महत्व देकर उस पर पुनः विचार करता है, उसका रस लेता है, उसमें आनंद लेता है")
phr("uppajjati", "verb", "उत्पन्न", num="sg")
phr("uppajjanti", "verb", "उत्पन्न", num="pl")
phr("uppajanti", "verb", "उत्पन्न", num="pl", slip="uppajanti (spelling) = uppajjanti")
phr("paṭisandhikkhaṇe", "adv", S.PATISANDHI)
phr("ahetukapaṭisandhikkhaṇe", "adv", S.AHETUKA_PATISANDHI)
phr("arūpe", "adv", S.ARUPE)
phr("asaññasattānaṃ", "adv", S.ASANNASATTA)
phr("assādeti", "fix", "उसका रस लेता है")
phr("taṃ paccavekkhati", "fix", "उस पर पुनः विचार करता है")
phr("dvepi kātabbā", "fix", "दोनों तैयार करने चाहिए")
phr("dibbena cakkhunā upādinnaṃ rūpaṃ passati", "fix", "दिव्य आँख से कर्म से उत्पन्न दृश्य रूप देखता है")
phr("dibbena cakkhunā anupādinnaṃ rūpaṃ passati", "fix",
    "दिव्य आँख से कर्म से उत्पन्न न होने वाला दृश्य रूप देखता है")
phr("dibbāya sotadhātuyā anupādinnaṃ saddaṃ suṇāti", "fix",
    "दिव्य कान के तत्व से कर्म से उत्पन्न न होने वाली ध्वनि सुनता है")
phr("kusalākusale niruddhe", "fix", "हितकर और हानिकर के समाप्त होने पर")
phr("pañcannaṃ viññāṇānaṃ", "fix", "पाँच प्रकार की चेतनाओं के लिए")
phr("attānaṃ ātāpeti paritāpeti", "fix", "स्वयं को तपाता है, कष्ट देता है")
phr("pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti", "fix", "खोज के कारण होने वाले दुःख का अनुभव करता है")
phr("kusalākusalaṃ kammaṃ", "fix", "हितकर और हानिकर कर्म", subj=("m", "sg"))
for _key, _stem in [("sārammaṇa", "sārammaṇa"), ("acetasika", "acetasika"), ("cittasampayutta", "cittasampayutta"),
                    ("nocittasamuṭṭhāna", "nocittasamuṭṭhāna"), ("bāhira", "bāhira"), ("noupādā", "noupādā"),
                    ("upādinna", "upādinna"), ("anupādinna", "anupādinna"), ("cetasika", "cetasika"),
                    ("cittasamuṭṭhāna", "cittasamuṭṭhāna"), ("ajjhattika", "ajjhattika"), ("upādā", "upādā"),
                    ("nocittasahabhū", "nocittasahabhū"), ("cittasahabhū", "cittasahabhū")]:
    phr(_stem + "cittasamaṅgissa", "fix", f"{inflect(HADJ[_key], 'm', 'sg', True)} मन से युक्त व्यक्ति के")
phr("nocittasamaṅgissa", "fix", f"{inflect(HADJ['nocitta'], 'f', 'sg', True)} परिघटना से युक्त व्यक्ति के")
phr("cittasampayuttasamaṅgissa", "fix",
    f"{inflect(HADJ['cittasampayutta'], 'f', 'sg', True)} परिघटना से युक्त व्यक्ति के")
phr("dānaṃ", "fix", "दान")
phr("dānaṃ datvā", "fix", "दान देकर")
phr("sīlaṃ", "fix", "सदाचार")
phr("uposathakammaṃ katvā", "fix", "उपवास-व्रत का पालन करके")
phr("pubbe suciṇṇāni", "fix", "पहले भली-भाँति किए गए कार्य")
phr("pubbe", "fix", "पहले")
phr("jhānā", "fix", "ध्यान से")
phr("jhānā vuṭṭhahitvā", "fix", "ध्यान से उठकर")
phr("jhānā vuṭṭhahitvā jhānaṃ", "fix", "ध्यान से उठकर ध्यान")
phr("ariyā maggā vuṭṭhahitvā", "fix", "आर्य जन मार्ग से उठकर", subj=("m", "pl"))
phr("ariyā", "fix", "आर्य जन", subj=("m", "pl"))
phr("ariyā maggā", "fix", "आर्य जन मार्ग", subj=("m", "pl"))
phr("maggā vuṭṭhahitvā", "fix", "मार्ग से उठकर")
phr("dibbena cakkhunā rūpaṃ passati", "fix", "दिव्य आँख से दृश्य रूप देखता है")
phr("dibbāya sotadhātuyā saddaṃ suṇāti", "fix", "दिव्य कान के तत्व से ध्वनि सुनता है")
phr("cetopariyañāṇena", "fix", S.CETOPARIYENA)
phr("cittaṃ jānāti", "fix", "मन को जानता है")
phr("dānaṃ deti", "fix", "दान देता है")
phr("mānaṃ jappeti", "fix", "अहंकार पालता है")
phr("diṭṭhiṃ gaṇhāti", "fix", "दृष्टि अपनाता है")
phr("samāpattiṃ uppādeti", "fix", "ध्यान-अवस्था उत्पन्न करता है")
phr("pāṇaṃ hanati", "fix", "प्राणी की हत्या करता है")
phr("saṅghaṃ bhindati", "fix", "संघ में फूट डालता है")
phr("kāyikaṃ sukhaṃ", "fix", "शारीरिक सुख")
phr("kāyikaṃ dukkhaṃ", "fix", "शारीरिक दुःख")
phr("kāyikassa sukhassa", "fix", "शारीरिक सुख के लिए")
phr("kāyikassa dukkhassa", "fix", "शारीरिक दुःख के लिए")
phr("purimā purimā", "fix", "")  # placeholder, replaced below by adjective analyses
phr("vipāko tadārammaṇatā uppajjati", "fix", S.TADARAMMANA)
phr("nirodhā vuṭṭhahantassa", "fix", "निरोध की ध्यान-अवस्था से बाहर आने वाले के लिए")
del PHR[("purimā", "purimā")]
for f, cls, n in [("purimā purimā", "N", "pl"), ("purimaṃ purimaṃ", "X", "sg")]:
    add(f, ("A", "purima", cls, n))
for f, cls, n in [("pacchimānaṃ pacchimānaṃ", "D", "pl"), ("pacchimassa pacchimassa", "D", "sg")]:
    add(f, ("A", "pacchima", cls, n))
add("pacchājātā", ("L", "pacchājāta", "W", None))

MULTI_LEX = {tuple(k.split()): v for k, v in LEX.items() if " " in k}
MAXPHR = max(len(k) for k in list(PHR) + list(MULTI_LEX))

# =====================================================================================
# 4. Conditions
# =====================================================================================
_STEMS = "|".join(sorted(S.COND_KEYS, key=len, reverse=True))
ABL_RX = re.compile(r"^(na|no)?(" + _STEMS + r")paccayā$")
INS_RX = re.compile(r"^(" + _STEMS + r")paccayena$")


def cond_abl(tok):
    m = ABL_RX.match(tok.lower())
    if not m:
        return None
    return S.NABL(m.group(2)) if m.group(1) else S.ABL(m.group(2))


# =====================================================================================
# 5. Tokenizer and generic clause engine
# =====================================================================================
TOK_RX = re.compile(r"…pe…|…|–|[,;.]|[^\s,;.…–]+")


def split_ca(w):
    lw = w.lower()
    if lw in LEX or lw in ("pañca",):
        return [w]
    if lw.endswith("ñca") and len(lw) > 4:
        return [w[:-3] + "ṃ", "ca"]
    return [w]


def tokenize(text):
    out = []
    for t in TOK_RX.findall(text):
        if t in ("…pe…", "…", "–", ",", ";", "."):
            out.append(("sep", t))
        else:
            for p in split_ca(t):
                out.append(("w", p))
    return out


SEP_HI = {"…pe…": "…", "…": "…", "–": "–", ",": ",", ";": ";", ".": "।"}


class State:
    def __init__(self):
        self.subj = ("f", "sg")
        self.frame_subj = ("f", "sg")


def units(toks):
    """Group word tokens into units (longest phrase match)."""
    res, i = [], 0
    while i < len(toks):
        kind, t = toks[i]
        if kind == "sep":
            res.append(("sep", t))
            i += 1
            continue
        # longest phrase over consecutive words
        best = None
        for L in range(MAXPHR, 0, -1):
            seg = toks[i:i + L]
            if len(seg) < L or any(k != "w" for k, _ in seg):
                continue
            key = tuple(x.lower() for _, x in seg)
            if key in PHR:
                best = ("phr", L, PHR[key])
                break
            if L > 1 and key in MULTI_LEX:
                best = ("lex", L, MULTI_LEX[key])
                break
        if best and best[0] == "phr":
            kind2, hi, kw = best[2]
            res.append((kind2, hi, kw))
            if kw.get("slip"):
                SLIPS.append((CUR_LINE[0], kw["slip"]))
            i += best[1]
            continue
        if best and best[0] == "lex":
            for a in best[2]:
                res.append(("np", a))
            i += best[1]
            continue
        lw = t.lower()
        if lw == "ca":
            res.append(("ca",))
        elif lw in LEX:
            for a in LEX[lw]:
                res.append(("np", a))
        elif cond_abl(t):
            res.append(("abl", cond_abl(t)))
        elif INS_RX.match(lw):
            k = INS_RX.match(lw).group(1)
            if i + 1 < len(toks) and toks[i + 1] == ("w", "paccayo"):
                res.append(("pred", k))
                i += 1
            else:
                res.append(("ins", k))
        elif lw in NUMWORD:
            res.append(("num", NUMWORD[lw]))
        else:
            res.append(("unk", t))
        i += 1
    return res


NUMWORD = {k: v for k, v in S.NUM.items()}
NUMWORD.update({"tīṇipi": "तीनों", "dvepi": "दोनों"})


LABEL_ADJ = {"sahajāta": "sahajāta_a", "purejāta": "purejāta_a", "pacchājāta": "pacchājāta_a"}


def render_conj(words, obl):
    """One conjunct: [adjectives] [numeral] [noun]. 'CA' markers after adjectives coordinate them."""
    ca_after = set()
    clean = []
    for w in words:
        if w == "CA":
            if clean:
                ca_after.add(len(clean) - 1)
            continue
        clean.append(w)
    words = clean
    nouns = [w for w in words if w[0] == "N"]
    if nouns:  # labels standing before a noun are attributes (pacchājātā cittasamuṭṭhānā khandhā)
        words = [("A", LABEL_ADJ[w[1]], w[2], w[3]) if w[0] == "L" and w[1] in LABEL_ADJ else w for w in words]
    adjs = [w for w in words if w[0] == "A"]
    adj_ca = [i for i, w in enumerate(words) if w[0] == "A" and i in ca_after]
    nums = [w for w in words if w[0] == "U"]
    labels = [w for w in words if w[0] == "L"]
    if not nouns and not nums and len(adjs) == 1 and adjs[0][1] == "vipāka":
        return ("कर्म-फल", ("m", "sg"))
    if nouns:
        nkey, ncls, nnum = nouns[-1][1], nouns[-1][2], nouns[-1][3]
        sgd, sgo, pld, plo, g = HNOUN[nkey]
        n = nnum or (nums[-1][3] if nums else "sg")
        if nums and nums[-1][1] > 1:
            n = "pl"
    else:
        g, n = "m", (nums[-1][3] if nums else (adjs[-1][3] if adjs and adjs[-1][3] else "sg"))
        sgd = sgo = pld = plo = ""
    if labels and not nouns:
        return ", ".join(HLABEL[w[1]] for w in labels), (g, n)
    o = obl
    aw = []
    for i, w in enumerate(words):
        if w[0] != "A" or w[1] == "kabaḷī":
            continue
        aw.append((w[1], inflect(HADJ[w[1]], g, n, o), i in ca_after))
    # coordinated adjectives (X ca Y ca noun): "X और Y"
    merged = []
    for key, s, c in aw:
        if c and merged and merged[-1][2]:
            merged[-1] = (merged[-1][0], merged[-1][1] + " और " + s, True)
        else:
            merged.append((key, s, c))
    aw = [(k, s) for k, s, _ in merged]
    noun_hi = ""
    if nouns:
        noun_hi = (plo if o else pld) if n == "pl" else (sgo if o else sgd)
        if nouns[-1][1] == "āhāra" and any(w[1] == "kabaḷī" for w in adjs):
            k = HNOUN["kabaḷīkāra"]
            noun_hi = (k[3] if o else k[2]) if n == "pl" else (k[1] if o else k[0])
    num_hi = NUMW[nums[-1][1]] if nums else ""
    # join adjectives
    astr = ""
    for idx, (key, s) in enumerate(aw):
        if idx == 0:
            astr = s
        else:
            prev = aw[idx - 1][0]
            astr += (" " if (prev in NOCOMMA or key in NOCOMMA) else ", ") + s
    single = len(aw) == 1 and " " not in aw[0][1]
    if num_hi and single:
        parts = [num_hi, astr, noun_hi]
    else:
        parts = [astr, num_hi, noun_hi]
    return " ".join(p for p in parts if p), (g, n)


def render_group(grp, role, post=None, trailing_ca=False):
    """grp: list of word analyses and 'CA' markers. role: dir / obl / dat."""
    conjs, cur, has_ca = [], [], False
    for w in grp:
        if w == "CA":
            has_ca = True
            if cur:
                cur.append(w)
            continue
        cur.append(w)
        if w[0] == "N":
            conjs.append(cur)
            cur = []
    if cur and any(w != "CA" for w in cur):
        conjs.append(cur)
    obl = role in ("obl", "dat")
    rendered = [render_conj(c, obl) for c in conjs]
    strs = [r[0] for r in rendered]
    if role == "dat":
        strs = [s + " के लिए" for s in strs]
    if len(strs) == 1:
        text = strs[0]
    elif has_ca:
        text = ", ".join(strs[:-1]) + " और " + strs[-1]
    else:
        text = ", ".join(strs)
    if trailing_ca and len(strs) == 1:
        text += " और"
    if post:
        text += " " + post
    if len(rendered) == 1:
        agr = rendered[0][1]
    else:
        g = "m" if any(r[1][0] == "m" for r in rendered) else "f"
        agr = (g, "pl")
    return text, agr


def translate_clause(text, st):
    """Translate a run of Pāli (no parentheticals) into Hindi pieces."""
    us = units(tokenize(text))
    out = []
    i = 0
    while i < len(us):
        u = us[i]
        if u[0] in ("np", "ca"):
            # collect NP group: same dative-ness
            grp, j = [], i
            dat = None
            trailing_ca = False
            while j < len(us) and us[j][0] in ("np", "ca"):
                if us[j][0] == "ca":
                    grp.append("CA")
                    j += 1
                    continue
                a = us[j][1]
                isd = a[2] == "D"
                if a[2] == "W":
                    isd = dat if dat is not None else None
                    if dat is False and grp:  # W words before a dative noun belong to the dative group
                        k2 = j
                        while k2 < len(us) and (us[k2][0] == "ca" or (us[k2][0] == "np" and us[k2][1][2] == "W")):
                            k2 += 1
                        if k2 < len(us) and us[k2][0] == "np" and us[k2][1][2] == "D":
                            break
                if dat is None and a[2] != "W":
                    dat = isd
                elif a[2] != "W" and isd != dat:
                    break
                grp.append(a)
                j += 1
            if grp and grp[-1] == "CA" and (j >= len(us) or us[j][0] == "sep"):
                trailing_ca = True   # kept in grp: it still marks the coordination of several conjuncts
            nxt = us[j] if j < len(us) else None
            if dat:
                s, agr = render_group(grp, "dat", trailing_ca=trailing_ca)
                out.append(s)
                i = j
                continue
            if nxt and nxt[0] == "post":
                post = nxt[1]
                if nxt[2].get("pl"):
                    _, agr0 = render_group(grp, "obl")
                    if agr0[1] == "pl":
                        post = nxt[2]["pl"]
                s, agr = render_group(grp, "obl", post=post, trailing_ca=trailing_ca)
                out.append(s)
                i = j + 1
                continue
            accish = any(a != "CA" and a[2] == "A" for a in grp)
            role = "obl" if accish else "dir"
            s, agr = render_group(grp, role, trailing_ca=trailing_ca)
            if role == "dir" and any(a != "CA" and a[0] in ("N", "A") for a in grp):
                st.subj = agr
            out.append(s)
            i = j
            continue
        if u[0] == "sep":
            out.append(("SEP", SEP_HI[u[1]]))
        elif u[0] in ("fix", "adv", "post"):
            out.append(u[1])
            if u[2].get("subj"):
                st.subj = u[2]["subj"]
        elif u[0] == "verb":
            out.append(f"{u[1]} {BE(*st.subj)}")
        elif u[0] == "pred":
            subj = st.frame_subj if (i > 0 and us[i - 1][0] == "sep" and us[i - 1][1] in ("…", "…pe…")) else st.subj
            out.append(f"{S.INS(u[1])} {BE(*subj)}")
        elif u[0] == "ins":
            out.append(S.INS(u[1]))
        elif u[0] == "abl":
            out.append(u[1])
        elif u[0] == "num":
            out.append(u[1])
        elif u[0] == "unk":
            out.append(unk(u[1]))
        i += 1
    return out


def join_pieces(pieces):
    """Join Hindi pieces: separators attach to the previous word; a space follows them."""
    s = ""
    for p in pieces:
        if isinstance(p, tuple):
            sep = p[1]
            s = s.rstrip(" ")
            if sep == "–":
                s += " –"
            else:
                s += sep
            continue
        if s and not s.endswith(" "):
            s += " "
        s += p
    return s


def fix_spacing(s):
    s = re.sub(r" +", " ", s)
    s = re.sub(r"(…)(?=[^\s…।,;)\]])", r"\1 ", s)
    s = re.sub(r"([,;।])(?=[^\s…।,;)\]])", r"\1 ", s)
    s = re.sub(r"–(?=\S)", "– ", s)
    s = re.sub(r"(?<=\S)–", " –", s)
    return s.strip()


# =====================================================================================
# 6. Frames (item tables)
# =====================================================================================
ITEM_FORMS = {}   # Pāli form -> (key, set of cases)  cases: acc / nom / dat (+ "_ca" variants)


def _reg(form, key, case):
    k0, cs = ITEM_FORMS.get(form, (key, set()))
    cs.add(case)
    ITEM_FORMS[form] = (key, cs)


def _item_forms(key, stem, kind):
    if kind == "a":
        forms = [(stem + "aṃ", "acc"), (stem + "o", "nom"), (stem + "assa", "dat"), (stem + "añca", "acc_ca"),
                 (stem + "o ca", "nom_ca"), (stem + "assa ca", "dat_ca")]
    elif kind == "u":
        forms = [(stem + "uṃ", "acc"), (stem + "ū", "nom"), (stem + "ussa", "dat"), (stem + "uñca", "acc_ca"),
                 (stem + "u ca", "nom_ca"), (stem + "ū ca", "nom_ca"), (stem + "ussa ca", "dat_ca")]
    elif kind == "i":
        forms = [(stem + "iṃ", "acc"), (stem + "i", "nom"), (stem + "issa", "dat"), (stem + "iñca", "acc_ca"),
                 (stem + "i ca", "nom_ca"), (stem + "issa ca", "dat_ca")]
    else:  # indeclinable (upādā / noupādā)
        forms = [(stem, "acc"), (stem, "nom"), (stem, "dat"), (stem + "ñca", "acc_ca"), (stem + " ca", "nom_ca"),
                 (stem + " ca", "dat_ca"), (stem + " ca", "acc_ca")]
    for f, c in forms:
        _reg(f, key, c)


FRAME_ITEMS = [(k, s, kd) for k, s, kd in ITEM_STEMS if not s.endswith("ak")] + [
    ("citta_i", "citt", "a"), ("upādā", "upādā", "w"), ("noupādā", "noupādā", "w")]
for k, s, kd in FRAME_ITEMS:
    _item_forms(k, s, kd)
_reg("no upādā", "noupādā", "nom")   # spacing slip (line 2605)

_IF = "|".join(sorted((re.escape(f) for f in ITEM_FORMS), key=len, reverse=True))
ITEM_RX = re.compile(r"(?:" + _IF + r")(?![^\s])")


def item_hi(key, g="f", n="sg", obl=False):
    return inflect(HADJ[key], g, n, obl)


def parse_items(s, case):
    """'sārammaṇañca anārammaṇañca' -> ['sārammaṇa', 'anārammaṇa'] (case-checked)."""
    s = s.strip()
    keys, pos = [], 0
    while pos < len(s):
        m = ITEM_RX.match(s, pos)
        if not m:
            return None
        k, cs = ITEM_FORMS[m.group(0)]
        if not any(c.startswith(case) for c in cs):
            return None
        if m.group(0) == "no upādā":
            SLIPS.append((CUR_LINE[0], "'No upādā' written apart (= Noupādā)"))
        keys.append(k)
        pos = m.end()
        while pos < len(s) and s[pos] == " ":
            pos += 1
    return keys


def OBJ(keys):
    w = [f"{item_hi(k)} {S.DHAMMA}" for k in keys]
    return w[0] if len(w) == 1 else ", ".join(w[:-1]) + " और " + w[-1]


def RES(keys):
    if len(keys) == 1:
        return f"{item_hi(keys[0])} {S.DHAMMA}"
    w = [item_hi(k, "f", "pl") for k in keys]
    return ", ".join(w[:-1]) + " और " + w[-1] + " " + S.DHAMMA_PL


def DAT(keys):
    return OBJ(keys) + " के लिए"


DEP_RX = r"(paṭicca|paccayā|nissāya|saṃsaṭṭho|saṃsaṭṭhā|sampayutto|sampayuttā|sahajāto|sahajātā)"
DEP_KEY = {"paṭicca": "paṭicca", "paccayā": "paccaya", "nissāya": "nissaya", "saṃsaṭṭho": "saṃsaṭṭha",
           "saṃsaṭṭhā": "saṃsaṭṭha", "sampayutto": "sampayutta", "sampayuttā": "sampayutta",
           "sahajāto": "sahajāta", "sahajātā": "sahajāta"}
ABL_TOK = r"(?:na|no)?(?:" + _STEMS + r")paccayā"
FRAME1 = re.compile(r"^(?P<o>.+?) dhammaṃ " + DEP_RX + r" (?P<r>.+?) (?P<d>dhammo|dhammā) "
                    r"(?P<v>uppajjati|uppajjanti)(?P<c>(?: ?…(?:pe…)? ?| )" + ABL_TOK + r"(?:(?:…(?:pe…)? ?)"
                    + ABL_TOK + r")*)?")
FRAME2 = re.compile(r"^(?P<s>.+?) (?P<d>dhammo|dhammā) (?P<t>[^ ]+ dhammassa ca(?: [^ ]+ dhammassa ca)+|.+? dhammassa|"
                    r"[^ ]+(?= sahajātaṃ))(?P<p> (?:" + _STEMS + r")paccayena paccayo)?")


def frame1(m, st):
    o = parse_items(m.group("o").lower(), "acc")
    r = parse_items(m.group("r"), "nom")
    if o is None or r is None:
        return None
    dep = S.DEP[DEP_KEY[m.group(2)]]
    pl = len(r) > 1
    if (m.group("d") == "dhammā") != pl:
        SLIPS.append((CUR_LINE[0], f"'{m.group('r')} {m.group('d')}': number of dhamma does not match the items"))
    if (m.group("v") == "uppajjanti") != pl:
        SLIPS.append((CUR_LINE[0], f"'{m.group('d')} {m.group('v')}': verb number does not match"))
    verb = "उत्पन्न होती हैं" if pl else "उत्पन्न होती है"
    conds = ""
    if m.group("c"):
        cs = re.findall(ABL_TOK, m.group("c"))
        seps = re.split(ABL_TOK, m.group("c"))[1:-1]
        parts = []
        for idx, c in enumerate(cs):
            parts.append(cond_abl(c))
            if idx < len(seps):
                parts.append("…")
        conds = "".join(p if p == "…" else (p if not parts or True else p) for p in parts)
        conds = re.sub(r"…(?=\S)", "… ", conds)
        conds = " " + conds
    st.subj = st.frame_subj = ("f", "pl" if pl else "sg")
    return f"{OBJ(o)} {dep} {RES(r)}{conds} {verb}"


def frame2(m, st):
    s = parse_items(m.group("s").lower(), "nom")
    traw = m.group("t")
    if "dhammassa" not in traw:
        SLIPS.append((CUR_LINE[0], f"'{traw}' without 'dhammassa' (translated as written, dative item)"))
    t = parse_items(traw.replace(" dhammassa ca", " ca").replace(" dhammassa", ""), "dat")
    if s is None or t is None:
        return None
    pl = len(s) > 1
    if (m.group("d") == "dhammā") != pl:
        SLIPS.append((CUR_LINE[0], f"'{m.group('s')} {m.group('d')}': number of dhamma does not match"))
    st.subj = st.frame_subj = ("f", "pl" if pl else "sg")
    out = f"{RES(s)}, {DAT(t)}"
    if m.group("p"):
        k = INS_RX.match(m.group("p").split()[0]).group(1)
        out += f" {S.INS(k)} {BE('f', 'pl' if pl else 'sg')}"
    return out


# =====================================================================================
# 7. Parentheticals, headings, special lines
# =====================================================================================
def DK(key):    # Sārammaṇadukaṃ -> "विषय वाली परिघटनाओं वाला दो का वर्गीकरण"
    return f"{item_hi(key, 'f', 'pl')} परिघटनाओं वाला दो का वर्गीकरण"


def DKO(key):   # oblique: "... वाले दो के वर्गीकरण"
    return f"{item_hi(key, 'f', 'pl')} परिघटनाओं वाले दो के वर्गीकरण"


DUKA_KEYS = {
    "Sārammaṇa": "sārammaṇa", "Citta": "citta_i", "Cetasika": "cetasika", "Cittasampayutta": "cittasampayutta",
    "Cittasaṃsaṭṭha": "cittasaṃsaṭṭha", "Cittasamuṭṭhāna": "cittasamuṭṭhāna", "Cittasahabhū": "cittasahabhū",
    "Cittānuparivatti": "cittānuparivatti", "Cittasaṃsaṭṭhasamuṭṭhāna": "cssam",
    "Cittasaṃsaṭṭhasamuṭṭhānasahabhū": "cssah", "Cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "csanu",
    "Ajjhattika": "ajjhattika", "Upādā": "upādā", "Upādinna": "upādinna",
}

HEAD = {
    "Mahantaradukaṃ": "बीच के बड़े दो-दो के वर्गीकरण",
    "Paṭiccavāro": S.VARA["paṭicca"], "Sahajātavāro": S.VARA["sahajāta"], "Paccayavāro": S.VARA["paccaya"],
    "Nissayavāro": S.VARA["nissaya"], "Saṃsaṭṭhavāro": S.VARA["saṃsaṭṭha"],
    "Sampayuttavāro": S.VARA["sampayutta"], "Pañhāvāro": S.VARA["pañhā"], "Vibhaṅgavāro": S.VARA["vibhaṅga"],
    "Saṅkhyāvāro": S.VARA["saṅkhyā"],
    "Paccayānulomaṃ": S.PACCAYANULOMA, "Paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "Paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA, "Paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA,
    "1-4. Paccayānulomādi": "1-4. " + S.PACCAYANULOMA + " आदि",
    "Suddhaṃ": S.SUDDHA,
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों का चयन",
    "Pacchājātāsevanapaccayā": f"{S.NAME('pacchājāta')} और {S.NAME('āsevana')}",
    "Vipāka-āhārapaccayā": f"{S.NAME('vipāka')} और {S.NAME('āhāra')}",
    "Vipākāhārapaccayā": f"{S.NAME('vipāka')} और {S.NAME('āhāra')}",
    "Kamma-vipākapaccayā": f"{S.NAME('kamma')} और {S.NAME('vipāka')}",
    "Anantara-samanantarapaccayā": f"{S.NAME('anantara')} और {S.NAME('samanantara')}",
}
for _p, _k in DUKA_KEYS.items():
    HEAD[_p + "dukaṃ"] = DK(_k)
for _k in S.COND_KEYS:
    _neg = S.NEG_PREFIX_PALI[_k]
    _cap = _k[0].upper() + _k[1:]
    HEAD[_cap + "paccayo"] = S.NAME(_k)
    HEAD[_cap + "paccayādi"] = S.NAME(_k) + " आदि"
    HEAD[_neg.capitalize() + _k + "paccayo"] = S.NNAME(_k)
    HEAD[_neg.capitalize() + _k + "paccayādi"] = S.NNAME(_k) + " आदि"

LINES = {
    "Mahantaradukaṃ niṭṭhitaṃ.": "बीच के बड़े दो-दो के वर्गीकरण समाप्त।",
    "Anulomaṃ.": S.ANULOMA + "।",
    "Paccanīyaṃ.": S.PACCANIYA + "।",
}
for _p, _k in DUKA_KEYS.items():
    LINES[_p + "dukaṃ niṭṭhitaṃ."] = DK(_k) + " समाप्त।"

NINNA = "बिना किसी अंतर के"
KT1, KT2, KT3 = "तैयार करना चाहिए", "तैयार करने चाहिए", "तैयार करनी चाहिए"   # kātabbaṃ / kātabbā (m) / (f)
P_SAMA = "निर्भरता के खंड के समान"        # paṭicca(vāra)sadisaṃ
C_SAMA = "कारण के खंड के समान"            # paccayavārasadisaṃ
MOHO3 = "मोह केवल तीन में"                 # tīṇiyeva moho / tīsuyeva moho
PURE_S = f"{S.NAME('purejāta')} के समान"   # purejātasadisaṃ
PATHAMA = "पहले प्रसंग के समान"           # paṭhamagamanasadisaṃ
NAVA9 = "नौ के नौ प्रश्न"                  # navapi pañhā
EVA = "इसी प्रकार"                         # evaṃ
ITARE = "बाकी दोनों गणनाएँ भी"             # itare dve gaṇanāpi
UPADAMULA = "व्युत्पन्न न होने वाली परिघटना से शुरू होने वाली शृंखला में"     # noupādāmūlake
UPADINNAMULA = "कर्म से उत्पन्न परिघटना से शुरू होने वाली शृंखला में"         # upādinnamūlake
PS = S.PATISANDHI
PANCAV = "पाँच प्रकार की चेतना"

PAREN = {
    "saṃkhittaṃ": "संक्षिप्त", "Saṃkhittaṃ": "संक्षिप्त", "Saṃkhittaṃ.": "संक्षिप्त।",
    "saṃkhittaṃ.": "संक्षिप्त।",
    "saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni.":
        "संक्षिप्त, जैसे पद रखे गए हैं वैसे उनका विस्तार करना चाहिए।",
    "Cittasaṃsaṭṭhadukaṃ yathā cittasampayuttadukaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ.":
        f"{DK('cittasaṃsaṭṭha')} को {DKO('cittasampayutta')} की तरह ही {KT1}, {NINNA}।",
    "Ekāyeva adhipati kātabbā, navapi pañhā. Yathā cittasahabhūdukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ":
        f"केवल एक प्रधानता {KT3}, {NAVA9}। जैसे {DK('cittasahabhū')}, वैसे ही {KT1}, {NINNA}",
    "Evaṃ dve pañhā pavattipaṭisandhi kātabbā. Saṃkhittaṃ.":
        f"{EVA} दो प्रश्न, जीवन-प्रवाह में और पुनर्जन्म में, {KT2}। संक्षिप्त।",
    "Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.": f"{EVA} {ITARE} और आश्रय का खंड भी {KT1}।",
    "Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.": f"{EVA} {ITARE} और जुड़ाव का खंड भी {KT1}।",
    "Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbā.": f"{EVA} {ITARE} और जुड़ाव का खंड भी {KT2}।",
    "Evaṃ itare dve gaṇanāpi sampayuttavāropi sabbe kātabbā.":
        f"{EVA} {ITARE} और जुड़ाव का खंड भी, सभी {KT2}।",
    "Evaṃ itare dve gaṇanāpi sampayuttavārāpi kātabbā.": f"{EVA} {ITARE} और जुड़ाव के खंड भी {KT2}।",
    'Evaṃ navapi pañhā kātabbā. "Ahetuka"nti niyāmetabbaṃ. Yathā anulome labbhati evaṃ kātabbaṃ. '
    'Tīṇi moho yathā cittasamuṭṭhānaduke evameva kātabbā.':
        f"{EVA} {NAVA9} {KT2}। “मूल से रहित” कहकर निश्चित करना चाहिए। जैसा सकारात्मक क्रम में मिलता है, "
        f"वैसा ही {KT1}। मोह वाले तीन, जैसे {DKO('cittasamuṭṭhāna')} में, ठीक वैसे ही {KT2}।",
    "Evaṃ navapi pañhā kātabbā. Ahetukanti sabbattha niyāmetabbaṃ, ekaṃyeva mohaṃ mūlapade.":
        f"{EVA} {NAVA9} {KT2}। हर जगह “मूल से रहित” कहकर निश्चित करना चाहिए, मूल पद में केवल एक मोह।",
    "Idha atthi sabbaṭṭhāne sahajātaṃ paccayavārasadisaṃ. Purejātaṃ purejātasadisaṃ. "
    "Pacchājātaṃ pacchājātasadisaṃ kātabbaṃ, ninnānākaraṇaṃ":
        f"यहाँ उपस्थिति-कारण में हर स्थान पर सह-उत्पत्ति रूपी {C_SAMA} है। पूर्व-उत्पत्ति रूपी {PURE_S} है। "
        f"पश्चात्-उत्पत्ति रूपी को {S.NAME('pacchājāta')} के समान {KT1}, {NINNA}",
    "Imaṃ cittasamuṭṭhānadukaṃ paccayavāre ārammaṇasadisaṃ. Channampi imesaṃ pañcaviññāṇamūlā kātabbā. "
    "Saṃkhittaṃ.":
        f"यह {DK('cittasamuṭṭhāna')} कारण के खंड में {S.NAME('ārammaṇa')} के समान है। इन छहों के लिए भी "
        f"{PANCAV} से शुरू होने वाली शृंखलाएँ {KT3}। संक्षिप्त।",
    "Itare dve gaṇanāpi sampayuttavāropi kātabbo.": f"{ITARE} और जुड़ाव का खंड भी {KT1}।",
    "Itare dve gaṇanāpi sampayuttavāropi sabbaṃ kātabbaṃ.": f"{ITARE} और जुड़ाव का खंड भी, सब {KT1}।",
    "Mūlaṃ": "मूल पद",
    "Mūlaṃ kātabbaṃ": f"मूल पद {KT1}",
    "Mūlaṃ pucchitabbaṃ": "मूल पद पूछना चाहिए",
    "Mūlaṃ pucchitabbaṃ ": "मूल पद पूछना चाहिए",
    "Mūlaṃ pucchitabbaṃ, tīṇi upanissayā": "मूल पद पूछना चाहिए, तीन प्रबल आश्रय",
    "Nava pañhā pañcaviññāṇampi yathā ārammaṇapaccayā evaṃ kātabbaṃ, tīsuyeva moho. "
    "Sabbe pañhā pavattipaṭisandhiyā kātabbā asammohantena.":
        f"नौ प्रश्न, {PANCAV} भी, जैसे {S.NAME('ārammaṇa')} में, वैसे ही {KT2}, {MOHO3}। सभी प्रश्न "
        f"जीवन-प्रवाह और पुनर्जन्म के लिए बिना भ्रमित हुए {KT2}।",
    "Nissayavāro paccayavārasadiso.": f"{S.VARA['nissaya']} {C_SAMA} है।",
    "Sabbe navapi pañhā kātabbā, paṭiccavārasadisā. Pañcaviññāṇampi kātabbaṃ. Tīṇiyeva moho.":
        f"सभी {NAVA9} {KT2}, {P_SAMA}। {PANCAV} भी {KT3}। {MOHO3}।",
    "Sahajātavāro paṭiccavārasadiso.": f"{S.VARA['sahajāta']} {P_SAMA} है।",
    "Sahajātavāropi paṭiccavārasadiso.": f"{S.VARA['sahajāta']} भी {P_SAMA} है।",
    "Saṃkhittaṃ. Evaṃ navapi pañhā kātabbā. Pañcaviññāṇampi pavesetvā tīṇiyeva moho.":
        f"संक्षिप्त। {EVA} {NAVA9} {KT2}। {PANCAV} को भी शामिल करके, {MOHO3}।",
    "Saṃkhittaṃ. Sabbaṃ kātabbaṃ. Paccayavārassa pañcaviññāṇaṃ channampi mūlā kātabbā. "
    "Sabbe mahābhūte tīṇiyeva moho. Saṃkhittaṃ.":
        f"संक्षिप्त। सब {KT1}। कारण के खंड की {PANCAV}: छहों के मूल पद {KT2}। सभी महाभूत, {MOHO3}। संक्षिप्त।",
    "Saṃkhittaṃ. Yathā cittasahabhūduke ārammaṇaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ. Navapi pañhā.":
        f"संक्षिप्त। जैसे {DKO('cittasahabhū')} में {S.NAME('ārammaṇa')}, वैसे ही {KT1}, {NINNA}। {NAVA9}।",
    "ahetukapaṭisandhikkhaṇe dvepi kātabbā": f"{S.AHETUKA_PATISANDHI} दोनों {KT2}",
    "anulomagaṇanā kātabbā": "सकारात्मक क्रम की गणना करनी चाहिए",
    "anulomamātikā kātabbā": f"सकारात्मक क्रम की मूल सूची {KT3}",
    "anulomamātikā vitthāretabbā": "सकारात्मक क्रम की मूल सूची का विस्तार करना चाहिए",
    "anulomaṃ": S.ANULOMA,
    "arūpaṃ sabbaṃ uddharitabbaṃ. Cittasamuṭṭhānadukasadisaṃ.":
        f"सारा अभौतिक निकाल लेना चाहिए। {DKO('cittasamuṭṭhāna')} के समान।",
    "cakkaṃ": "चक्र",
    "cittasahabhūdukasadisā ninnānākaraṇā. Tīṇipi sahajātā, nānākkhaṇikā":
        f"{DKO('cittasahabhū')} के समान, {NINNA}। तीनों में सह-उत्पत्ति रूपी, भिन्न क्षणों वाला",
    "cittasahabhūdukasadisā, ninnānākaraṇaṃ": f"{DKO('cittasahabhū')} के समान, {NINNA}",
    "cittasahabhūdukasadisā, ninnānākaraṇaṃ. Tīṇipi pacchājātā. Dve. Ekamūlānaṃ ekā ghaṭanā":
        f"{DKO('cittasahabhū')} के समान, {NINNA}। तीनों में पश्चात्-उत्पत्ति रूपी। दो। "
        f"एक मूल पद वालों का एक मेल",
    "cittasahabhūgamanasadisā, ekaṃyeva kabaḷīkāraṃ āhāraṃ":
        f"{item_hi('cittasahabhū', 'f', 'pl')} परिघटनाओं वाले प्रसंग के समान, केवल एक "
        f"कौर-कौर खाया जाने वाला भोजन",
    "cittasamuṭṭhānadukasadisaṃ": f"{DKO('cittasamuṭṭhāna')} के समान",
    "cittasamuṭṭhānadukasadisaṃ, ninnānākaraṇaṃ": f"{DKO('cittasamuṭṭhāna')} के समान, {NINNA}",
    "cittasamuṭṭhānadukasadisā": f"{DKO('cittasamuṭṭhāna')} के समान",
    "cittasamuṭṭhānadukasadisā. Imampi ekaṃ kabaḷīkāraāhārasadisaṃ":
        f"{DKO('cittasamuṭṭhāna')} के समान। यह एक भी कौर-कौर खाए जाने वाले भोजन के समान",
    "dve adhipatī tiṇṇampi kātabbā": f"दोनों प्रधानताएँ तीनों के लिए {KT3}",
    "dvepi adhipati kātabbā": f"दोनों प्रधानताएँ {KT3}",
    "dvepi adhipatī kātabbā": f"दोनों प्रधानताएँ {KT3}",
    "dvepi gamanā paṭhamagamanasadisaṃ ninnānākaraṇaṃ. Ārammaṇādhipati sahajātādhipati kātabbā":
        f"दोनों प्रसंग {PATHAMA}, {NINNA}। {S.ARAMMANADHIPATI}, {S.SAHAJATADHIPATI} {KT3}",
    "evaṃ gaṇetabbaṃ": f"{EVA} गिनना चाहिए",
    "evaṃ itare dvepi gaṇanā kātabbā": f"{EVA} बाकी दोनों गणनाएँ भी {KT3}",
    "evaṃ nava pañhā kātabbā. Paccayavāre pañcaviññāṇampi kātabbaṃ, tīṇiyeva moho":
        f"{EVA} नौ प्रश्न {KT2}। कारण के खंड में {PANCAV} भी {KT3}, {MOHO3}",
    "evaṃ navapi pañhā kātabbā": f"{EVA} {NAVA9} {KT2}",
    "evaṃ pañca kātabbā, tīṇiyeva moho": f"{EVA} पाँच {KT2}, {MOHO3}",
    "evaṃ pañcapi pañhā kātabbā, tīṇiyeva moho. Saṃkhittaṃ": f"{EVA} पाँचों प्रश्न {KT2}, {MOHO3}। संक्षिप्त",
    "evaṃ tīṇi kātabbāni, paṭhamagamanasadisaṃ. Pūritvā kātabbaṃ, ninnānākaraṇaṃ":
        f"{EVA} तीन {KT2}, {PATHAMA}। पूरा करके {KT1}, {NINNA}",
    "ime dve pūretukāmena kātabbā, purimagamanasadisaṃ":
        f"पूरा करना चाहने वाले को ये दोनों {KT2}, पिछले प्रसंग के समान",
    "ime dvepi pūretukāmena sabbattha kātabbā, paṭhamagamanasadisaṃ ninnānākaraṇaṃ":
        f"पूरा करना चाहने वाले को ये दोनों हर जगह {KT2}, {PATHAMA}, {NINNA}",
    "iminākāreneva pacchājāto vitthāretabbo": "इसी ढंग से पश्चात्-उत्पत्ति रूपी का विस्तार करना चाहिए",
    "itare dve gaṇanā, imassa sadisāyeva kātabbā": f"बाकी दोनों गणनाएँ, इसी के समान ही {KT3}",
    "mahābhūtā chasupi pañhesu kātabbā, adhipatiyā tīsu natthi.":
        f"महाभूत छहों प्रश्नों में {KT2}, {S.NAME('adhipati')} में तीन में नहीं हैं।",
    "nahetusadisaṃ, moho natthi": f"{S.SADISA('hetu', neg=True)}, मोह नहीं है",
    "nava pañhā kātabbā": f"नौ प्रश्न {KT2}",
    "navapi pañhā cittasahabhūdukasadisā": f"{NAVA9} {DKO('cittasahabhū')} के समान",
    "navapi pañhā cittasahabhūdukasadisā, ninnānākaraṇaṃ": f"{NAVA9} {DKO('cittasahabhū')} के समान, {NINNA}",
    "nocittasahabhū mūlaṃyeva labbhati, cittasamuṭṭhānadukasadisā. Tīṇipi ninnānākaraṇaṃ":
        f"केवल {item_hi('nocittasahabhū')} परिघटना ही मूल पद के रूप में मिलती है, "
        f"{DKO('cittasamuṭṭhāna')} के समान। तीनों {NINNA}",
    "noupādāmūlake tīṇi, paṭisandhikkhaṇe tīṇipi kātabbā": f"{UPADAMULA} तीन, {PS} तीनों {KT2}",
    "noupādāmūlake tīṇipi paṭiccasadisā, ninnānākaraṇā": f"{UPADAMULA} तीनों {P_SAMA}, {NINNA}",
    "paccanīyaṃ": S.PACCANIYA,
    "paccayasadisā": C_SAMA,
    "paccayavārasadisaṃ": C_SAMA,
    "paccayavārasadisā": C_SAMA,
    "paccayavārasadisaṃ paṭisandhipi pavattipi kātabbā sabbesampi pañhānaṃ.":
        f"{C_SAMA}, सभी प्रश्नों के लिए पुनर्जन्म भी और जीवन-प्रवाह भी {KT2}।",
    "paccayavārasadisā, pañhāghaṭanā natthi": f"{C_SAMA}, प्रश्नों का मेल नहीं है",
    "paccayavāre nissayasadisaṃ": f"कारण के खंड में {S.SADISA('nissaya')}",
    "paccayavāre nissayasadiso": f"कारण के खंड में {S.SADISA('nissaya')}",
    "paccayavāre nissayasadisā": f"कारण के खंड में {S.SADISA('nissaya')}",
    "pacchājātasadisaṃ kātabbaṃ": f"{S.SADISA('pacchājāta')} {KT1}",
    "pañca pañhā kātabbā. Tīṇi. Moho": f"पाँच प्रश्न {KT2}। तीन। मोह",
    "paṭhamagamanasadisaṃ": PATHAMA,
    "paṭhamagamanasadisaṃ ninnānākaraṇaṃ, imaṃ nānaṃ": f"{PATHAMA}, {NINNA}, यह अंतर है",
    "paṭhamagamanaṃ": "पहला प्रसंग",
    "paṭiccasadisaṃ": P_SAMA, "paṭiccasadisā": P_SAMA,
    "paṭiccavārasadisaṃ": P_SAMA, "paṭiccavārasadisā": P_SAMA,
    "paṭiccasadisaṃ, sabbe mahābhūtā": f"{P_SAMA}, सभी महाभूत",
    "paṭiccavārasadisaṃ, sabbe mahābhūtā": f"{P_SAMA}, सभी महाभूत",
    "paṭiccasadisā, pañhāghaṭanā natthi": f"{P_SAMA}, प्रश्नों का मेल नहीं है",
    "paṭiccavāre aññamaññasadisaṃ": f"निर्भरता के खंड में {S.SADISA('aññamañña')}",
    "paṭiccavāre sahajātasadisā": f"निर्भरता के खंड में {S.SADISA('sahajāta')}",
    "paṭisandhikkhaṇe": PS,
    "paṭisandhikkhaṇe dve": f"{PS} दो",
    "paṭisandhikkhaṇe dve kātabbā": f"{PS} दो {KT2}",
    "paṭisandhikkhaṇe dve, saṃkhittaṃ": f"{PS} दो, संक्षिप्त",
    "paṭisandhikkhaṇe dvepi": f"{PS} दोनों",
    "paṭisandhikkhaṇe dvepi kātabbā": f"{PS} दोनों {KT2}",
    "paṭisandhikkhaṇe dvepi kātabbā paṭiccavārasadisā": f"{PS} दोनों {KT2}, {P_SAMA}",
    "paṭisandhikkhaṇe dvepi kātabbā, saṃkhittaṃ": f"{PS} दोनों {KT2}, संक्षिप्त",
    "paṭisandhikkhaṇe dvepi kātabbā, yāva ajjhattikā mahābhūtā": f"{PS} दोनों {KT2}, आंतरिक महाभूतों तक",
    "paṭisandhikkhaṇe dvepi paṭiccavārasadisā": f"{PS} दोनों {P_SAMA}",
    "paṭisandhikkhaṇe ekaṃ": f"{PS} एक",
    "paṭisandhikkhaṇe ekaṃ kātabbaṃ": f"{PS} एक {KT1}",
    "paṭisandhikkhaṇe ekaṃ kātabbaṃ, saṃkhittaṃ": f"{PS} एक {KT1}, संक्षिप्त",
    "paṭisandhikkhaṇe ekaṃ, saṃkhittaṃ": f"{PS} एक, संक्षिप्त",
    "paṭisandhikkhaṇe tīṇi kātabbā": f"{PS} तीन {KT2}",
    "paṭisandhikkhaṇe tīṇipi kātabbā": f"{PS} तीनों {KT2}",
    "paṭisandhikkhaṇe tīṇipi kātabbā paṭiccavārasadisā": f"{PS} तीनों {KT2}, {P_SAMA}",
    "paṭisandhikkhaṇepi dve": f"{PS} भी दो",
    "paṭisandhiyā dve kātabbā": f"पुनर्जन्म के लिए दो {KT2}",
    "purejātasadisaṃ": PURE_S,
    "purejātasadisaṃ ninnānaṃ": f"{PURE_S}, {NINNA}",
    "purejātasadisaṃ ninnānākaraṇaṃ": f"{PURE_S}, {NINNA}",
    "purejātasadisaṃ purejātaṃ kātabbaṃ. Sabbaṃ saṃkhittaṃ. Vitthāretabbaṃ":
        f"पूर्व-उत्पत्ति रूपी को {PURE_S} {KT1}। सब संक्षिप्त है। विस्तार करना चाहिए",
    "purejātasadisaṃ, ninnānākaraṇaṃ": f"{PURE_S}, {NINNA}",
    "purejātasadisaṃ, saṃkhittaṃ": f"{PURE_S}, संक्षिप्त",
    "sabbattha ekaṃ": "हर जगह एक", "sabbattha nava": "हर जगह नौ", "sabbattha pañca": "हर जगह पाँच",
    "sabbattha satta": "हर जगह सात", "sabbattha tīṇi": "हर जगह तीन",
    "sabbattha nava, anulomamātikā": "हर जगह नौ, सकारात्मक क्रम की मूल सूची",
    "sabbaṃ paṭisandhiyaṃ kātabbaṃ, sahajātaṃ purejātampi":
        f"पुनर्जन्म में सब {KT1}, सह-उत्पत्ति रूपी और पूर्व-उत्पत्ति रूपी भी",
    "sabbaṃ vitthāretabbaṃ": "सबका विस्तार करना चाहिए",
    "sabbe mahābhūtā paṭiccasadisaṃ": f"सभी महाभूत, {P_SAMA}",
    "sahajātapaccayavārasadisaṃ ninnānākaraṇaṃ, paṭhamagamanasadisaṃyeva. "
    "Sabbe padā paṭhamaghaṭanānayena vibhajitabbā":
        f"सह-उत्पत्ति-कारण वाले खंड के समान, {NINNA}, पहले प्रसंग के समान ही। सभी पदों का पहले मेल की विधि से "
        f"विश्लेषण करना चाहिए",
    "saṃkhittaṃ, sabbaṃ kātabbaṃ": f"संक्षिप्त, सब {KT1}",
    "saṃkhittaṃ, yathā nikkhittapadāni vibhajitabbāni":
        "संक्षिप्त, जैसे पद रखे गए हैं वैसे उनका विश्लेषण करना चाहिए",
    "saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni":
        "संक्षिप्त, जैसे पद रखे गए हैं वैसे उनका विस्तार करना चाहिए",
    "saṃkhittaṃ. Purejātasadisaṃ ninnānākaraṇaṃ": f"संक्षिप्त। {PURE_S}, {NINNA}",
    "saṃkhittaṃ. Sabbe padā vibhajitabbā paṭhamaghaṭanānayena":
        "संक्षिप्त। सभी पदों का पहले मेल की विधि से विश्लेषण करना चाहिए",
    "saṃkhittaṃ. Tīṇiyeva moho": f"संक्षिप्त। {MOHO3}",
    "saṃkhittaṃ. Upādinnamūlake tīṇi. ": f"संक्षिप्त। {UPADINNAMULA} तीन।",
    "saṃkhittaṃ. Yathā nikkhittapadāni vibhajitabbāni paripuṇṇāni":
        "संक्षिप्त। जैसे पद रखे गए हैं वैसे उनका पूरा-पूरा विश्लेषण करना चाहिए",
    "tiṇṇampi ekasadisā": "तीनों एक जैसे",
    "tiṇṇampi ekāyeva adhipati": "तीनों के लिए केवल एक प्रधानता",
    "tīṇi kātabbā, vuṭṭhānaṃ natthi": f"तीन {KT2}, बाहर आना नहीं है",
    "tīṇi pañhā kātabbā": f"तीन प्रश्न {KT2}",
    "tīṇi, moho": "तीन, मोह",
    "tīṇi, paṭhamagamanasadisaṃ ninnānākaraṇaṃ": f"तीन, {PATHAMA}, {NINNA}",
    "tīṇipi garukārammaṇā kātabbā, ārammaṇādhipatiyeva":
        f"तीनों महत्व दिए गए विषय वाले {KT2}, केवल {S.ARAMMANADHIPATI}",
    "tīṇipi paṭiccasadisā, ninnānākaraṇā": f"तीनों {P_SAMA}, {NINNA}",
    "tīṇipi pūretvā kātabbā, cittassāti kātabbā, sampayuttakānañcāti kātabbā":
        f"तीनों पूरे करके {KT2}, “मन के लिए” {KT1}, “और जुड़े हुओं के लिए” {KT1}",
    "tīṇipi ārammaṇādhipati, sahajātādhipatipi kātabbā":
        f"तीनों में {S.ARAMMANADHIPATI}, {S.SAHAJATADHIPATI} भी {KT3}",
    "upādinnamūlake tīṇi, paṭhamasseva rūpajīvitindriyaṃ, itaresu natthi":
        f"{UPADINNAMULA} तीन, {S.RUPAJIVITINDRIYA} केवल पहले में, बाकियों में नहीं है",
    "vuṭṭhānaṃ natthi": "बाहर आना नहीं है",
    "yathā cittasahabhūdukaṃ evaṃ imaṃ dukaṃ kātabbaṃ, ninnānākaraṇaṃ":
        f"जैसे {DK('cittasahabhū')}, वैसे ही यह दो का वर्गीकरण {KT1}, {NINNA}",
    "yathā cittasaṃsaṭṭhasamuṭṭhānadukasadisaṃ, ninnānākaraṇaṃ": f"{DKO('cssam')} के समान ही, {NINNA}",
    "yathā cittasaṃsaṭṭhasamuṭṭhānadukaṃ, evaṃ imampi dukaṃ, ninnānākaraṇaṃ":
        f"जैसे {DK('cssam')}, वैसे ही यह दो का वर्गीकरण भी, {NINNA}",
    "yāva asaññasattā": "पहचान-रहित प्राणियों तक",
    "yāva asaññasattā kātabbā": f"पहचान-रहित प्राणियों तक {KT2}",
    "yāva asaññasattā, evaṃ tīṇi noupādāmūlake": f"पहचान-रहित प्राणियों तक, {EVA} {UPADAMULA} तीन",
    "yāva mahābhūtā": "महाभूतों तक",
    "yāva utusamuṭṭhānaṃ": "तापमान से उत्पन्न तक",
    "ārabbha kātabbā": f"“को विषय बनाकर” के रूप में {KT2}",
    "ārammaṇādhipatipi sahajātādhipatipi imesampi tiṇṇaṃ kātabbā. Navapi pañhā cittasamuṭṭhānadukasadisā. "
    "Ante tīṇi ārammaṇādhipatiyeva":
        f"इन तीनों के लिए भी {S.ARAMMANADHIPATI} भी और {S.SAHAJATADHIPATI} भी {KT3}। {NAVA9} "
        f"{DKO('cittasamuṭṭhāna')} के समान। अंत के तीन में केवल {S.ARAMMANADHIPATI}",
    "ārammaṇādhipatipi sahajātādhipatipi kātabbā": f"{S.ARAMMANADHIPATI} भी और {S.SAHAJATADHIPATI} भी {KT3}",
    "ārammaṇādhipatiyeva": f"केवल {S.ARAMMANADHIPATI}",
    "āvajjanāpi vuṭṭhānampi natthi": "न मन को विषय की ओर मोड़ना है, न बाहर आना",
}


def translate_text(text, st):
    """Translate a Pāli text run that may contain parentheticals."""
    if text.count("(") > text.count(")"):
        m = re.search(r"\(([^()]*?)\s*(\(\d+\))\s*$", text)
        if m:
            SLIPS.append((CUR_LINE[0], f"bracket '({m.group(1)}' not closed (kept unclosed)"))
            inner = PAREN.get(m.group(1)) or unk("PAREN:" + m.group(1))
            pre = translate_text(text[:m.start()], st)
            return fix_spacing(pre + " (" + inner + " " + m.group(2))
    pieces = []
    pos = 0
    for m in re.finditer(r"\(([^()]*)\)", text):
        before = text[pos:m.start()]
        if before.strip():
            pieces.append(("T", before))
        pieces.append(("P", m.group(1)))
        pos = m.end()
    if text[pos:].strip():
        pieces.append(("T", text[pos:]))
    out = ""
    for kind, t in pieces:
        if kind == "P":
            if re.fullmatch(r"\d+", t):
                h = f"({t})"
            elif t in PAREN:
                h = f"({PAREN[t]})"
            else:
                h = "(" + unk("PAREN:" + t) + ")"
            out = out.rstrip(" ") + " " + h + " "
            continue
        # leading punctuation of the run attaches to the previous text
        hi = translate_run(t, st)
        if hi.startswith(("।", ",", ";", "…")) or not out:
            out = out.rstrip(" ") + hi if hi[:1] in "।,;…" else out + hi
        else:
            out = out.rstrip(" ") + " " + hi
    return fix_spacing(out)


SENT_RX = re.compile(r"(?<=\.)\s+(?=[A-ZĀĪŪṬḌṆÑṄḶṂ])")


def translate_run(t, st):
    """Split into sentences (". " + capital); each sentence may start with a frame or be a count line."""
    lead_punct = re.match(r"^\s*([.,;]*)\s*", t)
    head = lead_punct.group(1)
    body = t[lead_punct.end():]
    pieces = []
    if head:
        pieces.append(("SEP", "।" if head == "." else head.replace("…pe…", "…")))
    sents = SENT_RX.split(body) if body.strip() else []
    for sn in sents:
        pieces.append(translate_sentence(sn, st))
    return join_pieces(pieces)


def translate_sentence(t, st):
    lead = t.strip()
    m = FRAME1.match(lead)
    if m:
        h = frame1(m, st)
        if h is not None:
            rest = lead[m.end():]
            return join_pieces([h] + translate_clause(rest, st)) if rest.strip() else h
    m = FRAME2.match(lead)
    if m:
        h = frame2(m, st)
        if h is not None:
            rest = lead[m.end():]
            return join_pieces([h] + translate_clause(rest, st)) if rest.strip() else h
    if COUNT_START.match(lead.lower()):
        try:
            return S.count_hi(lead)
        except ValueError:
            pass
    return join_pieces(translate_clause(lead, st))


COUNT_START = re.compile(r"^(?:(?:na|no) ?)?(?:" + "|".join(sorted(S.COND_LOC_PALI.values(), key=len, reverse=True))
                         + r"|(?:na|no)?(?:" + _STEMS + r")paccayā)\b")


def count_line(body):
    pieces = []
    pos = 0
    for m in re.finditer(r"\(([^()]*)\)", body):
        pieces.append(("T", body[pos:m.start()]))
        pieces.append(("P", m.group(1)))
        pos = m.end()
    pieces.append(("T", body[pos:]))
    out = ""
    for kind, t in pieces:
        if kind == "P":
            if t in PAREN:
                out = out.rstrip(" ") + f" ({PAREN[t]})"
            else:
                out = out.rstrip(" ") + " (" + unk("PAREN:" + t) + ")"
            continue
        if not t.strip():
            out += t
            continue
        h = S.count_hi(t.strip())
        if h[:1] in ",।…;":
            out = out.rstrip(" ") + h
        else:
            out = out.rstrip(" ") + " " + h
    return fix_spacing(out)


def translate_line(line, st):
    body = S.ID_RX.sub("", line).rstrip()
    if body.startswith("#"):
        hashes = body[: len(body) - len(body.lstrip("#"))]
        txt = body[len(hashes):].strip()
        ital = txt.startswith("*") and txt.endswith("*")
        core = txt.strip("*")
        h = HEAD.get(core)
        if h is None:
            h = unk("HEAD:" + core)
        return f"{hashes} " + (f"*{h}*" if ital else h)
    if body in LINES:
        return LINES[body]
    if "Upādā dhammañca noupādā dhammañca dhammaṃ" in body:
        SLIPS.append((CUR_LINE[0], "'Upādā dhammañca noupādā dhammañca dhammaṃ': dhamma written three times "
                                   "(rendered as the usual pair)"))
        body = body.replace("Upādā dhammañca noupādā dhammañca dhammaṃ", "Upādā ca noupādā ca dhammaṃ")
    if COUNT_START.match(body.lower()):
        try:
            return count_line(body)
        except ValueError:
            pass
    return translate_text(body, st)


# =====================================================================================
# 8. Build, write, check
# =====================================================================================
def build():
    src = SRC.read_text(encoding="utf-8")
    H = []
    st = State()
    for n, line in enumerate(src.splitlines(), 1):
        if not line.strip():
            continue
        CUR_LINE[0] = n
        if not line.startswith("#"):
            st = State()
        H.append(translate_line(line, st))
    return S.assemble(src, H)


def main():
    text = build()
    if "--unk" in sys.argv:
        seen = {}
        for n, w in UNK:
            seen.setdefault(w, []).append(n)
        for w, ns in sorted(seen.items(), key=lambda x: -len(x[1])):
            print(len(ns), w, ns[:6])
        print("UNK total", len(UNK), "unique", len(seen))
        return
    if "--slips" in sys.argv:
        for n, s in SLIPS:
            print(n, s)
        return
    if UNK:
        print("UNTRANSLATED:", len(UNK))
    if "--check" not in sys.argv:
        with open(OUT, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("wrote", OUT)
    sys.exit(1 if S.check([(SRC, OUT)]) else 0)


if __name__ == "__main__":
    main()
