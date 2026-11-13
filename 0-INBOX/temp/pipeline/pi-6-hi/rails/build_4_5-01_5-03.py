"""pi-6 Hindi plain RAILS: builder for 4-dhatuyamaka.md, 5-01-saccayamaka.md, 5-03-saccayamaka.md.

Imports build_rails_sample.py read-only (constants and formula strings) and adds the dhātu / sacca word tables,
the being / moment chains of the Saccayamaka and the pariññā frames. Every Pāli line must be matched by a
formula; an unknown line raises ValueError.

usage: python -I -X utf8 build_4_5-01_5-03.py            (write the three files)
       python -I -X utf8 build_4_5-01_5-03.py --dry      (translate, print failures, write nothing)
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = ["4-dhatuyamaka.md", "5-01-saccayamaka.md", "5-03-saccayamaka.md"]

# =====================================================================================================
# Word tables (Paṇṇattivāra): key (nominative) -> (direct, oblique, number)
# =====================================================================================================
WORDS = {
    # dhātu chapter: bare words
    "cakkhu": ("आँख", "आँख", "sg"), "sotaṃ": ("कान", "कान", "sg"), "ghānaṃ": ("नाक", "नाक", "sg"),
    "jivhā": ("जीभ", "जीभ", "sg"), "kāyo": ("शरीर", "शरीर", "sg"), "rūpaṃ": ("रूप", "रूप", "sg"),
    "saddo": ("ध्वनि", "ध्वनि", "sg"), "gandho": ("गंध", "गंध", "sg"), "raso": ("स्वाद", "स्वाद", "sg"),
    "phoṭṭhabbo": ("स्पर्श", "स्पर्श", "sg"), "mano": ("मन", "मन", "sg"),
    "cakkhuviññāṇaṃ": ("आँख की चेतना", "आँख की चेतना", "sg"),
    "sotaviññāṇaṃ": ("कान की चेतना", "कान की चेतना", "sg"),
    "ghānaviññāṇaṃ": ("नाक की चेतना", "नाक की चेतना", "sg"),
    "jivhāviññāṇaṃ": ("जीभ की चेतना", "जीभ की चेतना", "sg"),
    "kāyaviññāṇaṃ": ("शरीर की चेतना", "शरीर की चेतना", "sg"),
    "manoviññāṇaṃ": ("मन की चेतना", "मन की चेतना", "sg"),
    "dhammo": ("परिघटना", "परिघटना", "sg"),
    "dhātu": ("तत्व", "तत्व", "sg"), "dhātū": ("तत्व", "तत्वों", "pl"),
    # sacca chapter: bare words
    "dukkhaṃ": ("दुःख", "दुःख", "sg"), "samudayo": ("उत्पत्ति", "उत्पत्ति", "sg"),
    "nirodho": ("अंत", "अंत", "sg"), "maggo": ("मार्ग", "मार्ग", "sg"),
    "saccaṃ": ("सत्य", "सत्य", "sg"), "saccā": ("सत्य", "सत्यों", "pl"),
}
DHATU_NAMES = {  # element -> Hindi (direct)
    "cakkhudhātu": "आँख का तत्व", "sotadhātu": "कान का तत्व", "ghānadhātu": "नाक का तत्व",
    "jivhādhātu": "जीभ का तत्व", "kāyadhātu": "शरीर का तत्व", "rūpadhātu": "दृश्य रूप का तत्व",
    "saddadhātu": "ध्वनि का तत्व", "gandhadhātu": "गंध का तत्व", "rasadhātu": "स्वाद का तत्व",
    "phoṭṭhabbadhātu": "स्पर्श का तत्व", "cakkhuviññāṇadhātu": "आँख की चेतना का तत्व",
    "sotaviññāṇadhātu": "कान की चेतना का तत्व", "ghānaviññāṇadhātu": "नाक की चेतना का तत्व",
    "jivhāviññāṇadhātu": "जीभ की चेतना का तत्व", "kāyaviññāṇadhātu": "शरीर की चेतना का तत्व",
    "manodhātu": "मन का तत्व", "manoviññāṇadhātu": "मन की चेतना का तत्व",
    "dhammadhātu": "मन के विषयों का तत्व",
}
SACCA_NAMES = {
    "dukkhasaccaṃ": "दुःख का सत्य", "samudayasaccaṃ": "उत्पत्ति का सत्य",
    "nirodhasaccaṃ": "अंत का सत्य", "maggasaccaṃ": "मार्ग का सत्य",
}


def _obl(name):
    """«आँख का तत्व» -> «आँख के तत्व»; «मन के विषयों का तत्व» -> «मन के विषयों के तत्व»."""
    head, last = name.rsplit(" का ", 1)
    return f"{head} के {last}"


for _d in (DHATU_NAMES, SACCA_NAMES):
    for _k, _v in _d.items():
        WORDS[_k] = (_v, _obl(_v), "sg")

# accusative / enclitic forms -> key
ACC = {"cakkhuṃ": "cakkhu", "cakkhuñca": "cakkhu", "cakkhu": "cakkhu", "sotañca": "sotaṃ", "sotaṃ": "sotaṃ",
       "ghānaṃ": "ghānaṃ", "jivha": "jivhā", "jivhaṃ": "jivhā", "kāyañca": "kāyo", "rūpaṃ": "rūpaṃ",
       "rūpañca": "rūpaṃ", "saddaṃ": "saddo", "gandhaṃ": "gandho", "gandhañca": "gandho", "rasaṃ": "raso",
       "rasañca": "raso", "phoṭṭhabbaṃ": "phoṭṭhabbo", "manañca": "mano", "dhammañca": "dhammo",
       "dhātuñca": "dhātu", "dukkhaṃ": "dukkhaṃ", "dukkhañca": "dukkhaṃ", "samudayaṃ": "samudayo",
       "samudayañca": "samudayo", "nirodhaṃ": "nirodho", "nirodhañca": "nirodho", "maggaṃ": "maggo",
       "maggañca": "maggo", "saccañca": "saccaṃ"}
for _k in list(DHATU_NAMES):
    ACC[_k + "ṃ"] = _k
    ACC[_k + "ñca"] = _k
for _k in list(SACCA_NAMES):
    ACC[_k] = _k
    ACC[_k[:-1] + "ñca"] = _k
for _k in ("cakkhuviññāṇaṃ", "sotaviññāṇaṃ", "ghānaviññāṇaṃ", "jivhāviññāṇaṃ", "kāyaviññāṇaṃ",
           "manoviññāṇaṃ"):
    ACC[_k] = _k

# special subjects of the A-B-C answers -> (Hindi, number)
SUBJECTS = {
    "dibbacakkhu paññācakkhu": ("दिव्य आँख और प्रज्ञा की आँख", "pl"),
    "dibbasotaṃ taṇhāsotaṃ": ("दिव्य कान और तृष्णा की धारा", "pl"),
    "sīlagandho samādhigandho paññāgandho": ("सदाचार की गंध, एकाग्रता की गंध और प्रज्ञा की गंध", "pl"),
    "attharaso dhammaraso vimuttiraso": ("अर्थ का स्वाद, शिक्षा का स्वाद और मुक्ति का स्वाद", "pl"),
    "kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ": ("शारीरिक दुःख और मानसिक दुःख", "pl"),
}
AVASESA_NUM = {"avaseso": "sg", "avasesaṃ": "sg", "avasesā": "pl"}
COP = S.COP
PRON = S.PRON


def word(w):
    """Pāli word (any case of first letter, with or without -ti / -ñceva / ca) -> key of WORDS."""
    w = w.lower()
    if w in WORDS:
        return w
    if w.endswith("ūti") and w[:-3] + "u" in WORDS:     # dhātūti = dhātu + ti (singular predicate)
        return w[:-3] + "u"
    for cand in (w[:-2], w[:-3] + "ṃ", w[:-3] + "u", w[:-3] + "ū", w[:-3], w[:-5] + "ṃ", w[:-4] + "ṃ"):
        if cand in WORDS:
            return cand
    if w in ACC:
        return ACC[w]
    raise ValueError(f"word: {w}")


def is_word(w):
    try:
        word(w)
        return True
    except ValueError:
        return False


def W(w):
    return WORDS[word(w)]


def _base(w):
    """Stem before an enclitic -ñceva / -ñca ('sota' -> 'sotaṃ', 'cakkhudhātu' -> 'cakkhudhātu')."""
    w = w.lower()
    for cand in (w, w + "ṃ"):
        if cand in WORDS:
            return cand
    return None


def subject(s):
    """Subject of the A-B-C answers -> (Hindi, number)."""
    s0 = s.lower()
    if s0 in SUBJECTS:
        return SUBJECTS[s0]
    m = re.fullmatch(r"(.+?) ṭhapetvā (avaseso|avasesaṃ|avasesā)(?: (\S+))?", s0)
    if m:
        x = m.group(1)
        x_hi = SUBJECTS[x][0] if x in SUBJECTS else WORDS[ACC[x]][1]
        out = S.CHHODKAR.format(x=x_hi)
        if m.group(3):
            out += " " + W(m.group(3))[0]
        return out, AVASESA_NUM[m.group(2)]
    m = re.fullmatch(r"avasesā (\S+)", s0)
    if m:
        return f"{S.AVASESA} {W(m.group(1))[0]}", "pl"
    raise ValueError(f"subject: {s}")


# =====================================================================================================
# Paṇṇattivāra sentences
# =====================================================================================================
_LABEL = r"(?:\((Ka|Kha)\) )?"


def pannatti_question(s):
    """'(Ka) cakkhu cakkhudhātu?' / 'na A na B?' / unlabelled / without '?' (a fragment of an abbreviation)."""
    m = re.fullmatch(_LABEL + r"(na )?(\S+) (na )?(\S+?)(\?)?", s, flags=re.I)
    if not m or bool(m.group(2)) != bool(m.group(4)):
        return None
    if not (is_word(m.group(3)) and is_word(m.group(5))):
        return None
    lab = (S.LABELS[f"({m.group(1)})"] + " ") if m.group(1) else ""
    (ad, _, an), (bd, _, bn) = W(m.group(3)), W(m.group(5))
    q = m.group(6) or ""
    n2 = "pl" if "pl" in (an, bn) else "sg"
    if m.group(2):
        return f"{lab}जो {ad} नहीं {COP[an]}, क्या {PRON[an]} {bd} नहीं {COP[n2]}{q}"
    return f"{lab}क्या {ad}, {bd} {COP[n2]}{q}"


def pannatti_sentence(s):
    if s in FIXED_SENTENCES:
        return FIXED_SENTENCES[s]
    m = re.fullmatch(r"(.+?) (\S+), na (\S+)\.", s)                       # A B, na C.
    if m and is_word(m.group(2)) and is_word(m.group(3)):
        a, n = subject(m.group(1))
        return f"{a}, {W(m.group(2))[0]} {COP[n]}, पर {W(m.group(3))[0]} नहीं {COP[n]}।"
    m = re.fullmatch(r"(.+?) na (\S+), (\S+)\.", s)                       # A na C, B.
    if m and is_word(m.group(2)) and is_word(m.group(3)):
        a, n = subject(m.group(1))
        return f"{a}, {W(m.group(2))[0]} नहीं {COP[n]}, पर {W(m.group(3))[0]} {COP[n]}।"
    m = re.fullmatch(r"(.+?) (\S+?)(?:ñceva| ceva) (\S+?)(?:ñca| ca)\.", s)   # C B ceva C ca.
    if m and _base(m.group(2)) and _base(m.group(3)):
        b, c = WORDS[_base(m.group(2))], WORDS[_base(m.group(3))]
        subj = m.group(1)
        if is_word(subj):
            a, n = W(subj)[0], W(subj)[2]
        else:
            a, n = subject(subj)
        n = "pl" if "pl" in (n, b[2]) else n
        return f"{a}, {b[0]} भी {COP[n]} और {c[0]} भी।"
    m = re.fullmatch(r"(\S+?)(?:ñca| ca) (\S+?)(?:ñca| ca) ṭhapetvā (avaseso|avasesaṃ|avasesā) na ceva (\S+) "
                     r"na ca (\S+)\.", s)
    if m:
        b = WORDS[ACC[(m.group(1) + ("ñca" if (m.group(1) + "ñca").lower() in ACC else "")).lower()]]
        c = WORDS[ACC[(m.group(2) + "ñca").lower()]]
        n = AVASESA_NUM[m.group(3)]
        return (f"{b[1]} और {c[1]} को छोड़कर {S.AVASESA} न तो {W(m.group(4))[0]} {COP[n]}, "
                f"न {W(m.group(5))[0]}।")
    m = re.fullmatch(r"(.+?) na (\S+)\.", s)                              # <subj> na C.
    if m and is_word(m.group(2)):
        a, n = subject(m.group(1))
        return f"{a}, {W(m.group(2))[0]} नहीं {COP[n]}।"
    return None


def word_fragment(s):
    """Bare items of an abbreviated list: 'Ghānaṃ', 'na ghānaṃ', 'Ghānaviññāṇaṃ?', 'Na ghānaṃ?',
    'sotaṃ ṭhapetvā', 'jivha ṭhapetvā'."""
    m = re.fullmatch(r"(na )?(\S+?)( ṭhapetvā)?(\?)?", s, flags=re.I)
    if not m:
        return None
    w = m.group(2).lower()
    key = ACC.get(w) if m.group(3) else (w if w in WORDS else ACC.get(w))
    if key is None:
        return None
    hi = WORDS[key][1] + " को छोड़कर" if m.group(3) else WORDS[key][0]
    if m.group(1):
        hi += " नहीं"
    return hi + (m.group(4) or "")


# =====================================================================================================
# Pavattivāra
# =====================================================================================================
SUBJ = {k: (v, "m") for k, v in {**DHATU_NAMES, **SACCA_NAMES}.items()}   # तत्व, सत्य: masculine
_SUBJ_RE = "|".join(sorted(map(re.escape, SUBJ), key=len, reverse=True))


def verb_hi(tok, flip=False):
    return S.verb_hi(tok, "m", flip)


def strip_ti_verb(v):
    for cand in (v, v[:-3] + "i", v[:-3] + "a"):
        w = cand[3:] if cand.startswith("na ") else cand
        if w in S.VERB_FORMS:
            return cand
    raise ValueError(f"verb: {v}")


_REL = r"(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha)"
_COR = r"(tassa tattha|tassa|tattha)"


def pavatti_question(s):
    m = re.fullmatch(_LABEL + _REL + rf" ({_SUBJ_RE}) ((?:na )?\S+) " + _COR + rf" ({_SUBJ_RE}) ((?:na )?\S+)\?",
                     s[0].lower() + s[1:] if not s.startswith("(") else s)
    if not m:
        return None
    lab, rel, k1, v1, cor, k2, v2 = m.groups()
    rel_hi, cor_hi = S.REL_FRAMES[(rel, cor)]
    out = S.Q_FRAME.format(label="", rel=rel_hi, k1=SUBJ[k1][0], v1=verb_hi(v1), corr=cor_hi, k2=SUBJ[k2][0],
                           v2=verb_hi(strip_ti_verb(v2)))
    return (S.LABELS[f"({lab})"] + out) if lab else out[1:]


REL_ONLY = {"yattha vā pana": "और जिस स्थान पर", "yassa vā pana": "और जिस व्यक्ति में",
            "yassa vā pana yattha": "और जिस व्यक्ति में जिस स्थान पर", "yo vā pana": "और जो व्यक्ति",
            "yattha": "जिस स्थान पर", "yassa": "जिस व्यक्ति में", "yassa yattha": "जिस व्यक्ति में जिस स्थान पर"}


def pavatti_fragment(s):
    """Parts of abbreviated questions: '(Kha) yattha vā pana', 'Yattha dukkhasaccaṃ uppajjittha',
    '(Kha) yassa vā pana yattha samudayasaccaṃ uppajjissati', 'uppajjitthāti?'."""
    m = re.fullmatch(_LABEL + r"(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha|"
                     r"yo vā pana)(?: (" + _SUBJ_RE + r") ((?:na )?\S+))?", s[0].lower() + s[1:]
                     if not s.startswith("(") else s)
    if m:
        lab = (S.LABELS[f"({m.group(1)})"] + " ") if m.group(1) else ""
        out = lab + REL_ONLY[m.group(2)]
        if m.group(3):
            out += f" {SUBJ[m.group(3)][0]} {verb_hi(m.group(4))}"
        return out
    m = re.fullmatch(r"((?:na )?\S+?)\?", s)
    if m:
        try:
            return verb_hi(strip_ti_verb(m.group(1))) + "?"
        except (ValueError, KeyError):
            return None
    return None


# ---------------- beings, places, moments (Saccayamaka chains; Dhātuyamaka organ beings) ----------------
PART = {"upapajjantānaṃ": "जन्म लेने वालों में", "cavantānaṃ": "मरने वालों में"}
ORGAN_MODS = {"sacakkhukānaṃ": "आँख वाले", "acakkhukānaṃ": "आँख से रहित", "sasotakānaṃ": "कान वाले",
              "asotakānaṃ": "कान से रहित", "saghānakānaṃ": "नाक वाले", "aghānakānaṃ": "नाक से रहित",
              "sarūpakānaṃ": "भौतिक रूप वाले", "sacittakānaṃ": "मन वाले"}
BEINGS_G = {  # genitive plural beings -> chunk with «में»
    "arahantānaṃ": "अर्हतों में",
    "aggamaggasamaṅgīnaṃ": "सर्वोच्च मार्ग से युक्त लोगों में",
    "abhisametāvīnaṃ": "सत्यों का बोध पा चुके लोगों में",
    "anabhisametāvīnaṃ": "सत्यों का बोध न पाए लोगों में",
    "pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त लोगों में",
    "nirodhasamāpannānaṃ": "समाप्ति की ध्यान-अवस्था में लीन लोगों में",
    "asaññasattānaṃ": S.BEINGS["asaññasattānaṃ"],
    "āpāyikānaṃ": S.BEINGS["āpāyikānaṃ"],
    "suddhāvāsānaṃ": S.BEINGS["suddhāvāsānaṃ"],
    "catuvokārānaṃ pañcavokārānaṃ": f"{S.PLACE_NOUN['catupañcavokāra']} के प्राणियों में",
}
MOMENTS = {
    "cittassa uppādakkhaṇe": "मन के उत्पन्न होने के क्षण में",
    "cittassa bhaṅgakkhaṇe": "मन के भंग होने के क्षण में",
    "taṇhāvippayuttacittassa uppādakkhaṇe": "तृष्णा से अलग मन के उत्पन्न होने के क्षण में",
    "maggavippayuttacittassa uppādakkhaṇe": "मार्ग से अलग मन के उत्पन्न होने के क्षण में",
    "taṇhāvippayuttamaggavippayuttacittassa uppādakkhaṇe":
        "तृष्णा से अलग और मार्ग से अलग मन के उत्पन्न होने के क्षण में",
    "maggavippayuttataṇhāvippayuttacittassa uppādakkhaṇe":
        "मार्ग से अलग और तृष्णा से अलग मन के उत्पन्न होने के क्षण में",
    "taṇhāya uppādakkhaṇe": "तृष्णा के उत्पन्न होने के क्षण में",
    "taṇhāya bhaṅgakkhaṇe": "तृष्णा के भंग होने के क्षण में",
    "taṇhāvippayuttacitte vattamāne": "तृष्णा से अलग मन के चलते समय",
    "dutiye citte vattamāne": "दूसरे मन के चलते समय",
    "dutiye akusale citte vattamāne": "दूसरे हानिकर मन के चलते समय",
    "maggassa uppādakkhaṇe": "मार्ग के उत्पन्न होने के क्षण में",
    "maggassa ca phalassa ca uppādakkhaṇe": "मार्ग और फल के उत्पन्न होने के क्षण में",
    "phalassa uppādakkhaṇe": "फल के उत्पन्न होने के क्षण में",
    "aggamaggassa uppādakkhaṇe": "सर्वोच्च मार्ग के उत्पन्न होने के क्षण में",
    "aggamaggassa bhaṅgakkhaṇe": "सर्वोच्च मार्ग के भंग होने के क्षण में",
    "aggamaggassa ca phalassa ca uppādakkhaṇe": "सर्वोच्च मार्ग और फल के उत्पन्न होने के क्षण में",
    "aggaphalassa uppādakkhaṇe": "सर्वोच्च फल के उत्पन्न होने के क्षण में",
    "upapatticittassa uppādakkhaṇe": "जन्म के मन के उत्पन्न होने के क्षण में",
    "upapatticittassa bhaṅgakkhaṇe": "जन्म के मन के भंग होने के क्षण में",
    # yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe / bhaṅgakkhaṇe
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe":
        "जिस मन के ठीक बाद वे सर्वोच्च मार्ग प्राप्त करेंगे, उस मन के उत्पन्न होने के क्षण में",
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa bhaṅgakkhaṇe":
        "जिस मन के ठीक बाद वे सर्वोच्च मार्ग प्राप्त करेंगे, उस मन के भंग होने के क्षण में",
}
RELATIVES = {  # relative clauses about persons; correlative «, उनमें» added by the chain builder
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissanti": "जो इस मन के ठीक बाद सर्वोच्च मार्ग प्राप्त करेंगे",
    "ye ca puthujjanā maggaṃ na paṭilabhissanti": "जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे",
    "ye puthujjanā maggaṃ na paṭilabhissanti": "जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे",
    "ye caññe maggaṃ paṭilabhissanti": "जो दूसरे लोग मार्ग प्राप्त करेंगे",
    "ye maggaṃ paṭilabhissanti": "जो मार्ग प्राप्त करेंगे",
}
UNMEN = "उनमें"            # tesaṃ after a relative
UNMEN_SE = "उनमें से"      # tesaṃ + participle after a relative (harmonise B3)
LOGON_SE = "में से"        # being + participle: «… लोगों में से जन्म लेने वालों में»
SABBESAM_CITTA = "सभी के"  # sabbesaṃ + moment (harmonise B5)
ARAHANTANAM_CITTA = "अर्हतों के"   # arahantānaṃ cittassa X = «अर्हतों के मन के X होने के क्षण में» (as 5-02)
PAVATTE = "जीवन के दौरान"
AVASESE = "बाकी"           # Avasese (place), termbase

# phrase table: Pāli token tuple -> (kind, value); matched longest first
PHRASES = {}
for _k, _v in MOMENTS.items():
    PHRASES[tuple(_k.split())] = ("moment", _v)
for _k, _v in RELATIVES.items():
    PHRASES[tuple(_k.split())] = ("rel", _v)
for _k, _v in BEINGS_G.items():
    PHRASES[tuple(_k.split())] = ("being", _v)
for _k, _v in PART.items():
    PHRASES[(_k,)] = ("part", _v)
for _k, _v in ORGAN_MODS.items():
    PHRASES[(_k,)] = ("mod", _v)
PHRASES[("sabbesaṃ",)] = ("sabbesam", S.SABBESAM)
PHRASES[("itaresaṃ",)] = ("itaresam", S.ITARESAM)
PHRASES[("pavatte",)] = ("pre", PAVATTE)
PHRASES[("tesaṃ",)] = ("tesam", None)
for _f, (_key, _case) in S.PLACE_FORMS.items():
    PHRASES[(_f,)] = ("place", (_key, _case))
PHRASES[("catuvokāraṃ", "pañcavokāraṃ")] = ("place", ("catupañcavokāra", "acc"))
PHRASES[("catuvokārā", "pañcavokārā")] = ("place", ("catupañcavokāra", "abl"))
PHRASES[("catuvokāre", "pañcavokāre")] = ("place", ("catupañcavokāra", "loc"))
PHRASES[("asaññattā",)] = ("place", ("asaññasatta", "abl"))      # source slip, ^6-5-76
_MAXLEN = max(map(len, PHRASES))


def _norm_chain(s):
    s = s[0].lower() + s[1:]
    s = s.replace(",", "").replace("paṭilabhissānti", "paṭilabhissanti")
    return s.split()


def _items(s):
    toks, out, i = _norm_chain(s), [], 0
    while i < len(toks):
        for n in range(min(_MAXLEN, len(toks) - i), 0, -1):
            t = tuple(toks[i:i + n])
            if t in PHRASES:
                out.append(PHRASES[t])
                i += n
                break
        else:
            raise ValueError(f"chain: unknown token {toks[i]!r} in {s!r}")
    return out


def who(s):
    """Being / place / moment chain (before the frame's tesaṃ) -> Hindi; chunks end in «में» (or «समय»),
    joined «, » and « और » before the last (harmonise B8, B9)."""
    items = _items(s)
    chunks, pre, mods, place, i = [], [], [], None, 0

    def flush_check():
        if mods or place:
            raise ValueError(f"who: dangling modifier in {s!r}")

    while i < len(items):
        kind, val = items[i]
        nxt = items[i + 1] if i + 1 < len(items) else (None, None)
        if kind == "sabbesam":
            if nxt[0] == "moment":
                chunks.append(f"{SABBESAM_CITTA} {nxt[1]}")
                i += 2
                continue
            pre.append(val)
        elif kind == "itaresam":
            pre.append(val)
        elif kind == "pre":
            pre.append(val)
        elif kind == "mod":
            mods.append(val)
        elif kind == "place":
            key, case = val
            if case == "loc":
                pre.append(f"{S.PLACE_NOUN[key]} में")
            else:
                place = (key, case)
        elif kind == "moment":
            chunks.append(" ".join(pre + [val]))
            pre = []
        elif kind == "part":
            words = list(pre)
            if mods:
                words.append(S.JOIN_LAST.join(mods) if len(mods) <= 2 else ", ".join(mods[:-1]) + " और " + mods[-1])
            if place:
                words.append(f"{S.PLACE_NOUN[place[0]]} {S.CASE_POST[place[1]]}")
            words.append(val)
            chunks.append(" ".join(words))
            pre, mods, place = [], [], None
        elif kind == "being":
            flush_check()
            if nxt[0] == "part":
                chunks.append(" ".join(pre + [val[:-len("में")] + LOGON_SE, nxt[1]]))
                i += 2
                pre = []
                continue
            if nxt[0] == "moment" and val == BEINGS_G["arahantānaṃ"] and nxt[1].startswith("मन के "):
                chunks.append(" ".join(pre + [ARAHANTANAM_CITTA + " " + nxt[1]]))   # as 5-02
                i += 2
                pre = []
                continue
            if nxt[0] == "moment":
                chunks.append(" ".join(pre + [val, nxt[1]]))
                i += 2
                pre = []
                continue
            chunks.append(" ".join(pre + [val]))
            pre = []
        elif kind == "rel":
            flush_check()
            if pre:
                raise ValueError(f"who: prefix before a relative in {s!r}")
            # consecutive relatives share one «उनमें», joined « और » (as 5-02)
            rels = [val]
            while nxt[0] == "rel":
                rels.append(nxt[1])
                i += 1
                nxt = items[i + 1] if i + 1 < len(items) else (None, None)
            val = S.JOIN_LAST.join(rels)
            if nxt[0] == "tesam":
                n2 = items[i + 2] if i + 2 < len(items) else (None, None)
                if n2[0] == "part":
                    chunks.append(f"{val}, {UNMEN_SE} {n2[1]}")
                    i += 3
                    continue
                if n2[0] == "moment":
                    chunks.append(f"{val}, {UNMEN} {n2[1]}")
                    i += 3
                    continue
                chunks.append(f"{val}, {UNMEN}")
                i += 2
                continue
            chunks.append(f"{val}, {UNMEN}")
        elif kind == "tesam":
            raise ValueError(f"who: stray tesaṃ in {s!r}")
        i += 1
    if pre == [S.ITARESAM] and not chunks:
        return S.ITARESAM_ALONE
    if pre or mods or place:
        raise ValueError(f"who: dangling tokens in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


def place(s):
    s0 = s[0].lower() + s[1:]
    if s0.startswith("avasese "):
        return f"{AVASESE} {S.place(s0[len('avasese '):])}"
    return S.place(s0)


_T = r"(tesaṃ tattha|tesaṃ|tattha)"


def pavatti_sentence(s):
    s1 = s.replace("saccañca ", "saccaṃ ca ")
    m = re.fullmatch(rf"(.+?) {_T} ({_SUBJ_RE}) ((?:na )?\S+), no ca (?:tesaṃ tattha|tesaṃ|tattha) ({_SUBJ_RE}) "
                     r"((?:na )?\S+)\.", s1)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        v1h, v2h = verb_hi(v1), verb_hi(v2, flip=True)
        if t == "tattha":
            return S.BUT_PLACE.format(place=place(wh), k1=SUBJ[k1][0], v1=v1h, k2=SUBJ[k2][0], v2=v2h)
        frame = S.BUT_BEINGS_T if t == "tesaṃ tattha" else S.BUT_BEINGS
        return frame.format(who=who(wh), k1=SUBJ[k1][0], v1=v1h, k2=SUBJ[k2][0], v2=v2h)
    m = re.fullmatch(rf"(.+?) {_T} ({_SUBJ_RE}) ca ((?:na )?\S+) ({_SUBJ_RE}) ca ((?:na )?\S+)\.", s1)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        v1h, v2h = verb_hi(v1), verb_hi(v2)
        if t == "tattha":
            return S.BOTH_PLACE.format(place=place(wh), k1=SUBJ[k1][0], v1=v1h, k2=SUBJ[k2][0], v2=v2h)
        frame = S.BOTH_BEINGS_T if t == "tesaṃ tattha" else S.BOTH_BEINGS
        return frame.format(who=who(wh), k1=SUBJ[k1][0], v1=v1h, k2=SUBJ[k2][0], v2=v2h)
    return None


def pavatti_partial(s):
    """'<chain> tesaṃ tattha dukkhasaccaṃ' (before …pe…) -> «<who> वहाँ दुःख का सत्य»."""
    m = re.fullmatch(rf"(.+?) {_T} ({_SUBJ_RE})", s)
    if not m:
        return None
    wh, t, k = m.groups()
    there = " वहाँ" if t == "tesaṃ tattha" else ""
    return f"{who(wh)}{there} {SUBJ[k][0]}"


# ---------------- Pariññāvāra ----------------
PAJAHATI = {"pajahati": ("छोड़ता है", "नहीं छोड़ता"), "pajahittha": ("छोड़ा था", "नहीं छोड़ा था"),
            "pajahissati": ("छोड़ेगा", "नहीं छोड़ेगा")}
PARI_VERBS = {**S.PARIJANATI, **PAJAHATI}
PARI_FORMS = {"parijānāti": ("parijānāti", False), "parijānittha": ("parijānittha", False),
              "parijānissati": ("parijānissati", False), "pajahati": ("pajahati", False),
              "nappajahati": ("pajahati", True), "pajahittha": ("pajahittha", False),
              "nappajahittha": ("pajahittha", True), "pajahissati": ("pajahissati", False),
              "nappajahissati": ("pajahissati", True)}
ACC_OBJ = {**{k + "ṃ": _obl(v) for k, v in DHATU_NAMES.items()},
           **{k: _obl(v) for k, v in SACCA_NAMES.items()}}


def _pv(v):
    neg = v.startswith("na ")
    w = v[3:] if neg else v
    for cand in (w, w[:-3] + "i", w[:-3] + "a"):
        if cand in PARI_FORMS:
            stem, n = PARI_FORMS[cand]
            return PARI_VERBS[stem][1 if (neg or n) else 0], stem.endswith("ittha")
    raise ValueError(f"pariññā verb: {v}")


def parinna_question(s):
    m = re.fullmatch(_LABEL + r"(yo|Yo)( vā pana)? (\S+) ((?:na )?\S+) so (\S+) ((?:na )?\S+)\?", s)
    if not m or m.group(4) not in ACC_OBJ or m.group(6) not in ACC_OBJ:
        return None
    lab, _, vp, o1, v1, o2, v2 = m.groups()
    v1h, past1 = _pv(v1)
    v2h, past2 = _pv(v2)
    rel = ("और " if vp else "") + ("जिस व्यक्ति ने" if past1 else "जो व्यक्ति")
    cor = "उसने" if past2 else "वह"
    out = f"{rel} {ACC_OBJ[o1]} को {v1h}, क्या {cor} {ACC_OBJ[o2]} को {v2h}?"
    return (S.LABELS[f"({lab})"] + " " + out) if lab else out


# =====================================================================================================
# Fixed lines and sentences (unique lines, translated one by one)
# =====================================================================================================
FIXED_LINES = {
    # 4 ^6-4-1
    "Aṭṭhārasa dhātuyo – cakkhudhātu, sotadhātu, ghānadhātu, jivhādhātu, kāyadhātu, rūpadhātu, saddadhātu, "
    "gandhadhātu, rasadhātu, phoṭṭhabbadhātu, cakkhuviññāṇadhātu, sotaviññāṇadhātu, ghānaviññāṇadhātu, "
    "jivhāviññāṇadhātu, kāyaviññāṇadhātu, manodhātu, manoviññāṇadhātu, dhammadhātu.":
        "अठारह तत्व – आँख का तत्व, कान का तत्व, नाक का तत्व, जीभ का तत्व, शरीर का तत्व, दृश्य रूप का तत्व, "
        "ध्वनि का तत्व, गंध का तत्व, स्वाद का तत्व, स्पर्श का तत्व, आँख की चेतना का तत्व, कान की चेतना का तत्व, "
        "नाक की चेतना का तत्व, जीभ की चेतना का तत्व, शरीर की चेतना का तत्व, मन का तत्व, मन की चेतना का तत्व, "
        "मन के विषयों का तत्व।",
    # 4 ^6-4-4
    "(Kha) dhātū [dhātu (sī. ka.) aññehi yamakehi saṃsanditabbaṃ] sotadhātu?…Pe…":
        "(ख) क्या तत्व [वर्तनी-भेद (Sī., Ka.): dhātu; प्रश्नों के दूसरे जोड़ों से मिलान करना चाहिए], कान का तत्व हैं?…",
    "(Yathā āyatanayamake cakkaṃ bandhitaṃ evamidha cakkaṃ bandhitabbaṃ.)":
        "(जैसे “इंद्रिय-क्षेत्रों पर प्रश्नों के जोड़े” में चक्र पूरा किया गया है, वैसे ही यहाँ भी चक्र पूरा करना "
        "चाहिए।)",
    # 4 ^6-4-11
    "Na jivhā… (saṃkhittaṃ [yaṃ saṃkhittaṃ (syā.)], ubhato āmantā).":
        "जीभ नहीं… (संक्षिप्त किया गया है [पाठभेद (Syā.): yaṃ saṃkhittaṃ], दोनों प्रश्नों का उत्तर “हाँ” है)।",
    # 4 ^6-4-12
    "(Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti. Cakkaṃ bandhitabbaṃ).":
        "(जैसे “इंद्रिय-क्षेत्रों पर प्रश्नों के जोड़े” में शब्दावली है, वैसे ही “तत्वों पर प्रश्नों के जोड़े” में "
        "भी शब्दावली है। चक्र पूरा करना चाहिए)।",
    # 4 ^6-4-13
    "(Cakkaṃ bandhitabbaṃ, sabbe āmantā ubhatopi sesepi).":
        "(चक्र पूरा करना चाहिए, दोनों प्रश्नों में भी और शेष में भी सभी उत्तर “हाँ” हैं)।",
    # 4 ^6-4-17
    "(Yathā āyatanayamakassa paṇṇatti evaṃ dhātuyamakassa paṇṇatti vitthāretabbā)":
        "(जैसे “इंद्रिय-क्षेत्रों पर प्रश्नों के जोड़े” की शब्दावली का विस्तार किया गया है, वैसे ही “तत्वों पर "
        "प्रश्नों के जोड़े” की शब्दावली का विस्तार करना चाहिए)",
    # 4 ^6-4-18
    "(Yathā āyatanayamakaṃ vibhattaṃ evaṃ dhātuyamakampi vibhajitabbaṃ, sadisaṃ kātabbaṃ).":
        "(जैसे “इंद्रिय-क्षेत्रों पर प्रश्नों के जोड़े” का विभाजन किया गया है, वैसे ही “तत्वों पर प्रश्नों के "
        "जोड़े” का भी विभाजन करना चाहिए, उसी के समान करना चाहिए)।",
    # 5-01 ^6-5-1 (the Pāli lacks the comma after samudayasaccaṃ)
    "Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ.":
        "चार सत्य – दुःख का सत्य, उत्पत्ति का सत्य, अंत का सत्य, मार्ग का सत्य।",
    # 5-01 ^6-5-31
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        "(व्यक्ति वाले भाग का भी और व्यक्ति और स्थान वाले भाग का भी समान रूप से विस्तार करना चाहिए)।",
    # 5-01 ^6-5-40
    "(Yatthakampi sabbattha sadisaṃ. Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ).":
        "(स्थान वाला भाग भी हर जगह समान है। पाठ में अंतर पहले आए स्थान वाले भाग के समान है)।",
    # 5-03 ^6-5-164
    "(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā anulomampi paccanīkampi vibhattā evaṃ "
    "uppādanirodhavārepi asammohantena vibhajitabbaṃ).":
        "(जैसे समाप्त होने के खंड में अतीत और भविष्य के [वर्तनी-भेद (Syā.): atītenānāgatā] प्रश्नों का "
        "सकारात्मक भी और नकारात्मक भी विभाजन किया गया है, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी "
        "बिना भ्रम के विभाजन करना चाहिए)।",
}
FIXED_SENTENCES = {
    # notes
    "(Cakkaṃ bandhitabbaṃ).": "(चक्र पूरा करना चाहिए)।",
    "(Jivhāpi ghānadhātusadisā).": "(जीभ भी नाक के तत्व के समान है)।",
    "(Saddo ghānasadiso).": "(ध्वनि नाक के समान है)।",
    "(Phoṭṭhabbo ghānasadiso).": "(स्पर्श नाक के समान है)।",
    "(dhātuyamakaṃ paripuṇṇaṃ peyyālena).": "(“तत्वों पर प्रश्नों के जोड़े” संक्षेप के साथ पूरे हैं)।",
    "(yatthakā sadisā sabbe).": "(स्थान वाले सभी भाग समान हैं)।",
    "(yatthakampi yassayatthakasadisaṃ kātabbaṃ).": "(स्थान वाला भाग भी व्यक्ति और स्थान वाले भाग के समान करना चाहिए)।",
    # closings
    "Uppādavāro.": "उत्पन्न होने का खंड।",
    "Dhātuyamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Dhātuyamakaṃ"]),
    "Saccayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Saccayamakaṃ"]),
    "Uppajjittha.": S.verb_hi("uppajjittha", "m") + "।",
    "Uppajjissati.": S.verb_hi("uppajjissati", "m") + "।",
    # variant brackets in the Paṇṇatti answers
    "Kāyadhātuṃ ṭhapetvā avaseso kāyo [avaseso kāyo kāyo (syā.)], na kāyadhātu.":
        "शरीर के तत्व को छोड़कर शेष, शरीर है [पाठभेद (Syā.): avaseso kāyo kāyo], पर शरीर का तत्व नहीं है।",
    "Kāyañca kāyadhātuñca ṭhapetvā avaseso [avaseso kāyo (syā.)] na ceva kāyo na ca kāyadhātu.":
        "शरीर और शरीर के तत्व को छोड़कर शेष [पाठभेद (Syā.): avaseso kāyo] न तो शरीर है, न शरीर का तत्व।",
    "Avasesā dhātū [avasesā dhātū dhātū (syā.)] na sotadhātu.":
        "शेष तत्व [पाठभेद (Syā.): avasesā dhātū dhātū], कान का तत्व नहीं हैं।",
    "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ dukkhasaccaṃ [avasesaṃ dukkhasaccaṃ dukkhasaccaṃ (syā.) "
    "evamuparipi], na dukkhaṃ.":
        "शारीरिक दुःख और मानसिक दुःख को छोड़कर शेष, दुःख का सत्य है [पाठभेद (Syā.): avasesaṃ dukkhasaccaṃ "
        "dukkhasaccaṃ; आगे भी इसी प्रकार], पर दुःख नहीं है।",
    "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ na dukkhaṃ [avasesaṃ dukkhasaccaṃ na dukkhaṃ (sī. syā. ka.) "
    "evaṃ avasesesu tīsu saccesu] dukkhasaccaṃ.":
        "शारीरिक दुःख और मानसिक दुःख को छोड़कर शेष, दुःख नहीं है [पाठभेद (Sī., Syā., Ka.): avasesaṃ dukkhasaccaṃ "
        "na dukkhaṃ; शेष तीन सत्यों में भी इसी प्रकार], पर दुःख का सत्य है।",
    "Avasesā saccā [avasesā saccā saccā (syā.)] na samudayasaccaṃ.":
        "शेष सत्य [पाठभेद (Syā.): avasesā saccā saccā], उत्पत्ति का सत्य नहीं हैं।",
    # Pariññāvāra answers (5-03 ^6-5-168, ^6-5-169, ^6-5-170)
    "Arahā dukkhasaccaṃ na parijānāti, no ca samudayasaccaṃ nappajahittha.":
        "अर्हत् दुःख के सत्य को पूरी तरह नहीं समझता, पर उसने उत्पत्ति के सत्य को छोड़ा था।",
    "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā dukkhasaccañca na parijānanti samudayasaccañca "
    "nappajahittha.":
        "सर्वोच्च मार्ग से युक्त व्यक्ति और अर्हत् को छोड़कर शेष व्यक्ति दुःख के सत्य को भी पूरी तरह नहीं समझते "
        "और उन्होंने उत्पत्ति के सत्य को भी नहीं छोड़ा था।",
    "Aggamaggasamaṅgī samudayasaccaṃ nappajahittha, no ca dukkhasaccaṃ na parijānāti.":
        "सर्वोच्च मार्ग से युक्त व्यक्ति ने उत्पत्ति के सत्य को नहीं छोड़ा था, पर वह दुःख के सत्य को पूरी तरह "
        "समझता है।",
    "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā samudayasaccañca nappajahittha dukkhasaccañca na "
    "parijānanti.":
        "सर्वोच्च मार्ग से युक्त व्यक्ति और अर्हत् को छोड़कर शेष व्यक्तियों ने उत्पत्ति के सत्य को भी नहीं छोड़ा "
        "था और वे दुःख के सत्य को भी पूरी तरह नहीं समझते।",
    "Ye maggaṃ paṭilabhissanti te dukkhasaccaṃ na parijānanti, no ca samudayasaccaṃ nappajahissanti.":
        "जो मार्ग प्राप्त करेंगे, वे दुःख के सत्य को पूरी तरह नहीं समझते, पर वे उत्पत्ति के सत्य को छोड़ेंगे।",
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te dukkhasaccañca na parijānanti samudayasaccañca "
    "nappajahissanti.":
        "अर्हत् और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, वे दुःख के सत्य को भी पूरी तरह नहीं समझते और "
        "उत्पत्ति के सत्य को भी नहीं छोड़ेंगे।",
    "Aggamaggasamaṅgī samudayasaccaṃ nappajahissati, no ca dukkhasaccaṃ na parijānāti.":
        "सर्वोच्च मार्ग से युक्त व्यक्ति उत्पत्ति के सत्य को नहीं छोड़ेगा, पर वह दुःख के सत्य को पूरी तरह समझता "
        "है।",
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te samudayasaccañca nappajahissanti dukkhasaccañca na "
    "parijānanti.":
        "अर्हत् और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, वे उत्पत्ति के सत्य को भी नहीं छोड़ेंगे और दुःख के "
        "सत्य को भी पूरी तरह नहीं समझते।",
    "Ye maggaṃ paṭilabhissanti te dukkhasaccaṃ na parijānittha, no ca te samudayasaccaṃ nappajahissanti.":
        "जो मार्ग प्राप्त करेंगे, उन्होंने दुःख के सत्य को पूरी तरह नहीं समझा था, पर वे उत्पत्ति के सत्य को "
        "छोड़ेंगे।",
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te dukkhasaccañca na parijānittha "
    "samudayasaccañca nappajahissanti.":
        "सर्वोच्च मार्ग से युक्त व्यक्ति और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, उन्होंने दुःख के सत्य को भी "
        "पूरी तरह नहीं समझा था और वे उत्पत्ति के सत्य को भी नहीं छोड़ेंगे।",
    "Arahā samudayasaccaṃ nappajahissati, no ca dukkhasaccaṃ na parijānittha.":
        "अर्हत् उत्पत्ति के सत्य को नहीं छोड़ेगा, पर उसने दुःख के सत्य को पूरी तरह समझा था।",
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te samudayasaccañca nappajahissanti "
    "dukkhasaccañca na parijānittha.":
        "सर्वोच्च मार्ग से युक्त व्यक्ति और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, वे उत्पत्ति के सत्य को भी "
        "नहीं छोड़ेंगे और उन्होंने दुःख के सत्य को भी पूरी तरह नहीं समझा था।",
}
# variant brackets inside being chains: Pāli bracket -> (Hindi bracket, Hindi anchor it follows)
CHAIN_VARIANTS = {
    "[taṇhāvippayuttamaggavippayuttacittassa (sī.) evaṃ puggalokāsepi nirodhavārepi]":
        ("[पाठभेद (Sī.): taṇhāvippayuttamaggavippayuttacittassa; इसी प्रकार व्यक्ति और स्थान वाले भाग में भी और "
         "समाप्त होने के खंड में भी]", "मार्ग से अलग और तृष्णा से अलग मन"),
    "[uppatticittassa (syā.)]": ("[वर्तनी-भेद (Syā.): uppatticittassa]", "जन्म के मन"),
    "[paṭilabhissanti tassa cittassa uppādakkhaṇe ye (sī. syā.) puggalokāsavārepi]":
        ("[पाठभेद (Sī., Syā.): paṭilabhissanti tassa cittassa uppādakkhaṇe ye; व्यक्ति और स्थान वाले खंड में भी]",
         "जो इस मन के ठीक बाद सर्वोच्च मार्ग प्राप्त करेंगे"),
    "[apāyā asaññasattā (syā.)]": ("[पाठभेद (Syā.): apāyā asaññasattā]", "पहचान-रहित प्राणियों के लोक से"),
    "[apāyaṃ asaññasattaṃ (syā.)]": ("[पाठभेद (Syā.): apāyaṃ asaññasattaṃ]", "पहचान-रहित प्राणियों के लोक में"),
}

HEADINGS_EXTRA = {"Paṇṇattivāra": "शब्दावली का खंड"}


# =====================================================================================================
# Driver
# =====================================================================================================
def translate_sentence(s):
    if s in S.CLOSINGS:
        return S.CLOSINGS[s]
    if s in FIXED_SENTENCES:
        return FIXED_SENTENCES[s]
    for fn in (pavatti_question, parinna_question, pannatti_question, pannatti_sentence, pavatti_sentence):
        r = fn(s)
        if r:
            return r
    if s in ("Āmantā.", "No.", "Natthi.", "Uppajjati.", "Nuppajjati."):
        return S.short_answer(s, "m")
    if s == "Āmantā":   # «Āmantā…pe….»
        return S.AMANTA[:-1]
    for fn in (pavatti_fragment, word_fragment, pavatti_partial):
        r = fn(s)
        if r:
            return r
    raise ValueError(f"no formula for: {s}")


_SEP = re.compile(r"(…[Pp]e…|…)")


def translate_text_line(line):
    if line in FIXED_LINES:
        return FIXED_LINES[line]
    # chain variants: remove, translate, re-insert after the anchor
    inserts = []
    for pv, (hv, anchor) in CHAIN_VARIANTS.items():
        if pv in line:
            line = line.replace(" " + pv, "")
            inserts.append((hv, anchor))
    pieces = _SEP.split(line)
    out = []
    for k, piece in enumerate(pieces):
        if k % 2 == 1:
            out.append("…")
            continue
        if not piece.strip():
            out.append(piece)
            continue
        lead = piece[: len(piece) - len(piece.lstrip())]
        trail = piece[len(piece.rstrip()):]
        body = piece.strip()
        hi_parts = []
        if body.startswith(".") or body.startswith("?"):
            mark, body = body[0], body[1:].lstrip()
            prev = "".join(out).rstrip().rstrip("…")
            if mark == "?":
                hi_parts.append("?")
            elif not prev.endswith(("?", "।")):
                hi_parts.append("।")
            if not body:
                out.append("".join(hi_parts) + trail)
                continue
            lead = "".join(hi_parts) + " "     # the mark attaches to what precedes; a space before the text
        sents = S._split_sentences(body)
        sent_hi = [translate_sentence(x) for x in sents]
        out.append(lead + " ".join(sent_hi) + trail)
    res = "".join(out)
    for hv, anchor in inserts:
        if anchor not in res:
            raise ValueError(f"variant anchor not found: {anchor} in {res}")
        res = res.replace(anchor, f"{anchor} {hv}", 1)
    return res


def translate_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        hd = {**S.HEADINGS, **HEADINGS_EXTRA}
        if text not in hd:
            raise ValueError(f"unknown heading: {text}")
        return f"{hashes} {hd[text]}{bid}"
    return translate_text_line(line.strip()) + bid


def translate_text(pali_text, errors=None):
    out, prev_blank = [], True
    for n, line in enumerate(pali_text.splitlines(), 1):
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        try:
            out.append(translate_line(line))
        except (ValueError, KeyError) as e:
            if errors is None:
                raise
            errors.append(f"line {n}: {e!r}")
            out.append("@@ " + line)
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main():
    dry = "--dry" in sys.argv
    for f in FILES:
        pali = (S.PALI_DIR / f).read_text(encoding="utf-8")
        errs = []
        hi = translate_text(pali, errs)
        print(f, "failures:", len(errs))
        for e in errs[:40]:
            print("  ", e)
        if not dry and not errs:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
            print("  written")


if __name__ == "__main__":
    main()
