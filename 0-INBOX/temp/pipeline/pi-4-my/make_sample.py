"""Burmese zero-shot sample of pi-4 (Puggalapaññatti, «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»): preamble, 1-matika,
2-ekakapuggalapannatti.

usage: python3 -I -X utf8 make_sample.py [chapter ...] [--terms] [--misses]
Every line is generated from the Pāli by my4_formulas.translate_line() through the frames and tables of
my4_formulas.py (which reads / checks the FINAL pi-1 / pi-2 / pi-3 Burmese, read only) and the tables of this script:
UNIQUE (sentences of the definitions that occur once), PRED_M (mātikā predicates «atthekacco puggalo …»), LINES_M
(mātikā items no rule builds). A sentence no frame or table entry matches stops the run (my4_formulas.Miss), nothing
is guessed. A chapter is written only when every line passed; on a stop the lines that passed go to
scratch/partial-<chapter> and the failing line is printed. --misses lists every unmatched unit and writes nothing.
--terms (also by default with no chapter argument) rewrites my4-zeroshot-terms.md from the tables.
Model for later chapters: copy this file, put the chapter's unique prose in its own tables, shared sentences and new
names into my4_formulas (never change an existing value without the user's approval); change NAMES_OUT.
"""
import pathlib
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my4_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["preamble.md", "1-matika.md", "2-ekakapuggalapannatti.md"]
C, END, N, W = F.C, F.END, F.NAME, F.W
IDHA, ATTHI, COP, PUG, PUG_PL = F.IDHA, F.ATTHI, F.COP, F.PUGGALA, F.PUG_PL

