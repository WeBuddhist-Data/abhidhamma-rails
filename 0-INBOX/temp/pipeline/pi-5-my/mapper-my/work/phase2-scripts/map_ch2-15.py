"""Pāli→Burmese keyword mapping for pi-5 (Kathāvatthu), PHASE 2, group ch2–15 (2-parihanikatha … 15-sattamavaggo).

usage (/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8, from any directory):
  map_ch2-15.py             writes <ch>.mapped.md for the 14 chapters of the group, then verifies each (preservation,
                            presence, punctuation) and prints the results per chapter
  map_ch2-15.py --report    writes nothing; lists unmapped keywords and presence failures

Imports the shared module map5_rules.py (phase 1; NOT edited here). This script holds only the chapter tables of the
group (T[ch]), the per-segment overrides (CTX) and the new context functions (FUNCS2). Burmese: the FINAL pi-5 text of
this track only. Module overrides are listed in notes-ch2-15.md («Module overrides»).
"""
import sys
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map5_rules as R  # noqa: E402
import map_ch1 as C1  # noqa: E402  (tables only; map_ch1 runs nothing on import)

NONE = R.NONE
CHAPTERS = ["2-parihanikatha", "3-brahmacariyakatha", "4-jahatikatha", "5-sabbamatthitikatha",
            "6-atitakkhandhadikatha", "7-ekaccam-atthitikatha", "8-satipatthanakatha", "9-hevatthikatha",
            "10-dutiyavaggo", "11-tatiyavaggo", "12-catutthavaggo", "13-pancamavaggo", "14-chatthavaggo",
            "15-sattamavaggo"]

# ------------------------------------------------------------------------------------------------ shared in the group
# values that recur in several chapters of the group (consulted after the chapter's own table, before the module)
T_GROUP = {
    # ^5-274 … ^5-278 the partial abandoning (ch3; recurs in ch10)
    "pasādena": "ကြည်ညိုမှု", "avecca": "ခိုင်မြဲသော", "kolaṅkolo": "အမျိုးမှ အမျိုးသို့ ကူးသူ",
    "ekabījī": "မျိုးစေ့ တစ်စေ့သာ ရှိသူ", "upasampajja": "ပြည့်စုံစွာ ဝင်ရောက်၍", "paṭiladdho": ("ရရှိပြီးသော", "ရသော"),
    "kantehi": "နှစ်သက်သော", "sīlehi": "သီလ", "kilese": "ကိလေသာ", "ekadese": "တစ်စိတ်တစ်ဒေသ",
    "ekaṭṭhe": "တစ်နေရာတည်း တည်ရှိသော", "dassanena": "မြင်ခြင်း", "kāmarāgaṃ": "ကာမရာဂ",
    "jahitā": "စွန့်ပယ်ပြီးသော", "dassana": "အမြင်", "abhabba": "မစွမ်းနိုင်", "abhabbo": "မစွမ်းနိုင်",
    "kātuṃ": "ပြုလုပ်ရန်", "abhiṭhānāni": "ကြီးလေးသော ဒုစရိုက်", "vippamutto": "လွတ်မြောက်ပြီးသော",
    "apāyehi": "အပါယ်", "udapādi": "ဖြစ်ပေါ်သည်", "sāvakassa": "တပည့်", "virajaṃ": "မြူ ကင်းသော",
    "vītamalaṃ": "အညစ်အကြေး ကင်းသော", "khu": "မျက်စိ", "samudaya": ("ဖြစ်ပေါ်တတ်သော",),
    "kālaṃ karoti": "သေသည်", "saha": "တစ်ပြိုင်နက်",
    "niddhame": "ဖယ်ရှားသည်", "Kammāro": "ပန်းထိမ်သည်", "vicikicchitaṃ": "ယုံမှားခြင်း",
    "Sakkāyadiṭṭhī": "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ", "Sīlabbataṃ": "သီလ အကျင့်ဝတ်", "diṭṭhī": "အယူ",
    "kiñci": "တစ်စုံတစ်ရာ", "medhāvī": "ပညာရှိ",
    "odhiso": "အပိုင်းအပိုင်း", "vāso": "ကျင့်သုံးခြင်း", "adhivacana": "အမည်ခေါ်ဝေါ်မှု", "viññūhi": "ပညာရှိ",
    "atītānāgatā": "အတိတ်နှင့် အနာဂတ်", "Atītānāgato": "အတိတ်နှင့် အနာဂတ်", "atītakkhandha": "အတိတ် အစုအဝေး",
    "aṇusahagato": "အနည်းငယ်မျှ ကျန်ရှိသော", "apāyagamanīyo": "အပါယ်သို့ ရောက်စေတတ်သော",
    "Sattamavaggo": "သတ္တမ ဝဂ်", "upasampajja": ("ပြည့်စုံစွာ ဝင်ရောက်၍", "ပြည့်စုံစေ၍"),
    "aṅgo": NONE, "pahīnaṃ": "ပယ်ပြီးသော", "janassa": NONE, "sattesu": ("သတ္တဝါ", NONE), "vimutti": "လွတ်မြောက်ခြင်း", "atta": NONE,
    "ida": "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ",
    "thero": "မထေရ်", "Sāriputto thero": "သာရိပုတ္တရာ မထေရ်", "mahāpanthako thero": "မဟာပန္ထက မထေရ်",
    "arahanta": "ရဟန္တာ", "pajahati": "ပယ်သည်", "jana": NONE, "puna": "@puna",
    "bala": "စွမ်းအား", "balā": "စွမ်းအား", "cakka": "စက်",
    "gamanīyo": "ရောက်စေတတ်သော", "apāya": "အပါယ်", "yutti": "ယုတ္တိ", "sādhana": "သက်သေပြခြင်း",
    "sādhanaṃ": "သက်သေပြခြင်း", "sodhanā": "စိစစ်ခြင်း", "sodhana": "စိစစ်ခြင်း",
    "saṃsandana": "နှိုင်းယှဉ်ခြင်း", "brahmacariyavāso": "မြင့်မြတ်သော အကျင့်ကို ကျင့်သုံးခြင်း",
    "ekadesaṃ": "တစ်စိတ်တစ်ဒေသ", "adhigato": "ပိုင်ဆိုင်ပြီးသော", "avijjaṃ": "အမှန်ကို မသိမှု",
    "Sakkāyadiṭṭhiṃ": "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ", "sakkāyadiṭṭhiṃ": "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ",
    "sotāpattiphalappatto": "သောတာပတ္တိဖိုလ်သို့ ရောက်ပြီးသော",
    "sakadāgāmiphalappatto": "သကဒါဂါမိဖိုလ်သို့ ရောက်ပြီးသော",
    "anāgāmiphalappatto": "အနာဂါမိဖိုလ်သို့ ရောက်ပြီးသော", "arahattappatto": "ရဟန္တာ အဖြစ်သို့ ရောက်ပြီးသော",
    "Sotāpattiphalasacchikiriyāya": "သောတာပတ္တိဖိုလ်ကို မျက်မှောက်ပြုရန်",
    "Sakadāgāmiphalasacchikiriyāya": "သကဒါဂါမိဖိုလ်ကို မျက်မှောက်ပြုရန်",
    "Anāgāmiphalasacchikiriyāya": "အနာဂါမိဖိုလ်ကို မျက်မှောက်ပြုရန်",
    "Arahattasacchikiriyāya": "ရဟန္တာ အဖြစ်ကို မျက်မှောက်ပြုရန်",
    "Aṇusahagataṃ": "အနည်းငယ်မျှ ကျန်ရှိသော", "aṇusahagataṃ": "အနည်းငယ်မျှ ကျန်ရှိသော",
    "Rūparāgaṃ": "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ",
    "ariyakantehi": "အရိယာတို့ နှစ်သက်သော", "ariyakantehi sīlehi": "အရိယာတို့ နှစ်သက်သော သီလ",
    "arahanto": "ရဟန္တာ", "pahīnā": "ပယ်ပြီးသော", "pahīno": "ပယ်ပြီးသော", "pahīnāni": "ပယ်ပြီးသော",
    "upapannassa": "ပြန်လည် ဖြစ်ပေါ်သော", "parinibbāyī": "ပရိနိဗ္ဗာန် ပြုသော", "dhammapade": "“ဓမ္မပဒ”",
    "sammāsambuddhā": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    "ekadesaṃ samannāgato": "တစ်စိတ်တစ်ဒေသ … ပြည့်စုံသော",
    "oḷārikaṃ kāmarāgaṃ jahati": ("ရုန့်ရင်းသော ကာမရာဂကို စွန့်ပယ်သည်", "ရုန့်ရင်းသော ကာမရာဂ … စွန့်ပယ်သည်"),
    "Anāgāmissa": "အနာဂါမ်", "Sotāpannassa": "သောတာပန်", "Sakadāgāmissa": "သကဒါဂါမ်",
    "anāgāmiphala": "အနာဂါမိဖိုလ်", "sakadāgāmiphala": "သကဒါဂါမိဖိုလ်",
    "aṇu": "အနည်းငယ်မျှ", "oḷāriko": "ရုန့်ရင်းသော",
    # the arahant's epithets (^5-260, ^5-261, ^5-277 …)
    "rāgappahānāya": "ရာဂကို ပယ်ရန်", "dosappahānāya": "ဒေါသကို ပယ်ရန်",
    "anottappapahānāya": "ဒုစရိုက်ကို မကြောက်ရွံ့မှုကို ပယ်ရန်",
    "uppāda": "ဖြစ်ပေါ်တော့သော", "anabhāvaṅkato": "မရှိတော့အောင် ပြုသော", "mūlo": "အမြစ်", "vatthu": "ငုတ်တို",
    "tāla": "ထန်းပင်", "aggaḷo": "တံခါးမင်းတုံး", "paligho": "တံခါးကျင်", "ukkhitta": "ဖယ်ရှားပြီးသော",
    "khīṇa": "ကုန်ခန်းပြီးသော", "pari": NONE, "saṃyojano": "နှောင်ကြိုး", "saṅkiṇṇa": "ဖို့ပြီးသော",
    "parikho": "ကျုံး", "abbūḷha": "နုတ်ပစ်ပြီးသော", "esiko": "တိုင်", "panna": "ချပြီးသော",
    "visaññutto": "ကင်းလွတ်ပြီးသော", "vijayo": "အောင်ပွဲ", "vijita": "အောင်ပြီးသော", "ohita": "ချပြီးသော",
    "aññā": "သိ၍", "attho": "အကျိုးစီးပွား", "vītarāgo": "ရာဂ ကင်းသော", "vītadoso": "ဒေါသ ကင်းသော",
    "vītamoho": "မောဟ ကင်းသော", "abhiññeyyaṃ": "ထူးကဲစွာ သိရမည့်", "pariññātaṃ": "ပိုင်းခြား သိပြီးသော",
    "sacchikato": "မျက်မှောက်ပြုပြီးသော", "sacchikātabbaṃ": "မျက်မှောက်ပြုရမည့်",
    "Samayavimutto": "အချိန်အလိုက် လွတ်မြောက်သော", "samayavimuttassa": "အချိန်အလိုက် လွတ်မြောက်သော",
}

T = {ch: {} for ch in CHAPTERS}

CTX = {
    # «Parihāyati arahā» against «ရဟန္တာ၏ ဆုတ်ယုတ်ခြင်း» (parihāni) of the same segment: the proposition's own words
    "5-239": {"Parihāyati arahā": "ရဟန္တာ … ဆုတ်ယုတ်သည်"},
}

