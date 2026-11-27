# pi-6 Burmese zero-shot, group ch10c: notes (10-10 … 10-13-indriyayamaka, end of the book)

Status 2026-11-22: all four files generated and checked. Not committed. Brief: burmese-zeroshot-brief.md.
Source rule kept: translated from the Pāli only; no Burmese translation / nissaya / web source opened
(0-INBOX/temp/language-priority/ not opened), no web search. pi-1 … pi-5 read only through their FINAL rails texts
(kwic6.py lookups, witnesses in the generator) and the locked termbases. English pi-6 rails read for meaning only
(eteneva bhāvena …, na itthīnaṃ, the pariññā persons); pi-6-mr notes-ch10c.md read for the frame inventory only (no
Marathi words). Finished groups' generators (make_ch3.py, make_ch2-02-4-5.py, make_ch6-8.py) read, never run or
imported; their functions copied / adapted. The sibling groups' outputs (ch9-10a, ch10b; done) and notes read only.

## Files
- Output (AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/): 10-10 (12 segments, 128 lines),
  10-11 (10 / 125), 10-12 (39 / 340), 10-13 (66 / 387). 10-10 / 10-11: paccuppannānāgatavāra (Gha) … (Ca); 10-12:
  atītānāgatavāra, «Pavattivāro niṭṭhito.», the Pariññāvāro heading; 10-13: the pariññāvāra in six tense vāras
  (anuloma / paccanīka), the chapter and book colophons (^6-10-482).
- `make_ch10c.py` (generator; imports my6_formulas.py unchanged, extends its tables in memory; `--misses`),
  `check_ch10c.py` (per-line check + reuse test; `--mutate` = mutation self-test).
- Run: `python3 -I -X utf8 make_ch10c.py` (writes the four files), `check_ch10c.py`, `check_ch10c.py --mutate`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all four files (my chk-pe copies deleted).
- check_ch10c.py: A 4/4 regenerated identical; B1 980 lines; B2 2139 negations, each one Burmese negative; B3 2864
  finite verbs in order (uppajj-, parijān-, pajah-, bhāv-, sacchikar-, paṭilabh-, parinibbāy-: tense, polarity, the
  «no ca … na V» double negative), 171 answers; B4 474 labelled lines, every «vā pana» = «တစ်ဖန်»; B5 267 numbers;
  B6 1345 distinct Pāli sentences, one Burmese each (3 slip lines not sentence-aligned, see below); B7 33 headings /
  colophons; 0 mismatches.
- Reuse 8050 / 8050: C1 the 22 faculty names (pi-2 ^2-219, read in the check independently) 2836/2836; C2 49 terms
  read from pi-1 … pi-5 / the sample / the finished groups 5156/5156; C3 person leads identical with the finished pi-6
  chapters (sample, ch2-02-4-5, ch3, ch6-8) 58/58 distinct leads, their majority rendering. Per chapter: 10-10
  1450/1450, 10-11 1801/1801, 10-12 3047/3047, 10-13 1752/1752. No documented exceptions.
- C4 (not counted): every lead shared with the sibling ch. 9 / 10 groups (9-01 … 10-09) agrees: 94/94 distinct leads
  (290 occurrences).
- Mutation test (--mutate): dropped «မ», dropped «ခဲ့», future -> present, dropped «ကား မဟုတ်», Āmantā -> No,
  dropped «တစ်ဖန်», faculty changed, pariññā polarity, bhāveti polarity, number, person, place: 12/12 caught.

## Method
- Faculties: `F.items("2", "^2-219")` (the pi-2 list, read at import: the 22 names in the pi-1 / pi-2 order, the same
  call as the sibling groups); added as subjects (`F.add_subject`); any surface form (…ṃ, …ñca, …nti) via `ind()`.
- Pavatti frames: the module's Q_PAV / A_BUT / A_BOTH first; this group's frames for «X-ñca … Y-ñca …», tāsaṃ (f.)
  and the comma-less «… no ca …» (A_BUT2, A_BOTH2). who_my: the module's own parse first (so every sample group is as
  the sample), else the lead parser (units = module person runs, this group's person phrases, relative clauses,
  moments). LEAD STYLE (= ch2-02-4-5 / ch. 5 and the sibling groups ch9-10a / ch10b): a moment is its own adverbial
  unit, units joined «၊ », a final moment + «ထိုသူတို့အား»; sabbesaṃ + moment «သူ အားလုံးတို့၏ …»; ONE moment alone
  «… ခဏ၌ ရှိသူတို့အား» (8 / 6-02); person units joined «A၊ Bနှင့် C» (module); inner «tesaṃ / tāsaṃ + participle»
  after a relative clause «…သူတို့အနက် …ဆဲသူတို့» (ch2-02-4-5 / ch3). Identical Pāli in 6-02 with the ch6-8 style
  («Pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ») keeps 6-02's Burmese (F.GROUP_ATOMS entry).
