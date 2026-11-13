"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 2-04 .. 2-08 (triads 9-13).

Imports the approved sample builder read-only (constants and helpers) and adds the item system of these triads
and compositional phrase handlers. Phrase tables: hi_2_04_2_08_dicts.py (same folder).
usage (repo root):
  python -I -B -X utf8 0-INBOX\\temp\\pipeline\\pi-7-hi\\rails\\build_rails_2-04_2-08.py          build the five files
  python -I -B -X utf8 0-INBOX\\temp\\pipeline\\pi-7-hi\\rails\\build_rails_2-04_2-08.py --dump   list unknown clauses
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_rails_sample as S  # noqa: E402  (read-only)
import hi_2_04_2_08_dicts as D  # noqa: E402

PALI_DIR, OUT_DIR = S.PALI_DIR, S.OUT_DIR
FILES = ["2-04-dassanenapahatabbahetukattika.md", "2-05-acayagamittika.md", "2-06-sekkhattika.md",
         "2-07-parittattika.md", "2-08-parittarammanattika.md"]


# ---------------------------------------------------------------- 1. items


def VAL(base):
    """An item ending in an agreeing «वाला» / «का»: base carries {a} = ा / ी / े."""
    return {"m": base.format(a="ा"), "f": base.format(a="ी"), "o": base.format(a="े"), "short": False}


def INV(w):
    """A short invariant adjective (सीमित): «एक सीमित समूह», like «एक हितकर समूह»."""
    return {"m": w, "f": w, "o": w, "short": True}


ITEMS_04 = [VAL("सत्य-दर्शन से छोड़े जाने वाले मूलों वाल{a}"), VAL("मानसिक अभ्यास से छोड़े जाने वाले मूलों वाल{a}"),
            VAL("न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाल{a}")]
ITEMS_05 = [VAL("संचय की ओर ले जाने वाल{a}"), VAL("संचय घटाने की ओर ले जाने वाल{a}"),
            VAL("न संचय की ओर, न संचय घटाने की ओर ले जाने वाल{a}")]
ITEMS_06 = [VAL("सीखने के चरण क{a}"), VAL("सीखना पूरा होने के चरण क{a}"),
            VAL("न सीखने के चरण क{a}, न सीखना पूरा होने के चरण क{a}")]
ITEMS_07 = [INV("सीमित"), INV("उन्नत"), INV("अपरिमित")]
ITEMS_08 = [VAL("सीमित विषय वाल{a}"), VAL("उन्नत विषय वाल{a}"), VAL("अपरिमित विषय वाल{a}")]

PAR_STEMS = [("paritt", "a"), ("mahaggat", "a"), ("appamāṇ", "a")]
ARA_STEMS = [("parittārammaṇ", "a"), ("mahaggatārammaṇ", "a"), ("appamāṇārammaṇ", "a")]

TRIADS = {
    "2-04-dassanenapahatabbahetukattika.md": {
        "pre": [("nevadassanena nabhāvanāya pahātabbahetuk", "ndnbph"), ("dassanena pahātabbahetuk", "dph"),
                ("bhāvanāya pahātabbahetuk", "bph")],
        "§": ([("dph", "a"), ("bph", "a"), ("ndnbph", "a")], ITEMS_04), "¤": ([], []),
    },
    "2-05-acayagamittika.md": {
        "pre": [],
        "§": ([("ācayagām", "i"), ("apacayagām", "i"), ("nevācayagāmināpacayagām", "i")], ITEMS_05), "¤": ([], []),
        # Nevācayagāmīnāpacayagāmī (ī for i): spelling slip of item 3, rendered as meant
        "alias": [("nevācayagāmīnāpacayagām", "nevācayagāmināpacayagām")],
    },
    "2-06-sekkhattika.md": {
        "pre": [], "§": ([("sekkh", "a"), ("asekkh", "a"), ("nevasekkhanāsekkh", "a")], ITEMS_06), "¤": ([], []),
    },
    "2-07-parittattika.md": {"pre": [], "§": (PAR_STEMS, ITEMS_07), "¤": (ARA_STEMS, ITEMS_08)},
    "2-08-parittarammanattika.md": {"pre": [], "§": (ARA_STEMS, ITEMS_08), "¤": (PAR_STEMS, ITEMS_07)},
}