# ---- 15-sattamavaggo
T["15-sattamavaggo"].update({
    "Saṅgahitakathā": "အကျုံးဝင်ခြင်း … ဆွေးနွေးချက်",
    "Cetasikakathā": "စိတ်၏ အဖော် ဖြစ်သော သဘောတရား … ဆွေးနွေးချက်", "maya": "ဖြစ်သော",
    "Paribhogamayapuññakathā": "သုံးဆောင်ခြင်းမှ ဖြစ်သော ကောင်းမှု … ဆွေးနွေးချက်",
    "paribhogamayapuñña": "သုံးဆောင်ခြင်းမှ ဖြစ်သော ကောင်းမှု", "Paribhogamayaṃ": "သုံးဆောင်ခြင်းမှ ဖြစ်သော",
    "paribhogamayaṃ": "သုံးဆောင်ခြင်းမှ ဖြစ်သော",
    # ^5-471 … ^5-477 Saṅgahita, Sampayutta, Cetasika
    "jā": "ဖြစ်ပေါ်သော", "gaṇanaṃ": "ရေတွက်ခြင်း", "uddesaṃ": "ညွှန်ပြခြင်း", "sā": "ထို", "gaddulena": "ချိတ်",
    "balibaddā": "နွား", "dāmena": "ကြိုး", "sikkāya": "ချိုင့်ကြိုး", "yottena": "ထမ်းပိုး",
    "uppādā": ("ဖြစ်ပေါ်သော", "ဖြစ်ပေါ်ခြင်း"), "ucchumhi": "ကြံ", "anupaviṭṭhā": "အတွင်းသို့ ဝင်ရောက်နေသော",
    "anupaviṭṭhaṃ": "အတွင်းသို့ ဝင်ရောက်နေသော", "anugatā": "ပျံ့နှံ့သော", "anugataṃ": "ပျံ့နှံ့သော",
    "tilamhi": "နှမ်းစေ့", "anottappāsikā": "ဒုစရိုက်ကို မကြောက်ရွံ့မှု၏ အဖော် ဖြစ်သော", "paloka": "ပျက်စီးတတ်သော",
    "daso": "မြင်သော", "saṃviditassa": "ကောင်းစွာ သိသော", "viditvā": "သိ၍", "ādisati": "ဖော်ပြသည်",
    "vicāritaṃ": "သုံးသပ်ထားသော", "vitakkitaṃ": "ကြံစည်ထားသော",
    # ^5-478 … ^5-484 Dāna, Paribhogamaya
    "iṭṭhaphalaṃ": "လိုလားဖွယ် အသီးအပွင့် ရှိသော", "sukhudrayaṃ": "ချမ်းသာကို ဖြစ်ပေါ်စေသော",
    "sukhudrayo": "ချမ်းသာကို ဖြစ်ပေါ်စေသော", "pucchāya": "@roman", "vuccamānāya": "@roman", "abhisando": "@roman",
    "abhisandā": "စီးဆင်းရာ", "anuyātā": "လိုက်နာ ကျင့်သုံးသော", "saṅkiṇṇa": "ရောယှက်သော", "porāṇāni": "ရှေးကျသော",
    "aggaññāni": "အမြတ်ဆုံးဟု သိအပ်သော", "dānāni": "အလှူ", "mahādānāni": "ကြီးမြတ်သော အလှူ",
    "mahādānaṃ": "ကြီးမြတ်သော အလှူ", "rattaññāni": "ကြာမြင့်စွာ တည်ခဲ့သည်ဟု သိအပ်သော",
    "vaṃsaññāni": "အနွယ်ဟု သိအပ်သော", "asaṅkiṇṇapubbāni": "ရှေး … မရောယှက်ခဲ့သော", "diviyaṃ": "နတ်ပြည်သို့ သွားရာ",
    "abhayaṃ": "ဘေးမဲ့ခြင်း", "averaṃ": "ရန်မဲ့ခြင်း", "abyābajjhaṃ": "ညှဉ်းဆဲမှု ကင်းခြင်း", "byābajjhaṃ": "ညှဉ်းဆဲမှု",
    "aparimāṇānaṃ": "အတိုင်းအဆ မရှိသော", "hiriyaṃ": "ရှက်ခြင်း", "vādaṃ": "ပြောခြင်း", "pānaṃ": "သောက်ဖွယ်",
    "āvasathaṃ": "နေရာ", "annaṃ": "ထမင်း", "vilepanaṃ": ("နံ့သာပျောင်း", "နံ့သာ လိမ်းဖွယ်"), "ekacco": "အချို့သူ",
    "deyyadhammo": "ပေးလှူဖွယ် ဝတ္ထု", "Deyyadhammo": "ပေးလှူဖွယ် ဝတ္ထု", "viya": "ကဲ့သို့", "muñja": "ဖြူဆံမြက်",
    "māluvā": "နွယ်ကြီး", "Dāyako": "အလှူရှင်", "dāyako": "အလှူရှင်", "samannāharati": "စိတ်ကို ဆောင်သည်",
    "āvaṭṭentassa": "စိတ်ကို လှည့်ဆောင်သော", "ābhogassa": "စိတ်ညွတ်သော", "samannāharantassa": "စိတ်ကို ဆောင်သော",
    "manasikarontassa": "နှလုံးသွင်းသော", "cetayantassa": "စေ့ဆော်သော", "patthayantassa": "တောင့်တသော",
    "paṇidahantassa": "ဆုတောင်းသော",
    # ^5-485 … ^5-491
    "vidūrāni": "ဝေးကွာသော", "byāyiko": "ပျက်စီးတတ်သော", "asataṃ": "သူတော်ကောင်း မဟုတ်သော",
    "sappaṭibhāgā": "ဆန့်ကျင်ဘက် ရှိသော", "sammukhībhāvaṃ": "မျက်နှာချင်း ဆိုင်ခြင်း", "dūrataraṃ": "ပို၍ ဝေး",
    "pabha": "အလင်း", "veti": "ပျက်စီးသည်", "abbhudeti": "ထွက်သည်", "verocano": "နေ", "Nabhaṃ": "ကောင်းကင်",
    "manāpāya": "နှစ်သက်ဖွယ်", "sovaggikā": "နတ်ပြည်နှင့် ဆိုင်သော", "gāmino": "သွားသော", "ṭhā": "တည်သော",
    "kārakā": "တည်ဆောက်သူ", "janā": ("လူ", NONE), "Papaṃ": "ရေသောက်ဇရပ်", "upassayaṃ": "နေရာ",
    "dahati": "လောင်သည်", "vahati": "မျှောပါသွားသည်", "dāyādā": "အမွေခံ", "appiyā": "မချစ်ခင်သော",
    "paṭiggāhako": "အလှူခံ", "khādanīyaṃ": "ခဲဖွယ်", "pānīyaṃ": "သောက်ဖွယ်", "bhojanīyaṃ": "စားဖွယ်",
    "yāpenti": "အသက်မွေးသည်", "atthāya": "အတွက်", "pasādenti": "ကြည်လင်စေသည်", "dentaṃ": "ပေးနေသော",
    "anumodenti": "အနုမောဒနာ ပြုသည်", "upakappati": "အထောက်အကူ ဖြစ်သည်", "gorakkha": "နွားမွေးခြင်း",
    "kasī": "လယ်ထွန်ခြင်း", "kālaṅkatā": "သေလွန်သော", "vuṭṭhaṃ": "ရွာသော", "pavattati": "စီးဆင်းသည်",
    "Unname": "ကုန်းမြင့်", "paripūrenti": "ပြည့်စေသည်", "tādisī": "ထိုသို့သော", "Ovāda": "ဆုံးမ စကား",
    "hāpayaṃ": "ဆုတ်ယုတ်စေသော", "posī": "ကျွေးမွေးသော", "jāyamānaṃ": "ဖြစ်ပေါ်လာမည့်", "mātā": "မိဘ",
    "pitaro": NONE, "sampassantā": "မြင်သော", "kālaṅkatānaṃ": "သေလွန်ပြီးသော", "atha": "ထို့ပြင်",
    "dāyajjaṃ": "အမွေ", "dakkhiṇaṃ": "အလှူ", "Bhaṭo": "ဝေယျာဝစ္စ ပြုသူ", "kārinaṃ": "ကျေးဇူး ပြုခဲ့သော",
    "pasaṃsiyo": "ချီးမွမ်းထိုက်သော", "anussaraṃ": "အောက်မေ့၍", "katavedino": "ကျေးဇူးကို ဆပ်တတ်သော",
    "paṇḍitā": "ပညာရှိ",
    # ^5-492 … ^5-501 Vipāka
    "ocinituṃ": "စုဆောင်းရန်", "vicinituṃ": "ရွေးချယ်ရန်", "āṭhapetuṃ": "ပေါင်နှံရန်",
    "Sukhavedaniyā": "သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော", "Sukhavedaniyaṃ": "သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော",
    "dukkhavedaniyā": "နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော", "dukkhavedaniyaṃ": "နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော",
    "acoraharaṇo": "ခိုးသူတို့ မယူဆောင်နိုင်သော", "nidhi": "ရတနာသိုက်", "Kayirātha": "ပြုသည်",
    "care": ("ကျင့်သည်", "ကျင့်လိုသည်"), "macco": "သတ္တဝါ", "paṭilābhāya": ("ရရှိရန်", "ရရန်"),
    "adhipacca": ("အုပ်ချုပ်ခြင်း", "အကြီးအကဲ ဖြစ်ခြင်း"), "Dānaphalaṃ": "ပေးလှူခြင်း၏ အကျိုး",
    "bhāvanāphalaṃ": "ပွားများခြင်း၏ အကျိုး", "mahapphalaṃ": ("အကျိုး ကြီးမားသော", "ကြီးမားသော အကျိုး"),
    "paccati": "ကျက်သည်", "hanati": "သတ်သည်", "modati": "မွေ့လျော်သည်", "upacchedo": "ဖြတ်တောက်ခြင်း",
    "ekaṭṭhe": ("အနက် တူသော", "တစ်နေရာတည်း တည်ရှိသော"),
    "ariyadhamma": "အရိယာ တရား", "ottappena": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု", "anottappena": "ဒုစရိုက်ကို မကြောက်ရွံ့မှု",
    "rāgena": "ရာဂ", "dosena": "ဒေါသ", "paṭikuṭṭhāni": "ကဲ့ရဲ့အပ်သော", "mālaṃ": "ပန်း",
    "sappaṭibhāgā sammukhībhāvaṃ āgacchanti": "ဆန့်ကျင်ဘက် ရှိသော … မျက်နှာချင်း ဆိုင်ခြင်းသို့ ရောက်သည်",
    "Tena hi paribhogamayaṃ puññaṃ": "သို့ဖြစ်လျှင် … သုံးဆောင်ခြင်းမှ ဖြစ်သော ကောင်းမှု", "corā": "ခိုးသူ",
    "parakataṃ": "သူတစ်ပါး ပြုသော", "sukhadukkhaṃ": ("ချမ်းသာနှင့် ဆင်းရဲ", "ချမ်းသာ ဆင်းရဲ"),
    "parakataṃ sukhadukkhaṃ": "သူတစ်ပါး ပြုသော ချမ်းသာ ဆင်းရဲ", "khu": ("မျက်စိ", "“ခုဒ္ဒကပါဌ”"),
    "santo": "သူတော်ကောင်း", "issariyasaṃvattaniyaṃ kammaṃ": "အစိုးရခြင်းကို ဖြစ်စေတတ်သော ကံ",
    "dubbaṇṇasaṃvattaniyaṃ kammaṃ": "အဆင်း ဆိုးခြင်းကို ဖြစ်စေတတ်သော ကံ",
    "savipākaṃ ācayagāmī": "အကျိုး ရှိ၍ စုပုံခြင်းဆီသို့ ဦးတည်သော", "savipākaṃ": "အကျိုး ရှိ၍",
    "ācayagāmī": "စုပုံခြင်းဆီသို့ ဦးတည်သော",
    "saṅgahita": "အကျုံးဝင်ခြင်း", "Sampayuttakathā": "ယှဉ်တွဲခြင်း … ဆွေးနွေးချက်",
    "cetasika": "စိတ်၏ အဖော် ဖြစ်သော သဘောတရား", "nirodhā": ("ချုပ်ငြိမ်းသော", "ချုပ်ငြိမ်းခြင်း"),
    "vitakketi": "စတင်ကြံစည်သည်", "samādhiṃ": ("သမာဓိ", "တည်ကြည်ခြင်း"), "saṃvattati": "ဖြစ်စေသည်",
    "paribhuñjamāno": "သုံးဆောင်နေသော", "icchanti": "အလိုရှိသည်", "bhāvanā": "ပွားများခြင်း",
    "tiṭṭheyya": "တည်နေသည်", "sāmaññaṃ": "ရဟန်း၏ အဖြစ်", "brahmaññaṃ": "မြင့်မြတ်သူ၏ အဖြစ်",
    "asaṅkiṇṇāni": "မရောယှက်သော",
})

# ---- 14-chatthavaggo
T["14-chatthavaggo"].update({
    "Chaṭṭhavaggo": "ဆဋ္ဌမ ဝဂ်", "paṭiccasamuppāda": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ",
    "Paṭiccasamuppādo": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ", "paṭiccasamuppādo": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ",
    "āruppa": "ရုပ်မရှိသော ဘုံ", "āruppā": "ရုပ်မရှိသော ဘုံ", "nirodhasamāpatti": "ချုပ်ငြိမ်းခြင်း သမာပတ်",
    "Nirodhasamāpatti": "ချုပ်ငြိမ်းခြင်း သမာပတ်", "samuppādenti": "ကောင်းစွာ ဖြစ်ပေါ်စေသည်",
    "abhinibbattenti": "ထူးကဲစွာ ဖြစ်စေသည်", "samuṭṭhāpenti": "ကောင်းစွာ ထစေသည်", "samuṭṭhapenti": "ကောင်းစွာ ထစေသည်",
    "tāṇaṃ": "ကာကွယ်ရာ", "leṇaṃ": "ပုန်းအောင်းရာ", "Abhisambujjhitvā": "ထိုးထွင်း သိ၍", "vivarati": "ဖွင့်ပြသည်",
    "abhisambujjhati": "ထိုးထွင်း သိတော်မူသည်", "niyāmatā": "သေချာခြင်း", "dhammaniyāmatā": "တရား၏ သေချာခြင်း",
    "dhammaṭṭhitatā": "တရား၏ တည်ရှိခြင်း", "ṭhitatā": "တည်ရှိခြင်း", "avitathatā": "မဖောက်ပြန်ခြင်း",
    "anaññathatā": "အခြား မဟုတ်ခြင်း", "avitathāni": "မဖောက်ပြန်သော", "anejā": "မတုန်လှုပ်သော",
    "vuṭṭhahantassa": "ထမြောက်နေသော", "samāpajjantassa": "ဝင်စားနေသော", "cittasaṅkhāro": "စိတ်၏ ပြုပြင်ဖန်တီးမှု",
    "ninnaṃ": "ညွတ်သော", "pabbhāraṃ": "ရှိုင်းသော", "poṇaṃ": "ကိုင်းသော", "bāhuṃ": "လက်မောင်း", "usuṃ": "မြား",
    "pakkhino": "ငှက်", "vikubbanti": "ဖန်ဆင်းသည်", "khipanti": "ပစ်သည်", "laguḷaṃ": "တုတ်",
    "parivāretvā": "ဝန်းရံ၍", "gharāni": "အိမ်", "koṭṭhe": "ကျီ", "koṭṭhāni": "ကျီ", "antaradhāyati": "ကွယ်ပျောက်သည်",
    "tuccha": "ဗလာ", "pūriyamāne": "ဖြည့်နေသော", "khaññamāne": "တူးနေသော", "antaraṃ": "ကြား",
    "tāḷacchiddaṃ": "သော့ပေါက်", "chiddaṃ": "လေသာပြတင်းပေါက်", "thambhānaṃ": "တိုင်", "jalantaṃ": "တောက်လောင်နေသော",
    "sañcāliyamāne": "လှုပ်ယမ်းနေသော", "Niyamo": "သေချာသော လမ်းကြောင်း",
    "uppādenti": "ဖြစ်ပေါ်စေသည်", "Uppādā": "ပွင့်ပေါ်သည်", "tathatā": "ဟုတ်မှန်ခြင်း",
    "abhisameti": "ကောင်းစွာ သိတော်မူသည်", "abhisametvā": "ကောင်းစွာ သိ၍", "passasi": "မြင်သည်",
    "ālokentaṃ": "ရှေ့သို့ ကြည့်သော", "samiñjentaṃ": "ကွေးသော", "abhikkamantaṃ": "ရှေ့သို့ တိုးသွားသော",
    "pasārentaṃ": "ဆန့်သော", "vātapāna": "လေသာပြတင်း", "mahābhūtā": "မဟာဘုတ်", "bhūtā": "မဟာဘုတ်",
    "arahattaniyāmo": "ရဟန္တာ သေချာသော လမ်းကြောင်း", "Sotāpattiniyāmo": "သောတာပတ္တိ သေချာသော လမ်းကြောင်း",
    "arahattaniyāmo asaṅkhato": "ရဟန္တာ သေချာသော လမ်းကြောင်း … ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",
    "Sotāpattiniyāmo asaṅkhato": "သောတာပတ္တိ သေချာသော လမ်းကြောင်း … ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",
    "ākāsānañcāyatanūpagaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်သို့ ရောက်စေသော",
    "ākāsānañcāyatanūpagaṃ kammaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်သို့ ရောက်စေသော ကံ",
})
CTX.update({"5-461": {"karonti": "ဆောက်သည်"}})          # gharāni karonti «အိမ်တို့ကို ဆောက်ကြ၏»

