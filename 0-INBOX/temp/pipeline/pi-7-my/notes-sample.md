# pi-7 (Paṭṭhāna) Burmese zero-shot sample: notes

Files: `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/` 1-00-paccaya.md, 1-02-vedanattika.md.
Translated from the Pāli only (no Burmese translation or nissaya opened, no web search, `language-priority/` not opened).
Generator: `make_sample.py` (this sample's unique templates SK / HLINES / PH) + `my7_formulas.py` (shared module: tables,
frames, phrase lexicon LEX, engine). Check: `check_sample.py` (+ `chk_mutate.py`: 7 / 7 planted errors caught).
Term list: `my7-zeroshot-terms.md` (written by `make_sample.py --terms`). Helpers (read-only): `kwic.py`, `kw2.py`,
`tb.py`, `tbc.py`, `reuse_index.py`, `lax.py`; `check_text_pe7.py` = the pi-6-mr wrapper with its scratch copy in
`pi-7-my/chk-pe/` (deleted after each run; nothing written in pi-6-mr/).

## Status (all pass)
| file | segments | lines | check_chapter_ids | check_text_pe | check_marks | check_sample |
|---|---|---|---|---|---|---|
| 1-00-paccaya.md | 74 | 149 | OK | OK | OK | OK |
| 1-02-vedanattika.md | 271 | 385 | OK | OK | OK | OK |

