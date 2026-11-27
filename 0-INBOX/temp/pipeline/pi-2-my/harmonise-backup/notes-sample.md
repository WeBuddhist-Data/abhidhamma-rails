# pi-2 Burmese zero-shot sample: working notes

Scope: preamble, 1-khandhavibhango. Brief: burmese-zeroshot-sample-brief.md. Pāli only; no Burmese translation or
nissaya consulted; pi-1-my read only (nothing written there, no bytecode).

## Status (2026-11-17): done, for the user's review
- [x] preamble.md (3 segments), 1-khandhavibhango.md (169 segments, 535 lines, all three parts)
- [x] my2_formulas.py, make_sample.py, check_sample.py, my2-zeroshot-terms.md (generated)
- check_chapter_ids / pi-6-mr/check_text_pe / pi-4-mr/check_marks: OK on both files (chk-pe copies deleted).
- check_sample.py: 0 mismatches (29 definition lists checked); pi-1 reuse 16 / 16 identical (preamble 2, chapter 14:
  headings and the matter sentences of ^2-33).
- Regenerate: `python3 -I -X utf8 make_sample.py` (both files + terms). Check: `check_sample.py <pāli> <my> …`.
  Nothing committed.
- scratch/: p1find.py (pi-1 Pāli regex -> aligned final Burmese line), p1sents.py (sentences shared with pi-1),
  negdbg.py (negation markers per line).

## Method (model for chapters 2-18)
- my2_formulas.py reads pi-1-my/my_formulas.py and make_ch3.py as TEXT, applies the rails patches of
  pi-1-my/rails/my_formulas_rails.py in memory (as rails/build_rails.py), execs them: P1 = final pi-1 module
  (TERMS with bahiddhā = မိမိ၏ ပြင်ပ၌, uppanna = ဖြစ်ပေါ်ပြီးသော …; CEVA; NAMES), C3 = Rūpakaṇḍa namespace (PRED,
  NOUN, ekaka list, matter frames, used as-is for every matter clause of the abhidhamma part).
- The 4-01 lists (atīta / anāgata / paccuppanna / ajjhatta items) are read from the final pi-1 Burmese lines
  ^1-1044 / 1045 / 1046 / 1050 (item counts asserted), so they are pi-1's final words, incl. the rails samuppannā.
- Engine as pi-1 / pi-2 Marathi: clause by clause (RULES), punctuation by SEP, a rule may return None, unmatched
  text raises Miss. STATE: part (sut / abh / pan), topic noun, current aggregate (kh), subject number (pl), nv.
- check_sample.py negation tables count compound-internal privatives (kusalākusalā, kusalābyākatā, hetuahetuka,
  visaṃsaṭṭha) and ignore «ကာမ», «မနော», «မည်သည့် … မဆို», «သို့မဟုတ်».

## Choices (all in my2-zeroshot-terms.md)
- Book title Vibhaṅgapāḷi = «ခွဲခြမ်းစိတ်ဖြာခြင်း» (Analysis). Note: pi-1 uses the same string for vebhabyā inside
  the paññā synonym list (different context; flag for the user).
- Parts: Suttantabhājanīyaṃ «သုတ္တန်အလိုက် ခွဲခြမ်း ဖော်ပြချက်», Abhidhammabhājanīyaṃ «အဘိဓမ္မာအလိုက် ခွဲခြမ်း
  ဖော်ပြချက်» (bhājanīya = pi-1 «ခွဲခြမ်း ဖော်ပြချက်»), Pañhāpucchakaṃ «မေးခွန်းများဖြင့် ဖော်ပြချက်» (new).
- Colophons (new): Dukamūlakaṃ «နှစ်မျိုးတွဲကို အခြေခံသော ခွဲနည်း», Tikamūlakaṃ «သုံးမျိုးတွဲကို အခြေခံသော ခွဲနည်း»,
  Ubhatovaḍḍhakaṃ «နှစ်ဘက်စလုံး တိုးပွားသော ခွဲနည်း» (nayo = pi-1 «ခွဲနည်း»; «method» is implied, not in the Pāli).
- Eleven qualifiers = pi-1 values (atīta အတိတ် … dūre အဝေး၌ ရှိသော, santike အနီး၌ ရှိသော); in the summary «X vā» =
  «…ဖြစ်စေ» (pi-1 TAIL form); «Yaṃ kiñci rūpaṃ … tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā» = «… မည်သည့် ရုပ်မဆို၊
  ထိုအားလုံးကို တစ်စုတည်း ပေါင်းစု၍ အကျဉ်းချုံ့၍».
- Definitions: «Yaṃ rūpaṃ L …,» = «L … ရုပ် ရှိသမျှ၊» (L02 Yo / Yaṃ = ရှိသမျှ); closer «idaṃ vuccati X» = «ဤသည်ကို
  Xဟု ခေါ်သည်». New items: hīna / paṇīta lists (12 each, all distinct, polarity mirrored: uññāta အထင်သေးထားသော /
  anuññāta အထင်မသေးထားသော …; manāpa / amanāpa = pi-1 «စိတ်နှင့် တွေ့သော / မတွေ့သော»); dūre / santike items
  (anāsanna မနီးကပ်သော, anupakaṭṭha အနားမကပ်သော, asantika အနီး၌ မရှိသော, āsanna နီးကပ်သော, upakaṭṭha အနားကပ်သော,
  avidūra မဝေးလှသော); «tesaṃ tesaṃ sattānaṃ» before the hīna list = agent «ထိုထို သတ္တဝါတို့က».
