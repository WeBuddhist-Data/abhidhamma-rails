"""Per-line check of pi-2 Burmese chapter 18 (Dhammahadayavibhaṅga) against its Pāli, plus the pi-1 reuse test.

usage: python3 -I -X utf8 check_ch18.py <pali_file> <burmese_file>
Adapted from check_sample.py. For every non-empty line (same order) it compares:
  1. sentences  - Pāli sentence ends («.» «?» outside brackets) = Burmese «။»;
  2. negations  - weighted count of Pāli negation morphemes (free na / no / neva / natthi, the privative words and
                  compound members of this chapter, double forms = 2; realm and deva names excluded) against Burmese
                  negation markers («မ» before a verb, «အကုသိုလ်», the abyākata phrase = 1); own tables;
  3. numbers    - every Pāli quantity (number words, compound counts, ×100 / ×1000 / ×10^5 / ×10^7 multipliers,
                  tika / duka, «māso» / «saṃvaccharo» / «kappo» = 1, half, a third) against the Burmese quantities
                  parsed by an independent Burmese number reader (multiset per line);
  4. variants   - every Pāli «[text (sigla) [ref]]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla): text[; ref]]», same text
                  and order;
  5. items      - every list item of the chapter tables (aggregates, bases, elements, truths, faculties, roots,
                  nutriments, contacts, feelings …) named in the Pāli line has its Burmese in the line;
  6. terms      - every «siyā T» / «kati T» of the line: the table value of T occurs in the line;
  7. typography - no «?», «।», «:-», no Latin letters outside the variant brackets, Myanmar only U+1000-U+104F, NFC.
Then the pi-1 REUSE TEST (check_sample.reuse): every Pāli sentence (and heading) that also occurs in pi-1 must have
exactly pi-1's final Burmese sentence (rails text). Prints n / n.
"""
import pathlib
import re
import sys
import unicodedata
from fractions import Fraction

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_sample as CS  # noqa: E402  (pi-1 reuse test, typography)
import make_ch18 as M  # noqa: E402  (tables only)

F = M.F
BR_PI = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)(?: (?P<r>[^\]]+))?\]")
BR_MY = re.compile(r"\[(?P<k>" + F.P1.PATHA + "|" + F.P1.LEKHANA + r") \((?P<s>[^()]+)\): (?P<t>[^\];]+)(?:; (?P<r>[^\]]+))?\]")
L = "A-Za-zāīūṃṅñṭḍṇḷ"

# ------------------------------------------------------------------ negations
NEG_NAMES = r"(?:asaññasatt|avīc|avih|atapp|akaniṭṭh|appamāṇ|appekacc|aparā|avases|appaṃ)\w*"
NEG_PI = [
    (r"nevasaññānāsaññ\w*", 3), (r"nevavipākanavipāk\w*", 2), (r"adukkhamasukh\w*", 2),
    (r"anupādi[nṇ][nṇ]aanupādāniy\w*", 2), (r"avitakkaavicār\w*", 2),
    (r"(?:na|no|neva|natthi|Na|No|Neva|Natthi)(?![" + L + r"])", 1),
]
PRIV = ("apariyāpann anārammaṇ akusal abyākat ahetuk anāhār aphassak avedanak asaññak acetanak acittak alobh ados "
        "amoh avitakk anupādi arūp anāsav asaṅkhat anaññāt napuṃsak").split()
NEG_PI += [(p + r"\w*", 1) for p in PRIV]
NEG_PI_RE = [(re.compile(r"(?<![" + L + r"])" + p, re.I), w) for p, w in NEG_PI]
NEG_PI_RE += [(re.compile(r"ākusal|byākat|ānuppatt|nārammaṇ|āpariyāpann|ākāsānañc|viññāṇañc|ākiñcañ", re.I), 1)]
LETTER, CLOSE = "က-ဪ", "္်"
NEG_MY = [("ကာမ|မနော|မည်သည့်|မဆို|သို့မဟုတ်|မဟာ|ဗြဟ္မ", 0), (re.escape(F.T["abyākatā"].removesuffix("သော")), 1),
          ("အကုသိုလ်", 1), (r"မ(?=[" + LETTER + r"](?!့?[" + CLOSE + r"]))", 1)]
NEG_MY_RE = [(re.compile(p), w) for p, w in NEG_MY]


def neg_pi(s):
    s = re.sub(r"(?<![" + L + r"])" + NEG_NAMES, " ", s, flags=re.I)
    return CS.neg(s, NEG_PI_RE)


def neg_my(s):
    return CS.neg(s, NEG_MY_RE)


