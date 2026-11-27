# pi-6 Burmese zero-shot, group ch10b: notes (10-05 … 10-09-indriyayamaka)

Status 2026-11-22: all five files generated and checked. Not committed. Brief: burmese-zeroshot-brief.md.
Source rule kept: translated from the Pāli only; no Burmese translation / nissaya / web source opened
(0-INBOX/temp/language-priority/ not opened), no web search. pi-1 … pi-5 read only through their FINAL rails texts
(kwic6.py lookups, witnesses in the generator) and the locked termbases. English pi-6 rails read for meaning only
(eteneva bhāvena …, somanassena / upekkhāya upapajjati); pi-6-mr notes-ch10b.md read for the frame inventory only (no
Marathi words). Finished groups' generators (make_ch3.py, make_ch2-02-4-5.py, make_ch6-8.py) read, never run; their
functions copied.

## Files
- Output (AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/): 10-05 (59 segments, 393 lines),
  10-06 (40 / 318), 10-07 (10 / 99), 10-08 (39 / 288), 10-09 (22 / 249). All pavattivāra, uppādavāra only
  (atīta, anāgata, paccuppannātīta, paccuppannānāgata); no variant brackets, dashes or colophons; 10-09 ends inside
  the paccuppannānāgata (Ga) section (^6-10-384).
- `make_ch10b.py` (generator; imports my6_formulas.py unchanged, extends its tables in memory; `--misses`, `--who`),
  `check_ch10b.py` (per-line check + reuse test; `--mutate` = mutation self-test).
- Run: `python3 -I -X utf8 make_ch10b.py` (writes the five files), `check_ch10b.py`, `check_ch10b.py --mutate`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all five files (my chk-pe copies deleted).
- check_ch10b.py: A 5/5 regenerated identical; B1 1347 lines; B2 1816 negations, each one Burmese negative; B3 3623
  uppajj- verbs in order (tense, polarity, double negative), 384 answers; B4 586 labelled lines, every vā pana =
  «တစ်ဖန်»; B5 digits + 128 number words; B6 1645 distinct Pāli sentences, one Burmese each (also 1437 occurrences in
  the finished pi-6 files); B7 25 headings; B8 quotes OK; B9 3978 faculty words in order, each its pi-2 name; B10 1030
  attributes / head nouns / qualifiers, each its Burmese; 0 mismatches.
- Reuse 7654 / 7654 (C1 faculty names 2918/2918, C2 whole lines and answers 349/349, C3 34 reused terms 3617/3617,
  C4 pi-6 leads shared with the finished chapters 770/770 occurrences, 80 distinct leads). Per chapter: 10-05
  2151/2151, 10-06 1884/1884, 10-07 687/687, 10-08 1896/1896, 10-09 1624/1624. Documented exceptions not counted:
  the sample's anuloma / paccanīka, cavati, Natthi, and uppādakkhaṇe (ch. 5 / 6-8), 238 lines.
- Mutation test: dropped «မ», dropped «ခဲ့», future -> present, dropped double negative, Āmantā -> No, Natthi changed,
  faculty swapped / dropped, attribute polarity, na itthīnaṃ dropped, head noun changed, qualifier flipped, dropped
  «တစ်ဖန်», label changed, lead changed (itaresaṃ), bhāva phrase changed: all caught.
- Sibling ch. 10 groups (read after my first run, read only): of 386 lead occurrences shared with 10-01 … 10-04 and
  10-10 … 10-13, 369 agree. I took over somanassena / upekkhāya «…နှင့်အတူ» from both (my first run had «…ဖြင့်»).
  The 17 that differ are the moment leads of 10-10 / 10-11 (see «For the consistency pass» 1).

## Method
- Faculties: `F.items("2", "^2-219")` (pi-2 list, read at import; the 22 names in the pi-1 / pi-2 order and Burmese);
  added as pavatti subjects; «X-ñca» = «X…လည်း» (module).
