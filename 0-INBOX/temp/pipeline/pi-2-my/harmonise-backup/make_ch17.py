"""Burmese zero-shot of pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း») chapter 17 (Khuddakavatthuvibhaṅgo).

usage: python3 -I -X utf8 make_ch17.py [--notes]
Model: the approved sample (my2_formulas.py imported read-only; make_sample.py not run; nothing in pi-1-my written).
Every line is generated from the Pāli, sentence by sentence:
  1. a Pāli sentence identical with a pi-1 sentence takes pi-1's FINAL Burmese (rails text), word for word;
  2. a Pāli sentence identical with a sentence of a finished pi-2 chapter takes that chapter's Burmese;
  3. frames (question, «– ayaṃ vuccati "X"», «ime N X», enumerations, identities) over the NAME table;
  4. synonym lists through ITEMS: the pi-1 lists are read from the pi-1 Burmese (counts asserted), spelling twins
     of pi-1 items take pi-1's Burmese, new items are logged;
  5. prose clauses through the PH table and the pattern builders (māna, taṇhāvicarita, diṭṭhi, kusītavatthu …).
A sentence nothing matches stops the run (Miss); nothing is guessed. The chapter is written only when every line
passed. --notes prints the new strings (for notes-ch17.md).
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my2_formulas as F  # noqa: E402

P1 = F.P1
C, END, PE = F.C, F.END, F.PE
Miss = F.Miss
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
NAME_OUT = "17-khuddakavatthuvibhango.md"
ID = F.ID_RE
VAR = re.compile(r" ?\[[^\]]*\]")
NEW = {}
SLIPS = []
REUSE = {"p1": 0, "p2": 0}


def new(sec, d):
    NEW.setdefault(sec, {}).update(d)
    return d


# ===================================================================================== pi-1 / pi-2 sentences
def psplit(l):
    l = ID.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def bsplit(l):
    return [s for s in re.split(r"(?<=။) ", ID.sub("", l)) if s]


def _table(pdir, bdir, skip=()):
    S = {}
    for p in sorted(pdir.glob("*.md")):
        if p.name in skip or not (bdir / p.name).exists():
            continue
        for a, b in zip(p.read_text(encoding="utf-8-sig").split("\n"), (bdir / p.name).read_text(
                encoding="utf-8").split("\n")):
            if a.startswith("#"):
                continue
            ps, bs = psplit(a), bsplit(b)
            if len(ps) != len(bs):
                continue
            for x, y in zip(ps, bs):
                S.setdefault(x.replace("upādinn", "upādiṇṇ"), y)
    return S


S1 = _table(F.P1_PALI, F.P1_RAILS)
S2 = _table(PALI, OUT, skip=(NAME_OUT,))


def p1(prefix, S=S1):
    hits = [x for x in S if x.startswith(prefix)]
    if not hits:
        raise SystemExit("pi-1 sentence not found: " + prefix)
    return S[min(hits, key=len)]


def p1_name(prefix, S=S1):
    """X of a pi-1 «… – ဤသည်ကို Xဟု ခေါ်သည်။» sentence."""
    y = p1(prefix, S)
    m = re.search(r"ဤသည်ကို “?(.+?)”?ဟု ခေါ်သည်။$", y)
    if not m:
        raise SystemExit("no name in " + y[-80:])
    return m[1]


TB = {}
for _l in (ROOT / "AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    _m = re.match(r"^([^:{]+): \{(.*)\}\s*$", _l)
    if _m:
        TB.setdefault(_m[1].strip(), _m[2].rsplit(": ", 1)[-1])
T = F.T


def tb(k):
    if k not in TB:
        raise SystemExit("termbase: " + k)
    return TB[k]



# ===================================================================================== list items
ITEMS, ITEM_SRC = {}, {}
MULTI = {"cittassa sārāgo", "cittassa āghāto", "cittassa byāpatti", "anattamanatā cittassa",
         "ketukamyatā cittassa", "thambhitattaṃ cittassa", "bhantattaṃ cittassa", "cetaso vikkhepo",
         "aggahitattaṃ cittassa", "thīyitattaṃ cittassa", "thiyitattaṃ cittassa", "cetaso abhiniropanā",
         "lobho akusalamūlaṃ", "moho akusalamūlaṃ", "cittassa uddhaccaṃ", "cittassa akalyatā", "appaṭisaṅkhā bhojane"}
MULTI_SPLIT = {"lobho akusalamūlaṃ": 2, "moho akusalamūlaṃ": 2}


def _toks(pali):
    t = VAR.sub("", pali).split(" ")
    out, i = [], 0
    while i < len(t):
        if " ".join(t[i:i + 2]) in MULTI and " ".join(t[i:i + 2]) not in MULTI_SPLIT:
            out.append(" ".join(t[i:i + 2]))
            i += 2
        else:
            out.append(t[i])
            i += 1
    return out


HOMO = {"rūpataṇhā": "rūpataṇhā@realm"}     # lobha list: rūpataṇhā twice (realm, then sense object)


def add_items(pairs, src):
    for p, m in pairs:
        if p in HOMO and p in ITEMS and ITEMS[p] != m and HOMO[p] not in ITEMS:
            ITEMS[HOMO[p]] = ITEMS[p]          # first occurrence = the realm sense
            ITEMS[p] = m
            continue
        if p in HOMO and HOMO[p] in ITEMS and m == ITEMS[HOMO[p]]:
            continue
        if ITEMS.get(p, m) != m:
            raise SystemExit(f"item conflict {p}: «{ITEMS[p]}» / «{m}» ({src})")
        ITEMS[p] = m
        ITEM_SRC.setdefault(p, src)


def p1_list(prefix, S=S1, my_prefix="", start=None):
    """Items of a pi-1 / pi-2 list sentence «[Yo …] L – …»: Pāli tokens (MULTI joined) zipped with the Burmese
    items (after my_prefix, up to «ရှိသမျှ» / « –»); counts asserted."""
    hits = [x for x in S if x.startswith(prefix)]
    if not hits:
        raise SystemExit("list not found: " + prefix)
    x = min(hits, key=len)
    y = VAR.sub("", S[x])
    pali = x.split(" – ")[0]
    if start:
        pali = pali[pali.index(start):]
    else:
        pali = re.sub(r"^(?:Yo|Yā|Yaṃ)(?: evarūpo| evarūpā| evarūpaṃ)? ", "", pali)
    my = y.split(" – ")[0].removesuffix(" ရှိသမျှ")
    if my_prefix:
        if not my.startswith(my_prefix):
            raise SystemExit(f"prefix «{my_prefix}» not in «{my[:60]}»")
        my = my[len(my_prefix):]
    pt, mt = _toks(pali), my.split(C + " ")
    if len(pt) != len(mt):
        raise SystemExit(f"list {prefix[:40]}: {len(pt)} Pāli / {len(mt)} Burmese\n{pt}\n{mt}")
    add_items(zip(pt, mt), "pi-1" if S is S1 else "pi-2")
    return pt


EV = "ဤသို့ သဘောရှိသော "
p1_list("Yo rāgo sārāgo anunayo anurodho nandī nandīrāgo cittassa")
p1_list("Yo evarūpo cittassa āghāto paṭighāto", my_prefix=EV)
p1_list("Yaṃ evarūpaṃ aññāṇaṃ adassanaṃ", my_prefix=EV)
p1_list("Yā evarūpā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ", my_prefix=EV)
p1_list("Yo evarūpo māno maññanā", my_prefix=EV)
p1_list("Yo kāmesu kāmacchando kāmarāgo", start="kāmacchando", my_prefix="ကာမတို့၌ ရှိသော ")
p1_list("Yo bhavesu bhavachando bhavarāgo", start="bhavachando", my_prefix="ဘဝတို့၌ ရှိသော ")
p1_list("Yā tasmiṃ samaye saññā sañjānanā", start="saññā", my_prefix="ထိုအချိန်၌ ")
p1_list("Yā evarūpā kaṅkhā kaṅkhāyanā", my_prefix=EV)
p1_list("Yaṃ cittassa uddhaccaṃ avūpasamo", start="cittassa uddhaccaṃ")
ISSA_HEAD = VAR.sub("", p1("Yā paralābhasakkāra")).split("တို့၌ ဖြစ်သော ")[0] + "တို့၌ ဖြစ်သော "
p1_list("Yā paralābhasakkāra", start="issā", my_prefix=ISSA_HEAD)
p1_list("Yaṃ evarūpaṃ maccheraṃ", my_prefix=EV)
p1_list("Yā asati ananussati")
p1_list("Sahadhammike vuccamāne dovacassāyaṃ", start="dovacassāyaṃ",
        my_prefix="တရားနှင့် လျော်စွာ သွန်သင် ပြောဆိုသောအခါ ")
add_items(zip(["kāyiko vītikkamo", "vācasiko vītikkamo", "kāyikavācasiko vītikkamo"],
              p1("Yo kāyiko vītikkamo, vācasiko").split(" ရှိသမျှ")[0].split(C + " ")), "pi-1")
p1_list("Yā cittassa akalyatā", S=S2, start="cittassa akalyatā")
p1_list("Yā imesaṃ channaṃ indriyānaṃ agutti", S=S2, start="agutti")
p1_list("Yā tattha asantuṭṭhitā", start="asantuṭṭhitā", my_prefix="ထို၌ ရှိသော ")
_tk = p1("Byāpādapaṭisaṃyutto takko vitakko", S2).split(" – ")[0].split(" ", 2)[2]
_tk = re.fullmatch(r"(?P<a>.+?)၊ (?P<b>.+?)… (?P<c>.+)", _tk)
add_items([("takko", _tk["a"]), ("vitakko", _tk["b"]), ("micchāsaṅkappo", _tk["c"])], "pi-2")
# pāpamittatā: «ထိုသူတို့ကို ပေါင်းသင်းခြင်း၊ …» after the persons clause
_pm = VAR.sub("", p1("Ye te puggalā assaddhā"))
_pm_head, _pm_list = _pm.split(" ရှိကြ၏" + C + " ")
_pm_list = _pm_list.split(" ရှိသမျှ")[0].split(" – ")[0]
_PM_TOK = "sevanā nisevanā saṃsevanā bhajanā sambhajanā bhatti sambhatti taṃsampavaṅkatā".split()
_pm_my = _pm_list.removeprefix("ထိုသူတို့ကို ").split(C + " ")
assert len(_pm_my) == len(_PM_TOK), _pm_my
add_items(zip(_PM_TOK, _pm_my), "pi-1")
PM_PERSONS = _pm_head + " ရှိကြ၏"          # Ye te puggalā assaddhā dussīlā appassutā maccharino duppaññā
PM_TESAM = "ထိုသူတို့ကို "                  # yā tesaṃ (sevanā …)
assert _pm_list.startswith(PM_TESAM)
# vihiṃsā list (pi-2 ch3)
_vh = VAR.sub("", p1("Idhekacco pāṇinā vā leḍḍunā", S2))
VH_HEAD, _vh_list = _vh.split(C + " " + EV)
_vh_list = _vh_list.split(" ရှိသမျှ")[0]
_VH_TOK = "heṭhanā viheṭhanā hiṃsanā vihiṃsanā rosanā virosanā parūpaghāto".split()
assert len(_vh_list.split(C + " ")) == len(_VH_TOK)
add_items(zip(_VH_TOK, _vh_list.split(C + " ")), "pi-2")

# spelling twins of pi-1 items (same word)
TWIN = new("Spelling twins (pi-1 / pi-2 Burmese of the other spelling)", {
    "nandirāgo": "nandīrāgo", "parigedho": "paligedho", "āyūhanī": "āyūhinī", "āsīsanā": "āsisanā",
    "āsīsitattaṃ": "āsisitattaṃ", "chadanaṃ": "chādanaṃ", "unnāmo": "unnamo", "bhavacchando": "bhavachando",
    "vippaṭikulaggāhitā": "vippaṭikūlaggāhitā", "appatissavatā": "appaṭissavatā", "assati": "asati",
    "assaraṇatā": "asaraṇatā", "thīyanā": "thiyanā", "thīyitattaṃ cittassa": "thiyitattaṃ cittassa",
    "chambhitattaṃ": "thambhitattaṃ",
})
MULTI |= {"thīyitattaṃ cittassa"}

# new items (Vb only)
add_items(new("List items (new)", {
    "sotaṃ": "ရေစီးကြောင်း", "jappā": ITEMS["jappā"],
    # mada
    "mado": "မူးယစ်မှု", "majjanā": "မူးယစ်ခြင်း", "majjitattaṃ": "မူးယစ်ထားသော အဖြစ်",
    # pamāda / kosajja
    "vossaggo": "လွှတ်ထားခြင်း", "vossaggānuppadānaṃ": "လွှတ်ထားခြင်းကို ထပ်ကာထပ်ကာ ပြုခြင်း",
    "asakkaccakiriyatā": "ရိုရိုသေသေ မပြုခြင်း", "asātaccakiriyatā": "ထပ်ကာထပ်ကာ မပြုခြင်း",
    "anaṭṭhitakiriyatā": "တည်တံ့စွာ မပြုခြင်း", "olīnavuttitā": "တွန့်ဆုတ်သော အကျင့် ရှိခြင်း",
    "nikkhittachandatā": "ဆန္ဒကို ချထားခြင်း", "nikkhittadhuratā": "တာဝန်ကို ချထားခြင်း",
    "anāsevanā": "မမှီဝဲခြင်း", "abhāvanā": "မပွားများခြင်း", "abahulīkammaṃ": "အဖန်ဖန် မပြုခြင်း",
    "anadhiṭṭhānaṃ": "မဆောက်တည်ခြင်း", "ananuyogo": "အားမထုတ်ခြင်း", "pamādo": "မေ့လျော့မှု",
    "pamajjanā": "မေ့လျော့ခြင်း", "pamajjitattaṃ": "မေ့လျော့ထားသော အဖြစ်",
    # thambha
    "thambho": "တောင့်တင်းမှု", "thambhanā": tb("thambhanā"), "thambhitattaṃ": tb("thambhitattaṃ"), "kakkhaḷiyaṃ": "ကြမ်းတမ်းခြင်း",
    "phārusiyaṃ": "ကြမ်းကြုတ်သော အဖြစ်", "ujucittatā": "စိတ် ခေါင်းမာခြင်း", "amudutā": "မနူးညံ့ခြင်း",
    # sārambha
    "sārambho": "ပြိုင်ဆိုင်မှု", "paṭisārambho": "ပြန်လည် ပြိုင်ဆိုင်မှု", "sārambhanā": "ပြိုင်ဆိုင်ခြင်း",
    "paṭisārambhanā": "ပြန်လည် ပြိုင်ဆိုင်ခြင်း", "paṭisārambhitattaṃ": "ပြန်လည် ပြိုင်ဆိုင်ထားသော အဖြစ်",
    # icchā (atricchatā …)
    "icchāgatā": "အလိုရှိမှုသို့ ရောက်ခြင်း", "atricchatā": "အလွန်အကျွံ လိုချင်ခြင်း",
    "mahicchatā": "လိုချင်မှု ကြီးခြင်း", "pāpicchatā": "ယုတ်မာသော အလိုရှိခြင်း",
    "asantuṭṭhitā": ITEMS["asantuṭṭhitā"],
    # siṅga
    "siṅgaṃ": "ကြွားလုံး ထုတ်မှု", "siṅgāratā": "ကြွားလုံး ထုတ်ခြင်း", "cāturatā": "လိမ္မာဟန် ပြခြင်း",
    "cāturiyaṃ": "လိမ္မာဟန် ပြသော အဖြစ်", "parikkhattatā": "ကြော့ရှင်းဟန် ပြခြင်း",
    "pārikkhattiyaṃ": "ကြော့ရှင်းဟန် ပြသော အဖြစ်",
    # tintiṇa
    "tintiṇaṃ": "ငမ်းငမ်းတက် မြည်တမ်းမှု", "tintiṇāyanā": "ငမ်းငမ်းတက် မြည်တမ်းခြင်း",
    "tintiṇāyitattaṃ": "ငမ်းငမ်းတက် မြည်တမ်းထားသော အဖြစ်",
    # cāpalya
    "cīvaramaṇḍanā": "သင်္ကန်းကို အလှဆင်ခြင်း", "pattamaṇḍanā": "သပိတ်ကို အလှဆင်ခြင်း",
    "senāsanamaṇḍanā": "ကျောင်းအိပ်ရာနေရာကို အလှဆင်ခြင်း", "maṇḍanā": "အလှဆင်ခြင်း",
    "vibhūsanā": "တန်ဆာဆင်ခြင်း", "keḷanā": "ကစားခြင်း", "parikeḷanā": "အမျိုးမျိုး ကစားခြင်း",
    "giddhikatā": "မက်မောခြင်း", "giddhikattaṃ": "မက်မောထားသော အဖြစ်", "capalatā": "ပေါ့ပျက်ခြင်း",
    "cāpalyaṃ": "ပေါ့ပျက်မှု",
    # asabhāgavutti / dovacassatā
    "vipaccanīkasātatā": ITEMS["vipaccanīkasātatā"], "anādariyatā": "မလေးစားသော သဘော",
    "agāravatā": ITEMS["agāravatā"],
    # arati
    "arati": "မမွေ့လျော်မှု", "aratitā": "မမွေ့လျော်သော အဖြစ်", "anabhirati": "မပျော်မွေ့ခြင်း",
    "anabhiramaṇā": "မပျော်မွေ့နေခြင်း", "ukkaṇṭhitā": "ငြီးငွေ့ခြင်း", "paritassitā": "ပူပန်ခြင်း",
    # tandī
    "tandī": "ပျင်းရိငိုက်မျဉ်းမှု", "tandiyanā": "ပျင်းရိငိုက်မျဉ်းခြင်း",
    "tandimanakatā": "ပျင်းရိငိုက်မျဉ်းသော စိတ် ရှိခြင်း", "ālasyaṃ": "ပျင်းရိခြင်း",
    "ālasyāyanā": "ပျင်းရိနေခြင်း", "ālasyāyitattaṃ": "ပျင်းရိထားသော အဖြစ်",
    # vijambhitā
    "kāyassa jambhanā": "ကိုယ်၏ သမ်းဝေခြင်း", "vijambhanā": "အကြိမ်ကြိမ် သမ်းဝေခြင်း",
    "ānamanā": "ကိုင်းညွတ်ခြင်း", "vinamanā": "အမျိုးမျိုး ကိုင်းညွတ်ခြင်း", "sannamanā": "ကွေးညွတ်ခြင်း",
    "paṇamanā": "ရှေ့သို့ ညွတ်ခြင်း", "byādhiyakaṃ": "ဖျားနာသကဲ့သို့ ဖြစ်ခြင်း",
    # bhattasammada
    "bhuttāvissa bhattamucchā": "စားပြီးသူ၏ အစာကြောင့် မိန်းမောခြင်း",
    "bhattakilamatho": "အစာကြောင့် ပင်ပန်းခြင်း", "bhattapariḷāho": "အစာကြောင့် ပူလောင်ခြင်း",
    "kāyaduṭṭhullaṃ": "ကိုယ် လေးလံခြင်း",
    # kuhanā
    "bhākuṭitā": "မျက်မှောင် ကြုတ်ခြင်း", "bhākuṭiyaṃ": "မျက်မှောင် ကြုတ်ထားသော အဖြစ်",
    "kuhanā": "လှည့်ဖြား ဟန်ဆောင်မှု", "kuhāyanā": "လှည့်ဖြား ဟန်ဆောင်ခြင်း",
    "kuhitattaṃ": "လှည့်ဖြား ဟန်ဆောင်ထားသော အဖြစ်",
    # lapanā
    "ālapanā": "စကား စ၍ ပြောခြင်း", "lapanā": "ချော့မော့ ပြောဆိုခြင်း", "sallapanā": "ရင်းနှီးစွာ ပြောဆိုခြင်း",
    "ullapanā": "မြှောက်ပင့် ပြောဆိုခြင်း", "samullapanā": "အလွန် မြှောက်ပင့် ပြောဆိုခြင်း",
    "unnahanā": "ချည်နှောင်သကဲ့သို့ ပြောခြင်း", "samunnahanā": "အလွန် ချည်နှောင်သကဲ့သို့ ပြောခြင်း",
    "ukkācanā": "ချီးမွမ်း ပြောဆိုခြင်း", "samukkācanā": "အလွန် ချီးမွမ်း ပြောဆိုခြင်း",
    "anuppiyabhāṇitā": "နားဝင်ချိုအောင် ပြောခြင်း", "cāṭukamyatā": "ဖားယားလိုခြင်း",
    "muggasūpyatā": "ပဲဟင်းကဲ့သို့ အမှန်အမှား ရောယှက် ပြောခြင်း", "pāribhaṭayatā": "ကလေးထိန်းသကဲ့သို့ ချော့မော့ခြင်း",
    # nemittikatā
    "nimittaṃ": "အရိပ်အမြွက် ပြခြင်း", "nimittakammaṃ": "အရိပ်အမြွက် ပြုခြင်း", "obhāso": "သွယ်ဝိုက် ပြောခြင်း",
    "obhāsakammaṃ": "သွယ်ဝိုက် ပြောဆိုမှု ပြုခြင်း", "sāmantajappā": "အနီးအနား စကား ပြောခြင်း",
    "parikathā": "ပတ်လည် စကား ပြောခြင်း",
    # nippesikatā
    "akkosanā": "ဆဲရေးခြင်း", "vambhanā": "နှိမ့်ချ ပြောခြင်း", "garahaṇā": "ကဲ့ရဲ့ခြင်း",
    "ukkhepanā": "မြှောက်ပင့်ခြင်း", "samukkhepanā": "အလွန် မြှောက်ပင့်ခြင်း", "khipanā": "ပစ်ချခြင်း",
    "saṅkhipanā": "အလွန် ပစ်ချခြင်း", "pāpanā": "အသရေဖျက်ခြင်း", "sampāpanā": "အလွန် အသရေဖျက်ခြင်း",
    "avaṇṇahārikā": "ကဲ့ရဲ့ သတင်း ဆောင်ခြင်း", "parapiṭṭhimaṃsikatā": "ကွယ်ရာတွင် အတင်းပြောခြင်း",
    # lābhena lābhaṃ
    "eṭṭhi": "ရှာခြင်း", "gaveṭṭhi": "စုံစမ်းခြင်း", "pariyeṭṭhi": "အနှံ့ ရှာခြင်း", "esanā": "ရှာမှီးခြင်း",
    "gavesanā": "စုံစမ်း ရှာမှီးခြင်း", "pariyesanā": "အနှံ့ ရှာမှီးခြင်း",
    # omāna
    "omāno": "ယုတ်ညံ့ဟု ထင်မှတ်မှု", "omaññanā": "ယုတ်ညံ့ဟု ထင်မှတ်ခြင်း",
    "omaññitattaṃ": "ယုတ်ညံ့ဟု ထင်မှတ်ထားသော အဖြစ်", "hīḷanā": "မိမိကိုယ်ကို နှိမ့်ချခြင်း",
    "ohīḷanā": "မိမိကိုယ်ကို အလွန် နှိမ့်ချခြင်း", "ohīḷitattaṃ": "မိမိကိုယ်ကို နှိမ့်ချထားသော အဖြစ်",
    "attuññā": "မိမိကိုယ်ကို အထင်သေးခြင်း", "attavaññā": "မိမိကိုယ်ကို လျစ်လျူရှုခြင်း",
    "attaparibhavo": "မိမိကိုယ်ကို စော်ကားခြင်း",
    # kodha / upanāha
    "upanāho": "ရန်ငြိုး သိုထားမှု", "upanayhanā": "ရန်ငြိုး သိုထားခြင်း",
    "upanayhitattaṃ": "ရန်ငြိုး သိုထားသော အဖြစ်",
    "anusaṃsandanā": "ရန်ငြိုးကို ဆက်စပ်ထားခြင်း", "anuppabandhanā": "ရန်ငြိုးကို ဆက်တိုက် ဖွဲ့ထားခြင်း",
    "daḷhīkammaṃ kodhassa": "အမျက်ဒေါသကို ခိုင်မြဲအောင် ပြုခြင်း",
    # makkha / paḷāsa
    "makkho": "ကျေးဇူး ချေဖျက်မှု", "makkhāyanā": "ကျေးဇူး ချေဖျက်ခြင်း",
    "makkhāyitattaṃ": "ကျေးဇူး ချေဖျက်ထားသော အဖြစ်", "niṭṭhuriyaṃ": "ရက်စက်ခြင်း",
    "niṭṭhuriyakammaṃ": "ရက်စက်စွာ ပြုခြင်း", "paḷāso": "တုပြိုင်မှု", "paḷāsāyanā": "တုပြိုင်ခြင်း",
    "paḷāsāhāro": "တုပြိုင်မှုကို ဆောင်ခြင်း", "vivādaṭṭhānaṃ": "အငြင်းပွားရာ အကြောင်း",
    "yugaggāho": "တန်းတူ ဆွဲကိုင်ခြင်း", "appaṭinissaggo": "မစွန့်လွှတ်ခြင်း",
    # māyā / sāṭheyya
    "māyā": ITEMS["māyā"], "māyāvitā": "လှည့်စားတတ်သော အဖြစ်", "accāsarā": "အပြစ်ကို ကျော်လွှားခြင်း",
    "vañcanā": "လိမ်လည်ခြင်း", "nikati": "ကောက်ကျစ်ခြင်း", "vikiraṇā": "ဖုံးကွယ်ရန် ဖြန့်ကြဲခြင်း",
    "pariharaṇā": "ရှောင်တိမ်းခြင်း", "gūhanā": "ဝှက်ထားခြင်း", "parigūhanā": "အနှံ့ ဝှက်ထားခြင်း",
    "chādanā": "ဖုံးခြင်း", "paṭicchādanā": "ဖုံးကွယ်ခြင်း", "anuttānīkammaṃ": "ထင်ရှားအောင် မပြုခြင်း",
    "anāvikammaṃ": "ပေါ်လွင်အောင် မပြုခြင်း", "vocchādanā": "ကောင်းစွာ ဖုံးအုပ်ခြင်း",
    "pāpakiriyā": "ယုတ်မာသော အမှုကို ပြုခြင်း",
    "saṭhaṃ": "စဉ်းလဲမှု", "saṭhatā": "စဉ်းလဲခြင်း", "sāṭheyyaṃ": "စဉ်းလဲသော အဖြစ်",
    "kakkaratā": "ကောက်ကွေးခြင်း", "kakkariyaṃ": "ကောက်ကွေးသော အဖြစ်",
    # bhavataṇhā list
    "bhavasineho": "ဘဝကို ချစ်ခင်မှု" if "bhavasineho" not in ITEMS else ITEMS["bhavasineho"],
    # anajjava / amaddava
    "anajjavo": "မဖြောင့်မတ်မှု", "anajjavatā": "မဖြောင့်မတ်သော အဖြစ်", "jimhatā": "ကောက်ကျစ်သော အဖြစ်",
    "vaṅkatā": "ကွေးကောက်ခြင်း", "kuṭilatā": "တွန့်လိမ်ခြင်း", "amaddavatā": "မနူးညံ့သော အဖြစ်",
    "kakkhaḷatā": "ကြမ်းတမ်းသော အဖြစ်", "kaṭhinatā": "မာကျောခြင်း",
    # akkhanti
    "akkhanti": "မသည်းခံခြင်း", "akkhamanatā": "မသည်းခံနိုင်သော အဖြစ်", "anadhivāsanatā": "သည်းမခံနိုင်ခြင်း",
    # asākhalya
    "asaṇhavācatā": "စကား မပြေပြစ်ခြင်း", "asakhilavācatā": "စကား မချိုမြိန်ခြင်း",
    "pharusavācatā": "စကား ကြမ်းတမ်းခြင်း",
    # lokadhamma etc
    "uññā": "အထင်သေးခြင်း", "avaññā": "လျစ်လျူရှုခြင်း", "paribhavo": "စော်ကားခြင်း",
    "randhagavesitā": "အပြစ်အနာအဆာ ရှာခြင်း", "upārambho": "အပြစ်ရှာမှု", "anupārambho": "အဖန်ဖန် အပြစ်ရှာမှု",
    "upārambhanā": "အပြစ်ရှာခြင်း", "anupārambhanā": "အဖန်ဖန် အပြစ်ရှာခြင်း",
    "anupārambhitattaṃ": "အဖန်ဖန် အပြစ်ရှာထားသော အဖြစ်",
    # ariyānaṃ adassana / saddhamma
    "adassanakamyatā": "မဖူးမြင်လိုခြင်း", "adaṭṭhukamyatā": "မတွေ့မြင်လိုခြင်း", "asametukamyatā": "မဆုံလိုခြင်း",
    "asamāgantukamyatā": "မပေါင်းဆုံလိုခြင်း", "asotukamyatā": "မနာကြားလိုခြင်း",
    "asavanakamyatā": "နားမထောင်လိုခြင်း", "anuggahetukamyatā": "မသင်ယူလိုခြင်း",
    "adhāretukamyatā": "မဆောင်ထားလိုခြင်း",
    # assaddhiya
    "assaddhiyaṃ": "ယုံကြည်မှု မရှိခြင်း", "assaddahanā": "မယုံကြည်ခြင်း", "anokappanā": "သက်ဝင်၍ မယုံကြည်ခြင်း",
    "anabhippasādo": "ကြည်ညိုလေးစားခြင်း မရှိခြင်း",
    # anādariya
    "anaddā": "အလေးဂရု မပြုခြင်း", "anaddāyanā": "အလေးဂရု မပြုနေခြင်း",
    "anaddāyitattaṃ": "အလေးဂရု မပြုထားသော အဖြစ်", "asīlyaṃ": "ယဉ်ကျေးသော အလေ့ မရှိခြင်း",
    "acittīkāro": "အလေးမထားခြင်း",
    # pāpamittatā (pi-2 ^2-U21 adds paṭisevanā)
    "paṭisevanā": "ပြန်လည် ပေါင်းသင်းခြင်း", "sampavaṅkatā": ITEMS["taṃsampavaṅkatā"].removeprefix("ထိုသူတို့ဘက်သို့ "),
    # manasikāra
    "āvaṭṭanā": "လှည့်ခြင်း", "anāvaṭṭanā": "အဖန်ဖန် လှည့်ခြင်း", "ābhogo": "စိတ်ညွတ်ခြင်း",
    "samannāhāro": "စိတ်ကို ဆောင်ခြင်း", "manasikāro": "နှလုံးသွင်းခြင်း",
    # bhaya
    "bhayaṃ": "ကြောက်ခြင်း", "bhayānakaṃ": "ကြောက်မက်ဖွယ် ဖြစ်ခြင်း", "lomahaṃso": "ကြက်သီးမွေးညင်း ထခြင်း",
    "cetaso utrāso": "စိတ်၏ ထိတ်လန့်ခြင်း",
    # saññā / agati
    "sañjānanā": ITEMS.get("sañjānanā", "မှတ်သိခြင်း"), "sañjānitattaṃ": ITEMS.get("sañjānitattaṃ", "မှတ်သိထားသော အဖြစ်"),
    "agati": "အဂတိ", "agatigamanaṃ": "အဂတိ လိုက်ခြင်း", "chandagamanaṃ": "ဆန္ဒ အဂတိ လိုက်ခြင်း",
    "vaggagamanaṃ": "ဂိုဏ်းဖွဲ့၍ လိုက်ခြင်း", "vārigamanaṃ": "ရေကဲ့သို့ စီးဆင်း လိုက်ခြင်း",
    # vipariyāsa
    "saññāvipariyāso": "မှတ်သိမှု ပြောင်းပြန်", "cittavipariyāso": "စိတ် ပြောင်းပြန်",
    "diṭṭhivipariyāso": "အယူ ပြောင်းပြန်",
    # rāga sārāga
    "rāgo": ITEMS["rāgo"], "sārāgo": ITEMS["sārāgo"],
    # gehasita vedanā
    "gehasitaṃ cetasikaṃ sātaṃ": "လောကီ အိမ်ရာကို မှီသော စိတ်၌ ဖြစ်သော ချမ်းသာမှု",
    "cetasikaṃ sukhaṃ": "စိတ်၌ ဖြစ်သော သာယာမှု", "cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ":
        "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ချမ်းသာ သာယာစွာ ခံစားခြင်း",
    "cetosamphassajā sātā sukhā vedanā": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ချမ်းသာ သာယာသော ခံစားမှု",
    "gehasitaṃ cetasikaṃ asātaṃ": "လောကီ အိမ်ရာကို မှီသော စိတ်၌ ဖြစ်သော မချမ်းသာမှု",
    "cetasikaṃ dukkhaṃ": "စိတ်၌ ဖြစ်သော နာကျင်မှု", "cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ":
        "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မချမ်းသာ နာကျင်စွာ ခံစားခြင်း",
    "cetosamphassajā asātā dukkhā vedanā": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မချမ်းသာ နာကျင်သော ခံစားမှု",
    "gehasitaṃ cetasikaṃ neva sātaṃ nāsātaṃ": "လောကီ အိမ်ရာကို မှီသော စိတ်၌ ဖြစ်သော ချမ်းသာမှုလည်း မဟုတ်၊ "
                                             "မချမ်းသာမှုလည်း မဟုတ်သော",
    "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မနာကျင် မသာယာစွာ ခံစားခြင်း",
    "cetosamphassajā adukkhamasukhā vedanā": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မနာကျင် မသာယာသော ခံစားမှု",
    # āghāta (virodhavatthu)
    "cittassa āghāto": ITEMS["cittassa āghāto"],
}).items(), "new")
for _a, _b in TWIN.items():
    if _b in ITEMS and _a not in ITEMS:
        add_items([(_a, ITEMS[_b])], "twin")
ITEMS["rūpataṇhā arūpataṇhā"] = ITEMS["rūpataṇhā@realm"] + C + " " + ITEMS["arūpataṇhā"]   # the realm pair
for _k in list(ITEMS):
    if " " in _k:
        MULTI.add(_k)
ITEM_MAX = max(len(k.split()) for k in ITEMS)


def list_my(text, rel=False, ev=False):
    """Synonym list (pāli words, «…pe…», «…», variants) -> Burmese items «၊ »; «Yo …» adds «ရှိသမျှ»."""
    toks = re.findall(r"\[[^\]]*\]|…pe…|…|, |[^\s\[…,]+", text)
    words, var_after, pe_after, comma_after = [], {}, set(), set()
    for t in toks:
        if t.startswith("["):
            var_after.setdefault(len(words) - 1, []).append(t)
        elif t in ("…pe…", "…"):
            pe_after.add(len(words) - 1)
        elif t == ", ":
            comma_after.add(len(words) - 1)
        else:
            words.append(t)
    out, i, seen = "", 0, {}
    while i < len(words):
        for k in range(ITEM_MAX, 0, -1):
            key = " ".join(words[i:i + k])
            if i == 0:
                key = key[:1].lower() + key[1:] if key[:1].lower() + key[1:] in ITEMS else key
            if i + k <= len(words) and key in ITEMS and not any(j in pe_after for j in range(i, i + k - 1)):
                break
        else:
            raise Miss("list item: " + words[i] + "  in: " + text[:100])
        my = ITEMS[key]
        if my in seen and seen[my] != key and not (TWIN.get(key) == seen[my] or TWIN.get(seen[my]) == key):
            raise Miss(f"two items share «{my}»: {seen[my]} / {key}")
        seen[my] = key
        vs = [v.strip() for j in range(i, i + k) for v in var_after.get(j, [])]
        out += my + "".join(" " + var(v) for v in vs)
        last = i + k - 1
        i += k
        if i < len(words):
            out += (PE + " ") if last in pe_after else (C + " ")
        elif last in pe_after:
            out += PE
    LISTS.append(len(words))
    return (EV if ev else "") + out + (" ရှိသမျှ" if rel else "")


LISTS = []


def is_list(text):
    try:
        list_my(text)
        LISTS.pop()
        return True
    except Miss:
        return False


# ===================================================================================== variants, editorial
SIG = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "sī. syā.": "Sī., Syā.", "sī. ka.": "Sī., Ka.",
       "syā. ka.": "Syā., Ka.", "sī. syā. ka.": "Sī., Syā., Ka.", "saddanībhi": "Saddanīti", "?": "အမည်မသိ မူ", "sī. syā. ka.": "Sī., Syā., Ka."}
VAR_SPELL = {"cetaso līnattaṃ", "palāso", "nijigiṃsanatā", "jigiṃsanatā", "uṇṇati uṇṇāmo", "makkhiyanā makkhiyitattaṃ",
             "palāsāyanā palāsāyitattaṃ", "kathinatā", "visadā", "āyūhinī", "sandhavo", "āsiṃsanā āsiṃsitattaṃ",
             "vipariyesā", "cetasovinibaddhā", "vijjaṭṭhānena", "kumbhīrabhayaṃ", "kumbhīḷabhayaṃ",
             "cātummahābhūtiko", "evaṃdiṭṭhi", "appaṭisandhāro", "āṭhapanā", "codiyamāno", "anādā anādāyanā anādāyitattaṃ",
             "gilānavuṭṭhito", "samaggatā", "anavakārī", "avakārī", "paraṃ puggalaṃ"}
REF = new("Editorial references in variant brackets", {
    "dha. sa.": "သဘောတရားများကို စုစည်းရေတွက်ခြင်း", "dī. ni.": "ဒီဃနိကာယ်", "a. ni.": "အင်္ဂုတ္တရနိကာယ်"})


REF_RE = re.compile(r" (?P<b>dha\. sa\.|dī\. ni\.|a\. ni\.) (?P<n>[\d.]+)(?P<x>.*)$")
NOTE = new("Editorial notes in brackets (new)", {
    "pāḷiyā ṭīkā passitabbā": "ပါဠိ၏ ဋီကာကို ကြည့်ပါ", "(kumbha + īra + a = bhaya)": "(kumbha + īra + a = bhaya)"})


def var(v):
    """«[A (s1), B (s2) ref]» -> «[KIND (S1): A၊ (S2): B၊ “Ref” n]» (sample / pi-1 form, kind from P1.var_my)."""
    inner = v[1:-1]
    ref = ""
    m = REF_RE.search(inner)
    if m:
        ref = f"{C} “{REF[m['b']]}” {m['n']}"
        x = m["x"].strip()
        if x:
            if x not in NOTE:
                raise Miss("variant note: " + x)
            ref += " " + NOTE[x]
        inner = inner[:m.start()]
    segs = re.findall(r"(?P<t>[^()]+?) \((?P<s>[^()]+)\)(?:, |$| (?=\())", inner)
    if not segs or "".join(f"{t} ({s_})" for t, s_ in segs).replace(" ", "") != re.sub(r"[, ]", "", inner).replace(
            "", "") and False:
        raise Miss("variant: " + v)
    parts, kind = [], None
    for t, sg in segs:
        sg_my = SIG.get(sg, sg)
        if kind is None:
            try:
                k = F.var_my(f"[{t} ({sg})]")
            except Miss:
                k = P1.LEKHANA if all(w in VAR_SPELL for w in t.split(", ")) or t in VAR_SPELL else P1.PATHA
            kind = P1.LEKHANA if P1.LEKHANA in k else P1.PATHA
            parts.append(f"({sg_my}): {t}")
        else:
            parts.append(f"({sg_my}): {t}")
    rest = re.sub(r"(?P<t>[^()]+?) \((?P<s>[^()]+)\)(?:, |$| (?=\())", "", inner).strip()
    if rest:
        if rest not in NOTE:
            raise Miss("variant rest: " + rest + " in " + v)
        ref += " " + NOTE[rest]
    return f"[{kind} " + f"{C} ".join(parts) + ref + "]"


# ===================================================================================== names (headwords)
NUM = {"tīṇi": "သုံး", "tayo": "သုံး", "tisso": "သုံး", "cattāro": "လေး", "cattāri": "လေး", "catasso": "လေး",
       "pañca": "ငါး", "cha": "ခြောက်", "satta": "ခုနစ်", "aṭṭha": "ရှစ်", "nava": "ကိုး", "dasa": "ဆယ်",
       "dve": "နှစ်", "aṭṭhārasa": "ဆယ့်ရှစ်", "chattiṃsa": "သုံးဆယ့်ခြောက်", "dvāsaṭṭhi": "ခြောက်ဆယ့်နှစ်",
       "soḷasa": "ဆယ့်ခြောက်"}
MADA_BASE = new("Mada bases (X-mado = «Xကြောင့် မူးယစ်မှု»; Xṃ paṭicca = «Xကို စွဲ၍»)", {
    "jāti": "ဇာတိ", "gotta": "အမျိုးအနွယ်", "ārogya": "အနာကင်းခြင်း", "yobbana": "ပျိုရွယ်ခြင်း",
    "jīvita": "အသက်ရှင်ခြင်း", "lābha": "လာဘ်", "sakkāra": "အပူဇော်ခံရခြင်း", "garukāra": "အလေးပြုခံရခြင်း",
    "purekkhāra": "ရှေ့တန်းတင်ခံရခြင်း", "parivāra": "အခြံအရံ", "bhoga": "စည်းစိမ်ဥစ္စာ", "vaṇṇa": "အဆင်းလှခြင်း",
    "suta": "အကြားအမြင်", "paṭibhāna": "လျင်မြန်သော ဉာဏ်", "rattaññu": "ရဟန်းဝါ ကြာမြင့်ခြင်း",
    "piṇḍapātika": "ဆွမ်းခံ ဓုတင် ဆောင်ခြင်း", "anavaññāta": "အထင်မသေးခံရခြင်း", "iriyāpatha": "ကိုယ်ဟန် အမူအရာ",
    "iddhi": "တန်ခိုး", "yasa": "ကျော်ကြားမှု", "sīla": "သီလ", "jhāna": "ဈာန်", "sippa": "အတတ်ပညာ",
    "āroha": "အရပ်အမောင်း မြင့်ခြင်း", "pariṇāha": "ကိုယ်လုံး ပြည့်ဖြိုးခြင်း",
    "saṇṭhāna": "ကိုယ်ဟန် ပုံသဏ္ဌာန် လှပခြင်း", "pāripūri": "ကိုယ်အင်္ဂါ ပြည့်စုံခြင်း",
})
MADA_ACC = {"jātiṃ": "jāti", "gottaṃ": "gotta", "ārogyaṃ": "ārogya", "yobbanaṃ": "yobbana", "jīvitaṃ": "jīvita",
            "lābhaṃ": "lābha", "sakkāraṃ": "sakkāra", "garukāraṃ": "garukāra", "purekkhāraṃ": "purekkhāra",
            "parivāraṃ": "parivāra", "bhogaṃ": "bhoga", "vaṇṇaṃ": "vaṇṇa", "sutaṃ": "suta",
            "paṭibhānaṃ": "paṭibhāna", "rattaññutaṃ": "rattaññu", "piṇḍapātikattaṃ": "piṇḍapātika",
            "anavaññātaṃ": "anavaññāta", "iriyāpathaṃ": "iriyāpatha", "iddhiṃ": "iddhi", "yasaṃ": "yasa",
            "sīlaṃ": "sīla", "jhānaṃ": "jhāna", "sippaṃ": "sippa", "ārohaṃ": "āroha", "pariṇāhaṃ": "pariṇāha",
            "saṇṭhānaṃ": "saṇṭhāna", "pāripūriṃ": "pāripūri"}
MADO = ITEMS["mado"]
NAME = {}
for _k, _v in MADA_BASE.items():
    NAME[_k + "mado"] = f"{_v}ကြောင့် {MADO}"
MANA_SEED = {"seyyohamasmīti māno": "ငါသည် သာလွန်သူ ဖြစ်သည်ဟူသော မာန",
             "sadisohamasmīti māno": "ငါသည် တူညီသူ ဖြစ်သည်ဟူသော မာန",
             "hīnohamasmīti māno": "ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်ဟူသော မာန"}
assert all(v in p1("Seyyohamasmīti māno, sadisohamasmīti māno") for v in MANA_SEED.values())
MANA_SELF = {"seyyo": "သာလွန်သူ", "sadiso": "တူညီသူ", "hīno": "ယုတ်ညံ့သူ"}
MANA_OTHER = new("Māna (new forms)", {"seyyassa": "သာလွန်သူ ဖြစ်လျက်", "sadisassa": "တူညီသူ ဖြစ်လျက်",
                                     "hīnassa": "ယုတ်ညံ့သူ ဖြစ်လျက်"})
NAME.update(MANA_SEED)
NAME["hīno hamasmīti māno"] = MANA_SEED["hīnohamasmīti māno"]          # mātikā spacing
for _o, _om in MANA_OTHER.items():
    for _s, _sm in MANA_SELF.items():
        NAME[f"{_o} {_s}hamasmīti māno"] = f"{_om} ငါသည် {_sm} ဖြစ်သည်ဟူသော မာန"
_D = tb("diṭṭhi")                       # အယူ
NAME.update(new("Names (new unless marked pi-1)", {
    "mado": MADO, "pamādo": ITEMS["pamādo"], "thambho": ITEMS["thambho"], "sārambho": ITEMS["sārambho"],
    "atricchatā": ITEMS["atricchatā"], "mahicchatā": ITEMS["mahicchatā"], "pāpicchatā": ITEMS["pāpicchatā"],
    "siṅgaṃ": ITEMS["siṅgaṃ"], "tintiṇaṃ": ITEMS["tintiṇaṃ"], "cāpalyaṃ": ITEMS["cāpalyaṃ"],
    "asabhāgavutti": "မလျော်ကန်သော ဆက်ဆံမှု", "arati": ITEMS["arati"], "tandī": ITEMS["tandī"],
    "vijambhitā": "သမ်းဝေ ကိုင်းညွတ်မှု", "bhattasammado": "အစာကြောင့် မူးမော့မှု",
    "cetaso ca līnattaṃ": "စိတ်၏ တွန့်ဆုတ်နေမှု", "kuhanā": ITEMS["kuhanā"], "lapanā": ITEMS["lapanā"],
    "nemittikatā": "အရိပ်အမြွက် ပြတတ်ခြင်း", "nippesikatā": "နှိပ်ကွပ် ပြောဆိုတတ်ခြင်း",
    "lābhena lābhaṃ nijigīsanatā": "လာဘ်ဖြင့် လာဘ်ကို ရှာခြင်း",
    "māno": tb("māna"), "atimāno": "အလွန် မာနထားမှု", "mānātimāno": "မာနနှင့် အလွန် မာနထားမှု",
    "omāno": ITEMS["omāno"], "adhimāno": "လွန်ကဲစွာ ထင်မှတ်သော မာန", "asmimāno": "ငါ ရှိ၏ဟူသော မာန",
    "micchāmāno": "မှားယွင်းသော မာန", "ñātivitakko": "ဆွေမျိုးကို စတင်ကြံစည်မှု",
    "janapadavitakko": "ဇာတိ ဇနပုဒ်ကို စတင်ကြံစည်မှု", "amaravitakko": "မသေခြင်းကို ရည်ရွယ်သော စတင်ကြံစည်မှု",
    "parānuddayatāpaṭisaṃyutto vitakko": "သူတစ်ပါးကို စာနာခြင်းနှင့် စပ်ယှဉ်သော စတင်ကြံစည်မှု",
    "lābhasakkārasilokapaṭisaṃyutto vitakko": "လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှုတို့နှင့် စပ်ယှဉ်သော "
                                               "စတင်ကြံစည်မှု",
    "lābhādipaṭisaṃyutto vitakko": "လာဘ် စသည်တို့နှင့် စပ်ယှဉ်သော စတင်ကြံစည်မှု",
    "anavaññattipaṭisaṃyutto vitakko": "အထင်မသေးခံရခြင်းနှင့် စပ်ယှဉ်သော စတင်ကြံစည်မှု",
    # duka
    "kodho": tb("kodho"), "upanāho": ITEMS["upanāho"], "makkho": ITEMS["makkho"], "paḷāso": ITEMS["paḷāso"],
    "issā": tb("issā"), "macchariyaṃ": tb("macchariya"), "māyā": ITEMS["māyā"], "sāṭheyyaṃ": ITEMS["sāṭheyyaṃ"],
    "avijjā": tb("avijjā"), "bhavataṇhā": ITEMS["bhavataṇhā"],
    "bhavadiṭṭhi": f"ဘဝဆိုင်ရာ {_D}", "vibhavadiṭṭhi": f"ဘဝ ပျောက်ကွယ်ခြင်းဆိုင်ရာ {_D}",
    "sassatadiṭṭhi": f"မြဲသည်ဟူသော {_D}", "ucchedadiṭṭhi": f"ပြတ်သည်ဟူသော {_D}",
    "antavādiṭṭhi": f"အဆုံး ရှိသည်ဟူသော {_D}", "anantavādiṭṭhi": f"အဆုံး မရှိဟူသော {_D}",
    "pubbantānudiṭṭhi": f"အတိတ်ကာလကို အစွဲပြုသော {_D}", "aparantānudiṭṭhi": f"အနာဂတ်ကာလကို အစွဲပြုသော {_D}",
    "ahirikaṃ": tb("ahirikaṃ"), "anottappaṃ": tb("anottappaṃ"), "dovacassatā": tb("dovacassatā"),
    "pāpamittatā": p1_name("Ye te puggalā assaddhā"), "anajjavo": ITEMS["anajjavo"], "amaddavo": "မနူးညံ့မှု",
    "akkhanti": ITEMS["akkhanti"], "asoraccaṃ": "မယဉ်ကျေးခြင်း", "asākhalyaṃ": "စကား မချိုသာခြင်း",
    "appaṭisanthāro": "ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း မရှိခြင်း",
    "indriyesu aguttadvāratā": p1_name("Yā imesaṃ channaṃ indriyānaṃ agutti", S2),
    "bhojane amattaññutā": p1_name("Yā tattha asantuṭṭhitā"), "muṭṭhassaccaṃ": p1_name("Yā asati ananussati"),
    "asampajaññaṃ": tb("asampajaññaṃ"), "sīlavipatti": p1_name("Yo kāyiko vītikkamo, vācasiko"),
    "diṭṭhivipatti": p1_name("Natthi dinnaṃ, natthi yiṭṭhaṃ, natthi hutaṃ"),
    "ajjhattasaṃyojanaṃ": "အတွင်းပိုင်း နှောင်ကြိုး", "bahiddhāsaṃyojanaṃ": "အပြင်ပိုင်း နှောင်ကြိုး",
    # tika
    "lobho": tb("lobho"), "doso": tb("doso"), "moho": tb("moho"),
    "kāmavitakko": f"ကာမကို {tb('vitakko')}", "byāpādavitakko": f"{tb('byāpādo')}ဆိုင်ရာ {tb('vitakko')}",
    "vihiṃsāvitakko": f"ညှဉ်းပန်းမှုဆိုင်ရာ {tb('vitakko')}",
    "kāmasaññā": f"ကာမကို {tb('saññā')}", "byāpādasaññā": f"{tb('byāpādo')}ဆိုင်ရာ {tb('saññā')}",
    "vihiṃsāsaññā": f"ညှဉ်းပန်းမှုဆိုင်ရာ {tb('saññā')}",
    "kāmadhātu": p1("Tattha katamā kāmadhātu?", S2).split(" ", 1)[1].split(" ဟူသည်")[0],
    "byāpādadhātu": "ဖျက်ဆီးလိုစိတ် ဓာတ်", "vihiṃsādhātu": "ညှဉ်းပန်းမှု ဓာတ်",
    "kāyaduccaritaṃ": "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်", "vacīduccaritaṃ": "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်",
    "manoduccaritaṃ": "မနောဖြင့် ပြုသော ဒုစရိုက်",
    "pāṇātipāto": "သူ့အသက်ကို သတ်ခြင်း", "adinnādānaṃ": "မပေးသည်ကို ယူခြင်း",
    "kāmesumicchācāro": "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း", "musāvādo": "မုသား ပြောခြင်း",
    "pisuṇā vācā": "ကုန်းတိုက်သော စကား", "pharusā vācā": "ကြမ်းတမ်းသော စကား",
    "samphappalāpo": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", "abhijjhā": tb("abhijjhā"), "byāpādo": tb("byāpādo"),
    "micchādiṭṭhi": tb("micchādiṭṭhi"),
    "akusalaṃ kāyakammaṃ": f"{T['akusalā'].removesuffix('သော') if T['akusalā'].endswith('သော') else T['akusalā']} "
                           f"{tb('kāyakammaṃ')}",
    "kāmāsavo": tb("kāmāsavo"), "bhavāsavo": tb("bhavāsavo"), "diṭṭhāsavo": tb("diṭṭhāsavo"),
    "avijjāsavo": tb("avijjāsavo"),
    "sakkāyadiṭṭhi": tb("sakkāyadiṭṭhi"), "vicikicchā": tb("vicikicchā"), "sīlabbataparāmāso": tb("sīlabbataparāmāso"),
    "kāmataṇhā": ITEMS["kāmataṇhā"], "vibhavataṇhā": ITEMS["vibhavataṇhā"], "rūpataṇhā": ITEMS["rūpataṇhā@realm"],
    "arūpataṇhā": ITEMS["arūpataṇhā"], "rūpataṇhā@sense": ITEMS["rūpataṇhā"], "nirodhataṇhā": ITEMS["nirodhataṇhā"], "saddataṇhā": ITEMS["saddataṇhā"],
    "gandhataṇhā": ITEMS["gandhataṇhā"], "rasataṇhā": ITEMS["rasataṇhā"],
    "phoṭṭhabbataṇhā": ITEMS["phoṭṭhabbataṇhā"], "dhammataṇhā": ITEMS["dhammataṇhā"],
    "kāmesanā": "ကာမကို ရှာမှီးမှု", "bhavesanā": "ဘဝကို ရှာမှီးမှု", "brahmacariyesanā": "မြတ်သော အကျင့်ကို ရှာမှီးမှု",
    "jātibhayaṃ": "မွေးဖွားခြင်း ဘေး", "jarābhayaṃ": "အိုခြင်း ဘေး", "maraṇabhayaṃ": "သေခြင်း ဘေး",
    "byādhibhayaṃ": "ဖျားနာခြင်း ဘေး", "rājabhayaṃ": "မင်း ဘေး", "corabhayaṃ": "ခိုးသူ ဘေး",
    "aggibhayaṃ": "မီး ဘေး", "udakabhayaṃ": "ရေ ဘေး", "ūmibhayaṃ": "လှိုင်း ဘေး", "kumbhīlabhayaṃ": "မိကျောင်း ဘေး",
    "āvaṭṭabhayaṃ": "ဝဲဂယက် ဘေး", "susukābhayaṃ": "ငါးဆိုး ဘေး",
    "attānuvādabhayaṃ": "မိမိကိုယ်ကို အပြစ်တင်ခြင်း ဘေး", "parānuvādabhayaṃ": "သူတစ်ပါး အပြစ်တင်ခြင်း ဘေး",
    "daṇḍabhayaṃ": "ဒဏ်ခတ်ခံရခြင်း ဘေး", "duggatibhayaṃ": "ဆိုးသော လားရာ ဘေး",
    "ājīvakabhayaṃ": "အသက်မွေးဝမ်းကျောင်းမှု ဘေး", "asilokabhayaṃ": "အသရေပျက်ခြင်း ဘေး",
    "parisasārajjabhayaṃ": "ပရိသတ်ကို ရွံ့ကြောက်ခြင်း ဘေး",
    "kāyavisamaṃ": "ကိုယ်၏ ဖောက်ပြန်မှု", "vacīvisamaṃ": "နှုတ်၏ ဖောက်ပြန်မှု", "manovisamaṃ": "မနော၏ ဖောက်ပြန်မှု",
    "rāgaggi": "ရာဂ မီး", "dosaggi": "ဒေါသ မီး", "mohaggi": "မောဟ မီး",
    "rāgakasāvo": "ရာဂ အမည်းအစက်", "dosakasāvo": "ဒေါသ အမည်းအစက်", "mohakasāvo": "မောဟ အမည်းအစက်",
    "kāyakasāvo": "ကိုယ်၏ အမည်းအစက်", "vacīkasāvo": "နှုတ်၏ အမည်းအစက်", "manokasāvo": "မနော၏ အမည်းအစက်",
    "assādadiṭṭhi": f"သာယာမှုဆိုင်ရာ {_D}", "attānudiṭṭhi": f"အတ္တဟု အဖန်ဖန် ရှုမြင်သော {_D}",
    "vihesā": "နှိပ်စက်မှု", "adhammacariyā": "တရားနှင့် မညီသော အကျင့်", "nānattasaññā": "အမျိုးမျိုးသော မှတ်သိမှု",
    "uddhaccaṃ": tb("uddhaccaṃ"), "kosajjaṃ": "ပျင်းရိမှု", "asantuṭṭhitā": ITEMS["asantuṭṭhitā"],
    "asampajaññatā": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိသော အဖြစ်", "anādariyaṃ": ITEMS["anādariyaṃ"],
    "assaddhiyaṃ": ITEMS["assaddhiyaṃ"], "avadaññutā": "ပေးကမ်းရန် မလိုလားခြင်း", "asaṃvaro": tb("asaṃvaro"),
    "dussīlyaṃ": "သီလ ပျက်ခြင်း", "ariyānaṃ adassanakamyatā": "အရိယာတို့ကို မဖူးမြင်လိုခြင်း",
    "saddhammaṃ asotukamyatā": "သူတော်ကောင်းတရားကို မနာကြားလိုခြင်း",
    "upārambhacittatā": "အပြစ်ရှာလိုသော စိတ် ရှိခြင်း", "cetaso vikkhepo": ITEMS["cetaso vikkhepo"],
    "ayoniso manasikāro": f"{tb('ayoniso')} နှလုံးသွင်းခြင်း", "kummaggasevanā": "လမ်းမှားကို မှီဝဲခြင်း",
    "kummaggo": ITEMS["kummaggo"], "saddhammo": "သူတော်ကောင်းတရား", "upārambho": ITEMS["upārambho"],
    # catukka
    "kāmupādānaṃ": tb("kāmupādānaṃ"), "diṭṭhupādānaṃ": tb("diṭṭhupādānaṃ"),
    "sīlabbatupādānaṃ": tb("sīlabbatupādānaṃ"), "attavādupādānaṃ": "အတ္တဟူသော ဝါဒ စွဲလမ်းမှု",
    # pañcaka …
    "kāmacchando": tb("kāmacchando"), "rūparāgo": "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ",
    "arūparāgo": "ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ",
    "āvāsamacchariyaṃ": "နေရာထိုင်ခင်း ဝန်တိုမှု", "kulamacchariyaṃ": "ဒါယကာ အိမ်ဝန်း ဝန်တိုမှု",
    "lābhamacchariyaṃ": "လာဘ် ဝန်တိုမှု", "vaṇṇamacchariyaṃ": "ဂုဏ်ကျေးဇူး ဝန်တိုမှု", "dhammamacchariyaṃ": "တရား ဝန်တိုမှု",
    "rāgasaṅgo": "ရာဂ တွယ်ငြိမှု", "dosasaṅgo": "ဒေါသ တွယ်ငြိမှု", "mohasaṅgo": "မောဟ တွယ်ငြိမှု",
    "mānasaṅgo": "မာန တွယ်ငြိမှု", "diṭṭhisaṅgo": "အယူ တွယ်ငြိမှု",
    "rāgasallaṃ": "ရာဂ ငြောင့်", "dosasallaṃ": "ဒေါသ ငြောင့်", "mohasallaṃ": "မောဟ ငြောင့်", "mānasallaṃ": "မာန ငြောင့်",
    "diṭṭhisallaṃ": "အယူ ငြောင့်",
    "kāmacchandanīvaraṇaṃ": tb("kāmacchandanīvaraṇaṃ"), "byāpādanīvaraṇaṃ": tb("byāpādanīvaraṇaṃ"),
    "thinamiddhanīvaraṇaṃ": tb("thinamiddhanīvaraṇaṃ"), "uddhaccakukkuccanīvaraṇaṃ": tb("uddhaccakukkuccanīvaraṇaṃ"),
    "vicikicchānīvaraṇaṃ": tb("vicikicchānīvaraṇaṃ"),
    "surāmerayamajjapamādaṭṭhānā": "မေ့လျော့ခြင်း၏ အကြောင်း ဖြစ်သော သေရည်သေရက် သောက်ခြင်း",
    "ñātibyasanaṃ": "ဆွေမျိုး ပျက်စီးခြင်း", "bhogabyasanaṃ": "စည်းစိမ်ဥစ္စာ ပျက်စီးခြင်း",
    "rogabyasanaṃ": "ကျန်းမာရေး ပျက်စီးခြင်း", "sīlabyasanaṃ": "သီလ ပျက်စီးခြင်း", "diṭṭhibyasanaṃ": "အယူ ပျက်စီးခြင်း",
    # chakka
    "sandiṭṭhiparāmāsitā": "မိမိ အယူကိုသာ စွဲကိုင်ခြင်း",
    "kammārāmatā": "အလုပ်ကို နှစ်သက်ခြင်း", "bhassārāmatā": "စကားပြောခြင်းကို နှစ်သက်ခြင်း",
    "niddārāmatā": "အိပ်ခြင်းကို နှစ်သက်ခြင်း", "saṅgaṇikārāmatā": "အပေါင်းအသင်းကို နှစ်သက်ခြင်း",
    "saṃsaggārāmatā": "ရောနှောခြင်းကို နှစ်သက်ခြင်း", "papañcārāmatā": "ချဲ့ထွင်ခြင်းကို နှစ်သက်ခြင်း",
    # sattaka
    "kāmarāgānusayo": "ကာမရာဂ ကိန်းအောင်းခြင်း", "paṭighānusayo": "မုန်းတီးမှု ကိန်းအောင်းခြင်း",
    "mānānusayo": "မာန ကိန်းအောင်းခြင်း", "diṭṭhānusayo": "အယူ ကိန်းအောင်းခြင်း",
    "vicikicchānusayo": "ယုံမှားမှု ကိန်းအောင်းခြင်း", "bhavarāgānusayo": "ဘဝရာဂ ကိန်းအောင်းခြင်း",
    "avijjānusayo": "အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း",
    "kāmarāgasaṃyojanaṃ": tb("kāmarāgasaṃyojanaṃ"), "paṭighasaṃyojanaṃ": tb("paṭighasaṃyojanaṃ"),
    "mānasaṃyojanaṃ": tb("mānasaṃyojanaṃ"), "diṭṭhisaṃyojanaṃ": tb("diṭṭhisaṃyojanaṃ"),
    "vicikicchāsaṃyojanaṃ": tb("vicikicchāsaṃyojanaṃ"), "bhavarāgasaṃyojanaṃ": tb("bhavarāgasaṃyojanaṃ"),
    "avijjāsaṃyojanaṃ": tb("avijjāsaṃyojanaṃ"), "sīlabbataparāmāsasaṃyojanaṃ": tb("sīlabbataparāmāsasaṃyojanaṃ"),
    "issāsaṃyojanaṃ": tb("issāsaṃyojanaṃ"), "macchariyasaṃyojanaṃ": tb("macchariyasaṃyojanaṃ"),
    "kāmarāgapariyuṭṭhānaṃ": "ကာမရာဂ ထကြွခြင်း", "paṭighapariyuṭṭhānaṃ": "မုန်းတီးမှု ထကြွခြင်း",
    "mānapariyuṭṭhānaṃ": "မာန ထကြွခြင်း", "diṭṭhipariyuṭṭhānaṃ": "အယူ ထကြွခြင်း",
    "vicikicchāpariyuṭṭhānaṃ": "ယုံမှားမှု ထကြွခြင်း", "bhavarāgapariyuṭṭhānaṃ": "ဘဝရာဂ ထကြွခြင်း",
    "avijjāpariyuṭṭhānaṃ": "အမှန်ကို မသိမှု ထကြွခြင်း",
    # aṭṭhaka / dasaka
    "diṭṭhi": _D, "thinaṃ": tb("thinaṃ"),
    "micchāvācā": "မှားယွင်းသော စကား", "micchākammanto": "မှားယွင်းသော အလုပ်",
    "micchāājīvo": "မှားယွင်းသော အသက်မွေးမှု", "micchāvāyāmo": tb("micchāvāyāmo"), "micchāsati": "မှားယွင်းသော သတိ",
    "micchāsamādhi": tb("micchāsamādhi"), "micchāñāṇaṃ": "မှားယွင်းသော ဉာဏ်", "micchāvimutti": "မှားယွင်းသော လွတ်မြောက်မှု",
    "micchāsaṅkappo": tb("micchāsaṅkappo"),
}))
NAME["akusalaṃ kāyakammaṃ"] = f"အကုသိုလ် {tb('kāyakammaṃ')}"
NAME["akusalaṃ vacīkammaṃ"] = f"အကုသိုလ် {tb('vacīkammaṃ')}"
NAME["akusalaṃ manokammaṃ"] = f"အကုသိုလ် {tb('manokammaṃ')}"
NAME.update(new("Names (new)", {
    "akusalā kāyasañcetanā": "အကုသိုလ် ကိုယ်၏ စေ့ဆော်ခြင်း", "akusalā vacīsañcetanā": "အကုသိုလ် နှုတ်၏ စေ့ဆော်ခြင်း",
    "akusalā manosañcetanā": f"အကုသိုလ် {tb('manosañcetanā')}",
}))
# group nouns (plural headwords with a number): Pāli noun -> Burmese noun
GROUP = new("Group nouns («N X» = «X N-ပါး»)", {
    "akusalamūlāni": "အကုသိုလ်၏ အမြစ်", "akusalavitakkā": f"အကုသိုလ် {tb('vitakko')}",
    "akusalasaññā": f"အကုသိုလ် {tb('saññā')}", "akusaladhātuyo": "အကုသိုလ် ဓာတ်", "duccaritāni": "ဒုစရိုက်",
    "āsavā": tb("āsavā"), "saṃyojanāni": tb("saṃyojanāni"), "taṇhā": tb("taṇhā"), "esanā": "ရှာမှီးမှု",
    "vidhā": "နှိုင်းယှဉ် ချိန်ဆမှု", "bhayāni": "ဘေး", "tamāni": "အမှောင်",
    "titthāyatanāni": ITEMS["titthāyatanaṃ"], "kiñcanā": "တွယ်ငြိရာ", "aṅgaṇāni": "အစွန်းအကွက်", "malāni": "အညစ်အကြေး",
    "visamāni": "ဖောက်ပြန်မှု", "aggī": "မီး", "kasāvā": "အမည်းအစက်", "ganthā": tb("ganthā"), "oghā": tb("oghā"),
    "yogā": tb("yogā"), "upādānāni": tb("upādānāni"), "taṇhuppādā": "တပ်မက်မှု ဖြစ်ပေါ်ရာ",
    "agatigamanāni": "အဂတိ လိုက်ခြင်း", "vipariyāsā": "ပြောင်းပြန် ယူဆမှု",
    "anariyavohārā": "အရိယာ မဟုတ်သူတို့၏ ပြောဆိုမှု", "diṭṭhiyo": _D,
    "orambhāgiyāni saṃyojanāni": "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး",
    "uddhambhāgiyāni saṃyojanāni": "အထက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး",
    "macchariyāni": tb("macchariyāni"), "saṅgā": "တွယ်ငြိမှု", "sallā": "ငြောင့်", "cetokhilā": "စိတ်၏ ခက်ထန်မှု",
    "cetaso vinibandhā": "စိတ်ကို ချည်နှောင်ထားသော အရာ", "cetasovinibandhā": "စိတ်ကို ချည်နှောင်ထားသော အရာ",
    "nīvaraṇāni": tb("nīvaraṇaṃ"), "kammāni ānantarikāni": "ချက်ချင်း အကျိုးပေးသော ကံ", "verā": "ရန်",
    "byasanā": "ပျက်စီးခြင်း", "akkhantiyā ādīnavā": "မသည်းခံခြင်း၏ အပြစ်",
    "diṭṭhadhammanibbānavādā": "မျက်မှောက်ဘဝ၌ နိဗ္ဗာန်ဟု ဆိုသော ဝါဒ",
    "vivādamūlāni": "အငြင်းပွားမှု၏ အမြစ်", "chandarāgā": "လိုလားမှု ရာဂ", "virodhavatthūni": "ဆန့်ကျင်မှု၏ အကြောင်း",
    "taṇhākāyā": "တပ်မက်မှု အစု", "agāravā": "မရိုသေမှု", "parihāniyā dhammā": "ဆုတ်ယုတ်စေတတ်သော သဘောတရား",
    "somanassupavicārā": "ဝမ်းမြောက်ဖွယ်၌ စိတ် လှည့်လည်မှု", "domanassupavicārā": "စိတ်ဆင်းရဲဖွယ်၌ စိတ် လှည့်လည်မှု",
    "upekkhupavicārā": "လျစ်လျူရှုဖွယ်၌ စိတ် လှည့်လည်မှု",
    "gehasitāni somanassāni": "လောကီ အိမ်ရာကို မှီသော ဝမ်းမြောက်မှု",
    "gehasitāni domanassāni": "လောကီ အိမ်ရာကို မှီသော စိတ်ဆင်းရဲမှု",
    "gehasitā upekkhā": "လောကီ အိမ်ရာကို မှီသော ဥပေက္ခာ", "anusayā": tb("anusayo"),
    "pariyuṭṭhānāni": tb("pariyuṭṭhānaṃ"), "asaddhammā": "သူတော်ကောင်း မဟုတ်သူတို့၏ တရား", "mānā": tb("māna"),
    "kilesavatthūni": "ကိလေသာ အကြောင်းရင်း", "kusītavatthūni": "ပျင်းရိမှု၏ အကြောင်း",
    "micchattā": tb("micchattaṃ"), "purisadosā": "လူ၏ အပြစ်", "asaññīvādā": "မှတ်သိမှု မရှိသော အတ္တကို ဆိုသော ဝါဒ",
    "asaññivādā": "မှတ်သိမှု မရှိသော အတ္တကို ဆိုသော ဝါဒ",
    "nevasaññīnāsaññīvādā": "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သော အတ္တကို ဆိုသော ဝါဒ",
    "nevasaññināsaññivādā": "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သော အတ္တကို ဆိုသော ဝါဒ",
    "āghātavatthūni": "ရန်ငြိုးဖွဲ့ခြင်း၏ အကြောင်း", "purisamalāni": "လူ၏ အညစ်အကြေး", "navavidhā mānā": "ကိုးမျိုးသော မာန",
    "taṇhāmūlakā dhammā": "တပ်မက်မှုကို အမြစ်ပြုသော သဘောတရား", "iñjitāni": "တုန်လှုပ်မှု", "maññitāni": "ထင်မှတ်မှု",
    "phanditāni": "လှုပ်ရှားမှု", "papañcitāni": "ချဲ့ထွင်မှု", "saṅkhatāni": "ပြုပြင်ထားမှု",
    "akusalakammapathā": "အကုသိုလ် ကံ လမ်းကြောင်း", "taṇhāvicaritāni": "တပ်မက်မှု၏ ဖြစ်ပုံ",
    "diṭṭhigatāni": tb("diṭṭhigatānaṃ"), "lokadhammesu": "လောကဓံ",
})
NAME.update(new("Names (new)", {
    "dasavatthukā micchādiṭṭhi": f"အကြောင်းအရာ ဆယ်ပါး ရှိသော {tb('micchādiṭṭhi')}",
    "dasavatthukā antaggāhikā diṭṭhi": f"အကြောင်းအရာ ဆယ်ပါး ရှိသော အစွန်းကို စွဲကိုင်သော {_D}",
    "antaggāhikā diṭṭhi": f"အစွန်းကို စွဲကိုင်သော {_D}",
    "aṭṭhasu lokadhammesu cittassa paṭighāto": "လောကဓံ ရှစ်ပါးတို့၌ စိတ်၏ ထိခိုက်မှု",
    "aṭṭha taṇhāvicaritasataṃ": "တပ်မက်မှု၏ ဖြစ်ပုံ တစ်ရာ့ရှစ်ပါး", "ariyā": tb("ariyā"),
}))
LABEL = {"Ka": "က", "Kha": "ခ", "Ga": "ဂ", "Gha": "ဃ", "Ṅa": "င", "Ca": "စ", "Cha": "ဆ", "Ja": "ဇ",
         "ka": "က", "ga": "ဂ"}


def name(p):
    k = p[:1].lower() + p[1:]
    if k in NAME:
        return NAME[k]
    m = re.fullmatch(r"(?:(?P<a>aparāpi|aparepi|aparānipi) )?(?P<n>" + "|".join(NUM) + r") (?P<g>.+)", k)
    if m and m["g"] in GROUP:
        return ("နောက်ထပ် " if m["a"] else "") + f"{GROUP[m['g']]} {NUM[m['n']]}ပါး"
    for n in sorted(NUM, key=len, reverse=True):          # sandhi: sattānusayā, pañcorambhāgiyāni, pañcuddham…
        for stem in (n, n[:-1]):
            if k.startswith(stem) and len(k) > len(stem):
                g = k[len(stem):]
                for gg in (g, "a" + g[1:], "o" + g, "u" + g, "a" + g):
                    if gg in GROUP:
                        return f"{GROUP[gg]} {NUM[n]}ပါး"
    raise Miss("name: " + p)



NAME.update(new("Names (new)", {
    "kiñcanaṃ": GROUP["kiñcanā"], "aṅgaṇaṃ": GROUP["aṅgaṇāni"], "malaṃ": GROUP["malāni"],
    "visamaṃ": GROUP["visamāni"], "rūpataṇhā@sense": ITEMS["rūpataṇhā"],
}))
NAME["rāgo"] = ITEMS["rāgo"]

# ===================================================================================== prose tables
IDHEKACCO = p1("Idhekacco pāṇinā vā leḍḍunā", S2).split(" ", 3)
IDHEKACCO = " ".join(IDHEKACCO[:3])                       # ဤလောက၌ အချို့သော သူသည်
assert IDHEKACCO == "ဤလောက၌ အချို့သော သူသည်", IDHEKACCO
ANNATARA = "တစ်ခုခုသော အရာဖြင့်"                         # aññataraññatarena (pi-2 ch3)
assert ANNATARA in p1("Idhekacco pāṇinā vā leḍḍunā", S2)
DUKKHE = p1("Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ").removesuffix(END)
AVIJJA_TAIL = list_my("avijjālaṅgī moho akusalamūlaṃ")
OBJ = new("Objects of «ārabbha / paṭisaṃyutta / sahagata» (new unless pi-1)", {
    "kāma": "ကာမ", "byāpāda": tb("byāpādo"), "vihiṃsā": "ညှဉ်းပန်းမှု", "kāmadhātu": "ကာမဘုံ",
    "rūpadhātu": "သိမ်မွေ့သော ရုပ်ဘုံ", "arūpadhātu": "ရုပ်မရှိသော ဘုံ",
    "rūpadhātuarūpadhātu": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံ", "bhavadiṭṭhi": NAME["bhavadiṭṭhi"],
    "ucchedadiṭṭhi": NAME["ucchedadiṭṭhi"], "dukkarakāritā": "ပြုနိုင်ခဲသော အကျင့်ကို ကျင့်ခြင်း",
    "diṭṭhigata": tb("diṭṭhigata"), "ñātake": "ဆွေမျိုးတို့", "janapadaṃ": "ဇနပုဒ်",
    "lābhasakkārasilokaṃ": "လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှု", "pubbantaṃ": "အတိတ်ကာလ", "aparantaṃ": "အနာဂတ်ကာလ",
})
PATISAM = "နှင့် စပ်ယှဉ်သော "                               # -paṭisaṃyutta (pi-2 ch3)
assert PATISAM.strip() in p1("Byāpādapaṭisaṃyutto takko vitakko", S2)
SAHAGATA = "နှင့်အတူ ဖြစ်သော "
ARABBHA = "ကို အစွဲပြု၍ "
PATICCA = "ကို စွဲ၍"
VA = "ဖြစ်စေ"
BHAYA_OBJ = {"jātiṃ": "မွေးဖွားခြင်း", "jaraṃ": "အိုခြင်း", "maraṇaṃ": "သေခြင်း"}
LSS_GEN = "လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှုကို မှီသော၊ ယုတ်မာသော အလိုရှိသော၊ အလိုဆန္ဒ နှိပ်စက်ခံရသော သူ၏"
LSS_NOM = "လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှုကို မှီသော၊ ယုတ်မာသော အလိုရှိသော၊ အလိုဆန္ဒ နှိပ်စက်ခံရသော သူသည်"
add_items(new("List items (new)", {
    "gehasito takko": "လောကီ အိမ်ရာကို မှီသော တွေးတောခြင်း",
    "imassa vā pūtikāyassa bāhirānaṃ vā parikkhārānaṃ maṇḍanā":
        "ဤပုပ်စပ်သော ကိုယ်ကိုဖြစ်စေ၊ ပြင်ပ အသုံးအဆောင်တို့ကိုဖြစ်စေ အလှဆင်ခြင်း",
    "āmisassa eṭṭhi": "ပစ္စည်းကို ရှာခြင်း",
    "gehasito rāgo": "လောကီ အိမ်ရာကို မှီသော ရာဂ",
    "aṭṭhapanā": "ခိုင်ခိုင်မြဲမြဲ တည်ထားခြင်း",
}).items(), "new")
ITEMS["aṭhapanā"] = "ပြင်ဆင်ထားခြင်း"
ITEMS["ṭhapanā"] = "တည်ထားခြင်း"
ITEMS["saṇṭhapanā"] = "ကောင်းစွာ တည်ထားခြင်း"
NEW["List items (new)"].update({"aṭhapanā": ITEMS["aṭhapanā"], "ṭhapanā": ITEMS["ṭhapanā"],
                                "saṇṭhapanā": ITEMS["saṇṭhapanā"]})
for _k in list(ITEMS):
    if " " in _k:
        MULTI.add(_k)
ITEM_MAX = max(len(k.split()) for k in ITEMS)

# the bases of māna («jātiyā vā gottena vā … aññataraññatarena vatthunā»)
MB = [("jātiyā", "ဇာတိဖြင့်"), ("gottena", "အမျိုးအနွယ်ဖြင့်"), ("kolaputtiyena", "အမျိုးကောင်းသား ဖြစ်ခြင်းဖြင့်"),
      ("vaṇṇapokkharatāya", "အဆင်းလှခြင်းဖြင့်"), ("dhanena", "ဥစ္စာဖြင့်"), ("ajjhenena", "စာပေ သင်ယူမှုဖြင့်"),
      ("kammāyatanena", "အလုပ်အကိုင်ဖြင့်"), ("sippāyatanena", "အတတ်ပညာဖြင့်"), ("vijjāṭṭhānena", "ပညာရပ်ဖြင့်"),
      ("sutena", "အကြားအမြင်ဖြင့်"), ("paṭibhānena", "လျင်မြန်သော ဉာဏ်ဖြင့်")]
new("Māna bases (new)", dict(MB) | {"aññataraññatarena vatthunā": "တစ်ခုခုသော အကြောင်းဖြင့်"})
VATTHU = "တစ်ခုခုသော အကြောင်းဖြင့်"


def bases_my(t):
    """«jātiyā vā gottena vā …[…pe…] aññataraññatarena vatthunā» -> Burmese."""
    t = t.removesuffix(" aññataraññatarena vatthunā")
    out = []
    for part in re.split(r"(…pe…)", t):
        if part == "…pe…":
            out[-1] = out[-1].removesuffix(C) + PE
            continue
        for w in [x for x in part.strip().split(" vā") if x.strip()]:
            w = w.strip()
            mm = re.fullmatch(r"(?P<w>\S+)(?P<v> \[[^\]]+\])?", w)
            d = dict(MB)
            if not mm or mm["w"] not in d:
                raise Miss("māna base: " + w)
            out.append(d[mm["w"]] + (" " + var(mm["v"].strip()) if mm["v"] else "") + VA + C)
    return " ".join(out).replace(f"{VA}{C}{PE}", f"{VA}{PE}") + " " + VATTHU


BASES_RE = r"(?P<b>jātiyā vā gottena vā .+?aññataraññatarena vatthunā)"


# ===================================================================================== quoted views
VIEW = new("Quoted views and statements (new)", {
    "sassato loko": "လောကသည် မြဲ၏", "asassato loko": "လောကသည် မမြဲ", "antavā loko": "လောကသည် အဆုံး ရှိ၏",
    "anantavā loko": "လောကသည် အဆုံး မရှိ",
    "taṃ jīvaṃ taṃ sarīraṃ": "အသက်ကောင်သည်လည်း ထိုအရာပင်၊ ကိုယ်ခန္ဓာသည်လည်း ထိုအရာပင်",
    "aññaṃ jīvaṃ aññaṃ sarīraṃ": "အသက်ကောင်သည် တစ်ခြား၊ ကိုယ်ခန္ဓာသည် တစ်ခြား",
    "hoti tathāgato paraṃ maraṇā": "တထာဂတသည် သေပြီးနောက် ရှိ၏",
    "na hoti tathāgato paraṃ maraṇā": "တထာဂတသည် သေပြီးနောက် မရှိ",
    "hoti ca na ca hoti tathāgato paraṃ maraṇā": "တထာဂတသည် သေပြီးနောက် ရှိလည်း ရှိ၏၊ မရှိလည်း ဖြစ်၏",
    "neva hoti na na hoti tathāgato paraṃ maraṇā": "တထာဂတသည် သေပြီးနောက် ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်",
    "bhavissati attā ca loko ca": "အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း ဖြစ်လိမ့်မည်",
    "na bhavissati attā ca loko ca": "အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း ဖြစ်လိမ့်မည် မဟုတ်",
    "sassato attā ca loko ca": "အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း မြဲ၏",
    "ucchijjissati attā ca loko ca": "အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း ပြတ်စဲလိမ့်မည်",
    "antavā attā ca loko ca": "အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း အဆုံး ရှိ၏",
    "anantavā attā ca loko ca": "အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း အဆုံး မရှိ",
    "seyyohamasmi": "ငါသည် သာလွန်သူ ဖြစ်သည်", "sadisohamasmi": "ငါသည် တူညီသူ ဖြစ်သည်",
    "hīnohamasmi": "ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်",
    "anatthaṃ me acari": "ငါ့အား အကျိုးမဲ့ကို ပြုခဲ့ပြီ", "anatthaṃ me carati": "ငါ့အား အကျိုးမဲ့ကို ပြု၏",
    "anatthaṃ me carissati": "ငါ့အား အကျိုးမဲ့ကို ပြုလိမ့်မည်",
    "piyassa me manāpassa anatthaṃ acari": "ငါ ချစ်သော ငါ နှစ်သက်သူအား အကျိုးမဲ့ကို ပြုခဲ့ပြီ",
    "anatthaṃ carati": "အကျိုးမဲ့ကို ပြု၏", "anatthaṃ carissati": "အကျိုးမဲ့ကို ပြုလိမ့်မည်",
    "appiyassa me amanāpassa atthaṃ acari": "ငါ မချစ်သော ငါ မနှစ်သက်သူအား အကျိုးကို ပြုခဲ့ပြီ",
    "atthaṃ carati": "အကျိုးကို ပြု၏", "atthaṃ carissati": "အကျိုးကို ပြုလိမ့်မည်",
    "nicca": "မြဲ၏", "sukha": "ချမ်းသာ၏", "attā": "အတ္တ ဖြစ်၏", "subha": "တင့်တယ်၏",
    "mā maṃ jaññā": "ငါ့ကို မသိပါစေနှင့်",
    "sīlena suddhi vatena suddhi sīlabbatena suddhi": None,
    "sayaṅkataṃ sukhadukkhaṃ": "ချမ်းသာ ဆင်းရဲကို မိမိ ပြုသည်",
    "paraṅkataṃ sukhadukkhaṃ": "ချမ်းသာ ဆင်းရဲကို သူတစ်ပါး ပြုသည်",
    "sayaṅkatañca paraṅkatañca sukhadukkhaṃ": "ချမ်းသာ ဆင်းရဲကို မိမိလည်း ပြုသည်၊ သူတစ်ပါးလည်း ပြုသည်",
    "asayaṅkāraṃ aparaṅkāraṃ adhiccasamuppannaṃ sukhadukkhaṃ":
        "ချမ်းသာ ဆင်းရဲသည် မိမိ မပြု၊ သူတစ်ပါး မပြုဘဲ အကြောင်းမဲ့ ဖြစ်ပေါ်လာသည်",
    "atthi me attā": "ငါ၏ အတ္တ ရှိ၏", "natthi me attā": "ငါ၏ အတ္တ မရှိ",
    "attanā vā attānaṃ sañjānāmi": "အတ္တဖြင့် အတ္တကို ငါ သိ၏",
    "attanā vā anattānaṃ sañjānāmi": "အတ္တဖြင့် အတ္တ မဟုတ်သည်ကို ငါ သိ၏",
    "anattanā vā attānaṃ sañjānāmi": "အတ္တ မဟုတ်သည်ဖြင့် အတ္တကို ငါ သိ၏",
    "na sarāmi na sarāmi": "ငါ မမှတ်မိ၊ ငါ မမှတ်မိ",
    "nevāhaṃ āpannomhi, na panāhaṃ anāpannomhi": "ငါ အာပတ်သင့်သည်လည်း မဟုတ်၊ အာပတ် မသင့်သည်လည်း မဟုတ်",
    "asmi": "ငါ ရှိ၏", "ahamasmi": "ဤသည် ငါ ဖြစ်၏", "ayamahamasmi": "ဤအရာသည် ငါ ဖြစ်၏",
    "bhavissaṃ": "ငါ ဖြစ်လိမ့်မည်", "rūpī bhavissaṃ": "ငါ ရုပ် ရှိသူ ဖြစ်လိမ့်မည်",
    "arūpī bhavissaṃ": "ငါ ရုပ် မရှိသူ ဖြစ်လိမ့်မည်", "saññī bhavissaṃ": "ငါ မှတ်သိမှု ရှိသူ ဖြစ်လိမ့်မည်",
    "asaññī bhavissaṃ": "ငါ မှတ်သိမှု မရှိသူ ဖြစ်လိမ့်မည်",
    "nevasaññīnāsaññī bhavissaṃ": "ငါ မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ ဖြစ်လိမ့်မည်",
})
VIEW.pop("sīlena suddhi vatena suddhi sīlabbatena suddhi")
_SB = p1("Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi vatena suddhi")
SILABBATA = _SB.split("ဟူ၍")[0]                            # ဤသာသနာ အပြင်ဘက်ရှိ … ရှိသည်
VIEW["ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi vatena suddhi sīlabbatena suddhi"] = SILABBATA


def quote_key(q):
    q = q[:1].lower() + q[1:]
    q = re.sub(r"(?<=[ṃ])$", "", q)
    return q


def view(q):
    k = quote_key(q)
    for c in (k, k[:-1] + "ṃ" if k.endswith("n") else k, k.removesuffix("ī") + "i", k.removesuffix("ū") + "u",
              k.removesuffix("ā") + "a"):
        if c in VIEW:
            return VIEW[c]
    raise Miss("view: " + q)


QTI = re.compile(r'"(?P<q>[^"]+?)"(?P<t>nti|ti)')


def quotes_my(t):
    """«"X"ti» -> «“X”ဟု»; «"X"nti» -> X+ṃ."""
    def rep(m):
        q = m["q"] + ("ṃ" if m["t"] == "nti" else "")
        return "“" + view(q) + "”ဟု"
    return QTI.sub(rep, t)


# ===================================================================================== content (clause) engine
PH = {}            # Pāli clause -> Burmese (exact)
PREFIX = {}        # Pāli clause prefix (before a list) -> Burmese


def ph(sec, d):
    PH.update(new(sec, d))


def prefix(sec, d):
    PREFIX.update(new(sec, d))


def relist(c):
    """«Yo / Yā / Yaṃ [evarūpo] [tattha | tesaṃ | paresaṃ | imesaṃ …] LIST»."""
    m = re.fullmatch(r"(?:Yo|Yā|Yaṃ|yo|yā|yaṃ) (?P<e>evarūp(?:o|ā|aṃ) )?(?P<x>(?:tattha|tesaṃ|paresaṃ|imassa "
                     r"saddhammassa|imassa kummaggassa|imesaṃ ariyānaṃ|cittassa|kāyassa|bhuttāvissa|sā|kāmesu|bhavesu) )?(?P<l>.+)", c)
    if not m:
        return None
    x = (m["x"] or "").strip()
    head = {"": "", "tattha": "ထို၌ ရှိသော ", "tesaṃ": PM_TESAM, "paresaṃ": "သူတစ်ပါးတို့အပေါ် ",
            "imassa saddhammassa": "ဤသူတော်ကောင်းတရားကို ", "imassa kummaggassa": "ဤလမ်းမှားကို ",
            "imesaṃ ariyānaṃ": "ဤအရိယာတို့ကို ", "kāmesu": "ကာမတို့၌ ရှိသော ", "bhavesu": "ဘဝတို့၌ ရှိသော "}.get(x)
    l = m["l"]
    if x in ("cittassa", "kāyassa", "bhuttāvissa"):
        head, l = "", x + " " + l
    if head is None:
        return None
    if not is_list(l):
        return None
    return (EV if m["e"] else "") + head + list_my(l) + " ရှိသမျှ"


def ident(c):
    """«A B» (two names) -> «Aသည် B ဖြစ်သည်»."""
    w = c.split(" ")
    for i in range(1, len(w)):
        a, b = " ".join(w[:i]), " ".join(w[i:])
        try:
            return f"{name(a)}သည် {name(b)} {F.COP[False]}"
        except Miss:
            continue
    return None


def content(c):
    c = c.strip()
    for k in (c, c[:1].lower() + c[1:]):
        if k in PH:
            return PH[k]
    if c + "." in S1 and S1[c + "."].endswith(END):        # a pi-1 sentence used as a clause (before « – »)
        REUSE.setdefault("p1_clause", []).append(c)
        return S1[c + "."].removesuffix(END)
    for cc in dict.fromkeys((c, c[:1].lower() + c[1:])):
        for rgx, f in REGEX:
            m = rgx.fullmatch(cc)
            if m:
                try:
                    return f(m)
                except Miss:
                    pass
    if " – " in c:
        return " – ".join(content(x) for x in c.split(" – "))
    r = relist(c)
    if r:
        return r
    if is_list(c):
        return list_my(c)
    for k in sorted(PREFIX, key=len, reverse=True):
        if c.startswith(k + " "):
            return PREFIX[k] + " " + content(c[len(k) + 1:])
    for k in sorted((k for k in PH if ", " in k), key=len, reverse=True):
        if c.startswith(k + ", "):
            return PH[k] + C + " " + content(c[len(k) + 2:])
    m = re.fullmatch(r"(?P<x>\S+)(?P<k>paṭisaṃyutt[oā]|sahagato) (?P<l>.+)", c)
    if m and m["x"][:1].lower() + m["x"][1:] in OBJ and is_list(m["l"]):
        o = OBJ[m["x"][:1].lower() + m["x"][1:]]
        return o + (PATISAM if m["k"].startswith("p") else SAHAGATA) + list_my(m["l"])
    m = re.fullmatch(r"(?P<x>\S+) ārabbha (?P<l>.+)", c)
    if m and m["x"][:1].lower() + m["x"][1:] in OBJ and is_list(m["l"]):
        return OBJ[m["x"][:1].lower() + m["x"][1:]] + ARABBHA + list_my(m["l"])
    m = re.fullmatch(r"(?P<x>\S+) paṭicca (?P<l>.+)", c)
    if m:
        x = m["x"][:1].lower() + m["x"][1:]
        if m["l"].startswith("bhayaṃ") and x in BHAYA_OBJ:
            return BHAYA_OBJ[x] + PATICCA + " " + list_my(m["l"])
        if x in MADA_ACC and is_list(m["l"]):
            return MADA_BASE[MADA_ACC[x]] + PATICCA + " " + list_my(m["l"])
    if re.fullmatch(r"(?:\S+ paṭicca…pe… )+\S+ paṭicca .+", c):
        parts = c.split("…pe… ")
        out = []
        for p in parts[:-1]:
            x = p.removesuffix(" paṭicca")
            x = x[:1].lower() + x[1:]
            out.append(MADA_BASE[MADA_ACC[x]] + PATICCA + PE)
        return " ".join(out) + " " + content(parts[-1])
    if ", " in c or re.search(r" vā yathā so ", c):
        if re.search(r" vā yathā so ", c):
            SLIPS.append("taṇhāvicarita: comma missing in «… vā yathā so …» («၊» supplied between the items)")
        parts = re.split(r", (?![^\[]*\])|(?<= vā) (?=yathā so )", c)
        try:
            return f"{C} ".join(content(p) for p in parts)
        except Miss:
            pass
    if "; " in c:
        return f"{C} ".join(content(p) for p in c.split("; "))
    if "…pe… " in c:
        try:
            parts = c.split("…pe… ")
            out = [content(p) for p in parts]
            return (PE + " ").join(x.removesuffix(PE) for x in out[:-1]) + PE + " " + out[-1]
        except Miss:
            pass
    m = re.fullmatch(r'(?P<a>.+?metaṃ) (?P<b>".+)', c)          # ^2-964: comma missing between two clauses
    if m:
        SLIPS.append("^2-964: comma missing before «" + m["b"][:20] + "» (no «၊» added)")
        return content(m["a"]) + " " + content(m["b"])
    try:
        return name(c)
    except Miss:
        pass
    r = ident(c)
    if r:
        return r
    if '"' in c:
        q = quotes_my(c)
        if q != c and '"' not in q:
            rest = q
            return rest
    raise Miss("clause: " + c[:120])


# ===================================================================================== sentence engine
SENT = {}


def sent(sec, d):
    SENT.update(new(sec, d))


Q_RE = re.compile(r"[Tt]attha katam(?P<k>o|ā|aṃ|e|āni|esu) (?P<x>.+?)(?P<v> \[[^\]]+\])?\?")
VUCC_RE = re.compile(r'(?P<c>.+) – (?:ayaṃ|idaṃ) vuccati (?P<x>"[^"]+"|[^"]+?)(?P<slip>\."|)\.?')
GRP_RE = re.compile(r"(?P<c>.+) – (?:ime|imāni|imā|imesu) (?P<x>.+)\.")
GRP_ONLY = re.compile(r"(?:Ime|Imāni|Imā) (?P<x>.+)\.")
ASK = "ထိုတို့အနက် {} ဟူသည် အဘယ်{}နည်း"


def vname(x):
    if x.startswith('"'):
        x = x.strip('"')
        if x.endswith("."):
            SLIPS.append(f"full stop inside the closing quote: «\"{x}\"» (rendered «“…”ဟု ခေါ်သည်။»)")
            x = x[:-1]
        return "“" + name(x) + "”"
    return name(x)


def frame(b):
    m = Q_RE.fullmatch(b)
    if m:
        x = m["x"]
        if x.startswith("aṭṭhasu lokadhammesu"):
            nm = NAME["aṭṭhasu lokadhammesu cittassa paṭighāto"]
        else:
            nm = name(x)
        pl = m["k"] in ("e", "āni") or any(x.split(" ")[i] in NUM for i in range(min(2, len(x.split()))))
        return ASK.format(nm + (" " + var(m["v"].strip()) if m["v"] else ""), "တို့" if pl else "") + END
    m = VUCC_RE.fullmatch(b)
    if m:
        if m["slip"]:
            SLIPS.append(f"closing quote after the full stop: «{m['x']}{m['slip']}» (rendered «…”ဟု ခေါ်သည်။»)")
        return content(m["c"]) + " – ဤသည်ကို " + vname(m["x"] + ('"' if m["slip"] else "")) + "ဟု ခေါ်သည်" + END
    m = re.fullmatch(r"(?P<c>.+) – ayaṃ (?P<x>[^–]+)\.", b)
    if m:
        return content(m["c"]) + " – ဤသည်မှာ " + name(m["x"]) + " " + F.COP[False] + END
    m = GRP_RE.fullmatch(b)
    if m:
        return content(m["c"]) + " – ဤသည်တို့မှာ " + name(m["x"]) + " ဖြစ်ကြသည်" + END
    m = GRP_ONLY.fullmatch(b)
    if m:
        return "ဤသည်တို့မှာ " + name(m["x"]) + " ဖြစ်ကြသည်" + END
    m = re.fullmatch(r"(?P<a>.+) – (?P<b>[^–]+)\.", b)
    if m:
        try:
            return content(m["a"]) + " – " + name(m["b"]) + " " + F.COP[False] + END
        except Miss:
            pass
    m = re.fullmatch(r"(?:Sabbampi|Sabbāpi) (?P<a>.+) (?P<b>\S+)\.", b)
    if m:
        return f"{name(m['a'])} အားလုံးသည် {name(m['b'])} {F.COP[False]}{END}"
    m = re.fullmatch(r"Ayaṃ vuccati (?P<x>.+)\.", b)
    if m:
        return "ဤသည်ကို " + vname(m["x"]) + "ဟု ခေါ်သည်" + END
    if b.endswith("."):
        return content(b[:-1]) + END
    if b.endswith("?"):
        return content(b) + END
    raise Miss("sentence: " + b[:120])


def label(l):
    """«Ka» -> «က», «24. Ka» -> «24. က», «Ka-ga» -> «က-ဂ», digits kept."""
    def one(x):
        if re.fullmatch(r"\d+(?:-\d+)?", x) or x.strip() == "":
            return x
        if x in LABEL:
            return LABEL[x]
        m = re.fullmatch(r"(?P<n>\d+)\. (?P<l>\S+)", x)
        if m and m["l"] in LABEL:
            return f"{m['n']}. {LABEL[m['l']]}"
        m = re.fullmatch(r"(?P<a>\S+)-(?P<b>\S+)", x)
        if m and m["a"] in LABEL and m["b"] in LABEL:
            return f"{LABEL[m['a']]}-{LABEL[m['b']]}"
        raise Miss("label: " + x)
    return one(l)


def tr_sent(s):
    lab = ""
    m = re.match(r"\((?P<l>[^)]*)\)(?P<sp> ?)", s)
    if m and not s.startswith("( )") or (m and s.startswith("( )")):
        lab = f"({label(m['l'])}){m['sp']}"
        s = s[m.end():]
    ed = ""
    m = re.match(r"\[\((?P<q>tattha katamā [^)]+)\)(?P<x> \(\?\))?\] ", s)
    if m:                                           # editorial question in brackets (^2-916)
        q = Q_RE.fullmatch(m["q"][:1].upper() + m["q"][1:] + "?")
        ed = "[(" + ASK.format(name(q["x"]), "") + ")" + (" (အမည်မသိ မူ)" if m["x"] else "") + "] "
        s = s[m.end():]
    k = s[:1].upper() + s[1:]
    k = k.replace("upādinn", "upādiṇṇ")
    if k in S1 and k[:1] == s[:1].upper():
        REUSE["p1"] += 1
        REUSE.setdefault("p1_list", []).append(k)
        return lab + ed + S1[k]
    if k in S2:
        REUSE["p2"] += 1
        return lab + ed + S2[k]
    if s in SENT:
        return lab + ed + SENT[s]
    return lab + ed + frame(s)


def tr_body(body):
    out = []
    for s in psplit(body):
        out.append(tr_sent(s))
    return " ".join(out)


# ===================================================================================== prose (clauses and sentences)
_PAMADA_HEAD = (f"ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်၌{VA}{C} နှုတ်ဖြင့် ပြုသော ဒုစရိုက်၌{VA}{C} မနောဖြင့် ပြုသော ဒုစရိုက်၌{VA}{C} "
                f"ကာမဂုဏ် ငါးပါးတို့၌{VA} စိတ်ကို လွှတ်ထားခြင်း၊ လွှတ်ထားခြင်းကို ထပ်ကာထပ်ကာ ပြုခြင်း")
for _va in ("vā ", ""):
    for _c1, _c2 in (("", ""), (",", ",")):
        prefix("Pamāda / kosajja head", {
            f"Kāyaduccarite vā vacīduccarite vā manoduccarite vā pañcasu vā kāmaguṇesu cittassa vossaggo{_c1} "
            f"vossaggānuppadānaṃ kusalānaṃ {_va}dhammānaṃ{_c2} bhāvanāya":
                _PAMADA_HEAD + f"{C if _c1 else ''} ကုသိုလ် သဘောတရားတို့ကို{VA if _va else ''} ပွားများရာ၌"
                + (C if _c2 else "")})
_REQ = "သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်"
for _g in ("gilānappaccaya", "gilānapaccaya"):
    ph("Atricchatā / mahicchatā / asantuṭṭhitā", {
        f"Itarītaracīvarapiṇḍapātasenāsana{_g}bhesajjaparikkhārehi pañcahi vā kāmaguṇehi asantuṭṭhassa "
        "bhiyyokamyatā": f"ရရှိသမျှ {_REQ}တို့ဖြင့်ဖြစ်စေ၊ ကာမဂုဏ် ငါးပါးတို့ဖြင့်{VA} ရောင့်ရဲမှု မရှိသူ၏ "
                         "ပို၍ လိုချင်ခြင်း"})
_PAPI = [("assaddho", "ယုံကြည်မှု မရှိသူ", "saddho", "ယုံကြည်မှု ရှိသူ"), ("dussīlo", "သီလ ပျက်သူ", "sīlavā", "သီလ ရှိသူ"),
         ("appassuto", "အကြားအမြင် နည်းသူ", "bahussuto", "အကြားအမြင် များသူ"),
         ("saṅgaṇikārāmo", "အပေါင်းအသင်းကို နှစ်သက်သူ", "pavivitto", "ကင်းဆိတ်စွာ နေသူ"),
         ("kusīto", "ပျင်းရိသူ", "āraddhavīriyo", "ဝီရိယ အားထုတ်ထားသူ"),
         ("muṭṭhassatī", "သတိ လစ်သူ", "upaṭṭhitassatī", "သတိ တည်ထားသူ"),
         ("asamāhito", "စိတ် မတည်ကြည်သူ", "samāhito", "စိတ် တည်ကြည်သူ"), ("duppañño", "ပညာ နည်းသူ", "paññavā", "ပညာ ရှိသူ"),
         ("akhīṇāsavo", "စိတ်အစွန်းအထင်း မကုန်သေးသူ", "khīṇāsavo", "စိတ်အစွန်းအထင်း ကုန်ပြီးသူ")]
ph("Pāpicchatā", {"Idhekacco " + ", ".join(f'{a} samāno "{b}ti maṃ jano jānātū"ti icchati' for a, _, b, _ in _PAPI):
                  IDHEKACCO + " " + f"{C} ".join(f"{am} ဖြစ်လျက် “ငါ့ကို {bm}ဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏"
                                                 for _, am, _, bm in _PAPI)})
prefix("Prefixes before a list", {
    "Cīvaramaṇḍanā pattamaṇḍanā senāsanamaṇḍanā": None,
    "Mātari vā pitari vā jeṭṭhe vā bhātari vā ācariyesu vā upajjhāye vā buddhe vā sāvakesu vā aññataraññataresu "
    "garuṭṭhāniyesu": f"အမိ၌{VA}၊ အဖ၌{VA}၊ အကြီးအကဲ၌{VA}၊ ညီအစ်ကို၌{VA}၊ ဆရာတို့၌{VA}၊ ဥပဇ္ဈာယ်ဆရာ၌{VA}၊ "
                      f"ဘုရား၌{VA}၊ တပည့်သာဝကတို့၌{VA}၊ အလေးပြုထိုက်သော တစ်ဦးဦးတို့၌",
    "Pantesu vā senāsanesu aññataraññataresu vā adhikusalesu dhammesu":
        f"ဆိတ်ငြိမ်ရာ ကျောင်းအိပ်ရာနေရာတို့၌{VA}၊ မြင့်မြတ်သော ကုသိုလ် သဘောတရား တစ်ခုခုတို့၌{VA}",
    "Lābhasakkārasilokasannissitassa pāpicchassa icchāpakatassa paccayapaṭisevanasaṅkhātena "
    "[paccayapaṭisedhanasaṅkhātena (sī.)] vā sāmantajappitena vā iriyāpathassa vā":
        f"{LSS_GEN} ပစ္စည်းကို ငြင်းပယ်ဟန် ပြုခြင်းဟူသော နည်းဖြင့် {var('[paccayapaṭisedhanasaṅkhātena (sī.)]')}"
        f"{VA}၊ အနီးအနား စကား ပြောခြင်းဖြင့်{VA}၊ ကိုယ်ဟန် အမူအရာကို{VA}",
    "Lābhasakkārasilokasannissitassa pāpicchassa icchāpakatassa": LSS_GEN,
    "Sahadhammike vuccamāne": "တရားနှင့် လျော်စွာ သွန်သင် ပြောဆိုသောအခါ",
    "Yā paralābhasakkāragarukāramānanavandanapūjanāsu": ISSA_HEAD.rstrip(),
})
PREFIX.pop("Cīvaramaṇḍanā pattamaṇḍanā senāsanamaṇḍanā")
NEW["Prefixes before a list"].pop("Cīvaramaṇḍanā pattamaṇḍanā senāsanamaṇḍanā")
ph("Clauses", {
    "Lābhasakkārasilokasannissito pāpiccho icchāpakato ito laddhaṃ āmisaṃ amutra harati amutra vā laddhaṃ āmisaṃ "
    "idha āharati": f"{LSS_NOM} ဤနေရာမှ ရသော ပစ္စည်းကို ထိုနေရာသို့ ဆောင်၏၊ သို့မဟုတ် ထိုနေရာမှ ရသော ပစ္စည်းကို "
                    "ဤနေရာသို့ ဆောင်၏",
    "Ye te puggalā assaddhā dussīlā appassutā maccharino duppaññā": PM_PERSONS,
    "Appatte pattasaññitā": "မရောက်သေးသည်၌ ရောက်ပြီဟု မှတ်ထင်ခြင်း",
    "akate katasaññitā": "မပြုရသေးသည်၌ ပြုပြီးပြီဟု မှတ်ထင်ခြင်း",
    "anadhigate adhigatasaññitā": "မရရှိသေးသည်၌ ရရှိပြီဟု မှတ်ထင်ခြင်း",
    "asacchikate sacchikatasaññitā": "မျက်မှောက် မပြုရသေးသည်၌ မျက်မှောက်ပြုပြီးပြီဟု မှတ်ထင်ခြင်း",
    "Rūpaṃ asmīti māno": f"ရုပ်၌ ငါ ရှိ၏ဟူသော {tb('māna')}", "asmīti māno": f"ငါ ရှိ၏ဟူသော {tb('māna')}",
    "asmīti chando": "ငါ ရှိ၏ဟူသော ဆန္ဒ", "asmīti anusayo": f"ငါ ရှိ၏ဟူသော {tb('anusayo')}",
    "vedanā…pe… saññā…pe… saṅkhārā…pe… viññāṇaṃ asmīti māno":
        f"ခံစားမှု… မှတ်သိမှု… ပြုပြင်ဖန်တီးမှုများ… သိစိတ်၌ ငါ ရှိ၏ဟူသော {tb('māna')}",
    "Dukkarakāritāpaṭisaṃyutto vā diṭṭhigatapaṭisaṃyutto vā gehasito takko vitakko micchāsaṅkappo":
        f"{OBJ['dukkarakāritā']}{PATISAM.rstrip()}{VA}၊ {OBJ['diṭṭhigata']}{PATISAM.rstrip()}{VA} "
        + list_my("gehasito takko vitakko micchāsaṅkappo"),
    '"Anatthaṃ me acarī"ti āghāto jāyati': f"“{VIEW['anatthaṃ me acari']}”ဟု {tb('āghāto jāyati')}",
    '"anatthaṃ me caratī"ti āghāto jāyati': f"“{VIEW['anatthaṃ me carati']}”ဟု {tb('āghāto jāyati')}",
    '"anatthaṃ me carissatī"ti āghāto jāyati': f"“{VIEW['anatthaṃ me carissati']}”ဟု {tb('āghāto jāyati')}",
    '"piyassa me manāpassa anatthaṃ acari"…pe… anatthaṃ carati…pe… "anatthaṃ carissatī"ti āghāto jāyati':
        f"“{VIEW['piyassa me manāpassa anatthaṃ acari']}”… {VIEW['anatthaṃ carati']}… “{VIEW['anatthaṃ carissati']}”ဟု "
        f"{tb('āghāto jāyati')}",
    '"piyassa me manāpassa anatthaṃ acari"…pe… anatthaṃ carati…pe… anatthaṃ carissatīti āghāto jāyati':
        f"“{VIEW['piyassa me manāpassa anatthaṃ acari']}”… {VIEW['anatthaṃ carati']}… {VIEW['anatthaṃ carissati']}ဟု "
        f"{tb('āghāto jāyati')}",
    '"appiyassa me amanāpassa atthaṃ acari"…pe… atthaṃ carati…pe… "atthaṃ carissatī"ti āghāto jāyati':
        f"“{VIEW['appiyassa me amanāpassa atthaṃ acari']}”… {VIEW['atthaṃ carati']}… “{VIEW['atthaṃ carissati']}”ဟု "
        f"{tb('āghāto jāyati')}",
    'appiyassa me amanāpassa atthaṃ acari…pe… atthaṃ carati…pe… atthaṃ carissatīti āghāto jāyati':
        f"{VIEW['appiyassa me amanāpassa atthaṃ acari']}… {VIEW['atthaṃ carati']}… {VIEW['atthaṃ carissati']}ဟု "
        f"{tb('āghāto jāyati')}",
    "aṭṭhāne vā pana āghāto jāyati": f"{F.VA_OR} အကြောင်း မရှိဘဲ {tb('āghāto jāyati')}",
    "Dukkhe aññāṇaṃ…pe… avijjālaṅgī moho akusalamūlaṃ": DUKKHE.split(C + " ")[0] + PE + " " + AVIJJA_TAIL,
    "Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ, dukkhanirodhe aññāṇaṃ, dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ, "
    "pubbante aññāṇaṃ, aparante aññāṇaṃ, pubbantāparante aññāṇaṃ, idappaccayatā paṭiccasamuppannesu dhammesu "
    "aññāṇaṃ": DUKKHE,
    "Pubbantaṃ ārabbha yā uppajjati diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho":
        f"{OBJ['pubbantaṃ']}{ARABBHA}ဖြစ်ပေါ်လာသော " + list_my("diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho") + " ရှိသမျှ",
    "Aparantaṃ ārabbha yā uppajjati diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho":
        f"{OBJ['aparantaṃ']}{ARABBHA}ဖြစ်ပေါ်လာသော " + list_my("diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho") + " ရှိသမျှ",
    "Yaṃ na hirīyati hiriyitabbena, na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        p1("Yaṃ na hirīyati hiriyitabbena").split(" – ")[0],
    "Yaṃ na hirīyati hirīyitabbena, na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        p1("Yaṃ na hirīyati hiriyitabbena").split(" – ")[0],
    "Yaṃ na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        p1("Yaṃ na ottappati").split(" – ")[0],
    "Yaṃ na ottappati ottappitabbena, na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        p1("Yaṃ na ottappati").split(" – ")[0],
    "Idhekacco appaṭisanthārako hoti āmisapaṭisanthārena vā dhammapaṭisanthārena vā":
        f"{IDHEKACCO} ပစ္စည်းဖြင့် ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်းဖြင့်{VA}၊ တရားဖြင့် ဖော်ဖော်ရွေရွေ "
        f"ကြိုဆိုဆက်ဆံခြင်းဖြင့်{VA} ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း မရှိသူ ဖြစ်၏",
    "Kāyiko vītikkamo vācasiko vītikkamo kāyikavācasiko vītikkamo":
        list_my("kāyiko vītikkamo vācasiko vītikkamo kāyikavācasiko vītikkamo"),
    "Kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo":
        list_my("kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo"),
    "Idhekacco pāṇinā vā leḍḍunā vā daṇḍena vā satthena vā rajjuyā vā aññataraññatarena satte viheṭheti": VH_HEAD,
    "Kāyena adhammacariyāvisamacariyā": "ကိုယ်ဖြင့် တရားနှင့် မညီသော အကျင့်၊ ဖောက်ပြန်သော အကျင့်",
    "vācāya adhammacariyāvisamacariyā": "နှုတ်ဖြင့် တရားနှင့် မညီသော အကျင့်၊ ဖောက်ပြန်သော အကျင့်",
    "manasā adhammacariyāvisamacariyā": "မနောဖြင့် တရားနှင့် မညီသော အကျင့်၊ ဖောက်ပြန်သော အကျင့်",
    "Kāmasaññā, byāpādasaññā, vihiṃsāsaññā": f"{C} ".join(NAME[x] for x in ("kāmasaññā", "byāpādasaññā", "vihiṃsāsaññā")),
    "Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhavantattaṃ cittassa":
        list_my("cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa") + " ရှိသမျှ",
    "Idhekacco assaddho hoti, na saddahati buddhaṃ vā dhammaṃ vā saṅghaṃ vā":
        f"{IDHEKACCO} ယုံကြည်မှု မရှိသူ ဖြစ်၏၊ ဘုရားကို{VA}၊ တရားကို{VA}၊ သံဃာကို{VA} မယုံကြည်",
    "Anicce \"nicca\"nti ayoniso manasikāro": f"မမြဲသည်၌ “{VIEW['nicca']}”ဟု {NAME['ayoniso manasikāro']}",
    "dukkhe \"sukha\"nti ayoniso manasikāro": f"ဆင်းရဲသည်၌ “{VIEW['sukha']}”ဟု {NAME['ayoniso manasikāro']}",
    "anattani \"attā\"ti ayoniso manasikāro": f"အတ္တ မဟုတ်သည်၌ “{VIEW['attā']}”ဟု {NAME['ayoniso manasikāro']}",
    "asubhe \"subha\"nti ayoniso manasikāro": f"မတင့်တယ်သည်၌ “{VIEW['subha']}”ဟု {NAME['ayoniso manasikāro']}",
    "saccavippaṭikulena vā cittassa āvaṭṭanā anāvaṭṭanā ābhogo samannāhāro manasikāro":
        f"{F.VA_OR} သစ္စာနှင့် ဆန့်ကျင်သော နည်းဖြင့် စိတ်၏ " + list_my("āvaṭṭanā anāvaṭṭanā ābhogo samannāhāro manasikāro"),
    "Micchādiṭṭhi, micchāsaṅkappo, micchāvācā, micchākammanto, micchāājīvo, micchāvāyāmo, micchāsati, micchāsamādhi":
        f"{C} ".join(NAME[x] for x in "micchādiṭṭhi micchāsaṅkappo micchāvācā micchākammanto micchāājīvo "
                     "micchāvāyāmo micchāsati micchāsamādhi".split()),
    "Yā imassa saddhammassa asotukamyatā asavanakamyatā anuggahetukamyatā adhāretukamyatā":
        "ဤသူတော်ကောင်းတရားကို " + list_my("asotukamyatā asavanakamyatā anuggahetukamyatā adhāretukamyatā") + " ရှိသမျှ",
    "Yā imassa kummaggassa sevanā nisevanā saṃsevanā bhajanā sambhajanā bhatti sambhatti taṃsampavaṅkatā":
        "ဤလမ်းမှားကို " + list_my("sevanā nisevanā saṃsevanā bhajanā sambhajanā bhatti sambhatti taṃsampavaṅkatā")
        + " ရှိသမျှ",
    "Yā imesaṃ ariyānaṃ adassanakamyatā adaṭṭhukamyatā asametukamyatā asamāgantukamyatā":
        "ဤအရိယာတို့ကို " + list_my("adassanakamyatā adaṭṭhukamyatā asametukamyatā asamāgantukamyatā") + " ရှိသမျှ",
    "Cattāro satipaṭṭhānā, cattāro sammappadhānā, cattāro iddhipādā, pañcindriyāni, pañca balāni, satta bojjhaṅgā, "
    "ariyo aṭṭhaṅgiko maggo": "သတိပဋ္ဌာန် လေးပါး၊ မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း လေးပါး၊ ဣဒ္ဓိပါဒ် လေးပါး၊ "
                              "စွမ်းရည် ငါးပါး၊ စွမ်းအား ငါးပါး၊ ဗောဇ္ဈင် ခုနစ်ပါး၊ အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်",
    "Chandarāgā gehasitā dhammā": None,
    "Manāpiyesu rūpesu gehasito rāgo sārāgo cittassa sārāgo": None,
})
PH.pop("Chandarāgā gehasitā dhammā"), PH.pop("Manāpiyesu rūpesu gehasito rāgo sārāgo cittassa sārāgo")


# ---- regex clauses (tried first in content)
REGEX = []


def rx(pattern):
    def deco(f):
        REGEX.append((re.compile(pattern), f))
        return f
    return deco


MANA_OBJ = {"mānaṃ": tb("māna"), "omānaṃ": ITEMS["omāno"]}
CMP = {"seyyaṃ": "သူတစ်ပါးတို့ထက် သာလွန်သူဟု", "sadisaṃ": "သူတစ်ပါးတို့နှင့် တူညီသူဟု",
       "hīnaṃ": "သူတစ်ပါးတို့ထက် ယုတ်ညံ့သူဟု"}
new("Māna sentences (new)", {"X mānaṃ jappeti": "Xကို ဖြစ်ပေါ်စေ၏", "parehi seyyaṃ attānaṃ dahati":
    "မိမိကိုယ်ကို " + CMP["seyyaṃ"] + " ထား၏", "so taṃ nissāya": "ထိုသူသည် ထိုအကြောင်းကို မှီ၍",
    "pubbakālaṃ / aparakālaṃ": "အစောပိုင်း အချိန်၌ / နောက်ပိုင်း အချိန်၌",
    "parehi attānaṃ atimaññati": "မိမိကိုယ်ကို သူတစ်ပါးတို့ထက် အလွန် မြင့်မြတ်သည်ဟု ထင်မှတ်၏"})


@rx(r"Idhekacco " + BASES_RE + r" (?P<o>mānaṃ|omānaṃ) jappeti")
def _r1(m):
    return f"{IDHEKACCO} {bases_my(m['b'])} {MANA_OBJ[m['o']]}ကို ဖြစ်ပေါ်စေ၏"


@rx(r"Idhekacco (?P<s>seyyo|sadiso|hīno) hoti " + BASES_RE + r" parehi (?P<c>seyyaṃ|sadisaṃ|hīnaṃ) attānaṃ dahati; "
    r"so taṃ nissāya (?P<o>mānaṃ|omānaṃ) jappeti")
def _r2(m):
    return (f"{IDHEKACCO} {bases_my(m['b'])} {MANA_SELF[m['s']]} ဖြစ်၏{C} မိမိကိုယ်ကို {CMP[m['c']]} ထား၏{C} "
            f"ထိုသူသည် ထိုအကြောင်းကို မှီ၍ {MANA_OBJ[m['o']]}ကို ဖြစ်ပေါ်စေ၏")


@rx(r"Idhekacco " + BASES_RE + r" parehi attānaṃ atimaññati")
def _r3(m):
    return f"{IDHEKACCO} {bases_my(m['b'])} မိမိကိုယ်ကို သူတစ်ပါးတို့ထက် အလွန် မြင့်မြတ်သည်ဟု ထင်မှတ်၏"


@rx(r"Idhekacco " + BASES_RE + r" pubbakālaṃ parehi sadisaṃ attānaṃ dahati, aparakālaṃ attānaṃ seyyaṃ dahati")
def _r4(m):
    return (f"{IDHEKACCO} {bases_my(m['b'])} အစောပိုင်း အချိန်၌ မိမိကိုယ်ကို {CMP['sadisaṃ']} ထား၏{C} "
            f"နောက်ပိုင်း အချိန်၌ မိမိကိုယ်ကို သာလွန်သူဟု ထား၏")


@rx(r"Idhekacco " + BASES_RE + r" mā maṃ pare avajāniṃsūti")
def _r5(m):
    return f"{IDHEKACCO} {bases_my(m['b'])} သူတစ်ပါးတို့ ငါ့ကို အထင်မသေးကြပါစေနှင့်ဟု ကြံစည်၏"


_PAPAKA = [("kammāyatanena", "အလုပ်အကိုင်ဖြင့်"), ("sippāyatanena", "အတတ်ပညာဖြင့်"), ("vijjāṭṭhānena", "ပညာရပ်ဖြင့်"),
           ("sutena", "အကြားအမြင်ဖြင့်"), ("paṭibhānena", "လျင်မြန်သော ဉာဏ်ဖြင့်"), ("sīlena", "သီလဖြင့်"),
           ("vatena", "အကျင့်ဝတ်ဖြင့်"), ("sīlabbatena", "သီလ အကျင့်ဝတ်ဖြင့်")]
ph("Micchāmāna", {
    "Idhekacco " + " ".join(f"pāpakena vā {a}" for a, _ in _PAPAKA) + " pāpikāya vā diṭṭhiyā aññataraññatarena "
    "vatthunā mānaṃ jappeti": f"{IDHEKACCO} " + " ".join(f"ယုတ်မာသော {b}{VA}{C}" for _, b in _PAPAKA)
                              + f" ယုတ်မာသော အယူဖြင့်{VA}{C} {VATTHU} {tb('māna')}ကို ဖြစ်ပေါ်စေ၏"})
SENSE_P1 = p1("Sotena saddaṃ sutvā…pe… ghānena").split(" အမှတ်အသားကို")[0]        # နားဖြင့် … မနောဖြင့် သဘောတရားကို သိ၍
EYE_P1 = p1("Idhekacco cakkhunā rūpaṃ disvā nimittaggāhī").removeprefix(IDHEKACCO + " ").split(" အမှတ်အသားကို")[0]
UPAV = {"somanassaṭṭhāniyaṃ": "ဝမ်းမြောက်ဖွယ် ဖြစ်သော", "domanassaṭṭhāniyaṃ": "စိတ်ဆင်းရဲဖွယ် ဖြစ်သော",
        "upekkhāṭṭhāniyaṃ": "လျစ်လျူရှုဖွယ် ဖြစ်သော"}
new("Upavicāra (new)", UPAV | {"upavicarati": "စိတ်ဖြင့် လှည့်လည် ချဉ်းကပ်၏"})


@rx(r"Cakkhunā rūpaṃ disvā (?P<u>\S+) rūpaṃ upavicarati")
def _r6(m):
    return f"{EYE_P1} {UPAV[m['u']]} {F.OBJECT['rūpa']}ကို စိတ်ဖြင့် လှည့်လည် ချဉ်းကပ်၏"


@rx(r"sotena saddaṃ sutvā…pe… ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā ?…pe… kāyena phoṭṭhabbaṃ "
    r"phusitvā…pe… manasā dhammaṃ viññāya (?P<u>\S+) dhammaṃ upavicarati")
def _r7(m):
    return f"{SENSE_P1} {UPAV[m['u']]} သဘောတရားကို စိတ်ဖြင့် လှည့်လည် ချဉ်းကပ်၏"


M_OF = {"manāpiyesu": F.C3["MANAPA"], "amanāpiyesu": F.C3["AMANAPA"],
        "upekkhāṭṭhāniyesu": "လျစ်လျူရှုဖွယ် ဖြစ်သော"}
O_OF = {"rūpesu": F.OBJECT["rūpa"], "saddesu": F.OBJECT["sadda"], "gandhesu": F.OBJECT["gandha"], "rasesu": F.OBJECT["rasa"],
        "phoṭṭhabbesu": F.OBJECT["phoṭṭhabba"], "dhammesu": "သဘောတရား"}


@rx(r"(?P<m>manāpiyesu|amanāpiyesu|upekkhāṭṭhāniyesu|Manāpiyesu|Amanāpiyesu|Upekkhāṭṭhāniyesu) "
    r"(?P<o>rūpesu|saddesu|gandhesu|rasesu|phoṭṭhabbesu|dhammesu)(?P<pe>…pe…)?(?: (?P<l>.+))?")
def _r8(m):
    out = f"{M_OF[m['m'][:1].lower() + m['m'][1:]]} {O_OF[m['o']]}တို့၌"
    if m["pe"]:
        out += PE
    if m["l"]:
        out += " " + list_my(m["l"])
    return out


KV = p1("Satthari kaṅkhati vicikicchati, dhamme")
KV_OBJ = {"Satthari": "ဘုရားရှင်အပေါ်", "dhamme": "တရားတော်အပေါ်", "saṅghe": "သံဃာတော်အပေါ်", "sikkhāya": "ကျင့်စဉ်အပေါ်",
          "pubbante": "အတိတ်ကာလအပေါ်", "aparante": "အနာဂတ်ကာလအပေါ်"}
assert all(v + " သံသယ ဖြစ်၍ ယုံမှားသည်" in KV for v in KV_OBJ.values())
KANKHA = "သံသယ ဖြစ်၍ ယုံမှားသည်"
NADHI = new("Clauses", {"nādhimuccati na sampasīdati": "မဆုံးဖြတ်နိုင်၊ မကြည်လင်"})["nādhimuccati na sampasīdati"]
TIME = {"Atītaṃ vā addhānaṃ": "အတိတ်ကာလကို", "anāgataṃ vā addhānaṃ": "အနာဂတ်ကာလကို",
        "etarahi vā paccuppannaṃ addhānaṃ": "ယခု ပစ္စုပ္ပန်ကာလကို"}
new("Clauses", TIME)


@rx(r"(?P<o>Satthari|dhamme|saṅghe|sikkhāya) kaṅkhati vicikicchati nādhimuccati na sampasīdati")
def _r9(m):
    return f"{KV_OBJ[m['o']]} {KANKHA}{C} {NADHI}"


@rx(r"(?P<o>Atītaṃ vā addhānaṃ|anāgataṃ vā addhānaṃ|etarahi vā paccuppannaṃ addhānaṃ) ārabbha kaṅkhati vicikicchati "
    r"nādhimuccati na sampasīdati")
def _r10(m):
    return f"{TIME[m['o']]} အစွဲပြု၍{VA} {KANKHA}{C} {NADHI}"


@rx(r"(?P<o>Satthari|dhamme|saṅghe|sikkhāya|appamāde|paṭisanthāre) agāravo viharati appatisso")
def _r11(m):
    o = dict(KV_OBJ, appamāde="သတိ မလစ်ခြင်းအပေါ်", paṭisanthāre="ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်းအပေါ်")[m["o"]]
    return f"{o} ရိုသေမှု မရှိ၊ နာခံမှု မရှိဘဲ နေ၏"


VIEW.update(new("Quoted views and statements (new)", {f"{o} {s}hamasmi": f"{om} ငါသည် {sm} ဖြစ်သည်"
                                                     for o, om in MANA_OTHER.items() for s, sm in MANA_SELF.items()}))


@rx(r'"(?P<q>[^"]+)"ti (?P<w>vidhā|māno)')
def _r12(m):
    return f"“{view(m['q'])}”ဟူသော {GROUP['vidhā'] if m['w'] == 'vidhā' else tb('māna')}"


@rx(r'(?P<o>Anicce|dukkhe|anattani|asubhe) "(?P<q>[^"]+)"(?P<n>n?)ti (?P<l>.+)')
def _r13(m):
    o = {"Anicce": "မမြဲသည်၌", "dukkhe": "ဆင်းရဲသည်၌", "anattani": "အတ္တ မဟုတ်သည်၌", "asubhe": "မတင့်တယ်သည်၌"}[m["o"]]
    l = m["l"]
    rest = NAME[l] if l in NAME else list_my(l)
    return f"{o} “{view(m['q'])}”ဟု {rest}"


AV = new("Anariyavohāra (new)", {
    "adiṭṭhe diṭṭhavāditā": "မမြင်သည်ကို မြင်သည်ဟု ပြောခြင်း", "assute sutavāditā": "မကြားသည်ကို ကြားသည်ဟု ပြောခြင်း",
    "amute mutavāditā": "မထိတွေ့သည်ကို ထိတွေ့သည်ဟု ပြောခြင်း", "aviññāte viññātavāditā": "မသိသည်ကို သိသည်ဟု ပြောခြင်း",
    "diṭṭhe adiṭṭhavāditā": "မြင်သည်ကို မမြင်ဟု ပြောခြင်း", "sute assutavāditā": "ကြားသည်ကို မကြားဟု ပြောခြင်း",
    "mute amutavāditā": "ထိတွေ့သည်ကို မထိတွေ့ဟု ပြောခြင်း", "viññāte aviññātavāditā": "သိသည်ကို မသိဟု ပြောခြင်း",
    "lābhe sārāgo": "လာဘ်၌ တပ်မက်ခြင်း", "alābhe paṭivirodho": "လာဘ် မရခြင်း၌ ဆန့်ကျင်ခြင်း",
    "yase sārāgo": "အခြံအရံ ရခြင်း၌ တပ်မက်ခြင်း", "ayase paṭivirodho": "အခြံအရံ မရခြင်း၌ ဆန့်ကျင်ခြင်း",
    "pasaṃsāya sārāgo": "ချီးမွမ်းခြင်း၌ တပ်မက်ခြင်း", "nindāya paṭivirodho": "ကဲ့ရဲ့ခြင်း၌ ဆန့်ကျင်ခြင်း",
    "sukhe sārāgo": "ချမ်းသာ၌ တပ်မက်ခြင်း", "dukkhe paṭivirodho": "ဆင်းရဲ၌ ဆန့်ကျင်ခြင်း",
})
PH.update(AV)


@rx(r'"(?P<q>[^"]+)"(?P<n>n?)ti (?:vā assa )?saccato thetato diṭṭhi uppajjati')
def _r14(m):
    va = VA if " vā assa " in m[0] else ""
    return (f"“{view(m['q'] + ('ṃ' if m['n'] else ''))}”ဟု{va}{' ထိုသူ၏' if va else ''} အမှန်အားဖြင့် ခိုင်မြဲစွာ "
            f"{_D} ဖြစ်ပေါ်၏")


VIEW.update(new("Quoted views and statements (new)", {
    "natthi kāmesu doso": "ကာမတို့၌ အပြစ် မရှိ",
}))
ATTA_X = new("Self views («X attā hoti arogo paraṃ maraṇā»)", {
    "saññī": "မှတ်သိမှု ရှိသူ", "asaññī": "မှတ်သိမှု မရှိသူ", "nevasaññīnāsaññī": "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ",
    "rūpī": "ရုပ် ရှိသူ", "arūpī": "ရုပ် မရှိသူ", "rūpī ca arūpī ca": "ရုပ် ရှိသည်လည်း ဖြစ်၊ မရှိသည်လည်း ဖြစ်သူ",
    "nevarūpīnārūpī": "ရုပ် ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ", "antavā": "အဆုံး ရှိသူ",
    "anantavā": "အဆုံး မရှိသူ", "antavā ca anantavā ca": "အဆုံး ရှိသည်လည်း ဖြစ်၊ မရှိသည်လည်း ဖြစ်သူ",
    "nevantavā nānantavā": "အဆုံး ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ"})
for _x, _xm in ATTA_X.items():
    VIEW[f"{_x} attā hoti arogo paraṃ maraṇā"] = f"အတ္တသည် {_xm} ဖြစ်၍ သေပြီးနောက် အနာကင်း၏"


@rx(r'"(?P<q>[^"]+)"ti ittheke abhivadanti')
def _r15(m):
    return f"“{view(m['q'])}”ဟု ဤသို့ အချို့သူတို့ ကြွေးကြော်ကြ၏"


@rx(r"(?:(?P<x>.+?),? )?tadekaṭṭhaṃ akusalaṃ kāyakammaṃ vacīkammaṃ manokammaṃ")
def _r16(m):
    return ((f"{name(m['x'])}{C} " if m["x"] else "") + "ထိုနှင့် တစ်နေရာတည်း တည်ရှိသော အကုသိုလ် " + f"{tb('kāyakammaṃ')}{C} {tb('vacīkammaṃ')}{C} "
            f"{tb('manokammaṃ')}")


@rx(r"[Tt]attha katamā (?P<x>\S+)")
def _r17(m):
    return ASK.format(name(m["x"]), "")


@rx(r"(?P<x>Cīvara|piṇḍapāta|senāsana|itibhavābhava)hetu vā bhikkhuno taṇhā uppajjamānā uppajjati")
def _r18(m):
    x = {"Cīvara": "သင်္ကန်း", "piṇḍapāta": "ဆွမ်း", "senāsana": "ကျောင်းအိပ်ရာနေရာ", "itibhavābhava": "ဘဝ အဆင့်ဆင့်"}[m["x"]]
    return f"{x}ကြောင့်{VA} ရဟန်း၏ {tb('taṇhā')}သည် ဖြစ်ပေါ်လျှင် ဖြစ်ပေါ်၏"


T9 = new("Taṇhāmūlaka (new)", {"taṇhaṃ": tb("taṇhā"), "pariyesanā": "ရှာမှီးခြင်း", "pariyesanaṃ": "ရှာမှီးခြင်း",
                               "lābho": "ရရှိခြင်း", "lābhaṃ": "ရရှိခြင်း", "vinicchayo": "ဆုံးဖြတ်ခြင်း",
                               "vinicchayaṃ": "ဆုံးဖြတ်ခြင်း", "chandarāgo": "လိုလားမှု ရာဂ", "chandarāgaṃ": "လိုလားမှု ရာဂ",
                               "ajjhosānaṃ": ITEMS["ajjhosānaṃ"], "pariggaho": "သိမ်းပိုက်ခြင်း",
                               "pariggahaṃ": "သိမ်းပိုက်ခြင်း", "macchariyaṃ": tb("macchariya"), "ārakkho": "စောင့်ရှောက်ခြင်း"})


@rx(r"(?P<a>\S+) paṭicca (?P<b>\S+)")
def _r19(m):
    a = m["a"][:1].lower() + m["a"][1:]
    if a not in T9 or m["b"] not in T9:
        raise Miss("t9")
    return f"{T9[a]}ကို စွဲ၍ {T9[m['b']]} ဖြစ်၏"


@rx(r'"(?P<q>[^"]+)"(?P<n>n?)ti (?P<w>iñjita|maññita|phandita|papañcita|saṅkhata)metaṃ')
def _r20(m):
    w = {"iñjita": "တုန်လှုပ်မှု", "maññita": "ထင်မှတ်မှု", "phandita": "လှုပ်ရှားမှု", "papañcita": "ချဲ့ထွင်မှု",
         "saṅkhata": "ပြုပြင်ထားမှု"}[m["w"]]
    return f"“{view(m['q'] + ('ṃ' if m['n'] else ''))}”ဟူသည် ဤ{w} ဖြစ်၏"


@rx(r'"(?P<q>[^"]+)"(?P<n>n?)ti vā')
def _r21(m):
    return f"“{view(m['q'] + ('ṃ' if m['n'] else ''))}”ဟု{VA}"


@rx(r"(?P<q>(?:Sassato|asassato|antavā|anantavā|taṃ jīvaṃ taṃ|aññaṃ jīvaṃ aññaṃ|hoti|na hoti|hoti ca na ca hoti|"
    r"neva hoti na na hoti) .+?)ti vā")
def _r22(m):
    q = m["q"]
    q = q[:-1] + "ṃ" if q.endswith("sarīran") else q
    return f"{view(q)}ဟု{VA}"


@rx(r'"(?P<q>[^"]+)"(?P<n>n?)ti')
def _r23(m):
    return f"“{view(m['q'] + ('ṃ' if m['n'] else ''))}”ဟူ၍"


@rx(r"(?P<n>.+?) (?P<v>\[[^\]]+\])")
def _r24(m):
    return name(m["n"]) + " " + var(m["v"])


# ---- more names
GROUP.update(new("Group nouns («N X» = «X N-ပါး»)", {
    "sassatavādā": "မြဲသည်ဟု ဆိုသော ဝါဒ", "ekaccasassatikā": "အချို့ မြဲသည်ဟု ဆိုသော ဝါဒ",
    "antānantikā": "အဆုံးနှင့် အဆုံးမဲ့ကို ဆိုသော ဝါဒ", "amarāvikkhepikā": "ငါးရှဉ့်ကဲ့သို့ လှည့်ပတ် ပြောသော ဝါဒ",
    "adhiccasamuppannikā": "အကြောင်းမဲ့ ဖြစ်ပေါ်သည်ဟု ဆိုသော ဝါဒ", "saññīvādā": "မှတ်သိမှု ရှိသော အတ္တကို ဆိုသော ဝါဒ",
    "ucchedavādā": "ပြတ်သည်ဟု ဆိုသော ဝါဒ"}))
NAME.update(new("Names (new)", {
    "navavidhā mānā": GROUP["navavidhā mānā"], "kāmarāgo": tb("kāmarāgo"), "bhavarāgo": "ဘဝရာဂ",
    "akusalā saññā": f"အကုသိုလ် {tb('saññā')}", "gottamadādī": f"{NAME['gottamado']} စသည်",
    "cattāro ganthādī": f"{GROUP['ganthā']} လေးပါး စသည်", "nava maññitādīni": f"{GROUP['maññitāni']} ကိုးပါး စသည်",
    "ajjhattikassa upādāya": "အတွင်းကို မှီ၍", "bāhirassa upādāya": "အပြင်ကို မှီ၍",
}))
ORD = {"paṭhamaṃ": "ပထမ", "dutiyaṃ": "ဒုတိယ", "tatiyaṃ": "တတိယ", "catutthaṃ": "စတုတ္ထ", "pañcamaṃ": "ပဉ္စမ",
       "chaṭṭhaṃ": "ဆဋ္ဌမ", "sattamaṃ": "သတ္တမ", "aṭṭhamaṃ": "အဋ္ဌမ"}
for _k, _v in list(ORD.items()):
    ORD[_k[:-1] + "o"] = _v
NUMK = {"Ekaka": "တစ်", "Duka": "နှစ်", "Tika": "သုံး", "Catukka": "လေး", "Pañcaka": "ငါး", "Chakka": "ခြောက်",
        "Sattaka": "ခုနစ်", "Aṭṭhaka": "ရှစ်", "Navaka": "ကိုး", "Dasaka": "ဆယ်"}
HEAD = {"Khuddakavatthuvibhaṅgo": f"အသေးစား အကြောင်းအရာများကို {F.TITLE}",
        "Taṇhāvicaritaniddeso": f"{GROUP['taṇhāvicaritāni']} အကျယ် {F.VARA}", "Mātikā": "ခေါင်းစဉ်စာရင်း"}
for _k, _v in NUMK.items():
    HEAD[_k + "mātikā"] = f"{_v}မျိုးတွဲ ခေါင်းစဉ်စာရင်း"
    HEAD[_k + "niddeso"] = f"{_v}မျိုးတွဲ အကျယ် {F.VARA}"
new("Headings (new)", HEAD)


def dyad(t):
    m = re.fullmatch(r"(?P<a>.+?)(?P<x> ca|ñca) (?P<b>.+?)(?P<v> \[[^\]]+\])?(?P<y> ca|ñca)", t)
    if not m:
        return None
    a = m["a"] + ("ṃ" if m["x"] == "ñca" else "")
    b = m["b"] + ("ṃ" if m["y"] == "ñca" else "")
    return f"{name(a)}နှင့် {name(b)}" + (" " + var(m["v"].strip()) if m["v"] else "")


def head_item(t):
    for f in (lambda x: name(x), dyad):
        try:
            r = f(t)
            if r:
                return r
        except Miss:
            pass
    m = re.fullmatch(r"(?P<n>.+?) (?P<v>\[[^\]]+\])", t)
    if m:
        return head_item(m["n"]) + " " + var(m["v"])
    if ", " in t:
        return f"{C} ".join(head_item(x) for x in t.split(", "))
    raise Miss("heading item: " + t)


def heading(h, t):
    if t in HEAD:
        return f"{h} {HEAD[t]}"
    m = re.fullmatch(r"\((?P<l>[^)]+)\) (?P<t>.+)", t)
    if m:
        return f"{h} ({label(m['l'])}) {head_item(m['t'])}"
    return f"{h} {head_item(t)}"


def matika(body):
    out = []
    for ch in re.split(r"(?=\(\d+\))", body):
        if not ch:
            continue
        m = re.fullmatch(r"\((?P<n>\d+)\)(?P<sp> ?)(?P<t>.*?)(?P<e> ?)", ch)
        out.append(f"({m['n']}){m['sp']}{head_item(m['t'])}{m['e']}")
    return "".join(out)


# ---- narrative sentences
SAMANA = "ဤလောက၌ အချို့သော ရဟန်း သို့မဟုတ် ပုဏ္ဏားသည် ဤသို့ ဆိုလေ့ ရှိသူ၊ ဤသို့ အယူ ရှိသူ ဖြစ်၏"
SAMANA2 = "သို့ရာတွင် ဤလောက၌ အချို့သော ရဟန်း သို့မဟုတ် ပုဏ္ဏားသည် ဤသို့ ဆိုလေ့ ရှိသူ၊ ဤသို့ အယူ ရှိသူ ဖြစ်၏"
ph("Clauses", {
    "Idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhī": SAMANA,
    "idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhī": SAMANA,
    "Idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhi": SAMANA,
    "idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhi": SAMANA,
    "idha panekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhī": SAMANA2,
    "idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhi [evaṃdiṭṭhi (syā.)]":
        SAMANA.removesuffix(" ဖြစ်၏") + " " + var("[evaṃdiṭṭhi (syā.)]") + " ဖြစ်၏",
    '"yaṃ kiñcāyaṃ purisapuggalo paṭisaṃvedeti sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, sabbaṃ taṃ pubbe '
    'katahetū"ti': "“ဤပုဂ္ဂိုလ်သည် သာယာမှုကိုဖြစ်စေ၊ နာကျင်မှုကိုဖြစ်စေ၊ မနာကျင် မသာယာမှုကိုဖြစ်စေ ခံစားရသမျှ "
                   "ထိုအားလုံးသည် ရှေးက ပြုခဲ့သော ကံကြောင့် ဖြစ်သည်”ဟူ၍",
    '"yaṃ kiñcāyaṃ purisapuggalo paṭisaṃvedeti sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, sabbaṃ taṃ '
    'issaranimmānahetū"ti': "“ဤပုဂ္ဂိုလ်သည် သာယာမှုကိုဖြစ်စေ၊ နာကျင်မှုကိုဖြစ်စေ၊ မနာကျင် မသာယာမှုကိုဖြစ်စေ "
                           "ခံစားရသမျှ ထိုအားလုံးသည် ဖန်ဆင်းရှင်၏ ဖန်ဆင်းခြင်းကြောင့် ဖြစ်သည်”ဟူ၍",
    '"yaṃ kiñcāyaṃ purisapuggalo paṭisaṃvedeti sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, sabbaṃ taṃ ahetu '
    'appaccayā"ti': "“ဤပုဂ္ဂိုလ်သည် သာယာမှုကိုဖြစ်စေ၊ နာကျင်မှုကိုဖြစ်စေ၊ မနာကျင် မသာယာမှုကိုဖြစ်စေ ခံစားရသမျှ "
                    "ထိုအားလုံးသည် အကြောင်း မရှိ၊ အထောက်အပံ့ မရှိဘဲ ဖြစ်သည်”ဟူ၍",
    "sabrahmacārīsu kupito hoti anattamano āhatacitto khilajāto":
        "သီတင်းသုံးဖော်တို့အပေါ် အမျက်ထွက်သူ ဖြစ်၏၊ စိတ် မနှစ်သိမ့်သူ၊ ထိခိုက်သော စိတ် ရှိသူ၊ ခက်ထန်သော စိတ် ဖြစ်ပေါ်သူ ဖြစ်၏",
    "Kāme avītarāgo hoti avigatacchando avigatapemo avigatapipāso avigatapariḷāho avigatataṇho":
        "ကာမတို့၌ ရာဂ မကင်းသူ ဖြစ်၏၊ ဆန္ဒ မကင်းသူ၊ ချစ်ခင်မှု မကင်းသူ၊ ငတ်မွတ်မှု မကင်းသူ၊ ပူလောင်မှု မကင်းသူ၊ "
        "တပ်မက်မှု မကင်းသူ ဖြစ်၏",
    "kāye avītarāgo hoti… rūpe avītarāgo hoti… yāvadatthaṃ udarāvadehakaṃ bhuñjitvā seyyasukhaṃ passasukhaṃ "
    "middhasukhaṃ anuyutto viharati": "ကိုယ်၌ ရာဂ မကင်းသူ ဖြစ်၏… ရုပ်၌ ရာဂ မကင်းသူ ဖြစ်၏… ဝမ်းပြည့်အောင် "
                                      "လိုသလောက် စားပြီး၍ အိပ်ခြင်း၏ ချမ်းသာ၊ လှဲလျောင်းခြင်း၏ ချမ်းသာ၊ ငိုက်မျဉ်းခြင်း၏ "
                                      "ချမ်းသာကို အားထုတ်လျက် နေ၏",
    "aññataraṃ devanikāyaṃ paṇidhāya brahmacariyaṃ carati": "နတ်အပေါင်း တစ်ခုခုကို ဆုတောင်း၍ မြတ်သော အကျင့်ကို ကျင့်၏",
    '"imināhaṃ sīlena vā vatena vā tapena vā brahmacariyena vā devo vā bhavissāmi devaññataro vā"ti':
        "“ငါသည် ဤသီလဖြင့်ဖြစ်စေ၊ အကျင့်ဝတ်ဖြင့်ဖြစ်စေ၊ အကျင့်ခြိုးခြံမှုဖြင့်ဖြစ်စေ၊ မြတ်သော အကျင့်ဖြင့်ဖြစ်စေ နတ်ဖြစ်စေ၊ "
        "နတ်တစ်ပါးပါးဖြစ်စေ ဖြစ်ရလိမ့်မည်”ဟူ၍",
    "Mātā jīvitā voropitā hoti": "အမိသည် အသက်မှ ချခံရ၏", "pitā jīvitā voropito hoti": "အဖသည် အသက်မှ ချခံရ၏",
    "arahanto jīvitā voropito hoti": "ရဟန္တာသည် အသက်မှ ချခံရ၏",
    "duṭṭhena cittena tathāgatassa lohitaṃ uppāditaṃ hoti": "ပြစ်မှားသော စိတ်ဖြင့် မြတ်စွာဘုရား၏ သွေးကို ထွက်စေအပ်၏",
    "saṅgho bhinno hoti": "သံဃာသည် ကွဲပြားစေခံရ၏",
    "sato vā pana sattassa ucchedaṃ vināsaṃ vibhavaṃ paññāpenti":
        f"{F.VA_OR} ရှိနေသော သတ္တဝါ၏ ပြတ်စဲခြင်း၊ ပျက်စီးခြင်း၊ ဘဝ ပျောက်ကွယ်ခြင်းကို ပညတ်ကြ၏",
    "diṭṭhadhammanibbānaṃ vā paneke abhivadanti": f"{F.VA_OR} အချို့သူတို့သည် မျက်မှောက်ဘဝ၌ နိဗ္ဗာန်ကို ကြွေးကြော်ကြ၏",
    "Bahuno janassa appiyo hoti amanāpo": "လူအများ၏ မချစ်အပ်၊ မနှစ်သက်အပ်သူ ဖြစ်၏",
    "verabahulo ca hoti": "ရန် များသူလည်း ဖြစ်၏", "vajjabahulo ca": "အပြစ် များသူလည်း ဖြစ်၏",
    "sammūḷho kālaṅkaroti": "တွေဝေလျက် သေရ၏",
    "kāyassa bhedā paraṃ maraṇā apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapajjati":
        "ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက် အပါယ်၊ ဆိုးသော လားရာ၊ ပျက်စီး ကျရောက်ရာ၊ ငရဲသို့ ရောက်ရ၏",
    "Assaddho hoti": "ယုံကြည်မှု မရှိသူ ဖြစ်၏", "ahiriko hoti": "ဒုစရိုက်ကို မရှက်သူ ဖြစ်၏",
    "anottappī hoti": "ဒုစရိုက်ကို မကြောက်ရွံ့သူ ဖြစ်၏", "appassuto hoti": "အကြားအမြင် နည်းသူ ဖြစ်၏",
    "kusīto hoti": "ပျင်းရိသူ ဖြစ်၏", "muṭṭhassatī hoti": "သတိ လစ်သူ ဖြစ်၏", "duppañño hoti": "ပညာ နည်းသူ ဖြစ်၏",
    "ārakkhādhikaraṇaṃ daṇḍādāna-satthādāna-kalaha-viggahavivāda-tuvaṃtuvaṃ-pesuñña-musāvādā aneke pāpakā akusalā "
    "dhammā sambhavanti": "စောင့်ရှောက်ခြင်းကြောင့် တုတ်ကိုင်ခြင်း၊ လက်နက်ကိုင်ခြင်း၊ ခိုက်ရန်ဖြစ်ခြင်း၊ ငြင်းခုံ "
                         "အငြင်းပွားခြင်း၊ နင် ငါ ပြောဆိုခြင်း၊ ကုန်းတိုက်ခြင်း၊ မုသား ပြောခြင်းဟူသော ယုတ်မာသော "
                         "အကုသိုလ် သဘောတရား အများအပြားတို့ ဖြစ်ပေါ်ကြ၏",
    '"Natthi dinnaṃ, natthi yiṭṭhaṃ…pe… ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentī"ti': None,
    "asaññīti naṃ paññapenti": f"ထိုအတ္တကို {ATTA_X['asaññī']}ဟု ပညတ်ကြ၏",
    "nevasaññīnāsaññīti naṃ paññapenti": f"ထိုအတ္တကို {ATTA_X['nevasaññīnāsaññī']}ဟု ပညတ်ကြ၏",
    'arūpī attā…pe… rūpī ca arūpī ca…pe… nevarūpīnārūpī…pe… "antavā attā hoti arogo paraṃ maraṇā"ti':
        f"အတ္တသည် {ATTA_X['arūpī']}… {ATTA_X['rūpī ca arūpī ca']}… {ATTA_X['nevarūpīnārūpī']}… "
        f"“{VIEW['antavā attā hoti arogo paraṃ maraṇā']}”ဟူ၍",
    "atha vā panassa evaṃdiṭṭhi hoti": f"{F.VA_OR} ထိုသူအား ဤသို့ အယူ ရှိ၏",
    '"so me ayaṃ attā vado vedeyyo tatra tatra dīgharattaṃ kalyāṇapāpakānaṃ kammānaṃ vipākaṃ paccanubhoti':
        "“ငါ၏ ဤအတ္တသည် ပြောဆိုတတ်၏၊ ခံစားတတ်၏၊ ထိုထို ဘဝ၌ ကြာမြင့်စွာ ကောင်းသော ကံ၊ ယုတ်မာသော ကံတို့၏ အကျိုးကို "
        "ခံစား၏",
})
_N1 = p1("Natthi dinnaṃ, natthi yiṭṭhaṃ, natthi hutaṃ").split("ဟူ၍")[0]
_N1v = p1("Natthi dinnaṃ, natthi yiṭṭhaṃ, natthi hutaṃ, natthi sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko, natthi ayaṃ "
          "loko, natthi paro loko, natthi mātā, natthi pitā, natthi sattā opapātikā, natthi loke samaṇabrāhmaṇā "
          "sammaggatā [samaggatā (ka.)]").split("ဟူ၍")[0]
_tail = _N1[_N1.index("ဤလောကကိုလည်း"):]
PH['"Natthi dinnaṃ, natthi yiṭṭhaṃ…pe… ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentī"ti'] = \
    "“" + f"{C} ".join(_N1.split(C + " ")[:2]) + PE + " " + _tail + "”ဟူ၍"
NEW["Clauses"]['"Natthi dinnaṃ … pavedentī"ti (pi-1 ^1 natthi list, head 2 + tail)'] = \
    PH['"Natthi dinnaṃ, natthi yiṭṭhaṃ…pe… ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentī"ti']
NEW["Clauses"].pop('"Natthi dinnaṃ, natthi yiṭṭhaṃ…pe… ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā '
                   'pavedentī"ti')
_ASSU = p1("Idha assutavā puthujjano ariyānaṃ adassāvī")
assert _ASSU.count("ဖြစ်၍ ") == 1
_VIN = p1("Viññāṇaṃ attato samanupassati")
_JH = {"vivicceva kāmehi": "ကာမတို့မှ ကင်းဆိတ်၍သာ",
       "vitakkavicārānaṃ vūpasamā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်းကြောင့်",
       "pītiyā ca virāgā": "ပီတိလည်း ပြယ်ပျောက်သွားခြင်းကြောင့်", "sukhassa ca pahānā": "သာယာမှုကိုလည်း ပယ်ခြင်းကြောင့်"}
for _k, _v in _JH.items():
    assert any(_v + PE in y for y in S2.values()), _k
BHO = "အချင်း"
PATTA = "မျက်မှောက်ဘဝ၌ အမြတ်ဆုံး နိဗ္ဗာန်သို့ ရောက်သည်"
SAMUC = "ကောင်းစွာ ပြတ်စဲသည်"
UCCH = f"ခန္ဓာကိုယ် ပြိုကွဲသောအခါ ပြတ်စဲ၏{C} ပျက်စီး၏{C} သေပြီးနောက် မရှိတော့သောကြောင့်"
sent("Sentences (new)", {
    "Idhekacco gihīhi saṃsaṭṭho viharati sahanandī sahasokī, sukhitesu sukhito, dukkhitesu dukkhito, uppannesu "
    "kiccakaraṇīyesu attanā vā yogaṃ āpajjati.": f"{IDHEKACCO} လူဝတ်ကြောင်တို့နှင့် ရောနှော၍ နေ၏၊ အတူ ဝမ်းမြောက်၏၊ "
                                               "အတူ စိုးရိမ်၏၊ ချမ်းသာသူတို့၌ ချမ်းသာ၏၊ ဆင်းရဲသူတို့၌ ဆင်းရဲ၏၊ "
                                               "ပြုဖွယ်ကိစ္စတို့ ဖြစ်ပေါ်လာသောအခါ မိမိကိုယ်တိုင် ဝင်ရောက် "
                                               "ဆောင်ရွက်၏။",
    "Pubbakālaṃ kodho, aparakālaṃ upanāho.": f"အစောပိုင်း အချိန်၌ {NAME['kodho']} ဖြစ်၏၊ နောက်ပိုင်း အချိန်၌ "
                                             f"{NAME['upanāho']} ဖြစ်၏။",
    "Idhekacco kāyena duccaritaṃ caritvā, vācāya duccaritaṃ caritvā, manasā duccaritaṃ caritvā tassa "
    "paṭicchādanahetuṃ pāpikaṃ icchaṃ paṇidahati.": f"{IDHEKACCO} ကိုယ်ဖြင့် ဒုစရိုက်ကို ကျင့်၍၊ နှုတ်ဖြင့် ဒုစရိုက်ကို "
                                                   "ကျင့်၍၊ မနောဖြင့် ဒုစရိုက်ကို ကျင့်၍ ထိုဒုစရိုက်ကို ဖုံးကွယ်ရန် "
                                                   "အလို့ငှာ ယုတ်မာသော အလိုကို ထား၏။",
    '"Mā maṃ jaññā"ti icchati.': f"“{VIEW['mā maṃ jaññā']}”ဟု အလိုရှိ၏။",
    '"Mā maṃ jaññā"ti saṅkappeti.': f"“{VIEW['mā maṃ jaññā']}”ဟု ကြံစည်၏။",
    '"Mā maṃ jaññā"ti vācaṃ bhāsati.': f"“{VIEW['mā maṃ jaññā']}”ဟု စကားကို ပြော၏။",
    '"Mā maṃ jaññā"ti kāyena parakkamati.': f"“{VIEW['mā maṃ jaññā']}”ဟု ကိုယ်ဖြင့် ကြိုးပမ်း၏။",
    "Idhekacco saṭho hoti parisaṭho.": f"{IDHEKACCO} စဉ်းလဲသူ ဖြစ်၏၊ အလွန် စဉ်းလဲသူ ဖြစ်၏။",
    "Yā sā vācā kaṇḍakā kakkasā parakaṭukā parābhisajjanī kodhasāmantā asamādhisaṃvattanikā tathārūpiṃ vācaṃ "
    "bhāsitā hoti.": "ဆူးကဲ့သို့ စူးသော၊ ကြမ်းတမ်းသော၊ သူတစ်ပါးကို ခါးသက်စေသော၊ သူတစ်ပါးကို ထိခိုက်စေသော၊ "
                     "အမျက်ဒေါသနှင့် နီးစပ်သော၊ သမာဓိ မဖြစ်စေတတ်သော စကား ရှိ၏၊ ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏။",
    "Idha assutavā puthujjano ariyānaṃ adassāvī ariyadhammassa akovido ariyadhamme avinīto, sappurisānaṃ adassāvī "
    "sappurisadhammassa akovido sappurisadhamme avinīto – rūpaṃ attato samanupassati rūpavantaṃ vā attānaṃ attani vā "
    "rūpaṃ rūpasmiṃ vā attānaṃ.": _ASSU.replace("ဖြစ်၍ ", "ဖြစ်၍ – "),
    "Vedanaṃ…pe… saññaṃ…pe… saṅkhāre…pe… viññāṇaṃ attato samanupassati viññāṇavantaṃ vā attānaṃ attani vā "
    "viññāṇaṃ viññāṇasmiṃ vā attānaṃ.": f"ခံစားမှုကို{PE} မှတ်သိမှုကို{PE} ပြုပြင်ဖန်တီးမှုများကို{PE} " + _VIN,
    "Satthari kaṅkhati vicikicchati, dhamme kaṅkhati vicikicchati, saṅghe kaṅkhati vicikicchati, sikkhāya kaṅkhati "
    "vicikicchati, pubbante kaṅkhati vicikicchati, aparante kaṅkhati vicikicchati, pubbantāparante kaṅkhati "
    "vicikicchati, idappaccayatāpaṭiccasamuppannesu dhammesu kaṅkhati vicikicchati.": KV,
    "Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi vatena suddhi sīlabbatena suddhīti.": SILABBATA + "ဟူ၍" + END,
    "Avasesā taṇhā kāmataṇhā.": f"ကြွင်းကျန်သော {tb('taṇhā')}သည် {NAME['kāmataṇhā']} {F.COP[False]}{END}",
    '"Sassato loko"ti vā, "asassato loko"ti – vā…pe… "neva hoti na na hoti tathāgato paraṃ maraṇā"ti vā yā evarūpā '
    'diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho – ayaṃ vuccati "brahmacariyesanā".':
        f"“{VIEW['sassato loko']}”ဟု{VA}၊ “{VIEW['asassato loko']}”ဟု – {VA}{PE} “"
        f"{VIEW['neva hoti na na hoti tathāgato paraṃ maraṇā']}”ဟု{VA} "
        + EV + list_my("diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho") + " ရှိသမျှ – ဤသည်ကို “"
        + NAME["brahmacariyesanā"] + "”ဟု ခေါ်သည်။",
    "So kāmesu pātabyataṃ āpajjati.": "ထိုသူသည် ကာမတို့၌ သောက်သုံးသကဲ့သို့ နစ်မွန်းခြင်းသို့ ရောက်၏။",
    "Tattha katame cattāro ganthā …pe… cattāro oghā…pe… cattāro yogā…pe… cattāri upādānāni?":
        f"ထိုတို့အနက် {GROUP['ganthā']} လေးပါး{PE} {GROUP['oghā']} လေးပါး{PE} {GROUP['yogā']} လေးပါး{PE} "
        f"{GROUP['upādānāni']} လေးပါး ဟူသည် အဘယ်တို့နည်း။",
    "Chandāgatiṃ gacchati, dosāgatiṃ gacchati, mohāgatiṃ gacchati, bhayāgatiṃ gacchati.":
        "ဆန္ဒ အဂတိသို့ လိုက်၏၊ ဒေါသ အဂတိသို့ လိုက်၏၊ မောဟ အဂတိသို့ လိုက်၏၊ ကြောက်ခြင်း အဂတိသို့ လိုက်၏။",
    "Chandarāgā gehasitā dhammā.": f"{GROUP['chandarāgā']}တို့သည် လောကီ အိမ်ရာကို မှီသော သဘောတရားများ ဖြစ်ကြသည်။",
    "Tattha katamāni nava maññitāni… nava phanditāni… nava papañcitāni… nava saṅkhatāni?":
        f"ထိုတို့အနက် {GROUP['maññitāni']} ကိုးပါး… {GROUP['phanditāni']} ကိုးပါး… {GROUP['papañcitāni']} ကိုးပါး… "
        f"{GROUP['saṅkhatāni']} ကိုးပါး ဟူသည် အဘယ်တို့နည်း။",
    "Natthi dinnaṃ, natthi yiṭṭhaṃ, natthi hutaṃ, natthi sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko, natthi ayaṃ loko, "
    "natthi paro loko, natthi mātā, natthi pitā, natthi sattā opapātikā, natthi loke samaṇabrāhmaṇā sammaggatā "
    "[samaggatā (ka.)] sammā paṭipannā ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentīti – ayaṃ "
    "dasavatthukā micchādiṭṭhi.": _N1v + "ဟူ၍ – ဤသည်မှာ " + NAME["dasavatthukā micchādiṭṭhi"] + " ဖြစ်သည်။",
    "Ittheke sato sattassa paramadiṭṭhadhammanibbānaṃ paññapenti.":
        "ဤသို့ အချို့သူတို့သည် ရှိနေသော သတ္တဝါ၏ မျက်မှောက်ဘဝ၌ အမြတ်ဆုံး နိဗ္ဗာန်ကို ပညတ်ကြ၏။",
    "Ittheke sato sattassa ucchedaṃ vināsaṃ vibhavaṃ paññapenti.":
        "ဤသို့ အချို့သူတို့သည် ရှိနေသော သတ္တဝါ၏ ပြတ်စဲခြင်း၊ ပျက်စီးခြင်း၊ ဘဝ ပျောက်ကွယ်ခြင်းကို ပညတ်ကြ၏။",
    "Taṃ kissa hetu?": "ထိုသို့ အဘယ်ကြောင့်နည်း။",
    "Kāmā hi, bho, aniccā dukkhā vipariṇāmadhammā.": f"{BHO}၊ ကာမတို့သည် မမြဲကုန်၊ ဆင်းရဲကုန်၊ ဖောက်ပြန်ခြင်း "
                                                     "သဘော ရှိကုန်၏။",
    "Tesaṃ vipariṇāmaññathābhāvā uppajjanti sokaparidevadukkhadomanassupāyāsā.":
        "ထိုကာမတို့၏ ဖောက်ပြန်ခြင်း၊ တစ်မျိုးတစ်ဖုံ ဖြစ်ခြင်းကြောင့် စိုးရိမ်ခြင်း၊ ငိုကြွေးခြင်း၊ ကိုယ်ဆင်းရဲခြင်း၊ "
        "စိတ်ဆင်းရဲမှု၊ ပြင်းစွာ ပူပန်ခြင်းတို့ ဖြစ်ပေါ်ကြ၏။",
    "No ca kho, bho, ayaṃ attā ettāvatā paramadiṭṭhadhammanibbānappatto hoti.":
        f"{BHO}၊ သို့သော် ဤအတ္တသည် ဤမျှဖြင့် {PATTA} မဟုတ်။",
    "No ca kho, bho, ayaṃ attā ettāvatā sammā samucchinno hoti.": f"{BHO}၊ သို့သော် ဤအတ္တသည် ဤမျှဖြင့် {SAMUC} မဟုတ်။",
    "Neso natthīti vadāmi.": "ထိုအတ္တ မရှိဟု ငါ မဆို။",
    "‘Neso natthī’ti vadāmi.": "‘ထိုအတ္တ မရှိ’ဟု ငါ မဆို။",
    "Yadeva tattha vitakkitaṃ vicāritaṃ etena etaṃ oḷārikaṃ akkhāyati.":
        "ထိုဈာန်၌ စတင်ကြံစည်ခြင်း၊ ဆက်လက်သုံးသပ်ခြင်း ရှိသမျှ ထိုအရာကြောင့် ဤဈာန်ကို ရုန့်ရင်းသည်ဟု ဆိုရ၏။",
    "Yadeva tattha pītigataṃ cetaso uppilāvitaṃ, etena etaṃ oḷārikaṃ akkhāyati.":
        "ထိုဈာန်၌ ပီတိ ဖြစ်ခြင်း၊ စိတ်၏ ဖောင်းကြွခြင်း ရှိသမျှ ထိုအရာကြောင့် ဤဈာန်ကို ရုန့်ရင်းသည်ဟု ဆိုရ၏။",
    "Yadeva tattha sukhapīti cetaso ābhogo, etena etaṃ oḷārikaṃ akkhāyati.":
        "ထိုဈာန်၌ သာယာမှုနှင့် ပီတိဟု စိတ်၏ ညွတ်ခြင်း ရှိသမျှ ထိုအရာကြောင့် ဤဈာန်ကို ရုန့်ရင်းသည်ဟု ဆိုရ၏။",
    "Atthi kho bho añño attā dibbo rūpī kāmāvacaro kabaḷīkārabhakkho.":
        f"{BHO}၊ နတ်၌ ဖြစ်သော၊ ရုပ် ရှိသော၊ {T['kāmāvacarā']}၊ လုတ်ပြု၍ စားရသော အစာကို စားသော အခြား အတ္တ ရှိ၏။",
    "Atthi kho, bho, añño attā dibbo rūpī manomayo sabbaṅgapaccaṅgī ahīnindriyo.":
        f"{BHO}၊ နတ်၌ ဖြစ်သော၊ ရုပ် ရှိသော၊ စိတ်ဖြင့် ဖြစ်သော၊ ကြီးငယ် အင်္ဂါ အားလုံး ပြည့်စုံသော၊ မချို့ယွင်းသော "
        "အာရုံခံ စွမ်းရည် ရှိသော အခြား အတ္တ ရှိ၏။",
    "Atthi kho, bho, añño attā sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ "
    "amanasikārā ananto ākāsoti ākāsānañcāyatanūpago.":
        f"{BHO}၊ ရုပ်ဟု မှတ်သိမှုတို့ကို အလုံးစုံ ကျော်လွန်ခြင်းကြောင့် ထိခိုက်မှုဟု မှတ်သိမှုတို့ ချုပ်ငြိမ်းသွားခြင်းကြောင့် "
        "အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှုတို့ကို နှလုံး မသွင်းခြင်းကြောင့် ဟင်းလင်းပြင်သည် အဆုံး မရှိဟု အဆုံး မရှိသော "
        "ဟင်းလင်းပြင် နယ်ပယ်သို့ ရောက်သော အခြား အတ္တ ရှိ၏။",
    "Atthi kho, bho, añño attā sabbaso ākāsānañcāyatanaṃ samatikkamma anantaṃ viññāṇanti viññāṇañcāyatanūpago.":
        f"{BHO}၊ အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍ သိစိတ်သည် အဆုံး မရှိဟု အဆုံး မရှိသော "
        "သိစိတ် နယ်ပယ်သို့ ရောက်သော အခြား အတ္တ ရှိ၏။",
    "Atthi kho, bho, añño attā sabbaso viññāṇañcāyatanaṃ samatikkamma natthi kiñcīti ākiñcaññāyatanūpago.":
        f"{BHO}၊ အဆုံး မရှိသော သိစိတ် နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍ ဘာမျှ မရှိဟု ဘာမျှ မရှိသော နယ်ပယ်သို့ ရောက်သော "
        "အခြား အတ္တ ရှိ၏။",
    "Atthi kho, bho, añño attā sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanūpago.":
        f"{BHO}၊ ဘာမျှ မရှိသော နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍ မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း "
        "မဟုတ်သော နယ်ပယ်သို့ ရောက်သော အခြား အတ္တ ရှိ၏။",
    "Taṃ tvaṃ na jānāsi na passasi.": "ထိုအတ္တကို သင် မသိ၊ မမြင်။",
    "Tamahaṃ jānāmi passāmi.": "ထိုအတ္တကို ငါ သိ၏၊ မြင်၏။",
    'So kho, bho, attā yato kāyassa bhedā ucchijjati vinassati na hoti paraṃ maraṇā, ettāvatā kho, bho, ayaṃ attā '
    'sammāsamucchinno hotī"ti.': f"{BHO}၊ ထိုအတ္တသည် {UCCH} {BHO}၊ ဤမျှဖြင့် ဤအတ္တသည် {SAMUC} ဖြစ်၏”ဟု။",
    'So kho, bho, attā yato kāyassa bhedā ucchijjati vinassati na hoti paraṃ maraṇā, ettāvatā kho, bho, ayaṃ attā '
    'sammā samucchinno hotī"ti.': f"{BHO}၊ ထိုအတ္တသည် {UCCH} {BHO}၊ ဤမျှဖြင့် ဤအတ္တသည် {SAMUC} ဖြစ်၏”ဟု။",
    'Na so jāto nāhosi, na so jāto na bhavissati, nicco dhuvo sassato avipariṇāmadhammo"ti vā panassa saccato '
    'thetato diṭṭhi uppajjati.': f"ထိုအတ္တသည် မွေးဖွားသည် မဟုတ်၊ မဖြစ်ခဲ့၊ ထိုအတ္တသည် မွေးဖွားသည် မဟုတ်၊ မဖြစ်လတ္တံ့၊ "
                                 f"မြဲ၏၊ ခိုင်မြဲ၏၊ ထာဝရ တည်၏၊ ဖောက်ပြန်ခြင်း မရှိသော သဘော ရှိ၏”ဟု{VA} ထိုသူ၏ "
                                 f"အမှန်အားဖြင့် ခိုင်မြဲစွာ {_D} ဖြစ်ပေါ်၏။",
    "Yāni ca dvāsaṭṭhi diṭṭhigatāni brahmajāle veyyākaraṇe vuttāni bhagavatā.":
        f"မြတ်စွာဘုရားသည် ဗြဟ္မဇာလ ဒေသနာ၌ ဟောတော်မူခဲ့သော {GROUP['diṭṭhigatāni']} ခြောက်ဆယ့်နှစ်ပါးလည်း ရှိ၏။",
    "Tattha katamāni dvāsaṭṭhi diṭṭhigatāni brahmajāle veyyākaraṇe vuttāni bhagavatā?":
        f"ထိုတို့အနက် မြတ်စွာဘုရားသည် ဗြဟ္မဇာလ ဒေသနာ၌ ဟောတော်မူခဲ့သော {GROUP['diṭṭhigatāni']} ခြောက်ဆယ့်နှစ်ပါး "
        "ဟူသည် အဘယ်တို့နည်း။",
    "Cattāro sassatavādā, cattāro ekaccasassatikā, cattāro antānantikā, cattāro amarāvikkhepikā, dve "
    "adhiccasamuppannikā, soḷasa saññīvādā, aṭṭha asaññīvādā, aṭṭha nevasaññīnāsaññīvādā, satta ucchedavādā, pañca "
    "diṭṭhadhammanibbānavādā – imāni dvāsaṭṭhi diṭṭhigatāni brahmajāle veyyākaraṇe vuttāni bhagavatāti.":
        f"{C} ".join(name(x) for x in ("cattāro sassatavādā", "cattāro ekaccasassatikā", "cattāro antānantikā",
                                        "cattāro amarāvikkhepikā", "dve adhiccasamuppannikā", "soḷasa saññīvādā",
                                        "aṭṭha asaññīvādā", "aṭṭha nevasaññīnāsaññīvādā", "satta ucchedavādā",
                                        "pañca diṭṭhadhammanibbānavādā"))
        + f" – ဤသည်တို့မှာ မြတ်စွာဘုရားသည် ဗြဟ္မဇာလ ဒေသနာ၌ ဟောတော်မူခဲ့သော {GROUP['diṭṭhigatāni']} "
          "ခြောက်ဆယ့်နှစ်ပါး ဖြစ်ကြသည်ဟူ၍။",
    "Khuddakavatthuvibhaṅgo niṭṭhito.": f"“{HEAD['Khuddakavatthuvibhaṅgo']}” {F.NITTHITA}{END}",
})
_TA = GROUP["taṇhāvicaritāni"]
_SUM = F.SUMMARY_END
_AJJ, _BAH = f"အတွင်းကို မှီ၍ ဖြစ်သော {_TA}", f"အပြင်ကို မှီ၍ ဖြစ်သော {_TA}"
sent("Sentences (new)", {
    "Aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya, aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya, tadekajjhaṃ "
    "abhisaññūhitvā abhisaṅkhipitvā chattiṃsa taṇhāvicaritāni honti.":
        f"{_AJJ} ဆယ့်ရှစ်ပါး၊ {_BAH} ဆယ့်ရှစ်ပါး၊ {_SUM} {_TA} သုံးဆယ့်ခြောက်ပါး ဖြစ်ကြ၏။",
    "Iti atītāni chattiṃsa taṇhāvicaritāni, anāgatāni chattiṃsa taṇhāvicaritāni, paccuppannāni chattiṃsa "
    "taṇhāvicaritāni, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā aṭṭha taṇhāvicaritasataṃ hoti.":
        f"ဤသို့ {F.Q11A['atīta']} {_TA} သုံးဆယ့်ခြောက်ပါး၊ {F.Q11A['anāgata']} {_TA} သုံးဆယ့်ခြောက်ပါး၊ "
        f"{F.Q11A['paccuppanna']} {_TA} သုံးဆယ့်ခြောက်ပါး၊ {_SUM} {_TA} တစ်ရာ့ရှစ်ပါး ဖြစ်၏။",
    "Imāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya.": f"ဤသည်တို့မှာ {_AJJ} ဆယ့်ရှစ်ပါး ဖြစ်ကြသည်။",
    "Imāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya.": f"ဤသည်တို့မှာ {_BAH} ဆယ့်ရှစ်ပါး ဖြစ်ကြသည်။",
    "Iti imāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya, imāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya, "
    "tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā chattiṃsa taṇhāvicaritāni honti.":
        f"ဤသို့ ဤ{_AJJ} ဆယ့်ရှစ်ပါး၊ ဤ{_BAH} ဆယ့်ရှစ်ပါး၊ {_SUM} {_TA} သုံးဆယ့်ခြောက်ပါး ဖြစ်ကြ၏။",
    "Iti evarūpāni atītāni chattiṃsa taṇhāvicaritāni, anāgatāni chattiṃsa taṇhāvicaritāni, paccuppannāni chattiṃsa "
    "taṇhāvicaritāni, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā aṭṭhataṇhāvicaritasataṃ hoti.":
        f"ဤသို့ {EV}{F.Q11A['atīta']} {_TA} သုံးဆယ့်ခြောက်ပါး၊ {F.Q11A['anāgata']} {_TA} သုံးဆယ့်ခြောက်ပါး၊ "
        f"{F.Q11A['paccuppanna']} {_TA} သုံးဆယ့်ခြောက်ပါး၊ {_SUM} {_TA} တစ်ရာ့ရှစ်ပါး ဖြစ်၏။",
    "Tattha katamāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya?": ASK.format(f"{_AJJ} ဆယ့်ရှစ်ပါး", "တို့") + END,
    "Tattha katamāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya?": ASK.format(f"{_BAH} ဆယ့်ရှစ်ပါး", "တို့") + END,
})


# ---- diṭṭhadhammanibbāna / satta diṭṭhiyo openers
_ORDJ = {"paṭhamaṃ": "vivicceva kāmehi", "dutiyaṃ": "vitakkavicārānaṃ vūpasamā", "tatiyaṃ": "pītiyā ca virāgā",
         "catutthaṃ": "sukhassa ca pahānā"}
for _o, _p in _ORDJ.items():
    SENT[f'Yato kho, bho, ayaṃ attā {_p}…pe… {_o} jhānaṃ upasampajja viharati, ettāvatā kho, bho, ayaṃ attā '
         f'paramadiṭṭhadhammanibbānappatto hotī"ti.'] = (f"{BHO}၊ ဤအတ္တသည် {_JH[_p]}{PE} {ORD[_o]} ဈာန်ကို ဝင်စား၍ "
                                                       f"နေသောကြောင့် {BHO}၊ ဤမျှဖြင့် ဤအတ္တသည် {PATTA} ဖြစ်၏”ဟု။")
ph("Clauses", {
    '"yato kho, bho, ayaṃ attā pañcahi kāmaguṇehi samappito samaṅgībhūto paricāreti, ettāvatā kho, bho, ayaṃ attā '
    'paramadiṭṭhadhammanibbānappatto hotī"ti': f"“{BHO}၊ ဤအတ္တသည် ကာမဂုဏ် ငါးပါးတို့ဖြင့် ပြည့်စုံ၍ ယှဉ်လျက် "
                                              f"မွေ့လျော်သောကြောင့် {BHO}၊ ဤမျှဖြင့် ဤအတ္တသည် {PATTA} ဖြစ်၏”ဟူ၍",
    '"yato kho, bho, ayaṃ attā rūpī cātumahābhūtiko [cātummahābhūtiko (sī. syā.)] mātāpettikasambhavo kāyassa '
    'bhedā ucchijjati vinassati na hoti paraṃ maraṇā, ettāvatā kho bho, ayaṃ attā sammā samucchinno hotī"ti':
        f"“{BHO}၊ ဤအတ္တသည် ရုပ် ရှိ၏၊ မူလဓာတ်ကြီး လေးပါးဖြင့် ဖြစ်၏ {var('[cātummahābhūtiko (sī. syā.)]')}၊ "
        f"အမိအဖတို့မှ ဖြစ်ပေါ်လာ၏၊ {UCCH} {BHO}၊ ဤမျှဖြင့် ဤအတ္တသည် {SAMUC} ဖြစ်၏”ဟူ၍",
    "tamañño evamāha": "ထိုသူကို အခြားသူက ဤသို့ ဆို၏",
})
sent("Sentences (new)", {
    '"atthi kho, bho, eso attā yaṃ tvaṃ vadesi neso natthīti vadāmi.': None,
})
SENT.pop('"atthi kho, bho, eso attā yaṃ tvaṃ vadesi neso natthīti vadāmi.')
NEW["Sentences (new)"].pop('"atthi kho, bho, eso attā yaṃ tvaṃ vadesi neso natthīti vadāmi.')
_ATTHI = f"{BHO}၊ သင် ပြောသော ထိုအတ္တသည် ရှိပါ၏"
_ATTHI2 = "သင် ပြောသော ထိုအတ္တသည် ရှိပါ၏"
for _tm in ("(Kha) ", "(Ga) ", "(Gha) ", "(Ṅa) ", "(Ca) ", "(Cha) "):
    pass
ph("Clauses", {
    '"atthi kho, bho, eso attā yaṃ tvaṃ vadesi neso natthīti vadāmi': f"“{_ATTHI}၊ ထိုအတ္တ မရှိဟု ငါ မဆို",
})


@rx(r'(?P<a>tamañño evamāha) – "atthi kho,? (?P<b>bho,|pana) eso attā yaṃ tvaṃ vadesi')
def _r25(m):
    return "ထိုသူကို အခြားသူက ဤသို့ ဆို၏ – “" + (_ATTHI if m["b"] == "bho," else _ATTHI2)


# ---- kusītavatthu
_KUS_END = (f"ထိုရဟန်းသည် လှဲလျောင်း၏၊ မရောက်သေးသည်ကို ရောက်ရန်၊ မရရှိသေးသည်ကို ရရှိရန်၊ မျက်မှောက် "
            f"မပြုရသေးသည်ကို မျက်မှောက်ပြုရန် ဝီရိယကို မအားထုတ်{END}")
_PUNA = "တစ်ဖန် နောက်တစ်မျိုးမှာ "
_TASSA = "ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “"
_GAMA = (f"ရွာသို့{VA}၊ နိဂုံးသို့{VA} ဆွမ်းခံ လှည့်လည်လျက် ကြမ်းတမ်းသော အစာ၏{VA}၊ မွန်မြတ်သော အစာ၏{VA} လိုသလောက် "
         "ပြည့်စုံမှုကို")
sent("Kusītavatthu (new)", {
    "So nipajjati; na vīriyaṃ ārabhati appattassa pattiyā, anadhigatassa adhigamāya, asacchikatassa sacchikiriyāya.":
        _KUS_END,
    "idha bhikkhunā kammaṃ kātabbaṃ hoti.": "ဤသာသနာ၌ ရဟန်းသည် ပြုရမည့် အလုပ် ရှိ၏။",
    'Tassa evaṃ hoti – "kammaṃ kho me kātabbaṃ bhavissati.': _TASSA + "ငါ ပြုရမည့် အလုပ် ရှိလိမ့်မည်။",
    "Kammaṃ kho pana me karontassa kāyo kilamissati.": "အလုပ်ကို ပြုနေသော ငါ၏ ကိုယ်သည် ပင်ပန်းလိမ့်မည်။",
    'Handāhaṃ nipajjāmī"ti.': "ယခု ငါ လှဲလျောင်းအံ့”ဟု။",
    "puna caparaṃ bhikkhunā kammaṃ kataṃ hoti.": _PUNA + "ရဟန်းသည် အလုပ်ကို ပြုပြီး ဖြစ်၏။",
    'Tassa evaṃ hoti – "ahaṃ kho kammaṃ akāsiṃ.': _TASSA + "ငါ အလုပ်ကို ပြုခဲ့ပြီ။",
    "Kammaṃ kho pana me karontassa kāyo kilanto.": "အလုပ်ကို ပြုနေသော ငါ၏ ကိုယ်သည် ပင်ပန်းပြီ။",
    "puna caparaṃ bhikkhunā maggo gantabbo hoti.": _PUNA + "ရဟန်းသည် သွားရမည့် ခရီး ရှိ၏။",
    'Tassa evaṃ hoti – "maggo kho me gantabbo bhavissati.': _TASSA + "ငါ သွားရမည့် ခရီး ရှိလိမ့်မည်။",
    "Maggaṃ kho pana me gacchantassa kāyo kilamissati.": "ခရီးကို သွားနေသော ငါ၏ ကိုယ်သည် ပင်ပန်းလိမ့်မည်။",
    "puna caparaṃ bhikkhunā maggo gato hoti.": _PUNA + "ရဟန်းသည် ခရီးကို သွားပြီး ဖြစ်၏။",
    'Tassa evaṃ hoti – "ahaṃ kho maggaṃ agamāsiṃ.': _TASSA + "ငါ ခရီးကို သွားခဲ့ပြီ။",
    "Maggaṃ kho pana me gacchantassa kāyo kilanto.": "ခရီးကို သွားနေသော ငါ၏ ကိုယ်သည် ပင်ပန်းပြီ။",
    "puna caparaṃ bhikkhu gāmaṃ vā nigamaṃ vā piṇḍāya caranto na labhati lūkhassa vā paṇītassa vā bhojanassa "
    "yāvadatthaṃ pāripūriṃ.": f"{_PUNA}ရဟန်းသည် {_GAMA} မရ။",
    'Tassa evaṃ hoti – "ahaṃ kho gāmaṃ vā nigamaṃ vā piṇḍāya caranto nālatthaṃ lūkhassa vā paṇītassa vā bhojanassa '
    'yāvadatthaṃ pāripūriṃ.': f"{_TASSA}ငါ {_GAMA} မရခဲ့။",
    "Tassa me kāyo kilanto akammañño.": "ထိုငါ၏ ကိုယ်သည် ပင်ပန်း၏၊ အလုပ်နှင့် မလျော်။",
    "puna caparaṃ bhikkhu gāmaṃ vā nigamaṃ vā piṇḍāya caranto labhati lūkhassa vā paṇītassa vā bhojanassa "
    "yāvadatthaṃ pāripūriṃ.": f"{_PUNA}ရဟန်းသည် {_GAMA} ရ၏။",
    'Tassa evaṃ hoti – "ahaṃ kho gāmaṃ vā nigamaṃ vā piṇḍāya caranto alatthaṃ lūkhassa vā paṇītassa vā bhojanassa '
    'yāvadatthaṃ pāripūriṃ.': f"{_TASSA}ငါ {_GAMA} ရခဲ့ပြီ။",
    "Tassa me kāyo kilanto akammañño māsācitaṃ maññe.":
        "ထိုငါ၏ ကိုယ်သည် ပင်ပန်း၏၊ အလုပ်နှင့် မလျော်၊ ပဲတင်ထားသကဲ့သို့ လေးလံ၏ဟု ထင်၏။",
    "puna caparaṃ bhikkhuno uppanno hoti appamattako ābādho.": f"{_PUNA}ရဟန်းအား အနည်းငယ်သော အနာရောဂါ ဖြစ်ပေါ်၏။",
    'Tassa evaṃ hoti – "uppanno kho me ayaṃ appamattako ābādho.': _TASSA + "ငါ့အား ဤအနည်းငယ်သော အနာရောဂါ ဖြစ်ပေါ်ပြီ။",
    "Atthi kappo nipajjituṃ.": "လှဲလျောင်းရန် သင့်လျော်၏။",
    "puna caparaṃ bhikkhu gilānā vuṭṭhito [gilānavuṭṭhito (saddanībhi) a. ni. 6.16 pāḷiyā ṭīkā passitabbā] hoti "
    "aciravuṭṭhito gelaññā.": f"{_PUNA}ရဟန်းသည် ဖျားနာခြင်းမှ ထပြီး "
                             f"{var('[gilānavuṭṭhito (saddanībhi) a. ni. 6.16 pāḷiyā ṭīkā passitabbā]')} ဖြစ်၏၊ "
                             "ဖျားနာခြင်းမှ ထသည်မှာ မကြာသေး။",
    'Tassa evaṃ hoti – "ahaṃ kho gilānā vuṭṭhito aciravuṭṭhito gelaññā.':
        _TASSA + "ငါ ဖျားနာခြင်းမှ ထပြီး ဖြစ်၏၊ ဖျားနာခြင်းမှ ထသည်မှာ မကြာသေး။",
    "Tassa me kāyo dubbalo akammañño.": "ထိုငါ၏ ကိုယ်သည် အားနည်း၏၊ အလုပ်နှင့် မလျော်။",
})
for _o in ("paṭhamaṃ", "dutiyaṃ", "tatiyaṃ", "catutthaṃ", "pañcamaṃ", "chaṭṭhaṃ", "sattamaṃ", "aṭṭhamaṃ"):
    SENT[f"Idaṃ {_o} kusītavatthu."] = f"ဤသည်မှာ {ORD[_o]} {GROUP['kusītavatthūni']} ဖြစ်သည်{END}"
    SENT[f"Ayaṃ {_o[:-2]}o purisadoso."] = f"ဤသည်မှာ {ORD[_o]} {GROUP['purisadosā']} ဖြစ်သည်{END}"
# ---- purisadosa
_SOBH = "ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ"
_CODENTI = "ရဟန်းတို့သည် ရဟန်းကို အာပတ်ဖြင့် စောဒနာကြ၏။"
sent("Purisadosa (new)", {
    "idha bhikkhū bhikkhuṃ āpattiyā codenti.": "ဤသာသနာ၌ " + _CODENTI,
    "puna caparaṃ bhikkhū bhikkhuṃ āpattiyā codenti.": _PUNA + _CODENTI,
    'So bhikkhu bhikkhūhi āpattiyā codiyamāno [codiyamāno (sī. syā.) a. ni. 8.14] "na sarāmi na sarāmī"ti '
    'assatiyāva nibbeṭheti.': f"{_SOBH} {var('[codiyamāno (sī. syā.) a. ni. 8.14]')} “{VIEW['na sarāmi na sarāmi']}”ဟု "
                              "သတိ မရှိဟန်ဖြင့်သာ ငြင်းဆို၏။",
    'So bhikkhu bhikkhūhi āpattiyā codiyamāno codakaṃyeva paṭippharati – "kiṃ nu kho tuyhaṃ bālassa abyattassa '
    'bhaṇitena! Tvampi nāma maṃ bhaṇitabbaṃ maññasī"ti! Ayaṃ dutiyo purisadoso.':
        f"{_SOBH} စောဒနာသူကိုသာ ပြန်လည် တိုက်ခိုက်၏ – “မိုက်မဲ၍ မလိမ္မာသော သင်၏ ပြောဆိုမှုဖြင့် အဘယ် အကျိုး ရှိမည်နည်း။ "
        f"သင်ပင်လျှင် ငါ့ကို ပြောဆိုထိုက်သည်ဟု ထင်သလော”ဟု။ ဤသည်မှာ {ORD['dutiyaṃ']} {GROUP['purisadosā']} ဖြစ်သည်။",
    'So bhikkhu bhikkhūhi āpattiyā codiyamāno codakaṃyeva [codakasseva (syā.) a. ni. 8.14] paccāropeti – "tvampi '
    'khosi itthannāmaṃ āpattiṃ āpanno.': f"{_SOBH} စောဒနာသူကိုသာ {var('[codakasseva (syā.) a. ni. 8.14]')} ပြန်လည် "
                                       "စွပ်စွဲ၏ – “သင်လည်း ဤမည်သော အာပတ်သို့ ရောက်ခဲ့ပြီ။",
    'Tvaṃ tāva paṭhamaṃ paṭikarohī"ti.': "သင် ဦးစွာ ကုစားလော့”ဟု။",
    "So bhikkhu bhikkhūhi āpattiyā codiyamāno aññenāññaṃ paṭicarati, bahiddhā kathaṃ apanāmeti, kopañca dosañca "
    "appaccayañca pātukaroti.": f"{_SOBH} တစ်ခုဖြင့် တစ်ခုကို လွှဲရှောင်၏၊ စကားကို ပြင်ပသို့ လွှဲ၏၊ အမျက်ကိုလည်းကောင်း၊ "
                                "ဒေါသကိုလည်းကောင်း၊ မနှစ်သက်မှုကိုလည်းကောင်း ထင်ရှားစေ၏။",
    "So bhikkhu bhikkhūhi āpattiyā codiyamāno saṅghamajjhe bāhāvikkhepakaṃ bhaṇati.":
        f"{_SOBH} သံဃာ့အလယ်၌ လက်ကို ဝှေ့ယမ်း၍ ပြောဆို၏။",
    "So bhikkhu bhikkhūhi āpattiyā codiyamāno anādiyitvā saṅghaṃ, anādiyitvā codakaṃ, sāpattikova [āpattikova (ka.) "
    "a. ni. 8.14] yenakāmaṃ pakkamati.": f"{_SOBH} သံဃာကို အလေးမထား၍၊ စောဒနာသူကို အလေးမထား၍ အာပတ် ရှိလျက်ပင် "
                                         f"{var('[āpattikova (ka.) a. ni. 8.14]')} အလိုရှိရာသို့ ထွက်သွား၏။",
    'So bhikkhu bhikkhūhi āpattiyā codiyamāno "nevāhaṃ āpannomhi, na panāhaṃ anāpannomhī"ti tuṇhībhūto saṅghaṃ '
    'viheseti.': f"{_SOBH} “{VIEW['nevāhaṃ āpannomhi, na panāhaṃ anāpannomhi']}”ဟု ဆိတ်ဆိတ် နေ၍ သံဃာကို နှောင့်ယှက်၏။",
    'So bhikkhu bhikkhūhi āpattiyā codiyamāno evamāha – "kiṃ nu kho tumhe āyasmanto atibāḷhaṃ mayi byāvaṭā.':
        f"{_SOBH} ဤသို့ ဆို၏ – “အသျှင်တို့ သင်တို့သည် ငါ့အပေါ် အဘယ်ကြောင့် အလွန်အမင်း ဂရုစိုက်နေကြသနည်း။",
    'Idānāhaṃ sikkhaṃ paccakkhāya hīnāyāvattissāmī"ti.': "ယခု ငါ သိက္ခာကို စွန့်၍ လူဘောင်သို့ ပြန်လည်မည်”ဟု။",
    'So sikkhaṃ paccakkhāya hīnāyāvattitvā evamāha – "idāni kho tumhe āyasmanto attamanā hothā"ti.':
        "ထိုရဟန်းသည် သိက္ခာကို စွန့်၍ လူဘောင်သို့ ပြန်လည်ပြီး ဤသို့ ဆို၏ – “အသျှင်တို့ ယခု သင်တို့ စိတ်ကျေနပ်ကြလော့”ဟု။",
})


# ---- taṇhāvicarita
TVX = new("Taṇhāvicarita phrases (new)", {
    "asmi": VIEW["asmi"], "itthasmi": "ငါ ဤကဲ့သို့ ဖြစ်၏", "evasmi": "ငါ ထိုနည်းတူ ဖြစ်၏",
    "aññathāsmi": "ငါ အခြားတစ်မျိုး ဖြစ်၏", "bhavissaṃ": VIEW["bhavissaṃ"], "itthaṃ bhavissaṃ": "ငါ ဤကဲ့သို့ ဖြစ်လိမ့်မည်",
    "evaṃ bhavissaṃ": "ငါ ထိုနည်းတူ ဖြစ်လိမ့်မည်", "aññathā bhavissaṃ": "ငါ အခြားတစ်မျိုး ဖြစ်လိမ့်မည်",
    "asasmi": "ငါ အမြဲ ရှိ၏", "sātasmi": "ငါ ပြတ်စဲ၏", "siyaṃ": "ငါ ဖြစ်ရာ၏", "itthaṃ siyaṃ": "ငါ ဤကဲ့သို့ ဖြစ်ရာ၏",
    "evaṃ siyaṃ": "ငါ ထိုနည်းတူ ဖြစ်ရာ၏", "aññathā siyaṃ": "ငါ အခြားတစ်မျိုး ဖြစ်ရာ၏",
    "apāhaṃ siyaṃ": "ငါ ဖြစ်ရလျှင် ကောင်းမည်", "apāhaṃ itthaṃ siyaṃ": "ငါ ဤကဲ့သို့ ဖြစ်ရလျှင် ကောင်းမည်",
    "apāhaṃ evaṃ siyaṃ": "ငါ ထိုနည်းတူ ဖြစ်ရလျှင် ကောင်းမည်", "apāhaṃ aññathā siyaṃ": "ငါ အခြားတစ်မျိုး ဖြစ်ရလျှင် ကောင်းမည်",
})
PERSON = new("Persons (taṇhāvicarita; new)", {
    "khattiyo": "မင်းမျိုး", "brāhmaṇo": "ပုဏ္ဏား", "vesso": "ကုန်သည်မျိုး", "suddo": "သူဆင်းရဲမျိုး",
    "gahaṭṭho": "လူဝတ်ကြောင်", "pabbajito": "ရဟန်း", "devo": "နတ်", "manusso": "လူ", "rūpī": ATTA_X["rūpī"],
    "arūpī": ATTA_X["arūpī"], "saññī": ATTA_X["saññī"], "asaññī": ATTA_X["asaññī"],
    "nevasaññīnāsaññī": ATTA_X["nevasaññīnāsaññī"]})
IMINA = "ဤအရာဖြင့် "


def tv_key(x):
    """«asmīti» / «bhavissanti» / «apāhaṃ itthaṃ siyanti» -> TVX key."""
    x = re.sub(r"(?:ī|i)ti$", "i", x)
    x = re.sub(r"nti$", "ṃ", x)
    if x not in TVX:
        raise Miss("taṇhāvicarita: " + x)
    return x


def tv(x, imina):
    s = TVX[tv_key(x)]
    return (s.replace("ငါ ", "ငါ " + IMINA, 1) if imina else s)


def tv_item(t):
    """One «… vā» item of the taṇhāvicarita lists."""
    m = re.fullmatch(r"(?P<i>[Ii]minā )?(?P<a>[Aa]pāhaṃ )?(?P<p>\S+?)(?P<v>smīti| bhavissanti| siyanti) vā", t)
    if m and m["p"] in PERSON:
        return _tv_my(m["p"], m["v"].strip(), bool(m["i"]), bool(m["a"]), None) + VA
    m = re.fullmatch(r"(?:Parapuggalaṃ(?: (?P<var>\[[^\]]+\]))? upanidhāya )?yathā so (?P<p1>\S+) (?P<i>iminā )?"
                     r"(?P<mode>tathāhaṃ|nāhaṃ tathā|apāhaṃ tathā|apāhaṃ na tathā) (?P<p>\S+?)"
                     r"(?P<v>smīti| bhavissanti| siyanti) vā", t)
    if m and m["p"] in PERSON and m["p1"] == m["p"]:
        pre = ""
        if t.startswith("Parapuggalaṃ"):
            pre = "သူတစ်ပါးကို " + (var(m["var"]) + " " if m["var"] else "") + "နှိုင်းယှဉ်၍ "
        return (pre + f"ထိုသူ {PERSON[m['p']]} ဖြစ်သကဲ့သို့ " + _tv_my(m["p"], m["v"].strip(), bool(m["i"]),
                                                                      "apāhaṃ" in m["mode"], m["mode"]) + VA)
    raise Miss("taṇhāvicarita item: " + t)


def _tv_my(p, v, imina, apa, mode):
    P = PERSON[p]
    neg = mode in ("nāhaṃ tathā", "apāhaṃ na tathā")
    I = IMINA if imina else ""
    same = "ထိုနည်းတူ " if mode else ""
    lad = "လည်း" if mode in ("tathāhaṃ", "apāhaṃ tathā") else ""
    if v == "smīti":
        verb = "မဟုတ်" if neg else "ဖြစ်၏"
    elif v == "bhavissanti":
        verb = "ဖြစ်လိမ့်မည် မဟုတ်" if neg else "ဖြစ်လိမ့်မည်"
    elif apa:
        verb = "မဖြစ်ရလျှင် ကောင်းမည်" if neg else "ဖြစ်ရလျှင် ကောင်းမည်"
    else:
        verb = "မဖြစ်ရာ" if neg else "ဖြစ်ရာ၏"
    return f"{I}ငါ{lad} {same}{P} {verb}ဟု"


@rx(r"(?P<i>[Ii]minā )?(?P<x>(?:apāhaṃ )?(?:itthaṃ |evaṃ |aññathā )?(?:asmīti|itthasmīti|evasmīti|aññathāsmīti|"
    r"bhavissanti|asasmīti|sātasmīti|siyanti)) hoti")
def _r26(m):
    return tv(m["x"], bool(m["i"])) + "ဟု ဖြစ်သည်"


@rx(r"evaṃ (?P<i>iminā )?(?P<x>(?:apāhaṃ )?(?:itthaṃ |evaṃ |aññathā )?(?:asmīti|itthasmīti|evasmīti|aññathāsmīti|"
    r"bhavissanti|asasmīti|sātasmīti|siyanti)) hoti")
def _r27(m):
    return "ဤသို့ " + tv(m["x"], bool(m["i"])) + "ဟု ဖြစ်သည်"


@rx(r"(?P<i>[Ii]minā )?(?P<x>(?:apāhaṃ )?(?:itthaṃ |evaṃ |aññathā )?(?:asmīti|itthasmīti|evasmīti|aññathāsmīti|"
    r"bhavissanti|siyanti)) vā")
def _r28(m):
    return tv(m["x"], bool(m["i"])) + "ဟု" + VA


@rx(r".+? vā")
def _r29(m):
    return tv_item(m[0])


@rx(r"Kañci dhammaṃ (?P<an>an)?avakāriṃ(?: (?P<v>\[[^\]]+\]))? karitvā rūpaṃ(?P<pe>…pe…|…) vedanaṃ… saññaṃ… "
    r"saṅkhāre… viññāṇaṃ (?P<r>.+)")
def _r30(m):
    head = ("တစ်စုံတစ်ခုသော သဘောတရားကို " + ("မခွဲခြားဘဲ" if m["an"] else "ခွဲခြား၍")
            + (" " + var(m["v"]) if m["v"] else "") + " ပြု၍ ရုပ်… ခံစားမှု… မှတ်သိမှု… ပြုပြင်ဖန်တီးမှုများ… သိစိတ်ကို ")
    r = m["r"]
    mm = re.fullmatch(r"(?P<i>iminā )?(?P<x>.+?) chandaṃ paṭilabhati, (?:iminā )?(?P=x) mānaṃ paṭilabhati, "
                      r"(?:iminā )?(?P=x) diṭṭhiṃ paṭilabhati", r)
    if mm:
        x = tv(mm["x"], bool(mm["i"]))
        return head + f"{x}ဟု ဆန္ဒကို ရ၏၊ {x}ဟု မာနကို ရ၏၊ {x}ဟု အယူကို ရ၏"
    mm = re.fullmatch(r"(?P<i>iminā )?niccosmi dhuvosmi sassatosmi avipariṇāmadhammosmīti – evaṃ (?:iminā )?asasmīti "
                      r"hoti", r)
    if mm:
        I = IMINA if mm["i"] else ""
        return head + (f"{I}ငါ မြဲ၏၊ ငါ ခိုင်မြဲ၏၊ ငါ ထာဝရ တည်၏၊ ငါ ဖောက်ပြန်ခြင်း မရှိသော သဘော ရှိ၏ဟု – ဤသို့ "
                       + tv("asasmīti", bool(mm["i"])) + "ဟု ဖြစ်သည်")
    mm = re.fullmatch(r"(?P<i>iminā )?ucchijjissāmi vinassissāmi na bhavissāmīti – evaṃ (?:iminā )?sātasmīti hoti", r)
    if mm:
        I = IMINA if mm["i"] else ""
        return head + (f"{I}ငါ ပြတ်စဲလိမ့်မည်၊ ငါ ပျက်စီးလိမ့်မည်၊ ငါ ဖြစ်လိမ့်မည် မဟုတ်ဟု – ဤသို့ "
                       + tv("sātasmīti", bool(mm["i"])) + "ဟု ဖြစ်သည်")
    raise Miss("kañci: " + r)


ph("Clauses", {"Tasmiṃ sati imāni papañcitāni honti": f"ထိုသို့ ရှိသော် ဤ{GROUP['papañcitāni']}တို့ ဖြစ်ကြ၏"})


@rx(r"Kathañca (?P<i>iminā )?(?P<x>.+) hoti\?")
def _r31(m):
    return tv(m["x"], bool(m["i"])) + "ဟု အဘယ်သို့ ဖြစ်သနည်း"


@rx(r"(?P<i>[Ii]minā )?(?P<x>(?:apāhaṃ )?(?:itthaṃ |evaṃ |aññathā )?(?:asmīti|itthasmīti|evasmīti|aññathāsmīti|"
    r"bhavissanti|siyanti)) vā (?P<j>iminā )?(?P<y>(?:apāhaṃ )?(?:itthaṃ |evaṃ |aññathā )?(?:asmīti|itthasmīti|"
    r"evasmīti|aññathāsmīti|bhavissanti|siyanti)) vā (?P<k>iminā )?(?P<z>(?:apāhaṃ )?(?:itthaṃ |evaṃ |aññathā )?"
    r"(?:asmīti|itthasmīti|evasmīti|aññathāsmīti|bhavissanti|siyanti)) vā")
def _r32(m):
    return f"{C} ".join(tv(m[x], bool(m[i])) + "ဟု" + VA for x, i in (("x", "i"), ("y", "j"), ("z", "k")))


# ===================================================================================== lines, main
HEAD_RE = re.compile(r"(?P<h>#+) (?P<t>.+?)$")
STATE = {}


def translate_line(line):
    if not line.strip():
        return ""
    m = ID.search(line)
    body = line[:m.start()] if m else line
    bid = (" " + m.group(1)) if m else ""
    h = HEAD_RE.fullmatch(body)
    if h:
        if h["t"] == "Ekakaniddeso":
            STATE["matika"] = False
        if h["t"] == "Ekakamātikā":
            STATE["matika"] = True
        return heading(h["h"], h["t"]) + bid
    if STATE.get("matika") and re.match(r"\(\d+\)", body):
        return matika(body) + bid
    return tr_body(body) + bid


def main():
    name_ = NAME_OUT
    lines = (PALI / name_).read_text(encoding="utf-8-sig").splitlines()
    done = []
    STATE.clear()
    for i, line in enumerate(lines):
        try:
            done.append(translate_line(line))
        except Miss as e:
            part = HERE / "scratch" / ("partial-" + name_)
            part.write_text("\n".join(done) + "\n", encoding="utf-8")
            print(f"STOP line {i + 1}: {e}\n  {line[:200]}")
            sys.exit(1)
    txt = unicodedata.normalize("NFC", "\n".join(done).rstrip("\n") + "\n")
    (OUT / name_).write_text(txt, encoding="utf-8")
    print(f"wrote {name_}: {sum(1 for l in txt.splitlines() if l)} lines; pi-1 sentences reused {REUSE['p1']}, "
          f"pi-2 sentences reused {REUSE['p2']}")
    if "--notes" in sys.argv:
        for sec, d in NEW.items():
            print(f"\n### {sec}")
            for k, v in d.items():
                print(f"{k} = {v}")
        print("\n### Slips")
        for x in dict.fromkeys(SLIPS):
            print("- " + x)


if __name__ == "__main__":
    main()
