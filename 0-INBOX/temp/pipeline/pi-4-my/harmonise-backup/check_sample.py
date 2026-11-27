"""Check of the pi-4 Burmese zero-shot sample (preamble, 1-matika, 2-ekakapuggalapannatti) against the Pāli.

usage: python3 -I -X utf8 check_sample.py
  A. regeneration: make_sample's tables + my4_formulas.translate_line() on every Pāli line give exactly the files.
  B. per line, parsed here with its own patterns (not those of my4_formulas):
     B1 typography: no «?», «।», «:-», no Zawgyi sign (a vowel sign «ေ» opening a word), NFC; every Pāli
        sentence end («.» / «?», brackets and IDs removed) is one «။» (same count per line); a list head «… –»
        stays «… –»; a mātikā item without a full stop has none;
     B2 numbers: every number of the Pāli (cardinals in all cases, number stems in names and headings: ekaka …
        dasaka, ubhato-, dvi-, te-, chaḷ-, sattakkhattu-, saki- …) against the Burmese numbers before a classifier,
        same multiset per line (the fixed phrases «သူတစ်ပါး» others, «ကမ်းတစ်ဖက်» far bank, «တစ်စိတ်တစ်ပိုင်း»
        partly are not numbers);
     B3 polarity: the negations of each line (Pāli: na, no, neva, nap-, nār-, nā- and the privative words of
        PRIV) against the Burmese negations («မဟုတ်», the negative «မ» before a verb), same count per line,
        apart from the listed lexical renderings (LEX: avaṇṇa = «ကဲ့ရဲ့», anāgāmī = «အနာဂါမ်» …);
        and the polarity pairs of the name table (X / a-X …: the Burmese negations differ by the Pāli count);
     B4 table values: the topic lists of ^4-M-2 … ^4-M-6 item by item against the pi-2 rails lists;
     B5 names: each definition's question name = its closing name «“X”» = the mātikā item of the same type
        (^4-M-7 by position), and every name of a mātikā line is the table's.
  C. reuse test (pi-1 / pi-2 / pi-3 FINAL rails texts, read here independently): C1 the topic names; C2 every whole
     Pāli line / heading / colophon of the sample that also occurs in pi-1 / pi-2 / pi-3 has their Burmese; C3 every
     reused term and clause of REUSE: a rails segment has both the Pāli and the Burmese (witness), and every sample
     line with that Pāli has that Burmese. Prints n / n identical.
Exit 1 on any mismatch.
"""
import pathlib
import re
import sys
import unicodedata
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_sample as M  # noqa: E402  (installs its tables into my4_formulas; writes nothing at import)

F = M.F
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
NAMES = ["preamble.md", "1-matika.md", "2-ekakapuggalapannatti.md"]
ID = re.compile(r" ?\^[0-9A-Za-z-]+\s*$")
bad = []