# ===================================================================================== ch2: unique sentences
UNIQUE = {
    # ^4-1, ^4-2 samaya / asamaya
    "Idhekacco puggalo kālena kālaṃ samayena samayaṃ aṭṭha vimokkhe kāyena phusitvā [phassitvā (sī. pī.)] "
    "viharati, paññāya cassa disvā ekacce āsavā parikkhīṇā honti":
        f"{IDHA} {F.KALA} {F.SAMAYA} {W['vimokkha']}ကို ကိုယ်ဖြင့် ထိ၍ ⟦0⟧ နေ၏{C} {F.ASAVA_SOME}",
    "Idhekacco puggalo na heva kho kālena kālaṃ samayena samayaṃ aṭṭha vimokkhe kāyena phusitvā viharati, "
    "paññāya cassa disvā āsavā parikkhīṇā honti":
        f"{IDHA} {F.KALA} {F.SAMAYA} {W['vimokkha']}ကို ကိုယ်ဖြင့် ထိ၍ နေသည်ကား မဟုတ်{C} {F.ASAVA_ALL}",
    # ^4-9 puthujjano
    "Yassa puggalassa tīṇi saṃyojanāni appahīnāni; na ca tesaṃ dhammānaṃ pahānāya paṭipanno":
        f"အကြင် {PUG}၏ {W['samyojana']}ကို မပယ်ရသေး{C} ထိုသဘောတရားတို့ကို ပယ်ရန် ကျင့်ကြံသူလည်း မဟုတ်",
    # ^4-10 gotrabhū
    "Yesaṃ dhammānaṃ samanantarā ariyadhammassa avakkanti hoti tehi dhammehi samannāgato":
        f"အကြင် သဘောတရားတို့၏ {W['samanantara']} {W['ariya']}တို့၏ တရား သက်ဆင်းခြင်း ဖြစ်၏{C} "
        f"{W['tehi_dhammehi']} အပြည့်အဝ ပြည့်စုံသူ",
    # ^4-11 bhayūparato
    "Satta sekkhā bhayūparatā, ye ca puthujjanā sīlavanto.":
        f"{W['sekkha']} ခုနစ်{F.CL_P}နှင့် သီလ ရှိသော {W['puthujjana']}တို့သည် {N['bhayūparato']} ဖြစ်ကြ၏{END}",
    "Arahā abhayūparato.": f"{W['araha']}သည် {N['abhayūparato']} {COP}{END}",
    # ^4-12, ^4-13 abhabbāgamano / bhabbāgamano (pi-2 ^2-826 / ^2-827)
    "Ye te puggalā kammāvaraṇena samannāgatā, kilesāvaraṇena samannāgatā, vipākāvaraṇena samannāgatā, assaddhā "
    "acchandikā duppaññā eḷā, abhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ":
        "ကံ အဟန့်အတားနှင့် အပြည့်အဝ ပြည့်စုံသော၊ ကိလေသာ အဟန့်အတားနှင့် အပြည့်အဝ ပြည့်စုံသော၊ အကျိုး "
        "အဟန့်အတားနှင့် အပြည့်အဝ ပြည့်စုံသော၊ ယုံကြည်မှု မရှိသော၊ ဆန္ဒ မရှိသော၊ ပညာ နည်းသော၊ နုံအသော၊ "
        f"ကုသိုလ် သဘောတရားတို့၌ မှန်ကန်မှု ဖြစ်သော သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းရန် မထိုက်တန်သော {PUG} ရှိသမျှ",
    "Ye te puggalā na kammāvaraṇena samannāgatā, na kilesāvaraṇena samannāgatā, na vipākāvaraṇena samannāgatā, "
    "saddhā chandikā paññavanto [paññavantā (sī.)] aneḷā, bhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ":
        "ကံ အဟန့်အတားနှင့် မပြည့်စုံသော၊ ကိလေသာ အဟန့်အတားနှင့် မပြည့်စုံသော၊ အကျိုး အဟန့်အတားနှင့် "
        "မပြည့်စုံသော၊ ယုံကြည်မှု ရှိသော၊ ဆန္ဒ ရှိသော၊ ပညာ ရှိသော ⟦0⟧၊ မနုံအသော၊ ကုသိုလ် သဘောတရားတို့၌ "
        f"မှန်ကန်မှု ဖြစ်သော သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းရန် ထိုက်တန်သော {PUG} ရှိသမျှ",
    # ^4-14 niyato
    "Pañca puggalā ānantarikā, ye ca micchādiṭṭhikā niyatā, aṭṭha ca ariyapuggalā niyatā.":
        f"ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော {PUG} ငါး{F.CL_P}{C} မှားယွင်းသော အယူ ရှိ၍ "
        f"{N['niyato']}တို့နှင့် {W['ariya']} {PUG} ရှစ်{F.CL_P}တို့သည် {N['niyato']} ဖြစ်ကြ၏{END}",
    "Avasesā puggalā aniyatā.": f"ကြွင်းကျန်သော {PUG_PL}သည် {N['aniyato']} ဖြစ်ကြ၏{END}",
    # ^4-15 paṭipannako
    "Cattāro maggasamaṅgino puggalā paṭipannakā, cattāro phalasamaṅgino puggalā phale ṭhitā.":
        f"{F.GROUP['maggasamaṅgino']} {PUG} လေး{F.CL_P}တို့သည် {N['paṭipannako']} ဖြစ်ကြ၏{C} "
        f"{F.GROUP['phalasamaṅgino']} {PUG} လေး{F.CL_P}တို့သည် {N['phaleṭhito']} ဖြစ်ကြ၏{END}",
    # ^4-16 samasīsī
    "Yassa puggalassa apubbaṃ acarimaṃ āsavapariyādānañca hoti jīvitapariyādānañca":
        f"အကြင် {PUG}၏ {W['asava']}တို့ ကုန်ဆုံးခြင်းနှင့် အသက် ကုန်ဆုံးခြင်းသည် {W['apubbam_acarimam']} ဖြစ်၏",
    # ^4-17 ṭhitakappī
    "Ayañca puggalo sotāpattiphalasacchikiriyāya paṭipanno assa, kappassa ca uḍḍayhanavelā assa, neva tāva "
    "kappo uḍḍayheyya yāvāyaṃ puggalo na sotāpattiphalaṃ sacchikaroti.":
        f"ဤ{PUG}သည် {N['sotāpattiphalasacchikiriyāya paṭipanno']} ဖြစ်ငြားအံ့၊ ကမ္ဘာ မီးလောင်ရမည့် အချိန်လည်း "
        f"ရောက်ငြားအံ့၊ ဤ{PUG}သည် {W['sotapattiphala']}ကို မျက်မှောက် မပြုသေးသမျှ ကာလပတ်လုံး ကမ္ဘာသည် "
        f"မီး မလောင်သေးရာ{END}",
    "Sabbepi maggasamaṅgino puggalā ṭhitakappino.":
        f"{F.GROUP['maggasamaṅgino']} {PUG} အားလုံးသည် {N['ṭhitakappī']} ဖြစ်ကြ၏{END}",
    # ^4-18 ariyo, ^4-19 sekkho
    "Aṭṭha ariyapuggalā ariyā.": f"{W['ariya']} {PUG} ရှစ်{F.CL_P}တို့သည် {N['ariyo']} ဖြစ်ကြ၏{END}",
    "Avasesā puggalā anariyā.": f"ကြွင်းကျန်သော {PUG_PL}သည် {N['anariyo']} ဖြစ်ကြ၏{END}",
    'Cattāro maggasamaṅgino tayo phalasamaṅgino puggalā "sekkhā".':
        f"{F.GROUP['maggasamaṅgino']} {PUG} လေး{F.CL_P}၊ {F.GROUP['phalasamaṅgino']} {PUG} သုံး{F.CL_P}တို့သည် "
        f"“{N['sekkho']}” ဖြစ်ကြ၏{END}",
    "Arahā asekkho.": f"{W['araha']}သည် {N['asekkho']} {COP}{END}",
    "Avasesā puggalā nevasekkhanāsekkhā.": f"ကြွင်းကျန်သော {PUG_PL}သည် {N['nevasekkhanāsekkho']} ဖြစ်ကြ၏{END}",
    # ^4-20, ^4-21
    'Tīhi vijjāhi samannāgato puggalo "tevijjo".':
        f"{W['vijja']} သုံး{F.CL}နှင့် အပြည့်အဝ ပြည့်စုံသော {PUG}သည် “{N['tevijjo']}” ဖြစ်သည်{END}",
    'Chahi abhiññāhi samannāgato puggalo "chaḷabhiñño".':
        f"{W['abhinna6']}နှင့် အပြည့်အဝ ပြည့်စုံသော {PUG}သည် “{N['chaḷabhiñño']}” ဖြစ်သည်{END}",
    # ^4-22, ^4-23 the Buddhas
    "Idhekacco puggalo pubbe ananussutesu dhammesu sāmaṃ saccāni abhisambujjhati; tattha ca sabbaññutaṃ "
    "pāpuṇāti, balesu ca vasībhāvaṃ":
        f"{IDHA} {F.ANANUSSUTA} {F.ABHISAM}{C} ထို၌လည်း {F.SABBANNU} ရောက်၏{C} {F.BALA_VASI}လည်း ရောက်၏",
    "Idhekacco puggalo pubbe ananussutesu dhammesu sāmaṃ saccāni abhisambujjhati; na ca tattha sabbaññutaṃ "
    "pāpuṇāti, na ca balesu vasībhāvaṃ":
        f"{IDHA} {F.ANANUSSUTA} {F.ABHISAM}{C} ထို၌ {F.SABBANNU} မရောက်{C} {F.BALA_VASI}လည်း မရောက်",
    # ^4-29, ^4-30
    "Yassa puggalassa sotāpattiphalasacchikiriyāya paṭipannassa paññindriyaṃ adhimattaṃ hoti, paññāvāhiṃ "
    "paññāpubbaṅgamaṃ ariyamaggaṃ bhāveti":
        f"{W['sotapattiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော အကြင် {PUG}၏ ပညာ၏ စွမ်းရည်သည် လွန်ကဲ၏{C} "
        f"ထိုသူသည် ပညာက ဆောင်သော၊ ပညာ ရှေ့သွား ရှိသော {W['ariyamagga']}ကို ပွားများ၏",
    "Sotāpattiphalasacchikiriyāya paṭipanno puggalo dhammānusārī phale ṭhito diṭṭhippatto.":
        f"{W['sotapattiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော {PUG}သည် {N['dhammānusārī']} {COP}{C} "
        f"{W['phala']}၌ တည်သောအခါ {N['diṭṭhippatto']} {COP}{END}",
    "Yassa puggalassa sotāpattiphalasacchikiriyāya paṭipannassa saddhindriyaṃ adhimattaṃ hoti, saddhāvāhiṃ "
    "saddhāpubbaṅgamaṃ ariyamaggaṃ bhāveti":
        f"{W['sotapattiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော အကြင် {PUG}၏ ယုံကြည်မှု၏ စွမ်းရည်သည် လွန်ကဲ၏{C} "
        f"ထိုသူသည် ယုံကြည်မှုက ဆောင်သော၊ ယုံကြည်မှု ရှေ့သွား ရှိသော {W['ariyamagga']}ကို ပွားများ၏",
    "Sotāpattiphalasacchikiriyāya paṭipanno puggalo saddhānusārī phale ṭhito saddhāvimutto.":
        f"{W['sotapattiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော {PUG}သည် {N['saddhānusārī']} {COP}{C} "
        f"{W['phala']}၌ တည်သောအခါ {N['saddhāvimutto']} {COP}{END}",
    # ^4-31 … ^4-34 stream-enterers, once-returner
    "So sattakkhattuṃ deve ca mānuse ca sandhāvitvā saṃsaritvā dukkhassantaṃ karoti":
        f"ထိုသူသည် {W['deva']}တို့၌လည်း လူတို့၌လည်း ခုနစ်ကြိမ် {F._SAMS} {F._END_DUKKHA}",
    "So dve vā tīṇi vā kulāni sandhāvitvā saṃsaritvā dukkhassantaṃ karoti":
        f"ထိုသူသည် {W['kulani']} နှစ်မျိုးဖြစ်စေ၊ သုံးမျိုးဖြစ်စေ {F._SAMS} {F._END_DUKKHA}",
    "So ekaṃyeva mānusakaṃ bhavaṃ nibbattetvā dukkhassantaṃ karoti":
        f"ထိုသူသည် လူ့ ဘဝ တစ်ခုတည်းကိုသာ {W['nibbatteti']}၍ {F._END_DUKKHA}",
    "Idhekacco puggalo tiṇṇaṃ saṃyojanānaṃ parikkhayā rāgadosamohānaṃ tanuttā sakadāgāmī hoti, sakideva imaṃ "
    "lokaṃ āgantvā dukkhassantaṃ karoti":
        f"{IDHA} {W['samyojana']} {F._PARIKKHAYA}၊ ရာဂ၊ ဒေါသ၊ မောဟတို့ ပါးလျခြင်းကြောင့် {N['sakadāgāmī']} {COP}{C} "
        f"ဤလောကသို့ တစ်ကြိမ်သာ ပြန်လာ၍ {F._END_DUKKHA}",
    # ^4-36 … ^4-40 non-returners
    "So upapannaṃ vā samanantarā appattaṃ vā vemajjhaṃ āyuppamāṇaṃ ariyamaggaṃ sañjaneti upariṭṭhimānaṃ "
    "saṃyojanānaṃ pahānāya":
        f"ထိုသူသည် ပေါ်လာပြီး {W['samanantara']}ဖြစ်စေ၊ {W['ayuppamana']}၏ အလယ်သို့ မရောက်မီဖြစ်စေ "
        f"{F.UPARI_PAHANA}",
    "So atikkamitvā vemajjhaṃ āyuppamāṇaṃ upahacca vā kālakiriyaṃ [kālaṃ kiriyaṃ (ka.)] ariyamaggaṃ sañjaneti "
    "upariṭṭhimānaṃ saṃyojanānaṃ pahānāya":
        f"ထိုသူသည် {W['ayuppamana']}၏ အလယ်ကို ကျော်လွန်၍ဖြစ်စေ၊ {W['kalakiriya']}နှင့် နီးကပ်၍ဖြစ်စေ ⟦0⟧ "
        f"{F.UPARI_PAHANA}",
    "So asaṅkhārena ariyamaggaṃ sañjaneti upariṭṭhimānaṃ saṃyojanānaṃ pahānāya":
        f"ထိုသူသည် တိုက်တွန်းမှု မရှိဘဲ {F.UPARI_PAHANA}",
    "So sasaṅkhārena ariyamaggaṃ sañjaneti upariṭṭhimānaṃ saṃyojanānaṃ pahānāya":
        f"ထိုသူသည် {W['sasankharena']} {F.UPARI_PAHANA}",
    "So avihā cuto atappaṃ gacchati, atappā cuto sudassaṃ gacchati, sudassā cuto sudassiṃ gacchati, sudassiyā "
    "cuto akaniṭṭhaṃ gacchati; akaniṭṭhe ariyamaggaṃ sañjaneti upariṭṭhimānaṃ saṃyojanānaṃ pahānāya":
        "ထိုသူသည် " + f"{C} ".join(f"{a} ဘုံမှ သေ၍ {b} ဘုံသို့ သွား၏" for a, b in (
            ("အဝိဟာ", "အတပ္ပါ"), ("အတပ္ပါ", "သုဒဿာ"), ("သုဒဿာ", "သုဒဿီ"), ("သုဒဿီ", "အကနိဋ္ဌ"))) +
        f"{C} အကနိဋ္ဌ ဘုံ၌ {F.UPARI_PAHANA}",
    # ^4-41 … ^4-44 the four paths and fruits
    "Tiṇṇaṃ saṃyojanānaṃ pahānāya paṭipanno puggalo sotāpattiphalasacchikiriyāya paṭipanno.":
        f"{W['samyojana']}ကို ပယ်ရန် ကျင့်ကြံသော {PUG}သည် {N['sotāpattiphalasacchikiriyāya paṭipanno']} {COP}{END}",
    "Yassa puggalassa tīṇi saṃyojanāni pahīnāni":
        f"အကြင် {PUG}၏ {W['samyojana']}ကို ပယ်ပြီး ဖြစ်၏",
    "Kāmarāgabyāpādānaṃ tanubhāvāya paṭipanno puggalo sakadāgāmiphalasacchikiriyāya paṭipanno.":
        f"{W['kamaraga']}နှင့် ဖျက်ဆီးလိုစိတ်တို့ {W['tanubhavaya']} ကျင့်ကြံသော {PUG}သည် "
        f"{N['sakadāgāmiphalasacchikiriyāya paṭipanno']} {COP}{END}",
    "Yassa puggalassa kāmarāgabyāpādā tanubhūtā":
        f"အကြင် {PUG}၏ {W['kamaraga']}နှင့် ဖျက်ဆီးလိုစိတ်တို့ ပါးလျပြီ",
    "Kāmarāgabyāpādānaṃ anavasesappahānāya paṭipanno puggalo anāgāmiphalasacchikiriyāya paṭipanno.":
        f"{W['kamaraga']}နှင့် ဖျက်ဆီးလိုစိတ်တို့ကို အကြွင်းမဲ့ ပယ်ရန် ကျင့်ကြံသော {PUG}သည် "
        f"{N['anāgāmiphalasacchikiriyāya paṭipanno']} {COP}{END}",
    "Yassa puggalassa kāmarāgabyāpādā anavasesā pahīnā":
        f"အကြင် {PUG}၏ {W['kamaraga']}နှင့် ဖျက်ဆီးလိုစိတ်တို့ကို အကြွင်းမဲ့ ပယ်ပြီး ဖြစ်၏",
    "Rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya paṭipanno puggalo arahattaphalasacchikiriyāya "
    "paṭipanno.":
        f"{F.W['rupa_raga']}တို့ကို အကြွင်းမဲ့ ပယ်ရန် ကျင့်ကြံသော {PUG}သည် "
        f"{N['arahattaphalasacchikiriyāya paṭipanno']} {COP}{END}",
    "Yassa puggalassa rūparāgo arūparāgo māno uddhaccaṃ avijjā anavasesā pahīnā":
        f"အကြင် {PUG}၏ {F.W['rupa_raga']}တို့ကို အကြွင်းမဲ့ ပယ်ပြီး ဖြစ်၏",
}

