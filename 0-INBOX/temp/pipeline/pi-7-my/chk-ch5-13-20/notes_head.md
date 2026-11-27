# pi-7 part 5, 5-13 … 5-20 (the mixed orders anulomapaccanīya / paccanīyānuloma): Burmese zero-shot notes

PROGRESS: DONE (2026-11-24). Written to AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/:
5-13-anulomapaccaniya-tikatika.md, 5-14-anulomapaccaniya-dukaduka.md, 5-15-paccaniyanuloma-tika.md,
5-16-paccaniyanuloma-duka.md, 5-17-paccaniyanuloma-dukatika.md, 5-18-paccaniyanuloma-tikaduka.md,
5-19-paccaniyanuloma-tikatika.md, 5-20-paccaniyanuloma-dukaduka.md (the last chapter of the book).
(Check results: see the end of this file.)

## Files
- make_ch5-13-20.py: generator. It IMPORTS the finished part-5 group make_ch5-01-04.py as Q (read-only; Q's
  setup() runs on import, its main() never runs; Q loads its own engines, world A = make_ch3-09.py and world B =
  make_ch4-01.py, on their own copies of my7_formulas / make_sample). Q's atoms, na-X rule, chain rewrite («A၊ B N»),
  notes renderer, headings and numbers are used as they are; this script only adds things in memory (listed below).
  No file of the sample or of another group is edited; no other group's main block runs.
  `--dev` (chk-ch5-13-20/dev[-<ch>].txt), `--dump`, `--slips`, `--out DIR`; one chapter per call is fine
  (the chapters are independent; chk-ch5-13-20/runall.sh runs them in parallel). Each run writes its log
  chk-ch5-13-20/new-<ch>.txt (new strings, negated atoms, term chains, slips), merged below.
- check_ch5-13-20.py: checker (from check_ch5-01-04.py: S/C/O/P/N/I/T/R; plus its own table NOTE_TERMS of the terms
  the hand-written notes and sentences name, the R2 test of combined terms against the finished chapters, the pi-1
  FINAL rails text as an extra witness; `--mutate` runs 14 planted errors in parallel, `--pe`, `--groups`).
- chk-ch5-13-20/: scratch (dev output, logs, probes).

## How the chapters are run
- A chapter is cut at its part headings. A part heading is any h5 / h6 heading whose words name triads / dyads:
  «1-1. Kusalattika-vedanāttikaṃ», «2-4-1. Sahetukādidukāni-kusalattikaṃ», «1-19-53. Hetuduka-saññojanādigocchakaṃ»,
  «Kusalattikaṃ», «20-54. Saññojanādichagocchakāni» … (other headings, «1-7. Paṭiccavārādi», «Paccanīyaṃ»,
  «Akusalapadaṃ», stay inside the part).
- A part runs with the positive AND the negated atoms of its triads / dyads (the mixed orders have both on one
  line: «Kusalaṃ sukhāya … paṭicca nakusalo nasukhāya …», «Nahetuṃ nakusalaṃ … paccayā hetu kusalo …»). A dyad
  brings its whole cluster (the negated «ceva» dyads are written with the cluster's other terms, as in 5-04).
- The range of a group word: «-dvaya» = the triad and the next one; «-ādi» / «-āni» / «-gocchaka» = from the named
  triad / dyad to the end of the range the heading's numbers give (the numbers are read relative to the named item:
  «1-19-53. … saññojanādigocchakaṃ» = dyads 20 … 54), else to the end of its group (hetu 1-6, cūḷantara 7-13,
  āsava 14-19, saññojana … parāmāsa 20-54, mahantara 55-68, upādāna 69-74, kilesa 75-82, piṭṭhi 83-100).
- Two-set chapters (tikatika, dukaduka, dukatika, tikaduka) run as 5-01 / 5-02 (two terms on one noun stacked
  «A၊ B N»; a «ceva» term followed by a term stacks with it); the one-set chapters 5-15 / 5-16 run as 5-03 / 5-04
  (every atom also alone, before a noun or coordinated).
