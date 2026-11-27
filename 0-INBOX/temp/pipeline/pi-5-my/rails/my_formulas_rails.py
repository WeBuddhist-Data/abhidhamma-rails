"""pi-5 Burmese RAILS layer: the systematic termbase differences of the harmonised zero-shot, as in-memory source
patches of my5_formulas.py and of the zero-shot generators (none of them is edited on disk). Model: the approved
pi-4 rails layer (pi-4-my/rails/my_formulas_rails.py, read only).

Each patch is (old, new, count, reason): build_rails.py applies it to the source text before running it and fails
unless «old» occurs exactly «count» times. Patching the source (not the finished text) keeps every derived string
(tables, frames, the sample tables reused by the later generators) consistent: identical Pāli = identical Burmese.
A patch of my5_formulas / make_sample / make_ch6-10 / make_ch11-12 applies wherever that file runs or is imported.
Reasons start with the family id (Lnn), then the termbase headword(s) = term and the decision
(AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md, locked, sha256 6f2558f8…; termbase/decisions-A.tsv), or
the logged text inconsistency «§A n» (mapper-my/map-harmonise-notes.md §A, item n). Where a witnessed pi-1 … pi-4
value (my5_formulas.witness / W) holds the old word, the witness is kept (it still checks the earlier text) and the
pi-5 value is derived from it with one explicit replacement.
"""

PATCHES = {}


def p(f, old, new, count, reason):
    PATCHES.setdefault(f, []).append((old, new, count, reason))


# ------------------------------------------------------------------------------------------------------ L01 attahitāya
p("my5_formulas", 'ATTAHITA_PUG = "မိမိ၏ အကျိုးအတွက် ကျင့်ကြံသော ပုဂ္ဂိုလ်"',
  'ATTAHITA_PUG = "မိမိ၏ အကျိုးစီးပွားအတွက် ကျင့်ကြံသော ပုဂ္ဂိုလ်"', 1,
  "L01 hitāya = အကျိုးစီးပွား (decision hitāya|0, §A4: attahitāya reads «မိမိ၏ အကျိုးစီးပွား»; the pi-4 ^4-M-10 witness "
  "ATTAHITA is kept): the sutta quotation «atthi puggalo attahitāya paṭipanno» ch1")

# ------------------------------------------------------------------------------------------------------ L02 upacchedo
p("make_sample", 'V("သံသရာ စက်ဝန်း ပြတ်ခြင်း", "ရှိ", neg=True)', 'V("သံသရာ စက်ဝန်း ပြတ်စဲခြင်း", "ရှိ", neg=True)', 1,
  "L02 upacchedo = ပြတ်စဲခြင်း (decision upacchedo|0, pi-2 locked, stem uccheda «ပြတ်စဲ»): natthi vaṭṭupacchedo ch1, "
  "reused ch19")
p("make_ch13-16", "ဝဋ်ကို ဖြတ်တောက်ခြင်း {NEXIST}", "သံသရာ စက်ဝန်း ပြတ်စဲခြင်း {NEXIST}", 1,
  "L02 upacchedo = ပြတ်စဲခြင်း, vaṭṭa = သံသရာ စက်ဝန်း (decisions upacchedo|0, vaṭṭa|0): ^5-501 «natthi vaṭṭupacchedo» "
  "= ch1's wording (identical Pāli = identical Burmese)")

# ------------------------------------------------------------------------------------------------------ L03 upasampajja
p("make_ch2-5", "{SACCHIKAROTI}ပြီး၍ ပြည့်စုံစွာ ဝင်ရောက်၍", "{SACCHIKAROTI}ပြီး၍ ဝင်စား၍", 1,
  "L03 upasampajja (viharati) = ဝင်စား၍ (နေသည်) (decisions upasampajja|0, upasampajja viharati|0, pi-1 … pi-4 locked; "
  "the stream-entry passage follows): ^5-274 … ^5-277")
p("make_ch6-10", "မျက်မှောက်ပြုပြီး၍ ပြည့်စုံစွာ ဝင်ရောက်၍ နေသည်၊ ", "မျက်မှောက်ပြုပြီး၍ ဝင်စား၍ နေသည်၊ ", 1,
  "L03 upasampajja viharati = ဝင်စား၍ နေသည် (decision upasampajja viharati|0): ^5-340 … ^5-343, ^5-366, ^5-368")
p("make_ch13-16", '_APP = "အတိုင်းအဆ မရှိသော စိတ်၏ တည်ကြည်ခြင်းကို ပြည့်စုံစေလျက် နေ၏"',
  '_APP = "အတိုင်းအဆ မရှိသော စိတ်၏ သမာဓိကို ဝင်စား၍ နေ၏"', 1,
  "L03 upasampajja viharati = ဝင်စား၍ နေသည်, samādhiṃ = သမာဓိ (decisions upasampajja|0, samādhiṃ|0, pi-4 / pi-2 locked): "
  "^5-486 appamāṇaṃ cetosamādhiṃ upasampajja viharati")
p("make_ch13-16", "ပြည့်စုံစေလျက် နေ", "ဝင်စား၍ နေ", 3,
  "L03 upasampajja viharati = ဝင်စား၍ နေသည် (decision upasampajja viharati|0): «diṭṭhaṃ viditaṃ sacchikataṃ upasampajja "
  "viharati» ^5-421 / ^5-422")
p("make_ch13-16", "ပြည့်စုံစေလျက် မနေ", "ဝင်စား၍ မနေ", 2,
  "L03 na upasampajja viharati = the negative «ဝင်စား၍ မနေ» (decision upasampajja viharati|0): ^5-421 / ^5-422")

# ------------------------------------------------------------------------------------------------------ L04 issariya
p("make_ch26-31", "မိမိ၏ အစွမ်းဖြင့် အလိုရှိတိုင်း", "အစိုးရခြင်းဖြင့် အလိုရှိတိုင်း", 3,
  "L04 issariya = အစိုးရခြင်း (decision issariya|0: «မိမိ၏ အစွမ်း» adds «မိမိ၏», absent from the Pāli): "
  "issariyakāmakārikā ch31, heading ^5-31-3-1-0 and ^5-910 … ^5-914, ^5-918")

# ------------------------------------------------------------------------------------------------------ L05 the participle lists
p("make_ch2-5", 'CEASE = [("niruddhaṃ", "ချုပ်ငြိမ်း"), ("vigataṃ", "ကင်းကွာ"), ("vipariṇataṃ", "ဖောက်ပြန်ပြောင်းလဲ"),\n'
  '         ("atthaṅgataṃ", "ကွယ်"), ("abbhatthaṅgataṃ", "လုံးဝ ကွယ်")]',
  'CEASE = [("niruddhaṃ", "ချုပ်ငြိမ်း"), ("vigataṃ", "ကင်းပျောက်"), ("vipariṇataṃ", "ဖောက်ပြန်ပြောင်းလဲ"),\n'
  '         ("atthaṅgataṃ", "ကွယ်ပျောက်"), ("abbhatthaṅgataṃ", "လုံးဝ ကွယ်ပျောက်")]', 1,
  "L05 §A14 vigataṃ = ကင်းပျောက်ပြီးသော, atthaṅgataṃ = ကွယ်ပျောက်ပြီးသော, abbhatthaṅgataṃ = လုံးဝ ကွယ်ပျောက်ပြီးသော "
  "(decisions vigataṃ|0, atthaṅgataṃ|0, abbhatthaṅgataṃ|0, pi-2 locked): the ch5 lists = ch7 / pi-1 ^1-1044")
p("make_ch2-5", 'BORN = [("jātaṃ", "ဖြစ်"), ("bhūtaṃ", "ဖြစ်တည်"), ("sañjātaṃ", "ဖြစ်ပေါ်"), ("nibbattaṃ", "ဖြစ်မြောက်"),\n'
  '        ("abhinibbattaṃ", "ထင်ရှားစွာ ဖြစ်မြောက်"), ("pātubhūtaṃ", "ထင်ရှား ပေါ်ပေါက်")]',
  'BORN = [("jātaṃ", "မွေးဖွား"), ("bhūtaṃ", "ဖြစ်"), ("sañjātaṃ", "ကောင်းစွာ မွေးဖွား"), ("nibbattaṃ", "ပေါ်ထွက်"),\n'
  '        ("abhinibbattaṃ", "ထင်ရှားစွာ ပေါ်ထွက်"), ("pātubhūtaṃ", "ထင်ရှားလာ")]', 1,
  "L05 §A14 jātaṃ = မွေးဖွားပြီးသော, sañjātaṃ = ကောင်းစွာ မွေးဖွားပြီးသော, nibbattaṃ = ပေါ်ထွက်ပြီးသော, abhinibbattaṃ = "
  "ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော, pātubhūtaṃ = ထင်ရှားလာပြီးသော, ajātaṃ = မမွေးဖွားသေးသော (decisions, pi-2 locked); "
  "bhūtaṃ «ဖြစ်» = the pi-1 ^1-1045 / ^1-1046 list (bhūtā «ဖြစ်ပြီးသော», abhūtā «မဖြစ်သေးသော») = ch7")
p("make_ch2-5", '_PX = "|".join(re.escape(k) for k in sorted(PART, key=len, reverse=True))',
  'PART["apātubhūtaṃ"] = ("ထင်ရှား မလာသေး", len(BORN))   # rails L05\n'
  '_PX = "|".join(re.escape(k) for k in sorted(PART, key=len, reverse=True))', 1,
  "L05 §A14 apātubhūtaṃ = «ထင်ရှား မလာသေး» (pi-1 ^1-1045 apātubhūtā «ထင်ရှား မလာသေးသော», = ch7 DONE7)")
p("make_ch17-20", '_CEASED = "ချုပ်ငြိမ်းပြီး၊ ကင်းကွာပြီး၊ ဖောက်ပြန်ပြောင်းလဲပြီး၊ ကွယ်ပြီး၊ လုံးဝ ကွယ်ပြီးသော အရာ"',
  '_CEASED = "ချုပ်ငြိမ်းပြီး၊ ကင်းပျောက်ပြီး၊ ဖောက်ပြန်ပြောင်းလဲပြီး၊ ကွယ်ပျောက်ပြီး၊ လုံးဝ ကွယ်ပျောက်ပြီးသော အရာ"', 1,
  "L05 §A14: the ch17 copy of the ch5 list (^5-566 …) follows")
p("make_ch17-20", '_UNBORN = ("မဖြစ်သေး၊ မဖြစ်တည်သေး၊ မဖြစ်ပေါ်သေး၊ မဖြစ်မြောက်သေး၊ ထင်ရှားစွာ မဖြစ်မြောက်သေး၊ ထင်ရှား "\n'
  '           "မပေါ်ပေါက်သေးသော အရာ")',
  '_UNBORN = ("မမွေးဖွားသေး၊ မဖြစ်သေး၊ ကောင်းစွာ မမွေးဖွားသေး၊ မပေါ်ထွက်သေး၊ ထင်ရှားစွာ မပေါ်ထွက်သေး၊ ထင်ရှား "\n'
  '           "မလာသေးသော အရာ")', 1,
  "L05 §A14: the ch17 copy of the ch5 list follows")

