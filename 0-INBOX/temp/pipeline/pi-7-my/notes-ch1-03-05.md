# pi-7 (Paṭṭhāna) Burmese zero-shot: 1-03 vipākattika, 1-04 upādinnattika, 1-05 saṅkiliṭṭhattika — notes

Files: `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/` 1-03-vipakattika.md, 1-04-upadinnattika.md,
1-05-sankilitthattika.md. Translated from the Pāli only (no Burmese translation or nissaya opened, no web search,
`language-priority/` not opened). Meaning cross-checked only against the Marathi frame inventory (pi-7-mr notes).
Generator: `make_ch1-03-05.py` (imports `my7_formulas.py` and the sample's tables from `make_sample.py`; neither is
edited, nothing of the sample is written). Check: `check_ch1-03-05.py` (adapted from check_sample.py + chk_mutate.py).

## Status (all pass, 2026-11-23)
| file | segments | lines | check_chapter_ids | check_text_pe7 | check_marks | check_ch1-03-05 |
|---|---|---|---|---|---|---|
| 1-03-vipakattika.md | 283 | 544 | OK | OK | OK | OK |
| 1-04-upadinnattika.md | 219 | 485 | OK | OK | OK | OK |
| 1-05-sankilitthattika.md | 91 | 184 | OK | OK | OK | OK |

check_ch1-03-05 (`--pe --sample --mutate`): 1213 lines × (structure, polarity, conditions, term order, numbers), 2221
sentences for identity (with the approved sample on disk), 62 table values: **0 mismatches**. Reuse test: **101 / 101**
pi-1 … pi-6 values identical wherever their Pāli occurs; sentences also in pi-1 … pi-6: **567 / 567** identical.
Sample identity: 1-00 and 1-02 regenerated in memory with all of this script's extensions = the files on disk
(raw and with prep()). Mutation test: 8 / 8 planted errors caught (count, polarity, term order, condition, khandha
count, term, digits, note). No existing value of my7_formulas / make_sample was changed (only additions).

## Triad terms (pi-1 Mātikā ^1-M1-3/4/5, read from the FINAL rails by W())
- vipāka = ကံ၏ အကျိုး ဖြစ်သော; vipākadhammadhamma = အကျိုး ပေးတတ်သော;
  nevavipākanavipākadhammadhamma = ကံ၏ အကျိုးလည်း မဟုတ်၊ အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော
- upādinnupādāniya = ကံကြောင့် ဖြစ်၍ စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော; anupādinnupādāniya = ကံကြောင့် မဖြစ်သော်လည်း
  စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော; anupādinnaanupādāniya = ကံကြောင့်လည်း မဖြစ်၊ စွဲလမ်းမှု၏ အာရုံလည်း မဖြစ်နိုင်သော
  (pi-7 spells -dinn-, pi-1 -diṇṇ-: same Burmese)
- saṃkiliṭṭhasaṃkilesika = ကိလေသာဖြင့် ညစ်နွမ်း၍ ကိလေသာ၏ အာရုံလည်း ဖြစ်နိုင်သော; asaṃkiliṭṭhasaṃkilesika = ကိလေသာဖြင့်
  မညစ်နွမ်းသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော; asaṃkiliṭṭhaasaṃkilesika = ကိလေသာဖြင့်လည်း မညစ်နွမ်း၊ ကိလေသာ၏ အာရုံလည်း
  မဖြစ်နိုင်သော
- Chapter names: Vipākattikaṃ = ကံ၏ အကျိုး သုံးမျိုးတွဲ (pi-2); Upādinnattikaṃ = ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ (pi-2);
  Saṃkiliṭṭhattikaṃ = ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ (NEW, built like the pi-2 upādinna name).
- «vipākadhammadhammo» standing alone contains its noun (pi-1 «အကျိုး ပေးတတ်သော သဘောတရားများ»): prep() splits it in
  memory into «vipākadhamma dhammo» when no noun follows, so it renders «အကျိုး ပေးတတ်သော သဘောတရား»; before a noun
  («vipākadhammadhamme khandhe») it stays a qualifier. «vipākādhipati» = «vipāko adhipati» (term + noun, the same
  string as the sample's lex tail). Two terms of different triads on one noun («vipākānaṃ sukhāya vedanāya
  sampayuttānaṃ khandhānaṃ», «vipāko asaṃkiliṭṭhasaṃkilesiko eko khandho») are stacked, no «နှင့်».
- «kammaṃ vipākassa» = «ကံသည် ကံ၏ အကျိုးအား» (the noun vipāka, not the triad term).

