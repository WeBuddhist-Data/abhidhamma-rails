# pi-2 Burmese zero-shot, chapters 15-16: working notes

Scope: 15-patisambhidavibhango, 16-nanavibhango. Brief: burmese-zeroshot-brief.md. Pāli only; no Burmese translation
or nissaya consulted; my2_formulas.py, my2-zeroshot-terms.md and pi-1-my/ read only.

## Status
- [x] 15-patisambhidavibhango.md: 49 segments; three verifications OK; check_ch15-16.py 0 mismatches; pi-1 reuse 23 / 23.
- [x] 16-nanavibhango.md: 103 segments; three verifications OK; check_ch15-16.py 0 mismatches; pi-1 reuse 17 / 17.
- chk-pe copies of both chapters deleted. check_ch15-16.py = check_sample.py + chapter 15-16 tables (negation
  privatives, number words, brackets with notes / two sigla groups, «(1. Ka)» labels not counted as sentence ends).
- Regenerate: `python3 -I -X utf8 make_ch15-16.py [chapter]`. Check: `check_ch15-16.py <pāli> <my> …`. Nothing committed.

## Method
- make_ch15-16.py imports my2_formulas (pi-1 final module + sample tables). Own clause engine tr(): FIX (exact phrase
  table, longest first) then FRAMES (regex functions); unmatched text raises Miss.
- Cittuppāda openings (ch. 15 abhidhamma part): the final pi-1 Burmese, looked up sentence by sentence in the pi-1 rails
  text (p1_open); where pi-1 has no identical opening, built from pi-1 pieces (FIX_OPEN, r_open_single / r_open_multi
  in the pi-1 2-04 / 2-05 forms).
- Ch. 15 pañhāpucchaka: the sample engine (F.clauses_my) with the paṭisambhidā subjects added to F.KH in memory and a
  few EXTRA_RULES (capital Siyā, «na vattabbā» without dash, unquoted «-tipi» lists, «X ceva Y cāti», free «na T»).

