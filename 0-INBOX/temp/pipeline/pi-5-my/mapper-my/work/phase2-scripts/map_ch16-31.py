"""Pāli→Burmese keyword mapping for pi-5 (Kathāvatthu), PHASE 2, group ch16–31 (16-atthamavaggo … 31-tevisatimavaggo).

usage (/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8, from any directory):
  map_ch16-31.py [CH …]          writes <ch>.mapped.md for the chapters of the group (all 16 when none is named), then
                                 verifies each (preservation, presence, punctuation) and prints the results per chapter
  map_ch16-31.py --report [CH …] writes nothing; lists unmapped keywords and presence failures

Imports the shared module map5_rules.py (phase 1; NOT edited here) and the chapter table of map_ch1.py (read only; it
runs nothing on import). This script holds only the tables of the group (T_GROUP, T[ch]), the per-segment overrides
(CTX) and the new context functions (FUNCS3). Lookup: CTX[segment] → the chapter's table → the group table → the
module (FRAME / STOCK) → a ch1 table value the segment's Burmese has → the module's lookup (pi-5 terms, pi-1 … pi-4
values, compose rules). Burmese: the FINAL pi-5 text of this track only. Module overrides: notes-ch16-31.md.
"""
import sys
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map5_rules as R  # noqa: E402
import map_ch1 as C1  # noqa: E402

NONE = R.NONE
CHAPTERS = ["16-atthamavaggo", "17-navamavaggo", "18-dasamavaggo", "19-ekadasamavaggo", "20-dvadasamavaggo",
            "21-terasamavaggo", "22-cuddasamavaggo", "23-pannarasamavaggo", "24-solasamavaggo", "25-sattarasamavaggo",
            "26-attharasamavaggo", "27-ekunavisatimavaggo", "28-visatimavaggo", "29-ekavisatimavaggo",
            "30-bavisatimavaggo", "31-tevisatimavaggo"]

# ------------------------------------------------------------------------------------------------ vagga headings
# «Aṭṭhamavaggo» = «အဋ္ဌမ ဝဂ်» (the text's heading; FRAME vaggo = ဝဂ်, the ordinal as FRAME Pañcamo = ပဉ္စမ)
ORD = {"aṭṭhama": "အဋ္ဌမ", "navama": "နဝမ", "dasama": "ဒသမ", "ekādasama": "ဧကာဒသမ", "dvādasama": "ဒွါဒသမ",
       "terasama": "တေရသမ", "cuddasama": "စုဒ္ဒသမ", "pannarasama": "ပန္နရသမ", "soḷasama": "သောဠသမ",
       "sattarasama": "သတ္တရသမ", "aṭṭhārasama": "အဋ္ဌာရသမ", "ekūnavīsatima": "ဧကူနဝီသတိမ", "vīsatima": "ဝီသတိမ",
       "ekavīsatima": "ဧကဝီသတိမ", "bāvīsatima": "ဗာဝီသတိမ", "tevīsatima": "တေဝီသတိမ"}

# ------------------------------------------------------------------------------------------------ shared in the group
# values that recur in several chapters of the group (after the chapter's own table, before the module); a tuple
# («a», «b», …) = the first value the segment's Burmese has (presence), else the pi-1 … pi-4 value
T_GROUP = {
    # existence / planes (ch16 Antarābhava-, Kāma-, Rūpadhātu-kathā and later)
    "parinibbāyī": "ပရိနိဗ္ဗာန် ပြုသော",               # Q8 / pi-4 (the terms list «…ပြုသူ»)
    "antarā": "ကြား", "antare": "ကြား", "antarābhava": "ကြားဘဝ", "antarābhavo": "ကြားဘဝ", "Antarābhava": "ကြားဘဝ",
    "antarābhavūpagaṃ": "ကြားဘဝသို့ ရောက်စေသော", "antarābhavūpagā": "ကြားဘဝသို့ ရောက်သော",
    "upagaṃ": ("ရောက်စေသော",), "upagā": ("ရောက်သော",), "upagassa": ("ရောက်မည့်", "ရောက်သော"),
    "gatiyo": "လားရာ", "yoni": ("မွေးဖွားရာ အမျိုးအစား", "မွေးဖွားရာ"), "tiracchānayoni": "တိရစ္ဆာန် မွေးဖွားရာ",
    "nirayo": "ငရဲ", "manussā": "လူ", "vuttā": "ဟောတော်မူသည်", "āvāso": "နေရာ ဘုံ", "satta": ("သတ္တဝါ",),
    "ṭhiti": "@thiti", "attabhāvapaṭilābho": "ကိုယ်ခန္ဓာ ရရှိခြင်း", "attabhāva": ("ကိုယ်ခန္ဓာ",),
    "attabhāvo": ("ကိုယ်ခန္ဓာ",), "atta": "@atta",
    "jāyanti": "မွေးဖွားသည်", "jīyanti": "အိုသည်", "mīyanti": "သေဆုံးသည်",
    "kāmabhavo": "ကာမဘုံ၌ ဖြစ်သော ဘဝ", "kāmabhavassa": "ကာမဘုံ၌ ဖြစ်သော ဘဝ", "Kāmabhavassa": "ကာမဘုံ၌ ဖြစ်သော ဘဝ",
    "kāmabhavena": "ကာမဘုံ၌ ဖြစ်သော ဘဝ", "Kāmabhavena": "ကာမဘုံ၌ ဖြစ်သော ဘဝ",
    "rūpabhavo": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ", "Rūpabhavo": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ",
    "rūpabhavassa": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ", "Rūpabhavassa": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ",
    "rūpabhavena": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ",
    "arūpabhavo": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်သော ဘဝ", "arūpabhavassa": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်သော ဘဝ",
    "arūpabhavena": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်သော ဘဝ", "bhavehi": "ဘဝ",
    "dhātū": "@dhatu_plane", "kāmadhātū": "ကာမဘုံ", "kāmadhātu": ("ကာမဘုံ", "ကာမ ဓာတ်"),
    "rūpadhātū": ("သိမ်မွေ့သော ရုပ်ဘုံ", "အဆင်းအရောင် ဓာတ်"), "rūpadhātu": ("သိမ်မွေ့သော ရုပ်ဘုံ", "အဆင်းအရောင် ဓာတ်", "သိမ်မွေ့သော ရုပ် ဓာတ်"),
    "arūpadhātū": "ရုပ်မရှိသော ဘုံ", "arūpadhātu": ("ရုပ်မရှိသော ဘုံ", "ရုပ်မရှိသော ဓာတ်"), "Arūpe": "ရုပ်မရှိသော ဘုံ",
    "arūpesu": "ရုပ်မရှိသော ဘုံ", "guṇa": "ဂုဏ်", "guṇā": "ဂုဏ်", "kāmaguṇa": "ကာမဂုဏ်", "kāmaguṇā": "ကာမဂုဏ်",
    "rūpino dhammā": ("ရုပ် ဖြစ်သော သဘောတရား", "ရုပ် … သဘောတရား"),
    "arūpino dhammā": "ရုပ် မဟုတ်သော သဘောတရား",
    # the vipāka / samuṭṭhāna propositions
    "samuṭṭhitaṃ": "ဖြစ်ပေါ်သော", "samuṭṭhito": "ဖြစ်ပေါ်သော", "samuṭṭhitā": "ဖြစ်ပေါ်သော",
    "Kusalena": "ကုသိုလ်", "kusalena": "ကုသိုလ်", "Akusalena": "အကုသိုလ်", "akusalena": "အကုသိုလ်",
    "Yaṃ kiñci": "မှန်သမျှ", "yaṃ kiñci": "မှန်သမျှ",
    "phassavippayuttaṃ": "တွေ့ထိမှုနှင့် ကင်းကွာသော", "ekadesaṃ": "တစ်စိတ်တစ်ဒေသ", "ekadeso": "တစ်စိတ်တစ်ဒေသ",
    "bhijjati": "ပျက်သည်", "bhijjamāne": "ပျက်နေသော",
    "sukhadukkhaṃ": ("ချမ်းသာနှင့် ဆင်းရဲ", "ချမ်းသာ ဆင်းရဲ", "သုခ ဒုက္ခ"),
    "samāpannassa": ("ဝင်စားနေသော", "ဝင်စားသော"), "samāpanno": ("ဝင်စားနေသော", "ဝင်စားသော"),
    "saṅkhārakkhandha": "ပြုပြင်ဖန်တီးမှု အစုအဝေး",
    "sacchikaronti": "မျက်မှောက် ပြုသည်", "dukkhā": "@dukkha", "sāvaka": "သာဝက",
    "paccekasambuddhā": "ပစ္စေကဗုဒ္ဓါ", "sambuddhā": ("အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်",),
    "ariyassa": "အရိယာ", "purisassa": ("ယောကျ်ား", "ယောက်ျား", "လူ"),
    # the ten unwholesome courses / the heinous deeds
    "pāṇātipāta": "သူ့အသက်ကို သတ်ခြင်း", "Pāṇātipātakammassa": "သူ့အသက်ကို သတ်ခြင်း ကံ",
    "ruhira": "သွေး", "palāpa": "ပြိန်ဖျင်းသော စကား", "sampha": "အကျိုးမဲ့", "pisuṇa": "ကုန်းတိုက်သော",
    "pharusa": "ကြမ်းတမ်းသော", "musā": "မုသား", "pitu": "အဖ", "mātu": "အမိ",
    "micchācāra": "မှားယွင်းစွာ ကျင့်ခြင်း", "ādāna": "ယူခြင်း", "bheda": "သင်းခွဲခြင်း", "atipāta": "သတ်ခြင်း",
    "sotāpattiphalā": "သောတာပတ္တိဖိုလ်", "sakadāgāmiphalā": "သကဒါဂါမိဖိုလ်", "anāgāmiphalā": "အနာဂါမိဖိုလ်",
    "bhāvo": ("သဘော", NONE), "jano": "@jana", "janassa": "@jana", "aṅgo": "@anga3", "aṅga": "@anga3", "aṅgaṃ": "@anga3",
    "aṅgānaṃ": "@anga3", "aṅgā": "@anga3",
    "niruddhe": ("ချုပ်ငြိမ်းသွားသော", "ချုပ်ငြိမ်းပြီးသော", "ချုပ်ငြိမ်းသော"),
    "upapattesiye": "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော", "Upapattesiye": "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော",
    "Upapattesiyena": "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော", "sammukhībhāvaṃ": "မျက်နှာချင်း ဆိုင်ခြင်း",
    "āgacchanti": "ရောက်သည်", "sappaṭibhāgā": "ဆန့်ကျင်ဘက် ရှိသော",
    "sappaṭibhāgā sammukhībhāvaṃ āgacchanti": "ဆန့်ကျင်ဘက် ရှိသော … မျက်နှာချင်း ဆိုင်ခြင်းသို့ ရောက်သည်",
    "ānisaṃsa": "အကျိုးကျေးဇူး", "Ānisaṃsa": "အကျိုးကျေးဇူး",
    "maggasamaṅgī": "မဂ်နှင့် ပြည့်စုံသော", "Maggasamaṅgī": "မဂ်နှင့် ပြည့်စုံသော",
    "maggasamaṅgissa": "မဂ်နှင့် ပြည့်စုံသော", "Maggasamaṅgissa": "မဂ်နှင့် ပြည့်စုံသော",
    "samaṅgī": ("ပြည့်စုံသော", "ပြည့်စုံနေသော"), "samaṅgissa": "ပြည့်စုံသော",
    "Cakkhuviññāṇasamaṅgissa": "မျက်စိ သိစိတ်နှင့် ပြည့်စုံသော",
    "cakkhuviññāṇasamaṅgī": ("မျက်စိ သိစိတ်နှင့် ပြည့်စုံသော", "မျက်စိ သိစိတ်နှင့် ပြည့်စုံနေသော"),
    "Cakkhuviññāṇasamaṅgī": ("မျက်စိ သိစိတ်နှင့် ပြည့်စုံသော", "မျက်စိ သိစိတ်နှင့် ပြည့်စုံနေသော"),
    "lokiyena": "လောကနှင့် သက်ဆိုင်သော", "lokiyāya": "လောကနှင့် သက်ဆိုင်သော", "Lokiye": "လောကနှင့် သက်ဆိုင်သော",
    "lokiye": "လောကနှင့် သက်ဆိုင်သော", "lokuttarena": "လောကကို ကျော်လွန်သော",
    "lokuttarāya": "လောကကို ကျော်လွန်သော", "dhammo": ("သဘောတရား", "တရား"), "phassānaṃ": "တွေ့ထိမှု", "vīriyena": "ဝီရိယ", "saddhāya": "ယုံကြည်မှု",
    "cittavippayutto": "စိတ်နှင့် ကင်းကွာသော", "cittavippayuttaṃ": "စိတ်နှင့် ကင်းကွာသော",
    "cittavippayuttā": "စိတ်နှင့် ကင်းကွာသော", "cittavippayutta": "စိတ်နှင့် ကင်းကွာသော",
    "parinipphannā": ("ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော", "အမှန်တကယ် ဖြစ်ပေါ်ပြီးသော"),
    "parinipphannaṃ": ("ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော", "အမှန်တကယ် ဖြစ်ပေါ်ပြီးသော", "ပြည့်စုံစွာ ပြီးမြောက်သော"),
    "parinipphanno": ("ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော", "အမှန်တကယ် ဖြစ်ပေါ်ပြီးသော"),
    "samāpatti": ("ဈာန် ဝင်စားခြင်း", "သမာပတ်"), "nipphannā": "ဖြစ်ပေါ်ပြီးသော", "nipphannaṃ": "ဖြစ်ပေါ်ပြီးသော",
    "nipphanno": "ဖြစ်ပေါ်ပြီးသော", "sakavādī": "မိမိဘက်", "paravādī": "တစ်ဖက်သား", "āvuso": "ငါ့ရှင်",
    "kālaṅkato": "ကွယ်လွန်ပြီးသော", "viya": "ကဲ့သို့", "ñāṇena": "ဉာဏ်", "vutto": "ဟောတော်မူသည်",
    "niyāmaṃ": "သေချာသော လမ်းကြောင်း",
    "parinibbuto": ("ပရိနိဗ္ဗာန် ပြုပြီးသော", "ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့သော"),
    "bhāvitā": ("ပွားများထားသော", "ပွားများပြီးသော", "ပွားများသော"), "yugaṃ": ("နှစ်ပါး", "အစုံ"),
    "sāvakayugaṃ": ("အဂ္ဂသာဝက နှစ်ပါး", "တပည့် အစုံ"), "tiṭṭhati": ("တည်သည်", "တည်နေသည်", "တည်ရှိသည်"), "vedeti": ("ခံစားသည်", "ခံစားရသည်"),
    "saṅkhārakkhandhapariyāpanno": "ပြုပြင်ဖန်တီးမှု အစုအဝေး၌ အကျုံးဝင်သော",
    "saṅkhārakkhandhapariyāpannā": "ပြုပြင်ဖန်တီးမှု အစုအဝေး၌ အကျုံးဝင်သော",
    "rūpakkhandhapariyāpannā": "ရုပ် အစုအဝေး၌ အကျုံးဝင်သော", "antarikā": "@antarika3", "buddho": ("ဘုရားရှင်", "ဘုရား"), "Buddho": ("ဘုရားရှင်", "ဘုရား"), "pāṇaṃ": ("သတ္တဝါ", "သူ့အသက်"), "buddhena": ("ဘုရားရှင်", "ဘုရား"), "upacaya": ("စုဆောင်းမှု", "စုဆောင်းခြင်း"),
    "upacayo": ("စုဆောင်းမှု", "စုဆောင်းခြင်း"), "dānaṃ": ("အလှူ", "ဒါန", "ပေးလှူခြင်း"),
    "jīvitāvasese": ("အသက်၏ အကြွင်း", "အသက် အကြွင်းအကျန်"), "sañcetanikānaṃ": ("ရည်ရွယ်၍", "စေ့ဆော်၍"), "pajānāti": ("သိသည်", "ပိုင်းခြား သိသည်"),
    "nirodho": ("ချုပ်ငြိမ်းခြင်း", "ချုပ်သော"), "nirodhaṃ": ("ချုပ်ငြိမ်းရာ ဈာန်", "ချုပ်ငြိမ်းခြင်း", "ချုပ်သော"),
    "rūpadhātupariyāpanno": "သိမ်မွေ့သော ရုပ် ဓာတ်၌ အကျုံးဝင်သော", "saddadhātupariyāpanno": "အသံ ဓာတ်၌ အကျုံးဝင်သော",
    "gandhadhātupariyāpanno": "အနံ့ ဓာတ်၌ အကျုံးဝင်သော", "rasadhātupariyāpanno": "အရသာ ဓာတ်၌ အကျုံးဝင်သော",
    "phoṭṭhabbadhātupariyāpanno": "အထိအတွေ့ ဓာတ်၌ အကျုံးဝင်သော",
    "arūpadhātupariyāpanno": "ရုပ်မရှိသော ဓာတ်၌ အကျုံးဝင်သော", "kāmadhātupariyāpanno": "ကာမ ဓာတ်၌ အကျုံးဝင်သော", "sahajāto": "အတူ ပေါ်ပေါက်သော", "sahajātaṃ": "အတူ ပေါ်ပေါက်သော",
    "sahajātā": "အတူ ပေါ်ပေါက်သော", "anantarā": ("ချက်ချင်း နောက်", "ချက်ချင်း"),
    "tiracchānayoniṃ": ("တိရစ္ဆာန် ဘဝ", "တိရစ္ဆာန် ဘုံ", "တိရစ္ဆာန် မွေးဖွားရာ အမျိုးအစား"),
    "yoniṃ": ("ဘဝ", "ဘုံ", "မွေးဖွားရာ အမျိုးအစား"), "maggaṃ": ("မဂ်", "လမ်း"), "magga": ("မဂ်", "လမ်း"), "maggo": ("မဂ်", "လမ်း"),
    "Atītena": "အတိတ်", "atītena": "အတိတ်", "anāgatena": "အနာဂတ်", "paccuppannena": "ပစ္စုပ္ပန်", "vacīsañcetanā": "နှုတ်ဖြင့် စေ့ဆော်မှု", "kāyasañcetanā": "ကိုယ်ဖြင့် စေ့ဆော်မှု",
    "manosañcetanā": "မနောဖြင့် စေ့ဆော်မှု",
}

T = {ch: {} for ch in CHAPTERS}

