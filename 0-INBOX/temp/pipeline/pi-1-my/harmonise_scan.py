"""pi-1 Burmese zero-shot (Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»), consistency pass: one form per item.

usage: python3 -I -X utf8 harmonise_scan.py [--table]
For every item: on the lines whose Pāli has the item, count the chosen Burmese form and every other form, in the
chapter files before the pass (harmonise-backup/chapters-before/) and now. One line per item; exit 1 when an other
form is still present now. Before counting an other form, the chosen forms of the other items that contain it are
removed from the line (e.g. saṃsayo's old «သံသယ» = kaṅkhā's chosen «သံသယ»), so such an old form is not counted.
--table writes harmonise-table.tsv (Pāli <TAB> chosen Burmese <TAB> other forms (before the pass, uses) <TAB>
chapters), then the items checked and kept (CHECKED). Also runs harmonise_lines.py (identical Pāli units of any
length, headings included: 0 differing) and harmonise_tables.py (same Pāli key in all generators' tables: 0 left,
the kept sense / grammar keys listed there).
"""
import collections, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-1_split_chapters"
NOW = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
BEFORE = HERE / "harmonise-backup/chapters-before"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
sys.path.insert(0, str(HERE))
import my_formulas as F  # noqa: E402

# (item, Pāli regex for the line, (chosen regex, chosen display), [(other regex, other display)])
ITEMS = [
    ("uddhacca (todo 1)", r"uddhacc", (F.UDDHACCA, F.UDDHACCA), [("စိတ် ပျံ့လွင့်မှု", "စိတ် ပျံ့လွင့်မှု")]),
    ("vicikicchā (todo 2)", r"vicikicch", (F.VICIKICCHA, F.VICIKICCHA), [("ယုံမှားသံသယ", "ယုံမှားသံသယ")]),
    ("kaṅkhā / kaṅkhāyanā / kaṅkhāyitattaṃ (todo 2)", r"kaṅkh", ("သံသယ", "သံသယ / သံသယ ဖြစ်ခြင်း / သံသယ ဖြစ်ထားသော အဖြစ်"),
     [("ယုံမှားခြင်း|ယုံမှားနေခြင်း|ယုံမှားထားသော အဖြစ်", "ယုံမှားခြင်း / ယုံမှားနေခြင်း / ယုံမှားထားသော အဖြစ်")]),
    ("abhiññā (todo 3)", r"bhiññ", ("ထူးကဲစွာ သိ", F.ABHINNA),
     [("အထူးသိမြင်မှု", "အထူးသိမြင်မှု"), ("ထူးသော ဉာဏ်ဖြင့် သိ", "ထူးသော ဉာဏ်ဖြင့် သိ၍ (sayaṃ abhiññā)")]),
    ("dandha- / khippābhiñña (todo 3)", r"(?:dandh|khipp)ābhiññ", ("နှေးကွေးသော|လျင်မြန်သော", "… နှေးကွေးသော / လျင်မြန်သော"),
     [("သိမြင်မှု နှေး|သိမြင်မှု လျင်မြန်(?!သော)", "အထူးသိမြင်မှု နှေး / လျင်မြန်")]),
    ("kiriyā / kiriya (todo 4)", r"[Kk]iriy(?!at)", ("ပြုရုံမျှသာ", F.KIRIYA),
     [("ပြုလုပ်ရုံမျှသာ", "ပြုလုပ်ရုံမျှသာ ဖြစ်သော"), ("ပြုမှုမျှသာ", "ပြုမှုမျှသာ ဖြစ်သော")]),
    ("kāmarāga (todo 5)", r"kāmarā ?g", (F.KAMARAGA, F.KAMARAGA),
     [("ကာမကို တပ်မက်မှုနှင့်", "ကာမကို တပ်မက်မှု (2-03 purpose; kāmataṇhā keeps «ကာမကို တပ်မက်မှု»)"),
      ("ကာမ ရာဂ", "ကာမ ရာဂ")]),
    ("bhavarāga (todo 5)", r"bhavarāg", (F.BHAVARAGA, F.BHAVARAGA), [("ဘဝ ရာဂ", "ဘဝ ရာဂ")]),
    ("rūparāga / arūparāga (todo 5: rāga = ရာဂ)", r"rūparāgaarūparāga", ("ဘုံ၌ ရာဂ", "… ရုပ်ဘုံ၌ ရာဂ၊ … ဘုံ၌ ရာဂ"),
     [("ဘုံကို တပ်မက်မှု", "… ရုပ်ဘုံကို တပ်မက်မှု")]),
    ("māna (purpose, fetter)", r"mānauddhacca|māno|mānasaṃyojan", (F.MANA + "(?!်)", F.MANA), [("မာန်", "မာန်")]),
    ("kāmarāga / byāpāda tanubhāvāya", r"tanubhāvāya", ("ပါးလျစေရန်", "ပါးလျစေရန်"), [("ပါးလျားစေရန်", "ပါးလျားစေရန်")]),
    ("anavasesappahānāya", r"anavasesappahānāya", ("မရှိအောင် ပယ်ရန်", "အကြွင်းအကျန် မရှိအောင် ပယ်ရန်"),
     [("မရှိ ပယ်ရန်", "အကြွင်းအကျန် မရှိ ပယ်ရန်")]),
    ("cluster members: kāmarāga-, paṭigha-, vicikicchā-, sīlabbataparāmāsa- … (todo 6)",
     r"saṃyojanaṃ|kāyagantho|nīvaraṇaṃ|upādānaṃ|parāmāso",
     ("နှောင်ကြိုး|ကိုယ် အထုံး|အတားအဆီး|စွဲလမ်းမှု|ယူဆမှု", "the Nikkhepa names (my_formulas.HMEMBERS)"),
     [("ကိုယ်ကို ချည်နှောင်သော အထုံး", "… ဟူသော ကိုယ်ကို ချည်နှောင်သော အထုံး"), ("ကာမဆန္ဒ", "ကာမဆန္ဒ အတားအဆီး"),
      ("(?:ကာမ|အယူ|အကျင့်ဝတ်တို့|ဝါဒ)ကို စွဲလမ်းမှု", "ကာမကို / အယူကို … စွဲလမ်းမှု"),
      ("သီလနှင့် အကျင့်ဝတ်တို့", "သီလနှင့် အကျင့်ဝတ်တို့၌ / ကို …"), ("အယူဖြင့် မှားယွင်းသော", "အယူဖြင့် မှားယွင်းသော ယူဆမှု"),
      ("နောင်တပူပန်မှု", "နောင်တပူပန်မှု"), ("ဤအယူသာ အမှန်ဖြစ်သည်ဟူ၍", "ဤအယူသာ အမှန်ဖြစ်သည်ဟူ၍ စွဲမြဲစွာ ယူခြင်း"),
      ("စိတ်ထိခိုက်ခြင်း", "စိတ်ထိခိုက်ခြင်း (paṭigha)")]),
    ("diṭṭhigata (todo 7)", r"diṭṭhigat", (F.DITTHIGATA, F.DITTHIGATA),
     [("မှားယွင်းသော အယူတို့ကို", "မှားယွင်းသော အယူ (purpose)"), ("အယူ၌ ကျရောက်ခြင်း", "အယူ၌ ကျရောက်ခြင်း (list)")]),
    ("paṭigha = aversion (todo 11)", r"paṭighaṃ|paṭighasaṃyojan|paṭighasampayutt", (F.PATIGHA_AV, F.PATIGHA_AV),
     [("စိတ်ထိခိုက်ခြင်း", "စိတ်ထိခိုက်ခြင်း")]),
    ("kāya- / vacīviññatti (todo 8)", r"(?:kāya|vacī)viññatti", (F.VINNATTI, F.KAYAVINNATTI + " / " + F.VACIVINNATTI),
     [("အရိပ်အမြွက် ပြခြင်း", "… အရိပ်အမြွက် ပြခြင်း"), ("ရည်ရွယ်ချက်ကို ပြခြင်း", "… ရည်ရွယ်ချက်ကို ပြခြင်း")]),
    ("ākāsadhātu (todo 8)", r"ākāsadhātu", (F.AKASADHATU, F.AKASADHATU), [("ကောင်းကင် ဓာတ်", "ကောင်းကင် ဓာတ်")]),
    ("āpodhātu (todo 8)", r"āpodhātu", (F.APODHATU, F.APODHATU), [("ရေ ဓာတ်", "ရေ ဓာတ်")]),
    ("kabaḷīkāro āhāro (todo 8)", r"kabaḷīkār", ("လုတ်ပြု၍ စားရသော", F.KABALIKARA), [("စားသောက်ရသော", "စားသောက်ရသော အာဟာရ")]),
    ("rūpassa santati", r"rūpassa santati", (F.RUPA_SANTATI, F.RUPA_SANTATI), [("ဆက်လက် ဖြစ်ပေါ်ခြင်း", "ရုပ်၏ ဆက်လက် ဖြစ်ပေါ်ခြင်း")]),
    ("cittaja / cittahetuka", r"cittajaṃ", (F.CITTAJA, f"{F.CITTAJA}၊ {F.CITTAHETUKA}"),
     [("စိတ်ကြောင့် ဖြစ်သော", "စိတ်ကြောင့် ဖြစ်သော"), ("စိတ်ကို အကြောင်းပြုသော", "စိတ်ကို အကြောင်းပြုသော")]),
    ("kāyena (third jhāna) (todo 10)", r"sukhañca kāyena", (F.KAYA + "ဖြင့်", F.KAYA + "ဖြင့် ခံစား၍"),
     [("ကိုယ်ဖြင့် ခံစား", "ကိုယ်ဖြင့် ခံစား၍")]),
    ("mahākusala (todo 12)", r"mahākusal", ("မဟာကုသိုလ်", "မဟာကုသိုလ်စိတ်"), [("ကြီးကျယ်သော ကုသိုလ်", "ကြီးကျယ်သော ကုသိုလ်စိတ်")]),
    ("dukkha- / sukhapaṭipadaṃ (todo 13)", r"(?:dukkha|sukha)paṭipad", ("ကျင့်စဉ် (?:ခက်ခဲ|လွယ်ကူ)သော", "ကျင့်စဉ် ခက်ခဲသော / လွယ်ကူသော"),
     [("ကျင့်စဉ် (?:ခက်ခဲ|လွယ်ကူ)(?!သော)", "ကျင့်စဉ် ခက်ခဲ၍ / လွယ်ကူ၍")]),
    ("-ādhipateyyaṃ (todo 13)", r"dhipateyy", ("အကြီးအမှူးပြုသော", "X-ကို အကြီးအမှူးပြုသော"), [("အကြီးအမှူးပြု(?!သော)", "X-ကို အကြီးအမှူးပြု၍")]),
    ("X-kasiṇaṃ (todo 13)", r"kasiṇaṃ", ("ကသိုဏ်းကို အာရုံပြုသော", "X ကသိုဏ်းကို အာရုံပြုသော"), [("ကသိုဏ်းကို အာရုံပြု(?!သော)", "… အာရုံပြု၍")]),
    ("suññataṃ / animittaṃ / appaṇihitaṃ (todo 13)", r"(?:suññata|animitta|appaṇihita)[ṃn]",
     ("ဆိတ်သုဉ်းသော|အမှတ်အသား မရှိသော|တောင့်တမှု မရှိသော", "ဆိတ်သုဉ်းသော / အမှတ်အသား မရှိသော / တောင့်တမှု မရှိသော"),
     [("ဆိတ်သုဉ်း၍|အမှတ်အသား မရှိ၍|တောင့်တမှု မရှိ၍", "ဆိတ်သုဉ်း၍ / … မရှိ၍")]),
    ("lokuttaraṃ X bhāveti niyyānikaṃ apacayagāmiṃ PURPOSE (todo 13)", r"apacayagāmiṃ \S+ \S+ \S+ bhūmiyā",
     ("ရောက်ရန်၊ လွတ်မြောက်ရာသို့", "PURPOSE၊ လွတ်မြောက်ရာသို့ … X-ကို ပွားများ၍၊ …"),
     [("ပွားများ၍ (?:အယူမှား|ကာမရာဂ|ကာမကို)", "… X-ကို ပွားများ၍ PURPOSE …")]),
    ("rūpūpapattiyā / arūpūpapattiyā maggaṃ (todo 13)", r"rūpūpapattiyā maggaṃ", ("ဖြစ်ပေါ်ရန် လမ်းကို", "… ဖြစ်ပေါ်ရန် လမ်းကို"),
     [("လမ်းစဉ်ကို", "… ဖြစ်ပေါ်ရန် လမ်းစဉ်ကို")]),
    ("sabbaso X samatikkamma (todo 13)", r"samatikkamma", ("ကျော်လွန်၍", "… ကို အလုံးစုံ ကျော်လွန်၍"), [("လွန်မြောက်၍", "… လွန်မြောက်၍")]),
    ("ākāsānañca- / viññāṇañcāyatana (todo 13)", r"ākāsānañcāyatana|viññāṇañcāyatana", ("အဆုံး မရှိသော", "အဆုံး မရှိသော …"),
     [("အဆုံးမရှိသော", "အဆုံးမရှိသော …"), ("အာကာသာနဉ္စာယတန", "အာကာသာနဉ္စာယတန ဘုံ (4-02 realm name)")]),
    ("X-āyatanasaññāsahagataṃ (todo 13)", r"āyatanasaññāsahagataṃ", ("နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော", "X-ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော"),
     [("နယ်ပယ်နှင့် ဆိုင်သော မှတ်သိမှုနှင့်အတူ", "X-နှင့် ဆိုင်သော မှတ်သိမှုနှင့်အတူ")]),
    ("nevasaññānāsaññāyatana (todo 13)", r"nevasaññānāsaññāyatan", ("မှတ်သိမှု ရှိသည်လည်း မဟုတ်", "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ … မရှိသည်လည်း မဟုတ်သော"),
     [("ရှိခြင်းလည်း မဟုတ်", "မှတ်သိမှု ရှိခြင်းလည်း မဟုတ်၊ မရှိခြင်းလည်း မဟုတ်သော")]),
    ("nevasaññānāsaññāyatana (realm name)", r"nevasaññānāsaññāyatanupage", ("မှတ်သိမှု ရှိသည်လည်း မဟုတ်", F.JH_ARUPA_BASE["nevasaññānāsaññāyatana"]),
     [("နေဝသညာနာသညာယတန", "နေဝသညာနာသညာယတန ဘုံ")]),
    ("diṭṭhadhammasukhavihāra", r"diṭṭhadhammasukhavihār", ("မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်", "မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်-"),
     [("ချမ်းသာစွာ နေထိုင်", "မျက်မှောက်ဘဝ၌ ချမ်းသာစွာ နေထိုင်-")]),
    ("sabbaso rūpasaññānaṃ samatikkamā … (todo 13)", r"rūpasaññānaṃ samatikkamā", ("ရုပ်ဟု မှတ်သိမှုတို့ကို", "ရုပ်ဟု မှတ်သိမှုတို့ကို …"),
     [("ရုပ်နှင့် ဆိုင်သော မှတ်သိမှု", "ရုပ်နှင့် ဆိုင်သော မှတ်သိမှုတို့ကို …")]),
    ("iddhipāda (todo 13)", r"iddhipād", ("ဣဒ္ဓိပါဒ်", "ဣဒ္ဓိပါဒ်"), [("အောင်မြင်မှု၏ အခြေခံ", "အောင်မြင်မှု၏ အခြေခံ")]),
    ("aññindriyaṃ", r"(?<![pP])aññindriy", ("အပြည့်အဝ သိမြင်ခြင်း၏", "အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည်"),
     [("အပြည့်အဝ သိခြင်း၏", "အပြည့်အဝ သိခြင်း၏ စွမ်းရည်")]),
    ("vīmaṃsā", r"vīmaṃs", (F.VIMAMSA, F.VIMAMSA), [("စူးစမ်းဆင်ခြင်မှု", "စူးစမ်းဆင်ခြင်မှု")]),
    ("dukkhanirodhagāminī paṭipadā", r"gāminiyā paṭipadāya", ("ရောက်စေသော ကျင့်စဉ်", "… ရောက်စေသော ကျင့်စဉ်"),
     [("ရောက်စေသော အကျင့်", "… ရောက်စေသော အကျင့်")]),
    ("sāmaññaphala", r"sāmaññaphal", (F.SAMANNAPHALA, F.SAMANNAPHALA), [("ရဟန်းအဖြစ်၏ အကျိုး", "ရဟန်းအဖြစ်၏ အကျိုး")]),
    ("Katame dhammā X-vippayuttā Y / na hetū Y (Mātikā pair)", r"Katame dhammā (?:\S+vippayuttā \S+|na hetū \S+)\?",
     ("သဘောတရားများအနက်", "X သဘောတရားများအနက် Y"), [("ကင်းကွာ၍|မဟုတ်ဘဲ အမြစ်", "X-၍ / X-ဘဲ Y")]),
    ("ime dhammā X (closer of a Mātikā term)", r"ime dhammā (?!kusalā|akusalā)",
     ("သဘောတရားများ ဖြစ်ကြသည်", "ဤသဘောတရားများသည် {X} သဘောတရားများ ဖြစ်ကြသည်"),
     [("(?:နိုင်|ပို့ဆောင်|ဦးတည်|ကျိန်းသေ|ယှဉ်တွဲ|ရောနှော|တည်ရှိ|လိုက်ပါ|ဖြစ်ပေါ်လာ|ညစ်နွမ်း|ရှိ)ကြသည်။", "ဤသဘောတရားများသည် X-ကြသည် (predicate)")]),
    ("Teva / Tāneva / Sveva X …", r"(?:Teyeva|Teva|Tāneva|Sveva) ", ("(?:များ|ယူဆမှု)သည်ပင်", "ထို Xများသည်ပင် … သဘောတရားများ ဖြစ်ကြသည်"),
     [("တို့သည်ပင်", "ထို Xတို့သည်ပင် … ကြသည်")]),
    ("Cittaṃ na vattabbaṃ – …ntipi", r"Cittaṃ na vattabbaṃ", ("ခေါ်ဆို၍ မရ", "စိတ်သည် – … ဟုလည်းကောင်း … ခေါ်ဆို၍ မရ"),
     [("မပြောဆိုထိုက်", "စိတ်ကို မပြောဆိုထိုက် – … ဟူ၍လည်း")]),
    ("ye ca dhammā kiriyā … / sabbañca rūpaṃ / asaṅkhatā ca dhātu", r"ye ca dhammā kiriyā",
     ("ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း", F.KIRIYA_ATTR + " သဘောတရားများလည်း"),
     [("မဟုတ်သော ပြုလုပ်ရုံမျှသာ|ပြုမှုမျှသာ ဖြစ်၍", "… ပြုလုပ်ရုံမျှသာ / ပြုမှုမျှသာ ဖြစ်၍ …"), ("ရုပ် အားလုံး၊", "ရုပ် အားလုံး (no လည်း)")]),
    ("yañca rūpaṃ …", r"yañca rūpaṃ (?:na )?kammassa katattā(?! uppajj)|anidassanaṃ appaṭighaṃ dhammāyatana",
     ("ရုပ် ရှိသမျှလည်း", "… ရုပ် ရှိသမျှလည်း"), [("(?:ဖြစ်သော|မဟုတ်သော|အကျုံးဝင်သော) ရုပ်လည်း", "… ရုပ်လည်း")]),
    ("anidassanaṃ appaṭighaṃ (yañca rūpaṃ …)", r"anidassanaṃ appaṭighaṃ dhammāyatana",
     (F.TERMS["anidassanaappaṭighā"], F.TERMS["anidassanaappaṭighā"]), [("မမြင်နိုင်သော၊ ထိခိုက်မှု မရှိသော", "မမြင်နိုင်သော၊ ထိခိုက်မှု မရှိသော")]),
    ("avasesa", r"[Aa]vases", ("ကြွင်းကျန်သော", "ကြွင်းကျန်သော"), [("ကြွင်းသော", "ကြွင်းသော")]),
    ("Sabbeva kāmāvacarā kusalākusalābyākatā dhammā", r"[Ss]abbeva kāmāvacarā kusalākusalābyākatā",
     ("အားလုံးပင်", "ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်၊ အကုသိုလ်၊ … သဘောတရားများ အားလုံးပင်"), [("သဘောတရား အားလုံး", "… သဘောတရား အားလုံး")]),
    ("Suddhika- (headings) (todo 14)", r"Suddhika", ("သက်သက်", "X သက်သက်"), [("သီးသန့်", "သီးသန့် X")]),
    ("Vīsati mahānayā (todo 14)", r"Vīsati mahānayā", ("နည်းကြီး နှစ်ဆယ်", "နည်းကြီး နှစ်ဆယ်"), [("ကြီးကျယ်သော နည်း", "ကြီးကျယ်သော နည်း နှစ်ဆယ်")]),
    ("X-kaṇḍe Y-bhāṇavāro (todo 14)", r"kaṇḍe \S*bhāṇavāro", ("အခန်း၌", "X အခန်း၌ Y ရွတ်ဖတ်ရန် အပိုင်း"), [("အခန်း၏", "X အခန်း၏ …")]),
    ("Tattha katam- (todo 14)", r"Tattha katam", ("ထိုတို့အနက်", "ထိုတို့အနက်"), [("ထိုတွင်", "ထိုတွင်")]),
    ("idaṃ / ayaṃ vuccati X", r"vuccati", ("ဟု ခေါ်သည်", "ဤသည်ကို Xဟု ခေါ်သည်"), [(r"(?<=[^\s]) ဟု ခေါ်သည်", "ဤသည်ကို X ဟု ခေါ်သည်")]),
    ("dhammavicayasambojjhaṅgo", r"dhammavicayasambojjhaṅg", ("စိစစ်ခြင်း ဗောဇ္ဈင်", "သဘောတရားများကို စိစစ်ခြင်း ဗောဇ္ဈင်"),
     [("သိမြင်ခြင်း၏ အင်္ဂါ", "… ဟူသော သိမြင်ခြင်း၏ အင်္ဂါ")]),
    ("maggapariyāpannaṃ", r"maggapariyāpann", ("အကျုံးဝင်သောအရာ", "မဂ်၌ အကျုံးဝင်သောအရာ"), [("အကျုံးဝင်သော အရာ", "မဂ်၌ အကျုံးဝင်သော အရာ")]),
]

