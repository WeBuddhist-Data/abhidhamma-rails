
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