- Pariññā frames (from make_ch2-02-4-5.py): yo … so … question «အကြင်သူသည် Xကို V၏၊ ထိုသူသည် Yကို Vသလော။»; answers
  «Wသည် Xကို V1၊ သို့သော် Yကို (မ)V2(…ကား မဟုတ်)။» / «Wသည် Xကိုလည်း V1၊ Yကိုလည်း V2။»; «ကြ» after a plural subject.
- «…pe…» lines: each piece translated (first: clause + subject, middle: subject, last: subject + question verb,
  answers after «?»); one «…» per «…pe…» / «…Pe…».

## New recurring terms and frames («Pāli = Burmese»; witness = FINAL rails segment checked at import)
- the 22 faculties = pi-2 ^2-219 (e.g. cakkhundriyaṃ = မျက်စိ၏ စွမ်းရည်, anaññātaññassāmītindriyaṃ = မသိရသေးသည်ကို
  သိရတော့မည်ဟူသော စွမ်းရည်, aññindriyaṃ = အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည်, aññātāvindriyaṃ = အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်)
- (Xindriyamūlakaṃ) = (X၏ စွမ်းရည်ကို အခြေခံ၍) (ch3 pattern; = siblings); «(…)…pe….» = «(…)…။»; «(…).» = «(…)။»
- parijānāti = ပိုင်းခြား သိ (neg ပိုင်းခြား မသိ) (pi-5 ^5-317; ch2-02-4-5)
- pajahati = ပယ် (neg မပယ်) (pi-5 ^5-317; ch2-02-4-5)
- bhāveti = ပွားများ (neg မပွားများ) (pi-5 ^5-339; pi-1 / pi-2 termbase)
- sacchikaroti = မျက်မှောက်ပြု (neg မျက်မှောက် မပြု) (pi-5 ^5-194; neg pi-4 ^4-17)
- tenses as the module: pres «…သည် / …၏ / …သလော», past «…ခဲ့», fut «…လိမ့်မည် / …လိမ့်မည်လော»; sacchākāsi (aorist) = past
- Arahā = ရဟန္တာ (pi-4); arahantañca (ṭhapetvā) = ရဟန္တာ
- Aggamaggasamaṅgī = အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ (ch2-02-4-5)
- Anāgāmimaggasamaṅgī = အနာဂါမိမဂ်နှင့် ပြည့်စုံသူ (anāgāmimagga pi-5 ^5-339; -samaṅgī pi-2 ^2-809) (NEW)
- Anāgāmī = အနာဂါမ် (pi-4 ^4-M-7; = ch7a)
- Aṭṭhamako = အဋ္ဌမ ပုဂ္ဂိုလ် (pi-5 ^5-368; = ch7a)
- Dve / Tayo / Cattāro / Pañca / Cha / Satta / Aṭṭha puggalā = ပုဂ္ဂိုလ် နှစ် / သုံး / လေး / ငါး / ခြောက် / ခုနစ် / ရှစ်ယောက်တို့
  (counter «ယောက်» pi-4 ^4-M-8; «တို့» as ch7a 7-03)
- Tayo / Cattāro / Dve maggasamaṅgino = မဂ်နှင့် ပြည့်စုံသူ သုံး / လေး / နှစ်ယောက်(တို့) (NEW)
- X ṭhapetvā avasesā puggalā = Xကို ချန်ထား၍၊ ကြွင်းကျန်သော ပုဂ္ဂိုလ်တို့ (ch2-02-4-5); lists «Aနှင့် Bကို»
- Ye puthujjanā maggaṃ (na) paṭilabhissanti te = မဂ်ကို (မ)ရရှိမည့် ပုထုဇဉ်တို့ (ch2-02-4-5)
- Yo aggaphalaṃ sacchikaroti so = အမြတ်ဆုံး ဖိုလ်ကို မျက်မှောက်ပြုသူ(သည်); … sacchākāsi so = … မျက်မှောက်ပြုခဲ့သူ(သည်) (NEW)
- a variant bracket in a pariññā subject goes after «…သည်» (sample: after «…အား»), in a ṭhapetvā group after «…ကို»
- itthī / itthiyo / itthīnaṃ = မိန်းမ; purisa = ယောက်ျား (pi-2 ^2-219 names)
- Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ = ပြန်လည် ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသော မိန်းမတို့ (= ch10b);
  … purisānaṃ upapajjantānaṃ = … ယောက်ျားတို့; Pacchimabhavikānaṃ saghānakānaṃ upapajjantānaṃ = နှာခေါင်း ရှိလျက် ပြန်လည်
  ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသူတို့