T["16-atthamavaggo"] = {
    "Kāmakathā": "ကာမအကြောင်း ဆွေးနွေးချက်",
    "Kāmabhavassa antare antarābhavo": "ကာမဘုံ၌ ဖြစ်သော ဘဝ … ကြား၌ ကြားဘဝ",
    # ^5-503 / ^5-504 the six destinations
    "vaṇṇā": "အဆင်း", "asurā": "အသုရာ", "asura": "အသုရာ", "bhogā": "စည်းစိမ်", "āhārā": "အစာ", "pubba": "ရှေး",
    "vivāhaṃ": "ထိမ်းမြားခြင်း", "āvāha": NONE, "āyukā": "အသက်", "vepacitti": "ဝေပစိတ္တိ",
    "aṭṭhamī": "အဋ္ဌမ", "Pañcamī": "ပဉ္စမ", "chaṭṭhamī": "ဆဋ္ဌမ",
    "ānantariyassa": "အနန္တရိယ ကံကို ပြုသော", "nirayūpagassa puggalassa": "ငရဲသို့ ရောက်မည့် ပုဂ္ဂိုလ်",
    "antarāparinibbāyī puggalo": "သက်တမ်း၏ အလယ်သို့ မရောက်မီ ပရိနိဗ္ဗာန် ပြုသော ပုဂ္ဂိုလ်",
    "kāmabhavūpagaṃ kammaṃ": "ကာမဘုံ၌ ဖြစ်သော ဘဝသို့ ရောက်စေသော ကံ",
    "kāmaguṇūpagaṃ kammaṃ": "ကာမဂုဏ်တို့သို့ ရောက်စေသော ကံ", "rūpūpagaṃ kammaṃ": "ရုပ်သို့ ရောက်စေသော ကံ",
    "vedanūpagaṃ kammaṃ": "ခံစားမှုသို့ ရောက်စေသော ကံ",
    # ^5-510 … ^5-514 Kāmaguṇa- / Kāmakathā
    "virājetvā": "ကင်းစေ၍", "pamuccati": "လွတ်မြောက်သည်", "chaṭṭhā": "ခြောက်ခုမြောက်",
    "tappaṭisaññutto": "ထိုအရာနှင့် စပ်ယှဉ်သော", "tappaṭisaññuttaṃ": "ထိုအရာနှင့် စပ်ယှဉ်သော",
    "tappaṭisaṃyutto": "ထိုအရာနှင့် စပ်ယှဉ်သော", "tappaṭisaṃyuttaṃ": "ထိုအရာနှင့် စပ်ယှဉ်သော",

    "sambuddhā uppajjanti": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် … ပွင့်သည်",
    "paccekasambuddhā uppajjanti": "ပစ္စေကဗုဒ္ဓါ … ပွင့်သည်",
    "Cakkhuviññeyyā rūpā": "မျက်စိဖြင့် သိနိုင်သော … အဆင်းအရောင်", "iṭṭhā": "လိုလားဖွယ် ကောင်းသော",
    "kantā": "ချစ်ခင်ဖွယ် ကောင်းသော", "manāpā": "နှစ်သက်ဖွယ် ကောင်းသော", "piyarūpā": "ချစ်ဖွယ် သဘော ရှိသော",
    "kāmūpasaṃhitā": "ကာမနှင့် စပ်သော", "upasaṃhitā": "စပ်သော", "rajanīyā": "တပ်မက်ဖွယ် ကောင်းသော",
    "Pañcevāyatanā kāmā": "အာရုံခံ နယ်ပယ် ငါးပါးသည်သာ ကာမ", "pañcevāyatanā kāmā": "အာရုံခံ နယ်ပယ် ငါးပါးသည်သာ ကာမ",
    "citrāni": "အဆန်းတကြယ် ရှိသော အရာ", "saṅkappa": "ကြံစည်မှု", "vinayanti": "ပယ်ဖျောက်သည်",
    "Tiṭṭhanti": "တည်သည်", "dhīrā": "ပညာရှိ", "nibbedhika": "နိဗ္ဗေဓိက",
    # ^5-515 … ^5-526 Rūpadhātu- / Arūpadhātukathā
    "āyataniko": "အာရုံခံ နယ်ပယ် … ရှိသော", "khāriyaṃ": "ပြာရည် အရသာ", "loṇiyaṃ": "အငန်",
    "arūpattabhāvapaṭilābho": "ရုပ်မရှိသော … ကိုယ်ခန္ဓာ ရရှိခြင်း", "nissaraṇaṃ": "ထွက်မြောက်ရာ",
    "nekkhammaṃ": "ကာမမှ ထွက်မြောက်ခြင်း", "anāsavesu": "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော အရာ",
    # ^5-527 … ^5-538 Rūpaṃ kusalaṃ …
    "asuci": "မစင်ကြယ်သော သုက်ထွက်ခြင်း",
    # ^5-540 … ^5-545 Jīvitindriyakathā
    "rūpajīvita": "ရုပ် အသက်", "Arūpīnaṃ āyu": "ရုပ် မဟုတ်သော … သက်တမ်း", "arūpajīvita": "ရုပ် မဟုတ်သော အသက်",
    "Nirodhaṃ samāpannassa": "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသော",
    "upapattesiye": "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော", "Upapattesiyena": "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော",
    "avaseso": "အကြွင်း", "anavaseso": "အကြွင်းမဲ့", "maraṇehi": "သေခြင်း", "jīvati": "အသက်ရှင်သည်",
    "jīvitehi": "အသက်",
    # ^5-539 the Samiddhi sutta
    "byākareyya": "ဖြေဆိုသည်", "byākaramāno": "ဖြေဆိုသော", "vedayati": "ခံစားသည်",
    "vedaniyaṃ": "ခံစားမှုကို ဖြစ်စေတတ်သော", "dukkhavedaniyaṃ": "နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော",
    "sukhavedaniyaṃ": "သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော", "āvuso": "ငါ့ရှင်", "āvuso pāṭaliputta": "ငါ့ရှင် ပါဋလိပုတ္တ",
    "sañcetaniyaṃ": "စေ့ဆော်၍", "puriso": ("ယောကျ်ား",), "samiddhi": "သမိဒ္ဓိ", "paribbājakassa": "ပရိဗ္ဗာဇ်",
    "potaliputtassa": NONE, "catubbidhā": "လေးမျိုးသော", "tividhā": "သုံးမျိုးသော", "udrayaṃ": "ဖြစ်ပေါ်စေသော",
    "sukhudrayaṃ": "ချမ်းသာကို ဖြစ်ပေါ်စေသော", "cetayitvā": "စေ့ဆော်၍",
    # ^5-546 Kammahetukathā
    "abbhācikkhati": "စွပ်စွဲ ပြောဆိုသည်", "abbhācikkhana": "စွပ်စွဲ ပြောဆိုခြင်း", "uppāda": "ထွက်စေခြင်း",
    "vāda": "ပြောခြင်း", "kāmesu": "ကာမ", "padesu": "ပုဒ်", "tathā": "ထို့အတူ",
}

T["17-navamavaggo"] = {
    # headings
    "dassāvī": "ရှုမြင်သော",
    "atītānāgata": "အတိတ်နှင့် အနာဂတ်", "atītānāgataṃ": "အတိတ်နှင့် အနာဂတ်",
    "anāgatārammaṇa": "အနာဂတ်ကို အာရုံပြုခြင်း", "anupatita": "တွဲဖက်နေခြင်း", "anupatitaṃ": "တွဲဖက်နေသော",
    "vitakkānupatita": "စတင်ကြံစည်မှုနှင့် တွဲဖက်နေခြင်း", "vitakkānupatitaṃ": "စတင်ကြံစည်မှုနှင့် တွဲဖက်နေသော",
    "vipphāra": "ပျံ့နှံ့ခြင်း", "vipphāro": "ပျံ့နှံ့ခြင်း", "vitakkavipphāra": "စတင်ကြံစည်မှု ပျံ့နှံ့ခြင်း",
    "Vitakkavipphāra": "စတင်ကြံစည်မှု ပျံ့နှံ့ခြင်း", "vitakkavipphāro": "စတင်ကြံစည်မှု ပျံ့နှံ့ခြင်း",
    "vitakkavipphāro saddo": "စတင်ကြံစည်မှု ပျံ့နှံ့ခြင်း … အသံ", "kāyakamma": "ကိုယ်ဖြင့် ပြုသော ကံ",
    "samannāgata": "ပြည့်စုံခြင်း",
    # ^5-547 the 26 aspects (my5 notes ch17-20: «မမြဲဟု၊ ဆင်းရဲဟု …»; «ဟု» goes, rule 9; a fragment that lost
    # its negative = the positive part, rule 8)
    "aniccato": "မမြဲ", "dukkhato": "ဆင်းရဲ", "rogato": "ရောဂါ", "gaṇḍato": "အနာ", "sallato": "ငြောင့်",
    "aghato": "ဒုက္ခ ဖိစီးမှု", "ābādhato": "ဖျားနာမှု", "parato": "သူစိမ်း", "palokato": "ပျက်စီးတတ်သော အရာ",
    "ītito": "ဘေးဒဏ်", "upaddavato": "ဥပဒ်", "bhayato": "ကြောက်ဖွယ်", "upasaggato": "ဘေးအန္တရာယ်",
    "calato": "လှုပ်ရှားတတ်သော အရာ", "pabhaṅguto": "ပြိုပျက်တတ်သော အရာ", "dhuvato": "ခိုင်မြဲသော အရာ",
    "tāṇato": "ကာကွယ်ရာ", "leṇato": "ပုန်းအောင်းရာ", "saraṇato": "ကိုးကွယ်ရာ", "rittato": "ဗလာ",
    "tucchato": "အနှစ်မဲ့", "attato": "အတ္တ", "ādīnavato": "အပြစ်",
    "vipariṇāmadhammato": "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော", "pahīyanti": "ပယ်ခံရသည်",
    # ^5-548
    "satataṃ": "အမြဲတမ်း", "samitaṃ": "အစဉ်တစိုက်", "abbokiṇṇaṃ": "ကြားမလပ်ဘဲ", "adhimuccamāno": "ဆုံးဖြတ်သော",
    "pariyogāhamāno": "သက်ဝင်သော", "sukhānupassī": "ချမ်းသာဟု အဖန်ဖန် ရှုသော",
    "sukhānupassī viharati": "ချမ်းသာဟု အဖန်ဖန် ရှုသော … နေသည်",
    # ^5-549 / ^5-550 Amatārammaṇakathā
    "amata": "အမြိုက်", "Amataṃ": "အမြိုက်", "amataṃ": "အမြိုက်",
    "dosaṭṭhāniyaṃ": "ဒေါသ ဖြစ်ကြောင်း", "kopaṭṭhāniyaṃ": "အမျက် ဖြစ်ကြောင်း", "kopa": "အမျက်",
    "mohaṭṭhāniyaṃ": "မောဟ ဖြစ်ကြောင်း", "aññāṇa": "မသိခြင်း", "ñāṇa": "သိခြင်း", "karaṇaṃ": "ပြုတတ်သော",
    "acakkhukaraṇaṃ": "မျက်စိ မမြင်ခြင်းကို ပြုတတ်သော", "nirodhiyaṃ": "ချုပ်ငြိမ်းစေတတ်သော", "vighāta": "ပင်ပန်းခြင်း",
    "pakkhiyaṃ": "ဘက်၌ ပါသော", "saṃvattaniyaṃ": "ပို့ဆောင်တတ်သော", "rajaniyaṃ": "တပ်မက်ဖွယ်ကောင်းသော",
    "kamaniyaṃ": "လိုချင်ဖွယ်ကောင်းသော", "madaniyaṃ": "မူးယစ်စေတတ်သော", "bandhaniyaṃ": "နှောင်ဖွဲ့တတ်သော",
    "mucchaniyaṃ": "တွေဝေစေတတ်သော", "saṃkilesiyaṃ": "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော",
    # ^5-551
    "sañjānāti": "မှတ်သိသည်", "sañjānitvā": "မှတ်သိ၍", "maññati": "ထင်မှတ်သည်", "abhinandati": "နှစ်သက်သည်",
    # ^5-554 … ^5-558 Anusayā / Ñāṇaṃ anārammaṇaṃ
    "kāmarāgapariyuṭṭhānaṃ": "ကာမရာဂ ထကြွခြင်း", "avijjogho": "အမှန်ကို မသိမှု ရေအလျဉ်",
    "avijjāyogo": "အမှန်ကို မသိမှု ထမ်းပိုး", "avijjāpariyuṭṭhānaṃ": "အမှန်ကို မသိမှု ထကြွခြင်း",
    "bhavarāga": "ဘဝရာဂ", "bhavarāgānusayo": "ဘဝရာဂ ကိန်းအောင်းခြင်း",
    "abyākate": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "abyākate citte": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော စိတ်", "vattamāne": "ဖြစ်နေသော",
    "paññavā": "ပညာ ရှိသော",
    # ^5-563 Vitakkavipphārasaddakathā
    "Sabbaso": "အခါခပ်သိမ်း", "sabbaso": "အခါခပ်သိမ်း", "vitakkayato": "စတင်ကြံစည်မှု ပြုနေသော",
    "vicārayato": "ဆက်လက်သုံးသပ်မှု ပြုနေသော", "phusayato": "တွေ့ထိနေသော", "vedayato": "ခံစားနေသော",
    "sañjānato": "မှတ်သိနေသော", "cetayato": "စေ့ဆော်နေသော", "sarato": "အောက်မေ့နေသော",
    "pajānato": "ပိုင်းခြား သိနေသော",
    # ^5-564 … ^5-567 Na yathācittassa vācā / kāyakammaṃ
    "kāmo": "လို", "katheti": "ပြောဆိုသည်", "ālapati": "ခေါ်ပြောသည်", "voharati": "သုံးနှုန်းပြောသည်",
    "kathessāmi": "ပြောဆိုသည်", "ālapissāmi": "ခေါ်ပြောသည်", "voharissāmi": "သုံးနှုန်းပြောသည်",
    "jātā": "ပေါ်ပေါက်သော", "uppādā": "ဖြစ်ပေါ်သော", "uppādaṃ": "ဖြစ်ပေါ်သော", "paṇidahantassa": "ဆု တောင်းသော",
    "ābhogassa": "စိတ် ညွတ်သော", "phassakassa": "တွေ့ထိမှု ရှိသော", "vedanakassa": "ခံစားမှု ရှိသော",
    "saññakassa": "မှတ်သိမှု ရှိသော", "cetanakassa": "စေ့ဆော်မှု ရှိသော", "āvaṭṭentassa": "စိတ်ကို လှည့်ဆောင်သော",
    "gacchati": "သွားသည်", "pasāressāmi": "ဆန့်သည်",
    # ^5-568 / ^5-569 Atītānāgatasamannāgatakathā
    "ajātaṃ": "မဖြစ်သေးသော", "sañjātaṃ": "ဖြစ်ပေါ်သော", "nibbattaṃ": "ဖြစ်မြောက်သော",
    "abhinibbattaṃ": "ထင်ရှားစွာ ဖြစ်မြောက်သော", "pātubhūtaṃ": "ထင်ရှား ပေါ်ပေါက်သော", "vigataṃ": "ကင်းကွာပြီးသော",
    "vipariṇataṃ": "ဖောက်ပြန်ပြောင်းလဲပြီးသော", "atthaṅgataṃ": "ကွယ်ပြီးသော", "abbhatthaṅgataṃ": "လုံးဝ ကွယ်ပြီးသော",
    "Catupaññāsa": "ငါးဆယ့်လေးပါး", "Chasaṭṭhi": "ခြောက်ဆယ့်ခြောက်ပါး", "atītehi": "အတိတ်", "khandhehi": "အစုအဝေး",
    # ^5-570
    "jhāyī": "ဈာန်ဝင်သော", "lābhī": "ရသော",
}

T["18-dasamavaggo"] = {
    # headings
    "Nirodhakathā": "ချုပ်ငြိမ်းခြင်းအကြောင်း ဆွေးနွေးချက်", "ābhoga": "စိတ်ညွတ်ခြင်း", "sīlehi": "သီလ",
    "cetasika": "စိတ်၏ အဖော်", "samādāna": "ဆောက်တည်ခြင်း", "Samādāna": "ဆောက်တည်ခြင်း",
    "samādānahetu": "ဆောက်တည်ခြင်းကြောင့်", "Samādānahetukaṃ": "ဆောက်တည်ခြင်းကြောင့် ဖြစ်သော",
    "samādānahetukaṃ": "ဆောက်တည်ခြင်းကြောင့် ဖြစ်သော",
    "samādānahetukaṃ sīlaṃ": "ဆောက်တည်ခြင်းကြောင့် ဖြစ်သော သီလ",
    "dussilya": "သီလ ပျက်ခြင်း", "Dussilyaṃ": "သီလ ပျက်ခြင်း", "dussilyaṃ": "သီလ ပျက်ခြင်း", "sīlya": "သီလ",
    "Aviññatti": "ထုတ်ဖော်ပြသမှု မဟုတ်သော အရာ", "aviññatti": "ထုတ်ဖော်ပြသမှု မဟုတ်သော အရာ",
    # ^5-571 … ^5-577
    "khandhe": "အစုအဝေး", "Dasannaṃ": "ဆယ်ပါး", "Mato": "သေပြီးသော", "kālaṅkato": "ကွယ်လွန်ပြီးသော",
    "purejāta": "ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော", "manasikārā": "နှလုံး သွင်း", "samannāhārā": "စိတ်ကို ဆောင်ခြင်း",
    "ābhogā": "စိတ်ညွတ်ခြင်း", "visayaṃ": "နယ်ပယ်", "anubyañjana": "အသေးစိတ်",
    "ābhogaṃ": "စိတ်ညွတ်ခြင်း", "sābhogaṃ": "စိတ်ညွတ်ခြင်း ရှိသော",
    "Cakkhuviññāṇaṃ sābhogaṃ": "မျက်စိ သိစိတ်သည် စိတ်ညွတ်ခြင်း ရှိသော",
    # ^5-587 … ^5-589 Dvīhisīlehikathā
    "phassehi": "တွေ့ထိမှု", "saddhāhi": "ယုံကြည်မှု", "cetanāhi": "စေ့ဆော်မှု", "satīhi": "သတိ",
    "samādhīhi": "သမာဓိ", "paññāhi": "ပညာ", "Maggasamaṅgī samannāgato": "မဂ်နှင့် ပြည့်စုံသော … ပြည့်စုံသော",
    "khaṇḍa": "ကျိုးသော",
    # ^5-591 … ^5-596
    "iṭṭha": "လိုလားအပ်သော", "Aniṭṭha": "မလိုလားအပ်သော", "iṭṭhaphalaṃ": "လိုလားအပ်သော အကျိုး ရှိသော",
    "anuparivattī": "နောက်သို့ လိုက်ပါသော", "cittānuparivattī": "စိတ်နောက်သို့ လိုက်ပါသော",
    # ^5-598 … ^5-600 Samādānahetukathā
    "viya": "ကဲ့သို့", "muñja": "ဖြူဆံမြက်", "māluvā": "နွယ်ကြီး", "vidūrāni": "ဝေးကွာသော အရာ",
    "asabbhi": "သူတော်ကောင်း မဟုတ်သူ", "anavajjā": "အပြစ် မရှိသော", "Nabhaṃ": "ကောင်းကင်",
    "vitakkentassa": "စတင်ကြံစည်မှုကို ပြုနေသော", "samādiyitvā": "ဆောက်တည်၍", "gāmino": "သွားသော",
    "sampannā": "ပြည့်စုံသော", "ṭhā": "တည်သော", "sagga": "နတ်ပြည်", "janā": "လူ", "ārāma": "ဥယျာဉ်",
    # ^5-601 … ^5-604 Viññatti sīlaṃ / Aviññatti dussilyaṃ
    "pamādaṭṭhānā": "မေ့လျော့ခြင်း၏ အကြောင်း", "pamādaṭṭhānaṃ": "မေ့လျော့ခြင်း၏ အကြောင်း",
    "merayamajja": "အရက် မူးယစ်ဖွယ်", "Abhivādanaṃ": "ရှိခိုးခြင်း", "paccuṭṭhānaṃ": "ထ၍ ကြိုဆိုခြင်း",
    "añjali": "လက်အုပ်", "añjalikammaṃ": "လက်အုပ်ချီခြင်း", "sāmīci": "ရိုသေစွာ", "parikammaṃ": "ပွတ်တိုက်ပေးခြင်း",
    "nhāne": "ရေချိုးရာ", "pādakathalikā": "ခြေသုတ်ခုံ", "abhihāro": "ဆောင်ပေးခြင်း", "āsana": "နေရာ",
    "apuññaṃ": "မကောင်းမှု", "puññaṃ": "ကောင်းမှု", "dadantassa": "ပေးသော", "Niyāma": "သေချာသော လမ်းကြောင်း",
    "paṇṇāsako": "ငါးဆယ်အစု", "viññattisīlaṃ": "ထုတ်ဖော်ပြသမှုသည် သီလ", "samādinno": "ဆောက်တည်ခဲ့ပြီးသော",
}

