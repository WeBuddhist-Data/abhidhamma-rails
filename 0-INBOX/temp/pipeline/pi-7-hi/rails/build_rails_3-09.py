"""pi-7 Paṭṭhāna 3-09-mahantaraduka.md -> Hindi plain RAILS.

Uses the approved sample constants read-only (build_rails_sample as R).
Run:  python -I -B -X utf8 build_rails_3-09.py           (builds the output file)
      python -I -B -X utf8 build_rails_3-09.py --unk     (lists untranslated pieces)
"""
import os
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as R  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tables_3_09 import (HEAD9, NOTE9, PIECE9, LABEL9, DYAD_HI, NOUN, ADJ, NUMW, PREFIX9,  # noqa: E402
                         CLOSING9)

SRC = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters\3-09-mahantaraduka.md"
DST = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\3-09-mahantaraduka.md"

UNK = []

# ------------------------------------------------------------------ dyads and item tokens

DYADS = [
    # heading, P stem, N stem, stem class
    ("Sārammaṇadukaṃ", "sārammaṇ", "anārammaṇ", "a"),
    ("Cittadukaṃ", "citt", "nocitt", "a"),
    ("Cetasikadukaṃ", "cetasik", "acetasik", "a"),
    ("Cittasampayuttadukaṃ", "cittasampayutt", "cittavippayutt", "a"),
    ("Cittasaṃsaṭṭhadukaṃ", "cittasaṃsaṭṭh", "cittavisaṃsaṭṭh", "a"),
    ("Cittasamuṭṭhānadukaṃ", "cittasamuṭṭhān", "nocittasamuṭṭhān", "a"),
    ("Cittasahabhūdukaṃ", "cittasahabh", "nocittasahabh", "u"),
    ("Cittānuparivattidukaṃ", "cittānuparivatt", "nocittānuparivatt", "i"),
    ("Cittasaṃsaṭṭhasamuṭṭhānadukaṃ", "cittasaṃsaṭṭhasamuṭṭhān", "nocittasaṃsaṭṭhasamuṭṭhān", "a"),
    ("Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ", "cittasaṃsaṭṭhasamuṭṭhānasahabh", "nocittasaṃsaṭṭhasamuṭṭhānasahabh", "u"),
    ("Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ", "cittasaṃsaṭṭhasamuṭṭhānānuparivatt",
     "nocittasaṃsaṭṭhasamuṭṭhānānuparivatt", "i"),
    ("Ajjhattikadukaṃ", "ajjhattik", "bāhir", "a"),
    ("Upādādukaṃ", "upādā", "noupādā", "x"),
    ("Upādinnadukaṃ", "upādinn", "anupādinn", "a"),
]
DYAD_BY_HEAD = {d[0]: d for d in DYADS}

# Pāli endings -> canonical a-stem ending
END = {
    "a": {"aṃ": "aṃ", "o": "o", "ā": "ā", "e": "e", "assa": "assa", "ānaṃ": "ānaṃ", "añca": "añca",
          "ānañca": "ānañca", "ādhipati": "ādhipati", "acittasamaṅgissa": "acittasamaṅgissa",
          "asamaṅgissa": "asamaṅgissa", "akā": "ā", "ake": "e", "akānaṃ": "ānaṃ", "akānañca": "ānañca"},
    "u": {"uṃ": "aṃ", "ū": "o", "u": "o", "uno": "ā", "ussa": "assa", "ūnaṃ": "ānaṃ", "uñca": "añca",
          "ūnañca": "ānañca"},
    "i": {"iṃ": "aṃ", "i": "o", "ī": "o", "ino": "ā", "issa": "assa", "īnaṃ": "ānaṃ", "iñca": "añca",
          "īnañca": "ānañca"},
}