- na itthīnaṃ / na purisānaṃ (+ participle) = မိန်းမ မဟုတ်ဘဲ / ယောက်ျား မဟုတ်ဘဲ (= ch10b)
- sa-X-ka / a-X-ka = X ရှိလျက် / X မရှိဘဲ (ch3 / ch2-02-4-5): sacakkhukā, saghānakā, acakkhukānaṃ, aghānakānaṃ
- upapajjantīnaṃ / cavantīnaṃ (f.) = as upapajjantānaṃ / cavantānaṃ; tāsaṃ = ထိုသူတို့(အား) (= ch10b; ch9-10a has
  «ထိုမိန်းမတို့»)
- (ye|yā) ca [purisā|itthiyo] [sa-X-kā] [somanassena|upekkhāya|places] upapajjitvā parinibbāyissanti = [X ရှိလျက်]
  [ဝမ်းမြောက်မှုနှင့်အတူ|ဥပေက္ခာနှင့်အတူ|X၌] ပြန်လည် ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့် [ယောက်ျား|မိန်းမ]တို့ / …သူတို့
  (sample GROUP_ATOMS pattern; somanassa-sahagata «ဝမ်းမြောက်မှုနှင့်အတူ» pi-1 ^1-147; = siblings)
- (ye|yā) ca (purisā|itthiyo) eteneva bhāvena katici bhave dassetvā parinibbāyissanti = ဤ အဖြစ်ဖြင့်ပင် ဘဝ အချို့ကို
  ဖြတ်သန်းပြီး ပရိနိဗ္ဗာန် ပြုမည့် ယောက်ျား / မိန်းမတို့ (NEW; = siblings)
- tesaṃ / tāsaṃ cavantānaṃ / upapajjantānaṃ (after a relative) = …သူတို့အနက် စုတေဆဲ / ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့
- X-vippayuttacittassa = Xနှင့် ကင်းကွာသော စိတ်၏ (ñāṇa ဉာဏ် pi-1 ^1-147, saddhā ယုံကြည်မှု, somanassa ဝမ်းမြောက်မှု,
  upekkhā ဥပေက္ခာ); X-sampayuttapacchimacittassa = Xနှင့် ယှဉ်တွဲသော နောက်ဆုံး စိတ်၏
- X-sampayuttapacchimacittasamaṅgīnaṃ = Xနှင့် ယှဉ်တွဲသော နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူတို့; Pacchimacittasamaṅgīnaṃ =
  နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူတို့ (5-01)
- yassa cittassa anantarā X-pacchimacittaṃ uppajjissati (persons) = မိမိ စိတ်၏ ချက်ချင်း နောက်၌ X နောက်ဆုံး စိတ်
  ဖြစ်ပေါ်မည့်သူတို့ (ch6-8; = ch10b)
- … uppajjissati tassa cittassa uppāda- / bhaṅgakkhaṇe (moment) = အကြင်စိတ်၏ ချက်ချင်း နောက်၌ X နောက်ဆုံး စိတ်
  ဖြစ်ပေါ်လိမ့်မည်၊ ထိုစိတ်၏ ဖြစ်ခြင်း / ပြိုပျက်ခြင်း ခဏ၌ (ch. 5 correlative; = ch10b)
- Sabbesaṃ cittassa bhaṅgakkhaṇe X-vippayuttacittassa uppādakkhaṇe = သူ အားလုံးတို့၏ စိတ်၏ ပြိုပျက်ခြင်း ခဏ၌၊ X…
  ဖြစ်ခြင်း ခဏ၌ (5-01; = siblings)
- pavatte cittassa bhaṅgakkhaṇe = ဘဝ တည်နေစဉ် စိတ်၏ ပြိုပျက်ခြင်း ခဏ၌ (5-0x); dutiye citte vattamāne = ဒုတိယ စိတ်
  ဖြစ်နေစဉ် (5-01)
- kāmāvacara / rūpāvacara / arūpāvacara (places) = ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ (ch3 / ch6-8)

