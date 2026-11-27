"""Check of the pi-4 Burmese zero-shot chapters 6 … 11 against the Pāli (adapted from check_sample.py).

usage: python3 -I -X utf8 check_ch6-11.py
  A. regeneration: make_ch6-11's tables + my4_formulas.translate_line() on every Pāli line give exactly the files.
  B. per line, with this script's own patterns (not those of my4_formulas):
     B1 typography: no «?», «।», «:-», no Zawgyi-like «ေ» at word start, NFC; every Pāli sentence end («.» / «?»,
        brackets and IDs removed) is one «။»; a question line ends «နည်း။»; quotes “ ” balanced per line;
     B2 numbers: the numbers of the Pāli (cardinals, number stems) = the Burmese numbers before a classifier;
     B3 polarity: the negations of each line, Pāli (na, no, neva, nap-, nār-, nāparaṃ, the privative words of PRIV)
        = Burmese («မဟုတ်», the negative «မ» before a verb), apart from the listed lexical renderings;
     B5 names: every «Katamo ca puggalo X?» has the table name of X (the mātikā name, sample B5) in its question
        and in its closing «“X”ဟု ခေါ်သည်»; every «Kathañca puggalo X?» question and «Evaṃ puggalo X.» closing
        carry the same verb phrase; the chakka persons «X tena daṭṭhabbo» use the table names.
  C. reuse test: C3 every reused term / clause of REUSE: a pi-1 / pi-2 / pi-3 rails segment has both the Pāli and
     the Burmese (witness, read here independently), and every line of these chapters with that Pāli has that
     Burmese; C4 every line of these chapters whose Pāli (ID removed) is identical to another line of pi-4
     (sample chapters or these) has the identical Burmese. Prints n / n identical.
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

G = importlib.import_module("make_ch6-11")       # installs the tables; writes nothing at import
F = G.F
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
NAMES = G.NAMES_OUT
SAMPLE = ["preamble.md", "1-matika.md", "2-ekakapuggalapannatti.md"]
ID = re.compile(r" ?\^[0-9A-Za-z-]+\s*$")
bad = []


def nonempty(p):
    return [l for l in unicodedata.normalize("NFC", p.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]


def body(l):
    return ID.sub("", l).strip()


def nobr(s):
    return re.sub(r"\s*\[[^\]]*\]", "", s)


PAIRS = {}
for n in NAMES + SAMPLE:
    a, b = nonempty(PALI / n), nonempty(OUT / n)
    if len(a) != len(b):
        bad.append(f"{n}: line count differs")
    PAIRS[n] = list(zip(a, b))

# ===================================================================================== A. regeneration
for name in NAMES:
    raw = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    regen = "\n".join(F.translate_line(l) for l in raw).rstrip("\n") + "\n"
    if unicodedata.normalize("NFC", regen) != (OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A {name}: file differs from the regenerated text")
print(f"A. regeneration: {len(NAMES) - sum(1 for b in bad if b.startswith('A '))} / {len(NAMES)} files identical")

# ===================================================================================== B1. typography
nb1 = 0
for name in NAMES:
    raw = (OUT / name).read_text(encoding="utf-8")
    if raw != unicodedata.normalize("NFC", raw):
        bad.append(f"B1 {name}: not NFC")
    for ch in ("?", "।", ":-", "⟦"):
        if ch in raw:
            bad.append(f"B1 {name}: contains {ch}")
    if re.search(r"(^|[\s“‘(])ေ", raw, re.M):
        bad.append(f"B1 {name}: Zawgyi-like «ေ» at word start")
    for i, (p, m) in enumerate(PAIRS[name]):
        nb1 += 1
        pb, mb = nobr(body(p)), body(m)
        np_ = len(re.findall(r'[.?]"?(?=\s|$)', re.sub(r"^#+ .*", "", pb)))
        if np_ != mb.count("။"):
            bad.append(f"B1 {name}:{i + 1}: {np_} Pāli sentence ends, {mb.count('။')} «။»")
        if pb.endswith("?") and not mb.endswith("နည်း။"):
            bad.append(f"B1 {name}:{i + 1}: question without «နည်း။»")
        if mb.count("“") != mb.count("”") or mb.count("‘") != mb.count("’"):
            bad.append(f"B1 {name}:{i + 1}: quotes unbalanced")
print(f"B1. typography: {nb1} lines checked")

# ===================================================================================== B2. numbers
P_NUM = [
    (r"cattār[oi]", 4), (r"dve", 2), (r"tayo", 3), (r"tīṇi", 3), (r"tiṇṇaṃ", 3), (r"pañca", 5), (r"pañcime", 5),
    (r"pañcannaṃ", 5), (r"cha", 6), (r"satta", 7), (r"aṭṭha", 8), (r"nava", 9), (r"dasa", 10),
    (r"sattakkhattu\w*", 7), (r"ubhatobhāga\w*", 2), (r"ekabīj\w*", 1), (r"ekāsanikā", 1), (r"tecīvarikā", 3),
    (r"sakiṃ", 1), (r"sakideva", 1),
] + [(rf"{s}(?:ṃ|niddeso|puggalapaññatti)", n) for s, n in (
    ("pañcaka", 5), ("chakka", 6), ("sattaka", 7), ("aṭṭhaka", 8), ("navaka", 9), ("dasaka", 10))]
P_NUM_RE = [(re.compile(rf"(?<![\w]){rx}(?![\w])", re.I), n) for rx, n in P_NUM]
B_NUM = {"တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6, "ခုနစ်": 7, "ရှစ်": 8, "ကိုး": 9, "ဆယ်": 10}
B_NUM_RE = re.compile(r"(?<![က-႟])(" + "|".join(sorted(map(re.escape, B_NUM), key=len, reverse=True)) +
                      r")(?=ယောက်|ပါး|ကြိမ်|မျိုး|စေ့|ခု|ထည်|ဖက်|ထိုင်|နှစ်)")
NOT_NUM = ["သူတစ်ပါး", "ကမ်းတစ်ဖက်", "တစ်စိတ်တစ်ပိုင်း"]
nb2 = 0
for name in NAMES:
    for i, (p, m) in enumerate(PAIRS[name]):
        s = re.sub(r"^\(\d+\) ", "", nobr(body(p)))
        a = Counter(n for rx, n in P_NUM_RE for _ in rx.findall(s))
        t = re.sub(r"\[[^\]]*\]", "", re.sub(r"^#+ ", "", body(m)))
        for x in NOT_NUM:
            t = t.replace(x, "")
        b = Counter(B_NUM[x] for x in B_NUM_RE.findall(t))
        nb2 += sum(a.values())
        if a != b:
            bad.append(f"B2 {name}:{i + 1}: numbers Pāli {dict(a)} / Burmese {dict(b)}")
print(f"B2. numbers: {nb2} numbers checked")

# ===================================================================================== B3. polarity
NEG_FREE = re.compile(r"(?<![\w])(?:na|no|neva|nappajānāti|nappavaḍḍhanti|nāparaṃ)(?![\w])", re.I)
PRIV = ["aparisesā", "ananussutesu", "anabhisambujjhati", "anāgantā", "asaṅkhār", "avijjā", "akathaṃkathī",
        "abyāpann", "anuddhato", "anaṅgaṇe", "āneñjappatte", "appaccakkhāya", "anāvikatvā", "anāsav", "anāvattidhammo",
        "avinipātadhammo"]
PRIV_RE = re.compile(r"(?<![\w])(?:" + "|".join(map(re.escape, PRIV)) + r")\w*", re.I)
LEX = {"avaṇṇ": "avaṇṇa = «ကဲ့ရဲ့»", "anāgāmi": "anāgāmī = «အနာဂါမ်», anāgāmiphala = «အနာဂါမိဖိုလ်»",
       "akaniṭṭh": "Akaniṭṭha (name)", "akusal": "akusala = «အကုသိုလ်»", "avajānāti": "ava- (not privative)",
       "anupubbena": "anu- (not privative)", "anusāsiyamānā": "anu- (not privative)"}
B_EXTRA = {"nesajjikā": 1, "khalupacchābhattikā": 1, "lolo": 1, "antarāparinibbāy": 1}   # Burmese-only negations
P_COMPOUND = {"sāvajjānavajj": 1}                                                   # negation inside a compound
B_NEG_RE = re.compile(r"မဟုတ်|မ(?=[က-အ](?![့ံ]*[်္]))")
NOT_NEG = ["မနော", "မစင်", "ကာမ", "မိန်းမ", "ဆုံးမ", "သူမ"]   # ဆုံးမ = admonish (ovadati); သူမ = she (harmonise B3)
nb3 = 0
for name in NAMES:
    for i, (p, m) in enumerate(PAIRS[name]):
        s = re.sub(r"^#+ .*", "", nobr(body(p)))
        a = len(NEG_FREE.findall(s)) + len(PRIV_RE.findall(s))
        for k, c in list(B_EXTRA.items()) + list(P_COMPOUND.items()):
            a += c * len(re.findall(rf"(?<![\w]){k}", s, re.I))
        t = re.sub(r"\[[^\]]*\]", "", body(m))
        for x in NOT_NEG:
            t = t.replace(x, "")
        b = len(B_NEG_RE.findall(t))
        nb3 += a
        if a != b:
            bad.append(f"B3 {name}:{i + 1}: negations Pāli {a} / Burmese {b}")
print(f"B3. polarity: {nb3} negations checked; lexical renderings: {len(LEX)}, Burmese-only: {len(B_EXTRA)}")

# ===================================================================================== B5. names
nb5 = 0
for name in NAMES:
    for p, m in PAIRS[name]:
        pb = nobr(body(p))
        for k in re.findall(r"Katamo ca puggalo ([^?…]+)\?", pb):
            nb5 += 1
            if f"{F.NAME[F.key_of(k)]} ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။" not in m:
                bad.append(f"B5 question «{k}»")
        for q, k in re.findall(r'[Aa]yaṃ vuccati puggalo ("?)([^".]+)"?\.', pb):
            nb5 += 1
            nm = F.NAME[F.key_of(k)]        # quotes only where the Pāli has them (harmonise A2 / B1)
            if (f"“{nm}”ဟု ခေါ်သည်" if q else f"ဤပုဂ္ဂိုလ်ကို {nm}ဟု ခေါ်သည်") not in m:
                bad.append(f"B5 closing «{k}»")
        for k in re.findall(r"Kathañca puggalo ([^?]+)\?", pb):
            nb5 += 1
            v = G.KATHA[k]
            if f"ပုဂ္ဂိုလ်သည် အဘယ်သို့ {v}သနည်း။" not in m or f"ဤသို့ ပုဂ္ဂိုလ်သည် {v}၏။" not in m:
                bad.append(f"B5 Kathañca «{k}»")
        for k in re.findall(r", (sammāsambuddho|paccekasambuddho|anāgāmī) tena daṭṭhabbo", pb):
            nb5 += 1
            if f"{F.NAME[k]}{G.TENA}" not in m:
                bad.append(f"B5 tena «{k}»")
print(f"B5. names: {nb5} questions / closings / verb phrases checked")

# ===================================================================================== C. reuse test
SEGS, _cur = {}, []
for bk in "123":
    for f in sorted((ROOT / f"AI_translation/pali/pi-{bk}_split_chapters").glob("*.md")):
        bf = ROOT / f"AI_translation/burmese/pi-{bk}-burmese-plain-rails_split_chapters" / f.name
        if not bf.exists():
            continue
        pl, ml = nonempty(f), nonempty(bf)
        if len(pl) != len(ml):
            sys.exit(f"FINAL pi-{bk} {f.name}: line counts differ")
        for x, y in zip(pl, ml):
            _cur.append((x, y))
            mm = re.search(r"\^([0-9A-Za-z-]+)\s*$", x)
            if mm:
                SEGS[(bk, mm[1])] = (" ".join(a for a, _ in _cur), " ".join(c for _, c in _cur))
                _cur = []
REUSE = [  # (regex on the Pāli of these chapters, Pāli in a pi-1/2/3 segment, final Burmese)
    (r"\bpuggal", "ekaṃ puggalaṃ", "ပုဂ္ဂိုလ်"), (r"\bariyamaggaṃ", "Ariyamaggaṃ", "အရိယာ မဂ်"),
    (r"\baṭṭha vimokkhe", "Aṭṭha vimokkhā", "လွတ်မြောက်ခြင်း ရှစ်ပါး"), (r"\bāsavā\b", "āsavā dhammā", "စိတ်အစွန်းအထင်း"),
    (r"\bāsavānaṃ khay", "āsavānaṃ khayaṃ", "စိတ်အစွန်းအထင်းတို့ ကုန်ခန်း"),
    (r"\btiṇṇaṃ saṃyojanānaṃ", "Tīṇi saṃyojanāni", "နှောင်ကြိုး သုံးပါး"),
    (r"\borambhāgiyānaṃ saṃyojanānaṃ", "Pañcorambhāgiyāni saṃyojanāni",
     "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး"),
    (r"\bopapātiko", "Opapātikānaṃ", "အလိုအလျောက် ပေါ်လာ"),
    (r"\bsotāpattiphal", "sotāpattiphale", "သောတာပတ္တိဖိုလ်"), (r"\bsakadāgāmiphal", "sakadāgāmiphale", "သကဒါဂါမိဖိုလ်"),
    (r"\banāgāmiphal", "anāgāmiphale", "အနာဂါမိဖိုလ်"), (r"\barahattaphal", "arahattaphale", "ရဟန္တာဖိုလ်"),
    (r"\bcetovimuttiṃ paññāvimuttiṃ", "cetovimuttiṃ paññāvimuttiṃ", "စိတ်၏ လွတ်မြောက်ခြင်း၊ ပညာဖြင့် လွတ်မြောက်ခြင်း"),
    (r"\bdiṭṭhe(?:va| ceva) dhamme", "diṭṭheva dhamme", "မျက်မှောက်ဘဝ၌ပင်"),
    (r"\buppannā pāpakā", "uppannā", "ဖြစ်ပေါ်ပြီးသော"), (r"\bpāpakā akusalā", "pāpakā", "ယုတ်မာသော"),
    (r"\bakusalā dhammā", "akusalā dhammā", "အကုသိုလ် သဘောတရား"), (r"\bnirujjhanti", "nirujjhanti", "ချုပ်ငြိမ်း"),
    (r"\byathābhūtaṃ (?:nap)?pajānāti", "yathābhūtaṃ pajānāti", "ဟုတ်မှန်သည့်အတိုင်း ကွဲပြားစွာ"),
    (r"\bdukkhasamudayo", "dukkhasamudayo", "ဒုက္ခ ဖြစ်ပေါ်ခြင်း"), (r"\bdukkhanirodho", "dukkhanirodho", "ဒုက္ခ ချုပ်ငြိမ်းခြင်း"),
    (r"\bdukkhanirodhagāminī paṭipadā", "dukkhanirodhagāminī paṭipadā", "ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်"),
    (r"\btathāgatappaveditā", "tathāgato", "မြတ်စွာဘုရား"), (r"\bpaññindriyaṃ", "paññindriyaṃ", "ပညာ၏ စွမ်းရည်"),
    (r"\bsaddhindriyaṃ", "saddhindriyaṃ", "ယုံကြည်မှု၏ စွမ်းရည်"), (r"\bbhāveti", "bhāveti", "ပွားများ"),
    (r"\bkusalesu dhammesu", "kusalesu dhammesu", "ကုသိုလ် သဘောတရားတို့၌"), (r"\bsaddhā\b", "saddhā", "ယုံကြည်မှု"),
    (r"\bhirī\b", "hirī", "ဒုစရိုက်ကို ရှက်မှု"), (r"\bottappaṃ", "ottappaṃ", "ဒုစရိုက်ကို ကြောက်ရွံ့မှု"),
    (r"\bvīriyaṃ", "vīriyaṃ", "ဝီရိယ"), (r"\bkāmāsav", "kāmāsavo", "ကာမ စိတ်အစွန်းအထင်း"),
    (r"\bbhavāsav", "bhavāsavo", "ဘဝ စိတ်အစွန်းအထင်း"), (r"\bavijjāsav", "avijjāsavo", "အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း"),
    (r"\bbrahmacariy", "brahmacariy", "မြင့်မြတ်သော အကျင့်"), (r"\bjāti\b", "jāti", "မွေးဖွားခြင်း"),
    (r"\bsikkhaṃ paccakkhāya", "sikkhaṃ paccakkhāya", "သိက္ခာကို စွန့်၍ လူဘောင်သို့ ပြန်လည်"),
    (r"\bbhikkhu", "bhikkhu", "ရဟန်း"), (r"\b[Aa]raññagat", "Araññagato", "တောသို့ ရောက်"),
    (r"\bpallaṅkaṃ ābhujitvā", "pallaṅkaṃ ābhujitvā", "ထက်ဝယ်ဖွဲ့ခွေ၍"),
    (r"\babhijjhaṃ loke pahāya", "abhijjhaṃ loke pahāya", "လောက၌ သူ့ဥစ္စာကို လိုချင်ခြင်းကို ပယ်၍"),
    (r"\bime pañca nīvaraṇe", "ime pañca nīvaraṇe", "ဤအတားအဆီး ငါးပါး"),
    (r"\bvivicceva kāmehi", "vivicceva kāmehi", "ကာမတို့မှ ကင်းဆိတ်၍သာ"),
    (r"\bvitakkavicārānaṃ vūpasamā", "vitakkavicārānaṃ vūpasamā",
     "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်းကြောင့်"),
    (r"kukkucc", "kukkuccaṃ", "နောင်တ ပူပန်မှု"), (r"\bvicikicch", "vicikicchā", "ယုံမှားမှု"),
    (r"\bthinamiddh", "thinamiddh", "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု"),
    (r"\bkhīraṃ", "khīraṃ", "နွားနို့"), (r"\bdadhi\b", "dadhi", "နို့ချဉ်"), (r"\bnavanītaṃ", "navanītaṃ", "ထောပတ်"),
    (r"\bsappi\b", "sappi", "ထောပတ်ကြည်"), (r"\bgāme\b", "gāmaṃ", "ရွာ"), (r"\bnigame\b", "nigamaṃ", "နိဂုံး"),
    (r"\bitth[iī]ṃ?\b", "itthī", "မိန်းမ"), (r"\bpāpiccho icchāpakato", "pāpiccho icchāpakato", G.PAPICCHA),
    (r"\byena ?kāmaṃ pakkamati", "yenakāmaṃ pakkamati", "အလိုရှိရာသို့ ထွက်သွား"),
    (r"\bāsavānaṃ khayā anāsavaṃ", "āsavānaṃ khayā anāsavaṃ", "စိတ်အစွန်းအထင်း မရှိသော စိတ်၏ လွတ်မြောက်ခြင်း"),
    (r"\bSeyyathāpi", "Seyyathāpi", "ဥပမာအားဖြင့်"), (r"\bPuna caparaṃ", "Puna caparaṃ", "တစ်ဖန်"),
    (r"\bcīvarapiṇḍapāta", "cīvarapiṇḍapāta", "သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ"),
    (r"\bbuddhehi", "buddhā", "ဘုရားရှင်"), (r"\bkaṇha", "kaṇhā dhammā", "မည်းနက်"),
    (r"ppaṇīte\b", "paṇītā dhammā", "မွန်မြတ်"), (r"\bsamāhite\b", "samāhit", "တည်ကြည်"),
    (r"\bsammāsambuddho", "sammāsambuddho", "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်"),
    (r"\bavasesā\b", "avasesā", "ကြွင်းကျန်သော"), (r"\bsamannāgat", "samannāgato", "အပြည့်အဝ ပြည့်စုံ"),
    (r"\bsāvakapāram", "sāvako", "တပည့်"), (r"\bsaccāni", "saccāni", "သစ္စာ"), (r"\bāyasm", "āyasmanto", "အသျှင်"),
    (r"\bsantuṭṭh", "asantuṭṭhassa", "ရောင့်ရဲမှု"), (r"\bvisīdati|\bsaṃsīdati", "", ""),
]
REUSE = [r for r in REUSE if r[1]]
n_c3 = s_c3 = 0
MINE = [(nobr(body(p)), body(m)) for n in NAMES for p, m in PAIRS[n]]
for rx, fp, my in REUSE:
    n_c3 += 1
    wit = [k for k, (sp, sm) in SEGS.items() if fp.lower() in nobr(sp).lower() and my in sm]
    occ = [(p, m) for p, m in MINE if re.search(rx, p, re.I)]
    miss = [p[:70] for p, m in occ if my not in m]
    if wit and occ and not miss:
        s_c3 += 1
    else:
        bad.append(f"C3 «{rx}» / «{my}»: witness {wit[:1] or 'NONE'}, {len(occ)} lines, missing in {miss[:2]}")
# C4 identical Pāli lines within pi-4 (sample + these chapters)
ALL = {}
for n in SAMPLE + NAMES:
    for p, m in PAIRS[n]:
        ALL.setdefault(body(p), set()).add(body(m))
n_c4 = s_c4 = 0
for n in NAMES:
    for p, m in PAIRS[n]:
        k = body(p)
        if sum(1 for n2 in SAMPLE + NAMES for p2, _ in PAIRS[n2] if body(p2) == k) > 1:
            n_c4 += 1
            if len(ALL[k]) == 1:
                s_c4 += 1
            else:
                bad.append(f"C4 «{k[:60]}»: {len(ALL[k])} renderings")
print(f"C. reuse test: C3 terms and clauses {s_c3} / {n_c3} identical with pi-1 / pi-2 / pi-3 final; "
      f"C4 repeated Pāli lines within pi-4 {s_c4} / {n_c4}")
# consistency pass (harmonise-notes.md): forms changed on purpose against pi-1 / pi-2 / pi-3 (no longer reuse items)
HARMONISED = []          # B4 revised: tathāgata = pi-2 «မြတ်စွာဘုရား» again (a reuse item, C3)
n_h = s_h = 0
for rx, my, why in HARMONISED:
    n_h += 1
    occ = [(p, m) for p, m in MINE if re.search(rx, p)]
    miss = [p[:70] for p, m in occ if my not in m]
    if occ and not miss:
        s_h += 1
    else:
        bad.append(f"H «{rx}» / «{my}» ({why}): {len(occ)} lines, missing in {miss[:2]}")
print(f"H. harmonised forms (changed on purpose in the consistency pass): {s_h} / {n_h}")
tot_s, tot_n = s_c3 + s_c4, n_c3 + n_c4
if bad:
    print(f"\nMISMATCHES: {len(bad)}")
    for b in bad:
        print("  " + b)
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {tot_s} / {tot_n} identical")