# ---- 13-pancamavaggo
T["13-pancamavaggo"].update({
    "sekha": ("ကျင့်ကြံဆဲသူ", "ကျင့်ကြံမှု"), "viparīta": "ဖောက်ပြန်သော",
    "Anāgatañāṇakathā": "အနာဂတ်ကို သိသော ဉာဏ် … ဆွေးနွေးချက်", "Phalañāṇakathā": "ဖိုလ်ကို သိသော ဉာဏ် … ဆွေးနွေးချက်",
    "Paṭuppannañāṇakathā": "ပစ္စုပ္ပန်ကို သိသော ဉာဏ် … ဆွေးနွေးချက်",
    "Vimuttiñāṇaṃ": "လွတ်မြောက်ခြင်းကို သိသော ဉာဏ်", "vimuttiñāṇaṃ": "လွတ်မြောက်ခြင်းကို သိသော ဉာဏ်",
    "samaṅgissa": "ရရှိထားသော", "Sotāpattiphalasamaṅgissa": "သောတာပတ္တိဖိုလ်ကို ရရှိထားသော",
    "upasampajja": ("ပြည့်စုံစွာ ဝင်ရောက်၍", "ပြည့်စုံစေ၍"), "viditaṃ": "သိပြီးသော", "Sekhassa": "ကျင့်ကြံဆဲသူ",
    "sekhassa": "ကျင့်ကြံဆဲသူ", "sekhaṃ": ("ကျင့်ကြံဆဲသူ", "ကျင့်ကြံမှု"), "aviditaṃ": "မသိရသေးသော",
    "adiṭṭhaṃ": "မမြင်ရသေးသော", "viparīte": "ဖောက်ပြန်သော", "vipariyeso": "ဖောက်ပြန်ခြင်း",
    "viparītaṃ": "ဖောက်ပြန်သော", "gamanāya": "ရောက်ခြင်း", "abhisametuṃ": "ထိုးထွင်း သိသည်",
    "bhabbo": ("ထိုက်တန်သော", "သိနိုင်သော"), "okkamissati": "သက်ဆင်းသည်", "jānāti": ("သိသည်", "သိတော်မူသည်"),
    "paṭisambhidāpattā": "ပိုင်းခြားသိသော ဉာဏ်သို့ ရောက်ပြီးသော", "Sammutiñāṇaṃ": "သမုတ်ကို သိသော ဉာဏ်",
    "sammutiñāṇaṃ": "သမုတ်ကို သိသော ဉာဏ်", "Cetopariyāye": "စိတ်ကို ပိုင်းခြား၍ သိသော",
    "cetopariyāye": "စိတ်ကို ပိုင်းခြား၍ သိသော", "dadantassa": "ပေးနေသော", "sammutisaccamhi": "သမုတ် သစ္စာ",
    "samanantara": "ကောင်းစွာ ကြားမလပ်", "anantara": "ကြားမလပ်", "ārammaṇapaccayataṃ": "အာရုံ အကြောင်း ဖြစ်ခြင်း",
    "adhipatipaccayataṃ": "အကြီးအမှူး အကြောင်း ဖြစ်ခြင်း", "anantarapaccayataṃ": "ကြားမလပ် အကြောင်း ဖြစ်ခြင်း",
    "hetupaccayataṃ": "အမြစ် အကြောင်း ဖြစ်ခြင်း", "sambhavato": "ဖြစ်ပေါ်ရာ", "nidānato": "အစ",
    "bhavissanti": "ဖြစ်သည်", "antarāyā": "အန္တရာယ်", "mithubhedā": "အချင်းချင်း ကွဲပြားခြင်း", "mithu": "အချင်းချင်း",
    "pharasuṃ": "ပုဆိန်", "kudhāriṃ": "ပုဆိန်ငယ်", "vāsiṃ": "ပေါက်ပြား", "tacchati": "ခုတ်သည်", "gūthaṃ": "ကျင်ကြီး",
    "piyāyati": "နှစ်သက်သည်", "vedeti": "ခံစားသည်", "ceteti": "စေ့ဆော်သည်", "aṅgulaggaṃ": "လက်ချောင်းဖျား",
    "kataṃ": "ပြုလုပ်ချက်", "paññāpeti": "သတ်မှတ်ဖော်ပြသည်", "akkhātā": "ဟောကြားသူ", "upaharato": "ဆောင်ယူပေးခြင်း",
    "upaladdhiṃ": "တွေ့ရခြင်း", "paṇṇāsako": "ငါးဆယ်အစု",
    "asekha": "ကျင့်ကြံမှု ပြီးဆုံးသူ", "asekhaṃ": "ကျင့်ကြံမှု ပြီးဆုံးသူ", "sammutiṃ": "သမုတ်",
    "samuṭṭhānato": "ထကြွရာ", "mūlato": "မူလ", "hetuto": "အမြစ်", "vicāreti": "ဆက်လက်သုံးသပ်သည်",
    "matthakaṃ": "ဦးခေါင်း", "sañjānāti": "မှတ်သိသည်", "jānanti": "သိသည်",
    "arahattaphalasamaṅgissa": "ရဟန္တာ ဖိုလ်ကို ရရှိထားသော", "anāgāmiphalasamaṅgissa": "အနာဂါမိဖိုလ်ကို ရရှိထားသော",
    "sakadāgāmiphalasamaṅgissa": "သကဒါဂါမိဖိုလ်ကို ရရှိထားသော", "vimuttaṃ": "လွတ်မြောက်ပြီးသော",
    "abhisametuṃ": ("ထိုးထွင်း သိသည်", "ထိုးထွင်း သိနိုင်သော"),
    "sammattaniyāmaṃ okkamissati": "မှန်ကန်မှု၌ သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းသည်",
    "dadantassa": ("ပေးနေသော", "ပေးလှူနေသော"), "saccārammaṇaṃ": "သစ္စာကိုသာ အာရုံပြုသော",
    "sammutiñāṇaṃ saccārammaṇaṃ": "သမုတ်ကို သိသော ဉာဏ် … သစ္စာကိုသာ အာရုံပြုသော", "cittārammaṇaṃ": "@roman",
    "cetopariyāye cittārammaṇaṃ": "@roman", "Phassapariyāye": "တွေ့ထိမှုကို ပိုင်းခြား၍ သိသော",
    "Phassapariyāye ñāṇaṃ": "တွေ့ထိမှုကို ပိုင်းခြား၍ သိသော ဉာဏ်",
    "Anottappapariyāye": "ဒုစရိုက်ကို မကြောက်ရွံ့မှုကို ပိုင်းခြား၍ သိသော",
    "Anottappapariyāye ñāṇaṃ": "ဒုစရိုက်ကို မကြောက်ရွံ့မှုကို ပိုင်းခြား၍ သိသော ဉာဏ်",
    "sūciṃ": "အပ်", "nāsika": "နှာခေါင်း", "sarati": "အောက်မေ့သည်", "sibbeti": "ချုပ်သည်", "khaggaṃ": "ဓား",
    "dhovati": "ဆေးသည်",
})
CTX.update({"5-436": {"saṃkhittaṃ": "တွန့်ဆုတ်နေသော"}})     # «saṃkhittaṃ cittaṃ»: the citta adjective, not the heading

# ---- 12-catutthavaggo
T["12-catutthavaggo"].update({
    "Catutthavaggo": "စတုတ္ထ ဝဂ်", "niyāmokkanti": "သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းခြင်း",
    "Niyāmokkantikathā": "သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းခြင်း … ဆွေးနွေးချက်",
    # ^5-387 Gihissa arahā
    "paṭiggaṇheyya": "ခံယူသည်", "citta": ("စိတ်", "အရောင်စုံ"), "vāla": NONE, "moḷiṃ": "ဆံထုံး", "dasāni": "အနားစ",
    "tittira": "ခါ", "vaṭṭaka": "ငုံး", "mora": "ဒေါင်း", "kapiñjaraṃ": "ငှက်ကြီး", "yāvajīvaṃ": "အသက်ထက်ဆုံး",
    "kula": "အမျိုးကောင်း", "byañjanena": "အသွင်", "setu": "သေတု", "uttiyo": "ဥတ္တိယ", "yaso": "ယသ",
    "gihisaṃyojanaṃ": "လူဝတ်ကြောင်၏ နှောင်ကြိုး", "gotama": "ဂေါတမ", "bho": "အသျှင်", "antakaro": "အဆုံးကို ပြုသော",
    "vaccha": NONE, "vacchagotto": "ဝစ္ဆဂေါတ္တ", "paribbājako": "ပရိဗိုဇ်",
    # ^5-388 … ^5-399
    "cuti": ("စုတိ", "စုတေ"), "Upapattesiyena": "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော", "kameyya": "ထိရောက်သည်",
    "Taññeva": "ထို … ပင်", "Satataṃ": "အမြဲတမ်း", "abbokiṇṇaṃ": "ကြားမလပ်", "phoṭṭhabbaṃ": "အတွေ့အထိ",
    "vigatāya": "ကင်းပျောက်သော", "paṭipassaddhāya": "ငြိမ်းအေးသွားသော", "bodhipaṭilābhā": "ဗောဓိကို ရခြင်း",
    # ^5-400 … ^5-405 Lakkhaṇa, Niyāmokkanti
    "bodhisatto": "ဘုရားလောင်း", "Bodhisatto": "ဘုရားလောင်း", "bodhisattassa": "ဘုရားလောင်း", "padesa": "အချို့",
    "pacchā": "နောက်မှ", "jāyamānassa": "မွေးဖွားနေသော", "cakkavattisattassa": "စကြဝတေး မင်းလောင်း",
    "paṭiggaṇhanti": "ခံယူသည်", "byāmaṃ": "တစ်လံ", "pakati": "ပကတိ", "udakakiccaṃ": "ရေ၏ ကိစ္စ",
    "seṭṭho": "အမြတ်ဆုံး", "jeṭṭho": "အကြီးဆုံး", "abhimukho": "မျက်နှာမူသော", "pādehi": "ခြေ",
    "patiṭṭhahitvā": "ရပ်၍", "chatte": "ထီး", "setamhi": "ဖြူ", "sampati": "ပြီးခါစ", "pada": "လှမ်း",
    "viloketi": "ကြည့်သည်", "mātu": ("အမိ", "မယ်တော်"), "devaputtā": "နတ်သား", "Mahesakkho": "တန်ခိုးကြီးသော",
    "cālassa": "မြေငလျင်", "obhāsassa": "အရောင်", "obhāsati": "ထွန်းလင်းသည်", "attamanā": ("နှစ်သက်သော", "ဝမ်းမြောက်သော"),
    "dhārā": "အလျဉ်", "sena": "စစ်တပ်", "pamaddanā": "နှိမ်နင်းနိုင်သော", "vīra": "သူရဲကောင်း", "patto": NONE,
    "agāraṃ": "လူ့ဘောင်", "anto": "အဆုံး", "thāvariya": "တည်တံ့ခိုင်မြဲစေသော", "vijitāvī": "စစ်အောင်နိုင်သော",
    "anagāriyaṃ": NONE, "chado": "အဖုံးအကာ", "sāgara": "သမုဒ္ဒရာ", "dvattiṃsa": "သုံးဆယ့်နှစ်ပါး",
    "abhisambuddhāni": "ထိုးထွင်း သိတော်မူခဲ့သော", "okkantaniyāmo": "သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းပြီးသော",
    "kassapassa": "ကဿပ", "caritabrahmacariyo": "မြင့်မြတ်သော အကျင့်ကို ကျင့်ပြီးသော", "pāvacane": "သာသနာ",
    "Anussaviyo": "သူတစ်ပါးထံမှ ကြားနာ၍ သိသော", "uddisi": "ညွှန်ပြခဲ့သည်", "tapaṃ": "ခြိုးခြံသော အကျင့်",
    "Citto": "စိတ္တ", "hatthako": "ဟတ္ထက", "akāsi": "ကျင့်ခဲ့သည်", "Eko": "တစ်ဆူတည်းသော", "sītibhūto": "အေးငြိမ်းသော",
    "nibbuto": "ငြိမ်းချမ်းသော", "āhañchaṃ": "တီးသည်", "Andhībhūtasmiṃ": "ကန်းနေသော", "dundubhiṃ": "စည်",
    "puraṃ": "မြို့", "pavattetuṃ": "လည်စေရန်", "paṭijānāsi": "ဝန်ခံသည်", "ananta": "အဆုံးမဲ့",
    "Jitā": "အောင်နိုင်သော", "upaka": "ဥပက", "jinā": "အောင်နိုင်သူ", "ve": ("ဧကန်", NONE), "Mādisā": "ငါကဲ့သို့သော",
    "dudrabhinti": "@roman", "sadiso": "တူသော", "devakasmiṃ": "နတ်နှင့်တကွသော", "paṭipuggalo": "ပြိုင်ဘက် ပုဂ္ဂိုလ်",
    "vidū": "သိသော", "anupalitto": "လိမ်းကျံသော",
    "kameyya": ("ထိရောက်နိုင်သည်", "ထိရောက်သည်"), "okkantaniyāmo": ("သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းပြီးသော",
                                                                   "သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းသော"),
    "tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya": "ခါ … ငှက်ကြီး … ခံယူသည်",
    "anāsavaṃ taṃ sāsavaṃ": "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော … စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော",
    "sāsavaṃ taṃ anāsavaṃ": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော … စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော",
    "tīṇi phalāni paṭiladdhāni": "ဖိုလ် သုံးပါးတို့ကို ရပြီးသော", "paṭiladdhāni": "ရပြီးသော",
    "bodhiyā bodhikaraṇīyaṃ": "ဗောဓိဖြင့် ဗောဓိ၏ ပြုဖွယ် ကိစ္စ", "bodhikaraṇīyaṃ": "ဗောဓိ၏ ပြုဖွယ် ကိစ္စ",
    "bodhiyo paccupaṭṭhitā": "ဗောဓိ … ထင်ရှား တည်နေသော", "paccupaṭṭhitā": "ထင်ရှား တည်နေသော",
    "Lakkhaṇasamannāgato": "လက္ခဏာတို့နှင့် ပြည့်စုံသော",
    "Lakkhaṇasamannāgato bodhisatto": "လက္ခဏာတို့နှင့် ပြည့်စုံသော … ဘုရားလောင်း",
    "sītassa": "အေးသော", "uṇhassa": "ပူသော", "disā": "အရပ်", "dissāya": "@roman",
    "attamanā": ("နှစ်သက်သော", "ဝမ်းမြောက်သည်"), "hatthako āḷavako": "ဟတ္ထက အာဠဝက",
    "Dassanasampanno": "မှန်ကန်သော အမြင်နှင့် ပြည့်စုံသော", "Dassanasampanno puggalo": "မှန်ကန်သော အမြင်နှင့် ပြည့်စုံသော ပုဂ္ဂိုလ်",
    "dukkarakāriyaṃ": "ပြုရခက်သော အကျင့်", "pahātabbaṃ": "ပယ်ရမည့်", "bhāvetabbaṃ": "ပွားများရမည့်",
    "pariññeyyaṃ": "ပိုင်းခြား သိရမည့်", "Sayaṃ": ("မိမိ", "ကိုယ်တိုင်"),
    "pahāya": "ပယ်၍", "vijānanto": "သိသော", "udakassa": "ရေ", "vivaṭṭa": "ဖွင့်လှစ်ပြီးသော",
    "pabbajati": ("ရဟန်းပြုသည်", "ရဟန်း ပြုသည်"), "purisassa": "ယောကျ်ား", "dhammiko": "တရားနှင့် လျော်သော",
    "dhammarājā": "တရားမင်း", "sattamaṃ": "ခုနစ်ခုမြောက်", "gacchāmi": "သွားသည်", "abhibhū": "လွှမ်းမိုးသော",
    "samitaṃ": "အစဉ်တစိုက်",
    "ānando okkantaniyāmo": "အာနန္ဒာ … သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းပြီးသော",
    "āḷavako okkantaniyāmo": "အာဠဝက … သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းပြီးသော",
})
CTX.update({"5-402": {"para": "ကျော်"}})        # parosahassaṃ «တစ်ထောင်ကျော်» first (parasena «ရန်သူ့» after)

