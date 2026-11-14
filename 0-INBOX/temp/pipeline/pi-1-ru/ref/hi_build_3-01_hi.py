"""Build the Hindi plain zero-shot of pi-1 part 3-01 (Rūpakaṇḍa: opening statement, matrix, Ekakaniddesa).

usage: python -I -X utf8 build_3-01_hi.py
Sentence-level translation with fixed predicate strings, so every repeat is byte-identical
(structure mirrors pi-1-en/build_3-01.py). Predicates that are matrix items are taken from
build_matika_hi.BARE and only adapted in gender (परिघटनाएँ, fem. pl. -> भौतिक रूप, masc. sg.).
Importing this module does not write the file.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_hi as M  # noqa: E402

ROOT = HERE.parents[3]
PART = "3-01-rupakandam.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / PART
OUT = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters" / PART

DASH = "–"
PE = "…"
D = M.DANDA
RF = "भौतिक रूप"          # rūpa (matter), masc.
SABBA = "सारा भौतिक रूप"   # sabbaṃ rūpaṃ


def V(kind, sigla, text):
    label = "पाठभेद" if kind == "p" else "वर्तनी-भेद"
    return f" [{label} ({sigla}): {text}]"


# ---- headings and closing lines (hi-zeroshot-terms.md, verbatim) -----------------------------
HEAD = {
    "Rūpakaṇḍaṃ": "भौतिक रूप का अध्याय",
    "Uddeso": "रूपरेखा",
    "Mātikā": "मूल सूची",
    "Ekakaṃ": "एकल वर्गीकरण",
    "Dukaṃ": "दो-दो के वर्गीकरण",
    "Tikaṃ": "तीन-तीन के वर्गीकरण",
    "Catukkaṃ": "चार-चार के वर्गीकरण",
    "Pañcakaṃ": "पाँच-पाँच के वर्गीकरण",
    "Chakkaṃ": "छह-छह के वर्गीकरण",
    "Sattakaṃ": "सात-सात के वर्गीकरण",
    "Aṭṭhakaṃ": "आठ-आठ के वर्गीकरण",
    "Navakaṃ": "नौ-नौ के वर्गीकरण",
    "Dasakaṃ": "दस-दस के वर्गीकरण",
    "Ekādasakaṃ": "ग्यारह-ग्यारह के वर्गीकरण",
    "Rūpavibhatti": "भौतिक रूप का वर्गीकरण",
    "Ekakaniddeso": "एकल वर्गीकरण की व्याख्या",
}
CLOSE = {h + ".": HEAD[h] + D for h in HEAD if h not in ("Rūpakaṇḍaṃ", "Uddeso", "Rūpavibhatti")}
WAYS = {"ekavidhena": "एक", "duvidhena": "दो", "tividhena": "तीन", "catubbidhena": "चार",
        "pañcavidhena": "पाँच", "chabbidhena": "छह", "sattavidhena": "सात", "aṭṭhavidhena": "आठ",
        "navavidhena": "नौ", "dasavidhena": "दस", "ekādasavidhena": "ग्यारह"}
for k, v in WAYS.items():
    # Evaṃ X-vidhena rūpasaṅgaho. / X-vidhena rūpasaṅgaho –
    CLOSE[f"Evaṃ {k} rūpasaṅgaho."] = f"इस तरह {v} प्रकार से {RF} का वर्गीकरण हुआ{D}"
    CLOSE[f"{k[0].upper() + k[1:]} rūpasaṅgaho –"] = f"{v} प्रकार से {RF} का वर्गीकरण {DASH}"


# ---- matrix item names in the masculine singular ----------------------------------------------
GENDER_TOKENS = {"वाली": "वाला", "जुड़ी": "जुड़ा", "हुई": "हुआ", "समाई": "समाया", "चुकी": "चुका",
                 "छोड़ी": "छोड़ा", "जानी": "जाना"}


def masc(key):
    """Matrix item (BARE) without 'परिघटनाएँ', adapted to masc. sg. Only gender endings change."""
    s = M.BARE[key]
    assert s.endswith(" परिघटनाएँ"), s
    s = s[: -len(" परिघटनाएँ")]
    s = " ".join(GENDER_TOKENS.get(w.rstrip(","), w.rstrip(",")) + ("," if w.endswith(",") else "")
                 for w in s.split(" "))
    return s.replace("चरण की", "चरण का").replace("मन की सहचर", "मन का सहचर")


def mi(bid, letter):
    return masc((bid, letter))


# ---- predicates: Pāli -> (complement, negated) -------------------------------------------------
# 'X है' / 'X नहीं है'; in '…pe…' chains the copula stands only after the last member.
P = {}


def pair(pos, neg, hi_pos, hi_neg=None):
    P[pos] = (hi_pos, False)
    P[neg] = (hi_neg, False) if hi_neg is not None else (hi_pos, True)


# matrix items (word for word, gender-adapted)
pair("upādā", "no upādā", mi("1-M2-67", "क"), mi("1-M2-67", "ख"))
pair("upādiṇṇaṃ", "anupādiṇṇaṃ", mi("1-M2-68", "क"), mi("1-M2-68", "ख"))
pair("upādiṇṇupādāniyaṃ", "anupādiṇṇupādāniyaṃ", mi("1-M1-4", "क"), mi("1-M1-4", "ख"))
pair("sanidassanaṃ", "anidassanaṃ", mi("1-M2-9", "क"), mi("1-M2-9", "ख"))
pair("sappaṭighaṃ", "appaṭighaṃ", mi("1-M2-10", "क"), mi("1-M2-10", "ख"))
pair("cittasamuṭṭhānaṃ", "na cittasamuṭṭhānaṃ", mi("1-M2-60", "क"), mi("1-M2-60", "ख"))
pair("cittasahabhu", "na cittasahabhu", mi("1-M2-61", "क"), mi("1-M2-61", "ख"))
pair("cittānuparivatti", "na cittānuparivatti", mi("1-M2-62", "क"), mi("1-M2-62", "ख"))
pair("ajjhattikaṃ", "bāhiraṃ", mi("1-M2-66", "क"), mi("1-M2-66", "ख"))
# other predicates
pair("indriyaṃ", "na indriyaṃ", "क्षमता")
pair("mahābhūtaṃ", "na mahābhūtaṃ", "महाभूत")
pair("viññatti", "na viññatti", "प्रकट अभिव्यक्ति")
pair("oḷārikaṃ", "sukhumaṃ", "स्थूल", "सूक्ष्म")
pair("dūre", "santike", "दूर", "निकट")
SENSE = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर"}
for s, h in SENSE.items():
    pair(f"{s}samphassassa vatthu", f"{s}samphassassa na vatthu", f"{h} के संपर्क का आधार")
    pair(f"{s}viññāṇassa vatthu", f"{s}viññāṇassa na vatthu", f"{h} की चेतना का आधार")
    pair(f"{s}samphassassa ārammaṇaṃ", f"{s}samphassassa nārammaṇaṃ", f"{h} के संपर्क का विषय")
    pair(f"{s}viññāṇassa ārammaṇaṃ", f"{s}viññāṇassa nārammaṇaṃ", f"{h} की चेतना का विषय")
AYATANA = {"cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र", "sotāyatanaṃ": "कान का इंद्रिय-क्षेत्र",
           "ghānāyatanaṃ": "नाक का इंद्रिय-क्षेत्र", "jivhāyatanaṃ": "जीभ का इंद्रिय-क्षेत्र",
           "kāyāyatanaṃ": "शरीर का इंद्रिय-क्षेत्र", "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र",
           "saddāyatanaṃ": "ध्वनि का इंद्रिय-क्षेत्र", "gandhāyatanaṃ": "गंध का इंद्रिय-क्षेत्र",
           "rasāyatanaṃ": "स्वाद का इंद्रिय-क्षेत्र", "phoṭṭhabbāyatanaṃ": "स्पर्श का इंद्रिय-क्षेत्र"}
DHATU = {"cakkhudhātu": "आँख का तत्व", "sotadhātu": "कान का तत्व", "ghānadhātu": "नाक का तत्व",
         "jivhādhātu": "जीभ का तत्व", "kāyadhātu": "शरीर का तत्व", "rūpadhātu": "दृश्य रूप का तत्व",
         "saddadhātu": "ध्वनि का तत्व", "gandhadhātu": "गंध का तत्व", "rasadhātu": "स्वाद का तत्व",
         "phoṭṭhabbadhātu": "स्पर्श का तत्व",
         "ākāsadhātu": "आकाश तत्व", "āpodhātu": "जल तत्व", "pathavīdhātu": "पृथ्वी तत्व",
         "tejodhātu": "अग्नि तत्व", "vāyodhātu": "वायु तत्व"}
INDRIYA = {"cakkhundriyaṃ": "आँख की क्षमता", "sotindriyaṃ": "कान की क्षमता", "ghānindriyaṃ": "नाक की क्षमता",
           "jivhindriyaṃ": "जीभ की क्षमता", "kāyindriyaṃ": "शरीर की क्षमता",
           "itthindriyaṃ": "स्त्रीत्व की क्षमता", "purisindriyaṃ": "पुरुषत्व की क्षमता",
           "jīvitindriyaṃ": "जीवन-क्षमता"}
OTHER = {"kāyaviññatti": "शरीर द्वारा प्रकट अभिव्यक्ति", "vacīviññatti": "वाणी द्वारा प्रकट अभिव्यक्ति",
         "kabaḷīkāro āhāro": "कौर-कौर खाया जाने वाला भोजन"}
for d in (AYATANA, DHATU, INDRIYA, OTHER):
    for k, v in d.items():
        pair(k, "na " + k, v)
RUPASSA = {"lahutā": "का हल्कापन", "mudutā": "की मृदुता", "kammaññatā": "की कार्य-योग्यता",
           "upacayo": "की वृद्धि", "santati": "की धारा", "jaratā": "का बुढ़ापा", "aniccatā": "की अनित्यता"}
for k, v in RUPASSA.items():
    pair(f"rūpassa {k}", f"rūpassa na {k}", f"{RF} {v}")


def pred(p):
    c, neg = P[p]
    return c + (" नहीं है" if neg else " है")


def member(p):
    c, neg = P[p]
    return c + (" नहीं" if neg else "")


def chain(items):
    """'X…pe… Y…pe… Z': members joined with '… '."""
    return (PE + " ").join(items)


# ---- sentence patterns ---------------------------------------------------------------------------
RE_ATTHI = re.compile(r"^Atthi rūpaṃ (.+?), atthi rūpaṃ (.+?)\.$")
RE_YAM1 = re.compile(r"^Yaṃ taṃ rūpaṃ (.+?), taṃ (?!atthi )(.+?)\.$")
RE_YAM2 = re.compile(r"^Yaṃ taṃ rūpaṃ (.+?), taṃ atthi (.+?),? atthi (.+?)\.$")


def s_atthi(a, b):
    """Atthi rūpaṃ X, atthi rūpaṃ Y."""
    return f"कुछ {RF} {a}, कुछ {RF} {b}{D}"


def s_yam1(a, b):
    """Yaṃ taṃ rūpaṃ A, taṃ X."""
    return f"जो {RF} {pred(a)}, वह {b}{D}"


def s_yam2(a, x, y):
    """Yaṃ taṃ rūpaṃ A, taṃ atthi X, atthi Y."""
    return f"जो {RF} {pred(a)}, उसमें से कुछ {pred(x)} और कुछ {pred(y)}{D}"


# '…pe…' chains, written out from the fixed strings above
def contact_chain(what):
    """sotasamphassassa…pe… ghāna…pe… jivhā…pe… kāyasamphassassa <vatthu|ārammaṇaṃ> (last member bare)."""
    return chain([f"{SENSE[s]} के संपर्क का" for s in ("sota", "ghāna", "jivhā")] + [f"शरीर के संपर्क का {what}"])


def fpc(sense, what):
    """X-samphassajāya vedanāya…pe… saññāya…pe… cetanāya…pe… X-viññāṇassa <vatthu|ārammaṇaṃ>."""
    h = SENSE[sense]
    return chain([f"{h} के संपर्क से उत्पन्न अनुभूति का", "पहचान का", "इरादे का", f"{h} की चेतना का {what}"])


SPECIAL = {}
for s in ("cakkhu", "kāya"):
    for gap in ("cetanāya…pe…", "cetanāya …pe…"):  # ^1-U1 has a stray space once; same Hindi
        SPECIAL[f"Atthi rūpaṃ {s}samphassajāya vedanāya…pe… saññāya…pe… {gap} {s}viññāṇassa vatthu, "
                f"atthi rūpaṃ {s}viññāṇassa na vatthu."] = \
            s_atthi(fpc(s, "आधार") + " है", pred(f"{s}viññāṇassa na vatthu"))
    SPECIAL[f"Atthi rūpaṃ {s}samphassajāya vedanāya…pe… saññāya…pe… cetanāya…pe… {s}viññāṇassa ārammaṇaṃ, "
            f"atthi rūpaṃ {s}viññāṇassa nārammaṇaṃ."] = \
        s_atthi(fpc(s, "विषय") + " है", pred(f"{s}viññāṇassa nārammaṇaṃ"))
    SPECIAL[f"Yaṃ taṃ rūpaṃ bāhiraṃ, taṃ {s}samphassajāya vedanāya…pe… saññāya…pe… cetanāya…pe… "
            f"{s}viññāṇassa na vatthu."] = s_yam1("bāhiraṃ", fpc(s, "आधार") + " नहीं है")
    SPECIAL[f"Yaṃ taṃ rūpaṃ ajjhattikaṃ, taṃ {s}samphassajāya vedanāya…pe… saññāya…pe… cetanāya…pe… "
            f"{s}viññāṇassa nārammaṇaṃ."] = s_yam1("ajjhattikaṃ", fpc(s, "विषय") + " नहीं है")
SPECIAL.update({
    "Atthi rūpaṃ sotasamphassassa…pe… ghānasamphassassa…pe… jivhāsamphassassa…pe… kāyasamphassassa vatthu, "
    "atthi rūpaṃ kāyasamphassassa na vatthu.":
        s_atthi(contact_chain("आधार") + " है", pred("kāyasamphassassa na vatthu")),
    "Atthi rūpaṃ sotasamphassassa…pe… ghānasamphassassa…pe… jivhāsamphassassa…pe… kāyasamphassassa ārammaṇaṃ, "
    "atthi rūpaṃ kāyasamphassassa nārammaṇaṃ.":
        s_atthi(contact_chain("विषय") + " है", pred("kāyasamphassassa nārammaṇaṃ")),
    "Yaṃ taṃ rūpaṃ bāhiraṃ, taṃ sotasamphassassa…pe… ghānasamphassassa…pe… jivhāsamphassassa…pe… "
    "kāyasamphassassa na vatthu.":
        s_yam1("bāhiraṃ", contact_chain("आधार") + " नहीं है"),
    "Yaṃ taṃ rūpaṃ ajjhattikaṃ, taṃ sotasamphassassa…pe… ghānasamphassassa…pe… jivhāsamphassassa…pe… "
    "kāyasamphassassa nārammaṇaṃ.":
        s_yam1("ajjhattikaṃ", contact_chain("विषय") + " नहीं है"),
})
SENSE_AY = ["sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ"]
OBJ_AY = ["saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ"]
SENSE_DH = ["sotadhātu", "ghānadhātu", "jivhādhātu", "kāyadhātu"]
OBJ_DH = ["saddadhātu", "gandhadhātu", "rasadhātu", "phoṭṭhabbadhātu"]
SENSE_IN = ["sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ"]
for keys in (SENSE_AY, OBJ_AY, SENSE_DH, OBJ_DH, SENSE_IN):
    pali_pos = "…pe… ".join(keys)
    pali_neg = "…pe… ".join("na " + k for k in keys)
    last = keys[-1]
    SPECIAL[f"Atthi rūpaṃ {pali_pos}, atthi rūpaṃ na {last}."] = \
        s_atthi(chain([member(k) for k in keys[:-1]] + [pred(last)]), pred("na " + last))
    for who in ("ajjhattikaṃ", "bāhiraṃ"):
        SPECIAL[f"Yaṃ taṃ rūpaṃ {who}, taṃ {pali_neg}."] = \
            s_yam1(who, chain([member("na " + k) for k in keys[:-1]] + [pred("na " + last)]))

# ---- Uddeso ----------------------------------------------------------------------------------------
ABY = M.BARE[("1-M1-1", "ग")]
KUS = M.BARE[("1-M1-1", "क")].replace(" परिघटनाएँ", "")
AKUS = M.BARE[("1-M1-1", "ख")].replace(" परिघटनाएँ", "")
UDDESO_P = ("Katame dhammā abyākatā? Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā "
            "apariyāpannā vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho, ye ca dhammā kiriyā "
            "neva kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ, asaṅkhatā ca dhātu – ime dhammā abyākatā.")
UDDESO_H = (M.QUESTION(ABY) + f" {KUS} और {AKUS} परिघटनाओं के कर्म-फल, जो "
            + mi("1-M2-93", "क") + ", " + mi("1-M2-94", "क") + ", " + mi("1-M2-95", "क")
            + " या अस्तित्व के लोकों में न समाए हुए हैं, यानी अनुभूति का समूह, पहचान का समूह, "
            "मानसिक रचनाओं का समूह और चेतना का समूह; और वे परिघटनाएँ जो केवल क्रिया रूपी हैं, "
            f"न {KUS}, न {AKUS} और न ही कर्म-फल; और {SABBA}; और अनिर्मित तत्व {DASH} " + M.ANSWER(ABY))

# ---- Ekaka (^1-584) and Ekakaniddesa (^1-594) --------------------------------------------------------
# (Pāli, complement, negated). Matrix items gender-adapted; 'na X' of a triad member that has no
# matrix negative = 'X नहीं है'.
EKAKA = [
    ("na hetu", mi("1-M2-1", "ख"), False),
    ("ahetukaṃ", mi("1-M2-2", "ख"), False),
    ("hetuvippayuttaṃ", mi("1-M2-3", "ख"), False),
    ("sappaccayaṃ", mi("1-M2-7", "क"), False),
    ("saṅkhataṃ", mi("1-M2-8", "क"), False),
    ("rūpaṃ [rūpiyaṃ (sī.)]", mi("1-M2-11", "क") + V("p", "Sī.", "rūpiyaṃ"), False),
    ("lokiyaṃ", mi("1-M2-12", "क"), False),
    ("sāsavaṃ", mi("1-M2-15", "क"), False),
    ("saṃyojaniyaṃ", mi("1-M2-21", "क"), False),
    ("ganthaniyaṃ", mi("1-M2-27", "क"), False),
    ("oghaniyaṃ", mi("1-M2-33", "क"), False),
    ("yoganiyaṃ", mi("1-M2-39", "क"), False),
    ("nīvaraṇiyaṃ", mi("1-M2-45", "क"), False),
    ("parāmaṭṭhaṃ", mi("1-M2-51", "क"), False),
    ("upādāniyaṃ", mi("1-M2-70", "क"), False),
    ("saṃkilesikaṃ", mi("1-M2-76", "क"), False),
    ("abyākataṃ", mi("1-M1-1", "ग"), False),
    ("anārammaṇaṃ", mi("1-M2-55", "ख"), False),
    ("acetasikaṃ", mi("1-M2-57", "ख"), False),
    ("cittavippayuttaṃ", mi("1-M2-58", "ख"), False),
    ("nevavipākanavipākadhammadhammaṃ", mi("1-M1-3", "ग"), False),
    ("asaṃkiliṭṭhasaṃkilesikaṃ", mi("1-M1-5", "ख"), False),
    ("na savitakkasavicāraṃ", mi("1-M1-6", "क"), True),
    ("na avitakkavicāramattaṃ", mi("1-M1-6", "ख"), True),
    ("avitakkaavicāraṃ", mi("1-M1-6", "ग"), False),
    ("na pītisahagataṃ", mi("1-M2-90", "ख"), False),
    ("na sukhasahagataṃ", mi("1-M2-91", "ख"), False),
    ("na upekkhāsahagataṃ", mi("1-M2-92", "ख"), False),
    ("neva dassanena na bhāvanāya pahātabbaṃ", mi("1-M1-8", "ग"), False),
    ("neva dassanena na bhāvanāya pahātabbahetukaṃ", mi("1-M1-9", "ग"), False),
    ("neva ācayagāmi na apacayagāmi", mi("1-M1-10", "ग"), False),
    ("nevasekkhanāsekkhaṃ", mi("1-M1-11", "ग"), False),
    ("parittaṃ", mi("1-M1-12", "क"), False),
    ("kāmāvacaraṃ", mi("1-M2-93", "क"), False),
    ("na rūpāvacaraṃ", mi("1-M2-94", "ख"), False),
    ("na arūpāvacaraṃ", mi("1-M2-95", "ख"), False),
    ("pariyāpannaṃ", mi("1-M2-96", "क"), False),
    # 'not among the states not included …': the matrix item kept verbatim (oblique plural)
    ("no apariyāpannaṃ", M.BARE[("1-M2-96", "ख")].replace("परिघटनाएँ", "परिघटनाओं में से"), True),
    ("aniyataṃ", mi("1-M1-15", "ग"), False),
    ("aniyyānikaṃ", mi("1-M2-97", "ख"), False),
    ("uppannaṃ", mi("1-M1-17", "क"), False),
    ("chahi viññāṇehi viññeyyaṃ", "छह प्रकार की चेतना से जाना जा सकने वाला", False),
    ("aniccaṃ", "अनित्य", False),
    ("jarābhibhūtaṃ", "बुढ़ापे से ग्रस्त", False),
]


def ek(c, neg):
    return c + (" नहीं है" if neg else " है")


def ek_meva(c, neg):
    """-meva: 'X ही है' / 'X है ही नहीं'."""
    return c + (" है ही नहीं" if neg else " ही है")


EKAKA_HEAD_P = ("Tattha katamaṃ sabbaṃ rūpaṃ? Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – "
                "idaṃ vuccati sabbaṃ rūpaṃ. ")
UPADA = mi("1-M2-67", "क")
EKAKA_HEAD_H = (f"इनमें से {SABBA} क्या है? चार महाभूत और चार महाभूतों से {UPADA} {RF} {DASH} "
                f"इसे {SABBA} कहा जाता है{D} ")
EKAKA_P = EKAKA_HEAD_P + "Sabbaṃ rūpaṃ " + ", ".join(p for p, _, _ in EKAKA) + "."
EKAKA_H = EKAKA_HEAD_H + f"{SABBA} " + ", ".join(ek(c, n) for _, c, n in EKAKA) + D


def meva(p):
    p = re.sub(r" \[.*?\]", "", p)
    return (p[:-1] if p.endswith("ṃ") else p) + "meva"


# ^1-594: every item with '-meva'; 'uppannaṃ chahi viññāṇehi viññeyyameva' is one item there (no comma)
NIDDESA = []
for p, c, n in EKAKA:
    if p == "uppannaṃ":
        continue
    if p == "chahi viññāṇehi viññeyyaṃ":
        NIDDESA.append(("uppannaṃ chahi viññāṇehi viññeyyameva", "उत्पन्न होकर " + c, n))
        continue
    NIDDESA.append((meva(p), M.BRACKET.sub("", c), n))
NIDDESA_P = "Sabbaṃ rūpaṃ " + ", ".join(p for p, _, _ in NIDDESA) + "."
NIDDESA_H = f"{SABBA} " + ", ".join(ek_meva(c, n) for _, c, n in NIDDESA) + D

# ---- the lists of ^1-586 … ^1-593 ------------------------------------------------------------------
VINNEYYA = "से जाना जा सकने वाला"
KNOW5 = ", ".join(f"{SENSE[s]} {VINNEYYA} {RF}" for s in SENSE)
KNOW_MANO = f"मन {VINNEYYA} {RF}"
KNOW_MD = f"मन के तत्व {VINNEYYA} {RF}"
KNOW_MVD = f"मन की चेतना के तत्व {VINNEYYA} {RF}"
IND8 = ", ".join(INDRIYA.values())
NOT_IND = pred("na indriyaṃ")
LISTS = {
    "Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ.": f"देखा हुआ, सुना हुआ, अनुभव किया हुआ, जाना हुआ {RF}{D}",
    "Pathavīdhātu, āpodhātu, tejodhātu, vāyodhātu, yañca rūpaṃ upādā.":
        ", ".join(DHATU[k] for k in ("pathavīdhātu", "āpodhātu", "tejodhātu", "vāyodhātu"))
        + f" और जो {RF} {pred('upādā')}{D}",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "manoviññeyyaṃ rūpaṃ.":
        f"{KNOW5}, {KNOW_MANO}{D}",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        f"{KNOW5}, {KNOW_MD}, {KNOW_MVD}{D}",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ, manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        f"{KNOW5}, जिसमें से कुछ सुखद संपर्क वाला है, कुछ दुःखद संपर्क वाला है, {KNOW_MD}, {KNOW_MVD}{D}",
    # the Pāli lacks a comma after jivhindriyaṃ in ^1-591 and ^1-592
    "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, "
    "jīvitindriyaṃ, yañca rūpaṃ na indriyaṃ.":
        f"{IND8} और जो {RF} {NOT_IND}{D}",
    "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, "
    "jīvitindriyaṃ, na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ.":
        f"{IND8} और जो {RF} {NOT_IND}, उसमें से कुछ {pred('sappaṭighaṃ')} और कुछ {pred('appaṭighaṃ')}{D}",
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, "
    "gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, yañca rūpaṃ anidassanaappaṭighaṃ "
    "[anidassanaṃ appaṭighaṃ (sī. syā.)] dhammāyatanapariyāpannaṃ.":
        ", ".join(AYATANA.values()) + f" और जो {RF} {P['anidassanaṃ'][0]} और {P['appaṭighaṃ'][0]}"
        + V("s", "Sī., Syā.", "anidassanaṃ appaṭighaṃ")
        + f" है तथा मन के विषयों के इंद्रिय-क्षेत्र में {mi('1-M2-96', 'क').split(' में ')[1]} है{D}",
}
WHOLE = {UDDESO_P: UDDESO_H, NIDDESA_P: NIDDESA_H, EKAKA_P: EKAKA_H}
WHOLE.update(LISTS)
WHOLE.update(CLOSE)


def tr_sentence(s):
    if s in SPECIAL:
        return SPECIAL[s]
    m = RE_ATTHI.match(s)
    if m:
        return s_atthi(pred(m[1]), pred(m[2]))
    m = RE_YAM2.match(s)
    if m:
        return s_yam2(m[1], m[2], m[3])
    m = RE_YAM1.match(s)
    if m:
        return s_yam1(m[1], pred(m[2]))
    raise KeyError(f"no rule for sentence: {s!r}")


def split_sentences(line):
    return re.split(r"(?<=\.) (?=(?:Atthi rūpaṃ|Yaṃ taṃ rūpaṃ) )", line)


def tr_line(line):
    if line in WHOLE:
        return WHOLE[line]
    return " ".join(tr_sentence(s) for s in split_sentences(line))


LATIN = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪ]")


def build():
    out = []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            out.append("")
            continue
        m = re.match(r"^(.*?)(\s*\^[0-9A-Za-z-]+)?$", line)
        body, bid = m.group(1), m.group(2) or ""
        if body.startswith("#"):
            hashes, title = body.split(" ", 1)
            h = f"{hashes} {HEAD[title]}"
        else:
            h = tr_line(body)
        assert body.count("–") + body.count("—") == h.count("–"), (body, h)
        assert body.count("[") == h.count("["), (body, h)
        assert not LATIN.search(M.BRACKET.sub("", h)), h
        out.append(h + bid)
    return "\n".join(out).rstrip("\n") + "\n"


TEXT = build()
assert "—" not in TEXT and ":-" not in TEXT and "\n\n\n" not in TEXT

if __name__ == "__main__":
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT)
