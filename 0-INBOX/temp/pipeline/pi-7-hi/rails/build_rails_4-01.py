"""pi-7 Paṭṭhāna 4-01 (Kilesagocchaka + Piṭṭhiduka), Hindi plain RAILS builder.

Imports the approved sample builder read-only (constants only) and adds the dyad items and clauses of 4-01.
Run:  python -I -B -X utf8 build_rails_4-01.py        (writes the output file, lists unknown pieces)
"""
import os
import re
import sys
from collections import Counter

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails"
sys.path.insert(0, RAILS)
import build_rails_sample as S  # noqa: E402  (read-only)
from vocab_4_01 import (HEAD_X, ITEMS, ITEMS_D, NOUNS, NOM_X, OBL_X, DAT_X, PREFIX_X, CLAUSE_X, NOTE_X,  # noqa: E402
                        LINE_X, VARIANTS_X, SLIPS_X)

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
SRC = ROOT + r"\AI_translation\pali\pi-7_split_chapters\4-01-kilesagocchaka.md"
DST = ROOT + r"\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\4-01-kilesagocchaka.md"

# ---------------------------------------------------------------- headings
HEAD = dict(S.HEAD)
HEAD.update(HEAD_X)
for _k in S.KEYS:
    _n = ("no" if _k in ("atthi", "natthi", "vigata", "avigata") else "na") + _k
    HEAD.setdefault(_k[0].upper() + _k[1:] + "paccayādi", S.NAME[_k] + " आदि")
    HEAD.setdefault(_n[0].upper() + _n[1:] + "paccayādi", S.NNAME[_k] + " आदि")
    HEAD.setdefault(_n[0].upper() + _n[1:] + "dukaṃ", S.NDUKA[_k])


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)(\(\d+\.?\) |\d+-\d+\. )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    if body not in HEAD:
        raise KeyError("HEAD: " + body)
    return f"{hashes} {st}{num or ''}{HEAD[body]}{en}"


# ---------------------------------------------------------------- dyad items
FEM2M = [("वाली", "वाला", "वाले"), ("जुड़ी", "जुड़ा", "जुड़े"), ("समाई", "समाया", "समाए"), ("हुई", "हुआ", "हुए"),
         ("छोड़ी", "छोड़ा", "छोड़े")]


def masc(h, oblique):
    for f, ms, mo in FEM2M:
        h = re.sub(rf"(?<!\S){f}(?!\S)", mo if oblique else ms, h)
    return h


def simple(words, end):
    ws = words.split()
    idx = [i for i, w in enumerate(ws) if not w.startswith("=")]
    out = []
    for i, w in enumerate(ws):
        w = w.lstrip("=")
        out.append(w[:-1] + end if i in idx else w)
    return " ".join(out)


def forms(spec):
    """Pāli case forms of a dyad item. spec: 'stem words' ('=' marks a word that does not inflect),
    ('both', A, B) = A ceva B ca, ('butnot', Y, X) = Y ceva no ca X."""
    E = {"acc": "aṃ", "nom": "o", "dat": "assa", "accpl": "e", "nompl": "ā", "genpl": "ānaṃ", "adh": "ādhipati"}
    if isinstance(spec, str):
        return {c: simple(spec, e) for c, e in E.items()}
    kind, a, b = spec
    if kind == "both":
        return {"acc": f"{a[:-1]}añceva {b[:-1]}añca", "nom": f"{a[:-1]}o ceva {b[:-1]}o ca",
                "dat": f"{a[:-1]}assa ceva {b[:-1]}assa ca", "accpl": f"{a[:-1]}e ceva {b[:-1]}e ca",
                "nompl": f"{a[:-1]}ā ceva {b[:-1]}ā ca", "genpl": f"{a[:-1]}ānañceva {b[:-1]}ānañca",
                "adh": f"{a[:-1]}ā ceva {b[:-1]}ādhipati"}
    return {"acc": f"{a[:-1]}añceva no ca {b[:-1]}aṃ", "nom": f"{a[:-1]}o ceva no ca {b[:-1]}o",
            "dat": f"{a[:-1]}assa ceva no ca {b[:-1]}assa", "accpl": f"{a[:-1]}e ceva no ca {b[:-1]}e",
            "nompl": f"{a[:-1]}ā ceva no ca {b[:-1]}ā", "genpl": f"{a[:-1]}ānañceva no ca {b[:-1]}ānaṃ",
            "adh": f"{a[:-1]}ā ceva no ca {b[:-1]}ādhipati"}


