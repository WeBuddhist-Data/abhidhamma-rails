# pi-7 Burmese keyword mapping, phase 2, group g1 (1-01-kusalattika, 1-03-vipakattika, 1-04-upadinnattika, 1-05-sankilitthattika)

Script: `map_g1.py`, which imports `map7_rules.py`. The module is unchanged (md5 909bed2528b27eb55051c73f3ce28f81). The
script holds the g1 chapter tables (`NEW`, `OVERRIDE`), two per-segment overrides (`CTX`) and one context function
(`f_g1_natthi`). The Burmese comes only from the FINAL pi-7 text, its `notes-ch1-*.md` / `my7-zeroshot-terms.md`, and the
pi-1 … pi-6 values the module reads.

## Numbers

| chapter | lines | `bad` | presence failures | «, » / «၊» / « / » | (no direct equivalent) | chunks by an ending rule | stem (S1) |
|---|---|---|---|---|---|---|---|
| 1-01-kusalattika | 1508 | [] | 0 | 0 | 3 | 92 | 6 |
| 1-03-vipakattika | 267 | [] | 0 | 0 | 1 | 36 | 3 |
| 1-04-upadinnattika | 209 | [] | 0 | 0 | 3 | 34 | 3 |
| 1-05-sankilitthattika | 85 | [] | 0 | 0 | 2 | 19 | 1 |

- The (no direct equivalent) values are all karoti / katvā after an act compound (f_karoti, U2).
- Changes against the module-only dry run: 168 uses.
  - 71 uses (28 keyword forms) the module left unmapped.
  - 97 uses where a module value was overridden.
- Two runs give byte-identical files.

## Rules used

All the phase-1 rules, unchanged:
- pi-1 rules 1-11 and the agreed later rules;
- pi-2 N1-N11, pi-3 M1-M9, pi-4 P1-P8, pi-5 Q1-Q8 / S1, pi-6 R1-R9 and the phase-3 mechanics;
- T1-T13, M1, M2, and the decisions U1-U5.

These are the rules the g1 values lean on:
- T4: a hyphen-compound part takes the case of the compound.
- U1: two predicates that share one ending; the first predicate is bare.
- Rule 1: final case particles go, and «အခါ» goes as well (pi-5 niruddhe «ချုပ်ငြိမ်းသွားသော»).
- Rule 3: the gerundive «…ရမည့်».
- Rule 4: verbs drop the plural «ကြ» (by the ending rule).
- A5: the head noun the text adds is not part of the keyword.
- T12: a compound is its qualifier plus its head.

## New rules (extensions of existing rules, with reasons)

No rule outside T1-T13 / U1-U5 was needed. Four existing rules are applied to new cases:

1. **T4 for natthi** (`f_g1_natthi`).
   - In a heading, «Natthi-vigatapaccayā / -vigatadukāni / -vigatāvigatapaccayā» Natthi is the condition name «မရှိခြင်းဟူသော အကြောင်း».
   - In a note, «(Natthi-vigataṃ anantarasadisaṃ …)» «(မရှိခြင်း၊ ပျောက်ကွယ်ခြင်းသည် …)» it is the bare name «မရှိခြင်း».
   - The module's f_natthi gave the verb «မရှိသည်» here (7 uses).
2. **U1 for a predicate adjective**:
   - «gambhīrā sukhumatarā ca» is «နက်နဲ၍ ပို၍ သိမ်မွေ့သည်»;
   - gambhīrā takes the bare «နက်နဲ»;
   - sukhumatarā takes «ပို၍ သိမ်မွေ့သည်», since «ပို၍» renders -tara.
3. **Locative absolute** «nakamme gaṇite» «… ကို ရေတွက်သောအခါ» = «ရေတွက်သော» (the pi-5 niruddhe precedent, rule 1).
4. **Arūpa-sphere compounds** are the my7 sphere term plus the head (T12-like):
   - X-vipākassa: «… နယ်ပယ် ကံ၏ အကျိုး»;
   - X-kusalaṃ: «… နယ်ပယ် ကုသိုလ်»;
   - X-kiriyaṃ: «… နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော» (A5: the text's «စိတ်» goes, as for the module's kiriyaṃ).

## Keywords newly mapped (71 uses, 28 keyword forms)