# the shared synonym table of the akusala factors (my_formulas.HSYN): (Pāli key, chosen, the 2-04 / 2-05 form before)
SYN_ITEMS = [
    ("abhiniveso", "သက်ဝင်ယုံကြည်ခြင်း", "စွဲမြဲခြင်း"),
    ("anabhisamayo", "ထင်ထင်ရှားရှား မသိမြင်ခြင်း", "ပိုင်ပိုင် နားမလည်ခြင်း"),
    ("ananubodho", "လိုက်၍ မနားလည်ခြင်း", "သဘော မပေါက်ခြင်း"),
    ("apaccakkhakammaṃ", "ကိုယ်တိုင် ထင်ထင်ရှားရှား မပြုခြင်း", "မျက်မှောက် မပြုခြင်း"),
    ("apariyogāhanā", "နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း", "နက်နက်နဲနဲ မသက်ဝင်ခြင်း"),
    ("appaṭivedho", "ထိုးဖောက်၍ မသိခြင်း", "ထိုးထွင်း၍ မသိခြင်း"),
    ("asamapekkhanā", "ညီညီညွတ်ညွတ် မရှုမြင်ခြင်း", "မျှမျှတတ မရှုခြင်း"),
    ("asambodho", "ကောင်းစွာ မနားလည်ခြင်း", "ကောင်းစွာ မသိမြင်ခြင်း"),
    ("asaṃgāhanā", "စုစည်း၍ မယူနိုင်ခြင်း", "စုစည်း၍ မယူခြင်း"),
    ("asuropo", "စကား ကြမ်းခြင်း", "ရိုင်းစိုင်းခြင်း"),
    ("avijjālaṅgī", "အမှန်ကို မသိမှု တံခါးကန့်လန့်", "အမှန်ကို မသိမှု၏ တံခါးကန့်လန့်"),
    ("avijjānusayo", "အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း", "အမှန်ကို မသိမှု၏ ကိန်းဝပ်ခြင်း"),
    ("avijjāpariyuṭṭhānaṃ", "အမှန်ကို မသိမှု ထကြွခြင်း", "အမှန်ကို မသိမှု၏ ဖုံးလွှမ်းခြင်း"),
    ("avūpasamo", "မငြိမ်ဝပ်ခြင်း", "မငြိမ်းခြင်း"),
    ("byāpatti", "ဖောက်ပြန်ခြင်း", "ပျက်စီးစေလိုခြင်း"),
    ("diṭṭhigahanaṃ", "အယူ တောအုပ်", "အယူ ချုံထူ"),
    ("diṭṭhivipphanditaṃ", "အယူ၏ တုန်လှုပ်မှု", "အယူ တုန်လှုပ်မှု"),
    ("diṭṭhivisūkāyikaṃ", "အယူ၏ ကောက်ကွေးမှု", "အယူ ကွေ့ကောက်မှု"),
    ("dummejjhaṃ", "ဉာဏ်နုံခြင်း", "ဉာဏ်ထိုင်းခြင်း"),
    ("dussitattaṃ", "စိတ်ဆိုးထားသော အဖြစ်", "စိတ်ဆိုးသော အဖြစ်"),
    ("dvedhāpatho", "လမ်း နှစ်ခွ", "လမ်းနှစ်ခွ"),
    ("dveḷhakaṃ", "စိတ် နှစ်ခွ ဖြစ်ခြင်း", "စိတ်နှစ်ခွ ဖြစ်ခြင်း"),
    ("kaṅkhāyanā", "သံသယ ဖြစ်ခြင်း", "ယုံမှားနေခြင်း"),
    ("kaṅkhāyitattaṃ", "သံသယ ဖြစ်ထားသော အဖြစ်", "ယုံမှားထားသော အဖြစ်"),
    ("kummaggo", "လမ်းမှား", "လမ်းဆိုး"),
    ("manovilekho", "မနောကို ခြစ်ကုတ်ခြင်း", "စိတ်ကို ခြစ်ကုတ်ခြင်း"),
    ("pamoho", "အလွန် တွေဝေခြင်း", "အလွန် ဝေဝါးခြင်း"),
    ("parisappanā", "ပတ်ချာလည် ယိမ်းယိုင်ခြင်း", "ချီတုံချတုံ ဖြစ်ခြင်း"),
    ("sammoho", "လုံးဝ တွေဝေခြင်း", "လုံးဝ ဝေဝါးခြင်း"),
    ("saṃsayo", "ဒွိဟ ဖြစ်ခြင်း", "သံသယ"),
    ("titthāyatanaṃ", "အယူဝါဒတို့၏ တည်ရာ", "အယူဝါဒ ဂိုဏ်းတို့၏ တည်ရာ"),
    ("vimati", "စိတ်ရှုပ်ထွေးခြင်း", "တွေဝေခြင်း"),
    ("āsappanā", "ယိမ်းယိုင်ခြင်း", "တွန့်ဆုတ်ခြင်း"),
    ("bhantattaṃ cittassa", "စိတ်၏ ယိမ်းထိုးနေသော အဖြစ်", "စိတ် ယိမ်းယိုင်နေသော အဖြစ်"),
    ("cetaso vikkhepo", "စိတ်၏ ပျံ့လွင့်ခြင်း", "စိတ် ပျံ့လွင့်ခြင်း"),
    ("kaṅkhā", "သံသယ", "ယုံမှားခြင်း"),
]
_WB = "(?<![A-Za-zāīūṃṅñṭḍṇḷ])"
for _k, _c, _o in SYN_ITEMS:
    ITEMS.append((f"{_k} (synonym table, todo 7)", _WB + re.escape(_k) + "(?![A-Za-zāīūṃṅñṭḍṇḷ])",
                  (re.escape(_c), _c), [(re.escape(_o), _o)]))

