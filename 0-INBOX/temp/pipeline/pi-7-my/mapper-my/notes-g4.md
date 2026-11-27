# pi-7 Burmese keyword mapping, phase 2, group g4: notes (3-09-mahantaraduka, 3-10-upadanagocchaka, 4-01-kilesagocchaka)

Script `map_g4.py` imports `map7_rules.py` (md5 909bed2528b27eb55051c73f3ce28f81, not edited). It holds one group
table `G4` (the same for the three chapters), two per-segment overrides (`CTX`) and one new context function
(`f_natthi_g4`). Helpers are in `work/g4_*.py`, and all of them are read-only. The translation is not changed.

## Numbers

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) | stem (S1) uses |
|---|---|---|---|---|---|---|
| 3-09-mahantaraduka | 1084 | [] | 0 | 0 | 6 | 38 |
| 3-10-upadanagocchaka | 251 | [] | 0 | 0 | 8 | 8 |
| 4-01-kilesagocchaka | 1075 | [] | 0 | 0 | 29 | 27 |

- The (no direct equivalent) uses break down as follows:
  - katvā 19 and karoti 13, every one after uposathakammaṃ / gāmaghātaṃ / nigamaghātaṃ (T11, f_karoti, checked
    segment by segment);
  - ceva 10 (rule 9);
  - nti 1 (rule 9).
- Every chunk of every value is in its segment, literally or by an approved ending rule. The new values that need an
  ending rule are:
  - «တူသည်» for the text's «တူကြသည်» / «တူသည့်အတိုင်း» (verb);
  - «…ရမည့်» for «…ရမည်» (attr-fut);
  - «ပြည့်စုံသည်», «ဖြစ်စေသည်» and «ရှုသည်» for the «ကြ» forms (verb).
- Running the script twice gives byte-identical files.
- Values against pi-1 … pi-6, for the same keyword or its base form (R1):
  - 14677 uses equal a pi-1 … pi-6 value;
  - 16694 uses are of keywords pi-1 … pi-6 never mapped;
  - 1258 uses differ, in 50 keyword / value pairs (§D).

## A. Rules used

- **Binding rules:** pi-1 rules 1–11 and the agreed later rules; pi-2 N1–N11; pi-3 M1–M9; pi-4 P1–P8 / A2; pi-5 Q1–Q8,
  S1; pi-6 R1–R9 and the phase-3 mechanics.
- **Phase-1 rules:** T1–T13, M1 and M2, with the coordinator's decisions U1–U5.
- **Where each rule is applied here:**
  - T5 / T9 for the -sadisa notes and the dyad names;
  - T6 for X-mūlake;
  - T7 / T8 for diṭṭhigatavippayuttalobhasahagata- and noupādā;
  - T11 for gāmaghātaṃ;
  - T12 for X-adhipati and X-cittasamaṅgissa;
  - pi-4 P6 for the agent nouns pūretukāmena and vibhajantena;
  - rule 1 for the dropped «၌ / အား / ဖြင့် / အတိုင်း»;
  - rule 3 for the gerundives «…ရမည့်»;
  - R7 for the «လည်း» gap.

## B. New rules (group level, for phase 3)

- **G1. X-dukasadisa** = «X နှစ်မျိုးတွဲနှင့် တူသည်», or the text's adverbial «…နှင့် တူအောင်» before «ပြုရမည်».
  - X is the dyad name of the text's own heading «X နှစ်မျိုးတွဲ» (T9).
  - This is T5's -sadisa rule applied to a dyad instead of a vāra.
  - Table `DUKA`: cittasamuṭṭhāna, cittasahabhū, lokiya, upādāna, sappītika, arūpa, arūpāvacara, kilesa and
    pahātabbahetuka.
  - Uses: 3-09 has 9, 3-10 has 4 and 4-01 has 22.