| keyword | value | note |
|---|---|---|
| Sahetādhipati (heading) | အမြစ်ဟူသော အကြောင်း အကြီးအမှူးဟူသော အကြောင်း … ပါဝင်သော | T4 sa-X, as phase-1 Saindriya / Sādhipati; the «နှင့် စွမ်းရည်ဟူသော အကြောင်း» in the gap is indriya |
| vigatāvigatapaccayā (heading) | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းနှင့် မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | T4 (a heading names the conditions); the inner «နှင့်» stays |
| sajjhāyantena | သရဇ္ဈာယ်လျက် | the text's adverbial (as asammuyhantena) |
| asammohantena / Asammohantena | မရောထွေးစေဘဲ | = module asammuyhantena |
| gaṇite | ရေတွက်သော | extension 3 |
| ekasadisāni | တူညီသည် | rule 4, «ကြ» by the ending rule |
| sukhumatarā | ပို၍ သိမ်မွေ့သည် | extension 2 |
| bandhitabbaṃ | ဖွဲ့ရမည့် | rule 3 |
| bhāgo | အပိုင်း | my7 terms «(Paṭhamo bhāgo)» |
| viññāṇañcāyatanavipākassa | အဆုံး မရှိသော သိစိတ် နယ်ပယ် ကံ၏ အကျိုး | extension 4 |
| viññāṇañcāyatanakiriyassa | အဆုံး မရှိသော သိစိတ် နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော | extension 4 |
| nevasaññānāsaññāyatanakusalaṃ / -kusalassa | မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ကုသိုလ် | extension 4 (rule 6: no «၊») |
| nevasaññānāsaññāyatanakiriyaṃ | … နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော | extension 4 |
| vipākābyākatakiriyābyākatacittasamaṅgissa | ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော စိတ်နှင့် ပြည့်စုံသူ | T12 -cittasamaṅgissa (pi-6 R8), the «၊» between the qualifiers goes |
| kiriyasamāpattiṃ | ပြုရုံမျှသာ ဖြစ်သော သမာပတ် | notes-ch1-01 |
| Dibbasotadhātu | နတ်နား ဓာတ် | notes-ch1-01 |
| Utu / utu | ရာသီဥတု | notes-ch1-01, module SAMUTTHANA |
| atthappaṭisambhidāya | အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ် | notes-ch1-01; rule 1 |
| dhammappaṭisambhidāya | တရားကို ပိုင်းခြားသိသော ဉာဏ် | notes-ch1-01; rule 1 |
| niruttippaṭisambhidāya | စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ် | notes-ch1-01; rule 1 |
| paṭibhānappaṭisambhidāya | ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ် | notes-ch1-01; rule 1 |
| ṭhānāṭhānakosallassa | 1-01 ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း; 1-03 … 1-05 ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု | the segment's own form (A1 below) |
| niyatamicchādiṭṭhiyā | ကျိန်းသေသော မှားယွင်းသော အယူ | notes-ch1-01 |
| paṭighātatthāya | ချေဖျက်ရန် | the text's «ထိုအမှုကို ချေဖျက်ရန်» |
| suciṇṇāni (1-03 … 1-05) | ကောင်းစွာ ပြုခဲ့ဖူးသည် | the text's «ကောင်းစွာ ပြုခဲ့ဖူးသည်တို့ကို» (rule 1). In 1-01 it keeps the module's «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော» (A2) |

Several of these keywords recur in g2 … g6 (frame-coverage counts book-wide: atthappaṭisambhidāya 16, niyatamicchādiṭṭhiyā 16, suciṇṇāni 14, ṭhānāṭhānakosallassa 12, viññāṇañcāyatanavipākassa 7, …). These values are candidates for the module in phase 3.

## Module overrides (97 uses; for phase 3)

