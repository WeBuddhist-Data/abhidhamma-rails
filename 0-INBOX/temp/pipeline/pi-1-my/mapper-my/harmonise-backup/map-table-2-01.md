# pi-1 Burmese keyword mapping: 2-01 Cittuppādakaṇḍa (new rules and review table)

Written by map_2-01.py. Burmese from the FINAL text of this track only (AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/2-01-cittuppadakandam.md). The approved sample rules 1–11 and values (map-table.md, preamble / 1-matika) are kept; only what is new is listed here.

## New dictionary-form rules for 2-01 (rules 1–11 of map-table.md, approved, apply unchanged)

12. **Relative pronouns** of the definitions («Yo / Yā / Yaṃ tasmiṃ samaye A B C –»): Burmese has no relative
    pronoun; the text builds the relative clause with the attributive «ထိုအချိန်၌ ရှိသော A၊ B၊ C», so Yo / Yā / Yaṃ =
    (no direct equivalent). **ye / Ye** of «ye vā pana tasmiṃ samaye aññepi atthi …» is rendered by a word: the text's
    «… သဘောတရားများ ရှိသမျှလည်း» («whatever there are»), so ye = ရှိသမျှ («လည်း» = vā pana is not the keyword).
    yaṃ yaṃ (of «yaṃ yaṃ vā panārabbha») = မည်သည့်အရာ (text «မည်သည့်အရာကို»).
13. **«samaye X» bigrams** (from «tasmiṃ samaye X»: samaye phasso, samaye cittaṃ, samaye paññā …) = «အချိန်၌ ရှိသော X»:
    the time adverb keeps its locative ၌ (its meaning, as bahiddhā in rule 11), the attributive ရှိသော with which the
    text joins it to X stays (inside the value, rule 1), and ထို (tasmiṃ, not in the keyword) goes. X has its own value.
14. **Absolutives** (indeclinable gerunds) keep the text's conjunctive «၍»: ārabbha = အာရုံပြု၍, ṭhapetvā =
    ချန်ထား၍, paṭicca = အကြောင်းတို့ကို မှီ၍ (with the object «အကြောင်းတို့ကို» by which the text renders
    «depending [on conditions]»).
15. **Finite verbs** that the text renders by a verbal noun keep rule 4 (verb + «သည်»): hirīyati («ရှက်ခြင်း») =
    ရှက်သည်, ottappati («ကြောက်ရွံ့ခြင်း») = ကြောက်ရွံ့သည်. The check accepts «…ခြင်း» for «…သည်».
16. **Synonym lists**: each Pāli synonym = the Burmese item at its position in the definition line (as the 2-01
    synonym table of my_formulas.py places them), in the form the text gives it (…ခြင်း / …မှု / …သော အဖြစ် /
    …သော သဘော / noun). A keyword that is a part of a compound item = the part of the item that renders it:
    ārambho (vīriyārambho) = စတင်ခြင်း, chandatā = ဆန္ဒ, dhuratā = ဝန်, sampaggāho (dhurasampaggāho) = ခိုင်မြဲစွာ
    ထမ်းဆောင်ခြင်း, satthaṃ / pāsādo / āloko / obhāso / pajjoto / ratanaṃ (paññā-X) = ဓား / ပြာသာဒ် / အလင်း /
    အရောင်အဝါ / မီးအိမ် / ရတနာ, bhāvo (kammañña- / paguṇabhāvo) = သဘော, lahu (lahupariṇāmatā) = လျင်မြန်စွာ (the
    adverb as the text builds it), passambhitattaṃ (paṭipassambhitattaṃ) = အေးချမ်းသွားသော အဖြစ်, abhiniropanā
    (cetaso abhiniropanā) = အာရုံသို့ တင်ပို့ခြင်း (cetaso = စိတ်, its ကို goes with it), anusandhānatā (cittassa
    anusandhānatā) = အာရုံနှင့် ဆက်စပ်ထားခြင်း, attamanatā (attamanatā cittassa) = နှစ်သိမ့်ခြင်း; mānasatā
    (avisāhaṭamānasatā = «စိတ် မပြန့်ကျဲသော အဖြစ်») is discontinuous: စိတ် … အဖြစ်. cittassa alone = စိတ် (rule 1).
