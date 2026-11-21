# Brief: RAILS Vietnamese translation, plain audience, pi-4 (Puggalapaññatti): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8`.
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\. Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 / pi-2 / pi-3 file, never run git (not even git status), never write "seed" or "unseeded". No web. You cannot write report files for me: return your report as text.
- This sample (preamble, 1-matika, 2-ekakapuggalapannatti) is what the user reviews before the rest of the book is translated (three agents at a time, one chapter each). It sets every sentence formula and every person-type name the later agents will copy.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- The Vietnamese zero-shot of THIS book (translate FRESH from the Pāli): AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters\, pi-4-vietnamese-plain-zeroshot.md, and everything zero-shot in pi-4-vi-ai\ (build_*_vi.py, notes-*.md, vi-zeroshot-*.md, make_terms_vi.py, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, grep_vi.py, check_nfc_vi.py, find_pi123_vi.py, merge_zeroshot_vi.py); the Vietnamese side of the keyword maps (pi-4-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-4-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\vietnamese-style.md: register, typography (“…” / ‘…’), the strict DASH RULE, structure, review lessons, core terms (sati = «sự tỉnh thức», never «chánh niệm»).
- **The approved Vietnamese pi-1, pi-2 and pi-3 rails** (user-approved and reviewed): AI_translation\vietnamese\pi-1-…, pi-2-…, pi-3-vietnamese-plain-rails_split_chapters\ (the lists: aggregates, bases, elements, truths, faculties; jhāna, vimokkha, path / fruit phrases, sīla strings), and their formula files 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\vi-rails-formulas.md, pi-2-vi-ai\rails\vi-rails-formulas.md, pi-3-vi-ai\rails\vi-rails-formulas.md. Where pi-4 has the same Pāli as pi-1 / pi-2 / pi-3, reuse their Vietnamese unless the pi-4 termbase decides otherwise; report each difference. Find matches by grepping the Pāli in AI_translation\pali\pi-N_split_chapters\ and reading the same non-empty line in the Vietnamese rails file (0-INBOX\temp\pipeline\pi-3-vi-ai\rails\find_pi12_vi.py shows a lookup method; write a copy covering pi-1/2/3 in pi-4-vi-ai\rails\).
- For meaning and layout only (never wording): the Russian pi-4 rails AI_translation\russian\pi-4-russian-plain-rails_split_chapters\<ch>.md and 0-INBOX\temp\pipeline\pi-4\ru-rails-formulas.md; the English pi-4 rails AI_translation\english\pi-4-english-plain.md (grep by block ID).
- Where any model disagrees with the pi-4 Vietnamese termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-4_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-20):** AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md, `pali: {english tag: tiếng Việt; …}`, plus 0-INBOX\temp\pipeline\pi-4-vi-ai\termbase\APPROVED.md (the user's decisions: jīvita «sự sống»; saṭho «người gian trá»; ñāti «người thân»; samanantarā «liền sau»; sampavaṅkatā «sự nghiêng về phía»; icchā «sự mong muốn»; aggo «hàng đầu»; gatiṃ «cõi tái sinh»; aṭṭhakathā «Chú giải»; ^4-176 narassa as written) and the pi-1 / pi-2 / pi-3 decisions in their termbase\APPROVED.md.
  - Look up each Pāli word; pick the sense by its tag. Person-type names have their own entries (with the head noun «người» / «bậc»): use them exactly, in the matrix, in the definition heading / question and in the quoted name. A compound without an entry is built from its members' entries.
  - Terms are in citation form: a noun keeps its nominaliser where it stands as a noun; inside a phrase or as a modifier use the bare word; add or drop «các» / «những», «có», «là», «điều», tense words and classifiers as Vietnamese grammar needs. Never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Approved book frame and headings (user, 2026-11-20; copy verbatim):**
  - Homage «Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn»; `# Abhidhammapiṭake` = «# Tạng Vi Diệu Pháp»; `## Puggalapaññattipāḷi` = «## Định danh các hạng người»; colophon «Bộ “Định danh các hạng người” đã hoàn tất.».
  - `### Mātikā` «### Ma trận»; `#### Ekakauddeso … Dasakauddeso` «#### Phần nêu đề mục theo nhóm một … mười»; matrix group closers Ekakaṃ … «Phân loại theo nhóm một.» …; `### Niddeso` «### Phần giải thích»; `#### Ekakapuggalapaññatti … Dasakapuggalapaññatti` «#### Định danh các hạng người theo nhóm một … mười»; chapter closers Ekakaniddeso … «Giải thích phân loại theo nhóm một.» ….
  - Frames: «Kittāvatā X-ānaṃ X-paññatti?» = «Sự định danh về {X} bao quát đến mức nào?»; «Yāvatā …; ettāvatā …» answered in the same pattern; «Katamo ca puggalo X?» = «Thế nào là X?»; «Idhekacco puggalo» = «Ở đời này, có người»; «– ayaṃ vuccati puggalo "X"» = «– người này được gọi là “X”»; plural «– những người này được gọi là “…”»; Kathañca puggalo X hoti? = «Người như thế nào là X?», Evaṃ … = «Như vậy là X.»; questions about persons «… là những ai?», about things «… là gì?». puggalā counted = «hạng người».
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters\preamble.md, 1-matika.md, 2-ekakapuggalapannatti.md (create the folder).
2. 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\vi-rails-formulas.md: every recurring frame and fixed string of the sample ("Pāli = tiếng Việt", one per line) AND the full list of person-type names of the matrix (every group, ekaka … dasaka) as they now read, which chapters 3-11 must use verbatim. Mark each string taken unchanged from pi-1 / pi-2 / pi-3 rails with "(pi-1)" / "(pi-2)" / "(pi-3)".
3. 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\build_rails_sample_vi.py: builds 1 from fixed strings exposed as constants (NAME[pali] for every person type; the frames; headings; closers) that later agents import; importing must not rewrite outputs (`if __name__ == "__main__":`). It asserts at build time that every (pi-1) / (pi-2) / (pi-3) string still occurs in those rails files.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order. **Headings:** keep their #-level. **Segments:** the source's number of non-empty lines; one blank line between segments.
- **DASH RULE (user):** "–" only where the Pāli has "–", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…" (never «….»). Statements end with "."; questions with "?" and a Vietnamese question word. Quotes “…” / ‘…’.
- **Brackets:** "[khác chính tả (Sī.): …]" for spelling-only variants, "[dị bản (…): …]" otherwise, as the pi-1 / pi-2 rails word them.
- **Translate the Pāli as written** (user rule): no emendations, add nothing; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Vietnamese, within the sample and with the pi-1 / pi-2 / pi-3 Vietnamese rails.
- **Readability for a plain reader:** natural Vietnamese; recast where a literal string reads badly, keeping every term. Avoid a doubled «là».

## Verify (all must pass)
For preamble.md, 1-matika.md, 2-ekakapuggalapannatti.md:
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-4_split_chapters AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters <file>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese>
```
Then termbase adherence:
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-4-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters
```
Read the misses with judgement and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10-15 key formulas and 15 person names as "Pāli = tiếng Việt".
- Strings reused from pi-1 / pi-2 / pi-3 rails and any place where the pi-4 termbase made you differ.
- Termbase misfits (term, segment, why, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
