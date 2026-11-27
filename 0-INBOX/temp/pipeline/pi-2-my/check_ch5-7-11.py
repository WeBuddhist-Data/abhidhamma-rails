"""Per-line check of the pi-2 Burmese chapters 5, 7-11 against their Pāli, plus the pi-1 reuse test.

usage: python3 -I -X utf8 check_ch5-7-11.py [<pali_file> <burmese_file> ...]   (no arguments: the six chapters)
Adapted from check_sample.py (approved sample). For every non-empty line (same order) it compares:
  1. sentences  - Pāli sentence ends («.» «?» outside square brackets) = Burmese «။»;
  2. negations  - weighted count of Pāli negation morphemes (free na / no / neva / natthi, the privative a- / an- /
                  nir- words of PRIV, double forms = 2) against Burmese negation markers («မ» before a verb,
                  «အကုသိုလ်», the abyākata phrase = 1); own tables, independent of the generator;
  3. numbers    - Pāli number words (vidhena, indriya counts, cattāro / satta / tayo / cha / pañca, tika / duka …)
                  against Burmese number words before «မျိုး / ပါး»;
  4. variants   - every Pāli «[text (sigla) …]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla): text …]», same text, order;
  5. lists      - every definition list «Yo / Yā / Yaṃ [tasmiṃ samaye] [head] ITEMS –»: the Burmese of each item
                  (the generator's pi-1 / new list table) occurs, in order; two different Pāli items of one list
                  never share a Burmese item;
  6. terms      - every «siyā T» / «atthi T» / «kati T» of the line: the table value of T occurs in the line;
  7. typography - no «?», «।», «:-», no Latin letters outside the variant brackets, Myanmar only U+1000-U+104F, NFC,
                  no double spaces.
Then: CONSISTENCY - the same Pāli sentence gets the same Burmese sentence everywhere in the six chapters and in the
approved sample chapter 1-khandhavibhango; and the pi-1 REUSE TEST: every Pāli sentence (and heading) that also
occurs in pi-1 must have exactly pi-1's final Burmese sentence (rails text). Prints n / n.
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location("make_ch5_7_11", HERE / "make_ch5-7-11.py")
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)                   # tables only (writes nothing at import)
F = G.F
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"

WB = r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])"
WE = r"(?![A-Za-zāīūṃṅñṭḍṇḷ])"
VAR_PI = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)(?: [^\]]+)?\]")
VAR_MY = re.compile(r"\[(?P<k>" + F.P1.PATHA + "|" + F.P1.LEKHANA + r") \((?P<s>[^()]+)\): (?P<t>[^\]၊]+)(?:၊ [^\]]+)?\]")
BR = re.compile(r"\[[^\]]*\]")

# ------------------------------------------------------------------ negations
NEG_PI = [
    (r"nevavipākanavipāk\w*", 2), (r"nevācayagāmināpacay\w*", 2), (r"nevasekkhanāsekkh\w*", 2),
    (r"adukkhamasukh\w*", 2), (r"anupādi[nṇ][nṇ]aanupādāniy\w*", 2), (r"asaṃkiliṭṭhaasaṃkilesik\w*", 2),
    (r"avitakkaavicār\w*", 2), (r"anidassanaappaṭigh\w*", 2), (r"neva dassanena na bhāvanāya", 2),
    (r"neva sātaṃ nāsātaṃ", 3),                                   # neva sātaṃ + na asātaṃ
    (r"\w+vippayuttaa\w+", 1),
    (r"(?:na|no|neva|Na|No|Neva|natthi|natthissa)" + WE, 1),
]
PRIV = ("anupādi asaṃkiliṭṭh asaṃkilesik avitakk avicār appamāṇ aniyat anuppann anidassan appaṭigh "
        "ahetuk appaccay asaṅkhat arūp anāsav asaṃyojaniy aganthaniy anoghaniy ayoganiy anīvaraṇiy aparāmaṭṭh "
        "anārammaṇ acetasik cittavisaṃsaṭṭh anupādāniy appītik apariyāpann aniyyānik anuttar araṇ "
        "asāt "
        # pi-2 chapters 5, 7-11
        "anaññātaññassāmīt anaññāt adiṭṭh appatt avidit asacchikat asithil anikkhitt apilāpan asammussan "
        "avisāh avikkhep amoh alobh ados asucin asant amahaggat asamāhit avimutt anuppād asammos asallīn "
        "abyāpād avihiṃs adinn akiriy akaraṇ anajjhāpatt nirāmis").split()
NEG_PI += [(p + r"\w*", 1) for p in PRIV]
NEG_PI_RE = [(re.compile(WB + p, re.I), w) for p, w in NEG_PI]
NEG_PI_RE += [(re.compile(r"[aā]kusal|byākat|anatikkam|hetuahetuk|(?<!citta)visaṃsaṭṭh", re.I), 1)]
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
          (r"bāvīsat\w*", 22), (r"ekavīsatindriy\w*", 21), (r"aṭṭhārasindriy\w*", 18), (r"sattarasindriy\w*", 17),
          (r"soḷasindriy\w*", 16), (r"pannarasindriy\w*", 15), (r"cuddasindriy\w*", 14), (r"terasindriy\w*", 13),
          (r"dvādasindriy\w*", 12), (r"ekādasindriy\w*", 11), (r"dasindriy\w*", 10), (r"navindriy\w*", 9),
          (r"aṭṭhindriy\w*", 8), (r"sattindriy\w*", 7), (r"pañcindriy\w*", 5), (r"cattārindriy\w*", 4),
          (r"tīṇindriy\w*", 3), (r"dvindriy\w*", 2), (r"tīṇi", 3),
          (r"cattāro|catunnaṃ|catūhi|catunnañca", 4), (r"tayo|tīhi", 3), (r"dve", 2), (r"cha", 6),
          (r"satta|sattannaṃ|sattahi", 7), (r"pañca|pañcapi", 5), (r"aṭṭhaṅgik\w*|aṭṭhannaṃ", 8),
          (r"pañcaṅgik\w*", 5), (r"tikaṃ", 3), (r"dukaṃ", 2)]
NUM_PI_RE = [(re.compile(p, re.I), v) for p, v in NUM_PI]
NUM_MY = {"နှစ်ဆယ့်နှစ်": 22, "နှစ်ဆယ့်တစ်": 21, "ဆယ့်ရှစ်": 18, "ဆယ့်ခုနစ်": 17, "ဆယ့်ခြောက်": 16, "ဆယ့်ငါး": 15,
          "ဆယ့်လေး": 14, "ဆယ့်သုံး": 13, "ဆယ့်နှစ်": 12, "ဆယ့်တစ်": 11, "ဆယ်": 10, "ကိုး": 9, "ရှစ်": 8,
          "ခုနစ်": 7, "ခြောက်": 6, "ငါး": 5, "လေး": 4, "သုံး": 3, "နှစ်": 2, "တစ်": 1}
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
    return sorted(NUM_MY[m] for m in NUM_MY_RE.findall(s.replace("အမျိုးမျိုး", "")))


# ------------------------------------------------------------------ lists
LIST_PI = re.compile(r"(?:^|(?<=[ ?.,]))(?:Yo|Yā|Yaṃ|yo|yā|yaṃ)(?: tasmiṃ samaye)? (?:(?P<h>" + G.esc_alt(G.LHEAD)
                     + r") )?(?P<l>[^–]+?)(?= – |\.$)")


def list_errs(x, y):
    errs, pos, n = [], 0, 0
    for m in LIST_PI.finditer(x):
        toks = re.findall(r"\[[^\]]*\]|…pe…|[^\s\[…]+", m["l"])
        if not toks or not any(k == toks[0] or k.startswith(toks[0] + " ") for k in G.SYN2) or \
                {"so", "sā", "hoti"} & set(toks):
            continue                              # not a synonym list («Yā ṭhiti so asammoso …», «yo … phasso hoti»)
        keys, i = [], 0
        while i < len(toks):
            if toks[i].startswith("[") or toks[i] == "…pe…":
                i += 1
                continue
            for k in range(G.SYN_MAX, 0, -1):
                ws = toks[i:i + k]
                if len(ws) == k and " ".join(ws) in G.SYN2:
                    keys.append(" ".join(ws))
                    i += k
                    break
            else:
                errs.append("list word " + toks[i])
                break
        n += 1
        seen = {}
        for k in keys:
            v = G.SYN2[k]
            if v in seen and seen[v] != k:
                errs.append(f"two items share {v}")
            seen[v] = k
            j = y.find(v, pos)
            if j < 0:
                errs.append(f"list item {k} not found in order")
            else:
                pos = j + len(v)
        if m["h"] and G.LHEAD[m["h"]].strip() not in y:
            errs.append("list head " + m["h"])
    return errs, n


TERM_RE = re.compile(r"(?:siyā|[Aa]tthi|kati) (?!rūpaṃ|na vattabb)((?:(?!atthi |siyā )[\wāīūṃṅñṭḍṇḷ]+ ?){1,7}?)"
                     r"(?=, |\.|;|…|\?| atthi | siyā |$)")


def term_errs(x, y):
    errs = []
    for t in TERM_RE.findall(x):
        t = t.strip().replace("upādinn", "upādiṇṇ")
        try:
            v = F.term_my(t)
        except F.Miss:
            continue                               # not a mātikā term (atthi ajjhattaṃ dhammesu sati …)
        if v not in y:
            errs.append("term " + t)
    return errs


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
    if "  " in y:
        errs.append("double space")
    return errs


def sent_count(x):
    x = BR.sub("", x).replace("…pe…", "…").replace("…Pe…", "…")
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
        npi, nmy = neg(BR.sub("", x), NEG_PI_RE), neg(VAR_MY.sub("", y), NEG_MY_RE)
        if npi != nmy:
            errs.append(f"negations {npi}/{nmy}")
        if nums_pi(BR.sub("", x)) != nums_my(y):
            errs.append(f"numbers {nums_pi(BR.sub('', x))}/{nums_my(y)}")
        va, vb = VAR_PI.findall(x), VAR_MY.findall(y)
        if x.count("[") != len(va) or len(va) != len(vb) or any(t != t2 for (t, s), (k, s2, t2) in zip(va, vb)):
            errs.append("variants")
        le, n = list_errs(x.replace("upādinn", "upādiṇṇ"), y)
        lists += n
        errs += le + term_errs(x, y) + typo_errs(y)
        if errs:
            bad.append(f"line {i + 1}: " + "; ".join(errs))
    return bad, lists


# ------------------------------------------------------------------ consistency, pi-1 reuse
def psplit(l):
    l = F.ID_RE.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def bsplit(l):
    return [s for s in re.split(r"(?<=။) ", F.ID_RE.sub("", l)) if s]


def pairs_of(pali, my):
    a = [l for l in pathlib.Path(pali).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l for l in pathlib.Path(my).read_text(encoding="utf-8").splitlines() if l.strip()]
    out, bad = [], []
    for i, (x, y) in enumerate(zip(a, b)):
        if x.startswith("#"):
            out.append((i, F.ID_RE.sub("", x).split(" ", 1)[1], F.ID_RE.sub("", y).split(" ", 1)[1]))
            continue
        ps, bs = psplit(x), bsplit(y)
        if len(ps) != len(bs):
            bad.append(f"line {i + 1}: sentence split {len(ps)}/{len(bs)}")
            continue
        out += [(i, s, t) for s, t in zip(ps, bs)]
    return out, bad


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


def reuse(prs, D):
    n = same = 0
    diffs = []
    for i, s, t in prs:
        k = s.replace("upādinn", "upādiṇṇ")
        if k in D:
            n += 1
            if t in D[k]:
                same += 1
            else:
                diffs.append(f"line {i + 1}: «{s[:60]}» pi-1 «{sorted(D[k])[0][:60]}» here «{t[:60]}»")
    return n, same, diffs


if __name__ == "__main__":
    args = sys.argv[1:] or [str(p) for c in G.CHAPTERS for p in (PALI / c, OUT / c)]
    D = pi1_dict()
    total_bad, tn, ts = 0, 0, 0
    SEEN, SAMPLE = {}, {}                        # Pāli sentence -> {Burmese: where}
    for pali, my in [(PALI / "1-khandhavibhango.md", OUT / "1-khandhavibhango.md")] + list(zip(args[::2], args[1::2])):
        prs, sbad = pairs_of(pali, my)
        is_sample = pathlib.Path(my).name == "1-khandhavibhango.md"
        for i, s, t in prs:
            (SAMPLE if is_sample else SEEN).setdefault(s, {}).setdefault(t, f"{pathlib.Path(my).name}:{i + 1}")
        if is_sample:
            continue                             # the approved sample: consistency reference only
        bad, lists = check(pali, my)
        n, same, diffs = reuse(prs, D)
        tn, ts = tn + n, ts + same
        name = pathlib.Path(my).name
        print(f"{name}: {len(bad) + len(sbad)} mismatches ({lists} definition lists checked); "
              f"pi-1 reuse {same} / {n} identical")
        for e in bad[:20] + sbad[:10] + diffs[:20]:
            print("  " + e)
        total_bad += len(bad) + len(sbad) + len(diffs)
    for s, v in SEEN.items():                    # against the sample where the sample has one rendering only
        if s in SAMPLE and len(SAMPLE[s]) == 1:
            for t, w in SAMPLE[s].items():
                v.setdefault(t, w)
    incons = {s: v for s, v in SEEN.items() if len(v) > 1}
    print(f"consistency: {len(incons)} Pāli sentences with more than one Burmese rendering")
    for s, v in list(incons.items())[:15]:
        print(f"  «{s[:70]}»: " + " | ".join(f"{w}: {t[:50]}" for t, w in v.items()))
    total_bad += len(incons)
    print(f"pi-1 reuse total {ts} / {tn}")
    print("OK" if not total_bad else "MISMATCH")
    sys.exit(1 if total_bad else 0)
