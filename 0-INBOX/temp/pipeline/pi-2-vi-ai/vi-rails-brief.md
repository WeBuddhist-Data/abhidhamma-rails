# Brief: RAILS Vietnamese translation, plain audience, pi-2 (Vibhaṅga): remaining chapters

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write any file from PowerShell, not even a temporary list), PowerShell for commands, `python -I -X utf8`.
- Write ONLY your own chapter files, plus helper scripts and notes named after your chapters in 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit other agents' files or any pi-1 file, never run git (not even git status), never write "seed" or "unseeded". You cannot write report files for me: return your report as text.
- Write long builders in several Write/Edit calls (one very long call can stall).

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups of Vietnamese Abhidhamma translations.
- The Vietnamese zero-shot of THIS book (translate FRESH from the Pāli): AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\, pi-2-vietnamese-plain-zeroshot.md, the zero-shot builders and notes in the pi-2-vi-ai folder itself (build_*_vi.py, notes-*.md, ch1-sample.md, vi-zeroshot-terms.md, harmonise files, backup-pre-harmonise\, divergences*.md), and the Vietnamese side of the keyword maps (pi-2-vi-ai\mapper-vi\*.mapped.md, pi-2-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\vietnamese-style.md: register, typography (“…” / ‘…’), the strict DASH RULE, structure, review lessons, core terms (sati = «sự tỉnh thức», never «chánh niệm»). The book is «Phân tích các hiện tượng».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Models of house style and shared passages:
  - **The approved Vietnamese pi-1 rails** (the Vibhaṅga's Abhidhamma and question sections repeat the Dhammasaṅgaṇī word for word: matrix items, mind-state definitions, synonym strings, jhāna formulas, matter lists): AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\ (1-matika.md has every triad and pair name), 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\vi-rails-formulas.md and its builders (build_rails_*_vi.py, constants; import them, never edit them; importing writes nothing). Where pi-2 has the same Pāli as pi-1, reuse the pi-1 Vietnamese unless the pi-2 termbase or a pi-2 user decision says otherwise; report each such difference. Find matches by grepping the Pāli in AI_translation\pali\pi-1_split_chapters\ and reading the same non-empty line in the pi-1 Vietnamese rails file.
  - For how a Vibhaṅga chapter is structured (meaning and layout only, never wording): the approved Russian pi-2 rails builders and notes for the same chapters (0-INBOX\temp\pipeline\pi-2-ru\rails\build_rails_<chapters>_ru.py, notes-<chapters>.md) and outputs (AI_translation\russian\pi-2-russian-plain-rails_split_chapters\<ch>.md); the English pi-2 rails (AI_translation\english\pi-2-english-plain-rails_split_chapters\<ch>.md, grep by block ID) for meaning.
  - Where any model disagrees with the pi-2 Vietnamese termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-2_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-19):** AI_translation\vietnamese\pi-2-pali-vietnamese-termbase-plain.md, `pali: {english tag: tiếng Việt; …}`, plus 0-INBOX\temp\pipeline\pi-2-vi-ai\termbase\APPROVED.md and 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md.
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Terms are in citation form: a noun term keeps its nominaliser where it stands as a noun; inside a compound phrase or as a modifier use the bare word; add or drop «các» / «những», «có», «là», tense words and classifiers as Vietnamese grammar needs. Never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **User decisions the text must follow (pi-2 APPROVED.md):**
  - Cross-book terms aligned to pi-1: cuti «sự chết»; kamyatā «sự mong muốn» (sādhukamyatā …); samāpatti «thành tựu thiền»; ānantarika «có quả không gián đoạn»; the jātā string «đã sinh ra, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra …» exactly as the approved sample has it (ch12 too).
  - ṭhiti: «sự ổn định» in the concentration string, «sự duy trì» for the persistence of wholesome states, «sự tồn tại» in the life (jīvita) string (^2-220 and every repeat).
  - ^2-511 «mokkhaṃ pāmokkhaṃ» in the pātimokkha definition: NOT «sự giải thoát». Check the Vibhaṅga aṭṭhakathā on this passage (1-SOURCES\Commentaries\pi-vibhanga-atthakatha.md; grep "pāmokkh" / "mokkhan") and render it as 'chief, foremost' in our own plain words; report what you wrote and the commentary line you relied on.
  - ^2-1023 koṭi: counts converted to millions («triệu»), with the arithmetic exact.
  - Earlier pi-2 decisions: N-vidhena «theo nhóm N» (without «phân loại»); counted questions «… là những gì?»; rajataṃ «đồng tiền» vs sajjha «bạc»; vatthu «chỗ dựa»; Catukkaṃ / Pañcakaṃ «phương pháp chia bốn / năm» (jhāna method, ch12) vs «phân loại theo nhóm bốn / năm» (classification, ch16–17); the nāma/rūpa pair «phần tinh thần / phần vật chất»; kāmadhātu «yếu tố dục lạc» (element, ch3) vs «cõi dục lạc» (plane, ch18).
- **Translate the Pāli as written (user rule):** no emendations; only plain spelling slips and missing punctuation may be rendered as meant. A wrong punctuation mark, a doubled or missing negation, or a one-letter slip that changes the meaning stays as written. Known cases: ^2-171 doubled negation (literal); ^2-485, ^2-641, ^2-1031 missing negation; ^2-809 «atthato» (render atthato, 'in meaning', as written); ^2-957, ^2-1014, ^2-1023 questions closed with «.» (keep «.»); ^2-919 comma; ^2-1039 dukkhamasukhāya; ^2-1041 stray «4». Report any other suspected slip.
- **The approved sample (user-approved 2026-11-19): the model for everything.**
  - AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\preamble.md (done; do not rewrite it).
  - 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\sample-1\1-sample.md: chapter 1 through ^2-33.
  - 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\vi-rails-formulas.md (READ-ONLY): every string in it is binding; copy it verbatim (the 18 chapter headings, the section headings, the aggregate definition frames, the N-vidhena lines). rails\build_rails_sample_vi.py holds the same strings as Python constants: import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\rails"); import build_rails_sample_vi as S`) instead of retyping them. Never edit it; importing writes nothing.
  - Terms the termbase lacks, as built in the sample (reuse them): bhūta «đã trở thành»; the negated time words («chưa sinh ra», «chưa phát sinh» …); niyaka «cố hữu»; hīnasammataṃ / paṇītasammataṃ «được công nhận là thấp kém / ưu việt»; anāsanne / āsanne «(không) ở sát bên»; avidūre «không ở xa»; anupakaṭṭhe «không cận kề»; asantike «không ở gần»; ablative viññāṇā «so với thức …».
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** a builder script with fixed formula strings guarantees identical Vietnamese for identical Pāli. The Vibhaṅga is extremely repetitive (the three methods of each chapter, the question sections, the -pe- runs): build your chapters with one (rails\build_rails_<chapters>_vi.py).
- Any NEW recurring formula goes in rails\notes-<chapters>.md ("Pāli = tiếng Việt", one per line), not in the formulas file.
- **The chapter groups run ONE AT A TIME (user), in book order.** Before you start, read the finished earlier groups' rails builders and notes (rails\build_rails_*_vi.py, rails\notes-*.md) and their output chapters: the same Pāli must get the same Vietnamese, so import or copy their strings (never edit their files; importing must not rewrite their outputs). Where your chapter repeats a passage an earlier rails chapter (pi-2 or pi-1) already has, reuse that Vietnamese exactly.

## Output
AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\<ch>.md (the folder exists). 1-khandhavibhango.md only: its first 77 non-empty Pāli lines (^2-1-0 … ^2-33) are the approved sample; reuse rails\sample-1\1-sample.md byte-for-byte as the start of the file and continue from the next segment.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order (including any odd IDs such as ^2-U…).
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines; one blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…" (never «….»). Statements end with ".". Questions end with "?" and use a Vietnamese question word. Quotes “…” / ‘…’.
- **Brackets:** "[khác chính tả (Sī.): …]" for spelling-only variants, "[dị bản (…): …]" otherwise; (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Translate editorial notes. Follow the sample and the pi-1 Vietnamese rails for the exact bracket wording.
- **Formulas:** identical Pāli gets identical Vietnamese; where two segments differ only by a variant bracket or a numeral, the Vietnamese differs only there.
- **Readability for a plain reader:** the long lists and -pe- runs must read as natural Vietnamese sentences; recast where a literal string reads badly, keeping every term. Avoid a doubled «là».

## Verify each chapter (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py AI_translation\pali\pi-2_split_chapters\<ch>.md AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\<ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py AI_translation\pali\pi-2_split_chapters\<ch>.md AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\<ch>.md
```
1-khandhavibhango only: the file starts with the sample byte-for-byte. Then termbase adherence (checks the segments present in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-2-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-2-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters
```
Fix genuine misses in your chapters; gapped phrases, the nominaliser and classifiers cause false misses, so read them with judgement.

## Final report (short, as text, under 350 words)
- Per chapter: checks passed, segment count, adherence result for your chapters.
- New formulas (also in your notes file).
- Strings reused from pi-1 and any place where the pi-2 termbase made you differ from pi-1.
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Unsure Pāli or source slips.