ENDS = {"a": {"aṃ", "o", "ā", "e", "assa", "ānaṃ", "āya", "ena", "āni", "ehi", "asmiṃ"},
        "i": {"iṃ", "ī", "issa", "īnaṃ", "iyā", "ino", "inā"}}
CA = {"a": {"añca"}, "i": {"iñca"}}
WORD = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")
# words that look like an item but are persons (sekkhā = trainees), per file: (regex, token) before normalisation
_SEKKHA_ADJ = "khandhā|cetanā|hetū|adhipati|āhārā|indriyā|saddhā|paññā|khandho|phalasamāpatti|rāgo"
PROTECT = {"2-06-sekkhattika.md": [(rf"(?<!\w)sekkhā(?!\w)(?! (?:{_SEKKHA_ADJ})(?!\w))", "trainees"),
                                   (r"(?<!\w)sekkhānaṃ(?= (?:anulomaṃ|atthappaṭisambhidāya))", "traineesgen")]}
NOT_ITEM = {}


class Triad:
    def __init__(self, name):
        cfg = TRIADS[name]
        self.name = name
        self.pre = cfg["pre"]
        self.alias = cfg.get("alias", [])
        self.stems, self.hi = [], {}
        for mark in ("§", "¤"):
            stems, his = cfg[mark]
            for i, (st, decl) in enumerate(stems):
                self.stems.append((st, decl, f"{mark}{i + 1}"))
                self.hi[f"{mark}{i + 1}"] = his[i]
        self.stems.sort(key=lambda s: len(s[0]), reverse=True)
        self.keep = NOT_ITEM.get(name, set())

    def norm_word(self, w, top=True):
        if top and w in self.keep:
            return w
        for stem, decl, tag in self.stems:
            if not w.startswith(stem):
                continue
            rest = w[len(stem):]
            if rest in ENDS[decl]:
                return tag
            if rest in CA[decl]:
                return tag + " ca"
            link = "a" if decl == "a" else "i"
            if rest.startswith(link) and len(rest) > 1:
                r = rest[1:]
            elif decl == "a" and rest.startswith("ā") and len(rest) > 1:
                r = "a" + rest[1:]
            else:
                continue
            return tag + "+" + self.norm_word(r, False)
        return w

    def normalize(self, text):
        for a, b in self.alias:
            text = text.replace(a, b)
        for a, b in self.pre:
            text = re.sub(r"(?<![\w])" + re.escape(a), b, text)
        for a, b in PROTECT.get(self.name, []):
            text = re.sub(a, b, text)
        return WORD.sub(lambda m: self.norm_word(m.group(0)), text)


def gen(s):
    toks = re.findall(r"[§¤]\d", s)
    return re.sub(r"([§¤])\d", r"\1", s), toks


def fill(tpl, toks, T):
    def rep(m):
        it = T.hi[toks[int(m.group(1))]]
        code = m.group(2)
        if code in "fmo":
            return it[code]
        if code == "E":
            return f"एक {it['m']}" if it["short"] else f"{it['o']} एक"
        if code == "D":
            return f"एक {it['m']}" if it["short"] else f"{it['m']} एक"
        raise KeyError(code)
    return re.sub(r"‹(\d)([fmoED])›", rep, tpl)


def shift(tpl, k):
    """Renumber ‹n..› slots by +k (for composed phrases)."""
    return re.sub(r"‹(\d)", lambda m: f"‹{int(m.group(1)) + k}", tpl)


# ---------------------------------------------------------------- 2. tables

HEAD = dict(S.HEAD)
HEAD.update(D.HEAD_X)
for _k in S.KEYS:
    _n = ("no" if _k in ("atthi", "natthi", "vigata", "avigata") else "na") + _k
    HEAD[_k[0].upper() + _k[1:] + "paccayādi"] = S.NAME[_k] + " आदि"
    HEAD[_n[0].upper() + _n[1:] + "paccayādi"] = S.NNAME[_k] + " आदि"
    HEAD[_n[0].upper() + _n[1:] + "dukaṃ"] = S.NDUKA[_k]

NOTE = {k.rstrip(".").strip(): v.rstrip("।") for k, v in S.NOTE.items()}
NOTE.update(D.NOTE_X)
CLAUSE = dict(S.CLAUSE)
CLAUSE.update(D.CLAUSE_X)
for _w, _h in list(S.P_ABL.items()) + list(S.P_NABL.items()):
    CLAUSE.setdefault(_w, _h)
