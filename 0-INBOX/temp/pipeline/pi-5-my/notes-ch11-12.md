# pi-5 Burmese zero-shot, chapters 11-12: notes (11-tatiyavaggo, 12-catutthavaggo)

Status: DONE 2026-11-20 (not committed). Brief: burmese-zeroshot-brief.md. Source rule kept: translated from the Pāli only;
no Burmese translation / nissaya opened, 0-INBOX/temp/language-priority/ not opened, no web search. English pi-5
zero-shot (11-tatiyavaggo, first kathās) read for meaning only. pi-1 … pi-4 read only through their FINAL rails texts
(kwic5.py / my5_formulas.FINAL lookups); every reused value is witnessed (W / F.witness) at import.

## Files and run
- Output: AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/11-tatiyavaggo.md (57 segments, 243 lines:
  Tatiyavaggo, kathās 21-32 + uddāna), 12-catutthavaggo.md (51 segments, 202 lines: Catutthavaggo, kathās 33-42 + uddāna).
- make_ch11-12.py: imports make_ch6-10.py READ ONLY (which installs make_sample.py + my5_formulas.py); extends PROP / SENT /
  LINES / QUOTE / HEAD / COLO / ANCHOR / VAR_KIND / REF / REF_NOTE / BR_TABLE and ch10's GEN / LST / ACTS tables in
  memory only. make_ch2-5.py cannot be imported together with make_ch6-10.py (ch10 then breaks), so the ch2-5
  strings needed here are copied verbatim (check D verifies each one in the ch2-5 output).
  Run: python3 -I -X utf8 make_ch11-12.py [chapter] [--misses] [--units]; check_ch11-12.py [chapter] [--why].
- New frames (inserted before the generic «P-ti?» / «P-ti.»): «…pe… nanu P-ti?» (small letter); «Yaṃ tattha vadesi –
  "vattabbe kho ‘P,’ no ca vattabbe – ‘Q’"ti micchā» WITHOUT the dash after «kho» (^5-379, dash count kept); «Hañci P,
  tena vata re vattabbe – "Q"ti…pe….» (^5-397, ends «…»); «Yathā A, evamevaṃ B?» = «Aသကဲ့သို့ ထို့အတူပင် Bသလော»
  (the seven birth marvels, A with bodhisatta, B the same with cakkavattisatta).
- New rules: «S ariyaṃ (na vattabbaṃ –) X-ārammaṇaṃ(… Y-ārammaṇaṃ)»; the existence lists (saññābhavo saññāgati… / so ca
  …); «"X"ti ca manasi karoti» (the divine-eye thoughts, pi-4 ^4-184 wording); «… manasi karoti, dibbena cakkhunā rūpaṃ
  passati»; «S catūhi/tīhi/dvīhi/chahi phassehi … samannāgato»; «S Mmaggaṃ vītivatto, KILESAS vītivatto(,) tena
  samannāgato». Whole sutta sentences with an inner «ti.» are SENT entries (⟦b⟧ slots for inner variant brackets).

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for both (check_marks = pi-4-mr/check_marks.py). My chk-pe copies
  (pi-6-mr/chk-pe/11-…, 12-…) deleted; the other files in that folder are not mine and were left alone.
- check_ch11-12.py: A 2/2 rebuilt identical + A2 the 6 imported chapters (1, 6-10) still rebuild byte-identical with the
  ch11-12 tables installed; B1 445 lines; B2 1221 polarity marks; B2d 1030 negations (every Pāli negator / privative =
  one negative «မ»); B7 384 existence marks; B3 187 number words; B4 108 segments; B5 3213/3213 recurring sentences
  (also against the sample and ch6-10); B6 98 table values; 0 mismatches.
- Reuse test 1115 / 1115 (C1 45/45, C3 1031/1031 occurrences of 116 terms incl. 50 new witnessed terms of these chapters,
  D 39/39 copies of ch2-5 strings, each attested in the ch2-5 output).
- Mutation test: a «မ» dropped (B2d) and «လေး» changed to «သုံး» (B3) are caught; the file was regenerated afterwards.

