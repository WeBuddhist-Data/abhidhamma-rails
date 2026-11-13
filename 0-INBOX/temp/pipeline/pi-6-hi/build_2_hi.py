r"""pi-6 Yamaka, Hindi plain zero-shot: Khandhayamaka (2-01, 2-02) builder + shared engine.

usage: python -I -X utf8 build_2_hi.py
Writes AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\2-01-khandhayamaka.md and 2-02-….
Every line is composed from fixed frames (imported from build_sample_hi, plus the frames below);
an unknown line raises an error. build_4_hi.py imports this module for the Dhātuyamaka.
"""
import pathlib
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi"
sys.path.insert(0, HERE)
import build_sample_hi as S  # noqa: E402  (import only)

PALI_DIR, HI_DIR, ID_RE = S.PALI_DIR, S.HI_DIR, S.ID_RE

# ---------------------------------------------------------------- headings
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Uppādanirodhavāro": "उत्पन्न होने और समाप्त होने का खंड",
    "Pariññāvāro": "पूरी तरह समझने का खंड",
    "Paccuppannavāro": "वर्तमान का खंड",
    "Atītavāro": "अतीत का खंड",
    "Anāgatavāro": "भविष्य का खंड",
    "Paccuppannātītavāro": "वर्तमान और अतीत का खंड",
    "Paccuppannānāgatavāro": "वर्तमान और भविष्य का खंड",
    "Atītānāgatavāro": "अतीत और भविष्य का खंड",
    "Suddhadhātuvāro": "केवल तत्वों का खंड",
    "Suddhadhātumūlacakkavāro": "केवल तत्वों पर आधारित चक्र का खंड",
})

# ---------------------------------------------------------------- items (paṇṇattivāra)
# Pāli nominative -> (Hindi, plural?)
ITEMS = {k: (v, False) for k, v in S.KHANDHA.items()}
ITEMS.update(S.BARE)
ITEMS.update({"khandho": ("समूह", False), "khandhā": ("समूह", True)})
# oblique (before को / और … को)
OBL = dict(S.KHANDHA_OBL)
OBL.update(S.BARE_OBL)
OBL.update({"khandho": "समूह", "khandhā": "समूहों"})

# typos in the source, read as the intended word (reported)
ITEM_FIX = {"vadanākkhandho": "vedanākkhandho"}

AMANTA = S.AMANTA
SHORT = dict(S.SHORT_ANSWERS)
SHORT.update({
    "No.": "नहीं।",                       # No.
    "Natthi.": "ऐसा कोई नहीं है।",          # Natthi. (no such case)
})

QA_ANU_1_PL = "{A}, {B} हैं, पर {C} नहीं हैं।"        # A (plural) B, na C.
AVASESA_NOT = "शेष {X}{VAR}, {C} नहीं हैं।"           # Avasesā khandhā na C.
EXCEPT_REST = "{E} शेष {B}{VAR}, {C} नहीं {V}।"       # C ṭhapetvā avasesā B, na C.

# variant brackets: exact Pāli bracket -> Hindi bracket
VARIANTS = {
    "[avasesā khandhā khandhā (syā.) evamuparipi]":
        "[" + S.VAR_READ + " (Syā.): avasesā khandhā khandhā, आगे भी इसी तरह]",
    "[pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ (sī. syā.)]":
        "[" + S.VAR_READ + " (Sī., Syā.): pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ]",
    "[avasesā saṅkhārā saṅkhārā (syā.)]":
        "[" + S.VAR_READ + " (Syā.): avasesā saṅkhārā saṅkhārā]",
}


def var_hi(br):
    if not br:
        return ""
    br = br.strip()
    if br not in VARIANTS:
        raise ValueError("unknown variant " + br)
    return " " + VARIANTS[br]


def lc(w):
    return w[:1].lower() + w[1:]


def item(w):
    w = lc(w)
    w = ITEM_FIX.get(w, w)
    if w not in ITEMS:
        raise KeyError(w)
    return w


# ---------------------------------------------------------------- verbs
VERBS = dict(S.VERBS_M)
VERB_FIX = {"nirujjhattha": "nirujjhittha"}   # source slip at ^6-2-111


def vb(tok):
    t = tok
    for a, b in VERB_FIX.items():
        t = t.replace(a, b)
    return S.verb(t, VERBS)