OBJ = dict(S.SUBJ_P)
OBJ.update(D.OBJ_X)
RES = dict(S.OBJ_P)
RES.update(D.RES_X)
NUM = dict(S.NUM)
NUM.update(D.NUM_X)
PREFIX = dict(S.PREFIX)
PREFIX.update(D.PREFIX_X)

# subjects: phrase-level (may end in a comma) and units (composable with ca)
SUBJ_P = dict(S.SUBJ)
SUBJ_P.update(D.SUBJ_P_X)
SUBJ_U = {k: (v.rstrip(","), g) for k, (v, g) in S.SUBJ.items() if " ca " not in k}
SUBJ_U.update(D.SUBJ_U_X)
# datives: phrase-level (full Hindi) and units (without «के लिए»; flag = joined by ca)
DAT_P = dict(S.DAT)
DAT_P.update(D.DAT_P_X)
DAT_U = {}
for _k, _v in S.DAT.items():
    if _v.endswith(" के लिए") and _v.count("के लिए") == 1 and "," not in _k and " ca" not in _k:
        DAT_U[_k] = (_v[: -len(" के लिए")], False)
for _k, _v in S.NANA.items():
    DAT_U[_k] = (_v, False)
DAT_U.update(D.DAT_U_X)
for _acc, _nom, _dat, _h, _g in D.NOUNS:
    _X = "m" if _g == "m" else "f"
    _O = "o" if _g == "m" else "f"
    if _nom:
        SUBJ_U.setdefault(_nom, (_h, _g + "s"))
        SUBJ_U.setdefault("§ " + _nom, (f"‹0{_X}› {_h}", _g + "s"))
    if _dat:
        DAT_U.setdefault(_dat, (_h, False))
        DAT_U.setdefault("§ " + _dat, (f"‹0{_O}› {_h}", False))
NOUN_D, NOUN_O = {}, {}  # accusative nouns: direct (lists) and oblique (before a postposition)
for _acc, _nom, _dat, _h, _g in D.NOUNS:
    _X = "m" if _g == "m" else "f"
    _O = "o" if _g == "m" else "f"
    for _p in {_acc, _nom} - {None}:
        NOUN_D.setdefault(_p, _h)
        NOUN_D.setdefault("§ " + _p, f"‹0{_X}› {_h}")
    if _acc:
        NOUN_O.setdefault(_acc, _h)
        NOUN_O.setdefault("§ " + _acc, f"‹0{_O}› {_h}")
NOUN_D.update(D.NOUN_D_X)
NOUN_O.update(D.NOUN_O_X)

REL = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "saṃsaṭṭho": "से घुल-मिलकर", "saṃsaṭṭhā": "से घुल-मिलकर",
       "nissāya": "के आश्रय से", "sahajāto": "के साथ जन्म लेकर", "sahajātā": "के साथ जन्म लेकर",
       "sampayutto": "से जुड़कर", "sampayuttā": "से जुड़कर"}
ARISE_G = {"ms": "उत्पन्न होता है", "fs": "उत्पन्न होती है", "mp": "उत्पन्न होते हैं", "fp": "उत्पन्न होती हैं"}


def _alt(keys):
    return "|".join(re.escape(k).replace("§", r"§\d").replace("¤", r"¤\d")
                    for k in sorted(keys, key=len, reverse=True))


def comp_pat(units):
    u = _alt(units)
    return rf"(?:{u})(?: ca)?(?:,? (?:{u})(?: ca)?)*"


def parse_comp(text, units):
    """Split 'A ca B ca' / 'A, B' / 'A B ca' into [(key, toks, ca)] using the unit table, or None."""
    rx = re.compile(rf"({_alt(units)})( ca)?(?:,? |$)")
    pos, out = 0, []
    while pos < len(text):
        m = rx.match(text, pos)
        if not m or m.end() == pos:
            return None
        g, toks = gen(m.group(1))
        out.append((g, toks, bool(m.group(2))))
        pos = m.end()
    return out


