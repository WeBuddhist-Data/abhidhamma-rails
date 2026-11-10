# Brief: RAILS Hindi translation (pi-5, Kathāvatthu)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails.
- This is Windows: use the Read/Write tools for files and PowerShell for commands, and run python as `python -I -X utf8`.
- Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus helper scripts named after your chapters in 0-INBOX\temp\pipeline\pi-5-hi\rails\.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-style.md: register, typography, dash rule, structure, and book titles. Titles are in Hindi only: the book is «चर्चा के विषय».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the zero-shot Hindi chapter files (AI_translation\hindi\pi-5-hindi-plain-zeroshot_split_chapters\) or the merged zero-shot file.
- You may use the finished Hindi rails translations of pi-3 and pi-4 (AI_translation\hindi\pi-3-hindi-plain.md, pi-4-hindi-plain.md) as models of house style and shared passages.

## Inputs
- **Source:** AI_translation\pali\pi-5_split_chapters\<ch>.md
- **Locked termbase (authoritative, approved by the user):** AI_translation\hindi\pi-5-pali-hindi-termbase-plain.md, in the form `pali: {english tag: हिंदी; …}`.
  - Pick the sense by tag.
  - Inflect grammatically, but never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
  - niggaha has two senses: in the debate formulas it means refutation (खंडन); in the cittaniggaha debate it means restraint (अंकुश).
- **Sentence formulas (authoritative for sentence shape):** 0-INBOX\temp\pipeline\pi-5-hi\rails\hi-rails-formulas.md.
  - The chapter-1 sample agent creates it; it is read-only for everyone else.
  - Every debate formula (Āmantā, Na hevaṃ vattabbe, the refutation cycle, Nanu, Attheva suttanto, Tena hi, Na vattabbaṃ, the closings, Tassuddānaṃ, the paṇṇāsaka lines) must be copied from it verbatim.
  - Record any NEW recurring formula in rails\notes-<chapters>.md.
- **Approved rails sample (the model for everything):** 0-INBOX\temp\pipeline\pi-5-hi\rails\rails-sample.md, once approved.
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** a script with fixed formula strings guarantees identical Hindi for identical Pāli. The debate cycles are extremely repetitive, so use one.

## Output
AI_translation\hindi\pi-5-hindi-plain-rails_split_chapters\<ch>.md (the folder exists). Long chapters may be built in parts and joined, but the final file must be complete.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", at the same spot, with the same count on every line. pi-5 has very many source dashes (Hañci … vattabbe – "…"); keep every one. Never add a dash, and never use ":-".
- **Punctuation:**
  - "…pe…" becomes "…".
  - Statements end with «।».
  - Quotes are “…” / ‘…’; a third level stays unquoted, as in the Pāli.
- **Brackets:** translate editorial notes and variant brackets as in hindi-style.md. Sutta references use Devanagari collection names with digits, e.g. [संयुत्त निकाय 3.48].
- **Formulas:** identical Pāli formulas get identical Hindi.

## Verify each chapter (all must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-5_split_chapters AI_translation\hindi\pi-5-hindi-plain-rails_split_chapters <ch>.md
python -I -X utf8 -c "import sys;f=lambda p:[l for l in open(p,encoding='utf-8').read().splitlines() if l.strip()];c=lambda t:t.count('—')+t.count('–');a,b=f(sys.argv[1]),f(sys.argv[2]);bad=[i for i,(x,y) in enumerate(zip(a,b)) if c(x)!=c(y)];print('lines',len(a),len(b),'dash-line mismatches',len(bad),bad[:5])" AI_translation\pali\pi-5_split_chapters\<ch>.md AI_translation\hindi\pi-5-hindi-plain-rails_split_chapters\<ch>.md
```
Also confirm there are no double blank lines. Then run termbase adherence:
```
python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_adherence.py AI_translation\pali\pi-5-keywords-by-reference-pali-plain.md AI_translation\hindi\pi-5-pali-hindi-termbase-plain.md AI_translation\hindi\pi-5-hindi-plain-rails_split_chapters
```
Fix genuine misses. Inflection causes false misses, so read the misses with judgement.

## Final report (short)
- Per chapter: checks passed and segment count.
- New formulas.
- Termbase misfits.
- Unsure Pāli or source slips.
