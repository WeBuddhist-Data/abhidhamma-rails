# pi-2 Burmese zero-shot, chapter 6 (Paṭiccasamuppādavibhaṅgo): working notes

Scope: 6-paticcasamuppadavibhango.md. Brief: burmese-zeroshot-brief.md. Pāli only; no Burmese translation or nissaya
consulted, no web search; my2_formulas.py, my2-zeroshot-terms.md and pi-1-my/ read only (nothing written there);
make_sample.py not run.

## Status (2026-11-17): done
- [x] 6-paticcasamuppadavibhango.md: 145 segments, 413 non-empty lines (Suttanta part, Abhidhamma part with the
  four tetrads, Mātikā, the four tetrads per citta, the akusala / kusala / abyākata / avijjāmūlaka / kusalamūlaka /
  akusalamūlaka niddesas).
- check_chapter_ids / pi-6-mr/check_text_pe / pi-4-mr/check_marks: OK (my chk-pe copy deleted).
- check_ch6.py: 0 mismatches (204 definition lists checked); pi-1 reuse 121 / 121 identical; opening test: the
  generator's cittuppāda composer reproduces 37 / 37 pi-1 openings (final pi-1 Burmese) it can parse.
- Regenerate: `python3 -I -X utf8 make_ch6.py` (writes only the chapter). Check: `check_ch6.py <pāli> <my>`.
  Nothing committed.

## Method
- make_ch6.py imports my2_formulas (tables only extended in memory: VAR_KIND for 8 new variant words, sigla
  «bahūsu» = «Bahūsu»); own clause engine (RULES + SEP as the sample), any unmatched text raises Miss.
- pi-1 FINAL Burmese read from the rails text, counts asserted: the synonym lists (moha, cetanā, citta, phassa, the
  five vedanā lists, lobha head 7, diṭṭhi, dosa head + tail, vicikicchā, uddhacca, alobha, adosa, paññā (^1-292),
  saddhā head 4, rūpassa jarā / aniccatā, «Dukkhe aññāṇaṃ …» head 4); the jhāna / path openings (P1_OPEN, exact
  Pāli); the twelve links of ^1-1343 («Aကြောင့် B ဖြစ်ပေါ်သည်», paccayā = ကြောင့်, saḷāyatana = «အာရုံခံ နယ်ပယ်
  ခြောက်ပါး», nāmarūpa = «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း», the final «… တို့ ဖြစ်ပေါ်ကြသည်», evametassa … = «ဤသို့
  ဤဒုက္ခ အစုအဝေး အားလုံး၏ ဖြစ်ပေါ်ခြင်း ရှိသည်»); every reused string is asserted present in the pi-1 text.
- Cittuppāda openings composed in pi-1 order: one group = «OBJ… YAMYAM QUALS KINDသည် [ADV] ဖြစ်ပေါ်ပြီးသော»;
  several kinds (vipāka sense minds, kiriyā) = groups joined by «… » (pi-1 2-04/2-05); one kind with several
  quality groups = «KINDသည် Q1… Q2… OBJS ဖြစ်ပေါ်ပြီးသော» (pi-1 vipāka / kiriyā manoviññāṇadhātu). Verified 37/37.
- Links: statement «Aကြောင့်[လည်း] [Q] B ဖြစ်ပေါ်သည်»; noun phrase (questions, closers) «Aကြောင့် ဖြစ်သော B» /
  with quality «Aကြောင့် ဖြစ်၍ Q B». saṅkhāra as condition is plural in the Suttanta part (pi-1 ^1-1343:
  ပြုပြင်ဖန်တီးမှုများကြောင့်), singular in the Abhidhamma part (saṅkhāro, one cetanā).
- «idaṃ / ayaṃ vuccati "X"» = «ဤသည်ကို “X”ဟု ခေါ်သည်» (sample frame; the Pāli quotes kept, as written; ime vuccanti =
  ဤသည်တို့ကို). Lists «Yo / Yā / Yaṃ L –» = «L ရှိသမျှ –» (pi-1).

