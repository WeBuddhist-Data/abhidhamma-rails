# pi-6 Burmese zero-shot (Yamaka «အတွဲလိုက် မေးဖြေခြင်း»): consistency pass — notes

Brief: harmonise-brief.md; items: harmonise-todo.md (A1–A4, B1–B18). 2026-11-22. Not committed.
Backups (before any edit): harmonise-backup/ (all .py of pi-6-my and my6-zeroshot-terms.md) and
harmonise-backup/chapters/ (the 44 chapter files). Baseline: the nine generators rebuilt the 44 files byte-identical to
the backup before any change (regen_zeroshot.sh, first run). align-before.txt / align-hidden-before.txt saved from that
state (659 repeated sentences, 2 differing; hidden 0 unmatched).
Every change is made in a generator (comment «harmonise A… / B…»), never by hand in a chapter file; my6_formulas.py was
not changed (no shared string needed a change; the sample strings stay as approved). Import chains checked:
every generator imports my6_formulas only; make_ch7b imports make_ch7a (read-only tables); the checks import their
generator (check_sample → make_sample, check_ch3 → make_ch3, check_ch7a/7b → make_ch7a/7b, the others by importlib).
Rebuild + all checks: regen_zeroshot.sh (run twice: the second run changed no byte, see the end).

## Progress log
- [x] backups, baseline, align before
- [x] A1, A2, A3, A4; B1, B3, B4, B5, B6, B15, B16; the rest verified (no change)
- [x] checks updated where a form changed on purpose (check_ch3, check_ch6-8, check_ch10b, check_ch10c; listed below)
- [x] harmonise_pi12345.py, harmonise_scan.py (+ harmonise-table.tsv), harmonise_diff.py, harmonise_align_explained.py
- [x] regen_zeroshot.sh run twice, no byte changed by the second run

## Part A (source as written)

### A1 abhisametāvī / anabhisametāvī
- Chosen: «ထင်ထင်ရှားရှား သိမြင်ပြီးသူတို့» / «ထင်ထင်ရှားရှား မသိမြင်ရသေးသူတို့» (no «သစ္စာကို»).
- Reason: the Pāli has no saccaṃ; no locked pi-1 … pi-5 termbase entry has it (pi-4 / pi-5 abhisamaya «ထင်ထင်ရှားရှား
  သိမြင်ခြင်း», pi-5 abhisameti «ထင်ထင်ရှားရှား သိမြင်»).
- Changed: make_ch2-02-4-5.py (ABHI, ANABHI). 30 lines (5-01, 5-02).

