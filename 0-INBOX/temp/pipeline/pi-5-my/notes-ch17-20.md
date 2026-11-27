# pi-5 Burmese zero-shot, chapters 17-20: notes (17-navamavaggo, 18-dasamavaggo, 19-ekadasamavaggo, 20-dvadasamavaggo)

Status: DONE 2026-11-20 (not committed). Brief: burmese-zeroshot-brief.md. Source rule kept: translated from the Pāli only;
no Burmese translation / nissaya opened, 0-INBOX/temp/language-priority/ not opened, no web search. English pi-5
zero-shot (same files, headings and a few sentences) read for meaning only. pi-1 … pi-4 read only through their FINAL
rails texts (kwic5.py / my5_formulas.FINAL); every reused value is witnessed (W) at import.

## Files and run
- Output: AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/17-navamavaggo.md (46 segments, 103 lines),
  18-dasamavaggo.md (56 segments, 103 lines), 19-ekadasamavaggo.md (41 segments, 86 lines), 20-dvadasamavaggo.md
  (44 segments, 79 lines).
- make_ch17-20.py: imports make_ch11-12.py READ ONLY (which imports make_ch6-10.py -> make_sample.py -> my5_formulas.py);
  extends PROP / SENT / LINES / QUOTE / HEAD / COLO / ANCHOR / VAR_KIND / REF / BR_TABLE / NOTE in memory only.
  Run: python3 -I -X utf8 make_ch17-20.py [chapter] [--misses] [--units] [--look REGEX] (--look = read-only lookup of the
  finished pi-5 chapters); check_ch17-20.py [chapter] [--why].
- New frames (before the generic «P-ti?» / «P-ti.»): «Tena hi P-ti…pe….» (^5-586); «Na hevaṃ vattabbe…pe… "P"ti?» (a
  quotation right after the elision, the line is not cut there: ^5-618/619). Lines cut by hand: ^5-581 (unclosed quote,
  OPEN_Q_X) and ^5-620 (two inner variant brackets, LINE_PARTS).
- Bare fragments for the āyatana names were NOT added (they changed ch8): the sample's bare-noun rule («Xသည်…») is used.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all four (check_marks = pi-4-mr/check_marks.py). My chk-pe copies
  (pi-6-mr/chk-pe/17-… 20-…) deleted; the other files there are not mine.
- check_ch17-20.py: A 4/4 rebuilt identical + A2 the 8 imported chapters (1, 6-12) still rebuild byte-identical with the
  ch17-20 tables installed; B1 371 lines; B2 1243 polarity marks; B2d 1239 negations; B7 299 existence marks; B3 141 number
  words; B4 187 segments; B5 4263/4263 recurring sentences; B6 136 table values; 0 mismatches.
- Reuse test 1063 / 1063 (C1 119/119 topic names, C3 942/942 occurrences of 129 terms, D 2/2 copies of ch2-5 strings).

## Main choices (pi-1 … pi-4 FINAL wording reused, witnessed)
- sārammaṇa / anārammaṇa «အာရုံ ရှိ / မရှိ» (pi-1 ^1-M2-55), as predicate «Xသည် အာရုံ ရှိ(သည်)»; cetasika / acetasika
  «စိတ်၏ အဖော် ဖြစ် / မဟုတ်» (pi-1); cittasampayutta / -vippayutta «စိတ်နှင့် ယှဉ်တွဲသော / ကင်းကွာသော အရာ»;
  cittānuparivatti «စိတ်နောက်သို့ လိုက်ပါသော အရာ»; cittasamuṭṭhāna «စိတ်မှ ဖြစ်ပေါ်လာသော» (all pi-1 dyads).
