"""Pāli→Burmese keyword mapping for pi-5 (Kathāvatthu), PHASE 1: preamble and 1-puggalakatha.

usage (/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8, from any directory):
  map_ch1.py             writes preamble.mapped.md, 1-puggalakatha.mapped.md and map-table.md, then verifies them
  map_ch1.py --report    writes nothing; lists unmapped keywords and presence failures

The shared rules (frame / stock tables, context functions, compose rules, presence verifier) are in map5_rules.py,
which the phase-2 scripts import; this script adds only the chapter tables of the preamble and the Puggalakathā
(T_PREAMBLE, T_CH1) and the per-segment overrides CTX. Burmese: the FINAL pi-5 text of this track only.
"""
import sys
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map5_rules as R  # noqa: E402

NONE = R.NONE

# ------------------------------------------------------------------------------------------------------ preamble
T_PREAMBLE = {
    # pi-1 … pi-4 preamble values (approved samples), unchanged
    "abhidhamma": "အဘိဓမ္မာ", "Abhidhammapiṭake": "အဘိဓမ္မာပိဋက",
    "namo": "ရှိခိုးသည်", "bhagavato": "မြတ်စွာဘုရား", "arahato": "ရဟန္တာ", "sammā": "အပြည့်အဝ",
    "sammāsambuddhassa": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    "sambuddha": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်",
    # the pi-5 book title (rule 7: the approved title whole) and its members (my5-zeroshot-terms §1)
    "kathāvatthu": "အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း",
    "kathā": "ဆွေးနွေးခြင်း", "vatthu": "အငြင်းပွားရာ အကြောင်းအရာ",
}

