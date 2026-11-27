# pi-3 Burmese keyword mapping: rules and review table (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း», chapters 12-ekadasamanayo, 13-dvadasamanayo, 14-terasamanayo, 15-cuddasamanayo)

Written by map_ch12-15.py (a copy of the approved sample's map_all.py, extended). Burmese from the FINAL pi-3 text of this track only (AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters); pi-1 / pi-2 values from AI_translation/burmese/pi-1- and pi-2-keywords-by-reference-pali-burmese-plain.md. No other Burmese source.

## Verification

| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » | rule-matched chunks | (no direct equivalent) |
|---|---|---|---|---|---|---|
| 12-ekadasamanayo | 10 | bad [] | 0 | [] | 21 | 1 |
| 13-dvadasamanayo | 33 | bad [] | 0 | [] | 39 | 1 |
| 14-terasamanayo | 10 | bad [] | 0 | [] | 19 | 0 |
| 15-cuddasamanayo | 68 | bad [] | 0 | [] | 81 | 1 |

## Reuse of pi-1 / pi-2

- Keyword uses: 2122; distinct keywords: 382.
- Keywords that pi-1 or pi-2 also has: 125 distinct; their values taken **unchanged from pi-1 / pi-2**: 121 distinct keyword-value pairs, 652 uses (a pi-2 value: 109 pairs, 631 uses; a pi-1 value only: 12 pairs, 21 uses).
- Keywords new in pi-3 (in neither mapping): 257 distinct.
- Instrumental keywords resolved through their nominative (Q1): the value is the pi-1 / pi-2 value of the nominative for 169 distinct keyword-value pairs, 393 uses; the nominative is in neither mapping for 11 pairs, 59 uses (sample / T_CH12_15 values and the Q2 / M4 pairs); it differs from the nominative's pi-1 / pi-2 value for 2 pairs (below).

### Values that differ from pi-1 / pi-2 for the same keyword

| keyword | pi-3 value (uses) | pi-2 value(s) | pi-1 value(s) | reason |
|---|---|---|---|---|
| antare | ကြားညှပ် (1) | အကြား (1) | - | Paṭhamantare «ပထမ ကြားညှပ်»: the Mātikā section word «ကြားညှပ်» (pi-1 headings, Q5); pi-2 «အကြား» is «between» in another sense |
| aññāta | သိရသော (3) | - | သိသော (3) | pi-1 «သိသော» is not in the segment: the text renders anaññāta «မသိရသေးသည်ကို», positive part «သိရ» + «သော» (rule 8, M7) |
| bodhi | ဗောဇ္ဈင် (3) | ဗောဓိ (2) | - | pi-2 «ဗောဓိ» is not in the segment: the text renders bojjhaṅgā by the one word «ဗောဇ္ဈင်» (aṅgā = no direct equivalent) |
| dukkha | နာကျင် (1) | ဒုက္ခ (136) · ဆင်းရဲ (7) · ခက်ခဲသော (7) · နာကျင်သော (3) | ခက်ခဲသော (77) · နာကျင်သော (6) · နာကျင်မှု (5) · ဒုက္ခ (4) | fragment of adukkhamasukhāya: the positive part of the text's «မနာကျင်» (rule 8); one sense per segment |
| maccu | သေခြင်း (1) | သေမင်း (2) | - | maccurūpaṃ in the jāti-jarā-maraṇa verse list: the text's «သေခြင်း» (death); pi-2 «သေမင်း» is Death personified (Q5) |
| nayo | ခွဲနည်း (5) | - | နည်း (4) | the pi-3 text's one word «ခွဲနည်း» (M8); pi-1 «နည်း» stands alone in its text |
| vidhā | မျိုး (1) | နှိုင်းယှဉ် ချိန်ဆမှု (3) | - | tiṃsavidhā «သုံးဆယ်မျိုး»: «kind» (Q5); pi-2 «နှိုင်းယှဉ် ချိန်ဆမှု» is the vidhā of conceit |
| āyatanena | အာရုံခံ နယ်ပယ် (32) | (no direct equivalent) (9) | - | the counted noun «အာရုံခံ နယ်ပယ် N-ပါး» (ekenāyatanena); pi-2 (no direct equivalent) is a compound member inside one Burmese word |

### Instrumental keywords whose value differs from the pi-1 / pi-2 value of their nominative

| keyword | nominative | pi-3 value (uses) | pi-1 / pi-2 value(s) of the nominative | reason |
|---|---|---|---|---|
| dukkhena | dukkhaṃ | ကိုယ်ဆင်းရဲခြင်း (3) | နာကျင်မှု (24) · ဒုက္ခ (15) · နာကျင်သော (1) | the soko … upāyāso list: the sample's dukkhaṃ «ကိုယ်ဆင်းရဲခြင်း» (Q1); pi-2 «နာကျင်မှု / ဒုက္ခ» are not in the segment |
| hetukehi dhammehi | hetukā dhammā | အမြစ် … သဘောတရား (2) | အမြစ် ရှိသော သဘောတရား (3) | negated «na … pahātabbahetukehi» («…အမြစ် ရှိသည် မဟုတ်သော သဘောတရား»): the sample's M4 gap; the positive items keep pi-1 |

## Rules

**Binding and unchanged:** everything the approved sample (`map-table.md`) lists: pi-1 rules 1–11, the agreed later
pi-1 rules (absolutives keep «…၍»; one sense per segment; no « / » alternatives …), pi-2's N1–N11 and harmonise
decisions, and the sample's M1–M9 (count biterms «āyatanehi N» = «အာရုံခံ နယ်ပယ် … N-ပါး» and «N dhātūhi» =
«ဓာတ် N-ပါး»; «A / B» = «A … B»; khandhato = «အစုအဝေး ရေတွက်ရာ»; «X dhammā» with a gap (M4: the negated
«na … pahātabbahetukehi» = «အမြစ် … သဘောတရား», avitakka / savitakka dhammā …); the presence endings «သနည်း», «ရာ»,
«သေးသည်»; nayo = «ခွဲနည်း» …). The sample's tables and context functions (rūpa, dukkha, sukha by the first compound
of the segment) are copied unchanged and shared, so every keyword the sample has keeps the sample's value
(saṅgahitā / asaṅgahitā, ṭhapetvā, asaṅkhataṃ, the counts, the topic members, aññāta, ñassāmi, bodhi / aṅgā,
upaṭṭhāna, dukkhaṃ = «ကိုယ်ဆင်းရဲခြင်း» …). pi-2 and pi-1 values are reused for the same keyword where they occur
in the segment, as in the sample.