def subj_hi(text, T):
    g, toks = gen(text)
    if g in SUBJ_P:
        h, gg = SUBJ_P[g]
        return fill(h, toks, T), gg
    parts = parse_comp(text, SUBJ_U)
    if parts is None:
        return None, None
    hs, gs = [], []
    for k, tk, _ in parts:
        h, gg = SUBJ_U[k]
        hs.append(fill(h, tk, T))
        gs.append(gg)
    if len(hs) == 1:
        return hs[0], gs[0]
    return ", ".join(hs[:-1]) + " और " + hs[-1], ("fp" if all(x[0] == "f" for x in gs) else "mp")


def dat_hi(text, T):
    g, toks = gen(text)
    if g in DAT_P:
        return fill(DAT_P[g], toks, T)
    parts = parse_comp(text, DAT_U)
    if parts is None:
        return None
    hs, cas = [], []
    for k, tk, ca in parts:
        h, flag = DAT_U[k]
        hs.append(fill(h, tk, T))
        cas.append(ca or flag)
    if len(hs) == 1:
        return hs[0] + " के लिए"
    if any(cas) or len(hs) == 2:
        each = [h + " के लिए" for h in hs]
        if any(cas):
            return ", ".join(each[:-1]) + " और " + each[-1]
        return ", ".join(each)
    return ", ".join(hs[:-1]) + " और " + hs[-1] + " के लिए"


# ---------------------------------------------------------------- 3. frames

ACCX = r"[§¤]\d(?: ca [§¤]\d)*(?: ca)?"
RELX = "|".join(REL)
VARA_RE = re.compile(rf"(?<![\w§¤+])({ACCX}) dhammaṃ ({RELX}) "
                     rf"({ACCX}) (dhammo uppajjati|dhammā uppajjanti)(?: ({S.CHAIN_RE}))?")


def acc_hi(g):
    n = g.count("§") + g.count("¤")
    parts = [f"‹{i}f› परिघटना" for i in range(n)]
    return parts[0] if n == 1 else ", ".join(parts[:-1]) + " और " + parts[-1]


def nom_hi(g):
    n = g.count("§") + g.count("¤")
    if n == 1:
        return "‹0f› परिघटना", "s"
    parts = [f"‹{i}f›" for i in range(n)]
    return ", ".join(parts[:-1]) + " और " + parts[-1] + " परिघटनाएँ", "p"


def frame_hi(acc, rel, nom, verb, chain, T):
    parts = []
    if acc:
        ga, ta = gen(acc)
        parts.append(fill(acc_hi(ga), ta, T))
    if rel:
        parts.append(REL[rel])
    n = "s"
    if nom:
        gn, tn = gen(nom)
        nh, n = nom_hi(gn)
        parts.append(fill(nh, tn, T))
    if chain:
        parts.append(S.CH(chain))
    if verb:
        parts.append(S.ARISES[n])
    return " ".join(parts)


DEF_RE = SD_RE = None
LOG = collections.Counter()


