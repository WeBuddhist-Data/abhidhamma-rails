r"""pi-6 Yamaka, Anusayayamaka 7-06 .. 7-11: Hindi plain zero-shot builder.

usage: python -I -X utf8 build_7b_hi.py [7-06-anusayayamaka.md ...]
Without arguments it builds all six files. Unknown lines are reported (prefixed "@@").

The base frames (anusaya names, lists, persons, places, correlatives, question frames,
pajahati forms, tadekaṭṭhaṃ, short answers, headings, closing lines) are imported from
build_7a_hi.py (owner of notes-7a.md) so that they stay byte-identical with 7-01 .. 7-05.
Frames only these files need are defined here and listed in notes-7b.md.
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402  (import only)
import build_7a_hi as A      # noqa: E402  (import only)

PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR
FILES = ["7-%02d-anusayayamaka.md" % i for i in range(6, 12)]
PE = A.PE

# ================================================================ verbs
# kind, plural?, negative?
VERBS = dict(A.VERBS)
VERBS.update({
    "parijānāti": ("pari", False, False), "na_parijānāti": ("pari", False, True),
    "parijānanti": ("pari", True, False), "na_parijānanti": ("pari", True, True),
    "pahīno": ("pah", False, False), "pahīnā": ("pah", True, False),
    "appahīno": ("pah", False, True), "appahīnā": ("pah", True, True),
    "uppajjati": ("upp", False, False), "nuppajjati": ("upp", False, True),
})
QUOT = dict(A.QUOT)
QUOT.update({
    "parijānātīti": "parijānāti", "na_parijānātīti": "na_parijānāti",
    "pahīnoti": "pahīno", "pahīnāti": "pahīnā", "appahīnoti": "appahīno", "appahīnāti": "appahīnā",
    "uppajjatīti": "uppajjati", "nuppajjatīti": "nuppajjati",
})
NOMINATIVE_KINDS = set(A.NOMINATIVE_KINDS) | {"pari"}
PARI = {(False, False): "पूरी तरह समझता है", (False, True): "पूरी तरह नहीं समझता",
        (True, False): "पूरी तरह समझते हैं", (True, True): "पूरी तरह नहीं समझते"}
PAHINA = {(False, False): "छोड़ी जा चुकी है", (False, True): "छोड़ी नहीं गई है",
          (True, False): "छोड़ी जा चुकी हैं", (True, True): "छोड़ी नहीं गई हैं"}
UPP = {False: S.VERBS_F["uppajjati"][0], True: S.VERBS_F["uppajjati"][1]}   # उत्पन्न होती है / नहीं होती


def pred_h(kind, pl, neg, lst, both=False, tad=False):
    bhi = " भी" if both else ""
    if kind in ("anu", "sa", "nir", "paj"):
        return A.pred_h(kind, pl, neg, lst, both=both, tad=tad)
    if kind == "pari":                        # like pajahati: X को [भी] [tadekaṭṭhaṃ] V
        mid = f" {A.TADEKATTHA}" if tad else ""
        return f"{lst} को{bhi}{mid} {PARI[(pl, neg)]}"
    if kind == "pah":                         # like anuseti: X [भी] V
        return f"{lst}{bhi} {PAHINA[(pl, neg)]}"
    if kind == "upp":
        if pl:
            raise KeyError("plural uppajjati")
        return f"{lst}{bhi} {UPP[neg]}"
    raise KeyError(kind)


# ================================================================ predicates (7a algorithm + comma joins)
COMMA = "<,>"


def tokens(s):
    s = s.replace("…pe…", " PE ").replace("na parijān", "na_parijān")
    out = []
    for t in s.split():
        if t.endswith(",") and t != ",":
            out += [t[:-1], COMMA]
        else:
            out.append(t)
    return out


def parse_preds(toks):
    """tokens -> list of predicates (dict: items, kind, pl, neg, tad, comma=comma before it)."""
    preds, items, tad, comma = [], [], False, False
    for t in toks:
        m = A.ANUSAYA_RE.fullmatch(t[0].lower() + t[1:])
        if m:
            items.append([A.ANUSAYA[m.group(1)], m.group(2) == "añca"])
        elif t == "ca":
            if not items:
                raise ValueError("ca without item")
            items[-1][1] = True
        elif t == "PE":
            items.append(PE)
        elif t == "tadekaṭṭhaṃ":
            tad = True
        elif t == COMMA:
            if items or tad or not preds:
                raise ValueError("comma inside a predicate")
            comma = True
        else:
            t = QUOT.get(t, t)
            if t not in VERBS:
                raise KeyError(t)
            kind, pl, neg = VERBS[t]
            preds.append(dict(items=items, kind=kind, pl=pl, neg=neg, tad=tad, comma=comma))
            items, tad, comma = [], False, False
    if items or tad:
        raise ValueError("dangling items")
    return preds


def render_preds(preds, flip=False):
    both = len(preds) > 1 and all(A.all_ca(p) for p in preds)
    out = ""
    for k, p in enumerate(preds):
        neg = (not p["neg"]) if flip else p["neg"]
        h = pred_h(p["kind"], p["pl"], neg, A.join_list(A.names(p)), both=both, tad=p["tad"])
        if k:
            out += ("," if p["comma"] else "") + " और "
        out += h
    return out


# ================================================================ persons and places
PERSONS = dict(A.PERSONS)
PERSONS.update({
    "anāgāmimaggasamaṅgī": "फिर न लौटने के मार्ग से युक्त व्यक्ति",     # notes-7a, suggested for 7-06+
})
# "<X> ṭhapetvā avasesā puggalā" (terms file: C ṭhapetvā avasesā X = C को छोड़कर शेष X)
EXCEPT_OBJ = {
    "Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca": "दो मार्गों से युक्त व्यक्तियों और आठवें स्तर के व्यक्ति",
    "Dvinnaṃ maggasamaṅgīnaṃ": "दो मार्गों से युक्त व्यक्तियों",
    "Aggamaggasamaṅgiñca aṭṭhamakañca": "सर्वोच्च मार्ग से युक्त व्यक्ति और आठवें स्तर के व्यक्ति",
    "Anāgāmimaggasamaṅgiñca aṭṭhamakañca": "फिर न लौटने के मार्ग से युक्त व्यक्ति और आठवें स्तर के व्यक्ति",
    "Aggamaggasamaṅgiṃ": "सर्वोच्च मार्ग से युक्त व्यक्ति",
    "Anāgāmimaggasamaṅgiṃ": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
}
EXCEPT_FRAME = "{X} को छोड़कर शेष व्यक्ति"
EXCEPT_RE = re.compile(r"(" + "|".join(sorted(map(re.escape, EXCEPT_OBJ), key=len, reverse=True))
                       + r") ṭhapetvā avasesā puggalā ")
NOCA_COR = dict(A.NOCA_COR)
NOCA_COR["so"] = "वह"            # "no ca so Y V" (nominative person, no place)


def tr_clause(s):
    who = None
    m = EXCEPT_RE.match(s)
    if m:
        who, s = EXCEPT_FRAME.format(X=EXCEPT_OBJ[m.group(1)]), s[m.end():]
    toks = [t for t in tokens(s)]
    i = 0
    if who is None:
        who, i = A.take_phrase(toks, i, PERSONS)
    places = []
    while True:
        if i < len(toks) and toks[i] == COMMA and places:
            i += 1
        p, j = A.take_phrase(toks, i, A.PLACES)
        if p is None:
            break
        places.append(p)
        i = j
    sab = False
    if i < len(toks) and toks[i] == "sabbattha":
        sab, i = True, i + 1
    while i < len(toks) and (toks[i] in A.COR_FIRST or toks[i] in A.COR_LOC):
        i += 1
    preds = parse_preds(toks[i:])
    parts = []
    if who:
        parts.append(who)
    if places:
        parts.append(A.join_list(places) + " " + A.IN)
    if sab:
        parts.append(A.SABBATTHA)
    if not who and (places or sab) and preds[0]["kind"] in NOMINATIVE_KINDS:
        parts.append(A.KOI)
    parts.append(render_preds(preds))
    return " ".join(parts)


def tr_noca(s):
    toks = tokens(s)
    i, cor = 0, []
    while i < len(toks) and (toks[i] in A.COR_FIRST or toks[i] in A.COR_LOC):
        cor.append(toks[i])
        i += 1
    c = NOCA_COR[" ".join(cor)]
    preds = parse_preds(toks[i:])
    return "पर " + (c + " " if c else "") + render_preds(preds, flip=True)


# na vattabbo "pahīno"ti vā "appahīno"ti vā
VATT_RE = re.compile(r'(?:(.+) )?[Nn]a vattabb(o|ā) "pahīn[oā]"ti vā "appahīn[oā]"ti vā')
VATTABBA = "{X} न “{A}” कहा जा सकता है, न “{B}”"
VATTABBA_Q = {False: ("छोड़ी जा चुकी", "छोड़ी नहीं गई"), True: ("छोड़ी जा चुकीं", "छोड़ी नहीं गईं")}
VATTABBA_BARE = {False: "उसे", True: "उन्हें"}


def tr_vattabba(m):
    lst, num = m.groups()
    pl = num == "ā"
    if lst:
        preds_items = []
        for t in tokens(lst):
            mm = A.ANUSAYA_RE.fullmatch(t[0].lower() + t[1:])
            if mm:
                preds_items.append(A.ANUSAYA[mm.group(1)])
            elif t != "ca":
                raise ValueError("vattabba list: " + lst)
        X = A.join_list(preds_items) + " को"
    else:
        X = VATTABBA_BARE[pl]
    a, b = VATTABBA_Q[pl]
    return VATTABBA.format(X=X, A=a, B=b)


VITTHARETABBAM = "(विस्तार से कहना चाहिए)"


def tr_answer(s):
    """One answer sentence without its final period."""
    tail = ""
    if s.endswith(" (vitthāretabbaṃ)"):
        s, tail = s[:-len(" (vitthāretabbaṃ)")], " " + VITTHARETABBAM
    if s.endswith(" …pe…"):
        s, tail = s[:-len(" …pe…")], " " + PE + tail
    if s in A.SHORT:
        return A.SHORT[s] + tail + "।"
    if s == "Tadekaṭṭhaṃ parijānāti":
        return A.TADEKATTHA + " " + PARI[(False, False)] + tail + "।"
    if DHATU_START.match(s):
        # 7-10 ^6-7-335: a "kati …" question closed with "." in the source; Hindi keeps "?"
        return tr_dhatu(s) + tail + ("?" if s.endswith("kati anusayā bhaṅgā") else "।")
    outs = []
    for c in s.split("; "):
        m = VATT_RE.fullmatch(c)
        if m:
            outs.append(tr_vattabba(m))
            continue
        parts = re.split(r",? no ca ", c)
        o = tr_clause(parts[0])
        for p in parts[1:]:
            o += ", " + tr_noca(p)
        outs.append(o)
    return "; ".join(outs) + tail + "।"


# ================================================================ questions
VAR_PAHINO_P = " [pahīno (sī. ka.) anusayavārena pana na sameti]"
VAR_PAHINO_H = " [" + S.VAR_SPELL + " (Sī., Ka.): pahīno; पर यह सुप्त प्रवृत्तियों के खंड से मेल नहीं खाता]"


def tr_question(s):
    var = ""
    if VAR_PAHINO_P in s:
        s, var = s.replace(VAR_PAHINO_P, ""), VAR_PAHINO_H
    toks = tokens(s[:-1])
    toks[0] = toks[0].lower()
    rel, i, vp = [toks[0]], 1, False
    if toks[i:i + 2] == ["vā", "pana"]:
        vp, i = True, i + 2
    if toks[i] in ("yattha", "yato"):
        rel.append(toks[i])
        i += 1
    j = i
    while QUOT.get(toks[j], toks[j]) not in VERBS:
        j += 1
    p1 = parse_preds(toks[i:j + 1])
    k = j + 1
    cor = []
    while toks[k] in ("tassa", "tattha", "so", "tato"):
        cor.append(toks[k])
        k += 1
    p2 = parse_preds(toks[k:])
    P1 = render_preds(p1)
    if var:
        P1 += var
    return A.Q.format(AND=S.VA_PANA if vp else "", REL=A.Q_REL[" ".join(rel)], P1=P1,
                      COR=A.Q_COR[" ".join(cor)], P2=render_preds(p2))


# ================================================================ dhātu section (7-10, 7-11)
REALM = {"kāmadhātu": "इंद्रिय-सुखों के लोक", "rūpadhātu": "सूक्ष्म भौतिक लोक", "arūpadhātu": "अभौतिक लोक"}
REALM_NOT = "{R} से भिन्न लोक"                 # na X (na Y)
CUTASSA = "{R} में मरकर"                        # X-dhātuyā cutassa
UPAPAJJANTASSA = "{R} में जन्म लेने वाले"        # X-dhātuṃ upapajjantassa
KATI_Q = ("कितनी सुप्त प्रवृत्तियाँ सोई रहती हैं, कितनी सुप्त प्रवृत्तियाँ सोई नहीं रहतीं, "
          "कितनी सुप्त प्रवृत्तियाँ भंग हो चुकी हैं")
NUM = {"satta": "सात", "pañca": "पाँच", "tayo": "तीन"}
KASSACI = "किसी में {N} सुप्त प्रवृत्तियाँ सोई रहती हैं"
SATTEVA = "सात ही सुप्त प्रवृत्तियाँ सोई रहती हैं"
BHANGA_NATTHI = "भंग हो चुकी सुप्त प्रवृत्तियाँ नहीं हैं"
UPAPATTI_NATTHI = "{R} में जन्म नाम की कोई चीज़ नहीं है"
HETTHA = "नीचे जन्म लेता हुआ वह इंद्रिय-सुखों के लोक में ही जन्म लेता है"
DHATU_START = re.compile(r"(?:Na )?(?:[Kk]āma|[Rr]ūpa|[Aa]rūpa)dhātuyā .*cutassa ")
DH_RE = re.compile(r"((?:[Nn]a )?\S+dhātuyā(?: na \S+dhātuyā)?) cutassa (.+)")


def realm_phrase(words):
    names = [w for w in words if w != "na"]
    base = [REALM[re.sub(r"(yā|ṃ)$", "", n)] for n in names]
    if "na" in words:
        return REALM_NOT.format(R=A.join_list(base))
    if len(base) != 1:
        raise ValueError(words)
    return base[0]


def tr_dhatu(s):
    m = DH_RE.fullmatch(s)
    if not m:
        raise ValueError("dhatu: " + s)
    frm, rest = m.groups()
    R1 = CUTASSA.format(R=realm_phrase((frm[0].lower() + frm[1:]).split()))
    m2 = re.match(r"((?:na )?\S+dhātuṃ(?: na \S+dhātuṃ)?) upapajjantassa (.+)", rest)
    if m2:
        to, rest = m2.groups()
        who = R1 + " " + UPAPAJJANTASSA.format(R=realm_phrase(to.split()))
        if rest == "kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā":
            return f"{who} में {KATI_Q}"
        parts = rest.split("; ")
        if len(parts) != 2 or parts[1] != "anusayā bhaṅgā natthi":
            raise ValueError("dhatu answer: " + rest)
        if parts[0] == "satteva anusayā anusenti":
            body = f"{who} में {SATTEVA}"
        elif re.fullmatch(r"kassaci \S+ anusayā anusenti(?:, kassaci \S+ anusayā anusenti)*", parts[0]):
            ns = re.findall(r"kassaci (\S+) anusayā", parts[0])
            body = f"{who} " + ", ".join(KASSACI.format(N=NUM[n]) for n in ns)
        else:
            raise ValueError("dhatu answer: " + rest)
        return body + "; " + BHANGA_NATTHI
    m3 = re.fullmatch(r"((?:na )?\S+dhātuyā(?: na \S+dhātuyā)?) upapatti ?nāma natthi, heṭṭhā upapajjamāno "
                      r"kāmadhātuṃyeva upapajjati, satteva anusayā anusenti; anusayā bhaṅgā natthi", rest)
    if m3:
        R2 = realm_phrase(m3.group(1).split())
        return f"{R1} {UPAPATTI_NATTHI.format(R=R2)}, {HETTHA}, {SATTEVA}; {BHANGA_NATTHI}"
    raise ValueError("dhatu rest: " + rest)


# ================================================================ headings, closing lines, labels
HEADINGS = dict(A.HEADINGS)
HEADINGS.update({
    "Pariññāvāro": "पूरी तरह समझने का खंड",          # terms file
    "Pariññāvāra": "पूरी तरह समझने का खंड",
    "Pahīnavāro": "छोड़ा जा चुका होने का खंड",        # terms file
    "Pahīnavāra": "छोड़ा जा चुका होने का खंड",
    "Uppajjanavāro": "उत्पन्न होने का खंड",
    "(Ka) dhātupucchāvāro": "(क) लोकों के बारे में प्रश्नों का खंड",
    "(Kha) dhātuvisajjanāvāro": "(ख) लोकों के बारे में उत्तरों का खंड",
})
VARA = dict(A.VARA)
VARA.update({
    "Pariññā": ("पूरी तरह समझने का खंड", "पूरी तरह समझने के खंड"),
    "Pahīna": ("छोड़ा जा चुका होने का खंड", "छोड़ा जा चुका होने के खंड"),
    "Uppajjana": ("उत्पन्न होने का खंड", "उत्पन्न होने के खंड"),
    "Dhātupucchā": ("लोकों के बारे में प्रश्नों का खंड", "लोकों के बारे में प्रश्नों के खंड"),
    "Dhātuvisajja": ("लोकों के बारे में उत्तरों का खंड", "लोकों के बारे में उत्तरों के खंड"),
})
FIXED = dict(A.FIXED)
for _p, (_nom, _obl) in VARA.items():
    FIXED[_p + "vāro."] = _nom + "।"
    for _pp, _ph in A.PART.items():
        FIXED[_p + "vāre " + _pp + "."] = _obl + " का " + _ph + " भाग।"
FIXED.update({
    "Anusayayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Anusayayamakaṃ"]),
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,
    "9": "9",     # 7-10 ^6-7-311: a bare number line in the source
    "(Vitthāretabbaṃ).": "(विस्तार से कहना चाहिए)।",
})
MULAKA = {f"({k})": A.MULAKA_H.format(N=v) for k, v in A.MULAKA.items()}
MULAKA.update({
    "(Kāmadhātumūlakaṃ)": "(इंद्रिय-सुखों के लोक पर आधारित)",
    "(Rūpadhātumūlakaṃ)": "(सूक्ष्म भौतिक लोक पर आधारित)",
    "(Arūpadhātumūlakaṃ)": "(अभौतिक लोक पर आधारित)",
    "(Nakāmadhātumūlakaṃ)": "(इंद्रिय-सुखों के लोक से भिन्न लोक पर आधारित)",
    "(Narūpadhātumūlakaṃ)": "(सूक्ष्म भौतिक लोक से भिन्न लोक पर आधारित)",
    "(Naarūpadhātumūlakaṃ)": "(अभौतिक लोक से भिन्न लोक पर आधारित)",
    "(Nakāmanaarūpadhātumūlakaṃ)": "(इंद्रिय-सुखों के लोक और अभौतिक लोक से भिन्न लोक पर आधारित)",
    "(Narūpanaarūpadhātumūlakaṃ)": "(सूक्ष्म भौतिक लोक और अभौतिक लोक से भिन्न लोक पर आधारित)",
    "(Nakāmanarūpadhātumūlakaṃ)": "(इंद्रिय-सुखों के लोक और सूक्ष्म भौतिक लोक से भिन्न लोक पर आधारित)",
})


# ================================================================ lines
def split_sentences(text):
    """split after '. ' / '? ' outside square brackets"""
    parts, buf, depth = [], "", 0
    for i, ch in enumerate(text):
        buf += ch
        depth += (ch == "[") - (ch == "]")
        if depth == 0 and ch in ".?" and text[i + 1:i + 2] == " ":
            parts.append(buf.strip())
            buf = ""
    if buf.strip():
        parts.append(buf.strip())
    return parts


def tr_sentence(s):
    if s in FIXED:
        return FIXED[s]
    if s in MULAKA:
        return MULAKA[s]
    lab = ""
    m = re.match(r"^\((Ka|Kha)\) ", s)
    if m:
        lab, s = S.LABELS["(" + m.group(1) + ")"] + " ", s[m.end():]
    if s.endswith("?"):
        if DHATU_START.match(s):
            return lab + tr_dhatu(s[:-1]) + "?"
        return lab + tr_question(s)
    if s.endswith("."):
        return lab + tr_answer(s[:-1])
    raise ValueError("sentence without end: " + s)


def tr_body(text):
    if text in FIXED:
        return FIXED[text]
    return " ".join(tr_sentence(x) for x in split_sentences(text))


def tr_line(line):
    if not line.strip():
        return ""
    m = S.ID_RE.search(line)
    bid = m.group(1) if m else None
    text = (S.ID_RE.sub("", line) if m else line).rstrip()
    if text.startswith("#"):
        level = len(text) - len(text.lstrip("#"))
        out = "#" * level + " " + HEADINGS[text[level:].strip()]
    else:
        out = tr_body(text)
    return out + (" " + bid if bid else "")


def build(fname):
    src = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
    out, errs = [], []
    for n, line in enumerate(src, 1):
        try:
            out.append(tr_line(line))
        except Exception as e:  # report and continue
            errs.append(f"{fname}:{n}: {type(e).__name__}: {e}")
            out.append("@@ " + line)
    (HI_DIR / fname).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    return errs


def main():
    files = sys.argv[1:] or FILES
    total = 0
    for f in files:
        errs = build(f)
        total += len(errs)
        for e in errs[:40]:
            print(e)
        print(f, "errors:", len(errs))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
