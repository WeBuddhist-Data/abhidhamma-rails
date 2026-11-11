"""Build the Hindi plain zero-shot of pi-1 parts 3-02 and 3-03 (Rūpakaṇḍa, Rūpavibhatti:
the pairs, triads, fours ... elevens).

usage: python -I -X utf8 build_3-02_3-03_hi.py
Mirrors 0-INBOX/temp/pipeline/pi-1-en/build_3-02_3-03.py. Every recurring string is a fixed
constant, so every repeat is byte-identical. Unknown Pāli raises an error instead of being guessed.
Matrix-derived predicates are taken from build_matika_hi.BARE (masculine singular, agreeing with
भौतिक रूप); ch.2 strings (lahutā, mudutā, kammaññatā, life) from build_ch2_01_sample_hi.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SRC = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters"
PARTS = ["3-02-rupakandam.md", "3-03-rupakandam.md"]

sys.path.insert(0, str(HERE))
import build_matika_hi as M  # noqa: E402  (importing only computes the text, it does not write)
import build_ch2_01_sample_hi as C  # noqa: E402

DASH = C.DASH
DANDA = M.DANDA
V = C.V
RUPA = "भौतिक रूप"  # rūpa (matter)


# =====================================================================================
# 1. Item names of material form (noun phrases)
# =====================================================================================
ITEMS = {
    "cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र",
    "sotāyatanaṃ": "कान का इंद्रिय-क्षेत्र",
    "ghānāyatanaṃ": "नाक का इंद्रिय-क्षेत्र",
    "jivhāyatanaṃ": "जीभ का इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ": "शरीर का इंद्रिय-क्षेत्र",
    "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र",
    "saddāyatanaṃ": "ध्वनि का इंद्रिय-क्षेत्र",
    "gandhāyatanaṃ": "गंध का इंद्रिय-क्षेत्र",
    "rasāyatanaṃ": "स्वाद का इंद्रिय-क्षेत्र",
    "phoṭṭhabbāyatanaṃ": "स्पर्श का इंद्रिय-क्षेत्र",
    "cakkhudhātu": "आँख का तत्व",
    "sotadhātu": "कान का तत्व",
    "ghānadhātu": "नाक का तत्व",
    "jivhādhātu": "जीभ का तत्व",
    "kāyadhātu": "शरीर का तत्व",
    "rūpadhātu": "दृश्य रूप का तत्व",
    "saddadhātu": "ध्वनि का तत्व",
    "gandhadhātu": "गंध का तत्व",
    "rasadhātu": "स्वाद का तत्व",
    "phoṭṭhabbadhātu": "स्पर्श का तत्व",
    "cakkhundriyaṃ": "आँख की क्षमता",
    "sotindriyaṃ": "कान की क्षमता",
    "ghānindriyaṃ": "नाक की क्षमता",
    "jivhindriyaṃ": "जीभ की क्षमता",
    "kāyindriyaṃ": "शरीर की क्षमता",
    "itthindriyaṃ": "स्त्रीत्व की क्षमता",
    "purisindriyaṃ": "पुरुषत्व की क्षमता",
    "jīvitindriyaṃ": C.NAMES["jīvitindriyaṃ"],  # जीवन-क्षमता
    "kāyaviññatti": "शरीर द्वारा प्रकट अभिव्यक्ति",  # as 3-01 (pi-5 viññatti)
    "vacīviññatti": "वाणी द्वारा प्रकट अभिव्यक्ति",
    "ākāsadhātu": "आकाश तत्व",
    "pathavīdhātu": "पृथ्वी तत्व",
    "āpodhātu": "जल तत्व",
    "tejodhātu": "अग्नि तत्व",
    "vāyodhātu": "वायु तत्व",
    "rūpassa lahutā": "भौतिक रूप का हल्कापन",
    "rūpassa mudutā": "भौतिक रूप की मृदुता",
    "rūpassa kammaññatā": "भौतिक रूप की कार्य-योग्यता",
    "rūpassa upacayo": "भौतिक रूप की वृद्धि",
    "rūpassa santati": "भौतिक रूप की धारा",
    "rūpassa jaratā": "भौतिक रूप का बुढ़ापा",  # as 3-01 (pi-5 jarā)
    "rūpassa aniccatā": "भौतिक रूप की अनित्यता",
    "kabaḷīkāro āhāro": "कौर-कौर खाया जाने वाला भोजन",
}


# =====================================================================================
# 2. Classification terms. Each is (core, kind, neg): the predicate is core [+ " नहीं"] + " है".
#    kind "adj" = adjective (may share one «है» with another adjective), "noun" = noun phrase.
#    Matrix-based adjectives come verbatim from the chapter-1 matrix (masc. sg.).
# =====================================================================================
def masc(bare):
    """matrix item (fem. pl., 'परिघटनाएँ') -> masc. sg. attribute of भौतिक रूप"""
    assert bare.endswith(" परिघटनाएँ"), bare
    s = bare[: -len(" परिघटनाएँ")]
    return re.sub(r"वाली(?=\s|$)", "वाला", s)


def MX(bid, letter):
    return masc(M.BARE[(bid, letter)])


MATRIX_TERMS = {
    "upādā": MX("1-M2-67", "क"),
    "no upādā": MX("1-M2-67", "ख"),
    "upādiṇṇaṃ": MX("1-M2-68", "क"),
    "anupādiṇṇaṃ": MX("1-M2-68", "ख"),
    "upādiṇṇupādāniyaṃ": MX("1-M1-4", "क"),
    "anupādiṇṇupādāniyaṃ": MX("1-M1-4", "ख"),
    "sanidassanaṃ": MX("1-M2-9", "क"),
    "anidassanaṃ": MX("1-M2-9", "ख"),
    "sappaṭighaṃ": MX("1-M2-10", "क"),
    "appaṭighaṃ": MX("1-M2-10", "ख"),
    "cittasamuṭṭhānaṃ": MX("1-M2-60", "क"),
    "na cittasamuṭṭhānaṃ": MX("1-M2-60", "ख"),
    "cittasahabhu": MX("1-M2-61", "क"),
    "na cittasahabhu": MX("1-M2-61", "ख"),
    "cittānuparivatti": MX("1-M2-62", "क"),
    "na cittānuparivatti": MX("1-M2-62", "ख"),
    "ajjhattikaṃ": MX("1-M2-66", "क"),
    "bāhiraṃ": MX("1-M2-66", "ख"),
}
EXPECTED = {
    "upādā": "व्युत्पन्न", "no upādā": "व्युत्पन्न न होने वाला",
    "upādiṇṇaṃ": "कर्म से उत्पन्न", "anupādiṇṇaṃ": "कर्म से उत्पन्न न होने वाला",
    "upādiṇṇupādāniyaṃ": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
    "anupādiṇṇupādāniyaṃ": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला",
    "sanidassanaṃ": "दिखाई देने वाला", "anidassanaṃ": "दिखाई न देने वाला",
    "sappaṭighaṃ": "टकराव वाला", "appaṭighaṃ": "टकराव से रहित",
    "cittasamuṭṭhānaṃ": "मन से उत्पन्न", "na cittasamuṭṭhānaṃ": "मन से उत्पन्न न होने वाला",
    "cittasahabhu": "मन के साथ-साथ होने वाला", "na cittasahabhu": "मन के साथ-साथ न होने वाला",
    "cittānuparivatti": "मन का अनुसरण करने वाला", "na cittānuparivatti": "मन का अनुसरण न करने वाला",
    "ajjhattikaṃ": "आंतरिक", "bāhiraṃ": "बाह्य",
}
assert MATRIX_TERMS == EXPECTED, {k: v for k, v in MATRIX_TERMS.items() if EXPECTED[k] != v}

TERMS = {k: (v, "adj", False) for k, v in MATRIX_TERMS.items()}
TERMS.update({
    "indriyaṃ": ("क्षमता", "noun", False),
    "na indriyaṃ": ("क्षमता", "noun", True),
    "mahābhūtaṃ": ("महाभूत", "noun", False),
    "na mahābhūtaṃ": ("महाभूत", "noun", True),
    "viññatti": ("प्रकट अभिव्यक्ति", "noun", False),
    "na viññatti": ("प्रकट अभिव्यक्ति", "noun", True),
    "oḷārikaṃ": ("स्थूल", "adj", False),
    "sukhumaṃ": ("सूक्ष्म", "adj", False),
    "dūre": ("दूर", "adj", False),
    "santike": ("निकट", "adj", False),
    "anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ":  # as 3-01 ^1-593
        (MATRIX_TERMS["anidassanaṃ"] + " और " + MATRIX_TERMS["appaṭighaṃ"]
         + " है तथा मन के विषयों के इंद्रिय-क्षेत्र में समाया हुआ", "adj", False),
})
for k, v in ITEMS.items():
    TERMS[k] = (v, "noun", False)
    if k.startswith("rūpassa "):
        TERMS["rūpassa na " + k[len("rūpassa "):]] = (v, "noun", True)
    else:
        TERMS["na " + k] = (v, "noun", True)

# genitive / dative members of the contact chains (oblique Hindi, before «का आधार» / «का विषय»)
GEN = {
    "cakkhusamphassassa": "आँख के संपर्क",
    "sotasamphassassa": "कान के संपर्क",
    "ghānasamphassassa": "नाक के संपर्क",
    "jivhāsamphassassa": "जीभ के संपर्क",
    "kāyasamphassassa": "शरीर के संपर्क",
    "cakkhusamphassajāya vedanāya": "आँख के संपर्क से उत्पन्न अनुभूति",
    "kāyasamphassajāya vedanāya": "शरीर के संपर्क से उत्पन्न अनुभूति",
    "saññāya": "पहचान",
    "cetanāya": "इरादे",
    "cakkhuviññāṇassa": "आँख की चेतना",
    "kāyaviññāṇassa": "शरीर की चेतना",
}
REL = {"vatthu": "का आधार", "ārammaṇaṃ": "का विषय"}
COMPOSITE = {}
for g in GEN:
    for r in REL:
        for neg in (False, True):
            key = f"{g} {'na ' if neg else ''}{r}"
            COMPOSITE[key] = (g, neg, r)
            TERMS[key] = (f"{GEN[g]} {REL[r]}", "noun", neg)

VOCAB = set(TERMS) | set(GEN)
MAXW = max(len(k.split()) for k in VOCAB)


def tokenize(text, vocab):
    words, out, i = text.split(), [], 0
    while i < len(words):
        for n in range(min(MAXW, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            if cand in vocab:
                out.append(cand)
                i += n
                break
        else:
            raise ValueError(f"unknown term at {words[i:]!r} in {text!r}")
    return out


def core(key):
    c, kind, neg = TERMS[key]
    return c + (" नहीं" if neg else "")


def simple_adj(key):
    c, kind, neg = TERMS[key]
    return kind == "adj" and not neg and " और " not in c


PE = "…pe…"
ELL = "…"


def predicate(q):
    """Pāli classification term(s) of a question/answer -> Hindi predicate ending in «है»."""
    q = re.sub(r"\s*…pe…\s*", PE, q.strip())
    pieces = q.split(PE)
    first = tokenize(pieces[0], VOCAB)
    others = [tokenize(p, VOCAB) for p in pieces[1:]]
    if any(len(o) != 1 for o in others):
        raise ValueError(q)
    chain = [first[-1]] + [o[0] for o in others]
    prefix = first[:-1]
    if len(chain) == 1:
        body, sadj = core(chain[0]), simple_adj(chain[0])
    elif all(c in TERMS and c not in COMPOSITE for c in chain):
        assert all(TERMS[c][1] == "noun" for c in chain), chain
        body, sadj = (ELL + " ").join(core(c) for c in chain), False
    else:
        assert all(c in GEN for c in chain[:-1]) and chain[-1] in COMPOSITE, chain
        g, neg, r = COMPOSITE[chain[-1]]
        # every member carries «का», as in 3-01: «… अनुभूति का… पहचान का… इरादे का… आँख की चेतना का आधार»
        body = "".join(GEN[c] + " का" + ELL + " " for c in chain[:-1]) + GEN[g] + " " + REL[r] \
            + (" नहीं" if neg else "")
        sadj = False
    assert len(prefix) <= 1, q
    for p in prefix:
        pc = core(p)
        if " और " in pc or " और " in body:
            body = f"{pc} है तथा {body}"
        elif simple_adj(p) and sadj:
            body = f"{pc} और {body}"
        else:
            body = f"{pc} है और {body}"
    return body + " है"


# =====================================================================================
# 3. Answer lists of items
# =====================================================================================
CLAUSE = "yaṃ vā panaññampi atthi rūpaṃ"
QUALS = {
    "kammassa katattā": "किए गए कर्म के कारण है",
    "na kammassa katattā": "किए गए कर्म के कारण नहीं है",
    "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": "मन से जन्मा, मन के कारण होने वाला, मन से उत्पन्न है",
    "na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ":
        "न मन से जन्मा, न मन के कारण होने वाला, न मन से उत्पन्न है",
}
LEAD = {"kammassa katattā": "किए गए कर्म के कारण:", "na kammassa katattā": "किए गए कर्म के कारण नहीं:"}
WHATEVER = f"या जो भी दूसरा {RUPA} है जो "
LVOCAB = set(ITEMS) | {CLAUSE} | set(QUALS)


def list_hi(a):
    a = a[0].lower() + a[1:]
    a = re.sub(r"\s*…pe…\s*", " " + PE + " ", a).replace(",", " , ")
    words = a.split()
    toks, i = [], 0
    while i < len(words):
        w = words[i]
        if w in (",", PE):
            toks.append(w); i += 1; continue
        for n in range(min(6, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            if cand in LVOCAB:
                toks.append(cand); i += n; break
        else:
            raise ValueError(f"unknown list item at {words[i:]!r} in {a!r}")
    out, prev = "", None  # prev: 'item' | 'pe' | 'colon' | None
    j = 0
    while j < len(toks):
        t = toks[j]
        if t == ",":
            j += 1; continue
        if t == PE:
            out += ELL; prev = "pe"; j += 1; continue
        if t == CLAUSE:
            q = toks[j + 1]
            assert q in QUALS, toks
            out += ", " + WHATEVER + QUALS[q] + ":"
            prev = "colon"; j += 2; continue
        if t in LEAD and prev is None:
            out += LEAD[t]; prev = "colon"; j += 1; continue
        assert t in ITEMS, t
        if prev == "item":
            out += ", "
        elif prev in ("pe", "colon"):
            out += " "
        out += ITEMS[t]; prev = "item"; j += 1
    return out


# =====================================================================================
# 4. Definitions
# =====================================================================================
M_, F_ = "m", "f"
WALA = {(M_, False): "वाला", (M_, True): "वाले", (F_, False): "वाली", (F_, True): "वाली"}


def IA(g, obl=False):
    """anidassana sappaṭigha: invisible and making impact"""
    w = WALA[(g, obl)]
    return f"दिखाई न देने {w} और टकराव {w}"


def VA(g, obl=False):
    """sanidassana sappaṭigha: visible and making impact"""
    w = WALA[(g, obl)]
    return f"दिखाई देने {w} और टकराव {w}"


def STRIKE(g):
    if g == M_:
        return "टकरा चुका है, टकराता है, टकराएगा या टकरा सकता है"
    return "टकरा चुकी है, टकराती है, टकराएगी या टकरा सकती है"


ARISE_M = "उत्पन्न हो चुका है, उत्पन्न होता है, उत्पन्न होगा या उत्पन्न हो सकता है"
ARISE_F = "उत्पन्न हो चुकी है, उत्पन्न होती है, उत्पन्न होगी या उत्पन्न हो सकती है"
FOUR = "चार महाभूतों से व्युत्पन्न"  # catunnaṃ mahābhūtānaṃ upādāya
SENS = f"{FOUR} संवेदनशीलता है, व्यक्तिगत अस्तित्व में समाई हुई, {IA(F_)}"
NAMES_COMMON = "यह लोक है, यह द्वार है, यह समुद्र है, यह उज्ज्वलता है, यह खेत है, यह आधार है"
NAMES_EYE_EXTRA = "यह नेत्र है, यह नयन है"
NAMES_TAIL = "यह इस पार का किनारा है, यह सूना गाँव है"
REST = "अनुभूति… पहचान… इरादा…"  # vedanā…pe… saññā…pe… cetanā…pe…


def verbs(stem, fut):
    return f"{stem} चुका है, {stem}ता है, {fut} या {stem} सकता है"


ORGANS = {
    # key: (organ, organ gender, verb forms, object, object gender, object quality fn, extra names)
    "cakkhu": ("आँख", F_, verbs("देख", "देखेगा"), "दृश्य रूप", M_, VA, True),
    "sotaṃ": ("कान", M_, verbs("सुन", "सुनेगा"), "ध्वनि", F_, IA, False),
    "ghānaṃ": ("नाक", F_, verbs("सूँघ", "सूँघेगा"), "गंध", F_, IA, False),
    "jivhā": ("जीभ", F_, verbs("चख", "चखेगा"), "स्वाद", M_, IA, False),
    "kāyo": ("शरीर", M_, verbs("छू", "छुएगा"), "स्पर्श", M_, IA, False),
}
assert ORGANS["kāyo"][2] == "छू चुका है, छूता है, छुएगा या छू सकता है"


def organ_names(o, extra):
    s = (f"यह {o} है, यह {o} का इंद्रिय-क्षेत्र है, यह {o} का तत्व है, यह {o} की क्षमता है, "
         + NAMES_COMMON + ", ")
    if extra:
        s += NAMES_EYE_EXTRA + ", "
    return s + NAMES_TAIL


def contact_chain(o, n, lead_a, lead_b):
    """variant d: lead_a(…) precedes the contact, lead_b(…) precedes feeling…consciousness"""
    return (f"{lead_a[0]} {o} का संपर्क {ARISE_M}{ELL} "
            f"{lead_a[1]} {o} के संपर्क से उत्पन्न {REST} {o} की चेतना {ARISE_F}{ELL} "
            f"{lead_b[0]} {o} का संपर्क {ARISE_M}{ELL} "
            f"{lead_b[1]} {o} के संपर्क से उत्पन्न {REST} {o} की चेतना {ARISE_F}")


def organ_def(key, variant, vbracket=""):
    o, og, v, obj, objg, objq, extra = ORGANS[key]
    head = f"जो {o}{vbracket} {SENS}"
    if variant == "abbr":
        return f"जो {o} {FOUR} संवेदनशीलता है{ELL} {NAMES_TAIL.split(', ')[-1]}"
    if variant == "a":
        mid = f"{IA(og, True)} जिस {o} से कोई {objq(objg, True)} {obj} को {v}"
    elif variant == "b":
        mid = f"{IA(og, True)} जिस {o} पर {objq(objg)} {obj} {STRIKE(objg)}"
    elif variant == "c":
        mid = f"{IA(og)} जो {o} {objq(objg, True)} {obj} से {STRIKE(og)}"
    elif variant == "d":
        a = f"जिस {o} के सहारे {obj} को विषय बनाकर"
        b = f"जिस {o} के सहारे {obj} के विषय"
        mid = contact_chain(o, obj, (a, a), (b + " वाला", b + " वाली"))
    return f"{head}; {mid}; {organ_names(o, extra)}"


COLOURS = ("नीला, पीला, लाल, सफ़ेद, काला, मजीठ जैसा गहरा लाल{v1}, हरा, हरे रंग का, आम की कोंपलों के रंग का, "
           "लंबा, छोटा, बारीक, मोटा, गोल, वृत्ताकार, चौकोर{v2}, छह कोनों वाला, आठ कोनों वाला, सोलह कोनों वाला, "
           "नीचा, ऊँचा, छाया, धूप, प्रकाश, अंधकार, बादल, कोहरा, धुआँ, धूल, "
           "चंद्रमा के मंडल की रंग-आभा, सूर्य के मंडल की रंग-आभा{v3}, तारों की रंग-आभा, "
           "दर्पण के मंडल की रंग-आभा, मणि, शंख, मोती और वैदूर्य की रंग-आभा, सोने और चाँदी की रंग-आभा")
SOUNDS = ("नगाड़े की ध्वनि, मृदंग की ध्वनि, शंख की ध्वनि, ढोलक की ध्वनि, गाने की ध्वनि, बाजे की ध्वनि, "
          "मंजीरे की ध्वनि, ताली की ध्वनि, प्राणियों का शोर, वस्तुओं के आपस में टकराने की ध्वनि, हवा की ध्वनि, "
          "पानी की ध्वनि, मनुष्यों की ध्वनि, अमानवीय प्राणियों की ध्वनि")
SMELLS = ("जड़ों की गंध, लकड़ी के सार की गंध, छाल की गंध, पत्तों की गंध, फूलों की गंध, फलों की गंध, "
          "कच्चे मांस की गंध, सड़न की गंध, सुगंध, दुर्गंध")
TASTES = ("जड़ों का स्वाद, तनों का स्वाद, छाल का स्वाद, पत्तों का स्वाद, फूलों का स्वाद, फलों का स्वाद, "
          "खट्टा, मीठा, कड़वा, तीखा, नमकीन, खारा, हल्का खट्टा{v1}, कसैला, स्वादिष्ट, बेस्वाद")
SUKHA_PH, DUKKHA_PH = "सुखद संपर्क वाला", "दुःखद संपर्क वाला"  # sukha-/dukkhasamphassa, as 3-01 ^1-591
TOUCH_HEAD = (f"पृथ्वी तत्व, अग्नि तत्व, वायु तत्व, कठोर, मुलायम, चिकना, खुरदरा, {SUKHA_PH}, {DUKKHA_PH}, "
              "भारी, हल्का")
assert TOUCH_HEAD.startswith(ITEMS["pathavīdhātu"])

OBJECTS = {
    # key: (object noun, gender, quality fn, list, organ key)
    "rūpa": ("दृश्य रूप", M_, VA, None, "cakkhu"),
    "sadda": ("ध्वनि", F_, IA, SOUNDS, "sotaṃ"),
    "gandha": ("गंध", F_, IA, SMELLS, "ghānaṃ"),
    "rasa": ("स्वाद", M_, IA, TASTES, "jivhā"),
    "phoṭṭhabba": ("स्पर्श", M_, IA, None, "kāyo"),
}
OTHER = {M_: "दूसरा", F_: "दूसरी"}


def object_head(key, bracket_variants):
    n, g, q, lst, _ = OBJECTS[key]
    if key == "rūpa":
        if bracket_variants:
            col = COLOURS.format(v1=V("s", "Sī., Syā.", "mañjeṭṭhakaṃ"), v2=V("s", "Sī., Ka.", "caturassaṃ"),
                                 v3=V("s", "Sī., Syā.", "suriyamaṇḍalassa"))
        else:
            col = COLOURS.format(v1="", v2="", v3="")
        d = f"{FOUR} रंग-आभा है, {q(g)}"
        return f"जो {n} {d}: {col}, या जो भी {OTHER[g]} {n} है जो {d}"
    if key == "phoṭṭhabba":
        return TOUCH_HEAD
    if key == "rasa":
        lst = lst.format(v1=V("p", "Sī.", "lapilakaṃ") if bracket_variants else "")
    d = f"{FOUR} है, {q(g)}"
    return f"जो {n} {d}: {lst}, या जो भी {OTHER[g]} {n} है जो {d}"


def object_def(key, variant, bracket_variants=False):
    n, g, q, lst, okey = OBJECTS[key]
    o, og, v = ORGANS[okey][:3]
    names = f"यह {n} है, यह {n} का इंद्रिय-क्षेत्र है, यह {n} का तत्व है"
    if variant == "abbr":
        if key == "rūpa":
            return f"जो {n} {FOUR} रंग-आभा है{ELL} यह {n} का तत्व है"
        if key == "phoṭṭhabba":
            return f"{ITEMS['pathavīdhātu']}{ELL} यह {n} का तत्व है"
        raise ValueError(key)
    head = object_head(key, bracket_variants)
    if variant == "a":
        mid = f"{q(g, True)} जिस {n} को कोई {IA(og, True)} {o} से {v}"
    elif variant == "b":
        mid = f"{q(g, True)} जिस {n} पर {IA(og)} {o} {STRIKE(og)}"
    elif variant == "c":
        mid = f"{q(g)} जो {n} {IA(og, True)} {o} से {STRIKE(g)}"
    elif variant == "d":
        a = f"जिस {n} को विषय बनाकर {o} के सहारे"
        b = f"{o} के सहारे जिस {n} के विषय"
        mid = contact_chain(o, n, (a, a), (b + " वाला", b + " वाली"))
    return f"{head}; {mid}; {names}"


IN_RUPA = f"{RUPA} में जो "
OWN_OTHERS = (", चाहे " + M.BARE[("1-M1-20", "क")].replace(" परिघटनाएँ", "") + " हो या "
              + M.BARE[("1-M1-20", "ख")].replace(" परिघटनाएँ", "") + ", "
              + MATRIX_TERMS["upādiṇṇaṃ"] + " हो या " + MATRIX_TERMS["upādiṇṇaṃ"] + " न हो")
assert OWN_OTHERS == ", चाहे स्वयं से संबंधित हो या दूसरों से संबंधित, कर्म से उत्पन्न हो या कर्म से उत्पन्न न हो"
MINDS = "हितकर मन, हानिकर मन या नैतिक रूप से अनिर्धारित मन से"
INTIM = "प्रकट अभिव्यक्ति, प्रकट करना, प्रकट कर चुका होना"  # viññatti viññāpanā viññāpitattaṃ
SPEECH = "वाणी, बोल, बोलने का ढंग, उच्चारण, आवाज़, आवाज़ निकालना, वाणी, वाणी का फूटना"
WATER = "जल, जल की प्रकृति वाला, नमी, नमी की प्रकृति वाला, भौतिक रूप को बाँधे रखना"
ITTHI = "स्त्री में जो स्त्री की आकृति, स्त्री का चिह्न, स्त्री का आचरण, स्त्री का ढंग, स्त्रीत्व, स्त्री होने का भाव"
PURISA = "पुरुष में जो पुरुष की आकृति, पुरुष का चिह्न, पुरुष का आचरण, पुरुष का ढंग, पुरुषत्व, पुरुष होने का भाव"

SHORT_DEFS = {
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo": ITTHI + " है",
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo [itthittaṃ itthībhāvo (syā.)]":
        ITTHI + V("s", "Syā.", "itthittaṃ itthībhāvo") + " है",
    "Yaṃ purisassa purisaliṅgaṃ purisanimittaṃ purisakuttaṃ purisākappo purisattaṃ purisabhāvo": PURISA + " है",
    "Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        "उन " + masc(M.BARE[("1-M2-11", "क")]).replace("भौतिक", "भौतिक परिघटनाओं की")
        + " जो " + C.S_JIVITA + " है",
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā abhikkamantassa vā paṭikkamantassa vā "
    "ālokentassa vā vilokentassa vā samiñjentassa vā pasārentassa vā kāyassa thambhanā santhambhanā "
    "santhambhitattaṃ viññatti viññāpanā viññāpitattaṃ":
        f"{MINDS}, आगे बढ़ते, पीछे हटते, सामने देखते, इधर-उधर देखते, अंग सिकोड़ते या अंग फैलाते व्यक्ति के "
        f"शरीर का जो तनना, भली-भाँति तनना, भली-भाँति तना हुआ होना, {INTIM} है",
    "Yo ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi":
        "जो आकाश, आकाश की प्रकृति वाला, रिक्त स्थान, रिक्त स्थान की प्रकृति वाला, छेद, छेद की प्रकृति वाला, "
        "चार महाभूतों से अछूता है",
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa": f"जो {WATER} है",
    "Yā rūpassa lahutā lahupariṇāmatā adandhanatā avitthanatā": IN_RUPA + C.S_LAHUTA + " है",
    "Yā rūpassa mudutā maddavatā akakkhaḷatā akathinatā": IN_RUPA + C.S_MUDUTA + " है",
    "Yā rūpassa kammaññatā kammaññattaṃ kammaññabhāvo": IN_RUPA + C.S_KAMMANNATA + " है",
    "Yo āyatanānaṃ ācayo, so rūpassa upacayo":
        "इंद्रिय-क्षेत्रों का जो संचय है, वह " + ITEMS["rūpassa upacayo"] + " है",
    "Yo rūpassa upacayo, sā rūpassa santati":
        f"{RUPA} की जो वृद्धि है, वह " + ITEMS["rūpassa santati"] + " है",
    "Yā rūpassa jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko":
        IN_RUPA + "बुढ़ापा, जीर्ण होना, दाँतों का टूटना, बालों का पकना, त्वचा पर झुर्रियाँ पड़ना, आयु का घटना, "
        "इंद्रियों का पूरी तरह पक जाना है",
    "Yo rūpassa khayo vayo bhedo paribhedo aniccatā antaradhānaṃ":
        IN_RUPA + "क्षय, नाश, टूटना, बिखर जाना, अनित्यता, लुप्त हो जाना है",
    "Yaṃ kakkhaḷaṃ kharagataṃ [kharigataṃ (ka.)] kakkhaḷattaṃ kakkhaḷabhāvo ajjhattaṃ vā bahiddhā vā "
    "upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "जो कठोर, कर्कशता की प्रकृति वाला" + V("s", "Ka.", "kharigataṃ") + ", कठोरता, कठोर होने का भाव है"
        + OWN_OTHERS,
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā "
    "anupādiṇṇaṃ vā":
        f"जो {WATER} है" + OWN_OTHERS,
    "Yaṃ tejo tejogataṃ usmā usmāgataṃ usumaṃ usumagataṃ ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "जो अग्नि, अग्नि की प्रकृति वाला, ऊष्मा, ऊष्मा की प्रकृति वाला, गरमी, गरमी की प्रकृति वाला है"
        + OWN_OTHERS,
    "Yaṃ vāyo vāyogataṃ thambhitattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "जो वायु, वायु की प्रकृति वाला, भौतिक रूप का तना हुआ होना है" + OWN_OTHERS,
}
assert SHORT_DEFS["Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ "
                  "jīvitindriyaṃ"].startswith("उन भौतिक परिघटनाओं की जो आयु, ")
_VACI_HEAD = f"{MINDS} जो {SPEECH} है"
_VACI_TAIL = f"इसे वाणी कहा जाता है{DANDA} उस वाणी के द्वारा जो {INTIM} है"
_VACI_P = ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ {g} "
           "ghosakammaṃ vācā vacībhedo{sep} ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ")
SHORT_DEFS[_VACI_P.format(g="ghoso", sep=" –")] = f"{_VACI_HEAD} {DASH} {_VACI_TAIL}"
SHORT_DEFS[_VACI_P.format(g="ghoso", sep=",")] = f"{_VACI_HEAD}, {_VACI_TAIL}"
SHORT_DEFS[_VACI_P.format(g="dhoso", sep=",")] = f"{_VACI_HEAD}, {_VACI_TAIL}"  # ^1-850: 'dhoso' (source slip)
_KABALI = ("भात, दलिया, सत्तू, मछली, मांस, दूध, दही, घी, मक्खन, तेल, शहद, गुड़, "
           f"या जो भी दूसरा {RUPA} है जिसे जिस-जिस प्रदेश में वहाँ के प्राणी मुँह से खाते हैं, दाँतों से चबाते हैं, "
           "गले से नीचे उतारते हैं और जो पेट भरता है, वह पोषक सार जिससे प्राणी जीवित रहते हैं")
_KAB_P = ("Odano kummāso sattu maccho maṃsaṃ khīraṃ dadhi sappi navanītaṃ telaṃ madhu phāṇitaṃ, yaṃ vā "
          "panaññampi atthi rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ "
          "galajjhoharaṇīyaṃ kucchivitthambhanaṃ{sep} yāya ojāya sattā yāpenti")
SHORT_DEFS[_KAB_P.format(sep=",")] = _KABALI
SHORT_DEFS[_KAB_P.format(sep="")] = _KABALI

ORG_RE = re.compile(r"^(Yaṃ cakkhu|Yaṃ sotaṃ|Yaṃ ghānaṃ|Yā jivhā|Yo kāyo)( \[cakkhuṃ \(sī\. syā\.\)\])? "
                    r"catunnaṃ mahābhūtānaṃ upādāya pasādo")
OBJ_RE = re.compile(r"^(Yaṃ rūpaṃ|Yo saddo|Yo gandho|Yo raso) catunnaṃ mahābhūtānaṃ upādāya")
OBJ_KEY = {"Yaṃ rūpaṃ": "rūpa", "Yo saddo": "sadda", "Yo gandho": "gandha", "Yo raso": "rasa"}


def def_hi(a):
    """Return the Hindi of a definition answer, or None if `a` is an item list."""
    if a in SHORT_DEFS:
        return SHORT_DEFS[a]
    m = ORG_RE.match(a)
    if m:
        key = m.group(1).split()[1]
        vb = V("s", "Sī., Syā.", "cakkhuṃ") if m.group(2) else ""
        if "pasādo…pe…" in a:
            assert a.endswith("suñño gāmo peso"), a
            return organ_def(key, "abbr")
        rest = a.split("sappaṭigho, ", 1)[1]
        if " nissāya " in rest:
            var = "d"
        elif re.search(r"\b(passi|suṇi|ghāyi|sāyi|phusi) vā", rest):
            var = "a"
        elif rest.startswith(("yamhi", "yāya")):
            var = "b"
        elif re.match(r"(yaṃ cakkhu|yaṃ sotaṃ|yaṃ ghānaṃ|yā jivhā|yo kāyo) anidassan", rest):
            var = "c"
        else:
            raise ValueError(a)
        assert re.search(r"suñño gāmo ?peso$", a), a
        return organ_def(key, var, vb)
    m = OBJ_RE.match(a)
    if m or a.startswith("Pathavīdhātu"):
        key = OBJ_KEY[m.group(1)] if m else "phoṭṭhabba"
        if "…pe…" in a.split(",")[0] and "ārabbha" not in a:
            return object_def(key, "abbr")
        tail = a.rsplit("sappaṭighaṃ, " if key == "rūpa" else
                        ("lahukaṃ, " if key == "phoṭṭhabba" else "sappaṭigho, "), 1)[1]
        if "ārabbha" in tail:
            var = "d"
        elif re.search(r"\b(passi|suṇi|ghāyi|sāyi|phusi) vā", tail):
            var = "a"
        elif tail.startswith("yamhi"):
            var = "b"
        elif "paṭihaññi" in tail:
            var = "c"
        else:
            raise ValueError(a)
        return object_def(key, var, "[" in a)
    return None


# =====================================================================================
# 5. Fixed lines and headings
# =====================================================================================
NUM = {"du": "दो", "ti": "तीन", "catub": "चार", "pañca": "पाँच", "cha": "छह", "satta": "सात",
       "aṭṭha": "आठ", "nava": "नौ", "dasa": "दस", "ekādasa": "ग्यारह"}
SETS = {"Catukkaṃ": "catub", "Pañcakaṃ": "pañca", "Chakkaṃ": "cha", "Sattakaṃ": "satta", "Aṭṭhakaṃ": "aṭṭha",
        "Navakaṃ": "nava", "Dasakaṃ": "dasa", "Ekādasakaṃ": "ekādasa"}
H_DUKA_NIDDESA = "दो-दो के वर्गीकरणों की व्याख्या"
H_TIKA_NIDDESA = "तीन-तीन के वर्गीकरणों की व्याख्या"
H_UPADA = "व्युत्पन्न भौतिक रूप का विश्लेषण"
HEADINGS = {
    "##### Dukaniddeso": "##### " + H_DUKA_NIDDESA,
    "###### Upādābhājanīyaṃ": "###### " + H_UPADA,
    "##### Tikaniddeso": "##### " + H_TIKA_NIDDESA,
}
LINES = {
    "Upādābhājanīyaṃ.": H_UPADA + DANDA,
    "Rūpakaṇḍe paṭhamabhāṇavāro.": "भौतिक रूप के अध्याय का पहला पाठ-खंड।",
    "Dukaniddeso.": H_DUKA_NIDDESA + DANDA,
    "Tikaniddeso.": H_TIKA_NIDDESA + DANDA,
    "Aṭṭhamabhāṇavāro.": "आठवाँ पाठ-खंड।",
    "Rūpavibhatti.": "भौतिक रूप का वर्गीकरण।",
    "Rūpakaṇḍaṃ niṭṭhitaṃ.": "भौतिक रूप का अध्याय पूरा हुआ।",
}
for pali, k in SETS.items():
    n = NUM[k]
    HEADINGS["##### " + pali] = f"##### {n}-{n} के वर्गीकरण"
    LINES[pali + "."] = f"{n}-{n} के वर्गीकरण{DANDA}"
for k, n in NUM.items():
    pk = {"catub": "catubb", "cha": "chabb"}.get(k, k + "v")
    LINES[f"Evaṃ {pk}idhena rūpasaṅgaho."] = f"इस तरह {n} प्रकार से {RUPA} का वर्गीकरण हुआ{DANDA}"  # as 3-01
assert "Evaṃ catubbidhena rūpasaṅgaho." in LINES and "Evaṃ chabbidhena rūpasaṅgaho." in LINES
assert "Evaṃ duvidhena rūpasaṅgaho." in LINES and "Evaṃ ekādasavidhena rūpasaṅgaho." in LINES

KN = "से जाना जा सकने वाला भौतिक रूप है"  # -viññeyyaṃ rūpaṃ (cf. ^1-M2-13 «जानी जा सकने वाली»)
I = ITEMS
_FIVE = (f"{I['rūpāyatanaṃ']} आँख {KN}, {I['saddāyatanaṃ']} कान {KN}, {I['gandhāyatanaṃ']} नाक {KN}, "
         f"{I['rasāyatanaṃ']} जीभ {KN}")
_BODY = f"{I['phoṭṭhabbāyatanaṃ']} शरीर {KN}"
_FIVE_OBJ = (f"{I['rūpāyatanaṃ']}, {I['saddāyatanaṃ']}, {I['gandhāyatanaṃ']}, {I['rasāyatanaṃ']} और "
             f"{I['phoṭṭhabbāyatanaṃ']}")
_MANODHATU = f"{_FIVE_OBJ} मन के तत्व से जाना जा सकने वाला भौतिक रूप हैं"
_LAST = f"और सारा {RUPA} मन की चेतना के तत्व {KN}{DANDA}"
_AGREE = (f"मनभावन, {SUKHA_PH} स्पर्श शरीर {KN}, मन को न भाने वाला, {DUKKHA_PH} स्पर्श शरीर {KN}")
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ "
       "manoviññeyyaṃ rūpaṃ.")] = f"{_FIVE}, {_BODY}, और सारा {RUPA} मन {KN}{DANDA}"
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, rūpāyatanaṃ "
       "saddāyatanaṃ gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ manodhātuviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ "
       "manoviññāṇadhātuviññeyyaṃ rūpaṃ.")] = f"{_FIVE}, {_BODY}, {_MANODHATU}, {_LAST}"
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, manāpiyo phoṭṭhabbo sukhasamphasso kāyaviññeyyaṃ rūpaṃ, "
       "amanāpiyo phoṭṭhabbo dukkhasamphasso kāyaviññeyyaṃ rūpaṃ, rūpāyatanaṃ saddāyatanaṃ gandhāyatanaṃ "
       "rasāyatanaṃ phoṭṭhabbāyatanaṃ manodhātuviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ.")] = \
    f"{_FIVE}, {_AGREE}, {_MANODHATU}, {_LAST}"
LINES["Rūpāyatanaṃ diṭṭhaṃ, saddāyatanaṃ sutaṃ, gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ mutaṃ, "
      "sabbaṃ rūpaṃ manasā viññātaṃ rūpaṃ."] = \
    (f"{I['rūpāyatanaṃ']} देखा हुआ है, {I['saddāyatanaṃ']} सुना हुआ है, {I['gandhāyatanaṃ']}, "
     f"{I['rasāyatanaṃ']} और {I['phoṭṭhabbāyatanaṃ']} अनुभव किया हुआ है, और सारा {RUPA} मन से जाना हुआ "
     f"{RUPA} है{DANDA}")

PUNCT = {"?": "?", ".": DANDA, "": ""}


def FRAME_Q(pred, p):
    return f"वह {RUPA} कौन-सा है जो {pred}{PUNCT[p]}"


def FRAME_A(ans, pred, p):
    return f"{ans} {DASH} यह वह {RUPA} है जो {pred}{PUNCT[p]}"


LINES["Idaṃ taṃ rūpaṃ upādā."] = f"यह वह {RUPA} है जो {predicate('upādā')}{DANDA}"
LINES["Idaṃ taṃ rūpaṃ no upādā."] = f"यह वह {RUPA} है जो {predicate('no upādā')}{DANDA}"

QA_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)([?.]) (.+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")
NOQ_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (\S+ \S+) (itthindriyaṃ…pe… kabaḷīkāro āhāro|"
                    r"cakkhāyatanaṃ…pe… kāyāyatanaṃ, .+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")


def qa_hi(line):
    m = QA_RE.match(line)
    if m:
        q, qp, a, q2, ap = m.groups()
        qtext = FRAME_Q(predicate(q), qp)
    elif " – " not in line:  # ^1-595, ^1-646: bare list answer, no closing formula
        m = re.match(r"^Katamaṃ taṃ rūpaṃ (.+?)\? (.+)\.$", line)
        return FRAME_Q(predicate(m.group(1)), "?") + " " + list_hi(m.group(2)) + DANDA
    else:  # ^1-895, ^1-939: no question mark after the question (source as written)
        m = NOQ_RE.match(line)
        if not m:
            raise ValueError(line)
        q, a, q2, ap = m.groups()
        qtext = FRAME_Q(predicate(q), "")
        a = a[0].upper() + a[1:]
    ah = def_hi(a)
    if ah is None:
        ah = list_hi(a)
    assert predicate(q) == predicate(q2) or PE in q, (q, q2)
    return qtext + " " + FRAME_A(ah, predicate(q2), ap)


def line_hi(line):
    if line.startswith("#"):
        return HEADINGS[line]
    if line.startswith("Katamaṃ taṃ rūpaṃ"):
        return qa_hi(line)
    return LINES[line]


ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
LATIN_OUTSIDE = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]")
BRACKET = re.compile(r"\[[^\]]*\]")


def build(part):
    text = (SRC / part).read_text(encoding="utf-8")
    segs = [s for s in text.split("\n\n") if s.strip()]
    out = []
    for seg in segs:
        lines = [l for l in seg.split("\n") if l.strip()]
        m = ID.search(lines[-1])
        assert m, lines[-1]
        lines[-1] = lines[-1][:m.start()]
        hi = [line_hi(l.strip()) for l in lines]
        for p, h in zip(lines, hi):
            assert p.count("–") == h.count("–"), (m.group(1), p, h)
            assert p.count("[") == h.count("["), (m.group(1), p, h)
            assert not LATIN_OUTSIDE.search(BRACKET.sub("", h)), (m.group(1), h)
        hi[-1] += f" ^{m.group(1)}"
        out.append("\n".join(hi))
    t = "\n\n".join(out) + "\n"
    assert "—" not in t and ":-" not in t and "\r" not in t and "\n\n\n" not in t
    return t


if __name__ == "__main__":
    for part in PARTS:
        t = build(part)
        (OUT / part).write_text(t, encoding="utf-8", newline="\n")
        print("wrote", OUT / part, t.count("\n\n") + 1, "segments")