def build_res():
    global DEF_RE, SD_RE, PCLAUSE_RE, UPA_RE, REV_RE, ARB_RE, ARISE_RE, CETO_RE, SHORT_RE, NLIST_RE, OBJ_RE
    global RES_RE, VCL_RES
    subj = rf"(?:{_alt(SUBJ_P)}|{comp_pat(SUBJ_U)})"
    dat = rf"(?:{_alt(DAT_P)}|{comp_pat(DAT_U)})"
    keys = "|".join(sorted(S.KEYS, key=len, reverse=True))
    DEF_RE = re.compile(rf"(?<![\w§¤+])(?:(?:({_alt(D.LABEL)}) )?({subj}) )?(?:({dat}) )?(?:(kiñci kāle) )?(na )?"
                        rf"({keys})paccayena paccay([oa])")
    pre = _alt(PREFIX)
    global SUBJ_START
    SUBJ_START = re.compile(rf"(?:^|, |…(?:pe…)? ?|; )({comp_pat(SUBJ_U)})(?= |,|…|$)")
    SD_RE = re.compile(rf"^(?:({_alt(D.LABEL)}) )?(?:({pre}) )?(?:({subj}))?(?:(?<=\S) )?(?:({dat}))?$")
    PCLAUSE_RE = re.compile(rf"^(?:({pre}) )?({_alt(OBJ)}) ({RELX})(?: ({_alt(RES)}))?$")
    OBJ_RE = re.compile(rf"^(?:({pre}) )?({_alt(OBJ)})$")
    RES_RE = re.compile(rf"^({_alt(RES)})$")
    nlist = rf"(?:{_alt(NOUN_O)})(?:,? (?:{_alt(NOUN_O)}))*"
    UPA_RE = re.compile(rf"^(?:({_alt(D.PERSON)}) )?({nlist}) upanissāya(?: ({_alt(D.ACTIONS)}))?$")
    NLIST_RE = re.compile(rf"^(?:{_alt(NOUN_D)})(?:,? (?:{_alt(NOUN_D)}))*$")
    REV_RE = re.compile(rf"^(?:({_alt(D.PERSON)}) )?({_alt(D.ROBJ)})(?: (garuṃ katvā))?(?: ({_alt(D.RVERB)}))?$")
    ARB_RE = re.compile(rf"^(taṃ|{_alt(D.ROBJ)}|{comp_pat(D.ROBJ)}) (ārabbha|garuṃ katvā) ({subj})"
                        rf"(?: (uppajjati|uppajjanti))?$")
    ARISE_RE = re.compile(rf"^({subj}) (uppajjati|uppajjanti)$")
    CETO_RE = re.compile(r"^(?:(ariyā|sekkhā|arahā) )?cetopariyañāṇena ((?:[§¤]\d\+)+)cittasamaṅgissa cittaṃ "
                         r"(jānāti|jānanti)$")
    SHORT_RE = re.compile(rf"^(?:({_alt(D.SHORT_SUBJ)}) )?({_alt(D.SHORT_ON)}) ({S.COND_ALT})$")
    VCL_RES = [
        re.compile(rf"^({ACCX}) dhammaṃ(?: ({RELX}))?(?: ({ACCX}) (dhammo|dhammā))?$"),
        re.compile(rf"^({ACCX}) (dhammo uppajjati|dhammā uppajjanti)(?: ({S.CHAIN_RE}))?$"),
        re.compile(rf"^({ACCX}) dhammaṃ ({ACCX}) (dhammo uppajjati|dhammā uppajjanti)(?: ({S.CHAIN_RE}))?$"),
    ]


def def_frame(m, T, keep, state):
    label, subj, dat, kinci, neg, k, ending = m.groups()
    if ending == "a":
        LOG["slip: paccaya for paccayo (rendered as meant)"] += 1
    parts = []
    if label:
        parts.append(D.LABEL[label])
    if subj:
        sh, state["g"] = subj_hi(subj, T)
        parts.append(sh)
    if state["g"] is None:
        state["g"] = "mp"
        LOG[f"no subject, plural verb: {m.group(0)[:70]}"] += 1
    if dat:
        parts.append(dat_hi(dat, T))
    if kinci:
        parts.append(S.KINCI_KALE)
    parts.append(S.NINS(k, state["g"]) if neg else S.INS(k, state["g"]))
    return keep(" ".join(parts))


# ---------------------------------------------------------------- 4. counts


def count_words():
    return set(S.P_ABL) | set(S.P_NABL) | set(S.P_LOC) | set(S.P_NLOC) | set(NUM) | {"sabbattha"}


def is_count(text):
    toks = [t for t in re.split(r"(…pe…|…|, |; | |\.|\d+)", text)
            if t and t not in ("…pe…", "…", ", ", "; ", " ", ".") and not t.startswith("")]
    w = count_words()
    return bool(toks) and all(t in w for t in toks)


def count_hi(text):
    toks = [t for t in re.split(r"(…pe…|…|, |; | |\.$|\d+)", text) if t]
    out = []
    for i, t in enumerate(toks):
        if t == " ":
            prev = toks[i - 1] if i else ""
            out.append(", " if prev in S.P_ABL or prev in S.P_NABL else " ")
        elif t == "…pe…":
            out.append("…")
        elif t == ".":
            out.append("।")
        elif t in ("…", ", ", "; ") or t.startswith(""):
            out.append(t)
        elif t == "sabbattha":
            out.append("हर जगह")
        else:
            for d in (S.P_ABL, S.P_NABL, S.P_LOC, S.P_NLOC, NUM):
                if t in d:
                    out.append(d[t])
                    break
    return "".join(out)


# ---------------------------------------------------------------- 5. clauses