## New strings («Pāli = Burmese»; for the consistency pass)
jarāmaraṇaṃ = အိုခြင်းနှင့် သေခြင်း
chaṭṭhāyatanaṃ = ဆဋ္ဌမ အာရုံခံ နယ်ပယ်
kusalamūlā = ကုသိုလ်၏ အမြစ်များ
akusalamūla(paccayā) = အကုသိုလ်၏ အမြစ်များ
adhimokkho = ဆုံးဖြတ်မှု
pasādo (confidence) = ကြည်ညိုမှု
Xhetuka (avijjāhetuko …) = Xကို အကြောင်းပြုသော
(… nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ: the member) = ယင်းတို့အနက်
Evametesaṃ dhammānaṃ samudayo hoti = ဤသို့ ဤသဘောတရားများ၏ ဖြစ်ပေါ်ခြင်း ရှိသည်
saṅgati = စုဝေးခြင်း
samāgamo = ဆုံဆည်းခြင်း
samodhānaṃ = ပေါင်းစည်းခြင်း
pātubhāvo = ထင်ရှား လာခြင်း
«X»ti (lemma of a quoted statement) = “X”ဟူရာ၌
tena vuccati «X»ti = ထို့ကြောင့် “X”ဟု ဆိုသည်
puññābhisaṅkhāro = ကောင်းမှု ဖြစ်စေသော ပြုပြင်ဖန်တီးမှု
apuññābhisaṅkhāro = မကောင်းမှု ဖြစ်စေသော ပြုပြင်ဖန်တီးမှု
āneñjābhisaṅkhāro = မတုန်လှုပ်သော ပြုပြင်ဖန်တီးမှု
kāyasaṅkhāro = ကိုယ် ပြုပြင်ဖန်တီးမှု
vacīsaṅkhāro = နှုတ် ပြုပြင်ဖန်တီးမှု
cittasaṅkhāro = စိတ် ပြုပြင်ဖန်တီးမှု
kammabhavo = ကံ ဘဝ
upapattibhavo = ပဋိသန္ဓေ ဘဝ
tajjācakkhuviññāṇadhātu = သက်ဆိုင်ရာ မျက်စိ သိစိတ် ဓာတ်
tajjākāyaviññāṇadhātu = သက်ဆိုင်ရာ ကိုယ် သိစိတ် ဓာတ်
tajjāmanodhātu = သက်ဆိုင်ရာ မနော ဓာတ်
sañjāti = ကောင်းစွာ မွေးဖွားခြင်း
okkanti = သက်ဆင်းခြင်း
abhinibbatti = ထင်ရှားစွာ ပေါ်ထွက်ခြင်း
khandhānaṃ pātubhāvo = အစုအဝေးတို့၏ ထင်ရှား လာခြင်း
āyatanānaṃ paṭilābho = အာရုံခံ နယ်ပယ်တို့ကို ရရှိခြင်း
nibbatti = ပေါ်ထွက်ခြင်း
cuti = စုတေခြင်း
cavanatā = ရွေ့လျောခြင်း
maccu = သေမင်း
kālakiriyā = ကွယ်လွန်ခြင်း
khandhānaṃ bhedo = အစုအဝေးတို့၏ ကွဲခြင်း
kaḷevarassa nikkhepo = ကိုယ်ခန္ဓာကို စွန့်ပစ်ခြင်း
jīvitindriyassupacchedo = အသက်၏ စွမ်းရည် ပြတ်စဲခြင်း
socanā = စိုးရိမ်နေခြင်း
socitattaṃ = စိုးရိမ်ထားသော အဖြစ်
antosoko = အတွင်း စိုးရိမ်ခြင်း
antoparisoko = အတွင်း ပြင်းစွာ စိုးရိမ်ခြင်း
cetaso parijjhāyanā = စိတ်၏ လောင်မြိုက်ခြင်း
sokasallaṃ = စိုးရိမ်ခြင်းဟူသော ငြောင့်
ādevo = ငိုခြင်း
ādevanā = ငိုနေခြင်း
paridevanā = ငိုကြွေးနေခြင်း
ādevitattaṃ = ငိုထားသော အဖြစ်
paridevitattaṃ = ငိုကြွေးထားသော အဖြစ်
vācā palāpo = စကား ပေါက်ကရ ပြောခြင်း
vippalāpo = အမျိုးမျိုး ပေါက်ကရ ပြောခြင်း
lālappo = ညည်းတွားခြင်း
lālappanā = ညည်းတွားနေခြင်း
lālappitattaṃ = ညည်းတွားထားသော အဖြစ်
āyāso = ပူပန်ခြင်း
āyāsitattaṃ = ပူပန်ထားသော အဖြစ်
upāyāsitattaṃ = ပြင်းစွာ ပူပန်ထားသော အဖြစ်
cittassa adhimokkho = စိတ်၏ ဆုံးဖြတ်မှု
adhimuccanā = ဆုံးဖြတ်ခြင်း
tadadhimuttatā = ထိုအာရုံ၌ ဆုံးဖြတ်ထားသော အဖြစ်
tamhi tamhi sattanikāye = ထိုထို သတ္တဝါ အမျိုးအစား၌
tamhā tamhā sattanikāyā = ထိုထို သတ္တဝါ အမျိုးအစားမှ
tesaṃ tesaṃ dhammānaṃ = ထိုထို သဘောတရားတို့၏
cakkhusamphasso = မျက်စိ၏ တွေ့ထိမှု
sotasamphasso = နား၏ တွေ့ထိမှု
ghānasamphasso = နှာခေါင်း၏ တွေ့ထိမှု
jivhāsamphasso = လျှာ၏ တွေ့ထိမှု
kāyasamphasso = ကိုယ်၏ တွေ့ထိမှု
manosamphasso = မနော၏ တွေ့ထိမှု
cakkhāyatanassa upacayo = မျက်စိ အာရုံခံ နယ်ပယ်၏ တိုးပွားခြင်း
sotāyatanassa upacayo = နား အာရုံခံ နယ်ပယ်၏ တိုးပွားခြင်း
ghānāyatanassa upacayo = နှာခေါင်း အာရုံခံ နယ်ပယ်၏ တိုးပွားခြင်း
jivhāyatanassa upacayo = လျှာ အာရုံခံ နယ်ပယ်၏ တိုးပွားခြင်း
kāyāyatanassa upacayo = ကိုယ် အာရုံခံ နယ်ပယ်၏ တိုးပွားခြင်း
rūpataṇhā = အဆင်းအရောင်ကို တပ်မက်မှု
saddataṇhā = အသံကို တပ်မက်မှု
gandhataṇhā = အနံ့ကို တပ်မက်မှု
rasataṇhā = အရသာကို တပ်မက်မှု
phoṭṭhabbataṇhā = အထိအတွေ့ကို တပ်မက်မှု
dhammataṇhā = သဘောတရားကို တပ်မက်မှု
kāmabhavo = ကာမဘုံ၌ ဖြစ်သော ဘဝ
rūpabhavo = သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ
arūpabhavo = ရုပ်မရှိသော ဘုံ၌ ဖြစ်သော ဘဝ
saññābhavo = မှတ်သိမှု ရှိသော ဘဝ
asaññābhavo = မှတ်သိမှု မရှိသော ဘဝ
nevasaññānāsaññābhavo = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော ဘဝ
ekavokārabhavo = အစုအဝေး တစ်ပါး ရှိသော ဘဝ
catuvokārabhavo = အစုအဝေး လေးပါး ရှိသော ဘဝ
pañcavokārabhavo = အစုအဝေး ငါးပါး ရှိသော ဘဝ
-catukkaṃ (set of four) = လေးမျိုးတွဲ
Paccayacatukkaṃ = အကြောင်း လေးမျိုးတွဲ
Hetucatukkaṃ = အကြောင်းပြုခြင်း လေးမျိုးတွဲ
Sampayuttacatukkaṃ = ယှဉ်တွဲခြင်း လေးမျိုးတွဲ
Aññamaññacatukkaṃ = အချင်းချင်း အကြောင်းဖြစ်ခြင်း လေးမျိုးတွဲ
Akusalaniddeso = အကုသိုလ်ကို အကျယ် ဖော်ပြချက်
Kusalaniddeso = ကုသိုလ်ကို အကျယ် ဖော်ပြချက်
Abyākataniddeso = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို အကျယ် ဖော်ပြချက်
Avijjāmūlakakusalaniddeso = အမှန်ကို မသိမှုကို အခြေခံသော ကုသိုလ်ကို အကျယ် ဖော်ပြချက်
Kusalamūlakavipākaniddeso = ကုသိုလ်၏ အမြစ်များကို အခြေခံသော ကံ၏ အကျိုးကို အကျယ် ဖော်ပြချက်
Akusalamūlakavipākaniddeso = အကုသိုလ်၏ အမြစ်များကို အခြေခံသော ကံ၏ အကျိုးကို အကျယ် ဖော်ပြချက်
Paṭiccasamuppādavibhaṅgo = အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā = ကာမဘုံနှင့် ဆိုင်သော၊ သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော၊ ဒါနမှ ဖြစ်သော၊ သီလမှ ဖြစ်သော၊ ဘာဝနာမှ ဖြစ်သော ကုသိုလ် စေ့ဆော်မှု
Akusalā cetanā kāmāvacarā = ကာမဘုံနှင့် ဆိုင်သော အကုသိုလ် စေ့ဆော်မှု
Kusalā cetanā arūpāvacarā = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ကုသိုလ် စေ့ဆော်မှု
Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro = ကိုယ်ဖြင့် စေ့ဆော်ခြင်းသည် ကိုယ် ပြုပြင်ဖန်တီးမှု ဖြစ်သည်၊ နှုတ်ဖြင့် စေ့ဆော်ခြင်းသည် နှုတ် ပြုပြင်ဖန်တီးမှု ဖြစ်သည်၊ မနောဖြင့် စေ့ဆော်ခြင်းသည် စိတ် ပြုပြင်ဖန်တီးမှု ဖြစ်သည်
Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati = မနော သိစိတ် ဓာတ်သည် မှီ၍ ဖြစ်ပေါ်ရာ ရုပ် ရှိသမျှ
Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati = မူလဓာတ်ကြီး လေးပါးလည်းကောင်း၊ မနော သိစိတ် ဓာတ်သည် မှီ၍ ဖြစ်ပေါ်ရာ ရုပ်လည်းကောင်း
Sabbampi bhavagāmikammaṃ kammabhavo = ဘဝသို့ ဦးတည်သော ကံ အားလုံးသည်လည်း ကံ ဘဝ ဖြစ်သည်
Ñātibyasanena vā phuṭṭhassa … dukkhadhammena phuṭṭhassa = ဆွေမျိုး ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ၊ စည်းစိမ် ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ၊ ကျန်းမာရေး ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ၊ သီလ ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ၊ အယူ ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ၊ တစ်ခုခုသော ပျက်စီးခြင်းနှင့် ကြုံတွေ့နေရသူ၏၊ တစ်ခုခုသော ဆင်းရဲဖွယ်ရာဖြင့် ထိခိုက်ခံရသူ၏