## New strings («Pāli = Burmese»)
paṭisambhidā = ပိုင်းခြားသိသော ဉာဏ်
catasso / tisso / dve paṭisambhidā = ပိုင်းခြားသိသော ဉာဏ် လေးပါး / သုံးပါး / နှစ်ပါး
attha (paṭisambhidā chapter) = အကျိုးအနက်
dhamma (in dhammapaṭisambhidā, Dhamme ñāṇaṃ, dhammaniruttābhilāpa) = တရား
paṭibhāna = ဉာဏ်ပေါ်မှု
atthapaṭisambhidā = အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်
dhammapaṭisambhidā = တရားကို ပိုင်းခြားသိသော ဉာဏ်
niruttipaṭisambhidā = စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်
paṭibhānapaṭisambhidā = ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်
X-e ñāṇaṃ = Xကို သိသော ဉာဏ် (pi-1 Dukkhe ñāṇaṃ)
«X-e ñāṇaṃ Y-paṭisambhidā» = Xကို သိသော ဉာဏ်သည် Y ဖြစ်သည်
Atthe ñāṇaṃ = အကျိုးအနက်ကို သိသော ဉာဏ်
dhamme ñāṇaṃ = တရားကို သိသော ဉာဏ်
ñāṇesu ñāṇaṃ = ဉာဏ်တို့ကို သိသော ဉာဏ်
tatra dhammaniruttābhilāpe ñāṇaṃ = ထိုအရာ၌ တရား၏ စကားဖြင့် ဖော်ပြမှုကို ခေါ်ဆိုခြင်းကို သိသော ဉာဏ်
hetu (cause, Hetuvāra) = အကြောင်းရင်း; hetuphala = အကြောင်းရင်း၏ အကျိုး (mātikā hetu stays အမြစ်)
jarāmaraṇa = အိုခြင်းနှင့် သေခြင်း (pi-1 links of ^1-1343; the four truths as pi-1 moho list)
imesu dhammesu / tesu dhammesu = ဤသဘောတရားတို့ / ထိုသဘောတရားတို့; tesaṃ vipāke = ထိုသဘောတရားတို့၏ အကျိုး
yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti = အကြင် စကားဖြင့် ဖော်ပြမှုဖြင့် ထိုသဘောတရားတို့၏ သတ်မှတ်ချက် ဖြစ်၏
Yena ñāṇena tāni ñāṇāni jānāti – "imāni ñāṇāni idamatthajotakānī"ti = အကြင် ဉာဏ်ဖြင့် ထိုဉာဏ်တို့ကို သိ၏ – “ဤဉာဏ်တို့သည် ဤအကျိုးအနက်ကို ထင်ရှားစေကြသည်”ဟု
yamhā dhammā te dhammā L = အကြင် သဘောတရားမှ ထိုသဘောတရားများ L(stems) ဖြစ်ကြ၏
Ayaṃ X-vāro = ဤသည်မှာ X ဖော်ပြချက် ဖြစ်သည်
Saṅgahavāro = အကျဉ်းချုပ် ဖော်ပြချက်; Saccavāro = သစ္စာအလိုက် ဖော်ပြချက်; Hetuvāro = အကြောင်းရင်းအလိုက် ဖော်ပြချက်;
Dhammavāro = သဘောတရားအလိုက် ဖော်ပြချက်; Paṭiccasamuppādavāro = အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံအလိုက် ဖော်ပြချက်;
Pariyattivāro = ပရိယတ္တိအလိုက် ဖော်ပြချက်; Kusalavāro / Akusalavāro = ကုသိုလ်အလိုက် / အကုသိုလ်အလိုက် ဖော်ပြချက်;
Vipākavāro = ကံ၏ အကျိုးအလိုက် ဖော်ပြချက်; Kiriyavāro = ပြုရုံမျှသာ ဖြစ်သော စိတ်အလိုက် ဖော်ပြချက်
Paṭisambhidāvibhaṅgo = ပိုင်းခြားသိသော ဉာဏ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Ñāṇavibhaṅgo = ဉာဏ်ကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Idha bhikkhu = ဤသာသနာတော်၌ ရဟန်းသည်; jānāti = သိသည် (mid-sentence before a quote: သိ၏)
the nine aṅgas (names): သုတ်၊ ဂေယျ၊ ဝေယျာကရဏ၊ ဂါထာ၊ ဥဒါန်း၊ ဣတိဝုတ်၊ ဇာတ်၊ အဗ္ဘုတဓမ္မ၊ ဝေဒလ္လ
bhāsita = ဟောပြောချက်
kāmāvacarakusalato / kiriyato = ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်ထဲမှ / ပြုရုံမျှသာ ဖြစ်သော စိတ်ထဲမှ
cittuppāda = စိတ် ဖြစ်ပေါ်မှု (pi-1 5-atthakatha)
evamuparipi (variant note) = နောက်တွင်လည်း ဤနည်းတူ; passa dīghanikāye = “ဒီဃနိကာယ်”ကို ကြည့်ပါ
dhātuvibhaṅge pana pāṭhanānattaṃ natthi = “ဓာတ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း”၌ကား ပါဌ် ကွဲပြားမှု မရှိ (title of ch. 3
  assumed; align with the ch. 3 agent)
akusala qualifiers, kusala / akusala multi-citta openings: pi-1 2-04 forms (see FIX_OPEN / r_open_multi)
na T (free na, no table entry) = T သဘောတရား(များ) မဟုတ်(ကြ)
unquoted «X-tipi, Y-tipi» after na vattabbā = X သဘောတရား(များ)ဟုလည်းကောင်း၊ … ခေါ်ဆို၍ မရ
feminine -inī (ācayagāminī, maggādhipatinī, uppādinī …) = the pi-1 -ino terms