## Main choices (pi-1 … pi-4 FINAL wording reused)
- The ten powers: pi-2 ^2-760 objects + «ဟုတ်မှန်သည့်အတိုင်း သိသော ဉာဏ်» (^2-809); tathāgatabala «ဘုရားဆိုင်ရာ စွမ်းအား»;
  tathāgato «မြတ်စွာဘုရား» (pi-2); sāvaka «တပည့်» (pi-2 ariyasāvako).
- sarāga / sadosa / samoha / vītarāga citta pi-2 ^2-796; sahabhu / anuparivatti / saṃsaṭṭha / sampayutta and the Mātikā
  adjectives pi-1 dyads; kāmāvacara … apariyāpanna pi-1; upādiṇṇa «ကံကြောင့် ဖြစ်» (pi-1 ^1-M1-4).
- The two sutta passages «so evaṃ samāhite citte … abhininnāmeti» and «tassa evaṃ jānato … vimuccati» are read from
  pi-4 ^4-185; the divine-eye thoughts from ^4-184; persons assaddho / kusīto / muṭṭhassatī / asamāhito / duppañño
  from pi-2 ^2-851; the five precepts and surāmeraya… from pi-2 ^2-703 / pi-4 ^4-132; Gotrabhū pi-4; asaññasatta
  «အသညသတ်» (pi-2); the arūpa bases pi-1; ekavokāra … pañcavokāra pi-2 ^2-234; the four truths «… အရိယာ သစ္စာ»
  pi-2 ^2-189; okkantaniyāma from pi-4 ^4-13 «သေချာသော လမ်းကြောင်းသို့ သက်ဆင်း»; ananussutesu pi-4 ^4-M-12.
- From ch6-10 (imported): catubhāga frame reused with «တစ်စိတ်တစ်ဒေသ» for ekadesaṃ (^5-366, asserted identical to ch10
  apart from the word); arahant epithets, path groups, kilesa nouns, methuna act list, ratana names, cakkavatti.