# ---- 11-tatiyavaggo
T["11-tatiyavaggo"].update({
    "Vimuttikathā": "လွတ်မြောက်ခြင်း … ဆွေးနွေးချက်", "vimuccamāna": "လွတ်မြောက်ဆဲ အရာ",
    "vimuccamānaṃ": "လွတ်မြောက်ဆဲ အရာ", "aṭṭhamakassa": "အဋ္ဌမ", "Aṭṭhamakassa": "အဋ္ဌမ",
    "ñāṇakathā": "ဉာဏ် … ဆွေးနွေးချက်",
    # ^5-354 … ^5-356 Bala
    "sabbadassāvī": "အလုံးစုံကို မြင်သော", "paṭisaraṇo": "ကိုးကွယ်ရာ", "jino": "အောင်နိုင်သူ", "aññū": "သိသော",
    "sāmī": "အရှင်", "cariyā": "ကျင့်ကြံမှု", "yogo": ("အားထုတ်မှု", "ထမ်းပိုး"), "desanā": "ဟောကြားခြင်း",
    "vidū": "နားလည်သော", "kovido": "ကျွမ်းကျင်သော", "sādhāraṇaṃ": "ဆက်ဆံသော",
    "sāvakasādhāraṇaṃ": "တပည့်တို့နှင့် ဆက်ဆံသော", "khīṇā": ("ကုန်ခန်းပြီးသော", "ကုန်သော"),
    "sabbattha": ("နေရာတိုင်း", "ဘုံ အားလုံး"), "nānākaraṇaṃ": "ကွဲပြားမှု", "adhimuttikataṃ": "@roman",
    "sandhāya": "@roman", "paṭikkhepo": "@roman", "pakkhaṃ": "@roman", "bhinnaṃ": "@roman", "ādayo": "@roman",
    # ^5-357 … ^5-370 Vimutti, Vimuccamāna
    "jātaṃ": ("ပေါ်ပေါက်သော", "ဖြစ်ပေါ်သော"), "bhaṅga": "ပြိုပျက်ခြင်း", "aṅgaṇe": "အမည်းအစက်",
    "dussamānaṃ": "ဒေါသ ဖြစ်ဆဲ", "kilissamānaṃ": "ညစ်နွမ်းဆဲ", "muyhamānaṃ": "တွေဝေဆဲ", "rajjamānaṃ": "တပ်မက်ဆဲ",
    "tena": ("သို့ဖြစ်လျှင်", "ထို"),
    # ^5-371 … ^5-372 Aṭṭhamaka
    "elamūgo": "ဆွံ့အသော", "hīna": "ယုတ်လျော့သော", "vadāmi": "ဆိုသည်", "pakkhe": "ဘက်", "mudutarehi": "နုံ့သော",
    # ^5-373 … ^5-378 Dibbacakkhu, Dibbasota, Yathākammūpaga
    "maṃsa": "ပကတိ", "Maṃsacakkhuṃ": "ပကတိ မျက်စိ", "upatthaddhaṃ": "ထောက်ပံ့မှုကို ရသော", "ānubhāvo": "အစွမ်း",
    "pamuccati": "လွတ်မြောက်သည်", "Maṃsasotaṃ": "ပကတိ နား", "sotāni": "နား", "vata": ("အမှန်ပင်", "အကျင့်ဝတ်", NONE),
    "bhonto": "အချင်း", "paṇidhi": ("ဆုတောင်းခြင်း", "ဆုတောင်းမှု", "ဆုတောင်း"),
    # ^5-379 … ^5-386 Saṃvara, Asaññakathā
    "asaṃvaro": "မစောင့်စည်းမှု", "pamādaṭṭhānā": "မေ့လျော့ခြင်း၏ အကြောင်း", "āvāso": "နေရာ ဘုံ",
    "attabhāvapaṭilābho": "ကိုယ်ခန္ဓာ ရရှိခြင်း", "attabhāva": "ကိုယ်ခန္ဓာ", "atta": NONE,
    "Saññābhavo": "မှတ်သိမှု ရှိသော ဘဝ", "saññābhavo": "မှတ်သိမှု ရှိသော ဘဝ", "saññabhavo": "မှတ်သိမှု ရှိသော ဘဝ",
    "saññāsaṃsāro": "မှတ်သိမှု ရှိသော သံသရာ", "cuti": "စုတေ", "aggaṃ": NONE,
    "dibbacakkhu": "နတ်မျက်စိ", "dibbacakkhuṃ": "နတ်မျက်စိ", "paññācakkhuṃ": "ပညာမျက်စိ",
    "akkhāsi": ("ဟောကြားတော်မူခဲ့သည်", "ဟောကြားတော်မူသည်"), "kāle": "အချိန်",
    "Tathāgatabalaṃ": "ဘုရားဆိုင်ရာ စွမ်းအား", "tathāgatabalaṃ": "ဘုရားဆိုင်ရာ စွမ်းအား",
    "sāvakabalaṃ": "တပည့်၏ စွမ်းအား", "Saphassaṃ cittaṃ": "တွေ့ထိမှု ရှိသော စိတ်",
    "Savedanaṃ cittaṃ": "ခံစားမှု ရှိသော … စိတ်", "diṭṭhipariyuṭṭhānaṃ": "အယူ ထကြွခြင်း",
    "appahīno": "မပယ်ရသေးသော", "arahattasacchikiriyāya": ("ရဟန္တာ ဖိုလ်ကို မျက်မှောက်ပြုရန်",),
    "Yathākammūpagataṃ": "ကံအားလျော်စွာ ရောက်သွားခြင်းကို သိသော", "sacchikato": ("မျက်မှောက် ပြုရသေးသော",),
    "Āyasmā sāriputto": "အသျှင် သာရိပုတ္တရာ", "merayamajja": "အရက် မူးယစ်ဖွယ်",
    "asaññabhavo": "မှတ်သိမှု မရှိသော ဘဝ", "Asaññabhavo": "မှတ်သိမှု မရှိသော ဘဝ",
    "asaññasaṃsāro": "မှတ်သိမှု မရှိသော သံသရာ", "saññākaraṇīyaṃ": "မှတ်သိမှု၏ ပြုဖွယ် ကိစ္စ",
    "saññāya saññākaraṇīyaṃ": "မှတ်သိမှုဖြင့် မှတ်သိမှု၏ ပြုဖွယ် ကိစ္စ",
    "tathāgatabalaṃ taṃ sāvakabalaṃ": "ဘုရားဆိုင်ရာ စွမ်းအား … တပည့်၏ စွမ်းအား", "vimutti": "လွတ်မြောက်ခြင်း",
    "dibbasota": "နတ်နား", "dibbasotaṃ": "နတ်နား", "sabbaññū": "အလုံးစုံကို သိသော", "uppādetā": "ဖြစ်ပေါ်စေသူ",
    "sañjanetā": "ပေါ်ပေါက်စေသူ", "akkhānaṃ": "ပြောကြားခြင်း", "sañjātassa": "ပေါ်ပေါက်သော",
    "samattā": "ပြည့်စုံခြင်း", "paripūrattā": "ပြည့်ဝခြင်း", "sabbathā": "လုံးဝ", "ṭhāyino": "@roman",
    "saññāyoni": "မှတ်သိမှု ရှိသော မွေးဖွားရာ အမျိုးအစား", "asaññayoni": "မှတ်သိမှု မရှိသော မွေးဖွားရာ အမျိုးအစား",
    "saññāgati": "မှတ်သိမှု ရှိသော လားရာ", "asaññagati": "မှတ်သိမှု မရှိသော လားရာ",
})
CTX.update({
    # ^5-371 the sentence «Aṭṭhamako puggalo duppañño elamūgoti? Na hevaṃ vattabbe» has no Burmese (text omission)
    "5-371": {"elamūgo": NONE, "duppañño": NONE},
})