check_sample: 534 lines × (structure, polarity, conditions, term order, numbers), 881 sentences for identity,
40 table values: **0 mismatches**. Reuse test: **110 / 110** reused pi-1 … pi-6 values identical wherever their Pāli
occurs in the sample (156 values witnessed in all; each is re-read from the FINAL rails segment); sample sentences that
also occur in pi-1 … pi-6: **58 / 58** identical (the «(1)» «(2)» «(3)» lines).
Coverage on 1-01-kusalattika (`--dev`, not written): 823 distinct sentence skeletons still unmatched (the kusala
triad's own lexicon: rūpa, vatthu phrases, the remaining pañhā paragraphs …).

## Core choices (log)
- **Book title** Paṭṭhānapāḷi = «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ» ("how causes and results connect"; Burmese only).
  Tikapaṭṭhānaṃ = «သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ». (No preamble.md was asked for; its title line
  would be «## အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ».)
- **paccaya** = «အကြောင်း» (pi-5 termbase and rails). «Xpaccayena paccayo» = «Nဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်»
  exactly as the pi-5 rails (^5-711 … ^5-717, e.g. «ရှေးရှေး ကုသိုလ် သဘောတရားတို့သည် နောက်နောက် ကုသိုလ်
  သဘောတရားတို့အား ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း …»). Invariant verb (Pāli paccayo is
  invariant). «na Xpaccayena paccayo» = «… အကြောင်း ဖြစ်သည် မဟုတ်».
- **The 24 names N** (every case form is built from N by `cond()`):
  - from the pi-5 rails: hetu အမြစ်, ārammaṇa အာရုံ, adhipati အကြီးအမှူး, anantara ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း,
    samanantara ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း, sahajāta အတူ ပေါ်ပေါက်ခြင်း, āsevana အလေ့အကျင့် ပြုခြင်း,
    āhāra အာဟာရ, indriya စွမ်းရည်, magga မဂ်;
  - from pi-1 … pi-6 words: kamma ကံ, vipāka ကံ၏ အကျိုး (pi-1 Vipākattika), jhāna ဈာန်;
  - NEW: aññamañña အချင်းချင်း ထောက်ပံ့ခြင်း (pi-5 «အချင်းချင်း»; its «aññamaññapaccaya = အချင်းချင်း အကြောင်း
    ဖြစ်ခြင်း» would give «… အကြောင်း ဖြစ်ခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း»), nissaya အမှီ, upanissaya အားကြီးသော
    အမှီ, purejāta ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း (pi-2 purejāta «ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော»), pacchājāta နောက်မှ ဖြစ်ပေါ်ခြင်း,
    sampayutta ယှဉ်တွဲခြင်း, vippayutta ကင်းကွာခြင်း (pi-1 «…နှင့် ယှဉ်တွဲသော / ကင်းကွာသော»), atthi ရှိခြင်း,
    natthi မရှိခြင်း, vigata ပျောက်ကွယ်ခြင်း, avigata မပျောက်ကွယ်ခြင်း.
  - Forms: name «Nဟူသော အကြောင်း» (neg «… မဟုတ်ခြင်း»); Xpaccayā «Nဟူသော အကြောင်းကြောင့်» (pi-1 … pi-5
    dependent origination «Xကြောင့်»), naXpaccayā «… ကြောင့် မဟုတ်ဘဲ»; counting «Xe / Xyā K» = «Nဟူသော အကြောင်း၌ K»,
    «naXe K» = «Nဟူသော အကြောင်း မဟုတ်ခြင်း၌ K»; ghaṭanā lists use the bare N.
- **paṭicca** = «…ကို မှီ၍» (pi-2 ^2-184 / pi-5 rails «Cakkhuñca paṭicca rūpe ca uppajjati …» = «…ကိုလည်းကောင်း မှီ၍ …
  ဖြစ်ပေါ်သည်»); **uppajjati** «ဖြစ်ပေါ်သည်», uppajjanti «ဖြစ်ပေါ်ကြသည်».
  **Siyā … uppajjeyya** = «… ဖြစ်ပေါ်နိုင်သလော» (uppajjeyyuṃ «ဖြစ်ပေါ်နိုင်ကြသလော»): siyā has no word of its own; the
  question particle closes the question.
- **Word order**: «X ကို မှီ၍ Y သည် [conditions] ဖြစ်ပေါ်သည်». When the Pāli gives one verb and then a chain
  «uppajjati A… B… C», the Burmese verb follows the last condition («A-ကြောင့်… B-ကြောင့်… C-ကြောင့် ဖြစ်ပေါ်သည်»), so the
  question particle also ends the line; a closing note stays after the verb. The «ekaṃ khandhaṃ paṭicca dve khandhā …»
  explanations keep the Pāli's verbless form: «အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး နှစ်ပါး၊ …».
- **Sections and orders**: vāra «Xအလိုက် ဖော်ပြချက်» (pi-2 / pi-6): paṭicca- «မှီ၍ ဖြစ်ပေါ်ခြင်း», sahajāta- «အတူ
  ပေါ်ပေါက်ခြင်း», paccaya- «အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း», nissaya- «အမှီပြု၍ ဖြစ်ပေါ်ခြင်း», saṃsaṭṭha- «ရောနှောခြင်း»,
  sampayutta- «ယှဉ်တွဲခြင်း», pañhā- «ပြဿနာ», pucchā- «အမေး», vibhaṅga- «ခွဲခြမ်းစိတ်ဖြာခြင်း», saṅkhyā-
  «ရေတွက်ခြင်း». **anuloma / paccanīya** = pi-6 «အဟုတ်ပြ / အငြင်းပြ ပုံစံ»: the same sense (statements made with the
  conditions / dhammas affirmed, and the same statements with them negated, «naXpaccayā»), so pi-6 is reused;
  anulomapaccanīya «အဟုတ်ပြ အငြင်းပြ ပုံစံ», paccanīyānuloma «အငြင်းပြ အဟုတ်ပြ ပုံစံ»; Paccayānulomaṃ «အကြောင်း
  အဟုတ်ပြ ပုံစံ»; Dhammānulome «သဘောတရား အဟုတ်ပြ ပုံစံ၌». The mind moment anulomaṃ (conformity, before gotrabhu) is
  a homograph: «လျော်ညီခြင်း စိတ်».
- **Counting**: count words take «ခု» (answers): tīṇi «သုံးခု» … (NEW); khandha numbers «ပါး» (pi-2 / pi-3 / pi-5);
  counting groups dukaṃ … catuvīsakaṃ «နှစ်မျိုးတွဲ … နှစ်ဆယ့်လေးမျိုးတွဲ» (pi-1 tika / duka «သုံးမျိုးတွဲ / နှစ်မျိုးတွဲ»;
  the same Pāli word, so the same Burmese). Ablative given conditions take «၊» before the first count. X-sabhāgaṃ
  «Nဟူသော အကြောင်းနှင့် တွဲဖက်သည်များ», X-mūlakaṃ «… ကို အခြေခံခြင်း», ghaṭanā «ပေါင်းစပ်ချက်» (sāmañña «သာမန်»,
  pakiṇṇaka «အထွေထွေ»); ghaṭanā lines «A၊ B၊ … ဟူသော ပေါင်းစပ်ချက်၌ K» (no quote marks: the Pāli has none).
- **Doctrinal terms** (pi-1 … pi-6 unless NEW): khandha အစုအဝေး; mahābhūta မူလဓာတ်ကြီး; upādārūpa «မူလဓာတ်ကြီးတို့ကို
  မှီ၍ ဖြစ်သော ရုပ်» (pi-5 ^5-756 «mahābhūtā upādāyarūpānaṃ»); cittasamuṭṭhāna «စိတ်မှ ဖြစ်ပေါ်လာသော»; taṃsamuṭṭhāna
  «ထိုအရာမှ ဖြစ်ပေါ်လာသော», taṃsampayuttaka «ထိုအရာနှင့် ယှဉ်တွဲသော» (NEW); kaṭattārūpa «ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော
  ရုပ်» (NEW); paṭisandhi(kkhaṇe) «ပဋိသန္ဓေ (နေသော ခဏ၌)» (NEW); okkantikkhaṇe «သန္ဓေ သက်ဆင်းသော ခဏ၌» (NEW; pi-2
  okkanti «သက်ဆင်းခြင်း»); vatthu «မှီရာ ဝတ္ထု» (pi-5); nāmarūpa «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း»; cittacetasikā
  «စိတ်နှင့် စိတ်၏ အဖော်»; arūpino «ရုပ် မဟုတ်သော»; arūpe «ရုပ်မရှိသော ဘုံ၌»; ahetuka «အမြစ် မရှိသော»; cetanā
  «စေ့ဆော်မှု»; the āyatana, dhātu and indriya names, kabaḷīkāro āhāro, rūpajīvitindriya, the four arūpa āyatanas,
  the deeds list (pi-5 ^5-314 optative forms, here present «… သည်»), dānaṃ datvā … (pi-2 ^2-1021).
- Path moments (NEW): gotrabhu «အနွယ် ပြောင်းခြင်း စိတ်», vodāna «စင်ကြယ်ခြင်း စိတ်» (pi-2 ^2-760 vodānaṃ «စင်ကြယ်ခြင်း»),
  bhavaṅga «ဘဝင် စိတ်», āvajjanā «စိတ်ညွတ်ခြင်း», cuticitta «စုတေခြင်း စိတ်» (pi-2 cuti), upapatticitta «ပြန်လည်
  ဖြစ်ပေါ်ခြင်း စိတ်», vuṭṭhāna «ထမြောက်ခြင်း စိတ်», phalasamāpatti «ဖိုလ်သမာပတ်», nirodhā vuṭṭhahantassa «ချုပ်ငြိမ်းခြင်း
  သမာပတ်မှ ထမြောက်နေသူ၏»; kamma kinds sahajātā «အတူ ပေါ်ပေါက်သည့် ကံ», nānākkhaṇikā «ခဏ ကွဲပြားသည့် ကံ»;
  upanissaya kinds ārammaṇūpanissaya «အာရုံဖြင့် အားကြီးသော အမှီ», anantarūpanissaya «ချက်ချင်း နောက်၌
  ဖြစ်စေခြင်းဖြင့် အားကြီးသော အမှီ», pakatūpanissaya «ပကတိ အားကြီးသော အမှီ»; ārammaṇādhipati «အာရုံ အကြီးအမှူး»,
  sahajātādhipati «အတူ ပေါ်ပေါက်သော အကြီးအမှူး» (pi-5 «ဆန္ဒ အကြီးအမှူး» pattern).
- vācanāmaggena «ရွတ်ဆိုသည့် နည်းလမ်းအတိုင်း», sajjhāyamaggena «သရဇ္ဈာယ်သည့် နည်းလမ်းအတိုင်း» (two Pāli words,
  two Burmese); yathā … vitthārito, evaṃ … vitthāretabbo «… အကျယ် ချဲ့ထားသည့်အတိုင်း … ထိုနည်းတူ … အကျယ်
  ချဲ့ရမည်» (pi-2 ^2-66 «… အကျယ် ဖော်ပြထားသည့်အတိုင်း … ထိုနည်းတူ», pi-5 ^5-839 vitthāretabbaṃ «အကျယ် ချဲ့ရမည်»);
  asammuyhantena «မရောထွေးစေဘဲ»; gaṇanā «ရေတွက်ချက်».
- **Variants**: the pi-7 Pāli writes them in braces. The Burmese uses the pi-1 label in the same braces,
  «{ပါဌ်ကွဲ (Syā.): paccayoti}», «{စာလုံးပေါင်းကွဲ (Ka., Sī., Syā.): kabaḷiṅkāro}», because pi-4-mr/check_marks.py
  compares the number of «[» per line with the Pāli (square brackets would fail it on every variant line). One switch
  (`VAR_OPEN` / `VAR_CLOSE` in my7_formulas.py) gives «[…]» if the coordinator prefers it (check_marks would then need a
  folded copy, like check_text_pe). Spelling-only: kabaḷiṅkāro, nānākhaṇikā.

## For the coordinator: points that need a decision
1. **paṭicca and nissāya are both «… ကို မှီ၍»**: both are locked so in pi-1 … pi-6 (paṭicca pi-2 ^2-184 / pi-5; nissāya
   pi-1 ^1-599 «yaṃ cakkhuṃ nissāya» «ထို မျက်စိကို မှီ၍», pi-2, pi-4, pi-5). The Paṭṭhāna keeps paṭiccavāra and nissayavāra
   apart; here only the headings differ («မှီ၍ ဖြစ်ပေါ်ခြင်း» / «အမှီပြု၍ ဖြစ်ပေါ်ခြင်း»). Option: nissāya «ကို အမှီပြု၍»
   in pi-7 (then 1-00 ^7-1-8 / ^7-1-10 / ^7-1-21 «Yaṃ rūpaṃ nissāya» would differ from pi-1).
2. samanantarā (adverb, ^7-1-5) «ကောင်းစွာ ချက်ချင်း နောက်၌» to match the condition name; pi-5 ^5-576 has
   samanantarā «ချက်ချင်း နောက်၌», which here is anantarā (^7-1-4).
3. upādārūpa: pi-5 rails «မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်» followed; pi-1 termbase upādā «မူလဓာတ်ကြီးများကို မှီ၍
   ဖြစ်သော», pi-2 rails «မူလဓာတ်ကြီး လေးပါးကို မှီ၍ ဖြစ်သော ရုပ်» (with catunnaṃ).
4. vipāka: pi-1 «ကံ၏ အကျိုး ဖြစ်သော» followed; pi-5 15-sattamavaggo has «vipākā cattāro khandhā arūpino» = «အကျိုး
   ဖြစ်သော ရုပ် မဟုတ်သော အစုအဝေး လေးပါး» (without ကံ၏).
5. āsevana: the pi-5 rails frame «အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းဖြင့် …» followed; the pi-5 termbase has
   āsevanapaccayatā «အဖန်ဖန် မှီဝဲခြင်း …» (rails wins).
6. abyākata: the termbases write it without «၊»; the rails texts have «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော»
   (followed).
7. Variant braces (above).

## Unsure Pāli
- «paripuṇṇaṃ paṭisandhikaṃ» (^7-3-9, ^7-3-11): "complete, with rebirth-linking" «ပဋိသန္ဓေနှင့်တကွ ပြည့်စုံသည်».
- «saddhāpañcamakesu … kātabbaṃ, avasesesu na kātabbaṃ» (^7-3-53): "in the five headed by faith add …, not in the
  others": «ယုံကြည်မှု စသော ငါးပါးတို့၌ … ထည့်ရမည်၊ ကြွင်းသည်တို့၌ မထည့်ရ».
- «pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti» «ရှာမှီးခြင်းကို အရင်းခံသော ဆင်းရဲကို ခံစားသည်»; «attānaṃ ātāpeti
  paritāpeti» «မိမိကိုယ်ကို ပူပန်စေ၍ ပြင်းစွာ ပူပန်စေသည်».
- «catuviññāṇasahagataṃ» (^7-3-13) «သိစိတ် လေးပါးနှင့်အတူ ဖြစ်သော» (the four sense consciousnesses other than body).
- «samudāciṇṇe kilese» «ရှေးက ဖြစ်ခဲ့ဖူးသော ကိလေသာ»; «vikkhambhite» «ခွာထားပြီးသော».
- «(mūlakaṃ saṃkhittaṃ)» (^7-U261) «(အခြေခံ အကြောင်းများကို အကျဉ်းချုပ်)».
- «Niddesavāre tevīsatipaccayā» (^7-1-52) «အကြောင်းများ၏ အကျယ် ဖော်ပြချက်၌ အကြောင်း နှစ်ဆယ့်သုံးပါး» (read as the
  niddesa of the pucchāvāra).
- «kesañci» after a recipient (^7-1-9) «… သဘောတရားတို့အနက် အချို့အား».
- The verse (^7-1-41 …): «tikañca paṭṭhānavaraṃ dukuttamaṃ» «သုံးမျိုးတွဲတို့၏ မြတ်သော အကြောင်းနှင့် အကျိုး
  ဆက်စပ်ပုံ၊ နှစ်မျိုးတွဲတို့၏ အမြတ်ဆုံး ဆက်စပ်ပုံ၊»; the final «-ti» is not rendered (also in the uddesa list ^7-U1).

## Source slips (translated as written)
- 1-00 ^7-1-5 «Ghāṇaviññāṇadhātu» (ṇ for n): rendered as ghānaviññāṇadhātu.
- 1-00 ^7-1-41, ^7-1-44 «vitthāretabbaṃ. )» stray space before «)» (kept: «… ချဲ့ရမည်။ )»).
- 1-02 ^7-3-13 «Sukhāya … paṭicca dukkhāya vedanāya sampayutto dhammo uppajjati navipākapaccayā…» with the explanation
  «sukhasahagataṃ kāyaviññāṇasahagataṃ»: the second term should probably be sukhāya; kept.
