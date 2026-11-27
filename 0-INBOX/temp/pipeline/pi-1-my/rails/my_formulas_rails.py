"""pi-1 Burmese RAILS layer: the systematic termbase differences of the harmonised zero-shot, as in-memory source
patches of my_formulas.py and of the zero-shot generators (none of them is edited on disk).

Each patch is (old, new, count, reason): build_rails.py applies it to the source text before running it and fails
unless «old» occurs exactly «count» times. Patching the source (not the finished text) keeps every derived string
(tables, frames, the Mātikā items reused by later chapters) consistent: identical Pāli = identical Burmese.
Reasons name the termbase headword(s) (AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md, locked) or the
binding approval (termbase/APPROVED.md).
"""

REL = "ရှိသမျှ"          # Yo / Yaṃ / ye / yañca (relative pronoun of the definition formula) = «… ရှိသမျှ»

# ------------------------------------------------------------------------------------------------- my_formulas.py
FORMULA_PATCHES = [
    ('UPPANNA = "ဖြစ်ပေါ်လာသော"', 'UPPANNA = "ဖြစ်ပေါ်ပြီးသော"', 1,
     "L01 uppannaṃ / uppannā / cittaṃ uppannaṃ / dhātu uppannā = ဖြစ်ပေါ်ပြီးသော (citta-opening formula, decision "
     "uppannaṃ|0; samuppannā stays ဖြစ်ပေါ်လာသော)"),
    ('CU_REL = {"sg": "ရှိသော", "pl": "ရှိကြသော"}',
     f'CU_REL = {{"sg": "ရှိသော", "pl": "ရှိကြသော"}}\nYO_REL = "{REL}"', 1,
     "L02 Yo / Yaṃ = ရှိသမျှ: the relative of the definition list (decision Yo|0)"),
    ('        parts += [TASMIM, CU_REL["sg"]]\n', '        parts += [TASMIM]\n', 1,
     "L02 Yo / Yaṃ: «ထိုအချိန်၌ ရှိသော A၊ B …» -> «ထိုအချိန်၌ A၊ B … ရှိသမျှ –»"),
    ('    parts.append(items_my(list_items(s[m.end():end])))\n',
     '    parts.append(items_my(list_items(s[m.end():end])) + " " + YO_REL)\n', 1,
     "L02 Yo / Yaṃ = «… ရှိသမျှ» before the dash"),
    ('"ākāsānañcāyatana": "အဆုံး မရှိသော ကောင်းကင် နယ်ပယ်"', '"ākāsānañcāyatana": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်"',
     1, "L03 ākāsa = ဟင်းလင်းပြင်, also in the immaterial base (decision ākāsa|0)"),
    ('"paṭiccasamuppādakusalatā": "အကြောင်းအကျိုး ဆက်စပ်ဖြစ်ပေါ်ပုံ၌ ကျွမ်းကျင်ခြင်း"',
     '"paṭiccasamuppādakusalatā": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ၌ ကျွမ်းကျင်ခြင်း"', 1,
     "L04 paṭicca = အကြောင်းတို့ကို မှီ၍; paṭiccasamuppāda = «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ» (APPROVED.md)"),
    ('"Suññatavāro": f"ဆိတ်သုဉ်းကြောင်း {VARA}"', '"Suññatavāro": f"ဆိတ်သုဉ်းခြင်း {VARA}"', 1,
     "L05 Suññata = ဆိတ်သုဉ်းခြင်း; Suññatavāro = «ဆိတ်သုဉ်းခြင်း ဖော်ပြချက်» (APPROVED.md)"),
    ('"samāpattivuṭṭhānakusalatā": "ဈာန်မှ ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း"',
     '"samāpattivuṭṭhānakusalatā": "ဈာန် ဝင်စားရာမှ ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း"', 1,
     "L06 samāpatti (compound member) = ဈာန် ဝင်စားရာ, vuṭṭhānakusalatā = ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း"),
    ('f"{TASMIM} ရှက်ထိုက်သည့်အရာကို ရှက်ခြင်း၊ {_PAPA} ရှက်ခြင်း"',
     f'f"{{TASMIM}} ရှက်ထိုက်သည့်အရာကို ရှက်ခြင်း၊ {{_PAPA}} ရှက်ခြင်း {REL}"', 1,
     "L02 Yaṃ = ရှိသမျှ (the hiri definition «Yaṃ tasmiṃ samaye hirīyati … – idaṃ»)"),
    ('f"{TASMIM} ကြောက်ရွံ့ထိုက်သည့်အရာကို ကြောက်ရွံ့ခြင်း၊ {_PAPA} ကြောက်ရွံ့ခြင်း"',
     f'f"{{TASMIM}} ကြောက်ရွံ့ထိုက်သည့်အရာကို ကြောက်ရွံ့ခြင်း၊ {{_PAPA}} ကြောက်ရွံ့ခြင်း {REL}"', 1,
     "L02 Yaṃ = ရှိသမျှ (the ottappa definition)"),
]