# ------------------------------------------------------------------------------------------------------ L06 samāpatti
p("make_ch21-25", 'SVN = W("2", "^2-808", "saññāvedayitanirodhasamāpattiyā", "မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်")',
  'SVN = W("2", "^2-808", "saññāvedayitanirodhasamāpattiyā", "မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်").replace(\n'
  '    "ချုပ်ငြိမ်းရာ ဈာန်", "ချုပ်ငြိမ်းခြင်း သမာပတ်")   # rails L06', 1,
  "L06 samāpatti = သမာပတ်, cessation «ချုပ်ငြိမ်းခြင်း သမာပတ်» (decision samāpatti|0: departs from pi-2 / pi-1 «ဈာန် "
  "ဝင်စားရာ»; the pi-2 ^2-808 witness is kept, the pi-5 value derived): ch24 saññāvedayitanirodhasamāpatti")
p("make_ch21-25", 'SVS = new("saññāvedayitanirodhasamāpatti", f"{SVN} ဝင်စားခြင်း")',
  'SVS = new("saññāvedayitanirodhasamāpatti", f"{SVN}")', 1,
  "L06 samāpatti = သမာပတ် (the noun itself; «… ဝင်စားခြင်း» was the old «ဈာန် ဝင်စားခြင်း»): ^5-728 … ^5-742")
p("make_ch21-25", 'V("ချုပ်ငြိမ်းရာ ဈာန်ကို ဝင်စားနေသူ", neg=True)', 'V("ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ", neg=True)', 1,
  "L06 nirodhaṃ samāpanno = ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသော (decision nirodhaṃ samāpanno|0)")
p("make_ch26-31", 'W("2", "^2-808", "saññāvedayitanirodhasamāpattiyā", SVN)',
  'W("2", "^2-808", "saññāvedayitanirodhasamāpattiyā", SVN)\n'
  'SVN = SVN.replace("ချုပ်ငြိမ်းရာ ဈာန်", "ချုပ်ငြိမ်းခြင်း သမာပတ်")   # rails L06', 1,
  "L06 samāpatti = သမာပတ် (decision samāpatti|0; the pi-2 ^2-808 witness is kept): ch28 nirodhasamāpatti")
p("make_ch6-10", 'ATT["saññāvedayitanirodhaṃ"] = "မှတ်သိမှုနှင့် ခံစားမှု ချုပ်ငြိမ်းခြင်း သမာပတ်"',
  'ATT["saññāvedayitanirodhaṃ"] = "မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းခြင်း သမာပတ်"', 1,
  "L06 vedayita = ခံစားရခြင်း (decisions vedayita|0, saññāvedayita|0, pi-2 locked; vedanā «ခံစားမှု» kept apart): ^5-333")
p("make_ch17-20", '"navasu anupubbavihārasamāpattīsu", f"အစဉ်အတိုင်း နေထိုင်ရာ ဈာန် ဝင်စားရာ {F.NUM_MY[9]}{F.CL}")',
  '"navasu anupubbavihārasamāpattīsu", f"အစဉ်အတိုင်း နေထိုင်ရာ ဈာန် ဝင်စားရာ {F.NUM_MY[9]}{F.CL}").replace(\n'
  '    "ဈာန် ဝင်စားရာ", "သမာပတ်")   # rails L06', 1,
  "L06 samāpattīnaṃ = သမာပတ် (decision samāpattīnaṃ|0; the pi-2 ^2-808 witness is kept): ^5-570 navannaṃ "
  "anupubbavihārasamāpattīnaṃ")
p("make_ch11-12", '"ဈာန်၊ လွတ်မြောက်ခြင်း၊ သမာဓိ၊ ဈာန် ဝင်စားရာတို့၏ ညစ်နွမ်းခြင်း၊ စင်ကြယ်ခြင်း၊ ထမြောက်ခြင်း") + "ကို",',
  '"ဈာန်၊ လွတ်မြောက်ခြင်း၊ သမာဓိ၊ ဈာန် ဝင်စားရာတို့၏ ညစ်နွမ်းခြင်း၊ စင်ကြယ်ခြင်း၊ ထမြောက်ခြင်း").replace(\n'
  '        "ဈာန် ဝင်စားရာ", "သမာပတ်") + "ကို",   # rails L06', 1,
  "L06 samāpattīnaṃ = သမာပတ် (decision samāpattīnaṃ|0; the pi-2 ^2-760 witness is kept): ^5-355 "
  "jhānavimokkhasamādhisamāpattīnaṃ")
p("make_ch17-20", '_AVJH = (f"{_VM}ဖြင့် ဈာန်ဝင်သူ၊ ', '_AVJH = (f"{_VM}ဖြင့် ဈာန် ဝင်စားသူ၊ ', 1,
  "L06 jhāyī = ဈာန် ဝင်စားသော (termbase jhāyī): ^5-570 aṭṭhavimokkhajhāyī (the zero-shot passed only through the "
  "old «ဈာန် ဝင်စားရာ» of the same line)")

# ------------------------------------------------------------------------------------------------------ L07 mānusaka
p("make_sample", '"mānusakaṃ sukhaṃ": ("လူတို့၏ ချမ်းသာ", "mānusakassa sukhassa"),',
  '"mānusakaṃ sukhaṃ": ("လူ့ချမ်းသာ", "mānusakassa sukhassa"),', 1,
  "L07 Mānusakaṃ = လူ့ (decision Mānusakaṃ|0, pi-4 locked): mānusakaṃ sukhaṃ ch1 ^5-150 … ^5-156 (and ^5-338)")

# ------------------------------------------------------------------------------------------------------ L08 kata
p("my5_formulas", '("katakaraṇīyo", "ပြုဖွယ် ကိစ္စကို ပြုပြီးသူ")', '("katakaraṇīyo", "ပြုဖွယ်ကို ပြုခဲ့သူ")', 1,
  "L08 kata = ပြုခဲ့သော (decision kata|0, pi-2 locked: «the arahant epithet katakaraṇīyo reads «ပြုဖွယ်ကို ပြုခဲ့သော»»)")
p("make_ch2-5", "{VITA3}၊ ပြုဖွယ် ကိစ္စကို ပြုပြီးသူ၊ ", "{VITA3}၊ ပြုဖွယ်ကို ပြုခဲ့သူ၊ ", 1,
  "L08 kata = ပြုခဲ့သော: the arahant epithet list ^5-261 … (= my5_formulas)")
p("make_ch2-5", 'CAYA = new("katassa paticayo", "ပြုပြီးသော အရာ၌ ထပ်မံ စုဆောင်းခြင်း")',
  'CAYA = new("katassa paticayo", "ပြုခဲ့သော အရာ၌ ထပ်မံ စုဆောင်းခြင်း")', 1,
  "L08 katassa = ပြုခဲ့သော အရာ (decision katassa|0, family kata): ^5-266")
p("make_ch2-5", 'KATA = new("katakaraṇīyo bhāvitabhāvano", "ပြုဖွယ် ကိစ္စကို ပြုပြီး၊ ပွားများဖွယ်ကို ပွားများပြီး")',
  'KATA = new("katakaraṇīyo bhāvitabhāvano", "ပြုဖွယ်ကို ပြုခဲ့၊ ပွားများဖွယ်ကို ပွားများပြီး")', 1,
  "L08 kata = ပြုခဲ့သော (katakaraṇīyo «ပြုဖွယ်ကို ပြုခဲ့»): ^5-273 anāgāmī … katakaraṇīyo bhāvitabhāvano")

# ------------------------------------------------------------------------------------------------------ L09 hīna
p("make_ch6-10", "တို့၏ မြင့်ခြင်း နိမ့်ခြင်း၊ ယုတ်ခြင်း မြတ်ခြင်း၊ ", "တို့၏ မြင့်ခြင်း နိမ့်ခြင်း၊ ယုတ်ညံ့ခြင်း မြတ်ခြင်း၊ ", 1,
  "L09 hīna = ယုတ်ညံ့သော (decision hīna|0, pi-4 locked; paṇītatā keeps its own term «မြတ်ခြင်း»): "
  "hīnapaṇītatā ^5-353, ^5-445, ^5-448, ^5-452")
p("make_ch26-31", "ဘုရားတို့ထက် ယုတ်ခြင်း ထူးခြင်း", "ဘုရားတို့ထက် ယုတ်ညံ့ခြင်း ထူးခြင်း", 2,
  "L09 hīna = ယုတ်ညံ့သော: hīnātirekatā ^5-885, uddāna ^5-891")
p("make_ch11-12", '+ "၍ ဝီရိယ ယုတ်လျော့သူ"', '+ "၍ ဝီရိယ ယုတ်ညံ့သူ"', 1,
  "L09 hīna = ယုတ်ညံ့သော: kusīto hīnavīriyo ^5-371 (the pi-2 ^2-851 witness «ပျင်းရိသူ» is kept)")
p("make_ch21-25", "ကြီးငယ် အင်္ဂါ အားလုံး ပြည့်စုံ၍ မချို့ယွင်းသော အာရုံခံ", "ကြီးငယ် အင်္ဂါ အားလုံး ပြည့်စုံ၍ မယုတ်ညံ့သော အာရုံခံ", 1,
  "L09 hīna = ယုတ်ညံ့သော: ahīnindriyo ^5-691 «မယုတ်ညံ့သော» (the pi-2 ^2-951 witness _SAB is kept)")

# ------------------------------------------------------------------------------------------------------ L10 upagā
p("make_ch13-16", "သို့ ရောက်သော {F.SATTA}တို့", "သို့ ရောက်သွားသော {F.SATTA}တို့", 2,
  "L10 upagā = ရောက်သွားသော (decision upagā|0, family upagata / upage; approved yathākammūpaga «… ရောက်သွားသော»): "
  "«atthi X-ūpagā sattā» ^5-455, ^5-506, ^5-507, ^5-511, ^5-515, ^5-517")
p("make_ch6-10", "WHO16 = {f\"{k} devānaṃ\": f\"{v} နတ်တို့၏\" for k, v in DEVA_N.items()}",
  "DEVA_N[\"ākāsānañcāyatanūpagānaṃ\"] = DEVA_N[\"ākāsānañcāyatanūpagānaṃ\"].replace(\"ရောက်သော\", \"ရောက်သွားသော\")   # rails L10\n"
  "WHO16 = {f\"{k} devānaṃ\": f\"{v} နတ်တို့၏\" for k, v in DEVA_N.items()}", 1,
  "L10 upagānaṃ = ရောက်သွားသော (decision upagānaṃ|0): ākāsānañcāyatanūpagānaṃ devānaṃ ^5-337 (the pi-2 ^2-1028 "
  "witness is kept, the pi-5 value derived)")
p("make_ch2-5", "{BRAHMALOKA}သို့ ရောက်ကြ၏", "{BRAHMALOKA}သို့ ရောက်သွားကြ၏", 2,
  "L10 upagā = ရောက်သွားသော: the verse «brahmalokūpagā ahu» ^5-281")

