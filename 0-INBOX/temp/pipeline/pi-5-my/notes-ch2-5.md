# pi-5 Burmese zero-shot, chapters 2-5: notes (2-parihanikatha, 3-brahmacariyakatha, 4-jahatikatha, 5-sabbamatthitikatha)

Status: DONE 2026-11-20 (not committed). Brief: burmese-zeroshot-brief.md. Model: the approved sample (my5_formulas.py
imported and extended IN MEMORY only, never edited; make_sample.py never run or imported).
Source rule kept: Pāli only; no Burmese translation / nissaya opened, 0-INBOX/temp/language-priority/ not opened, no web
search. English pi-5 zero-shot read for meaning only (Sabbamatthi ^5-282 / ^5-288 / ^5-295). pi-1 … pi-4 read only
through their FINAL rails texts and the locked termbases (grep / kwic5.py lookups).

## Files
- Output: AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/ 2-parihanikatha.md (34 segments,
  150 lines), 3-brahmacariyakatha.md (14 segments, 77 lines: Brahmacariyakathā + Odhisokathā), 4-jahatikatha.md
  (6 segments, 36 lines), 5-sabbamatthitikatha.md (26 segments, 113 lines).
- make_ch2-5.py (generator: tables PROP_X / SENT_X / LINES_X / QUOTE_X, rules via F.rule, frames inserted before the
  two generic frames, LATE functions composing whole lines from translated units), check_ch2-5.py.
- Run: python3 -I -X utf8 make_ch2-5.py [chapter] [--misses]; check_ch2-5.py [--why].

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all four (check_marks.py is pi-4-mr/check_marks.py: the
  path pi-5-mr/check_marks.py of the brief does not exist). My chk-pe copies (pi-6-mr/chk-pe/2-…5-*.md) deleted.
- check_ch2-5.py: A 4/4 rebuilt identical; B1 376 lines; B2 1569 polarity marks (upalabbh / vattabba / Āmantā /
  Na hevaṃ + parihāyati «ဆုတ်ယုတ်» + jahati «စွန့်ပယ်», negation by clause) + B2d 1221 negations (every Pāli
  negator and listed privative = one negative «မ» in the Burmese line; non-negative «မ» words: မနော, မထေရ်, မဟာ,
  မဂဓ, ကာမ, သို့မဟုတ်, …မဆို «whatever»); B3 107 number words; B4 80 segments; B5 1085/1085 recurring sentences
  (118); B6 63 headings / colophons / table lines; 0 mismatches.
- Reuse test 1331 / 1331 (C1 topic names 59/59, C3 102 terms 1272/1272; per chapter 579/579, 269/269, 115/115,
  368/368). The witnesses are searched in the FINAL texts by check_ch2-5.py itself (W() of the generator also falls
  back to a search when the given segment does not hold the pair).
- Mutation test: a dropped «မ» (jahati, ch4), a «မ…သေး» turned positive and a changed digit (ch5) are all caught.
- One real bug the checks caught during the run: «adhimattā … bhāvanā» in the Hañci clause had come out negative
  (fixed: VV()).

## Main choices (frames and building blocks)
- parihāyati = «ဆုတ်ယုတ်» (pi-4 ^4-7), arahatta = «ရဟန္တာ အဖြစ်» (abstract of pi-1/pi-2 «ရဟန္တာ»), the fruits
  pi-2 ^2-807; «S F parihāyati» = «Sသည် Fမှ ဆုတ်ယုတ်»; parihāyittha (theras) = «ဆုတ်ယုတ်ခဲ့».
- Question-word clauses (kiṃ / kattha / kuhiṃ / katamena) end «…သနည်း» in every position (class Wh); elliptical
  noun questions «Sotāpattimaggenāti?» = «…ဖြင့်လော။» (SENT).