def vb_flip(tok):
    t = tok
    for a, b in VERB_FIX.items():
        t = t.replace(a, b)
    return S.verb_flip(t, VERBS)


def untie(w, known):
    if w.endswith("ūti"):
        cands = [w[:-3] + "u", w[:-2]]
    elif w.endswith("īti"):
        cands = [w[:-3] + "i"]
    elif w.endswith("nti"):
        cands = [w[:-3] + "ṃ"]
    elif w.endswith("āti"):
        cands = [w[:-2], w[:-3] + "a"]
    elif w.endswith("ti"):
        cands = [w[:-2]]
    else:
        cands = []
    for c in cands:
        if c in known or ITEM_FIX.get(c, "") in known:
            return c
    return w


# ---------------------------------------------------------------- paṇṇattivāra questions
def q_pannatti(body):
    """'rūpaṃ rūpakkhandho' / 'na khandhā na vedanā' (no '?', quotative already removed)."""
    m = re.fullmatch(r"(na )?(\S+) (na )?(\S+)", body)
    if not m:
        return None
    n1, x, n2, y = m.groups()
    if bool(n1) != bool(n2):
        return None
    try:
        x, y = item(x), item(y)
    except KeyError:
        return None
    xh, pl = ITEMS[x]
    yh = ITEMS[y][0]
    v = "हैं" if pl else "है"
    if n1:
        return S.PANNATTI_Q_PACC.format(X=xh, Y=yh, V=v, P="वे" if pl else "वह")[:-1]
    return S.PANNATTI_Q_ANU.format(X=xh, Y=yh, V=v)[:-1]


# ---------------------------------------------------------------- pavattivāra
ITEM_ALT = None   # set by set_items()
_V = r"(?:na )?[^\s,]+"
_LOC = "tesaṃ tattha|tesaṃ|tattha"


def set_items():
    global ITEM_ALT
    keys = sorted(set(ITEMS) | set(ITEM_FIX), key=len, reverse=True)
    ITEM_ALT = "|".join(re.escape(k) for k in keys)


set_items()


def q_pavatti(body):
    m = re.fullmatch(rf"(yassa|yattha)( vā pana)?( yattha)? ({ITEM_ALT}) ({_V}) (tassa tattha|tassa|tattha) ({ITEM_ALT}) ({_V})", body)
    if not m:
        return None
    rel, vp, rel2, x, v1, cor, y, v2 = m.groups()
    rel = rel + (rel2 or "")
    return S.PAVATTI_Q.format(AND=S.VA_PANA if vp else "", REL=S.Q_REL[rel], X=ITEMS[item(x)][0],
                              V1=vb(v1)[0], COR=S.Q_COR[cor], Y=ITEMS[item(y)][0], V2=vb(v2)[0])[:-1]


# places: Pāli stem -> Hindi
PLACE = {
    "asaññasatta": "पहचान-रहित प्राणियों के लोक",
    "pañcavokāra": "पाँच समूहों वाले अस्तित्व",
    "catuvokāra pañcavokāra": "चार या पाँच समूहों वाले अस्तित्व",
    "arūpa": "अभौतिक लोक",
    "suddhāvāsa": "शुद्ध निवास लोक",
}


def _case(stem, end):
    """'catuvokāra pañcavokāra' + 'ṃ' -> 'catuvokāraṃ pañcavokāraṃ'."""
    return " ".join(w + end for w in stem.split(" "))


