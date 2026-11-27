# pi-5 Burmese zero-shot, chapters 26-31: notes (26-attharasamavaggo … 31-tevisatimavaggo)

Status: DONE 2026-11-20 (not committed). Brief: burmese-zeroshot-brief.md. Source rule kept: translated from the Pāli only;
no Burmese translation / nissaya opened, 0-INBOX/temp/language-priority/ not opened, no web search. English pi-5 zero-shot
(30-bavisatimavaggo ^5-894, 31-tevisatimavaggo first kathās) read for meaning only. pi-1 … pi-4 read only through their
FINAL rails texts (kwic5.py / my5_formulas.FINAL); every reused value is witnessed (W / F.witness / asserted in FINAL).

## Files and run
- Output: AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/
  26-attharasamavaggo.md (44 segments, 91 lines), 27-ekunavisatimavaggo.md (45 / 81), 28-visatimavaggo.md (33 / 72),
  29-ekavisatimavaggo.md (30 / 54), 30-bavisatimavaggo.md (32 / 56), 31-tevisatimavaggo.md (21 / 44; ends with the
  book colophon «“အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း” ကျမ်း ပြီးဆုံးပြီ။» = F.BOOK_END, pi-1 … pi-3 pattern).
- make_ch26-31.py: imports make_ch11-12.py READ ONLY (which imports make_ch6-10.py, make_sample.py, my5_formulas.py) and
  extends the tables in memory only. P() / S() / Q() / section() keep an earlier chapter's entry when the key is already
  defined or already resolved by an earlier rule (REUSED: 5 keys, e.g. «atthi tassa vitakkavicārā» from ch10, «nibbānaṃ
  asaṅkhataṃ», «dvādasa sotāpattiphalāni»). make_ch2-5.py strings copied verbatim (check D verifies them in ch2-5).
  Run: python3 -I -B -X utf8 make_ch26-31.py [chapter] [--misses] [--units]; check_ch26-31.py [chapter] [--why].

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all six (my chk-pe copies in pi-6-mr/chk-pe deleted).
- check_ch26-31.py (all six): A 6/6 rebuilt identical + A2 the 8 imported chapters (1, 6-12) rebuild byte-identical with
  the ch26-31 tables installed; B1 398 lines; B2 1018 polarity marks; B2d 963 negations; B7 424 existence marks; B3 81
  number words; B4 205 segments; B5 4115/4115 recurring sentences (also against the sample, ch6-10, ch11-12); B6 177
  table values; 0 mismatches. Reuse 663 / 663 (C1 62/62, C3 570/570 occurrences of 104 terms incl. 28 new witnessed
  terms of these chapters, D 31/31 copies of 9 ch2-5 strings).
  Per chapter: ch26 104/104, ch27 234/234, ch28 75/75, ch29 105/105, ch30 81/81, ch31 64/64; each 0 mismatches.
- Check adaptations (check_ch11-12.py copied): Āmantā counted case-insensitively (^5-905 «āmantā»); negators nattheva,
  mā, nopi, nevācināti; new privatives (PRIV) and «မရှိ» words (EXEMPT) of these chapters; NOT_NEG «မယား», «တမလွန်»
  (nouns, not negations); number words dvādasa, nava, caturo; C1 exemption made case-insensitive («Cakkhunā rūpaṃ»
  heading); REUSE regexes narrowed where the Pāli is another word (vessabhū / vessavaṇa, saṅghātaka hell, makkhikā fly,
  -khandhapariyāpanna, pāṇātipātī agent, avipariṇāma-, sakadāgāmi…pe…, indriyesu guttadvāratā = pi-1 «အာရုံခံ အင်္ဂါ»).
- Mutation test: a dropped «မ» (B2d + A) and a changed number word (A) are caught; regenerated afterwards.

## New frames, rules and machinery (all in make_ch26-31.py, inserted before the generic frames)
- «"P"ti – attheva suttantoti?» = «“P”ဟူ၍ – ထိုသို့သော သုတ္တန် အမှန်ပင် ရှိသလော။»; rule «"P"ti – (n)attheva suttanto»
  in conditions = «“P”ဟူ၍ – ထိုသို့သော သုတ္တန် အမှန်ပင် (မ)ရှိလျှင်» (dash kept).