## New recurring terms and phrases (Pāli = Burmese; the NEW table of make_ch11-12.py)
- sāvakabalaṃ = တပည့်၏ စွမ်းအား
- sāvakasādhāraṇa / sāvakaasādhāraṇa = တပည့်တို့နှင့် ဆက်ဆံ / တပည့်တို့နှင့် မဆက်ဆံ
- ariya (noble, of a knowledge) = အရိယာ အရာ
- Tatiyavaggo = တတိယ ဝဂ်
- (21) 1. Balakathā = (21) 1. စွမ်းအားအကြောင်း ဆွေးနွေးချက်
- Balakathā = စွမ်းအားအကြောင်း ဆွေးနွေးချက်
- X yathābhūtaṃ ñāṇaṃ tathāgatabalaṃ = Xကို ဟုတ်မှန်သည့်အတိုင်း သိသော ဉာဏ်ဟူသော ဘုရားဆိုင်ရာ စွမ်းအား
- yādisaṃ A tādisaṃ B = Aကဲ့သို့ပင် Bသည် ထိုနည်းတူ ဖြစ်
- pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā = ရှေးကာလ အားထုတ်မှု၊ ရှေးကာလ ကျင့်ကြံမှု၊ တရားကို ပြောကြားခြင်း၊ တရားကို ဟောကြားခြင်း
- jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo = အောင်နိုင်သူ၊ ဆရာ၊ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်၊ အလုံးစုံကို သိသူ၊ အလုံးစုံကို မြင်သူ၊ တရား၏ အရှင်၊ တရား၏ ကိုးကွယ်ရာ
- anuppannassa maggassa uppādetā … maggakovido = မဖြစ်ပေါ်သေးသော မဂ်ကို ဖြစ်ပေါ်စေသူ၊ မပေါ်ပေါက်သေးသော မဂ်ကို ပေါ်ပေါက်စေသူ၊ မဟောကြားရသေးသော မဂ်ကို ဟောကြားသူ၊ မဂ်ကို သိသူ၊ မဂ်ကို နားလည်သူ၊ မဂ်၌ ကျွမ်းကျင်သူ
- Natthi. (answer) = မရှိပါ။
- (22) 2. Ariyantikathā = (22) 2. အရိယာ ဟူသော ဆွေးနွေးချက်
- Ariyantikathā = အရိယာ ဟူသော ဆွေးနွေးချက်
- suññatārammaṇa = ဆိတ်သုဉ်းခြင်းကို အာရုံပြုသော
- animittārammaṇa = အမှတ်အသား မရှိခြင်းကို အာရုံပြုသော
- appaṇihitārammaṇa = တောင့်တမှု မရှိခြင်းကို အာရုံပြုသော
- X na vattabbaṃ – ariyaṃ = Xကို ဤသို့ မဆိုသင့် – “အရိယာ အရာ”ဟု
- X-ñca manasi karoti = Xကိုလည်း နှလုံးသွင်း
- dvinnaṃ phassānaṃ dvinnaṃ cittānaṃ samodhānaṃ hoti = တွေ့ထိမှု နှစ်ပါး၊ စိတ် နှစ်ပါးတို့၏ ပေါင်းဆုံခြင်း
- (23) 3. Vimuttikathā = (23) 3. လွတ်မြောက်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Vimuttikathā = လွတ်မြောက်ခြင်းအကြောင်း ဆွေးနွေးချက်
- sarāgaṃ cittaṃ = ရာဂ ရှိသော စိတ်
- sadosaṃ cittaṃ = ဒေါသ ရှိသော စိတ်
- samohaṃ cittaṃ = မောဟ ရှိသော စိတ်
- saphassaṃ cittaṃ = တွေ့ထိမှု ရှိသော စိတ်
- savedanaṃ cittaṃ = ခံစားမှု ရှိသော စိတ်
- sasaññaṃ cittaṃ = မှတ်သိမှု ရှိသော စိတ်
- sacetanaṃ cittaṃ = စေ့ဆော်မှု ရှိသော စိတ်
- sapaññaṃ cittaṃ = ပညာ ရှိသော စိတ်
- X ca cittañca ubho vimuccanti = Xနှင့် စိတ် နှစ်ပါးစလုံး လွတ်မြောက်ကြ
- X-sahajāta = Xနှင့်အတူ ပေါ်ပေါက်သော
- (24) 4. Vimuccamānakathā = (24) 4. လွတ်မြောက်ဆဲ အရာအကြောင်း ဆွေးနွေးချက်
- Vimuccamānakathā = လွတ်မြောက်ဆဲ အရာအကြောင်း ဆွေးနွေးချက်
- vimuttaṃ vimuccamānaṃ = လွတ်မြောက်ပြီးသော အရာသည် လွတ်မြောက်ဆဲ အရာ ဖြစ်
- bhaṅgakkhaṇo = ပြိုပျက်ခြင်း ခဏ
- (25) 5. Aṭṭhamakakathā = (25) 5. အဋ္ဌမ ပုဂ္ဂိုလ်အကြောင်း ဆွေးနွေးချက်
- Aṭṭhamakakathā = အဋ္ဌမ ပုဂ္ဂိုလ်အကြောင်း ဆွေးနွေးချက်
- aṭṭhamako puggalo (the eighth person) = အဋ္ဌမ ပုဂ္ဂိုလ်
- gotrabhū puggalo = အရိယာ အနွယ်သို့ ပြောင်းသော ပုဂ္ဂိုလ်
- diṭṭhipariyuṭṭhānaṃ = အယူ ထကြွခြင်း
- diṭṭhānusayo / vicikicchānusayo = အယူ ကိန်းအောင်းခြင်း / ယုံမှားမှု ကိန်းအောင်းခြင်း
- amaggena pahīnaṃ lokiyena sāsavena… saṃkilesiyena = မဂ် မဟုတ်သော၊ လောကနှင့် သက်ဆိုင်သော၊ စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော… ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော အရာဖြင့် ပယ်ပြီး
- uppajjissati / nuppajjissati = ဖြစ်ပေါ်လိမ့်မည် / ဖြစ်ပေါ်လိမ့်မည် မဟုတ်
- (26) 6. Aṭṭhamakassaindriyakathā = (26) 6. အဋ္ဌမ ပုဂ္ဂိုလ်၏ စွမ်းရည်အကြောင်း ဆွေးနွေးချက်
- Aṭṭhamakassa indriyakathā = အဋ္ဌမ ပုဂ္ဂိုလ်၏ စွမ်းရည်အကြောင်း ဆွေးနွေးချက်
- assaddho = ယုံကြည်မှု မရှိသူ
- kusīto hīnavīriyo = ပျင်းရိ၍ ဝီရိယ ယုတ်လျော့သူ
- muṭṭhassati asampajāno = သတိ လစ်၍ ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း ကင်းသူ
- asamāhito vibbhantacitto = စိတ် မတည်ကြည်၍ စိတ် ပျံ့လွင့်သူ
- duppañño elamūgo = ပညာ နည်း၍ နုံအ ထုံထိုင်းသူ
- bāhiro puthujjanapakkhe ṭhito = သာသနာပ ပုထုဇဉ် ဘက်၌ တည်သူ
- sā ca saddhā niyyānikā = ထိုယုံကြည်မှုသည်လည်း လွတ်မြောက်ရာသို့ ပို့ဆောင်သော အရာ ဖြစ်
- (27) 7. Dibbacakkhukathā = (27) 7. နတ်မျက်စိအကြောင်း ဆွေးနွေးချက်
- Dibbacakkhukathā = နတ်မျက်စိအကြောင်း ဆွေးနွေးချက်
- (28) 8. Dibbasotakathā = (28) 8. နတ်နားအကြောင်း ဆွေးနွေးချက်
- Dibbasotakathā = နတ်နားအကြောင်း ဆွေးနွေးချက်
- maṃsacakkhu = ပကတိ မျက်စိ
- paññācakkhu = ပညာမျက်စိ
- dibbasota = နတ်နား
- maṃsasota = ပကတိ နား
- dhammupatthaddha = တရား၏ ထောက်ပံ့မှုကို ရသော
- visayo ānubhāvo gocaro = နယ်ပယ်၊ အစွမ်း၊ ကျက်စားရာ
- X hutvā Y hoti = X ဖြစ်ပြီးမှ Y ဖြစ်လာ
- (29) 9. Yathākammūpagatañāṇakathā = (29) 9. ကံအားလျော်စွာ ရောက်သွားခြင်းကို သိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- Yathākammūpagatañāṇakathā = ကံအားလျော်စွာ ရောက်သွားခြင်းကို သိသော ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- yathākammūpagata = ကံအားလျော်စွာ ရောက်သွားခြင်း
- yathākammūpagataṃ ñāṇaṃ = ကံအားလျော်စွာ ရောက်သွားခြင်းကို သိသော ဉာဏ်
- dibbena cakkhunā rūpaṃ passati (after «manasi karoti») = နတ်မျက်စိဖြင့် အဆင်းအရောင်ကို မြင်
- (30) 10. Saṃvarakathā = (30) 10. စောင့်စည်းမှုအကြောင်း ဆွေးနွေးချက်
- Saṃvarakathā = စောင့်စည်းမှုအကြောင်း ဆွေးနွေးချက်
- saṃvaro / asaṃvaro = စောင့်စည်းမှု / မစောင့်စည်းမှု
- asaṃvarā saṃvaro sīlaṃ = မစောင့်စည်းမှုမှ စောင့်စည်းမှုသည် သီလ ဖြစ်
- (31) 11. Asaññakathā = (31) 11. အသညသတ်အကြောင်း ဆွေးနွေးချက်
- Asaññakathā = အသညသတ်အကြောင်း ဆွေးနွေးချက်
- gati = လားရာ
- sattāvāso = သတ္တဝါတို့ နေရာ ဘုံ
- saṃsāro = သံသရာ
- yoni = မွေးဖွားရာ အမျိုးအစား
- attabhāvapaṭilābho = ကိုယ်ခန္ဓာ ရရှိခြင်း
- saññābhavo = မှတ်သိမှု ရှိသော ဘဝ
- asaññabhavo = မှတ်သိမှု မရှိသော ဘဝ
- so ca X (the existence) = ထိုဘဝသည်လည်း X ဖြစ်
- tāya saññāya saññākaraṇīyaṃ karoti = ထိုမှတ်သိမှုဖြင့် မှတ်သိမှု၏ ပြုဖွယ် ကိစ္စကို ပြု
- kiñci kāle = အချို့ အချိန်၌
- cutikāle / upapattikāle / ṭhitikāle = စုတေသည့် အချိန်၌ / ပြန်လည် ဖြစ်ပေါ်သည့် အချိန်၌ / တည်နေသည့် အချိန်၌
- (32) 12. Nevasaññānāsaññāyatanakathā = (32) 12. မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်အကြောင်း ဆွေးနွေးချက်
- Nevasaññānāsaññāyatanakathā = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်အကြောင်း ဆွေးနွေးချက်
- X-e na vattabbaṃ – "saññā atthī"ti = X၌ ဤသို့ မဆိုသင့် – “မှတ်သိမှု ရှိသည်”
- Catutthavaggo = စတုတ္ထ ဝဂ်
- dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti = ဒုက္ခကို ပိုင်းခြား သိသည်၊ ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို ပယ်သည်၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းကို မျက်မှောက်ပြုသည်၊ မဂ်ကို ပွားများ
- apāyagamanīya (make_ch2-5, copied) = အပါယ်သို့ ရောက်စေတတ်သော
- (33) 1. Gihissa arahātikathā = (33) 1. လူဝတ်ကြောင် ရဟန္တာ ဖြစ်နိုင်သည်ဟူသော ဆွေးနွေးချက်
- Gihissa arahātikathā = လူဝတ်ကြောင် ရဟန္တာ ဖြစ်နိုင်သည်ဟူသော ဆွေးနွေးချက်
- gihissa arahā = လူဝတ်ကြောင်သည် ရဟန္တာ ဖြစ်နိုင်
- gihisaṃyojanaṃ = လူဝတ်ကြောင်၏ နှောင်ကြိုး
- ajeḷakaṃ paṭiggaṇheyya = ဆိတ်နှင့် သိုးကို ခံယူရာ
- kukkuṭasūkaraṃ paṭiggaṇheyya = ကြက်နှင့် ဝက်ကို ခံယူရာ
- hatthigavassavaḷavaṃ paṭiggaṇheyya = ဆင်၊ နွား၊ မြင်း၊ မြင်းမတို့ကို ခံယူရာ
- tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya = ခါ၊ ငုံး၊ ဒေါင်း၊ ငှက်ကြီးတို့ကို ခံယူရာ
- cittavaṇḍavālamoḷiṃ dhāreyya = အရောင်စုံ ဆံထုံးကို ဆောင်ရာ
- odātāni vatthāni dīghadasāni dhāreyya = အနားစ ရှည်သော အဖြူ အဝတ်တို့ကို ဝတ်ဆင်ရာ
- yāvajīvaṃ agāriyabhūto assa = အသက်ထက်ဆုံး လူ့ဘောင်၌ နေသူ ဖြစ်ရာ
- (34) 2. Upapattikathā = (34) 2. ပြန်လည် ဖြစ်ပေါ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Upapattikathā = ပြန်လည် ဖြစ်ပေါ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- saha upapattiyā = ပြန်လည် ဖြစ်ပေါ်သည်နှင့် တစ်ပြိုင်နက်
- upapattesiyaṃ cittaṃ = ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော စိတ်
- (35) 3. Anāsavakathā = (35) 3. စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော အရာအကြောင်း ဆွေးနွေးချက်
- Anāsavakathā = စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော အရာအကြောင်း ဆွေးနွေးချက်
- bandhana = အနှောင်အဖွဲ့
- arahā anāsavo = ရဟန္တာသည် စိတ်အစွန်းအထင်း ကင်းသူ ဖြစ်
- (36) 4. Samannāgatakathā = (36) 4. ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- Samannāgatakathā = ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- (41) 9. Aparāpi samannāgatakathā = (41) 9. နောက်ထပ် ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- Aparāpi samannāgatakathā = နောက်ထပ် ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- X-phalena samannāgato «Y»ti vattabbo = Xနှင့် ပြည့်စုံသူကို “Y”ဟု ဆိုသင့်
- (37) 5. Upekkhāsamannāgatakathā = (37) 5. ဥပေက္ခာနှင့် ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- Upekkhāsamannāgatakathā = ဥပေက္ခာနှင့် ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- satataṃ samitaṃ abbokiṇṇaṃ = အမြဲတမ်း၊ အစဉ်တစိုက်၊ ကြားမလပ်ဘဲ
- chaḷaṅgupekkho = အင်္ဂါ ခြောက်ပါးနှင့် ပြည့်စုံသော ဥပေက္ခာ ရှိသူ
- (38) 6. Bodhiyā buddhotikathā = (38) 6. ဗောဓိဖြင့် ဘုရား ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Bodhiyā buddhotikathā = ဗောဓိဖြင့် ဘုရား ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- bodhi (awakening) = ဗောဓိ
- (39) 7. Lakkhaṇakathā = (39) 7. လက္ခဏာအကြောင်း ဆွေးနွေးချက်
- Lakkhaṇakathā = လက္ခဏာအကြောင်း ဆွေးနွေးချက်
- bodhisatto = ဘုရားလောင်း
- cakkavattisatto = စကြဝတေး မင်းလောင်း
- punabbhava (make_ch2-5, copied) = ဘဝသစ်
- (40) 8. Niyāmokkantikathā = (40) 8. သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းခြင်းအကြောင်း ဆွေးနွေးချက်
- Niyāmokkantikathā = သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းခြင်းအကြောင်း ဆွေးနွေးချက်
- pāvacane okkantaniyāmo caritabrahmacariyo = သာသနာ၌ သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းပြီး၍ မြင့်မြတ်သော အကျင့်ကို ကျင့်ပြီးသူ
- anussaviyo / sayambhū = သူတစ်ပါးထံမှ ကြားနာ၍ သိသူ / ကိုယ်တိုင် အလိုလို သိတော်မူသူ
- dassanasampanno puggalo = မှန်ကန်သော အမြင်နှင့် ပြည့်စုံသော ပုဂ္ဂိုလ်
- sabbasaṃyojanānaṃ pahānaṃ = နှောင်ကြိုး အားလုံးတို့ကို ပယ်ခြင်း
- (42) 10. Sabbasaṃyojanappahānakathā = (42) 10. နှောင်ကြိုး အားလုံးတို့ကို ပယ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Sabbasaṃyojanappahānakathā = နှောင်ကြိုး အားလုံးတို့ကို ပယ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- anavasesa (make_ch2-5, copied) = အကြွင်းမဲ့

