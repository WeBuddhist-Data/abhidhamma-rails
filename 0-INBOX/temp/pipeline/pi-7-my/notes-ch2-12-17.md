# Notes: Burmese zero-shot pi-7 2-12 … 2-17 (uppannattika, atītattika, atītārammaṇattika, ajjhattattika,
# ajjhattārammaṇattika, sanidassanasappaṭighattika)

Generator `make_ch2-12-17.py`, check `check_ch2-12-17.py`. Translated from the Pāli only (no Burmese translation or
nissaya opened, no language-priority folder, no web). Brief: `burmese-zeroshot-brief.md` + coordinator decisions.

## Method
- Engine: `make_ch2-03-06.py` is IMPORTED (its setup() runs, its main() does not). It brings the primary engine
  (my7_formulas + make_sample + make_ch1-01) and the isolated per-sentence fallback (make_ch1-03-05 on its own module
  copy), plus all 2-03 … 2-06 extensions. `--regress` regenerates 1-00, 1-02 and 2-03 … 2-06 in memory: all identical.
- Only the chapter's own triad is active while it is translated (as 2-03 … 2-06). uppādī (-in stem) read with
  a-stem endings in memory (uppādī → uppādo / uppādā / uppāde before khandhā / khandhe; uppādiṃ → uppādaṃ).
- NEW fallback "term-strip": a unit no frame takes because a triad term stands before a noun that is not dhamma
  (2-17: «anidassanasappaṭighe mahābhūte paṭicca sanidassanasappaṭighaṃ cittasamuṭṭhānaṃ rūpaṃ …», 2-15: «ajjhatto
  kabaḷīkāro āhāro bahiddhā kāyassa …») is translated without those terms by the existing frames; each term is put
  back right before the Burmese of the word it stood before. Stacked terms «Xañca Yañca N» = «X၊ Y N» (as 1-01's
  stacked abyākata qualifiers). A «-ñca» term after a noun list moves its «ca» to the noun («tayo khandhā Xañca
  cittasamuṭṭhānaṃ rūpaṃ» = «… cittasamuṭṭhānañca rūpaṃ» + X). The term order is re-checked by check (O).
- Another triad's words used as plain adjectives (2-14 atīta / anāgata / paccuppanna; 2-16 ajjhatta / bahiddhā)
  take the pi-1 Mātikā values (kind «adj»); the check counts them as terms in those chapters.
- A run of locative conditions cut by «…pe…» («naadhipatiyā naanantare … naupanissaye…pe… novigate ekaṃ») is rendered
  as 2-03 … 2-06's runs (each condition in the locative, «၊» between).