ACC, NOMI, DATI = {}, {}, {}     # item + dhammaṃ / dhammo / dhammassa
NOM = dict(NOM_X)                 # nominative NPs: pali -> (hindi, gender)
OBL = dict(OBL_X)                 # accusative NPs (object of paṭicca etc.): pali -> hindi oblique
DAT = dict(DAT_X)                 # dative NPs: pali -> hindi oblique (without «के लिए»)


def one_khandha(h):
    return f"एक {h} समूह" if " " not in h else f"{h} एक समूह"


def is_compound(h):
    return " और " in h or "," in h


ITEM_H = {}
for spec, hf in ITEMS:
    F = forms(spec)
    hmo, hms = masc(hf, True), masc(hf, False)
    ITEM_H[F["acc"]] = hf
    ACC[F["acc"]] = f"{hf} परिघटना"
    NOMI[F["nom"]] = (f"{hf} परिघटना", "fs")
    DATI[F["dat"]] = f"{hf} परिघटना के लिए"
    OBL.setdefault(f"{F['acc']} ekaṃ khandhaṃ", one_khandha(hmo))
    OBL.setdefault(f"ahetukaṃ {F['acc']} ekaṃ khandhaṃ", "मूल से रहित, " + one_khandha(hmo))
    OBL.setdefault(f"{F['accpl']} khandhe", f"{hmo} समूहों")
    OBL.setdefault(f"ahetuke {F['accpl']} khandhe", f"मूल से रहित, {hmo} समूहों")
    NOM.setdefault(f"{F['nompl']} khandhā", (f"{hmo} समूह", "mp"))
    NOM.setdefault(f"ahetukā {F['nompl']} khandhā", (f"मूल से रहित, {hmo} समूह", "mp"))
    NOM.setdefault(f"purimā purimā {F['nompl']} khandhā", (f"पहले-पहले के {hmo} समूह", "mp"))
    NOM.setdefault(f"{F['nompl']} hetū", (f"{hmo} मूल", "mp"))
    NOM.setdefault(f"{F['nompl']} cetanā", (f"{hms} इरादा", "ms"))
    NOM.setdefault(f"{F['nom']} eko khandho", (f"{hms} एक समूह", "ms"))
    NOM.setdefault(F["adh"], (f"{hf} प्रधानता", "fs"))
    DAT.setdefault(f"{F['genpl']} khandhānaṃ", f"{hmo} समूहों")
    DAT.setdefault(f"pacchimānaṃ pacchimānaṃ {F['genpl']} khandhānaṃ", f"बाद-बाद के {hmo} समूहों")

# plain nouns, item adjective + noun, «purimā purimā» / «pacchimānaṃ pacchimānaṃ», adverbs «Xena cittena»
ADV = {}
ADJ_END = {"m": ("o", "aṃ", "assa"), "f": ("ā", "aṃ", "āya"), "n": ("aṃ", "aṃ", "assa")}
PURIMA = {"m": "purimo purimo", "f": "purimā purimā", "n": "purimaṃ purimaṃ"}
PACCHIMA = {"m": "pacchimassa pacchimassa", "f": "pacchimāya pacchimāya", "n": "pacchimassa pacchimassa"}
GEN_POST = {"m": "का", "f": "की"}


def add_noun(pn, pa, pd, pg, hd, ho, hg, adj_f=None):
    """pn/pa/pd: Pāli nom/acc/dat; pg: Pāli gender; hd/ho: Hindi direct/oblique; hg: Hindi gender (m/f)."""
    NOM.setdefault(pn, (hd, hg + "s"))
    OBL.setdefault(pa, ho)
    DAT.setdefault(pd, ho)
    NOM.setdefault(f"{PURIMA[pg]} {pn}", (f"पहले-पहले {GEN_POST[hg]} {hd}", hg + "s"))
    DAT.setdefault(f"{PACCHIMA[pg]} {pd}", f"बाद-बाद {'के' if hg == 'm' else 'की'} {ho}")


ABL_ADJ = {}
CETO = {}
SUBJ_H = {"ariyā": "आर्य", "sekkhā": S.SEKKHA, "arahā": S.ARAHA}
for _n in NOUNS:
    add_noun(*_n)