- Person groups: the module's who_my / group_my first (every sample / ch. 3 group as there), with `F._one_group`
  extended for the attributes (ch. 3 code) and this chapter's attributes and head nouns; when the module raises Miss,
  the lead parser (copied from make_ch2-02-4-5.py): units = person groups, relative clauses, named persons, moments,
  places; person units joined «A၊ Bနှင့် C», other units «၊ »; final person + «အား», final moment + «ထိုသူတို့အား»;
  a lead that is ONE moment alone = «… ခဏ၌ ရှိသူတို့အား» (8-cittayamaka, identical Pāli «Pacchimacittassa
  uppādakkhaṇe tesaṃ»). tāsaṃ (f.) = tesaṃ «ထိုသူတို့(အား)».
- «…pe…» lines: make_ch3.py's fragment engine (each piece between «…» translated token by token; every «…» kept).
- Notes «(Xmūlakaṃ)» from the faculty table.

## New recurring terms and phrases (Pāli = Burmese; for the consistency pass)
Reused (witnessed at import): the 22 faculties = pi-2 ^2-219 («မျက်စိ၏ စွမ်းရည်» … «အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်»;
head «စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး»); somanassa «ဝမ်းမြောက်မှု», ñāṇa «ဉာဏ်», -sampayutta «နှင့် ယှဉ်တွဲသော» (pi-1 ^1-1);
upekkhā «ဥပေက္ခာ», -vippayutta «နှင့် ကင်းကွာသော» (pi-2 ^2-767); saddhā «ယုံကြည်မှု», itthī «မိန်းမ», purisa «ယောက်ျား»
(pi-2 ^2-219); sahetuka «အမြစ် ရှိ» (pi-1 ^1-M2-2); -sahagata «…နှင့်အတူ» (pi-1 ^1-1, ^1-M1-7); kāmāvacara /
rūpāvacara / arūpāvacara places (as ch. 3); uppāda- / bhaṅgakkhaṇe, citte vattamāne, anantarā, -samaṅgī (as ch. 5).
NEW here:
- (Cakkhundriyamūlakaṃ) = (မျက်စိ၏ စွမ်းရည်ကို အခြေခံ၍); likewise every «(Xindriyamūlakaṃ)» = «(X၏ စွမ်းရည်ကို အခြေခံ၍)»
  (as ch. 3 «(Xအာရုံခံ နယ်ပယ်ကို အခြေခံ၍)»)
- (Sadisaṃ) = (တူညီသည်) (ch. 5 sadisaṃ «တူညီသည်»)
- sahetukānaṃ (persons) = အမြစ် ရှိလျက် (ahetukānaṃ = အမြစ် မရှိဘဲ; as sa-X-ka «X ရှိလျက်», ch. 3)
- ñāṇasampayuttānaṃ (persons) = ဉာဏ်နှင့် ယှဉ်တွဲလျက် (ñāṇavippayuttānaṃ = ဉာဏ်နှင့် ကင်းကွာလျက်) (= 10-02 agent)
- somanassena upapajjantānaṃ = ဝမ်းမြောက်မှုနှင့်အတူ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့; upekkhāya … = ဥပေက္ခာနှင့်အတူ … (= sibling agents)
- itthīnaṃ upapajjantīnaṃ = ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့; purisānaṃ upapajjantānaṃ = ပြန်လည် ဖြစ်ပေါ်ဆဲ ယောက်ျားတို့
  (itthī / purisa = the head noun in place of «သူ»); Itarāsaṃ itthīnaṃ … = ပြန်လည် ဖြစ်ပေါ်ဆဲ အခြား မိန်းမတို့;
  Itaresaṃ purisānaṃ … = … အခြား ယောက်ျားတို့; Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ = ပြန်လည် ဖြစ်ပေါ်ဆဲ
  နောက်ဆုံး ဘဝ ရှိသော မိန်းမတို့ (= 10-10 agent)
- na itthīnaṃ / na purisānaṃ (before the participle) = မိန်းမ မဟုတ်ဘဲ / ယောက်ျား မဟုတ်ဘဲ: Sabbesaṃ cavantānaṃ na
  itthīnaṃ upapajjantānaṃ = စုတေဆဲသူ အားလုံးတို့နှင့် မိန်းမ မဟုတ်ဘဲ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့ (= 10-10 agent);
  Kāmāvacarā cavantānaṃ na purisānaṃ kāmāvacaraṃ upapajjantānaṃ = ကာမဘုံမှ စုတေဆဲသူတို့၊ ယောက်ျား မဟုတ်ဘဲ ကာမဘုံ၌
  ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့
