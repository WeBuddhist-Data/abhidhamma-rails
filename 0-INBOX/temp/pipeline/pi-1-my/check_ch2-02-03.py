"""Per-line check of the pi-1 Burmese chapters 2-02 and 2-03 against their Pāli (adapted from check_ch2-01.py).

usage: python3 -I -X utf8 check_ch2-02-03.py <pali_file> <burmese_file> [...pairs]
The tables come from my_formulas.py plus the in-memory additions of make_ch2-02-03.py (extend(); the generator is
imported, it writes nothing). For every non-empty line (same order) it compares, independently of translate_cu():
  1. block ids  - same id at the end of the same line;
  2. negations  - weighted Pāli negation morphemes (free na / no / neva; privative a- / an- of PRIV; double / triple
                  forms; the arūpa bases ākāsānañca- / viññāṇañca- / ākiñcañña- = 1, nevasaññānāsañña- = 3) against
                  Burmese negation syllables («မ» + an unclosed letter, «အကုသိုလ်», the abyākata phrase); NOT_NEG
                  («ကာမ», «မနော», «ဗြဟ္မ») are not negations;
  3. numbers    - Pāli number words (incl. tivaṅgika, navindriya, catūhi, soḷasakkhattuka, vīsati, tebhūmaka …)
                  against Burmese number + classifier and «တစ်ဆယ့်ခြောက်» (16), «နှစ်ဆယ်» (20);
  4. variants   - every «[text (sigla)]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla): text]», label as VAR_KIND;
  5. frames     - counts per line: questions, closers, «ye vā pana», «ṭhapetvā», «ime dhammā kusalā», «Katame dhammā
                  kusalā», «Tasmiṃ kho pana samaye», «Yasmiṃ samaye» (= «… ဖြစ်ပေါ်လာသော / ဝင်စား၍ နေသော အချိန်၌»),
                  «hoti / honti» = Burmese verb forms, «.» + «?» = «။»;
  6. openings   - every phrase of the «Yasmiṃ samaye …» clause is found in the opening tables (no Pāli word left
                  over) and its Burmese value occurs in the Burmese line as often as in the Pāli;
  7. terms      - outside the opening, factor names, synonyms, list heads and sentence definitions in Pāli order;
                  headings and colophon lines must equal the table value;
  8. lists      - within one synonym list two different Pāli items never share one Burmese value;
  9. typography - no «?», «।», «:-», no Latin outside brackets, NFC, Myanmar code points U+1000-U+104F only, a line
                  ending in «.» / «?» ends in «။».
Prints OK or the mismatching lines; exit 1 on any mismatch.
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my_formulas as F  # noqa: E402

_spec = importlib.util.spec_from_file_location("make_ch2_02_03", HERE / "make_ch2-02-03.py")
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)
G.extend()

W = "[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]"
WB = r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])"
WE = r"(?![A-Za-zāīūṃṅñṭḍṇḷ])"
# ------------------------------------------------------------------ negations (Pāli)
NEG_PI = [
    (r"nevavipākanavipāk\w*", 2), (r"nevācayagāmināpacay\w*", 2), (r"nevasekkhanāsekkh\w*", 2),
    (r"adukkhamasukh\w*", 2), (r"anupādiṇṇaanupādāniy\w*", 2), (r"asaṃkiliṭṭhaasaṃkilesik\w*", 2),
    (r"avitakkaavicār\w*", 2), (r"anidassanaappaṭigh\w*", 2), (r"nāsāt\w*", 2),
    # 2-02 / 2-03
    (r"nevasaññānāsaññ\w*", 3), (r"rūparāgaarūparāgamānauddhaccaavijj\w*", 2), (r"velāanatikkam\w*", 1),
    (r"ākāsānañc\w*", 1), (r"viññāṇañc\w*", 1), (r"ākiñcaññ\w*", 1),
    (r"(?:na|no|neva|Na|No|Neva)" + WE, 1),
]
PRIV = ("akusal abyākat anupādiṇṇ asaṃkiliṭṭh asaṃkilesik avitakk avicār appamāṇ aniyat anuppann anidassan "
        "appaṭigh ahetuk appaccay asaṅkhat arūp anāsav asaṃyojaniy aganthaniy anoghaniy ayoganiy anīvaraṇiy "
        "aparāmaṭṭh anārammaṇ acetasik cittavisaṃsaṭṭh anupādāniy appītik apariyāpann aniyyānik anuttar "
        "araṇ avijj atapanīy ahirik anottapp dovacass aguttadvār amattaññ asampajañ asantuṭṭh appaṭivān "
        "anuppād anantavā aṭṭhān avikkhep "
        "alobh ados amoh anabhijjh abyāpād abyāpajj alubbh asārāg asārajj adussan adussit adūs asithil anikkhitt "
        "apilāpan asammussan avisāh adandhan avitthan akakkhaḷ akathin ajimh avaṅk akuṭil "
        # 2-02 / 2-03
        "amanasikār anaññāt adiṭṭh appatt avidit asacchikat anavases appaṇihit asubh akiriy akaraṇ "
        "anajjhāpatt").split()
NEG_PI += [(p + r"\w*", 1) for p in PRIV]
NEG_PI_RE = [(re.compile(WB + p, re.I), w) for p, w in NEG_PI]
# ------------------------------------------------------------------ negations (Burmese)
LETTER = "က-ဪ"
CLOSE = "္်"
NOT_NEG = ["ကာမ", "မနော", "ဗြဟ္မ"]   # kāma, mano, brahma-: a «မ» that is not a negation
NEG_MY = [
    ("|".join(NOT_NEG), 0),
    (re.escape(F.TERMS["abyākatā"].removesuffix("သော")), 1),
    (r"အကုသိုလ်", 1),
    (r"မ(?=[" + LETTER + r"](?!့?[" + CLOSE + r"]))", 1),
]
NEG_MY_RE = [(re.compile(p), w) for p, w in NEG_MY]


def neg_count(s, table):
    n = 0
    for rx, w in table:
        n += len(rx.findall(s)) * w
        s = rx.sub(" ", s)
    return n


# ------------------------------------------------------------------ numbers
NUM_PI = [(r"soḷasakkhattuk\w*", 16), (r"aṭṭhakkhattuk\w*", 8), (r"aṭṭhakasiṇ\w*", 8), (r"catasso", 4),
          (r"vīsati", 20), (r"navindriy\w*", 9), (r"aṭṭhaṅgik\w*", 8), (r"tivaṅgik\w*", 3), (r"duvaṅgik\w*", 2),
          (r"catūhi", 4), (r"tīhi", 3), (r"tebhūmak\w*", 3), (r"catukka\w*", 4), (r"pañcaka\w*", 5),
          (r"tika\w*", 3), (r"\w*duka\w*", 2), (r"eko|ekā|ekaṃ", 1), (r"dve|dvi\w*|dvā\w*", 2), (r"tayo|tīṇi", 3),
          (r"cattāro|cattāri|caturaṅgik\w*", 4), (r"pañca|pañcaṅgik\w*", 5), (r"cha", 6),
          (r"satta|sattindriy\w*", 7), (r"aṭṭha|aṭṭhindriy\w*", 8)]
NUM_PI_RE = [(re.compile(p, re.I), v) for p, v in NUM_PI]
NUM_MY = {"တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6, "ခုနစ်": 7, "ရှစ်": 8, "ကိုး": 9}
NUM_COMPOUND = {"တစ်ဆယ့်ခြောက်": 16, "နှစ်ဆယ်": 20}
CLASSIFIER = "မျိုး|ပါး|ခု|ချက်|ယောက်|ကြိမ်"
NUM_MY_RE = re.compile("(" + "|".join(NUM_MY) + ")(?=" + CLASSIFIER + ")")
NUM_IDIOM = ["တစ်စုံတစ်ခု", "သူတစ်ပါး"]


def nums_pi(s):
    out = []
    for w in re.findall(W + "+", s):
        for rx, v in NUM_PI_RE:
            if rx.fullmatch(w):
                out.append(v)
                break
    return sorted(out + [int(d) for d in re.findall(r"\((\d+)\)", s)])


def nums_my(s):
    for i in NUM_IDIOM:
        s = s.replace(i, " ")
    out = []
    for k, v in NUM_COMPOUND.items():
        out += [v] * s.count(k)
        s = s.replace(k, " ")
    return sorted(out + [NUM_MY[m] for m in NUM_MY_RE.findall(s)] + [int(d) for d in re.findall(r"\((\d+)\)", s)])


# ------------------------------------------------------------------ variants
VAR_PI = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)\]")
VAR_MY = re.compile(r"\[(?P<k>" + F.PATHA + "|" + F.LEKHANA + r") \((?P<s>[^()]+)\): (?P<t>[^\]]+)\]")


def var_check(x, y):
    a, b = VAR_PI.findall(x), VAR_MY.findall(y)
    if x.count("[") != y.count("[") or len(a) != len(b):
        return ["variant count"]
    errs = []
    for (t, s), (k, s2, t2) in zip(a, b):
        if t != t2:
            errs.append(f"variant text {t2}")
        if F.VAR_KIND.get(t) != k:
            errs.append(f"variant label {k} for {t}")
        if s2 != ", ".join(z[0].upper() + z[1:] for z in s.split()):
            errs.append(f"sigla {s2}")
    return errs


# ------------------------------------------------------------------ frames (counts)
OPEN_END = r"(?:" + re.escape(F.UPPANNA) + "|" + re.escape(G.UPAS) + r") " + re.escape(F.YASMIM)
VERB = r"(?:ရှိသည်|ရှိကြသည်|ဖြစ်သည်|ဖြစ်ကြသည်)(?![" + LETTER + r"])|အဘယ်နည်း|အဘယ်တို့နည်း|" + \
       re.escape(F.UPPANNA + " " + F.YASMIM)


def frames(x, y):
    errs = []
    pairs = [
        (r"Katam(?:o|ā|aṃ|e|āni) tasmiṃ samaye", r"ဟူသည် အဘယ်(?:တို့)?နည်း", "question"),
        (r"(?:[Aa]yaṃ|[Ii]daṃ|[Ii]me|[Ii]māni|[Ii]mā) tasmiṃ samaye", r"ဤသည်(?:တို့)?မှာ ထိုအချိန်၌", "closer"),
        (r"[Yy]e vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā", re.escape(F.YEVA), "ye vā pana"),
        (r"ṭhapetvā", re.escape(F.THAPETVA), "ṭhapetvā"),
        (r"ime dhammā kusalā", re.escape(F.IME_KUSALA), "ime dhammā kusalā"),
        (r"Katame dhammā kusalā", re.escape(F.KATAME_KUSALA), "katame kusalā"),
        (r"Tasmiṃ kho pana samaye", re.escape(F.KHO_PANA_SAMAYE), "kho pana"),
        (r"Yasmiṃ samaye", OPEN_END, "yasmiṃ samaye"),
    ]
    for p, m, name in pairs:
        a, b = len(re.findall(p, x)), len(re.findall(m, y))
        if name == "question":
            b -= len(re.findall(re.escape(F.KATAME_KUSALA), y))
        if a != b:
            errs.append(f"{name} {a} vs {b}")
    hoti = len(re.findall(r"\b(?:hoti|honti)\b", x))
    verbs = len(re.findall(VERB, y))
    verbs -= len(re.findall(re.escape(F.IME_KUSALA), y)) + len(re.findall(re.escape(F.KATAME_KUSALA), y))
    if hoti != verbs:
        errs.append(f"hoti {hoti} vs verbs {verbs}")
    ends_x = len(re.findall(r"[.?]", re.sub(r"\[[^\]]*\]", "", x)))
    if ends_x != y.count(F.END):
        errs.append(f"sentence ends {ends_x} vs {y.count(F.END)}")
    return errs


# ------------------------------------------------------------------ openings
OPEN_RE = re.compile(r"Yasmiṃ samaye (?P<body>(?:(?!tasmiṃ samaye).)+?)(?=(?:, | – | )tasmiṃ samaye)")
OPEN_KEYS = {}
for _name, _tab in G.OPEN_TABLES.items():
    if _name in ("PRE_FIXED",):
        continue
    for _k, _v in _tab.items():
        OPEN_KEYS.setdefault(_k, _v)
OPEN_KEYS.update({k: v for k, v in G.PRE_FIXED.items()})
OPEN_KEYS_SORTED = sorted(OPEN_KEYS, key=len, reverse=True)
LEFT_RE = re.compile(r"\[[^\]]*\]|…pe…|[,–]|\s+")


def openings(x, y):
    """Check the phrases of every «Yasmiṃ samaye …» clause; return (errors, x without the clause, y offset)."""
    errs, rest, yoff = [], x, 0
    for m in OPEN_RE.finditer(x):
        body = m["body"]
        need = []
        pm = G.PRE_RE.search(body)
        if pm:
            need += [G.ARUPASANNI, G.RUPANI_PASSATI, G.TANI_ABHIBHUYYA]
            body = body[:pm.start()] + " " + pm["adj"] + " " + body[pm.end():]
        for k in OPEN_KEYS_SORTED:
            rx = re.compile(WB + re.escape(k) + WE)
            n = len(rx.findall(body))
            if n:
                need += [OPEN_KEYS[k]] * n
                body = rx.sub(" ", body)
        left = LEFT_RE.sub("", body)
        if left:
            errs.append(f"opening words not in the tables: {body.split()[:6]}")
        for v in set(need):
            if y.count(v) < need.count(v):
                errs.append(f"opening missing «{v}»")
        rest = x[m.end():]          # the text before the clause is «Katame dhammā kusalā?» (frame-checked)
        e = re.search(OPEN_END, y)
        if e:
            yoff = max(yoff, e.end())
    return errs, rest, yoff


# ------------------------------------------------------------------ terms (own scanner)
ORDERED = {}
for d in (F.SYN, F.NAMES, F.GEN):
    for k, v in d.items():
        ORDERED.setdefault(k, v)
MAXW = max(len(k.split()) for k in ORDERED)
LIST_RE = re.compile(r"(?:Yo|Yā|Yaṃ)(?: tasmiṃ samaye)? (.*?)(?: – |, (?:idaṃ|ayaṃ) tasmiṃ samaye)")


def words(s):
    return re.findall(r"[^\s,;?.\[\]…–]+", re.sub(r"\[[^\]]*\]|…pe…", " ", s))


def scan(s):
    w, i, out = words(s), 0, []
    while i < len(w):
        for k in range(MAXW, 0, -1):
            if len(w[i:i + k]) < k:
                continue
            key = " ".join(w[i:i + k])
            low = key[0].lower() + key[1:]
            if low in ORDERED:
                out.append((low, ORDERED[low]))
                i += k
                break
        else:
            i += 1
    return out


def terms(x, y):
    errs = []
    m = re.fullmatch(r"(#+) (.+)", x)
    if m:
        exp = f"{m[1]} {F.HEAD.get(m[2], '?')}"
        return [] if exp == y else [f"heading: expected «{exp}»"]
    m = re.fullmatch(r"([^\[]+?)\.", x)
    if m and m[1] in G.TITLES:
        exp = G.TITLES[m[1]] + F.END
        return [] if exp == y else [f"colophon: expected «{exp}»"]
    e, x, pos = openings(x, y)
    errs += e
    for k, v in F.BODY.items():
        if k in x:
            if y.count(v) != x.count(k):
                errs.append(f"body missing «{v[:30]}…»")
            x = x.replace(k, " ")
    for p, v in scan(x):
        j = y.find(v, pos)
        if j < 0:
            errs.append(f"order / missing «{v}» ({p})")
            break
        pos = j + len(v)
    for lst in LIST_RE.findall(x):
        seen = {}
        for p, v in scan(lst):
            if v in seen and seen[v] != p:
                errs.append(f"list shares «{v}»: {seen[v]} / {p}")
            seen[v] = p
    return errs


ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)$")


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


def strip_br(s):
    return re.sub(r"\[[^\]]*\]", " ", s)


bad = 0
args = sys.argv[1:]
for src, tgt in zip(args[::2], args[1::2]):
    a, b = lines(src), lines(tgt)
    raw = open(tgt, encoding="utf-8").read()
    probs = []
    if len(a) != len(b):
        probs.append(f"line count {len(a)} vs {len(b)}")
    if unicodedata.normalize("NFC", raw) != raw:
        probs.append("not NFC")
    bad_cp = sorted({hex(ord(c)) for c in raw if "က" <= c <= "႟" and c > "၏"})
    if bad_cp:
        probs.append(f"Myanmar code points outside U+1000-U+104F: {bad_cp[:5]}")
    nterm = 0
    for i, (x, y) in enumerate(zip(a, b), 1):
        mx, my_ = ID_RE.search(x), ID_RE.search(y)
        if (mx and mx[1]) != (my_ and my_[1]):
            probs.append(f"line {i}: block id")
        xb = x[:mx.start()] if mx else x
        yb = y[:my_.start()] if my_ else y
        e = []
        xs, ys = strip_br(xb), strip_br(yb)
        if not xb.startswith("#"):
            np_, nm = neg_count(xs, NEG_PI_RE), neg_count(ys, NEG_MY_RE)
            if np_ != nm:
                e.append(f"negations {np_} vs {nm}")
            e += frames(xb, yb)
        if nums_pi(xs) != nums_my(ys):
            e.append(f"numbers {nums_pi(xs)} vs {nums_my(ys)}")
        e += var_check(xb, yb)
        for ch in ("?", "।", ":-"):
            if ch in yb:
                e.append(f"contains {ch}")
        if re.search(W, re.sub(r"\[[^\]]*\]", "", yb)):
            e.append("Latin outside brackets")
        if not xb.startswith("#") and xb[-1:] in ".?" and not yb.endswith(F.END):
            e.append("no ။ at the end")
        e += terms(xb, yb)
        nterm += 1
        if e:
            probs.append(f"line {i}: " + "; ".join(e[:4]))
    if probs:
        bad += 1
        print(f"{tgt}: {len(probs)} mismatches")
        for p in probs[:40]:
            print("  ", p)
    else:
        print(f"{tgt}: OK ({len(b)} lines, {nterm} lines term-checked, 0 mismatches)")
sys.exit(1 if bad else 0)
