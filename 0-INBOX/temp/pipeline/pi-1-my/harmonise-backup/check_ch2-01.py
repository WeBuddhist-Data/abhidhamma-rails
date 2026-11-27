"""Per-line check of a pi-1 Burmese Cittuppāda chapter against its Pāli (adapted from check_sample.py).

usage: python3 -I -X utf8 check_ch2-01.py <pali_file> <burmese_file> [...pairs]
For every non-empty line (same order) it compares, independently of my_formulas.translate_cu():
  1. block ids  - same id at the end of the same line;
  2. negations  - weighted Pāli negation morphemes (free na / no / neva; privative a- / an- words of PRIV; double forms
                  = 2; «nāsāta» = 2) against Burmese negation syllables («မ» + an unclosed letter, «အကုသိုလ်», the abyākata
                  phrase); words in NOT_NEG («ကာမ», «မနော») are not negations;
  3. numbers    - Pāli number words (eko … aṭṭha, dvāyatanāni, pañcaṅgika …) against Burmese number + classifier;
  4. variants   - every «[text (sigla)]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla): text]», label as VAR_KIND;
  5. frames     - counts per line: questions «Katam… tasmiṃ samaye … hoti» = «ဟူသည် အဘယ်(တို့)နည်း»; closers «ayaṃ / idaṃ
                  / ime … tasmiṃ samaye» = «ဤသည်(တို့)မှာ ထိုအချိန်၌»; «ye vā pana …» = YEVA; «ṭhapetvā» = «ချန်ထား၍»;
                  «ime dhammā kusalā» = IME_KUSALA; «hoti / honti» = Burmese verb forms; «.» + «?» = «။»;
  6. terms      - the Pāli line is scanned (own longest-match scanner) for factor names, synonyms, list heads, sentence
                  definitions and opening words; their Burmese table values must occur in the Burmese line, the names /
                  synonyms / heads in the same order; headings and colophon lines must equal the table value;
  7. lists      - within one synonym list two different Pāli items never share one Burmese value;
  8. typography - no «?», «।», «:-», no Latin outside brackets, NFC, Myanmar code points U+1000-U+104F only, a line
                  ending in «.» / «?» ends in «။».
Prints OK or the mismatching lines; exit 1 on any mismatch.
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my_formulas as F  # noqa: E402  (tables only)

W = "[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]"
WB = r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])"
WE = r"(?![A-Za-zāīūṃṅñṭḍṇḷ])"
# ------------------------------------------------------------------ negations (Pāli)
NEG_PI = [
    (r"nevavipākanavipāk\w*", 2), (r"nevācayagāmināpacay\w*", 2), (r"nevasekkhanāsekkh\w*", 2),
    (r"adukkhamasukh\w*", 2), (r"anupādiṇṇaanupādāniy\w*", 2), (r"asaṃkiliṭṭhaasaṃkilesik\w*", 2),
    (r"avitakkaavicār\w*", 2), (r"anidassanaappaṭigh\w*", 2), (r"nāsāt\w*", 2),
    (r"(?:na|no|neva|Na|No|Neva)" + WE, 1),
]
PRIV = ("akusal abyākat anupādiṇṇ asaṃkiliṭṭh asaṃkilesik avitakk avicār appamāṇ aniyat anuppann anidassan "
        "appaṭigh ahetuk appaccay asaṅkhat arūp anāsav asaṃyojaniy aganthaniy anoghaniy ayoganiy anīvaraṇiy "
        "aparāmaṭṭh anārammaṇ acetasik cittavisaṃsaṭṭh anupādāniy appītik apariyāpann aniyyānik anuttar "
        "araṇ avijj atapanīy ahirik anottapp dovacass aguttadvār amattaññ asampajañ asantuṭṭh appaṭivān "
        "anuppād anantavā aṭṭhān avikkhep "
        # Cittuppāda (2-01)
        "alobh ados amoh anabhijjh abyāpād abyāpajj alubbh asārāg asārajj adussan adussit adūs asithil anikkhitt "
        "apilāpan asammussan avisāh adandhan avitthan akakkhaḷ akathin ajimh avaṅk akuṭil").split()
NEG_PI += [(p + r"\w*", 1) for p in PRIV]
NEG_PI_RE = [(re.compile(WB + p, re.I), w) for p, w in NEG_PI]
# ------------------------------------------------------------------ negations (Burmese)
LETTER = "က-ဪ"
CLOSE = "္်"
NOT_NEG = ["ကာမ", "မနော"]          # «ကာမ-» (kāma), «မနော» (mano): a free «မ» that is not a negation
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
NUM_PI = [(r"tika\w*", 3), (r"\w*duka\w*", 2), (r"eko|ekā|ekaṃ", 1), (r"dve|dvi\w*|dvā\w*", 2), (r"tayo|tīṇi", 3),
          (r"cattāro|cattāri|caturaṅgik\w*", 4), (r"pañca|pañcaṅgik\w*", 5), (r"cha", 6),
          (r"satta|sattindriy\w*", 7), (r"aṭṭha|aṭṭhindriy\w*", 8)]
NUM_PI_RE = [(re.compile(p, re.I), v) for p, v in NUM_PI]
NUM_MY = {"တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6, "ခုနစ်": 7, "ရှစ်": 8}
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
    return sorted([NUM_MY[m] for m in NUM_MY_RE.findall(s)] + [int(d) for d in re.findall(r"\((\d+)\)", s)])


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
        (r"Yasmiṃ samaye", re.escape(F.UPPANNA + " " + F.YASMIM), "yasmiṃ samaye"),
    ]
    for p, m, name in pairs:
        a, b = len(re.findall(p, x)), len(re.findall(m, y))
        if name == "question":       # «Katame dhammā kusalā» has its own frame (KATAME_KUSALA, counted below)
            b -= len(re.findall(re.escape(F.KATAME_KUSALA), y))
        if a != b:
            errs.append(f"{name} {a} vs {b}")
    hoti = len(re.findall(r"\b(?:hoti|honti)\b", x))
    verbs = len(re.findall(r"ရှိသည်|ရှိကြသည်|အဘယ်နည်း|အဘယ်တို့နည်း|ဖြစ်သည်|ဖြစ်ကြသည်|"
                           + re.escape(F.UPPANNA + " " + F.YASMIM), y))
    verbs -= len(re.findall(re.escape(F.IME_KUSALA), y)) + len(re.findall(re.escape(F.KATAME_KUSALA), y))
    if hoti != verbs:
        errs.append(f"hoti {hoti} vs verbs {verbs}")
    ends_x = len(re.findall(r"[.?]", re.sub(r"\[[^\]]*\]", "", x)))
    if ends_x != y.count(F.END):
        errs.append(f"sentence ends {ends_x} vs {y.count(F.END)}")
    return errs


# ------------------------------------------------------------------ terms (own scanner)
ORDERED = {}
for d in (F.SYN, F.NAMES, F.GEN):
    for k, v in d.items():
        ORDERED.setdefault(k, v)
PRESENT = {**F.CITTA_KIND, **F.QUAL, **F.QUAL_ADV, **{k: v + F.ARAMMANA_VA for k, v in F.ARAMMANA.items()}}
MAXW = max(len(k.split()) for k in list(ORDERED) + list(PRESENT))
LIST_RE = re.compile(r"(?:Yo|Yā|Yaṃ)(?: tasmiṃ samaye)? (.*?) – ")


def words(s):
    return re.findall(r"[^\s,;?.\[\]…–]+", re.sub(r"\[[^\]]*\]|…pe…", " ", s))


def scan(s):
    """[(kind, pāli, burmese)] for the table words of a Pāli string, longest match first."""
    w, i, out = words(s), 0, []
    while i < len(w):
        for k in range(MAXW, 0, -1):
            key = " ".join(w[i:i + k])
            if len(w[i:i + k]) < k:
                continue
            low = key[0].lower() + key[1:]
            if low in PRESENT:
                out.append(("present", low, PRESENT[low]))
                i += k
                break
            if low in ORDERED:
                out.append(("ordered", low, ORDERED[low]))
                i += k
                break
        else:
            i += 1
    return out


def terms(x, y):
    errs = []
    m = re.fullmatch(r"(#+) (.+)", x)
    if m:
        exp = f"{m[1]} {F.HEAD[m[2]]}"
        return [] if exp == y else [f"heading: expected «{exp}»"]
    m = re.fullmatch(r"([^\[]+?)\.", x)
    if m and m[1] in F.COLO and m[1] in F._CU_TITLES:
        exp = F.COLO[m[1]] + F.END
        return [] if exp == y else [f"colophon: expected «{exp}»"]
    for k, v in F.BODY.items():
        if k in x:
            if y.count(v) != x.count(k):
                errs.append(f"body missing «{v[:30]}…»")
            x = x.replace(k, " ")
    pos = 0
    for kind, p, v in scan(x):
        if kind == "present":
            if v not in y:
                errs.append(f"missing «{v}» ({p})")
            continue
        j = y.find(v, pos)
        if j < 0:
            errs.append(f"order / missing «{v}» ({p})")
            break
        pos = j + len(v)
    for lst in LIST_RE.findall(x):
        seen = {}
        for _, p, v in scan(lst):
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
        t = terms(xb, yb)
        nterm += 1
        e += t
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
