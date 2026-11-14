# Brief: apply the review fixes, pi-1 Russian plain RAILS translation

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write only in AI_translation\russian\pi-1-russian-plain-rails_split_chapters\ (14 files) and 0-INBOX\temp\pipeline\pi-1-ru\review\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the builders in pi-1-ru\rails\ or the termbase, do not run git, never write "seed". You cannot write report files for me: return your report as text.

## Input
- The four review reports with my decision on each row: 0-INBOX\temp\pipeline\pi-1-ru\review\findings-r1.md … findings-r4.md. Apply every row whose decision is **APPLY** (including "APPLY book-wide"). Do not apply REJECT rows.
- **User decisions (2026-11-14), apply everywhere the Pāli has the item, sample and matrix included:**
  1. The sārāga family is all «пристрастие»: asārāgo «отсутствие пристрастия» (already), asārajjanā «отсутствие проявления пристрастия», asārajjitattaṃ «отсутствие состояния пристрастия»; sārajjanā «проявление пристрастия», sārajjitattaṃ «состояние пристрастия» (positive forms in the greed strings). rāga stays «страсть».
  2. asantuṭṭhitā ca kusalesu dhammesu (^1-M2-140 and wherever this item recurs, e.g. ch4 definitions) = «Ненасытность в благих явлениях» (inflect where the frame needs it).
  3. bhāṇavāra = «часть для чтения вслух» book-wide: «Первая часть для чтения вслух», «Первая часть для чтения вслух в разделе о материальной форме», «Вторая часть для чтения вслух в разделе сводки» … (including 2-01 ^1-57 and every other occurrence).
  4. Matter-chapter headings and closing lines, for 2 … 11: «Классификация по два / … / по одиннадцать» → «Классификация на два вида», «на три вида», «на четыре вида», «на пять видов» … «на одиннадцать видов»; the closing «Такова классификация материальной формы на два вида.» etc.; the «Классификация материальной формы по N –» lines likewise «… на N видов –». For Ekakaṃ (by one) keep «по одному» unless another wording clearly reads better; report what you chose.
  5. Rūpavibhatti = «Разбор материальной формы» (^1-2-3-0, ^1-984 and any other occurrence); rūpasaṅgaha stays «классификация материальной формы».
  6. bhūmi in ch5 «catūsu / tīsu bhūmīsu» = «уровень»: «благой ум четырёх уровней», «… трёх уровней» (and every other catūsu/tīsu bhūmīsu). The heading Tebhūmaka «Благой ум трёх миров» in ch2 stays (approved heading).
- **Book-wide consistency rules** that go with the APPLY rows:
  - X-gataṃ after a noun = «то, что считается X»: «просвет, то, что считается просветом», «вода, то, что считается водой, влага, то, что считается влагой», «огонь, то, что считается огнём, …», «ветер, то, что считается ветром» (every occurrence: ^1-637, 651, 724, 726, 853, 856, 968, 969, 970 and any other).
  - niyyānikaṃ apacayagāmiṃ = «ведущее к освобождению и к убыванию» (masculine «ведущий к освобождению и к убыванию» etc.), wherever the Russian has «ведущее к освобождению и ведущее к убыванию».
  - «X – это …» without a comma after a plain noun phrase or list, including lists with inner commas (the r3 rows); the comma stays where it closes a clause, a «кроме» phrase or a participial phrase (^1-583 keeps it). r3 row ^1-700/817/983: add the comma there (the «это X, …, это Y» chain).
  - «какая бы другая материальная форма ни была (не) вследствие …» → «… ни возникла (не) вследствие …» everywhere.

## Method
Write review\apply_review_fixes_ru.py: fixed old → new string rules, each conditioned on the block ID or on the aligned Pāli line (non-empty line i ↔ i), plus per-segment rules for the one-off rows. Back up the 14 files once to review\backup-pre-fixes\ and always start from the backup, so the script can be rerun. Log every change to review\fixes-log.tsv (file, line, rule, old, new). Support --dry. Line counts, IDs, heading levels and dashes must not change.
Note: the rails builders in pi-1-ru\rails\ are now stale; list in review\builders-stale.md which builder constant each rule would need, so a rebuild can be followed by this script (it must be rerun after any rebuild, after rails\fix_bare_comma_ru.py).

## Verify
For all 14 files: check_chapter_ids (OK), `0-INBOX\temp\pipeline\dashcheck.py` (0 mismatches, 0 extra), `0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py` (OK); grep for «—», «:-», «ли» as a word, «seed», Latin outside [..], CR, double blank lines; grep that none of these is left: «считающееся», «ведущее к освобождению и ведущее», «раздел для чтения вслух», «Классификация по два», «четырёх миров», «проявления страсти», «Отсутствие довольства», «говорит такой речью», «двое или трое оков», «ни была». Identical Pāli → identical Russian still holds: `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\rails\find_divergences_rails_ru.py` (0 diverging). Termbase adherence before and after:
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence.py AI_translation\pali\pi-1-keywords-by-reference-pali-plain.md AI_translation\russian\pi-1-pali-russian-termbase-plain.md AI_translation\russian\pi-1-russian-plain-rails_split_chapters
```

## Report (under 400 words)
Rules applied with counts; every APPLY row you could not apply and why; the Ekakaṃ decision; check results.