- **G2. X-gamanasadisa / dutiyavārasadisa** = «ပထမ / ဒုတိယ သွားပုံနှင့် တူသည်» or «ဒုတိယ ဖော်ပြချက်နှင့် တူသည်», the
  text's words.
  - gamanā is «သွားပုံ», and dutiyavāre is «ဒုတိယ ဖော်ပြချက်» (rule 1).
- **G3. natthi inside a term** (`f_natthi_g4`): the module's f_natthi takes «မရှိသည်» wherever the segment has it.
  - In ^7-32-214 the only «မရှိသည်» is inside «… မှတ်သိမှု မရှိသည်လည်း မဟုတ်» (nevasaññānāsaññāyatana).
  - There the note's own «(… ထမြောက်ခြင်း စိတ် မရှိ)» is taken: «မရှိ» (pi-5 Q5). This affects 3 uses.
- **G4. A condition name in the nominative plural as «the kinds»** («tīṇi upanissayā» «အားကြီးသော အမှီ သုံးခု»): the
  bare name N (T1), not the ablative of T2. This affects 5 uses.
- **G5. A dyad member compound with a supplied head**: these keep what the text joins to the keyword.
  - X-mūlake «… သဘောတရားကို အခြေခံခြင်း» (T6);
  - pahātabbabhājanakāraṇe «ပယ်ရမည့် … သဘောတရားကို ခွဲခြားသည့် နည်းလမ်း», where the gap holds the «မဟုတ်သော» of
    nabhāvanāya.
  - A head noun that only follows the keyword is left out, as in harmonise A5: arūpamissake without «အပိုင်း», and
    suddhake «ရိုးရိုး».

## C. Module overrides (for the coordinator to move into map7_rules.py in phase 3)

| keyword | module value | g4 value | uses | reason |
|---|---|---|---|---|
| pīti | (no direct equivalent) | ပီတိ | 53 | FRAME has pīti = pi + iti; in 4-01 every pīti is the noun «ပီတိ» («khandhā ca pīti ca»). The module needs a context function: the noun where the text has «ပီတိ» for it. |
| natthi (^7-32-214) | မရှိသည် | မရှိ | 3 | G3 |
| ajjhattikassa | အတွင်း (pi-2) | အတွင်းပိုင်း | 29 | the pi-2 value stands only inside the word «အတွင်းပိုင်း» (phrase_ok accepts a value followed by more letters of the same word) |
| cakkaṃ / Cakkaṃ / cakkā | စက် | စက်ဝိုင်း | 19 | the same sub-word problem: the text's «(စက်ဝိုင်း)» |
| noupādā / Noupādā | မှီ၍ … မဟုတ်သော | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော | 45 | T8 na-X of upādā «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော»; the module's gapped value had lost the noun |
| kilesānañca | ကိလေသာ … ဖြစ်သော | ကိလေသာ | 4 | the noun «ကိလေသာတို့အားလည်းကောင်း» («khandhānaṃ kilesānañca») |
| tadārammaṇatā | စိတ်သည် | ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ် | 5 | the module value was the head noun of vipāko; rule 1: «ဖြင့်» goes |
| pañcaviññāṇaṃ / Pañcaviññāṇaṃ | သိစိတ် | သိစိတ် ငါးပါး | 2 | the text's «သိစိတ် ငါးပါး» (pi-5 pañcaviññāṇā) |
| uppādenti | ဖြစ်စေကြသည် | ဖြစ်စေသည် | 2 | dictionary form (LEXW uppādeti); «ကြ» by the ending rule |
| vipassanti | ထိုးထွင်း၍ ရှုကြသည် | ထိုးထွင်း၍ ရှုသည် | 1 | as uppādenti (LEXW vipassati) |
| gaṇetabbā | ရေတွက်ရမည် | ရေတွက်ရမည့် | 1 | rule 3 (FRAME gaṇetabbaṃ) |
| vitthāretabbāni | အကျယ် ချဲ့ရမည် | အကျယ် ချဲ့ရမည့် | 1 | rule 3 (FRAME vitthāretabbā) |
| paripuṇṇā | ပြည့်စုံ | ပြည့်စုံသည် | 1 | the text's verb «ပြည့်စုံကြသည်» (rule 4) |
| bhāgo (CTX ^7-33-116) | သဘော | အပိုင်း | 2 | «Tatiyo bhāgo niṭṭhito» «တတိယ အပိုင်း ပြီးဆုံးပြီ» |
| vipāke (CTX ^7-35-232) | ကံ၏ အကျိုး | ကံ၏ အကျိုး ဖြစ်သော | 1 | «vipāke rūpāvacare khandhe»: the attributive (rule 3, STOCK vipāko) |
| paccavekkhitvā | ဆင်ခြင်၍ (stem) | ပြန်လည် ဆင်ခြင်၍ | 1 | S1 corrected: U3, the pi-7 word of paccavekkhati |