for spec, hf in ITEMS:
    if not isinstance(spec, str):
        continue
    hmo, hms = masc(hf, True), masc(hf, False)
    ADV[simple(spec, "ena") + " cittena"] = f"{hmo} मन से"
    ABL_ADJ[simple(spec, "ā")] = hmo
    for _v, _vh in (("jānāti", "जानता है"), ("jānanti", "जानते हैं")):
        CETO[f"cetopariyañāṇena {simple(spec, 'a')}cittasamaṅgissa cittaṃ {_v}"] = \
            f"{S.CETOPARIYA} {hmo} मन से युक्त व्यक्ति के मन को {_vh}"
    for pn, pa, pd, pg, hd, ho, hg in NOUNS:
        e_n, e_a, e_d = ADJ_END[pg]
        an, aa, ad = simple(spec, e_n), simple(spec, e_a), simple(spec, e_d)
        if hg == "f":
            add_noun(f"{an} {pn}", f"{aa} {pa}", f"{ad} {pd}", pg, f"{hf} {hd}", f"{hf} {ho}", hg)
        else:
            add_noun(f"{an} {pn}", f"{aa} {pa}", f"{ad} {pd}", pg, f"{hms} {hd}", f"{hmo} {ho}", hg)
# two adjectives before khandha (vipākaṃ nakāmāvacaraṃ ekaṃ khandhaṃ …)
for pre_spec, pre_h in (("vipāka", "कर्म-फल रूपी"), ("ahetuka", "मूल से रहित")):
    for spec, hf in ITEMS:
        if not isinstance(spec, str) or spec == pre_spec:
            continue
        F = forms(spec)
        hmo = masc(hf, True)
        P = forms(pre_spec)
        OBL.setdefault(f"{P['acc']} {F['acc']} ekaṃ khandhaṃ", f"{pre_h}, " + one_khandha(hmo))
        OBL.setdefault(f"{P['accpl']} {F['accpl']} khandhe", f"{pre_h}, {hmo} समूहों")
        NOM.setdefault(f"{P['nompl']} {F['nompl']} khandhā", (f"{pre_h}, {hmo} समूह", "mp"))
        DAT.setdefault(f"{P['genpl']} {F['genpl']} khandhānaṃ", f"{pre_h}, {hmo} समूहों")

# «X-assa parikammaṃ» = «X की प्रारंभिक तैयारी»
for _d in list(DAT):
    if re.search(r"(jhānassa|ñāṇassa|āyatanassa|cakkhussa|sotadhātuyā|maggassa)$", _d):
        NOM.setdefault(f"{_d} parikammaṃ", (f"{DAT[_d]} की प्रारंभिक तैयारी", "fs"))

# pairs of the two items of each dyad (and the 'both'/'butnot' pairs)
PAIRS = list(ITEMS_D)


def _ca_acc(a):
    return a[:-1] + "ñca" if a.endswith("aṃ") else a


def _ca(a):
    return a if a.endswith(" ca") else a + " ca"


for (sa, ha), (sb, hb) in PAIRS:
    Fa, Fb = forms(sa), forms(sb)
    ACC[f"{_ca_acc(Fa['acc'])} {_ca_acc(Fb['acc'])}"] = f"{ha} परिघटना और {hb} परिघटना"
    if is_compound(ha) or is_compound(hb):
        NOMI[f"{_ca(Fa['nom'])} {_ca(Fb['nom'])}"] = (f"{ha} परिघटना और {hb} परिघटना", "fp")
    else:
        NOMI[f"{_ca(Fa['nom'])} {_ca(Fb['nom'])}"] = (f"{ha} और {hb} परिघटनाएँ", "fp")
    DATI[f"{_ca(Fa['dat'])} {_ca(Fb['dat'])}"] = f"{ha} परिघटना और {hb} परिघटना के लिए"
    # ^7-35-91 (Pāli line 623): the final «ca» is missing; same meaning
    DATI.setdefault(f"{_ca(Fa['dat'])} {Fb['dat']}", f"{ha} परिघटना और {hb} परिघटना के लिए")

NITTHITA = {"Dhammānulome dukapaṭṭhānaṃ": "परिघटनाओं के सकारात्मक क्रम में दो-दो के वर्गीकरणों के कारण-संबंध"}
for spec, hf in ITEMS:
    if isinstance(spec, str):
        DAT.setdefault(forms(spec)["dat"], masc(hf, True))
        OBL.setdefault("ahetukaṃ " + forms(spec)["acc"], "मूल से रहित, " + masc(hf, True))
        OBL.setdefault(forms(spec)["accpl"] + " pahīne kilese", masc(hf, True) + ", छोड़े जा चुके मन के क्लेशों")

