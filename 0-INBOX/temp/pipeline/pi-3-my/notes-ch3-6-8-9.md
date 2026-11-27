# Notes: pi-3 Burmese zero-shot, chapters 3, 4, 5, 6, 8, 9 (Dhātukathā)

Brief: `burmese-zeroshot-brief.md`. Generator `make_ch3-6-8-9.py` (imports my3_formulas.py read only and extends it in
memory), check `check_ch3-6-8-9.py`. Output in `AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/`:
3-dutiyanayo.md, 4-tatiyanayo.md, 5-catutthanayo.md, 6-pancamanayo.md, 8-sattamanayo.md, 9-atthamanayo.md.
Translated from the Pāli only (English zero-shot and Marathi rails read for meaning only); no Burmese translation or
nissaya opened, no web search; pi-1-my / pi-2-my / my3_formulas.py / my3-zeroshot-terms.md not edited.

## Status
- All six chapters generated; the three verifiers OK; check_ch3-6-8-9.py 0 mismatches, reuse 203 / 203. chk-pe copies
  of my chapters deleted.

## Frames (new; one rendering per Pāli formula)
- X-ena ye dhammā (in a chain with saṅgahitā / sampayuttā / vippayuttā) = Xနှင့် (the relative head «သော သဘောတရားများ»
  is said once, after the predicate; chain items joined by «… »)
- khandhasaṅgahena saṅgahitā = အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် အကျုံးဝင် (same wording as make_ch12-15.py rel_my)
- āyatanasaṅgahena saṅgahitā = အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်းဖြင့် အကျုံးဝင်
- dhātusaṅgahena saṅgahitā = ဓာတ် အကျုံးဝင်ခြင်းဖြင့် အကျုံးဝင် (asaṅgahitā: … အကျုံးမဝင်); the three joined by «၊», then «သော သဘောတရားများ»
- ye dhammā sampayuttā = ယှဉ်တွဲသော သဘောတရားများ; ye dhammā vippayuttā = ကင်းကွာသော သဘောတရားများ
- tehi dhammehi ye dhammā = ထိုသဘောတရားတို့နှင့် …သော သဘောတရားများ (pi-1 ^1-1115, identical Pāli «Tehi dhammehi ye dhammā sampayuttā»)
- tehi dhammehi ye dhammā…pe… = ထိုသဘောတရားတို့နှင့်…
- te dhammā = ထိုသဘောတရားများသည် (pi-1 ^1-1091)
- «…, te dhammā» after the relative clause = «…သော သဘောတရားများ၊ ထိုသဘောတရားများသည်»
- te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi (a)saṅgahitā? = ထိုသဘောတရားများသည် အစုအဝေး မည်မျှ၊ အာရုံခံ နယ်ပယ် မည်မျှ၊ ဓာတ် မည်မျှတို့တွင် အကျုံး(မ)ဝင်ကြသနည်း။ (sample Q1_MY, plural)
- te dhammā katihi … sampayuttā(ti) / vippayuttā? = ထိုသဘောတရားများသည် အစုအဝေး မည်မျှ၊ အာရုံခံ နယ်ပယ် မည်မျှ၊ ဓာတ် မည်မျှတို့နှင့် ယှဉ်တွဲ / ကင်းကွာကြသနည်း။ (the closing «ti» not rendered, as in the sample)
- Te dhammā COUNTS (a)saṅgahitā. = ထိုသဘောတရားများသည် COUNTSတို့တွင် အကျုံးဝင်ကြသည် / အကျုံးမဝင်ကြ။ (sample counts_my; zero «အကျုံးဝင်ရာ အစုအဝေး မရှိ၊ …»)
- Te dhammā COUNTS vippayuttā. = ထိုသဘောတရားများသည် COUNTSတို့နှင့် ကင်းကွာကြသည်။ (one count of one: «…တစ်ပါးနှင့်»)
- na kehici khandhehi na kehici āyatanehi … vippayuttā = ကင်းကွာရာ အစုအဝေး၊ အာရုံခံ နယ်ပယ် မရှိ၊ … (sample zero-run pattern)
- ; ekenāyatanena ekāya dhātuyā kehici vippayuttā = ၊ အာရုံခံ နယ်ပယ် တစ်ပါး၊ ဓာတ် တစ်ပါးတို့၏ အချို့နှင့် ကင်းကွာကြသည် (kehici = «တို့၏ အချို့နှင့်», as make_ch12-15.py / make_ch7-10-11.py)
- Natthi. = မရှိ။ (pi-1 ^1-1221 «natthi» = «မရှိ»)
- A chain line without predicate, ending «ye dhammā….» (^3-192) = «Xနှင့်… Yနှင့်…။»
- Bare chain items without «dhammehi ye dhammā» (^3-187 «Saṃyojanehi … ganthehi…», ^3-192 «āsavehi… saṃyojanehi…») = the term without «သဘောတရားများ» and without «နှင့်»: «နှောင်ကြိုး ဖြစ်သော… အထုံး ဖြစ်သော… … မှားယွင်းသော ယူဆမှု ဖြစ်သော သဘောတရားများနှင့်…»

