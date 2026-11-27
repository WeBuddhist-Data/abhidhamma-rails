# pi-2 Burmese keyword mapping: rules and review table (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း», chapter: 18-dhammahadayavibhango)

Written by map_18.py (a copy of the approved sample's map_all.py). Burmese from the FINAL pi-2 text of this track only (AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters); pi-1 values from AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md. No other Burmese source.

## Verification

| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » | rule-matched chunks | (no direct equivalent) |
|---|---|---|---|---|---|---|
| 18-dhammahadayavibhango | 98 | bad [] | 0 | [] | 63 | 0 |

## Reuse of pi-1

- Keyword uses: 2017; distinct keywords: 588.
- Keywords that pi-1 also has: 252 distinct; their values taken **unchanged from pi-1**: 246 distinct keyword-value pairs, 1192 uses.
- Keywords new in pi-2 (not in the pi-1 mapping): 336 distinct.

### Values that differ from pi-1 for the same keyword

| keyword | pi-2 value (uses) | pi-1 value(s) | reason |
|---|---|---|---|
| Abhiññā | ထူးကဲစွာ သိရမည့် (1) | ထူးကဲစွာ သိ၍ (3) | pi-1 «ထူးကဲစွာ သိ၍» is the absolutive abhiññāya; here the summary verse's abhiññeyyā «ထူးကဲစွာ သိရမည့်» |
| antara | အသီးသီး (1) | ကြားညှပ် (8) | pi-1 «ကြားညှပ်» is antarā (between); bhūmantara = the various planes «ဘုံ အသီးသီး» |
| appamāṇa | အပ္ပမာဏ (1) | အတိုင်းအဆ မရှိသော (10) | part of the deity name appamāṇasubha «အပ္ပမာဏသုဘ» (loan, pi-1 4 rule 19), not the quality |
| dhātu | ဘုံ (15) | ဓာတ် (348) | the planes Kāma- / Rūpa- / Arūpadhātu: the text's «ဘုံ» (C1); the element keeps pi-1 «ဓာတ်» |
| gatā | ရောက်သော (1) | ရောက်ရှိသော (3) | pi-1 «ရောက်ရှိသော» does not occur: the verse's «ရောက်ကြသည်» |
| hadaya | နှလုံးသား (2) | နှလုံး (1) | pi-1 «နှလုံး» is hadayaṅgamā («နှလုံးသို့»); the title's word is «နှလုံးသား» (= pi-1 hadayaṃ, C7) |
| kusalahetu | ကုသိုလ် အမြစ် (3) | ကုသိုလ်၏ အမြစ် (1) | pi-1 «ကုသိုလ်၏ အမြစ်» does not occur: the text's «ကုသိုလ် အမြစ်» (as pi-1 kusalahetū) |
| Rūpadhātu | သိမ်မွေ့သော ရုပ်ဘုံ (3) | အဆင်းအရောင် ဓာတ် (14) | the fine-material plane (heading; text «သိမ်မွေ့သော ရုပ်ဘုံ», C1); the element keeps pi-1 |
| rūpadhātu | သိမ်မွေ့သော ရုပ်ဘုံ (2) | အဆင်းအရောင် ဓာတ် (14) | the fine-material plane in rūpadhātupariyāpanna (text «သိမ်မွေ့သော ရုပ်ဘုံ၌», C1); the element keeps pi-1 |
| samphasso | တွေ့ထိမှု (13) | ထိတွေ့ရ (1) | pi-1 «ထိတွေ့ရ» is sukhasamphasso (the tangible, Rūpakaṇḍa); here contact «တွေ့ထိမှု» (the list noun) |
| sattā | သတ် (1) | သတ္တဝါ (3) | heading Asaññasattā «အသညသတ်များ»: the part of the loan (pi-1 4 rule 19); pi-1 «သတ္တဝါ» in ^2-1029 |
| sutā | ကြားရသော (1) | အကြားအမြင် (2) | pi-1 «အကြားအမြင်» is learning (sutaṃ); here «heard» (diṭṭha suta muta viññāta) «ကြားရသော» |
| Vīsati | နှစ်သောင်း (1) | နှစ်ဆယ် (4) | pi-1 «နှစ်ဆယ်» is twenty; here «Vīsati kappasahassāni» = the fused numeral «နှစ်သောင်း» (C3) |

## Rules

**Binding and unchanged:** the approved pi-2 sample (`map-table.md`: pi-1 rules 1–11 and N1–N11, the sample's
tables, compose rules, context functions and verifier, copied into map_18.py) and the agreed later pi-1 rules
(absolutives keep «…၍»; one sense per segment, the FIRST occurrence in the Pāli segment decides; no « / »
alternatives; numerals keep the text's count with «ပါး»; loans: a fragment of a transliterated name is its part of
the loan, pi-1 4 rule 19). Lookup: CTX -> this chapter's table T_18 -> the sample's tables -> the most frequent
final pi-1 value present in the segment -> compose. The sample's values are not changed.

Rules this chapter uses that pi-1 / the sample already had, applied to the Dhammahadaya's shapes:

- **The twelve lists** (pi-1 rule 1, 4 rule 18): plurals and genitives are the noun (phassā / samphasso =
  တွေ့ထိမှု, indriyā = စွမ်းရည်, saccāni / saccā / saccānaṃ = သစ္စာ, cittānaṃ = စိတ်); counted compounds keep the
  count with «ပါး» (dvādasāyatanāni = အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး, Soḷasa dhātuyo = ဓာတ် ဆယ့်ခြောက်ပါး,
  bāvīsatindriyāni = စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး; bare Soḷasa / Pannarasa / Terasa = ဆယ့်ခြောက်ပါး …).
- **Headings** (pi-1 decision 4): the heading's own Burmese; a -vāro title compound = the heading whole
  (Uppattānuppattivāro, Bhūmantaradassanavāro, Abhiññeyyādivāro …); vāro = ဖော်ပြချက် (pi-1); dassana = ပြသသော,
  ādi = စသည်, Vipākattikaṃ = ကံ၏ အကျိုး သုံးမျိုးတွဲ.
- **Subject + predicate pairs** (pi-1 5 rule 21): dhātuyo kāmadhātupariyāpannā = ဓာတ် … ကာမဘုံ၌ အကျုံးဝင်သော
  (the count between is the gap).
- **Gerundives** «…ရမည့်» (pi-1 pahātabbā): abhiññeyyā = ထူးကဲစွာ သိရမည့်, pariññeyyā = ပိုင်းခြား သိရမည့်,
  bhāvetabbā = ပွားများရမည့်, sacchikātabbā = မျက်မှောက်ပြုရမည့်; the verse's abbreviation Abhiññā the same.
- **Verbs** (rule 4, plural ကြ dropped): pātubhavanti / pātubhavati = ထင်ရှားလာသည်, upapajjanti = ပြန်လည်
  ဖြစ်ပေါ်သည်, cavanti = စုတေသည်; absolutives keep «၍»: bhāvetvā = ပွားများ၍, samādiyitvā = ဆောက်တည်၍,
  katvā (uposathakammaṃ katvā «ဥပုသ်ကို စောင့်ထိန်း၍») = စောင့်ထိန်း၍, deve antokaritvā = နတ်တို့ကို အတွင်း
  ထည့်သွင်း၍ (inner particles stay, rule 1); purpose dative keeps ရန် (mokkhāya = လွတ်မြောက်ရန်).
- **Person nouns** «…သူ» (pi-1 3 rule 18 / 4 rule 20): paripuṇṇāyatanānaṃ = အာရုံခံ နယ်ပယ် ပြည့်စုံသူ,
  jaccandhānaṃ = မွေးရာပါ မျက်စိ ကန်းသူ, badhirānaṃ = နား ပင်းသူ, napuṃsakānaṃ = လိင် မရှိသူ, cintakā =
  စဉ်းစားတတ်သူ; adjectives the text builds as «…သူ» are «…သော» (sahetukānaṃ = အမြစ် ရှိသော, ñāṇavippayuttānaṃ =
  ဉာဏ်နှင့် ကင်းကွာသော, anāsavāti = စိတ်အစွန်းအထင်း မရှိသော).
- **Coordinated compound with the head between** (N5): kusalākusalabyākatā = ကုသိုလ် အကုသိုလ် … ကုသိုလ်လည်း
  မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (text «… သဘောတရားနှင့် …»).
- **-dhamma forms** (N6): nevavipākanavipākadhammadhammo keeps «သဘောတရား» because the text renders it here
  («… မဟုတ်သော သဘောတရား ဖြစ်သည်»), the same value as the plural -dhammā.
- **Deity and plane names** (pi-1 4 rule 19): the loan or its part: paranimmitavasavattī = ပရနိမ္မိတဝသဝတ္တီ,
  vasavattīnaṃ = ဝသဝတ္တီ, nimmāna = နိမ္မာန, ratīnaṃ = ရတီ, mahārājike = မဟာရာဇ် (စာတုမဟာရာဇ်), subhānaṃ = သုဘ,
  kiṇhānaṃ = ကိဏှ, appamāṇa = အပ္ပမာဏ (in appamāṇasubha), Asañña = အသည and sattā = သတ် (heading «အသညသတ်များ»;
  sattā elsewhere = pi-1 သတ္တဝါ); the bigram «X devānaṃ» = the name + « နတ်». kappikānaṃ (paṭhamakappika) =
  ကမ္ဘာဦး, the text's one word for the compound.

## NEW rules (for the user's review)

C1. **dhātu by sense, one sense per segment**: the plane «ဘုံ» in Kāmadhātu / Rūpadhātu / Arūpadhātu (text
    «ကာမဘုံ», «သိမ်မွေ့သော ရုပ်ဘုံ», «ရုပ်မရှိသော ဘုံ»), the element «ဓာတ်» for the eighteen dhātus. The bare
    keyword dhātu takes the sense of its FIRST bare-stem occurrence in the Pāli segment (kāmadhātupariyāpanna …
    = ဘုံ in ^2-999 … ^2-1004 and the headings; cakkhudhātu / asaṅkhatā dhātu = ဓာတ် elsewhere); the locative
    dhātuyā (only in Kāma- / Rūpa- / Arūpadhātuyā) = ဘုံ. rūpadhātu = the plane «သိမ်မွေ့သော ရုပ်ဘုံ» in the
    locative, in -pariyāpanna and as a heading, the visible-object element «အဆင်းအရောင် ဓာတ်» (pi-1) in the lists;
    rūpa / Rūpa follow the first rūpa compound of their own case (sample f_rupa extended: the plane rūpadhātu =
    «သိမ်မွေ့သော ရုပ်»); in the verse kāmarūpagatiṃ (^2-1029) rūpa = «သိမ်မွေ့သော ရုပ်» (CTX).
C2. **upapatti** (rebirth) = «ပြန်လည် ဖြစ်ပေါ်ခြင်း» where the text has the noun (^2-1021 upapattidevā
    «ပြန်လည် ဖြစ်ပေါ်ခြင်းအားဖြင့် နတ်»), else «ပြန်လည် ဖြစ်ပေါ်သော» (the text's «ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ»,
    N11's «…သည့်» ending; two forms of ONE sense, the ALT mechanism of the sample). upapattikkhaṇe = «ပြန်လည်
    ဖြစ်ပေါ်သည့် ခဏ» (rule 1: its locative goes); inside «upapattikkhaṇe X» the ၌ stays («… ခဏ၌ အာရုံခံ နယ်ပယ်
    ဆယ့်တစ်ပါး»; with only the count: «… ခဏ၌ … ဆယ့်တစ်ပါး», the noun ဓာတ် in the gap).
C3. **Fused Burmese numerals** (^2-1023, ^2-1027, ^2-1028): Burmese writes count × hundred / thousand / ten
    thousand as one word, so the fused numeral goes to each Pāli part that has no word of its own (pi-1 4 rule
    19), first occurrence deciding: vassasatāni (dibbāni pañca vassasatāni) = နှစ် ငါးရာ, satāni = ငါးရာ,
    sahassaṃ = တစ်ထောင်, soḷasa (soḷasa vassasatāni) = တစ်ထောင့်ခြောက်ရာ; ^2-1028 Vīsati and sahassāni =
    နှစ်သောင်း, Cattārīsa = လေးသောင်း, Saṭṭhi = ခြောက်သောင်း, Caturāsīti = ရှစ်သောင်းလေးထောင်; with kappa as the
    classifier the bare number (Soḷasa kappā = ဆယ့်ခြောက်, Bāttiṃsa = သုံးဆယ့်နှစ်). Time units keep the text's
    «တစ်» (māso = တစ်လ, saṃvaccharo = တစ်နှစ်, rattindivo = တစ်ရက်: «a month / a year / a day»).
C4. **Causal «…သဖြင့်»** (Pāli ablative āyusaṅkhayā «သက်တမ်း ကုန်ဆုံးသဖြင့်») is dropped like pi-1's «…ကြောင့်»
    (pi-1 2-02 rule 15): āyusaṅkhayā = သက်တမ်း ကုန်ဆုံး, saṅkhayā = ကုန်ဆုံး. The participle saṅkhāto
    (ekasaṅkhāto) keeps the text's conditional «ရေတွက်လျှင်» (the text builds no attributive for it).
C5. **Place adverb** uparito = «အထက်၌» (the locative is its meaning, as bahiddhā in pi-1 rule 11 and N10); the
    noun antare (etasmiṃ antare) = «အကြား» (rule 1).
C6. **Presence check, one more ending**: «Xသော» is accepted against the plural predicate «Xကြသည်»
    (samiddhino «ပြည့်စုံကြသည်»), as the sample accepts «Xသည်» and «Xကြသော».
C7. **hadaya** (title Dhammahadaya) = «နှလုံးသား», the title's word (pi-1 hadayaṃ = နှလုံးသား, 26 uses); pi-1's
    one «နှလုံး» is hadayaṅgamā «နှလုံးသို့».

## Presence: chunks matched by an ending rule (not literally in the segment)

Every other chunk of every value occurs literally in its segment's Burmese.

| segment | keyword | chunk | rule |
|---|---|---|---|
| 2-18-10-4-0 | Upādinna | ဖြစ်သော | attr |
| 2-1007 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1008 | pātubhavanti | ထင်ရှားလာသည် | verb |
| 2-1008 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1009 | pātubhavanti | ထင်ရှားလာသည် | verb |
| 2-1009 | jaccandhānaṃ | ကန်းသော | attr |
| 2-1009 | paripuṇṇāyatanānaṃ | ပြည့်စုံသော | attr |
| 2-1009 | badhirānaṃ | ပင်းသော | attr |
| 2-1009 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1010 | pātubhavanti | ထင်ရှားလာသည် | verb |
| 2-1010 | jaccandhānaṃ | ကန်းသော | attr |
| 2-1010 | paripuṇṇāyatanānaṃ | ပြည့်စုံသော | attr |
| 2-1010 | badhirānaṃ | ပင်းသော | attr |
| 2-1010 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1011 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1012 | pātubhavanti | ထင်ရှားလာသည် | verb |
| 2-1012 | sampayuttānaṃ | ယှဉ်တွဲသော | attr |
| 2-1012 | jaccandhānaṃ | ကန်းသော | attr |
| 2-1012 | paripuṇṇāyatanānaṃ | ပြည့်စုံသော | attr |
| 2-1012 | badhirānaṃ | ပင်းသော | attr |
| 2-1012 | vippayuttānaṃ | ကင်းကွာသော | attr |
| 2-1012 | ñāṇavippayuttānaṃ | ကင်းကွာသော | attr |
| 2-1012 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1012 | sahetukānaṃ | ရှိသော | attr |
| 2-1013 | pātubhavanti | ထင်ရှားလာသည် | verb |
| 2-1013 | sampayuttānaṃ | ယှဉ်တွဲသော | attr |
| 2-1013 | vippayuttānaṃ | ကင်းကွာသော | attr |
| 2-1013 | ñāṇavippayuttānaṃ | ကင်းကွာသော | attr |
| 2-1013 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1014 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1015 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1016 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1017 | aphassakā | မရှိသော | attr |
| 2-1017 | avedanakā | မရှိသော | attr |
| 2-1017 | acetanakā | မရှိသော | attr |
| 2-1017 | acittakā | မရှိသော | attr |
| 2-1017 | anāhārā | မရှိသော | attr |
| 2-1017 | asaññakā | မရှိသော | attr |
| 2-1017 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1017 | ahetukā | မရှိသော | attr |
| 2-1018 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1019 | upapatti | ဖြစ်ပေါ်သော | attr |
| 2-1020 | samāpannassa | ဝင်စားသော | attr |
| 2-1020 | vihārissa | နေထိုင်သော | attr |
| 2-1020 | sukhavihārissa | နေထိုင်သော | attr |
| 2-1020 | upapannassa | ဖြစ်ပေါ်သော | attr |
| 2-1021 | upapajjanti | ဖြစ်ပေါ်သည် | verb |
| 2-1023 | samiddhino | ပြည့်စုံသော | attr |
| 2-1023 | pakāsitāti | ဖော်ပြထားသော | attr |
| 2-1024 | upapajjanti | ဖြစ်ပေါ်သည် | verb |
| 2-1025 | upapajjanti | ဖြစ်ပေါ်သည် | verb |
| 2-1026 | upapajjanti | ဖြစ်ပေါ်သည် | verb |
| 2-1027 | upapajjanti | ဖြစ်ပေါ်သည် | verb |
| 2-1029 | punāgacchanti | ပြန်လာသည် | verb |
| 2-1029 | parinibbanti | ပြုသည် | verb |
| 2-1029 | cavanti | စုတေသည် | verb |
| 2-1029 | bhāventi | ပွားများသည် | verb |
| 2-1029 | gatā | ရောက်သော | attr |
| 2-1029 | Ukkhittā | မြှောက်တင်ခံရသော | attr |
| 2-1029 | nipuṇā | လိမ္မာသော | attr |
| 2-1029 | anāsavāti | မရှိသော | attr |
| 2-1029 | dhīrā | ပညာရှိသော | attr |
| 2-1044 | niṭṭhito | ပြီးဆုံးသော | attr |

## Keyword → Burmese (uses)

«pi-1» = the value is a pi-1 value of the same keyword. Several values = the keyword reads differently by context.

| Pāli keyword | Burmese (uses) |
|---|---|
| abhinīhāra | ဦးတည် ပို့ဆောင်ခြင်း (1) |
| abhiññeyyo | ထူးကဲစွာ သိရမည့် (1) |
| abhiññeyyā | ထူးကဲစွာ သိရမည့် (1) |
| Abhiññeyyādivāro | ထူးကဲစွာ သိရမည့် သဘောတရား စသည်ကို ပြသသော ဖော်ပြချက် (1) |
| Abhiññā | ထူးကဲစွာ သိရမည့် (1) |
| abyākata | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (8, pi-1) |
| abyākatahetū | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ် (9, pi-1) |
| abyākato | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (1) |
| acetanakā | စေ့ဆော်မှု မရှိသော (1) |
| acittakā | စိတ် မရှိသော (1) |
| adoso | ဒေါသ မရှိခြင်း (6, pi-1) |
| adukkhamasukhāya | မနာကျင် မသာယာသော (1, pi-1) |
| ahetukā | အမြစ် မရှိသော (1) |
| akaniṭṭhe deve | အကနိဋ္ဌ နတ် (1) |
| akaniṭṭhānaṃ devānaṃ | အကနိဋ္ဌ နတ် (1) |
| akusala | အကုသိုလ် (13, pi-1) |
| akusalahetu | အကုသိုလ် အမြစ် (3) |
| akusalahetū | အကုသိုလ် အမြစ် (13, pi-1) |
| akusalā | အကုသိုလ် (1, pi-1) |
| Alobho | လောဘ မရှိခြင်း (5, pi-1) |
| alobho | လောဘ မရှိခြင်း (1, pi-1) |
| amoho | မောဟ မရှိခြင်း (6, pi-1) |
| Anaññātaññassāmītindriyaṃ | မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည် (2, pi-1) |
| anaññātaññassāmītindriyaṃ | မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည် (3, pi-1) |
| antara | အသီးသီး (1) |
| antare | အကြား (1) |
| anāhārā | အာဟာရ မရှိသော (1) |
| anārammaṇo | အာရုံ မရှိသော (1) |
| anārammaṇārammaṇā | အာရုံ မရှိသည်ကို အာရုံပြုသော (2) |
| anāsavāti | စိတ်အစွန်းအထင်း မရှိသော (1) |
| Apariyāpannaṃ | ဘဝဘုံတို့၌ အကျုံးမဝင်သော (1, pi-1) |
| apariyāpannā dhammā | ဘဝဘုံတို့၌ အကျုံးမဝင်သော သဘောတရား (1, pi-1) |
| aphassakā | တွေ့ထိမှု မရှိသော (1) |
| appamāṇa | အပ္ပမာဏ (1) |
| appamāṇābhānaṃ | အပ္ပမာဏာဘ (1) |
| arahanto | ရဟန္တာ (1) |
| Arūpa | ရုပ်မရှိသော (6, pi-1) |
| arūpa | ရုပ်မရှိသော (3, pi-1) |
| Arūpadhātu | ရုပ်မရှိသော ဘုံ (3) |
| arūpadhātu | ရုပ်မရှိသော ဘုံ (2) |
| Arūpadhātuyā | ရုပ်မရှိသော ဘုံ (3) |
| arūpadhātuyā | ရုပ်မရှိသော ဘုံ (1) |
| arūpā | ရုပ် မဟုတ်သော (1) |
| arūpāvacarā | ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော (1, pi-1) |
| Asañña | အသည (1) |
| asaññakā | မှတ်သိမှု မရှိသော (1) |
| Asaññasattānaṃ | အသညသတ် (1) |
| asaññasattānaṃ | အသညသတ် (2) |
| Asaññasattānaṃ devānaṃ | အသညသတ် နတ် (1) |
| asaññasattānaṃ devānaṃ | အသညသတ် နတ် (2) |
| asaṅkhatā | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (1, pi-1) |
| asaṅkhatā ca dhātu | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော ဓာတ် (1, pi-1) |
| asurānaṃ | အသုရာ (3) |
| atappānaṃ | အတပ္ပါ (1) |
| atappānaṃ devānaṃ | အတပ္ပါ နတ် (1) |
| Avasesānaṃ | ကြွင်းသော (1) |
| avedanakā | ခံစားမှု မရှိသော (1) |
| avihānaṃ | အဝိဟာ (1) |
| avihānaṃ devānaṃ | အဝိဟာ နတ် (1) |
| Aññindriyaṃ | အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည် (2, pi-1) |
| aññindriyaṃ | အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည် (4, pi-1) |
| aññātāvindriyaṃ | အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည် (5) |
| aṭṭhavīsañca | နှစ်ဆယ့်ရှစ် (1) |
| aṭṭhārasa | ဆယ့်ရှစ်ပါး (4) |
| aṭṭhārasa dhātuyo | ဓာတ် ဆယ့်ရှစ်ပါး (4) |
| Aṭṭhārasannaṃ | ဆယ့်ရှစ်ပါး (1) |
| Aṭṭhārasannaṃ dhātūnaṃ | ဓာတ် ဆယ့်ရှစ်ပါး (1) |
| badhirānaṃ | နား ပင်းသော (3) |
| Bhavaggatampi | ဘဝ၏ ထိပ်ဆုံး (1) |
| bhavo | ဘဝ (1, pi-1) |
| Bhāvayitvā | ပွားများ၍ (1) |
| bhāventi | ပွားများသည် (1) |
| bhāvetabbo | ပွားများရမည့် (1) |
| bhāvetabbā | ပွားများရမည့် (1) |
| bhāvetvā | ပွားများ၍ (4) |
| Bhūmantaradassanavāro | ဘုံ အသီးသီးကို ပြသသော ဖော်ပြချက် (1) |
| brahmānaṃ devānaṃ | ဗြဟ္မာ နတ် (1) |
| brāhmaṇa | ပုဏ္ဏားမျိုး (1) |
| Bāttiṃsa | သုံးဆယ့်နှစ် (1) |
| Bāvīsatindriyā | စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး (1) |
| bāvīsatindriyāni | စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး (4) |
| Cakkhu | မျက်စိ (1, pi-1) |
| cakkhu | မျက်စိ (1, pi-1) |
| Cakkhudhātu | မျက်စိ ဓာတ် (4, pi-1) |
| cakkhudhātu | မျက်စိ ဓာတ် (1, pi-1) |
| Cakkhundriyaṃ | မျက်စိ၏ စွမ်းရည် (4) |
| cakkhundriyaṃ | မျက်စိ၏ စွမ်းရည် (1) |
| Cakkhusamphassa | မျက်စိ၏ တွေ့ထိမှု (3) |
| Cakkhusamphassajā | မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (4, pi-1) |
| Cakkhusamphassajā cetanā | မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော စေ့ဆော်မှု (2) |
| Cakkhusamphassajā saññā | မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မှတ်သိမှု (2) |
| Cakkhusamphassajā vedanā | မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု (2, pi-1) |
| Cakkhusamphasso | မျက်စိ၏ တွေ့ထိမှု (3, pi-1) |
| cakkhuviññāṇa | မျက်စိ သိစိတ် (3, pi-1) |
| cakkhuviññāṇadhātu | မျက်စိ သိစိတ် ဓာတ် (3, pi-1) |
| Cakkhuviññāṇaṃ | မျက်စိ သိစိတ် (1, pi-1) |
| Cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် (4, pi-1) |
| cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် (1, pi-1) |
| Cattārīsa | လေးသောင်း (1) |
| Caturāsīti | ရှစ်သောင်းလေးထောင် (1) |
| Catusaṭṭhi | ခြောက်ဆယ့်လေး (1) |
| Catutthaṃ jhānaṃ | စတုတ္ထ ဈာန် (1, pi-1) |
| cavanti | စုတေသည် (1) |
| cetanā | စေ့ဆော်မှု (26, pi-1) |
| cetasikā | စိတ်၏ အဖော် (1, pi-1) |
| chanda | ဆန္ဒ (1, pi-1) |
| cintakā | စဉ်းစားတတ်သူ (1) |
| citta | စိတ် (1, pi-1) |
| cittaṃ | စိတ် (6, pi-1) |
| cittā | စိတ် (9, pi-1) |
| cittānaṃ | စိတ် (14) |
| cittāni | စိတ် (12, pi-1) |
| Cuddasindriyā | စွမ်းရည် ဆယ့်လေးပါး (3) |
| cuddasindriyāni | စွမ်းရည် ဆယ့်လေးပါး (4) |
| Dasa | ဆယ်ပါး (1, pi-1) |
| dasa | ဆယ်ပါး (1, pi-1) |
| Dasa dhātuyo | ဓာတ် ဆယ်ပါး (6) |
| dasa dhātuyo | ဓာတ် ဆယ်ပါး (2) |
| Dasindriyā | စွမ်းရည် ဆယ်ပါး (4) |
| dasindriyāni | စွမ်းရည် ဆယ်ပါး (4) |
| dassana | ပြသသော (4) |
| dassanavāro | ပြသသော ဖော်ပြချက် (4) |
| Dasāyatanā | အာရုံခံ နယ်ပယ် ဆယ်ပါး (13) |
| dasāyatanāni | အာရုံခံ နယ်ပယ် ဆယ်ပါး (2) |
| deve | နတ် (1, pi-1) |
| deve antokaritvā | နတ်တို့ကို အတွင်း ထည့်သွင်း၍ (1) |
| deviyo | မိဖုရား (1) |
| devā | နတ် (1) |
| devānaṃ | နတ် (12) |
| Dhamma | သဘောတရား (3, pi-1) |
| dhamma | သဘောတရား (2, pi-1) |
| Dhammadhātu | သဘောတရား ဓာတ် (5, pi-1) |
| dhammadhātu | သဘောတရား ဓာတ် (9, pi-1) |
| dhammā | သဘောတရား (1, pi-1) |
| dhammānaṃ | သဘောတရား (3) |
| Dhammāyatanaṃ | သဘောတရား အာရုံခံ နယ်ပယ် (5, pi-1) |
| dhammāyatanaṃ | သဘောတရား အာရုံခံ နယ်ပယ် (9, pi-1) |
| dhātu | ဓာတ် (17, pi-1) · ဘုံ (15) |
| dhātuyo | ဓာတ် (31, pi-1) |
| dhātuyo kāmadhātupariyāpannā | ဓာတ် … ကာမဘုံ၌ အကျုံးဝင်သော (1) |
| dhātuyo pariyāpannā | ဓာတ် … ဘဝဘုံတို့၌ အကျုံးဝင်သော (1) |
| dhātuyā | ဘုံ (18) |
| dhātūnaṃ | ဓာတ် (1, pi-1) |
| dhīrā | ပညာရှိသော (1) |
| dibbāni | နတ် (1) |
| diṭṭhadhamma | မျက်မှောက်ဘဝ (1, pi-1) |
| Diṭṭhasutādidassanavāro | မြင်ရသော ကြားရသော စသည်တို့ကို ပြသသော ဖော်ပြချက် (1) |
| Domanassindriyaṃ | စိတ်ဆင်းရဲမှု၏ စွမ်းရည် (4) |
| domanassindriyaṃ | စိတ်ဆင်းရဲမှု၏ စွမ်းရည် (1) |
| Doso | ဒေါသ (1, pi-1) |
| doso | ဒေါသ (1, pi-1) |
| duggatiṃ | ဆိုးသော လားရာ (1) |
| dukaṃ | နှစ်မျိုးတွဲ (2, pi-1) |
| Dukkha | ဒုက္ခ (18, pi-1) |
| dukkha | ဒုက္ခ (3, pi-1) |
| Dukkhasaccaṃ | ဒုက္ခ သစ္စာ (18) |
| dukkhasaccaṃ | ဒုက္ခ သစ္စာ (3) |
| dukkhindriyaṃ | နာကျင်မှု၏ စွမ်းရည် (1, pi-1) |
| dukkhāya | နာကျင်သော (1, pi-1) |
| dukkhāya vedanāya | နာကျင်သော ခံစားမှု (1, pi-1) |
| dvādasa | ဆယ့်နှစ် (1) |
| dvādasamāsiyo saṃvaccharo | ဆယ့်နှစ်လ … တစ်နှစ် (1) |
| Dvādasannaṃ | ဆယ့်နှစ်ပါး (1) |
| Dvādasannaṃ āyatanānaṃ | အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး (1) |
| Dvādasindriyā | စွမ်းရည် ဆယ့်နှစ်ပါး (1) |
| dvādasindriyāni | စွမ်းရည် ဆယ့်နှစ်ပါး (4) |
| dvādasāyatanāni | အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး (4) |
| Dānaṃ | အလှူ (1) |
| dīghāyukā | သက်တမ်း ရှည်သော (1) |
| ekādasa | ဆယ့်တစ်ပါး (1, pi-1) |
| ekādasa dhātuyo | ဓာတ် ဆယ့်တစ်ပါး (2) |
| Ekādasindriyā | စွမ်းရည် ဆယ့်တစ်ပါး (1) |
| ekādasindriyāni | စွမ်းရည် ဆယ့်တစ်ပါး (2) |
| ekādasāyatanāni | အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး (2) |
| Gabbhaseyyakānaṃ | အမိဝမ်းတွင်း၌ ဖြစ်သော (3) |
| gabbhaseyyakānaṃ | အမိဝမ်းတွင်း၌ ဖြစ်သော (1) |
| gahapati | သူကြွယ်မျိုး (1) |
| gandha | အနံ့ (2, pi-1) |
| Gandhadhātu | အနံ့ ဓာတ် (1, pi-1) |
| gandhadhātu | အနံ့ ဓာတ် (3, pi-1) |
| Gandhāyatanaṃ | အနံ့ အာရုံခံ နယ်ပယ် (1, pi-1) |
| gandhāyatanaṃ | အနံ့ အာရုံခံ နယ်ပယ် (3, pi-1) |
| gatiṃ | လားရာ (1) |
| gatā | ရောက်သော (1) |
| gaṇanāya | ရေတွက်ပုံ (1) |
| ghāna | နှာခေါင်း (2, pi-1) |
| ghānadhātu | နှာခေါင်း ဓာတ် (3, pi-1) |
| ghānasamphassa | နှာခေါင်း၏ တွေ့ထိမှု (3) |
| ghānasamphassajā | နှာခေါင်း၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (4, pi-1) |
| ghānasamphasso | နှာခေါင်း၏ တွေ့ထိမှု (2, pi-1) |
| ghānaviññāṇa | နှာခေါင်း သိစိတ် (2, pi-1) |
| ghānaviññāṇadhātu | နှာခေါင်း သိစိတ် ဓာတ် (2) |
| ghānaviññāṇaṃ | နှာခေါင်း သိစိတ် (1, pi-1) |
| ghānindriyaṃ | နှာခေါင်း၏ စွမ်းရည် (2) |
| ghānāyatanaṃ | နှာခေါင်း အာရုံခံ နယ်ပယ် (3, pi-1) |
| hadaya | နှလုံးသား (2) |
| hetu | အမြစ် (7, pi-1) |
| hetū | အမြစ် (31, pi-1) |
| indriyaṃ | စွမ်းရည် (18, pi-1) |
| indriyā | စွမ်းရည် (15) |
| indriyāni | စွမ်းရည် (16, pi-1) |
| itthindriyaṃ | မိန်းမ၏ စွမ်းရည် (2, pi-1) |
| jaccandhānaṃ | မွေးရာပါ မျက်စိ ကန်းသော (3) |
| Jarā | အိုခြင်း (1, pi-1) |
| Jarāmaraṇa | အိုခြင်း သေခြင်း (1) |
| jhānaṃ | ဈာန် (4, pi-1) |
| jivhindriyaṃ | လျှာ၏ စွမ်းရည် (2) |
| jivhā | လျှာ (2, pi-1) |
| jivhādhātu | လျှာ ဓာတ် (3, pi-1) |
| jivhāsamphassa | လျှာ၏ တွေ့ထိမှု (3) |
| jivhāsamphassajā | လျှာ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (4, pi-1) |
| jivhāsamphasso | လျှာ၏ တွေ့ထိမှု (2, pi-1) |
| jivhāviññāṇa | လျှာ သိစိတ် (2, pi-1) |
| jivhāviññāṇadhātu | လျှာ သိစိတ် ဓာတ် (2) |
| jivhāviññāṇaṃ | လျှာ သိစိတ် (1, pi-1) |
| jivhāyatanaṃ | လျှာ အာရုံခံ နယ်ပယ် (3, pi-1) |
| Jīvitindriyaṃ | အသက်၏ စွမ်းရည် (4, pi-1) |
| jīvitindriyaṃ | အသက်၏ စွမ်းရည် (8, pi-1) |
| Kabaḷīkāro | လုတ်ပြု၍ စားရသော (15, pi-1) |
| Kabaḷīkārāhāro | လုတ်ပြု၍ စားရသော အာဟာရ (2) |
| Kappasahassaṃ | ကမ္ဘာ တစ်ထောင် (1) |
| kappasahassāni | ကမ္ဘာ နှစ်ထောင် (1) · ကမ္ဘာ နှစ်သောင်း (1) |
| Kappassa | ကမ္ဘာ (1) |
| kappikānaṃ | ကမ္ဘာဦး (4) |
| kappā | ကမ္ဘာ (2) |
| karitvā | ပြု၍ (1, pi-1) |
| katvā | စောင့်ထိန်း၍ (1) |
| khandha | အစုအဝေး (1, pi-1) |
| khandho | အစုအဝေး (24, pi-1) |
| khandhā | အစုအဝေး (26, pi-1) |
| khandhānaṃ | အစုအဝေး (14) |
| khattiya | မင်းမျိုး (1) |
| khaṇe | ခဏ (13) |
| kiriyābyākatesu | ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (2) |
| kiṇhānaṃ | ကိဏှ (1) |
| koci | တစ်စုံတစ်ရာ (1) |
| koṭiyo | ကုဋေ (1) |
| kumārā | မင်းသား (1) |
| Kusala | ကုသိုလ် (1, pi-1) |
| kusala | ကုသိုလ် (8, pi-1) |
| kusalahetu | ကုသိုလ် အမြစ် (3) |
| kusalahetū | ကုသိုလ် အမြစ် (8, pi-1) |
| kusalā | ကုသိုလ် (1, pi-1) |
| kusalākusalabyākatā | ကုသိုလ် အကုသိုလ် … ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (1) |
| Kusalānaṃ | ကုသိုလ် (3, pi-1) |
| Kusalānaṃ dhammānaṃ | ကုသိုလ် သဘောတရား (1, pi-1) |
| Kusalānaṃ vā dhammānaṃ | ကုသိုလ် သဘောတရား (2, pi-1) |
| Kāma | ကာမ (12, pi-1) |
| kāma | ကာမ (5, pi-1) |
| Kāmadhātu | ကာမဘုံ (3) |
| kāmadhātu | ကာမဘုံ (2) |
| Kāmadhātuyā | ကာမဘုံ (9) |
| kāmadhātuyā | ကာမဘုံ (1) |
| Kāmāvacarā | ကာမဘုံနှင့် ဆိုင်သော (1, pi-1) |
| kāmāvacarā | ကာမဘုံနှင့် ဆိုင်သော (1, pi-1) |
| Kāmāvacarā dhammā | ကာမဘုံနှင့် ဆိုင်သော သဘောတရား (1) |
| Kāmāvacarānaṃ | ကာမဘုံနှင့် ဆိုင်သော (4) |
| kāya | ကိုယ် (2, pi-1) |
| kāyadhātu | ကိုယ် ဓာတ် (3, pi-1) |
| kāyasamphassa | ကိုယ်၏ တွေ့ထိမှု (3, pi-1) |
| kāyasamphassajā | ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (4, pi-1) |
| kāyasamphasso | ကိုယ်၏ တွေ့ထိမှု (2, pi-1) |
| kāyaviññāṇa | ကိုယ် သိစိတ် (3, pi-1) |
| Kāyaviññāṇadhātu | ကိုယ် သိစိတ် ဓာတ် (1, pi-1) |
| kāyaviññāṇadhātu | ကိုယ် သိစိတ် ဓာတ် (3, pi-1) |
| kāyaviññāṇaṃ | ကိုယ် သိစိတ် (1, pi-1) |
| kāyindriyaṃ | ကိုယ်၏ စွမ်းရည် (2) |
| kāyāyatanaṃ | ကိုယ် အာရုံခံ နယ်ပယ် (3, pi-1) |
| Lobho | လောဘ (2, pi-1) |
| Lokiya | လောကနှင့် သက်ဆိုင်သော (1) |
| lokiyā | လောကနှင့် သက်ဆိုင်သော (1, pi-1) |
| lokuttarā | လောကကို ကျော်လွန်သော (1) |
| Magga | မဂ် (5, pi-1) |
| magga | မဂ် (4, pi-1) |
| maggaṃ | မဂ် (1, pi-1) |
| Maggā | မဂ် (1, pi-1) |
| mahesinā | မြတ်စွာဘုရား (1) |
| mahābrahmānaṃ | မဟာဗြဟ္မာ (1) |
| mahābrahmānaṃ devānaṃ | မဟာဗြဟ္မာ နတ် (1) |
| mahārājike | မဟာရာဇ် (1) |
| mahārājikānaṃ | မဟာရာဇ် (1) |
| mahāsālānaṃ | ကြွယ်ဝသော (1) |
| majjhimaṃ | အလယ်အလတ် (3, pi-1) |
| manasikāra | နှလုံးသွင်းခြင်း (1, pi-1) |
| Manindriyaṃ | မနော၏ စွမ်းရည် (3, pi-1) |
| manindriyaṃ | မနော၏ စွမ်းရည် (4, pi-1) |
| Mano | မနော (2, pi-1) |
| mano | မနော (2, pi-1) |
| Manodhātu | မနော ဓာတ် (3, pi-1) |
| manodhātu | မနော ဓာတ် (8, pi-1) |
| manodhātusamphassa | မနော ဓာတ်၏ တွေ့ထိမှု (3) |
| manodhātusamphassajā | မနော ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (4) |
| Manodhātusamphasso | မနော ဓာတ်၏ တွေ့ထိမှု (3) |
| manodhātusamphasso | မနော ဓာတ်၏ တွေ့ထိမှု (3) |
| manosañcetanāhāro | မနော၏ စေ့ဆော်ခြင်း အာဟာရ (8) |
| Manoviññāṇa | မနော သိစိတ် (12, pi-1) |
| manoviññāṇa | မနော သိစိတ် (10, pi-1) |
| Manoviññāṇadhātu | မနော သိစိတ် ဓာတ် (13, pi-1) |
| manoviññāṇadhātu | မနော သိစိတ် ဓာတ် (14, pi-1) |
| Manoviññāṇadhātusamphassajā | မနော သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (1) |
| Manoviññāṇadhātusamphassajā cetanā | မနော သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော စေ့ဆော်မှု (1) |
| Manoviññāṇadhātusamphassajā saññā | မနော သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မှတ်သိမှု (1) |
| Manoviññāṇadhātusamphassajā vedanā | မနော သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု (1) |
| Manussānaṃ | လူ (1) |
| manussānaṃ | လူ (4) |
| Manussānaṃ gaṇanāya | လူတို့၏ ရေတွက်ပုံ (1) |
| Manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (8, pi-1) |
| manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (5, pi-1) |
| maraṇa | သေခြင်း (1, pi-1) |
| Moho | မောဟ (1, pi-1) |
| moho | မောဟ (2, pi-1) |
| mokkhāya | လွတ်မြောက်ရန် (1) |
| muto | နမ်း မြည်း ထိတွေ့ရသော (1) |
| mutā | နမ်း မြည်း ထိတွေ့ရသော (1) |
| mānusakaṃ vassasataṃ | လူ့ နှစ် တစ်ရာ (1) |
| mānusakāni | လူ့ (1) |
| māso | တစ်လ (1) |
| napuṃsakānaṃ | လိင် မရှိသူ (1) |
| nerayikānaṃ | ငရဲသား (3) |
| nevasaññānāsaññāyatanūpage | မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| Nevasaññānāsaññāyatanūpagānaṃ | မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| nevasaññānāsaññāyatanūpagānaṃ | မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| nevavipākanavipākadhammadhammo | ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား (1) |
| nevavipākanavipākadhammadhammā | ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား (1) |
| nibbānogadhagāminaṃ | နိဗ္ဗာန်ထဲသို့ သက်ဝင် ရောက်ရှိစေသော (1) |
| nicco | မြဲသော (1) |
| nimmāna | နိမ္မာန (2) |
| nimmānaratīnaṃ devānaṃ | နိမ္မာနရတီ နတ် (2) |
| nipakā | ရင့်ကျက်သော (1) |
| nipuṇā | လိမ္မာသော (1) |
| nirayaṃ | ငရဲ (1) |
| Nirodha | ချုပ်ငြိမ်းခြင်း (7, pi-1) |
| nirodha | ချုပ်ငြိမ်းခြင်း (2, pi-1) |
| niṭṭhito | ပြီးဆုံးသော (1, pi-1) |
| nānattatā | ကွဲပြားခြင်း (1) |
| opapātikānaṃ | အလိုအလျောက် ပေါ်လာသော (3) |
| opapātikānaṃ asurānaṃ | အလိုအလျောက် ပေါ်လာသော အသုရာ (3) |
| Opapātikānaṃ petānaṃ | အလိုအလျောက် ပေါ်လာသော ပြိတ္တာ (1) |
| opapātikānaṃ petānaṃ | အလိုအလျောက် ပေါ်လာသော ပြိတ္တာ (2) |
| opapātikānaṃ tiracchānagatānaṃ | အလိုအလျောက် ပေါ်လာသော တိရစ္ဆာန် (3) |
| pahātabbo | ပယ်ရမည့် (1) |
| pahātabbā | ပယ်ရမည့် (1, pi-1) |
| pakaraṇaṃ | ကျမ်း (1) |
| pakāsitāti | ဖော်ပြထားသော (1) |
| pamāṇa | အတိုင်းအတာ (1) |
| pamāṇaṃ | အတိုင်းအတာ (8) |
| Pannarasa | ဆယ့်ငါးပါး (1) |
| Pannarasa dhātuyo | ဓာတ် ဆယ့်ငါးပါး (1) |
| paranimmitavasavattī | ပရနိမ္မိတဝသဝတ္တီ (1) |
| paranimmitavasavattī deve | ပရနိမ္မိတဝသဝတ္တီ နတ် (1) |
| paranimmitavasavattīnaṃ | ပရနိမ္မိတဝသဝတ္တီ (2) |
| paranimmitavasavattīnaṃ devānaṃ | ပရနိမ္မိတဝသဝတ္တီ နတ် (2) |
| parinibbanti | ပရိနိဗ္ဗာန် ပြုသည် (1) |
| paripuṇṇāyatanānaṃ | အာရုံခံ နယ်ပယ် ပြည့်စုံသော (3) |
| parittaṃ | အကန့်အသတ် ရှိသော (3, pi-1) |
| pariyantaṃ | အဆုံးအစွန် (1, pi-1) |
| pariññeyyo | ပိုင်းခြား သိရမည့် (1) |
| pariññeyyā | ပိုင်းခြား သိရမည့် (1) |
| pariññāya | ပိုင်းခြား သိ၍ (1) |
| paññindriyaṃ | ပညာ၏ စွမ်းရည် (7, pi-1) |
| paññā | ပညာ (1, pi-1) |
| paññāsa | ငါးဆယ် (1) |
| paṇidhi | စိတ်ညွှတ်ခြင်း (1, pi-1) |
| paṇītaṃ | မွန်မြတ်သော (3, pi-1) |
| petānaṃ | ပြိတ္တာ (3) |
| phalāni | ဖိုလ် (1, pi-1) |
| phasso | တွေ့ထိမှု (5, pi-1) |
| phassā | တွေ့ထိမှု (21) |
| Phassāhāro | တွေ့ထိမှု အာဟာရ (5) |
| phassāhāro | တွေ့ထိမှု အာဟာရ (3) |
| phoṭṭhabba | အထိအတွေ့ (2, pi-1) |
| phoṭṭhabbadhātu | အထိအတွေ့ ဓာတ် (4, pi-1) |
| phoṭṭhabbāyatanaṃ | အထိအတွေ့ အာရုံခံ နယ်ပယ် (4, pi-1) |
| punāgacchanti | တဖန် ပြန်လာသည် (1) |
| purisindriyaṃ | ယောက်ျား၏ စွမ်းရည် (2, pi-1) |
| purohitānaṃ | ပုရောဟိတ (1) |
| puñña | ကောင်းမှု (1) |
| pārisajjānaṃ | ပါရိသဇ္ဇ (1) |
| pātubhavanti | ထင်ရှားလာသည် (12) |
| pātubhavati | ထင်ရှားလာသည် (8) |
| rasa | အရသာ (2, pi-1) |
| rasadhātu | အရသာ ဓာတ် (4, pi-1) |
| rasāyatanaṃ | အရသာ အာရုံခံ နယ်ပယ် (4, pi-1) |
| rattindivo | တစ်ရက် (1) |
| rattiyo | ည (1) |
| rattiyo māso | ည … တစ်လ (1) |
| ratīnaṃ | ရတီ (2) |
| rājāno | ဘုရင် (1) |
| Rūpa | ရုပ် (19, pi-1) · သိမ်မွေ့သော ရုပ် (6, pi-1) |
| rūpa | သိမ်မွေ့သော ရုပ် (4, pi-1) · အဆင်းအရောင် (2, pi-1) · ရုပ် (1, pi-1) |
| Rūpadhātu | သိမ်မွေ့သော ရုပ်ဘုံ (3) · အဆင်းအရောင် ဓာတ် (1, pi-1) |
| rūpadhātu | အဆင်းအရောင် ဓာတ် (6, pi-1) · သိမ်မွေ့သော ရုပ်ဘုံ (2) |
| Rūpadhātuyā | သိမ်မွေ့သော ရုပ်ဘုံ (3) |
| rūpadhātuyā | သိမ်မွေ့သော ရုပ်ဘုံ (1) |
| rūpajīvitindriyaṃ | ရုပ် အသက်၏ စွမ်းရည် (1) |
| Rūpakkhandho | ရုပ် အစုအဝေး (19, pi-1) |
| rūpakkhandho | ရုပ် အစုအဝေး (2, pi-1) |
| rūpaṃ | ရုပ် (1, pi-1) |
| rūpā | ရုပ် (1) |
| rūpāvacarā | သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော (1, pi-1) |
| Rūpāyatanaṃ | အဆင်းအရောင် အာရုံခံ နယ်ပယ် (1, pi-1) |
| rūpāyatanaṃ | အဆင်းအရောင် အာရုံခံ နယ်ပယ် (6, pi-1) |
| Sabba | အားလုံး (1) |
| sabba | အားလုံး (1) |
| saccaṃ | သစ္စာ (25, pi-1) |
| sacchikātabbo | မျက်မှောက်ပြုရမည့် (1) |
| sacchikātabbā | မျက်မှောက်ပြုရမည့် (1) |
| saccā | သစ္စာ (6) |
| saccānaṃ | သစ္စာ (1) |
| saccāni | သစ္စာ (14) |
| sadda | အသံ (1, pi-1) |
| Saddadhātu | အသံ ဓာတ် (2, pi-1) |
| saddadhātu | အသံ ဓာတ် (3, pi-1) |
| saddhindriyaṃ | ယုံကြည်မှု၏ စွမ်းရည် (7, pi-1) |
| Saddāyatanaṃ | အသံ အာရုံခံ နယ်ပယ် (2, pi-1) |
| saddāyatanaṃ | အသံ အာရုံခံ နယ်ပယ် (3, pi-1) |
| sahassaṃ | တစ်ထောင် (2) |
| sahassāni | နှစ်သောင်း (1) |
| sahetukānaṃ | အမြစ် ရှိသော (1) |
| samiddhino | ပြည့်စုံသော (1) |
| sammuti | သမုတ်ခြင်း (1) |
| sampayuttā | ယှဉ်တွဲသော (1, pi-1) |
| sampayuttānaṃ | ယှဉ်တွဲသော (2) |
| samphassa | တွေ့ထိမှု (3, pi-1) |
| samphasso | တွေ့ထိမှု (13) |
| Samudaya | ဖြစ်ပေါ်ခြင်း (6) |
| samudaya | ဖြစ်ပေါ်ခြင်း (4) |
| samādhindriyaṃ | သမာဓိ၏ စွမ်းရည် (7, pi-1) |
| samādiyitvā | ဆောက်တည်၍ (1) |
| samāpannassa | ဈာန် ဝင်စားသော (1, pi-1) |
| sataṃ | တစ်ရာ (1) |
| satindriyaṃ | သတိ၏ စွမ်းရည် (7, pi-1) |
| sattā | သတ် (1) · သတ္တဝါ (1, pi-1) |
| sattānaṃ | သတ္တဝါ (4, pi-1) |
| satāni | ငါးရာ (2) |
| saññā | မှတ်သိမှု (33, pi-1) |
| saññākkhandho | မှတ်သိမှု အစုအဝေး (8, pi-1) |
| saṃvaccharo | တစ်နှစ် (1) |
| saṅgāhika | စုစည်းသော (1) |
| saṅkhayā | ကုန်ဆုံး (1) |
| Saṅkhāra | ပြုပြင်ဖန်တီးမှု (1, pi-1) |
| saṅkhāra | ပြုပြင်ဖန်တီးမှု (8, pi-1) |
| Saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး (1, pi-1) |
| saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး (8, pi-1) |
| saṅkhārā | ပြုပြင်ဖန်တီးမှု (1, pi-1) |
| saṅkhāto | ရေတွက်လျှင် (1) |
| Saṭṭhi | ခြောက်သောင်း (1) |
| somanassindriyaṃ | ဝမ်းမြောက်မှု၏ စွမ်းရည် (6, pi-1) |
| sota | နား (2, pi-1) |
| sotadhātu | နား ဓာတ် (5, pi-1) |
| sotasamphassa | နား၏ တွေ့ထိမှု (3) |
| sotasamphassajā | နား၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (4, pi-1) |
| sotasamphasso | နား၏ တွေ့ထိမှု (3, pi-1) |
| sotaviññāṇa | နား သိစိတ် (3, pi-1) |
| sotaviññāṇadhātu | နား သိစိတ် ဓာတ် (3) |
| sotaviññāṇaṃ | နား သိစိတ် (1, pi-1) |
| sotindriyaṃ | နား၏ စွမ်းရည် (5) |
| sotāyatanaṃ | နား အာရုံခံ နယ်ပယ် (5, pi-1) |
| Soḷasa | ဆယ့်ခြောက်ပါး (7) · ဆယ့်ခြောက် (1) · တစ်သောင်းခြောက်ထောင် (1) |
| soḷasa | တစ်ထောင့်ခြောက်ရာ (1) |
| Soḷasa dhātuyo | ဓာတ် ဆယ့်ခြောက်ပါး (7) |
| subhānaṃ | သုဘ (1) |
| suciṃ | စင်ကြယ်သော (1) |
| sudassānaṃ | သုဒဿာ (1) |
| sudassānaṃ devānaṃ | သုဒဿာ နတ် (1) |
| sudassīnaṃ devānaṃ | သုဒဿီ နတ် (1) |
| sukhavihārissa | သာယာစွာ နေထိုင်သော (1) |
| sukhindriyaṃ | သာယာမှု၏ စွမ်းရည် (1) |
| sukhāya | သာယာသော (1, pi-1) |
| sukhāya vedanāya | သာယာသော ခံစားမှု (1, pi-1) |
| suto | ကြားရသော (1) |
| sutā | ကြားရသော (1) |
| sārammaṇā | အာရုံ ရှိသော (3) |
| Sārammaṇānārammaṇavāro | အာရုံ ရှိခြင်း မရှိခြင်း ဖော်ပြချက် (1) |
| sārammaṇārammaṇā | အာရုံ ရှိသည်ကို အာရုံပြုသော (2) |
| Sāsavā | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| sīlaṃ | သီလ (1) |
| tadupari | ထိုအထက် (1) |
| Tasmā | ထို့ကြောင့် (1) |
| Tattha | ထိုတို့အနက် (16, pi-1) |
| tejena | တန်ခိုး (1) |
| Terasa | ဆယ့်သုံးပါး (1) |
| Terasindriyā | စွမ်းရည် ဆယ့်သုံးပါး (1) |
| terasindriyāni | စွမ်းရည် ဆယ့်သုံးပါး (2) |
| tikaṃ | သုံးမျိုးတွဲ (5) |
| Tikādidassanavāro | သုံးမျိုးတွဲ စသည်တို့ကို ပြသသော ဖော်ပြချက် (1) |
| tiracchānagatānaṃ | တိရစ္ဆာန် (3) |
| tiṃsa | သုံးဆယ် (1) |
| tusitānaṃ | တုသိတာ (2) |
| tusitānaṃ devānaṃ | တုသိတာ နတ် (2) |
| tāvatiṃsānaṃ | တာဝတိံသာ (2) |
| Ukkhittā | မြှောက်တင်ခံရသော (1) |
| upapajjanti | ပြန်လည် ဖြစ်ပေါ်သည် (5) |
| upapannassa | ထိုဘုံ၌ ဖြစ်ပေါ်သော (1, pi-1) |
| upapatti | ပြန်လည် ဖြစ်ပေါ်သော (13) · ပြန်လည် ဖြစ်ပေါ်ခြင်း (1) |
| upapattikkhaṇe | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ (13) |
| upapattikkhaṇe dasa | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌ … ဆယ်ပါး (1) |
| upapattikkhaṇe dasa dhātuyo | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌ ဓာတ် ဆယ်ပါး (1) |
| upapattikkhaṇe dasindriyāni | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌ စွမ်းရည် ဆယ်ပါး (1) |
| upapattikkhaṇe dasāyatanāni | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌ အာရုံခံ နယ်ပယ် ဆယ်ပါး (1) |
| upapattikkhaṇe ekādasa | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌ … ဆယ့်တစ်ပါး (1) |
| upapattikkhaṇe ekādasa dhātuyo | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌ ဓာတ် ဆယ့်တစ်ပါး (1) |
| upapattikkhaṇe ekādasāyatanāni | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌ အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး (1) |
| upapattikkhaṇe terasindriyāni | ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌ စွမ်းရည် ဆယ့်သုံးပါး (1) |
| uparito | အထက်၌ (1) |
| Upekkhindriyaṃ | ဥပေက္ခာ၏ စွမ်းရည် (1, pi-1) |
| upekkhindriyaṃ | ဥပေက္ခာ၏ စွမ်းရည် (7, pi-1) |
| uposatha | ဥပုသ် (1) |
| Uppattānuppattivāro | ဖြစ်ပေါ်ခြင်း မဖြစ်ပေါ်ခြင်း ဖော်ပြချက် (1) |
| Uppādaka | ဖြစ်ပေါ်စေသော (2) |
| Uppādakakamma | ဖြစ်ပေါ်စေသော ကံ (1) |
| Uppādakakammaṃ | ဖြစ်ပေါ်စေသော ကံ (1) |
| Upādinna | ကံကြောင့် ဖြစ်သော (1) |
| upādinnā | ကံကြောင့် ဖြစ်သော (1) |
| upādāniyā | စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| uttamaṃ | အမြတ်ဆုံး (1) |
| vasavattī | ဝသဝတ္တီ (1, pi-1) |
| vasavattīnaṃ | ဝသဝတ္တီ (2) |
| vassasatāni | နှစ် ငါးရာ (1) |
| vassāni | နှစ် (1) |
| vattabbo | ခေါ်ဆို၍ ရ (1, pi-1) |
| vattabbā | ခေါ်ဆို၍ ရ (1, pi-1) |
| Vedanā | ခံစားမှု (1, pi-1) |
| vedanā | ခံစားမှု (33, pi-1) |
| Vedanākkhandho | ခံစားမှု အစုအဝေး (3, pi-1) |
| vedanākkhandho | ခံစားမှု အစုအဝေး (5, pi-1) |
| vedanāya | ခံစားမှု (1, pi-1) |
| vehapphalānaṃ | ဝေဟပ္ဖိုလ် (1) |
| vehapphalānaṃ devānaṃ | ဝေဟပ္ဖိုလ် နတ် (1) |
| Vibhaṅgapakaraṇaṃ | ခွဲခြမ်းစိတ်ဖြာခြင်း ကျမ်း (1) |
| vibhaṅgo | ခွဲခြမ်းစိတ်ဖြာခြင်း (2) |
| vicārā | ဆက်လက်သုံးသပ်မှု (1, pi-1) |
| vihārissa | နေထိုင်သော (1, pi-1) |
| vippayuttānaṃ | ကင်းကွာသော (2) |
| vipāka | ကံ၏ အကျိုး (3, pi-1) |
| vipākadhammadhammā | အကျိုး ပေးတတ်သော သဘောတရား (1, pi-1) |
| vipākahetu | ကံ၏ အကျိုး ဖြစ်သော စိတ်၏ အမြစ် (3, pi-1) |
| vipākato | အကျိုး ဖြစ်သော စိတ် (3, pi-1) |
| Vipākattikaṃ | ကံ၏ အကျိုး သုံးမျိုးတွဲ (1) |
| visuddhi | စင်ကြယ်ခြင်း (1, pi-1) |
| Vitakka | စတင်ကြံစည်မှု (1, pi-1) |
| vitakka | စတင်ကြံစည်မှု (1, pi-1) |
| vitakkaṃ | စတင်ကြံစည်မှု (1, pi-1) |
| viññāto | သိရသော (1) |
| viññātā | သိရသော (1) |
| viññāṇa | သိစိတ် (8, pi-1) |
| viññāṇadhātu | သိစိတ် ဓာတ် (22) |
| viññāṇakkhandho | သိစိတ် အစုအဝေး (9, pi-1) |
| Viññāṇañcāyatanūpagānaṃ | အဆုံး မရှိသော သိစိတ် နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| viññāṇañcāyatanūpagānaṃ | အဆုံး မရှိသော သိစိတ် နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| viññāṇaṃ | သိစိတ် (1, pi-1) |
| viññāṇāhāro | သိစိတ် အာဟာရ (2) |
| vāro | ဖော်ပြချက် (10, pi-1) |
| vīriyindriyaṃ | ဝီရိယ၏ စွမ်းရည် (7, pi-1) |
| Vīsati | နှစ်သောင်း (1) |
| yāmānaṃ devānaṃ | ယာမာ နတ် (2) |
| ñāṇa | ဉာဏ် (2, pi-1) |
| ñāṇavippayuttānaṃ | ဉာဏ်နှင့် ကင်းကွာသော (2) |
| ābhassarānaṃ | အာဘဿရ (1) |
| ābhānaṃ | ပရိတ္တာဘ (1) |
| ādi | စသည် (3) |
| āhāro | အာဟာရ (22, pi-1) |
| āhārā | အာဟာရ (31, pi-1) |
| Ākiñcaññāyatanūpagānaṃ | ဘာမျှ မရှိသော နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| ākiñcaññāyatanūpagānaṃ | ဘာမျှ မရှိသော နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| ākāsānañcāyatanūpage | အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| Ākāsānañcāyatanūpagānaṃ | အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| ākāsānañcāyatanūpagānaṃ | အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| ānuppatti | ဖြစ်ပေါ်ခြင်း (1) |
| ārammaṇa | အာရုံ (2) |
| ārammaṇo | အာရုံ (1, pi-1) |
| ārammaṇā | အာရုံ (2, pi-1) |
| āsave | စိတ်အစွန်းအထင်း (1) |
| āvacarā | ဘုံနှင့် ဆိုင်သော (1) |
| āvacarānaṃ | ဘုံနှင့် ဆိုင်သော (4) |
| āyatanaṃ | အာရုံခံ နယ်ပယ် (16, pi-1) |
| āyatanā | အာရုံခံ နယ်ပယ် (16, pi-1) |
| āyatanānaṃ | အာရုံခံ နယ်ပယ် (3, pi-1) |
| āyatanāni | အာရုံခံ နယ်ပယ် (16, pi-1) |
| āyatanūpage | နယ်ပယ် ဘုံသို့ ရောက်သော (1) |
| āyatanūpagānaṃ | နယ်ပယ် ဘုံသို့ ရောက်သော (2) |
| Āyu | သက်တမ်း (1, pi-1) |
| āyu | သက်တမ်း (8, pi-1) |
| āyuppamāṇa | သက်တမ်း အတိုင်းအတာ (1) |
| Āyuppamāṇaṃ | သက်တမ်း အတိုင်းအတာ (1) |
| āyuppamāṇaṃ | သက်တမ်း အတိုင်းအတာ (7) |
| āyusaṅkhayā | သက်တမ်း ကုန်ဆုံး (1) |
| ṭhapetvā | ချန်ထား၍ (2, pi-1) |