## NEW rules (for the user's review)

Q1. **Instrumental items take the value of their nominative.** Methods 11-14 name every topic in the instrumental
    («Samudayasaccena / hetūhi dhammehi / dhātuyā ye dhammā …»); the text renders each item by the topic's
    nominative Burmese + «နှင့်» (the generator's item_nom), so the keyword takes the pi-1 / pi-2 / sample value of
    the nominative, without the case particle (pi-1 rule 1): saccena = သစ္စာ, indriyena = စွမ်းရည်, bhavena = ဘဝ,
    jātiyā = မွေးဖွားခြင်း, hetūhi = အမြစ်, hetukehi = အမြစ် (rule 2), sampayuttehi = ယှဉ်တွဲသော, Rūpīhi dhammehi =
    ရုပ် ဖြစ်သော သဘောတရား, bhāvanāya pahātabbehi = ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် … Candidates per word (-ena
    -> -o / -aṃ / -ā; -ehi -> -ā / -āni / -o / -aṃ; -āya -> -ā; -iyā -> -i; -uyā -> -u; -īhi -> -ino / -ī;
    -bhūhi -> -bhuno; -ūhi -> -ū; hetūhi -> hetū; upādādhammehi -> upādā dhammā); a candidate in a table first,
    then the one pi-1 / pi-2 use most (the real lemma); its value must be present in the segment. An instrumental
    keyword that pi-1 / pi-2 already map as such keeps that value (dassanena = သစ္စာကို မြင်ခြင်း, pi-1 / pi-2).
    rūpīhi = «ရုပ် ဖြစ်သော» (the sample's Rūpino, the same as Rūpīhi; not pi-2's «ရုပ် ရှိသော» for rūpī).
Q2. **«X-ena / X-ehi (ye dhammā) vippayuttā»** (the extractor's pair of an item and the verb of the relative
    clause) = «Xနှင့် ကင်းကွာသော» where the text has it contiguously, as pi-1 «vedanāya sampayuttā = ခံစားမှုနှင့်
    ယှဉ်တွဲသော» (the object keeps its «နှင့်», rule 3): bhavena vippayuttā = ဘဝနှင့် ကင်းကွာသော, Adhimokkhena
    vippayuttā = ဆုံးဖြတ်မှုနှင့် ကင်းကွာသော; an inner plural stays (pi-1 vitakkavicāravippayuttā «…တို့နှင့်
    ကင်းကွာသော»): dhammehi vippayuttā = သဘောတရားများနှင့် ကင်းကွာသော (the text of these chapters has «များ»; the
    parallel chapters 7-10-11 have «တို့» in their text). Where other items stand between, « … » (rule 10) after
    «Xနှင့်»: viññāṇena vippayuttā = သိစိတ်နှင့် … ကင်းကွာသော, bhavena vippayuttā (3-470, 3-471) = ဘဝနှင့် …
    ကင်းကွာသော; where the text has no «Xနှင့်» (Kusalehi: «ကုသိုလ် သဘောတရားများနှင့်…»): ကုသိုလ် … ကင်းကွာသော.
    The same forms as the parallel chapters 7-10-11 (their M3).
Q3. **The frame words**: kehici = «အချို့» (text «… တို့၏ အချို့နှင့်», «partly»; the genitive of the counts and
    «နှင့်» go, rule 1); dhammehi khandhasaṅgahena = «သဘောတရား … အစုအဝေး အကျုံးဝင်ခြင်း» (the item's head noun and
    the instrumental «အစုအဝေး အကျုံးဝင်ခြင်းဖြင့်» without «ဖြင့်», rule 1; the gap holds «များနှင့်»; the same value
    as the parallel chapters 7-10-11).
Q4. **Headings and colophons**: the ordinals ekādasama / -mo, dvādasama / -mo, terasama / -mo, cuddasama / -mo =
    the text's word «ဧကာဒသမ / ဒွါဒသမ / တေရသမ / စုဒ္ဒသမ» (heading's own word, pi-1 decision 4); the members of the
    «…padaniddeso» headings sampayutta / vippayutta / saṅgahita / asaṅgahita = «ယှဉ်တွဲသော / ကင်းကွာသော /
    အကျုံးဝင်သော / အကျုံးမဝင်သော» (text «…သည့်အရာ», N11; the head «အရာ» is not the keyword, as the sample's
    sampayuttaṃ in the Uddesa); sacca / phassa (Saccādi, Phassādisattakaṃ) = «သစ္စာ / တွေ့ထိမှု», ādi = «စသည်»
    (sample; text «စသည့်» matched by the verb ending rule).