PREFIX = dict(S.PREFIX)
PREFIX.update(PREFIX_X)
CLAUSE = {k: v for k, v in S.CLAUSE.items()}
CLAUSE.update(CETO)
CLAUSE.update(CLAUSE_X)
NOTE = dict(NOTE_X)

# ---------------------------------------------------------------- NP lists


def norm_words(text):
    """Split the enclitic: 'khandhañca' -> 'khandhaṃ ca' (not '-ñceva')."""
    out = []
    for w in text.split():
        if w.endswith("ñca") and len(w) > 3:
            out += [w[:-3] + "ṃ", "ca"]
        else:
            out.append(w)
    return out


NORMD = {}


def normd(D):
    """D keyed by normalised Pāli (cached by id)."""
    if id(D) not in NORMD:
        NORMD[id(D)] = {" ".join(norm_words(k)): k for k in D}
    return NORMD[id(D)]


def np_parse(words, D):
    """Greedy longest-match parse of a word list into NPs of dictionary D; 'ca' and '¦' are separators,
    a 'ca' inside a window may also be dropped (cittasamuṭṭhānañca rūpaṃ). Returns list of Pāli keys or None."""
    words = norm_words(" ".join(words))
    ND = normd(D)
    out, i, n = [], 0, len(words)
    maxl = 14
    while i < n:
        if words[i] in ("ca", "¦"):
            i += 1
            continue
        hit = None
        for L in range(min(maxl, n - i), 0, -1):
            seg = words[i:i + L]
            if seg[-1] in ("ca", "¦"):
                continue
            key = " ".join(seg)
            if key in ND:
                hit = (ND[key], L)
                break
            k2 = " ".join(w for w in seg if w != "ca")
            if "¦" not in seg and k2 in ND:
                hit = (ND[k2], L)
                break
        if not hit:
            return None
        out.append(hit[0])
        i += hit[1]
    return out


def join_list(hs):
    if len(hs) == 1:
        return hs[0]
    return ", ".join(hs[:-1]) + " और " + hs[-1]


def nom_list(words):
    keys = np_parse(words, NOM)
    if not keys:
        return None
    hs = [NOM[k][0] for k in keys]
    if len(keys) == 1:
        g = NOM[keys[0]][1]
    else:
        g = "fp" if all(NOM[k][1].startswith("f") for k in keys) else "mp"
    return join_list(hs), g


def obl_list(words):
    keys = np_parse(words, OBL)
    if not keys:
        return None
    return join_list([OBL[k] for k in keys])


def dat_list(words):
    keys = np_parse(words, DAT)
    if not keys:
        return None
    hs = [DAT[k] for k in keys]
    if len(hs) == 2:
        return f"{hs[0]} के लिए और {hs[1]} के लिए"
    return join_list(hs) + " के लिए"


VERBP = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "saṃsaṭṭho": "से घुल-मिलकर", "saṃsaṭṭhā": "से घुल-मिलकर",
         "sahajāto": "के साथ जन्म लेकर", "sahajātā": "के साथ जन्म लेकर", "nissāya": "के आश्रय से",
         "sampayutto": "से जुड़कर", "sampayuttā": "से जुड़कर"}
ARISE_G = {"ms": "उत्पन्न होता है", "fs": "उत्पन्न होती है", "mp": "उत्पन्न होते हैं", "fp": "उत्पन्न होती हैं"}
STATE = {"g": "fs", "prev": ""}
SAV_PL = "उनका रस लेता है, उनमें आनंद लेता है"

FRAME_RE = None


def build_frame_re():
    global FRAME_RE
    alt = lambda d: "|".join(re.escape(k) for k in sorted(d, key=len, reverse=True))
    FRAME_RE = re.compile(
        rf"^(siyā )?({alt(ACC)}) dhammaṃ (paṭicca|paccayā|sahajāto|sahajātā|nissāya|saṃsaṭṭho|saṃsaṭṭhā|sampayutto|sampayuttā) "
        rf"({alt(NOMI)}) (?:dhammo uppajjati|dhammā uppajjanti|dhammo uppajjeyya|dhammā uppajjeyyuṃ) ({S.CHAIN_RE})$")
    return FRAME_RE


PANHA_HEAD_RE = None