T["19-ekadasamavaggo"] = {
    # headings
    "anusaya": "ကိန်းအောင်းခြင်း", "Ñāṇakathā": "ဉာဏ်အကြောင်း ဆွေးနွေးချက်",
    "Ñāṇakathā niṭṭhitā": "ဉာဏ်အကြောင်း ဆွေးနွေးချက် ပြီးဆုံးသော",
    "Ñāṇaṃ cittavippayutta": "ဉာဏ် … စိတ်နှင့် ကင်းကွာသော", "bala": "စွမ်းအား", "iddhibala": "ဣဒ္ဓိ စွမ်းအား",
    "ṭhitatā": "တည်နေခြင်း သဘော", "dhammaṭṭhitatā": "သဘောတရားတို့၏ တည်နေခြင်း သဘော",
    "Dhammaṭṭhitatā": "သဘောတရားတို့၏ တည်နေခြင်း သဘော",
    # ^5-605 … ^5-612 the three Anusayakathās
    "paṭighapariyuṭṭhānaṃ": "မုန်းတီးမှု ထကြွခြင်း", "mānapariyuṭṭhānaṃ": "မာန ထကြွခြင်း",
    "vicikicchāpariyuṭṭhānaṃ": "ယုံမှားမှု ထကြွခြင်း", "bhavarāgapariyuṭṭhānaṃ": "ဘဝရာဂ ထကြွခြင်း",
    "diṭṭhipariyuṭṭhānaṃ": "အယူ ထကြွခြင်း", "hetunā": "အမြစ်",
    # ^5-613 … ^5-620 Ñāṇa- / Idaṃ dukkhanti-kathā
    "kilese": "ကိလေသာ", "mohe": "မောဟ", "Dose": "ဒေါသ", "Rāge": "ရာဂ", "vigate": "ကင်းသွားသော",
    "ñāṇe": "သိခြင်း", "Aññāṇe": "မသိခြင်း", "aññāṇe": "မသိခြင်း", "ñāṇavippayutte": "ဉာဏ်နှင့် ကင်းကွာသော",
    "niruddhena": "ချုပ်ငြိမ်းပြီးသော", "paṭipassaddhena": "ငြိမ်းအေးပြီးသော", "dissati": "ထင်ရသည်",
    "pavattati": "ဖြစ်ပွားသည်", "bhāsato": "ပြောနေသော", "vācaṃ bhāsato": "စကား ပြောနေသော", "kha": "ခ",
    # ^5-621 … ^5-624 Iddhibalakathā
    "attabhāvappaṭilābho": "ကိုယ်ခန္ဓာ ရရှိခြင်း", "bhāva": ("သဘော", NONE), "mato": "သေပြီးသော",
    "kappaṃ": "ကမ္ဘာ", "tiṭṭheyya": "တည်နေသည်", "Iddhibalena": "ဣဒ္ဓိ စွမ်းအား", "iddhibalena": "ဣဒ္ဓိ စွမ်းအား",
    "balena": "စွမ်းအား", "avasese": "အကြွင်း", "avasesaṃ": "အကြွင်း",
    "jīriṃsu": "အိုသည်", "jāyiṃsu": "ဖြစ်သည်", "nirujjhi": "ချုပ်ငြိမ်းသည်", "mīyiṃsu": "သေသည်",
    "byādhiyiṃsu": "နာသည်", "jīrī": "အိုသည်", "mīyī": "သေသည်", "byādhiyī": "နာသည်", "mā": "မ", "jāti": "ဖြစ်ခြင်း",
    "niccaṃ": ("မြဲသော", "မြဲ"), "iddhiyā paggahetuṃ": "ဣဒ္ဓိဖြင့် ထိန်းထား",
    "bahulīkatā": "အဖန်ဖန် ပြုထားသော",
    "yānīkatā": "ယာဉ်ကဲ့သို့ ပြုထားသော", "anuṭṭhitā": "အမြဲ လေ့ကျင့်ထားသော",
    "paricitā": "ကျွမ်းဝင်အောင် ပြုထားသော", "samāraddhā": "အားထုတ်ထားသော", "yassa kassaci": "မည်သူမဆို",
    "ākaṅkhamāno": "အလိုရှိသော", "pāṭibhogo": "အာမခံနိုင်သူ", "māro": "မာရ်", "brahmā": "ဗြဟ္မာ", "māro vā brahmā": "မာရ် … ဗြဟ္မာ",
    "jarāmaraṇiyāni": "အိုခြင်း သေခြင်းကို ဖြစ်စေတတ်သော",
    "dukkhavipākāni jātijarāmaraṇiyāni": "ဆင်းရဲ အကျိုး ရှိသော … ဖြစ်ခြင်း အိုခြင်း သေခြင်းကို ဖြစ်စေတတ်သော",
    "saṃkilesikāni": "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော", "darāni": "ပူပန်ဖွယ်", "sadarāni": "ပူပန်ဖွယ် ရှိသော",
    "katāni": "ပြုခဲ့သော", "bhavikāni": "ဘဝ", "ponobbhavikāni": "ဘဝသစ်ကို ဖြစ်စေတတ်သော",
    # ^5-625 / ^5-626 Samādhikathā
    "santati": "အစဉ်", "Cittasantati": "စိတ်အစဉ်", "cittasantati": "စိတ်အစဉ်", "pahomi": "နိုင်သည်",
    "viharituṃ": "နေ", "iñjamāno": "လှုပ်ရှားသော", "bhāsamāno": "ပြောသော", "rattindivāni": "ရက် … ညဉ့်",
    "ekanta": "တစ်ထစ်ချ", "rāgasahagatacittasamaṅgī": "ရာဂနှင့်အတူ ဖြစ်သော စိတ်နှင့် ပြည့်စုံသော",
    "khaṇiko": "ခဏ၌သာ ဖြစ်သော", "cittakkhaṇiko": "စိတ် … ခဏ၌သာ ဖြစ်သော",
    "Ekacittakkhaṇiko": "စိတ် တစ်ခဏ၌သာ ဖြစ်သော",
    # ^5-627 … ^5-629 Dhammaṭṭhitatā- / Aniccatākathā
    "viññāṇassa": "သိစိတ်", "dukkhassantakiriyā": "ဒုက္ခ၏ အဆုံးကို ပြုခြင်း", "Tāya tāyeva": "ထိုထိုအရာ၏ပင်",
    "saṅkhārānaṃ": "ပြုပြင်ဖန်တီးမှု", "Aniccatā": "မမြဲခြင်း သဘော", "bhedo": "ပြိုပျက်ခြင်း", "yattha": "အကြင်",
}

# ^5-630 / ^5-631 the faculties' restraint «Xindriyasaṃvaro Xkammaṃ» (the text: «X၏ စွမ်းရည်၌ စောင့်စည်းမှုသည် Xဖြင့်
# ပြုသော ကံ»)
_FAC = {"cakkhu": ("Cakkhu", "မျက်စိ"), "sot": ("Sot", "နား"), "ghān": ("Ghān", "နှာခေါင်း"), "jivh": ("Jivh", "လျှာ"),
        "kāy": ("Kāy", "ကိုယ်"), "man": ("Man", "မနော")}
_KAMMA = {"cakkhu": "cakkhukammaṃ", "sot": "sotakammaṃ", "ghān": "ghānakammaṃ", "jivh": "jivhākammaṃ",
          "kāy": "kāyakammaṃ", "man": "manokammaṃ"}
T_FAC = {}
for _st, (_St, _my) in _FAC.items():
    for _neg, _w in (("", "စောင့်စည်းမှု"), ("a", "မစောင့်စည်းမှု")):
        for _x in (_st, _St):
            _k = f"{_x}{'u' if _st == 'cakkhu' else ''}ndriya{_neg}saṃvaro".replace("cakkhuundriya", "cakkhundriya") \
                .replace("Cakkhuundriya", "Cakkhundriya").replace("Cakkhuu", "Cakkhu")
            _k = _k.replace("sotndriya", "sotindriya").replace("Sotndriya", "Sotindriya") \
                .replace("ghānndriya", "ghānindriya").replace("Ghānndriya", "Ghānindriya") \
                .replace("jivhndriya", "jivhindriya").replace("Jivhndriya", "Jivhindriya") \
                .replace("kāyndriya", "kāyindriya").replace("Kāyndriya", "Kāyindriya") \
                .replace("manndriya", "manindriya").replace("Manndriya", "Manindriya")
            T_FAC[_k] = f"{_my}၏ စွမ်းရည်၌ {_w}"
            T_FAC[f"{_k} {_KAMMA[_st]}"] = f"{_my}၏ စွမ်းရည်၌ {_w}သည် {_my}ဖြင့် ပြုသော ကံ"
    T_FAC[_KAMMA[_st]] = f"{_my}ဖြင့် ပြုသော ကံ"
    T_FAC[_St.lower() + ("" if _st == "cakkhu" else "i") + "ndriya" if _st != "cakkhu" else "cakkhundriya"] = \
        f"{_my}၏ စွမ်းရည်"

T["20-dvadasamavaggo"] = dict(T_FAC, **{
    # headings
    "upapajjeyya": ("ရောက်သည်",), "Kammakathā": "ကံအကြောင်း ဆွေးနွေးချက်", "kolaṅkola": "အမျိုးမှ အမျိုးသို့ ကူးသူ",
    "kolaṅkolo": "အမျိုးမှ အမျိုးသို့ ကူးသူ", "ekabījī": "မျိုးစေ့ တစ်စေ့သာ ရှိသူ",
    "sattakkhattuparamo": "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ", "voropana": "သတ်ခြင်း",
    "Jīvitā voropana": "အသက်မှ သတ်ခြင်း", "voropanakathā": "သတ်ခြင်းအကြောင်း ဆွေးနွေးချက်", "du": "ဆိုးသော",
    "Duggatikathā": "ဆိုးသော လားရာအကြောင်း ဆွေးနွေးချက်", "bhavika": "ဘဝ၌ ရှိသော", "sattama": "ခုနစ်ကြိမ်မြောက်",
    "sattamabhavika": "ခုနစ်ကြိမ်မြောက် ဘဝ၌ ရှိသော", "bhavikassa": "ဘဝ၌ ရှိသော",
    "sattamabhavikassa": "ခုနစ်ကြိမ်မြောက် ဘဝ၌ ရှိသော",
    # ^5-630 … ^5-637 Saṃvaro kammaṃ, Kammakathā, Saddo vipāko …
    "Asaṃvaro": "မစောင့်စည်းမှု", "asaṃvaro": "မစောင့်စည်းမှု",
    "Kiriyābyākatā": "ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "Vipākābyākatā": "ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "katānaṃ": "ပြုခဲ့", "upacitānaṃ": "ဆည်းပူးခဲ့သော", "paṭisaṃviditvā": "ခံစားရ၍",
    "pariyāye": "အလှည့်", "upapajje": "နောက်ဘဝ", "vedaniyo": "ခံစားမှုကို ဖြစ်စေတတ်သော",
    "dukkhavedaniyo": "နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော", "Sukhavedaniyo": "သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော",
    "ussannattā": "များပြားခြင်း", "vipulattā": "ကြွယ်ဝခြင်း", "karavika": "ကရဝိက်ငှက်", "bhāṇī": "ပြောဆိုသော",
    "saro": "အသံ", "dīghanikāye": "“ဒီဃနိကာယ်”",
    # ^5-641 … ^5-647 the niyāma of the stream-enterer types
    "Abhabbo": "မထိုက်တန်သော", "abhisametuṃ": "ထိုးထွင်း သိမြင်ရန်",
    "sattakkhattuparamatāniyato": "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ၏ အဖြစ်၌ ကျိန်းသေသော",
    "saṅgho bhinno": "သံဃာ … ကွဲပြားစေခံရသော", "bhinno": "ကွဲပြားစေခံရသော", "niyamo": "ကျိန်းသေမှု",
    "niyamena": "ကျိန်းသေမှု", "balā": "စွမ်းအား", "okkamanti": "သက်ဆင်းသည်",
    "niyāmaṃ okkamanti": "သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းသည်",
    "kolaṅkolatāniyato": "အမျိုးမှ အမျိုးသို့ ကူးသူ၏ အဖြစ်၌ ကျိန်းသေသော",
    "ekabījitāniyato": "မျိုးစေ့ တစ်စေ့သာ ရှိသူ၏ အဖြစ်၌ ကျိန်းသေသော",
    # ^5-648 … ^5-653 Jīvitā voropana-, Duggati-, Sattamabhavikakathā
    "arahantaṃ": "ရဟန္တာ", "voropeyya": "သတ်သည်", "sañcicca": "ရည်ရွယ်၍", "gāravo": "ရိုသေသော",
    "sagāravo": "ရိုသေသော", "saṅghaṃ bhindeyya": "သံဃာကို ခွဲသည်", "sikkhāya": "သိက္ခာ",
    "ativattati": "ကျော်လွန်သည်", "atikkamanti": "ကျော်လွန်သည်", "ohadeyya": "ကျင်ကြီး စွန့်သည်",
    "omutteyya": "ကျင်ငယ် စွန့်သည်", "niṭṭhubheyya": "တံတွေး ထွေးသည်", "thūpe": "စေတီ", "apabyāmato": "လက်ဝဲ ထား၍",
    "paññattaṃ": "သတ်မှတ်ထားသော", "velaṃ": "ကမ်းစပ်", "ṭhita": "တည်မြဲသော", "paṭiseveyya": "မှီဝဲသည်",
    "methunaṃ dhammaṃ": "မေထုန် အကျင့်", "kaññāya": "သတို့သမီး", "amanussa": "လူ မဟုတ်သော",
    "tiracchānagata": "တိရစ္ဆာန်", "eḷakaṃ": "သိုး", "sūkaraṃ": "ဝက်", "vaḷavaṃ": "မြင်းမ", "assa": "မြင်း",
    "tittira": "ခါ", "vaṭṭaka": "ငုံး", "mora": "ဒေါင်း", "kapiñjaraṃ": "ငှက်ကြီး", "paṭiggaṇheyya": "ခံယူသည်",
    "tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya": "ခါ … ငှက်ကြီးတို့ကို ခံယူသည်",
    "sampannassa": "ပြည့်စုံသော", "Diṭṭhisampannassa": "အယူ ပြည့်စုံသော", "diṭṭhisampannassa": "အယူ ပြည့်စုံသော",
    "Diṭṭhisampanno": "အယူ ပြည့်စုံသော", "duggati": "ဆိုးသော လားရာ",
    "Diṭṭhisampannassa pahīnā duggati": "အယူ ပြည့်စုံသော … ဆိုးသော လားရာကို ပယ်ပြီးသော", "rajjeyya": "တပ်မက်သည်",
    "āpāyike": "အပါယ်နှင့် ဆိုင်သော", "tiracchānayoniṃ": "တိရစ္ဆာန် ဘဝ", "yoniṃ": "ဘဝ",
    "kathāyaṃ": "ဆွေးနွေးချက်", "duggatikathāyaṃ": "ဆိုးသော လားရာအကြောင်း ဆွေးနွေးချက်", "lakkhaṇaṃ": "အမှတ်အသား",
    "dissanti": "ထင်ရသည်",
})