# ---- 10-dutiyavaggo
T["10-dutiyavaggo"].update({
    # headings and the uddāna
    "upahāra": "ဆောင်ယူပေးခြင်း", "ñāṇa": ("ဉာဏ်", "သိခြင်း"), "aññāṇa": "မသိခြင်း", "vitāraṇa": "ရှင်းပြပေးခြင်း",
    "vitāraṇā": "ရှင်းပြပေးခြင်း", "bheda": "စကား ထွက်ခြင်း", "vacībheda": "နှုတ်ဖြင့် စကား ထွက်ခြင်း",
    "āhārakathā": "ဆိုခြင်း … ဆွေးနွေးချက်", "āhāra": "ဆိုခြင်း", "āhāro": "ဆိုခြင်း", "ṭhiti": "တည်ခြင်း",
    "cittaṭṭhiti": "စိတ်၏ တည်ခြင်း", "kukkuḷa": "ပြာပူ", "kukkuḷā": "ပြာပူ", "abhisamaya": "ထင်ထင်ရှားရှား သိမြင်ခြင်း",
    "vohāra": "ပြောဆို သုံးနှုန်းခြင်း", "Nirodhakathā": "ချုပ်ငြိမ်းခြင်း … ဆွေးနွေးချက်",
    "Vacībhedo": "နှုတ်ဖြင့် စကား ထွက်ခြင်း",
    # ^5-307 … ^5-313 Parūpahāra
    "upasaṃharanti": "ဆောင်ယူပေးသည်", "kāyikā": "အပေါင်းအပါ", "Mārakāyikā": "မာရ်နတ်၏ အပေါင်းအပါ",
    "sukkavissaṭṭhi": "သုက်ထွက်ခြင်း", "vissaṭṭhi": "ထွက်ခြင်း", "sukka": "သုက်", "asuci": "မစင်ကြယ်သော",
    "asuciṃ": "မစင်ကြယ်သော", "sukkavissaṭṭhiṃ": "သုက်", "vissaṭṭhiṃ": NONE, "upahāro": ("ဆောင်ယူပေးခြင်း",),
    "keci": ("မည်သူမဆို", "အချို့", NONE), "puthujjanassa": "ပုထုဇဉ်", "janassa": NONE, "janā": NONE,
    "lomakūpehi": "ချွေးပေါက်", "idappaccayatāpaṭiccasamuppannesu":
        "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော",
    "ida": "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ", "asanti": "စားသည်", "pivanti": "သောက်သည်", "khādanti": "ခဲသည်",
    "sāyanti": "လျက်သည်", "asita": "စား", "pīta": "သောက်", "khāyita": "ခဲ", "sāyitassa": "လျက်ထားသော",
    "Dārakā": ("ကလေး", "သူငယ်"), "Paṇḍakā": "ပဏ္ဍုက်", "nissando": "အကျိုးဆက်", "vimatiṃ": "စိတ်ရှုပ်ထွေးခြင်း",
    "āsayo": "သိုလှောင်ရာ", "passāvo": "ကျင်ငယ်", "sādiyeyya": "သာယာသည်", "sayanaṃ": "အိပ်ရာ",
    "uppādeyya": "ဖြစ်စေသည်", "sambādha": "ကျဉ်းကျပ်သော", "paṭiseveyya": "မှီဝဲသည်", "paccanubhaveyya": "ခံစားသည်",
    "ajjhāvaseyya": "နေသည်", "vilepanaṃ": "နံ့သာပျောင်း", "candanaṃ": "စန္ဒကူး", "kāsikacandanaṃ": "ကာသိ စန္ဒကူး",
    "putta": "သားသမီး", "mālā": "ပန်း", "methunaṃ": "မေထုန်", "rajataṃ": "ငွေ", "dhāreyya": "ဆောင်သည်",
    "dhamma": ("အရာ", "တရား", "သဘောတရား"), "kusalassa": "ကျွမ်းကျင်သော", "niddaṃ": "အိပ်ပျော်",
    "satā": "သတိ ရှိသော", "muccati": "ထွက်သည်", "Aṭṭhānaṃ": "အကြောင်း မဟုတ်", "anavakāso": "အခွင့် မဟုတ်",
    "avakāso": "အခွင့်", "bāhirakā": "သာသနာပ", "isayo": "ရသေ့", "arahattaṃ": ("ရဟန္တာ အဖြစ်", "ရဟန္တာ ဖိုလ်", "ရဟန္တာ"),
    # ^5-314 … ^5-321 Aññāṇa, Kaṅkhā
    "paripanthe": "လမ်းခရီး", "sandhiṃ": "အိမ်", "chindeyya": "ဖောက်သည်", "hareyya": "လုယူသည်", "nillopaṃ": "ဥစ္စာ",
    "palapeyya": "ပြောသည်", "ghātaṃ": "ဖျက်ဆီး၍ လုယက်သည်", "haneyya": "သတ်သည်", "tiṭṭheyya": "ဓားပြ တိုက်သည်",
    "pakato": "လွှမ်းမိုးခံရသော", "aññāṇapakato": "မသိခြင်းဖြင့် လွှမ်းမိုးခံရသော",
    "ekāgāriyaṃ kareyya": "အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည်", "dāraṃ": "မယား",
    "avijjāyogo": "အမှန်ကို မသိမှု ထမ်းပိုး", "avijjogho": "အမှန်ကို မသိမှု ရေအလျဉ်",
    "pajahaṃ": "ပယ်၍", "bhabbo": "ထိုက်တန်သော", "abhijānaṃ": "ထူးကဲစွာ သိ၍", "virājayaṃ": "ကင်းစေ၍",
    "parijānaṃ": "ပိုင်းခြား သိ၍", "abhabbo": ("မထိုက်တန်", "မစွမ်းနိုင်"), "virajaṃ": ("မြူမှုန် ကင်းသော", "မြူ ကင်းသော"),
    "atthaṅgamo": "ချုပ်ငြိမ်းသွားခြင်း", "gottaṃ": "အနွယ်", "gotte": "အနွယ်", "purisānaṃ": "ယောက်ျား",
    "nāma": "အမည်", "amaggaṃ": "မဟုတ်", "amagge": "မဟုတ်", "vataṃ": "အကျင့်ဝတ်", "passato": "မြင်သော",
    "Saha": ("တစ်ပြိုင်နက်", "တပြိုင်နက်"), "saha": ("တစ်ပြိုင်နက်", "တပြိုင်နက်"),
    "kiñci": ("တစ်စုံတစ်ရာ", "မှန်သမျှ"), "kiṃ": "အဘယ်", "pajahanti": "ပယ်သည်",
    "brahma": ("မြင့်မြတ်သော", "မြတ်သော"), "carantā": "ကျင့်သော", "Jhāyino": "ဈာန် ဝင်စားသော",
    "arahatte": ("ရဟန္တာ အဖြစ်", "ရဟန္တာ ဖိုလ်"), "Sūriyo": "နေမင်း", "suriyova": "နေမင်း", "iva": "ကဲ့သို့",
    "obhāsayaṃ": "ထွန်းလင်းစေသော", "Vidhūpayaṃ": "ဖြိုခွင်း၍", "senaṃ": "စစ်သည်", "brāhmaṇassa": "ပုဏ္ဏား",
    "pātubhavanti": "ထင်ရှား ပေါ်လာသည်", "jhāyato": "ဈာန် ဝင်စားသော", "Ātāpino": "အားထုတ်သော",
    "pāṇisu": "သတ္တဝါ", "samatikkantā": "လွန်မြောက်ပြီးသော", "huraṃ": "တမလွန်လောက", "vediyā": "ဖြစ်သော",
    "saka": "မိမိ", "jinaṃ": "အောင်မြင်တော်မူသော", "nitthiṇṇa": "ကူးမြောက်သော", "indā": "အရှင်",
    "namassāma": "ရှိခိုးသည်", "Asaṃsayā": "ယုံမှားခြင်း ကင်းသော", "saṃsayā": "ယုံမှားခြင်း",
    "mahapphalaṃ": "ကြီးမားသော အကျိုး", "visaṃyuttā": "နှောင်ကြိုးမှ ကင်းလွတ်သော", "pakāsanā": "ပြသခြင်း",
    "vapayanti": "ကင်းပျောက်သည်",
    # ^5-322 … ^5-325 Paravitāraṇa
    "pattiyo": "ယုံကြည်ရသော", "paṭibaddhabhū": "ချည်နှောင်နေသော", "asammūḷho": "မတွေဝေသော",
    "sahissāmi": "တတ်နိုင်သည်", "kañci": "တစ်စုံတစ်ယောက်", "dhotaka": "ဓောတက", "pamocanāya": "လွတ်မြောက်စေရန်",
    "taresi": "ကူးမြောက်သည်", "seṭṭhaṃ": "မြတ်သော",
    # ^5-326 … ^5-333 Vacībheda
    "Samāpannassa": "သမာပတ်ကို ဝင်စားနေသော", "samāpannassa": ("သမာပတ်ကို ဝင်စားနေသော", "ဝင်စားနေသော"),
    "bhedo": ("စကား ထွက်ခြင်း", "ကွဲပြားခြင်း"), "vacībhedo": "နှုတ်ဖြင့် စကား ထွက်ခြင်း", "samāpattīsu": "သမာပတ်",
    "kāyabhedo": ("ကိုယ်ဖြင့် … ထွက်ခြင်း", "ကိုယ်"), "jānanto": "သိသော", "ākāsānañca": "အဆုံး မရှိသော ဟင်းလင်းပြင်",
    "Lokiyasamāpattiṃ": "လောကနှင့် သက်ဆိုင်သော သမာပတ်", "samuṭṭhānā": "ဖြစ်ပေါ်သော",
    "vitakkavicārā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု", "vacīsaṅkhārā": "နှုတ်၏ ပြုပြင်ဖန်တီးမှု",
    "yuñjatha": "ကြိုးစားသည်", "Ārabbhatha": "အားထုတ်သည်", "nikkamatha": "ထွက်မြောက်သည်",
    "jāti": ("ပဋိသန္ဓေ နေခြင်း", "မွေးဖွားခြင်း"), "assāsapassāsā": "ထွက်သက် ဝင်သက်", "sāsane": "သာသနာ",
    "kuñjaro": "ဆင်", "āgāraṃ": "အိမ်", "naḷa": "ကျူရိုး", "Dhunātha": "ဖြိုဖျက်သည်", "appamatto": "မမေ့မလျော့သော",
    "vihassati": "နေသည်", "viharissati": "နေသည်", "vihessati": "နေသည်", "viññāpesi": "သိစေခဲ့သည်",
    "dasasahassi": "တစ်သောင်း", "sarena": "အသံ", "kaṇḍako": "ဆူးငြောင့်", "uppādako": "စိမ်းစေသူ",
    # ^5-334 … ^5-337 Dukkhāhāra, Cittaṭṭhiti
    "khaṇo": "ခဏ", "sākhaṃ": "သစ်ကိုင်း", "gaṇhati": "ဆွဲကိုင်သည်", "araññe": "တောအုပ်ကြီး", "pavane": NONE,
    "vane": NONE, "muñcitvā": "လွှတ်၍", "makkaṭo": "မျောက်", "caramāno": "လှည့်လည် သွားလာသော",
    "upamā": "ဥပမာ", "Dvecattārīsa": "လေးသောင်းနှစ်ထောင်", "kappasatāni": "ကမ္ဘာ", "kappasahassāni": "ကမ္ဘာ",
    "Ekaṃ": "တစ်ခု", "ekaṃ": "တစ်ခု", "phalānaṃ": "ဝေဟပ္ဖိုလ်", "āyukaṃ": "အသက်",
    "yāvata": "ရှည်သမျှ ကာလပတ်လုံး", "muhuttaṃ": "ခဏခဏ", "vattīnaṃ": ("ဝတ္တီ",),
    # ^5-338 Kukkuḷa
    "sāmañña": ("ရဟန်းအဖြစ်", "ရဟန်း"), "upadhi": "ဥပဓိ", "nirūpadhi": "ဥပဓိ ကင်းသော", "kāyikaṃ": "ကိုယ်",
    "sakkāra": "အရိုအသေ ပြုခံရခြင်း", "ve": "ဧကန်", "ādhipacca": "အကြီးအကဲ ဖြစ်ခြင်း", "anuppattā": "ရောက်ပြီးသော",
    "bhūtesu": NONE, "Abyāpajjaṃ": "မဖျက်ဆီးခြင်း", "byāpajjaṃ": "ဖျက်ဆီးခြင်း", "saṃyamo": "စောင့်စည်းခြင်း",
    "samatikkamo": "လွန်မြောက်ခြင်း", "ādittaṃ": "လောင်ကျွမ်းနေသော", "upasaṃhitā": "စပ်သော",
    "kāmūpasaṃhitā": "ကာမနှင့် စပ်သော", "odhiṃ": "ချွင်းချက်", "rajanīyā": "တပ်မက်ဖွယ်ကောင်းသော",
    "piyarūpā": "ချစ်ဖွယ် သဘော ရှိသော", "tuṭṭhassa": "ရောင့်ရဲသော", "amanāpa": "စိတ်နှင့် မတွေ့ဖွယ်",
    "suladdhaṃ": "ကောင်းစွာ ရသော", "vāsāya": "ကျင့်ရန်", "paramaṃ": ("အမြတ်ဆုံး", "အဆုံးစွန်"),
    "vinayo": "ပယ်ဖျောက်ခြင်း", "udrayaṃ": "ဖြစ်ပေါ်စေသော", "accanta": "အဆုံးစွန်",
    # ^5-339 … ^5-346 Anupubbābhisamaya
    "Anupubbābhisamayo": "အစဉ်အတိုင်း ထင်ထင်ရှားရှား သိမြင်ခြင်း",
    "anupubbābhisamayo": "အစဉ်အတိုင်း ထင်ထင်ရှားရှား သိမြင်ခြင်း",
    "arahattaphalaṃ": "ရဟန္တာ ဖိုလ်", "arahattamaggaṃ": "ရဟန္တာ မဂ်", "anāgāmimaggaṃ": "အနာဂါမိမဂ်",
    "sakadāgāmimaggaṃ": "သကဒါဂါမိမဂ်", "sotāpattimaggaṃ": "သောတာပတ္တိမဂ်", "dakkhanto": "မြင်နေသော",
    "aniccato": "မမြဲ", "catucattārīsa": "လေးဆယ့်လေးပါး", "sotāpattiphalāni": "သောတာပတ္တိဖိုလ်",
    "poṇo": "ညွတ်ကိုင်းသော", "pabbhāro": "စောင်းသော", "ninno": "နိမ့်ဆင်းသော", "sammukhā": "မျက်မှောက်",
    "āvuso": "ငါ့ရှင်", "sutaṃ": "ကြားခဲ့ရသော", "gavampati": "ဂဝမ္ပတိ", "sikkhā": "ကျင့်ခြင်း",
    # ^5-347 … ^5-353 Vohāra, Nirodha
    "lokuttaro": "လောကကို ကျော်လွန်သော", "paṭivijānanti": "ထိုးထွင်း သိသည်", "suṇanti": "ကြားသည်",
    "kopa": "အမျက်", "acakkhu": "မျက်စိ မမြင်ခြင်း", "nirodhiko": "ချုပ်ငြိမ်းစေတတ်သော", "karaṇo": "ပြုတတ်သော",
    "vighāta": "ပင်ပန်းခြင်း", "saṃvattaniko": "ပို့ဆောင်တတ်သော", "pakkhiko": "ဘက်၌ ပါသော",
    "bandhanīyo": "နှောင်ဖွဲ့တတ်သော", "kamanīyo": "လိုချင်ဖွယ်ကောင်းသော", "rajanīyo": "တပ်မက်ဖွယ်ကောင်းသော",
    "mucchanīyo": "တွေဝေစေတတ်သော", "madanīyo": "မူးယစ်စေတတ်သော", "muyheyyuṃ": "တွေဝေသည်",
    "rajjeyyuṃ": "တပ်မက်သည်", "avighāta": "မပင်ပန်းခြင်း", "dusseyyuṃ": "အမျက်ထွက်သည်",
    "elaṇḍiyāya": "ကြက်ဆူပင်", "sovaṇṇamayāya": "ရွှေဖြင့် ပြုလုပ်သော", "laṭṭhiyā": "တုတ်",
    "voharati": "ပြောဆို သုံးနှုန်းသည်", "voharantassa": "ပြောဆိုသော", "sīmā": "နယ်နိမိတ်", "rāji": "မျဉ်းကြောင်း",
    "hīna": "ယုတ်ခြင်း", "paṇīta": "မြတ်ခြင်း", "nirodhenti": "ချုပ်ငြိမ်းစေသည်", "niruddhe": "ချုပ်ငြိမ်းသော",
    "paṭisaṅkhā": "ပြန်လည် ဆင်ခြင်၍", "bhaggā": "ပျက်စီးပြီးသော", "avakaṃso": "ညံ့ဖျင်းခြင်း",
    "Sadhammakusalo": "မိမိ၏ အရာ၌ ကျွမ်းကျင်သော", "sadhammakusalo": "မိမိ၏ အရာ၌ ကျွမ်းကျင်သော",
    "Sadhammakusalassa": "မိမိ၏ အရာ၌ ကျွမ်းကျင်သော", "rāgā": "ရာဂ", "samānaṃ": NONE,
    "avijjāpariyuṭṭhānaṃ": "အမှန်ကို မသိမှု ထကြွခြင်း", "bhaṇeyya": "ပြောသည်",
    "vicikicchāpariyuṭṭhānaṃ": "ယုံမှားမှု ထကြွခြင်း", "paravitāraṇā": "သူတစ်ပါးက ရှင်းပြပေးခြင်း",
    "sikhissa": "သိခီ", "nipāte": "@roman", "tika": "@roman", "dissati": "@roman",
    "saññāvedayitanirodhaṃ": "မှတ်သိမှုနှင့် ခံစားမှု ချုပ်ငြိမ်းခြင်း", "saññāvedayita": "မှတ်သိမှုနှင့် ခံစားမှု",
    "aññaṭṭhānesu": "အခြား နေရာ", "lahuparivattaṃ": "လျင်မြန်စွာ ပြောင်းလဲတတ်သော",
    "lahuparivattā": "လျင်မြန်စွာ ပြောင်းလဲတတ်သော", "uppādakkhaṇo": "ဖြစ်ခြင်း ခဏ",
    "Divaso uppādakkhaṇo": ("နေ့ … ဖြစ်ခြင်း ခဏ",), "soḷasa vassasahassāni": "နှစ် တစ်သောင်းခြောက်ထောင်",
    "vassasahassaṃ": "နှစ် တစ်ထောင်", "rājikānaṃ": "စာတုမဟာရာဇ်", "āyatanikā": NONE, "gihi": "လူဝတ်ကြောင်",
    "nirāmisaṃ": "ကာမဂုဏ် ကင်းသော", "sukhudrayaṃ sukhavipākaṃ": "ချမ်းသာကို ဖြစ်ပေါ်စေသော … ချမ်းသာသော အကျိုး ရှိသော",
    "viveka": "ဆိတ်ငြိမ်ခြင်း", "issariya": "အစိုးရခြင်း", "guṇā": "ဂုဏ်", "yamidaṃ": NONE, "sambodha": "အမှန်ကို သိခြင်း",
    "catubhāgaṃ": "လေးပုံတစ်ပုံ", "Catubhāgaṃ": "လေးပုံတစ်ပုံ", "Niratthiyaṃ": "အကျိုးမဲ့", "āyatakena": "ရုတ်တရက်",
    "aṅgo": NONE, "kopaṭṭhāniyo": "အမျက် ဖြစ်ကြောင်း", "mohaṭṭhāniyo": "မောဟ ဖြစ်ကြောင်း",
    "dosaṭṭhāniyo": "ဒေါသ ဖြစ်ကြောင်း", "nirodhadhammaṃ": ("ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော", "ချုပ်ငြိမ်းခြင်း သဘော ရှိသော"),
    "pīta": ("သောက်",), "uppāda": ("ဖြစ်ခြင်း", "ဖြစ်ပေါ်ခြင်း"), "anuppattā": ("ရောက်ပြီးသော", "ရောက်သော"),
    "khaṇo": ("ခဏ", "အခါ"), "aññā": ("ရဟန္တာ ဖိုလ်",), "accanta": ("အဆုံးစွန်", "လုံးဝ"),
    "amatāni": "အမြိုက်", "paccayo": ("အားကိုးရသော",), "vassasataṃ": "နှစ် တစ်ရာ", "paritta": "ပရိတ္တာဘ",
    "lakkhaṇaṃ": "@roman", "paṭivedho": ("ထိုးထွင်း သိမြင်ခြင်း", "ထိုးထွင်း သိခြင်း"), "uppajjitvā": "ဖြစ်ပေါ်၍",
    "Buddhassa": ("ဘုရားရှင်", "ဘုရား"), "accutāni": "မစုတေသော အရာ", "tāṇāni": "ကာကွယ်ရာ", "leṇāni": "ပုန်းအောင်းရာ",
    "saraṇāni": "ကိုးကွယ်ရာ", "parāyaṇāni": "မှီခိုရာ", "nirodhasaccāni": "ချုပ်ငြိမ်းခြင်း သစ္စာ",
})
CTX.update({
    "5-314": {"ñāṇaṃ": "သိခြင်း"},       # the fragment of aññāṇaṃ «မသိခြင်း» (rule 8)
    "5-338": {"pāṇa": "သတ္တဝါ"},          # pāṇabhūtesu «သတ္တဝါ»
})

