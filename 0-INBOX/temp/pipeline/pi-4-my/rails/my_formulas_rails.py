"""pi-4 Burmese RAILS layer: the systematic termbase differences of the harmonised zero-shot, as in-memory source
patches of my4_formulas.py and of the zero-shot generators (none of them is edited on disk). Model: the approved
pi-3 / pi-2 rails layers (pi-3-my/rails/my_formulas_rails.py, pi-2-my/rails/my_formulas_rails.py, read only).

Each patch is (old, new, count, reason): build_rails.py applies it to the source text before running it and fails
unless «old» occurs exactly «count» times. Patching the source (not the finished text) keeps every derived string
(tables, frames, the sample tables reused by the later generators) consistent: identical Pāli = identical Burmese.
Reasons start with the family id (Lnn), then the termbase headword(s) = term and the decision
(AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md, locked, sha256 6ba052ff… since 2026-11-20 (was c6a4e611…); termbase/decisions-A.tsv), or
the logged text inconsistency «H n» (mapper-my/map-harmonise-notes.md, «Text inconsistencies for the rails step»,
item n). A make_sample patch applies both where make_sample runs and where the later generators import it.
Where a witnessed pi-1 / pi-2 value (my4_formulas.witness) holds the old word, the witness is kept (it still checks
the pi-2 text) and the pi-4 value is derived from it with one explicit replacement.
"""

# ------------------------------------------------------------------------------------------------- my4_formulas.py
FORMULA_PATCHES = []

