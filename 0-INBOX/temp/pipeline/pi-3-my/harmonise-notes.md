# pi-3 Burmese zero-shot: consistency pass (harmonise) log

Brief `harmonise-brief.md`, items `harmonise-todo.md` (A1-A5, B1-B8). Pāli only; no Burmese translation or nissaya
opened, no web search; pi-1-my / pi-2-my only read. Nothing committed.

## How it was applied
- Backups before any edit: `harmonise-backup/` (every generator, check and module, `my3-zeroshot-terms.md`) and
  `harmonise-backup/chapters/` (all 16 chapter files before the pass).
- One place: `my3_formulas.py`, new block «consistency pass (harmonise)» at the end: the book-wide frame words
  (WITH, WITH_PL, SOME, REL, TE, TEHI, NATTHI, BY), `chain_item_my()` (B3), `bare_item_my()` (B7), the verse
  vocabulary (B5) and `install()`, which adds the numbers 19 / 30 / 43 / 47 / 50 / 123, TERM_ALIAS (A5), the siglum
  «bahūsu» (B8), the variant labels, the headings Khandhādi / Saccādi / Phassādisattakaṃ and the book colophon (B6),
  the singular subject «avijjāpaccayā saṅkhāro» (B4) and ALL 43 summary-verse lines of the book (F.VERSES / F.FIXED).
  `line_my()` records the topic names of a fixed (verse) line in USED when the line is generated (FIXED_USES), so
  the reuse tests still count only what the text uses.
- make_sample.py does not call install(): the user-approved sample (preamble, 1, 2) and my3-zeroshot-terms.md are
  byte-identical to before (checked).
- make_ch3-6-8-9.py, make_ch7-10-11.py, make_ch12-15.py: call `F.install()`; their own verse tables, numbers,
  aliases, headings, sigla and frame constants removed or pointed at the shared ones; the item rules call
  F.chain_item_my / F.bare_item_my. No chapter file was edited by hand.

## Items (chosen form; reason; generators changed; lines / uses changed)

### Part A: the source as written
- A1 ^3-413 (in 12-ekadasamanayo; the todo says ch15) «… dhātusaṅgahena saṅgahitā te dhammā»: no «၊» before
  «ထိုသဘောတရားများသည်» (the Pāli has no mark), as ^3-225 «… အကျုံးမဝင်သော သဘောတရားများ ထိုသဘောတရားတို့နှင့်…»
  (kept). make_ch12-15.py CONN_MY « » -> « ». 1 line.
- A2 ^3-269 (ch7) «Dassanena pahātabbā dhammā bhāvanāya pahātabbā dhammā…»: the Pāli has no mark between the two
  subjects; the Burmese now has none either: «…ပယ်ရမည့် သဘောတရားများသည် ဘာဝနာ ပွားများခြင်းဖြင့် …» (no «၊», no «…»).
  make_ch7-10-11.py SLIP_SPLIT join. 1 line.
- A3 a space before «…» in the Pāli (21 lines: ch2, 4-8, 10, 14, 15): typography only, every generator writes «X…»
  (one regex `F.ELL_RE` / `\s*(…pe…|…)\s*`; make_ch3-6-8-9.py now uses F.ELL_RE). 0 lines changed.
- A4 confirmed, nothing "corrected": ^3-357 «..» kept («…နှင့်.. …»); ^3-287 «… aparāmaṭṭhā dhammā sampayuttāti?»
  (no «…pe…»: «…သဘောတရားများသည် ယှဉ်တွဲကြသနည်း။», no «…» added); ^3-298 «… dhammā… sampayuttāti?» as written.