Q5. **Summary verses** (the text's words; pi-1 rule 1): Uddhaṃ / upari = «အထက်» (text «အထက်တွင်», «ထို့အထက်တွင်»;
    the locative goes, as the parallel chapters 7-10-11 do); gocchaka / gocchake = «အစု»; vidhā
    (tiṃsavidhā «သုံးဆယ်မျိုး») = «မျိုး», tiṃsa = «သုံးဆယ်» (pi-2); the counts with «ပါး» (pannarasa, cuddasa,
    soḷasa, tecattālīsaṃ, sattacattālīsa); sattacattālīsa dhammā = «သဘောတရား လေးဆယ့်ခုနစ်ပါး» (counted noun keeps
    its count, rule 1); saṅgahaṃ gatā («are included», text «အကျုံးဝင်ကြသည်») = «အကျုံးဝင်သော» (rule 3, as
    saṅgahitā); su / buddho (subuddho «ကောင်းစွာ နားလည်အပ်သည်») = «ကောင်းစွာ» / «နားလည်အပ်သော» (rule 3);
    maccu (maccurūpaṃ) / mataṃ (jātijarāmataṃ) = «သေခြင်း»; pumaṃ (itthipumaṃ) = «ယောက်ျား»; Samucchede =
    «ပိုင်းဖြတ်ခြင်း»; mogha / pucchakena (moghapucchakena «မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်») = «အချည်းနှီး» /
    «မေးခွန်း»; labbhare (na labbhare «မတွေ့ရကြ») = «တွေ့ရသည်» (rules 4, 8: the positive verb, check by infixed
    «မ»); antara / antare (Mahantaraduke, Paṭhamantare) = «ကြားညှပ်» (pi-1 headings); duke = «နှစ်မျိုးတွဲ»;
    Navamassa = «နဝမ»; niddese = «အကျယ် ဖော်ပြချက်».
Q6. **adhimokkho** (in Adhimokkhena) = «ဆုံးဖြတ်မှု» (my3-zeroshot-terms, pi-2 ^2-281 text; pi-1 / pi-2 have only
    the compound adhimokkhapaccayā «ဆုံးဖြတ်မှုကြောင့်»).

## Presence: chunks matched by an ending rule (not literally in the segment)

Every other chunk of every value occurs literally in its segment's Burmese.

| segment | keyword | chunk | rule |
|---|---|---|---|
| 3-12-1-0 | sampayutta | ယှဉ်တွဲသော | attr |
| 3-12-1-0 | vippayutta | ကင်းကွာသော | attr |
| 3-409 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-409 | vippayuttā | ကင်းကွာသော | attr |
| 3-410 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-410 | vippayuttā | ကင်းကွာသော | attr |
| 3-410 | Natthi | မရှိသည် | verb |
| 3-411 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-411 | vippayuttā | ကင်းကွာသော | attr |
| 3-412 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-412 | vippayuttā | ကင်းကွာသော | attr |
| 3-413 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-413 | vippayuttā | ကင်းကွာသော | attr |
| 3-413 | ñassāmi | သိရတော့သည် | verb |
| 3-413 | aññāta | သိရသော | attr |
| 3-414 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-414 | vippayuttā | ကင်းကွာသော | attr |
| 3-414 | Natthi | မရှိသည် | verb |
| 3-415 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-415 | vippayuttā | ကင်းကွာသော | attr |
| 3-416 | vippayuttā | ကင်းကွာသော | attr |
| 3-13-1-0 | sampayutta | ယှဉ်တွဲသော | attr |
| 3-13-1-0 | asaṅgahita | အကျုံးမဝင်သော | attr |
| 3-417 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-417 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-418 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-419 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-420 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-421 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-422 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-423 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-423 | ñassāmi | သိရတော့သည် | verb |
| 3-423 | aññāta | သိရသော | attr |
| 3-424 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-425 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-426 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-427 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-428 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-429 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-430 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-431 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-432 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-433 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-434 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-435 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-436 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-437 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-437 | avitakka dhammehi | မရှိသော | attr |
| 3-438 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-439 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-440 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-441 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-442 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-443 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-444 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-445 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-446 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-447 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-447 | saṅgahaṃ gatā | အကျုံးဝင်သော | attr |
| 3-447 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-14-1-0 | sampayutta | ယှဉ်တွဲသော | attr |
| 3-14-1-0 | vippayutta | ကင်းကွာသော | attr |
| 3-14-1-0 | asaṅgahita | အကျုံးမဝင်သော | attr |
| 3-448 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-448 | vippayuttā | ကင်းကွာသော | attr |
| 3-449 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-449 | vippayuttā | ကင်းကွာသော | attr |
| 3-450 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-450 | vippayuttā | ကင်းကွာသော | attr |
| 3-451 | saṃkiliṭṭha | ညစ်နွမ်းသော | attr |
| 3-451 | vippayuttā | ကင်းကွာသော | attr |
| 3-451 | asaṃkiliṭṭha | မညစ်နွမ်းသော | attr |
| 3-452 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-452 | vippayuttā | ကင်းကွာသော | attr |
| 3-453 | Natthi | မရှိသည် | verb |
| 3-454 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-455 | pariyāpannehi | အကျုံးဝင်သော | attr |
| 3-455 | Natthi | မရှိသည် | verb |
| 3-455 | buddho | နားလည်အပ်သော | attr |
| 3-15-1-0 | vippayutta | ကင်းကွာသော | attr |
| 3-15-1-0 | asaṅgahita | အကျုံးမဝင်သော | attr |
| 3-15-1-3-0 | ādi | စသည် | verb |
| 3-456 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-456 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-457 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-457 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-458 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-459 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-460 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-461 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-462 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-463 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-464 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-465 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-465 | ñassāmi | သိရတော့သည် | verb |
| 3-465 | aññāta | သိရသော | attr |
| 3-466 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-467 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-468 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-469 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-470 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-471 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-472 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-473 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-474 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-475 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-476 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-477 | saṃkiliṭṭha | ညစ်နွမ်းသော | attr |
| 3-477 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-478 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-478 | asaṃkiliṭṭha | မညစ်နွမ်းသော | attr |
| 3-479 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-479 | upādinna | ဖြစ်သော | attr |
| 3-480 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-481 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-482 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-483 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-484 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-485 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-486 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-486 | gāmīhi dhammehi | ဦးတည်သော | attr |
| 3-487 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-488 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-489 | mahaggata | ကြီးမြတ်သော | attr |
| 3-489 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-490 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-491 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-492 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-493 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-494 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-495 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-496 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-497 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-498 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-499 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-500 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-501 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-502 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-503 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-504 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-505 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-506 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-507 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-508 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-509 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-510 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-511 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-512 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-513 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-514 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-515 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-516 | pariyāpannehi | အကျုံးဝင်သော | attr |
| 3-516 | kāmāvacarehi | ဆိုင်သော | attr |
| 3-516 | avacarehi | ဆိုင်သော | attr |
| 3-517 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-518 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-518 | niṭṭhitaṃ | ပြီးဆုံးသော | attr |
| 3-518 | labbhare | တွေ့ရသည် | verb |
| 3-518 | avacarehi | ဆိုင်သော | attr |
| 3-518 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |

## Keyword → Burmese (uses)

«pi-2» / «pi-1» = the value is a pi-2 / pi-1 value of the same keyword. Several values = the keyword reads differently by context.

| Pāli keyword | Burmese (uses) |
|---|---|
| Abyākatehi | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (1) |
| Adhimokkhena vippayuttā | ဆုံးဖြတ်မှုနှင့် ကင်းကွာသော (1) |
| adhipatīhi | အကြီးအမှူး (2) |
| akusalehi | အကုသိုလ် (2, pi-2) |
| akusalehi dhammehi | အကုသိုလ် သဘောတရား (2, pi-2) |
| anidassana | မမြင်နိုင်သော (1, pi-2) |
| antara | ကြားညှပ် (1, pi-1) |
| antare | ကြားညှပ် (1) |
| anuparivatti | နောက်သို့ လိုက်ပါသော (1, pi-1) |
| anuparivattīhi | နောက်သို့ လိုက်ပါသော (3) |
| anuparivattīhi dhammehi | နောက်သို့ လိုက်ပါသော သဘောတရား (1) |
| anuttarehi | ထိုထက် သာလွန်သည် မရှိသော (2) |
| anuttarehi dhammehi | ထိုထက် သာလွန်သည် မရှိသော သဘောတရား (2) |
| Anāsavehi | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (1) |
| anāsavehi | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (1) |
| Anāsavehi dhammehi | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော သဘောတရား (1) |
| anāsavehi dhammehi | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော သဘောတရား (1) |
| apacaya | လျော့ပါးခြင်း (3, pi-2) |
| Appamaññāya | အပ္ပမညာ (1) |
| appamaññāya | အပ္ပမညာ (2) |
| appamāṇa | အတိုင်းအဆ မရှိသော (1, pi-1) |
| Appamāṇehi | အတိုင်းအဆ မရှိသော (1) |
| appamāṇehi | အတိုင်းအဆ မရှိသော (1) |
| Appamāṇehi dhammehi | အတိုင်းအဆ မရှိသော သဘောတရား (1) |
| appamāṇehi dhammehi | အတိုင်းအဆ မရှိသော သဘောတရား (1) |
| ariyena | အရိယာ (3) |
| arūpa | ရုပ်မရှိသော (5, pi-2) |
| Arūpīhi | ရုပ် မဟုတ်သော (1) |
| Arūpīhi dhammehi | ရုပ် မဟုတ်သော သဘောတရား (1) |
| asaṃkiliṭṭha | ကိလေသာဖြင့် မညစ်နွမ်းသော (3, pi-2) |
| asaṃkiliṭṭhehi | ကိလေသာဖြင့် မညစ်နွမ်းသော (2) |
| asaṃyojaniyehi dhammehi | နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော သဘောတရား (1) |
| asaṅgahita | အကျုံးမဝင်သော (4) |
| asaṅgahitā | အကျုံးမဝင်သော (94) |
| asaṅkhataṃ | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (32, pi-2) |
| asaṅkhataṃ ṭhapetvā | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော … ချန်ထား၍ (32) |
| asaṅkhatehi | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (1) |
| asaṅkhatehi dhammehi | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရား (1) |
| asekkhehi | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ (3) |
| avacarehi | ဘုံနှင့် ဆိုင်သော (5) |
| avijjāya | အမှန်ကို မသိမှု (3, pi-1) |
| avitakka dhammehi | စတင်ကြံစည်မှု မရှိသော … သဘောတရား (4) |
| aññā / aññātāvī | အပြည့်အဝ သိမြင်ခြင်း … အပြည့်အဝ သိမြင်ပြီးသူ (3) |
| aññāta | သိရသော (3) |
| aṅgehi | (no direct equivalent) (3) |
| aṭṭhaṅgikena | အင်္ဂါ ရှစ်ပါး ရှိသော (3) |
| aṭṭhārasahi | ဆယ့်ရှစ်ပါး (18) |
| aṭṭhārasahi dhātūhi | ဓာတ် ဆယ့်ရှစ်ပါး (18) |
| bahiddhā | မိမိ၏ ပြင်ပ၌ (4, pi-2) |
| balehi | စွမ်းအား (3) |
| bhavena | ဘဝ (9) |
| bhavena vippayuttā | ဘဝနှင့် ကင်းကွာသော (2) · ဘဝနှင့် … ကင်းကွာသော (2) |
| bhāvanāya pahātabbehi | ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် (5) |
| bodhi | ဗောဇ္ဈင် (3) |
| buddho | နားလည်အပ်သော (1) |
| bāhiraṃ | ပြင်ပ (1, pi-2) |
| bāhirehi | ပြင်ပ (1) |
| bāhirehi dhammehi | ပြင်ပ သဘောတရား (1) |
| cakkhu | မျက်စိ (2, pi-2) |
| cakkhudhātuyā | မျက်စိ ဓာတ် (1) |
| cakkhundriyena | မျက်စိ၏ စွမ်းရည် (1) |
| cakkhuviññāṇa | မျက်စိ သိစိတ် (2, pi-2) |
| Cakkhuviññāṇadhātuyā | မျက်စိ သိစိတ် ဓာတ် (1) |
| cakkhuviññāṇadhātuyā | မျက်စိ သိစိတ် ဓာတ် (1) |
| Cakkhāyatanena | မျက်စိ အာရုံခံ နယ်ပယ် (1) |
| cetanāya | စေ့ဆော်မှု (3, pi-2) |
| Cetasikehi | စိတ်၏ အဖော် (1) |
| cetasikehi | စိတ်၏ အဖော် (1) |
| citta | စိတ် (2, pi-2) |
| cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi | စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော (2) |
| cittaṃ | စိတ် (1, pi-2) |
| Cittehi | စိတ် (1) |
| cittehi | စိတ် (2) |
| Cittena | စိတ် (1, pi-2) |
| cittena | စိတ် (1, pi-2) |
| cittānuparivattīhi | စိတ်နောက်သို့ လိုက်ပါသော (1) |
| cittānuparivattīhi dhammehi | စိတ်နောက်သို့ လိုက်ပါသော သဘောတရား (1) |
| Cuddasa | ဆယ့်လေးပါး (1) |
| cuddasa | ဆယ့်လေးပါး (1) |
| cuddasama | စုဒ္ဒသမ (1) |
| cuddasamo | စုဒ္ဒသမ (1) |
| dasa | ဆယ်ပါး (60, pi-2) |
| dasahi dhātūhi | ဓာတ် ဆယ်ပါး (27) |
| dasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ်ပါး (60) |
| Dassanena | သစ္စာကို မြင်ခြင်း (2, pi-2) |
| dassanena | သစ္စာကို မြင်ခြင်း (4, pi-2) |
| dhamma | သဘောတရား (3, pi-2) |
| dhammehi khandhasaṅgahena | သဘောတရား … အစုအဝေး အကျုံးဝင်ခြင်း (2) |
| dhammehi vippayuttā | သဘောတရားများနှင့် ကင်းကွာသော (38) |
| dhammā saṅgahitā | သဘောတရား … အကျုံးဝင်သော (5) |
| dhātu | ဓာတ် (17, pi-2) |
| dhātukathā | ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း (1) |
| dhātuyā | ဓာတ် (32, pi-2) |
| dhātūhi | ဓာတ် (94) |
| domanassa | စိတ်ဆင်းရဲမှု (3, pi-2) |
| domanassena | စိတ်ဆင်းရဲမှု (3) |
| duke | နှစ်မျိုးတွဲ (1) |
| dukkha | နာကျင်မှု (3, pi-2) · ဒုက္ခ (1, pi-2) · နာကျင် (1) |
| Dukkhasaccena | ဒုက္ခ သစ္စာ (1) |
| dukkhena | ကိုယ်ဆင်းရဲခြင်း (3) |
| dukkhāya | နာကျင်သော (3, pi-2) |
| dvādasa | ဆယ့်နှစ်ပါး (29, pi-2) |
| dvādasahi dhātūhi | ဓာတ် ဆယ့်နှစ်ပါး (2) |
| dvādasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး (28) |
| dvādasama | ဒွါဒသမ (1) |
| dvādasamo | ဒွါဒသမ (1) |
| ekādasa | ဆယ့်တစ်ပါး (17, pi-2) |
| ekādasahi | ဆယ့်တစ်ပါး (1) |
| ekādasahi dhātūhi | ဓာတ် ဆယ့်တစ်ပါး (6) |
| ekādasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး (16) |
| ekādasama | ဧကာဒသမ (1) |
| ekādasamo | ဧကာဒသမ (1) |
| ganthaniyehi | အထုံး၏ အာရုံ ဖြစ်နိုင်သော (1) |
| ganthehi | အထုံး (3) |
| ghānaviññāṇa | နှာခေါင်း သိစိတ် (1, pi-2) |
| ghānaviññāṇadhātuyā | နှာခေါင်း သိစိတ် ဓာတ် (1) |
| gocchaka | အစု (1) |
| gocchake | အစု (2) |
| gāmīhi dhammehi | ဦးတည်သော သဘောတရား (3) |
| hetukehi | အမြစ် (9) |
| hetukehi dhammehi | အမြစ် ရှိသော သဘောတရား (4) · အမြစ် … သဘောတရား (2) |
| Hetūhi | အမြစ် (2) |
| hetūhi | အမြစ် (1) |
| hīnehi | ယုတ်ညံ့သော (2) |
| hīnehi dhammehi | ယုတ်ညံ့သော သဘောတရား (2) |
| iddhi | ဣဒ္ဓိ (3, pi-2) |
| indriyehi | စွမ်းရည် (3) |
| indriyena | စွမ်းရည် (14) |
| indriyā | စွမ်းရည် (1, pi-2) |
| itthi | မိန်းမ (4, pi-2) |
| jarā | အိုခြင်း (2, pi-2) |
| jarāya | အိုခြင်း (1) |
| Jhānena | ဈာန် (1) |
| jhānena | ဈာန် (1) |
| jivhāviññāṇa | လျှာ သိစိတ် (1, pi-2) |
| jivhāviññāṇadhātuyā | လျှာ သိစိတ် ဓာတ် (1) |
| jāti | မွေးဖွားခြင်း (2, pi-2) |
| jātiyā | မွေးဖွားခြင်း (1, pi-2) |
| jīvita | အသက် (1, pi-1) |
| jīvitaṃ | အသက် (2, pi-2) |
| kathā | ဆွေးနွေးခြင်း (1) |
| kehici | အချို့ (16) |
| khandha | အစုအဝေး (17, pi-2) |
| khandhato | အစုအဝေး ရေတွက်ရာ (32) |
| khandhehi | အစုအဝေး (94) |
| khandhena | အစုအဝေး (62) |
| kilesa | ကိလေသာ (3, pi-2) |
| kilesehi | ကိလေသာ (4) |
| Kusalehi | ကုသိုလ် (2) |
| Kusalehi dhammehi | ကုသိုလ် သဘောတရား (2) |
| Kusalehi vippayuttā | ကုသိုလ် … ကင်းကွာသော (1) |
| kāma | ကာမ (1, pi-2) |
| kāma / āyatana | ကာမ … အာရုံခံ နယ်ပယ် (1) |
| kāma / āyatanehi | ကာမ … အာရုံခံ နယ်ပယ် (3) |
| Kāmāvacarehi | ကာမဘုံနှင့် ဆိုင်သော (1) |
| kāmāvacarehi | ကာမဘုံနှင့် ဆိုင်သော (2) |
| kāya | ကိုယ် (1, pi-2) |
| kāyaviññāṇa | ကိုယ် သိစိတ် (1, pi-2) |
| kāyaviññāṇadhātuyā | ကိုယ် သိစိတ် ဓာတ် (1) |
| labbhare | တွေ့ရသည် (1) |
| Lokiyehi | လောကနှင့် သက်ဆိုင်သော (1) |
| Lokiyehi dhammehi | လောကနှင့် သက်ဆိုင်သော သဘောတရား (1) |
| lokuttarehi | လောကကို ကျော်လွန်သော (2) |
| maccu | သေခြင်း (1) |
| magga | မဂ် (5, pi-2) |
| maggena | မဂ် (3) |
| mahaggata | ကြီးမြတ်သော (1, pi-1) |
| mahaggatehi | ကြီးမြတ်သော (2) |
| mahaggatehi dhammehi | ကြီးမြတ်သော သဘောတရား (2) |
| Majjhimehi | အလယ်အလတ် (1) |
| Majjhimehi dhammehi | အလယ်အလတ် သဘောတရား (1) |
| mana | မနော (4, pi-1) |
| manasikārena | နှလုံးသွင်းခြင်း (3) |
| mano | မနော (1, pi-2) |
| manodhātuyā | မနော ဓာတ် (2, pi-2) |
| manoviññāṇa | မနော သိစိတ် (2, pi-2) |
| manoviññāṇadhātuyā | မနော သိစိတ် ဓာတ် (2) |
| manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (1, pi-2) |
| manāyatanena | မနော အာရုံခံ နယ်ပယ် (2) |
| maraṇena | သေခြင်း (1) |
| mataṃ | သေခြင်း (1) |
| micchatta | မှားယွင်းမှု (2, pi-2) |
| mogha | အချည်းနှီး (1) |
| Natthi | မရှိသည် (6, pi-2) |
| Navamassa | နဝမ (1) |
| nayo | ခွဲနည်း (5) |
| niddese | အကျယ် ဖော်ပြချက် (1) |
| niddeso | အကျယ် ဖော်ပြချက် (7, pi-2) |
| nirodha | ချုပ်ငြိမ်းခြင်း (1, pi-2) |
| niyatehi | ကျိန်းသေသော (6) |
| niyatehi dhammehi | ကျိန်းသေသော သဘောတရား (4) |
| niyyānikehi dhammehi | လွတ်မြောက်ရာသို့ ပို့ဆောင်သော သဘောတရား (2) |
| niṭṭhitaṃ | ပြီးဆုံးသော (1, pi-1) |
| nāmarūpaṃ | စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (2, pi-2) |
| nāmarūpena | စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (1) |
| nāsaññā | မှတ်သိမှု မရှိသည် မဟုတ်သော (2, pi-1) |
| nīvaraṇehi | အတားအဆီး (3, pi-2) |
| nīvaraṇiyehi | အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော (1) |
| oghaniyehi | ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော (1) |
| oghehi | ရေအလျဉ် (3) |
| paccayā | ကြောင့် (10, pi-2) |
| padhānena | ကြိုးပမ်းအားထုတ်ခြင်း (3) |
| pahātabbehi | ပယ်ရမည့် (6) |
| pannarasa | ဆယ့်ငါးပါး (1, pi-2) |
| pannarasahi | ဆယ့်ငါးပါး (6) |
| pannarasahi dhātūhi | ဓာတ် ဆယ့်ငါးပါး (6) |
| Paridevena | ငိုကြွေးခြင်း (1) |
| paridevena | ငိုကြွေးခြင်း (1) |
| paritta | အကန့်အသတ် ရှိသော (2, pi-2) |
| parittehi | အကန့်အသတ် ရှိသော (1) |
| parittehi dhammehi | အကန့်အသတ် ရှိသော သဘောတရား (1) |
| pariyāpannehi | ဘဝဘုံတို့၌ အကျုံးဝင်သော (3) |
| Parāmaṭṭhehi | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (1) |
| parāmaṭṭhehi | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (4) |
| Parāmaṭṭhehi dhammehi | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား (1) |
| parāmāsa | မှားယွင်းသော ယူဆမှု (5, pi-2) |
| parāmāsehi | မှားယွင်းသော ယူဆမှု (4) |
| paññā | ပညာ (3, pi-2) |
| paṇītehi | မွန်မြတ်သော (2) |
| paṇītehi dhammehi | မွန်မြတ်သော သဘောတရား (2) |
| paṭicca | အကြောင်းတို့ကို မှီ၍ (1, pi-2) |
| phassa | တွေ့ထိမှု (2, pi-2) |
| Phassena | တွေ့ထိမှု (2) |
| phassena | တွေ့ထိမှု (4) |
| phoṭṭhabba | အထိအတွေ့ (1, pi-2) |
| phoṭṭhabbadhātuyā | အထိအတွေ့ ဓာတ် (1) |
| phoṭṭhabbāyatanena | အထိအတွေ့ အာရုံခံ နယ်ပယ် (1) |
| pucchakena | မေးခွန်း (1) |
| pumaṃ | ယောက်ျား (1) |
| purisa | ယောက်ျား (3, pi-2) |
| pīti | ပီတိ (3, pi-2) |
| pītikehi | ပီတိ (3) |
| raṇehi | ပဋိပက္ခ (3) |
| rūpa | သိမ်မွေ့သော ရုပ် (4, pi-2) · ရုပ် (3, pi-2) |
| Rūpakkhandhena | ရုပ် အစုအဝေး (2) |
| Rūpaṃ | ရုပ် (1, pi-2) |
| Rūpīhi | ရုပ် ဖြစ်သော (1) |
| rūpīhi | ရုပ် ဖြစ်သော (1) |
| Rūpīhi dhammehi | ရုပ် ဖြစ်သော သဘောတရား (1) |
| rūpīhi dhammehi | ရုပ် ဖြစ်သော သဘောတရား (1) |
| sacca | သစ္စာ (1, pi-2) |
| saccena | သစ္စာ (5) |
| saccā | သစ္စာ (2, pi-2) |
| saddhā | ယုံကြည်မှု (3, pi-2) |
| sahabhu | အတူ တည်ရှိသော (1, pi-2) |
| sahabhūhi | အတူ တည်ရှိသော (3) |
| sahabhūhi dhammehi | အတူ တည်ရှိသော သဘောတရား (1) |
| sahagatehi | အတူ ဖြစ်သော (8) |
| sahagatehi dhammehi | အတူ ဖြစ်သော သဘောတရား (8) |
| sammatta | မှန်ကန်မှု (2, pi-2) |
| sammā | မှန်ကန်သော (3, pi-2) |
| sampayutta | ယှဉ်တွဲသော (3, pi-1) |
| sampayuttehi | ယှဉ်တွဲသော (11) |
| sampayuttā | ယှဉ်တွဲသော (43, pi-2) |
| Samucchede | ပိုင်းဖြတ်ခြင်း (1) |
| samudaya | ဖြစ်ပေါ်ခြင်း (3, pi-2) |
| samuṭṭhāna | ဖြစ်ပေါ်လာသော (1, pi-1) |
| samuṭṭhānehi | ဖြစ်ပေါ်လာသော (3) |
| samuṭṭhānehi dhammehi | ဖြစ်ပေါ်လာသော သဘောတရား (1) |
| samādhi | သမာဓိ (3, pi-2) |
| sanidassana | မြင်နိုင်သော (1, pi-2) |
| sanidassanehi | မြင်နိုင်သော (1) |
| sanidassanehi dhammehi | မြင်နိုင်သော သဘောတရား (1) |
| Sappītikehi dhammehi | ပီတိ ရှိသော သဘောတရား (1) |
| sappītikehi dhammehi | ပီတိ ရှိသော သဘောတရား (2) |
| saraṇehi dhammehi | ပဋိပက္ခ ရှိသော သဘောတရား (2) |
| sati | သတိ (6, pi-2) |
| sattacattālīsa | လေးဆယ့်ခုနစ်ပါး (1) |
| sattacattālīsa dhammā | သဘောတရား လေးဆယ့်ခုနစ်ပါး (1) |
| sattarasahi | ဆယ့်ခုနစ်ပါး (15) |
| sattarasahi dhātūhi | ဓာတ် ဆယ့်ခုနစ်ပါး (15) |
| sauttarehi | ထိုထက် သာလွန်သည် ရှိသေးသော (1) |
| savicārehi dhammehi | ဆက်လက်သုံးသပ်မှု ရှိသော သဘောတရား (3) |
| savitakka dhammehi | စတင်ကြံစည်မှု ရှိသော … သဘောတရား (3) |
| Savitakkehi dhammehi | စတင်ကြံစည်မှု ရှိသော သဘောတရား (1) |
| savitakkehi dhammehi | စတင်ကြံစည်မှု ရှိသော သဘောတရား (2) |
| saññā | မှတ်သိမှု (7, pi-2) |
| saññākkhandhena | မှတ်သိမှု အစုအဝေး (2) |
| saññāya | မှတ်သိမှု (2, pi-1) |
| Saṃkilesikehi | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (1) |
| saṃkilesikehi | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (9) |
| Saṃkilesikehi dhammehi | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား (1) |
| saṃkiliṭṭha | ကိလေသာဖြင့် ညစ်နွမ်းသော (2, pi-2) |
| Saṃkiliṭṭhehi | ကိလေသာဖြင့် ညစ်နွမ်းသော (1) |
| saṃkiliṭṭhehi | ကိလေသာဖြင့် ညစ်နွမ်းသော (4) |
| saṃkiliṭṭhehi dhammehi | ကိလေသာဖြင့် ညစ်နွမ်းသော သဘောတရား (1) |
| saṃsaṭṭhaṃ | ရောနှောသော (1, pi-2) |
| saṃsaṭṭhehi | ရောနှောသော (4) |
| saṃsaṭṭhehi dhammehi | ရောနှောသော သဘောတရား (3) |
| Saṃyojanehi | နှောင်ကြိုး (2) |
| saṃyojanehi | နှောင်ကြိုး (1) |
| saṃyojaniyehi | နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော (1) |
| saṅgahaṃ gatā | အကျုံးဝင်သော (1) |
| saṅkhāra | ပြုပြင်ဖန်တီးမှု (4, pi-2) |
| saṅkhārakkhandhena | ပြုပြင်ဖန်တီးမှု အစုအဝေး (2) |
| saṅkhārehi | ပြုပြင်ဖန်တီးမှု (3) |
| sekkha | ကျင့်ကြံဆဲသူ၏ (1, pi-2) |
| sekkhehi | ကျင့်ကြံဆဲသူ၏ (2) |
| Sokena | စိုးရိမ်ခြင်း (2) |
| sokena | စိုးရိမ်ခြင်း (1) |
| somanassa | ဝမ်းမြောက်မှု (3, pi-2) |
| sotaviññāṇa | နား သိစိတ် (1, pi-2) |
| sotaviññāṇadhātuyā | နား သိစိတ် ဓာတ် (1) |
| soḷasa | ဆယ့်ခြောက်ပါး (1, pi-2) |
| soḷasahi | ဆယ့်ခြောက်ပါး (25) |
| soḷasahi dhātūhi | ဓာတ် ဆယ့်ခြောက်ပါး (25) |
| su | ကောင်းစွာ (1) |
| sukha | သာယာမှု (7, pi-2) · သာယာသော (2, pi-2) |
| Sukhāya | သာယာသော (1, pi-2) |
| sukhāya | သာယာသော (3, pi-2) |
| Sāsavehi dhammehi | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား (1) |
| taṇhāya | တပ်မက်မှု (3, pi-2) |
| tecattālīsaṃ | လေးဆယ့်သုံးပါး (1) |
| terasahi | ဆယ့်သုံးပါး (5) |
| terasahi dhātūhi | ဓာတ် ဆယ့်သုံးပါး (5) |
| terasama | တေရသမ (1) |
| terasamo | တေရသမ (1) |
| tiṃsa | သုံးဆယ် (1, pi-2) |
| Uddhaṃ | အထက် (1) |
| upapatti | ပြန်လည် ဖြစ်ပေါ်ခြင်း (1, pi-2) |
| upari | အထက် (1) |
| upaṭṭhānena | ပဋ္ဌာန် (3) |
| upekkhā | ဥပေက္ခာ (9, pi-2) |
| Uppannehi | ဖြစ်ပေါ်ပြီးသော (1) |
| Uppannehi dhammehi | ဖြစ်ပေါ်ပြီးသော သဘောတရား (1) |
| uppādīhi | ဖြစ်ပေါ်လာမည့် (1) |
| upādinna | ကံကြောင့် ဖြစ်သော (3, pi-2) |
| Upādinnehi | ကံကြောင့် ဖြစ်သော (1) |
| upādinnehi | ကံကြောင့် ဖြစ်သော (1) |
| upādā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော (3, pi-2) |
| upādādhammehi | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား (2) |
| Upādānehi | စွဲလမ်းမှု (2) |
| upādānehi | စွဲလမ်းမှု (1) |
| upādānena | စွဲလမ်းမှု (3) |
| upādāniyehi | စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော (4) |
| Upāyāsena | ပြင်းစွာ ပူပန်ခြင်း (2) |
| upāyāsena | ပြင်းစွာ ပူပန်ခြင်း (1) |
| vedanā | ခံစားမှု (5, pi-2) |
| Vedanākkhandhena | ခံစားမှု အစုအဝေး (2) |
| Vedanāya | ခံစားမှု (1, pi-2) |
| vedanāya | ခံစားမှု (7, pi-2) |
| vicāra | ဆက်လက်သုံးသပ်မှု (1, pi-2) |
| vicārehi | ဆက်လက်သုံးသပ်မှု (7) |
| vidhā | မျိုး (1) |
| vippayutta | ကင်းကွာသော (3, pi-2) |
| vippayuttehi | ကင်းကွာသော (3) |
| vippayuttehi dhammehi | ကင်းကွာသော သဘောတရား (11) |
| vippayuttā | ကင်းကွာသော (76, pi-2) |
| visaṃsaṭṭhehi dhammehi | မရောနှောသော သဘောတရား (1) |
| vitakka | စတင်ကြံစည်မှု (5, pi-2) |
| vitakka / vicāra | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (1) |
| vitakka / vicārehi | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (4) |
| vitakkehi | စတင်ကြံစည်မှု (3) |
| vitakkehi / vicārehi | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (3) |
| viññāṇa | သိစိတ် (4, pi-2) |
| Viññāṇakkhandhena | သိစိတ် အစုအဝေး (1) |
| viññāṇakkhandhena | သိစိတ် အစုအဝေး (1) |
| viññāṇena | သိစိတ် (2) |
| viññāṇena vippayuttā | သိစိတ်နှင့် … ကင်းကွာသော (1) |
| vokāra | အစုအဝေး (5) |
| yoganiyehi | ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော (1) |
| yogehi | ထမ်းပိုး (3) |
| ñassāmi | သိရတော့သည် (3) |
| ācaya | စုပုံခြင်း (3, pi-2) |
| ādi | စသည် (3, pi-2) |
| ārammaṇaṃ | အာရုံ (1, pi-2) |
| ārammaṇehi | အာရုံ (9) |
| āsava | စိတ်အစွန်းအထင်း (1, pi-2) |
| Āsavehi | စိတ်အစွန်းအထင်း (2) |
| āsavehi | စိတ်အစွန်းအထင်း (4) |
| āyatana | အာရုံခံ နယ်ပယ် (18, pi-2) |
| āyatanehi | အာရုံခံ နယ်ပယ် (92) |
| āyatanehi aṭṭhārasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ရှစ်ပါး (18) |
| āyatanehi dasahi | အာရုံခံ နယ်ပယ် … ဆယ်ပါး (27) |
| āyatanehi dvādasahi | အာရုံခံ နယ်ပယ် … ဆယ့်နှစ်ပါး (2) |
| āyatanehi ekādasahi | အာရုံခံ နယ်ပယ် … ဆယ့်တစ်ပါး (6) |
| āyatanehi pannarasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ငါးပါး (6) |
| āyatanehi sattarasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ခုနစ်ပါး (15) |
| āyatanehi soḷasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ခြောက်ပါး (25) |
| āyatanehi terasahi | အာရုံခံ နယ်ပယ် … ဆယ့်သုံးပါး (5) |
| āyatanena | အာရုံခံ နယ်ပယ် (32) |
| ṭhapetvā | ချန်ထား၍ (32, pi-2) |