ATOMS = {
    "sabbesaṃ cavantānaṃ": "सभी मरने वालों में",
    "sabbesaṃ upapajjantānaṃ": "सभी जन्म लेने वालों में",
    "parinibbantānaṃ": "पूर्ण निर्वाण पाने वालों में",
    "pacchimabhavikānaṃ": "अंतिम जन्म वालों में",
    "pacchimabhavikānaṃ upapajjantānaṃ": "अंतिम जन्म लेने वालों में",
    "ye arūpaṃ upapajjitvā parinibbāyissanti":
        "जो अभौतिक लोक में जन्म लेकर पूर्ण निर्वाण पाएँगे, उनमें",
    "ye ca arūpaṃ upapajjitvā parinibbāyissanti":
        "जो अभौतिक लोक में जन्म लेकर पूर्ण निर्वाण पाएँगे, उनमें",
    "ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ":
        "जो अभौतिक लोक में जन्म लेकर पूर्ण निर्वाण पाएँगे, उनमें से मरने वालों में",
}
for _st, _p in PLACE.items():
    _ws = _st.split(" ")                        # every stem ends in -a
    _acc = " ".join(w + "ṃ" for w in _ws)       # asaññasattaṃ
    _abl = " ".join(w[:-1] + "ā" for w in _ws)  # asaññasattā
    _loc = " ".join(w[:-1] + "e" for w in _ws)  # asaññasatte
    _gen = " ".join(w[:-1] + "ānaṃ" for w in _ws)  # asaññasattānaṃ
    ATOMS[_acc + " upapajjantānaṃ"] = f"{_p} में जन्म लेने वालों में"
    ATOMS["pacchimabhavikānaṃ " + _acc + " upapajjantānaṃ"] = f"{_p} में अंतिम जन्म लेने वालों में"
    ATOMS[_abl + " cavantānaṃ"] = f"{_p} से मरने वालों में"
    ATOMS[_loc + " parinibbantānaṃ"] = f"{_p} में पूर्ण निर्वाण पाने वालों में"
    ATOMS[_loc + " pacchimabhavikānaṃ"] = f"{_p} में अंतिम जन्म वालों में"
    ATOMS[_gen] = "पहचान-रहित प्राणियों में" if _st == "asaññasatta" else f"{_p} के प्राणियों में"

# beings by sense organ (Dhātu/Āyatana): sacakkhuka / acakkhuka …
SENSE = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर",
         "rūpa": "भौतिक रूप", "citta": "मन"}


def _sense_adj(w):
    m = re.fullmatch(r"(sa|a)(\S+?)kānaṃ", w)
    if not m or m.group(2) not in SENSE:
        return None
    return m.group(1), SENSE[m.group(2)]


def _sense_atom(words, i):
    """sacakkhukānaṃ asotakānaṃ upapajjantānaṃ -> (Hindi, next index)."""
    adjs = []
    j = i
    while j < len(words) and _sense_adj(words[j]):
        adjs.append(_sense_adj(words[j]))
        j += 1
    if not adjs or j >= len(words) or words[j] != "upapajjantānaṃ":
        return None
    if len(adjs) == 1:
        (p, s), = adjs
        d = f"{s} वाले" if p == "sa" else f"{s}-रहित"
    elif len(adjs) == 2:
        (p1, s1), (p2, s2) = adjs
        if p1 == "sa" and p2 == "sa":
            d = f"{s1} और {s2} वाले"
        elif p1 == "sa" and p2 == "a":
            d = f"{s1} वाले लेकिन {s2}-रहित"
        else:
            return None
    else:
        return None
    return d + " जन्म लेने वालों में", j + 1


def join_hi(parts):
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + " और " + parts[-1]


def who(s):
    """Genitive-plural being phrase (before tesaṃ) -> Hindi ending in 'में'."""
    words = lc(s).split(" ")
    itare = False
    if words[0] == "itaresaṃ":
        itare, words = True, words[1:]
        if not words:
            return "बाकी सबमें"
    out, i = [], 0
    keys = sorted(ATOMS, key=lambda k: len(k.split(" ")), reverse=True)
    while i < len(words):
        for k in keys:
            kw = k.split(" ")
            if words[i:i + len(kw)] == kw:
                out.append(ATOMS[k])
                i += len(kw)
                break
        else:
            r = _sense_atom(words, i)
            if not r:
                raise KeyError("who: " + " ".join(words[i:]))
            out.append(r[0])
            i = r[1]
    h = join_hi(out)
    return ("बाकी " + h) if itare else h