def tokenize_items(text, dyad):
    """Replace the dyad's item words with ‹P:end› / ‹N:end› tokens."""
    if not dyad:
        return text
    head, ps, ns, cls = dyad
    if cls == "x":  # upādā / noupādā: indeclinable
        text = re.sub(r"(?<!\w)(no)?upādā(ādhipati|dhipati|cittasamaṅgissa)(?!\w)",
                      lambda m: "‹%s:%s›" % ("N" if m.group(1) else "P",
                                             "acittasamaṅgissa" if m.group(2) == "cittasamaṅgissa" else "ādhipati"),
                      text)
        text = re.sub(r"(?<!\w)noupādā(?!\w|rūp)", "‹N:x›", text)
        text = re.sub(r"(?<![\w‹:])upādā(?!\w|rūp)", "‹P:x›", text)
        return text
    ends = sorted(END[cls], key=len, reverse=True)
    alt = "|".join(re.escape(e) for e in ends)
    text = re.sub(rf"(?<!\w){ns}({alt})(?!\w)", lambda m: f"‹N:{END[cls][m.group(1)]}›", text)
    if head == "Cittadukaṃ":
        # citta is an item only together with dhamma (or in a pair with nocitta); elsewhere it is the noun «मन»
        text = re.sub(r"(?<!\w)citt(o|aṃ|assa)(?= dhamm)", lambda m: f"‹P:{m.group(1)}›", text)
        text = re.sub(r"(?<!\w)citt(o ca|assa ca|añca)(?= ‹N:)",
                      lambda m: "‹P:" + {"o ca": "o›", "assa ca": "assa›", "añca": "añca›"}[m.group(1)]
                      + (" ca" if m.group(1) in ("o ca", "assa ca") else ""), text)
        return text
    neg_look = r"(?! rūp|ñca rūp| ca rūp)"
    if head == "Cittasamuṭṭhānadukaṃ":
        # «cittasamuṭṭhānaṃ rūpaṃ» stays the ordinary phrase (mind-produced matter)
        text = re.sub(rf"(?<!\w){ps}({alt})(?!\w){neg_look}",
                      lambda m: f"‹P:{END[cls][m.group(1)]}›", text)
        return text
    if head == "Ajjhattikadukaṃ":
        text = re.sub(rf"(?<!\w){ps}({alt})(?!\w)", lambda m: f"‹P:{END[cls][m.group(1)]}›", text)
        return text
    text = re.sub(rf"(?<!\w){ps}({alt})(?!\w)", lambda m: f"‹P:{END[cls][m.group(1)]}›", text)
    return text


AGREE = {"ms": "ा", "mo": "े", "f": "ी"}


def item_hi(sign, form, dyad):
    tpl = DYAD_HI[dyad[0]][sign]
    return tpl.replace("{a}", AGREE[form])


def fill(s, dyad):
    """Resolve {P:ms} / {N:f} … placeholders."""
    return re.sub(r"\{([PN]):(ms|mo|f)\}", lambda m: item_hi(m.group(1), m.group(2), dyad), s)


def is_short(sign, dyad):
    return " " not in DYAD_HI[dyad[0]][sign]


# ------------------------------------------------------------------ dhamma frames (pre-pass)

STORE = []


def keep(h):
    STORE.append(h)
    return f"⟦{len(STORE) - 1}⟧"


IT = r"‹([PN]):(\w+)›"
DH_PATTERNS = [
    # pairs first
    (re.compile(r"‹P:(?:añca|x)›(?: ca)? ‹N:(?:añca|x)›(?: ca)? dhammaṃ"), "acc2"),
    (re.compile(r"‹P:(?:o|x)› ca ‹N:(?:o|x)› ca dhamm(?:ā|o)"), "nom2"),
    (re.compile(r"‹P:(?:assa|x)› ca ‹N:(?:assa|x)› ca dhammassa"), "dat2"),
    (re.compile(IT + r" dhammaṃ"), "acc1"),
    (re.compile(IT + r" dhammo"), "nom1"),
    (re.compile(IT + r" dhammassa"), "dat1"),
]


