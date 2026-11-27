# pi-2 Burmese zero-shot, chapter 17 (Khuddakavatthuvibhaṅgo): working notes

Scope: 17-khuddakavatthuvibhango.md. Brief: burmese-zeroshot-brief.md. Pāli only; no Burmese translation or nissaya
consulted, no web search; my2_formulas.py, my2-zeroshot-terms.md and pi-1-my/ read only (nothing written there);
make_sample.py not run. Nothing committed.

## Status (2026-11-17): done
- [x] 17-khuddakavatthuvibhango.md: 444 segments, 591 non-empty lines (Mātikā, ekaka … dasaka niddesa,
  taṇhāvicarita, the 62 views).
- check_chapter_ids / pi-6-mr/check_text_pe / pi-4-mr/check_marks: OK (my chk-pe copy deleted).
- check_ch17.py: 0 mismatches (sentences, negations, numbers, variants, typography); pi-1 reuse 56 / 56 identical.
- Regenerate: `python3 -I -X utf8 make_ch17.py [--notes]` (writes only the chapter). Check:
  `check_ch17.py <pāli> <my>`.

## Method
- make_ch17.py imports my2_formulas (read only). Sentence by sentence: (1) a Pāli sentence identical with pi-1 takes
  pi-1's final Burmese (82 sentence uses, 56 distinct lines tested); (2) identical with a finished pi-2 chapter takes
  that Burmese (5: avijjā, indriyesu aguttadvāratā, uddhacca, kāmadhātu question, Ariyā vuccanti …); (3) frames:
  «Tattha katamo X?» = «ထိုတို့အနက် X ဟူသည် အဘယ်(တို့)နည်း။», «– ayaṃ vuccati "X"» = «– ဤသည်ကို “X”ဟု ခေါ်သည်။»,
  «– ime N X» = «– ဤသည်တို့မှာ X N-ပါး ဖြစ်ကြသည်။», «– ayaṃ X» = «– ဤသည်မှာ X ဖြစ်သည်။», «Sabbampi A B» =
  «A အားလုံးသည် B ဖြစ်သည်။» (pi-1 ^ Sabbāpi micchādiṭṭhi …), «A B» identities = «Aသည် B ဖြစ်သည်»;
  (4) synonym lists: «Yo / Yā / Yaṃ [evarūpo] L» = «[ဤသို့ သဘောရှိသော ]L ရှိသမျှ»; the pi-1 lists read from the pi-1
  rails Burmese with counts asserted (lobha, dosa, moha, diṭṭhi, māna, kāma-/bhava-āsava, vicikicchā, uddhacca,
  issā, macchariya, muṭṭhassacca, dovacassatā, pāpamittatā, saññā, bhojane amattaññutā, vītikkama), pi-2 lists
  (thina ch12, indriya-agutti ch12, takko … ch3, vihiṃsā ch3); (5) prose clauses and pattern builders (māna bases,
  taṇhāvicarita, views, kusītavatthu, purisadosa, diṭṭhadhammanibbāna, uccheda views). Unmatched text stops the run.
- The Dhammasaṅgaṇī sentences reused whole: the indriya-agutti sentences, bhojane, Dve paṭisanthārā, Pañca
  macchariyāni, the āsava / upādāna questions, Sabbāpi micchādiṭṭhi …, Ṭhapetvā sīlabbatupādānañca …, Dukkhe aññāṇaṃ …
  (also as a clause), Satthari kaṅkhati …, the natthi list (^2-971; head + tail elsewhere), the sakkāya sentence
  (Vb adds « – » after «ဖြစ်၍»).
- Vb spellings of pi-1 items take pi-1's Burmese (list «Spelling twins» below). The lobha list has rūpataṇhā twice
  (realm, then sense object): the first = «သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု», the second «အဆင်းအရောင်ကို
  တပ်မက်မှု» (as pi-1); the tika «Kāmataṇhā, rūpataṇhā, arūpataṇhā» uses the realm form, the six taṇhākāyā the sense
  form (ch2-4 rūpataṇhā = အဆင်းအရောင်ကို တပ်မက်မှု).
- Identical Pāli = identical Burmese also across senses: ṭhapanā / saṇṭhapanā (kuhanā and upanāha lists) =
  «တည်ထားခြင်း / ကောင်းစွာ တည်ထားခြင်း»; aṭhapanā (kuhanā) «ပြင်ဆင်ထားခြင်း», aṭṭhapanā (upanāha)
  «ခိုင်ခိုင်မြဲမြဲ တည်ထားခြင်း»; chambhitattaṃ (bhaya) = pi-1 thambhitattaṃ «တောင့်တင်းထားသော အဖြစ်» (as ch12).
- Own check: Pāli negation words of the chapter (free na / no / neva / mā / natthi, privatives; nāsaññ-, nārūp-,
  nānant-, nāsāt-, adukkhamasukh- = 2) against «မ» before a syllable; «္မ» (stacked, ဗြဟ္မ), «တမလွန်», «မည်»
  ignored; the elided last «natthi» of «"Natthi dinnaṃ, natthi yiṭṭhaṃ…pe… pavedentī"ti» counted (its Burmese tail
  «… ရဟန်းပုဏ္ဏားတို့ မရှိ» carries the relative clause). Lexical «မ» avoided in new words (ဖျားနာ, not နာမကျန်း;
  ထပ်ကာထပ်ကာ, not အဆက်မပြတ်; ဆက်တိုက်).

## Unsure Pāli / choices to confirm
- asasmi = «ငါ အမြဲ ရှိ၏», sātasmi = «ငါ ပြတ်စဲ၏» (from their own niddesa: nicco … / ucchijjissāmi …); apāhaṃ siyaṃ =
  «ငါ … ဖြစ်ရလျှင် ကောင်းမည်»; anavakāriṃ / avakāriṃ karitvā = «မခွဲခြားဘဲ / ခွဲခြား၍ ပြု၍».
- ^2-943 (Ṅa) «Yadeva tattha sukhapīti cetaso ābhogo» (as written; sukhamiti?) = «သာယာမှုနှင့် ပီတိဟု စိတ်၏ ညွတ်ခြင်း».
- ^2-948 «Na so jāto nāhosi, na so jāto na bhavissati» = «မွေးဖွားသည် မဟုတ်၊ မဖြစ်ခဲ့၊ … မဖြစ်လတ္တံ့» (literal).
- vidhā = «နှိုင်းယှဉ် ချိန်ဆမှု»; kiñcana «တွယ်ငြိရာ»; aṅgaṇa «အစွန်းအကွက်»; kasāva «အမည်းအစက်»; mada «မူးယစ်မှု»
  (X-mado «Xကြောင့် မူးယစ်မှု»); cetokhila «စိတ်၏ ခက်ထန်မှု»; taṇhāvicarita «တပ်မက်မှု၏ ဖြစ်ပုံ»;
  amaravitakka «မသေခြင်းကို ရည်ရွယ်သော စတင်ကြံစည်မှု»; adhimāna «လွန်ကဲစွာ ထင်မှတ်သော မာန»; tathāgata in the views
  kept as «တထာဂတ»; the (?) of the editors = «(အမည်မသိ မူ)» (as ch18).
- dovacassatā / pāpamittatā / muṭṭhassacca / bhojane amattaññutā / sīla- and diṭṭhivipatti / indriyesu aguttadvāratā
  names = pi-1 / pi-2 values (dovacassatā = «သွန်သင်ချက်ကို နားမထောင်ခြင်း»).
- The 37 bodhipakkhiya names in ^2-U26 follow the pi-2 chapter titles (စွမ်းရည်, မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း,
  ဣဒ္ဓိပါဒ်); kāmāvacara «ကာမဘုံနှင့် ဆိုင်သော» (pi-1).

## Source slips (translated as written)
- ^2-905: «ayaṃ vuccati "bhojane amattaññutā."» (full stop inside the quote): «… “…”ဟု ခေါ်သည်။».
- ^2-896: «ayaṃ vuccati vibhavadiṭṭhi» without quotes: no quotes.
- ^2-964: «"ayamahamasmī"ti iñjitametaṃ "bhavissa"nti» (comma missing): no «၊» there.
- ^2-974 / ^2-976 (taṇhāvicarita): «… vā yathā so …» with the comma missing (several items): «၊» supplied between
  the items (commas are not checked; flag for the consistency pass).
- ^2-974 (7): «– evaṃ bhavissanti hoti» (for «evaṃ evaṃ bhavissanti hoti»): rendered as written «ဤသို့ ငါ ဖြစ်လိမ့်မည်ဟု
  ဖြစ်သည်».
- ^2-916: the bracketed editorial questions «( ) [(tattha katamā bhavataṇhā)]», «[(tattha katamā vibhavataṇhā) (?)]»:
  translated inside the brackets, «( )» kept.
- ^2-919: «"asassato loko"ti – vā…pe…» (dash before vā): the dash kept at the same spot.
- ^2-922 / ^2-941: «nādhimuccati na sampasīdati» = «မဆုံးဖြတ်နိုင်၊ မကြည်လင်».
- ^2-951 (Cha): «atthi kho pana eso attā» (pana for bho): no «အချင်း».
- ^2-U53: «pañca cetaso vinibandhā» (question) / «cetasovinibandhā» (closer): same Burmese.
- ^2-933: «bhavantattaṃ cittassa» read as pi-1 bhantattaṃ (spelling slip).

## New strings («Pāli = Burmese»; for the consistency pass)

### Spelling twins (pi-1 / pi-2 Burmese of the other spelling)
nandirāgo = nandīrāgo
parigedho = paligedho
āyūhanī = āyūhinī
āsīsanā = āsisanā
āsīsitattaṃ = āsisitattaṃ
chadanaṃ = chādanaṃ
unnāmo = unnamo
bhavacchando = bhavachando
vippaṭikulaggāhitā = vippaṭikūlaggāhitā
appatissavatā = appaṭissavatā
assati = asati
assaraṇatā = asaraṇatā
thīyanā = thiyanā
thīyitattaṃ cittassa = thiyitattaṃ cittassa
chambhitattaṃ = thambhitattaṃ