- A5 spelling-only slips: the intended (pi-1) word is kept (rule); all in one place:
  * ^3-189 «Cittasahabhūmi dhammehi» = cittasahabhuno dhammā «စိတ်နှင့်အတူ တည်ရှိသော သဘောတရားများ» (make_ch3-6-8-9 SLIP)
  * ^3-210 «paccupannārammaṇehi» = paccuppannārammaṇā (TERM_ALIAS, now in install())
  * ^3-213, ^3-279 and ch10-15 «na hetusahetuk-» (one word) = na hetū sahetukā (TERM_ALIAS / INSTR_ITEM), 7 lines
  * «na hetuahetukehi» (one word, ch12-15) = na hetū ahetukā (INSTR_ITEM), 1 line
  * ^3-454 «dhātusaṅgena» = dhātusaṅgahena «ဓာတ် အကျုံးဝင်ခြင်းဖြင့်» (make_ch12-15 REL_SG)
  * upādinn- (pi-3) = upādiṇṇ- (pi-1; pi-1 lists upādinn- as the Syā. spelling): anupādinnupādāniya- (4 lines),
    anupādinnaanupādāniya- (6), anupādinnā / -ehi (4) (TERM_ALIAS of the sample)
  * kept as written (not spelling only): ^3-450 «Natthi?» = «မရှိ။» (no «?» in Burmese); ^3-453
    «āsavavippayuttehi ceva no ca āsavehi» (new term, as written); ^3-487 «ye vippayuttā» (dhammā missing, same frame).

### Part B: one form per item
- B1 verb number: the Pāli number, the sample's rule (-o / -aṃ singular, -āni plural, -ā singular after a feminine
  singular subject: dhātu, avijjā, vedanā, saññā …, else plural), the same in questions and answers. Checked
  book-wide: every agent's check tests it (sample, ch7-10-11 by subject; ch3-6-8-9 and ch12-15: subject always «te
  dhammā», all «ကြ»); the ch7-10-11 «… မည်မျှတို့နှင့် ယှဉ်တွဲသနည်း။» occurs only after a singular / feminine
  singular subject (e.g. ^3-233 «Cakkhudhātu …pe… sampayuttāti?»), every «te dhammā … sampayuttā?» has «ကြသနည်း»
  (28 / 28). 0 lines changed. The 5 sentences align_check still reports differ only by «ကြ» for this reason
  (harmonise_align_kept.py, below).
- B2 kehici «… (တို့)၏ အချို့နှင့် V» (212 uses) and na kehici «V-ရာ X၊ Y မရှိ» (109 lines): already one form in all
  groups; now one constant (F.SOME). 0 lines changed.
- B3 relative-clause frames: «X-ena ye dhammā…» with the verb elided = «Xနှင့်…» (the relative «Vသော သဘောတရားများ»
  only where the Pāli says the verb), the form of ch3-6-8-9 and ch12-15 (majority; the Pāli elides the verb).
  make_ch7-10-11.py (chunk_my) now uses F.chain_item_my: 186 chain items in ch10 / ch11 changed (931 items in the
  book, 0 other form left). khandhasaṅgahena … «အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် အကျုံး(မ)ဝင်၊ …သော သဘောတရားများ»,
  tehi dhammehi «ထိုသဘောတရားတို့နှင့်» (pi-1 ^1-1115), te dhammā «ထိုသဘောတရားများသည်» (pi-1 ^1-1091), Natthi «မရှိ။»
  (pi-1 ^1-1221): already one form; now the shared constants.
- B4 saṅkhāra: singular «avijjāpaccayā saṅkhārena» (ch4, 5, 6) = «… ပြုပြင်ဖန်တီးမှု» (pi-2 ^2-249); plural
  «saṅkhārā / saṅkhārehi» (ch2, 7, 10-15) = «… ပြုပြင်ဖန်တီးမှုများ» (sample, pi-2 ^2-227); «saṅkhārapaccayā
  viññāṇa-» = «ပြုပြင်ဖန်တီးမှုများကြောင့် ဖြစ်သော သိစိတ်» (sample) everywhere. Already by the Pāli number; the
  singular subject moved into install(). 0 lines changed.