## Headings and colophons
- (6) Atītānāgatavāro and the vāra / naya / puggala / okāsa headings: module H (sample).
- Pariññāvāro = ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက် (= 2-02 / 5-03); colophon «Pariññāvāro.» = «ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက်။»
- Pavattivāro niṭṭhito. = “ဖြစ်ပျက်ခြင်းအလိုက် ဖော်ပြချက်” ပြီးဆုံးပြီ။ (= 2-02 / 3-06 / 5-03)
- Indriyayamakaṃ niṭṭhitaṃ. = “စွမ်းရည်များကို အတွဲလိုက် မေးဖြေခြင်း” ပြီးဆုံးပြီ။ (module COLO, chapter name as proposed)
- Yamakapakaraṇaṃ niṭṭhitaṃ. = “အတွဲလိုက် မေးဖြေခြင်း” ကျမ်း ပြီးဆုံးပြီ။ (book colophon: the pi-1 … pi-5 pattern
  «“X” ကျမ်း ပြီးဆုံးပြီ။», e.g. pi-2 ^2-1044; NEW)

## For the consistency pass
1. Lead style: mine follows ch2-02-4-5 / ch. 5 and the siblings (moment = adverbial unit); 6-02 / 8 (ch6-8) use «…
   ခဏ၌ ရှိသူတို့» before persons. The one identical lead («Pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ», 10-11
   ^6-10-402 / ^6-10-403) keeps 6-02's «နောက်ဆုံး စိတ်၏ ပြိုပျက်ခြင်း ခဏ၌ ရှိသူတို့နှင့် အသညသတ်တို့»; the similar «Pacchimacittassa
   uppādakkhaṇe asaññasattaṃ upapajjantānaṃ» keeps the sibling style «…ခဏ၌၊ အသညသတ် ဘုံ၌ …». The finished groups
   disagree on the lone lead «Pacchimacittassa bhaṅgakkhaṇe tesaṃ» (13 «ရှိသူတို့အား» vs 2 «ထိုသူတို့အား»): majority taken.
2. «tesaṃ cavantānaṃ» after a relative: «အနက်» (ch2-02-4-5 / ch3 / siblings) vs ch6-8 «ထဲမှ».
3. tāsaṃ: «ထိုသူတို့» (mine, ch10b) vs «ထိုမိန်းမတို့» (ch9-10a).
4. Counted persons with «တို့» («ပုဂ္ဂိုလ် နှစ်ယောက်တို့သည်», ch7a); pi-4 has the bare «ပုဂ္ဂိုလ် နှစ်ယောက်» (a heading).

## Unsure Pāli / meaning
- eteneva bhāvena katici bhave dassetvā = «ဤ အဖြစ်ဖြင့်ပင် ဘဝ အချို့ကို ဖြတ်သန်းပြီး» (in this very state, i.e. as a man /
  as a woman, going through some existences; dassetvā «showing» given by its sense «ဖြတ်သန်း»), as the English rails.
- The scope of «tesaṃ cavantānaṃ» after several groups is kept on the last group only (as ch2-02-4-5 / ch3).
- sabbesaṃ before two moments is applied to the first only («သူ အားလုံးတို့၏ M1၊ M2»), as 5-01.
- Aṭṭhamako «အဋ္ဌမ ပုဂ္ဂိုလ်» (the eighth person, on the first path) is left as the name the earlier books use.
- «Tayo maggasamaṅgino ca arahantañca ṭhapetvā» = «မဂ်နှင့် ပြည့်စုံသူ သုံးယောက်နှင့် ရဟန္တာကို ချန်ထား၍»; the counted group
  in a ṭhapetvā list has no «တို့».

## Source slips (translated as written)
- ^6-10-393 (10-10) «… no ca tesaṃ manindriyaṃ na uppajjissati pacchimacittassa bhaṅgakkhaṇe tesaṃ …» (no «.»): two
  Burmese sentences.
- ^6-10-387, ^6-10-452, ^6-10-477 «… no ca …» without the comma: the same Burmese as with it.
- ^6-10-398 (10-11) «Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ» (for upapajjantānaṃ): «ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသော
  ယောက်ျားတို့» (arising), as written.
- ^6-10-452 (10-13) «…, pañca puggalā aññindriyañca bhavissanti …»: a missing «.», and «bhavissanti» (will be) with an
  object, read as bhāvessanti «ပွားများကြလိမ့်မည်»; two Burmese sentences.
- ^6-10-468 (10-13) «… pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.» (no «.»,
  stray comma, plural verbs with a singular subject): two Burmese sentences, the verbs singular after the subject.
- ^6-10-477 (10-13) «(Kha) yo vā pana aññindriyaṃ bhāvessati. So anaññātaññassāmītindriyaṃ bhāvitthāti?» (a «.» inside the
  question): «… ပွားများလိမ့်မည်။ ထိုသူသည် … ပွားများခဲ့သလော။».
- ^6-10-455 (10-13) two questions end with «.» for «?»: rendered as questions.
- ^6-10-480 (10-13) «nappajjahittha» = nappajahittha (past, negative).
- ^6-10-482 «(Aññindriyamūlakaṃ).» with a «.»: «(…ကို အခြေခံ၍)။».