### List items (new)
sotaṃ = ရေစီးကြောင်း
jappā = တမ်းတခြင်း
mado = မူးယစ်မှု
majjanā = မူးယစ်ခြင်း
majjitattaṃ = မူးယစ်ထားသော အဖြစ်
vossaggo = လွှတ်ထားခြင်း
vossaggānuppadānaṃ = လွှတ်ထားခြင်းကို ထပ်ကာထပ်ကာ ပြုခြင်း
asakkaccakiriyatā = ရိုရိုသေသေ မပြုခြင်း
asātaccakiriyatā = ထပ်ကာထပ်ကာ မပြုခြင်း
anaṭṭhitakiriyatā = တည်တံ့စွာ မပြုခြင်း
olīnavuttitā = တွန့်ဆုတ်သော အကျင့် ရှိခြင်း
nikkhittachandatā = ဆန္ဒကို ချထားခြင်း
nikkhittadhuratā = တာဝန်ကို ချထားခြင်း
anāsevanā = မမှီဝဲခြင်း
abhāvanā = မပွားများခြင်း
abahulīkammaṃ = အဖန်ဖန် မပြုခြင်း
anadhiṭṭhānaṃ = မဆောက်တည်ခြင်း
ananuyogo = အားမထုတ်ခြင်း
pamādo = မေ့လျော့မှု
pamajjanā = မေ့လျော့ခြင်း
pamajjitattaṃ = မေ့လျော့ထားသော အဖြစ်
thambho = တောင့်တင်းမှု
thambhanā = တောင့်တင်းခြင်း
thambhitattaṃ = တောင့်တင်းထားသော အဖြစ်
kakkhaḷiyaṃ = ကြမ်းတမ်းခြင်း
phārusiyaṃ = ကြမ်းကြုတ်သော အဖြစ်
ujucittatā = စိတ် ခေါင်းမာခြင်း
amudutā = မနူးညံ့ခြင်း
sārambho = ပြိုင်ဆိုင်မှု
paṭisārambho = ပြန်လည် ပြိုင်ဆိုင်မှု
sārambhanā = ပြိုင်ဆိုင်ခြင်း
paṭisārambhanā = ပြန်လည် ပြိုင်ဆိုင်ခြင်း
paṭisārambhitattaṃ = ပြန်လည် ပြိုင်ဆိုင်ထားသော အဖြစ်
icchāgatā = အလိုရှိမှုသို့ ရောက်ခြင်း
atricchatā = အလွန်အကျွံ လိုချင်ခြင်း
mahicchatā = လိုချင်မှု ကြီးခြင်း
pāpicchatā = ယုတ်မာသော အလိုရှိခြင်း
asantuṭṭhitā = ရောင့်ရဲမှု မရှိခြင်း
siṅgaṃ = ကြွားလုံး ထုတ်မှု
siṅgāratā = ကြွားလုံး ထုတ်ခြင်း
cāturatā = လိမ္မာဟန် ပြခြင်း
cāturiyaṃ = လိမ္မာဟန် ပြသော အဖြစ်
parikkhattatā = ကြော့ရှင်းဟန် ပြခြင်း
pārikkhattiyaṃ = ကြော့ရှင်းဟန် ပြသော အဖြစ်
tintiṇaṃ = ငမ်းငမ်းတက် မြည်တမ်းမှု
tintiṇāyanā = ငမ်းငမ်းတက် မြည်တမ်းခြင်း
tintiṇāyitattaṃ = ငမ်းငမ်းတက် မြည်တမ်းထားသော အဖြစ်
cīvaramaṇḍanā = သင်္ကန်းကို အလှဆင်ခြင်း
pattamaṇḍanā = သပိတ်ကို အလှဆင်ခြင်း
senāsanamaṇḍanā = ကျောင်းအိပ်ရာနေရာကို အလှဆင်ခြင်း
maṇḍanā = အလှဆင်ခြင်း
vibhūsanā = တန်ဆာဆင်ခြင်း
keḷanā = ကစားခြင်း
parikeḷanā = အမျိုးမျိုး ကစားခြင်း
giddhikatā = မက်မောခြင်း
giddhikattaṃ = မက်မောထားသော အဖြစ်
capalatā = ပေါ့ပျက်ခြင်း
cāpalyaṃ = ပေါ့ပျက်မှု
vipaccanīkasātatā = ဆန့်ကျင်ခြင်း၌ နှစ်သက်ခြင်း
anādariyatā = မလေးစားသော သဘော
agāravatā = ရိုသေမှု မရှိခြင်း
arati = မမွေ့လျော်မှု
aratitā = မမွေ့လျော်သော အဖြစ်
anabhirati = မပျော်မွေ့ခြင်း
anabhiramaṇā = မပျော်မွေ့နေခြင်း
ukkaṇṭhitā = ငြီးငွေ့ခြင်း
paritassitā = ပူပန်ခြင်း
tandī = ပျင်းရိငိုက်မျဉ်းမှု
tandiyanā = ပျင်းရိငိုက်မျဉ်းခြင်း
tandimanakatā = ပျင်းရိငိုက်မျဉ်းသော စိတ် ရှိခြင်း
ālasyaṃ = ပျင်းရိခြင်း
ālasyāyanā = ပျင်းရိနေခြင်း
ālasyāyitattaṃ = ပျင်းရိထားသော အဖြစ်
kāyassa jambhanā = ကိုယ်၏ သမ်းဝေခြင်း
vijambhanā = အကြိမ်ကြိမ် သမ်းဝေခြင်း
ānamanā = ကိုင်းညွတ်ခြင်း
vinamanā = အမျိုးမျိုး ကိုင်းညွတ်ခြင်း
sannamanā = ကွေးညွတ်ခြင်း
paṇamanā = ရှေ့သို့ ညွတ်ခြင်း
byādhiyakaṃ = ဖျားနာသကဲ့သို့ ဖြစ်ခြင်း
bhuttāvissa bhattamucchā = စားပြီးသူ၏ အစာကြောင့် မိန်းမောခြင်း
bhattakilamatho = အစာကြောင့် ပင်ပန်းခြင်း
bhattapariḷāho = အစာကြောင့် ပူလောင်ခြင်း
kāyaduṭṭhullaṃ = ကိုယ် လေးလံခြင်း
bhākuṭitā = မျက်မှောင် ကြုတ်ခြင်း
bhākuṭiyaṃ = မျက်မှောင် ကြုတ်ထားသော အဖြစ်
kuhanā = လှည့်ဖြား ဟန်ဆောင်မှု
kuhāyanā = လှည့်ဖြား ဟန်ဆောင်ခြင်း
kuhitattaṃ = လှည့်ဖြား ဟန်ဆောင်ထားသော အဖြစ်
ālapanā = စကား စ၍ ပြောခြင်း
lapanā = ချော့မော့ ပြောဆိုခြင်း
sallapanā = ရင်းနှီးစွာ ပြောဆိုခြင်း
ullapanā = မြှောက်ပင့် ပြောဆိုခြင်း
samullapanā = အလွန် မြှောက်ပင့် ပြောဆိုခြင်း
unnahanā = ချည်နှောင်သကဲ့သို့ ပြောခြင်း
samunnahanā = အလွန် ချည်နှောင်သကဲ့သို့ ပြောခြင်း
ukkācanā = ချီးမွမ်း ပြောဆိုခြင်း
samukkācanā = အလွန် ချီးမွမ်း ပြောဆိုခြင်း
anuppiyabhāṇitā = နားဝင်ချိုအောင် ပြောခြင်း
cāṭukamyatā = ဖားယားလိုခြင်း
muggasūpyatā = ပဲဟင်းကဲ့သို့ အမှန်အမှား ရောယှက် ပြောခြင်း
pāribhaṭayatā = ကလေးထိန်းသကဲ့သို့ ချော့မော့ခြင်း
nimittaṃ = အရိပ်အမြွက် ပြခြင်း
nimittakammaṃ = အရိပ်အမြွက် ပြုခြင်း
obhāso = သွယ်ဝိုက် ပြောခြင်း
obhāsakammaṃ = သွယ်ဝိုက် ပြောဆိုမှု ပြုခြင်း
sāmantajappā = အနီးအနား စကား ပြောခြင်း
parikathā = ပတ်လည် စကား ပြောခြင်း
akkosanā = ဆဲရေးခြင်း
vambhanā = နှိမ့်ချ ပြောခြင်း
garahaṇā = ကဲ့ရဲ့ခြင်း
ukkhepanā = မြှောက်ပင့်ခြင်း
samukkhepanā = အလွန် မြှောက်ပင့်ခြင်း
khipanā = ပစ်ချခြင်း
saṅkhipanā = အလွန် ပစ်ချခြင်း
pāpanā = အသရေဖျက်ခြင်း
sampāpanā = အလွန် အသရေဖျက်ခြင်း
avaṇṇahārikā = ကဲ့ရဲ့ သတင်း ဆောင်ခြင်း
parapiṭṭhimaṃsikatā = ကွယ်ရာတွင် အတင်းပြောခြင်း
eṭṭhi = ရှာခြင်း
gaveṭṭhi = စုံစမ်းခြင်း
pariyeṭṭhi = အနှံ့ ရှာခြင်း
esanā = ရှာမှီးခြင်း
gavesanā = စုံစမ်း ရှာမှီးခြင်း
pariyesanā = အနှံ့ ရှာမှီးခြင်း
omāno = ယုတ်ညံ့ဟု ထင်မှတ်မှု
omaññanā = ယုတ်ညံ့ဟု ထင်မှတ်ခြင်း
omaññitattaṃ = ယုတ်ညံ့ဟု ထင်မှတ်ထားသော အဖြစ်
hīḷanā = မိမိကိုယ်ကို နှိမ့်ချခြင်း
ohīḷanā = မိမိကိုယ်ကို အလွန် နှိမ့်ချခြင်း
ohīḷitattaṃ = မိမိကိုယ်ကို နှိမ့်ချထားသော အဖြစ်
attuññā = မိမိကိုယ်ကို အထင်သေးခြင်း
attavaññā = မိမိကိုယ်ကို လျစ်လျူရှုခြင်း
attaparibhavo = မိမိကိုယ်ကို စော်ကားခြင်း
upanāho = ရန်ငြိုး သိုထားမှု
upanayhanā = ရန်ငြိုး သိုထားခြင်း
upanayhitattaṃ = ရန်ငြိုး သိုထားသော အဖြစ်
anusaṃsandanā = ရန်ငြိုးကို ဆက်စပ်ထားခြင်း
anuppabandhanā = ရန်ငြိုးကို ဆက်တိုက် ဖွဲ့ထားခြင်း
daḷhīkammaṃ kodhassa = အမျက်ဒေါသကို ခိုင်မြဲအောင် ပြုခြင်း
makkho = ကျေးဇူး ချေဖျက်မှု
makkhāyanā = ကျေးဇူး ချေဖျက်ခြင်း
makkhāyitattaṃ = ကျေးဇူး ချေဖျက်ထားသော အဖြစ်
niṭṭhuriyaṃ = ရက်စက်ခြင်း
niṭṭhuriyakammaṃ = ရက်စက်စွာ ပြုခြင်း
paḷāso = တုပြိုင်မှု
paḷāsāyanā = တုပြိုင်ခြင်း
paḷāsāhāro = တုပြိုင်မှုကို ဆောင်ခြင်း
vivādaṭṭhānaṃ = အငြင်းပွားရာ အကြောင်း
yugaggāho = တန်းတူ ဆွဲကိုင်ခြင်း
appaṭinissaggo = မစွန့်လွှတ်ခြင်း
māyā = လှည့်စားတတ်ခြင်း
māyāvitā = လှည့်စားတတ်သော အဖြစ်
accāsarā = အပြစ်ကို ကျော်လွှားခြင်း
vañcanā = လိမ်လည်ခြင်း
nikati = ကောက်ကျစ်ခြင်း
vikiraṇā = ဖုံးကွယ်ရန် ဖြန့်ကြဲခြင်း
pariharaṇā = ရှောင်တိမ်းခြင်း
gūhanā = ဝှက်ထားခြင်း
parigūhanā = အနှံ့ ဝှက်ထားခြင်း
chādanā = ဖုံးခြင်း
paṭicchādanā = ဖုံးကွယ်ခြင်း
anuttānīkammaṃ = ထင်ရှားအောင် မပြုခြင်း
anāvikammaṃ = ပေါ်လွင်အောင် မပြုခြင်း
vocchādanā = ကောင်းစွာ ဖုံးအုပ်ခြင်း
pāpakiriyā = ယုတ်မာသော အမှုကို ပြုခြင်း
saṭhaṃ = စဉ်းလဲမှု
saṭhatā = စဉ်းလဲခြင်း
sāṭheyyaṃ = စဉ်းလဲသော အဖြစ်
kakkaratā = ကောက်ကွေးခြင်း
kakkariyaṃ = ကောက်ကွေးသော အဖြစ်
bhavasineho = ဘဝကို ချစ်ခင်မှု
anajjavo = မဖြောင့်မတ်မှု
anajjavatā = မဖြောင့်မတ်သော အဖြစ်
jimhatā = ကောက်ကျစ်သော အဖြစ်
vaṅkatā = ကွေးကောက်ခြင်း
kuṭilatā = တွန့်လိမ်ခြင်း
amaddavatā = မနူးညံ့သော အဖြစ်
kakkhaḷatā = ကြမ်းတမ်းသော အဖြစ်
kaṭhinatā = မာကျောခြင်း
akkhanti = မသည်းခံခြင်း
akkhamanatā = မသည်းခံနိုင်သော အဖြစ်
anadhivāsanatā = သည်းမခံနိုင်ခြင်း
asaṇhavācatā = စကား မပြေပြစ်ခြင်း
asakhilavācatā = စကား မချိုမြိန်ခြင်း
pharusavācatā = စကား ကြမ်းတမ်းခြင်း
uññā = အထင်သေးခြင်း
avaññā = လျစ်လျူရှုခြင်း
paribhavo = စော်ကားခြင်း
randhagavesitā = အပြစ်အနာအဆာ ရှာခြင်း
upārambho = အပြစ်ရှာမှု
anupārambho = အဖန်ဖန် အပြစ်ရှာမှု
upārambhanā = အပြစ်ရှာခြင်း
anupārambhanā = အဖန်ဖန် အပြစ်ရှာခြင်း
anupārambhitattaṃ = အဖန်ဖန် အပြစ်ရှာထားသော အဖြစ်
adassanakamyatā = မဖူးမြင်လိုခြင်း
adaṭṭhukamyatā = မတွေ့မြင်လိုခြင်း
asametukamyatā = မဆုံလိုခြင်း
asamāgantukamyatā = မပေါင်းဆုံလိုခြင်း
asotukamyatā = မနာကြားလိုခြင်း
asavanakamyatā = နားမထောင်လိုခြင်း
anuggahetukamyatā = မသင်ယူလိုခြင်း
adhāretukamyatā = မဆောင်ထားလိုခြင်း
assaddhiyaṃ = ယုံကြည်မှု မရှိခြင်း
assaddahanā = မယုံကြည်ခြင်း
anokappanā = သက်ဝင်၍ မယုံကြည်ခြင်း
anabhippasādo = ကြည်ညိုလေးစားခြင်း မရှိခြင်း
anaddā = အလေးဂရု မပြုခြင်း
anaddāyanā = အလေးဂရု မပြုနေခြင်း
anaddāyitattaṃ = အလေးဂရု မပြုထားသော အဖြစ်
asīlyaṃ = ယဉ်ကျေးသော အလေ့ မရှိခြင်း
acittīkāro = အလေးမထားခြင်း
paṭisevanā = ပြန်လည် ပေါင်းသင်းခြင်း
sampavaṅkatā = ညွတ်ကိုင်းခြင်း
āvaṭṭanā = လှည့်ခြင်း
anāvaṭṭanā = အဖန်ဖန် လှည့်ခြင်း
ābhogo = စိတ်ညွတ်ခြင်း
samannāhāro = စိတ်ကို ဆောင်ခြင်း
manasikāro = နှလုံးသွင်းခြင်း
bhayaṃ = ကြောက်ခြင်း
bhayānakaṃ = ကြောက်မက်ဖွယ် ဖြစ်ခြင်း
lomahaṃso = ကြက်သီးမွေးညင်း ထခြင်း
cetaso utrāso = စိတ်၏ ထိတ်လန့်ခြင်း
sañjānanā = မှတ်သိခြင်း
sañjānitattaṃ = မှတ်သိထားသော အဖြစ်
agati = အဂတိ
agatigamanaṃ = အဂတိ လိုက်ခြင်း
chandagamanaṃ = ဆန္ဒ အဂတိ လိုက်ခြင်း
vaggagamanaṃ = ဂိုဏ်းဖွဲ့၍ လိုက်ခြင်း
vārigamanaṃ = ရေကဲ့သို့ စီးဆင်း လိုက်ခြင်း
saññāvipariyāso = မှတ်သိမှု ပြောင်းပြန်
cittavipariyāso = စိတ် ပြောင်းပြန်
diṭṭhivipariyāso = အယူ ပြောင်းပြန်
rāgo = ရာဂ
sārāgo = တပ်မက်ခြင်း
gehasitaṃ cetasikaṃ sātaṃ = လောကီ အိမ်ရာကို မှီသော စိတ်၌ ဖြစ်သော ချမ်းသာမှု
cetasikaṃ sukhaṃ = စိတ်၌ ဖြစ်သော သာယာမှု
cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ = စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ချမ်းသာ သာယာစွာ ခံစားခြင်း
cetosamphassajā sātā sukhā vedanā = စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ချမ်းသာ သာယာသော ခံစားမှု
gehasitaṃ cetasikaṃ asātaṃ = လောကီ အိမ်ရာကို မှီသော စိတ်၌ ဖြစ်သော မချမ်းသာမှု
cetasikaṃ dukkhaṃ = စိတ်၌ ဖြစ်သော နာကျင်မှု
cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ = စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မချမ်းသာ နာကျင်စွာ ခံစားခြင်း
cetosamphassajā asātā dukkhā vedanā = စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မချမ်းသာ နာကျင်သော ခံစားမှု
gehasitaṃ cetasikaṃ neva sātaṃ nāsātaṃ = လောကီ အိမ်ရာကို မှီသော စိတ်၌ ဖြစ်သော ချမ်းသာမှုလည်း မဟုတ်၊ မချမ်းသာမှုလည်း မဟုတ်သော
cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ = စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မနာကျင် မသာယာစွာ ခံစားခြင်း
cetosamphassajā adukkhamasukhā vedanā = စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မနာကျင် မသာယာသော ခံစားမှု
cittassa āghāto = စိတ်၏ ရန်ငြိုးဖွဲ့ခြင်း
gehasito takko = လောကီ အိမ်ရာကို မှီသော တွေးတောခြင်း
imassa vā pūtikāyassa bāhirānaṃ vā parikkhārānaṃ maṇḍanā = ဤပုပ်စပ်သော ကိုယ်ကိုဖြစ်စေ၊ ပြင်ပ အသုံးအဆောင်တို့ကိုဖြစ်စေ အလှဆင်ခြင်း
āmisassa eṭṭhi = ပစ္စည်းကို ရှာခြင်း
gehasito rāgo = လောကီ အိမ်ရာကို မှီသော ရာဂ
aṭṭhapanā = ခိုင်ခိုင်မြဲမြဲ တည်ထားခြင်း
aṭhapanā = ပြင်ဆင်ထားခြင်း
ṭhapanā = တည်ထားခြင်း
saṇṭhapanā = ကောင်းစွာ တည်ထားခြင်း

### Editorial references in variant brackets
dha. sa. = သဘောတရားများကို စုစည်းရေတွက်ခြင်း
dī. ni. = ဒီဃနိကာယ်
a. ni. = အင်္ဂုတ္တရနိကာယ်

### Editorial notes in brackets (new)
pāḷiyā ṭīkā passitabbā = ပါဠိ၏ ဋီကာကို ကြည့်ပါ
(kumbha + īra + a = bhaya) = (kumbha + īra + a = bhaya)

### Mada bases (X-mado = «Xကြောင့် မူးယစ်မှု»; Xṃ paṭicca = «Xကို စွဲ၍»)
jāti = ဇာတိ
gotta = အမျိုးအနွယ်
ārogya = အနာကင်းခြင်း
yobbana = ပျိုရွယ်ခြင်း
jīvita = အသက်ရှင်ခြင်း
lābha = လာဘ်
sakkāra = အပူဇော်ခံရခြင်း
garukāra = အလေးပြုခံရခြင်း
purekkhāra = ရှေ့တန်းတင်ခံရခြင်း
parivāra = အခြံအရံ
bhoga = စည်းစိမ်ဥစ္စာ
vaṇṇa = အဆင်းလှခြင်း
suta = အကြားအမြင်
paṭibhāna = လျင်မြန်သော ဉာဏ်
rattaññu = ရဟန်းဝါ ကြာမြင့်ခြင်း
piṇḍapātika = ဆွမ်းခံ ဓုတင် ဆောင်ခြင်း
anavaññāta = အထင်မသေးခံရခြင်း
iriyāpatha = ကိုယ်ဟန် အမူအရာ
iddhi = တန်ခိုး
yasa = ကျော်ကြားမှု
sīla = သီလ
jhāna = ဈာန်
sippa = အတတ်ပညာ
āroha = အရပ်အမောင်း မြင့်ခြင်း
pariṇāha = ကိုယ်လုံး ပြည့်ဖြိုးခြင်း
saṇṭhāna = ကိုယ်ဟန် ပုံသဏ္ဌာန် လှပခြင်း
pāripūri = ကိုယ်အင်္ဂါ ပြည့်စုံခြင်း

### Māna (new forms)
seyyassa = သာလွန်သူ ဖြစ်လျက်
sadisassa = တူညီသူ ဖြစ်လျက်
hīnassa = ယုတ်ညံ့သူ ဖြစ်လျက်