def a_pavatti(s):
    """One answer sentence without its final '.'."""
    var = ""
    m = re.search(r" (\[[^\]]+\])", s)
    if m:
        var = var_hi(m.group(1))
        s = s.replace(" " + m.group(1), "")
    m = re.fullmatch(rf"(.+?) ({_LOC}) ({ITEM_ALT}) ({_V}), no ca ({_LOC}) ({ITEM_ALT}) ({_V})", s)
    if m:
        w, l1, x, v1, l2, y, v2 = m.groups()
        wh = S.WHERE.get(w) or who(w)
        return S.ANS_BUT.format(WHO=wh + var, L1=S.LOC1[l1], X=ITEMS[item(x)][0], V1=vb(v1)[0],
                                L2=S.LOC2[l2], Y=ITEMS[item(y)][0], V2=vb_flip(v2))
    m = re.fullmatch(rf"(.+?) ({_LOC}) ({ITEM_ALT})( ca)? ({_V}),? ({ITEM_ALT})( ca)? ({_V})", s)
    if m:
        w, l1, x, c1, v1, y, c2, v2 = m.groups()
        wh = S.WHERE.get(w) or who(w)
        xh, yh = ITEMS[item(x)][0], ITEMS[item(y)][0]
        if c1 and c2:
            return S.ANS_BOTH.format(WHO=wh + var, L1=S.LOC1[l1], X=xh, V1=vb(v1)[0], Y=yh, V2=vb(v2)[0])
        # one 'ca' missing in the source: the missing «भी» is dropped too
        x2 = xh + (" भी" if c1 else "")
        y2 = yh + (" भी" if c2 else "")
        return f"{wh}{var}{S.LOC1[l1]} {x2} {vb(v1)[0]} और {y2} {vb(v2)[0]}।"
    return None


# ---------------------------------------------------------------- pariññāvāra
PARI = {  # verb -> (positive, negative, relative, correlative)
    "parijānāti": ("पूरी तरह समझता है", "पूरी तरह नहीं समझता", "जो", "वह"),
    "parijānittha": ("पूरी तरह समझा था", "पूरी तरह नहीं समझा था", "जिसने", "उसने"),
    "parijānissati": ("पूरी तरह समझेगा", "पूरी तरह नहीं समझेगा", "जो", "वह"),
}
PARI_PL = {
    "parijānanti": ("पूरी तरह समझते हैं", "पूरी तरह नहीं समझते"),
    "parijānittha": ("पूरी तरह समझा था", "पूरी तरह नहीं समझा था"),
    "parijānissanti": ("पूरी तरह समझेंगे", "पूरी तरह नहीं समझेंगे"),
}
ACC = {}   # accusative object -> Hindi with को


def set_acc():
    for k in list(ITEMS):
        if k.endswith("khandho"):
            ACC[k[:-1] + "aṃ"] = OBL[k] + " को"


set_acc()


def q_parinna(body):
    m = re.fullmatch(r"yo( vā pana)? (\S+) (na )?(\S+) so (\S+) (na )?(\S+)", body)
    if not m:
        return None
    vp, x, n1, v1, y, n2, v2 = m.groups()
    if x not in ACC or y not in ACC or v1 not in PARI or v2 not in PARI:
        return None
    a, b = PARI[v1], PARI[v2]
    return (("और " if vp else "") + f"{a[2]} {ACC[x]} {a[1 if n1 else 0]}, क्या {b[3]} {ACC[y]} {b[1 if n2 else 0]}")


# ---------------------------------------------------------------- generic line handling
QUESTIONS = [q_pannatti, q_pavatti, q_parinna]
KNOWN = set(ITEMS) | set(ITEM_FIX) | set(VERBS) | {"n" + v for v in VERBS} | set(PARI)


def question(q):
    """Pāli question without label and without '?' -> Hindi without '?'."""
    words = q.split(" ")
    if words[-1].endswith("ti") and words[-1] not in KNOWN:
        words[-1] = untie(words[-1], KNOWN)
    q2 = " ".join(words)
    for f in QUESTIONS:
        try:
            r = f(q2)
        except KeyError:
            r = None
        if r:
            return r
    return None


ANSWERS = []      # functions: sentence (without final '.') -> Hindi or None
FIXED = dict(S.FIXED)


def answer(text):
    if text in FIXED:
        return FIXED[text]
    if text in SHORT:
        return SHORT[text]
    tail = ""
    if text.endswith("…pe…."):
        text, tail = text[:-len("…pe….")] + ".", "…"
    sents = re.split(r"(?<=\.) (?=[A-ZĀĪŪṬḌṆÑṄ(])", text)
    outs = []
    for s in sents:
        if s in FIXED:
            outs.append(FIXED[s])
            continue
        if s in SHORT:
            outs.append(SHORT[s])
            continue
        if not s.endswith("."):
            return None
        r = None
        for f in ANSWERS:
            try:
                r = f(s[:-1])
            except KeyError:
                r = None
            if r:
                break
        if not r:
            return None
        outs.append(r)
    out = " ".join(outs)
    if tail:
        out = out[:-1] + tail + "।"
    return out