# ===================================================================================== 1-matika: predicates and lines
CL, CLP, G, GN, NUM = F.CL, F.CL_P, F.GROUP, F.GROUP_NOUN, F.NUM_MY
PRED_M = {}      # «atthekacco puggalo PRED» (mātikā) whose Burmese is not «NAME ဖြစ်၏»; «⟦n⟧» = n-th bracket
# ---- tika (13), (15): names with a variant bracket inside
PRED_M["sakkatvā garuṃ katvā [garukatvā (sī.)] sevitabbo bhajitabbo payirupāsitabbo"] = (
    f"ရိုသေ၍ လေးစားကာ ⟦0⟧ {F.SEV3}သူ {COP}")
PRED_M["sīlesu paripūrakārī [paripūrīkārī (syā.)], samādhismiṃ mattaso kārī, paññāya mattaso kārī"] = (
    f"{F.SILA_FULL} ⟦0⟧၍ သမာဓိကို {F.PART}{C} ပညာကို {F.PART}သူ {COP}")
# ---- catukka (15), (16): praise and blame, trust
ANAN, ANU = "မစုံစမ်း မစိစစ်ဘဲ", "စုံစမ်း စိစစ်၍"            # ananuvicca apariyogāhetvā / anuvicca pariyogāhetvā
PR_W, BL_W = "ချီးမွမ်းထိုက်သူကို", "ကဲ့ရဲ့ထိုက်သူကို"            # vaṇṇārahassa / avaṇṇārahassa
PR, BL = "ချီးမွမ်း ပြောဆိုသူ", "ကဲ့ရဲ့ ပြောဆိုသူ"                # vaṇṇaṃ bhāsitā / avaṇṇaṃ bhāsitā
TR_W, NTR_W = "ကြည်ညိုထိုက်သော အရာ၌", "မကြည်ညိုထိုက်သော အရာ၌"   # pasādanīye / appasādanīye ṭhāne
TR, NTR = "ကြည်ညိုမှုကို ပြသသူ", "မကြည်ညိုမှုကို ပြသသူ"          # pasādaṃ / appasādaṃ upadaṃsitā
for _pa, _ma in (("ananuvicca apariyogāhetvā", ANAN), ("anuvicca pariyogāhetvā", ANU)):
    PRED_M[f"{_pa} avaṇṇārahassa vaṇṇaṃ bhāsitā hoti"] = f"{_ma} {BL_W} {PR} {COP}"
    PRED_M[f"{_pa} vaṇṇārahassa avaṇṇaṃ bhāsitā hoti"] = f"{_ma} {PR_W} {BL} {COP}"
    PRED_M[f"{_pa} appasādanīye ṭhāne pasādaṃ upadaṃsitā hoti"] = f"{_ma} {NTR_W} {TR} {COP}"
    PRED_M[f"{_pa} pasādanīye ṭhāne appasādaṃ upadaṃsitā hoti"] = f"{_ma} {TR_W} {NTR} {COP}"
    PRED_M[f"{_pa} avaṇṇārahassa avaṇṇaṃ bhāsitā hoti"] = f"{_ma} {BL_W} {BL} {COP}"
    PRED_M[f"{_pa} vaṇṇārahassa vaṇṇaṃ bhāsitā hoti"] = f"{_ma} {PR_W} {PR} {COP}"
    PRED_M[f"{_pa} appasādanīye ṭhāne appasādaṃ upadaṃsitā hoti"] = f"{_ma} {NTR_W} {NTR} {COP}"
    PRED_M[f"{_pa} pasādanīye ṭhāne pasādaṃ upadaṃsitā hoti"] = f"{_ma} {TR_W} {TR} {COP}"