# ------------------------------------------------------------------------------------------------- generators
GEN_PATCHES = {
    # ============================================================================ sample: preamble, 1, 2
    "make_sample": [
        ("၌ တည်သောအခါ {N[", "၌ တည်နေသောအခါ {N[", 2,
         "L01 ṭhito = တည်နေသော (decision ṭhito|0; H10: phale ṭhito = the approved NAME «ဖိုလ်၌ တည်နေသူ»; "
         "^4-29 / ^4-30 and the reused ^4-206 / ^4-208 «ဖိုလ်၌ တည်သောအခါ» align)"),
        ("    f\"{N['maggasamaṅgī']} လေး{CLP}{C} {G['phalasamaṅgino']} {PUG} လေး{CLP}{END}\")",
         "    f\"{G['maggasamaṅgino']} {PUG} လေး{CLP}{C} {G['phalasamaṅgino']} {PUG} လေး{CLP}{END}\")", 1,
         "L02 ^4-M-14 (8) maggasamaṅgino = the approved group NAME «မဂ်နှင့် ပြည့်စုံသော ပုဂ္ဂိုလ် Nယောက်» "
         "(my4-zeroshot-terms «N maggasamaṅgino puggalā», as phalasamaṅgino in the same line; H12); the same Pāli "
         "line is reused in the ^4-207 question"),
    ],
    # ============================================================================ chapters 3, 4
    "make_ch3-4": [
        ('SUNATI = f"ထိုသူသည် ကြားရ၏"', 'SUNATI = f"ထိုသူသည် ကြား၏"', 1,
         "L03 suṇāti = ကြားသည် (decision suṇāti|0, pi-1 / pi-2 locked; H6: one verb «ကြား», ^4-91 … ^4-93)"),
        ("အဆုံး၌ ကောင်းသော တရားကို ဟောကြားကြ၏{C} ", "အဆုံး၌ ကောင်းသော တရားကို ဟောကြ၏{C} ", 1,
         "L04 desenti = ဟောသည် (decision desenti|0, pi-2 locked; bhikkhū desenti|0; H1: = ^4-177 deseti «ဟော»; "
         "«ဟောကြား» is paveda-'s word)"),
        ("မြင့်မြတ်သော အကျင့်ကို ထုတ်ဖော် ပြကြ၏{END}", "မြင့်မြတ်သော အကျင့်ကို ထင်ရှားပြကြ၏{END}", 1,
         "L05 pakāsenti = ထင်ရှားပြသည် (decision pakāsenti|0, brahmacariyaṃ pakāsenti|0; H1: one verb with ^4-177 "
         "pakāseti «ထင်ရှားပြတော်မူ»)"),
        ('        f"တရား ဟောကြားခြင်းကို ခွင့်ပြုတော်မူ၏{C} ', '        f"တရား ဟောခြင်းကို ခွင့်ပြုတော်မူ၏{C} ', 1,
         "L04 dhammadesanā (no entry) = the desa- family «ဟော» (decisions desenti|0 / desetabbo|0, part 4 d: «desa- "
         "«ဟော» vs paveda- «ဟောကြား»»), one verb with desetabbo in the same sentence ^4-94"),
        ('        f"ဟောကြားရမည်{END}",', '        f"ဟောရမည်{END}",', 1,
         "L04 desetabbo = ဟောရမည့် (decision desetabbo|0: family desenti / deseti «ဟော»), ^4-94 «dhammo desetabbo»"),
        ("ထိုသူတို့အား ထိုအမှုသည် ကြာမြင့်စွာ {{}} ဖြစ်၏{END}", "ထိုသူတို့အား ထိုအမှုသည် ရှည်လျားသော ကာလပတ်လုံး {{}} ဖြစ်၏{END}", 1,
         "L06 dīgharattaṃ = ရှည်လျားသော ကာလပတ်လုံး (decision dīgharattaṃ|0; H4: ^4-116 / ^4-117 have no ciraṃ, "
         "«ကြာမြင့်စွာ» is ciraṃ's word)"),
        ('UGLY, PAINF, CHEAP = "အဆင်း ညှိုး",', 'UGLY, PAINF, CHEAP = "အဆင်း ဆိုး",', 1,
         "L07 dubbaṇṇo = အဆင်း ဆိုးသော, dubbaṇṇatāya = အဆင်း ဆိုးခြင်း (decisions dubbaṇṇo|0 / dubbaṇṇatāya|0, "
         "pi-2 locked dubbaṇṇe; H9: the cloth ^4-116 = the persons ^4-168 / ^4-184)"),
        ('ACCEPT = (f"{F.SO} အကြင်သူတို့၏{{}} {_REQ}ကို',
         '_REQ = _REQ.replace("ကျောင်းအိပ်ရာနေရာ", "အိပ်ရာ နေရာ")   # rails L08\n'
         'ACCEPT = (f"{F.SO} အကြင်သူတို့၏{{}} {_REQ}ကို', 1,
         "L08 senāsana = အိပ်ရာ နေရာ (decision senāsana|0, pi-2 locked senāsanaṃ; H2: the requisite formula "
         "^4-116 / ^4-117 takes the one word; the pi-2 ^2-929 witness is kept, the pi-4 value derived from it)"),
        ("(f\"“ဤလူ {PUG}သည် {N['pāpamitto']}", "(f\"“ဤ{PUG}သည် {N['pāpamitto']}", 1,
         "L09 purisapuggalo = ပုဂ္ဂိုလ် (decision purisapuggalo|0, pi-2 locked: ^4-124 «ဤပုဂ္ဂိုလ်သည် …»)"),
        ("(f\"“ဤလူ {PUG}သည် {N['kalyāṇamitto']}", "(f\"“ဤ{PUG}သည် {N['kalyāṇamitto']}", 1,
         "L09 purisapuggalo = ပုဂ္ဂိုလ် (decision purisapuggalo|0: ^4-126)"),
        ("မျက်စိဖြင့် မရသေးသော စည်းစိမ်ဥစ္စာကို ရရာ၏{C} ရပြီးသော \"\n               f\"စည်းစိမ်ဥစ္စာကို",
         "မျက်စိဖြင့် မရသေးသော စည်းစိမ်ကို ရရာ၏{C} ရပြီးသော \"\n               f\"စည်းစိမ်ကို", 1,
         "L10 bhogaṃ = စည်းစိမ် (decision bhogaṃ|0, pi-2 locked; = this book's bhoge, bhogakkhandhaṃ): ^4-104 … ^4-106"),
        ("ဘဝင်မြင့်သူ{C} ပေါ့ပျက်သူ{C} စကားများသူ{C} ရှုပ်ပွေစွာ ပြောတတ်သူ{C}",
         "ဘဝင် မြင့်သူ{C} ပေါ့ပျက်သူ{C} စကား များသူ{C} ရှုပ်ပွေစွာ စကားကို ပြောသူ{C}", 1,
         "L11 unnaḷo = ဘဝင် မြင့်သော, mukharo = စကား များသော (termbase; H14 / A4 spacing: = ^4-119), "
         "vikiṇṇavāco = vikiṇṇa ရှုပ်ပွေစွာ + vāco စကားကို ပြောသော (decision vāco|0: ^4-118 reads «… စကားကို ပြောသူ»)"),
        ("ရှုပ်ပွေစွာ မပြောတတ်သူ{C}", "ရှုပ်ပွေစွာ စကားကို မပြောသူ{C}", 1,
         "L11 avikiṇṇavāco = the negative of vikiṇṇavāco «ရှုပ်ပွေစွာ စကားကို ပြောသူ» (decision vāco|0: ^4-119)"),
    ],
    # ============================================================================ chapter 5
    "make_ch5": [
        ('_SURA = "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့ခြင်း၏ အကြောင်း"',
         '_SURA = "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့မှု၏ အကြောင်း"', 1,
         "L25 pamāda = မေ့လျော့မှု (decision pamāda|0, pi-2 locked; kept apart from sammusanatā «မေ့လျော့ခြင်း» "
         "^4-59): surāmerayamajjapamādaṭṭhāyī ^4-132 … ^4-135 (the pi-2 ^2-703 witness is kept; doubt 6)"),
        ('ABHISAMAYA = new("dhammābhisamayo", "တရားကို ထိုးဖောက် သိမြင်ခြင်း")',
         'ABHISAMAYA = new("dhammābhisamayo", "တရားကို ထင်ထင်ရှားရှား သိမြင်ခြင်း")', 1,
         "L12 abhisamayo = ထင်ထင်ရှားရှား သိမြင်ခြင်း (decision abhisamayo|0, puggalassa abhisamayo|0; H7: the "
         "positive of anabhisamayo ^4-60, kept apart from paṭivedho «ထိုးဖောက်၍ သိခြင်း»): ^4-148 … ^4-151"),
        ("ဟောထားသည်၏ အနက်ကို အကျယ်အားဖြင့်", "ဟောထားသည်၏ အနက်အဓိပ္ပာယ်ကို အကျယ်အားဖြင့်", 1,
         "L13 atthe = အနက်အဓိပ္ပာယ် (decision atthe|0: ^4-149)"),
        ("{YASSA} များစွာ ကြားနာသော်လည်း၊", "{YASSA} များစွာ ကြားသော်လည်း၊", 1,
         "L03 suṇato = ကြားသော (decision suṇato|0; H6: one verb «ကြား»): ^4-151"),
        ('WELL_P, BAD_P, WRONG_P, RIGHT_P = "ကောင်းစွာ ကျင့်သော", "ဆိုးစွာ ကျင့်သော", "မှားယွင်းစွာ ကျင့်သော", '
         '"မှန်ကန်စွာ ကျင့်သော"',
         'WELL_P, BAD_P, WRONG_P, RIGHT_P = "ကောင်းစွာ ကျင့်ကြံသော", "ဆိုးစွာ ကျင့်ကြံသော", "မှားယွင်းစွာ ကျင့်ကြံသော", '
         '"မှန်ကန်စွာ ကျင့်ကြံသော"', 1,
         "L15 paṭipanna family = ကျင့်ကြံ (decisions paṭipannānaṃ|0, duppaṭipannānaṃ|0, micchāpaṭipannānaṃ|0, "
         "sammāpaṭipannānaṃ|0; pi-1 / pi-2 locked paṭipannā; H5): ^4-164 / ^4-165"),
        ('Q_GOOD = f"“ကောင်းစွာ ကျင့်သူတို့”ဟူ၍လည်း{C} “မှန်ကန်စွာ ကျင့်သူတို့”ဟူ၍လည်း',
         'Q_GOOD = f"“ကောင်းစွာ ကျင့်ကြံသူတို့”ဟူ၍လည်း{C} “မှန်ကန်စွာ ကျင့်ကြံသူတို့”ဟူ၍လည်း', 1,
         "L15 suppaṭipannā sammāpaṭipannā = ကျင့်ကြံ (decision sammāpaṭipannā|0; H5): ^4-164 / ^4-165"),
        ('Q_BAD = f"“ဆိုးစွာ ကျင့်သူတို့”ဟူ၍လည်း{C} “မှားယွင်းစွာ ကျင့်သူတို့”ဟူ၍လည်း',
         'Q_BAD = f"“ဆိုးစွာ ကျင့်ကြံသူတို့”ဟူ၍လည်း{C} “မှားယွင်းစွာ ကျင့်ကြံသူတို့”ဟူ၍လည်း', 1,
         "L15 duppaṭipannā micchāpaṭipannā = ကျင့်ကြံ (H5): ^4-164 / ^4-165"),
        ("အသက်မွေးရ ခက်ခဲသော၊ \"\n          \"အစာနှင့် အဝတ်ကို ခက်ခဲစွာ ရရသော",
         "အသက်မွေးရ ပင်ပန်းသော၊ \"\n          \"အစာနှင့် အဝတ်ကို ပင်ပန်းစွာ ရရသော", 1,
         "L17 kasira = ပင်ပန်း, kasirena = ပင်ပန်းစွာ (decisions kasira|0 / kasirena|0, pi-2 locked kasirena: "
         "kasiravuttika aligns; kiccha «ခက်ခဲ» stays the other word): ^4-168"),
        ("ပုကွသူ၊ ရောဂါ များသူ၊", "ပုကွသူ၊ အနာရောဂါ များသူ၊", 1,
         "L18 ābādho = အနာရောဂါ (decision ābādho|0, pi-2 locked: bahvābādho «အနာရောဂါ များသူ»): ^4-168"),
        ('f"ထိုသူသည်လည်း ရုပ်ချောသူ၊ ရှုချင်ဖွယ် ဖြစ်သူ၊ {PASADIKA} ဖြစ်သူ၊',
         'f"ထိုသူသည်လည်း အဆင်းလှသူ၊ ရှုချင်ဖွယ် ကောင်းသူ၊ {PASADIKA} ကောင်းသူ၊', 1,
         "L16 abhirūpo = အဆင်းလှသော, dassanīyo = ရှုချင်ဖွယ် ကောင်းသော, pāsādiko = ကြည်ညိုဖွယ် ကောင်းသော (decisions: "
         "the list = abhirūpā dassanīyā pāsādikā ^4-194 / ^4-195), agent «…သူ» as in the rest of the list: ^4-168"),
        ("{SHAVE} ကြမ်းသော သားရေ ⟦1⟧ကို ဝတ်၍ ထောပတ်နှင့် ဆီဖြင့်", "{SHAVE} ကြမ်းသော သမင်သားရေ ⟦1⟧ကို ဝတ်၍ ထောပတ်ကြည်နှင့် ဆီဖြင့်", 1,
         "L19 ajinaṃ = သမင်သားရေ (decision ajinaṃ|0: ^4-176 kharājina takes it too); L20 sappi = ထောပတ်ကြည် (decision "
         "sappi|0; H3: ^4-176 sappitela takes it, navanītaṃ «ထောပတ်» ^4-199 stays apart): ^4-176"),
        ('"မိခင်နှင့် အဆင်းတူသော နွားသငယ်', '"မိခင်နှင့် အဆင်းအရောင် တူသော နွားသငယ်', 1,
         "L21 rūpa = အဆင်းအရောင် in sarūpavaccha (decision rūpa|1, its gloss names sarūpavaccha): ^4-176"),
        ("အနက် ပြည့်စုံသော၊ သဒ္ဒါ ပြည့်စုံသော \"", "အနက်အဓိပ္ပာယ်နှင့် ပြည့်စုံသော၊ စကားလုံးနှင့် ပြည့်စုံသော \"", 1,
         "L13 atthaṃ = အနက်အဓိပ္ပာယ်, L14 byañjanaṃ = စကားလုံး (decisions atthaṃ|0 / byañjanaṃ|0; H1: sātthaṃ "
         "sabyañjanaṃ = ^4-107 … ^4-109 «အနက်အဓိပ္ပာယ်နှင့် ပြည့်စုံသော၊ စကားလုံးနှင့် ပြည့်စုံသော»): ^4-177"),
        ("{REBORN}ဖြစ်စေ ကြားနာ၏{END}", "{REBORN}ဖြစ်စေ ကြား၏{END}", 1,
         "L03 suṇāti = ကြားသည် (decision suṇāti|0; H6: ^4-177 «ကြားနာ» aligns)"),
        ("{SO} ထိုတရားကို ကြားနာ၍ {TATH}", "{SO} ထိုတရားကို ကြား၍ {TATH}", 1,
         "L03 sutvā = ကြား၍ (decision sutvā|0, pi-1 / pi-2 locked; H6): ^4-177"),
        ("ကျဉ်းကျပ်၏၊ မြူမှုန် တက်ရာ လမ်း ဖြစ်၏၊", "ကျဉ်းကျပ်၏၊ ဖုန်လုံး တက်ရာ လမ်း ဖြစ်၏၊", 1,
         "L22 raja = ဖုန်လုံး (decision raja|0: ^4-177 rajāpatho «ဖုန်လုံး တက်ရာ လမ်း»)"),
        ("အိမ်ရာ၌ နေသူသည် စင်စစ် ပြည့်စုံ၍ စင်စစ် စင်ကြယ်သော၊", "အိမ်ရာ၌ နေသူသည် လုံးဝ ပြည့်စုံ၍ လုံးဝ စင်ကြယ်သော၊", 1,
         "L23 ekanta = လုံးဝ (decision ekanta|0: ^4-177 ekantaparipuṇṇaṃ ekantaparisuddhaṃ «လုံးဝ ပြည့်စုံ၍ လုံးဝ "
         "စင်ကြယ်သော»)"),
        ('  f"စဉ်းလဲခြင်း၊ ကောက်ကျစ်သော နည်းလမ်း ⟦0⟧မှ', '  f"ကောက်ကျစ်ခြင်း၊ ကောက်ကျစ်သော နည်းလမ်း ⟦0⟧မှ', 1,
         "L24 nikati = ကောက်ကျစ်ခြင်း (decision nikati|0, pi-2 locked; H8: «စဉ်းလဲ» is sāṭheyya / saṭho's word "
         "^4-51): ^4-179 (sāci «ကောက်ကျစ်သော» is the next item: doubt 5)"),
        ('_DHA = "အနက်ကို သိ၍၊ တရားကို သိ၍ တရားနှင့် လျော်သော တရားကို ကျင့်သူ"',
         '_DHA = "အနက်အဓိပ္ပာယ်ကို သိ၍၊ တရားကို သိ၍ တရားနှင့် လျော်သော တရားကို ကျင့်ကြံသူ"', 1,
         "L13 attha = အနက်အဓိပ္ပာယ် (decision attha|0: atthamaññāya); L15 paṭipanno = ကျင့်ကြံသော (decision "
         "paṭipanno|0; H5: dhammānudhammappaṭipanno «… ကျင့်သူ» aligns): ^4-189"),
        ('new("dhammānudhammappaṭipanno", "တရားနှင့် လျော်သော တရားကို ကျင့်သူ")',
         'new("dhammānudhammappaṭipanno", "တရားနှင့် လျော်သော တရားကို ကျင့်ကြံသူ")', 1,
         "L15 paṭipanno = ကျင့်ကြံသော (H5): the term table entry of ^4-189 / ^4-M-10"),
        # ---- bilingual-review fixes (review/fix-brief.md, review/fix-notes.md): the formulas that repeat
        ('  f"{IDHA} ချီးမွမ်းဖွယ်လည်း ရှိ၏{C} ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏{END}")',
         '  f"{IDHA.removesuffix(\'သည်\')}အဖို့ ချီးမွမ်းဖွယ်လည်း ရှိ၏{C} ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏{END}")', 1,
         "L26 review B2 (^4-166, 4 lines): vaṇṇopi saṃvijjati avaṇṇopi saṃvijjati = the praise / blame that can be "
         "said of a person, not the speaker's own qualities: «ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်အဖို့ ချီးမွမ်းဖွယ်လည်း ရှိ၏၊ "
         "ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏»; every other word kept"),
        ('_BL_T, _PR_T = "ထိုသူ၌ ကဲ့ရဲ့ဖွယ် ရှိသမျှကို", "ထိုသူ၌ ချီးမွမ်းဖွယ် ရှိသမျှကို"',
         '_BL_T, _PR_T = "ထိုတို့အနက် ကဲ့ရဲ့ဖွယ် ရှိသမျှကို", "ထိုတို့အနက် ချီးမွမ်းဖွယ် ရှိသမျှကို"', 1,
         "L26 review B2 (^4-166, 4 lines, 8 clauses): yo (pi) tattha (a)vaṇṇo = «ထိုတို့အနက် … ရှိသမျှကို» (tattha = "
         "«ထိုတို့အနက်», as elsewhere in the book), not «ထိုသူ၌» (the speaker)"),
        ('  f"“ကောင်းသော ကျင့်စဉ်”ဟူ၍လည်း{C} “မှန်ကန်သော ကျင့်စဉ်”ဟူ၍လည်း ပြောဆို၏{END}")',
         '  f"“ကောင်းသော ကျင့်စဉ်”ဟူ၍လည်း{C} “မှန်ကန်သော ကျင့်စဉ်”ဟူ၍လည်း {TRUST}{END}")', 1,
         "L27 review B4 (^4-164 l.103, ^4-165 l.109): pasādaṃ janeti – \"suppaṭipadā\" itipi … has no verb of saying: "
         "the line ends with its own janeti phrase «ကြည်ညိုမှုကို ဖြစ်စေ၏» (termbase pasādaṃ janeti), no added "
         "«ပြောဆို၏»; the bhāsati lines keep «ပြောဆို၏»"),
        ('  f"“ဆိုးသော ကျင့်စဉ်”ဟူ၍လည်း{C} “မှားယွင်းသော ကျင့်စဉ်”ဟူ၍လည်း ပြောဆို၏{END}")',
         '  f"“ဆိုးသော ကျင့်စဉ်”ဟူ၍လည်း{C} “မှားယွင်းသော ကျင့်စဉ်”ဟူ၍လည်း {NOTRUST}{END}")', 1,
         "L27 review B4 (^4-164 l.104, ^4-165 l.108): appasādaṃ janeti – \"duppaṭipadā\" itipi … ends with its own "
         "janeti phrase «မကြည်ညိုမှုကို ဖြစ်စေ၏» (termbase appasādaṃ «မကြည်ညိုမှု» + janeti), no added «ပြောဆို၏»"),
    ],
    # ============================================================================ chapters 6 … 11
    "make_ch6-11": [
        ('put("Idhekacco puggalo yassa puggalassa deti cīvarapiṇḍapāta',
         'CIVARA = CIVARA.replace("ကျောင်းအိပ်ရာနေရာ", "အိပ်ရာ နေရာ")   # rails L08\n'
         'put("Idhekacco puggalo yassa puggalassa deti cīvarapiṇḍapāta', 1,
         "L08 senāsana = အိပ်ရာ နေရာ (decision senāsana|0; H2: the requisite formula ^4-192; the pi-2 ^2-849 "
         "witness is kept, the pi-4 value derived from it)"),
    ],
}
