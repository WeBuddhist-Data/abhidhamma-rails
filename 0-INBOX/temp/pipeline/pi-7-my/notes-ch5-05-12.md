# pi-7 part 5, 5-05 … 5-12 (paccanīya dukatika / tikaduka / tikatika / dukaduka, anulomapaccanīya tika / duka / dukatika / tikaduka): Burmese zero-shot notes

PROGRESS: DONE (2026-11-24). Written to AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/:
5-05-paccaniya-dukatika.md, 5-06-paccaniya-tikaduka.md, 5-07-paccaniya-tikatika.md, 5-08-paccaniya-dukaduka.md,
5-09-anulomapaccaniya-tika.md, 5-10-anulomapaccaniya-duka.md, 5-11-anulomapaccaniya-dukatika.md,
5-12-anulomapaccaniya-tikaduka.md. (Check results: see the end of this file.)

## Files
- make_ch5-05-12.py: generator. It IMPORTS the finished part-5 group make_ch5-01-04.py as M (read-only; M's main
  never runs) and uses M's atoms (every triad / dyad term of the finished groups), M's na-X rule, chain rewriting,
  note renderer, numbers and M's two engines (world A = make_ch3-09, world B = make_ch4-01), extended in memory.
  `--dev`, `--dump`, `--slips`, `--new`, `--out DIR`. Regenerating gives identical files (checked with `--out`).
- check_ch5-05-12.py: checker, adapted from check_ch5-01-04.py (structure, conditions, term order, polarity,
  numbers, identity, tables, reuse; `--mutate`, `--groups`). The finished groups for the identity test are 1-00 … 4-14
  and 5-01 … 5-04 (not the chapters in progress).
- chk-ch5-05-12/: scratch (dev output, probes, the check output).

## How the chapters are run
- Each chapter is cut at its part headings: «##### 1-1. Hetuduka-kusalattikaṃ» (5-05 … 5-08, 5-11, 5-12),
  «##### Kusalattikaṃ» (5-09), «##### Hetudukaṃ» / «##### 20-49. Saññojanadukādi» (5-10).
- The atoms of a part are those of the dyads / triads its heading names; a group word («Cūḷantaradukāni»,
  «Āsavagocchaka», «Chagocchakāni» (dyads 20-54), «Dvigocchakāni» / «upādānādi» (69-82), «mahantara» (with upādāna and
  kilesa, as 5-08 «1-54-81»), «piṭṭhi», «X-ādittikāni» (X to the last triad), «X-ādidukāni» / «Xdukādi» (X to the end of
  its cluster)) gives the whole group; every dyad is widened to its cluster (the paccanīya of a «ceva» dyad uses the
  terms of the other dyads of the cluster, as 5-04). World B when every dyad of the part is a world-B dyad, else A.
- Every term chain is rewritten into one synthetic term exactly as M does: two terms on one noun stacked «A၊ B N»
  (the dukatika / tikaduka stacking of 4-02-09 / 4-10-14 and 5-01 … 5-04); the pi-1 dyad pairs keep their dyad Burmese
  (the sixth dyads, «X ceva Y ca»); na-X by M's rule («…သော» → «…သည် မဟုတ်သော», «X ဖြစ်သော» → «X မဟုတ်သော», double
  negatives twice: «nanahetu» «အမြစ် မဟုတ်သည် မဟုတ်သော»).
- One change to M's chain rule (in this script only): a «ceva … ca» term stacks with a following SINGLE term
  («Hetu ceva sahetuko ca kusalo dhammo» «အမြစ်လည်း ဖြစ်၊ အမြစ်လည်း ရှိသော၊ ကုသိုလ် သဘောတရား», as 5-02 does with its
  closer_links), but a «ceva» term followed by another «ceva» term is coordination (as 5-04).
- A lone term before «…» or ending an elided list «…pe… nonīvaraṇaṃ.» is a term (its noun elided), as before its noun.
- Part / heading words as M: «Dhammapaccanīye» «သဘောတရား အငြင်းပြ ပုံစံ၌»; «Dhammānulomapaccanīye» «သဘောတရား
  အဟုတ်ပြ အငြင်းပြ ပုံစံ၌» (the order word «Anulomapaccanīyaṃ» «အဟုတ်ပြ အငြင်းပြ ပုံစံ» of the finished groups);
  «dukatika» «နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ …» (4-02), «tikaduka» «သုံးမျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ …»; part
  headings «<num> <dyad name>နှင့် <triad name>» (4-02); group words «X-ādi…āni» «X စသည်တို့၏ …များ» (as M «Oghādidukāni»),
  «Xdukādi» «<X dyad name> စသည်» (as «Paṭiccavārādi» «… စသည်»).
- Hand-written units (a short sentence the engine has no frame for, 5-12) go in as placeholders and come back after the
  engine; the notes the engine and M do not render are composed by this script's clause table (see the list below).

