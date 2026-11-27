# pi-7 Burmese keyword mapping: text inconsistencies, consistency scan, S1 review (phases 1–3)

Phase 1 (preamble, 1-00-paccaya, 1-02-vedanattika) wrote the first version of this file (kept as
`work/map-harmonise-notes-phase1.md`); phase 2 (groups g1 … g6) wrote `notes-g1.md` … `notes-g6.md`; phase 3
(2026-11-26, whole book, under the user's standing go-ahead) wrote this version. The translation was not changed.
Burmese only from this track's FINAL pi-7 text, `my7-zeroshot-terms.md`, the pi-7 generators (read as text) and the
final pi-1 … pi-6 mappings; pi-1-my … pi-6-my were only read.

Phase-3 files: `phase3-changes.tsv` (every value that differs from the phase-2 files, 214 rows, each with its stage
and reason), the staged runs `work/stages/<stage>/` (+ `work/p3_diff_<stage>.tsv`, `work/stages/order.txt`), the
phase-2 snapshot `work/phase2-mapped/` (md5 = `work/before-phase3-files-md5.txt`) and `work/phase2-scripts/`, the scans
`work/scan-before.tsv`, `work/scan-mid.tsv`, `work/scan-after.tsv` (+ `-detail.txt`), `work/scan-family-mid.tsv` /
`work/scan-family-after.tsv`, `work/scan-class.tsv`, the S1 list `work/p3_s1_after.tsv`, the verification
`work/p3_verify_all.txt`, `work/p3_md5_run3.txt` / `work/p3_md5_run4.txt`. Helpers: `work/p3_stage.py`,
`work/p3_changes.py`, `work/p3_s1.py`, `work/map_scan.py`, `work/p3_family_scan.py`, `work/p3_scan_classify.py`,
`work/p3_verify_all.py`, `work/p3_kw.py`, `work/p3_grep.py`, `work/p3_tables.py`, `work/p3_strip.py` (p3_stage /
p3_changes / map_scan modelled on pi-6-my/mapper-my/work, copied, not imported).

## A. Text inconsistencies for the rails step (merged: phase 1 §A 1–12, notes-g1 A1–A6, notes-g2 G1–G10, notes-g3 1–6, notes-g4 G1–G7, notes-g5 1–5, notes-g6 1–6, and the phase-3 scan)

1. **samanantarā (adverb)** (phase 1 A1): «ကောင်းစွာ ချက်ချင်း နောက်၌» (^7-1-5), the word of the condition name; pi-5
   ^5-576 has «ချက်ချင်း နောက်၌», the word pi-7 uses for anantarā (^7-1-4).
2. **paccavekkhati / -anti / paccavekkhitvā** (phase 1 A2, U3): pi-7 «ပြန်လည် ဆင်ခြင်», against pi-2 / pi-5 «ဆင်ခြင်».
3. **kusalākusalaṃ (kammaṃ)** (phase 1 A3): pi-7 «ကုသိုလ်နှင့် အကုသိုလ် ကံ», against pi-1 «ကုသိုလ် အကုသိုလ်».
4. **The -sadisa notes in four shapes** (phase 1 A4, g3 6, g4 G4, g5 2, g6 3): «…နှင့် တူသည်» (most), «…နှင့်
   တူကြသည်» (-sadisā, H24), the adverbial «…နှင့် တူအောင် ပြုရမည် / အကျယ် ချဲ့ရမည်» before kātabbā / vitthāretabbā
   (2-08 ^7-14-24, 3-01 ^7-24-19, 4-02 ^7-36-11, 4-07 ^7-41-27, 4-10 ^7-44-17, 4-13 ^7-47-104 …), and «…နှင့်
   တူသည့်အတိုင်း» after yathā (4-01 ^7-35-345, 4-13 ^7-47-76). Each segment's form is mapped (coordinator).
5. **Head nouns the text adds after the keyword** (each mapped without the noun, phase 1 A5): «ကံ» after the kamma kinds
   sahajātā / nānākkhaṇikā (H7); «စိတ်» after kiriyaṃ and the X-kiriya compounds (g1 A5, g2 G7; notes-ch1-01 records
   the compounds with «စိတ်»); «အမှု» after suciṇṇāni (1-01 «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှုတို့»); «ရုပ်» after
   X-samuṭṭhāna (H8 4); «စိတ်» after vipāko in «… ကံ၏ အကျိုး ဖြစ်သော စိတ်သည် ထိုအာရုံကိုပင် …» (g3 5, g4 G6); «ပြဿနာ»
   after paṭhamasseva (^7-32-461); «အပိုင်း» after suddhake / arūpamissake (g4 G6); «ထိုအမှု» for tassa in «tassa
   paṭighātatthāya» (g1 A4, g4 G6). The mind-moment names (gotrabhu, vodāna, bhavaṅga, upapatticitta) keep «စိတ်».
6. **The head noun «သဘောတရား» inside the -sadisa / -mūla / -kāraṇa notes** (g2 G7, g4 H, g5 3, g6 3, phase 1
   Abyākatamūlaṃ): the Pāli has no dhamma. Phase 3 (coordinator) leaves it out with a « … » gap wherever the next chunk
   does not start with a particle (Abyākatamūlaṃ / -mūle, the G2-3 term-mūlakas, upādinnamūlake, pahātabbabhājanakāraṇe)
   and keeps it inside where a gap is impossible: the g5 «… ၏ ကုသိုလ် / အကုသိုလ် / … မဟုတ်သော သဘောတရားနှင့် တူသည်»
   notes (21 forms), atītasadisaṃ «အတိတ် သဘောတရားနှင့် တူသည်», sappaccayasadisaṃ «အကြောင်း ရှိသော သဘောတရားနှင့်
   တူသည်», arūpamissake «ရုပ် မဟုတ်သော သဘောတရားနှင့် ရောနှောသော». Against these, Sappaccayadukasadisaṃ (5-02 ^7-56-22) and
   lokiyadukasadisaṃ have the bare dyad name.
7. **assādeti abhinandati share one ending** «သာယာ နှစ်သက်သည်» (phase 1 A6): assādeti has no «…သည်» form there (U1).
8. **Act compounds carry their verb** (phase 1 A7): «uposathakammaṃ katvā / karoti» «ဥပုသ်ကို စောင့်ထိန်း၍ / …သည်»,
   «gāmaghātaṃ / nigamaghātaṃ karoti», «ekāgārikaṃ karoti», «dānaṃ datvā / deti» «ပေးလှူခြင်းကို ပြု၍ / ပြုသည်»,
   «paripanthe tiṭṭhati» «လမ်းခရီး၌ ဓားပြ တိုက်သည်». Cut off by …pe…, uposathakammaṃ is «ဥပုသ်…» in some segments and
   «ဥပုသ် စောင့်ထိန်းခြင်း…» in others (g2 G5), gāmaghātaṃ «ရွာကို…» (4-01).
9. **kātabbā** «ထည့်ရမည်» ("to be included", ^7-4-110 / ^7-4-111 «paṭisandhi kātabbā») and «ပြုရမည်» elsewhere
   (phase 1 A8).
10. **The list comma inside terms**: abyākata «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော» and the stacked qualifiers «A၊ B
    N» (diṭṭhigatavippayuttalobhasahagata- «အယူမှားနှင့် ကင်းကွာသော၊ လောဘနှင့်အတူ ဖြစ်သော»); the values drop the «၊»
    (rule 6; phase 1 A9, g3 G3, g4 G3).
11. **paṭicca and nissāya are both «… ကို မှီ၍»** (phase 1 A10).
12. **Pāli spellings and slips, mapped as written**: upādinna- against pi-1 upādiṇṇa- (A11); Ghāṇaviññāṇadhātu and the
    hyphen slips of the ghaṭanā lists (notes-sample); vicākānaṃ for vipākānaṃ (^7-7-114; g2 G1); paṭibhānapaṭisambhidāya
    (2-05) against paṭibhānappaṭisambhidāya, ārammaṇaupanissayā against ārammaṇūpanissayo (g2 G9); lokuttarasa for
    lokuttarassa (3-02), idaṃsaccābhinivesaṃ kāyaganthaṃ (two words) beside idaṃsaccābhinivesakāyaganthaṃ (3-05; g3 4);
    suddhaka / suddhika (4-01; g4 G2); asakkho for asekkho (^7-36-338), sāsavoca for «sāsavo ca» (^7-39-36; g5 1);
    ovattā, found only at ^7-72-57 (elsewhere parivatta-; g6 2); «nano ca āsavo / nano ca saññojano» against nanoāsavo
    (5-04; g6 1); uppajanti for uppajjanti (3-09, S1).
13. **The ablative -to forms** aniccato / dukkhato / anattato «မမြဲဟု / ဆင်းရဲဟု / အတ္တ မဟုတ်ဟု»: the quotative «ဟု» goes
    in the value (phase 1 A12, pi-5 aniccato «မမြဲ»).
14. **ṭhānāṭhānakosallassa, two renderings** (g1 A1, g2 G2): «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း» (1-01,
    2-05, 2-06, 3-02, 4-01 …) and «ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု» (1-03 … 1-05, 2-07
    ^7-13-74, 2-10 ^7-16-46).
15. **pubbe suciṇṇāni, two renderings** (g1 A2, g2 G3): «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှုတို့» (1-01, 2-03, 2-05, 2-06,
    2-13, 2-15 … 4-01) and «ကောင်းစွာ ပြုခဲ့ဖူးသည်တို့» (1-03 … 1-05, 2-01, 2-07, 2-08, 2-10; notes-ch1-03-05 [NEW]).
16. **tadārammaṇatā, two renderings** (g1 A3, g3 5): «ထိုအာရုံကို အာရုံပြုသည့် အနေဖြင့်» (1-01, 2-05 ^7-11-46) and
    «ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့်» (1-03 … 1-05, 3-01, 3-09).
17. **tassa paṭighātatthāya** (g1 A4): the text has «ထိုအမှုကို ချေဖျက်ရန်» everywhere; the notes-ch1-01 term list has
    «ထိုအမှုကို ပယ်ဖျက်ရန်အတွက်», which the text does not use.
18. **uppannaṃ (samāpattiṃ) samāpajjati** (g1 A6): 1-01 ^7-2-423 repeats the noun «ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို
    ဝင်စား…»; 1-03 ^7-4-103 nominalises «ဖြစ်ပေါ်ပြီးသည်ကို ဝင်စားသည်».
19. **pavatti** (g2 G4, g3 1): «ဘဝ ဖြစ်စဉ်» (2-04, 2-14, 2-15, 3-01, 3-02, 3-09, 4-01) and «ဘဝ ဖြစ်ဆဲ ကာလ» (2-07, and
    2-01 «pavattipi» «ဘဝ ဖြစ်ဆဲ ကာလကိုလည်း»), against pi-6 pavatte «ဘဝ တည်နေစဉ်».
20. **The verb dropped in abbreviated sentences** (g2 G6): «ဖြစ်ပေါ်သည်» (uppajjati) is missing in the aligned sentence
    of ^7-9-19, ^7-9-42, ^7-10-20, ^7-22-5 (the value stands elsewhere in the segment).
21. **The sekkha triad** (g2 G8): the body has «ကျင့်ကြံဆဲသူ၏» (qualifier), the heading Sekkhattikaṃ «ကျင့်ကြံဆဲသူ
    သုံးမျိုးတွဲ», the persons «ကျင့်ကြံဆဲသူတို့».
22. **passitvā «ကြည့်၍»** ("looking at"), against pi-4 «မြင်၍» (g2 G10).
23. **naviññeyyo «(…စိတ်ဖြင့်) မသိနိုင်သော»**, not the na-X form of H21 «သိနိုင်သည် မဟုတ်သော» (g3 2; the coordinator keeps
    the text's lexical negative). Part 5 has both: «kenaci naviññeyyo» «… မသိနိုင်သော», «Nakenaci viññeyyaṃ» «…
    သိနိုင်သည် မဟုတ်သော».
24. **rūpī / arūpī** «ရုပ် ဖြစ်သော / ရုပ် မဟုတ်သော», against pi-1 … pi-6 «ရုပ် ရှိသော / ရုပ် မရှိသော» (g3 3).
25. **arūpa- in dyad names is the plane** (g4 G1): arūpadukasadisa- «ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲ» (4-01), while the dyad
    terms arūpino / arūpaṃ are «ရုပ် မဟုတ်သော».
26. **The same note read two ways** (g4 G2): ^7-35-204 «suddhake arūpamissake ca» «ရိုးရိုး အပိုင်း၌လည်းကောင်း၊ ရုပ်
    မဟုတ်သော သဘောတရားနှင့် ရောနှောသော အပိုင်း၌လည်းကောင်း» against ^7-35-243 «suddhike arūpe ca missake ca» «ရိုးရိုး
    အပိုင်း၌ ရုပ်မရှိသော ဘုံ၌လည်းကောင်း၊ ရောနှောသော အပိုင်း၌လည်းကောင်း».
27. **nānā(karaṇa) has two nouns** (g4 G3): «ကွဲပြားချက်» (ninnānākaraṇaṃ, nānākaraṇaṃ) and «ကွဲပြားမှု» (^7-33-98
    ninnānā, ^7-35-167 ninnānaṃ).
28. **«ပယ်ရမည် မဟုတ်သော» without the final dot** at 4-01 ^7-35-101 (twice), against «ပယ်ရမည့်» everywhere else (g4 G5).
29. **Keyword-file gaps** (g4 G7, g5 1, g6 1): ^7-32-76 has purimagamanasadisaṃ in the Pāli but not in the list;
    ^7-35-243 lists nti but not suddhike / missake; ^7-39-36 lacks sāsavo (the slip sāsavoca); the «nano ca X» segments
    list only the bare āsavo / saññojano / saññojanañca. The lists are mapped as given.
30. **«belonging to» in the dyad names inside notes** (g5 4): lokiyaduka «လောကနှင့် သက်ဆိုင်ခြင်း», kāmāvacaraduka
    «ကာမဘုံနှင့် ဆိုင်ခြင်း».
31. **The elliptic «(dassane ekaṃ, nadassane dve)»** (4-13 ^7-47-6, ^7-47-17) is spelled out in the text as the full term
    «သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် / ပယ်ရမည် မဟုတ်သော သဘောတရား၌» (g5 5).
32. **Anulomadukatikapaṭṭhānato** (5-20 ^7-74-92), one Pāli compound, is split in the text into the order and a quoted
    title «အဟုတ်ပြ ပုံစံ၌ “နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ …” မှ» (g6 4).
33. **nevadassanena** (g2 G2-2, g5 U-g5-4, g6 5): one value book-wide, «သစ္စာကို မြင်ခြင်း … မဟုတ်» (35 segments); the
    text's neva-clause is «သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်၊» in the pahātabba frame (15 segments: 2-03,
    4-13 …) and «… ဖြင့်လည်း ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်၊» in the pahātabbahetuka frame (20 segments: 2-04, 5-19 …);
    the na-member (nadassanena) closes with «… မဟုတ်သော». No other shape.
34. **Heading number** (g6 6): «saññojanādigocchakāni» «… အစုများ» in most headings, «… အစု» at 5-14 ^7-5-14-6-0 (Pāli
    singular -gocchakaṃ).
35. **niruddhe** (phase-3 scan): «ချုပ်ငြိမ်းသောအခါ» (1-01, 2-05) against «ချုပ်ငြိမ်းသွားသောအခါ» (1-03 … 1-05, 3-01,
    3-09) for the same «kusale / kusalākusale niruddhe».
36. **saññojanādidukāni in headings** (phase-3 scan): 4-17 ^7-4-3-3-12-4-0 «ကုသိုလ် သုံးမျိုးတွဲနှင့် နှောင်ကြိုး
    နှစ်မျိုးတွဲ စသည်» against 5-02 / 5-08 / 5-11 / 5-12 «… နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ».
37. **vibhajantena** (phase-3 scan): the adverbial «ခွဲခြမ်းစိတ်ဖြာလျက်» (3-05 ^7-28-52) against the agent noun
    «ခွဲခြမ်းစိတ်ဖြာသူသည်» (3-10 ^7-U409) for the same note participle.
38. **Two keywords written as one word** (phase-3 fix 1): «dibbena cakkhunā» «နတ်မျက်စိဖြင့်», «dibbāya sotadhātuyā /
    dibbassa sotassa» «နတ်နား …» (the pi-1 … pi-6 «နတ်» is kept for dibba-; §B, boundary exception).

## B. Book-wide consistency scan (75 *.mapped.md; model pi-6-my/mapper-my/work/map_scan.py)

`work/map_scan.py` (first letter case-insensitive) — **before** (the phase-2 files, `work/phase2-mapped/`): 2,315
keywords, **98 with more than one value**; **after** phase 3: 2,315 keywords, **88 with more than one value**
(179,791 uses). A second scan by term family (`work/p3_family_scan.py`: R1 base form and case stem, fix 8 «one value
per term») found 64 families with an odd member before the alignment and 63 after; all of them are the condition
cases of T1–T4 (name / ablative / bare by frame), the term against the plain noun (dukkhāya «နာကျင်သော»), false
families of two lemmas (uppādī / uppādeti, noupādāna / noupādā), or the keywords below. Every keyword with more than
one value was checked by hand against the Pāli and the Burmese (`work/p3_kw.py`, `work/scan-class.tsv`).

### Aligned (11 keywords dropped out of the scan; 2 more made one value per term; phase3-changes.tsv)

- **cakkaṃ** «စက်» → «စက်ဝိုင်း» (fix 1; the text's «(စက်ဝိုင်း)», module STOCK).
- **saññojano, saññojanaṃ, yogaṃ, kilesañceva** «N ဖြစ်သော / N … ဖြစ်သော» → «N» (coordinator: the gocchaka item is the
  bare noun book-wide; module cluster_cands), with **Upādānañca** (R1 order, fix 5).
- **nahetuṃ** «…ကြောင့် မဟုတ် / … မဟုတ်ခြင်း» → «အမြစ် မဟုတ်သော» («Nahetuṃ (X) dhammaṃ» is the dyad term; g3 override
  moved into cond_cands).
- **naviññeyyo / naviññeyyaṃ** «သိနိုင်သည် မဟုတ်သော» → «မသိနိုင်သော» (coordinator; f_navinn: only where the text has it).
- **paripuṇṇā** «ပြည့်စုံသည်» → «ပြည့်စုံသော» and **paripuṇṇaṃ** «ပြည့်စုံ» → «ပြည့်စုံစွာ» (fix 9; the adverb where the text
  has only that).
- **pañcaviññāṇaṃ** «သိစိတ်» → «သိစိတ် ငါးပါး» (fix 3 / fix 9).
- **suddhake** «ရိုးရိုး အပိုင်း» → «ရိုးရိုး» (one value per term; the text's «အပိုင်း» is its addition, A5).
- **suciṇṇāni** (still two values, the two text forms): g1's «ကောင်းစွာ ပြုခဲ့ဖူးသည်» → g2's «ကောင်းစွာ ပြုခဲ့ဖူးသော» (rule 3).
- **sekkhāya** «ကျင့်ကြံဆဲသူ» → «…၏» (the qualifier of phalasamāpatti, coordinator's sekkha decision; f_sekkha), and
  **arūpāvacare** «ရုပ်မရှိသော ဘုံ» → «ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော» and **vipākassa** (^7-2-423, after «kammaṃ») «ကံ၏
  အကျိုး ဖြစ်သော» → «ကံ၏ အကျိုး» (family scan).
- New in the scan: **sahajātaṃ** (^7-U409 «"sahajātaṃ kāmupādāna"nti» «“အတူ ပေါ်ပေါက်သော ကာမ စွဲလမ်းမှု”»): the
  adjective, by fix 1 (the old value stood only inside «…ခြင်းအလိုက်»); kept as grammar.

### Kept (88 keywords: real sense, grammar, construction or text differences)

Kinds: grammar 36 (36 of them the condition by its frame, T1–T4), construction 27 (the « … » gap of R7 at the «လည်း» of
ca / ceva, and U2), sense 9, text shape 8 (the -sadisa shapes, coordinator), text 6 + text / grammar 1 (§A items),
grammar / sense 1 (natthi).

| keyword | values (uses) | kind | why kept |
|---|---|---|---|
| adhipati | အကြီးအမှူး (75) / အကြီးအမှူးဟူသော အကြောင်း (2) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| adhipatipaccayā | အကြီးအမှူးဟူသော အကြောင်းကြောင့် (237) / အကြီးအမှူးဟူသော အကြောင်း (11) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| anantara | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း (16) / ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း (13) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| anantarapaccayā | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် (148) / ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း (6) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| anulomaṃ | အဟုတ်ပြ ပုံစံ (535) / လျော်ညီခြင်း စိတ် (29) | sense | the order «အဟုတ်ပြ ပုံစံ» or the mind moment «လျော်ညီခြင်း စိတ်» (phase 1 §B, harmonise H1) |
| arūpadukasadisā | ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူအောင် (2) / ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူသည် (1) | text shape | -sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator) |
| assādeti | သာယာ (415) / သာယာသည် (28) | construction | U1: the bare «သာယာ» where the text joins «သာယာ နှစ်သက်သည်» with one ending, «သာယာသည်» where it has that |
| atthi | ရှိခြင်း (129) / ရှိသည် (2) / ရှိခြင်းဟူသော အကြောင်း (1) | grammar | the condition (T4), the verb «ရှိသည်» of a note (g2 CTX ^7-10-112), the name in a heading |
| avigatapaccayā | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် (228) / မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း (4) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| aññamañña | အချင်းချင်း ထောက်ပံ့ခြင်း (92) / အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း (2) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| cittadukakusalasadisaṃ | စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည် (1) / စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူအောင် (1) | text shape | -sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator) |
| dukkhaṃ | နာကျင်မှု (26) / ဆင်းရဲ (1) | sense | bodily pain «နာကျင်မှု» / suffering «ဆင်းရဲ» («pariyiṭṭhimūlakaṃ dukkhaṃ», g2 CTX ^7-11-54) |
| dutiyagamanasadisaṃ | ဒုတိယ သွားပုံနှင့် တူသည် (3) / ဒုတိယ သွားပုံနှင့် တူအောင် (1) | text shape | -sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator) |
| ekāgārikaṃ | အိမ်တစ်လုံးတည်း (5) / အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည် (4) | construction | U2: the whole act «… ဝိုင်း၍ တိုက်သည်», the bare noun where …pe… cuts the verb off |
| ganthaniyo | အထုံး၏ အာရုံ ဖြစ်နိုင်သော (3) / အထုံး၏ အာရုံ … ဖြစ်နိုင်သော (2) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| ganthasampayutto | အထုံးနှင့် ယှဉ်တွဲသော (37) / အထုံးနှင့် … ယှဉ်တွဲသော (5) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| gāmaghātaṃ | ရွာကို ဖျက်ဆီး၍ လုယက်သည် (5) / ရွာ (3) | construction | U2 (coordinator): the whole act, the bare «ရွာ» before …pe… |
| hetudukaṃ | အမြစ် နှစ်မျိုးတွဲ (199) / အမြစ်ဟူသော အကြောင်း၏ နှစ်မျိုးတွဲ (80) | sense | the condition dyad «အမြစ်ဟူသော အကြောင်း၏ နှစ်မျိုးတွဲ» (counting headings of parts 1-4) / the gocchaka dyad «အမြစ် နှစ်မျိုးတွဲ» (3-01, parts 4-5) |
| hetupaccayā | အမြစ်ဟူသော အကြောင်းကြောင့် (7098) / အမြစ်ဟူသော အကြောင်း (10) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| indriya | စွမ်းရည် (72) / စွမ်းရည်ဟူသော အကြောင်း (3) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| jhāna | ဈာန်ဟူသော အကြောင်း (2) / ဈာန် (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| kamma | ကံ (20) / ကံဟူသော အကြောင်း (5) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| kammapaccayā | ကံဟူသော အကြောင်းကြောင့် (116) / ကံဟူသော အကြောင်း (3) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| katvā | ပြု၍ (139) / (no direct equivalent) (65) | construction | U2: (no direct equivalent) after an act compound, «ပြု၍» elsewhere (f_karoti) |
| kilesasampayutto | ကိလေသာနှင့် ယှဉ်တွဲသော (2) / ကိလေသာနှင့် … ယှဉ်တွဲသော (1) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| kātabbā | ပြုရမည့် (214) / ထည့်ရမည့် (2) | sense | «ပြုရမည့်» (do) / «ထည့်ရမည့်» (include: «paṭisandhi kātabbā», 1-03) (phase 1 §A 8) |
| lokiyadukaabyākatasadisaṃ | လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည် (5) / လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူအောင် (1) | text shape | -sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator) |
| naadhipati | အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း (2) / အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ် (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| naadhipatipaccayā | အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ် (328) / အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း (21) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| naanantara | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း (4) / ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် (2) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| naindriya | စွမ်းရည်ဟူသော အကြောင်းကြောင့် မဟုတ် (2) / စွမ်းရည်ဟူသော အကြောင်း မဟုတ်ခြင်း (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| namagga | မဂ်ဟူသော အကြောင်း မဟုတ်ခြင်း (1) / မဂ်ဟူသော အကြောင်းကြောင့် မဟုတ် (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| napacchājāta | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း (14) / နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် (2) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| natthi | မရှိ (38) / မရှိသည် (20) / မရှိခြင်း (16) / မရှိခြင်းဟူသော အကြောင်း (6) | grammar / sense | the condition «မရှိခြင်း» in a ghaṭanā list, the name «… ဟူသော အကြောင်း» as a heading part (T4), the verb «မရှိသည်» / «မရှိ» (module f_natthi, coordinator) |
| natthipaccayā | မရှိခြင်းဟူသော အကြောင်းကြောင့် (82) / မရှိခြင်းဟူသော အကြောင်း (3) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| naārammaṇapaccayā | အာရုံဟူသော အကြောင်းကြောင့် မဟုတ် (184) / အာရုံဟူသော အကြောင်း မဟုတ်ခြင်း (34) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| nevavipākanavipākadhammadhammo | ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား (463) / ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော (64) | grammar | rule 5: «… သဘောတရား» where the keyword's own -dhammo is the noun; the qualifier alone where a separate dhammo keyword follows (tikaduka «X nahetu dhammo») |
| niruddhe | ချုပ်ငြိမ်းသွားသော (30) / ချုပ်ငြိမ်းသော (3) | text | the text has «ချုပ်ငြိမ်းသောအခါ» (1-01, 2-05) and «ချုပ်ငြိမ်းသွားသောအခါ» (1-03 … 3-09); §A |
| nissaya | အမှီ (115) / အမှီဟူသော အကြောင်း (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| nīvaraṇasampayuttañca | အတားအဆီးနှင့် ယှဉ်တွဲသော (3) / အတားအဆီးနှင့် … ယှဉ်တွဲသော (1) | construction | R7 «လည်း» gap |
| nīvaraṇasampayutto | အတားအဆီးနှင့် ယှဉ်တွဲသော (27) / အတားအဆီးနှင့် … ယှဉ်တွဲသော (2) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| nīvaraṇiyañca | အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော (2) / အတားအဆီး၏ အာရုံ … ဖြစ်နိုင်သော (2) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| nīvaraṇiyo | အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော (13) / အတားအဆီး၏ အာရုံ … ဖြစ်နိုင်သော (1) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| pacchājāta | နောက်မှ ဖြစ်ပေါ်ခြင်း (7) / နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| pahātabbahetukādhipati | ပယ်ရမည့် အမြစ် ရှိသည် … အကြီးအမှူး (2) / ပယ်ရမည့် အမြစ် ရှိသော အကြီးအမှူး (2) | construction | rule 10: «ပယ်ရမည့် အမြစ် ရှိသည် … အကြီးအမှူး» where nadassanena's negative stands inside (g4) |
| paripuṇṇaṃ | ပြည့်စုံသော (36) / ပြည့်စုံစွာ (4) | grammar | fix 9 «ပြည့်စုံသော»; the text's adverb «ပြည့်စုံစွာ» where it has only that («(paripuṇṇaṃ nava)» «(ပြည့်စုံစွာ ကိုးခု)») |
| parāmaṭṭho | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (13) / မှားယွင်းသော ယူဆမှု၏ အာရုံ … ဖြစ်နိုင်သော (2) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| pavattipaṭisandhi | ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ (10) / ဘဝ ဖြစ်ဆဲ ကာလ … ပဋိသန္ဓေ (2) | text | two text forms «ဘဝ ဖြစ်စဉ်» / «ဘဝ ဖြစ်ဆဲ ကာလ» (§A) |
| paṭiccavārasadisaṃ | မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည် (386) / မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် (93) | text shape | -sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator) |
| paṭiccavārasadiso | မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည် (193) / မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် (5) | text shape | -sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator) |
| paṭiccavārasadisā | မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် (360) / မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည် (139) | text shape | -sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator) |
| purejātapaccayā | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် (130) / ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း (2) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| rūpaṃ | ရုပ် (3079) / အဆင်းအရောင် (57) | sense | matter «ရုပ်» or the visible object «အဆင်းအရောင်» (f_rupam, phase 1 §B) |
| sahajāta | အတူ ပေါ်ပေါက်ခြင်း (119) / အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း (1) / အတူ ပေါ်ပေါက်သော (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| sahajātapaccayā | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းကြောင့် (151) / အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း (5) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| sahajātaṃ | အတူ ပေါ်ပေါက်ခြင်း (241) / အတူ ပေါ်ပေါက်သော (1) | grammar | the kind of a condition «အတူ ပေါ်ပေါက်ခြင်း» in a list, the adjective «အတူ ပေါ်ပေါက်သော» in «sahajātaṃ kāmupādānanti» (^7-U409) |
| sahetukassa | အမြစ် ရှိသော (17) / အမြစ် … ရှိသော (1) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| sahetukañca | အမြစ် ရှိသော (4) / အမြစ် … ရှိသော (1) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| sahetuko | အမြစ် ရှိသော (231) / အမြစ် … ရှိသော (27) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| samanantarapaccayā | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် (115) / ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း (3) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| sappītikadukasadisaṃ | ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည် (6) / ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူအောင် (1) | text shape | -sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator) |
| saññojanasampayutto | နှောင်ကြိုးနှင့် ယှဉ်တွဲသော (59) / နှောင်ကြိုးနှင့် … ယှဉ်တွဲသော (3) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| saññojaniyañca | နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော (3) / နှောင်ကြိုး၏ အာရုံ … ဖြစ်နိုင်သော (1) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| saññojaniyo | နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော (22) / နှောင်ကြိုး၏ အာရုံ … ဖြစ်နိုင်သော (3) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| saññojanādidukāni | နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲ (6) / နှောင်ကြိုး နှစ်မျိုးတွဲ စသည် (1) | text | the headings differ: 4-17 «နှောင်ကြိုး နှစ်မျိုးတွဲ စသည်», 5-xx «နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ» (§A) |
| saṃkilesiko | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (20) / ကိလေသာ၏ အာရုံ … ဖြစ်နိုင်သော (8) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| saṃkiliṭṭhañca | ကိလေသာဖြင့် ညစ်နွမ်းသော (9) / ကိလေသာဖြင့် … ညစ်နွမ်းသော (1) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| saṃkiliṭṭho | ကိလေသာဖြင့် ညစ်နွမ်းသော (58) / ကိလေသာဖြင့် … ညစ်နွမ်းသော (7) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| suciṇṇāni | ကောင်းစွာ ကျင့်ခဲ့ဖူးသော (78) / ကောင်းစွာ ပြုခဲ့ဖူးသော (14) | text | two text forms «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော» / «ကောင်းစွာ ပြုခဲ့ဖူးသော» (§A) |
| sāsavañca | စိတ်အစွန်းအထင်း၏ အာရုံ … ဖြစ်နိုင်သော (4) / စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော (2) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| sāsavo | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော (60) / စိတ်အစွန်းအထင်း၏ အာရုံ … ဖြစ်နိုင်သော (6) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| tadārammaṇatā | ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ် (25) / ထိုအာရုံကို အာရုံပြုသည့် အနေ (3) | text | fix 3: one value per text form (1-01 / 2-05 «… အာရုံပြုသည့် အနေ», 1-03 … «… အာရုံပြုသော အဖြစ်»); §A |
| upanissaya | အားကြီးသော အမှီ (26) / အားကြီးသော အမှီဟူသော အကြောင်း (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| upanissayapaccayā | အားကြီးသော အမှီဟူသော အကြောင်းကြောင့် (160) / အားကြီးသော အမှီဟူသော အကြောင်း (12) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| uposathakammaṃ | ဥပုသ်ကို စောင့်ထိန်းသည် (264) / ဥပုသ် စောင့်ထိန်းခြင်း (58) / ဥပုသ် (6) | construction | U2 (coordinator, g2): the whole act; the text's noun «ဥပုသ် စောင့်ထိန်းခြင်း» before …pe…; the bare «ဥပုသ်» where the text has only that |
| vibhajantena | ခွဲခြမ်းစိတ်ဖြာလျက် (1) / ခွဲခြမ်းစိတ်ဖြာသူ (1) | text / grammar | the text has the adverbial «ခွဲခြမ်းစိတ်ဖြာလျက်» (3-05) and the agent noun «ခွဲခြမ်းစိတ်ဖြာသူသည်» (3-10); each segment's form (§A) |
| vigatapaccayā | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် (54) / ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း (2) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| vipāka | ကံ၏ အကျိုး (6) / ကံ၏ အကျိုးဟူသော အကြောင်း (1) | grammar | T4: the bare name in a ghaṭanā list, the name «… ဟူသော အကြောင်း» in a heading |
| vipākassa | ကံ၏ အကျိုး (4) / ကံ၏ အကျိုး ဖြစ်သော (4) | sense | the noun «ကံ၏ အကျိုး» after «kammaṃ» (f_vipakassa), the triad adjective before dhammassa |
| vipākaṃ | ကံ၏ အကျိုး ဖြစ်သော (67) / ကံ၏ အကျိုး (3) | sense | the triad adjective / the noun (phase 1 §B) |
| vipāke | ကံ၏ အကျိုးဟူသော အကြောင်း (20) / ကံ၏ အကျိုး (3) / ကံ၏ အကျိုး ဖြစ်သော (1) | sense | the counting locative (condition), the noun, the adjective of «vipāke … khandhe» (g4 CTX) |
| vipāko | ကံ၏ အကျိုး ဖြစ်သော (68) / ကံ၏ အကျိုး (1) | sense | the adjective / the noun of «vipāko natthi» «ကံ၏ အကျိုး မရှိ» |
| ārammaṇa | အာရုံ (15) / အာရုံဟူသော အကြောင်း (6) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| ārammaṇapaccayā | အာရုံဟူသော အကြောင်းကြောင့် (563) / အာရုံဟူသော အကြောင်း (79) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| āsavasampayuttaṃ | စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော (6) / စိတ်အစွန်းအထင်းနှင့် … ယှဉ်တွဲသော (2) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| āsavasampayutto | စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော (28) / စိတ်အစွန်းအထင်းနှင့် … ယှဉ်တွဲသော (9) | construction | R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value |
| āsevanapaccayā | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့် (107) / အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း (1) | grammar | T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound) |
| ṭhānāṭhānakosallassa | ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း (7) / ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု (5) | text | two text forms (§A) |

Boundary exceptions of fix 1 (logged): dibbena / dibbaṃ / dibbassa / dibbāya keep «နတ်» where the text writes
«နတ်မျက်စိ / နတ်နား» as one word for two keywords (STOCK; the presence check of a book table value is the verifier's,
not the boundary test); the -sadisa / arūpamissake values that keep «သဘောတရား» inside (§A 6).

## C. S1 review (stem fallback)

`work/p3_s1.py` lists every use whose final value comes from the stem fallback, with the phase-2 value at the same
place (`work/p3_s1_after.tsv`, with the Pāli and Burmese context): **292 uses in 30 keyword / value pairs, none
changed in phase 3**, so none needed a new check (the brief: re-check only the values that changed). They are the kept
lists of the groups (g1 13, g2 25, g3 112, g4 72, g5 56, g6 14), each checked by eye in phase 2: **kept 292, corrected
0** in phase 3. The phase-2 corrections (g3: suddhake, assādanā, paccavekkhitvā; g4: paccavekkhitvā) and g4's kept
suddhake are now table values (BOOK / g3 table), so they are no longer stem uses. Pairs: passati «မြင်သည်» 69, gaṇitaṃ
«ရေတွက်ထားသော» 50, rūpī / Rūpī / rūpissa / rūpiṃ / Rūpiṃ «ရုပ် ဖြစ်သော» 89, itare / Itare «အခြား» 19, vibhajitabbaṃ /
-āni / -o «ခွဲခြမ်းစိတ်ဖြာရမည့်» 17, ninnānākaraṇā «ကွဲပြားချက် မရှိ» 13, Cittasaṃsaṭṭhasamuṭṭhānañca / -ṃ «စိတ်နှင့်
ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော» 11, ganthasampayuttakā 6, bhinditvā 4, uppādetvā 2, patthayamāno 2, pisuṇavācā,
pharusavācā, ādiyitvā, sajjhāyamaggo, gaṇanāni, Gaṇanāya, samenti, lokuttarasa, ekekampi, uppajanti 1 each.

## D. Module consolidation (task 1)

Staged runs (each runs map_sample → map_g1 … map_g6 and diffs all 75 files with the previous stage;
`work/p3_stage.py`, `work/stages/order.txt`); the values each stage changed (214 in all, `phase3-changes.tsv`):

| stage | change | values |
|---|---|---|
| s1-bound | fix 1 word boundaries (`occurs`, `bounded_at` in phrase_present / contiguous / the terms check / pick); STOCK dibba «နတ်» (exception) and cakkaṃ «စက်ဝိုင်း»; the hyphen vāra-name part (`vara_part`: paccaya «အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း», saṃsaṭṭha «ရောနှောခြင်း») | 58 |
| s2-gen | fix 3: `_GEN_RX` skips a concatenated generator string; STOCK tadārammaṇatā (two text forms) | 8 |
| s3-r1 | fix 5: `_chain` tries each step for the keyword and its R1 base forms before the next step; `_rest` without the term family, which is its own later step | 2 |
| s4-neg | fix 4 noupādā (STOCK), fix 6 (plain na-X candidates first) | 0 |
| s5-num | fix 7 «bīsa(ti)» | 0 |
| s6-item | the gocchaka item is the bare «N» (cluster_cands) | 47 |
| s7-natthi | f_natthi: the T4 hyphen part (g1 f_g1_natthi), the in-term mask (g4 G3; coordinator); g2 f_natthi_g2 and g4 f_natthi_g4 dropped | 11 |
| s8-book | BOOK (fix 2, fix 8, fix 9, the decided points, the agreed overrides, the group values that recur), f_sekkha, f_navinn, the term guard in cond_cands (Nahetuṃ), STOCK uposathakammaṃ | 68 |
| s9-strip | the group-table entries the module now holds removed from map_g1 … map_g6 (146 table lines), g3 item table, g4 DLS table, g6 f_r1, the CTX entries g1 sekkhā / g4 bhāgo / g6 kusale | 7 |
| s10-head | the head-noun rule in the group tables (g4, g6) | 8 |
| s11-scan | scan alignments: BOOK suddhake, arūpāvacare, f_vipakassa, f_sekkha for sekkhāya / asekkhāya | 5 |
| s12 … s14 | re-runs (0 changes; s13 / s14 byte-identical) | 0 |

Values changed by reason: word boundaries 13 (paripanthe 9, cakkaṃ 3, sahajātaṃ 1) and the vāra-name part 45;
generator reading (tadārammaṇatā 1, pañcaviññāṇaṃ 7) 8; R1 order 2; gocchaka items 47; natthi 11; uposathakammaṃ 46;
Nahetuṃ as the term 16; paripuṇṇa- (fix 9) 4; naviññeyyo 3; suciṇṇāni 6; head-noun rule 8; scan alignments 5. Fixes 2,
4, 6, 7, 8 (asekkhassa …) and the other dictionary forms of fix 9 changed no value: the group tables had the same
values; the module now makes them.

Not found: the brief's «5 uses of tadārammaṇatā in the sample 1-02» — 1-02 has no tadārammaṇatā keyword; the only
module «စိတ်သည်» left was 2-05 ^7-11-46 (now the 1-01 form, which the text has there).

Verification (task 4, `work/p3_verify_all.txt`): 75 files, 15,312 lines, 179,791 keywords; preservation `bad []` in
every file; presence failures 0 (3,039 chunks matched by the approved ending rules: attr-fut 1,524, verb 808, attr 706,
neg-verb 1; no other exception); «, » / «၊» / « / » in a value 0; (no direct equivalent) 156. Two further runs of all
seven scripts on the final code (stages s13, s14) gave byte-identical files (`work/p3_md5_run3.txt` =
`work/p3_md5_run4.txt`).

Assembly (task 5): `mapper_chunks.py assemble` wrote
`AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md`: 15,312 lines, every ID once and in the
keyword file's order, 179,791 keywords (unchanged per line).

## E. Keyword ambiguities (phase 1 §B, as settled)

- The counting locatives are homographs of plain nouns (kamme, magge, jhāne, āhāre, indriye, vipāke, ārammaṇe): the
  condition «Nဟူသော အကြောင်း» where the segment has it, else the plain noun.
- natthi: «မရှိခြင်း» in a ghaṭanā list; the name as a heading part (T4); the verb «မရှိသည်» / «မရှိ» (§D s7).
- Hyphen-compound parts take the case of the whole compound (T4); a part of a hyphen vāra name is the vāra member.
- anulomaṃ: the order or the mind moment; rūpaṃ: matter or the visible object; taṃ: «ထိုအရာ» / «ထို»; katvā / karoti:
  «ပြု၍» or (no direct equivalent) after an act compound; evaṃ: «ထိုနည်းတူ» / «ဤသို့»; vipāka-: the adjective, the noun
  («kammaṃ vipākassa»), or the condition.
- sekkha / asekkha: the qualifier «…၏» before dhamma / khandha (up to three words later) and phalasamāpatti, else the
  person noun (f_sekkha).

## F. Unclear points: how they were settled, and what is left

Settled by the coordinator (2026-11-26) and applied in phase 3: the group rules book-wide; the module fixes 1–9; the
gocchaka item «N»; the head-noun gap rule; the -sadisa shapes; nevadassanena one form; naviññeyyo «မသိနိုင်သော»; the
locative absolutes; ṭhitena «တည်၍», gambhīrā «နက်နဲ»; U2 act compounds; natthi; the g2 decisions (sekkha, kāraṇena,
uposathakammaṃ, G2-3, gahite, dassitanayena). g2's G2-1 (natthi in a note) is replaced by the module rule; the
G2-4 / G2-5 values stay as group values.

Left for review:
1. **The vāra-name part** (new in phase 3, s1): paccaya / saṃsaṭṭha inside «Sahajāta-paccaya-nissaya-saṃsaṭṭha-
   sampayuttavāro» take the vāra member «အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း» / «ရောနှောခြင်း» (45 uses), the text's heading words.
2. **The dibba boundary exception**: dibba- keeps «နတ်» inside «နတ်မျက်စိ / နတ်နား»; the alternative is the whole written
   word, which would repeat cakkhunā's / sota-'s word.
3. **natthi by the ending rule**: «… မရှိ။» gives «မရှိသည်» (the module's ending rule) and «(… မရှိ)» gives «မရှိ»; the
   alternative is «မရှိ» for every clause-final note.
4. **sekkha qualifier test**: Pāli dhamma / khandha up to three words after the keyword, or phalasamāpatti; the person
   noun elsewhere (sekkhā maggā vuṭṭhahitvā, sekkhā phalaṃ garuṃ katvā).
5. **vibhajantena** keeps the text's two forms (§A 37); the alternative is one form (the agent noun of pi-4 P6, or the
   adverbial of FRAME anumajjantena).
