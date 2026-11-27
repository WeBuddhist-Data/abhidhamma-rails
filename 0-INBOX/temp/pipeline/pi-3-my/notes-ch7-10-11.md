# Notes: pi-3 Burmese zero-shot, chapters 7-chatthanayo, 10-navamanayo, 11-dasamanayo

Brief: `burmese-zeroshot-brief.md`. Files: `make_ch7-10-11.py` (generator), `check_ch7-10-11.py` (check), this file.
Output: `AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/{7-chatthanayo,10-navamanayo,11-dasamanayo}.md`.
Translated from the Pāli only; no Burmese translation or nissaya opened, no web search; `my3_formulas.py`,
`my3-zeroshot-terms.md`, pi-1-my / pi-2-my only read. English pi-3 zero-shot and Marathi notes used for meaning /
frame inventory only.

## Status
- 7-chatthanayo.md (86 segments), 10-navamanayo.md (36), 11-dasamanayo.md (60): generated, the three verifiers OK,
  check_ch7-10-11.py 0 mismatches, reuse 200 / 200. chk-pe copies deleted.

## How the generator works
- Imports my3_formulas (F) and adds IN MEMORY: one sentence rule in F.EXTRA_RULES (all sentences of these
  chapters), F.HEAD["Saccādi"], F.SIGLA["bahūsu"], two F.VAR_KIND entries, the verse lines in F.FIXED, one
  F.TERM_ALIAS entry. Everything else (topic names, mātikā terms, numbers, counted nouns, headings, colophons) is the
  sample's tables, read from the FINAL pi-1 / pi-2 Burmese.
- Instrumental items of ch10 / ch11 («Vedanākkhandhena», «Kusalehi dhammehi», «avijjāya», «pañcahi indriyehi» …)
  are turned back into their nominative (rules + a short special table) and must then be an existing subject; the
  Burmese name is the subject's FINAL name + «နှင့်».

