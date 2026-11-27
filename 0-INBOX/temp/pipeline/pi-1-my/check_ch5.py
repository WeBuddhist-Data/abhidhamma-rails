"""Per-line check of the pi-1 Burmese chapter 5 (Aṭṭhakathākaṇḍa) against its Pāli (adapted from check_ch2-01.py).

usage: python3 -I -X utf8 check_ch5.py <pali_file> <burmese_file>
For every non-empty line (same order) it compares, independently of make_ch5.py (only the shared my_formulas tables
are read):
  1. block ids   - same id at the end of the same line;
  2. negations   - weighted Pāli negation morphemes (free na / no / neva / natthi; privative a- / an- words of PRIV;
                   double and triple forms) against Burmese negation syllables («မ» + an unclosed letter, «အကုသိုလ်»,
                   the abyākata phrase = 1); «ကာမ», «မနော» are not negations;
  3. numbers     - Pāli number words (cardinals, locatives, tika / duka …, the jhāna-method compounds) against
                   Burmese number + classifier;
  4. variants    - every «[text (sigla)]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla): text]»;
  5. frames      - counts per line: «Katame dhammā» = «ဟူသည် အဘယ်တို့နည်း»; «ime dhammā» = «ဤသဘောတရားများသည်»;
                   «ṭhapetvā» = «ကို ချန်ထား၍»; «na vattabb-» = «ခေါ်ဆို၍ မရ»; «siyā» = «တစ်ခါတစ်ရံ»; «uppajj-» =
                   «ဖြစ်ပေါ်(ကြ)သည် / ဖြစ်ပေါ်ကြရာ»; quoted «…ti / …tipi» = «ဟု»; «.» + «?» = «။»; «…pe…» = «…»;
  6. key words   - per-line counts of Pāli stems against their Burmese words (kusala, vipāka, kiriyā, cittuppāda,
                   rūpa, nibbāna, magga, phala, hetu, vedanā, lobha, dosa, moha and the nine cluster nouns);
  7. Mātikā      - every «Katame dhammā T?» question is the approved Mātikā string of T (TERMS / CEVA / CEVANO, a
                   «kho pana» pair as «X သဘောတရားများအနက် Y») + «သဘောတရားများ ဟူသည် အဘယ်တို့နည်း»; every
                   «– ime dhammā T.» closer with a single term T is «ဤသဘောတရားများသည် T-string …»;
  8. headings    - heading lines equal the table value; colophons as expected;
  9. typography  - no «?», «।», «:-», no Latin outside brackets, NFC, Myanmar code points U+1000-U+104F only, a line
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
    (r"nevasaññānāsaññ\w*", 3),
    (r"nevavipākanavipāk\w*", 2), (r"nevācayagāmināpacay\w*", 2), (r"nevasekkhanāsekkh\w*", 2),
    (r"adukkhamasukh\w*", 2), (r"anupādiṇṇaanupādāniy\w*", 2), (r"asaṃkiliṭṭhaasaṃkilesik\w*", 2),
    (r"avitakkaavicār\w*", 2), (r"anidassanaappaṭigh\w*", 2), (r"kusalākusalābyākat\w*", 2),
    (r"ya(?= vedanāya)", 2),          # 1389: source slip for «adukkhamasukhāya», rendered in full
    (r"(?:na|no|neva|Na|No|Neva|natthi)" + WE, 1),
]
PRIV = ("akusal abyākat anupādiṇṇ asaṃkiliṭṭh asaṃkilesik avitakk avicār appamāṇ aniyat anuppann anidassan "
        "appaṭigh ahetuk appaccay asaṅkhat arūp anāsav asaṃyojaniy aganthaniy anoghaniy ayoganiy anīvaraṇiy "
        "aparāmaṭṭh anārammaṇ acetasik cittavisaṃsaṭṭh visaṃsaṭṭh anupādāniy appītik apariyāpann aniyyānik "
        "anuttar araṇ avijj ahirik anottapp alobh ados amoh "
        # chapter 5
        "kiriyābyākat kiriyāhetuk kāmāvacarakiriyābyākat sabbākusal kusalābyākat dvādasākusal anindriy ārupp "
        "ākiñcañ ākāsānañc viññāṇañc").split()
NEG_PI += [(p + r"\w*", 1) for p in PRIV]
NEG_PI_RE = [(re.compile(WB + p, re.I), w) for p, w in NEG_PI]
# ------------------------------------------------------------------ negations (Burmese)
LETTER = "က-ဪ"
CLOSE = "္်"
NOT_NEG = ["ကာမ", "မနော"]
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
JN = {"ekaka": 1, "duka": 2, "tika": 3, "catukka": 4, "pañcaka": 5}
JH_PI = re.compile(r"(?:rūpāvacara|lokuttara)(ekaka|duka|tika|catukka)(duka|tika|catukka|pañcaka)jjhānā", re.I)
NUM_PI = [(r"\w*pañcakanaye", [5]), (r"dvepañcaviññāṇāni", [2, 5]), (r"dvādasā?\w*", [12]), (r"ekādasa", [11]),
          (r"tika\w*", [3]), (r"\w*duka\w*", [2]), (r"eko|ekā|ekaṃ", [1]), (r"dve|dvīsu|dvi\w*|dvā\w*", [2]),
          (r"tayo|tīṇi|tisso|tīsu", [3]), (r"cattāro|cattāri|catūsu|catunnañca|catunnaṃ|caturaṅgik\w*", [4]),
          (r"pañca|pañcaṅgik\w*", [5]), (r"cha", [6]), (r"satta|sattindriy\w*", [7]),
          (r"aṭṭha|aṭṭhasu|aṭṭhindriy\w*", [8]), (r"nava", [9]), (r"dasa", [10])]
NUM_PI_RE = [(re.compile(p, re.I), v) for p, v in NUM_PI]
NUM_MY = {"ဆယ့်တစ်": 11, "ဆယ့်နှစ်": 12, "တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6,
          "ခုနစ်": 7, "ရှစ်": 8, "ကိုး": 9, "ဆယ်": 10}
CLASSIFIER = "မျိုး|ပါး|ခု|စု|ချက်|ယောက်|ကြိမ်"
NUM_MY_RE = re.compile("(" + "|".join(sorted(NUM_MY, key=len, reverse=True)) + ")(?=" + CLASSIFIER + ")")
NUM_IDIOM = ["တစ်စုံတစ်ခု", "သူတစ်ပါး"]


def nums_pi(s):
    out = []
    for w in re.findall(W + "+", s):
        m = JH_PI.fullmatch(w)
        if m:
            a, b = JN[m[1].lower()], JN[m[2].lower()]
            out += [4, 5] if (a, b) == (4, 5) else [a, b, 4, 5]     # + the two method numbers
            continue
        for rx, v in NUM_PI_RE:
            if rx.fullmatch(w):
                out += v
                break
    return sorted(out + [int(d) for d in re.findall(r"\((\d+)\)", s)])


def nums_my(s):
    for i in NUM_IDIOM:
        s = s.replace(i, " ")
    return sorted([NUM_MY[m] for m in NUM_MY_RE.findall(s)] + [int(d) for d in re.findall(r"\((\d+)\)", s)])


# ------------------------------------------------------------------ variants
VAR_PI = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)\]")
VAR_MY = re.compile(r"\[(?P<k>" + F.PATHA + "|" + F.LEKHANA + r") \((?P<s>[^()]+)\): (?P<t>[^\]]+)\]")
VAR_KIND5 = {"dutiyajjhāne": F.LEKHANA, "sabbeva": F.PATHA}       # chapter 5 (as the Marathi track)


def var_check(x, y):
    a, b = VAR_PI.findall(x), VAR_MY.findall(y)
    if x.count("[") != y.count("[") or len(a) != len(b):
        return ["variant count"]
    errs = []
    for (t, s), (k, s2, t2) in zip(a, b):
        if t != t2:
            errs.append(f"variant text {t2}")
        if VAR_KIND5.get(t, F.VAR_KIND.get(t)) != k:
            errs.append(f"variant label {k} for {t}")
        if s2 != ", ".join(z[0].upper() + z[1:] for z in s.split()):
            errs.append(f"sigla {s2}")
    return errs


# ------------------------------------------------------------------ frames (counts)
DHS = F.DHAMMA_PL
FRAMES = [
    (r"Katame dhammā", r"ဟူသည် အဘယ်တို့နည်း", "question"),
    (r"ime dhammā", "ဤ" + DHS + "သည်", "ime dhammā"),
    (r"[Ṭṭ]hapetvā", re.escape(F.THAPETVA), "ṭhapetvā"),
    (r"na vattabb", r"ခေါ်ဆို၍ မရ", "na vattabbā"),
    (WB + r"siyā" + WE, r"တစ်ခါတစ်ရံ", "siyā"),
    (r"uppajj", r"ဖြစ်ပေါ်(?:ကြ)?(?:သည်|ရာ)", "uppajjati"),
    (r"tipi(?=[,.])|(?:ā|o|(?<!jja)n)ti(?=\.)", r"(?<!အမှန်)ဟု(?=လည်းကောင်း| )", "ti / tipi"),   # «ဤအရာသာ အမှန်ဟု …» is the shared kāyagantha name, not a «ti»
    (r"…pe…|…", r"…", "pe"),
]


def frames(x, y):
    errs = []
    for p, m, name in FRAMES:
        a, b = len(re.findall(p, x)), len(re.findall(m, y))
        if a != b:
            errs.append(f"{name} {a} vs {b}")
    ends_x = len(re.findall(r"[.?]", re.sub(r"\[[^\]]*\]", "", x)))
    if ends_x != y.count(F.END):
        errs.append(f"sentence ends {ends_x} vs {y.count(F.END)}")
    return errs


# ------------------------------------------------------------------ key words (counts)
ABY_N = F.TERMS["abyākatā"].removesuffix("သော")
KEY = [
    ("kusala", r"kusal", "ကုသိုလ်", lambda x: 2 * len(re.findall(r"byākat", x))),
    ("vipāka", r"vipāk", "အကျိုး", None),
    ("kiriyā", r"kiriy", "ပြုရုံမျှသာ", None),
    ("cittuppāda", r"cittuppād", F.MIND + " ဖြစ်ပေါ်မှု", None),
    ("rūpa", r"rūp(?!āyatan)|ārupp", "ရုပ်", None),
    ("nibbāna", r"nibbān", "နိဗ္ဗာန်", None),
    ("magga", r"magg", "မဂ်", None),
    ("phala", r"phal", "ဖိုလ်", None),
    ("hetu", r"hetu|hetū", "အမြစ်", lambda x: len(re.findall(r"neva dassanena na bhāvanāya pahātabbahetuk", x))),
    ("vedanā", r"vedan", "ခံစားမှု", lambda x: len(re.findall(r"vedanāya", x)) * 0),
    ("lobha", r"lobh", "လောဘ", None),
    ("dosa", r"(?<![a-z])(?:a)?dos[oa]", "ဒေါသ", None),
    ("moha", r"moh", "မောဟ", None),
]
for _st, _d in F.FAMILY.items():
    pat = {"āsava": r"(?<!parām)āsav", "saṃyojana": r"saṃyojan", "gantha": r"ganth", "ogha": r"ogh", "yoga": r"(?<![a-zā])yog",
           "nīvaraṇa": r"nīvaraṇ", "parāmāsa": r"parāmās|parāmaṭṭh", "upādāna": r"upādān|upādāniy",
           "kilesa": r"kiles|kiliṭṭh"}[_st]
    KEY.append((_st, pat, _d["N"], None))


def keys(x, y):
    errs = []
    for name, p, my, extra in KEY:
        a = len(re.findall(p, x, re.I)) + (extra(x) if extra else 0)
        b = len(re.findall(re.escape(my), y))
        if a != b:
            errs.append(f"{name} {a} vs {b}")
    return errs


# ------------------------------------------------------------------ Mātikā strings
def mat(t):
    if t in F.TERMS:
        return F.TERMS[t]
    m = re.fullmatch(r"(.+?) ceva (.+?) ca", t)
    if m and (m[1], m[2]) in F.CEVA:
        return F.CEVA[(m[1], m[2])]
    m = re.fullmatch(r"(.+?) ceva (?:no|na) ca (.+)", t)
    if m and (m[1], m[2]) in F.CEVANO:
        return F.CEVANO[(m[1], m[2])]
    m = re.fullmatch(r"(na hetū|\S+vippayuttā) (\S+)", t)
    if m and m[1] in F.TERMS and m[2] in F.TERMS:
        return f"{F.TERMS[m[1]]} {F.DHAMMA_AMONG} {F.TERMS[m[2]]}"
    return None


def matika(x, y):
    errs = []
    for t in re.findall(r"Katame dhammā (.+?)(?:…pe…)?[?.](?: |$)", x):
        s = mat(t)
        if s is None:
            errs.append(f"unknown term {t}")
        elif f"{s} {DHS} ဟူသည် အဘယ်တို့နည်း" not in y:
            errs.append(f"question string for {t}")
    for t in re.findall(r"– ime dhammā ([^.,;]+?)\.(?: |$)", x):
        if t.startswith(("siyā", "na vattabb")) or " siyā " in t:
            continue
        s = mat(t)
        if s is None:
            continue
        exp = f"ဤ{DHS}သည် {s} ဖြစ်ကြသည်" if t in ("kusalā", "akusalā") else f"ဤ{DHS}သည် {s} {DHS} ဖြစ်ကြသည်"
        if exp not in y:
            errs.append(f"closer string for {t}")
    return errs


HEAD5 = {"Aṭṭhakathākaṇḍaṃ": f"အနက်ဖွင့် {F.KANDA}", "Tikaatthuddhāro": f"{F.TIKA}တို့၏ အနက် ထုတ်ဖော်ချက်",
         "Dukaatthuddhāro": f"{F.DUKA}တို့၏ အနက် ထုတ်ဖော်ချက်"}
COLO5 = {"Tikaṃ.": F.TIKA + F.END, "Atthuddhāro niṭṭhito.": f"“အနက် ထုတ်ဖော်ချက်” {F.NITTHITA}{F.END}",
         "Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ.": f"“{F.TITLE}” ကျမ်း {F.NITTHITA}{F.END}"}

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
    for i, (x, y) in enumerate(zip(a, b), 1):
        mx, my_ = ID_RE.search(x), ID_RE.search(y)
        if (mx and mx[1]) != (my_ and my_[1]):
            probs.append(f"line {i}: block id")
        xb = x[:mx.start()] if mx else x
        yb = y[:my_.start()] if my_ else y
        e = []
        xs, ys = strip_br(xb), strip_br(yb)
        m = re.fullmatch(r"(#+) (.+)", xb)
        if m:
            exp = f"{m[1]} {HEAD5.get(m[2]) or F.HEAD.get(m[2])}"
            if exp != yb:
                e.append(f"heading: expected «{exp}»")
        else:
            np_, nm = neg_count(xs, NEG_PI_RE), neg_count(ys, NEG_MY_RE)
            if np_ != nm:
                e.append(f"negations {np_} vs {nm}")
            e += frames(xb, yb)
            e += keys(xs, ys)
            e += matika(xb, yb)
            if xb in COLO5 and yb != COLO5[xb]:
                e.append(f"colophon: expected «{COLO5[xb]}»")
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
        if e:
            probs.append(f"line {i}: " + "; ".join(e[:5]))
    if probs:
        bad += 1
        print(f"{tgt}: {len(probs)} mismatches")
        for p in probs[:40]:
            print("  ", p)
    else:
        print(f"{tgt}: OK ({len(b)} lines, 0 mismatches)")
sys.exit(1 if bad else 0)