The sub-word problem behind ajjhattikassa and cakkaṃ is general. A pi-1 … pi-6 value or a term value that the segment
has only as the start of a longer word should not pass. map-table.md already says such a value «is not taken», but
the module's check does not catch a value that is followed by more letters of the same word.

## D. Values that differ from pi-1 … pi-6 or from the sample (same keyword)

**g4 table values:**

| keyword = g4 value | prior value | reason |
|---|---|---|
| ajjhattikassa = အတွင်းပိုင်း | pi-2 အတွင်း | §C (the text's word) |
| cakkaṃ = စက်ဝိုင်း | လှည့်ပတ်ခြင်း | the text's «(စက်ဝိုင်း)»; the prior value is not in the segment |
| natthi = မရှိ | မရှိသည် | G3 / pi-5 Q5 |
| uppādenti = ဖြစ်စေသည် | ဖြစ်ပေါ်စေသည် | phase-1 uppādeti «ဖြစ်စေသည်» (LEXW); the prior value is not in the segment |
| nānākaraṇaṃ = ကွဲပြားချက် | ကွဲပြားမှု | the text's «ကွဲပြားချက် ဖြစ်သည်» (FRAME ninnānākaraṇaṃ «ကွဲပြားချက် မရှိ») |
| likhitaṃ = ရေးထားသော | ပွတ်ထားသော | the text's «ရေးထားသော စာ»; the prior value has another sense |
| passitvā = ကြည့်၍ | မြင်၍ | the text's «… ကို ကြည့်၍»; the prior value is not in the segment |

**Against the sample:**
- **gāmaghātaṃ = «ရွာ»** (3 uses): «…pe…» cuts the verb off, «ရွာကို… နိဂုံးကို ဖျက်ဆီး၍ လုယက်သည်». This is the bare
  noun, as in STOCK uposathakammaṃ. The one use with the whole phrase keeps «ရွာကို ဖျက်ဆီး၍ လုယက်သည်».
- **vipāke (^7-35-232):** §C.

**Module values that differ** (phase-1 rules; the text's own word, with the prior value not in the segment):
- **Settled in phase 1:** vatthu «မှီရာ ဝတ္ထု», assādeti «သာယာ» (U1), the counting locatives (T2), uppādeti,
  paccavekkhati, deti / datvā / katvā (T11), anulomaṃ «လျော်ညီခြင်း စိတ်» (the mind moment: «anulomaṃ gotrabhussa /
  vodānassa / phalasamāpattiyā», checked), kusalākusalaṃ, nirodhā, vuṭṭhahantassa, vipassati, bhaṇati, and R7 gaps
  (saṃkiliṭṭho, saṃkilesiko).
- **New in this group but standard module output:**
  - sahajātaṃ «အတူ ပေါ်ပေါက်ခြင်း» (the kamma kind);
  - asaññasattā «အသညသတ်»;
  - pañhā «ပြဿနာ»;
  - bhojanaṃ «အစားအစာ»;
  - bāhiro «ပြင်ပ»;
  - parikammaṃ «ကြိုတင် ပြင်ဆင်မှု»;
  - vodānaṃ «စင်ကြယ်ခြင်း စိတ်»;
  - voropeti «သတ်သည်»;
  - patthanā «တောင့်တခြင်း»;
  - ekoyeva «တစ်ခု».

## E. S1 stem-fallback review

There were 74 stem uses, each checked by eye against the segment's Pāli and Burmese. **73 are kept and 1 is
corrected.**

- **Kept:**
  - passati «မြင်သည်» (30: «dibbena cakkhunā rūpaṃ passati» «… အဆင်းအရောင်ကို မြင်သည်»);
  - itare / Itare «အခြား» (18: «itare dve» «အခြား နှစ်ခု», «itaresu» «အခြားတို့၌»);
  - ninnānākaraṇā «ကွဲပြားချက် မရှိ» (10);
  - Cittasaṃsaṭṭhasamuṭṭhānañca / -ṃ «စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော» (8);
  - vibhajitabbaṃ / -o / -āni «ခွဲခြမ်းစိတ်ဖြာရမည့်» (4);
  - uppajanti «ဖြစ်ပေါ်သည်» (1, the Pāli spelling of uppajjanti);
  - bhinditvā «ဖြိုခွဲ၍» (1: «saṅghaṃ bhinditvā» «သံဃာကို ဖြိုခွဲ၍»);
  - suddhake «ရိုးရိုး» (1).
- **Corrected:** paccavekkhitvā «ဆင်ခြင်၍» → «ပြန်လည် ဆင်ခြင်၍» (§C).

## F. Newly mapped keywords

**83 keyword forms, 234 uses, unmapped by the module.** Every one now has a value.

- **The -sadisa dyad and gamana notes:** G1 and G2.
- **diṭṭhigatavippayuttalobhasahagata- in five cases** (99 uses): «အယူမှားနှင့် ကင်းကွာသော လောဘနှင့်အတူ ဖြစ်သော».
  - This is the generator's stacked qualifier; the «၊» goes by rule 6.
  - -ādhipati adds « အကြီးအမှူး».
- **Doctrinal and situational terms:**
  - viññāṇañcāyatanavipākassa, ākāsānañcāyatanakusalaṃ;
  - ṭhānāṭhānakosallassa «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း» (the inner «၌» stays; rule 1);
  - niyatamicchādiṭṭhiyā;
  - vicikicchāsahagatamohaṭṭhāne;
  - noupādācittasamaṅgissa;
  - pahātabbahetukādhipati (alt «ပယ်ရမည့် အမြစ် ရှိသည် … အကြီးအမှူး» after nadassanena);
  - cakkhu- / vaṇṇa- / gandha- / rasasampadaṃ «X ပြည့်စုံခြင်း»;
  - sakabhaṇḍe;
  - paṭighātatthāya «ချေဖျက်ရန်».
- **Note words:**
  - āmasanaṃ / -ā «ရည်ညွှန်းပုံ», ninnānā, nānākaraṇaṃ;
  - the gerundives niyāmetabba-, uddharitabba-, dassetabbo, kātabbāni;
  - the agent nouns pūretukāmena, vibhajantena;
  - asammohantena (= FRAME asammuyhantena), garukārammaṇā, iminākāreneva, sabbaṭṭhāne, paṭhamasseva, paṭhamaṃ,
    pākatikā, likhitaṃ, passitvā, pavesetvā, ekasadisā;
  - the vāra names anulomapaccayavāraṃ / anulomapaṭiccavāro «အဟုတ်ပြ ပုံစံ၏ …အလိုက် ဖော်ပြချက်» (T5);
  - dassanadukaṃ, arūpamissake, upādinnamūlake, pavattipaṭisandhi(yā), upanissayā (G4), gāmaghātaṃ, nti.

## G. Text inconsistencies (for the rails step)

1. **arūpa- in dyad names is rendered as the plane.** arūpadukasadisa- is «ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲ» (4-01
   ^7-35-320 / -338 / -349). The dyad terms arūpino / arūpaṃ are «ရုပ် မဟုတ်သော», and arūpāvacaraduka is «ရုပ်မရှိသော
   ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ». The mapping follows the text.
2. **The same note, read two ways.**
   - ^7-35-204 «suddhake arūpamissake ca» is «ရိုးရိုး အပိုင်း၌လည်းကောင်း၊ ရုပ် မဟုတ်သော သဘောတရားနှင့်
     ရောနှောသော အပိုင်း၌လည်းကောင်း».
   - ^7-35-243 «suddhike arūpe ca missake ca» is «ရိုးရိုး အပိုင်း၌ ရုပ်မရှိသော ဘုံ၌လည်းကောင်း၊ ရောနှောသော
     အပိုင်း၌လည်းကောင်း», with arūpa as the plane.
   - The Pāli spellings differ too: suddhaka and suddhika.
3. **nānā(karaṇa) has two nouns.**
   - «ကွဲပြားချက်»: ninnānākaraṇaṃ «ကွဲပြားချက် မရှိ», nānākaraṇaṃ «ကွဲပြားချက် ဖြစ်သည်».
   - «ကွဲပြားမှု»: 3-10 ^7-33-98 «upādānadukasadisā ninnānā» «ကွဲပြားမှု မရှိ», and 4-01 ^7-35-167 «āmasanaṃ
     ninnānaṃ» «ရည်ညွှန်းပုံသည် ကွဲပြားမှု မရှိ».
4. **A fourth -sadisa shape:** 4-01 ^7-35-345 has «… နှစ်မျိုးတွဲနှင့် တူသည့်အတိုင်း» (harmonise A4 lists three shapes).
5. **«ပယ်ရမည်» without the final dot.** 4-01 ^7-35-101 has «ပယ်ရမည် မဟုတ်သော» (twice) against «ပယ်ရမည့်» everywhere
   else.
6. **Head nouns the text adds** (harmonise A5); each is mapped without the noun:
   - «စိတ်» after vipāko in «ကံ၏ အကျိုး ဖြစ်သော စိတ်သည် ထိုအာရုံကိုပင် …» (^7-32-447);
   - «ပြဿနာ» after paṭhamasseva «ပထမ ပြဿနာ၌သာ» (^7-32-461);
   - «အပိုင်း» after suddhake / arūpamissake;
   - «ထိုအမှု» for tassa in «tassa paṭighātatthāya».
7. **Keyword-file gaps:**
   - ^7-32-76 has «purimagamanasadisaṃ» in the Pāli but not in the keyword list;
   - ^7-35-243 lists nti but not suddhike / missake.

   The lists are mapped as given.

## H. Unclear mappings (for the coordinator)

- **upādinnamūlake = «ကံကြောင့် ဖြစ်သော သဘောတရားကို အခြေခံခြင်း»** keeps the text's inner «သဘောတရား». It cannot be
  cut out without a gapped «… ကို» chunk. Compare harmonise A5 on Abyākatamūlaṃ (5-11, group g6), which should be
  decided the same way.
- **pavattipaṭisandhi(yā) = «ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ»**: rule 1, plus the R7 gap for the text's «၌လည်း၊». The
  alternative is «ဘဝ ဖြစ်စဉ်၌လည်း ပဋိသန္ဓေ», which keeps the inner particle. The keyword is also unmapped in other
  groups (11 uses book-wide).
- **pahātabbabhājanakāraṇe = «ပယ်ရမည့် … သဘောတရားကို ခွဲခြားသည့် နည်းလမ်း»** (G5): the gap holds nabhāvanāya's
  negation.
- **pākatikā = «ပကတိ»**: «အတိုင်း» is dropped, as in vācanāmaggena. The alternative is the text's whole
  «ပကတိအတိုင်း».
- **iminākāreneva = «ဤ ပုံစံ»**: R1 and rule 1 drop «အတိုင်းပင်». The alternative is «ဤ ပုံစံအတိုင်းပင်».
- **gāmaghātaṃ = «ရွာ»** where «…pe…» cuts the verb off (U2 applied to a cut-off phrase, as in STOCK uposathakammaṃ).