## New strings, chapter 16 («Pāli = Burmese»)
ñāṇavatthu = ဉာဏ် အခြေခံ (pi-1 kilesavatthu = ကိလေသာ အခြေခံ); Xvidhena ñāṇavatthu – = Nမျိုးဖြင့် ကြည့်လျှင် ဉာဏ် အခြေခံ –
Evaṃ Xvidhena ñāṇavatthu. = ဤသို့ Nမျိုးဖြင့် ကြည့်လျှင် ဉာဏ် အခြေခံ ဖြစ်သည်။ (sample VIDHA / LOOK / EVAM)
Ekaka- … Dasakamātikā = တစ်မျိုးတွဲ … ဆယ်မျိုးတွဲ ခေါင်းစဉ်စာရင်း; Catukka- … Dasakaniddeso = လေးမျိုးတွဲ … ဆယ်မျိုးတွဲ အကျယ် ဖော်ပြချက် (pi-1 pattern)
T paññā = T ပညာ (T = pi-1 mātikā term); «A paññā B paññā» = A ပညာသည် B ပညာ ဖြစ်သည်; «X paññā atthi T» = X ပညာတွင် T ပညာ ရှိသည်
āsavavippayuttā sāsavā paññā (and the other families) = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော၊ … အာရုံ ဖြစ်နိုင်သော ပညာ
pañca viññāṇā = သိစိတ် ငါးပါး; their ekaka list = the pi-1 Rūpakaṇḍa ^1-594 form (C3 eka_attr; -meva = …သည်ပင်)
vatthu = မှီရာ; ārammaṇa = အာရုံ; purejāta = ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော; asambhinna = မပျက်စီးသေးသော; nānā- = အသီးသီး ကွဲပြားသော
ajjhattika / bāhira = အတွင်းပိုင်း / ပြင်ပ (pi-1); gocaravisaya = ကျက်စားရာ နယ်ပယ်; paccanubhoti = ခံစား
samannāhāra = အာရုံသို့ စိတ်ညွတ်ခြင်း; ābhoga = ဆင်ခြင်ခြင်း; āvaṭṭanā = စိတ်ကို လှည့်ဆောင်ခြင်း; manasikāra = နှလုံးသွင်းခြင်း (pi-1)
abbokiṇṇa = ကြားမပြတ် ဆက်တိုက်; apubbaṃ acarimaṃ = ရှေ့ မရှိ၊ နောက် မရှိဘဲ; samanantarā = ချက်ချင်း နောက်၌; ekakkhaṇe = တစ်ခဏတည်း၌
abhinipāta / āpāta = အာရုံ ကျရောက် / အာရုံ ရှေ့သို့ ရောက်လာ; paṭivijānāti = ပိုင်းခြား၍ သိ; iriyāpatha = ဣရိယာပုထ်
gamana / ṭhāna / nisajjā / seyyā = သွားခြင်း / ရပ်ခြင်း / ထိုင်ခြင်း / လျောင်းခြင်း; samādiyati = ဆောက်တည်
samāpajjati / vuṭṭhāti = ဝင်စား / ထမြောက်; cavati = သေ (pi-1 cuti); supati / paṭibujjhati / supina = အိပ် / နိုး / အိပ်မက်
yāthāvakavatthuvibhāvanā paññā = အရာဝတ္ထုကို ဟုတ်မှန်သည့်အတိုင်း ထင်ရှားစေသော ပညာ
«X-ti Y» (niddesa gloss) = X ဟူသည် Y (pi-1 ^1-1382)
cintāmayā / sutamayā / bhāvanāmayā = စဉ်းစားခြင်းမှ / ကြားနာခြင်းမှ / ဘာဝနာ ပွားများခြင်းမှ ဖြစ်သော; dānamayā / sīlamayā = ပေးလှူခြင်းမှ / သီလမှ ဖြစ်သော
adhisīla / adhicitta / adhipaññā = လွန်မြတ်သော သီလ / စိတ် / ပညာ; X-e paññā = X၌ ရှိသော ပညာ
āya- / apāya- / upāyakosalla = တိုးတက်ရာ၌ / ဆုတ်ယုတ်ရာ၌ / နည်းလမ်း၌ ကျွမ်းကျင်ခြင်း (pi-1 kosalla)
tīsu / catūsu bhūmīsu = ဘုံ သုံးပါး / လေးပါး၌ ဖြစ်သော; kusalābyākata = ကုသိုလ် သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ်၊ … သဘောတရား (sample QV)
kiriyābyākata = ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား; catūsu maggesu / phalesu = မဂ် / ဖိုလ် လေးပါးတို့၌
atthajāpikā / jāpitatthā = အကျိုးကို ဖြစ်စေတတ်သော / ဖြစ်စေပြီးသော; upariṭṭhima arahattaphala = အမြင့်ဆုံး ဖြစ်သော အရဟတ္တဖိုလ်
yogavihita = ပညာရှိတို့ စီမံထားသော; kammāyatana / sippāyatana / vijjāṭṭhāna = အလုပ်အကိုင် / အတတ်ပညာ / အသိပညာ ဌာန
anulomikā khanti diṭṭhi ruci mudi pekkhā dhammanijjhānakkhanti = လျော်ညီသော သည်းခံ လက်ခံမှု၊ အယူ၊ နှစ်သက်မှု၊ ကြည်နူးမှု၊ ရှုကြည့်မှု၊ သဘောတရားကို ဆင်ခြင်၍ လက်ခံမှု
parato (a)sutvā = အခြားသူထံမှ (မ)ကြားနာ(ဘဲ/၍); X ārabbha = Xကို အာရုံပြု၍; ariyamagga = အရိယာ မဂ်
yā uppajjati / yā tattha / yā evarūpā paññā pajānanā…pe… = ဖြစ်ပေါ်သော / ထို၌ ရှိသော / ဤသို့ သဘောရှိသော ပညာ၊ ကွဲပြားစွာ သိခြင်း… ရှိသမျှ (pi-1)
kammassakatañāṇa, saccānulomika ñāṇa, magga- / phalasamaṅgissa ñāṇa = pi-1 ^1-1373; «Atthi dinnaṃ …» quote = pi-1 diṭṭhisampadā
anvaye / pariye / sammutiñāṇa = ဆက်စပ်၍ / စိတ်ကို ပိုင်းခြား၍ / သမုတ်ကို သိသော ဉာဏ်; Xpetaṃ ñāṇaṃ = Xကို သိသော ဉာဏ်လည်း ဖြစ်သည်
ācaya / apacaya (Xāya) = စုပုံခြင်း / လျော့ပါးခြင်းအတွက် (pi-1); nibbidā = ငြီးငွေ့ခြင်း; paṭivedha = ထိုးဖောက်၍ သိခြင်း (pi-1)
hāna- / ṭhiti- / visesa- / nibbedhabhāginī = ဆုတ်ယုတ်ခြင်း၏ / တည်တံ့ခြင်း၏ / ထူးခြားခြင်း၏ / ဖောက်ထွင်းခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော (pi-1 bhāgino)
saññāmanasikārā samudācaranti = မှတ်သိမှုနှင့် နှလုံးသွင်းခြင်းတို့ ထကြွလာလျှင်; virāgūpasañhitā = ရာဂ ကင်းခြင်းနှင့် စပ်သော
catasso paṭipadā = ကျင့်စဉ် လေးပါး; cattāri ārammaṇāni = အာရုံ လေးပါး; dukkha- / sukhapaṭipadā dandha- / khippābhiññā = pi-1 JH_Q values
nikāmalābhī = စိတ်တိုင်းကျ ရသူ; thokaṃ / vipulaṃ pharati = အနည်းငယ် / ကျယ်ပြန့်စွာ ပျံ့နှံ့စေ
pañcaṅgika / pañcañāṇika sammāsamādhi = အင်္ဂါ / ဉာဏ် ငါးပါး ရှိသော မှန်ကန်သော သမာဓိ; -pharaṇatā = … ပျံ့နှံ့ခြင်း
paccavekkhaṇā = ပြန်လည် ဆင်ခြင်ခြင်း; nimitta = အမှတ်အသား; dibbacakkhu = နတ်မျက်စိ; paracitta = အခြားသူ၏ စိတ်
iddhividha = တန်ခိုး အမျိုးမျိုး; sotadhātuvisuddhiyā ñāṇaṃ = စင်ကြယ်သော နား ဓာတ်ဖြင့် သိသော ဉာဏ်
sattasattati ñāṇavatthūni = ဉာဏ် အခြေခံ ခုနစ်ဆယ့်ခုနစ်ပါး; Xpaccayā Y-ti ñāṇaṃ = Xကြောင့် Y ဖြစ်ပေါ်သည်ဟု သိသော ဉာဏ် (pi-1 ^1-1343)
asati X natthi Y = X မရှိလျှင် Y မရှိ; dhammaṭṭhitiñāṇa = သဘောတရား တည်ရှိပုံကို သိသော ဉာဏ်
sotāpatti- … arahattamagga / phala = သောတာပတ္တိ… အရဟတ္တ မဂ် / ဖိုလ်; anupubbavihārasamāpatti = အစဉ်အတိုင်း နေထိုင်ရာ ဈာန် ဝင်စားရာ
tathāgata = မြတ်စွာဘုရား (pi-1); tathāgatabala = ဘုရားဆိုင်ရာ စွမ်းအား; (tathāgato) pajānāti = သိတော်မူသည်; yathābhūtaṃ = ဟုတ်မှန်သည့်အတိုင်း
āsabhaṃ ṭhānaṃ = အမြတ်ဆုံး နေရာ; sīhanāda = ခြင်္သေ့ဟိန်းသံ; brahmacakka = မြတ်သော တရားစက်
ṭhāna / aṭṭhāna = ဖြစ်နိုင်သော / မဖြစ်နိုင်သော အကြောင်း; anavakāsa = အခွင့်အလမ်း မရှိ; diṭṭhisampanna puggala = အယူ ပြည့်စုံသော ပုဂ္ဂိုလ်
puthujjana = ပုထုဇဉ်; itthī / puriso = အမျိုးသမီး / အမျိုးသား; cakkavattī = စကြဝတေး မင်း; lokadhātu = လောကဓာတ်
sammāsambuddha = (pi-1) အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား; duccarita / sucarita = ဒုစရိုက် / သုစရိုက်
sugati saggaṃ lokaṃ = ကောင်းသော လားရာ၊ နတ်ပြည် လောက; apāya duggati vinipāta niraya = အပါယ်၊ ဆိုးသော လားရာ၊ ပျက်စီး ကျရောက်ရာ၊ ငရဲ
kammasamādāna = ကံ ဆောက်တည်မှု; gati / upadhi / kāla / payoga = လားရာ ဘဝ / ခန္ဓာကိုယ် / အချိန်ကာလ / ကြိုးစား အားထုတ်မှု; sampatti / vipatti = ပြည့်စုံမှု / ချို့ယွင်းမှု
āsaya / anusaya / carita / adhimutti = စိတ်သဘောထား / ကိန်းအောင်းခြင်း (pi-1) / စရိုက် / စိတ်ညွတ်ရာ
appa- / mahārajakkha = ကိလေသာ မြူ နည်းသော / များသော; tikkh- / mudindriya = စွမ်းရည် ထက်မြက်သော / နုံ့သော
svākāra / dvākāra = အခြင်းအရာ ကောင်းသော / ဆိုးသော; su- / duviññāpaya = သိအောင် ပြောပြရ လွယ်သော / ခက်သော; bhabba / abhabba = ထိုက်တန်သော / မထိုက်တန်သော
āvaraṇa = အဟန့်အတား (kept apart from nīvaraṇa = အတားအဆီး); niyāma = သေချာသော လမ်းကြောင်း
the ten views = pi-1 diṭṭhāsavo items (quoted); bhava- / vibhavadiṭṭhi = pi-1 values
puñña- / apuñña- / āneñjābhisaṅkhāra = ကောင်းမှုကို / မကောင်းမှုကို / မတုန်လှုပ်ခြင်းကို ပြုပြင်ဖန်တီးမှု
jhāyī = ဈာန်ဝင်စားသူ; vimokkha = လွတ်မြောက်ခြင်း (pi-1); the arūpa formulas = pi-1 JH_FORM / JH_ARUPA_BASE
saṃkilesa / vodāna / vuṭṭhāna = ညစ်နွမ်းခြင်း / စင်ကြယ်ခြင်း / ထမြောက်ခြင်း
pubbenivāsānussati = ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့ခြင်း (pi-1 ñāṇa form); cutūpapāta = သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်း (pi-1)
anāsavaṃ cetovimuttiṃ = စိတ်အစွန်းအထင်း မရှိသော စိတ်၏ လွတ်မြောက်ခြင်း (sense «free of taints», not the mātikā anāsava)
hetū paccayā (ṭhāna formula) = အကြောင်းရင်း၊ အကြောင်း

