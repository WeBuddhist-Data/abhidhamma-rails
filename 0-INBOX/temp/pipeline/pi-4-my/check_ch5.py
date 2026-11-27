"""Check of the pi-4 Burmese zero-shot chapter 5-catukkapuggalapannatti against the Pāli (adapted from check_sample.py).

usage: python3 -I -X utf8 check_ch5.py
  A. regeneration: make_ch5.generate() (its tables + my4_formulas.translate_line()) gives exactly the file.
  B. per line, parsed here with its own patterns (not those of the generator):
     B1 typography: no «?», «।», «:-», no Zawgyi-like «ေ» at word start, NFC; every Pāli sentence end («.» «?» «!»,
        brackets removed) is one «။» outside brackets (same count per line); every Pāli «?» is one «နည်း။»;
     B2 numbers: cardinals (all cases, number stems in compounds: ekāgāriko, dvīhika, sattāhika, ekabhattiko,
        sāyatatiyaka, the jāti list …) against the Burmese numbers before a classifier (and «တစ်ရာ / တစ်ထောင် /
        တစ်သိန်း»), same multiset per line; ordinals (paṭhama … catuttha) against ပထမ … စတုတ္ထ;
     B3 polarity: the negations of each line (Pāli: na, no, neva, naheva, nopi, nap-, nā- compounds and the
        privative words of PRIV) against the Burmese negations («မဟုတ်», the negative «မ» before a verb), same count
        per line; and the polarity pairs of the new names (X / neva X no Y …);
     B5 names: (a) «Katamo ca puggalo X?» name = its closing name «ဤပုဂ္ဂိုလ်ကို X ဟု ခေါ်သည်» = NAME table =
        the Burmese mātikā line (1-matika) that has this Pāli name; (b) «Kathañca puggalo X hoti?» predicate = its
        closing «Evaṃ puggalo X hoti.» predicate, and = the mātikā predicate / name of the type, or, for a member of a
        simile group, = the names line «Katame cattāro? …» of its group; (c) every simile names the group's object.
  C. reuse test (pi-1 / pi-2 / pi-3 FINAL rails texts, read here independently): C1 whole Pāli lines / headings /
     colophons that also occur in pi-1/2/3 have their Burmese; C2 every reused term and clause of REUSE: a rails
     segment has both the Pāli and the Burmese (witness), and every ch5 line with that Pāli has that Burmese.
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
import make_ch5 as G  # noqa: E402  (installs the tables in memory; writes nothing at import)

F = G.F
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
NAME = G.NAME_OUT
ID = re.compile(r" ?\^[0-9A-Za-z-]+\s*$")
bad = []


def nonempty(p):
    return [l for l in unicodedata.normalize("NFC", p.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]


def body(l):
    return ID.sub("", l).strip()


def nobr(s):
    return re.sub(r"\s*\[[^\]]*\]", "", s)


PL, ML = nonempty(PALI / NAME), nonempty(OUT / NAME)
if len(PL) != len(ML):
    bad.append("line count differs")
PAIRS = list(zip(PL, ML))

# ===================================================================================== A. regeneration
regen = G.generate()
same = regen == (OUT / NAME).read_text(encoding="utf-8")
if not same:
    bad.append("A: file differs from the regenerated text")
print(f"A. regeneration: {int(same)} / 1 file identical")

# ===================================================================================== B1. typography
raw = (OUT / NAME).read_text(encoding="utf-8")
if raw != unicodedata.normalize("NFC", raw):
    bad.append("B1: not NFC")
for ch in ("?", "।", ":-"):
    if ch in raw:
        bad.append(f"B1: contains {ch}")
if re.search(r"(^|[\s“‘(])ေ", raw, re.M):
    bad.append("B1: Zawgyi-like «ေ» at word start")
for i, (p, m) in enumerate(PAIRS):
    pb, mb = nobr(body(p)), nobr(body(m))
    pb = re.sub(r"^#+ .*", "", pb)
    np_ = len(re.findall(r'[.?!]"?(?=\s|$)', pb))
    if np_ != mb.count("။"):
        bad.append(f"B1 {i + 1}: {np_} Pāli sentence ends, {mb.count('။')} «။»")
    if pb.count("?") != mb.count("နည်း။"):
        bad.append(f"B1 {i + 1}: {pb.count('?')} «?», {mb.count('နည်း။')} «နည်း။»")
print(f"B1. typography: {len(PAIRS)} lines checked")

# ===================================================================================== B2. numbers
P_NUM = [
    (r"cattār(?:o|i|ome)", 4), (r"catasso(?:pi)?", 4), (r"dve(?:pi)?", 2), (r"dvinnaṃ", 2), (r"tisso(?:pi)?", 3),
    (r"tiṇṇaṃ", 3), (r"pañca(?:pi)?", 5), (r"pañcannaṃ", 5), (r"dasapi", 10), (r"vīsampi", 20), (r"tiṃsampi", 30),
    (r"cattālīsampi", 40), (r"paññāsampi", 50), (r"jātisatampi", 100), (r"jātisahassampi", 1000),
    (r"jātisatasahassampi", 100000), (r"ekampi", 1), (r"ekissā(?:pi)?", 1), (r"ekasmiṃ", 1),
    (r"ekāgāriko|ekālopiko|ekāhikampi|ekabhattiko", 1), (r"dvāgāriko|dvālopiko|dvīhipi|dvīhikampi", 2),
    (r"sattāgāriko|sattālopiko|sattahipi|sattāhikampi", 7), (r"sāyatatiyakampi", 3), (r"sakideva", 1),
    (r"catukka(?:puggalapaññatti|niddeso)", 4),
]
P_NUM_RE = [(re.compile(rf"(?<![\w]){rx}(?![\w])", re.I), n) for rx, n in P_NUM]
P_ORD = [(r"paṭhamaṃ", 1), (r"dutiy(?:aṃ|asmiṃ)", 2), (r"tatiy(?:aṃ|asmiṃ)", 3), (r"catutth(?:aṃ|asmiṃ)", 4)]
P_ORD_RE = [(re.compile(rf"(?<![\w]){rx}(?![\w])", re.I), n) for rx, n in P_ORD]
B_NUM = {"တစ်": 1, "နှစ်": 2, "သုံး": 3, "လေး": 4, "ငါး": 5, "ခြောက်": 6, "ခုနစ်": 7, "ရှစ်": 8, "ကိုး": 9, "ဆယ်": 10,
         "နှစ်ဆယ်": 20, "သုံးဆယ်": 30, "လေးဆယ်": 40, "ငါးဆယ်": 50}
CLF = "ယောက်|ပါး|ကြိမ်|မျိုး|ခု|ဘဝ|အိမ်|လုတ်|ခွက်|ရက်|ကောင်|လုံး|နပ်"
B_NUM_RE = re.compile(r"(?<![က-႟])(" + "|".join(sorted(map(re.escape, B_NUM), key=len, reverse=True)) +
                      rf")(?={CLF})")
B_BIG = {"တစ်ရာ": 100, "တစ်ထောင်": 1000, "တစ်သိန်း": 100000}
B_ORD = {"ပထမ": 1, "ဒုတိယ": 2, "တတိယ": 3, "စတုတ္ထ": 4}
NOT_NUM = ["သူတစ်ပါး"]


def p_nums(p):
    s = re.sub(r"^#+ ", "", nobr(body(p)))
    out = []
    for rx, n in P_NUM_RE:
        out += [n] * len(rx.findall(s))
    for rx, n in P_ORD_RE:
        out += [f"o{n}"] * len(rx.findall(s))
    return Counter(out)


def b_nums(m):
    s = re.sub(r"^#+ ", "", nobr(body(m)))
    for x in NOT_NUM:
        s = s.replace(x, "")
    out = []
    for k, v in B_BIG.items():
        out += [v] * s.count(k)
        s = s.replace(k, "")
    out += [B_NUM[x] for x in B_NUM_RE.findall(s)]
    for k, v in B_ORD.items():
        out += [f"o{v}"] * s.count(k)
    return Counter(out)


nb2 = 0
for i, (p, m) in enumerate(PAIRS):
    a, b = p_nums(p), b_nums(m)
    nb2 += sum(a.values())
    if a != b:
        bad.append(f"B2 {i + 1}: numbers Pāli {dict(a)} / Burmese {dict(b)}")
print(f"B2. numbers: {nb2} numbers checked")

# ===================================================================================== B3. polarity
NEG_FREE = re.compile(r"(?<![\w])(?:na|no|neva|naheva|nopi|nappajānāti)(?![\w])", re.I)
P_COMPOUND = {  # negations inside compounds / sandhi
    "naehibhaddantiko": 1, "natiṭṭhabhaddantiko": 1, "nābhihaṭaṃ": 1, "nānubyañjanaggāhī": 1, "nayidaṃ": 1,
    "nāparaṃ": 1, "sahitāsahitassa": 1,
}
PRIV = [  # privative a- / an- rendered with a Burmese negation (each counts once per occurrence)
    "asappuris", "adinnādān", "adinnādāy", "anabhijjh", "abyāpann", "abyāpād", "anavajj", "appasādanīye",
    "appasādaṃ", "ananuvicca", "apariyogāhetvā", "anupapanno", "anattantapo", "aparantapo", "arūpasahagat",
    "asahitañca", "acelako", "athenena", "abrahmacariyaṃ", "avisaṃvādako", "anuttaro", "anagāriyaṃ", "asaṃvutaṃ",
    "abyāsekasukhaṃ", "anuddhato", "akathaṃkathī", "avitakkaṃ", "avicāraṃ", "adukkhamasukhaṃ", "anaṅgaṇe",
    "āneñjappatte", "anupavādakā", "avijjāsavāpi", "anāsavaṃ", "anāvattidhammo", "avinipātadhammo", "appahīno",
    "anantarahitāya", "samaṇamacalo",
]
PRIV_RE = re.compile(r"(?<![\w])(?:" + "|".join(map(re.escape, PRIV)) + r")\w*", re.I)
PRIV_DOUBLE = {"adukkhamasukhaṃ": 2}           # a-dukkha a-sukha = «မနာကျင် မသာယာ»
LEX = {  # look negative in Pāli, rendered without a Burmese negation (not counted; listed for the report)
    "avaṇṇ": "avaṇṇa (dispraise) = «ကဲ့ရဲ့»", "akusal": "akusala = «အကုသိုလ်»", "aneka": "aneka = «များစွာ / အမျိုးမျိုး»",
    "anu-": "anu- (not privative)", "nelā": "nelā (faultless) = «အပြစ် ကင်းသော»", "nicchāto": "«ဆာလောင်မှု ကင်း»",
    "vigata-": "«ကင်း»", "appa-": "appa (little) = «နည်း»", "du-": "du- = «ဆိုး»", "aññ": "añña = «အခြား»",
}
NOT_NEG = ["မနော", "ကာမ", "မိန်းမ", "သို့မဟုတ်", "ကျွန်မ", "မြင်းမ", "နွားမ", "မိမိ", "ထောမနာ", "ဆုံးမ"]
# (words with a «မ» that is no negation: mano, kāma, woman, «or», female slave, mare, cow, self, praise, to train)
B_NEG_RE = re.compile(r"မဟုတ်|မ(?=[က-အ](?![့ံ]*[်္]))")


def p_neg(p):
    s = re.sub(r"^#+ .*", "", nobr(body(p)))
    n = len(NEG_FREE.findall(s)) + len(PRIV_RE.findall(s))
    for k, c in PRIV_DOUBLE.items():
        n += (c - 1) * len(re.findall(rf"(?<![\w]){k}", s, re.I))
    for k, c in P_COMPOUND.items():
        n += c * len(re.findall(rf"(?<![\w]){k}(?![\w])", s, re.I))
    return n


def b_neg(m):
    s = nobr(body(m))
    for x in NOT_NEG:
        s = s.replace(x, "")
    return len(B_NEG_RE.findall(s))


nb3 = 0
for i, (p, m) in enumerate(PAIRS):
    a, b = p_neg(p), b_neg(m)
    nb3 += a
    if a != b:
        bad.append(f"B3 {i + 1}: negations Pāli {a} / Burmese {b}")
POLAR = []
for _g, _d in G.GROUP5.items():
    (o1, p1, m1), (o2, p2, m2), (o3, p3, m3), (o4, p4, m4) = _d["members"]
    POLAR += [(p3, p1, 1), (p3, p2, 1), (p3, p4, 2)] if "no" in p1.split() else []
for pos, neg, n in POLAR:
    nb3 += 1
    if b_neg(F.NAME[neg]) - b_neg(F.NAME[pos]) != n:
        bad.append(f"B3 pair {pos} / {neg}: expected +{n}")
print(f"B3. polarity: {nb3} negations / pairs checked; lexical renderings without negation: {len(LEX)}")

# ===================================================================================== B5. names
MAT = [(nobr(body(p)), nobr(body(m))) for p, m in zip(nonempty(PALI / "1-matika.md"), nonempty(OUT / "1-matika.md"))]
nb5 = 0
QMY = re.compile(r"(.+?) ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။")
CLOSE_MY = re.compile(r"ဤပုဂ္ဂိုလ်ကို “?(.+?)”?ဟု ခေါ်သည်။")
for i, (p, m) in enumerate(PAIRS):
    pb, mb = nobr(body(p)), body(m)
    for q in re.finditer(r"Katamo ca puggalo ([^?]+)\?", pb):
        nb5 += 1
        key = F.key_of(q[1])
        qm = QMY.match(re.sub(r" \[[^\]]*\]", "", mb[mb.find(F.NAME[key]):]) if key else "")
        if not key or not qm or qm[1] != F.NAME[key]:
            bad.append(f"B5 {i + 1} question «{q[1]}»")
            continue
        mat = [mm for pp, mm in MAT if re.search(rf"(?<!\w){re.escape(q[1])}(?!\w)",
                                                  pp.replace(",", "").lower()) and (F.NAME[key] in mm or F.adj(F.NAME[key]) in mm)]
        if not mat:
            bad.append(f"B5 {i + 1} «{q[1]}»: name not in the Burmese mātikā")
    for c in re.finditer(r'vuccati,? puggalo "?([^".]+)"?(?:ti)?\.', pb):
        nb5 += 1
        names = [x for x in CLOSE_MY.findall(mb)]
        if F.NAME[F.key_of(c[1])] not in names:
            bad.append(f"B5 {i + 1} closing «{c[1]}»")
KQ = re.compile(r"ပုဂ္ဂိုလ်သည် အဘယ်သို့ (.+?)(?:ဖြစ်သနည်း|သနည်း)")
KE = re.compile(r"ဤသို့ ပုဂ္ဂိုလ်သည် (.+?)(?:ဖြစ်၏)?။")
GROUP_NAMES = {}
for _g, _d in G.GROUP5.items():
    GROUP_NAMES.update({F.NAME[p]: _g for o, p, m in _d["members"]})
for i, (p, m) in enumerate(PAIRS):
    pb, mb = nobr(body(p)), body(m)
    nq = len(re.findall(r"Kathañca puggalo", pb))
    if not nq:
        continue
    qs, es = KQ.findall(mb), KE.findall(mb)
    nb5 += nq
    if len(qs) != nq or len(es) != len(re.findall(r"[Ee]vaṃ puggalo", pb)):
        bad.append(f"B5 {i + 1}: {nq} Kathañca, {len(qs)} / {len(es)} Burmese frames")
        continue
    for qx, ex in zip(qs, es):
        if qx.strip() != ex.strip() and qx.strip() != ex.strip().rstrip("မဟုတ်").strip() + " မဟုတ်":
            if not (ex.endswith("မဟုတ်") and qx.strip() == ex.strip()):
                bad.append(f"B5 {i + 1}: question «{qx[:40]}» / closing «{ex[:40]}»")
        x = ex.strip()
        if x.endswith("ဖြစ်၏"):
            x = x[:-len("ဖြစ်၏")].strip()
        g = GROUP_NAMES.get(x)
        if g:
            names_line = [mm for pp, mm in PAIRS if f"Tattha katame cattāro {g} puggalā?" in pp]
            if not names_line or x not in names_line[0]:
                bad.append(f"B5 {i + 1}: «{x[:40]}» not in the names line of {g}")
        elif not any(x in mm for pp, mm in MAT):
            bad.append(f"B5 {i + 1}: predicate «{x[:50]}» not in the Burmese mātikā")
for i, (p, m) in enumerate(PAIRS):       # (c) similes
    for s_ in re.finditer(r"Seyyathāpi (so|sā|taṃ) (\S+) ", nobr(body(p))):
        nb5 += 1
        nouns = {d["sim"].split()[1]: d["noun"] for d in G.GROUP5.values()}
        if f"ဥပမာအားဖြင့် ထို{nouns[s_[2]]}သည်" not in body(m):
            bad.append(f"B5 {i + 1}: simile {s_[2]}")
print(f"B5. names: {nb5} questions / closings / similes checked")

# ===================================================================================== C. reuse test (independent)
FIN = []
for b in "123":
    for f in sorted((ROOT / f"AI_translation/pali/pi-{b}_split_chapters").glob("*.md")):
        bf = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters" / f.name
        if not bf.exists():
            continue
        pl, ml = nonempty(f), nonempty(bf)
        if len(pl) != len(ml):
            sys.exit(f"FINAL pi-{b} {f.name}: line counts differ")
        FIN += [(b, x, y) for x, y in zip(pl, ml)]
SEGS, _cur = [], []
for b, x, y in FIN:
    _cur.append((x, y))
    if re.search(r"\^[0-9A-Za-z-]+\s*$", x):
        SEGS.append((" ".join(a for a, _ in _cur), " ".join(c for _, c in _cur)))
        _cur = []
FIN_LINE = {}
for b, x, y in FIN:
    FIN_LINE.setdefault(nobr(body(x)).rstrip("."), set()).add(body(y).rstrip("။"))
n_c1 = s_c1 = 0
for p, m in PAIRS:
    k = nobr(body(p)).rstrip(".")
    if k in FIN_LINE:
        n_c1 += 1
        s_c1 += nobr(body(m)).rstrip("။") in FIN_LINE[k]
        if nobr(body(m)).rstrip("။") not in FIN_LINE[k]:
            bad.append(f"C1 «{k[:50]}»")
REUSE = [  # (regex on the ch5 Pāli, Pāli in a pi-1/2/3 segment, the final Burmese)
    (r"\bpuggal", "ekaṃ puggalaṃ", "ပုဂ္ဂိုလ်"),
    (r"\bpāṇātipāt", "pāṇātipātā veramaṇī", "သူ့အသက်ကို သတ်"),
    (r"\badinnādān", "adinnādānā veramaṇī", "မပေးသည်ကို ယူခြင်း"),
    (r"\bkāmesumicchācār", "kāmesumicchācārā veramaṇī", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်"),
    (r"\bmusāvād", "musāvādā veramaṇī", "မုသား ပြော"),
    (r"\bsurāmerayamajjapamādaṭṭhān", "surāmerayamajjapamādaṭṭhānā",
     "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့ခြင်း၏ အကြောင်း"),
    (r"\bpisuṇāya vācāya", "pisuṇāya vācāya veramaṇī", "ကုန်းတိုက်သော စကား"),
    (r"\bpharusāya vācāya", "pharusāya vācāya veramaṇī", "ကြမ်းတမ်းသော စကား"),
    (r"\bsamphappalāp", "samphappalāpā veramaṇī", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား"),
    (r"\bveramaṇiyā", "pāṇātipātā veramaṇī", "ကင်းဝေးခြင်း"),
    (r"\babhijjh", "abhijjhā kāyagantho", "သူ့ဥစ္စာကို"), (r"\bbyāpād", "byāpādo", "ဖျက်ဆီးလိုစိတ်"),
    (r"\babyāpannacitto", "Abyāpannacitto", "ဖျက်ဆီးလိုစိတ် မရှိသော စိတ် ရှိသူ"),
    (r"\bmicchādiṭṭhi", "micchādiṭṭhikā", "မှားယွင်းသော အယူ"),
    (r"\bsammādiṭṭhi", "sammādiṭṭhikā", "မှန်ကန်သော အယူ"),
    (r"duccarit", "kāyaduccaritaṃ", "ဒုစရိုက်"), (r"sucarit", "kāyasucaritena", "သုစရိုက်"),
    (r"\bkāyassa bhedā paraṃ maraṇā", "kāyassa bhedā paraṃ maraṇā", "ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက်"),
    (r"\bapāyaṃ duggatiṃ vinipātaṃ nirayaṃ", "apāyaṃ duggatiṃ vinipātaṃ nirayaṃ",
     "အပါယ်၊ ဆိုးသော လားရာ၊ ပျက်စီး ကျရောက်ရာ၊ ငရဲ"),
    (r"\bsugatiṃ saggaṃ lokaṃ", "sugatiṃ saggaṃ lokaṃ", "ကောင်းသော လားရာ၊ နတ်ပြည် လောက"),
    (r"\bsuttaṃ geyyaṃ", "suttaṃ geyyaṃ", "သုတ်၊ ဂေယျ၊ ဝေယျာကရဏ၊ ဂါထာ၊ ဥဒါန်း၊ ဣတိဝုတ်၊ ဇာတ်၊ အဗ္ဘုတဓမ္မ၊ ဝေဒလ္လ"),
    (r"\byathābhūtaṃ pajānāti", "yathābhūtaṃ pajānāti", "ဟုတ်မှန်သည့်အတိုင်း ကွဲပြားစွာ သိ"),
    (r"\bdukkhasamudayo", "dukkhasamudayo", "ဒုက္ခ ဖြစ်ပေါ်ခြင်း"),
    (r"\bdukkhanirodhagāminī paṭipadā", "dukkhanirodhagāminī paṭipadā", "ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်"),
    (r"\bāsav", "āsavā dhammā", "စိတ်အစွန်းအထင်း"),
    (r"\bkhattiyamahāsāl", "khattiyamahāsālānaṃ", "ကြွယ်ဝသော မင်းမျိုး"),
    (r"\bbrāhmaṇamahāsāl", "brāhmaṇamahāsālānaṃ", "ကြွယ်ဝသော ပုဏ္ဏားမျိုး"),
    (r"\bgahapatimahāsāl", "gahapatimahāsālānaṃ", "ကြွယ်ဝသော သူကြွယ်မျိုး"),
    (r"\bdubbaṇṇ", "dubbaṇṇe", "အဆင်း ဆိုး"), (r"\btathāgat", "tathāgato", "မြတ်စွာဘုရား"),
    (r"\bsammāsambuddho", "sammāsambuddho", "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်"),
    (r"\bsayaṃ abhiññā sacchikatvā", "sayaṃ abhiññā sacchikatvā", "ကိုယ်တိုင် ထူးကဲစွာ သိ၍ မျက်မှောက်ပြုပြီး"),
    (r"\bbrahmacariy", "brahmacariye", "မြင့်မြတ်သော အကျင့်"),
    (r"\bsabbapāṇabhūtahitānukampī", "sabbapāṇabhūtahitānukampī", "ခပ်သိမ်းသော သတ္တဝါတို့၏ အကျိုးကို စာနာလျက်"),
    (r"\bsampajānakārī", "sampajānakārī", "ကောင်းစွာ ဆင်ခြင်သိမြင်လျက် ပြုလေ့ရှိသူ"),
    (r"\bnimittaggāhī", "nimittaggāhī", "အမှတ်အသားကို စွဲယူသူ"),
    (r"nubyañjanaggāhī", "anubyañjanaggāhī", "အသေးစိတ်ကို စွဲယူသူ"),
    (r"\bcakkhundriy", "cakkhundriyaṃ", "မျက်စိ၏ စွမ်းရည်"), (r"\bmanindriy", "manindriyaṃ", "မနော၏ စွမ်းရည်"),
    (r"\bvivittaṃ senāsanaṃ", "vivittaṃ senāsanaṃ", "ဆိတ်ငြိမ်သော အိပ်ရာ နေရာ"),
    (r"\bsenāsana", "senāsanaṃ", "အိပ်ရာ နေရာ"),
    (r"\bpallaṅkaṃ ābhujitvā", "pallaṅkaṃ ābhujitvā", "ထက်ဝယ်ဖွဲ့ခွေ၍"),
    (r"\bpañca nīvaraṇe", "pañca nīvaraṇe", "အတားအဆီး ငါးပါး"),
    (r"\bpaṭhamaṃ jhānaṃ", "paṭhamaṃ jhānaṃ", "ပထမ ဈာန်"), (r"\bdutiyaṃ jhānaṃ", "dutiyaṃ jhānaṃ", "ဒုတိယ ဈာန်"),
    (r"\btatiyaṃ jhānaṃ", "tatiyaṃ jhānaṃ", "တတိယ ဈာန်"), (r"\bcatutthaṃ jhānaṃ", "catutthaṃ jhānaṃ", "စတုတ္ထ ဈာန်"),
    (r"\bpubbenivāsānussatiñāṇ", "pubbenivāsānussati ñāṇaṃ", "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်"),
    (r"\bcutūpapātañāṇ", "cutūpapāte ñāṇaṃ", "သတ္တဝါတို့၏ သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်းကို သိသော ဉာဏ်"),
    (r"\bkhayañāṇ", "āsavānaṃ khaye ñāṇaṃ", "စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းကို သိသော ဉာဏ်"),
    (r"\bdibbena cakkhunā", "dibbena cakkhunā", "နတ်မျက်စိဖြင့်"),
    (r"\bariyānaṃ upavādakā", "ariyānaṃ upavādakā", "အရိယာတို့ကို စွပ်စွဲ"),
    (r"\bkāmāsav", "Kāmāsavo", "ကာမ စိတ်အစွန်းအထင်း"), (r"\bbhavāsav", "bhavāsavo", "ဘဝ စိတ်အစွန်းအထင်း"),
    (r"\bavijjāsav", "avijjāsavo", "အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း"), (r"\bKhīṇā jāti", "katamā jāti", "မွေးဖွားခြင်း"),
    (r"\banāsavaṃ cetovimuttiṃ", "anāsavaṃ cetovimuttiṃ", "စိတ်အစွန်းအထင်း မရှိသော စိတ်၏ လွတ်မြောက်ခြင်း"),
    (r"\bdiṭṭheva dhamme", "diṭṭheva dhamme", "မျက်မှောက်ဘဝ၌ပင်"),
    (r"\borambhāgiy", "Pañcorambhāgiyāni saṃyojanāni", "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး"),
    (r"\btiṇṇaṃ saṃyojanānaṃ", "Tīṇi saṃyojanāni", "နှောင်ကြိုး သုံးပါး"),
    (r"\bNerayik", "nerayikānaṃ", "ငရဲသား"), (r"\bParanimmitavasavatt", "paranimmitavasavattīnaṃ", "ပရနိမ္မိတဝသဝတ္တီ"),
    (r"\blokuttara", "lokuttarā dhammā", "လောကကို ကျော်လွန်သော"), (r"\bsamāpatt", "samāpattikusalatā", "ဈာန် ဝင်စားရာ"),
    (r"\bdussīl", "dussīlā", "သီလ ပျက်"), (r"\bkodho", "Kodho ca upanāho", "အမျက်ဒေါသ"),
    (r"\bupekkhako", "upekkhako", "ဥပေက္ခာ ရှိ"), (r"\bsato sampajāno", "sato sampajāno", "သတိ ရှိလျက်"),
    (r"\bparisā", "parisāsu", "ပရိသတ်"), (r"\bpiṇḍapāt", "piṇḍapāta", "ဆွမ်း"), (r"\bcīvar", "cīvara", "သင်္ကန်း"),
    (r"saṅghāṭipattacīvaradhāraṇ", "saṅghāṭipattacīvaradhāraṇe", "ဒုကုဋ်၊ သပိတ်၊ သင်္ကန်းကို ဆောင်"),
    (r"\babhikkant", "abhikkante", "ရှေ့သို့ တိုး"),
    (r"\bvitakkavicārānaṃ vūpasamā", "vitakkavicārānaṃ vūpasamā", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်းကြောင့်"),
    (r"\bgahapati\b", "gahapati", "သူကြွယ်"),
    (r"\bpabbajit", "pabbajitehi", "ရဟန်း"), (r"\bariyena", "ariyamaggesu", "အရိယာ"),
    (r"\bsīlakkhandh", "Pañcakkhandhā", "အစုအဝေး"), (r"\bvimutti", "vimutti ca", "လွတ်မြောက်မှု"),
    (r"\bsīlasampad", "sīlasampadā ca", "သီလ ပြည့်စုံခြင်း"), (r"\bsamannāgat", "samannāgato", "အပြည့်အဝ ပြည့်စုံ"),
    (r"\bkusalesu dhammesu", "kusalesu dhammesu", "ကုသိုလ် သဘောတရားတို့၌"),
    (r"\bsamādhi", "samādhi", "သမာဓိ"), (r"\bpañña(?:ṃ|ā)\b", "paññā", "ပညာ"),
]
n_c2 = s_c2 = 0
PI = [(nobr(body(p)), body(m)) for p, m in PAIRS]
for rx, fp, my in REUSE:
    n_c2 += 1
    wit = [1 for sp, sm in SEGS if fp.lower() in nobr(sp).lower() and my in sm]
    occ = [(p, m) for p, m in PI if re.search(rx, p, re.I)]
    miss = [p[:70] for p, m in occ if my not in m]
    if wit and occ and not miss:
        s_c2 += 1
    else:
        bad.append(f"C2 «{rx}» / «{my}»: witness {bool(wit)}, {len(occ)} lines, missing in {miss[:2]}")
# C3 the approved pi-4 sample: every sample sentence (my4_formulas / make_sample SENT, no placeholder) that occurs in a
# ch5 Pāli line has the sample's Burmese in that line; every mātikā (catukka) predicate used by a frame is the sample's
n_c3 = s_c3 = 0
for k, v in F.SENT.items():
    if k in G.SENT5 or "⟦" in v or len(k) < 30:
        continue
    k0 = k.rstrip(".")
    occ = [(p, m) for p, m in PI if k0 in p]
    if occ:
        n_c3 += 1
        ok = all(v.rstrip("။") in m for p, m in occ)
        s_c3 += ok
        if not ok:
            bad.append(f"C3 sample sentence «{k0[:50]}»")
for k, v in F.PRED.items():
    k0 = k.replace(", no ", " no ")
    occ = [(p, m) for p, m in PI if f"puggalo {k} " in p or f"puggalo {k}?" in p or f"puggalo {k0}?" in p]
    if occ and "⟦" not in v:
        n_c3 += 1
        ok = all(v in m or v.replace("ဖြစ်၏", "ဖြစ်သနည်း") in m for p, m in occ)
        s_c3 += ok
        if not ok:
            bad.append(f"C3 mātikā predicate «{k[:50]}»")
print(f"C. reuse test: C1 whole lines {s_c1} / {n_c1}; C2 terms and clauses {s_c2} / {n_c2} identical with "
      f"pi-1 / pi-2 / pi-3 final; C3 sample sentences and mātikā predicates {s_c3} / {n_c3}")
# consistency pass (harmonise-notes.md): forms changed on purpose against pi-1 / pi-2 / pi-3 (no longer reuse items)
HARMONISED = [(r"buddho bhagavā", F.BHAGAVA_EPITHET,
               "B4: bhagavā as the epithet of the subject tathāgato (^4-177) = «ဘုန်းတော်ရှင်», not pi-1 «မြတ်စွာဘုရား»")]
n_h = s_h = 0
for rx, my, why in HARMONISED:
    n_h += 1
    occ = [(p, m) for p, m in PI if re.search(rx, p)]
    miss = [p[:70] for p, m in occ if my not in m]
    if occ and not miss:
        s_h += 1
    else:
        bad.append(f"H «{rx}» / «{my}» ({why}): {len(occ)} lines, missing in {miss[:2]}")
print(f"H. harmonised forms (changed on purpose in the consistency pass): {s_h} / {n_h}")
s_c2, n_c2 = s_c2 + s_c3, n_c2 + n_c3
if bad:
    print(f"\nMISMATCHES: {len(bad)}")
    for b in bad:
        print("  " + b)
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {s_c1 + s_c2} / {n_c1 + n_c2} identical")