def dhamma_prepass(text):
    # «purimā purimā sārammaṇā…pe…»: the noun (dhammā) is elided; Hindi names it, as in the sample formula
    text = re.sub(r"purimā purimā ‹([PN]):ā›(?=…)",
                  lambda m: keep(("NP", "पहले-पहले की {%s:f} परिघटनाएँ" % m.group(1), "fp", "nom")), text)
    for rx, kind in DH_PATTERNS:
        def rep(m, kind=kind):
            if kind == "acc2":
                return keep(("NP", "{P:f} परिघटना और {N:f} परिघटना", "fp", "acc"))
            if kind == "nom2":
                return keep(("NP", "{P:f} और {N:f} परिघटनाएँ", "fp", "nom"))
            if kind == "dat2":
                return keep(("NP", "{P:f} परिघटना और {N:f} परिघटना", "fp", "dat"))
            sign = m.group(1)
            case = {"acc1": "acc", "nom1": "nom", "dat1": "dat"}[kind]
            return keep(("NP", "{%s:f} परिघटना" % sign, "fs", case))
        text = rx.sub(rep, text)
    return text


# ------------------------------------------------------------------ NP parser

CA = "&"


def split_words(s):
    out = []
    for w in s.split():
        if w == "ca":
            out.append(CA)
        elif w.startswith("‹") and w.endswith("añca›"):
            out.append(w.replace("añca›", "aṃ›"))
            out.append(CA)
        elif w.startswith("‹") and w.endswith("ānañca›"):
            out.append(w.replace("ānañca›", "ānaṃ›"))
            out.append(CA)
        elif w.endswith("ñca") and w not in NOUN and w not in ADJ:
            out.append(w[:-3] + "ṃ")
            out.append(CA)
        else:
            out.append(w)
    return out


def item_adj(tok):
    m = re.fullmatch(r"‹([PN]):(\w+)›", tok)
    if not m:
        return None
    sign, end = m.groups()
    case = {"aṃ": "acc", "o": "nom", "ā": "nom", "e": "acc", "assa": "dat", "ānaṃ": "dat", "x": "any"}.get(end)
    if case is None:
        return None
    num = {"ā": "p", "e": "p", "ānaṃ": "p"}.get(end, "s")
    return {"item": sign, "case": case, "n": num}


def _new():
    return {"pre": [], "adjs": [], "num": None, "noun": None, "ca": False, "adj_ca": False}


BARE = {"d": "", "o": "", "g": "m", "n": "p", "case": "acc", "bare": True}


def parse_nps(s, bare=True):
    """Return a list of NPs: dict(pre, adjs, num, noun) or None when a word is unknown.
    A trailing group of adjectives without a noun (an elided noun) is allowed when bare=True."""
    words = split_words(s)
    nps, cur = [], _new()
    i = 0
    while i < len(words):
        w = words[i]
        # multiword lexicon entries (longest first)
        hit = None
        for L in (4, 3, 2):
            if i + L <= len(words):
                cand = " ".join(words[i:i + L])
                if cand in NOUN or cand in ADJ:
                    hit = (cand, L)
                    break
        if hit:
            w, step = hit
        else:
            step = 1
        if w == CA:
            cur["ca"] = True
            if cur["adjs"]:
                cur["adj_ca"] = True
        elif w in NUMW:
            cur["num"] = NUMW[w]
        elif w in ADJ:
            a = ADJ[w]
            (cur["pre"] if a.get("pre") else cur["adjs"]).append(a)
        elif re.fullmatch(r"‹([PN]):ādhipati›", w):
            cur["noun"] = {"d": "{%s:f} प्रधानता" % w[1], "o": "{%s:f} प्रधानता" % w[1], "g": "f", "n": "s",
                           "case": "nom"}
            nps.append(cur)
            cur = _new()
        elif item_adj(w):
            cur["adjs"].append(item_adj(w))
        elif re.fullmatch(r"⟦\d+⟧", w) and STORE[int(w[1:-1])][0] == "NP":
            st = STORE[int(w[1:-1])]
            cur["noun"] = {"d": st[1], "o": st[1], "g": st[2][0], "n": st[2][1], "case": st[3], "ph": True}
            nps.append(cur)
            cur = _new()
        elif w in NOUN:
            cur["noun"] = NOUN[w]
            nps.append(cur)
            cur = _new()
        else:
            return None
        i += step
    if cur["num"] and not cur["adjs"] and not cur["pre"]:
        return None
    if cur["adjs"] or cur["pre"]:
        if not bare:
            return None
        cur["noun"] = dict(BARE)
        cur["noun"]["case"] = cur["adjs"][0].get("case", "acc") if cur["adjs"] else "acc"
        nps.append(cur)
    return nps