- āvaṭṭanā ābhogo samannāhāro manasikāro (pi-2 ^2-766) + cetanā (ch8), patthanā (pi-1), paṇidhi «ဆုတောင်းမှု» (ch11 verse).
- The five consciousnesses passage: pi-2 ^2-751 lines (2)-(13) verbatim (uppannavatthukā … anābhogā); «cakkhuñca paṭicca
  rūpe ca uppajjati cakkhuviññāṇaṃ» pi-2 ^2-184; sense-restraint sutta pi-1 ^1-1354 (nimittaggāhī, the five senses,
  manasā dhammaṃ viññāya); the seven anusaya pi-2 ^2-949; kāma / avijjā / paṭigha … clusters pi-1 ^1-1118 / ^1-1158 and
  the avijjā list of pi-1; abyākata, kiriyā «ပြုရုံမျှသာ ဖြစ်သော» (pi-1 ^1-567); kusalākusala / sāvajjānavajja /
  hīnapaṇīta / kaṇhasukkasappaṭibhāga pi-4 ^4-104; five precepts pi-2 ^2-703; three akusala vitakka pi-2 ^2-910;
  viññatti pi-1 ^1-U1 (aviññatti «ထုတ်ဖော်ပြသမှု မဟုတ်သော အရာ»); dussīla / dussīlya pi-1 / pi-2; kāya- / vacī- /
  manokamma pi-1 ^1-985 and pi-2 ^2-751 («ကိုယ်ဖြင့် ပြုသော ကံ» …, so cakkhukamma «မျက်စိဖြင့် ပြုသော ကံ»);
  diṭṭhisampanno puggalo «အယူ ပြည့်စုံသော ပုဂ္ဂိုလ်» and «… အသက်မှ သတ်ရာ / သံဃာကို ခွဲရာ» pi-2 ^2-809; the five
  ānantariya passives pi-2 ^2-U55 («အမိသည် အသက်မှ ချခံရ» …, the same as make_ch21-25); niraya / tiracchānayoni /
  pettivisaya pi-2 ^2-809 / ^2-811; niyata «ကျိန်းသေ» (pi-1 ^1-M1-15); sattakkhattuparama / kolaṅkola / ekabījī pi-4;
  maggasamaṅgī «မဂ်နှင့် ပြည့်စုံသူ» (pi-1 ^1-1373), so -samaṅgī = «…နှင့် ပြည့်စုံသူ / ပြည့်စုံသော».
- From the earlier pi-5 chapters (imported): rāgaṭṭhāniya … lists (ch10), sotaviññeyya … (ch10), ārabbha «ကို
  အာရုံပြု၍» (ch8), Mātikā adjectives (ch11), saṃvara / asaṃvara (ch11), pahīyanti «ပယ်ခံရကြ» (ch12), upapattesiya (ch12),
  the āpāyika acts list (ch12 gihi table), samannāgata «ပြည့်စုံ» (ch12), amata «အမြိုက်» (ch12 verse), the regress
  «natthi vaṭṭupacchedo / anupādāparinibbānaṃ» (sample), ch5 strings for niruddhaṃ vigataṃ … / ajātaṃ abhūtaṃ … (copied,
  check D verifies them in the ch5 output).

