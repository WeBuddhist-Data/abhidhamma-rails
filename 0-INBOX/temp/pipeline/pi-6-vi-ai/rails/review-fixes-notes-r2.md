# Review fixes, stage 1, part r2 (3-06, 4, 5-01, 5-02, 5-03, 6-01, 6-02, 7-01): notes

Script: `review_fixes_r2_vi.py` (builds from `backup-pre-review\<ch>.md`, re-runnable; `scan` = read-only survey).
Log: `review-fixes-log-r2.tsv` (file, block id, line, old, new, rule). 316 lines changed.

## Counts (occurrences; lines changed in brackets)

| chapter | F3 | F4 | F5 | F6 | lines |
|---|---|---|---|---|---|
| 3-06 | 0 | 38 | | | 38 |
| 4 | 0 | 7 | | 14 | 10 |
| 5-01 | 6 | 51 | | | 55 |
| 5-02 | 10 | 45 | | | 53 |
| 5-03 | 2 | 11 | | | 12 |
| 6-01 | 19 | 48 | 13 | | 70 |
| 6-02 | 23 | 49 | 24 | | 78 |
| 7-01 | 0 | 0 | | | 0 |
| total | 60 | 249 | 37 | 14 | 316 |

- F4: every hit is a single member after «nhưng ở <pron>[, ở nơi ấy]»: «không có X V» → «X không V», «không có X đã V» → «X chưa từng V», «không có X sẽ V» → «X sẽ không V». No "neither" (two-member) pavatti line and no participle («đang») form occurs in this part. 7-01 is all anuseti: untouched (its «không có A, cũng không có B nằm sẵn» stay).
- F3: Pāli nirodhasamāpann- 6 / 11 / 2 / 19 / 23; the one extra Pāli hit in 5-02 (^6-5-122, line 239) is inside a variant bracket, which keeps its Pāli. Quoted forms in the notes ^6-5-95, ^6-5-143, ^6-6-28, ^6-6-86, ^6-6-135 changed too.
- F5: only «tâm cuối cùng không có sự hướng tâm cũng không có sự duy trì tâm sẽ sinh khởi» → «tâm cuối cùng, vốn không có sự hướng tâm cũng không có sự duy trì tâm, sẽ sinh khởi». Not changed (no «sẽ sinh khởi» after the modifier): «những người có được tâm cuối cùng không có sự hướng tâm cũng không có sự duy trì tâm» (Pacchimacittasamaṅgīnaṃ avitakka…), and «tâm cuối cùng có sự hướng tâm và sự duy trì tâm» (no «không có»).
- F6: ^6-4-6 «… Thức qua mũi?… thức qua lưỡi?… Thức qua thân?»; ^6-4-7 «… Những gì không phải là mũi?… …» (8 stubs) and «… Những gì không phải là thức qua tai?… …» (3 stubs). Full questions such as «Mũi có phải là yếu tố không?» (Pāli "Ghānaṃ dhātu?") stay.
- F2: the ^6-3-23 note Pāli does not recur in this part. 6-01 ^6-6-31 "(Yatthakampi sabbattha ekasadisaṃ)" «(Phần về nơi chốn ở mọi chỗ cũng đều giống hệt nhau)» is a different note (it says the sections are alike): kept.

## Stale builder constants (chapters were not rebuilt)

- `build_rails_7-01_vi.py` `neg_clause_vi()` (line ~278) with `NEITHER_FIRST` / `NEITHER_NEXT`: after "no ca" a positive verb gives «không có A[, cũng không có B] V» for every verb; after F4 that holds only for anuseti. Every pavatti chapter importing it (2-01 setter, 3-06, 4, 5-01 … 6-02) now differs from its builder output.
- `build_rails_8_vi.py` `PERSON["nirodhasamāpannānaṃ"]` (line 255) «những người nhập thành tựu thiền chấm dứt»; through it `build_rails_6-01_vi.py` `NIRODHA_Q` (346) / `NOTE_NA_LABBHATI` (351), `build_rails_6-02_vi.py` line 96, `build_rails_5-01_vi.py` line 255 and its termbase check list (777), `build_rails_5-02_vi.py` termbase check list (356) and the note text (449). The termbase entry needs the same change (alignment step).
- `build_rails_6-01_vi.py` `anantara_group()` (147-153): `FINAL_MIND + " " + AVITAKKA` gives the old F5 form; 6-02 imports it.
- `build_rails_4_vi.py` `bare_q()` (236) with `TAIL_POS` / `TAIL_NEG` (217-218) and the note row at line 581: old «Thức qua mũi không?» / «…, có phải không?» stubs.
- The per-chapter notes files (notes-rails-3-06.md … notes-rails-6-02.md, vi-rails-formulas.md) still describe the old wordings; not edited.
