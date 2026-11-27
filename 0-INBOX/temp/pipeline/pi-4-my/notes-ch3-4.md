# pi-4 Burmese zero-shot: notes for 3-dukapuggalapannatti, 4-tikapuggalapannatti

Status: DONE 2026-11-19 (both chapters written and checked). Brief: burmese-zeroshot-brief.md. Not committed.

## Files
- Output: `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/3-dukapuggalapannatti.md` (47 segments,
  48 lines), `4-tikapuggalapannatti.md` (42 segments, 57 lines).
- `make_ch3-4.py` (generator; imports make_sample.py, so the sample tables are installed; adds its own tables in
  memory only; my4_formulas.py and make_sample.py unchanged), `check_ch3-4.py` (adapted check_sample.py).
- Run: `python3 -I -X utf8 make_ch3-4.py [--misses]`, then `check_ch3-4.py`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for both files (my chk-pe copies deleted).
- check_ch3-4.py: A 2/2 regenerated identical; B1 105 lines; B2 45 numbers; B3 359 negations / pairs; B4 72 quality
  nouns; B5 147 questions / closing names; 0 mismatches. Reuse 173 / 173 (C1 83 final units read, 13 of them adapted
  where the pi-4 Pāli differs, list ADAPTED in the check; C2 2/2 heading / colophon; C3 88/88 terms and clauses).
- Mutation test: a dropped «မဟုတ်», a «မ» removed from a verb and a wrong closing name are each caught (B3, B5).

## What is added to my4_formulas in memory (make_ch3-4.py)
- `F.var_my` wrapped: BR_MY table (whole brackets with several readings, notes, references) and `vibha.` / `ma. ni.`
  references; VAR_KIND entries (see "Variant readings"); REF «vibha.» = «“ခွဲခြမ်းစိတ်ဖြာခြင်း”», «ma. ni.» =
  «“မဇ္ဈိမနိကာယ်”» (pi-2 ^2-760).
- EXTRA_RULES (new frames): «Tattha katamo X?»; «ayaṃ / idaṃ vuccati X.» (X a quality noun); «Yassa puggalassa ayaṃ X
  (ap)pahīno»; «Iminā / Imāya X-ena samannāgato puggalo "Y".»; «Katame dve puggalā G?»; «Tattha katame tayo G
  puggalā?» / «… tayo satthāro?»; «… . (n)» (item number at a line end); «…"ti! Next» (an exclamation ends a sentence).
- F.PLURAL «kāmesu ca bhavesu ca avītarāgā» -> the singular name.
- SENT: UNIQUE3 / UNIQUE4 (all sentences of the two chapters; FIN_UNITS = units copied verbatim from FINAL).

