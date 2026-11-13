"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 3-03 .. 3-08 (dyad clusters āsava, saññojana, gantha,
ogha/yoga, nīvaraṇa, parāmāsa).

Imports the approved sample builder read-only (R) for every shared formula; adds a small grammar for the dyad items
and the noun phrases of the bodies.  Phrase tables live in lex_3-03_3-08.py.
usage: python -I -B -X utf8 build_rails_3-03_3-08.py [--check] [files...]
  --check : translate everything, print the unknown pieces, write nothing
"""
import collections
import os
import re
import sys

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails"
sys.path.insert(0, RAILS)
import build_rails_sample as R  # noqa: E402  (read-only)
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("lex_3_03_3_08", os.path.join(RAILS, "lex_3-03_3-08.py"))
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
OUT_DIR = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters")
FILES = ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
         "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md"]


class Unknown(Exception):
    pass


# ------------------------------------------------------------------ Hindi helpers

def infl(s, g, n, obl):
    """Inflect the marked words: 'ा~' / 'आ~' -> m.sg.dir ा/आ, m.obl or m.pl े/ए, f ी/ई."""
    if g == "f":
        a, b = "ी", "ई"
    elif n == "s" and not obl:
        a, b = "ा", "आ"
    else:
        a, b = "े", "ए"
    s = s.replace("या~", "य" + a if a == "ा" else b).replace("ा~", a).replace("आ~", b)
    return s.replace("~", "")


def join_and(parts):
    parts = [p for p in parts if p]
    if len(parts) <= 1:
        return "".join(parts)
    return ", ".join(parts[:-1]) + " और " + parts[-1]


def join_alt(parts, n):
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + (" और " if n == "p" else " या ") + parts[-1]


ARISE = {("s", "m"): "उत्पन्न होता है", ("s", "f"): "उत्पन्न होती है",
         ("p", "m"): "उत्पन्न होते हैं", ("p", "f"): "उत्पन्न होती हैं"}
GNMAP = {("s", "m"): "ms", ("s", "f"): "fs", ("p", "m"): "mp", ("p", "f"): "fp"}

# ------------------------------------------------------------------ per-file state

G = {}        # current gocchaka strings
LEX = {}      # current lexicon: pali word -> entry
KEY = ""      # current file key "3-03" ...


def setup(key):
    global G, LEX, KEY
    KEY = key
    G = L.GOC.get(key, {})
    LEX = L.build_lex(key)


def normalize(text):
    for stem, tok in G.get("stems", []):
        text = re.sub(rf"(?<!\w)(no)?{stem}", lambda m: (m.group(1) or "") + tok, text)
    return re.sub(r"(?<=GG)a(?=sampayutt|vippayutt|cittasamaṅg)", "", text)


def fill(s):
    """Fill the gocchaka placeholders {w} {rupi} … of a phrase-table string."""
    return s.format(**G) if "{" in s else s


# ------------------------------------------------------------------ tokens and noun phrases

class Tok:
    def __init__(self, w, ca=False):
        self.w = w
        self.ca = ca
        self.e = LEX.get(w)

    def __repr__(self):
        return self.w + ("+ca" if self.ca else "")


def tokenize(text):
    """Split a Pāli phrase into tokens; enclitic -ñca / -ñceva / separate ca become flags."""
    src = text
    text = re.sub(r"ñceva(?!\w)", "ṃ ceva", text.strip())
    text = re.sub(r"ñca(?!\w)", "ṃ ca", text)
    for a, b in L.ITEM_JOIN:
        text = re.sub(a, b, text)
    for a, b in L.JOIN.items():
        text = re.sub(rf"(?<!\w){re.escape(a)}(?!\w)", b, text)
    toks = []
    for w in text.split():
        if w in ("ca", "ceva"):
            if not toks:
                raise Unknown(f"ca at start: {src!r}")
            toks[-1].ca = True
            continue
        if w in LEX:
            toks.append(Tok(w))
            continue
        raise Unknown(f"word {w!r} in {src!r}")
    return toks


def is_noun(t, nxt):
    e = t.e
    if e["k"] == "N":
        return True
    if e["k"] == "GN":  # gocchaka noun: adjective only before an allowed head
        return not (nxt is not None and nxt.e["k"] == "N" and nxt.e.get("head"))
    return False


def conjuncts(toks):
    out, cur = [], []
    for i, t in enumerate(toks):
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        cur.append(t)
        noun = is_noun(t, nxt)
        if noun:
            out.append(cur)
            cur = []
        elif t.ca:
            if nxt is not None and nxt.e["k"] in ("N",) and not t.e["k"] == "NUM":
                continue  # 'sampayuttakā ca khandhā': ca opens this conjunct
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def render_conj(c, obl):
    """One conjunct -> (hindi, g, n, case)."""
    head = c[-1]
    e = head.e
    if e["k"] in ("N", "GN"):
        mods = c[:-1]
        noun = e
        n = e["n"]
    else:
        mods = c
        noun = None
        n = e["n"]
    num = None
    for t in mods:
        if t.e["k"] == "NUM":
            num = t.e
    if num and num["v"] > 1:
        n = "p"
    if noun:
        if noun["k"] == "GN":
            forms = (G["sg"], G["sgo"], G["pl"], G["plo"], G["g"])
        else:
            forms = noun["f"]
        g = forms[4]
        nh = fill(forms[(0 if n == "s" else 2) + (1 if obl else 0)])
    else:
        g = e.get("g", "m")
        nh = ""
    # modifiers, Pāli order; consecutive 'alt' adjectives form one alternative group
    parts, group = [], []

    def flush():
        if group:
            parts.append(("A", join_alt([infl(fill(t.e["h"]), g, n, obl) for t in group], n)))
            group.clear()

    for t in mods:
        k = t.e["k"]
        if k == "A" and t.e.get("alt"):
            group.append(t)
            continue
        flush()
        if k == "A":
            parts.append(("A", infl(fill(t.e["h"]), g, n, obl)))
        elif k == "D":
            parts.append(("D", infl(fill(t.e["h"]), g, n, obl)))
        elif k == "NUM":
            parts.append(("NUM", t.e["h"]))
        elif k == "GN":  # gocchaka word used as adjective before a head noun
            parts.append(("A", fill(G["rupi"])))
        else:
            raise Unknown(f"modifier {t.w}")
    flush()
    s = ""
    prev = None
    for kind, h in parts:
        if not s:
            s = h
        elif kind == "A" and prev == "A":
            s += ", " + h
        else:
            s += " " + h
        prev = kind
    if nh:
        s = (s + " " + nh) if s else nh
    if not s:
        raise Unknown(f"empty conjunct {c}")
    case = e.get("c", "n")
    return s, g, n, case


def np_hi(text, obl=False):
    """Pāli noun phrase (possibly coordinated) -> (hindi, g, n)."""
    if text in L.NP:
        h, g, n = L.NP[text]
        if isinstance(h, tuple):
            h = h[1] if obl else h[0]
        return fill(h), g, n
    if text in L.CLAUSE and text != "taṃ":
        return fill(L.CLAUSE[text]), "m", "s"
    toks = tokenize(text)
    cs = [render_conj(c, obl) for c in conjuncts(toks)]
    if len(cs) == 1:
        return cs[0][0], cs[0][1], cs[0][2]
    g = "f" if all(x[1] == "f" for x in cs) else "m"
    return join_and([x[0] for x in cs]), g, "p"


def sd_hi(text):
    """'SUBJ DAT…' (subject optional) -> (subject hindi or None, gn or None, dative hindi or '')."""
    text = text.replace(",", "")
    if text in L.SD:
        h, gn = L.SD[text]
        return fill(h), gn, ""
    lab = ""
    first = text.split(" ", 1)
    if len(first) == 2 and first[0] in L.LABEL:
        lab, text = L.LABEL[first[0]] + ", ", first[1]
    sh, gn, dh = _sd(text)
    if lab:
        if sh:
            sh = lab + sh
        else:
            dh = lab + dh
    return sh, gn, dh


def _sd(text):
    toks = tokenize(text)
    if all(t.e["k"] == "NUM" for t in toks):
        raise Unknown(f"number only {text!r}")
    cs = conjuncts(toks)
    subj, dat = [], []
    for c in cs:
        e = c[-1].e
        case = e.get("c", "n")
        if case == "n" and not dat:
            subj.append(c)
        elif case == "d":
            dat.append(c)
        else:
            raise Unknown(f"case order in {text!r}")
    sh, gn = None, None
    if subj:
        rs = [render_conj(c, False) for c in subj]
        if len(rs) == 1:
            sh, gn = rs[0][0], GNMAP[(rs[0][2], rs[0][1])]
        else:
            sh = join_and([x[0] for x in rs])
            gn = "fp" if all(x[1] == "f" for x in rs) else "mp"
    dh = ""
    if dat:
        rd = [render_conj(c, True)[0] for c in dat]
        if len(rd) == 2:
            dh = f"{rd[0]} के लिए और {rd[1]} के लिए"
        else:
            dh = join_and(rd) + " के लिए"
    return sh, gn, dh


def subj_dat(sh, dh):
    if sh and dh:
        w1 = sh.split()
        w2 = dh.split()
        if w1[0] == w2[0] or w1[-1] == w2[0] or w1[-1].rstrip("ों") == w2[0].rstrip("ों"):
            return f"{sh}, {dh}"
        return f"{sh} {dh}"
    return sh or dh or ""


# ------------------------------------------------------------------ items (X dhammo …)

def item_tokens(text):
    """'GGañca noGGañca' / 'GGo ca noGGo ca' / 'GGassa ca noGGassa ca' -> list of item keys."""
    text = re.sub(r"ñceva(?!\w)", "ṃ ceva", text.strip())
    text = re.sub(r"ñca(?!\w)", "ṃ ca", text)
    for a, b in L.ITEM_JOIN:
        text = re.sub(a, b, text)
    keys = []
    for w in text.split():
        if w in ("ca",):
            continue
        m = re.fullmatch(r"(.+?)(aṃ|o|ā|assa|ānaṃ|e)", w)
        if not m or m.group(1) not in L.ITEM:
            raise Unknown(f"item {w!r} in {text!r}")
        keys.append(m.group(1))
    return keys


def item_adj(k):
    return fill(L.ITEM[k])


def item_np(keys, case):
    """case: 'acc' (oblique sg each), 'nom' (subject), 'dat'. Returns (hindi, n)."""
    if len(keys) == 1:
        h = infl(item_adj(keys[0]), "f", "s", False) + " परिघटना"
        return (h + " के लिए" if case == "dat" else h), "s"
    composite = any(k in L.COMPOSITE for k in keys)
    if case == "nom" and not composite:
        return join_and([infl(item_adj(k), "f", "p", False) for k in keys]) + " परिघटनाएँ", "p"
    h = join_and([infl(item_adj(k), "f", "s", False) + " परिघटना" for k in keys])
    return (h + " के लिए" if case == "dat" else h), "p"


REL_HI = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "nissāya": "के आश्रय से",
          "saṃsaṭṭho": "से घुल-मिलकर", "saṃsaṭṭhā": "से घुल-मिलकर", "saṃsaṭṭhaṃ": "से घुल-मिलकर","sampayutto": "से जुड़कर",
          "sampayuttā": "से जुड़कर", "sahajāto": "के साथ जन्म लेकर", "sahajātā": "के साथ जन्म लेकर"}
REL_ALT = "paṭicca|paccayā|nissāya|saṃsaṭṭho|saṃsaṭṭhā|saṃsaṭṭhaṃ|sampayutto|sampayuttā|sahajāto|sahajātā"
K_ALT = "|".join(sorted(R.KEYS, key=len, reverse=True))
HEAD_FRAME = re.compile(
    rf"(?<![\w])([^\s.;–…()\x01\x02][^.;–…()\x01\x02]*?) dhammaṃ ({REL_ALT}) ([^.;–…()\x01\x02]*?) "
    rf"(dhammo uppajjati|dhammā uppajjanti)(?: ({R.CHAIN_RE}))?(?=$|[ .,;…(\x01])")
HEAD_SHORT = re.compile(rf"(?<![\w])([^\s.;–…()\x01\x02][^.;–…()\x01\x02]*?) dhammaṃ ({REL_ALT})(?=…)")
PANHA_HEAD = re.compile(
    rf"(?<![\w])([^\s.;–…()\x01\x02][^.;–…()\x01\x02]*?) (dhammo|dhammā) ([^.;–…()\x01\x02]*?) dhammassa ({K_ALT})paccayena paccayo")


def head_frame(m):
    x, rel, y, verb, chain = m.groups()
    xh, _ = item_np(item_tokens(x), "acc")
    yh, yn = item_np(item_tokens(y), "nom")
    arise = "उत्पन्न होती है" if yn == "s" and verb.startswith("dhammo") else "उत्पन्न होती हैं"
    if yn == "s" and verb.startswith("dhammā"):
        arise = "उत्पन्न होती हैं"
    if chain:
        return f"{xh} {REL_HI[rel]} {yh} {R.CH(chain)} {arise}"
    return f"{xh} {REL_HI[rel]} {yh} {arise}"


def head_short(m):
    x, rel = m.groups()
    xh, _ = item_np(item_tokens(x), "acc")
    return f"{xh} {REL_HI[rel]}"


STATE = {"gn": None}
HEADGN = {}


def panha_head(m):
    x, num, y, k = m.groups()
    xh, xn = item_np(item_tokens(x), "nom")
    yh, _ = item_np(item_tokens(y), "dat")
    gn = "fs" if (num == "dhammo" and xn == "s") else "fp"
    STATE["gn"] = gn
    return f"{xh}, {yh} {R.INS(k, gn)}"


PANHA_HEAD2 = re.compile(
    rf"(?<![\w])([^\s.;–…()\x01\x02][^.;–…()\x01\x02]*?) (dhammo|dhammā) ([^.;–…()\x01\x02]*?) dhammassa"
    rf"(?= (?:sahajātaṃ|purejātaṃ|pacchājātaṃ|āhāraṃ|indriyaṃ))")


def panha_head2(m):
    x, num, y = m.groups()
    xh, _ = item_np(item_tokens(x), "nom")
    yh, _ = item_np(item_tokens(y), "dat")
    return f"{xh}, {yh}"


# ------------------------------------------------------------------ predicate clauses in the bodies

PRED = re.compile(rf"(?<![\w])(na )?({K_ALT})paccayena paccayo")
HARD = re.compile(r" – |; |\. |…pe…|…|[\x01\x02]")


def predicates(text, store):
    """Replace every '… Xpaccayena paccayo' with a placeholder, taking the subject and datives before it."""
    out = []
    pos = 0
    for m in PRED.finditer(text):
        seg = text[pos:m.start()]
        for hm in re.finditer(r"\x01(\d+)\x01", seg):
            if int(hm.group(1)) in HEADGN:
                STATE["gn"] = HEADGN[int(hm.group(1))]
        # chunk = after the last hard delimiter inside seg
        cut = 0
        for d in HARD.finditer(seg):
            cut = d.end()
        lead, chunk = seg[:cut], seg[cut:]
        sp = re.match(r"[ ,]*", chunk).group(0)
        lead, chunk = lead + sp, chunk[len(sp):]
        # a leading comma-separated part that is not subject/dative stays outside
        pieces = chunk.split(", ")
        res = None
        for i in range(len(pieces)):
            cand = ", ".join(pieces[i:])
            try:
                res = sd_hi(cand.strip()) if cand.strip() else (None, None, "")
                lead += ", ".join(pieces[:i]) + (", " if i else "")
                break
            except Unknown:
                continue
        if res is None:
            raise Unknown(f"predicate chunk {chunk!r}")
        sh, gn, dh = res
        if gn:
            STATE["gn"] = gn
        g = STATE["gn"] or "mp"
        k = m.group(2)
        ins = R.NINS(k, g) if m.group(1) else R.INS(k, g)
        h = subj_dat(sh, dh)
        store.append((h + " " + ins) if h else ins)
        out.append(lead + f"\x02{len(store) - 1}\x02")
        pos = m.end()
    out.append(text[pos:])
    return "".join(out)


# ------------------------------------------------------------------ clauses

def clause(piece):
    core = piece.strip()
    if not core:
        return piece
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    return lead + clause_core(core) + trail


def clause_core(core):
    if core == ".":
        return "।"
    if core in L.CLAUSE:
        return fill(L.CLAUSE[core])
    if core in R.CLAUSE and core not in L.CLAUSE_BLOCK:
        return R.CLAUSE[core]
    if core in R.NUM:
        return R.NUM[core]
    if core in R.P_ABL:
        return R.P_ABL[core]
    if core in R.P_NABL:
        return R.P_NABL[core]
    if core in L.LABEL:
        return L.LABEL[core]
    if is_count(core):
        return R.count_hi(core)
    if core.endswith(" dhammaṃ"):
        return item_np(item_tokens(core[:-8]), "acc")[0]
    # prefix
    pre = ""
    m = re.match(r"^(arūpe|paṭisandhikkhaṇe|ahetukapaṭisandhikkhaṇe) (.+)$", core)
    if m:
        pre = R.PREFIX[m.group(1)] + " "
        core = m.group(2)
    # X REL Y
    m = re.fullmatch(rf"(.+?) ({REL_ALT})(?: (.+))?", core)
    if m:
        x, rel, y = m.groups()
        xh = np_hi(x, obl=True)[0]
        s = f"{xh} {REL_HI[rel]}"
        if y:
            s += " " + np_hi(y)[0]
        return pre + s
    m = re.fullmatch(r"(.+?) upanissāya (.+)", core)
    if m:
        r2 = m.group(2)
        if r2 in L.CLAUSE:
            rest = fill(L.CLAUSE[r2])
        else:
            mv = re.fullmatch(r"(.+) (uppajjati|uppajjanti)", r2)
            if mv:
                yh, g, n = np_hi(mv.group(1))
                rest = f"{yh} {ARISE[(n, g)]}"
            else:
                rest = np_hi(r2)[0]
        return pre + np_hi(m.group(1), obl=True)[0] + " के प्रबल आश्रय से " + rest
    # a label without its dash ('Ārammaṇādhipati X …')
    fw = core.split(" ", 1)
    if len(fw) == 2 and fw[0] in L.LABEL:
        return pre + L.LABEL[fw[0]] + ", " + clause_core(fw[1])
    # X ārabbha / garuṃ katvā Y uppajjati (Y and the verb may be elided)
    m = re.fullmatch(r"(.+?) (ārabbha|garuṃ katvā)(?: (.+?))?(?: (uppajjati|uppajjanti))?", core)
    if m and not (m.group(3) or "").startswith(("assādeti", "paccavekkh", "taṃ assādeti")):
        x, how, y, v = m.groups()
        if y:
            yh, g, n = np_hi(y)
        else:
            yh, g, n = "", "m", "s"
        how_h = "को विषय बनाकर" if how == "ārabbha" else "को महत्व देकर"
        if x == "taṃ":
            xh = "उसे"
            how_h = how_h[3:]
        else:
            xh = np_hi(x, obl=True)[0]
        s = f"{xh} {how_h}"
        if yh:
            s += " " + yh
        if v:
            s += " " + ARISE[(n, g)]
        return pre + s
    m = re.fullmatch(r"(.+?) (uppajjati|uppajjanti)", core)
    if m:
        yh, g, n = np_hi(m.group(1))
        return pre + f"{yh} {ARISE[(n, g)]}"
    # X (garuṃ katvā) assādeti abhinandati
    m = re.fullmatch(r"(.+?) garuṃ katvā taṃ assādeti abhinandati", core)
    if m:
        xh, g, n = np_hi(m.group(1), obl=True)
        return pre + f"{xh} को महत्व देकर उसका " + R.SAVOURS.format(p="उसमें")
    m = re.fullmatch(r"(.+?) (garuṃ katvā )?assādeti abhinandati", core)
    if m:
        xh, g, n = np_hi(m.group(1), obl=True)
        p = "उनमें" if n == "p" else "उसमें"
        if m.group(2):
            return pre + f"{xh} को महत्व देकर {'उनका' if n == 'p' else 'उसका'} " + R.SAVOURS.format(p=p)
        return pre + f"{xh} का " + R.SAVOURS.format(p=p)
    m = re.fullmatch(r"(.+?) (garuṃ katvā )?assādeti", core)
    if m:
        xh, g, n = np_hi(m.group(1), obl=True)
        if m.group(2):
            return pre + f"{xh} को महत्व देकर {'उनका' if n == 'p' else 'उसका'} रस लेता है"
        return pre + f"{xh} का रस लेता है"
    m = re.fullmatch(r"(.+?) upanissāya", core)
    if m:
        return pre + np_hi(m.group(1), obl=True)[0] + " के प्रबल आश्रय से"
    m = re.fullmatch(r"cetopariyañāṇena (\S+?)a?cittasamaṅgissa cittaṃ (jānāti|jānanti)", core)
    if m and m.group(1) in L.ITEM:
        adj = infl(fill(L.ITEM[m.group(1)]), "m", "s", True)
        v = "जानता है" if m.group(2) == "jānāti" else "जानते हैं"
        return pre + f"{R.CETOPARIYA} {adj} मन से युक्त व्यक्ति के मन को {v}"
    m = re.fullmatch(r"(.+?) aniccato dukkhato anattato (vipassati|vipassanti)", core)
    if m:
        x = m.group(1)
        subj = ""
        for s_p, s_h in L.SUBJ_PERSON.items():
            if x.startswith(s_p + " "):
                subj, x = s_h + " ", x[len(s_p) + 1:]
                break
        v = R.VIPASSATI["s" if m.group(2) == "vipassati" else "p"]
        return pre + subj + np_hi(x, obl=True)[0] + f" को {R.ANICCA} {v}"
    m = re.fullmatch(r"(.+?) aniccato (vipassati|vipassanti)", core)
    if m:
        v = R.VIPASSATI["s" if m.group(2) == "vipassati" else "p"]
        return pre + np_hi(m.group(1), obl=True)[0] + f" को अनित्य के रूप में {v}"
    m = re.fullmatch(r"(.+?) aniccato", core)
    if m:
        return pre + np_hi(m.group(1), obl=True)[0] + " को अनित्य"
    m = re.fullmatch(r"(.+?) (garuṃ katvā )?(paccavekkhati|paccavekkhanti)", core)
    if m:
        x, gk, v = m.groups()
        subj = ""
        for s_p, s_h in L.SUBJ_PERSON.items():
            if x.startswith(s_p + " "):
                subj, x = s_h + " ", x[len(s_p) + 1:]
                break
        rv = R.REVIEW["s" if v == "paccavekkhati" else "p"]
        if x == "taṃ":
            return pre + subj + (f"उसे महत्व देकर {rv}" if gk else f"उस पर {rv}")
        xh = np_hi(x, obl=True)[0]
        return pre + subj + (f"{xh} को महत्व देकर {rv}" if gk else f"{xh} पर {rv}")
    # subject + datives without predicate (elided)
    try:
        sh, gn, dh = sd_hi(core)
        if dh:
            return pre + subj_dat(sh, dh)
    except Unknown:
        pass
    # bare noun phrase (oblique when the Pāli is an accusative plural in -e)
    h, g, n = np_hi(core, obl=core.split()[-1].endswith("e"))
    return pre + h


# ------------------------------------------------------------------ line translator

ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)((?:\d+(?:-\d+)?\.? )?)(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    h = L.HEAD.get(body) or R.HEAD.get(body)
    if h is None:
        raise Unknown(f"heading {body!r}")
    return f"{hashes} {st}{num}{fill(h)}{en}"


def is_count(text):
    toks = [t for t in re.split(r"(…pe…|…|, |; | |\.)", text) if t and t not in ("…pe…", "…", ", ", "; ", " ", ".")]
    words = set(R.P_ABL) | set(R.P_NABL) | set(R.P_LOC) | set(R.P_NLOC) | set(R.NUM)
    return bool(toks) and all(t in words for t in toks) and any(t in R.NUM for t in toks)


def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    if line in L.LINE_HAND:
        return fill(L.LINE_HAND[line])
    m = re.fullmatch(r"(\S+) (?:niṭṭhitaṃ|niṭṭhito)\.", line)
    if m:
        h = L.HEAD.get(m.group(1)) or R.HEAD.get(m.group(1))
        if h is None:
            raise Unknown(f"closing {line!r}")
        return f"{h} समाप्त।"
    inserts = []
    for v, (kind, anchor) in L.VARIANTS.items():
        if v in line:
            line = line.replace(" " + v, "")
            inserts.append((anchor, R.variant_hi(v, kind)))
    for a, b in L.SLIPS.items():
        line = line.replace(a, b)
    text = normalize(R.lower_initials(line))
    store = []
    STATE["gn"] = None

    def keep(h):
        store.append(h)
        return f"\x01{len(store) - 1}\x01"

    def note(m):
        n = m.group(1)
        if re.fullmatch(r"\d+", n):
            return m.group(0)
        if n not in L.NOTE:
            raise Unknown(f"note ({n})")
        return keep("(" + fill(L.NOTE[n]) + ")")

    text = re.sub(r"\(([^()]*)\)", note, text)
    # counting lines (possibly with notes between the counts)
    chunks = re.split(r"(\x01\d+\x01)", text)
    plain = [c for c in chunks if not c.startswith("\x01") and c.strip(" .,")]
    if plain and all(is_count(c.strip(" ,")) or is_count(c.strip(" .,")) for c in plain):
        out = []
        for c in chunks:
            if c.startswith("\x01") or not c.strip(" .,"):
                out.append(c.replace(".", "।"))
                continue
            lead = c[: len(c) - len(c.lstrip(" ,"))]
            core = c.strip(" ,")
            parts = core.split(". ")
            hi = "। ".join(R.count_hi(p if (i == len(parts) - 1) else p + ".")[:-1] if i < len(parts) - 1
                           else R.count_hi(p) for i, p in enumerate(parts))
            out.append(lead + hi + c[len(lead) + len(core):])
        return _finish("".join(out), store, inserts)
    # head frames
    text = HEAD_FRAME.sub(lambda m: keep(head_frame(m)), text)
    text = HEAD_SHORT.sub(lambda m: keep(head_short(m)), text)
    HEADGN.clear()

    def keep_head(m):
        h = panha_head(m)
        HEADGN[len(store)] = STATE["gn"]
        return keep(h)

    text = PANHA_HEAD.sub(keep_head, text)
    text = PANHA_HEAD2.sub(lambda m: keep(panha_head2(m)), text)
    # predicates of the bodies (placeholders \x02n\x02)
    st2 = []
    text = predicates(text, st2)
    # pieces
    out = []
    for tok in re.split(r"( – |; |, |\. |…pe…|…|\.$|\x01\d+\x01|\x02\d+\x02)", text):
        if tok in (" – ", "; ", ", ", "…"):
            out.append(tok)
        elif tok == ". ":
            out.append("। ")
        elif tok == ".":
            out.append("।")
        elif tok == "…pe…":
            out.append("…")
        elif tok.startswith("\x01") or tok.startswith("\x02"):
            out.append(tok)
        elif tok:
            for part in re.split(r"(\(\d+\))", tok):
                if not part.strip() or re.fullmatch(r"\(\d+\)", part.strip()):
                    out.append(part)
                else:
                    out.append(clause(part))
    s = "".join(out)
    s = re.sub(r"\x02(\d+)\x02", lambda m: st2[int(m.group(1))], s)
    return _finish(s, store, inserts)


def _finish(s, store, inserts):
    s = re.sub(r"\x01(\d+)\x01", lambda m: store[int(m.group(1))], s)
    s = s.replace("?।", "?")
    for anchor, br in inserts:
        assert anchor in s, (anchor, s)
        s = s.replace(anchor, anchor + " " + br, 1)
    return s


# ------------------------------------------------------------------ driver

def build(name, check=False, unknown=None):
    setup(name[:4])
    lines = open(os.path.join(PALI_DIR, name), encoding="utf-8").read().split("\n")
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
        except (Unknown, KeyError) as ex:
            if unknown is None:
                raise
            unknown[str(ex)] += 1
            hi = "??"
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    if not check:
        with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(out) + "\n")
    return out


if __name__ == "__main__":
    check = "--check" in sys.argv
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or FILES
    unk = collections.Counter() if check else None
    for nm in names:
        nm = next(f for f in FILES if f.startswith(nm[:4]))
        build(nm, check=check, unknown=unk)
        print("built" if not check else "checked", nm)
    if check:
        print("unknown:", len(unk))
        for k, v in sorted(unk.items(), key=lambda x: -x[1]):
            print(v, k)