## Topic names (all read from pi-1 / pi-2 final through F.subject(); instrumental -> nominative table INS in the generator)
- New subject key: avijjāpaccayā saṅkhāro (singular, Pāli «avijjāpaccayā saṅkhārena» ^3-182, ^3-192, ^3-200) = အမှန်ကို မသိမှုကြောင့် ဖြစ်သော ပြုပြင်ဖန်တီးမှု (pi-2 ^2-249 «Tattha katamo avijjāpaccayā saṅkhāro?»). The sample's plural «avijjāpaccayā saṅkhārā» (ch2) = «… ပြုပြင်ဖန်တီးမှုများ»; for the consistency pass.
- saṅkhārapaccayā viññāṇaṃ = ပြုပြင်ဖန်တီးမှုများကြောင့် ဖြစ်သော သိစိတ် (as the sample, pi-2 ^2-227).
- TERM_ALIAS (in memory): paccupannārammaṇā -> paccuppannārammaṇā (pi-3 spelling ^3-210); na hetusahetukā -> na hetū sahetukā (^3-213, as make_ch7-10-11.py).
- Instrumental plural adjectives: -ehi -> -ā, -īhi -> -ino (ācayagāmīhi, maggādhipatīhi, rūpīhi, -ānuparivattīhi), -bhūhi -> -bhuno, hetūhi -> hetū.

## Variant readings (labels)
- upādānapaccayā kammabhavena (syā.) = ပါဌ်ကွဲ, after «ကံ ဘဝနှင့်» (^3-182)
- [na hetū sahetukehi (sī.), na hetūhi sahetukehi (syā. ka.)] = [ပါဌ်ကွဲ (Sī.): na hetū sahetukehi၊ (Syā., Ka.): na hetūhi sahetukehi] (pi-2 ^2-165 two-variant pattern), before «သဘောတရားများ» (^3-213)
- punareva (pī.), cullantaradukā (sī.), tiṃsavidhanti (pī.) = စာလုံးပေါင်းကွဲ; dvevīsati (syā.) = ပါဌ်ကွဲ

