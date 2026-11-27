# pi-2 Burmese zero-shot, chapter 18-dhammahadayavibhango: working notes

Scope: 18-dhammahadayavibhango.md (the book's last chapter). Brief: burmese-zeroshot-brief.md. Pāli only; no Burmese
translation or nissaya opened, no web search; my2_formulas.py, my2-zeroshot-terms.md and pi-1-my/ only read.

## Status (2026-11-17): done
- Output: AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/18-dhammahadayavibhango.md
  (99 segments, 325 non-empty lines).
- check_chapter_ids / pi-6-mr/check_text_pe / pi-4-mr/check_marks: OK (chk-pe copy deleted).
- check_ch18.py: 0 mismatches; pi-1 reuse 20 / 20 identical. The checker was tested on a corrupted copy
  (number, negation, item, list changes): all 5 corruptions flagged.
- Regenerate: `python3 -I -X utf8 make_ch18.py`; check: `check_ch18.py <pāli> <my>`. Nothing committed.

## Method
- make_ch18.py imports my2_formulas (pi-1 final module read-only) and adds its own tables in memory: count noun
  phrases (number + noun, compounds dvādasāyatanāni …), list items (ITEMS, from F.ITEM / P1.NAMES / termbase),
  predicate terms (TERM, else F.term_my), beings lists, deva names, sentence frames (SENT_FRAMES); unmatched text
  raises Miss.
- Sentences whose Pāli is identical to pi-1 take the pi-1 final Burmese (P1SENT, from the aligned rails text).
  Derived from pi-1 lines (variants removed / full list put in): ^1-1287, ^1-1289, ^1-1291, ^1-1293 (the plane
  definitions, ^2-1020), ^1-1068 (abyākatahetū; for apariyāpanne without «kiriyābyākatesu vā dhammesu»).
- Statements («S T», «siyā T», «na vattabbo T-tipi …») follow the sample pañhāpucchaka frames; here the Pāli has no
  dash and no quotes, so none in Burmese: «Sသည် A သဘောတရား(များ)ဟုလည်းကောင်း၊ … ခေါ်ဆို၍ မရ».
  A chain «A B na C» = full attributives joined by «၊» (as the sample). Each comma group = its own clause.

## Choices / new terms («Pāli = Burmese»)
Dhammahadayavibhaṅgo = သဘောတရားများ၏ နှလုံးသားကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Dhammahadayavibhaṅgo niṭṭhito. = “သဘောတရားများ၏ နှလုံးသားကို ခွဲခြမ်းစိတ်ဖြာခြင်း” ပြီးဆုံးပြီ။
Vibhaṅgapakaraṇaṃ niṭṭhitaṃ. = “ခွဲခြမ်းစိတ်ဖြာခြင်း” ကျမ်း ပြီးဆုံးပြီ။ (pi-1 ^1-1616 pattern)
Sabbasaṅgāhikavāro = အားလုံးကို စုစည်းသော ဖော်ပြချက်
Uppattānuppattivāro = ဖြစ်ပေါ်ခြင်း မဖြစ်ပေါ်ခြင်း ဖော်ပြချက်
Pariyāpannāpariyāpannavāro = ဘဝဘုံ၌ အကျုံးဝင်ခြင်း အကျုံးမဝင်ခြင်း ဖော်ပြချက်
Pariyāpannāpariyāpannaṃ = ဘဝဘုံတို့၌ အကျုံးဝင်သောအရာနှင့် အကျုံးမဝင်သောအရာ
Apariyāpannaṃ (heading) = ဘဝဘုံတို့၌ အကျုံးမဝင်သောအရာ; apariyāpanne = …အရာ၌
Dhammadassanavāro = သဘောတရားများကို ပြသသော ဖော်ပြချက်
Bhūmantaradassanavāro = ဘုံ အသီးသီးကို ပြသသော ဖော်ပြချက်
Uppādakakammaāyuppamāṇavāro = ဖြစ်ပေါ်စေသော ကံနှင့် သက်တမ်း အတိုင်းအတာ ဖော်ပြချက်
Uppādakakammaṃ = ဖြစ်ပေါ်စေသော ကံ; Āyuppamāṇaṃ = သက်တမ်း အတိုင်းအတာ
Abhiññeyyādivāro = ထူးကဲစွာ သိရမည့် သဘောတရား စသည်ကို ပြသသော ဖော်ပြချက်
Sārammaṇānārammaṇavāro = အာရုံ ရှိခြင်း မရှိခြင်း ဖော်ပြချက်
Diṭṭhasutādidassanavāro = မြင်ရသော ကြားရသော စသည်တို့ကို ပြသသော ဖော်ပြချက်
Tikādidassanavāro = သုံးမျိုးတွဲ စသည်တို့ကို ပြသသော ဖော်ပြချက်
Kusalattikaṃ = ကုသိုလ် သုံးမျိုးတွဲ; Vedanātikaṃ = ခံစားမှု သုံးမျိုးတွဲ; Vipākattikaṃ = ကံ၏ အကျိုး သုံးမျိုးတွဲ
Upādinnattikaṃ = ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ; Vitakkattikaṃ = စတင်ကြံစည်မှု သုံးမျိုးတွဲ
Rūpadukaṃ = ရုပ် နှစ်မျိုးတွဲ; Lokiyadukaṃ = လောကနှင့် သက်ဆိုင်သော နှစ်မျိုးတွဲ
Asaññasattā (heading) = အသညသတ်များ; asaññasattānaṃ devānaṃ = အသညသတ် နတ်တို့ (name, rule 1)
kāmadhātu / rūpadhātu / arūpadhātu (realm) = ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ (pi-1 plane names;
  rūpadhātu as list item stays အဆင်းအရောင် ဓာတ်)
kāmadhātuyā (locative) = ကာမဘုံ၌; «kāmadhātuyā pañcakkhandhā» = ကာမဘုံ၌ ရှိသော အစုအဝေး ငါးပါး
kāmadhātupariyāpanna = ကာမဘုံ၌ အကျုံးဝင်သော; na … = ကာမဘုံ၌ အကျုံးဝင်သည် မဟုတ်သော (also rūpa-, arūpa-)
kati N = N မည်မျှ … ရှိသနည်း (sample)
dukkhasaccaṃ = ဒုက္ခ သစ္စာ; samudayasaccaṃ = ဒုက္ခ ဖြစ်ပေါ်ခြင်း သစ္စာ; nirodhasaccaṃ = ဒုက္ခ ချုပ်ငြိမ်းခြင်း သစ္စာ;
  maggasaccaṃ = မဂ် သစ္စာ (pi-1 Dukkhe / dukkhasamudaye / dukkhanirodhe)
Xviññāṇadhātu = X သိစိတ် ဓာတ်; Xsamphasso = X၏ တွေ့ထိမှု; kāyaviññāṇadhātusamphasso = ကိုယ် သိစိတ် ဓာတ်၏ တွေ့ထိမှု
aññātāvindriyaṃ = အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည် (pi-1 2-05); rūpajīvitindriyaṃ = ရုပ် အသက်၏ စွမ်းရည် (new)
alobho kusalahetu = ကုသိုလ် အမြစ် ဖြစ်သော လောဘ မရှိခြင်း (pi-1 ^1-1441); lobho akusalahetu = အကုသိုလ် အမြစ် ဖြစ်သော လောဘ
alobho vipākahetu = ကံ၏ အကျိုး ဖြစ်သော စိတ်၏ အမြစ် ဖြစ်သော လောဘ မရှိခြင်း (pi-1 ^1-1441)
ime tayo kusalahetū = ဤသည်တို့မှာ ကုသိုလ် အမြစ် သုံးပါး ဖြစ်ကြသည် (pi-1 ^1-1067); ime vuccanti "X" = ဤသည်တို့ကို “X”ဟု ခေါ်သည်
X vā Y vā (faculties) = X သို့မဟုတ် Y
upapattikkhaṇe = ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌; upapajjanti = ပြန်လည် ဖြစ်ပေါ်ကြသည်; pātubhavati / -nti = ထင်ရှားလာသည် / ထင်ရှားလာကြသည်
sabbesaṃ / kassaci / kassa / etesaṃ = အားလုံးအား / အချို့အား / မည်သူတို့အား / ဤသူတို့အား; katama (rebirth questions) = မည်သည့်
aparāni / aparā = အခြား; ahetukā pātubhavanti = အမြစ် မရှိဘဲ ထင်ရှားလာကြသည်
kāmāvacarā devā = ကာမဘုံနှင့် ဆိုင်သော နတ်; paṭhamakappikā manussā = ကမ္ဘာဦး လူ; opapātikā petā / asurā / tiracchānagatā
  = အလိုအလျောက် ပေါ်လာသော ပြိတ္တာ / အသုရာ / တိရစ္ဆာန်; nerayikā = ငရဲသား; gabbhaseyyakā sattā = အမိဝမ်းတွင်း၌ ဖြစ်သော သတ္တဝါ
beings + qualifiers = «N1၊ N2 … တို့အနက် Q1၍ Q2သူတို့»: sahetuka အမြစ် ရှိ, ahetuka အမြစ် မရှိ, ñāṇasampayutta ဉာဏ်နှင့် ယှဉ်တွဲ,
  ñāṇavippayutta ဉာဏ်နှင့် ကင်းကွာ, paripuṇṇāyatana အာရုံခံ နယ်ပယ် ပြည့်စုံ, jaccandha မွေးရာပါ မျက်စိ ကန်း,
  jaccabadhira မွေးရာပါ နား ပင်း, jaccandhabadhira မွေးရာပါ မျက်စိ ကန်း၍ နား ပင်း, napuṃsaka လိင် မရှိ;
  ṭhapetvā X = Xတို့ကို ချန်ထား၍ (pi-1)
deva names (proper names): စာတုမဟာရာဇ်, တာဝတိံသာ, ယာမာ, တုသိတာ, နိမ္မာနရတီ, ပရနိမ္မိတဝသဝတ္တီ (pi-1), ဗြဟ္မပါရိသဇ္ဇ,
  ဗြဟ္မပုရောဟိတ, မဟာဗြဟ္မာ, ပရိတ္တာဘ, အပ္ပမာဏာဘ, အာဘဿရ, ပရိတ္တသုဘ, အပ္ပမာဏသုဘ, သုဘကိဏှ, အသညသတ်, ဝေဟပ္ဖိုလ်, အဝိဟာ,
  အတပ္ပါ, သုဒဿာ, သုဒဿီ, အကနိဋ္ဌ (pi-1) + « နတ်»; arūpa planes as pi-1 ^1-1291 (ākāsānañcāyatanūpagā = အဆုံး မရှိသော
  ဟင်းလင်းပြင် နယ်ပယ် ဘုံသို့ ရောက်သော နတ် …)
sammutidevā / upapattidevā / visuddhidevā = သမုတ်ခြင်းအားဖြင့် / ပြန်လည် ဖြစ်ပေါ်ခြင်းအားဖြင့် / စင်ကြယ်ခြင်းအားဖြင့် နတ်
rājāno, deviyo, kumārā = ဘုရင်များ၊ မိဖုရားများ၊ မင်းသားများ; arahanto = ရဟန္တာ
dāna / sīla samādiyitvā / uposathakamma = အလှူကို ပေး၍ / သီလကို ဆောက်တည်၍ / ဥပုသ်ကို စောင့်ထိန်း၍
khattiya- / brāhmaṇa- / gahapatimahāsāla = ကြွယ်ဝသော မင်းမျိုး / ပုဏ္ဏားမျိုး / သူကြွယ်မျိုး; sahabyataṃ = …နှင့် အတူ;
  appekacce = အချို့တို့သည်; kattha = မည်သည့်နေရာ၌
āyuppamāṇa = သက်တမ်း အတိုင်းအတာ; kittakaṃ = မည်မျှ (… ရှိသနည်း); rattindivo = ရက် (တစ်ရက်); māsa = လ; saṃvacchara = နှစ်;
  mānusaka vassa = လူ့ နှစ်; dibba vassa = နတ် နှစ်; gaṇanāya = ရေတွက်ပုံဖြင့်; koṭi = ကုဋေ; satasahassa = သိန်း;
  kappa = ကမ္ဘာ; kappassa tatiyo bhāgo = ကမ္ဘာ၏ သုံးပုံတစ်ပုံ; upaḍḍhakappo = ကမ္ဘာ တစ်ဝက်
paritta / majjhima / paṇīta (jhāna level) = အကန့်အသတ် ရှိသော / အလယ်အလတ် / မွန်မြတ်သော အဆင့်ဖြင့်; bhāvetvā = ပွားများ၍
X-nānattatā = X ကွဲပြားခြင်း: ārammaṇa အာရုံ, manasikāra နှလုံးသွင်းခြင်း, chanda ဆန္ဒ, paṇidhi စိတ်ညွှတ်ခြင်း (pi-1),
  adhimokkha ဆုံးဖြတ်ချက် (new), abhinīhāra ဦးတည် ပို့ဆောင်ခြင်း (new), paññā ပညာ
abhiññeyya = ထူးကဲစွာ သိရမည့်; pariññeyya = ပိုင်းခြား သိရမည့်; bhāvetabba = ပွားများရမည့်; sacchikātabba = မျက်မှောက်ပြုရမည့်;
  pahātabba = ပယ်ရမည့် (pi-1); negatives «…မည် မဟုတ်သော»
sārammaṇārammaṇa / anārammaṇārammaṇa = အာရုံ ရှိသည်ကို / အာရုံ မရှိသည်ကို အာရုံပြုသော (pi-1 parittārammaṇa form)
diṭṭha / suta / muta / viññāta = မြင်ရသော / ကြားရသော / နမ်း မြည်း ထိတွေ့ရသော / သိရသော (pi-1); negatives «…သည် မဟုတ်သော»
verses ^2-1023 / ^2-1029 and the uddāna: fixed lines in make_ch18.py FIXED (puñña ကောင်းမှု, duggati ဆိုးသော လားရာ,
  mahesi မြတ်စွာဘုရား, parinibbanti ပရိနိဗ္ဗာန် ပြုကြသည်, anāsavā စိတ်အစွန်းအထင်း မရှိသူများ)
variants: sigla «(?)» = «(အမည်မသိ မူ)» (no «?» allowed); references dī. ni. 2.7 / a. ni. 3.71 = «; ဒီဃနိကာယ် 2.7» /
  «; အင်္ဂုတ္တရနိကာယ် 3.71» inside the same bracket; kinds in make_ch18.py VAR

## Unsure Pāli / to confirm
- upapatti(kkhaṇa) = «ပြန်လည် ဖြစ်ပေါ်» (rebirth) rather than paṭisandhi words; pi-1 upapanna = «ထိုဘုံ၌ ဖြစ်ပေါ်သော».
- kassaci / avasesānaṃ … ahetukā pātubhavanti = «… အမြစ် မရှိဘဲ ထင်ရှားလာကြသည်» (genitive kept as «အား»).
- Beings lists: the trailing qualifier (paripuṇṇāyatana, jaccandha …, sahetuka ñāṇasampayutta) read as restricting the
  whole group: «… တို့အနက် Q သူတို့».
- kāmadhātu etc. as realm = the pi-1 plane names (not «ကာမ ဓာတ်»), for readability.
- samudayasaccaṃ = «ဒုက္ခ ဖြစ်ပေါ်ခြင်း သစ္စာ» adds ဒုက္ခ (clarification, pi-1 dukkhasamudaye); align with the Saccavibhaṅga agent.
- adhimokkha, abhinīhāra (new words); «Cha ete» = «ဤနတ်ဘုံ ခြောက်ပါး» (နတ်ဘုံ added).

## Source slips (translated as written unless said)
- ^2-992: «Cakkhusamphasso sotasamphasso» (comma missing): no «၊»; «imā vuccatti» = vuccanti.
- ^2-994 / ^2-996 etc.: «Ime vuccanti rūpadhātuyā aṭṭha hetū» without quotes: no quotes.
- ^2-1000: «kāmadhātu pariyāpanno» (space): same term.
- ^2-1012: «kāyindriyaṃ manindriyaṃ» (comma missing): no «၊».
- ^2-1014: «… katame cattāro āhārā pātubhavanti.» question ending with «.»: rendered as a question with «။».
- ^2-1013 variant «avasesā sattā (?)»: sigla «?» rendered «အမည်မသိ မူ».
- ^2-1035: «siyā sārammaṇārammaṇo siyā anārammaṇārammaṇo» (comma missing): no «၊».
- ^2-1039: «siyā dukkhamasukhāya» read as adukkhamasukhāya (a- missing); «sampayuttoti pi» (space): same term.
- ^2-1040: «siyā vipākā siyā vipākadhammadhammā» (comma missing): no «၊».
- ^2-1041: stray «4» after «anupādinnupādāniyo»: kept as « 4» before «။».
- ^2-1042: «siyā avitakkaavicāro siyā na vattabbo» (comma missing); «pañca cittā avitakkaavicārā manodhātu …» (period
  missing): new subject without punctuation.
- ^2-1043: «satta cetanā satta cittā» («…» missing): rendered «စေ့ဆော်မှု ခုနစ်ပါး၊ စိတ် ခုနစ်ပါး».
