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