- New frames (sentence level): «S F parihāyamāno kattha saṇṭhātīti?»; «kassa bahutarā kilesā pahīnā / adhimattā
  X-bhāvanā A vā B vāti?» = «Aနှင့် Bတို့အနက် အဘယ်သူ…သနည်း»; «Hañci P, tena vata re vattabbe – Q ti…pe….»
  (ends «…»); «X-dassanena kiṃ jahatīti?»; «Hañci P, Q-ti micchā.» (^5-288); «Hañci P, tena… Q-ti.» (^5-295, no
  «vattabbe»); «No ce pana P-ti, no ca vata re vattabbe – Q» = «တစ်ဖန် အကယ်၍ P ဟူသည် မဟုတ်လျှင် …» (^5-295);
  «nanu P-ti?» with a small letter after «…pe… ».
- brahmacariyavāsa = «မြင့်မြတ်သော အကျင့်ကို ကျင့်သုံးခြင်း» (pi-2 brahmacariya); its place rules (LOC (n)atthi
  …, yattha … tattheva / natthi tattha …, yo … tasseva / natthi tassa …).
- jahati = «စွန့်ပယ်» (kept apart from pajahati / pahīna «ပယ်»), vikkhambheti = «ဖိနှိပ်ထား».
- The arahant epithets (vītarāgo … suvijitavijayo) and the accomplished tasks (dukkhaṃ tassa pariññātaṃ …
  sacchikātabbaṃ sacchikataṃ) one building block each, used in ch2 and Odhiso.
- The 13 path qualities (niyyāniko … asaṃkilesiyo / aniyyāniko … saṃkilesiyo) from pi-1 (dyad wording «…၏ အာရုံ
  (မ)ဖြစ်နိုင်သော»); na khayagāmī etc. «…ဆီသို့ ဦးမတည်သော».
- Sabbamatthi: atīta / anāgata / paccuppanna pi-1 «အတိတ် / အနာဂတ် / ပစ္စုပ္ပန်»; «X atthi» = «X ရှိ», «atthi X» =
  «ရှိသော အရာသည် X», nvatthi / nvā- = «မရှိ» / «… မဟုတ်»; the two participle sets (niruddhaṃ … abbhatthaṅgataṃ
  «…ပြီး», negatives «မ…သေး»; jātaṃ … pātubhūtaṃ) in one rule (a partial list with a subject is a fragment);
  nicca … avipariṇāmadhamma = the sample's NICCA, the negative ANICCA4 new; «Xbhāvaṃ (na) jahati» = «X ဖြစ်ခြင်းကို
  (မ)စွန့်ပယ်»; the rūpa formula of ^5-296 is pi-2 ^2-2's wording; the ten akusala agents are pi-4 ^4-136's.
- Visible object rūpaṃ (^5-289 «atītaṃ rūpaṃ passati») = «အဆင်းအရောင်» (pi-2 rūpāyatana), excluded from C1 as the
  sample excluded rūpā.