## For the consistency pass (divergences between earlier agents; the choice made here)
- aveccappasāda: ch2-5 «ခိုင်မြဲသော ကြည်ညိုမှု», ch10 «မတုန်မလှုပ်သော ကြည်ညိုမှု» -> ch10 used (^5-366).
- aṇusahagata (kāmarāga / byāpāda): ch2-5 «အနည်းငယ်မျှ ကျန်ရှိသော», ch10 «သိမ်မွေ့သော» -> ch10 used.
- ucchinnamūla … anuppādadhamma: ch2-5 and ch10 differ -> ch10's neuter wording (P6.UCCH_MY) used (^5-387).
- bodhagāmī: ch4 «ထိုးထွင်း သိခြင်းဆီသို့», ch8 «ဗောဓိဆီသို့» -> ch8 used (^5-390).
- rūparāga / arūparāga: ch10 «ရုပ်၌ တပ်မက်မှု / ရုပ်မဲ့၌ …», pi-2 ^2-U49 (and ch2-5) «သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ / ရုပ်မရှိသော
  ဘဝကို …» -> pi-2 used (^5-416, binding FINAL).
- dukkhanirodhagāminī paṭipadā: ch10 «ဒုက္ခ ချုပ်ငြိမ်းခြင်းသို့ ရောက်ကြောင်း အကျင့်», pi-2 ^2-189 «ဒုက္ခ ချုပ်ငြိမ်းရာသို့
  ရောက်စေသော ကျင့်စဉ်» -> pi-2 used in the ariyasacca sutta (^5-405).