# ------------------------------------------------------------------------------------------------------ 1-puggalakatha
T_CH1 = {
    # headings (my5-zeroshot-terms §2)
    "lakkhaṇa": "လက္ခဏာ", "gati": "လားရာ", "purisa": "@purisa", "abhiññā": "ထူးကဲစွာ သိခြင်း",
    "ñātaka": "ဆွေမျိုး", "paṭivedha": "ထိုးထွင်း သိမြင်ခြင်း", "sabhāga": "တူညီခြင်း",
    # negated propositions
    "Puggalo nupalabbhati": "ပုဂ္ဂိုလ် … မတွေ့ရ",
    # kathā members, aggregates, bases, faculties (pi-2 values where the text has them)
    "āyatanaṃ upalabbhati": "အာရုံခံ နယ်ပယ် … တွေ့ရသည်",
    "dhammāyatanaṃ upalabbhati": "သဘောတရား အာရုံခံ နယ်ပယ် … တွေ့ရသည်",
    "dhātu upalabbhati": "ဓာတ် … တွေ့ရသည်", "dhammadhātu upalabbhati": "သဘောတရား ဓာတ် … တွေ့ရသည်",
    "indriyaṃ upalabbhati": "စွမ်းရည် … တွေ့ရသည်",
    "aññātāvī upalabbhati": "အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည် … တွေ့ရသည်",
    "bahūsu": "အများစု", "aññāta": "သိရသော",
    # phase 3: the frame «aññaṃ X añño puggalo» = «Xနှင့် ပုဂ္ဂိုလ်သည် တခြားစီ» in text order (Q3; not G2: the Pāli
    # order «တခြားစီ … X» stands only in the simile «… တခြားစီ ဖြစ်သကဲ့သို့ ထို့အတူပင် ရုပ်»)
    "aññaṃ rūpaṃ": "ရုပ် … တခြားစီ", "aññaṃ viññāṇaṃ": ("သိစိတ်သည် တခြားစီ", "သိစိတ် … တခြားစီ"),
    "aññaṃ aññā vedanā": "ခံစားမှု … တခြားစီ", "aññaṃ aññe saṅkhārā": "ပြုပြင်ဖန်တီးမှု … တခြားစီ",
    "Aññā vedanā": "ခံစားမှု … တခြားစီ",
    "Rūpasmiṃ": "ရုပ်", "aññatra": "အခြား",
    # the eight / existence propositions
    "sabbo": "အားလုံး", "kehici": "အချို့", "kāmī": "ကာမ ရှိသော", "kāmino": "ကာမ ရှိသော",
    "jāto": "မွေးဖွားလာသော", "rūpī puggalo": "ရုပ် ရှိသော ပုဂ္ဂိုလ်",
    "sama": "တူသော", "same": "ညီမျှသော", "appiyaṃ": "ဦးစားမပေး", "karitvā": NONE, "jāte": "တစ်မျိုးတည်းမှ ဖြစ်သော",
    "aṭṭhe": "အနက် တူသော", "Kāyo": "ကိုယ်",
    # Gatianuyoga
    "itivuttake": "“ဣတိဝုတ်”", "sandhāvitvāna": "ကူးသွား၍", "khattu": "ကြိမ်", 
    "dukkhassanta": "ဒုက္ခ၏ အဆုံး", "khayā": "ကုန်ခန်းခြင်း",
    "anamataggo": "အစကို ရှာ၍ မတွေ့နိုင်", "nīvaraṇānaṃ": "အတားအဆီး",
    "sandhāvataṃ": "ကူးသွား", "saṃsāro": "သံသရာ", "saṃsarataṃ": "ကျင်လည်နေသော",
    "atipāto": "သတ်ခြင်း", "pāṇa": "သူ့အသက်", "katānaṃ": "ပြုခဲ့သော", "kammavipāko": "ကံ၏ အကျိုး",
    "vipaccamāne": "အကျိုး ပေးနေသော", "kusalākusale": "ကုသိုလ်နှင့် အကုသိုလ်", "maraṇaṃ": "သေခြင်း",
    "mahiso": "ကျွဲ", "kuṇi": "ကောက်သော", "chinno hoti": "ပြတ်သူ … ဖြစ်သည်", "aṅguli": "လက်ချောင်း",
    "hatthako": "လက်", "kaṇḍara": "အကြော", "aḷa": "လက်မ", "phaṇa": "လက်ချောင်းများ ကပ်နေသော",
    "manussalokā": "လူ့လောက", "upapanno": "ပြန်လည် ဖြစ်ပေါ်သော", "lokā upapanno": "လောက … ပြန်လည် ဖြစ်ပေါ်သော",
    "vigato": "ကွယ်ပျောက်သော", "viññāṇo": "သိစိတ်", "vedano": "ခံစားမှု", "rūpo": "ရုပ်", "sañño": "မှတ်သိမှု",
    "saṅkhāro": "ပြုပြင်ဖန်တီးမှု",
    "Ucchedā": "ပြတ်စဲခြင်း", "bhijjamānesu": "ပြိုကွဲကြသော", "bhijjati": "ပြိုကွဲသည်", "buddhena": "ဘုရားရှင်",
    "samasamo": "အလွန် တူညီစွာ", "vivajjitā": "ပယ်ရှားတော်မူသော",
    # Upādāpaññattānuyoga
    "paṭiccasamuppannaṃ": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော",
    "paṭiccasamuppanno": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော",
    "khayadhammā": "ကုန်ခန်းတတ်သော သဘော … ရှိသော", "vayadhammā": "ပျက်စီးတတ်သော သဘော … ရှိသော",
    "virāgadhammā": "ပြယ်ပျောက်တတ်သော သဘော … ရှိသော", "nirodhadhammā": "ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော",
    "khayadhammo": "ကုန်ခန်းတတ်သော သဘော … ရှိသော", "vayadhammo": "ပျက်စီးတတ်သော သဘော … ရှိသော",
    "virāgadhammo": "ပြယ်ပျောက်တတ်သော သဘော … ရှိသော", "nirodhadhammo": "ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော",
    "vipariṇāmadhammā": "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော",
    "vipariṇāmadhammo": "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော",
    "anicco": "မမြဲသော", "pītaṃ": "အဝါ", "lohitaṃ": "အနီ", "appaṭighassa": "ထိခိုက်မှု မရှိသော",
    "saphalā": "အသီးအပွင့် ရှိသော", "saphalaṃ": "အသီးအပွင့် ရှိသော", "phalā": "အသီးအပွင့်",
    "puggalo saphalo": "ပုဂ္ဂိုလ် … အသီးအပွင့် ရှိသော",
    "iṭṭha": "လိုလားဖွယ်", "aniṭṭha": "မလိုလားဖွယ်", "kanta": "ချစ်ခင်ဖွယ်", "akanta": "မချစ်ခင်ဖွယ်",
    "manuñña": "စိတ်နှင့် တွေ့သော", "amanuñña": "စိတ်နှင့် မတွေ့သော",
    "asecanaka": "မရောနှောသော", "secanaka": "ရောနှောသော",
    "kusalassa puggalassa": "ကုသိုလ် ပုဂ္ဂိုလ်", "akusalassa puggalassa": "အကုသိုလ် ပုဂ္ဂိုလ်",
    "abyākatassa puggalassa": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပုဂ္ဂိုလ်",
    "kusalassa puggalassa paññatti": "ကုသိုလ် ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက်",
    "akusalassa puggalassa paññatti": "အကုသိုလ် ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက်",
    "abyākatassa puggalassa paññatti": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက်",
    "Abyākataṃ": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "niruddhe": "ချုပ်ငြိမ်းသွားသော", "niruddhāya": "ချုပ်ငြိမ်းသွားသော", "cakkhumā": "မျက်စိ ရှိသော",
    "manaṃ": "မနော", "Micchādiṭṭhiṃ": "မှားယွင်းသော အယူ", "Micchādiṭṭhiṃ upādāya": "မှားယွင်းသော အယူကို မှီ၍",
    "dhammadhātuṃ": "သဘောတရား ဓာတ်", "Cakkhudhātuṃ": "မျက်စိ ဓာတ်",
    "Ekavokārabhavaṃ": "အစုအဝေး တစ်ပါး ရှိသော ဘဝ", "Catuvokārabhavaṃ": "အစုအဝေး လေးပါး ရှိသော ဘဝ",
    "Pañcavokārabhavaṃ": "အစုအဝေး ငါးပါး ရှိသော ဘဝ",
    "anantara": "နောက်ဆက်တွဲ", "vāra": "အကြိမ်", "chāyāya": "အရိပ်", "rukkhaṃ": "သစ်ပင်", "gāmikassa": "ရွာသား",
    "rañño": "မင်း", "raṭṭhaṃ": "တိုင်းပြည်", "rūpavā": "ရုပ် ရှိသော", "nigaḷo": "သံခြေချင်း",
    "negaḷiko": "သံခြေချင်း ခတ်ထားသူ",
    "Citte": "စိတ်", "citte": "စိတ်", "citte uppanne": "စိတ် ဖြစ်ပေါ်သော", "uppanne": "ဖြစ်ပေါ်သော",
    "jāyati": "မွေးဖွားသည်", "jīyati": "အိုသည်", "mīyati": "သေဆုံးသည်", "kumārako": "သူငယ်", "kumārikā": "သူငယ်မ",
    "puriso": "ယောက်ျား", "itthī": "မိန်းမ",
    # Purisakārānuyoga
    "kammāni upalabbhanti": "ကံတို့ကို တွေ့ရသည်", "pāpakāni kammāni upalabbhanti": "ယုတ်မာသော ကံတို့ကို တွေ့ရသည်",
    "kalyāṇa kāretā": "ကောင်းမွန်သော … ပြုလုပ်စေသူ", "kalyāṇa vipāko": "ကောင်းမွန်သော … အကျိုး",
    "kammānaṃ upalabbhati": "ကံ … တွေ့ရသည်", "pāpakānaṃ kammānaṃ upalabbhati": "ယုတ်မာသော ကံ … တွေ့ရသည်",
    "Tassa tasseva": "ထိုထိုသူ၏ပင်", "dukkhassa antakiriyā": "ဒုက္ခ၏ အဆုံးကို ပြုခြင်း", "upacchedo": "ပြတ်ခြင်း",
    "vaṭṭa": "သံသရာ စက်ဝန်း", "pabbata": "တောင်", "sineru": "မြင့်မိုရ်", "rājā": "@raja",
    "kaṭṭha": "ထင်း", "vanappatayo": "သစ်ပင်", "kaṭṭhavanappatayo": "ထင်း … သစ်ပင်",
    "vanappatayo upalabbhanti": "သစ်ပင်တို့ကို တွေ့ရသည်", "vanappatayo atthi": "သစ်ပင်တို့ ရှိသည်",
    "Dibbaṃ": "နတ်", "dibbassa": "နတ်", "Dibbassa": "နတ်", "Mānusakaṃ": "လူ", "mānusakassa": "လူ",
    "Mānusakassa": "လူ", "Āpāyikaṃ": "အပါယ်", "Nerayikaṃ": "ငရဲ", "sukhassa": "ချမ်းသာ",
    "dukkhassa paṭisaṃvedī": "ဆင်းရဲကို ခံစားသော", "puggalassa paṭisaṃvedī": "ပုဂ္ဂိုလ်ကို ခံစားသော",
    "nibbānassa paṭisaṃvedī": "နိဗ္ဗာန်ကို ခံစားသော", "anattā": "အတ္တ မဟုတ်သော",
    "kataṃ dukkhaṃ": "ဆင်းရဲ … ပြုထားသော", "kāraṃ dukkhaṃ": "ဆင်းရဲ … ပြုသော", "adhicca": "အကြောင်းမဲ့",
    # Abhiññānuyoga, Ñātaka, Paṭivedha, Saṅgha
    "vikubbati": "ဖန်ဆင်းပြသည်", "iddhiṃ": "ဣဒ္ဓိ", "dibbāya": "နတ်", "sotadhātuyā": "နား ဓာတ်",
    "dibbāya sotadhātuyā": "နတ်နား ဓာတ်", "nivāsaṃ": "ဘဝ", "vijānāti": "သိသည်",
    "suṇāti": "ကြားသည်", "ghāyati": "နမ်းသည်", "sāyati": "လျက်သည်", "phusati": "ထိသည်",
    "purisapuggalā": "ပုဂ္ဂိုလ်", "purisayugā": "လူ အတွဲ", "yugā": "အတွဲ",
    "pātubhavanti": "ပေါ်ပေါက်သည်", "pātubhāvā": "ပွင့်ပေါ်ခြင်း", "buddha": "@buddha",
    # Saccikaṭṭhasabhāgānuyoga
    "koṭi": "အစွန်း", "ālapana": "ခေါ်ဝေါ်ပုံ", "nānaṃ": "ကွဲပြားသည်", "uppādo": "ဖြစ်ခြင်း",
    "lakkhaṇāni": "လက္ခဏာ", "ṭhitassa": "တည်နေသော", "Puggalassa": "ပုဂ္ဂိုလ်",
    "Asaṅkhatānaṃ dhammānaṃ": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရား",
    "puggalo neva saṅkhato": "ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားသော အရာလည်း မဟုတ်",
    "Puggalo neva saṅkhato": "ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားသော အရာလည်း မဟုတ်",
    "ucchinno": "ပြတ်စဲသွားသော", "atthatthamhi": "ရှိခြင်း သဘော", "tiṭṭhati": "တည်သည်",
    "samuppanno": "ဖြစ်ပေါ်လာသော", "vediyamāno": "ခံစားနေသော", "sukhaṃ vediyamāno": "သာယာသော ခံစားမှုကို ခံစားနေသော",
    "sadā": "အမြဲ", "taro": "ကူးမြောက်သူ", "Suññato": "ဆိတ်သုဉ်းသည်", "niddesa": "ဖွင့်ဆိုချက်",
    "avekkhassu": "ရှုမြင်သည်", "avekkhantaṃ": "ရှုမြင်နေသော", "māṇava": "လုလင်", "ohacca": NONE, "uhacca": NONE,
    "ūhacca": "နှုတ်ပယ်၍", "anudiṭṭhiṃ": "အယူ", "avekkhati": "ရှုမြင်သည်", "rūpena": "ရုပ်",
    "nikkhamitvā": "ထွက်၍", "bahiddhā": "အပြင်", "uppajjamāno": "ပေါ်ပေါက်လာသော",
    "anukampāya": "သနားခြင်း", "sukhāya": "ချမ်းသာ", "dha": "“ဓမ္မပဒ”",
    "uppajjamānaṃ": "ဖြစ်ပေါ်သော", "nirujjhamānaṃ": "ချုပ်ငြိမ်းသော", "paccaya": "အကြောင်း",
    "veti": "ပျက်ကွယ်သည်", "paccesi": "ယုံကြည်သည်", "ratho": "ရထား", "sambhoti": "ဖြစ်ပေါ်သည်",
    "pāpimantaṃ": "မကောင်းမှု ပြုသော", "Nāññatra": "တစ်ပါး", "bhikkhunī": "ဘိက္ခုနီ", "sammati": NONE,
    "sambhārā": "အစိတ်အပိုင်း", "Kinnu": "အဘယ်ကြောင့်", "te": "သင်", "puñjo": "အစုအပုံ",
    "attaniyena": "အတ္တနှင့် ဆိုင်သော အရာ", "bhagavantaṃ": "မြတ်စွာဘုရား", "cakkhusamphasso": "မျက်စိ တွေ့ထိမှု",
    "vedayitaṃ": "ခံစားရမှု", "manosamphasso": "မနော တွေ့ထိမှု", "attena": "အတ္တ", "tasmā": "သောကြောင့်",
    "āyasmā": "အသျှင်", "āyasmā ānando": "အသျှင် အာနန္ဒာ", "yampidaṃ": "ရှိသမျှ",
    "attaniyaṃ": "အတ္တနှင့် ဆိုင်သော အရာ", "paripūro": "ပြည့်စုံသော", "pecca": "သေပြီးနောက်",
    "sassatisamaṃ": "ထာဝရ တည်မြဲသည်နှင့် တူစွာ", "bāla": "လူမိုက်", "tatheva": "ထိုအတိုင်းပင်",
    "attani": "အတ္တ", "dhuvo": "ခိုင်ခံ့သော", "ṭhānaṃ": "တည်ရာ", "ṭhassāmi": "တည်သည်", "kevalo": "သက်သက်",
    "pana": "တစ်ဖန်", "paññāpeti": "ပညတ်သည်", "atthato": "အဓိပ္ပာယ်", "seniya": "သေနိယ",
    "satthāro santo": "ဆရာ … ရှိသည်",
    "sarāvakaṃ": "ပန်းကန်", "āharaṇena": "ကိုးကားခြင်း", "dhuva": "ခိုင်ခံ့သော", "kosakaṃ": "ခွက်",
    "sutta": "သုတ္တန်", "thālakaṃ": "ဗန်း", "pānīya": "သောက်ရေ", "sassatā": "ထာဝရ တည်မြဲသော", "yāgū": "ယာဂု",
    "bhattaṃ": "ထမင်း", "khīra": "နွားနို့", "phāṇita": "တင်လဲ", "sandhāvaniyā": "ကူးသွားခြင်း",
    "peyyālā": "အကျဉ်းချုံ့ချက်", "aṭṭhamaṃ": "အဋ္ဌမ", "pañcamaṃ": "ပဉ္စမ",
    "visadisaṃ": "ကွဲပြားသည်", "thokaṃ": "အနည်းငယ်", "pajānāmi": "ကွဲပြားစွာ သိသည်",
}
FUNCS1 = {
    "purisa": lambda kw, pali, my: "လူ" if R.re.search(r"purisakār|purisayug|purisapuggal", pali) and "လူ" in my
        else ("ယောက်ျား" if "ယောက်ျား" in my else "လူ"),
    "raja": lambda kw, pali, my: "မင်း" if "မင်း" in my else "@prior",
    "buddha": lambda kw, pali, my: "ဘုရား" if "ဘုရား ပွင့်ပေါ်" in my else "@prior",
}

