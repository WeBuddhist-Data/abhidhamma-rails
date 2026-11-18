# Brief: RAILS Vietnamese translation, plain audience, pi-1 (Dhammasaṅgaṇī): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`.
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git (not even git status), never write "seed" or "unseeded". You cannot write report files for me: return your report as text.
- This sample is what the user reviews before the rest of the book is translated. It sets every sentence formula the later agents will copy.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups of Vietnamese Abhidhamma translations.
- The Vietnamese zero-shot of this book (translate FRESH from the Pāli): AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters\, pi-1-vietnamese-plain-zeroshot.md, the zero-shot builders and notes in pi-1-vi-ai\ (build_*_vi.py, notes-*.md, ch2-01-sample.md, vi-zeroshot-terms.md, harmonise files, backup-pre-harmonise\), and the Vietnamese side of the keyword maps (mapper-vi\*.mapped.md, the assembled pi-1-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\vietnamese-style.md: register, typography (“…” / ‘…’), the strict DASH RULE, structure, review lessons, core terms (sati = «sự tỉnh thức», never «chánh niệm»). The book title is «Liệt kê các hiện tượng».
- Models of structure and shared passages (meaning and layout only, never wording): the approved Russian pi-1 rails sample, 0-INBOX\temp\pipeline\pi-1-ru\rails\ru-rails-formulas.md and build_rails_sample_ru.py, with its outputs AI_translation\russian\pi-1-russian-plain-rails_split_chapters\preamble.md and 1-matika.md; the English pi-1 rails translation (3-TRANSFORMATIONS\Translations\en-Contemporary-English-Abhidhamma\en-dhammasangani-ai.md; grep it by block ID) for meaning.

## Inputs
- **Source:** AI_translation\pali\pi-1_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-18):** AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md, `pali: {english tag: tiếng Việt; …}`, plus 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md (user decisions: bodily pain dukkha = «khó chịu»; sukha split into «hạnh phúc» (jhāna factor) vs «dễ chịu» (pleasant feeling); vāro «mục» vs bhāṇavāra «phần»; the citation-form rule).
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Terms are in citation form: a noun term keeps its nominaliser where it stands as a noun («sự tỉnh thức»); inside a compound phrase or as a modifier use the bare word («năng lực tỉnh thức», «tỉnh thức đúng đắn»); add or drop «các» / «những», «có», «là», tense words as Vietnamese grammar needs. Never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\preamble.md (source preamble.md; create the folder).
2. AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\1-matika.md: the whole matrix. It fixes every triad and pair name; chapters 3–5 will reuse them verbatim in their question and answer frames (Katame dhammā X? / ime dhammā X).
3. 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\sample-2-01\2-01-sample.md: chapter 2 from its start through ^1-57 (the first 122 non-empty Pāli lines; the Pāli slice is in 0-INBOX\temp\pipeline\pi-1-ru\ref\ch2-01-pali-1-122.md).
4. 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\vi-rails-formulas.md: every recurring sentence formula and fixed string (the matrix items with their question/answer forms, the «tasmiṃ samaye … hoti» frames, the factor names, every synonym string of ^1-1 … ^1-57, the closing line, the chapter headings for chapters 2–5) as "Pāli = tiếng Việt", one per line. It becomes binding for the later agents.
5. 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\build_rails_sample_vi.py: builds 1–3 from fixed formula strings (Python constants the later agents can import; importing must not rewrite outputs: guard with `if __name__ == "__main__":`).

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-". The Pāli of chapter 2 has "–" before «ime dhammā kusalā» / «ayaṃ tasmiṃ samaye …»: keep exactly that one.
- **Punctuation:** "…pe…" becomes "…" (never «….»). Statements end with ".". Questions end with "?" and use a Vietnamese question word (gì, nào …). Quotes “…” / ‘…’.
- **Brackets:** "[khác chính tả (Sī.): …]" for spelling-only variants, "[dị bản (…): …]" otherwise; (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Translate editorial notes.
- **Translate the Pāli as written** (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Vietnamese.
- **Readability for a plain reader:** the long lists and -pe- runs must read as natural Vietnamese sentences. Never leave a term sitting ungrammatically; recast a sentence where a literal string reads badly, while keeping every term. Avoid doubled «là» («đây là … là …»).

## Verify (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters 1-matika.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>     (preamble, 1-matika, and pi-1-ru\ref\ch2-01-pali-1-122.md vs rails\sample-2-01\2-01-sample.md)
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese> [<pali> <vietnamese> …]     (the same three pairs)
```
Then termbase adherence for the matrix (it checks the segments in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-1-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters
```
and the same for the 2-01 sample (copy it into a scratch folder under pi-1-vi-ai\rails\ named 2-01-cittuppadakandam.md to run the tool on it). Read the misses with judgement (gapped phrases and the nominaliser cause false misses) and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10–15 key formulas as "Pāli = tiếng Việt" (the kusala question/answer frame, «tasmiṃ samaye … hoti», a factor definition, a triad name, a dyad name, the closing line).
- Termbase misfits (term, segment, why it does not fit, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
