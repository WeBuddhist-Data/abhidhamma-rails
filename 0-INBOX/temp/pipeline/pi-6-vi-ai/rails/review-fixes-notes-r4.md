# Review fixes, stage 1, part r4 (2026-11-22)

Chapters: 7-09, 7-10, 7-11, 8-cittayamaka, 9-01, 9-02, 9-03, 10-01, 10-02. Script: review_fixes_r4_vi.py (builds from
backup-pre-review/<ch>, asserted counts, re-runnable; log review-fixes-log-r4.tsv, one row per replacement).

## Lines changed

| chapter | F1 | F3 | F4 | F9 | lines |
|---|---|---|---|---|---|
| 7-09 | 0 | 0 | 0 | 0 | 0 |
| 7-10 | 0 | 0 | 1 | 0 | 1 |
| 7-11 | 0 | 0 | 0 | 4 | 4 |
| 8 | 26 | 16 | 28 | 0 | 60 |
| 9-01 | 0 | 11 | 46 | 0 | 51 |
| 9-02 | 0 | 13 | 51 | 0 | 58 |
| 9-03 | 0 | 9 | 31 | 0 | 34 |
| 10-01 | 0 | 0 | 0 | 0 | 0 |
| 10-02 | 0 | 0 | 84 | 0 | 84 |

Replacements: F1 26 (20 question lines, 6 answer lines), F3 49, F4 241 (present 155, past «chưa từng» 24, future
«sẽ không» 52, uppanna «không ở trạng thái đã sinh khởi» 8, uppajjamāna / nirujjhamāna 2), F9 4. No "neither" F4
shape occurs in r4 (0 «không có X, cũng không có Y <V>»). 0 «không có <member> (đã |sẽ )?(sinh khởi|chấm dứt)» left
after a positive "no ca" clause. 13 "no ca" + verb clauses in 8 (dhamma frames ^6-8-37, 81, 85, 86, 94, 96, 97, 98,
101, 102) already had the negation on the verb («nhưng tâm ấy không …», «nhưng không phải đang …»): unchanged.

## F1 (8-cittayamaka Atikkantakāla, ^6-8-20, 40, 60, 83, 104)

Questions (uddesa and niddesa identical, as the Pāli apart from "-ṃ?" / "-nti?"):
- person: «(a) Ở người nào mà tâm đã vượt qua khoảnh khắc sinh khởi và đã thuộc thời đã qua, thì ở người ấy có phải tâm
  cũng đã vượt qua khoảnh khắc chấm dứt và đã thuộc thời đã qua không?» / «(b) Còn ở người nào mà tâm đã vượt qua
  khoảnh khắc chấm dứt và …, thì ở người ấy có phải tâm cũng đã vượt qua khoảnh khắc sinh khởi và … không?»;
  negative «chưa vượt qua … và chưa thuộc thời đã qua …, … có phải tâm cũng chưa vượt qua … và chưa thuộc thời đã qua
  không?»
- dhamma: «(a) Tâm nào đã vượt qua khoảnh khắc sinh khởi và đã thuộc thời đã qua, thì có phải tâm ấy cũng đã vượt qua
  khoảnh khắc chấm dứt và đã thuộc thời đã qua không?», «(b) Còn tâm nào …»; negative the same with «chưa».
- person + dhamma: «(a) Ở người nào mà tâm nào đã vượt qua …, thì ở người ấy có phải tâm ấy cũng đã vượt qua … không?»,
  «(b) Còn ở người nào mà tâm nào …»; negative the same with «chưa».
Answers: «Tâm vào khoảnh khắc tan rã đã vượt qua khoảnh khắc sinh khởi mà chưa vượt qua khoảnh khắc tan rã, tâm thuộc
quá khứ đã vượt qua khoảnh khắc sinh khởi và đã vượt qua khoảnh khắc tan rã.»; «Tâm thuộc quá khứ.» (unchanged);
«Tâm vào khoảnh khắc sinh khởi và tâm thuộc tương lai.»; «Tâm vào khoảnh khắc tan rã chưa vượt qua khoảnh khắc tan rã
nhưng đã vượt qua khoảnh khắc sinh khởi, tâm vào khoảnh khắc sinh khởi và tâm thuộc tương lai chưa vượt qua khoảnh khắc
tan rã và chưa vượt qua khoảnh khắc sinh khởi.».
The questions keep «khoảnh khắc chấm dứt» (nirujjhamānaṃ khaṇaṃ = nirodhakkhaṇa, commentary) and the answers
«khoảnh khắc tan rã» (bhaṅgakkhaṇa), as the Pāli words differ. ^6-8-83's slip "vītakkantaṃ" stays rendered as meant.

## Decision to check: participle after "no ca" (F4)
The brief's example is «X không đang sinh khởi». 8 already says «không phải đang …» for na + uppajjamāna / nirujjhamāna
(family D) and for the dhamma-frame "no ca" answers («nhưng tâm ấy không phải đang sinh khởi», ^6-8-97, 98). To keep one
form in the chapter, the two person-frame lines ^6-8-76, 77 read «nhưng ở những người ấy tâm không phải đang sinh khởi /
chấm dứt». The participle occurs only in 8 (no other part touches it). If the brief's «không đang» is wanted, change
NEG["đang "] in review_fixes_r4_vi.py and re-run.

## Stale builder constants (chapters not rebuilt)
- build_rails_8_vi.py: MOMENT_PROG («khoảnh khắc đang …»), PASSED / NOT_PASSED («đã / chưa vượt khỏi»; pi-2
  vītikkanto «đã vượt khỏi» noted there), STILL_PASSED («đã từng vượt khỏi»), GONE / NOT_GONE, ATK_TAIL,
  passed_phrase() and question() for the atikkanta frame; the answer list «Tâm vào khoảnh khắc sinh khởi, tâm thuộc
  tương lai.»; nirodhasamāpannānaṃ «những người nhập …» (PERSON table, l. 255); NONE = C.NEITHER_FIRST used for
  the "no ca" person-frame answers and questions.
- build_rails_2-01_vi.py: b_noca() / noca_vi() («nhưng ở những người ấy không có B V2») used by 9-01 … 9-03, 10-01,
  10-02 (via their imports); build_rails_7-01_vi.py NEITHER_FIRST for uppajjati in 7-10 (^6-7-330).
- build_rails_7-11_vi.py: HETTHA «xuống phía dưới» (l. 69, docstrings l. 23, 116).
- coordinator rules / termbase: «những người nhập thành tựu thiền chấm dứt» (rails 8 entry), 7-11 heṭṭhā entry.

## Checks
check_chapter_ids OK, dashcheck 0 mismatches, verify_rails_vi OK for all nine chapters; NFC, LF, no CR; no «—»,
«:-», «….», «được được», «là là», «chánh niệm», «vẫn đã», «seed», double spaces; 0 «vượt khỏi», «khoảnh khắc đang
sinh khởi / chấm dứt», «đó là tâm», «nhập thành tựu thiền chấm dứt» without «đang», «xuống phía dưới» left;
identical-Pāli lines with two Vietnamese forms in the part: 0 before, 0 after.
