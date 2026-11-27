# pi-1 Burmese zero-shot, chapters 2-04 and 2-05 (Cittuppādakaṇḍa: twelve unwholesome cittas, resultants, functional cittas): notes

Status 2026-11-16: both chapters done, all checks pass. Not committed. Translated from the Pāli only
(AI_translation/pali/pi-1_split_chapters/2-04-, 2-05-cittuppadakandam.md). The English zero-shot was read for meaning
only. No Burmese translation, nissaya or web source was used.

## Files
- AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/2-04-cittuppadakandam.md (149 segments, 169 lines)
- AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/2-05-cittuppadakandam.md (99 segments, 129 lines)
- make_ch2-04-05.py: generator (`python3 -I -X utf8 make_ch2-04-05.py [2-04 | 2-05 | --terms]`). It imports
  my_formulas.py and adds every new string IN MEMORY (add() refuses to change an existing value); my_formulas.py and
  my-zeroshot-terms.md are not edited. New clause rules in F.CU_EXTRA_RULES: «Katame / ime dhammā akusalā / abyākatā»
  and open_my() for every opening that is not «Yasmiṃ samaye KIND cittaṃ uppannaṃ hoti …». The akusala openings
  use the model's r_open unchanged (CITTA_KIND «akusalaṃ cittaṃ» and the new QUAL entries added).
  --terms rewrites the generated list at the end of this file.
- check_ch2-04-05.py: own per-line check, adapted from check_ch2-01.py (tables from my_formulas + the generator's
  in-memory additions; the engine is not used). Mutation-tested: a dropped negation, two swapped synonyms, a dropped
  synonym, a wrong number and a wrong jhāna qualifier are all reported.

## Checks (all pass, both chapters)
- check_chapter_ids.py: OK (2-04: 149 segments; 2-05: 99 segments).
- pi-6-mr/check_text_pe.py: OK (169 / 129 lines, dashes match); my chk-pe copies were deleted afterwards.
- pi-4-mr/check_marks.py: OK.
- check_ch2-04-05.py: OK (169 / 129 lines, 0 mismatches).

## How the openings are built (open_my)
- The Pāli between «Yasmiṃ samaye» (or «Tasseva») and «, tasmiṃ samaye» is split at «…pe…»; each segment is read
  with a longest-match phrase table (PRE, JH, Q, QN, K, KIND, QUAL, OBJ); the «…» stays where the Pāli has «…pe…».
  The opening ends in «… အချိန်၌» (after a «…သော» form; «ဖြစ်သော အချိန်၌» after a noun), then «၊ ထိုအချိန်၌» as in
  the model.
- Resultant / functional citta with «X-ārammaṇā vā …»: the model's order (objects, «မည်သည့်အရာကို …», qualifiers,
  «KIND-သည် ဖြစ်ပေါ်လာသော အချိန်၌»), the «…» inside the object list as in 2-01.
- Sense consciousness segments (^1-443, ^1-556): each segment is a full clause «X-ကို အာရုံပြုသော၊ QUAL KIND-သည်
  ဖြစ်ပေါ်လာသော», only the last gets «အချိန်၌».
- The eight-fold qualifier chains (^1-498, ^1-576): «KIND-သည် QUAL၊ QUAL… QUAL [တိုက်တွန်းမှုဖြင့်]… objects …
  ဖြစ်ပေါ်လာသော အချိန်၌»: the one «uppannā hoti» comes once, at the end (verb-final Burmese).
- Jhāna segments: the qualifiers that follow «upasampajja viharati» (pathavīkasiṇaṃ, dukkhapaṭipadaṃ …, suññataṃ …,
  chandādhipateyyaṃ …) are put before the jhāna inside the same segment: «Q1၍ Q2သော ပထမ ဈာန်ကို ဝင်စား၍ နေသော»;
  a qualifier-only segment is «Q1၍ Q2သော…». «…nti kusalaṃ» / «…nti vipāko» = «Q…သော ကုသိုလ်» / «Q…သော ကံ၏ အကျိုး»
  (the quotation «ti» is carried by the apposition; no quote marks added).

## Main choices (one-line reasons)
- akusala frames = the model's kusala frames with «အကုသိုလ်»; abyākata: «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
  သဘောတရားများ ဟူသည် အဘယ်တို့နည်း» and «ဤသဘောတရားများသည် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ
  ဖြစ်ကြသည်» (TERMS abyākatā is attributive, so the noun is repeated).
- micchā- = «မှားယွင်းသော» (as micchattaniyatā); diṭṭhigata = «အယူမှား» (everyday «wrong view»), in
  diṭṭhigatasampayutta, diṭṭhigatānaṃ pahānāya and the micchādiṭṭhi list alike.
