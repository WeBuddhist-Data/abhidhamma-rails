# Notes: pi-3 Burmese zero-shot, chapters 12-15 (Ekādasama … Cuddasama naya)

Brief: `burmese-zeroshot-brief.md`. Files: `12-ekadasamanayo.md`, `13-dvadasamanayo.md`, `14-terasamanayo.md`,
`15-cuddasamanayo.md` in `AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/`; generator
`make_ch12-15.py` (imports my3_formulas.py, adds to its tables in memory only; never writes my3-zeroshot-terms.md),
checker `check_ch12-15.py`. Translated from the Pāli only; no Burmese translation or nissaya opened, no web search;
pi-1-my / pi-2-my, the English zero-shot and the Marathi notes (frame inventory only) were only read.

## Status
- All four chapters generated and verified (check_chapter_ids, check_text_pe, check_marks: OK; chk-pe copies deleted).
- check_ch12-15.py: A 4 / 4 regenerated identical; B 110 content lines, 110 chains, 365 verbs, 689 counts,
  17 verse lines, 0 mismatches; C reuse 261 / 261 terms + 4 / 4 headings / names = 265 / 265 (one new term, below).
- Mutation test of the checker (a count, a polarity, a «kehici», a relative clause changed in a copy): all caught.

## Frames (new, built once, used identically in all four methods)
- X-ena ye dhammā… (chain item) = Xနှင့်…  (each item «…pe…» / «…» = one «…»; spacing normalised to «Xနှင့်… »)
- Y-ena ye dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā = Yနှင့် အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် အကျုံးဝင်၊ အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်းဖြင့် အကျုံးဝင်၊ ဓာတ် အကျုံးဝင်ခြင်းဖြင့် အကျုံးဝင်သော သဘောတရားများ
- Y-ena ye dhammā khandhasaṅgahena asaṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā = Yနှင့် အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် အကျုံးမဝင်၊ အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်းဖြင့် အကျုံးမဝင်၊ ဓာတ် အကျုံးဝင်ခြင်းဖြင့် အကျုံးမဝင်သော သဘောတရားများ
- Y-ena ye dhammā sampayuttā = Yနှင့် ယှဉ်တွဲသော သဘောတရားများ (pi-1 SAMP)
- Y-ena ye dhammā vippayuttā = Yနှင့် ကင်းကွာသော သဘောတရားများ (pi-1 VIPP)
- khandhasaṅgahena = အစုအဝေး အကျုံးဝင်ခြင်းဖြင့်
- āyatanasaṅgahena = အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်းဖြင့်
- dhātusaṅgahena = ဓာတ် အကျုံးဝင်ခြင်းဖြင့်
- …, te dhammā / , te dhammā = …၊ ထိုသဘောတရားများသည် / ၊ ထိုသဘောတရားများသည်
- …pe… te dhammā / … te dhammā = … ထိုသဘောတရားများသည်
- te dhammā = ထိုသဘောတရားများသည် (pi-1 ^1-57 «ime dhammā» = «ဤသဘောတရားများ»)
- te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttā(ti)? = ထိုသဘောတရားများသည် အစုအဝေး မည်မျှ၊ အာရုံခံ နယ်ပယ် မည်မျှ၊ ဓာတ် မည်မျှတို့နှင့် ယှဉ်တွဲကြသနည်း။
- te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā? = ထိုသဘောတရားများသည် အစုအဝေး မည်မျှ၊ အာရုံခံ နယ်ပယ် မည်မျှ၊ ဓာတ် မည်မျှတို့တွင် အကျုံးဝင်ကြသနည်း။ (sample Q1)
- Katihi vippayuttā? = မည်မျှတို့နှင့် ကင်းကွာကြသနည်း။
- Katihi asaṅgahitā? = မည်မျှတို့တွင် အကျုံးမဝင်ကြသနည်း။ (sample)
- COUNTS sampayuttā = COUNTSတို့နှင့် ယှဉ်တွဲကြသည် (one count of one: «…နှင့်»)
- COUNTS vippayuttā = COUNTSတို့နှင့် ကင်းကွာကြသည် (one count of one: «…နှင့်»)
- COUNTS kehici sampayuttā = COUNTSတို့၏ အချို့နှင့် ယှဉ်တွဲကြသည် (one count of one: «…၏ အချို့နှင့်»)
- COUNTS kehici vippayuttā = COUNTSတို့၏ အချို့နှင့် ကင်းကွာကြသည်
- kehici = အချို့ (partly: with some of …)
- COUNTS saṅgahitā / asaṅgahitā / na kehici … = sample counts_my, plural (… အကျုံးဝင်ကြသည် / … အကျုံးမဝင်ကြ / အကျုံးမဝင်ရာ … မရှိ)
- A; B (two answer clauses) = A၊ B။
- Natthi. = မရှိ။
- asaṅkhataṃ khandhato ṭhapetvā = sample THAPETVA, after «ထိုသဘောတရားများသည်»
- All verbs plural («ကြ»): the subject is always ye / te dhammā.
- The quotative «-ti» of «sampayuttāti?» and of the verse ends is not rendered (as the sample).