# ------------------------------------------------------------------ numbers (Pāli)
PNUM = {"eko": 1, "ekā": 1, "ekaṃ": 1, "dve": 2, "tayo": 3, "tīṇi": 3, "tisso": 3, "cattāro": 4, "cattāri": 4,
        "catasso": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11,
        "dvādasa": 12, "terasa": 13, "cuddasa": 14, "pannarasa": 15, "soḷasa": 16, "aṭṭhārasa": 18, "vīsati": 20,
        "ekavīsa": 21, "aṭṭhavīsa": 28, "tiṃsa": 30, "bāttiṃsa": 32, "cattārīsa": 40, "paññāsa": 50,
        "sattapaññāsa": 57, "saṭṭhi": 60, "catusaṭṭhi": 64, "caturāsīti": 84, "navuti": 90,
        "pañcannaṃ": 5, "sattannaṃ": 7, "dvādasannaṃ": 12, "aṭṭhārasannaṃ": 18, "catunnaṃ": 4}
PSTEM = {"eka": 1, "ek": 1, "dv": 2, "tīṇ": 3, "cattār": 4, "pañc": 5, "cha": 6, "satt": 7, "aṭṭh": 8, "nav": 9, "das": 10,
         "ekādas": 11, "dvādas": 12, "teras": 13, "cuddas": 14, "bāvīsat": 22, "tiṃsa": 30, "dvādasa": 12,
         "pañca": 5}
PCOMP = re.compile(r"(?P<n>" + "|".join(sorted(PSTEM, key=len, reverse=True)) + r")(?:kkhandh|āyatan|indriy|"
                   r"māsiy|ratti|kappasat|saṅkhāt)\w*")
PMULT = [(r"vassakoṭisat\w*|koṭisat\w*", 10 ** 9), (r"vassakoṭ\w*|koṭiy\w*", 10 ** 7),
         (r"vassasatasahass\w*|satasahass\w*", 10 ** 5), (r"vassasahass\w*|kappasahass\w*", 1000),
         (r"vassasat\w*", 100)]
PMULT = [(re.compile(p), v) for p, v in PMULT]
PONE = {"māso", "saṃvaccharo", "kappo", "tikaṃ", "dukaṃ"}


def nums_pi(s):
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = s.replace("Kappassa tatiyo bhāgo", " §third§ ").replace("Upaḍḍhakappo", " §half§ ")
    words = re.findall(r"[" + L + r"§]+", s)
    out, i = [], 0
    while i < len(words):
        w = words[i].lower()
        if w not in PNUM and w.endswith("ñca") and w[:-3] in PNUM:      # cuddasañca = cuddasa + ca
            w = w[:-3]
        if w == "§third§":
            out.append(Fraction(1, 3))
        elif w == "§half§":
            out.append(Fraction(1, 2))
        elif w in PNUM or PCOMP.fullmatch(w):
            n = PNUM.get(w)
            if n is None:
                cm = PCOMP.fullmatch(w)
                n = PSTEM[cm["n"]] * (100 if "kappasat" in w else 1)
            j = i + 1
            if j < len(words) and words[j] == "ca":
                j += 1
            mult = 1
            if j < len(words):
                for rx, v in PMULT:
                    if rx.fullmatch(words[j].lower()):
                        mult, i = v, j
                        break
            out.append(Fraction(n * mult))
        elif w.endswith(("ttikaṃ", "tikaṃ")) or w in ("tikādidassanavāro",):
            out.append(Fraction(3))
        elif w.endswith("dukaṃ"):
            out.append(Fraction(2))
        elif w in PONE:
            out.append(Fraction(1))
        else:
            for rx, v in PMULT:
                if rx.fullmatch(w):
                    out.append(Fraction(v))
                    break
        i += 1
    return sorted(out)