- The dukatika / tikaduka terms: Q's stacking gives «<dyad term>၊ <triad term>» = the 4-02 … 4-14 combined terms
  (checked: R2 566 / 566 combined terms identical with the finished chapters, 5-01 … 5-04 and 4-02 … 4-14 among
  them); the tikaduka terms (4-15 … 4-21 still in progress) are the same stacking, triad first («<triad>၊ <dyad>»).
- The na-X rule is Q's, unchanged («…သော» → «…သည် မဟုတ်သော»; «X ဖြစ်သော» → «X မဟုတ်သော»; double negatives twice).

## Coordinator decisions applied
- «Anulomaṃ.» (end of the positive order), the «Sahajātā –» label, asaññasattānaṃ, the heinous deeds: none of these
  occurs in 5-13 … 5-20.
- The sixth-dyad forms: those of 3-03-06 (Q's KNOWN_ADJ).
- Order headings: anulomapaccanīya «အဟုတ်ပြ အငြင်းပြ ပုံစံ», paccanīyānuloma «အငြင်းပြ အဟုတ်ပြ ပုံစံ» (the finished
  groups' ORDER_N), so «Dhammānulomapaccanīye» = «သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌», «Dhammapaccanīyānulome» =
  «သဘောတရား အငြင်းပြ အဟုတ်ပြ ပုံစံ၌» (as «Dhammānulome» «သဘောတရား အဟုတ်ပြ ပုံစံ၌»); the part words «Paccanīyaṃ»,
  «1-7. Paṭiccavārādi», «Hetu-ārammaṇapaccayā», «Paccanīyuddhāro», «Pañhāvāro» are the engine's.
- Colophons as the finished groups: «X niṭṭhitaṃ.» «<order> “<title>” ပြီးဆုံးပြီ။»; the book's end
  «Paṭṭhānapakaraṇaṃ niṭṭhitaṃ.» «“အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ကျမ်း ပြီးဆုံးပြီ။» (as pi-1 / pi-3 / pi-4 «“…” ကျမ်း
  ပြီးဆုံးပြီ။»); bhāṇavāra «ရွတ်ဖတ်ရန် အပိုင်း» (pi-1).
- Supplied words (logged here; H8): «သဘောတရား» after a term used as a noun in a note or sentence («Kusale pañca»
  «ကုသိုလ် သဘောတရား၌ ငါးခု», «Sahetukasadisaṃ» «အမြစ် ရှိသော သဘောတရားနှင့် တူသည်», «-mūla» «X သဘောတရားကို
  အခြေခံခြင်း»), as 2-01 «Savitakkasavicāramūlakā …» «… ရှိသော သဘောတရားကို အခြေခံသော ပြဿနာ»; the attributive term
  needs a noun in Burmese. No other word is supplied.

## Source slips and unsure Pāli (translated as written unless stated)
- 5-15 ^7-69-1 «… dve khandhe paṭicca dve khandhā nakusalaṃ dhammaṃ paṭicca abyākato dhammo uppajjati …»: the stop
  after «dve khandhā» is missing (the next sentence of the same line, the frame «Nakusalaṃ dhammaṃ paṭicca X dhammo
  uppajjati»); read with the stop (logged by the generator, SLIP_ADD; the checker reads it the same way).
- 5-14 ^7-68-49 «… uppajjati hetupaccayā ekaṃ… hetuyā dve.»: a count after the condition before «…» (Q's
  count-after rule widened from «.» to «.» / «…»): «… ဖြစ်ပေါ်သည် တစ်ခု…».
- 5-15 ^7-69-24 (and 5-12 ^7-66-73 / -82, other group) «{hetuyā aṭṭha?}»: an uncertain reading with «?»; rendered
  as the uncertain variants of 1-01 «{ပါဌ်ကွဲ ((မသေချာ)): hetuyā aṭṭha}» (reading kept in Roman, no «?»).
- 5-13 ^7-67-33 «(Tīṇi veditakaṃ kātabbaṃ.)»: «veditakaṃ» is unclear (the English zero-shot reads «relating to
  feeling», the Marathi «having known»); rendered «သုံးခုကို သိမှတ်၍ ပြုရမည်» (veditabba «to be known»). Unsure.
- 5-18 ^7-72-57 «(Nahetu nanahetu ovattā, …)»: «ovattā» read as «reversed» («ပြောင်းပြန် ဖြစ်ကြသည်»; English and
  Marathi agree). Unsure word.
- 5-17 ^7-71-95 «(Nasāsavaṃ naanidassanasappaṭighamūlassa …)»: «Nasāsavaṃ» stands apart (accusative) before the
  compound; read as one root «na-sāsava na-anidassanasappaṭigha» (as the neighbouring notes).
- 5-17 ^7-71-93 «Nakenaci viññeyyaṃ naanidassanasappaṭighassa purimasadisaṃ navapañhaṃ kātabbaṃ.»: accusative +
  genitive read as «for the root …» («… သဘောတရားအတွက် ရှေ့နှင့် တူသော ပြဿနာ ကိုးခု ပြုရမည်»).
- 5-17 ^7-71-97 «(Naāsavañceva naanāsavaṃ …mūlepi …)»: a «ceva» term without its closing «ca»; as written, stacked.
- 5-19 ^7-73-48 «(… dukamūlāni sattameva …)» in a tikatika chapter: as written («နှစ်မျိုးတွဲကို အခြေခံခြင်းများ»).
- 5-13 ^7-67-13 «Akusale tīṇi. Abyākataṃ anupādinnupādāniye tīṇiyeva…pe….»: a lone locative / accusative of terms;
  «… သဘောတရား၌ သုံးခု။ … သဘောတရားကို … သဘောတရား၌ သုံးခုသာ…။».
- Group names: «Cūḷantaradukāni» / «Mahantaradukāni» = the group's name «ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ် / အစုကြီး»
  (the group's dyads; «နှစ်မျိုးတွဲ» is not repeated); «Piṭṭhidukāni» = «နောက်ဆုံး နှစ်မျိုးတွဲများ» (Q's group name,
  already plural); «Antimadukaṃ» (5-20) «အဆုံးသတ် နှစ်မျိုးတွဲ», kept apart from piṭṭhi «နောက်ဆုံး».
- For a reviewer: the numbers of «1-19-20. Kusalattika-ajjhattattikadvayaṃ» etc. are kept as digits; the
  «-dvaya» name «… သုံးမျိုးတွဲ နှစ်ခု» (two triads) is new.

## Recurring sentences built by this script (placeholders, as Q's bare counts)
- Akusale tīṇi. = အကုသိုလ် သဘောတရား၌ သုံးခု။
- Abyākataṃ anupādinnupādāniye tīṇiyeva…pe…. = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို ကံကြောင့် မဖြစ်သော်လည်း စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား၌ သုံးခုသာ…။
- Nahetu nadukkhāya vedanāya sampayuttamūlaṃ tīṇiyeva. = အမြစ် မဟုတ်သော၊ နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသည် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း သုံးခုသာ။
- Nakenaci viññeyyaṃ naanidassanasappaṭighassa purimasadisaṃ navapañhaṃ kātabbaṃ. = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သည် မဟုတ်သော၊ မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသည် မဟုတ်သော သဘောတရားအတွက် ရှေ့နှင့် တူသော ပြဿနာ ကိုးခု ပြုရမည်။
- Nakenaci viññeyyaṃ naanidassanaappaṭighamūlassa navapañhameva. = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သည် မဟုတ်သော၊ မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသည် မဟုတ်သော သဘောတရားကို အခြေခံခြင်းအတွက် ပြဿနာ ကိုးခုသာ။
- Hetuyā cha pañhā. = အမြစ်ဟူသော အကြောင်း၌ ပြဿနာ ခြောက်ခု။
- Naasaṅkhataṃ…pe… (sappaccayadukasadisaṃ). = ပြုပြင်ဖန်တီးထားခြင်း မရှိသည် မဟုတ်သော သဘောတရား… (အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်)။
- Loose fragments (engine LEX): «gaṇitakena tīṇi» «ရေတွက်ချက်အားဖြင့် သုံးခု», «gaṇitakena tīṇi pañhā»
  «ရေတွက်ချက်အားဖြင့် ပြဿနာ သုံးခု», «cha pañhā» «ပြဿနာ ခြောက်ခု», «saṃsaṭṭhavāre» «ရောနှောခြင်းအလိုက် ဖော်ပြချက်၌».
