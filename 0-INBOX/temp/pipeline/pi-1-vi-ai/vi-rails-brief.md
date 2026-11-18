# Brief: RAILS Vietnamese translation, plain audience, pi-1 (Dhammasaṅgaṇī): remaining chapters

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`.
- Write ONLY your own chapter files, plus helper scripts and notes named after your chapters in 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit other agents' files, never run git (not even git status), never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups of Vietnamese Abhidhamma translations.
- The Vietnamese zero-shot of this book (translate FRESH from the Pāli): AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters\, pi-1-vietnamese-plain-zeroshot.md, the zero-shot builders and notes in pi-1-vi-ai\ itself (build_*_vi.py, notes-*.md, ch2-01-sample.md, vi-zeroshot-terms.md, harmonise files, backup-pre-harmonise\), and the Vietnamese side of the keyword maps (mapper-vi\*.mapped.md, pi-1-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\vietnamese-style.md: register, typography (“…” / ‘…’), the strict DASH RULE, structure, review lessons, core terms (sati = «sự tỉnh thức», never «chánh niệm»). The book is «Liệt kê các hiện tượng».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Models of structure and meaning only (never wording): the approved Russian pi-1 rails builders and notes for the same chapters (0-INBOX\temp\pipeline\pi-1-ru\rails\build_rails_<chapters>_ru.py, notes-<chapters>.md) and outputs (AI_translation\russian\pi-1-russian-plain-rails_split_chapters\<ch>.md); the English pi-1 rails (3-TRANSFORMATIONS\Translations\en-Contemporary-English-Abhidhamma\en-dhammasangani-ai.md, grep by block ID). Where they disagree with the Vietnamese termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-1_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-18):** AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md, `pali: {english tag: tiếng Việt; …}`, plus 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md (user decisions: bodily pain dukkha = «khó chịu», so dukkhasahagataṃ body-consciousness takes «khó chịu», never «sự đau khổ»; sukha split: jhāna factor «hạnh phúc» vs pleasant feeling, mental or bodily, «dễ chịu», so sukhasahagataṃ body-consciousness takes «dễ chịu»; vāro «mục» vs bhāṇavāra «phần»; ajjhatta family «ở nơi bản thân»; the citation-form rule).
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Terms are in citation form: a noun term keeps its nominaliser where it stands as a noun; inside a compound phrase or as a modifier use the bare word; add or drop «các» / «những», «có», «là», tense words as Vietnamese grammar needs. Never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **The approved sample (user-approved 2026-11-18): the model for everything.**
  - AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\preamble.md and 1-matika.md (done; do not rewrite them). 1-matika fixes every triad and pair name: chapters 3–5 reuse them verbatim in their question and answer frames («Những hiện tượng nào X?» / «– những hiện tượng này X.»).
  - 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\sample-2-01\2-01-sample.md: chapter 2 through ^1-57.
  - 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\vi-rails-formulas.md (READ-ONLY): every string in it is binding; copy it verbatim. rails\build_rails_sample_vi.py holds the same strings as Python constants: import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\rails"); import build_rails_sample_vi as S`) instead of retyping them. Never edit it; importing writes nothing.
  - Terms the termbase lacks, as built in the sample (reuse them): gocchaka «nhóm», saṃphusitattaṃ, byappanā, anuvicāro, upavicāro, paṭipassaddhi, paṭipassambhanā, the alubbhanā / asārajjanā / adussanā strings, the kāya- / citta- passaddhi … ujukatā series («… của thân tinh thần» / «… của tâm»); hoti = «có» / «là» as the sentence needs (the termbase's «còn tồn tại» belongs only to the views).
  - Source slips are translated as written (user): ^1-33 keeps the Pāli «?».
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** a builder script with fixed formula strings guarantees identical Vietnamese for identical Pāli. The Dhammasaṅgaṇī is extremely repetitive (synonym strings, jhāna formulas, the «samaye» lists, the -pe- runs): build your chapters with one (rails\build_rails_<chapters>_vi.py).
- Any NEW recurring formula goes in rails\notes-<chapters>.md ("Pāli = tiếng Việt", one per line), not in the formulas file.
- **The chapter groups run ONE AT A TIME (user), in book order.** Before you start, read the finished earlier groups' rails builders and notes (rails\build_rails_*_vi.py, rails\notes-*.md) and their output chapters: the same Pāli must get the same Vietnamese, so import or copy their strings (never edit their files; importing must not rewrite their outputs). Where your chapter repeats a passage an earlier rails chapter already has, reuse that Vietnamese exactly.

## Output
AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\<ch>.md (the folder exists). 2-01-cittuppadakandam.md only: its first 122 non-empty Pāli lines (^1-1-0 … ^1-57) are the approved sample; reuse rails\sample-2-01\2-01-sample.md byte-for-byte as the start of the file and continue from the next segment.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order (including any odd IDs such as ^1-U1).
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines; one blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…" (never «….»). Statements end with ".". Questions end with "?" and use a Vietnamese question word. Quotes “…” / ‘…’.
- **Brackets:** "[khác chính tả (Sī.): …]" for spelling-only variants, "[dị bản (…): …]" otherwise; (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Translate editorial notes.
- **Translate the Pāli as written** (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Vietnamese; where two segments differ only by a variant bracket or a numeral, the Vietnamese differs only there.
- **Readability for a plain reader:** the long lists and -pe- runs must read as natural Vietnamese sentences; recast where a literal string reads badly, keeping every term. Avoid doubled «là».

## Verify each chapter (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py AI_translation\pali\pi-1_split_chapters\<ch>.md AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\<ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py AI_translation\pali\pi-1_split_chapters\<ch>.md AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\<ch>.md
```
2-01 only: the file starts with the sample byte-for-byte. Then termbase adherence (checks the segments present in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-1-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters
```
Fix genuine misses in your chapters; gapped phrases and the nominaliser cause false misses, so read them with judgement.

## Final report (short, as text, under 350 words)
- Per chapter: checks passed, segment count, adherence result for your chapters.
- New formulas (also in your notes file).
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Unsure Pāli or source slips.
