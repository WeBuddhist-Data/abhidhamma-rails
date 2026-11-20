# Brief: Vietnamese zero-shot of pi-2 (Vibhaṅga), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY the files named below plus helper scripts in 0-INBOX\temp\pipeline\pi-2-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git (not even git status), never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

This is the SAMPLE the user reviews before the rest of the book is translated by other agents, who will copy your formulas verbatim. Be careful, exact and consistent.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups of Vietnamese Abhidhamma translations. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\ (search only the specific files named here). Our wording must be our own.

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, the strict DASH RULE, “…” / ‘…’, core terms (sati = «sự tỉnh thức», never «chánh niệm»), review lessons, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Vietnamese (user-approved and reviewed):** pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng») is finished in Vietnamese. The Vibhaṅga reuses its formulas heavily: the matrix triads and dyads, the aggregate definitions, the synonym strings, the matter classifications, the question/answer frames. **Where the Pāli is identical or nearly identical to pi-1, reuse the pi-1 Vietnamese wording.** Sources, in order:
  1. AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\ (the final, reviewed text; 1-matika.md has every matrix item, 3-0x-rupakandam.md the matter classifications). Find matches by grepping the Pāli in AI_translation\pali\pi-1_split_chapters\ and reading the same line in the pi-1 Vietnamese rails file (non-empty lines align one to one).
  2. AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md and 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md (the user's decisions: bodily pain «khó chịu»; sukha «hạnh phúc» (jhāna factor) vs «dễ chịu» (pleasant feeling); vāra «mục» vs bhāṇavāra «phần»; ajjhatta «ở nơi bản thân»; vaṇṇanibhā «ánh màu»; asuropo «sự nói năng cộc cằn»; cittahetuka «có tâm làm nguyên nhân»; the citation-form rule).
  3. 0-INBOX\temp\pipeline\pi-1-vi-ai\vi-core-terms.md (the approved cross-book core terms).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English rails translation AI_translation\english\pi-2-english-plain-rails_split_chapters\<part>.md and the Russian one AI_translation\russian\pi-2-russian-plain-rails_split_chapters\<part>.md (same segments and lines); the Russian pi-2 sample builder and term list of the same scope: 0-INBOX\temp\pipeline\pi-2-ru\build_ch1_sample_ru.py, pi-2-ru\ru-zeroshot-terms.md (its chapter-title list shows the book's structure).

## Source and output
- Source: AI_translation\pali\pi-2_split_chapters\preamble.md and 1-khandhavibhango.md.
- Write:
  1. AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\preamble.md (whole file; create the folder).
  2. 0-INBOX\temp\pipeline\pi-2-vi-ai\ch1-sample.md: the Vietnamese of the Pāli slice 0-INBOX\temp\pipeline\pi-2-vi-ai\ch1-sample-pali.md (the first 77 non-empty lines of 1-khandhavibhango.md, from `### Khandhavibhaṅgo ^2-1-0` to the line before `##### Vedanākkhandho ^2-1-2-2-0`), with the same blank lines. The agent who finishes chapter 1 later reuses it byte for byte.
  3. 0-INBOX\temp\pipeline\pi-2-vi-ai\build_ch1_sample_vi.py: a builder with fixed formula strings (constants other agents can import: aggregate names, the past/future/present … strings, question/answer frames, classification frames). Importing it must not rewrite outputs (guard with `if __name__ == "__main__":`).
  4. 0-INBOX\temp\pipeline\pi-2-vi-ai\vi-zeroshot-terms.md: every formula and key term you settled, "Pāli = tiếng Việt", one per line, grouped (book frame, chapter and section headings, aggregate formulas, classification frames, terms). Mark which come from pi-1 Vietnamese and which are new.
- **Book and chapter titles:** propose the Vietnamese title of the book (Vibhaṅgapāḷi) and Vietnamese headings for ALL 18 chapters (Khandhavibhaṅga … Dhammahadayavibhaṅga) and the recurring section headings (Suttantabhājanīya, Abhidhammabhājanīya, Pañhāpucchaka) in the terms file. Vietnamese only, no Pāli name and no bracketed gloss (vietnamese-style.md "Book titles"). Give one or two alternatives for the book title. The pi-1 title is «Liệt kê các hiện tượng»; the pi-1 headings use the pattern «Phần về …».

## Rules
- Identical Pāli = identical Vietnamese, within the sample and with pi-1 Vietnamese.
- Core: dhamma = hiện tượng; abyākata = không xác định về mặt đạo đức; kusala/akusala = thiện/bất thiện; khandha = khối; rūpa = vật chất (visible form = hình sắc); saṅkhāra (aggregate) = tạo tác; vedanā = cảm giác; saññā = tri giác; viññāṇa = thức; mātikā = ma trận.
- No notes or commentary of your own inside the translation. Variant brackets "[khác chính tả (Sī., Syā.): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…" (never «….»). (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Digits stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line); no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- Translate the Pāli as written (user rule): no emendations; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.

## Verify (all must pass before you report)
- preamble: `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters preamble.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>` for the preamble and for (ch1-sample-pali.md, ch1-sample.md): equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py 0-INBOX\temp\pipeline\pi-2-vi-ai\ch1-sample-pali.md 0-INBOX\temp\pipeline\pi-2-vi-ai\ch1-sample.md` (IDs, line counts, NFC, foreign letters, «chánh niệm») and the same for the preamble pair.

## Report (under 450 words, as text)
- Checks passed, segment count.
- The proposed book title (with alternatives) and the chapter/section headings.
- Key formulas and terms, and which were reused from pi-1 Vietnamese.
- Pāli you were unsure about or that looks like a source slip (translated as written).