## Coordinator decisions applied
- «Anulomaṃ.» does not occur in these chapters; «Sahajātā –», asaññasattānaṃ and the heinous deeds do not occur.
- The sixth-dyad forms are those of 3-03-06 (M's KNOWN_ADJ).
- The na-X rule and the part / heading words are M's (5-01-04), unchanged.
- Supplied words: «ရုပ်» in «(cittasamuṭṭhānameva …)» «စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်သာ» (the noun of the fixed phrase
  cittasamuṭṭhānaṃ rūpaṃ, elided in the note); «သဘောတရား» after a term used as a noun in the notes / hand units
  («akusalaṃ kusalasadisaṃ» «အကုသိုလ် သဘောတရားသည် ကုသိုလ် သဘောတရားနှင့် တူသည်»; the finished notes' pattern).
- Identity with the finished groups for one sentence: «(Sahajātavārampi…pe… sampayuttavārampi vitthāretabbaṃ.)» keeps
  the nominative list «…ဖော်ပြချက်လည်း… အကျယ် ချဲ့ရမည်» of 4-10 … 4-14 (M's general «…ကိုလည်း» is kept for the other
  lists; H20 is still open). «(Yathā kusalattike pañhāvārassa … gaṇitaṃ, evaṃ gaṇetabbaṃ.)» as 4-02 (no «၊» for the
  comma).

## Source slips and unsure Pāli (translated as written unless stated; all logged by `--slips`)
- 5-05 ^7-59-1 «Nahetuṃ nakusalaṃ dhammaṃ paṭicca nanahetuṃ nakusalo dhammo»: the conditioned term written in the
  accusative; read «nanahetu nakusalo» (the parallel sentences).
- 5-05 ^7-59-42 «Naapaccayaṃ» = «naappaccayaṃ» (spelling); 5-07 ^7-61-52 «nanevāsekkhanāsekkhaṃ» = «nanevasekkha…»;
  5-05 ^7-59-17 «nanevaācayagāmiṃ nāpacayagāmiṃ» (two words) = the term «nanevācayagāmināpacayagāmi»; 5-12 ^7-66-83
  «naanupannassa» = «naanuppannassa». The term's Burmese in each case.
- 5-08 ^7-62-11 «Nahetuṃ naupādādhammaṃ» read «naupādā dhammaṃ»; «nocittasampayuttaṃ» (the dyad has no «no-» term):
  «no» read as «na», the na-X rule on cittasampayutta «စိတ်နှင့် ယှဉ်တွဲသည် မဟုတ်သော».
- 5-10 ^7-64-7 «nahetuvippayutto ceva nanahetu dhammo ca uppajjati»: read «nanahetu ca dhammo»;
  ^7-64-21 «āsavavippayutto nanoanāsavo»: read «naanāsavo» (the two sentences before it).
- 5-11 ^7-65-32 «naahetukassa ceva nana hetussa»: read «nana ca hetussa» (the same sentence before it).
- 5-07 ^7-61-65 «Hetuyā. Nava (sabbattha nava.)»: a stray full stop, kept «အမြစ်ဟူသော အကြောင်း၌။ ကိုးခု (…)».
- 5-10 ^7-64-14 «(Lokuttaraṃ dhammaṃ paṭicca nalokiyo ca nalokuttaro ca dhammā uppajjanti hetupaccayā.)» (a sentence
  in brackets) and the editorial note «{ayaṃ saṅkhyā vicāretabbā, nalokiyanalokuttaradhammo nāma natthi}»: kept as
  written, the sentence translated inside its brackets.
- 5-07 ^7-61-45 the editorial note in braces between a term and its noun: kept in that place.
- 5-12 ^7-66-73 / -82 «{hetuyā aṭṭha?}»: «{အမြစ်ဟူသော အကြောင်း၌ ရှစ်ခု (မသေချာ)}» («?» as the sample's «(?)»).
- 5-12 ^7-66-18 / -19 / -34 / -35 / -36: counts after a term written as short sentences («Kusalaṃ appaṭighena tīṇi.»,
  «Akusalena tīṇiyeva.», «Abyākatāni tīṇi.»): hand-written, the instrumental «…ဖြင့်», the plural «…များ၌».
- 5-09 ^7-63-12 «sukhavedanā» (pleasant feeling, the noun): «သာယာသော ခံစားမှု» (the vedanā triad's words).
- Unsure: «(Ekapañhameva. Etena upāyena kusalākusaladukaṃ kusalattikameva ettha vaṭṭati.)» (5-05 ^7-59-41): read
  «only one question; in this way only the kusala-akusala dyad / kusala triad applies here»; «vattati / vaṭṭati»
  «သက်ဆိုင်သည်». «Abyākatamūlaṃ tīṇiyeva paccayavasena» «… အခြေခံခြင်းသည် အကြောင်းအလိုက် သုံးခုသာ».

## New strings (headings, names, note words, numbers, hand units)
- Dhammānulomapaccanīye = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌
- Dhammapaccanīye tikatikapaṭṭhānaṃ = သဘောတရား အငြင်းပြ ပုံစံ၌ သုံးမျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammapaccanīye tikatikapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အငြင်းပြ ပုံစံ၌ “သုံးမျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammapaccanīye dukadukapaṭṭhānaṃ = သဘောတရား အငြင်းပြ ပုံစံ၌ နှစ်မျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammapaccanīye dukadukapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အငြင်းပြ ပုံစံ၌ “နှစ်မျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammapaccanīye dukatikapaṭṭhānaṃ = သဘောတရား အငြင်းပြ ပုံစံ၌ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammapaccanīye dukatikapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အငြင်းပြ ပုံစံ၌ “နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammapaccanīye tikadukapaṭṭhānaṃ = သဘောတရား အငြင်းပြ ပုံစံ၌ သုံးမျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammapaccanīye tikadukapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အငြင်းပြ ပုံစံ၌ “သုံးမျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammapaccanīye tikapaṭṭhānaṃ = သဘောတရား အငြင်းပြ ပုံစံ၌ သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammapaccanīye tikapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အငြင်းပြ ပုံစံ၌ “သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammapaccanīye dukapaṭṭhānaṃ = သဘောတရား အငြင်းပြ ပုံစံ၌ နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammapaccanīye dukapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အငြင်းပြ ပုံစံ၌ “နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammānulomapaccanīye tikatikapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ သုံးမျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammānulomapaccanīye tikatikapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ “သုံးမျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammānulomapaccanīye dukadukapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ နှစ်မျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammānulomapaccanīye dukadukapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ “နှစ်မျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammānulomapaccanīye dukatikapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammānulomapaccanīye dukatikapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ “နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammānulomapaccanīye tikadukapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ သုံးမျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammānulomapaccanīye tikadukapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ “သုံးမျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammānulomapaccanīye tikapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammānulomapaccanīye tikapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ “သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Dhammānulomapaccanīye dukapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Dhammānulomapaccanīye dukapaṭṭhānaṃ niṭṭhitaṃ. = သဘောတရား အဟုတ်ပြ အငြင်းပြ ပုံစံ၌ “နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Paccanīyapaṭṭhānaṃ niṭṭhitaṃ. = အငြင်းပြ ပုံစံ၌ “အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
- Tatiyapadaṃ = တတိယ ပုဒ်
- Kusalattikapiṭṭhidukaṃ niṭṭhitaṃ. = “ကုသိုလ် သုံးမျိုးတွဲနှင့် နောက်ဆုံး နှစ်မျိုးတွဲများ” ပြီးဆုံးပြီ။
- ekūnapaññāsa = လေးဆယ့်ကိုး
- aṭṭhacattālīsa = လေးဆယ့်ရှစ်
- ekūnavīsa = ဆယ့်ကိုး
- pañcavīsa = နှစ်ဆယ့်ငါး
- chabbīsa = နှစ်ဆယ့်ခြောက်
- aṭṭhavīsa = နှစ်ဆယ့်ရှစ်
- ekūnavīsati = ဆယ့်ကိုး
- nocittasampayutta = စိတ်နှင့် ယှဉ်တွဲသည် မဟုတ်သော
- {ito paṭṭhāya yāva ajjhattārammaṇattikā … nanu tehipi bhavitabbaṃ} = ဤနေရာမှ စ၍ မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ တိုင်အောင် စာမူ အားလုံးတို့၌ အကုသိုလ် ပုဒ်နှင့် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော ပုဒ်တို့ကို မတွေ့ရ၊ ခံစားမှု သုံးမျိုးတွဲနှင့် မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲတို့၌ကဲ့သို့ ထိုပုဒ်တို့လည်း ရှိသင့်သည် မဟုတ်လော
- {hetuyā aṭṭha?} = အမြစ်ဟူသော အကြောင်း၌ ရှစ်ခု (မသေချာ)
- {ayaṃ saṅkhyā vicāretabbā, nalokiyanalokuttaradhammo nāma natthi} = ဤ ရေတွက်ချက်ကို စိစစ်ရမည်၊ လောကနှင့် သက်ဆိုင်သည် မဟုတ်၊ လောကကို ကျော်လွန်သည် မဟုတ်သော သဘောတရား ဟူ၍ မရှိ
- kātabbā / kātabbaṃ (N …) = ပြုရမည်
- -yeva (only, after a count) = သာ
- ekaṃyeva = တစ်ခုတည်း
- X-mūlaṃ (nominative) = ကို အခြေခံခြင်း
- paccayavasena = အကြောင်းအလိုက်
- etena upāyena = ဤနည်းလမ်းဖြင့်
- ettha = ဤနေရာ၌
- na labbhati = မတွေ့ရ
- (X-e) na sadisaṃ = မတူ
- vattati / vaṭṭati (applies here) = သက်ဆိုင်သည်
- ete saṃkhittā = ဤတို့ကို အကျဉ်းချုပ်ထားသည်
- yāva X-epi (up to X too) = တိုင်အောင်လည်း
- (pañhāvāraṃ vitthāretabbaṃ) = ပြဿနာအလိုက် ဖော်ပြချက်ကို အကျယ် ချဲ့ရမည်
- (pañhāvāraṃ evaṃ vitthāretabbaṃ) = ပြဿနာအလိုက် ဖော်ပြချက်ကို ဤသို့ အကျယ် ချဲ့ရမည်
- (vitthāretabbaṃ) = အကျယ် ချဲ့ရမည်
- (piṭṭhidukaṃ vitthāretabbaṃ) = နောက်ဆုံး နှစ်မျိုးတွဲများကို အကျယ် ချဲ့ရမည်
- (paccanīyaṃ vitthāretabbaṃ) = အငြင်းပြ ပုံစံကို အကျယ် ချဲ့ရမည်
- (abyākatamūlaṃ tīṇiyeva) = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို အခြေခံခြင်းသည် သုံးခုသာ
- (abyākatamūlaṃ tīṇiyeva paccayavasena) = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို အခြေခံခြင်းသည် အကြောင်းအလိုက် သုံးခုသာ
- (abyākatamūlaṃ dve) = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို အခြေခံခြင်းသည် နှစ်ခု
- (abyākatamūlaṃ ekaṃyeva) = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို အခြေခံခြင်းသည် တစ်ခုတည်း
- (abyākatamūle dve) = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ နှစ်ခု
- (abyākatavāre sabbattha paccayavasena gaṇetabbaṃ) = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားအလိုက် ဖော်ပြချက်၌ နေရာတိုင်း၌ အကြောင်းအလိုက် ရေတွက်ရမည်
- (nanocittapadaṃ na labbhati) = စိတ် မဟုတ်သည် မဟုတ်သော ပုဒ်ကို မတွေ့ရ
- (yāva pañhāvārepi ekaṃ) = ပြဿနာအလိုက် ဖော်ပြချက် တိုင်အောင်လည်း တစ်ခု
- (cittasamuṭṭhānarūpameva ettha vattati) = ဤနေရာ၌ စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်သာ သက်ဆိုင်သည်
- (cittasamuṭṭhānameva) = စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်သာ
- (ārammaṇaṃ natthi) = အာရုံဟူသော အကြောင်း မရှိ
- (mahābhūtā natthi) = မူလဓာတ်ကြီးတို့ မရှိ
- (ekapañhameva) = ပြဿနာ တစ်ခုသာ
- (etena upāyena kusalākusaladukaṃ kusalattikameva ettha vaṭṭati) = ဤနည်းလမ်းဖြင့် ဤနေရာ၌ ကုသိုလ်နှင့် အကုသိုလ် နှစ်မျိုးတွဲ၊ ကုသိုလ် သုံးမျိုးတွဲသာ သက်ဆိုင်သည်
- (etena upāyena nava pañhā kātabbā) = ဤနည်းလမ်းဖြင့် ပြဿနာ ကိုးခု ပြုရမည်
- (etena upāyena kenaci naviññeyye ekūnavīsati pañhā kātabbā) = ဤနည်းလမ်းဖြင့် တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော သဘောတရား၌ ပြဿနာ ဆယ့်ကိုးခု ပြုရမည်
- (ete saṃkhittā) = ဤတို့ကို အကျဉ်းချုပ်ထားသည်
- (dukattayaṃ cittadukasadisaṃ) = နှစ်မျိုးတွဲ သုံးခုသည် စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်
- (pañhāvāre na sadisaṃ) = ပြဿနာအလိုက် ဖော်ပြချက်၌ မတူ
- (āsavagocchakasadisaṃ) = စိတ်အစွန်းအထင်းတို့၏ အစုနှင့် တူသည်
- (saṃkiliṭṭhasaṃkilesikattikasadisaṃ) = ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲနှင့် တူသည်
- (akusalaṃ tīṇi kātabbaṃ) = အကုသိုလ် သဘောတရားကို သုံးခု ပြုရမည်
- (abyākataṃ tīṇi kātabbaṃ) = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို သုံးခု ပြုရမည်
- (saṅkhataṃ sappaccayasadisaṃ) = ပြုပြင်ဖန်တီးထားသော သဘောတရားသည် အကြောင်း ရှိသော သဘောတရားနှင့် တူသည်
- (asaṅkhataṃ appaccayasadisaṃ) = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရားသည် အကြောင်း မရှိသော သဘောတရားနှင့် တူသည်
- (akusalaṃ kusalasadisaṃ) = အကုသိုလ် သဘောတရားသည် ကုသိုလ် သဘောတရားနှင့် တူသည်
- (anāgato atītasadiso) = အနာဂတ် သဘောတရားသည် အတိတ် သဘောတရားနှင့် တူသည်
- (saṃkhittaṃ sappaccayasadisaṃ) = အကျဉ်းချုပ်၊ အကြောင်း ရှိသော သဘောတရားနှင့် တူသည်
- Kusalaṃ appaṭighena tīṇi. = ကုသိုလ်၊ ထိခိုက်မှု မရှိသော သဘောတရားဖြင့် သုံးခု။
- Akusalaṃ appaṭighena tīṇi. = အကုသိုလ်၊ ထိခိုက်မှု မရှိသော သဘောတရားဖြင့် သုံးခု။
- Abyākataṃ appaṭighena tīṇi. = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော၊ ထိခိုက်မှု မရှိသော သဘောတရားဖြင့် သုံးခု။
- Kusalaṃ appaṭighañca abyākataṃ appaṭighañca tīṇi. = ကုသိုလ်၊ ထိခိုက်မှု မရှိသော သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော၊ ထိခိုက်မှု မရှိသော သဘောတရား၌ သုံးခု။
- Akusalaṃ appaṭighañca abyākataṃ appaṭighañca tīṇi. = အကုသိုလ်၊ ထိခိုက်မှု မရှိသော သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော၊ ထိခိုက်မှု မရှိသော သဘောတရား၌ သုံးခု။
- Akusalena tīṇiyeva. = အကုသိုလ် သဘောတရားဖြင့် သုံးခုသာ။
- Abyākatena tīṇiyeva. = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားဖြင့် သုံးခုသာ။
- Abyākatāni tīṇi. = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ၌ သုံးခု။
- Acetasikāni nava. = စိတ်၏ အဖော် မဟုတ်သော သဘောတရားများ၌ ကိုးခု။
- Cittavippayutte tīṇi. = စိတ်နှင့် ကင်းကွာသော သဘောတရား၌ သုံးခု။
- satta pañhā (after «…») = ပြဿနာ ခုနစ်ခု
- sukhavedanā = သာယာသော ခံစားမှု
- 1-1. Hetuduka-kusalattikaṃ = 1-1. အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 1-2 Hetuduka-vedanāttikaṃ = 1-2 အမြစ် နှစ်မျိုးတွဲနှင့် ခံစားမှု သုံးမျိုးတွဲ
- 1-3-9. Hetuduka-vipākādittikāni = 1-3-9. အမြစ် နှစ်မျိုးတွဲနှင့် ကံ၏ အကျိုး စသည်တို့၏ သုံးမျိုးတွဲများ
- 1-10-21. Hetuduka-ācayagāmādittikāni = 1-10-21. အမြစ် နှစ်မျိုးတွဲနှင့် စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း စသည်တို့၏ သုံးမျိုးတွဲများ
- 1-22. Hetuduka-sanidassanattikaṃ = 1-22. အမြစ် နှစ်မျိုးတွဲနှင့် မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ
- 2-3-1. Sahetukadukādi-kusalattikaṃ = 2-3-1. အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ စသည်နှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 4-5-1. Hetusahetukadukādi-kusalattikaṃ = 4-5-1. အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ စသည်နှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 6-1. Nahetusahetukaduka-kusalattikaṃ = 6-1. အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 7-13-1. Cūḷantaradukāni-kusalattikaṃ = 7-13-1. ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်နှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 14-19-1. Āsavagocchaka-kusalattikaṃ = 14-19-1. စိတ်အစွန်းအထင်းတို့၏ အစုနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 20-54-1. Chagocchakāni-kusalattikaṃ = 20-54-1. အစု ခြောက်ခုနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 55-1. Mahantaraduka-kusalattikaṃ = 55-1. ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီးနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 69-74-1. Upādānagocchaka-kusalattikaṃ = 69-74-1. စွဲလမ်းမှုတို့၏ အစုနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 75-82-1. Kilesagocchaka-kusalattikaṃ = 75-82-1. ကိလေသာတို့၏ အစုနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 83-1. Piṭṭhiduka-kusalattikaṃ = 83-1. နောက်ဆုံး နှစ်မျိုးတွဲများနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 100-2. Saraṇaduka-vedanādittikāni = 100-2. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ခံစားမှု စသည်တို့၏ သုံးမျိုးတွဲများ
- 100-22. Saraṇaduka-sanidassanattikaṃ = 100-22. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ
- 1-1. Kusalattika-hetudukaṃ = 1-1. ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 1-2. Kusalattika-sahetukadukaṃ = 1-2. ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- 1-3-6. Kusalattika-hetusampayuttādidukāni = 1-3-6. ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 1-7-13. Kusalattika-cūḷantaradukāni = 1-7-13. ကုသိုလ် သုံးမျိုးတွဲနှင့် ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်
- 1-14-19. Kusalattika-āsavagocchakaṃ = 1-14-19. ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်းတို့၏ အစု
- 1-20-54. Kusalattika-saññojanādigocchakāni = 1-20-54. ကုသိုလ် သုံးမျိုးတွဲနှင့် နှောင်ကြိုး စသည်တို့၏ အစုများ
- 1-55-68. Kusalattika-mahantaradukāni = 1-55-68. ကုသိုလ် သုံးမျိုးတွဲနှင့် ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး
- 1-69-82. Kusalattika-upādānādidukāni = 1-69-82. ကုသိုလ် သုံးမျိုးတွဲနှင့် စွဲလမ်းမှု စသည်တို့၏ နှစ်မျိုးတွဲများ
- 1-83. Kusalattika-piṭṭhidukaṃ = 1-83. ကုသိုလ် သုံးမျိုးတွဲနှင့် နောက်ဆုံး နှစ်မျိုးတွဲများ
- 2-1. Vedanāttika-hetudukaṃ = 2-1. ခံစားမှု သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 3-21-1. Vipākādittikāni-hetudukaṃ = 3-21-1. ကံ၏ အကျိုး စသည်တို့၏ သုံးမျိုးတွဲများနှင့် အမြစ် နှစ်မျိုးတွဲ
- 22-1-6. Sanidassanattika-hetvādidukāni = 22-1-6. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် စသည်တို့၏ နှစ်မျိုးတွဲများ
- 22-7-13. Sanidassanattika-cūḷantaradukāni = 22-7-13. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်
- 22-14-54. Sanidassanattika-āsavādigocchakāni = 22-14-54. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း စသည်တို့၏ အစုများ
- 22-55-68. Sanidassanattika-mahantaradukāni = 22-55-68. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး
- 22-69-82. Sanidassanattika-upādānādidukāni = 22-69-82. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စွဲလမ်းမှု စသည်တို့၏ နှစ်မျိုးတွဲများ
- 22-83. Sanidassanattika-piṭṭhidukaṃ = 22-83. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် နောက်ဆုံး နှစ်မျိုးတွဲများ
- 1-1. Kusalattika-vedanāttikaṃ = 1-1. ကုသိုလ် သုံးမျိုးတွဲနှင့် ခံစားမှု သုံးမျိုးတွဲ
- 1-2. Kusalattika-vipākattikaṃ = 1-2. ကုသိုလ် သုံးမျိုးတွဲနှင့် ကံ၏ အကျိုး သုံးမျိုးတွဲ
- 1-3. Kusalattika-upādinnattikaṃ = 1-3. ကုသိုလ် သုံးမျိုးတွဲနှင့် ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ
- 1-4. Kusalattika-saṃkiliṭṭhattikaṃ = 1-4. ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ
- 1-5. Kusalattika-vitakkattikaṃ = 1-5. ကုသိုလ် သုံးမျိုးတွဲနှင့် စတင်ကြံစည်မှု သုံးမျိုးတွဲ
- 1-6. Kusalattika-pītittikaṃ = 1-6. ကုသိုလ် သုံးမျိုးတွဲနှင့် ပီတိ သုံးမျိုးတွဲ
- 1-7-12. Kusalattika-dassanādittikāni = 1-7-12. ကုသိုလ် သုံးမျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း စသည်တို့၏ သုံးမျိုးတွဲများ
- 1-13-20. Kusalattika-hīnādittikāni = 1-13-20. ကုသိုလ် သုံးမျိုးတွဲနှင့် ယုတ်ညံ့ခြင်း စသည်တို့၏ သုံးမျိုးတွဲများ
- 1-21. Kusalattika-sanidassanattikaṃ = 1-21. ကုသိုလ် သုံးမျိုးတွဲနှင့် မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ
- 2-1. Vedanāttika-kusalattikaṃ = 2-1. ခံစားမှု သုံးမျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 2-2. Vedanāttika-vipākattikaṃ = 2-2. ခံစားမှု သုံးမျိုးတွဲနှင့် ကံ၏ အကျိုး သုံးမျိုးတွဲ
- 3-1. Vipākattika-kusalattikaṃ = 3-1. ကံ၏ အကျိုး သုံးမျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 4-1. Upādinnattika-kusalattikaṃ = 4-1. ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 5-1. Saṃkiliṭṭhattika-kusalattikaṃ = 5-1. ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 6-21-1. Vitakkādittikāni-kusalattikaṃ = 6-21-1. စတင်ကြံစည်မှု စသည်တို့၏ သုံးမျိုးတွဲများနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 22-1. Sanidassanattika-kusalattikaṃ = 22-1. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 22-2-21. Sanidassanattika-vedanādittikāni = 22-2-21. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ခံစားမှု စသည်တို့၏ သုံးမျိုးတွဲများ
- 1-1-5. Hetuduka-sahetukādidukāni = 1-1-5. အမြစ် နှစ်မျိုးတွဲနှင့် အမြစ် ရှိခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 1-6. Hetuduka-cūḷantaradukaṃ = 1-6. အမြစ် နှစ်မျိုးတွဲနှင့် ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်
- 1-13-18. Hetuduka-āsavādigocchakāni = 1-13-18. အမြစ် နှစ်မျိုးတွဲနှင့် စိတ်အစွန်းအထင်း စသည်တို့၏ အစုများ
- 1-19-53. Hetuduka-saññojanādidukāni = 1-19-53. အမြစ် နှစ်မျိုးတွဲနှင့် နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ
- 1-54-81. Hetuduka-mahantaradukaṃ = 1-54-81. အမြစ် နှစ်မျိုးတွဲနှင့် ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး
- 1-82. Hetuduka-piṭṭhidukaṃ = 1-82. အမြစ် နှစ်မျိုးတွဲနှင့် နောက်ဆုံး နှစ်မျိုးတွဲများ
- 2-6-1. Sahetukādidukāni-hetudukaṃ = 2-6-1. အမြစ် ရှိခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများနှင့် အမြစ် နှစ်မျိုးတွဲ
- 7-13-1. Cūḷantaradukāni-hetudukaṃ = 7-13-1. ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်နှင့် အမြစ် နှစ်မျိုးတွဲ
- 14-19-1. Āsavagocchaka-hetudukaṃ = 14-19-1. စိတ်အစွန်းအထင်းတို့၏ အစုနှင့် အမြစ် နှစ်မျိုးတွဲ
- 20-54-1. Saññojanādidukāni-hetudukaṃ = 20-54-1. နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများနှင့် အမြစ် နှစ်မျိုးတွဲ
- 55-68-1. Mahantaradukāni-hetudukaṃ = 55-68-1. ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီးနှင့် အမြစ် နှစ်မျိုးတွဲ
- 69-82-1. Upādānādidukāni-hetudukaṃ = 69-82-1. စွဲလမ်းမှု စသည်တို့၏ နှစ်မျိုးတွဲများနှင့် အမြစ် နှစ်မျိုးတွဲ
- 83-1. Piṭṭhiduka-hetudukaṃ = 83-1. နောက်ဆုံး နှစ်မျိုးတွဲများနှင့် အမြစ် နှစ်မျိုးတွဲ
- 100-2-6. Saraṇaduka-sahetukādidukāni = 100-2-6. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အမြစ် ရှိခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 100-7-13. Saraṇaduka-cūḷantaradukāni = 100-7-13. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်
- 100-14-19. Saraṇaduka-āsavagocchakaṃ = 100-14-19. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် စိတ်အစွန်းအထင်းတို့၏ အစု
- 100-20-54. Saraṇaduka-saññojanādidukāni = 100-20-54. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ
- 100-55-68. Saraṇaduka-mahantaradukāni = 100-55-68. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး
- 100-69-82. Saraṇaduka-upādānādidukāni = 100-69-82. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် စွဲလမ်းမှု စသည်တို့၏ နှစ်မျိုးတွဲများ
- 100-83. Saraṇaduka-dassanādidukāni = 100-83. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 7-8. Sappaccayadukādi = 7-8. အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ စသည်
- 20-49. Saññojanadukādi = 20-49. နှောင်ကြိုး နှစ်မျိုးတွဲ စသည်
- 50-54. Parāmāsadukāni = 50-54. မှားယွင်းသော ယူဆမှု နှစ်မျိုးတွဲများ
- 57-68. Cetasikadukādi = 57-68. စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ စသည်
- 69-74. Upādānagocchakaṃ = 69-74. စွဲလမ်းမှုတို့၏ အစု
- 75-82. Kilesagocchakaṃ = 75-82. ကိလေသာတို့၏ အစု
- 87-88. Savitakkadukādi = 87-88. စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ စသည်
- 89-92. Sappītikadukādi = 89-92. ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ စသည်
- 93-95. Kāmāvacarādidukāni = 93-95. ကာမဘုံနှင့် ဆိုင်ခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 1-2. Hetuduka-vedanāttikaṃ = 1-2. အမြစ် နှစ်မျိုးတွဲနှင့် ခံစားမှု သုံးမျိုးတွဲ
- 1-3. Hetuduka-vipākattikaṃ = 1-3. အမြစ် နှစ်မျိုးတွဲနှင့် ကံ၏ အကျိုး သုံးမျိုးတွဲ
- 1-4. Hetuduka-upādinnattikaṃ = 1-4. အမြစ် နှစ်မျိုးတွဲနှင့် ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ
- 1-5. Hetuduka-saṃkiliṭṭhattikaṃ = 1-5. အမြစ် နှစ်မျိုးတွဲနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ
- 1-6. Hetuduka-vitakkattikaṃ = 1-6. အမြစ် နှစ်မျိုးတွဲနှင့် စတင်ကြံစည်မှု သုံးမျိုးတွဲ
- 1-7. Hetuduka-pītittikaṃ = 1-7. အမြစ် နှစ်မျိုးတွဲနှင့် ပီတိ သုံးမျိုးတွဲ
- 1-8. Hetuduka-dassanattikaṃ = 1-8. အမြစ် နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲ
- 1-9. Hetuduka-dassanahetuttikaṃ = 1-9. အမြစ် နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲ
- 1-10. Hetuduka-ācayagāmittikaṃ = 1-10. အမြစ် နှစ်မျိုးတွဲနှင့် စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲ
- 1-11. Hetuduka-sekkhattikaṃ = 1-11. အမြစ် နှစ်မျိုးတွဲနှင့် ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲ
- 1-12. Hetuduka-parittattikaṃ = 1-12. အမြစ် နှစ်မျိုးတွဲနှင့် အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ
- 1-13. Hetuduka-parittārammaṇattikaṃ = 1-13. အမြစ် နှစ်မျိုးတွဲနှင့် အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- 1-14. Hetuduka-hīnattikaṃ = 1-14. အမြစ် နှစ်မျိုးတွဲနှင့် ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ
- 1-15. Hetuduka-micchattaniyatattikaṃ = 1-15. အမြစ် နှစ်မျိုးတွဲနှင့် မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ
- 1-16. Hetuduka-maggārammaṇattikaṃ = 1-16. အမြစ် နှစ်မျိုးတွဲနှင့် မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- 1-17. Hetuduka-uppannattikaṃ = 1-17. အမြစ် နှစ်မျိုးတွဲနှင့် ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲ
- 1-18. Hetuduka-atītattikaṃ = 1-18. အမြစ် နှစ်မျိုးတွဲနှင့် အတိတ် သုံးမျိုးတွဲ
- 1-19. Hetuduka-atītārammaṇattikaṃ = 1-19. အမြစ် နှစ်မျိုးတွဲနှင့် အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- 1-20. Hetuduka-ajjhattārammaṇattikaṃ = 1-20. အမြစ် နှစ်မျိုးတွဲနှင့် မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- 1-21. Hetuduka-sanidassanattikaṃ = 1-21. အမြစ် နှစ်မျိုးတွဲနှင့် မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ
- 2-1. Sahetukaduka-kusalattikaṃ = 2-1. အမြစ် ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 3-1. Hetusampayuttaduka-kusalattikaṃ = 3-1. အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 4-5-1. Hetusahetukādidukāni-kusalattikaṃ = 4-5-1. အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 7-8-1. Sappaccayādidukāni-kusalattikaṃ = 7-8-1. အကြောင်း ရှိခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 9-10-1. Sanidassanādidukāni-kusalattikaṃ = 9-10-1. မြင်နိုင်ခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 11-1. Rūpīduka-kusalattikaṃ = 11-1. ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 12-1. Lokiyaduka-kusalattikaṃ = 12-1. လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 13-1. Kenaciviññeyyaduka-kusalattikaṃ = 13-1. တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 14-1. Āsavaduka-kusalattikaṃ = 14-1. စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 15-1. Sāsavaduka-kusalattikaṃ = 15-1. စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 16-1. Āsavasampayuttaduka-kusalattikaṃ = 16-1. စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 17-18-1. Āsavasāsavādidukāni-kusalattikaṃ = 17-18-1. စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 19-1. Āsavavippayuttasāsavaduka-kusalattikaṃ = 19-1. စိတ်အစွန်းအထင်းနှင့် ကင်းကွာခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 20-54-1. Saññojanādidukāni-kusalattikaṃ = 20-54-1. နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 55-1. Sārammaṇaduka-kusalattikaṃ = 55-1. အာရုံ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 56-1. Cittaduka-kusalattikaṃ = 56-1. စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 57-1. Cetasikaduka-kusalattikaṃ = 57-1. စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 58-1. Cittasampayuttaduka-kusalattikaṃ = 58-1. စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 59-1. Cittasaṃsaṭṭhaduka-kusalattikaṃ = 59-1. စိတ်နှင့် ရောနှောခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 60-1. Cittasamuṭṭhānaduka-kusalattikaṃ = 60-1. စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 61-1. Cittasahabhūduka-kusalattikaṃ = 61-1. စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 62-1. Cittānuparivattiduka-kusalattikaṃ = 62-1. စိတ်နောက်သို့ လိုက်ပါခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 63-1. Cittasaṃsaṭṭhasamuṭṭhānaduka-kusalattikaṃ = 63-1. စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 64-1. Cittasaṃsaṭṭhasamuṭṭhānasahabhūduka-kusalattikaṃ = 64-1. စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 65-1. Cittasaṃsaṭṭhasamuṭṭhānānuparivattiduka-kusalattikaṃ = 65-1. စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 66-1. Ajjhattikaduka-kusalattikaṃ = 66-1. အတွင်းပိုင်း ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 67-1. Upādāduka-kusalattikaṃ = 67-1. မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 68-1. Upādinnaduka-kusalattikaṃ = 68-1. ကံကြောင့် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- dvi (gocchakāni) = နှစ်ခု
- 69-82-1. Dvigocchakāni-kusalattikaṃ = 69-82-1. အစု နှစ်ခုနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 83-1. Dassanenapahātabbaduka-kusalattikaṃ = 83-1. သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 84-1. Bhāvanāyapahātabbaduka-kusalattikaṃ = 84-1. ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 85-1. Dassanenapahātabbahetukaduka-kusalattikaṃ = 85-1. သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 86-1. Bhāvanāyapahātabbahetukaduka-kusalattikaṃ = 86-1. ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 87-1. Savitakkaduka-kusalattikaṃ = 87-1. စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 88-1. Savicāraduka-kusalattikaṃ = 88-1. ဆက်လက်သုံးသပ်မှု ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 89-1. Sappītikaduka-kusalattikaṃ = 89-1. ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 90-1. Pītisahagataduka-kusalattikaṃ = 90-1. ပီတိနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 91-1. Sukhasahagataduka-kusalattikaṃ = 91-1. သာယာမှုနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 92-1. Upekkhāsahagataduka-kusalattikaṃ = 92-1. ဥပေက္ခာနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 93-1. Kāmāvacaraduka-kusalattikaṃ = 93-1. ကာမဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 94-1. Rūpāvacaraduka-kusalattikaṃ = 94-1. သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 95-1. Arūpāvacaraduka-kusalattikaṃ = 95-1. ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 96-1. Pariyāpannaduka-kusalattikaṃ = 96-1. ဘဝဘုံတို့၌ အကျုံးဝင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 97-1. Niyyānikaduka-kusalattikaṃ = 97-1. လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 98-1. Niyataduka-kusalattikaṃ = 98-1. ကျိန်းသေခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 99-1. Sauttaraduka-kusalattikaṃ = 99-1. ထိုထက် သာလွန်သည် ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 100-1. Saraṇaduka-kusalattikaṃ = 100-1. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
- 100-2. Saraṇaduka-vedanāttikaṃ = 100-2. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ခံစားမှု သုံးမျိုးတွဲ
- 100-3. Saraṇaduka-vipākattikaṃ = 100-3. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကံ၏ အကျိုး သုံးမျိုးတွဲ
- 100-4. Saraṇaduka-upādinnattikaṃ = 100-4. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ
- 100-5. Saraṇaduka-saṃkiliṭṭhattikaṃ = 100-5. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ
- 100-6. Saraṇaduka-vitakkattikaṃ = 100-6. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် စတင်ကြံစည်မှု သုံးမျိုးတွဲ
- 100-7. Saraṇaduka-pītittikaṃ = 100-7. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ပီတိ သုံးမျိုးတွဲ
- 100-8. Saraṇaduka-dassanattikaṃ = 100-8. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲ
- 100-9. Saraṇaduka-dassanahetuttikaṃ = 100-9. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲ
- 100-10. Saraṇaduka-ācayagāmittikaṃ = 100-10. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲ
- 100-11. Saraṇaduka-sekkhattikaṃ = 100-11. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲ
- 100-12. Saraṇaduka-parittattikaṃ = 100-12. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ
- 100-13. Saraṇaduka-parittārammaṇattikaṃ = 100-13. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- 100-14. Saraṇaduka-hīnattikaṃ = 100-14. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ
- 100-15. Saraṇaduka-micchattaniyatattikaṃ = 100-15. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ
- 100-16. Saraṇaduka-maggārammaṇattikaṃ = 100-16. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- 100-17. Saraṇaduka-uppannattikaṃ = 100-17. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲ
- 100-18. Saraṇaduka-atītattikaṃ = 100-18. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အတိတ် သုံးမျိုးတွဲ
- 100-19. Saraṇaduka-atītārammaṇattikaṃ = 100-19. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- 100-21. Saraṇaduka-ajjhattārammaṇattikaṃ = 100-21. ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- 1-3. Kusalattika-hetusampayuttadukaṃ = 1-3. ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- 1-4. Kusalattika-hetusahetukadukaṃ = 1-4. ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- 1-5. Kusalattika-hetuhetusampayuttadukaṃ = 1-5. ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- 1-6. Kusalattika-hetusahetukadukaṃ = 1-6. ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- 1-7-8. Kusalattika-sappaccayādidukāni = 1-7-8. ကုသိုလ် သုံးမျိုးတွဲနှင့် အကြောင်း ရှိခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 1-9. Kusalattika-sanidassanadukaṃ = 1-9. ကုသိုလ် သုံးမျိုးတွဲနှင့် မြင်နိုင်ခြင်း နှစ်မျိုးတွဲ
- 1-10. Kusalattika-sappaṭighadukaṃ = 1-10. ကုသိုလ် သုံးမျိုးတွဲနှင့် ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- 1-11. Kusalattika-rūpīdukaṃ = 1-11. ကုသိုလ် သုံးမျိုးတွဲနှင့် ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 1-12. Kusalattika-lokiyadukaṃ = 1-12. ကုသိုလ် သုံးမျိုးတွဲနှင့် လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- 1-13. Kusalattika-kenaciviññeyyadukaṃ = 1-13. ကုသိုလ် သုံးမျိုးတွဲနှင့် တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲ
- 1-20-54. Kusalattika-chagocchakadukāni = 1-20-54. ကုသိုလ် သုံးမျိုးတွဲနှင့် အစု ခြောက်ခု၏ နှစ်မျိုးတွဲများ
- 1-55. Kusalattika-sārammaṇadukaṃ = 1-55. ကုသိုလ် သုံးမျိုးတွဲနှင့် အာရုံ ရှိခြင်း နှစ်မျိုးတွဲ
- 1-56. Kusalattika-cittadukaṃ = 1-56. ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 1-57. Kusalattika-cetasikadukaṃ = 1-57. ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 1-58. Kusalattika-cittasampayuttadukaṃ = 1-58. ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- 1-59. Kusalattika-cittasaṃsaṭṭhadukaṃ = 1-59. ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်နှင့် ရောနှောခြင်း နှစ်မျိုးတွဲ
- 1-60. Kusalattika-cittasamuṭṭhānadukaṃ = 1-60. ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲ
- 1-61. Kusalattika-cittasahabhūdukaṃ = 1-61. ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲ
- 1-62-65. Kusalattika-cittānuparivattādidukāni = 1-62-65. ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်နောက်သို့ လိုက်ပါခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 1-66-68. Kusalattika-ajjhattikādidukāni = 1-66-68. ကုသိုလ် သုံးမျိုးတွဲနှင့် အတွင်းပိုင်း ဖြစ်ခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 3-1. Vipākattika-hetudukaṃ = 3-1. ကံ၏ အကျိုး သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 4-1. Upādinnattika-hetudukaṃ = 4-1. ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 5-1. Saṃkiliṭṭhattika-hetudukaṃ = 5-1. ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 6-1. Vitakkattika-hetudukaṃ = 6-1. စတင်ကြံစည်မှု သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 7-1. Pītittika-hetudukaṃ = 7-1. ပီတိ သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 8-1. Dassanattika-hetudukaṃ = 8-1. သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 9-1. Dassanahetuttika-hetudukaṃ = 9-1. သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 10-1. Ācayagāmittika-hetudukaṃ = 10-1. စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 11-1. Sekkhattika-hetudukaṃ = 11-1. ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 12-1. Parittattika-hetudukaṃ = 12-1. အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 13-1. Parittārammaṇattika-hetudukaṃ = 13-1. အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 14-1. Hīnattika-hetudukaṃ = 14-1. ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 15-1. Micchattaniyatattika-hetudukaṃ = 15-1. မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 16-1. Maggārammaṇattika-hetudukaṃ = 16-1. မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 17-1. Uppannattika-hetudukaṃ = 17-1. ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 18-1. Atītattika-hetudukaṃ = 18-1. အတိတ် သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 19-1. Atītārammaṇattika-hetudukaṃ = 19-1. အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 20-1. Ajjhattattika-hetudukaṃ = 20-1. မိမိ၌ ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 21-1. Ajjhattārammaṇattika-hetudukaṃ = 21-1. မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 22-1. Sanidassanattika-hetudukaṃ = 22-1. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- 22-2. Sanidassanattika-sahetukadukaṃ = 22-2. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- 22-3. Sanidassanattika-hetusampayuttadukaṃ = 22-3. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- 22-4. Sanidassanattika-hetusahetukadukaṃ = 22-4. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- 22-5. Sanidassanattika-hetuhetusampayuttadukaṃ = 22-5. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- 22-6. Sanidassanattika-nahetusahetukadukaṃ = 22-6. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- 22-7. Sanidassanattika-sappaccayadukaṃ = 22-7. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ
- 22-9. Sanidassanattika-sanidassanadukaṃ = 22-9. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် မြင်နိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-10. Sanidassanattika-sappaṭighadukaṃ = 22-10. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- 22-11. Sanidassanattika-rūpīdukaṃ = 22-11. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-12. Sanidassanattika-lokiyadukaṃ = 22-12. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-13. Sanidassanattika-kenaciviññeyyadukaṃ = 22-13. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-14. Sanidassanattika-āsavadukaṃ = 22-14. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲ
- 22-15. Sanidassanattika-sāsavadukaṃ = 22-15. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-16. Sanidassanattika-āsavasampayuttadukaṃ = 22-16. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- 22-17. Sanidassanattika-āsavasāsavadukaṃ = 22-17. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-18. Sanidassanattika-āsavaāsavasampayuttadukaṃ = 22-18. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- 22-19. Sanidassanattika-āsavavippayuttasāsavadukaṃ = 22-19. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်းနှင့် ကင်းကွာခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-20-54. Sanidassanattika-saññojanādidukāni = 22-20-54. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ
- 22-55. Sanidassanattika-sārammaṇadukaṃ = 22-55. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အာရုံ ရှိခြင်း နှစ်မျိုးတွဲ
- 22-56. Sanidassanattika-cittadukaṃ = 22-56. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-57. Sanidassanattika-cetasikadukaṃ = 22-57. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-58. Sanidassanattika-cittasampayuttadukaṃ = 22-58. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- 22-59. Sanidassanattika-cittasaṃsaṭṭhadukaṃ = 22-59. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်နှင့် ရောနှောခြင်း နှစ်မျိုးတွဲ
- 22-60. Sanidassanattika-cittasamuṭṭhānadukaṃ = 22-60. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲ
- 22-61. Sanidassanattika-cittasahabhūdukaṃ = 22-61. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲ
- 22-62. Sanidassanattika-cittānuparivattidukaṃ = 22-62. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်နောက်သို့ လိုက်ပါခြင်း နှစ်မျိုးတွဲ
- 22-63-65. Sanidassanattika-cittasaṃsaṭṭhasamuṭṭhānādidukāni = 22-63-65. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း စသည်တို့၏ နှစ်မျိုးတွဲများ
- 22-66. Sanidassanattika-ajjhattadukaṃ = 22-66. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အတွင်းပိုင်း ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-67. Sanidassanattika-upādādukaṃ = 22-67. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-68. Sanidassanattika-upādinnadukaṃ = 22-68. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ကံကြောင့် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-83. Sanidassanattika-dassanenapahātabbadukaṃ = 22-83. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ
- 22-84. Sanidassanattika-bhāvanāyapahātabbadukaṃ = 22-84. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ
- 22-85. Sanidassanattika-dassanenapahātabbahetukadukaṃ = 22-85. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲ
- 22-86. Sanidassanattika-bhāvanāyapahātabbahetukadukaṃ = 22-86. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲ
- 22-87. Sanidassanattika-savitakkadukaṃ = 22-87. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- 22-88. Sanidassanattika-savicāradukaṃ = 22-88. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ဆက်လက်သုံးသပ်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- 22-89. Sanidassanattika-sappītikadukaṃ = 22-89. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ
- 22-90. Sanidassanattika-pītisahagatadukaṃ = 22-90. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ပီတိနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-91. Sanidassanattika-sukhasahagatadukaṃ = 22-91. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် သာယာမှုနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-92. Sanidassanattika-upekkhāsahagatadukaṃ = 22-92. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ဥပေက္ခာနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- 22-93. Sanidassanattika-kāmāvacaradukaṃ = 22-93. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ကာမဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-94. Sanidassanattika-rūpāvacaradukaṃ = 22-94. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-95. Sanidassanattika-arūpāvacaradukaṃ = 22-95. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- 22-96. Sanidassanattika-pariyāpannadukaṃ = 22-96. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ဘဝဘုံတို့၌ အကျုံးဝင်ခြင်း နှစ်မျိုးတွဲ
- 22-97. Sanidassanattika-niyyānikadukaṃ = 22-97. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း နှစ်မျိုးတွဲ
- 22-98. Sanidassanattika-niyatadukaṃ = 22-98. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ကျိန်းသေခြင်း နှစ်မျိုးတွဲ
- 22-99. Sanidassanattika-sauttaradukaṃ = 22-99. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ထိုထက် သာလွန်သည် ရှိခြင်း နှစ်မျိုးတွဲ
- 22-100. Sanidassanattika-saraṇadukaṃ = 22-100. မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ

(Plus the per-part heading lines «<num> X-Y» = «<num> <X name>နှင့် <Y name>», composed from the finished groups'
dyad / triad / group names; they are in the list above as printed by `--new`.)

## Check results (2026-11-24, final files)
| chapter | segments | check_chapter_ids | check_text (folded copy) | check_marks |
|---|---|---|---|---|
| 5-05-paccaniya-dukatika | 119 | OK | OK (215 lines) | OK |
| 5-06-paccaniya-tikaduka | 114 | OK | OK (187 lines) | OK |
| 5-07-paccaniya-tikatika | 110 | OK | OK (185 lines) | OK |
| 5-08-paccaniya-dukaduka | 82 | OK | OK (210 lines) | OK |
| 5-09-anulomapaccaniya-tika | 145 | OK | OK (229 lines) | OK |
| 5-10-anulomapaccaniya-duka | 127 | OK | OK (226 lines) | OK |
| 5-11-anulomapaccaniya-dukatika | 203 | OK | OK (378 lines) | OK |
| 5-12-anulomapaccaniya-tikaduka | 252 | OK | OK (408 lines) | OK |

- check_ch5-05-12.py (all eight): 0 mismatches (S 2038, C 2038, O 1578, P 1578, N 2038, I 3169, T 376); reuse: terms
  154 / 154 witnessed in the finished chapters, sentences 123 / 123 identical with pi-1 … pi-6; identity with the
  finished groups (1-00 … 4-14, 5-01 … 5-04): 123 / 123 sentences identical; `--mutate` 13 / 13 planted errors caught.
- The text check was run on a «…Pe…»-folded copy in chk-pe/ch5-05-12/ (only that folder deleted afterwards);
  check_text_pe7.py was not run.
- Regenerating (`--out` to a scratch folder) gives byte-identical files.
