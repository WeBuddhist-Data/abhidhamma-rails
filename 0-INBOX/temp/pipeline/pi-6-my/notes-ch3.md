# pi-6 Burmese zero-shot, ch. 3 (Āyatanayamaka): 3-01 … 3-06 — notes

Status 2026-11-22: all six files generated; check_chapter_ids / check_text_pe / check_marks OK for each (chk-pe copies
deleted); check_ch3.py 0 mismatches, reuse 10059 / 10059. Not committed. Brief: burmese-zeroshot-brief.md.
Source rule kept: translated from the Pāli only; no Burmese translation / nissaya / web source opened
(0-INBOX/temp/language-priority/ not opened). pi-1 … pi-5 read only through their rails texts (FINAL) and locked
termbases (kwic6.py / scratch/findw.py, read-only). English and Marathi pi-6 rails read for meaning only (sarūpaka,
the «ye ca … tesaṃ upapajjantānaṃ» group, the sota pun); pi-6-mr/make_ch3.py and notes-ch3.md read for the frame
inventory only (no Marathi words).

## Files
- Output: `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/3-01 … 3-06-ayatanayamaka.md`
  (segments 95 / 48 / 49 / 69 / 69 / 69; lines 599 / 227 / 296 / 315 / 335 / 309).
- `make_ch3.py` (generator; imports my6_formulas.py, extends its tables in memory only; `--misses`),
  `check_ch3.py` (per-line check + reuse test; `--mutate` = mutation self-test).
- Run: `python3 -I -X utf8 make_ch3.py` (writes the six files), `check_ch3.py`, `check_ch3.py --mutate`.

## Checks (final run)
- A 6/6 regenerated identical; B1 2081 lines; B2 3405 negations (na / no / nuppajj- / nāyatana / Natthi and the
  privative a-X-ka) each one Burmese negative; B3 4148 uppajj- / nirujjh- and 72 parijān- verbs in order with tense,
  polarity, double negative, 398 answers; B4 1096 labelled lines, every vā pana = «တစ်ဖန်»; B5 digits + 261 number
  words; B6 2177 distinct Pāli sentences, one Burmese each (also the 201 occurrences in the approved sample files);
  B7 301 headings / colophons / notes / list lines; 0 mismatches.
- Reuse 10059 / 10059 (C1 āyatana names and bare words 3647/3647; C2 whole lines and answers 365/365; C3 51 reused
  terms 6047/6047). Documented exceptions not counted: the sample's anuloma / paccanīka, cavati, Natthi (415 lines).
- One line exception (B2): 3-06 line 189 (^6-3-237) «… no ca tesaṃ tattha…pe… …»: the negated verb is cut by the «…», so the
  Burmese «သို့သော် ထိုသူတို့အား ထိုနေရာ၌…» has no verb to negate.
- Mutation test: dropped «မ», dropped «ခဲ့», tense swap, attribute polarity, dropped double negative, changed answer,
  changed base name, changed label: all caught.

## New recurring terms and phrases (Pāli = Burmese; for the consistency pass)
- Āyatanayamakaṃ = အာရုံခံ နယ်ပယ်များကို အတွဲလိုက် မေးဖြေခြင်း (module TOPICS, proposed there)
- Dvādasāyatanāni – … = အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး – … (pi-2 ^2-154; names read by items())
- cakkhāyatanaṃ … dhammāyatanaṃ = မျက်စိ / နား / နှာခေါင်း / လျှာ / ကိုယ် / အဆင်းအရောင် / အသံ / အနံ့ / အရသာ / အထိအတွေ့ /
  မနော / သဘောတရား + « အာရုံခံ နယ်ပယ်» (pi-2 ^2-154)