- dibbena cakkhunā rūpaṃ passati: the sample has «နတ်မျက်စိဖြင့် ရုပ်ကို မြင်သူ» (agent in a series), ch10 / pi-1 rūpa as
  visible form «အဆင်းအရောင်» -> «နတ်မျက်စိဖြင့် အဆင်းအရောင်ကို မြင်» here (a rule, so the sample stays unchanged).
- sādhāraṇa «ဆက်ဆံ» also for «kākehi gijjhehi kulalehi sādhāraṇo» (^5-391) to keep one word.
- Quote marks the Pāli lacks: «sotāpannoti vattabbo» (^5-407, unquoted) shares its key with the quoted ^5-394 and gets
  the marks; «dve sotāni vuttāni bhagavatā – maṃsasotaṃ, dibbasotaṃ» in the Hañci clause has none (as the Pāli), the
  quoted «Nanu …» sentence has them (SENT).

## Unsure Pāli / interpretation
- sāvakasādhāraṇa «တပည့်တို့နှင့် ဆက်ဆံ» ("shared with disciples"); ariya (of a power) «အရိယာ အရာ».
- dhammupatthaddha «တရား၏ ထောက်ပံ့မှုကို ရသော»; maṃsacakkhu «ပကတိ မျက်စိ»; aṭṭhamaka «အဋ္ဌမ ပုဂ္ဂိုလ်».
- «… nuppajjissatīti katvā pahīnaṃ» = «… ဖြစ်ပေါ်လိမ့်မည် မဟုတ်ဟု အကြောင်းပြု၍ ထိုအရာကို ပယ်ပြီး» («ထိုအရာကို» supplied).
- vimuttaṃ vimuccamānaṃ = «လွတ်မြောက်ပြီးသော အရာသည် လွတ်မြောက်ဆဲ အရာ ဖြစ်»; the ratta / aratta list (^5-367) rendered
  with «…ပြီးသည်လည်း ဖြစ်၍ မ…သည်လည်း ဖြစ်» per pair.