# ------------------------------------------------------------------ numbers (Burmese)
U = "(?:တစ်|နှစ်|သုံး|လေး|ငါး|ခြောက်|ခုနစ်|ရှစ်|ကိုး)"
UV = {"တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6, "ခုနစ်": 7, "ရှစ်": 8, "ကိုး": 9}
BNUM = re.compile(r"(?:(?P<k>" + U + r")သောင်း)?(?:(?P<t>" + U + r")(?:ထောင့်|ထောင်))?(?:(?P<h>" + U + r")ရာ့?)?"
                  r"(?:(?P<d>" + U + r")?(?P<ds>ဆယ့်|ဆယ်))?(?P<u>" + U + r")?")
SUFFIX = ("ပါး", "မျိုး", "ကမ္ဘာ", "လ", "နှစ်", "ရက်", "ပေါင်းတည်း")
PARTICLE = ("", "သည်", "၏", "နှင့်")
BMULT = {"သိန်း": 10 ** 5, "ကုဋေ": 10 ** 7}


def bnum(tok):
    """Burmese token -> value or None."""
    if tok == "သုံးပုံတစ်ပုံ":
        return Fraction(1, 3)
    if tok == "တစ်ဝက်":
        return Fraction(1, 2)
    for end in range(len(tok), 0, -1):
        m = BNUM.fullmatch(tok[:end])
        if not m or not m[0]:
            continue
        rest = tok[end:]
        if rest in PARTICLE or rest.startswith(SUFFIX):
            v = sum(UV[m[g]] * f for g, f in (("k", 10000), ("t", 1000), ("h", 100)) if m[g])
            if m["ds"]:
                v += (UV[m["d"]] if m["d"] else 1) * 10
            if m["u"]:
                v += UV[m["u"]]
            return Fraction(v)
    return None


def nums_my(s):
    s = re.sub(r"\[[^\]]*\]", " ", s)
    toks = [t for t in re.split(r"[ ၊။–…“”]+", s) if t]
    out, mult = [], 1
    for t in toks:
        if t in BMULT:
            mult = BMULT[t]
            continue
        if t == "နှစ်":                          # «နှစ်» alone = year
            continue
        v = bnum(t)
        if v is not None:
            out.append(v * mult)
        mult = 1
    return sorted(out)


# ------------------------------------------------------------------ variants
def var_errs(x, y):
    va, vb = BR_PI.findall(x), BR_MY.findall(y)
    if len(va) != len(vb) or x.count("[") != y.count("["):
        return ["variant count"]
    errs = []
    for (t, s, r), (k, s2, t2, r2) in zip(va, vb):
        if t != t2 or M.VAR.get(t) != k or s2 != ", ".join(M.SIGLA[z] for z in s.split()) or (M.REF.get(r) if r else "") != r2:
            errs.append("variant " + t)
    return errs


# ------------------------------------------------------------------ items and terms
AMBIG = {"rūpā", "saddā", "gandhā", "rasā", "phoṭṭhabbā"}        # objects / predicates (rūpā = material)
ITEM_KEYS = sorted((k for k in M.ITEMS if k not in AMBIG), key=len, reverse=True)
ITEM_RX = [(k, re.compile(r"(?<![" + L + r"])[" + k[0].upper() + k[0] + "]" + re.escape(k[1:]) + r"(?![" + L + r"])"))
           for k in ITEM_KEYS]


def item_errs(x, y):
    errs, s = [], x
    for k, rx in ITEM_RX:
        if rx.search(s):
            if M.ITEMS[k] not in y:
                errs.append("item " + k)
            s = rx.sub(" ", s)
    return errs


TERM_RE = re.compile(r"(?:siyā|kati) (?!na vattabb)((?:(?!siyā |kati )[" + L + r"]+ ?){1,3}?)(?=, |\.|;|…|\?|$| siyā)")


def term_errs(x, y):
    errs = []
    for t in TERM_RE.findall(x):
        t = t.strip()
        if t in M.KATI_NOUN:
            continue                                  # «kati khandhā»: a noun, checked as an item
        try:
            v = M.chain_my(t.split(" "))
        except M.Miss:
            continue                                  # nouns after «kati» (kati khandhā) are checked as items
        if v not in y:
            errs.append("term " + t)
    return errs


def sent_count(x):
    x = re.sub(r"\[[^\]]*\]", "", x).replace("…pe…", "…").replace("…Pe…", "…")
    return len(re.findall(r"[.?](?=\"|”|\)|\s|$)", x))


SLIPS = [("siyā dukkhamasukhāya", "siyā adukkhamasukhāya")]      # read as intended (logged in notes-ch18.md)


def check(pali, my):
    a = [l for l in pathlib.Path(pali).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l for l in pathlib.Path(my).read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(a) != len(b):
        return [f"line count {len(a)} vs {len(b)}"]
    bad = []
    for i, (x, y) in enumerate(zip(a, b)):
        x, y = F.ID_RE.sub("", x), F.ID_RE.sub("", y)
        for p, q in SLIPS:
            x = x.replace(p, q)
        errs = []
        if not x.startswith("#") and sent_count(x) != y.count(F.END):
            errs.append(f"sentences {sent_count(x)}/{y.count(F.END)}")
        nx, ny = neg_pi(re.sub(r"\[[^\]]*\]", "", x)), neg_my(re.sub(r"\[[^\]]*\]", "", y))
        if nx != ny:
            errs.append(f"negations {nx}/{ny}")
        px, py = nums_pi(x), nums_my(y)
        if px != py:
            errs.append(f"numbers {[str(v) for v in px]}/{[str(v) for v in py]}")
        errs += var_errs(x, y) + ([] if x.startswith("#") else item_errs(x, y)) + term_errs(x, y) + CS.typo_errs(re.sub(r"\[[^\]]*\]", "", y))
        if errs:
            bad.append(f"line {i + 1}: " + "; ".join(errs))
    return bad


if __name__ == "__main__":
    pali, my = sys.argv[1:3]
    bad = check(pali, my)
    D = CS.pi1_dict()
    n, same, diffs = CS.reuse(pali, my, D)
    print(f"{pathlib.Path(my).name}: {len(bad)} mismatches; pi-1 reuse {same} / {n} identical")
    for e in bad[:40] + diffs[:20]:
        print("  " + e)
    ok = not bad and not [d for d in diffs if "pi-1" in d]
    print("OK" if ok else "MISMATCH")
    sys.exit(0 if ok else 1)