### Names (new unless marked pi-1)
mado = မူးယစ်မှု
pamādo = မေ့လျော့မှု
thambho = တောင့်တင်းမှု
sārambho = ပြိုင်ဆိုင်မှု
atricchatā = အလွန်အကျွံ လိုချင်ခြင်း
mahicchatā = လိုချင်မှု ကြီးခြင်း
pāpicchatā = ယုတ်မာသော အလိုရှိခြင်း
siṅgaṃ = ကြွားလုံး ထုတ်မှု
tintiṇaṃ = ငမ်းငမ်းတက် မြည်တမ်းမှု
cāpalyaṃ = ပေါ့ပျက်မှု
asabhāgavutti = မလျော်ကန်သော ဆက်ဆံမှု
arati = မမွေ့လျော်မှု
tandī = ပျင်းရိငိုက်မျဉ်းမှု
vijambhitā = သမ်းဝေ ကိုင်းညွတ်မှု
bhattasammado = အစာကြောင့် မူးမော့မှု
cetaso ca līnattaṃ = စိတ်၏ တွန့်ဆုတ်နေမှု
kuhanā = လှည့်ဖြား ဟန်ဆောင်မှု
lapanā = ချော့မော့ ပြောဆိုခြင်း
nemittikatā = အရိပ်အမြွက် ပြတတ်ခြင်း
nippesikatā = နှိပ်ကွပ် ပြောဆိုတတ်ခြင်း
lābhena lābhaṃ nijigīsanatā = လာဘ်ဖြင့် လာဘ်ကို ရှာခြင်း
māno = မာန
atimāno = အလွန် မာနထားမှု
mānātimāno = မာနနှင့် အလွန် မာနထားမှု
omāno = ယုတ်ညံ့ဟု ထင်မှတ်မှု
adhimāno = လွန်ကဲစွာ ထင်မှတ်သော မာန
asmimāno = ငါ ရှိ၏ဟူသော မာန
micchāmāno = မှားယွင်းသော မာန
ñātivitakko = ဆွေမျိုးကို စတင်ကြံစည်မှု
janapadavitakko = ဇာတိ ဇနပုဒ်ကို စတင်ကြံစည်မှု
amaravitakko = မသေခြင်းကို ရည်ရွယ်သော စတင်ကြံစည်မှု
parānuddayatāpaṭisaṃyutto vitakko = သူတစ်ပါးကို စာနာခြင်းနှင့် စပ်ယှဉ်သော စတင်ကြံစည်မှု
lābhasakkārasilokapaṭisaṃyutto vitakko = လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှုတို့နှင့် စပ်ယှဉ်သော စတင်ကြံစည်မှု
lābhādipaṭisaṃyutto vitakko = လာဘ် စသည်တို့နှင့် စပ်ယှဉ်သော စတင်ကြံစည်မှု
anavaññattipaṭisaṃyutto vitakko = အထင်မသေးခံရခြင်းနှင့် စပ်ယှဉ်သော စတင်ကြံစည်မှု
kodho = အမျက်ဒေါသ
upanāho = ရန်ငြိုး သိုထားမှု
makkho = ကျေးဇူး ချေဖျက်မှု
paḷāso = တုပြိုင်မှု
issā = ငြူစူမှု
macchariyaṃ = ဝန်တိုမှု
māyā = လှည့်စားတတ်ခြင်း
sāṭheyyaṃ = စဉ်းလဲသော အဖြစ်
avijjā = အမှန်ကို မသိမှု
bhavataṇhā = ဘဝကို တပ်မက်မှု
bhavadiṭṭhi = ဘဝဆိုင်ရာ အယူ
vibhavadiṭṭhi = ဘဝ ပျောက်ကွယ်ခြင်းဆိုင်ရာ အယူ
sassatadiṭṭhi = မြဲသည်ဟူသော အယူ
ucchedadiṭṭhi = ပြတ်သည်ဟူသော အယူ
antavādiṭṭhi = အဆုံး ရှိသည်ဟူသော အယူ
anantavādiṭṭhi = အဆုံး မရှိဟူသော အယူ
pubbantānudiṭṭhi = အတိတ်ကာလကို အစွဲပြုသော အယူ
aparantānudiṭṭhi = အနာဂတ်ကာလကို အစွဲပြုသော အယူ
ahirikaṃ = ဒုစရိုက်ကို မရှက်မှု
anottappaṃ = ဒုစရိုက်ကို မကြောက်ရွံ့မှု
dovacassatā = သွန်သင်ချက်ကို နားမထောင်ခြင်း
pāpamittatā = မိတ်ဆွေဆိုးနှင့် ပေါင်းသင်းခြင်း
anajjavo = မဖြောင့်မတ်မှု
amaddavo = မနူးညံ့မှု
akkhanti = မသည်းခံခြင်း
asoraccaṃ = မယဉ်ကျေးခြင်း
asākhalyaṃ = စကား မချိုသာခြင်း
appaṭisanthāro = ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း မရှိခြင်း
indriyesu aguttadvāratā = အာရုံခံ အင်္ဂါတို့၏ တံခါးကို မစောင့်ထိန်းခြင်း
bhojane amattaññutā = အစားအစာ၌ အတိုင်းအရှည်ကို မသိခြင်း
muṭṭhassaccaṃ = သတိလစ်ခြင်း
asampajaññaṃ = ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိခြင်း
sīlavipatti = သီလ ပျက်စီးခြင်း
diṭṭhivipatti = အယူ ပျက်စီးခြင်း
ajjhattasaṃyojanaṃ = အတွင်းပိုင်း နှောင်ကြိုး
bahiddhāsaṃyojanaṃ = အပြင်ပိုင်း နှောင်ကြိုး
lobho = လောဘ
doso = ဒေါသ
moho = မောဟ
kāmavitakko = ကာမကို စတင်ကြံစည်မှု
byāpādavitakko = ဖျက်ဆီးလိုစိတ်ဆိုင်ရာ စတင်ကြံစည်မှု
vihiṃsāvitakko = ညှဉ်းပန်းမှုဆိုင်ရာ စတင်ကြံစည်မှု
kāmasaññā = ကာမကို မှတ်သိမှု
byāpādasaññā = ဖျက်ဆီးလိုစိတ်ဆိုင်ရာ မှတ်သိမှု
vihiṃsāsaññā = ညှဉ်းပန်းမှုဆိုင်ရာ မှတ်သိမှု
kāmadhātu = ကာမ ဓာတ်
byāpādadhātu = ဖျက်ဆီးလိုစိတ် ဓာတ်
vihiṃsādhātu = ညှဉ်းပန်းမှု ဓာတ်
kāyaduccaritaṃ = ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်
vacīduccaritaṃ = နှုတ်ဖြင့် ပြုသော ဒုစရိုက်
manoduccaritaṃ = မနောဖြင့် ပြုသော ဒုစရိုက်
pāṇātipāto = သူ့အသက်ကို သတ်ခြင်း
adinnādānaṃ = မပေးသည်ကို ယူခြင်း
kāmesumicchācāro = ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း
musāvādo = မုသား ပြောခြင်း
pisuṇā vācā = ကုန်းတိုက်သော စကား
pharusā vācā = ကြမ်းတမ်းသော စကား
samphappalāpo = အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား
abhijjhā = သူ့ဥစ္စာကို လိုချင်ခြင်း
byāpādo = ဖျက်ဆီးလိုစိတ်
micchādiṭṭhi = မှားယွင်းသော အယူ
akusalaṃ kāyakammaṃ = အကုသိုလ် ကိုယ်ဖြင့် ပြုသော ကံ
kāmāsavo = ကာမ စိတ်အစွန်းအထင်း
bhavāsavo = ဘဝ စိတ်အစွန်းအထင်း
diṭṭhāsavo = အယူ စိတ်အစွန်းအထင်း
avijjāsavo = အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း
sakkāyadiṭṭhi = ကိုယ်ကို အတ္တဟု ယူဆသော အယူ
vicikicchā = ယုံမှားမှု
sīlabbataparāmāso = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု
kāmataṇhā = ကာမကို တပ်မက်မှု
vibhavataṇhā = ဘဝ ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု
rūpataṇhā = သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု
arūpataṇhā = ရုပ်မရှိသော ဘဝကို တပ်မက်မှု
rūpataṇhā@sense = အဆင်းအရောင်ကို တပ်မက်မှု
nirodhataṇhā = ချုပ်ငြိမ်းခြင်းကို တပ်မက်မှု
saddataṇhā = အသံကို တပ်မက်မှု
gandhataṇhā = အနံ့ကို တပ်မက်မှု
rasataṇhā = အရသာကို တပ်မက်မှု
phoṭṭhabbataṇhā = အထိအတွေ့ကို တပ်မက်မှု
dhammataṇhā = သဘောတရားကို တပ်မက်မှု
kāmesanā = ကာမကို ရှာမှီးမှု
bhavesanā = ဘဝကို ရှာမှီးမှု
brahmacariyesanā = မြတ်သော အကျင့်ကို ရှာမှီးမှု
jātibhayaṃ = မွေးဖွားခြင်း ဘေး
jarābhayaṃ = အိုခြင်း ဘေး
maraṇabhayaṃ = သေခြင်း ဘေး
byādhibhayaṃ = ဖျားနာခြင်း ဘေး
rājabhayaṃ = မင်း ဘေး
corabhayaṃ = ခိုးသူ ဘေး
aggibhayaṃ = မီး ဘေး
udakabhayaṃ = ရေ ဘေး
ūmibhayaṃ = လှိုင်း ဘေး
kumbhīlabhayaṃ = မိကျောင်း ဘေး
āvaṭṭabhayaṃ = ဝဲဂယက် ဘေး
susukābhayaṃ = ငါးဆိုး ဘေး
attānuvādabhayaṃ = မိမိကိုယ်ကို အပြစ်တင်ခြင်း ဘေး
parānuvādabhayaṃ = သူတစ်ပါး အပြစ်တင်ခြင်း ဘေး
daṇḍabhayaṃ = ဒဏ်ခတ်ခံရခြင်း ဘေး
duggatibhayaṃ = ဆိုးသော လားရာ ဘေး
ājīvakabhayaṃ = အသက်မွေးဝမ်းကျောင်းမှု ဘေး
asilokabhayaṃ = အသရေပျက်ခြင်း ဘေး
parisasārajjabhayaṃ = ပရိသတ်ကို ရွံ့ကြောက်ခြင်း ဘေး
kāyavisamaṃ = ကိုယ်၏ ဖောက်ပြန်မှု
vacīvisamaṃ = နှုတ်၏ ဖောက်ပြန်မှု
manovisamaṃ = မနော၏ ဖောက်ပြန်မှု
rāgaggi = ရာဂ မီး
dosaggi = ဒေါသ မီး
mohaggi = မောဟ မီး
rāgakasāvo = ရာဂ အမည်းအစက်
dosakasāvo = ဒေါသ အမည်းအစက်
mohakasāvo = မောဟ အမည်းအစက်
kāyakasāvo = ကိုယ်၏ အမည်းအစက်
vacīkasāvo = နှုတ်၏ အမည်းအစက်
manokasāvo = မနော၏ အမည်းအစက်
assādadiṭṭhi = သာယာမှုဆိုင်ရာ အယူ
attānudiṭṭhi = အတ္တဟု အဖန်ဖန် ရှုမြင်သော အယူ
vihesā = နှိပ်စက်မှု
adhammacariyā = တရားနှင့် မညီသော အကျင့်
nānattasaññā = အမျိုးမျိုးသော မှတ်သိမှု
uddhaccaṃ = ယောက်ယက်ခတ်မှု
kosajjaṃ = ပျင်းရိမှု
asantuṭṭhitā = ရောင့်ရဲမှု မရှိခြင်း
asampajaññatā = ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိသော အဖြစ်
anādariyaṃ = မလေးစားခြင်း
assaddhiyaṃ = ယုံကြည်မှု မရှိခြင်း
avadaññutā = ပေးကမ်းရန် မလိုလားခြင်း
asaṃvaro = မစောင့်စည်းခြင်း
dussīlyaṃ = သီလ ပျက်ခြင်း
ariyānaṃ adassanakamyatā = အရိယာတို့ကို မဖူးမြင်လိုခြင်း
saddhammaṃ asotukamyatā = သူတော်ကောင်းတရားကို မနာကြားလိုခြင်း
upārambhacittatā = အပြစ်ရှာလိုသော စိတ် ရှိခြင်း
cetaso vikkhepo = စိတ်၏ ပျံ့လွင့်ခြင်း
ayoniso manasikāro = မသင့်လျော်စွာ နှလုံးသွင်းခြင်း
kummaggasevanā = လမ်းမှားကို မှီဝဲခြင်း
kummaggo = လမ်းမှား
saddhammo = သူတော်ကောင်းတရား
upārambho = အပြစ်ရှာမှု
kāmupādānaṃ = ကာမ စွဲလမ်းမှု
diṭṭhupādānaṃ = အယူ စွဲလမ်းမှု
sīlabbatupādānaṃ = သီလ အကျင့်ဝတ် စွဲလမ်းမှု
attavādupādānaṃ = အတ္တဟူသော ဝါဒ စွဲလမ်းမှု
kāmacchando = ကာမကို လိုလားမှု
rūparāgo = သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ
arūparāgo = ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ
āvāsamacchariyaṃ = နေရာထိုင်ခင်း ဝန်တိုမှု
kulamacchariyaṃ = ဒါယကာ အိမ်ဝန်း ဝန်တိုမှု
lābhamacchariyaṃ = လာဘ် ဝန်တိုမှု
vaṇṇamacchariyaṃ = ဂုဏ်ကျေးဇူး ဝန်တိုမှု
dhammamacchariyaṃ = တရား ဝန်တိုမှု
rāgasaṅgo = ရာဂ တွယ်ငြိမှု
dosasaṅgo = ဒေါသ တွယ်ငြိမှု
mohasaṅgo = မောဟ တွယ်ငြိမှု
mānasaṅgo = မာန တွယ်ငြိမှု
diṭṭhisaṅgo = အယူ တွယ်ငြိမှု
rāgasallaṃ = ရာဂ ငြောင့်
dosasallaṃ = ဒေါသ ငြောင့်
mohasallaṃ = မောဟ ငြောင့်
mānasallaṃ = မာန ငြောင့်
diṭṭhisallaṃ = အယူ ငြောင့်
kāmacchandanīvaraṇaṃ = ကာမကို လိုလားမှု အတားအဆီး
byāpādanīvaraṇaṃ = ဖျက်ဆီးလိုစိတ် အတားအဆီး
thinamiddhanīvaraṇaṃ = ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု အတားအဆီး
uddhaccakukkuccanīvaraṇaṃ = ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု အတားအဆီး
vicikicchānīvaraṇaṃ = ယုံမှားမှု အတားအဆီး
surāmerayamajjapamādaṭṭhānā = မေ့လျော့ခြင်း၏ အကြောင်း ဖြစ်သော သေရည်သေရက် သောက်ခြင်း
ñātibyasanaṃ = ဆွေမျိုး ပျက်စီးခြင်း
bhogabyasanaṃ = စည်းစိမ်ဥစ္စာ ပျက်စီးခြင်း
rogabyasanaṃ = ကျန်းမာရေး ပျက်စီးခြင်း
sīlabyasanaṃ = သီလ ပျက်စီးခြင်း
diṭṭhibyasanaṃ = အယူ ပျက်စီးခြင်း
sandiṭṭhiparāmāsitā = မိမိ အယူကိုသာ စွဲကိုင်ခြင်း
kammārāmatā = အလုပ်ကို နှစ်သက်ခြင်း
bhassārāmatā = စကားပြောခြင်းကို နှစ်သက်ခြင်း
niddārāmatā = အိပ်ခြင်းကို နှစ်သက်ခြင်း
saṅgaṇikārāmatā = အပေါင်းအသင်းကို နှစ်သက်ခြင်း
saṃsaggārāmatā = ရောနှောခြင်းကို နှစ်သက်ခြင်း
papañcārāmatā = ချဲ့ထွင်ခြင်းကို နှစ်သက်ခြင်း
kāmarāgānusayo = ကာမရာဂ ကိန်းအောင်းခြင်း
paṭighānusayo = မုန်းတီးမှု ကိန်းအောင်းခြင်း
mānānusayo = မာန ကိန်းအောင်းခြင်း
diṭṭhānusayo = အယူ ကိန်းအောင်းခြင်း
vicikicchānusayo = ယုံမှားမှု ကိန်းအောင်းခြင်း
bhavarāgānusayo = ဘဝရာဂ ကိန်းအောင်းခြင်း
avijjānusayo = အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း
kāmarāgasaṃyojanaṃ = ကာမရာဂ နှောင်ကြိုး
paṭighasaṃyojanaṃ = မုန်းတီးမှု နှောင်ကြိုး
mānasaṃyojanaṃ = မာန နှောင်ကြိုး
diṭṭhisaṃyojanaṃ = အယူ နှောင်ကြိုး
vicikicchāsaṃyojanaṃ = ယုံမှားမှု နှောင်ကြိုး
bhavarāgasaṃyojanaṃ = ဘဝရာဂ နှောင်ကြိုး
avijjāsaṃyojanaṃ = အမှန်ကို မသိမှု နှောင်ကြိုး
sīlabbataparāmāsasaṃyojanaṃ = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု နှောင်ကြိုး
issāsaṃyojanaṃ = ငြူစူမှု နှောင်ကြိုး
macchariyasaṃyojanaṃ = ဝန်တိုမှု နှောင်ကြိုး
kāmarāgapariyuṭṭhānaṃ = ကာမရာဂ ထကြွခြင်း
paṭighapariyuṭṭhānaṃ = မုန်းတီးမှု ထကြွခြင်း
mānapariyuṭṭhānaṃ = မာန ထကြွခြင်း
diṭṭhipariyuṭṭhānaṃ = အယူ ထကြွခြင်း
vicikicchāpariyuṭṭhānaṃ = ယုံမှားမှု ထကြွခြင်း
bhavarāgapariyuṭṭhānaṃ = ဘဝရာဂ ထကြွခြင်း
avijjāpariyuṭṭhānaṃ = အမှန်ကို မသိမှု ထကြွခြင်း
diṭṭhi = အယူ
thinaṃ = ထိုင်းမှိုင်းမှု
micchāvācā = မှားယွင်းသော စကား
micchākammanto = မှားယွင်းသော အလုပ်
micchāājīvo = မှားယွင်းသော အသက်မွေးမှု
micchāvāyāmo = မှားယွင်းသော အားထုတ်မှု
micchāsati = မှားယွင်းသော သတိ
micchāsamādhi = မှားယွင်းသော သမာဓိ
micchāñāṇaṃ = မှားယွင်းသော ဉာဏ်
micchāvimutti = မှားယွင်းသော လွတ်မြောက်မှု
micchāsaṅkappo = မှားယွင်းသော ကြံစည်မှု

### Names (new)
akusalā kāyasañcetanā = အကုသိုလ် ကိုယ်၏ စေ့ဆော်ခြင်း
akusalā vacīsañcetanā = အကုသိုလ် နှုတ်၏ စေ့ဆော်ခြင်း
akusalā manosañcetanā = အကုသိုလ် မနော၏ စေ့ဆော်ခြင်း
dasavatthukā micchādiṭṭhi = အကြောင်းအရာ ဆယ်ပါး ရှိသော မှားယွင်းသော အယူ
dasavatthukā antaggāhikā diṭṭhi = အကြောင်းအရာ ဆယ်ပါး ရှိသော အစွန်းကို စွဲကိုင်သော အယူ
antaggāhikā diṭṭhi = အစွန်းကို စွဲကိုင်သော အယူ
aṭṭhasu lokadhammesu cittassa paṭighāto = လောကဓံ ရှစ်ပါးတို့၌ စိတ်၏ ထိခိုက်မှု
aṭṭha taṇhāvicaritasataṃ = တပ်မက်မှု၏ ဖြစ်ပုံ တစ်ရာ့ရှစ်ပါး
ariyā = အရိယာ
kiñcanaṃ = တွယ်ငြိရာ
aṅgaṇaṃ = အစွန်းအကွက်
malaṃ = အညစ်အကြေး
visamaṃ = ဖောက်ပြန်မှု
rūpataṇhā@sense = အဆင်းအရောင်ကို တပ်မက်မှု
navavidhā mānā = ကိုးမျိုးသော မာန
kāmarāgo = ကာမရာဂ
bhavarāgo = ဘဝရာဂ
akusalā saññā = အကုသိုလ် မှတ်သိမှု
gottamadādī = အမျိုးအနွယ်ကြောင့် မူးယစ်မှု စသည်
cattāro ganthādī = အထုံး လေးပါး စသည်
nava maññitādīni = ထင်မှတ်မှု ကိုးပါး စသည်
ajjhattikassa upādāya = အတွင်းကို မှီ၍
bāhirassa upādāya = အပြင်ကို မှီ၍

### Group nouns («N X» = «X N-ပါး»)
akusalamūlāni = အကုသိုလ်၏ အမြစ်
akusalavitakkā = အကုသိုလ် စတင်ကြံစည်မှု
akusalasaññā = အကုသိုလ် မှတ်သိမှု
akusaladhātuyo = အကုသိုလ် ဓာတ်
duccaritāni = ဒုစရိုက်
āsavā = စိတ်အစွန်းအထင်း
saṃyojanāni = နှောင်ကြိုး
taṇhā = တပ်မက်မှု
esanā = ရှာမှီးမှု
vidhā = နှိုင်းယှဉ် ချိန်ဆမှု
bhayāni = ဘေး
tamāni = အမှောင်
titthāyatanāni = အယူဝါဒတို့၏ တည်ရာ
kiñcanā = တွယ်ငြိရာ
aṅgaṇāni = အစွန်းအကွက်
malāni = အညစ်အကြေး
visamāni = ဖောက်ပြန်မှု
aggī = မီး
kasāvā = အမည်းအစက်
ganthā = အထုံး
oghā = ရေအလျဉ်
yogā = ထမ်းပိုး
upādānāni = စွဲလမ်းမှု
taṇhuppādā = တပ်မက်မှု ဖြစ်ပေါ်ရာ
agatigamanāni = အဂတိ လိုက်ခြင်း
vipariyāsā = ပြောင်းပြန် ယူဆမှု
anariyavohārā = အရိယာ မဟုတ်သူတို့၏ ပြောဆိုမှု
diṭṭhiyo = အယူ
orambhāgiyāni saṃyojanāni = အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး
uddhambhāgiyāni saṃyojanāni = အထက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး
macchariyāni = ဝန်တိုမှု
saṅgā = တွယ်ငြိမှု
sallā = ငြောင့်
cetokhilā = စိတ်၏ ခက်ထန်မှု
cetaso vinibandhā = စိတ်ကို ချည်နှောင်ထားသော အရာ
cetasovinibandhā = စိတ်ကို ချည်နှောင်ထားသော အရာ
nīvaraṇāni = အတားအဆီး
kammāni ānantarikāni = ချက်ချင်း အကျိုးပေးသော ကံ
verā = ရန်
byasanā = ပျက်စီးခြင်း
akkhantiyā ādīnavā = မသည်းခံခြင်း၏ အပြစ်
diṭṭhadhammanibbānavādā = မျက်မှောက်ဘဝ၌ နိဗ္ဗာန်ဟု ဆိုသော ဝါဒ
vivādamūlāni = အငြင်းပွားမှု၏ အမြစ်
chandarāgā = လိုလားမှု ရာဂ
virodhavatthūni = ဆန့်ကျင်မှု၏ အကြောင်း
taṇhākāyā = တပ်မက်မှု အစု
agāravā = မရိုသေမှု
parihāniyā dhammā = ဆုတ်ယုတ်စေတတ်သော သဘောတရား
somanassupavicārā = ဝမ်းမြောက်ဖွယ်၌ စိတ် လှည့်လည်မှု
domanassupavicārā = စိတ်ဆင်းရဲဖွယ်၌ စိတ် လှည့်လည်မှု
upekkhupavicārā = လျစ်လျူရှုဖွယ်၌ စိတ် လှည့်လည်မှု
gehasitāni somanassāni = လောကီ အိမ်ရာကို မှီသော ဝမ်းမြောက်မှု
gehasitāni domanassāni = လောကီ အိမ်ရာကို မှီသော စိတ်ဆင်းရဲမှု
gehasitā upekkhā = လောကီ အိမ်ရာကို မှီသော ဥပေက္ခာ
anusayā = ကိန်းအောင်းခြင်း
pariyuṭṭhānāni = ထကြွခြင်း
asaddhammā = သူတော်ကောင်း မဟုတ်သူတို့၏ တရား
mānā = မာန
kilesavatthūni = ကိလေသာ အကြောင်းရင်း
kusītavatthūni = ပျင်းရိမှု၏ အကြောင်း
micchattā = မှားယွင်းမှု
purisadosā = လူ၏ အပြစ်
asaññīvādā = မှတ်သိမှု မရှိသော အတ္တကို ဆိုသော ဝါဒ
asaññivādā = မှတ်သိမှု မရှိသော အတ္တကို ဆိုသော ဝါဒ
nevasaññīnāsaññīvādā = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သော အတ္တကို ဆိုသော ဝါဒ
nevasaññināsaññivādā = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သော အတ္တကို ဆိုသော ဝါဒ
āghātavatthūni = ရန်ငြိုးဖွဲ့ခြင်း၏ အကြောင်း
purisamalāni = လူ၏ အညစ်အကြေး
navavidhā mānā = ကိုးမျိုးသော မာန
taṇhāmūlakā dhammā = တပ်မက်မှုကို အမြစ်ပြုသော သဘောတရား
iñjitāni = တုန်လှုပ်မှု
maññitāni = ထင်မှတ်မှု
phanditāni = လှုပ်ရှားမှု
papañcitāni = ချဲ့ထွင်မှု
saṅkhatāni = ပြုပြင်ထားမှု
akusalakammapathā = အကုသိုလ် ကံ လမ်းကြောင်း
taṇhāvicaritāni = တပ်မက်မှု၏ ဖြစ်ပုံ
diṭṭhigatāni = အယူမှား
lokadhammesu = လောကဓံ
sassatavādā = မြဲသည်ဟု ဆိုသော ဝါဒ
ekaccasassatikā = အချို့ မြဲသည်ဟု ဆိုသော ဝါဒ
antānantikā = အဆုံးနှင့် အဆုံးမဲ့ကို ဆိုသော ဝါဒ
amarāvikkhepikā = ငါးရှဉ့်ကဲ့သို့ လှည့်ပတ် ပြောသော ဝါဒ
adhiccasamuppannikā = အကြောင်းမဲ့ ဖြစ်ပေါ်သည်ဟု ဆိုသော ဝါဒ
saññīvādā = မှတ်သိမှု ရှိသော အတ္တကို ဆိုသော ဝါဒ
ucchedavādā = ပြတ်သည်ဟု ဆိုသော ဝါဒ