## Engine extensions (in memory, in make_ch1-03-05.py; all logged here)
- prep(): the split above; «khandhañca vatthuñca» = «khandhaṃ ca vatthuṃ ca» (13 nouns, list NCA); «X-assa ca Y-assa
  ca» before a condition gets the frame's noun «dhammassa»; «tayo khandhā vatthu ca» / «khandhānaṃ vatthussa ca» read
  as «A ca B ca»; «[purejātassa] [imassa] [terms] kāyassa» and «[terms] kabaḷīkāro āhāro» become one NP token
  («ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော T1၊ T2 ဤကိုယ်», «T လုတ်ပြု၍ စားရသော အာဟာရ»); «Sahajātā –» outside the kamma section
  (no cetanā follows) is the kind label «အတူ ပေါ်ပေါက်ခြင်း» (the sample's «အတူ ပေါ်ပေါက်သည့် ကံ» kept for the
  kamma section).
- Wrappers: np_parse (asyndetic lists of multi-word fixed NPs; a bare term = term + သဘောတရား), np_my (stacked terms;
  the NP tokens), _case_of (trailing «ca»), pairs (a coordinated first member takes the link's case inside each
  member, as pi-2 ^2-184: «…ကိုလည်းကောင်း၊ …ကိုလည်းကောင်း မှီ၍», «…ကြောင့်လည်းကောင်း၊ …»), panha (+ verbless
  pairs, pairs without their second member, NP-only fragments, «NP-nom NP-dat» without the condition, kinds lists
  «sahajātaṃ, purejātaṃ…»), unit_my (the «(Yathā kusalattike X Vpp, evaṃ Y)» instructions built from parts; «(X-vāropi
  Y-vāropi sadiso / vitthāretabbo)»; «(n) …» and «… .) …» on one line split; a missing dash before «ahetukaṃ»).
- Counts above ten: ekādasa ဆယ့်တစ် … catuvīsati နှစ်ဆယ့်လေး (pi-1 … pi-3 forms «ဆယ့်နှစ်ပါး» etc.) + «ခု»; bāvīsati /
  tevīsa (short forms) = 22 / 23. Counting groups «Ekādasakaṃ» = ဆယ့်တစ်မျိုးတွဲ.