# ---- 6-atitakkhandhadikatha … 9-hevatthikatha
T["7-ekaccam-atthitikatha"].update({
    "nirujjhissanti": "ချုပ်ငြိမ်းသည်", "vipakkavipākā": "အကျိုး ရင့်ကျက်ပြီးသော", "vipakka": "ရင့်ကျက်ပြီးသော",
    "avipakkavipākā": "အကျိုး မရင့်ကျက်သေးသော", "avipakkavipākā atthi": "အကျိုး မရင့်ကျက်သေးသော … ရှိသည်",
    "avipakkavipākā dhammā": "အကျိုး မရင့်ကျက်သေးသော … သဘောတရား",
    "vipaccissanti": "အကျိုး ပေးသည်", "atthaṅgataṃ": "ကွယ်ပျောက်ပြီးသော",
    # ^5-300 the text's own series (jāta «မွေးဖွား», not ch5's «ဖြစ်ပေါ်»)
    "jātaṃ": "မွေးဖွားပြီးသော", "sañjātaṃ": "ကောင်းစွာ မွေးဖွားပြီးသော", "nibbattaṃ": "ပေါ်ထွက်ပြီးသော",
    "pātubhūtaṃ": "ထင်ရှားလာပြီးသော", "ajātaṃ": "မမွေးဖွားသေးသော", "uppādino": "ဖြစ်ပေါ်လာမည့်",
})
T["8-satipatthanakatha"].update({
    "ānāpāna": "ထွက်သက် ဝင်သက်", "upasama": "ငြိမ်းချမ်းခြင်း", "cāga": "စွန့်ကြဲမှု", "buddha": "ဘုရား",
    "devatā": "နတ်", "gatā": "အာရုံပြုသော", "aṅgo": NONE, "kāyagatāsati": "ကိုယ်ကို အာရုံပြုသော သတိ",
    "kāyagatāsatiṃ": "ကိုယ်ကို အာရုံပြုသော သတိ", "ekāyana": "တစ်ကြောင်းတည်းသော", "ekāyano": "တစ်ကြောင်းတည်းသော",
    "samohitā": "ယှဉ်တွဲသော", "pariṇāyaka": "ခေါင်းဆောင်", "pātubhāvā": "ထင်ရှား လာခြင်း", "ratanānaṃ": "ရတနာ",
    "cakkavattissa": "စကြဝတေး", "bahulīkaronti": "အကြိမ်ကြိမ် ပြုသည်", "paṭilabhanti": "ရရှိသည်",
    "āsevanti": "အလေ့အကျင့် ပြုသည်", "amataṃ": "အမြိုက်", "paribhuñjanti": "သုံးဆောင်သည်",
    "atthaṅgamāya": "ချုပ်ငြိမ်းရန်", "aṅga": NONE, "assa": "မြင်း", "paridevānaṃ": "ငိုကြွေးခြင်း",
    "ñāyassa": "မှန်ကန်သော နည်းလမ်း", "yadidaṃ": "ယင်းကား", "samatikkamāya": "လွန်မြောက်ရန်",
    "visuddhiyā": "စင်ကြယ်ရန်", "sambojjhaṅga": "ဗောဇ္ဈင်", "satisambojjhaṅga": "သတိ ဗောဇ္ဈင်", "ratanassa": "ရတနာ",
})
T["9-hevatthikatha"].update({
    "atthibhāvo": "ရှိခြင်း၏ အဖြစ်", "Sevatthi": "ထိုအရာပင် ရှိသည်", "vādo": "ဝါဒ", "Pariññā": "ပိုင်းခြား သိခြင်း",
    "Upalabbho": "တွေ့ရခြင်း", "parihāni": "ဆုတ်ယုတ်ခြင်း", "samabhāge": "အချိုး တူသော",
    "tajjāte": "တစ်မျိုးတည်းမှ ဖြစ်သော",
})

# ---- 5-sabbamatthitikatha
T["5-sabbamatthitikatha"].update({
    "kāla": "အချိန်", "samodhāna": "ပေါင်းစုခြင်း", "atītacakkhu": "အတိတ် မျက်စိ", "atītañāṇa": "အတိတ် ဉာဏ်",
    "atītahattha": "အတိတ် လက်", "atītakkhandha": "အတိတ် အစုအဝေး",
    "Sabbena": "အပြည့်အဝ", "yogaṃ": "ဆက်စပ်",
    "ajātaṃ": ("မဖြစ်သေးသော",), "sañjātaṃ": ("ဖြစ်ပေါ်သော",), "abhinibbattaṃ": ("ထင်ရှားစွာ ဖြစ်မြောက်သော",),
    "pātubhūtaṃ": ("ထင်ရှား ပေါ်ပေါက်သော",), "nibbattaṃ": ("ဖြစ်မြောက်သော",),
    "vipariṇataṃ": ("ဖောက်ပြန်ပြောင်းလဲပြီးသော",), "abbhatthaṅgataṃ": ("လုံးဝ ကွယ်ပြီးသော",),
    "vigataṃ": ("ကင်းကွာပြီးသော",), "atthaṅgataṃ": ("ကွယ်ပြီးသော",),
    "samabhāge": "အချိုး တူသော", "tajjāte": "တစ်မျိုးတည်းမှ ဖြစ်သော", "nirujjhamānaṃ": "ချုပ်ငြိမ်းနေသော",
    "vatthaṃ": "အဝတ်", "rajjamānaṃ": "ဆိုးဆေး ဆိုးနေသော",
    "sassataṃ": "ထာဝရ တည်မြဲသော", "niccaṃ": "မြဲသော", "dhuvaṃ": "ခိုင်ခံ့သော", "adhuvaṃ": "မခိုင်ခံ့သော",
    "pañho": "@roman", "pañhehi": "@roman", "yuttataraṃ": "@roman",
    "vatthuṃ": "မှီရာ ဝတ္ထု", "parijānāti": "ပိုင်းခြား သိသည်",
    "anottappī": "ဒုစရိုက်ကို မကြောက်ရွံ့မှု ရှိသော", "Puthujjanassa": "ပုထုဇဉ်", "diṭṭhiko": "အယူ ရှိသော",
    "samiñjana": "ကွေးခြင်း", "pasāraṇaṃ": "ဆန့်ခြင်း", "bandhanehi": "အနှောင်အဖွဲ့",
    "bandhanena": "အနှောင်အဖွဲ့", "bandhituṃ": "နှောင်ဖွဲ့ခြင်း", "saṅkhalika": "သံကြိုး", "nagara": "မြို့",
    "kaṇṭha": "လည်ပင်း", "pañcamehi": "ပဉ္စမ ပြုသော", "rajju": "ကြိုး", "addu": "ခြေချင်း", "nigama": "နိဂုံး",
    "gāma": "ရွာ", "bhedana": "ခွဲခြင်း", "kākehi": "ကျီး", "gijjhehi": "လင်းတ", "kulalehi": "စွန်",
    "sādhāraṇo": "ဆက်ဆံရသော", "pādā": "ခြေ", "abhikkama": "ရှေ့သို့ တက်ခြင်း", "hatthā": "လက်",
    "jighacchā": "ဆာလောင်ခြင်း", "pipāsā": "ရေငတ်ခြင်း", "pabbā": "အဆစ်", "ādāna": "ယူခြင်း",
    "nikkhepanaṃ": "ချခြင်း", "visaṃ": "အဆိပ်", "satthaṃ": "လက်နက်",
    "sammuddho": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်",
    "sammāsammuddho": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    "sambuddhānaṃ": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်",
    "sammāsambuddhānaṃ": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    "sammukhībhāvo": "မျက်မှောက် ဆုံဆည်းခြင်း", "rājūnaṃ": "မင်း", "catupaññāsa": "ငါးဆယ့်လေးပါး",
    "chasaṭṭhi": "ခြောက်ဆယ့်ခြောက်ပါး",
    # ^5-296 the suttas
    "sasokaṃ": "စိုးရိမ်ခြင်း ရှိသော", "rajaṃ": "မြူ", "upāyāsaṃ": "ပြင်းစွာ ပူပန်ခြင်း", "sokaṃ": "စိုးရိမ်ခြင်း",
    "samaṇehi": "ရဟန်း", "brāhmaṇehi": "ပုဏ္ဏား", "pubbe": "ရှေး", "adhivacana": "အမည်ခေါ်ဝေါ်မှု",
    "asaṅkiṇṇapubbā": "ရှေး … ရောနှောခြင်း မရှိခဲ့သော", "asaṅkiṇṇā": "ရောနှောခြင်း မရှိသော",
    "paṭikuṭṭhā": "ကန့်ကွက်အပ်သော", "viññūhi": "ပညာရှိ", "vītivatte": "ကျော်လွန်ပြီးသော", "vaṭṭe": "ဝဋ်",
    "paññāpeyya": ("ထင်ရှားပြသည်", "ထင်ရှားပြနိုင်သည်"), "paññāpayamāno": "ထင်ရှားပြလိုသော",
    "papañce": "ပပဉ္စ တရား", "vaṭume": "သံသရာ လမ်း", "nindā": "ကဲ့ရဲ့ခြင်း", "byārosa": "ပြစ်တင်ခြင်း",
    "upārambha": "အပြစ်တင် စွပ်စွဲခြင်း", "bhayā": "ကြောက်သော", "hetuka": "အကြောင်း", "natthika": "ဘာမျှ မရှိ",
    "garahitabbaṃ": "ကဲ့ရဲ့အပ်", "vassa": "ဝဿ", "nandī": "ပျော်မွေ့မှု", "nandako": "နန္ဒက",
    "kabaḷīkāre": "လုတ်ပြု၍ စားရသော", "āhāre": "အာဟာရ", "patiṭṭhitaṃ": "တည်သော", "virūḷhaṃ": "စည်ပင်သော",
    "phagguno": "ဖဂ္ဂုန", "Atītaṃ nvatthi": "အတိတ် မရှိ", "ñāṇakaraṇīyaṃ": "ဉာဏ်၏ ပြုဖွယ် ကိစ္စ",
    "ñāṇena ñāṇakaraṇīyaṃ": "ဉာဏ်ဖြင့် ဉာဏ်၏ ပြုဖွယ် ကိစ္စ", "bāvīsatindriyāni": "စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး",
    "atītāni bāvīsatindriyāni atthi": "အတိတ် စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး ရှိသည်",
    "nvānāgataṃ": "အနာဂတ် မဟုတ်", "nvātītaṃ": "အတိတ် မဟုတ်",
    "nvānāgataṃ anāgataṃ": "အနာဂတ် မဟုတ်သော အရာသည် အနာဂတ်", "nvātītaṃ atītaṃ": "အတိတ် မဟုတ်သော အရာသည် အတိတ်",
    "sañcetanāya": "စေ့ဆော်ခြင်း", "nāmarūpassa": "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း", "atīte buddhe": "အတိတ် ဘုရားရှင်",
    "atīte paññāpayamāno": "အတိတ် … ထင်ရှားပြလိုသော", "parinibbute": "ပရိနိဗ္ဗာန် စံဝင်တော်မူပြီးသော",
    "saṅkiṇṇa": "ရောနှောခြင်း",
    "anāgataṃ viññāṇaṃ jahati": "အနာဂတ် သိစိတ် … စွန့်ပယ်သည်", "atītaṃ viññāṇaṃ jahati": "အတိတ် သိစိတ် … စွန့်ပယ်သည်",
    "paccuppannaṃ viññāṇaṃ jahati": "ပစ္စုပ္ပန် သိစိတ် … စွန့်ပယ်သည်",
    "sambuddhānaṃ sammukhībhāvo": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင် … မျက်မှောက် ဆုံဆည်းခြင်း", "saṅkhā": "ရေတွက်ခေါ်ဆိုချက်", "vuddhi": ("ကြီးပွားခြင်း", "စည်ပင်ခြင်း", "တိုးပွားခြင်း"),
})
CTX.update({"5-282": {"katvā": "မှတ်ယူ၍"}})