### A2 quote marks
- anaññātaññassāmīti (bare word, 10-01 / 10-02): no quote marks (the Pāli has none) — chosen «မသိရသေးသည်ကို
  သိရတော့မည်ဟူသော အရာ» = the pi-1 / pi-2 faculty name «မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည်» without «စွမ်းရည်»,
  with «အရာ» (the «…ဟူသော» form needs a noun, as ch9-10a's bare abyākatā «… မဟုတ်သော အရာများ»). Changed: make_ch9-10a.py
  (BARE_MY). 30 lines.
- Kept (checked): the sota pun «“သောတ” (နား သို့မဟုတ် ရေစီး)» (B7: the word cited as a word, coordinator); the colophon
  titles «“X” ပြီးဆုံးပြီ။» (style rule: a title mid-sentence in quotes); in the editorial notes the cited question parts
  «“အကြင်သူအား” အပိုင်း» … and cited answers «“ဟုတ်ပါသည်” ဟု ဖြေရမည်», «“မဟုတ်ပါ” ဟု မဖြေရ» (Pāli «-ti» cites the
  word, as the sota pun; no pi-1 … pi-5 precedent for these notes). The Pāli quotes of 7-09 / 7-10 («"pahīno"ti …») are
  rendered as quotes (counts equal on every line).

### A3 source slips (every group's SLIPS / notes checked)
- One rule: translated as written; the evident word only where the spelling alone slipped (a letter); no corrections of
  the Pāli's wording, number or punctuation.
- Changed: ch10c ^6-10-398 «Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ» (was «ဖြစ်ပေါ်ဆဲ», "arising") now read as
  upapajjantānaṃ «ပြန်လည် ဖြစ်ပေါ်ဆဲ» like the same one-letter slips elsewhere (ch3 ^6-3-212 upapajjissati, ch9-10a
  ^6-10-206 uppajjantīnaṃ, ch10b ^6-10-309 upapajjissati: the parallel lines show the word). 1 line (10-11).
- Changed (reverted corrections): ch10c had made plural Pāli verbs singular after a singular subject — ^6-10-454
  «Aggamaggasamaṅgī aññātāvindriyaṃ sacchikarissanti, no ca aññindriyaṃ bhāvessanti», ^6-10-468 «anāgāmimaggasamaṅgi
  aññindriyañca bhāvessanti, domanassindriyañca pajahanti», 10-13 «Aggamaggasamaṅgī … pajahittha … parijānanti»,
  ^6-10-388 (10-10) «tesaṃ itthindriyaṃ na uppajjissanti»: now as written, «ကြ» (also B5). make_ch10c.py (PV, but_my, VP).
- Kept, as logged by the groups (spelling-only or evident word): kāmārāga-, anusanti, ariyāpanne, Pajahanā-,
  Dhātuvisajja-, upapattināma (ch7a / ch7b); vadanā-, jivha, paṭilabhissānti, asaññattā, nirujjhiti (ch2-02-4-5);
  sotāyanan-, parinibbānt-, tasaṃ, «=93» kept, doubled «ca ca» one «လည်း» (ch3); vītakkantaṃ, Uppajjamānananirodha-,
  paccanīkaokāsā (ch6-8); viriyindiyaṃ, anaññātaññāssāmīti (ch9-10a); Ghānandriya-, -samaṅgīna, cavantāna (ch10b);
  nappajjahittha, bhavissanti read bhāvessanti (with an object; the evident word), sacchākāsi (ch10c). The «na» for «ca»
  of ^6-6-121 and every missing «ca» (ch2-02-4-5, ch3) stay as written.

### A4 punctuation («၊» / «။» only where the Pāli has «,» / «.», besides the approved frames)
- ^6-3-1 list «sotāyatanaṃ ghānāyatanaṃ» (no comma): no «၊» (ch3 P_LIST builds «၊» only after a Pāli «,»). 1 line.
- ^6-5-1 list «samudayasaccaṃ nirodhasaccaṃ»: no «၊» (make_ch2-02-4-5.py LINES). 1 line.
- A statement «… V no ca …» without the Pāli comma: no «၊» before «သို့သော်» (as ch7a / ch9-10a already did):
  ch10b ^6-10-318 (10-06), ch10c 10-10 ^6-10-387, 10-13 ^6-10-452 / ^6-10-477, ch6-8 8 (14) «… avītikkantaṃ no ca …»
  (2 lines). make_ch10b.py (pavatti), make_ch10c.py (ch10_sentence), make_ch6-8.py (SENT).
- A sentence end without the Pāli «.»: no «။» (ch10c add_slip now takes the Pāli mark after each part): ^6-10-393
  «… na uppajjissati pacchimacittassa …» (joined with a space), ^6-10-452 «… pajahissanti, pañca puggalā …» («၊»),
  ^6-10-468 «… pajahanti anāgāmimaggasamaṅgi …» (space). 3 lines.
- 7-08 the stray «,» of «kāmadhātuyā tīsu vedanāsu, apariyāpanne» kept as «၊» (was dropped; make_ch7b.py body()).
- 8 ^6-8-115 «Yassa vā pana…pe…? Āmantā …pe….»: «…လော။ ဟုတ်ပါသည် …။» (no «။» added after Āmantā; ch7a / ch9-10a
  form); make_ch6-8.py fragment().
- Kept (frame): the yassa-clause break «…၏၊ / …၊» of the sample's question frame, also in the ch8 (11) questions
  «yassa cittaṃ uppajjittha no ca tassa …, tassa …?» (the Pāli never has a comma after the yassa clause; the frame
  «၊» is the approved sample typography); the «၊» between «…လည်း V၊ …လည်း V» members; ṭhapetvā «…ကို ချန်ထား၍၊».
- Scan (scratch/stops.py): every line now has as many «။» as the Pāli has «.» / «?» (outside brackets, «…pe…» folded).

## Part B (one form per item book-wide)

### B1 moment leads — the ch. 5 style
- Chosen: a moment phrase is its own adverbial unit «GEN၏ ဖြစ်ခြင်း / ပြိုပျက်ခြင်း ခဏ၌» («… စိတ် ဖြစ်နေစဉ်»); units
  joined «၊ » (consecutive person groups «A၊ Bနှင့် C»); sabbesaṃ + moment «သူ အားလုံးတို့၏ M»; itaresaṃ + moment
  «အခြားသူတို့၊ M» (ch9-10a); a final moment, also a lead that is one moment alone, + «ထိုသူတို့အား».
- Reason: harmonise-todo B1 (ch2-02-4-5, ch9-10a, ch10b, ch10c). Before, identical Pāli had two Burmese leads
  («Pacchimacittassa bhaṅgakkhaṇe tesaṃ» 21 «… ခဏ၌ ရှိသူတို့အား» vs 14 «… ခဏ၌ ထိုသူတို့အား»; «Sabbesaṃ cittassa
  bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ»), and ch6-8 fused moments with the person group before or
  after them («… ခဏ၌ ကာမဘုံ၌ ရှိသူတို့», «M ရှိသူ အားလုံးတို့», «M ရှိသော အခြားသူတို့»).
- Changed: make_ch6-8.py (units_of / join_units / group_my), make_ch10b.py (no lone-moment exception), make_ch10c.py
  (no lone-moment exception; the whole-lead atom «pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ» removed).
  Lines: 6-01 84, 6-02 111, 8 32 (with the B15 notes), 10-09 19, 10-10 / 10-11 (with B3).
- Check: harmonise_scan.py B1 lead test: 1338 distinct Pāli leads, 0 with two Burmese (before 2); «ခဏ၌ ရှိသူ» 0
  (before 162).

### B2 uppādakkhaṇe / bhaṅgakkhaṇe
- «ဖြစ်ခြင်း ခဏ» / «ပြိုပျက်ခြင်း ခဏ» (pi-5 ^5-366) in every group (959 / 856 uses); the vāra headings uppāda
  «ဖြစ်ပေါ်ခြင်း» (sample). Nothing to change.

### B3 tāsaṃ (fem., after itthīnaṃ …)
- Chosen: «ထိုမိန်းမတို့(အား)» (after a final moment, «no ca tāsaṃ», «tāsaṃ tattha»); a lead ending with the women group
  keeps «… မိန်းမတို့အား». Changed: make_ch10b.py, make_ch10c.py (ch9-10a had it). 35 uses changed (61 lines now).

### B4 «ye ca … tesaṃ cavantānaṃ / upapajjantānaṃ»
- Chosen «…တို့အနက်» (majority). Changed: make_ch6-8.py (AMONG «ထဲမှ» → «အနက်»), 12 uses.

### B5 plural «ကြ»
- Rule: «ကြ» where the Pāli finite verb is plural (-nti / -issanti / -essanti), never where it is singular (-ti /
  -issati / -essati / -āsi), also against the subject in a slip (A3); the number-neutral -ittha (used in the Yamaka
  with singular and plural subjects: «rūpakkhandho uppajjittha», «kusalā dhammā uppajjittha») takes the subject's
  number — so ch9-10a's Dhammayamaka «ဖြစ်ပေါ်ခဲ့ကြ», «ချုပ်ငြိမ်းခဲ့ကြ» and the plural -ittha of 2-02 / 3-06 / 5-03 / 10-13
  stay; bare short answers keep the number of their verb form (Uppajjittha. «ဖြစ်ပေါ်ခဲ့သည်။», sample). Nominal
  sentences (no verb) keep the sample's plural predicates.
- Changed: make_ch10c.py (PV / but_my: the verb's own ending; VP for the pavatti frames). 5 lines (10-10, 10-13).
- Check: harmonise_scan.py B5 test on 5116 verb sentences: 0 outside the rule (before 3).

### B6 «ထိုသူတို့ပင်နှင့်» (tesaṃyeva + moment, ch6-8)
- Chosen «ထိုသူတို့၏ပင် M» (ch. 5 inner «tesaṃ + moment» «ထိုသူတို့၏ M»; eva «ပင်» after the case as ch7a «Tesaññeva
  puggalānaṃ» «ထိုပုဂ္ဂိုလ်တို့အားပင်»). No other group has tesaṃyeva. make_ch6-8.py. 15 lines (20 uses).

### B7 sota pun
- «“သောတ” (နား သို့မဟုတ် ရေစီး)» in all 8 lines (3-01, 4, 10-01), subject «နတ်နားနှင့် တပ်မက်မှု ရေစီးတို့သည်». No change.

### B8 planes as places
- kāmāvacara / kāmadhātu «ကာမဘုံ», rūpāvacara / rūpadhātuyā «သိမ်မွေ့သော ရုပ်ဘုံ», arūpāvacara / arūpa / arūpadhātu
  «ရုပ်မရှိသော ဘုံ» in every group; adjectival kāmāvacara (of citta) «ကာမဘုံနှင့် ဆိုင်သော» (pi-1 ^1-1). rūpadhātu of the
  dhātu list (ch. 4) is the visible-form element «အဆင်းအရောင် ဓာတ်» (pi-2), another sense. No change.

### B9 person types and attributes (verified, one form each)
- sa-X-ka / a-X-ka «X ရှိလျက် / X မရှိဘဲ»; sahetuka / ahetuka (persons) «အမြစ် ရှိလျက် / မရှိဘဲ» (pi-1 Mātikā sense;
  hetu «အကြောင်း» stays only in the hetuvāra list, the sample's approved departure: different sense, logged);
  ñāṇasampayutta / -vippayutta «ဉာဏ်နှင့် ယှဉ်တွဲလျက် / ကင်းကွာလျက်»; somanassena / upekkhāya «…နှင့်အတူ» (vinā …
  «… မပါဘဲ»); na itthīnaṃ / na purisānaṃ «… မဟုတ်ဘဲ»; the women frame «… မိန်းမတို့»; -samaṅgī «…နှင့် ပြည့်စုံသူ»;
  nirodhasamāpanna «ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ» (pi-5); Aggamaggasamaṅgī «အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ»;
  Aṭṭhamaka «အဋ္ဌမ ပုဂ္ဂိုလ်» (pi-5); Anāgāmī «အနာဂါမ်» (pi-4). No change.

### B10 «yassa cittassa anantarā»
- Three renderings, each = one Pāli syntax (survey scratch/anantara.py: every identical Pāli has one Burmese):
  (a) a person group with the last mind as subject «… pacchimacittaṃ uppajjissati» (yassa = whose) «မိမိ စိတ်၏ ချက်ချင်း
  နောက်၌ … ဖြစ်ပေါ်မည့်သူတို့»; (b) persons as subject «… aggamaggaṃ paṭilabhissanti» «အကြင်စိတ်၏ ချက်ချင်း နောက်၌ …
  ရရှိမည့်သူတို့»; (c) the correlative with «tassa cittassa M» «အကြင်စိတ်၏ … ၊ ထိုစိတ်၏ M». The third 10-10 rendering of
  the todo («… ဖြစ်ပေါ်မည့် စိတ်၏ ဖြစ်ခြင်း ခဏ၌ ရှိသူတို့») is gone with B1. No generator change for B10.

### B11 the 22 faculties, the seven anusayas, khandha / āyatana / dhātu / sacca names and bare words
- = pi-1 / pi-2 final in every group (agents' C1 tests n / n; harmonise_pi12345 identical). No change.

### B12 headings, vāra / naya / uddesa / niddesa names, colophons, notes, chapter names, book end
- 155 distinct heading / colophon Pāli lines, each one Burmese (harmonise_scan B12 test); mahāvāra «ဖော်ပြချက်ကြီး»;
  paṭiloma = paccanīka «အငြင်းပြ ပုံစံ»; chapter names «Xများကို အတွဲလိုက် မေးဖြေခြင်း» (Cittayamaka «စိတ်ကို …», the
  module's singular topic); colophons «“X” ပြီးဆုံးပြီ။»; book end «“အတွဲလိုက် မေးဖြေခြင်း” ကျမ်း ပြီးဆုံးပြီ။»;
  «(Xmūlakaṃ)» «(Xကို အခြေခံ၍)» in ch3 / ch7a / ch7b / ch9-10a / ch10b / ch10c. No change.

### B13 pariññā / bhāvanā verbs
- parijānāti «ပိုင်းခြား သိ» (neg. «ပိုင်းခြား မသိ»), pajahati «ပယ်» («မပယ်»), bhāveti «ပွားများ» («မပွားများ»),
  sacchikaroti «မျက်မှောက်ပြု» («မျက်မှောက် မပြု», pi-4 ^4-17) in every tense, «ကြ» before «လိမ့်မည်», after «ခဲ့». No change.

### B14 unsure readings (no group differs)
- yato / tato «အကြင်နေရာ၌ / ထိုနေရာ၌», tadekaṭṭhaṃ, sakkāya «ကိုယ်» (ch7a; ch7b imports ch7a's tables); dassetvā
  «ဘဝ အချို့ကို ဖြတ်သန်းပြီး» (ch10b = ch10c); avaseso kāyo «ကြွင်းကျန်သော အရာသည် ကိုယ်» (ch. 3 / 4 / 10-01). No change.

### B15 the align_check / align_hidden items and the note vocabulary
- align_check before: 2 differing sentences — «(Kha) yassa vā pana yattha…pe…?» (ch6-8 «…။» vs «…လော။») and «(Yassakampi
  yassayatthakampi sadisaṃ).» (3-05 vs 5-02). Both aligned; after: 0. align_hidden: 0 before, 0 after.
- A question cut before its verb «…pe…?» = «…လော။» (ch3 / ch2-02-4-5 / ch7a): make_ch6-8.py fragment(); 38 lines.
- The editorial notes, one vocabulary (ch3 / ch2-02-4-5, the majority): yassaka / yatthaka / yassayatthaka «“အကြင်သူအား”
  / “အကြင်နေရာ၌” / “အကြင်သူအား အကြင်နေရာ၌” အပိုင်း» (ch6-8 had «“အကြင်သူ” မေးခွန်း» …); «(yassakampi yassayatthakampi
  sadisaṃ)» «(Aလည်း၊ Bလည်း တူညီသည်)» (ch2-02-4-5 ×3; ch3 and ch6-8 aligned); sadisaṃ «တူညီသည်» (ch6-8 «တူသည်»);
  ekasadisaṃ «တစ်ထပ်တည်း တူညီ»; vibhajitabbaṃ «ခွဲခြား ပြရမည်», vibhatta «ခွဲခြား ပြထားသကဲ့သို့» (ch6-8 «ခွဲခြား
  ဖော်ပြ…»); pucchā «အမေး» (pi-5 ^5-652; ch6-8 «မေးခွန်း»); itaresaṃ (in a note) «အခြား»; «X-nti na kātabbaṃ» «“X”ဟု
  မပြုရ» (ch6-8 «…ဟူသော စကားကို မထည့်ရ»), «… na labbhati» «…ဟူသော စကားကို မရ»; the cited nirodhasamāpannānaṃ with
  «အား» as in ch2-02-4-5; «(Yassa yatthakampi sadisaṃ vitthāretabbaṃ)» (3-04) = ch2-02-4-5's wording. make_ch6-8.py,
  make_ch3.py.
- saṃkhittaṃ (note) «အကျဉ်းချုပ်» = pi-5 «(Saṃkhittaṃ).» «(အကျဉ်းချုပ်)။» (pi-1 … pi-5 identity; was «အကျဉ်း ဖော်ပြထားသည်»):
  make_ch3.py (2 notes), make_ch2-02-4-5.py (4 ^6-4-…). The vārasaṅkhepo note keeps «အကျဉ်း ဖော်ပြထားသည်» (another word).

### B16 (vitthāretabbaṃ)
- Chosen «(အကျယ် ချဲ့ရမည်)» (pi-5 ^5-839; ch3, ch2-02-4-5, ch7b); make_ch6-8.py (VITTHAR). 3 uses.

### B17 cavati / cuta
- «စုတေ» book-wide (1091 uses); pi-5 ^5-65 «သေ၍» has no identical pi-6 sentence. No change.

### B18 Uppajjanavāro = Uppādavāro
- Uppajjanavāro occurs only in 7-09 (with its colophon), which has no Uppādavāro: one form «ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်».

## Checks updated on purpose (expected Burmese changed with the form)
- check_ch3.py B7 list line: «၊» only after a Pāli «,» (A4).
- check_ch6-8.py B3 / C2 Āmantā: «Āmantā …pe….» = «ဟုတ်ပါသည် …» (A4); m_neg counts «မပြုရ» (B15 note wording).
- check_ch10b.py B10: the pronoun tāsaṃ «ထိုမိန်းမတို့» counted apart from the head noun itthī (B3).
- check_ch10c.py C2: same for tāsaṃ (B3); «upapajjant» also counts the slip «uppajjantānaṃ» (A3).

## pi-1 … pi-5 identity (harmonise_pi12345.py)
- pi-1 10 / 10, pi-2 14 / 14, pi-3 10 / 332 + 322 explained (Natthi «မရှိပါ။», the sample's answer register), pi-4 10 / 10,
  pi-5 2791 / 2791 (before the pass 2790: «(Saṃkhittaṃ).»). The other approved departures (anuloma / paccanīka, hetu in
  the hetuvāra list, cavati «စုတေ») never meet an identical pi-1 … pi-5 sentence, so none is counted; they stay listed as
  exceptions in the agents' checks.