- «"Q"ti – katvā tena ca kāraṇena P-ti?» (^5-852, dash before katvā) = «…ဟု – အကြောင်းပြု၍ ထိုအကြောင်းကြောင့်လည်း …»။
- «"WISH"ti – atthi adhippāyaiddhi buddhānaṃ vā sāvakānaṃ vāti?» = «“WISH”ဟူ၍ – … ဣဒ္ဓိ ရှိသလော။» (wishes = Fixed
  clauses «… ပါစေ» / «မ… ပါစေနှင့်»).
- «Nanu āyasmā sāriputto etadavoca – "Q"ti!» = «အသျှင် သာရိပုတ္တရာသည် ဤသို့ ဆိုခဲ့သည် မဟုတ်လော – “Q”။».
- Classes: NanuPart («X-assa X-tā, nanu X-tā …» = «X ရှိ၏၊ Y မဟုတ်လော» in every form), Fixed (one wording in every
  form), Must (-tabba «… ရမည်» / «… ရမည်လော»).
- SLIP: three lines whose quotes are unbalanced in the source (the cutter cannot cut them) are whole-line LINES entries
  built from their sentence units after install (^5-834, ^5-868 line 2, ^5-877 line 2).
- vagga headings 18-23 = «ဆယ့်ရှစ်ခုမြောက် ဝဂ်» … «နှစ်ဆယ့်သုံးခုမြောက် ဝဂ်» (ORD_MY stops at 10).

## Main choices (pi-1 … pi-4 FINAL wording reused, all witnessed)
- karuṇā / mettā «ကရုဏာ» / «မေတ္တာ» (pi-1); āvaṭṭanā «စိတ်ကို လှည့်ဆောင်ခြင်း» (pi-2 ^2-766); the three samādhis
  (pi-2 ^2-828); sappītika, sukhasahagata, sārammaṇa / anārammaṇa, alobha (pi-1); saññāvedayitanirodha (pi-2 ^2-808);
  kilesa (pi-1 ^1-M2-75); kusalākusala … kaṇhasukkasappaṭibhāga (pi-4 ^4-104); sassata- / ucchedadiṭṭhi (pi-1
  ^1-M2-112); niyata «ကျိန်းသေ» and the micchatta / sammatta / aniyata triad (pi-1 ^1-M1-15); the paññā synonyms
  (pi-1 ^1-16); the eight path factors (pi-1 ^1-277); indriyesu guttadvāratā, bhojane mattaññutā (pi-1); makkha, paḷāsa
  (pi-2 ^2-833); upāyāsa (pi-1 ^1-1343); the ten views (pi-1 ^1-1105); «Idha bhikkhu vivicceva kāmehi…» (pi-2 ^2-487);
  the arūpa bases, the requisites, the deva realms, the path / fruit names, the anicca … vipariṇāmadhamma list (sample);
  the dhammacakka passage built from ch12's parts (_TR, _AS, _EYE5, _ANAN).
- From make_ch2-5.py (copied, check D): jahati «စွန့်ပယ်»; «Katamena maggenāti?» «အဘယ် မဂ်ဖြင့်နည်း။»;
  «Sotāpattimaggenāti?» «သောတာပတ္တိမဂ်ဖြင့်လော။»; the path epithets niyyāniko … asaṃkilesiyo; abhisamaya
  «ထင်ထင်ရှားရှား သိမြင်ခြင်း»; āyasmā «အသျှင်»; anavasesa «အကြွင်းမဲ့».