def adj_form(a, g, n, obl):
    if g == "f":
        form = "f"
    elif n == "p" or obl:
        form = "mo"
    else:
        form = "ms"
    if "item" in a:
        return "{%s:%s}" % (a["item"], form), a["item"]
    return a[form], None


def np_hi(np, obl, dyad):
    noun = np["noun"]
    g, n = noun["g"], noun["n"]
    if np["num"] and np["num"] != "एक":
        n = "p"
    pre = [adj_form(p, g, n, obl)[0] for p in np["pre"]]
    long_adjs, short_adjs = [], []
    for a in np["adjs"]:
        h, sign = adj_form(a, g, n, obl)
        short = (sign and is_short(sign, dyad)) or (not sign and a.get("short"))
        (short_adjs if short else long_adjs).append(h)
    joiner = " और " if np.get("adj_ca") else ", "
    if np.get("adj_ca") and long_adjs and short_adjs:
        long_adjs, short_adjs = [adj_form(a, g, n, obl)[0] for a in np["adjs"]], []
    parts = list(pre)
    if long_adjs:
        parts.append(joiner.join(long_adjs) + ("," if noun.get("complex") and not np["num"] and not short_adjs else ""))
    if np["num"]:
        parts.append(np["num"])
    if short_adjs:
        parts.append((" और " if np.get("adj_ca") else " ").join(short_adjs) + ("," if noun.get("complex") else ""))
    if not noun.get("bare"):
        parts.append(noun["o"] if obl else noun["d"])
    elif np["adjs"] and all("item" in a and a["case"] == "dat" for a in np["adjs"]):
        parts = [x.replace(":mo}", ":f}") for x in parts] + ["परिघटना"]  # «cittavippayuttassa» without dhammassa
    return " ".join(parts)


def join_and(xs):
    if len(xs) == 1:
        return xs[0]
    return ", ".join(xs[:-1]) + " और " + xs[-1]


def nps_hi(nps, mode, dyad):
    """mode: d (direct), o (oblique, postposition after the whole list), dat (… के लिए)."""
    if mode == "dat":
        hs = [np_hi(np, True, dyad) for np in nps]
        if len(hs) == 2:
            return f"{hs[0]} के लिए और {hs[1]} के लिए"
        return join_and(hs) + " के लिए"
    return join_and([np_hi(np, mode == "o", dyad) for np in nps])


def nps_gender(nps):
    if len(nps) > 1:
        return ("m" if any(np["noun"]["g"] == "m" for np in nps) else "f") + "p"
    np = nps[0]
    n = "p" if (np["noun"]["n"] == "p" or (np["num"] and np["num"] != "एक")) else "s"
    return np["noun"]["g"] + n


def np_case(np):
    return np["noun"].get("case", "nom")


# ------------------------------------------------------------------ conditions

ABL_ALL = dict(R.P_ABL)
ABL_ALL.update(R.P_NABL)
INS_RE = re.compile(r"(?:(na) )?(" + "|".join(sorted(R.KEYS, key=len, reverse=True)) + r")paccayena paccayo$")
GSG = {"ms": "ms", "fs": "fs", "mp": "mp", "fp": "fp"}


# ------------------------------------------------------------------ piece translators

