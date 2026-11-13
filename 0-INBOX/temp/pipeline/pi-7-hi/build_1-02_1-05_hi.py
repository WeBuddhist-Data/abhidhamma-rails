# -*- coding: utf-8 -*-
"""Hindi plain zero-shot builder for pi-7 1-02 vedanattika, 1-03 vipakattika, 1-04 upadinnattika,
1-05 sankilitthattika.

Every line is composed from fixed frames: the approved formulas of build_sample_hi.py (imported, never
edited), the triad item tables below (pi-1 matrix Hindi), and a phrase table (Pāli word sequence ->
Hindi chunk). A small chunk grammar handles Hindi agreement (item adjective with the following noun,
the verb "कारण होता/होती/होते/होती है/हैं" with the last subject) and moves "uppajjati" after its
condition chain. Unknown Pāli is reported, never guessed.

    python -I -B -X utf8 build_1-02_1-05_hi.py            # write the four files
    python -I -B -X utf8 build_1-02_1-05_hi.py --dry      # report unknowns only
"""
import collections
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

PALI_DIR, HI_DIR = S.PALI_DIR, S.HI_DIR
FILES = ["1-02-vedanattika.md", "1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md"]
VF = {"msg": "होता है", "fsg": "होती है", "mpl": "होते हैं", "fpl": "होती हैं"}
UNKNOWN = collections.Counter()
UNK_CTX = {}
UNK_ALL = {}