## Item names (instrumental -> the topic's nominative, all FINAL pi-1 / pi-2 Burmese through the sample's SUBJ)
- «X-ena / X-āya / X-iyā / X-uyā / X-ehi» -> the nominative in SUBJ (e.g. Samudayasaccena = samudayasaccaṃ,
  jātiyā = jāti, avijjāpaccayā saṅkhārehi = avijjāpaccayā saṅkhārā); «… dhammehi» -> «… dhammā» word by word
  (-ehi -> -ā, -īhi -> -ino, -bhūhi -> -bhuno, bahiddhāhi -> bahiddhā, hetūhi -> hetū).
- Irregular: pañcahi indriyehi = pañcindriyāni; pañcahi balehi = pañca balāni; sattahi bojjhaṅgehi = satta
  bojjhaṅgā; ariyena aṭṭhaṅgikena maggena = ariyo aṭṭhaṅgiko maggo; upādādhammehi = upādā dhammā;
  na hetusahetukehi = na hetū sahetukā; na hetuahetukehi = na hetū ahetukā (pi-3 writes «hetusahetuka» as one word).
- dukkhena (soko … upāyāso list) = dukkhaṃ = «ကိုယ်ဆင်းရဲခြင်း» (sample's sense); vedanāya / saññāya / cetanāya /
  cittena (phassādi lists) = the pi-1 NAMES.
- NEW term (source slip, below): āsavavippayuttā ceva no ca āsavā dhammā = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော်လည်း စိတ်အစွန်းအထင်း မဟုတ်သော သဘောတရားများ

## Headings and colophons (new)
- Khandhādi = အစုအဝေး စသည် (pattern of the sample's «Paṭiccasamuppādādi»)
- Saccādi = သစ္စာ စသည်
- Phassādisattakaṃ = တွေ့ထိမှု စသည့် ခုနစ်မျိုးတွဲ (sattaka: pi-2 «Pañcakaṃ = ငါးမျိုးတွဲ» pattern)
- Dhātukathāpakaraṇaṃ niṭṭhitaṃ. = “ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း” ကျမ်း ပြီးဆုံးပြီ။ (pi-1 ^1-1616, pi-2 ^2-1044 pattern)
- Tikaṃ / Dukaṃ and the «…padaniddeso ekādasamo.» colophons: the sample's tables.

## Verse summaries (uddāna; hand-translated, fixed lines in make_ch12-15.py)
Words reused: gocchaka = အစု (pi-1 «Hetugocchakaṃ = အမြစ်တို့၏ အစု»); Mahantaraduka = ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး
and Piṭṭhiduka = နောက်ဆုံး နှစ်မျိုးတွဲများ (pi-1 headings); antara = ကြားညှပ်; paṭicca(samuppāda) = pi-2 name;
navamassa padassa niddese = နဝမ ပုဒ်ကို အကျယ် ဖော်ပြချက်၌ (NIDDESO pattern); na labbhare / na labbhanti = မတွေ့ရကြ.
Numbers (new): tiṃsa = သုံးဆယ်, tecattālīsa = လေးဆယ့်သုံး, sattacattālīsa = လေးဆယ့်ခုနစ်.
- Dve saccā pannarasindriyā, ekādasa paṭiccapadā; = သစ္စာ နှစ်ပါး၊ စွမ်းရည် ဆယ့်ငါးပါး၊ အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ၏ ပုဒ် ဆယ့်တစ်ပါး၊
- Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti. = ထို့အထက်တွင် နောက်ထပ် ဆယ့်တစ်ပါး၊ ဤနေရာ၌ အစုတို့၏ ပုဒ်သည် သုံးဆယ်မျိုး ရှိသည်။
- Rūpakkhandhā cattāro, manāyatanameva ca; = ရုပ် အစုအဝေးမှလွဲ၍ အစုအဝေး လေးပါး၊ မနော အာရုံခံ နယ်ပယ်လည်း၊
- Viññāṇadhātuyo satta, dve saccā cuddasindriyā. = သိစိတ် ဓာတ် ခုနစ်ပါး၊ သစ္စာ နှစ်ပါး၊ စွမ်းရည် ဆယ့်လေးပါး။
- Paccaye dvādasa padā, tato upari soḷasa; = အကြောင်း အပိုင်း၌ ပုဒ် ဆယ့်နှစ်ပါး၊ ထို့အထက်တွင် ဆယ့်ခြောက်ပါး၊
- Tikesu aṭṭha gocchake, tecattālīsameva ca. = သုံးမျိုးတွဲတို့၌ ရှစ်ပါး၊ အစုတို့၌ လေးဆယ့်သုံးပါးလည်း ဖြစ်သည်။
- Mahantaraduke satta, padā piṭṭhidukesu cha; = ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး၌ ခုနစ်ပါး၊ နောက်ဆုံး နှစ်မျိုးတွဲများ၌ ပုဒ် ခြောက်ပါး၊
- Navamassa padassete, niddese saṅgahaṃ gatāti. = ဤပုဒ်တို့သည် နဝမ ပုဒ်ကို အကျယ် ဖော်ပြချက်၌ အကျုံးဝင်ကြသည်။
- Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ; = ရုပ်၊ သဘောတရား အာရုံခံ နယ်ပယ်၊ သဘောတရား ဓာတ်၊ မိန်းမ၊ ယောက်ျား၊ အသက်၊ စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း၊
- Dve bhavā jātijarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ. = ဘဝ နှစ်ပါး၊ မွေးဖွားခြင်း၊ အိုခြင်း၊ သေခြင်း၊ ရုပ် ဖြစ်သော သဘောတရား၊ အာရုံ မရှိသော သဘောတရား၊ စိတ် မဟုတ်သော သဘောတရား၊ စိတ်နှင့် ကင်းကွာသော သဘောတရား။
- Visaṃsaṭṭhaṃ samuṭṭhānasahabhu, anuparivatti bāhiraṃ upādā; = စိတ်နှင့် မရောနှောသော သဘောတရား၊ စိတ်မှ ဖြစ်ပေါ်လာသော သဘောတရား၊ စိတ်နှင့်အတူ တည်ရှိသော သဘောတရား၊ စိတ်နောက်သို့ လိုက်ပါသော သဘောတရား၊ ပြင်ပ သဘောတရား၊ မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား၊
- Dve visayo esanayo subuddhoti. = နှစ်ပါး၊ နယ်ပယ်နှင့်တကွ ဤခွဲနည်းကို ကောင်းစွာ သိမြင်အပ်သည်။
- Dhammāyatanaṃ dhammadhātu, atha jīvitaṃ nāmarūpaṃ; = သဘောတရား အာရုံခံ နယ်ပယ်၊ သဘောတရား ဓာတ်၊ ထို့နောက် အသက်၊ စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း၊
- Saḷāyatanaṃ jātijarāmataṃ, dve ca tike na labbhare. = အာရုံခံ နယ်ပယ် ခြောက်ပါး၊ မွေးဖွားခြင်း၊ အိုခြင်း၊ သေခြင်း၊ သုံးမျိုးတွဲတို့၌ နှစ်ပါးလည်း မတွေ့ရကြ။
- Paṭhamantare satta ca, gocchake dasa aparante; = ပထမ ကြားညှပ်၌ ခုနစ်ပါး၊ အစုတို့၌ ဆယ်ပါး၊ နောက် ကြားညှပ်၌
- Cuddasa cha ca matthake, iccete sattacattālīsa dhammā; = ဆယ့်လေးပါး၊ အဆုံး၌ ခြောက်ပါး၊ ဤသို့ ဤသဘောတရား လေးဆယ့်ခုနစ်ပါးတို့သည်
- Samucchede na labbhanti, moghapucchakena cāti. = ဤပိုင်းခြားမှု၌ မတွေ့ရကြ၊ အချည်းနှီး မေးခွန်း ဖြစ်သောကြောင့်လည်း ဖြစ်သည်။
(The verse lists use the pi-1 / pi-2 topic names; «X dhammā» terms as singular «… သဘောတရား».)

## Unsure Pāli
- ^3-447 «Rūpakkhandhā cattāro»: read as ablative, «the four [aggregates] apart from the form aggregate» (the
  chapter's items are vedanā … viññāṇa); Burmese «ရုပ် အစုအဝေးမှလွဲ၍ အစုအဝေး လေးပါး» (small clarification).
- ^3-455 «Dve visayo esanayo subuddhoti»: translated as written («two; with its range this method is well
  understood»). The items of ch14 that have answers are exactly 22 (rūpa; dhammāyatana … maraṇa = 11; rūpino;
  anārammaṇa … upādā = 9), so the line may originally read «dvevīsa yo esa nayo» (twenty-two); not adopted.
- ^3-518 «Samucchede» = «ဤပိုင်းခြားမှု၌» (in this analysis); «matthake» = «အဆုံး၌» (at the end, i.e. the last
  dyads); «aparante» = later intermediate (antara) section «နောက် ကြားညှပ်၌».
- ^3-447 «Paccaye» = «အကြောင်း အပိုင်း၌» (the section of conditions = dependent arising).

## Source slips (translated as written; logged)
- ^3-450 «Natthi?» (question mark for a full stop): the Burmese has no «?»; rendered «မရှိ။» like every «Natthi.».
- ^3-453 «āsavavippayuttehi ceva no ca āsavehi dhammehi»: only here (pi-1 has «āsavasampayuttā ceva no ca āsavā»);
  translated as written, new term built from the pi-1 term with «ယှဉ်တွဲ» -> «ကင်းကွာ».
- ^3-454 «dhātusaṅgena» for «dhātusaṅgahena»: same Burmese as dhātusaṅgahena.
- ^3-487 «paṇītehi dhammehi ye vippayuttā» («dhammā» missing after «ye»): same frame.
- ^3-413 «…dhātusaṅgahena saṅgahitā te dhammā» (no mark before «te dhammā»): «၊» added.
- ^3-421 «sampayuttā…, te dhammā»: «…၊ ထိုသဘောတရားများသည်».
- ^3-454, ^3-455, ^3-462, ^3-471, ^3-517 a space before «…» («ye dhammā …»): normalised to «Xနှင့်… ».

## For the consistency pass
- The chain / relative-clause frame «Y-ena ye dhammā khandhasaṅgahena (a)saṅgahitā …» also occurs in methods 2-5
  (other agents) with mixed polarity per saṅgaha; please align with the strings above (or vice versa).
- «kehici» (partly) and «Natthi» may also be rendered by the agents of methods 6-10.
- Khandhādi / Saccādi / Phassādisattakaṃ headings may recur in other chapters.