## New recurring terms and phrases (Pāli = Burmese; the NEW table of make_ch17-20.py)
- āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi = စိတ်ကို လှည့်ဆောင်ခြင်း၊ စိတ်ညွတ်ခြင်း၊ စိတ်ကို ဆောင်ခြင်း၊ နှလုံးသွင်းခြင်း၊ စေ့ဆော်မှု၊ တောင့်တခြင်း၊ ဆုတောင်းမှု
- katamakkhandhapariyāpanno? saṅkhārakkhandhapariyāpanno = အဘယ် အစုအဝေး၌ အကျုံးဝင်သနည်း / ပြုပြင်ဖန်တီးမှု အစုအဝေး၌ အကျုံးဝင်သည်
- X ekadeso sārammaṇo ekadeso anārammaṇo = X၏ တစ်စိတ်တစ်ဒေသသည် အာရုံ ရှိ၍ တစ်စိတ်တစ်ဒေသသည် အာရုံ မရှိ
- Navamavaggo = နဝမ ဝဂ်
- ānisaṃsadassāvī = အကျိုးကျေးဇူးကို ရှုမြင်သူ
- (84) 1. Ānisaṃsadassāvīkathā = (84) 1. အကျိုးကျေးဇူးကို ရှုမြင်သူအကြောင်း ဆွေးနွေးချက်
- Ānisaṃsadassāvīkathā = အကျိုးကျေးဇူးကို ရှုမြင်သူအကြောင်း ဆွေးနွေးချက်
- ānisaṃsadassāvissa saṃyojanānaṃ pahānaṃ = အကျိုးကျေးဇူးကို ရှုမြင်သူ၏ နှောင်ကြိုးတို့ကို ပယ်ခြင်း ဖြစ်
- aniccato … vipariṇāmadhammato (the 26 aspects) = မမြဲဟု၊ ဆင်းရဲဟု၊ ရောဂါဟု၊ အနာဟု၊ ငြောင့်ဟု၊ ဒုက္ခ ဖိစီးမှုဟု၊ ဖျားနာမှုဟု၊ သူစိမ်းဟု၊ ပျက်စီးတတ်သော အရာဟု၊ ဘေးဒဏ်ဟု၊ ဥပဒ်ဟု၊ ကြောက်ဖွယ်ဟု၊ ဘေးအန္တရာယ်ဟု၊ လှုပ်ရှားတတ်သော အရာဟု၊ ပြိုပျက်တတ်သော အရာဟု၊ မခိုင်မြဲသော အရာဟု၊ ကာကွယ်ရာ မဟုတ်ဟု၊ ပုန်းအောင်းရာ မဟုတ်ဟု၊ ကိုးကွယ်ရာ မဟုတ်ဟု၊ ကိုးကွယ်ရာ မဖြစ်သော အရာဟု၊ ဗလာဟု၊ အနှစ်မဲ့ဟု၊ ဆိတ်သုဉ်းဟု၊ အတ္တ မဟုတ်ဟု၊ အပြစ်ဟု၊ ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘောဟု
- idha, bhikkhave, bhikkhu = ရဟန်းတို့၊ ဤသာသနာ၌ ရဟန်းသည်
- (85) 2. Amatārammaṇakathā = (85) 2. အမြိုက်ကို အာရုံပြုခြင်းအကြောင်း ဆွေးနွေးချက်
- Amatārammaṇakathā = အမြိုက်ကို အာရုံပြုခြင်းအကြောင်း ဆွေးနွေးချက်
- amatārammaṇaṃ saṃyojanaṃ = နှောင်ကြိုးသည် အမြိုက်ကို အာရုံပြု
- maññati (conceives) = ထင်မှတ်
- (86) 3. Rūpaṃ sārammaṇantikathā = (86) 3. ရုပ်သည် အာရုံ ရှိသည်ဟူသော ဆွေးနွေးချက်
- Rūpaṃ sārammaṇantikathā = ရုပ်သည် အာရုံ ရှိသည်ဟူသော ဆွေးနွေးချက်
- (87) 4. Anusayā anārammaṇakathā = (87) 4. ကိန်းအောင်းခြင်းတို့သည် အာရုံ မရှိဟူသော ဆွေးနွေးချက်
- Anusayā anārammaṇātikathā = ကိန်းအောင်းခြင်းတို့သည် အာရုံ မရှိဟူသော ဆွေးနွေးချက်
- kusalābyākate citte vattamāne = ကုသိုလ်စိတ်နှင့် ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော စိတ် ဖြစ်နေစဉ်
- (88) 5. Ñāṇaṃ anārammaṇantikathā = (88) 5. ဉာဏ်သည် အာရုံ မရှိဟူသော ဆွေးနွေးချက်
- Ñāṇaṃ anārammaṇantikathā = ဉာဏ်သည် အာရုံ မရှိဟူသော ဆွေးနွေးချက်
- (89) 6. Atītānāgatārammaṇakathā = (89) 6. အတိတ်နှင့် အနာဂတ်ကို အာရုံပြုခြင်းအကြောင်း ဆွေးနွေးချက်
- Atītānāgatārammaṇakathā = အတိတ်နှင့် အနာဂတ်ကို အာရုံပြုခြင်းအကြောင်း ဆွေးနွေးချက်
- (90) 7. Vitakkānupatitakathā = (90) 7. စတင်ကြံစည်မှုနှင့် တွဲဖက်နေခြင်းအကြောင်း ဆွေးနွေးချက်
- Vitakkānupatitakathā = စတင်ကြံစည်မှုနှင့် တွဲဖက်နေခြင်းအကြောင်း ဆွေးနွေးချက်
- X-anupatita = Xနှင့် တွဲဖက်နေ
- vitakkavipphāro saddo = စတင်ကြံစည်မှု ပျံ့နှံ့ခြင်းဟူသော အသံ
- (91) 8. Vitakkavipphārasaddakathā = (91) 8. စတင်ကြံစည်မှု ပျံ့နှံ့ခြင်းဟူသော အသံအကြောင်း ဆွေးနွေးချက်
- Vitakkavipphārasaddakathā = စတင်ကြံစည်မှု ပျံ့နှံ့ခြင်းဟူသော အသံအကြောင်း ဆွေးနွေးချက်
- (92) 9. Na yathācittassa vācātikathā = (92) 9. စကားသည် စိတ်အတိုင်း မဟုတ်ဟူသော ဆွေးနွေးချက်
- Na yathācittassa vācātikathā = စကားသည် စိတ်အတိုင်း မဟုတ်ဟူသော ဆွေးနွေးချက်
- (93) 10. Na yathācittassa kāyakammantikathā = (93) 10. ကိုယ်ဖြင့် ပြုသော ကံသည် စိတ်အတိုင်း မဟုတ်ဟူသော ဆွေးနွေးချက်
- Na yathācittassa kāyakammantikathā = ကိုယ်ဖြင့် ပြုသော ကံသည် စိတ်အတိုင်း မဟုတ်ဟူသော ဆွေးနွေးချက်
- na yathācittassa X = Xသည် စိတ်အတိုင်း မဟုတ်
- cittena saha ekuppāda = စိတ်နှင့် တစ်ပြိုင်နက် ဖြစ်ပေါ်သော
- na X-tukāmo X-ti (does X without wishing to) = X မလိုဘဲ X
- aññaṃ X-issāmīti aññaṃ X-ti = «တစ်ခုကို Xမည်»ဟု ကြံ၍ အခြား တစ်ခုကို X
- atītānāgatehi (samannāgato) = အတိတ်၊ အနာဂတ်တို့
- (94) 11. Atītānāgatasamannāgatakathā = (94) 11. အတိတ်၊ အနာဂတ်တို့နှင့် ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- Atītānāgatasamannāgatakathā = အတိတ်၊ အနာဂတ်တို့နှင့် ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- aṭṭhavimokkhajhāyī catunnaṃ jhānānaṃ nikāmalābhī navannaṃ anupubbavihārasamāpattīnaṃ lābhī = လွတ်မြောက်ခြင်း ရှစ်ပါးဖြင့် ဈာန်ဝင်သူ၊ ဈာန် လေးပါးကို အလိုရှိတိုင်း ရသူ၊ အစဉ်အတိုင်း နေထိုင်ရာ ဈာန် ဝင်စားရာ ကိုးပါးကို ရသူ
- tatheva (uddāna) = ထိုနည်းတူပင်
- Dasamavaggo = ဒသမ ဝဂ်
- (95) 1. Nirodhakathā = (95) 1. ချုပ်ငြိမ်းခြင်းအကြောင်း ဆွေးနွေးချက်
- Nirodhakathā = ချုပ်ငြိမ်းခြင်းအကြောင်း ဆွေးနွေးချက်
- upapattesiye pañcakkhandhe aniruddhe / niruddhe = ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော အစုအဝေး ငါးပါး မချုပ်ငြိမ်းသေးမီ / ချုပ်ငြိမ်းပြီးသောအခါ
- sammukhībhāvaṃ āgacchanti = မျက်မှောက်သို့ ရောက်လာကြ
- (96) 2. Rūpaṃ maggotikathā = (96) 2. ရုပ်သည် မဂ် ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Rūpaṃ maggotikathā = ရုပ်သည် မဂ် ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- X-ti – attheva suttantoti? = “X” – ထိုသို့သော သုတ္တန် အမှန်ပင် ရှိသလော
- (97) 3. Pañcaviññāṇasamaṅgissa maggakathā = (97) 3. သိစိတ် ငါးပါးနှင့် ပြည့်စုံသူ၏ မဂ်အကြောင်း ဆွေးနွေးချက်
- Pañcaviññāṇasamaṅgissa maggakathā = သိစိတ် ငါးပါးနှင့် ပြည့်စုံသူ၏ မဂ်အကြောင်း ဆွေးနွေးချက်
- (98) 4. Pañcaviññāṇā kusalāpi akusalāpītikathā = (98) 4. သိစိတ် ငါးပါးသည် ကုသိုလ်လည်း ဖြစ်ကြ၍ အကုသိုလ်လည်း ဖြစ်ကြသည်ဟူသော ဆွေးနွေးချက်
- Pañcaviññāṇā kusalāpi akusalāpītikathā = သိစိတ် ငါးပါးသည် ကုသိုလ်လည်း ဖြစ်ကြ၍ အကုသိုလ်လည်း ဖြစ်ကြသည်ဟူသော ဆွေးနွေးချက်
- (99) 5. Sābhogātikathā = (99) 5. စိတ်ညွတ်ခြင်း ရှိကြသည်ဟူသော ဆွေးနွေးချက်
- Sābhogātikathā = စိတ်ညွတ်ခြင်း ရှိကြသည်ဟူသော ဆွေးနွေးချက်
- (100) 6. Dvīhisīlehikathā = (100) 6. သီလ နှစ်ပါးနှင့် ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- Dvīhisīlehikathā = သီလ နှစ်ပါးနှင့် ပြည့်စုံခြင်းအကြောင်း ဆွေးနွေးချက်
- (101) 7. Sīlaṃ acetasikantikathā = (101) 7. သီလသည် စိတ်၏ အဖော် မဟုတ်ဟူသော ဆွေးနွေးချက်
- Sīlaṃ acetasikantikathā = သီလသည် စိတ်၏ အဖော် မဟုတ်ဟူသော ဆွေးနွေးချက်
- (102) 8. Sīlaṃ na cittānuparivattītikathā = (102) 8. သီလသည် စိတ်နောက်သို့ လိုက်ပါသော အရာ မဟုတ်ဟူသော ဆွေးနွေးချက်
- Sīlaṃ na cittānuparivattītikathā = သီလသည် စိတ်နောက်သို့ လိုက်ပါသော အရာ မဟုတ်ဟူသော ဆွေးနွေးချက်
- (103) 9. Samādānahetukathā = (103) 9. ဆောက်တည်ခြင်းကြောင့် ဖြစ်သော သီလအကြောင်း ဆွေးနွေးချက်
- Samādānahetukathā = ဆောက်တည်ခြင်းကြောင့် ဖြစ်သော သီလအကြောင်း ဆွေးနွေးချက်
- (104) 10. Viññatti sīlantikathā = (104) 10. ထုတ်ဖော်ပြသမှုသည် သီလ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Viññatti sīlantikathā = ထုတ်ဖော်ပြသမှုသည် သီလ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- (105) 11. Aviññatti dussilyantikathā = (105) 11. ထုတ်ဖော်ပြသမှု မဟုတ်သော အရာသည် သီလ ပျက်ခြင်း ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Aviññatti dussilyantikathā = ထုတ်ဖော်ပြသမှု မဟုတ်သော အရာသည် သီလ ပျက်ခြင်း ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- paṇṇāsako (a set of fifty) = ငါးဆယ်အစု
- ekādasama (11th) = ဧကာဒသမ
- Ekādasamavaggo = ဧကာဒသမ ဝဂ်
- (106-108) 1-3. Tissopi anusayakathā = (106-108) 1-3. ကိန်းအောင်းခြင်းအကြောင်း ဆွေးနွေးချက် သုံးရပ်လုံး
- Tissopi anusayakathā = ကိန်းအောင်းခြင်းအကြောင်း ဆွေးနွေးချက် သုံးရပ်လုံး
- (109) 4. Ñāṇakathā = (109) 4. ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- Ñāṇakathā = ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- X-e vigate = X ကင်းသွားသောအခါ
- (110) 5. Ñāṇaṃ cittavippayuttantikathā = (110) 5. ဉာဏ်သည် စိတ်နှင့် ကင်းကွာသော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Ñāṇaṃ cittavippayuttantikathā = ဉာဏ်သည် စိတ်နှင့် ကင်းကွာသော အရာ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- (111) 6. Idaṃ dukkhantikathā = (111) 6. “ဤကား ဒုက္ခ”ဟူသော ဆွေးနွေးချက်
- Idaṃ dukkhantikathā = “ဤကား ဒုက္ခ”ဟူသော ဆွေးနွေးချက်
- I-ti ca da-nti ca du-ti ca kha-nti ca (the syllables) = “ဣ”ဟူ၍လည်း “ဒံ”ဟူ၍လည်း “ဒု”ဟူ၍လည်း “ခ”ဟူ၍လည်း
- (112) 7. Iddhibalakathā = (112) 7. ဣဒ္ဓိ စွမ်းအားအကြောင်း ဆွေးနွေးချက်
- Iddhibalakathā = ဣဒ္ဓိ စွမ်းအားအကြောင်း ဆွေးနွေးချက်
- iddhibalena samannāgato kappaṃ tiṭṭheyya = ဣဒ္ဓိ စွမ်းအားနှင့် ပြည့်စုံသူသည် ကမ္ဘာ ပတ်လုံး တည်နေရာ
- (113) 8. Samādhikathā = (113) 8. သမာဓိအကြောင်း ဆွေးနွေးချက်
- Samādhikathā = သမာဓိအကြောင်း ဆွေးနွေးချက်
- (114) 9. Dhammaṭṭhitatākathā = (114) 9. သဘောတရားတို့၏ တည်နေခြင်း သဘောအကြောင်း ဆွေးနွေးချက်
- Dhammaṭṭhitatākathā = သဘောတရားတို့၏ တည်နေခြင်း သဘောအကြောင်း ဆွေးနွေးချက်
- (115) 10. Aniccatākathā = (115) 10. မမြဲခြင်း သဘောအကြောင်း ဆွေးနွေးချက်
- Aniccatākathā = မမြဲခြင်း သဘောအကြောင်း ဆွေးနွေးချက်
- parinipphanna = ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော အရာ
- dvādasama (12th) = ဒွါဒသမ
- Dvādasamavaggo = ဒွါဒသမ ဝဂ်
- (116) 1. Saṃvaro kammantikathā = (116) 1. စောင့်စည်းမှုသည် ကံ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Saṃvaro kammantikathā = စောင့်စည်းမှုသည် ကံ ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- (117) 2. Kammakathā = (117) 2. ကံအကြောင်း ဆွေးနွေးချက်
- Kammakathā = ကံအကြောင်း ဆွေးနွေးချက်
- (118) 3. Saddo vipākotikathā = (118) 3. အသံသည် ကံ၏ အကျိုး ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- Saddo vipākotikathā = အသံသည် ကံ၏ အကျိုး ဖြစ်သည်ဟူသော ဆွေးနွေးချက်
- (119) 4. Saḷāyatanakathā = (119) 4. အာရုံခံ နယ်ပယ် ခြောက်ပါးအကြောင်း ဆွေးနွေးချက်
- Saḷāyatanakathā = အာရုံခံ နယ်ပယ် ခြောက်ပါးအကြောင်း ဆွေးနွေးချက်
- (120) 5. Sattakkhattuparamakathā = (120) 5. အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူအကြောင်း ဆွေးနွေးချက်
- Sattakkhattuparamakathā = အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူအကြောင်း ဆွေးနွေးချက်
- (121) 6. Kolaṅkolakathā = (121) 6. အမျိုးမှ အမျိုးသို့ ကူးသူအကြောင်း ဆွေးနွေးချက်
- Kolaṅkolakathā = အမျိုးမှ အမျိုးသို့ ကူးသူအကြောင်း ဆွေးနွေးချက်
- (122) 7. Ekabījīkathā = (122) 7. မျိုးစေ့ တစ်စေ့သာ ရှိသူအကြောင်း ဆွေးနွေးချက်
- Ekabījīkathā = မျိုးစေ့ တစ်စေ့သာ ရှိသူအကြောင်း ဆွေးနွေးချက်
- X puggalo X-tāniyato = X ဖြစ်သော ပုဂ္ဂိုလ်သည် X၏ အဖြစ်၌ ကျိန်းသေသူ ဖြစ်
- (123) 8. Jīvitā voropanakathā = (123) 8. အသက်မှ သတ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Jīvitā voropanakathā = အသက်မှ သတ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- (124) 9. Duggatikathā = (124) 9. ဆိုးသော လားရာအကြောင်း ဆွေးနွေးချက်
- Duggatikathā = ဆိုးသော လားရာအကြောင်း ဆွေးနွေးချက်
- sattamabhaviko puggalo = ခုနစ်ကြိမ်မြောက် ဘဝ၌ ရှိသော ပုဂ္ဂိုလ်
- (125) 10. Sattamabhavikakathā = (125) 10. ခုနစ်ကြိမ်မြောက် ဘဝ၌ ရှိသော ပုဂ္ဂိုလ်အကြောင်း ဆွေးနွေးချက်
- Sattamabhavikakathā = ခုနစ်ကြိမ်မြောက် ဘဝ၌ ရှိသော ပုဂ္ဂိုလ်အကြောင်း ဆွေးနွေးချက်
- (not in NEW, inline) aniccatā = မမြဲခြင်း သဘော; ṭhitatā = တည်နေခြင်း သဘော; cittasantati = စိတ်အစဉ်; ekacittakkhaṇiko
  samādhi = သမာဓိသည် စိတ် တစ်ခဏ၌သာ ဖြစ်သော အရာ; samāpanno = ဝင်စားနေသူ; pavattati (ñāṇaṃ) = ဖြစ်ပွား; vācaṃ bhāsato =
  …ဟု စကား ပြောနေသူ၌; iddhibala = ဣဒ္ဓိ စွမ်းအား; kappa = ကမ္ဘာ (… ပတ်လုံး တည်နေရာ); labbhā iddhiyā paggahetuṃ = …ဟု
  ဣဒ္ဓိဖြင့် ထိန်းထားနိုင်; mā X = မ…ပါစေနှင့်; uppanna = ဖြစ်ပေါ်ပြီးသော; niyama = ကျိန်းသေမှု; sañcicca = ရည်ရွယ်၍;
  sagāravo / agāravo = ရိုသေသူ / မရိုသေသူ; āpāyika = အပါယ်နှင့် ဆိုင်သော; iṭṭhaphala = လိုလားအပ်သော အကျိုး ရှိသော;
  saphala savipāka / aphala avipāka = အကျိုး ရှိသော၊ အကျိုး ပေးသော / အကျိုး မရှိသော၊ အကျိုး မပေးသော; samādānahetuka =
  ဆောက်တည်ခြင်းကြောင့် ဖြစ်သော; vaḍḍhati = တိုးပွား; vipāko (predicate) = ကံ၏ အကျိုး; -vedaniya = …ခံစားမှုကို
  ဖြစ်စေတတ်သော; saḷāyatana = အာရုံခံ နယ်ပယ် ခြောက်ပါး; maggabhāvanā = မဂ်ကို ပွားများခြင်း; kiriyā (functional) =
  ပြုရုံမျှသာ ဖြစ်သော; sabbaso = အခါခပ်သိမ်း.