- lobha / dosa / moha = «လောဘ / ဒေါသ / မောဟ» (the model has «လောဘ မရှိခြင်း» …); abhijjhā = «သူ့ဥစ္စာကို လိုချင်ခြင်း»,
  byāpāda = «ဖျက်ဆီးလိုစိတ်» (the model's negatives without «မ»).
- ahirika / anottappa (factor and body) = the sample's SUT «ဒုစရိုက်ကို မရှက်မှု / မကြောက်ရွံ့မှု»; the definitions
  are the model's hiri / ottappa sentences with «မရှက်ခြင်း / မကြောက်ရွံ့ခြင်း».
- domanassa = «စိတ်ဆင်းရဲမှု» (mental pain; «နှလုံးမသာ» rejected: its «မ» is not a Pāli negation); paṭigha
  (aversion) = «မုန်းတီးမှု», kept apart from paṭigha (impact) = the sample's «ထိခိုက်မှု» in paṭighasaññā.
- vicikicchā = «ယုံမှားသံသယ», kaṅkhā = «ယုံမှားခြင်း», saṃsaya = «သံသယ», vimati = «တွေဝေခြင်း» (kept apart, style rule).
- uddhacca = «ယောက်ယက်ခတ်မှု» (restlessness); vikkhepa = «ပျံ့လွင့်ခြင်း» (one root with the model's avikkhepo).
- asāta = «နှစ်သက်ဖွယ် မကောင်း» (as the model's nāsātaṃ); kāyika = «ကိုယ်ပိုင်းဆိုင်ရာ» (parallel to cetasika
  «စိတ်ပိုင်းဆိုင်ရာ»); kāyasamphassaja = «ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော»; the physical body = «ကိုယ်» (the model's
  KAYA «စိတ်၏ အဖော်တို့» is only for kāyapassaddhi …).
- cakkhu / sota / ghāna / jivhā / kāya-viññāṇa = «မျက်စိ / နား / နှာခေါင်း / လျှာ / ကိုယ် သိစိတ်»; manodhātu = «မနော ဓာတ်».
- vipāka = «ကံ၏ အကျိုး» (TERMS vipākā); kusalavipāka = «ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော»; «kammassa katattā upacitattā» =
  «ကံကို ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့်»; «jhānassa katattā bhāvitattā» = «ဈာန်ကို ပြုခဲ့၍ ပွားများခဲ့သောကြောင့်»;
  «Tasseva … vipākaṃ» = «ထို …ကိုပင် … ကံ၏ အကျိုး အဖြစ်ဖြင့်».
- kiriya = «ပြုရုံမျှသာ ဖြစ်သော» (functional, merely doing; the loan ကြိယာ is not plain); «kiriyā neva kusalā nākusalā
  na ca kammavipākā» = «ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်၊ ကံ၏ အကျိုးလည်း မဟုတ်သော».
- Jhāna formula: bhāveti = «ပွားများ၍»; upasampajja viharati = «ဝင်စား၍ နေ» (as the sample's samāpatti «ဝင်စား»);
  vivicceva kāmehi = «ကာမတို့မှ ကင်းဆိတ်၍သာ»; vitakkavicārānaṃ vūpasamā = «စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့
  ငြိမ်းသွားခြင်းကြောင့်»; sukhassa ca pahānā = «သာယာမှုကိုလည်း ပယ်ခြင်းကြောင့်»; ordinal jhānas with the sample's ORD
  (ပထမ … ပဉ္စမ ဈာန်); pathavīkasiṇa = «မြေ ကသိုဏ်း».
- rūpūpapattiyā maggaṃ = «သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်းစဉ်» (magga here = the way to rebirth, so «လမ်းစဉ်», not
  the path «မဂ်»); lokuttaraṃ maggaṃ (^1-528) = «မဂ်».
- Immaterial bases: «အဆုံးမရှိသော ကောင်းကင် နယ်ပယ်», «အဆုံးမရှိသော သိစိတ် နယ်ပယ်», «ဘာမျှ မရှိသော နယ်ပယ်», «မှတ်သိမှု
  ရှိခြင်းလည်း မဟုတ်၊ မရှိခြင်းလည်း မဟုတ်သော နယ်ပယ်» (āyatana = «နယ်ပယ်», one root with «အာရုံခံ နယ်ပယ်»);
  «-saññāsahagataṃ» = «…နှင့် ဆိုင်သော မှတ်သိမှုနှင့်အတူ» (adverbial, it stands before «sukhassa ca pahānā»).
- Supramundane: niyyānika / apacayagāmi / lokuttara = the Mātikā TERMS; bhūmi = «အဆင့်» (stage); paṭipadā =
  «ကျင့်စဉ်» with dukkha- / sukha- = «ခက်ခဲ / လွယ်ကူ» (ease of the practice, a different sense from the feeling words
  «နာကျင် / သာယာ»); abhiññā = «အထူးသိမြင်မှု», dandha / khippa = «နှေး / လျင်မြန်»; suññata = «ဆိတ်သုဉ်း» (as
  Suññatavāra); animitta = «အမှတ်အသား မရှိ»; appaṇihita = «တောင့်တမှု မရှိ»; -ādhipateyya = «…ကို အကြီးအမှူးပြု» (as
  maggādhipatino); vīmaṃsā = «စုံစမ်းဆင်ခြင်မှု».
- aññindriya = «အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည်», aññātāvindriya = «အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်»; aññā = «အပြည့်အဝ
  သိမြင်ခြင်း»; bojjhaṅga = «ဗောဇ္ဈင်», satipaṭṭhāna = «သတိပဋ္ဌာန်» (everyday Burmese words, like ဈာန်, မဂ်).
- Fetters of the higher paths: kāmarāga = «ကာမရာဂ», rāga = «ရာဂ», māna = «မာန» (everyday words); anavasesappahānāya =
  «အကြွင်းအကျန် မရှိ ပယ်ရန်»; tanubhāvāya = «ပါးလျားစေရန်».
- Numbers: dvādasa = «ဆယ့်နှစ်ပါး», vīsati mahānayā = «ကြီးကျယ်သော နည်း နှစ်ဆယ်»; counted groups with ပါး as in 2-01.
- Headings: suddhika = «သီးသန့်»; «Lokuttaravipāka-paṭhamamaggavipākā» = «… ကံ၏ အကျိုး၊ ပထမ မဂ်၏ အကျိုး» (the hyphen is
  not a dash: no «–» added).
- Variants: [paṭiggāho (sī. syā.)] = ပါဌ်ကွဲ (another word); [vipariyesagāho (ka.)] = စာလုံးပေါင်းကွဲ.

## Unsure Pāli / for the reviewer
- asuropo (dosa list) = «ရိုင်းစိုင်းခြင်း» (rudeness), read as NOT privative; if it is a-suropa, a «မ» is missing.
- The moha list needs 24 distinct «not knowing» words; anabhisamaya / ananubodha / asambodha / appaṭivedha
  («ပိုင်ပိုင် နားမလည် / သဘော မပေါက် / ကောင်းစွာ မသိမြင် / ထိုးထွင်း၍ မသိ») and asaṃgāhanā / apariyogāhanā
  («စုစည်း၍ မယူ / နက်နက်နဲနဲ မသက်ဝင်») are near-synonyms rendered from their roots; please check they read naturally.
- diṭṭhi list images (gahana «ချုံထူ», kantāra «ကန္တာရ», visūkāyika «ကွေ့ကောက်မှု», vipphandita «တုန်လှုပ်မှု»,
  titthāyatana «အယူဝါဒ ဂိုဏ်းတို့၏ တည်ရာ») are literal.
- The «…nti kusalaṃ / vipāko» chains of 2-05 are rendered as appositions («…သော ကုသိုလ်», «…သော ကံ၏ အကျိုး»);
  quote marks could make the quotation explicit.
- kiriya «ပြုရုံမျှသာ ဖြစ်သော» and iddhipāda «အောင်မြင်မှု၏ အခြေခံ» are plain renderings where religious readers may
  expect the loans ကြိယာ / ဣဒ္ဓိပါဒ်.
- The jhāna / path / immaterial phrases are new here and also occur in 2-02 / 2-03 (another agent): the consistency
  pass should align them.

## Source slips (translated as written)
- ^1-377 ends «… samādhindriyaṃ hoti?» (a statement with a question mark): «။» as everywhere.
- ^1-473: «Katamā tasmiṃ samaye cetanā hoti.» (a question with a full stop): rendered as the question frame.
- ^1-528: «… ime dhammā kusalā tasseva lokuttarassa …»: no full stop and a small «t»; no «။» added.
- ^1-544: «… upasampajja viharati, animittaṃ chandādhipateyyaṃ»: stray comma; dropped (the qualifier is put before
  the jhāna).
- ^1-553: «kāmarā gabyāpādānaṃ» (a space inside kāmarāga-byāpādānaṃ): read as kāmarāgabyāpādānaṃ.
- ^1-574: «samādhindriyaṃ hoti manindriyaṃ hoti» (comma missing): no «၊» there in the Burmese either.
- ^1-579: «… upasampajja viharati tasmiṃ samaye» (comma missing): no «၊» before «ထိုအချိန်၌» either.

## New recurring terms (generated by make_ch2-04-05.py --terms)

One «Pāli = Burmese» per line, generated from the in-memory additions of make_ch2-04-05.py (my_formulas.py and my-zeroshot-terms.md are not edited).

### Factor names (NAMES)

micchādiṭṭhi = မှားယွင်းသော အယူ
micchāsaṅkappo = မှားယွင်းသော ကြံစည်မှု
micchāvāyāmo = မှားယွင်းသော အားထုတ်မှု
micchāsamādhi = မှားယွင်းသော သမာဓိ
ahirikabalaṃ = ဒုစရိုက်ကို မရှက်မှု၏ စွမ်းအား
anottappabalaṃ = ဒုစရိုက်ကို မကြောက်ရွံ့မှု၏ စွမ်းအား
lobho = လောဘ
doso = ဒေါသ
moho = မောဟ
abhijjhā = သူ့ဥစ္စာကို လိုချင်ခြင်း
byāpādo = ဖျက်ဆီးလိုစိတ်
ahirikaṃ = ဒုစရိုက်ကို မရှက်မှု
anottappaṃ = ဒုစရိုက်ကို မကြောက်ရွံ့မှု
dukkhaṃ = နာကျင်မှု
domanassindriyaṃ = စိတ်ဆင်းရဲမှု၏ စွမ်းရည်
sukhindriyaṃ = သာယာမှု၏ စွမ်းရည်
dukkhindriyaṃ = နာကျင်မှု၏ စွမ်းရည်
vicikicchā = ယုံမှားမှု
uddhaccaṃ = ယောက်ယက်ခတ်မှု
abyākatamūlaṃ = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အမြစ်
cakkhuviññāṇadhātu = မျက်စိ သိစိတ် ဓာတ်
kāyaviññāṇadhātu = ကိုယ် သိစိတ် ဓာတ်
manodhātu = မနော ဓာတ်
aññindriyaṃ = အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည်
aññātāvindriyaṃ = အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်
hetu = အမြစ်
tīṇindriyāni = စွမ်းရည် သုံးပါး
pañcindriyāni = စွမ်းရည် ငါးပါး
cattāri indriyāni = စွမ်းရည် လေးပါး
tivaṅgiko maggo = အင်္ဂါ သုံးပါး ရှိသော မဂ်
duvaṅgiko maggo = အင်္ဂါ နှစ်ပါး ရှိသော မဂ်
cattāri balāni = စွမ်းအား လေးပါး
tīṇi balāni = စွမ်းအား သုံးပါး

### Synonyms (SYN)

diṭṭhi = အယူ
diṭṭhigataṃ = အယူမှား
diṭṭhigahanaṃ = အယူ တောအုပ်
diṭṭhikantāro = အယူ ကန္တာရ
diṭṭhivisūkāyikaṃ = အယူ၏ ကောက်ကွေးမှု
diṭṭhivipphanditaṃ = အယူ၏ တုန်လှုပ်မှု
diṭṭhisaṃyojanaṃ = အယူ နှောင်ကြိုး
gāho = စွဲကိုင်ခြင်း
patiṭṭhāho = ခိုင်မြဲစွာ စွဲကိုင်ခြင်း
abhiniveso = သက်ဝင်ယုံကြည်ခြင်း
parāmāso = မှားယွင်းသော ယူဆမှု
kummaggo = လမ်းမှား
micchāpatho = မှားယွင်းသော လမ်းကြောင်း
micchattaṃ = မှားယွင်းမှု
titthāyatanaṃ = အယူဝါဒတို့၏ တည်ရာ
vipariyāsaggāho = ပြောင်းပြန် စွဲကိုင်ခြင်း
lubbhanā = မက်မောခြင်း
lubbhitattaṃ = မက်မောသော အဖြစ်
sārāgo = တပ်မက်ခြင်း
sārajjanā = စွဲမက်ခြင်း
sārajjitattaṃ = စွဲမက်သော အဖြစ်
akusalamūlaṃ = အကုသိုလ်၏ အမြစ်
aññāṇaṃ = မသိခြင်း
adassanaṃ = မမြင်ခြင်း
anabhisamayo = ထင်ထင်ရှားရှား မသိမြင်ခြင်း
ananubodho = လိုက်၍ မနားလည်ခြင်း
asambodho = ကောင်းစွာ မနားလည်ခြင်း
appaṭivedho = ထိုးဖောက်၍ မသိခြင်း
asaṃgāhanā = စုစည်း၍ မယူနိုင်ခြင်း
apariyogāhanā = နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း
asamapekkhanā = ညီညီညွတ်ညွတ် မရှုမြင်ခြင်း
apaccavekkhanā = ပြန်လည် မဆင်ခြင်ခြင်း
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
dussanā = စိတ်ဆိုးခြင်း
dussitattaṃ = စိတ်ဆိုးထားသော အဖြစ်
byāpatti = ဖောက်ပြန်ခြင်း
byāpajjanā = ညှဉ်းဆဲလိုခြင်း
byāpajjitattaṃ = ညှဉ်းဆဲလိုသော အဖြစ်
virodho = ဆန့်ကျင်ခြင်း
paṭivirodho = ပြန်လည် ဆန့်ကျင်ခြင်း
caṇḍikkaṃ = ကြမ်းကြုတ်ခြင်း
asuropo = စကား ကြမ်းခြင်း
anattamanatā cittassa = စိတ်၏ မနှစ်သိမ့်ခြင်း
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
thambhitattaṃ cittassa = စိတ် တောင့်တင်းနေသော အဖြစ်
manovilekho = မနောကို ခြစ်ကုတ်ခြင်း
cittassa uddhaccaṃ = စိတ်၏ ယောက်ယက်ခတ်မှု
avūpasamo = မငြိမ်ဝပ်ခြင်း
cetaso vikkhepo = စိတ်၏ ပျံ့လွင့်ခြင်း
bhantattaṃ cittassa = စိတ်၏ ယိမ်းထိုးနေသော အဖြစ်
cetasikaṃ asātaṃ = စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု
cetasikaṃ dukkhaṃ = စိတ်ပိုင်းဆိုင်ရာ နာကျင်မှု
cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ = စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားရခြင်း
cetosamphassajā asātā dukkhā vedanā = စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားမှု
kāyikaṃ sātaṃ = ကိုယ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ်ကောင်းမှု
kāyikaṃ sukhaṃ = ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှု
kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ = ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားရခြင်း
kāyasamphassajā sātā sukhā vedanā = ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားမှု
kāyikaṃ asātaṃ = ကိုယ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု
kāyikaṃ dukkhaṃ = ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု
kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ = ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားရခြင်း
kāyasamphassajā asātā dukkhā vedanā = ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားမှု
tajjācakkhuviññāṇadhātu = သက်ဆိုင်ရာ မျက်စိ သိစိတ် ဓာတ်
tajjākāyaviññāṇadhātu = သက်ဆိုင်ရာ ကိုယ် သိစိတ် ဓာတ်
tajjāmanodhātu = သက်ဆိုင်ရာ မနော ဓာတ်
aññā = အပြည့်အဝ သိမြင်ခြင်း
dhammavicayasambojjhaṅgo = သဘောတရားများကို စိစစ်ခြင်း ဗောဇ္ဈင်
maggaṅgaṃ = မဂ်၏ အင်္ဂါ
maggapariyāpannaṃ = မဂ်၌ အကျုံးဝင်သောအရာ

### List heads (GEN)

tajjācakkhuviññāṇadhātusamphassajaṃ = သက်ဆိုင်ရာ မျက်စိ သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော
tajjācakkhuviññāṇadhātusamphassajā = သက်ဆိုင်ရာ မျက်စိ သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော
tajjākāyaviññāṇadhātusamphassajaṃ = သက်ဆိုင်ရာ ကိုယ် သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော
tajjākāyaviññāṇadhātusamphassajā = သက်ဆိုင်ရာ ကိုယ် သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော
tajjāmanodhātusamphassajaṃ = သက်ဆိုင်ရာ မနော ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော
tajjāmanodhātusamphassajā = သက်ဆိုင်ရာ မနော ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော
tesaṃ aññātāvīnaṃ dhammānaṃ = အပြည့်အဝ သိမြင်ပြီးသော ထို သဘောတရားတို့၏

### Sentence definitions (BODY)

Yaṃ tasmiṃ samaye na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ထိုအချိန်၌ ရှက်ထိုက်သည့်အရာကို မရှက်ခြင်း၊ ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို မရှက်ခြင်း
Yaṃ tasmiṃ samaye na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ထိုအချိန်၌ ကြောက်ရွံ့ထိုက်သည့်အရာကို မကြောက်ရွံ့ခြင်း၊ ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို မကြောက်ရွံ့ခြင်း

### Citta opening (CITTA_KIND)

akusalaṃ cittaṃ = အကုသိုလ်စိတ်

### Citta opening (QUAL)

diṭṭhigatasampayuttaṃ = အယူမှားနှင့် ယှဉ်တွဲသော
diṭṭhigatavippayuttaṃ = အယူမှားနှင့် ကင်းကွာသော
domanassasahagataṃ = စိတ်ဆင်းရဲမှုနှင့်အတူ ဖြစ်သော
paṭighasampayuttaṃ = မုန်းတီးမှုနှင့် ယှဉ်တွဲသော
vicikicchāsampayuttaṃ = ယုံမှားမှုနှင့် ယှဉ်တွဲသော
uddhaccasampayuttaṃ = ယောက်ယက်ခတ်မှုနှင့် ယှဉ်တွဲသော
sukhasahagataṃ = သာယာမှုနှင့်အတူ ဖြစ်သော
dukkhasahagataṃ = နာကျင်မှုနှင့်အတူ ဖြစ်သော

### Citta opening (resultant / functional)

kiriyā neva kusalā nākusalā na ca kammavipākā = ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်၊ ကံ၏ အကျိုးလည်း မဟုတ်သော

### Jhāna and path phrases (openings)

kāmāvacarassa kusalassa kammassa katattā upacitattā = ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်ကံကို ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့်
akusalassa kammassa katattā upacitattā = အကုသိုလ်ကံကို ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့်
tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ = ထို သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ကုသိုလ်ကံကိုပင် ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့် ကံ၏ အကျိုး အဖြစ်ဖြင့်
tasseva arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ = ထို ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ကုသိုလ်ကံကိုပင် ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့် ကံ၏ အကျိုး အဖြစ်ဖြင့်
tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ = ထို လောကကို ကျော်လွန်သော ကုသိုလ် ဈာန်ကိုပင် ပြုခဲ့၍ ပွားများခဲ့သောကြောင့် ကံ၏ အကျိုး အဖြစ်ဖြင့်
rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ = ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်၊ ကံ၏ အကျိုးလည်း မဟုတ်သော၊ မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်ရန် ဖြစ်သော သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ဈာန်ကို ပွားများ၍
arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ = ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်၊ ကံ၏ အကျိုးလည်း မဟုတ်သော၊ မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်ရန် ဖြစ်သော ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ဈာန်ကို ပွားများ၍
sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā = ရုပ်ဟု မှတ်သိမှုတို့ကို အလုံးစုံ ကျော်လွန်ခြင်းကြောင့်၊ ထိခိုက်မှုဟု မှတ်သိမှုတို့ ချုပ်ငြိမ်းသွားခြင်းကြောင့်၊ အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှုတို့ကို နှလုံး မသွင်းခြင်းကြောင့်
rūpūpapattiyā maggaṃ bhāveti = သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်းကို ပွားများ၍
arūpūpapattiyā maggaṃ bhāveti = ရုပ်မရှိသော ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်းကို ပွားများ၍
vivicceva kāmehi = ကာမတို့မှ ကင်းဆိတ်၍သာ
vitakkavicārānaṃ vūpasamā = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်းကြောင့်
sukhassa ca pahānā = သာယာမှုကိုလည်း ပယ်ခြင်းကြောင့်
sabbaso ākāsānañcāyatanaṃ samatikkamma = အဆုံး မရှိသော ကောင်းကင် နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍
sabbaso viññāṇañcāyatanaṃ samatikkamma = အဆုံး မရှိသော သိစိတ် နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍
sabbaso ākiñcaññāyatanaṃ samatikkamma = ဘာမျှ မရှိသော နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍
lokuttaraṃ jhānaṃ bhāveti = လောကကို ကျော်လွန်သော ဈာန်ကို ပွားများ၍
lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော ဈာန်ကို ပွားများ၍
lokuttaraṃ maggaṃ bhāveti = လောကကို ကျော်လွန်သော မဂ်ကို ပွားများ၍
lokuttaraṃ maggaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော မဂ်ကို ပွားများ၍
lokuttaraṃ satipaṭṭhānaṃ bhāveti = လောကကို ကျော်လွန်သော သတိပဋ္ဌာန်ကို ပွားများ၍
lokuttaraṃ satipaṭṭhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော သတိပဋ္ဌာန်ကို ပွားများ၍
lokuttaraṃ sammappadhānaṃ bhāveti = လောကကို ကျော်လွန်သော မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်းကို ပွားများ၍
lokuttaraṃ sammappadhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်းကို ပွားများ၍
lokuttaraṃ iddhipādaṃ bhāveti = လောကကို ကျော်လွန်သော ဣဒ္ဓိပါဒ်ကို ပွားများ၍
lokuttaraṃ iddhipādaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော ဣဒ္ဓိပါဒ်ကို ပွားများ၍
lokuttaraṃ indriyaṃ bhāveti = လောကကို ကျော်လွန်သော စွမ်းရည်ကို ပွားများ၍
lokuttaraṃ indriyaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော စွမ်းရည်ကို ပွားများ၍
lokuttaraṃ balaṃ bhāveti = လောကကို ကျော်လွန်သော စွမ်းအားကို ပွားများ၍
lokuttaraṃ balaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော စွမ်းအားကို ပွားများ၍
lokuttaraṃ bojjhaṅgaṃ bhāveti = လောကကို ကျော်လွန်သော ဗောဇ္ဈင်ကို ပွားများ၍
lokuttaraṃ bojjhaṅgaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော ဗောဇ္ဈင်ကို ပွားများ၍
lokuttaraṃ saccaṃ bhāveti = လောကကို ကျော်လွန်သော သစ္စာကို ပွားများ၍
lokuttaraṃ saccaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော သစ္စာကို ပွားများ၍
lokuttaraṃ samathaṃ bhāveti = လောကကို ကျော်လွန်သော စိတ်ငြိမ်သက်ခြင်းကို ပွားများ၍
lokuttaraṃ samathaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော စိတ်ငြိမ်သက်ခြင်းကို ပွားများ၍
lokuttaraṃ dhammaṃ bhāveti = လောကကို ကျော်လွန်သော သဘောတရားကို ပွားများ၍
lokuttaraṃ dhammaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော သဘောတရားကို ပွားများ၍
lokuttaraṃ khandhaṃ bhāveti = လောကကို ကျော်လွန်သော အစုအဝေးကို ပွားများ၍
lokuttaraṃ khandhaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော အစုအဝေးကို ပွားများ၍
lokuttaraṃ āyatanaṃ bhāveti = လောကကို ကျော်လွန်သော အာရုံခံ နယ်ပယ်ကို ပွားများ၍
lokuttaraṃ āyatanaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော အာရုံခံ နယ်ပယ်ကို ပွားများ၍
lokuttaraṃ dhātuṃ bhāveti = လောကကို ကျော်လွန်သော ဓာတ်ကို ပွားများ၍
lokuttaraṃ dhātuṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော ဓာတ်ကို ပွားများ၍
lokuttaraṃ āhāraṃ bhāveti = လောကကို ကျော်လွန်သော အာဟာရကို ပွားများ၍
lokuttaraṃ āhāraṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော အာဟာရကို ပွားများ၍
lokuttaraṃ phassaṃ bhāveti = လောကကို ကျော်လွန်သော တွေ့ထိမှုကို ပွားများ၍
lokuttaraṃ phassaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော တွေ့ထိမှုကို ပွားများ၍
lokuttaraṃ vedanaṃ bhāveti = လောကကို ကျော်လွန်သော ခံစားမှုကို ပွားများ၍
lokuttaraṃ vedanaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော ခံစားမှုကို ပွားများ၍
lokuttaraṃ saññaṃ bhāveti = လောကကို ကျော်လွန်သော မှတ်သိမှုကို ပွားများ၍
lokuttaraṃ saññaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော မှတ်သိမှုကို ပွားများ၍
lokuttaraṃ cetanaṃ bhāveti = လောကကို ကျော်လွန်သော စေ့ဆော်မှုကို ပွားများ၍
lokuttaraṃ cetanaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော စေ့ဆော်မှုကို ပွားများ၍
lokuttaraṃ cittaṃ bhāveti = လောကကို ကျော်လွန်သော စိတ်ကို ပွားများ၍
lokuttaraṃ cittaṃ bhāveti niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော စိတ်ကို ပွားများ၍
diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā = အယူမှားတို့ကို ပယ်ရန်၊ ပထမ အဆင့်သို့ ရောက်ရန်
kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā = ကာမရာဂနှင့် ဖျက်ဆီးလိုစိတ်တို့ ပါးလျစေရန်၊ ဒုတိယ အဆင့်သို့ ရောက်ရန်
kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā = ကာမရာဂနှင့် ဖျက်ဆီးလိုစိတ်တို့ကို အကြွင်းအကျန် မရှိအောင် ပယ်ရန်၊ တတိယ အဆင့်သို့ ရောက်ရန်
rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā = သိမ်မွေ့သော ရုပ်ဘုံ၌ ရာဂ၊ ရုပ်မရှိသော ဘုံ၌ ရာဂ၊ မာန၊ ယောက်ယက်ခတ်မှု၊ အမှန်ကို မသိမှုတို့ကို အကြွင်းအကျန် မရှိအောင် ပယ်ရန်၊ စတုတ္ထ အဆင့်သို့ ရောက်ရန်
kāmarā gabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā = ကာမရာဂနှင့် ဖျက်ဆီးလိုစိတ်တို့ကို အကြွင်းအကျန် မရှိအောင် ပယ်ရန်၊ တတိယ အဆင့်သို့ ရောက်ရန်
ākāsānañcāyatanasaññāsahagataṃ = အဆုံး မရှိသော ကောင်းကင် နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
viññāṇañcāyatanasaññāsahagataṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
ākiñcaññāyatanasaññāsahagataṃ = ဘာမျှ မရှိသော နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
nevasaññānāsaññāyatanasaññāsahagataṃ = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော

### Jhāna (ordinal)

paṭhamaṃ jhānaṃ = ပထမ ဈာန်
dutiyaṃ jhānaṃ = ဒုတိယ ဈာန်
tatiyaṃ jhānaṃ = တတိယ ဈာန်
catutthaṃ jhānaṃ = စတုတ္ထ ဈာန်
pañcamaṃ jhānaṃ = ပဉ္စမ ဈာန်

### Jhāna qualifiers (attributives, joined with «၊ »; shared my_formulas.JH_Q)

pathavīkasiṇaṃ = မြေ ကသိုဏ်းကို အာရုံပြုသော
dukkhapaṭipadaṃ = ကျင့်စဉ် ခက်ခဲသော
sukhapaṭipadaṃ = ကျင့်စဉ် လွယ်ကူသော
dandhābhiññaṃ = ထူးကဲစွာ သိခြင်း နှေးကွေးသော
khippābhiññaṃ = ထူးကဲစွာ သိခြင်း လျင်မြန်သော
suññataṃ = ဆိတ်သုဉ်းသော
animittaṃ = အမှတ်အသား မရှိသော
appaṇihitaṃ = တောင့်တမှု မရှိသော
chandādhipateyyaṃ = ဆန္ဒကို အကြီးအမှူးပြုသော
vīriyādhipateyyaṃ = ဝီရိယကို အကြီးအမှူးပြုသော
cittādhipateyyaṃ = စိတ်ကို အကြီးအမှူးပြုသော
vīmaṃsādhipateyyaṃ = စုံစမ်းဆင်ခြင်မှုကို အကြီးအမှူးပြုသော
upasampajja viharati = ဝင်စား၍ နေသော (after «…ဈာန်ကို»)
…nti kusalaṃ / …nti vipāko = … ကုသိုလ် / … ကံ၏ အကျိုး (after the qualifier chain)
vipākaṃ / vipākā (before the citta) = ကံ၏ အကျိုး ဖြစ်သော

### Frames

Katame dhammā akusalā? = အကုသိုလ် သဘောတရားများ ဟူသည် အဘယ်တို့နည်း။
Katame dhammā abyākatā? = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ ဟူသည် အဘယ်တို့နည်း။
ime dhammā akusalā = ဤသဘောတရားများသည် အကုသိုလ် ဖြစ်ကြသည်
ime dhammā abyākatā = ဤသဘောတရားများသည် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ ဖြစ်ကြသည်
Yasmiṃ samaye / Tasseva … (opening), tasmiṃ samaye = … အချိန်၌၊ ထိုအချိန်၌

### Headings and colophons

Dvādasa akusalāni = အကုသိုလ် ဆယ့်နှစ်ပါး
Dvādasa akusalacittāni = အကုသိုလ်စိတ် ဆယ့်နှစ်ပါး
Abyākatavipāko = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော ကံ၏ အကျိုး
Kusalavipākapañcaviññāṇāni = ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော သိစိတ် ငါးပါး
Kusalavipākāni pañcaviññāṇāni = ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော သိစိတ် ငါးပါး
Kusalavipākamanodhātu = ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ်
Kusalavipākā manodhātu = ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ်
Kusalavipākamanoviññāṇadhātusomanassasahagatā = ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော၊ ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော မနော သိစိတ် ဓာတ်
Kusalavipākā manoviññāṇadhātu somanassasahagatā = ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော၊ ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော မနော သိစိတ် ဓာတ်
Kusalavipākamanoviññāṇadhātuupekkhāsahagatā = ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော၊ ဥပေက္ခာနှင့်အတူ ဖြစ်သော မနော သိစိတ် ဓာတ်
Kusalavipākā upekkhāsahagatā manoviññāṇadhātu = ကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော၊ ဥပေက္ခာနှင့်အတူ ဖြစ်သော မနော သိစိတ် ဓာတ်
Aṭṭhamahāvipākā = ကြီးကျယ်သော ကံ၏ အကျိုး ရှစ်ပါး
Rūpāvacaravipākā = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ကံ၏ အကျိုး
Arūpāvacaravipākā = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ကံ၏ အကျိုး
Lokuttaravipāka-paṭhamamaggavipākā = လောကကို ကျော်လွန်သော ကံ၏ အကျိုး၊ ပထမ မဂ်၏ အကျိုး
Suddhikapaṭipadā = ကျင့်စဉ် သက်သက်
Suddhikasuññataṃ = ဆိတ်သုဉ်းခြင်း သက်သက်
Suññatapaṭipadā = ဆိတ်သုဉ်းခြင်းနှင့် ကျင့်စဉ်
Suddhikaappaṇihitaṃ = တောင့်တမှု မရှိခြင်း သက်သက်
Appaṇihitapaṭipadā = တောင့်တမှု မရှိခြင်းနှင့် ကျင့်စဉ်
Vīsati mahānayā = နည်းကြီး နှစ်ဆယ်
Chandādhipateyyasuddhikapaṭipadā = ဆန္ဒကို အကြီးအမှူးပြုသော ကျင့်စဉ် သက်သက်
Chandādhipateyyasuddhikasuññatā = ဆန္ဒကို အကြီးအမှူးပြုသော ဆိတ်သုဉ်းခြင်း သက်သက်
Paṭhamamaggavipāko = ပထမ မဂ်၏ အကျိုး
Dutiyādimaggavipāko = ဒုတိယ စသော မဂ်တို့၏ အကျိုး
Lokuttaravipāko = လောကကို ကျော်လွန်သော ကံ၏ အကျိုး
Akusalavipākaabyākataṃ = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အကုသိုလ်ကံ၏ အကျိုး
Akusalavipākapañcaviññāṇāni = အကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော သိစိတ် ငါးပါး
Akusalavipākamanodhātu = အကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ်
Akusalavipākā manodhātu = အကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ်
Akusalavipākamanoviññāṇadhātu = အကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ်
Akusalavipākā manoviññāṇadhātu = အကုသိုလ်ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ်
Vipākā abyākatā = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ
Ahetukakiriyāabyākataṃ = အမြစ် မရှိသော၊ ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား
Kiriyāmanodhātu = ပြုရုံမျှသာ ဖြစ်သော မနော ဓာတ်
Kiriyā manodhātu = ပြုရုံမျှသာ ဖြစ်သော မနော ဓာတ်
Kiriyāmanoviññāṇadhātusomanassasahagatā = ပြုရုံမျှသာ ဖြစ်သော၊ ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော မနော သိစိတ် ဓာတ်
Kiriyā manoviññāṇadhātu somanassasahagatā = ပြုရုံမျှသာ ဖြစ်သော၊ ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော မနော သိစိတ် ဓာတ်
Kiriyāmanoviññāṇadhātuupekkhāsahagatā = ပြုရုံမျှသာ ဖြစ်သော၊ ဥပေက္ခာနှင့်အတူ ဖြစ်သော မနော သိစိတ် ဓာတ်
Kiriyā manoviññāṇadhātu upekkhāsahagatā = ပြုရုံမျှသာ ဖြစ်သော၊ ဥပေက္ခာနှင့်အတူ ဖြစ်သော မနော သိစိတ် ဓာတ်
Ahetukā kiriyā abyākatā = အမြစ် မရှိသော၊ ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ
Sahetukakāmāvacarakiriyā = အမြစ် ရှိသော၊ ကာမဘုံနှင့် ဆိုင်သော ပြုရုံမျှသာ ဖြစ်သော စိတ်
Sahetukā kāmāvacarakiriyā = အမြစ် ရှိသော၊ ကာမဘုံနှင့် ဆိုင်သော ပြုရုံမျှသာ ဖြစ်သော စိတ်
Rūpāvacarakiriyā = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ပြုရုံမျှသာ ဖြစ်သော စိတ်
Arūpāvacarakiriyā = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ပြုရုံမျှသာ ဖြစ်သော စိတ်
Kiriyā abyākatā = ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားများ
Cittuppādakaṇḍaṃ niṭṭhitaṃ = “စိတ် ဖြစ်ပေါ်ခြင်း အခန်း” ပြီးဆုံးပြီ

### Variant readings

paṭiggāho = ပါဌ်ကွဲ
vipariyesagāho = စာလုံးပေါင်းကွဲ