### Objects of «ārabbha / paṭisaṃyutta / sahagata» (new unless pi-1)
kāma = ကာမ
byāpāda = ဖျက်ဆီးလိုစိတ်
vihiṃsā = ညှဉ်းပန်းမှု
kāmadhātu = ကာမဘုံ
rūpadhātu = သိမ်မွေ့သော ရုပ်ဘုံ
arūpadhātu = ရုပ်မရှိသော ဘုံ
rūpadhātuarūpadhātu = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံ
bhavadiṭṭhi = ဘဝဆိုင်ရာ အယူ
ucchedadiṭṭhi = ပြတ်သည်ဟူသော အယူ
dukkarakāritā = ပြုနိုင်ခဲသော အကျင့်ကို ကျင့်ခြင်း
diṭṭhigata = အယူမှား
ñātake = ဆွေမျိုးတို့
janapadaṃ = ဇနပုဒ်
lābhasakkārasilokaṃ = လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှု
pubbantaṃ = အတိတ်ကာလ
aparantaṃ = အနာဂတ်ကာလ

### Māna bases (new)
jātiyā = ဇာတိဖြင့်
gottena = အမျိုးအနွယ်ဖြင့်
kolaputtiyena = အမျိုးကောင်းသား ဖြစ်ခြင်းဖြင့်
vaṇṇapokkharatāya = အဆင်းလှခြင်းဖြင့်
dhanena = ဥစ္စာဖြင့်
ajjhenena = စာပေ သင်ယူမှုဖြင့်
kammāyatanena = အလုပ်အကိုင်ဖြင့်
sippāyatanena = အတတ်ပညာဖြင့်
vijjāṭṭhānena = ပညာရပ်ဖြင့်
sutena = အကြားအမြင်ဖြင့်
paṭibhānena = လျင်မြန်သော ဉာဏ်ဖြင့်
aññataraññatarena vatthunā = တစ်ခုခုသော အကြောင်းဖြင့်

### Quoted views and statements (new)
sassato loko = လောကသည် မြဲ၏
asassato loko = လောကသည် မမြဲ
antavā loko = လောကသည် အဆုံး ရှိ၏
anantavā loko = လောကသည် အဆုံး မရှိ
taṃ jīvaṃ taṃ sarīraṃ = အသက်ကောင်သည်လည်း ထိုအရာပင်၊ ကိုယ်ခန္ဓာသည်လည်း ထိုအရာပင်
aññaṃ jīvaṃ aññaṃ sarīraṃ = အသက်ကောင်သည် တစ်ခြား၊ ကိုယ်ခန္ဓာသည် တစ်ခြား
hoti tathāgato paraṃ maraṇā = တထာဂတသည် သေပြီးနောက် ရှိ၏
na hoti tathāgato paraṃ maraṇā = တထာဂတသည် သေပြီးနောက် မရှိ
hoti ca na ca hoti tathāgato paraṃ maraṇā = တထာဂတသည် သေပြီးနောက် ရှိလည်း ရှိ၏၊ မရှိလည်း ဖြစ်၏
neva hoti na na hoti tathāgato paraṃ maraṇā = တထာဂတသည် သေပြီးနောက် ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်
bhavissati attā ca loko ca = အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း ဖြစ်လိမ့်မည်
na bhavissati attā ca loko ca = အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း ဖြစ်လိမ့်မည် မဟုတ်
sassato attā ca loko ca = အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း မြဲ၏
ucchijjissati attā ca loko ca = အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း ပြတ်စဲလိမ့်မည်
antavā attā ca loko ca = အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း အဆုံး ရှိ၏
anantavā attā ca loko ca = အတ္တသည်လည်းကောင်း၊ လောကသည်လည်းကောင်း အဆုံး မရှိ
seyyohamasmi = ငါသည် သာလွန်သူ ဖြစ်သည်
sadisohamasmi = ငါသည် တူညီသူ ဖြစ်သည်
hīnohamasmi = ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်
anatthaṃ me acari = ငါ့အား အကျိုးမဲ့ကို ပြုခဲ့ပြီ
anatthaṃ me carati = ငါ့အား အကျိုးမဲ့ကို ပြု၏
anatthaṃ me carissati = ငါ့အား အကျိုးမဲ့ကို ပြုလိမ့်မည်
piyassa me manāpassa anatthaṃ acari = ငါ ချစ်သော ငါ နှစ်သက်သူအား အကျိုးမဲ့ကို ပြုခဲ့ပြီ
anatthaṃ carati = အကျိုးမဲ့ကို ပြု၏
anatthaṃ carissati = အကျိုးမဲ့ကို ပြုလိမ့်မည်
appiyassa me amanāpassa atthaṃ acari = ငါ မချစ်သော ငါ မနှစ်သက်သူအား အကျိုးကို ပြုခဲ့ပြီ
atthaṃ carati = အကျိုးကို ပြု၏
atthaṃ carissati = အကျိုးကို ပြုလိမ့်မည်
nicca = မြဲ၏
sukha = ချမ်းသာ၏
attā = အတ္တ ဖြစ်၏
subha = တင့်တယ်၏
mā maṃ jaññā = ငါ့ကို မသိပါစေနှင့်
sīlena suddhi vatena suddhi sīlabbatena suddhi = None
sayaṅkataṃ sukhadukkhaṃ = ချမ်းသာ ဆင်းရဲကို မိမိ ပြုသည်
paraṅkataṃ sukhadukkhaṃ = ချမ်းသာ ဆင်းရဲကို သူတစ်ပါး ပြုသည်
sayaṅkatañca paraṅkatañca sukhadukkhaṃ = ချမ်းသာ ဆင်းရဲကို မိမိလည်း ပြုသည်၊ သူတစ်ပါးလည်း ပြုသည်
asayaṅkāraṃ aparaṅkāraṃ adhiccasamuppannaṃ sukhadukkhaṃ = ချမ်းသာ ဆင်းရဲသည် မိမိ မပြု၊ သူတစ်ပါး မပြုဘဲ အကြောင်းမဲ့ ဖြစ်ပေါ်လာသည်
atthi me attā = ငါ၏ အတ္တ ရှိ၏
natthi me attā = ငါ၏ အတ္တ မရှိ
attanā vā attānaṃ sañjānāmi = အတ္တဖြင့် အတ္တကို ငါ သိ၏
attanā vā anattānaṃ sañjānāmi = အတ္တဖြင့် အတ္တ မဟုတ်သည်ကို ငါ သိ၏
anattanā vā attānaṃ sañjānāmi = အတ္တ မဟုတ်သည်ဖြင့် အတ္တကို ငါ သိ၏
na sarāmi na sarāmi = ငါ မမှတ်မိ၊ ငါ မမှတ်မိ
nevāhaṃ āpannomhi, na panāhaṃ anāpannomhi = ငါ အာပတ်သင့်သည်လည်း မဟုတ်၊ အာပတ် မသင့်သည်လည်း မဟုတ်
asmi = ငါ ရှိ၏
ahamasmi = ဤသည် ငါ ဖြစ်၏
ayamahamasmi = ဤအရာသည် ငါ ဖြစ်၏
bhavissaṃ = ငါ ဖြစ်လိမ့်မည်
rūpī bhavissaṃ = ငါ ရုပ် ရှိသူ ဖြစ်လိမ့်မည်
arūpī bhavissaṃ = ငါ ရုပ် မရှိသူ ဖြစ်လိမ့်မည်
saññī bhavissaṃ = ငါ မှတ်သိမှု ရှိသူ ဖြစ်လိမ့်မည်
asaññī bhavissaṃ = ငါ မှတ်သိမှု မရှိသူ ဖြစ်လိမ့်မည်
nevasaññīnāsaññī bhavissaṃ = ငါ မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ ဖြစ်လိမ့်မည်
seyyassa seyyohamasmi = သာလွန်သူ ဖြစ်လျက် ငါသည် သာလွန်သူ ဖြစ်သည်
seyyassa sadisohamasmi = သာလွန်သူ ဖြစ်လျက် ငါသည် တူညီသူ ဖြစ်သည်
seyyassa hīnohamasmi = သာလွန်သူ ဖြစ်လျက် ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်
sadisassa seyyohamasmi = တူညီသူ ဖြစ်လျက် ငါသည် သာလွန်သူ ဖြစ်သည်
sadisassa sadisohamasmi = တူညီသူ ဖြစ်လျက် ငါသည် တူညီသူ ဖြစ်သည်
sadisassa hīnohamasmi = တူညီသူ ဖြစ်လျက် ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်
hīnassa seyyohamasmi = ယုတ်ညံ့သူ ဖြစ်လျက် ငါသည် သာလွန်သူ ဖြစ်သည်
hīnassa sadisohamasmi = ယုတ်ညံ့သူ ဖြစ်လျက် ငါသည် တူညီသူ ဖြစ်သည်
hīnassa hīnohamasmi = ယုတ်ညံ့သူ ဖြစ်လျက် ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်
natthi kāmesu doso = ကာမတို့၌ အပြစ် မရှိ

### Pamāda / kosajja head
Kāyaduccarite vā vacīduccarite vā manoduccarite vā pañcasu vā kāmaguṇesu cittassa vossaggo vossaggānuppadānaṃ kusalānaṃ vā dhammānaṃ bhāvanāya = ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ နှုတ်ဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ မနောဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ ကာမဂုဏ် ငါးပါးတို့၌ဖြစ်စေ စိတ်ကို လွှတ်ထားခြင်း၊ လွှတ်ထားခြင်းကို ထပ်ကာထပ်ကာ ပြုခြင်း ကုသိုလ် သဘောတရားတို့ကိုဖြစ်စေ ပွားများရာ၌
Kāyaduccarite vā vacīduccarite vā manoduccarite vā pañcasu vā kāmaguṇesu cittassa vossaggo, vossaggānuppadānaṃ kusalānaṃ vā dhammānaṃ, bhāvanāya = ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ နှုတ်ဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ မနောဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ ကာမဂုဏ် ငါးပါးတို့၌ဖြစ်စေ စိတ်ကို လွှတ်ထားခြင်း၊ လွှတ်ထားခြင်းကို ထပ်ကာထပ်ကာ ပြုခြင်း၊ ကုသိုလ် သဘောတရားတို့ကိုဖြစ်စေ ပွားများရာ၌၊
Kāyaduccarite vā vacīduccarite vā manoduccarite vā pañcasu vā kāmaguṇesu cittassa vossaggo vossaggānuppadānaṃ kusalānaṃ dhammānaṃ bhāvanāya = ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ နှုတ်ဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ မနောဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ ကာမဂုဏ် ငါးပါးတို့၌ဖြစ်စေ စိတ်ကို လွှတ်ထားခြင်း၊ လွှတ်ထားခြင်းကို ထပ်ကာထပ်ကာ ပြုခြင်း ကုသိုလ် သဘောတရားတို့ကို ပွားများရာ၌
Kāyaduccarite vā vacīduccarite vā manoduccarite vā pañcasu vā kāmaguṇesu cittassa vossaggo, vossaggānuppadānaṃ kusalānaṃ dhammānaṃ, bhāvanāya = ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ နှုတ်ဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ မနောဖြင့် ပြုသော ဒုစရိုက်၌ဖြစ်စေ၊ ကာမဂုဏ် ငါးပါးတို့၌ဖြစ်စေ စိတ်ကို လွှတ်ထားခြင်း၊ လွှတ်ထားခြင်းကို ထပ်ကာထပ်ကာ ပြုခြင်း၊ ကုသိုလ် သဘောတရားတို့ကို ပွားများရာ၌၊

### Atricchatā / mahicchatā / asantuṭṭhitā
Itarītaracīvarapiṇḍapātasenāsanagilānappaccayabhesajjaparikkhārehi pañcahi vā kāmaguṇehi asantuṭṭhassa bhiyyokamyatā = ရရှိသမျှ သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်တို့ဖြင့်ဖြစ်စေ၊ ကာမဂုဏ် ငါးပါးတို့ဖြင့်ဖြစ်စေ ရောင့်ရဲမှု မရှိသူ၏ ပို၍ လိုချင်ခြင်း
Itarītaracīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhārehi pañcahi vā kāmaguṇehi asantuṭṭhassa bhiyyokamyatā = ရရှိသမျှ သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်တို့ဖြင့်ဖြစ်စေ၊ ကာမဂုဏ် ငါးပါးတို့ဖြင့်ဖြစ်စေ ရောင့်ရဲမှု မရှိသူ၏ ပို၍ လိုချင်ခြင်း

### Pāpicchatā
Idhekacco assaddho samāno "saddhoti maṃ jano jānātū"ti icchati, dussīlo samāno "sīlavāti maṃ jano jānātū"ti icchati, appassuto samāno "bahussutoti maṃ jano jānātū"ti icchati, saṅgaṇikārāmo samāno "pavivittoti maṃ jano jānātū"ti icchati, kusīto samāno "āraddhavīriyoti maṃ jano jānātū"ti icchati, muṭṭhassatī samāno "upaṭṭhitassatīti maṃ jano jānātū"ti icchati, asamāhito samāno "samāhitoti maṃ jano jānātū"ti icchati, duppañño samāno "paññavāti maṃ jano jānātū"ti icchati, akhīṇāsavo samāno "khīṇāsavoti maṃ jano jānātū"ti icchati = ဤလောက၌ အချို့သော သူသည် ယုံကြည်မှု မရှိသူ ဖြစ်လျက် “ငါ့ကို ယုံကြည်မှု ရှိသူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏၊ သီလ ပျက်သူ ဖြစ်လျက် “ငါ့ကို သီလ ရှိသူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏၊ အကြားအမြင် နည်းသူ ဖြစ်လျက် “ငါ့ကို အကြားအမြင် များသူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏၊ အပေါင်းအသင်းကို နှစ်သက်သူ ဖြစ်လျက် “ငါ့ကို ကင်းဆိတ်စွာ နေသူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏၊ ပျင်းရိသူ ဖြစ်လျက် “ငါ့ကို ဝီရိယ အားထုတ်ထားသူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏၊ သတိ လစ်သူ ဖြစ်လျက် “ငါ့ကို သတိ တည်ထားသူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏၊ စိတ် မတည်ကြည်သူ ဖြစ်လျက် “ငါ့ကို စိတ် တည်ကြည်သူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏၊ ပညာ နည်းသူ ဖြစ်လျက် “ငါ့ကို ပညာ ရှိသူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏၊ စိတ်အစွန်းအထင်း မကုန်သေးသူ ဖြစ်လျက် “ငါ့ကို စိတ်အစွန်းအထင်း ကုန်ပြီးသူဟု လူတို့ သိကြပါစေ”ဟု အလိုရှိ၏

### Prefixes before a list
Mātari vā pitari vā jeṭṭhe vā bhātari vā ācariyesu vā upajjhāye vā buddhe vā sāvakesu vā aññataraññataresu garuṭṭhāniyesu = အမိ၌ဖြစ်စေ၊ အဖ၌ဖြစ်စေ၊ အကြီးအကဲ၌ဖြစ်စေ၊ ညီအစ်ကို၌ဖြစ်စေ၊ ဆရာတို့၌ဖြစ်စေ၊ ဥပဇ္ဈာယ်ဆရာ၌ဖြစ်စေ၊ ဘုရား၌ဖြစ်စေ၊ တပည့်သာဝကတို့၌ဖြစ်စေ၊ အလေးပြုထိုက်သော တစ်ဦးဦးတို့၌
Pantesu vā senāsanesu aññataraññataresu vā adhikusalesu dhammesu = ဆိတ်ငြိမ်ရာ ကျောင်းအိပ်ရာနေရာတို့၌ဖြစ်စေ၊ မြင့်မြတ်သော ကုသိုလ် သဘောတရား တစ်ခုခုတို့၌ဖြစ်စေ
Lābhasakkārasilokasannissitassa pāpicchassa icchāpakatassa paccayapaṭisevanasaṅkhātena [paccayapaṭisedhanasaṅkhātena (sī.)] vā sāmantajappitena vā iriyāpathassa vā = လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှုကို မှီသော၊ ယုတ်မာသော အလိုရှိသော၊ အလိုဆန္ဒ နှိပ်စက်ခံရသော သူ၏ ပစ္စည်းကို ငြင်းပယ်ဟန် ပြုခြင်းဟူသော နည်းဖြင့် [ပါဌ်ကွဲ (Sī.): paccayapaṭisedhanasaṅkhātena]ဖြစ်စေ၊ အနီးအနား စကား ပြောခြင်းဖြင့်ဖြစ်စေ၊ ကိုယ်ဟန် အမူအရာကိုဖြစ်စေ
Lābhasakkārasilokasannissitassa pāpicchassa icchāpakatassa = လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှုကို မှီသော၊ ယုတ်မာသော အလိုရှိသော၊ အလိုဆန္ဒ နှိပ်စက်ခံရသော သူ၏
Sahadhammike vuccamāne = တရားနှင့် လျော်စွာ သွန်သင် ပြောဆိုသောအခါ
Yā paralābhasakkāragarukāramānanavandanapūjanāsu = သူတစ်ပါး၏ လာဘ်၊ အရိုအသေ ပြုခံရမှု၊ လေးစားခံရမှု၊ ချီးမြှောက်ခံရမှု၊ ရှိခိုးခံရမှု၊ ပူဇော်ခံရမှုတို့၌ ဖြစ်သော

