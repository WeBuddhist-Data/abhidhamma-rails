# Brief: RAILS Hindi translation, plain audience (pi-1, Dhammasaṅgaṇī)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails.
- Windows: use the Read/Write tools for files and PowerShell for commands; run python as `python -I -X utf8`.
- Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus helper scripts and notes named after your chapters in 0-INBOX\temp\pipeline\pi-1-hi\rails\. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.
- Do not use the words "seed" or "unseeded" anywhere.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-style.md: register, typography, dash rule, structure. Titles are in Hindi only: the book is «परिघटनाओं की गणना».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the zero-shot Hindi chapter files (AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters\), the merged zero-shot file, or the keyword maps' Hindi side.
- You may use the finished Hindi rails translations of the other books (AI_translation\hindi\pi-3-hindi-plain.md, pi-4-hindi-plain.md, pi-5-hindi-plain.md) as models of house style and shared passages. Where they disagree with the pi-1 termbase, the pi-1 termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-1_split_chapters\<ch>.md
- **Locked termbase (authoritative, approved by the user):** AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md, in the form `pali: {english tag: हिंदी; …}`.
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Inflect grammatically (number, gender, oblique case, verb agreement), but never swap in a synonym. Terms are in dictionary form: «X के साथ होने वाला» becomes «X के साथ होने वाली परिघटनाएँ» as the sentence needs; «परिघटना» becomes «परिघटनाएँ» / «परिघटनाओं».
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Sentence formulas (authoritative for sentence shape):** 0-INBOX\temp\pipeline\pi-1-hi\rails\hi-rails-formulas.md. The sample agent creates it; it is read-only for everyone else. Any NEW recurring formula goes in your notes file rails\notes-<chapters>.md.
- **Matrix items:** the approved rails 1-matika.md (AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\1-matika.md) fixes every triad and pair name. Chapters 4 and 5 must reuse those names verbatim in their question and answer frames (Katame dhammā X? / ime dhammā X).
- **Approved rails sample (the model for everything):** the sample's files in the rails folder, once approved.
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** a script with fixed formula strings guarantees identical Hindi for identical Pāli. The Dhammasaṅgaṇī is highly repetitive (the synonym strings of each factor, the jhāna formulas, the "samaye" definition lists, the -pe- runs), so use one.

## The approved sample (user-approved 2026-11-11): read it first, it is the model for everything
- AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\preamble.md and 1-matika.md (done; do not rewrite them).
- 0-INBOX\temp\pipeline\pi-1-hi\rails\sample-2-01\2-01-sample.md: chapter 2 through ^1-57.
- 0-INBOX\temp\pipeline\pi-1-hi\rails\hi-rails-formulas.md: every string in it is binding, copy it verbatim. 0-INBOX\temp\pipeline\pi-1-hi\rails\build_rails_sample.py holds the same strings as Python constants; import it instead of retyping them (import only; never edit it).
- Three points from the review of the sample, all binding:
  - The termbase's "no comma inside a term" is a file-format rule, not punctuation. Hindi sentences take normal commas: «न X, न Y», «X, पर Y», and commas in lists.
  - vipāka as a class of phenomena = «कर्म-फल रूपी»; after हितकर/हानिकर = «हितकर कर्म के फल रूपी …», «हानिकर कर्म के फल रूपी …».
  - The citta synonym string is fixed in the formulas file, with mano = «मानस» there only (the one place). Everywhere else mano = «मन».
- Terms the termbase lacks, as built in the sample: anuvicāro «बार-बार सतत विचार», upavicāro «गहरा सतत विचार», paṭipassaddhi «पूरी प्रशांति», gocchaka «वर्ग». Reuse them.

## Output
AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\<ch>.md (the folder exists). Long chapters may be built in parts and joined, but the final file must be complete.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order (including the odd ^1-U1).
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", at the same spot, with the same count on every line. Never add a dash, and never use ":-".
- **Punctuation:** "…pe…" becomes "…". Statements end with «।». Quotes are “…” / ‘…’.
- **Brackets:** variant brackets as in hindi-style.md: «[वर्तनी-भेद (Sī.): …]» for spelling-only variants, «[पाठभेद (…): …]» otherwise; (Ka)/(Kha) → (क)/(ख). Editorial notes are translated.
- **Formulas:** identical Pāli gets identical Hindi. Where the Pāli of two segments differs only by a variant bracket or a numeral, the Hindi differs only there.
- **Readability for a plain reader:** the long -pe- runs and the abbreviated lists must still read as Hindi sentences. Do not leave a term sitting ungrammatically; where a literal string reads badly (for example a noun repeated right next to its own adjective), recast the sentence while keeping every term.

## Verify each chapter (all must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py AI_translation\pali\pi-1_split_chapters\<ch>.md AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\<ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py AI_translation\pali\pi-1_split_chapters\<ch>.md AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\<ch>.md
```
Also confirm there are no double blank lines. Then run termbase adherence (it checks only the segments present in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_adherence.py AI_translation\pali\pi-1-keywords-by-reference-pali-plain.md AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters
```
Fix genuine misses. Inflection and split phrases cause false misses, so read the misses with judgement.

## Final report (short)
- Per chapter: checks passed and segment count; adherence result.
- New formulas.
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Unsure Pāli or source slips.