17. **Fragments without their negative prefix** (rule 8 extended) = the positive part: lubbhanā = မက်မောခြင်း
    (alubbhanā), sārajjanā = စွဲမက်ခြင်း, dussanā = စိတ်ဆိုးခြင်း (adussanā «စိတ်မဆိုးခြင်း»: infixed မ), byāpajjo =
    ညှဉ်းဆဲလိုခြင်း, dandhanatā = နှေးကွေးခြင်း, vitthanatā = တုံ့ဆိုင်းခြင်း, kakkhaḷatā = ကြမ်းတမ်းခြင်း, kathinatā =
    မာကျောခြင်း, jimhatā = ကောက်ကွေးခြင်း, vaṅkatā = ကွေးညွှတ်ခြင်း, kuṭilatā = လိမ်ကောက်ခြင်း, pilāpanatā =
    အပေါ်ယံ ပေါ်လောခြင်း, sammussanatā = မေ့လျော့ခြင်း. The participle **nikkhitta** (anikkhitta-chandatā /
    -dhuratā: «ဆန္ဒကို လက်မလွှတ်ခြင်း», «ဝန်ကို မချထားခြင်း») = လက်လွှတ်သော / ချထားသော (two compounds, two
    Burmese verbs: genuine alternatives, rule 3 «…သော»); **asithila** («မလျော့ရဲဘဲ ကြိုးစားခြင်း») = မလျော့ရဲသော
    (the negative conjunctive «…ဘဲ» normalised to «…သော», as «…၍» in rule 3). The check accepts «ဘဲ» among the
    attributive sources and an infixed မ inside an attributive stem.
18. **kāya** (kāyapassaddhi … kāyujukatā) = စိတ်၏ အဖော်တို့: the approved term for the mental «body» (the feeling,
    perception and formation aggregates, as the text defines it) kept whole; its «တို့» marks the group and keeps it
    apart from cetasika «စိတ်၏ အဖော်» (the one exception to rule 1's dropped plural marker; for review).
19. **Sense by context** (rule 11 extended): rūpa in rūpārammaṇa = the visible object «အဆင်းအရောင်» (sadda / gandha /
    rasa / phoṭṭhabba = အသံ / အနံ့ / အရသာ / အထိအတွေ့; dhamma(-ārammaṇa / -āyatana / -dhātu) = သဘောတရား);
    sātaṃ = the noun «နှစ်သက်ဖွယ်ကောင်းမှု» in the sukha lists («cetasikaṃ sātaṃ»), the attributive
    «နှစ်သက်ဖွယ်ကောင်းသော» in «neva sātaṃ nāsātaṃ» (text «…ကောင်းသည်လည်း မဟုတ်»; asātaṃ = နှစ်သက်ဖွယ်
    မကောင်းသော); -vāro = «ဖော်ပြချက်» (Koṭṭhāsa- / Suññatavāro: exposition) but «အပိုင်း» in bhāṇavāro (recitation
    section; bhāṇa = ရွတ်ဖတ်ရန်); sammā- = မှန်ကန်သော (right: sammādiṭṭhi …; the preamble's «အပြည့်အဝ» belongs to
    sammāsambuddha).
20. **«ye vā pana … aññepi atthi paṭiccasamuppannā arūpino dhammā»**: the text puts «အခြား» (aññe, not a keyword)
    between the attributes and the noun, so arūpino dhammā = ရုပ် မဟုတ်သော … သဘောတရား and samuppannā arūpino dhammā =
    ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော … သဘောတရား (rule 10); arūpino = ရုပ် မဟုတ်သော (the Mātikā value); the contiguous
    arūpīnaṃ dhammānaṃ («ထို ရုပ် မဟုတ်သော သဘောတရားတို့၏») = ရုပ် မဟုတ်သော သဘောတရား (the Mātikā value).
21. **Counts and ordinals**: a keyword with a numeral keeps the text's count (pañcaṅgikaṃ = အင်္ဂါ ငါးပါး ရှိသော,
    caturaṅgiko maggo = အင်္ဂါ လေးပါး ရှိသော မဂ်); a plural without numeral is the bare noun (khandhā, indriyāni,
    balāni, āhārā, dhātuyo, āyatanāni, cittāni); ordinals as the text: Pañcamaṃ … Aṭṭhamaṃ = ပဉ္စမ … အဋ္ဌမ.