### Clauses
Lābhasakkārasilokasannissito pāpiccho icchāpakato ito laddhaṃ āmisaṃ amutra harati amutra vā laddhaṃ āmisaṃ idha āharati = လာဘ်၊ အပူဇော်ခံရခြင်း၊ ကျော်စောမှုကို မှီသော၊ ယုတ်မာသော အလိုရှိသော၊ အလိုဆန္ဒ နှိပ်စက်ခံရသော သူသည် ဤနေရာမှ ရသော ပစ္စည်းကို ထိုနေရာသို့ ဆောင်၏၊ သို့မဟုတ် ထိုနေရာမှ ရသော ပစ္စည်းကို ဤနေရာသို့ ဆောင်၏
Ye te puggalā assaddhā dussīlā appassutā maccharino duppaññā = ယုံကြည်မှု မရှိသော၊ သီလ ပျက်သော၊ အကြားအမြင် နည်းသော၊ ဝန်တိုသော၊ ပညာ နည်းသော ပုဂ္ဂိုလ်တို့ ရှိကြ၏
Appatte pattasaññitā = မရောက်သေးသည်၌ ရောက်ပြီဟု မှတ်ထင်ခြင်း
akate katasaññitā = မပြုရသေးသည်၌ ပြုပြီးပြီဟု မှတ်ထင်ခြင်း
anadhigate adhigatasaññitā = မရရှိသေးသည်၌ ရရှိပြီဟု မှတ်ထင်ခြင်း
asacchikate sacchikatasaññitā = မျက်မှောက် မပြုရသေးသည်၌ မျက်မှောက်ပြုပြီးပြီဟု မှတ်ထင်ခြင်း
Rūpaṃ asmīti māno = ရုပ်၌ ငါ ရှိ၏ဟူသော မာန
asmīti māno = ငါ ရှိ၏ဟူသော မာန
asmīti chando = ငါ ရှိ၏ဟူသော ဆန္ဒ
asmīti anusayo = ငါ ရှိ၏ဟူသော ကိန်းအောင်းခြင်း
vedanā…pe… saññā…pe… saṅkhārā…pe… viññāṇaṃ asmīti māno = ခံစားမှု… မှတ်သိမှု… ပြုပြင်ဖန်တီးမှုများ… သိစိတ်၌ ငါ ရှိ၏ဟူသော မာန
Dukkarakāritāpaṭisaṃyutto vā diṭṭhigatapaṭisaṃyutto vā gehasito takko vitakko micchāsaṅkappo = ပြုနိုင်ခဲသော အကျင့်ကို ကျင့်ခြင်းနှင့် စပ်ယှဉ်သောဖြစ်စေ၊ အယူမှားနှင့် စပ်ယှဉ်သောဖြစ်စေ လောကီ အိမ်ရာကို မှီသော တွေးတောခြင်း၊ စတင်ကြံစည်မှု၊ မှားယွင်းသော ကြံစည်မှု
"Anatthaṃ me acarī"ti āghāto jāyati = “ငါ့အား အကျိုးမဲ့ကို ပြုခဲ့ပြီ”ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
"anatthaṃ me caratī"ti āghāto jāyati = “ငါ့အား အကျိုးမဲ့ကို ပြု၏”ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
"anatthaṃ me carissatī"ti āghāto jāyati = “ငါ့အား အကျိုးမဲ့ကို ပြုလိမ့်မည်”ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
"piyassa me manāpassa anatthaṃ acari"…pe… anatthaṃ carati…pe… "anatthaṃ carissatī"ti āghāto jāyati = “ငါ ချစ်သော ငါ နှစ်သက်သူအား အကျိုးမဲ့ကို ပြုခဲ့ပြီ”… အကျိုးမဲ့ကို ပြု၏… “အကျိုးမဲ့ကို ပြုလိမ့်မည်”ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
"piyassa me manāpassa anatthaṃ acari"…pe… anatthaṃ carati…pe… anatthaṃ carissatīti āghāto jāyati = “ငါ ချစ်သော ငါ နှစ်သက်သူအား အကျိုးမဲ့ကို ပြုခဲ့ပြီ”… အကျိုးမဲ့ကို ပြု၏… အကျိုးမဲ့ကို ပြုလိမ့်မည်ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
"appiyassa me amanāpassa atthaṃ acari"…pe… atthaṃ carati…pe… "atthaṃ carissatī"ti āghāto jāyati = “ငါ မချစ်သော ငါ မနှစ်သက်သူအား အကျိုးကို ပြုခဲ့ပြီ”… အကျိုးကို ပြု၏… “အကျိုးကို ပြုလိမ့်မည်”ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
appiyassa me amanāpassa atthaṃ acari…pe… atthaṃ carati…pe… atthaṃ carissatīti āghāto jāyati = ငါ မချစ်သော ငါ မနှစ်သက်သူအား အကျိုးကို ပြုခဲ့ပြီ… အကျိုးကို ပြု၏… အကျိုးကို ပြုလိမ့်မည်ဟု ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
aṭṭhāne vā pana āghāto jāyati = သို့မဟုတ် အကြောင်း မရှိဘဲ ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်
Dukkhe aññāṇaṃ…pe… avijjālaṅgī moho akusalamūlaṃ = ဒုက္ခကို မသိခြင်း… အမှန်ကို မသိမှု တံခါးကန့်လန့်၊ မောဟ၊ အကုသိုလ်၏ အမြစ်
Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ, dukkhanirodhe aññāṇaṃ, dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ, pubbante aññāṇaṃ, aparante aññāṇaṃ, pubbantāparante aññāṇaṃ, idappaccayatā paṭiccasamuppannesu dhammesu aññāṇaṃ = ဒုက္ခကို မသိခြင်း၊ ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို မသိခြင်း၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းကို မသိခြင်း၊ ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်ကို မသိခြင်း၊ အတိတ်ကာလကို မသိခြင်း၊ အနာဂတ်ကာလကို မသိခြင်း၊ အတိတ်ကာလနှင့် အနာဂတ်ကာလကို မသိခြင်း၊ ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော သဘောတရားတို့ကို မသိခြင်း
Pubbantaṃ ārabbha yā uppajjati diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho = အတိတ်ကာလကို အစွဲပြု၍ ဖြစ်ပေါ်လာသော အယူ၊ အယူမှား… ပြောင်းပြန် စွဲကိုင်ခြင်း ရှိသမျှ
Aparantaṃ ārabbha yā uppajjati diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho = အနာဂတ်ကာလကို အစွဲပြု၍ ဖြစ်ပေါ်လာသော အယူ၊ အယူမှား… ပြောင်းပြန် စွဲကိုင်ခြင်း ရှိသမျှ
Yaṃ na hirīyati hiriyitabbena, na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ရှက်ထိုက်သည့်အရာကို မရှက်ခြင်း၊ ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို မရှက်ခြင်း ရှိသမျှ
Yaṃ na hirīyati hirīyitabbena, na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ရှက်ထိုက်သည့်အရာကို မရှက်ခြင်း၊ ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို မရှက်ခြင်း ရှိသမျှ
Yaṃ na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ကြောက်ရွံ့ထိုက်သည့်အရာကို မကြောက်ရွံ့ခြင်း၊ ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို မကြောက်ရွံ့ခြင်း ရှိသမျှ
Yaṃ na ottappati ottappitabbena, na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = ကြောက်ရွံ့ထိုက်သည့်အရာကို မကြောက်ရွံ့ခြင်း၊ ယုတ်မာသော အကုသိုလ် သဘောတရားတို့ကို ကျူးလွန်ခြင်းကို မကြောက်ရွံ့ခြင်း ရှိသမျှ
Idhekacco appaṭisanthārako hoti āmisapaṭisanthārena vā dhammapaṭisanthārena vā = ဤလောက၌ အချို့သော သူသည် ပစ္စည်းဖြင့် ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်းဖြင့်ဖြစ်စေ၊ တရားဖြင့် ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်းဖြင့်ဖြစ်စေ ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း မရှိသူ ဖြစ်၏
Kāyiko vītikkamo vācasiko vītikkamo kāyikavācasiko vītikkamo = ကိုယ်ပိုင်းဆိုင်ရာ ကျူးလွန်ခြင်း၊ နှုတ်ပိုင်းဆိုင်ရာ ကျူးလွန်ခြင်း၊ ကိုယ်ပိုင်းဆိုင်ရာနှင့် နှုတ်ပိုင်းဆိုင်ရာ ကျူးလွန်ခြင်း
Kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo = ကိုယ်ပိုင်းဆိုင်ရာ ကျူးလွန်ခြင်း၊ နှုတ်ပိုင်းဆိုင်ရာ ကျူးလွန်ခြင်း၊ ကိုယ်ပိုင်းဆိုင်ရာနှင့် နှုတ်ပိုင်းဆိုင်ရာ ကျူးလွန်ခြင်း
Idhekacco pāṇinā vā leḍḍunā vā daṇḍena vā satthena vā rajjuyā vā aññataraññatarena satte viheṭheti = ဤလောက၌ အချို့သော သူသည် လက်ဖြင့်ဖြစ်စေ၊ မြေစိုင်ခဲဖြင့်ဖြစ်စေ၊ တုတ်ဖြင့်ဖြစ်စေ၊ လက်နက်ဖြင့်ဖြစ်စေ၊ ကြိုးဖြင့်ဖြစ်စေ၊ တစ်ခုခုသော အရာဖြင့် သတ္တဝါတို့ကို ညှဉ်းဆဲ၏
Kāyena adhammacariyāvisamacariyā = ကိုယ်ဖြင့် တရားနှင့် မညီသော အကျင့်၊ ဖောက်ပြန်သော အကျင့်
vācāya adhammacariyāvisamacariyā = နှုတ်ဖြင့် တရားနှင့် မညီသော အကျင့်၊ ဖောက်ပြန်သော အကျင့်
manasā adhammacariyāvisamacariyā = မနောဖြင့် တရားနှင့် မညီသော အကျင့်၊ ဖောက်ပြန်သော အကျင့်
Kāmasaññā, byāpādasaññā, vihiṃsāsaññā = ကာမကို မှတ်သိမှု၊ ဖျက်ဆီးလိုစိတ်ဆိုင်ရာ မှတ်သိမှု၊ ညှဉ်းပန်းမှုဆိုင်ရာ မှတ်သိမှု
Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhavantattaṃ cittassa = စိတ်၏ ယောက်ယက်ခတ်မှု၊ မငြိမ်ဝပ်ခြင်း၊ စိတ်၏ ပျံ့လွင့်ခြင်း၊ စိတ်၏ ယိမ်းထိုးနေသော အဖြစ် ရှိသမျှ
Idhekacco assaddho hoti, na saddahati buddhaṃ vā dhammaṃ vā saṅghaṃ vā = ဤလောက၌ အချို့သော သူသည် ယုံကြည်မှု မရှိသူ ဖြစ်၏၊ ဘုရားကိုဖြစ်စေ၊ တရားကိုဖြစ်စေ၊ သံဃာကိုဖြစ်စေ မယုံကြည်
Anicce "nicca"nti ayoniso manasikāro = မမြဲသည်၌ “မြဲ၏”ဟု မသင့်လျော်စွာ နှလုံးသွင်းခြင်း
dukkhe "sukha"nti ayoniso manasikāro = ဆင်းရဲသည်၌ “ချမ်းသာ၏”ဟု မသင့်လျော်စွာ နှလုံးသွင်းခြင်း
anattani "attā"ti ayoniso manasikāro = အတ္တ မဟုတ်သည်၌ “အတ္တ ဖြစ်၏”ဟု မသင့်လျော်စွာ နှလုံးသွင်းခြင်း
asubhe "subha"nti ayoniso manasikāro = မတင့်တယ်သည်၌ “တင့်တယ်၏”ဟု မသင့်လျော်စွာ နှလုံးသွင်းခြင်း
saccavippaṭikulena vā cittassa āvaṭṭanā anāvaṭṭanā ābhogo samannāhāro manasikāro = သို့မဟုတ် သစ္စာနှင့် ဆန့်ကျင်သော နည်းဖြင့် စိတ်၏ လှည့်ခြင်း၊ အဖန်ဖန် လှည့်ခြင်း၊ စိတ်ညွတ်ခြင်း၊ စိတ်ကို ဆောင်ခြင်း၊ နှလုံးသွင်းခြင်း
Micchādiṭṭhi, micchāsaṅkappo, micchāvācā, micchākammanto, micchāājīvo, micchāvāyāmo, micchāsati, micchāsamādhi = မှားယွင်းသော အယူ၊ မှားယွင်းသော ကြံစည်မှု၊ မှားယွင်းသော စကား၊ မှားယွင်းသော အလုပ်၊ မှားယွင်းသော အသက်မွေးမှု၊ မှားယွင်းသော အားထုတ်မှု၊ မှားယွင်းသော သတိ၊ မှားယွင်းသော သမာဓိ
Yā imassa saddhammassa asotukamyatā asavanakamyatā anuggahetukamyatā adhāretukamyatā = ဤသူတော်ကောင်းတရားကို မနာကြားလိုခြင်း၊ နားမထောင်လိုခြင်း၊ မသင်ယူလိုခြင်း၊ မဆောင်ထားလိုခြင်း ရှိသမျှ
Yā imassa kummaggassa sevanā nisevanā saṃsevanā bhajanā sambhajanā bhatti sambhatti taṃsampavaṅkatā = ဤလမ်းမှားကို ပေါင်းသင်းခြင်း၊ နီးကပ်စွာ ပေါင်းသင်းခြင်း၊ ကောင်းစွာ ပေါင်းသင်းခြင်း၊ ဆည်းကပ်ခြင်း၊ ကောင်းစွာ ဆည်းကပ်ခြင်း၊ ကိုးကွယ်ခြင်း၊ ကောင်းစွာ ကိုးကွယ်ခြင်း၊ ထိုသူတို့ဘက်သို့ ညွတ်ကိုင်းခြင်း ရှိသမျှ
Yā imesaṃ ariyānaṃ adassanakamyatā adaṭṭhukamyatā asametukamyatā asamāgantukamyatā = ဤအရိယာတို့ကို မဖူးမြင်လိုခြင်း၊ မတွေ့မြင်လိုခြင်း၊ မဆုံလိုခြင်း၊ မပေါင်းဆုံလိုခြင်း ရှိသမျှ
Cattāro satipaṭṭhānā, cattāro sammappadhānā, cattāro iddhipādā, pañcindriyāni, pañca balāni, satta bojjhaṅgā, ariyo aṭṭhaṅgiko maggo = သတိပဋ္ဌာန် လေးပါး၊ မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း လေးပါး၊ ဣဒ္ဓိပါဒ် လေးပါး၊ စွမ်းရည် ငါးပါး၊ စွမ်းအား ငါးပါး၊ ဗောဇ္ဈင် ခုနစ်ပါး၊ အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်
Chandarāgā gehasitā dhammā = None
Manāpiyesu rūpesu gehasito rāgo sārāgo cittassa sārāgo = None
nādhimuccati na sampasīdati = မဆုံးဖြတ်နိုင်၊ မကြည်လင်
Atītaṃ vā addhānaṃ = အတိတ်ကာလကို
anāgataṃ vā addhānaṃ = အနာဂတ်ကာလကို
etarahi vā paccuppannaṃ addhānaṃ = ယခု ပစ္စုပ္ပန်ကာလကို
Idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhī = ဤလောက၌ အချို့သော ရဟန်း သို့မဟုတ် ပုဏ္ဏားသည် ဤသို့ ဆိုလေ့ ရှိသူ၊ ဤသို့ အယူ ရှိသူ ဖြစ်၏
idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhī = ဤလောက၌ အချို့သော ရဟန်း သို့မဟုတ် ပုဏ္ဏားသည် ဤသို့ ဆိုလေ့ ရှိသူ၊ ဤသို့ အယူ ရှိသူ ဖြစ်၏
Idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhi = ဤလောက၌ အချို့သော ရဟန်း သို့မဟုတ် ပုဏ္ဏားသည် ဤသို့ ဆိုလေ့ ရှိသူ၊ ဤသို့ အယူ ရှိသူ ဖြစ်၏
idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhi = ဤလောက၌ အချို့သော ရဟန်း သို့မဟုတ် ပုဏ္ဏားသည် ဤသို့ ဆိုလေ့ ရှိသူ၊ ဤသို့ အယူ ရှိသူ ဖြစ်၏
idha panekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhī = သို့ရာတွင် ဤလောက၌ အချို့သော ရဟန်း သို့မဟုတ် ပုဏ္ဏားသည် ဤသို့ ဆိုလေ့ ရှိသူ၊ ဤသို့ အယူ ရှိသူ ဖြစ်၏
idhekacco samaṇo vā brāhmaṇo vā evaṃvādī hoti evaṃdiṭṭhi [evaṃdiṭṭhi (syā.)] = ဤလောက၌ အချို့သော ရဟန်း သို့မဟုတ် ပုဏ္ဏားသည် ဤသို့ ဆိုလေ့ ရှိသူ၊ ဤသို့ အယူ ရှိသူ [စာလုံးပေါင်းကွဲ (Syā.): evaṃdiṭṭhi] ဖြစ်၏
"yaṃ kiñcāyaṃ purisapuggalo paṭisaṃvedeti sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, sabbaṃ taṃ pubbe katahetū"ti = “ဤပုဂ္ဂိုလ်သည် သာယာမှုကိုဖြစ်စေ၊ နာကျင်မှုကိုဖြစ်စေ၊ မနာကျင် မသာယာမှုကိုဖြစ်စေ ခံစားရသမျှ ထိုအားလုံးသည် ရှေးက ပြုခဲ့သော ကံကြောင့် ဖြစ်သည်”ဟူ၍
"yaṃ kiñcāyaṃ purisapuggalo paṭisaṃvedeti sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, sabbaṃ taṃ issaranimmānahetū"ti = “ဤပုဂ္ဂိုလ်သည် သာယာမှုကိုဖြစ်စေ၊ နာကျင်မှုကိုဖြစ်စေ၊ မနာကျင် မသာယာမှုကိုဖြစ်စေ ခံစားရသမျှ ထိုအားလုံးသည် ဖန်ဆင်းရှင်၏ ဖန်ဆင်းခြင်းကြောင့် ဖြစ်သည်”ဟူ၍
"yaṃ kiñcāyaṃ purisapuggalo paṭisaṃvedeti sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, sabbaṃ taṃ ahetu appaccayā"ti = “ဤပုဂ္ဂိုလ်သည် သာယာမှုကိုဖြစ်စေ၊ နာကျင်မှုကိုဖြစ်စေ၊ မနာကျင် မသာယာမှုကိုဖြစ်စေ ခံစားရသမျှ ထိုအားလုံးသည် အကြောင်း မရှိ၊ အထောက်အပံ့ မရှိဘဲ ဖြစ်သည်”ဟူ၍
sabrahmacārīsu kupito hoti anattamano āhatacitto khilajāto = သီတင်းသုံးဖော်တို့အပေါ် အမျက်ထွက်သူ ဖြစ်၏၊ စိတ် မနှစ်သိမ့်သူ၊ ထိခိုက်သော စိတ် ရှိသူ၊ ခက်ထန်သော စိတ် ဖြစ်ပေါ်သူ ဖြစ်၏
Kāme avītarāgo hoti avigatacchando avigatapemo avigatapipāso avigatapariḷāho avigatataṇho = ကာမတို့၌ ရာဂ မကင်းသူ ဖြစ်၏၊ ဆန္ဒ မကင်းသူ၊ ချစ်ခင်မှု မကင်းသူ၊ ငတ်မွတ်မှု မကင်းသူ၊ ပူလောင်မှု မကင်းသူ၊ တပ်မက်မှု မကင်းသူ ဖြစ်၏
kāye avītarāgo hoti… rūpe avītarāgo hoti… yāvadatthaṃ udarāvadehakaṃ bhuñjitvā seyyasukhaṃ passasukhaṃ middhasukhaṃ anuyutto viharati = ကိုယ်၌ ရာဂ မကင်းသူ ဖြစ်၏… ရုပ်၌ ရာဂ မကင်းသူ ဖြစ်၏… ဝမ်းပြည့်အောင် လိုသလောက် စားပြီး၍ အိပ်ခြင်း၏ ချမ်းသာ၊ လှဲလျောင်းခြင်း၏ ချမ်းသာ၊ ငိုက်မျဉ်းခြင်း၏ ချမ်းသာကို အားထုတ်လျက် နေ၏
aññataraṃ devanikāyaṃ paṇidhāya brahmacariyaṃ carati = နတ်အပေါင်း တစ်ခုခုကို ဆုတောင်း၍ မြတ်သော အကျင့်ကို ကျင့်၏
"imināhaṃ sīlena vā vatena vā tapena vā brahmacariyena vā devo vā bhavissāmi devaññataro vā"ti = “ငါသည် ဤသီလဖြင့်ဖြစ်စေ၊ အကျင့်ဝတ်ဖြင့်ဖြစ်စေ၊ အကျင့်ခြိုးခြံမှုဖြင့်ဖြစ်စေ၊ မြတ်သော အကျင့်ဖြင့်ဖြစ်စေ နတ်ဖြစ်စေ၊ နတ်တစ်ပါးပါးဖြစ်စေ ဖြစ်ရလိမ့်မည်”ဟူ၍
Mātā jīvitā voropitā hoti = အမိသည် အသက်မှ ချခံရ၏
pitā jīvitā voropito hoti = အဖသည် အသက်မှ ချခံရ၏
arahanto jīvitā voropito hoti = ရဟန္တာသည် အသက်မှ ချခံရ၏
duṭṭhena cittena tathāgatassa lohitaṃ uppāditaṃ hoti = ပြစ်မှားသော စိတ်ဖြင့် မြတ်စွာဘုရား၏ သွေးကို ထွက်စေအပ်၏
saṅgho bhinno hoti = သံဃာသည် ကွဲပြားစေခံရ၏
sato vā pana sattassa ucchedaṃ vināsaṃ vibhavaṃ paññāpenti = သို့မဟုတ် ရှိနေသော သတ္တဝါ၏ ပြတ်စဲခြင်း၊ ပျက်စီးခြင်း၊ ဘဝ ပျောက်ကွယ်ခြင်းကို ပညတ်ကြ၏
diṭṭhadhammanibbānaṃ vā paneke abhivadanti = သို့မဟုတ် အချို့သူတို့သည် မျက်မှောက်ဘဝ၌ နိဗ္ဗာန်ကို ကြွေးကြော်ကြ၏
Bahuno janassa appiyo hoti amanāpo = လူအများ၏ မချစ်အပ်၊ မနှစ်သက်အပ်သူ ဖြစ်၏
verabahulo ca hoti = ရန် များသူလည်း ဖြစ်၏
vajjabahulo ca = အပြစ် များသူလည်း ဖြစ်၏
sammūḷho kālaṅkaroti = တွေဝေလျက် သေရ၏
kāyassa bhedā paraṃ maraṇā apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapajjati = ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက် အပါယ်၊ ဆိုးသော လားရာ၊ ပျက်စီး ကျရောက်ရာ၊ ငရဲသို့ ရောက်ရ၏
Assaddho hoti = ယုံကြည်မှု မရှိသူ ဖြစ်၏
ahiriko hoti = ဒုစရိုက်ကို မရှက်သူ ဖြစ်၏
anottappī hoti = ဒုစရိုက်ကို မကြောက်ရွံ့သူ ဖြစ်၏
appassuto hoti = အကြားအမြင် နည်းသူ ဖြစ်၏
kusīto hoti = ပျင်းရိသူ ဖြစ်၏
muṭṭhassatī hoti = သတိ လစ်သူ ဖြစ်၏
duppañño hoti = ပညာ နည်းသူ ဖြစ်၏
ārakkhādhikaraṇaṃ daṇḍādāna-satthādāna-kalaha-viggahavivāda-tuvaṃtuvaṃ-pesuñña-musāvādā aneke pāpakā akusalā dhammā sambhavanti = စောင့်ရှောက်ခြင်းကြောင့် တုတ်ကိုင်ခြင်း၊ လက်နက်ကိုင်ခြင်း၊ ခိုက်ရန်ဖြစ်ခြင်း၊ ငြင်းခုံ အငြင်းပွားခြင်း၊ နင် ငါ ပြောဆိုခြင်း၊ ကုန်းတိုက်ခြင်း၊ မုသား ပြောခြင်းဟူသော ယုတ်မာသော အကုသိုလ် သဘောတရား အများအပြားတို့ ဖြစ်ပေါ်ကြ၏
asaññīti naṃ paññapenti = ထိုအတ္တကို မှတ်သိမှု မရှိသူဟု ပညတ်ကြ၏
nevasaññīnāsaññīti naṃ paññapenti = ထိုအတ္တကို မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူဟု ပညတ်ကြ၏
arūpī attā…pe… rūpī ca arūpī ca…pe… nevarūpīnārūpī…pe… "antavā attā hoti arogo paraṃ maraṇā"ti = အတ္တသည် ရုပ် မရှိသူ… ရုပ် ရှိသည်လည်း ဖြစ်၊ မရှိသည်လည်း ဖြစ်သူ… ရုပ် ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ… “အတ္တသည် အဆုံး ရှိသူ ဖြစ်၍ သေပြီးနောက် အနာကင်း၏”ဟူ၍
atha vā panassa evaṃdiṭṭhi hoti = သို့မဟုတ် ထိုသူအား ဤသို့ အယူ ရှိ၏
"so me ayaṃ attā vado vedeyyo tatra tatra dīgharattaṃ kalyāṇapāpakānaṃ kammānaṃ vipākaṃ paccanubhoti = “ငါ၏ ဤအတ္တသည် ပြောဆိုတတ်၏၊ ခံစားတတ်၏၊ ထိုထို ဘဝ၌ ကြာမြင့်စွာ ကောင်းသော ကံ၊ ယုတ်မာသော ကံတို့၏ အကျိုးကို ခံစား၏
"Natthi dinnaṃ … pavedentī"ti (pi-1 ^1 natthi list, head 2 + tail) = “ပေးလှူခြင်း မရှိ၊ ယဇ်ပူဇော်ခြင်း မရှိ… ဤလောကကိုလည်း တမလွန် လောကကိုလည်း ကိုယ်တိုင် ထူးကဲစွာ သိ၍ မျက်မှောက်ပြုပြီး ဟောကြားသော ရဟန်းပုဏ္ဏားတို့ မရှိ”ဟူ၍
"yato kho, bho, ayaṃ attā pañcahi kāmaguṇehi samappito samaṅgībhūto paricāreti, ettāvatā kho, bho, ayaṃ attā paramadiṭṭhadhammanibbānappatto hotī"ti = “အချင်း၊ ဤအတ္တသည် ကာမဂုဏ် ငါးပါးတို့ဖြင့် ပြည့်စုံ၍ ယှဉ်လျက် မွေ့လျော်သောကြောင့် အချင်း၊ ဤမျှဖြင့် ဤအတ္တသည် မျက်မှောက်ဘဝ၌ အမြတ်ဆုံး နိဗ္ဗာန်သို့ ရောက်သည် ဖြစ်၏”ဟူ၍
"yato kho, bho, ayaṃ attā rūpī cātumahābhūtiko [cātummahābhūtiko (sī. syā.)] mātāpettikasambhavo kāyassa bhedā ucchijjati vinassati na hoti paraṃ maraṇā, ettāvatā kho bho, ayaṃ attā sammā samucchinno hotī"ti = “အချင်း၊ ဤအတ္တသည် ရုပ် ရှိ၏၊ မူလဓာတ်ကြီး လေးပါးဖြင့် ဖြစ်၏ [စာလုံးပေါင်းကွဲ (Sī., Syā.): cātummahābhūtiko]၊ အမိအဖတို့မှ ဖြစ်ပေါ်လာ၏၊ ခန္ဓာကိုယ် ပြိုကွဲသောအခါ ပြတ်စဲ၏၊ ပျက်စီး၏၊ သေပြီးနောက် မရှိတော့သောကြောင့် အချင်း၊ ဤမျှဖြင့် ဤအတ္တသည် ကောင်းစွာ ပြတ်စဲသည် ဖြစ်၏”ဟူ၍
tamañño evamāha = ထိုသူကို အခြားသူက ဤသို့ ဆို၏
"atthi kho, bho, eso attā yaṃ tvaṃ vadesi neso natthīti vadāmi = “အချင်း၊ သင် ပြောသော ထိုအတ္တသည် ရှိပါ၏၊ ထိုအတ္တ မရှိဟု ငါ မဆို
Tasmiṃ sati imāni papañcitāni honti = ထိုသို့ ရှိသော် ဤချဲ့ထွင်မှုတို့ ဖြစ်ကြ၏