T["21-terasamavaggo"] = {
    # headings
    "kappa": "ကမ္ဘာ", "ṭha": "တည်ရမည့်", "ṭho": "တည်ရမည့်", "Kappaṭṭho": "ကမ္ဘာ ပတ်လုံး တည်ရမည့်သူ",
    "kappaṭṭho": "ကမ္ဘာ ပတ်လုံး တည်ရမည့်သူ", "Kusalapaṭilābhakathā": "ကုသိုလ်ကို ရခြင်းအကြောင်း ဆွေးနွေးချက်",
    "paṭilābha": "ရခြင်း", "payutta": "ကံကို ပြုခဲ့သော", "payutto": "ကံကို ပြုခဲ့သော",
    "Anantarāpayutto puggalo": "ချက်ချင်း အကျိုးပေးသော ကံကို ပြုခဲ့သော ပုဂ္ဂိုလ်",
    "anantarāpayutto puggalo": "ချက်ချင်း အကျိုးပေးသော ကံကို ပြုခဲ့သော ပုဂ္ဂိုလ်",
    "nivuta": "အတားအဆီး ဖုံးလွှမ်းထားသော", "Nivuto": "အတားအဆီး ဖုံးလွှမ်းထားသော",
    "nivuto": "အတားအဆီး ဖုံးလွှမ်းထားသော", "sammukhībhūta": "မျက်နှာချင်းဆိုင် ဖြစ်နေသော",
    "Sammukhībhūto": "မျက်နှာချင်းဆိုင် ဖြစ်နေသော", "sammukhībhūto": "မျက်နှာချင်းဆိုင် ဖြစ်နေသော",
    "assādeti": "သာယာသည်", "Samāpanno assādeti": "သမာပတ်ကို ဝင်စားနေသော … သာယာသည်",
    "samāpanno assādeti": "သမာပတ်ကို ဝင်စားနေသော … သာယာသည်", "asāta": "မသာယာဖွယ်",
    "Dhammataṇhā": "သဘောတရားကို တပ်မက်မှု", "dhammataṇhā": "သဘောတရားကို တပ်မက်မှု",
    "Rūpataṇhā": "အဆင်းအရောင်ကို တပ်မက်မှု", "Saddataṇhā": "အသံကို တပ်မက်မှု", "gandhataṇhā": "အနံ့ကို တပ်မက်မှု",
    "rasataṇhā": "အရသာကို တပ်မက်မှု", "phoṭṭhabbataṇhā": "အထိအတွေ့ကို တပ်မက်မှု",
    # ^5-654 … ^5-659 Kappaṭṭha- / Kusalapaṭilābhakathā
    "kālaṃ karoti": "သေသည်", "vehāsaṃ": "ကောင်းကင်", "Mato": "သေသော",
    "paṭiññā": "ဝန်ခံချက်", "vādissa": "တစ်ဖက်သား", "ḍayhante": "မီးလောင်သော", "vepakkaṃ": "အကျိုးပေးသော",
    "Āpāyiko": "အပါယ်သို့ ရောက်သော", "nerayiko": "ငရဲ၌ ကျသော", "rato": "မွေ့လျော်သော", "khemā": "လွတ်ငြိမ်းရာ",
    "padhaṃsati": "ပျက်စီးသည်", "samaggaṃ": "ညီညွတ်သော", "bhedako": "သင်းခွဲသူ", "paccati": "ပူလောင်ရသည်",
    "piṇḍapātaṃ": "ဆွမ်း", "cīvaraṃ": "သင်္ကန်း", "khādanīyaṃ": "ခဲဖွယ်",
    "bhojanīyaṃ": "ဘောဇဉ်", "pānīyaṃ": "သောက်ရေ", "cetiyaṃ": "စေတီ", "vandeyya": "ရှိခိုးသည်", "mālaṃ": "ပန်း",
    "gandhaṃ": "နံ့သာ", "vilepanaṃ": "နံ့သာပျောင်း", "abhidakkhiṇaṃ": "လက်ယာရစ်", "paṭilabheyya": "ရသည်",
    "vuṭṭhānaṃ": "ထမြောက်ရန်",
    # ^5-660 … ^5-664 Anantarāpayutta- / Niyatassa niyāmakathā
    "uppāditaṃ": ("ဖြစ်ပေါ်စေခဲ့ပြီးသော", "ထွက်စေအပ်သော"), "janitaṃ": "ဖြစ်စေခဲ့ပြီးသော",
    "vippaṭisāriyaṃ": "စိတ် ပူလောင်မှု", "okkameyya": "သက်ဆင်းသည်", "okkamati": "သက်ဆင်းသည်",
    "okkamituṃ": "မသက်ဆင်းနိုင်", "niyāmaṃ okkamituṃ": "သေချာသော လမ်းကြောင်းသို့ မသက်ဆင်းနိုင်",
    "paṭisaṃharitvā": "ပြန်ရုပ်သိမ်း၍", "paṭivinetvā": "ဖယ်ရှား၍", "paṭivinodetvā": "ပယ်ဖျောက်၍",
    "pacchā": "နောက်မှ", "Niyato": "လမ်းကြောင်း သေချာပြီးသော", "niyato": ("လမ်းကြောင်း သေချာပြီးသော", "ကျိန်းသေသော"),
    "sammattaniyato": "မှန်ကန်မှု၌ လမ်းကြောင်း သေချာပြီးသော",
    "Micchattaniyato": "မှားယွင်းမှု၌ လမ်းကြောင်း သေချာပြီးသော", "sotāpattimaggaṃ": "သောတာပတ္တိမဂ်",
    "bodhisatto": "ဘုရားလောင်း",
    # ^5-665 … ^5-670 Nivuta- / Sammukhībhūtakathā
    "Ratto": "တပ်မက်နေသော", "duṭṭho": "ဒေါသ ဖြစ်နေသော", "mūḷho": "တွေဝေနေသော", "kiliṭṭho": "ညစ်နွမ်းနေသော",
    "patte": "ရောက်သော", "aṅgaṇe": "အမည်းအစက်",
    # ^5-671 … ^5-675 Samāpanno assādeti-, Asātarāgakathā
    "ceteti": "စေ့ဆော်သည်", "vicāreti": "ဆက်လက်သုံးသပ်သည်", "piyāyati": "နှစ်သက်သည်",
    "sarati": "အောက်မေ့သည်", "vitakkena": "စတင်ကြံစည်မှု",
    "jhānanikanti": "ဈာန်ကို စွဲလန်းခြင်း", "nikāmeti": "နှစ်သက်တောင့်တသည်", "vittiṃ": "နှစ်သိမ့်မှု",
    "abhinandino": "နှစ်သက်သော", "patthenti": "တောင့်တသည်", "esanti": "ရှာသည်", "gavesanti": "ရှာဖွေသည်",
    "pariyesanti": "စုံစမ်းရှာဖွေသည်", "anurodha": "လိုက်လျောခြင်း", "virodhaṃ": "ဆန့်ကျင်ခြင်း",
    "abhivadati": "ချီးမွမ်းသည်", "mahā": "မဟာ", "saṅkhaye": "သင်္ခယ",
    # ^5-676 … ^5-683 Dhammataṇhā abyākatā-, Dhammataṇhā na dukkhasamudayokathā
    "lobho": "လောဘ", "abhinandinī": "အလွန် နှစ်သက်တတ်သော", "bhavikā": "ဘဝ", "pono": "သစ်",
    "ponobbhavikā": "ဘဝသစ်ကို ဖြစ်စေတတ်သော",
}

T["22-cuddasamavaggo"] = {
    # headings
    "paṭisandahana": "ဆက်စပ်ခြင်း", "uppatti": "ဖြစ်ပေါ်ခြင်း", "anantara": "ချက်ချင်း နောက်၌ ဖြစ်စေသော",
    "anantarapaccaya": "ချက်ချင်း နောက်၌ ဖြစ်စေသော အကြောင်း", "ariyarūpa": "အရိယာ ရုပ်",
    "Ariyarūpaṃ": "အရိယာ ရုပ်", "ariyarūpaṃ": "အရိယာ ရုပ်",
    # ^5-686 … ^5-690 Kusalākusalapaṭisandahanakathā
    "paṭisandahati": "ဆက်စပ်သည်", "Akusalamūlaṃ": "အကုသိုလ်၏ အမြစ်", "akusalamūlaṃ": "အကုသိုလ်၏ အမြစ်",
    "Kusalamūlaṃ": "ကုသိုလ်၏ အမြစ်", "kusalamūlaṃ": "ကုသိုလ်၏ အမြစ်", "paṭighassa": "မုန်းတီးမှု",
    "aratiyā": "မမွေ့လျော်မှု", "avihiṃsā": "မညှဉ်းပန်းခြင်း", "abyāpāda": "မဖျက်ဆီးလိုခြင်း",
    "karuṇāya": "ကရုဏာ", "upekkhāya": "ဥပေက္ခာ", "muditāya": "မုဒိတာ", "mettāya": "မေတ္တာ",
    "virajjati": "တပ်မက်မှု ကင်းသည်", "rajjati": "တပ်မက်သည်", "vatthusmiṃ": "အရာဝတ္ထု",
    # ^5-691 / ^5-692 Saḷāyatanuppattikathā
    "kaṇṇo": "နား", "pādā": "ခြေ", "hatthā": "လက်", "sīsaṃ": "ဦးခေါင်း", "mukhaṃ": "ပါးစပ်", "nāsikā": "နှာခေါင်း",
    "hīna": ("ယုတ်ညံ့သော", "ချို့ယွင်းသော"), "paccaṅgī": "ကြီးငယ် အင်္ဂါ … ပြည့်စုံသော", "saṇṭhāti": "တည်သည်",
    "kucchismiṃ": "ဝမ်း", "kalalaṃ": "အရည်ကြည်", "abbudaṃ": "အမြှုပ်", "pesi": "အသားစ", "ghano": "အခဲ",
    "pasākhā": "အကိုင်းအခက်", "jāyate": "ဖြစ်ပေါ်သည်", "nibbattate": "ဖြစ်လာသည်", "aṭṭhī": "အရိုး",
    "pānaṃ": "အဖျော်", "annaṃ": "အစာ", "bhojanaṃ": "ဘောဇဉ်", "bhuñjati": "စားသည်", "naro": "လူ",
    "yāpeti": "အသက် မွေးသည်", "gatassa": "ရောက်ပြီးသော", "Mātukucchigatassa": "အမိဝမ်း၌ ရောက်ပြီးသော",
    "paṭilābhāya": "ရရှိရန်",
    # ^5-693 … ^5-697 Anantarapaccayakathā
    "pañcaviññāṇā": "သိစိတ် ငါးပါး", "naccati": "ကသည်", "gāyati": "သီဆိုသည်", "vādeti": "တီးမှုတ်",
    # ^5-701 … ^5-709
    "Pariyuṭṭhito": "ထကြွခြင်း ရှိသော", "Samāpattesiyo": "သမာပတ်ကို ရှာသော", "samāpattesiyo": "သမာပတ်ကို ရှာသော",
    "upapattesiyo": "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော", "esiyo": "ရှာသော", "diṭṭhadhamma": "ယခုဘဝ",
    "sukhavihāro": "ချမ်းသာစွာ နေခြင်း", "vihāro": "နေခြင်း", "samāpatti": "သမာပတ်", "jāto": "ပေါ်ပေါက်သော",
    "diṭṭhadhammasukhavihārena cittena": "ယခုဘဝ၌ ချမ်းသာစွာ နေခြင်း ဖြစ်သော စိတ်",
    "samāpattesiyena cittena": "သမာပတ်ကို ရှာသော စိတ်", "Rūparāgo": "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ",
    "rūparāgo": "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ", "Arūparāgo": "ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ",
    "arūparāgo": "ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ", "Gandharāgo": "အနံ့ကို တပ်မက်သော ရာဂ",
    "Saddarāgo": "အသံကို တပ်မက်သော ရာဂ", "rasarāgo": "အရသာကို တပ်မက်သော ရာဂ",
    "phoṭṭhabbarāgo": "အထိအတွေ့ကို တပ်မက်သော ရာဂ", "anuseti": "ကိန်းအောင်းသည်",
    "rūpadhātuṃ": "သိမ်မွေ့သော ရုပ် ဓာတ်", "saddadhātuṃ": "အသံ ဓာတ်", "arūpadhātuṃ": "ရုပ်မရှိသော ဓာတ်",
    "kāmadhātuṃ": "ကာမ ဓာတ်", "vadāmi": "ဟောသည်", "gatīnaṃ": "လားရာ", "vajjāni": "အပြစ်", "paramāni": "အကြီးဆုံး",
    "vuttāni": "ဟောတော်မူသည်", "vaccha": "ဝစ္ဆ", "samattaṃ": "ပြည့်စုံစွာ", "samādinnaṃ": "ဆောက်တည်ထားသော",
    "micchādiṭṭhikassa": "မှားယွင်းသော အယူ ရှိသော", "aniṭṭhāya": "မလိုလားဖွယ်ရာ", "akantāya": "မနှစ်သက်ဖွယ်ရာ",
    "amanāpāya": "စိတ် မတွေ့ဖွယ်ရာ", "ahitāya": "အစီးအပွား မဖြစ်ဖွယ်ရာ", "anantavā": "အဆုံး မရှိသော",
    "sotāpattimaggo": "သောတာပတ္တိမဂ်", "sakadāgāmimaggo": "သကဒါဂါမိမဂ်", "anāgāmimaggo": "အနာဂါမိမဂ်",
    "arahattamaggo": "ရဟန္တာ မဂ်", "sotāpattiphalaṃ": "သောတာပတ္တိဖိုလ်", "sakadāgāmiphalaṃ": "သကဒါဂါမိဖိုလ်",
    "anāgāmiphalaṃ": "အနာဂါမိဖိုလ်", "arahattaphalaṃ": "ရဟန္တာ ဖိုလ်", "bojjhaṅgo": "ဗောဇ္ဈင်",
}

_SVN = "မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ"
T["23-pannarasamavaggo"] = {
    # headings
    "paccayatā": "အကြောင်းဖြစ်ပုံ", "Paccayatā": "အကြောင်းဖြစ်ပုံ", "vavatthitā": "ပိုင်းခြား သတ်မှတ်ပြီးသော",
    "Aññamaññapaccayakathā": "အချင်းချင်း အကြောင်း ဖြစ်ခြင်းအကြောင်း ဆွေးနွေးချက်", "aññamañña": "အချင်းချင်း",
    "aññamaññapaccaya": "အချင်းချင်း အကြောင်း ဖြစ်ခြင်း", "laya": "အခိုက်အတန့်", "layo": "အခိုက်အတန့်",
    "khaṇa": "ခဏ", "Khaṇo": "ခဏ", "khaṇo": "ခဏ", "muhutta": "မုဟုတ်ကာလ", "muhuttaṃ": "မုဟုတ်ကာလ",
    "vedayita": "ခံစားရခြင်း", "saññāvedayita": "မှတ်သိမှုနှင့် ခံစားရခြင်း",
    "Saññāvedayitakathā": f"{_SVN} ဈာန်အကြောင်း ဆွေးနွေးချက်",
    "Dutiyasaññāvedayitakathā": f"ဒုတိယ {_SVN} ဈာန်အကြောင်း ဆွေးနွေးချက်",
    "Tatiyasaññāvedayitakathā": f"တတိယ {_SVN} ဈာန်အကြောင်း ဆွေးနွေးချက်",
    "Saññāvedayitakathā niṭṭhitā": f"{_SVN} ဈာန်အကြောင်း ဆွေးနွေးချက် ပြီးဆုံးသော",
    "Dutiyasaññāvedayitakathā niṭṭhitā": f"ဒုတိယ {_SVN} ဈာန်အကြောင်း ဆွေးနွေးချက် ပြီးဆုံးသော",
    "Tatiyasaññāvedayitakathā niṭṭhitā": f"တတိယ {_SVN} ဈာန်အကြောင်း ဆွေးနွေးချက် ပြီးဆုံးသော",
    "upika": "ရောက်စေတတ်သော", "upikā": "ရောက်စေတတ်သော", "asaññasattupikā": "အသညသတ် ဘုံသို့ ရောက်စေတတ်သော",
    "upacaya": "စုဆောင်းမှု", "upacayo": "စုဆောင်းမှု", "kammūpacaya": "ကံ၏ စုဆောင်းမှု",
    "kammūpacayo": "ကံ၏ စုဆောင်းမှု", "Kammūpacayo": "ကံ၏ စုဆောင်းမှု", "saññūpacayo": "မှတ်သိမှု၏ စုဆောင်းမှု",
    "phassūpacayo": "တွေ့ထိမှု၏ စုဆောင်းမှု", "vedanūpacayo": "ခံစားမှု၏ စုဆောင်းမှု",
    "cetanūpacayo": "စေ့ဆော်မှု၏ စုဆောင်းမှု", "cittūpacayo": "စိတ်၏ စုဆောင်းမှု",
    # ^5-711 … ^5-717 Paccayatā- / Aññamaññapaccayakathā
    "jātānaṃ": "ပေါ်ပေါက်သော", "sahajāta": "အတူ ပေါ်ပေါက်ခြင်း",
    "sahajātānaṃ dhammānaṃ": "အတူ ပေါ်ပေါက်သော သဘောတရား",
    "chandādhipati adhipati": "ဆန္ဒ အကြီးအမှူး … အကြီးအမှူး", "vīriyādhipati adhipati": "ဝီရိယ အကြီးအမှူး … အကြီးအမှူး",
    "cittādhipati adhipati": "စိတ် အကြီးအမှူး … အကြီးအမှူး",
    "vīmaṃsādhipati adhipati": "စုံစမ်းဆင်ခြင်မှု အကြီးအမှူး … အကြီးအမှူး",
    "sahajātapaccayena": "အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း", "adhipatipaccayena": "အကြီးအမှူးဟူသော အကြောင်း",
    "hetupaccayena": "အမြစ်ဟူသော အကြောင်း", "Hetupaccayena": "အမြစ်ဟူသော အကြောင်း",
    "indriyapaccayena": "စွမ်းရည်ဟူသော အကြောင်း", "maggapaccayena": "မဂ်ဟူသော အကြောင်း",
    "ārammaṇapaccayena": "အာရုံဟူသော အကြောင်း",
    "anantarapaccayena": "ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း",
    "āsevanapaccayena": "အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း",
    "samanantara": "ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း", "paccayo": "အကြောင်း",
    "garuṃ": "လေးစားဖွယ်ရာ", "ariyaṃ": "အရိယာ", "purimā": "ရှေးရှေး", "dhammā paccayo": "သဘောတရား … အကြောင်း",
    # ^5-720 … ^5-723 Addhā- / Khaṇalayamuhuttakathā
    "addhā": "ကာလ", "addhānaṃ": "ကာလ", "katheyya": "ပြောသည်", "kathāvatthūni": "စကားပြောရာ အကြောင်းအရာ",
    # ^5-726 / ^5-727 Jarāmaraṇaṃ
    "balānaṃ": "စွမ်းအား", "Arahattaphalassa": "ရဟန္တာ ဖိုလ်",
    "anāgāmiphalassa": "အနာဂါမိဖိုလ်", "sakadāgāmiphalassa": "သကဒါဂါမိဖိုလ်", "arahattamaggassa": "ရဟန္တာ မဂ်",
    "anāgāmimaggassa": "အနာဂါမိမဂ်", "sakadāgāmimaggassa": "သကဒါဂါမိမဂ်",
    "Lokuttarānaṃ": "လောကကို ကျော်လွန်သော", "lokuttarānaṃ": "လောကကို ကျော်လွန်သော",
    "lokuttarā": "လောကကို ကျော်လွန်သော",
    # ^5-728 … ^5-736 the three Saññāvedayitakathās, Asaññasattupikakathā
    "saññāvedayitanirodha": _SVN, "Saññāvedayitanirodhasamāpatti": f"{_SVN} ဈာန် ဝင်စားခြင်း",
    "saññāvedayitanirodhasamāpatti": f"{_SVN} ဈာန် ဝင်စားခြင်း",
    "Saññāvedayitanirodhaṃ": f"{_SVN} ဈာန်", "saññāvedayitanirodhaṃ": f"{_SVN} ဈာန်",
    "nirodhaṃ samāpanno": "ချုပ်ငြိမ်းရာ ဈာန်ကို ဝင်စားနေသော",
    "nirodhaṃ samāpannassa": "ချုပ်ငြိမ်းရာ ဈာန်ကို ဝင်စားနေသော", "kālaṃ kareyya": "သေသည်",
    "kameyya": "ထိရောက်နိုင်သည်", "visaṃ": "အဆိပ်", "satthaṃ": "လက်နက်", "māraṇa": "သေခါနီး",
    "māraṇantiyo": "သေခါနီး", "niyāmo": "စည်းမျဉ်း", "samāpajjanti": "ဝင်စားသည်",
    # ^5-737 … ^5-742 Kammūpacayakathā
    "sampayuttena": "ယှဉ်တွဲသော", "Kusalena kammena kusalo": "ကုသိုလ် ကံ … ကုသိုလ်",
    "Akusalena kammena akusalo": "အကုသိုလ် ကံ … အကုသိုလ်", "jātaṃ": ("ပေါ်ပေါက်သော", "ဖြစ်ပေါ်သော"), "bhijjamānaṃ": "ပျက်သော",
    "nibbattati": "ဖြစ်ပေါ်သည်", "kappo": "ကမ္ဘာ", "kāyasaṅkhāraṃ": "ကိုယ်ဖြင့် ပြုပြင်ဖန်တီးမှု",
    "vacīsaṅkhāraṃ": "နှုတ်ဖြင့် ပြုပြင်ဖန်တီးမှု", "manosaṅkhāraṃ": "စိတ်ဖြင့် ပြုပြင်ဖန်တီးမှု",
    "abhisaṅkharoti": "ပြုပြင်ဖန်တီးသည်", "abhisaṅkharitvā": "ပြုပြင်ဖန်တီး၍", "sabyābajjhaṃ": "ဆင်းရဲစေတတ်သော",
    "abyābajjhaṃ": "မဆင်းရဲစေတတ်သော", "sabyābajjhaṃ abyābajjhaṃ": "ဆင်းရဲစေတတ်သော … မဆင်းရဲစေတတ်သော",
    "paṭiccasamuppādo": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ", "dāyādā": "အမွေခံ", "seyyathāpi": "ဥပမာ",
    "vinipātikā": "အပါယ်သား", "vokiṇṇa": "ရောယှက်နေသော", "phuṭṭho": "တွေ့ထိခြင်း ခံရသော", "phusanti": "တွေ့ထိသည်",
}