# =====================================================================================
# 1. Triad items (pi-1 1-matika.md Hindi; singular feminine form for परिघटना)
# =====================================================================================
ITEMS = {
    "1-02": [("sukhāya vedanāya sampayutt", "सुखद अनुभूति से जुड़ी"),
             ("dukkhāya vedanāya sampayutt", "दुःखद अनुभूति से जुड़ी"),
             ("adukkhamasukhāya vedanāya sampayutt", "न दुःखद, न सुखद अनुभूति से जुड़ी")],
    "1-03": [("vipāk", "कर्म-फल रूपी"),
             ("vipākadhammadhamm", "कर्म-फल उत्पन्न करने वाली"),
             ("nevavipākanavipākadhammadhamm", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली")],
    "1-04": [("upādinnupādāniy", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली"),
             ("anupādinnupādāniy", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली"),
             ("anupādinnaanupādāniy", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली")],
    "1-05": [("saṃkiliṭṭhasaṃkilesik", "क्लेशों से मलिन और क्लेशों का विषय बनने वाली"),
             ("asaṃkiliṭṭhasaṃkilesik", "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली"),
             ("asaṃkiliṭṭhaasaṃkilesik", "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली")],
}
TIKA_NAME = {"1-02": "अनुभूति", "1-03": "कर्म-फल", "1-04": "कर्म से उत्पन्न", "1-05": "क्लेशों से मलिन"}


def forms(f):
    m = f.replace("जुड़ी", "जुड़ा").replace("वाली", "वाला")
    mo = f.replace("जुड़ी", "जुड़े").replace("वाली", "वाले")
    return {"f": f, "m": m, "mo": mo}


# =====================================================================================
# 2. Chunks
# =====================================================================================
class Ch:
    """kind: w (plain), noun, adj (item/other adjective), ins (…paccayena paccayo), abl, dep,
    verb (needs an object postposition), item_acc/item_nom/item_dat, p (punctuation), var."""

    def __init__(self, kind, hi="", **kw):
        self.kind, self.hi = kind, hi
        for a in ("g", "form", "agr", "forms", "fb", "fbagr", "after", "num", "tag", "post", "noobj"):
            setattr(self, a, kw.get(a))
        self.sp = True


PH = {}      # global phrase table: tuple(words) -> factory
MAXLEN = 1


def norm(w):
    return w[:1].lower() + w[1:] if w else w


def add(pali, hi, kind="w", **kw):
    """Register a Pāli word sequence. hi may be a str or a callable returning a Ch."""
    global MAXLEN
    key = tuple(norm(x) for x in pali.split())
    MAXLEN = max(MAXLEN, len(key))
    if callable(hi):
        PH[key] = hi
    else:
        PH[key] = (lambda h=hi, k=kind, a=kw: Ch(k, h, **a))


def noun(pali, hi, g="m", form="o", agr=None, num=None, tag=None):
    add(pali, hi, "noun", g=g, form=form, agr=agr, num=num, tag=tag)


def acc(pali, hi, num="sg", g="m", agr=None):
    """Object noun: a following verb chunk appends its postposition (को/पर/का)."""
    add(pali, hi, "noun", g=g, form="d" if num == "sg" else "o", num=num, tag="acc", agr=agr)


def verb(pali, post, sg, pl=None, noobj=None, tag=None):
    """Verb that needs its object marked: post = को/पर/का. noobj = text used with no object
    ("{p}" = pronoun उस/उन). Registered for the singular (…ti) and, if given, the plural (…nti)."""
    psg, ppl = (pali if isinstance(pali, tuple) else (pali, None))
    add(psg, sg, "verb", post=post, noobj=noobj[0] if noobj else None, tag=tag)
    if ppl:
        add(ppl, pl, "verb", post=post, noobj=noobj[1] if noobj else None, tag=tag)


# --- conditions -------------------------------------------------------------------
K = S.COND_KEYS
for k in K:
    neg = S.NEG_PREFIX_PALI[k]
    add(f"{k}paccayā", S.ABL(k), "abl")
    add(f"{neg}{k}paccayā", S.NABL(k), "abl")
    add(f"{k}paccayena paccayo", S.INS(k), "ins")
    add(f"{k}paccayena", S.INS(k), "ins")
    add(f"{k}paccayo", S.NAME(k))
    add(f"{neg}{k}paccayo", S.NNAME(k))
    add(f"{k}paccayasadisaṃ", S.SADISA(k) + " है")
    add(f"{neg}{k}paccayasadisaṃ", S.SADISA(k, neg=True) + " है")
    add(f"{k}sadisaṃ", S.SADISA(k) + " है")
    add(f"{k}sadisā", S.SADISA(k))
add("na adhipatipaccayā", S.NABL("adhipati"), "abl")   # spaced "na adhipati" (as count_hi)

# --- dependence words (six "dependent" sections) ------------------------------------
for w in ("paṭicca",):
    add(w, S.DEP["paṭicca"], "dep")
for w in ("sahajāto", "sahajātā"):
    add(w, S.DEP["sahajāta"], "dep")
add("paccayā", S.DEP["paccaya"], "dep")
add("nissāya", S.DEP["nissaya"], "dep")
for w in ("saṃsaṭṭho", "saṃsaṭṭhā"):
    add(w, S.DEP["saṃsaṭṭha"], "dep")
for w in ("sampayutto", "sampayuttā"):
    add(w, S.DEP["sampayutta"], "dep")

# --- numbers --------------------------------------------------------------------------
for p, h in S.NUM.items():
    add(p, h)
add("ekā", "एक")
add("tisso", "तीन")

# --- khandha / mahābhūta / rūpa -------------------------------------------------------
noun("ekaṃ khandhaṃ", "एक समूह", "m", "o")
noun("eko khandho", "एक समूह", "m", "d", agr="msg")
noun("khandhā", "समूह", "m", "o", agr="mpl", num="pl")
noun("khandhe", "समूहों", "m", "o", num="pl")
noun("khandhānaṃ", "समूहों के लिए", "m", "o")
noun("khandhassa", "समूह के लिए", "m", "o")
noun("ekaṃ khandhañca vatthuñca", "एक समूह और आधार", "m", "o")
noun("khandhe ca mahābhūte ca", "समूहों और महाभूतों", "m", "o")
noun("khandhe ca vatthuñca", "समूहों और आधार", "m", "o")
noun("khandhā ca mahābhūtā ca", "समूह और महाभूत", "m", "o", agr="mpl")
noun("eko khandho ca vatthu ca", "एक समूह और आधार", "m", "d", agr="mpl")
add("tayo khandhā", "तीन समूह", "noun", g="m", form="o", agr="mpl")
add("tayokhandhā", "तीन समूह", "noun", g="m", form="o", agr="mpl")
add("tayo khandhe", "तीन समूहों")
add("dve khandhā", "दो समूह", "noun", g="m", form="o", agr="mpl")
add("dve khandhe", "दो समूहों")
add("tayo khandhe ca vatthuñca", "तीन समूहों और आधार")
add("dve khandhe ca vatthuñca", "दो समूहों और आधार")
add("dvinnaṃ khandhānaṃ", "दो समूहों के लिए")
add("tiṇṇannaṃ khandhānaṃ", "तीन समूहों के लिए")
add("tiṇṇannaṃ", "तीन के लिए")
add("dvinnaṃ", "दो के लिए")
add("ekassa khandhassa", "एक समूह के लिए")
add("cittasamuṭṭhānañca rūpaṃ", S.AND_CSR)
add("kaṭattā ca rūpaṃ", S.AND_KTR)
add("vatthu ca", "और आधार")
noun("ekaṃ mahābhūtaṃ", "एक महाभूत", "m", "o")
add("tayo mahābhūtā", "तीन महाभूत", "noun", g="m", form="o", agr="mpl")
add("tayo mahābhūte", "तीन महाभूतों")
add("dve mahābhūte", "दो महाभूतों")
add("dve mahābhūtā", "दो महाभूत", "noun", g="m", form="o", agr="mpl")
noun("mahābhūte", "महाभूतों", "m", "o")
add("mahābhūtā", "महाभूत", "noun", g="m", form="o", agr="mpl")
add("tiṇṇannaṃ mahābhūtānaṃ", "तीन महाभूतों के लिए")
add("ekassa mahābhūtassa", "एक महाभूत के लिए")
add("dvinnaṃ mahābhūtānaṃ", "दो महाभूतों के लिए")
add("bāhiraṃ ekaṃ mahābhūtaṃ", f"एक {S.BAHIRA} महाभूत")
add("cittasamuṭṭhānaṃ rūpaṃ", S.CSR, "noun", g="m", form="d", agr="msg")
add("kaṭattārūpaṃ", S.KTR, "noun", g="m", form="d", agr="msg")
add("upādārūpaṃ", S.UPR)
add("cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ", f"{S.CSR}, {S.KTR}, {S.UPR}")
add("cittasamuṭṭhānaṃ rūpaṃ upādārūpaṃ", f"{S.CSR}, {S.UPR}")
add("kaṭattārūpaṃ upādārūpaṃ", f"{S.KTR}, {S.UPR}")
add("rūpaṃ", "भौतिक रूप")
add("cittasamuṭṭhānānaṃ rūpānaṃ", f"{S.CSR_OBL} के लिए")
add("kaṭattārūpānaṃ", f"{S.KTR_OBL} के लिए")
add("upādārūpānaṃ", f"{S.UPR_OBL} के लिए")
add("cittasamuṭṭhānānaṃ rūpānaṃ kaṭattārūpānaṃ upādārūpānaṃ",
    f"{S.CSR_OBL} के लिए, {S.KTR_OBL} के लिए, {S.UPR_OBL} के लिए")
add("kaṭattārūpānaṃ upādārūpānaṃ", f"{S.KTR_OBL} के लिए, {S.UPR_OBL} के लिए")
add("cittasamuṭṭhānānañca rūpānaṃ", f"और {S.CSR_OBL} के लिए")
add("cittasamuṭṭhānañca rūpānaṃ", f"और {S.CSR_OBL} के लिए")   # source slip (spelling) for -ānañca
add("kaṭattā ca rūpānaṃ", f"और {S.KTR_OBL} के लिए")
add("sampayuttakānaṃ khandhānaṃ", f"{S.SAMPAYUTTAKA_KH_OBL} के लिए")
add("sappayuttakānaṃ khandhānaṃ", f"{S.SAMPAYUTTAKA_KH_OBL} के लिए")  # spelling slip
add("vatthu", "आधार", "noun", g="m", form="d", agr="msg")
add("vatthuṃ", "आधार")
add("vatthussa", "आधार के लिए")
add("vatthussa ca", "और आधार के लिए")
noun("hetū", "मूल", "m", "o", agr="mpl")
noun("cetanā", "इरादा", "m", "d", agr="msg")
noun("āhārā", "आहार", "m", "o", agr="mpl")
noun("indriyā", "क्षमताएँ", "f", "o", agr="fpl")
noun("jhānaṅgā", "ध्यान के अंग", "m", "o", agr="mpl")
noun("maggaṅgā", "मार्ग के अंग", "m", "o", agr="mpl")
noun("adhipati", "प्रधानता", "f", "d", agr="fsg")

# --- circumstances --------------------------------------------------------------------
add("paṭisandhikkhaṇe", S.PATISANDHI)
add("paṭisandhikhaṇe", S.PATISANDHI)      # spelling slip
add("ahetukapaṭisandhikkhaṇe", S.AHETUKA_PATISANDHI)
add("arūpe", S.ARUPE)
add("bāhiraṃ", S.BAHIRA)
add("āhārasamuṭṭhānaṃ", S.AHARASAM)
add("utusamuṭṭhānaṃ", S.UTUSAM)
add("asaññasattānaṃ", S.ASANNASATTA)
add("vicikicchāsahagate uddhaccasahagate khandhe", S.KHANDHE_VU)
add("vicikicchāsahagato uddhaccasahagato moho", S.MOHA_VU, "noun", g="m", form="d", agr="msg")
add("pañcaviññāṇasahagataṃ ekaṃ khandhaṃ", f"{S.PANCAVINNANA_SAHAGATA} एक समूह")
add("rūpajīvitindriyaṃ", S.RUPAJIVITINDRIYA, "noun", g="f", form="d", agr="fsg")

# --- notes -----------------------------------------------------------------------------
add("saṃkhittaṃ", "संक्षिप्त")
add("saṅkhittaṃ", "संक्षिप्त")

# =====================================================================================
# 3. Per-file item entries
# =====================================================================================
ENDINGS = ["aṃ", "o", "ā", "e", "assa", "ānaṃ", "akānaṃ", "ena", "āya"]
FB = {"aṃ": ("परिघटना", None), "o": ("परिघटना", "fsg"), "assa": ("परिघटना के लिए", None),
      "ā": ("परिघटनाएँ", "fpl"), "e": ("परिघटनाओं", None), "ānaṃ": ("परिघटनाओं के लिए", None)}


def item_phrases(code):
    """Return {key: factory} for the three items of a triad file."""
    out = {}
    items = ITEMS[code]

    def reg(pali, factory):
        out[tuple(norm(x) for x in pali.split())] = factory

    for stem, f in items:
        fm = forms(f)
        d = "" if stem.endswith("dhamm") else " "      # vipākadhammadhammaṃ has no separate dhammaṃ
        dh = (lambda e: f"{stem}{e}") if d == "" else (lambda e, s=stem: f"{s}{e}")
        # item + dhamma
        if d == "":
            reg(f"{stem}aṃ", None)  # placeholder, overwritten by ADJ below (lookahead decides)
        else:
            reg(f"{stem}aṃ dhammaṃ", lambda h=f: Ch("item_acc", f"{h} परिघटना"))
            reg(f"{stem}o dhammo", lambda h=f: Ch("item_nom", f"{h} परिघटना", agr="fsg"))
            reg(f"{stem}assa dhammassa", lambda h=f: Ch("item_dat", f"{h} परिघटना के लिए"))
        # adjective (+ noun decides the form); without a noun it falls back to the item noun
        for e in ENDINGS:
            fb, fbagr = FB.get(e, ("परिघटना", None))
            kind = {"aṃ": "item_acc", "o": "item_nom", "assa": "item_dat"}.get(e, "adj")
            reg(f"{stem}{e}", lambda fm=fm, fb=fb, fbagr=fbagr, f=f, kind=kind:
                Ch("adj", forms=fm, fb=f"{f} {fb}", fbagr=fbagr, after=kind))
        # compounds
        reg(f"{stem}ādhipati", lambda h=fm["f"]: Ch("noun", f"{h} प्रधानता", g="f", form="d", agr="fsg"))
        reg(f"{stem}acittasamaṅgissa cittaṃ", lambda h=fm["mo"]: Ch("w", f"{h} मन से युक्त व्यक्ति के मन को"))
        reg(f"{stem}cittasamaṅgissa cittaṃ", lambda h=fm["mo"]: Ch("w", f"{h} मन से युक्त व्यक्ति के मन को"))
    # pairs: Xañca Yañca dhammaṃ / Xo ca Yo ca dhammā / Xassa ca Yassa ca dhammassa
    for s1, f1 in items:
        for s2, f2 in items:
            if s1 == s2:
                continue
            reg(f"{s1}añca {s2}añca dhammaṃ", lambda a=f1, b=f2: Ch("item_acc", f"{a} परिघटना और {b} परिघटना"))
            reg(f"{s1}o ca {s2}o ca dhammā", lambda a=f1, b=f2: Ch("item_nom", f"{a} और {b} परिघटनाएँ", agr="fpl"))
            reg(f"{s1}assa ca {s2}assa ca dhammassa",
                lambda a=f1, b=f2: Ch("item_dat", f"{a} परिघटना और {b} परिघटना के लिए"))
            reg(f"{s1}assa ca {s2}assa ca",
                lambda a=f1, b=f2: Ch("item_dat", f"{a} परिघटना और {b} परिघटना के लिए"))
    for sa, fa in items:
        ma = forms(fa)["m"]
        reg(f"purejātassa imassa {sa}assa ca kāyassa",
            lambda h=forms(fa)["mo"]: Ch("w", f"और पहले उत्पन्न इस {h} शरीर के लिए"))
        reg(f"{sa}o kabaḷīkāro āhāro", lambda h=ma: Ch("noun", f"{h} कौर-कौर खाया जाने वाला भोजन",
                                                      g="m", form="d", agr="msg"))
        reg(f"{sa}o kabaḷīkāro āhāro ca", lambda h=ma: Ch("w", f"{h} कौर-कौर खाया जाने वाला भोजन और"))
        for sb, fb in items:
            if sa != sb:
                mb = forms(fb)["m"]
                reg(f"{sa}o ca {sb}o ca kabaḷīkāro āhāro",
                    lambda a=ma, b=mb: Ch("noun", f"{a} और {b} कौर-कौर खाया जाने वाला भोजन", g="m", form="d",
                                          agr="msg"))
                reg(f"{sa}añca {sb}añca", lambda a=fa, b=fb: Ch("item_acc", f"{a} परिघटना और {b} परिघटना"))
    (s1, f1), (s2, f2), (s3, f3) = items
    reg(f"{s1}o ca {s2}o ca {s3}o ca dhammā", lambda: Ch("item_nom", f"{f1}, {f2} और {f3} परिघटनाएँ", agr="fpl"))
    reg(f"{s1}assa ca {s2}assa ca {s3}assa ca dhammassa",
        lambda: Ch("item_dat", f"{f1} परिघटना, {f2} परिघटना और {f3} परिघटना के लिए"))
    reg(f"{s1}añca {s2}añca {s3}añca dhammaṃ",
        lambda: Ch("item_acc", f"{f1} परिघटना, {f2} परिघटना और {f3} परिघटना"))
    for s, f in items:
        fm = forms(f)
        reg(f"{s}āni jhānaṅgāni", lambda h=fm["mo"]: Ch("noun", f"{h} ध्यान के अंग", g="m", form="o", agr="mpl"))
        reg(f"{s}āni maggaṅgāni", lambda h=fm["mo"]: Ch("noun", f"{h} मार्ग के अंग", g="m", form="o", agr="mpl"))
    if code == "1-05":   # spelling slip asaṅkiliṭṭhasaṃkilisikassa = asaṃkiliṭṭhasaṃkilesikassa
        reg("asaṅkiliṭṭhasaṃkilisikassa dhammassa", lambda h=f2: Ch("item_dat", f"{h} परिघटना के लिए"))
    return out


# =====================================================================================
# 4. Tokenizer and translator
# =====================================================================================
TOK = re.compile(r"\{[^}]*\}|\((?:[^()]|\([^()]*\))*\)|…pe…|…|–|[,;.:?“”]|[^\s,;.…(){}–?“”]+|\s+")
COND_RX = re.compile(r"^(?:na|no)?(" + "|".join(sorted(K, key=len, reverse=True)) + r")paccayā$")
NOTES = {}      # exact parenthetical / sentence translations (filled below)
EXACT = {}      # exact line bodies


def tokens(text):
    out, sp = [], False
    for m in TOK.finditer(text):
        t = m.group(0)
        if t.isspace():
            sp = True
            continue
        out.append((t, sp))
        sp = False
    return out


def is_word(t):
    return not (t[0] in "{(…–,;.:?“”")


def reorder_uppajjati(toks):
    """Move uppajjati/uppajjanti after the following condition chain."""
    out, i = [], 0
    while i < len(toks):
        t, sp = toks[i]
        if norm(t) in ("uppajjati", "uppajjanti"):
            j, last = i + 1, None
            while j < len(toks):
                tj = norm(toks[j][0])
                if COND_RX.match(tj) or (tj == "na" and j + 1 < len(toks) and COND_RX.match("na" + toks[j + 1][0])):
                    last = j
                    j += 1
                elif tj in ("…", "…pe…") or toks[j][0].startswith("("):
                    j += 1
                else:
                    break
            if last is not None:
                out.extend(toks[i + 1:last + 1])
                out.append((t, True))
                i = last + 1
                continue
        out.append((t, sp))
        i += 1
    return out


def lookup(words, table):
    for n in range(min(12, len(words)), 0, -1):
        key = tuple(norm(w) for w in words[:n])
        f = table.get(key) or PH.get(key)
        if f is not None:
            return n, f
    return 0, None


def render_paren(t, table):
    inner = t[1:-1]
    if re.fullmatch(r"\d+(\.)?", inner):
        return t
    if inner in NOTES:
        return "(" + NOTES[inner] + ")"
    return "(" + tr(inner, table) + ")"


VARIANTS = {}   # "{…}" -> Hindi bracket


SPELLING_VARIANTS = {"{nānākhaṇikā (ka.)}"}


def render_variant(t):
    """{word (sī. syā.)} -> [पाठभेद (Sī., Syā.): word]; spelling-only ones -> वर्तनी-भेद."""
    if t in VARIANTS:
        return VARIANTS[t]
    m = re.fullmatch(r"\{(.+?) \(([^()]+)\)\}", t)
    if not m:
        UNKNOWN[t] += 1
        return "[??" + t + "]"
    sig = ", ".join(x.strip().capitalize() for x in m.group(2).split(".") if x.strip())
    sig = ", ".join(s + "." for s in sig.split(", "))
    label = "वर्तनी-भेद" if t in SPELLING_VARIANTS else "पाठभेद"
    return f"[{label} ({sig}): {m.group(1)}]"


NANA = {"iddhividha": S.IDDHIVIDHA_OBL, "cetopariya": S.CETOPARIYA_OBL,
        "pubbenivāsānussati": S.PUBBENIVASA_OBL, "yathākammūpaga": S.YATHAKAMMUPAGA_OBL,
        "anāgataṃsa": S.ANAGATAMSA_OBL}
NANA_RX = re.compile(r"((?:(?:" + "|".join(NANA) + r")ñāṇassa(?:, | )?)+)(āvajjanāya )?")


def nana_sub(text, local):
    """'iddhividhañāṇassa, …, anāgataṃsañāṇassa, āvajjanāya' -> one chunk 'A, B और C के लिए तथा …'."""
    def rep(m):
        names = re.findall(r"(" + "|".join(NANA) + r")ñāṇassa", m.group(1))
        obl = [NANA[x] for x in names]
        h = (obl[0] if len(obl) == 1 else ", ".join(obl[:-1]) + " और " + obl[-1]) + " के लिए"
        if m.group(2):
            h += " तथा " + S.AVAJJANA_FOR
        key = f"ñlist{len(local)}"
        local[(key,)] = (lambda h=h: Ch("w", h))
        return key + " "
    return NANA_RX.sub(rep, text).replace("  ", " ")


def tr(text, table, ctx=""):
    """Translate a Pāli span (no block ID)."""
    local = {}
    text = nana_sub(text, local)
    if local:
        table = dict(table)
        table.update(local)
    toks = reorder_uppajjati(tokens(text))
    chunks = []
    i = 0
    while i < len(toks):
        t, sp = toks[i]
        if not is_word(t):
            if t.startswith("("):
                c = Ch("p", render_paren(t, table))
            elif t.startswith("{"):
                c = Ch("var", render_variant(t))
            else:
                c = Ch("p", {"…pe…": "…", ".": "।"}.get(t, t))
            c.sp = sp
            chunks.append(c)
            i += 1
            continue
        # gather word run
        j = i
        while j < len(toks) and is_word(toks[j][0]):
            j += 1
        words = [w for w, _ in toks[i:j]]
        sps = [s for _, s in toks[i:j]]
        if len(words) == 1 and norm(words[0]) in LABELS:
            c = Ch("w", LABELS[norm(words[0])])
            c.sp = sps[0]
            chunks.append(c)
            i = j
            continue
        k = 0
        while k < len(words):
            n, f = lookup(words[k:], table)
            if f is None:
                # unknown: collect a maximal unknown run
                m = k + 1
                while m < len(words) and lookup(words[m:], table)[1] is None:
                    m += 1
                unk = " ".join(words[k:m])
                UNKNOWN[unk] += 1
                UNK_CTX.setdefault(unk, ctx or text[:120])
                UNK_ALL.setdefault(unk, []).append(" ".join(words[max(0, k - 4):k + 4]))
                c = Ch("w", "??" + unk + "??")
                c.sp = sps[k]
                chunks.append(c)
                k = m
                continue
            c = f()
            c.sp = sps[k]
            chunks.append(c)
            k += n
        i = j
    return render(chunks)


def render(chunks):
    out = []
    last_agr = None
    n = len(chunks)
    eff = []
    for idx, c in enumerate(chunks):
        j2 = idx + 1
        while j2 < n and chunks[j2].kind == "adj":
            j2 += 1
        if c.kind == "adj" and not (j2 < n and chunks[j2].kind == "noun"):
            eff.append(c.after)
        else:
            eff.append(c.kind)
    txts = []
    for idx, c in enumerate(chunks):
        nxt = chunks[idx + 1] if idx + 1 < n else None
        if c.kind == "adj" and eff[idx] != "adj":
            txt = c.fb
            if c.fbagr:
                last_agr = c.fbagr
            if eff[idx] == "item_nom" and idx + 1 < n and eff[idx + 1] == "item_dat":
                txt += ","
        elif c.kind == "adj":
            noun_c = None
            for c2 in chunks[idx + 1:]:
                if c2.kind == "noun":
                    noun_c = c2
                    break
                if c2.kind != "adj":
                    break
            key = "f" if noun_c is None or noun_c.g == "f" else ("m" if noun_c.form == "d" else "mo")
            txt = c.forms[key] + ("," if nxt is not None and nxt.kind == "adj" else "")
        elif c.kind == "ins":
            txt = f"{c.hi} {VF.get(last_agr or 'msg')}"
        elif c.kind == "w" and c.hi == "@UPP":
            txt = "उत्पन्न " + VF.get(last_agr or "fsg")
        else:
            txt = c.hi
            if c.agr:
                last_agr = c.agr
            if c.kind == "item_nom" and idx + 1 < n and eff[idx + 1] == "item_dat":
                txt += ","
        txts.append(txt)
    # object postpositions demanded by verbs (paccavekkhati पर, vipassati को, assādeti का …)
    for idx, c in enumerate(chunks):
        if c.kind != "verb":
            continue
        j = idx - 1
        while j >= 0 and (chunks[j].tag == "instr" or (chunks[j].kind == "adj" and j + 1 < n
                                                          and chunks[j + 1].tag == "instr")):
            j -= 1
        obj = j if j >= 0 and chunks[j].tag == "acc" else None
        num = None
        if obj is not None:
            num = chunks[obj].num or "sg"
            k = obj
            while True:
                txts[k] = attach(txts[k], c.post)
                if k >= 1 and chunks[k - 1].kind == "adj" and chunks[k - 1].forms and chunks[k].g == "m":
                    txts[k - 1] = chunks[k - 1].forms["mo"] + ("," if txts[k - 1].endswith(",") else "")
                # a "…"-list of objects before it gets the same postposition
                m = k - 1
                while m >= 0 and chunks[m].kind == "adj":
                    m -= 1
                if m >= 1 and chunks[m].kind == "p" and chunks[m].hi == "…" and chunks[m - 1].tag == "acc":
                    k = m - 1
                    continue
                break
            txts[idx] = c.hi.replace("{p}", "उन" if num == "pl" else "उस")
        else:
            # no object: pronoun from the last object in the sentence (or after garuṃ katvā)
            m = idx - 1
            while m >= 0 and not (chunks[m].kind == "p" and chunks[m].hi in ("।", ";", "–")):
                if chunks[m].tag == "acc":
                    num = chunks[m].num or "sg"
                    break
                m -= 1
            p = "उन" if num == "pl" else "उस"
            if j >= 0 and chunks[j].tag == "garu":
                txts[idx] = attach(p, c.post) + " " + c.hi.replace("{p}", p)
            elif c.noobj is not None:
                txts[idx] = c.noobj.replace("{p}", p)
            else:
                txts[idx] = c.hi.replace("{p}", p)
    for idx, c in enumerate(chunks):
        txt = txts[idx]
        if c.kind in ("p", "var") and not c.sp:
            out.append(txt)
        elif not out:
            out.append(txt)
        else:
            out.append((" " if c.sp else "") + txt)
    return "".join(out)


def attach(np, post):
    if np.endswith("उस") and post == "को":
        return np[:-2] + "उसे"
    if np.endswith("उन") and post == "को":
        return np[:-2] + "उन्हें"
    if np.endswith("उस") or np.endswith("उन"):
        return np + ("का" if post == "का" else " " + post)
    return np + " " + post


add("uppajjati", "@UPP")
add("uppajjanti", "@UPP")

# =====================================================================================
# 4b. Vocabulary of the pañhāvāra (and the paṭicca bodies)
# =====================================================================================
# labels (a one-word run before "–", "," or ".")
LABELS = {
    "sahajātaṃ": "सह-उत्पत्ति रूपी", "sahajātā": "सह-उत्पत्ति रूपी", "sahajāto": "सह-उत्पत्ति रूपी",
    "purejātaṃ": "पूर्व-उत्पत्ति रूपी", "pacchājātaṃ": "पश्चात्-उत्पत्ति रूपी",
    "pacchājātā": "पश्चात्-उत्पत्ति रूपी", "nānākkhaṇikā": "भिन्न क्षण रूपी",
    "āhāraṃ": "आहार रूपी", "indriyaṃ": "क्षमता रूपी",
}
for _w in ("sahajātaṃ", "purejātaṃ", "pacchājātaṃ", "āhāraṃ", "indriyaṃ", "nānākkhaṇikā"):
    add(_w, LABELS[_w])
add("ārammaṇādhipati", S.ARAMMANADHIPATI)
add("sahajātādhipati", S.SAHAJATADHIPATI)
add("ārammaṇūpanissayo", S.ARAMMANUPANISSAYA)
add("anantarūpanissayo", S.ANANTARUPANISSAYA)
add("pakatūpanissayo", S.PAKATUPANISSAYA)
add("ārammaṇapurejātaṃ", S.ARAMMANAPUREJATA)
add("vatthupurejātaṃ", S.VATTHUPUREJATA)
add("pacchājātā", "बाद में उत्पन्न")
add("purejātassa imassa kāyassa", "पहले उत्पन्न इस शरीर के लिए")
add("imassa kāyassa", "इस शरीर के लिए")
add("kabaḷīkāro āhāro", "कौर-कौर खाया जाने वाला भोजन", "noun", g="m", form="d", agr="msg")
noun("khandhā ca kabaḷīkāro āhāro ca", "समूह और कौर-कौर खाया जाने वाला भोजन", agr="mpl")
noun("khandhā ca rūpajīvitindriyañca", "समूह और भौतिक जीवन-क्षमता", agr="mpl")
add("vatthuṃ purejātapaccayā", f"आधार पर {S.ABL('purejāta')}")
add("vatthuṃ vippayuttapaccayā", f"आधार पर {S.ABL('vippayutta')}")
add("vatthuṃ khandhā", "आधार पर समूह")          # source slip: paṭicca missing (1-04)

# other adjectives (forms: f, m, mo)
GADJ = [("kusal", "हितकर"), ("vipāk", "कर्म के फल रूपी"), ("ahetuk", "मूल से रहित")]
for stem, h in GADJ:
    for e in ENDINGS:
        add(f"{stem}{e}", lambda h=h: Ch("adj", forms={"f": h, "m": h, "mo": h}, fb=h, after="adj"))

# subjects / persons
add("ariyā", "आर्य", "noun", g="m", form="o", agr="mpl")
add("sekkhā", S.SEKKHA, "noun", g="m", form="o", agr="mpl")
add("sekkhā vā puthujjanā vā", S.SEKKHA_VA_PUTHUJJANA, "noun", g="m", form="o", agr="mpl")
add("arahā", S.ARAHA, "noun", g="m", form="d", agr="msg")
add("sekkhānaṃ anulomaṃ", "सीखने के चरण वालों की अनुकूलता", "noun", g="f", form="d", agr="fsg")
add("arahato anulomaṃ", "अर्हत् की अनुकूलता", "noun", g="f", form="d", agr="fsg")
add("sekkhānaṃ atthappaṭisambhidāya", "सीखने के चरण वालों के अर्थ के विश्लेषणात्मक ज्ञान के लिए")
add("arahato atthappaṭisambhidāya", "अर्हत् के अर्थ के विश्लेषणात्मक ज्ञान के लिए")
add("ṭhānāṭhānakosallassa", "संभव और असंभव को जानने की कुशलता के लिए")

# instrumental "with … mind"
noun("cittena", "मन से", "m", "o", tag="instr")
add("duṭṭhena cittena tathāgatassa lohitaṃ uppādeti", "दुष्ट मन से तथागत का खून बहाता है")

# objects
for p, h, nm, g in [
        ("cakkhuṃ", "आँख", "sg", "f"), ("sotaṃ", "कान", "sg", "m"), ("ghānaṃ", "नाक", "sg", "f"),
        ("jivhaṃ", "जीभ", "sg", "f"), ("kāyaṃ", "शरीर", "sg", "m"), ("rūpe", "दृश्य रूपों", "pl", "m"),
        ("sadde", "ध्वनियों", "pl", "f"), ("gandhe", "गंधों", "pl", "f"), ("rase", "स्वादों", "pl", "m"),
        ("phoṭṭhabbe", "स्पर्शों", "pl", "m"), ("phalaṃ", "फल", "sg", "m"), ("nibbānaṃ", "निर्वाण", "sg", "m"),
        ("maggaṃ", "मार्ग", "sg", "m"), ("jhānaṃ", "ध्यान", "sg", "m"), ("gotrabhuṃ", "गोत्र-परिवर्तन", "sg", "m"),
        ("vodānaṃ", "शुद्धि", "sg", "f"), ("pahīne kilese", "छोड़े जा चुके मन के क्लेशों", "pl", "m"),
        ("vikkhambhite kilese", "दबाए जा चुके मन के क्लेशों", "pl", "m"),
        ("pubbe samudāciṇṇe kilese", "पहले बार-बार उठे मन के क्लेशों", "pl", "m"),
        ("pubbe suciṇṇāni", S.SUCINNA, "pl", "m"), ("saṅkhāre", "मानसिक रचनाओं", "pl", "f"),
        ("taṃ", "उस", "sg", "m"), ("khandhe", "समूहों", "pl", "m"), ("vatthuṃ", "आधार", "sg", "m"),
        ("dosaṃ", "द्वेष", "sg", "m"), ("mohaṃ", "मोह", "sg", "m"), ("rāgaṃ", "राग", "sg", "m")]:
    acc(p, h, nm, g)
acc("phalaṃ", "फल", "sg", "m", agr="msg")
acc("nibbānaṃ", "निर्वाण", "sg", "m", agr="msg")
acc("vodānaṃ", "शुद्धि", "sg", "f", agr="fsg")
noun("khandhe", "समूहों", "m", "o", num="pl", tag="acc")
noun("jhāne parihīne", "ध्यान के छूट जाने पर", "m", "o")
add("rūpaṃ passati", "दृश्य रूप देखता है", "noun", g="m", form="d")
add("rūpaṃ passanti", "दृश्य रूप देखते हैं", "noun", g="m", form="d")
add("dibbena cakkhunā", "दिव्य आँख से")
add("dibbāya sotadhātuyā saddaṃ suṇāti", "दिव्य कान के तत्व से ध्वनि सुनता है")
add("dibbāya sotadhātuyā saddaṃ suṇanti", "दिव्य कान के तत्व से ध्वनि सुनते हैं")
add("dibbāya sotadhātuyā saddaṃ", "दिव्य कान के तत्व से ध्वनि")
add("dibbāya sotadhātuyā", "दिव्य कान के तत्व से")
add("rūpaṃ", "दृश्य रूप", "noun", g="m", form="d")

# verbs with object marking
verb(("paccavekkhati", "paccavekkhanti"), "पर", S.REVIEW_SG, S.REVIEW_PL)
VIP = S.ANICCA3
verb(("aniccato dukkhato anattato vipassati", "aniccato dukkhato anattato vipassanti"), "को",
     f"{VIP} {S.VIPASSATI}", f"{VIP} {S.VIPASSANTI}")
verb("aniccato dukkhato anattato vippassanti", "को", f"{VIP} {S.VIPASSANTI}")   # spelling slip
verb("aniccato", "को", "अनित्य")
verb(("assādeti abhinandati", "assādenti abhinandanti"), "का",
     "रस लेता है, {p}में आनंद लेता है", "रस लेते हैं, {p}में आनंद लेते हैं",
     noobj=("{p}का रस लेता है, {p}में आनंद लेता है", "{p}का रस लेते हैं, {p}में आनंद लेते हैं"))
verb("assādenti abhinandati", "का", "रस लेते हैं, {p}में आनंद लेते हैं",
     noobj=("{p}का रस लेते हैं, {p}में आनंद लेते हैं",))   # agreement slip (pl + sg) kept plural
verb(("assādeti", "assādenti"), "का", "रस लेता है", "रस लेते हैं",
     noobj=("{p}का रस लेता है", "{p}का रस लेते हैं"))
verb("garuṃ katvā", "को", "महत्व देकर", tag="garu")
verb("ārabbha", "को", "विषय बनाकर")
verb(("jānāti", "jānanti"), "को", "जानता है", "जानते हैं", noobj=("जानता है", "जानते हैं"))

# arising
for p, h, a in [("rāgo", "राग", "m"), ("diṭṭhi", "दृष्टि", "f"), ("vicikicchā", "संशय", "m"),
                ("uddhaccaṃ", "बेचैनी", "f"), ("domanassaṃ", "उदासी", "f"), ("doso", "द्वेष", "m"),
                ("moho", "मोह", "m")]:
    add(f"{p} uppajjati", f"{h} उत्पन्न {'होता है' if a == 'm' else 'होती है'}", "noun", g=a, form="d")
    add(p, h, "noun", g=a, form="d", agr=a + "sg")
add("vipāko tadārammaṇatā uppajjati", S.TADARAMMANA)
add("vipāko tadārammaṇatā", "कर्म-फल उसी विषय को लेकर")
add("tadārammaṇatā uppajjati", "उसी विषय को लेकर उत्पन्न होता है")
add("kusalākusale niruddhe", "हितकर और हानिकर के समाप्त होने पर")
add("vippaṭisārissa domanassaṃ uppajjati", "ग्लानि से भरे व्यक्ति में उदासी उत्पन्न होती है")
add("cetopariyañāṇena", S.CETOPARIYENA)

# dāna etc.
add("dānaṃ datvā", "दान देकर")
add("sīlaṃ samādiyitvā", "सदाचार ग्रहण करके")
add("uposathakammaṃ katvā", "उपवास-व्रत का पालन करके")
for p, h in [("jhānā", "ध्यान"), ("maggā", "मार्ग"), ("phalā", "फल")]:
    noun(f"{p} vuṭṭhahitvā", f"{h} से उठकर", "m", "o")
for p, h in [
        ("dānaṃ deti", "दान देता है"), ("sīlaṃ samādiyati", "सदाचार ग्रहण करता है"),
        ("uposathakammaṃ karoti", "उपवास-व्रत का पालन करता है"),
        ("vipassanaṃ uppādeti", "अंतर्दृष्टि उत्पन्न करता है"), ("maggaṃ uppādeti", "मार्ग उत्पन्न करता है"),
        ("abhiññaṃ uppādeti", "उच्च ज्ञान उत्पन्न करता है"),
        ("samāpattiṃ uppādeti", "ध्यान-अवस्था उत्पन्न करता है"), ("mānaṃ jappeti", "अहंकार पालता है"),
        ("diṭṭhiṃ gaṇhāti", "दृष्टि ग्रहण करता है"), ("adinnaṃ ādiyati", "बिना दी हुई वस्तु लेता है"),
        ("musā bhaṇati", "झूठ बोलता है"), ("pisuṇaṃ bhaṇati", "चुगली करता है"),
        ("pharusaṃ bhaṇati", "कठोर वचन बोलता है"), ("samphaṃ palapati", "व्यर्थ बकवास करता है"),
        ("sandhiṃ chindati", "सेंध लगाता है"), ("nillopaṃ harati", "डाका डालता है"),
        ("ekāgārikaṃ karoti", "एक ही घर को लूटता है"), ("paripanthe tiṭṭhati", "राह में घात लगाता है"),
        ("paradāraṃ gacchati", "पराई स्त्री के पास जाता है"), ("gāmaghātaṃ karoti", "गाँव को लूटता है"),
        ("nigamaghātaṃ karoti", "कस्बे को लूटता है"), ("pāṇaṃ hanati", "प्राणी की हत्या करता है"),
        ("mātaraṃ jīvitā voropeti", "माता की जान लेता है"), ("pitaraṃ jīvitā voropeti", "पिता की जान लेता है"),
        ("arahantaṃ jīvitā voropeti", "अर्हत् की जान लेता है"), ("saṅghaṃ bhindati", "संघ में फूट डालता है"),
        ("attānaṃ ātāpeti paritāpeti", "स्वयं को तपाता है, कष्ट देता है"),
        ("pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti", "खोज के कारण होने वाला दुःख भोगता है"),
        ("anuppannaṃ kiriyasamāpattiṃ uppādeti", "अब तक उत्पन्न न हुई केवल क्रिया रूपी ध्यान-अवस्था उत्पन्न करता है"),
        ("uppannaṃ samāpajjati", "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करता है"),
        ("anuppannaṃ kusalasamāpattiṃ uppādenti", "अब तक उत्पन्न न हुई हितकर ध्यान-अवस्था उत्पन्न करते हैं"),
]:
    add(p, h)
noun("jhānaṃ uppādeti", "ध्यान उत्पन्न करता है", "m", "d")
add("upanissāya", "के प्रबल आश्रय से")
# qualities (acc / nom / dat)
QUAL = [("saddh", "श्रद्धा", "f", "aṃ", "ā", "āya"), ("sīl", "सदाचार", "m", "aṃ", "aṃ", "assa"),
        ("sut", "सुना-सीखा ज्ञान", "m", "aṃ", "aṃ", "assa"), ("cāg", "त्याग", "m", "aṃ", "o", "assa"),
        ("paññ", "प्रज्ञा", "f", "aṃ", "ā", "āya"), ("rāg", "राग", "m", "aṃ", "o", "assa"),
        ("dos", "द्वेष", "m", "aṃ", "o", "assa"), ("moh", "मोह", "m", "aṃ", "o", "assa"),
        ("mān", "अहंकार", "m", "aṃ", "o", "assa"), ("patthan", "कामना", "f", "aṃ", "ā", "āya")]
for stem, h, g, a_, n_, d_ in QUAL:
    if n_ != a_:
        noun(stem + n_, h, g, "d", agr=g + "sg")
    noun(stem + a_, h, g, "d", num="sg", tag="acc", agr=(g + "sg") if n_ == a_ else None)
    obl = "सुने-सीखे ज्ञान" if h == "सुना-सीखा ज्ञान" else h
    noun(stem + d_, f"{obl} के लिए", g, "o")
noun("diṭṭhiṃ", "दृष्टि", "f", "d")
noun("diṭṭhiyā", "दृष्टि के लिए", "f", "o")
for p, h in [("utuṃ", "तापमान"), ("utu", "तापमान"), ("bhojanaṃ", "भोजन"), ("senāsanaṃ", "निवास-स्थान")]:
    noun(p, h, "m", "d", agr="msg")
noun("kāyikaṃ sukhaṃ", "शारीरिक सुख", "m", "d", agr="msg")
noun("kāyikaṃ dukkhaṃ", "शारीरिक दुःख", "m", "d", agr="msg")
noun("kāyikassa sukhassa", "शारीरिक सुख के लिए")
noun("kāyikassa dukkhassa", "शारीरिक दुःख के लिए")
noun("phalasamāpattiyā", "फल की ध्यान-अवस्था के लिए", "f", "o")
noun("phalasamāpatti", "फल की ध्यान-अवस्था", "f", "d", agr="fsg")

# sensory / consciousness
for s in S.SENSES:
    sv = {"cakkhu": "cakkhu", "sota": "sota", "ghāna": "ghāna", "jivhā": "jivhā", "kāya": "kāya"}[s]
    ay = {"cakkhu": "cakkhāyatana", "sota": "sotāyatana", "ghāna": "ghānāyatana", "jivhā": "jivhāyatana",
          "kāya": "kāyāyatana"}[s]
    ind = {"cakkhu": "cakkhundriya", "sota": "sotindriya", "ghāna": "ghānindriya", "jivhā": "jivhindriya",
           "kāya": "kāyindriya"}[s]
    A = S.AYA_SENSE(s)
    Ao = A.replace(" का ", " के ")
    noun(f"{ay}ṃ", A, "m", "d", agr="msg")
    add(f"{ay}ṃ paccayā", f"{Ao} के कारण")
    noun(f"{sv}viññāṇaṃ", S.VINNANA(s), "f", "d", agr="fsg")
    noun(f"{sv}viññāṇassa", f"{S.VINNANA(s)} के लिए", "f", "o")
    noun(f"{ind}ṃ", S.INDRIYA_SENSE(s), "f", "d", agr="fsg")
    noun(f"{ind}ñca {sv}viññāṇañca", f"{S.INDRIYA_SENSE(s)} और {S.VINNANA(s)}", "f", "d", agr="fpl")
    add(f"{sv}viññāṇasahagatānaṃ khandhānaṃ", f"{S.VINNANA(s)} के साथ होने वाले समूहों के लिए")
    add(f"{sv}viññāṇasahagataṃ ekaṃ khandhañca {ay}ñca", f"{S.VINNANA(s)} के साथ होने वाले एक समूह और {Ao}")
    add(f"dve khandhe ca {ay}ñca", f"दो समूहों और {Ao}")
    noun(f"{sv}viññāṇasahagato eko khandho ca {ay}ñca", f"{S.VINNANA(s)} के साथ होने वाला एक समूह और {A}",
         "m", "d", agr="mpl")
    add(f"{sv}viññāṇasahagato", f"{S.VINNANA(s)} के साथ होने वाला")
AYP = {"cakkhu": "cakkhāyatana", "sota": "sotāyatana", "ghāna": "ghānāyatana", "jivhā": "jivhāyatana",
       "kāya": "kāyāyatana"}
for o, s in zip(S.OBJECTS, S.SENSES):
    op = o[:-1] + "āyatana"
    noun(f"{op}ṃ", S.AYA_OBJ(o), "m", "d", agr="msg")
    noun(f"{op}ñca {AYP[s]}ñca", f"{S.AYA_OBJ(o)} और {S.AYA_SENSE(s)}", "m", "d", agr="mpl")
    noun(f"{op}ñca vatthu ca", f"{S.AYA_OBJ(o)} और आधार", "m", "d", agr="mpl")
    noun(f"{op}ñca", f"{S.AYA_OBJ(o)} और", "m", "d")
    noun(f"{op}ṃ {S.SENSE[s] and s}viññāṇassa", f"{S.AYA_OBJ(o)} {S.VINNANA(s)} के लिए", "m", "d", agr="msg")
noun("kāyassa", "शरीर के लिए", "m", "o")
add("purejātassa imassa", "पहले उत्पन्न इस")
add("=19", "=19")
add("pakatūnissayo", S.PAKATUPANISSAYA)   # spelling slip
for p, h, g in [("vicikicchaṃ", "संशय", "m"), ("uddhaccaṃ", "बेचैनी", "f"), ("domanassaṃ", "उदासी", "f"),
                ("diṭṭhiṃ", "दृष्टि", "f")]:
    noun(p, h, g, "d", num="sg", tag="acc")
noun("jhānaṅgāni", "ध्यान के अंग", "m", "o", agr="mpl")
noun("maggaṅgāni", "मार्ग के अंग", "m", "o", agr="mpl")
add("phalasamāpattiṃ samāpajjati", "फल की ध्यान-अवस्था में प्रवेश करता है")
add("anuppannaṃ samāpattiṃ uppādenti", "अब तक उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं")
add("uppannaṃ samāpattiṃ samāpajjanti", "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं")
add("ariyānaṃ atthappaṭisambhidāya dhammappaṭisambhidāya niruttippaṭisambhidāya paṭibhānappaṭisambhidāya",
    "आर्यों के अर्थ के विश्लेषणात्मक ज्ञान के लिए, परिघटनाओं के विश्लेषणात्मक ज्ञान के लिए, भाषा के "
    "विश्लेषणात्मक ज्ञान के लिए, सूझ-बूझ के विश्लेषणात्मक ज्ञान के लिए")
add("ariyānaṃ atthappaṭisambhidāya", "आर्यों के अर्थ के विश्लेषणात्मक ज्ञान के लिए")
for p, h in [("paṭhamassa", "पहले"), ("dutiyassa", "दूसरे"), ("tatiyassa", "तीसरे"), ("catutthassa", "चौथे")]:
    add(p, f"{h} के लिए")
    add(f"{p} jhānassa", f"{h} ध्यान के लिए")
    add(f"{p} maggassa", f"{h} मार्ग के लिए")
    add(f"{p} jhānassa parikammaṃ", f"{h} ध्यान की तैयारी", "noun", g="f", form="d", agr="fsg")
    add(f"{p} maggassa parikammaṃ", f"{h} मार्ग की तैयारी", "noun", g="f", form="d", agr="fsg")
for p, h in [("paṭhamaṃ jhānaṃ", "पहला ध्यान"), ("paṭhamo maggo", "पहला मार्ग"), ("dutiyo maggo", "दूसरा मार्ग"),
             ("tatiyo maggo", "तीसरा मार्ग"), ("paṭhamo", "पहला"), ("dutiyo", "दूसरा"), ("tatiyo", "तीसरा")]:
    noun(p, h, "m", "d", agr="msg")
for key in S.ARUPA_AYATANA:
    kk = key[:-1] if key.endswith("a") else key
    obl = S.ARUPA_OBL(key)
    add(f"{kk}āyatanassa parikammaṃ", f"{obl} की तैयारी", "noun", g="f", form="d", agr="fsg")
add("pāṇātipāto pāṇātipātassa", "प्राणी-हत्या प्राणी-हत्या के लिए")
add("pāṇātipāto", "प्राणी-हत्या", "noun", g="f", form="d", agr="fsg")
add("micchādiṭṭhiyā", "ग़लत दृष्टि के लिए")
add("micchādiṭṭhi micchādiṭṭhiyā", "ग़लत दृष्टि ग़लत दृष्टि के लिए")
add("byāpādassa", "दुर्भावना के लिए")
add("mātughātikammaṃ mātughātikammassa", "माता की हत्या का कर्म माता की हत्या के कर्म के लिए")
add("niyatamicchādiṭṭhiyā", "नियत ग़लत दृष्टि के लिए")
add("niyatamicchādiṭṭhi niyatamicchādiṭṭhiyā", "नियत ग़लत दृष्टि नियत ग़लत दृष्टि के लिए")
add("saṅghabhedakakammassa", "संघ में फूट डालने के कर्म के लिए")
add("akusale niruddhe", "हानिकर के समाप्त होने पर")
add("kusale niruddhe", "हितकर के समाप्त होने पर")
add("vipassanaṃ", "अंतर्दृष्टि")
add("pāṇaṃ hantvā tassa paṭighātatthāya", "प्राणी की हत्या करके उसके निवारण के लिए")
add("saṅghaṃ bhinditvā tassa paṭighātatthāya", "संघ में फूट डालकर उसके निवारण के लिए")
noun("akusalaṃ kammaṃ", "हानिकर कर्म", "m", "d", agr="msg")
noun("kusalaṃ kammaṃ", "हितकर कर्म", "m", "d", agr="msg")
noun("kammaṃ", "कर्म", "m", "d", agr="msg")
add("vipāko ca ubhayañca", "कर्म-फल रूपी और दोनों")
add("nevavipākanavipākadhamma-dhammo", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली परिघटना", "item_nom", agr="fsg")
add("adukkhamasukhāya vedanāya", "न दुःखद, न सुखद अनुभूति")
S.NUM["tevīsa"] = "तेईस"
noun("khandhā ca vatthu ca", "समूह और आधार", "m", "o", agr="mpl")
noun("tayo khandhā ca vatthu ca", "तीन समूह और आधार", "m", "o", agr="mpl")
noun("dve khandhā ca vatthu ca", "दो समूह और आधार", "m", "o", agr="mpl")
noun("khandhā ca", "समूह और", "m", "o")
noun("rūpajīvitindriyañca", S.RUPAJIVITINDRIYA, "f", "d", agr="mpl")
add("ca rūpajīvitindriyañca", "और " + S.RUPAJIVITINDRIYA, "noun", g="f", form="d", agr="mpl")
add("purimā purimā", "पहले-पहले के")
add("pacchimānaṃ pacchimānaṃ", "बाद-बाद के")
add("vicikicchāsahagate uddhaccasahagate khandhe ca vatthuñca", f"{S.KHANDHE_VU} और आधार")
add("purejāta", S.NAME("purejāta"))
add("paccayo", "कारण", "ins")
for k in K:
    add(S.COND_LOC_PALI[k], S.LOC(k))
    add(S.NEG_PREFIX_PALI[k] + S.COND_LOC_PALI[k], S.NLOC(k))
add("paṭṭhānapāḷi paṭhamo bhāgo niṭṭhito", f"“{S.BOOK_TITLE}” का पहला भाग समाप्त")
KT = "हितकर वाले तीन के वर्गीकरण"
NOTES.update({
    "Yathā kusalattike, evaṃ vitthāretabbaṃ": f"जैसे {KT} में है, वैसे ही विस्तार करना चाहिए",
    "Yathā kusalattike paccanīyānulomagaṇanā vibhattā, evaṃ vibhajitabbaṃ.":
        f"जैसे {KT} में नकारात्मक-सकारात्मक क्रम की गणना का विश्लेषण किया गया है, वैसे ही विश्लेषण करना चाहिए।",
})
for p, h in [("sota", "कान"), ("ghāna", "नाक"), ("jivhā", "जीभ"), ("kāya", "शरीर")]:
    add(p, h)
noun("kāyaviññāṇaṃ", S.VINNANA("kāya"), "f", "d", agr="fsg")
noun("sukhasahagataṃ kāyaviññāṇaṃ", f"सुख के साथ होने वाली {S.VINNANA('kāya')}", "f", "d", agr="fsg",
     num="sg", tag="acc")
noun("dukkhasahagataṃ kāyaviññāṇaṃ", f"दुःख के साथ होने वाली {S.VINNANA('kāya')}", "f", "d", agr="fsg",
     num="sg", tag="acc")
noun("sukhasahagatassa kāyaviññāṇassa", f"सुख के साथ होने वाली {S.VINNANA('kāya')} के लिए", "f", "o")
noun("dukkhasahagatassa kāyaviññāṇassa", f"दुःख के साथ होने वाली {S.VINNANA('kāya')} के लिए", "f", "o")
add("sukhasahagataṃ kāyaviññāṇasahagataṃ ekaṃ khandhaṃ",
    f"सुख के साथ होने वाले, {S.VINNANA('kāya')} के साथ होने वाले एक समूह")
add("dukkhasahagataṃ kāyaviññāṇasahagataṃ ekaṃ khandhaṃ",
    f"दुःख के साथ होने वाले, {S.VINNANA('kāya')} के साथ होने वाले एक समूह")
add("catuviññāṇasahagataṃ ekaṃ khandhaṃ", "चार प्रकार की चेतना के साथ होने वाले एक समूह")
noun("pañcaviññāṇaṃ", "पाँच प्रकार की चेतना", "f", "d", agr="fsg")
add("pañcannaṃ viññāṇānaṃ", "पाँच प्रकार की चेतनाओं के लिए")
noun("vipākamanodhātu", f"कर्म के फल रूपी {S.MANODHATU}", "m", "d", agr="msg")
noun("vipākamanodhātuyā", f"कर्म के फल रूपी {S.MANODHATU_OBL} के लिए", "m", "o")
noun("vipākamanoviññāṇadhātu", f"कर्म के फल रूपी {S.MVD}", "m", "d", agr="msg")
noun("vipākamanoviññāṇadhātuyā", f"कर्म के फल रूपी {S.MVD_OBL} के लिए", "m", "o")
noun("kiriyamanoviññāṇadhātuyā", f"केवल क्रिया रूपी {S.MVD_OBL} के लिए", "m", "o")

# javana sequence
noun("anulomaṃ", "अनुकूलता", "f", "d", agr="fsg")
noun("gotrabhu", S.GOTRABHU, "m", "d", agr="msg")
noun("maggo", "मार्ग", "m", "d", agr="msg")
noun("gotrabhussa", f"{S.GOTRABHU} के लिए", "m", "o")
noun("vodānassa", f"{S.VODANA} के लिए", "f", "o")
noun("maggassa", "मार्ग के लिए", "m", "o")
noun("phalassa", "फल के लिए", "m", "o")
noun("vuṭṭhānassa", "बाहर आने के लिए", "m", "o")
noun("cuticittaṃ", "मृत्यु का मन", "m", "d", agr="msg")
noun("upapatticittassa", "जन्म के मन के लिए", "m", "o")
noun("bhavaṅgaṃ", "जीवन-धारा", "f", "d", agr="fsg")
noun("bhavaṅgassa", "जीवन-धारा के लिए", "f", "o")
noun("āvajjanā", "मन को विषय की ओर मोड़ना", "m", "d", agr="msg")
add("āvajjanāya", S.AVAJJANA_FOR)
noun("kusalākusalaṃ", "हितकर और हानिकर", "m", "d", agr="msg")
noun("kiriyaṃ", "केवल क्रिया रूपी", "m", "d", agr="msg")
add("nirodhā vuṭṭhahantassa", "समाप्ति की ध्यान-अवस्था से उठने वाले व्यक्ति का")
for key, hk in S.ARUPA_AYATANA.items():
    obl = S.ARUPA_OBL(key)
    kk = key[:-1] if key.endswith("a") else key
    noun(f"{kk}āyatanaṃ", hk, "m", "d", agr="msg")
    noun(f"{kk}āyatanassa", f"{obl} के लिए", "m", "o")
    for q, hq in [("kusal", "हितकर"), ("vipāk", "कर्म के फल रूपी"), ("kiriy", "केवल क्रिया रूपी")]:
        noun(f"{kk}āyatana{q}aṃ", f"{obl} का {hq} मन", "m", "d", agr="msg")
        noun(f"{kk}āyatana{q}assa", f"{obl} के {hq} मन के लिए", "m", "o")
add("ñāṇalist", "")  # placeholder key (see NANA_RX)
noun("kusalākusalaṃ kammaṃ", "हितकर और हानिकर कर्म", "m", "d", agr="msg")
noun("kusalākusalaṃ kammaṃ vipākassa", "हितकर और हानिकर कर्म कर्म-फल के लिए", "m", "d", agr="msg")
noun("vipākassa", "कर्म-फल के लिए", "m", "o")

# =====================================================================================
# 5. Headings
# =====================================================================================
HEAD = {
    "Paṭiccavāro": S.VARA["paṭicca"], "Sahajātavāro": S.VARA["sahajāta"], "Paccayavāro": S.VARA["paccaya"],
    "Nissayavāro": S.VARA["nissaya"], "Saṃsaṭṭhavāro": S.VARA["saṃsaṭṭha"],
    "Sampayuttavāro": S.VARA["sampayutta"], "Pañhāvāro": S.VARA["pañhā"],
    "Vibhaṅgavāro": S.VARA["vibhaṅga"], "Saṅkhyāvāro": S.VARA["saṅkhyā"],
    "Paccayānulomaṃ": S.PACCAYANULOMA, "Paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "Paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA, "Paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA,
    "Suddhaṃ": S.SUDDHA, "Anulomaṃ": S.ANULOMA, "Paccanīyaṃ.": S.PACCANIYA + "।",
    "1-4. Paccayacatukkaṃ": "1-4. कारणों के चार क्रम",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Sabhāgaṃ": "सहभागी कारण",
    "2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        "2-6 सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "Ghaṭanā": "संयोजन",
    "Sāmaññaghaṭanā": "सामान्य संयोजन",
    "Pakiṇṇakaghaṭanā": "मिश्रित संयोजन",
    "Saindriya-maggaghaṭanā": f"{S.NAME('indriya')} और {S.NAME('magga')} सहित संयोजन",
    "Sādhipati-indriya-maggaghaṭanā": f"{S.NAME('adhipati')}, {S.NAME('indriya')} और {S.NAME('magga')} सहित संयोजन",
}
GROUPW = dict(S.GROUP)
GROUPW.update({"chakkaṃ": 6, "navakaṃ": 9, "dasakaṃ": 10, "catuvīsakaṃ": 24})
CSTEM = sorted(K, key=len, reverse=True)


def cond_names(spec):
    """'Napacchājāta-naāsevanapaccayā' / 'Ārammaṇapaccayādi' -> Hindi names joined."""
    s = spec
    adi = False
    for suf in ("paccayādi", "ādipaccayā", "ādi"):
        if s.endswith(suf):
            s, adi = s[: -len(suf)], True
            break
    s = re.sub(r"paccay[oā]$", "", s)
    parts = s.split("-")
    names = []
    for p in parts:
        p = norm(p)
        neg = False
        m = re.match(r"^(na|no)(.+)$", p)
        if m and m.group(2) in K:
            neg, p = True, m.group(2)
        if p == "vigatāvigata":
            names += [S.NAME("vigata"), S.NAME("avigata")]
            continue
        if p not in K:
            return None
        names.append(S.NNAME(p) if neg else S.NAME(p))
    if len(names) == 1:
        res = names[0]
    else:
        res = ", ".join(names[:-1]) + " और " + names[-1]
    return res + (" आदि" if adi else "")


def head_hi(text, code):
    t = text.strip()
    if t in HEAD:
        return HEAD[t]
    m = re.fullmatch(r"(.+?)( \(\d+\))", t)
    if m and m.group(1) in HEAD:
        return HEAD[m.group(1)] + m.group(2)
    if m:
        h = head_hi(m.group(1), code)
        return None if h is None else h + m.group(2)
    if t.endswith("ttikaṃ"):
        return S.TIKA(TIKA_NAME[code])
    low = norm(t)
    m = re.fullmatch(r"(.+?)( \((saupanissayaṃ|sakammaṃ)\))?", low)
    base, tag = m.group(1), m.group(3)
    tagh = {None: "", "saupanissayaṃ": f" ({S.NAME('upanissaya')} सहित)", "sakammaṃ": f" ({S.NAME('kamma')} सहित)"}[tag]
    if base in GROUPW:
        return S.GROUP_HI(GROUPW[base]) + tagh
    # X(ādi)dukaṃ / X(ādi)dukāni
    m = re.fullmatch(r"(na|no)?(.+?)(ādi)?duk(aṃ|āni)", base)
    if m and m.group(2) not in K and m.group(2) + "a" in K:
        k = m.group(2) + "a"
        h = S.DUKANI(k, neg=bool(m.group(1)), plural=(m.group(4) == "āni"))
        nm = S.NNAME_OBL(k) if m.group(1) else S.NAME(k)
        return h.replace(nm, nm + " आदि", 1) if m.group(3) else h
    if m and m.group(2) in K:
        k = m.group(2)
        h = S.DUKANI(k, neg=bool(m.group(1)), plural=(m.group(4) == "āni"))
        if m.group(3):
            nm = S.NNAME_OBL(k) if m.group(1) else S.NAME(k)
            h = h.replace(nm, nm + " आदि", 1)
        return h
    m = re.fullmatch(r"(.+?)(ādi)?sabhāgaṃ", base)
    if m:
        k = m.group(1) if m.group(1) in K else (m.group(1) + "a" if m.group(1) + "a" in K else None)
        if k:
            return f"{S.NAME(k)}{' आदि' if m.group(2) else ''} के सहभागी कारण"
    m = re.fullmatch(r"(.+?)sāmaññaghaṭanā", base)
    if m and m.group(1) in K:
        return f"{S.NAME(m.group(1))} के सामान्य संयोजन"
    m = re.fullmatch(r"(.+?)ghaṭanā", base)
    if m and m.group(1) in K:
        return f"{S.NAME(m.group(1))} वाले संयोजन"
    m = re.fullmatch(r"(na)?(.+?)mūlakaṃ(\.)?", base)
    if m and m.group(2) in K:
        return S.MULAKA(m.group(2), neg=bool(m.group(1))) + ("।" if m.group(3) else "")
    c = cond_names(t)
    if c:
        return c
    return None


# =====================================================================================
# 6. Counting lines and ghaṭanā lines
# =====================================================================================
def ghatana_names(comp):
    s = comp.replace(" -", "-").replace("- ", "-")
    if s.endswith("nti"):
        s = s[:-3]
    elif s.endswith("īti"):
        s = s[:-3] + "i"
    s = norm(s).replace("-", "").replace("sahajātaṃ", "sahajāta")
    s = s.replace("ārammaṇādhipati", "ārammaṇaadhipati").replace("adhipatī", "adhipati")
    out, i = [], 0
    while i < len(s):
        for k in CSTEM:
            if s.startswith(k, i):
                out.append(k)
                i += len(k)
                break
        else:
            return None
    names = [S.NAME(k) for k in out]
    return ", ".join(names[:-1]) + " और " + names[-1]


GH_RX = re.compile(r"([A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]+(?:\s?-\s?[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]+)+(?:nti|ti))")


def ghatana_line(body):
    """'Hetu-…-avigatanti tīṇi. Hetu-…nti dve.' and 'Hetu-…nti naārammaṇe tīṇi…'"""
    if not GH_RX.search(body):
        return None
    trail = ""
    m = re.fullmatch(r"(.*?)((?:\s*\([^()]*\)\.?)+)", body)
    if m and m.group(1).strip():
        body, trail = m.group(1), m.group(2)
        r = ghatana_line(body)
        return None if r is None else r + tr_trail(trail)
    parts = GH_RX.split(body)
    out = ""
    for idx, p in enumerate(parts):
        if idx % 2 == 1:
            nm = ghatana_names(p)
            if nm is None:
                return None
            out += nm + " के संयोजन"
        else:
            if idx == 0:
                if p.strip():
                    return None
                continue
            rest = p.strip()
            # rest like "tīṇi. " or "dve " or "naārammaṇe tīṇi…pe… novigate tīṇi."
            m = re.fullmatch(r"(ekaṃ|dve|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava)(\.?)", rest)
            if m:
                out += f" में {S.NUM[m.group(1)]}" + ("।" if m.group(2) else "") + (" " if idx < len(parts) - 1 else "")
            else:
                try:
                    out += " से, " + S.count_hi(rest) + (" " if idx < len(parts) - 1 else "")
                except ValueError:
                    return None
    return out.rstrip()


NEGSTEM_RX = re.compile(r"(na|no)(" + "|".join(CSTEM) + ")")


def expand_neg_compound(m):
    """'naārammaṇa-naadhipati-…-noatthipaccayā' -> 'naārammaṇapaccayā naadhipatipaccayā …'."""
    s = m.group(0)[: -len("paccayā")].replace("-", "")
    parts = []
    pos = 0
    while pos < len(s):
        mm = NEGSTEM_RX.match(s, pos)
        if not mm:
            return m.group(0)
        parts.append(mm.group(1) + mm.group(2) + "paccayā")
        pos = mm.end()
    return " ".join(parts)


def count_line(body):
    if "{" in body or body.lstrip().startswith("("):
        return None
    body = re.sub(r"\S*-\S*paccayā", expand_neg_compound, body)
    pieces = re.split(r"(\s*\([^()]*\)\.?)", body)
    out = ""
    for p in pieces:
        if not p.strip():
            continue
        if p.strip().startswith("("):
            out += tr_trail(p)
            continue
        try:
            h = S.count_hi(p.strip())
        except ValueError:
            return None
        out += (" " if out else "") + h
    return out.strip() or None


KT = "हितकर वाले तीन के वर्गीकरण"
EXACT.update({
    "Anulomaṃ.": S.ANULOMA + "।", "Paccanīyaṃ.": S.PACCANIYA + "।", "Paccanīyaṃ": S.PACCANIYA,
    "Anulomapaccanīyaṃ.": S.ANULOMAPACCANIYA + "।", "Paccanīyānulomaṃ.": S.PACCANIYANULOMA + "।",
    "Anulomagaṇanā.": f"{S.ANULOMA} की गणना।", "Paccanīyagaṇanā.": f"{S.PACCANIYA} की गणना।",
    "Anulomapaccanīyagaṇanā.": f"{S.ANULOMAPACCANIYA} की गणना।",
    "Pañhāvārassa anulomaṃ.": f"{S.VARA['pañhā']} का {S.ANULOMA}।",
    "Nahetumūlakaṃ.": S.MULAKA("hetu", neg=True) + "।",
    "Paṭiccavāro.": S.VARA["paṭicca"] + "।", "Sahajātavāro.": S.VARA["sahajāta"] + "।",
    "Paccayavāro.": S.VARA["paccaya"] + "।", "Nissayavāro.": S.VARA["nissaya"] + "।",
    "Saṃsaṭṭhavāro.": S.VARA["saṃsaṭṭha"] + "।", "Sampayuttavāro.": S.VARA["sampayutta"] + "।",
    "Vedanāttikaṃ niṭṭhitaṃ.": f"{S.TIKA('अनुभूति')} समाप्त।",
    "Vipākattikaṃ niṭṭhitaṃ.": f"{S.TIKA('कर्म-फल')} समाप्त।",
    "Upādinnattikaṃ niṭṭhitaṃ.": f"{S.TIKA('कर्म से उत्पन्न')} समाप्त।",
    "Saṃkiliṭṭhattikaṃ niṭṭhitaṃ.": f"{S.TIKA('क्लेशों से मलिन')} समाप्त।",
})
NOTES.update({
    "Yathā kusalattikassa paccayagaṇanā, evaṃ vitthāretabbā": f"जैसे {KT} में कारणों की गणना है, वैसे ही विस्तार करना चाहिए",
    "Yathā kusalattikaṃ, evaṃ gaṇetabbaṃ.": f"जैसे {KT} में है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattikassa paccanīyagaṇanā gaṇitā, evaṃ idampi asammuyhantena sabbaṃ mūlakaṃ gaṇetabbaṃ {gahetabbaṃ (syā.)}.":
        f"जैसे {KT} में नकारात्मक क्रम की गणना की गई है, वैसे ही यहाँ भी बिना भ्रमित हुए हर शृंखला को गिनना चाहिए [पाठभेद (Syā.): gahetabbaṃ]।",
    "Yathā kusalattikassa anulomapaccanīyagaṇanā sajjhāyamaggena gaṇitā, evaṃ idampi gaṇetabbaṃ.":
        f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना पाठ के क्रम से की गई है, वैसे ही यहाँ भी गिनना चाहिए।",
    "Yathā kusalattikassa paccanīyānulomagaṇanā sajjhāyamaggena gaṇitā, evaṃ gaṇetabbaṃ.":
        f"जैसे {KT} में नकारात्मक-सकारात्मक क्रम की गणना पाठ के क्रम से की गई है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattikassa gaṇanā, evaṃ gaṇetabbaṃ.": f"जैसे {KT} में गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike sajjhāyamaggena gaṇitaṃ, evaṃ idhāpi gaṇetabbaṃ.":
        f"जैसे {KT} में पाठ के क्रम से गिना गया है, वैसे ही यहाँ भी गिनना चाहिए।",
    "Yathā kusalattike anulomapaccanīyagaṇanā gaṇitā, evaṃ gaṇetabbaṃ.":
        f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना की गई है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike nahetumūlakaṃ gaṇitaṃ, evaṃ gaṇetabbaṃ. Yathā kusalattike paccanīyānulomaṃ vitthāritaṃ, evaṃ idaṃ vitthāretabbaṃ.":
        f"जैसे {KT} में {S.MULAKA('hetu', neg=True)} को गिना गया है, वैसे ही गिनना चाहिए। "
        f"जैसे {KT} में {S.PACCANIYANULOMA} का विस्तार किया गया है, वैसे ही इसका विस्तार करना चाहिए।",
    "Yathā kusalattike gaṇanā, evaṃ gaṇetabbaṃ.": f"जैसे {KT} में गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike gaṇanā, evaṃ gaṇetabbā.": f"जैसे {KT} में गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike gaṇanā evaṃ gaṇetabbā.": f"जैसे {KT} में गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike paccanīyagaṇanā, evaṃ gaṇetabbaṃ.":
        f"जैसे {KT} में नकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike anulomapaccanīyagaṇanā, evaṃ gaṇetabbaṃ.":
        f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike anulomapaccanīyagaṇanā, evaṃ gaṇetabbā.":
        f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike paccanīyānulomagaṇanā, evaṃ gaṇetabbaṃ.":
        f"जैसे {KT} में नकारात्मक-सकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike paccanīyānulomagaṇanā, evaṃ gaṇetabbā.":
        f"जैसे {KT} में नकारात्मक-सकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike pañhāvārassa anulomagaṇanā gaṇitā, evaṃ vitthāretabbā.":
        f"जैसे {KT} में प्रश्नों के खंड के सकारात्मक क्रम की गणना की गई है, वैसे ही विस्तार करना चाहिए।",
    "Yathā kusalattike paccanīyagaṇanā vitthāritā, evaṃ vitthāretabbaṃ.":
        f"जैसे {KT} में नकारात्मक क्रम की गणना का विस्तार किया गया है, वैसे ही विस्तार करना चाहिए।",
    "Yathā kusalattike anulomapaccanīyagaṇanā vitthāritā evaṃ vitthāretabbaṃ. Asammohantena eso sajjhāyamaggo.":
        f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना का विस्तार किया गया है, वैसे ही विस्तार करना चाहिए। "
        f"बिना भ्रमित हुए यही पाठ का क्रम है।",
    "Yathā kusalattike paccanīyānulomagaṇanā vitthāritā, evaṃ vitthāratabbaṃ.":
        f"जैसे {KT} में नकारात्मक-सकारात्मक क्रम की गणना का विस्तार किया गया है, वैसे ही विस्तार करना चाहिए।",
    "Yathā kusalattikassa paṭiccavāro sajjhāyamaggena vitthārito, evaṃ vitthāretabbaṃ.":
        f"जैसे {KT} के {S.VARA['paṭicca']} का पाठ के क्रम से विस्तार किया गया है, वैसे ही विस्तार करना चाहिए।",
    "Yathā kusalattike paṭiccagaṇanā sajjhāyamaggena gaṇitā, evaṃ gaṇetabbaṃ.":
        f"जैसे {KT} में {S.VARA['paṭicca']} की गणना पाठ के क्रम से की गई है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike paccanīyavāro vitthārito, evaṃ vitthāretabbo.":
        f"जैसे {KT} में {S.PACCANIYA} के खंड का विस्तार किया गया है, वैसे ही विस्तार करना चाहिए।",
    "Yathā kusalattike vibhattaṃ, evaṃ vibhajitabbaṃ.":
        f"जैसे {KT} में विश्लेषण किया गया है, वैसे ही विश्लेषण करना चाहिए।",
    "adhipatiyā paṭisandhi natthi": f"{S.LOC('adhipati')} पुनर्जन्म नहीं है",
    "adhipatiyā paṭisandhikkhaṇe natthi": f"{S.LOC('adhipati')} पुनर्जन्म का क्षण नहीं है",
    "nādhipati paripuṇṇaṃ paṭisandhikaṃ": f"{S.NNAME('adhipati')} पुनर्जन्म सहित पूरा है",
    "napacchājātampi naāsevanampi paripuṇṇaṃ paṭisandhikaṃ":
        f"{S.NNAME('pacchājāta')} भी और {S.NNAME('āsevana')} भी पुनर्जन्म सहित पूरे हैं",
    "Dukkhāya vedanāya sampayuttapaṭisandhi na labbhati.": "दुःखद अनुभूति से जुड़ा पुनर्जन्म नहीं मिलता।",
    "aññamaññampi nissayampi sahajātapaccayasadisaṃ":
        f"{S.NAME('aññamañña')} भी और {S.NAME('nissaya')} भी {S.SADISA('sahajāta')} हैं",
    "mūlakaṃ saṃkhittaṃ": "शृंखला संक्षिप्त",
    "sahajātaṃ sabbaṃ hetupaccayasadisaṃ": f"{S.NAME('sahajāta')} पूरा का पूरा {S.SADISA('hetu')} है",
    "sahajāte idaṃ nānākaraṇaṃ": f"{S.LOC('sahajāta')} यह अंतर है",
    "Saṃkhittaṃ. Yathā anulomaṃ sahajātasadisaṃ.":
        f"संक्षिप्त। जैसे {S.ANULOMA} में, वैसे ही {S.SADISA('sahajāta')} है।",
    "idaṃ nānattaṃ": "यह अंतर है",
    "hetupaccayasadisā nava": f"{S.SADISA('hetu')} नौ",
    "paṭisandhi paripuṇṇaṃ": "पुनर्जन्म पूरा है",
    "Paṭiccavāropi sahajātavāropi sadiso.": f"{S.VARA['paṭicca']} भी और {S.VARA['sahajāta']} भी एक समान हैं।",
    "Paccayavāropi nissayavāropi sadiso": f"{S.VARA['paccaya']} भी और {S.VARA['nissaya']} भी एक समान हैं",
    "Saṃsaṭṭhavāropi sampayuttavāropi sadiso.": f"{S.VARA['saṃsaṭṭha']} भी और {S.VARA['sampayutta']} भी एक समान हैं।",
    "Catuvīsatipaccayā vitthāretabbā, avigatapaccayā.":
        f"चौबीस कारणों का विस्तार करना चाहिए, {S.NAME('avigata')} तक।",
    "Sabbāni padāni vitthāretabbāni.": "सभी पदों का विस्तार करना चाहिए।",
    "saṃkhittaṃ. Sabbāni padāni vitthāretabbāni.": "संक्षिप्त। सभी पदों का विस्तार करना चाहिए।",
    "Sabbāni padāni vibhajitabbāni.": "सभी पदों का विश्लेषण करना चाहिए।",
    "vitthārena gaṇetabbaṃ": "विस्तार से गिनना चाहिए",
    "Vitthārena gaṇetabbaṃ.": "विस्तार से गिनना चाहिए।",
    "Paṭisandhipi imesaṃ tiṇṇannaṃ kātabbā.": "इन तीनों में पुनर्जन्म भी जोड़ना चाहिए।",
    "paṭisandhi kātabbā {kātabbaṃ (sī.)}.": "पुनर्जन्म जोड़ना चाहिए [पाठभेद (Sī.): kātabbaṃ]।",
    "Natthi-vigataṃ anantarasadisaṃ, avigataṃ atthisadisaṃ.":
        f"{S.NAME('natthi')} और {S.NAME('vigata')} {S.SADISA('anantara')} हैं, "
        f"{S.NAME('avigata')} {S.SADISA('atthi')} है।",
    "Satta pañhā": "सात प्रश्न", "Terasa pañhā": "तेरह प्रश्न", "Ekā pañhā.": "एक प्रश्न।",
    "anantarasadisaṃ. Saṃkhittaṃ": f"{S.SADISA('anantara')} है। संक्षिप्त",
    'saddhāpañcamakesu "mānaṃ jappeti, diṭṭhiṃ gaṇhātī"ti kātabbaṃ, avasesesu na kātabbaṃ':
        "श्रद्धा आदि पाँच में “अहंकार पालता है, दृष्टि ग्रहण करता है” जोड़ना चाहिए, बाकी में नहीं जोड़ना चाहिए",
    "Saṃkhittaṃ.": "संक्षिप्त।", "saṃkhittaṃ.": "संक्षिप्त।",
    "Saṃkhittaṃ. Sabbāni padāni vitthāretabbāni.": "संक्षिप्त। सभी पदों का विस्तार करना चाहिए।",
    "Yathā kusalattike anulomapaccanīyagaṇanā vibhattā, evaṃ gaṇetabbā.":
        f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना का विश्लेषण किया गया है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike paccanīyānulomagaṇanā vibhattā, evaṃ gaṇetabbā.":
        f"जैसे {KT} में नकारात्मक-सकारात्मक क्रम की गणना का विश्लेषण किया गया है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike anulomapaccanīyagaṇanā vibhattā, evaṃ vibhajitabbaṃ.":
        f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना का विश्लेषण किया गया है, वैसे ही विश्लेषण करना चाहिए।",
    "Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo.":
        f"{S.VARA['sahajāta']} भी, {S.VARA['paccaya']} भी, {S.VARA['nissaya']} भी, {S.VARA['saṃsaṭṭha']} भी "
        f"और {S.VARA['sampayutta']} भी विस्तार से कहना चाहिए।",
    "Yathā kusalattikassa gaṇanā sajjhāyamaggena gaṇitā, evaṃ gaṇetabbā. Kusalattikassa gaṇanato upādinnattike "
    "gaṇanā gambhīrā sukhumatarā ca, evaṃ kātūna asammohantena gaṇetabbaṃ.":
        f"जैसे {KT} की गणना पाठ के क्रम से की गई है, वैसे ही गिनना चाहिए। {KT} की गणना की तुलना में "
        f"{S.TIKA('कर्म से उत्पन्न').replace('वाला तीन का', 'वाले तीन के')} में गणना गहरी और अधिक सूक्ष्म है, "
        f"ऐसा करके बिना भ्रमित हुए गिनना चाहिए।",
    "Avipākaṃ – 4": f"{S.NAME('vipāka')} रहित – 4",
    "Savipākaṃ – 5": f"{S.NAME('vipāka')} सहित – 5",
})


def tr_trail(trail):
    out = ""
    for t, sp in tokens(trail):
        if t.startswith("("):
            out += (" " if sp or out else " ") + render_paren(t, {})
        elif t == ".":
            out += "।"
        else:
            return out + " ??" + t
    return out


# =====================================================================================
# 7. File assembly
# =====================================================================================
ID_RX = S.ID_RX
HEAD_RX = re.compile(r"^(#+) (\*?)(.+?)(\*?)$")


def tr_line(line, code, table):
    m = ID_RX.search(line)
    body = ID_RX.sub("", line) if m else line
    hm = HEAD_RX.match(body)
    if hm:
        h = head_hi(hm.group(3).strip("*"), code)
        if h is None:
            UNKNOWN["HEAD:" + hm.group(3)] += 1
            h = "??" + hm.group(3)
        return f"{hm.group(1)} {hm.group(2)}{h}{hm.group(4)}"
    if body in EXACT:
        return EXACT[body]
    g = ghatana_line(body)
    if g is not None:
        return g
    c = count_line(body)
    if c is not None:
        return c
    return tr(body, table, ctx=body[:100]).replace(",।", "।")   # 1-03 "uppajjati,." punctuation slip


def build(fname):
    code = fname[:4]
    table = item_phrases(code)
    ptxt = (PALI_DIR / fname).read_text(encoding="utf-8")
    hi = []
    for line in ptxt.splitlines():
        if line.strip():
            hi.append(tr_line(line, code, table))
    return S.assemble(ptxt, hi)


def main():
    dry = "--dry" in sys.argv
    outs = {f: build(f) for f in FILES}
    if UNKNOWN:
        print("UNKNOWN:", len(UNKNOWN))
        for u, c in UNKNOWN.most_common(int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 60):
            print(f"{c:4d} | {u} || {UNK_CTX.get(u, '')[:90]}")
            if "--all" in sys.argv:
                for x in sorted(set(UNK_ALL.get(u, [])))[:8]:
                    print("        ~", x)
    if not dry:
        for f, t in outs.items():
            with open(HI_DIR / f, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(t)
            print("wrote", f)


if __name__ == "__main__":
    main()
