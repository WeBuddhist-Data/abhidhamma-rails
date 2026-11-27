"""Per-line check of the pi-1 Burmese Nikkhepakaṇḍa chapters (4-01 … 4-03) against the Pāli (adapted from check_ch2-01.py).

usage: python3 -I -X utf8 check_ch4.py <pali_file> <burmese_file> [...pairs]
The tables (Mātikā TERMS, synonyms, names, phrases) are read from my_formulas / make_ch4 (make_ch4.build() only installs
them in memory; nothing is written). The line-by-line comparison is independent of the clause engine:
  1. block ids  - same id at the end of the same line;
  2. negations  - weighted Pāli negation morphemes (free na / no / neva / natthi; privative a- / an- stems of PRIV;
                  fixed double forms; abyākata = 3, as its Burmese phrase has three negation marks) against Burmese
                  negation marks («မ» + an unclosed letter, «အကုသိုလ်»); «ကာမ», «မနော» are not negations;
  3. numbers    - Pāli number words (tīṇi, cattāro, dasa, aṭṭhārasa, saḷāyatana, tadubhaya …) against Burmese number +
                  classifier;
  4. variants   - every «[text (sigla)]» -> «[ပါဌ်ကွဲ | စာလုံးပေါင်းကွဲ (Sigla): text]», label as VAR_KIND; same «[» count;
  5. frames     - counts per line: questions (Katame dhammā / Tattha katam-) = «ဟူသည် အဘယ်(တို့)နည်း»; closers «ime
                  dhammā» = «ဤသဘောတရားများသည်»; «ime tayo / nava / cha …» = «ဤသည်တို့မှာ»; «vuccati» = «ဟု ခေါ်သည်»;
                  «ṭhapetvā» = «ချန်ထား၍»; «.» + «?» = «။»;
  6. Mātikā     - the Burmese of every «Katame dhammā X?» (X from the Mātikā tables) and of every closer «ime dhammā X»
                  (its predicate form) and every «Tattha katamo X? … vuccati X» definiendum must stand in the line;
  7. lists      - every synonym list (after «Yo / Yā / Yaṃ [head]» up to « – ») is re-tokenised by an own longest-match
                  scanner: same items, same order, same count in the Burmese, two different Pāli items never share one
                  Burmese value;
  8. phrases    - the rest of the line (frames and lists removed) is scanned for table words / phrases; their Burmese must
                  occur in the line in the same order;
  9. typography - no «?», «।», «:-», no Latin outside brackets, NFC, Myanmar code points U+1000-U+104F only, a line
                  ending in «.» / «?» ends in «။».
Prints OK or the mismatching lines; exit 1 on any mismatch.
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my_formulas as F  # noqa: E402
import make_ch4 as M  # noqa: E402

M.build()

L = "A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ"
W = f"[{L}]"
WB = rf"(?<![{L}])"
WE = rf"(?![{L}])"
# ------------------------------------------------------------------ negations (Pāli)
NEG_PI = [
    (r"nevavipākanavipāk", 2), (r"nevācayagāmināpacay", 2), (r"nevasekkhanāsekkh", 2), (r"adukkhamasukh", 2),
    (r"anupādiṇṇaanupādāniy", 2), (r"asaṃkiliṭṭhaasaṃkilesik", 2), (r"avitakkaavicār", 2),
    (r"anidassanaappaṭigh", 2),
    (r"[aā]byākat", 3),                       # abyākata = «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်»
    (r"nākusal", 2),                          # na + akusala
    (r"[aā]kusal(?!atā)", 1),                        # akusala, also inside kusalākusala
    (r"nānubyañjan", 1),                      # na + anubyañjana
    (r"visaṃsaṭṭh", 1),
]
PRIV = (
    # sample and 2-01
    "anupādiṇṇ asaṃkiliṭṭh asaṃkilesik avitakk avicār appamāṇ aniyat anuppann anidassan appaṭigh ahetuk appaccay "
    "asaṅkhat arūp anāsav asaṃyojaniy aganthaniy anoghaniy ayoganiy anīvaraṇiy aparāmaṭṭh anārammaṇ acetasik "
    "anupādāniy appītik apariyāpann aniyyānik anuttar araṇ avijj atapanīy ahirik ahirīk anottapp dovacass "
    "aguttadvār amattaññ asampajañ asantuṭṭh appaṭivān anuppād anantavā aṭṭhān avikkhep "
    "alobh ados amoh anabhijjh abyāpād abyāpajj alubbh asārāg asārajj adussan adussit adūs asithil anikkhitt "
    "apilāpan asammussan asammusan avisāh adandhan avitthan akakkhaḷ akathin ajimh avaṅk akuṭil "
    # Nikkhepa (4-01 … 4-03)
    "assutav adassāv akovid avinīt aññāṇ adassan anabhisamay ananubodh asambodh appaṭivedh asaṃgāhan "
    "apariyogāhan asamapekkhan apaccavekkhaṇ apaccakkh adhammarāg anattaman anatth appiy amanāp anekaṃs avipakk ajāt "
    "abhūt asañjāt anibbatt anabhinibbatt apātubhūt asamuppann anuṭṭhit asamuṭṭhit akallat akammaññ avūpasam "
    "akappiy avajj asaṃvut appaṭisaṅkh ayonis anavajj asati ananussat appaṭissat asaraṇ adhāraṇ anādar agārav "
    "appaṭissav appaṭikūl avipaccanīk assaddh asamādhi apharus agutt agopan anārakkh asaṃvar avītikkam acaṇḍikk "
    "anasurop asammos aṭṭhit anolīn asassat").split()
# the immaterial realm names (consistency pass: the shared my_formulas.JH_ARUPA_BASE strings, as check_ch2-02-03):
# ākāsānañca- / viññāṇañca- (an-anta) = 1, ākiñcañña- = 1, nevasaññānāsañña- = 3
NEG_PI = [(r"(?:ākāsānañc|viññāṇañc|ākiñcaññ)āyatan\w*", 1), (r"nevasaññānāsaññ\w*", 3)] + list(NEG_PI)
NEG_PI_RE = [(re.compile(p, re.I), w) for p, w in NEG_PI]
NEG_PI_RE += [(re.compile(WB + p + W + "*", re.I), 1) for p in PRIV]
NEG_PI_RE += [(re.compile(WB + r"(?:na|no|neva|natthi)" + WE, re.I), 1)]
# ------------------------------------------------------------------ negations (Burmese)
LETTER = "က-ဪ"
NOT_NEG = ["ကာမ", "မနော", "တမလွန်"]
NEG_MY_RE = [(re.compile("|".join(NOT_NEG)), 0), (re.compile("အကုသိုလ်"), 1),
             (re.compile(r"မ(?=[" + LETTER + r"](?!့?[္်]))"), 1)]


def neg_count(s, table, fill=" "):
    """Weighted count; each match is replaced by «fill» so that it is not counted twice («x» for Pāli keeps the
    word boundary: the rest of a compound is not taken for a new word)."""
    n = 0
    for rx, w in table:
        n += len(rx.findall(s)) * w
        s = rx.sub(fill, s)
    return n


# ------------------------------------------------------------------ numbers
NUM_PI = [(r"tika\w*", 3), (r"\w*duka\w*", 2), (r"eko|ekā|ekaṃ", 1), (r"dvādas\w*", 12), (r"dve|dvi\w*", 2),
          (r"tadubhay\w*", 2), (r"tayo|tīṇi|tīsu|tisso", 3), (r"cattāro|cattāri|catunnañca", 4),
          (r"pañca|pañcapi|pañcakkhandh\w*", 5), (r"cha|channaṃ|saḷāyatan\w*", 6), (r"satta|sattapi", 7),
          (r"aṭṭha", 8), (r"nava", 9), (r"dasa", 10), (r"aṭṭhārasa", 18)]
NUM_PI_RE = [(re.compile(p, re.I), v) for p, v in NUM_PI]
NUM_MY = {"ဆယ့်နှစ်": 12, "ဆယ့်ရှစ်": 18, "တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6,
          "ခုနစ်": 7, "ရှစ်": 8, "ကိုး": 9, "ဆယ်": 10}
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
    return sorted(out)


def nums_my(s):
    for i in NUM_IDIOM:
        s = s.replace(i, " ")
    return sorted(NUM_MY[m] for m in NUM_MY_RE.findall(s))


# ------------------------------------------------------------------ variants
VAR_PI = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)\]")
VAR_MY = re.compile(r"\[(?P<k>" + F.PATHA + "|" + F.LEKHANA + r") \((?P<s>[^()]+)\): (?P<t>[^\]]+)\]")


def var_check(x, y):
    if x.count("[") != y.count("["):
        return ["variant count"]
    for br, my in M.MULTI_VAR.items():
        if br in x:
            if my not in y:
                return ["multi variant"]
            x, y = x.replace(br, " "), y.replace(my, " ")
    a, b = VAR_PI.findall(x), VAR_MY.findall(y)
    if len(a) != len(b):
        return ["variant count"]
    errs = []
    for (t, s), (k, s2, t2) in zip(a, b):
        if t != t2:
            errs.append(f"variant text {t2}")
        if F.VAR_KIND.get(t) != k:
            errs.append(f"variant label {k} for {t}")
        if s2 != ", ".join(F.SIGLA[z] for z in s.split()):
            errs.append(f"sigla {s2}")
    return errs


# ------------------------------------------------------------------ frames (counts)
def frames(x, y):
    errs = []
    pairs = [
        (r"Katame dhammā|Tattha katam(?:o|ā|aṃ|e)" + WE, r"ဟူသည် အဘယ်(?:တို့)?နည်း", "question"),
        (r"[Ii]me dhammā", re.escape(M.IME_PL), "closer"),
        (r"[Ii]me (?:tayo|nava|cha) ", r"ဤသည်တို့မှာ", "ime N"),
        (r"vuccati", r"ဟု ခေါ်သည်", "vuccati"),
        (r"[Ṭṭ]hapetvā", re.escape(F.THAPETVA), "ṭhapetvā"),
    ]
    for p, m, name in pairs:
        a, b = len(re.findall(p, x)), len(re.findall(m, y))
        if a != b:
            errs.append(f"{name} {a} vs {b}")
    ends_x = len(re.findall(r"[.?]", re.sub(r"\[[^\]]*\]", "", x)))
    if ends_x != y.count(F.END):
        errs.append(f"sentence ends {ends_x} vs {y.count(F.END)}")
    return errs


# ------------------------------------------------------------------ Mātikā items, definienda
QT = sorted(set(M.ALLQ) | set(M.CLOSE_EXTRA), key=len, reverse=True)
QT_ALT = "|".join(re.escape(k) for k in QT)
DEF_ALT = "|".join(re.escape(k) for k in sorted(M.DEF, key=len, reverse=True))
KATAME_RE = re.compile(rf"Katame dhammā ({QT_ALT})\?")
IME_RE = re.compile(rf"[Ii]me dhammā ({QT_ALT})(?=[.?]|$)")
TATTHA_RE = re.compile(rf"Tattha katam(?:o|ā|aṃ|e) ([Tt]?{DEF_ALT})(?=\?|…pe…)")
VUCC_RE = re.compile(rf"(?:ayaṃ|idaṃ) vuccati ({DEF_ALT})(?![{L}])")


def matika(x, y):
    errs = []
    for k in KATAME_RE.findall(x):
        exp = f"{M.ALLQ[k]} {F.DHAMMA_PL} {F.CU_Q['pl']}"
        if exp not in y:
            errs.append(f"question «{k}»")
    for k in IME_RE.findall(x):
        # consistency pass: the closer keeps the approved Mātikā string + «သဘောတရားများ ဖြစ်ကြသည်» (as 2-04 / 2-05 / 5);
        # kusalā / akusalā take the model's noun predicate; the non-Mātikā CLOSE_EXTRA items keep their predicate form
        if k == "kusalā":
            exp = F.IME_KUSALA
        elif k == "akusalā":
            exp = f"{M.IME_PL} {F.TERMS[k]} {F.CU_COP['pl']}"
        elif k in M.CLOSE_EXTRA:
            exp = f"{M.IME_PL} {M.pred(M.CLOSE_EXTRA[k])}"
        else:
            exp = f"{M.IME_PL} {M.ALLQ[k]} {F.DHAMMA_PL} {F.CU_COP['pl']}"
        if exp not in y:
            errs.append(f"closer «{k}»")
    for k in TATTHA_RE.findall(x):
        k = k[0].lower() + k[1:]
        if f"{M.TATTHA} {M.DEF[k]} ဟူသည်" not in y:
            errs.append(f"Tattha «{k}»")
    for k in VUCC_RE.findall(x):
        if M.VUCC.format(M.DEF[k]) not in y:
            errs.append(f"vuccati «{k}»")
    return errs


# ------------------------------------------------------------------ lists and phrases (own scanner)
SCAN = {}
for d in (F.NAMES, F.SYN, M.PH):
    for k, v in d.items():
        if v is not None:
            SCAN.setdefault(k, v)
MAXW = max(len(k.split()) for k in SCAN)
GEN_ALT = "|".join(re.escape(k) for k in sorted(F.GEN, key=len, reverse=True))
LIST_RE = re.compile(rf"(?:^|(?<=[ ]))(?:[Yy]o|[Yy]ā|[Yy]aṃ)(?: (?:{GEN_ALT}))? ([^;–]+?)(?= – |\.$)")
YE_RE = re.compile(r"Ye dhammā (?:tesaṃ tesaṃ (?:sattānaṃ|parasattānaṃ parapuggalānaṃ) )?([^,]+?)(?=, )")
FRAME_STRIP = [KATAME_RE, IME_RE, TATTHA_RE, VUCC_RE, re.compile(M.SAMANA_RE),
               re.compile(r"(?:Ye te|ye vā pana te) dhammā \w+viññeyyā,? na te dhammā \w+viññeyyā"),
               re.compile(r"Tehi dhammehi ye dhammā (?:na hetū )?\w+"),
               re.compile(r"\S+ dhamme ārabbha ye uppajjanti cittacetasikā dhammā"),
               re.compile(r"(?:Teyeva|Teva|Tāneva|Sveva) .+?(?=[.]|$)"),
               re.compile(r"te aññamaññaṃ hetū ceva \w+ ca"),
               re.compile(r"\S+ (?:\S+ )?\S+ (?:hetu|āsavo|gantho|kileso) ceva \S+ ca|\S+ (?:\S+ )?\S+ \w+ñceva \w+ñca"),
               re.compile(r"\S+ (?:\S+ )?\S+ kileso ceva \S+"),
               re.compile(r"(?:[Tt]ayo|[Nn]ava|[Cc]ha) \w+hetū|[Ii]me (?:tayo|nava|cha) \w+hetū"),
               re.compile(r"(?:Ṭhapetvā .+? )?[Ss]abb\w+ .+?(?=[.]|$)"),
               re.compile(r"Sattapi bojjhaṅgā \w+")]


def toks(s):
    """Words of a Pāli string; a variant bracket and «…pe…» become a barrier «¦» that no table key spans."""
    return re.findall(r"[^\s,;?.\[\]…–ः’‘]+(?:’ti)?|‘[^\s,]+", re.sub(r"\[[^\]]*\]|…pe…", " ¦ ", s))


def scan(s):
    w, i, out = toks(s), 0, []
    while i < len(w):
        for k in range(MAXW, 0, -1):
            if i + k > len(w):
                continue
            key = " ".join(w[i:i + k])
            for kk in (key, key[0].lower() + key[1:], key[0].upper() + key[1:]):
                if kk in SCAN:
                    out.append((kk, SCAN[kk]))
                    i += k
                    break
            else:
                continue
            break
        else:
            i += 1
    return out


PH_Y = sorted((k for k in M.PH if k.split()[0].lower() in ("yo", "yā", "yaṃ")), key=len, reverse=True)


def list_matches(x):
    """Synonym lists of the line; a «Yo / Yā / Yaṃ» that starts a fixed phrase of the tables is not a list."""
    out = []
    for m in LIST_RE.finditer(x):
        tail = x[m.start():]
        if any(tail.startswith(k) or tail.startswith(k[0].swapcase() + k[1:]) for k in PH_Y):
            continue
        out.append(m)
    return out + list(YE_RE.finditer(x))


def lists_and_phrases(x, y):
    errs = []
    rest = x
    lists = list_matches(x)
    for m in lists:
        items = scan(m[1])
        seen, pos = {}, 0
        for p, v in items:
            if v in seen and seen[v] != p:
                errs.append(f"list shares «{v}»: {seen[v]} / {p}")
            seen[v] = p
            j = y.find(v, pos)
            if j < 0:
                errs.append(f"list item missing / out of order «{v}» ({p})")
                break
            pos = j + len(v)
        rest = rest.replace(m[0], " ")
    for rx in FRAME_STRIP:
        rest = rx.sub(" ", rest)
    pos = 0
    for p, v in scan(rest):
        j = y.find(v, pos)
        if j < 0:
            errs.append(f"phrase missing / out of order «{v[:40]}» ({p})")
            break
        pos = j + len(v)
    return errs


def list_words_ok(x):
    """Every word of every synonym list is covered by the scanner (no unknown or skipped Pāli word)."""
    errs = []
    for m in list_matches(x):
        covered = sum(len(k.split()) for k, _ in scan(m[1]))
        total = len([t for t in toks(m[1]) if t != "¦"])
        if covered != total:
            errs.append(f"list words {covered} of {total} known")
    return errs


ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)$")


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


def strip_br(s):
    return re.sub(r"\[[^\]]*\]", " ", s)


def main():
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
            if xb.startswith("#"):
                m = re.fullmatch(r"(#+) (.+)", xb)
                if yb != f"{m[1]} {F.HEAD[m[2]]}":
                    e.append("heading")
            else:
                np_, nm = neg_count(xs, NEG_PI_RE, "x"), neg_count(ys, NEG_MY_RE)
                if np_ != nm:
                    e.append(f"negations {np_} vs {nm}")
                e += frames(xb, yb)
                e += matika(xb, yb)
                e += lists_and_phrases(xb, yb)
                e += list_words_ok(xb)
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
                probs.append(f"line {i}: " + "; ".join(e[:4]))
        if probs:
            bad += 1
            print(f"{tgt}: {len(probs)} mismatches")
            for p in probs[:60]:
                print("  ", p)
        else:
            print(f"{tgt}: OK ({len(b)} lines, 0 mismatches)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