# ---- 4-jahatikatha
T["4-jahatikatha"].update({
    "āharaṇa": "ကိုးကားသော",            # «Nasuttāharaṇa» «သုတ္တန်ကို မကိုးကားသော»: the positive part (rule 8)
    "Accantaṃ": "အပြီးအပိုင်", "avasesaṃ": "အကြွင်း", "appaṭisandhiyaṃ": "ပြန်လည် မဆက်စပ်နိုင်အောင်",
    "paṭisandhiyaṃ": "ပြန်လည် ဆက်စပ်နိုင်အောင်", "samūlaṃ": "အမြစ်နှင့်တကွ",
    "paṭivijjhanto": "ထိုးထွင်း သိမြင်လျက်", "sacchikaronto": "မျက်မှောက်ပြုလျက်", "akuppaṃ": "မပျက်ယွင်းတတ်သော",
    "anāgāmiphalaṃ": "အနာဂါမိဖိုလ်", "ñāṇena": "ဉာဏ်", "bodha": "ထိုးထွင်း သိခြင်း",
    "saṃkilesiyo": "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော",
    "kāmarāgabyāpādaṃ": "ကာမရာဂနှင့် ဖျက်ဆီးလိုစိတ်", "kāmarāgabyāpādānaṃ": "ကာမရာဂနှင့် ဖျက်ဆီးလိုစိတ်",
    "jano": NONE, "avacarena": "ဘုံနှင့် ဆိုင်သော", "anāgāmimaggena": "အနာဂါမိမဂ်",
    "Anāgāmimaggena": "အနာဂါမိမဂ်", "Sakadāgāmimaggena": "သကဒါဂါမိမဂ်", "Sotāpattimaggena": "သောတာပတ္တိမဂ်",
    "Rūpāvacarena": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော", "Vikkhambheti": "ဖိနှိပ်ထားသည်",
    "Arahatte": "ရဟန္တာ အဖြစ်", "abhisamayā": "ထင်ထင်ရှားရှား သိမြင်ခြင်း", "saṇṭhāti": "တည်သည်",
    "anāgāmiphale": "အနာဂါမိဖိုလ်", "samādhīnaṃ": "သမာဓိ", "phassānaṃ": "တွေ့ထိမှု", "saddhānaṃ": "ယုံကြည်မှု",
    "cetanānaṃ": "စေ့ဆော်မှု", "satīnaṃ": "သတိ", "paññānaṃ": "ပညာ",
    # ^5-281 the suttas
    "virājetvā": "ကင်းစေ၍", "atigā": "ကျော်လွန်သော", "adhimuttā": "စိတ်ညွှတ်သော", "upagā": "ရောက်သော",
    "abhisamenti": "ထင်ထင်ရှားရှား သိမြင်သည်", "buddho": "ဘုရားရှင်", "khīṇā": "ကုန်သော",
    "anubuddhaṃ": "အစဉ်အတိုင်း သိပြီးသော", "paṭividdhaṃ": "ထိုးထွင်း သိမြင်ပြီးသော", "puna": NONE,
    "netti": "ကြိုး", "sunetto": "သုနေတ္တ", "sakadāgāmiphalaṃ": "သကဒါဂါမိဖိုလ်", "tanubhāvā": "ပါးလျခြင်း",
    "ciraṭṭhitiko": "ကြာမြင့်စွာ တည်နေသော",
    "dīghāyuko": "အသက် ရှည်သော", "parimutto": "လွတ်မြောက်သည်", "dukkhehi": "ကိုယ်ဆင်းရဲခြင်း", "dukkhasmā": "ဒုက္ခ",
    "sotāpattiphalaṃ": "သောတာပတ္တိဖိုလ်", "gotamena": "ဂေါတမ ဘုရားရှင်", "satāni": "ရာပေါင်း",
    "vimuttiyā": "လွတ်မြောက်မှု", "Ariyassa": "အရိယာ", "sīlassa": "သီလ", "karo": "ပြုတော်မူသော",
    "paṭivedhā": "ထိုးထွင်း သိမြင်ခြင်း", "anubodhā": "အစဉ်အတိုင်း သိခြင်း", "dhammānaṃ": "တရား",
    "yasassino": "ကျော်ကြားသော", "yasassinā": "ကျော်ကြားတော်မူသော", "atītaṃse": "အတိတ်ကာလ",
    "upāyāsehi": "ပြင်းစွာ ပူပန်ခြင်း", "domanassehi": "စိတ်ဆင်းရဲမှု", "paridevehi": "ငိုကြွေးခြင်း",
    "sokehi": "စိုးရိမ်ခြင်း", "āma": "ဟုတ်ပါသည်", "parinibbuto": "ပရိနိဗ္ဗာန် ပြုတော်မူသော",
    "kāmarāgaṃ": "ကာမရာဂ", "gandhā": "အပုပ်နံ့", "akkhāsi": "ဟောကြားတော်မူသည်", "anuttarā": "အမြတ်ဆုံး",
})

# ---- 3-brahmacariyakatha
T["3-brahmacariyakatha"].update({
    "Odhisodhiso": "အပိုင်းအပိုင်း", "odhisodhiso": "အပိုင်းအပိုင်း",
    "devesu": "နတ်", "manussesu": "လူ", "janapadesu": "ဇနပုဒ်",
    # ^5-269 the devas' qualities (privative a- = the text's «မ…», ch1 appiyaṃ; the -ī / -aka words Q8 / P6)
    "paṭibalā": "သိနိုင်သော", "nappaṭibalā": "မသိနိုင်", "aññātuṃ": "သိသည်", "vissajjite": "ဖြေကြားတော်မူသော",
    "arahanta": "ရဟန္တာ", "pucchanti": "မေးသည်", "dubbhāsitānaṃ": "ဆိုးစွာ ဆိုအပ်သော စကား",
    "bhāsita": "ဆိုအပ်သော", "ruhira": "သွေး", "uppādakā": "ထွက်စေသူ", "bhedakā": "ခွဲသူ",
    "bhabbā": "သက်ဆင်းနိုင်သော", "abhabbā": "မသက်ဆင်းနိုင်", "okkamituṃ": "သက်ဆင်းသည်",
    "niyāmaṃ": "သေချာသော လမ်း", "niyāmaṃ okkamituṃ": "သေချာသော လမ်းသို့ သက်ဆင်းသည်",
    "palāpino": "ပြိန်ဖျင်းသော စကားကို ပြောသော", "saṃvācikā": "ပြောဆိုသော", "pasannā": "ကြည်ညိုသော",
    "abhijjhāluno": "သူ့ဥစ္စာကို လိုချင်သော", "elamūgā": "ဆွံ့အသော", "jaḷā": "ထုံထိုင်းသော",
    "cārino": "ကျင့်သော", "micchācārino": "မှားယွင်းစွာ ကျင့်သော", "pitu": "အဖ", "mātu": "အမိ",
    "viññū": "နားလည်တတ်သော", "aviññū": "နားမလည်တတ်သော", "pāṇātipātino": "သူ့အသက်ကို သတ်သော",
    "atipātino": "သတ်သော", "ghātakā": "သတ်သူ", "duppaññā": "ပညာ ညံ့သော", "attamanā": "နှစ်သက်သော",
    "pañhe": "ပြဿနာ", "sammattaṃ": "မှန်ကန်ခြင်း", "vādino": "ပြောသော",
    # ^5-270 … ^5-271
    "uppajjanti": "ပေါ်ပေါက်သည်", "uppajjati": "ပေါ်ပေါက်သည်",
    "sambuddhā": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်", "paccekasambuddhā": "ပစ္စေကဗုဒ္ဓါ",
    "dhāraṇā": "ဆောင်ခြင်း", "kāsāva": "သင်္ကန်း", "muṇḍiyaṃ": "ခေါင်းတုံးခြင်း", "muṇḍo": "ခေါင်းတုံးသော",
    "sāvakayugaṃ": "တပည့် အစုံ", "yugaṃ": "အစုံ", "uppannaṃ": "ပေါ်ပေါက်ခဲ့သော", "Magadhesu": "မဂဓ တိုင်း",
    "bodhiyā": "ဗောဓိပင်", "mūle": "ရင်း", "jāto": "ဖွားမြင်တော်မူသော", "abhisambuddho": "ဘုရား ဖြစ်တော်မူသော",
    "dhamma": "ဓမ္မ", "cakkaṃ": "စကြာ", "pavattitaṃ": "လည်စေတော်မူသော", "pabbajati": "ရဟန်းပြုသည်",
    "Paccantimesu": "အစွန်အဖျား", "milakkhesu": "မိစ္ဆာ လူမျိုး", "gati": "သွားလာခြင်း", "yattha": NONE,
    "viññātāresu": "နားလည်သော", "Sūrā": "ရဲရင့်သော", "satimanto": "သတိ ရှိသော", "sañña": "အသညသတ်",
    "ṭhānehi": "အကြောင်း", "adhiggaṇhanti": "သာလွန်သည်", "uttarakuruke": "ဥတ္တရကုရု ကျွန်း",
    "tāvatiṃse": "တာဝတိံသာ",
    # ^5-272 … ^5-273 the non-returner
    "uppatti": "ဖြစ်ပေါ်ခြင်း", "cutassa": "သေသော", "oharaṇaṃ": "ချခြင်း", "paṭivedho": "ထိုးထွင်း သိမြင်ခြင်း",
    "aṭṭhena": "အကြောင်း", "bhāvitena": "ပွားများခဲ့သော", "bhāvita": "ပွားများခဲ့သော",
    "pahīyanti": "ပယ်သည်", "niṭṭhassa": "ပြီးမြောက်သော", "sallena": "မြား", "migo": "သမင်",
    "viddho": "ထိုးမိသော", "gantvā": "သွား၍", "parinibbāyati": "ပရိနိဗ္ဗာန် ပြုသည်",
    "parinibbāyi": "ပရိနိဗ္ဗာန် ပြုသော", "parinibbāyipuggalo": "ပရိနိဗ္ဗာန် ပြုသော … ပုဂ္ဂိုလ်",
    "gatiyā": "လားရာ", "saṃsārena": "သံသရာ",
    "pariññāta": "ပိုင်းခြား သိရသေးသော", "sacchikata": "မျက်မှောက် ပြုရသေးသော",
    "paṭividdha": "ထိုးထွင်း သိမြင်ရသေးသော", "ohaṭa": "ချရသေးသော", "oharaṇāya": "ချရန်",
    "paṭivedhāya": "ထိုးထွင်း သိမြင်ရန်", "akuppo": "မပျက်ယွင်းတတ်သော",
    "arahattasacchikiriyāya": "ရဟန္တာ အဖြစ်ကို မျက်မှောက်ပြုရန်",
})
CTX.update({
    "5-272": {"pariññātaṃ": "ပိုင်းခြား သိခြင်း"},
    "5-269": {"attha": "အနက်", "dhamme": "တရား"},     # «atthamaññātuṃ» «အနက်ကို မသိနိုင်»; «dhamme pasannā» «တရား၌»       # «dukkhapariññātaṃ» the noun «ဒုက္ခကို ပိုင်းခြား သိခြင်း»
})