## New recurring terms and phrases (Pāli = Burmese; the NEW table of make_ch26-31.py plus fixed words)
- Aṭṭhārasamavaggo = ဆယ့်ရှစ်ခုမြောက် ဝဂ်
- Ekūnavīsatimavaggo = ဆယ့်ကိုးခုမြောက် ဝဂ်
- Vīsatimavaggo = နှစ်ဆယ်ခုမြောက် ဝဂ်
- Ekavīsatimavaggo = နှစ်ဆယ့်တစ်ခုမြောက် ဝဂ်
- Bāvīsatimavaggo = နှစ်ဆယ့်နှစ်ခုမြောက် ဝဂ်
- Tevīsatimavaggo = နှစ်ဆယ့်သုံးခုမြောက် ဝဂ်
- buddho bhagavā = ဘုရားရှင် မြတ်စွာဘုရား
- manussaloka = လူ့ပြည်
- (buddho bhagavā manussaloke) aṭṭhāsi = နေတော်မူခဲ့
- Manussalokakathā = လူ့ပြည်အကြောင်း ဆွေးနွေးချက်
- āyusaṅkhāro ossaṭṭho = အသက်ကို ဆက်လက် တည်စေသော ပြုပြင်ဖန်တီးမှုကို စွန့်လွှတ်တော်မူခဲ့
- dhammadesanā = တရား ဟောကြားခြင်း
- Dhammadesanākathā = တရား ဟောကြားခြင်းအကြောင်း ဆွေးနွေးချက်
- abhinimmito (a created figure) = ဖန်ဆင်းထားသော သူ
- Kena desito = အဘယ်သူက ဟောခဲ့သနည်း
- Karuṇākathā = ကရုဏာအကြောင်း ဆွေးနွေးချက်
- akāruṇiko / kāruṇiko = ကရုဏာ မရှိသူ / ကရုဏာ ရှိသူ
- lokahito lokānukampako lokatthacaro = လောက၏ အကျိုးကို လိုလားသူ၊ လောကကို သနားစောင့်ရှောက်သူ၊ လောက၏ အကျိုးအတွက် ကျင့်သူ
- uccārapassāvo = ကျင်ကြီး ကျင်ငယ်
- gandhajāta = နံ့သာ မျိုး
- Gandhajātikathā = နံ့သာ မျိုးအကြောင်း ဆွေးနွေးချက်
- ekena ariyamaggena = အရိယာ မဂ် တစ်ပါးတည်းဖြင့်
- Ekamaggakathā = မဂ် တစ်ပါးတည်းအကြောင်း ဆွေးနွေးချက်
- adiṭṭhaṃ dakkhanti anadhigataṃ adhigacchanti asacchikataṃ sacchikaronti = မမြင်ဖူးသည်ကို မြင်ကြ၊ မရောက်ဖူးသည်ကို ရောက်ကြ၊ မျက်မှောက် မပြုဖူးသည်ကို မျက်မှောက်ပြုကြ
- saṅkamati (passes over) = ကူးပြောင်း
- Jhānasaṅkantikathā = ဈာန် ကူးပြောင်းခြင်းအကြောင်း ဆွေးနွေးချက်
- paṇidhi = စိတ် ဦးတည်ထားခြင်း
- X ādīnavato manasikaroto uppajjati = Xကို အပြစ်အားဖြင့် နှလုံးသွင်းသူ၌ ဖြစ်ပေါ်
- jhānantarikā = ဈာန်တို့အကြား ကာလ
- Jhānantarikakathā = ဈာန်တို့အကြား ကာလအကြောင်း ဆွေးနွေးချက်
- Saddaṃ suṇātītikathā = အသံကို ကြားသည် ဟူသော ဆွေးနွေးချက်
- sotaviññāṇasamaṅgī = နား သိစိတ်နှင့် ပြည့်စုံနေသူ
- manoviññāṇasamaṅgissa = မနော သိစိတ်နှင့် ပြည့်စုံနေသူ၌
- Cakkhunā rūpaṃ passatītikathā = မျက်စိဖြင့် အဆင်းအရောင်ကို မြင်သည် ဟူသော ဆွေးနွေးချက်
- rūpena rūpaṃ passati / paṭivijānāti / phusati = ရုပ်ဖြင့် ရုပ်ကို မြင် / ခွဲခြား သိ / ထိ
- Kilesajahanakathā = ကိလေသာ စွန့်ပယ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- niruddhaṃ nirodheti … abbhatthaṅgataṃ abbhatthaṅgameti = ချုပ်ငြိမ်းပြီးသော အရာကို ချုပ်ငြိမ်းစေ … လုံးဝ ကွယ်ပျောက်ပြီးသော အရာကို လုံးဝ ကွယ်ပျောက်စေ
- ajātaṃ ajaneti … apātubhūtaṃ apātubhāveti = မမွေးဖွားသေးသော အရာကို မမွေးဖွားစေ … မထင်ရှားသေးသော အရာကို မထင်ရှားစေ
- cittasampayutto = စိတ်နှင့် ယှဉ်တွဲသော အရာ
- sammukhībhāvaṃ āgacchanti = မျက်နှာချင်းဆိုင် ဖြစ်လာကြ
- suññatā = ဆိတ်သုဉ်းခြင်း
- Suññatākathā = ဆိတ်သုဉ်းခြင်းအကြောင်း ဆွေးနွေးချက်
- X-kkhandhapariyāpanna = X အစုအဝေး၌ အကျုံးဝင်သော အရာ
- na anicco na saṅkhato … na vipariṇāmadhammo = မမြဲသော အရာ မဟုတ်၊ ပြုပြင်ဖန်တီးထားသော အရာ မဟုတ်၊ … ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော မဟုတ်
- Sāmaññaphalakathā = ရဟန်း၏ အကျိုးအကြောင်း ဆွေးနွေးချက်
- sāmaññaṃ = ရဟန်း အဖြစ်
- tāṇaṃ leṇaṃ saraṇaṃ parāyaṇaṃ accutaṃ amataṃ = ကာကွယ်ရာ၊ ပုန်းအောင်းရာ၊ ကိုးကွယ်ရာ၊ ဆုံးခန်းတိုင်ရာ၊ မစုတေသော အရာ၊ မသေသော အရာ
- dve / pañca / cha / nava asaṅkhatāni = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော အရာ နှစ်ပါး / ငါးပါး / ခြောက်ပါး / ကိုးပါး ရှိ
- dve tāṇāni…pe… antarikā vā = ကာကွယ်ရာ နှစ်ပါး… ကြားအပိုင်းဖြစ်စေ ရှိ (ch10 ending)
- patti (attainment) = ရရှိခြင်း
- Pattikathā = ရရှိခြင်းအကြောင်း ဆွေးနွေးချက်
- (evaṃ sabbaṃ vitthāretabbaṃ) = (ဤနည်းဖြင့် အားလုံးကို အကျယ် ချဲ့ရမည်)
- tathatā = ဟုတ်တိုင်းမှန်သော သဘော
- Tathatākathā = ဟုတ်တိုင်းမှန်သော သဘောအကြောင်း ဆွေးနွေးချက်
- rūpassa rūpatā = ရုပ်၏ ရုပ်ဖြစ်ခြင်း
- nibbānadhātu = နိဗ္ဗာန် ဓာတ်
- Kusalakathā = ကုသိုလ်အကြောင်း ဆွေးနွေးချက်
- anavajja = အပြစ် မရှိသော အရာ
- adoso / amoho = ဒေါသ မရှိခြင်း / မောဟ မရှိခြင်း
- accantaniyāmatā = အပြီးအပိုင် ကျိန်းသေခြင်း
- accantaniyato = အပြီးအပိုင် ကျိန်းသေသူ
- Accantaniyāmakathā = အပြီးအပိုင် ကျိန်းသေခြင်းအကြောင်း ဆွေးနွေးချက်
- uppajjeyya / nuppajjeyya = ဖြစ်ပေါ်ရာ / မဖြစ်ပေါ်ရာ
- Pahīnāti? = ပယ်ပြီးသလော။
- Akusalena maggena = အကုသိုလ် မဂ်ဖြင့် ဖြစ်သည်
- ummujjitvā = ပေါ်လာပြီး
- Indriyakathā = စွမ်းရည်အကြောင်း ဆွေးနွေးချက်
- asañcicca / sañcicca = မရည်ရွယ်ဘဲ / ရည်ရွယ်၍
- Asañciccakathā = မရည်ရွယ်ဘဲ ပြုခြင်းအကြောင်း ဆွေးနွေးချက်
- ānantariko = အနန္တရိယကံ ရှိသူ
- dhammasaññī saṅghabhedako = တရားဟု မှတ်ထင်လျက် သံဃာကို သင်းခွဲသူ
- Ñāṇakathā = ဉာဏ်အကြောင်း ဆွေးနွေးချက်
- samāpajjeyya / dadeyya = ဝင်စားရာ / ပေးရာ
- nirayapālā = ငရဲထိန်းတို့
- kammakāraṇā / kāraṇikā = ညှဉ်းပန်း နှိပ်စက်ခြင်းတို့ / ညှဉ်းပန်း နှိပ်စက်သူတို့
- Nirayapālakathā = ငရဲထိန်းအကြောင်း ဆွေးနွေးချက်
- pāpakammaṃ = ယုတ်မာသော ကံ
- Tiracchānakathā = တိရစ္ဆာန်အကြောင်း ဆွေးနွေးချက်
- pañcaṅgiko / aṭṭhaṅgiko maggo = မဂ်သည် အင်္ဂါ ငါးပါး / ရှစ်ပါး ရှိ (vutto bhagavatā: «အင်္ဂါ ရှစ်ပါး ရှိသော မဂ်»)
- seyyathidaṃ = ယင်းမှာ
- maggaṅgaṃ = မဂ်၏ အင်္ဂါ
- Maggakathā = မဂ်အကြောင်း ဆွေးနွေးချက်
- dhammavinaya = တရားနှင့် ဝိနည်း
- dvādasavatthukaṃ ñāṇaṃ = အခြေ ဆယ့်နှစ်ပါး ရှိသော ဉာဏ်
- paṇṇāsako (a group of fifty) = ငါးဆယ်အစု
- Catuttho paṇṇāsako = စတုတ္ထ ငါးဆယ်အစု
- Khuddako aḍḍhapaṇṇāsako = သေးငယ်သော ငါးဆယ်တစ်ဝက်အစု
- Paṇṇāsakuddānaṃ – = ငါးဆယ်အစုတို့၏ အကျဉ်းချုပ် –
- Sāsanakathā = သာသနာအကြောင်း ဆွေးနွေးချက်
- navaṃ kataṃ / navaṃ karoti / puna navaṃ kātuṃ = အသစ် ပြုထား / အသစ် ပြုလုပ် / တစ်ဖန် အသစ် ပြုလုပ်နိုင်
- tedhātuka = ဘုံ သုံးပါးနှင့် ဆိုင်သော
- avivitto (not detached from) = မကင်းသူ
- Avivittakathā = မကင်းခြင်းအကြောင်း ဆွေးနွေးချက်
- rūpadhātuarūpadhātūpagaṃ kammaṃ = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံသို့ ရောက်စေသော ကံ
- Saṃyojanakathā = နှောင်ကြိုးအကြောင်း ဆွေးနွေးချက်
- arahattappatti = ရဟန္တာ အဖြစ်သို့ ရောက်ခြင်း
- parinibbānaṃ = ပရိနိဗ္ဗာန် ပြုခြင်း
- sarāgo … sakileso / nirāgo … nikkileso = ရာဂ ရှိသူ … ကိလေသာ ရှိသူ / ရာဂ ကင်းသူ … ကိလေသာ ကင်းသူ
- sabbaṃ buddhavisayaṃ = ဘုရား၏ နယ်ပယ် အားလုံး
- adhippāyaiddhi = အလိုအတိုင်း ဖြစ်စေနိုင်သော ဣဒ္ဓိ
- Iddhikathā = ဣဒ္ဓိအကြောင်း ဆွေးနွေးချက်
- hīnātirekatā = ယုတ်ခြင်း ထူးခြင်း
- Buddhakathā = ဘုရားအကြောင်း ဆွေးနွေးချက်
- Sabbadisākathā = အရပ် အားလုံးအကြောင်း ဆွေးနွေးချက်
- puratthimā … uparimā disā = အရှေ့ / တောင် / အနောက် / မြောက် / အောက် / အထက် အရပ်
- Dhammakathā = သဘောတရားအကြောင်း ဆွေးနွေးချက်
- Kammakathā = ကံအကြောင်း ဆွေးနွေးချက်
- micchattaniyata / sammattaniyata / aniyata = မှားယွင်းမှု၌ ကျိန်းသေ / မှန်ကန်မှု၌ ကျိန်းသေ / မကျိန်းသေ (pi-1)
- rāsi = အစု
- X-ṭṭhena = X၏ အနက်အားဖြင့်
- diṭṭhadhamma- / upapajja- / aparāpariyavedanīyaṃ kammaṃ = မျက်မှောက်ဘဝ၌ ခံစားရမည့် ကံ / နောက်ဘဝ၌ ခံစားရမည့် ကံ / နောက်ဘဝ အဆက်ဆက်၌ ခံစားရမည့် ကံ
- Parinibbānakathā = ပရိနိဗ္ဗာန် ပြုခြင်းအကြောင်း ဆွေးနွေးချက်
- parinibbāyati = ပရိနိဗ္ဗာန် ပြု (pi-4)
- Kusalacittakathā = ကုသိုလ် စိတ်အကြောင်း ဆွေးနွေးချက်
- āneñja (the imperturbable) = မတုန်မလှုပ်သော အခြေ
- Āneñjakathā = မတုန်မလှုပ်သော အခြေအကြောင်း ဆွေးနွေးချက်
- dhammābhisamayo = တရားကို ထင်ထင်ရှားရှား သိမြင်ခြင်း
- gabbhaseyyāya = အမိဝမ်း၌ ကိန်းအောင်းစဉ်
- supinagatassa = အိပ်မက် မက်နေသူ၌
- Dhammābhisamayakathā = တရားကို ထင်ထင်ရှားရှား သိမြင်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Tissopikathā = သုံးပါးလုံးအကြောင်း ဆွေးနွေးချက်
- Abyākatakathā = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အရာအကြောင်း ဆွေးနွေးချက်
- supinantena = အိပ်မက်ထဲ၌
- abbohāriya = ထည့်တွက်ရန် မထိုက်သော အရာ
- āsevanapaccayatā = အဖန်ဖန် မှီဝဲခြင်း အကြောင်းဖြစ်ခြင်း
- Āsevanapaccayakathā = အဖန်ဖန် မှီဝဲခြင်း အကြောင်းဖြစ်ခြင်းအကြောင်း ဆွေးနွေးချက်
- āsevito bhāvito bahulīkato = အဖန်ဖန် မှီဝဲထား၊ ပွားများထား၊ အကြိမ်များစွာ ပြုထားသော
- X-saṃvattaniko = X သို့ ပို့ဆောင်တတ်
- Khaṇikakathā = ခဏအကြောင်း ဆွေးနွေးချက်
- ekacittakkhaṇika = စိတ် တစ်ခု၏ ခဏမျှသာ တည်သော အရာ
- āvuso = ငါ့ရှင်တို့
- ekādhippāyena = တူညီသော ရည်ရွယ်ချက်ဖြင့်
- Ekādhippāyakathā = တူညီသော ရည်ရွယ်ချက်အကြောင်း ဆွေးနွေးချက်
- amanussā = လူ မဟုတ်သူတို့
- Arahantavaṇṇakathā = ရဟန္တာတို့၏ အသွင်အကြောင်း ဆွေးနွေးချက်
- the eleven wrong deeds (adinnaṃ ādiyati … nigamaghātakaṃ karoti) = မပေးသည်ကို ယူ၊ မုသား ပြော၊ ကုန်းချောစကား ပြော၊ ကြမ်းတမ်းသော စကား ပြော၊ အကျိုးမဲ့ စကား ပြော၊ အိမ်ကို ဖောက်ထွင်း၊ လုယက်၊ အိမ်တစ်လုံးကို ဝိုင်းဝန်း လုယက်၊ လမ်း၌ ဓားပြ တိုက်၊ သူတစ်ပါး၏ မယားထံ သွား၊ ရွာကို ဖျက်ဆီး၊ နိဂုံးကို ဖျက်ဆီး
- issariyakāmakārikāhetu = မိမိ၏ အစွမ်းဖြင့် အလိုရှိတိုင်း ပြုခြင်းကြောင့်
- Issariyakāmakārikādikathā = မိမိ၏ အစွမ်းဖြင့် အလိုရှိတိုင်း ပြုခြင်း စသည်တို့အကြောင်း ဆွေးနွေးချက်
- vinipāta = ပျက်စီးကျရောက်ရာ ဘုံ
- Patirūpakathā = အတုအယောင်အကြောင်း ဆွေးနွေးချက်
- atthi na X X-patirūpako = X မဟုတ်ဘဲ Xနှင့် တူသော အရာ ရှိ
- aparinipphanna / parinipphanna = ပြည့်စုံစွာ မပြီးမြောက်သော အရာ / ပြည့်စုံစွာ ပြီးမြောက်သော အရာ
- Aparinipphannakathā = ပြည့်စုံစွာ မပြီးမြောက်သော အရာအကြောင်း ဆွေးနွေးချက်
- yadaniccaṃ taṃ dukkhaṃ = မမြဲသော အရာသည် ဆင်းရဲ၏
- Pañcattiṃsabhāṇavāraṃ = ရွတ်ဆိုရန် အပိုင်း သုံးဆယ့်ငါးပိုင်း
- Kathāvatthupakaraṇaṃ niṭṭhitaṃ = “အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း” ကျမ်း ပြီးဆုံးပြီ (F.BOOK_END)