## Choices to confirm
- hetuka = «Xကို အကြောင်းပြုသော» as pi-1 cittahetukaṃ («စိတ်ကို အကြောင်းပြုသော»), kept apart from paccayā «ကြောင့်».
- «viññāṇapaccayā nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ» (only nāma is associated): statement «သိစိတ်ကြောင့်
  စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း ဖြစ်ပေါ်သည်၊ ယင်းတို့အနက် စိတ်ပိုင်းသည် သိစိတ်နှင့် ယှဉ်တွဲသည်»; noun phrase «…ကြောင့်
  ဖြစ်သော စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း၊ ယင်းတို့အနက် သိစိတ်နှင့် ယှဉ်တွဲသော စိတ်ပိုင်း» (same for saḷāyatanaṃ
  nāmasampayuttaṃ chaṭṭhāyatanaṃ).
- chaṭṭhāyatana = «ဆဋ္ဌမ အာရုံခံ နယ်ပယ်» (ordinal ဆဋ္ဌမ as pi-1 Chaṭṭhaṃ); jarāmaraṇa alone = «အိုခြင်းနှင့်
  သေခြင်း» (dvandva with နှင့်, as nāmarūpa); in the full formula the pi-1 list «အိုခြင်း၊ သေခြင်း၊ …» stays.
