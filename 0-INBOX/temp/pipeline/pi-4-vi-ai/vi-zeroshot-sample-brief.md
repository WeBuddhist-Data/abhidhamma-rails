# Brief: Vietnamese zero-shot of pi-4 (Puggalapaññatti), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY the files named below plus helper scripts in 0-INBOX\temp\pipeline\pi-4-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git (not even git status), never write "seed" or "unseeded" in any file you write. No web access. You cannot write report files for me: return your report as text.

This is the SAMPLE the user reviews before the rest of the book is translated by other agents (three at a time, one chapter each), who will copy your formulas verbatim. Be careful, exact and consistent.

The sample is the preamble, chapter 1 (1-matika.md, the matrix: the six designations and the list of all person types, 185 lines) AND chapter 2 (2-ekakapuggalapannatti.md, the single persons, 47 lines). Chapter 2 settles the definition frame («Katamo ca puggalo X? Idhekacco puggalo … – ayaṃ vuccati puggalo "X".») that chapters 3-11 build on.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here. Our wording must be our own.

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, the strict DASH RULE, “…” / ‘…’, core terms (sati = «sự tỉnh thức», never «chánh niệm»), review lessons, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Vietnamese (user-approved and reviewed): pi-1 («Liệt kê các hiện tượng»), pi-2 («Phân tích các hiện tượng»), pi-3 («Thảo luận về các yếu tố»).** The matrix's first part (the aggregates, bases, elements, truths, faculties) and many person terms (sotāpanna, arahant, the jhāna and vimokkha formulas, kāyasakkhī …) are already translated there. **Reuse that wording exactly.** Sources, in order:
  1. AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\, pi-2-vietnamese-plain-rails_split_chapters\, pi-1-vietnamese-plain-rails_split_chapters\ (final reviewed text; find matches by grepping the Pāli in the same-named file of AI_translation\pali\pi-N_split_chapters\ and reading the same non-empty line in the Vietnamese file). 0-INBOX\temp\pipeline\pi-3-vi-ai\rails\find_pi12_vi.py shows a lookup method; adapt a copy in pi-4-vi-ai\ that also covers pi-3.
  2. Termbases and the user's decisions: AI_translation\vietnamese\pi-3-pali-vietnamese-termbase-plain.md, pi-2-…, pi-1-…; 0-INBOX\temp\pipeline\pi-3-vi-ai\termbase\APPROVED.md, pi-2-vi-ai\termbase\APPROVED.md, pi-1-vi-ai\termbase\APPROVED.md, pi-1-vi-ai\vi-core-terms.md. Cross-book terms follow pi-1 (pi-2 rule).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** AI_translation\english\pi-4-english-plain.md and AI_translation\russian\pi-4-russian-plain-rails_split_chapters\<ch>.md (find segments by block ID); 0-INBOX\temp\pipeline\pi-4\ru-zeroshot-terms.md and ru-rails-formulas.md show the book's structure and formulas.

## Source and output
- Source: AI_translation\pali\pi-4_split_chapters\preamble.md, 1-matika.md, 2-ekakapuggalapannatti.md.
- Write:
  1. AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters\preamble.md, 1-matika.md, 2-ekakapuggalapannatti.md (whole files; create the folder).
  2. 0-INBOX\temp\pipeline\pi-4-vi-ai\build_sample_vi.py: a builder with fixed formula strings exposed as constants other agents import: EVERY person-type name of the matrix (chapters 3-11 define them: the later agents must use these names verbatim), the designation frame («Kittāvatā … paññatti? Yāvatā … ettāvatā …»), the definition frame («Katamo ca puggalo X? … – ayaṃ vuccati puggalo “X”.»), «Idhekacco puggalo», the section headings and the closing lines. Importing it must not rewrite outputs (guard with `if __name__ == "__main__":`). It must assert at build time that every string it claims to take from pi-1 / pi-2 / pi-3 still occurs in those rails files.
  3. 0-INBOX\temp\pipeline\pi-4-vi-ai\vi-zeroshot-terms.md: every formula and key term you settled, "Pāli = tiếng Việt", one per line, grouped (book frame, chapter and section headings, frames, person names by chapter, terms). Mark which come from pi-1 / pi-2 / pi-3 and which are new.
- **Book and chapter titles:** propose the Vietnamese title of the book (Puggalapaññattipāḷi; give one or two alternatives; the earlier books: «Liệt kê các hiện tượng», «Phân tích các hiện tượng», «Thảo luận về các yếu tố») and Vietnamese headings for ALL chapters and sections (Mātikā, Ekakauddeso … Dasakauddeso, Niddeso, Ekakapuggalapaññatti … Dasakapuggalapaññatti; read every chapter file's heading lines) in the terms file. Vietnamese only, no Pāli name and no bracketed gloss (vietnamese-style.md "Book titles").

## Rules
- Identical Pāli = identical Vietnamese, within the sample and with pi-1 / pi-2 / pi-3 Vietnamese.
- Core: dhamma = hiện tượng (the Teaching = Giáo Pháp); khandha = khối; āyatana = lĩnh vực nhận biết; dhātu = yếu tố; sacca = sự thật; indriya = năng lực; puggala = người; paññatti: choose and state one rendering for the designation sense (e.g. «sự định danh») and use it throughout; sati = sự tỉnh thức.
- Person names: a consistent noun-phrase pattern (e.g. «người được giải thoát theo thời điểm»); the matrix name of a person and its definition heading/question must match exactly. The quoted name at the end of each definition («ayaṃ vuccati puggalo "X"») is the same string in “…”.
- No notes or commentary of your own inside the translation. Variant brackets "[khác chính tả (Sī., Syā.): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…" (never «….»). (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Digits and numbering stay.
- **DASH RULE:** "–" exactly where the Pāli has "–" (this book has many, e.g. before «ayaṃ vuccati»), same count per line; never add one; no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- Translate the Pāli as written (user rule): no emendations, add nothing; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.

## Verify every file (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-4_split_chapters AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters <file>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese>` prints OK.
- The builder's cross-book string asserts pass.

## Report (under 450 words, as text)
- Checks passed, segment count per file.
- The proposed book title (with alternatives), the chapter / section headings, the paññatti rendering.
- The definition frame and 10-15 person names; what was reused from pi-1 / pi-2 / pi-3.
- Pāli you were unsure about or that looks like a source slip (translated as written).