REL = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "saṃsaṭṭhā": "से घुल-मिलकर",
       "saṃsaṭṭho": "से घुल-मिलकर", "saṃsaṭṭhaṃ": "से घुल-मिलकर", "sahajāto": "के साथ जन्म लेकर",
       "sahajātā": "के साथ जन्म लेकर", "nissāya": "के आश्रय से", "sampayutto": "से जुड़कर",
       "sampayuttā": "से जुड़कर"}
FRAME_RE = re.compile(r"^⟦(\d+)⟧ (paṭicca|paccayā|saṃsaṭṭho|sahajāto|nissāya|sampayutto) ⟦(\d+)⟧ "
                      r"(?:uppajjati|uppajjanti)(?: (.+))?$")
ARISE = {"s": "उत्पन्न होती है", "p": "उत्पन्न होती हैं"}
VERB_ARISE = {"ms": "उत्पन्न होता है", "fs": "उत्पन्न होती है", "mp": "उत्पन्न होते हैं", "fp": "उत्पन्न होती हैं"}


def chain_hi(ch):
    words = ch.split(" ")
    if all(w in ABL_ALL for w in words):
        return ", ".join(ABL_ALL[w] for w in words)
    return None


def tr_frame(m):
    x, rel, y, ch = m.groups()
    xs, ys = STORE[int(x)], STORE[int(y)]
    yh, yg = ys[1], ys[2]
    rel_hi = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "saṃsaṭṭho": "से घुल-मिलकर",
              "sahajāto": "के साथ जन्म लेकर", "nissāya": "के आश्रय से", "sampayutto": "से जुड़कर"}[rel]
    out = f"{xs[1]} {rel_hi} {yh}"
    num = ""
    if ch and ch.split(" ")[-1] in R.NUM and len(ch.split(" ")) > 1:
        num = " " + R.NUM[ch.split(" ")[-1]]
        ch = ch.rsplit(" ", 1)[0]
    if ch:
        c = chain_hi(ch)
        if c is None:
            return None
        out += " " + c
    return out + " " + ARISE[yg[1]] + num


BODY_RELS = ["paṭicca", "paccayā", "saṃsaṭṭhā", "saṃsaṭṭho", "saṃsaṭṭhaṃ"]
BODY_RE = re.compile(r"^(?:(" + "|".join(PREFIX9) + r") )?(.*?)(?: (" + "|".join(BODY_RELS) + r")(?: (.+))?)?$")
AROUSE_RE = re.compile(r"^(.+?) (ārabbha|garuṃ katvā) (.+) (uppajjati|uppajjanti)$")


def tr_body(p, dyad):
    """[PREFIX] NP_acc [REL [NP_nom]]  |  PREFIX  |  NP alone."""
    if p in PREFIX9:
        return PREFIX9[p]
    m = AROUSE_RE.match(p)
    if m:
        a, how, b, verb = m.groups()
        na, nb = (None if a == "taṃ" else parse_nps(a, bare=False)), parse_nps(b, bare=False)
        if (na or a == "taṃ") and nb:
            g = nps_gender(nb)
            if verb == "uppajjanti" and g[1] == "s":
                g = g[0] + "p"
            how_hi = "विषय बनाकर" if how == "ārabbha" else "महत्व देकर"
            obj = "उसे" if a == "taṃ" else nps_hi(na, "o", dyad) + " को"
            return f"{obj} {how_hi} {nps_hi(nb, 'd', dyad)} {VERB_ARISE[g]}"
    m = re.match(r"^(.+) (uppajjati|uppajjanti)$", p)
    if m and not any(f" {r} " in p for r in BODY_RELS):
        nb = parse_nps(m.group(1), bare=False)
        if nb:
            g = nps_gender(nb)
            if m.group(2) == "uppajjanti" and g[1] == "s":
                g = g[0] + "p"
            return f"{nps_hi(nb, 'd', dyad)} {VERB_ARISE[g]}"
    m = BODY_RE.match(p)
    if not m:
        return None
    pre, subj, rel, obj = m.groups()
    if not subj:
        return None
    ns = parse_nps(subj)
    if ns is None:
        return None
    out = [PREFIX9[pre]] if pre else []
    if rel:
        out.append(nps_hi(ns, "o", dyad) + " " + REL[rel])
        if obj:
            no = parse_nps(obj)
            if no is None:
                return None
            out.append(nps_hi(no, "d", dyad))
    else:
        # bare NP: accusative -> oblique (object of an elided paṭicca), nominative -> direct
        cases = {np_case(np) for np in ns}
        out.append(nps_hi(ns, "o" if cases <= {"acc"} else "d", dyad))
    return " ".join(out)