# items checked and kept as they are (sense differences, already one form, source slips): Pāli, form, note, chapters
CHECKED = [
    ("bahiddhā (todo 9)", "သူတစ်ပါး၌ (Mātikā, 3-03, 4-0x, 5) / ပြင်ပ၌ (2-02 abhibhāyatana)",
     "kept: genuine sense difference; «ajjhattaṃ arūpasaññī bahiddhā rūpāni passati» = forms seen outside oneself "
     "(the kasiṇa objects of the bases of mastery), not «in other beings» (the Mātikā ajjhatta / bahiddhā pair)", "2-02"),
    ("paṭigha (todo 11)", f"{F.PATIGHA_AV} (aversion) / {F.IMPACT} (impact: sappaṭigha, paṭighasaññā)",
     "kept: genuine sense difference, both forms book-wide by sense", "1, 2-02, 2-04, 3, 4, 5"),
    ("upasampajja viharati (todo 13)", F.JH_UPAS, "already one form in 2-02 … 2-05 (now from my_formulas.JH_UPAS)", "2-02 … 2-05"),
    ("«…nti kusalaṃ / …nti vipāko» (todo 13)", "Q…သော ကုသိုလ် / Q…သော ကံ၏ အကျိုး",
     "only in 2-05; apposition after the shared qualifier chain (Q now the shared attributives)", "2-05"),
    ("saṃsayo (todo 2)", "ဒွိဟ ဖြစ်ခြင်း", "the shared table (4-0x); the old 2-04 «သံသယ» is now kaṅkhā's form, so it is "
     "not counted by the scan: list distinctness is enforced by my_formulas.list_items", "2-04"),
    ("mahāvipāka (Aṭṭhamahāvipākā)", "ကြီးကျယ်သော ကံ၏ အကျိုး ရှစ်ပါး", "kept: vipāka has no loan in this track (ကံ၏ အကျိုး), "
     "so «မဟာ» + it would not read; mahākusala = မဟာကုသိုလ် (todo 12)", "2-04"),
    ("micchādiṭṭhi / diṭṭhigataṃ in one list", "မှားယွင်းသော အယူ / အယူမှား",
     "distinct strings; both carry «wrong» (diṭṭhigata = wrong view book-wide): for the user's review", "2-04, 4-0x"),
    ("sineho", "စေးကပ်မှု (āpodhātu) / ချစ်ခင်ခြင်း (greed list)", "kept: sense differs (cohesion / affection)", "3-03, 4-0x"),
    ("niyatā", "ကျိန်းသေသော (Mātikā) / သီးသန့် ဖြစ်သော (ajjhatta list)", "kept: sense differs", "4-0x"),
    ("nāmaṃ", "စိတ်ပိုင်း (nāma dyad) / အမည် (adhivacana list)", "kept: sense differs", "4-0x"),
    ("headings and colophons (todo 14)", "-", "harmonise_lines.py: 0 identical Pāli units with differing Burmese "
     "(headings included); kaṇḍe-bhāṇavāra, Tattha, vuccati, suddhika and mahānaya aligned (items above)", "all"),
    ("source slips (todo 15)", "-", "^1-850 dhoso = ghoso (3-03: same Burmese); patiṭṭhāho = paṭiggāho (2-04, 4-0x: "
     "«ခိုင်မြဲစွာ စွဲကိုင်ခြင်း»); Devanāgarī «ः» = «၊» (4-0x); ^1-553 «kāmarā gabyāpādānaṃ» = kāmarāga…; missing commas "
     "stay missing (2-02 ^1-165 / 189 / 204, 2-04 ^1-574 / 579, 4-0x ^1-1059 / 1101) except the 4-0x noun series that "
     "already took «၊» consistently", "2-02, 2-04, 2-05, 3-03, 4-0x"),
]