T["24-solasamavaggo"] = {
    # headings
    "Niggahakathā": "စိတ်ကို ချုပ်ကိုင်ခြင်းအကြောင်း ဆွေးနွေးချက်",
    "Paggahakathā": "စိတ်ကို မြှင့်တင်ခြင်းအကြောင်း ဆွေးနွေးချက်", "paggaha": "မြှင့်တင်ခြင်း", "paggaho": "မြှင့်တင်ခြင်း",
    "Sukhānuppadānakathā": "သုခကို ပေးခြင်းအကြောင်း ဆွေးနွေးချက်", "sukhānuppadāna": "သုခကို ပေးခြင်း",
    "sukhānuppadānaṃ": "သုခကို ပေးခြင်း", "anuppadāna": "ပေးခြင်း", "anuppadānaṃ": "ပေးခြင်း",
    "sukha": "@sukha24", "sukhaṃ": "@sukha24", "adhigayha": "အလုံးစုံကို စုပေါင်း၍", "Adhigayha": "အလုံးစုံကို စုပေါင်း၍",
    "sahetukaṃ": "အမြစ် ရှိသော", "Rūpaṃ sahetukaṃ": "ရုပ်သည် အမြစ် ရှိသော", "rūpaṃ sahetukaṃ": "ရုပ်သည် အမြစ် ရှိသော",
    "Rūpārūpadhātupariyāpannakathā": "သိမ်မွေ့သော ရုပ် ဓာတ် … ရုပ်မရှိသော ဓာတ်၌ အကျုံးဝင်ခြင်းအကြောင်း ဆွေးနွေးချက်",
    "pariyāpanna": "အကျုံးဝင်ခြင်း", "rūpārūpadhātu": "သိမ်မွေ့သော ရုပ် ဓာတ် … ရုပ်မရှိသော ဓာတ်",
    # ^5-743 … ^5-748 Niggaha-, Paggaha-, Sukhānuppadānakathā
    "pajahati": "ပယ်သည်", "Paro": "တစ်ဦး", "paro": "တစ်ဦး", "parassa": ("အခြားသူ", "အခြားတစ်ယောက်"),
    "atthāya": "အကျိုး", "dussi": "ဒေါသ ဖြစ်သည်", "rajji": "တပ်မက်သည်", "muyhi": "တွေဝေသည်",
    "kilissi": "ညစ်နွမ်းသည်", "niggaṇhāti": "ချုပ်ကိုင်သည်", "pāpaṃ": "ယုတ်မာမှု", "akataṃ": "မပြုသော",
    "asuddhi": "မစင်ကြယ်ခြင်း", "visujjhati": "စင်ကြယ်သည်", "visodhaye": "စင်ကြယ်စေနိုင်",
    "parijānāti": "ပိုင်းခြား သိသည်", "paraṅkataṃ dukkhaṃ": "သူတစ်ပါး ပြုထားသော … ဒုက္ခ",
    "sukhaṃ dukkhaṃ": "သုခ ဒုက္ခ", "pattā": "ရောက်ပြီးသော", "vasī": "အလိုအတိုင်း", "bhūtā": ("ဖြစ်စေနိုင်သော", "ဓာတ်ကြီး"),
    "alobhaṃ": "လောဘ မရှိခြင်း", "adosaṃ": "ဒေါသ မရှိခြင်း", "amohaṃ": "မောဟ မရှိခြင်း", "alobha": "လောဘ မရှိခြင်း",
    "adosa": "ဒေါသ မရှိခြင်း", "amoha": "မောဟ မရှိခြင်း", "paggaṇhāti": "မြှင့်တင်သည်", "anuppadeti": "ပေးသည်",
    "apahattā": "ဖယ်ရှားပေးတော်မူ", "upahattā": "ဆောင်ယူပေးတော်မူ", "laṭukika": "လဋုကိကောပမ", "upame": NONE,
    # ^5-749 … ^5-775
    "vicārena": "ဆက်လက်သုံးသပ်မှု", "manasikaronto": "နှလုံးသွင်းနေသော", "nibbindati": "ငြီးငွေ့သည်",
    "upādāyarūpānaṃ": "မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်", "vihāraṃ": "နေခြင်း",
    "sukhavihāraṃ": "ချမ်းသာစွာ နေခြင်း", "esiyaṃ": "ရှာသော", "samāpattesiyaṃ": "သမာပတ်ကို ရှာသော",
    "Samāpattesiyaṃ": "သမာပတ်ကို ရှာသော", "upapattesiyaṃ": "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော",
}

T["25-sattarasamavaggo"] = {
    # headings
    "puññūpacaya": "ကောင်းမှု စုဆောင်းခြင်း", "puññūpacayo": "ကောင်းမှု စုဆောင်းခြင်း", "apuñña": "မကောင်းမှု",
    "akāla": "အချိန်မတန်မီ", "akālamaccu": "အချိန်မတန်မီ သေခြင်း", "kammato": "ကံကြောင့်",
    "kammavipākato": "ကံ၏ အကျိုးကြောင့်", "dakkhiṇaṃ": "အလှူ", "paṭiggaṇhāti": "ခံယူသည်", "visodheti": "စင်ကြယ်စေသည်",
    "mahapphalaṃ": "အကျိုး ကြီးမားသော", "buddhassa": "ဘုရား", "dakkhiṇā": "အလှူ",
    "Dakkhiṇāvisuddhi": "အလှူ၏ စင်ကြယ်ခြင်း", "visuddhiyo": "စင်ကြယ်ခြင်း", "sukha": "@sukha24",
    # ^5-776 … ^5-779 Arahato puññūpacayakathā
    "āneñja": "မတုန်လှုပ်သော", "saṃvattaniyaṃ": "ရောက်စေတတ်သော", "saṃvattaniyaṃ kammaṃ": "ရောက်စေတတ်သော ကံ",
    "issariya": "အစိုးရခြင်း", "adhipacca": "အကြီးအကဲ ဖြစ်ခြင်း", "parivāra": "အခြံအရံ",
    "sobhagya": "ကောင်းသော ကံကြမ္မာ", "abhisaṅkhāraṃ": "ပြုပြင်ဖန်တီးမှု", "pajahitvā": "ပယ်၍",
    "ussineti": "စုပုံသည်", "ācināti": "စုဆောင်းသည်", "upādiyati": "စွဲလမ်းသည်", "sandhūpeti": "တောက်လောင်စေသည်",
    "vidhūpeti": "ငြိမ်းစေသည်", "visineti": "ဖြန့်ကြဲသည်", "visinetvā": "ဖြန့်ကြဲ၍", "apacināti": "ဖြိုဖျက်သည်",
    "apacinitvā": "ဖြိုဖျက်၍",
    # ^5-780 … ^5-785 Akālamaccu-, Sabbamidaṃ kammato-kathā
    "voropeti": "ချသည်", "paṭisaṃveditvā": "ခံစားရ၍", "upapajjaṃ": "နောက်ဘဝ",
    "phalo": "အသီးအပွင့်", "haneyya": "သတ်သည်", "bhaṇeyya": "ပြောသည်", "palapeyya": "ပြောသည်",
    "samphaṃ": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", "sandhiṃ": "အိမ်", "chindeyya": "ဖောက်ထွင်းသည်", "nillopaṃ": "ဓားပြ",
    "hareyya": "တိုက်သည်", "ekāgārikaṃ kareyya": "အိမ်တစ်အိမ်တည်းကို ဝိုင်းဝန်း၍ လုယက်သည်", "paripanthe": "လမ်း",
    "tiṭṭheyya": ("တည်နေသည်", "စောင့်ဆိုင်းလုယက်သည်"), "dāraṃ": "မယား", "gāma": "ရွာ", "ghātakaṃ": "ဖျက်ဆီးသည်",
    "nigama": "နိဂုံး", "bandhaṃ": "နှောင်ဖွဲ့ခံရခြင်း", "nibandhanā": "ချည်နှောင်ထားသော", "rathassa": "ရထား",
    "āṇī": "ဝင်ရိုးချောင်း", "yāyato": "သွားနေသော", "pajā": "သတ္တဝါ အပေါင်း", "kittiṃ": "ကျော်စောခြင်း",
    "pasaṃsaṃ": "ချီးမွမ်းခံရခြင်း", "vadhaṃ": "သတ်ဖြတ်ခံရခြင်း", "viditvā": "သိ၍", "karaṇaṃ": ("ပြုတတ်သော", "ကွဲပြားစေတတ်သော"),
    "vattatī": "ဖြစ်သည်", "vattate": "ဖြစ်သည်", "vattati": "ဖြစ်သည်",
    # ^5-786 … ^5-789 Indriyabaddha-, Ṭhapetvā ariyamaggaṃ-kathā
    "baddhaṃ": "ဆက်စပ်သော", "Indriyabaddhaṃ": "စွမ်းရည်တို့နှင့် ဆက်စပ်သော", "indriyabaddhaṃ": "စွမ်းရည်တို့နှင့် ဆက်စပ်သော",
    "dvayena": "နှစ်ခု", "bhagavati": "မြတ်စွာဘုရား", "vussati": "ကျင့်ရသည်",
    "indriyabaddhassa dukkhassa": "စွမ်းရည်တို့နှင့် ဆက်စပ်သော ဒုက္ခ", "pariññāya": "ပိုင်းခြား သိရန်",
    "pariññātaṃ": "ပိုင်းခြား သိပြီးသော", "Ariyamaggo": "အရိယာ မဂ်", "ariyamaggo": "အရိယာ မဂ်", "aṭṭhena": "အနက်",
    # ^5-791 … ^5-801 the Saṅgha-, Buddha- and Dakkhiṇāvisuddhikathās
    "Āhutiṃ": "ပူဇော်ဖွယ်", "jātavedo": "မီး", "meghaṃ": "မိုး", "medanī": "မြေကြီး",
    "āhuneyyo": "ပူဇော်ဖွယ်တို့ကို ခံထိုက်သော", "āhuneyyā": "ပူဇော်ဖွယ်တို့ကို ခံထိုက်သော",
    "pāhuneyyo": "ဧည့်ဝတ်တို့ကို ခံထိုက်သော", "pāhuneyyā": "ဧည့်ဝတ်တို့ကို ခံထိုက်သော",
    "dakkhiṇeyyo": "အလှူကို ခံထိုက်သော", "dakkhiṇeyyā": "အလှူကို ခံထိုက်သော",
    "añjalikaraṇīyo": "လက်အုပ်ချီ၍ ရှိခိုးထိုက်သော", "añjalikaraṇīyā": "လက်အုပ်ချီ၍ ရှိခိုးထိုက်သော",
    "karaṇīyo": "ရှိခိုးထိုက်သော", "karaṇīyā": "ရှိခိုးထိုက်သော", "anuttaraṃ": "အမြတ်ဆုံး",
    "puññakkhettaṃ": "ကောင်းမှု လယ်မြေ", "khettaṃ": "လယ်မြေ", "purisayugā": "လူ အစုံ", "yugā": "အစုံ",
    "ārādhenti": "အောင်မြင်စေသည်", "ambapānaṃ": "သရက်သီး အဖျော်", "jambupānaṃ": "သပြေသီး အဖျော်",
    "jambu": "သပြေသီး", "coca": "အစေ့ပါ ငှက်ပျောသီး", "moca": "အစေ့ကင်း ငှက်ပျောသီး", "madhuka": "မဓုက သီး",
    "madhukapānaṃ": "မဓုက သီး အဖျော်", "muddika": "စပျစ်သီး", "muddikapānaṃ": "စပျစ်သီး အဖျော်",
    "sāluka": "ကြာရင်းမြစ်", "sālukapānaṃ": "ကြာရင်းမြစ် အဖျော်", "phārusakapānaṃ": "ဖာရုသက သီး အဖျော်",
    "khādati": "ခဲသည်", "uddesa": "ခွဲဝေ", "pānāni": "အဖျော်", "yāgu": "ယာဂု", "bhattāni": "ဆွမ်း",
    "atiritta": "ကြွင်းကျန်သော", "parampara": "အဆင့်ဆင့်", "Yajamānānaṃ": "အလှူ ပေးနေသော",
    "apekkhāna": "မျှော်ကိုးသော", "pāṇinaṃ": "သတ္တဝါ", "opadhikaṃ": "ဘဝသစ်ကို ဖြစ်စေတတ်သော",
    "sakko": "သိကြားမင်း", "indo": "အရှင်", "vipulo": "ပြန့်ပြောသော", "appameyyo": "အတိုင်းအဆ မရှိသော",
    "udadhi": "ပင်လယ်", "sāgaro": "သမုဒ္ဒရာ", "seṭṭhā": "မြတ်သော", "nara": "လူ", "vīra": "သူရဲကောင်း",
    "karā": "ပြုသော", "pabhā": "အလင်း", "iva": "ကဲ့သို့", "udīrayanti": "ဟောကြားသည်",
    "dhammamudīrayanti": "တရားကို ဟောကြားသည်", "yaññaṃ": "ယဇ်", "anussarantā": "အောက်မေ့သော",
    "veda": "ဝမ်းမြောက်ခြင်း", "Vineyya": "ဖယ်ရှား၍", "macchera": "ဝန်တိုခြင်း", "samūlaṃ": "အမြစ်နှင့်တကွ",
    "Aninditā": "မကဲ့ရဲ့ခံရသော", "ṭhānaṃ": ("တည်ရာ", "ဌာန"), "paṭipannā": "ကျင့်ကြံဆဲသော", "ṭhitā": "တည်ပြီးသော",
    "ujubhūto": "ဖြောင့်မတ်သော", "samāhito": "ပြည့်စုံသော", "pūjito": "ပူဇော်ခံရသော",
    "yiṭṭhaṃ": "ယဇ်ပူဇော်ခြင်း", "uddissa": "ရည်စူး၍", "vaṇṇitā": "ချီးမွမ်းတော်မူသော", "vidūna": "သိတော်မူသူ",
    "vijjati": "ရှိသည်", "āhuneyyānaṃ": "ပူဇော်ဖွယ်ကို ခံထိုက်သော", "aggataṃ": "အမြတ်ဆုံး အဖြစ်",
    "esinaṃ": "ရှာသော", "vipula": "ကြီးမားသော", "atthikānaṃ": "လိုလားသော", "dvipadānaṃ": "ခြေနှစ်ချောင်း ရှိသော",
    "seṭṭho": ("မြတ်သော", "အမွန်မြတ်ဆုံး"), "samo": "တူသော", "asamo": "တူသူ မရှိသော",
    "paṭisamo": "ပြိုင်ဘက် ရှိသော", "paṭibhāgo": "နှိုင်းယှဉ်ဖွယ် ရှိသော", "paṭipuggalo": "ပြိုင်ဘက် ပုဂ္ဂိုလ် ရှိသော",
    "Dāyakato": "ပေးလှူသူကြောင့်", "dāyakato": "ပေးလှူသူကြောင့်", "Paṭiggāhakato": "အလှူခံသူကြောင့်",
    "paṭiggāhakato": "အလှူခံသူကြောင့်", "paṭiggāhakā": "အလှူခံ", "anāgāmissa": "အနာဂါမ်",
    "sotāpanne": "သောတာပန်", "buddhena sīlena": "ဘုရား … သီလ", "parakataṃ": "သူတစ်ပါး ပြုထားသော",
    "parakataṃ sukhadukkhaṃ": "သုခ ဒုက္ခ … သူတစ်ပါး ပြုထားသော",
}