# ------------------------------------------------------------------------------------------------------ L11 diṭṭhadhamma
p("make_ch21-25", 'DDS = new("diṭṭhadhammasukhavihāra", "ယခုဘဝ၌ ချမ်းသာစွာ နေခြင်း ဖြစ်သော")',
  'DDS = new("diṭṭhadhammasukhavihāra", "မျက်မှောက်ဘဝ၌ ချမ်းသာစွာ နေခြင်း ဖြစ်သော")', 1,
  "L11 diṭṭhadhamma = မျက်မှောက်ဘဝ (decision diṭṭhadhamma|0, pi-2 / pi-1 locked; «ယခုဘဝ» aligns): "
  "diṭṭhadhammasukhavihāra ^5-703, ^5-704, ^5-768, ^5-769, ^5-771, ^5-773")

# ------------------------------------------------------------------------------------------------------ L12 iṭṭha / aniṭṭha (phala)
p("make_ch17-20", 'IPH = "လိုလားအပ်သော အကျိုး"', 'IPH = "လိုလားဖွယ် အသီးအပွင့်"', 1,
  "L12 iṭṭha = လိုလားဖွယ်, iṭṭhaphalaṃ = လိုလားဖွယ် အသီးအပွင့် ရှိသော, Aniṭṭha = မလိုလားဖွယ် (decisions iṭṭha|0 §A23 «ch18 "
  "«လိုလားအပ်သော» aligns», iṭṭhaphalaṃ|0, aniṭṭha|0; = the sample's _FR_K «လိုလားဖွယ် အသီးအပွင့် ရှိသော»): ch18 ^5-591 …")

# ------------------------------------------------------------------------------------------------------ L13 yaṃ kiñci
p("make_ch13-16", 'V(f"{VN} မှန်သမျှ ထိုအားလုံးသည် {VIMUTTA}")', 'V(f"မည်သည့် {VN}မဆို ထိုအားလုံးသည် {VIMUTTA}")', 1,
  "L13 Yaṃ kiñci = မည်သည့် … မဆို (decision Yaṃ kiñci|0, pi-2 locked; «မှန်သမျှ» aligns): ^5-418")
p("make_ch13-16", 'V(f"{_cm} စိတ်ကြောင့် ဖြစ်ပေါ်သော {F.RUPA.my} မှန်သမျှ ထိုအားလုံးသည် {_cm}")',
  'V(f"{_cm} စိတ်ကြောင့် ဖြစ်ပေါ်သော မည်သည့် {F.RUPA.my}မဆို ထိုအားလုံးသည် {_cm}")', 1,
  "L13 Yaṃ kiñci = မည်သည့် … မဆို: ^5-528, ^5-532 … ^5-534")
p("make_ch6-10", "‹ဖြစ်ပေါ်ခြင်း သဘော ရှိသော အရာ မှန်သမျှ အားလုံးသည် ချုပ်ငြိမ်းခြင်း သဘော ရှိ၏›ဟု",
  "‹ဖြစ်ပေါ်တတ်သော သဘော ရှိသော မည်သည့် အရာမဆို အားလုံးသည် ချုပ်ငြိမ်းတတ်သော သဘော ရှိ၏›ဟု", 1,
  "L13 yaṃ kiñci = မည်သည့် … မဆို (decision Yaṃ kiñci|0: «the stock phrase yaṃ kiñci samudayadhammaṃ … «မှန်သမျှ» "
  "aligns»), §A20 nirodhadhammaṃ = ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော (decision nirodhadhammaṃ|0, «ch10 … aligns»): ^5-317, "
  "^5-321, ^5-325, ^5-346; samudayadhammaṃ «ဖြစ်ပေါ်တတ်သော သဘော» = ch3's wording of the same sutta")
p("make_ch21-25", "{ADUKKHA} ခံစားမှုဖြစ်စေ အကြင် ခံစားမှုကို ခံစား၏၊", "{ADUKKHA} ခံစားမှုဖြစ်စေ မည်သည့် ခံစားမှုကိုမဆို ခံစား၏၊", 1,
  "L13 yaṃ kiñci = မည်သည့် … မဆို: «yaṃ kiñci vedanaṃ vedayati» ^5-675")
p("make_ch21-25", 'f"{_R} ရုပ် ဟူသမျှသည် {MAHAB} {F.NUM_MY[4]}{F.CL}နှင့် {_UPR} ဖြစ်၏")',
  'f"{_R} မည်သည့် ရုပ်မဆို {MAHAB} {F.NUM_MY[4]}{F.CL}နှင့် {_UPR} ဖြစ်၏")', 1,
  "L13 yaṃ kiñci = မည်သည့် … မဆို: «yaṃ kiñci, bhikkhave, rūpaṃ …» ^5-699")

# ------------------------------------------------------------------------------------------------------ L14 anuttara, uttamo
p("make_ch2-5", '"“သီလ၊ သမာဓိ၊ ပညာနှင့် အမြတ်ဆုံး လွတ်မြောက်မှု၊"', '"“သီလ၊ သမာဓိ၊ ပညာနှင့် ထိုထက် သာလွန်သည် မရှိသော လွတ်မြောက်မှု၊"', 1,
  "L14 anuttarā = ထိုထက် သာလွန်သည် မရှိသော (decision anuttarā|0, pi-3 locked; kept apart from seṭṭha «အမြတ်ဆုံး»): ^5-281")
p("make_ch11-12", 'f"“{MC}၊ {DC}၊ အမြတ်ဆုံး {PC}၊"', 'f"“{MC}၊ {DC}၊ ထိုထက် သာလွန်သည် မရှိသော {PC}၊"', 1,
  "L14 anuttaraṃ = ထိုထက် သာလွန်သည် မရှိသော (decision anuttaraṃ|0, pi-2 locked): ^5-374 paññācakkhuṃ anuttaraṃ")
p("make_ch11-12", 'f"အကြင်အခါ၌ အမြတ်ဆုံး {PC}ဟူသော ဉာဏ် ဖြစ်ပေါ်လာ၏၊"', 'f"အကြင်အခါ၌ ထိုထက် သာလွန်သည် မရှိသော {PC}ဟူသော ဉာဏ် ဖြစ်ပေါ်လာ၏၊"', 1,
  "L14 anuttaraṃ = ထိုထက် သာလွန်သည် မရှိသော: ^5-374 (the same verse, second stanza)")
p("make_ch11-12", 'f"ဤမျက်စိ {F.NUM_MY[3]}{F.CL}တို့ကို လူတို့တွင် အမြတ်ဆုံးသူသည် ဟောကြားတော်မူခဲ့၏{END}")',
  'f"ဤမျက်စိ {F.NUM_MY[3]}{F.CL}တို့ကို လူတို့တွင် အထွတ်အထိပ် ဖြစ်တော်မူသူသည် ဟောကြားတော်မူခဲ့၏{END}")', 1,
  "L14 uttamo = အထွတ်အထိပ် (decision uttamo|0, pi-4 locked; kept apart from seṭṭho): purisuttamo ^5-374")
p("make_ch11-12", 'f"“ငါသည် လောက၌ {ARAHA} ဖြစ်၏၊ ငါသည် အမြတ်ဆုံး ဆရာ ဖြစ်၏၊"', 'f"“ငါသည် လောက၌ {ARAHA} ဖြစ်၏၊ ငါသည် ထိုထက် သာလွန်သည် မရှိသော ဆရာ ဖြစ်၏၊"', 1,
  "L14 anuttaro = ထိုထက် သာလွန်သည် မရှိသော (decision anuttaro|0): ^5-405 ahaṃ satthā anuttaro")
p("make_ch21-25", '"လောက၏ အမြတ်ဆုံး ကောင်းမှု လယ်မြေ")', '"လောက၏ ထိုထက် သာလွန်သည် မရှိသော ကောင်းမှု လယ်မြေ")', 1,
  "L14 anuttaraṃ = ထိုထက် သာလွန်သည် မရှိသော: anuttaraṃ puññakkhettaṃ lokassa ^5-791, ^5-793, ^5-797, ^5-800")

# ------------------------------------------------------------------------------------------------------ L15 samanantarā
p("make_ch26-31", 'bb(f"{BUDDHA}သည် စတုတ္ထ {JH}မှ ထ၍ ချက်ချင်း", "ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့"))',
  'bb(f"{BUDDHA}သည် စတုတ္ထ {JH}မှ ထ၍ ချက်ချင်း နောက်၌", "ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့"))', 1,
  "L15 samanantarā = ချက်ချင်း နောက်၌ (decision samanantarā|0, pi-4 / pi-2 locked): ^5-896")

# ------------------------------------------------------------------------------------------------------ L16 sayaṃ
p("make_sample", 'V(f"{SD}သည် မိမိ ပြုထားသော အရာ")', 'V(f"{SD}သည် ကိုယ်တိုင် ပြုထားသော အရာ")', 1,
  "L16 sayaṃ = ကိုယ်တိုင် (decision sayaṃ|0, pi-4 / pi-2 locked: «sayaṃkataṃ «ကိုယ်တိုင် ပြုသော»; keeps «မိမိ» for atta / "
  "saka»): Sayaṅkataṃ sukhadukkhaṃ ^5-171")
p("make_sample", 'V(f"{SD}သည် မိမိ ပြုထားသော အရာလည်း၊ ', 'V(f"{SD}သည် ကိုယ်တိုင် ပြုထားသော အရာလည်း၊ ', 1,
  "L16 sayaṃ = ကိုယ်တိုင်: sayaṅkatañca paraṅkatañca ^5-175 / ^5-179")
p("make_sample", 'f"{SD}သည် မိမိ မပြု၊ သူတစ်ပါး မပြုဘဲ', 'f"{SD}သည် ကိုယ်တိုင် မပြု၊ သူတစ်ပါး မပြုဘဲ', 1,
  "L16 sayaṃ = ကိုယ်တိုင်: asayaṅkāraṃ … ^5-177")

# ------------------------------------------------------------------------------------------------------ L17 ṭhito / ṭhitā
p("make_ch6-10", "ဖိုလ်၌ တည်သူ", "ဖိုလ်၌ တည်နေသူ", 3,
  "L17 ṭhito = တည်နေသော (decision ṭhito|0, pi-4 locked; = pi-4 L01 «ဖိုလ်၌ တည်နေသူ»): phale ṭhito ^5-344 …")
p("make_ch6-10", "အမည်ရှိသော တပည့်သည် ဗြဟ္မာ့လောက၌ တည်လျက် ", "အမည်ရှိသော တပည့်သည် ဗြဟ္မာ့လောက၌ တည်နေလျက် ", 1,
  "L17 ṭhito = တည်နေသော: brahmaloke ṭhito ^5-333")
p("make_ch11-12", "ဘက်၌ တည်သူ", "ဘက်၌ တည်နေသူ", 2,
  "L17 ṭhito = တည်နေသော: bāhiro puthujjanapakkhe ṭhito ^5-371 / ^5-372")
p("make_ch21-25", "ဖိုလ်၌ တည်ပြီးသူ လေးယောက်တို့သည်", "ဖိုလ်၌ တည်နေသူ လေးယောက်တို့သည်", 1,
  "L17 ṭhitā = တည်နေသော (decision ṭhitā|0, pi-4 locked, family ṭhito): «cattāro ca phale ṭhitā» ^5-798")