def build_panha_re():
    global PANHA_HEAD_RE, PANHA_LBL_RE
    alt = lambda d: "|".join(re.escape(k) for k in sorted(d, key=len, reverse=True))
    PANHA_HEAD_RE = re.compile(rf"^({alt(NOMI)}) (?:dhammo|dhammā) ({alt(DATI)}) dhammassa (na )?(\w+)paccayena paccayo$")
    PANHA_LBL_RE = re.compile(rf"^({alt(NOMI)}) (?:dhammo|dhammā) ({alt(DATI)}) dhammassa(?: (.+))?$")


PANHA_LBL_RE = None


def is_count_piece(t):
    return S.is_count(t)


INS_RE = re.compile(r"^(.*?) ?(?:(kiñci kāle) )?(?:(na|no) )?(\w+)paccayena paccayo$")
VP_RE = re.compile(r"^(.+?) (paṭicca|paccayā|saṃsaṭṭho|saṃsaṭṭhā|sahajāto|sahajātā|nissāya|sampayutto|sampayuttā)(?: (.+))?$")
OBJ_RE = re.compile(r"^(.+?)(?: (\S+ena cittena))? (aniccato|garuṃ katvā assādeti abhinandati|assādeti abhinandati|"
                    r"garuṃ katvā|ārabbha)$")
UPA_RE = re.compile(r"^(.+?) upanissāya(?: (\S+ena cittena))?(?: (.+))?$")
AR_RE = re.compile(r"^(.+?) (ārabbha|garuṃ katvā) (.+) (uppajjati|uppajjanti)$")


def clause(piece):
    """Translate one piece (no separators). Returns Hindi or raises KeyError."""
    core = piece.strip()
    if not core:
        return piece
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    h = clause_core(core)
    return lead + h + trail