T["26-attharasamavaggo"] = {
    # headings
    "manussaloka": "လူ့ပြည်", "manussaloke": "လူ့ပြည်", "desanā": "ဟောကြားခြင်း", "gandhajāti": "နံ့သာ မျိုး",
    "jāti": ("ဖြစ်ခြင်း", "မျိုး"), "jāte": "မျိုး", "gandhajāte": "နံ့သာ မျိုး",
    "saṅkantikathā": "ကူးပြောင်းခြင်းအကြောင်း ဆွေးနွေးချက်", "saṅkanti": "ကူးပြောင်းခြင်း", "saṅkamati": "ကူးပြောင်းသည်",
    "antarika": "အကြား ကာလ", "jhānantarika": "ဈာန်တို့အကြား ကာလ",
    "jhānantarikā": "ဈာန်တို့အကြား ကာလ",
    # ^5-802 / ^5-803 Manussalokakathā
    "abhisambuddho": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့သော", "bodhiyā": "ဗောဓိပင်", "mūle": "ရင်း",
    "jāto": ("ဖွားမြင်တော်မူခဲ့သော", "ဖွားမြင်တော်မူသော"), "bhagavā jāto": ("မြတ်စွာဘုရား … ဖွားမြင်တော်မူခဲ့သော", "မြတ်စွာဘုရား … ဖွားမြင်တော်မူသော"),
    "pavattitaṃ": "လည်စေတော်မူခဲ့သော", "bhagavatā pavattitaṃ": "မြတ်စွာဘုရား … လည်စေတော်မူခဲ့သော",
    "dhamma": ("ဓမ္မ", "တရား", "သဘောတရား"), "cakkaṃ": "စကြာ", "dhammacakkaṃ pavattitaṃ": "ဓမ္မစကြာကို လည်စေတော်မူခဲ့သော",
    "ossaṭṭho": "စွန့်လွှတ်တော်မူခဲ့သော", "subhaga": "သုဘဂ", "vane": "ဝုန်တော", "mahāvane": "မဟာဝုန်တော",
    "veḷu": "ဝေဠုဝန်", "sāla": "အင်ကြင်း", "ajapāla": "အဇပါလ", "nigrodhe": "ညောင်ပင်", "kaḷandaka": "ကလန္ဒက",
    "nivāpe": "နိဝါပ", "jeta": "ဇေတဝန်", "ārāme": "အရံ", "kūṭāgāra": "ကူဋာဂါရ", "sālāyaṃ": "ဇရပ်",
    "samayaṃ": "အခါ", "viharāmi": ("နေသည်", "နေခဲ့သည်"), "aṭṭhāsi": "နေတော်မူခဲ့သည်",
    "buddhavutthāni": "ဘုရားရှင် မြတ်စွာဘုရား သီတင်းသုံးတော်မူခဲ့သော", "vutthāni": "သီတင်းသုံးတော်မူခဲ့သော",
    "cetiyāni": "စေတီ", "cetiye": "စေတီ", "ārāma": "အရံ", "vihāra": "ကျောင်း", "nagarāni": "မြို့",
    "raṭṭhāni": "တိုင်း", "saṃvaḍḍho": "ကြီးပြင်းတော်မူသော", "anupalitto": "မလိမ်းကျံသော",
    # ^5-804 … ^5-806 Dhammadesanākathā
    "jino": "အောင်နိုင်သူ", "sabbaññū": "အလုံးစုံကို သိသူ", "sabbadassāvī": "အလုံးစုံကို မြင်သော", "sāmī": "အရှင်",
    "paṭisaraṇo": "ကိုးကွယ်ရာ", "Abhinimmitena": "ဖန်ဆင်းထားသော သူ", "desito": ("ဟောတော်မူခဲ့သော", "ဟောခဲ့သော"),
    "Āyasmatā": "အသျှင်", "Āyasmatā ānandena": "အသျှင် အာနန္ဒာ", "deseyyaṃ": "ဟောနိုင်သည်",
    "aññātāro": "နားလည်သူ", "dullabhā": "ရှားပါးသော", "abhiññāya": "ထူးကဲစွာ သိ၍", "desemi": "ဟောသည်",
    "pāṭihāriyaṃ": "အံ့ဖွယ်", "karaṇīyo": "လိုက်နာသင့်သော", "ovādo": "ဆုံးမခြင်း", "anusāsanī": "သွန်သင်ခြင်း",
    "alaṃ": "လုံလောက်သည်", "tuṭṭhiyā": "ကျေနပ်ခြင်း", "attamanatāya": "စိတ် နှစ်သက်ခြင်း",
    "somanassāya": "ဝမ်းမြောက်ခြင်း", "suppaṭipanno saṅgho": "သံဃာ … ကောင်းစွာ ကျင့်ကြံသော",
    "akkhāto": "ဟောထားသော", "veyyākaraṇasmiṃ": "ဖြေရှင်းချက်", "bhaññamāne": "ဟောနေသော",
    "dasasahassi": "တစ်သောင်း", "akampitthā": "တုန်လှုပ်ခဲ့သည်",
    # ^5-807 … ^5-809 Karuṇā-, Gandhajātikathā
    "kāruṇiko": "ကရုဏာ ရှိသော", "hito": "အကျိုးကို လိုလားသော", "caro": "ကျင့်သော", "mahākaruṇā": "မဟာကရုဏာ",
    "samāpattiṃ": "သမာပတ်", "mahākaruṇāsamāpattiṃ": "မဟာကရုဏာ သမာပတ်", "samāpajji": "ဝင်စားတော်မူခဲ့သည်",
    "nhāyanti": "ရေချိုးသည်", "vilimpanti": "လိမ်းကျံသည်", "ucchādenti": "ပွတ်တိုက်သည်", "peḷāya": "သေတ္တာ",
    "paṭisāmenti": "သိမ်းဆည်းသည်", "karaṇḍāya": "ကြုတ်", "pasārenti": "ခင်းကျင်းသည်", "gandhena": "အနံ့",
    "passāvo": "ကျင်ငယ်", "adhiggaṇhāti": "လွှမ်းမိုးသည်", "bhuñjati": ("စားသည်", "ဘုဉ်းပေးတော်မူသည်"),
    "kummāsaṃ": "မုန့်", "odana": "ထမင်း", "bhojī": "စားသုံးသော",
    "Bhagavā gandhabhojī": "မြတ်စွာဘုရား … အနံ့ကို စားသုံးသော",
    # ^5-810 … ^5-812 Ekamaggakathā
    "aṇu": "အနည်းငယ်မျှ", "aṇusahagataṃ": "အနည်းငယ်မျှ ကျန်ရှိသော", "oḷārikaṃ": "ရုန့်ရင်းသော",
    "oḷārikaṃ kāmarāgaṃ jahati": "ရုန့်ရင်းသော ကာမရာဂ … စွန့်ပယ်သည်",
    "kāmarāgaṃ": "ကာမရာဂ", "sakkāyadiṭṭhiṃ": "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ",
    "kāmarāgabyāpādānaṃ": "ကာမရာဂနှင့် ဖျက်ဆီးလိုစိတ်", "tanubhāvaṃ": "ပါးလျခြင်း", "Ekena": "တစ်ပါးတည်း",
    "ekena": "တစ်ပါးတည်း", "ariyamaggena": "အရိယာ မဂ်", "Arahattamaggena": "ရဟန္တာ မဂ်",
    "anāgāmimaggena": "အနာဂါမိမဂ်", "sakadāgāmimaggena": "သကဒါဂါမိမဂ်", "Sotāpattimaggena": "သောတာပတ္တိမဂ်",
    "maggehi": "မဂ်", "adhigacchanti": "ရောက်သည်", "sacchikataṃ": "မျက်မှောက် ပြုဖူးသော",
    # ^5-813 … ^5-826 Jhānasaṅkanti-, Jhānantarika-, Saddaṃ suṇāti-kathā
    "savitakkaṃ": "စတင်ကြံစည်မှု ရှိသော", "pītikaṃ": "ပီတိ ရှိသော", "kaṇṭako": "ဆူးငြောင့်",
    "assāsapassāso": "ဝင်လေ ထွက်လေ", "ākāsānañca": "အဆုံး မရှိသော ဟင်းလင်းပြင်", "paṭivijānāti": "ခွဲခြား သိသည်",
}

T["27-ekunavisatimavaggo"] = {
    # headings
    "jahana": "စွန့်ပယ်ခြင်း", "tathatā": "ဟုတ်တိုင်းမှန်သော သဘော", "accanta": "အပြီးအပိုင်",
    "accantaniyāma": "အပြီးအပိုင် ကျိန်းသေခြင်း", "niyāma": ("ကျိန်းသေခြင်း", "သေချာသော လမ်းကြောင်း"),
    "accantaniyāmatā": "အပြီးအပိုင် ကျိန်းသေခြင်း", "niyāmatā": "ကျိန်းသေခြင်း", "puthujjanassa": "ပုထုဇဉ်",
    # ^5-828 … ^5-831 Kilesajahanakathā
    "nirodheti": "ချုပ်ငြိမ်းစေသည်", "khīṇaṃ": "ကုန်ခန်းပြီးသော", "khepeti": "ကုန်ခန်းစေသည်",
    "atthaṅgataṃ": ("ကွယ်ပြီးသော", "ကွယ်ပျောက်ပြီးသော"), "atthaṅgameti": "ကွယ်ပျောက်စေသည်",
    "abbhatthaṅgameti": "လုံးဝ ကွယ်ပျောက်စေသည်", "sañjātaṃ": ("ဖြစ်ပေါ်သော", "ပေါ်ပေါက်သော"),
    "nibbattaṃ": ("ဖြစ်မြောက်သော", "ဖြစ်ထွန်းသော"), "ajaneti": "မမွေးဖွားစေသည်", "asañjaneti": "မပေါ်ပေါက်စေသည်",
    "anibbatteti": "မဖြစ်ထွန်းစေသည်", "apātubhāveti": "မထင်ရှားစေသည်",
    # ^5-832 … ^5-846 Suññatā-, Sāmaññaphala-, Patti-, Tathatā-, Kusalakathā
    "Appaṇihito": "တောင့်တမှု မရှိခြင်း", "Rūpakkhandhassa": "ရုပ် အစုအဝေး",
    "Saṅkhārakkhandhassa": "ပြုပြင်ဖန်တီးမှု အစုအဝေး", "suññaṃ": "ဆိတ်သုဉ်းသော", "āneñja": "အာနေဉ္ဇသပ္ပာယ",
    "Sāmaññaphalaṃ": "ရဟန်းအဖြစ်၏ ဖိုလ်", "parāyaṇaṃ": "မှီခိုရာ", "accutaṃ": "မစုတေသော အရာ",
    "tāṇaṃ": "ကာကွယ်ရာ", "tāṇāni": "ကာကွယ်ရာ", "saraṇaṃ": "ကိုးကွယ်ရာ", "leṇaṃ": "ပုန်းအောင်းရာ",
    "asaṅkhatāni": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော အရာ", "Patti": "ရရှိခြင်း", "piṇḍapātassa": "ဆွမ်း",
    "senāsanassa": "ကျောင်းအိပ်ရာနေရာ", "parikkhārassa": "အသုံးအဆောင်",
    "gilānapaccayabhesajjaparikkhārassa": "သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်", "Cīvarassa": "သင်္ကန်း",
    "vitthāretabbaṃ": "အကျယ် ချဲ့ရမည့်", "sotāpattiphalassa": "သောတာပတ္တိဖိုလ်",
    "sotāpattimaggassa": "သောတာပတ္တိမဂ်", "Sotāpattimaggassa": "သောတာပတ္တိမဂ်",
    "Sabbadhammānaṃ": "သဘောတရား အားလုံး", "viññāṇatā": "သိစိတ်ဖြစ်ခြင်း", "rūpatā": "ရုပ်ဖြစ်ခြင်း",
    "saṅkhāratā": "ပြုပြင်ဖန်တီးမှုဖြစ်ခြင်း", "Nibbānadhātu": "နိဗ္ဗာန် ဓာတ်", "nibbānadhātu": "နိဗ္ဗာန် ဓာတ်",
    # ^5-847 … ^5-856 Accantaniyāma-, Indriyakathā
    "arahanta": "ရဟန္တာ", "uppādako": "စိမ်းစေသူ", "Pahīnā": "ပယ်ပြီးသော", "uppajjeyya": "ဖြစ်ပေါ်သည်",
    "bodha": "ထိုးထွင်း သိခြင်း", "Sassatadiṭṭhiyā": "အတ္တသည် ထာဝရ တည်မြဲသည်ဟူသော အယူ",
    "Ucchedadiṭṭhiyā": "အတ္တသည် ပြတ်စဲသွားသည်ဟူသော အယူ", "niyatassa": "ကျိန်းသေသော", "nimuggo": "နစ်မြုပ်သော",
    "Sabbakālaṃ": "အချိန်ခပ်သိမ်း", "nimujjati": "ပြန်နစ်သည်", "vipassati": "ကြည့်ရှုသည်",
    "viloketi": "ဝေ့ဝဲ ကြည့်သည်", "patigādha": "ခြေကုတ်ရာ မြေ", "mudu": "နုံ့သော", "raja": "မြူ",
    "akkhe": "မျက်စိ", "tikkha": "ထက်မြက်သော", "viharante": "နေသော",
    "suviññāpaye": "သိအောင် ပြရ လွယ်ကူသော", "viññāpaye": "သိအောင် ပြရ", "addasaṃ": "မြင်ခဲ့သည်",
    "dassāvino": "မြင်သော", "volokento": "ကြည့်ရှုသော", "dissanti": ("ထင်ရသည်", "မြင်ရသည်"),
    "dvākāre": NONE, "duviññāpaye": NONE, "lokiyāni": "လောကနှင့် သက်ဆိုင်သော",
}

T["28-visatimavaggo"] = {
    # headings
    "asañcicca": "မရည်ရွယ်ဘဲ", "Asañcicca": "မရည်ရွယ်ဘဲ", "Nirayapālakathā": "ငရဲထိန်းအကြောင်း ဆွေးနွေးချက်",
    "nirayapāla": "ငရဲထိန်း", "nirayapālā": "ငရဲထိန်း", "pāla": "ထိန်း", "pālā": "ထိန်း",
    # ^5-857 … ^5-862 Asañciccakathā
    "ānantariko": "အနန္တရိယကံ ရှိသော", "voropetvā": "သတ်၍", "mātaraṃ voropetvā": "အမိကို သတ်၍",
    "Asañcicca voropetvā": "မရည်ရွယ်ဘဲ … သတ်၍", "hantvā": "သတ်၍", "bhaṇitvā": "ပြော၍",
    "voropitā": "သတ်ခဲ့ပြီးသော", "jīvitā voropitā": "သတ်ခဲ့ပြီးသော",
    "ruhiruppādako": "ဘုရားရှင်၏ သွေးကို စိမ်းစေသူ", "pitughātako": "အဖကို သတ်သူ", "mātughātako": "အမိကို သတ်သူ",
    "Mātughātako": "အမိကို သတ်သူ", "Saṅghabhedako": "သံဃာကို သင်းခွဲသူ", "saṅghabhedako": "သံဃာကို သင်းခွဲသူ",
    "saṅghabhedakā": "သံဃာကို သင်းခွဲသူ", "Dhammasaññī": "တရားဟု မှတ်ထင်သော", "dhammasaññī": "တရားဟု မှတ်ထင်သော",
    "saññī": ("မှတ်သိသော", "မှတ်ထင်သော"), "āpāyiko": ("အပါယ်သို့ ရောက်သော", "အပါယ်သို့ ရောက်မည့်"),
    "nerayiko": ("ငရဲ၌ ကျသော", "ငရဲ၌ ကျမည့်"), "atekiccho": "ကုစား၍ မရနိုင်သော",
    # ^5-864 … ^5-871 Ñāṇa-, Nirayapāla-, Tiracchānakathā
    "samāpajjeyya": "ဝင်စားသည်", "dadeyya": ("ပေးသည်", "လှူသည်", "ပြုသည်"), "manussesu": "လူ",
    "kāraṇikā": ("ညှဉ်းပန်း နှိပ်စက်သူ", "လေ့ကျင့်ပေးသူ"), "nirayesu": "ငရဲ",
    "kammakāraṇā": "ညှဉ်းပန်း နှိပ်စက်ခြင်း", "Somo": "သောမ", "yamo": "ယမ", "hananti": "သတ်သည်",
    "paṇunnaṃ": "နှင်ထုတ်ခံရသော", "uddehakaṃ": "ဆူပွက်သော", "pheṇa": "အမြှုပ်", "paccati": ("ပူလောင်ရသည်", "ကျက်သည်"),
    "tiriyaṃ": "ဘေး", "vāsīhi": "ပဲခွပ်", "pādaṃ": "ခြေ", "siraṃ": "ခေါင်း", "ṭhapetvā": ("ချန်ထား၍", "ထား၍"),
    "nirayapālā ṭhapetvā": "ငရဲထိန်း … ထား၍", "kuṭhārīhi": "ပုဆိန်", "saṃvesetvā": "လှဲချ၍", "tacchanti": "ခုတ်သည်",
    "pañcavidha": "ငါးပါး", "bandhanaṃ": "အနှောင်", "kāraṇaṃ": "ညှဉ်းပန်းမှု", "kārenti": "ပြုသည်",
    "tattaṃ": "ပူလောင်သော", "ayokhīlaṃ": "သံချောင်း", "hatthe": "လက်", "pāde": "ခြေ", "urasmiṃ": "ရင်",
    "gamenti": "ရိုက်သွင်းသည်", "tibbā": "ပြင်းထန်သော", "kaṭukā": "ခါးသက်သော", "rathe": "ရထား", "yojetvā": "ကပ်၍",
    "ādittāya": "ပူလောင်နေသော", "sampajjalitāya": "တောက်လောင်နေသော", "sajotibhūtāya": "မီးလျှံ ထွက်နေသော",
    "pathaviyā": "မြေပြင်", "paccāsārenti": "နောက်သို့ … ဆွဲသည်", "kumbhiyā": "အိုး", "loha": "ကြေး",
    "pakkhipanti": "ပစ်ထည့်သည်", "āropenti": "တက်စေသည်", "aṅgāra": "မီးကျီး", "kaṇṇo": "ထောင့်",
    "vibhatto": "ခွဲခြား", "mito": "တိုင်းတာထားသော", "bhāgaso": "အပိုင်းအခြားအလိုက်", "pākāra": "တံတိုင်း",
    "paṭikujjito": "အပေါ်မှ အုပ်ထားသော", "vedayati": ("ခံစားသည်", "ခံစားရသည်"), "tejasā": "မီး", "yojana": "ယူဇနာ",
    "pharitvā": "ပျံ့နှံ့၍", "mahāniraye": "ငရဲကြီး",
    "tiracchānayonī": "တိရစ္ဆာန် မွေးဖွားရာ အမျိုးအစား", "yonī": "မွေးဖွားရာ အမျိုးအစား",
    "tiracchānagatā": "တိရစ္ဆာန်", "devesu": "နတ်", "kīṭā": "ပိုးမွှား", "paṭaṅgā": "ပိုးဖလံ", "makasā": "ခြင်",
    "makkhikā": "ယင်", "ahī": "မြွေ", "vicchikā": "ကင်းမြီးကောက်", "satapadī": "ကင်းခြေများ", "gaṇḍuppādā": "တီကောင်",
    "yānaṃ": "ယာဉ်", "hatthināgo": "ဆင်ပြောင်", "sahassa": "တစ်ထောင်", "yuttaṃ": "ကပ်ထားသော", "bandhā": "ထိန်း",
    "yāvasikā": "မြက်ကျွေးသူ", "bhattakārakā": "အစာ ချက်ပြုတ်သူ",
    # ^5-872 … ^5-877 Pañcaṅgika-, Dvādasavatthuka-kathā
    "Maggānaṃ": "မဂ်", "padā": "ပုဒ်", "Virāgo": "ရာဂ ကင်းခြင်း", "seṭṭho": ("မြတ်သော", "အမြတ်ဆုံး"),
    "dvipadānaṃ": ("ခြေနှစ်ချောင်း ရှိသော", "ခြေ နှစ်ချောင်း ရှိသော"), "seyyathidaṃ": "ယင်းမှာ", "pubbe": "ရှေးဦးစွာ",
    "parisuddho": "စင်ကြယ်သော", "pāripūriṃ": "ပြည့်စုံခြင်း", "gacchati": ("သွားသည်", "ရောက်သည်"),
    "Suññā": "ဆိတ်သုဉ်းသော", "pavādā": "ဝါဒ", "samaṇebhi": "ရဟန်း", "subhadda": "သုဘဒ္ဒ", "yasmiṃ": "အကြင်",
    "catuttho samaṇo": "စတုတ္ထ ရဟန်း", "vatthukaṃ": "အခြေ … ရှိသော",
    "Dvādasavatthukaṃ": "အခြေ ဆယ့်နှစ်ပါး ရှိသော", "dvādasavatthukaṃ": "အခြေ ဆယ့်နှစ်ပါး ရှိသော",
    "sotāpattiphalāni": "သောတာပတ္တိဖိုလ်", "dvādasa sotāpattimaggā": "သောတာပတ္တိမဂ် ဆယ့်နှစ်ပါး",
    "lokuttarañāṇāni": "လောကကို ကျော်လွန်သော ဉာဏ်", "pahātabbaṃ": "ပယ်ရမည့်", "bhāvetabbaṃ": "ပွားများရမည့်",
    "pariññeyyaṃ": "ပိုင်းခြား သိရမည့်", "sacchikātabbaṃ": "မျက်မှောက်ပြုရမည့်", "udapādi": "ဖြစ်ပေါ်သည်",
    "sañcayo": "စုဆောင်းခြင်း", "puññasañcayo": "ကောင်းမှု စုဆောင်းခြင်း",
}