## For the consistency pass
- «"sānusayo"ti / "sarāgo"ti vattabbo» and «arahā cakkhuviññāṇasamaṅgī "ñāṇī"ti / "paññavā"ti vattabbo»: quoted in ch19
  (^5-606/608/613, ^5-617), unquoted in ch17 (^5-556, ^5-558); one key, so the ch17 lines also get the marks (as ch12 did
  for «sotāpannoti vattabbo»).
- dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hoti: «တွေ့ထိမှု နှစ်ပါး… စိတ် နှစ်ပါးတို့၏ ပေါင်းဆုံခြင်း» (ch11 full
  form «တွေ့ထိမှု နှစ်ပါး၊ စိတ် နှစ်ပါးတို့၏ ပေါင်းဆုံခြင်း»); ch13-16 may have its own elided form.
- The paṇṇāsaka uddāna (^5-604) names the first kathās of vaggas 6-10: «သေချာသော လမ်းကြောင်း (Niyāma, ch14 heading)၊
  စုစည်းခြင်း (Saṅgahita, ch15: check the ch15 heading)၊ လားရာ (Chagati, ch16)၊ အကျိုးကျေးဇူး (Ānisaṃsa)၊ ချုပ်ငြိမ်းခြင်း».
- Dutiyo paṇṇāsako «ဒုတိယ ငါးဆယ်အစု» (ch13-16 «Mahāpaṇṇāsako = ကြီးမားသော ငါးဆယ်အစု»).
- ordinals 11 / 12 «ဧကာဒသမ / ဒွါဒသမ» (my5_formulas ORD_MY stops at 10): later vaggas need the same series.
- tassa tasseva / tāya tāyeva natthi dukkhassantakiriyā «ထိုထိုအရာ၏ပင် …» (sample «tassa tasseva natthi dukkhassa
  antakiriyā» of persons = «ထိုထိုသူ၏ပင် …»).
