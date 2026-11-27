# pi-2 Burmese zero-shot, chapters 2-4: working notes

Scope: 2-ayatanavibhango, 3-dhatuvibhango, 4-saccavibhango. Brief: burmese-zeroshot-brief.md. Pāli only; no Burmese
translation or nissaya consulted, no web search; pi-1-my, my2_formulas.py, my2-zeroshot-terms.md read only (nothing
written there; make_sample.py not run). Meaning cross-checked against the English pi-2 rails only.

## Status (2026-11-17): done
- [x] 2-ayatanavibhango.md (24 segments, 62 lines)
- [x] 3-dhatuvibhango.md (22 segments, 92 lines)
- [x] 4-saccavibhango.md (40 segments, 136 lines)
- check_chapter_ids / pi-6-mr/check_text_pe / pi-4-mr/check_marks: OK on all three (chk-pe copies deleted).
- check_ch2-4.py: 0 mismatches on all three; pi-1 reuse 4 / 4, 2 / 2, 2 / 2 (8 / 8).
- Regenerate: `python3 -I -X utf8 make_ch2-4.py` (all three chapters, then this file's generated section).
  Check: `python3 -I -X utf8 check_ch2-4.py <pāli> <my> …`. Lookup helper: `make_ch2-4.py --find REGEX …` (pi-1
  Pāli sentence + final pi-1 Burmese sentence). Nothing committed.

## Method
- make_ch2-4.py imports my2_formulas (F) and extends its tables in memory only (KH subjects, HEAD / COLO, ITEM,
  TERM_IRREG, EXTRA_RULES; P1.SYN / P1.NAMES / P1.CU_EXTRA_RULES of the in-memory pi-1 module). Every line is split
  into sentences; each sentence: (1) pi-1 final sentence if the Pāli occurs in pi-1; (2) a whole-sentence frame
  (SENT); (3) the sample clause engine (F.clauses_my) with the chapter rules; (4) the pi-1 Rūpakaṇḍa / cittuppāda
  engine (F.P1.clauses_my, rails patches applied; it reproduces the pi-1 rails text of 3-01, 3-02, 3-03 exactly).
  A sentence nothing matches stops the chapter.
- pi-1 lists reused item by item from the pi-1 rails Burmese (learn(): avijjā, micchā- / sammāsaṅkappa, dosa, adosa,
  the kāyika / cetasika feelings, the lokuttara path-factor lists); pi-1 strings that are copied are asserted against
  the rails text (lobha list: kāmataṇhā …, abhijjhā; paṭiccasamuppāda: soka… list, jāti, jarā, maraṇa; ^1-1377 the
  four right efforts; ^1-277 the lokuttara opening; ^1-6 the citta list; ^1-1340 dhātu names; ^1-1050 ajjhatta /
  paccatta / upādiṇṇa).
- Variant brackets: one reader for all forms (several readings «[KIND (S.): a၊ (S.): b]» as pi-1 ^1-1065;
  «evamuparipi» = «၊ အောက်တွင်လည်း ဤနည်းအတိုင်း»; «dha. sa. 596-599» = «၊ “သဘောတရားများကို စုစည်းရေတွက်ခြင်း”
  596-599»; siglum «(?)» = «(ရင်းမြစ် မသေချာ)», since «?» is not allowed in the text).

## Choices (all strings in the generated section below)
- Chapter titles as approved: «အာရုံခံ နယ်ပယ်များ / ဓာတ်များ / သစ္စာများကို ခွဲခြမ်းစိတ်ဖြာခြင်း».
- Truths: sacca = «သစ္စာ», ariya = «အရိယာ», dukkha (truth) = «ဒုက္ခ» (pi-1 «Dukkhe ñāṇaṃ»), samudaya = «ဖြစ်ပေါ်ခြင်း»,
  nirodha = «ချုပ်ငြိမ်းခြင်း», nirodhagāminī paṭipadā = «ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်» (pi-1 4-01). Section
  headings Dukkhasaccaṃ … = «ဒုက္ခ သစ္စာ», «ဖြစ်ပေါ်ခြင်း သစ္စာ», «ချုပ်ငြိမ်းခြင်း သစ္စာ», «မဂ် သစ္စာ».
- dukkha has two senses in ch4 suttanta: the truth / characteristic «ဒုက္ခ», and bodily pain «ကိုယ်ဆင်းရဲခြင်း»
  (pi-1 soka… list) in «Tattha katamaṃ dukkhaṃ? Yaṃ kāyikaṃ asātaṃ …». The same Pāli question in the abhidhamma part
  asks for the truth («ဒုက္ခ»). Decided by part (suttanta / abhidhamma).
- Three characteristics (ch2): aniccaṃ = pi-1 «မမြဲသော», dukkhaṃ = «ဒုက္ခ ဖြစ်သော», anattā = «အတ္တ မဟုတ်သော».
- Element definitions (ch3): qualifiers from pi-1 ^1-1050 / Mātikā; Burmese order «Q1 SYN… ဖြစ်၍ Q2 အရာ ရှိသမျှ»
  (the second ajjhatta / bahiddhā set is kept, as the Pāli repeats it); seyyathidaṃ = «ဆိုလိုသည်မှာ».
- New lists (body parts, metals and stones, liquids, fires, winds, openings) in plain modern words.
- Suttanta finite verbs end in «၏» as pi-1 ^1-1377 (ဖြစ်စေ၏ …, ဝင်စား၍ နေ၏); idha = «ဤသာသနာ၌» for a monk /
  disciple (pi-1 ^1-1377), «ဤလောက၌» for anyone (pi-1 Idhekacco).
- Mid-sentence «…, na vattabbā – "X"ti» (after siyā clauses, no subject) = «… သို့သော် – “X”ဟု ခေါ်ဆို၍ မရ».

## Unsure Pāli / to confirm
- sajjhaṃ vs rajataṃ (both «silver» in the English rails): sajjhaṃ = «ငွေဖြူ», rajataṃ = «ငွေ» (pi-1 rajata).
- masāragallaṃ = «မြ» (a gem; exact stone uncertain); lohitaṅko = «ပတ္တမြား».
- verambhavātā = «လေပွေ», kāḷavātā = «လေမည်း», uppalakavātā = «ထိုးဖောက်သကဲ့သို့ ဖြစ်သော လေ».
- raso in the external water list = sap («အမြစ် အရည်» …), not taste (pi-1 rasa list «အမြစ် အရသာ» …).
- hadayaṃ in the body list = the organ «နှလုံး» (citta list: «နှလုံးသား»); ñātī = «ဆွေမျိုး» (pi-1 lobha list has the
  same Burmese for paṭibandhu).
- nekkhamma = «ကာမမှ ထွက်မြောက်ခြင်း» (no pi-1 value found).
- ch3 ^2-187 «Nava dhātuyo anidassanaappaṭighā» (expected sappaṭighā?) translated as written.

## Source slips (read as noted)
- ch2 ^2-159 «jīvhindriyampetaṃ» read as jivhindriyampetaṃ.
- ch2 ^2-171 (Dukaṃ) «"saṃyojanañceva saṃyojaniya"ntipi» (ca missing): read as «… saṃyojaniyañcā"tipi».
- ch2 Dukaṃ «"upādāniyañceva upādānasampayuttañcā"ti» read as upādānañceva …; «siyā upādānasampayuttaupādāniyā»
  read as upādānavippayuttaupādāniyā; «kilesasampayuttā ceva no ca na kilesā» read as «… no ca kilesā».
- ch3 ^2-184 saṅkhārakkhandha «atthi hetu, atthi ahetu» read as «atthi na hetu» (as ch2).
- ch3 ^2-188 (Dukaṃ) «"parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā"» read as two items (as ch2).
- ch3 «Sattadhātuyo» (joined) = «satta dhātuyo».
- ch4 ^2-206 «micchā ājīvā ārati» = pi-1 «micchāājīvā ārati» (spelling).
- ch4 Dukaṃ «Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā.» (stop missing): joined with «၊».
- ch4 Dukaṃ «Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ» (ajjhattika duka) read as ajjhattikaṃ.
- ch4 Dukaṃ «"upādānañceva upādānasampayuttañcā" tipi», «"kileso ceva kilesasampayuttañcā" tipi»: stray space dropped.
- ch4 «… sammāsamādhi. Ayaṃ vuccati – "dukkhanirodhagāminī paṭipadā".» (dash after vuccati, once): dash kept.
- ch4 «na ca, vata, no jāti …»: no = «to us» (the check counts it as a pronoun, not a negation).

## New terms and strings (generated by make_ch2-4.py)

One «Pāli = Burmese» per line; pi-1 values marked in the code (asserts against the pi-1 rails text). my2_formulas.py and my2-zeroshot-terms.md are not changed.

### Spelling of pi-1 list words (same Burmese as pi-1)

caturassaṃ = as pi-1 caturaṃsaṃ
maṇisaṅkhamuttaveḷuriyassa = as pi-1 maṇisaṅkhamuttāveḷuriyassa
āmagandho = as pi-1 āmakagandho
lambikaṃ = as pi-1 lambilaṃ
asaṅgāhaṇā = as pi-1 asaṃgāhanā
apariyogāhaṇā = as pi-1 apariyogāhanā
apaccavekkhaṇā = as pi-1 apaccavekkhanā
kharigataṃ = as pi-1 kharagataṃ

### Headings and colophons

Āyatanavibhaṅgo = အာရုံခံ နယ်ပယ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Āyatanavibhaṅgo niṭṭhito = “အာရုံခံ နယ်ပယ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း” ပြီးဆုံးပြီ
Dhātuvibhaṅgo = ဓာတ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Dhātuvibhaṅgo niṭṭhito = “ဓာတ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း” ပြီးဆုံးပြီ
Saccavibhaṅgo = သစ္စာများကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Saccavibhaṅgo niṭṭhito = “သစ္စာများကို ခွဲခြမ်းစိတ်ဖြာခြင်း” ပြီးဆုံးပြီ
Dukkhasaccaṃ = ဒုက္ခ သစ္စာ
Samudayasaccaṃ = ဖြစ်ပေါ်ခြင်း သစ္စာ
Nirodhasaccaṃ = ချုပ်ငြိမ်းခြင်း သစ္စာ
Maggasaccaṃ = မဂ် သစ္စာ

### Subjects (pañhāpucchaka)

dasāyatanā = အာရုံခံ နယ်ပယ် ဆယ်ပါး
dvāyatanā = အာရုံခံ နယ်ပယ် နှစ်ပါး
pañcāyatanā = အာရုံခံ နယ်ပယ် ငါးပါး
cattāro āyatanā = အာရုံခံ နယ်ပယ် လေးပါး
ekādasāyatanā = အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး
navāyatanā = အာရုံခံ နယ်ပယ် ကိုးပါး
chāyatanā = အာရုံခံ နယ်ပယ် ခြောက်ပါး
soḷasa dhātuyo = ဓာတ် ဆယ့်ခြောက်ပါး
dve dhātuyo = ဓာတ် နှစ်ပါး
dasa dhātuyo = ဓာတ် ဆယ်ပါး
pañca dhātuyo = ဓာတ် ငါးပါး
pannarasa dhātuyo = ဓာတ် ဆယ့်ငါးပါး
sattarasa dhātuyo = ဓာတ် ဆယ့်ခုနစ်ပါး
cha dhātuyo = ဓာတ် ခြောက်ပါး
nava dhātuyo = ဓာတ် ကိုးပါး
aṭṭha dhātuyo = ဓာတ် ရှစ်ပါး
satta dhātuyo = ဓာတ် ခုနစ်ပါး
ekādasa dhātuyo = ဓာတ် ဆယ့်တစ်ပါး
dvādasa dhātuyo = ဓာတ် ဆယ့်နှစ်ပါး
tisso dhātuyo = ဓာတ် သုံးပါး
sattadhātuyo = ဓာတ် ခုနစ်ပါး
dve saccā = သစ္စာ နှစ်ပါး
tīṇi saccāni = သစ္စာ သုံးပါး

### Topic noun of «atthi T» (abhidhamma part)

manāyatanaṃ = မနော အာရုံခံ နယ်ပယ်

### Characteristics (āyatana suttanta part)

aniccaṃ / aniccā / anicco = မမြဲသော
dukkhaṃ / dukkhā / dukkho (characteristic) = ဒုက္ခ ဖြစ်သော
anattā = အတ္တ မဟုတ်သော
vipariṇāmadhammaṃ / -ā / -o = ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော

### List items

rāgakkhayo = ရာဂ ကုန်ခန်းခြင်း
dosakkhayo = ဒေါသ ကုန်ခန်းခြင်း
mohakkhayo = မောဟ ကုန်ခန်းခြင်း

### Names (elements)

viññāṇadhātu = သိစိတ် ဓာတ်
sukhadhātu = သာယာမှု ဓာတ်
dukkhadhātu = နာကျင်မှု ဓာတ်
somanassadhātu = ဝမ်းမြောက်မှု ဓာတ်
domanassadhātu = စိတ်ဆင်းရဲမှု ဓာတ်
upekkhādhātu = ဥပေက္ခာ ဓာတ်
avijjādhātu = အမှန်ကို မသိမှု ဓာတ်
kāmadhātu = ကာမ ဓာတ်
byāpādadhātu = ဖျက်ဆီးလိုစိတ် ဓာတ်
vihiṃsādhātu = ညှဉ်းပန်းမှု ဓာတ်
nekkhammadhātu = ကာမမှ ထွက်မြောက်ခြင်း ဓာတ်
abyāpādadhātu = ဖျက်ဆီးလိုစိတ် မရှိခြင်း ဓာတ်
avihiṃsādhātu = ညှဉ်းပန်းမှု မရှိခြင်း ဓာတ်
ajjhattikā pathavīdhātu = အတွင်းပိုင်း မြေဓာတ်
bāhirā pathavīdhātu = ပြင်ပ မြေဓာတ်
ajjhattikā āpodhātu = အတွင်းပိုင်း ရေဓာတ်
bāhirā āpodhātu = ပြင်ပ ရေဓာတ်
ajjhattikā tejodhātu = အတွင်းပိုင်း မီးဓာတ်
bāhirā tejodhātu = ပြင်ပ မီးဓာတ်
ajjhattikā vāyodhātu = အတွင်းပိုင်း လေဓာတ်
bāhirā vāyodhātu = ပြင်ပ လေဓာတ်
ajjhattikā ākāsadhātu = အတွင်းပိုင်း ဟင်းလင်းပြင် ဓာတ်
bāhirā ākāsadhātu = ပြင်ပ ဟင်းလင်းပြင် ဓာတ်

### Synonym lists (element definitions)

kharigataṃ = ခက်မာ သဘော ရှိသောအရာ
asamphuṭṭhaṃ maṃsalohitehi = အသားနှင့် သွေးတို့နှင့် မထိတွေ့သောအရာ

### Examples of the elements (seyyathidaṃ – …)

kesā = ဆံပင်
lomā = မွေးညင်း
nakhā = ခြေသည်းလက်သည်း
dantā = သွား
taco = အရေ
maṃsaṃ = အသား
nhāru = အကြော
aṭṭhi = အရိုး
aṭṭhimiñjaṃ = ရိုးတွင်းခြင်ဆီ
vakkaṃ = ကျောက်ကပ်
hadayaṃ = နှလုံး
yakanaṃ = အသည်း
kilomakaṃ = အမြှေး
pihakaṃ = သရက်ရွက်
papphāsaṃ = အဆုတ်
antaṃ = အူမ
antaguṇaṃ = အူသိမ်
udariyaṃ = အစာသစ်
karīsaṃ = အစာဟောင်း
ayo = သံ
lohaṃ = ကြေး
tipu = သံဖြူ
sīsaṃ = ခဲ
sajjhaṃ = ငွေဖြူ
muttā = ပုလဲ
maṇi = ကျောက်မျက်
veḷuriyo = ကြောင်မျက်ရွဲ
saṅkho = ခရုသင်း
silā = ကျောက်ဖျာ
pavāḷaṃ = သန္တာ
rajataṃ = ငွေ
jātarūpaṃ = ရွှေ
lohitaṅko = ပတ္တမြား
masāragallaṃ = မြ
tiṇaṃ = မြက်
kaṭṭhaṃ = ထင်း
sakkharā = ကျောက်စရစ်
kaṭhalaṃ = အိုးခြမ်းကွဲ
bhūmi = မြေ
pāsāṇo = ကျောက်တုံး
pabbato = တောင်
pittaṃ = သည်းခြေ
semhaṃ = သလိပ်
pubbo = ပြည်
lohitaṃ = သွေး
sedo = ချွေး
medo = အဆီခဲ
assu = မျက်ရည်
vasā = အဆီကြည်
kheḷo = တံတွေး
siṅghāṇikā = နှပ်
lasikā = အစေး
muttaṃ = ကျင်ငယ်
mūlaraso = အမြစ် အရည်
khandharaso = ပင်စည် အရည်
tacaraso = အခေါက် အရည်
pattaraso = အရွက် အရည်
puppharaso = ပန်း အရည်
phalaraso = အသီး အရည်
khīraṃ = နွားနို့
dadhi = နို့ချဉ်
sappi = ထောပတ်ကြည်
navanītaṃ = ထောပတ်
telaṃ = ဆီ
madhu = ပျားရည်
phāṇitaṃ = တင်လဲ
bhummāni vā udakāni antalikkhāni vā = မြေပေါ်ရှိ ရေဖြစ်စေ၊ ကောင်းကင်မှ ရေဖြစ်စေ
yena ca santappati = အကြင်အရာဖြင့် ကိုယ် ပူနွေးခြင်း
yena ca jīrīyati = အကြင်အရာဖြင့် အိုမင်းခြင်း
yena ca pariḍayhati = အကြင်အရာဖြင့် ကိုယ် ပူလောင်ခြင်း
yena ca asitapītakhāyitasāyitaṃ sammā pariṇāmaṃ gacchati = အကြင်အရာဖြင့် စားထားသော၊ သောက်ထားသော၊ ခဲထားသော၊ လျက်ထားသော အစာ ကောင်းစွာ ကြေကျက်ခြင်း
kaṭṭhaggi = ထင်း မီး
palālaggi = ကောက်ရိုး မီး
tiṇaggi = မြက် မီး
gomayaggi = နွားချေး မီး
thusaggi = ဖွဲ မီး
saṅkāraggi = အမှိုက် မီး
indaggi = မိုးကြိုး မီး
aggisantāpo = မီး၏ အပူ
sūriyasantāpo = နေ၏ အပူ
kaṭṭhasannicayasantāpo = ထင်းပုံ၏ အပူ
tiṇasannicayasantāpo = မြက်ပုံ၏ အပူ
dhaññasannicayasantāpo = စပါးပုံ၏ အပူ
bhaṇḍasannicayasantāpo = ကုန်ပစ္စည်းပုံ၏ အပူ
uddhaṅgamā vātā = အထက်သို့ တက်သော လေ
adhogamā vātā = အောက်သို့ ဆင်းသော လေ
kucchisayā vātā = ဝမ်းတွင်း၌ ရှိသော လေ
koṭṭhāsayā vātā = အူတွင်း၌ ရှိသော လေ
aṅgamaṅgānusārino vātā = ကိုယ်အင်္ဂါ အသီးသီးသို့ လှည့်လည်သွားသော လေ
satthakavātā = ဓားဖြင့် ထိုးသကဲ့သို့ ဖြစ်သော လေ
khurakavātā = သင်တုန်းဓားဖြင့် ရိတ်သကဲ့သို့ ဖြစ်သော လေ
uppalakavātā = ထိုးဖောက်သကဲ့သို့ ဖြစ်သော လေ
assāso passāso iti vā = ဝင်လေ ထွက်လေ ဟူ၍လည်း
puratthimā vātā = အရှေ့ လေ
pacchimā vātā = အနောက် လေ
uttarā vātā = မြောက် လေ
dakkhiṇā vātā = တောင် လေ
sarajā vātā = ဖုန်ပါသော လေ
arajā vātā = ဖုန်မပါသော လေ
sītā vātā = အေးသော လေ
uṇhā vātā = ပူသော လေ
parittā vātā = အားနည်းသော လေ
adhimattā vātā = ပြင်းထန်သော လေ
kāḷavātā = လေမည်း
verambhavātā = လေပွေ
pakkhavātā = အတောင်ခတ်ရာမှ ဖြစ်သော လေ
supaṇṇavātā = ဂဠုန် အတောင်ခတ်ရာမှ ဖြစ်သော လေ
tālavaṇṭavātā = ထန်းလက် ယပ်ဖြင့် ခတ်သော လေ
vidhūpanavātā = ယပ်တောင်ဖြင့် ခတ်သော လေ
kaṇṇacchiddaṃ = နားပေါက်
nāsacchiddaṃ = နှာခေါင်းပေါက်
mukhadvāraṃ = ခံတွင်းပေါက်
yena ca asitapītakhāyitasāyitaṃ ajjhoharati = အကြင်အရာဖြင့် စားထားသော၊ သောက်ထားသော၊ ခဲထားသော၊ လျက်ထားသော အစာကို မျိုချခြင်း
yattha ca asitapītakhāyitasāyitaṃ santiṭṭhati = အကြင်အရာ၌ စားထားသော၊ သောက်ထားသော၊ ခဲထားသော၊ လျက်ထားသော အစာ တည်နေခြင်း
yena ca asitapītakhāyitasāyitaṃ adhobhāgaṃ nikkhamati = အကြင်အရာဖြင့် စားထားသော၊ သောက်ထားသော၊ ခဲထားသော၊ လျက်ထားသော အစာ အောက်ဘက်သို့ ထွက်ခြင်း

### Synonym lists (vihiṃsā, mettā, karuṇā)

heṭhanā = နှိပ်စက်ခြင်း
viheṭhanā = ညှဉ်းဆဲခြင်း
hiṃsanā = ထိခိုက်နာကျင်စေခြင်း
vihiṃsanā = ညှဉ်းပန်းခြင်း
rosanā = ဒေါသ ထွက်စေခြင်း
virosanā = အလွန် ဒေါသ ထွက်စေခြင်း
parūpaghāto = သူတစ်ပါးကို ထိပါးခြင်း
mettācetovimutti = မေတ္တာဖြင့် စိတ်လွတ်မြောက်မှု
karuṇā = ကရုဏာ
karuṇāyanā = ကရုဏာ ထားခြင်း
karuṇāyitattaṃ = ကရုဏာ ထားသော အဖြစ်
karuṇācetovimutti = ကရုဏာဖြင့် စိတ်လွတ်မြောက်မှု

### Synonym lists (citta)

tajjācakkhuviññāṇadhātu = သက်ဆိုင်ရာ မျက်စိ သိစိတ် ဓာတ်
tajjāsotaviññāṇadhātu = သက်ဆိုင်ရာ နား သိစိတ် ဓာတ်
tajjāghānaviññāṇadhātu = သက်ဆိုင်ရာ နှာခေါင်း သိစိတ် ဓာတ်
tajjājivhāviññāṇadhātu = သက်ဆိုင်ရာ လျှာ သိစိတ် ဓာတ်
tajjākāyaviññāṇadhātu = သက်ဆိုင်ရာ ကိုယ် သိစိတ် ဓာတ်
tajjāmanodhātu = သက်ဆိုင်ရာ မနော ဓာတ်

### Names (truths, suffering)

dukkhaṃ ariyasaccaṃ = ဒုက္ခ အရိယာ သစ္စာ
dukkhasamudayaṃ ariyasaccaṃ = ဒုက္ခ ဖြစ်ပေါ်ခြင်း အရိယာ သစ္စာ
dukkhanirodhaṃ ariyasaccaṃ = ဒုက္ခ ချုပ်ငြိမ်းခြင်း အရိယာ သစ္စာ
dukkhanirodhagāminī paṭipadā ariyasaccaṃ = ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ် အရိယာ သစ္စာ
dukkhasamudayo = ဒုက္ခ ဖြစ်ပေါ်ခြင်း
dukkhanirodho = ဒုက္ခ ချုပ်ငြိမ်းခြင်း
dukkhanirodhagāminī paṭipadā = ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်
dukkhasaccaṃ = ဒုက္ခ သစ္စာ
samudayasaccaṃ = ဖြစ်ပေါ်ခြင်း သစ္စာ
nirodhasaccaṃ = ချုပ်ငြိမ်းခြင်း သစ္စာ
maggasaccaṃ = မဂ် သစ္စာ
jāti = မွေးဖွားခြင်း
jarā = အိုခြင်း
maraṇaṃ = သေခြင်း
soko = စိုးရိမ်ခြင်း
paridevo = ငိုကြွေးခြင်း
domanassaṃ = စိတ်ဆင်းရဲမှု
upāyāso = ပြင်းစွာ ပူပန်ခြင်း
taṇhā = တပ်မက်မှု
appiyehi sampayogo dukkho = မချစ်သော အရာတို့နှင့် ပေါင်းဆုံရခြင်းသည် ဒုက္ခ
piyehi vippayogo dukkho = ချစ်သော အရာတို့နှင့် ကွေကွင်းရခြင်းသည် ဒုက္ခ
yampicchaṃ na labhati tampi dukkhaṃ = အလိုရှိသည်ကို မရခြင်း၊ ထိုသည်လည်း ဒုက္ခ
saṃkhittena pañcupādānakkhandhā dukkhā = အကျဉ်းအားဖြင့် စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော အစုအဝေး ငါးပါးတို့သည် ဒုက္ခ
sammāvācā = မှန်ကန်သော စကား
sammākammanto = မှန်ကန်သော အလုပ်
sammāājīvo = မှန်ကန်သော အသက်မွေးမှု
sammādiṭṭhi = မှန်ကန်သော အယူ
sammāsaṅkappo = မှန်ကန်သော ကြံစည်မှု
sammāvāyāmo = မှန်ကန်သော အားထုတ်မှု
sammāsati = မှန်ကန်သော သတိ
sammāsamādhi = မှန်ကန်သော သမာဓိ
rūpupādānakkhandho = စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော ရုပ် အစုအဝေး
vedanupādānakkhandho = စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော ခံစားမှု အစုအဝေး
saññupādānakkhandho = စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော မှတ်သိမှု အစုအဝေး
saṅkhārupādānakkhandho = စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော ပြုပြင်ဖန်တီးမှု အစုအဝေး
viññāṇupādānakkhandho = စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော သိစိတ် အစုအဝေး

### Synonym lists (truths)

jāti = မွေးဖွားခြင်း
sañjāti = ကောင်းစွာ မွေးဖွားခြင်း
okkanti = သက်ဆင်းခြင်း
abhinibbatti = ထင်ရှားစွာ ပေါ်ထွက်ခြင်း
khandhānaṃ pātubhāvo = အစုအဝေးတို့၏ ထင်ရှား လာခြင်း
āyatanānaṃ paṭilābho = အာရုံခံ နယ်ပယ်တို့ကို ရရှိခြင်း
cuti = စုတေခြင်း
cavanatā = ရွေ့လျောခြင်း
maccu = သေမင်း
maraṇaṃ = သေခြင်း
kālakiriyā = ကွယ်လွန်ခြင်း
khandhānaṃ bhedo = အစုအဝေးတို့၏ ကွဲခြင်း
kaḷevarassa nikkhepo = ကိုယ်ခန္ဓာကို စွန့်ပစ်ခြင်း
jīvitindriyassupacchedo = အသက်၏ စွမ်းရည် ပြတ်စဲခြင်း
soko = စိုးရိမ်ခြင်း
socanā = စိုးရိမ်နေခြင်း
socitattaṃ = စိုးရိမ်ထားသော အဖြစ်
antosoko = အတွင်း စိုးရိမ်ခြင်း
antoparisoko = အတွင်း ပြင်းစွာ စိုးရိမ်ခြင်း
cetaso parijjhāyanā = စိတ်၏ လောင်မြိုက်ခြင်း
domanassaṃ = စိတ်ဆင်းရဲမှု
sokasallaṃ = စိုးရိမ်ခြင်းဟူသော ငြောင့်
ādevo = ငိုခြင်း
paridevo = ငိုကြွေးခြင်း
ādevanā = ငိုနေခြင်း
paridevanā = ငိုကြွေးနေခြင်း
ādevitattaṃ = ငိုထားသော အဖြစ်
paridevitattaṃ = ငိုကြွေးထားသော အဖြစ်
vācā = စကား
palāpo = ပေါက်ကရ ပြောခြင်း
vippalāpo = ကမောက်ကမ ပြောခြင်း
lālappo = မြည်တမ်းခြင်း
lālappanā = မြည်တမ်းနေခြင်း
lālappitattaṃ = မြည်တမ်းထားသော အဖြစ်
āyāso = ပူပန်ခြင်း
upāyāso = ပြင်းစွာ ပူပန်ခြင်း
āyāsitattaṃ = ပူပန်ထားသော အဖြစ်
upāyāsitattaṃ = ပြင်းစွာ ပူပန်ထားသော အဖြစ်
asesavirāganirodho = အကြွင်း မရှိ ကင်းပြတ်ချုပ်ငြိမ်းခြင်း
cāgo = စွန့်လွှတ်ခြင်း
paṭinissaggo = စွန့်ပစ်ခြင်း
mutti = လွတ်မြောက်ခြင်း
anālayo = မတွယ်တာခြင်း
saṅgati = စုဝေးခြင်း
samāgamo = ဆုံဆည်းခြင်း
samodhānaṃ = ပေါင်းစည်းခြင်း
missībhāvo = ရောနှောခြင်း
asaṅgati = မစုဝေးခြင်း
asamāgamo = မဆုံဆည်းခြင်း
asamodhānaṃ = မပေါင်းစည်းခြင်း
amissībhāvo = မရောနှောခြင်း

### The sixty items «X loke piyarūpaṃ sātarūpaṃ»

cakkhuṃ = မျက်စိ
cakkhuviññāṇaṃ = မျက်စိ သိစိတ်
cakkhusamphasso = မျက်စိ၏ တွေ့ထိမှု
cakkhusamphassajā vedanā = မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု
sotaṃ = နား
sotaviññāṇaṃ = နား သိစိတ်
sotasamphasso = နား၏ တွေ့ထိမှု
sotasamphassajā vedanā = နား၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု
ghānaṃ = နှာခေါင်း
ghānaviññāṇaṃ = နှာခေါင်း သိစိတ်
ghānasamphasso = နှာခေါင်း၏ တွေ့ထိမှု
ghānasamphassajā vedanā = နှာခေါင်း၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု
jivhā = လျှာ
jivhāviññāṇaṃ = လျှာ သိစိတ်
jivhāsamphasso = လျှာ၏ တွေ့ထိမှု
jivhāsamphassajā vedanā = လျှာ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု
kāyo = ကိုယ်
kāyaviññāṇaṃ = ကိုယ် သိစိတ်
kāyasamphasso = ကိုယ်၏ တွေ့ထိမှု
kāyasamphassajā vedanā = ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု
mano = မနော
manoviññāṇaṃ = မနော သိစိတ်
manosamphasso = မနော၏ တွေ့ထိမှု
manosamphassajā vedanā = မနော၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု
rūpā = အဆင်းအရောင်
rūpasaññā = အဆင်းအရောင်ကို မှတ်သိမှု
rūpasañcetanā = အဆင်းအရောင်ကို စေ့ဆော်မှု
rūpataṇhā = အဆင်းအရောင်ကို တပ်မက်မှု
rūpavitakko = အဆင်းအရောင်ကို စတင်ကြံစည်မှု
rūpavicāro = အဆင်းအရောင်ကို ဆက်လက်သုံးသပ်မှု
saddā = အသံ
saddasaññā = အသံကို မှတ်သိမှု
saddasañcetanā = အသံကို စေ့ဆော်မှု
saddataṇhā = အသံကို တပ်မက်မှု
saddavitakko = အသံကို စတင်ကြံစည်မှု
saddavicāro = အသံကို ဆက်လက်သုံးသပ်မှု
gandhā = အနံ့
gandhasaññā = အနံ့ကို မှတ်သိမှု
gandhasañcetanā = အနံ့ကို စေ့ဆော်မှု
gandhataṇhā = အနံ့ကို တပ်မက်မှု
gandhavitakko = အနံ့ကို စတင်ကြံစည်မှု
gandhavicāro = အနံ့ကို ဆက်လက်သုံးသပ်မှု
rasā = အရသာ
rasasaññā = အရသာကို မှတ်သိမှု
rasasañcetanā = အရသာကို စေ့ဆော်မှု
rasataṇhā = အရသာကို တပ်မက်မှု
rasavitakko = အရသာကို စတင်ကြံစည်မှု
rasavicāro = အရသာကို ဆက်လက်သုံးသပ်မှု
phoṭṭhabbā = အထိအတွေ့
phoṭṭhabbasaññā = အထိအတွေ့ကို မှတ်သိမှု
phoṭṭhabbasañcetanā = အထိအတွေ့ကို စေ့ဆော်မှု
phoṭṭhabbataṇhā = အထိအတွေ့ကို တပ်မက်မှု
phoṭṭhabbavitakko = အထိအတွေ့ကို စတင်ကြံစည်မှု
phoṭṭhabbavicāro = အထိအတွေ့ကို ဆက်လက်သုံးသပ်မှု
dhammā = သဘောတရား
dhammasaññā = သဘောတရားကို မှတ်သိမှု
dhammasañcetanā = သဘောတရားကို စေ့ဆော်မှု
dhammataṇhā = သဘောတရားကို တပ်မက်မှု
dhammavitakko = သဘောတရားကို စတင်ကြံစည်မှု
dhammavicāro = သဘောတရားကို ဆက်လက်သုံးသပ်မှု

### Wishers (appiya / piya)

anatthakāmā = အကျိုး မရှိခြင်းကို လိုလားသူ
ahitakāmā = အစီးအပွား မရှိခြင်းကို လိုလားသူ
aphāsukakāmā = ချမ်းသာ မရှိခြင်းကို လိုလားသူ
ayogakkhemakāmā = ဘေးကင်းမှု မရှိခြင်းကို လိုလားသူ
atthakāmā = အကျိုးကို လိုလားသူ
hitakāmā = အစီးအပွားကို လိုလားသူ
phāsukakāmā = ချမ်းသာကို လိုလားသူ
yogakkhemakāmā = ဘေးကင်းမှုကို လိုလားသူ

### Relatives (piya)

mātā = မိခင်
pitā = ဖခင်
bhātā = ညီအစ်ကို
bhaginī = ညီအစ်မ
mittā = မိတ်ဆွေတို့
amaccā = အပေါင်းအဖော်တို့
ñātī = ဆွေမျိုးတို့
sālohitā = သွေးချင်းတို့

### Right intention (suttanta)

Nekkhammasaṅkappo = ကာမမှ ထွက်မြောက်ခြင်းဆိုင်ရာ ကြံစည်မှု
abyāpādasaṅkappo = ဖျက်ဆီးလိုစိတ် မရှိခြင်းဆိုင်ရာ ကြံစည်မှု
avihiṃsāsaṅkappo = ညှဉ်းပန်းမှု မရှိခြင်းဆိုင်ရာ ကြံစည်မှု

### Abstentions (veramaṇī = pi-1 ကင်းဝေးခြင်း)

Musāvādā = မုသား ပြောခြင်းမှ
pisuṇāya vācāya = ကုန်းတိုက်သော စကားမှ
pharusāya vācāya = ကြမ်းတမ်းသော စကားမှ
samphappalāpā = အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားမှ
Pāṇātipātā = သူ့အသက်ကို သတ်ခြင်းမှ
adinnādānā = မပေးသည်ကို ယူခြင်းမှ
kāmesumicchācārā = ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ

### Abhidhamma part: what is suffering / its arising

taṇhā = တပ်မက်မှုလည်း
avasesā ca kilesā = ကြွင်းကျန်သော ကိလေသာတို့လည်း
avasesā ca akusalā dhammā = ကြွင်းကျန်သော အကုသိုလ် သဘောတရားတို့လည်း
tīṇi ca kusalamūlāni sāsavāni = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်၏ အမြစ် သုံးပါးတို့လည်း
avasesā ca sāsavā kusalā dhammā = ကြွင်းကျန်သော စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ် သဘောတရားတို့လည်း
sāsavā ca kusalākusalānaṃ dhammānaṃ vipākā = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်နှင့် အကုသိုလ် သဘောတရားတို့၏ အကျိုးတို့လည်း
sāsavā kusalākusalānaṃ dhammānaṃ vipākā = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်နှင့် အကုသိုလ် သဘောတရားတို့၏ အကျိုးတို့လည်း
ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā = ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်၊ ကံ၏ အကျိုးလည်း မဟုတ်သော သဘောတရားများလည်း
sabbañca rūpaṃ = ရုပ် အားလုံးလည်း

### … and its ceasing

taṇhāya = တပ်မက်မှုကိုလည်းကောင်း
avasesānañca kilesānaṃ = ကြွင်းကျန်သော ကိလေသာတို့ကိုလည်းကောင်း
avasesānañca akusalānaṃ dhammānaṃ = ကြွင်းကျန်သော အကုသိုလ် သဘောတရားတို့ကိုလည်းကောင်း
tiṇṇañca kusalamūlānaṃ sāsavānaṃ = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်၏ အမြစ် သုံးပါးတို့ကိုလည်းကောင်း
avasesānañca sāsavānaṃ kusalānaṃ dhammānaṃ = ကြွင်းကျန်သော စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ် သဘောတရားတို့ကိုလည်းကောင်း

### Building blocks

sacca = သစ္စာ
ariya = အရိယာ
dukkha (truth / characteristic) = ဒုက္ခ
dukkha (bodily pain, suttanta definitions; pi-1 soka… list) = ကိုယ်ဆင်းရဲခြင်း
samudaya = ဖြစ်ပေါ်ခြင်း
nirodha = ချုပ်ငြိမ်းခြင်း
nirodhagāminī = ချုပ်ငြိမ်းရာသို့ ရောက်စေသော
seyyathidaṃ = ဆိုလိုသည်မှာ
yaṃ vā panaññampi atthi … = … အခြား … ရှိသမျှလည်း
-paṭisaṃyutta = နှင့် စပ်ယှဉ်သော
uppajjati (finite) = ဖြစ်ပေါ်သည်
uppajjitvā niruddhasamanantarā = ဖြစ်ပေါ်ပြီး ချုပ်ပြီးသည့် အခြားမဲ့၌
Xñca paṭicca Y ca uppajjati = Xကိုလည်းကောင်း၊ Yတို့ကိုလည်းကောင်း မှီ၍ … ဖြစ်ပေါ်သည်
Idha (monk / disciple) = ဤသာသနာ၌
Idha (anyone; pi-1 Idhekacco) = ဤလောက၌
bhikkhu = ရဟန်းသည်
ariyasāvako = အရိယာ တပည့်သည်
avasesa = ကြွင်းကျန်သော
pahānaṃ = ပယ်ခြင်း
piyarūpaṃ = ချစ်ဖွယ် သဘော ရှိသော
sātarūpaṃ = နှစ်သက်ဖွယ်ကောင်းသော သဘော ရှိသော
loke = လောက၌
-dhamma (having the nature of) = သဘော ရှိသော
…, na vattabbā – … (after siyā clauses) = သို့သော်
(?) siglum = အမည်မသိ မူ
evamuparipi = အောက်တွင်လည်း ဤနည်းအတိုင်း
dha. sa. N (cross-reference) = “သဘောတရားများကို စုစည်းရေတွက်ခြင်း” N
Imā cha dhātuyo = ဤတို့သည် ဓာတ် ခြောက်ပါး ဖြစ်ကြသည်
Yā sattesu … = သတ္တဝါတို့အပေါ်၌ … ရှိသမျှ
Dasasu vā āghātavatthūsu = ရန်ငြိုးဖွဲ့ရာ အကြောင်း ဆယ်ပါးတို့၌ဖြစ်စေ
sabbadhammesu vā pana paṭhamasamannāhāro = သို့မဟုတ် သဘောတရား အားလုံးတို့၌ ပထမ နှလုံးသွင်းခြင်း ဖြစ်သော
Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā = ကြွင်းကျန်သော သဘောတရားတို့သည် ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်နှင့် ယှဉ်တွဲသော သဘောတရားများ ဖြစ်ကြသည်

### Count heads

Dvādasāyatanāni = အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး
Cha dhātuyo = ဓာတ် ခြောက်ပါး
Aparāpi cha dhātuyo = နောက်ထပ် ဓာတ် ခြောက်ပါး
Aṭṭhārasa dhātuyo = ဓာတ် ဆယ့်ရှစ်ပါး
Cattāri ariyasaccāni = အရိယာ သစ္စာ လေးပါး
Cattāri saccāni = သစ္စာ လေးပါး
Dvādasannaṃ āyatanānaṃ = အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါးတို့အနက်
Aṭṭhārasannaṃ dhātūnaṃ = ဓာတ် ဆယ့်ရှစ်ပါးတို့အနက်
Catunnaṃ ariyasaccānaṃ = အရိယာ သစ္စာ လေးပါးတို့အနက်