# ---- catukka (17): at the right time (bhūtaṃ tacchaṃ kālena)
BTK = f"အမှန်အတိုင်း{C} ဟုတ်တိုင်း{C} အချိန်အခါနှင့် လျော်စွာ"
_BT = "bhūtaṃ tacchaṃ kālena"
PRED_M[f"avaṇṇārahassa avaṇṇaṃ bhāsitā hoti {_BT}, no ca kho vaṇṇārahassa vaṇṇaṃ bhāsitā hoti {_BT}"] = (
    f"{BL_W} {BTK} {BL} {COP}{C} သို့သော် {PR_W} {BTK} {PR}ကား မဟုတ်")
PRED_M[f"vaṇṇārahassa vaṇṇaṃ bhāsitā hoti {_BT}, no ca kho avaṇṇārahassa avaṇṇaṃ bhāsitā hoti {_BT}"] = (
    f"{PR_W} {BTK} {PR} {COP}{C} သို့သော် {BL_W} {BTK} {BL}ကား မဟုတ်")
PRED_M[f"avaṇṇārahassa ca avaṇṇaṃ bhāsitā hoti {_BT}; vaṇṇārahassa ca vaṇṇaṃ bhāsitā hoti {_BT}"] = (
    f"{BL_W}လည်း {BTK} {BL} {COP}{C} {PR_W}လည်း {BTK} {PR} {COP}")
