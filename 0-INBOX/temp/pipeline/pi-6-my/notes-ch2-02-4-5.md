# pi-6 Burmese zero-shot: notes for 2-02-khandhayamaka, 4-dhatuyamaka, 5-01 / 5-02 / 5-03-saccayamaka

Status: generated and checked 2026-11-22. Not committed. Brief: burmese-zeroshot-brief.md.
Source rule kept: translated from the Pāli only; no Burmese translation / nissaya / web source opened
(0-INBOX/temp/language-priority/ not opened), no web search. pi-1 … pi-5 read only through their FINAL rails texts
(kwic6.py lookups and witnesses in the generator) and the locked termbases; English / Marathi pi-6 rails and the
Marathi make / notes files read for meaning and frame inventory only.

## Files
- Output (AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/): 2-02-khandhayamaka.md (169 segments,
  366 lines), 4-dhatuyamaka.md (51 / 265), 5-01-saccayamaka.md (160 / 550), 5-02-saccayamaka.md (122 / 314),
  5-03-saccayamaka.md (33 / 102).
- `make_ch2-02-4-5.py` (generator: imports my6_formulas read only and extends its tables IN MEMORY; `--misses`,
  `--who`), `check_ch2-02-4-5.py` (check_sample.py adapted; optional chapter arguments).
- Run: `python3 -I -X utf8 make_ch2-02-4-5.py` (writes the five files), `check_ch2-02-4-5.py`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all five files (chk-pe copies of my five files deleted).
- check_ch2-02-4-5.py: A 5/5 regenerated identical; B1 1597 lines; B2 2135 negations; B3 2222 uppajj / nirujjh + 136
  parijān / pajah verbs (root, tense, polarity, double negative) + 227 answers; B4 807 labelled lines; B5 digits + 180
  number words; B6 2001 distinct Pāli sentences, one Burmese each, TOGETHER WITH the sample's 1 / 2-01; B7 270
  headings / colophons / table lines; B8 29 quoted lines nested right; 0 mismatches. Reuse test 6900 / 6900 (C1
  569/569, C2 203/203, C3 96 reused terms 6128/6128). Per chapter: 2-02 1619/1619, 4 462/462, 5-01 2320/2320, 5-02
  1804/1804, 5-03 695/695. 7 documented exceptions / notes listed by the check.
- Aligned with the ch. 3 agent's notes (notes-ch3.md, read after my first run) where the Pāli is identical: agga
  «အမြတ်ဆုံး» (pi-2 ^2-1029), sa-X-ka / a-X-ka «X ရှိလျက် / X မရှိဘဲ», «“သောတ” (နား သို့မဟုတ် ရေစီး)», inner «tesaṃ
  cavantānaṃ» after a relative «…သူတို့အနက် စုတေဆဲသူတို့», cakkaṃ bandhitabbaṃ «… အပြည့်အစုံ ဖွဲ့ရမည်», saṃkhittaṃ
  «အကျဉ်း ဖော်ပြထားသည်», yassaka / yatthaka / yassayatthaka «“အကြင်သူအား” / “အကြင်နေရာ၌” / “အကြင်သူအား အကြင်နေရာ၌”
  အပိုင်း», vibhajitabba «ခွဲခြား ပြရမည်». Still different from ch. 3 (for the consistency pass): natthi nānākaraṇaṃ
  «ကွဲပြားချက် မရှိ» here vs nānaṃ natthi «ကွဲပြားခြင်း မရှိ» there (different Pāli words).