- bare words (paṇṇattivāra) cakkhu = မျက်စိ; sotaṃ = နား; ghānaṃ = နှာခေါင်း; jivhā = လျှာ; kāyo = ကိုယ်; saddo = အသံ;
  gandho = အနံ့; raso = အရသာ; phoṭṭhabbo = အထိအတွေ့; mano = မနော; dhammo = သဘောတရား; rūpaṃ = ရုပ် (as the sample;
  NOT «အဆင်းအရောင်»: the text says the other rūpa is rūpa but not the visible-form base)
- āyatanaṃ = အာရုံခံ နယ်ပယ်; āyatanā = အာရုံခံ နယ်ပယ်တို့ (pi-1 ^1-1342, plural «ကြ»); nāyatanā / nāyatanaṃ = na āyatana
- avaseso / avasesaṃ X (sg.) = ကြွင်းကျန်သော အရာ (sg.; the sample's avasesā = ကြွင်းကျန်သော အရာများ, pl.)
- Dibbacakkhu paññācakkhu = နတ်မျက်စိနှင့် ပညာမျက်စိ (pi-5)
- Dibbasotaṃ taṇhāsotaṃ = နတ်နားနှင့် တပ်မက်မှု ရေစီး (dibbasota pi-5; taṇhā; sota = stream «ရေစီး», pi-4 anusota)
- sotaṃ said of these two = “သောတ” (နား သို့မဟုတ် ရေစီး) (NEW: the word play sota = ear / stream; REVIEW)
- Sīlagandho samādhigandho paññāgandho = သီလ၏ အနံ့၊ သမာဓိ၏ အနံ့နှင့် ပညာ၏ အနံ့
- Attharaso dhammaraso vimuttiraso = အနက်၏ အရသာ၊ တရား၏ အရသာနှင့် လွတ်မြောက်မှု၏ အရသာ
- joined subjects of the niddesa answers: «Aနှင့် Bတို့သည် … ဖြစ်ကြသည်၊ … မဟုတ်ကြ။» (plural)
- X Y ceva Yāyatanañca. = Xသည် Yလည်း ဖြစ်၊ Xလည်း ဖြစ်သည်။ (sample P2, fused «…ñca» accepted)
- fragments: «Sotaṃ ṭhapetvā» = နားကို ချန်ထား၍; «na ca āyatanā» = အာရုံခံ နယ်ပယ်တို့လည်း မဟုတ်; «na X» (end of
  «avasesā āyatanā na X») = X မဟုတ်ကြ; a question cut before its verb «…?» = «…လော။»; a lone group before «…» = «…အား…»
- Places (added to PLACES): kāmāvacara = ကာမဘုံ; rūpāvacara = သိမ်မွေ့သော ရုပ်ဘုံ; arūpāvacara = ရုပ်မရှိသော ဘုံ (= arūpa)
  (style core plane names, witnesses pi-1 ^1-M2-93 / 94 / 95); Kāmāvacarānaṃ = ကာမဘုံ၌ ရှိသူတို့ (module gen. frame)
- Persons (NEW): sa-X-ka = «X ရှိလျက်», a-X-ka = «X မရှိဘဲ», before place and participle: sacakkhuka / acakkhuka မျက်စိ;
  sasotaka / asotaka နား; saghānaka / aghānaka နှာခေါင်း; sarūpaka / arūpaka ရုပ်; sacittaka / acittaka စိတ်.
  Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ = မျက်စိ ရှိလျက် နား မရှိဘဲ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့;
  acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ = မျက်စိ မရှိဘဲ ကာမဘုံ၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့;
  Itaresaṃ sacakkhukānaṃ upapajjantānaṃ = မျက်စိ ရှိလျက် ပြန်လည် ဖြစ်ပေါ်ဆဲ အခြားသူတို့
- ye (ca) <places> upapajjitvā parinibbāyissanti = <places>၌ ပြန်လည် ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့်သူတို့ (module atom,
  generalised to any places); … tesaṃ upapajjantānaṃ / cavantānaṃ = …သူတို့အနက် ပြန်လည် ဖြစ်ပေါ်ဆဲ / စုတေဆဲသူတို့
  (those among them now being reborn / passing away; English rails meaning); joined to a preceding group with «နှင့်»
- Headings: Suddhāyatanavāro = ရိုးရိုး အာရုံခံ နယ်ပယ် ဖော်ပြချက်; Suddhāyatanamūlacakkavāro = ရိုးရိုး အာရုံခံ
  နယ်ပယ်ကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက် (as the sample's Suddhakhandha-); Pavatti 3. uppādanirodhavāro =
  ဖြစ်ပျက်ခြင်း 3. ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်; Pariññāvāro = ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက်
- Colophons: Uppādavāro. = ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်။; Nirodhavāro. = ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်။;
  Uppādanirodhavāro. = ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်။; Pavattivāro niṭṭhito. = “ဖြစ်ပျက်ခြင်းအလိုက်
  ဖော်ပြချက်” ပြီးဆုံးပြီ။; Pariññāvāro. = ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက်။; Āyatanayamakaṃ niṭṭhitaṃ. = module COLO
- Pariññāvāra (NEW frames; the khandha / dhātu agents need the same): parijānāti = ပိုင်းခြား သိ (pi-5 ^5-390), the «မ»
  before «သိ»: ပိုင်းခြား မသိ; tenses as my_verb: သိ၏ / သိသလော / သိသည်; သိခဲ့၏ / သိခဲ့သလော / သိခဲ့သည်; သိလိမ့်မည် /
  သိလိမ့်မည်လော; plural ကြ (မသိကြ၊ မသိခဲ့ကြ၊ မသိကြလိမ့်မည်); object «Xကို».
  yo X parijānāti so Y parijānātīti? = အကြင်သူသည် Xကို ပိုင်းခြား သိ၏၊ ထိုသူသည် Yကို ပိုင်းခြား သိသလော။
  (yo vā pana = တစ်ဖန် အကြင်သူသည် …; parallel to yassa … tassa «အကြင်သူအား … ထိုသူအား»)
  S X na parijānāti, no ca Y na parijānittha. = Sသည် Xကို ပိုင်းခြား မသိ၊ သို့သော် Yကို ပိုင်းခြား မသိခဲ့သည်ကား မဟုတ်။
  S Xñca na parijānanti Yñca na parijānittha. = Sသည် Xကိုလည်း ပိုင်းခြား မသိကြ၊ Yကိုလည်း ပိုင်းခြား မသိခဲ့ကြ။
- Arahā = ရဟန္တာ; Aggamaggasamaṅgī = အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ (agga pi-2 ^2-1029, magga, samaṅgī pi-2 ^2-809);
  Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā = အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူနှင့် ရဟန္တာကို ချန်ထား၍၊
  ကြွင်းကျန်သော ပုဂ္ဂိုလ်တို့; Ye maggaṃ paṭilabhissanti te = မဂ်ကို ရရှိမည့်သူတို့; (Arahā / Aggamaggasamaṅgī) ye ca
  puthujjanā maggaṃ na paṭilabhissanti te = ရဟန္တာ / အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူနှင့် မဂ်ကို မရရှိမည့် ပုထုဇဉ်တို့
- Notes (table NOTES in make_ch3.py, one Burmese each): (Cakkhāyatanamūlakaṃ) = (မျက်စိ အာရုံခံ နယ်ပယ်ကို အခြေခံ၍),
  likewise ghāna-, rūpa-, mana-; (Cakkaṃ bandhitabbaṃ) = (လှည့်ပတ်ခြင်းကို အပြည့်အစုံ ဖွဲ့ရမည်); (Saṃkhittaṃ) =
  (အကျဉ်း ဖော်ပြထားသည်); yassaka / yatthaka / yassayatthaka = “အကြင်သူအား” / “အကြင်နေရာ၌” / “အကြင်သူအား အကြင်နေရာ၌”
  အပိုင်း; pucchā = အမေး (pi-5); sadisa = တူညီ; vitthāretabba = အကျယ် ချဲ့ရမည် (pi-5 ^5-839); vibhajitabba = ခွဲခြား
  ပြရမည် (pi-2); upari vārasaṅkhepo = နောက်ပိုင်း ဖော်ပြချက်တို့၌ အကျဉ်း ဖော်ပြထားသည်; nānaṃ natthi = ကွဲပြားခြင်း မရှိ;
  noti na kātabbaṃ = “မဟုတ်ပါ” ဟု မဖြေရ; sabbattha āmantāti kātabbaṃ = နေရာတိုင်း၌ “ဟုတ်ပါသည်” ဟု ဖြေရမည်
- Variant bracket with two readings: [ပါဌ်ကွဲ (Syā.): a၊ (Sī., Ka.): b] (the module's variant() has one reading only).

## Unsure (for review)
- The sota pun “သောတ” (နား သို့မဟုတ် ရေစီး): Pāli word in Burmese script with a gloss; alternative «နား» (identity)
  would make «the stream of craving is an ear». gandha / rasa figurative uses keep အနံ့ / အရသာ (the argument needs it).
- Attribute order «X ရှိလျက် / X မရှိဘဲ» before the place and participle; two negatives give «မျက်စိ မရှိဘဲ နား မရှိဘဲ».
- sarūpaka / arūpaka = «ရုပ် ရှိလျက် / ရုပ် မရှိဘဲ» (material form, English rails «with material form»).
- arūpāvacara and arūpa share «ရုပ်မရှိသော ဘုံ» (two Pāli words, one place).
- A cut question «…pe…?» = «…လော။» (the question particle alone after the «…»).
- The plural subjects of the pariññā answers repeat no pronoun in the «no ca» clause (as the Pāli).

## Source slips (translated as written or minimally; Pāli not changed; SLIPS / SLIP_POST in make_ch3.py)
- 3-01 ^6-3-1: no comma after «sotāyatanaṃ» in the list: the Burmese list has «၊» there (punctuation only).
- 3-01 ^6-3-13: «sotāyananti» for sotāyatananti (read as sotāyatana).
- 3-01 ^6-3-43: «uppajjittharūpāyatanañca» (missing space; read as two words).
- 3-01 ^6-3-23: «… vārasaṅkhepo [...] tīti jānitabbaṃ» («tīti» unclear, perhaps «hotīti»): rendered «… ဟု သိရမည်».
- 3-02 ^6-3-75: «rūpāyatanañca ca uppajjittha» (doubled ca; one «လည်း»).
- 3-03 ^6-3-118: «(Ka) yassa =93 yattha …» stray «=93»: kept in the Burmese «အကြင်သူအား =93 အကြင်နေရာ၌».
- 3-03 ^6-3-100, ^6-3-116: two «X ca … Y ca» answers with one member lacking «ca» (the member without «လည်း»).
- 3-04 ^6-3-131: «na nirujjhatī ti» (split ti; one word).
- 3-04 ^6-3-148: «… na nirujjhissati, parinibbantānaṃ …»: comma for a full stop; translated as two sentences, the
  comma kept as «၊».
- 3-05 ^6-3-172: «parinibbāntānaṃ» for parinibbantānaṃ; 3-05 ^6-3-186: «manāyatana…pe…» (missing ṃ).
- 3-06 ^6-3-212: «no ca tesaṃ ghānāyatanaṃ upapajjissati» read as uppajjissati («ဖြစ်ပေါ်လိမ့်မည်»; the
  following «ghānāyatanañca uppajjissati» shows the intended verb).
- 3-06 ^6-3-229: sigla «(sī syā. ka.)» without the dot after sī; 3-06 ^6-3-244: «arūpānaṃ tasaṃ tattha» for tesaṃ.
- 3-01 a (Ka) line has «yassa vā pana» (^6-3-50): label kept «(က)», vā pana = «တစ်ဖန်» as written.
- 3-06 last segment: «Namo tassa …» stands after the chapter colophon inside ^6-3-254 (kept, module NAMO).