PRED_M[f"neva avaṇṇārahassa avaṇṇaṃ bhāsitā hoti {_BT}, no ca vaṇṇārahassa vaṇṇaṃ bhāsitā hoti {_BT}"] = (
    f"{BL_W} {BTK} {BL}လည်း မဟုတ်{C} {PR_W} {BTK} {PR}လည်း မဟုတ်")
# ---- catukka (24): one's own good and others' good
OWN, OTH, PAT = "မိမိ၏ အကျိုးအတွက်", "သူတစ်ပါး၏ အကျိုးအတွက်", "ကျင့်ကြံသူ"
PRED_M["attahitāya paṭipanno hoti, no parahitāya"] = f"{OWN} {PAT} {COP}{C} {OTH} မဟုတ်"
PRED_M["parahitāya paṭipanno hoti, no attahitāya"] = f"{OTH} {PAT} {COP}{C} {OWN} မဟုတ်"
PRED_M["attahitāya ceva paṭipanno hoti parahitāya ca"] = f"{OWN}လည်း {OTH}လည်း {PAT} {COP}"
PRED_M["neva attahitāya paṭipanno hoti no parahitāya"] = f"{OWN}လည်း {PAT} မဟုတ်{C} {OTH}လည်း မဟုတ်"
# ---- catukka (25): tormenting oneself and others
AT, ATP = "မိမိကိုယ်ကို ပူပန်စေသူ", "မိမိကိုယ်ကို ပူပန်စေခြင်းကို အားထုတ်သူ"
PT, PTP = "သူတစ်ပါးကို ပူပန်စေသူ", "သူတစ်ပါးကို ပူပန်စေခြင်းကို အားထုတ်သူ"
PRED_M["attantapo hoti attaparitāpanānuyogamanuyutto"] = f"{AT} {COP}{C} {ATP} {COP}"
PRED_M["parantapo hoti paraparitāpanānuyogamanuyutto"] = f"{PT} {COP}{C} {PTP} {COP}"
PRED_M["attantapo ca hoti attaparitāpanānuyogamanuyutto, parantapo ca paraparitāpanānuyogamanuyutto"] = (
    f"{AT}လည်း {COP}{C} {ATP} {COP}{C} {PT}လည်း {COP}{C} {PTP} {COP}")