def tr_body(text):
    if text in FIXED:
        return FIXED[text]
    m = re.match(r"^(\((?:Ka|Kha|Ga|Gha|Ṅa|Ca)\)) (.*)$", text)
    if m:
        label, rest = m.groups()
        # source slip ^6-2-36: "…khandhoti. Āmantā." (question ends with '.')
        rest = re.sub(r"ti\. (Āmantā\.)$", r"ti? \1", rest)
        if "? " in rest:
            q, ans = rest.split("? ", 1)
        elif rest.endswith("?"):
            q, ans = rest[:-1], None
        else:
            raise ValueError("no question mark: " + text)
        hq = question(q)
        if hq is None:
            raise ValueError("untranslated question: " + text)
        out = S.LABELS[label] + " " + hq + "?"
        if ans:
            ha = answer(ans)
            if ha is None:
                raise ValueError("untranslated answer: " + text)
            out += " " + ha
        return out
    r = answer(text)
    if r is None:
        raise ValueError("untranslated line: " + text)
    return r


def tr_line(line, body=None):
    body = body or tr_body
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
        out = body(text)
    return out + (" " + bid if bid else "")


# ---------------------------------------------------------------- paṇṇattivāra answers
SPECIAL_A = {   # A of "A B, na C" -> (Hindi, plural?)
    "Piyarūpaṃ sātarūpaṃ": (S.PIYARUPAM_SATARUPAM, False),
    "Diṭṭhisaññā": (S.DITTHISANNA, False),
}
B_OVERRIDE = {}  # A -> Hindi for B (pun on a word)


def a_pannatti(s):
    # C B ceva C ca
    m = re.fullmatch(r"(\S+) (\S+?)(ñceva| ceva) (\S+) ca", s)
    if m:
        c1, b, j, c2 = m.groups()
        if lc(c1) == c2:
            b = b + "ṃ" if j == "ñceva" else b
            return S.QA_ANU_2.format(B=ITEMS[item(b)][0], C=ITEMS[item(c2)][0])
    # Avasesā khandhā [var] na C
    m = re.fullmatch(r"Avasesā (\S+)( \[[^\]]+\])? na (\S+)", s)
    if m:
        x, br, c = m.groups()
        return AVASESA_NOT.format(X=ITEMS[item(x)][0], VAR=var_hi(br), C=ITEMS[item(c)][0])
    # A B, na C  (special A)
    for a, (ah, pl) in SPECIAL_A.items():
        m = re.fullmatch(re.escape(a) + r" (\S+), na (\S+)", s)
        if m:
            b, c = m.groups()
            bh = B_OVERRIDE.get(a, ITEMS[item(b)][0])
            fr = QA_ANU_1_PL if pl else S.QA_ANU_1
            return fr.format(A=ah, B=bh, C=ITEMS[item(c)][0])
        m = re.fullmatch(re.escape(a) + r" na (\S+), (\S+)", s)
        if m:
            c, b = m.groups()
            bh = B_OVERRIDE.get(a, ITEMS[item(b)][0])
            return S.QA_PACC_1.format(A=ah, C=ITEMS[item(c)][0], B=bh, V="हैं" if pl else "है")
    # Bañca Cañca ṭhapetvā avasesā [var] na ceva B na ca C
    m = re.fullmatch(r"(.+) ṭhapetvā (avasesā|avaseso|avasesaṃ)( \[[^\]]+\])? na ceva (\S+) na ca (\S+)", s)
    if m:
        _, _, br, b, c = m.groups()
        b, c = item(b), item(c)
        txt = S.QA_PACC_2.format(B=OBL[b], C=OBL[c], Bn=ITEMS[b][0], Cn=ITEMS[c][0])
        if br:
            txt = txt.replace(" शेष ", " शेष" + var_hi(br) + " ", 1)
        return txt
    # E ṭhapetvā avasesā na C, B   (E = C or a bare word)
    m = re.fullmatch(r"(\S+) ṭhapetvā (avasesā|avaseso|avasesaṃ)( \S+)? na (\S+), (\S+)", s)
    if m:
        e, _, x, c, b = m.groups()
        c, b = item(c), item(b)
        ex = EXCEPT_OF(e)
        a = ex + " " + S.AVASESA + ((" " + ITEMS[item(x.strip())][0]) if x else "")
        return S.QA_PACC_1.format(A=a, C=ITEMS[c][0], B=ITEMS[b][0], V="हैं" if (ITEMS[b][1] or x) else "है")
    # E ṭhapetvā avasesā B [var], na C   /  E ṭhapetvā avasesā dhātū na C
    m = re.fullmatch(r"(\S+) ṭhapetvā (avasesā|avaseso|avasesaṃ) ([^\s,]+)( \[[^\]]+\])?,? na (\S+)", s)
    if m:
        e, _, b, br, c = m.groups()
        b, c = item(b), item(c)
        return EXCEPT_REST.format(E=EXCEPT_OF(e), B=ITEMS[b][0], VAR=var_hi(br), C=ITEMS[c][0],
                                  V="हैं" if ITEMS[b][1] else "है")
    return None