def clause_core(core):
    low = S.lower_initials(core)
    if low in CLAUSE:
        if low.startswith("maggo "):
            STATE["g"] = "ms"
        return CLAUSE[low]
    if re.fullmatch(S.CHAIN_RE, low):
        return S.CH(low)
    m = re.match(r"^(.+) niṭṭhitaṃ$", core)
    if m:
        name = m.group(1)
        if name in NITTHITA:
            return NITTHITA[name] + " समाप्त"
        if name in HEAD:
            return HEAD[name] + " समाप्त"
    m = FRAME_RE.match(low)
    if m:
        siya, x, v, y, chain = m.groups()
        yh, g = NOMI[y]
        verb = ("उत्पन्न हो सकती हैं" if g == "fp" else "उत्पन्न हो सकती है") if siya else \
            ("उत्पन्न होती हैं" if g == "fp" else "उत्पन्न होती है")
        STATE["g"] = g
        return f"{'क्या ' if siya else ''}{ACC[x]} {VERBP[v]} {yh} {S.CH(chain)} {verb}{'?' if siya else ''}"
    # frame followed by its body without the dash (^7-35-53)
    m = re.match(FRAME_RE.pattern[:-1] + r" (.+)$", low)
    if m:
        frame_len = len(low) - len(m.group(6)) - 1
        return clause_core(low[:frame_len]) + " " + clause_core(m.group(6))
    m = PANHA_HEAD_RE.match(low)
    if m:
        x, y, neg, k = m.groups()
        xh, g = NOMI[x]
        STATE["g"] = STATE["frame_g"] = g
        ins = S.NINS(k, g) if neg else S.INS(k, g)
        return f"{xh}, {DATI[y]} {ins}"
    words = low.split()
    # prefix (arūpe …)
    pre = ""
    for p in sorted(PREFIX, key=len, reverse=True):
        if low.startswith(p + " "):
            pre = PREFIX[p] + " "
            low = low[len(p) + 1:]
            words = low.split()
            break
        if low == p:
            return PREFIX[p]
    # X paṭicca / paccayā … Y
    m = VP_RE.match(low)
    if m:
        a, v, b = m.groups()
        ah = obl_list(a.split())
        if ah is not None:
            if not b:
                return pre + f"{ah} {VERBP[v]}"
            bh = nom_list(b.split())
            if bh is not None:
                STATE["g"] = bh[1]
                return pre + f"{ah} {VERBP[v]} {bh[0]}"
    # X ārabbha / garuṃ katvā Y uppajjati
    m = AR_RE.match(low)
    if m:
        a, v, b, verb = m.groups()
        ah = "उसे" if a == "taṃ" else obl_list(a.split())
        bh = nom_list(b.split())
        if ah is not None and bh is not None:
            vh = ("विषय बनाकर" if v == "ārabbha" else "महत्व देकर")
            vh = vh if a == "taṃ" else "को " + vh
            STATE["g"] = bh[1]
            return pre + f"{ah} {vh} {bh[0]} {ARISE_G[bh[1]]}"
    # X aniccato / X assādeti abhinandati / X garuṃ katvā … / X ārabbha (optionally «Yena cittena» before the verb)
    m = OBJ_RE.match(low)
    if m:
        keys = np_parse(m.group(1).split(), OBL)
        if keys:
            ah = join_list([OBL[k] for k in keys])
            pl = len(keys) > 1 or ah.endswith("ों")
            adv = (" " + ADV[m.group(2)]) if m.group(2) else ""
            v = m.group(3)
            if v == "aniccato":
                return pre + f"{ah} को{adv} अनित्य"
            if v == "assādeti abhinandati":
                return pre + f"{ah} का{adv} रस लेता है, {'उनमें' if pl else 'उसमें'} आनंद लेता है"
            if v == "garuṃ katvā assādeti abhinandati":
                return pre + f"{ah} को{adv} महत्व देकर {'उनका' if pl else 'उसका'} रस लेता है, {'उनमें' if pl else 'उसमें'} आनंद लेता है"
            if v == "garuṃ katvā":
                return pre + f"{ah} को{adv} महत्व देकर"
            if v == "ārabbha":
                return pre + f"{ah} को{adv} विषय बनाकर"
    m = UPA_RE.match(low)
    if m:
        ah = obl_list(m.group(1).split())
        if ah is not None:
            adv = (" " + ADV[m.group(2)]) if m.group(2) else ""
            act = (" " + clause_core(m.group(3))) if m.group(3) else ""
            return pre + f"{ah} के प्रबल आश्रय से{adv}{act}"
    # (ariyā) (avitakkā) jhānā / maggā / phalā vuṭṭhahitvā (…)
    m = re.match(r"^(?:(ariyā|sekkhā|arahā) )?(?:(\S+) )?(jhānā|maggā|phalā) vuṭṭhahitvā(?: (.+))?$", low)
    if m and (not m.group(2) or m.group(2) in ABL_ADJ):
        subj, adj, src, rest = m.groups()
        h = (SUBJ_H[subj] + " " if subj else "") + (ABL_ADJ[adj] + " " if adj else "") + \
            {"jhānā": "ध्यान", "maggā": "मार्ग", "phalā": "फल"}[src] + " से उठकर"
        if rest:
            h += " " + clause_core(rest)
        return pre + h
    # (ariyā) X (garuṃ katvā) paccavekkhati / paccavekkhanti
    m = re.match(r"^(?:(ariyā|sekkhā|arahā) )?(.+?)(?: (\S+ena cittena))?( garuṃ katvā)? (paccavekkhati|paccavekkhanti)"
                 r"(,? assādeti abhinandati)?$", low)
    if m:
        subj, obj, adv, garu, verb, sav = m.groups()
        oh = "उस" if obj == "taṃ" else obl_list(obj.split())
        if oh is not None:
            vh = "पुनः विचार करता है" if verb == "paccavekkhati" else "पुनः विचार करते हैं"
            mid = (" को महत्व देकर" if garu else " पर")
            if obj == "taṃ" and garu:
                oh, mid = "उसे", " महत्व देकर"
            adv = (" " + ADV[adv]) if adv else ""
            pl = oh.endswith("ों") or " और " in oh
            tail = (", " + (SAV_PL if pl else "उसका रस लेता है, उसमें आनंद लेता है")) if sav else ""
            return pre + (SUBJ_H[subj] + " " if subj else "") + f"{oh}{adv}{mid} {vh}{tail}"
    # (ariyā) (Yena cittena) …  = subject + rest
    m = re.match(r"^(ariyā|sekkhā|arahā) (.+)$", low)
    if m:
        try:
            return pre + SUBJ_H[m.group(1)] + " " + clause_core(m.group(2))
        except KeyError:
            pass
    # (appītikā) jhānā / maggā / phalā
    m = re.match(r"^(?:(\S+) )?(jhānā|maggā|phalā)$", low)
    if m and (not m.group(1) or m.group(1) in ABL_ADJ):
        return pre + (ABL_ADJ[m.group(1)] + " " if m.group(1) else "") + \
            {"jhānā": "ध्यान", "maggā": "मार्ग", "phalā": "फल"}[m.group(2)] + " से"
    # pañhā head with labels instead of a condition (… dhammassa sahajātaṃ… purejātaṃ) or elided
    m = PANHA_LBL_RE.match(low)
    if m:
        x, y, rest = m.groups()
        xh, g = NOMI[x]
        STATE["g"] = STATE["frame_g"] = g
        return f"{xh}, {DATI[y]}" + (" " + clause_core(rest) if rest else "")
    if is_count_piece(low):
        return S.count_hi(low)
    # X ārabbha / garuṃ katvā Y (verb elided)
    m = re.match(r"^(.+?) (ārabbha|garuṃ katvā) (.+)$", low)
    if m:
        a, v, b = m.groups()
        ah = "उसे" if a == "taṃ" else obl_list(a.split())
        bh = nom_list(b.split())
        if ah is not None and bh is not None:
            vh = ("विषय बनाकर" if v == "ārabbha" else "महत्व देकर")
            vh = vh if a == "taṃ" else "को " + vh
            return pre + f"{ah} {vh} {bh[0]}"
    # X uppādeti (object in the direct case)
    m = re.match(r"^(.+) (uppādeti|uppādenti)$", low)
    if m:
        ws = m.group(1).split()
        bh = nom_list(ws)
        oh = bh[0] if bh is not None else obl_list(ws)
        if oh is not None:
            return pre + f"{oh} {'उत्पन्न करता है' if m.group(2) == 'uppādeti' else 'उत्पन्न करते हैं'}"
    # «X uppajjati / uppajjanti» (domanassaṃ uppajjati, kilesā uppajjanti)
    m = re.match(r"^(.+) (uppajjati|uppajjanti)$", low)
    if m:
        bh = nom_list(m.group(1).split())
        if bh is not None:
            return pre + f"{bh[0]} {ARISE_G[bh[1]]}"
    # an adverb «Xena cittena» inside an otherwise known clause: translate both sides
    m = re.match(r"^(.*?)\b(\S+ena cittena)\b ?(.*)$", low)
    if m and m.group(2) in ADV:
        left, adv, right = m.group(1).strip(), ADV[m.group(2)], m.group(3).strip()
        try:
            lh = clause_core(left) if left else ""
            rh = clause_core(right) if right else ""
            return pre + " ".join(x for x in (lh, adv, rh) if x)
        except KeyError:
            pass
    # … Xpaccayena paccayo
    m = INS_RE.match(low)
    if m and m.group(4) not in S.KEYS and m.group(4)[2:] in S.KEYS and m.group(4)[:2] in ("na", "no") \
            and not m.group(3):
        m = INS_RE.match(low.replace(m.group(4) + "paccayena", m.group(4)[:2] + " " + m.group(4)[2:] + "paccayena"))
    if m and m.group(4) in S.KEYS:
        body, kinci, neg, k = m.groups()
        ws = body.split() if body else []
        parts, g = None, STATE["g"]
        for cut in range(len(ws), -1, -1):
            sub = nom_list(ws[:cut]) if cut else ("", None)
            if sub is None:
                continue
            dat = dat_list(ws[cut:]) if cut < len(ws) else ""
            if dat is None:
                continue
            parts = []
            if cut:
                parts.append(sub[0])
                g = sub[1]
                # the last member of an elided list «saddhā…pe… senāsanaṃ …» takes the plural verb
                if " ".join(ws[:cut]) in ("senāsanaṃ", "paññā", "patthanā") and STATE.get("after_pe"):
                    g = "mp"
            if dat:
                parts.append(dat)
            if not cut and not dat:
                g = STATE.get("frame_g", g)
            break
        if parts is not None:
            if cut or dat:
                STATE["g"] = g
            if kinci:
                parts.append(S.KINCI_KALE)
            parts.append(S.NINS(k, g) if neg else S.INS(k, g))
            return pre + " ".join(parts)
    # bare NP lists
    if low.endswith(" ca"):
        r = clause_core(low[:-3])
        return r + " और"
    for f in (lambda w: nom_list(w), lambda w: obl_list(w)):
        r = f(words)
        if r is not None:
            return pre + (r[0] if isinstance(r, tuple) else r)
    # NOM + DAT without verb (Rūpāyatanaṃ cakkhuviññāṇassa…)
    for cut in range(len(words) - 1, 0, -1):
        a, b = nom_list(words[:cut]), dat_list(words[cut:])
        if a is not None and b is not None:
            STATE["g"] = "mp" if (STATE.get("after_pe") or " ".join(words[:cut]) == "senāsanaṃ") else a[1]
            return pre + f"{a[0]} {b}"
    r = dat_list(words)
    if r is not None:
        return pre + r
    raise KeyError(core)


