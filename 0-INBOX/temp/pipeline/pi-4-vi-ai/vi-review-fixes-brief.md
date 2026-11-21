# Brief: apply the user-approved review fixes, pi-4 Vietnamese rails (Puggalapaññatti)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8`. Edit ONLY the chapter files in AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters\, plus new files in 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\ (review_fixes_vi.py, review-fixes-log.tsv, review-fixes-notes.md, backup-pre-review\). Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git, never write "seed". No web. Return your report as text.

## FORBIDDEN
Never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\; this book's Vietnamese zero-shot (AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot*, and the zero-shot files in pi-4-vi-ai\); the Vietnamese side of the keyword maps. Grep only named files, never whole folders. The fixes are in our own words (the findings files contain no reference text).

## Read first
- The findings: 0-INBOX\temp\pipeline\pi-4-vi-ai\review\findings-r1.md, findings-r2.md, findings-r3.md.
- 0-INBOX\temp\pipeline\vietnamese-style.md; the termbase AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md and termbase\APPROVED.md; rails\vi-rails-formulas.md and rails\build_rails_*_vi.py (to find every place a string occurs, incl. the matrix 1-matika.md).
- The Pāli: AI_translation\pali\pi-4_split_chapters\<ch>.md.

## User decisions (2026-11-21, "Apply as recommended")
1. **^4-10** gotrabhū: «… liền sau chúng xảy ra sự đi vào Giáo Pháp cao quý» → «… mà liền sau chúng, trạng thái cao quý khởi lên» (keep the rest of the sentence; the matrix item for gotrabhū too if it contains the same phrase).
2. **^4-209 and the matrix ^4-M-16** idha niṭṭhā / idha vihāya niṭṭhā: «ở đời này» → «ngay trong cõi này»; «sau khi rời khỏi đời này» → «sau khi rời bỏ cõi này». Same strings in the matrix, the questions and the closers. Do NOT change «ngay trong đời này» for diṭṭhe (va) dhamme or «Ở đời này, có người» (Idhekacco): only idha in these niṭṭhā phrases.
3. **^4-170 heartwood simile** (and the matrix item (24) or wherever the four names occur): the four trees «cây gỗ xốp mà các cây quanh nó có lõi», «cây có lõi mà các cây quanh nó là gỗ xốp», «cây gỗ xốp và các cây quanh nó cũng là gỗ xốp», «cây có lõi và các cây quanh nó cũng có lõi» (check which Pāli pheggu / sāra … parivāro is which); the four persons «người không có lõi mà những người quanh mình có lõi» and the matching three; identical across list, question, «Như vậy là …» and simile.
4. **^4-91, ^4-92, ^4-93** «Đến bao giờ tôi cũng sẽ …?» → «Đến bao giờ tôi mới được như vậy: nhờ sự diệt tận các ô nhiễm, ngay trong đời này tự mình … không còn ô nhiễm?» (keep each segment's middle as it is; one formula in all three).
5. **^4-124, ^4-126** «nghiêng về phía điều xấu / điều tốt» → «nghiêng về phía người xấu / người tốt»; «Con người kết bạn với …» → «Người đàn ông này kết bạn với …».
6. **^4-102, ^4-108** purisa: «một người có mắt» → «một người đàn ông có mắt»; «vạt áo của một người» → «vạt áo của một người đàn ông» (and any other puriso / purisassa rendered «người» alone, except the address «Này ông»; list them).
7. **^4-176 narassa:** KEEP as written («ở phía đông của một người»). No change.
8. **Names:** uddhaṃsoto akaniṭṭhagāmī → «người theo dòng đi lên đến cõi Sắc Cứu Cánh» (matrix, question, quoted name, every chapter; paṭisotagāmī stays «người đi ngược dòng»); dhammappamāṇo dhammappasanno → «người lấy phẩm hạnh làm thước đo, người có lòng tin trong sáng nơi phẩm hạnh» (matrix (23), ^4-172, wherever else).
9. **Keep:** dhammānusārī «người đi theo Giáo Pháp»; ^4-130 as is; diṭṭhippatto as is; M-10 (17) as is.
10. **^4-166:** remove the added «thấy»: «Ở đời này, về một người nào đó, có điều đáng khen và cũng có điều đáng chê.» (adapt to the segment's actual sentence; report the final wording).
11. **Small fixes:**
   - ^4-22 / matrix M-12 first person: «… và trong đó đạt đến sự toàn tri cùng sự làm chủ đối với các sức mạnh».
   - ^4-17: «… thì kiếp sẽ không bị thiêu hủy cho đến khi người này tự mình chứng nghiệm thành quả vào dòng.»
   - ^4-3 to ^4-8: «đi kèm với không hình sắc» → «đi kèm với cái không có hình sắc» (all six).
   - ^4-27, ^4-28 (and identical strings elsewhere, e.g. ^4-208): «Giáo Pháp do Như Lai tuyên bố» → «những điều do Như Lai tuyên bố» (adjust the verb agreement).
   - ^4-167: «Chư thiên Tha Hóa Tự Tại và chư thiên ở các cõi cao hơn …».
   - ^4-113, ^4-114, ^4-163 (and any identical anger string): «nằm sẵn nơi người ấy lâu dài suốt một thời gian dài» → «âm ỉ trong người ấy rất lâu» (negated: «không âm ỉ trong người ấy lâu»).
   - ^4-164, ^4-165: «các vị Phật và các đệ tử của các vị Phật» → «chư Phật và các đệ tử của Đức Phật».
   - ^4-181: «vị ấy» throughout the monk's sentence.
   - ^4-168: «ít thức ăn, thức uống và đồ ăn» → «ít lương thực, đồ uống và món ăn».
   - ^4-174: «xuống nước đến lần thứ ba vào buổi chiều» → «xuống nước ba lần mỗi ngày, lần thứ ba vào buổi chiều».
   - ^4-93: «Vì sự mong cầu được giải thoát mà người ấy từng có trước đây, khi chưa được giải thoát, nay đã lắng xuống.»
   - ^4-98, ^4-99: «vì một chút lợi lộc vật chất nhỏ nhặt» → «vì chút lợi lộc vật chất».
   - ^4-62: «cách cấu tạo câu chữ cần xem xét» → «cách cấu tạo của từ này cần được xem xét».
   - ^4-94: put the result first: «… chỉ khỏi bệnh ấy khi có được thức ăn thích hợp chứ không phải khi không có được, khi có được thuốc men … chứ không phải …, khi có được người chăm sóc … chứ không phải …» and the same order in the Tathāgata half («… chỉ bước vào sự cố định … khi có được dịp thấy Như Lai …»); keep every clause.

## Method
1. Back up all chapter files to rails\backup-pre-review\.
2. Write rails\review_fixes_vi.py: exact string replacements (or per-segment regex anchored on the block ID), each rule with an asserted occurrence count, building from the backup so it can be re-run, logging to rails\review-fixes-log.tsv (file, block id, old, new, decision number). Do not rebuild chapters from their builders; list stale builder constants in review-fixes-notes.md.
3. Identical Pāli must still give identical Vietnamese: re-run `python -I -X utf8 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\consistency\find_divergences_vi.py 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\consistency\divergences-after-review.md` (expected: only the intended ch6 ^4-193 / ^4-198 «người ấy» / «vị ấy» sentence).

## Verify (all must pass, every chapter)
check_chapter_ids.py OK, dashcheck.py 0 mismatches, pi-1-vi-ai\verify_rails_vi.py OK (commands in vi-rails-brief.md); no «—», «:-», «….», «được được», «là là», «chánh niệm», «seed», double spaces; 0 remaining hits of the replaced strings. Termbase adherence over the folder: report before / after miss counts.

## Report (under 400 words, as text)
Lines changed per chapter and per decision; final wording for decisions 3, 8 and 10; checks; anything you could not apply or that needs the user.
