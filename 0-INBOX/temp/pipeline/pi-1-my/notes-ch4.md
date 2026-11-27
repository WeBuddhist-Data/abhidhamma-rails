# pi-1 Burmese zero-shot, chapters 4-01, 4-02, 4-03 (Nikkhepakaṇḍa, brief exposition of the Mātikā): notes

Status 2026-11-16: done, all checks pass. Not committed. Translated from the Pāli only
(AI_translation/pali/pi-1_split_chapters/4-0[1-3]-nikkhepakandam.md). The English zero-shot and the Marathi track were
read for meaning only (Tathāgata after death, upādiṇṇa in the ajjhatta list). No Burmese translation, nissaya or web
source was used.

## Files
- AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/4-01-nikkhepakandam.md (179 segments, 187 lines),
  4-02-nikkhepakandam.md (155 segments, 161 lines), 4-03-nikkhepakandam.md (82 segments, 83 lines).
- make_ch4.py: generator (`python3 -I -X utf8 make_ch4.py [4-01|4-02|4-03]`). Imports my_formulas, adds its tables
  and frames IN MEMORY only (add() refuses to change an existing value), then my_formulas.translate_cu() renders every
  line. Writes only the three chapter files; my_formulas.py and my-zeroshot-terms.md are not touched.
- check_ch4.py: own per-line check (see its docstring). Mutation-tested on 4-01: a dropped negation, two swapped
  synonyms, a dropped synonym, a wrong number and a wrong Mātikā closer are all reported.

## Checks (all pass)
- check_chapter_ids.py: OK for 4-01 (179), 4-02 (155), 4-03 (82 segments).
- pi-6-mr/check_text_pe.py: OK (187 / 161 / 83 lines, dashes match); the chk-pe copies were deleted.
- pi-4-mr/check_marks.py: OK for all three.
- check_ch4.py: OK, 0 mismatches for all three (negations, numbers, variants, frame counts, Mātikā strings, list items
  in order and distinct, phrase order, typography). No «?» in the Burmese.

