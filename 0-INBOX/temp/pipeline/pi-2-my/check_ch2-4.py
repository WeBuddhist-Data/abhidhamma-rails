"""Per-line check of the pi-2 Burmese chapters 2-4 against their Pāli, plus the pi-1 reuse test.
(Adapted from check_sample.py: wider variant brackets, the number words and privatives of chapters 2-4, the source
slips read as make_ch2-4.py reads them.)

usage: python3 -I -X utf8 check_ch2-4.py <pali_file> <burmese_file> [...pairs]
For every non-empty line (same order) it compares:
  1. sentences  - Pāli sentence ends («.» «?» outside variant brackets) = Burmese «။»;
  2. negations  - weighted count of Pāli negation morphemes (free na / no / neva, the privative a- / an- words of
                  PRIV, double forms = 2) against Burmese negation markers («မ» before a verb, «အကုသိုလ်», the
                  abyākata phrase = 1); own tables, independent of my2_formulas;
  3. numbers    - Pāli number words (ekavidhena … catuvīsati, cattāro, tayo, dve, pañca, chahi, tika / duka) against
                  Burmese number words before «မျိုး / ပါး»;
  4. variants   - every Pāli «[text (sigla)]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla): text]», same text and order;
  5. lists      - every definition list «Yaṃ / Yā / Ye N … ,» and «yaṃ vā panaññampi atthi rūpaṃ …»: the Burmese
                  of each item (DEF table) occurs, in order, and the item count equals the Pāli count; two different
                  Pāli items never share a Burmese item;
  6. terms      - every «siyā T» / «atthi T» / «kati T» of the line: the table value of T occurs in the line;
  7. typography - no «?», «।», «:-», no Latin letters outside the variant brackets, Myanmar only U+1000-U+104F, NFC.
Then the pi-1 REUSE TEST: every Pāli sentence (and heading) of the file that also occurs in pi-1 (Pāli, spelling
upādinn = upādiṇṇ) must have exactly pi-1's final Burmese sentence (rails text). Prints n / n.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my2_formulas as F  # noqa: E402  (tables only)

WB = r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])"
WE = r"(?![A-Za-zāīūṃṅñṭḍṇḷ])"
VAR_PI = re.compile(r"\[[^\[\]]+\]")
VAR_ONE = re.compile(r"\s*(?P<t>[^(),]+?) \((?P<s>[^()]+)\),?")
VAR_MY = re.compile(r"\[(?:" + F.P1.PATHA + "|" + F.P1.LEKHANA + r") \([^()]+\): [^\]]+\]")

# ------------------------------------------------------------------ negations
NEG_PI = [
    (r"nevavipākanavipāk\w*", 2), (r"nevācayagāmināpacay\w*", 2), (r"nevasekkhanāsekkh\w*", 2),
    (r"adukkhamasukh\w*", 2), (r"anupādi[nṇ][nṇ]aanupādāniy\w*", 2), (r"asaṃkiliṭṭhaasaṃkilesik\w*", 2),
    (r"avitakkaavicār\w*", 2), (r"anidassanaappaṭigh\w*", 2), (r"neva dassanena na bhāvanāya", 2),
    (r"āsavavippayuttaanāsav\w*|\w+vippayuttaa\w+|āsavippayuttaanāsav\w*", 1),
    (r"neva kusalā nākusalā na ca kammavipākā", 2),       # = Burmese abyākata phrase + «ကံ၏ အကျိုးလည်း မဟုတ်»
    (r"nāsāt\w*|nākusal\w*", 2),
    (r"(?:na|no|neva|Na|No|Neva)" + WE, 1),
]
PRIV = ("anupādi asaṃkiliṭṭh asaṃkilesik avitakk avicār appamāṇ aniyat anuppann anidassan appaṭigh "
        "ahetuk appaccay asaṅkhat arūp anāsav asaṃyojaniy aganthaniy anoghaniy ayoganiy anīvaraṇiy aparāmaṭṭh "
        "anārammaṇ acetasik cittavisaṃsaṭṭh anupādāniy appītik apariyāpann aniyyānik anuttar araṇ "
        "ajāt abhūt asañjāt anibbatt anabhinibbatt apātubhūt asamuppann anuṭṭhit asamuṭṭhit "
        "acittīkat anuññāt anavaññāt ahīḷit aparibhūt aniṭṭh akant amanāp anāsanne anupakaṭṭhe asantike avidūre "
        "asamāpann anicc anatt amanuss asād araj asamphuṭṭh avijj asāt abyāpād avihiṃs aññāṇ adassan anabhisamay "
        "ananubodh asambodh appaṭivedh asaṅgāh apariyogāh asamapekkh apaccavekkh apaccakkh asampajañ appiy ahit aphāsuk ayogakkhem asaṅgat asamāgam asamodhān amissībhāv asesa "
        "anālay anuppād asammos amoh akiriy akaraṇ anajjhāpatt adinn avikkhep").split()
NEG_PI += [(p + r"\w*", 1) for p in PRIV]
NEG_PI += [(r"ahetu(?![\wāīūṃṅñṭḍṇḷ])", 1)]          # consistency pass: ^2-184 «atthi ahetu» as written (a-hetu)
NEG_PI_RE = [(re.compile(WB + p, re.I), w) for p, w in NEG_PI]
NEG_PI_RE += [(re.compile(r"anatikkam|[aā]kusal|byākat|het[uū]ahetuk|(?<!citta)visaṃsaṭṭh", re.I), 1)]          # inside compounds too (kusalākusalā, kusalābyākatā)
LETTER, CLOSE = "က-ဪ", "္်"
NEG_MY = [("ကာမ|မနော|မည်သည့်|မဆို|သို့မဟုတ်", 0), (re.escape(F.T["abyākatā"].removesuffix("သော")), 1), ("အကုသိုလ်", 1),
          (r"မ(?=[" + LETTER + r"](?!့?[" + CLOSE + r"]))", 1)]
NEG_MY_RE = [(re.compile(p), w) for p, w in NEG_MY]


def neg(s, table):
    n = 0
    for rx, w in table:
        n += len(rx.findall(s)) * w
        s = rx.sub(" ", s)
    return n


# ------------------------------------------------------------------ numbers
NUM_PI = [(r"ekavidh\w*", 1), (r"duvidh\w*", 2), (r"tividh\w*", 3), (r"catubbidh\w*", 4), (r"pañcavidh\w*", 5),
          (r"chabbidh\w*", 6), (r"sattavidh\w*", 7), (r"aṭṭhavidh\w*", 8), (r"navavidh\w*", 9), (r"dasavidh\w*", 10),
          (r"ekādasavidh\w*", 11), (r"catuvīsatividh\w*", 24), (r"tiṃsa(?:ti)?vidh\w*", 30),
          (r"pañcakkhandhā|pañcannaṃ", 5), (r"cattāro|catunnañca|catunnaṃ", 4), (r"tayo", 3), (r"dve", 2),
          (r"chahi", 6), (r"tikaṃ|tikamūlakaṃ|kusalattike|tikā", 3), (r"dukaṃ|dukamūlakaṃ", 2),
          # chapters 2-4: counted subjects and heads
          (r"dvādas\w*", 12), (r"ekādas\w*", 11), (r"dasāyatan\w*|dasa", 10), (r"navāyatan\w*|nava", 9),
          (r"aṭṭha", 8), (r"satta(?:dhātuyo)?", 7), (r"chāyatan\w*|cha", 6), (r"pañcāyatan\w*|pañca", 5),
          (r"dvāyatan\w*|dve", 2), (r"cattāri|cattāro|catunnaṃ|catūhi", 4), (r"tīṇi|tīhi|tisso|tiṇṇañca", 3),
          (r"soḷasa", 16), (r"pannarasa", 15), (r"sattarasa", 17), (r"aṭṭhārasa\w*", 18),
          (r"aṭṭhaṅgiko|aṭṭhaṅgikaṃ", 8), (r"pañcaṅgiko|pañcaṅgikaṃ", 5), (r"pañcupādānakkhandhā", 5),
          (r"chakkāni", 6), (r"dvayaṃ|\w+dvayaṃ", 2), (r"dasasu", 10), (r"tadekajjhaṃ", 1)]
NUM_PI_RE = [(re.compile(p, re.I), v) for p, v in NUM_PI]
NUM_MY = {"နှစ်ဆယ့်လေး": 24, "သုံးဆယ်": 30, "ဆယ့်ရှစ်": 18, "ဆယ့်ခုနစ်": 17, "ဆယ့်ခြောက်": 16, "ဆယ့်ငါး": 15,
          "ဆယ့်နှစ်": 12, "ဆယ့်တစ်": 11, "ဆယ်": 10, "ကိုး": 9, "ရှစ်": 8, "ခုနစ်": 7,
          "ခြောက်": 6, "ငါး": 5, "လေး": 4, "သုံး": 3, "နှစ်": 2, "တစ်": 1}
NUM_MY_RE = re.compile(r"(?<![က-႟])(" + "|".join(NUM_MY) + ")(?=မျိုး|ပါး|စု(?!ံ))")


def nums_pi(s):
    out = []
    for w in re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]+", s):
        for rx, v in NUM_PI_RE:
            if rx.fullmatch(w):
                out.append(v)
                break
    return sorted(out)


def nums_my(s):
    s = s.replace("အမျိုးမျိုး", "")
    return sorted(NUM_MY[m] for m in NUM_MY_RE.findall(s.replace(" ", " ")))


# ------------------------------------------------------------------ lists
DEF_RE = re.compile(r"(?:Yaṃ|Yā|Ye) (?!rūpaṃ catunnaṃ)(?:rūpaṃ|vedanā|saññā|saṅkhārā|viññāṇaṃ) (?:tesaṃ tesaṃ (?:para)?sattānaṃ "
                    r"(?:parapuggalānaṃ )?)?(?P<l>[^,]+?),|yaṃ vā panaññampi atthi rūpaṃ (?P<l2>[^–]+?) –")


def list_errs(x, y):
    errs, pos = [], 0
    for m in DEF_RE.finditer(x):
        words = (m["l"] or m["l2"]).split(" ")
        keys, i = [], 0
        while i < len(words):                    # own longest-first split against the DEF keys
            for k in range(4, 0, -1):
                key = F.dkey(" ".join(words[i:i + k]))
                if len(words[i:i + k]) == k and key in F.DEF:
                    keys.append(key)
                    i += k
                    break
            else:
                errs.append("list word " + words[i])
                break
        mys = [F.DEF[k] for k in keys]
        seen = {}
        for k, v in zip(keys, mys):
            if v in seen and seen[v] != k:
                errs.append(f"two items share {v}")
            seen[v] = k
        s = f"{F.C} ".join(mys)
        j = y.find(s, pos)
        if j < 0:
            errs.append("list not found: " + s[:60])
        else:
            pos = j + len(s)
        if len(keys) != len(words) - sum(len(k.split(" ")) - 1 for k in keys):
            errs.append("list count")
    return errs


TERM_RE = re.compile(r"(?:siyā|[Aa]tthi|kati) (?!rūpaṃ|na vattabb)((?:(?!atthi |siyā )[\wāīūṃṅñṭḍṇḷ]+ ?){1,7}?)"
                     r"(?=, |\.|;|…|\?| atthi |$)")


def term_errs(x, y):
    errs = []
    for t in TERM_RE.findall(x):
        t = t.strip().replace("upādinn", "upādiṇṇ")
        try:
            v = F.term_my(t)
        except F.Miss:
            continue                               # matter predicates (pi-1 Rūpakaṇḍa tables) are not terms
        if v not in y:
            errs.append("term " + t)
    return errs


# ------------------------------------------------------------------ typography
def typo_errs(y):
    errs = []
    if any(c in y for c in "?।") or ":-" in y:
        errs.append("forbidden mark")
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", VAR_MY.sub("", y)):
        errs.append("Latin outside variants")
    if re.search(r"[ၐ-႟ꧠ-꧿ꩠ-ꩿ]", y):
        errs.append("code point outside U+1000-104F")
    if unicodedata.normalize("NFC", y) != y:
        errs.append("not NFC")
    return errs


def sent_count(x):
    x = VAR_PI.sub("", x).replace("…pe…", "…").replace("…Pe…", "…")
    return len(re.findall(r"[.?](?=\"|”|\)|\s|$)", x))


SLIPS = {   # source slips, read as make_ch2-4.py reads them (notes-ch2-4.md); consistency pass: the content slips
    # («no ca na kilesā», «atthi ahetu», «ajjhattaṃ») are now translated as written, so they are no longer replaced here
    "vata, no ": "vata, amhākaṃ ",               # «no» = to us (pronoun), not a negation
}


def check(pali, my):
    a = [l for l in pathlib.Path(pali).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l for l in pathlib.Path(my).read_text(encoding="utf-8").splitlines() if l.strip()]
    bad = []
    if len(a) != len(b):
        return [f"line count {len(a)} vs {len(b)}"], 0
    lists = 0
    for i, (x, y) in enumerate(zip(a, b)):
        x = F.ID_RE.sub("", x)
        for k, v in SLIPS.items():
            x = x.replace(k, v)
        y = F.ID_RE.sub("", y)
        errs = []
        if not x.startswith("#") and sent_count(x) != y.count(F.END):
            errs.append(f"sentences {sent_count(x)}/{y.count(F.END)}")
        if neg(VAR_PI.sub("", x), NEG_PI_RE) != neg(VAR_MY.sub("", y), NEG_MY_RE):
            errs.append(f"negations {neg(VAR_PI.sub('', x), NEG_PI_RE)}/{neg(VAR_MY.sub('', y), NEG_MY_RE)}")
        if nums_pi(VAR_PI.sub("", x)) != nums_my(y):
            errs.append(f"numbers {nums_pi(x)}/{nums_my(y)}")
        va, vb = VAR_PI.findall(x), VAR_MY.findall(y)
        if len(va) != len(vb) or any(any(t.strip() not in b for t, _ in VAR_ONE.findall(a[1:-1]))
                                                         for a, b in zip(va, vb)):
            errs.append("variants")
        lists += len(DEF_RE.findall(x))
        errs += list_errs(x.replace("upādinn", "upādiṇṇ"), y) + term_errs(x, y) + typo_errs(y)
        if errs:
            bad.append(f"line {i + 1}: " + "; ".join(errs))
    return bad, lists


# ------------------------------------------------------------------ pi-1 reuse
def psplit(l):
    l = F.ID_RE.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)      # no split inside variant brackets
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def bsplit(l):
    l = F.ID_RE.sub("", l)
    return [s for s in re.split(r"(?<=။) ", l) if s]


def pi1_dict():
    D = {}
    for p in sorted(F.P1_PALI.glob("*.md")):
        pl = p.read_text(encoding="utf-8-sig").split("\n")
        bl = (F.P1_RAILS / p.name).read_text(encoding="utf-8").split("\n")
        for x, y in zip(pl, bl):
            if not x.strip():
                continue
            if x.startswith("#"):
                D.setdefault(F.ID_RE.sub("", x).split(" ", 1)[1], set()).add(F.ID_RE.sub("", y).split(" ", 1)[1])
                continue
            ps, bs = psplit(x), bsplit(y)
            if len(ps) == len(bs):
                for s, t in zip(ps, bs):
                    D.setdefault(s.replace("upādinn", "upādiṇṇ"), set()).add(t)
    return D


def reuse(pali, my, D):
    a = [l for l in pathlib.Path(pali).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l for l in pathlib.Path(my).read_text(encoding="utf-8").splitlines() if l.strip()]
    n = same = 0
    diffs = []
    for i, (x, y) in enumerate(zip(a, b)):
        if x.startswith("#"):
            pairs = [(F.ID_RE.sub("", x).split(" ", 1)[1], F.ID_RE.sub("", y).split(" ", 1)[1])]
        else:
            ps, bs = psplit(x), bsplit(y)
            if len(ps) != len(bs):
                diffs.append(f"line {i + 1}: sentence split {len(ps)}/{len(bs)}")
                continue
            pairs = list(zip(ps, bs))
        for s, t in pairs:
            k = s.replace("upādinn", "upādiṇṇ")
            if k in D:
                n += 1
                if t in D[k]:
                    same += 1
                else:
                    diffs.append(f"line {i + 1}: «{s[:60]}» pi-1 «{sorted(D[k])[0][:60]}» here «{t[:60]}»")
    return n, same, diffs


if __name__ == "__main__":
    args = sys.argv[1:]
    D = pi1_dict()
    total_bad, tn, ts = 0, 0, 0
    for pali, my in zip(args[::2], args[1::2]):
        bad, lists = check(pali, my)
        n, same, diffs = reuse(pali, my, D)
        tn, ts = tn + n, ts + same
        name = pathlib.Path(my).name
        print(f"{name}: {len(bad)} mismatches ({lists} definition lists checked); pi-1 reuse {same} / {n} identical")
        for e in bad[:20] + diffs[:20]:
            print("  " + e)
        total_bad += len(bad) + len([d for d in diffs if "pi-1" in d])
    print("OK" if not total_bad else "MISMATCH")
    sys.exit(1 if total_bad else 0)