def tr_panha(p, dyad, state):
    """[PREFIX] ([SUBJ…] [DAT…])+ [na Cpaccayena paccayo]."""
    m = INS_RE.search(p)
    verb = None
    rest = p
    if m:
        neg, k = m.groups()
        rest = p[: m.start()].strip()
        verb = (neg, k)
    pre = None
    for pf in sorted(PREFIX9, key=len, reverse=True):
        if rest == pf or rest.startswith(pf + " "):
            pre, rest = PREFIX9[pf], rest[len(pf):].strip()
            break
    groups = []
    if rest:
        nps = parse_nps(rest)
        if nps is None:
            return None
        cur = None
        for np in nps:
            is_dat = np_case(np) == "dat"
            if cur is None or (not is_dat and cur[1]):
                cur = ([], [])
                groups.append(cur)
            (cur[1] if is_dat else cur[0]).append(np)
    if not groups and not verb:
        return None
    parts = [pre] if pre else []
    texts = []
    last_subj = None
    for subj, dats in groups:
        t = []
        if subj:
            sh = nps_hi(subj, "d", dyad)
            last_subj = subj
            if dats:
                first = nps_hi(dats, "dat", dyad).split(" ")[0]
                last = sh.split(" ")[-1]
                d0 = dats[0]
                bare_mind = d0["noun"].get("d") == "मन" and not d0["adjs"] and not d0["pre"]
                if (subj[0]["noun"].get("ph") or first.startswith(last) or last.startswith(first) or bare_mind
                        or len(subj) > 1):
                    sh += ","
            t.append(sh)
        if dats:
            t.append(nps_hi(dats, "dat", dyad))
        texts.append(" ".join(t))
    if texts:
        parts.append(", ".join(texts))
    subj = last_subj
    if subj:
        state["g"] = nps_gender(subj)
        if not verb:
            state["subs"].append(state["g"])
    if verb:
        g = state.get("g")
        if not subj and len(state["subs"]) > 1:
            g = ("m" if any(x[0] == "m" for x in state["subs"]) else "f") + "p"
        if g is None:
            return None
        state["subs"] = []
        neg, k = verb
        parts.append(R.NINS(k, g) if neg else R.INS(k, g))
    return " ".join(parts)


COUNT_WORDS = set(R.P_ABL) | set(R.P_NABL) | set(R.P_LOC) | set(R.P_NLOC) | set(R.NUM)


def tr_count_piece(p):
    """A piece made only of condition words and numbers (counts, chains)."""
    toks = p.split(" ")
    if not toks or not all(t in COUNT_WORDS for t in toks):
        return None
    out = []
    for i, t in enumerate(toks):
        for d in (R.P_ABL, R.P_NABL, R.P_LOC, R.P_NLOC, R.NUM):
            if t in d:
                h = d[t]
                break
        if i and toks[i - 1] in ABL_ALL:
            out.append(", " + h)
        elif i:
            out.append(" " + h)
        else:
            out.append(h)
    return "".join(out)


def tr_label(p, dyad, state):
    """'sahajātaṃ cakkhāyatanaṃ …' without a dash: label + comma + rest."""
    for lab, h in LABEL9.items():
        if p.startswith(lab + " "):
            r = tr_piece(p[len(lab) + 1:], dyad, state)
            if r is not None:
                return f"{h}, {r}"
    return None


