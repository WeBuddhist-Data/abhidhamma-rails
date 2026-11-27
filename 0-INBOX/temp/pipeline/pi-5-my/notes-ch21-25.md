# pi-5 Burmese zero-shot, chapters 21-25: notes (21-terasamavaggo … 25-sattarasamavaggo)

Status: DONE 2026-11-20 (not committed). Brief: burmese-zeroshot-brief.md. Source rule kept: translated from the Pāli only;
no Burmese translation / nissaya opened, 0-INBOX/temp/language-priority/ not opened, no web search. English pi-5 zero-shot
(21-terasamavaggo, first kathās) read for meaning only. pi-1 … pi-4 read only through their FINAL rails texts (kwic5.py /
my5_formulas.FINAL); every reused value is witnessed (W / F.witness) at import. No /tmp used.

## Files and run
- Output: AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/
  21-terasamavaggo.md (52 segments, kathās 126-135 + uddāna), 22-cuddasamavaggo.md (43; 136-144),
  23-pannarasamavaggo.md (54; 145-155 + uddāna of the 3rd paṇṇāsaka), 24-solasamavaggo.md (53; 156-165),
  25-sattarasamavaggo.md (48; 166-176).
- make_ch21-25.py: imports make_ch11-12.py READ ONLY (which imports make_ch6-10.py, make_sample.py, my5_formulas.py);
  extends PROP / SENT / QUOTE / LINES / HEAD / COLO / ANCHOR / VAR_KIND / REF / REF_NOTE / BR_TABLE in memory only.
  P() refuses a key the imported tables already have with another Burmese (so nothing of ch1-12 is overridden;
  A2 re-checks that). Strings of make_ch2-5.py are copied verbatim (check D verifies each in the ch2-5 output).
  Run: python3 -I -X utf8 make_ch21-25.py [chapter] [--units]; check_ch21-25.py [chapter.md ...] [--why].
- New frames (inserted before the generic «P-ti?» / «P-ti.»): «P, na vattabbaṃ – "Q"ti?» = «P-သည်၊ ဤသို့
  မဆိုသင့်သလော – “Q”»; «(Tena hi) P, na vattabbaṃ – "Q"ti.»; «X-rāgo na vattabbaṃ – "Q"ti?» (no comma) = «Xကို
  ဤသို့ မဆိုသင့်သလော – “Q”»; «"P"ti – attheva suttantoti?» = «“P” – ဤသို့သော သုတ္တန် အမှန်ပင် ရှိသလော»;
  «Tena hi na vattabbaṃ – "P"ti…pe….»; «Nanu āyasmā udāyī etadavoca – "Q"ti!»; generic «(Y)yathā A, evamevaṃ B-ti?» =
  «Aသကဲ့သို့ ထို့အတူပင် Bသလော». Lines whose quotation never closes (open_q(): sentences cut with the quotes
  ignored, a protected sutta quotation kept whole): ^5-693, ^5-721, ^5-723, ^5-725, ^5-727, ^5-729, ^5-731.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all five (check_marks = pi-4-mr/check_marks.py). My chk-pe
  copies (pi-6-mr/chk-pe/21-… … 25-…) deleted; the other files in that folder are not mine and were left alone.
- check_ch21-25.py (adapted from check_ch11-12.py): A 5/5 rebuilt identical + A2 the 8 imported chapters (1, 6-12) still
  rebuild byte-identical with the ch21-25 tables installed; B1 506 lines; B2 1269 polarity marks; B2d 1191 negations
  (every Pāli negator / privative = one negative «မ»; privatives of these chapters added to PRIV, «vata no» = «for us»
  not counted, «mā» counted); B7 312 existence marks; B3 86 number words; B4 250 segments; B5 4298/4298 recurring
  sentences (also against the sample and ch6-12); B6 226 table values; 0 mismatches.