UNKNOWN = collections.Counter()
EXAMPLE = {}
CUR = {"file": "", "id": ""}


def unknown(kind, g):
    UNKNOWN[(kind, g)] += 1
    EXAMPLE.setdefault((kind, g), f"{CUR['file'][:4]} {CUR['id']}")
    return "⁇"


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)(\(\d+\.?\) |2-6\. )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    h = HEAD[body] if body in HEAD else unknown("HEAD", body)
    return f"{hashes} {st}{num or ''}{h}{en}"


def pl(h):
    """Singular Hindi verb phrase -> plural (करता है -> करते हैं)."""
    h = re.sub(r"ता है", "ते हैं", h)
    return h


def robj(key, T):
    g, toks = gen(key)
    d, o, n = D.ROBJ[g]
    return fill(d, toks, T), fill(o, toks, T), n


def rev_hi(person, ob, garu, verb, T):
    d, o, n = robj(ob, T)
    their, in_ = ("उनका", "उनमें") if n == "p" else ("उसका", "उसमें")
    out = []
    if person:
        out.append(D.PERSON[person][0])
    if verb is None and not garu:
        out.append(d)
        return " ".join(out)
    vh = D.RVERB[verb] if verb else None
    if garu:
        if vh is None:
            out.append(f"{o} को महत्व देकर")
        elif vh[0] == "review":
            out.append(f"{o} को महत्व देकर पुनः विचार {vh[1]}")
        elif vh[0] == "savour":
            out.append(f"{o} को महत्व देकर {their} रस {vh[1]}, {in_} आनंद {vh[1]}")
        elif vh[0] == "savour1":
            out.append(f"{o} को महत्व देकर {their} रस {vh[1]}")
        else:
            raise KeyError(verb)
    else:
        if vh[0] == "review":
            out.append(f"{o} पर पुनः विचार {vh[1]}")
        elif vh[0] == "savour":
            out.append(f"{o} का रस {vh[1]}, {in_} आनंद {vh[1]}")
        elif vh[0] == "savour1":
            out.append(f"{o} का रस {vh[1]}")
        elif vh[0] == "insight":
            out.append(f"{o} को {S.ANICCA} अंतर्दृष्टि से {vh[1]}")
        elif vh[0] == "anicca":
            out.append(f"{o} को अनित्य")
        elif vh[0] == "know":
            out.append(f"{o} को {vh[1]}")
        else:
            raise KeyError(verb)
    if verb and "vippassa" in verb:
        LOG["slip: vippassati/-nti for vipassati/-nti (rendered as meant)"] += 1
    return " ".join(out)


def nlist_hi(text, table, T):
    keys = re.findall(rf"(?:{_alt(table)})", text)
    hs = []
    for k in keys:
        g, toks = gen(k)
        hs.append(fill(table[g], toks, T))
    return ", ".join(hs)


def clause(piece, T):
    core = piece.strip()
    if not core:
        return piece
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    h = clause_core(core, T)
    return lead + h + trail


DONE = {"h": ""}