# per-segment overrides (one sense per segment where the keyword list mixes two constructions)
CTX = {
    "5-122": {"rūpaṃ": "အဆင်းအရောင်", "Rūpaṃ puggalo": "ရုပ် … ပုဂ္ဂိုလ်", "Puggalo rūpaṃ": "ပုဂ္ဂိုလ် … ရုပ်",
              "rūpaṃ cavati": "ရုပ်သည် စုတေသည်"},
    "5-230": {"uppajjati": "ပေါ်ပေါက်လာသည်"},           # «uppajjamāno uppajjati» «… ပေါ်ပေါက်လာသောအခါ»
    "5-232": {"paccaya": "မှီသော"},
    "5-238": {"nicca": "အမြဲ", "dhuva": "အမြဲ"},       # niccabhattaṃ / dhuvayāgū «အမြဲ ထမင်း / အမြဲ ယာဂု» first                     # aparappaccaya «သူတစ်ပါးကို မမှီသော» (rule 8)
}

CHAPTERS = ["preamble", "1-puggalakatha"]


def mapper():
    return R.Mapper(chapter_tables={"preamble": T_PREAMBLE, "1-puggalakatha": T_CH1}, ctx=CTX, funcs=FUNCS1)


def main():
    report = "--report" in sys.argv
    M = mapper()
    total_bad = 0
    out = {}
    for ch in CHAPTERS:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        out[ch] = (lines, problems, unmapped, nne)
        for sid, kw in unmapped:
            print("UNMAPPED", ch, sid, kw)
        for sid, kw, v in problems:
            print("ABSENT", ch, sid, kw, "=", v)
        total_bad += len(unmapped) + len(problems)
        if not report and not unmapped and not problems:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if report or total_bad:
        print("problems", total_bad)
        return
    for ch in CHAPTERS:
        n, bad, fails, punct, ruled = R.verify_file(ch)
        print(ch, "lines", n, "bad", bad, "presence failures", len(fails), "punct", punct,
              "ending-rule chunks", len(ruled), "(no direct equivalent)", out[ch][3])
    import map_table_ch1
    map_table_ch1.write(M, out)


if __name__ == "__main__":
    main()
