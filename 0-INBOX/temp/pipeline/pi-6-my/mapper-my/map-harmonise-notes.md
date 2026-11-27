# pi-6 Burmese keyword mapping: text inconsistencies, consistency scan, S1 review (phases 1–3)

Phase 1 (preamble, 1-mulayamaka, 2-01-khandhayamaka) wrote the first version of this file (kept as
`work/map-harmonise-notes-phase1.md`); phase 2 (groups G1 / G2 / G3) wrote `notes-g1.md`, `notes-g2.md`, `notes-g3.md`;
phase 3 (2026-11-22, whole book) wrote this version. The translation was not changed. Burmese only from this track's
FINAL pi-6 text, `my6-zeroshot-terms.md` and the final pi-1 … pi-5 mappings; pi-1-my … pi-5-my were only read.

Phase-3 files: `phase3-changes.tsv` (every value that differs from the phase-2 files, with its reason), the staged runs
`work/stages/<stage>/` (+ `work/p3_diff_<stage>.tsv`, `work/stages/order.txt`), the phase-2 snapshot
`work/phase2-mapped/` (md5 = `work/before-phase3-files-md5.txt`) and `work/phase2-scripts/`, the scans
`work/scan-before.tsv` / `work/scan-mid.tsv` (+ `-detail.txt`, `work/scan-class.tsv`), the S1 list
`work/p3_s1_before.tsv` / `work/p3_s1_after.tsv`, the verification `work/p3_verify_all.txt`, `work/p3_md5_run1.txt` /
`work/p3_md5_run2.txt`. Helpers: `work/p3_stage.py`, `work/p3_changes.py`, `work/p3_s1.py`, `work/map_scan.py`,
`work/p3_scan_classify.py`, `work/p3_verify_all.py` (map_scan / scan_classify copied from pi-5-my, not edited there).

## A. Text inconsistencies for the rails step (merged: phase 1 A1–A6, notes-g1 T1–T4, notes-g2 T1–T5, notes-g3 T1–T6, the coordinator's phase-3 decisions)

1. **«yassa cittassa anantarā» has two Burmese forms** (phase 1 A1, g3 T6): «အကြင်စိတ်၏ ချက်ချင်း နောက်၌»
   (correlative: 5-01 … 5-03, 9-01 … 9-03, 10-09 … 10-11; 166 places) and «မိမိ စိတ်၏ ချက်ချင်း နောက်၌» ("one's own
   citta": 6-01, 6-02, 10-05 … 10-07, 10-12; 92 places). Same Pāli, same frame; no keyword is affected (cittassa
   «စိတ်», anantarā «ချက်ချင်း နောက်»). The rails step should choose one.