PRED_M["neva attantapo hoti na attaparitāpanānuyogamanuyutto, na parantapo na paraparitāpanānuyogamanuyutto. "
       "So anattantapo aparantapo diṭṭheva dhamme nicchāto nibbuto sītībhūto [sītibhūto (sī. ka.)] "
       "sukhappaṭisaṃvedī brahmabhūtena attanā viharati"] = (
    f"{AT}လည်း မဟုတ်{C} {ATP}လည်း မဟုတ်{C} {PT}လည်း မဟုတ်{C} {PTP}လည်း မဟုတ်{END} ထိုသူသည် မိမိကိုယ်ကို "
    f"မပူပန်စေ၊ သူတစ်ပါးကို မပူပန်စေဘဲ {W['ditthe_dhamme']} ဆာလောင်မှု ကင်း၍ ငြိမ်းအေး၍ အေးမြသူ ⟦0⟧ ဖြစ်ကာ "
    f"သာယာမှုကို ခံစား၍ မြင့်မြတ်သူ ဖြစ်ပြီးသော မိမိကိုယ်ဖြင့် နေ၏")
# ---- catukka (27): calm and insight
CS, VP = "မိမိ၌ စိတ်ငြိမ်သက်ခြင်းကို", "လွန်ကဲသော ပညာဖြင့် သဘောတရားတို့ကို ထိုးထွင်းသိမြင်ခြင်းကို"
GOT = "ရရှိသူ"
PRED_M["lābhī hoti ajjhattaṃ cetosamathassa, na lābhī adhipaññādhammavipassanāya"] = (
    f"{CS} {GOT} {COP}{C} {VP} {GOT} မဟုတ်")
PRED_M["lābhī hoti adhipaññādhammavipassanāya, na lābhī ajjhattaṃ cetosamathassa"] = (
    f"{VP} {GOT} {COP}{C} {CS} {GOT} မဟုတ်")
PRED_M["lābhī ceva hoti ajjhattaṃ cetosamathassa, lābhī ca adhipaññādhammavipassanāya"] = (
    f"{CS}လည်း {GOT} {COP}{C} {VP}လည်း {GOT} {COP}")
PRED_M["neva lābhī hoti ajjhattaṃ cetosamathassa, na lābhī adhipaññādhammavipassanāya"] = (
    f"{CS}လည်း {GOT} မဟုတ်{C} {VP}လည်း {GOT} မဟုတ်")
# ---- pañcaka (1): wrongdoing, remorse, the liberation not known / known
_YATTHA = ("ထိုသူ၏ ဖြစ်ပေါ်ပြီးသော ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ အကြွင်းအကျန် မရှိဘဲ ချုပ်ငြိမ်းရာ ဖြစ်သော "
           f"ထို{W['cetovimuttim']}ကိုလည်း {W['yathabhutam_pajanati']}")
_NOKNOW, _KNOW = _YATTHA.replace(" ကွဲပြားစွာ သိ", " ကွဲပြားစွာ မသိ"), _YATTHA + "၏"
_REST = ("tañca cetovimuttiṃ paññāvimuttiṃ yathābhūtaṃ {}, yatthassa te uppannā pāpakā akusalā dhammā aparisesā "
         "nirujjhanti")
WRONG, NOWRONG = "မှားယွင်းစွာ ပြုမူ၏", "မှားယွင်းစွာ မပြုမူ"           # ārabhati / nārabhati
REM = F.VIPPATISARI                                               # vippaṭisārī (B5: pi-1 vippaṭisāro «နောင်တ ရခြင်း»)
PRED_M["ārabhati [ārambhati (sī. syā.)] ca vippaṭisārī ca hoti, " + _REST.format("nappajānāti")] = (
    f"မှားယွင်းစွာလည်း ပြုမူ၏ ⟦0⟧{C} {REM}လည်း {COP}{C} {_NOKNOW}")
PRED_M["ārabhati na vippaṭisārī ca hoti, " + _REST.format("nappajānāti")] = (
    f"{WRONG}{C} {REM}ကား မဟုတ်{C} {_NOKNOW}")
PRED_M["nārabhati vippaṭisārī ca hoti, " + _REST.format("nappajānāti")] = (
    f"{NOWRONG}{C} {REM}ကား {COP}{C} {_NOKNOW}")