# ------------------------------------------------------------------------------------------------- generators
GEN_PATCHES = {
    "make_ch2-02-03": [
        ('    parts = [F.TASMIM, F.CU_REL["sg"]] if m["ts"] else []\n', '    parts = [F.TASMIM] if m["ts"] else []\n',
         1, "L02 Yo / Yaṃ = ရှိသမျှ (list closed by «, idaṃ tasmiṃ samaye», ^1-364)"),
        ('    parts.append(F.items_my(F.list_items(m["lst"])))\n',
         '    parts.append(F.items_my(F.list_items(m["lst"])) + " " + F.YO_REL)\n', 1, "L02 Yo / Yaṃ = ရှိသမျှ"),
        ('"Catukkanayo": f"{F.JHANA} {C[\'catu\']}{F.CL} {NAYA}", "Pañcakanayo": f"{F.JHANA} {C[\'pañca\']}{F.CL} {NAYA}"',
         '"Catukkanayo": f"{F.JHANA} {C[\'catu\']}{F.CL} ခွဲနည်း", "Pañcakanayo": f"{F.JHANA} {C[\'pañca\']}{F.CL} ခွဲနည်း"',
         1, "L07 Catukkanayo / Pañcakanayo = ဈာန် လေးပါး / ငါးပါး ခွဲနည်း (nayo = ခွဲနည်း)"),
    ],
    "make_ch2-04-05": [
        ('AKASA = "အဆုံးမရှိသော ကောင်းကင် နယ်ပယ်"', 'AKASA = "အဆုံးမရှိသော ဟင်းလင်းပြင် နယ်ပယ်"', 1,
         "L03 ākāsa = ဟင်းလင်းပြင်"),
        ('"Suddhikaappaṇihitaṃ": f"{PANIHITA} မရှိခြင်း {SUDDHIKA}"',
         '"Suddhikaappaṇihitaṃ": f"{PANIHITA} မရှိသော ဈာန် {SUDDHIKA}"', 1,
         "L08 Suddhikaappaṇihitaṃ = တောင့်တမှု မရှိသော ဈာန် သက်သက်"),
        ('{_PAPA} မရှက်ခြင်း",', f'{{_PAPA}} မရှက်ခြင်း {REL}",', 1, "L02 Yaṃ = ရှိသမျှ (ahirika definition)"),
        ('{_PAPA} မကြောက်ရွံ့ခြင်း",', f'{{_PAPA}} မကြောက်ရွံ့ခြင်း {REL}",', 1, "L02 Yaṃ = ရှိသမျှ (anottappa definition)"),
    ],
    "make_ch3": [
        ('"indriyānaṃ paripāko": f"{F.INDRIYA}တို့ ရင့်ရော်ခြင်း"', '"indriyānaṃ paripāko": "အာရုံခံ အင်္ဂါတို့ ရင့်ရော်ခြင်း"',
         1, "L09 indriyānaṃ = အာရုံခံ အင်္ဂါ (decision: «in the ageing definition the sense organs decline»)"),
        ('f"{AYATANA}တို့၏ စုပုံခြင်း{C} ထိုအရာသည်', f'f"{{AYATANA}}တို့၏ စုပုံခြင်း {REL}{{C}} ထိုအရာသည်', 1,
         "L02 Yo = ရှိသမျှ («Yo āyatanānaṃ ācayo, so …»)"),
        ('f"{NOUN[\'rūpassa upacayo\']}{C} ထိုအရာသည်', f'f"{{NOUN[\'rūpassa upacayo\']}} {REL}{{C}} ထိုအရာသည်', 1,
         "L02 Yo = ရှိသမျှ («Yo rūpassa upacayo, sā …»)"),
        ("    return f\"{F.items_my(F.list_items(m['l']))}{C} {TAIL}\"\n",
         f"    return f\"{{F.items_my(F.list_items(m['l']))}} {REL}{{C}} {{TAIL}}\"\n", 1,
         "L02 Yaṃ = ရှိသမျှ (the element definitions «Yaṃ kakkhaḷaṃ … ajjhattaṃ vā bahiddhā vā … –»)"),
        ("    return f\"{CITTA3} {F.items_my(F.list_items(m['l']))}\"\n",
         f"    return f\"{{CITTA3}} {{F.items_my(F.list_items(m['l']))}} {REL}\"\n", 1,
         "L02 Yā (same definition formula as Yo / Yaṃ) = ရှိသမျှ (vācā list)"),
    ],
    "make_ch4": [
        ('KAMMA_KATATTA = "ကံကို ပြုခဲ့ခြင်းကြောင့်"', 'KAMMA_KATATTA = "ပြုခဲ့သော ကံကြောင့်"', 1,
         "L10 kammassa katattā = ပြုခဲ့သော ကံကြောင့် (decision, 3-0x form)"),
        ('"vibhavataṇhā": f"{BHAVA} ပြတ်စဲခြင်းကို တပ်မက်မှု"', '"vibhavataṇhā": f"{BHAVA} ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု"', 1,
         "L11 vibhava = ဘဝ ပျောက်ကွယ်ခြင်း (APPROVED.md)"),
        ('"Kusalānaṃ vā dhammānaṃ vipākato": f"{KUS} {DH}တို့၏ အကျိုး အဖြစ်ဖြင့်ဖြစ်စေ"',
         '"Kusalānaṃ vā dhammānaṃ vipākato": f"{KUS} {DH}တို့၏ အကျိုး ဖြစ်သော စိတ်၌ဖြစ်စေ"', 1,
         "L12 vipākato = အကျိုး ဖြစ်သော စိတ် (decision: fits after a genitive)"),
        ('"Kusalānaṃ dhammānaṃ vipākato": f"{KUS} {DH}တို့၏ အကျိုး အဖြစ်ဖြင့်"',
         '"Kusalānaṃ dhammānaṃ vipākato": f"{KUS} {DH}တို့၏ အကျိုး ဖြစ်သော စိတ်၌"', 1,
         "L12 vipākato = အကျိုး ဖြစ်သော စိတ်"),
        ('_VIT = {"kāyiko": "ကိုယ်ဖြင့်", "vācasiko": "နှုတ်ဖြင့်", "kāyikavācasiko": "ကိုယ်နှင့် နှုတ်ဖြင့်"}',
         '_VIT = {"kāyiko": "ကိုယ်ပိုင်းဆိုင်ရာ", "vācasiko": "နှုတ်ပိုင်းဆိုင်ရာ", '
         '"kāyikavācasiko": "ကိုယ်ပိုင်းဆိုင်ရာနှင့် နှုတ်ပိုင်းဆိုင်ရာ"}', 1,
         "L13 kāyiko = ကိုယ်ပိုင်းဆိုင်ရာ, vācasiko = နှုတ်ပိုင်းဆိုင်ရာ"),
        ('ဒေါသနှင့် နီးစပ်သော', 'အမျက်ဒေါသနှင့် နီးစပ်သော', 1, "L14 kodha = အမျက်ဒေါသ (kodhasāmantā)"),
        ('နားဝင်ချိုသော', 'နား သာယာသော', 1, "L15 sukhā = သာယာသော (decision: kaṇṇasukhā «နား သာယာသော»)"),
        ('နှလုံးသို့ ရောက်သော', 'နှလုံးသားသို့ ရောက်သော', 1, "L16 hadaya = နှလုံးသား (hadayaṅgamā)"),
        ('"bhiyyokamyatā": "ပိုမို လိုလားခြင်း"', '"bhiyyokamyatā": "ပိုမို လိုချင်ခြင်း"', 1,
         "L17 kamyatā = လိုချင်ခြင်း (compound final)"),
        ("num('သိမြင်ခြင်း၏ အင်္ဂါ', 'satta')", "num('ဗောဇ္ဈင်', 'satta')", 1, "L18 bojjhaṅgā = ဗောဇ္ဈင်"),
        ('ဟူသော သိမြင်ခြင်း၏ အင်္ဂါ"', 'ဟူသော ဗောဇ္ဈင်"', 1, "L18 sambojjhaṅgo = ဗောဇ္ဈင်"),
        ('"Saṃvegoti": F.SAMVEGA + _TI', '"Saṃvegoti": F.SAMVEGA + " ရခြင်း" + _TI', 1,
         "L19 Saṃvego = သံဝေဂ ရခြင်း (as the Mātikā item)"),
        ('{DH}တို့ မဖြစ်ပေါ်စေရန်', '{DH}တို့ မဖြစ်ပေါ်ရန်', 1, "L20 anuppādāya = မဖြစ်ပေါ်ရန် (not a causative)"),
        ('{DH}တို့ ဖြစ်ပေါ်စေရန်', '{DH}တို့ ဖြစ်ပေါ်ရန်', 1, "L20 uppādāya = ဖြစ်ပေါ်ရန် (not a causative)"),
        ('ရှေးဘဝများကို အောက်မေ့နိုင်သော ဉာဏ်', 'ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်', 1,
         "L21 anussati = အဖန်ဖန် အောက်မေ့ခြင်း (pubbenivāsānussati)"),
        ('"Yo eva so dhammo appaccayo": f"အကြင် {DH}သည် {pred(T[\'appaccayā\'], False)}"',
         f'"Yo eva so dhammo appaccayo": f"{{T[\'appaccayā\']}} {{DH}} {REL}"', 1, "L02 Yo = ရှိသမျှ"),
        ('"samuppannā": "ကောင်းစွာ ဖြစ်ပေါ်ပြီးသော"', '"samuppannā": "ဖြစ်ပေါ်လာသော"', 1,
         "L22 samuppannā = ဖြစ်ပေါ်လာသော (kept apart from uppannā in the arisen-states list, decision samuppannā)"),
        ('"asamuppannā": "ကောင်းစွာ မဖြစ်ပေါ်သေးသော"', '"asamuppannā": "မဖြစ်ပေါ်လာသေးသော"', 1,
         "L22 asamuppannā: the not-arisen list builds «မ…သေးသော» from the positive (now ဖြစ်ပေါ်လာသော)"),
        ('    return g + F.items_my(F.list_items(m["list"].replace(",", "")))\n',
         '    return g + F.items_my(F.list_items(m["list"].replace(",", ""))) + " " + F.YO_REL\n', 1,
         "L02 Yo / Yaṃ = «… ရှိသမျှ» (Nikkhepa definition lists)"),
        ('    ph({f"{_y}{_k} avītikkamo": f"{_v} မကျူးလွန်ခြင်း", f"{_y}{_k} vītikkamo": f"{_v} ကျူးလွန်ခြင်း"})\n',
         f'    _r = " {REL}" if _k == "kāyikavācasiko" else ""\n'
         '    ph({f"{_y}{_k} avītikkamo": f"{_v} မကျူးလွန်ခြင်း{_r}", f"{_y}{_k} vītikkamo": f"{_v} ကျူးလွန်ခြင်း{_r}"})\n',
         1, "L02 Yo = ရှိသမျှ («Yo kāyiko …, vācasiko …, kāyikavācasiko … –»: before the dash)"),
        ('"na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{_PAPA} မရှက်ခြင်း"',
         f'"na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{{_PAPA}} မရှက်ခြင်း {REL}"', 1,
         "L02 Yaṃ = ရှိသမျှ («Yaṃ na hirīyati …, na hirīyati … –»)"),
        ('"na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{_PAPA} မကြောက်ရွံ့ခြင်း"',
         f'"na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{{_PAPA}} မကြောက်ရွံ့ခြင်း {REL}"', 1,
         "L02 Yaṃ = ရှိသမျှ"),
        ('"hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{_PAPA} ရှက်ခြင်း"',
         f'"hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{{_PAPA}} ရှက်ခြင်း {REL}"', 1,
         "L02 Yaṃ = ရှိသမျှ (as the 2-01 BODY; the assert of make_ch4 still holds)"),
        ('"ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{_PAPA} ကြောက်ရွံ့ခြင်း"',
         f'"ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{{_PAPA}} ကြောက်ရွံ့ခြင်း {REL}"', 1,
         "L02 Yaṃ = ရှိသမျှ"),
        ('"yañca rūpaṃ kammassa katattā uppajjissati": f"{KAMMA_KATATTA} ဖြစ်ပေါ်လာမည့် ရုပ်လည်း"',
         f'"yañca rūpaṃ kammassa katattā uppajjissati": f"{{KAMMA_KATATTA}} ဖြစ်ပေါ်လာမည့် ရုပ် {REL}လည်း"', 1,
         "L02 yañca = ရှိသမျှ (as the other «yañca rūpaṃ …» items «… ရုပ် ရှိသမျှလည်း»)"),
        ('"sineho": "ချစ်ခင်ခြင်း"', '"sineho": "ချစ်ခင်မှု"', 1,
         "L26 sineho = ချစ်ခင်မှု (decision: same nominaliser as nandī / mucchā of the kāma lists)"),
        ('"mucchā": "မိန်းမောခြင်း"', '"mucchā": "မိန်းမောမှု"', 1, "L26 mucchā = မိန်းမောမှု (decision)"),
        ('"santuṭṭhitā": "ရောင့်ရဲခြင်း"', '"santuṭṭhitā": "ရောင့်ရဲမှု"', 1,
         "L26 santuṭṭhitā = ရောင့်ရဲမှု (decision, as the Mātikā asantuṭṭhitā «ရောင့်ရဲမှု မရှိခြင်း»)"),
        ('ကိုယ်ဆင်းရဲခြင်း၊ စိတ်ဆင်းရဲခြင်း၊ ', 'ကိုယ်ဆင်းရဲခြင်း၊ စိတ်ဆင်းရဲမှု၊ ', 1,
         "L27 domanassa = စိတ်ဆင်းရဲမှု (decision, 29 of 30; sokaparidevadukkhadomanassupāyāsā)"),
        ("{SYN['abhijjhā']}၊ စိတ်ဆင်းရဲခြင်း ဟူသော ", "{SYN['abhijjhā']}၊ စိတ်ဆင်းရဲမှု ဟူသော ", 1,
         "L27 domanassā / abhijjhādomanassā = … စိတ်ဆင်းရဲမှု (re-alignment)"),
    ],
    "make_ch5": [
        ('ETTH = new("etthuppanna (arisen therein)", "ထိုတို့၌ ဖြစ်ပေါ်သော")',
         'ETTH = new("etthuppanna (arisen therein)", "ထိုတို့၌ ဖြစ်ပေါ်ပြီးသော")', 1,
         "L01 uppanne / uppannaṃ vicāraṃ / uppanne hetū = ဖြစ်ပေါ်ပြီးသော"),
        ('"ဖြစ်ပေါ်သော")\nAVAS', '"ဖြစ်ပေါ်ပြီးသော")\nAVAS', 1, "L01 uppanno = ဖြစ်ပေါ်ပြီးသော"),
        ('"kusalato ca vipākato ca kiriyato ca": f"{T[\'kusalā\']}{AS}{F.COMMA} ကံ၏ အကျိုး{AS}{F.COMMA} {KIR_STEM}{AS}"',
         '"kusalato ca vipākato ca kiriyato ca": f"{KUS}{AMONG}{CA}ကောင်း{F.COMMA} အကျိုး ဖြစ်သော {MIND}{AMONG}{CA}ကောင်း'
         '{F.COMMA} {KIR}{AMONG}{CA}ကောင်း"', 1,
         "L23 kusalato = ကုသိုလ်စိတ်; vipākato ca kiriyato = «အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း ပြုရုံမျှသာ ဖြစ်သော "
         "စိတ်အနက်လည်းကောင်း» (decision)"),
        ('"kusalato ca vipākato ca": f"{T[\'kusalā\']}{AS}{F.COMMA} ကံ၏ အကျိုး{AS}"',
         '"kusalato ca vipākato ca": f"{KUS}{AMONG}{CA}ကောင်း{F.COMMA} အကျိုး ဖြစ်သော {MIND}{AMONG}{CA}ကောင်း"', 1,
         "L23 kusalato / vipākato"),
        ('"kusalato ca kiriyato ca": f"{T[\'kusalā\']}{AS}{F.COMMA} {KIR_STEM}{AS}"',
         '"kusalato ca kiriyato ca": f"{KUS}{AMONG}{CA}ကောင်း{F.COMMA} {KIR}{AMONG}{CA}ကောင်း"', 1,
         "L23 kusalato / kiriyato"),
        ('"rūpañca nibbānañca": f"{RUP}နှင့် {NIB}"', '"rūpañca nibbānañca": f"{RUP}{CA} {NIB}{CA}"', 1,
         "L24 rūpañca nibbānañca = ရုပ်လည်း နိဗ္ဗာန်လည်း (decision, 45 of 47)"),
        ('ကံကို ပြုခဲ့ခြင်းကြောင့် ဖြစ်သော {RUP}', 'ပြုခဲ့သော ကံကြောင့် ဖြစ်သော {RUP}', 1,
         "L10 kammassa katattā = ပြုခဲ့သော ကံကြောင့်"),
        ('ကံကို ပြုခဲ့ခြင်းကြောင့် ဖြစ်သည် မဟုတ်သော {RUP}', 'ပြုခဲ့သော ကံကြောင့် ဖြစ်သည် မဟုတ်သော {RUP}', 1,
         "L10 kammassa katattā = ပြုခဲ့သော ကံကြောင့်"),
        ('_HETU = {"kusala": f"{T[\'kusalā\']}၏ {ROOT}"', '_HETU = {"kusala": f"{T[\'kusalā\']} {ROOT}"', 1,
         "L25 kusalahetu = ကုသိုလ် အမြစ် (decision kusalahetū)"),
        ('"kusalahetū": f"{T[\'kusalā\']}၏ {ROOT}", "akusalahetū": f"{T[\'akusalā\']}၏ {ROOT}"',
         '"kusalahetū": f"{T[\'kusalā\']} {ROOT}", "akusalahetū": f"{T[\'akusalā\']} {ROOT}"', 1,
         "L25 kusalahetū / akusalahetū = ကုသိုလ် / အကုသိုလ် အမြစ် (as 4-01)"),
        ('"abyākatahetū": f"{ABY} {DH}တို့၏ {ROOT}"', '"abyākatahetū": f"{ABY} {ROOT}"', 1,
         "L25 abyākatahetū = «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်» (as 4-01)"),
    ],
}