ACC_TO_ITEM = {}   # accusative after ṭhapetvā -> item


def EXCEPT_OF(acc):
    a = lc(acc)
    if a in ACC_TO_ITEM:
        k = ACC_TO_ITEM[a]
    else:
        k = None
        for cand in (a[:-2] + "o", a[:-2] + "ā", a, a[:-1]):
            if cand in ITEMS:
                k = cand
                break
        if k is None:
            raise KeyError("except " + acc)
    return S.EXCEPT.format(C=OBL[k])


ANSWERS.extend([a_pannatti, a_pavatti])

# ---------------------------------------------------------------- Khandha fixed lines
KH = S.KHANDHA
KO = {k[:-1] + "aṃ": S.KHANDHA_OBL[k] + " को" for k in KH}
ARAHA = "अर्हत्"
AGGA = "सर्वोच्च मार्ग से युक्त व्यक्ति"            # Aggamaggasamaṅgī
AGGA_ARAHA_EXCEPT = f"{AGGA} और {ARAHA} को छोड़कर शेष व्यक्ति"   # Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā
WILL_GAIN = "जो मार्ग प्राप्त करेंगे, वे"            # Ye maggaṃ paṭilabhissanti te
WILL_GAIN_PAST = "जो मार्ग प्राप्त करेंगे, उन्होंने"
PUTHU = "वे साधारण व्यक्ति जो मार्ग प्राप्त नहीं करेंगे"  # ye ca puthujjanā maggaṃ na paṭilabhissanti
R, V = KO["rūpakkhandhaṃ"], KO["vedanākkhandhaṃ"]

FIXED.update({
    "Uppādavāro niṭṭhito.": "उत्पन्न होने का खंड पूरा हुआ।",
    "Nirodhavāro.": "समाप्त होने का खंड।",
    "Uppādanirodhavāro.": "उत्पन्न होने और समाप्त होने का खंड।",
    "Pavattivāro niṭṭhito.": "प्रक्रिया का खंड पूरा हुआ।",
    "Pariññāvāro.": "पूरी तरह समझने का खंड।",
    "Khandhayamakapāḷi niṭṭhitā.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Khandhayamakaṃ"]),
    "(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ).":
        "(जैसे उत्पन्न होने के खंड में वर्तमान और अतीत का विभाजन किया गया है, वैसे ही यहाँ विभाजन करना चाहिए)।",
    # pariññāvāra answers
    "Arahā rūpakkhandhaṃ na parijānāti, no ca vedanākkhandhaṃ na parijānittha.":
        f"{ARAHA} {R} पूरी तरह नहीं समझता, पर उसने {V} पूरी तरह समझा था।",
    "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānittha.":
        f"{AGGA_ARAHA_EXCEPT} {R} भी पूरी तरह नहीं समझते और उन्होंने {V} भी पूरी तरह नहीं समझा था।",
    "Aggamaggasamaṅgī vedanākkhandhaṃ na parijānittha, no ca rūpakkhandhaṃ na parijānāti.":
        f"{AGGA} ने {V} पूरी तरह नहीं समझा था, पर वह {R} पूरी तरह समझता है।",
    "Ye maggaṃ paṭilabhissanti te rūpakkhandhaṃ na parijānanti, no ca vedanākkhandhaṃ na parijānissanti.":
        f"{WILL_GAIN} {R} पूरी तरह नहीं समझते, पर वे {V} पूरी तरह समझेंगे।",
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānissanti.":
        f"{ARAHA} और {PUTHU}, {R} भी पूरी तरह नहीं समझते और {V} भी पूरी तरह नहीं समझेंगे।",
    "Aggamaggasamaṅgī vedanākkhandhaṃ na parijānissati, no ca rūpakkhandhaṃ na parijānāti.":
        f"{AGGA} {V} पूरी तरह नहीं समझेगा, पर वह {R} पूरी तरह समझता है।",
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te vedanākkhandhañca na parijānissanti rūpakkhandhañca na parijānanti.":
        f"{ARAHA} और {PUTHU}, {V} भी पूरी तरह नहीं समझेंगे और {R} भी पूरी तरह नहीं समझते।",
    "Ye maggaṃ paṭilabhissanti te rūpakkhandhaṃ na parijānittha, no ca vedanākkhandhaṃ na parijānissanti.":
        f"{WILL_GAIN_PAST} {R} पूरी तरह नहीं समझा था, पर वे {V} पूरी तरह समझेंगे।",
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te rūpakkhandhañca na parijānittha vedanākkhandhañca na parijānissanti.":
        f"{AGGA} और {PUTHU}, उन्होंने {R} भी पूरी तरह नहीं समझा था और वे {V} भी पूरी तरह नहीं समझेंगे।",
    "Arahā vedanākkhandhaṃ na parijānissati, no ca rūpakkhandhaṃ na parijānittha.":
        f"{ARAHA} {V} पूरी तरह नहीं समझेगा, पर उसने {R} पूरी तरह समझा था।",
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te vedanākkhandhañca na parijānissanti rūpakkhandhañca na parijānittha.":
        f"{AGGA} और {PUTHU}, {V} भी पूरी तरह नहीं समझेंगे और उन्होंने {R} भी पूरी तरह नहीं समझा था।",
})
# the agent for the past tense needs ने: «शेष व्यक्तियों ने»
FIXED["Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā vedanākkhandhañca na parijānittha rūpakkhandhañca na parijānanti."] = \
    f"{AGGA} और {ARAHA} को छोड़कर शेष व्यक्तियों ने {V} भी पूरी तरह नहीं समझा था और वे {R} भी पूरी तरह नहीं समझते।"


