# pi-5 Burmese zero-shot, chapters 13-16: notes (13-pancamavaggo, 14-chatthavaggo, 15-sattamavaggo, 16-atthamavaggo)

Status: DONE 2026-11-20 (not committed). Brief: burmese-zeroshot-brief.md. Source rule kept: translated from the Pāli only;
no Burmese translation / nissaya opened, 0-INBOX/temp/language-priority/ not opened, no web search. English pi-5
zero-shot (13, 14 first lines) read for meaning only. pi-1 … pi-4 read only through their FINAL rails texts (kwic5.py /
my5_formulas.FINAL); every reused value is witnessed (W) at import or checked by check_ch13-16.py C3.

## Files and run
- Output (AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/): 13-pancamavaggo.md (47 segments, 93
  lines: kathās 43-52 + uddāna + Mahāpaṇṇāsaka uddāna), 14-chatthavaggo.md (46 segments, 95 lines: kathās 53-62),
  15-sattamavaggo.md (52 segments, 154 lines: kathās 63-72), 16-atthamavaggo.md (66 segments, 160 lines: kathās 73-83).
- make_ch13-16.py: imports make_ch11-12.py READ ONLY (which imports make_ch6-10 / make_sample / my5_formulas);
  extends PROP / SENT / LINES / QUOTE / HEAD / COLO / ANCHOR / VAR_KIND / REF / BR_TABLE in memory only.
  P() never overwrites an imported key and KEEPS the imported Burmese wherever an imported table or rule already
  translates a key (28 keys, e.g. the bare nouns vedanā / saññā / the āyatana names / «so ca pañcavokārabhavo…»):
  identical Pāli = identical Burmese with ch1-12. Scratch options --q REGEX, --try LINE, --units, --skipped.
  Run: python3 -I -X utf8 make_ch13-16.py [chapter] [--misses]; check_ch13-16.py [chapter] [--why].
- New frames (before the generic ones): «Hañci P, no vata re vattabbe – "Q"ti» (^5-429, «ca» missing = the «no ca»
  consequence); «Tena hi P-ti…pe….» (^5-443); «Hañci P, tena vata re vattabbe "Q"ti» without dash (^5-456, no dash
  added); «X-ti katvā P-ti?» (^5-476, ^5-509; no «–» inside); «Na vattabbaṃ P-ti?» without dash and quotes (^5-509:
  «Pဟု ဤသို့ မဆိုသင့်သလော», nothing added). New rules: the feeling / association adjective chains of kathā 69-70
  (_r_adj: «… ဖြစ်စေတတ်သော၊ … နှင့် ယှဉ်တွဲသော၊ … အာရုံ ရှိသော အရာ», each «na» = one «မ…»); «(a)kusalena cittena
  samuṭṭhitaṃ S P1 P2 …» of kathā 81 (_r_81). WH clause («katama…» questions end «…သနည်း»).
- One post-pass in make_ch13-16.run() (these four chapters only): a verse line whose Pāli opens with «"» opens with
  «“» (^5-514 has the same verse line twice, once opening the stanza; the engine looks lines up without quotes).

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all four (check_marks = pi-4-mr/check_marks.py). My chk-pe
  copies (pi-6-mr/chk-pe/13-… 16-…) deleted; the other files there are not mine and were left alone.
- check_ch13-16.py: A 4/4 rebuilt identical + A2 the 8 imported chapters (1, 6-12) still rebuild byte-identical with the
  ch13-16 tables installed; B1 502 lines; B2 1592 polarity marks; B2d 1421 negations; B7 781 existence marks; B3 160
  number words; B4 211 segments; B5 4602/4602 recurring sentences (also against the sample and ch6-12); B6 185 table
  values; 0 mismatches. Reuse test 1152 / 1152 (C1 322/322, C3 822/822 occurrences of 108 terms incl. 25 new witnessed
  terms of these chapters, D 8/8 ch2-5 copies).
- Checker adaptations (documented in the script): «no vata re» counted as negative; «āmantā» in small letters (^5-504)
  and «Na hevaṃ vattabba» (^5-443) counted as the answers; «upaladdh» (uddāna) as upalabbhati; «ထိတွေ့ရ» (pi-1
  phoṭṭhabba list) not counted as «တွေ့ရ»; «vā no» (= us, ^5-491) and «nete» (= na ete) handled; PRIV / EXEMPT extended
  with the privatives of these chapters; C3 skips headings / colophons (B6 checks them); C1 skips rūpadhātu in ch16
  (the realm, pi-2 ^2-916 «သိမ်မွေ့သော ရုပ်ဘုံ», not the element «အဆင်းအရောင် ဓာတ်») and «cakkhunā taṃ rūpaṃ».