- Reuse test 1002 / 1002 (C1 110/110, C3 875/875 occurrences of 148 terms incl. the new witnessed terms of these
  chapters, D 17/17 copies of ch2-5 strings, each attested in the ch2-5 output).

## Main choices (pi-1 … pi-4 FINAL wording reused)
- Vagga ordinals 13-17 «တေရသမ / စုဒ္ဒသမ / ပန္နရသမ / သောဠသမ / သတ္တရသမ ဝဂ်» (the ORD_MY pattern ပထမ … ဒသမ continued;
  the agents of vaggas 11-12 will choose ဧကာဒသမ / ဒွါဒသမ or similar: align in the consistency pass).
- taṇhā «တပ်မက်မှု», rūpa- … dhammataṇhā «Xကို တပ်မက်မှု» (pi-2 ^2-U62); the «yāyaṃ taṇhā ponobbhavikā …» quotation
  read from pi-2 ^2-203; lobha «လောဘ» (pi-1); kusalākusala / sāvajjānavajja / hīnapaṇīta / kaṇhasukkasappaṭibhāga from
  pi-4 ^4-104; the five ānantarika deeds from pi-2 ^2-U55; kukkucca «နောင်တ ပူပန်မှု», nīvaraṇa «အတားအဆီး» (pi-1);
  the four iddhipādas (pi-2 headings); vivicceva kāmehi … / vitakkavicārānaṃ vūpasamā (pi-1 ^1-160/161);
  sukha / dukkha / adukkhamasukha vedanā (pi-1 triad); anusaya / pariyuṭṭhāna and the 7 anusaya (pi-2 ^2-816, ch6-10,
  ch11-12); kāma- / byāpāda- / vihiṃsāsaññā (pi-2 ^2-911), mettā … upekkhā (pi-2 ^2-683); sabbaṅgapaccaṅgī
  ahīnindriyo (pi-2 ^2-951, as a person); kesā lomā nakhā dantā aṭṭhi (pi-2 ^2-173); cakkhuviññāṇa «မျက်စိ သိစိတ်»
  (pi-1), «cakkhuñca paṭicca rūpe ca» (pi-2 ^2-184); mahābhūta «မူလဓာတ်ကြီး», upādāya rūpaṃ (pi-1 ^1-584);
  diṭṭhigata «အယူမှား» and the ten views (pi-1 ^1-1105); paṭiccasamuppāda links (pi-1 ^1-1343); saññāvedayitanirodha
  (pi-2 ^2-808); alobha / adosa (pi-1 ^1-32/33); sahetuka, sārammaṇa / anārammaṇa, cittacetasika, kammassa katattā
  (pi-1); puñña- / āneñjābhisaṅkhāra (pi-2 ^2-817); the misdeeds (pi-2 ^2-487); the requisites (pi-2 ^2-849);
  rūparāga / arūparāga (pi-2 ^2-U49, as ch11-12); adhipati «အကြီးအမှူး» (pi-3 ^3-98); āsevana (pi-1 ^1-1361).
- From ch11-12 / ch6-10 (imported): the ekuppāda list frame «… စိတ်တို့နှင့်အတူ ဖြစ်သော၊ …»; upapattesiya, sahajāta,
  pariyāpanna / apariyāpanna, the path / fruit names, the jhāna word, kamma words; «arahato kāye visaṃ kameyya …» =
  «… တိုးဝင်ရာ၏၊ …» (ch11-12 ^5-391 wording, also used for the nirodha-attainer and the negative forms).
- From ch2-5 (copied, check D): jahati «စွန့်ပယ်», kālaṃ karoti «သေ», ācināti … sandhūpeti (ACINA), arahantaghātaka.