22. **Headings**: uppāda = ဖြစ်ပေါ်ခြင်း, Cittuppāda = စိတ် ဖြစ်ပေါ်ခြင်း, kaṇḍaṃ = အခန်း; bhājanī / bhājanīyaṃ
    (Padabhājanī) = ခွဲခြမ်း ဖော်ပြချက် (pada «ပုဒ်အလိုက်» is not in the keyword); Koṭṭhāsa = အစုအပိုင်း (the
    postposition «အလိုက်», «by», goes: rule 1); Suññata = ဆိတ်သုဉ်းကြောင်း (the text's nominal form).

## Presence: chunks matched by a dictionary-form rule (not literally in the segment)

Every other chunk of every value occurs literally in its segment's Burmese (particles that the rules strip follow the chunk in the text). Rule-matched chunks, one row per keyword and chunk (segments listed):

| keyword | chunk | rule | segments |
|---|---|---|---|
| nikkhitta | လက်လွှတ်သော | neg-infix+attr | 1-13 1-22 1-26 1-56 1-76 1-92 1-97 |
| nikkhitta | ချထားသော | attr | 1-13 1-22 1-26 1-56 1-76 1-92 1-97 |
| asithila | မလျော့ရဲသော | attr | 1-13 1-22 1-26 1-56 1-76 1-92 1-97 |
| hirīyati | ရှက်သည် | verb | 1-30 1-38 1-101 |
| ottappati | ကြောက်ရွံ့သည် | verb | 1-31 1-39 1-102 |
| dussanā | စိတ်ဆိုးခြင်း | neg-infix | 1-33 1-36 1-105 |
| sātaṃ | နှစ်သက်ဖွယ်ကောင်းသော | attr | 1-152 1-153 1-154 |
| asātaṃ | မကောင်းသော | attr | 1-152 1-153 1-154 |

## Keyword → Burmese (number of uses)

Source: own = the 2-01 table T_CU, samaye = rule 13, shared = the approved sample tables. Several values = the keyword reads differently by context.

| Pāli keyword | Burmese (uses) | source |
|---|---|---|
| abhiniropanā | အာရုံသို့ တင်ပို့ခြင်း (4) | own |
| abhippasādo | ကြည်ညိုလေးစားခြင်း (4) | own |
| abyāpajjo | မညှဉ်းဆဲလိုခြင်း (3) | own |
| abyāpādo | ဖျက်ဆီးလိုစိတ် မရှိခြင်း (12) | own |
| adandhanatā | မနှေးကွေးခြင်း (2) | own |
| adoso | ဒေါသ မရှိခြင်း (14) | own |
| adukkhamasukhaṃ | မနာကျင် မသာယာသော (3) | own |
| ajimhatā | မကောက်ကွေးခြင်း (2) | own |
| akakkhaḷatā | မကြမ်းတမ်းခြင်း (2) | own |
| akusalānaṃ | အကုသိုလ် (6) | own |
| akusalānaṃ dhammānaṃ | အကုသိုလ် သဘောတရား (6) | own |
| Alobho | လောဘ မရှိခြင်း (2) | own |
| alobho | လောဘ မရှိခြင်း (12) | own |
| amoho | မောဟ မရှိခြင်း (18) | own |
| anabhijjhā | သူ့ဥစ္စာကို မလိုချင်ခြင်း (12) | own |
| anupekkhanatā | အာရုံကို စေ့စေ့ ရှုကြည့်ခြင်း (2) | own |
| anusandhānatā | အာရုံနှင့် ဆက်စပ်ထားခြင်း (2) | own |
| anussati | အဖန်ဖန် အောက်မေ့ခြင်း (7) | own |
| appanā | အာရုံ၌ စိတ်ကို သွင်းခြင်း (4) | own |
| arūpino | ရုပ် မဟုတ်သော (15) | own |
| arūpino dhammā | ရုပ် မဟုတ်သော … သဘောတရား (15) | own |
| arūpīnaṃ | ရုပ် မဟုတ်သော (2) | own |
| arūpīnaṃ dhammānaṃ | ရုပ် မဟုတ်သော သဘောတရား (2) | own |
| asithila | မလျော့ရဲသော (7) | own |
| asārāgo | မတပ်မက်ခြင်း (3) | own |
| asātaṃ | နှစ်သက်ဖွယ် မကောင်းသော (3) | own |
| attamanatā | နှစ်သိမ့်ခြင်း (2) | own |
| avacara | ဘုံနှင့် ဆိုင်သော (1) | own |
| avacaraṃ | ဘုံနှင့် ဆိုင်သော (8) | own |
| avaṭṭhiti | ခိုင်မြဲစွာ တည်တံ့ခြင်း (10) | own |
| avikkhepo | စိတ် မပျံ့လွင့်ခြင်း (23) | own |
| avisāhaṭa | မပြန့်ကျဲသော (10) | own |
| avisāhaṭamānasatā | စိတ် မပြန့်ကျဲသော အဖြစ် (10) | own |
| avisāhāro | မပြန့်ကျဲခြင်း (10) | own |
| Aṭṭhamaṃ | အဋ္ဌမ (1) | own |
| balaṃ | စွမ်းအား (53) | own |
| balāni | စွမ်းအား (8) | own |
| bhājanī | ခွဲခြမ်း ဖော်ပြချက် (1) | own |
| bhājanīyaṃ | ခွဲခြမ်း ဖော်ပြချက် (1) | own |
| bhāvo | သဘော (4) | own |
| bhāṇa | ရွတ်ဖတ်ရန် (2) | own |
| bhūrī | ကျယ်ပြန့်ခြင်း (10) | own |
| byāpajjo | ညှဉ်းဆဲလိုခြင်း (3) | own |
| caturaṅgikaṃ | အင်္ဂါ လေးပါး ရှိသော (2) | own |
| caturaṅgiko | အင်္ဂါ လေးပါး ရှိသော (1) | own |
| caturaṅgiko maggo | အင်္ဂါ လေးပါး ရှိသော မဂ် (2) | own |
| cetanā | စေ့ဆော်မှု (14) | own |
| cetasikaṃ | စိတ်ပိုင်းဆိုင်ရာ (11) | own |
| cetasikaṃ sukhaṃ | စိတ်ပိုင်းဆိုင်ရာ သာယာမှု (8) | own |
| cetasikaṃ sātaṃ | စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ်ကောင်းမှု (8) | own |
| cetasiko | စိတ်ပိုင်းဆိုင်ရာ (7) | own |
| cetasiko vīriyārambho | စိတ်ပိုင်းဆိုင်ရာ ဝီရိယ စတင်ခြင်း (7) | own |
| cetaso | စိတ် (4) | own |
| cetayitattaṃ | စေ့ဆော်ထားသော အဖြစ် (3) | own |
| cetosamphassajaṃ | စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (11) | own |
| cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ | စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မနာကျင် မသာယာသော ခံစားရခြင်း (3) | own |
| cetosamphassajā | စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (8) | own |
| cetosamphassajā adukkhamasukhā vedanā | စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မနာကျင် မသာယာသော ခံစားမှု (3) | own |
| chandatā | ဆန္ဒ (7) | own |
| Chaṭṭhaṃ | ဆဋ္ဌမ (1) | own |
| cintā | စဉ်းစားခြင်း (10) | own |
| Citta | စိတ် (1) | own |
| citta | စိတ် (6) | own |
| cittakammaññatā | စိတ် အသုံးပြုရန် သင့်တော်ခြင်း (10) | own |
| cittalahutā | စိတ် ပေါ့ပါးခြင်း (10) | own |
| cittamudutā | စိတ် ပျော့ပျောင်းခြင်း (10) | own |
| cittapassaddhi | စိတ် ငြိမ်းအေးခြင်း (10) | own |
| cittapāguññatā | စိတ် ကျင့်သားရခြင်း (10) | own |
| cittassa | စိတ် (21) | own |
| cittassa ṭhiti | စိတ်၏ တည်တံ့ခြင်း (10) | own |
| cittassekaggatā | စိတ်၏ စူးစိုက်မှု (13) | own |
| cittaṃ | စိတ် (27) | own |
| cittujukatā | စိတ် ဖြောင့်တန်းခြင်း (10) | own |
| Cittuppāda | စိတ် ဖြစ်ပေါ်ခြင်း (1) | own |
| cittāni | စိတ် (1) | own |
| cāro | သုံးသပ်ခြင်း (2) | own |
| dandhanatā | နှေးကွေးခြင်း (2) | own |
| dhamma | သဘောတရား (21) | own |
| dhammadhātu | သဘောတရား ဓာတ် (10) | own |
| dhammavicayo | သဘောတရားများကို စိစစ်ခြင်း (11) | own |
| dhammā kusalā | ကုသိုလ် သဘောတရား (17) | own |
| dhammāyatanaṃ | သဘောတရား အာရုံခံ နယ်ပယ် (10) | own |
| dhiti | ဇွဲ (7) | own |
| dhuratā | ဝန် (7) | own |
| dhāraṇatā | စွဲမှတ်ထားခြင်း (7) | own |
| dhātu | ဓာတ် (27) | own |
| dhātuyo | ဓာတ် (8) | own |
| diṭṭhi | အယူ (18) | own |
| dussanā | စိတ်ဆိုးခြင်း (3) | own |
| ekaggatā | စူးစိုက်မှု (13) | own |
| gandha | အနံ့ (4) | own |
| hadayaṃ | နှလုံးသား (12) | own |
| hetū | အမြစ် (8) | own |
| hiri | ဒုစရိုက်ကို ရှက်မှု (13) | own |
| hiribalaṃ | ဒုစရိုက်ကို ရှက်မှု၏ စွမ်းအား (13) | own |
| hirī | ဒုစရိုက်ကို ရှက်မှု (1) | own |
| hirīyati | ရှက်သည် (3) | own |
| hāso | ပြုံးရွှင်ခြင်း (2) | own |
| indriyaṃ | စွမ်းရည် (69) | own |
| indriyāni | စွမ်းရည် (8) | own |
| iriyanā | လှုပ်ရှားခြင်း (2) | own |
| jhānaṃ | ဈာန် (8) | own |
| jimhatā | ကောက်ကွေးခြင်း (2) | own |
| jīvita | အသက် (13) | own |
| jīvitindriyaṃ | အသက်၏ စွမ်းရည် (13) | own |
| kakkhaḷatā | ကြမ်းတမ်းခြင်း (2) | own |
| kammaññattaṃ | အသုံးပြုရန် သင့်တော်သော အဖြစ် (2) | own |
| kammaññatā | အသုံးပြုရန် သင့်တော်ခြင်း (11) | own |
| kathinatā | မာကျောခြင်း (2) | own |
| kaṇḍaṃ | အခန်း (1) | own |
| khandhassa | အစုအဝေး (12) | own |
| khandho | အစုအဝေး (36) | own |
| khandhā | အစုအဝေး (8) | own |
| kosallaṃ | ကျွမ်းကျင်ခြင်း (10) | own |
| Koṭṭhāsa | အစုအပိုင်း (2) | own |
| kusala | ကုသိုလ် (7) | own |
| kusalamūlaṃ | ကုသိုလ်၏ အမြစ် (7) | own |
| kusalaṃ | ကုသိုလ် (1) | own |
| kusalaṃ cittaṃ | ကုသိုလ်စိတ် (8) | own |
| kusalā | ကုသိုလ် (17) | own |
| kuṭilatā | လိမ်ကောက်ခြင်း (2) | own |
| Kāma | ကာမ (1) | own |
| kāma | ကာမ (8) | own |
| Kāmāvacara | ကာမဘုံနှင့် ဆိုင်သော (1) | own |
| kāmāvacaraṃ | ကာမဘုံနှင့် ဆိုင်သော (8) | own |
| kāya | စိတ်၏ အဖော်တို့ (15) | own |
| lahu | လျင်မြန်စွာ (2) | own |
| lahutā | ပေါ့ပါးခြင်း (11) | own |
| lubbhanā | မက်မောခြင်း (3) | own |
| maddavatā | နူးညံ့သော အဖြစ် (2) | own |
| maggo | မဂ် (8) | own |
| Mana | မနော (2) | own |
| mana | မနော (22) | own |
| manindriyaṃ | မနော၏ စွမ်းရည် (21) | own |
| mano | မနော (15) | own |
| manosañcetanā | မနော၏ စေ့ဆော်ခြင်း (3) | own |
| Manoviññāṇa | မနော သိစိတ် (2) | own |
| manoviññāṇa | မနော သိစိတ် (19) | own |
| Manoviññāṇadhātu | မနော သိစိတ် ဓာတ် (2) | own |
| manoviññāṇadhātu | မနော သိစိတ် ဓာတ် (19) | own |
| Manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (2) | own |
| manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (15) | own |
| medhā | ဉာဏ်ထက်မြက်ခြင်း (10) | own |
| mudutā | ပျော့ပျောင်းခြင်း (11) | own |
| mānasatā | စိတ် … အဖြစ် (10) | own |
| mānasaṃ | စိတ်နှလုံး (12) | own |
| mūlaṃ | အမြစ် (7) | own |
| nepuññaṃ | နက်နဲသိမ်မွေ့ခြင်း (10) | own |
| nikkamo | ရှေ့သို့ တိုးထွက်ခြင်း (7) | own |
| nikkhitta | လက်လွှတ်သော / ချထားသော (7) | own |
| obhāso | အရောင်အဝါ (10) | own |
| odagyaṃ | စိတ်တက်ကြွခြင်း (2) | own |
| okappanā | စိတ်ချ အားကိုးခြင်း (4) | own |
| ottappa | ဒုစရိုက်ကို ကြောက်ရွံ့မှု (13) | own |
| ottappabalaṃ | ဒုစရိုက်ကို ကြောက်ရွံ့မှု၏ စွမ်းအား (13) | own |
| ottappati | ကြောက်ရွံ့သည် (3) | own |
| ottappaṃ | ဒုစရိုက်ကို ကြောက်ရွံ့မှု (1) | own |
| paccupalakkhaṇā | လက္ခဏာကို အသီးသီး ခွဲခြားခြင်း (10) | own |
| paggāho | စိတ်ကို မြှင့်တင်ခြင်း (10) | own |
| paguṇattaṃ | ကျင့်သားရသော အဖြစ် (2) | own |
| pahāso | အလွန် ပြုံးရွှင်ခြင်း (2) | own |
| pajjoto | မီးအိမ် (10) | own |
| pajānanā | ကွဲပြားစွာ သိခြင်း (11) | own |
| pamodanā | အလွန် ဝမ်းသာခြင်း (2) | own |
| parakkamo | ရဲရင့်စွာ ကြိုးစားခြင်း (7) | own |
| pariṇāyikā | လမ်းပြခြင်း (10) | own |
| passaddhi | ငြိမ်းအေးခြင်း (11) | own |
| passambhanā | အေးချမ်းခြင်း (2) | own |
| passambhitattaṃ | အေးချမ်းသွားသော အဖြစ် (2) | own |
| patodo | နှင်တံ (10) | own |
| pavicayo | သေချာစွာ စိစစ်ခြင်း (10) | own |
| Pañcamaṃ | ပဉ္စမ (1) | own |
| pañcaṅgikaṃ | အင်္ဂါ ငါးပါး ရှိသော (4) | own |
| pañcaṅgiko | အင်္ဂါ ငါးပါး ရှိသော (3) | own |
| paññindriyaṃ | ပညာ၏ စွမ်းရည် (17) | own |
| paññā | ပညာ (20) | own |
| paññābalaṃ | ပညာ၏ စွမ်းအား (17) | own |
| paññāobhāso | ပညာ အရောင်အဝါ (10) | own |
| paññāpajjoto | ပညာ မီးအိမ် (10) | own |
| paññāpāsādo | ပညာ ပြာသာဒ် (10) | own |
| paññāratanaṃ | ပညာ ရတနာ (10) | own |
| paññāsatthaṃ | ပညာ ဓား (10) | own |
| paññāāloko | ပညာ အလင်း (10) | own |
| paṇḍaraṃ | ကြည်လင်သောအရာ (12) | own |
| paṇḍiccaṃ | လိမ္မာခြင်း (10) | own |
| paṭicca | အကြောင်းတို့ကို မှီ၍ (15) | own |
| paṭiccasamuppannā | အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော (15) | own |
| paṭiccasamuppannā arūpino | အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော (15) | own |
| paṭipassambhitattaṃ | လုံးဝ အေးချမ်းသွားသော အဖြစ် (2) | own |
| paṭissati | ပြန်လည် အောက်မေ့ခြင်း (7) | own |
| Phassa | တွေ့ထိမှု (2) | own |
| phassa | တွေ့ထိမှု (1) | own |
| Phasso | တွေ့ထိမှု (5) | own |
| phasso | တွေ့ထိမှု (15) | own |
| phoṭṭhabba | အထိအတွေ့ (4) | own |
| phusanā | ထိခြင်း (4) | own |
| pilāpanatā | အပေါ်ယံ ပေါ်လောခြင်း (7) | own |
| pāguññatā | ကျင့်သားရခြင်း (11) | own |
| pālanā | စောင့်ရှောက်ခြင်း (2) | own |
| pāmojjaṃ | ရွှင်လန်းခြင်း (2) | own |
| pāpakānaṃ | ယုတ်မာသော (6) | own |
| pāsādo | ပြာသာဒ် (10) | own |
| pīti | ပီတိ (9) | own |
| rasa | အရသာ (4) | own |
| ratanaṃ | ရတနာ (10) | own |
| rūpa | အဆင်းအရောင် (8) | own |
| sadda | အသံ (4) | own |
| saddahanā | ယုံကြည်ခြင်း (4) | own |
| Saddhindriyaṃ | ယုံကြည်မှု၏ စွမ်းရည် (2) | own |
| saddhindriyaṃ | ယုံကြည်မှု၏ စွမ်းရည် (13) | own |
| Saddhā | ယုံကြည်မှု (4) | own |
| saddhā | ယုံကြည်မှု (13) | own |
| Saddhābalaṃ | ယုံကြည်မှု၏ စွမ်းအား (2) | own |
| saddhābalaṃ | ယုံကြည်မှု၏ စွမ်းအား (13) | own |
| sahagataṃ | အတူ ဖြစ်သော (8) | own |
| sallakkhaṇā | လက္ခဏာကို ကောင်းစွာ ခွဲခြားခြင်း (10) | own |
| samatho | စိတ်ငြိမ်သက်ခြင်း (19) | own |
| samaye adoso | အချိန်၌ ရှိသော ဒေါသ မရှိခြင်း (3) | samaye |
| samaye alobho | အချိန်၌ ရှိသော လောဘ မရှိခြင်း (3) | samaye |
| samaye cetanā | အချိန်၌ ရှိသော စေ့ဆော်မှု (2) | samaye |
| samaye cetasikaṃ | အချိန်၌ ရှိသော စိတ်ပိုင်းဆိုင်ရာ (7) | samaye |
| samaye cittaṃ | အချိန်၌ ရှိသော စိတ် (12) | samaye |
| samaye cāro | အချိန်၌ ရှိသော သုံးသပ်ခြင်း (2) | samaye |
| samaye paññā | အချိန်၌ ရှိသော ပညာ (11) | samaye |
| samaye phasso | အချိန်၌ ရှိသော တွေ့ထိမှု (4) | samaye |
| samaye saddhā | အချိန်၌ ရှိသော ယုံကြည်မှု (4) | samaye |
| samaye sati | အချိန်၌ ရှိသော သတိ (7) | samaye |
| samaye saññā | အချိန်၌ ရှိသော မှတ်သိမှု (3) | samaye |
| samaye takko | အချိန်၌ ရှိသော တွေးတောခြင်း (4) | samaye |
| sammussanatā | မေ့လျော့ခြင်း (7) | own |
| Sammā | မှန်ကန်သော (2) | own |
| sammā | မှန်ကန်သော (48) | own |
| sampaggāho | ခိုင်မြဲစွာ ထမ်းဆောင်ခြင်း (7) | own |
| sampajaññaṃ | ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း (15) | own |
| sampayuttaṃ | ယှဉ်တွဲသော (4) | own |
| samphassajaṃ | တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (2) | own |
| samphassajā | တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (2) | own |
| samuppannā | ဖြစ်ပေါ်လာသော (11) | own |
| samuppannā arūpino | ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော (15) | own |
| samuppannā arūpino dhammā | ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော … သဘောတရား (15) | own |
| samādhi | သမာဓိ (25) | own |
| samādhibalaṃ | သမာဓိ၏ စွမ်းအား (21) | own |
| samādhindriyaṃ | သမာဓိ၏ စွမ်းရည် (21) | own |
| samāpattiyā | ကျူးလွန်ခြင်း (6) | own |
| saraṇatā | မှတ်မိခြင်း (7) | own |
| sati | သတိ (22) | own |
| satibalaṃ | သတိ၏ စွမ်းအား (18) | own |
| satindriyaṃ | သတိ၏ စွမ်းရည် (18) | own |
| Sattamaṃ | သတ္တမ (1) | own |
| satthaṃ | ဓား (10) | own |
| sañcetanā | စေ့ဆော်ခြင်း (5) | own |
| sañjānanā | မှတ်သိခြင်း (4) | own |
| sañjānitattaṃ | မှတ်သိထားသော အဖြစ် (4) | own |
| saññā | မှတ်သိမှု (32) | own |
| saññākkhandhassa | မှတ်သိမှု အစုအဝေး (6) | own |
| saññākkhandhaṃ | မှတ်သိမှု အစုအဝေး (5) | own |
| saññākkhandho | မှတ်သိမှု အစုအဝေး (14) | own |
| saṃphusanā | တွေ့ထိခြင်း (4) | own |
| saṅkappo | ကြံစည်မှု (15) | own |
| saṅkhāra | ပြုပြင်ဖန်တီးမှု (23) | own |
| saṅkhārakkhandhassa | ပြုပြင်ဖန်တီးမှု အစုအဝေး (6) | own |
| saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး (17) | own |
| saṅkhārena | တိုက်တွန်းမှု (4) | own |
| saṇṭhiti | ကောင်းစွာ တည်တံ့ခြင်း (10) | own |
| somanassa | ဝမ်းမြောက်မှု (8) | own |
| somanassasahagataṃ | ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော (4) | own |
| somanassindriyaṃ | ဝမ်းမြောက်မှု၏ စွမ်းရည် (6) | own |
| sukhaṃ | သာယာမှု (12) | own |
| sukhaṃ vedayitaṃ | သာယာသော ခံစားရခြင်း (8) | own |
| sukhā | သာယာသော (8) | own |
| sukhā vedanā | သာယာသော ခံစားမှု (8) | own |
| Suññata | ဆိတ်သုဉ်းကြောင်း (2) | own |
| sārajjanā | စွဲမက်ခြင်း (3) | own |
| sātaṃ | နှစ်သက်ဖွယ်ကောင်းမှု (8) / နှစ်သက်ဖွယ်ကောင်းသော (3) | own |
| tajjā | သက်ဆိုင်ရာ (16) | own |
| takko | တွေးတောခြင်း (4) | own |
| thāmo | ခွန်အား (7) | own |
| ujukatā | ဖြောင့်တန်းခြင်း (11) | own |
| ujutā | ဖြောင့်ခြင်း (2) | own |
| upalakkhaṇā | လက္ခဏာကို အနီးကပ် ခွဲခြားခြင်း (10) | own |
| upaparikkhā | စူးစမ်းဆန်းစစ်ခြင်း (10) | own |
| upekkhindriyaṃ | ဥပေက္ခာ၏ စွမ်းရည် (3) | own |
| upekkhā | ဥပေက္ခာ (6) | own |
| upekkhāsahagataṃ | ဥပေက္ခာနှင့်အတူ ဖြစ်သော (4) | own |
| uppannaṃ | ဖြစ်ပေါ်လာသော (8) | own |
| uppāda | ဖြစ်ပေါ်ခြင်း (1) | own |
| ussoḷhī | ပြင်းပြသော အားမာန် (7) | own |
| ussāho | စိတ်အားထက်သန်မှု (7) | own |
| uyyāmo | ထကြွ ကြိုးစားခြင်း (7) | own |
| vattanā | လည်ပတ်ခြင်း (2) | own |
| vaṅkatā | ကွေးညွှတ်ခြင်း (2) | own |
| vebhabyā | ခွဲခြမ်းစိတ်ဖြာခြင်း (10) | own |
| Vedanā | ခံစားမှု (9) | own |
| vedanā | ခံစားမှု (30) | own |
| vedanākkhandhassa | ခံစားမှု အစုအဝေး (6) | own |
| vedanākkhandhaṃ | ခံစားမှု အစုအဝေး (5) | own |
| Vedanākkhandho | ခံစားမှု အစုအဝေး (9) | own |
| vedanākkhandho | ခံစားမှု အစုအဝေး (5) | own |
| vedayitaṃ | ခံစားရခြင်း (11) | own |
| vicayo | စိစစ်ခြင်း (11) | own |
| vicāro | ဆက်လက်သုံးသပ်မှု (13) | own |
| vipassanā | ထိုးထွင်းသိမြင်ခြင်း (15) | own |
| vippayuttaṃ | ကင်းကွာသော (4) | own |
| Vitakko | စတင်ကြံစည်မှု (2) | own |
| vitakko | စတင်ကြံစည်မှု (13) | own |
| vitthanatā | တုံ့ဆိုင်းခြင်း (2) | own |
| vitti | ကျေနပ်ခြင်း (2) | own |
| viññāṇa | သိစိတ် (22) | own |
| viññāṇakkhandhassa | သိစိတ် အစုအဝေး (6) | own |
| viññāṇakkhandhaṃ | သိစိတ် အစုအဝေး (5) | own |
| viññāṇakkhandho | သိစိတ် အစုအဝေး (18) | own |
| viññāṇaṃ | သိစိတ် (9) | own |
| vāro | ဖော်ပြချက် (4) / အပိုင်း (2) | own |
| vāyāmo | အားထုတ်မှု (18) | own |
| vīriyabalaṃ | ဝီရိယ၏ စွမ်းအား (18) | own |
| vīriyindriyaṃ | ဝီရိယ၏ စွမ်းရည် (18) | own |
| yapanā | ဆက်လက် ဖြစ်နေခြင်း (2) | own |
| Yaṃ | (no direct equivalent) (23) | own |
| yaṃ yaṃ | မည်သည့်အရာ (8) | own |
| Ye | ရှိသမျှ (4) | own |
| ye | ရှိသမျှ (5) | own |
| Yo | (no direct equivalent) (25) | own |
| Yā | (no direct equivalent) (53) | own |
| yāpanā | ဆက်လက် ရှင်သန်စေခြင်း (2) | own |
| ñāṇa | ဉာဏ် (8) | own |
| ñāṇavippayuttaṃ | ဉာဏ်နှင့် ကင်းကွာသော (4) | own |
| āhāro | အာဟာရ (5) | own |
| āhārā | အာဟာရ (8) | own |
| āloko | အလင်း (10) | own |
| āmodanā | ဝမ်းသာခြင်း (2) | own |
| ārabbha | အာရုံပြု၍ (8) | own |
| ārambho | စတင်ခြင်း (7) | own |
| ārammaṇaṃ | အာရုံ (8) | own |
| āyatanāni | အာရုံခံ နယ်ပယ် (8) | own |
| āyu | သက်တမ်း (2) | own |
| ṭhapetvā | ချန်ထား၍ (5) | own |
| ṭhiti | တည်တံ့ခြင်း (12) | own |