T["29-ekavisatimavaggo"] = {
    # headings
    "sāsana": "သာသနာ", "sāsanaṃ": "သာသနာ", "vivitta": "ကင်းခြင်း", "Iddhikathā": "ဣဒ္ဓိအကြောင်း ဆွေးနွေးချက်",
    "buddha": "ဘုရား", "disā": "အရပ်", "Dhammakathā": "သဘောတရားအကြောင်း ဆွေးနွေးချက်",
    # ^5-879 … ^5-884 Avivitta-, Saṃyojana-, Iddhikathā
    "kammehi": "ကံ", "tedhātukehi": "ဘုံ သုံးပါးနှင့် ဆိုင်သော", "vivitto": "ကင်းသော", "avivitto": "မကင်းသော",
    "Puthujjano avivitto": "ပုထုဇဉ် … မကင်းသော",
    "rūpadhātuarūpadhātūpagaṃ kammaṃ": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံသို့ ရောက်စေသော ကံ",
    "pahāya": "ပယ်၍", "kiñci saṃyojanaṃ pahāya": "နှောင်ကြိုး တစ်စုံတစ်ရာကို ပယ်၍",
    "appahāya arahattappatti": "မပယ်ဘဲ ရဟန္တာ အဖြစ်သို့ ရောက်ခြင်း", "arahattappatti": "ရဟန္တာ အဖြစ်သို့ ရောက်ခြင်း",
    "nirāgo": "ရာဂ ကင်းသော", "niddoso": "ဒေါသ ကင်းသော", "nimmoho": "မောဟ ကင်းသော",
    "nicca": "အမြဲ", "paṇṇā": "ရွက်စိမ်း", "pupphā": "ပန်းပွင့်", "phalikā": "အသီး သီး", "juṇhaṃ": "လရောင် သာ",
    "khemaṃ": "ဘေးကင်း", "subhikkhaṃ": "စားနပ်ရိက္ခာ ပေါများ", "suvatthi": "ချမ်းသာ",
    "jāyiṃsu": ("ဖြစ်သည်", "မွေးဖွားသည်"), "buddhānaṃ": "ဘုရား", "buddhānaṃ vā sāvakānaṃ": "ဘုရား … တပည့်",
    "adhippāyaiddhi": "အလိုအတိုင်း ဖြစ်စေနိုင်သော ဣဒ္ဓိ", "adhippāyiddhi": "အလိုအတိုင်း ဖြစ်စေနိုင်သော ဣဒ္ဓိ",
    "adhippāya": "အလိုအတိုင်း", "māgadhassa": "မဂဓ", "pāsādaṃ": "ပြာသာဒ်", "pilindavaccho": "ပိလိန္ဒဝစ္ဆ",
    "adhimucci": "ဆုံးဖြတ်ခဲ့သည်", "seniyassa": "သေနိယ", "seniyassa bimbisārassa": "သေနိယ ဗိမ္ဗိသာရ",
    # ^5-885 / ^5-886 Buddha-, Sabbadisākathā
    "buddhānaṃ hīnātirekatā": "ဘုရား … ယုတ်ခြင်း ထူးခြင်း", "hīna": "ယုတ်ခြင်း", "atireka": "ထူးခြင်း",
    "vasibhāva": "အစိုးရခြင်း", "sabbaññuta": "အလုံးစုံကို သိမြင်သော", "upaṭṭhāko": "အလုပ်အကျွေး",
    "jacco": "အမျိုးဇာတ်", "pattaṃ": "သပိတ်", "dhāreti": "ဆောင်သည်", "sāvaka": ("သာဝက", "တပည့်"),
    "nagare": "မြို့", "pitaro": "မိဘ", "mātā": NONE, "kīdisaṃ": "အဘယ်သို့သော", "raṭṭhe": "တိုင်း",
    "nāmā": "အမည်",
    "buddhā": "ဘုရား", "tiṭṭhanti": ("တည်သည်", "တည်ရှိသည်"), "disāya": "အရပ်", "ratiyā": "နိမ္မာနရတီ",
    "Puratthimāya": "အရှေ့", "rājike": "စာတုမဟာရာဇ်", "uttarāya": "မြောက်", "Dakkhiṇāya": "တောင်",
    "tāvatiṃse": "တာဝတိံသာ", "tusite": "တုသိတာ", "vattiyā": "ပရနိမ္မိတဝသဝတ္တီ",
    # ^5-887 … ^5-890 Dhamma-, Kammakathā
    "sammattaniyatā": "မှန်ကန်မှု၌ ကျိန်းသေသော", "Micchattaniyatā": "မှားယွင်းမှု၌ ကျိန်းသေသော",
    "niyato rāsi": "ကျိန်းသေသော … အစု", "rāsi": "အစု", "rāsī": "အစု", "kammā": "ကံ",
    "vedanīyaṃ": "ခံစားရမည့်", "Diṭṭhadhammavedanīyaṃ": "မျက်မှောက်ဘဝ၌ ခံစားရမည့်", "niyataṃ": "ကျိန်းသေသော",
    "sammattaniyataṃ": "မှန်ကန်မှု၌ ကျိန်းသေသော", "Micchattaniyataṃ": "မှားယွင်းမှု၌ ကျိန်းသေသော",
    "aparāpariya": "နောက်ဘဝ အဆက်ဆက်", "aparāpariyavedanīyaṃ": "နောက်ဘဝ အဆက်ဆက်၌ ခံစားရမည့်",
    "upapajja": "နောက်ဘဝ",
}

T["30-bavisatimavaggo"] = {
    # headings
    "Parinibbānakathā": "ပရိနိဗ္ဗာန် ပြုခြင်းအကြောင်း ဆွေးနွေးချက်", "parinibbāna": "ပရိနိဗ္ဗာန် ပြုခြင်း",
    "āneñja": ("မတုန်မလှုပ်သော", "မတုန်လှုပ်သော", "အာနေဉ္ဇသပ္ပာယ"), "kusalacitta": "ကုသိုလ် စိတ်", "kusalacitto": "ကုသိုလ် စိတ် ရှိသော", "abhisamaya": "ထင်ထင်ရှားရှား သိမြင်ခြင်း",
    "abhisamayakathā": "ထင်ထင်ရှားရှား သိမြင်ခြင်းအကြောင်း ဆွေးနွေးချက်",
    "Āsevanapaccayakathā": "အဖန်ဖန် မှီဝဲခြင်း အကြောင်းဖြစ်ခြင်းအကြောင်း ဆွေးနွေးချက်",
    "āsevana": "အဖန်ဖန် မှီဝဲခြင်း", "āsevanapaccaya": "အဖန်ဖန် မှီဝဲခြင်း အကြောင်းဖြစ်ခြင်း", "khaṇika": "ခဏ",
    # ^5-892 … ^5-896 Parinibbāna-, Kusalacitta-, Āneñjakathā
    "appahāya parinibbānaṃ": "မပယ်ဘဲ ပရိနိဗ္ဗာန် ပြုခြင်း", "ācinanto": "စုဆောင်းသော", "apacinanto": "ဖျက်ဆီးသော",
    "pajahanto": "ပယ်သော", "upādiyanto": "စွဲလမ်းသော", "visinento": "ဖြန့်ကျက်သော", "ussinento": "စုစည်းသော",
    "vidhūpento": "ငြိမ်းစေသော", "sandhūpento": "တောက်လောင်စေသော", "ussineti": ("စုပုံသည်", "စုစည်းသည်"),
    "visineti": ("ဖြန့်ကြဲသည်", "ဖြန့်ကျက်သည်"), "visinetvā": ("ဖြန့်ကြဲ၍", "ဖြန့်ကျက်၍"),
    "apacināti": ("ဖြိုဖျက်သည်", "ဖျက်ဆီးသည်"), "apacinitvā": ("ဖြိုဖျက်၍", "ဖျက်ဆီး၍"),
    "parinibbāyati": "ပရိနိဗ္ဗာန် ပြုသည်", "abhisaṅkharonto": "ပြုပြင်ဖန်တီးသော", "karonto": "ပြုသော",
    "sobhagya": ("ကောင်းသော ကံကြမ္မာ", "ကောင်းကျိုး ချမ်းသာ"), "upaṭṭhita": "ထင်ရှား တည်သော",
    "vuṭṭhahitvā": "ထ၍", "samanantarā": ("ချက်ချင်း နောက်၌", "ချက်ချင်း"), "catutthajjhānā": "စတုတ္ထ ဈာန်",
    "kiriyamaye": "ကြိယာ", "kiriyābyākate": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ကြိယာ",
    "āneñje": "မတုန်မလှုပ်သော အခြေ", "ṭhito": ("တည်နေသော", "တည်သော"), "pakati": "ပကတိ", "pakaticitte": "ပကတိ စိတ်",
    "vipākābyākate": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အကျိုး",
    # ^5-897 … ^5-905 Dhammābhisamaya-, Supina-, Āsevanapaccayakathā
    "Suttassa": "အိပ်ပျော်နေသော", "pamattassa": "မေ့လျော့နေသော", "muṭṭhassatissa": "သတိ လစ်နေသော",
    "sampajānassa": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း", "jāgariya": "နိုးကြား", "sākacchā": "ဆွေးနွေးခြင်း",
    "savanaṃ": "နာကြားခြင်း", "ratta": "ညဉ့်ဦးယံ ညဉ့်နောက်ယံ", "paripucchā": "မေးမြန်းခြင်း",
    "samādānaṃ": "ဆောက်တည်ခြင်း", "seyyāya": "ကိန်းအောင်း", "gabbha": "အမိဝမ်း", "ghoso": "အသံ",
    "supinagatassa": "အိပ်မက် မက်နေသော", "Supinantena": "အိပ်မက်ထဲ", "mucceyya": "ထွက်သည်",
    "bhojanīyaṃ": ("ဘောဇဉ်", "စားဖွယ်"), "ādeyya": "လက်ခံထိုက်သော", "palāpassa": "စကား",
    "pānaṃ": ("အဖျော်", "သောက်ခြင်း"), "abbhakkhāna": "စွပ်စွဲခံရခြင်း", "abbhūta": "လုပ်ကြံ", "vādassa": "ပြောခြင်း",
    "bhūtassa": "ဖြစ်လာသော", "bahulīkato": "အကြိမ်များစွာ ပြုထားသော",
    "bhāvito": ("ပွားများပြီးသော", "ပွားများထားသော", "ပွားများသော"), "saṃvattaniko": "ပို့ဆောင်တတ်သော",
    "nirayasaṃvattaniko": "ငရဲသို့ ပို့ဆောင်တတ်သော", "āyuka": "အသက်", "sabbalahuso": "အပေါ့ဆုံး",
    "sabbalahuso vipāko": "အပေါ့ဆုံး အကျိုး", "āsevito": "အဖန်ဖန် မှီဝဲထားသော",
    "paccayatā": ("အကြောင်းဖြစ်ပုံ", "အကြောင်းဖြစ်ခြင်း"), "āsevanapaccayatā": "အဖန်ဖန် မှီဝဲခြင်း အကြောင်းဖြစ်ခြင်း",
    "amanāpa": "မနှစ်သက်ဖွယ်", "bhedana": "ကွဲပြားခြင်း", "pisuṇāya": "ကုန်းချောစကား", "mittehi": "မိတ်ဆွေ",
    "ummattaka": "ရူးသွပ်ခြင်း", "micchācārassa": "မှားယွင်းစွာ ကျင့်ခြင်း", "sapatta": "ရန်သူ",
    "bahulīkatā": ("အဖန်ဖန် ပြုထားသော", "အကြိမ်များစွာ ပြုထားသော"), "saṃvattanikā": "ပို့ဆောင်တတ်သော",
    "nirayasaṃvattanikā": "ငရဲသို့ ပို့ဆောင်တတ်သော", "āsevitā": "အဖန်ဖန် မှီဝဲထားသော", "ogadhā": "သက်ဝင်သော",
    "parāyanā": "ဆုံးခန်းတိုင်ရာ", "pariyosānā": "အဆုံးသတ်သော",
    # ^5-906 / ^5-907 Khaṇikakathā
    "kāyaviññāṇena": "ကိုယ် သိစိတ်", "cakkhuviññāṇena": "မျက်စိ သိစိတ်", "ajjhattikaṃ": "မိမိ၏",
    "aparibhinnaṃ": "မပျက်စီးသော", "tajjo": "ထိုအရာနှင့် ဆိုင်သော", "samannāhāro": ("နှလုံးသွင်းခြင်း", "နှလုံးသွင်းမှု"),
    "pātubhāvo": "ထင်ရှား ဖြစ်ပေါ်ခြင်း", "bhāgassa": "အစိတ်အပိုင်း", "āyasmā sāriputto": "အသျှင် သာရိပုတ္တရာ",
    "khaṇikā": "ခဏမျှသာ တည်သော", "cittakkhaṇikā": "စိတ် … ခဏမျှသာ တည်သော",
    "Ekacittakkhaṇikā": "စိတ် တစ်ခု၏ ခဏမျှသာ တည်သော", "ekacittakkhaṇikā": "စိတ် တစ်ခု၏ ခဏမျှသာ တည်သော",
    "niccā": "မြဲသော", "dhuvā": "ခိုင်ခံ့သော", "vipariṇāmadhammā": "ဖောက်ပြန်ပြောင်းလဲခြင်း … သဘော ရှိသော",
}

T["31-tevisatimavaggo"] = {
    # headings
    "adhippāya": "ရည်ရွယ်ချက်", "ekādhippāya": "တူညီသော ရည်ရွယ်ချက်", "Ekādhippāyena": "တူညီသော ရည်ရွယ်ချက်",
    "adhippāyena": "ရည်ရွယ်ချက်", "vaṇṇa": "အသွင်", "arahantavaṇṇa": "ရဟန္တာတို့၏ အသွင်", "vaṇṇena": "အသွင်",
    "Arahantānaṃ": "ရဟန္တာ", "arahantānaṃ": "ရဟန္တာ", "arahantānaṃ vaṇṇena": "ရဟန္တာတို့၏ အသွင်",
    "kārikā": "အလိုရှိတိုင်း ပြုခြင်း", "issariya": ("အစိုးရခြင်း", "မိမိ၏ အစွမ်း"),
    "Issariyakāmakārikādikathā": "မိမိ၏ အစွမ်းဖြင့် အလိုရှိတိုင်း ပြုခြင်း စသည်တို့အကြောင်း ဆွေးနွေးချက်",
    "Issariyakāmakārikākathā": "မိမိ၏ အစွမ်းဖြင့် အလိုရှိတိုင်း ပြုခြင်းအကြောင်း ဆွေးနွေးချက်",
    "patirūpa": "အတုအယောင်", "Patirūpakathā": "အတုအယောင်အကြောင်း ဆွေးနွေးချက်", "patirūpako": "တူသော အရာ",
    "cittapatirūpakaṃ": "စိတ်နှင့် တူသော အရာ", "nipphanna": "ပြီးမြောက်သော",
    "parinipphanna": "ပြည့်စုံစွာ ပြီးမြောက်သော",
    "Dukkhaṃ parinipphannaṃ": "ဆင်းရဲ ဒုက္ခ … ပြည့်စုံစွာ ပြီးမြောက်သော",
    # ^5-908 / ^5-909 Ekādhippāya-, Arahantavaṇṇakathā (the list as ch30 / ch31 word it)
    "pāṇo": "သတ္တဝါ", "hantabbo": "သတ်ရမည့်", "bhaṇitabbā": "ပြောရမည့်", "pisuṇaṃ": "ကုန်းချောစကား",
    "samphaṃ": "အကျိုးမဲ့ စကား", "palapitabbaṃ": "ပြောရမည့်", "sandhi": "အိမ်", "cheditabbo": "ဖောက်ထွင်းရမည့်",
    "nillopaṃ": "လုယက်", "hātabbaṃ": NONE, "haranti": NONE,
    "ekāgārikaṃ kātabbaṃ": "အိမ်တစ်လုံးကို ဝိုင်းဝန်း လုယက်ရမည့်", "ṭhātabbaṃ": "ဓားပြ တိုက်ရမည့်",
    "dāro": "မယား", "ghātako": "ဖျက်ဆီးရမည့်", "pārājikena": "ပါရာဇိက ကျသော", "assamaṇena": "ရဟန်း မဟုတ်သော",
    "abhikkhunā": "ဘိက္ခု မဟုတ်သော", "mūlena": "အမြစ်", "paṭisevitabbo": "မှီဝဲရမည့်", "methuno": "မေထုန်",
    "methuno dhammo": "မေထုန် အကျင့်", "amanussā": "လူ မဟုတ်သော", "paṭisevanti": "မှီဝဲသည်",
    "chindanti": "ဖောက်ထွင်းသည်", "palapanti": "ပြောသည်", "bhaṇanti": "ပြောသည်", "tiṭṭhanti": "ဓားပြ တိုက်သည်",
    "ekāgārikaṃ karonti": "အိမ်တစ်လုံးကို ဝိုင်းဝန်း လုယက်သည်",
    # ^5-910 … ^5-914 Issariyakāmakārikākathā
    "roruvaṃ": "ရောရုဝ", "upapajjeyya": ("ပြန်လည် ဖြစ်ပေါ်သည်",), "vīmaṃsa": "ဝီမံသ", "iddhimā": "ဣဒ္ဓိ ရှိသော",
    "gabbhaseyyaṃ": "အမိဝမ်း၌ ကိန်းအောင်းခြင်း", "paccāgacchi": "ယူဆခဲ့သည်", "dukkarakārikaṃ": "ပြုရခက်သော အကျင့်",
    "akāsi": ("ပြုခဲ့သည်", "ကျင့်ခဲ့သည်"), "tapaṃ": "ပြင်းထန်သော အကျင့်", "uddisi": "ကိုးကွယ်ခဲ့သည်",
    # ^5-918 the uddānas and the book's colophon
    "pakaraṇe": "ကျမ်း", "niyāmo": ("စည်းမျဉ်း", "သေချာသော လမ်းကြောင်း"), "maddanā": "ချေမှုန်းတတ်သော",
    "samaye": "အယူဝါဒ", "pavāda": "ဝါဒ", "samāhitā": "ကောင်းစွာ တည်သော", "Ujjotanā": "ထွန်းလင်းစေတတ်သော",
    "kathāvatthu": "အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း", "nibbuti": "ငြိမ်းအေးခြင်း",
    "aḍḍhapaṇṇāsako": "ငါးဆယ်တစ်ဝက်အစု", "bhāṇavāraṃ": "ရွတ်ဖတ်ရန် အပိုင်း", "Pañcattiṃsa": "သုံးဆယ့်ငါးပိုင်း",
}