## New strings («Pāli = Burmese»)
- sampayutto / sampayuttā (pl.) = ယှဉ်တွဲသည် / ယှဉ်တွဲကြသည် (question: ယှဉ်တွဲသနည်း / ယှဉ်တွဲကြသနည်း)
- vippayutto / vippayuttā (pl.) = ကင်းကွာသည် / ကင်းကွာကြသည် (question: ကင်းကွာသနည်း / ကင်းကွာကြသနည်း)
- COUNTS sampayutto = A n-ပါး၊ B m-ပါးတို့နှင့် ယှဉ်တွဲသည် (one count of one: «A တစ်ပါးနှင့်»)
- S katihi khandhehi katihāyatanehi katihi dhātūhi sampayutto(ti)? = Sသည် အစုအဝေး မည်မျှ၊ အာရုံခံ နယ်ပယ် မည်မျှ၊ ဓာတ် မည်မျှတို့နှင့် ယှဉ်တွဲသနည်း။
- Katihi vippayutto? = မည်မျှတို့နှင့် ကင်းကွာသနည်း။
- S…pe… sampayuttoti? (question words elided) = Sသည်… ယှဉ်တွဲသနည်း။ (the «…» stands for the elided «with how many»)
- Natthi. = မရှိ။ (pi-1 ^1-1433 «natthi» = «မရှိ»)
- COUNTS kehici sampayutto = A n-ပါး၊ B m-ပါးတို့၏ အချို့နှင့် ယှဉ်တွဲသည် («with some of»; one count of one: «… ၏ အချို့နှင့်»)
- clause «; » = «၊ » (first clause ends with its verb «…သည်၊», the last with «။»)
- na kehici khandhehi na kehici āyatanehi N dhātūhi vippayutto = ကင်းကွာရာ အစုအဝေး၊ အာရုံခံ နယ်ပယ် မရှိ၊ ဓာတ် N-ပါးတို့နှင့် ကင်းကွာသည် (the sample's zero-run pattern with ယှဉ်တွဲ / ကင်းကွာ)
- X-ena ye dhammā sampayuttā = Xနှင့် ယှဉ်တွဲသော သဘောတရားများ (pattern of pi-1 ^1-1115)
- tehi dhammehi ye dhammā sampayuttā = ထိုသဘောတရားတို့နှင့် ယှဉ်တွဲသော သဘောတရားများ (pi-1 ^1-1115, identical Pāli)
- te dhammā = ထိုသဘောတရားများသည် (pi-1 ^1-1091)
- ch10 / ch11 question: «R1… Rn၊ ထိုသဘောတရားတို့နှင့် Vသော သဘောတရားများ၊ ထိုသဘောတရားများသည် အစုအဝေး မည်မျှ၊ … ဓာတ် မည်မျှတို့နှင့် Vကြသနည်း။»; answer «ထိုသဘောတရားများသည် COUNTS Vကြသည်၊ COUNTS တို့၏ အချို့နှင့် Vကြသည်။»
- in a chain «X-ena ye dhammā… Y-ena ye dhammā V»: every item gets its relative verb («Xနှင့် Vသော သဘောတရားများ…»)
- bare instrumental items «Saṃyojanehi… ganthehi…» (^3-346, no «dhammehi ye dhammā») = the name + «နှင့်»: «နှောင်ကြိုး ဖြစ်သော သဘောတရားများနှင့်…»
- Saccādi (heading) = သစ္စာ စသည် (pattern of Paṭiccasamuppādādi)
- (bahūsu) (sigla) = (မူ အများ)
- [na hetūhi sahetukehi (bahūsu)] = [ပါဌ်ကွဲ (မူ အများ): na hetūhi sahetukehi] (word variant, as the sample's ^3-112)
- [anupādiṇṇehi (sī. ka.)] = [ပါဌ်ကွဲ (Sī., Ka.): anupādiṇṇehi]

## Summary verses (whole lines; «;» = «၊», «.» = «။», the closing «ti» not rendered)
- Dhammāyatanaṃ dhammadhātu, dukkhasaccañca jīvitaṃ; = သဘောတရား အာရုံခံ နယ်ပယ်၊ သဘောတရား ဓာတ်၊ ဒုက္ခ သစ္စာနှင့် အသက်၊
- Saḷāyatanaṃ nāmarūpaṃ, cattāro ca mahābhavā. = အာရုံခံ နယ်ပယ် ခြောက်ပါး၊ စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း၊ ဘဝကြီး လေးပါးတို့လည်း။
- Jāti jarā ca maraṇaṃ, tikesvekūnavīsati; = မွေးဖွားခြင်း၊ အိုခြင်းနှင့် သေခြင်း၊ သုံးမျိုးတွဲတို့တွင် ဆယ့်ကိုးပုဒ်၊
- Gocchakesu ca paññāsa, aṭṭha cūḷantare padā. = အစုတို့တွင် ငါးဆယ်ပုဒ်၊ ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်တွင် ရှစ်ပုဒ်။
- Mahantare pannarasa, aṭṭhārasa tato pare; = ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီးတွင် ဆယ့်ငါးပုဒ်၊ ထို့နောက်တွင် ဆယ့်ရှစ်ပုဒ်၊
- Tevīsa padasataṃ etaṃ, sampayoge na labbhatīti. = ဤပုဒ် တစ်ရာ့နှစ်ဆယ့်သုံးပုဒ်ကို ယှဉ်တွဲခြင်း၌ မတွေ့ရ။
- Arūpakkhandhā cattāro, manāyatanameva ca; = ရုပ် မဟုတ်သော အစုအဝေး လေးပါးနှင့် မနော အာရုံခံ နယ်ပယ်လည်း၊
- Viññāṇadhātuyo satta, dve saccā cuddasindriyā. = သိစိတ် ဓာတ် ခုနစ်ပါး၊ သစ္စာ နှစ်ပါး၊ စွမ်းရည် ဆယ့်လေးပါး။
- Paccaye dvādasa padā, tato upari soḷasa; = အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ၌ ဆယ့်နှစ်ပုဒ်၊ ထို့အထက်တွင် ဆယ့်ခြောက်ပုဒ်၊
- Tikesu aṭṭha gocchake, tecattālīsameva ca. = သုံးမျိုးတွဲတို့တွင် ရှစ်ပုဒ်၊ အစုတို့တွင် လေးဆယ့်သုံးပုဒ်လည်း။
- Mahantaraduke satta, padā piṭṭhi dukesu cha; = ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီးတွင် ခုနစ်ပုဒ်၊ နောက်ဆုံး နှစ်မျိုးတွဲများတွင် ခြောက်ပုဒ်၊
- Navamassa padassete, niddese saṅgahaṃ gatāti. = ဤပုဒ်တို့သည် နဝမ ပုဒ်ကို အကျယ် ဖော်ပြချက်၌ အကျုံးဝင်ကြသည်။
- Words: gocchaka = အစု (pi-1 «N-တို့၏ အစု»); cūḷantara(duka) / mahantara(duka) / piṭṭhiduka = pi-1 headings
  «ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ် / အစုကြီး», «နောက်ဆုံး နှစ်မျိုးတွဲများ»; tika = သုံးမျိုးတွဲ; pada = ပုဒ် (sample PADA);
  jīvitaṃ = အသက် (pi-2 termbase); saḷāyatanaṃ = အာရုံခံ နယ်ပယ် ခြောက်ပါး, nāmarūpaṃ = စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (pi-2);
  mahābhava = ဘဝကြီး (new); arūpa- = ရုပ် မဟုတ်သော (pi-2 arūpajīvitindriya); 19 ဆယ့်ကိုး, 43 လေးဆယ့်သုံး,
  50 ငါးဆယ် (pi-2), 123 တစ်ရာ့နှစ်ဆယ့်သုံး; na labbhati = မတွေ့ရ; saṅgahaṃ gatā = အကျုံးဝင်ကြသည်.

## Unsure Pāli / choices for review
- kehici after the counts: «… တို့၏ အချို့နှင့်» (associated / dissociated with some of that base and element, i.e.
  partly). The meaning cross-check (English «partly with …») agrees.
- An elided question «…pe… sampayuttāti?» keeps «…သနည်း» (the wh-word is in the elided part); a strict yes/no form
  would be «…သလော».
- jīvitaṃ in the verse is the life faculty; rendered «အသက်» (pi-2 termbase jīvitaṃ), not «အသက်၏ စွမ်းရည်».
- «Paccaye» (in the dependent-arising part) = «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ၌» (small clarification).
- «tato pare» = «ထို့နောက်တွင်», «tato upari» = «ထို့အထက်တွင်» (two Pāli phrases, two Burmese phrases).

## Source slips (translated as written)
- ^3-269: «Dassanena pahātabbā dhammā bhāvanāya pahātabbā dhammā…» has no «…» between the first two subjects; the
  Burmese joins them with «၊» (each with «သည်»).
- ^3-287: «… parāmāsavippayuttā aparāmaṭṭhā dhammā sampayuttāti?» and ^3-298 «… pahātabbahetukā dhammā… sampayuttāti?»:
  the question words are elided without «…pe…»; rendered as the elided question («… ယှဉ်တွဲကြသနည်း။»).
- ^3-279 «na hetusahetukā» (ch10 «na hetusahetukehi») = pi-1 «na hetū sahetukā»: same term, same Burmese (TERM_ALIAS).
- ^3-343: the variant «[na hetūhi sahetukehi (bahūsu)]» stands after «tehi dhammehi», not after «na hetusahetukehi»
  which it glosses; kept at the Pāli position («ထိုသဘောတရားတို့နှင့် [ပါဌ်ကွဲ …] ယှဉ်တွဲသော …»).
- ^3-357: «kāyindriyena ye dhammā.. itthindriyena»: «..» instead of «…»; kept as «..» (the ellipsis count stays equal).
- ^3-397: «Anārammaṇehi [anupādiṇṇehi (sī. ka.)] dhammehi»: the variant names a different term; kept as a word variant.
- ^3-408: the ch11 (dissociation) verse is word for word the ch7 verse, ending «sampayoge na labbhatīti»; translated
  as written (identical Burmese).
