"""Family scan for the pi-4 Burmese termbase (copied from pi-3-my/termbase/family_scan.py, pi-4 paths): list lemma families whose
headwords carry more than one Burmese term, so drift inside a family is visible.

usage: python3 -I -X utf8 family_scan.py [<senses-or-termbase.md>] [stem ...]
Default file: AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md.
Three parts:
  A. core-word check: every headword that contains one of the listed Pāli stems must contain its approved Burmese word
     (factor names, cluster nouns, the book's core terms; burmese-style.md / my-zeroshot-terms.md);
  B. lemma families: headwords grouped by a normalised stem (case endings, -ñca/-ñceva/-pi/-ti and na-/no- prefixes
     removed, the polarity kept apart); groups with more than one term are printed;
  C. stem substring families (the Marathi pi-1 method).
Compound members that legitimately differ still show; judge them.
"""
import sys, collections, pathlib, re

BASE = pathlib.Path(__file__).resolve().parents[5]
args = sys.argv[1:]
path = pathlib.Path(args.pop(0)) if args and args[0].endswith(".md") else BASE / "AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md"

CORE = ["hetu", "āsav", "saññojan", "ganth", "nīvaraṇ", "parāmās", "kiles", "vitakk",
        "vicār", "pīti", "sukh", "upekkh", "cetasik", "saṅkhār", "viññāṇ", "vedan",
        "saññ", "khandh", "indriy", "magg", "kusal", "kām", "lok", "sanidassan", "sappaṭigh", "upādinn", "upādiṇṇ",
        "saṃkiles", "saṃkiliṭṭh", "dassan", "bhāvan", "paritt", "mahaggat", "appamāṇ",
        "hīn", "paṇīt", "micchatt", "sammatt", "ārammaṇ", "adhipat", "uppann", "atīt",
        "anāgat", "paccuppann", "ajjhatt", "bahiddh", "upādān", "arūp",
        "vipāk", "sekkh", "pahātabb", "rūpāvacar", "kāmāvacar", "pariyāpann",
        "niyyānik", "saraṇ", "araṇ", "ācay", "apacay", "sāsav", "anāsav", "cittasaṃsaṭṭh",
        "cetan", "ogh", "yog", "sahajāt", "nissay", "āhār", "jhān", "sampayutt", "vippayutt",
        "vatthu", "rūp", "mahābhūt", "dukaṃ", "ttik", "gocchak", "phass", "passaddh", "lahut", "mudut",
        "kammaññ", "pāguññ", "ujuk", "sati", "samādh", "paññ", "vīriy", "saddh", "hiri", "hirī", "ottapp",
        "lobh", "dos", "moh", "diṭṭh", "vicikicch", "kaṅkh", "uddhacc", "kukkucc", "thin", "middh", "rāg",
        "taṇh", "abhijjh", "byāpād", "mett", "samath", "vipassan", "ekaggat", "ñāṇ", "vijj", "āyatan", "dhāt",
        "suññat", "animitt", "appaṇihit", "kiriy", "domanass", "somanass", "ākās", "para", "paṭicc"]