# ------------------------------------------------------------------------------------------------------ L18 ruhiruppādaka (§A13)
p("make_ch6-10", '"ruhiruppādako": "ဘုရားရှင်၏ သွေးကို စိမ်းစေသူ"', '"ruhiruppādako": "ဘုရားရှင်၏ သွေးကို ထွက်စေသူ"', 1,
  "L18 §A13 ruhiruppādako = ဘုရားရှင်၏ သွေးကို ထွက်စေသူ (decisions ruhiruppādako|0, uppādako|0, ruhiruppādako ānantariko|0: "
  "= ch3 ^5-269, uppādeyya «ထွက်စေ» pi-2 locked): ch10 ^5-334, ^5-350, ch28 ^5-847, ch29 ^5-859, ch30 ^5-877")
p("make_ch2-5", "‹ဖြစ်ပေါ်တတ်သော သဘော ရှိသမျှ အားလုံးသည် ချုပ်ငြိမ်းတတ်သော သဘော ရှိ၏›ဟု",
  "‹ဖြစ်ပေါ်တတ်သော သဘော ရှိသော မည်သည့် အရာမဆို အားလုံးသည် ချုပ်ငြိမ်းတတ်သော သဘော ရှိ၏›ဟု", 1,
  "L13 yaṃ kiñci = မည်သည့် … မဆို: the same sutta in ch3 (^5-278 …) = ch10 (identical Pāli = identical Burmese)")
p("make_ch2-5", "အရိယာ တပည့်အား မြူ ကင်းသော၊ အညစ်အကြေး ကင်းသော", "အရိယာ တပည့်အား မြူမှုန် ကင်းသော၊ အညစ်အကြေး ကင်းသော", 1,
  "L13 virajaṃ = မြူမှုန် ကင်းသော (decision virajaṃ|0, 4 of 5 uses; = ch10's wording of the same sutta): ^5-278")

# ------------------------------------------------------------------------------------------------------ L19 buddha family
p("make_ch11-12", "ဗောဓိဖြင့် ဘုရား ဖြစ်သည်ဟူသော", "ဗောဓိဖြင့် ဘုရားရှင် ဖြစ်သည်ဟူသော", 2,
  "L19 buddho = ဘုရားရှင် (decision buddho|0, family buddha pi-2 / pi-4 locked; «ဘုရား» aligns): heading ^5-12-6-1-0")
p("make_ch11-12", 'BUD = "ဘုရား"', 'BUD = "ဘုရားရှင်"', 1,
  "L19 buddho = ဘုရားရှင်: bodhiyā buddho, sāvako hutvā buddho ^5-398, ^5-399, ^5-403, ^5-417")
p("make_ch2-5", 'VV(f"ဘုရား၌ {F.AVECCA}နှင့်", "ပြည့်စုံ")', 'VV(f"ဘုရားရှင်၌ {F.AVECCA}နှင့်", "ပြည့်စုံ")', 1,
  "L19 buddhe = ဘုရားရှင် (decision buddhe|0, pi-2 locked): buddhe aveccappasādena ^5-274, ^5-340, ^5-366")
p("make_ch2-5", "ဘုရား၌ ကြည်ညို", "ဘုရားရှင်၌ ကြည်ညို", 2,
  "L19 buddhe = ဘုရားရှင်: «atthi devā buddhe pasannā» ch3 (the same word)")
p("make_ch6-10", '"buddhānussati": f"ဘုရားကို {ANUSS}"', '"buddhānussati": f"ဘုရားရှင်ကို {ANUSS}"', 1,
  "L19 buddha = ဘုရားရှင် (decision buddha|0): buddhānussati ^5-301")
p("make_ch21-25", 'Cl(f"{_KS} ဘုရားလည်း လောက၌"', 'Cl(f"{_KS} ဘုရားရှင်လည်း လောက၌"', 1,
  "L19 buddho = ဘုရားရှင်: kappo ca saṇṭhāti buddho ca loke uppajjati ^5-654")
p("make_ch21-25", 'f"ဘုရားအား လှူသော {DAK}သည် အကျိုး ကြီးမားသည်ဟု"', 'f"ဘုရားရှင်အား လှူသော {DAK}သည် အကျိုး ကြီးမားသည်ဟု"', 1,
  "L19 buddhassa = ဘုရားရှင် (decision Buddhassa|0): heading ^5-25-10-1-0")
p("make_ch21-25", '(("saṅghassa", SG), ("buddhassa", "ဘုရား"))', '(("saṅghassa", SG), ("buddhassa", "ဘုရားရှင်"))', 1,
  "L19 buddhassa = ဘုရားရှင်: buddhassa dinnaṃ mahapphalaṃ ^5-799")
p("make_ch26-31", "သည် ဘုရား၏ နယ်ပယ် အားလုံးကို", "သည် ဘုရားရှင်၏ နယ်ပယ် အားလုံးကို", 1,
  "L19 buddha = ဘုရားရှင်: buddhavisaya ^5-882, ^5-893")
p("make_ch26-31", '_BS = f"ဘုရားတို့၏ဖြစ်စေ {SAV}တို့၏ဖြစ်စေ"', '_BS = f"ဘုရားရှင်တို့၏ဖြစ်စေ {SAV}တို့၏ဖြစ်စေ"', 1,
  "L19 buddhānaṃ = ဘုရားရှင် (decision buddhānaṃ|0, pi-4 locked): ^5-883, ^5-884, ^5-891")
p("make_ch26-31", "ဘုရားအကြောင်း {KATHA}", "ဘုရားရှင်အကြောင်း {KATHA}", 2,
  "L19 buddha = ဘုရားရှင်: heading Buddhakathā ^5-29-5-1-0")
p("make_ch26-31", "ဘုရားတို့၌ ဘုရားတို့ထက်", "ဘုရားရှင်တို့၌ ဘုရားရှင်တို့ထက်", 2,
  "L19 buddhānaṃ buddhehi = ဘုရားရှင်: hīnātirekatā ^5-885, uddāna ^5-891")
p("make_ch26-31", "အရပ် အားလုံးတို့၌ ဘုရားတို့", "အရပ် အားလုံးတို့၌ ဘုရားရှင်တို့", 2,
  "L19 buddhā (tiṭṭhanti) = ဘုရားရှင် (decisions buddhā|0, buddhā tiṭṭhanti|0): ^5-886, uddāna ^5-891")
p("make_ch26-31", 'Cl(f"{_m} အရပ်၌ ဘုရား", *STD)', 'Cl(f"{_m} အရပ်၌ ဘုရားရှင်", *STD)', 1,
  "L19 buddho = ဘုရားရှင်: «puratthimāya disāya buddho tiṭṭhati» ^5-886")
p("make_ch26-31", "ငါသည် ဘုရား မျက်စိဖြင့် လောကကို", "ငါသည် ဘုရားရှင် မျက်စိဖြင့် လောကကို", 1,
  "L19 buddha = ဘုရားရှင်: buddhacakkhunā ^5-856")

# ------------------------------------------------------------------------------------------------------ L20 saha
p("my5_formulas", '("Sahāvassa dassanasampadāya,", "“ထိုသူ၏ အမြင် ပြည့်စုံခြင်းနှင့် တစ်ပြိုင်နက်ပင်၊"),',
  '("Sahāvassa dassanasampadāya,", "“ထိုသူ၏ အမြင် ပြည့်စုံခြင်းနှင့် အတူပင်၊"),', 1,
  "L20 saha = အတူ (decision saha|0, pi-2 locked: «တစ်ပြိုင်နက် (saha upapattiyā, ^5-278 …) aligns»): the ratana verse "
  "^5-278, ^5-317, ^5-321, ^5-325")
p("make_ch11-12", 'SAHA_U = new("saha upapattiyā", "ပြန်လည် ဖြစ်ပေါ်သည်နှင့် တစ်ပြိုင်နက်")',
  'SAHA_U = new("saha upapattiyā", "ပြန်လည် ဖြစ်ပေါ်သည်နှင့် အတူ")', 1,
  "L20 saha = အတူ: saha upapattiyā ^5-388 … ^5-390")
p("make_ch2-5", "ဖြစ်ပေါ်သည်နှင့် တစ်ပြိုင်နက် အရိယာ တပည့်သည်", "ဖြစ်ပေါ်သည်နှင့် အတူ အရိယာ တပည့်သည်", 1,
  "L20 saha = အတူ: saha dassanuppādā (the sutta ch3)")
p("make_ch6-10", "ဖြစ်ပေါ်သည်နှင့် တပြိုင်နက် အရိယာ တပည့်၏", "ဖြစ်ပေါ်သည်နှင့် အတူ အရိယာ တပည့်၏", 1,
  "L20 saha = အတူ: saha dassanuppādā (the same sutta ch10)")
p("make_ch2-5", "{ABHISAMAYA}နှင့် တစ်ပြိုင်နက်", "{ABHISAMAYA}နှင့် အတူ", 2,
  "L20 saha = အတူ: saha dhammābhisamayā ^5-280")

# ------------------------------------------------------------------------------------------------------ L21 niruddha
p("my5_formulas", 'return f"{n.my} ချုပ်ငြိမ်းသွားသောအခါ “{pq(m[\'b\'], \'stmt\', 1)}”ဟု ဆိုသင့်သလော{END}"',
  'return f"{n.my} ချုပ်ငြိမ်းပြီးသောအခါ “{pq(m[\'b\'], \'stmt\', 1)}”ဟု ဆိုသင့်သလော{END}"', 1,
  "L21 niruddhe / niruddhāya = ချုပ်ငြိမ်းပြီးသော (decisions niruddhe|0, niruddhāya|0, family pi-2 locked niruddhaṃ / "
  "niruddhā; «ချုပ်ငြိမ်းသွားသော» aligns): the frame «X-mhi niruddhe …» ch1 ^5-104 … ^5-106")
p("make_sample", 'return Cl(f"{HAVER[m[\'x\']]} {PUG}", "ချုပ်ငြိမ်းသွား", "မချုပ်ငြိမ်းသွား")',
  'return Cl(f"{HAVER[m[\'x\']]} {PUG}", "ချုပ်ငြိမ်းပြီး ဖြစ်", "ချုပ်ငြိမ်းပြီး မဖြစ်")', 1,
  "L21 niruddho (no entry; family niruddha «ချုပ်ငြိမ်းပြီးသော»): «B puggalo niruddho» inside the same frame ^5-104 …")
p("make_ch11-12", "ချုပ်ငြိမ်း၍ ကင်းပျောက်၍ ငြိမ်းအေးသွားသောအခါ", "ချုပ်ငြိမ်းပြီး၍ ကင်းပျောက်၍ ငြိမ်းအေးပြီးသောအခါ", 1,
  "L21 niruddhāya = ချုပ်ငြိမ်းပြီးသော, paṭipassaddhāya = ငြိမ်းအေးပြီးသော (decisions niruddhāya|0, paṭipassaddhāya|0): "
  "^5-398")