2. **kāmāvacarānaṃ: the beings or the adjective of pacchimacitta** (phase 1 A2, g2 T1): «anantarā kāmāvacarānaṃ
   pacchimacittaṃ» = «ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်» (6-01 ^6-6-39, ^6-6-47; 6-02 ^6-6-88, ^6-6-91, ^6-6-140 …)
   while the same genitive plural elsewhere, also in the same segment («Kāmāvacarānaṃ pacchimacittassa uppādakkhaṇe»
   «ကာမဘုံ၌ ရှိသူတို့၊ နောက်ဆုံး စိတ်၏ …»), is the beings. Grammatically the Pāli is «the last citta of the kāma beings».
   The mapping follows the text (module f_plane_adj: the keyword's first occurrence decides).
3. **Colophons of the vāras** (phase 1 A3): «Uddesavāro / Niddesavāro niṭṭhito» = «“အကျဉ်း / အကျယ် ဖော်ပြချက်”
   ပြီးဆုံးပြီ» (no «…အလိုက်», no word for vāro), while the headings «Mūlavāro» etc. are «Xအလိုက် ဖော်ပြချက်».
   Consistent with my6-zeroshot-terms §2; noted because vāro has no word of its own there.
4. **Heading IDs out of text order in the keyword files** (phase 1 A4): e.g. ^6-2-18-0 «Pavatti 2. nirodhavāro»
   after ^6-2-18. No effect (each segment is looked up by its ID; the assembly follows the keyword file's order).
5. **Keyword gaps** (phase 1 A5, g2 T5): ^6-2-79 / ^6-2-81 key «pañcavokārā / pañcavokāraṃ» but not the first member
   «Catuvokārā / catuvokāraṃ» of «Catuvokārā pañcavokārā cavantānaṃ»; the heading «Uppajjamāna-nanirodhavāro» is keyed
   as two parts «Uppajjamāna, nanirodhavāro» in four headings but as one «Uppajjamānananirodhavāro» in ^6-8-10-7-0;
   «Yassa cittake … yaṃ cittake … yassa yaṃ cittake» (^6-8-113) has one keyword «cittake» for three cited sections; the
   second kāmāvacarānaṃ of ^6-6-88 has no keyword of its own.
6. **Pāli slips of the source** (phase 1 A6, g1 T1 / G11, g2 T4, g3 T1; the Burmese renders the intended word in each,
   and the mapping gives the intended word's value): ^6-2-36 «.» for «?», ^6-2-61 «(Ka)» for «(Kha)», ^6-2-111
   nirujjhattha, ^6-1-99 «nāmahetū ti», ^6-2-44 split line; vadanākkhandho (^6-2-185), sotāyananti (^6-3-13),
   **uppajjittharūpāyatanañca** (^6-3-43, two words run together; g1 U4 decided: mapped as g1 chose, «အဆင်းအရောင်
   အာရုံခံ နယ်ပယ် … ဖြစ်ပေါ်ခဲ့သည်», and a rails item), parinibbāntānaṃ (^6-3-172), manāyatana…pe… (^6-3-186),
   upapajjissati for uppajjissati (^6-3-212, ^6-10-309), nirujjhatī ti (3-04 ^6-3-131), asaññattā (^6-5-76), nirujjhiti
   (5-02), aggamaggaṃ paṭilabhissānti (5-01), kāmārāgānusayo (^6-7-21), Pajahanāvāre (^6-7-197), paccanīkaokāsā
   (^6-6-16-5-0), Dhātuvisajjavāro (^6-7-349), uppajjantānaṃ for upapajjantānaṃ (^6-10-398), uppajjantīnaṃ for
   upapajjantīnaṃ (^6-10-206), anaññātaññāssāmīti (^6-10-3), Ghānandriyamūlakaṃ (^6-10-336), cavantāna (^6-10-361),
   Pacchimacittasamaṅgīna (^6-10-314).
7. **Heading layout** (g2 T4, g3 T5): the heading «4 (Ṅa) paccanīkaokāso» stands in the body of ^6-6-65 and
   «(14) Atikkantakālavāro» in the body of ^6-8-82; «#### 3 Suddhadhammavāro» / «#### 4 Suddhadhammamūlacakkavāro»
   (^6-9-4-0, ^6-9-5-0) carry a source digit without a dot, so the heading parts do not split as elsewhere (mapped by
   the module table BOOK).
8. **aggamagga / aggaphala** (g1 T2): 5-03 ^6-5-159 / ^6-5-162 have both «arūpe aggamaggassa ca phalassa ca
   uppādakkhaṇe» and «arūpe aggaphalassa uppādakkhaṇe»; the text keeps them apart («အမြတ်ဆုံး မဂ်နှင့် ဖိုလ်» /
   «အမြတ်ဆုံး ဖိုလ်»), correct; noted because the keyword list has aggaphalassa and Aggamaggassa / phalassa together.
9. **sadisaṃ two constructions** (g1 T3): the notes render «sadisaṃ» as «တူညီသည်» but «sadisaṃ kātabbaṃ» as «တူညီအောင်
   ပြုရမည်» (5-01 ^6-5-70, 4 ^6-4-18, 3-05 ^6-3-201); the mapping takes each segment's form (f_aka).
10. **sotaṃ in the āyatana niddesa** (g1 T4): «Dibbasotaṃ taṇhāsotaṃ sotaṃ», the predicate sotaṃ is «“သောတ” (နား
    သို့မဟုတ် ရေစီး)» while sotaṃ elsewhere in the segment is «နား»; one sense per segment «နား» («ရေစီး» is taṇhāsotaṃ's).
11. **uppāda** (g2 T2): the vāra headings and colophons «ဖြစ်ပေါ်ခြင်း(အလိုက်)», the moment «ဖြစ်ခြင်း ခဏ» (zero-shot
    exception 2); Uppajjanavāro (7-10) and Uppādavāro are both «ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်»; Pahīnavāro «ပယ်ပြီး
    ဖြစ်ခြင်းအလိုက်».
12. **kāyasaṅkhāro** (g2 T3): the pi-2 / pi-5 FINAL mappings have «ကိုယ် ပြုပြင်ဖန်တီးမှု», every pi-5 / pi-6 text
    «ကိုယ်၏ ပြုပြင်ဖန်တီးမှု» (mapped «ကိုယ်၏ …», g2 O1).
13. **sacchikaroti spacing** (g3 T2; g3 U4 decided: a rails item): positive joined «မျက်မှောက်ပြု…», negative spaced
    «မျက်မှောက် မပြု…» (as pi-4 ^4-17 and pi-5 §A 10); the pi-5 FINAL mapping has «မျက်မှောက် ပြုသည်». Phase 3 maps the
    joined form everywhere (verifier ending «neg-verb-sp»).
14. **Words the text adds that no keyword carries** (g3 T3 / T4, g2 U3 / U5 / U6, decided by the coordinator: the value
    is the keyword's own meaning, without the translator's addition): the understood dhammānaṃ after kusalānaṃ /
    akusalānaṃ / kusalākusalānaṃ («ကုသိုလ် သဘောတရားတို့၏ ဖြစ်ခြင်း ခဏ၌»; g3 U2: the module value without «သဘောတရား»);
    the head noun «အရာ(များ)» after the bare anaññātaññassāmīti and abyākatā («… ဟူသော အရာ», «… မဟုတ်သော အရာများ»;
    g3 U1 / U3); «အတွဲ» after saraṇaaraṇā («“ပဋိပက္ခ ရှိသော” “ပဋိပက္ခ မရှိသော” အတွဲ»; g2 U3: no «အတွဲ» since the Pāli
    keyword is not a -duka); «ပုဂ္ဂိုလ်» after Aṭṭhamako («အဋ္ဌမ ပုဂ္ဂိုလ်»; g2 U5 «အဋ္ဌမ» as pi-5); the plural / emphatic
    «ထိုသူတို့၏ပင်» of tesaṃyeva (g2 U6 «ထိုသူ»).

## B. Book-wide consistency scan (44 *.mapped.md; model pi-5-my/mapper-my/work/map_scan.py)

`work/map_scan.py` (first letter case-insensitive) — **before** (the phase-2 files, `work/phase2-mapped/`): 1,127
keywords, **15 with more than one value**; **after** phase 3: 1,127 keywords, **12 with more than one value**. A second
scan by R1 family (every «-ti / ca / ceva / yeva» form with its base) adds no other keyword (the families are
uniform). `work/p3_scan_classify.py` lists, for every use of a keyword with more than one value, whether the segment
also has one of the other values as a phrase; every such keyword was then checked by hand against the Pāli and the
Burmese (the minority value is chosen only where the segment's Burmese has that form and not the other, by the
candidate order of the module).

### Aligned (3 keywords, 13 uses; phase3-changes.tsv)

- **uppannaṃ** (8, 5 uses) «ဖြစ်ပေါ်ပြီး» → «ဖြစ်ပေါ်ပြီးသော»: mechanic 5, the ending «Xပြီး မဟုတ်» (g2 U4 decided).
- **sacchikarittha / sacchikaritthāti** (10-13, 4 + 4 uses) «မျက်မှောက် ပြုခဲ့သည်» → «မျက်မှောက်ပြုခဲ့သည်»: the verifier
  ending «neg-verb-sp» (g3 U4 decided); g3 W6 dropped.
- (not a scan keyword, one value before and after) **saraṇaaraṇā** (8, 2 uses) «… အတွဲ» → «ပဋိပက္ခ ရှိသော ပဋိပက္ခ မရှိသော»
  (g2 U3 decided).

### Kept (12 keywords: real sense, grammar or construction differences)

| keyword | values (uses; chapters) | kind | why kept |
|---|---|---|---|
| abhisametāvīnaṃ | ထင်ထင်ရှားရှား သိမြင်ပြီးသူ (12) / …သိမြင်ပြီးသော (8; 5-01, 5-02) | grammar | g1 G10 / P6: the agent noun, its attributive where the text puts the word before another person noun («… သိမြင်ပြီးသော စုတေဆဲသူတို့ / ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့»); each segment's own form |
| anabhisametāvīnaṃ | …မသိမြင်ရသေးသူ (14) / …မသိမြင်ရသေးသော (8) | grammar | as abhisametāvīnaṃ |
| arūpāvacarānaṃ | ရုပ်မရှိသော ဘုံ၌ ရှိသူ (71) / …၌ ရှိသော (4; 6-01, 6-02) | grammar | R5: the beings of a plane, the attributive before another person noun «… ဘုံ၌ ရှိသော အခြားသူတို့» (rule 3) |
| kāmāvacarānaṃ | ကာမဘုံ၌ ရှိသူ (45) / ကာမဘုံ၌ ရှိသော (6) / ကာမဘုံနှင့် ဆိုင်သော (3; 6-01) | grammar / sense | R5 beings and their attributive; the adjective of pacchimacitta is the text's other reading (§A 2, f_plane_adj) |
| rūpāvacarānaṃ | သိမ်မွေ့သော ရုပ်ဘုံ၌ ရှိသူ (68) / …ရုပ်ဘုံ … ရှိသူ (22) / …ရုပ်ဘုံ … ရှိသော (4; 6-01, 6-02) | construction | R5: two coordinated planes share one «…၌ ရှိသူ / ရှိသော» («သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံ၌ ရှိသူတို့»), rule 10 « … »; mechanic 3 keeps the shared ending inside the noun phrase |
| pañcavokārānaṃ | အစုအဝေး ငါးပါး ရှိသော ဘဝ၌ ရှိသော (43) / …၌ ရှိသူ (25) | grammar | R5 / phase 1 B4: the attributive before «အခြားသူ» (Itaresaṃ pañcavokārānaṃ «… ဘဝ၌ ရှိသော အခြားသူတို့»), the agent noun elsewhere |
| itaresaṃ | အခြားသူ (227) / အခြား (2; 10-09) | grammar | the attributive before a noun («အခြား ယောက်ျားတို့»), STOCK tuple |
| pacchimabhavikānaṃ | နောက်ဆုံး ဘဝ ရှိသူ (129) / …ရှိသော (4; 10-09) | grammar | the attributive before «မိန်းမတို့ / ယောက်ျားတို့» (rule 3), STOCK tuple |
| upapajjantānaṃ | ပြန်လည် ဖြစ်ပေါ်ဆဲသူ (314) / ပြန်လည် ဖြစ်ပေါ်ဆဲ (29; 2-01, 2-02, 3-04, 3-06) | grammar | R3 / phase 1 B3: the participle before «နောက်ဆုံး ဘဝ ရှိသူ» without a marker |
| upapajjantīnaṃ | ပြန်လည် ဖြစ်ပေါ်ဆဲ (18) / …ဆဲသူ (4; 10-09, 10-11) | grammar | g3 W3: the attributive before «မိန်းမတို့», the agent noun after a relative («tāsaṃ upapajjantīnaṃ») |
| uppajjissati | ဖြစ်ပေါ်လိမ့်မည် (254) / ဖြစ်ပေါ်မည့် (15; 6-02) | grammar | R2: the future in a relative clause «… ဖြစ်ပေါ်မည့်သူတို့» = the future participle (rule 3); those segments have no «ဖြစ်ပေါ်လိမ့်မည်» |
| rūpadhātuṃ | သိမ်မွေ့သော ရုပ်ဘုံ (18; 7-10, 7-11) / အဆင်းအရောင် ဓာတ် (2; 4) | sense | the plane of the dhātupucchā vs the visible-object element of the eighteen (rule 11); never both in one segment |

## C. S1 review (stem fallback, now approved after this review)

`work/p3_s1.py` lists every use whose final value comes from the stem fallback (`make_stem()`): **442 uses, 54
keyword / value pairs, all in 3-01 … 10-13 (none in the sample chapters)**; none changed in phase 3 (the module's BOOK
gave no stem value a new word: the gapped table value «အတိတ် … အနာဂတ်» was first taken by atītepi / atītānāgatepi as a
stem donor, so gapped table values are no longer stem donors, mechanic of `make_stem()`). They are exactly the «kept»
lists of g1 (66), g2 (264) and g3 (112), each checked by the groups against its segment; phase 3 re-checked every pair
against the segment's Burmese and the keyword's sense (`work/p3_s1_before.tsv`, context column): **kept 442,
corrected 0**. The pairs: anulomampi / paccanīkampi «အဟုတ်ပြ / အငြင်းပြ ပုံစံ», uppādepi / nirodhepi / atītepi /
paccuppannepi / atītānāgatepi (the cited «X၌လည်း»), Apāye «အပါယ်», Avasese «ကြွင်းကျန်သော», the dhātu names of ch. 4 (Kāya- /
Mano- / Rūpa- / sota- / gandha- / rasadhātu(ṃ / ñca) «X ဓာတ်», dhātū «ဓာတ်»), Jivhāpi / jivha «လျှာ», manāyatana (slip),
paññācakkhu «ပညာမျက်စိ», kāma- / rūpa- / arūpadhātuṃ «ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ» (7-10, 7-11),
Aṭṭhamako / aṭṭhamakañca «အဋ္ဌမ» (pi-5 binding, g2 U5), assāsapassāsā (-ānaṃ, -ehi) «ဝင်လေ ထွက်လေ», vitakkavicārehi,
catutthajjhānaṃ / -e «စတုတ္ထ ဈာန်», cittasampayuttakā «စိတ်နှင့် ယှဉ်တွဲသော», vacī- / cittasaṅkhārañca, vacīsaṅkhāraṃ
«နှုတ်၏ / စိတ်၏ ပြုပြင်ဖန်တီးမှု», khaṇaṃ «ခဏ», araṇaṃ «ပဋိပက္ခ မရှိသော», yamakāni «အတွဲလိုက် မေးဖြေခြင်း», itthiyo /
itthīnaṃ / Itthiṃ / Itthiñca «မိန်းမ», purisā / Purisaṃ / Purisañca «ယောက်ျား».

## D. Module consolidation (task 1)

Staged runs (each runs map_sample → map_g1 → map_g2 → map_g3 and diffs all 44 files with the previous stage;
`work/p3_stage.py`, `work/stages/order.txt`):

| stage | change in `map6_rules.py` / the scripts | values changed |
|---|---|---|
| s1-literal | mechanic 1: `pi_get`'s literal tier needs `phrase_ok` (g2 O1) | 0 |
| s2-anti | mechanic 2: `base_forms` skips a finite «-anti / -enti / -onti» (`_finite`, g1 override 4, g3 O8) | 0 |
| s3-shared | mechanic 3: `shared_being` only across ONE other plane «Pနှင့် Q၌ ရှိသူ» (g2 O2, ^6-6-47) | 0 |
| s4-amano | mechanic 4: -amāno = person, «…ဆဲသူ» first (g2 O3) | 0 |
| s5-endings | mechanic 5: ending «Xပြီး မဟုတ်» (perf-neg) in `chunk_present` / `phrase_present`; ending «neg-verb-sp» (g3 U4); uppannaṃ one value; f_sacchi (W6) dropped | 13 |
| s6a-rupam | f_rupam = g1's f_rupam_g1, book-wide | 0 |
| s6b-book | BOOK table + `book_auto()` (f_vara, f_aka, f_citta, f_saka, f_fem), f_nayatana, f_plane_adj, title_value() for cited titles in any case; group scripts CTX only; gapped values no stem donors; g2 U3 | 2 |
| s7-final | upapajjamāno's table entry removed (mechanic 4 does it); docstrings | 0 |

- **What moved into the module** (section «BOOK», after the alt values): g1 T_ALL / FUNCS_G1 (f_rupam_g1 → f_rupam,
  f_aka, f_saka, f_citta, f_nayatana; G1-G10), g2 T6 / T7 / T8 / f_plane_adj / f_vara (V1-V7, O1-O9), g3 T_ALL /
  FUNCS_G3 (f_citta merged with g1's: members taṇhā, magga, kusala, akusala, saddhā, somanassa, upekkhā, ñāṇa with
  sampayutta / vippayutta, heads citta / pacchimacitta / pacchimacittasamaṅgī; f_saka with rūpak / cittak; f_fem;
  f_vara with bhāvanā; W1-W5, W7). Lookup order: CTX → chapter table → BOOK → book_auto() → FRAME → STOCK → … (as the
  group tables before). The phase-2 «conflicts» were only form (fixed value vs the function giving the same value).
- **What stayed in the group scripts**: the keywords that occur in ONE segment of the book (per-segment CTX): map_g1
  10 segments (vāresu, vārasaṅkhepo, the paccuppanna- pairs, ghānasadiso / ghānadhātusadisā, the slips vadanākkhandho,
  sotāyananti, parinibbāntānaṃ, asaññattā, uppajjittharūpāyatanañca, upapajjissati ^6-3-212); map_g2 9 segments
  (paccanīkaokāsā, Sattānusayā, Pajahanāvāre, Dhātupucchāvāro, Dhātuvisajjavāro / upapattināma, Atikkantakālavāro,
  cittake, sarāgacittassa uppādakkhaṇe, Pacchimakusalacittassa); map_g3 7 segments (anaññātaññāssāmīti, upapajjissati
  ^6-10-309, uppajjantānaṃ ^6-10-398, uppajjantīnaṃ ^6-10-206, Ghānandriyamūlakaṃ, cavantāna, Yamakapakaraṇaṃ).
  map_sample has no table. All four scripts build the stem with `make_stem([R.FRAME, R.STOCK, R.BOOK])`.
- **Result**: 15 values changed against the phase-2 files (phase3-changes.tsv: mechanic 5 5, g3 U4 8, g2 U3 2); every
  other value is byte-identical, i.e. the book-wide rules give the same values the group tables gave.

## E. Keyword ambiguities (phase 1, as settled)

B1–B10 of phase 1 hold as approved (two root-predicate shapes of R4, abyākata as an adjectival root base,
upapajjantānaṃ «…ဆဲသူ» / «…ဆဲ», pañcavokārānaṃ «… ရှိသူ / … ရှိသော», asaññasatta plane / beings, hetu / paccaya in the
hetuvāra, Samuṭṭhānāhārārammaṇā joined, the answers Āmantā / Natthi / No, Viññāṇañca = viññāṇaṃ + ca, nāma
«စိတ်ပိုင်း»); see `work/map-harmonise-notes-phase1.md` §B.

## F. Unclear points: how they were settled, and what is left

- **g1 / g2 points** were decided by the coordinator (phase-3 brief) and are applied: g1 U1 nāyatanā gapped value,
  U2 sa-X-ka «X ရှိသော / X မရှိသော», U3 Yattha «အကြင်နေရာ» / Yassa yattha «အကြင်သူအား အကြင်နေရာ», U4 the slip as g1
  chose (rails §A 6); g2 U1 sānusayo / niranusayo whole, U2 cited sections without quotation marks, U3 saraṇaaraṇā
  without «အတွဲ» (changed), U4 uppannaṃ «ဖြစ်ပေါ်ပြီးသော» everywhere (changed, mechanic 5), U5 Aṭṭhamako «အဋ္ဌမ», U6
  tesaṃyeva «ထိုသူ», U7 vattamāne «ဖြစ်နေသော» / bhaṅgā «ပြိုပျက်သော».
- **g3 points** (settled by the coordinator's general principle — the keyword's own meaning, dictionary form,
  present as a phrase, no plural / case particle, no translator's addition): U1 anaññātaññassāmīti without «အရာ»
  (kept); U2 kusalānaṃ uppādakkhaṇe without «သဘောတရား» (kept); U3 Abyākatañca dhamme gapped (kept); U4 the joined
  «မျက်မှောက်ပြု…» everywhere by the new ending «neg-verb-sp», W6 dropped (changed, 8 uses); U5 Aṭṭhamako «အဋ္ဌမ» (as
  g2 U5), U6 vattamāne «ဖြစ်နေသော» (as g2 U7), U7 sa-X-ka / ñāṇasampayuttānaṃ «…သော» (as g1 U2); U8 Yamakapakaraṇaṃ
  «အတွဲလိုက် မေးဖြေခြင်း ကျမ်း» (kept; now a per-segment rule of map_g3, the only segment).
- **Left open**: none. Observations for a later run: (a) the «-pi / -mpi» forms (anulomampi, uppādepi, atītepi …) get
  their values from S1, not from R1, because `base_forms` has no «-pi» rule; the values are the base's and right;
  (b) f_rupam book-wide relies on a free «ရုပ်» in the segment: no segment outside G1 changed.