## New terms and strings (Pāli = Burmese; also the whole NEW table of make_ch2-5.py)
- arahatta (arahantship) = ရဟန္တာ အဖြစ်
- apāyagamanīya = အပါယ်သို့ ရောက်စေတတ်သော
- aṇusahagata = အနည်းငယ်မျှ ကျန်ရှိသော
- brahmacariyavāsa = မြင့်မြတ်သော အကျင့်ကို ကျင့်သုံးခြင်း
- jahati = စွန့်ပယ်
- saṇṭhāti = တည်
- parihāyati = ဆုတ်ယုတ်
- Parihānikathā = ဆုတ်ယုတ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Vādayuttiparihāni = ဆုတ်ယုတ်ခြင်း၌ ဝါဒ၏ ယုတ္တိ
- Ariyapuggalasaṃsandanaparihāni = ဆုတ်ယုတ်ခြင်း၌ အရိယာ ပုဂ္ဂိုလ်တို့ကို နှိုင်းယှဉ်ခြင်း
- Ariyapuggalasaṃsandanaṃ = အရိယာ ပုဂ္ဂိုလ်တို့ကို နှိုင်းယှဉ်ခြင်း
- Suttasādhanaparihāni = ဆုတ်ယုတ်ခြင်း၌ သုတ္တန်ဖြင့် သက်သေပြခြင်း
- Brahmacariyakathā = မြင့်မြတ်သော အကျင့်အကြောင်း ဆွေးနွေးချက်
- Suddhabrahmacariyakathā = ရိုးရိုး မြင့်မြတ်သော အကျင့်အကြောင်း ဆွေးနွေးချက်
- Saṃsandanabrahmacariyakathā = နှိုင်းယှဉ်ခြင်းဖြင့် မြင့်မြတ်သော အကျင့်အကြောင်း ဆွေးနွေးချက်
- Odhisokathā = အပိုင်းအပိုင်း စွန့်ပယ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Jahatikathā = စွန့်ပယ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Nasuttāharaṇakathā = သုတ္တန်ကို မကိုးကားသော ဆွေးနွေးချက်
- Suttāharaṇakathā = သုတ္တန်ကို ကိုးကားသော ဆွေးနွေးချက်
- Sabbamatthītikathā = အရာအားလုံး ရှိသည် ဟူသော ဆွေးနွေးချက်
- Vādayutti = ဝါဒ၏ ယုတ္တိ
- Kālasaṃsandanā = အချိန်ကို နှိုင်းယှဉ်ခြင်း
- Vacanasodhanā = စကားလုံးကို စိစစ်ခြင်း
- Atītacakkhurūpādikathā = အတိတ် မျက်စိ၊ ရုပ် စသည်အကြောင်း ဆွေးနွေးချက်
- Atītañāṇādikathā = အတိတ် ဉာဏ် စသည်အကြောင်း ဆွေးနွေးချက်
- Arahantādikathā = ရဟန္တာ စသည်အကြောင်း ဆွေးနွေးချက်
- Atītahatthādikathā = အတိတ် လက် စသည်အကြောင်း ဆွေးနွေးချက်
- Atītakkhandhādisamodhānakathā = အတိတ် အစုအဝေး စသည်တို့ကို ပေါင်းစုခြင်းအကြောင်း ဆွေးနွေးချက်
- Padasodhanakathā = ပုဒ်ကို စိစစ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Suttasādhanaṃ = သုတ္တန်ဖြင့် သက်သေပြခြင်း
- [(āmantā) (?) evaṃ anantaravārattayepi] = [(ဟုတ်ပါသည်) (မသေချာ) နောက်ဆက်တွဲ အကြိမ် သုံးကြိမ်၌လည်း ဤနည်းတူ]
- [(āmantā) (ka.)] = [(ဟုတ်ပါသည်) (Ka.)]
- [no vata re (syā. pī.) evamuparipi] = [ပါဌ်ကွဲ (Syā., Pī.): no vata re၊ အထက်၌လည်း ဤနည်းတူ]
- [mahākaccāno (ma. ni. 1.202 ādayo)] = [စာလုံးပေါင်းကွဲ (“မဇ္ဈိမနိကာယ်” 1.202 စသည်): mahākaccāno]
- [paṭipādā (aṭṭha.)] = [စာလုံးပေါင်းကွဲ (အဋ္ဌကထာ): paṭipādā]
- [mahāva. 244; a. ni. 6.55] = [“မဟာဝဂ်” 244၊ “အင်္ဂုတ္တရနိကာယ်” 6.55]
- [khu. pā. 6.10; su. ni. 233] = [“ခုဒ္ဒကပါဌ” 6.10၊ “သုတ္တနိပါတ်” 233]
- [aṅguttaranikāye] = [“အင်္ဂုတ္တရနိကာယ်”၌]
- [saṃyuttanikāye] = [“သံယုတ္တနိကာယ်”၌]
- [( ) (?)] = [( ) (မသေချာ)]
- [na jahatīti (bahūsu) aṭṭhakathā oloketabbā] = [ပါဌ်ကွဲ (အများစု၌): na jahatīti၊ အဋ္ဌကထာကို ကြည့်ပါ]
- [na jahatīti (bahūsu) anulomapañhoyeva] = [ပါဌ်ကွဲ (အများစု၌): na jahatīti၊ အစဉ်အတိုင်း အမေးသာ ဖြစ်သည်]
- [na jahatīti (?) purimapañhehi saṃsandetabbaṃ] = [ပါဌ်ကွဲ (မသေချာ): na jahatīti၊ ရှေ့ အမေးတို့နှင့် နှိုင်းယှဉ်ရမည်]
- [na jahatīti (?) purimañhehi saṃsandetabbaṃ] = [ပါဌ်ကွဲ (မသေချာ): na jahatīti၊ ရှေ့ အမေးတို့နှင့် နှိုင်းယှဉ်ရမည်]
- [sadaraṃ (saṃ. ni. 2.64) tadeva yuttataraṃ] = [ပါဌ်ကွဲ (“သံယုတ္တနိကာယ်” 2.64): sadaraṃ၊ ထိုပါဌ်ကပင် ပို၍ သင့်လျော်သည်]
- sāriputto thero = သာရိပုတ္တရာ မထေရ်
- mahāmoggallāno thero = မဟာမောဂ္ဂလ္လာန် မထေရ်
- mahākassapo thero = မဟာကဿပ မထေရ်
- mahākaccāyano thero = မဟာကစ္စာယန မထေရ်
- mahākoṭṭhiko thero = မဟာကောဋ္ဌိက မထေရ်
- mahāpanthako thero = မဟာပန္ထက မထေရ်
- puthujjanabhūmi = ပုထုဇဉ် အဆင့်၌
- catūhi satasahassehi seṭṭhī seṭṭhittaṃ kārento satasahasse parihīne = ငွေ လေးသိန်းဖြင့် သူဌေး အဖြစ်ကို ပြုနေသော သူဌေးသည် ငွေ တစ်သိန်း ဆုတ်ယုတ်သွားသောအခါ
- …bhāvanā (development of …) = …ကို ပွားများခြင်း
- ucchinnamūla tālāvatthukata anabhāvaṅkata āyatiṃ anuppādadhamma = အမြစ်ပြတ်စေပြီး၊ ငုတ်တို ထန်းပင်ကဲ့သို့ ပြုပြီး၊ မရှိတော့အောင် ပြုပြီး၊ နောင်အခါ မဖြစ်ပေါ်တော့သော သဘော ရှိစေပြီး
- ekadesaṃ = တစ်စိတ်တစ်ဒေသ
- chinnassa chediyaṃ = ဖြတ်ပြီးသော အရာ၌ ဖြတ်ဖွယ်
- katassa paticayo = ပြုပြီးသော အရာ၌ ထပ်မံ စုဆောင်းခြင်း
- kammārāmatā = အလုပ်ကို နှစ်သက်ခြင်း
- bhassārāmatā = စကားပြောခြင်းကို နှစ်သက်ခြင်း
- niddārāmatā = အိပ်ခြင်းကို နှစ်သက်ခြင်း
- saṅgaṇikārāmatā = အပေါင်းအသင်းကို နှစ်သက်ခြင်း
- ācinati = စုဆောင်း
- apacinati = ဖြိုဖျက်
- pajahati = ပယ်
- upādiyati = စွဲလမ်း
- visineti = ဖြန့်ကြဲ
- ussineti = စုပုံ
- vidhūpeti = ငြိမ်းစေ
- sandhūpeti = တောက်လောင်စေ
- milakkhesu aviññātāresu yattha natthi gati bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ = ရဟန်းတို့၊ ဘိက္ခုနီတို့၊ ဥပါသကာတို့၊ ဥပါသိကာတို့ သွားလာခြင်း မရှိသော၊ နားမလည်သော မိစ္ဆာ လူမျိုးတို့ နေထိုင်ရာ
- sāvakayuga = တပည့် အစုံ
- idha brahmacariyavāso (sutta) = ဤနေရာ၌ မြင့်မြတ်သော အကျင့်ကို ကျင့်သုံးခြင်း ရှိခြင်း
- ito cutassa tattha upapannassa = ဤလောကမှ သေ၍ ထိုဘုံ၌ ပြန်လည် ဖြစ်ပေါ်သော ထိုသူ၏
- katakaraṇīyo bhāvitabhāvano = ပြုဖွယ် ကိစ္စကို ပြုပြီး၊ ပွားများဖွယ်ကို ပွားများပြီး
- apariññātadukkho appahīnakileso asacchikatanirodho appaṭividdhākuppo = ဒုက္ခကို ပိုင်းခြား မသိရသေး၊ ကိလေသာကို မပယ်ရသေး၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းကို မျက်မှောက် မပြုရသေး၊ မပျက်ယွင်းတတ်သော အရာကို ထိုးထွင်း မသိမြင်ရသေး
- punabbhava = ဘဝသစ်
- yathā migo sallena viddho dūrampi gantvā = မြားဖြင့် ထိုးမိသော သမင်သည် အဝေးသို့ပင် သွားပြီးမှ
- ariyakantehi sīlehi = အရိယာတို့ နှစ်သက်သော သီလတို့နှင့်
- vikkhambheti = ဖိနှိပ်ထား
- accantaṃ = အပြီးအပိုင်
- anavasesaṃ = အကြွင်းမဲ့
- appaṭisandhiyaṃ = ပြန်လည် မဆက်စပ်နိုင်အောင်
- samūlaṃ = အမြစ်နှင့်တကွ
- sataṇhaṃ = တပ်မက်မှုနှင့်တကွ
- sānusayaṃ = ကိန်းအောင်းခြင်းနှင့်တကွ
- ariyena ñāṇena = အရိယာ ဉာဏ်ဖြင့်
- ariyena maggena = အရိယာ မဂ်ဖြင့်
- akuppaṃ paṭivijjhanto = မပျက်ယွင်းတတ်သော အရာကို ထိုးထွင်း သိမြင်လျက်
- anāgāmiphalaṃ sacchikaronto = အနာဂါမိဖိုလ်ကို မျက်မှောက်ပြုလျက်
- sabbaṃ (everything) = အရာအားလုံး
- aniccaṃ adhuvaṃ asassataṃ vipariṇāmadhammaṃ = မမြဲသော၊ မခိုင်ခံ့သော၊ ထာဝရ မတည်မြဲသော၊ ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော
- (Saṃkhittaṃ). = (အကျဉ်းချုပ်)။

