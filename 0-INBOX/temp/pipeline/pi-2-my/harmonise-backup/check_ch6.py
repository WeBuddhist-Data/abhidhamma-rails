"""Per-line check of the pi-2 Burmese chapter 6 against its Pāli, the pi-1 reuse test and the opening test.

usage: python3 -I -X utf8 check_ch6.py <pali_file> <burmese_file>
Adapted from check_sample.py. For every non-empty line (same order) it compares:
  1. sentences  - Pāli sentence ends («.» «?» outside variant brackets) = Burmese «။»;
  2. negations  - weighted count of Pāli negation morphemes (free na / no / neva, the privative a- / an- words of
                  PRIV, double forms = 2) against Burmese negation markers («မ» before a verb, «အကုသိုလ်», the
                  abyākata phrase = 1); own tables, independent of the generator;
  3. numbers    - Pāli number words (duvidhena, cattāro, saḷāyatana, -catukka, eka- / catu- / pañcavokāra …) against
                  Burmese number words before «မျိုး / ပါး»;
  4. variants   - every Pāli «[text (sigla)]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla): text]», same text and order;
  5. lists      - every definition list «Yo / Yā / Yaṃ … –» (and the soka / parideva / upāyāsa lists after
                  «phuṭṭhassa»): its Pāli items are found in the generator's list tables (in order, «…pe…» gaps
                  allowed), the Burmese of each item occurs in the line in that order, the item count is the Pāli
                  count, and two different Pāli items of one list never share a Burmese item;
  6. terms      - every «siyā T» / «atthi T» / «kati T» with a mātikā term: its value occurs in the line;
  7. typography - no «?», «।», «:-», no Latin letters outside the variant brackets, Myanmar only U+1000-U+104F, NFC.
Then the pi-1 REUSE TEST: every Pāli sentence (and heading) of the file that also occurs in pi-1 must have exactly
pi-1's final Burmese sentence (rails text), and the OPENING TEST: the generator's opening() reproduces the final pi-1
Burmese of every pi-1 cittuppāda opening «Yasmiṃ samaye …, tasmiṃ samaye» that it can parse. Prints n / n.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my2_formulas as F  # noqa: E402  (tables only)
import make_ch6 as G  # noqa: E402  (tables only; writes nothing at import)

WB = r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])"
WE = r"(?![A-Za-zāīūṃṅñṭḍṇḷ])"
VAR_PI = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)\]")
VAR_MY = re.compile(r"\[(?P<k>" + F.P1.PATHA + "|" + F.P1.LEKHANA + r") \((?P<s>[^()]+)\): (?P<t>[^\]]+)\]")

# ------------------------------------------------------------------ negations
NEG_PI = [
    (r"nevasaññānāsaññ\w*", 3), (r"neva sātaṃ nāsātaṃ", 3),
    (r"neva kusal\w* nākusal\w*", 1),          # = the abyākata phrase «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်» (1)
    (r"adukkhamasukh\w*", 2), (r"(?:na|no|neva|Na|No|Neva)" + WE, 1),
]
PRIV = ("avijj aññāṇ adassan anabhisamay ananubodh asambodh appaṭivedh asaṃgāhan apariyogāh asamapekkhan "
        "apaccavekkhan apaccakkhakamm asampajañ akusamūl apuññ āneñj asaññ asāt alobh alubbh asārāg asārajj anabhijjh "
        "ākiñcaññ adoso adussan adussit abyāpād abyāpajj amoh avūpasam anattaman anekaṃs avikkhep aniccat arūp").split()
NEG_PI += [(p + r"\w*", 1) for p in PRIV]
NEG_PI_RE = [(re.compile(WB + p, re.I), w) for p, w in NEG_PI]
NEG_PI_RE += [(re.compile(r"[aā]kusal|byākat", re.I), 1)]          # inside compounds too (Akusalaniddeso …)
LETTER, CLOSE = "က-ဪ", "္်"
NEG_MY = [("ကာမ|မနော|မည်သည့်|မဆို(?!း)|သို့မဟုတ်", 0), (re.escape(F.T["abyākatā"].removesuffix("သော")), 1), ("အကုသိုလ်", 1),
          (r"မ(?=[" + LETTER + r"](?!့?[" + CLOSE + r"]))", 1)]
NEG_MY_RE = [(re.compile(p), w) for p, w in NEG_MY]


def neg(s, table):
    n = 0
    for rx, w in table:
        n += len(rx.findall(s)) * w
        s = rx.sub(" ", s)
    return n


# ------------------------------------------------------------------ numbers
NUM_PI = [(r"duvidh\w*", 2), (r"cattāro|catunnañca|catunnaṃ", 4), (r"saḷāyatan\w*", 6), (r"\w*catukk\w*", 4),
          (r"ekavokār\w*", 1), (r"catuvokār\w*", 4), (r"pañcavokār\w*", 5)]
NUM_PI_RE = [(re.compile(p, re.I), v) for p, v in NUM_PI]
NUM_MY = {"နှစ်ဆယ့်လေး": 24, "သုံးဆယ်": 30, "ဆယ့်တစ်": 11, "ဆယ်": 10, "ကိုး": 9, "ရှစ်": 8, "ခုနစ်": 7,
          "ခြောက်": 6, "ငါး": 5, "လေး": 4, "သုံး": 3, "နှစ်": 2, "တစ်": 1}
NUM_MY_RE = re.compile(r"(?<![က-႟])(" + "|".join(NUM_MY) + ")(?=မျိုး|ပါး)")


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
    return sorted(NUM_MY[m] for m in NUM_MY_RE.findall(s))


# ------------------------------------------------------------------ lists
LIST_RE = re.compile(r"(?:(?<=\? )|^)(?:Yo|Yā|Yaṃ) (?P<l>[^–]+?) –|(?<=phuṭṭhassa )(?P<l2>[^–]+?) –")
NOT_LISTS = ("rūpaṃ nissāya",)


def _gen(text):
    for g in G.LIST_GEN:
        if text.startswith(g + " "):
            return text[len(g) + 1:]
    return text


def list_items(text):
    """Own matcher: the Pāli items (keys) of one list occurrence and the list they belong to."""
    toks = [t for t in G._tokens(text) if not t.startswith("[")]
    for name, items in G.LISTS.items():
        keys = [k.split(" ") for k, _ in items]
        out, i, pos, gap = [], 0, 0, False
        while i < len(toks):
            if toks[i] == "…pe…":
                gap, i = True, i + 1
                continue
            hit = None
            for j in (range(pos, len(keys)) if gap else [pos]):
                if j < len(keys) and toks[i:i + len(keys[j])] == keys[j]:
                    hit = j
                    break
            if hit is None:
                out = None
                break
            out.append(hit)
            i, pos, gap = i + len(keys[hit]), hit + 1, False
        if out and out[0] == 0:
            return name, out
    return None, None


def list_errs(x, y):
    errs, pos, n = [], 0, 0
    for m in LIST_RE.finditer(x):
        text = m["l"] or m["l2"]
        if any(text.startswith(s) for s in NOT_LISTS):
            continue
        text = _gen(text)
        name, idx = list_items(text)
        if not name:
            errs.append("list not matched: " + text[:50])
            continue
        n += 1
        items = G.LISTS[name]
        seen = {}
        for k, v in items:
            if v in seen and seen[v] != k:
                errs.append(f"list {name}: two items share {v}")
            seen[v] = k
        words = [t for t in G._tokens(text) if not t.startswith("[") and t != "…pe…"]
        if sum(len(items[j][0].split(" ")) for j in idx) != len(words):
            errs.append(f"list {name}: count")
        for j in idx:
            k = y.find(items[j][1], pos)
            if k < 0:
                errs.append(f"list {name}: item {items[j][0]} not found in order")
                break
            pos = k + len(items[j][1])
    return errs, n


TERM_RE = re.compile(r"(?:siyā|[Aa]tthi|kati) (?!rūpaṃ|na vattabb)((?:(?!atthi |siyā )[\wāīūṃṅñṭḍṇḷ]+ ?){1,7}?)"
                     r"(?=, |\.|;|…|\?| atthi |$)")


def term_errs(x, y):
    errs = []
    for t in TERM_RE.findall(x):
        t = t.strip().replace("upādinn", "upādiṇṇ")
        try:
            v = F.term_my(t)
        except (F.Miss, KeyError):
            continue
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


def check(pali, my):
    a = [l for l in pathlib.Path(pali).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l for l in pathlib.Path(my).read_text(encoding="utf-8").splitlines() if l.strip()]
    bad = []
    if len(a) != len(b):
        return [f"line count {len(a)} vs {len(b)}"], 0
    lists = 0
    for i, (x, y) in enumerate(zip(a, b)):
        x = F.ID_RE.sub("", x)
        y = F.ID_RE.sub("", y)
        errs = []
        if not x.startswith("#") and sent_count(x) != y.count(F.END):
            errs.append(f"sentences {sent_count(x)}/{y.count(F.END)}")
        if neg(VAR_PI.sub("", x), NEG_PI_RE) != neg(VAR_MY.sub("", y), NEG_MY_RE):
            errs.append(f"negations {neg(VAR_PI.sub('', x), NEG_PI_RE)}/{neg(VAR_MY.sub('', y), NEG_MY_RE)}")
        if nums_pi(VAR_PI.sub("", x)) != nums_my(y):
            errs.append(f"numbers {nums_pi(x)}/{nums_my(y)}")
        va, vb = VAR_PI.findall(x), VAR_MY.findall(y)
        if len(va) != len(vb) or any(t != t2 or F.VAR_KIND.get(t) != k for (t, s), (k, s2, t2) in zip(va, vb)):
            errs.append("variants")
        le, n = list_errs(x, y)
        lists += n
        errs += le + term_errs(x, y) + typo_errs(y)
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


def opening_test():
    """The generator's opening() against every pi-1 opening it parses (pi-1 final Burmese)."""
    n = same = 0
    diffs = []
    for k, vs in G.P1_OPEN.items():
        if not k.startswith("Yasmiṃ samaye "):
            continue
        try:
            got = G.opening(k[len("Yasmiṃ samaye "):])
        except (F.Miss, KeyError):
            continue
        n += 1
        if got in vs:
            same += 1
        else:
            diffs.append(f"opening «{k[14:70]}»: pi-1 «{sorted(vs)[0][:80]}» here «{got[:80]}»")
    return n, same, diffs


if __name__ == "__main__":
    args = sys.argv[1:]
    D = pi1_dict()
    total_bad = 0
    for pali, my in zip(args[::2], args[1::2]):
        bad, lists = check(pali, my)
        n, same, diffs = reuse(pali, my, D)
        name = pathlib.Path(my).name
        print(f"{name}: {len(bad)} mismatches ({lists} definition lists checked); pi-1 reuse {same} / {n} identical")
        for e in bad[:30] + diffs[:20]:
            print("  " + e)
        total_bad += len(bad) + len([d for d in diffs if "pi-1" in d])
    on, osame, odiffs = opening_test()
    print(f"opening test: {osame} / {on} pi-1 openings reproduced")
    for e in odiffs[:10]:
        print("  " + e)
    total_bad += len(odiffs)
    print("OK" if not total_bad else "MISMATCH")
    sys.exit(1 if total_bad else 0)