def lines_of(md_dir):
    out = []
    for p in sorted(PD.glob("*.md")):
        a = [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [ID.sub("", l) for l in (md_dir / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        out += [(p.name[:4].rstrip("-"), x, y) for x, y in zip(a, b)]
    return out


CHOSEN_LIT = sorted({*F.HSYN.values()} | {c for _, _, (_, c), _ in ITEMS if "|" not in c and "…" not in c}, key=len,
                    reverse=True)


def count(md_dir):
    lines = lines_of(md_dir)
    res = {}
    for name, pr, (cr, cd), others in ITEMS:
        c = 0
        oth = collections.defaultdict(collections.Counter)
        for ch, x, y in lines:
            if not re.search(pr, x):
                continue
            c += len(re.findall(cr, y))
            for orx, od in others:
                yy = y
                for s in CHOSEN_LIT:          # chosen forms of other items that contain this old form
                    if s != cd and re.search(orx, s):
                        yy = yy.replace(s, "")
                k = len(re.findall(orx, yy))
                if k:
                    oth[od][ch] += k
        res[name] = (c, oth)
    return res


def main():
    before, now = count(BEFORE), count(NOW)
    bad, rows = 0, []
    for name, _, (_, chosen), others in ITEMS:
        b_ch, b_oth = before[name]
        n_ch, n_oth = now[name]
        left = sum(sum(v.values()) for v in n_oth.values())
        was = sum(sum(v.values()) for v in b_oth.values())
        bad += left
        print(f"{'OK ' if not left else 'LEFT'} {name}: chosen {b_ch} -> {n_ch}; other forms {was} -> {left}")
        for od, chs in n_oth.items():
            print(f"      still: {od} {dict(chs)}")
        other_txt = "; ".join(f"{od} ({sum(chs.values())})" for od, chs in b_oth.items()) or "- (0 uses before)"
        chs = sorted({c for v in b_oth.values() for c in v})
        rows.append((name, chosen, other_txt, ", ".join(chs) if chs else "-"))
    py = [sys.executable, "-I", "-X", "utf8"]
    for script, ok in (("harmonise_lines.py", "with differing Burmese: 0 (headings 0)"),
                       ("harmonise_tables.py", "with more than one Burmese: 0")):
        out = subprocess.run(py + [str(HERE / script)], capture_output=True, text=True).stdout
        first = out.splitlines()[0] if out else "(no output)"
        print(f"     {script}: {first}")
        if ok not in first:
            bad += 1
    if "--table" in sys.argv:
        with open(HERE / "harmonise-table.tsv", "w", encoding="utf-8") as f:
            f.write("Pāli\tchosen Burmese\tother forms found (before the pass, uses)\tchapters\n")
            for r in rows:
                f.write("\t".join(r) + "\n")
            for p, form, note, chs in CHECKED:
                f.write(f"{p}\t{form}\tCHECKED: {note}\t{chs}\n")
        print("harmonise-table.tsv written:", len(rows), "items +", len(CHECKED), "checked items")
    print("items with other forms left:", bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