## New recurring terms and phrases (Pāli = Burmese; the NEW table of make_ch21-25.py, headings left out)
- Terasamavaggo = တေရသမ ဝဂ်
- Cuddasamavaggo = စုဒ္ဒသမ ဝဂ်
- Pannarasamavaggo = ပန္နရသမ ဝဂ်
- Soḷasamavaggo = သောဠသမ ဝဂ်
- Sattarasamavaggo = သတ္တရသမ ဝဂ်
- sammukhībhāvaṃ āgacchanti = မျက်နှာချင်းဆိုင် ဖြစ်လာကြ
- vipākābyākata / kiriyābyākata = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အရာ / ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အရာ
- kappaṭṭho = ကမ္ဘာ ပတ်လုံး တည်ရမည့်သူ
- kappaṭṭhiyaṃ kammaṃ = ကမ္ဘာ ပတ်လုံး တည်စေသော ကံ
- Kappaṭṭhakathā = ကမ္ဘာ ပတ်လုံး တည်ရမည့်သူအကြောင်း ဆွေးနွေးချက်
- yogakkhema = ထမ်းပိုးမှ လွတ်ငြိမ်းရာ
- Kusalapaṭilābhakathā = ကုသိုလ်ကို ရခြင်းအကြောင်း ဆွေးနွေးချက်
- dānaṃ dadeyya = ဒါန ပြုရာ
- cetiya = စေတီ
- sammattaniyāma = မှန်ကန်မှု၌ သေချာသော လမ်းကြောင်း
- micchattaniyāma = မှားယွင်းမှု၌ သေချာသော လမ်းကြောင်း
- anantarāpayutto puggalo = ချက်ချင်း အကျိုးပေးသော ကံကို ပြုခဲ့သော ပုဂ္ဂိုလ်
- Anantarāpayuttakathā = ချက်ချင်း အကျိုးပေးသော ကံကို ပြုခဲ့သော ပုဂ္ဂိုလ်အကြောင်း ဆွေးနွေးချက်
- vippaṭisāriya = စိတ် ပူလောင်မှု
- niyato (a person) = လမ်းကြောင်း သေချာပြီးသူ
- micchattaniyato = မှားယွင်းမှု၌ လမ်းကြောင်း သေချာပြီးသူ
- sammattaniyato = မှန်ကန်မှု၌ လမ်းကြောင်း သေချာပြီးသူ
- Niyatassa niyāmakathā = လမ်းကြောင်း သေချာပြီးသူ၏ သေချာသော လမ်းကြောင်းအကြောင်း ဆွေးနွေးချက်
- nivuto = အတားအဆီး ဖုံးလွှမ်းထားသူ
- Nivutakathā = အတားအဆီး ဖုံးလွှမ်းထားသူအကြောင်း ဆွေးနွေးချက်
- sammukhībhūto = နှောင်ကြိုးနှင့် မျက်နှာချင်းဆိုင် ဖြစ်နေသူ
- Sammukhībhūtakathā = နှောင်ကြိုးနှင့် မျက်နှာချင်းဆိုင် ဖြစ်နေသူအကြောင်း ဆွေးနွေးချက်
- jhānanikanti = ဈာန်ကို စွဲလန်းခြင်း
- Samāpanno assādetikathā = သမာပတ်ကို ဝင်စားနေသူ သာယာသည်ဟူသော ဆွေးနွေးချက်
- so taṃ assādeti taṃ nikāmeti tena ca vittiṃ āpajjati = ထိုသူသည် ထိုဈာန်ကို သာယာ၏၊ ထိုဈာန်ကို နှစ်သက်တောင့်တ၏၊ ထိုဈာန်ဖြင့်လည်း နှစ်သိမ့်မှုသို့ ရောက်၏
- asātarāgo = မသာယာဖွယ်ကို တပ်မက်မှု
- Asātarāgakathā = မသာယာဖွယ်ကို တပ်မက်မှုအကြောင်း ဆွေးနွေးချက်
- Dhammataṇhā abyākatātikathā = သဘောတရားကို တပ်မက်မှုသည် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Dhammataṇhā na dukkhasamudayotikathā = သဘောတရားကို တပ်မက်မှုသည် ဒုက္ခ ဖြစ်ပေါ်ခြင်း မဟုတ်ဟူသော ဆွေးနွေးချက်
- Kusalākusalapaṭisandahanakathā = ကုသိုလ် အကုသိုလ် ဆက်စပ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- paṇidhi = စိတ်ကို ထားရှိခြင်း
- yoniso / ayoniso manasikaroto = သင့်လျော်စွာ / မသင့်လျော်စွာ နှလုံးသွင်းသူအား
- nekkhamma- / abyāpāda- / avihiṃsāsaññā = ကာမမှ ထွက်မြောက်ခြင်းဆိုင်ရာ မှတ်သိမှု / မဖျက်ဆီးလိုခြင်းဆိုင်ရာ မှတ်သိမှု / မညှဉ်းပန်းခြင်းဆိုင်ရာ မှတ်သိမှု
- arati = မမွေ့လျော်မှု
- X-assa anantarā = X၏ ချက်ချင်း နောက်၌
- Saḷāyatanuppattikathā = အာရုံခံ နယ်ပယ် ခြောက်ပါး ဖြစ်ပေါ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Anantarapaccayakathā = ချက်ချင်း နောက်၌ ဖြစ်စေသော အကြောင်းအကြောင်း ဆွေးနွေးချက်
- ariyarūpaṃ = အရိယာ ရုပ်
- Ariyarūpakathā = အရိယာ ရုပ်အကြောင်း ဆွေးနွေးချက်
- Añño anusayotikathā = ကိန်းအောင်းခြင်းသည် တခြား ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Pariyuṭṭhānaṃ cittavippayuttantikathā = ထကြွခြင်းသည် စိတ်နှင့် ကင်းကွာသော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Pariyāpannakathā = ဘဝဘုံတို့၌ အကျုံးဝင်သော အရာအကြောင်း ဆွေးနွေးချက်
- rūpadhātu / arūpadhātu (realms) = သိမ်မွေ့သော ရုပ် ဓာတ် / ရုပ်မရှိသော ဓာတ်
- samāpattesiya = သမာပတ်ကို ရှာသော
- diṭṭhadhammasukhavihāra = ယခုဘဝ၌ ချမ်းသာစွာ နေခြင်း ဖြစ်သော
- sahagato sahajāto saṃsaṭṭho sampayutto ekuppādo ekanirodho ekavatthuko ekārammaṇo = အတူ ဖြစ်သော၊ အတူ ပေါ်ပေါက်သော၊ ရောနှောသော၊ ယှဉ်တွဲသော၊ အတူ ဖြစ်ပေါ်သော၊ အတူ ချုပ်သော၊ မှီရာ တူသော၊ အာရုံ တူသော
- Abyākatakathā = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အရာအကြောင်း ဆွေးနွေးချက်
- abyākatametaṃ (undeclared) = ဤသည်ကို မဖြေကြားအပ်
- Apariyāpannakathā = ဘဝဘုံတို့၌ အကျုံးမဝင်သော အရာအကြောင်း ဆွေးနွေးချက်
- paccayatā = အကြောင်းဖြစ်ပုံ
- Paccayatākathā = အကြောင်းဖြစ်ပုံအကြောင်း ဆွေးနွေးချက်
- X-paccayena paccayo = Xဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်
- Aññamaññapaccayakathā = အချင်းချင်း အကြောင်း ဖြစ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- addhā = ကာလ
- parinipphanna = အမှန်တကယ် ဖြစ်ပေါ်ပြီးသော
- Addhākathā = ကာလအကြောင်း ဆွေးနွေးချက်
- khaṇo / layo / muhuttaṃ = ခဏ / အခိုက်အတန့် / မုဟုတ်ကာလ
- Khaṇalayamuhuttakathā = ခဏ၊ အခိုက်အတန့်၊ မုဟုတ်ကာလအကြောင်း ဆွေးနွေးချက်
- Āsavakathā = စိတ်အစွန်းအထင်းအကြောင်း ဆွေးနွေးချက်
- Jarāmaraṇakathā = အိုခြင်း သေခြင်းအကြောင်း ဆွေးနွေးချက်
- saññāvedayitanirodhasamāpatti = မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန် ဝင်စားခြင်း
- saññāvedayitanirodhaṃ samāpanno = မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်ကို ဝင်စားနေသူ
- Saññāvedayitakathā = မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်အကြောင်း ဆွေးနွေးချက်
- Dutiyasaññāvedayitakathā = ဒုတိယ မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်အကြောင်း ဆွေးနွေးချက်
- Tatiyasaññāvedayitakathā = တတိယ မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်အကြောင်း ဆွေးနွေးချက်
- māraṇantiya = သေခါနီး
- so niyāmo yena niyāmena niyato (a fixed law) = အကြင် စည်းမျဉ်းဖြင့် သတ်မှတ်ထားသောကြောင့် …၊ ထိုစည်းမျဉ်း
- asaññasattupika = အသညသတ် ဘုံသို့ ရောက်စေတတ်သော
- Asaññasattupikakathā = အသညသတ် ဘုံသို့ ရောက်စေတတ်သော အရာအကြောင်း ဆွေးနွေးချက်
- kammūpacayo = ကံ၏ စုဆောင်းမှု
- Kammūpacayakathā = ကံ၏ စုဆောင်းမှုအကြောင်း ဆွေးနွေးချက်
- sabyābajjhampi abyābajjhampi = ဆင်းရဲစေတတ်သည်လည်း ဖြစ် မဆင်းရဲစေတတ်သည်လည်း ဖြစ်သော
- paṇṇāsaka = ငါးဆယ်အစု
- niggaṇhāti / paggaṇhāti (a mind) = ချုပ်ကိုင် / မြှင့်တင်
- Niggahakathā = စိတ်ကို ချုပ်ကိုင်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Paggahakathā = စိတ်ကို မြှင့်တင်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Sukhānuppadānakathā = သုခကို ပေးခြင်းအကြောင်း ဆွေးနွေးချက်
- adhigayha manasi karoti = အလုံးစုံကို စုပေါင်း၍ နှလုံးသွင်း
- Adhigayhamanasikārakathā = အလုံးစုံကို စုပေါင်း၍ နှလုံးသွင်းခြင်းအကြောင်း ဆွေးနွေးချက်
- Rūpaṃ hetūtikathā = ရုပ်သည် အမြစ် ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Rūpaṃ sahetukantikathā = ရုပ်သည် အမြစ် ရှိသော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Rūpaṃ kusalākusalantikathā = ရုပ်သည် ကုသိုလ် အကုသိုလ် ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Rūpaṃ vipākotikathā = ရုပ်သည် ကံ၏ အကျိုး ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- sukhavedaniya / dukkhavedaniya / adukkhamasukhavedaniya = သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော / နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော / မနာကျင် မသာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော
- Rūpaṃ rūpāvacarārūpāvacarantikathā = ရုပ်သည် သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော အရာ၊ ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Rūpārūpadhātupariyāpannakathā = သိမ်မွေ့သော ရုပ် ဓာတ်၊ ရုပ်မရှိသော ဓာတ်၌ အကျုံးဝင်ခြင်းအကြောင်း ဆွေးနွေးချက်
- puññūpacayo = ကောင်းမှု စုဆောင်းခြင်း
- apuññūpacayo = မကောင်းမှု စုဆောင်းခြင်း
- Arahato puññūpacayakathā = ရဟန္တာ၏ ကောင်းမှု စုဆောင်းခြင်းအကြောင်း ဆွေးနွေးချက်
- akālamaccu = အချိန်မတန်မီ သေခြင်း
- Natthi arahato akālamaccūtikathā = ရဟန္တာ၌ အချိန်မတန်မီ သေခြင်း မရှိဟူသော ဆွေးနွေးချက်
- sati / asati jīvite jīvitāvasese = အသက်နှင့် အသက် အကြွင်းအကျန် ရှိစဉ် / အသက်နှင့် အသက် အကြွင်းအကျန် မရှိစဉ်
- Sabbamidaṃ kammatotikathā = ဤအရာ အားလုံးသည် ကံကြောင့် ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- indriyabaddha = စွမ်းရည်တို့နှင့် ဆက်စပ်သော
- anindriyabaddha = စွမ်းရည်တို့နှင့် မဆက်စပ်သော
- Indriyabaddhakathā = စွမ်းရည်တို့နှင့် ဆက်စပ်သော အရာအကြောင်း ဆွေးနွေးချက်
- Ṭhapetvā ariyamaggantikathā = အရိယာ မဂ်ကို ချန်ထား၍ဟူသော ဆွေးနွေးချက်
- Na vattabbaṃ saṅgho dakkhiṇaṃ paṭiggaṇhātikathā = သံဃာသည် အလှူကို ခံယူသည်ဟု မဆိုသင့်ဟူသော ဆွေးနွေးချက်
- Na vattabbaṃ saṅgho dakkhiṇaṃ visodhetītikathā = သံဃာသည် အလှူကို စင်ကြယ်စေသည်ဟု မဆိုသင့်ဟူသော ဆွေးနွေးချက်
- Na vattabbaṃ saṅgho bhuñjatītikathā = သံဃာသည် စားသည်ဟု မဆိုသင့်ဟူသော ဆွေးနွေးချက်
- Na vattabbaṃ saṅghassadinnaṃ mahapphalantikathā = သံဃာအား လှူသော အလှူသည် အကျိုး ကြီးမားသည်ဟု မဆိုသင့်ဟူသော ဆွေးနွေးချက်
- Na vattabbaṃ buddhassadinnaṃ mahapphalantikathā = ဘုရားအား လှူသော အလှူသည် အကျိုး ကြီးမားသည်ဟု မဆိုသင့်ဟူသော ဆွေးနွေးချက်
- āhuneyyo pāhuneyyo dakkhiṇeyyo añjalikaraṇīyo anuttaraṃ puññakkhettaṃ lokassa = ပူဇော်ဖွယ်တို့ကို ခံထိုက်သော၊ ဧည့်ဝတ်တို့ကို ခံထိုက်သော၊ အလှူကို ခံထိုက်သော၊ လက်အုပ်ချီ၍ ရှိခိုးထိုက်သော၊ လောက၏ အမြတ်ဆုံး ကောင်းမှု လယ်မြေ
- cattāro purisayugā aṭṭha purisapuggalā = လူ အစုံ လေးစုံ၊ ပုဂ္ဂိုလ် ရှစ်ယောက်
- ambapānaṃ … phārusakapānaṃ = သရက်သီး အဖျော်၊ သပြေသီး အဖျော်၊ အစေ့ပါ ငှက်ပျောသီး အဖျော်၊ အစေ့ကင်း ငှက်ပျောသီး အဖျော်၊ မဓုက သီး အဖျော်၊ စပျစ်သီး အဖျော်၊ ကြာရင်းမြစ် အဖျော်၊ ဖာရုသက သီး အဖျော်
- dakkhiṇāvisuddhi = အလှူ၏ စင်ကြယ်ခြင်း
- Dakkhiṇāvisuddhikathā = အလှူ၏ စင်ကြယ်ခြင်းအကြောင်း ဆွေးနွေးချက်