## For the harmonise pass
- vagga ordinals beyond 10 («ဆယ့်ရှစ်ခုမြောက် ဝဂ်» …) and paṇṇāsaka «ငါးဆယ်အစု»: the ch13-25 agents choose their own; align.
- jahati: followed ch2-5 «စွန့်ပယ်» (ch26 Ekamagga, ch27); ch10 renders «catubhāgaṃ jahati» «ပယ်», ch12 pajahati «ပယ်».
- sāmaññaphala: followed ch11-12 «ရဟန်း၏ အကျိုး»; ch2-5 has «ရဟန်းအဖြစ်၏ ဖိုလ်»; sāmañña here «ရဟန်း အဖြစ်».
- ghāyati / sāyati: followed ch6-10 SENSE «… ခံ»; ch12 uses «နမ်း / လျက်».
- niyata «ကျိန်းသေ» (pi-1) for accantaniyata / sassatadiṭṭhiyā niyata; niyāma (okkantaniyāma, the Paṇṇāsaka verse) stays
  «သေချာသော လမ်းကြောင်း» (pi-4).
- «atthi tassa vitakkavicārā» keeps the ch10 rule wording «… ဆက်လက်သုံးသပ်မှု ရှိ» (without «တို့»).
- Words that the negation check reads as «မ»: «ဆုံးမ» / «အဆုံးအမ» avoided (ovāda = «ဩဝါဒ»); pāpakamma = «ယုတ်မာသော ကံ»
  (not «မကောင်းမှု»); «မယား», «တမလွန်» added to NOT_NEG.