- B5 summary verses (all 43 lines in my3_formulas._verses(); identical Pāli lines now identical Burmese):
  * locatives (-e / -esu / -su, ettha) = «တွင်» (the sample's IN): 24 «၌» -> «တွင်»
  * «padā» with a number = «ပုဒ် N-ပါး»; a count without «padā» = «N-ပါး» (classifier ပါး as the sample): 16 + 6
  * gocchaka «အစု»; antara «ကြားညှပ်»; duka «နှစ်မျိုးတွဲ» only where the Pāli has duka: cūḷantare / mahantare /
    mahantarā = «ကြားညှပ် အစုငယ် / အစုကြီး», Sattantarā «ကြားညှပ်တို့မှ», Paṭhamantare «ပထမ ကြားညှပ်», aparante
    «နောက် ကြားညှပ်» (no «အစု» added); Mahantaraduke / cūḷantaradukā / piṭṭhidukesu = the pi-1 headings
  * paccayākāre «အကြောင်းတို့၏ အခြင်းအရာတွင်»; paccaye «အကြောင်း အပိုင်းတွင်» (ch10 had the dependent-arising name)
  * upari / uddhaṃ «အထက်တွင်», tato upari «ထို့အထက်တွင်», tato pare «ထို့နောက်တွင်»; puna «တဖန်» (not «နောက်ထပ်»);
    atha «ထို့နောက်» (^3-190 «…တို့၌မူ» -> «ထို့နောက် …»); tathā / tathariva «ထို့အတူ»
  * numbers 30 / 43 / 47 one word with ပါး / မျိုး («သုံးဆယ်ပါး အပြည့်», «သုံးဆယ်မျိုး»)
  * na labbhati «မတွေ့ရ» (sg), na labbhare / labbhanti «မတွေ့ရကြ» (pl, ^3-318 fixed); jīvitaṃ «အသက်»; mahābhavā
    «ဘဝကြီး»; samuccheda «ပိုင်းဖြတ်ခြင်း»; moghapucchakena «မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်»; matthake «အဆုံးတွင်»;
    iccete … dhammā «ဤသို့ ဤသဘောတရား N-ပါးတို့သည်» (no «များ» with a count)
  * maccurūpaṃ: rūpaṃ = the term «ရုပ် ဖြစ်သော သဘောတရား» (ch14 form, as its neighbours anārammaṇaṃ …), ^3-227
  * verse verbs «…သည်» (no «၏»); no verb added after «… ca» («…လည်း။», ^3-447 / ^3-518 «လည်း ဖြစ်သည်» removed)
  * manāyatanameva ca = «၊ မနော အာရုံခံ နယ်ပယ်လည်း» (^3-345 «လေးပါးနှင့်» -> «လေးပါး၊»)
  * ^3-227 / ^3-455 «(Bāhiraṃ upādā) dve, visayo [dvevīsati (syā.)] esanayo subuddho» / «Dve visayo esanayo
    subuddhoti»: one literal treatment, as written, no emendation: «နှစ်ပါး၊ အပိုင်းအခြား၊ ဤခွဲနည်းကို ကောင်းစွာ
    နားလည်အပ်သည်» (visayo «အပိုင်းအခြား», not «နယ်ပယ်» = āyatana; subuddho «ကောင်းစွာ နားလည်အပ်သည်»; ch6 «ဟူသော
    နှစ်ပါးသည် … ဖြစ်၏၊ … နားလည်ပြီ» and ch14 «နယ်ပယ်နှင့်တကွ … သိမြင်အပ်သည်» dropped)
  Verse lines changed: 34 (ch4 3, ch5 1, ch6 2, ch7 4, ch8 1, ch9 4, ch10 5, ch11 4, ch12 1, ch13 4, ch14 1, ch15 4).
  Other lines changed: 63 (ch10 22 and ch11 39 = B3 chain items / B7 / B8; ch7 1 = A2; ch12 1 = A1).
- B6 headings / colophons: Khandhādi «အစုအဝေး စသည်», Saccādi «သစ္စာ စသည်», Phassādisattakaṃ «တွေ့ထိမှု စသည့်
  ခုနစ်မျိုးတွဲ», Tikaṃ / Dukaṃ (pi-2), «(X-mūlakaṃ.)» (pi-2 pattern), the book colophon «“ဓာတ်များအကြောင်း
  ဆွေးနွေးခြင်း” ကျမ်း ပြီးဆုံးပြီ။» (pi-1 ^1-1616 / pi-2 ^2-1044): already one form; now defined once in install().
  0 lines changed.
- B7 bare instrumental items «Saṃyojanehi… ganthehi…» (no «dhammehi ye dhammā»): the pi-1 term without
  «သဘောတရားများ» and without «နှင့်» («နှောင်ကြိုး ဖြစ်သော…»), the form of ch4 / ch5 (2 lines of 3; the «…» stands
  for the elided words, as in the Pāli). ^3-346 (ch10) changed (F.bare_item_my). The elided question
  «…(pe…) sampayuttāti?» keeps the sample's katihi particle «…သနည်း» (32 lines, no «သလော»).
- B8 sigla: «(bahūsu)» = «(Bahūsu)», the pi-1 / pi-2 final form (pi-1 ^1 2-02, 4-01, pi-2 ch6: «(Bahūsu)», Roman like
  every other siglum), read from FINAL by heads_sigla(); the ch7-10-11 «မူ အများ» dropped (^3-343, 1 line). «(?)» =
  «(အမည်မသိ မူ)» (pi-2 ^2-924); Sī. Syā. Ka. Pī. (pi-1). For the user's review: the todo wrote «မူ အများ»; the
  precedence (pi-1 / pi-2 final > the parallel agents) gave «Bahūsu».

## Checks changed on purpose (only where a form was changed on purpose)
- check_ch12-15.py B_REL: also «… သဘောတရားများ ထိုသဘောတရားများသည်» (no «၊», A1).
- check_ch3-6-8-9.py verse numbers: «သုံးဆယ်မျိုး» (one word, B5).
- check_ch7-10-11.py relatives: only a «ye dhammā» with its verb has a Burmese relative; an elided item is «Xနှင့်…»
  (B3). Its relative count is now 180 (the explicit ones).

## Cross-chapter alignment
- align_check: 11 differing -> 5; align_hidden: 0 -> 0. The 5 left differ only by «ကြ»: the same Pāli answer
  («… vippayuttā; … kehici vippayuttā.» / «… asaṅgahitā.») follows a feminine singular subject in ch2 / ch7 (dhātu,
  avijjā, vedanā, saññā: singular, the sample's rule) and «te dhammā» / a plural subject elsewhere
  (harmonise_align_kept.py verifies both conditions for every location).
- Identical Pāli chunks (between ellipses) with different Burmese: 151 before, 0 now (scratch/chunks.py).
- harmonise_pi12.py: pi-1 13 / 13, pi-2 12 / 12 identical (before and after).

## Lines changed per chapter (harmonise_diff.py)
97 lines: preamble 0, 1 0, 2 0, 3 0, 4 3, 5 1, 6 2, 7 5, 8 1, 9 4, 10 27, 11 43, 12 2, 13 4, 14 1, 15 4.

## Verification (regen_zeroshot.sh, run twice, the second run changed no chapter byte)
- check_chapter_ids / check_text_pe / check_marks: OK for all 16 files (chk-pe copies deleted).
- check_sample 0 mismatches, reuse 322 / 322; check_ch3-6-8-9 0, 203 / 203; check_ch7-10-11 0, 201 / 201 (was
  200 / 200: the shared verse table records its names per generated line); check_ch12-15 0, 265 / 265.
- harmonise_scan.py: 69 / 69 items OK (harmonise-table.tsv).