# ---------------------------------------------------------------- line translator
ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")
NOTE_RE = re.compile(r"\(([^()]*[^\d().][^()]*)\)")
UNKNOWN = Counter()


def note_hi(n):
    if n in NOTE:
        return NOTE[n]
    low = S.lower_initials(n)
    if low in S.NOTE:
        return S.NOTE[low]
    raise KeyError("NOTE: " + n)


def protect_dat_commas(t):
    return re.sub(r"(\S*(?:ssa|āya|iyā|ānaṃ)(?: ca)?), (?=\S*(?:ssa|āya|iyā|ānaṃ)\b)", r"\1 ¦ ", t)


def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    if line in LINE_X:
        return LINE_X[line]
    store = []

    def keep(h):
        store.append(h)
        return f"\x00{len(store) - 1}\x01"

    inserts = []
    for v, (kind, anchor) in VARIANTS_X.items():
        if v in line:
            line = line.replace(" " + v, "")
            inserts.append((anchor, S.variant_hi(v, kind)))
    if "{" in line:
        raise KeyError("variant: " + line)
    for a, b in SLIPS_X.items():
        line = line.replace(a, b)
    text = NOTE_RE.sub(lambda m: keep("(" + note_hi(m.group(1)) + ")"), line)
    # counting lines (segments between notes)
    segs = re.split(r"(\x00\d+\x01)", text)
    isc = lambda s: S.is_count(S.lower_initials(s))
    if all(not s.strip(" ,.") or s.startswith("\x00") or isc(s.strip(" ")) or
           isc(s.strip(" ,")) for s in segs) and any(s.strip(" ,.") and not s.startswith("\x00") for s in segs):
        out = []
        for s in segs:
            if s.startswith("\x00") or not s.strip(" ,."):
                out.append(s.replace(".", "।") if not s.startswith("\x00") else s)
            else:
                out.append(count_seg(s))
        return finish("".join(out), store, inserts)
    text = protect_dat_commas(text)
    out = []
    STATE["after_pe"] = False
    for tok in re.split(r"( – |; |, |\. |…pe…|…|\.$)", text):
        if tok in (" – ", "; ", ", ", "…", "…pe…", ". ", "."):
            STATE["after_pe"] = tok in ("…", "…pe…")
        if tok in (" – ", "; ", ", ", "…"):
            out.append(tok)
        elif tok == ". ":
            out.append("। ")
        elif tok == ".":
            out.append("।")
        elif tok == "…pe…":
            out.append("…")
        elif tok:
            for part in re.split(r"(\x00\d+\x01|\(\d+\))", tok):
                if not part.strip() or re.fullmatch(r"\x00\d+\x01|\(\d+\)", part):
                    out.append(part)
                else:
                    try:
                        if part.strip() == "assādeti abhinandati" and STATE.get("prev", "").endswith("vipassati"):
                            out.append(part.replace("assādeti abhinandati", SAV_PL))
                            continue
                        STATE["prev"] = part.strip()
                        out.append(clause(part))
                    except KeyError as e:
                        UNKNOWN[str(e)] += 1
                        out.append("⟦" + part + "⟧")
    return finish("".join(out), store, inserts)


def count_seg(s):
    lead = s[: len(s) - len(s.lstrip(" ,"))]
    core = s.strip(" ,")
    trail = s[len(s.rstrip(" ")):]
    core = core.rstrip(" ")
    h = S.count_hi(core)
    return lead + h + trail


def finish(s, store, inserts):
    s = re.sub(r"\x00(\d+)\x01", lambda m: store[int(m.group(1))], s)
    s = s.replace("?।", "?").replace(" ¦ ", ", ")
    for anchor, br in inserts:
        assert anchor in s, (anchor, s)
        s = s.replace(anchor, anchor + " " + br, 1)
    return s


def build():
    build_frame_re()
    build_panha_re()
    lines = open(SRC, encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        try:
            hi = translate_line(body)
        except KeyError as e:
            UNKNOWN[str(e)] += 1
            hi = "⟦" + body + "⟧"
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    with open(DST, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    build()
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 80
    for k, v in UNKNOWN.most_common(lim):
        print(v, k)
    print("unknown kinds:", len(UNKNOWN), "total:", sum(UNKNOWN.values()))