## For the consistency pass (divergences; the choice made here)
- kameyya (visaṃ / satthaṃ / aggi): ch2-5 «ထိရောက်နိုင်», ch11-12 «တိုးဝင်ရာ» -> ch11-12 used (^5-732, ^5-781).
- niggaha / niggaṇhāti (restraining a mind, ch24) «ချုပ်ကိုင်» kept apart from the dialectic niggaha «ချေပချက်».
- niyāma: path sense «သေချာသော လမ်းကြောင်း» (pi-4); «so niyāmo yena niyāmena niyato» (a fixed law, ^5-733/734)
  «စည်းမျဉ်း» (another sense).
- abyākata (ethically) = the core term; «abyākatametaṃ» (undeclared, ^5-708) «ဤသည်ကို မဖြေကြားအပ်» (the opponent's pun
  on the two senses cannot be kept in Burmese).
- rūpadhātu (realm, ch22/24) «သိမ်မွေ့သော ရုပ် ဓာတ်», arūpadhātu «ရုပ်မရှိသော ဓာတ်», kāmadhātu «ကာမ ဓာတ်» (pi-2); the sense
  elements «Xကို တပ်မက်သော ရာဂ» / «X ဓာတ်» keep the parallel the argument needs.
- okkamati: niyāma «သက်ဆင်း» (pi-4), mātukucchismiṃ okkamati also «သက်ဆင်း».
- dukkha / sukha as objects (ch21, ch24) «ဒုက္ခ» / «သုခ»; as vedanā «နာကျင်သော / သာယာသော ခံစားမှု» (pi-1).
- vipāka «ကံ၏ အကျိုး» (pi-1), phala «အကျိုး»; kammūpacaya «ကံ၏ စုဆောင်းမှု».
- The C3 reuse test does not ask «နှင့် ရောနှောသော / နှင့် ယှဉ်တွဲသော» inside the ekuppāda list (one «နှင့်» for the list)
  nor pi-1 «ဘဝဘုံတို့၌ အကျုံးဝင်သော» for «X-dhātupariyāpanna» («X ဓာတ်၌ အကျုံးဝင်»).

