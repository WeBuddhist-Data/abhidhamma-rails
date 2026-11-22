# Brief: apply the user-approved review fixes, pi-6 Vietnamese rails (Yamaka): STAGE 1, ONE PART

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell, not even a scratch file), PowerShell for commands, `python -I -X utf8 -B`, LF line endings (newline="\n"). Five fix agents run at once, one per part (r1 … r5); each edits ONLY the chapter files of its own part in AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\, plus its own new files in 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\: review_fixes_<rN>_vi.py, review-fixes-log-<rN>.tsv, review-fixes-notes-<rN>.md, and backup copies of its own chapters in rails\backup-pre-review\ (copy once, never overwrite). Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, the termbase, the builders, the sample builder, other parts' chapters; never run git; never write "seed". No web. Return your report as text.

## Parts
- r1: preamble.md, 1-mulayamaka.md, 2-01, 2-02, 3-01 … 3-05
- r2: 3-06, 4-dhatuyamaka.md, 5-01, 5-02, 5-03, 6-01, 6-02, 7-01
- r3: 7-02 … 7-08
- r4: 7-09, 7-10, 7-11, 8-cittayamaka.md, 9-01, 9-02, 9-03, 10-01, 10-02
- r5: 10-03 … 10-13

## FORBIDDEN
Never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\; this book's Vietnamese zero-shot (AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot*, and everything in pi-6-vi-ai\ outside rails\, termbase\ and review\review-findings.md); the Vietnamese side of the keyword map (pi-6-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-6-keywords-by-reference-pali-vietnamese-plain.md); the review\r*_*.py scripts (they read the reference); the tool-results cache folders. Grep only named files, never whole folders (a Python script may read your own part's chapter files and their Pāli). The fixes are in our own words.

## Read first
- 0-INBOX\temp\pipeline\pi-6-vi-ai\review\review-findings.md (the findings; the user approved them all as proposed on 2026-11-22).
- 0-INBOX\temp\pipeline\vietnamese-style.md; rails\rails-coordinator-rules.md, rails\consistency-notes.md; the Pāli AI_translation\pali\pi-6_split_chapters\<ch>.md; the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md (Pāli, allowed; grep it).

## What stage 1 applies (fixed target wordings, so all five parts agree)
**Not in stage 1** (a single book-wide agent does them next, on your output): A5 case boundaries in answer heads, the faculty-attribute head order, the «chúng sinh Vô Tưởng» run fix, the ye-group «khi những người ấy đang chết đi» tail. Do not touch the answer heads (the text before «thì») except for F3 below.

- **F1 (A1, r4 only): 8-cittayamaka Atikkantakāla section** (^6-8-20, ^6-8-40, ^6-8-60, ^6-8-83, ^6-8-104; every question line of the section, uddesa and niddesa). Recast as the Pāli's A → B question, with the mind as the thing that passes the moment and belongs to past time (commentary: "kiṃ tassa cittaṃ evaṃ nirodhakkhaṇampi vītikkantaṃ hutvā atikkantakālaṃ nāma hotīti pucchati"; uppajjamānaṃ khaṇaṃ = the arising moment):
  - person frame: «(a) Ở người nào mà tâm đã vượt qua khoảnh khắc sinh khởi và đã thuộc thời đã qua, thì ở người ấy có phải tâm cũng đã vượt qua khoảnh khắc chấm dứt và đã thuộc thời đã qua không?» / «(b) Còn ở người nào mà tâm đã vượt qua khoảnh khắc chấm dứt và đã thuộc thời đã qua, thì ở người ấy có phải tâm cũng đã vượt qua khoảnh khắc sinh khởi và đã thuộc thời đã qua không?»;
  - negative pair: «chưa vượt qua … và chưa thuộc thời đã qua», «có phải tâm cũng chưa vượt qua …»;
  - dhamma frame (yaṃ cittaṃ …): «Tâm nào đã vượt qua … và đã thuộc thời đã qua, thì có phải tâm ấy cũng …?»; person + dhamma frame (yassa yaṃ …): «Ở người nào mà tâm nào …, thì ở người ấy có phải tâm ấy cũng … không?»;
  - in the same section's answers: «khoảnh khắc đang sinh khởi / đang chấm dứt» → «khoảnh khắc sinh khởi / chấm dứt» where the Pāli is the moment (uppajjamānaṃ / nirujjhamānaṃ khaṇaṃ); vītikkanta = «đã vượt qua» (not «đã từng vượt khỏi»), avītikkanta = «chưa vượt qua»; "Uppādakkhaṇe anāgataṃ cittaṃ." = «Tâm vào khoảnh khắc sinh khởi và tâm thuộc tương lai.».
  Read the whole section, its answers and the commentary before changing; report the final wording of every frame.