- Mutation test: a dropped «မ», a changed digit and «နှစ်» -> «သုံး» are all caught (A, B1, B2d, B7, B3, B5); the file
  was regenerated afterwards.

## Main choices (pi-1 … pi-4 FINAL wording reused, witnessed)
- sekha / asekha pi-1 ^1-M1-11 «ကျင့်ကြံဆဲသူ» / «ကျင့်ကြံမှု ပြီးဆုံးသူ»; niyata / aniyata pi-1 «ကျိန်းသေ» (person
  «(မ)ကျိန်းသေသူ»); niyāma pi-4 ^4-13 «သေချာသော လမ်းကြောင်း»; sammattaniyāma «မှန်ကန်မှု၌ သေချာသော လမ်းကြောင်း»;
  paṭisambhidā pi-2 ^2-718; sammutiñāṇa, cetopariyañāṇa (= pariye ñāṇaṃ) and the sixteen mind states pi-2 ^2-796;
  paccavekkhaṇañāṇa pi-2 ^2-804; kasiṇa / samāpatti ch6-10 ATT; «X-e ñāṇaṃ» = «Xကို သိသော ဉာဏ်» (pi-1 ^1-1063).
- Dependent origination pi-1 «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ», the chain pi-2 ^2-225 («Xကြောင့် Y ဖြစ်ပေါ်»; the
  soka … list), idappaccayatā pi-1; the truths pi-2 ^2-982 / ^2-189; kāmataṇhā … pi-2 ^2-916; the asaṅkhata / tāṇa …
  amata words ch6-10; kāmabhava / rūpabhava / arūpabhava, catu- / pañcavokāra pi-2 ^2-234; kāma- / rūpa- / arūpadhātu
  as realms pi-2 ^2-916; kāyakamma / vacīkamma / manokamma pi-1 ^1-985; cetasika pi-1 ^1-M2-57; rūpino / arūpino
  «ရုပ် ဖြစ်သော / ရုပ် မဟုတ်သော» (pi-1 ^1-19, M-dyad); the āyu … pālanā list pi-1 ^1-19; the gandha / rasa / phoṭṭhabba
  lists pi-1; saṅgahita pi-3 ^3-7 «အကျုံးဝင်»; samphassajā saññā pi-2; the precepts' words pi-2 ^2-703 / pi-1.