## Unsure Pāli / to confirm
- paṭisambhidā = «ပိုင်းခြားသိသော ဉာဏ်» (plain) rather than the well-known Burmese loan ပဋိသမ္ဘိဒါ; paṭibhāna = ဉာဏ်ပေါ်မှု.
- attha = «အကျိုးအနက်» covers both result (hetuphala, vipāka) and meaning (bhāsitassa attho).
- ^2-809 «kañci dhammaṃ atthato upagaccheyya»: read as written (atthato «as having substance», «အနှစ်သာရ ရှိသည်ဟု»);
  the parallel suttas have «attato» (as self). Flag for the user.
- anvaye ñāṇaṃ = «ဆက်စပ်၍ သိသော ဉာဏ်», pariye ñāṇaṃ = «စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်», sammutiñāṇaṃ = «သမုတ်ကို သိသော ဉာဏ်».
- āsaya = «စိတ်သဘောထား»; adhimutti = «စိတ်ညွတ်ရာ»; abbokiṇṇa = «ကြားမပြတ် ဆက်တိုက်» (gloss: na paṭipāṭiyā).
- tathāgata actions with the honorific «တော်မူ» (pajānāti = သိတော်မူသည်); a bhikkhu's pajānāti = သိသည်.

## Source slips (translated as written)
- ^2-720: «dhammapaṭisambhidā niruttipaṭisambhidā» (comma missing): no «၊» there.
- ^2-749: «Anidassanaapaṭighā» (for anidassanaappaṭighā): read as the pi-1 term.
- ^2-750: «nahetūahetukātipi» (one word): read as na hetū ahetukā.
- ^2-750: «āsavo [āsavā (sī.) …] ceva sāsavā cāti»: the variant is put after that term's Burmese.
- ^2-726 …: «paññatti hoti tatra» (no comma) kept without «၊».
- ^2-753 (40): «anuppādinnupādāniyā, anuppādinnaanupādāniyā» read as anupādinn-; (62) «ajjhatā» read as ajjhattā.
- ^2-788: «pajānanā …pe…» (stray space): one «…».
- ^2-803 «(12-21) Dhammasamaṅgissa ñāṇaṃ» (elsewhere Maggasamaṅgissa): translated as written «တရားနှင့် ပြည့်စုံသူ၏
  ဉာဏ်»; ^2-803 «idaṃ vuccati "saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ.» (closing quote missing): kept without «”».
- ^2-804 «So kho panāhaṃ … vuṭṭhahāmī"ti» (opening quote missing): kept without «“».
- ^2-809 line 2 «Aṭṭhānametaṃ …» (opening quote missing): kept; ^2-815 «"hoti tathāgato paraṃ maraṇāti vā» (closing quote
  missing): kept without «”».
- ^2-828 «[sampattiyeva (ka.)]» gives the same reading as the text: kept as a spelling variant.
- ^2-777 «upariṭṭhimā [upariṭṭhime (syā.), upariṭṭhimaṃ (ka.)] arahattaphale»: read as the locative (upariṭṭhime).