COREW = [  # (Pāli stem in the headword, Burmese word every such headword must contain)
    ("vitakk", "ကြံစည်"), ("vicār", "သုံးသပ်"), ("phass", "တွေ့ထိ"), ("vedan", "ခံစား"), ("cetan", "စေ့ဆော်"),
    ("somanass", "ဝမ်းမြောက်"), ("domanass", "စိတ်ဆင်းရဲ"), ("upekkh", "ဥပေက္ခာ"), ("pīti", "ပီတိ"),
    ("ottapp", "ကြောက်ရွံ့"), ("vicikicch", "ယုံမှား"), ("kaṅkh", "သံသယ"), ("uddhacc", "ယောက်ယက်ခတ်"),
    ("kukkucc", "နောင်တ"), ("saṃyojan", "နှောင်ကြိုး"), ("saññojan", "နှောင်ကြိုး"), ("nīvaraṇ", "အတားအဆီး"),
    ("āsav", "စိတ်အစွန်းအထင်း"), ("ogh", "ရေအလျဉ်"), ("kiles", "ကိလေသာ"), ("upādān", "စွဲလမ်း"),
    ("vipassan", "ထိုးထွင်း"), ("samath", "ငြိမ်သက်"), ("passaddh", "ငြိမ်းအေး"), ("lahut", "ပေါ့ပါး"),
    ("mudut", "ပျော့ပျောင်း"), ("kammaññ", "သင့်တော်"), ("pāguññ", "ကျင့်သားရ"), ("ujuk", "ဖြောင့်"),
    ("jhān", "ဈာန်"), ("vīriy", "ဝီရိယ"), ("abhijjh", "လိုချင်"), ("kusal", "ကုသိုလ်"),
    ("sati", "သတိ"), ("paññ", "ပညာ"), ("samādh", "သမာဓိ"), ("saddh", "ယုံကြည်"), ("hiri", "ရှက်"), ("hirī", "ရှက်"),
    ("lobh", "လောဘ"), ("moh", "မောဟ"), ("diṭṭh", "အယူ"), ("thin", "ထိုင်းမှိုင်း"), ("middh", "ငိုက်မျဉ်း"),
    ("ākās", "ဟင်းလင်းပြင်"), ("vipāk", "အကျိုး"), ("kiriy", "ပြုရုံမျှသာ"), ("saṅkhār", "ပြုပြင်ဖန်တီး"),
    ("viññāṇ", "သိစိတ်"), ("saññ", "မှတ်သိ"), ("khandh", "အစု"), ("āyatan", "နယ်ပယ်"), ("dhāt", "ဓာတ်"),
    ("ganth", "အထုံး"), ("yog", "ထမ်းပိုး"), ("parāmās", "ယူဆ"), ("ārammaṇ", "အာရုံ"), ("sappaṭigh", "ထိခိုက်"),
    ("hetu", "အမြစ်"), ("hetū", "အမြစ်"), ("suññat", "ဆိတ်သုဉ်း"), ("appaṇihit", "တောင့်တ"), ("animitt", "အမှတ်အသား"),
    ("indriy", "စွမ်းရည်"), ("vicikicch", "ယုံမှား"), ("uppann", "ဖြစ်ပေါ်"), ("uppād", "ဖြစ်ပေါ်"),
    ("domanass", "စိတ်ဆင်းရဲမှု"), ("somanass", "ဝမ်းမြောက်မှု"), ("upekkh", "ဥပေက္ခာ"), ("sukh", "သာယာ"),
    ("dukkh", "နာကျင်"), ("rāg", "ရာဂ"), ("taṇh", "တပ်မက်"), ("ekaggat", "စူးစိုက်"), ("vipassan", "ထိုးထွင်းသိမြင်"),
    ("passaddh", "ငြိမ်းအေးခြင်း"), ("lahut", "ပေါ့ပါးခြင်း"), ("mudut", "ပျော့ပျောင်းခြင်း"), ("ujuk", "ဖြောင့်တန်းခြင်း"),
    ("kammaññat", "သင့်တော်ခြင်း"), ("pāguññat", "ကျင့်သားရခြင်း"), ("bahiddh", "၌"), ("ajjhatt", "မိမိ"),
    ("paṭicca", "အကြောင်းတို့ကို မှီ၍"), ("āsav", "စိတ်အစွန်းအထင်း"), ("cetasik", "စိတ်"),
    ("vippayutt", "ကင်းကွာ"), ("sampayutt", "ယှဉ်တွဲ"), ("sahagat", "အတူ"), ("dos", "ဒေါသ"), ("byāpād", "ဖျက်ဆီးလို"),
    ("kāmāvacar", "ကာမဘုံ"), ("rūpāvacar", "သိမ်မွေ့သော ရုပ်ဘုံ"), ("arūpāvacar", "ရုပ်မရှိသော ဘုံ"),
    ("lokuttar", "လောကကို ကျော်လွန်"), ("lokiy", "လောက"), ("atīt", "အတိတ်"), ("anāgat", "အနာဂတ်"),
    ("upādiṇṇ", "ကံကြောင့်"), ("upādinn", "ကံကြောင့်"), ("sanidassan", "မြင်"), ("pahātabb", "ပယ်ရမည်"),
    ("sekkh", "ကျင့်ကြံ"), ("niyyānik", "လွတ်မြောက်ရာ"), ("tathāgat", "မြတ်စွာဘုရား"), ("mahābhūt", "မူလဓာတ်"),
    ("viññatt", "ထုတ်ဖော်ပြသ"), ("pariyāpann", "အကျုံးဝင်"), ("saṃkiliṭṭh", "ညစ်နွမ်း"), ("saṃkiles", "ကိလေသာ"),
    ("cittasaṃsaṭṭh", "စိတ်နှင့်"), ("cittasamuṭṭhān", "စိတ်"), ("ārammaṇ", "အာရုံ"), ("adhipat", "အကြီးအမှူး"),
]
COND_FORM = re.compile(r"^(?:na|no|a|an)?.*({}).*$")

