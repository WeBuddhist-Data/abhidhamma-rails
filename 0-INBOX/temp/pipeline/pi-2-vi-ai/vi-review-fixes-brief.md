# Brief: apply the review fixes, pi-2 Vietnamese plain rails

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8`. Write ONLY: the 19 chapter files in AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\ (through your fix script only) and files in 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\ named review_fixes_* / review-fixes-*. Nothing at the repo root; never run git; never write "seed". Do not touch 1-SOURCES\ or 4-SYSTEM\.

## FORBIDDEN
- The copyrighted Tịnh Sự translation (1-SOURCES\Translations\Vietnamese\ any file, 0-INBOX\raw-data\vi-*, the pi-N-vi alignment folders, vi-tools\): do not open it. All fixes are in our own words.
- The pi-2 Vietnamese zero-shot and the Vietnamese side of the keyword maps.

## Inputs
- The review findings (coordinator summaries in our own words): 0-INBOX\temp\pipeline\pi-2-vi-ai\review\findings-r1.md … findings-r7.md.
- The Pāli: AI_translation\pali\pi-2_split_chapters\; the approved pi-1 Vietnamese: AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\ (for the pi-1 drift fixes, copy pi-1 verbatim); the commentary 1-SOURCES\Commentaries\pi-vibhanga-atthakatha.md where a fix rests on it.
- Style: 0-INBOX\temp\pipeline\vietnamese-style.md (DASH RULE: no new «–»; “…” / ‘…’; sati «sự tỉnh thức»).

## Method (as pi-1)
Write rails\review_fixes_vi.py: fixed old → new strings, each rule scoped to the Vietnamese line(s) of the given block ID (non-empty line i of the Vietnamese ↔ line i of the Pāli). Back up the pre-fix chapter files once to rails\backup-pre-review\ and always start from the backup (rerunnable); log every replacement to rails\review-fixes-log.tsv (rule, file, ID, line, old, new); support --dry. Every rule must match exactly the number of times you expect (assert), so nothing is silently skipped. Do NOT rerun the rails builders; record in rails\review-fixes-notes.md which builder constants would need the same change. Write the script in several Write/Edit steps.

## What to apply (user decisions 2026-11-20 included)
APPLY every item marked CRITICAL, MAJOR and MINOR "(fix)" in findings-r1…r7, with these decisions:
1. **Scope pattern (all chapters):** a predicate with no count of its own is restated with the whole set («Năm khối …», «cả mười hai lĩnh vực đều …», «Cả bốn trạng thái …», «Cả bốn tầng thiền …», «Cả bốn loại hiểu biết thông suốt đều …» …), and «ba loại còn lại / hai loại còn lại» at ^2-749. Use one pattern book-wide; keep line counts.
2. **^2-809 atthato:** KEEP as written (user). No change.
3. **Source slips** ^2-803, ^2-749 asaṃkilesikā, ^2-187, ^2-245: KEEP as written (user); only at ^2-803 replace the wrong «Giáo Pháp» with a neutral «người đang có các hiện tượng ấy» (or the closest plain wording that keeps «Dhammasamaṅgissa» as written).
4. **Chapter 16 terms (user: follow the commentary):** dhamme ñāṇaṃ in the path-knowledge set (^2-754 (4), ^2-796 (a)(b)(d) and every repeat in ch16) = «sự hiểu biết về chân lý» («Bằng chân lý này, đã được biết …», «Ngoại trừ sự hiểu biết về chân lý …»); ñāṇavatthu = «loại hiểu biết»: «Các loại hiểu biết theo nhóm N –», «Như vậy là các loại hiểu biết theo nhóm N», «bảy mươi bảy loại hiểu biết», «bốn mươi bốn loại hiểu biết» (check every occurrence, incl. ch16 headings and ch6/ch17 if present). The ch15 formula «hiểu biết thông suốt về các hiện tượng» and ^2-724 «Giáo Pháp» stay.
5. **kamyatā (user):** «sự mong muốn không …»: ^2-934, ^2-834 (33), the heading ^2-17-4-51-0, ^2-U26 and the matrix lines: «sự mong muốn không thấy, sự mong muốn không nhìn, sự mong muốn không đến gần, sự mong muốn không hội họp với …», «sự mong muốn không nghe …» (all four of that set), titles likewise; ^2-862 cāṭukamyatā «sự mong muốn nịnh bợ».
6. **^2-830 bhonto** is nominative, agreeing with sattā (not an address): «Quả thật, những chúng sinh đáng kính này …» and «Hoặc những chúng sinh đáng kính này …» (drop «thưa các ngài»).
7. **^2-511:** keep «điều cao nhất, điều đứng đầu»; the tail becomes «… cho việc đạt được các hiện tượng thiện».
8. **pi-1 drift** (^2-182, ^2-181 «bao gồm cả», ^2-517, ^2-518, ^2-905, ^2-U24): copy the pi-1 Vietnamese of the identical Pāli verbatim, keeping only what the pi-2 Pāli itself adds (quote marks, variant brackets).
9. **«maccu maraṇaṃ»** (ch4 ^2-193, ch6 ^2-236 and any repeat): one item; drop the doubled «sự chết»: «…, sự tử vong, sự qua đời, …». Check pi-1's maraṇa string first: if pi-1 has the same Pāli, match pi-1.
10. **Missing quotes after «đó được gọi là»** (r3 list): add “…” (missing punctuation, user rule).
11. **r1 ^2-11…31** samāpanna: «của người không ở trong thành tựu thiền / của người đang ở trong thành tựu thiền».
12. **Not applied (keep):** r1 ^2-153 quote marks around B (as the Pāli prints them); r1 colon-list and «;»-chain options (pi-1 pattern); the book-wide naming of subjects in all question-section answers (only the subset-adjacent ones under 1); ^2-187 body-consciousness «dễ chịu» (user rule); ^2-433 / ^2-220 vīriya ṭhiti «sự ổn định»; ^2-434 iddhi «thần thông»; ^2-711 «trung bình, ưu việt»; ^2-974 (7) «Tôi sẽ là»; matrix heading «bộ đôi …» vs «nhóm» option; ^2-1043 «…»; Tāvatiṃsa «Ba Mươi Ba»; ^2-365 option.
13. Where a findings fix says «optional» and is not listed under 12, apply it only if it is a plain clarity gain that adds no word without Pāli support; list what you applied and skipped.
14. Keep identical Pāli = identical Vietnamese: when you change a formula, change every occurrence of the same Pāli in all 19 files (search the Pāli to find them).

## Verify (all must pass)
For all 19 files: check_chapter_ids.py, dashcheck.py (0 mismatches, 0 extra), pi-1-vi-ai\verify_rails_vi.py; termbase_adherence_vi.py on the folder (report the new miss count; misses caused by decisions 4 and 5 are expected); grep for «—», «:-», «chánh niệm», «seed», «….», «thưa các ngài», «chỗ dựa của sự hiểu biết», «sự hiểu biết về Giáo Pháp».

## Report (as text, under 450 words)
Rules applied (count per rule and file), any finding you could not apply and why, optional items applied/skipped, the builder constants affected, the termbase headwords whose approved term the decisions 4/5/6 now override (so the coordinator can record them), check results.