- (more, in the tables of the script) thera names: Sāriputta «သာရိပုတ္တရာ», Mahāmoggallāna «မဟာမောဂ္ဂလ္လာန်», Mahākassapa
  «မဟာကဿပ», Mahākaccāyana «မဟာကစ္စာယန», Mahākoṭṭhika «မဟာကောဋ္ဌိက», Mahāpanthaka «မဟာပန္ထက», thera «မထေရ်»;
  āvaraṇa «အဟန့်အတား» (kept apart from nīvaraṇa); sāvakayuga «တပည့် အစုံ»; aveccappasāda «ခိုင်မြဲသော ကြည်ညိုမှု»;
  ariyakanta sīla «အရိယာတို့ နှစ်သက်သော သီလ»; nandī «ပျော်မွေ့မှု»; vuddhi «ကြီးထွားခြင်း»; upacaya «တိုးပွားခြင်း»;
  virūḷha «စည်ပင်»; avakkanti «သက်ဆင်းခြင်း»; saṅkhā / samaññā «ရေတွက်ခေါ်ဆိုချက် / အမည်ပေးချက်»; rājā cakkavattī
  «စကြဝတေး မင်း» (pi-2); the Arahantādi «sa-X» = «X ရှိသူ», anottappī «ဒုစရိုက်ကို မကြောက်ရွံ့သူ».