- paññatta (sikkhāpada) «သတ်မှတ်ထားသော» (reuse test: paññatti = «သတ်မှတ်»), not «ပညတ်».

## Unsure Pāli / interpretation
- ānisaṃsadassāvī «အကျိုးကျေးဇူးကို ရှုမြင်သူ»; the 26 aspects (aniccato … vipariṇāmadhammato) are plain renderings
  (agha «ဒုက္ခ ဖိစီးမှု», ābādha «ဖျားနာမှု», para «သူစိမ်း», īti «ဘေးဒဏ်», upasagga «ဘေးအန္တရာယ်»; anatta «အတ္တ မဟုတ်»).
- vitakkavipphāro saddo «စတင်ကြံစည်မှု ပျံ့နှံ့ခြင်းဟူသော အသံ» (vipphāra = outflow); sabbaso «အခါခပ်သိမ်း» (English
  "in every case"); -anupatita «…နှင့် တွဲဖက်နေ».
- na yathācittassa vācā «စကားသည် စိတ်အတိုင်း မဟုတ်»; «na bhaṇitukāmo bhaṇati» «မပြောလိုဘဲ ပြော»; katheti «ပြောဆို»
  (not «ဆို», which the B2d counter cannot tell from «ဆိုသင့်»).
- aṭṭhavimokkhajhāyī «လွတ်မြောက်ခြင်း ရှစ်ပါးဖြင့် ဈာန်ဝင်သူ»; nikāmalābhī «အလိုရှိတိုင်း ရသူ».
- parinipphanna «ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော အရာ»; ṭhitatā «တည်နေခြင်း သဘော»; Iddhimayiko so āyu «ထိုသက်တမ်းသည် ဣဒ္ဓိဖြင့်
  ဖြစ်သော အရာ».