- upapattesiya citta «ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော စိတ်»; kaṇṭhapañcamehi bandhanehi «လည်ပင်း ပါဝင်သော ပဉ္စမ ပြည့်
  အနှောင်အဖွဲ့တို့»; bandhana «အနှောင်အဖွဲ့» kept apart from saṃyojana «နှောင်ကြိုး»; arahā anāsavo «စိတ်အစွန်းအထင်း
  ကင်းသူ» (a person; the dhamma sense keeps the pi-1 dyad wording).
- chaḷaṅgupekkho «အင်္ဂါ ခြောက်ပါးနှင့် ပြည့်စုံသော ဥပေက္ခာ ရှိသူ»; satataṃ samitaṃ abbokiṇṇaṃ «အမြဲတမ်း၊ အစဉ်တစိုက်၊
  ကြားမလပ်ဘဲ»; bodhi «ဗောဓိ», bodhiyā mūle «ဗောဓိပင်ရင်း၌» (tree).
- padesa / tibhāga / upaḍḍha-bodhisatta «အချို့ / သုံးပုံတစ်ပုံ / တစ်ဝက် ဘုရားလောင်း»; cakkavattisatta «စကြဝတေး မင်းလောင်း»;
  aparantapaṃ (var. amaraṃ tapaṃ) «အခြားသော ခြိုးခြံသော အကျင့်»; anussaviya «သူတစ်ပါးထံမှ ကြားနာ၍ သိသူ»; sayambhū
  «ကိုယ်တိုင် အလိုလို သိတော်မူသူ»; the 32-marks passage and the Upaka verses are plain renderings (best guesses for the
  kingly epithets: cāturanto «လေးဘက် သမုဒ္ဒရာ အဆုံးရှိ မြေကို အစိုးရသော», vivaṭṭacchado «ကိလေသာ အဖုံးအကာကို
  ဖွင့်လှစ်ပြီးသော»).