- The Kathāvatthu frame «Na vattabbaṃ – P-ti?» adds “…” also where the Pāli has no quotes (^5-838, ^5-887): as the sample.

## Unsure Pāli / interpretation (for the reviewer)
- ^5-806 «sappāṭihāriya» = «အံ့ဖွယ် ရှိသော»; «karaṇīyo ovādo karaṇīyā anusāsanī» = «ငါ၏ ဩဝါဒကို လိုက်နာသင့်၏၊
  အနုသာသနီကို လိုက်နာသင့်၏» (English zero-shot reading); dasasahassilokadhātu «စကြဝဠာ တစ်သောင်း».
- ^5-809 «nhāyanti vilimpanti ucchādenti … gandhakaraṇīyaṃ karonti» (bathe, anoint, rub … make perfume); odanakummāsa
  «ထမင်းနှင့် မုန့်» (kummāsa = a gruel / junket; approximate).
- ^5-802 place names transliterated (ဥက္ကဋ္ဌာ, သုဘဂဝုန်တော, ကလန္ဒကနိဝါပ, ကူဋာဂါရ ဇရပ်).
- ^5-813 paṇidhi «စိတ် ဦးတည်ထားခြင်း» (āvaṭṭanā …pe… paṇidhi = the series from adverting to aspiration).
- ^5-829 «ajātaṃ ajaneti, asañjātaṃ asañjaneti …» read as «the unborn is made unborn» (parallel to «niruddhaṃ nirodheti»).
- ^5-841/842 tathatā «ဟုတ်တိုင်းမှန်သော သဘော»; «rūpassa rūpatā, nanu rūpatā asaṅkhatā» = «ရုပ်၏ ရုပ်ဖြစ်ခြင်း ရှိ၏၊
  ရုပ်ဖြစ်ခြင်းသည် … အရာ ဖြစ်သည် မဟုတ်လော» (the inner «nanu» kept as a question in every form).
- ^5-852 «sakiṃ nimuggo nimuggova hoti» «တစ်ကြိမ် နစ်မြုပ်လျှင် နစ်မြုပ်လျက်သာ ဖြစ်၏»; patigādhappatto «ခြေကုတ်ရာ မြေသို့ ရောက်».
- ^5-853 «tikkhindriye mudindriye … svākāre suviññāpaye» (sharp / dull faculties, good disposition, easy to teach).
- ^5-862 verse: «vaggarato adhammaṭṭho, yogakkhemā padhaṃsati» «အုပ်စုကွဲခြင်း၌ မွေ့လျော်၍ တရား မဟုတ်သည်၌ တည်သဖြင့်
  ထမ်းပိုးတို့မှ ဘေးကင်းခြင်းမှ ပျက်စီး၏».
- ^5-867 verse: Vessabhū / pettirājā / Soma / Yama / Vessavaṇa as names; «ito paṇunnaṃ paralokapattaṃ» = the one driven
  from here who has reached the next world.
- ^5-868 the hell punishments (kuṭhārī «ပုဆိန်», vāsī «ပဲခွပ်», pheṇuddehakaṃ paccati «အမြှုပ် ဆူပွက်လျက် ကျက်»).
- ^5-870/871 «sahassayuttaṃ dibbaṃ yānaṃ» «တစ်ထောင်ဖြင့် ကပ်ထားသော နတ် ယာဉ်»; yāvasikā kāraṇikā bhattakārakā
  «မြက်ကျွေးသူ၊ လေ့ကျင့်ပေးသူ၊ အစာ ချက်ပြုတ်သူ».
- ^5-894 ācinanto apacinanto … visinento ussinento vidhūpento sandhūpento = «စုဆောင်း၊ ဖျက်ဆီး … ဖြန့်ကျက်၊ စုစည်း၊
  ငြိမ်းစေ၊ တောက်လောင်စေ» (as the English zero-shot).
- ^5-906 «tajjo samannāhāro» «ထိုအရာနှင့် ဆိုင်သော နှလုံးသွင်းမှု»; «viññāṇabhāga» «သိစိတ် အစိတ်အပိုင်း»; in the kāya version
  «no ca…pe…» = «… နှလုံးသွင်းမှုလည်း မဖြစ်…» (the elided verb supplied so the negation stays visible).
- ^5-913 «aparantapaṃ akāsi» «အခြား ပြင်းထန်သော အကျင့်ကို ကျင့်ခဲ့»; «aññaṃ satthāraṃ uddisi» «အခြား ဆရာကို ကိုးကွယ်ခဲ့».
- ^5-918 Paṇṇāsaka verse read as the first kathās / names of the five paṇṇāsakas (Mahā-, Niyāma, Anusaya, Niggaha,
  the small fifth); «ujjotanā satthusamaye» «ဆရာ၏ အယူဝါဒ၌ ထွန်းလင်းစေတတ်သော».

## Source slips (translated as written; Pāli not changed)
- ^5-820 «no ca vata re vattabbe – "dvinnaṃ … jhānantarikāti.» opening quote never closed (and the consequent adds
  «jhānantarikā»): closed in the Burmese.
- ^5-834 «Na vattabbaṃ – suññatā saṅkhārakkhandhapariyāpannā"ti?» opening quote missing (SLIP line, regular quotes).
- ^5-836 heading «(188) 3 Sāmaññaphalakathā» without the dot: kept «(188) 3 …».
- ^5-849 «Akusalena maggena.» without «ti» (^5-848/850 have it): same Burmese. ^5-849/850 «Akusalo maggo…pe… no ca vata re
  vattabbe – "…"ti.» without «Hañci»: rendered «အကုသိုလ် မဂ်သည်… အမှန်ပင် ဤသို့လည်း မဆိုသင့် – “…”။».
- ^5-864 «no ca vata re vattabbe – natthi puthujjanassa ñāṇa"nti» opening quote missing: regular quotes.
- ^5-868 line 2: the quotation opened on the line closes only at the end of the verse (four lines later), as the Pāli.
- ^5-877 «"idaṃ dukkhaṃ ariyasacca"nti me …» the outer double quote closes after the first phrase (SLIP line; the Burmese
  uses the regular nesting of ch12's passage). Variants «dukkhasamudayo» / «dukkhanirodhā» spelling labels.
- ^5-903 «Nanu vuttaṃ … "…"ti [a. ni. 8.40]. Attheva suttantoti?» with «.» (elsewhere «!»): rendered as the nanu question.
- ^5-905 «…amatapariyosāno"ti attheva suttantoti, āmantā.» (one sentence, small letters): «…”ဟူ၍ ထိုသို့သော သုတ္တန်
  အမှန်ပင် ရှိသလော၊ ဟုတ်ပါသည်။».
- ^5-914 colophon «Issariyakāmakārikākathā niṭṭhitā» vs heading «Issariyakāmakārikādikathā»: each translated as written.
- ^5-891 uddāna «adhippāyiddhi» vs the text «adhippāyaiddhi»: same Burmese.
- ^5-827 uddāna «cakkhunā rūpaṃ passati kāyena phoṭṭhabbaṃ phusati.» (no «ti»): as written.