PRED_M["nārabhati na vippaṭisārī hoti, " + _REST.format("nappajānāti")] = (
    f"{NOWRONG}{C} {REM}လည်း မဟုတ်{C} {_NOKNOW}")
PRED_M["nārabhati na vippaṭisārī hoti, " + _REST.format("pajānāti")] = (
    f"{NOWRONG}{C} {REM}လည်း မဟုတ်{C} {_KNOW}")
# ---- chakka (1): the six (two Buddhas, the disciples)
_AN = "pubbe ananussutesu dhammesu sāmaṃ saccāni"
_DUK = "ဒုက္ခ၏ အဆုံးကို ပြုသူ"                                    # dukkhassantakaro
_SAVAKA = "တပည့် ပါရမီ"                                            # sāvakapāramī (sāvaka = «တပည့်», pi-2)
PRED_M[f"{_AN} abhisambujjhati, tattha ca sabbaññutaṃ pāpuṇāti balesu [phalesu (pī.)] ca vasībhāvaṃ"] = (
    f"{F.ANANUSSUTA} {F.ABHISAM}{C} ထို၌လည်း {F.SABBANNU} ရောက်၏{C} စွမ်းအားတို့၌ ⟦0⟧ နိုင်နင်းခြင်းသို့လည်း "
    f"ရောက်၏")
PRED_M[f"{_AN} abhisambujjhati, na ca tattha sabbaññutaṃ pāpuṇāti na ca balesu vasībhāvaṃ"] = (
    f"{F.ANANUSSUTA} {F.ABHISAM}{C} ထို၌ {F.SABBANNU} မရောက်{C} {F.BALA_VASI}လည်း မရောက်")
PRED_M[f"{_AN} anabhisambujjhati, diṭṭhe ceva dhamme dukkhassantakaro hoti sāvakapāramiñca pāpuṇāti"] = (
    f"{F.ANANUSSUTA} {F.ANABHISAM}{C} {W['ditthe_dhamme']} {_DUK} {COP}{C} {_SAVAKA}သို့လည်း ရောက်၏")
PRED_M[f"{_AN} anabhisambujjhati, diṭṭheva dhamme dukkhassantakaro hoti, na ca sāvakapāramiṃ pāpuṇāti"] = (
    f"{F.ANANUSSUTA} {F.ANABHISAM}{C} {W['ditthe_dhamme']} {_DUK} {COP}{C} {_SAVAKA}သို့ကား မရောက်")
PRED_M[f"{_AN} anabhisambujjhati, na ca diṭṭheva dhamme dukkhassantakaro hoti, anāgāmī hoti anāgantā "
       "[anāgantvā (syā. ka.) a. ni. 4.171] itthattaṃ"] = (
    f"{F.ANANUSSUTA} {F.ANABHISAM}{C} {W['ditthe_dhamme']} {_DUK}လည်း မဟုတ်{C} {N['anāgāmī']} {COP}{C} "
    f"ဤဘဝသို့ ပြန်မလာမည့်သူ ⟦0⟧ {COP}")
PRED_M[f"{_AN} anabhisambujjhati, na ca diṭṭheva dhamme dukkhassantakaro hoti, āgāmī "
       "[sotāpannasakadāgāmī (syā. ka.)] hoti āgantā itthattaṃ"] = (
    f"{F.ANANUSSUTA} {F.ANABHISAM}{C} {W['ditthe_dhamme']} {_DUK}လည်း မဟုတ်{C} ပြန်လာသူ ⟦0⟧ {COP}{C} "
    f"ဤဘဝသို့ ပြန်လာမည့်သူ {COP}")

LINES_M = {}     # mātikā items no rule builds (whole item text after «(n) »); «⟦n⟧» = n-th bracket
LINES_M["Cha paññattiyo – khandhapaññatti, āyatanapaññatti, dhātupaññatti, saccapaññatti, indriyapaññatti, "
        "puggalapaññattīti."] = (
    f"{F.PANNATTI} ခြောက်{CL} – " + f"{C} ".join(F.pannatti_my(s) for s in
                                               ("khandha", "āyatana", "dhātu", "sacca", "indriya", "puggala")) + END)
LINES_M["Arahattaphalasacchikiriyāya [arahattāya (sī.)] paṭipanno"] = (
    f"{W['arahattaphala']}ကို မျက်မှောက်ပြုရန် ⟦0⟧ ကျင့်ကြံသူ")
LINES_M["Makkhī ca, paḷāsī [palāsī (syā. ka.)] ca."] = f"{N['makkhī']}နှင့် {N['paḷāsī']} ⟦0⟧{END}"
LINES_M["Dvinnaṃ puggalānaṃ āsavā vaḍḍhanti."] = (
    f"{PUG} နှစ်{CLP}တို့၏ {W['asava']}တို့သည် တိုးပွားကုန်၏{END}")
LINES_M["Dvinnaṃ puggalānaṃ āsavā na vaḍḍhanti."] = (
    f"{PUG} နှစ်{CLP}တို့၏ {W['asava']}တို့သည် မတိုးပွားကုန်{END}")