- Verses: each stanza opens «“», only the last closes (sample convention; B4 accepts it).

## Source slips (translated as written; Pāli not changed)
- ^5-356 «sāvakaasādhāraṇa» (sandhi as written) = sāvaka-asādhāraṇa; ^5-360 «suññātārammaṇa», ^5-361
  «appapaṇihitārammaṇā»: the same Burmese as suññata- / appaṇihita-.
- ^5-379 second Yaṃ-tattha line has no dash after «vattabbe kho»; both lines close ‘…sīla"’nti (irregular order):
  regular ’” used.
- ^5-382 «so ca saññābhavo saññāgati sattāvāso saṃsāro yoni attabhāvapaṭilābho» (only the first two with saññā-) as written.
- ^5-389 «mahākaccāno» (ch2-5 has mahākaccāyano): the same Burmese «မဟာကစ္စာယန မထေရ်».
- ^5-391 the second «Labbhā …» has «gāmanigamanagarajanapadabandhanena» as one compound: one Burmese item.
- ^5-395 commas in the kilesa list (^5-408 without): the same Burmese; ^5-397 Hañci line ends «…ti…pe….».
- ^5-405 Upaka verse variants (andhabhūtasmiṃ, āhaññiṃ, dudrabhinti) as brackets; «pariññātanti / pahīnanti …» are
  unquoted in the Pāli and unquoted in the Burmese.