- Statements: «X N oḷārikā» = «X Nသည် ရုန့်ရင်းသည်»; two kinds (kusalābyākatā, sukhā ca adukkhamasukhā ca …) =
  plural «… Nများသည် … ကြသည်» (the viññāṇa passage marks the number itself); compound «kusalābyākatā» = pi-1 B9 form
  «ကုသိုလ် Nနှင့် ကုသိုလ်လည်း မဟုတ်၊ … N»; «… dūre» = «… N2မှ ဝေးသည်», «… santike» = «… N2နှင့် နီးသည်»;
  asamāpannassa / samāpannassa = «ဈာန် မဝင်စားသူ၏ / ဝင်စားသူ၏» (pi-1 ^1-1289); paṭigha- / adhivacanasamphassajā =
  «ထိခိုက်မှု၏ / အမည်ခေါ်ဝေါ်မှု၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော» (pi-1 IMPACT, adhivacana); «Taṃ taṃ vā pana … daṭṭhabbaṃ» =
  «သို့မဟုတ် ထိုထို Nနှင့် နှိုင်းယှဉ်၍ Nကို Aသည်ဟုလည်းကောင်း၊ Bသည်ဟုလည်းကောင်း မှတ်ယူရမည်».
- Abhidhamma part: «Xvidhena K –» = «Nမျိုးဖြင့် ကြည့်လျှင် K –» (vidhena = pi-1 termbase မျိုး; «ကြည့်လျှင်» is the
  minor clarification), «Evaṃ …» = «ဤသို့ … ကြည့်လျှင် K ဖြစ်သည်», Aparopi = «နောက်တစ်နည်းဖြင့်», bahuvidhena =
  «အမျိုးမျိုးဖြင့်», catuvīsati = နှစ်ဆယ့်လေး, tiṃsa(ti) = သုံးဆယ်; «atthi T» = «T KN ရှိသည်» with KN = the
  aggregate's noun (ခံစားမှု / မှတ်သိမှု / ပြုပြင်ဖန်တီးမှု / သိစိတ်), the pi-1 matter frame «T ရုပ် ရှိသည်»;
  «X atthi T» = «Xတွင် T KN ရှိသည်» (pi-1 ^1-592); «K – phassasampayutto» = «… တွေ့ထိမှုနှင့် ယှဉ်တွဲသော သဘောတရား
  ဖြစ်သည်»; Xsamphassapaccayā = «X၏ တွေ့ထိမှုကို အကြောင်းပြု၍ ဖြစ်သော» (paccaya = pi-1 အကြောင်း).
- Pañhāpucchaka: pi-1 aṭṭhakathākaṇḍa / nikkhepa frames: «S T» = «Sသည် T သဘောတရား ဖြစ်သည်» (pl «…များ ဖြစ်ကြသည်»),
  siyā = «တစ်ခါတစ်ရံ», na vattabbo = «Sသည် – “…”ဟုလည်းကောင်း … ခေါ်ဆို၍ မရ», kati = «… မည်မျှ … ရှိသနည်း»;
  combined dyads (na hetu sahetuka, Xvippayutta-Y) = pi-1 «A သဘောတရားများအနက် B».
- New mātikā-pattern terms: phassasampayutta, dukkhasahagata, sukha- / dukkh- (indriya)sampayutta, the combined
  dyads (list in the terms file, section «new in pi-2»).

## Unsure Pāli / to confirm
- niyaka (Vb ajjhatta list) ≠ Dhs niyatā («သီးသန့် ဖြစ်သော»): rendered «ကိုယ်ပိုင် ဖြစ်သော» (one's own).
- «atthi T» with the bare aggregate noun (ခံစားမှု …) rather than the full «… အစုအဝေး»: shorter, same sense.
- The bare «Sappaccayā, saṅkhatā.» (no subject; the five aggregates) = «အကြောင်း ရှိသော သဘောတရားများ ဖြစ်ကြသည်၊ …».

## Source slips (translated as written)
- ^2-41 (one place): «āsavippayuttaanāsavo» read as āsavavippayuttaanāsavo.
- ^2-153: «Rūpakkhandho na vattabbo – "saṃyojanañceva saṃyojaniyo cā"ti, "saṃyojaniyo ceva no ca saṃyojanaṃ".» (also
  gantha, nīvaraṇa, parāmāsa, upādāna, kilesa): second item in quotes without «ti»; the āsava line has it unquoted as a
  statement. Rendered as a statement: «… ခေါ်ဆို၍ မရ၊ “… သဘောတရား” ဖြစ်သည်။» (quotes kept).
- ^2-153: «siyā na vattabbā – kilesasampayuttā ceva no ca kilesā"ti» (opening quote missing): kept without «“».
- ^2-153: «"kileso ceva saṃkiliṭṭhā cā"ti», «"upādānañceva upādāniyā cā"ti» (singular first member, plural subject):
  the subject's plural used.
- ^2-153: «Rūpakkhandho … siyā upādinnā, siyā anupādinnā» (plural forms, singular subject): singular used.
- ^2-61 «Tiṃsavidhena» beside «Tiṃsatividhena»: both «သုံးဆယ်မျိုးဖြင့်».
- ^2-120 (saṅkhāra Aparopi): «atthi bahiddhārammaṇo atthi ajjhattabahiddhārammaṇo» (comma missing): no «၊» there.
- Stray spaces before «…pe…» («ghānasamphassapaccayā …pe…») dropped.