- pasāda here = confidence (defined by saddhā) «ကြည်ညိုမှု», kept apart from pi-1 pasāda = sense sensitivity
  «အာရုံခံ ကြည်လင်မှု» and abhippasāda «ကြည်ညိုလေးစားခြင်း».
- adhimokkha (not in pi-1) «ဆုံးဖြတ်မှု»; upapattibhava «ပဋိသန္ဓေ ဘဝ» (pi-1 upapatti- in rūpūpapattiyā is
  «ဖြစ်ပေါ်ရန်»; flag); kammabhava «ကံ ဘဝ»; vokāra = «အစုအဝေး» (count with ပါး, pi-1 count_my).
- cuti «စုတေခြင်း» (pi-1 uses သေခြင်း for cuti in cutūpapāta, but maraṇaṃ = သေခြင်း is in the same list here).
- Lemma «X»ti = «“X”ဟူရာ၌» (+ «။» where the Pāli has a full stop); «tena vuccati "X"ti» = «ထို့ကြောင့် “X”ဟု ဆိုသည်».
- vācā palāpo taken as one item («စကား ပေါက်ကရ ပြောခြင်း»), vippalāpo «အမျိုးမျိုး ပေါက်ကရ ပြောခြင်း».
- Headings: -catukka «လေးမျိုးတွဲ» (as pi-1 duka / tika), niddesa «အကျယ် ဖော်ပြချက်» (pi-1), -mūlaka «ကို အခြေခံသော»
  (sample). Paccaya- «အကြောင်း», Hetu- «အကြောင်းပြုခြင်း», Sampayutta- «ယှဉ်တွဲခြင်း», Aññamañña- «အချင်းချင်း
  အကြောင်းဖြစ်ခြင်း».