## Unsure Pāli / interpretation
- kappaṭṭha «ကမ္ဘာ ပတ်လုံး တည်ရမည့်သူ» (the schismatic in hell for an aeon); kappaṭṭhiya kamma «… တည်စေသော ကံ»;
  aparāpariyavepakka «နောက်ဘဝ အဆက်ဆက်၌ အကျိုးပေးသော».
- anantarāpayutta «ချက်ချင်း အကျိုးပေးသော ကံကို ပြုခဲ့သော»; vippaṭisāriya «စိတ် ပူလောင်မှု» (kept apart from kukkucca).
- sammukhībhūta «နှောင်ကြိုးနှင့် မျက်နှာချင်းဆိုင် ဖြစ်နေသူ» («နှောင်ကြိုး» supplied from the proposition); sammukhībhāvaṃ
  āgacchanti «မျက်နှာချင်းဆိုင် ဖြစ်လာကြ».
- asātarāga «မသာယာဖွယ်ကို တပ်မက်မှု»; anurodhavirodha «လိုက်လျောခြင်း ဆန့်ကျင်ခြင်း».
- paṇidhi «စိတ်ကို ထားရှိခြင်း» (no FINAL witness found); āvaṭṭanā «စိတ်ကို လှည့်ဆောင်ခြင်း» (pi-2).
- The embryo verse (^5-692): kalala / abbuda / pesi / ghana / pasākhā = «အရည်ကြည် / အမြှုပ် / အသားစ / အခဲ / အကိုင်းအခက်».
- paccayatā «အကြောင်းဖြစ်ပုံ», vavatthita «ပိုင်းခြား သတ်မှတ်ပြီး»; X-paccayena paccayo «Xဟူသော အကြောင်းဖြင့် အကြောင်း
  ဖြစ်» (pi-7 not yet in Burmese; anantara «ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း», ch22 heading «ချက်ချင်း နောက်၌ ဖြစ်စေသော
  အကြောင်း»).
