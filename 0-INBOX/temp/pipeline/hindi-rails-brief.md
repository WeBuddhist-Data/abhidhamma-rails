# Brief: RAILS Hindi translation (pi-3, Dhātukathā)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails.
- This is Windows: use the Read/Write tools for files and PowerShell for commands. Run python as `python -I -X utf8`.
- Other agents may translate other chapters in parallel. Write ONLY your own chapter files, plus helper scripts named after your chapters in 0-INBOX\temp\pipeline\pi-3-hi\rails\.

## Read first
- AI_translation\skills\rails-verse-translator.md, and follow it.
- 0-INBOX\temp\pipeline\hindi-style.md: register, typography, the dash rule, structure.
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the zero-shot Hindi chapter files (AI_translation\hindi\pi-3-hindi-plain-zeroshot_split_chapters\) or the merged zero-shot file.

## Inputs
- **Source:** AI_translation\pali\pi-3_split_chapters\<ch>.md
- **Locked termbase (authoritative, approved by the user):** AI_translation\hindi\pi-3-pali-hindi-termbase-plain.md, in the form `pali: {english tag: हिंदी; …}`.
  - Pick the sense by its tag.
  - Inflect grammatically (number, gender, oblique case, verb agreement), but never swap in a synonym.
  - Terms are listed in dictionary form; e.g. "X परिघटना" becomes «X परिघटनाएँ» / «X परिघटनाओं» as the sentence needs.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Sentence formulas (authoritative for sentence shape):** 0-INBOX\temp\pipeline\pi-3-hi\rails\hi-rails-formulas.md. The chapter-1 sample agent creates it; it is read-only for everyone else.
  - Any NEW recurring formula goes in your notes file rails\notes-<chapters>.md, not in the formulas file.
- **Approved rails sample, the model for everything:** 0-INBOX\temp\pipeline\pi-3-hi\rails\rails-sample.md, once approved.
- **Audience:** AI_translation\audience_profile\plain.md.
- **Helper:** a script with fixed formula strings guarantees identical Hindi for identical Pāli. The Dhātukathā is highly tabular, so use one.

## Output
- AI_translation\hindi\pi-3-hindi-plain-rails_split_chapters\<ch>.md (the folder exists).

## Rules
- **Structure:**
  - Block IDs exact, at the end of the last line of each segment, in the same order.
  - Headings keep their #-level.
  - Each segment has the source's number of non-empty lines.
  - One blank line between segments; no double blank lines.
- **DASH RULE (user):**
  - "–" only where the Pāli has "–" or "—", at the same spot, with the same count on every line.
  - No dash anywhere else, and no ":-".
- **Punctuation and notes:**
  - "…pe…" becomes "…".
  - Statements end with «।».
  - Quotes are “…” / ‘…’.
  - Translate editorial notes and variant brackets as in hindi-style.md.
- **Consistency:** identical Pāli formulas get identical Hindi.

## Verify each chapter (all must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-3_split_chapters AI_translation\hindi\pi-3-hindi-plain-rails_split_chapters <ch>.md
python -I -X utf8 -c "import sys;f=lambda p:[l for l in open(p,encoding='utf-8').read().splitlines() if l.strip()];c=lambda t:t.count('—')+t.count('–');a,b=f(sys.argv[1]),f(sys.argv[2]);bad=[i for i,(x,y) in enumerate(zip(a,b)) if c(x)!=c(y)];print('lines',len(a),len(b),'dash-line mismatches',len(bad),bad[:5])" AI_translation\pali\pi-3_split_chapters\<ch>.md AI_translation\hindi\pi-3-hindi-plain-rails_split_chapters\<ch>.md
```
Also confirm there are no double blank lines.

Finally, run a termbase adherence check:
```
python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_adherence.py AI_translation\pali\pi-3-keywords-by-reference-pali-plain.md AI_translation\hindi\pi-3-pali-hindi-termbase-plain.md AI_translation\hindi\pi-3-hindi-plain-rails_split_chapters
```
It checks only the segments present in the folder. Read misses with judgement (inflection or a split phrase can cause false misses), and fix the genuine ones.

## Final report (short)
- Per chapter: checks passed and segment count.
- New formulas.
- Termbase misfits.
- Unsure Pāli or source slips.
