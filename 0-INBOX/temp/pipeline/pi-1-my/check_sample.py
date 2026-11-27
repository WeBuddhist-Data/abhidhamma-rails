"""Per-line check of a pi-1 Burmese chapter against its Pāli.

usage: python3 -I -X utf8 check_sample.py <pali_file> <burmese_file> [...pairs]
For every non-empty line (same order) it compares:
  1. letters    - item letter «(Ka) (Kha) (Ga)» -> «(က) (ခ) (ဂ)» (my_formulas.LABEL), same order;
  2. negations  - weighted count of Pāli negation morphemes (free na / no / neva, the privative «a- / an-» words of
                  PRIV, the double forms «neva…na…» / «a-X-a-Y» = 2) against Burmese negation markers (the syllable
                  «မ» before a verb: «မ» + a letter that does not close it, i.e. «မဟုတ်», «မရှိ», «မဖြစ်»; plus
                  «အကုသိုလ်»; the abyākata phrase counts 1); independent of my_formulas;
  3. numbers    - Pāli «tika / duka» (and number words, for later chapters) against Burmese «သုံးမျိုး / နှစ်မျိုး» …;
  4. variants   - every Pāli «[text (sigla)]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla, …): text]», same count, same text,
                  the label as in my_formulas.VAR_KIND, sigla capitalised;
  5. terms      - every mātikā line is parsed here (own patterns) into its Pāli term(s) and the expected Burmese is
                  rebuilt from the tables (TERMS, CEVA, CEVANO, SUT, MFIXED, COLO, HEAD): the line must be equal;
                  each term's table value must also occur in the line;
  6. typography - no «?», «।», «:-», no Latin letters outside the variant brackets, Myanmar letters only from
                  U+1000-U+104F (no Zawgyi-range code points), NFC, a mātikā / colophon line ends with «။».
Prints OK or the mismatching lines; exit 1 on any mismatch.
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my_formulas as F  # noqa: E402  (tables only; the parsing below is independent of F.translate)

W = "[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]"
WB = r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])"
WE = r"(?![A-Za-zāīūṃṅñṭḍṇḷ])"
# ------------------------------------------------------------------ negations (Pāli)
NEG_PI = [
    (r"nevavipākanavipāk\w*", 2), (r"nevācayagāmināpacay\w*", 2), (r"nevasekkhanāsekkh\w*", 2),
    (r"adukkhamasukh\w*", 2), (r"anupādiṇṇaanupādāniy\w*", 2), (r"asaṃkiliṭṭhaasaṃkilesik\w*", 2),
    (r"avitakkaavicār\w*", 2), (r"anidassanaappaṭigh\w*", 2),
    (r"(?:na|no|neva|Na|No|Neva)" + WE, 1),
]
PRIV = ("akusal abyākat anupādiṇṇ asaṃkiliṭṭh asaṃkilesik avitakk avicār appamāṇ aniyat anuppann anidassan "
        "appaṭigh ahetuk appaccay asaṅkhat arūp anāsav asaṃyojaniy aganthaniy anoghaniy ayoganiy anīvaraṇiy "
        "aparāmaṭṭh anārammaṇ acetasik cittavisaṃsaṭṭh anupādāniy appītik apariyāpann aniyyānik anuttar "
        "araṇ avijj atapanīy ahirik anottapp dovacass aguttadvār amattaññ asampajañ asantuṭṭh appaṭivān "
        "anuppād anantavā aṭṭhān avikkhep").split()
NEG_PI += [(p + r"\w*", 1) for p in PRIV]
NEG_PI_RE = [(re.compile(WB + p, re.I), w) for p, w in NEG_PI]
# ------------------------------------------------------------------ negations (Burmese)
LETTER = "က-ဪ"                   # consonants and independent vowels
CLOSE = "္်"                     # virama (stack) / asat: the letter closes the «မ» syllable
NOT_NEG = ["ကာမ"]                         # words with a free «မ» syllable that is not a negation (kāma-)
NEG_MY = [
    ("|".join(NOT_NEG), 0),
    (re.escape(F.TERMS["abyākatā"].removesuffix("သော")), 1),     # «neither K nor A-K» = the one privative of abyākata
    (r"အကုသိုလ်", 1),
    (r"မ(?=[" + LETTER + r"](?!\u1037?[" + CLOSE + r"]))", 1),     # «့» may stand before «်»
]
NEG_MY_RE = [(re.compile(p), w) for p, w in NEG_MY]


def neg_count(s, table):
    n = 0
    for rx, w in table:
        k = len(rx.findall(s))
        n += k * w
        s = rx.sub(" ", s)
    return n


# ------------------------------------------------------------------ numbers
NUM_PI = [(r"tika\w*", 3), (r"\w*duka\w*", 2), (r"eko|ekā|ekaṃ", 1), (r"dve|dvi\w*", 2), (r"tayo|tīṇi", 3),
          (r"cattāro|cattāri", 4), (r"pañca", 5)]
NUM_PI_RE = [(re.compile(p, re.I), v) for p, v in NUM_PI]
NUM_MY = {"တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6, "ခုနစ်": 7, "ရှစ်": 8}
CLASSIFIER = "မျိုး|ပါး|ခု|ချက်|ယောက်|ကြိမ်"
NUM_MY_RE = re.compile("(" + "|".join(NUM_MY) + ")(?=" + CLASSIFIER + ")")
NUM_IDIOM = ["တစ်စုံတစ်ခု", "သူတစ်ပါး"]          # «some», «others»: not numbers


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


# ------------------------------------------------------------------ terms (own parser)
D, END = F.DHAMMA_PL, F.END


def expect(body):
    """(expected Burmese, [table values that must occur]) for one Pāli line body, or (None, []) if not a term line."""
    if body == "Namo tassa bhagavato arahato sammāsambuddhassa":
        return F.NAMO, [F.NAMO]
    m = re.fullmatch(r"(#+) (.+)", body)
    if m:
        h = {**F.HEAD, "Abhidhammapiṭake": F.ABHI, "Dhammasaṅgaṇīpāḷi": F.TITLE}[m[2]]
        return f"{m[1]} {h}", [h]
    m = re.fullmatch(r"(\((?:Ka|Kha|Ga)\)) (.+)", body)
    if not m:
        m2 = re.fullmatch(r"([^\[]+?)(?: (\[[^\]]+\]))?\.", body)
        if m2 and m2[1] in F.COLO:
            v = " " + F.var_my(m2[2]) if m2[2] else ""
            return f"{F.COLO[m2[1]]}{v}{END}", [F.COLO[m2[1]]]
        return None, []
    lab, r = F.LABEL[m[1]] + " ", m[2]
    if r in F.MFIXED:
        return lab + F.MFIXED[r], [F.MFIXED[r]]
    m = re.fullmatch(r"(.+?) ceva dhammā (.+?) ca\.", r)
    if m:
        v = F.CEVA[(m[1], m[2])]
        return f"{lab}{v} {D}{END}", [v]
    m = re.fullmatch(r"(.+?) ceva dhammā (?:na|no) ca (.+?)\.", r)
    if m:
        v = F.CEVANO[(m[1], m[2])]
        return f"{lab}{v} {D}{END}", [v]
    m = re.fullmatch(r"(.+?) kho pana dhammā (.+?)pi\.", r)
    if m:
        x, y = F.TERMS[m[1]], F.TERMS[m[2]]
        return f"{lab}{F.KHO_PANA} {x} {F.DHAMMA_AMONG} {y[:-3]}သည်တို့{F.PI}{END}", [x, y[:-3]]
    m = re.fullmatch(r"(.+?)(?: (\[[^\]]+\]))? dhammā\.", r) or re.fullmatch(r"(\S+dhammadhammā)()\.", r)
    if m:
        t = F.TERMS[m[1]]
        v = " " + F.var_my(m[2]) if m[2] else ""
        return f"{lab}{t}{v} {D}{END}", [t]
    m = re.fullmatch(r"(\S+)pi\.", r)
    if m:
        y = F.TERMS[m[1]]
        return f"{lab}{y[:-3]}သည်တို့{F.PI}{END}", [y[:-3]]
    m = re.fullmatch(r"(.+?)(?: ca|ñca)(?: (\[[^\]]+\]))?\.", r)
    if m:
        t = F.SUT[m[1]]
        v = " " + F.var_my(m[2]) if m[2] else ""
        return f"{lab}{t}{v}{END}", [t]
    raise KeyError("no check pattern: " + body)


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
        lx = re.match(r"\((Ka|Kha|Ga)\)", xb)
        ly = re.match(r"\((က|ခ|ဂ)\)", yb)
        if (lx and F.LABEL[lx[0]]) != (ly and ly[0]):
            e.append("item letter")
        xs, ys = strip_br(xb), strip_br(yb)
        if not xb.startswith("#"):
            np_, nm = neg_count(xs, NEG_PI_RE), neg_count(ys, NEG_MY_RE)
            if np_ != nm:
                e.append(f"negations {np_} vs {nm}")
        if nums_pi(xs) != nums_my(ys):
            e.append(f"numbers {nums_pi(xs)} vs {nums_my(ys)}")
        e += var_check(xb, yb)
        for ch in ("?", "।", ":-"):
            if ch in yb:
                e.append(f"contains {ch}")
        if re.search(W, re.sub(r"\[[^\]]*\]", "", yb)):
            e.append("Latin outside brackets")
        if not xb.startswith("#") and xb.endswith(".") and not yb.endswith(END):
            e.append("no ။ at the end")
        try:
            exp, vals = expect(xb)
        except KeyError as k:
            exp, vals = None, []
            e.append(str(k))
        if exp is not None:
            nterm += 1
            if exp != yb:
                e.append(f"term: expected «{exp}»")
            for v in vals:
                if v not in yb:
                    e.append(f"table value missing «{v}»")
        if e:
            probs.append(f"line {i}: " + "; ".join(e[:4]))
    if probs:
        bad += 1
        print(f"{tgt}: {len(probs)} mismatches")
        for p in probs[:40]:
            print("  ", p)
    else:
        print(f"{tgt}: OK ({len(b)} lines, {nterm} term lines checked, 0 mismatches)")
sys.exit(1 if bad else 0)