| keyword | module value | g1 value | uses | reason |
|---|---|---|---|---|
| Vipākañca | ကံ၏ အကျိုး (cond family) | ကံ၏ အကျိုး ဖြစ်သော | 31 | «Vipākañca nevavipāka…dhammañca dhammaṃ paṭicca» is the triad term («ကံ၏ အကျိုး ဖြစ်သော သဘောတရားနှင့် …»), not the condition name. The cond family catches «vipāka + ñca» before R1. |
| vipassanti | ထိုးထွင်း၍ ရှုကြသည် | ထိုးထွင်း၍ ရှုသည် | 17 | rule 4: the plural «ကြ» goes (as vipassati, abhinandanti, paccavekkhanti) |
| tadārammaṇatā | စိတ်သည် | 1-01 ထိုအာရုံကို အာရုံပြုသည့် အနေ; 1-03 … 1-05 ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ် | 14 | the module value is the head noun the text supplies to vipāko, with a case particle. The keyword is «… အနေဖြင့် / အဖြစ်ဖြင့်»; rule 1: «ဖြင့်» goes. |
| gaṇetabbā / gaṇetabbāti | ရေတွက်ရမည် | ရေတွက်ရမည့် | 8 | rule 3, as the module's gaṇetabbaṃ |
| Natthi | မရှိသည် (f_natthi) | မရှိခြင်းဟူသော အကြောင်း (headings) / မရှိခြင်း (note) | 7 | T4 (extension 1) |
| uppādenti | ဖြစ်ပေါ်စေသည် (pi-5) / ဖြစ်စေကြသည် | ဖြစ်စေသည် | 4 | The text's verb is «ဖြစ်စေကြသည်» (rule 4: «ကြ» goes; = uppādeti). In ^7-2-423 the pi-5 «ဖြစ်ပေါ်စေသည်» stands only for jappeti «မာနကို ဖြစ်ပေါ်စေသည်». |
| vitthāretabbāni | အကျယ် ချဲ့ရမည် | အကျယ် ချဲ့ရမည့် | 4 | rule 3, as the module's vitthāretabbaṃ |
| niyatamicchādiṭṭhi | ကျိန်းသေသော | ကျိန်းသေသော မှားယွင်းသော အယူ | 4 | the term family gave only the first member |
| kusale | ကုသိုလ် သဘောတရား (pi-2) | ကုသိုလ် | 2 | «kusale khandhe» «ကုသိုလ် အစုအဝေး», «kusale niruddhe» «ကုသိုလ် ချုပ်ငြိမ်းသောအခါ»; the segment's «သဘောတရား» belongs to dhammo / dhammaṃ |
| ṭhitena | တည်သော | တည်၍ | 2 | «nahetuyā ṭhitena» «… မဟုတ်ခြင်း၌ တည်၍»: the text's adverbial, as for -antena |
| gambhīrā | နက် | နက်နဲ | 1 | the module value is only part of the word (extension 2) |
| Cakkaṃ | စက် | စက်ဝိုင်း | 1 | «(Cakkaṃ bandhitabbaṃ.)» «(စက်ဝိုင်း ဖွဲ့ရမည်။)» |
| sekkhā (CTX ^7-2-423) | ကျင့်ကြံဆဲသူ၏ (pi-2) | ကျင့်ကြံဆဲသူ | 1 | rule 1: «၏» goes |
| paccayaṃ (CTX ^7-2-85) | ကြောင့် | အကြောင်း | 1 | «(Ekekaṃ paccayaṃ mūlakaṃ kātūna …)» «(အကြောင်း တစ်ခုစီကို အခြေခံ ပြု၍ …)» |

Checked and kept: the standalone paccayā of the paccayavāra, «Kusalaṃ dhammaṃ paccayā» «ကုသိုလ် သဘောတရားကြောင့်». Its value «ကြောင့်» (pi-2, 1-02 phase 1) is the text's word.

## Values that differ from pi-1 … pi-6 or from the sample (same keyword)

- **Module values already explained in phase 1:** the T1 / T2 condition names and cases, the T6 counts «…ခု», U1 assādeti, U4, datvā / deti, paccavekkhati, vipassati, uppādeti, sahajāto, nirodhā, vuṭṭhahantassa, bhaṇati, harati, tiṭṭhati, Kusalākusalaṃ, mūlakaṃ, and katvā (no direct equivalent).
  - They appear in g1 the same way, and `map_g1.py --diff` lists them.
  - The same holds for module term values such as the abyākata compounds (kiriyābyākataṃ / -te, vipākābyākate, without the pi-2 head «စိတ် / သဘောတရား») and bhojanaṃ «အစားအစာ» (pi «ဘောဇဉ်»). The coordinator settles these in phase 3, as for the sample.
- **g1 values that differ from pi-1 … pi-6:**
  - Natthi «မရှိခြင်းဟူသော အကြောင်း» / «မရှိခြင်း» (pi «မရှိသည်»): T4.
  - kusale «ကုသိုလ်» (pi-2 «ကုသိုလ် သဘောတရား»): the text has no «သဘောတရား» with this word.
  - uppādenti «ဖြစ်စေသည်» (pi-5 «ဖြစ်ပေါ်စေသည်»): not the text's verb.
  - Cakkaṃ «စက်ဝိုင်း» (pi «လှည့်ပတ်ခြင်း»): not in the segment.
