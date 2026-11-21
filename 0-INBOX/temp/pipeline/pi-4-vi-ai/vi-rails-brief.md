# Brief: RAILS Vietnamese translation, plain audience, pi-4 (Puggalapaññatti): ONE chapter

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8`.
- Write ONLY your chapter file AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters\<ch>.md, plus `build_rails_<N>_vi.py` and `notes-rails-<N>.md` (N = chapter number) in 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\. Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (the sample, its builder, vi-rails-formulas.md, other agents' chapters), never run git (not even git status), never write "seed" or "unseeded". No web. You cannot write report files for me: return your report as text.
- The user approved the rails sample (preamble, 1-matika, 2-ekakapuggalapannatti) on 2026-11-20. **Three agents work at the same time, one chapter each.** Copy the approved strings exactly; finished chapters of other agents (build_rails_<M>_vi.py, notes-rails-<M>.md, their chapter files) must be followed for identical Pāli.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- The Vietnamese zero-shot of THIS book: AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters\, pi-4-vietnamese-plain-zeroshot.md, and everything zero-shot in pi-4-vi-ai\ (build_*_vi.py and notes-*.md outside rails\, vi-zeroshot-*.md, make_terms_vi.py, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, grep_vi.py, check_nfc_vi.py, find_pi123_vi.py, merge_zeroshot_vi.py); the Vietnamese side of the keyword maps (pi-4-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-4-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- AI_translation\skills\rails-verse-translator.md; 0-INBOX\temp\pipeline\vietnamese-style.md.
- 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\vi-rails-formulas.md (approved: frames, headings, closers and EVERY person-type name) and the sample builder rails\build_rails_sample_vi.py (import READ-ONLY: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails"); import build_rails_sample_vi as S`; importing writes nothing). **S.NAME[pali] is the name of every person type: your definition headings, questions and quoted names MUST use exactly these strings.** The approved sample chapters AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters\1-matika.md, 2-ekakapuggalapannatti.md.
- Locked termbase: AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md and 0-INBOX\temp\pipeline\pi-4-vi-ai\termbase\APPROVED.md (jīvita «sự sống»; saṭho «người gian trá»; ñāti «người thân»; samanantarā «liền sau»; sampavaṅkatā «sự nghiêng về phía»; icchā «sự mong muốn»; aggo «hàng đầu»; gatiṃ «cõi tái sinh»; aṭṭhakathā «Chú giải»; ^4-176 narassa as written «của một người»), plus pi-1 / pi-2 / pi-3 APPROVED.md. Terms in citation form; add or drop «các» / «những», «có», «là», tense words as grammar needs; never swap in a synonym. If no sense fits, use the closest sibling entry and REPORT it.
- pi-1 / pi-2 / pi-3 Vietnamese rails for identical Pāli (AI_translation\vietnamese\pi-1/2/3-vietnamese-plain-rails_split_chapters\; rails\find_pi123_rails_vi.py prints the line for a Pāli pattern).
- Meaning and layout only: AI_translation\russian\pi-4-russian-plain-rails_split_chapters\<ch>.md, AI_translation\english\pi-4-english-plain.md (grep by block ID); 0-INBOX\temp\pipeline\pi-4\ru-rails-formulas.md.

## Approved frames (from the sample; copy exactly)
- «Katamo ca puggalo X?» = «Thế nào là X?»; «Idhekacco puggalo» = «Ở đời này, có người»; «– ayaṃ vuccati puggalo "X"» = «– người này được gọi là “X”» (plural «– những người này được gọi là “…”»; where the Pāli has no dash or quotes: «Người này được gọi là X.»).
- «Kathañca puggalo X hoti?» = «Người như thế nào là X?»; «Evaṃ puggalo X hoti.» = «Như vậy là X.».
- Questions about persons «… là những ai?», about things «… là gì?»; counted puggalā «hạng người».
- samannāgata «được trang bị» for qualities / «mang» for bad states; «So» = «vị ấy» for a monk, «người ấy» otherwise.
- Chapter heading «Định danh các hạng người theo nhóm N»; closer «Giải thích phân loại theo nhóm N.»; colophon (ch11) «Bộ “Định danh các hạng người” đã hoàn tất.».

## Source and output
- Source: AI_translation\pali\pi-4_split_chapters\<ch>.md. Output: AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters\<ch>.md.
- Build it with rails\build_rails_<N>_vi.py from fixed strings (importing S), so every repeat is byte-identical; the builder asserts every (pi-1) / (pi-2) / (pi-3) string it uses still occurs in those rails and every person name equals S.NAME.
- New recurring strings (similes, verses, frames not in the formulas file): notes-rails-<N>.md, "Pāli = tiếng Việt" per line.

## Rules
- Block IDs exact; headings keep their #-level; each segment has the source's number of non-empty lines; one blank line between segments.
- DASH RULE: "–" only where the Pāli has one, same count per line; no ":-". "…pe…" → "…" (never «….»). Questions end with "?" with a Vietnamese question word. Quotes “…” / ‘…’. Variant brackets as the sample.
- Translate the Pāli as written: no emendations, add nothing that is not in the Pāli; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- Similes and verses: each Pāli line one Vietnamese line.
- Readability for a plain reader; avoid «là là», «được được».

## Verify (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-4_split_chapters AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>
```
Termbase adherence: copy your chapter (Write tool) into rails\adh-<N>\ and run `python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-4-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\adh-<N>`; read misses with judgement and fix genuine ones.

## Report (under 300 words, as text)
Checks, segment count, adherence; new strings (notes file); reuse from the sample / pi-1 / pi-2 / pi-3 / other chapters; termbase misfits and gaps; unsure Pāli or slips.
