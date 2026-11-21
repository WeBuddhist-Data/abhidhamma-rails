# Brief: apply the user-approved review fixes, pi-5 Vietnamese rails (Kathāvatthu): ONE PART

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8 -B`, LF line endings (newline="\n"). Five fix agents run at once, one per part (r1 … r5); each edits ONLY the chapter files of its own part in AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\, plus its own new files in 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\: review_fixes_<rN>_vi.py, review-fixes-log-<rN>.tsv, review-fixes-notes-<rN>.md, and backup copies of its own chapters in rails\backup-pre-review\ (copy once, never overwrite). Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, the termbase, the builders, the sample builder, other parts' chapters; never run git; never write "seed". No web. Return your report as text.

## Parts
- r1: preamble.md, 1-puggalakatha.md, 2-parihanikatha.md
- r2: 3-brahmacariyakatha.md … 10-dutiyavaggo.md
- r3: 11-tatiyavaggo.md … 15-sattamavaggo.md
- r4: 16-atthamavaggo.md … 22-cuddasamavaggo.md
- r5: 23-pannarasamavaggo.md … 31-tevisatimavaggo.md

## FORBIDDEN
Never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\; this book's Vietnamese zero-shot (AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot*, and the zero-shot files in pi-5-vi-ai\: backup-pre-harmonise\, harmonise*, build_*_vi.py and notes-*.md outside rails\, divergences*.md outside rails\); the Vietnamese side of the keyword maps (pi-5-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-5-keywords-by-reference-pali-vietnamese-plain.md); the tool-results cache folders. Grep only named files, never whole folders. The fixes are in our own words (the findings files contain no reference text).

## Read first
- 0-INBOX\temp\pipeline\pi-5-vi-ai\review\findings-summary.md (the user's approved decisions: A and B) and YOUR part's findings file review\findings-rN.md (every Part A row and every Part B row with a fix).
- 0-INBOX\temp\pipeline\vietnamese-style.md; the termbase AI_translation\vietnamese\pi-5-pali-vietnamese-termbase-plain.md and termbase\APPROVED.md; rails\vi-rails-formulas.md, rails\rails-coordinator-rules.md, rails\consistency-notes.md; the Pāli AI_translation\pali\pi-5_split_chapters\<ch>.md; the commentary 1-SOURCES\Commentaries\pi-kathavatthu-atthakatha.md (Pāli, allowed); pi-1 … pi-4 rails (rails\find_pi1234r_vi.py).

## User decision (2026-11-22): "Approve as proposed"
Apply ALL of findings-summary.md section A (A1-A20, incl. every MINOR row of your findings file, unless a B decision says otherwise) and section B as recommended. Fixed target wordings, so all five parts agree:
- **A2 assa:** «ngựa đực» → «ngựa» everywhere (assaratana «báu vật ngựa»; hatthibandhā assabandhā «người giữ voi, người giữ ngựa»); any «… đực» added for assa.
- **A19 bare samāpanna:** «người đang nhập» with no object → «người đang nhập thiền» where the context is jhāna; where the context is another attainment (e.g. saññāvedayitanirodha), name it («người đang nhập diệt thọ tưởng» or the chapter's existing wording for that attainment). Where an object already follows, keep it; «người đang nhập thành tựu thiền» → «người đang nhập thiền».
- **B3 kammaṃ karoti / karonti:** «tạo nghiệp» (replace «làm nghiệp»).
- **B4 taṃ jīvaṃ taṃ sarīraṃ:** «linh hồn và thân thể là một» (pi-1), in the frame's grammar (question «Có phải linh hồn và thân thể là một không?»); in the sample too (r1); aññaṃ jīvaṃ aññaṃ sarīraṃ by the pi-1 wording if present.
- **B5:** ^5-229 «đức Thế Tôn» → «Đức Thế Tôn».
- **B6 dibbasota:** «thiên nhĩ» (replace «tai thuộc cõi trời», e.g. «yếu tố thiên nhĩ»), symmetric with dibbacakkhu «thiên nhãn».
- **B7 Handa hi:** «Bởi vì» where it answers «theo nghĩa nào» / «vì sao»; ^5-308 the resolve form (A8); ch16 «Này,» / ^5-546 «Này, vì»: use «Bởi vì» if the Pāli is "Handa hi" answering a question; if it is a plain "handa" of resolve, the A8 style («Nào, …»). Report each.
- **B8 uppādino:** «có tính chất sinh khởi» (uppajjissanti stays «sẽ sinh khởi»).
- **B9 atthi / natthi:** «tồn tại» / «không tồn tại» where the thesis asks whether a thing exists (ch30 āsevanapaccayatā: «Có phải không tồn tại bất cứ tính chất làm điều kiện thực hành nào không?» / «… có tồn tại …»); «có» with a possessor or a place (ch11 saññā atthi with a locative stays «có»).
- **B10:** supply «?» where the Pāli's "…ti, āmantā." / "…ti, na hevaṃ" lacks it: «… không? Đúng vậy.» / «… sao? Đúng vậy.» / «… không? Không nên nói như vậy …» (^5-295, ^5-504, ^5-693, ^5-704, ^5-738, ^5-742, ^5-905 and any like them in your part).
- **B11:** keep ^5-405 and ^5-425 as written. **B12, B13, B15, B18:** keep.
- **B14:** kappaṭṭha «người lưu lại suốt một kiếp» (heading, theses, verse ^5-657, close, uddāna); idioms ^5-514 «vẫn còn nguyên như thế», ^5-674 / 675 ajjhosāya tiṭṭhanti / tiṭṭhati «cứ bám chặt».
- **B16 uddāna separators:** commas; semicolons only where an item itself contains a comma.
- **B17 Sakka:** «Đế Thích».
- **A12** anantarāpayutta «người đã khởi xướng nghiệp có quả không gián đoạn», payuttaṃ «đã được khởi xướng»; **A13** apariyāpanna «không nằm trong các cõi tồn tại» (heading «Bàn về điều không nằm trong các cõi tồn tại»); **A14** «hiểu biết sai lệch». When a kathā name changes, change its heading, closing line and every uddāna that names it (a fifty-group uddāna in another part: list it in your notes for the coordinator; do not edit another part's file).

## Method
1. Back up your part's chapter files to rails\backup-pre-review\ (once).
2. Write rails\review_fixes_<rN>_vi.py: exact string replacements (or per-segment regex anchored on the block ID), each rule with an asserted occurrence count, building from the backup so it can be re-run; log to rails\review-fixes-log-<rN>.tsv (file, block id, old, new, decision id A#/B#/minor). Do not rebuild chapters from their builders; list stale builder constants in review-fixes-notes-<rN>.md.
3. Identical Pāli must still give identical Vietnamese inside your part; where your fix changes a string that also occurs in another part (by the fixed wordings above it will match), note it.

## Verify (all must pass, every chapter of your part)
`python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-5_split_chapters AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters <ch>.md`; `dashcheck.py <pali ch> <vietnamese ch>` 0 mismatches; `pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>` OK; no «—», «:-», «….», «được được», «là là», «chánh niệm», «seed», double spaces; no CR; 0 remaining hits of the replaced strings.

## Report (under 400 words, as text)
Lines changed per chapter and per decision; final wording for A1, A4-A8, A12-A15, A18 (those in your part); anything you could not apply or that needs the user; strings shared with other parts; checks.