p("make_ch13-16", "ဖြစ်ပေါ်၍ ချုပ်ငြိမ်းသွားသောအခါ", "ဖြစ်ပေါ်၍ ချုပ်ငြိမ်းပြီးသောအခါ", 2,
  "L21 niruddhe = ချုပ်ငြိမ်းပြီးသော: niyāme uppajjitvā niruddhe ^5-447")
p("make_ch17-20", "ဖြစ်ပေါ်ပြီး ချုပ်ငြိမ်းသွားသောအခါ", "ဖြစ်ပေါ်ပြီး ချုပ်ငြိမ်းပြီးသောအခါ", 1,
  "L21 niruddhe = ချုပ်ငြိမ်းပြီးသော: sīle uppajjitvā niruddhe ^5-594, ^5-597")
p("make_ch6-10", 'NIR = ("ချုပ်ငြိမ်းသွား", "မချုပ်ငြိမ်းသွား")', 'NIR = ("ချုပ်ငြိမ်းပြီး ဖြစ်", "ချုပ်ငြိမ်းပြီး မဖြစ်")', 1,
  "L21 niruddhā = ချုပ်ငြိမ်းပြီးသော (decision niruddhā|0, pi-2 locked): «… samāpannassa Y niruddhā hoti» ^5-333")

# ------------------------------------------------------------------------------------------------------ L22 tiṭṭhati / saṇṭhāti
p("make_ch2-5", 'SANTHATI = new("saṇṭhāti", "တည်")', 'SANTHATI = new("saṇṭhāti", "တည်နေ")', 1,
  "L22 saṇṭhāti = တည်နေသည် (decision saṇṭhāti|0, pi-4 locked, = tiṭṭhati): ch2 ^5-241, ch4 ^5-280 …")
p("make_ch13-16", 'Cl(f"ပထမဦးစွာ မြေ တည်၏၊ နောက်မှ', 'Cl(f"ပထမဦးစွာ မြေ တည်နေ၏၊ နောက်မှ', 1,
  "L22 saṇṭhāti = တည်နေသည်: paṭhamaṃ pathavī saṇṭhāti ^5-493")
p("make_ch21-25", '"တည်", "မတည်"))', '"တည်နေ", "မတည်နေ"))', 4,
  "L22 saṇṭhāti = တည်နေသည်: saḷāyatanaṃ … saṇṭhāti, upapattesiyena cittena … saṇṭhāti ^5-691")
p("make_ch21-25", 'f"{m} တည်၍" for _, m in _BODY[:-1]', 'f"{m} တည်နေ၍" for _, m in _BODY[:-1]', 1,
  "L22 saṇṭhāti / saṇṭhanti = တည်နေ: hatthā saṇṭhanti … ^5-691")
p("make_ch26-31", '"စိတ် (တစ်ခု၏ ခဏ)၌ မဟာပထဝီ မြေကြီး တည်၏၊ မဟာသမုဒ္ဒရာ တည်၏၊ မြင့်မိုရ် တောင်မင်း တည်၏၊ ရေ တည်၏၊ မီး တည်၏၊ "\n'
  '     "လေ တည်၏၊ မြက်၊ ထင်း၊ တောအုပ်၊ သစ်ပင်တို့", "တည်ကြ", "မတည်ကြ"))',
  '"စိတ် (တစ်ခု၏ ခဏ)၌ မဟာပထဝီ မြေကြီး တည်နေ၏၊ မဟာသမုဒ္ဒရာ တည်နေ၏၊ မြင့်မိုရ် တောင်မင်း တည်နေ၏၊ ရေ တည်နေ၏၊ မီး တည်နေ၏၊ "\n'
  '     "လေ တည်နေ၏၊ မြက်၊ ထင်း၊ တောအုပ်၊ သစ်ပင်တို့", "တည်နေကြ", "မတည်နေကြ"))', 1,
  "L22 saṇṭhāti = တည်နေသည်: citte mahāpathavī saṇṭhāti … ^5-906")
p("make_sample", 'SENT_1["Puggalo kiṃ nissāya tiṭṭhatīti?"] = f"{PUG}သည် အဘယ်ကို မှီ၍ တည်သနည်း{END}"',
  'SENT_1["Puggalo kiṃ nissāya tiṭṭhatīti?"] = f"{PUG}သည် အဘယ်ကို မှီ၍ တည်နေသနည်း{END}"', 1,
  "L22 tiṭṭhati = တည်နေသည် (decision tiṭṭhati|0, family ṭhito pi-4 locked): ^5-217")
p("make_sample", 'SENT_1["Bhavaṃ nissāya tiṭṭhatīti."] = f"ဘဝကို မှီ၍ တည်သည်{END}"',
  'SENT_1["Bhavaṃ nissāya tiṭṭhatīti."] = f"ဘဝကို မှီ၍ တည်နေသည်{END}"', 1,
  "L22 tiṭṭhati = တည်နေသည်: ^5-217")
p("make_sample", "ဒုက္ခသာ တည်၍ ပျက်ကွယ်၏၊", "ဒုက္ခသာ တည်နေ၍ ပျက်ကွယ်၏၊", 1,
  "L22 tiṭṭhati = တည်နေသည်: the verse «dukkhaṃ tiṭṭhati veti ca» ^5-233")
p("make_ch6-10", '"မာရ်နတ်၏ စစ်သည်ကို ဖြိုခွင်းလျက် တည်၏၊"', '"မာရ်နတ်၏ စစ်သည်ကို ဖြိုခွင်းလျက် တည်နေ၏၊"', 1,
  "L22 tiṭṭhati = တည်နေသည်: the verse «vidhūpayaṃ tiṭṭhati mārasenaṃ» ^5-321")
p("make_ch6-10", 'STAY = ("တည်", "မတည်")', 'STAY = ("တည်နေ", "မတည်နေ")', 1,
  "L22 tiṭṭhati = တည်နေသည်: «ekaṃ cittaṃ divasaṃ tiṭṭhati» ch10 (the same verb)")

# ------------------------------------------------------------------------------------------------------ L23 ekanirodha, assāsapassāsā
p("make_ch21-25", "အတူ ဖြစ်ပေါ်သော၊ အတူ ချုပ်သော၊ မှီရာ တူသော", "အတူ ဖြစ်ပေါ်သော၊ အတူ ချုပ်ငြိမ်းသော၊ မှီရာ တူသော", 1,
  "L23 nirodho / nirodhaṃ = ချုပ်ငြိမ်းခြင်း (decisions nirodho|0, nirodhaṃ|0, pi-4 / pi-2 locked): ekanirodha «အတူ "
  "ချုပ်ငြိမ်းသော» (the verb of the term; = ch15's «… တစ်ပြိုင်နက် ချုပ်ငြိမ်းကြ»): ^5-703, ^5-704, ^5-768 …")
p("make_ch6-10", '"assāsapassāsā": "ထွက်သက် ဝင်သက်"', '"assāsapassāsā": "ဝင်လေ ထွက်လေ"', 1,
  "L23 assāsapassāsā = ဝင်လေ ထွက်လေ (decision assāsapassāsā|0, family assāsapassāso: one order, one word; = ch28): ^5-333")


# ------------------------------------------------------------------------------------------------------ L24 sukha (§A19)
p('make_ch21-25', 'သုခ ဒုက္ခ', 'ချမ်းသာနှင့် ဆင်းရဲ', 2,
  'L24 §A19 sukhadukkhaṃ = ချမ်းသာနှင့် ဆင်းရဲ (decisions sukhadukkhaṃ|0 «သုခ ဒုက္ခ aligns», parakataṃ sukhadukkhaṃ|0): ^5-801 …')
p('make_ch21-25', 'သုခ', 'ချမ်းသာ', 11,
  'L24 §A19 sukha / sukhaṃ = ချမ်းသာ (decisions sukha|1, sukhaṃ|1: ««သုခ» (^5-748, ^5-775, ^5-801, ch24 heading) aligns»): ch24 ^5-743 … ^5-747, ^5-775, ^5-24-3-1-0')

# ------------------------------------------------------------------------------------------------------ L25 paṭivedha family (coordinator change: «ထိုးဖောက်၍ သိ…»)
p('my5_formulas', '"Paṭivedhānuyogo": f"ထိုးထွင်း သိမြင်ခြင်းကို {ANUYOGA_W}",', '"Paṭivedhānuyogo": f"ထိုးဖောက်၍ သိခြင်းကို {ANUYOGA_W}",', 1,
  'L25 Paṭivedhānuyogo = ထိုးဖောက်၍ သိခြင်းကို စစ်ဆေးမေးမြန်းခြင်း (termbase/APPROVED.md coordinator change: the locked pi-4 paṭivedho term): ^5-1-20-0, ^5-205')
p('make_ch2-5', 'PATIVEDHA = "ထိုးထွင်း သိမြင်ခြင်း"', 'PATIVEDHA = "ထိုးဖောက်၍ သိခြင်း"', 1,
  'L25 paṭivedho / paṭivedha = ထိုးဖောက်၍ သိခြင်း (coordinator change): ch3 ^5-272, ^5-281')
p('make_ch2-5', 'အရာကို ထိုးထွင်း သိမြင်ရန်', 'အရာကို ထိုးဖောက်၍ သိရန်', 2,
  'L25 paṭivedhāya = ထိုးဖောက်၍ သိရန် (coordinator change): akuppapaṭivedhāya ^5-273')
p('make_ch2-5', 'အရာကို ထိုးထွင်း သိမြင်လျက်', 'အရာကို ထိုးဖောက်၍ သိလျက်', 1,
  'L25 paṭivijjhanto = ထိုးဖောက်၍ သိလျက် (coordinator change): ^5-279')
p('make_ch2-5', 'ထိုးထွင်း သိမြင်ပြီး', 'ထိုးဖောက်၍ သိပြီး', 4,
  'L25 paṭividdhaṃ / paṭividdhā = ထိုးဖောက်၍ သိပြီးသော (coordinator change): «anubuddhā paṭividdhā» ^5-281')
p('make_ch2-5', 'ထိုးထွင်း မသိမြင်ခြင်း', 'ထိုးဖောက်၍ မသိခြင်း', 3,
  'L25 appaṭivedhā = the negative of paṭivedha «ထိုးဖောက်၍ သိခြင်း» (coordinator change): ^5-281')
p('make_ch6-10', 'ရဟန္တာ ဖိုလ်ကို ထိုးထွင်း သိခြင်း', 'ရဟန္တာ ဖိုလ်ကို ထိုးဖောက်၍ သိခြင်း', 1,
  'L25 paṭivedho = ထိုးဖောက်၍ သိခြင်း: aññāpaṭivedho ^5-346')
p('make_ch17-20', 'ကြားကာလ၌ တရားကို ထိုးထွင်း သိမြင်ရန်', 'ကြားကာလ၌ တရားကို ထင်ထင်ရှားရှား သိမြင်ရန်', 1,
  'L25 abhisametuṃ = ထင်ထင်ရှားရှား သိမြင်ရန် (coordinator change: the abhisamaya family, locked pi-4): ^5-641')