def nonempty(p):
    return [l for l in unicodedata.normalize("NFC", p.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]


PAIRS = {n: list(zip(nonempty(PALI / n), nonempty(OUT / n))) for n in NAMES}
for n, prs in PAIRS.items():
    if len(nonempty(PALI / n)) != len(nonempty(OUT / n)):
        bad.append(f"{n}: line count differs")


def body(l):
    return ID.sub("", l).strip()


def nobr(s):
    return re.sub(r"\s*\[[^\]]*\]", "", s)


# ===================================================================================== A. regeneration
for name in NAMES:
    raw = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    regen = "\n".join(F.translate_line(l) for l in raw).rstrip("\n") + "\n"
    if unicodedata.normalize("NFC", regen) != (OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A {name}: file differs from the regenerated text")
print(f"A. regeneration: {len(NAMES) - sum(1 for b in bad if b.startswith('A '))} / {len(NAMES)} files identical")

# ===================================================================================== B1. typography
nb1 = 0
for name, prs in PAIRS.items():
    raw = (OUT / name).read_text(encoding="utf-8")
    if raw != unicodedata.normalize("NFC", raw):
        bad.append(f"B1 {name}: not NFC")
    for ch in ("?", "।", ":-"):
        if ch in raw:
            bad.append(f"B1 {name}: contains {ch}")
    if re.search(r"(^|[\s“‘(])ေ", raw, re.M):
        bad.append(f"B1 {name}: Zawgyi-like «ေ» at word start")
    for i, (p, m) in enumerate(prs):
        nb1 += 1
        pb, mb = nobr(body(p)), body(m)
        np_ = len(re.findall(r'[.?]"?(?=\s|$)', re.sub(r"^#+ .*", "", pb)))
        nm = mb.count("။")
        if np_ != nm:
            bad.append(f"B1 {name}:{i + 1}: {np_} Pāli sentence ends, {nm} «။»")
        if pb.endswith("–") != mb.endswith("–"):
            bad.append(f"B1 {name}:{i + 1}: list-head dash")
        if pb.endswith("?") and not mb.endswith("နည်း။"):
            bad.append(f"B1 {name}:{i + 1}: question without «နည်း။»")
        if re.match(r"\(\d+\) ", pb) and not pb.endswith((".", "?")) and mb.endswith("။"):
            bad.append(f"B1 {name}:{i + 1}: item without full stop got «။»")
print(f"B1. typography: {nb1} lines checked")

# ===================================================================================== B2. numbers
P_NUM = [  # (regex on the Pāli, number)  — word-bounded, case-insensitive
    (r"pañcakkhandhā", 5), (r"dvādasāyatanāni", 12), (r"aṭṭhārasa", 18), (r"bāvīsatindriyāni", 22),
    (r"cattār[oi]", 4), (r"dve", 2), (r"dvinnaṃ", 2), (r"tayo", 3), (r"tīṇi", 3), (r"tiṇṇaṃ", 3), (r"tīhi", 3),
    (r"pañca", 5), (r"pañcannaṃ", 5), (r"cha", 6), (r"chahi", 6), (r"satta", 7), (r"aṭṭha", 8), (r"nava", 9),
    (r"dasa", 10), (r"sattakkhattu\w*", 7), (r"chaḷabhiñño", 6), (r"tevijjo", 3), (r"ubhatobhāga\w*", 2),
    (r"dvicakkhu", 2), (r"ekacakkhu", 1), (r"ekabījī", 1), (r"ekaṃyeva", 1), (r"ekāsanikā", 1),
    (r"tecīvarikā", 3), (r"sakiṃ", 1), (r"sakideva", 1),
    (r"ekaka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 1), (r"duka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 2),
    (r"tika(?:ṃ|uddeso|niddeso|puggalapaññatti)", 3), (r"catukka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 4),
    (r"pañcaka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 5), (r"chakka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 6),
    (r"sattaka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 7), (r"aṭṭhaka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 8),
    (r"navaka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 9), (r"dasaka(?:ṃ|uddeso|niddeso|puggalapaññatti)", 10),
]
P_NUM_RE = [(re.compile(rf"(?<![\w]){rx}(?![\w])", re.I), n) for rx, n in P_NUM]
B_NUM = {"တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6, "ခုနစ်": 7, "ရှစ်": 8, "ကိုး": 9, "ဆယ်": 10,
         "ဆယ့်နှစ်": 12, "ဆယ့်ရှစ်": 18, "နှစ်ဆယ့်နှစ်": 22}
B_NUM_RE = re.compile(r"(?<![က-႟])(" + "|".join(sorted(map(re.escape, B_NUM), key=len, reverse=True)) +
                      r")(?=ယောက်|ပါး|ကြိမ်|မျိုး|စေ့|ခု|ထည်|ဖက်|ထိုင်)")
NOT_NUM = ["သူတစ်ပါး", "ကမ်းတစ်ဖက်", "တစ်စိတ်တစ်ပိုင်း"]


def p_nums(p):
    s = nobr(body(p))
    s = re.sub(r"^\(\d+\) ", "", s)
    out = []
    for rx, n in P_NUM_RE:
        out += [n] * len(rx.findall(s))
    return Counter(out)


def b_nums(m):
    s = body(m)
    s = re.sub(r"^#+ |^\(\d+\) ", "", s)
    s = re.sub(r"\[[^\]]*\]", "", s)
    for x in NOT_NUM:
        s = s.replace(x, "")
    return Counter(B_NUM[x] for x in B_NUM_RE.findall(s))


nb2 = 0
for name, prs in PAIRS.items():
    for i, (p, m) in enumerate(prs):
        a, b = p_nums(p), b_nums(m)
        nb2 += sum(a.values())
        if a != b:
            bad.append(f"B2 {name}:{i + 1}: numbers Pāli {dict(a)} / Burmese {dict(b)}")
print(f"B2. numbers: {nb2} numbers checked")

# ===================================================================================== B3. polarity
NEG_FREE = re.compile(r"(?<![\w])(?:na|no|neva|nappajānāti|nārabhati)(?![\w])", re.I)
PRIV = [  # Pāli words whose privative a- / an- is a negation in the Burmese (each counts once per occurrence)
    "asamayavimutt", "akuppadhamm", "aparihānadhamm", "akicchalābhī", "akasiralābhī", "aṭṭhānametaṃ", "anavakāso",
    "abhayūparato", "abhabbāgaman", "abhabbā", "aniyat", "anariy", "appahīnāni", "assaddhā", "acchandikā", "aneḷā",
    "apubbaṃ", "acarimaṃ", "ananussutesu", "anabhisambujjhati", "avinipātadhammo", "anāvattidhammo", "appattaṃ",
    "asaṅkhār", "arūpasahagatānaṃ", "arūparāg", "avijjā", "anaññātaññassāmītindriyaṃ", "akkodhano", "anupanāhī",
    "amakkhī", "apaḷāsī", "anissukī", "amaccharī", "asaṭho", "amāyāvī", "ahiriko", "anottappī", "aguttadvāro",
    "amattaññū", "asampajāno", "avītarāgo", "appameyyo", "asappuris", "anavajjo", "appasādanīye", "appasādaṃ",
    "ananuvicca", "apariyogāhetvā", "anupapanno", "samaṇamacalo", "anattantapo", "aparantapo", "aparisesā",
    "anāgantā", "anāgantvā", "nirāso",
]
PRIV_RE = re.compile(r"(?<![\w])(?:" + "|".join(map(re.escape, PRIV)) + r")\w*", re.I)
LEX = {  # rendered by a Burmese word without negation (Pāli count 0) / Burmese negation without a Pāli one
    "avaṇṇ": "avaṇṇa (dispraise) = «ကဲ့ရဲ့»", "asekkh": "asekkha (beyond training) = «ကျင့်ကြံမှု ပြီးဆုံးသူ»",
    "anāgāmī": "anāgāmī = «အနာဂါမ်»", "anāgāmi": "anāgāmiphala = «အနာဂါမိဖိုလ်»", "akaniṭṭh": "Akaniṭṭha (name)",
    "avihā": "Avihā (name)", "atapp": "Atappa (name)", "anavases": "anavasesa = «အကြွင်းမဲ့»",
    "akusal": "akusala = «အကုသိုလ်»", "anurakkh": "anu- (not privative)", "anusot": "anu- (not privative)",
    "aññ": "añña (not privative)",
}
B_EXTRA = {  # Burmese negations with no Pāli negation: (line marker, count, reason)
    "dubbaco": (1, "dubbaco (du-) = «သွန်သင်ချက်ကို နားမထောင်သူ»"),
    "nesajjikā": (1, "nesajjika = «မလျောင်းဘဲ ထိုင်၍သာ နေသူ»"),
    "khalupacchābhattikā": (1, "khalupacchābhattika = «… ဆွမ်းကို မစားသူ»"),
    "lolo": (1, "lolo (fickle) = «စိတ် မတည်ငြိမ်သူ»"),
    "antarāparinibbāyī": (1, "antarā (in the interval) = «သက်တမ်း၏ အလယ်သို့ မရောက်မီ»"),
    "na yatthicchakaṃ": (1, "one na before «samāpajjatipi vuṭṭhātipi» = two Burmese negations"),
}
P_COMPOUND = {"nevasekkhanāsekkh": 2, "rūparāgaarūparāgamānauddhaccaavijjāya": 2}   # negations inside compounds
B_NEG_RE = re.compile(r"မဟုတ်|မ(?=[က-အ](?![့ံ]*[်္]))")
NOT_NEG = ["မနော", "မစင်", "ကာမ", "မိန်းမ"]           # mano, gūtha, kāma, itthī: a final / initial «မ» that is no negation


def p_neg(p):
    s = nobr(body(p))
    s = re.sub(r"^#+ .*", "", s)
    n = len(NEG_FREE.findall(s)) + len(PRIV_RE.findall(s))
    for k, (c, _) in B_EXTRA.items():
        n += c * len(re.findall(rf"(?<![\w]){k}", s, re.I))
    for k, c in P_COMPOUND.items():
        n += c * len(re.findall(rf"(?<![\w]){k}", s, re.I))
    return n


def b_neg(m):
    s = re.sub(r"\[[^\]]*\]", "", body(m))
    for x in NOT_NEG:
        s = s.replace(x, "")
    return len(B_NEG_RE.findall(s))


nb3 = 0
for name, prs in PAIRS.items():
    for i, (p, m) in enumerate(prs):
        a, b = p_neg(p), b_neg(m)
        nb3 += a
        if a != b:
            bad.append(f"B3 {name}:{i + 1}: negations Pāli {a} / Burmese {b}")
POLAR = [  # (positive, negative, Pāli negations more in the negative)
    ("samayavimutto", "asamayavimutto", 1), ("kuppadhammo", "akuppadhammo", 1),
    ("parihānadhammo", "aparihānadhammo", 1), ("bhayūparato", "abhayūparato", 1),
    ("bhabbāgamano", "abhabbāgamano", 1), ("niyato", "aniyato", 1), ("ariyo", "anariyo", 1),
    ("kodhano", "akkodhano", 1), ("upanāhī", "anupanāhī", 1), ("makkhī", "amakkhī", 1), ("paḷāsī", "apaḷāsī", 1),
    ("issukī", "anissukī", 1), ("maccharī", "amaccharī", 1), ("saṭho", "asaṭho", 1), ("māyāvī", "amāyāvī", 1),
    ("hirimā", "ahiriko", 1), ("ottappī", "anottappī", 1), ("indriyesu guttadvāro", "indriyesu aguttadvāro", 1),
    ("bhojane mattaññū", "bhojane amattaññū", 1), ("sampajāno", "asampajāno", 1), ("sappuriso", "asappuriso", 1),
    ("kāmesu ca bhavesu ca vītarāgo", "kāmesu ca bhavesu ca avītarāgo", 1),
    ("sevitabbo bhajitabbo payirupāsitabbo", "na sevitabbo na bhajitabbo na payirupāsitabbo", 3),
    ("yuttappaṭibhāno ca muttappaṭibhāno ca", "neva yuttappaṭibhāno no muttappaṭibhāno", 2),
    ("uṭṭhānaphalūpajīvī ca puññaphalūpajīvī ca", "neva uṭṭhānaphalūpajīvī no puññaphalūpajīvī", 2),
    ("appassuto sutena upapanno", "appassuto sutena anupapanno", 1),
    ("bahussuto sutena upapanno", "bahussuto sutena anupapanno", 1), ("sekkho", "nevasekkhanāsekkho", 2),
]
for pos, neg, n in POLAR:
    a, b = F.NAME[pos], F.NAME[neg]
    nb3 += 1
    if b_neg(neg_m := b) - b_neg(a) != n or a == b:
        bad.append(f"B3 pair {pos} / {neg}: Burmese negations {b_neg(a)} / {b_neg(neg_m)}, expected +{n}")
print(f"B3. polarity: {nb3} negations / pairs checked; lexical renderings: {len(LEX)}, Burmese-only: {len(B_EXTRA)}")

# ===================================================================================== FINAL (independent read)
FIN = []
for b in "123":
    for f in sorted((ROOT / f"AI_translation/pali/pi-{b}_split_chapters").glob("*.md")):
        bf = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters" / f.name
        if not bf.exists():
            continue
        segs, cur_p, cur_m = [], [], []
        pl = [l for l in f.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        ml = [l for l in unicodedata.normalize("NFC", bf.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]
        if len(pl) != len(ml):
            sys.exit(f"FINAL pi-{b} {f.name}: line counts differ")
        sid = ""
        for x, y in zip(pl, ml):
            FIN.append((b, f.name, x, y))
SEGS = {}
_cur = []
for b, fn, x, y in FIN:
    _cur.append((x, y))
    m = re.search(r"\^([0-9A-Za-z-]+)\s*$", x)
    if m:
        SEGS[(b, m[1])] = (" ".join(a for a, _ in _cur), " ".join(c for _, c in _cur))
        _cur = []

# ===================================================================================== B4. topic lists vs pi-2
LISTS = {}
for b, fn, x, y in FIN:
    if b == "2" and re.match(r"(Pañcakkhandhā|Dvādasāyatanāni|Aṭṭhārasa dhātuyo|Bāvīsatindriyāni) – ", x):
        ph, pl_ = nobr(body(x)).split(" – ", 1)
        mh, ml_ = re.sub(r"\s*\[[^\]]*\]", "", body(y)).split(" – ", 1)
        LISTS.setdefault(ph, (mh, dict(zip([t.strip() for t in pl_.rstrip(".").split(",")],
                                           [t.strip() for t in ml_.rstrip("။").split("၊")]))))
SACCA = {"dukkhasaccaṃ": "ဒုက္ခ သစ္စာ", "samudayasaccaṃ": "ဖြစ်ပေါ်ခြင်း သစ္စာ", "nirodhasaccaṃ": "ချုပ်ငြိမ်းခြင်း သစ္စာ",
         "maggasaccaṃ": "မဂ် သစ္စာ"}
for k, v in SACCA.items():      # pi-2 ^2-218 (pañhāpucchaka subjects «Xသည်»)
    if v + "သည်" not in SEGS[("2", "2-218")][1] or k[0].upper() + k[1:] not in SEGS[("2", "2-218")][0]:
        bad.append(f"B4 sacca {k}: not in pi-2 ^2-218")
LISTS["cattāri saccāni"] = ("သစ္စာ လေးပါး", SACCA)
n_top = same_top = 0
for p, m in PAIRS["1-matika.md"][3:8]:
    mm = re.search(r"Yāvatā (.+?) – (.+); ettāvatā", p)
    head = mm[1]
    key = head[0].upper() + head[1:] if head[0].upper() + head[1:] in LISTS else head
    mh, items = LISTS[key]
    my_list = re.search(r"နည်း။ (.+?) – (.+) ရှိသမျှ၊", m)
    n_top += 1 + len(mm[2].split(","))
    same_top += (my_list[1] == mh)
    for pi_, my_ in zip([t.strip() for t in mm[2].split(",")], my_list[2].split("၊ ")):
        same_top += (items.get(pi_) == my_)
        if items.get(pi_) != my_:
            bad.append(f"B4/C1 topic {pi_}: «{my_}» vs pi-2 «{items.get(pi_)}»")
print(f"B4. topic lists: {same_top} / {n_top} heads and items as pi-2")

# ===================================================================================== B5. names
mat = [body(m) for p, m in PAIRS["1-matika.md"] if re.match(r"\(\d+\) ", p) and "^4-M-7" not in p][:0]
ek_p = [body(p) for p, m in PAIRS["1-matika.md"]][9:63]
ek_m = [body(m) for p, m in PAIRS["1-matika.md"]][9:63]
assert ek_p[0].startswith("(1) ") and ek_p[-1].startswith("(54) ")
MAT_NAME = {}
for p, m in zip(ek_p, ek_m):
    kp = nobr(re.sub(r"^\(\d+\) ", "", p))
    MAT_NAME.setdefault(kp.lower(), re.sub(r"\s*\[[^\]]*\]", "", re.sub(r"^\(\d+\) ", "", m)))
nb5 = 0
for p, m in PAIRS["2-ekakapuggalapannatti.md"]:
    q = re.match(r"Katamo ca puggalo (.+?)\?", p)
    if not q:
        continue
    nb5 += 1
    k = q[1]
    qm = re.match(r"(.+?) ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။", m)[1]
    names = re.findall(r'vuccati puggalo "([^"]+)"|vuccanti puggalā "([^"]+)"', p)
    quoted = re.findall(r"“([^”]+)”ဟု ခေါ်သည်", m)
    mk = MAT_NAME.get(k.lower().replace(" ", "")) or MAT_NAME.get(k.lower())
    if k == "sotāpanno sotāpattiphalasacchikiriyāya paṭipanno":
        exp = f"{MAT_NAME['sotāpanno']}နှင့် {MAT_NAME['sotāpattiphalasacchikiriyāya paṭipanno']}"
    else:
        exp = mk
    if qm != exp:
        bad.append(f"B5 question «{k}»: «{qm}» vs mātikā «{exp}»")
    for (a, b_), qn in zip(names, quoted):
        pn = (a or b_)
        if F.NAME[F.key_of(pn)] != qn:
            bad.append(f"B5 closing name «{pn}»: «{qn}»")
        if pn.lower() in MAT_NAME and MAT_NAME[pn.lower()] != qn:
            bad.append(f"B5 closing name «{pn}» vs mātikā")
    if len(names) != len(quoted):
        bad.append(f"B5 «{k}»: {len(names)} closing names, {len(quoted)} quoted")
# every name of the mātikā (sections 1-10) is the table's
for p, m in PAIRS["1-matika.md"]:
    t = nobr(re.sub(r"^\(\d+\) ", "", body(p))).rstrip(".")
    k = F.key_of(t) if t else None
    if k and re.match(r"\(\d+\) ", p):
        nb5 += 1
        if re.sub(r"\s*\[[^\]]*\]", "", re.sub(r"^\(\d+\) ", "", body(m))).rstrip("။") != F.NAME[k]:
            bad.append(f"B5 mātikā item {t}")
print(f"B5. names: {nb5} questions / mātikā names checked")

# ===================================================================================== C. reuse test
# C1 topic names = B4 (pi-2 lists)
# C2 whole lines / headings / colophons
FIN_LINE = {}
for b, fn, x, y in FIN:
    FIN_LINE.setdefault(nobr(body(x)).rstrip("."), set()).add(body(y).rstrip("။"))
n_c2 = s_c2 = 0
for name, prs in PAIRS.items():
    for p, m in prs:
        k = nobr(body(p)).rstrip(".")
        if k in FIN_LINE:
            n_c2 += 1
            mb = re.sub(r"\s*\[[^\]]*\]", "", body(m)).rstrip("။")
            if mb in FIN_LINE[k]:
                s_c2 += 1
            else:
                bad.append(f"C2 «{k}»: «{mb}» vs final {sorted(FIN_LINE[k])[:2]}")
# C3 reused terms and clauses: (regex on the pi-4 Pāli, the Pāli in a pi-1/2/3 segment, the final Burmese)
REUSE = [
    (r"\bpuggal", "ekaṃ puggalaṃ", "ပုဂ္ဂိုလ်"), (r"\bariyapuggal", "ariyamaggesu", "အရိယာ"),
    (r"\bariyamaggaṃ", "Ariyamaggaṃ ārabbha", "အရိယာ မဂ်"), (r"\baṭṭha vimokkhe", "Aṭṭha vimokkhā", "လွတ်မြောက်ခြင်း ရှစ်ပါး"),
    (r"\bvimokkhe\b", "vimokkho", "လွတ်မြောက်ခြင်း"), (r"\bkāyena\b", "kāyena", "ကိုယ်ဖြင့်"),
    (r"\bphusitvā", "phusitvā", "ထိ၍"),
    (r"\bāsavā\b", "āsavā dhammā", "စိတ်အစွန်းအထင်း"), (r"\bsamāpatt", "samāpattikusalatā", "ဈာန် ဝင်စားရာ"),
    (r"\bsamāpajjati", "samāpajjati", "ဝင်စား"), (r"\bvuṭṭhāti", "vuṭṭhāti", "ထမြောက်"),
    (r"\bpamādamāgamma", "Pamādo", "မေ့လျော့မှု"), (r"āgamma", "āgamma", "မှီ၍"),
    (r"\bAṭṭhānametaṃ anavakāso", "Aṭṭhānametaṃ anavakāso", "မဖြစ်နိုင်သော အကြောင်း ဖြစ်သည်၊ အခွင့်အလမ်း မရှိ"),
    (r"\bṬhānaṃ kho panetaṃ vijjati", "Ṭhānañca kho etaṃ vijjati", "ဟူသည်ကား ဖြစ်နိုင်သော အကြောင်း ရှိသည်"),
    (r"\bsaṃyojan", "saṃyojanāni", "နှောင်ကြိုး"), (r"\b(?:tīṇi saṃyojanāni|tiṇṇaṃ saṃyojanānaṃ)", "Tīṇi saṃyojanāni",
                                                       "နှောင်ကြိုး သုံးပါး"),
    (r"\bpahānāya", "pahānāya", "ပယ်ရန်"), (r"\bpahīnā", "pahīn", "ပယ်ပြီး"), (r"\bputhujjan", "puthujjano", "ပုထုဇဉ်"),
    (r"\bsamanantarā", "samanantarā", "ချက်ချင်း နောက်၌"), (r"\btehi dhammehi", "tehi dhammehi", "ထိုသဘောတရားတို့နှင့်"),
    (r"\bsamannāgato", "samannāgato", "အပြည့်အဝ ပြည့်စုံ"),
    (r"(?<!na )\bkammāvaraṇena samannāgatā", "kammāvaraṇena samannāgatā", "ကံ အဟန့်အတားနှင့် အပြည့်အဝ ပြည့်စုံသော"),
    (r"\bkilesāvaraṇena samannāgatā", "kilesāvaraṇena samannāgatā", "ကိလေသာ အဟန့်အတားနှင့်"),
    (r"\bvipākāvaraṇena samannāgatā", "vipākāvaraṇena samannāgatā", "အကျိုး အဟန့်အတားနှင့်"),
    (r"\bna kammāvaraṇena samannāgatā", "na kammāvaraṇena samannāgatā", "ကံ အဟန့်အတားနှင့် မပြည့်စုံသော"),
    (r"\bassaddhā acchandikā duppaññā", "assaddhā acchandikā duppaññā", "ယုံကြည်မှု မရှိသော၊ ဆန္ဒ မရှိသော၊ ပညာ နည်းသော"),
    (r"\bsaddhā chandikā paññavanto", "saddhā chandikā paññavanto", "ယုံကြည်မှု ရှိသော၊ ဆန္ဒ ရှိသော၊ ပညာ ရှိသော"),
    (r"\bniyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ", "niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ",
     "ကုသိုလ် သဘောတရားတို့၌ မှန်ကန်မှု ဖြစ်သော သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းရန်"),
    (r"\babhabbā niyāmaṃ", "abhabbā niyāmaṃ", "သက်ဆင်းရန် မထိုက်တန်သော"),
    (r"(?<![a])\bbhabbā niyāmaṃ", "bhabbā niyāmaṃ", "သက်ဆင်းရန် ထိုက်တန်သော"),
    (r"\bsekkhā\b", "sekkhā dhammā", "ကျင့်ကြံဆဲသူ"), (r"\basekkho", "asekkhā dhammā", "ကျင့်ကြံမှု ပြီးဆုံးသူ"),
    (r"\bsīlavanto", "sīlavanto", "သီလ ရှိသော"), (r"\b[Aa]rahā\b", "arahanto jīvitā", "ရဟန္တာ"),
    (r"\bānantarikā", "kammāni ānantarikāni", "ချက်ချင်း အကျိုးပေးသော ကံ"),
    (r"\bmicchādiṭṭhikā", "micchādiṭṭhik", "မှားယွင်းသော အယူ ရှိ"), (r"\bniyat", "niyato", "ကျိန်းသေ"),
    (r"\bavasesā", "avasesā", "ကြွင်းကျန်သော"), (r"\bmaggasamaṅgino", "maggasamaṅgissa", "မဂ်နှင့် ပြည့်စုံ"),
    (r"\bphalasamaṅgino", "phalasamaṅgissa", "ဖိုလ်နှင့် ပြည့်စုံ"),
    (r"\bapubbaṃ acarimaṃ", "apubbaṃ acarimaṃ", "ရှေ့ မရှိ၊ နောက် မရှိဘဲ"), (r"\bjīvita", "jīvitā", "အသက်"),
    (r"\bsotāpattiphal", "sotāpattiphale", "သောတာပတ္တိဖိုလ်"), (r"\bsakadāgāmiphal", "sakadāgāmiphale", "သကဒါဂါမိဖိုလ်"),
    (r"\banāgāmiphal", "anāgāmiphale", "အနာဂါမိဖိုလ်"), (r"\barahattaphal", "arahattaphale", "ရဟန္တာဖိုလ်"),
    (r"sacchikiriyāya", "sacchikiriyāya", "မျက်မှောက်ပြုရန်"), (r"\bpaṭipann", "paṭipannā", "ကျင့်ကြံ"),
    (r"\bkappassa", "kappassa", "ကမ္ဘာ"), (r"\bvijjāhi", "vijjā ca", "အမှန်သိမြင်မှု"),
    (r"\bChahi abhiññāhi", "Chasu abhiññāsu", "ထူးကဲစွာ သိခြင်း ခြောက်ပါး"),
    (r"\bsammāsambuddho", "sammāsambuddho", "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်"),
    (r"\bbalesu", "balañca", "စွမ်းအား"), (r"\bsaccāni", "saccāni", "သစ္စာ"),
    (r"\byathābhūtaṃ pajānāti", "yathābhūtaṃ pajānāti", "ဟုတ်မှန်သည့်အတိုင်း ကွဲပြားစွာ သိ"),
    (r"\bdukkhasamudayo", "dukkhasamudayo", "ဒုက္ခ ဖြစ်ပေါ်ခြင်း"), (r"\bdukkhanirodho", "dukkhanirodho", "ဒုက္ခ ချုပ်ငြိမ်းခြင်း"),
    (r"\bdukkhanirodhagāminī paṭipadā", "dukkhanirodhagāminī paṭipadā", "ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်"),
    (r"\bTathāgatappaveditā", "tathāgato", "မြတ်စွာဘုရား"), (r"\bpaññindriyaṃ", "paññindriyaṃ", "ပညာ၏ စွမ်းရည်"),
    (r"\bsaddhindriyaṃ", "saddhindriyaṃ", "ယုံကြည်မှု၏ စွမ်းရည်"), (r"\bbhāveti", "bhāveti", "ပွားများ"),
    (r"\bdeve\b", "deve", "နတ်"), (r"\bkulāni", "kulāni", "အမျိုး"), (r"\bnibbattetvā", "nibbatteti", "ပေါ်ထွက်စေ"),
    (r"\bbhavaṃ\b", "aṭṭhamaṃ bhavaṃ", "ဘဝ"),
    (r"\borambhāgiyānaṃ saṃyojanānaṃ", "Pañcorambhāgiyāni saṃyojanāni", "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး"),
    (r"\bopapātiko", "Opapātikānaṃ", "အလိုအလျောက် ပေါ်လာ"), (r"\bāyuppamāṇaṃ", "āyuppamāṇaṃ", "သက်တမ်း အတိုင်းအတာ"),
    (r"\bkālakiriyaṃ", "kālakiriyā", "ကွယ်လွန်ခြင်း"), (r"\bsasaṅkhārena", "sasaṅkhārena", "တိုက်တွန်းမှုဖြင့်"),
    (r"\bavihā\b", "Avihānaṃ", "အဝိဟာ"), (r"\batappaṃ", "Atappānaṃ", "အတပ္ပါ"), (r"\bsudassaṃ", "Sudassānaṃ", "သုဒဿာ"),
    (r"\bsudassiṃ", "Sudassīnaṃ", "သုဒဿီ"), (r"\bakaniṭṭh", "Akaniṭṭhānaṃ", "အကနိဋ္ဌ"), (r"\bcuto", "cuto", "သေ"),
    (r"\bKāmarāgabyāpād", "kāmarāgo", "ကာမရာဂ"), (r"\bKāmarāgabyāpād", "byāpādo", "ဖျက်ဆီးလိုစိတ်"),
    (r"\btanubhāvāya", "tanubhāvāya", "ပါးလျစေရန်"),
    (r"\brūparāgo arūparāgo māno uddhaccaṃ avijjā", "Rūparāgo, arūparāgo, māno, uddhaccaṃ, avijjā",
     "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ၊ ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ၊ မာန၊ ယောက်ယက်ခတ်မှု၊ အမှန်ကို မသိမှု"),
    (r"\bkodhano", "Kodho ca upanāho", "အမျက်ဒေါသ"), (r"\bupanāhī", "Kodho ca upanāho", "ရန်ငြိုး သိုထား"),
    (r"\bMakkhī", "Makkho ca paḷāso", "ကျေးဇူး ချေဖျက်"), (r"\bpaḷāsī", "Makkho ca paḷāso", "တုပြိုင်"),
    (r"\bIssukī", "Issā ca macchariyañca", "ငြူစူ"), (r"\bmaccharī", "Issā ca macchariyañca", "ဝန်တို"),
    (r"\bSaṭho", "Māyā ca sāṭheyyañca", "စဉ်းလဲ"), (r"\bmāyāvī", "Māyā ca sāṭheyyañca", "လှည့်စား"),
    (r"\bAhiriko", "ahirikañca", "ဒုစရိုက်ကို မရှက်"), (r"\banottappī", "anottappañca", "ဒုစရိုက်ကို မကြောက်ရွံ့"),
    (r"\bHirimā", "hirī ca", "ဒုစရိုက်ကို ရှက်"), (r"(?<!an)ottappī", "ottappañca", "ဒုစရိုက်ကို ကြောက်ရွံ့"),
    (r"\bDubbaco", "dovacassatā ca", "သွန်သင်ချက်ကို နားမထောင်"), (r"\bSuvaco", "sovacassatā ca", "သွန်သင်ချက်ကို နားထောင်"),
    (r"\bpāpamitto", "pāpamittatā ca", "မိတ်ဆွေဆိုးနှင့် ပေါင်းသင်း"),
    (r"\bkalyāṇamitto", "kalyāṇamittatā ca", "မိတ်ဆွေကောင်းနှင့် ပေါင်းသင်း"),
    (r"\bIndriyesu aguttadvāro", "indriyesu aguttadvāratā", "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို မစောင့်ထိန်း"),
    (r"\bIndriyesu guttadvāro", "indriyesu guttadvāratā", "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို စောင့်ထိန်း"),
    (r"\bbhojane amattaññū", "bhojane amattaññutā", "အစားအစာ၌ အတိုင်းအရှည်ကို မသိ"),
    (r"\bbhojane mattaññū", "bhojane mattaññutā", "အစားအစာ၌ အတိုင်းအရှည်ကို သိ"),
    (r"\bMuṭṭhassati", "Muṭṭhassaccañca", "သတိလစ်"), (r"\basampajāno", "asampajaññañca", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိ"),
    (r"(?<!a)\bsampajāno", "sampajaññañca", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း"),
    (r"\bSīlavipanno", "sīlavipatti ca", "သီလ ပျက်စီး"), (r"\bdiṭṭhivipanno", "diṭṭhivipatti ca", "အယူ ပျက်စီး"),
    (r"\bSīlasampanno", "sīlasampadā ca", "သီလ ပြည့်စုံ"), (r"\bdiṭṭhisampanno", "diṭṭhisampadā ca", "အယူ ပြည့်စုံ"),
    (r"\bAjjhattasaṃyojano", "Ajjhattasaṃyojanañca", "အတွင်းပိုင်း နှောင်ကြိုး"),
    (r"\bbahiddhāsaṃyojano", "bahiddhāsaṃyojanañca", "အပြင်ပိုင်း နှောင်ကြိုး"),
    (r"\bHīnādhimutto", "hīnā dhammā", "ယုတ်ညံ့"), (r"\bpaṇītādhimutto", "paṇītā dhammā", "မွန်မြတ်"),
    (r"\b\w+ādhimutto", "adhimutto", "စိတ်ညွတ်"), (r"\b[Aa]?sappuris", "sappurisānaṃ", "သူတော်ကောင်း"),
    (r"\bvītarāgo", "vītarāg", "ရာဂ ကင်း"), (r"\bkāmesu", "kāmesu", "ကာမ"), (r"\bbhavesu", "bhavesu", "ဘဝ"),
    (r"\bsevitabbo", "sevanā", "ပေါင်းသင်း"), (r"\bbhajitabbo", "bhajanā", "ဆည်းကပ်"),
    (r"\bpayirupāsitabbo", "payirupās", "ချဉ်းကပ် ခစား"), (r"\bsīlesu", "sīla", "သီလ"),
    (r"\bsamādhism", "samādhi", "သမာဓိ"), (r"\bsatthāro", "satthāraṃ", "ဆရာ"), (r"\bsamaṇa", "samaṇo", "ရဟန်း"),
    (r"\bbrāhmaṇo", "brāhmaṇo", "ပုဏ္ဏား"), (r"\b[Aa]ppassuto", "appassutā", "အကြားအမြင် နည်း"),
    (r"\bbahussuto", "bahussutā", "အကြားအမြင် များ"), (r"\bSarāgo", "rāgo", "ရာဂ"), (r"\bsadoso", "doso", "ဒေါသ"),
    (r"\bsamoho", "moho", "မောဟ"), (r"\bsamāno\b", "Māno", "မာန"),
    (r"\badhipaññādhammavipassanāya", "vipassanā ca", "ထိုးထွင်းသိမြင်ခြင်း"),
    (r"\bcetosamathassa", "samatho ca", "စိတ်ငြိမ်သက်ခြင်း"), (r"\bajjhattaṃ cetosamath", "ajjhattaṃ arūpasaññī", "မိမိ၌"),
    (r"\bdiṭṭhe(?:va| ceva) dhamme", "diṭṭheva dhamme", "မျက်မှောက်ဘဝ၌ပင်"),
    (r"\bcetovimuttiṃ paññāvimuttiṃ", "cetovimuttiṃ paññāvimuttiṃ", "စိတ်၏ လွတ်မြောက်ခြင်း၊ ပညာဖြင့် လွတ်မြောက်ခြင်း"),
    (r"\buppannā pāpakā akusalā dhammā", "uppannā", "ဖြစ်ပေါ်ပြီးသော"), (r"\bpāpakā akusalā", "pāpakā", "ယုတ်မာသော"),
    (r"\bakusalā dhammā", "akusalā dhammā", "အကုသိုလ် သဘောတရား"), (r"\bnirujjhanti", "nirujjhanti", "ချုပ်ငြိမ်း"),
    (r"\bsāvakapārami", "sāvako", "တပည့်"), (r"\brukkhamūlikā", "rukkhamūla", "သစ်ပင်"),
    (r"\bghosapp", "ghoso", "အသံဗလံ"), (r"\bRūpappamāṇo", "rūpārammaṇaṃ", "အဆင်းအရောင်"),
    (r"\b[Ss]āvajjo|\bvajjabahulo|\bappavajjo|\banavajjo", "vajjesu", "အပြစ်"),
    (r"\bappaṭibhān|ppaṭibhāno", "paṭibhānapaṭisambhidā", "ဉာဏ်ပေါ်မှု"), (r"\bpuññaphal", "puñña", "ကောင်းမှု"),
    (r"\bvaḍḍhanti", "vaḍḍh", "တိုးပွား"),
]
n_c3 = s_c3 = 0
PI4 = [(nobr(body(p)), body(m)) for prs in PAIRS.values() for p, m in prs]
for rx, fp, my in REUSE:
    n_c3 += 1
    wit = [k for k, (sp, sm) in SEGS.items() if fp.lower() in nobr(sp).lower() and my in sm]
    occ = [(p, m) for p, m in PI4 if re.search(rx, p, re.I)]
    miss = [p[:70] for p, m in occ if my not in m]
    if wit and occ and not miss:
        s_c3 += 1
    else:
        bad.append(f"C3 «{rx}» / «{my}»: witness {wit[:1] or 'NONE'}, {len(occ)} sample lines, missing in {miss[:2]}")
print(f"C. reuse test: C1 topic names {same_top} / {n_top}; C2 whole lines / headings / colophons {s_c2} / {n_c2}; "
      f"C3 terms and clauses {s_c3} / {n_c3} identical with pi-1 / pi-2 / pi-3 final")
tot_s, tot_n = same_top + s_c2 + s_c3, n_top + n_c2 + n_c3
if bad:
    print(f"\nMISMATCHES: {len(bad)}")
    for b in bad:
        print("  " + b)
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {tot_s} / {tot_n} identical")