def a_yattha_short(s):
    """'Yattha rūpakkhandho nirujjhati…pe…' / '… (yatthakaṃ paripuṇṇaṃ kātabbaṃ)' (whole line)."""
    m = re.fullmatch(rf"Yattha ({ITEM_ALT}) ({_V})(…pe…\.| \(yatthakaṃ paripuṇṇaṃ kātabbaṃ\)\.)", s)
    if not m:
        return None
    x, v, tail = m.groups()
    base = f"जिस स्थान पर {ITEMS[item(x)][0]} {vb(v)[0]}"
    if tail.startswith("…"):
        return base + "…।"
    return base + " (स्थान वाला भाग पूरा करके पढ़ना चाहिए)।"


def tr_body_kh(text):
    r = a_yattha_short(text)
    if r:
        return r
    return tr_body(text)


# ---------------------------------------------------------------- build
def build(fname, body=None):
    raw = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
    out = [tr_line(l, body) for l in raw]
    text = "\n".join(out).rstrip("\n") + "\n"
    (HI_DIR / fname).write_text(text, encoding="utf-8", newline="\n")
    return text


def check_sample(fname, name, a, b):
    """Non-empty lines a..b of the built file must equal the sample file byte for byte."""
    built = [l for l in (HI_DIR / fname).read_text(encoding="utf-8").splitlines() if l.strip()][a - 1:b]
    samp = [l for l in (S.SAMPLE_DIR / f"{name}.md").read_text(encoding="utf-8").splitlines() if l.strip()]
    bad = [(i + a, x, y) for i, (x, y) in enumerate(zip(built, samp)) if x != y]
    ok = not bad and len(built) == len(samp)
    print(f"  sample {name}: {'identical' if ok else 'DIFFERENT'} ({len(samp)} lines)")
    for i, x, y in bad[:5]:
        print("   line", i, "\n    built :", x, "\n    sample:", y)
    return ok


def main():
    for f in ("2-01-khandhayamaka.md", "2-02-khandhayamaka.md"):
        build(f, tr_body_kh)
        print("built", f)
    check_sample("2-01-khandhayamaka.md", "s2-khandha-uddesa", 1, 27)
    check_sample("2-01-khandhayamaka.md", "s3-khandha-niddesa", 219, 248)
    check_sample("2-01-khandhayamaka.md", "s4-khandha-pavatti", 518, 547)


if __name__ == "__main__":
    main()