p('make_ch6-10', 'ထိုးထွင်း သိကြ', 'ခွဲခြား သိကြ', 9,
  "L25 paṭivijānanti = ခွဲခြား သိသည် (decision paṭivijānanti|0, family paṭivijānāti; «ထိုးထွင်း» is paṭivedha's word): vohāraṃ … paṭivijānanti ^5-347, ^5-352")
p('make_ch6-10', 'ထိုးထွင်း မသိကြ', 'ခွဲခြား မသိကြ', 5,
  'L25 na paṭivijānanti = ခွဲခြား မသိ: ^5-347, ^5-352')

# ------------------------------------------------------------------------------------------------------ L26 parinipphanna (§A24), arūpadhātu, rūpadhātu
p('make_ch21-25', 'အမှန်တကယ် ဖြစ်ပေါ်ပြီး', 'ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီး', 2,
  "L26 §A24 parinipphanno / parinipphannaṃ = ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော (decisions parinipphanno|0, parinipphannaṃ|0: ch19's form): ch23 ^5-720 … ^5-723")
p('make_ch26-31', 'ပြည့်စုံစွာ ပြီးမြောက်', 'ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီး', 1,
  'L26 §A24 parinipphannaṃ = ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော: ch31 ^5-917, ^5-918')
p('make_ch21-25', '"arūpa": "ရုပ်မရှိသော ဓာတ်"', '"arūpa": "ရုပ်မရှိသော ဘုံ"', 1,
  'L26 arūpadhātu = ရုပ်မရှိသော ဘုံ (decision arūpadhātu|0, pi-2 locked, approved plane name): ch24 ^5-773, ^5-774, heading ^5-24-10-1-0')
p('make_ch21-25', '"rūpa": "သိမ်မွေ့သော ရုပ် ဓာတ်"', '"rūpa": "သိမ်မွေ့သော ရုပ်ဘုံ"', 1,
  'L26 rūpadhātu = သိမ်မွေ့သော ရုပ်ဘုံ (decision rūpadhātu|1, approved plane name): ch24 ^5-771, ^5-772')

# ------------------------------------------------------------------------------------------------------ L27 abhabba / bhabba
p('my5_formulas', 'RATANA_LAST = "ကြီးလေးသော ဒုစရိုက် ခြောက်ပါးတို့ကို ပြုလုပ်ရန် မစွမ်းနိုင်"', 'RATANA_LAST = "ကြီးလေးသော ဒုစရိုက် ခြောက်ပါးတို့ကို ပြုလုပ်ရန် မထိုက်တန်"', 1,
  'L27 abhabba = မထိုက်တန်သော (decision abhabba|0, pi-4 locked; mapper binding Abhabbo «မထိုက်တန်»): the ratana verse «chaccābhiṭhānāni abhabba kātuṃ» ^5-278, ^5-346 …')

# ------------------------------------------------------------------------------------------------------ L28 saṃvattaniya (§A26)
p('make_ch6-10', '"နိဗ္ဗာန်သို့ မပို့ဆောင်တတ်သော"', '"နိဗ္ဗာန်သို့ မဖြစ်စေတတ်သော"', 1,
  'L28 §A26 saṃvattaniyaṃ = ဖြစ်စေတတ်သော (decision saṃvattaniyaṃ|0: one verb «ဖြစ်စေ», pi-2 saṃvattanikā): anibbānasaṃvattaniyaṃ ^5-549, ^5-550')
p('make_ch6-10', '"နိဗ္ဗာန်သို့ ပို့ဆောင်တတ်သော"', '"နိဗ္ဗာန်ကို ဖြစ်စေတတ်သော"', 1,
  'L28 §A26 saṃvattaniyaṃ = ဖြစ်စေတတ်သော: nibbānasaṃvattaniyaṃ (the pair)')
p('make_ch26-31', '_SV = "သို့ ပို့ဆောင်တတ်သော ကံကို ပြုလျက်"', '_SV = "ကို ဖြစ်စေတတ်သော ကံကို ပြုလျက်"', 1,
  'L28 §A26 saṃvattaniyaṃ kammaṃ = ဖြစ်စေတတ်သော ကံ (decision saṃvattaniyaṃ kammaṃ|0): ^5-894')
p('make_ch26-31', '_LEAD = "သို့ ပို့ဆောင်တတ်၏"', '_LEAD = "ကို ဖြစ်စေတတ်၏"', 1,
  'L28 §A26 saṃvattanikā = ဖြစ်စေသော (decision saṃvattanikā|0, pi-2 locked): ^5-903, ^5-904')

# ------------------------------------------------------------------------------------------------------ L29 saññī, pisuṇa, khaṇika, āneñja (§A26 / §A27)
p('make_ch26-31', 'တရားဟု မှတ်ထင်လျက်', 'တရားဟု မှတ်သိလျက်', 1,
  'L29 saññī = မှတ်သိသော (decision saññī|0, pi-1 … pi-4 locked): dhammasaññī ^5-860 …')
p('make_ch26-31', 'ကုန်းချောစကား', 'ကုန်းတိုက်သော စကား', 2,
  'L29 §A27 pisuṇaṃ = ကုန်းတိုက်သော စကား (decision pisuṇaṃ|0, pi-4 locked; «ch30 / ch31 «ကုန်းချောစကား» align»): ^5-901, ^5-903, ^5-908, ^5-909')
p('make_ch26-31', 'EKC = f"စိတ် {F.NUM_MY[1]}ခု၏ ခဏမျှသာ တည်သော အရာ"', 'EKC = f"စိတ် {F.NUM_MY[1]}ခဏ၌သာ ဖြစ်သော အရာ"', 1,
  'L29 Ekacittakkhaṇikā = စိတ် တစ်ခဏ၌သာ ဖြစ်သော (decisions Ekacittakkhaṇikā|0, khaṇikā|0, cittakkhaṇikā|0): ^5-906, ^5-907')
p('make_ch26-31', 'မတုန်မလှုပ်', 'မတုန်လှုပ်', 2,
  'L29 §A26 āneñja = မတုန်လှုပ်… (decisions āneñja|0, āneñje|0, pi-4 locked: one stem «မတုန်လှုပ်»): ^5-894, ^5-896, ^5-907, heading ^5-30-3-1-0')
p('my5_formulas', '(ch3 ^5-274; was «မတုန်မလှုပ်သော …» ch10 / ch11)', '(ch3 ^5-274; was «မတုန်လှုပ်သော …» ch10 / ch11)', 1,
  'L29 §A26 (a comment of my5_formulas that names the old word; changed so that the source has one stem)')

# ------------------------------------------------------------------------------------------------------ L30 yoni (decision yoni|0 «မွေးဖွားရာ အမျိုးအစား»)
p('make_ch17-20', '"tiracchānayoniṃ": "တိရစ္ဆာန် ဘဝသို့"', '"tiracchānayoniṃ": "တိရစ္ဆာန် မွေးဖွားရာ အမျိုးအစားသို့"', 1,
  'L30 tiracchānayoniṃ = တိရစ္ဆာန် မွေးဖွားရာ အမျိုးအစား (decision tiracchānayoniṃ|0, family yoni; the pi-2 ^2-811 tiracchānayonigāmī witness is kept): ^5-652, ^5-653')

# ------------------------------------------------------------------------------------------------------ L31 niyato, samaṅgī, dhammaṭṭhitatā / dhammaniyāmatā
p('make_ch21-25', 'NIYATO = new("niyato (a person)", "လမ်းကြောင်း သေချာပြီးသူ")', 'NIYATO = new("niyato (a person)", "ကျိန်းသေသူ")', 1,
  'L31 niyato = ကျိန်းသေသော (decisions niyato|0, Niyato|0, Micchattaniyato|0, pi-4 / pi-2 locked): ch21 ^5-663, ^5-664')
p('make_ch13-16', 'HAVING = "ကို ရရှိထားသော"', 'HAVING = "နှင့် ပြည့်စုံသော"', 1,
  'L31 samaṅgissa = ပြည့်စုံသော (decision samaṅgissa|0, pi-2 / pi-1 locked, 8 of 10): X-phalasamaṅgī ^5-419, ^5-420')
p('make_ch13-16', 'တရား၏ တည်ရှိခြင်း၊ တရား၏ သေချာခြင်း', 'သဘောတရားတို့၏ တည်နေခြင်း သဘော၊ သဘောတရားတို့၏ သေချာခြင်း', 3,
  'L31 dhammaṭṭhitatā = သဘောတရားတို့၏ တည်နေခြင်း သဘော, dhammaniyāmatā = သဘောတရားတို့၏ သေချာခြင်း (decisions dhammaṭṭhitatā|0, dhammaniyāmatā|0: the ch11 heading / ch19 debate): ^5-450, ^5-451')

# ------------------------------------------------------------------------------------------------------ L32 mixed single terms with one source line each
p('make_sample', 'လူ အတွဲ', 'လူ အစုံ', 2,
  'L32 §A28 purisayugā = လူ အစုံ, yugā = အစုံ (decisions purisayugā|0, yugā|0: «ch1 «လူ အတွဲ» aligns»): ^5-206, ^5-207')
p('make_ch17-20', 'အခါခပ်သိမ်း', 'အလုံးစုံ', 1,
  'L32 Sabbaso = အလုံးစုံ (decision Sabbaso|0, pi-2 locked: «အခါခပ်သိမ်း» means "always"): ^5-563, ^5-570')
p('make_ch26-31', 'ဖြန့်ကျက်', 'ဖြန့်ကြဲ', 3,
  'L32 §A26 visineti = ဖြန့်ကြဲသည် (decisions visineti|0, visinetvā|0): ^5-894')
p('make_ch26-31', '"ကျင့်ခဲ့"))', '"ပြုခဲ့"))', 1,
  'L32 akāsi = ပြုခဲ့သည် (decision akāsi|0, family karoti «ပြု»): aparantapaṃ akāsi ^5-913')
p('make_ch26-31', 'ပြင်းထန်သော အကျင့်ကို ကျင့်ခဲ့၊', 'ပြင်းထန်သော အကျင့်ကို ပြုခဲ့၊', 1,
  'L32 akāsi = ပြုခဲ့သည်: the uddāna ^5-918')
p('make_ch11-12', 'Cl(f"{BS}သည် {DKK}ကို", "ကျင့်ခဲ့", "မကျင့်ခဲ့"))', 'Cl(f"{BS}သည် {DKK}ကို", "ပြုခဲ့", "မပြုခဲ့"))', 1,
  'L32 akāsi = ပြုခဲ့သည်: dukkarakāriyaṃ akāsi ^5-404')
p('make_ch11-12', 'ခြိုးခြံသော အကျင့်ကို ကျင့်ခဲ့၍', 'ပြင်းထန်သော အကျင့်ကို ပြုခဲ့၍', 1,
  'L32 akāsi = ပြုခဲ့သည်, tapaṃ = ပြင်းထန်သော အကျင့် (decisions akāsi|0, tapaṃ|0): ^5-404')

p('make_sample', 'လူ့လောကမှ', 'လူ့ပြည်မှ', 2,
  'L32 manussalokā = လူ့ပြည် (decision manussalokā|0, family manussaloka): ^5-87, ^5-88')

