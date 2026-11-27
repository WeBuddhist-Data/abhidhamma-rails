# pi-5 Burmese zero-shot, chapters 6-10: notes

Status: DONE 2026-11-20 (not committed). Chapters 6-atitakkhandhadikatha (5 segments), 7-ekaccam-atthitikatha (5),
8-satipatthanakatha (4), 9-hevatthikatha (4), 10-dutiyavaggo (69).
Source rule kept: translated from the Pāli only; no Burmese translation or nissaya opened, no web search; English pi-5
zero-shot read for meaning only (ch6, ch9); Marathi pi-5 notes-ch6-10.md read for the frame inventory only.

## Files and run
- `make_ch6-10.py`: imports `make_sample.py` (read only: installs the approved sample tables, its main never runs)
  and `my5_formulas.py`; extends PROP / QUOTE / SENT / LINES / HEAD / COLO / ANCHOR / VAR_KIND / REF / REF_NOTE /
  BR_TABLE / NOTE in memory only. New frames: «X-ti katvā P-ti?», «X-ti P-ti?» (satipaṭṭhāna), «Tena hi vattabbaṃ –
  "P"ti.»; new rules: atthi G X / G atthi X (list of LST words, «…» inside lists), optative act lists (methuna, the
  ten crimes), «X samāpannassa Y niruddhā hoti», «G Y kaṇṭako vutto bhagavatā», «S vuttā bhagavatā – "Q"», durations
  «(WHO) (ekaṃ cittaṃ) DUR tiṭṭhati», «WHO DUR āyuppamāṇaṃ». Future clauses: class Fut («…လိမ့်မည်»).
  `--misses` / `--units` list misses and write nothing. NEW (in the script) holds the new strings listed below.
- `check_ch6-10.py [chapter.md …]`: A rebuild; B1 structure (+ no double space); B2 polarity (sample);
  B7 existence polarity (every natthi / na atthi = one «မရှိ», exemptions: the arūpa base names and asaṅkhata /
  asaṅkhāraparinibbāyī whose fixed pi-1 / pi-4 Burmese has «မရှိ»; positive atthi ≤ «ရှိ»); B3 numbers; B4 quote
  nesting; B5 recurring sentences, also across the approved sample files; B6 table values; C reuse (sample REUSE list,
  narrowed where needed, plus 52 terms of these chapters).
- Mutation test: a «မရှိ» changed to «ရှိ» is caught (A, B7, B5).

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all five (check_marks is `pi-4-mr/check_marks.py`: the
  brief's `pi-5-mr/check_marks.py` does not exist; burmese-style.md names the pi-4-mr one). chk-pe copies deleted.
- check_ch6-10.py: 0 mismatches; reuse 882 / 882 (per chapter: ch6 110/110, ch7 40/40, ch8 98/98, ch9 49/49,
  ch10 585/585); B5 2104 / 2104 recurring occurrences identical.

## Main choices (for the consistency pass; chapters 2-5 may render some of these differently)
- atīta / anāgata / paccuppanna = «အတိတ် / အနာဂတ် / ပစ္စုပ္ပန်» (pi-1); atthi / natthi (existence) = «ရှိ / မရှိ».
- Headings: Nasuttasādhanaṃ «သုတ္တန်ဖြင့် မသက်သေပြခြင်း», Suttasādhanaṃ «သုတ္တန်ဖြင့် သက်သေပြခြင်း» (ch5 has
  Suttasādhanaṃ too); kathā names «X-အကြောင်း ဆွေးနွေးချက်»; Dutiyavaggo «ဒုတိယ ဝဂ်»; Paṭhamavaggo «ပထမ ဝဂ်»;
  Mahāvaggo «“ကြီးမြတ်သော” ဝဂ်» (pattern of the sample's «“ကောင်းမွန်သော”»); Tassuddānaṃ – «ထို၏ အကျဉ်းချုပ် –».
- The uddāna of vagga 1 names kathās 1-9 (Upalabbho «တွေ့ရခြင်း», parihāni «ဆုတ်ယုတ်ခြင်း», brahmacariyavāso «မြတ်သော
  အကျင့်ကို ကျင့်ခြင်း», odhiso «အပိုင်းအခြားအားဖြင့်», pariññā «ပိုင်းခြား သိခြင်း», kāmarāgappahānaṃ «ကာမရာဂကို
  ပယ်ခြင်း», sabbatthivādo «အားလုံး ရှိသည်ဟူသော ဝါဒ», āyatanaṃ, atītānāgato, subhaṅgo «ကောင်းစွာ ခွဲခြားချက်»):
  to be aligned with the ch1-5 headings.
- Pāli lists of Mātikā adjectives reuse pi-1 (anāsava … «X၏ အာရုံ မဖြစ်နိုင်သော»); the kilesa ten (pi-1 ^1-1235,
  rāga «ရာဂ» termbase); bojjhaṅga names (pi-2 ^2-466); deva realms and lifespans (pi-2 ^2-1023 … ^2-1028); the
  vicikicchā objects (pi-2 ^2-915); pi-4 person types (^4-M-7); khandha definitions read from pi-2 ^2-2 … ^2-26.
- avipāka (dhammā) «အကျိုး မပေးသော» (to keep «မရှိ» for natthi only); vimati «စိတ်ရှုပ်ထွေးခြင်း» (pi-1), aññāṇa
  «မသိခြင်း» (termbase; avijjā stays «အမှန်ကို မသိမှု»), kaṅkhā «သံသယ».
- anuppādadhamma written «နောင်အခါ မဖြစ်ပေါ်နိုင်သော သဘော» and niraggaḷa «တံခါး ဂျက်ကို ဖြုတ်ပြီးသူ» (no «မရှိ»).

## New recurring terms and phrases (Pāli = Burmese; from make_ch6-10.py NEW)
- Atītakkhandhādikathā = အတိတ် အစုအဝေး စသည်တို့အကြောင်း ဆွေးနွေးချက်
- Nasuttasādhanaṃ = သုတ္တန်ဖြင့် မသက်သေပြခြင်း
- Suttasādhanaṃ = သုတ္တန်ဖြင့် သက်သေပြခြင်း
- atītaṃ / anāgataṃ / paccuppannaṃ (the past …) = အတိတ် / အနာဂတ် / ပစ္စုပ္ပန်
- atthi / natthi (exists) = ရှိ / မရှိ
- khandhā dhātu āyatanaṃ = အစုအဝေး၊ ဓာတ်၊ အာရုံခံ နယ်ပယ်
- X khandhā / khandho (is aggregates / an aggregate) = Xသည် အစုအဝေးတို့ / အစုအဝေး ဖြစ်
- X P X atthi / natthi = Xသည် P ဖြစ်၍ X ရှိ / မရှိ
- atītānāgatā khandhā dhātu āyatanaṃ natthi cete = အတိတ်နှင့် အနာဂတ်သည် အစုအဝေး၊ ဓာတ်၊ အာရုံခံ နယ်ပယ်တို့ ဖြစ်ကြ၍ ထိုအရာတို့ မရှိ
- Ekaccaṃ atthītikathā = အချို့ ရှိသည်ဟူသော ဆွေးနွေးချက်
- Atītādiekaccakathā = အတိတ် စသည်တို့၏ အချို့အကြောင်း ဆွေးနွေးချက်
- Anāgatādiekaccakathā = အနာဂတ် စသည်တို့၏ အချို့အကြောင်း ဆွေးနွေးချက်
- ekaccaṃ / ekacce (some) = အချို့
- te (those dhammas, after «–») = ထိုအရာတို့
- vipakkavipāka = အကျိုး ရင့်ကျက်ပြီးသော
- avipāka (dhammā) = အကျိုး မပေးသော
- anuppādino (dhammā) = မဖြစ်ပေါ်လာမည့်
- niruddhaṃ = ချုပ်ငြိမ်းပြီး / မချုပ်ငြိမ်းသေး
- vigataṃ = ကင်းပျောက်ပြီး / မကင်းပျောက်သေး
- atthaṅgataṃ = ကွယ်ပျောက်ပြီး / မကွယ်ပျောက်သေး
- abbhatthaṅgataṃ = လုံးဝ ကွယ်ပျောက်ပြီး / လုံးဝ မကွယ်ပျောက်သေး
- jātaṃ = မွေးဖွားပြီး / မမွေးဖွားသေး
- sañjātaṃ = ကောင်းစွာ မွေးဖွားပြီး / ကောင်းစွာ မမွေးဖွားသေး
- nibbattaṃ = ပေါ်ထွက်ပြီး / မပေါ်ထွက်သေး
- pātubhūtaṃ = ထင်ရှားလာပြီး / ထင်ရှား မလာသေး
- Kiṃ atthi(,) kiṃ natthīti? = အဘယ်အရာ ရှိ၍ အဘယ်အရာ မရှိသနည်း။
- ekadesaṃ (in part) = တစ်စိတ်တစ်ဒေသ
- vipaccissanti = အကျိုး ပေးကြလိမ့်မည်
- uppajjissanti = ဖြစ်ပေါ်ကြလိမ့်မည်
- nirujjhissanti = ချုပ်ငြိမ်းကြလိမ့်မည်
- X dhammā – te atthi / natthi = X သဘောတရားတို့ – ထိုအရာတို့ ရှိ / မရှိ
- X ekacce atthi, ekacce natthi = X၌ အချို့ ရှိသည်၊ အချို့ မရှိ
- X-ti katvā P-ti? = Xဟု အကြောင်းပြု၍ Pသလော
- Satipaṭṭhānakathā = သတိပဋ္ဌာန်အကြောင်း ဆွေးနွေးချက်
- ekāyanamaggo = တစ်ကြောင်းတည်းသော လမ်း
- khayagāmī = ကုန်ခန်းခြင်းဆီသို့ ဦးတည်သော
- bodhagāmī = ဗောဓိဆီသို့ ဦးတည်သော
- buddhānussati = ဘုရားကို အဖန်ဖန် အောက်မေ့ခြင်း
- dhammānussati = တရားကို အဖန်ဖန် အောက်မေ့ခြင်း
- saṅghānussati = သံဃာကို အဖန်ဖန် အောက်မေ့ခြင်း
- sīlānussati = သီလကို အဖန်ဖန် အောက်မေ့ခြင်း
- cāgānussati = စွန့်ကြဲမှုကို အဖန်ဖန် အောက်မေ့ခြင်း
- devatānussati = နတ်တို့ကို အဖန်ဖန် အောက်မေ့ခြင်း
- ānāpānassati = ထွက်သက် ဝင်သက်၌ သတိ ထားခြင်း
- maraṇānussati = သေခြင်းကို အဖန်ဖန် အောက်မေ့ခြင်း
- kāyagatāsati = ကိုယ်ကို အာရုံပြုသော သတိ
- upasamānussati = ငြိမ်းချမ်းခြင်းကို အဖန်ဖန် အောက်မေ့ခြင်း
- satipaṭṭhāna = သတိပဋ္ဌာန်
- X satipaṭṭhānaṃ, tañca (na) sati = Xသည် သတိပဋ္ဌာန် ဖြစ်၍ ထိုအရာသည်လည်း သတိ (မဟုတ်)
- phassapaṭṭhāna / cittapaṭṭhāna = တွေ့ထိမှု ပဋ္ဌာန် / စိတ် ပဋ္ဌာန်
- ārabbha … santiṭṭhati = …ကို အာရုံပြု၍ … တည်နေ
- X-ti P-ti? (P because of X) = Xဟူ၍ Pသလော
- amata (the deathless) = အမြိုက်
- paribhuñjati = သုံးဆောင်
- cakkavattī (rājā) = စကြဝတေး မင်း
- ratana = ရတနာ
- tathāgata arahant sammāsambuddha = ရဟန္တာ၊ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် ဖြစ်တော်မူသော မြတ်စွာဘုရား
- heva (in a way, hevatthi / heva natthi) = တစ်နည်းအားဖြင့်
- Hevatthikathā = တစ်နည်းအားဖြင့် ရှိသည်ဟူသော ဆွေးနွေးချက်
- hevatthi, heva natthi = တစ်နည်းအားဖြင့် ရှိသည်၊ တစ်နည်းအားဖြင့် မရှိ
- sevatthi, seva natthi = ထိုအရာပင် ရှိသည်၊ ထိုအရာပင် မရှိ
- Kintatthi, kinti natthīti? = အဘယ်နည်းဖြင့် ရှိ၍ အဘယ်နည်းဖြင့် မရှိသနည်း။
- atthaṭṭho / natthaṭṭho; atthibhāvo / natthibhāvo = ရှိခြင်း၏ အနက် / မရှိခြင်း၏ အနက်; ရှိခြင်း၏ အဖြစ် / မရှိခြင်း၏ အဖြစ်
- X Y-ti hevatthi / heva natthi = Xသည် Y အနေဖြင့် တစ်နည်းအားဖြင့် ရှိ / မရှိ
- Tassuddānaṃ – = ထို၏ အကျဉ်းချုပ် –
- Paṭhamavaggo = ပထမ ဝဂ်
- Mahāvaggo = “ကြီးမြတ်သော” ဝဂ်
- Dutiyavaggo = ဒုတိယ ဝဂ်
- sadhammakusala / paradhammakusala arahā = မိမိ၏ အရာ၌ ကျွမ်းကျင်သော ရဟန္တာ / သူတစ်ပါး၏ အရာ၌ ကျွမ်းကျင်သော ရဟန္တာ
- mārakāyikā devatā = မာရ်နတ်၏ အပေါင်းအပါ နတ်တို့
- asuci sukkavissaṭṭhi = မစင်ကြယ်သော သုက်ထွက်ခြင်း
- kāmarāgapariyuṭṭhānaṃ = ကာမရာဂ ထကြွခြင်း
- kāmogho = ကာမ ရေအလျဉ်
- kāmayogo = ကာမ ထမ်းပိုး
- kāmacchandanīvaraṇaṃ = ကာမကို လိုလားမှု အတားအဆီး
- avijjogho = အမှန်ကို မသိမှု ရေအလျဉ်
- avijjānusayo = အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း
- avijjāpariyuṭṭhānaṃ = အမှန်ကို မသိမှု ထကြွခြင်း
- vicikicchāpariyuṭṭhānaṃ = ယုံမှားမှု ထကြွခြင်း
- āsayo = သိုလှောင်ရာ
- parūpahāro = သူတစ်ပါးက ဆောင်ယူပေးခြင်း
- atthi G X / natthi G X = G၌ X ရှိ / မရှိ
- Kenaṭṭhenāti? = အဘယ် အနက်ကြောင့်နည်း။
- Kiṃ kāraṇāti? = အဘယ် အကြောင်းကြောင့်နည်း။
- upasaṃharanti = ဆောင်ယူပေးကြ
- asitapītakhāyitasāyitassa nissando = စား၊ သောက်၊ ခဲ၊ လျက်ထားသော အရာ၏ အကျိုးဆက်
- methunaṃ dhammaṃ paṭiseveyya = မေထုန် အကျင့်ကို မှီဝဲရာ
- methunaṃ uppādeyya = မေထုန်ကို ဖြစ်စေရာ
- puttasambādhasayanaṃ ajjhāvaseyya = သားသမီးတို့ဖြင့် ကျဉ်းကျပ်သော အိပ်ရာ၌ နေရာ
- kāsikacandanaṃ paccanubhaveyya = ကာသိ စန္ဒကူးကို ခံစားရာ
- mālāgandhavilepanaṃ dhāreyya = ပန်း၊ နံ့သာ၊ နံ့သာပျောင်းကို ဆောင်ရာ
- jātarūparajataṃ sādiyeyya = ရွှေ ငွေကို သာယာရာ
- pāṇaṃ haneyya = သူ့အသက်ကို သတ်ရာ
- adinnaṃ ādiyeyya = မပေးသည်ကို ယူရာ
- musā bhaṇeyya = မုသား ပြောရာ
- pisuṇaṃ bhaṇeyya = ကုန်းတိုက်သော စကားကို ပြောရာ
- pharusaṃ bhaṇeyya = ကြမ်းတမ်းသော စကားကို ပြောရာ
- samphaṃ palapeyya = အကျိုးမဲ့ စကားကို ပြောရာ
- sandhiṃ chindeyya = အိမ်ကို ဖောက်ရာ
- nillopaṃ hareyya = ဥစ္စာကို လုယူရာ
- ekāgāriyaṃ kareyya = အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်ရာ
- paripanthe tiṭṭheyya = လမ်းခရီး၌ ဓားပြ တိုက်ရာ
- paradāraṃ gaccheyya = သူတစ်ပါး၏ မယားထံ သွားရာ
- gāmaghātaṃ kareyya = ရွာကို ဖျက်ဆီး၍ လုယက်ရာ
- nigamaghātaṃ kareyya = နိဂုံးကို ဖျက်ဆီး၍ လုယက်ရာ
- aññāṇapakato = မသိခြင်းဖြင့် လွှမ်းမိုးခံရ၍
- pahīno ucchinnamūlo tālāvatthukato anabhāvaṅkato āyatiṃ anuppādadhammo = ပယ်ပြီး၊ အမြစ် ပြတ်ပြီး၊ ထန်းငုတ်ကဲ့သို့ ပြုထားပြီး၊ ပျောက်ပျက်အောင် ပြုထားပြီး ဖြစ်၍ နောင်အခါ မဖြစ်ပေါ်နိုင်သော သဘော
- Xppahānāya maggo bhāvito = Xကို ပယ်ရန် မဂ်ကို ပွားများပြီး
- vītarāgo = ရာဂ ကင်းသူ
- vītadoso = ဒေါသ ကင်းသူ
- vītamoho = မောဟ ကင်းသူ
- katakaraṇīyo = ပြုဖွယ်ကိစ္စကို ပြုပြီးသူ
- ohitabhāro = ဝန်ကို ချထားပြီးသူ
- anuppattasadattho = မိမိ၏ အကျိုးသို့ ရောက်ပြီးသူ
- parikkhīṇabhavasaṃyojano = ဘဝ နှောင်ကြိုး ကုန်ခန်းပြီးသူ
- sammadaññāvimutto = မှန်ကန်စွာ သိ၍ လွတ်မြောက်ပြီးသူ
- ukkhittapaligho = တံခါး ကန့်လန့်ကို ဖယ်ရှားပြီးသူ
- saṅkiṇṇaparikho = ကျုံးကို ဖို့ပြီးသူ
- abbūḷhesiko = တိုင်ကို နုတ်ပြီးသူ
- niraggaḷo = တံခါး ဂျက်ကို ဖြုတ်ပြီးသူ
- ariyo = အရိယာ
- pannaddhajo = အလံကို ချပြီးသူ
- pannabhāro = ဝန်ထုပ်ကို ပစ်ချပြီးသူ
- visaññutto = နှောင်ကြိုးမှ ကင်းလွတ်ပြီးသူ
- suvijitavijayo = အောင်ပွဲကို ကောင်းစွာ အောင်ပြီးသူ
- dukkhaṃ tassa pariññātaṃ … sacchikātabbaṃ sacchikataṃ = ထိုသူသည် ဒုက္ခကို ပိုင်းခြား သိပြီး၊ ဖြစ်ပေါ်ခြင်းကို ပယ်ပြီး၊ ချုပ်ငြိမ်းခြင်းကို မျက်မှောက်ပြုပြီး၊ မဂ်ကို ပွားများပြီး၊ ထူးကဲစွာ သိရမည့် အရာကို ထူးကဲစွာ သိပြီး၊ ပိုင်းခြား သိရမည့် အရာကို ပိုင်းခြား သိပြီး၊ ပယ်ရမည့် အရာကို ပယ်ပြီး၊ ပွားများရမည့် အရာကို ပွားများပြီး၊ မျက်မှောက်ပြုရမည့် အရာကို မျက်မှောက်ပြုပြီး
- (10) 1. Parūpahārakathā = (10) 1. သူတစ်ပါးက ဆောင်ယူပေးခြင်းအကြောင်း ဆွေးနွေးချက်
- Parūpahārakathā = သူတစ်ပါးက ဆောင်ယူပေးခြင်းအကြောင်း ဆွေးနွေးချက်
- (11) 2. Aññāṇakathā = (11) 2. မသိခြင်းအကြောင်း ဆွေးနွေးချက်
- Aññāṇakathā = မသိခြင်းအကြောင်း ဆွေးနွေးချက်
- (12) 3. Kaṅkhākathā = (12) 3. သံသယအကြောင်း ဆွေးနွေးချက်
- Kaṅkhākathā = သံသယအကြောင်း ဆွေးနွေးချက်
- (13) 4. Paravitāraṇakathā = (13) 4. သူတစ်ပါးက ရှင်းပြပေးခြင်းအကြောင်း ဆွေးနွေးချက်
- Paravitāraṇakathā = သူတစ်ပါးက ရှင်းပြပေးခြင်းအကြောင်း ဆွေးနွေးချက်
- paravitāraṇā = သူတစ်ပါးက ရှင်းပြပေးခြင်း
- dukkhasamudayo / dukkhanirodho / dukkhanirodhagāminī paṭipadā = ဒုက္ခ ဖြစ်ပေါ်ခြင်း / ဒုက္ခ ချုပ်ငြိမ်းခြင်း / ဒုက္ခ ချုပ်ငြိမ်းခြင်းသို့ ရောက်ကြောင်း အကျင့်
- paraneyyo = သူတစ်ပါး လမ်းပြရသူ
- parapattiyo = သူတစ်ပါးကို ယုံကြည်ရသူ
- parapaccayo = သူတစ်ပါးကို အားကိုးရသူ
- parapaṭibaddhabhū = သူတစ်ပါးနှင့် ချည်နှောင်နေသူ
- na jānāti na passati sammūḷho asampajāno = မသိ၊ မမြင်၊ တွေဝေ၍ ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း ကင်းသူ
- (14) 5. Vacībhedakathā = (14) 5. နှုတ်ဖြင့် စကား ထွက်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Vacībhedakathā = နှုတ်ဖြင့် စကား ထွက်ခြင်းအကြောင်း ဆွေးနွေးချက်
- vacībhedo = နှုတ်ဖြင့် စကား ထွက်ခြင်း
- kāyabhedo = ကိုယ်ကို လှုပ်ရှားခြင်း
- samāpannassa = သမာပတ်ကို ဝင်စားနေသူ
- ñāṇaṃ saccagocaraṃ / sotaṃ saddagocaraṃ = ဉာဏ်သည် သစ္စာကို ကျက်စားရာ ပြု / နားသည် အသံကို ကျက်စားရာ ပြု
- vitakkavicārā vacīsaṅkhārā / vitakkasamuṭṭhānā vācā = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ကို နှုတ်၏ ပြုပြင်ဖန်တီးမှုတို့ဟု / စတင်ကြံစည်မှုကြောင့် ဖြစ်ပေါ်သော စကားဟု
- kaṇṭako / kaṇḍako (a thorn) = ဆူးငြောင့်
- (15) 6. Dukkhāhārakathā = (15) 6. ဒုက္ခဟု ဆိုခြင်းအကြောင်း ဆွေးနွေးချက်
- Dukkhāhārakathā = ဒုက္ခဟု ဆိုခြင်းအကြောင်း ဆွေးနွေးချက်
- dukkhāhāro = ဒုက္ခဟု ဆိုခြင်း
- mātughātako = အမိကို သတ်သူ
- pitughātako = အဖကို သတ်သူ
- arahantaghātako = ရဟန္တာကို သတ်သူ
- ruhiruppādako = ဘုရားရှင်၏ သွေးကို စိမ်းစေသူ
- saṅghabhedako = သံဃာကို သင်းခွဲသူ
- (16) 7. Cittaṭṭhitikathā = (16) 7. စိတ်၏ တည်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Cittaṭṭhitikathā = စိတ်၏ တည်ခြင်းအကြောင်း ဆွေးနွေးချက်
- uppādakkhaṇo / vayakkhaṇo = ဖြစ်ခြင်း ခဏ / ပျက်ခြင်း ခဏ
- lahuparivatta = လျင်မြန်စွာ ပြောင်းလဲတတ်သော
- (17) 8. Kukkuḷakathā = (17) 8. ပြာပူအကြောင်း ဆွေးနွေးချက်
- Kukkuḷakathā = ပြာပူအကြောင်း ဆွေးနွေးချက်
- sabbe saṅkhārā anodhiṃ katvā kukkuḷā = ပြုပြင်ဖန်တီးမှု အားလုံးတို့သည် ချွင်းချက် မထားဘဲ ပြာပူ ဖြစ်
- sukhā vedanā = သာယာသော ခံစားမှု
- kāyikaṃ sukhaṃ = ကိုယ်၏ ချမ်းသာ
- cetasikaṃ sukhaṃ = စိတ်၏ ချမ်းသာ
- dibbaṃ sukhaṃ = နတ်တို့၏ ချမ်းသာ
- mānusakaṃ sukhaṃ = လူတို့၏ ချမ်းသာ
- lābhasukhaṃ = လာဘ် ရခြင်း၏ ချမ်းသာ
- sakkārasukhaṃ = အရိုအသေ ပြုခံရခြင်း၏ ချမ်းသာ
- yānasukhaṃ = ယာဉ်၏ ချမ်းသာ
- sayanasukhaṃ = အိပ်ရာ၏ ချမ်းသာ
- issariyasukhaṃ = အစိုးရခြင်း၏ ချမ်းသာ
- ādhipaccasukhaṃ = အကြီးအကဲ ဖြစ်ခြင်း၏ ချမ်းသာ
- gihisukhaṃ = လူဝတ်ကြောင်၏ ချမ်းသာ
- sāmaññasukhaṃ = ရဟန်း၏ ချမ်းသာ
- sāsavaṃ sukhaṃ = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ချမ်းသာ
- anāsavaṃ sukhaṃ = စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော ချမ်းသာ
- upadhisukhaṃ = ဥပဓိနှင့် စပ်သော ချမ်းသာ
- nirūpadhisukhaṃ = ဥပဓိ ကင်းသော ချမ်းသာ
- sāmisaṃ sukhaṃ = ကာမဂုဏ်နှင့် စပ်သော ချမ်းသာ
- nirāmisaṃ sukhaṃ = ကာမဂုဏ် ကင်းသော ချမ်းသာ
- sappītikaṃ sukhaṃ = ပီတိနှင့်တကွ ဖြစ်သော ချမ်းသာ
- nippītikaṃ sukhaṃ = ပီတိ ကင်းသော ချမ်းသာ
- jhānasukhaṃ = ဈာန်၏ ချမ်းသာ
- vimuttisukhaṃ = လွတ်မြောက်ခြင်း၏ ချမ်းသာ
- kāmasukhaṃ = ကာမ၏ ချမ်းသာ
- nekkhammasukhaṃ = ကာမမှ ထွက်မြောက်ခြင်း၏ ချမ်းသာ
- vivekasukhaṃ = ဆိတ်ငြိမ်ခြင်း၏ ချမ်းသာ
- upasamasukhaṃ = ငြိမ်းချမ်းခြင်း၏ ချမ်းသာ
- sambodhasukhaṃ = အမှန်ကို သိခြင်း၏ ချမ်းသာ
- cha phassāyatanikā nirayā / saggā = တွေ့ထိမှု ခြောက်ပါးနှင့် စပ်သော ငရဲ / နတ်ပြည်
- (18) 9. Anupubbābhisamayakathā = (18) 9. အစဉ်အတိုင်း ထင်ထင်ရှားရှား သိမြင်ခြင်းအကြောင်း ဆွေးနွေးချက်
- Anupubbābhisamayakathā = အစဉ်အတိုင်း ထင်ထင်ရှားရှား သိမြင်ခြင်းအကြောင်း ဆွေးနွေးချက်
- anupubbābhisamayo = အစဉ်အတိုင်း ထင်ထင်ရှားရှား သိမြင်ခြင်း
- tadekaṭṭhe ca kilese catubhāgaṃ jahati = ထိုတို့နှင့် တစ်နေရာတည်း တည်ရှိသော ကိလေသာတို့ကိုလည်း လေးပုံတစ်ပုံ ပယ်သည်
- catubhāgaṃ = လေးပုံတစ်ပုံ
- paṭipannako / phale ṭhito = ကျင့်ကြံဆဲသူ / ဖိုလ်၌ တည်သူ
- [sakavādīpucchālakkhaṇaṃ] / [paravādīpucchālakkhaṇaṃ] = မိမိဘက်၏ အမေး၏ အမှတ်အသား / တစ်ဖက်သား၏ အမေး၏ အမှတ်အသား
- (19) 10. Vohārakathā = (19) 10. ပြောဆို သုံးနှုန်းခြင်းအကြောင်း ဆွေးနွေးချက်
- Vohārakathā = ပြောဆို သုံးနှုန်းခြင်းအကြောင်း ဆွေးနွေးချက်
- buddhassa bhagavato vohāro = ဘုရားရှင် မြတ်စွာဘုရား၏ ပြောဆို သုံးနှုန်းခြင်း
- (20) 11. Nirodhakathā = (20) 11. ချုပ်ငြိမ်းခြင်းအကြောင်း ဆွေးနွေးချက်
- Nirodhakathā = ချုပ်ငြိမ်းခြင်းအကြောင်း ဆွေးနွေးချက်
- tāṇa / leṇa / saraṇa / parāyaṇa / accuta / amata = ကာကွယ်ရာ / ပုန်းအောင်းရာ / ကိုးကွယ်ရာ / မှီခိုရာ / မစုတေသော အရာ / အမြိုက်

## Unsure Pāli / interpretation (for the reviewer)
- ch6 «Atītaṃ khandhāti?» read «the past is aggregates» («အတိတ်သည် အစုအဝေးတို့ ဖြစ်သလော»); «…natthi cete» =
  «… ဖြစ်ကြ၍ ထိုအရာတို့ မရှိ».
- ch6 the nirutti sutta (elided): «ဤ သုံးပါးတို့ကား စကားဖြင့် ဖော်ပြမှု၏ လမ်းကြောင်း၊ အမည်ခေါ်ဝေါ်မှု၏ လမ်းကြောင်း၊
  သတ်မှတ်ချက်… ပညာရှိတို့…» (pi-1 dyad words).
- ch8 ekāyanamaggo «တစ်ကြောင်းတည်းသော လမ်း», bodhagāmī «ဗောဓိဆီသို့ ဦးတည်သော», kāyagatāsati «ကိုယ်ကို အာရုံပြုသော
  သတိ», X-paṭṭhāna (phassa / citta) «X ပဋ္ဌာန်» (mirrors satipaṭṭhāna); upaṭṭhitasatino … samohitā rendered as a list
  of persons.
- ch9 heva atthi = «တစ်နည်းအားဖြင့် ရှိ»; sevatthi seva natthi = «ထိုအရာပင် ရှိသည်၊ ထိုအရာပင် မရှိ»; «X Y-ti hevatthi» =
  «Xသည် Y အနေဖြင့် တစ်နည်းအားဖြင့် ရှိ»; atthaṭṭha / atthibhāva «ရှိခြင်း၏ အနက် / အဖြစ်».
- ch10 Parūpahāra: asuci sukkavissaṭṭhi «မစင်ကြယ်သော သုက်ထွက်ခြင်း»; tassa (āsayo) = «ထိုအရာ၏» (of the semen /
  excrement), elsewhere tassa = «ထိုသူ၌»; mārakāyikā devatā «မာရ်နတ်၏ အပေါင်းအပါ နတ်တို့»; attano / aññesaṃ / tassa
  asuciṃ = the deities' own / others' / the arahant's.
- ch10 the crimes list (sandhiṃ chindeyya «အိမ်ကို ဖောက်ရာ», nillopaṃ hareyya «ဥစ္စာကို လုယူရာ», ekāgāriyaṃ kareyya
  «အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်ရာ», paripanthe tiṭṭheyya «လမ်းခရီး၌ ဓားပြ တိုက်ရာ»); arahant epithets
  (ukkhittapaligho, saṅkiṇṇaparikho, abbūḷhesiko, niraggaḷo) best guesses.
- ch10 «Saññāsamuṭṭhānā vācā vuttā bhagavatā – tatiyaṃ jhānaṃ…» (^5-332, no quotation marks in the Pāli): the rule
  sets the quotation marks of the parallel line (both clauses quoted).
- ch10 «Nanu "paṭhamaṃ jhānaṃ … niruddhā hotī"ti!» (no vuttaṃ) = «“…”ဟူ၍ ဟောထားသည် မဟုတ်လော» (verb supplied).
- ch10 Kukkuḷa: kukkuḷa «ပြာပူ»; sabbe saṅkhārā «ပြုပြင်ဖန်တီးမှု အားလုံးတို့»; anodhiṃ katvā «ချွင်းချက် မထားဘဲ»;
  the 28 kinds of sukha (upadhi «ဥပဓိ», sāmisa «ကာမဂုဏ်နှင့် စပ်သော»).
- ch10 Anupubbābhisamaya: catubhāgaṃ «လေးပုံတစ်ပုံ»; the «catubhāgaṃ X … na Y» lists rendered as one clause ending in
  the last (negative) verb; «na uddhaṃsoto na akaniṭṭhagāmī» vs «na uddhaṃsoto akaniṭṭhagāmī» (two Pāli forms) kept
  apart; vohāra «ပြောဆို သုံးနှုန်းခြင်း» (termbase); elaṇḍa «ကြက်ဆူပင်».
- ch10 Nirodha: paṭisaṅkhā- / appaṭisaṅkhāniruddha «ပြန်လည် ဆင်ခြင်၍ / ပြန်လည် မဆင်ခြင်ဘဲ ချုပ်ငြိမ်းသော»; tāṇa …
  amata «ကာကွယ်ရာ … အမြိုက်».

## Source slips (translated as written; Pāli not changed)
- ch8 ^5-303 «Attheva suttantoti? Āmantā?»: «ဟုတ်ပါသည်။» (module frame).
- ch9 ^5-305 «Na hevaṃ vattabbe.…Pe….» = «ဤသို့ မဆိုသင့်ပါ။ …»; ^5-306 «rūpaṃ vedanāti hevaṃ natthi» (hevaṃ for heva):
  as heva; ^5-306 line «Na vattabbaṃ – "rūpaṃ hevatthi, …» the quotation never closes: the sentences cut by hand
  (OPEN_Q), the quotation closed after its «ti».
- ch10 ^5-321 «…nāme kaṅkheyyā"ti?» and ^5-352 «Na vattabbaṃ – "buddhassa … hotīti?» stray / unclosed quotation
  marks: cut by hand (OPEN_Q), regular marks.
- ch10 ^5-322 «idapaccayatā…» (single p): the same Burmese as idappaccayatā.
- ch10 ^5-323 «Hañci arahā vītarāgo vītadoso vītamoho sacchikātabbaṃ sacchikataṃ» (no …pe…): as written.
- ch10 ^5-333 the Abhibhū verse closes «…karissatī"’ti» (closing order) and the first stanza never closes its ‘…’:
  regular ’” order, the first stanza's ‘…’ closed at its end.
- ch10 ^5-338 «Hañci brahmacariyaṃ … sukhavipākanti, no ca vata re»: «ti» inside the condition, as written.
- ch10 kaṇḍako / kaṇṭako (^5-332): both = «ဆူးငြောင့်».