- From ch6-12 (imported): dāna «ပေးလှူခြင်း» (the debate's subject, ch6-10), the iṭṭhaphala … sukhavipāka list (sample),
  «tassa tasseva …», «esese ekaṭṭhe …» (sample), sukhā / adukkhamasukhā vedanā, the ch10 senses (ghāyati / sāyati «ခံ»),
  existence-list words (ch11 TOK), the upapattesiya citta, «ekadesaṃ» «တစ်စိတ်တစ်ဒေသ», asaññasatta, PT4 person types.

## New recurring terms and phrases (Pāli = Burmese; the NEW table of make_ch13-16.py)
- X-phalasamaṅgī puggalo = Xဖိုလ်ကို ရရှိထားသော ပုဂ္ဂိုလ်
- Pañcamavaggo = ပဉ္စမ ဝဂ်
- (43) 1. Vimuttikathā = (43) 1. လွတ်မြောက်ခြင်းအကြောင်း ဆွေးနွေးချက်
- vimuttiñāṇaṃ = လွတ်မြောက်ခြင်းကို သိသော ဉာဏ်
- attained … (pattassa paṭiladdhassa adhigatassa sacchikatassa) = သို့ ရောက်ပြီး၊ ရပြီး၊ ပြည့်မီပြီး၊ မျက်မှောက်ပြုပြီးသူ
- asekhaṃ ñāṇaṃ = ကျင့်ကြံမှု ပြီးဆုံးသူ၏ ဉာဏ်
- (44) 2. Asekhañāṇakathā = (44) 2. ကျင့်ကြံမှု ပြီးဆုံးသူ၏ ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- Asekhañāṇakathā = ကျင့်ကြံမှု ပြီးဆုံးသူ၏ ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- diṭṭhaṃ viditaṃ sacchikataṃ upasampajja viharati = မြင်ပြီး၊ သိပြီး၊ မျက်မှောက်ပြုပြီးသော ထိုတရားကို ပြည့်စုံစေလျက် နေ
- uḷāro = မြင့်မြတ်သူ ဖြစ်သည်
- viparīte ñāṇaṃ = ဖောက်ပြန်သော ဉာဏ်
- vipariyeso = ဖောက်ပြန်ခြင်း
- (45) 3. Viparītakathā = (45) 3. ဖောက်ပြန်သော အရာအကြောင်း ဆွေးနွေးချက်
- Viparītakathā = ဖောက်ပြန်သော အရာအကြောင်း ဆွေးနွေးချက်
- anicce niccanti … asubhe subhanti vipariyeso = မမြဲသော အရာ၌ မြဲသည်ဟု / ဆင်းရဲသော အရာ၌ ချမ်းသာသည်ဟု / အတ္တ မဟုတ်သော အရာ၌ အတ္တဟု / မတင့်တယ်သော အရာ၌ တင့်တယ်သည်ဟု ဖောက်ပြန်ခြင်း
- saññāvipariyeso cittavipariyeso diṭṭhivipariyeso = မှတ်သိမှု ဖောက်ပြန်ခြင်း၊ စိတ် ဖောက်ပြန်ခြင်း၊ အယူ ဖောက်ပြန်ခြင်း
- (46) 4. Niyāmakathā = (46) 4. သေချာသော လမ်းကြောင်းအကြောင်း ဆွေးနွေးချက်
- Niyāmakathā = သေချာသော လမ်းကြောင်းအကြောင်း ဆွေးနွေးချက်
- niyāmagamanāya / aniyāmagamanāya = သေချာသော လမ်းကြောင်းသို့ ရောက်ခြင်းအတွက် / သေချာသော လမ်းကြောင်း မဟုတ်ရာသို့ ရောက်ခြင်းအတွက်
- niyato / aniyato (person) = ကျိန်းသေသူ / မကျိန်းသေသူ
- sammattaniyāmo = မှန်ကန်မှု၌ သေချာသော လမ်းကြောင်း
- (47) 5. Paṭisambhidākathā = (47) 5. ပိုင်းခြားသိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- Paṭisambhidākathā = ပိုင်းခြားသိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- cetopariyāye ñāṇaṃ = စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်
- paṭisambhidāpatto = ပိုင်းခြားသိသော ဉာဏ်သို့ ရောက်ပြီးသူ
- X dadantassa = Xကို ပေးလှူနေသူ၌
- (48) 6. Sammutiñāṇakathā = (48) 6. သမုတ်ကို သိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- Sammutiñāṇakathā = သမုတ်ကို သိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- X-ārammaṇaññeva na aññārammaṇaṃ = Xကိုသာ အာရုံပြု၏၊ အခြားကို အာရုံ မပြု
- sammutisaccaṃ = သမုတ် သစ္စာ
- (49) 7. Cittārammaṇakathā = (49) 7. စိတ်ကို အာရုံပြုခြင်းအကြောင်း ဆွေးနွေးချက်
- Cittārammaṇakathā = စိတ်ကို အာရုံပြုခြင်းအကြောင်း ဆွေးနွေးချက်
- anāgate ñāṇaṃ = အနာဂတ်ကို သိသော ဉာဏ်
- (50) 8. Anāgatañāṇakathā = (50) 8. အနာဂတ်ကို သိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- Anāgatañāṇakathā = အနာဂတ်ကို သိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- mūlato … samudayato jānāti = မူလအားဖြင့်၊ အမြစ်အားဖြင့်၊ အစအားဖြင့်၊ ဖြစ်ပေါ်ရာအားဖြင့်၊ ပေါ်ပေါက်ရာအားဖြင့်၊ ထကြွရာအားဖြင့်၊ အာဟာရအားဖြင့်၊ အာရုံအားဖြင့်၊ အကြောင်းအားဖြင့်၊ ဖြစ်ပေါ်ခြင်းအားဖြင့် သိ
- hetupaccayatā … samanantarapaccayatā = အမြစ် အကြောင်း ဖြစ်ခြင်း / အာရုံ အကြောင်း ဖြစ်ခြင်း / အကြီးအမှူး အကြောင်း ဖြစ်ခြင်း / ကြားမလပ် အကြောင်း ဖြစ်ခြင်း / ကောင်းစွာ ကြားမလပ် အကြောင်း ဖြစ်ခြင်း
- paṭuppanne ñāṇaṃ = ပစ္စုပ္ပန်ကို သိသော ဉာဏ်
- (51) 9. Paṭuppannakathā = (51) 9. ပစ္စုပ္ပန်အကြောင်း ဆွေးနွေးချက်
- tena X-ena taṃ X-aṃ … (the self-reference list) = ထိုXဖြင့် ထိုXကို …
- phale ñāṇaṃ = ဖိုလ်ကို သိသော ဉာဏ်
- (52) 10. Phalañāṇakathā = (52) 10. ဖိုလ်ကို သိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- Phalañāṇakathā = ဖိုလ်ကို သိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- X-paropariyatti = Xတို့ မြင့်မြတ်ခြင်း နိမ့်ကျခြင်းကို သိခြင်း
- Mahāpaṇṇāsako = ကြီးမားသော ငါးဆယ်အစု
- Chaṭṭhavaggo = ဆဋ္ဌမ ဝဂ်
- nibbānaṃ tāṇaṃ leṇaṃ saraṇaṃ parāyanaṃ accutaṃ amataṃ = နိဗ္ဗာန်၊ ကာကွယ်ရာ၊ ပုန်းအောင်းရာ၊ ကိုးကွယ်ရာ၊ မှီခိုရာ၊ မစုတေသော အရာ၊ အမြိုက်
- sotāpattiniyāmo … arahattaniyāmo = သောတာပတ္တိ သေချာသော လမ်းကြောင်း … ရဟန္တာ သေချာသော လမ်းကြောင်း
- micchattaniyāmo = မှားယွင်းမှု၌ သေချာသော လမ်းကြောင်း
- okkamanti paṭilabhanti … sañjanenti = သက်ဆင်းကြ၊ ရရှိကြ၊ ဖြစ်ပေါ်စေကြ၊ ကောင်းစွာ ဖြစ်ပေါ်စေကြ၊ ထစေကြ၊ ကောင်းစွာ ထစေကြ၊ ဖြစ်စေကြ၊ ထူးကဲစွာ ဖြစ်စေကြ၊ မွေးဖွားစေကြ၊ ကောင်းစွာ မွေးဖွားစေကြ
- (53) 1. Niyāmakathā = (53) 1. သေချာသော လမ်းကြောင်းအကြောင်း ဆွေးနွေးချက်
- (54) 2. Paṭiccasamuppādakathā = (54) 2. အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံအကြောင်း ဆွေးနွေးချက်
- Paṭiccasamuppādakathā = အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံအကြောင်း ဆွေးနွေးချက်
- dhammaṭṭhitatā dhammaniyāmatā = တရား၏ တည်ရှိခြင်း၊ တရား၏ သေချာခြင်း
- tathatā avitathatā anaññathatā = ဟုတ်မှန်ခြင်း၊ မဖောက်ပြန်ခြင်း၊ အခြား မဟုတ်ခြင်း
- (55) 3. Saccakathā = (55) 3. သစ္စာအကြောင်း ဆွေးနွေးချက်
- Saccakathā = သစ္စာအကြောင်း ဆွေးနွေးချက်
- tatha / avitatha / anaññatha = ဟုတ်မှန် / မဖောက်ပြန် / အခြား မဟုတ်
- cattāro āruppā = ရုပ်မရှိသော ဘုံ လေးပါး
- (56) 4. Āruppakathā = (56) 4. ရုပ်မရှိသော ဘုံအကြောင်း ဆွေးနွေးချက်
- Āruppakathā = ရုပ်မရှိသော ဘုံအကြောင်း ဆွေးနွေးချက်
- viññāṇaṭṭhiti = သိစိတ် တည်ရာ
- aneja (of the āruppa) = မတုန်လှုပ်သော အရာ
- (57) 5. Nirodhasamāpattikathā = (57) 5. ချုပ်ငြိမ်းခြင်း သမာပတ်အကြောင်း ဆွေးနွေးချက်
- Nirodhasamāpattikathā = ချုပ်ငြိမ်းခြင်း သမာပတ်အကြောင်း ဆွေးနွေးချက်
- nirodhasamāpatti = ချုပ်ငြိမ်းခြင်း သမာပတ်
- vivekaninnaṃ … vivekapabbhāraṃ = ကင်းဆိတ်ခြင်းသို့ ညွတ်သော၊ … ကိုင်းသော၊ … ရှိုင်းသော
- (58) 6. Ākāsakathā = (58) 6. ဟင်းလင်းပြင်အကြောင်း ဆွေးနွေးချက်
- Ākāsakathā = ဟင်းလင်းပြင်အကြောင်း ဆွေးနွေးချက်
- (59) 7. Ākāso sanidassanotikathā = (59) 7. ဟင်းလင်းပြင်သည် မြင်နိုင်သော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Ākāso sanidassanotikathā = ဟင်းလင်းပြင်သည် မြင်နိုင်သော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- (60) 8. Pathavīdhātu sanidassanātiādikathā = (60) 8. မြေဓာတ်သည် မြင်နိုင်သော အရာ ဖြစ်သည် စသည်ဟူသော ဆွေးနွေးချက်
- Pathavīdhātu sanidassanātiādikathā = မြေဓာတ်သည် မြင်နိုင်သော အရာ ဖြစ်သည် စသည်ဟူသော ဆွေးနွေးချက်
- (61) 9. Cakkhundriyaṃ sanidassanantiādikathā = (61) 9. မျက်စိ၏ စွမ်းရည်သည် မြင်နိုင်သော အရာ ဖြစ်သည် စသည်ဟူသော ဆွေးနွေးချက်
- Cakkhundriyaṃ sanidassanantiādikathā = မျက်စိ၏ စွမ်းရည်သည် မြင်နိုင်သော အရာ ဖြစ်သည် စသည်ဟူသော ဆွေးနွေးချက်
- (62) 10. Kāyakammaṃ sanidassanantikathā = (62) 10. ကိုယ်ဖြင့် ပြုသော ကံသည် မြင်နိုင်သော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Kāyakammaṃ sanidassanantikathā = ကိုယ်ဖြင့် ပြုသော ကံသည် မြင်နိုင်သော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Sattamavaggo = သတ္တမ ဝဂ်
- (63) 1. Saṅgahitakathā = (63) 1. အကျုံးဝင်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Saṅgahitakathā = အကျုံးဝင်ခြင်းအကြောင်း ဆွေးနွေးချက်
- saṅgahita (the simile, tied together) = စုစည်းထား
- (64) 2. Sampayuttakathā = (64) 2. ယှဉ်တွဲခြင်းအကြောင်း ဆွေးနွေးချက်
- Sampayuttakathā = ယှဉ်တွဲခြင်းအကြောင်း ဆွေးနွေးချက်
- sahagatā … ekārammaṇā (with X) = Xနှင့်အတူ ဖြစ်ကြ၊ Xနှင့်အတူ ပေါ်ပေါက်ကြ၊ Xနှင့် ရောနှောကြ၊ Xနှင့် ယှဉ်တွဲကြ၊ Xနှင့် တစ်ပြိုင်နက် ဖြစ်ပေါ်ကြ၊ Xနှင့် တစ်ပြိုင်နက် ချုပ်ငြိမ်းကြ၊ Xနှင့် မှီရာ တူကြ၊ Xနှင့် အာရုံ တူကြ
- (65) 3. Cetasikakathā = (65) 3. စိတ်၏ အဖော် ဖြစ်သော သဘောတရားအကြောင်း ဆွေးနွေးချက်
- Cetasikakathā = စိတ်၏ အဖော် ဖြစ်သော သဘောတရားအကြောင်း ဆွေးနွေးချက်
- (66) 4. Dānakathā = (66) 4. ပေးလှူခြင်းအကြောင်း ဆွေးနွေးချက်
- Dānakathā = ပေးလှူခြင်းအကြောင်း ဆွေးနွေးချက်
- deyyadhammo = ပေးလှူဖွယ် ဝတ္ထု
- dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā = ပေးလှူခြင်းကို လိုလားဖွယ် အသီးအပွင့် ရှိသော အရာဟု မြတ်စွာဘုရား ဟောတော်မူ၏
- puññaṃ = ကောင်းမှု
- paribhogamayaṃ puññaṃ = သုံးဆောင်ခြင်းမှ ဖြစ်သော ကောင်းမှု
- (67) 5. Paribhogamayapuññakathā = (67) 5. သုံးဆောင်ခြင်းမှ ဖြစ်သော ကောင်းမှုအကြောင်း ဆွေးနွေးချက်
- Paribhogamayapuññakathā = သုံးဆောင်ခြင်းမှ ဖြစ်သော ကောင်းမှုအကြောင်း ဆွေးနွေးချက်
- āvaṭṭentassa … paṇidahantassa hoti = စိတ်ကို လှည့်ဆောင်သူ၌၊ စိတ်ညွတ်သူ၌၊ စိတ်ကို ဆောင်သူ၌၊ နှလုံးသွင်းသူ၌၊ စေ့ဆော်သူ၌၊ တောင့်တသူ၌၊ ဆုတောင်းသူ၌ ဖြစ်
- kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā = ကုသိုလ် အကုသိုလ်၊ အပြစ် ရှိသော အပြစ် ကင်းသော၊ ယုတ်ညံ့သော မြင့်မြတ်သော၊ မည်းသော ဖြူသော ဆန့်ကျင်ဘက် ရှိသော
- ito dinnena tattha yāpenti = ဤလောကမှ ပေးလှူသော အရာဖြင့် ထိုလောက၌ အသက်မွေးကြ
- (68) 6. Itodinnakathā = (68) 6. ဤလောကမှ ပေးလှူသော အရာအကြောင်း ဆွေးနွေးချက်
- Ito dinnakathā = ဤလောကမှ ပေးလှူသော အရာအကြောင်း ဆွေးနွေးချက်
- kammavipāko = ကံ၏ အကျိုး
- (69) 7. Pathavī kammavipākotikathā = (69) 7. မြေသည် ကံ၏ အကျိုး ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Pathavī kammavipākotikathā = မြေသည် ကံ၏ အကျိုး ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- (70) 8. Jarāmaraṇaṃ vipākotikathā = (70) 8. အိုခြင်း၊ သေခြင်းသည် ကံ၏ အကျိုး ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Jarāmaraṇaṃ vipākotikathā = အိုခြင်း၊ သေခြင်းသည် ကံ၏ အကျိုး ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi = စိတ်ကို လှည့်ဆောင်ခြင်း၊ စိတ်ညွတ်ခြင်း၊ စိတ်ကို ဆောင်ခြင်း၊ နှလုံးသွင်းခြင်း၊ စေ့ဆော်မှု၊ တောင့်တခြင်း၊ ဆုတောင်းခြင်း
- ariyadhammavipāko = အရိယာ တရား၏ အကျိုး
- (71) 9. Ariyadhammavipākakathā = (71) 9. အရိယာ တရား၏ အကျိုးအကြောင်း ဆွေးနွေးချက်
- Ariyadhammavipākakathā = အရိယာ တရား၏ အကျိုးအကြောင်း ဆွေးနွေးချက်
- (72) 10. Vipāko vipākadhammadhammotikathā = (72) 10. ကံ၏ အကျိုးသည် အကျိုး ပေးတတ်သော သဘောတရား ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Vipāko vipākadhammadhammotikathā = ကံ၏ အကျိုးသည် အကျိုး ပေးတတ်သော သဘောတရား ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- arūpino (khandhā / dhammā) = ရုပ် မဟုတ်သော
- Aṭṭhamavaggo = အဋ္ဌမ ဝဂ်
- (73) 1. Chagatikathā = (73) 1. လားရာ ခြောက်ပါးအကြောင်း ဆွေးနွေးချက်
- Chagatikathā = လားရာ ခြောက်ပါးအကြောင်း ဆွေးနွေးချက်
- nirayo, tiracchānayoni, pettivisayo, manussā, devā = ငရဲ၊ တိရစ္ဆာန် မွေးဖွားရာ၊ ပြိတ္တာ နယ်ပယ်၊ လူတို့၊ နတ်တို့
- antarābhavo = ကြားဘဝ
- kāmadhātu / rūpadhātu / arūpadhātu (realms) = ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ (pi-2 ^2-916)
- (74) 2. Antarābhavakathā = (74) 2. ကြားဘဝအကြောင်း ဆွေးနွေးချက်
- Antarābhavakathā = ကြားဘဝအကြောင်း ဆွေးနွေးချက်
- ānantariyo puggalo = အနန္တရိယ ကံကို ပြုသော ပုဂ္ဂိုလ်
- upahaccabhavo / sasaṅkhārabhavo = သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ ဖြစ်သော ဘဝ / တိုက်တွန်းမှုဖြင့် ဖြစ်သော ဘဝ
- (75) 3. Kāmaguṇakathā = (75) 3. ကာမဂုဏ်အကြောင်း ဆွေးနွေးချက်
- Kāmaguṇakathā = ကာမဂုဏ်အကြောင်း ဆွေးနွေးချက်
- (76) 4. Kāmakathā = (76) 4. ကာမအကြောင်း ဆွေးနွေးချက်
- Kāmakathā = ကာမအကြောင်း ဆွေးနွေးချက်
- tappaṭisaññutto / tappaṭisaṃyutto = ထိုအရာနှင့် စပ်ယှဉ်သော
- (77) 5. Rūpadhātukathā = (77) 5. သိမ်မွေ့သော ရုပ်ဘုံအကြောင်း ဆွေးနွေးချက်
- Rūpadhātukathā = သိမ်မွေ့သော ရုပ်ဘုံအကြောင်း ဆွေးနွေးချက်
- (78) 6. Arūpadhātukathā = (78) 6. ရုပ်မရှိသော ဘုံအကြောင်း ဆွေးနွေးချက်
- Arūpadhātukathā = ရုပ်မရှိသော ဘုံအကြောင်း ဆွေးနွေးချက်
- (79) 7. Rūpadhātuyāāyatanakathā = (79) 7. သိမ်မွေ့သော ရုပ်ဘုံ၌ အာရုံခံ နယ်ပယ်အကြောင်း ဆွေးနွေးချက်
- Rūpadhātuyā āyatanakathā = သိမ်မွေ့သော ရုပ်ဘုံ၌ အာရုံခံ နယ်ပယ်အကြောင်း ဆွေးနွေးချက်
- saḷāyataniko attabhāvo = အာရုံခံ နယ်ပယ် ခြောက်ပါး ရှိသော ကိုယ်ခန္ဓာ ရရှိခြင်း
- tena cakkhunā taṃ rūpaṃ passati … (the five) = ထိုမျက်စိဖြင့် ထိုအဆင်းအရောင်ကို မြင် … (ခံ / ခံ / ထိ / သိ; ch6-10 SENSE)
- (80) 8. Arūpe rūpakathā = (80) 8. ရုပ်မရှိသော ဘုံ၌ ရုပ်အကြောင်း ဆွေးနွေးချက်
- Arūpe rūpakathā = ရုပ်မရှိသော ဘုံ၌ ရုပ်အကြောင်း ဆွေးနွေးချက်
- (81) 9. Rūpaṃ kammantikathā = (81) 9. ရုပ်သည် ကံ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Rūpaṃ kammantikathā = ရုပ်သည် ကံ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- kusalena cittena samuṭṭhitaṃ X = ကုသိုလ် စိတ်ကြောင့် ဖြစ်ပေါ်သော X
- rūpajīvitindriyaṃ / arūpajīvitindriyaṃ = ရုပ် အသက်၏ စွမ်းရည်
- arūpajīvitindriyaṃ = ရုပ် မဟုတ်သော အသက်၏ စွမ်းရည်
- (82) 10. Jīvitindriyakathā = (82) 10. အသက်၏ စွမ်းရည်အကြောင်း ဆွေးနွေးချက်
- Jīvitindriyakathā = အသက်၏ စွမ်းရည်အကြောင်း ဆွေးနွေးချက်
- (83) 11. Kammahetukathā = (83) 11. ကံကြောင့်ဟူသော ဆွေးနွေးချက်
- Kammahetukathā = ကံကြောင့်ဟူသော ဆွေးနွေးချက်

## For the consistency pass
- sekha «ကျင့်ကြံဆဲသူ» (pi-1) is the same Burmese as ch10 paṭipannako «ကျင့်ကြံဆဲသူ»: two Pāli words share one Burmese
  (pi-1 binding kept).
- saṅgahita (pi-3) «အကျုံးဝင်» and pariyāpanna (pi-1) «… အကျုံးဝင်» share a verb; in the saṅgaha simile (^5-472)
  saṅgahita = tied together «စုစည်းထား» (other sense); «gaṇanaṃ gacchanti … pariyāpannā» (^5-471) «အကျုံးဝင်ကြ»
  without «ဘဝဘုံတို့၌» (counting, not the realms).
- dāna: the subject of the debate «ပေးလှူခြင်း» (ch6-10); the thing given (dānaṃ deti / dadāti, the sutta's five
  dānāni) «အလှူ».
- vipāka alone = «ကံ၏ အကျိုး» (pi-1); X-ānaṃ dhammānaṃ vipāko «X သဘောတရားတို့၏ အကျိုး»; phala (dānaphala …) «… ၏ အကျိုး».
- rūpabhava in kathā 80 (rūpabhavo rūpagati …) read as the fine-material existence (pi-2 wording, the adjective
  distributed over the list), like kathā 74.
- sotāpatti- … arahatta-niyāmo «သောတာပတ္တိ / သကဒါဂါမိ / အနာဂါမိ / ရဟန္တာ သေချာသော လမ်းကြောင်း»; the elided stage
  names «sakadāgāmi…pe…» take the person names «သကဒါဂါမ်… အနာဂါမ်…».
- ^5-472 sakavādivacana note, ^5-479 note: translated editorial notes.

## Unsure Pāli / interpretation
- X-phalasamaṅgī «Xဖိုလ်ကို ရရှိထားသော ပုဂ္ဂိုလ်»; viparīte ñāṇaṃ «ဖောက်ပြန်သော ဉာဏ်»; vipariyesa «ဖောက်ပြန်ခြင်း»;
  «pathaviṃ pathavito samāpajjati» «မြေကို မြေအဖြစ် ဝင်စား»; niyāmagamanāya «… သို့ ရောက်ခြင်းအတွက်».
- sammutisacca «သမုတ် သစ္စာ» (sammuti pi-2 «သမုတ်»); «saccārammaṇaññeva na aññārammaṇaṃ» «သစ္စာကိုသာ အာရုံပြု၏၊
  အခြားကို အာရုံ မပြု».
- The anāgata list: mūla «မူလ», hetu «အမြစ်» (pi-1 hetu), nidāna «အစ», sambhava / pabhava / samuṭṭhāna «ဖြစ်ပေါ်ရာ /
  ပေါ်ပေါက်ရာ / ထကြွရာ»; the paccaya names «အမြစ် / အာရုံ / အကြီးအမှူး / ကြားမလပ် / ကောင်းစွာ ကြားမလပ် အကြောင်း».
- phalassa kataṃ paññāpeti «ဖိုလ်၏ ပြုလုပ်ချက်ကို သတ်မှတ်ဖော်ပြ»; X-paropariyatti «Xတို့ မြင့်မြတ်ခြင်း နိမ့်ကျခြင်းကို
  သိခြင်း»; aññāṇī «ဉာဏ် မရှိသူ».
- The tool list ^5-441 (kudhārī «ပုဆိန်ငယ်», vāsī «ပေါက်ပြား»); gūtha / mutta «ကျင်ကြီး / ကျင်ငယ်» (a polite word: «မစင်»
  would read as a negative in the checker's «မ» count and is avoided).
- The sutta / verse renderings (^5-450, ^5-454, ^5-477, ^5-480, ^5-485, ^5-486, ^5-490, ^5-491, ^5-493, ^5-510 …
  ^5-514, ^5-539) are plain renderings; kāmūpasaṃhita «ကာမနှင့် စပ်သော», piyarūpa «ချစ်ဖွယ် သဘော ရှိသော»,
  verocana / pabhaṅkara (the sun) «အလင်းရောင် ဖြာထွက်သော နေ / အလင်းကို ပြုသော နေ», upakappati «အထောက်အကူ ဖြစ်».
- antarābhava «ကြားဘဝ»; upahaccabhava / sasaṅkhārabhava (the opponent's nonce words) «သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ ဖြစ်သော
  ဘဝ / တိုက်တွန်းမှုဖြင့် ဖြစ်သော ဘဝ»; ānantariya puggala «အနန္တရိယ ကံကို ပြုသော ပုဂ္ဂိုလ်»; vepacittiparisā
  «ဝေပစိတ္တိ အသုရာ၏ ပရိသတ်တို့»; asurakāya «အသုရာ အပေါင်း».
- «kusalena cittena samuṭṭhitaṃ kāyakammaṃ rūpaṃ» «ကုသိုလ် စိတ်ကြောင့် ဖြစ်ပေါ်သော ကိုယ်ဖြင့် ပြုသော ကံ ဖြစ်သော ရုပ်».
- Mahāpaṇṇāsako «ကြီးမားသော ငါးဆယ်အစု»; the Mahāpaṇṇāsaka uddāna names the first kathās of vaggas 1-5.

## Source slips (translated as written; Pāli not changed)
- ^5-429 «no vata re vattabbe» (without «ca», twice): the «no ca» consequence. ^5-443 «Na hevaṃ vattabba…pe….» (final
  «e» missing): the standard answer. ^5-443 «tena hi … atthīti…pe….»: ends «…».
- ^5-456 «tena vata re vattabbe "cattāro …"ti» without dash: no dash in the Burmese.
- ^5-466 «"āpodhātu sanidassanāti…pe….» (the quote never closes) and «Na vattabbaṃ – tejodhātu sanidassanāti?»
  (no quotes): regular marks in the Burmese (balanced).
- ^5-472 «sā gaddulena saṅgahito» (gender), «balibaddā» / «balībaddā» spelled two ways: one Burmese.
- ^5-473 «vedanākhandhena» (= vedanākkhandhena): the same Burmese.
- ^5-460 «iddhiṃ [sattiṃ (?)] khipanti»: «ဣဒ္ဓိကို … ပစ်ကြ» as written (the variant «sattiṃ», a spear, in the bracket).
- ^5-503 «kālakañcikā [variants] surā» (the next sentence has «asurā»): «ကာလကဉ္စိက နတ်တို့» as written.
- ^5-504 «Nanu atthi asurakāyoti, āmantā.» (one sentence, small «āmantā»): «… မဟုတ်လော၊ ဟုတ်ပါသည်။».
- ^5-509 «Na vattabbaṃ atthi antarābhavoti?» without dash / quotes: none added.
- ^5-511 «paccekasabuddhā» (= paccekasambuddhā): the same Burmese. ^5-523 colophon «Rūpadhātuyā āyatanakathā» vs the
  heading «Rūpadhātuyāāyatanakathā»: one Burmese name. ^5-442 colophon «Paṭuppannañāṇakathā» vs heading
  «Paṭuppannakathā»: rendered as written («ပစ္စုပ္ပန်ကို သိသော ဉာဏ်» / «ပစ္စုပ္ပန်»).
- ^5-470 uddāna «Niyamo» (= niyāmo): «သေချာသော လမ်းကြောင်း». ^5-545 «Āmantā [na hevaṃ vattabbe (syā. kaṃ. pī.)].»:
  the variant answer kept in the bracket.
- ^5-527 «paṇidhīti, no ca vata re» (an inner «ti» in the Hañci clause): same Burmese as without it.
