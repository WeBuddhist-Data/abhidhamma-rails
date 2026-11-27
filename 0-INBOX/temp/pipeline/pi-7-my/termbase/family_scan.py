"""Family scan for the pi-7 Burmese termbase (copied from pi-6-my/termbase/family_scan.py, pi-7 paths and the pi-7 frame words): list lemma families whose
headwords carry more than one Burmese term, so drift inside a family is visible.

usage: python3 -I -X utf8 family_scan.py [<senses-or-termbase.md>] [stem ...]
Default file: AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md.
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
path = pathlib.Path(args.pop(0)) if args and args[0].endswith(".md") else BASE / "AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md"

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
    ("indriy", "စွမ်းရည်"), ("vicikicch", "ယုံမှား"), ("uppann", "ဖြစ်ပေါ်", ("paccuppann",)), ("uppād", "ဖြစ်ပေါ်"),
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
COREW = [c for c in COREW if c[0] not in ("paṭicca", "pahātabb")]  # pi-7: paṭicca «မှီ၍» (approved sample), pahātabba «ပယ်ရမည့်» (rule 3)
COREW += [  # pi-7 (Paṭṭhāna) additions: the frame words, the 24 condition names (map-table T1-T6) and the doctrinal terms
    ("paṭicca", "မှီ၍"), ("nissāya", "မှီ၍"), ("pahātabb", "ပယ်ရမည", ("pahātabbattik",)), ("paccay", "အကြောင်း"),
    ("paṭṭhān", "ဆက်စပ်ပုံ"), ("anantar", "ချက်ချင်း နောက်"), ("samanantar", "ကောင်းစွာ ချက်ချင်း နောက်"),
    ("sahajāt", "အတူ ပေါ်ပေါက်"), ("aññamañña", "အချင်းချင်း"), ("nissay", "အမှီ"), ("upanissay", "အားကြီးသော အမှီ"),
    ("purejāt", "ရှေးဦးစွာ ဖြစ်ပေါ်"), ("pacchājāt", "နောက်မှ ဖြစ်ပေါ်"), ("āsevan", "အလေ့အကျင့်"), ("āhār", "အာဟာရ"),
    ("vigat", "ပျောက်ကွယ်"), ("khandh", "အစုအဝေး"), ("āyatan", "နယ်ပယ်"), ("samaṅg", "ပြည့်စုံ"), ("nirodh", "ချုပ်ငြိမ်း"),
    ("niruddh", "ချုပ်ငြိမ်း"), ("magg", "မဂ်"), ("phal", "ဖိုလ်"), ("citt", "စိတ်"), ("paṭisandh", "ပဋိသန္ဓေ"),
    ("samuṭṭhān", "ဖြစ်ပေါ်လာ"), ("kaṭattā", "ကံ ပြုခဲ့"), ("vatthu", "ဝတ္ထု"), ("anulom", "အဟုတ်ပြ"), ("paccanīy", "အငြင်းပြ"),
    ("gaṇan", "ရေတွက်"), ("ghaṭan", "ပေါင်းစပ်"), ("sadis", "တူ"), ("vāro", "ဖော်ပြချက်"), ("vāra", "ဖော်ပြချက်"),
    ("uppajj", "ဖြစ်ပေါ်"), ("asaññasatt", "အသညသတ်"), ("abyākat", "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်"),
    ("akusal", "အကုသိုလ်", ("nakusal", "dukakusal", "yatanakusal", "mak")), ("sampayutt", "ယှဉ်တွဲ"), ("vippayutt", "ကင်းကွာ"),
    ("paccavekkh", "ပြန်လည် ဆင်ခြင်"), ("arah", "ရဟန္တာ"), ("puthujjan", "ပုထုဇဉ်"), ("avases", "ကြွင်း"),
]
# substrings of another word (Part A): stem -> headword substrings that are not that stem
NOTSTEM = {"saññ": ("saññojan",), "mūl": ("mūlak", "mūlā", "mūla", "mūle"), "itar": ("pitar", "mātar"), "sukh": ("sukhum",),
           "sati": ("vīsati", "bbīsati"), "paññ": ("paññās",), "moh": ("mohant",), "āsav": ("parāmāsav",), "sacc": ("saccābhinives",),
           "arūpāvacar": ("narūpāvacar",), "uppād": ("ruhiruppād",), "bhaṅg": ("vibhaṅg",), "ajjhatt": ("ajjhattik",)}

# Part A, explained (an approved pi-7 form, or another sense): stem -> ((headword substring, reason), ...)
EXPL = {
    "atīt": (("tīti", "the verb ending -tīti (uppajjatīti …), not atīta"),),
    "sati": (("ssati", "the future ending -issati, not sati"), ("anussati", "pubbenivāsānussati «အဖန်ဖန် အောက်မေ့» (recollection), not the factor sati")),
    "saññ": (("asaññasatt", "the plane / beings name asaññasatta «အသညသတ်» (pi-2, name kept)"),),
    "thin": (("itthindriy", "itthindriya, not thina"),),
    "rūpāvacar": (("arūpāvacar", "arūpāvacara, not rūpāvacara"),),
    "dukkh": (("dukkhato", "the characteristic «ဆင်းရဲ» (aniccato / dukkhato / anattato, pi-5 aniccato «မမြဲ», §A 13), not the feeling"),
              ("dukkhaṃ", "dukkhaṃ|1 the characteristic «ဆင်းရဲ» (senses step), not the feeling")),
    "uppād": (("uppādetvā", "lohitaṃ uppādetvā «ထွက်စေ၍» (another sense, the heinous deed, pi-5 H5)"),
              ("uppāde", "uppādeti / uppādenti «ဖြစ်စေသည်» (the pi-7 text; departs from pi-5 uppādenti «ဖြစ်ပေါ်စေသည်»: jappeti «ဖြစ်ပေါ်စေသည်», locked pi-5, stands in the same deeds-list segments, notes-part5 5a)")),
    "magg": (("vācanāmagg", "vācanāmagga «ရွတ်ဆိုသည့် နည်းလမ်း» (the way of reciting), not the path"),
             ("sajjhāyamagg", "sajjhāyamagga «သရဇ္ဈာယ်သည့် နည်းလမ်း» (the way of chanting), not the path")),
    "pariyāpann": (("apariyāpann", "the privative «အကျုံးမဝင်သော» (မ + verb, burmese-style negation)"),),
    "vipassan": (("vipassanti", "the verb «ထိုးထွင်း၍ ရှုသည်» (= vipassati), the noun vipassanā «ထိုးထွင်းသိမြင်ခြင်း»: the same «ထိုးထွင်း»"),),
    "anulom": (("anulomañca", "the conformity mind moment «လျော်ညီခြင်း စိတ်» (NEW_SENSE, H1)"),
               ("anulomaṃ", "Anulomaṃ|1 the conformity mind moment «လျော်ညီခြင်း စိတ်» (NEW_SENSE, H1)")),
    "pahātabb": (("pahātabbattik", "the triad name «… ပယ်ခြင်း သုံးမျိုးတွဲ» (heading, noun form)"),),
    "paccay": (("aññamaññapaccaya", "the bare stem = the bare name N «အချင်းချင်း ထောက်ပံ့ခြင်း» (T1), as the other stems"),
               ("paccayā", "the bare ablative of the dependent-origination formula «…ကြောင့်» (pi-2 avijjāpaccayā, locked)")),
}
explained = []

# Part B, explained families (pi-7 termbase decisions, notes-part5.txt 5c): "neg-stem" -> reason
FRAME = ("the condition by its frame (map-table T1-T4; senses step NEW_SENSE): the bare name N (lists), the name «Nဟူသော အကြောင်း» "
         "(headings, -paccayo, -paccayena, the counting locative), the ablative «…ကြောင့်»; the same N, case and frame only")
FAM_EXPL = {k: FRAME for k in ("adhip", "adhipat", "anantar", "atth", "avigat", "aññamaññ", "na-aññamaññ", "aññamaññapaccay", "indriy", "jhān",
                               "kamm", "magg", "nissay", "na-nissay", "pacchājāt", "purejāt", "na-purejāt", "sahajāt", "samanantar",
                               "sampayutt", "na-sampayutt", "na-tth", "upanissay", "na-upanissay", "vigat", "vippayutt", "na-vippayutt",
                               "vipāk", "na-vipāk", "āhār", "ārammaṇ", "na-ārammaṇ", "āsevan", "na-āsevan", "paccay", "hetuduk")}
FAM_EXPL.update({
    "vipāk": FRAME + "; vipāka itself: the attributive «ကံ၏ အကျိုး ဖြစ်သော» (vipāko, vipākā …) vs the noun «ကံ၏ အကျိုး» (vipākassa, vipāke|1, the bare name): the same word, grammar",
    "na-vipāk": FRAME + "; navipākañca «ကံ၏ အကျိုး မဟုတ်သော» is the triad term (T8), another sense",
    "paccay": "paccaya «အကြောင်း» (pi-5, approved sample) vs the vāra member paccaya- «အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း» (T5): two senses",
    "hetuduk": "the Mātikā root dyad «အမြစ် နှစ်မျိုးတွဲ» (pi-1) vs the root-condition pairs «အမြစ်ဟူသော အကြောင်း၏ နှစ်မျိုးတွဲ» (T1): two senses",
    "anulom": "two senses: the positive method «အဟုတ်ပြ ပုံစံ» (pi-6, approved sample) vs the conformity mind moment «လျော်ညီခြင်း စိတ်» (H1)",
    "arūp": "the dyad term «ရုပ် မဟုတ်သော» (pi-1 arūpino) vs arūpe «ရုပ်မရှိသော ဘုံ» (the plane, locative): two senses",
    "rūp": "three senses: matter «ရုပ်», the dyad term «ရုပ် ဖြစ်သော» (pi-1 rūpino), the visible object «အဆင်းအရောင်»",
    "dukkh": "three senses: the feeling «နာကျင်သော / နာကျင်မှု» (burmese-style), the characteristic «ဆင်းရဲ» (dukkhato)",
    "sukh": "grammar: the attributive «သာယာသော» (Sukhāya … vedanāya) vs the noun «သာယာမှု»; the same word",
    "gaṇit": "grammar: gaṇite in the locative absolute «… ရေတွက်သောအခါ» (^7-2-193) vs the participle «ရေတွက်ထားသော»; the same verb",
    "kātabb": "two senses (senses step, §A 9): «ပြုရမည့်» (to be done) vs «ထည့်ရမည့်» (to be included)",
    "sekkh": "the persons «ကျင့်ကြံဆဲသူ» (sekkhā, sekkhānaṃ; pi-4) vs the triad qualifier «ကျင့်ကြံဆဲသူ၏» (pi-1 / pi-2 final, coordinator's sekkha decision, §A 21): two uses",
    "saṃsaṭṭh": "the vāra member «ရောနှောခြင်း» (T5) vs the adjective saṃsaṭṭho «ရောနှောသော»: grammar / sense",
    "uppād": "two lemmas: uppādeti «ဖြစ်စေသည်» (causative verb) vs uppādī «ဖြစ်ပေါ်လာမည့်» (bound to arise, the triad term)",
    "no-upād": "two lemmas: noupādā «… မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော» (upādā) vs noupādānaṃ «စွဲလမ်းမှု မဟုတ်သော» (upādāna)",
    "nevavipākanavipākadhammadhamm": "grammar: with the head noun «သဘောတရား» (dhammo) vs the attributive before a noun; the same words",
    "maggapaccay": "maggapaccaya is the source slip for the ablative maggapaccayā (^7-12-5, part 3: the intended word's term «…ကြောင့်»); Maggapaccayo / maggapaccayena are the name (T1)",
    "anidassanaappaṭighamūlak": "grammar: -mūlake «… အခြေခံခြင်း» (the series) vs -mūlakā «… အခြေခံသော» (adjective pl.)",
    "anidassanasappaṭighamūlak": "grammar: -mūlake «… အခြေခံခြင်း» (the series) vs -mūlakā «… အခြေခံသော» (adjective pl.)",
})
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
    for st, my, *ex in COREW:
        if st not in h or my in t: continue
        why = next((w for x, w in EXPL.get(st, ()) if x in h), None)
        if any(x in h for x in (ex[0] if ex else ())): continue
        if any(x in h for x in NOTSTEM.get(st, ())): continue
        if why:
            explained.append(f"   {hw}|{i}: {t}   [{st} = {my}]  explained: {why}"); continue
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
print(f"\n== A2. explained core-word hits ({len(explained)})"); print("\n".join(explained))
print("\n== B. lemma families with more than one term (same polarity prefix)")
nfam = {True: 0, False: 0}
for st in sorted(stems_pos):
    grp = collections.defaultdict(list)
    for neg, hw, i, t in stems_pos[st]: grp[neg].append((hw, i, t))
    for neg, items in sorted(grp.items()):
        terms = collections.Counter(t for _, _, t in items)
        if len(terms) > 1:
            key = f"{neg + '-' if neg else ''}{st}"
            why = FAM_EXPL.get(key)
            nfam[bool(why)] += 1
            print(f"-- {key} ({len(items)} senses, {len(terms)} terms)" + (f"  explained: {why}" if why else "  UNEXPLAINED"))
            for hw, i, t in items: print(f"   {hw}|{i}: {t}")

print(f"\n== B summary: {nfam[True] + nfam[False]} families with more than one term, explained {nfam[True]}, unexplained {nfam[False]}")
print("\n== C. stem substring families")
for st in (args or CORE):
    hits = [(hw, i, t) for hw, i, _, t in rows if st in hw.lower()]
    terms = collections.Counter(t for _, _, t in hits)
    if len(terms) > 1:
        print(f"== {st} ({len(hits)} senses, {len(terms)} terms)")
        for hw, i, t in hits: print(f"   {hw}|{i}: {t}")