### Māna sentences (new)
X mānaṃ jappeti = Xကို ဖြစ်ပေါ်စေ၏
parehi seyyaṃ attānaṃ dahati = မိမိကိုယ်ကို သူတစ်ပါးတို့ထက် သာလွန်သူဟု ထား၏
so taṃ nissāya = ထိုသူသည် ထိုအကြောင်းကို မှီ၍
pubbakālaṃ / aparakālaṃ = အစောပိုင်း အချိန်၌ / နောက်ပိုင်း အချိန်၌
parehi attānaṃ atimaññati = မိမိကိုယ်ကို သူတစ်ပါးတို့ထက် အလွန် မြင့်မြတ်သည်ဟု ထင်မှတ်၏

### Micchāmāna
Idhekacco pāpakena vā kammāyatanena pāpakena vā sippāyatanena pāpakena vā vijjāṭṭhānena pāpakena vā sutena pāpakena vā paṭibhānena pāpakena vā sīlena pāpakena vā vatena pāpakena vā sīlabbatena pāpikāya vā diṭṭhiyā aññataraññatarena vatthunā mānaṃ jappeti = ဤလောက၌ အချို့သော သူသည် ယုတ်မာသော အလုပ်အကိုင်ဖြင့်ဖြစ်စေ၊ ယုတ်မာသော အတတ်ပညာဖြင့်ဖြစ်စေ၊ ယုတ်မာသော ပညာရပ်ဖြင့်ဖြစ်စေ၊ ယုတ်မာသော အကြားအမြင်ဖြင့်ဖြစ်စေ၊ ယုတ်မာသော လျင်မြန်သော ဉာဏ်ဖြင့်ဖြစ်စေ၊ ယုတ်မာသော သီလဖြင့်ဖြစ်စေ၊ ယုတ်မာသော အကျင့်ဝတ်ဖြင့်ဖြစ်စေ၊ ယုတ်မာသော သီလ အကျင့်ဝတ်ဖြင့်ဖြစ်စေ၊ ယုတ်မာသော အယူဖြင့်ဖြစ်စေ၊ တစ်ခုခုသော အကြောင်းဖြင့် မာနကို ဖြစ်ပေါ်စေ၏

### Upavicāra (new)
somanassaṭṭhāniyaṃ = ဝမ်းမြောက်ဖွယ် ဖြစ်သော
domanassaṭṭhāniyaṃ = စိတ်ဆင်းရဲဖွယ် ဖြစ်သော
upekkhāṭṭhāniyaṃ = လျစ်လျူရှုဖွယ် ဖြစ်သော
upavicarati = စိတ်ဖြင့် လှည့်လည် ချဉ်းကပ်၏

### Anariyavohāra (new)
adiṭṭhe diṭṭhavāditā = မမြင်သည်ကို မြင်သည်ဟု ပြောခြင်း
assute sutavāditā = မကြားသည်ကို ကြားသည်ဟု ပြောခြင်း
amute mutavāditā = မထိတွေ့သည်ကို ထိတွေ့သည်ဟု ပြောခြင်း
aviññāte viññātavāditā = မသိသည်ကို သိသည်ဟု ပြောခြင်း
diṭṭhe adiṭṭhavāditā = မြင်သည်ကို မမြင်ဟု ပြောခြင်း
sute assutavāditā = ကြားသည်ကို မကြားဟု ပြောခြင်း
mute amutavāditā = ထိတွေ့သည်ကို မထိတွေ့ဟု ပြောခြင်း
viññāte aviññātavāditā = သိသည်ကို မသိဟု ပြောခြင်း
lābhe sārāgo = လာဘ်၌ တပ်မက်ခြင်း
alābhe paṭivirodho = လာဘ် မရခြင်း၌ ဆန့်ကျင်ခြင်း
yase sārāgo = အခြံအရံ ရခြင်း၌ တပ်မက်ခြင်း
ayase paṭivirodho = အခြံအရံ မရခြင်း၌ ဆန့်ကျင်ခြင်း
pasaṃsāya sārāgo = ချီးမွမ်းခြင်း၌ တပ်မက်ခြင်း
nindāya paṭivirodho = ကဲ့ရဲ့ခြင်း၌ ဆန့်ကျင်ခြင်း
sukhe sārāgo = ချမ်းသာ၌ တပ်မက်ခြင်း
dukkhe paṭivirodho = ဆင်းရဲ၌ ဆန့်ကျင်ခြင်း

### Self views («X attā hoti arogo paraṃ maraṇā»)
saññī = မှတ်သိမှု ရှိသူ
asaññī = မှတ်သိမှု မရှိသူ
nevasaññīnāsaññī = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ
rūpī = ရုပ် ရှိသူ
arūpī = ရုပ် မရှိသူ
rūpī ca arūpī ca = ရုပ် ရှိသည်လည်း ဖြစ်၊ မရှိသည်လည်း ဖြစ်သူ
nevarūpīnārūpī = ရုပ် ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ
antavā = အဆုံး ရှိသူ
anantavā = အဆုံး မရှိသူ
antavā ca anantavā ca = အဆုံး ရှိသည်လည်း ဖြစ်၊ မရှိသည်လည်း ဖြစ်သူ
nevantavā nānantavā = အဆုံး ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ

### Taṇhāmūlaka (new)
taṇhaṃ = တပ်မက်မှု
pariyesanā = ရှာမှီးခြင်း
pariyesanaṃ = ရှာမှီးခြင်း
lābho = ရရှိခြင်း
lābhaṃ = ရရှိခြင်း
vinicchayo = ဆုံးဖြတ်ခြင်း
vinicchayaṃ = ဆုံးဖြတ်ခြင်း
chandarāgo = လိုလားမှု ရာဂ
chandarāgaṃ = လိုလားမှု ရာဂ
ajjhosānaṃ = နစ်မွန်းခြင်း
pariggaho = သိမ်းပိုက်ခြင်း
pariggahaṃ = သိမ်းပိုက်ခြင်း
macchariyaṃ = ဝန်တိုမှု
ārakkho = စောင့်ရှောက်ခြင်း

### Headings (new)
Khuddakavatthuvibhaṅgo = အသေးစား အကြောင်းအရာများကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Taṇhāvicaritaniddeso = တပ်မက်မှု၏ ဖြစ်ပုံ အကျယ် ဖော်ပြချက်
Mātikā = ခေါင်းစဉ်စာရင်း
Ekakamātikā = တစ်မျိုးတွဲ ခေါင်းစဉ်စာရင်း
Ekakaniddeso = တစ်မျိုးတွဲ အကျယ် ဖော်ပြချက်
Dukamātikā = နှစ်မျိုးတွဲ ခေါင်းစဉ်စာရင်း
Dukaniddeso = နှစ်မျိုးတွဲ အကျယ် ဖော်ပြချက်
Tikamātikā = သုံးမျိုးတွဲ ခေါင်းစဉ်စာရင်း
Tikaniddeso = သုံးမျိုးတွဲ အကျယ် ဖော်ပြချက်
Catukkamātikā = လေးမျိုးတွဲ ခေါင်းစဉ်စာရင်း
Catukkaniddeso = လေးမျိုးတွဲ အကျယ် ဖော်ပြချက်
Pañcakamātikā = ငါးမျိုးတွဲ ခေါင်းစဉ်စာရင်း
Pañcakaniddeso = ငါးမျိုးတွဲ အကျယ် ဖော်ပြချက်
Chakkamātikā = ခြောက်မျိုးတွဲ ခေါင်းစဉ်စာရင်း
Chakkaniddeso = ခြောက်မျိုးတွဲ အကျယ် ဖော်ပြချက်
Sattakamātikā = ခုနစ်မျိုးတွဲ ခေါင်းစဉ်စာရင်း
Sattakaniddeso = ခုနစ်မျိုးတွဲ အကျယ် ဖော်ပြချက်
Aṭṭhakamātikā = ရှစ်မျိုးတွဲ ခေါင်းစဉ်စာရင်း
Aṭṭhakaniddeso = ရှစ်မျိုးတွဲ အကျယ် ဖော်ပြချက်
Navakamātikā = ကိုးမျိုးတွဲ ခေါင်းစဉ်စာရင်း
Navakaniddeso = ကိုးမျိုးတွဲ အကျယ် ဖော်ပြချက်
Dasakamātikā = ဆယ်မျိုးတွဲ ခေါင်းစဉ်စာရင်း
Dasakaniddeso = ဆယ်မျိုးတွဲ အကျယ် ဖော်ပြချက်