- upapajjantīnaṃ (f.) = upapajjantānaṃ «ပြန်လည် ဖြစ်ပေါ်ဆဲ»; tāsaṃ / tāsaṃ tattha = ထိုသူတို့အား / … ထိုနေရာ၌
- eteneva bhāvena katici bhave dassetvā = ဤ အဖြစ်ဖြင့်ပင် ဘဝ အချို့ကို ဖြတ်သန်းပြီး
- relative clauses (sample GROUP_ATOMS pattern): Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti =
  ဤ အဖြစ်ဖြင့်ပင် ဘဝ အချို့ကို ဖြတ်သန်းပြီး ပရိနိဗ္ဗာန် ပြုမည့် ယောက်ျားတို့ (Yā itthiyo … = … မိန်းမတို့);
  … dassetvā somanassena upapajjitvā parinibbāyissanti = … ဖြတ်သန်းပြီး ဝမ်းမြောက်မှုနှင့်အတူ ပြန်လည် ဖြစ်ပေါ်ပြီး
  ပရိနိဗ္ဗာန် ပြုမည့် …; Ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti = မျက်စိ ရှိလျက် ဥပေက္ခာနှင့်အတူ ပြန်လည်
  ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့်သူတို့ (saghānakā «နှာခေါင်း ရှိလျက်»); ye ca somanassena rūpāvacaraṃ upapajjitvā … =
  ဝမ်းမြောက်မှုနှင့်အတူ သိမ်မွေ့သော ရုပ်ဘုံ၌ ပြန်လည် ဖြစ်ပေါ်ပြီး …; yā ca itthiyo rūpāvacaraṃ arūpāvacaraṃ upapajjitvā … =
  … ပရိနိဗ္ဗာန် ပြုမည့် မိန်းမတို့; inner «tesaṃ / tāsaṃ upapajjantānaṃ / upapajjantīnaṃ» after a relative =
  «…တို့အနက် ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့» (ch. 3 / ch. 5)
- X-sampayuttacitta / X-vippayuttacitta (X = somanassa, upekkhā, saddhā, ñāṇa) = Xနှင့် ယှဉ်တွဲသော / ကင်းကွာသော စိတ်;
  X-sampayuttapacchimacitta = Xနှင့် ယှဉ်တွဲသော နောက်ဆုံး စိတ်
- Yassa cittassa anantarā X-pacchimacittaṃ uppajjissati (a person group) = မိမိ စိတ်၏ ချက်ချင်း နောက်၌ X နောက်ဆုံး စိတ်
  ဖြစ်ပေါ်မည့်သူတို့ (ch. 6-8 frame «မိမိ စိတ်၏ …»)
- … yassa cittassa anantarā X-pacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe (a moment, correlative) =
  အကြင်စိတ်၏ ချက်ချင်း နောက်၌ X နောက်ဆုံး စိတ် ဖြစ်ပေါ်လိမ့်မည်၊ ထိုစိတ်၏ ဖြစ်ခြင်း ခဏ၌ (ch. 5 «အကြင်စိတ်၏ … ထိုစိတ်၏»)
- Pacchimacittassa / Somanassasampayuttapacchimacittassa uppādakkhaṇe (alone before tesaṃ) = … ခဏ၌ ရှိသူတို့အား
  (8-cittayamaka)
- Sabbesaṃ cittassa bhaṅgakkhaṇe X-vippayuttacittassa uppādakkhaṇe = သူ အားလုံးတို့၏ စိတ်၏ ပြိုပျက်ခြင်း ခဏ၌၊ Xနှင့်
  ကင်းကွာသော စိတ်၏ ဖြစ်ခြင်း ခဏ၌ (ch. 5 sabbesaṃ + moment; = 10-03 / 10-04 agent)