- **Values that differ from the sample chapters:** none for the same keyword in the same kind of segment.
  - suciṇṇāni, tadārammaṇatā and ṭhānāṭhānakosallassa take two forms because the text has two forms (§A).

## S1 review (stem fallback): 13 uses, 13 kept, 0 corrected

Each value was checked by eye against the segment and the sense:
- passati «မြင်သည်»: ^7-2-410, ^7-4-94, ^7-5-52, ^7-5-65, ^7-5-82; «dibbena cakkhunā rūpaṃ passati» «… အဆင်းအရောင်ကို မြင်သည်».
- bhinditvā «ဖြိုခွဲ၍»: ^7-2-423, ^7-6-14; «saṅghaṃ bhinditvā» «သံဃာကို ဖြိုခွဲ၍».
- pisuṇavācā «ကုန်းတိုက်သော စကား» and pharusavācā «ကြမ်းတမ်းသော စကား»: ^7-2-423.
- ādiyitvā «ယူ၍»: ^7-2-423, «adinnaṃ ādiyitvā» «မပေးသည်ကို ယူ၍».
- uppādetvā «ထွက်စေ၍»: ^7-2-423, «lohitaṃ uppādetvā» «သွေးကို ထွက်စေ၍».
- vibhajitabbāni «ခွဲခြမ်းစိတ်ဖြာရမည့်»: ^7-4-85; rule 3, the text «ခွဲခြမ်းစိတ်ဖြာရမည်».
- sajjhāyamaggo «သရဇ္ဈာယ်သည့် နည်းလမ်း»: ^7-U277, notes-ch1-03-05.

## A. Text inconsistencies (for the rails step; the translation is not changed)

1. **ṭhānāṭhānakosallassa**: 1-01 has «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း»; 1-03, 1-04 and 1-05 have «ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု».
2. **pubbe suciṇṇāni**: 1-01 has «ရှေးက ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှုတို့», with the added noun «အမှု»; 1-03, 1-04 and 1-05 have «ရှေးက ကောင်းစွာ ပြုခဲ့ဖူးသည်တို့». notes-ch1-03-05 records the second form as [NEW].
3. **tadārammaṇatā**: 1-01 has «ထိုအာရုံကို အာရုံပြုသည့် အနေဖြင့်»; 1-03, 1-04 and 1-05 have «ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့်».
4. **tassa paṭighātatthāya**: the text has «ထိုအမှုကို ချေဖျက်ရန်» in every g1 chapter. The notes-ch1-01 term list gives «ထိုအမှုကို ပယ်ဖျက်ရန်အတွက်», which the text does not use. The mapping follows the text.
5. **X-kiriya compounds**: the text adds «စိတ်» («… နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်», «ပြုရုံမျှသာ ဖြစ်သော စိတ်အား»), and notes-ch1-01 records the compound values with «စိတ်». The values drop it, as the module does for kiriyaṃ (phase-1 A5).
6. **uppannaṃ (samāpattiṃ) samāpajjati**: in 1-01 ^7-2-423 the text repeats the noun, «ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို ဝင်စား…». In 1-03 ^7-4-103 it nominalises instead, «ဖြစ်ပေါ်ပြီးသည်ကို ဝင်စားသည်». The module value «ဖြစ်ပေါ်ပြီးသော» stands in both, by the ending rule.

## B. Unclear mappings (for the coordinator)

1. **kiriya compounds without «စိတ်»** (A5). The alternative keeps «စိတ်» in the four compound keywords, as the pi-7 notes do. The plain kiriyaṃ / kiriyassa of the module would then stay without it.
2. **gaṇite «ရေတွက်သော»**. The locative absolute follows the pi-5 niruddhe precedent. The alternative is the text's whole «ရေတွက်သောအခါ».
3. **gambhīrā «နက်နဲ»**. This is U1 applied to an adjective. The alternative is «နက်နဲ၍».
4. **ṭhitena «တည်၍»**. This is the text's adverbial. The alternative is rule 3 «တည်သော», the module value, which stands only by an ending rule.
5. **paṭighātatthāya «ချေဖျက်ရန်»**. It keeps the purpose marker «ရန်» as the meaning of -atthāya. The alternative is the bare «ချေဖျက်».
6. **Sahetādhipati**. It takes the two condition names and the closing «ပါဝင်သော» across a gap, as phase-1 Saindriya / Sādhipati do.
