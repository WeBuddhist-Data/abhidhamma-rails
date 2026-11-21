# Brief: Vietnamese zero-shot of pi-5 (Kathāvatthu), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths under D:\Work\OpenPecha\abhidhamma-rails, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY the files named below plus helper scripts in 0-INBOX\temp\pipeline\pi-5-vi-ai\. Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git (not even git status), never write "seed" or "unseeded" in any file you write. No web access. You cannot write report files for me: return your report as text.

This is the SAMPLE the user reviews before the rest of the book is translated by other agents (three at a time, one chapter each), who will copy your formulas verbatim. Be careful, exact and consistent.

The sample is the preamble and chapter 1 (1-puggalakatha.md, the debate on the person, 430 lines). It sets every debate formula of the book: the questions and the answers (Āmantā / Na hevaṃ vattabbe), the five-part rebuttal (anuloma, paṭikamma, niggaha, upanayana, niggamana: Ājānāhi niggahaṃ … micchā), the opponent's / our side's question headings, the section labels (Anulomapañcakaṃ …) and the sutta quotations.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here. Our wording must be our own.

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, the strict DASH RULE, “…” / ‘…’ (nested quotes in this book are frequent: outer “…”, inner ‘…’), core terms (sati = «sự tỉnh thức», never «chánh niệm»), review lessons, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Vietnamese (user-approved and reviewed): pi-1 («Liệt kê các hiện tượng»), pi-2 («Phân tích các hiện tượng»), pi-3 («Thảo luận về các yếu tố»), pi-4 («Định danh các hạng người»).** The Kathāvatthu quotes their lists (aggregates, bases, elements, faculties, path / fruit, the person types) and many terms. **Reuse that wording exactly.** Sources: AI_translation\vietnamese\pi-1/2/3/4-vietnamese-plain-rails_split_chapters\ (find matches by grepping the Pāli in AI_translation\pali\pi-N_split_chapters\ and reading the same non-empty line; 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\find_pi123_rails_vi.py shows a lookup method: adapt a copy in pi-5-vi-ai\ that covers pi-1-4); termbases AI_translation\vietnamese\pi-1/2/3/4-pali-vietnamese-termbase-plain.md; the user's decisions 0-INBOX\temp\pipeline\pi-1/2/3/4-vi-ai\termbase\APPROVED.md and pi-1-vi-ai\vi-core-terms.md. Cross-book terms follow pi-1 (pi-2 rule). Person-type names: pi-4 (e.g. sotāpanna «bậc vào dòng», arahant «bậc A-la-hán»).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** AI_translation\russian\pi-5-russian-plain-rails_split_chapters\<ch>.md (by block ID), 0-INBOX\temp\pipeline\pi-5-ru\ru-zeroshot-terms.md and ru-rails-formulas.md (the formula inventory of this book), and the commentary 1-SOURCES\Commentaries\pi-kathavatthu-atthakatha.md for hard readings (the commentary is Pāli; allowed).

## Source and output
- Source: AI_translation\pali\pi-5_split_chapters\preamble.md, 1-puggalakatha.md.
- Write:
  1. AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters\preamble.md, 1-puggalakatha.md (create the folder).
  2. 0-INBOX\temp\pipeline\pi-5-vi-ai\build_sample_vi.py: a builder with fixed formula strings exposed as constants other agents import (the question frame with "…ti?", Āmantā, Na hevaṃ vattabbe, the rebuttal pentad sentences with their slots, "Yaṃ tattha vadesi … micchā", "Ājānāhi niggahaṃ / paṭikammaṃ", the section labels, the speaker headings [iminā lakkhaṇena …], the sutta-quote frames «Vuttaṃ bhagavatā …», the heading words …kathā «Bàn về …»). Importing it must not rewrite outputs (`if __name__ == "__main__":`). It must assert at build time that every string it claims to take from pi-1-4 still occurs in those rails files.
  3. 0-INBOX\temp\pipeline\pi-5-vi-ai\vi-zeroshot-terms.md: every formula and key term you settled, "Pāli = tiếng Việt", one per line, grouped (book frame, headings, debate frames, rebuttal pentad, labels, terms). Mark which come from pi-1-4 and which are new.
- **Book and chapter titles:** propose the Vietnamese title of the book (Kathāvatthupāḷi; one or two alternatives; earlier titles «Liệt kê các hiện tượng», «Phân tích các hiện tượng», «Thảo luận về các yếu tố», «Định danh các hạng người») and Vietnamese headings for ALL chapters (read the heading lines of the 33 files: the first nine kathā of the first vagga, then Dutiyavaggo … Tevīsatimavaggo with their kathā sub-headings) in the terms file. Vietnamese only, no Pāli name and no bracketed gloss.

## Rules
- Identical Pāli = identical Vietnamese, within the sample and with pi-1-4 Vietnamese.
- Core: dhamma = hiện tượng (the Teaching = Giáo Pháp); puggala = người; paramattha / saccikaṭṭha: choose and state one rendering each and use it throughout; upalabbhati: one rendering; sakavādī / paravādī: one rendering each (they appear in the bracketed speaker notes); sati = sự tỉnh thức.
- Speaker-marked notes in square brackets in the Pāli ("[iminā lakkhaṇena sakavādīpucchā dassitā]") are part of the text: translate them inside the same brackets. Variant brackets: "[khác chính tả (Sī., Syā.): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…" (never «….»). (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Digits and numbering stay.
- **DASH RULE:** "–" exactly where the Pāli has "–", same count per line; never add one; no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- **Quotes:** the Pāli nests "…" and ‘…’ and sometimes closes them in an odd order ("…"’ti): keep the nesting the Pāli shows, as “…” outer and ‘…’ inner, and count them per line; report any line where you had to repair the order.
- Translate the Pāli as written (user rule): no emendations, add nothing; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.

## Verify every file (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-5_split_chapters AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters <file>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese>` prints OK.
- The builder's cross-book string asserts pass.

## Report (under 450 words, as text)
- Checks passed, segment count per file.
- The proposed book title (with alternatives), the chapter / kathā headings, and the renderings of paramattha, saccikaṭṭha, upalabbhati, sakavādī / paravādī.
- The debate formulas (question, the two answers, the five rebuttal steps, the labels) as "Pāli = tiếng Việt".
- What was reused from pi-1-4; Pāli you were unsure about or source slips (translated as written).