## For the consistency pass
1. Moment leads: 10-10 / 10-11 (ch10c) use the ch. 6-8 style («စိတ်၏ ပြိုပျက်ခြင်း ခဏ၌ ရှိသူ အားလုံးတို့၊ … ခဏ၌ ရှိသူတို့၊ …»;
   «… ဖြစ်ပေါ်မည့် စိတ်၏ ဖြစ်ခြင်း ခဏ၌ ရှိသူတို့»), while 10-01 … 10-04, ch. 5 and this group use the ch. 5 style
   («သူ အားလုံးတို့၏ စိတ်၏ ပြိုပျက်ခြင်း ခဏ၌၊ …»; final moment + «ထိုသူတို့အား»). 17 occurrences in 10-10 / 10-11.
2. «yassa cittassa anantarā» has two renderings by syntax: a person group «မိမိ စိတ်၏ ချက်ချင်း နောက်၌ … ဖြစ်ပေါ်မည့်သူတို့»
   (ch. 6-8) and the correlative with «tassa cittassa» «အကြင်စိတ်၏ … ၊ ထိုစိတ်၏ …» (ch. 5); 10-10 has a third
   («ချက်ချင်း နောက်၌ … ဖြစ်ပေါ်မည့် စိတ်၏ ဖြစ်ခြင်း ခဏ၌ ရှိသူတို့»).
3. A lone moment lead «… ခဏ၌ ရှိသူတို့အား» (8-citta) vs a moment closing a longer lead «… ခဏ၌ ထိုသူတို့အား» (ch. 5).

## Unsure Pāli / meaning
- eteneva bhāvena katici bhave dassetvā: «ဤ အဖြစ်ဖြင့်ပင် ဘဝ အချို့ကို ဖြတ်သန်းပြီး» (in this very state, i.e. as a man /
  woman, having gone through some existences); dassetvā («having shown») rendered by its meaning «ဖြတ်သန်းပြီး»
  (English rails «remaining men, will pass through several more existences»).
- somanassena / upekkhāya upapajjati «…နှင့်အတူ ပြန်လည် ဖြစ်ပေါ်» (reborn with joy / equanimity: the rebirth mind
  accompanied by it).
- itthī / purisa as the head noun («ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့») but na itthīnaṃ as an attribute («မိန်းမ မဟုတ်ဘဲ
  ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့», the beings reborn not as women).
- tāsaṃ «ထိုသူတို့အား» (no gender in the Burmese pronoun).
- «Suddhāvāsānaṃ upapajjantānaṃ asaññasattānaṃ» (^6-10-277; gen. place with the participle, elsewhere «Suddhāvāsaṃ
  upapajjantānaṃ»): the module reads it «သုဒ္ဓါဝါသ ဘုံ၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့» (as the acc. form).

## Source slips (translated as written or minimally; SLIPS / SLIPS_LEAD / NOTES in make_ch10b.py)
- 10-05 ^6-10-240 «Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ …» (tattha for tassa): kept «ထိုနေရာ၌».
- 10-05 ^6-10-256 «manindriyaṃ ca uppajj…» for manindriyañca (one «လည်း»).
- 10-06 ^6-10-301 «… itthindriyañca uppajjissati. Somanassindriyañca uppajjissati.» (a full stop inside one «ca … ca»
  sentence): two Burmese sentences, each «…လည်း ဖြစ်ပေါ်လိမ့်မည်။».
- 10-06 ^6-10-309 «no ca tesaṃ somanassindriyaṃ na upapajjissati» read as na uppajjissati («မဖြစ်ပေါ်လိမ့်မည်ကား မဟုတ်»).
- 10-06 ^6-10-314 «Pacchimacittasamaṅgīna» (missing ṃ); 10-08 ^6-10-361 «cavantāna» (missing ṃ).
- 10-06 ^6-10-318 «… na uppajjissati no ca tattha …» (no comma before no ca): Burmese «၊ သို့သော်» as everywhere.
- 10-08 ^6-10-336 «(Ghānandriyamūlakaṃ)» = Ghānindriyamūlakaṃ.
- 10-09 ^6-10-366 «(Sadisaṃ )» (stray space; Burmese «(တူညီသည်)»); 10-09 ^6-10-369 «uppajjissati, tassa» (stray comma).