def clause_core(core, T):
    g, toks = gen(core)
    if g == "zzdone":
        return DONE["h"]
    if g in CLAUSE:
        return fill(CLAUSE[g], toks, T)
    if core.endswith(".") and len(core) > 1:
        return clause_core(core[:-1], T) + "।"
    m = PCLAUSE_RE.match(core)
    if m:
        pre, obj, rel, res = m.groups()
        go, to = gen(obj)
        h = (PREFIX[pre] + " " if pre else "") + fill(OBJ[go], to, T) + " " + REL[rel]
        if res:
            gr, tr = gen(res)
            h += " " + fill(RES[gr], tr, T)
        return h
    m = VCL_RES[0].match(core)
    if m:
        acc, rel, nom, _ = m.groups()
        return frame_hi(acc, rel, nom, None, None, T)
    m = VCL_RES[1].match(core)
    if m:
        nom, verb, chain = m.groups()
        return frame_hi(None, None, nom, verb, chain, T)
    m = VCL_RES[2].match(core)
    if m:
        acc, nom, verb, chain = m.groups()
        LOG["slip: X dhammaṃ Y dhammo uppajjati without paṭicca (translated as written)"] += 1
        return fill(acc_hi(gen(acc)[0]), gen(acc)[1], T) + ", " + frame_hi(None, None, nom, verb, chain, T)
    m = OBJ_RE.match(core)
    if m:
        pre, obj = m.groups()
        go, to = gen(obj)
        return (PREFIX[pre] + " " if pre else "") + fill(OBJ[go], to, T)
    m = RES_RE.match(core)
    if m:
        return fill(RES[g], toks, T)
    m = SHORT_RE.match(core)
    if m:
        ss, on, cond = m.groups()
        h = ""
        if ss:
            h = fill(D.SHORT_SUBJ[gen(ss)[0]], gen(ss)[1], T) + " "
        return h + fill(D.SHORT_ON[gen(on)[0]], gen(on)[1], T) + " पर " + S._cond_word(cond)
    m = CETO_RE.match(core)
    if m:
        person, mind, verb = m.groups()
        tk = re.findall(r"[§¤]\d", mind)
        mh = " ".join(T.hi[t]["o"] for t in tk)
        v = "जानता है" if verb == "jānāti" else "जानते हैं"
        p = D.PERSON[person][0] + " " if person else ""
        return f"{p}{S.CETOPARIYA} {mh} मन से युक्त व्यक्ति के मन को {v}"
    m = UPA_RE.match(core)
    if m:
        person, nl, act = m.groups()
        h = (D.PERSON[person][0] + " " if person else "") + nlist_hi(nl, NOUN_O, T) + " के प्रबल आश्रय से"
        if act:
            ga, ta = gen(act)
            h += " " + fill(D.ACTIONS[ga], ta, T)
        return h
    m = ARB_RE.match(core)
    if m:
        ob, how, subj, verb = m.groups()
        if ob == "taṃ":
            oh = "उसे"
        else:
            parts = parse_comp(ob, D.ROBJ)
            oh = " और ".join(fill(D.ROBJ[k][1], tk, T) for k, tk, _ in parts) + " को"
        sh, sg = subj_hi(subj, T)
        how_h = "विषय बनाकर" if how == "ārabbha" else "महत्व देकर"
        return f"{oh} {how_h} {sh}" + (f" {ARISE_G[sg]}" if verb else "")
    m = ARISE_RE.match(core)
    if m:
        subj, verb = m.groups()
        sh, sg = subj_hi(subj, T)
        if sh is not None:
            return f"{sh} {ARISE_G[sg]}"
    m = REV_RE.match(core)
    if m:
        person, ob, garu, verb = m.groups()
        return rev_hi(person, ob, garu, verb, T)
    m = SD_RE.match(core)
    if m and (m.group(3) or m.group(4)):
        label, pre, subj, dat = m.groups()
        out = []
        if label:
            out.append(D.LABEL[label])
        if pre:
            out.append(PREFIX[pre])
        if subj:
            sh, _ = subj_hi(subj, T)
            if sh is None:
                return unknown("CLAUSE", g)
            out.append(sh if dat else sh.rstrip(","))
        if dat:
            dh = dat_hi(dat, T)
            if dh is None:
                return unknown("CLAUSE", g)
            out.append(dh)
        return " ".join(out)
    if NLIST_RE.match(core):
        return nlist_hi(core, NOUN_D, T)
    if g in D.ACTIONS:
        return fill(D.ACTIONS[g], toks, T)
    return unknown("CLAUSE", g)


# ---------------------------------------------------------------- 6. line translator


def note_hi(content, T):
    """A note: sentences split at '. ', parts at ', ' when the whole is not in the table."""
    c = content.strip()
    end = ""
    if c.endswith("."):
        c, end = c[:-1], "।"
    g, toks = gen(c)
    if g in NOTE:
        return fill(NOTE[g], toks, T) + end
    sents = c.split(". ")
    if len(sents) > 1:
        return "। ".join(note_hi(s, T) for s in sents) + end
    parts = c.split(", ")
    if len(parts) > 1:
        return ", ".join(note_hi(p, T) for p in parts) + end
    return unknown("NOTE", g) + end