## Summary verses (uddāna; table VERSES in the generator). New words:
- gocchaka = အစု (pi-1 Hetugocchakaṃ «အမြစ်တို့၏ အစု»); antara = ကြားညှပ် (pi-1 Cūḷantaradukaṃ «ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်», Mahantaradukaṃ «… အစုကြီး», read by heads())
- pada = ပုဒ် (sample); paccayākāra = အကြောင်းတို့၏ အခြင်းအရာ (new); paṭicca(pada) = အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ (sample)
- upari = ထို့အထက်၌; uddhaṃ = အထက်ပိုင်း၌; puna / punadeva = တဖန်; tathā / tathariva = ထို့အတူ; atha = ထို့နောက် (^3-318) / «မူ» (^3-190)
- na labbhare / na labbhanti = မတွေ့ရ / မတွေ့ရကြ; samuccheda = ပိုင်းဖြတ်ခြင်း; moghapucchaka = မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်
- visayo = အပိုင်းအခြား; esa nayo subuddho = ဤခွဲနည်းကို ကောင်းစွာ နားလည်ပြီ; yuttā (manena) = (စိတ်နှင့်) ယှဉ်သော; matthake = အဆုံးပိုင်း၌; aparante = နောက်ပိုင်း (ကြားညှပ် အစု)တွင်
- itthi / pumaṃ / jīvitaṃ (verse) = မိန်းမ / ယောက်ျား / အသက် (the faculty names without «၏ စွမ်းရည်»); maccu = သေခြင်း (= maraṇa); rūpaṃ = ရုပ်; nāmarūpaṃ = စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း
- neuter singular topics in the verses = the pi-1 term with «သဘောတရား» instead of «သဘောတရားများ» (e.g. sanidassanasappaṭighaṃ = မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိသော သဘောတရား)
- Numbers: 30 = သုံးဆယ်, 47 = လေးဆယ့်ခုနစ် (as make_ch12-15.py); counted with «ပါး» (sample); «tiṃsavidha» = သုံးဆယ် မျိုး
- ^3-190 L3 «Samatiṃsa padā honti, gocchakesu dasasvatha» = «အစု ဆယ်ပါးတို့၌မူ ပုဒ် သုံးဆယ် အပြည့် ရှိ၏၊» (word order changed inside the line)
- ^3-190 L4 «Duve cūḷantaradukā …, aṭṭha honti mahantarāti» = «နှစ်ပါးသည် ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ် [..] ဖြစ်၏၊ ရှစ်ပါးသည် ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး ဖြစ်၏။»

## Unsure Pāli (verses translated literally, for review)
- ^3-178 «Anidassanaṃ punadeva sappaṭighaṃ upādāti»: the prose order is anidassanasappaṭigha, sanidassana, sappaṭigha, upādā; rendered word by word «မမြင်နိုင်သော သဘောတရား၊ တဖန် … ထိခိုက်မှု ရှိသော သဘောတရား၊ …».
- ^3-192 «gocchakapadamettha tiṃsavidhāti» = «here the cluster terms are of thirty kinds».
- ^3-227 «Bāhiraṃ upādā dve, visayo [dvevīsati (syā.)] esanayo subuddho»: read «the two, external and derived; (this is) the range; this method is well understood»; Syā. «dvevīsati» (22) changes the sense; the weakest line.
- ^3-316 «Tayo paṭicca tathariva phassapañcamā» = three from dependent arising, likewise the five beginning with contact; «dve ca manena yuttā» = two joined with mind.
- ^3-318 «Samucchede na labbhanti, moghapucchakena» = not found in (this) division, because the question is empty.

## Source slips (translated as written, logged)
- ^3-189 «Cittasahabhūmi dhammehi»: read as cittasahabhūhi (= cittasahabhuno dhammā «စိတ်နှင့်အတူ တည်ရှိသော သဘောတရားများ»).
- ^3-225 no comma before «tehi dhammehi»: the Burmese has no «၊» there either.
- ^3-210 «paccupannārammaṇehi» (single -p-): pi-1 term paccuppannārammaṇā.
- ^3-213 «na hetusahetukehi» (compound, variants «na hetū / na hetūhi sahetukehi»): pi-1 term na hetū sahetukā.
- Spacing before ellipses («ye dhammā …», «Saṃyojanehi …», «dhammā ….») normalized to «…» directly after the item.

## Checks
- check_chapter_ids / check_text_pe / check_marks: OK for all six (segments: ch3 10, ch4 14, ch5 4, ch6 39, ch8 13, ch9 4).
- check_ch3-6-8-9.py: A 6 / 6 regenerated identical; B 73 content lines, 85 sentences, 85 predicates (polarity of each
  of the three saṅgaha parts / sampayutta-vippayutta), 212 counts (kind, number, verb kind and polarity, kehici),
  25 verse lines (numbers, variant text); 0 mismatches; C reuse 201 / 201 topic names and mātikā terms, 2 / 2
  headings (Tikaṃ, Dukaṃ) = 203 / 203.