## New frames («Pāli = Burmese»)
Tattha katamo X? = ထိုတို့အနက် X ဟူသည် အဘယ်နည်း။ (pi-1 / pi-2 frame; X from QUAL, all read from FINAL)
ayaṃ / idaṃ vuccati X. = ဤသည်ကို Xဟု ခေါ်သည်။ (pi-1 form without quotes; pi-4 has none)
Yassa puggalassa ayaṃ X appahīno = အကြင် ပုဂ္ဂိုလ်၏ ဤXကို မပယ်ရသေး (sample ^4-9)
Yassa puggalassa ayaṃ X pahīno = အကြင် ပုဂ္ဂိုလ်၏ ဤXကို ပယ်ပြီး ဖြစ်၏ (sample ^4-41)
Iminā X-ena samannāgato puggalo "Y". = ဤXနှင့် အပြည့်အဝ ပြည့်စုံသော ပုဂ္ဂိုလ်သည် “Y” ဖြစ်သည်။ (sample ^4-20)
Katame dve puggalā G? = G ပုဂ္ဂိုလ် နှစ်ယောက် ဟူသည် အဘယ် ပုဂ္ဂိုလ်တို့နည်း။ (plural of the sample's question frame)
Tattha katame tayo G puggalā? = ထိုတို့အနက် G ပုဂ္ဂိုလ် သုံးယောက် ဟူသည် အဘယ် ပုဂ္ဂိုလ်တို့နည်း။
Tattha katame (aparepi) tayo satthāro? = ထိုတို့အနက် (နောက်ထပ်) ဆရာ သုံးယောက် ဟူသည် အဘယ် ဆရာတို့နည်း။
Katame tayo? = အဘယ် ပုဂ္ဂိုလ် သုံးယောက်နည်း။
Katamesaṃ dvinnaṃ puggalānaṃ āsavā (na) vaḍḍhanti? = အဘယ် ပုဂ္ဂိုလ် နှစ်ယောက်တို့၏ စိတ်အစွန်းအထင်းတို့သည် (မ)တိုးပွားကုန်သနည်း။
imesaṃ dvinnaṃ puggalānaṃ āsavā (na) vaḍḍhanti. = ဤပုဂ္ဂိုလ် နှစ်ယောက်တို့၏ စိတ်အစွန်းအထင်းတို့သည် တိုးပွားကုန်၏။ / မတိုးပွားကုန်။ (mātikā (23), (24))
ime dve puggalā dullabhā lokasmiṃ. = ဤပုဂ္ဂိုလ် နှစ်ယောက်တို့သည် လောက၌ ရခဲကုန်၏။
ime dve puggalā "duttappayā". = ဤပုဂ္ဂိုလ် နှစ်ယောက်တို့ကို “ရောင့်ရဲစေရန် ခက်ခဲသော ပုဂ္ဂိုလ်”ဟု ခေါ်သည်။ (sutappayā likewise)
ime vuccanti puggalā NAME (no quotes) = ဤပုဂ္ဂိုလ်တို့ကို NAMEဟု ခေါ်သည်။ (^4-127; ^4-128 / ^4-129 singular)
Seyyathāpi (nāma) X, evamevaṃ Y = ဥပမာအားဖြင့် X သကဲ့သို့၊ ဤအတူပင် Y
Seyyathāpi so X, tathūpamo ayaṃ puggalo. = ထိုXသည် … သကဲ့သို့၊ ဤပုဂ္ဂိုလ်သည် ထိုနှင့် တူ၏။
idha panekacco = တစ်ဖန် ဤလောက၌ အချို့သော
Tatra yvāyaṃ X …, Y = ထိုXတို့အနက် … သော အကြင် X ရှိ၏၊ Y
santo saṃvijjamānā (lokasmiṃ / bhikkhūsu) = (လောက၌ / ရဟန်းတို့အတွင်း၌) ရှိကြ၏၊ ထင်ရှား တွေ့ရကြ၏
tena daṭṭhabbo = …ဟု ထိုအကြောင်းဖြင့် သိမြင်ရမည်
Taṃ kissa hetu? = ထိုသို့ အဘယ်ကြောင့်နည်း။ (pi-2 ^2-943)
Tasmā = ထို့ကြောင့်
evarūpo puggalo (na) sevitabbo bhajitabbo payirupāsitabbo = ဤသို့ သဘောရှိသော ပုဂ္ဂိုလ်ကို ပေါင်းသင်းအပ်၏၊ ဆည်းကပ်အပ်၏၊ ချဉ်းကပ် ခစားအပ်၏ / မပေါင်းသင်းအပ်၊ မဆည်းကပ်အပ်၊ မချဉ်းကပ် ခစားအပ် (sample SEV3_NO)
sevati bhajati payirupāsati = ပေါင်းသင်း၏၊ ဆည်းကပ်၏၊ ချဉ်းကပ် ခစား၏

## New terms («Pāli = Burmese»)
### ch3 (duka)
paḷāsāyitattaṃ = တုပြိုင်ထားသော အဖြစ် (pi-2 ^2-892 lacks the word; pattern of makkhāyitattaṃ)
paṭiggāho (diṭṭhi list) = လက်ခံ စွဲကိုင်ခြင်း (pi-1 has patiṭṭhāho «ခိုင်မြဲစွာ စွဲကိုင်ခြင်း» there)
pubbakārī = ရှေးဦးစွာ ကျေးဇူးပြုသူ
kataññū katavedī = ကျေးဇူးကို သိ၍ ကျေးဇူးကို ဆပ်သူ
laddhaṃ laddhaṃ = ရတိုင်း ရတိုင်းကို
nikkhipati / na nikkhipati = သိုမှီးထား / မသိုမှီးထား
vissajjeti / na vissajjeti = စွန့်ကြဲ / မစွန့်ကြဲ
kukkuccāyitabbaṃ / na kukkuccāyitabbaṃ = နောင်တ ပူပန်ရန် ထိုက်သည်ကို / နောင်တ ပူပန်ရန် မထိုက်သည်ကို
kukkuccāyati / na kukkuccāyati = နောင်တ ပူပန် / နောင်တ မပူပန် (kukkucca pi-1 «နောင်တ ပူပန်မှု»)
dussīlo hoti pāpadhammo = သီလ ပျက်သူ ဖြစ်၏၊ ယုတ်မာသော သဘော ရှိသူ ဖြစ်၏ (dussīla pi-2 ^2-851; pāpadhamma = the catukka name)
sīlavā hoti kalyāṇadhammo = သီလ ရှိသူ ဖြစ်၏၊ ကောင်းမွန်သော သဘော ရှိသူ ဖြစ်၏
aññaṃ dussīlaṃ pāpadhammaṃ = သီလ ပျက်သော၊ ယုတ်မာသော သဘော ရှိသော အခြားသူကို
tathāgatassa sāvakā arahanto = မြတ်စွာဘုရား၏ ရဟန္တာ တပည့်တို့
Paccekasambuddhā = ပစ္စေကဗုဒ္ဓါတို့
### ch4 (tika)
So suṇāti = ထိုသူသည် ကြားရ၏
itthannāmo kira bhikkhu … viharatī"ti = “ဤမည်သော ရဟန်းသည် … နေသတတ်”ဟု
kudāssu nāmāhampi … viharissāmī"ti = “ငါသည်လည်း အဘယ်အခါမှ … နေရပါမည်နည်း”ဟု
Tassa (na) evaṃ hoti = ထိုသူအား ဤသို့ အကြံ ဖြစ်၏ / မဖြစ် (pi-2 ^2-953 «ထိုရဟန်းအား …»: here the subject is a person, not a monk)
āsavānaṃ khayā … upasampajja viharati = (pi-2 ^2-831 verbatim) … ဝင်စား၍ နေ၏ (pi-2 «နေတော်မူ၏» is said of the Buddha)
asuci = စင်ကြယ်မှု မရှိသူ; saṅkassarasamācāro = သံသယဖြင့် အောက်မေ့ရသော အကျင့် ရှိသူ; paṭicchannakammanto = ဖုံးကွယ်ထားသော အမှု ရှိသူ
assamaṇo samaṇapaṭiñño = ရဟန်း မဟုတ်ဘဲ ရဟန်းဟု ဝန်ခံသူ; abrahmacārī brahmacāripaṭiñño = မြင့်မြတ်သော အကျင့်ကို မကျင့်ဘဲ မြင့်မြတ်သော အကျင့်ကို ကျင့်သူဟု ဝန်ခံသူ
antopūti = အတွင်း၌ ပုပ်သိုးသူ; avassuto = ကိလေသာ စိုစွတ်သူ; kasambujāto = အမှိုက်သရိုက်ကဲ့သို့ ဖြစ်နေသူ
avimuttassa vimuttāsā … paṭippassaddhā = မလွတ်မြောက်သေးစဉ် ဖြစ်ခဲ့သော လွတ်မြောက်လိုသော မျှော်လင့်ချက် … ငြိမ်းသွားပြီ
gilāna = လူနာ; sappāyāni bhojanāni / bhesajjāni = သင့်လျော်သော အစားအစာ / ဆေးဝါးတို့ကို; patirūpaṃ upaṭṭhākaṃ = လျောက်ပတ်သော လုပ်ကျွေးပြုစုသူကို
labhanto vā … alabhanto vā = ရသည်ဖြစ်စေ၊ မရသည်ဖြစ်စေ; labhanto … no alabhanto = ရသည်သာ ဖြစ်၍ မရသည် မဟုတ်
vuṭṭhāti tamhā ābādhā (recovers) = ထိုအနာရောဂါမှ ပျောက်ကင်း၏ (sense kept apart from vuṭṭhāti «ထမြောက်» of the attainments)
anuññāta = ခွင့်ပြုတော်မူ၏ (by the Blessed One); bhagavā = မြတ်စွာဘုရား (as tathāgata)
gilānabhattaṃ / gilānabhesajjaṃ / gilānupaṭṭhāko = လူနာ၏ အစားအစာ / လူနာ၏ ဆေးဝါး / လူနာကို လုပ်ကျွေးပြုစုသူ
tathāgataṃ dassanāya = မြတ်စွာဘုရားကို ဖူးမြင်ရန်; dhammavinayaṃ savaṇāya = တရားနှင့် ဝိနည်းကို နာကြားရန် (dhammavinaya pi-2)
okkamati niyāmaṃ … = … သေချာသော လမ်းကြောင်းသို့ သက်ဆင်း၏ (sample «သက်ဆင်းရန်»); dhammadesanā = တရား ဟောကြားခြင်း
musāvādī = မုသား ပြောသူ (musāvāda pi-2 ^2-942); sampajānamusā bhāsitā = သိလျက် မုသား ပြောသူ
sabhaggato … rājakulamajjhagato vā abhinīto sakkhipuṭṭho = လူစုအဝေးသို့ … မင်းမျိုးမင်းနွယ် အလယ်သို့ ရောက်နေသည်ဖြစ်စေ သက်သေအဖြစ် ခေါ်ဆောင်ခံရ၍ မေးမြန်းခံရသောအခါ
ehambho purisa = လာလော့ အချင်း၊ ယောက်ျား; ajānaṃ / jānaṃ / apassaṃ / passaṃ vā āha = မသိလျက်လည်း / သိလျက်လည်း / မမြင်လျက်လည်း / မြင်လျက်လည်း ပြော၏
attahetu vā parahetu vā āmisakiñcikkhahetu vā = မိမိ၏ … သူတစ်ပါး၏ အကြောင်းကြောင့်ဖြစ်စေ၊ အနည်းငယ်သော ပစ္စည်း လာဘ်ကြောင့်ဖြစ်စေ
nelā kaṇṇasukhā pemaniyā hadayaṅgamā porī bahujanakantā bahujanamanāpā = အပြစ် ကင်းသော၊ နားဝင် ချိုသော၊ ချစ်ခင်ဖွယ် ကောင်းသော၊ နှလုံးသို့ ရောက်သော၊ ယဉ်ကျေးသော၊ လူအများ နှစ်သက်သော၊ လူအများ စိတ်တိုင်းကျသော
kodhano hoti upāyāsabahulo … pātukaroti = အမျက်ဒေါသ ထွက်တတ်သူ ဖြစ်၏၊ ပြင်းစွာ ပူပန်ခြင်း များသူ ဖြစ်၏ … ထင်ရှား ပြ၏ (upāyāsa pi-2 ^2-198, kopa pi-1 ^1-1066)
abhisajjati / kuppati / byāpajjati / patitthīyati = ငြိုငြင်၏ / အမျက်ထွက်၏ / ဖောက်ပြန်၏ / ခိုင်ခိုင်မာမာ ဆန့်ကျင်၏; appaccaya = မနှစ်သက်မှု
kaṭṭhena vā kaṭhalāya vā ghaṭṭito bhiyyoso mattāya = သစ်သားချောင်းဖြင့်ဖြစ်စေ၊ အိုးခြမ်းကွဲဖြင့်ဖြစ်စေ ထိခိုက်မိလျှင် ပို၍ ပို၍
duṭṭhāruko … āsavaṃ deti = ပြည်တည်နေသော အနာသည် … ပြည်ယို (āsava = discharge here, not the taint «စိတ်အစွန်းအထင်း»)
tindukālātaṃ … cicciṭāyati ciṭiciṭāyati = တည်သားဖြင့် လုပ်သော မီးစသည် … တဖျစ်ဖျစ် မြည်၍ တဖွားဖွား မီးပွင့်; gūthakūpo … duggandho = မစင်တွင်းသည် … အနံ့ ဆိုး
cakkhumā puriso rattandhakāratimisāya vijjantarikāya = မျက်စိ ကောင်းသော ယောက်ျားသည် ညဉ့်အခါ မှောင်မိုက် ထူထပ်စဉ် လျှပ်စီး လက်သည့် ခဏ၌
vajirassa natthi kiñci abhejjaṃ maṇi vā pāsāṇo vā = စိန်အတွက် ပတ္တမြားဖြစ်စေ၊ ကျောက်ဖြစ်စေ မဖောက်ထွင်းနိုင်သည့် အရာ တစ်စုံတစ်ရာမျှ မရှိ
bhoga = စည်းစိမ်ဥစ္စာ; anadhigataṃ / adhigataṃ = မရသေးသော / ရပြီးသော; phātiṃ kareyya = တိုးပွားအောင် ပြုရာ၏
kusalākusale / sāvajjānavajje / hīnappaṇīte / kaṇhasukkasappaṭibhāge dhamme = ကုသိုလ် အကုသိုလ် / အပြစ် ရှိသော အပြစ် မရှိသော / ယုတ်ညံ့သော မွန်မြတ်သော / မည်းနက်သော ဖြူစင်သော ဆန့်ကျင်ဘက် ရှိသော သဘောတရားတို့ကို (pi-1 duka adjectives)
ārāmaṃ gantā hoti abhikkhaṇaṃ bhikkhūnaṃ santike dhammassavaṇāya = ရဟန်းတို့၏ အထံ၌ တရား နာကြားရန် ကျောင်းသို့ ခဏခဏ သွားသူ ဖြစ်၏ (abhikkhaṇaṃ / abhiṇhaṃ = ခဏခဏ; «မကြာခဏ» avoided: it reads as a negation)
ādikalyāṇaṃ … brahmacariyaṃ pakāsenti = အစ၌ ကောင်းသော … စင်ကြယ်သော မြင့်မြတ်သော အကျင့်ကို ထုတ်ဖော် ပြကြ၏
(na) ādiṃ manasi karoti = အစကိုလည်း နှလုံးသွင်း၏ / နှလုံး မသွင်း (pi-1 «နှလုံးသွင်း», «နှလုံး မသွင်းဘဲ»)
so tasmiṃ āsane nisinno / vuṭṭhitopi / vuṭṭhito ca kho tamhā āsanā = ထိုသူသည် ထိုနေရာ၌ ထိုင်နေစဉ် / ထိုနေရာမှ ထပြီးသော်လည်း / ထပြီးသောအခါ၌ကား
kumbho nikkujjo / ukkujjo = မှောက်ထားသော / လှန်ထားသော အိုး; vivaṭṭati / saṇṭhāti = စီးကျသွား / တည်နေ
ucchaṅge nānākhajjakāni ākiṇṇāni – tilā taṇḍulā modakā badarā = ပေါင်ခွင်၌ အမျိုးမျိုးသော စားဖွယ်တို့ … – နှမ်း၊ ဆန်၊ မုန့်လုံး၊ ဆီးသီး
satisammosā pakireyya = သတိလစ်၍ … ဖိတ်ကျစေရာ၏
abhiṇhaṃ kujjhati = ခဏခဏ အမျက်ဒေါသ ထွက်၏; ciraṃ dīgharattaṃ anuseti = ကြာမြင့်စွာ ရှည်လျားသော ကာလပတ်လုံး ကိန်းအောင်း၏
lekhā (na) khippaṃ lujjati … (na) ciraṭṭhitikā = အရေးအကြောင်းသည် … လျင်မြန်စွာ (မ)ပျက် … ကြာမြင့်စွာ (မ)တည်
āgāḷhena / pharusena / amanāpena vuccamāno = ပြင်းထန်စွာ / ကြမ်းတမ်းစွာ / မနှစ်မြို့ဖွယ် ပြောဆိုခံရသော်လည်း
saṃsandatimeva sandhiyatimeva sammodatimeva = ညီညွတ်စွာ ပေါင်းစည်းသည်သာ၊ ပြန်လည် ဆက်စပ်သည်သာ၊ ဝမ်းမြောက်စွာ ဆက်ဆံသည်သာ
potthaka = လျှော်ပိတ်စ (sample); kāsikavattha = ကာသိ ပိတ်စ (sample); nava / majjhima / jiṇṇa = အသစ် ဖြစ်သော / အလယ်အလတ် ဖြစ်သော / ဟောင်းနွမ်းသော
dubbaṇṇa / dukkhasamphassa / appaggha = အဆင်း ညှိုး / ထိတွေ့ရ နာကျင် (pi-1) / တန်ဖိုး နည်း; vaṇṇavant / sukhasamphassa / mahaggha = အဆင်း လှ / ထိတွေ့ရ သာယာ (pi-1) / တန်ဖိုး ကြီး
ukkhaliparimajjanaṃ = အိုးသုတ်ဝတ်; saṅkārakūṭa = အမှိုက်ပုံ; ratanapaliveṭhanaṃ = ရတနာ ထုပ်ရာ အဝတ်; gandhakaraṇḍaka = နံ့သာ ဘူး
navo / majjhimo / thero cepi bhikkhu = ရဟန်း ဝါငယ် / ဝါလတ် / ထေရ် ဖြစ်စေကာမူ; idamassa …tāya = ဤသည်မှာ ထိုရဟန်း၏ …ခြင်း ဖြစ်၏
diṭṭhānugatiṃ āpajjati = အမြင်ကို အတုယူ လိုက်နာ; dīgharattaṃ ahitāya dukkhāya / hitāya sukhāya = ကြာမြင့်စွာ အစီးအပွား မရှိခြင်းငှာ၊ ဆင်းရဲခြင်းငှာ / အစီးအပွားငှာ၊ ချမ်းသာခြင်းငှာ
cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāra = (pi-2 ^2-929) သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်
(na) mahapphalaṃ … mahānisaṃsaṃ = အကျိုး ကြီးမား(သည် မဟုတ်)၊ အာနိသင် ကြီးမား(သည် မဟုတ်)
saṅghamajjhe bhaṇati = သံဃာ့အလယ်၌ ပြောဆို (pi-2); bālassa abyattassa bhaṇitena = (pi-2 ^2-957 verbatim)
kupito anattamano = အမျက်ထွက်၍ စိတ်မနှစ်သိမ့်ဘဲ; saṅgho ukkhipati = သံဃာက နှင်ထုတ်
appasaddā āyasmanto hotha = အသျှင်တို့ အသံ ငြိမ်ကြလော့ (āyasmanto pi-2); vacanaṃ ādheyyaṃ gacchati = စကားသည် လက်ခံ မှတ်သားထိုက်သော စကား ဖြစ်လာ၏
uddhato unnaḷo capalo mukharo vikiṇṇavāco = ယောက်ယက်ခတ်သူ၊ ဘဝင်မြင့်သူ၊ ပေါ့ပျက်သူ၊ စကားများသူ၊ ရှုပ်ပွေစွာ ပြောတတ်သူ (and the a- forms with «မ»)
asamāhito / samāhito = စိတ် မတည်ကြည်သူ / စိတ် တည်ကြည်သူ (pi-2 ^2-851); vibbhantacitto = စိတ် ပျံ့လွင့်သူ; ekaggacitto = စိတ် တစ်ခုတည်း၌ စူးစိုက်သူ
pākaṭindriyo / saṃvutindriyo = အာရုံခံ အင်္ဂါတို့ ပွင့်ဟနေသူ / အာရုံခံ အင်္ဂါတို့ကို စောင့်စည်းသူ
hīno / sadiso / adhiko hoti sīlena samādhinā paññāya = သီလ၊ သမာဓိ၊ ပညာတို့ဖြင့် ယုတ်ညံ့သူ / တူညီသူ / သာလွန်သူ ဖြစ်၏
aññatra anuddayā aññatra anukampā = သနားကြင်နာခြင်းကြောင့်မှလွဲ၍၊ စာနာ ထောက်ထားခြင်းကြောင့်မှလွဲ၍ (pi-1 ^1-1062)
sīlasāmaññagatānaṃ sataṃ sīlakathā ca no bhavissati … = သီလ တူညီမှုသို့ ရောက်ကြသော ငါတို့အား သီလနှင့် စပ်သော စကားသည်လည်း ဖြစ်လိမ့်မည် … (no = "us")
aparipūraṃ / paripūraṃ sīlakkhandhaṃ = မပြည့်စုံသေးသော / ပြည့်စုံပြီးသော သီလ အစုအဝေး (khandha = «အစုအဝေး»); anuggahessāmi = ချီးမြှင့် ထောက်ပံ့မည်
kittisaddo abbhuggacchati = သတင်းစကား ပျံ့နှံ့၏ (pāpako / kalyāṇo = ယုတ်မာသော / ကောင်းမွန်သော)
pāpamitto purisapuggalo pāpasahāyo pāpasampavaṅko = ဤလူ ပုဂ္ဂိုလ်သည် မိတ်ဆွေဆိုးနှင့် ပေါင်းသင်းသူ၊ အပေါင်းအဖော် ဆိုး ရှိသူ၊ ဆိုးသူတို့ဘက်သို့ ညွတ်ကိုင်းသူ (kalyāṇa- likewise)
ahi gūthagato … na ḍaṃsati … makkheti = မစင်ထဲ၌ ရှိသော မြွေသည် မကိုက်သော်လည်း လူကို ပေကျံစေ
akkoseyya / paribhāseyya / anatthaṃ kareyya = ဆဲရေးရာ၏ / ကဲ့ရဲ့ ပြောဆိုရာ၏ / မကောင်းမှုကို ပြုရာ၏ (anattha pi-1 ^1-1066)
satthā = ဆရာ (mātikā); pariññaṃ paññapeti = ပိုင်းခြား သိခြင်းကို ပညတ်၏ (pariññā, paññapeti pi-2); kāmā / rūpā / vedanā = ကာမ / ရုပ် / ခံစားမှု
attānaṃ saccato thetato = အတ္တကို အမှန်အားဖြင့် ခိုင်မြဲစွာ (pi-2 ^2-948); abhisamparāyaṃ = တမလွန်ဘဝ၌
sassatavādo / ucchedavādo satthā = ထာဝရ တည်မြဲသည်ဟု / ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ ရှိသော ဆရာ (pi-2 ^2-977)
rūpāvacara- / arūpāvacarasamāpattiyā lābhī = သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ဈာန် ဝင်စားရာကို ရရှိသော
Sotāpannasakadāgāmino = သောတာပန်နှင့် သကဒါဂါမ်တို့

## Variant readings (new)
VAR_KIND: dūsanā dūsitattaṃ, ussuyā ussuyanā, sukaṭadukkaṭānaṃ, evameva, dhammassavanāya, paṭhaviyā, patiṭṭhīyati,
nikujjo, tilataṇḍulā, pavattanī, paññāpeti, ehi bho = spelling «စာလုံးပေါင်းကွဲ»; samaggatā, assavanoti, … ceva =
word «ပါဌ်ကွဲ». Several readings: «[LABEL (Sī.): X၊ (Ka.): Y]» (pi-2 ^2-832). (sabbattha) = «(Sabbattha)» (pi-2 ^2-754);
(aṭṭhakathā) = «(အဋ္ဌကထာ)». Notes translated: «evaṃ khuddakavibhaṅgadukaniddesepi» = «“အသေးစား အကြောင်းအရာများကို
ခွဲခြမ်းစိတ်ဖြာခြင်း”၏ နှစ်မျိုးတွဲ အကျယ် ဖော်ပြချက်၌လည်း ဤနည်းတူ»; «padasiddhi cintetabbā» = «ပုဒ်၏ ဖြစ်ပုံကို
စဉ်းစားရမည်»; «rūpasiddhiṭīkāya pana sameti» = «ရူပသိဒ္ဓိ ဋီကာနှင့်ကား ညီ၏»; «[tappetā ca, ayaṃ vuccati puggalo
titto (sī.)]» = a word variant, Pāli kept.

## Reused with an adjustment (identical Pāli is not possible; see check ADAPTED)
- ^4-48 paḷāsa list: pi-2 ^2-892 + paḷāsāyitattaṃ; ^4-75 sovacassatā: pi-1 ^1-1334 items reordered to the pi-4 order;
  ^4-76 sampavaṅkatā as pi-2 ^2-901 (pi-1 taṃsampavaṅkatā «ထိုသူတို့ဘက်သို့ …»); ^4-62 paṭiggāho (above);
  ^4-57 / ^4-58 / ^4-72 / ^4-77 / ^4-78 «Idhekacco puggalo» = IDHA for the final «Idhekacco» «… သူသည်»; sentences
  joined with «၊» where the pi-4 Pāli has «;» or «,» for the final «.»; ^4-78 the pi-1 sentence split at «.» and quoted.
- Spelling differences treated as the same word (final Burmese kept): saṅkappati / saṅkappeti, vippaṭikula- /
  vippaṭikūla-, anādariyatā / anādaratā, appatissavatā / appaṭissavatā, asamapekkhaṇā / -nā, «Pubbakālaṃ kodho
  aparakālaṃ upanāho.» without the comma of pi-2 (Burmese «၊» kept, as the sample's harmonise note on ^4-1).

## Unsure Pāli / to review
- saṅkassarasamācāro, avassuto, kasambujāto, antopūti: plain glosses (see terms); unnaḷo «ဘဝင်မြင့်သူ», mukharo
  «စကားများသူ», pākaṭindriyo «အာရုံခံ အင်္ဂါတို့ ပွင့်ဟနေသူ».
- ^4-121 aññatra anuddayā aññatra anukampā «… ကြောင့်မှလွဲ၍» (except out of sympathy).
- ^4-116 «saṅkārakūṭeva naṃ potthakaṃ» read as a simile «… စွန့်ပစ်သကဲ့သို့ပင်»; ^4-117 «ādheyyaṃ gacchati» «လက်ခံ
  မှတ်သားထိုက်သော စကား ဖြစ်လာ၏».
- ^4-130 «tena daṭṭhabbo» «ထိုအကြောင်းဖြင့် သိမြင်ရမည်»; rūpa of «rūpānaṃ pariññaṃ» = «ရုပ်».
- dukkhasamphassa of a cloth = pi-1 «ထိတွေ့ရ နာကျင်» (literal, kept for identical Pāli).
- vuṭṭhāti tamhā ābādhā «ပျောက်ကင်း» (kept apart from «ထမြောက်» of the attainments): a sense split for review.
- Tassa (na) evaṃ hoti «ထိုသူအား» vs pi-2 «ထိုရဟန်းအား» (context): to harmonise.

## Source slips (translated as written)
- ^4-55 «Tattha katamo dovacassatā?» (katamo for katamā): frame unchanged.
- ^4-66 «… aparakālaṃ upanāho yo evarūpo …»: no full stop (^4-46 has one): one Burmese sentence, joined with «၊».
- ^4-69 «Katamo ca pugalo amaccharī?» (pugalo): same Burmese as the question frame.
- ^4-51 «parikkhattattā» (^4-71 and pi-2 «parikkhattatā»): same Burmese.
- ^4-97 «yathādiṭṭhippattassa» (one word; ch2 sample «yathā diṭṭhippattassa»): same Burmese.
- ^4-109 «ārāmaṃ gantā honti» (plural verb, singular subject): same Burmese as «hoti».
- ^4-90 the segment has no closing «ayaṃ vuccati» (the Dukaniddeso colophon closes it, 2 lines, kept).
- ^4-52 «"mā maṃ jaññā"ti saṅkappati "mā maṃ jaññā"ti …» (no comma; ^4-72 has one): same Burmese («၊»).