## How the engine is used (frames added in F.CU_EXTRA_RULES, tried before the 2-01 built-ins)
- `Katame dhammā X?` = «{Mātikā X} သဘောတရားများ ဟူသည် အဘယ်တို့နည်း။» (for kusalā this is the model's KATAME_KUSALA).
- `ime dhammā X` = «ဤသဘောတရားများသည် {predicate of X}» (kusalā = the model's IME_KUSALA). Predicate = the Mātikā
  string with final «သော» -> «ကြသည်»; negated verb -> «ကြ» (no «သည်»: «… မဟုတ်ကြ», «… မရှိကြ»); «… ပြီးသော» ->
  «… ကြပြီ»; «မ… သေးသော» -> «မ… ကြသေး»; «… မည့်» -> «… ကြမည်»; noun -> «… ဖြစ်ကြသည်»; genitive («ကျင့်ကြံဆဲသူ၏»)
  -> «… သဘောတရားများ ဖြစ်ကြသည်».
- `Tattha katamo / katamā / katamaṃ X?` = «ထိုတို့အနက် X ဟူသည် အဘယ်နည်း။» (katame: «… အဘယ်တို့နည်း»);
  `ayaṃ / idaṃ vuccati X` = «ဤသည်ကို Xဟု ခေါ်သည်».
- Synonym lists after `Yo / Yā / Yaṃ [head]` up to « – » use the 2-01 list_items / items_my (distinctness enforced);
  a Pāli comma inside a list is the same «၊» as the joiner. `Ye dhammā [head] A B C, …` = «A၊ B၊ C သဘောတရားများ၊ …».
- Singular ceva lines `Lobho mohena hetu ceva sahetuko ca` = «လောဘသည် မောဟဖြင့် {CEVA, singular predicate}»;
  `te aññamaññaṃ …` = «ထိုတို့သည် အချင်းချင်း …»; `Teyeva āsavā …` = «ထို N-တို့သည်ပင် …» (Sveva: «ထို Nသည်ပင်»).
- `Tehi dhammehi ye dhammā sampayuttā / vippayuttā` = «ထိုသဘောတရားတို့နှင့် ယှဉ်တွဲသော / ကင်းကွာသော သဘောတရားများ»;
  with any other Mātikā Y: «ထိုသဘောတရားတို့နှင့် စပ်လျဉ်း၍ {Y} သဘောတရားများ».
- `X dhamme ārabbha ye uppajjanti cittacetasikā dhammā` = «{Mātikā X} သဘောတရားတို့ကို အာရုံပြု၍ ဖြစ်ပေါ်ကြသော
  စိတ်နှင့် စိတ်၏ အဖော် သဘောတရားများ».
- Kenaci list: `Ye te dhammā A, na te dhammā B; ye vā pana …` = «အကြင် သဘောတရားများသည် A-ကြသည်၊ ထိုသဘောတရားများသည်
  B-သည် မဟုတ်ကြ၊ တစ်ဖန် …» (A, B = «မျက်စိဖြင့် သိနိုင်» …).
- Counted roots: `tayo kusalahetū` = «ကုသိုလ် အမြစ် သုံးပါး»; `ime tayo … hetū` = «ဤသည်တို့မှာ … ဖြစ်ကြသည်».
- `Sabbāpi micchādiṭṭhi X` = «မှားယွင်းသော အယူ အားလုံးသည် X ဖြစ်သည်» (with `Ṭhapetvā Y`: «Y-ကို ချန်ထား၍ …»);
  `Sabbepi akusalā dhammā X` = «အကုသိုလ် သဘောတရား အားလုံးသည် {predicate X}»; `Sabbopi sīlasaṃvaro X` …
- A space-separated series of nouns (alobho adoso amoho; rūpāyatanaṃ saddāyatanaṃ …; cakkhudhātu rūpadhātu …) is
  joined with «၊» (the 2-01 r_nameseq idea, extended to multi-word nouns). This also fills the missing commas of
  ^1-1019 («kāmāvacarā rūpāvacarā») and 4-02 («kāmāvacare rūpāvacare …»); ^1-1059 keeps its missing comma.
- Separator added: the Devanāgarī visarga «ः» (a source slip for «;») = «၊».

## Mātikā strings adapted grammatically (logged as the brief asks; the approved string itself is unchanged)
- Closers use the predicate form above (all Mātikā items; for example ပယ်ရမည့် -> ပယ်ရကြမည်, ဖြစ်ပေါ်ပြီးသော ->
  ဖြစ်ပေါ်ကြပြီ, မဖြစ်ပေါ်သေးသော -> မဖြစ်ပေါ်ကြသေး, ဖြစ်ပေါ်လာမည့် -> ဖြစ်ပေါ်လာကြမည်).
- Two Mātikā items in one phrase are joined: first «… သော» -> «… ၍» (negated: «… ဘဲ»). Used for «āsavavippayuttā
  sāsavā» = «စိတ်အစွန်းအထင်းနှင့် ကင်းကွာ၍ စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော» (all nine clusters, with and
  without a-), «na hetū sahetukā» = «အမြစ် မဟုတ်ဘဲ အမြစ် ရှိသော», «na hetū ahetukā», and the closer «kenaci viññeyyā
  kenaci na viññeyyā» = «တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်၍ တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်ကြ». The question
  «kenaci viññeyyā, kenaci na viññeyyā» keeps both strings with «၊».
- Locatives kāmāvacare / rūpāvacare / arūpāvacare / apariyāpanne = «… ဆိုင်သည်၌», «… အကျုံးမဝင်သည်၌».
- atītā / anāgatā / paccuppannā inside an adjective list = «အတိတ် ဖြစ်သော», «အနာဂတ် ဖြစ်သော», «ပစ္စုပ္ပန် ဖြစ်သော»;
  «-aṃsena saṅgahitā» = «{Mātikā string} အပိုင်း၌ အကျုံးဝင်သော».
- paññatti / nirutti as list nouns (the synonym list of 1-1313) = «သတ်မှတ်ချက်», «စကားဖြင့် ဖော်ပြမှု» (the Mātikā
  string without «ဖြစ်သော»).
- upādā with its number (catunnañca mahābhūtānaṃ upādāya rūpaṃ) = «မူလဓာတ်ကြီး လေးပါးကို မှီ၍ ဖြစ်သော ရုပ်».
- The Mātikā quotations of 4-03 («Diṭṭhivisuddhi kho panāti –», «Yathādiṭṭhissa ca padhānanti –» … «Anuppāde
  ñāṇanti –») = the MFIXED / SUT string without its «။» + « ဟူသည်».
- hirī / ottappa definitions = the 2-01 BODY sentences without «ထိုအချိန်၌» (asserted in the script); their negatives
  add «မ».
- «neva ācayagāmi na apacayagāmino» (Nikkhepa spelling) = the Mātikā «nevācayagāmināpacayagāmino».

## Main choices (one-line reasons)
- nikkhepa = «အကျဉ်း ဖော်ပြချက်» (brief exposition; kaṇḍa = အခန်း, as 2-01); Tikanikkhepa = «သုံးမျိုးတွဲ အကျဉ်း
  ဖော်ပြချက်»; colophon «Tikaṃ.» = «သုံးမျိုးတွဲ။», «Abhidhammadukaṃ.» = «အဘိဓမ္မာ နှစ်မျိုးတွဲ။».
- Tattha = «ထိုတို့အနက်» («among those»); vuccati = «… ဟု ခေါ်သည်».
- taṃsampayutta = «ထိုတို့နှင့် ယှဉ်တွဲသော»; taṃsamuṭṭhāna = «ထိုတို့မှ ဖြစ်ပေါ်လာသော»; tadekaṭṭha = «ထိုတို့နှင့်
  တစ်နေရာတည်း တည်ရှိသော» («standing in one place with them»).
- kāya- / vacī- / manokamma = «ကိုယ်ဖြင့် / နှုတ်ဖြင့် / မနောဖြင့် ပြုသော ကံ»; duccarita / sucarita = «ဒုစရိုက် /
  သုစရိုက်» (everyday words; the Mātikā hirī already uses «ဒုစရိုက်»).
- kiriyā = «ပြုမှုမျှသာ ဖြစ်သော» («merely functional»); vipāka in «kusalākusalānaṃ dhammānaṃ vipākā» = «… သဘောတရားတို့၏
  အကျိုး ဖြစ်သော».
- -bhūmiyaṃ (planes of consciousness) = «X ရှိရာ အဆင့်၌»; «Na pītibhūmiyaṃ» = «ပီတိ ရှိရာ အဆင့် မဟုတ်သည့် နေရာ၌».
- maggaphala = «မဂ်၏ ဖိုလ်»; sāmaññaphala = «ရဟန်းအဖြစ်၏ အကျိုး»; arahattaphala = «ရဟန္တာ ဖိုလ်».
- sakkāyadiṭṭhi = «ကိုယ်ကို အတ္တဟု ယူဆသော အယူ»; sīlabbataparāmāsa = «သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု»
  (parāmāsa = the cluster noun); diṭṭhiparāmāsa = «အယူဆိုင်ရာ မှားယွင်းသော ယူဆမှု».
- vicikicchā = «ယုံမှားမှု», kaṅkhā = «သံသယ» (kept apart, style rule); saṃsaya = «ဒွိဟ ဖြစ်ခြင်း», vimati =
  «စိတ်ရှုပ်ထွေးခြင်း».
- taṇhā = «… ကို တပ်မက်မှု» (as the approved bhavataṇhā); rāga = «ရာဂ»; sārāga = «တပ်မက်ခြင်း» (as 2-01 asārāgo);
  both rūpataṇhā of the lobha list = «ရုပ်ကို တပ်မက်မှု» (identical Pāli, one rendering covering both senses).
- āghāta = «ရန်ငြိုးဖွဲ့ခြင်း»; anattha = «မကောင်းမှု»; paṭigha (aversion) = «စိတ်ထိခိုက်ခြင်း» (echoes the Mātikā
  paṭigha = ထိခိုက်မှု); dussanā / dussitattaṃ / byāpajjanā = the 2-01 negatives without «မ».
- uddhacca = «ယောက်ယက်ခတ်မှု», kukkucca = «နောင်တ ပူပန်မှု», thina = «ထိုင်းမှိုင်းမှု», middha = «ငိုက်မျဉ်းမှု»;
  kāyassa in the middha list = the 2-01 KAYA «စိတ်၏ အဖော်တို့၏» (the mental body).
- māna = «မာန»; issā = «ငြူစူမှု», usūyā = «သဝန်တိုမှု»; macchariya = «ဝန်တိုမှု»; veviccha = «တစ်ကိုယ်ကောင်းဆန်ခြင်း»
  (fits both the greed and the avarice list).
- The views: «Sassato loko» = «လောကသည် ထာဝရ တည်မြဲသည်» (as the approved sassatadiṭṭhi wording); jīva = «အသက်»,
  sarīra = «ကိုယ်ခန္ဓာ»; tathāgata = «မြတ်စွာဘုရား»; «-ti vā» = «… ဟူ၍ဖြစ်စေ».
- natthi dinnaṃ … = «ပေးလှူခြင်း မရှိ …»; opapātika = «အလိုအလျောက် ပေါ်လာသော».
- cakkhundriya / manindriya = «မျက်စိ၏ စွမ်းရည်» / «မနော၏ စွမ်းရည်» (2-01 pattern); indriyāni in the restraint lists =
  «အာရုံခံ အင်္ဂါ» (as the approved indriyesu guttadvāratā); nimitta = «အမှတ်အသား» (as samathanimitta).
- āpatti = «အပြစ်»; samāpatti = «ဈာန် ဝင်စားမှု» (as the approved samāpattikusalatā); bojjhaṅga = «သိမြင်ခြင်း၏
  အင်္ဂါ».
- Numbers with «ပါး» throughout; 9 = ကိုး, 10 = ဆယ်, 12 = ဆယ့်နှစ်, 18 = ဆယ့်ရှစ်.
- Words chosen to avoid a false «မ» negation: «ဆုံးမ» (avoided: «သွန်သင်»), «သမဏ» (avoided: «ရဟန်း»), «မနုဿ»;
  «တမလွန်» (para loka) is not a negation (in the checker's NOT_NEG).
- Variant labels: different word = ပါဌ်ကွဲ (diṭṭhivisūkāyitaṃ, uparimaṃ, rūpā, nīvaraṇāni, samaggatā,
  diṭṭhadhammasukhavihārassa, upādāya, cittassa ca); spelling = စာလုံးပေါင်းကွဲ (the rest). New siglum «bahūsu» =
  «Bahūsu». The double bracket «[puñcikatā (syā.) pucchikatā (sī.)]» = «[စာလုံးပေါင်းကွဲ (Syā.): puñcikatā၊ (Sī.):
  pucchikatā]».

## Unsure Pāli / for the reviewer
- ajjhatta list (1-1050/1051): niyatā = «သီးသန့် ဖြစ်သော» (restricted to each being), a different sense from the Mātikā
  niyatā «ကျိန်းသေသော»; upādiṇṇā kept as the Mātikā «ကံကြောင့် ဖြစ်သော» (the English reads it the same way).
- tathāgata in the ten views = «မြတ်စွာဘုရား» (the text's word; the commentarial «a being» is not added).
- patiṭṭhāho (1-1124 onward) is read as a slip for paṭiggāho and rendered the same «ခိုင်မြဲစွာ စွဲကိုင်ခြင်း».
- 4-03 spells asammusanatā (2-01: asammussanatā): rendered as the model «မမေ့လျော့ခြင်း».
- kāyagantha = «ကိုယ် အထုံး» (literal «body-knot»; kāya = mental and physical body).
- The immaterial realm and deva names (ပရနိမ္မိတဝသဝတ္တီ, အကနိဋ္ဌ, အာကာသာနဉ္စာယတန, နေဝသညာနာသညာယတန, အဝီစိ) are kept as
  proper names.
- «aṭṭhāne vā pana āghāto jāyati» = «အကြောင်း မရှိဘဲလည်း ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်».
- The samaṇabrāhmaṇa clause of the wrong view (natthi loke samaṇabrāhmaṇā … ye … pavedentīti) is rendered as one
  Burmese clause whose verb «မရှိ / ရှိသည်» comes at the end (a frame in make_ch4.py, r_samana).

## Source slips (translated as written unless stated)
- «ः» (Devanāgarī visarga) for «;» in ^1-1106, 1-1123, 1-1128, 1-1143, 1-1144, 1-1168, 1-1181, 1-1240, 1-1241,
  1-1369, 1-1371: rendered «၊».
- ^1-1310 «ime dhammā sukkā?»: a statement with «?»; rendered as a statement ending in «။».
- ^1-1059 «nava kāmāvacarahetū cha rūpāvacarahetū» and ^1-1101 «kāyaviññeyyā na te dhammā»: comma missing; the
  Burmese has none there either. ^1-1019, 4-02 «kāmāvacare rūpāvacare …»: commas missing; the noun series gets «၊».
- ^1-1142 «acarī ti» (spaced) = the same Burmese as «acarīti».
- ^1-1257 «kileso ceva kilesasampayuttā ca / … sampayuttañca»: gender forms vary; all = «ကိလေသာလည်း ဖြစ်၊
  ကိလေသာနှင့်လည်း ယှဉ်တွဲသည်».

## Known differences with the parallel chapters (for the consistency pass; not aligned here)
Same Pāli, different Burmese in the notes of 2-02/03, 2-04/05, 3 and 5 (theirs -> mine): vicikicchā «ယုံမှားသံသယ» ->
«ယုံမှားမှု»; kaṅkhā «ယုံမှားခြင်း» -> «သံသယ»; saṃsayo «သံသယ» -> «ဒွိဟ ဖြစ်ခြင်း»; vimati «တွေဝေခြင်း» ->
«စိတ်ရှုပ်ထွေးခြင်း»; most items of the view list (diṭṭhigataṃ «အယူမှား», abhiniveso «စွဲမြဲခြင်း», kummaggo
«လမ်းဆိုး» …) and of the moha list (pamoho «အလွန် ဝေဝါးခြင်း» …); byāpatti «ပျက်စီးစေလိုခြင်း» -> «ဖောက်ပြန်ခြင်း»;
asuropo «ရိုင်းစိုင်းခြင်း» -> «စကား ကြမ်းခြင်း»; kāyaviññatti «ကိုယ်ဖြင့် ထုတ်ဖော်ပြသမှု» (3) / «… ရည်ရွယ်ချက်ကို
ပြခြင်း» (5) -> «ကိုယ်ဖြင့် အရိပ်အမြွက် ပြခြင်း»; ākāsadhātu «ဟင်းလင်းပြင် ဓာတ်» -> «ကောင်းကင် ဓာတ်»; kabaḷīkāro
āhāro «လုတ်ပြု၍ စားရသော အာဟာရ» -> «စားသောက်ရသော အာဟာရ»; the fetter, knot, hindrance and clinging names (5: «ကာမရာဂ
နှောင်ကြိုး», «မုန်းတီးမှု နှောင်ကြိုး», «… ကိုယ်ကို ချည်နှောင်သော အထုံး», «ကာမဆန္ဒ အတားအဆီး», «ကာမကို စွဲလမ်းမှု» …);
dhammavicayasambojjhaṅgo «… ဗောဇ္ဈင်» -> «… ဟူသော သိမြင်ခြင်း၏ အင်္ဂါ»; cittaja «စိတ်ကြောင့် ဖြစ်သော» -> «စိတ်မှ
မွေးဖွားသော». Agreed: lobha, dosa, moha, issā, abhijjhā, diṭṭhi, uddhacca, ahirika, anottappa, cakkhundriya, āpodhātu
(spacing only), rūpassa upacayo / santati.

## New recurring terms («Pāli = Burmese»)
Generated from the make_ch4.py tables (synonyms and names, fixed phrases, list heads, headings and colophons, variant
kinds). The frames are listed above.

### Synonyms and names (added to SYN)

lobho = လောဘ
doso = ဒေါသ
moho = မောဟ
jātā = မွေးဖွားပြီးသော
bhūtā = ဖြစ်ပြီးသော
sañjātā = ကောင်းစွာ မွေးဖွားပြီးသော
nibbattā = ပေါ်ထွက်ပြီးသော
abhinibbattā = ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော
pātubhūtā = ထင်ရှားလာပြီးသော
uppannā = ဖြစ်ပေါ်ပြီးသော
samuppannā = ကောင်းစွာ ဖြစ်ပေါ်ပြီးသော
uṭṭhitā = ထပေါ်ပြီးသော
samuṭṭhitā = ကောင်းစွာ ထပေါ်ပြီးသော
ajātā = မမွေးဖွားသေးသော
abhūtā = မဖြစ်သေးသော
asañjātā = ကောင်းစွာ မမွေးဖွားသေးသော
anibbattā = မပေါ်ထွက်သေးသော
anabhinibbattā = ထင်ရှားစွာ မပေါ်ထွက်သေးသော
apātubhūtā = ထင်ရှား မလာသေးသော
anuppannā = မဖြစ်ပေါ်သေးသော
asamuppannā = ကောင်းစွာ မဖြစ်ပေါ်သေးသော
anuṭṭhitā = မထပေါ်သေးသော
asamuṭṭhitā = ကောင်းစွာ မထပေါ်သေးသော
atītā = အတိတ် ဖြစ်သော
anāgatā = အနာဂတ် ဖြစ်သော
paccuppannā = ပစ္စုပ္ပန် ဖြစ်သော
niruddhā = ချုပ်ငြိမ်းပြီးသော
vigatā = ကင်းပျောက်ပြီးသော
vipariṇatā = ဖောက်ပြန် ပြောင်းလဲပြီးသော
atthaṅgatā = ကွယ်ပျောက်ပြီးသော
abbhatthaṅgatā = လုံးဝ ကွယ်ပျောက်ပြီးသော
uppajjitvā vigatā = ဖြစ်ပေါ်ပြီးမှ ကင်းပျောက်ပြီးသော
uppannaṃsena saṅgahitā = ဖြစ်ပေါ်ပြီးသော အပိုင်း၌ အကျုံးဝင်သော
anuppannaṃsena saṅgahitā = မဖြစ်ပေါ်သေးသော အပိုင်း၌ အကျုံးဝင်သော
atītaṃsena saṅgahitā = အတိတ် အပိုင်း၌ အကျုံးဝင်သော
anāgataṃsena saṅgahitā = အနာဂတ် အပိုင်း၌ အကျုံးဝင်သော
paccuppannaṃsena saṅgahitā = ပစ္စုပ္ပန် အပိုင်း၌ အကျုံးဝင်သော
ajjhattaṃ = မိမိ၏ အတွင်း၌ ဖြစ်သော
paccattaṃ = ကိုယ်စီ ဖြစ်သော
niyatā = သီးသန့် ဖြစ်သော
pāṭipuggalikā = ပုဂ္ဂိုလ်တစ်ဦးချင်းစီ၏ ဖြစ်သော
upādiṇṇā = ကံကြောင့် ဖြစ်သော
vicikicchā = ယုံမှားမှု
diṭṭhi = အယူ
diṭṭhigataṃ = အယူ၌ ကျရောက်ခြင်း
diṭṭhigahanaṃ = အယူ တောအုပ်
diṭṭhikantāro = အယူ ကန္တာရ
diṭṭhivisūkāyikaṃ = အယူ၏ ကောက်ကွေးမှု
diṭṭhivipphanditaṃ = အယူ၏ တုန်လှုပ်မှု
diṭṭhisaṃyojanaṃ = အယူ နှောင်ကြိုး
gāho = စွဲကိုင်ခြင်း
paṭiggāho = ခိုင်မြဲစွာ စွဲကိုင်ခြင်း
patiṭṭhāho = ခိုင်မြဲစွာ စွဲကိုင်ခြင်း
abhiniveso = သက်ဝင်ယုံကြည်ခြင်း
parāmāso = မှားယွင်းသော ယူဆမှု
kummaggo = လမ်းမှား
micchāpatho = မှားယွင်းသော လမ်းကြောင်း
micchattaṃ = မှားယွင်းမှု
titthāyatanaṃ = အယူဝါဒတို့၏ တည်ရာ
vipariyāsaggāho = ပြောင်းပြန် စွဲကိုင်ခြင်း
kaṅkhā = သံသယ
kaṅkhāyanā = သံသယ ဖြစ်ခြင်း
kaṅkhāyitattaṃ = သံသယ ဖြစ်ထားသော အဖြစ်
vimati = စိတ်ရှုပ်ထွေးခြင်း
dveḷhakaṃ = စိတ် နှစ်ခွ ဖြစ်ခြင်း
dvedhāpatho = လမ်း နှစ်ခွ
saṃsayo = ဒွိဟ ဖြစ်ခြင်း
anekaṃsaggāho = တစ်ထစ်ချ မယူနိုင်ခြင်း
āsappanā = ယိမ်းယိုင်ခြင်း
parisappanā = ပတ်ချာလည် ယိမ်းယိုင်ခြင်း
apariyogāhanā = နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း
thambhitattaṃ cittassa = စိတ် တောင့်တင်းနေသော အဖြစ်
manovilekho = မနောကို ခြစ်ကုတ်ခြင်း
metti = မေတ္တာ
mettāyanā = မေတ္တာ ထားခြင်း
mettāyitattaṃ = မေတ္တာ ထားသော အဖြစ်
anuddā = သနားကြင်နာခြင်း
anuddāyanā = သနားကြင်နာနေခြင်း
anudāyitattaṃ = သနားကြင်နာထားသော အဖြစ်
hitesitā = အကျိုးကို လိုလားခြင်း
anukampā = စာနာ ထောက်ထားခြင်း
dhammavicayasambojjhaṅgo = သဘောတရားများကို စိစစ်ခြင်း ဟူသော သိမြင်ခြင်း၏ အင်္ဂါ
maggaṅgaṃ = မဂ်၏ အင်္ဂါ
maggapariyāpannaṃ = မဂ်၌ အကျုံးဝင်သော အရာ
aññāṇaṃ = မသိခြင်း
adassanaṃ = မမြင်ခြင်း
anabhisamayo = ထင်ထင်ရှားရှား မသိမြင်ခြင်း
ananubodho = လိုက်၍ မနားလည်ခြင်း
asambodho = ကောင်းစွာ မနားလည်ခြင်း
appaṭivedho = ထိုးဖောက်၍ မသိခြင်း
asaṃgāhanā = စုစည်း၍ မယူနိုင်ခြင်း
asamapekkhanā = ညီညီညွတ်ညွတ် မရှုမြင်ခြင်း
apaccavekkhaṇā = ပြန်လည် မဆင်ခြင်ခြင်း
apaccakkhakammaṃ = ကိုယ်တိုင် ထင်ထင်ရှားရှား မပြုခြင်း
dummejjhaṃ = ဉာဏ်နုံခြင်း
bālyaṃ = မိုက်မဲခြင်း
asampajaññaṃ = ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိခြင်း
pamoho = အလွန် တွေဝေခြင်း
sammoho = လုံးဝ တွေဝေခြင်း
avijjā = အမှန်ကို မသိမှု
avijjogho = အမှန်ကို မသိမှု ရေအလျဉ်
avijjāyogo = အမှန်ကို မသိမှု ထမ်းပိုး
avijjānusayo = အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း
avijjāpariyuṭṭhānaṃ = အမှန်ကို မသိမှု ထကြွခြင်း
avijjālaṅgī = အမှန်ကို မသိမှု တံခါးကန့်လန့်
akusalamūlaṃ = အကုသိုလ်၏ အမြစ်
rāgo = ရာဂ
sārāgo = တပ်မက်ခြင်း
anunayo = လိုက်လျောခြင်း
anurodho = သဘောတူ လိုက်ပါခြင်း
nandī = နှစ်သက်ခြင်း
nandīrāgo = နှစ်သက်မှု ရာဂ
cittassa sārāgo = စိတ်၏ တပ်မက်ခြင်း
icchā = အလိုရှိခြင်း
mucchā = မိန်းမောခြင်း
ajjhosānaṃ = နစ်မွန်းခြင်း
gedho = ငမ်းငမ်းတက် လိုချင်ခြင်း
paligedho = အလွန် ငမ်းငမ်းတက် လိုချင်ခြင်း
saṅgo = တွယ်ကပ်ခြင်း
paṅko = ရွှံ့ညွန်
ejā = တုန်လှုပ်ခြင်း
māyā = လှည့်စားတတ်ခြင်း
janikā = မွေးဖွားပေးတတ်သူ
sañjananī = ကောင်းစွာ မွေးဖွားပေးတတ်သူ
sibbinī = ချုပ်လုပ်တတ်သူ
jālinī = ပိုက်ကွန်ကဲ့သို့ ဖြစ်သူ
saritā = စီးဆင်းတတ်သူ
visattikā = ပျံ့နှံ့ တွယ်ကပ်တတ်သူ
suttaṃ = ချည်ကြိုး
visaṭā = ပျံ့နှံ့ခြင်း
āyūhinī = ကြိုးပမ်းစေတတ်သူ
dutiyā = အဖော်
paṇidhi = စိတ်ညွှတ်ခြင်း
bhavanetti = ဘဝသို့ ဆွဲဆောင်သော ကြိုး
vanaṃ = တော
vanatho = တောအုပ်
santhavo = ရင်းနှီးခြင်း
sineho = ချစ်ခင်ခြင်း
apekkhā = ငဲ့ကွက်ခြင်း
paṭibandhu = ဆွေမျိုး
āsā = မျှော်လင့်ခြင်း
āsisanā = တောင့်တခြင်း
āsisitattaṃ = တောင့်တထားသော အဖြစ်
lābhāsā = လာဘ်ကို မျှော်လင့်ခြင်း
dhanāsā = ဥစ္စာကို မျှော်လင့်ခြင်း
puttāsā = သားသမီးကို မျှော်လင့်ခြင်း
jīvitāsā = အသက်ကို မျှော်လင့်ခြင်း
jappā = တမ်းတခြင်း
pajappā = အလွန် တမ်းတခြင်း
abhijappā = ထူးထူးခြားခြား တမ်းတခြင်း
jappanā = တမ်းတနေခြင်း
jappitattaṃ = တမ်းတထားသော အဖြစ်
loluppaṃ = လိုချင်လွန်းခြင်း
loluppāyanā = လိုချင်လွန်းနေခြင်း
loluppāyitattaṃ = လိုချင်လွန်းထားသော အဖြစ်
pucchañjikatā = အမြီး ခါ၍ ချော့မော့ခြင်း
sādhukamyatā = ကောင်းသည်ထက် ကောင်းသည်ကို လိုချင်ခြင်း
adhammarāgo = မတရားသော ရာဂ
visamalobho = ဖောက်ပြန်သော လောဘ
nikanti = စွဲလန်းခြင်း
nikāmanā = အလွန် လိုလားခြင်း
patthanā = ဆုတောင်းခြင်း
pihanā = အားကျ လိုချင်ခြင်း
sampatthanā = ကောင်းစွာ ဆုတောင်းခြင်း
bhavataṇhā = ဘဝကို တပ်မက်မှု
vibhavataṇhā = ဘဝ ပြတ်စဲခြင်းကို တပ်မက်မှု
rūpataṇhā = ရုပ်ကို တပ်မက်မှု
arūpataṇhā = ရုပ်မရှိသော ဘဝကို တပ်မက်မှု
nirodhataṇhā = ချုပ်ငြိမ်းခြင်းကို တပ်မက်မှု
dhammataṇhā = သဘောတရားကို တပ်မက်မှု
ogho = ရေအလျဉ်
yogo = ထမ်းပိုး
gantho = အထုံး
upādānaṃ = စွဲလမ်းမှု
āvaraṇaṃ = ပိတ်ဆို့ခြင်း
nīvaraṇaṃ = အတားအဆီး
chādanaṃ = ဖုံးအုပ်ခြင်း
bandhanaṃ = အချည်အနှောင်
upakkileso = ညစ်နွမ်းစေတတ်သော အညစ်အကြေး
anusayo = ကိန်းအောင်းခြင်း
pariyuṭṭhānaṃ = ထကြွခြင်း
latā = နွယ်ပင်
vevicchaṃ = တစ်ကိုယ်ကောင်းဆန်ခြင်း
dukkhamūlaṃ = ဒုက္ခ၏ အမြစ်
dukkhanidānaṃ = ဒုက္ခ၏ ဇာစ်မြစ်
dukkhappabhavo = ဒုက္ခ၏ ဖြစ်ပေါ်ရာ
mārapāso = မာရ်၏ ကျော့ကွင်း
mārabaḷisaṃ = မာရ်၏ ငါးမျှားချိတ်
māravisayo = မာရ်၏ နယ်ပယ်
taṇhānadī = တပ်မက်မှု မြစ်
taṇhājālaṃ = တပ်မက်မှု ပိုက်ကွန်
taṇhāgaddulaṃ = တပ်မက်မှု ကြိုးသိုင်း
taṇhāsamuddo = တပ်မက်မှု သမုဒ္ဒရာ
abhijjhā = သူ့ဥစ္စာကို လိုချင်ခြင်း
rūpāsā = အဆင်းအရောင်ကို မျှော်လင့်ခြင်း
saddāsā = အသံကို မျှော်လင့်ခြင်း
saddataṇhā = အသံကို တပ်မက်မှု
gandhāsā = အနံ့ကို မျှော်လင့်ခြင်း
gandhataṇhā = အနံ့ကို တပ်မက်မှု
rasāsā = အရသာကို မျှော်လင့်ခြင်း
rasataṇhā = အရသာကို တပ်မက်မှု
phoṭṭhabbāsā = အထိအတွေ့ကို မျှော်လင့်ခြင်း
phoṭṭhabbataṇhā = အထိအတွေ့ကို တပ်မက်မှု
kāmacchando = ကာမကို လိုလားမှု
kāmarāgo = ကာမ ရာဂ
kāmanandī = ကာမကို နှစ်သက်မှု
kāmataṇhā = ကာမကို တပ်မက်မှု
kāmasineho = ကာမကို ချစ်ခင်မှု
kāmapariḷāho = ကာမကြောင့် ပူလောင်မှု
kāmamucchā = ကာမ၌ မိန်းမောမှု
kāmajjhosānaṃ = ကာမ၌ နစ်မွန်းမှု
bhavachando = ဘဝကို လိုလားမှု
bhavarāgo = ဘဝ ရာဂ
bhavanandī = ဘဝကို နှစ်သက်မှု
bhavasineho = ဘဝကို ချစ်ခင်မှု
bhavapariḷāho = ဘဝကြောင့် ပူလောင်မှု
bhavamucchā = ဘဝ၌ မိန်းမောမှု
bhavajjhosānaṃ = ဘဝ၌ နစ်မွန်းမှု
āghāto = ရန်ငြိုးဖွဲ့ခြင်း
paṭighāto = ပြန်လည် ရန်ငြိုးဖွဲ့ခြင်း
paṭighaṃ = စိတ်ထိခိုက်ခြင်း
paṭivirodho = ပြန်လည် ဆန့်ကျင်ခြင်း
kopo = အမျက်ထွက်ခြင်း
pakopo = အလွန် အမျက်ထွက်ခြင်း
sampakopo = ပြင်းစွာ အမျက်ထွက်ခြင်း
padoso = အလွန် ဒေါသထွက်ခြင်း
sampadoso = ပြင်းစွာ ဒေါသထွက်ခြင်း
cittassa byāpatti = စိတ်၏ ဖောက်ပြန်ခြင်း
manopadoso = မနောဖြင့် ဒေါသထွက်ခြင်း
kodho = အမျက်ဒေါသ
kujjhanā = အမျက်ဒေါသ ထွက်ခြင်း
kujjhitattaṃ = အမျက်ဒေါသ ထွက်ထားသော အဖြစ်
dussanā = စိတ်ဆိုးခြင်း
dussitattaṃ = စိတ်ဆိုးထားသော အဖြစ်
byāpatti = ဖောက်ပြန်ခြင်း
byāpajjanā = ညှဉ်းဆဲလိုခြင်း
byāpajjitattaṃ = ညှဉ်းဆဲလိုသော အဖြစ်
virodho = ဆန့်ကျင်ခြင်း
caṇḍikkaṃ = ကြမ်းကြုတ်ခြင်း
asuropo = စကား ကြမ်းခြင်း
anattamanatā cittassa = စိတ်၏ မနှစ်သိမ့်ခြင်း
māno = မာန
maññanā = ထင်မှတ်ခြင်း
maññitattaṃ = ထင်မှတ်ထားသော အဖြစ်
unnati = စိတ် မြင့်တက်ခြင်း
unnamo = ခေါင်းမော့ခြင်း
dhajo = အလံ
sampaggāho = အလွန် မြှင့်တင်ခြင်း
ketukamyatā cittassa = စိတ်၏ အလံ ထူလိုခြင်း
issā = ငြူစူမှု
issāyanā = ငြူစူခြင်း
issāyitattaṃ = ငြူစူထားသော အဖြစ်
usūyā = သဝန်တိုမှု
usūyanā = သဝန်တိုခြင်း
usūyitattaṃ = သဝန်တိုထားသော အဖြစ်
maccheraṃ = ဝန်တိုခြင်း
maccharāyanā = ဝန်တိုနေခြင်း
maccharāyitattaṃ = ဝန်တိုထားသော အဖြစ်
kadariyaṃ = ကပ်စေးနည်းခြင်း
kaṭukañcukatā = တွန့်တိုခြင်း
aggahitattaṃ cittassa = စိတ်၏ တင်းတင်း ဆုပ်ကိုင်ထားသော အဖြစ်
kāmacchandanīvaraṇaṃ = ကာမကို လိုလားမှု အတားအဆီး
byāpādanīvaraṇaṃ = ဖျက်ဆီးလိုစိတ် အတားအဆီး
thinamiddhanīvaraṇaṃ = ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု အတားအဆီး
uddhaccakukkuccanīvaraṇaṃ = ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု အတားအဆီး
uddhaccanīvaraṇaṃ = ယောက်ယက်ခတ်မှု အတားအဆီး
kukkuccanīvaraṇaṃ = နောင်တ ပူပန်မှု အတားအဆီး
vicikicchānīvaraṇaṃ = ယုံမှားမှု အတားအဆီး
avijjānīvaraṇaṃ = အမှန်ကို မသိမှု အတားအဆီး
diṭṭhiparāmāso = အယူဆိုင်ရာ မှားယွင်းသော ယူဆမှု
kāmupādānaṃ = ကာမ စွဲလမ်းမှု
diṭṭhupādānaṃ = အယူ စွဲလမ်းမှု
sīlabbatupādānaṃ = သီလ အကျင့်ဝတ် စွဲလမ်းမှု
attavādupādānaṃ = အတ္တဟူသော ဝါဒ စွဲလမ်းမှု
thinaṃ = ထိုင်းမှိုင်းမှု
middhaṃ = ငိုက်မျဉ်းမှု
uddhaccaṃ = ယောက်ယက်ခတ်မှု
kukkuccaṃ = နောင်တ ပူပန်မှု
ahirikaṃ = ဒုစရိုက်ကို မရှက်မှု
anottappaṃ = ဒုစရိုက်ကို မကြောက်ရွံ့မှု
akallatā = မကျန်းမာခြင်း
akammaññatā = အသုံးပြုရန် မသင့်တော်ခြင်း
olīyanā = တွန့်ဆုတ်ခြင်း
sallīyanā = လုံးဝ တွန့်ဆုတ်ခြင်း
līnaṃ = အားပျော့ခြင်း
līyanā = အားပျော့နေခြင်း
līyitattaṃ = အားပျော့ထားသော အဖြစ်
thiyanā = ထိုင်းမှိုင်းခြင်း
thiyitattaṃ cittassa = စိတ်၏ ထိုင်းမှိုင်းထားသော အဖြစ်
onāho = ပိတ်ဖုံးခံရခြင်း
pariyonāho = အပြည့် ပိတ်ဖုံးခံရခြင်း
antosamorodho = အတွင်း၌ ပိတ်ဆို့ခံရခြင်း
soppaṃ = အိပ်ငိုက်ခြင်း
pacalāyikā = ငိုက်ဆင်းခြင်း
supanā = အိပ်ပျော်ခြင်း
supitattaṃ = အိပ်ပျော်ထားသော အဖြစ်
avūpasamo = မငြိမ်ဝပ်ခြင်း
cetaso vikkhepo = စိတ်၏ ပျံ့လွင့်ခြင်း
bhantattaṃ cittassa = စိတ်၏ ယိမ်းထိုးနေသော အဖြစ်
kukkuccāyanā = နောင်တ ပူပန်ခြင်း
kukkuccāyitattaṃ = နောင်တ ပူပန်ထားသော အဖြစ်
cetaso vippaṭisāro = စိတ်၏ နောင်တ ရခြင်း
saṅkhā = ရေတွက် ခေါ်ဝေါ်ခြင်း
samaññā = အများ သမုတ်ခြင်း
paññatti = သတ်မှတ်ချက်
vohāro = ပြောဆို သုံးနှုန်းခြင်း
nāmaṃ = အမည်
nāmakammaṃ = အမည်ပေးခြင်း
nāmadheyyaṃ = အမည်နာမ
nirutti = စကားဖြင့် ဖော်ပြမှု
byañjanaṃ = ဖော်ပြသော စကားလုံး
abhilāpo = ခေါ်ဆိုခြင်း
dovacassāyaṃ = စကား နားမထောင်ခြင်း
dovacassiyaṃ = စကား နားမထောင်သော အဖြစ်
dovacassatā = သွန်သင်ချက်ကို နားမထောင်ခြင်း
vippaṭikūlaggāhitā = ဆန့်ကျင်ဘက် ယူခြင်း
vipaccanīkasātatā = ဆန့်ကျင်ခြင်း၌ နှစ်သက်ခြင်း
anādariyaṃ = မလေးစားခြင်း
anādaratā = မလေးစားသော အဖြစ်
agāravatā = ရိုသေမှု မရှိခြင်း
appaṭissavatā = နာခံမှု မရှိခြင်း
sovacassāyaṃ = စကား နားထောင်ခြင်း
sovacassiyaṃ = စကား နားထောင်သော အဖြစ်
sovacassatā = သွန်သင်ချက်ကို နားထောင်ခြင်း
appaṭikūlaggāhitā = ဆန့်ကျင်ဘက် မယူခြင်း
avipaccanīkasātatā = ဆန့်ကျင်ခြင်း၌ မနှစ်သက်ခြင်း
sagāravatā = ရိုသေမှု ရှိခြင်း
sādariyaṃ = လေးစားခြင်း
sādaratā = လေးစားသော အဖြစ်
sappaṭissavatā = နာခံမှု ရှိခြင်း
sevanā = ပေါင်းသင်းခြင်း
nisevanā = နီးကပ်စွာ ပေါင်းသင်းခြင်း
saṃsevanā = ကောင်းစွာ ပေါင်းသင်းခြင်း
bhajanā = ဆည်းကပ်ခြင်း
sambhajanā = ကောင်းစွာ ဆည်းကပ်ခြင်း
bhatti = ကိုးကွယ်ခြင်း
sambhatti = ကောင်းစွာ ကိုးကွယ်ခြင်း
taṃsampavaṅkatā = ထိုသူတို့ဘက်သို့ ညွတ်ကိုင်းခြင်း
āpattikusalatā = အပြစ်တို့၌ ကျွမ်းကျင်ခြင်း
samāpattikusalatā = ဈာန် ဝင်စားရာ၌ ကျွမ်းကျင်ခြင်း
dhātukusalatā = ဓာတ်တို့၌ ကျွမ်းကျင်ခြင်း
manasikārakusalatā = နှလုံးသွင်းခြင်း၌ ကျွမ်းကျင်ခြင်း
āyatanakusalatā = အာရုံခံ နယ်ပယ်တို့၌ ကျွမ်းကျင်ခြင်း
vuṭṭhānakusalatā = ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း
ajjavatā = ဖြောင့်မတ်သော အဖြစ်
nīcacittatā = စိတ် နှိမ့်ချခြင်း
khanti = သည်းခံခြင်း
khamanatā = ခွင့်လွှတ်ခြင်း
adhivāsanatā = လက်ခံ သည်းညည်းခံခြင်း
acaṇḍikkaṃ = မကြမ်းကြုတ်ခြင်း
anasuropo = စကား မကြမ်းခြင်း
saṇhavācatā = ချောမွေ့သော စကားကို ဆိုခြင်း
sakhilavācatā = ချိုသာသော စကားကို ဆိုခြင်း
apharusavācatā = မကြမ်းတမ်းသော စကားကို ဆိုခြင်း
agutti = မစောင့်ထိန်းခြင်း
agopanā = မကာကွယ်ခြင်း
anārakkho = မစောင့်ရှောက်ခြင်း
asaṃvaro = မစောင့်စည်းခြင်း
gutti = စောင့်ထိန်းခြင်း
gopanā = ကာကွယ်ခြင်း
ārakkho = စောင့်ရှောက်ခြင်း
saṃvaro = စောင့်စည်းခြင်း
asantuṭṭhitā = ရောင့်ရဲမှု မရှိခြင်း
amattaññutā = အတိုင်းအရှည်ကို မသိခြင်း
appaṭisaṅkhā bhojane = အစားအစာ၌ ပြန်လည် မဆင်ခြင်ခြင်း
santuṭṭhitā = ရောင့်ရဲခြင်း
mattaññutā = အတိုင်းအရှည်ကို သိခြင်း
paṭisaṅkhā bhojane = အစားအစာ၌ ပြန်လည် ဆင်ခြင်ခြင်း
asati = သတိ မရှိခြင်း
ananussati = အဖန်ဖန် မအောက်မေ့ခြင်း
appaṭissati = ပြန်လည် မအောက်မေ့ခြင်း
asaraṇatā = မမှတ်မိခြင်း
adhāraṇatā = စွဲမှတ် မထားခြင်း
pilāpanatā = အပေါ်ယံ ပေါ်လောခြင်း
sammusanatā = မေ့လျော့ခြင်း
āsevanā = အလေ့အကျင့် ပြုခြင်း
bhāvanā = ပွားများခြင်း
bahulīkammaṃ = အကြိမ်ကြိမ် ပြုခြင်း
bhiyyokamyatā = ပိုမို လိုလားခြင်း
sakkaccakiriyatā = ရိုသေစွာ ပြုခြင်း
sātaccakiriyatā = အစဉ်တစိုက် ပြုခြင်း
aṭṭhitakiriyatā = ရပ်တန့်ခြင်း မရှိဘဲ ပြုခြင်း
anolīnavuttitā = မတွန့်ဆုတ်ဘဲ ကျင့်ခြင်း
asammusanatā = မမေ့လျော့ခြင်း

### Fixed phrases and clauses (PH)

rūpakkhandho = ရုပ် အစုအဝေး
rūpaṃ = ရုပ်
saṅkhārā = ပြုပြင်ဖန်တီးမှုများ
viññāṇaṃ = သိစိတ်
kāyakammaṃ = ကိုယ်ဖြင့် ပြုသော ကံ
vacīkammaṃ = နှုတ်ဖြင့် ပြုသော ကံ
manokammaṃ = မနောဖြင့် ပြုသော ကံ
Tīṇi kusalamūlāni = ကုသိုလ်၏ အမြစ် သုံးပါး
Tīṇi akusalamūlāni = အကုသိုလ်၏ အမြစ် သုံးပါး
taṃsampayutto = ထိုတို့နှင့် ယှဉ်တွဲသော
taṃsamuṭṭhānaṃ = ထိုတို့မှ ဖြစ်ပေါ်လာသော
tadekaṭṭhā ca kilesā = ထိုတို့နှင့် တစ်နေရာတည်း တည်ရှိသော ကိလေသာများလည်း
Tadekaṭṭho = ထိုတို့နှင့် တစ်နေရာတည်း တည်ရှိသော
Avaseso = ကြွင်းကျန်သော
avasesā = ကြွင်းကျန်သော
Kusalākusalānaṃ dhammānaṃ vipākā = ကုသိုလ်နှင့် အကုသိုလ် သဘောတရားတို့၏ အကျိုး ဖြစ်သော
Kusalākusalānaṃ dhammānaṃ avipakkavipākānaṃ vipākā = အကျိုး မရင့်ကျက်သေးသော ကုသိုလ်နှင့် အကုသိုလ် သဘောတရားတို့၏ အကျိုး ဖြစ်သော
ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā = ပြုမှုမျှသာ ဖြစ်၍ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်၊ ကံ၏ အကျိုးလည်း မဟုတ်သော သဘောတရားများလည်း
sabbañca rūpaṃ = ရုပ် အားလုံးလည်း
asaṅkhatā ca dhātu = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော ဓာတ်လည်း
Asaṅkhatā dhātu = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော ဓာတ်
Kusalākusalā dhammā = ကုသိုလ်နှင့် အကုသိုလ် သဘောတရားများ
kusalābyākatā dhammā = ကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ
kusalākusalābyākatā dhammā = ကုသိုလ်၊ အကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ
Sabbeva kāmāvacarā kusalākusalābyākatā dhammā = ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်၊ အကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား အားလုံး
maggā ca = မဂ်များလည်း
maggaphalāni ca = မဂ်၏ ဖိုလ်များလည်း
yañca rūpaṃ kammassa katattā = ကံကို ပြုခဲ့ခြင်းကြောင့် ဖြစ်သော ရုပ်လည်း
yañca rūpaṃ na kammassa katattā = ကံကို ပြုခဲ့ခြင်းကြောင့် ဖြစ်သည် မဟုတ်သော ရုပ်လည်း
yañca rūpaṃ kammassa katattā uppajjissati = ကံကို ပြုခဲ့ခြင်းကြောင့် ဖြစ်ပေါ်လာမည့် ရုပ်လည်း
Te dhamme ṭhapetvā = ထိုသဘောတရားတို့ကို ချန်ထား၍
Cattāro maggā apariyāpannā = ဘဝဘုံတို့၌ အကျုံးမဝင်သော မဂ် လေးပါး
heṭṭhimāni ca tīṇi sāmaññaphalāni = အောက်ပိုင်း ရဟန်းအဖြစ်၏ အကျိုး သုံးပါးလည်း
Upariṭṭhimaṃ = အမြင့်ဆုံး
arahattaphalaṃ = ရဟန္တာ ဖိုလ်
Pañca kammāni ānantarikāni = နောက်ဘဝ၌ ချက်ချင်း အကျိုးပေးသော ကံ ငါးပါး
yā ca micchādiṭṭhiniyatā = ကျိန်းသေသော မှားယွင်းသော အယူလည်း
yā ca micchādiṭṭhi niyatā = ကျိန်းသေသော မှားယွင်းသော အယူလည်း
Ariyamaggaṃ ārabbha ye uppajjanti cittacetasikā dhammā = အရိယာ မဂ်ကို အာရုံပြု၍ ဖြစ်ပေါ်ကြသော စိတ်နှင့် စိတ်၏ အဖော် သဘောတရားများ
Ariyamaggaṃ adhipatiṃ karitvā ye uppajjanti cittacetasikā dhammā = အရိယာ မဂ်ကို အကြီးအမှူး ပြု၍ ဖြစ်ပေါ်ကြသော စိတ်နှင့် စိတ်၏ အဖော် သဘောတရားများ
Ariyamaggasamaṅgissa = အရိယာ မဂ်နှင့် ပြည့်စုံသူ၏
maggaṅgāni ṭhapetvā = မဂ်၏ အင်္ဂါတို့ကို ချန်ထား၍
sammādiṭṭhi maggo ceva hetu ca = မှန်ကန်သော အယူသည် မဂ်လည်း ဖြစ်၊ အမြစ်လည်း ဖြစ်သည်
sammādiṭṭhiṃ ṭhapetvā = မှန်ကန်သော အယူကို ချန်ထား၍
vīmaṃsādhipateyyaṃ maggaṃ bhāvayantassa = စူးစမ်းဆင်ခြင်မှုကို အကြီးအမှူးပြုသော မဂ်ကို ပွားများနေသူ၏
vīmaṃsaṃ ṭhapetvā = စူးစမ်းဆင်ခြင်မှုကို ချန်ထား၍
Tadubhayaṃ = ထိုနှစ်မျိုးလုံး
yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ = မမြင်နိုင်သော၊ ထိခိုက်မှု မရှိသော၊ သဘောတရား အာရုံခံ နယ်ပယ်၌ အကျုံးဝင်သော ရုပ်လည်း
Pañcakkhandhā = အစုအဝေး ငါးပါး
Cattāro ca mahābhūtā = မူလဓာတ်ကြီး လေးပါးလည်း
catunnañca mahābhūtānaṃ upādāya rūpaṃ = မူလဓာတ်ကြီး လေးပါးကို မှီ၍ ဖြစ်သော ရုပ်လည်း
Kusalānaṃ vā dhammānaṃ vipākato = ကုသိုလ် သဘောတရားတို့၏ အကျိုး အဖြစ်ဖြင့်ဖြစ်စေ
kiriyābyākatesu vā dhammesu = ပြုမှုမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားတို့၌ဖြစ်စေ
Kusalānaṃ dhammānaṃ vipākato = ကုသိုလ် သဘောတရားတို့၏ အကျိုး အဖြစ်ဖြင့်
Sāsavā = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော
Apariyāpannā = ဘဝဘုံတို့၌ အကျုံးမဝင်သော
Rūpāvacarā = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော
kāmāvacarā = ကာမဘုံနှင့် ဆိုင်သော
rūpāvacarā = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော
arūpāvacarā = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော
apariyāpannā = ဘဝဘုံတို့၌ အကျုံးမဝင်သော
kāmāvacare = ကာမဘုံနှင့် ဆိုင်သည်၌
rūpāvacare = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သည်၌
arūpāvacare = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သည်၌
apariyāpanne = ဘဝဘုံတို့၌ အကျုံးမဝင်သည်၌
Sukhabhūmiyaṃ = သာယာမှု ရှိရာ အဆင့်၌
Dukkhabhūmiyaṃ = နာကျင်မှု ရှိရာ အဆင့်၌
Adukkhamasukhabhūmiyaṃ = မနာကျင် မသာယာမှု ရှိရာ အဆင့်၌
Savitakkasavicārabhūmiyaṃ = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိရာ အဆင့်၌
Pītibhūmiyaṃ = ပီတိ ရှိရာ အဆင့်၌
Upekkhābhūmiyaṃ = ဥပေက္ခာ ရှိရာ အဆင့်၌
Savitakkabhūmiyaṃ = စတင်ကြံစည်မှု ရှိရာ အဆင့်၌
Savicārabhūmiyaṃ = ဆက်လက်သုံးသပ်မှု ရှိရာ အဆင့်၌
Sappītikabhūmiyaṃ = ပီတိ ရှိရာ အဆင့်၌
Avitakkavicāramattabhūmiyaṃ = စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိရာ အဆင့်၌
Avitakkaavicārabhūmiyaṃ = စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိရာ အဆင့်၌
Avitakkabhūmiyaṃ = စတင်ကြံစည်မှု မရှိရာ အဆင့်၌
Avicārabhūmiyaṃ = ဆက်လက်သုံးသပ်မှု မရှိရာ အဆင့်၌
Appītikabhūmiyaṃ = ပီတိ မရှိရာ အဆင့်၌
Na pītibhūmiyaṃ = ပီတိ ရှိရာ အဆင့် မဟုတ်သည့် နေရာ၌
Na sukhabhūmiyaṃ = သာယာမှု ရှိရာ အဆင့် မဟုတ်သည့် နေရာ၌
Na upekkhābhūmiyaṃ = ဥပေက္ခာ ရှိရာ အဆင့် မဟုတ်သည့် နေရာ၌
sukhaṃ vedanaṃ ṭhapetvā = သာယာသော ခံစားမှုကို ချန်ထား၍
dukkhaṃ vedanaṃ ṭhapetvā = နာကျင်သော ခံစားမှုကို ချန်ထား၍
adukkhamasukhaṃ vedanaṃ ṭhapetvā = မနာကျင် မသာယာသော ခံစားမှုကို ချန်ထား၍
vitakkavicāre ṭhapetvā = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုကို ချန်ထား၍
vicāraṃ ṭhapetvā = ဆက်လက်သုံးသပ်မှုကို ချန်ထား၍
vitakkaṃ ṭhapetvā = စတင်ကြံစည်မှုကို ချန်ထား၍
pītiṃ ṭhapetvā = ပီတိကို ချန်ထား၍
sukhaṃ ṭhapetvā = သာယာမှုကို ချန်ထား၍
upekkhaṃ ṭhapetvā = ဥပေက္ခာကို ချန်ထား၍
rūpāyatanaṃ = အဆင်းအရောင် အာရုံခံ နယ်ပယ်
saddāyatanaṃ = အသံ အာရုံခံ နယ်ပယ်
gandhāyatanaṃ = အနံ့ အာရုံခံ နယ်ပယ်
rasāyatanaṃ = အရသာ အာရုံခံ နယ်ပယ်
phoṭṭhabbāyatanaṃ = အထိအတွေ့ အာရုံခံ နယ်ပယ်
cakkhāyatanaṃ = မျက်စိ အာရုံခံ နယ်ပယ်
cakkhuviññāṇaṃ = မျက်စိ သိစိတ်
cakkhuviññeyyā = မျက်စိဖြင့် သိနိုင်သော
sotāyatanaṃ = နား အာရုံခံ နယ်ပယ်
sotaviññāṇaṃ = နား သိစိတ်
sotaviññeyyā = နားဖြင့် သိနိုင်သော
ghānāyatanaṃ = နှာခေါင်း အာရုံခံ နယ်ပယ်
ghānaviññāṇaṃ = နှာခေါင်း သိစိတ်
ghānaviññeyyā = နှာခေါင်းဖြင့် သိနိုင်သော
jivhāyatanaṃ = လျှာ အာရုံခံ နယ်ပယ်
jivhāviññāṇaṃ = လျှာ သိစိတ်
jivhāviññeyyā = လျှာဖြင့် သိနိုင်သော
kāyāyatanaṃ = ကိုယ် အာရုံခံ နယ်ပယ်
kāyaviññāṇaṃ = ကိုယ် သိစိတ်
kāyaviññeyyā = ကိုယ်ဖြင့် သိနိုင်သော
manodhātu = မနော ဓာတ်
Tīṇi saṃyojanāni = နှောင်ကြိုး သုံးပါး
Imāni tīṇi saṃyojanāni = ဤနှောင်ကြိုး သုံးပါး
sakkāyadiṭṭhi = ကိုယ်ကို အတ္တဟု ယူဆသော အယူ
sīlabbataparāmāso = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု
Idha assutavā puthujjano ariyānaṃ adassāvī ariyadhammassa akovido ariyadhamme avinīto sappurisānaṃ adassāvī sappurisadhammassa akovido sappurisadhamme avinīto = ဤလောက၌ အကြားအမြင် မရှိသော ပုထုဇဉ်သည် အရိယာတို့ကို မမြင်ဖူးသူ၊ အရိယာတို့၏ တရား၌ မကျွမ်းကျင်သူ၊ အရိယာတို့၏ တရား၌ မလေ့ကျင့်ထားသူ၊ သူတော်ကောင်းတို့ကို မမြင်ဖူးသူ၊ သူတော်ကောင်းတို့၏ တရား၌ မကျွမ်းကျင်သူ၊ သူတော်ကောင်းတို့၏ တရား၌ မလေ့ကျင့်ထားသူ ဖြစ်၍
rūpaṃ attato samanupassati = ရုပ်ကို အတ္တဟု ရှုမြင်သည်
rūpavantaṃ vā attānaṃ = အတ္တကို ရုပ် ရှိသည်ဟုဖြစ်စေ
attani vā rūpaṃ = အတ္တ၌ ရုပ် ရှိသည်ဟုဖြစ်စေ
rūpasmiṃ vā attānaṃ = ရုပ်၌ အတ္တ ရှိသည်ဟုဖြစ်စေ ရှုမြင်သည်
vedanaṃ attato samanupassati = ခံစားမှုကို အတ္တဟု ရှုမြင်သည်
vedanāvantaṃ vā attānaṃ = အတ္တကို ခံစားမှု ရှိသည်ဟုဖြစ်စေ
attani vā vedanaṃ = အတ္တ၌ ခံစားမှု ရှိသည်ဟုဖြစ်စေ
vedanāya vā attānaṃ = ခံစားမှု၌ အတ္တ ရှိသည်ဟုဖြစ်စေ ရှုမြင်သည်
vedanaṃ = ခံစားမှုကို
saññaṃ attato samanupassati = မှတ်သိမှုကို အတ္တဟု ရှုမြင်သည်
saññāvantaṃ vā attānaṃ = အတ္တကို မှတ်သိမှု ရှိသည်ဟုဖြစ်စေ
attani vā saññaṃ = အတ္တ၌ မှတ်သိမှု ရှိသည်ဟုဖြစ်စေ
saññāya vā attānaṃ = မှတ်သိမှု၌ အတ္တ ရှိသည်ဟုဖြစ်စေ ရှုမြင်သည်
saññaṃ = မှတ်သိမှုကို
saṅkhāre attato samanupassati = ပြုပြင်ဖန်တီးမှုများကို အတ္တဟု ရှုမြင်သည်
saṅkhāravantaṃ vā attānaṃ = အတ္တကို ပြုပြင်ဖန်တီးမှုများ ရှိသည်ဟုဖြစ်စေ
attani vā saṅkhāre = အတ္တ၌ ပြုပြင်ဖန်တီးမှုများ ရှိသည်ဟုဖြစ်စေ
saṅkhāresu vā attānaṃ = ပြုပြင်ဖန်တီးမှုများ၌ အတ္တ ရှိသည်ဟုဖြစ်စေ ရှုမြင်သည်
saṅkhāre = ပြုပြင်ဖန်တီးမှုများကို
viññāṇaṃ attato samanupassati = သိစိတ်ကို အတ္တဟု ရှုမြင်သည်
viññāṇavantaṃ vā attānaṃ = အတ္တကို သိစိတ် ရှိသည်ဟုဖြစ်စေ
attani vā viññāṇaṃ = အတ္တ၌ သိစိတ် ရှိသည်ဟုဖြစ်စေ
viññāṇasmiṃ vā attānaṃ = သိစိတ်၌ အတ္တ ရှိသည်ဟုဖြစ်စေ ရှုမြင်သည်
Satthari kaṅkhati vicikicchati = ဘုရားရှင်အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်
dhamme kaṅkhati vicikicchati = တရားတော်အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်
saṅghe kaṅkhati vicikicchati = သံဃာတော်အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်
sikkhāya kaṅkhati vicikicchati = ကျင့်စဉ်အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်
pubbante kaṅkhati vicikicchati = အတိတ်ကာလအပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်
aparante kaṅkhati vicikicchati = အနာဂတ်ကာလအပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်
pubbantāparante kaṅkhati vicikicchati = အတိတ်ကာလနှင့် အနာဂတ်ကာလအပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်
idappaccayatā paṭiccasamuppannesu dhammesu kaṅkhati vicikicchati = ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော သဘောတရားတို့အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်
Ito bahiddhā samaṇabrāhmaṇānaṃ = ဤသာသနာ အပြင်ဘက်ရှိ ရဟန်းပုဏ္ဏားတို့၏
‘sīlena suddhi = “သီလဖြင့် စင်ကြယ်ခြင်း ရှိသည်
sīlena suddhi = သီလဖြင့် စင်ကြယ်ခြင်း ရှိသည်
vatena suddhi = အကျင့်ဝတ်ဖြင့် စင်ကြယ်ခြင်း ရှိသည်
sīlabbatena suddhī’ti = သီလနှင့် အကျင့်ဝတ်ဖြင့် စင်ကြယ်ခြင်း ရှိသည်”ဟူ၍
sīlabbatena suddhīti = သီလနှင့် အကျင့်ဝတ်ဖြင့် စင်ကြယ်ခြင်း ရှိသည်ဟူ၍
Dukkhe ñāṇaṃ = ဒုက္ခကို သိသော ဉာဏ်
Dukkhe aññāṇaṃ = ဒုက္ခကို မသိခြင်း
dukkhasamudaye ñāṇaṃ = ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို သိသော ဉာဏ်
dukkhasamudaye aññāṇaṃ = ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို မသိခြင်း
dukkhanirodhe ñāṇaṃ = ဒုက္ခ ချုပ်ငြိမ်းခြင်းကို သိသော ဉာဏ်
dukkhanirodhe aññāṇaṃ = ဒုက္ခ ချုပ်ငြိမ်းခြင်းကို မသိခြင်း
dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ = ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော အကျင့်ကို သိသော ဉာဏ်
dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ = ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော အကျင့်ကို မသိခြင်း
pubbante ñāṇaṃ = အတိတ်ကာလကို သိသော ဉာဏ်
pubbante aññāṇaṃ = အတိတ်ကာလကို မသိခြင်း
aparante ñāṇaṃ = အနာဂတ်ကာလကို သိသော ဉာဏ်
aparante aññāṇaṃ = အနာဂတ်ကာလကို မသိခြင်း
pubbantāparante ñāṇaṃ = အတိတ်ကာလနှင့် အနာဂတ်ကာလကို သိသော ဉာဏ်
pubbantāparante aññāṇaṃ = အတိတ်ကာလနှင့် အနာဂတ်ကာလကို မသိခြင်း
idappaccayatā paṭiccasamuppannesu dhammesu ñāṇaṃ = ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော သဘောတရားတို့ကို သိသော ဉာဏ်
idappaccayatā paṭiccasamuppannesu dhammesu aññāṇaṃ = ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော သဘောတရားတို့ကို မသိခြင်း
Anatthaṃ me acarīti āghāto jāyati = ငါ့အား မကောင်းမှု ပြုခဲ့ပြီဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
Anatthaṃ me acarī ti āghāto jāyati = ငါ့အား မကောင်းမှု ပြုခဲ့ပြီဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
anatthaṃ me caratīti āghāto jāyati = ငါ့အား မကောင်းမှု ပြုနေသည်ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
anatthaṃ me carissatīti āghāto jāyati = ငါ့အား မကောင်းမှု ပြုလိမ့်မည်ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
piyassa me manāpassa anatthaṃ acari = ငါ ချစ်ခင်သော နှစ်လိုဖွယ်ကောင်းသော သူအား မကောင်းမှု ပြုခဲ့ပြီ
anatthaṃ carati = မကောင်းမှု ပြုနေသည်
anatthaṃ carissatīti āghāto jāyati = မကောင်းမှု ပြုလိမ့်မည်ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
appiyassa me amanāpassa atthaṃ acari = ငါ မချစ်ခင်သော နှစ်လိုဖွယ် မကောင်းသော သူအား အကျိုးကို ပြုခဲ့ပြီ
atthaṃ carati = အကျိုးကို ပြုနေသည်
atthaṃ carissatīti āghāto jāyati = အကျိုးကို ပြုလိမ့်မည်ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
aṭṭhāne vā pana āghāto jāyati = အကြောင်း မရှိဘဲလည်း ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
kāmāsavo = ကာမ စိတ်အစွန်းအထင်း
bhavāsavo = ဘဝ စိတ်အစွန်းအထင်း
diṭṭhāsavo = အယူ စိတ်အစွန်းအထင်း
avijjāsavo = အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း
kāmarāgasaṃyojanaṃ = ကာမ ရာဂ နှောင်ကြိုး
paṭighasaṃyojanaṃ = စိတ်ထိခိုက်ခြင်း နှောင်ကြိုး
mānasaṃyojanaṃ = မာန နှောင်ကြိုး
diṭṭhisaṃyojanaṃ = အယူ နှောင်ကြိုး
vicikicchāsaṃyojanaṃ = ယုံမှားမှု နှောင်ကြိုး
sīlabbataparāmāsasaṃyojanaṃ = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု နှောင်ကြိုး
bhavarāgasaṃyojanaṃ = ဘဝ ရာဂ နှောင်ကြိုး
issāsaṃyojanaṃ = ငြူစူမှု နှောင်ကြိုး
macchariyasaṃyojanaṃ = ဝန်တိုမှု နှောင်ကြိုး
avijjāsaṃyojanaṃ = အမှန်ကို မသိမှု နှောင်ကြိုး
abhijjhā kāyagantho = သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် အထုံး
byāpādo kāyagantho = ဖျက်ဆီးလိုစိတ်ဟူသော ကိုယ် အထုံး
sīlabbataparāmāso kāyagantho = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် အထုံး
idaṃsaccābhiniveso kāyagantho = ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် အထုံး
abhijjhākāyagantho = သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် အထုံး
idaṃ saccābhiniveso kāyagantho = ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် အထုံး
Cattāro āsavā = စိတ်အစွန်းအထင်း လေးပါး
Dasa saṃyojanāni = နှောင်ကြိုး ဆယ်ပါး
Cattāro ganthā = အထုံး လေးပါး
sassato lokoti vā = လောကသည် ထာဝရ တည်မြဲသည်ဟူ၍ဖြစ်စေ
sassato loko = လောကသည် ထာဝရ တည်မြဲသည်
asassato lokoti vā = လောကသည် ထာဝရ မတည်မြဲဟူ၍ဖြစ်စေ
asassato loko = လောကသည် ထာဝရ မတည်မြဲ
antavā lokoti vā = လောကသည် အဆုံး ရှိသည်ဟူ၍ဖြစ်စေ
antavā loko = လောကသည် အဆုံး ရှိသည်
anantavā lokoti vā = လောကသည် အဆုံး မရှိဟူ၍ဖြစ်စေ
anantavā loko = လောကသည် အဆုံး မရှိ
taṃ jīvaṃ taṃ sarīranti vā = အသက်သည် ကိုယ်ခန္ဓာပင် ဖြစ်သည်ဟူ၍ဖြစ်စေ
taṃ jīvaṃ taṃ sarīraṃ = အသက်သည် ကိုယ်ခန္ဓာပင် ဖြစ်သည်
aññaṃ jīvaṃ aññaṃ sarīranti vā = အသက်နှင့် ကိုယ်ခန္ဓာသည် တခြားစီ ဖြစ်သည်ဟူ၍ဖြစ်စေ
aññaṃ jīvaṃ aññaṃ sarīraṃ = အသက်နှင့် ကိုယ်ခန္ဓာသည် တခြားစီ ဖြစ်သည်
hoti tathāgato paraṃ maraṇāti vā = မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်ဟူ၍ဖြစ်စေ
hoti tathāgato paraṃ maraṇā = မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်
na hoti tathāgato paraṃ maraṇāti vā = မြတ်စွာဘုရားသည် သေပြီးနောက် မရှိဟူ၍ဖြစ်စေ
na hoti tathāgato paraṃ maraṇā = မြတ်စွာဘုရားသည် သေပြီးနောက် မရှိ
hoti ca na ca hoti tathāgato paraṃ maraṇāti vā = မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်လည်း ဖြစ် မရှိသည်လည်း ဖြစ်သည်ဟူ၍ဖြစ်စေ
hoti ca na ca hoti tathāgato paraṃ maraṇā = မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်လည်း ဖြစ် မရှိသည်လည်း ဖြစ်သည်
neva hoti na na hoti tathāgato paraṃ maraṇāti vā = မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်ဟူ၍ဖြစ်စေ
neva hoti na na hoti tathāgato paraṃ maraṇā = မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်
idameva saccaṃ moghamaññanti vā = ဤအရာသာ အမှန် ဖြစ်၍ အခြားအရာသည် အချည်းနှီး ဖြစ်သည်ဟူ၍ဖြစ်စေ
Seyyohamasmīti māno = ငါသည် သာလွန်သူ ဖြစ်သည်ဟူသော မာန
sadisohamasmīti māno = ငါသည် တူညီသူ ဖြစ်သည်ဟူသော မာန
hīnohamasmīti māno = ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်ဟူသော မာန
Pañca macchariyāni = ဝန်တိုမှု ငါးပါး
āvāsamacchariyaṃ = နေရာထိုင်ခင်းကို ဝန်တိုမှု
kulamacchariyaṃ = ကိုးကွယ်သော အိမ်ကို ဝန်တိုမှု
lābhamacchariyaṃ = လာဘ်ကို ဝန်တိုမှု
vaṇṇamacchariyaṃ = ဂုဏ်သတင်းကို ဝန်တိုမှု
dhammamacchariyaṃ = တရားကို ဝန်တိုမှု
ahirīkaṃ = ဒုစရိုက်ကို မရှက်မှု
Cattāro oghā = ရေအလျဉ် လေးပါး
Cattāro yogā = ထမ်းပိုး လေးပါး
Cha nīvaraṇā = အတားအဆီး ခြောက်ပါး
Cattāri upādānāni = စွဲလမ်းမှု လေးပါး
Dasa kilesavatthūni = ကိလေသာ ဖြစ်ရာ အခြေခံ ဆယ်ပါး
Atthi thinaṃ = ထိုင်းမှိုင်းမှု ရှိသည်
atthi middhaṃ = ငိုက်မျဉ်းမှု ရှိသည်
Atthi uddhaccaṃ = ယောက်ယက်ခတ်မှု ရှိသည်
atthi kukkuccaṃ = နောင်တ ပူပန်မှု ရှိသည်
Iti idañca thinaṃ = ဤသို့ ဤထိုင်းမှိုင်းမှုလည်း
idañca middhaṃ = ဤငိုက်မျဉ်းမှုလည်း
Iti idañca uddhaccaṃ = ဤသို့ ဤယောက်ယက်ခတ်မှုလည်း
idañca kukkuccaṃ = ဤနောင်တ ပူပန်မှုလည်း
Akappiye kappiyasaññitā = မအပ်စပ်သည်၌ အပ်စပ်သည်ဟု မှတ်ထင်ခြင်း
kappiye akappiyasaññitā = အပ်စပ်သည်၌ မအပ်စပ်သည်ဟု မှတ်ထင်ခြင်း
avajje vajjasaññitā = အပြစ်မရှိသည်၌ အပြစ်ရှိသည်ဟု မှတ်ထင်ခြင်း
vajje avajjasaññitā = အပြစ်ရှိသည်၌ အပြစ်မရှိသည်ဟု မှတ်ထင်ခြင်း
Cittañca = စိတ်လည်း
avasesañca rūpaṃ = ကြွင်းကျန်သော ရုပ်လည်း
Cittaṃ na vattabbaṃ = စိတ်ကို မပြောဆိုထိုက်
cittena sampayuttantipi = စိတ်နှင့် ယှဉ်တွဲသည်ဟူ၍လည်း
cittena vippayuttantipi = စိတ်နှင့် ကင်းကွာသည်ဟူ၍လည်း
cittena saṃsaṭṭhantipi = စိတ်နှင့် ရောနှောသည်ဟူ၍လည်း
cittena visaṃsaṭṭhantipi = စိတ်နှင့် မရောနှောသည်ဟူ၍လည်း
yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ = စိတ်မှ မွေးဖွားသော၊ စိတ်ကို အကြောင်းပြုသော၊ စိတ်မှ ဖြစ်ပေါ်လာသော အခြား ရုပ် ရှိသမျှလည်း
kāyaviññatti = ကိုယ်ဖြင့် အရိပ်အမြွက် ပြခြင်း
vacīviññatti = နှုတ်ဖြင့် အရိပ်အမြွက် ပြခြင်း
ākāsadhātu = ကောင်းကင် ဓာတ်
āpodhātu = ရေ ဓာတ်
rūpassa lahutā = ရုပ်၏ ပေါ့ပါးခြင်း
rūpassa mudutā = ရုပ်၏ ပျော့ပျောင်းခြင်း
rūpassa kammaññatā = ရုပ်၏ အသုံးပြုရန် သင့်တော်ခြင်း
rūpassa upacayo = ရုပ်၏ တိုးပွားခြင်း
rūpassa santati = ရုပ်၏ ဆက်လက် ဖြစ်ပေါ်ခြင်း
kabaḷīkāro āhāro = စားသောက်ရသော အာဟာရ
dhammāyatanaṃ = သဘောတရား အာရုံခံ နယ်ပယ်
natthi dinnaṃ = ပေးလှူခြင်း မရှိ
atthi dinnaṃ = ပေးလှူခြင်း ရှိသည်
natthi yiṭṭhaṃ = ယဇ်ပူဇော်ခြင်း မရှိ
atthi yiṭṭhaṃ = ယဇ်ပူဇော်ခြင်း ရှိသည်
natthi hutaṃ = ပူဇော်သကာ ဆက်ကပ်ခြင်း မရှိ
atthi hutaṃ = ပူဇော်သကာ ဆက်ကပ်ခြင်း ရှိသည်
natthi sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko = ကောင်းစွာ ပြုသော ကံ၊ ဆိုးစွာ ပြုသော ကံတို့၏ အသီးအပွင့် အကျိုးဆက် မရှိ
atthi sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko = ကောင်းစွာ ပြုသော ကံ၊ ဆိုးစွာ ပြုသော ကံတို့၏ အသီးအပွင့် အကျိုးဆက် ရှိသည်
natthi ayaṃ loko = ဤလောက မရှိ
atthi ayaṃ loko = ဤလောက ရှိသည်
natthi paro loko = တမလွန် လောက မရှိ
atthi paro loko = တမလွန် လောက ရှိသည်
natthi mātā = အမိ မရှိ
atthi mātā = အမိ ရှိသည်
natthi pitā = အဖ မရှိ
atthi pitā = အဖ ရှိသည်
natthi sattā opapātikā = အလိုအလျောက် ပေါ်လာသော သတ္တဝါ မရှိ
atthi sattā opapātikā = အလိုအလျောက် ပေါ်လာသော သတ္တဝါ ရှိသည်
Vitakko ca = စတင်ကြံစည်မှုလည်း
vicāro ca = ဆက်လက်သုံးသပ်မှုလည်း
pīti ca = ပီတိလည်း
sukhañca = သာယာမှုလည်း
upekkhā ca = ဥပေက္ခာလည်း
Heṭṭhato avicinirayaṃ pariyantaṃ karitvā = အောက်၌ အဝီစိ ငရဲကို အဆုံးအစွန် ပြု၍
uparito paranimmitavasavattī deve = အထက်၌ ပရနိမ္မိတဝသဝတ္တီ နတ်တို့ကို
anto karitvā = အတွင်း ထည့်သွင်း၍
yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā khandhadhātu āyatanā = ဤအကြား၌ ကျင်လည်သော၊ ဤအကြား၌ အကျုံးဝင်သော အစုအဝေး၊ ဓာတ်၊ အာရုံခံ နယ်ပယ်တို့
Heṭṭhato brahmalokaṃ pariyantaṃ karitvā = အောက်၌ ဗြဟ္မာ့ပြည်ကို အဆုံးအစွန် ပြု၍
uparito akaniṭṭhe deve = အထက်၌ အကနိဋ္ဌ နတ်တို့ကို
yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā = ဤအကြား၌ ကျင်လည်သော၊ ဤအကြား၌ အကျုံးဝင်သော
samāpannassa vā = ဈာန် ဝင်စားသူ၏ဖြစ်စေ
upapannassa vā = ထိုဘုံ၌ ဖြစ်ပေါ်သူ၏ဖြစ်စေ
diṭṭhadhammasukhavihārissa = မျက်မှောက်ဘဝ၌ ချမ်းသာစွာ နေထိုင်သူ၏
diṭṭhadhammasukhavihārissa vā = မျက်မှောက်ဘဝ၌ ချမ်းသာစွာ နေထိုင်သူ၏ဖြစ်စေ
cittacetasikā dhammā = စိတ်နှင့် စိတ်၏ အဖော် သဘောတရားများ
vā cittacetasikā dhammā = ဖြစ်စေ စိတ်နှင့် စိတ်၏ အဖော် သဘောတရားများ
Heṭṭhato ākāsānañcāyatanupage deve pariyantaṃ karitvā = အောက်၌ အာကာသာနဉ္စာယတန ဘုံသို့ ရောက်သော နတ်တို့ကို အဆုံးအစွန် ပြု၍
uparito nevasaññānāsaññāyatanupage deve = အထက်၌ နေဝသညာနာသညာယတန ဘုံသို့ ရောက်သော နတ်တို့ကို
Yaṃ na hirīyati hiriyitabbena = ရှက်ထိုက်သည့်အရာကို မရှက်ခြင်း
na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို မရှက်ခြင်း
Yaṃ na ottappati ottappitabbena = ကြောက်ရွံ့ထိုက်သည့်အရာကို မကြောက်ရွံ့ခြင်း
na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို မကြောက်ရွံ့ခြင်း
Yaṃ hirīyati hiriyitabbena = ရှက်ထိုက်သည့်အရာကို ရှက်ခြင်း
hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို ရှက်ခြင်း
Yaṃ ottappati ottappitabbena = ကြောက်ရွံ့ထိုက်သည့်အရာကို ကြောက်ရွံ့ခြင်း
ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို ကြောက်ရွံ့ခြင်း
Vijjāya sampayuttakā dhammā = အမှန်သိမြင်မှုနှင့် ယှဉ်တွဲသော သဘောတရားများ
Avijjāya sampayuttakā dhammā = အမှန်ကို မသိမှုနှင့် ယှဉ်တွဲသော သဘောတရားများ
Heṭṭhimesu tīsu ariyamaggesu paññā = အောက်ပိုင်း အရိယာ မဂ် သုံးပါးတို့၌ ရှိသော ပညာ
Upariṭṭhime arahattamagge paññā = အမြင့်ဆုံး ရဟန္တာ မဂ်၌ ရှိသော ပညာ
Ahirīkañca anottappañca = ဒုစရိုက်ကို မရှက်မှုလည်း ဒုစရိုက်ကို မကြောက်ရွံ့မှုလည်း
Hirī ca ottappañca = ဒုစရိုက်ကို ရှက်မှုလည်း ဒုစရိုက်ကို ကြောက်ရွံ့မှုလည်း
Kāyaduccaritaṃ = ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်
vacīduccaritaṃ = နှုတ်ဖြင့် ပြုသော ဒုစရိုက်
manoduccaritaṃ = မနောဖြင့် ပြုသော ဒုစရိုက်
Kāyasucaritaṃ = ကိုယ်ဖြင့် ပြုသော သုစရိုက်
vacīsucaritaṃ = နှုတ်ဖြင့် ပြုသော သုစရိုက်
manosucaritaṃ = မနောဖြင့် ပြုသော သုစရိုက်
Bhavissati attā ca loko cāti = အတ္တနှင့် လောကသည် ဆက်လက် တည်ရှိလိမ့်မည်ဟူ၍
Na bhavissati attā ca loko cāti = အတ္တနှင့် လောကသည် ဆက်လက် တည်ရှိလိမ့်မည် မဟုတ်ဟူ၍
Sassato attā ca loko cāti = အတ္တနှင့် လောကသည် ထာဝရ တည်မြဲသည်ဟူ၍
Ucchijjissati attā ca loko cāti = အတ္တနှင့် လောကသည် ပြတ်စဲသွားလိမ့်မည်ဟူ၍
Antavā attā ca loko cāti = အတ္တနှင့် လောကသည် အဆုံး ရှိသည်ဟူ၍
Anantavā attā ca loko cāti = အတ္တနှင့် လောကသည် အဆုံး မရှိဟူ၍
Pubbantaṃ ārabbha = အတိတ်ကာလကို အာရုံပြု၍
Aparantaṃ ārabbha = အနာဂတ်ကာလကို အာရုံပြု၍
Sahadhammike vuccamāne = တရားနှင့် လျော်စွာ သွန်သင် ပြောဆိုသောအခါ
Ye te puggalā assaddhā dussīlā appassutā maccharino duppaññā = ယုံကြည်မှု မရှိသော၊ သီလ ပျက်သော၊ အကြားအမြင် နည်းသော၊ ဝန်တိုသော၊ ပညာ နည်းသော ပုဂ္ဂိုလ်တို့ ရှိကြ၏
Ye te puggalā saddhā sīlavanto bahussutā cāgavanto paññavanto = ယုံကြည်မှု ရှိသော၊ သီလ ရှိသော၊ အကြားအမြင် များသော၊ စွန့်ကြဲမှု ရှိသော၊ ပညာ ရှိသော ပုဂ္ဂိုလ်တို့ ရှိကြ၏
Pañcapi āpattikkhandhā āpattiyo = အပြစ် အစု ငါးပါးလုံးသည် အပြစ်တို့ ဖြစ်သည်
sattapi āpattikkhandhā āpattiyo = အပြစ် အစု ခုနစ်ပါးလုံးသည် အပြစ်တို့ ဖြစ်သည်
Atthi savitakkasavicārā samāpatti = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော ဈာန် ဝင်စားမှု ရှိသည်
atthi avitakkavicāramattā samāpatti = စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော ဈာန် ဝင်စားမှု ရှိသည်
atthi avitakkaavicārā samāpatti = စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော ဈာန် ဝင်စားမှု ရှိသည်
Aṭṭhārasa dhātuyo = ဓာတ် ဆယ့်ရှစ်ပါး
Dvādasāyatanāni = အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး
rūpadhātu = အဆင်းအရောင် ဓာတ်
saddadhātu = အသံ ဓာတ်
gandhadhātu = အနံ့ ဓာတ်
rasadhātu = အရသာ ဓာတ်
phoṭṭhabbadhātu = အထိအတွေ့ ဓာတ်
cakkhudhātu = မျက်စိ ဓာတ်
cakkhuviññāṇadhātu = မျက်စိ သိစိတ် ဓာတ်
sotadhātu = နား ဓာတ်
sotaviññāṇadhātu = နား သိစိတ် ဓာတ်
ghānadhātu = နှာခေါင်း ဓာတ်
ghānaviññāṇadhātu = နှာခေါင်း သိစိတ် ဓာတ်
jivhādhātu = လျှာ ဓာတ်
jivhāviññāṇadhātu = လျှာ သိစိတ် ဓာတ်
kāyadhātu = ကိုယ် ဓာတ်
kāyaviññāṇadhātu = ကိုယ် သိစိတ် ဓာတ်
Avijjāpaccayā saṅkhārā = အမှန်ကို မသိမှုကြောင့် ပြုပြင်ဖန်တီးမှုများ ဖြစ်ပေါ်သည်
saṅkhārapaccayā viññāṇaṃ = ပြုပြင်ဖန်တီးမှုများကြောင့် သိစိတ် ဖြစ်ပေါ်သည်
viññāṇapaccayā nāmarūpaṃ = သိစိတ်ကြောင့် စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း ဖြစ်ပေါ်သည်
nāmarūpapaccayā saḷāyatanaṃ = စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းကြောင့် အာရုံခံ နယ်ပယ် ခြောက်ပါး ဖြစ်ပေါ်သည်
saḷāyatanapaccayā phasso = အာရုံခံ နယ်ပယ် ခြောက်ပါးကြောင့် တွေ့ထိမှု ဖြစ်ပေါ်သည်
phassapaccayā vedanā = တွေ့ထိမှုကြောင့် ခံစားမှု ဖြစ်ပေါ်သည်
vedanāpaccayā taṇhā = ခံစားမှုကြောင့် တပ်မက်မှု ဖြစ်ပေါ်သည်
taṇhāpaccayā upādānaṃ = တပ်မက်မှုကြောင့် စွဲလမ်းမှု ဖြစ်ပေါ်သည်
upādānapaccayā bhavo = စွဲလမ်းမှုကြောင့် ဘဝ ဖြစ်ပေါ်သည်
bhavapaccayā jāti = ဘဝကြောင့် မွေးဖွားခြင်း ဖြစ်ပေါ်သည်
jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā sambhavanti = မွေးဖွားခြင်းကြောင့် အိုခြင်း၊ သေခြင်း၊ စိုးရိမ်ခြင်း၊ ငိုကြွေးခြင်း၊ ကိုယ်ဆင်းရဲခြင်း၊ စိတ်ဆင်းရဲခြင်း၊ ပြင်းစွာ ပူပန်ခြင်းတို့ ဖြစ်ပေါ်ကြသည်
evametassa kevalassa dukkhakkhandhassa samudayo hotīti = ဤသို့ ဤဒုက္ခ အစုအဝေး အားလုံး၏ ဖြစ်ပေါ်ခြင်း ရှိသည်ဟူ၍
Ye ye dhammā yesaṃ yesaṃ dhammānaṃ hetū paccayā uppādāya = အကြင် အကြင် သဘောတရားတို့သည် အကြင် အကြင် သဘောတရားတို့ ဖြစ်ပေါ်ရန် အကြောင်း၊ အထောက်အပံ့ ဖြစ်ကြ၏
taṃ taṃ ṭhānanti = ထိုထိုသည် ဖြစ်နိုင်သည့်အရာ ဖြစ်သည်ဟူ၍
Ye ye dhammā yesaṃ yesaṃ dhammānaṃ na hetū na paccayā uppādāya taṃ taṃ aṭṭhānanti = အကြင် အကြင် သဘောတရားတို့သည် အကြင် အကြင် သဘောတရားတို့ ဖြစ်ပေါ်ရန် အကြောင်း မဟုတ်၊ အထောက်အပံ့ မဟုတ်ကြ၊ ထိုထိုသည် မဖြစ်နိုင်သည့်အရာ ဖြစ်သည်ဟူ၍
Yo kāyiko avītikkamo = ကိုယ်ဖြင့် မကျူးလွန်ခြင်း
Yo kāyiko vītikkamo = ကိုယ်ဖြင့် ကျူးလွန်ခြင်း
vācasiko avītikkamo = နှုတ်ဖြင့် မကျူးလွန်ခြင်း
vācasiko vītikkamo = နှုတ်ဖြင့် ကျူးလွန်ခြင်း
kāyikavācasiko avītikkamo = ကိုယ်နှင့် နှုတ်ဖြင့် မကျူးလွန်ခြင်း
kāyikavācasiko vītikkamo = ကိုယ်နှင့် နှုတ်ဖြင့် ကျူးလွန်ခြင်း
Yā sā vācā aṇḍakā kakkasā parakaṭukā parābhisajjanī kodhasāmantā asamādhisaṃvattanikā = ခက်ထန်သော၊ ကြမ်းတမ်းသော၊ သူတစ်ပါးကို နာကျင်စေသော၊ သူတစ်ပါးကို ထိခိုက်စေသော၊ ဒေါသနှင့် နီးစပ်သော၊ သမာဓိ မဖြစ်စေသော စကား ရှိ၏
tathārūpiṃ vācaṃ pahāya = ထိုသို့သော စကားကို ပယ်၍
yā sā vācā neḷā kaṇṇasukhā pemanīyā hadayaṅgamā porī bahujanakantā bahujanamanāpā = အပြစ်ကင်းသော၊ နားဝင်ချိုသော၊ ချစ်ခင်ဖွယ်ကောင်းသော၊ နှလုံးသို့ ရောက်သော၊ ယဉ်ယဉ်ကျေးကျေး ရှိသော၊ လူအများ နှစ်သက်သော၊ လူအများ စိတ်တွေ့သော စကား ရှိ၏
tathārūpiṃ vācaṃ bhāsitā hoti = ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏
Dve paṭisanthārā = ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း နှစ်ပါး
āmisapaṭisanthāro ca = ပစ္စည်းဖြင့် ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်းလည်း
dhammapaṭisanthāro ca = တရားဖြင့် ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်းလည်း
Idhekacco paṭisanthārako hoti āmisapaṭisanthārena vā dhammapaṭisanthārena vā = ဤလောက၌ အချို့သော သူသည် ပစ္စည်းဖြင့်ဖြစ်စေ တရားဖြင့်ဖြစ်စေ ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံသူ ဖြစ်၏
Idhekacco = ဤလောက၌ အချို့သော သူသည်
cakkhunā rūpaṃ disvā = မျက်စိဖြင့် အဆင်းအရောင်ကို မြင်၍
nimittaggāhī hoti anubyañjanaggāhī = အမှတ်အသားကို စွဲယူသူ အသေးစိတ်ကို စွဲယူသူ ဖြစ်၏
na nimittaggāhī hoti na anubyañjanaggāhī = အမှတ်အသားကို စွဲယူသူ မဟုတ်၊ အသေးစိတ်ကို စွဲယူသူ မဟုတ်
na nimittaggāhī hoti nānubyañjanaggāhī = အမှတ်အသားကို စွဲယူသူ မဟုတ်၊ အသေးစိတ်ကို စွဲယူသူ မဟုတ်
Sotena saddaṃ sutvā = နားဖြင့် အသံကို ကြား၍
ghānena gandhaṃ ghāyitvā = နှာခေါင်းဖြင့် အနံ့ကို နမ်း၍
jivhāya rasaṃ sāyitvā = လျှာဖြင့် အရသာကို လျက်၍
kāyena phoṭṭhabbaṃ phusitvā = ကိုယ်ဖြင့် အထိအတွေ့ကို ထိ၍
manasā dhammaṃ viññāya = မနောဖြင့် သဘောတရားကို သိ၍
tassa saṃvarāya na paṭipajjati = ထိုစွမ်းရည်ကို စောင့်စည်းရန် မကျင့်ကြံ
tassa saṃvarāya paṭipajjati = ထိုစွမ်းရည်ကို စောင့်စည်းရန် ကျင့်ကြံ၏
Yatvādhikaraṇamenaṃ cakkhundriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ = အကြင် အကြောင်းကြောင့် မျက်စိ၏ စွမ်းရည်ကို မစောင့်စည်းဘဲ နေသော ထိုသူ့ထံသို့ သူ့ဥစ္စာကို လိုချင်ခြင်း၊ စိတ်ဆင်းရဲခြင်း ဟူသော ယုတ်မာသော အကုသိုလ် သဘောတရားများ စီးဝင်လာနိုင်သည်
na rakkhati cakkhundriyaṃ = မျက်စိ၏ စွမ်းရည်ကို မစောင့်ရှောက်
rakkhati cakkhundriyaṃ = မျက်စိ၏ စွမ်းရည်ကို စောင့်ရှောက်၏
cakkhundriye na saṃvaraṃ āpajjati = မျက်စိ၏ စွမ်းရည်၌ စောင့်စည်းမှု မပြု
cakkhundriye saṃvaraṃ āpajjati = မျက်စိ၏ စွမ်းရည်၌ စောင့်စည်းမှု ပြု၏
Yatvādhikaraṇamenaṃ manindriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ = အကြင် အကြောင်းကြောင့် မနော၏ စွမ်းရည်ကို မစောင့်စည်းဘဲ နေသော ထိုသူ့ထံသို့ သူ့ဥစ္စာကို လိုချင်ခြင်း၊ စိတ်ဆင်းရဲခြင်း ဟူသော ယုတ်မာသော အကုသိုလ် သဘောတရားများ စီးဝင်လာနိုင်သည်
na rakkhati manindriyaṃ = မနော၏ စွမ်းရည်ကို မစောင့်ရှောက်
rakkhati manindriyaṃ = မနော၏ စွမ်းရည်ကို စောင့်ရှောက်၏
manindriye na saṃvaraṃ āpajjati = မနော၏ စွမ်းရည်၌ စောင့်စည်းမှု မပြု
manindriye saṃvaraṃ āpajjati = မနော၏ စွမ်းရည်၌ စောင့်စည်းမှု ပြု၏
Idhekacco appaṭisaṅkhā ayoniso āhāraṃ āhāreti davāya madāya maṇḍanāya vibhūsanāya = ဤလောက၌ အချို့သော သူသည် ပြန်လည် မဆင်ခြင်ဘဲ မသင့်လျော်စွာ ကစားရန် မာန်ယစ်ရန် အလှပြင်ရန် တန်ဆာဆင်ရန် အစာကို စားသုံး၏
Idhekacco paṭisaṅkhā yoniso āhāraṃ āhāreti = ဤလောက၌ အချို့သော သူသည် ပြန်လည် ဆင်ခြင်၍ သင့်လျော်စွာ အစာကို စားသုံး၏
neva davāya na madāya na maṇḍanāya na vibhūsanāya yāvadeva imassa kāyassa ṭhitiyā yāpanāya vihiṃsūparatiyā brahmacariyānuggahāya = ကစားရန် မဟုတ်၊ မာန်ယစ်ရန် မဟုတ်၊ အလှပြင်ရန် မဟုတ်၊ တန်ဆာဆင်ရန် မဟုတ်၊ ဤကိုယ်ခန္ဓာ တည်တံ့ရန်၊ ဆက်လက် ရှင်သန်ရန်၊ ညှဉ်းပန်းမှု ငြိမ်းရန်၊ မြင့်မြတ်သော အကျင့်ကို ထောက်ပံ့ရန်သာ ဖြစ်၏
iti purāṇañca vedanaṃ paṭihaṅkhāmi = ဤသို့ ဟောင်းသော ခံစားမှုကိုလည်း ပယ်ဖျောက်မည်
navañca vedanaṃ na uppādessāmi = သစ်သော ခံစားမှုကိုလည်း မဖြစ်ပေါ်စေမည်
yātrā ca me bhavissati anavajjatā ca phāsuvihāro cāti = ငါ၏ အသက်မွေးမှုလည်း ဖြစ်လိမ့်မည်၊ အပြစ် မရှိမှုလည်း၊ ချမ်းသာစွာ နေထိုင်မှုလည်း ဖြစ်လိမ့်မည်ဟူ၍
kammassakatañāṇaṃ = ကံသာ မိမိ၏ ဥစ္စာ ဖြစ်ကြောင်း သိသော ဉာဏ်
saccānulomikañāṇaṃ = သစ္စာနှင့် လျော်ညီသော ဉာဏ်
maggasamaṅgissa ñāṇaṃ = မဂ်နှင့် ပြည့်စုံသူ၏ ဉာဏ်
phalasamaṅgissa ñāṇaṃ = ဖိုလ်နှင့် ပြည့်စုံသူ၏ ဉာဏ်
jātibhayaṃ = မွေးဖွားခြင်း ဘေး
jarābhayaṃ = အိုခြင်း ဘေး
byādhibhayaṃ = နာခြင်း ဘေး
maraṇabhayaṃ = သေခြင်း ဘေး
jāti = မွေးဖွားခြင်း
jarā = အိုခြင်း
byādhi = နာခြင်း
maraṇaṃ = သေခြင်း
Diṭṭhivisuddhi kho panāti = ထို့ပြင် အယူ စင်ကြယ်ခြင်း ဟူသည်
Yathādiṭṭhissa ca padhānanti = အယူနှင့် လျော်ညီသူ၏ ကြိုးပမ်းအားထုတ်ခြင်း ဟူသည်
Saṃvegoti = သံဝေဂ ဟူသည်
Saṃvejaniyaṃ = သံဝေဂ ရဖွယ်
ṭhānanti = အခြေအနေ ဟူသည်
Saṃviggassa ca yoniso padhānanti = သံဝေဂ ရသူ၏ သင့်လျော်စွာ ကြိုးပမ်းအားထုတ်ခြင်း ဟူသည်
Asantuṭṭhitā ca kusalesu dhammesūti = ကုသိုလ် သဘောတရားတို့၌ ရောင့်ရဲမှု မရှိခြင်း ဟူသည်
Appaṭivānitā ca padhānasminti = ကြိုးပမ်းအားထုတ်ခြင်း၌ နောက်မဆုတ်ခြင်း ဟူသည်
Vijjāti = အမှန်သိမြင်မှု ဟူသည်
Vimuttīti = လွတ်မြောက်မှု ဟူသည်
Khaye ñāṇanti = ကုန်ခန်းခြင်းကို သိသော ဉာဏ် ဟူသည်
Anuppāde ñāṇanti = နောက်ထပ် မဖြစ်ပေါ်ခြင်းကို သိသော ဉာဏ် ဟူသည်
idha bhikkhu = ဤသာသနာ၌ ရဟန်းသည်
anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya = မဖြစ်ပေါ်သေးသော ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ မဖြစ်ပေါ်စေရန်
chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati = ဆန္ဒကို ဖြစ်စေ၏၊ အားထုတ်၏၊ ဝီရိယကို စတင်၏၊ စိတ်ကို မြှင့်တင်၏၊ ကြိုးပမ်း၏
uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya = ဖြစ်ပေါ်ပြီးသော ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ပယ်ရန်
anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya = မဖြစ်ပေါ်သေးသော ကုသိုလ် သဘောတရားတို့ ဖြစ်ပေါ်စေရန်
uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā = ဖြစ်ပေါ်ပြီးသော ကုသိုလ် သဘောတရားတို့ တည်တံ့ရန်၊ မပျောက်ပျက်ရန်၊ ပိုမို တိုးပွားရန်၊ ပြန့်ပြောရန်၊ ပွားများခြင်းဖြင့် ပြည့်စုံရန်
tisso vijjā = အမှန်သိမြင်မှု သုံးပါး
pubbenivāsānussati ñāṇaṃ vijjā = ရှေးဘဝများကို အောက်မေ့နိုင်သော ဉာဏ်သည် အမှန်သိမြင်မှု ဖြစ်သည်
sattānaṃ cutūpapāte ñāṇaṃ vijjā = သတ္တဝါတို့၏ သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်းကို သိသော ဉာဏ်သည် အမှန်သိမြင်မှု ဖြစ်သည်
āsavānaṃ khaye ñāṇaṃ vijjā = စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းကို သိသော ဉာဏ်သည် အမှန်သိမြင်မှု ဖြစ်သည်
dve vimuttiyo = လွတ်မြောက်မှု နှစ်ပါး
cittassa = စိတ်၏
adhimutti = အလွန် လွတ်မြောက်မှု
nibbānañca = နိဗ္ဗာန်လည်း
Yeva te dhammā sappaccayā = အကြင် သဘောတရားများသည် အကြောင်း ရှိကြသည်
teva te dhammā saṅkhatā = ထိုသဘောတရားများသည်ပင် ပြုပြင်ဖန်တီးထားကြသည်
Yo eva so dhammo appaccayo = အကြင် သဘောတရားသည် အကြောင်း မရှိ
so eva so dhammo asaṅkhato = ထိုသဘောတရားသည်ပင် ပြုပြင်ဖန်တီးထားခြင်း မရှိ

### Definienda (Tattha katamo X / vuccati X; cluster members)

kāmāsavo = ကာမ စိတ်အစွန်းအထင်း
bhavāsavo = ဘဝ စိတ်အစွန်းအထင်း
diṭṭhāsavo = အယူ စိတ်အစွန်းအထင်း
avijjāsavo = အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း
kāmarāgasaṃyojanaṃ = ကာမ ရာဂ နှောင်ကြိုး
paṭighasaṃyojanaṃ = စိတ်ထိခိုက်ခြင်း နှောင်ကြိုး
mānasaṃyojanaṃ = မာန နှောင်ကြိုး
diṭṭhisaṃyojanaṃ = အယူ နှောင်ကြိုး
vicikicchāsaṃyojanaṃ = ယုံမှားမှု နှောင်ကြိုး
sīlabbataparāmāsasaṃyojanaṃ = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု နှောင်ကြိုး
bhavarāgasaṃyojanaṃ = ဘဝ ရာဂ နှောင်ကြိုး
issāsaṃyojanaṃ = ငြူစူမှု နှောင်ကြိုး
macchariyasaṃyojanaṃ = ဝန်တိုမှု နှောင်ကြိုး
avijjāsaṃyojanaṃ = အမှန်ကို မသိမှု နှောင်ကြိုး
abhijjhā kāyagantho = သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် အထုံး
byāpādo kāyagantho = ဖျက်ဆီးလိုစိတ်ဟူသော ကိုယ် အထုံး
sīlabbataparāmāso kāyagantho = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် အထုံး
idaṃsaccābhiniveso kāyagantho = ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် အထုံး
abhijjhākāyagantho = သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် အထုံး
idaṃ saccābhiniveso kāyagantho = ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် အထုံး
lobho = လောဘ
doso = ဒေါသ
moho = မောဟ
kāmacchandanīvaraṇaṃ = ကာမကို လိုလားမှု အတားအဆီး
byāpādanīvaraṇaṃ = ဖျက်ဆီးလိုစိတ် အတားအဆီး
thinamiddhanīvaraṇaṃ = ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု အတားအဆီး
uddhaccakukkuccanīvaraṇaṃ = ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု အတားအဆီး
uddhaccanīvaraṇaṃ = ယောက်ယက်ခတ်မှု အတားအဆီး
kukkuccanīvaraṇaṃ = နောင်တ ပူပန်မှု အတားအဆီး
vicikicchānīvaraṇaṃ = ယုံမှားမှု အတားအဆီး
avijjānīvaraṇaṃ = အမှန်ကို မသိမှု အတားအဆီး
diṭṭhiparāmāso = အယူဆိုင်ရာ မှားယွင်းသော ယူဆမှု
kāmupādānaṃ = ကာမ စွဲလမ်းမှု
diṭṭhupādānaṃ = အယူ စွဲလမ်းမှု
sīlabbatupādānaṃ = သီလ အကျင့်ဝတ် စွဲလမ်းမှု
attavādupādānaṃ = အတ္တဟူသော ဝါဒ စွဲလမ်းမှု
thinaṃ = ထိုင်းမှိုင်းမှု
middhaṃ = ငိုက်မျဉ်းမှု
uddhaccaṃ = ယောက်ယက်ခတ်မှု
kukkuccaṃ = နောင်တ ပူပန်မှု
māno = မာန
diṭṭhi = အယူ
vicikicchā = ယုံမှားမှု
ahirikaṃ = ဒုစရိုက်ကို မရှက်မှု
anottappaṃ = ဒုစရိုက်ကို မကြောက်ရွံ့မှု

### Mātikā combinations used in questions and closers

āsavavippayuttā sāsavā = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာ၍ စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော
āsavavippayuttā anāsavā = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာ၍ စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော
saṃyojanavippayuttā saṃyojaniyā = နှောင်ကြိုးနှင့် ကင်းကွာ၍ နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော
saṃyojanavippayuttā asaṃyojaniyā = နှောင်ကြိုးနှင့် ကင်းကွာ၍ နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော
ganthavippayuttā ganthaniyā = အထုံးနှင့် ကင်းကွာ၍ အထုံး၏ အာရုံ ဖြစ်နိုင်သော
ganthavippayuttā aganthaniyā = အထုံးနှင့် ကင်းကွာ၍ အထုံး၏ အာရုံ မဖြစ်နိုင်သော
oghavippayuttā oghaniyā = ရေအလျဉ်နှင့် ကင်းကွာ၍ ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော
oghavippayuttā anoghaniyā = ရေအလျဉ်နှင့် ကင်းကွာ၍ ရေအလျဉ်၏ အာရုံ မဖြစ်နိုင်သော
yogavippayuttā yoganiyā = ထမ်းပိုးနှင့် ကင်းကွာ၍ ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော
yogavippayuttā ayoganiyā = ထမ်းပိုးနှင့် ကင်းကွာ၍ ထမ်းပိုး၏ အာရုံ မဖြစ်နိုင်သော
nīvaraṇavippayuttā nīvaraṇiyā = အတားအဆီးနှင့် ကင်းကွာ၍ အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော
nīvaraṇavippayuttā anīvaraṇiyā = အတားအဆီးနှင့် ကင်းကွာ၍ အတားအဆီး၏ အာရုံ မဖြစ်နိုင်သော
parāmāsavippayuttā parāmaṭṭhā = မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာ၍ မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော
parāmāsavippayuttā aparāmaṭṭhā = မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာ၍ မှားယွင်းသော ယူဆမှု၏ အာရုံ မဖြစ်နိုင်သော
upādānavippayuttā upādāniyā = စွဲလမ်းမှုနှင့် ကင်းကွာ၍ စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော
upādānavippayuttā anupādāniyā = စွဲလမ်းမှုနှင့် ကင်းကွာ၍ စွဲလမ်းမှု၏ အာရုံ မဖြစ်နိုင်သော
kilesavippayuttā saṃkilesikā = ကိလေသာနှင့် ကင်းကွာ၍ ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော
kilesavippayuttā asaṃkilesikā = ကိလေသာနှင့် ကင်းကွာ၍ ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော
na hetū sahetukā = အမြစ် မဟုတ်ဘဲ အမြစ် ရှိသော
na hetū ahetukā = အမြစ် မဟုတ်ဘဲ အမြစ် မရှိသော
kenaci viññeyyā, kenaci na viññeyyā = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော၊ တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော
kenaci viññeyyā kenaci na viññeyyā = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်၍ တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော
neva ācayagāmi na apacayagāmino = စုပုံခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်သော
dassanena pahātabbahetū = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ်များ
bhāvanāya pahātabbahetū = ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ်များ
maggahetū = မဂ်၏ အမြစ်များ

### List heads (GEN)

evarūpā = ဤသို့ သဘောရှိသော
evarūpo = ဤသို့ သဘောရှိသော
evarūpaṃ = ဤသို့ သဘောရှိသော
evarūpo cittassa = ဤသို့ သဘောရှိသော စိတ်၏
kāmesu = ကာမတို့၌ ရှိသော
bhavesu = ဘဝတို့၌ ရှိသော
paralābhasakkāragarukāramānanavandanapūjanāsu = သူတစ်ပါး၏ လာဘ်၊ အရိုအသေ ပြုခံရမှု၊ လေးစားခံရမှု၊ ချီးမြှောက်ခံရမှု၊ ရှိခိုးခံရမှု၊ ပူဇော်ခံရမှုတို့၌ ဖြစ်သော
cittassa = စိတ်၏
kāyassa = စိတ်၏ အဖော်တို့၏
tesaṃ tesaṃ dhammānaṃ = ထိုထို သဘောတရားတို့၏
uppajjati = ဖြစ်ပေါ်သော
tesaṃ = ထိုသူတို့ကို
tāsaṃ āpattīnaṃ = ထိုအပြစ်တို့၌
tāhi āpattīhi = ထိုအပြစ်တို့မှ
tāsaṃ samāpattīnaṃ = ထိုဈာန် ဝင်စားမှုတို့၌
tāhi samāpattīhi = ထိုဈာန် ဝင်စားမှုတို့မှ
tāsaṃ dhātūnaṃ = ထိုဓာတ်တို့၌
tesaṃ āyatanānaṃ = ထိုအာရုံခံ နယ်ပယ်တို့၌
tattha = ထို၌ ရှိသော
kusalānaṃ dhammānaṃ = ကုသိုလ် သဘောတရားတို့ကို
kusalānaṃ dhammānaṃ bhāvanāya = ကုသိုလ် သဘောတရားတို့ကို ပွားများရာ၌
kusalānaṃ dhammānaṃ bhāvanāya asantuṭṭhassa = ကုသိုလ် သဘောတရားတို့ကို ပွားများရာ၌ မရောင့်ရဲသူ၏
imesaṃ channaṃ indriyānaṃ = ဤ အာရုံခံ အင်္ဂါ ခြောက်ပါးတို့၏
tesaṃ tesaṃ sattānaṃ = ထိုထို သတ္တဝါတို့၏
tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ = ထိုထို အခြား သတ္တဝါ၊ အခြား ပုဂ္ဂိုလ်တို့၏

### Headings and colophons

Nikkhepakaṇḍaṃ = အကျဉ်း ဖော်ပြချက် အခန်း
Tikanikkhepaṃ = သုံးမျိုးတွဲ အကျဉ်း ဖော်ပြချက်
Dukanikkhepaṃ = နှစ်မျိုးတွဲ အကျဉ်း ဖော်ပြချက်
Suttantikadukanikkhepaṃ = သုတ္တန် နှစ်မျိုးတွဲ အကျဉ်း ဖော်ပြချက်
Tikaṃ = သုံးမျိုးတွဲ
Abhidhammadukaṃ = အဘိဓမ္မာ နှစ်မျိုးတွဲ
Nikkhepakaṇḍe paṭhamabhāṇavāro = အကျဉ်း ဖော်ပြချက် အခန်း၌ ပထမ ရွတ်ဖတ်ရန် အပိုင်း
Nikkhepakaṇḍe dutiyabhāṇavāro = အကျဉ်း ဖော်ပြချက် အခန်း၌ ဒုတိယ ရွတ်ဖတ်ရန် အပိုင်း
Nikkhepakaṇḍaṃ niṭṭhitaṃ = “အကျဉ်း ဖော်ပြချက် အခန်း” ပြီးဆုံးပြီ

### Variant readings

diṭṭhivisūkāyitaṃ = ပါဌ်ကွဲ
nandirāgo = စာလုံးပေါင်းကွဲ
sibbanī = စာလုံးပေါင်းကွဲ
āyūhanī = စာလုံးပေါင်းကွဲ
āsiṃsanā āsiṃsitattaṃ = စာလုံးပေါင်းကွဲ
bhavacchando = စာလုံးပေါင်းကွဲ
uṇṇati uṇṇāmo = စာလုံးပေါင်းကွဲ
ussuyā ussuyanā ussuyitattaṃ = စာလုံးပေါင်းကွဲ
uparimaṃ = ပါဌ်ကွဲ
rūpā = ပါဌ်ကွဲ
nīvaraṇāni = ပါဌ်ကွဲ
kāmūpādānaṃ diṭṭhūpādānaṃ sīlabbatūpādānaṃ attavādūpādānaṃ = စာလုံးပေါင်းကွဲ
samaggatā = ပါဌ်ကွဲ
paranimmitavasavattideve = စာလုံးပေါင်းကွဲ
akaniṭṭhadeve = စာလုံးပေါင်းကွဲ
diṭṭhadhammasukhavihārassa = ပါဌ်ကွဲ
upādāya = ပါဌ်ကွဲ
saṃvejanīyaṃ = စာလုံးပေါင်းကွဲ
cittassa ca = ပါဌ်ကွဲ
[puñcikatā (syā.) pucchikatā (sī.)] = [စာလုံးပေါင်းကွဲ (Syā.): puñcikatā၊ (Sī.): pucchikatā]
