# Brief: RAILS Marathi translation (pi-3, Dhātukathā)

## Setup
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Use the Read/Write tools for files and run Python as `python3 -I -X utf8`. Write helper scripts to files.
- Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus helper scripts and notes named after your chapters, in 0-INBOX/temp/pipeline/pi-3-mr/rails/. Never use the system temp directory. Don't commit.

## Read first
- AI_translation/skills/rails-verse-translator.md, and follow it.
- 0-INBOX/temp/pipeline/marathi-style.md: register, typography, the dash rule, structure.
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the zero-shot Marathi chapter files (AI_translation/marathi/pi-3-marathi-plain-zeroshot_split_chapters/), the merged zero-shot file, or the zero-shot generators (make_ch*.py, mr_items_*.py, mr_harmonised.py).

## Inputs
- **Source:** AI_translation/pali/pi-3_split_chapters/<ch>.md
- **Locked termbase (authoritative, approved by the user on 2026-11-09):** AI_translation/marathi/pi-3-pali-marathi-termbase-plain.md, in the form `pali: {english tag: मराठी; …}`.
  - Pick the sense by its tag.
  - Inflect grammatically (number, gender, case endings, agreement), but never swap in a synonym.
  - Terms are listed in dictionary form; e.g. «मुळांसह असलेला» becomes «मुळांसह असलेल्या घटनांसोबत» as the sentence needs. A " … " inside a term marks a gap: the parts stand apart in the sentence.
  - If no sense fits, use the closest sibling entry and REPORT it. Never edit the termbase.
- **Sentence formulas (authoritative for sentence shape, read-only):** 0-INBOX/temp/pipeline/pi-3-mr/rails/mr-rails-formulas.md.
  - Its section 5 lists every Pāli line that recurs in the book (summary verses, headings, closers) with its one Marathi line: use those byte-for-byte.
  - The same formula strings are coded in 0-INBOX/temp/pipeline/pi-3-mr/mr_formulas.py: import it (sys.path.insert to that folder) instead of retyping them. Do not edit it.
  - Oblique forms of item names in sentence context: the harmonised table at the end of 0-INBOX/temp/pipeline/pi-3-mr/harmonise-notes.md plus its "User decisions" section. The termbase wins on any conflict; report it.
  - Any NEW recurring formula goes in your notes file rails/notes-<chapters>.md, not in the formulas file.
- **Approved rails sample, the model for everything:** 0-INBOX/temp/pipeline/pi-3-mr/rails/rails-sample.md and its generator make_rails_sample.py, which shows the method: read each Pāli line, take the counts from the Pāli words, take the item names from the termbase, and build the sentence with the formula helpers.
- **Audience:** AI_translation/audience_profile/plain.md.

## Output
- AI_translation/marathi/pi-3-marathi-plain-rails_split_chapters/<ch>.md (the folder exists).
- Chapter 2 only: blocks ^3-2-0 to ^3-21 are the approved sample (rails/ch2-sample.md). Keep them byte-for-byte (self-check in your script) and continue from ^3-2-1-2-0.

## Rules
- **Structure:**
  - Block IDs exact, at the end of the last line of each segment, in the same order.
  - Headings keep their #-level.
  - Each segment has the source's number of non-empty lines.
  - One blank line between segments; no double blank lines.
- **DASH RULE (user):**
  - "–" only where the Pāli has "–" or "—", at the same spot, with the same count on every line.
  - No dash anywhere else, and no ":-". A hyphen inside a compound word (इंद्रिय-क्षेत्र) is not a dash.
- **Punctuation and notes:**
  - "…pe…" becomes "…"; one space after «…» before a following word (use mr_formulas.space_ellipsis on your output).
  - Statements end with «.» (never «।»).
  - Quotes are “…” / ‘…’.
  - Translate editorial notes and variant brackets as in marathi-style.md.
- **Consistency:** identical Pāli formulas get identical Marathi. Generate the tables with a script; get every number from the Pāli.
- **Book titles:** Marathi only («तत्त्वांवरील चर्चा», «घटनांची गणना»), in quotes mid-sentence.

## Verify each chapter (all must pass)
```
python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-3_split_chapters AI_translation/marathi/pi-3-marathi-plain-rails_split_chapters <ch>.md
python3 -I -X utf8 0-INBOX/temp/pipeline/pi-3-mr/check_text.py AI_translation/pali/pi-3_split_chapters/<ch>.md AI_translation/marathi/pi-3-marathi-plain-rails_split_chapters/<ch>.md
```
Both must print OK: IDs, line counts, dashes, ellipses, no "।", no ":-", no double blank lines.

Then write and run a number check: the sequence of numbers on each Marathi line must match the Pāli line (map ekena/eken…/dvīhi/tīhi/catūhi/… and the Marathi number words to integers; ignore the group closers). 0 mismatches.

Finally, run the termbase adherence check:
```
python3 -I -X utf8 0-INBOX/temp/pipeline/marathi_termbase_adherence.py AI_translation/pali/pi-3-keywords-by-reference-pali-plain.md AI_translation/marathi/pi-3-pali-marathi-termbase-plain.md AI_translation/marathi/pi-3-marathi-plain-rails_split_chapters
```
It checks only the segments present in the folder. Read misses with judgement (inflection or a split phrase can cause false misses), and fix the genuine ones.

## Final report (short)
- Per chapter: checks passed, segment count, number-check result, adherence result.
- New formulas.
- Termbase misfits.
- Unsure Pāli or source slips.