def translate_line(line, T):
    if line.startswith("#"):
        return heading(line)
    if line in D.LINE_X:
        return D.LINE_X[line]
    inserts = []
    for v, (br, anchor) in D.VARIANTS_X.items():
        if v in line:
            line = line.replace(" " + v, "")
            inserts.append((anchor, br))
    if "{" in line:
        return unknown("VARIANT", line)
    for a, b in S.SLIPS.items():
        line = line.replace(a, b)
    m = re.search(r"(\w+ttikaṃ) niṭṭhitaṃ", line)
    if m and m.group(1)[0].upper() + m.group(1)[1:] in HEAD:
        DONE["h"] = HEAD[m.group(1)[0].upper() + m.group(1)[1:]] + " समाप्त"
        line = line.replace(m.group(0), "zzdone")
    for a, (b, why) in D.SLIPS_X.items():
        if a in line:
            line = line.replace(a, b)
            LOG[f"slip: {why}"] += 1
    text = T.normalize(S.lower_initials(line))
    store = []

    def keep(h):
        store.append(h)
        return f"{len(store) - 1}"

    text = re.sub(r"\(([^()]*[^\d().][^()]*)\)", lambda m: keep("(" + note_hi(m.group(1), T) + ")"), text)
    if is_count(text):
        return finish(count_hi(text), store)
    text = VARA_RE.sub(lambda m: keep(frame_hi(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), T)),
                       text)
    state = {"g": None}
    sents = re.split(r"( – |\. )", text)
    for i in range(0, len(sents), 2):
        s = sents[i]

        def one(m, s=s):
            if not m.group(2):
                # no subject before the verb: take it from the clause-initial subjects of this sentence
                cands = [x.group(1) for x in SUBJ_START.finditer(s[: m.start()])]
                if len(cands) == 1:
                    state["g"] = subj_hi(cands[0], T)[1]
                elif len(cands) > 1:
                    state["g"] = "mp"
            return def_frame(m, T, keep, state)
        sents[i] = DEF_RE.sub(one, s)
    text = "".join(sents)
    out = []
    for tok in re.split(r"( – |; |, |\. |…pe…|…|\.$)", text):
        if tok in (" – ", "; ", ", ", "…"):
            out.append(tok)
        elif tok == ". ":
            out.append("। ")
        elif tok == ".":
            out.append("।")
        elif tok == "…pe…":
            out.append("…")
        elif tok:
            for part in re.split(r"(\d+|\(\d+\))", tok):
                if not part.strip() or re.fullmatch(r"\d+|\(\d+\)", part):
                    out.append(part)
                else:
                    out.append(clause(part, T))
    hi = finish("".join(out), store)
    for anchor, br in inserts:
        i = 0
        while True:
            j = hi.find(anchor, i)
            if j < 0 and "⁇" in hi:
                break
            assert j >= 0, (anchor, hi[:80])
            k = j + len(anchor)
            if not hi.startswith(" [", k):
                hi = hi[:k] + " " + br + hi[k:]
                break
            i = k
    return hi


def finish(s, store):
    while "" in s:
        s = re.sub(r"(\d+)", lambda m: store[int(m.group(1))], s)
    return s.replace("?।", "?")


# ---------------------------------------------------------------- 7. files

ID_RE = S.ID_RE


def build_file(name, dump=False):
    T = Triad(name)
    CUR["file"] = name
    lines = open(os.path.join(PALI_DIR, name), encoding="utf-8").read().split("\n")
    out, fails = [], 0
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        CUR["id"] = m.group(1) if m else CUR["id"]
        hi = translate_line(body, T)
        if "⁇" in hi:
            fails += 1
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    if not dump:
        with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(out) + "\n")
    return fails


def main():
    dump = "--dump" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    build_res()
    total = 0
    for name in FILES:
        if only and not any(name.startswith(o) for o in only):
            continue
        f = build_file(name, dump=dump)
        total += f
        print(f"{name}: {f} lines with unknowns")
    rows = [f"{c}\t{k}\t{EXAMPLE[(k, g)]}\t{g}" for (k, g), c in
            sorted(UNKNOWN.items(), key=lambda x: (x[0][0], -x[1], x[0][1]))]
    open(os.path.join(HERE, "unknown_2-04_2-08.txt"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(rows) + "\n")
    print(len(UNKNOWN), "unknown keys -> unknown_2-04_2-08.txt")
    for k, v in sorted(LOG.items()):
        print("LOG", v, k)
    if not dump and total:
        print("WARNING: files written with ⁇ lines")


if __name__ == "__main__":
    main()
