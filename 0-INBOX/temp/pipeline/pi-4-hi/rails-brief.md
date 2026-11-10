# Brief: RAILS Hindi translation (pi-4, Puggalapaññatti)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails.
- The machine runs Windows. Use the Read/Write tools for files and PowerShell for commands. Run python as `python -I -X utf8`.
- Other agents may translate other chapters in parallel. Write ONLY your own chapter files, plus helper scripts named after your chapters in 0-INBOX\temp\pipeline\pi-4-hi\rails\.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-style.md: register, typography, the dash rule, structure, and book titles. A book title is the Hindi name only, e.g. «व्यक्तियों का विवरण», never «पुग्गलपञ्ञत्ति (…)».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the zero-shot Hindi chapter files (AI_translation\hindi\pi-4-hindi-plain-zeroshot_split_chapters\) or the merged zero-shot file.
- The finished pi-3 Hindi rails translation, AI_translation\hindi\pi-3-hindi-plain.md, may be used as a model of the house style.

## Inputs
- **Source:** AI_translation\pali\pi-4_split_chapters\<ch>.md
- **Locked termbase:** AI_translation\hindi\pi-4-pali-hindi-termbase-plain.md, in the form `pali: {english tag: हिंदी; …}`. The user has approved it, and it is authoritative.
  - Pick the sense by its tag.
  - Inflect the term grammatically (number, gender, oblique, verb agreement), but never replace it with a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Person-type names:** use the exact termbase / approved mātikā forms. Every definition answers a mātikā name, and the name must read the same in the mātikā, the question and the closing "– ayaṃ vuccati puggalo …" line.
- **Sentence formulas:** 0-INBOX\temp\pipeline\pi-4-hi\rails\hi-rails-formulas.md is authoritative for sentence shape. The chapter-1 sample agent creates it; it is read-only for everyone else. Record any NEW recurring formula in rails\notes-<chapters>.md.
- **Approved rails sample:** 0-INBOX\temp\pipeline\pi-4-hi\rails\rails-sample.md, once approved. It is the model for everything.
- **Audience:** AI_translation\audience_profile\plain.md.
- **Helper script:** recommended. A script with fixed formula strings guarantees identical Hindi for identical Pāli. The definitions repeat whole passages, e.g. the seven noble persons in ch2, ch8 and ch10, and the similes in ch4–5.

## Output
- AI_translation\hindi\pi-4-hindi-plain-rails_split_chapters\<ch>.md (the folder exists).

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" goes only where the Pāli has "–" or "—", at the same spot, with the same count on every line. pi-4 has many source dashes (e.g. "– ayaṃ vuccati puggalo …"); keep each one. Never add one, and never use ":-".
- **Punctuation:** "…pe…" becomes "…". Statements end with «।». Quotes are “…” / ‘…’.
- **Notes and brackets:** translate editorial notes and variant brackets as in hindi-style.md. Keep source citations such as "a. ni. …" as in the source.
- **Formulas:** identical Pāli formulas get identical Hindi.

## Verify each chapter (all must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-4_split_chapters AI_translation\hindi\pi-4-hindi-plain-rails_split_chapters <ch>.md
python -I -X utf8 -c "import sys;f=lambda p:[l for l in open(p,encoding='utf-8').read().splitlines() if l.strip()];c=lambda t:t.count('—')+t.count('–');a,b=f(sys.argv[1]),f(sys.argv[2]);bad=[i for i,(x,y) in enumerate(zip(a,b)) if c(x)!=c(y)];print('lines',len(a),len(b),'dash-line mismatches',len(bad),bad[:5])" AI_translation\pali\pi-4_split_chapters\<ch>.md AI_translation\hindi\pi-4-hindi-plain-rails_split_chapters\<ch>.md
```
Also confirm there are no double blank lines. Then run the termbase adherence check, which covers only the segments present in the folder:
```
python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_adherence.py AI_translation\pali\pi-4-keywords-by-reference-pali-plain.md AI_translation\hindi\pi-4-pali-hindi-termbase-plain.md AI_translation\hindi\pi-4-hindi-plain-rails_split_chapters
```
Fix genuine misses. Inflection or a split phrase can produce false misses; read them with judgement.

## Final report (short)
- Per chapter: checks passed and segment count.
- New formulas.
- Termbase misfits.
- Unsure Pāli or source slips.
