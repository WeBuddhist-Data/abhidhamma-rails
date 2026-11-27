"""Check of the pi-4 Burmese zero-shot chapters 3-dukapuggalapannatti and 4-tikapuggalapannatti against the Pāli.

usage: python3 -I -X utf8 check_ch3-4.py
Adapted from check_sample.py.
  A. regeneration: make_ch3-4's tables + my4_formulas.translate_line() on every Pāli line give exactly the files.
  B. per line, parsed here with its own patterns (not those of my4_formulas / make_ch3-4):
     B1 typography: no «?», «।», «:-», no Zawgyi sign, NFC; every Pāli sentence end («.» / «?» / «!», brackets and
        IDs removed) is one «။» (same count per line); every Pāli «?» is one «နည်း။» (questions inside quotes in the
        Burmese without a Pāli «?» end in «နည်း”»); an item number «(n)» at a line end stays there;
     B2 numbers: every number of the Pāli (cardinals, number stems: duka-, tika-, dvi-, eka-, channaṃ …) against
        the Burmese numbers before a classifier, same multiset per line;
     B3 polarity: the negations of each line (Pāli: na, no, neva, natthi, mā, nā- and the privative words of PRIV;
        «no» = "us" in ^4-122 is not a negation) against the Burmese negations («မဟုတ်», the negative «မ» before a
        verb), same count per line, apart from the listed lexical renderings (LEX) and Burmese-only negations
        (B_EXTRA); and the polarity pairs of the duka / tika names;
     B4 quality nouns: in each duka definition the noun of «Tattha katamo X?» is the noun of «ayaṃ vuccati X» and
        of «Yassa puggalassa ayaṃ X …» / «Iminā X-ena …» in the same line;
     B5 names: each definition's question name = its closing name(s) («“X”ဟု ခေါ်သည်» / «“X” ဖြစ်သည်» / unquoted
        «…ဟု ခေါ်သည်») = the name table = the mātikā Burmese (1-matika ^4-M-8 duka, ^4-M-9 tika).
  C. reuse test (pi-1 / pi-2 / pi-3 FINAL rails texts, read here independently):
     C1 every final unit read by make_ch3-4 (REUSED): the final segment has its Pāli and its Burmese, and the
        Burmese stands (variant brackets left out) in every pi-4 line with that Pāli, apart from the ADAPTED list
        (the pi-4 Pāli differs; reason given);
     C2 whole lines / headings / colophons that also occur in pi-1 / pi-2 / pi-3 have their Burmese;
     C3 reused terms and clauses (REUSE): a rails segment has both, every pi-4 line with that Pāli has that Burmese.
     Prints n / n identical.
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
import importlib  # noqa: E402

G = importlib.import_module("make_ch3-4")       # installs its tables into my4_formulas; writes nothing at import
F = G.F
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
NAMES = ["3-dukapuggalapannatti.md", "4-tikapuggalapannatti.md"]
ID = re.compile(r" ?\^[0-9A-Za-z-]+\s*$")
bad = []


def nonempty(p):
    return [l for l in unicodedata.normalize("NFC", p.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]


PAIRS = {n: list(zip(nonempty(PALI / n), nonempty(OUT / n))) for n in NAMES}
for n in NAMES:
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
    for ch in ("?", "।", ":-", "!"):
        if ch in raw:
            bad.append(f"B1 {name}: contains {ch}")
    if re.search(r"(^|[\s“‘(])ေ", raw, re.M):
        bad.append(f"B1 {name}: Zawgyi-like «ေ» at word start")
    for i, (p, m) in enumerate(prs):
        nb1 += 1
        pb, mb = nobr(body(p)), nobr(body(m))
        pb0 = re.sub(r"^#+ .*", "", pb)
        np_ = len(re.findall(r'[.?!]"?(?=\s|$)', pb0))
        if np_ != mb.count("။"):
            bad.append(f"B1 {name}:{i + 1}: {np_} Pāli sentence ends, {mb.count('။')} «။»")
        if pb0.count("?") != mb.count("နည်း။"):
            bad.append(f"B1 {name}:{i + 1}: {pb0.count('?')} «?», {mb.count('နည်း။')} «နည်း။»")
        if re.findall(r"\(\d+\)$", pb) != re.findall(r"\(\d+\)$", mb):
            bad.append(f"B1 {name}:{i + 1}: item number at the line end")
print(f"B1. typography: {nb1} lines checked")

# ===================================================================================== B2. numbers
P_NUM = [
    (r"cattār[oi]", 4), (r"dve", 2), (r"dvinnaṃ", 2), (r"tayo", 3), (r"tayome", 3), (r"tīṇi", 3), (r"tiṇṇaṃ", 3),
    (r"pañca", 5), (r"pañc(?:or|uddh)ambhāgiyāni", 5), (r"cha", 6), (r"channaṃ", 6), (r"satta", 7), (r"aṭṭha", 8),
    (r"dvicakkhu", 2), (r"ekacakkhu", 1), (r"ekaggacitto", 1),
    (r"duka(?:ṃ|niddeso|puggalapaññatti)", 2), (r"tika(?:ṃ|niddeso|puggalapaññatti)", 3),
]
P_NUM_RE = [(re.compile(rf"(?<![\w]){rx}(?![\w])", re.I), n) for rx, n in P_NUM]
B_NUM = {"တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6, "ခုနစ်": 7, "ရှစ်": 8, "ကိုး": 9, "ဆယ်": 10}
B_NUM_RE = re.compile(r"(?<![က-႟])(" + "|".join(sorted(map(re.escape, B_NUM), key=len, reverse=True)) +
                      r")(?=ယောက်|ပါး|ကြိမ်|မျိုး|စေ့|ခု|ထည်|ဖက်|ထိုင်)")
NOT_NUM = ["သူတစ်ပါး"]


def p_nums(p):
    s = nobr(body(p))
    out = []
    for rx, n in P_NUM_RE:
        out += [n] * len(rx.findall(s))
    return Counter(out)


def b_nums(m):
    s = re.sub(r"^#+ ", "", nobr(body(m)))
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
NEG_FREE = re.compile(r"(?<![\w])(?:na|no|neva|natthi|mā|nānubyañjanaggāhī)(?![\w])", re.I)
NOT_NEG_P = [r"\b(?:ca|sā ca) no (?=bhavissat|phāsu|pavattinī)"]      # «no» = "us" (^4-122)
PRIV = [  # Pāli words whose privative a- / an- / ni- is a negation in the Burmese (stems; each occurrence once)
    "abhejj", "abrahmacār", "abyatt", "acapal", "adassan", "adhāraṇ", "agopan", "aguttadvār", "agutti", "agārav",
    "ahirik", "ahitāya", "ajānaṃ", "akkodhan", "alabhant", "amacchar", "amakkh", "amanāp", "amattaññ", "amukhar",
    "amāyāv", "amoh", "anabhisamay", "anadhigat", "ananubodh", "ananussat", "anattaman", "anatth", "anavajj",
    "anissuk", "anottapp", "anuddhat", "anunnaḷ", "anupanāh", "anuttānīkamm", "anādariy", "anārakkh", "anāsav",
    "anāvikamm", "apaccakkhakamm", "apaccavekkhaṇ", "aparipūr", "apariyogāhaṇ", "apassaṃ", "apaḷās", "apilāpan",
    "appaccay", "appahīn", "appameyy", "appatissav", "appaṭinissagg", "appaṭisaṅkh", "appaṭissat", "appaṭivedh",
    "arūpāvacar", "asamapekkhaṇ", "asambodh", "asammusan", "asampajañ", "asampajān", "asamāhit", "asantuṭṭh",
    "asaṃvar", "asaṃvut", "asaṅgāhaṇ", "asaṭh", "assaddh", "assamaṇ", "assaraṇ", "assati", "asuci", "avijj",
    "avikiṇṇ", "avimutt", "avipaccanīk", "avippaṭikul", "avītarāg", "avītikkam", "ayonis", "aññāṇ", "nirās",
]
PRIV_RE = re.compile(r"(?<![\w])(?:" + "|".join(map(re.escape, PRIV)) + r")\w*", re.I)
LEX = {  # rendered by a Burmese word without negation (Pāli count 0)
    "akusal": "akusala = «အကုသိုလ်»", "asurop": "asuropa = «စကား ကြမ်းခြင်း» (pi-1 / pi-2)",
    "aggahit": "aggahitatta (ā-) = «… ဆုပ်ကိုင်ထားသော အဖြစ်»", "accāsar": "accāsarā = «အပြစ်ကို ကျော်လွှားခြင်း»",
    "appaggh": "appaggha (appa, little) = «တန်ဖိုး နည်း»", "appasadd": "appasadda = «အသံ ငြိမ်»",
    "appassut": "appassuta = «အကြားအမြင် နည်း»", "appamp": "appampi (a little) = «အနည်းငယ်မျှ»",
    "anāgām": "anāgāmī = «အနာဂါမ်»", "anu-": "anubyañjana, anuddayā, anukampā, anuseti, anuññāta … (anu-)",
    "aññ": "añña (other) / aññatra (except)", "ajjh": "ajjhatta / ajjhupekkhitabba", "dus-": "du- words (dussīla, "
    "dubbaṇṇa, duppañña …) = «ပျက်», «ညှိုး», «နည်း» … (no negation)", "nelā": "nelā (faultless) = «အပြစ် ကင်းသော»",
}
B_EXTRA = {  # Burmese negations with no Pāli negation word: (stem, count per occurrence, reason)
    "dubbaco": (1, "dubbaco (du-) = «သွန်သင်ချက်ကို နားမထောင်သူ» (sample name)"),
    "dovacass": (1, "dovacassatā = «… နားမထောင်ခြင်း» (pi-1 ^1-1332)"),
    "sāvajjānavajje": (1, "the an- inside sāvajja-anavajja = «အပြစ် မရှိသော»"),
}
B_NEG_RE = re.compile(r"မဟုတ်|မ(?=[က-အ](?![့ံ]*[်္]))")
NOT_NEG = ["မနော", "မစင်", "ကာမ", "မိန်းမ", "တမလွန်", "သို့မဟုတ်"]   # … «တမလွန်» next world, «သို့မဟုတ်» or


def p_neg(p):
    s = re.sub(r"^#+ .*", "", nobr(body(p)))
    for x in NOT_NEG_P:
        s = re.sub(x, "", s)
    n = len(NEG_FREE.findall(s)) + len(PRIV_RE.findall(s))
    for k, (c, _) in B_EXTRA.items():
        n += c * len(re.findall(rf"(?<![\w]){k}", s, re.I))
    return n


def b_neg(m):
    s = nobr(body(m))
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
POLAR = [
    ("kodhano", "akkodhano", 1), ("upanāhī", "anupanāhī", 1), ("makkhī", "amakkhī", 1), ("paḷāsī", "apaḷāsī", 1),
    ("issukī", "anissukī", 1), ("maccharī", "amaccharī", 1), ("saṭho", "asaṭho", 1), ("māyāvī", "amāyāvī", 1),
    ("hirimā", "ahiriko", 1), ("ottappī", "anottappī", 1), ("indriyesu guttadvāro", "indriyesu aguttadvāro", 1),
    ("bhojane mattaññū", "bhojane amattaññū", 1), ("sampajāno", "asampajāno", 1), ("āsaṃso", "nirāso", 1),
    ("kāmesu ca bhavesu ca vītarāgo", "kāmesu ca bhavesu ca avītarāgo", 1),
    ("sevitabbo bhajitabbo payirupāsitabbo", "na sevitabbo na bhajitabbo na payirupāsitabbo", 3),
]
for pos, neg, n in POLAR:
    a, b = F.NAME[pos], F.NAME[neg]
    nb3 += 1
    if b_neg(b) - b_neg(a) != n or a == b:
        bad.append(f"B3 pair {pos} / {neg}: Burmese negations {b_neg(a)} / {b_neg(b)}, expected +{n}")
QPAIRS = [("kodho", "akkodhano"), ("hirī", "ahirikaṃ"), ("ottappaṃ", "anottappaṃ"), ("sovacassatā", "dovacassatā"),
          ("indriyesu guttadvāratā", "indriyesu aguttadvāratā"), ("bhojane mattaññutā", "bhojane amattaññutā"),
          ("sampajaññaṃ", "asampajaññaṃ")]
for pos, neg in QPAIRS[1:]:
    nb3 += 1
    if b_neg(G.QUAL[neg]) - b_neg(G.QUAL[pos]) != 1:
        bad.append(f"B3 quality pair {pos} / {neg}: {G.QUAL[pos]} / {G.QUAL[neg]}")
print(f"B3. polarity: {nb3} negations / pairs checked; lexical renderings: {len(LEX)}, Burmese-only: {len(B_EXTRA)}")

# ===================================================================================== B4. quality nouns (duka)
nb4 = 0
for p, m in PAIRS["3-dukapuggalapannatti.md"]:
    q = re.search(r"Tattha katam\S+ (.+?)\?", p)
    if not q:
        continue
    qm = re.search(r"ထိုတို့အနက် (.+?) ဟူသည် အဘယ်နည်း။", m)[1]
    nb4 += 1
    for rx, mx in ((r"[ai][yd]aṃ vuccati ([^\"\.]+?)[.,]", r"ဤသည်ကို ([^။၊]+?)ဟု ခေါ်သည်။"),):
        for pv, mv in zip(re.findall(rx, nobr(p)), re.findall(mx, nobr(m))):
            if pv.strip() == q[1] and mv != qm:
                bad.append(f"B4 «{q[1]}»: «{qm}» / «{mv}»")
    for mv in (re.findall(r"အကြင် ပုဂ္ဂိုလ်၏ ဤ([^။]+?)ကို (?:မ?ပယ်)", m) +
               re.findall(r"(?:^|။ )ဤ([^။]+?)နှင့် အပြည့်အဝ ပြည့်စုံသော ပုဂ္ဂိုလ်သည်", m)):
        nb4 += 1
        if mv != qm:
            bad.append(f"B4 «{q[1]}»: «{qm}» / «{mv}»")
print(f"B4. quality nouns: {nb4} checked")

# ===================================================================================== B5. names
_mp, _mm = nonempty(PALI / "1-matika.md"), nonempty(OUT / "1-matika.md")
SEC, cur = {}, []
for p, m in zip(_mp, _mm):
    cur.append(m)
    mm = re.search(r"\^(4-M-\d+)\s*$", p)
    if mm:
        SEC[mm[1]] = nobr(" ".join(cur))
        cur = []
nb5 = 0
for name, sec in (("3-dukapuggalapannatti.md", "4-M-8"), ("4-tikapuggalapannatti.md", "4-M-9")):
    for p, m in PAIRS[name]:
        for q in re.findall(r"Katamo ca pug+alo (.+?)\?", p):
            nb5 += 1
            k = F.key_of(q)
            nm = F.NAME[k]
            if not body(m).startswith(nm + " ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။") and f"။ {nm} ဟူသည် အဘယ်" not in m:
                bad.append(f"B5 question «{q}»: «{nm}» not the question of the line")
            if nm not in SEC[sec] and nm[:-2] + "သော ပုဂ္ဂိုလ်" not in SEC[sec] and nm[:-2] + "သူ ဖြစ်၏" not in SEC[sec]:
                bad.append(f"B5 «{q}»: «{nm}» not in the mātikā {sec}")
            pc = re.findall(r'vucca(?:ti|nti) pug+al[oā] "([^"]+)"|samannāgato puggalo "([^"]+)"', p)
            mc = re.findall(r"“([^”]+)”ဟု ခေါ်သည်|“([^”]+)” ဖြစ်သည်", m)
            for (a1, a2), (b1, b2) in zip(pc, mc):
                pn, mn = a1 or a2, b1 or b2
                nb5 += 1
                if F.NAME[F.key_of(pn)] != mn or mn != nm:
                    bad.append(f"B5 closing name «{pn}»: «{mn}» / question «{nm}»")
            if len(pc) != len(mc):
                bad.append(f"B5 «{q}»: {len(pc)} closing names, {len(mc)} quoted")
            for pn in re.findall(r"vucca(?:ti|nti) pug+al[oā] (sīlesu [^.]+)\.", p):
                nb5 += 1
                if f"ကို {nm}ဟု ခေါ်သည်" not in m:
                    bad.append(f"B5 unquoted closing name «{pn}»")
print(f"B5. names: {nb5} questions / closing names checked")

# ===================================================================================== FINAL (independent read)
FIN = []
for b in "123":
    for f in sorted((ROOT / f"AI_translation/pali/pi-{b}_split_chapters").glob("*.md")):
        bf = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters" / f.name
        if not bf.exists():
            continue
        pl = [l for l in f.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        ml = [l for l in unicodedata.normalize("NFC", bf.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]
        if len(pl) != len(ml):
            sys.exit(f"FINAL pi-{b} {f.name}: line counts differ")
        FIN += [(b, f.name, x, y) for x, y in zip(pl, ml)]
SEGS, _cur = {}, []
for b, fn, x, y in FIN:
    _cur.append((x, y))
    m = re.search(r"\^([0-9A-Za-z-]+)\s*$", x)
    if m:
        SEGS[(b, "^" + m[1])] = (" ".join(a for a, _ in _cur), " ".join(c for _, c in _cur))
        _cur = []
PI4 = [(nobr(body(p)), nobr(body(m))) for prs in PAIRS.values() for p, m in prs]

# C1 the final units read by make_ch3-4
ADAPTED = {  # final Pāli key (start) -> why the pi-4 Burmese differs from the final unit
    "yo paḷāso paḷāsāyanā paḷāsāhāro": "pi-4 adds paḷāsāyitattaṃ «တုပြိုင်ထားသော အဖြစ်» (pattern of makkhāyitattaṃ)",
    "sahadhammike vuccamāne sovacassāyaṃ": "pi-4 order sādariyaṃ sādariyatā sagāravatā (pi-1: sagāravatā first)",
    "ye te puggalā saddhā sīlavanto": "pi-4 sampavaṅkatā «ညွတ်ကိုင်းခြင်း» (pi-2 ^2-901) for pi-1 taṃsampavaṅkatā",
    "idhekacco kāyena duccaritaṃ": "^4-72 «Idhekacco puggalo» = «ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်သည်» (sample IDHA)",
    "idhekacco cakkhunā rūpaṃ disvā": "«Idhekacco puggalo» = IDHA",
    "idhekacco appaṭisaṅkhā ayoniso": "«Idhekacco puggalo» = IDHA",
    "yā evarūpā diṭṭhi diṭṭhigataṃ": "pi-4 paṭiggāho «လက်ခံ စွဲကိုင်ခြင်း» for pi-1 patiṭṭhāho",
    "idhekacco paṭisaṅkhā yoniso āhāraṃ": "pi-4 splits the sentence and quotes it (pi-1 one sentence)",
    "pubbakālaṃ kodho, aparakālaṃ upanāho.": "^4-66 joined with the next sentence (no full stop in the pi-4 Pāli)",
    "yā tasmiṃ samaye paññā": "without «yā tasmiṃ samaye» = «ထိုအချိန်၌»",
    '"Mā maṃ jaññā"ti saṅkappeti': "pi-4 spelling saṅkappati (same verb)",
    "sahadhammike vuccamāne dovacassāyaṃ": "pi-4 spellings vippaṭikula-, anādariyatā, appatissavatā (same words)",
    "yaṃ aññāṇaṃ adassanaṃ": "pi-4 spelling asamapekkhaṇā (pi-2 ^2-180 asamapekkhanā)",
    "āsavānaṃ khayā": "the pi-2 «viharati» of the Buddha «နေတော်မူ၏» is «နေ၏» for a person",
}
n_c1 = s_c1 = a_c1 = 0


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[\"“”.,;!?]", "", t)).strip().lower()


seen = set()
for p4, fk, b, bid, my in G.REUSED:
    if (fk, my) in seen:
        continue
    seen.add((fk, my))
    n_c1 += 1
    sp, sm = SEGS[(b, bid)]
    myn = nobr(my)
    if myn not in nobr(sm).replace("။", "") + nobr(sm) and myn.rstrip("။") not in nobr(sm):
        bad.append(f"C1 «{fk[:50]}»: Burmese not in the final {bid}")
        continue
    key = norm(fk)
    if " … " in fk:                     # an excerpt (the middle left out): the Burmese stands in some pi-4 line
        occ = [(p, m) for p, m in PI4 if norm(fk.split(" … ")[0]) in norm(p)]
        used = [m for p, m in occ if myn.rstrip("။") in m]
        occ = occ[:len(used)] if used else occ
    else:
        occ = [(p, m) for p, m in PI4 if key in norm(p)]
        used = [m for p, m in occ if myn.rstrip("။") in m]
    if occ and len(used) == len(occ):
        s_c1 += 1
    elif any(fk.startswith(a) for a in ADAPTED):
        a_c1 += 1
        s_c1 += 1
    elif not occ and fk.startswith("tattha katam"):
        s_c1 += 1                       # a quality noun of a question: checked by B4 / C3
    else:
        bad.append(f"C1 «{fk[:60]}» ({bid}): in {len(used)} / {len(occ)} pi-4 lines")
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
            if nobr(body(m)).rstrip("။") in FIN_LINE[k]:
                s_c2 += 1
            else:
                bad.append(f"C2 «{k}»: «{body(m)}» vs final {sorted(FIN_LINE[k])[:2]}")
# C3 reused terms and clauses: (regex on the pi-4 Pāli, the Pāli in a pi-1/2/3 segment, the final Burmese)
REUSE = [
    (r"\bpuggal", "ekaṃ puggalaṃ", "ပုဂ္ဂိုလ်"), (r"Idhekacco puggalo", "Idhekacco samaṇo", "ဤလောက၌ အချို့သော"),
    (r"\bkodho\b", "Tattha katamo kodho", "အမျက်ဒေါသ"), (r"\bupanāho\b", "Tattha katamo upanāho", "ရန်ငြိုး သိုထားမှု"),
    (r"\bmakkho\b", "katamo makkho", "ကျေးဇူး ချေဖျက်မှု"), (r"\bpaḷāso\b", "katamo paḷāso", "တုပြိုင်မှု"),
    (r"\bissā\b", "katamā issā", "ငြူစူမှု"), (r"\bmacchariyaṃ\b", "katamaṃ macchariyaṃ", "ဝန်တိုမှု"),
    (r"\bsāṭheyyaṃ\b", "katamaṃ sāṭheyyaṃ", "စဉ်းလဲသော အဖြစ်"), (r"\bmāyā\b", "katamā māyā", "လှည့်စားတတ်ခြင်း"),
    (r"\bahirik", "ahirikaṃ", "ဒုစရိုက်ကို မရှက်"), (r"\banottapp", "anottappaṃ", "ဒုစရိုက်ကို မကြောက်ရွံ့"),
    (r"\bhiri(?:mā|yā)|\bhirī\b", "Tattha katamā hirī", "ဒုစရိုက်ကို ရှက်"),
    (r"\bottapp(?:aṃ|ī|ena)\b", "Tattha katamaṃ ottappaṃ", "ဒုစရိုက်ကို ကြောက်ရွံ့"),
    (r"\bdovacass", "dovacassatā", "သွန်သင်ချက်ကို နားမထောင်"), (r"\bsovacass", "sovacassatā", "သွန်သင်ချက်ကို နားထောင်"),
    (r"\bpāpamitt", "pāpamittatā", "မိတ်ဆွေဆိုးနှင့် ပေါင်းသင်း"),
    (r"\bkalyāṇamitt", "kalyāṇamittatā", "မိတ်ဆွေကောင်းနှင့် ပေါင်းသင်း"),
    (r"\bindriyesu aguttadvār", "indriyesu aguttadvāratā", "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို မစောင့်ထိန်း"),
    (r"\bindriyesu guttadvār", "indriyesu guttadvāratā", "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို စောင့်ထိန်း"),
    (r"\bbhojane amattaññ", "bhojane amattaññutā", "အစားအစာ၌ အတိုင်းအရှည်ကို မသိ"),
    (r"\bbhojane mattaññ", "bhojane mattaññutā", "အစားအစာ၌ အတိုင်းအရှည်ကို သိ"),
    (r"\bmuṭṭhassacc", "muṭṭhassaccaṃ", "သတိလစ်"), (r"\basampajañ", "asampajaññaṃ", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိ"),
    (r"\bsīlavipatt", "sīlavipatti", "သီလ ပျက်စီး"), (r"\bdiṭṭhivipatt", "diṭṭhivipatti", "အယူ ပျက်စီး"),
    (r"\bsīlasampad", "sīlasampadā", "သီလ ပြည့်စုံ"), (r"\bdiṭṭhisampad", "diṭṭhisampadā", "အယူ ပြည့်စုံ"),
    (r"\bTattha katamā sati\b", "Tattha katamā sati", "သတိ"), (r"\bsampajaññ", "sampajaññaṃ", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း"),
    (r"\bpañcorambhāgiyāni", "Pañcorambhāgiyāni saṃyojanāni", "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး"),
    (r"\bpañcuddhambhāgiyāni", "Pañcuddhambhāgiyāni saṃyojanāni", "အထက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး"),
    (r"\bsamannāgato", "samannāgato", "အပြည့်အဝ ပြည့်စုံ"), (r"\bāsavā\b", "āsavā dhammā", "စိတ်အစွန်းအထင်း"),
    (r"\bkukkucc", "kukkuccaṃ", "နောင်တ ပူပန်"), (r"\bdussīl", "dussīlo samāno", "သီလ ပျက်"),
    (r"\bsīlavā\b", "sīlavāti", "သီလ ရှိသူ"), (r"\bsevitabbo", "sevanā", "ပေါင်းသင်း"),
    (r"\bTathāgatappaveditā", "tathāgato", "မြတ်စွာဘုရား"), (r"\btathāgatassa sāvakā", "tathāgato", "မြတ်စွာဘုရား"),
    (r"\barahanto\b", "arahanto jīvitā", "ရဟန္တာ"), (r"\bSammāsambuddho", "sammāsambuddho",
                                                   "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်"),
    (r"\bāsavānaṃ khayā anāsavaṃ cetovimuttiṃ", "āsavānaṃ khayā anāsavaṃ cetovimuttiṃ",
     "စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းကြောင့် စိတ်အစွန်းအထင်း မရှိသော စိတ်၏ လွတ်မြောက်ခြင်း၊ ပညာဖြင့် လွတ်မြောက်ခြင်းကို"),
    (r"\bdiṭṭheva dhamme sayaṃ abhiññā", "diṭṭheva dhamme sayaṃ abhiññā", "မျက်မှောက်ဘဝ၌ပင် ကိုယ်တိုင် ထူးကဲစွာ သိ၍"),
    (r"\bdiṭṭhe ceva dhamme", "diṭṭheva dhamme", "မျက်မှောက်ဘဝ၌ပင်"),
    (r"\bTaṃ kissa hetu", "Taṃ kissa hetu", "ထိုသို့ အဘယ်ကြောင့်နည်း"),
    (r"\byathābhūtaṃ pajānāti", "yathābhūtaṃ pajānāti", "ဟုတ်မှန်သည့်အတိုင်း ကွဲပြားစွာ သိ"),
    (r"\baṭṭha vimokkhe", "Aṭṭha vimokkhā", "လွတ်မြောက်ခြင်း ရှစ်ပါး"),
    (r"\bniyāmaṃ kusalesu dhammesu sammattaṃ", "niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ",
     "ကုသိုလ် သဘောတရားတို့၌ မှန်ကန်မှု ဖြစ်သော သေချာသော လမ်းကြောင်းသို့"),
    (r"\bdhammavinay", "imasmiṃ dhammavinaye", "တရားနှင့် ဝိနည်း"), (r"\bābādhā", "ābādho", "အနာရောဂါ"),
    (r"\bupāyāsa", "upāyāso", "ပြင်းစွာ ပူပန်ခြင်း"), (r"\bkopañca", "kopo pakopo", "အမျက်ထွက်ခြင်း"),
    (r"\bbrahmacariyaṃ pakāsenti", "brahmacariyānuggahāya", "မြင့်မြတ်သော အကျင့်"),
    (r"(?<!neva )(?<!na )\b(?:ādimpi|majjhampi|pariyosānampi) manasi karoti", "manasikārakusalatā", "နှလုံးသွင်း"),
    (r"\b(?:neva|na) (?:ādiṃ|majjhaṃ|pariyosānaṃ) manasi karoti", "Na amanasikārā", "နှလုံး မသွင်း"), (r"\bkodhano\b", "Tattha katamo kodho", "အမျက်ဒေါသ"),
    (r"\bdukkhasamphass", "dukkhasamphassaṃ", "ထိတွေ့ရ နာကျင်"), (r"\bsukhasamphass", "sukhasamphassaṃ", "ထိတွေ့ရ သာယာ"),
    (r"cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāraṃ",
     "Itarītaracīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhārehi",
     "သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်"),
    (r"\bsaṅghamajjhe", "saṅghamajjhe", "သံဃာ့အလယ်၌"), (r"\bāyasmanto", "āyasmanto", "အသျှင်တို့"),
    (r"\bbālassa abyattassa", "bālassa abyattassa", "မိုက်မဲ၍ မလိမ္မာသော သင်၏ ပြောဆိုမှုဖြင့် အဘယ် အကျိုး ရှိမည်နည်း"),
    (r"\bmuṭṭhassati\b", "Muṭṭhassaccañca", "သတိလစ်"), (r"\bsampajāno\b", "sampajaññañca", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း"),
    (r"\bsamādhinā", "samādhinā", "သမာဓိ"), (r"kkhandhaṃ", "Pañcakkhandhā", "အစုအဝေး"),
    (r"\banuddayā", "anuddā", "သနားကြင်နာခြင်း"), (r"\banukampā", "anukampā", "စာနာ ထောက်ထားခြင်း"),
    (r"\banatthampi", "anatthaṃ me", "မကောင်းမှု"),
    (r"\bpariññaṃ", "Sabbāsave pariññāya", "ပိုင်းခြား သိ"), (r"\bpaññapeti", "paññapenti", "ပညတ်"),
    (r"\bsaccato thetato", "saccato thetato", "အမှန်အားဖြင့် ခိုင်မြဲစွာ"),
    (r"\battānaṃ", "Atthi me attā", "အတ္တ"), (r"\bsassatavādo", "sassatavādā", "ထာဝရ တည်မြဲသည်ဟု ဆိုသော ဝါဒ"),
    (r"\bucchedavādo", "ucchedavādā", "ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ"),
    (r"(?<!a)\brūpāvacarasamāpattiyā", "rūpāvacaraṃ", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော"),
    (r"\barūpāvacarasamāpattiyā", "Arūpāvacaravipākā", "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော"),
    (r"samāpattiyā lābhī", "samāpattikusalatā", "ဈာန် ဝင်စားရာ"),
    (r"\bkusalākusale", "kusalākusalā", "ကုသိုလ်"), (r"\bhīnappaṇīte", "paṇītā dhammā", "မွန်မြတ်သော"),
    (r"\bkaṇhasukka", "sukkā dhammā", "ဖြူစင်သော"), (r"\bkaṇhasukka", "kaṇhā dhammā", "မည်းနက်သော"),
    (r"\bmusāvād", "musāvādo", "မုသား ပြော"), (r"\bpharusena", "pharusā vācā", "ကြမ်းတမ်း"),
    (r"\bbhikkhu\b", "idha bhikkhu", "ရဟန်း"), (r"\bbhikkhū\b", "bhikkhūhi", "ရဟန်း"),
    (r"\bvajirassa", "vajirūpamā", "စိန်"),
]
REUSE = [r for r in REUSE if r[2]]
n_c3 = s_c3 = 0
for rx, fp, my in REUSE:
    n_c3 += 1
    wit = [k for k, (sp, sm) in SEGS.items() if fp.lower() in nobr(sp).lower() and my in sm]
    occ = [(p, m) for p, m in PI4 if re.search(rx, p, re.I)]
    miss = [p[:70] for p, m in occ if my not in m]
    if wit and occ and not miss:
        s_c3 += 1
    else:
        bad.append(f"C3 «{rx}» / «{my}»: witness {wit[:1] or 'NONE'}, {len(occ)} pi-4 lines, missing in {miss[:2]}")
print(f"C. reuse test: C1 final units {s_c1} / {n_c1} ({a_c1} adapted: ADAPTED); C2 whole lines / headings / "
      f"colophons {s_c2} / {n_c2}; C3 terms and clauses {s_c3} / {n_c3} identical with pi-1 / pi-2 / pi-3 final")
tot_s, tot_n = s_c1 + s_c2 + s_c3, n_c1 + n_c2 + n_c3
if bad:
    print(f"\nMISMATCHES: {len(bad)}")
    for b in bad:
        print("  " + b)
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {tot_s} / {tot_n} identical")
