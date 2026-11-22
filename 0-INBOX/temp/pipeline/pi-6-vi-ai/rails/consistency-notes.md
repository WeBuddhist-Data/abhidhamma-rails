# pi-6 Vietnamese rails: consistency pass (2026-11-22)

Brief: consistency-brief.md. Scope: the 43 rails chapters + preamble in
AI_translation/vietnamese/pi-6-vietnamese-plain-rails_split_chapters/.

Files: consistency_find_vi.py (finder; writes divergences-rails.md, before and after), consistency_fix_vi.py (explicit
(file, old, new, count, reason) replacements with asserted counts, run from the pre-fix copies, re-runnable),
consistency/ (pre-fix copies of the 13 changed chapters, made once), consistency-log.tsv (one row per replacement:
file, block id, old -> new, reason). No builder, notes-rails-*, vi-rails-formulas.md, rails-coordinator-rules.md or
termbase file was edited. The approved sample (preamble.md, 1-mulayamaka.md) is unchanged (asserted by the fixer;
no fix needed it, so there is no "sample differs" item).

## Finder

Reads only the rails chapters, the Pāli chapters, rails/consistency/ and (read-only imports, nothing written) the
member tables of the family builders (2-01 KHANDHA, 3-01 AYATANA, 4 DHATU_M, 5-01 SACCA_A / SACCA_B, 6-01 SANKHARA,
7-01 ANUSAYA, 9-01 DHAMMA, 10-01 INDRIYA). Levels: (L) lines, (S) sentences, (M) sentences with members and the verb
lexemes masked (tense / negation kept), (H) answer heads (person / place head before «thì», compared unmasked),
(B) answer bodies (masked), (P) notes in round brackets, (C) headings and closing sentences, (N) identical Pāli
phrases inside the editorial notes, (Q) «?» per line and cut questions, (V) a nested run with a second run-level «và».
«?» is kept in the keys: a cut "…pe…?" and a cut "…pe…." are different Pāli (rule: «… không?» / «…»).

Group counts, before → after: L 0 → 0, S 0 → 0, M 2 → 2, H 2 → 2, B 2 → 2, P 0 → 0, C 0 → 0, N 4 → 0, Q 5 → 5,
V 79 → 0. (A first, cruder run that stripped «?» showed L 1 / M 6: all were "…pe…?" against "…pe…." cuts, i.e.
not identical Pāli; see clash 5.)

The book was already uniform at the identical-Pāli level: 11 363 line keys, 10 567 sentence keys, 6 260 masked keys,
some 1 100 head keys and 135 heading / closer keys, none with two Vietnamese forms except the groups below.

## Changes: 87 (clash 1: 79, clash 2: 8)

| chapter | changes | blocks |
|---|---|---|
| 3-03 | 6 | ^6-3-96, 101, 117 |
| 3-04 | 4 | ^6-3-132, 134, 141, 143 |
| 3-05 | 6 | ^6-3-181, 184, 196, 210 |
| 3-06 | 5 | ^6-3-220, 229, 248 |
| 4 | 1 | ^6-4-18 |
| 5-02 | 1 | ^6-5-91 |
| 6-01 | 10 | ^6-6-32, 33, 38, 39, 42, 44, 72 |
| 6-02 | 12 | ^6-6-88, 91, 93, 121, 137, 140, 142 |
| 10-06 | 6 | ^6-10-301, 302 |
| 10-07 | 6 | ^6-10-328, 329 |
| 10-10 | 12 | ^6-10-386, 387, 388 |
| 10-11 | 6 | ^6-10-396, 397, 398 |
| 10-12 | 12 | ^6-10-427, 428, 429 |

All other chapters: 0. (6-02 ^6-6-121: the two changed sentences are the jhāna runs; the line reported in
notes-rails-6-02 as translated as written, «… kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati», is a
different line and is untouched.)

## Known clashes