- Notes holding a triad term or two sentences (and the ghaṭanā notes «(avipākaṃ-4)» «(savipākaṃ-5)») are replaced by
  a placeholder in memory (NOTEP, as 2-07 … 2-11's NOTEP); the check reads the raw Pāli.

## Coordinator decisions applied
- Sahajātā (kind label) = bare «အတူ ပေါ်ပေါက်ခြင်း»; in the kamma note «sahajātā nānākkhaṇikā» = the kamma kinds
  «အတူ ပေါ်ပေါက်သည့် ကံ၊ ခဏ ကွဲပြားသည့် ကံ» (LEX of the sample).
- asaññasattānaṃ = 1-01's «အသညသတ်တို့၏» (also on the fallback copy, via 2-03 … 2-06).
- Triads = pi-1 final Mātikā ^1-M1-17 … ^1-M1-22 (witnessed); bahiddhā = «မိမိ၏ ပြင်ပ၌ ရှိသော» (pi-1 termbase sense 2).

## Source slips (translated as the usual form; logged by --slips)
- 2-12 «sotudhātuyā» = sotadhātuyā; 2-13 «vipāko paccuppano eko» = paccuppanno; 2-17 «kaṭatārūpaṃ» = kaṭattārūpaṃ.
- 2-13 «ghānasampadaṃ jivhāsampadaṃ» and «paccuppannaṃ bhojanaṃ senāsanaṃ» have no «…pe…» between the two objects:
  translated as written, joined by «၊».
- 2-17 ghaṭanā: «aññamaññanissaya», «nissayavipāka», «atthiavigatanti» (no hyphen), «atthi -avigatanti» (space):
  read as the hyphenated compounds (engine slip log).
- 2-14 / 2-15 / 2-16 inherited 2-03 … 2-06 slip readings: «Natthivigatāvigatapaccayā» = Natthi-vigatāvigatapaccayā.

## Unsure Pāli (meaning choices, for review)
- 2-15 «paro ajjhattaṃ cakkhuṃ … vipassati»: paro = «သူတစ်ပါးသည်» (another person contemplates one's internal eye).
- 2-15 «(vatthuṃ atirekaṃ, …)» = «မှီရာ ဝတ္ထု ပိုသည်» (the base is additional).
- 2-15 «(purimā purimā bahiddhāti nānākaraṇaṃ, taṃyeva gamanaṃ)» = the difference is «ရှေးရှေး … bahiddhā», the
  rest the same course; no quote marks (the Pāli has none).
- 2-17 «(saṃkhittaṃ, asaññasattānañca kātabbā)» = «အသညသတ်တို့ကိုလည်း ပြုရမည်» (the genitive read as "for them too").
- 2-17 «adhipati tividharūpasaṅgahena» = «အကြီးအမှူးကို ရုပ် သုံးမျိုးကို စုစည်းခြင်းဖြင့်»; «rūpajīvitindriyañca
  ante ante» = «… ကိုလည်း အဆုံးတိုင်း၌».
- 2-17 «paṭisandhipi kaṭattāpi natthi»: kaṭattā = kaṭattārūpa «ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်».

## For the consistency pass (harmonise)
- Shared count runs «… atthiyā avigate ekaṃ»: the last condition before the count gets no «၊» (same as 2-03 … 2-06,
  kept for identity).
- 1-05 renders «vatthupurejātaṃ – cakkhāyatanaṃ cakkhuviññāṇassa…» as «မျက်စိ အာရုံခံ နယ်ပယ်၊ မျက်စိ သိစိတ်တို့အား…»
  (a list); these chapters (1-01 engine) have «… နယ်ပယ်သည် မျက်စိ သိစိတ်အား…» (2 sentences of 2-17; the only
  differences from the finished groups: 89 / 91 identical).
- anumajjantena: 2-03 … 2-06 «ပြန်လည် စိစစ်လျက်» (used here) vs 2-01 … 2-02 «အစဉ်လိုက် သုံးသပ်လျက်».
- New engine words not built with new(): paro «သူတစ်ပါး» (2-03 … 2-06 para-), āpodhātu «ရေဓာတ်», itthindriyaṃ
  «မိန်းမ၏ စွမ်းရည်», purisindriyaṃ «ယောက်ျား၏ စွမ်းရည်», jīvitindriyaṃ «အသက်၏ စွမ်းရည်», indriyaṃ «စွမ်းရည်»
  (pi-1 witnessed); kāyassa «ကိုယ်»; dibbaṃ cakkhuṃ / dibbaṃ sotadhātuṃ (1-01 values); the higher knowledges as
  objects «…ဉာဏ်ကို ပြန်လည် ဆင်ခြင်သည် / လေးစားဖွယ်ရာ ပြု၍»; «dve mahābhūtā…» = «မူလဓာတ်ကြီး နှစ်ပါး…» (as «dve khandhā»;
  the shared LEX count word «dve» would put «နှစ်ခု» first); ajjhattikā indriyā «အတွင်းပိုင်း ဖြစ်သော စွမ်းရည်များ»;
  utusamuṭṭhānā «ရာသီဥတုမှ ဖြစ်ပေါ်လာသော»; numbers dvāvīsa / bāvīsa / catuvīsa / dvādasa / tevīsa = the 1-03 … 1-05 values.
- Headings: «Paccanīyānulomaṃ» (heading) = «အငြင်းပြ အဟုတ်ပြ ပုံစံ» (the line's value); «*2-6. Sahajāta-…*» as
  2-01 … 2-02; colophons «Pañhāvāro niṭṭhito.» «“ပြဿနာအလိုက် ဖော်ပြချက်” ပြီးဆုံးပြီ။», «Dhammānulome tikapaṭṭhānaṃ
  niṭṭhitaṃ.» «သဘောတရား အဟုတ်ပြ ပုံစံ၌ “သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။».

## Results (2026-11-23)
| chapter | segments | lines | own check | reuse terms | reuse sentences |
|---|---|---|---|---|---|
| 2-12 | 50 | 61 | 0 | 41/41 | 24/24 |
| 2-13 | 47 | 61 | 0 | 56/56 | 23/23 |
| 2-14 | 93 | 145 | 0 | 35/35 | 71/71 |
| 2-15 | 128 | 183 | 0 | 71/71 | 72/72 |
| 2-16 | 67 | 99 | 0 | 37/37 | 36/36 |
| 2-17 | 133 | 241 | 0 | 79/79 | 74/74 |
All six: check_chapter_ids OK, check_marks OK, check_text (folded copy in chk-pe/ch2-12-17/, deleted) OK; own check
0 mismatches, reuse 85/85 terms + 300/300 sentences, mutation 10/10, sample identity (raw and prep) identical,
--regress 1-00 / 1-02 / 2-03 … 2-06 identical.

## New strings (Pāli = Burmese)
- pañcavīsa(ti) = နှစ်ဆယ့်ငါး
- Uppannattikaṃ = ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲ
- Atītattikaṃ = အတိတ် သုံးမျိုးတွဲ
- Atītārammaṇattikaṃ = အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- Ajjhattattikaṃ = မိမိ၌ ရှိခြင်း သုံးမျိုးတွဲ
- Ajjhattārammaṇattikaṃ = မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- Sanidassanasappaṭighattikaṃ = မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ
- patthayamāno = တောင့်တလျက်
- paṭisandhicittaṃ = ပဋိသန္ဓေ စိတ်
- iminā kāraṇena = ဤနည်းလမ်းဖြင့်
- avasesā (attributive) = ကြွင်းသော
- -mūlakā (attributive) = ကို အခြေခံသော
- ninnānākaraṇaṃ / -ā = ကွဲပြားချက် မရှိ
- tividharūpasaṅgaho = ရုပ် သုံးမျိုးကို စုစည်းခြင်း
- vibhajitvā = ခွဲခြမ်းစိတ်ဖြာ၍
- Dutiyo bhāgo niṭṭhito. = ဒုတိယ အပိုင်း ပြီးဆုံးပြီ။
- -paccuppannacittasamaṅgissa = ပစ္စုပ္ပန် စိတ်နှင့် ပြည့်စုံသူ
- -bahiddhācittasamaṅgissa = မိမိ၏ ပြင်ပ၌ ရှိသော စိတ်နှင့် ပြည့်စုံသူ
- aniccānupassanā = မမြဲဟု အဖန်ဖန် ရှုခြင်း
- dukkhānupassanā = ဆင်းရဲဟု အဖန်ဖန် ရှုခြင်း
- anattānupassanā = အတ္တ မဟုတ်ဟု အဖန်ဖန် ရှုခြင်း
- vaṇṇasampadā = အဆင်းအရောင် ပြည့်စုံခြင်း
- saddasampadā = အသံ ပြည့်စုံခြင်း
- gandhasampadā = အနံ့ ပြည့်စုံခြင်း
- rasasampadā = အရသာ ပြည့်စုံခြင်း
- phoṭṭhabbasampadā = အထိအတွေ့ ပြည့်စုံခြင်း
- cakkhusampadā = မျက်စိ ပြည့်စုံခြင်း
- sotasampadā = နား ပြည့်စုံခြင်း
- ghānasampadā = နှာခေါင်း ပြည့်စုံခြင်း
- jivhāsampadā = လျှာ ပြည့်စုံခြင်း
- kāyasampadā = ကိုယ် ပြည့်စုံခြင်း
- pañcaviññāṇasahagataṃ = သိစိတ် ငါးပါးနှင့်အတူ ဖြစ်သော
- atirekaṃ = ပိုသည်
- pacchā = နောက်၌
- pañcāyatanāni = အာရုံခံ နယ်ပယ် ငါးပါး
- sādhukaṃ = ကောင်းစွာ
- ante ante = အဆုံးတိုင်း၌
- yāva X = အထိ
- pariyosānapadā = အဆုံးသတ် ပုဒ်တို့
- niṭṭhānapadā = အပြီးသတ် ပုဒ်တို့
- Nissaya-saṃsaṭṭha-sampayuttavāro = အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်
TRIADS
- uppann- = ဖြစ်ပေါ်ပြီးသော
- anuppann- = မဖြစ်ပေါ်သေးသော
- uppād- = ဖြစ်ပေါ်လာမည့်
- atīt- = အတိတ်
- anāgat- = အနာဂတ်
- paccuppann- = ပစ္စုပ္ပန်
- atītārammaṇ- = အတိတ်ကို အာရုံပြုသော
- anāgatārammaṇ- = အနာဂတ်ကို အာရုံပြုသော
- paccuppannārammaṇ- = ပစ္စုပ္ပန်ကို အာရုံပြုသော
- ajjhatt- = မိမိ၌ ရှိသော
- bahiddh- = မိမိ၏ ပြင်ပ၌ ရှိသော
- ajjhattabahiddh- = မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော
- ajjhattārammaṇ- = မိမိ၌ ရှိသည်ကို အာရုံပြုသော
- bahiddhārammaṇ- = မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော
- ajjhattabahiddhārammaṇ- = မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော
- sanidassanasappaṭigh- = မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိသော
- anidassanasappaṭigh- = မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော
- anidassanaappaṭigh- = မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော
NOTES
- (uppannattike atthisadisaṃ) = (ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲ၌ ရှိခြင်းနှင့် တူသည်)
- (imesu padesu ekaṃyeva) = (ဤ ပုဒ်တို့၌ တစ်ခုပင်)
- (purejātepi āsevanepi paṭisandhi natthi) = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း၌လည်း၊ အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း၌လည်း ပဋိသန္ဓေ မရှိ)
- (anulomasahajātasadisaṃ) = (အဟုတ်ပြ ပုံစံ၌ အတူ ပေါ်ပေါက်ခြင်းနှင့် တူသည်)
- (ninnānākaraṇaṃ) = (ကွဲပြားချက် မရှိ)
- (nahetusadisā tisso pañhā , moho natthi) = (အမြစ် မဟုတ်ခြင်းနှင့် တူကြသည်၊ ပြဿနာ သုံးခု၊ မောဟ မရှိ)
- (moho natthi) = (မောဟ မရှိ)
- (tayopi paccayā paṭiccavārasadisā) = (အကြောင်း သုံးပါးလုံးလည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)
- (sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)
- (sahajātavāropi paccayavāropi nissayavāropi paṭiccavārasadisā , saṃsaṭṭhavāropi sampayuttavāropi arūpeyeva kātabbā) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ရုပ် မဟုတ်သော သဘောတရား၌သာ ပြုရမည်)
- (pavattipaṭisandhi kātabbā) = (ဘဝ ဖြစ်စဉ်ကိုလည်း၊ ပဋိသန္ဓေကိုလည်း ပြုရမည်)
- (pavattipaṭisandhipi mahābhūtāpi kātabbā) = (ဘဝ ဖြစ်စဉ်ကိုလည်း၊ ပဋိသန္ဓေကိုလည်း၊ မူလဓာတ်ကြီးတို့ကိုလည်း ပြုရမည်)
- (vatthuṃ atirekaṃ) = (မှီရာ ဝတ္ထု ပိုသည်)
- (sahajātavāre paripuṇṇā) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌ ပြည့်စုံကြသည်)
- (mahābhūtānaṃ khandhānañca pacchā pañcāyatanāni ca vatthu ca kātabbā) = (မူလဓာတ်ကြီးတို့နှင့် အစုအဝေးတို့၏ နောက်၌ အာရုံခံ နယ်ပယ် ငါးပါးကိုလည်းကောင်း၊ မှီရာ ဝတ္ထုကိုလည်းကောင်း ပြုရမည်)
- (nissayavāro paccayavārasadiso) = (အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်သည် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo) = (ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း အကျယ် ချဲ့ရမည်)
- (ajjhattasadisaṃyeva) = (မိမိ၌ ရှိသော သဘောတရားနှင့်ပင် တူသည်)
- (rūpajīvitindriyampi vitthāretabbaṃ) = (ရုပ် အသက်၏ စွမ်းရည်ကိုလည်း အကျယ် ချဲ့ရမည်)
- (mātikāpadāni anumajjantena vitthāretabbāni) = (ခေါင်းစဉ်စာရင်း ပုဒ်တို့ကို ပြန်လည် စိစစ်လျက် အကျယ် ချဲ့ရမည်)
- (mātikāpadāni vitthāretabbāni) = (ခေါင်းစဉ်စာရင်း ပုဒ်တို့ကို အကျယ် ချဲ့ရမည်)
- (anulomapadāni gaṇetabbāni) = (အဟုတ်ပြ ပုံစံ၏ ပုဒ်တို့ကို ရေတွက်ရမည်)
- (purimā purimā bahiddhāti nānākaraṇaṃ , taṃyeva gamanaṃ) = (ရှေးရှေး မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရားဟူ၍ ကွဲပြားချက် ရှိသည်၊ ထို သွားပုံပင် ဖြစ်သည်)
- (iminā kāraṇena sattapi pañhā vibhajitabbā) = (ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်)
- (iminā kāraṇena satta pañhā vibhajitabbā) = (ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်)
- (iminā kāraṇena satta pañhā vitthāretabbā asammohantena) = (ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုကို မရောထွေးစေဘဲ အကျယ် ချဲ့ရမည်)
- (ghaṭane iminā kāraṇena sattapi pañhā vibhajitabbā) = (ပေါင်းစပ်ချက်၌ ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်)
- (iminā kāraṇena ekavīsa pañhā vibhajitabbā) = (ဤနည်းလမ်းဖြင့် ပြဿနာ နှစ်ဆယ့်တစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်)
- (iminā kāraṇena vibhajitabbā ekavīsāpi) = (ဤနည်းလမ်းဖြင့် နှစ်ဆယ့်တစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်)
- (kammaṃ vibhajitvā nakammeneva ekavīsa pañhā kātabbā) = (ကံကို ခွဲခြမ်းစိတ်ဖြာ၍ ကံဟူသော အကြောင်း မဟုတ်ခြင်းဖြင့်ပင် ပြဿနာ နှစ်ဆယ့်တစ်ခုကို ပြုရမည်)
- (paṭisandhipi kaṭattāpi natthi , pañcavokāreyeva kātabbā) = (ပဋိသန္ဓေလည်း၊ ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်လည်း မရှိ၊ အစုအဝေး ငါးပါး ရှိသော ဘဝ၌သာ ပြုရမည်)
- (saṃkhittaṃ , sabbe pañhā vibhajitabbā) = (အကျဉ်းချုပ်၊ ပြဿနာ အားလုံးကို ခွဲခြမ်းစိတ်ဖြာရမည်)
- (saṃkhittaṃ , sattapi pañhā vibhajitabbā) = (အကျဉ်းချုပ်၊ ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်)
- (evaṃ sattapi pañhā vibhajitabbā) = (ဤသို့ ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်)
- (nahetusadisaṃ kātabbaṃ) = (အမြစ် မဟုတ်ခြင်းနှင့် တူအောင် ပြုရမည်)
- (paripuṇṇaṃ) = (ပြည့်စုံသည်)
- (paṭiccavārasadisaṃ sādhukaṃ kātabbaṃ) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် ကောင်းစွာ ပြုရမည်)
- (aññamaññapaccaye paṭiccavāre aññamaññasadisaṃ , nissayapaccaye paṭiccavārasadisaṃ) = (အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း၌ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အချင်းချင်း ထောက်ပံ့ခြင်းနှင့် တူသည်၊ အမှီဟူသော အကြောင်း၌ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (evaṃ satta pañhā vibhajitabbā , tividharūpasaṅgaho) = (ဤသို့ ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်၊ ရုပ် သုံးမျိုးကို စုစည်းခြင်း)
- (evaṃ satta pañhā sahajātā nānākkhaṇikā iminā kāraṇena vibhajitabbā , tividharūpasaṅgaho) = (ဤသို့ ပြဿနာ ခုနစ်ခုကို အတူ ပေါ်ပေါက်သည့် ကံ၊ ခဏ ကွဲပြားသည့် ကံဟု ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်၊ ရုပ် သုံးမျိုးကို စုစည်းခြင်း)
- (evaṃ satta pañhā vitthāretabbā , pavattipaṭisandhi) = (ဤသို့ ပြဿနာ ခုနစ်ခုကို အကျယ် ချဲ့ရမည်၊ ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း)
- (evaṃ satta pañhā pavattipaṭisandhi vibhajitabbā , sattasupi kabaḷīkāro āhāro kātabbo) = (ဤသို့ ပြဿနာ ခုနစ်ခုကို ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ခွဲခြမ်းစိတ်ဖြာရမည်၊ ခုနစ်ခုလုံး၌လည်း လုတ်ပြု၍ စားရသော အာဟာရကို ပြုရမည်)
- (evaṃ pavattipaṭisandhi satta pañhā vibhajitabbā , rūpajīvitindriyañca ante ante) = (ဤသို့ ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်၊ ရုပ် အသက်၏ စွမ်းရည်ကိုလည်း အဆုံးတိုင်း၌)
- (avasesā pañca pañhā evaṃ vitthāretabbā) = (ကြွင်းသော ပြဿနာ ငါးခုကို ဤသို့ အကျယ် ချဲ့ရမည်)
- (sahajātā , pacchājātā) = (အတူ ပေါ်ပေါက်ခြင်း၊ နောက်မှ ဖြစ်ပေါ်ခြင်း)
- (avasesā cattāro pañhā vitthāretabbā) = (ကြွင်းသော ပြဿနာ လေးခုကို အကျယ် ချဲ့ရမည်)
- (paṭiccavāre sahajātapaccayasadisā , ninnānākaraṇā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ)
- (evaṃ avasesā cha pañhā vibhajitabbā) = (ဤသို့ ကြွင်းသော ပြဿနာ ခြောက်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်)
- (sahajātaṃ , pacchājātaṃ , āhāraṃ , indriyampi kātabbā) = (အတူ ပေါ်ပေါက်ခြင်း၊ နောက်မှ ဖြစ်ပေါ်ခြင်း၊ အာဟာရ၊ စွမ်းရည်ကိုလည်း ပြုရမည်)
- (saṃkhittaṃ , asaññasattānañca kātabbā) = (အကျဉ်းချုပ်၊ အသညသတ်တို့ကိုလည်း ပြုရမည်)
- (yāva asaññasattā kātabbā) = (အသညသတ်တို့အထိ ပြုရမည်)
- (yāva asaññasattā vitthāretabbā) = (အသညသတ်တို့အထိ အကျယ် ချဲ့ရမည်)
- (avasesā catasso pañhā vibhajitabbā) = (ကြွင်းသော ပြဿနာ လေးခုကို ခွဲခြမ်းစိတ်ဖြာရမည်)
- (natthivigatapaccayaṃ anantarasadisaṃ) = (မရှိခြင်းဟူသော အကြောင်း၊ ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းသည် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်)
- (avigatapaccayaṃ atthisadisaṃ) = (မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းသည် ရှိခြင်းနှင့် တူသည်)
- (evaṃ sabbo gaṇanavāro gaṇetabbo) = (ဤသို့ ရေတွက်ခြင်းအလိုက် ဖော်ပြချက် အားလုံးကို ရေတွက်ရမည်)
- (paṭiccavāre nissayapaccayasadisaṃ) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အမှီဟူသော အကြောင်းနှင့် တူသည်)
- (paṭhamagamanasadisaṃ) = (ပထမ သွားပုံနှင့် တူသည်)
- (idhāpi saṃkhittaṃ) = (ဤနေရာ၌လည်း အကျဉ်းချုပ်)
- (anidassanasappaṭighamūlake iminā kāraṇena satta pañhā vibhajitabbā , pariyosānapadā natthi) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်၊ အဆုံးသတ် ပုဒ်တို့ မရှိ)
- (iminā kāraṇena anidassanasappaṭighamūlake satta pañhā vibhajitabbā , niṭṭhānapadā natthi) = (ဤနည်းလမ်းဖြင့် မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်၊ အပြီးသတ် ပုဒ်တို့ မရှိ)
- (anidassanasappaṭighamūlakā satta pañhā iminā kāraṇena vibhajitabbā) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်)
- (anidassanasappaṭighamūlake satta pañhā iminā kāraṇena kātabbā) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ပြဿနာ ခုနစ်ခုကို ဤနည်းလမ်းဖြင့် ပြုရမည်)
- (anidassanasappaṭighamūlake iminā kāraṇena sattapi pañhā vibhajitabbā) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်)
- (anidassanasappaṭighamūlakā iminā kāraṇena satta pañhā vibhajitabbā) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်)
- (anidassanasappaṭighamūlakā iminā kāraṇena sattapi pañhā vitthāretabbā) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ဤနည်းလမ်းဖြင့် အကျယ် ချဲ့ရမည်)
- (anidassanasappaṭighamūlake iminā kāraṇena sattapi pañhā vitthāretabbā) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုလုံးကိုလည်း အကျယ် ချဲ့ရမည်)
- (anidassanasappaṭighamūlakeyeva iminā kāraṇena satta pañhā vibhajitabbā) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံခြင်း၌ပင် ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်)
- (anidassanasappaṭighamūlake sattapi pañhā vibhajitabbā , adhipati tividharūpasaṅgahena) = (မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်၊ အကြီးအမှူးကို ရုပ် သုံးမျိုးကို စုစည်းခြင်းဖြင့်)
- (anidassanaappaṭighamūlake iminā kāraṇena satta pañhā vibhajitabbā , pariyosānapadā natthi) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံခြင်း၌ ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်၊ အဆုံးသတ် ပုဒ်တို့ မရှိ)
- (iminā kāraṇena anidassanaappaṭighamūlake satta pañhā vibhajitabbā , niṭṭhānapadā natthi) = (ဤနည်းလမ်းဖြင့် မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံခြင်း၌ ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်၊ အပြီးသတ် ပုဒ်တို့ မရှိ)
- (anidassanaappaṭighamūlakā satta pañhā iminā kāraṇena vibhajitabbā) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်)
- (anidassanaappaṭighamūlake satta pañhā iminā kāraṇena kātabbā) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံခြင်း၌ ပြဿနာ ခုနစ်ခုကို ဤနည်းလမ်းဖြင့် ပြုရမည်)
- (anidassanaappaṭighamūlake iminā kāraṇena sattapi pañhā vibhajitabbā) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံခြင်း၌ ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်)
- (anidassanaappaṭighamūlakā iminā kāraṇena satta pañhā vibhajitabbā) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်)
- (anidassanaappaṭighamūlakā iminā kāraṇena sattapi pañhā vitthāretabbā) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ဤနည်းလမ်းဖြင့် အကျယ် ချဲ့ရမည်)
- (anidassanaappaṭighamūlake iminā kāraṇena sattapi pañhā vitthāretabbā) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံခြင်း၌ ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုလုံးကိုလည်း အကျယ် ချဲ့ရမည်)
- (anidassanaappaṭighamūlakeyeva iminā kāraṇena satta pañhā vibhajitabbā) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံခြင်း၌ပင် ဤနည်းလမ်းဖြင့် ပြဿနာ ခုနစ်ခုကို ခွဲခြမ်းစိတ်ဖြာရမည်)
- (anidassanaappaṭighamūlake sattapi pañhā vibhajitabbā , adhipati tividharūpasaṅgahena) = (မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော သဘောတရားကို အခြေခံခြင်း၌ ပြဿနာ ခုနစ်ခုလုံးကိုလည်း ခွဲခြမ်းစိတ်ဖြာရမည်၊ အကြီးအမှူးကို ရုပ် သုံးမျိုးကို စုစည်းခြင်းဖြင့်)
NOTEP
- (vipākaṃ atītārammaṇaṃ ekaṃ khandhaṃ, tissopi pañhā paripuṇṇā. Pavattipaṭisandhi kātabbā) = (ကံ၏ အကျိုး ဖြစ်သော အတိတ်ကို အာရုံပြုသော အစုအဝေး တစ်ပါးကို၊ ပြဿနာ သုံးခုလုံးလည်း ပြည့်စုံကြသည်။ ဘဝ ဖြစ်စဉ်ကိုလည်း၊ ပဋိသန္ဓေကိုလည်း ပြုရမည်)
- (bahiddhā ninnānākaraṇaṃ, mātikāpadāni vitthāretabbāni) = (မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရား၌ ကွဲပြားချက် မရှိ၊ ခေါင်းစဉ်စာရင်း ပုဒ်တို့ကို အကျယ် ချဲ့ရမည်)
- (purimā purimā bahiddhāti nānākaraṇaṃ, taṃyeva gamanaṃ) = (ရှေးရှေး မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရားဟူ၍ ကွဲပြားချက် ရှိသည်၊ ထို သွားပုံပင် ဖြစ်သည်)
- (avipākaṃ-4) = (ကံ၏ အကျိုးဟူသော အကြောင်း မပါဝင်သော-4)
- (savipākaṃ-5) = (ကံ၏ အကျိုးဟူသော အကြောင်း ပါဝင်သော-5)
SK/SKF
- khandhā vatthussa, vatthu khandhānaṃ §C§ena paccayo = အစုအဝေးတို့သည် မှီရာ ဝတ္ထုအား၊ မှီရာ ဝတ္ထုသည် အစုအဝေးတို့အား {C1.if}
- pañcaviññāṇasahagataṃ §T§aṃ ekaṃ = သိစိတ် ငါးပါးနှင့်အတူ ဖြစ်သော {T1} တစ်ပါး