## Recurring renderings worth a look in the consistency pass
- tadārammaṇatā uppajjati = «စိတ်သည် ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့် ဖြစ်ပေါ်သည်» (the bare «vipāko» before it
  gets «စိတ်», as the sample's kiriyaṃ «ပြုရုံမျှသာ ဖြစ်သော စိတ်»); kusalākusale niruddhe = «ကုသိုလ်နှင့် အကုသိုလ်
  ချုပ်ငြိမ်းသွားသောအခါ».
- Kinds of a condition (atthi / vippayutta / purejāta sections): sahajātaṃ, purejātaṃ, pacchājātaṃ, āhāraṃ, indriyaṃ
  and the labels Sahajāto / Sahajātā / Pacchājātā = the bare names N; ārammaṇapurejātaṃ = «အာရုံ ရှေးဦးစွာ
  ဖြစ်ပေါ်ခြင်း», vatthupurejātaṃ = «မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း» (pattern of the sample's «အာရုံ အကြီးအမှူး»).
- sekkhā ကျင့်ကြံဆဲသူ (pi-4), puthujjanā ပုထုဇဉ် (pi-6), arahā ရဟန္တာ; «sekkhā vā puthujjanā vā» = «ကျင့်ကြံဆဲသူတို့ဖြစ်စေ၊
  ပုထုဇဉ်တို့ဖြစ်စေ»; X-kusalaṃ / -kiriyaṃ / -vipākassa of the formless bases = «<base>နှင့် ဆိုင်သော ကုသိုလ် / ပြုရုံမျှသာ
  ဖြစ်သော စိတ် / ကံ၏ အကျိုး ဖြစ်သော စိတ်»; parikamma «ကြိုတင် ပြင်ဆင်မှု»; ordinals ပထမ ဒုတိယ တတိယ စတုတ္ထ.
- (Xsadisaṃ) = «(Nနှင့် တူသည်)», (Xpaccayasadisaṃ) = «(Nဟူသော အကြောင်းနှင့် တူသည်)» for every stem (sample pattern);
  nānākaraṇaṃ «ကွဲပြားချက်» vs nānattaṃ «ကွဲပြားခြင်း» (two Pāli words, two Burmese).
- avipākaṃ / savipākaṃ (ghaṭanā groups) = «ကံ၏ အကျိုးဟူသော အကြောင်း မပါဝင်သော / ပါဝင်သော» (sample PAREN pattern).

## Unsure Pāli
- «khandhe paṭicca vatthu, vatthuṃ khandhā» (1-04): the second pair leaves out paṭicca; rendered with «မှီ၍» supplied
  («မှီရာ ဝတ္ထုကို မှီ၍ အစုအဝေးများ»).
- «Vipākañca nevavipākanavipākadhammadhammañca… tīṇi» / «vipāko ca ubhayañca… tīṇi» (1-03 ^7-4-72): elliptic;
  «… သဘောတရားနှင့် … သဘောတရား… သုံးခု», «… သဘောတရားလည်းကောင်း၊ နှစ်မျိုးလုံးလည်းကောင်း… သုံးခု».
- «Upādinnupādāniyañca …dhammaṃ paṭicca upādinnupādāniyo…pe…»: a bare term = term + «သဘောတရား» (noun supplied).
- «(paṭisandhipi imesaṃ tiṇṇannaṃ kātabbā)» = «(ဤ သုံးခုတို့၌ ပဋိသန္ဓေကိုလည်း ထည့်ရမည်။)» (the three answers).
- «Kusalattikassa gaṇanato upādinnattike gaṇanā gambhīrā sukhumatarā ca, evaṃ kātūna …» = «… ရေတွက်ချက်ထက် … ရေတွက်ချက်သည်
  နက်နဲ၍ ပို၍ သိမ်မွေ့သည်၊ ဤသို့ ပြု၍ …»; «asammohantena eso sajjhāyamaggo» = «ဤသည်မှာ မရောထွေးစေဘဲ သရဇ္ဈာယ်သည့်
  နည်းလမ်း ဖြစ်သည်» (asammohantena = the sample's asammuyhantena «မရောထွေးစေဘဲ»).
- «rūpāyatanaṃ cakkhuviññāṇassa purejāta…pe…» (cut short): «… ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း…».
- «tassa paṭighātatthāya» «ထိုအမှုကို ချေဖျက်ရန်»; «pubbe suciṇṇāni» «ရှေးက ကောင်းစွာ ပြုခဲ့ဖူးသည်တို့».

## Source slips (translated as written; normalised only where a frame needs it; logged by the generator)
- 1-03 «nevavipākanavipākadhamma-dhammo» (hyphen), «sappayuttakānaṃ», «paṭisandhikhaṇe», «vippassanti»,
  «vitthāratabbaṃ»: read as the usual forms. «uppajjati nahetupaccayā ahetukaṃ …» (^7-4-55): no dash in the source,
  none added (two parts joined by a space). «diṭṭhi uppajjati,.» kept («ဖြစ်ပေါ်သည်၊။»). «assādenti abhinandati»
  (plural + singular) kept: «သာယာကြ၍ နှစ်သက်သည်».
- 1-04 «tayokhandhā» (one word), «pakatūnissayo»: read as «tayo khandhā», «pakatūpanissayo». «tiṇṇannaṃ khandhānaṃ
  purejātassa imassa X ca kāyassa»: the «ca» read as joining the khandhas and the body («…လည်းကောင်း၊ …ဤကိုယ်အားလည်းကောင်း»).
- 1-03 / 1-04 / 1-05 «na adhipatiyā tīṇi», «na adhipatipaccayā», «na sampayutte cha» written apart: read as «naX».
- 1-05 «asaṅkiliṭṭhasaṃkilisikassa» = asaṃkiliṭṭhasaṃkilesikassa (same Burmese); «paccayo =19 …pe…» a stray «=19», kept
  as «=19»; ghaṭanā hyphens missing «nissayaatthi», «aññamaññanissaya», «vipākasampayutta» (segmented by stem).

## For the coordinator
1. Kind labels: the sample's LEX «sahajātā» = «အတူ ပေါ်ပေါက်သည့် ကံ» fits only the kamma section; elsewhere the label
   is rendered as the bare name «အတူ ပေါ်ပေါက်ခြင်း» (prep marker SahajātāKIND). A shared module value for the kinds
   would settle it for 1-01 as well.
2. The 1-01 agent builds the same pañhāvāra lexicon at the same time; the strings above (LEX entries) should be aligned
   with 1-01's in the consistency pass.
3. A plural asyndetic list in a pair keeps the module's «…များ» at its end («… ရုပ်၊ … ရုပ်များ»), as the module does.

## New strings of this script («Pāli = Burmese», table in brackets; generated stems: (Xsadisaṃ) / (Xpaccayasadisaṃ) /
## (naXpaccayasadisaṃ) for all 24 stems, the ordinals paṭhama … catuttha × jhāna / magga / parikamma, and the four
## formless bases × kusala / kiriya / vipāka follow the first entry of each pattern)
- vatthu = မှီရာ ဝတ္ထု  [NOUN]
- vatthussa = မှီရာ ဝတ္ထု  [NOUN]
- mahābhūtaṃ = မူလဓာတ်ကြီး  [NOUN]
- mahābhūte = မူလဓာတ်ကြီး  [NOUN]
- mahābhūtānaṃ = မူလဓာတ်ကြီး  [NOUN]
- kammaṃ = ကံ  [NOUN]
- vipākassa = ကံ၏ အကျိုး  [NOUN]
- adhipati = အကြီးအမှူး  [NOUN]
- āvajjanā = စိတ်ညွတ်ခြင်း  [NOUN]
- viññāṇānaṃ = သိစိတ်  [NOUN]
- āhārā = အာဟာရ  [NOUN]
- indriyā = စွမ်းရည်  [NOUN]
- jhānaṅgā = ဈာန်၏ အင်္ဂါ  [NOUN]
- maggaṅgā = မဂ်၏ အင်္ဂါ  [NOUN]
- mahābhūtassa = မူလဓာတ်ကြီး  [NOUN]
- cittasamuṭṭhānaṃ = စိတ်မှ ဖြစ်ပေါ်လာသော  [QUAL]
- ahetuke = အမြစ် မရှိသော  [QUAL]
- ahetukā = အမြစ် မရှိသော  [QUAL]
- pañcaviññāṇasahagataṃ = သိစိတ် ငါးပါးနှင့်အတူ ဖြစ်သော  [QUAL]
- cakkhuviññāṇasahagataṃ = မျက်စိ သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- cakkhuviññāṇasahagato = မျက်စိ သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- cakkhuviññāṇasahagatānaṃ = မျက်စိ သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- sotaviññāṇasahagataṃ = နား သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- sotaviññāṇasahagato = နား သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- sotaviññāṇasahagatānaṃ = နား သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- ghānaviññāṇasahagataṃ = နှာခေါင်း သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- ghānaviññāṇasahagato = နှာခေါင်း သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- ghānaviññāṇasahagatānaṃ = နှာခေါင်း သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- jivhāviññāṇasahagataṃ = လျှာ သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- jivhāviññāṇasahagato = လျှာ သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- jivhāviññāṇasahagatānaṃ = လျှာ သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- kāyaviññāṇasahagato = ကိုယ် သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- kāyaviññāṇasahagatānaṃ = ကိုယ် သိစိတ်နှင့်အတူ ဖြစ်သော  [QUAL]
- bāhiraṃ = ပြင်ပ  [QUAL]
- āhārasamuṭṭhānaṃ = အာဟာရမှ ဖြစ်ပေါ်လာသော  [QUAL]
- utusamuṭṭhānaṃ = ရာသီဥတုမှ ဖြစ်ပေါ်လာသော  [QUAL]
- sahajātā = အတူ ပေါ်ပေါက်သည့်  [QUAL]
- nānākkhaṇikā = ခဏ ကွဲပြားသည့်  [QUAL]
- kabaḷīkāro = လုတ်ပြု၍ စားရသော  [QUAL]
- kabaḷīkāro āhāro = လုတ်ပြု၍ စားရသော အာဟာရ  [FIXED]
- cakkhuviññāṇaṃ = မျက်စိ သိစိတ်  [FIXED]
- cakkhuviññāṇassa = မျက်စိ သိစိတ်  [FIXED]
- sotaviññāṇaṃ = နား သိစိတ်  [FIXED]
- sotaviññāṇassa = နား သိစိတ်  [FIXED]
- ghānaviññāṇaṃ = နှာခေါင်း သိစိတ်  [FIXED]
- ghānaviññāṇassa = နှာခေါင်း သိစိတ်  [FIXED]
- jivhāviññāṇaṃ = လျှာ သိစိတ်  [FIXED]
- jivhāviññāṇassa = လျှာ သိစိတ်  [FIXED]
- kāyaviññāṇaṃ = ကိုယ် သိစိတ်  [FIXED]
- kāyaviññāṇassa = ကိုယ် သိစိတ်  [FIXED]
- cittasamuṭṭhānaṃ rūpaṃ = စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်  [FIXED]
- kaṭattārūpaṃ = ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်  [FIXED]
- kaṭattā ca rūpaṃ = ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်  [FIXED]
- upādārūpaṃ = မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်  [FIXED]
- pañcaviññāṇaṃ = သိစိတ် ငါးပါး  [FIXED]
- bhavaṅgaṃ = ဘဝင် စိတ်  [FIXED]
- vipākamanodhātu = ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ်  [FIXED]
- vipākamanoviññāṇadhātu = ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ်  [FIXED]
- vipākamanodhātuyā = ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ်  [FIXED]
- vipākamanoviññāṇadhātuyā = ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ်  [FIXED]
- kiriyamanoviññāṇadhātuyā = ပြုရုံမျှသာ ဖြစ်သော မနော သိစိတ် ဓာတ်  [FIXED]
- bhavaṅgassa = ဘဝင် စိတ်  [FIXED]
- āvajjanāya = စိတ်ညွတ်ခြင်း  [FIXED]
- cittasamuṭṭhānānaṃ rūpānaṃ = စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်  [FIXED]
- tiṇṇannaṃ = သုံးပါး  [FIXED]
- dvinnaṃ = နှစ်ပါး  [FIXED]
- asaññasattānaṃ = အသညသတ်တို့၌  [LEX]
- sekkhā = ကျင့်ကြံဆဲသူ  [LEX]
- arahā = ရဟန္တာ  [LEX]
- puthujjanā = ပုထုဇဉ်  [LEX]
- mahābhūtā = မူလဓာတ်ကြီး  [LEX]
- phalasamāpatti = ဖိုလ်သမာပတ်  [LEX]
- utu = ရာသီဥတု  [LEX]
- pāṇātipāto = သူ့အသက်ကို သတ်ခြင်း  [LEX]
- micchādiṭṭhi = မှားယွင်းသော အယူ  [LEX]
- mātughātikammaṃ = အမိကို သတ်ခြင်း ကံ  [LEX]
- niyatamicchādiṭṭhi = ကျိန်းသေသော မှားယွင်းသော အယူ  [LEX]
- dhammo = သဘောတရား  [LEX]
- dhammā = သဘောတရား  [LEX]
- kusalākusalaṃ kammaṃ = ကုသိုလ်နှင့် အကုသိုလ် ကံ  [LEX]
- paṭhamassa jhānassa parikammaṃ = ပထမ ဈာန်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- paṭhamassa jhānassa = ပထမ ဈာန်  [LEX]
- nevasaññānāsaññāyatanassa parikammaṃ = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- ākāsānañcāyatanakusalaṃ = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်နှင့် ဆိုင်သော ကုသိုလ်  [LEX]
- ākāsānañcāyatanakiriyaṃ = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်နှင့် ဆိုင်သော ပြုရုံမျှသာ ဖြစ်သော စိတ်  [LEX]
- ākāsānañcāyatanakusalassa = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်နှင့် ဆိုင်သော ကုသိုလ်  [LEX]
- ākāsānañcāyatanakiriyassa = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်နှင့် ဆိုင်သော ပြုရုံမျှသာ ဖြစ်သော စိတ်  [LEX]
- ākāsānañcāyatanavipākassa = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်နှင့် ဆိုင်သော ကံ၏ အကျိုး ဖြစ်သော စိတ်  [LEX]
- nibbānaṃ = နိဗ္ဗာန်  [LEX]
- kāyikaṃ sukhaṃ = ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှု  [LEX]
- kāyikaṃ dukkhaṃ = ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု  [LEX]
- bhojanaṃ = အစားအစာ  [LEX]
- senāsanaṃ = အိပ်ရာ နေရာ  [LEX]
- cakkhuṃ = မျက်စိ  [LEX]
- sotaṃ = နား  [LEX]
- ghānaṃ = နှာခေါင်း  [LEX]
- jivhaṃ = လျှာ  [LEX]
- kāyaṃ = ကိုယ်  [LEX]
- rūpe = အဆင်းအရောင်  [LEX]
- sadde = အသံ  [LEX]
- gandhe = အနံ့  [LEX]
- rase = အရသာ  [LEX]
- phoṭṭhabbe = အထိအတွေ့  [LEX]
- saṅkhāre = ပြုပြင်ဖန်တီးမှု  [LEX]
- maggaṃ = မဂ်  [LEX]
- jhānaṃ = ဈာန်  [LEX]
- gotrabhuṃ = အနွယ် ပြောင်းခြင်း စိတ်  [LEX]
- utuṃ = ရာသီဥတု  [LEX]
- pubbe suciṇṇāni = ရှေးက ကောင်းစွာ ပြုခဲ့ဖူးသည်  [LEX]
- anuppannaṃ kiriyasamāpattiṃ = မဖြစ်ပေါ်သေးသော ပြုရုံမျှသာ ဖြစ်သော သမာပတ်  [LEX]
- anuppannaṃ kusalasamāpattiṃ = မဖြစ်ပေါ်သေးသော ကုသိုလ် သမာပတ်  [LEX]
- anuppannaṃ samāpattiṃ = မဖြစ်ပေါ်သေးသော သမာပတ်  [LEX]
- uppannaṃ = ဖြစ်ပေါ်ပြီးသည်  [LEX]
- uppannaṃ samāpattiṃ = ဖြစ်ပေါ်ပြီးသော သမာပတ်  [LEX]
- phalasamāpattiṃ = ဖိုလ်သမာပတ်  [LEX]
- rūpaṃ = အဆင်းအရောင်  [LEX]
- saddaṃ = အသံ  [LEX]
- kāyikassa sukhassa = ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှု  [LEX]
- kāyikassa dukkhassa = ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု  [LEX]
- dhammassa = သဘောတရား  [LEX]
- pāṇātipātassa = သူ့အသက်ကို သတ်ခြင်း  [LEX]
- micchādiṭṭhiyā = မှားယွင်းသော အယူ  [LEX]
- byāpādassa = ဖျက်ဆီးလိုစိတ်  [LEX]
- mātughātikammassa = အမိကို သတ်ခြင်း ကံ  [LEX]
- niyatamicchādiṭṭhiyā = ကျိန်းသေသော မှားယွင်းသော အယူ  [LEX]
- saṅghabhedakakammassa = သံဃာကို သင်းခွဲခြင်း ကံ  [LEX]
- ṭhānāṭhānakosallassa = ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု  [LEX]
- pañcannaṃ viññāṇānaṃ = သိစိတ် ငါးပါး  [LEX]
- atthappaṭisambhidāya = အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်  [LEX]
- dhammappaṭisambhidāya = တရားကို ပိုင်းခြားသိသော ဉာဏ်  [LEX]
- niruttippaṭisambhidāya = စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်  [LEX]
- paṭibhānappaṭisambhidāya = ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်  [LEX]
- sekkhānaṃ = ကျင့်ကြံဆဲသူ  [LEX]
- arahato = ရဟန္တာ  [LEX]
- ariyānaṃ = အရိယာ  [LEX]
- dibbena cakkhunā = နတ်မျက်စိ  [LEX]
- dibbāya sotadhātuyā = နတ်နား ဓာတ်  [LEX]
- vipassanti = ထိုးထွင်း၍ ရှုကြသည်  [LEX]
- assādenti abhinandanti = သာယာ နှစ်သက်ကြသည်  [LEX]
- assādenti abhinandati = သာယာကြ၍ နှစ်သက်သည်  [LEX]
- assādeti = သာယာသည်  [LEX]
- assādenti = သာယာကြသည်  [LEX]
- uppādeti = ဖြစ်စေသည်  [LEX]
- uppādenti = ဖြစ်စေကြသည်  [LEX]
- samāpajjati = ဝင်စားသည်  [LEX]
- samāpajjanti = ဝင်စားကြသည်  [LEX]
- sekkhā vā puthujjanā vā = ကျင့်ကြံဆဲသူတို့ဖြစ်စေ၊ ပုထုဇဉ်တို့ဖြစ်စေ  [LEX]
- rūpaṃ passati = အဆင်းအရောင်ကို မြင်သည်  [LEX]
- rūpaṃ passanti = အဆင်းအရောင်ကို မြင်ကြသည်  [LEX]
- saddaṃ suṇāti = အသံကို ကြားသည်  [LEX]
- saddaṃ suṇanti = အသံကို ကြားကြသည်  [LEX]
- kusalākusale niruddhe = ကုသိုလ်နှင့် အကုသိုလ် ချုပ်ငြိမ်းသွားသောအခါ  [LEX]
- niruddhe = ချုပ်ငြိမ်းသွားသောအခါ  [LEX]
- tadārammaṇatā uppajjati = စိတ်သည် ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့် ဖြစ်ပေါ်သည်  [LEX]
- pāṇaṃ hantvā = သတ္တဝါကို သတ်၍  [LEX]
- tassa paṭighātatthāya = ထိုအမှုကို ချေဖျက်ရန်  [LEX]
- saṅghaṃ bhinditvā = သံဃာကို ဖြိုခွဲ၍  [LEX]
- sahajātaṃ = အတူ ပေါ်ပေါက်ခြင်း  [LEX]
- purejātaṃ = ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း  [LEX]
- pacchājātaṃ = နောက်မှ ဖြစ်ပေါ်ခြင်း  [LEX]
- āhāraṃ = အာဟာရ  [LEX]
- indriyaṃ = စွမ်းရည်  [LEX]
- sahajāto = အတူ ပေါ်ပေါက်ခြင်း  [LEX]
- pacchājātā = နောက်မှ ဖြစ်ပေါ်ခြင်း  [LEX]
- sahajātākind = အတူ ပေါ်ပေါက်ခြင်း  [LEX]
- ārammaṇapurejātaṃ = အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း  [LEX]
- vatthupurejātaṃ = မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း  [LEX]
- sahajātāKIND = အတူ ပေါ်ပေါက်ခြင်း  [LEX]
- ārabbha rāgo = အာရုံပြု၍ ရာဂ  [LEX]
- tadārammaṇatā = စိတ်သည် ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့်  [LEX]
- aniccato = မမြဲဟု  [LEX]
- vicikicchaṃ ārabbha = ယုံမှားမှုကို အာရုံပြု၍  [LEX]
- uddhaccaṃ ārabbha = ယောက်ယက်ခတ်မှုကို အာရုံပြု၍  [LEX]
- vipassanaṃ = ထိုးထွင်းသိမြင်ခြင်း  [LEX]
- (sahajāte idaṃ nānākaraṇaṃ) = (အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း၌ ဤသည်မှာ ကွဲပြားချက် ဖြစ်သည်)  [NOTES]
- (idaṃ nānattaṃ) = (ဤသည်မှာ ကွဲပြားခြင်း ဖြစ်သည်)  [NOTES]
- (adhipatiyā paṭisandhikkhaṇe natthi) = (အကြီးအမှူးဟူသော အကြောင်း၌ ပဋိသန္ဓေ နေသော ခဏ မရှိ)  [NOTES]
- (hetupaccayasadisā nava) = (အမြစ်ဟူသော အကြောင်းနှင့် တူသည်များ ကိုးခု)  [NOTES]
- (vitthārena gaṇetabbaṃ) = (အကျယ်အားဖြင့် ရေတွက်ရမည်)  [NOTES]
- (paṭisandhi paripuṇṇaṃ) = (ပဋိသန္ဓေ ပြည့်စုံသည်)  [NOTES]
- (ekā pañhā) = (ပြဿနာ တစ်ခု)  [NOTES]
- (satta pañhā) = (ပြဿနာ ခုနစ်ခု)  [NOTES]
- (terasa pañhā) = (ပြဿနာ ဆယ့်သုံးခု)  [NOTES]
- (saṃkhittaṃ.) = (အကျဉ်းချုပ်။)  [NOTES]
- (saṃkhittaṃ. = (အကျဉ်းချုပ်။  [NOTES]
- =19 = =19  [NOTES]
- (saṃkhittaṃ = (အကျဉ်းချုပ်  [NOTES]
- sahajātā = (function)  [LINK]
- saṃsaṭṭhā = (function)  [LINK]
- Paccanīyaṃ = အငြင်းပြ ပုံစံ  [HEAD]
- Vipākattikaṃ = ကံ၏ အကျိုး သုံးမျိုးတွဲ  [TIKA_NAME]
- Upādinnattikaṃ = ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ  [TIKA_NAME]
- Saṃkiliṭṭhattikaṃ = ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ  [TIKA_NAME]
- ekādasaka = ဆယ့်တစ်မျိုးတွဲ  [GROUP]
- dvādasaka = ဆယ့်နှစ်မျိုးတွဲ  [GROUP]
- terasaka = ဆယ့်သုံးမျိုးတွဲ  [GROUP]
- cuddasaka = ဆယ့်လေးမျိုးတွဲ  [GROUP]
- pannarasaka = ဆယ့်ငါးမျိုးတွဲ  [GROUP]
- soḷasaka = ဆယ့်ခြောက်မျိုးတွဲ  [GROUP]
- sattarasaka = ဆယ့်ခုနစ်မျိုးတွဲ  [GROUP]
- aṭṭhārasaka = ဆယ့်ရှစ်မျိုးတွဲ  [GROUP]
- ekādasa = ဆယ့်တစ်ခု  [COUNT]
- dvādasa = ဆယ့်နှစ်ခု  [COUNT]
- terasa = ဆယ့်သုံးခု  [COUNT]
- cuddasa = ဆယ့်လေးခု  [COUNT]
- pannarasa = ဆယ့်ငါးခု  [COUNT]
- soḷasa = ဆယ့်ခြောက်ခု  [COUNT]
- sattarasa = ဆယ့်ခုနစ်ခု  [COUNT]
- aṭṭhārasa = ဆယ့်ရှစ်ခု  [COUNT]
- ekūnavīsati = ဆယ့်ကိုးခု  [COUNT]
- vīsati = နှစ်ဆယ်ခု  [COUNT]
- ekavīsati = နှစ်ဆယ့်တစ်ခု  [COUNT]
- dvāvīsati = နှစ်ဆယ့်နှစ်ခု  [COUNT]
- bāvīsati = နှစ်ဆယ့်နှစ်ခု  [COUNT]
- tevīsati = နှစ်ဆယ့်သုံးခု  [COUNT]
- tevīsa = နှစ်ဆယ့်သုံးခု  [COUNT]
- catuvīsati = နှစ်ဆယ့်လေးခု  [COUNT]
- cakkhu = မျက်စိ  [SKF]
- sota = နား  [SKF]
- ghāna = နှာခေါင်း  [SKF]
- jivhā = လျှာ  [SKF]
- kāya = ကိုယ်  [SKF]
- ekaṃ mahābhūtaṃ = မူလဓာတ်ကြီး တစ်ပါး  [SKF]
- §T§o ca ubhayañca = {T1} သဘောတရားလည်းကောင်း၊ နှစ်မျိုးလုံးလည်းကောင်း  [SKF]
- §T§añca §T§añca = {T1} သဘောတရားနှင့် {T2} သဘောတရား  [SKF]
- vatthuṃ khandhā = မှီရာ ဝတ္ထုကို မှီ၍ အစုအဝေးများ  [SKF]
- purimā purimā = ရှေးရှေး  [SKF]
- rūpāyatanaṃ cakkhuviññāṇassa purejāta = အဆင်းအရောင် အာရုံခံ နယ်ပယ်သည် မျက်စိ သိစိတ်အား ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း  [SKF]
- ekā = တစ်ခု  [SKF]
- tisso = သုံးခု  [SKF]
- tīṇi (paṭisandhi kātabbā §V§.) = သုံးခု (ပဋိသန္ဓေကို ထည့်ရမည် {V1}။)  [SKF]
- vatthuṃ §C§ā (anantarasadisaṃ = မှီရာ ဝတ္ထု {C1.ab} (ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်  [SKF]
- paccayo = အကြောင်း ဖြစ်သည်  [SKF]
- tiṇṇannaṃ = 3  [NP_NUM]
- pañcannaṃ = 5  [NP_NUM]
- 5 = ငါးပါး  [PAA]
- ubhayañca (after X ca) = နှစ်မျိုးလုံး  [NEW]
- nānākaraṇaṃ = ကွဲပြားချက်  [NEW]
- nānattaṃ = ကွဲပြားခြင်း  [NEW]
- vitthārena = အကျယ်အားဖြင့်  [NEW]
- pañhā = ပြဿနာ  [NEW]
- Sabhāgaṃ = တွဲဖက်သည်များ  [NEW]
- parikammaṃ = ကြိုတင် ပြင်ဆင်မှု  [NEW]
- ṭhānāṭhānakosalla = ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု  [NEW]
- suciṇṇāni = ကောင်းစွာ ပြုခဲ့ဖူးသည်  [NEW]
- tadārammaṇatā = ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့်  [NEW]
- hantvā = သတ်၍  [NEW]
- bhinditvā = ဖြိုခွဲ၍  [NEW]
- sadiso (X-pi Y-pi sadiso) = တူသည်  [NEW]
- avipākaṃ (ghaṭanā group) = ကံ၏ အကျိုးဟူသော အကြောင်း မပါဝင်သော  [NEW]
- savipākaṃ (ghaṭanā group) = ကံ၏ အကျိုးဟူသော အကြောင်း ပါဝင်သော  [NEW]
- gambhīrā sukhumatarā ca = နက်နဲ၍ ပို၍ သိမ်မွေ့သည်  [NEW]
- evaṃ kātūna = ဤသို့ ပြု၍  [NEW]
- sajjhāyamaggo = သရဇ္ဈာယ်သည့် နည်းလမ်း  [NEW]
- vibhattā / vibhattaṃ (after yathā) = ခွဲခြမ်းစိတ်ဖြာထားသည့်အတိုင်း  [NEW]
- vibhajitabbaṃ / -bāni = ခွဲခြမ်းစိတ်ဖြာရမည်  [NEW]
- idhāpi = ဤနေရာ၌လည်း  [NEW]
- idaṃ (object) = ဤသည်ကို  [NEW]
- vipāk = ကံ၏ အကျိုး ဖြစ်သော  [TRIAD]
- vipākadhammadhamm = အကျိုး ပေးတတ်သော  [TRIAD]
- nevavipākanavipākadhammadhamm = ကံ၏ အကျိုးလည်း မဟုတ်၊ အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော  [TRIAD]
- vipākadhamma = အကျိုး ပေးတတ်သော  [TRIAD]
- nevavipākanavipākadhamma = ကံ၏ အကျိုးလည်း မဟုတ်၊ အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော  [TRIAD]
- upādinnupādāniy = ကံကြောင့် ဖြစ်၍ စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော  [TRIAD]
- anupādinnupādāniy = ကံကြောင့် မဖြစ်သော်လည်း စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော  [TRIAD]
- anupādinnaanupādāniy = ကံကြောင့်လည်း မဖြစ်၊ စွဲလမ်းမှု၏ အာရုံလည်း မဖြစ်နိုင်သော  [TRIAD]
- saṃkiliṭṭhasaṃkilesik = ကိလေသာဖြင့် ညစ်နွမ်း၍ ကိလေသာ၏ အာရုံလည်း ဖြစ်နိုင်သော  [TRIAD]
- asaṃkiliṭṭhasaṃkilesik = ကိလေသာဖြင့် မညစ်နွမ်းသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော  [TRIAD]
- asaṃkiliṭṭhaasaṃkilesik = ကိလေသာဖြင့်လည်း မညစ်နွမ်း၊ ကိလေသာ၏ အာရုံလည်း မဖြစ်နိုင်သော  [TRIAD]
- asaṅkiliṭṭhasaṃkilisik = ကိလေသာဖြင့် မညစ်နွမ်းသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော  [TRIAD]
