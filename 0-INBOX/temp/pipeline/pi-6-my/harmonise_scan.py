"""Consistency pass (pi-6 Burmese, Yamaka «အတွဲလိုက် မေးဖြေခြင်း»): every item of harmonise-todo.md, before vs now.
For each item the lines whose Pāli matches `pali` are taken (an item is counted only where the Pāli line has it); in
their Burmese the uses of the chosen form and of every other form are counted, in the chapter files before the pass
(harmonise-backup/chapters/) and now. An item fails if an other form is left now, or if a line that has the Pāli item
lacks the chosen form now. Three book-wide tests are run as functions: B1 the leads (identical Pāli lead = identical
Burmese lead), B5 the plural «ကြ», B12 the headings / colophons (identical Pāli = identical Burmese).
Model: pi-5-my/harmonise_scan.py (read only).
usage: python3 -I -X utf8 harmonise_scan.py [--table]   (--table also writes harmonise-table.tsv:
       Pāli<TAB>chosen Burmese<TAB>other forms (uses before)<TAB>chapters with an other form before)"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"
NOW = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
BEFORE = HERE / "harmonise-backup/chapters"
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
NOT_SO = r"(?<!ပြို)"

# (item, Pāli label for the table, Pāli regex on the line, chosen Burmese (regex), [other forms (regex)], kind)
# kind: A = source as written, B = term / frame drift, R = rule kept (verified, nothing to change)
ITEMS = [
    # ---- Part A
    ("A1 abhisametāvī / anabhisametāvī (no added «သစ္စာကို»)", "abhisametāvīnaṃ / anabhisametāvīnaṃ",
     r"abhisametāv", r"ထင်ထင်ရှားရှား (?:မ)?သိမြင်", [r"သစ္စာကို ထင်ထင်ရှားရှား"], "A"),
    ("A2 anaññātaññassāmīti (bare word; no quote marks: pi-1 / pi-2 name without «စွမ်းရည်» + «အရာ»)",
     "anaññātaññassāmīti", r"[Aa]naññātaññ[aā]ssāmīti(?!ndriy)", r"မသိရသေးသည်ကို သိရတော့မည်ဟူသော အရာ",
     [r"“မသိရသေးသည်ကို သိရတော့မည်”"], "A"),
    ("A2 the sota pun keeps its quote marks (the word cited as a word; B7)", "Dibbasotaṃ taṇhāsotaṃ … sotaṃ",
     r"Dibbasotaṃ taṇhāsotaṃ", r"“သောတ” \(နား သို့မဟုတ် ရေစီး\)", [], "R"),
    ("A2 colophons: the title in quotes (style rule «mid-sentence, put the title in quotes»)", "X niṭṭhito / niṭṭhitaṃ",
     r"niṭṭhit[oaā]\.", r"” (?:ကျမ်း )?ပြီးဆုံးပြီ။", [], "R"),
    ("A3 ^6-10-398 «purisānaṃ uppajjantānaṃ» read as upapajjantānaṃ (one slip rule: ch3, ch9-10a, ch10b)",
     "Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ", r"purisānaṃ uppajjantānaṃ",
     r"ပြန်လည် ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသော ယောက်ျား", [r"(?<!ပြန်လည် )ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသော ယောက်ျား"], "A"),
    ("A3 plural verb after a singular subject, as written («ကြ»; 10-13 ^6-10-454 / ^6-10-468)",
     "Aggamaggasamaṅgī … sacchikarissanti / anāgāmimaggasamaṅgi … bhāvessanti",
     r"Aggamaggasamaṅgī aññātāvindriyaṃ sacchikarissanti|anāgāmimaggasamaṅgi aññindriyañca bhāvessanti",
     r"(?:မျက်မှောက်ပြု|ပွားများ)ကြလိမ့်မည်", [r"ပြည့်စုံသူသည် [^။]*?(?:မျက်မှောက်ပြု|ပွားများ)လိမ့်မည်"], "A"),
    ("A4 ^6-3-1 list (no «,» after sotāyatanaṃ: no «၊»)", "… sotāyatanaṃ ghānāyatanaṃ …",
     r"sotāyatanaṃ ghānāyatanaṃ", r"နား အာရုံခံ နယ်ပယ် နှာခေါင်း", [r"နား အာရုံခံ နယ်ပယ်၊ နှာခေါင်း"], "A"),
    ("A4 ^6-5-1 list (no «,» after samudayasaccaṃ: no «၊»)", "… samudayasaccaṃ nirodhasaccaṃ …",
     r"samudayasaccaṃ nirodhasaccaṃ", r"ဖြစ်ပေါ်ခြင်း သစ္စာ ချုပ်ငြိမ်းခြင်း", [r"ဖြစ်ပေါ်ခြင်း သစ္စာ၊ ချုပ်ငြိမ်းခြင်း"], "A"),
    ("A4 a statement «… V no ca …» without the Pāli «,» (no «၊» before «သို့သော်»; ch7a, ch9-10a already)",
     "… na uppajjissati no ca … (^6-10-318, 10-10, 10-13, 8 (14))",
     r"(?:ssati|jjati|anti|ntaṃ|ttha) no ca (?!tassa cittaṃ|taṃ cittaṃ|tassa taṃ)", r"[^၊] သို့သော်", [], "A"),
    ("A4 the (11) questions «yassa … no ca tassa …, tassa …?» keep the frame «…၊» after the yassa clause (the sample's clause break)",
     "yassa cittaṃ uppajjittha no ca tassa cittaṃ uppannaṃ, …?",
     r"(?:jjittha|jjissati) no ca (?:tassa cittaṃ|taṃ cittaṃ|tassa taṃ cittaṃ) (?:na )?uppannaṃ,",
     r"၊ သို့သော်", [], "R"),
    ("A4 a sentence end without the Pāli «.» (^6-10-393 / ^6-10-452 / ^6-10-468: no «။»; «,» = «၊»)",
     "… na uppajjissati pacchimacittassa … / … pajahissanti, pañca puggalā … / … pajahanti anāgāmi…",
     r"na uppajjissati pacchimacittassa|pajahissanti, pañca puggalā|pajahanti anāgāmimaggasamaṅgi",
     r"(?:ကား မဟုတ် နောက်ဆုံး|မပယ်ကြလိမ့်မည်၊ ပုဂ္ဂိုလ် ငါး|မပယ်ကြ အနာဂါမိ)",
     [r"ကား မဟုတ်။ နောက်ဆုံး", r"လိမ့်မည်။ ပုဂ္ဂိုလ် ငါး", r"မပယ်ကြ။ အနာဂါမိ"], "A"),
    ("A4 7-08 the stray «,» in «kāmadhātuyā tīsu vedanāsu, apariyāpanne» kept as «၊»", "tīsu vedanāsu, apariyāpanne",
     r"tīsu vedanāsu, apariyāpanne", r"သုံးပါး၊ ဘဝဘုံတို့၌", [r"သုံးပါးနှင့် ဘဝဘုံတို့၌"], "A"),
    ("A4 «Āmantā …pe….» = «ဟုတ်ပါသည် …။» (no «။» added before the «…»)", "Āmantā …pe….",
     r"Āmantā …[pP]e…", r"ဟုတ်ပါသည် …", [r"ဟုတ်ပါသည်။ …"], "A"),
    # ---- Part B
    ("B1 moment leads: the ch. 5 style («M၊ …», a final moment + «ထိုသူတို့အား»)", "… uppādakkhaṇe / bhaṅgakkhaṇe tesaṃ",
     r"kkhaṇe|citte vattamāne", r"ခဏ၌|ဖြစ်နေစဉ်",
     [r"ခဏ၌ ရှိသူ", r"ခဏ၌ ရှိသော အခြားသူ", r"ခဏ၌ (?:ကာမဘုံ|သိမ်မွေ့သော|ရုပ်မရှိသော|ဒုတိယ|တတိယ|စတုတ္ထ|ပထမ)"
      r"[^၊။]*?သူတို့(?:အား|၊|နှင့်)", r"ထိုသူတို့ပင်(?:နှင့်|၊)"], "B"),
    ("B2 uppādakkhaṇe «ဖြစ်ခြင်း ခဏ» (pi-5 ^5-366); the vāra headings uppāda «ဖြစ်ပေါ်ခြင်း»", "uppādakkhaṇe",
     r"[Uu]ppādakkhaṇ", r"ဖြစ်ခြင်း ခဏ", [r"ဖြစ်ပေါ်ခြင်း ခဏ"], "R"),
    ("B2 bhaṅgakkhaṇe «ပြိုပျက်ခြင်း ခဏ» (pi-5 ^5-366)", "bhaṅgakkhaṇe", r"[Bb]haṅgakkhaṇ", r"ပြိုပျက်ခြင်း ခဏ",
     [NOT_SO + r"ပျက်ခြင်း ခဏ"], "R"),
    ("B3 tāsaṃ (fem.) «ထိုမိန်းမတို့»", "no ca tāsaṃ", r"^(?!.*no ca tesaṃ).*no ca tāsaṃ", r"သို့သော် ထိုမိန်းမတို့အား",
     [r"သို့သော် ထိုသူတို့အား"], "B"),
    ("B4 «ye ca … tesaṃ cavantānaṃ / upapajjantānaṃ» «…တို့အနက်»", "ye ca … tesaṃ cavantānaṃ",
     r"parinibbāyissanti t[eā]saṃ (?:cavant|upapajjant)", r"တို့အနက်", [r"တို့ထဲမှ"], "B"),
    ("B6 tesaṃyeva + moment «ထိုသူတို့၏ပင် M» (the ch. 5 inner «tesaṃ + moment»)", "tesaṃyeva",
     r"tesaṃyeva", r"ထိုသူတို့၏ပင်", [r"ထိုသူတို့ပင်(?:နှင့်|၊)"], "B"),
    ("B7 sota pun «“သောတ” (နား သို့မဟုတ် ရေစီး)» (one form, 3-01 / 4 / 10-01)", "Dibbasotaṃ taṇhāsotaṃ sotaṃ",
     r"Dibbasotaṃ taṇhāsotaṃ", r"နတ်နားနှင့် တပ်မက်မှု ရေစီးတို့သည်", [], "R"),
    ("B8 kāmāvacara / kāmadhātu (place) «ကာမဘုံ»", "kāmāvacara- / kāmadhātu", r"[Kk]āmāvacar|[Kk]āmadhātu",
     r"ကာမဘုံ", [r"ကာမာဝစရ", r"ကာမလောက"], "R"),
    ("B8 rūpāvacara / rūpadhātu (plane) «သိမ်မွေ့သော ရုပ်ဘုံ»", "rūpāvacara- / rūpadhātuyā (plane)",
     r"(?<![Aa])[Rr]ūpāvacar|(?<![Aa])[Rr]ūpadhātuyā", r"သိမ်မွေ့သော ရုပ်ဘုံ", [r"ရူပ", r"(?<!သိမ်မွေ့သော )ရုပ်ဘုံ"], "R"),
    ("B8 arūpāvacara / arūpa (place) «ရုပ်မရှိသော ဘုံ»", "arūpāvacara- / arūpe / arūpaṃ",
     r"[Aa]rūpāvacar|\b[Aa]rūp(?:e|aṃ|ānaṃ)\b|[Aa]rūpadhātu", r"ရုပ်မရှိသော ဘုံ", [r"အရူပ", r"ရုပ်မဲ့"], "R"),
    ("B9 sa-X-ka / a-X-ka «X ရှိလျက် / X မရှိဘဲ»", "sacakkhukānaṃ / acakkhukānaṃ …",
     r"\b[Ss]a(?:cakkhu|sota|ghāna|rūpa|citta)kānaṃ|\b[Aa](?:cakkhu|sota|ghāna|rūpa|citta)kānaṃ",
     r"ရှိလျက်|မရှိဘဲ", [r"(?:မျက်စိ|နား|နှာခေါင်း|ရုပ်|စိတ်) ရှိသော (?:ပြန်လည်|သူ)"], "R"),
    ("B9 sahetuka / ahetuka (persons) «အမြစ် ရှိလျက် / မရှိဘဲ» (pi-1 Mātikā sense; hetu «အကြောင်း» only in the "
     "hetuvāra list)", "sahetukānaṃ / ahetukānaṃ", r"\b[SsAa]a?hetukānaṃ", r"အမြစ် (?:ရှိလျက်|မရှိဘဲ)",
     [r"အကြောင်း ရှိလျက်", r"အကြောင်း မရှိဘဲ"], "R"),
    ("B9 ñāṇasampayutta / -vippayutta (persons) «ဉာဏ်နှင့် ယှဉ်တွဲလျက် / ကင်းကွာလျက်»",
     "ñāṇasampayuttānaṃ / ñāṇavippayuttānaṃ", r"ñāṇa(?:sam|vip)payuttānaṃ", r"ဉာဏ်နှင့် (?:ယှဉ်တွဲ|ကင်းကွာ)လျက်", [], "R"),
    ("B9 somanassena / upekkhāya «…နှင့်အတူ»", "somanassena / upekkhāya", r"(?<![Vv]inā )\b[Ss]omanassena\b|(?<![Vv]inā )\b[Uu]pekkhāya\b(?! vedanāya)",
     r"(?:ဝမ်းမြောက်မှု|ဥပေက္ခာ)နှင့်အတူ", [r"(?:ဝမ်းမြောက်မှု|ဥပေက္ခာ)ဖြင့်"], "R"),
    ("B9 na itthīnaṃ / na purisānaṃ «မိန်းမ / ယောက်ျား မဟုတ်ဘဲ»", "na itthīnaṃ / na purisānaṃ",
     r"\b[Nn]a (?:itthīnaṃ|purisānaṃ)", r"(?:မိန်းမ|ယောက်ျား) မဟုတ်ဘဲ", [], "R"),
    ("B9 -samaṅgī «…နှင့် ပြည့်စုံသူ»", "-samaṅgī / -samaṅgīnaṃ", r"samaṅg", r"နှင့် ပြည့်စုံသူ", [r"ပိုင်ဆိုင်သူ"], "R"),
    ("B9 nirodhasamāpanna «ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ» (pi-5 ^5-458)", "nirodhasamāpannānaṃ",
     r"nirodhasamāpann", r"ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ", [r"နိရောဓ"], "R"),
    ("B9 Aṭṭhamaka «အဋ္ဌမ ပုဂ္ဂိုလ်» (pi-5 ^5-368); Anāgāmī «အနာဂါမ်» (pi-4)", "Aṭṭhamako / Anāgāmī",
     r"[Aa]ṭṭhamak|[Aa]nāgām(?:ī|i)\b", r"အဋ္ဌမ ပုဂ္ဂိုလ်|အနာဂါမ်", [], "R"),
    ("B10 «yassa cittassa anantarā»: persons «မိမိ စိတ်၏» (citta subject) / «အကြင်စိတ်၏ …» (persons subject) / "
     "correlative «အကြင်စိတ်၏ …၊ ထိုစိတ်၏ …» (the split follows the Pāli syntax)", "yassa cittassa anantarā",
     r"[Yy]assa cittassa anantarā", r"(?:မိမိ |အကြင်)စိတ်၏ ချက်ချင်း နောက်၌", [], "R"),
    ("B12 mahāvāra «ဖော်ပြချက်ကြီး»", "Mahāvāro", r"Mahāvāro", r"ဖော်ပြချက်ကြီး", [], "R"),
    ("B12 paṭiloma = paccanīka «အငြင်းပြ ပုံစံ»", "paṭiloma- / paccanīka-", r"paṭilom|paccanīk", r"အငြင်းပြ ပုံစံ",
     [r"ပြောင်းပြန်"], "R"),
    ("B13 parijānāti «ပိုင်းခြား သိ» (negative «ပိုင်းခြား မသိ»)", "parijānāti", r"parijān", r"ပိုင်းခြား (?:မ)?သိ",
     [r"မပိုင်းခြား", r"ပိုင်းခြား၍ သိ"], "R"),
    ("B13 bhāveti «ပွားများ» (negative «မပွားများ»)", "bhāveti", r"\b(?:na )?bhāv(?:eti|enti|essati|essanti|ittha)",
     r"ပွားများ", [r"ပွါး"], "R"),
    ("B13 sacchikaroti «မျက်မှောက်ပြု» (negative «မျက်မှောက် မပြု», pi-4 ^4-17)", "sacchikaroti", r"sacchikar|sacchākāsi",
     r"မျက်မှောက်(?: မ)?ပြု", [r"မမျက်မှောက်"], "R"),
    ("B15 yassaka / yatthaka / yassayatthaka «“…” အပိုင်း»", "yassakaṃ / yatthakaṃ / yassayatthakaṃ",
     r"[Yy]assak|[Yy]atthak|[Yy]assayatthak", r"” အပိုင်း", [r"” မေးခွန်း"], "B"),
    ("B15 sadisaṃ (note) «တူညီ»", "sadisaṃ / sadisā", r"[Ss]adis", r"တူညီ", [r"တူသည်"], "B"),
    ("B15 vibhajitabbaṃ «ခွဲခြား ပြရမည်», vibhatta «ခွဲခြား ပြထားသကဲ့သို့»", "vibhajitabbaṃ / vibhattaṃ",
     r"vibhajitabb|vibhatt", r"ခွဲခြား ပြ", [r"ခွဲခြား ဖော်ပြ"], "B"),
    ("B15 pucchā «အမေး» (pi-5 ^5-652)", "pucchā", r"pucchā", r"အမေး", [r"မေးခွန်း"], "B"),
    ("B15 saṃkhittaṃ (note) «အကျဉ်းချုပ်» (= pi-5 «(Saṃkhittaṃ).»)", "(saṃkhittaṃ)", r"[Ss]aṃkhittaṃ(?=[ ,)])(?! cittaṃ)",
     r"အကျဉ်းချုပ်", [r"အကျဉ်း ဖော်ပြထားသည်(?! \[ပါဌ်ကွဲ \(Syā\.\): uparivāre)"], "B"),
    ("B15 a question cut before its verb «…pe…?» = «…လော။»", "(Kha) yassa vā pana (yattha)…pe…?",
     r"…[pP]e…\?", r"…လော။", [r"(?:အား|၌|မှု)…။"], "B"),
    ("B16 vitthāretabbaṃ «အကျယ် ချဲ့ရမည်» (pi-5 ^5-839)", "vitthāretabbaṃ", r"[Vv]itthāre(?:tabb|tabbā)",
     r"အကျယ် ချဲ့", [r"အကျယ် ဖော်ပြရမည်"], "B"),
    ("B17 cavati / cuta «စုတေ» (sample; pi-5 ^5-65 «သေ၍» binds only an identical sentence: none)", "cavantānaṃ / cutassa",
     r"\bcavant|\bcutassa", r"စုတေ", [r"(?<!စု)တေ(?!ဆဲ)(?=သူ)", r" သေ၍", r" သေဆဲ"], "R"),
    ("B18 Uppajjanavāro = Uppādavāro «ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်» (never both in one chapter)", "Uppajjanavāro",
     r"Uppajjanavāro", r"ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်", [], "R"),
]

# ---- book-wide function tests
PL_END = re.compile(r"(?:nti|ntī|issanti|essanti)(?:ti)?$")
SG_END = re.compile(r"(?:ati|eti|oti|āti|atī|etī|otī|ātī|issati|essati|issatī|essatī|āsi)(?:ti)?$")
IT_END = re.compile(r"(?:ittha|itthā)(?:ti)?$")
VROOT = re.compile(r"^(?:na|n|nap)?(?:uppajj|nirujjh|anus|ānus|pajah|ppajah|pajjah|parijān|bhāv|bhav|sacchikar|"
                   r"sacchāk|upapajj)\w*$")
NONFIN = re.compile(r"(?:ant[āī]naṃ|antassa|anto|amāna\w*|itvā|anaṃ|issantīnaṃ)$|^(?:upapajjamāno|bhāvanā\w*|"
                    r"parinibbāyissanti|paṭilabh\w*)$")
NOMINAL = re.compile(r"(?:ဖြစ်|ရှိ|မဟုတ်|ပြိုပျက်)ကြ")
KO = re.compile(r"ကြ(?![ါ-ှ]|[က-အ]်)")


def psplit(l):
    l = re.sub(r"\[[^\]]*\]", "", ID.sub("", l))
    return [s for s in re.split(r"(?<=[.?]) (?=\S)", l) if s]


def bsplit(l):
    l = re.sub(r"\[[^\]]*\]", "", ID.sub("", l))
    return [s for s in re.split(r"(?<=။) ", l) if s]


def plural_test(md):
    """B5: per aligned sentence, n_pl Pāli plural finite verbs (-nti / -issanti), n_it number-neutral -ittha;
    Burmese verbal «ကြ» (nominal «ဖြစ်ကြ / ရှိကြ / မဟုတ်ကြ / ပြိုပျက်ကြ» not counted) must be n_pl … n_pl + n_it.
    Relative-clause verbs («ye … paṭilabhissanti / parinibbāyissanti») are not finite here."""
    bad, n = [], 0
    for p in sorted(PD.glob("*.md")):
        a = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [l for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for i, (x, y) in enumerate(zip(a, b), 1):
            if x.startswith("#"):
                continue
            ps, bs = psplit(x), bsplit(y)
            if len(ps) != len(bs):
                continue
            for s, t in zip(ps, bs):
                toks = [w.strip(",.?;()…") for w in re.sub(r"…[pP]e…", " ", s).split()]
                npl = nit = 0
                for w in toks:
                    w = w.lower()
                    if not VROOT.match(w) or NONFIN.search(w):
                        continue
                    if PL_END.search(w):
                        npl += 1
                    elif IT_END.search(w):
                        nit += 1
                if not npl and not nit:
                    continue
                if re.search(r"\bye\b|\byā\b|yāni", s) and re.search(r"(?:uppajjanti|paṭilabhissanti)\b", s) \
                        and t.count("သော") and "ကြသော" in t:
                    continue                    # the sample's ch. 1 relative «Mūlāni yāni ekato uppajjanti …»
                n += 1
                nk = len(KO.findall(t)) - len(NOMINAL.findall(t))
                if not (npl <= nk <= npl + nit):
                    bad.append(f"{p.name[:-3]}:{i} pl {npl} ittha {nit} «ကြ» {nk}: {s[:90]}")
    return n, bad


def lead_test(md):
    """B1: every answer lead (the Pāli before tesaṃ / tāsaṃ, not a relative) has one Burmese lead (up to «အား»)."""
    lead = re.compile(r"^(?:\(\w+\) )?(?P<who>.+?) (?P<pro>tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ)(?= )"
                      r"(?! (?:\w+ant[āī]naṃ|cittassa|(?:\S+ )?\S+kkhaṇe|tattha \w+ant[āī]naṃ)\b)")
    D = collections.defaultdict(collections.Counter)
    for p in sorted(PD.glob("*.md")):
        a = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [l for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for x, y in zip(a, b):
            ps, bs = psplit(x), bsplit(y)
            if len(ps) != len(bs):
                continue
            for s, t in zip(ps, bs):
                m = lead.match(s)
                if not m or re.match(r"(?i)(yassa|yattha|yo|ya[mṃ]|yā)\b", m["who"]):
                    continue
                k = re.search("အား(?!လုံး)", t)
                if k:
                    D[(m["who"][0].lower() + m["who"][1:], m["pro"])][t[:k.end()]] += 1
    bad = [f"{w} | {pr}: {dict(c)}" for (w, pr), c in D.items() if len(c) > 1]
    return len(D), bad


def heading_test(md):
    """B12: headings and colophon / heading-like lines: identical Pāli = identical Burmese."""
    D = collections.defaultdict(set)
    for p in sorted(PD.glob("*.md")):
        a = [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [ID.sub("", l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for x, y in zip(a, b):
            if x.startswith("#") or re.search(r"(?:vāro|vāre \w+|niṭṭhito|niṭṭhitaṃ|niṭṭhitā|anulomaṃ|paṭilomaṃ)\.$", x):
                D[re.sub(r"^#+ ", "", x)].add(re.sub(r"^#+ ", "", y))
    bad = [f"{k}: {sorted(v)}" for k, v in D.items() if len(v) > 1]
    both = []
    for p in sorted(PD.glob("*.md")):
        t = p.read_text(encoding="utf-8-sig")
        if "Uppajjanavāro" in t and "Uppādavāro" in t:
            both.append(p.name)
    return len(D), bad + [f"Uppajjanavāro and Uppādavāro both in {n}" for n in both]


def pairs(md):
    for p in sorted(PD.glob("*.md")):
        ch = p.name[:-3].rsplit("-", 1)[0] if p.name[0].isdigit() else p.name[:-3]
        a = [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [ID.sub("", l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for x, y in zip(a, b):
            yield ch, re.sub(r"\[[^\]]*\]", "", x), y          # an item counts in the Pāli text, not in a variant


def count(md, pali, chosen, others):
    nl = nc = miss = 0
    no = [0] * len(others)
    chs = [set() for _ in others]
    for ch, x, y in pairs(md):
        if not re.search(pali, x):
            continue
        nl += 1
        c = len(re.findall(chosen, y))
        nc += c
        miss += c == 0
        for i, o in enumerate(others):
            k = len(re.findall(o, y))
            no[i] += k
            if k:
                chs[i].add(ch)
    return nl, nc, miss, no, chs


def main(argv):
    rows, fails = [], 0
    for item, label, pali, chosen, others, kind in ITEMS:
        nl, nc0, _, no0, ch0 = count(BEFORE, pali, chosen, others)
        nl1, nc1, miss1, no1, _ = count(NOW, pali, chosen, others)
        left = sum(no1)
        bad = left or not nl1 or miss1
        fails += bool(bad)
        chs = sorted(set().union(*ch0)) if others else []
        print(f"{'FAIL' if bad else 'OK  '} {item}: {nl1} lines; chosen {nc0} -> {nc1}"
              + (f"; other forms {sum(no0)} -> {left}" if others else "")
              + (f"; {miss1} lines without it" if miss1 else ""))
        rows.append((label, chosen.replace("\\", ""), "; ".join(f"{o.replace(chr(92), '')} ({n})" for o, n in zip(others, no0) if n)
                     or "-", ", ".join(chs) or "-"))
    for name, fn, label, chosen in (
            ("B1 leads: identical Pāli lead = identical Burmese lead", lead_test, "(every answer lead)", "one Burmese each"),
            ("B5 plural «ကြ» = the Pāli verb's number (-ittha: the subject's)", plural_test, "(every finite verb)",
             "«ကြ» with -nti / -issanti (-ittha with a plural subject), never with -ti / -issati"),
            ("B12 headings / colophons: identical Pāli = identical Burmese", heading_test, "(every heading)",
             "one Burmese each")):
        n0, b0 = fn(BEFORE)
        n1, b1 = fn(NOW)
        fails += bool(b1)
        print(f"{'FAIL' if b1 else 'OK  '} {name}: {n1} units; differing {len(b0)} -> {len(b1)}")
        for b in b1[:12]:
            print("      ", b[:220])
        rows.append((label, chosen, f"differing before: {len(b0)}", "-"))
    if "--table" in argv:
        with open(HERE / "harmonise-table.tsv", "w", encoding="utf-8") as fh:
            fh.write("Pāli\tchosen Burmese\tother forms (uses before the pass)\tchapters\n")
            for r in rows:
                fh.write("\t".join(r) + "\n")
    print(f"{len(ITEMS) + 3 - fails} / {len(ITEMS) + 3} items OK")
    return fails


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