- sati / asati jīvite jīvitāvasese «အသက်နှင့် အသက်၏ အကြွင်း ရှိနေစဉ် / မရှိနေစဉ်»; the alternative question
  (^5-621) rendered «… တည်နေရာသလော၊ သို့မဟုတ် … တည်နေရာသလော».
- ^5-624 sutta: pāṭibhogo «အာမခံနိုင်သူ», sadarāni «ပူပန်ဖွယ် ရှိသော», ponobbhavikāni «ဘဝသစ်ကို ဖြစ်စေတတ်သော»; «yāni … tesaṃ
  vipāko» «… ယုတ်မာသော ကံ မှန်သမျှ၊ ထိုကံတို့၏ အကျိုးကို …».
- ^5-635 sutta «upapajje vā apare vā pariyāye» «နောက်ဘဝ၌ဖြစ်စေ၊ ထို့နောက် အခြား ဘဝ အလှည့်၌ဖြစ်စေ»; byantibhāva «ကုန်ဆုံးခြင်း».
- ^5-637 brahmassaro karavikabhāṇī «ဗြဟ္မာ၏ အသံကဲ့သို့ အသံ ရှိသူ၊ ကရဝိက်ငှက်ကဲ့သို့ ပြောဆိုသူ».
- apabyāmato kareyya «လက်ဝဲ ထား၍ ပြုရာ» (pass keeping it on the left, disrespect); ohadeyya omutteyya niṭṭhubheyya
  «ကျင်ကြီး စွန့်ရာ၊ ကျင်ငယ် စွန့်ရာ၊ တံတွေး ထွေးရာ».