CETO_RE = re.compile(r"^cetopariyañāṇena (\S+) cittaṃ (jānāti|jānanti)$")
SAMANGI = {"acittasamaṅgissa": "{%s:mo} मन से युक्त व्यक्ति", "asamaṅgissa": "{%s:f} परिघटनाओं से युक्त व्यक्ति"}


def tr_ceto(p):
    m = CETO_RE.match(p)
    if not m:
        return None
    w, verb = m.groups()
    t = re.fullmatch(r"‹([PN]):(acittasamaṅgissa|asamaṅgissa)›", w)
    if t:
        who = SAMANGI[t.group(2)] % t.group(1)
    elif w == "nocittasamaṅgissa":
        who = SAMANGI["asamaṅgissa"] % "N"
    else:
        return None
    return f"{R.CETOPARIYA} {who} के मन को " + ("जानता है" if verb == "jānāti" else "जानते हैं")


def tr_piece(p, dyad, state):
    if not p.strip():
        return p
    # notes inside a piece: translate the parts around them
    notes = [m for m in re.finditer(r"⟦(\d+)⟧", p) if STORE[int(m.group(1))][0] == "NOTE"]
    if notes and not re.fullmatch(r"⟦\d+⟧", p):
        out, pos = [], 0
        for m in notes:
            before = p[pos:m.start()].strip()
            if before:
                h = tr_piece(before, dyad, state)
                if h is None:
                    return None
                out.append(h)
            out.append(STORE[int(m.group(1))][1])
            pos = m.end()
        after = p[pos:].strip()
        if after:
            h = tr_piece(after, dyad, state)
            if h is None:
                return None
            out.append(h)
        return " ".join(out)
    if p in PIECE9:
        return PIECE9[p]
    r = tr_ceto(p)
    if r is not None:
        return r
    if p in LABEL9:
        return LABEL9[p]
    if p in R.CLAUSE:
        return R.CLAUSE[p]
    m = re.fullmatch(r"⟦(\d+)⟧", p)
    if m:
        st = STORE[int(m.group(1))]
        if st[0] == "NP":
            if st[3] == "nom":
                state["g"] = st[2]
            return st[1] + (" के लिए" if st[3] == "dat" else "")
        return st[1]
    r = tr_count_piece(p)
    if r is not None:
        return r
    m = FRAME_RE.match(p)
    if m:
        r = tr_frame(m)
        if r is not None:
            return r
    if state["panha"] or "paccayena paccayo" in p or re.search(r"⟦\d+⟧ ⟦\d+⟧", p):
        r = tr_panha(p, dyad, state)
        if r is not None:
            return r
    r = tr_body(p, dyad)
    if r is not None:
        return r
    r = tr_panha(p, dyad, state)
    if r is not None:
        return r
    r = tr_label(p, dyad, state)
    if r is not None:
        return r
    for lab, h in LABEL9.items():  # header without a verb, followed by a label (as written)
        if p.endswith(" " + lab):
            r = tr_piece(p[: -len(lab) - 1], dyad, state)
            if r is not None:
                return f"{r} {h}"
    return None


LAST_G = [None]
# source slips: only pure spelling slips are rendered as the word meant (listed in notes-3-09.md)
SLIPS9 = {
    "uppajanti": "uppajjanti",
    " eka khandhañca": " ekaṃ khandhañca",
    "citañca": "cittañca",
    "kaṭattā rūpānaṃ": "kaṭattārūpānaṃ",
    "No upādā dhammo": "Noupādā dhammo",
    "na aññamaññe": "naaññamaññe",
    "na aññamaññapaccayā": "naaññamaññapaccayā",
}
SEP_RE = re.compile(r"( – |; |, |\. |…pe…\.$|…pe…|…\.$|…|\.$| (?=\(\d+\))|(?<=\)) )")