- **F2 (A2, r1 only): ^6-3-23 note**: say that the questions about the two bases are treated alike, not that the bases are the same: «… thì các câu hỏi về lĩnh vực ý và về lĩnh vực đối tượng của ý được trình bày giống hệt nhau, không có gì khác …» (keep the rest of the note as it is, variants included). Check whether the same note Pāli recurs in your part and treat it the same way.
- **F3 (A3, all parts): nirodhasamāpannānaṃ** «những người nhập thành tựu thiền chấm dứt» → «những người đang nhập thành tựu thiền chấm dứt» everywhere, inside notes and quotes too (also any other «nhập thành tựu thiền chấm dứt» without «đang» for the same Pāli).
- **F4 (A4, all parts with pavatti frames): "no ca" + uppajjati / nirujjhati** (and their tenses): the negation goes on the verb.
  - «nhưng ở <pron>[, ở nơi ấy] không có X sinh khởi» → «nhưng ở <pron>[, ở nơi ấy] X không sinh khởi»; «… không có X đã sinh khởi» → «… X chưa từng sinh khởi»; «… không có X sẽ sinh khởi» → «… X sẽ không sinh khởi»; the same with «chấm dứt»; the participle forms the same way («X không đang sinh khởi», «X không ở trạng thái đã sinh khởi») only if the chapter has «không có X đang …» there.
  - "neither" with these verbs: «…, nhưng ở <pron> không có X, cũng không có Y <V>» → «…, nhưng ở <pron> X <neg V>, Y cũng <neg V>» (e.g. «X chưa từng sinh khởi, Y cũng chưa từng sinh khởi»).
  - Do NOT change anuseti / sānusaya / niranusaya / pajahati / parijānāti / bhāveti / pahīna frames (they keep «không có A nằm sẵn», the user's "neither" wording «không có A, cũng không có B», and their own approved forms), and do not change any denied-negative «vẫn V» / «đã từng V» / «vẫn sẽ V».
  - Count each rule; assert 0 «không có <member> (đã |sẽ )?(sinh khởi|chấm dứt)» left after "no ca" in your part.
- **F5 (A6 minor, r2): Saṅkhāra modifier**: «những người mà tâm cuối cùng không có sự hướng tâm cũng không có sự duy trì tâm sẽ sinh khởi ngay sau tâm này» → «những người mà tâm cuối cùng, vốn không có sự hướng tâm cũng không có sự duy trì tâm, sẽ sinh khởi ngay sau tâm này» (and the same shape for any other «tâm cuối cùng <long modifier> sẽ sinh khởi» in 6-01 / 6-02 where the modifier itself contains «không có»).
- **F6 (A6 minor, r2): 4-dhatuyamaka cut stubs** ^6-4-6, ^6-4-7: «Thức qua mũi không?» → «Thức qua mũi?»; «Những gì không phải là mũi, có phải không?» → «Những gì không phải là mũi?» (the bare stub, as the Pāli's "Ghānaviññāṇaṃ?…" / "Na ghānaṃ?…"); every such stub the same way.
- **F7 (A6 minor, r1): sample 1-mulayamaka ^6-1-49 and ^6-1-99** (first line each): the cut question that opens «có phải» ends «… không» (no "?", as the Pāli).
- **F8 (A6 minor, r1): ^6-3-148** line 5: the Pāli's comma where a sentence ends is rendered as a full stop: «…vẫn sẽ chấm dứt. Ở những người đang nhập Niết-bàn trọn vẹn…».
- **F9 (A6 minor, r4): heṭṭhā** (7-11) «xuống phía dưới» → «xuống cõi thấp hơn».
- Everything in section B of the findings stays as it is; section C lines stay as written.

## Method
1. Back up your part's chapter files to rails\backup-pre-review\ (once).
2. Write rails\review_fixes_<rN>_vi.py: exact string replacements (or per-segment regex anchored on the block ID), each rule with an asserted occurrence count, building from the backup so it can be re-run; rewrite rails\review-fixes-log-<rN>.tsv each run (file, block id, old, new, rule F#). Do not rebuild chapters from their builders; list stale builder constants in review-fixes-notes-<rN>.md.
3. Identical Pāli must still give identical Vietnamese inside your part.

## Verify (all must pass, every chapter of your part)
`python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters <ch>.md`; `python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>` 0 mismatches; `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>` OK; no «—», «:-», «….», «được được», «là là», «chánh niệm», «vẫn đã», «seed», double spaces; no CR; NFC; 0 remaining hits of the replaced strings.

## Report (under 400 words, as text)
Lines changed per chapter and per rule F1-F9; the final F1 wordings (r4); anything you could not apply or that needs the user; checks.