# ---- 2-parihanikatha
T["2-parihanikatha"].update({
    # headings
    "parihāni": "ဆုတ်ယုတ်ခြင်း", "yutti": "ယုတ္တိ", "sādhana": "သက်သေပြခြင်း", "parihānāya": "ဆုတ်ယုတ်ခြင်း",
    # ^5-239 the setthi simile
    "parihīno": "ဆုတ်ယုတ်သော", "parihāyamāno": "ဆုတ်ယုတ်နေသော", "phalehi": "ဖိုလ်", "kārento": "ပြုနေသော",
    "sata": NONE, "sahassehi": "သိန်း", "parihāyituṃ": "ဆုတ်ယုတ်သည်", "parihīne": "ဆုတ်ယုတ်သွားသော",
    "seṭṭhī": "သူဌေး", "seṭṭhittaṃ": "သူဌေး အဖြစ်", "sāpateyyā": "ဥစ္စာ",
    # the fruits and the persons (the text's «-ဖိုလ်» compounds; the instrumental / genitive persons by the text's name)
    "anāgāmiphalā": "အနာဂါမိဖိုလ်", "sakadāgāmiphalā": "သကဒါဂါမိဖိုလ်", "sotāpattiphalā": "သောတာပတ္တိဖိုလ်",
    "Anāgāmiphale": "အနာဂါမိဖိုလ်", "Sakadāgāmiphale": "သကဒါဂါမိဖိုလ်", "Sotāpattiphale": "သောတာပတ္တိဖိုလ်",
    "Anāgāminā": "အနာဂါမ်", "Sakadāgāminā": "သကဒါဂါမ်", "Sotāpannena": "သောတာပန်", "Arahatā": "ရဟန္တာ",
    "Anāgāmissa": "အနာဂါမ်", "Sotāpannassa": "သောတာပန်",
    "saṇṭhāti": "တည်သည်", "anantarā": "နောက်တွင် ချက်ချင်း", "jana": NONE,
    "pahīnā": "ပယ်ပြီးသော", "pahīno": "ပယ်ပြီးသော", "aṅga": "@anga", "adhimattā": "လွန်ကဲသော", "oḷāriko": "ရုန့်ရင်းသော", "gamanīyo": "ရောက်စေတတ်သော", "apāya": "အပါယ်",
    "aṇu": "အနည်းငယ်မျှ",
    # ^5-265, ^5-266 the verses
    "samaṇena": "ရဟန်းမြတ်", "pakāsitā": "ထင်ရှားပြတော်မူသော", "ekaguṇaṃ": "တစ်ကြိမ်တည်း", "diguṇaṃ": "နှစ်ကြိမ်",
    "pāraṃ": "ကမ်းတစ်ဖက်", "mutaṃ": "မှတ်ယူအပ်", "taṇho": "တပ်မက်မှု", "ādāno": "စွဲလမ်းမှု", "vijjati": "ရှိသည်",
    "samūhato": "နုတ်ပယ်ပြီးသော", "paticayo": "ထပ်မံ စုဆောင်းခြင်း", "katassa": "ပြုပြီးသော အရာ",
    "Iṭṭhā": "နှစ်သက်ဖွယ်", "aniṭṭhā": "မနှစ်သက်ဖွယ်", "tādino": "ထိုသို့ တည်ကြည်သော",
    "pavedhenti": "တုန်လှုပ်စေသည်", "vippamuttaṃ": "လွတ်မြောက်ပြီးသော", "vayaṃ": "ပျက်ခြင်း",
    "Ṭhitaṃ": "တည်ငြိမ်သော", "ghano": "ခဲနက်", "Selo": "ကျောက်တောင်", "samīrati": "လှုပ်ရှားသည်",
    "santa": "ငြိမ်သက်သော", "phassā": "အတွေ့", "anupassati": "အဖန်ဖန် ရှုသည်",
    # ^5-267, ^5-268
    "kamma": "အလုပ်", "niddā": "အိပ်ခြင်း", "bhassa": "စကားပြောခြင်း",
    "kāmarāgapariyuṭṭhānaṃ": "ကာမရာဂ ထကြွခြင်း", "pajahati": "ပယ်သည်", "pajahitvā": "ပယ်ပြီး၍",
    "ussineti": "စုပုံသည်", "ācinati": "စုဆောင်းသည်", "upādiyati": "စွဲလမ်းသည်", "bhavarāga": "ဘဝရာဂ",
    "bhavarāgānusayo": "ဘဝရာဂ ကိန်းအောင်းခြင်း", "sandhūpeti": "တောက်လောင်စေသည်",
    "pariyuṭṭhito": "ထကြွခြင်းကို ခံရသော", "vidhūpeti": "ငြိမ်းစေသည်", "visineti": "ဖြန့်ကြဲသည်",
    "visinitvā": "ဖြန့်ကြဲပြီး၍", "apacinati": "ဖြိုဖျက်သည်", "apacinitvā": "ဖြိုဖျက်ပြီး၍",
    # multiword keywords the compose rules miss (members in text order, Q3; inner particles stay, rule 1)
    "puthujjana": "ပုထုဇဉ်", "arahanto parihāyanti": "ရဟန္တာ … ဆုတ်ယုတ်သည်",
    "bahutarā kilesā pahīnā": "ကိလေသာတို့ကို ပိုများစွာ ပယ်ပြီးသော",
    "adhimattā": "ပို၍ လွန်ကဲသော",
    "adhimattā bojjhaṅgabhāvanā": "ဗောဇ္ဈင်ကို ပွားများခြင်းသည် ပို၍ လွန်ကဲသော",
    "maggo bhāvito": ("မဂ်ကို ပွားများပြီးသော", "မဂ် … ပွားများပြီးသော"), "bojjhaṅgā bhāvitā": ("ဗောဇ္ဈင်တို့ကို ပွားများပြီးသော", "ဗောဇ္ဈင် … ပွားများပြီးသော"),
    "vimuttassa bhāvito": "လွတ်မြောက်သော … ပွားများပြီးသော",
    # ^5-264 the elders (the text's «မထေရ်»)
    "parihāyittha": "ဆုတ်ယုတ်ခဲ့သည်", "Sāriputto thero parihāyittha": "သာရိပုတ္တရာ မထေရ် … ဆုတ်ယုတ်ခဲ့သည်",
    "mahāpanthako thero parihāyittha": "မဟာပန္ထက မထေရ် … ဆုတ်ယုတ်ခဲ့သည်",
    "Sāriputto parihāyittha": "သာရိပုတ္တရာ … ဆုတ်ယုတ်ခဲ့သည်", "mahāpanthako parihāyittha": "မဟာပန္ထက … ဆုတ်ယုတ်ခဲ့သည်",
    "ādayo": "@roman",
})

CUR = {"ch": None}       # the chapter being mapped (for the context functions that look a part up again)
MM = {}                  # the mapper without the ch1 fallback (set by mapper())


def f_ch1(kw, pali, my):
    """a keyword of the Puggalakathā table (map_ch1.T_CH1) that this group's tables do not have: the ch1 value where
    this segment's Burmese has it (one value book-wide), else the module's own chain (FRAME / STOCK / pi-5 terms /
    pi-1 … pi-4 / compose)."""
    v = R.table_get(C1.T_CH1, kw)
    if v is not None and v.startswith("@"):
        try:
            v = MM["m"].resolve(v, kw, pali, my)
        except KeyError:
            v = None
    if v is not None and R.presence(v, my)[0]:
        return v
    return MM["m"].lookup(CUR["ch"], "", kw, pali, my)


def f_neg(kw, pali, my):
    """«na / no V S» (a negated proposition): the members in text order with the text's «မ + verb» and no «သည်» (Q5,
    pi-2 «na uppajjati = … မဖြစ်ပေါ်»); the module's neg_value checks a gapped value «S … မV» as one phrase and misses
    it, so the negative is built here and checked part by part."""
    ws = kw.split()
    rest = " ".join(w for w in ws if R.low(w) not in ("na", "no"))
    v = MM["m"].lookup(CUR["ch"], "", rest, pali, my)
    if v.endswith(("သည်", "သော")):
        st = v[:-3]
        for sep in (" … ", " "):
            if sep in st:
                head, last = st.rsplit(sep, 1)
                head += sep
                break
        else:
            head, last = "", st
        for cand in (head + "မ" + last, head + last + " မ" + "ဟုတ်"):
            if R.presence(cand, my)[0] and all(p in my for p in cand.split(" … ")):
                return cand
    return R.neg_value(v, my)


FUNCS2 = dict(C1.FUNCS1)
FUNCS2.update({
    "ch1": f_ch1, "neg": f_neg,
    # puna: «တစ်ဖန်» (pi-4); inside punabbhava (one Burmese word «ဘဝသစ်») (no direct equivalent), pi-2 decision 4
    "puna": lambda kw, pali, my: "တစ်ဖန်" if "တစ်ဖန်" in my else (NONE if "punabbhav" in pali.lower() else "@prior"),
})



def tables(ch1=True):
    """{ch: table}: the ch1 fallback (keys of T_CH1 not in FRAME / STOCK), the automatic «na …» entries, the group
    table, the chapter's own table (later wins)."""
    out = {}
    for ch in CHAPTERS:
        d = {}
        if ch1:
            d.update({k: "@ch1" for k in C1.T_CH1 if R.table_get(R.FRAME, k) is None and R.table_get(R.STOCK, k) is None})
        for _, kws in R.keyword_rows(ch):
            for k in kws:
                ws = [R.low(w) for w in k.split()]
                if len(ws) > 2 and ("na" in ws or "no" in ws) or len(ws) == 2 and ws[1] in ("na", "no"):
                    d.setdefault(k, "@neg")
        own = dict(T_GROUP)
        own.update(T[ch])
        for k, v in own.items():       # every table value is checked against the segment (group rule S2): where the
            if isinstance(v, str) and not v.startswith("@") and v != NONE:   # segment lacks it, the module's chain
                v = (v,)
            d[k] = v
        for k, v in list(d.items()):
            if isinstance(v, tuple):              # («a», «b», …): the first the segment's Burmese has, else pi-1 … pi-4
                name = "alt:" + "|".join(v)
                FUNCS2[name] = _alt(v)
                d[k] = "@" + name
        out[ch] = d
    return out


def _alt(vals):
    def f(kw, pali, my):
        for v in vals:                   # first a value the text has as a phrase, then one present by the ending rules
            if v == NONE or R.presence(v, my)[0] and R.phrase_ok(v, my):
                return v
        for v in vals:
            if R.presence(v, my)[0]:
                return v
        if " " in kw:                    # the module's compose rules (members looked up as usual)
            v = MM["m"].compose(CUR["ch"], "", kw, pali, my)
            if v is not None and R.presence(v, my)[0]:
                return v
        v = R.pi_get(kw, my)[0] or stem_value(kw, my)
        if v is None:
            raise KeyError(kw)
        return v
    return f


TABLES = None


_POOL = {}


def _pool():
    """{low(kw): Counter(value)}: the pi-1 … pi-4 values, the ch1 table, the module tables and this group's tables (the
    values a keyword of the same stem has elsewhere)."""
    if not _POOL:
        import collections
        pool = collections.defaultdict(collections.Counter)
        for t in R.PRIOR_ORDER:
            for k, c in R.prior()[t].items():
                pool[k].update(c)
        tabs = [C1.T_CH1, R.FRAME, R.STOCK, T_GROUP] + [T[c] for c in CHAPTERS]
        for tab in tabs:
            for k, v in tab.items():
                for x in (v if isinstance(v, tuple) else (v,)):
                    if not x.startswith("@") and x != NONE:
                        pool[R.low(k)][x] += 50
        _POOL.update(pool)
        _POOL["__keys__"] = sorted(k for k in pool if " " not in k)
    return _POOL


def stem_value(kw, my):
    """NEW (group rule S1): a single keyword that neither the tables, the module nor pi-1 … pi-4 map takes the value of
    a keyword of the same stem (the longest common beginning, at least the keyword less four letters; pi-1 … pi-4, ch1,
    this group's tables) that this segment's Burmese has as a phrase; most frequent first."""
    import collections
    pool = _pool()
    k = R.low(kw)
    for n in range(len(k), max(4, len(k) - 4) - 1, -1):
        pre = k[:n]
        c = collections.Counter()
        for kk in pool["__keys__"]:
            if kk.startswith(pre) and abs(len(kk) - len(k)) <= 5:
                c.update(pool[kk])
        for v, _ in c.most_common():
            if R.presence(v, my)[0] and R.phrase_ok(v, my):
                return v
    return None


class _Mapper(R.Mapper):
    def map_chapter(self, ch):
        CUR["ch"] = ch
        return super().map_chapter(ch)

    def lookup(self, ch, sid, kw, pali, my):
        try:
            return super().lookup(ch, sid, kw, pali, my)
        except KeyError:
            if " " in kw:
                raise
            v = stem_value(kw, my)
            if v is None:
                raise
            self.SRC[(sid, kw)] = "stem"
            return v


def mapper():
    global TABLES
    TABLES = tables()
    MM["m"] = _Mapper(chapter_tables=tables(ch1=False), ctx=CTX, funcs=FUNCS2)
    return _Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS2)


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
    if report or total:
        print("problems", total)
        return
    for ch in (only or CHAPTERS):
        n, bad, fails, punct, ruled = R.verify_file(ch)
        print(ch, "lines", n, "bad", bad, "presence failures", len(fails), "punct", punct,
              "ending-rule chunks", len(ruled), "(no direct equivalent)", out[ch])


if __name__ == "__main__":
    main()