### Sentences (new)
Idhekacco gihīhi saṃsaṭṭho viharati sahanandī sahasokī, sukhitesu sukhito, dukkhitesu dukkhito, uppannesu kiccakaraṇīyesu attanā vā yogaṃ āpajjati. = ဤလောက၌ အချို့သော သူသည် လူဝတ်ကြောင်တို့နှင့် ရောနှော၍ နေ၏၊ အတူ ဝမ်းမြောက်၏၊ အတူ စိုးရိမ်၏၊ ချမ်းသာသူတို့၌ ချမ်းသာ၏၊ ဆင်းရဲသူတို့၌ ဆင်းရဲ၏၊ ပြုဖွယ်ကိစ္စတို့ ဖြစ်ပေါ်လာသောအခါ မိမိကိုယ်တိုင် ဝင်ရောက် ဆောင်ရွက်၏။
Pubbakālaṃ kodho, aparakālaṃ upanāho. = အစောပိုင်း အချိန်၌ အမျက်ဒေါသ ဖြစ်၏၊ နောက်ပိုင်း အချိန်၌ ရန်ငြိုး သိုထားမှု ဖြစ်၏။
Idhekacco kāyena duccaritaṃ caritvā, vācāya duccaritaṃ caritvā, manasā duccaritaṃ caritvā tassa paṭicchādanahetuṃ pāpikaṃ icchaṃ paṇidahati. = ဤလောက၌ အချို့သော သူသည် ကိုယ်ဖြင့် ဒုစရိုက်ကို ကျင့်၍၊ နှုတ်ဖြင့် ဒုစရိုက်ကို ကျင့်၍၊ မနောဖြင့် ဒုစရိုက်ကို ကျင့်၍ ထိုဒုစရိုက်ကို ဖုံးကွယ်ရန် အလို့ငှာ ယုတ်မာသော အလိုကို ထား၏။
"Mā maṃ jaññā"ti icchati. = “ငါ့ကို မသိပါစေနှင့်”ဟု အလိုရှိ၏။
"Mā maṃ jaññā"ti saṅkappeti. = “ငါ့ကို မသိပါစေနှင့်”ဟု ကြံစည်၏။
"Mā maṃ jaññā"ti vācaṃ bhāsati. = “ငါ့ကို မသိပါစေနှင့်”ဟု စကားကို ပြော၏။
"Mā maṃ jaññā"ti kāyena parakkamati. = “ငါ့ကို မသိပါစေနှင့်”ဟု ကိုယ်ဖြင့် ကြိုးပမ်း၏။
Idhekacco saṭho hoti parisaṭho. = ဤလောက၌ အချို့သော သူသည် စဉ်းလဲသူ ဖြစ်၏၊ အလွန် စဉ်းလဲသူ ဖြစ်၏။
Yā sā vācā kaṇḍakā kakkasā parakaṭukā parābhisajjanī kodhasāmantā asamādhisaṃvattanikā tathārūpiṃ vācaṃ bhāsitā hoti. = ဆူးကဲ့သို့ စူးသော၊ ကြမ်းတမ်းသော၊ သူတစ်ပါးကို ခါးသက်စေသော၊ သူတစ်ပါးကို ထိခိုက်စေသော၊ အမျက်ဒေါသနှင့် နီးစပ်သော၊ သမာဓိ မဖြစ်စေတတ်သော စကား ရှိ၏၊ ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏။
Idha assutavā puthujjano ariyānaṃ adassāvī ariyadhammassa akovido ariyadhamme avinīto, sappurisānaṃ adassāvī sappurisadhammassa akovido sappurisadhamme avinīto – rūpaṃ attato samanupassati rūpavantaṃ vā attānaṃ attani vā rūpaṃ rūpasmiṃ vā attānaṃ. = ဤလောက၌ အကြားအမြင် မရှိသော ပုထုဇဉ်သည် အရိယာတို့ကို မမြင်ဖူးသူ၊ အရိယာတို့၏ တရား၌ မကျွမ်းကျင်သူ၊ အရိယာတို့၏ တရား၌ မလေ့ကျင့်ထားသူ၊ သူတော်ကောင်းတို့ကို မမြင်ဖူးသူ၊ သူတော်ကောင်းတို့၏ တရား၌ မကျွမ်းကျင်သူ၊ သူတော်ကောင်းတို့၏ တရား၌ မလေ့ကျင့်ထားသူ ဖြစ်၍ – ရုပ်ကို အတ္တဟု ရှုမြင်သည်၊ အတ္တကို ရုပ် ရှိသည်ဟုဖြစ်စေ၊ အတ္တ၌ ရုပ် ရှိသည်ဟုဖြစ်စေ၊ ရုပ်၌ အတ္တ ရှိသည်ဟုဖြစ်စေ ရှုမြင်သည်။
Vedanaṃ…pe… saññaṃ…pe… saṅkhāre…pe… viññāṇaṃ attato samanupassati viññāṇavantaṃ vā attānaṃ attani vā viññāṇaṃ viññāṇasmiṃ vā attānaṃ. = ခံစားမှုကို… မှတ်သိမှုကို… ပြုပြင်ဖန်တီးမှုများကို… သိစိတ်ကို အတ္တဟု ရှုမြင်သည်၊ အတ္တကို သိစိတ် ရှိသည်ဟုဖြစ်စေ၊ အတ္တ၌ သိစိတ် ရှိသည်ဟုဖြစ်စေ၊ သိစိတ်၌ အတ္တ ရှိသည်ဟုဖြစ်စေ ရှုမြင်သည်။
Satthari kaṅkhati vicikicchati, dhamme kaṅkhati vicikicchati, saṅghe kaṅkhati vicikicchati, sikkhāya kaṅkhati vicikicchati, pubbante kaṅkhati vicikicchati, aparante kaṅkhati vicikicchati, pubbantāparante kaṅkhati vicikicchati, idappaccayatāpaṭiccasamuppannesu dhammesu kaṅkhati vicikicchati. = ဘုရားရှင်အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်၊ တရားတော်အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်၊ သံဃာတော်အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်၊ ကျင့်စဉ်အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်၊ အတိတ်ကာလအပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်၊ အနာဂတ်ကာလအပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်၊ အတိတ်ကာလနှင့် အနာဂတ်ကာလအပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်၊ ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော သဘောတရားတို့အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်။
Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi vatena suddhi sīlabbatena suddhīti. = ဤသာသနာ အပြင်ဘက်ရှိ ရဟန်းပုဏ္ဏားတို့၏ သီလဖြင့် စင်ကြယ်ခြင်း ရှိသည် အကျင့်ဝတ်ဖြင့် စင်ကြယ်ခြင်း ရှိသည် သီလနှင့် အကျင့်ဝတ်ဖြင့် စင်ကြယ်ခြင်း ရှိသည်ဟူ၍။
Avasesā taṇhā kāmataṇhā. = ကြွင်းကျန်သော တပ်မက်မှုသည် ကာမကို တပ်မက်မှု ဖြစ်သည်။
"Sassato loko"ti vā, "asassato loko"ti – vā…pe… "neva hoti na na hoti tathāgato paraṃ maraṇā"ti vā yā evarūpā diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho – ayaṃ vuccati "brahmacariyesanā". = “လောကသည် မြဲ၏”ဟုဖြစ်စေ၊ “လောကသည် မမြဲ”ဟု – ဖြစ်စေ… “တထာဂတသည် သေပြီးနောက် ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်”ဟုဖြစ်စေ ဤသို့ သဘောရှိသော အယူ၊ အယူမှား… ပြောင်းပြန် စွဲကိုင်ခြင်း ရှိသမျှ – ဤသည်ကို “မြတ်သော အကျင့်ကို ရှာမှီးမှု”ဟု ခေါ်သည်။
So kāmesu pātabyataṃ āpajjati. = ထိုသူသည် ကာမတို့၌ သောက်သုံးသကဲ့သို့ နစ်မွန်းခြင်းသို့ ရောက်၏။
Tattha katame cattāro ganthā …pe… cattāro oghā…pe… cattāro yogā…pe… cattāri upādānāni? = ထိုတို့အနက် အထုံး လေးပါး… ရေအလျဉ် လေးပါး… ထမ်းပိုး လေးပါး… စွဲလမ်းမှု လေးပါး ဟူသည် အဘယ်တို့နည်း။
Chandāgatiṃ gacchati, dosāgatiṃ gacchati, mohāgatiṃ gacchati, bhayāgatiṃ gacchati. = ဆန္ဒ အဂတိသို့ လိုက်၏၊ ဒေါသ အဂတိသို့ လိုက်၏၊ မောဟ အဂတိသို့ လိုက်၏၊ ကြောက်ခြင်း အဂတိသို့ လိုက်၏။
Chandarāgā gehasitā dhammā. = လိုလားမှု ရာဂတို့သည် လောကီ အိမ်ရာကို မှီသော သဘောတရားများ ဖြစ်ကြသည်။
Tattha katamāni nava maññitāni… nava phanditāni… nava papañcitāni… nava saṅkhatāni? = ထိုတို့အနက် ထင်မှတ်မှု ကိုးပါး… လှုပ်ရှားမှု ကိုးပါး… ချဲ့ထွင်မှု ကိုးပါး… ပြုပြင်ထားမှု ကိုးပါး ဟူသည် အဘယ်တို့နည်း။
Natthi dinnaṃ, natthi yiṭṭhaṃ, natthi hutaṃ, natthi sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko, natthi ayaṃ loko, natthi paro loko, natthi mātā, natthi pitā, natthi sattā opapātikā, natthi loke samaṇabrāhmaṇā sammaggatā [samaggatā (ka.)] sammā paṭipannā ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentīti – ayaṃ dasavatthukā micchādiṭṭhi. = ပေးလှူခြင်း မရှိ၊ ယဇ်ပူဇော်ခြင်း မရှိ၊ ပူဇော်သကာ ဆက်ကပ်ခြင်း မရှိ၊ ကောင်းစွာ ပြုသော ကံ၊ ဆိုးစွာ ပြုသော ကံတို့၏ အသီးအပွင့် အကျိုးဆက် မရှိ၊ ဤလောက မရှိ၊ တမလွန် လောက မရှိ၊ အမိ မရှိ၊ အဖ မရှိ၊ အလိုအလျောက် ပေါ်လာသော သတ္တဝါ မရှိ၊ လောက၌ မှန်ကန်စွာ ရောက်ရှိသော [ပါဌ်ကွဲ (Ka.): samaggatā] မှန်ကန်စွာ ကျင့်ကြံသော၊ ဤလောကကိုလည်း တမလွန် လောကကိုလည်း ကိုယ်တိုင် ထူးကဲစွာ သိ၍ မျက်မှောက်ပြုပြီး ဟောကြားသော ရဟန်းပုဏ္ဏားတို့ မရှိဟူ၍ – ဤသည်မှာ အကြောင်းအရာ ဆယ်ပါး ရှိသော မှားယွင်းသော အယူ ဖြစ်သည်။
Ittheke sato sattassa paramadiṭṭhadhammanibbānaṃ paññapenti. = ဤသို့ အချို့သူတို့သည် ရှိနေသော သတ္တဝါ၏ မျက်မှောက်ဘဝ၌ အမြတ်ဆုံး နိဗ္ဗာန်ကို ပညတ်ကြ၏။
Ittheke sato sattassa ucchedaṃ vināsaṃ vibhavaṃ paññapenti. = ဤသို့ အချို့သူတို့သည် ရှိနေသော သတ္တဝါ၏ ပြတ်စဲခြင်း၊ ပျက်စီးခြင်း၊ ဘဝ ပျောက်ကွယ်ခြင်းကို ပညတ်ကြ၏။
Taṃ kissa hetu? = ထိုသို့ အဘယ်ကြောင့်နည်း။
Kāmā hi, bho, aniccā dukkhā vipariṇāmadhammā. = အချင်း၊ ကာမတို့သည် မမြဲကုန်၊ ဆင်းရဲကုန်၊ ဖောက်ပြန်ခြင်း သဘော ရှိကုန်၏။
Tesaṃ vipariṇāmaññathābhāvā uppajjanti sokaparidevadukkhadomanassupāyāsā. = ထိုကာမတို့၏ ဖောက်ပြန်ခြင်း၊ တစ်မျိုးတစ်ဖုံ ဖြစ်ခြင်းကြောင့် စိုးရိမ်ခြင်း၊ ငိုကြွေးခြင်း၊ ကိုယ်ဆင်းရဲခြင်း၊ စိတ်ဆင်းရဲမှု၊ ပြင်းစွာ ပူပန်ခြင်းတို့ ဖြစ်ပေါ်ကြ၏။
No ca kho, bho, ayaṃ attā ettāvatā paramadiṭṭhadhammanibbānappatto hoti. = အချင်း၊ သို့သော် ဤအတ္တသည် ဤမျှဖြင့် မျက်မှောက်ဘဝ၌ အမြတ်ဆုံး နိဗ္ဗာန်သို့ ရောက်သည် မဟုတ်။
No ca kho, bho, ayaṃ attā ettāvatā sammā samucchinno hoti. = အချင်း၊ သို့သော် ဤအတ္တသည် ဤမျှဖြင့် ကောင်းစွာ ပြတ်စဲသည် မဟုတ်။
Neso natthīti vadāmi. = ထိုအတ္တ မရှိဟု ငါ မဆို။
‘Neso natthī’ti vadāmi. = ‘ထိုအတ္တ မရှိ’ဟု ငါ မဆို။
Yadeva tattha vitakkitaṃ vicāritaṃ etena etaṃ oḷārikaṃ akkhāyati. = ထိုဈာန်၌ စတင်ကြံစည်ခြင်း၊ ဆက်လက်သုံးသပ်ခြင်း ရှိသမျှ ထိုအရာကြောင့် ဤဈာန်ကို ရုန့်ရင်းသည်ဟု ဆိုရ၏။
Yadeva tattha pītigataṃ cetaso uppilāvitaṃ, etena etaṃ oḷārikaṃ akkhāyati. = ထိုဈာန်၌ ပီတိ ဖြစ်ခြင်း၊ စိတ်၏ ဖောင်းကြွခြင်း ရှိသမျှ ထိုအရာကြောင့် ဤဈာန်ကို ရုန့်ရင်းသည်ဟု ဆိုရ၏။
Yadeva tattha sukhapīti cetaso ābhogo, etena etaṃ oḷārikaṃ akkhāyati. = ထိုဈာန်၌ သာယာမှုနှင့် ပီတိဟု စိတ်၏ ညွတ်ခြင်း ရှိသမျှ ထိုအရာကြောင့် ဤဈာန်ကို ရုန့်ရင်းသည်ဟု ဆိုရ၏။
Atthi kho bho añño attā dibbo rūpī kāmāvacaro kabaḷīkārabhakkho. = အချင်း၊ နတ်၌ ဖြစ်သော၊ ရုပ် ရှိသော၊ ကာမဘုံနှင့် ဆိုင်သော၊ လုတ်ပြု၍ စားရသော အစာကို စားသော အခြား အတ္တ ရှိ၏။
Atthi kho, bho, añño attā dibbo rūpī manomayo sabbaṅgapaccaṅgī ahīnindriyo. = အချင်း၊ နတ်၌ ဖြစ်သော၊ ရုပ် ရှိသော၊ စိတ်ဖြင့် ဖြစ်သော၊ ကြီးငယ် အင်္ဂါ အားလုံး ပြည့်စုံသော၊ မချို့ယွင်းသော အာရုံခံ စွမ်းရည် ရှိသော အခြား အတ္တ ရှိ၏။
Atthi kho, bho, añño attā sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā ananto ākāsoti ākāsānañcāyatanūpago. = အချင်း၊ ရုပ်ဟု မှတ်သိမှုတို့ကို အလုံးစုံ ကျော်လွန်ခြင်းကြောင့် ထိခိုက်မှုဟု မှတ်သိမှုတို့ ချုပ်ငြိမ်းသွားခြင်းကြောင့် အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှုတို့ကို နှလုံး မသွင်းခြင်းကြောင့် ဟင်းလင်းပြင်သည် အဆုံး မရှိဟု အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်သို့ ရောက်သော အခြား အတ္တ ရှိ၏။
Atthi kho, bho, añño attā sabbaso ākāsānañcāyatanaṃ samatikkamma anantaṃ viññāṇanti viññāṇañcāyatanūpago. = အချင်း၊ အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍ သိစိတ်သည် အဆုံး မရှိဟု အဆုံး မရှိသော သိစိတ် နယ်ပယ်သို့ ရောက်သော အခြား အတ္တ ရှိ၏။
Atthi kho, bho, añño attā sabbaso viññāṇañcāyatanaṃ samatikkamma natthi kiñcīti ākiñcaññāyatanūpago. = အချင်း၊ အဆုံး မရှိသော သိစိတ် နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍ ဘာမျှ မရှိဟု ဘာမျှ မရှိသော နယ်ပယ်သို့ ရောက်သော အခြား အတ္တ ရှိ၏။
Atthi kho, bho, añño attā sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanūpago. = အချင်း၊ ဘာမျှ မရှိသော နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍ မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်သို့ ရောက်သော အခြား အတ္တ ရှိ၏။
Taṃ tvaṃ na jānāsi na passasi. = ထိုအတ္တကို သင် မသိ၊ မမြင်။
Tamahaṃ jānāmi passāmi. = ထိုအတ္တကို ငါ သိ၏၊ မြင်၏။
So kho, bho, attā yato kāyassa bhedā ucchijjati vinassati na hoti paraṃ maraṇā, ettāvatā kho, bho, ayaṃ attā sammāsamucchinno hotī"ti. = အချင်း၊ ထိုအတ္တသည် ခန္ဓာကိုယ် ပြိုကွဲသောအခါ ပြတ်စဲ၏၊ ပျက်စီး၏၊ သေပြီးနောက် မရှိတော့သောကြောင့် အချင်း၊ ဤမျှဖြင့် ဤအတ္တသည် ကောင်းစွာ ပြတ်စဲသည် ဖြစ်၏”ဟု။
So kho, bho, attā yato kāyassa bhedā ucchijjati vinassati na hoti paraṃ maraṇā, ettāvatā kho, bho, ayaṃ attā sammā samucchinno hotī"ti. = အချင်း၊ ထိုအတ္တသည် ခန္ဓာကိုယ် ပြိုကွဲသောအခါ ပြတ်စဲ၏၊ ပျက်စီး၏၊ သေပြီးနောက် မရှိတော့သောကြောင့် အချင်း၊ ဤမျှဖြင့် ဤအတ္တသည် ကောင်းစွာ ပြတ်စဲသည် ဖြစ်၏”ဟု။
Na so jāto nāhosi, na so jāto na bhavissati, nicco dhuvo sassato avipariṇāmadhammo"ti vā panassa saccato thetato diṭṭhi uppajjati. = ထိုအတ္တသည် မွေးဖွားသည် မဟုတ်၊ မဖြစ်ခဲ့၊ ထိုအတ္တသည် မွေးဖွားသည် မဟုတ်၊ မဖြစ်လတ္တံ့၊ မြဲ၏၊ ခိုင်မြဲ၏၊ ထာဝရ တည်၏၊ ဖောက်ပြန်ခြင်း မရှိသော သဘော ရှိ၏”ဟုဖြစ်စေ ထိုသူ၏ အမှန်အားဖြင့် ခိုင်မြဲစွာ အယူ ဖြစ်ပေါ်၏။
Yāni ca dvāsaṭṭhi diṭṭhigatāni brahmajāle veyyākaraṇe vuttāni bhagavatā. = မြတ်စွာဘုရားသည် ဗြဟ္မဇာလ ဒေသနာ၌ ဟောတော်မူခဲ့သော အယူမှား ခြောက်ဆယ့်နှစ်ပါးလည်း ရှိ၏။
Tattha katamāni dvāsaṭṭhi diṭṭhigatāni brahmajāle veyyākaraṇe vuttāni bhagavatā? = ထိုတို့အနက် မြတ်စွာဘုရားသည် ဗြဟ္မဇာလ ဒေသနာ၌ ဟောတော်မူခဲ့သော အယူမှား ခြောက်ဆယ့်နှစ်ပါး ဟူသည် အဘယ်တို့နည်း။
Cattāro sassatavādā, cattāro ekaccasassatikā, cattāro antānantikā, cattāro amarāvikkhepikā, dve adhiccasamuppannikā, soḷasa saññīvādā, aṭṭha asaññīvādā, aṭṭha nevasaññīnāsaññīvādā, satta ucchedavādā, pañca diṭṭhadhammanibbānavādā – imāni dvāsaṭṭhi diṭṭhigatāni brahmajāle veyyākaraṇe vuttāni bhagavatāti. = မြဲသည်ဟု ဆိုသော ဝါဒ လေးပါး၊ အချို့ မြဲသည်ဟု ဆိုသော ဝါဒ လေးပါး၊ အဆုံးနှင့် အဆုံးမဲ့ကို ဆိုသော ဝါဒ လေးပါး၊ ငါးရှဉ့်ကဲ့သို့ လှည့်ပတ် ပြောသော ဝါဒ လေးပါး၊ အကြောင်းမဲ့ ဖြစ်ပေါ်သည်ဟု ဆိုသော ဝါဒ နှစ်ပါး၊ မှတ်သိမှု ရှိသော အတ္တကို ဆိုသော ဝါဒ ဆယ့်ခြောက်ပါး၊ မှတ်သိမှု မရှိသော အတ္တကို ဆိုသော ဝါဒ ရှစ်ပါး၊ မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သော အတ္တကို ဆိုသော ဝါဒ ရှစ်ပါး၊ ပြတ်သည်ဟု ဆိုသော ဝါဒ ခုနစ်ပါး၊ မျက်မှောက်ဘဝ၌ နိဗ္ဗာန်ဟု ဆိုသော ဝါဒ ငါးပါး – ဤသည်တို့မှာ မြတ်စွာဘုရားသည် ဗြဟ္မဇာလ ဒေသနာ၌ ဟောတော်မူခဲ့သော အယူမှား ခြောက်ဆယ့်နှစ်ပါး ဖြစ်ကြသည်ဟူ၍။
Khuddakavatthuvibhaṅgo niṭṭhito. = “အသေးစား အကြောင်းအရာများကို ခွဲခြမ်းစိတ်ဖြာခြင်း” ပြီးဆုံးပြီ။
Aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya, aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā chattiṃsa taṇhāvicaritāni honti. = အတွင်းကို မှီ၍ ဖြစ်သော တပ်မက်မှု၏ ဖြစ်ပုံ ဆယ့်ရှစ်ပါး၊ အပြင်ကို မှီ၍ ဖြစ်သော တပ်မက်မှု၏ ဖြစ်ပုံ ဆယ့်ရှစ်ပါး၊ ထိုအားလုံးကို တစ်စုတည်း ပေါင်းစု၍ အကျဉ်းချုံ့၍ တပ်မက်မှု၏ ဖြစ်ပုံ သုံးဆယ့်ခြောက်ပါး ဖြစ်ကြ၏။
Iti atītāni chattiṃsa taṇhāvicaritāni, anāgatāni chattiṃsa taṇhāvicaritāni, paccuppannāni chattiṃsa taṇhāvicaritāni, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā aṭṭha taṇhāvicaritasataṃ hoti. = ဤသို့ အတိတ် တပ်မက်မှု၏ ဖြစ်ပုံ သုံးဆယ့်ခြောက်ပါး၊ အနာဂတ် တပ်မက်မှု၏ ဖြစ်ပုံ သုံးဆယ့်ခြောက်ပါး၊ ပစ္စုပ္ပန် တပ်မက်မှု၏ ဖြစ်ပုံ သုံးဆယ့်ခြောက်ပါး၊ ထိုအားလုံးကို တစ်စုတည်း ပေါင်းစု၍ အကျဉ်းချုံ့၍ တပ်မက်မှု၏ ဖြစ်ပုံ တစ်ရာ့ရှစ်ပါး ဖြစ်၏။
Imāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya. = ဤသည်တို့မှာ အတွင်းကို မှီ၍ ဖြစ်သော တပ်မက်မှု၏ ဖြစ်ပုံ ဆယ့်ရှစ်ပါး ဖြစ်ကြသည်။
Imāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya. = ဤသည်တို့မှာ အပြင်ကို မှီ၍ ဖြစ်သော တပ်မက်မှု၏ ဖြစ်ပုံ ဆယ့်ရှစ်ပါး ဖြစ်ကြသည်။
Iti imāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya, imāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā chattiṃsa taṇhāvicaritāni honti. = ဤသို့ ဤအတွင်းကို မှီ၍ ဖြစ်သော တပ်မက်မှု၏ ဖြစ်ပုံ ဆယ့်ရှစ်ပါး၊ ဤအပြင်ကို မှီ၍ ဖြစ်သော တပ်မက်မှု၏ ဖြစ်ပုံ ဆယ့်ရှစ်ပါး၊ ထိုအားလုံးကို တစ်စုတည်း ပေါင်းစု၍ အကျဉ်းချုံ့၍ တပ်မက်မှု၏ ဖြစ်ပုံ သုံးဆယ့်ခြောက်ပါး ဖြစ်ကြ၏။
Iti evarūpāni atītāni chattiṃsa taṇhāvicaritāni, anāgatāni chattiṃsa taṇhāvicaritāni, paccuppannāni chattiṃsa taṇhāvicaritāni, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā aṭṭhataṇhāvicaritasataṃ hoti. = ဤသို့ ဤသို့ သဘောရှိသော အတိတ် တပ်မက်မှု၏ ဖြစ်ပုံ သုံးဆယ့်ခြောက်ပါး၊ အနာဂတ် တပ်မက်မှု၏ ဖြစ်ပုံ သုံးဆယ့်ခြောက်ပါး၊ ပစ္စုပ္ပန် တပ်မက်မှု၏ ဖြစ်ပုံ သုံးဆယ့်ခြောက်ပါး၊ ထိုအားလုံးကို တစ်စုတည်း ပေါင်းစု၍ အကျဉ်းချုံ့၍ တပ်မက်မှု၏ ဖြစ်ပုံ တစ်ရာ့ရှစ်ပါး ဖြစ်၏။
Tattha katamāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya? = ထိုတို့အနက် အတွင်းကို မှီ၍ ဖြစ်သော တပ်မက်မှု၏ ဖြစ်ပုံ ဆယ့်ရှစ်ပါး ဟူသည် အဘယ်တို့နည်း။
Tattha katamāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya? = ထိုတို့အနက် အပြင်ကို မှီ၍ ဖြစ်သော တပ်မက်မှု၏ ဖြစ်ပုံ ဆယ့်ရှစ်ပါး ဟူသည် အဘယ်တို့နည်း။