- 1-02 ^7-3-40, ^7-3-41 «cittaṃ jānanti» (plural) where ^7-3-39 has «jānāti»: kept («သိကြသည်»).
- 1-02 ^7-3-40 «… āvajjanāya ārammaṇapaccayena paccayo – dukkhāya …»: a dash where the other blocks have a full stop;
  kept (dash rule).
- 1-02 ^7-3-65 no full stop between the two ghaṭanā items («… avigatanti dve hetu-adhipati-…»): kept.
- 1-02 ghaṭanā hyphen slips (segmented by stem, logged by the generator): missing hyphens «sahajātaaññamañña» (8),
  «Kammasahajāta», «Indriyasahajāta», «Jhānasahajāta», «Maggasahajāta», «Āhārasahajāta» (9 before sahajāta),
  «Indriyahetu», «Maggahetu», «samanantaraupanissaya», «anantarasamanantara», «indriyasampayutta», «sampayuttaatthi» (2);
  spaces at a hyphen «nissaya -vipāka», «magga -sampayutta», «aññamañña -nissaya» (4); «Adhipati-sahajātaṃ-» (ṃ).
- 1-02 ^7-U251 «Āhāra-sahajāta-aññamañña-nissaya-kamma-sampayutta-avigatanti tīṇi» lacks «atthi» (its pair has it).
- 1-02 ^7-U265 the negated compound «naārammaṇa-…-nasamanantaranasahajāta-…-navipākanaāhāra-…» lacks two hyphens.

## For the next agents
- Copy make_sample.py (change NAMES and the tables), import my7_formulas, run with `--dev` until 0 unmatched, then
  without; add your triads to `F.TRIADS` / `F.TRIAD_END` and call `F.rebuild()`; add nouns with `add_noun()`,
  qualifiers `add_qual()`, fixed phrases `add_fixed()`, lexicon phrases `add_lex()`, notes to `F.NOTES`; reuse a
  pi-1 … pi-6 value only through `F.W(pali, burmese, book, bid)` so the reuse test sees it.
- check_sample.py: add new Pāli negation tokens to NEG_NOT / NEG_MA, new condition-bearing notes to NOTE_CONDS, and the
  new triad terms to TERMS_MY / T_PI. Run chk_mutate.py after changing the checker.
- Never run pi-6-mr/check_text_pe.py (it writes into pi-6-mr/chk-pe/); use pi-7-my/check_text_pe7.py.