- Brackets: BR_TABLE entries for (āmantā) (ka.), no vata re … evamuparipi, mahākaccāno (ma. ni. 1.202 ādayo), paṭipādā
  (aṭṭha.) «(အဋ္ဌကထာ)», mahāva. «“မဟာဝဂ်”», khu. pā. «“ခုဒ္ဒကပါဌ”», aṅguttaranikāye / saṃyuttanikāye «“…”၌», ( ) (?),
  the na jahatīti notes, sadaraṃ … tadeva yuttataraṃ; REF_NOTE suttanipāte «“သုတ္တနိပါတ်”၌».

## Unsure Pāli / interpretation (for the reviewer)
- satasahasse parihīne (^5-239) = «ငွေ တစ်သိန်း ဆုတ်ယုတ်သွားသောအခါ» (kept the parih- verb for consistency).
- anusahagata = «အနည်းငယ်မျှ ကျန်ရှိသော» (residual); visineti / ussineti / vidhūpeti / sandhūpeti (^5-268) =
  «ဖြန့်ကြဲ / စုပုံ / ငြိမ်းစေ / တောက်လောင်စေ» (best guesses).
- «Ayoganti katvā sabbamatthi» = «မဆက်စပ်ဟု မှတ်ယူ၍ …» (as the English zero-shot: "taking it as not joined").
- «sabbena sabbaṃ» = «အပြည့်အဝ»; nvatthi / nvātītaṃ read as negatives (as the English zero-shot).
- The verse lines (Uccāvacā …, Chaccābhiṭhānāni = «ကြီးလေးသော ဒုစရိုက် ခြောက်ပါး», Nirāmagandhā = «ကိလေသာ အပုပ်နံ့ ကင်း»
  with a clarifying «ကိလေသာ»), ukkalā vassabhaññā = «ဥက္ကလ ဇနပုဒ်သား … ဝဿနှင့် ဘည».
