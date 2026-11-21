# Brief: Vietnamese zero-shot of pi-3 (Dhātukathā), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY the files named below plus helper scripts in 0-INBOX\temp\pipeline\pi-3-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git (not even git status), never write "seed" or "unseeded" in any file you write. No web access. You cannot write report files for me: return your report as text.

This is the SAMPLE the user reviews before the rest of the book is translated by other agents (three at a time, one chapter each), who will copy your formulas verbatim. Be careful, exact and consistent.

The sample is the preamble, chapter 1 (1-uddeso.md, the matrices) AND chapter 2 (2-pathamanayo.md, the first method). Chapter 1 alone is only a list of headings; chapter 2 settles the saṅgaha / asaṅgaha question-and-answer frame that chapters 3-15 build on.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here. Our wording must be our own.

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, the strict DASH RULE, “…” / ‘…’, core terms (sati = «sự tỉnh thức», never «chánh niệm»), review lessons, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Vietnamese (user-approved and reviewed): pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng») and pi-2 (Vibhaṅga, «Phân tích các hiện tượng»).** The Dhātukathā's lists (5 aggregates, 12 bases, 18 elements, 4 truths, 22 faculties, dependent origination, satipaṭṭhāna … the seven mental factors) and its matrix items are already translated there. **Reuse that wording exactly.** Sources, in order:
  1. AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\ and AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\ (final reviewed text; find matches by grepping the Pāli in the same-named file of AI_translation\pali\pi-2_split_chapters\ or pi-1_split_chapters\ and reading the same non-empty line in the Vietnamese file). 0-INBOX\temp\pipeline\pi-2-vi-ai\pi1_lookup_vi.py shows the lookup method; adapt a copy for pi-2 in pi-3-vi-ai\ if useful.
  2. Termbases and the user's decisions: AI_translation\vietnamese\pi-2-pali-vietnamese-termbase-plain.md, AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md, 0-INBOX\temp\pipeline\pi-2-vi-ai\termbase\APPROVED.md, 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md, 0-INBOX\temp\pipeline\pi-1-vi-ai\vi-core-terms.md. Where pi-1 and pi-2 differ, pi-2's APPROVED.md says which wins (cross-book terms follow pi-1).
  3. 0-INBOX\temp\pipeline\pi-2-vi-ai\vi-zeroshot-terms.md (pi-2 chapter titles: the 18 vibhaṅga names and list frames).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** AI_translation\english\pi-3-english-plain.md and AI_translation\russian\pi-3-russian-plain-rails_split_chapters\<ch>.md (find segments by block ID); 0-INBOX\temp\pipeline\pi-3\ru-zeroshot-terms.md and ru-rails-formulas.md show the book's structure and formulas.

## Source and output
- Source: AI_translation\pali\pi-3_split_chapters\preamble.md, 1-uddeso.md, 2-pathamanayo.md.
- Write:
  1. AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters\preamble.md, 1-uddeso.md, 2-pathamanayo.md (whole files; create the folder).
  2. 0-INBOX\temp\pipeline\pi-3-vi-ai\build_sample_vi.py: a builder with fixed formula strings, exposed as constants other agents import (list-member names in every case form needed: khandha / āyatana / dhātu names, counts «một khối … mười tám yếu tố», the katihi … saṅgahito? / asaṅgahito? frames, the «na kehici …» frame, the (Ekamūlakaṃ.) … closing labels, section headings). Importing it must not rewrite outputs (guard with `if __name__ == "__main__":`). It must assert at build time that every string it claims to take from pi-1 / pi-2 still occurs in those rails files.
  3. 0-INBOX\temp\pipeline\pi-3-vi-ai\vi-zeroshot-terms.md: every formula and key term you settled, "Pāli = tiếng Việt", one per line, grouped (book frame, chapter and section headings, frames, list members, counts, terms). Mark which come from pi-1 / pi-2 Vietnamese and which are new.
- **Book and chapter titles:** propose the Vietnamese title of the book (Dhātukathāpāḷi; give one or two alternatives) and Vietnamese headings for ALL chapters (Uddeso, Paṭhamanayo … Cuddasamanayo; read the 15 chapter files' heading lines and their #### / ##### sub-headings) and the recurring sub-headings (Saṅgahāsaṅgahapadaniddeso, etc.) in the terms file. Vietnamese only, no Pāli name and no bracketed gloss (vietnamese-style.md "Book titles"). The pi-1 title is «Liệt kê các hiện tượng», pi-2 «Phân tích các hiện tượng».

## Rules
- Identical Pāli = identical Vietnamese, within the sample and with pi-1 / pi-2 Vietnamese.
- Core: dhamma = hiện tượng (the Teaching = Giáo Pháp); khandha = khối; āyatana = lĩnh vực nhận biết (as pi-2); dhātu = yếu tố; rūpa = vật chất (visible form = hình sắc); saṅkhāra (aggregate) = tạo tác; vedanā = cảm giác; saññā = tri giác; viññāṇa = thức; mātikā = ma trận. Pick one rendering each for saṅgahita / asaṅgahita, sampayutta / vippayutta (pi-1 has sampayutta «gắn liền với»; reuse it), sabhāga / visabhāga, and use it throughout.
- Numbers: a count word is required by the Pāli (ekena, ekādasahi …); write counts as Vietnamese words, consistently.
- No notes or commentary of your own inside the translation. Variant brackets "[khác chính tả (Sī., Syā.): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…" (never «….»). (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Digits and (1) (2) … numbering stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line); no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- Translate the Pāli as written (user rule): no emendations; only plain spelling slips and missing punctuation (e.g. a missing space after "(7)") may be rendered as meant. Report suspected slips.

## Verify every file (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-3_split_chapters AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters <file>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese>` prints OK.
- The builder's pi-1 / pi-2 string asserts pass.

## Report (under 450 words, as text)
- Checks passed, segment count per file.
- The proposed book title (with alternatives) and the chapter / sub-section headings.
- Key formulas and terms, and which were reused from pi-1 / pi-2 Vietnamese.
- Pāli you were unsure about or that looks like a source slip (translated as written).