LINES_M["Tayo satthāro."] = f"ဆရာ သုံး{CLP}{END}"
LINES_M["Aparepi tayo satthāro."] = f"နောက်ထပ် ဆရာ သုံး{CLP}{END}"
LINES_M["Cattāro balībaddūpamā [balibaddūpamā (sī.)] puggalā."] = f"{G['balībaddūpamā']} ⟦0⟧ {PUG} လေး{CLP}{END}"
LINES_M["Anusotagāmī puggalo, paṭisotagāmī puggalo, ṭhitatto puggalo, tiṇṇo pāraṅgato [pāragato (sī. syā.)] "
        "thale tiṭṭhati brāhmaṇo."] = (
    f"{F.adj(N['anusotagāmī'])}{C} {F.adj(N['paṭisotagāmī'])}{C} {F.adj(N['ṭhitatto'])}{C} "
    f"ကူးမြောက်ပြီး ကမ်းတစ်ဖက်သို့ ရောက်၍ ⟦0⟧ ကုန်းပေါ်၌ ရပ်တည်နေသော ပုဏ္ဏား{END}")
assert N["tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo"] == "ကူးမြောက်ပြီး ကမ်းတစ်ဖက်သို့ ရောက်၍ ကုန်းပေါ်၌ ရပ်တည်နေသော ပုဏ္ဏား"
LINES_M["Datvā avajānāti, saṃvāsena avajānāti, ādheyyamukho hoti, lolo hoti, mando momūho hoti."] = (
    f"{N['datvā avajānāti'][:-2]}၏{C} {N['saṃvāsena avajānāti'][:-2]}၏{C} {N['ādheyyamukho']} {COP}{C} "
    f"{N['lolo']} {COP}{C} {N['mando momūho']} {COP}{END}")
LINES_M["Satta udakūpamā puggalā. Sakiṃ nimuggo nimuggova hoti, ummujjitvā nimujjati, ummujjitvā ṭhito hoti, "
        "ummujjitvā vipassati viloketi, ummujjitvā patarati, ummujjitvā paṭigādhappatto hoti, ummujjitvā tiṇṇo hoti "
        "pāraṅgato thale tiṭṭhati brāhmaṇo."] = (
    f"{G['udakūpamā']} {PUG} ခုနစ်{CLP}{END} တစ်ကြိမ် နစ်လျှင် နစ်မြဲ နစ်နေသူ {COP}{C} ပေါ်လာပြီး ပြန်နစ်၏{C} "
    f"ပေါ်လာပြီး တည်နေသူ {COP}{C} ပေါ်လာပြီး {F.VIPASSATI}၏{C} ပေါ်လာပြီး ကူးခတ်၏{C} "
    f"ပေါ်လာပြီး ခြေကုပ်ရာသို့ ရောက်သူ {COP}{C} ပေါ်လာပြီး "
    f"{N['tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo']} {COP}{END}")
LINES_M["Cattāro maggasamaṅgino, cattāro phalasamaṅgino puggalā."] = (
    f"{N['maggasamaṅgī']} လေး{CLP}{C} {G['phalasamaṅgino']} {PUG} လေး{CLP}{END}")
LINES_M["Pañcannaṃ idha niṭṭhā, pañcannaṃ idha vihāya niṭṭhā."] = (
    f"ငါး{CLP}တို့၏ ပြီးမြောက်ခြင်းသည် ဤလောက၌ ဖြစ်၏{C} ငါး{CLP}တို့၏ ပြီးမြောက်ခြင်းသည် ဤလောကကို "
    f"စွန့်ခွာပြီးမှ ဖြစ်၏{END}")

# ===================================================================================== install the tables
F._UNIQUE_KEYS = set(UNIQUE)
for _t, _d in ((F.SENT, UNIQUE), (F.PRED, PRED_M), (F.LINES, LINES_M)):
    for _k, _v in _d.items():
        if _k in _t and _t[_k] != _v:
            raise SystemExit("table conflict: " + _k[:80])
        _t[_k] = unicodedata.normalize("NFC", _v)


# ===================================================================================== generator
def bids(lines):
    bid_of, cur = {}, []
    for i, line in enumerate(lines):          # block ID of each line = the ID that closes its segment
        if line.strip():
            cur.append(i)
            m = F.ID_RE.search(line)
            if m:
                for j in cur:
                    bid_of[j] = m.group(1)
                cur = []
    return bid_of


def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name, misses=None):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    bid_of = bids(lines)
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(F.translate_line(line, bid_of.get(i)))
        except F.Miss as e:
            if misses is not None:
                misses.append(f"{name}:{i + 1}: {e}")
                done.append("")
                continue
            part = HERE / "scratch" / ("partial-" + name)
            part.parent.mkdir(exist_ok=True)
            part.write_text("\n".join(done) + "\n", encoding="utf-8")
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:200]}\n  ({len(done)} lines kept in {part})")
            return False
    if misses is not None:
        return not misses
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    names = args or NAMES_OUT
    if "--misses" in sys.argv:
        ms = []
        for n in names:
            chapter(n, ms)
        print("\n".join(ms) or "no misses")
        print(f"{len(ms)} misses")
        sys.exit(0)
    OUT.mkdir(parents=True, exist_ok=True)
    ok = True
    for n in names:
        ok = chapter(n) and ok
    if ok and ("--terms" in sys.argv or not args):
        import terms_my4
        terms_my4.write_terms(F, HERE / "my4-zeroshot-terms.md")
    sys.exit(0 if ok else 1)