- Compound questions follow the approved convention (non-final parts as statements, «…ဟူ၍၊» after «ti»), e.g. ^5-267
  «Atthi arahato bhassārāmatā, atthi …?» and the na-ca ñāṇa list (^5-290), where one «na» covers four verbs: rendered
  with one negative over a nominal list «…ခြင်းကို မပြုသလော» so that the polarity stays one per Pāli «na».

## Source slips (translated as written; Pāli not changed)
- ^5-270 «Āmantā?» (with «?»): rendered «ဟုတ်ပါသည်။».
- ^5-274 «…ariyakantehi sīlehi samannāgato ekadesaṃ …» (no comma; ^5-274 line 4 has it): rendered with «၊».
- ^5-279 «so ca na accantaṃ jahati» etc. as written; ^5-292 «…atītaṃ anottappaṃ atthi puthujjano tena …» (no comma):
  «၊» supplied.
- ^5-294 «Atīto sammāsammuddho» (for sammāsambuddho): rendered as sammāsambuddho.
- ^5-295 «Paccuppannaṃ atthīti, āmantā.» (comma, small letter): one sentence «…ရှိသလော၊ ဟုတ်ပါသည်။»; «tena
  paccuppannaṃ, no paccuppannaṃ» (comma) = the claim's wording; ^5-295 lines without commas («atthi atthi siyā …
  siyā nvānāgataṃ») as written; «panānāgataṃ» = pana anāgataṃ.
- ^5-296 «natthi nu kho so, phagguna, mano» (nu in the Buddha's answer): rendered as a plain negative.
- ^5-287 «purimañhehi» (for purimapañhehi) in a variant note: same Burmese as the correct one.
- ^5-266 «Evaṃ rūpā rasā …» ends with «.» mid-stanza: Burmese «၊».
- Pāli spellings kept in their own keys: pisuṇavācā / pisuṇāvācā (^5-269), mahākoṭṭhiko, idha parinibbāyipuggalo.