- addhā «ကာလ», parinipphanna «အမှန်တကယ် ဖြစ်ပေါ်ပြီး»; khaṇa / laya / muhutta «ခဏ / အခိုက်အတန့် / မုဟုတ်ကာလ».
- māraṇantiya «သေခါနီး»; asaññasattupika «အသညသတ် ဘုံသို့ ရောက်စေတတ်သော»; adhigayha manasi karoti «အလုံးစုံကို
  စုပေါင်း၍ နှလုံးသွင်း».
- paggaṇhāti «မြှင့်တင်»; balappattā / vasībhūtā «စွမ်းအားသို့ ရောက်ပြီးသူတို့ / အလိုအတိုင်း ဖြစ်စေနိုင်သူတို့».
- sukhavedaniya «သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော»; upādāyahetu «မှီရာ အမြစ်».
- akālamaccu «အချိန်မတန်မီ သေခြင်း»; sati / asati jīvite jīvitāvasese «အသက်နှင့် အသက် အကြွင်းအကျန် ရှိစဉ် / မရှိစဉ်».
- The misdeeds sandhiṃ chindeyya … nigamaghātakaṃ kareyya; the eight drinks (coca / moca «အစေ့ပါ / အစေ့ကင်း ငှက်ပျောသီး»,
  madhuka / phārusaka kept as names); saṅghabhatta / uddesabhatta «သံဃာအတွက် ဆွမ်း / ခွဲဝေ ဆွမ်း»; gaṇabhojana …
  anatirittabhojana; ārādheti (dakkhiṇaṃ) «အလှူကို အောင်မြင်စေ»; the Sakka verses and vi.va. verses (plain renderings);
  dvipadānaṃ aggo … appaṭipuggalo; paññāsīlasamāhito «ပညာ၊ သီလ၊ သမာဓိနှင့် ပြည့်စုံသော».
- Verse stanzas keep the Pāli convention: each stanza opens «“», only the last closes (B4 accepts it). In the
  Nayimasmiṃ verse (^5-799) the negation «မရှိ» is put on the first line (the Pāli «na» stands there).
- Quote marks added where the Pāli has none: «yadaniccaṃ taṃ dukkhaṃ» (^5-787, a quoted saying).

## Source slips (translated as written; Pāli not changed)
- Unclosed quotations: ^5-693 («"yā … paṇidhīti? Āmantā. …»), ^5-721 / ^5-723 / ^5-725 / ^5-727 / ^5-729 / ^5-731
  («Na vattabbaṃ – "X-ti? Āmantā. …»), ^5-733 (last «"…kareyyāti.»): the Burmese closes them after the proposition.
- Comma for «? Āmantā.» / «? Na hevaṃ»: ^5-693 «…uppajjatīti, āmantā.», ^5-704 «…pariyāpanno"ti, na hevaṃ vattabbe»,
  ^5-738 «…sahajātoti, āmantā.» / «…kusaloti, na hevaṃ vattabbe…», ^5-742 «…kammūpacayoti, āmantā.»: as one sentence.
- ^5-656: the bracket «[vehāsaṃ gacchatīti (?) …]» stands after «vattabbe…pe…»: in the Burmese before the «…».
- ^5-745 «"mā rajji,""mā dussi,"…» without spaces; ^5-791 «aṭṭhapurisapuggalā» (one word): the same Burmese.
- ^5-701 «sānusayo» / ^5-709 «Vigatadiṭṭhiyo» etc. read as names in quotes (as the Pāli).
- ^5-778 «nevācināti nāpacināti» vs «nevācināti na apacināti»: the same Burmese.
- ^5-792 colophon «…paṭiggaṇhātītikathā» vs heading «…paṭiggaṇhātikathā»; ^5-798 / ^5-799 colophons «saṅghassa dinnaṃ» vs
  headings «saṅghassadinnaṃ»; ^5-775 colophon «Rūparāgo rūpadhātupariyāpanno … tikathā» before the heading's name.
- ^5-742 uddāna «saññāvedayitanirodhasamāpatti lokuttarā / lokiyā», «sveva maggo asaññasattupapattiyā» as written.