### Kusītavatthu (new)
So nipajjati; na vīriyaṃ ārabhati appattassa pattiyā, anadhigatassa adhigamāya, asacchikatassa sacchikiriyāya. = ထိုရဟန်းသည် လှဲလျောင်း၏၊ မရောက်သေးသည်ကို ရောက်ရန်၊ မရရှိသေးသည်ကို ရရှိရန်၊ မျက်မှောက် မပြုရသေးသည်ကို မျက်မှောက်ပြုရန် ဝီရိယကို မအားထုတ်။
idha bhikkhunā kammaṃ kātabbaṃ hoti. = ဤသာသနာ၌ ရဟန်းသည် ပြုရမည့် အလုပ် ရှိ၏။
Tassa evaṃ hoti – "kammaṃ kho me kātabbaṃ bhavissati. = ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “ငါ ပြုရမည့် အလုပ် ရှိလိမ့်မည်။
Kammaṃ kho pana me karontassa kāyo kilamissati. = အလုပ်ကို ပြုနေသော ငါ၏ ကိုယ်သည် ပင်ပန်းလိမ့်မည်။
Handāhaṃ nipajjāmī"ti. = ယခု ငါ လှဲလျောင်းအံ့”ဟု။
puna caparaṃ bhikkhunā kammaṃ kataṃ hoti. = တစ်ဖန် နောက်တစ်မျိုးမှာ ရဟန်းသည် အလုပ်ကို ပြုပြီး ဖြစ်၏။
Tassa evaṃ hoti – "ahaṃ kho kammaṃ akāsiṃ. = ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “ငါ အလုပ်ကို ပြုခဲ့ပြီ။
Kammaṃ kho pana me karontassa kāyo kilanto. = အလုပ်ကို ပြုနေသော ငါ၏ ကိုယ်သည် ပင်ပန်းပြီ။
puna caparaṃ bhikkhunā maggo gantabbo hoti. = တစ်ဖန် နောက်တစ်မျိုးမှာ ရဟန်းသည် သွားရမည့် ခရီး ရှိ၏။
Tassa evaṃ hoti – "maggo kho me gantabbo bhavissati. = ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “ငါ သွားရမည့် ခရီး ရှိလိမ့်မည်။
Maggaṃ kho pana me gacchantassa kāyo kilamissati. = ခရီးကို သွားနေသော ငါ၏ ကိုယ်သည် ပင်ပန်းလိမ့်မည်။
puna caparaṃ bhikkhunā maggo gato hoti. = တစ်ဖန် နောက်တစ်မျိုးမှာ ရဟန်းသည် ခရီးကို သွားပြီး ဖြစ်၏။
Tassa evaṃ hoti – "ahaṃ kho maggaṃ agamāsiṃ. = ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “ငါ ခရီးကို သွားခဲ့ပြီ။
Maggaṃ kho pana me gacchantassa kāyo kilanto. = ခရီးကို သွားနေသော ငါ၏ ကိုယ်သည် ပင်ပန်းပြီ။
puna caparaṃ bhikkhu gāmaṃ vā nigamaṃ vā piṇḍāya caranto na labhati lūkhassa vā paṇītassa vā bhojanassa yāvadatthaṃ pāripūriṃ. = တစ်ဖန် နောက်တစ်မျိုးမှာ ရဟန်းသည် ရွာသို့ဖြစ်စေ၊ နိဂုံးသို့ဖြစ်စေ ဆွမ်းခံ လှည့်လည်လျက် ကြမ်းတမ်းသော အစာ၏ဖြစ်စေ၊ မွန်မြတ်သော အစာ၏ဖြစ်စေ လိုသလောက် ပြည့်စုံမှုကို မရ။
Tassa evaṃ hoti – "ahaṃ kho gāmaṃ vā nigamaṃ vā piṇḍāya caranto nālatthaṃ lūkhassa vā paṇītassa vā bhojanassa yāvadatthaṃ pāripūriṃ. = ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “ငါ ရွာသို့ဖြစ်စေ၊ နိဂုံးသို့ဖြစ်စေ ဆွမ်းခံ လှည့်လည်လျက် ကြမ်းတမ်းသော အစာ၏ဖြစ်စေ၊ မွန်မြတ်သော အစာ၏ဖြစ်စေ လိုသလောက် ပြည့်စုံမှုကို မရခဲ့။
Tassa me kāyo kilanto akammañño. = ထိုငါ၏ ကိုယ်သည် ပင်ပန်း၏၊ အလုပ်နှင့် မလျော်။
puna caparaṃ bhikkhu gāmaṃ vā nigamaṃ vā piṇḍāya caranto labhati lūkhassa vā paṇītassa vā bhojanassa yāvadatthaṃ pāripūriṃ. = တစ်ဖန် နောက်တစ်မျိုးမှာ ရဟန်းသည် ရွာသို့ဖြစ်စေ၊ နိဂုံးသို့ဖြစ်စေ ဆွမ်းခံ လှည့်လည်လျက် ကြမ်းတမ်းသော အစာ၏ဖြစ်စေ၊ မွန်မြတ်သော အစာ၏ဖြစ်စေ လိုသလောက် ပြည့်စုံမှုကို ရ၏။
Tassa evaṃ hoti – "ahaṃ kho gāmaṃ vā nigamaṃ vā piṇḍāya caranto alatthaṃ lūkhassa vā paṇītassa vā bhojanassa yāvadatthaṃ pāripūriṃ. = ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “ငါ ရွာသို့ဖြစ်စေ၊ နိဂုံးသို့ဖြစ်စေ ဆွမ်းခံ လှည့်လည်လျက် ကြမ်းတမ်းသော အစာ၏ဖြစ်စေ၊ မွန်မြတ်သော အစာ၏ဖြစ်စေ လိုသလောက် ပြည့်စုံမှုကို ရခဲ့ပြီ။
Tassa me kāyo kilanto akammañño māsācitaṃ maññe. = ထိုငါ၏ ကိုယ်သည် ပင်ပန်း၏၊ အလုပ်နှင့် မလျော်၊ ပဲတင်ထားသကဲ့သို့ လေးလံ၏ဟု ထင်၏။
puna caparaṃ bhikkhuno uppanno hoti appamattako ābādho. = တစ်ဖန် နောက်တစ်မျိုးမှာ ရဟန်းအား အနည်းငယ်သော အနာရောဂါ ဖြစ်ပေါ်၏။
Tassa evaṃ hoti – "uppanno kho me ayaṃ appamattako ābādho. = ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “ငါ့အား ဤအနည်းငယ်သော အနာရောဂါ ဖြစ်ပေါ်ပြီ။
Atthi kappo nipajjituṃ. = လှဲလျောင်းရန် သင့်လျော်၏။
puna caparaṃ bhikkhu gilānā vuṭṭhito [gilānavuṭṭhito (saddanībhi) a. ni. 6.16 pāḷiyā ṭīkā passitabbā] hoti aciravuṭṭhito gelaññā. = တစ်ဖန် နောက်တစ်မျိုးမှာ ရဟန်းသည် ဖျားနာခြင်းမှ ထပြီး [စာလုံးပေါင်းကွဲ (Saddanīti): gilānavuṭṭhito၊ “အင်္ဂုတ္တရနိကာယ်” 6.16 ပါဠိ၏ ဋီကာကို ကြည့်ပါ] ဖြစ်၏၊ ဖျားနာခြင်းမှ ထသည်မှာ မကြာသေး။
Tassa evaṃ hoti – "ahaṃ kho gilānā vuṭṭhito aciravuṭṭhito gelaññā. = ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်၏ – “ငါ ဖျားနာခြင်းမှ ထပြီး ဖြစ်၏၊ ဖျားနာခြင်းမှ ထသည်မှာ မကြာသေး။
Tassa me kāyo dubbalo akammañño. = ထိုငါ၏ ကိုယ်သည် အားနည်း၏၊ အလုပ်နှင့် မလျော်။

### Purisadosa (new)
idha bhikkhū bhikkhuṃ āpattiyā codenti. = ဤသာသနာ၌ ရဟန်းတို့သည် ရဟန်းကို အာပတ်ဖြင့် စောဒနာကြ၏။
puna caparaṃ bhikkhū bhikkhuṃ āpattiyā codenti. = တစ်ဖန် နောက်တစ်မျိုးမှာ ရဟန်းတို့သည် ရဟန်းကို အာပတ်ဖြင့် စောဒနာကြ၏။
So bhikkhu bhikkhūhi āpattiyā codiyamāno [codiyamāno (sī. syā.) a. ni. 8.14] "na sarāmi na sarāmī"ti assatiyāva nibbeṭheti. = ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ [စာလုံးပေါင်းကွဲ (Sī., Syā.): codiyamāno၊ “အင်္ဂုတ္တရနိကာယ်” 8.14] “ငါ မမှတ်မိ၊ ငါ မမှတ်မိ”ဟု သတိ မရှိဟန်ဖြင့်သာ ငြင်းဆို၏။
So bhikkhu bhikkhūhi āpattiyā codiyamāno codakaṃyeva paṭippharati – "kiṃ nu kho tuyhaṃ bālassa abyattassa bhaṇitena! Tvampi nāma maṃ bhaṇitabbaṃ maññasī"ti! Ayaṃ dutiyo purisadoso. = ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ စောဒနာသူကိုသာ ပြန်လည် တိုက်ခိုက်၏ – “မိုက်မဲ၍ မလိမ္မာသော သင်၏ ပြောဆိုမှုဖြင့် အဘယ် အကျိုး ရှိမည်နည်း။ သင်ပင်လျှင် ငါ့ကို ပြောဆိုထိုက်သည်ဟု ထင်သလော”ဟု။ ဤသည်မှာ ဒုတိယ လူ၏ အပြစ် ဖြစ်သည်။
So bhikkhu bhikkhūhi āpattiyā codiyamāno codakaṃyeva [codakasseva (syā.) a. ni. 8.14] paccāropeti – "tvampi khosi itthannāmaṃ āpattiṃ āpanno. = ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ စောဒနာသူကိုသာ [ပါဌ်ကွဲ (Syā.): codakasseva၊ “အင်္ဂုတ္တရနိကာယ်” 8.14] ပြန်လည် စွပ်စွဲ၏ – “သင်လည်း ဤမည်သော အာပတ်သို့ ရောက်ခဲ့ပြီ။
Tvaṃ tāva paṭhamaṃ paṭikarohī"ti. = သင် ဦးစွာ ကုစားလော့”ဟု။
So bhikkhu bhikkhūhi āpattiyā codiyamāno aññenāññaṃ paṭicarati, bahiddhā kathaṃ apanāmeti, kopañca dosañca appaccayañca pātukaroti. = ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ တစ်ခုဖြင့် တစ်ခုကို လွှဲရှောင်၏၊ စကားကို ပြင်ပသို့ လွှဲ၏၊ အမျက်ကိုလည်းကောင်း၊ ဒေါသကိုလည်းကောင်း၊ မနှစ်သက်မှုကိုလည်းကောင်း ထင်ရှားစေ၏။
So bhikkhu bhikkhūhi āpattiyā codiyamāno saṅghamajjhe bāhāvikkhepakaṃ bhaṇati. = ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ သံဃာ့အလယ်၌ လက်ကို ဝှေ့ယမ်း၍ ပြောဆို၏။
So bhikkhu bhikkhūhi āpattiyā codiyamāno anādiyitvā saṅghaṃ, anādiyitvā codakaṃ, sāpattikova [āpattikova (ka.) a. ni. 8.14] yenakāmaṃ pakkamati. = ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ သံဃာကို အလေးမထား၍၊ စောဒနာသူကို အလေးမထား၍ အာပတ် ရှိလျက်ပင် [ပါဌ်ကွဲ (Ka.): āpattikova၊ “အင်္ဂုတ္တရနိကာယ်” 8.14] အလိုရှိရာသို့ ထွက်သွား၏။
So bhikkhu bhikkhūhi āpattiyā codiyamāno "nevāhaṃ āpannomhi, na panāhaṃ anāpannomhī"ti tuṇhībhūto saṅghaṃ viheseti. = ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ “ငါ အာပတ်သင့်သည်လည်း မဟုတ်၊ အာပတ် မသင့်သည်လည်း မဟုတ်”ဟု ဆိတ်ဆိတ် နေ၍ သံဃာကို နှောင့်ယှက်၏။
So bhikkhu bhikkhūhi āpattiyā codiyamāno evamāha – "kiṃ nu kho tumhe āyasmanto atibāḷhaṃ mayi byāvaṭā. = ထိုရဟန်းသည် ရဟန်းတို့က အာပတ်ဖြင့် စောဒနာခံရသောအခါ ဤသို့ ဆို၏ – “အသျှင်တို့ သင်တို့သည် ငါ့အပေါ် အဘယ်ကြောင့် အလွန်အမင်း ဂရုစိုက်နေကြသနည်း။
Idānāhaṃ sikkhaṃ paccakkhāya hīnāyāvattissāmī"ti. = ယခု ငါ သိက္ခာကို စွန့်၍ လူဘောင်သို့ ပြန်လည်မည်”ဟု။
So sikkhaṃ paccakkhāya hīnāyāvattitvā evamāha – "idāni kho tumhe āyasmanto attamanā hothā"ti. = ထိုရဟန်းသည် သိက္ခာကို စွန့်၍ လူဘောင်သို့ ပြန်လည်ပြီး ဤသို့ ဆို၏ – “အသျှင်တို့ ယခု သင်တို့ စိတ်ကျေနပ်ကြလော့”ဟု။

### Taṇhāvicarita phrases (new)
asmi = ငါ ရှိ၏
itthasmi = ငါ ဤကဲ့သို့ ဖြစ်၏
evasmi = ငါ ထိုနည်းတူ ဖြစ်၏
aññathāsmi = ငါ အခြားတစ်မျိုး ဖြစ်၏
bhavissaṃ = ငါ ဖြစ်လိမ့်မည်
itthaṃ bhavissaṃ = ငါ ဤကဲ့သို့ ဖြစ်လိမ့်မည်
evaṃ bhavissaṃ = ငါ ထိုနည်းတူ ဖြစ်လိမ့်မည်
aññathā bhavissaṃ = ငါ အခြားတစ်မျိုး ဖြစ်လိမ့်မည်
asasmi = ငါ အမြဲ ရှိ၏
sātasmi = ငါ ပြတ်စဲ၏
siyaṃ = ငါ ဖြစ်ရာ၏
itthaṃ siyaṃ = ငါ ဤကဲ့သို့ ဖြစ်ရာ၏
evaṃ siyaṃ = ငါ ထိုနည်းတူ ဖြစ်ရာ၏
aññathā siyaṃ = ငါ အခြားတစ်မျိုး ဖြစ်ရာ၏
apāhaṃ siyaṃ = ငါ ဖြစ်ရလျှင် ကောင်းမည်
apāhaṃ itthaṃ siyaṃ = ငါ ဤကဲ့သို့ ဖြစ်ရလျှင် ကောင်းမည်
apāhaṃ evaṃ siyaṃ = ငါ ထိုနည်းတူ ဖြစ်ရလျှင် ကောင်းမည်
apāhaṃ aññathā siyaṃ = ငါ အခြားတစ်မျိုး ဖြစ်ရလျှင် ကောင်းမည်

### Persons (taṇhāvicarita; new)
khattiyo = မင်းမျိုး
brāhmaṇo = ပုဏ္ဏား
vesso = ကုန်သည်မျိုး
suddo = သူဆင်းရဲမျိုး
gahaṭṭho = လူဝတ်ကြောင်
pabbajito = ရဟန်း
devo = နတ်
manusso = လူ
rūpī = ရုပ် ရှိသူ
arūpī = ရုပ် မရှိသူ
saññī = မှတ်သိမှု ရှိသူ
asaññī = မှတ်သိမှု မရှိသူ
nevasaññīnāsaññī = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ

