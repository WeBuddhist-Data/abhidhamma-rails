# pi-4 Burmese zero-shot, chapters 6 … 11 (Pañcaka … Dasakapuggalapaññatti): notes

Status: DONE 2026-11-19. Brief: burmese-zeroshot-brief.md. Not committed. Source: the Pāli only.

## Files
- Output: `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/` 6-pancakapuggalapannatti.md (12 segments,
  34 lines), 7-chakka… (2, 8), 8-sattaka… (5, 12), 9-atthaka… (2, 3), 10-navaka… (2, 11), 11-dasaka… (2, 6).
- `make_ch6-11.py` (generator; imports my4_formulas and make_sample read only, extends their tables in memory),
  `check_ch6-11.py` (own check + reuse test). Run: `python3 -I -X utf8 make_ch6-11.py`, then `check_ch6-11.py`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all six files (chk-pe copies deleted).
- check_ch6-11.py: A 6/6 regenerated identical; B1 74 lines; B2 65 numbers; B3 106 negations; B5 37 names / verb
  phrases; 0 mismatches. Reuse 75 / 75 (C3 terms and clauses vs pi-1/2/3 final 71/71; C4 repeated Pāli lines within
  pi-4 4/4). Mutation-tested (a changed number and a dropped «မ» are caught).

## Method
- Every unit goes through my4_formulas (Q_RE, V_RE, SENT …); this script adds SENT entries built from frames
  (the four admonished persons, the five warriors / five monks, the two ascetic lists, the six of ch7, the ch2
  definitions with ch8 / ch10 punctuation) and three EXTRA_RULES (Kathañca / Evaṃ / unquoted Ayaṃ vuccati).
- Reused and witnessed (pi-2 ^2-508 word for word where the Pāli is the same): «So vivittaṃ senāsanaṃ …», «So
  araññagato vā …», the five hindrance sentences (joined by «၊» where ch6 has «;»), «So ime pañca nīvaraṇe … paṭhamaṃ
  jhānaṃ … vitakkavicārānaṃ vūpasamā»; ^2-831 «āsavānaṃ khayā anāsavaṃ … upasampajja» (without the honorific
  «တော်မူ», said of the Tathāgata there); ^2-957 «sikkhaṃ paccakkhāya hīnāyāvattati», «yenakāmaṃ pakkamati»,
  «āyasmā», the quote frame «… – “…”ဟု။»; ^2-865 «pāpiccho icchāpakato»; ^2-849 the four requisites; ^2-643
  «Seyyathāpi … evameva»; ^2-760 «Puna caparaṃ», «āsavānaṃ khayaṃ»; pi-1 kāmāsava / bhavāsava / avijjāsava.
- Sample strings reused as they are: the mātikā predicates of pañcaka (1) and chakka (1) (from PRED_M), the mātikā
  names of pañcaka (2) and sattaka (1) as verb phrases, STREAM / ANAGAMI (with «ထိုသူသည်» for «So»), the ch2
  definitions (UNIQUE / SENT), the aṭṭhaka and dasaka mātikā lines.

## New frames and recurring strings («Pāli = Burmese»)
Kathañca puggalo X? = ပုဂ္ဂိုလ်သည် အဘယ်သို့ Vသနည်း။ (V = the mātikā name as a verb phrase)
Evaṃ puggalo X. = ဤသို့ ပုဂ္ဂိုလ်သည် V၏။
Ayaṃ vuccati puggalo X. (no quotes in the Pāli, ch8 / ch10) = ဤပုဂ္ဂိုလ်ကို “X”ဟု ခေါ်သည်။ (the sample frame, quotes kept)
Tatra / Tattha = ထိုတို့အနက်
Tattha katame pañca X puggalā? = ထိုတို့အနက် X ပုဂ္ဂိုလ် ငါးယောက် ဟူသည် အဘယ် ပုဂ္ဂိုလ်တို့နည်း။
Katame pañca? = အဘယ် ငါးယောက်တို့နည်း။
Tatra yvāyaṃ puggalo P, so evamassa vacanīyo – "…"ti. = ထိုတို့အနက် အကြင် ပုဂ္ဂိုလ်သည် P၊ ထိုပုဂ္ဂိုလ်ကို ဤသို့ ပြောဆိုသင့်၏ – “…”ဟု။
Tatra yvāyaṃ puggalo P, X tena daṭṭhabbo. = ထိုတို့အနက် အကြင် ပုဂ္ဂိုလ်သည် P၊ Xကို ထိုသို့ သိမှတ်ရမည်။
āyasmato … saṃvijjanti / na saṃvijjanti = အသျှင်၌ … ရှိကုန်၏ / မရှိကုန်
ārambhaja = မှားယွင်းစွာ ပြုမူခြင်းမှ ဖြစ်သော
vippaṭisāraja = နောင်တ ပူပန်မှုမှ ဖြစ်သော
pavaḍḍhanti / nappavaḍḍhanti = ပို၍ ပို၍ တိုးပွားကုန်၏ / ပို၍ ပို၍ မတိုးပွားကုန်
paṭivinodetvā = ဖယ်ရှားပြီး
Sādhu vatāyasmā … bhāvetu = အသျှင်သည် … ပွားများလျှင် ကောင်းလေစွ
cittaṃ paññañca = စိတ်ကိုလည်း ပညာကိုလည်း
amunā pañcamena puggalena samasamo bhavissati = ထို ပဉ္စမ ပုဂ္ဂိုလ်နှင့် တန်းတူ ဖြစ်လိမ့်မည်
evaṃ ovadiyamānā evaṃ anusāsiyamānā anupubbena = ဤသို့ ဆုံးမခံရ၍ ဤသို့ သွန်သင်ခံရသဖြင့် အစဉ်အတိုင်း
tassa evaṃ hoti = ထိုသူ၌ ဤသို့ အကြံ ဖြစ်၏
paṭiggaṇhāti = လက်ခံ၏
saṃvasati = အတူ နေ၏; vassāni = နှစ် (dve vā tīṇi vā = နှစ်နှစ်ဖြစ်စေ၊ သုံးနှစ်ဖြစ်စေ)
khippaññeva adhimuccitā = လျင်မြန်စွာပင် ယုံကြည်လိုက်သူ
ittara- = ခဏတာသာ; bhatti = ကိုးကွယ်ခြင်း (pi-2); pema = ချစ်ခင်မှု; pasāda = ကြည်ညိုမှု
sāvajjānavajja = အပြစ် ရှိသော အပြစ် မရှိသော; hīnappaṇīta = ယုတ်ညံ့သော မွန်မြတ်သော; kaṇhasukkasappaṭibhāga = မည်းနက်သော ဖြူစင်သော ဆန့်ကျင်ဘက် ရှိသော
yodhājīva = စစ်သည် (sample GROUP); rajagga = ဖုန်လုံး; dhajagga = အလံဖျား; ussāraṇa = ကြွေးကြော်သံ; sampahāra = ထိပ်တိုက် တိုက်ခိုက်ခြင်း
saṃsīdati visīdati na santhambhati = စိတ်ဓာတ် ကျဆင်း၏၊ အားလျော့၏၊ ခိုင်ခိုင်မာမာ မရပ်တည်နိုင်
na sakkoti saṅgāmaṃ otarituṃ = စစ်ပွဲသို့ မဝင်နိုင်
sahati X = Xကို သည်းခံနိုင်၏; api ca kho = သို့သော်
haññati byāpajjati = အသတ်ခံရ၏၊ ဒဏ်ရာ ရ၏
So taṃ saṅgāmaṃ abhivijinitvā vijitasaṅgāmo tameva saṅgāmasīsaṃ ajjhāvasati = ထိုသူသည် ထိုစစ်ပွဲကို အောင်နိုင်၍ စစ်ပွဲကို အောင်ပြီးသူ ဖြစ်ကာ ထိုစစ်ပွဲ၏ ရှေ့တန်းကိုပင် အုပ်စိုး နေ၏
Evarūpopi idhekacco X hoti = ဤလောက၌ အချို့သော Xသည်လည်း ဤသို့ သဘောရှိသူ ဖြစ်၏
santo saṃvijjamāno lokasmiṃ / bhikkhūsu = လောက၌ / ရဟန်းတို့အထဲ၌ ထင်ရှား ရှိနေသော
paṭhamo … pañcamo = ပထမ … ပဉ္စမ (pi-2 ordinals)
Seyyathāpi so X …, tathūpamo ayaṃ puggalo = ဥပမာအားဖြင့် ထို X သည် …သကဲ့သို့၊ ဤပုဂ္ဂိုလ်သည် ထို Xနှင့် တူ၏
Kimassa X? / Idamassa X. = ထိုရဟန်းအတွက် X ဟူသည် အဘယ်နည်း။ / ဤသည်ကား ထိုရဟန်းအတွက် X ဖြစ်၏။
saṅgāmavijaya = စစ်ပွဲ၌ အောင်နိုင်ခြင်း
brahmacariyaṃ sandhāretuṃ (na sakkoti) = မြင့်မြတ်သော အကျင့်ကို ဆက်လက် (မ)ထိန်းသိမ်းနိုင်
sikkhādubbalyaṃ āvikatvā = သိက္ခာ၌ အားနည်းချက်ကို ထုတ်ဖော်၍; dubbalyaṃ anāvikatvā = အားနည်းချက်ကို မထုတ်ဖော်ဘဲ; sikkhaṃ appaccakkhāya = သိက္ခာကို မစွန့်ဘဲ
Idha bhikkhu = ဤသာသနာ၌ ရဟန်းသည် (pi-2); idhekacco bhikkhu = ဤလောက၌ အချို့သော ရဟန်းသည် (idhekacco as the sample)
asukasmiṃ nāma = ဤမည်သော (pi-2 itthannāma); gāma / nigama = ရွာ / နိဂုံး; itthī / kumārī = မိန်းမ / အပျို; mātugāma = အမျိုးသမီး
abhirūpā dassanīyā pāsādikā paramāya vaṇṇapokkharatāya samannāgatā = အဆင်းလှသော၊ ရှုချင်ဖွယ် ကောင်းသော၊ ကြည်ညိုဖွယ် ကောင်းသော၊ အလွန် ကောင်းမွန်သော အသားအရေနှင့် အပြည့်အဝ ပြည့်စုံသော
ūhasati ullapati ujjagghati uppaṇḍeti = ပြုံးရယ်၏၊ စကား ပြောဆို ချော့မော့၏၊ ကျယ်လောင်စွာ ရယ်မော၏၊ ကျီစယ် ပြက်ရယ်ပြု၏
abhinisīdati abhinipajjati ajjhottharati = အနီး၌ ထိုင်၏၊ အနီး၌ လှဲလျောင်း၏၊ ဖိ၍ အုပ်မိုး၏
methunaṃ dhammaṃ paṭisevati = မေထုန် အကျင့်ကို မှီဝဲ၏
viniveṭhetvā vinimocetvā = ရုန်းထွက်၍ လွတ်မြောက်အောင် ပြုပြီး
evaṃ samāhite citte parisuddhe pariyodāte anaṅgaṇe vigatūpakkilese mudubhūte kammaniye ṭhite āneñjappatte = ဤသို့ စိတ် တည်ကြည်၍ စင်ကြယ်ပြီး၊ ဖြူစင်ပြီး၊ အညစ်အကြေး မရှိဘဲ၊ ညစ်နွမ်းမှု ကင်း၍၊ နူးညံ့ပြီး၊ အလုပ်ပေးရ လွယ်ကူပြီး၊ တည်တံ့၍ မတုန်လှုပ်သည့် အခြေသို့ ရောက်သောအခါ
āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti = စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းကို သိသော ဉာဏ်အတွက် စိတ်ကို ရှေးရှု ညွှတ်၏
ime āsavā / āsavasamudayo / āsavanirodho / āsavanirodhagāminī paṭipadā = စိတ်အစွန်းအထင်းတို့ / … ဖြစ်ပေါ်ခြင်း / … ချုပ်ငြိမ်းခြင်း / … ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ် (the dukkha pattern of ^4-27)
X-āsavāpi cittaṃ vimuccati = X စိတ်အစွန်းအထင်းမှလည်း (စိတ်သည်) လွတ်မြောက်၏
Vimuttasmiṃ vimuttamiti ñāṇaṃ hoti = လွတ်မြောက်သောအခါ “လွတ်မြောက်ပြီ”ဟု သိသော ဉာဏ် ဖြစ်၏
Khīṇā jāti, vusitaṃ brahmacariyaṃ, kataṃ karaṇīyaṃ, nāparaṃ itthattāya = မွေးဖွားခြင်း ကုန်ပြီ၊ မြင့်မြတ်သော အကျင့်ကို ကျင့်ပြီးပြီ၊ ပြုဖွယ် ကိစ္စကို ပြုပြီးပြီ၊ ဤအဖြစ်အတွက် နောက်ထပ် ပြုဖွယ် မရှိတော့ပြီ
mandattā momūhattā = ထုံထိုင်းခြင်း၊ အလွန် တွေဝေခြင်းကြောင့်; ummādā cittavikkhepā = ရူးသွပ်ခြင်း၊ စိတ် ပျံ့လွင့်ခြင်းကြောင့်
"vaṇṇitaṃ buddhehi buddhasāvakehī"ti = “ဘုရားရှင်တို့နှင့် ဘုရားရှင်၏ တပည့်တို့ ချီးမွမ်းထားသည်”ဟု
api ca (ascetics) = ထို့ပြင်
appicchatā / santuṭṭhi / sallekha / idamatthitā (…yeva nissāya) = အလိုနည်းခြင်း / ရောင့်ရဲမှု / ကိလေသာကို ခြစ်ခွာခြင်း / ဤမျှဖြင့် လုံလောက်ခြင်း (ကိုသာ မှီ၍)
aggo ca seṭṭho ca pāmokkho ca uttamo ca pavaro ca = အမြတ်ဆုံးလည်း၊ အကောင်းဆုံးလည်း၊ အကြီးမှူးလည်း၊ အထွတ်အထိပ်လည်း၊ အမွန်မြတ်ဆုံးလည်း ဖြစ်၏
gavā khīraṃ … sappimaṇḍaṃ tattha aggamakkhāyati = နွားမှ နွားနို့ … ထောပတ်ကြည် အနှစ် … အမြတ်ဆုံးဟု ဆိုကြသကဲ့သို့ (khīra, dadhi, navanīta, sappi = pi-2)
sāriputtamoggallānā = သာရိပုတ္တရာနှင့် မောဂ္ဂလ္လာန်တို့; avasesā arahantā = ကြွင်းကျန်သော ရဟန္တာတို့; sotāpannasakadāgāmino = သောတာပန်နှင့် သကဒါဂါမ်တို့
ummujjati "sādhu saddhā kusalesu dhammesu …"ti = “ကုသိုလ် သဘောတရားတို့၌ ယုံကြည်မှုသည် ကောင်း၏ …”ဟု သဘောထား၍ ပေါ်လာ၏
neva tiṭṭhati no vaḍḍhati hāyatiyeva = မတည်တံ့၊ မတိုးပွား၊ ယုတ်လျော့သာ ယုတ်လျော့၏; neva hāyati no vaḍḍhati ṭhitā hoti = မယုတ်လျော့၊ မတိုးပွား၊ တည်နေ၏
ekantakāḷaka = လုံးဝ မည်းနက်သော
Katamesaṃ pañcannaṃ idha (vihāya) niṭṭhā? = အဘယ် ငါးယောက်တို့၏ ပြီးမြောက်ခြင်းသည် ဤလောက၌ (ဤလောကကို စွန့်ခွာပြီးမှ) ဖြစ်သနည်း။
yo ca diṭṭheva dhamme arahā = (…နှင့်) မျက်မှောက်ဘဝ၌ပင် ရဟန္တာ ဖြစ်သူ
Ettāvatā puggalānaṃ puggalapaññattīti = ဤမျှသည် ပုဂ္ဂိုလ်တို့၏ ပုဂ္ဂိုလ် သတ်မှတ်ချက် ဖြစ်သည်။ (yavata_my pattern)
Variant labels (added in memory to VAR_KIND): ārabbhajā, satthambhati, āvīkatvā, uhasati, idamaṭṭhitaṃyeva, nonītaṃ, sāhu, viriyaṃ = စာလုံးပေါင်းကွဲ; ayaṃ pana, ussādanaṃyeva, ussādanaññeva, santānetuṃ, sāmaṃyeva, appicchaṃyeva, mokkho, dukkhassantaṃ karoti = ပါဌ်ကွဲ
Several readings in one bracket = «[L (S1): a၊ (S2): b၊ ref]» (pi-2 ^2-832); sigla aṭṭhakathā = (အဋ္ဌကထာ) (pi-2 ^2-811); evamuparipi = နောက်တွင်လည်း ဤနည်းတူ (pi-2 ^2-796); evaṃ tīsu ṭhānesupi = နေရာ သုံးခုလုံး၌လည်း ဤနည်းတူ (new)

## Choices to review (unsure Pāli / harmonise)
- vippaṭisāra(ja) keeps the sample's «နောင်တ ပူပန်…» (vippaṭisārī), which is also pi-1 / pi-2 kukkucca «နောင်တ
  ပူပန်မှု» (pi-1 ^1-1166 renders cetaso vippaṭisāro «စိတ်၏ နောင်တ ရခြင်း»); the harmonise pass may separate them.
- agga / uttama: the termbase gives «အမြတ်ဆုံး» for both; in the synonym list uttama = «အထွတ်အထိပ်» (one word each).
- «ummujjitvā vipassati viloketi» as a verb phrase: «… သေချာစွာ မြင်၍ ပတ်ဝန်းကျင်ကို ကြည့်» (mātikā «မြင်၏၊»).
- «tena daṭṭhabbo» read as "is to be understood thus / by this": «Xကို ထိုသို့ သိမှတ်ရမည်»; also with the plural
  examples (Sāriputta and Moggallāna, the other arahants, stream-enterers and once-returners).
- ummujjati "…"ti: the thought is rendered «“…”ဟု သဘောထား၍ ပေါ်လာ၏» (minor clarification «သဘောထား၍»).
- sallekha «ကိလေသာကို ခြစ်ခွာခြင်း» (clarifying object added); idamatthitā «ဤမျှဖြင့် လုံလောက်ခြင်း».
- rajagga / dhajagga / ussāraṇa / sampahāra (simile words) and saṅgāmasīsa «ရှေ့တန်း»; haññati byāpajjati «အသတ်ခံရ၏၊
  ဒဏ်ရာ ရ၏».
- «parassa vaṇṇe vā avaṇṇe vā bhāsiyamāne» = «သူတစ်ပါးကို ချီးမွမ်း၍ဖြစ်စေ၊ ကဲ့ရဲ့၍ဖြစ်စေ ပြောဆိုနေစဉ်».
- In the ch8 arahant sentence the pi-2 ^2-831 Burmese is used without «တော်မူ» (honorific of the Buddha there).

## Source slips (translated as written)
- ^4-191 line 4: «yatthassa te pāpakā …» lacks «uppannā» (lines 1-3 and the mātikā have it): «ဖြစ်ပေါ်ပြီးသော» left out.
- ^4-191: the chapter opens with «Tatra yvāyaṃ puggalo …» (no question); lines 2-4 «ārabhati na vippaṭisārī hoti»,
  «na ārabhati …» differ in «ca» / «nārabhati» from the mātikā; the Burmese of the mātikā predicates is kept.
- ^4-198 line 2: «abyāpannacitto viharati, sabbapāṇabhūtahitānukampī byāpādapadosā …» (pi-2 ^2-508 has the comma
  after «sabbapāṇabhūtahitānukampī»); the hindrance sentences are joined by «;» (pi-2 «.»): pi-2 Burmese kept, «၊»
  for «;».
- ^4-200 «pañca rukkhamūlikā …pe…» has a space before the ellipsis; the last «…pe….» ends the line.
- ^4-203 «sāhu saddhā» first, then «sādhu [sāhu (sī. syā.) …]»: both «ကောင်း၏»; «patigādhappatto» (mātikā
  «paṭigādhappatto»): same name; «dukkhassantakaro hoti» here vs «dukkhassantaṃ karoti» in ch2 ^4-34: sample _DUK
  «ဒုက္ခ၏ အဆုံးကို ပြုသူ ဖြစ်၏»; the anāgāmī sentence lacks the comma after «opapātiko hoti»: same Burmese.
- ^4-204 / ch10: «viharati paññāya» without «;», «Ayaṃ vuccati puggalo X.» without quotes, after a full stop; ch10
  joins the diṭṭhippatta / saddhāvimutta sentences with commas and abbreviates the four truths with «…pe…».
- ^4-205 «dhammānusārī ….» has a space before the ellipsis (Marathi notes too).
- ^4-206 / ^4-208 «… phale ṭhito saddhāvimuttoti.» (closing «ti»; ch2 has no «ti») and a comma after
  «saddhānusārī» / «dhammānusārī»: the ch2 Burmese is kept.
- ^4-202 line 6: «āgantā itthattaṃ» without «āgāmī hoti» (the mātikā has it): rendered without «ပြန်လာသူ ဖြစ်၏».