- Spelling twins of pi-1 items given the pi-1 Burmese: samphusanā / saṃphusanā, nandirāgo / nandīrāgo, dvidhāpatho /
  dvedhāpatho, apariyogāhaṇā / apariyogāhanā, chambhitattaṃ / thambhitattaṃ (cittassa), sañcetayitattaṃ / pi-1
  cetayitattaṃ («စေ့ဆော်ထားသော အဖြစ်»).
- «Cattāro mahābhūtā, catunnañca …» (first «ca» missing) = the pi-1 «Cattāro ca mahābhūtā, …» Burmese.
- Own check: «neva kusalā nākusalā» counted as one negation (= the abyākata phrase, as the sample counts it);
  the sample's ignore-pattern «မဆို» narrowed to «မဆို(?!း)» (else «စိတ်မဆိုး» was skipped).

## Unsure Pāli
- okkanti «သက်ဆင်းခြင်း» (descent), sokasallaṃ «စိုးရိမ်ခြင်းဟူသော ငြောင့်», cetaso parijjhāyanā «စိတ်၏
  လောင်မြိုက်ခြင်း», maccu «သေမင်း», rogabyasana «ကျန်းမာရေး ပျက်စီးခြင်း», samannāgatassa «ကြုံတွေ့နေရသူ၏»,
  tadadhimuttatā «ထိုအာရုံ၌ ဆုံးဖြတ်ထားသော အဖြစ်», «Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati» = «မနော
  သိစိတ် ဓာတ်သည် မှီ၍ ဖြစ်ပေါ်ရာ ရုပ် ရှိသမျှ». The Suttanta jāti / jarā / maraṇa / soka … lists recur in ch. 4
  (Saccavibhaṅga, another agent): align in the consistency pass.

## Source slips (translated as written)
- ^2-238: «ayaṃ vuccati paridevo"» (opening quote missing): «ဤသည်ကို ငိုကြွေးခြင်း”ဟု ခေါ်သည်».
- ^2-245 (4th chain): «taṇhāpaccayā upādānaṃ upādānasampayuttaṃ» (for taṇhāsampayuttaṃ): «… စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော
  စွဲလမ်းမှု …».
- ^2-257: «samudayo hoti"ti» (hoti for hotī): same Burmese.
- ^2-262: «saṅkhārahetukaṃ viññāṇapaccayā» (comma missing): no «၊» there.
- ^2-259, ^2-273, ^2-279, ^2-281, ^2-283, ^2-327, ^2-354: «vuccati X» without quotes: no quotes in the Burmese.
- ^2-273: «abhinibbati» read as abhinibbatti.
- ^2-277: «akusamūlaṃ» read as akusalamūlaṃ; «"avijjāpaccayā saṅkhāro.» (closing quote missing): kept so.
- ^2-296: «ayaṃ vuccati – "…"» (dash): «ဤသည်ကို – “…”ဟု ခေါ်သည်» (dash rule).
- ^2-354: «Tena vuccati evametassa … hotī"ti» (opening quote missing): kept so.
- ^2-340 «kāmehi …pe…», ^2-265 / ^2-269 «… …pe…», «mānasaṃ …pe…»: stray spaces dropped.
- ^2-323 (Tasseva lokuttara … dandhābhiññaṃ) without «suññataṃ», ^2-349 with it: pi-1 Burmese with / without
  «၊ ဆိတ်သုဉ်းသော».