1. Double «và» in nested runs (79 changes). Rule: a run of groups joined flat with one run-level «và».
   - Flattened (no misreading), 12: 10-06 ^6-10-301 / 302, 10-07 ^6-10-328 / 329 "Rūpāvacarānaṃ arūpāvacarānaṃ ye
     ca purisā / itthiyo …" «Ở chúng sinh trong cõi hình sắc, chúng sinh trong cõi không hình sắc và những người nam
     / nữ nào …» (3-02's flat form for a nested plane-being run, as 6-01 ^6-6-32 / 3-06 ^6-3-226 already read).
   - Inner «và» kept, outer item joined with «, và …» (flattening would read the next group as one more place after
     «trong» / «vào», or as an object of «nhập»), 67: «… trong / vào cõi hình sắc và cõi không hình sắc, và những
     người nào …» (31: 3-03, 3-04, 3-05, 3-06, 6-01, 6-02, 10-10), «… cõi hình sắc và cõi không hình sắc, và chúng
     sinh Vô Tưởng» (26: 3-03, 3-05, 10-11, 10-12), «… tầng thiền thứ hai và tầng thiền thứ ba, và chúng sinh (khác)
     trong cõi dục lạc» (8: 6-01, 6-02), «… tầng thiền thứ ba và tầng thiền thứ tư, và chúng sinh trong cõi Tịnh Cư»
     (2: 6-01).
   - Kept (not a nested run: one run-level «và» only): (k1) an inner plane list inside a ye-clause closed by its verb,
     «Những người nào sau khi tái sinh vào cõi hình sắc và cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn và những
     người nam / nữ nào …» (36: 10-05 ^6-10-283 / 284, 10-06 ^6-10-310 / 311, 10-09, 10-10, 10-12); this is the 10-05
     item of the coordinator's list: nothing to flatten. (k2) a run whose LAST item holds the inner list, «A và
     những người … trong cõi hình sắc và cõi không hình sắc» / «… và những người đang nhập tầng thiền thứ hai và tầng
     thiền thứ ba» (52: 3-03, 3-06, 6-01 ^6-6-67 / 72, 6-02, 10-06, 10-10, 10-11, 10-12). (k3) not a run of groups:
     6-01 ^6-6-19 «sự hướng tâm và sự duy trì tâm mà không có hơi thở vào và hơi thở ra» (10), 8 ^6-8-83 (2).
   - 3-06 ^6-3-221 … 226 were already flat (no double «và» left there); 9-01 has no nested run left.
2. Editorial-note wording (8 changes), identical Pāli phrases, (N) 4 → 0:
   - vibhajitabbaṃ «cũng nên phân tích như vậy» (pi-2 1-khandhavibhango; 2-02, 3-06, 5-02, 5-03, 6-01, 6-02): 4 ^6-4-18
     «… cũng nên được phân tích như vậy» → «… cũng nên phân tích như vậy».
   - pucchā «các câu hỏi về …» (family setter 5-02): 3-04 ^6-3-132, ^6-3-141, 3-05 ^6-3-210, 3-06 ^6-3-229, ^6-3-248 (×2).
   - anulomampi paccanīkampi «cả chiều thuận lẫn chiều nghịch» (5-02, 5-03, 6-01, 6-02): 3-04 ^6-3-132, 3-05 ^6-3-210,
     3-06 ^6-3-229 (= 6-02 ^6-6-147 shape); 3-06 ^6-3-248 «ở cả chiều thuận lẫn chiều nghịch» (same Pāli run
     yassakampi yatthakampi yassayatthakampi anulomampi paccanīkampi as 5-02 ^6-5-153).
   - one-subject sadisaṃ vitthāretabbaṃ «… cũng nên được trình bày chi tiết giống như vậy» (setter 3-04 ^6-3-125):
     5-02 ^6-5-91 «giống nhau» → «giống như vậy» (Pāli "Yassa yatthakampi" / "Yassayatthakampi": spacing only).
   - vitthāretabbaṃ «nên được trình bày chi tiết» was already uniform; «như đã được phân tích trong …» uniform.
3. Head parsers: (H) compares every identical Pāli head across all chapters; none prints differently (the 10-03 /
   10-02 / 3-02 plane-only heads and the 9-01 / 3-02 nested runs agree; the nested runs are settled under 1).
4. Headings and closers: (C) 135 keys, 0 groups: "<X>vāro." / "<X>vāro niṭṭhito." / "<X>vāre anulomaṃ / paṭilomaṃ."
   and the yamaka closers read the same in every yamaka (nirodhavāro «Mục về sự chấm dứt» ×13, uppādavāro «Mục về sự
   sinh khởi» ×12, pajahana- / pahīna- / pariññā- / sānusaya- / anusayavāre anulomaṃ / paṭilomaṃ «Chiều thuận /
   ngược trong mục về …», «Phần các cặp câu hỏi về … đã hoàn tất.»). No change.
5. Cut questions: every Pāli cut "…?" / "…pe…?" has «… không?», no cut "…pe…." has one. 3-05 ^6-3-166 / 167 / 171
   «(b) Còn ở người nào mà lĩnh vực hình sắc…» vs 3-06 ^6-3-221 / 236 «… không?», and 5-02 ^6-5-153 «…» vs 3-05 / 8
   «… không?»: not identical Pāli ("…pe…." vs "…pe…?"); both follow the rule. No change.
6. Every remaining finder group is explained below.

## Remaining groups (after)

- (M) «(kha) M M Māti?», «(kha) M M M?» (9-01 ^6-9-1, 3, 17, 19): false hit: masking merges "kusalā dhammā | kusalā"
  with "dhammā | akusalā dhammā" (different Pāli word grouping).
- (H) «Dve puggalā», «Puthujjano» (7-03 ^6-7-73, 75, 76; 7-04 ^6-7-106): false hit: nominative heads without tesaṃ;
  the Vietnamese predicate («có» / «không có») stands before the member, so the cut is not at the same point.
- (B) «tesaṃ (tattha) Mñca Vissati Mñca Vati» (3-06 ^6-3-230, 236, 237): false hit: lines cut by …pe… after the head
  (the Pāli head boundary falls in the second clause).
- (Q) 5: kept, reported: questions the Pāli ends with «.» that are plainly questions, rendered «?» by their chapters:
  2-01 ^6-2-36, 7-10 ^6-7-335, 10-13 ^6-10-455 (×2) (in their notes); 5-02 ^6-5-130 «(Kha) yassa vā pana yattha …
  nirujjhitthāti.» (not in notes-rails-5-02: listed here for the review).
- kept: context (not divergences): sabbattha «ở mọi nơi» (7-02, 7-04, 7-06, 7-08 person answers) / «ở mọi chỗ»
  (notes 3-01, 3-04, 5-01, 6-01); bare dukkhaṃ «khổ đau» (Sacca) / «sự khó chịu» (Indriya); sadisaṃ «giống nhau»
  with two subjects or with sabbattha (5-01 ^6-5-31, ^6-5-40, 3-04 ^6-3-124) / «giống như vậy» with one subject.

## Left for the user

- Termbase vs chapter (to the termbase alignment; not changed): Itaresaṃ «người khác» vs «chúng sinh khác trong cõi …»
  / «những người khác có mắt …»; the second-plane forms «chúng sinh trong cõi X và cõi Y» (pañcavokārānaṃ,
  rūpāvacarānaṃ, kāmāvacarānaṃ, arūpānaṃ, asaññasattānaṃ after another plane-being); kusalā / akusalā / abyākatā
  dhammā in the sample; nāyatanā. Termbase adherence lists them (169 misses, unchanged).
- Lines translated as written where the Pāli looks inconsistent (^6-7-243, ^6-9-192, ^6-6-121, ^6-10-357,
  ^6-10-361 and the others in the chapter notes): untouched; they go to the review.
- The «, và …» joins of clash 1 (67) are the brief's fallback for runs that cannot be flattened without a misreading;
  the user may prefer spelling the groups out instead.

## Checks (after the fixes, all 44 files)

- check_chapter_ids.py: 44 / 44 OK; dashcheck.py: 0 dash-line mismatches, 0 extra dashes; verify_rails_vi.py: 44 / 44 OK.
- No «….», «:-», «là là», «được được», «chánh niệm», «vẫn đã», «Vào tâm mà ngay sau đó»; NFC; LF (fixer asserts).
- termbase_adherence_vi.py (whole folder): 27 353 keyword occurrences in 3 128 segments, 169 without the termbase term
  (0.6%), before and after: unchanged.