def tr_line(line, dyad, lineno):
    STORE.clear()
    if line.startswith("#"):
        return tr_heading(line)
    for a, b in SLIPS9.items():
        line = line.replace(a, b)
    text = R.lower_initials(line)
    # notes and counts in parentheses
    text = re.sub(r"\(([^()]*[^\d()][^()]*)\)", lambda m: keep(("NOTE", "(" + note_hi(m.group(1), lineno) + ")")), text)
    text = tokenize_items(text, dyad)
    text = dhamma_prepass(text)
    # multi-piece phrases
    for k in sorted(PHRASES, key=len, reverse=True):
        if k in text:
            v = PHRASES[k]
            text = text.replace(k, keep(v if isinstance(v, tuple) else ("PH", v)))
    state = {"g": LAST_G[0], "subs": [], "panha": "paccayena paccayo" in line or "dhammassa" in line}
    out = []
    for tok in SEP_RE.split(text):
        if tok is None or tok == "":
            continue
        if tok in (" – ", "; ", ", ", "…"):
            out.append(tok)
            if tok != ", " and tok != "…":
                state["subs"] = []
        elif tok == ". ":
            out.append("। ")
            state["subs"] = []
        elif tok in (".", "…pe…"):
            out.append({".": "।", "…pe…": "…"}[tok])
        elif tok == "…pe….":
            out.append("…।")
        elif tok == "….":
            out.append("…।")
        elif tok == " ":
            out.append(" ")
        elif re.fullmatch(r"\(\d+\)", tok.strip()):
            out.append(tok)
        else:
            lead = tok[: len(tok) - len(tok.lstrip())]
            trail = tok[len(tok.rstrip()):]
            core = tok.strip()
            h = tr_piece(core, dyad, state)
            if h is None:
                UNK.append((lineno, core))
                h = f"⟪{core}⟫"
            out.append(lead + h + trail)
    LAST_G[0] = state["g"]
    s = "".join(out)
    for _ in range(3):
        s = re.sub(r"⟦(\d+)⟧", lambda m: piece_store(int(m.group(1))), s)
    s = fill(s, dyad) if dyad else s
    return s


def piece_store(i):
    st = STORE[i]
    if st[0] == "NP":
        return st[1] + (" के लिए" if st[3] == "dat" else "")
    return st[1]


def note_hi(n, lineno):
    key = n.strip()
    if key in NOTE9:
        return NOTE9[key]
    if key in R.NOTE:
        return R.NOTE[key]
    UNK.append((lineno, "NOTE: " + key))
    return "⟪" + key + "⟫"


def tr_heading(line):
    m = re.fullmatch(r"(#+) (\*?)(.*?)(\*?)", line)
    hashes, st, body, en = m.groups()
    if body in HEAD9:
        return f"{hashes} {st}{HEAD9[body]}{en}"
    if body in R.HEAD:
        return f"{hashes} {st}{R.HEAD[body]}{en}"
    UNK.append((0, "HEAD: " + body))
    return f"{hashes} {st}⟪{body}⟫{en}"


from tables_3_09 import PHRASES  # noqa: E402

ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")


def build():
    lines = open(SRC, encoding="utf-8").read().split("\n")
    out = []
    dyad = None
    for no, ln in enumerate(lines, 1):
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        if body.startswith("#"):
            hb = re.fullmatch(r"#+ \*?(.*?)\*?", body).group(1)
            if hb in DYAD_BY_HEAD:
                dyad = DYAD_BY_HEAD[hb]
        if body in CLOSING9:
            hi = CLOSING9[body]
        else:
            hi = tr_line(body, dyad, no)
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    return out


if __name__ == "__main__":
    res = build()
    if "--unk" in sys.argv:
        seen = {}
        for no, p in UNK:
            seen.setdefault(p, no)
        for p, no in sorted(seen.items(), key=lambda x: x[1]):
            print(f"{no}\t{p}")
        print(len(seen), "unknown pieces", file=sys.stderr)
    else:
        with open(DST, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(res) + "\n")
        print("written", DST, "unknown:", len(UNK))