rows = []
for line in path.read_text(encoding="utf-8").splitlines():
    if not line.strip(): continue
    hw, body = line.split(": {", 1)
    for i, s in enumerate(body[:-1].split("; ")):
        tag, terms = s.rsplit(": ", 1)
        rows.append((hw, i, tag, terms))

print("== A. core words: headwords with the stem whose term lacks the approved word")
for hw, i, tag, t in rows:
    h = hw.lower()
    for st, my in COREW:
        if st in h and my not in t:
            print(f"   {hw}|{i}: {t}   [{st} = {my}]  ({tag[:70]})")

ENC = ["ñceva", "ñcā", "ñca", "mpi", "pi", "nti", "ti", "yeva", "eva"]
END = sorted(["ānaṃ", "ānañ", "assa", "āya", "ena", "ehi", "esu", "āni", "aṃ", "o", "ā", "e", "a", "ī", "iṃ", "issa",
              "īnaṃ", "inaṃ", "inā", "ino", "ūnaṃ", "uṃ", "u", "ū", "ussa", "uno", "āyaṃ", "iyā", "yā", "i", "ato", "to"],
             key=len, reverse=True)
def lemma(hw):
    h = hw.lower()
    neg = ""
    for p in ("nano", "na", "no"):
        if h.startswith(p) and len(h) > len(p) + 3 and h[len(p):len(p)+1] not in "ṃ":
            neg = p; h2 = h[len(p):]; break
    else:
        h2 = h
    for e in ENC:
        if h2.endswith(e) and len(h2) - len(e) >= 4: h2 = h2[: -len(e)]; break
    for e in END:
        if h2.endswith(e) and len(h2) - len(e) >= 3: h2 = h2[: -len(e)]; break
    return neg, h2

stems_pos = collections.defaultdict(list)
for hw, i, tag, t in rows:
    neg, st = lemma(hw)
    stems_pos[st].append((neg, hw, i, t))
print("\n== B. lemma families with more than one term (same polarity prefix)")
for st in sorted(stems_pos):
    grp = collections.defaultdict(list)
    for neg, hw, i, t in stems_pos[st]: grp[neg].append((hw, i, t))
    for neg, items in sorted(grp.items()):
        terms = collections.Counter(t for _, _, t in items)
        if len(terms) > 1:
            print(f"-- {neg + '-' if neg else ''}{st} ({len(items)} senses, {len(terms)} terms)")
            for hw, i, t in items: print(f"   {hw}|{i}: {t}")

print("\n== C. stem substring families")
for st in (args or CORE):
    hits = [(hw, i, t) for hw, i, _, t in rows if st in hw.lower()]
    terms = collections.Counter(t for _, _, t in hits)
    if len(terms) > 1:
        print(f"== {st} ({len(hits)} senses, {len(terms)} terms)")
        for hw, i, t in hits: print(f"   {hw}|{i}: {t}")