p('make_ch11-12', 'မဂ်ကို ဟောကြားသူ', 'မဂ်ကို ပြောကြားသူ', 1,
  'L33 akkhātā = ပြောကြားသော (decision akkhātā|0, pi-4 locked): maggassa akkhātā ^5-354, ^5-443 (one source line for both)')

p('make_ch21-25', 'ASATA = new("asātarāgo", "မသာယာဖွယ်ကို တပ်မက်မှု")', 'ASATA = new("asātarāgo", "မသာယာဖွယ်ကို တပ်မက်သော ရာဂ")', 1,
  "L34 §A3 rāga = ရာဂ (decision rāga|0 / rāgo|0, pi-4 / pi-2 / pi-1 locked: «ch21 asātarāga «တပ်မက်မှု» (taṇhā's word) aligns»): ^5-21-8-1-0, ^5-675, ^5-685")
p('make_ch6-10', 'ဤ ဓမ္မ ဝိနည်း', 'ဤ တရား ဝိနည်း', 2,
  'L34 dhamma = တရား in dhammavinaya (decision dhamma|1: «here also in … dhammavinaya»; «ဓမ္မ» only the fixed name dhammacakka): ^5-333, ^5-346')

p('make_ch11-12', 'ယောကျ်ား', 'ယောက်ျား', 3,
  'L35 §A17 puriso / purisassa = ယောက်ျား (decisions puriso|0, purisassa|0: the standard spelling): ch12 ^5-402 …')
p('make_ch13-16', 'ယောကျ်ား', 'ယောက်ျား', 5,
  'L35 §A17 the standard spelling «ယောက်ျား»: ch15 ^5-491, ch16 ^5-514, ^5-539')
p('make_ch26-31', 'ပြည့်စုံစွာ မပြီးမြောက်သော', 'ပြည့်စုံစွာ မဖြစ်ပေါ်သော', 3,
  'L26 §A24 aparinipphanna = the negative of parinipphanna «ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော»: ch31 heading and ^5-917')
p('make_ch26-31', '"စိမ်းစေခဲ့ပြီး", "မစိမ်းစေရသေး"', '"ထွက်စေခဲ့ပြီး", "မထွက်စေရသေး"', 1,
  'L18 §A13 lohitaṃ uppāditaṃ = «… သွေးကို ထွက်စေခဲ့ပြီး» (uppādeyya «ထွက်စေ», pi-2 locked): ch28 ^5-847')

p('make_sample', 'ဒုတိယ စိတ် ဖြစ်ပေါ်သောအခါ', 'ဒုတိယ စိတ် ဖြစ်ပေါ်ပြီးသောအခါ', 3,
  'L36 uppanne = ဖြစ်ပေါ်ပြီးသော (decision uppanne|0, pi-1 locked): dutiye citte uppanne ^5-116, ^5-117')
p('make_ch13-16', 'ဤ{PUG}သည် တရားကို ထိုးထွင်း သိနိုင်သူ ဖြစ်သည်', 'ဤ{PUG}သည် တရားကို ထင်ထင်ရှားရှား သိမြင်ရန် ထိုက်တန်သူ ဖြစ်သည်', 1,
  'L36 bhabbo … abhisametuṃ = ထိုက်တန်သော … ထင်ထင်ရှားရှား သိမြင်ရန် (decisions bhabbo|0, abhisametuṃ|0): ^5-431')
p('make_ch11-12', 'ငါသည် လောက၏ အမြတ်ဆုံး ဖြစ်၏', 'ငါသည် လောက၏ အကောင်းဆုံး ဖြစ်၏', 1,
  'L36 seṭṭho = အကောင်းဆုံး (decision seṭṭho|0, pi-4 locked; agga keeps «ထိပ်ဆုံး»): seṭṭhohamasmi lokassa ^5-401')
p('make_ch26-31', 'အမြတ်ဆုံး ဖြစ်၏', 'အကောင်းဆုံး ဖြစ်၏', 4,
  'L36 seṭṭho = အကောင်းဆုံး: the verse «Maggānaṭṭhaṅgiko seṭṭho …» ^5-872')
p('make_ch26-31', '_FIRE = "ပူလောင်နေသော၊', '_FIRE = "လောင်ကျွမ်းနေသော၊', 1,
  'L36 ādittāya = လောင်ကျွမ်းနေသော (decision ādittāya|0, family ādittaṃ): ^5-868')
p('make_ch21-25', '"ခြေနှစ်ချောင်း ရှိသူတို့တွင် အမွန်မြတ်ဆုံး"', '"ခြေနှစ်ချောင်း ရှိသူတို့တွင် အကောင်းဆုံး"', 1,
  'L36 seṭṭho = အကောင်းဆုံး: dvipadānaṃ seṭṭho ^5-799')

p('make_ch26-31', 'အပါယ်သို့ ရောက်မည့်၊ ငရဲ၌ ကျမည့်၊', 'အပါယ်သို့ ရောက်သော၊ ငရဲ၌ ကျသော၊', 1,
  'L37 §A28 Āpāyiko = အပါယ်သို့ ရောက်သော, nerayiko = ငရဲ၌ ကျသော (decisions Āpāyiko|0, nerayiko|0: «ငရဲ၌ ကျမည့်» ^5-861 aligns)')
p('make_ch26-31', 'အပါယ်သို့ မရောက်မည့်၊ ငရဲ၌ မကျမည့်၊', 'အပါယ်သို့ မရောက်သော၊ ငရဲ၌ မကျသော၊', 1,
  'L37 §A28 the negatives of Āpāyiko / nerayiko: ^5-861')
p('make_sample', 'အမြဲ ထမင်း… အမြဲ ယာဂု', 'အမြဲ ထမင်း… ခိုင်ခံ့သော ယာဂု', 1,
  "L37 §A2 dhuva = ခိုင်ခံ့သော (decision dhuva|0: «nicca «မြဲ» and dhuva «ခိုင်ခံ့» stay apart in ^5-238»; «အမြဲ» is nicca's): dhuvayāgū ^5-238 (wording doubt)")

p('make_ch21-25', '"ခြေနှစ်ချောင်း ရှိသူတို့တွင် အထူးမြတ်ဆုံး"', '"ခြေနှစ်ချောင်း ရှိသူတို့တွင် အမွန်မြတ်ဆုံး"', 1,
  'L36 pavaro = အမွန်မြတ်ဆုံး (termbase pavaro): the fifth word of the list dvipadānaṃ aggo seṭṭho pamokkho uttamo pavaro ^5-799 (seṭṭho, the second, = «အကောင်းဆုံး»)')


p('make_ch21-25', '_SB = "ဆင်းရဲစေတတ်သည်လည်း ဖြစ် မဆင်းရဲစေတတ်သည်လည်း ဖြစ်သော"', '_SB = "ညှဉ်းဆဲမှု ရှိသည်လည်း ဖြစ် ညှဉ်းဆဲမှု ကင်းသည်လည်း ဖြစ်သော"', 1,
  'L39 sabyābajjhaṃ = ညှဉ်းဆဲမှု ရှိသော, abyābajjhaṃ = ညှဉ်းဆဲမှု ကင်းခြင်း, the pair sabyābajjhaṃ abyābajjhaṃ «ညှဉ်းဆဲမှု ရှိသော … ညှဉ်းဆဲမှု ကင်းသော» (termbase change 2026-11-22, coordinator): ^5-742')


# ====================================================================================================== bilingual review
# Fixes of the bilingual review (review/report-A.md, review/report-B.md; decisions review/fix-brief.md; results
# review/fix-notes.md) that change a repeated formula, proposition or term constant (L40 … L51). The single-segment
# fixes are the explicit rules F01 … of apply_fixes.py.
# ------------------------------------------------------------------------------------------------------ L40 A2 + A3 identity formula
p('make_sample', 'ဟူသော စကားကို ဦးစားမပေးဘဲ ဤစကားတို့သည် အနက် တူသော၊',
  'ဟူသော စကားကို မခွဲခြားဘဲ ဤစကားတို့သည် တစ်ခုတည်း ဖြစ်သော၊ အနက် တူသော၊', 2,
  'L40 A2 appiyaṃ karitvā = «…ဟူသော စကားကို မခွဲခြားဘဲ» (termbase appiyaṃ «မခွဲခြား», change 2026-11-22); A3 esese '
  '= «တစ်ခုတည်း ဖြစ်သော» (the predicate lost), then ekaṭṭhe «အနက် တူသော» …: kāyoti vā sarīranti vā … ^5-67, ^5-68')
p('make_ch2-5', 'ဟူသော စကားကို ဦးစားမပေးဘဲ ဤစကားတို့သည် အနက် တူသော၊',
  'ဟူသော စကားကို မခွဲခြားဘဲ ဤစကားတို့သည် တစ်ခုတည်း ဖြစ်သော၊ အနက် တူသော၊', 1,
  'L40 A2 appiyaṃ «မခွဲခြား» + A3 esese «တစ်ခုတည်း ဖြစ်သော»: SYN_TAIL, the Kālasaṃsandanā synonyms ^5-285')
p('make_ch6-10', '_SAME = "ဤစကားတို့သည် အနက် တူသော၊', '_SAME = "ဤစကားတို့သည် တစ်ခုတည်း ဖြစ်သော၊ အနက် တူသော၊', 1,
  'L40 A3 esese = «တစ်ခုတည်း ဖြစ်သော» (= sample _KAYA_SYN, asserted): atthaṭṭho natthaṭṭho … esese ekaṭṭhe ^5-304 … '
  '^5-306, ^5-501')

# ------------------------------------------------------------------------------------------------------ L41 B4 paṇidahantassa
p('make_ch13-16', '("paṇidahantassa", "ဆုတောင်းသူ၌", "ဆု မတောင်းသူ၌")', '("paṇidahantassa", "ဆုတောင်းသူ၌", "မဆုတောင်းသူ၌")', 1,
  'L41 B4 paṇidahantassa / appaṇidahantassa = «ဆုတောင်းသူ» / «မဆုတောင်းသူ» (termbase paṇidahantassa «ဆုတောင်းသော»): '
  'paribhogamaya ^5-484')
p('make_ch17-20', '"ဆုတောင်းသူ", "ဆု မတောင်းသူ")', '"ဆုတောင်းသူ", "မဆုတောင်းသူ")', 1,
  'L41 B4 paṇidahantassa / appaṇidahantassa «ဆုတောင်းသူ» / «မဆုတောင်းသူ»: vācā / kāyakamma ^5-564, ^5-566')
p('make_ch21-25', 'စိတ်ကို မထားရှိသူအား', 'မဆုတောင်းသူအား', 1,
  'L41 B4 appaṇidahantassa = «မဆုတောင်းသူ» (was «စိတ်ကို မထားရှိသူ»): ch22 ^5-686 … ^5-695')
p('make_ch21-25', 'စိတ်ကို ထားရှိသူအား', 'ဆုတောင်းသူအား', 2,
  'L41 B4 paṇidahantassa = «ဆုတောင်းသူ» (was «စိတ်ကို ထားရှိသူ»): ch22 ^5-686 … ^5-695')
