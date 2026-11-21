# Brief: pi-5 Vietnamese rails CONSISTENCY PASS (coordinator-delegated, 2026-11-21)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write a file from PowerShell), PowerShell for commands, `python -I -X utf8 -B`. LF line endings: open(..., "w", encoding="utf-8", newline="\n").
- All 31 rails chapters + preamble are finished in AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\ and pass the checks. Your job: make identical Pāli read identically across the chapters, by the precedence below, WITHOUT changing anything else.
- Write ONLY: 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\consistency_fix_vi.py, rails\consistency\ (pre-fix copies of every chapter you change, made once, never overwritten), rails\consistency-log.tsv (file, block id, old → new, reason), rails\consistency-notes.md, and the changed chapter files. Do NOT edit any build_rails_*.py, notes-rails-*.md, vi-rails-formulas.md, rails-coordinator-rules.md, the termbase, or anything outside these. Never run git. Never write "seed". No web. No files at the repo root. Return your report as text.

## FORBIDDEN (strict)
- Never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- Never open this book's Vietnamese zero-shot: AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters\, pi-5-vietnamese-plain-zeroshot.md, pi-5-vi-ai\backup-pre-harmonise\, pi-5-vi-ai\divergences*.md (the zero-shot report; rails\divergences-rails.md is the RAILS report and is allowed), harmonise*, and the Vietnamese side of the keyword map (pi-5-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-5-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only single named files.

## Inputs (allowed)
- rails\divergences-rails.md: the scan of the rails chapters (identical Pāli → differing Vietnamese: (a2) lines, (a3) sentences, (a4) members, (b) brackets, (d) kathā heading vs closing line, (c) recurring terms). Re-run it any time: `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\consistency_find_vi.py`.
- The rails chapters, rails\build_rails_<N>_vi.py and notes-rails-<N>.md (to see why a chapter chose a wording), vi-rails-formulas.md, rails-coordinator-rules.md, vi-rails-brief.md (pi-5-vi-ai\), the termbase AI_translation\vietnamese\pi-5-pali-vietnamese-termbase-plain.md and pi-5-vi-ai\termbase\APPROVED.md, pi-1 … pi-4 rails (rails\find_pi1234r_vi.py), the Pāli chapters, the commentary 1-SOURCES\Commentaries\pi-kathavatthu-atthakatha.md (Pāli).

## Precedence (where identical Pāli differs)
1. The termbase / APPROVED.md (user-approved) decides a term.
2. pi-1 … pi-4 rails wording for that Pāli.
3. The approved sample (preamble, 1-puggalakatha) and vi-rails-formulas.md.
4. The earlier chapter.
Only where the Pāli is truly identical AND the meaning in context is the same. Where the context differs (a different referent, person vs thing, a different sense), keep both and list it in the notes as "kept: context". Sentence-initial capitals are not divergences.

## Do NOT change (these are for the user's review decisions; list them in the notes as "left for the user")
- "Tassuddānaṃ –" after a fifty-group close = «Tóm tắt của nhóm này –» (ch18, ch23, ch28, ch31) vs «Tóm tắt của chương này –» after a vagga close.
- ch29 buddho tiṭṭhati / buddhā tiṭṭhanti «tồn tại».
- Any termbase-vs-chapter wording (that goes to the termbase alignment later).
- If a fix would change the approved sample (1-puggalakatha.md or preamble.md), do not change it: list it as "sample differs" with both wordings.

## Known clashes logged by the coordinator (check each; fix by the precedence or report why not)
1. "Nanu <name> bhagavantaṃ etadavoca –": sample «đã nói với Đức Thế Tôn điều này sao –» vs ch5 «… thế này sao –».
2. udā. citation: ch10 «Kinh Phật Tự Thuyết» vs ch13 «Phật Tự Thuyết».
3. uppajjati said of Buddhas arising in the world: ch21 «sinh khởi» vs ch3 / ch16 / pi-4 «xuất hiện».
4. Sutta quote opening "idha, bhikkhave …": lower case «“ở đây» (ch14, ch17 ^5-548) vs capitalised (sample, ch15, ch18, ch20, ch21, ch27).
5. "idha": «Ở đây» (ch23 and others) vs pi-4 «Ở đời này» (ch27): check whether the Pāli matches the pi-4 context.
6. Tāya / Tassa tasseva: ch19 «đối với từng cái như vậy» (a thing) vs ch15 ^5-501 / sample «từng người»: likely context, check.
7. Puṇṇa: ch22 «Pun-na» vs ch23 «Phú-lâu-na» (same person? check the Pāli context and pi-1 … pi-4).
8. The magga list question: «Có phải là …» (ch10, ch12, ch22) vs «Có phải đó là …» (ch11, ch23).
9. taṃ jīvaṃ taṃ sarīraṃ: pi-1 / ch22 / ch31 «Linh hồn và thân thể là một» vs the sample «linh hồn cũng chính là thân thể» (do not edit the sample: report).
10. samāpanno: ch26 «người đang nhập thành tựu thiền» vs ch19 «người đang nhập».
11. dhammappaṭisaraṇo: ch11 «về» (ch26 follows) vs ch13 «của».
12. kammaṃ karoti: ch22 «làm nghiệp» vs ch15 «tạo nghiệp».
13. The cetiya / gift list: ch25 vs ch21 ^5-658.
14. Fifty-group uddānas: their catchwords must use the wording of the kathā names they point to — ch18 ^5-604 (kathās of ch14-18), ch23 ^5-742 (ch19-23), ch28 (ch24-28), ch31 (ch29-31 «Mới, sự nhập Niết-bàn, cùng một ý định.», and the Paṇṇāsakuddānaṃ verse vs the fifty-group closes). Each vagga uddāna vs its own kathā names likewise.
15. Kathā names: heading vs closing line ("X niṭṭhitā.") vs uddāna, per kathā (section (d)).
- Plus every group in divergences-rails.md (a2)-(a4), (b), (c).

## Method
- consistency_fix_vi.py: explicit (file, old, new) replacements with asserted counts (as 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\consistency_fix_vi.py does), working from the pre-fix copies in rails\consistency\, so it can be re-run safely; it appends to consistency-log.tsv (rewrite it each run).
- After the fixes, run for EVERY chapter file (32 files incl. preamble):
  - `python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-5_split_chapters AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters <ch>.md`
  - `python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>`
  - `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>`
  - and re-run consistency_find_vi.py; every remaining group must be explained in consistency-notes.md ("kept: context", "left for the user", "sample differs", "not identical Pāli", "false hit").
- Rules stay in force: no "—" / "–" beyond the Pāli's dashes; no «….», «:-», «là là», «được được», «chánh niệm»; NFC; LF.

## Report (under 400 words, as text)
Number of changes per chapter; each known clash 1-15 and how it was settled; what is left for the user; checks.