# ------------------------------------------------------------------------------------------------- bilingual-review fixes
# review/report-A.md, review/report-B.md, decisions in review/fix-brief.md, results in review/fix-notes.md. Only the fixes
# that change a repeated formula or term are here (one source string = every copy); the positional / single-segment
# fixes are explicit rules in apply_fixes.py, run after apply_termbase.py.
_BAH = "မိမိ၏ ပြင်ပ၌"   # bahiddhā (external, not one's own): user-approved termbase change 2026-11-17 (APPROVED.md)
FORMULA_PATCHES += [
    ('"bahiddhā": "သူတစ်ပါး၌ ရှိသော"', f'"bahiddhā": "{_BAH} ရှိသော"', 1,
     "L28 bahiddhā = မိမိ၏ ပြင်ပ၌ (termbase bahiddhā|1, dhammā bahiddhā, bahiddhā dhammā; user-approved 2026-11-17; "
     "B3, B5)"),
    ('"ajjhattabahiddhā": "မိမိ၌နှင့် သူတစ်ပါး၌ ရှိသော"', f'"ajjhattabahiddhā": "မိမိ၌နှင့် {_BAH} ရှိသော"', 1,
     "L28 ajjhattabahiddhā = မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော"),
    ('"bahiddhārammaṇā": f"သူတစ်ပါး၌ ရှိသည်{TAKES}"', f'"bahiddhārammaṇā": f"{_BAH} ရှိသည်{{TAKES}}"', 1,
     "L28 bahiddhārammaṇā = မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော"),
    ('"ajjhattabahiddhārammaṇā": f"မိမိ၌နှင့် သူတစ်ပါး၌ ရှိသည်{TAKES}"',
     f'"ajjhattabahiddhārammaṇā": f"မိမိ၌နှင့် {_BAH} ရှိသည်{{TAKES}}"', 1,
     "L28 ajjhattabahiddhārammaṇā = မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော"),
    ('{_SATA}သည်လည်း မဟုတ်၊ နှစ်သက်ဖွယ် မကောင်းသည်လည်း မဟုတ်သော အဖြစ်',
     '{_SATA}သည်လည်း မဟုတ် နှစ်သက်ဖွယ် မကောင်းသည်လည်း မဟုတ်သော အဖြစ်', 1,
     "L32 A5 cetasikaṃ neva sātaṃ nāsātaṃ: one synonym item, no «၊» inside it"),
]
# B6, B7, B10: applied after the user-approved termbase change of 2026-11-17 (termbase/APPROVED.md, decisions-A.tsv
# section «Review fix B6/B7/B10»); patches L36–L38 below.
FORMULA_PATCHES += [
    ('CITTAHETUKA = f"{MIND}ကို အမြစ်ပြုသော"', 'CITTAHETUKA = f"{MIND}ကို အကြောင်းပြုသော"', 1,
     "L36 B6 cittahetukaṃ = စိတ်ကို အကြောင်းပြုသော (caused by mind; termbase cittahetukaṃ|0, user-approved 2026-11-17)"),
    ('"ucchedadiṭṭhi": "အတ္တသည် သေပြီးနောက် ပြတ်စဲသွားသည်ဟူသော အယူ"',
     '"ucchedadiṭṭhi": "အတ္တသည် ပြတ်စဲသွားသည်ဟူသော အယူ"', 1,
     "L38 B10 ucchedadiṭṭhi without the added «သေပြီးနောက်» (termbase uccheda|0, ucchedadiṭṭhi|0, user-approved "
     "2026-11-17); the Mātikā item ^1-M2-112 and 4-03 ^1-1323 share this string"),
]
GEN_PATCHES["make_ch3"] += [
    ('CITTAJA, CITTAHETU = f"{F.MIND}မှ မွေးဖွားသော", f"{F.MIND}ကို အမြစ်ပြုသော"',
     'CITTAJA, CITTAHETU = f"{F.MIND}မှ မွေးဖွားသော", f"{F.MIND}ကို အကြောင်းပြုသော"', 1,
     "L36 B6 cittahetuka = စိတ်ကို အကြောင်းပြုသော in the Rūpakaṇḍa (and its negative via no_)"),
]
GEN_PATCHES["make_ch2-04-05"] += [
    ('"byāpajjanā": "ညှဉ်းဆဲလိုခြင်း", "byāpajjitattaṃ": "ညှဉ်းဆဲလိုသော အဖြစ်"',
     '"byāpajjanā": "ဖောက်ပြန်နေခြင်း", "byāpajjitattaṃ": "ဖောက်ပြန်ထားသော အဖြစ်"', 1,
     "L37 B7 byāpatti / byāpajjanā / byāpajjitattaṃ on one stem (termbase byāpatti ဖောက်ပြန်ခြင်း, byāpajjanā|0 "
     "ဖောက်ပြန်နေခြင်း, user-approved 2026-11-17)"),
]
GEN_PATCHES["make_ch4"] += [
    ('"byāpajjanā": "ညှဉ်းဆဲလိုခြင်း",', '"byāpajjanā": "ဖောက်ပြန်နေခြင်း",', 1, "L37 B7 byāpajjanā = ဖောက်ပြန်နေခြင်း"),
    ('"byāpajjitattaṃ": "ညှဉ်းဆဲလိုသော အဖြစ်",', '"byāpajjitattaṃ": "ဖောက်ပြန်ထားသော အဖြစ်",', 1,
     "L37 B7 byāpajjitattaṃ = ဖောက်ပြန်ထားသော အဖြစ်"),
]
GEN_PATCHES["make_ch2-04-05"] += [
    ('"Abyākatavipāko": f"{ABY} {VIPAKA_N}"', '"Abyākatavipāko": f"{VIPAKA_ATTR} {ABY} {DHAMMA}"', 1,
     "L29 A1 Abyākatavipāko = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား (the result is "
     "abyākata; as ^1-565 Vipākā abyākatā)"),
    ('"Akusalavipākaabyākataṃ": f"{ABY} {T[\'akusalā\']}{KAMMA}၏ အကျိုး"',
     '"Akusalavipākaabyākataṃ": f"{_AKV} {ABY} {DHAMMA}"', 1,
     "L29 A2 Akusalavipākaabyākataṃ = အကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ … သဘောတရား"),
    ('"Aṭṭhamahāvipākā": f"ကြီးကျယ်သော {VIPAKA_N} {F.NUM[\'aṭṭha\']}{F.CL}"',
     '"Aṭṭhamahāvipākā": f"{KAMMA}၏ ကြီးကျယ်သော အကျိုး {F.NUM[\'aṭṭha\']}{F.CL}"', 1,
     "L30 A3 Aṭṭhamahāvipākā = ကံ၏ ကြီးကျယ်သော အကျိုး ရှစ်ပါး (mahā qualifies vipāka)"),
    ('"Suddhikasuññataṃ": f"{SUNNATA}ခြင်း {SUDDHIKA}"', '"Suddhikasuññataṃ": f"{SUNNATA}သော ဈာန် {SUDDHIKA}"', 1,
     "L31 A4 Suddhikasuññataṃ = ဆိတ်သုဉ်းသော ဈာန် သက်သက် (as Suññataṃ ^1-344, Suddhikaappaṇihitaṃ ^1-522)"),
    ('"Chandādhipateyyasuddhikasuññatā": f"ဆန္ဒ{ADHIPATI}သော {SUNNATA}ခြင်း {SUDDHIKA}"',
     '"Chandādhipateyyasuddhikasuññatā": f"ဆန္ဒ{ADHIPATI}သော {SUNNATA}သော ဈာန် {SUDDHIKA}"', 1,
     "L31 A4 Chandādhipateyyasuddhikasuññatā = ဆန္ဒကို အကြီးအမှူးပြုသော ဆိတ်သုဉ်းသော ဈာန် သက်သက်"),
]
GEN_PATCHES["make_ch3"] += [
    ('def r_cause_other(m):\n    return f"{CAUSE[m[\'q\']]} အခြား {RUPA} ရှိသမျှလည်း"\n',
     'def r_cause_other(m):\n    return f"{CAUSE[m[\'q\']]} အခြား {RUPA} ရှိသမျှလည်း"\n\n\n'
     'def r_cause_other_list(m):\n    return f"{CAUSE[m[\'q\']]} အခြား {RUPA} ရှိသမျှ ဖြစ်သည့်"\n', 1,
     "L35 B11 «yaṃ vā panaññampi atthi rūpaṃ CAUSE» + list: «… အခြား ရုပ် ရှိသမျှ ဖြစ်သည့် LIST» (the frame)"),
    ('    (rf"yaṃ vā panaññampi atthi rūpaṃ (?P<q>{_alt(CAUSE)})", r_cause_other),\n',
     '    (rf"yaṃ vā panaññampi atthi rūpaṃ (?P<q>{_alt(CAUSE)})(?= [a-zāīūṃṅñṭḍṇḷ])", r_cause_other_list),\n'
     '    (rf"yaṃ vā panaññampi atthi rūpaṃ (?P<q>{_alt(CAUSE)})", r_cause_other),\n', 1,
     "L35 B11 the list follows directly (a space and a list item, no «,» / «–» in the Pāli): linked with «ဖြစ်သည့်»"),
]
GEN_PATCHES["make_ch4"] += [
    ('"Dasa kilesavatthūni": num(f"{F.KIL} ဖြစ်ရာ အခြေခံ", "dasa")', '"Dasa kilesavatthūni": num(f"{F.KIL} အခြေခံ", "dasa")',
     1, "L33 B4 Dasa kilesavatthūni = ကိလေသာ အခြေခံ ဆယ်ပါး (termbase vatthūni = အခြေခံ; as ^1-1565)"),
    ('"kusalābyākatā dhammā": f"{KUS}နှင့် {ABY} {DHP}"', '"kusalābyākatā dhammā": f"{KUS} သဘောတရားနှင့် {ABY} {DHP}"', 1,
     "L34 B9 kusalābyākatā dhammā = ကုသိုလ် သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ်၊ …"),
    ('"kusalākusalābyākatā dhammā": f"{KUS}၊ {AKUS}နှင့် {ABY} {DHP}"',
     '"kusalākusalābyākatā dhammā": f"{KUS}၊ {AKUS} သဘောတရားနှင့် {ABY} {DHP}"', 1,
     "L34 B9 kusalākusalābyākatā dhammā = ကုသိုလ်၊ အကုသိုလ် သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ်၊ …"),
    ('{T[\'cittasamuṭṭhānā\']} အခြား ရုပ် ရှိသမျှလည်း"})', '{T[\'cittasamuṭṭhānā\']} အခြား ရုပ် ရှိသမျှ ဖြစ်သည့်"})', 1,
     "L35 B11 «yaṃ vā panaññampi atthi rūpaṃ cittajaṃ …» + list (^1-1201)"),
]
GEN_PATCHES["make_ch5"] += [
    ('f"{T[\'kusalā\']}နှင့် {ABY}{F.COMMA} {RUPA} {DHS}', 'f"{T[\'kusalā\']} သဘောတရားနှင့် {ABY}{F.COMMA} {RUPA} {DHS}', 1,
     "L34 B9 kusalābyākatā (^1-1418) = ကုသိုလ် သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ်၊ …"),
]


def after_import(F):
    """Hook for value overrides after import (none needed: every change is a source patch above)."""
    return None