CTX = {
    "5-504": {"kāyo": "အပေါင်း"},                       # asurakāyo «အသုရာ အပေါင်း»
    "5-508": {"sañña": "အသညသတ်"},                     # asaññasattūpaga «အသညသတ်သို့ ရောက်မည့်» (one Burmese word)
    "5-517": {"rūpino dhammā": "ရုပ် … သဘောတရား"},     # fragment of arūpino dhammā (rule 8: the positive part)
    "5-519": {"bhāvo": NONE},                          # attabhāvo = ကိုယ်ခန္ဓာ (pi-2: one word, one member)
    "5-522": {"su": "မွှေးသော", "du": "နံစော်သော"},       # sugandho / duggandho
    "5-525": {"sabbattha": NONE},                      # the siglum «(sabbattha)» stays Roman in the text
    "5-539": {"katvā": "ပြု၍"},                         # «kammaṃ katvā» «ကံကို ပြုပြီးလျှင်» (Q1)
    "5-543": {"sattānaṃ": "အသညသတ်", "sañña": NONE},   # Asaññasattānaṃ «အသညသတ်တို့၌»: one word, one member                  # Asaññasattānaṃ «အသညသတ်တို့၌»
    "5-545": {"vattabbe": NONE},
    "5-599": {"dhammo": "တရား"},                        # «sataṃ dhammo» «သူတော်ကောင်းတို့၏ တရား» (not pi-4 -dhammo)
    "5-603": {"dhammo": "တရား"},
    "5-601": {"kammaṃ": "ပြုမူခြင်း"},
    "5-626": {"satta": "ခုနစ်"},                        # satta rattindivāni «ခုနစ်ရက်ခုနစ်ညဉ့်»
    "5-644": {"sakadāgāmi": "သကဒါဂါမ်", "anāgāmi": "အနာဂါမ်"},   # «Sakadāgāminiyamenā» «သကဒါဂါမ်၏ ကျိန်းသေမှုဖြင့်»
    "5-648": {"pāṇaṃ": "သတ္တဝါ"}, "5-649": {"pāṇaṃ": "သတ္တဝါ"},                   # «sañcicca pāṇaṃ jīvitā voropeyya» «ရည်ရွယ်၍ သတ္တဝါကို …»
    "5-650": {"rūpe": "အဆင်းအရောင်"},                  # «āpāyike rūpe rajjeyya»
    "5-21-8-1-0": {"rāga": "တပ်မက်မှု"},               # Asātarāga «မသာယာဖွယ်ကို တပ်မက်မှု»
    "5-675": {"rāgo": "တပ်မက်မှု", "samāpanno": "ရောက်သော", "yaṃ kiñci": "အကြင်"},   # anurodhavirodhaṃ samāpanno
    "5-658": {"dadeyya": "ပြုသည်", "Kappaṭṭho dadeyya": "ကမ္ဘာ ပတ်လုံး တည်ရမည့်သူ … ပြုသည်"},   # «dānaṃ dadeyya» first
    "5-660": {"payuttaṃ": "ပြုခဲ့ပြီးသော"},             # «taṃ kammaṃ payuttaṃ» «ထိုကံကို ပြုခဲ့ပြီး၍»
    "5-661": {"abhabbo": NONE},                         # «abhabbo … okkamituṃ» = one Burmese verb «မသက်ဆင်းနိုင်»
    "5-664": {"abhisametuṃ": "ထိုးထွင်း သိ၍"},         # «nābhisametuṃ» «ထိုးထွင်း မသိဘဲ»
    "5-656": {"Mato": "သေ၍"},
    "5-685": {"rāgo": "တပ်မက်မှု"},                    # uddāna «asātarāgo»
    "5-692": {"jāyanti": "ဖြစ်ပေါ်သည်", "nibbattati": NONE},   # «pasākhā jāyanti»; nibbattati only in the variant
    "5-699": {"yaṃ kiñci": "ဟူသမျှ"},                   # «yaṃ kiñci rūpaṃ» «ရုပ် ဟူသမျှ»
    "5-23-10-1-0": {"satta": "အသညသတ်", "sañña": NONE},  # Asaññasattupika «အသညသတ် ဘုံသို့ ရောက်စေတတ်သော»
        "5-779": {"dānaṃ": "ဒါန", "dadeyya": "ပြုသည်", "Arahā dadeyya": "ရဟန္တာ … ပြုသည်"},   # «dānaṃ dadeyya» first
    "5-799": {"pavaro": "အထူးမြတ်ဆုံး"},                # dvipadānaṃ pavaro (pi-4 «အမွန်မြတ်ဆုံး» is seṭṭho here)
    "5-782": {"pariyāye": "ဘဝအဆက်ဆက်"},               # «apare vā pariyāye» «နောက်ထပ် ဘဝအဆက်ဆက်၌»
    "5-798": {"jātā": "ဖြစ်ပေါ်သော", "viharanti": NONE},   # vedajātā «ဝမ်းမြောက်ခြင်း ဖြစ်ပေါ်»; viharanti only a variant
    "5-803": {"viharati": "နေတော်မူသည်", "jāto": "ဖွားမြင်တော်မူသော"},   # «lokaṃ abhibhuyya viharati»
    "5-820": {"niruddhaṃ": "ချုပ်ငြိမ်းပြီး", "jhānaṃ niruddhaṃ": "ဈာန် ချုပ်ငြိမ်းပြီး"},  # «… ချုပ်ငြိမ်းပြီး ဒုတိယ …»
    "5-851": {"kho": NONE},                             # only in the variant «[evaṃ kho bhikkhave …]»
    "5-857": {"jīvitā": NONE}, "5-858": {"jīvitā": NONE}, "5-859": {"jīvitā": NONE},   # «mātaraṃ jīvitā voropetvā» «အမိကို သတ်၍» (one verb)
    "5-868": {"sabbadā": "အမြဲ"},                       # «tiṭṭhati sabbadā» «အမြဲ တည်နေ၏»
    "5-875": {"para": "အခြား"},                         # parappavādā «အခြား ဝါဒတို့»
    "5-883": {"niccaṃ": "အမြဲ"},                       # «niccaṃ juṇhaṃ hotu» «အမြဲ လရောင် သာပါစေ»
    "5-884": {"pana": NONE},                            # «suvaṇṇo ca pana āsi» (particle)
    "5-887": {"dha": "သဘောတရားများကို စုစည်းရေတွက်ခြင်း"},   # the reference «dha. sa.» (ch1 dha. pa. «ဓမ္မပဒ»)
    "5-897": {"anuyogo": "နိုးကြားစွာ အားထုတ်ခြင်း"},  # jāgariyānuyogo (not the anuyoga heading of ch1)
    "5-901": {"pisuṇaṃ": "ကုန်းချောစကား", "samphaṃ": "အကျိုးမဲ့ စကား", "nillopaṃ": "လုယက်", "hareyya": NONE,
              "tiṭṭheyya": "ဓားပြ တိုက်သည်", "ekāgārikaṃ kareyya": "အိမ်တစ်လုံးကို ဝိုင်းဝန်း လုယက်သည်",
              "kareyya": "လုယက်သည်", "asuci": "မစင်ကြယ်သော သုက်", "dhammaṃ": "အကျင့်"},   # the list as ch30 words it
    "5-31-1-0": {"eka": "တူညီသော"},                   # Ekādhippāya «တူညီသော ရည်ရွယ်ချက်»
    "5-908": {"dhammo": "အကျင့်"}, "5-909": {"dhammaṃ": "အကျင့်"},   # methuno dhammo «မေထုန် အကျင့်»
    "5-911": {"citta": "စိတ္တ"},                         # cittiddhipāda «စိတ္တ ဣဒ္ဓိပါဒ်»
    "5-735": {"satta": "အသညသတ်", "sañña": NONE}, "5-736": {"satta": "အသညသတ်", "sañña": NONE},
    "5-715": {"katvā": "ပြု၍"},                         # «garuṃ katvā» «လေးစားဖွယ်ရာ ပြု၍»
    "5-742": {"mano": "စိတ်", "sukhadukkhaṃ": "သာယာမှု နာကျင်မှု"},   # manosaṅkhāra «စိတ်ဖြင့်»; vokiṇṇasukhadukkhaṃ                   # «yaṃ kiñci rūpaṃ» «ရုပ် ဟူသမျှ»
    "5-708": {"dukkhāya": "ဆင်းရဲဖွယ်ရာ"},                    # uddāna «asātarāgo»
}

FUNCS3 = {
    # antarikā: jhānantarikā «ဈာန်တို့အကြား ကာလ» (ch26), else the module's «ကြားအပိုင်း»
    "antarika3": lambda kw, pali, my: "အကြား ကာလ" if "အကြား ကာလ" in my else R.FUNCS["antarika"](kw, pali, my),
    # aṅga: the member of bojjhaṅga «ဗောဇ္ဈင်» (one Burmese word: the other member, pi-2) = (no direct equivalent) where
    # the FIRST aṅga compound of the Pāli is bojjhaṅga; else «အင်္ဂါ» (maggaṅga «မဂ်၏ အင်္ဂါ» …)
    "anga3": lambda kw, pali, my: NONE if (R.first_compound(R.strip_brackets(pali), [(r"[a-zāīūṃṅñṭḍṇḷ]*bojjhaṅg", "B"),
        (r"[a-zāīūṃṅñṭḍṇḷ]+aṅg", "A"), ("aṅg", "A")]) == "B" and "ဗောဇ္ဈင်" in my) else (
        "အင်္ဂါ" if "အင်္ဂါ" in my else "@prior"),
    # sukha of the Sukhānuppadānakathā «သုခ» (ch24), else the module's f_sukha
    "sukha24": lambda kw, pali, my: "သုခ" if "သုခ" in my else R.f_sukha(kw, pali, my),
    # jano / janassa of puthujjana: the one Burmese word «ပုထုဇဉ်» goes to puthu (pi-2: one word, one member)
    "jana": lambda kw, pali, my: NONE if "puthujjan" in pali.lower() and "ပုထုဇဉ်" in my else "@prior",
    # ṭhiti: viññāṇaṭṭhiti «သိစိတ် တည်ရာ», the life list āyu ṭhiti «တည်တံ့ခြင်း» (pi-1 / pi-2)
    "thiti": lambda kw, pali, my: "တည်ရာ" if "ṇaṭṭhiti" in pali and "တည်ရာ" in my else (
        "တည်တံ့ခြင်း" if "တည်တံ့ခြင်း" in my else ("တည်ရာ" if "တည်ရာ" in my else "@prior")),
    # atta of attabhāva «ကိုယ်ခန္ဓာ» = ကိုယ်; else the pi-1 / pi-2 «အတ္တ», pi-4 «မိမိ»
    "atta": lambda kw, pali, my: "ကိုယ်" if "attabhāv" in pali and "ကိုယ်ခန္ဓာ" in my else (
        "အတ္တ" if "အတ္တ" in my else ("မိမိ" if "မိမိ" in my else "@prior")),
    # dhātū before «ti» (kāma- / rūpa- / arūpadhātūti): the plane «ဘုံ», else the element «ဓာတ်»
    "dhatu_plane": lambda kw, pali, my: "ဘုံ" if "ဘုံ" in my and re.search(r"(kāma|rūpa)dhāt", pali) else (
        "ဓာတ်" if "ဓာတ်" in my else "@prior"),
}


def _ordinals():
    """the ordinal keywords (aṭṭhama, Aṭṭhamavaggo …) with the text's own spelling where it differs."""
    d = {}
    for k, v in ORD.items():
        d[k] = ("@ord:" + k)
        d[k[:1].upper() + k[1:] + "vaggo"] = ("@ordv:" + k)
    return d


def _ord_f(k, whole):
    def f(kw, pali, my):
        v = ORD[k]
        cands = [v + " ဝဂ်", v + "ဝဂ်"] if whole else [v]
        for c in cands:
            if c in my:
                return c
        m = re.search(r"(\S+) ဝဂ်", my)
        if m:
            return (m.group(1) + " ဝဂ်") if whole else m.group(1)
        return "@prior"
    return f


for _k in ORD:
    FUNCS3["ord:" + _k] = _ord_f(_k, False)
    FUNCS3["ordv:" + _k] = _ord_f(_k, True)


def _alt(vals):
    """(«a», «b», …): the first the segment's Burmese has (presence), else the pi-1 … pi-4 value."""
    def f(kw, pali, my):
        for v in vals:
            if v == NONE or R.presence(v, my)[0]:
                return v
        return "@prior"
    return f


def tables():
    out = {}
    for ch in CHAPTERS:
        d = dict(_ordinals())
        d.update(T_GROUP)
        d.update(T[ch])
        for k, v in list(d.items()):
            if isinstance(v, tuple):
                name = "alt:" + "|".join(v)
                FUNCS3[name] = _alt(v)
                d[k] = "@" + name
        out[ch] = d
    return out


NEG = ("na", "no")


def negate_last(v, my):
    """Q5 for a negative inside a multiword keyword («anāgāmī na parihāyati»): the last verb chunk «Xသည်» becomes the
    text's «မX» (pi-2 «na uppajjati = … မဖြစ်ပေါ်»); else the text's «X … မဟုတ်» (pi-1 rule 5)."""
    head, sep, last = v.rpartition(" … ")
    pre, sp, w = last.rpartition(" ")
    if w.endswith("သည်") and "မ" + w[:-3] in my:
        return head + sep + pre + sp + "မ" + w[:-3]
    if w.endswith("သည်"):
        for i in range(1, len(w) - 3):                       # «Xမ Y»: the text's infix (ဖြစ်ပေါ်… / တွေ့ရ…)
            if w[:i] + "မ" + w[i:-3] in my:
                return head + sep + pre + sp + w[:i] + "မ" + w[i:-3]
    return v + " … မဟုတ်" if "မဟုတ်" in my else v


class Mapper(R.Mapper):
    def lookup(self, ch, sid, kw, pali, my):
        ws = kw.split()
        if len(ws) > 1 and R.low(ws[0]) not in NEG + ("neva",) and any(R.low(w) in NEG for w in ws[1:]) \
                and R.table_get(self.ctx.get(sid, {}), kw) is None and R.table_get(self.tables.get(ch, {}), kw) is None:
            rest = " ".join(w for w in ws if R.low(w) not in NEG)
            v = negate_last(self.lookup(ch, sid, rest, pali, my), my)
            self.SRC[(sid, kw)] = "neg"
            return v
        v = self._lookup(ch, sid, kw, pali, my)
        if len(ws) == 2 and self.SRC.get((sid, kw)) == "compose" and v != NONE:
            v = self.pali_order(ch, sid, ws, v, pali, my)
        return v

    def pali_order(self, ch, sid, ws, v, pali, my):
        """two members joined by compose: (G1) the «ပင်» of eva / va between them is not part of the keyword (as Q4:
        « … »); (G2) where the text has the members in the Pāli order too, that order (an adjacent pair in the other
        order with no particle between them may be a neighbouring phrase: «… စောင့်ရှောက်ခြင်း ရုပ် အသက်…»; an
        adjacency with a particle is the text's own construction and stays: «ဆိုးသော လားရာကို ပယ်ပြီးသော»)."""
        try:
            x, y = (self._lookup(ch, sid, w, pali, my) for w in ws)
        except KeyError:
            return v
        if NONE in (x, y) or R.is_verb(x) or R.is_verb(y) or x == y:
            return v
        for g in ("ပင် ", "သည်ပင် ", "၏ပင် ", "ကိုပင် "):
            if v in (x + g + y, y + g + x):
                v = (x + " … " + y) if v.startswith(x) else (y + " … " + x)
        g_rev = R.glue(y, x, my)
        glued = g_rev is not None and g_rev.strip() and v == y + g_rev + x     # «ဆိုးသော လားရာကို ပယ်ပြီးသော»
        if v.startswith(y) and v.endswith(x) and len(v) > len(y) + len(x) - 1 and not glued:
            px = R.occurrences(x, my)
            py = R.occurrences(y, my)
            if px and py and min(px) < max(py):
                g = R.glue(x, y, my)
                return x + (g.replace("\0", "") if g is not None else " … ") + y
        return v

    def _lookup(self, ch, sid, kw, pali, my):
        if R.table_get(self.ctx.get(sid, {}), kw) is None and R.table_get(self.tables.get(ch, {}), kw) is None \
                and R.table_get(R.FRAME, kw) is None and R.table_get(R.STOCK, kw) is None:
            # G4: another chapter's value of this group, where the segment has it (before the ch1 table)
            for other in CHAPTERS:
                v = R.table_get(T[other], kw) if other != ch else None
                if isinstance(v, str) and v != NONE and not v.startswith("@") and R.presence(v, my)[0]:
                    self.SRC[(sid, kw)] = "group"
                    return v
            v = R.table_get(C1.T_CH1, kw)
            if v is not None:
                try:
                    v = self.resolve(v, kw, pali, my)
                except KeyError:
                    v = None
                if v is not None and R.presence(v, my)[0]:
                    self.SRC[(sid, kw)] = "ch1"
                    return v
        return super().lookup(ch, sid, kw, pali, my)


def mapper():
    funcs = dict(C1.FUNCS1)
    tabs = tables()
    funcs.update(FUNCS3)
    return Mapper(chapter_tables=tabs, ctx=CTX, funcs=funcs)


def main():
    report = "--report" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    M = mapper()
    total = 0
    out = {}
    for ch in (only or CHAPTERS):
        lines, problems, unmapped, nne = M.map_chapter(ch)
        out[ch] = nne
        for sid, kw in unmapped:
            print("UNMAPPED", ch, sid, kw)
        for sid, kw, v in problems:
            print("ABSENT", ch, sid, kw, "=", v)
        total += len(unmapped) + len(problems)
        if not report and not unmapped and not problems:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        elif not report:
            print("NOT WRITTEN", ch)
    if report:
        print("problems", total)
        return
    for ch in (only or CHAPTERS):
        if not (HERE / f"{ch}.mapped.md").exists():
            continue
        n, bad, fails, punct, ruled = R.verify_file(ch)
        print(ch, "lines", n, "bad", bad, "presence failures", len(fails), "punct", punct,
              "ending-rule chunks", len(ruled), "(no direct equivalent)", out[ch])


if __name__ == "__main__":
    main()
