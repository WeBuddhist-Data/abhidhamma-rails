# Brief: termbase-builder, Pāli→Hindi plain, pi-2 (Vibhaṅga)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`. Write ONLY the files named in your task (in 0-INBOX\temp\pipeline\pi-2-hi\termbase\). Do not touch 1-SOURCES\, 4-SYSTEM\, AI_translation\ (the assembler writes there, not you), and do not run git. Do not use the words "seed" or "unseeded" anywhere.

## Read first

- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-termbase-brief.md: the brief used for the approved pi-3/pi-4/pi-5 Hindi termbases. Its "How to choose" rules 1–5 apply here unchanged; this file only adds what is specific to pi-2.
- 0-INBOX\temp\pipeline\pi-1-hi\hi-termbase-brief.md and pi-1-hi\termbase\termbase-decisions.md: how the approved pi-1 termbase was decided (pi-1 is the book closest to pi-2).
- AI_translation\audience_profile\plain.md (no Buddhist background; understanding first).
- 0-INBOX\temp\pipeline\hindi-style.md (core terms; binding).
- 0-INBOX\temp\pipeline\pi-2-hi\hi-zeroshot-terms.md (the pi-2 binding term list: book and chapter titles, formulas) and pi-2-hi\harmonise-notes.md. The user approved the pi-2 translation built from these.

## Input, output, tools

- Input: AI_translation\hindi\pi-2-pali-word-hindi-senses-plain.md (4,969 headwords, 5,094 senses; about 250 senses have 2+ candidates). Line N of this file = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-2-hi\termbase\decisions-part<K>.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based in the senses line). Start the file with a `#` comment line naming your line range.
- Helper (read its docstring): `python -I -X utf8 0-INBOX\temp\pipeline\pi-2-hi\termbase\tb_tool_pi2.py`
  - `list <from> <to> [--multi]`: your senses with candidate counts from the pi-2 map, decisions so far, and the same headword's terms in the approved pi-1/3/4/5 Hindi termbases ("prior").
  - `fam <regex>`: a whole lemma family across all of pi-2 (use it for every family you touch).
  - `prior <regex>`: a family in the pi-1/3/4/5 termbases.
  - `hcount <hindi> …`: how often a string occurs in the harmonised pi-2 Hindi translation.
  - `check <from> <to>`: every multi-candidate sense in your range decided, no forbidden characters, outside-candidate choices listed. Must print "no errors".
- The final assembler (`python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_assemble.py 2`) is run by the coordinator after all parts exist; you only need `check` to pass for your range.

## pi-2 specifics

1. **Order of preference for multi-candidate senses:** (a) a core term in hindi-style.md or the pi-2 term list (hi-zeroshot-terms.md); (b) the term the approved **pi-1** termbase gives the same Pāli word in the same meaning, when it is among the candidates (pi-1 shares most formulas with pi-2 and was reviewed bilingually); then the pi-3/4/5 termbases; (c) the form the pi-2 translation uses most (map counts / hcount); (d) the clearest plain-Hindi candidate. Dictionary form.
2. **Family alignment** (re-align decisions on single-candidate senses) only where the same Pāli lemma in the same meaning drifted to a different Hindi word. Grammatical variants inside one sense are not drift: choose the dictionary form. Genuine sense splits in the senses file stay split.
3. **Cross-book differences: report, do not force.** Where pi-2's term for a sense differs from the term the pi-1 (or pi-3/4/5) termbase gives the same Pāli word and meaning, keep the pi-2 term unless the prior term is among the candidates (then rule 1b applies), and list the case in your report under "Cross-book differences" (pali | sense | pi-2 term | prior term(s) | books). The user decides those.
4. **Known pi-2 open points (decide those in your range and give the reason; if one is outside your range, leave it):**
   - dukkhanirodhagāminī paṭipadā: the harmonised text has pi-1's «… प्रगति का ढंग»; pi-5 has «मार्ग». Decide paṭipadā in this phrase and report it as a cross-book item.
   - āsevati / bhāveti / bahulīkaroti: chapters 8 and 9 render the same verb string differently; one term each.
   - padhāna (प्रयत्न, approved in sammappadhāna = सही प्रयत्न), vāyāma (प्रयास), vīriya (उत्साह), parakkama (pi-1: प्रयत्न): keep padhāna and parakkama apart where the text puts them side by side; report the clash.
   - duccarita: «शारीरिक/वाचिक/मानसिक दुराचरण» vs «शरीर/वाणी/मन का दुराचरण»: one form for the family.
   - dhaja / ketu: «ध्वजा» / «झंडा»; follow pi-1's decision for ketu and dhajo.
   - kilesa: «मन के क्लेश» (core term) vs «क्लेश».
   - saṃkilesika: «क्लेशों का विषय बनने वाला» (approved for pi-1 after its review).
   - dhamma in dhammapaṭisambhidā: परिघटना vs शिक्षा.
   - samāpatti: «अपनाना» / «प्राप्ति» / «अवस्था».
5. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash.

## Report (short, under 300 words)

- The `check` output line for your range.
- Number of multi-candidate decisions and of family re-alignments.
- Outside-candidate choices with reasons.
- The 15 most consequential choices (high-frequency terms, contested pairs, the open points above that fall in your range).
- Cross-book differences (the table described in rule 3).
- Anything you are unsure of.
