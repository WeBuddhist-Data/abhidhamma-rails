"""Per-line scan of the rails families (stricter than the per-segment adherence check; model pi-4-my/rails/line_scan.py):
a Burmese line whose Pāli line holds the family's Pāli form must not keep the zero-shot form the family replaces
(forbid), and must hold the termbase form (req) where the family states one. A family may name a Pāli «unless» regex:
lines matching it are not scanned for it. Variant readings in square brackets stay Pāli and are not counted.
usage: line_scan.py <pali dir> <burmese dir> [--stats]   (one line per failure; nothing = clean; --stats: Pāli hits)"""
import pathlib
import re
import sys
import unicodedata

pd, md = map(pathlib.Path, sys.argv[1:3])
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
FAM = [  # (family, Pāli regex, Burmese regex, mode, Pāli «unless» regex or None)
    ("L02 upacchedo = ပြတ်စဲခြင်း", r"upacchedo", r"ပြတ်စဲခြင်း", "req", None),
    ("L02 upacchedo (old «ပြတ်ခြင်း» / «ဖြတ်တောက်ခြင်း»)", r"upacchedo", r"(?<!စဲ)ပြတ်ခြင်း|ဖြတ်တောက်ခြင်း", "forbid", None),
    ("L03 upasampajja viharati (old «ပြည့်စုံစွာ ဝင်ရောက်၍» / «ပြည့်စုံစေလျက်»)", r"upasampajja viharati",
     r"ပြည့်စုံစွာ ဝင်ရောက်၍|ပြည့်စုံစေလျက်", "forbid", None),
    ("L04 issariya (old «မိမိ၏ အစွမ်း»)", r"(?i)issariyakāmakārik", r"မိမိ၏ အစွမ်း", "forbid", None),
    ("L04 issariya = အစိုးရခြင်း", r"(?i)issariyakāmakārik", r"အစိုးရခြင်း", "req", None),
    ("L05 vigataṃ (old «ကင်းကွာ»)", r"(?<![a-z])vigataṃ", r"ကင်းကွာ", "forbid", None),
    ("L05 atthaṅgataṃ (old «ကွယ်ပြီး»)", r"atthaṅgataṃ", r"(?<![ပျောက်])ကွယ်ပြီး", "forbid", None),
    ("L05 pātubhūtaṃ (old «ထင်ရှား ပေါ်ပေါက်»)", r"pātubhūtaṃ", r"ထင်ရှား (?:မ)?ပေါ်ပေါက်", "forbid", None),
    ("L05 abhinibbattaṃ (old «ဖြစ်မြောက်»)", r"abhinibbattaṃ", r"ဖြစ်မြောက်", "forbid", None),
    ("L06 nirodhasamāpatti (old «ချုပ်ငြိမ်းရာ ဈာန်»)", r"(?i)nirodhasamāpatt|nirodhaṃ samāpann", r"ချုပ်ငြိမ်းရာ ဈာန်",
     "forbid", None),
    ("L06 nirodhasamāpatti = ချုပ်ငြိမ်းခြင်း သမာပတ်", r"(?i)saññāvedayitanirodhasamāpatt", r"ချုပ်ငြိမ်းခြင်း သမာပတ်",
     "req", None),
    ("L10 X-ūpagā sattā (old «သို့ ရောက်သော သတ္တဝါ»)", r"ūpagā sattā", r"သို့ ရောက်သော သတ္တဝါ", "forbid", None),
    ("L11 diṭṭhadhammasukhavihāra (old «ယခုဘဝ»)", r"diṭṭhadhammasukhavihār", r"ယခုဘဝ", "forbid", None),
    ("L11 diṭṭhadhammasukhavihāra = မျက်မှောက်ဘဝ", r"diṭṭhadhammasukhavihār", r"မျက်မှောက်ဘဝ", "req", None),
    ("L13 yaṃ kiñci (old «မှန်သမျှ»)", r"(?i)yaṃ kiñci", r"မှန်သမျှ", "forbid", None),
    ("L14 anuttara (old «အမြတ်ဆုံး»)", r"anuttar", r"အမြတ်ဆုံး", "forbid", r"(?i)agg|seṭṭh|uttamo|sāsana"),
    ("L17 phale ṭhito (old «ဖိုလ်၌ တည်သူ»)", r"phale ṭhit", r"ဖိုလ်၌ တည်(?:သူ|ပြီးသူ)", "forbid", None),
    ("L18 ruhiruppādaka (old «စိမ်းစေ»)", r"ruhiruppād", r"စိမ်းစေ", "forbid", None),
    ("L19 buddhe aveccappasāda = ဘုရားရှင်၌", r"buddhe aveccappasād", r"ဘုရားရှင်၌", "req", None),
    ("L20 saha upapattiyā (old «တစ်ပြိုင်နက်»)", r"(?i)saha upapattiy", r"တစ်ပြိုင်နက်", "forbid", None),
    ("L21 X niruddhe … vattabbo (old «ချုပ်ငြိမ်းသွားသောအခါ»)", r"(?:niruddhe|niruddhāya) .*vattabb",
     r"ချုပ်ငြိမ်းသွားသောအခါ", "forbid", None),
    ("L22 saṇṭhāti (old «တည်» without «နေ»)", r"saṇṭh", r"တည်(?:သည်|၏|သနည်း|သလော)", "forbid", r"tiṭṭhant"),
    ("L24 sukhaṃ anuppadeti / Sukhānuppadāna (old «သုခ»)", r"(?i)sukhaṃ anuppadet|sukhānuppadān", r"သုခ", "forbid", None),
    ("L25 paṭivedha family (old «ထိုးထွင်း သိမြင်»)", r"paṭivedh|paṭivijjh|paṭividdh", r"ထိုးထွင်း သိမြင်", "forbid",
     r"vipassan"),
    ("L26 parinipphanna (old «အမှန်တကယ် ဖြစ်ပေါ်ပြီး» / «ပြည့်စုံစွာ ပြီးမြောက်»)", r"parinipphann",
     r"အမှန်တကယ် ဖြစ်ပေါ်ပြီး|ပြည့်စုံစွာ (?:မ)?ပြီးမြောက်", "forbid", None),
    ("L29 pisuṇa (old «ကုန်းချော»)", r"pisuṇ", r"ကုန်းချော", "forbid", None),
    ("L29 āneñja (old «မတုန်မလှုပ်»)", r"āneñj", r"မတုန်မလှုပ်", "forbid", None),
    ("L30 tiracchānayoni (old «တိရစ္ဆာန် ဘဝ»)", r"tiracchānayoniṃ", r"တိရစ္ဆာန် ဘဝ", "forbid", r"tiracchānayonigām"),
    ("§A17 purisa spelling (old «ယောကျ်ား»)", r"(?i)puris", r"ယောကျ်ား", "forbid", None),
    ("§A29 mātaraṃ jīvitā voropetvā (old «အမိကို သတ်»)", r"mātaraṃ jīvitā vorop", r"အမိကို သတ်", "forbid", None),
    ("§A30 Mahāniyāmo = one item", r"Mahāniyāmo", r"ကြီးမားသော အစု၊ သေချာသော", "forbid", None),
    # ---- bilingual review 2026-11-22 (apply_fixes.py F nn, layer L40 … L51; review/fix-notes.md)
    ("L40 A2 appiyaṃ karitvā = မခွဲခြားဘဲ", r"appiyaṃ karitvā", r"မခွဲခြားဘဲ", "req", None),
    ("L40 A2 appiyaṃ karitvā (old «ဦးစားမပေး»)", r"appiyaṃ karitvā", r"ဦးစားမပေး", "forbid", None),
    ("L40 A3 esese = တစ်ခုတည်း ဖြစ်သော", r"\besese\b", r"တစ်ခုတည်း ဖြစ်သော", "req", None),
    ("F04-F06 A4 / A5 appaṭividdha / abhisambuddha family (old «ထိုးထွင်း»)", r"(?i)appaṭividdh|abhisambuddhān|abhisambujjh",
     r"ထိုးထွင်း", "forbid", None),
    ("F01 B2 Bhaṭo (old «ဝေယျာဝစ္စ»)", r"Bhaṭo", r"ဝေယျာဝစ္စ", "forbid", None),
    ("L41 B4 paṇidahantassa = ဆုတောင်းသူ", r"paṇidahantassa", r"ဆုတောင်းသူ", "req", None),
    ("L41 B4 paṇidahantassa (old «ထားရှိသူ» / «ဦးတည်ထားသူ» / «ဆု မတောင်း»)", r"paṇidahantassa",
     r"ထားရှိသူ|ဦး(?:မ)?တည်ထားသူ|ဆု မတောင်း", "forbid", None),
    ("L51 / R501 / F10 B5 active jīvitā voropeti (old «အသက်မှ ချ»)", r"jīvitā vorope(?:t[iī]|tvā|yya)", r"အသက်မှ ချ(?!ခံ)",
     "forbid", None),
    ("L42 B6 ānantarika (old «အနန္တရိယ»)", r"\bānantari[ky]", r"အနန္တရိယ", "forbid", None),
    ("L43 B7 ariyo aṭṭhaṅgiko maggo (old «… မဂ်၊ အရိယာ မဂ်»)", r"(?i)ariyo aṭṭhaṅgiko maggo", r"မဂ်၊ အရိယာ မဂ်", "forbid", None),
    ("L44 B8 pettivisaya = ပြိတ္တာ ဘုံ", r"(?i)pettivisay", r"ပြိတ္တာ ဘုံ", "req", None),
    ("L45 / F43 B9 yadaniccaṃ taṃ dukkhaṃ = «“မမြဲသော အရာသည် ဒုက္ခ”ဟု»", r"yadaniccaṃ taṃ dukkhaṃ",
     r"“မမြဲသော အရာသည် ဒုက္ခ”ဟု", "req", None),
    ("L45 B9 dukkhaññeva / yadaniccaṃ (old «ဆင်းရဲ ဒုက္ခ» / «ဆင်းရဲ၏»)", r"(?i)dukkhaññeva|yadaniccaṃ taṃ dukkhaṃ",
     r"ဆင်းရဲ ဒုက္ခ|ဆင်းရဲ၏", "forbid", None),
    ("F13 B11 adinnādāna (old «မပေးသည်ကို ကိုင်»)", r"adinnādān", r"မပေးသည်ကို ကိုင်", "forbid", None),
    ("L46 B12 samphaṃ / samphappalāpa = အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", r"samphaṃ palap|samphappalāp",
     r"အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", "req", None),
    ("L47 B13 kusalo sārammaṇo (old «… ဖြစ်သော၊ အာရုံ»)", r"kusal\w* (?:an)?ārammaṇ", r"ဖြစ်သော၊ အာရုံ", "forbid", None),
    ("L48 B15 saḷāyataniko attabhāvo (no «ရရှိခြင်း»)", r"saḷāyataniko attabhāvo", r"ကိုယ်ခန္ဓာ ရရှိခြင်း", "forbid", None),
    ("L49 A16 Handa hi = ကဲ၊", r"\bHanda hi\b", r"ကဲ၊", "req", None),
    ("F45 passive (pitā / arahā) jīvitā voropito = «… အသက်မှ ချခံရ»", r"(?:pitā|arahā) jīvitā voropito", r"အသက်မှ ချခံရ",
     "req", None),
    ("F46 ajjhattiko … kāyo = အတွင်းပိုင်း", r"ajjhattiko ceva", r"အတွင်းပိုင်း", "req", None),
    ("A21 / B20 vagga line or heading without Pāli quotes (no quote marks)", r"vaggo\b|^#+ ", r"[“”‘’]", "forbid",
     r"[\"“”‘’']"),
]
BR = re.compile(r"\[[^\]]*\]")
STATS = {f[0]: 0 for f in FAM}
for p in sorted(pd.glob("*.md")):
    pl = [N(l) for l in p.read_text(encoding="utf-8-sig").splitlines()]
    ml = [N(l) for l in (md / p.name).read_text(encoding="utf-8").splitlines()]
    for k, (a, b) in enumerate(zip(pl, ml), 1):
        a2, b2 = BR.sub("", a), BR.sub("", b)
        for fam, prx, brx, mode, unless in FAM:
            hits = len(re.findall(prx, a2))
            if not hits or (unless and re.search(unless, a2)):
                continue
            STATS[fam] += hits
            found = re.findall(brx, b2)
            if (mode == "forbid" and found) or (mode == "req" and not found):
                print(f"{p.name}:{k}\t{fam}\t{mode}\t{(found or [''])[0]}")
if "--stats" in sys.argv:
    for f, n in STATS.items():
        print(f"stats\t{n}\t{f}")
