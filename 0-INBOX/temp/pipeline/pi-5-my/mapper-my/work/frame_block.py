# ---- FRAME-BEGIN
# The dialectic machinery and the stock frame words of the Kathāvatthu (my5-zeroshot-terms §3-§6), settled on
# 1-puggalakatha. Dictionary forms: pi-1 rules 1-11 (nouns without final particles, attributives «…သော», verbs
# «…သည်», absolutives «…၍»), pi-2 N1-N11, pi-3 M1-M9, pi-4 P1-P8; the NEW pi-5 rules Q1-Q8 (map-table.md).
FRAME = {
    # answers and the eight-fold refutation (anuloma / paṭikamma / niggaha / upanayana / niggamana)
    "Āmantā": "ဟုတ်ပါသည်",                       # Q2: the answer formula «ဟုတ်ပါသည်။» whole
    "Ājānāhi": "လက်ခံသည်",                       # «ချေပချက်ကို လက်ခံလော့» (rule 4)
    "niggahaṃ": "@niggaha", "niggaha": "@niggaha", "niggaho": "@niggaha", "niggahe": "@niggaha",
    "paṭikammaṃ": "ပြန်လှန် ချေပချက်", "paṭikamma": "ပြန်လှန် ချေပချက်", "paṭikamme": "ပြန်လှန် ချေပချက်",
    "upanayana": "ဆက်စပ် အသုံးချချက်", "niggamana": "နိဂုံးချုပ်ချက်", "paṭipādanā": "ဆက်စပ် တင်ပြချက်",
    "anuloma": "အစဉ်အတိုင်း", "anulomaṃ": "အစဉ်အတိုင်း", "paccanīka": "ပြောင်းပြန်", "paccanīkaṃ": "ပြောင်းပြန်",
    "Anulomapaccanīkaṃ": "အစဉ်အတိုင်းနှင့် ပြောင်းပြန်", "Paccanīkānulomaṃ": "ပြောင်းပြန်နှင့် အစဉ်အတိုင်း",
    "paṭijānantaṃ": "ဝန်ခံနေသော", "paṭijānantā": "ဝန်ခံနေသော", "paṭiññāya": "ဝန်ခံချက်", "hetāya": "ထို",
    "niggaṇhāma": "ချေပသည်", "niggaṇhāsi": "ချေပသည်",
    "niggahetabbe": "@niggahetabba", "niggahetabbā": "@niggahetabba",
    "Suniggahito": "ကောင်းစွာ ချေပခြင်း ခံရသော", "Dunniggahitā": "မကောင်းစွာ ချေပခြင်း ခံရသော",
    "dunniggahite": "မကောင်းစွာ ချေပခြင်း", "niggahite": "ချေပခြင်း", "dukkaṭe": "မကောင်းစွာ ပြုခဲ့သော",
    "suniggahitova": "@roman", "hevameva": "@hevameva",
    "tava": "သင်", "ṭīkā": "ဋီကာ", "oloketabbā": "ကြည့်သည်",
    "vata": "@vata", "micchā": "@miccha", "Nanu": "မဟုတ်လော", "Tena hi": "@tenahi", "hevaṃ": "ဤသို့",
    # the speakers' note «[iminā lakkhaṇena sakavādī/paravādīpucchā dassitā]»
    "pucchā": "@puccha", "dassitā": "ပြထားသော", "lakkhaṇena": "အမှတ်အသား", "vādī": "@vadi",
    # the proposition of the Puggalakathā (§4, §7)
    "upalabbhati": "တွေ့ရသည်", "upalabbhanti": "တွေ့ရသည်", "nupalabbhati": "မတွေ့ရ", "nupalabbhanti": "မတွေ့ရ",
    "saccikaṭṭhaparamatthena": "အမှန်တကယ် အဆုံးစွန် အနက်",      # rule 1: the instrumental «အားဖြင့်» goes
    "paramatthena": "အဆုံးစွန် အနက်", "atthena": "@atthena", "parama": "@parama",
    "paramattho": "အဆုံးစွန် အရာ", "saccikaṭṭho": "@saccikattho", "saccikaṭṭha": "@saccikattho",
    "aṭṭho": "အရာ", "aṭṭha": "@attha_thing", "suddha": "@suddha", "okāsa": "နေရာ", "avayava": "အစိတ်အပိုင်း",
    "Sabbattha": "နေရာတိုင်း", "Sabbadā": "အချိန်တိုင်း", "Sabbesu": "@sabbesu",
    # sets and ordinals (§5)
    "Pañcamo": "ပဉ္စမ", "Chaṭṭho": "ဆဋ္ဌမ", "Sattamo": "သတ္တမ", "aṭṭhaka": "ရှစ်ပါးအစု",
    "Saṃkhittaṃ": "အကျဉ်းချုပ်",
    # quotations and reasons (§3)
    "bhagavatā": "မြတ်စွာဘုရား", "suttanto": "သုတ္တန်", "Vuttaṃ": "ဟောတော်မူသည်", "vuttaṃ": "ဟောတော်မူသည်",
    "Vuttaṃ bhagavatā": "မြတ်စွာဘုရား … ဟောတော်မူသည်", "bhikkhave": "ရဟန်း", "bhante": "အသျှင်ဘုရား",
    "kāraṇena": "အကြောင်း", "katvā": "@katva", "eva": "@eva",
    # headings and colophons (§2)
    "kathā": "@katha", "anuyogo": "စစ်ဆေးမေးမြန်းခြင်း", "anuyoga": "စစ်ဆေးမေးမြန်းခြင်း", "vaggo": "ဝဂ်",
    "niṭṭhitā": "ပြီးဆုံးသော", "saṃsandanaṃ": "နှိုင်းယှဉ်ခြင်း", "saṃsandanā": "နှိုင်းယှဉ်ခြင်း",
    "suddhika": "ရိုးရိုး", "opamma": "ဥပမာ", "catukka": "လေးပါး", "naya": "@naya", "sodhanaṃ": "စိစစ်ခြင်း",
    # pronouns of the frames
    "koci": "@koci", "Yo": "@yo", "yo": "@yo", "yaṃ": "@yam", "yena": "@yena", "Aññaṃ": "@anna", "aññaṃ": "@anna",
    "añño": "@anna", "Añño": "@anna", "aññā": "@anna_f", "Aññā": "@anna_f", "Aññe": "@anna", "aññe": "@anna",
    "Aññāni": "@anna",
    "hoti": "@hoti", "atthi": "ရှိသည်", "Atthi": "ရှိသည်", "bhavati": "ဖြစ်သည်",
}
# Core terms of the book that recur in every kathā (my5-zeroshot-terms §7-§8), settled on 1-puggalakatha.
STOCK = {
    "puggala": "ပုဂ္ဂိုလ်", "puggalo": "ပုဂ္ဂိုလ်", "Puggalo": "ပုဂ္ဂိုလ်", "puggalassa": "ပုဂ္ဂိုလ်",
    "puggalā": "ပုဂ္ဂိုလ်", "puggalaṃ": "ပုဂ္ဂိုလ်", "puggalānaṃ": "ပုဂ္ဂိုလ်",
    "paññatti": "သတ်မှတ်ချက်", "paññatta": "သတ်မှတ်ချက်", "upādāya": "မှီ၍", "upādā": "@upada", "nissāya": "မှီ၍",
    "sandhāvati": "ကူးသွားသည်", "sandhāvanti": "ကူးသွားသည်", "upapajjati": "ပြန်လည် ဖြစ်ပေါ်သည်",
    "paññāyati": "ထင်ရှားသည်", "cavati": "@cavati", "cuto": "သေသော",
    "kattā": "ပြုလုပ်သူ", "kāretā": "ပြုလုပ်စေသူ", "kattā kāretā": "ပြုလုပ်သူ … ပြုလုပ်စေသူ",
    "paṭisaṃvedī": "ခံစားသူ", "vipākapaṭisaṃvedī": "အကျိုးကို ခံစားသူ", "kārako": "ပြုသူ",
    "Kammakārako": "ကံကို ပြုသူ", "kammakārako": "ကံကို ပြုသူ",
    "paṭisaṃvedeti": "ခံစားသည်", "paṭisaṃvedenti": "ခံစားသည်", "karoti": "@karoti", "karonti": "@karoti",
    "sukhadukkhaṃ": "ချမ်းသာနှင့် ဆင်းရဲ", "kalyāṇa": "ကောင်းမွန်သော", "pāpakāni": "ယုတ်မာသော",
    "pāpakānaṃ": "ယုတ်မာသော", "Kalyāṇapāpakāni": "ကောင်းမွန်သော … ယုတ်မာသော",
    "Kalyāṇapāpakānaṃ": "ကောင်းမွန်သော … ယုတ်မာသော", "kammāni": "ကံ", "kammānaṃ": "ကံ", "vipāko": "အကျိုး",
    "Vipāko": "အကျိုး",
    "saṅkhato": "ပြုပြင်ဖန်တီးထားသော", "asaṅkhato": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",
    "sappaccayo": "အကြောင်း ရှိသော", "appaccayo": "အကြောင်း မရှိသော", "sassato": "@sassato",
    "nimitto": "အမှတ်အသား ရှိသော", "animitto": "အမှတ်အသား မရှိသော",
    "vijjamāno": "ရှိနေသော", "saṃvijjamāno": "ထင်ရှား ရှိနေသော",
    "khayadhammaṃ": "ကုန်ခန်းတတ်သော သဘော … ရှိသော", "vayadhammaṃ": "ပျက်စီးတတ်သော သဘော … ရှိသော",
    "virāgadhammaṃ": "ပြယ်ပျောက်တတ်သော သဘော … ရှိသော", "nirodhadhammaṃ": "ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော",
    "vipariṇāmadhammaṃ": "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော",
    "virāga": "@viraga",
    "sotāpanno": "သောတာပန်", "sakadāgāmī": "သကဒါဂါမ်", "anāgāmī": "အနာဂါမ်", "arahā": "ရဟန္တာ",
    "manusso": "လူ", "devo": "နတ်", "hutvā": "ဖြစ်၍", "jīvaṃ": "အသက်", "jīvo": "အသက်", "sarīraṃ": "ကိုယ်ခန္ဓာ",
    "rūpaṃ": "@rupam", "Rūpaṃ": "@rupam", "rūpa": "@rupa", "dukkhaṃ": "@dukkha", "Dukkhaṃ": "@dukkha",
    "dukkha": "@dukkha", "sukhaṃ": "@sukha", "sukha": "@sukha", "dhātuyā": "@dhatuya",
    "nibbānaṃ": "နိဗ္ဗာန်", "Nibbānaṃ": "နိဗ္ဗာန်", "nibbānassa": "နိဗ္ဗာန်",
    "parinibbānaṃ": "ပရိနိဗ္ဗာန် ပြုခြင်း", "Parinibbuto": "ပရိနိဗ္ဗာန် ပြုပြီးသော",
    "parinibbute": "ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသော",
    "sayaṃ": "မိမိ", "para": "@para", "hitāya": "@hitaya",
    "bhagavā": "မြတ်စွာဘုရား", "saccavādī": "မှန်သော စကားကို ဆိုတော်မူသူ", "tathavādī": "ဟုတ်တိုင်း ဆိုတော်မူသူ",
    "avitathavādī": "မမှားယွင်းဘဲ ဆိုတော်မူသူ", "anaññathavādī": "အခြားတစ်မျိုး မဆိုတော်မူသူ",
    "sacca": "@sacca", "tatha": "ဟုတ်တိုင်း", "vitatha": "မှားယွင်း", "aññatha": "အခြားတစ်မျိုး",
    "Khandhesu": "အစုအဝေး", "khandhesu": "အစုအဝေး", "Khandhā": "အစုအဝေး",
}
NUM_MY = {"eka": "တစ်", "ekassa": "တစ်", "dve": "နှစ်", "dvinnaṃ": "နှစ်", "tayo": "သုံး", "tiṇṇaṃ": "သုံး",
          "cattāro": "လေး", "catunnaṃ": "လေး", "pañca": "ငါး", "pañcannaṃ": "ငါး", "aṭṭha": "ရှစ်"}
# ---- FRAME-END