## Method
- Pure person runs / bare places go through the module (who_my, group_my, place_my), so they are identical to the
  sample. Only when the module raises Miss does the lead parser (lead_units) take over: units = person groups
  (module _one_group), relative clauses (REL), attributes + participle (ATTR), moments (GEN + uppāda / bhaṅga khaṇe,
  «… citte vattamāne», «tassa cittassa …»), places. Consecutive person units are joined as the module joins groups
  («A၊ Bနှင့် C»); other units with «၊ »; a final person run takes «အား», a final moment «ထိုသူတို့အား» (Pāli tesaṃ);
  «tesaṃ tattha» adds «ထိုနေရာ၌». A variant bracket goes after the unit holding the word before it; at the end of a
  lead after «…အား» (the sample's rule).
- «…pe…» lines: every piece between «…» is translated (sentence frames, else fragment()); every «…» kept.
- Paṇṇatti frames extended for avaseso / avasesaṃ (singular «ကြွင်းကျန်သော အရာ») and the special subjects
  (plural «…တို့»; verbs «ဖြစ်ကြသည် / မဟုတ်ကြ»).

## New recurring terms and phrases (Pāli = Burmese)
Reused from pi-1 … pi-5 FINAL (witnessed at import): dhātu names = pi-2 ^2-183 list («မျက်စိ ဓာတ်» … «သဘောတရား ဓာတ်»);
head «ဓာတ် ဆယ့်ရှစ်ပါး»; bare words = the dhātu name without «ဓာတ်» (cakkhu «မျက်စိ», sotaṃ «နား», ghānaṃ «နှာခေါင်း»,
jivhā «လျှာ», kāyo «ကိုယ်», saddo «အသံ», gandho «အနံ့», raso «အရသာ», phoṭṭhabbo «အထိအတွေ့», mano «မနော», dhammo «သဘောတရား»,
X-viññāṇaṃ «X သိစိတ်»), rūpaṃ «ရုပ်» (sample); sacca names pi-4 ^4-M-5 («ဒုက္ခ သစ္စာ», «ဖြစ်ပေါ်ခြင်း သစ္စာ»,
«ချုပ်ငြိမ်းခြင်း သစ္စာ», «မဂ် သစ္စာ»), «သစ္စာ လေးပါး» pi-2 ^2-206; dukkhaṃ «နာကျင်မှု», kāyikaṃ dukkhaṃ
«ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု» (pi-1 ^1-559); samudayo «ဖြစ်ပေါ်ခြင်း», nirodho «ချုပ်ငြိမ်းခြင်း» (pi-1 ^1-1063); maggo
«မဂ်» (pi-1); phala «ဖိုလ်»; arahā «ရဟန္တာ» (pi-4), arahantānaṃ «ရဟန္တာတို့» (pi-5); -samaṅgī «…နှင့် ပြည့်စုံသူ» (pi-1);
puthujjana «ပုထုဇဉ်»; paṭilabhati «ရရှိ» (pi-2); taṇhā «တပ်မက်မှု»; parijānāti «ပိုင်းခြား သိ», pajahati «ပယ်» (pi-5
^5-317); uppādakkhaṇe «ဖြစ်ခြင်း ခဏ၌», bhaṅgakkhaṇe «ပြိုပျက်ခြင်း ခဏ၌» (pi-5 ^5-366); citte vattamāne «စိတ် ဖြစ်နေစဉ်»
(pi-5 ^5-556); anantarā «ချက်ချင်း နောက်၌» (pi-2 ^2-751); abhisameti «ထင်ထင်ရှားရှား သိမြင်» (pi-5 ^5-431); apāya «အပါယ်»
(pi-5); dibbacakkhu / paññācakkhu «နတ်မျက်စိ / ပညာမျက်စိ», dibbasotaṃ «နတ်နား» (pi-5); pucchā «အမေး» (pi-5).

NEW (proposed here):
- dhātū (plural) = ဓာတ်တို့; saccā (plural) = သစ္စာတို့ (as khandhā «အစုအဝေးတို့»)
- Dhātuyamakaṃ = ဓာတ်များကို အတွဲလိုက် မေးဖြေခြင်း; Saccayamakaṃ = သစ္စာများကို အတွဲလိုက် မေးဖြေခြင်း (module TOPICS)
- cetasikaṃ dukkhaṃ = စိတ်ပိုင်းဆိုင်ရာ နာကျင်မှု
- Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ = ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှုနှင့် စိတ်ပိုင်းဆိုင်ရာ နာကျင်မှုတို့
- Dibbacakkhu paññācakkhu = နတ်မျက်စိနှင့် ပညာမျက်စိတို့
- Dibbasotaṃ taṇhāsotaṃ = နတ်နားနှင့် တပ်မက်မှု ရေစီးတို့ (sota = stream «ရေစီး», pi-5 termbase)
- sotaṃ in the two Dibbasotaṃ taṇhāsotaṃ sentences = “သောတ” (နား သို့မဟုတ် ရေစီး) (as ch. 3; see Choices)
- Sīlagandho samādhigandho paññāgandho = သီလ၏ အနံ့၊ သမာဓိ၏ အနံ့နှင့် ပညာ၏ အနံ့တို့
- Attharaso dhammaraso vimuttiraso = အနက်၏ အရသာ၊ တရား၏ အရသာနှင့် လွတ်မြောက်မှု၏ အရသာတို့
- avaseso / avasesaṃ (bare) = ကြွင်းကျန်သော အရာ (singular; avasesā «ကြွင်းကျန်သော အရာများ» as the sample)
- yo … so …? = အကြင်သူသည် …၊ ထိုသူသည် … သလော။ (as yassa … tassa); yo vā pana = တစ်ဖန် အကြင်သူသည်
- parijānāti / parijānittha / parijānissati = ပိုင်းခြား သိသည် / သိခဲ့သည် / သိလိမ့်မည်; na … = ပိုင်းခြား မသိ /
  မသိခဲ့ / မသိလိမ့်မည်; pajahati … = ပယ်သည် / ပယ်ခဲ့သည် / ပယ်လိမ့်မည်; nappajahati … = မပယ် / မပယ်ခဲ့ / မပယ်လိမ့်မည်;
  plural «…ကြ…»; double negative «no ca … na V» = «… မVသည်ကား မဟုတ်» (future «…လိမ့်မည်ကား မဟုတ်»)
- agga- (aggamagga / aggaphala) = အမြတ်ဆုံး (pi-2 ^2-1029; as ch. 3); Aggamaggasamaṅgī = အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ
- Ye maggaṃ paṭilabhissanti (te) = မဂ်ကို ရရှိမည့်သူတို့; ye (ca) puthujjanā maggaṃ na paṭilabhissanti = မဂ်ကို မရရှိမည့်
  ပုထုဇဉ်တို့; ye caññe maggaṃ paṭilabhissanti = မဂ်ကို ရရှိမည့် အခြားသူတို့
- Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā = အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူနှင့် ရဟန္တာကို ချန်ထား၍၊ ကြွင်းကျန်သော ပုဂ္ဂိုလ်တို့
- Arahā / Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te = ရဟန္တာ / အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူနှင့်
  မဂ်ကို မရရှိမည့် ပုထုဇဉ်တို့
- yassa cittassa anantarā aggamaggaṃ paṭilabhissanti = အကြင်စိတ်၏ ချက်ချင်း နောက်၌ အမြတ်ဆုံး မဂ်ကို ရရှိမည့်သူတို့;
  tassa cittassa uppāda- / bhaṅgakkhaṇe = ထိုစိတ်၏ ဖြစ်ခြင်း / ပြိုပျက်ခြင်း ခဏ၌
- pavatte = ဘဝ တည်နေစဉ် (in the course of existence, as against rebirth / death)
- X-assa uppādakkhaṇe / bhaṅgakkhaṇe = X၏ ဖြစ်ခြင်း / ပြိုပျက်ခြင်း ခဏ၌; cittassa «စိတ်၏», taṇhāya «တပ်မက်မှု၏», maggassa
  «မဂ်၏», aggamaggassa «အမြတ်ဆုံး မဂ်၏», phalassa «ဖိုလ်၏», aggaphalassa «အမြတ်ဆုံး ဖိုလ်၏», maggassa ca phalassa ca
  «မဂ်နှင့် ဖိုလ်၏», aggamaggassa ca phalassa ca «အမြတ်ဆုံး မဂ်နှင့် ဖိုလ်၏»
- pacchimacitta = နောက်ဆုံး စိတ်; pacchimacittasamaṅgīnaṃ = နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူတို့
- upapatticitta = ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်
- taṇhāvippayuttacitta = တပ်မက်မှုနှင့် ကင်းကွာသော စိတ်; maggavippayuttacitta = မဂ်နှင့် ကင်းကွာသော စိတ်;
  maggavippayuttataṇhāvippayuttacitta = မဂ်နှင့် ကင်းကွာ၍ တပ်မက်မှုနှင့် ကင်းကွာသော စိတ်;
  taṇhāvippayuttamaggavippayuttacitta = တပ်မက်မှုနှင့် ကင်းကွာ၍ မဂ်နှင့် ကင်းကွာသော စိတ်
- X-citte vattamāne = X စိတ် ဖြစ်နေစဉ်; dutiye (akusale) citte vattamāne = ဒုတိယ (အကုသိုလ်) စိတ် ဖြစ်နေစဉ်
- āpāyikānaṃ = အပါယ်၌ ရှိသူတို့; Apāye = အပါယ်၌ (PLACES «apāya» = «အပါယ်»)
- nirodhasamāpannānaṃ = ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူတို့ (nirodhasamāpatti pi-4 termbase)
- abhisametāvīnaṃ = သစ္စာကို ထင်ထင်ရှားရှား သိမြင်ပြီးသူတို့ (attr. «…သိမြင်ပြီးသော»); anabhisametāvīnaṃ = သစ္စာကို
  ထင်ထင်ရှားရှား မသိမြင်ရသေးသူတို့ (attr. «…မသိမြင်ရသေးသော»)
- sa-X-ka / a-X-ka (sacakkhuka …) = «X ရှိလျက်» / «X မရှိဘဲ» (as ch. 3), joined with a space before the participle:
  Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ = မျက်စိ ရှိလျက် နား မရှိဘဲ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့ (cakkhu «မျက်စိ», sota «နား»,
  ghāna «နှာခေါင်း», rūpa «ရုပ်», citta «စိတ်»)
- inner tesaṃ + participle (after a relative clause) = …သူတို့အနက် …ဆဲသူတို့ (those among them now …; as ch. 3 and the
  English rails), e.g. ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ = ရုပ်မရှိသော ဘုံ၌ ပြန်လည်
  ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့်သူတို့အနက် စုတေဆဲသူတို့
- inner tesaṃ + moment = ထိုသူတို့၏ …; sabbesaṃ before a moment = သူ အားလုံးတို့၏ …
- Avasese catuvokāre pañcavokāre = ကြွင်းကျန်သော အစုအဝေး လေးပါး ရှိသော ဘဝနှင့် အစုအဝေး ငါးပါး ရှိသော ဘဝ၌
- Headings: Uppādanirodhavāro = ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်; Pavatti 3. uppādanirodhavāro = ဖြစ်ပျက်ခြင်း 3.
  ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်; Pariññāvāro = ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက်; Suddhadhātuvāro =
  ရိုးရိုး ဓာတ် ဖော်ပြချက်; Suddhadhātumūlacakkavāro = ရိုးရိုး ဓာတ်ကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက်; Suddhasaccavāro /
  Suddhasaccamūlacakkavāro = ရိုးရိုး သစ္စာ ဖော်ပြချက် / ရိုးရိုး သစ္စာကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက်; Paṇṇattivāra (5-01
  spelling) = as Paṇṇattivāro
- Colophons: Nirodhavāro. = ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်။; Uppādanirodhavāro(.) = ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက်
  ဖော်ပြချက်(။); Pavattivāro niṭṭhito. = “ဖြစ်ပျက်ခြင်းအလိုက် ဖော်ပြချက်” ပြီးဆုံးပြီ။; Pariññāvāro. = ပိုင်းခြား သိခြင်းအလိုက်
  ဖော်ပြချက်။; Khandhayamakapāḷi niṭṭhitā. / Dhātuyamakaṃ niṭṭhitaṃ. = module COLO
- Editorial notes: yassaka = “အကြင်သူအား” အပိုင်း; yatthaka = “အကြင်နေရာ၌” အပိုင်း; yassayatthaka = “အကြင်သူအား
  အကြင်နေရာ၌” အပိုင်း (as ch. 3); sadisaṃ / sadisā = တူညီသည်; natthi nānākaraṇaṃ = ကွဲပြားချက် မရှိ; vitthāretabbaṃ = အကျယ် ချဲ့ရမည်;
  vibhajitabbaṃ = ခွဲခြား ပြရမည် (as ch. 3); (yathā …) vibhattaṃ = ခွဲခြား ပြထားသကဲ့သို့; cakkaṃ bandhitabbaṃ =
  လှည့်ပတ်ခြင်းကို အပြည့်အစုံ ဖွဲ့ရမည် (as ch. 3); kātabbaṃ = ပြုရမည် (na kātabbaṃ = မပြုရ); paripuṇṇaṃ = ပြည့်စုံအောင်; peyyālena = အကျဉ်းချုံ့၍; saṃkhittaṃ =
  အကျဉ်း ဖော်ပြထားသည် (as ch. 3); ubhato āmantā = နှစ်ဖက်စလုံး “ဟုတ်ပါသည်”; sabbe āmantā ubhatopi sesepi = နှစ်ဖက်စလုံး၌လည်း၊
  ကြွင်းကျန်သည်တို့၌လည်း အားလုံး “ဟုတ်ပါသည်”; asammohantena = မရောထွေးစေဘဲ; X-sadiso / -sadisā = Xနှင့် တူညီသည်;
  āyatanayamaka / dhātuyamaka (in notes) = “အာရုံခံ နယ်ပယ်များကို အတွဲလိုက် မေးဖြေခြင်း” / “ဓာတ်များကို …”; Tantinānākaraṇaṃ
  heṭṭhā yatthakasadisaṃ = စာကိုယ် ကွဲပြားချက်သည် ရှေ့၌ ရှိသော နေရာအလိုက် အပိုင်းနှင့် တူညီသည်; samudayasaccaṃ maggasaccaṃ
  nānākaraṇaṃ = ဖြစ်ပေါ်ခြင်း သစ္စာနှင့် မဂ် သစ္စာ ကွဲပြားချက်ကား …; nirodhasamāpannānanti = “ချုပ်ငြိမ်းခြင်း သမာပတ်ကို
  ဝင်စားနေသူတို့အား”ဟု
- Notes inside variant brackets: aññehi yamakehi saṃsanditabbaṃ = အခြား အတွဲလိုက် မေးဖြေခြင်းများနှင့် တိုက်ဆိုင် စစ်ဆေးရမည်;
  evaṃ avasesesu tīsu saccesu = ကြွင်းကျန်သော သစ္စာ သုံးပါးတို့၌လည်း ဤနည်းတူ; evaṃ puggalokāsepi nirodhavārepi = ပုဂ္ဂိုလ်နှင့်
  နေရာအလိုက်၌လည်း၊ ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်၌လည်း ဤနည်းတူ; puggalokāsavārepi = ပုဂ္ဂိုလ်နှင့် နေရာအလိုက် ဖော်ပြချက်၌လည်း;
  uppādavāre pana pāṭhantaraṃ natthi = ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ကား ပါဌ်ကွဲ မရှိ. Spelling-only variants
  («စာလုံးပေါင်းကွဲ»): «dhātu (sī. ka.)», «uppatticittassa (syā.)».
- Fragments between «…»: «X?» = «Xလော။»; «Na X?» = «X မဟုတ်သော အရာလော။»; bare «X» = «X»; «X ṭhapetvā» = «Xကို ချန်ထား၍»;
  «(Kha) yattha / yassa / yo vā pana…pe…?» = «(ခ) တစ်ဖန် အကြင်နေရာ၌ / အကြင်သူအား / အကြင်သူသည်…လော။»; «… uppajjitthāti?»
  (verb only) = «… ဖြစ်ပေါ်ခဲ့သလော။»; an answer clause cut by «…pe…» keeps its statement verb without «။».

## Choices for the reviewer / the consistency pass
1. uppādakkhaṇe «ဖြစ်ခြင်း ခဏ၌» follows pi-5 ^5-366 (identical Pāli word, binding), while pi-6 headings have uppāda
   «ဖြစ်ပေါ်ခြင်း» (sample). Alternative for pi-6-wide unity: «ဖြစ်ပေါ်ခြင်း ခဏ၌». Listed in EXCEPT of the check.
2. bare dukkhaṃ = «နာကျင်မှု» (painful feeling, pi-1 ^1-559): the Saccayamaka sets dukkha (bodily / mental pain) apart
   from dukkhasacca («Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ dukkhasaccaṃ, na dukkhaṃ»); pi-5 termbase has also
   dukkhaṃ «ဒုက္ခ» (truth sense), which would make that sentence say "dukkhasacca is not dukkha".
3. The lead rule (units joined «၊ », final moment + «ထိုသူတို့အား») keeps the Pāli juxtaposition; it does not decide
   whether a moment restricts the persons before it (as the English rails, which also join with commas).
4. «Dibbasotaṃ taṇhāsotaṃ sotaṃ, na sotadhātu»: sotaṃ rendered «“သောတ” (နား သို့မဟုတ် ရေစီး)» in these two sentences only (the Pāli word play
   ear / stream; «နား» would say "the stream of craving is an ear"); elsewhere sotaṃ «နား». The ch. 3 agent does the same
   for sotāyatana. The other special subjects keep the bare term (eye, smell, taste work in Burmese).
5. pavatte «ဘဝ တည်နေစဉ်» is NEW (the module's pavatti «ဖြစ်ပျက်ခြင်း» is the heading sense, "occurrence").

## Unsure Pāli / meaning
- abhisametāvī: «သစ္စာကို» (the truths) added for clarity, as the English / Marathi rails.
- aggamagga «အမြတ်ဆုံး မဂ်» (the arahant path); «aggamaggassa ca phalassa ca» «အမြတ်ဆုံး မဂ်နှင့် ဖိုလ်၏» leaves open whether
  agga covers phala too (as the Pāli).
- upapatticitta «ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်» (rebirth consciousness), literal.
- inner «tesaṃ cavantānaṃ» after «ye ca …» read as "those among them passing away" («…သူတို့အနက် စုတေဆဲသူတို့»),
  scoping over the relative clause only (English rails); it could also cover the groups before it.
- dutiye citte «ဒုတိယ စိတ်» (the second consciousness), literal; which consciousness is meant is not said.
- Natthi after a yattha question: «မရှိပါ။» as everywhere (module NATTHI).

## Source slips (translated as written, logged)
- 2-02 ^6-2-134 «… saññākkhandho ca nirujjhissati vedanākkhandho nirujjhati» (second ca missing) and ^6-2-163
  «rūpakkhandho nuppajjati vedanākkhandho ca …» (first ca missing): «လည်း» only where the Pāli has ca.
- 2-02 ^6-2-151 a stray comma before the second «… ca» clause (ignored).
- 2-02 ^6-2-185 «vadanākkhandho» for vedanākkhandho.
- 4 ^6-4-9 «…Pe….» (stop after the ellipsis): «…။».
- 4 ^6-4-15 «jivha ṭhapetvā» for jivhaṃ.
- 4 ^6-4-17 «Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhudhātu.» (the parallels have «na cakkhu, dhātu») and «Cakkhu ca
  dhātuñca» for Cakkhuñca: as written.
- 4 ^6-4-17 «(Yathā … vitthāretabbā)» without a stop: no «။».
- 5-01 ^6-5-1 «samudayasaccaṃ nirodhasaccaṃ» (comma missing in the list): «၊» put.
- 5-01 ^6-5-74 «paṭilabhissānti» for paṭilabhissanti; ^6-5-76 «asaññattā cavantānaṃ» for asaññasattā.
- 5-02 ^6-5-125 «na nirujjhiti» for na nirujjhati (read as present).
- 5-03 ^6-5-170 the line «… samudayasaccañca nappajahissanti» (after «Aggamaggasamaṅgī ye ca puthujjanā …») ends
  without «.»: «။» put. «no ca te samudayasaccaṃ …» (with te) = «သို့သော် ထိုသူတို့သည် …».