- «na ca arahā āpāyike sadde… paṭiggaṇheyya» (^5-651): the one Pāli «na» = one «မ» on the last verb (ch10's rule negates every
  act; not used here).
- «Sakadāgāminiyamenāti?» «သကဒါဂါမ်၏ ကျိန်းသေမှုဖြင့်လော။» (bare instrumental question).
- Syllable joke ^5-620 «"I"ti ca "da"nti ca "du"ti ca "kha"nti ca» in Burmese letters «ဣ / ဒံ / ဒု / ခ».
- [sakavādīpucchā viya dissati] «[မိမိဘက်၏ အမေးကဲ့သို့ ထင်ရသည်]»; ^5-652 note translated in full.

## Source slips (translated as written; Pāli not changed)
- ^5-581 «Cakkhuñca paṭicca suññatañca uppajjati cakkhuviññāṇa"nti – attheva suttantoti?» lacks the opening quote: the line is
  cut by hand (OPEN_Q_X) and the regular marks are used; the same line has «Na hevaṃ vattabbe.» without «…pe…».
- ^5-585 «Natthi…pe… "cakkhuñca …"» (an elision after the answer): «မရှိပါ… “…” – … ရှိသလော။».
- ^5-612 «avijjāsaṅkhārakkhandhapariyāpannā» (no space): the same Burmese as «avijjā saṅkhārakkhandhapariyāpannā».
- ^5-610/611 «Vedanākkhandho saññākkhandho cittavippayutto» (only two khandhas): as written.
- ^5-619 last «na ca "dukkha"nti» (for «idaṃ dukkha»): «“ဒုက္ခ”ဟု».
- ^5-634 «Hañci apariyāpannā / arūpāvacarā …» (the Hañci clause drops part of the list): as written.
- ^5-653 uddāna «kolaṅkolapuggalo» (one word): as written; ^5-650 variant «[… kapiñjalaṃ …]» keeps its ellipsis.
- ^5-653 (kathā 125) «Na vattabbaṃ "sattamabhavikassa …"ti?» has no dash: «“…”ဟု မဆိုသင့်သလော။» without a dash.
- ^5-576/580/584 «Nanu … nanu pañcaviññāṇā …»: one Burmese «မဟုတ်လော» (B2d counts the two Pāli nanu as one).
- «Na hevaṃ vattabbe.» without «…pe…» in several places (e.g. ^5-581, ^5-594, ^5-597, ^5-612, ^5-613, ^5-617, ^5-628):
  «ဤသို့ မဆိုသင့်ပါ။» as written.
