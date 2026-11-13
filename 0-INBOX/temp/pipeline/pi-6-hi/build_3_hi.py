r"""pi-6 Yamaka, Āyatanayamaka (3-01 … 3-06): Hindi plain zero-shot builder.

usage: python -I -X utf8 build_3_hi.py [--check]
Translates AI_translation\pali\pi-6_split_chapters\3-0N-ayatanayamaka.md (N = 1..6)
into AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\ (same names).
Every line is composed from the approved sample frames (build_sample_hi, imported, never
edited) plus the āyatana item table below; an unknown line raises an error.
--check: translate everything, report untranslated lines, write nothing.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402

FILES = [f"3-0{n}-ayatanayamaka.md" for n in range(1, 7)]

# ================================================================ item table
# āyatana stem -> Hindi (pi-2 ^2-155 / pi-2 termbase), masculine singular
AYATANA = {
    "cakkhāyatana": "आँख का इंद्रिय-क्षेत्र",
    "sotāyatana": "कान का इंद्रिय-क्षेत्र",
    "ghānāyatana": "नाक का इंद्रिय-क्षेत्र",
    "jivhāyatana": "जीभ का इंद्रिय-क्षेत्र",
    "kāyāyatana": "शरीर का इंद्रिय-क्षेत्र",
    "rūpāyatana": "दृश्य रूप का इंद्रिय-क्षेत्र",
    "saddāyatana": "ध्वनि का इंद्रिय-क्षेत्र",
    "gandhāyatana": "गंध का इंद्रिय-क्षेत्र",
    "rasāyatana": "स्वाद का इंद्रिय-क्षेत्र",
    "phoṭṭhabbāyatana": "स्पर्श का इंद्रिय-क्षेत्र",
    "manāyatana": "मन का इंद्रिय-क्षेत्र",
    "dhammāyatana": "मन के विषयों का इंद्रिय-क्षेत्र",
}
AYATANA_OBL = {k: v.replace(" का इंद्रिय-क्षेत्र", " के इंद्रिय-क्षेत्र") for k, v in AYATANA.items()}
AY_ORDER = list(AYATANA)
AYATANA_WORD = "इंद्रिय-क्षेत्र"          # āyatanaṃ / āyatanā (bare, sg. and pl.)
TWELVE = "बारह इंद्रिय-क्षेत्र"            # Dvādasāyatanāni (pi-2 ^2-155)

# bare words of the word-checking pairs (sample choice 2: bare word = bare Hindi)
# Pāli nominative -> (stem, Hindi); all singular
BARE = {
    "cakkhu": ("cakkhāyatana", "आँख"),
    "sotaṃ": ("sotāyatana", "कान"),
    "ghānaṃ": ("ghānāyatana", "नाक"),
    "jivhā": ("jivhāyatana", "जीभ"),
    "kāyo": ("kāyāyatana", "शरीर"),
    "rūpaṃ": ("rūpāyatana", "रूप"),          # wide word-sense, as in the sample
    "saddo": ("saddāyatana", "ध्वनि"),
    "gandho": ("gandhāyatana", "गंध"),
    "raso": ("rasāyatana", "स्वाद"),
    "phoṭṭhabbo": ("phoṭṭhabbāyatana", "स्पर्श"),
    "mano": ("manāyatana", "मन"),
    "dhammo": ("dhammāyatana", "परिघटना"),   # dhamma = परिघटना (core rule)
}
BARE_HI = {k: v[1] for k, v in BARE.items()}
STEM_BARE = {v[0]: k for k, v in BARE.items()}

# beings with / without a base (sa-…-ka / a-…-ka): rendered by desc_hi() below
DESC = {p + s + "ānaṃ" for p in ("sa", "a") for s in ("cakkhuk", "sotak", "ghānak", "rūpak", "cittak")}
# planes: Pāli stem -> Hindi oblique (before में / के प्राणियों में)
PLANE = {
    "kāmāvacar": "इंद्रिय-सुखों के लोक",
    "rūpāvacar": "सूक्ष्म भौतिक लोक",
    "arūpāvacar": "अभौतिक लोक",
    "arūp": "अभौतिक लोक",
    "pañcavokār": "पाँच समूहों वाले अस्तित्व",
    "catuvokār": "चार समूहों वाले अस्तित्व",
    "asaññasatt": "पहचान-रहित प्राणियों के लोक",
    "suddhāvās": "शुद्ध निवास लोक",
}
LOC = {p + "e": p for p in PLANE}            # Kāmāvacare (in the plane)
ACC = {p + "aṃ": p for p in PLANE}           # kāmāvacaraṃ upapajjantānaṃ (reborn into)
ABL = {p + "ā": p for p in PLANE}            # kāmāvacarā cavantānaṃ (passing away from)
GEN = {p + "ānaṃ": p for p in PLANE}         # Kāmāvacarānaṃ (the beings of the plane)
GEN_HI = {p: PLANE[p] + " के प्राणियों में" for p in PLANE}
GEN_HI["asaññasatt"] = "पहचान-रहित प्राणियों में"   # terms file: Asaññasattānaṃ
HEAD = {
    "upapajjantānaṃ": "जन्म लेने वालों में",
    "cavantānaṃ": "मरने वालों में",
    "parinibbantānaṃ": "पूर्ण निर्वाण पाने वालों में",
}
PACCH = "pacchimabhavikānaṃ"
PACCH_HEAD = "अंतिम जन्म वालों में"           # Pacchimabhavikānaṃ (terms file)
PACCH_UPA = "अंतिम जन्म लेने वालों में"        # Pacchimabhavikānaṃ … upapajjantānaṃ
SABBE = "सभी"                                 # Sabbesaṃ (sample)
ITARE = "बाकी"                                # Itaresaṃ + group
ITARE_ALONE = "बाकी सबमें"                    # Itaresaṃ tesaṃ (terms file)
YE_CLAUSE = "जो {P} में जन्म लेकर पूर्ण निर्वाण पाएँगे, उनमें"   # ye … upapajjitvā parinibbāyissanti tesaṃ
YE_TAIL = {"upapajjantānaṃ": " से जन्म लेने वालों में", "cavantānaṃ": " से मरने वालों में"}
AND = "और"
OR = "या"

NATTHI = "ऐसा कोई नहीं है।"                    # Natthi.
NO = "नहीं।"                                   # No. (pi-2)
MULAKA = "{X} पर आधारित"                        # (Cakkhāyatanamūlakaṃ)

SHORT = dict(S.SHORT_ANSWERS)
SHORT["Natthi."] = NATTHI
SHORT["No."] = NO

# ================================================================ headings
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Suddhāyatanavāro": "केवल इंद्रिय-क्षेत्रों का खंड",
    "Suddhāyatanamūlacakkavāro": "केवल इंद्रिय-क्षेत्रों पर आधारित चक्र का खंड",
    "Pariññāvāro": "पूरी तरह समझने का खंड",
    "Paccuppannavāro": "वर्तमान का खंड",
    "Atītavāro": "अतीत का खंड",
    "Anāgatavāro": "भविष्य का खंड",
    "Paccuppannātītavāro": "वर्तमान और अतीत का खंड",
    "Paccuppannānāgatavāro": "वर्तमान और भविष्य का खंड",
    "Atītānāgatavāro": "अतीत और भविष्य का खंड",
})

# ================================================================ helpers
AYW = r"(?:cakkh|sot|ghān|jivh|kāy|rūp|sadd|gandh|ras|phoṭṭhabb|man|dhamm)āyatana"
V = r"(?:na )?[a-zāīū]+"


def ay(tok):
    """'cakkhāyatanaṃ' / 'cakkhāyatanañca' / 'cakkhāyatananti' -> stem."""
    m = re.fullmatch(rf"({AYW})(?:ṃ|ñca|nti|ñceva)?", tok)
    if not m:
        raise KeyError(tok)
    return m.group(1)


def lf(s):
    return s[:1].lower() + s[1:]


def join_list(items, conj=AND):
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + f" {conj} " + items[-1]


def untie(word):
    """remove the quotative -ti: uppajjatīti -> uppajjati, uppajjitthāti -> uppajjittha."""
    if word.endswith("īti"):
        return word[:-3] + "i"
    if word.endswith("āti"):
        return word[:-3] + "ā"
    if word.endswith("ūti"):
        return word[:-3] + "u"
    if word.endswith("nti"):
        return word[:-3] + "ṃ"
    if word.endswith("ti"):
        return word[:-2]
    return word


def untie_verb(word):
    if word in S.VERBS_M or word[1:] in S.VERBS_M or word in PARI:
        return word
    w = untie(word)
    if w.endswith("ā"):          # uppajjitthāti, nuppajjitthāti, parijānitthāti
        return w[:-1] + "a"
    return w


# ---------------------------------------------------------------- who / where
DESC_NOUN = {"cakkhuk": "आँख", "sotak": "कान", "ghānak": "नाक", "rūpak": "भौतिक रूप", "cittak": "मन"}
DESC_WITH = "{N} के साथ"          # sa-…-ka: आँख के साथ / आँख और कान के साथ
DESC_WITHOUT = "बिना {N} के"      # a-…-ka: बिना आँख के / बिना आँख और कान के
DESC_BUT = "{A} पर {B}"           # mixed pair: आँख के साथ पर बिना कान के


def _desc_parts(d):
    m = re.fullmatch(r"(sa|a)(\w+?)ānaṃ", d)
    return m.group(1) == "sa", DESC_NOUN[m.group(2)]


def desc_hi(descs):
    """sacakkhukānaṃ asotakānaṃ … -> one Hindi phrase (Pāli order kept)."""
    parts = [_desc_parts(d) for d in descs]
    if len(parts) == 1 or all(p[0] == parts[0][0] for p in parts):
        nouns = " और ".join(p[1] for p in parts)
        return (DESC_WITH if parts[0][0] else DESC_WITHOUT).format(N=nouns)
    if len(parts) == 2:
        a, b = [(DESC_WITH if p[0] else DESC_WITHOUT).format(N=p[1]) for p in parts]
        return DESC_BUT.format(A=a, B=b)
    raise ValueError("descriptors " + " ".join(descs))


def _plane_list(stems, conj):
    names = []
    for p in stems:
        if PLANE[p] not in names:
            names.append(PLANE[p])
    return f" {conj} ".join(names) + " में"


def _render_group(g):
    if g["head"] is None and not (g["locs"] or g["accs"] or g["abls"] or g["descs"] or g["pacch"]):
        if g["itare"]:
            return ITARE_ALONE
        raise ValueError("empty group")
    if isinstance(g["head"], tuple):
        s = GEN_HI[g["head"][1]]
    elif g["head"] is None:
        if g["accs"] or g["abls"] or g["descs"] or g["pacch"] or g["sabbe"]:
            raise ValueError("group without head")
        s = _plane_list(g["locs"], AND)
    else:
        parts = []
        if g["sabbe"]:
            parts.append(SABBE)
        if g["locs"]:
            parts.append(_plane_list(g["locs"], AND))
        if g["accs"]:
            parts.append(_plane_list(g["accs"], OR))
        if g["abls"]:
            parts.append(_plane_list(g["abls"], AND))
        if g["descs"]:
            parts.append(desc_hi(g["descs"]))
        if g["head"] == "pacch":
            parts.append(PACCH_HEAD)
        elif g["pacch"]:
            if g["head"] != "upapajjantānaṃ":
                raise ValueError("pacch + " + g["head"])
            parts.append(PACCH_UPA)
        else:
            parts.append(HEAD[g["head"]])
        s = " ".join(parts)
    if g["itare"]:
        s = ITARE + " " + s
    return s


def _new():
    return {"itare": False, "sabbe": False, "locs": [], "accs": [], "abls": [],
            "descs": [], "pacch": False, "head": None}


def _groups(tokens):
    out, g = [], _new()
    for i, tok in enumerate(tokens):
        t = lf(tok)
        nxt = lf(tokens[i + 1]) if i + 1 < len(tokens) else None
        if t == "itaresaṃ":
            g["itare"] = True
        elif t == "sabbesaṃ":
            g["sabbe"] = True
        elif t in LOC:
            g["locs"].append(LOC[t])
        elif t in ACC:
            g["accs"].append(ACC[t])
        elif t in ABL:
            g["abls"].append(ABL[t])
        elif t in DESC:
            g["descs"].append(t)
        elif t == PACCH:
            g["pacch"] = True
            if nxt not in ACC and nxt != "upapajjantānaṃ":
                g["head"] = "pacch"
                out.append(g)
                g = _new()
        elif t in HEAD:
            g["head"] = t
            out.append(g)
            g = _new()
        elif t in GEN:
            g["head"] = ("gen", GEN[t])
            out.append(g)
            g = _new()
        else:
            raise KeyError("who-token " + tok)
    if g != _new():
        out.append(g)
    return out


YE_RE = re.compile(r"(?:^|\s)(?:ye ca|Ye) (.+?) upapajjitvā parinibbāyissanti(?: tesaṃ (upapajjantānaṃ|cavantānaṃ))?$")


def who_hi(phrase):
    """Pāli being/place phrase (before tesaṃ / tattha) -> Hindi ending in 'में'."""
    ye = None
    m = YE_RE.search(phrase)
    if m:
        planes = [ACC[lf(t)] for t in m.group(1).split(" ")]
        ye = YE_CLAUSE.format(P=_plane_list(planes, OR)[:-len(" में")])
        if m.group(2):
            ye += YE_TAIL[m.group(2)]
        phrase = phrase[:m.start()].strip()
    items = [_render_group(g) for g in _groups(phrase.split(" "))] if phrase else []
    if ye:
        items.append(ye)
    return join_list(items)


# ---------------------------------------------------------------- pavatti
def tr_pavatti_q(body):
    """'yassa cakkhāyatanaṃ uppajjati tassa sotāyatanaṃ uppajjati?' (quotative removed)."""
    m = re.fullmatch(rf"(yassa|yattha)( vā pana)?( yattha)? ({AYW})ṃ ({V}) (tassa tattha|tassa|tattha) ({AYW})ṃ ({V})\?", body)
    if not m:
        return None
    rel, vp, rel2, x, v1, cor, y, v2 = m.groups()
    rel = rel + (rel2 or "")
    return S.PAVATTI_Q.format(AND=S.VA_PANA if vp else "", REL=S.Q_REL[rel], X=AYATANA[x],
                              V1=S.verb(v1)[0], COR=S.Q_COR[cor], Y=AYATANA[y], V2=S.verb(v2)[0])


_LOCS = "tesaṃ tattha|tasaṃ tattha|tesaṃ|tattha"
LOC1 = dict(S.LOC1)
LOC1["tasaṃ tattha"] = " वहाँ"      # source slip tasaṃ for tesaṃ (3-06)


def tr_pavatti_sentence(s):
    """one answer sentence without its final '.'"""
    m = re.fullmatch(rf"(.+?) ({_LOCS}) ({AYW})ṃ ({V}), no ca ({_LOCS}) ({AYW})ṃ ({V})", s)
    if m:
        who, l1, x, v1, l2, y, v2 = m.groups()
        return S.ANS_BUT.format(WHO=who_hi(who), L1=LOC1[l1], X=AYATANA[x], V1=S.verb(v1)[0],
                                L2=S.LOC2[l2], Y=AYATANA[y], V2=S.verb_flip(v2))
    # source slips tolerated: 'ñca ca' (3-02 ^6-3-62), a missing ca (3-03), a comma (3-03, 3-05)
    m = re.fullmatch(rf"(.+?) ({_LOCS}) ({AYW})(?:ñca(?: ca)?| ca|ṃ) ({V}),? ({AYW})(?:ñca| ca|ṃ) ({V})", s)
    if m:
        who, l1, x, v1, y, v2 = m.groups()
        return S.ANS_BOTH.format(WHO=who_hi(who), L1=LOC1[l1], X=AYATANA[x], V1=S.verb(v1)[0],
                                 Y=AYATANA[y], V2=S.verb(v2)[0])
    return None


# ---------------------------------------------------------------- pariññā
PARI = {   # tense -> (sg pos, sg neg, pl pos, pl neg); relative/correlative
    "parijānāti": ("पूरी तरह समझता है", "पूरी तरह नहीं समझता"),
    "parijānittha": ("पूरी तरह समझा था", "पूरी तरह नहीं समझा था"),
    "parijānissati": ("पूरी तरह समझेगा", "पूरी तरह नहीं समझेगा"),
}
PARI_REL = {"parijānāti": ("जो", "वह"), "parijānittha": ("जिसने", "उसने"),
            "parijānissati": ("जो", "वह")}
PARI_Q = "{AND}{REL} {X} को {V1}, क्या {COR} {Y} को {V2}?"


def tr_pari_q(body):
    m = re.fullmatch(rf"yo( vā pana)? ({AYW})ṃ (na )?(parijān\S+) so ({AYW})ṃ (na )?(parijān\S+)\?", body)
    if not m:
        return None
    vp, x, n1, v1, y, n2, v2 = m.groups()
    return PARI_Q.format(AND=S.VA_PANA if vp else "", REL=PARI_REL[v1][0], X=AYATANA_OBL[x],
                         V1=PARI[v1][1 if n1 else 0], COR=PARI_REL[v2][1], Y=AYATANA_OBL[y],
                         V2=PARI[v2][1 if n2 else 0])


# ---------------------------------------------------------------- paṇṇatti questions
def _term(tok):
    """-> (Hindi, plural?) for a bare word, an āyatana name, āyatanaṃ / āyatanā."""
    if tok in BARE_HI:
        return BARE_HI[tok], False
    if tok == "āyatanaṃ":
        return AYATANA_WORD, False
    if tok == "āyatanā":
        return AYATANA_WORD, True
    return AYATANA[ay(tok)], False


_KNOWN = set(BARE_HI) | {"āyatanaṃ", "āyatanā"} | {s + "ṃ" for s in AYATANA}
_TYPO = {"sotāyananti": "sotāyatanaṃ"}   # source slip (3-01 ^6-3-13)


def _untie_term(w):
    if w in _KNOWN:
        return w
    if w in _TYPO:
        return _TYPO[w]
    for cand in (untie(w), w[:-2], w[:-3] + "u"):
        if cand in _KNOWN:
            return cand
    return w


def tr_pannatti_q(body):
    words = body[:-1].split(" ")
    if words[-1] == "nāyatananti":
        words[-1] = "nāyatanaṃ"
    words[-1] = _untie_term(words[-1])
    split = []
    for w in words:          # nāyatanaṃ / nāyatanā = na āyatanaṃ / na āyatanā
        split += ["na", w[1:]] if w in ("nāyatanaṃ", "nāyatanā") else [w]
    words = split
    if len(words) == 2:
        neg = False
        x, y = words
    elif len(words) == 4 and words[0] == "na" and words[2] == "na":
        neg = True
        x, y = words[1], words[3]
    else:
        return None
    try:
        xh, pl = _term(x)
        yh, _ = _term(y)
    except KeyError:
        return None
    v = "हैं" if pl else "है"
    if neg:
        return S.PANNATTI_Q_PACC.format(X=xh, Y=yh, V=v, P="वे" if pl else "वह")
    return S.PANNATTI_Q_ANU.format(X=xh, Y=yh, V=v)


# ---------------------------------------------------------------- paṇṇatti answers
QA_ANU_1_PL = "{A}, {B} हैं, पर {C} नहीं हैं।"          # A (two items) B, na C.
QA_REST = "{E} {R} {B}, {C} नहीं {V}।"                  # C ṭhapetvā avaseso B, na C. (sample saṅkhārā line)
AVASESA_NA = "{R} {X}, {Y} नहीं हैं।"                   # Avasesā āyatanā na Y.
SPECIAL = {   # the commentarial senses of a bare word (two or three items)
    "Dibbacakkhu paññācakkhu": "दिव्य आँख और प्रज्ञा की आँख",
    "Dibbasotaṃ taṇhāsotaṃ": "दिव्य कान और तृष्णा की धारा",
    "Sīlagandho samādhigandho paññāgandho": "सदाचार की गंध, एकाग्रता की गंध और प्रज्ञा की गंध",
    "Attharaso dhammaraso vimuttiraso": "अर्थ का स्वाद, शिक्षा का स्वाद और मुक्ति का स्वाद",
}


def _var(label, sigla, pali):
    return " " + S._var(label, sigla, pali)


def pannatti_sentences():
    """Pāli sentence (with its final '.') -> Hindi, for the paṇṇatti answers."""
    d = {}
    acc_bare = {"cakkhu": "Cakkhuṃ", "sotaṃ": "Sotaṃ", "ghānaṃ": "Ghānaṃ", "jivhā": "Jivhaṃ",
                "kāyo": "Kāyaṃ", "rūpaṃ": "Rūpaṃ", "saddo": "Saddaṃ", "gandho": "Gandhaṃ",
                "raso": "Rasaṃ", "phoṭṭhabbo": "Phoṭṭhabbaṃ", "mano": "Manaṃ", "dhammo": "Dhammaṃ"}
    ca_bare = {"cakkhu": "Cakkhuñca", "sotaṃ": "Sotañca", "kāyo": "Kāyañca", "rūpaṃ": "Rūpañca",
               "gandho": "Gandhañca", "raso": "Rasañca", "dhammo": "Dhammañca", "mano": "Manañca"}
    for stem in AY_ORDER:
        P = stem[0].upper() + stem[1:]
        bare = STEM_BARE[stem]
        b = BARE_HI[bare]
        c, c_obl = AYATANA[stem], AYATANA_OBL[stem]
        # X āyatanañceva Xāyatanañca. / Avasesā āyatanā na X.
        d[f"{P}ṃ āyatanañceva {stem}ñca."] = S.QA_ANU_2.format(B=AYATANA_WORD, C=c)
        d[f"Avasesā āyatanā na {stem}ṃ."] = AVASESA_NA.format(R=S.AVASESA, X=AYATANA_WORD, Y=c)
        d[f"avasesā āyatanā na {stem}ṃ."] = d[f"Avasesā āyatanā na {stem}ṃ."]
        # C bare ceva C ca.  (rūpañceva / sotañceva / cakkhu ceva / kāyo ceva …)
        for form in (f"{bare} ceva", bare[:-1] + "ñceva" if bare.endswith("ṃ") else None):
            if form:
                d[f"{P}ṃ {form} {stem}ñca."] = S.QA_ANU_2.format(B=b, C=c)
        # C ṭhapetvā avaseso/avasesaṃ B, na C.  /  … avaseso na C, B.
        exc = S.EXCEPT.format(C=c_obl)
        for av in ("avaseso", "avasesaṃ"):
            d[f"{P}ṃ ṭhapetvā {av} {bare}, na {stem}ṃ."] = QA_REST.format(E=exc, R=S.AVASESA, B=b, C=c, V="है")
            d[f"{P}ṃ ṭhapetvā {av} na {stem}ṃ, {bare}."] = S.QA_PACC_1.format(
                A=exc + " " + S.AVASESA, C=c, B=b, V="है")
        # Bañca Cañca ṭhapetvā avasesaṃ na ceva B na ca C.
        if bare in ca_bare:
            d[f"{ca_bare[bare]} {stem}ñca ṭhapetvā avasesaṃ na ceva {bare} na ca {stem}ṃ."] = \
                S.QA_PACC_2.format(B=b, C=c_obl, Bn=b, Cn=c)
        # suddhāyatana paccanīka: Cakkhuṃ ṭhapetvā avasesā āyatanā na cakkhu, āyatanā. …
        d[f"{acc_bare[bare]} ṭhapetvā avasesā āyatanā na {bare}, āyatanā."] = S.QA_PACC_1.format(
            A=S.EXCEPT.format(C=b) + " " + S.AVASESA + " " + AYATANA_WORD, C=b, B=AYATANA_WORD, V="हैं")
        if bare in ca_bare:
            d[f"{ca_bare[bare]} āyatanañca ṭhapetvā avasesā na ceva {bare} na ca āyatanā."] = \
                S.QA_PACC_2.format(B=b, C=AYATANA_WORD, Bn=b, Cn=AYATANA_WORD)
    # commentarial senses
    for pali, hi in SPECIAL.items():
        stem = {"Dibbacakkhu": "cakkhāyatana", "Dibbasotaṃ": "sotāyatana",
                "Sīlagandho": "gandhāyatana", "Attharaso": "rasāyatana"}[pali.split(" ")[0]]
        bare = STEM_BARE[stem]
        d[f"{pali} {bare}, na {stem}ṃ."] = QA_ANU_1_PL.format(A=hi, B=BARE_HI[bare], C=AYATANA[stem])
        d[f"{pali} na {stem}ṃ, {bare}."] = S.QA_PACC_1.format(A=hi, C=AYATANA[stem], B=BARE_HI[bare], V="हैं")
    return d


PSENT = pannatti_sentences()


def _with_var(hi, var):
    """insert a variant bracket after the first 'शेष' of a QA_PACC_2 sentence."""
    i = hi.index(S.AVASESA)
    return hi[:i + len(S.AVASESA)] + var + hi[i + len(S.AVASESA):]


# variant-bearing sentences (spelling-only variants of avasesaṃ)
PSENT["Cakkhuñca cakkhāyatanañca ṭhapetvā avasesaṃ [avasesā (syā. pī.)] na ceva cakkhu na ca cakkhāyatanaṃ."] = _with_var(
    PSENT["Cakkhuñca cakkhāyatanañca ṭhapetvā avasesaṃ na ceva cakkhu na ca cakkhāyatanaṃ."],
    _var(S.VAR_SPELL, "Syā., Pī.", "avasesā"))
PSENT["Kāyañca kāyāyatanañca ṭhapetvā avasesaṃ [avaseso (syā.)] na ceva kāyo na ca kāyāyatanaṃ."] = _with_var(
    PSENT["Kāyañca kāyāyatanañca ṭhapetvā avasesaṃ na ceva kāyo na ca kāyāyatanaṃ."],
    _var(S.VAR_SPELL, "Syā.", "avaseso"))
PSENT["Gandhañca gandhāyatanañca ṭhapetvā avasesaṃ [avasesā (syā.)] na ceva gandho na ca gandhāyatanaṃ."] = _with_var(
    PSENT["Gandhañca gandhāyatanañca ṭhapetvā avasesaṃ na ceva gandho na ca gandhāyatanaṃ."],
    _var(S.VAR_SPELL, "Syā.", "avasesā"))

# ================================================================ closing lines
PSENT.update({
    "Paṇṇattiuddesavāro.": S.FIXED["Paṇṇattiuddesavāro."],
    "Paṇṇattiniddesavāro.": S.FIXED["Paṇṇattiniddesavāro."],
    "Uppādavāro.": "उत्पन्न होने का खंड।",
    "Nirodhavāro.": "समाप्त होने का खंड।",
    "Uppādanirodhavāro.": "उत्पन्न होने और समाप्त होने का खंड।",
    "Pavattivāro niṭṭhito.": "प्रक्रिया का खंड पूरा हुआ।",
    "Pariññāvāro.": "पूरी तरह समझने का खंड।",
    "Āyatanayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Āyatanayamakaṃ"]),
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,
})

# ================================================================ pariññā answers
AGGA = "सर्वोच्च मार्ग से युक्त व्यक्ति"          # Aggamaggasamaṅgī
ARAHA = "अर्हत्"                                 # Arahā
YE_MAGGA = "जो मार्ग प्राप्त करेंगे"              # Ye maggaṃ paṭilabhissanti
PUTHU = "जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे"  # ye ca puthujjanā maggaṃ na paṭilabhissanti
REST = f"{AGGA} और {ARAHA} को छोड़कर शेष व्यक्ति"   # Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā
C_, S_ = AYATANA_OBL["cakkhāyatana"], AYATANA_OBL["sotāyatana"]
PSENT.update({
    "Arahā cakkhāyatanaṃ na parijānāti, no ca sotāyatanaṃ na parijānittha.":
        f"{ARAHA} {C_} को पूरी तरह नहीं समझता, पर उसने {S_} को पूरी तरह समझा था।",
    "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā cakkhāyatanañca na parijānanti sotāyatanañca na parijānittha.":
        f"{REST} {C_} को भी पूरी तरह नहीं समझते और उन्होंने {S_} को भी पूरी तरह नहीं समझा था।",
    "Aggamaggasamaṅgī sotāyatanaṃ na parijānittha, no ca cakkhāyatanaṃ na parijānāti.":
        f"{AGGA} ने {S_} को पूरी तरह नहीं समझा था, पर वह {C_} को पूरी तरह समझता है।",
    "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā sotāyatanañca na parijānittha cakkhāyatanañca na parijānanti.":
        f"{REST} ने {S_} को भी पूरी तरह नहीं समझा था और वे {C_} को भी पूरी तरह नहीं समझते।".replace("व्यक्ति ने", "व्यक्तियों ने"),
    "Ye maggaṃ paṭilabhissanti te cakkhāyatanaṃ na parijānanti, no ca sotāyatanaṃ na parijānissanti.":
        f"{YE_MAGGA}, वे {C_} को पूरी तरह नहीं समझते, पर {S_} को पूरी तरह समझेंगे।",
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te cakkhāyatanañca na parijānanti sotāyatanañca na parijānissanti.":
        f"{ARAHA} और {PUTHU}, वे {C_} को भी पूरी तरह नहीं समझते और {S_} को भी पूरी तरह नहीं समझेंगे।",
    "Aggamaggasamaṅgī sotāyatanaṃ na parijānissati, no ca cakkhāyatanaṃ na parijānāti.":
        f"{AGGA} {S_} को पूरी तरह नहीं समझेगा, पर {C_} को पूरी तरह समझता है।",
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te sotāyatanañca na parijānissanti cakkhāyatanañca na parijānanti.":
        f"{ARAHA} और {PUTHU}, वे {S_} को भी पूरी तरह नहीं समझेंगे और {C_} को भी पूरी तरह नहीं समझते।",
    "Ye maggaṃ paṭilabhissanti te cakkhāyatanaṃ na parijānittha, no ca sotāyatanaṃ na parijānissanti.":
        f"{YE_MAGGA}, उन्होंने {C_} को पूरी तरह नहीं समझा था, पर वे {S_} को पूरी तरह समझेंगे।",
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te cakkhāyatanañca na parijānittha sotāyatanañca na parijānissanti.":
        f"{AGGA} और {PUTHU}, उन्होंने {C_} को भी पूरी तरह नहीं समझा था और वे {S_} को भी पूरी तरह नहीं समझेंगे।",
    "Arahā sotāyatanaṃ na parijānissati, no ca cakkhāyatanaṃ na parijānittha.":
        f"{ARAHA} {S_} को पूरी तरह नहीं समझेगा, पर उसने {C_} को पूरी तरह समझा था।",
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te sotāyatanañca na parijānissanti cakkhāyatanañca na parijānittha.":
        f"{AGGA} और {PUTHU}, वे {S_} को भी पूरी तरह नहीं समझेंगे और उन्होंने {C_} को भी पूरी तरह नहीं समझा था।",
})

# ================================================================ editorial notes (in brackets)
NOTES = {
    "(Cakkaṃ bandhitabbaṃ)": "(चक्र को जोड़ लेना चाहिए)",
    "(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena).":
        "(एक-एक शब्द पर आधारित चक्र को बिना भ्रम के जोड़ लेना चाहिए)।",
    "(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ).":
        "(चक्र जोड़ते समय हर जगह “हाँ” कहना चाहिए)।",
    "(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana vārasaṅkhepo [uparivāre saṅkhepo (syā.), uparivāre saṅkhepaṃ (sī. ka.)] tīti jānitabbaṃ.)":
        f"(जिस स्थान पर {AYATANA['ghānāyatana']} उत्पन्न होता है, वहाँ {AYATANA['manāyatana']} और "
        f"{AYATANA['dhammāyatana']} एक समान हैं, कोई अंतर नहीं है, पर आगे के खंड संक्षेप में हैं "
        "[पाठभेद: uparivāre saṅkhepo (Syā.), uparivāre saṅkhepaṃ (Sī., Ka.)], ऐसा समझना चाहिए।)",
    "(saṃkhittaṃ yassakasadisaṃ [yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)] )":
        "(संक्षेप में, व्यक्ति वाले खंड के समान [पाठभेद: yassakampi sadisaṃ (Sī.), yassekasadisaṃ (Syā.)])",
    "(yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi paccuppannānāgatepi atītānāgatepi sabbattha sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ).":
        "(स्थान वाला खंड वर्तमान में भी, अतीत में भी, भविष्य में भी, वर्तमान और अतीत में भी, वर्तमान और भविष्य में भी, "
        "अतीत और भविष्य में भी, हर जगह समान है, केवल “उत्पन्न होता है”, “उत्पन्न हुआ था” जैसे शब्द अतिरिक्त जोड़ने चाहिए)।",
    "(Saṃkhittaṃ).": "(संक्षेप में)।",
    "(tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti).":
        f"(उसमें {AYATANA['manāyatana']} और {AYATANA['dhammāyatana']} समान हैं, ये दोनों समान ही होते हैं)।",
    "(uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ).":
        "(उत्पन्न होने में भी, समाप्त होने में भी, उत्पन्न होने और समाप्त होने में भी स्थान वाला खंड हर जगह समान है)।",
    "(Yassa yatthakampi sadisaṃ vitthāretabbaṃ).":
        "(व्यक्ति और स्थान वाले खंड का भी इसी प्रकार विस्तार करना चाहिए)।",
    "(yassa yatthakampi yassakasadisaṃ).":
        "(व्यक्ति और स्थान वाला खंड भी व्यक्ति वाले खंड के समान है)।",
    "(Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi [paccaniyampi (sī. syā. ka.)] sadisaṃ.)":
        "(उत्पन्न होने के खंड में भी, समाप्त होने के खंड में भी, उत्पन्न होने और समाप्त होने के खंड में भी अतीत के प्रश्न "
        "सकारात्मक भी और नकारात्मक भी [वर्तनी-भेद (Sī., Syā., Ka.): paccaniyampi] समान हैं।)",
    "(Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi vitthāretabbā).":
        "(जैसे उत्पन्न होने के खंड में व्यक्ति और स्थान वाले भाग में भविष्य के प्रश्नों का विस्तार किया गया है, "
        "वैसे ही समाप्त होने के खंड में भी विस्तार करना चाहिए)।",
    "(yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ).":
        "(जैसे वर्तमान और अतीत वाले खंड में भी तीन प्रकार से विस्तार किया गया है, वैसे ही इसका भी विस्तार करना चाहिए)।",
    "(yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu sadisaṃ).":
        "(स्थान वाले खंड में “नहीं” उत्तर नहीं देना चाहिए, स्थान वाले खंड को बाकी स्थान वाले खंडों के समान बनाना चाहिए, "
        "स्थान वाला खंड तीनों खंडों में समान है)।",
    "(Yassakampi yassayatthakampi sadisaṃ).":
        "(व्यक्ति वाला खंड भी और व्यक्ति और स्थान वाला खंड भी समान हैं)।",
    "(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ).":
        "(अतीत के प्रश्न उत्पन्न होने में भी, समाप्त होने में भी, उत्पन्न होने और समाप्त होने में भी, सकारात्मक भी और "
        "नकारात्मक भी, समान हैं)।",
    "(Yathā uppādavāre paccuppannātītā pucchā vibhattā evaṃ uppādanirodhepi paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā [vibhajitabbaṃ (sī syā. ka.)] ).":
        "(जैसे उत्पन्न होने के खंड में वर्तमान और अतीत के प्रश्नों का विश्लेषण किया गया है, वैसे ही उत्पन्न होने और "
        "समाप्त होने के खंड में भी वर्तमान और अतीत के प्रश्नों का सकारात्मक भी और नकारात्मक भी विश्लेषण करना चाहिए "
        "[वर्तनी-भेद (Sī., Syā., Ka.): vibhajitabbaṃ])।",
    "(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā yassakampi yatthakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ, evaṃ uppādanirodhepi atītānāgatā pucchā vibhajitabbā.)":
        "(जैसे समाप्त होने के खंड में अतीत और भविष्य के [वर्तनी-भेद (Syā.): atītenānāgatā] प्रश्नों का व्यक्ति वाला खंड भी, "
        "स्थान वाला खंड भी, व्यक्ति और स्थान वाला खंड भी, सकारात्मक भी और नकारात्मक भी विश्लेषण किया गया है, वैसे ही "
        "उत्पन्न होने और समाप्त होने के खंड में भी अतीत और भविष्य के प्रश्नों का विश्लेषण करना चाहिए।)",
}

# ================================================================ fixed lines
FIXED = {
    # uddesa: the Pāli lacks the comma after sotāyatanaṃ (source slip, comma supplied)
    "Dvādasāyatanāni – cakkhāyatanaṃ, sotāyatanaṃ ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ.":
        TWELVE + " – " + ", ".join(AYATANA[s] for s in AY_ORDER) + "।",
}


# ================================================================ line translator
def tr_question(body):
    for f in (tr_pavatti_q, tr_pari_q, tr_pannatti_q):
        try:
            r = f(body)
        except KeyError:
            r = None
        if r:
            return r
    return None


def tr_frag_q(u):
    """Token-wise translation of a (possibly truncated) yassa/yattha question or a piece of
    one: relative words, āyatana names, verbs, correlatives.  u may end in '?', '.' or nothing."""
    end = u[-1] if u[-1:] in ("?", ".") else ""
    toks = lf(u[:-1] if end else u).split(" ")
    out = []
    i = 0
    while i < len(toks):
        t = toks[i]
        if t in ("yassa", "yattha") and not out:
            j, vp, rel = i + 1, False, t
            if toks[j:j + 2] == ["vā", "pana"]:
                vp, j = True, j + 2
            if t == "yassa" and toks[j:j + 1] == ["yattha"]:
                rel, j = "yassa yattha", j + 1
            out.append((S.VA_PANA if vp else "") + S.Q_REL[rel])
            i = j
            continue
        if t == "tassa":
            cor = "tassa"
            if toks[i + 1:i + 2] == ["tattha"]:
                cor, i = "tassa tattha", i + 1
            out.append("\x00, क्या " + S.Q_COR[cor])
            i += 1
            continue
        if t == "tattha" and out:
            out.append("\x00, क्या " + S.Q_COR["tattha"])
            i += 1
            continue
        if t == "na" and i + 1 < len(toks):
            out.append(S.verb("na " + untie_verb(toks[i + 1]))[0])
            i += 2
            continue
        try:
            out.append(AYATANA[ay(t)])
        except KeyError:
            out.append(S.verb(untie_verb(t))[0])      # KeyError if unknown
        i += 1
    s = " ".join(out).replace(" \x00", "").replace("\x00", "")
    return s + {"?": "?", ".": "।", "": ""}[end]


def tr_partial_answer(core):
    """pieces of a pavatti answer cut by …pe…: 'who tesaṃ X V, no ca tesaṃ', 'who tesaṃ X',
    'who tesaṃ', 'who'."""
    try:
        m = re.fullmatch(rf"(.+?) ({_LOCS}) ({AYW})ṃ ({V}), no ca ({_LOCS})", core)
        if m:
            who, l1, x, v1, l2 = m.groups()
            return f"{who_hi(who)}{LOC1[l1]} {AYATANA[x]} {S.verb(v1)[0]}, पर {S.LOC2[l2]}"
        m = re.fullmatch(rf"(.+?) ({_LOCS}) ({AYW})ṃ", core)
        if m:
            who, l1, x = m.groups()
            return f"{who_hi(who)}{LOC1[l1]} {AYATANA[x]}"
        m = re.fullmatch(rf"(.+?) ({_LOCS})", core)
        if m:
            who, l1 = m.groups()
            return f"{who_hi(who)}{LOC1[l1]}"
        return who_hi(core)
    except (KeyError, ValueError):
        return None


ACC_BARE = {"cakkhuṃ": "cakkhu", "sotaṃ": "sotaṃ", "ghānaṃ": "ghānaṃ", "jivhaṃ": "jivhā",
            "kāyaṃ": "kāyo", "rūpaṃ": "rūpaṃ", "saddaṃ": "saddo", "gandhaṃ": "gandho",
            "rasaṃ": "raso", "phoṭṭhabbaṃ": "phoṭṭhabbo", "manaṃ": "mano", "dhammaṃ": "dhammo"}


def tr_pannatti_piece(core):
    """pieces of a paṇṇatti line cut by …pe…"""
    l = lf(core)
    if l in BARE_HI:                                     # ghānaṃ… jivhā… kāyo…
        return BARE_HI[l]
    m = re.fullmatch(r"(\S+) ṭhapetvā", l)                # Sotaṃ ṭhapetvā…
    if m and m.group(1) in ACC_BARE:
        return S.EXCEPT.format(C=BARE_HI[ACC_BARE[m.group(1)]])
    if l == "na ca āyatanā":                             # … na ca āyatanā.
        return "न " + AYATANA_WORD
    m = re.fullmatch(rf"na ({AYW})ṃ", l)                  # … na cakkhāyatanaṃ (= avasesā āyatanā na …)
    if m:
        return f"{AYATANA[m.group(1)]} नहीं हैं"
    return None


def _tr_unit(u):
    if u in ("?", "."):
        return {"?": "?", ".": "।"}[u]
    end = u[-1] if u[-1] in "?." else ""
    if u in SHORT:
        return SHORT[u]
    if u in PSENT:
        return PSENT[u]
    if not end:
        for e in (".", "?"):
            if u + e in SHORT:
                return SHORT[u + e][:-1]
            if u + e in PSENT:
                return PSENT[u + e][:-1]
    lw = lf(u)
    if end in ("?", ""):
        words = (lw[:-1] if end else lw).split(" ")
        if words[0] in ("yassa", "yattha", "yo"):
            words[-1] = untie_verb(words[-1])
        q = tr_question(" ".join(words) + "?")
        if q:
            return q if end else q[:-1]
    if end in (".", ""):
        try:
            r = tr_pavatti_sentence(u[:-1] if end else u)
        except KeyError:
            r = None
        if r:
            return r if end else r[:-1]
    core = u[:-1] if end == "." else u
    if end != "?":
        r = tr_partial_answer(core) or tr_pannatti_piece(core)
        if r:
            return r + ("।" if end == "." else "")
    try:
        return tr_frag_q(u)
    except KeyError:
        pass
    raise ValueError("untranslated: " + u)


def tr_unit(u):
    lab = ""
    m = re.match(r"^(\((?:Ka|Kha|Ga|Gha)\)) (.*)$", u)
    if m:
        lab, u = S.LABELS[m.group(1)] + " ", m.group(2)
    return lab + _tr_unit(u)


def tr_text(text):
    """split at …pe… / … and at sentence ends, translate each unit, keep the spacing."""
    prot = re.sub(r"\[[^\]]*\]", lambda m: m.group(0).replace(". ", ".\x01"), text)
    parts = re.split(r"(…[Pp]e…|…)", prot)
    out = []
    for k, part in enumerate(parts):
        if k % 2:
            out.append("…")
            continue
        subs = re.split(r"(?<=[?.])(\s+)(?=\S)", part)
        for j, sp in enumerate(subs):
            if j % 2:
                out.append(sp)
                continue
            lead = sp[:len(sp) - len(sp.lstrip())]
            trail = sp[len(sp.rstrip()):]
            core = sp.strip().replace(".\x01", ". ")
            out.append(lead + (tr_unit(core) if core else "") + trail)
    return "".join(out)


NORMALIZE = [   # source slips, translated as meant (reported)
    ("uppajjittharūpāyatanañca", "uppajjittha rūpāyatanañca"),     # 3-01 ^6-3-43
    ("parinibbāntānaṃ", "parinibbantānaṃ"),                       # 3-05 ^6-3-172
    ("ghānāyatanaṃ upapajjissati", "ghānāyatanaṃ uppajjissati"),  # 3-06 ^6-3-232
    ("yassa =93 yattha", "yassa yattha"),                         # 3-03 ^6-3-118
    ("na nirujjhatī ti", "na nirujjhatīti"),                      # 3-04 ^6-3-131
]


def tr_body(text):
    if text in FIXED:
        return FIXED[text]
    for a, b in NORMALIZE:
        text = text.replace(a, b)
    for key in sorted(NOTES, key=len, reverse=True):
        if key in text:
            before, after = text.split(key, 1)
            hb = tr_body(before.rstrip()) if before.strip() else ""
            sep = before[len(before.rstrip()):]
            return hb + sep + NOTES[key] + (tr_text(after) if after else "")
    tail = ""
    m = re.search(r" \(([A-ZĀ][a-zāīūṃñṭḍṅṇḷ]*āyatana)mūlakaṃ\)(\.?)$", text)
    if m:
        stem = lf(m.group(1))
        tail = " (" + MULAKA.format(X=AYATANA_OBL[stem]) + ")" + ("।" if m.group(2) else "")
        text = text[:m.start()]
    return tr_text(text) + tail


# 3-04 ^6-3-142: two answer sentences joined by a comma in the Pāli (source slip; comma kept)
_A = "Rūpāvacarānaṃ arūpāvacarānaṃ tesaṃ tattha ghānāyatanaṃ na nirujjhissati, no ca tesaṃ tattha manāyatanaṃ na nirujjhissati"
_B = "parinibbantānaṃ asaññasattānaṃ tesaṃ tattha ghānāyatanañca na nirujjhissati manāyatanañca na nirujjhissati"
FIXED[f"{_A}, {_B}."] = tr_pavatti_sentence(_A)[:-1] + ", " + tr_pavatti_sentence(_B)


def tr_line(line):
    if not line.strip():
        return ""
    m = S.ID_RE.search(line)
    bid = m.group(1) if m else None
    text = S.ID_RE.sub("", line) if m else line
    if text.startswith("#"):
        level = len(text) - len(text.lstrip("#"))
        h = text[level:].strip()
        if h not in HEADINGS:
            raise ValueError("untranslated heading: " + h)
        out = "#" * level + " " + HEADINGS[h]
    else:
        out = tr_body(text)
    return out + (" " + bid if bid else "")


def main():
    check = "--check" in sys.argv
    bad = 0
    for fname in FILES:
        src = (S.PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
        out = []
        for i, line in enumerate(src, 1):
            try:
                out.append(tr_line(line))
            except (ValueError, KeyError) as e:
                bad += 1
                out.append("")
                if check:
                    print(f"{fname}:{i}: {e}")
        if not check:
            (S.HI_DIR / fname).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
            print(fname, len([l for l in src if l.strip()]), "lines")
    if bad:
        print("UNTRANSLATED:", bad)
        if not check:
            sys.exit(1)


if __name__ == "__main__":
    main()