p('make_ch26-31', 'စိတ် ဦးမတည်ထားသူ၌', 'မဆုတောင်းသူ၌', 1,
  'L41 B4 appaṇidahantassa = «မဆုတောင်းသူ» (was «စိတ် ဦးမတည်ထားသူ»): ch26 ^5-813 … ^5-815')
p('make_ch26-31', 'စိတ် ဦးတည်ထားသူ၌', 'ဆုတောင်းသူ၌', 1,
  'L41 B4 paṇidahantassa = «ဆုတောင်းသူ» (was «စိတ် ဦးတည်ထားသူ»): ch26 ^5-813 … ^5-815')

# ------------------------------------------------------------------------------------------------------ L42 B6 ānantariko / ānantariyassa
p('make_ch26-31', 'ANANT = new("ānantariko", "အနန္တရိယကံ ရှိသူ")', 'ANANT = new("ānantariko", "ချက်ချင်း အကျိုးပေးသော ကံ ရှိသူ")', 1,
  'L42 B6 ānantariko = «ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော» (termbase ānantariko, Dhammasaññī ānantariko, change '
  '2026-11-22; pi-2 / pi-4 ānantarika family; was the loanword «အနန္တရိယကံ»): ch28 ^5-857 … ^5-862, ^5-877')
p('make_ch13-16', 'ANANT = new("ānantariyo puggalo", "အနန္တရိယ ကံကို ပြုသော ပုဂ္ဂိုလ်")',
  'ANANT = new("ānantariyo puggalo", "ချက်ချင်း အကျိုးပေးသော ကံကို ပြုသော ပုဂ္ဂိုလ်")', 1,
  'L42 B6 ānantariyassa = «ချက်ချင်း အကျိုးပေးသော ကံကို ပြုသော» (termbase ānantariyassa, change 2026-11-22): ^5-508')

# ------------------------------------------------------------------------------------------------------ L43 B7 ariyo aṭṭhaṅgiko maggo
p('make_ch26-31', 'ဤ{AAM}၊ "\n  f"အရိယာ မဂ်သည် ပွားများခြင်း',
  'ဤ{AAM.replace("ရှိသော မဂ်", "ရှိသော အရိယာ မဂ်")}သည် "\n  f"ပွားများခြင်း', 1,
  'L43 B7 ariyo aṭṭhaṅgiko maggo = «အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်» (pi-2 ^2-486 / pi-3 one term; was «… မဂ်၊ အရိယာ '
  'မဂ်»): MN 3.431 ^5-874')
p('make_ch26-31', '_AM = f"{AAM}၊ အရိယာ မဂ်ကို"', '_AM = AAM.replace("ရှိသော မဂ်", "ရှိသော အရိယာ မဂ်") + "ကို"', 1,
  'L43 B7 ariyo aṭṭhaṅgiko maggo «အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်»: the Subhadda sutta ^5-875')

# ------------------------------------------------------------------------------------------------------ L44 B8 pettivisaya
p('make_ch13-16', '{F.PETA} နယ်ပယ်၊ {F.MANUSSA}', '{F.PETA} ဘုံ၊ {F.MANUSSA}', 1,
  'L44 B8 pettivisayo = «ပြိတ္တာ ဘုံ» (pi-2 ^2-811 «ပြိတ္တာ ဘုံသို့», = ch20 ^5-652 / ^5-653; termbase petti «ပြိတ္တာ»): '
  'the five gatis ^5-503')
p('make_ch26-31', 'ပြိတ္တာ နယ်{_LEAD}', 'ပြိတ္တာ ဘုံ{_LEAD}', 2,
  'L44 B8 pettivisayasaṃvattaniko = «ပြိတ္တာ ဘုံကို ဖြစ်စေတတ်၏» (pi-2 «ပြိတ္တာ ဘုံ»): ^5-903, ^5-904')

# ------------------------------------------------------------------------------------------------------ L45 B9 yadaniccaṃ taṃ dukkhaṃ / dukkhaññeva
p('make_ch26-31', 'V(f"ဆင်းရဲ ဒုက္ခသည်သာ {APN[1]}")', 'V(f"ဒုက္ခသည်သာ {APN[1]}")', 1,
  'L45 B9 dukkhaññeva = «ဒုက္ခသည်သာ» (termbase dukkhaṃ «ဒုက္ခ» in the noble-truth sense; no doubled «ဆင်းရဲ ဒုက္ခ»): '
  'ch31 thesis ^5-917, ^5-918')
p('make_ch26-31', '«မမြဲသော အရာသည် ဆင်းရဲ၏»ဟု {BUDDHA}', '«မမြဲသော အရာသည် ဒုက္ခ»ဟု {BUDDHA}', 1,
  'L45 B9 yadaniccaṃ taṃ dukkhaṃ = «“မမြဲသော အရာသည် ဒုက္ခ”ဟု» (one wording = ch10 ^5-338, ch25 ^5-787): ^5-917, ^5-918')

# ------------------------------------------------------------------------------------------------------ L46 B12 samphaṃ palapati
p('make_ch6-10', '("အကျိုးမဲ့ စကားကို", "ပြောရာ")', '("အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားကို", "ပြောရာ")', 1,
  'L46 B12 samphaṃ (palapeyya) = «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား» (termbase samphaṃ, change 2026-11-22; pi-1 … pi-4 '
  'samphappalāpa): ^5-314')
p('make_ch26-31', '("samphaṃ", "အကျိုးမဲ့ စကား ပြော")', '("samphaṃ", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား ပြော")', 1,
  'L46 B12 samphaṃ palapeyya / palapanti / palapitabbaṃ «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား»: ^5-901, ^5-908, ^5-909')

# ------------------------------------------------------------------------------------------------------ L47 B13 ch15 / ch16 = ch24
p('make_ch13-16', '    last = "".join(out)\n',
  '    last = "".join(out).replace("သာယာသော ခံစားမှုကို မဖြစ်စေတတ်သော၊ နာကျင်သော ခံစားမှုကို မဖြစ်စေတတ်သော… ", '
  '"သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော အရာ မဟုတ်၊ နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော အရာ မဟုတ်… ")\n', 1,
  'L47 B13 «na sukhavedaniyaṃ na dukkhavedaniyaṃ…pe… anārammaṇaṃ» = ch24 ^5-766 / ch20 ^5-636: «… ဖြစ်စေတတ်သော အရာ '
  'မဟုတ်၊ … ဖြစ်စေတတ်သော အရာ မဟုတ်…» (the full negative list of ^5-492 keeps its attributive «မဖြစ်စေတတ်သော»): '
  'ch15 ^5-492, ^5-494, ^5-495')
p('make_ch13-16', 'out.append(w + " ဖြစ်သော")', 'out.append(w + " ဖြစ်၍")', 1,
  'L47 B13 «X kusalo sārammaṇo / anārammaṇo» = ch24 ^5-760 … ^5-762: «… ကုသိုလ် ဖြစ်၍ အာရုံ ရှိသော အရာ» (was «… '
  'ကုသိုလ် ဖြစ်သော၊ အာရုံ …»): ch16 ^5-529 … ^5-532')
p('make_ch13-16', '    body = "၊ ".join(out)\n', '    body = "၊ ".join(out).replace(" ဖြစ်၍၊ ", " ဖြစ်၍ ")\n', 1,
  'L47 B13 no «၊» after the conjunctive «ဖြစ်၍» (= ch24)')

# ------------------------------------------------------------------------------------------------------ L48 B15 saḷāyataniko attabhāvo
p('make_ch13-16', 'SAL = new("saḷāyataniko attabhāvo", f"အာရုံခံ နယ်ပယ် {F.NUM_MY[6]}{F.CL} ရှိသော {_ATB}")',
  'SAL = new("saḷāyataniko attabhāvo", f"အာရုံခံ နယ်ပယ် {F.NUM_MY[6]}{F.CL} ရှိသော ကိုယ်ခန္ဓာ")', 1,
  'L48 B15 saḷāyataniko attabhāvo = «အာရုံခံ နယ်ပယ် ခြောက်ပါး ရှိသော ကိုယ်ခန္ဓာ» (termbase attabhāvo «ကိုယ်ခန္ဓာ»; the '
  'Pāli has no paṭilābha, so no «ရရှိခြင်း»; the 4 uses of the book): ^5-519, ^5-523, ^5-546')

# ------------------------------------------------------------------------------------------------------ L49 A16 Handa hi
p('make_ch6-10', 'f"အမှန်အားဖြင့် {MK}သည်', 'f"ကဲ၊ {MK}သည်', 1,
  'L49 A16 Handa hi (the answer «Handa hi …ti») = «ကဲ၊» (= ^5-272): ^5-307')
p('make_ch6-10', 'f"အမှန်အားဖြင့် {VIMATI}ကို', 'f"ကဲ၊ {VIMATI}ကို', 1,
  'L49 A16 Handa hi = «ကဲ၊» (= ^5-272): ^5-308')
p('make_ch13-16', 'f"ကောင်းပြီ၊ ရဟန္တာတို့ကို စွပ်စွဲ', 'f"ကဲ၊ ရဟန္တာတို့ကို စွပ်စွဲ', 1,
  'L49 A16 Handa hi = «ကဲ၊» (= ^5-272; was «ကောင်းပြီ၊»): ^5-546')

# ------------------------------------------------------------------------------------------------------ L50 B1 na ca arahā … (every verb)
p('make_ch17-20', 'P("na ca arahā" + _LONG, Cl(f"{ARAHA}သည်ကား {_LONGM}", _TIT[1], "မ" + _TIT[1], neg=True))',
  '_LONGM_N = (f"{_SEN}… {_MET} မမှီဝဲရာ၊ "\n'
  '           + "၊ ".join(_x.rsplit(" ", 1)[0] + " မ" + _x.rsplit(" ", 1)[1] for _x in _ACTL) + f"… {_TIT[0]}")\n'
  'P("na ca arahā" + _LONG, Cl(f"{ARAHA}သည်ကား {_LONGM_N}", _TIT[1], "မ" + _TIT[1], neg=True))', 1,
  'L50 B1 «na ca arahā … methunaṃ dhammaṃ paṭiseveyya, ajeḷakaṃ paṭiggaṇheyya … paṭiggaṇheyyāti?»: «na» governs every '
  'verb, so every verb is negative («မမှီဝဲရာ၊ … မခံယူရာ၊ …»): ^5-651')

# ------------------------------------------------------------------------------------------------------ L51 B5 active voropeti
p('make_ch21-25', '_VOR = W("2", "^2-U55", "Mātā jīvitā voropitā hoti", "အသက်မှ ချ")',
  '_VOR = W("2", "^2-U55", "Mātā jīvitā voropitā hoti", "အသက်မှ ချ").replace("ချ", "သတ်")', 1,
  'L51 B5 active jīvitā voropeti = «အသက်မှ သတ်…» (termbase voropeti «သတ်သည်», change 2026-11-22; pi-2 active voropeyya '
  '«သတ်သည်»; the pi-2 ^2-U55 witness of the passive voropitā «ချခံရ» is kept and still checked): ^5-780')
