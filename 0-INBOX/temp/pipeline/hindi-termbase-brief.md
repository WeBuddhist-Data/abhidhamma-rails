# Brief: termbase-builder, Pāli→Hindi plain (pi-3, pi-4, pi-5)

Work in D:\Work\OpenPecha\abhidhamma-rails (Windows; Read/Write tools for files, PowerShell for commands; python as `python -I -X utf8`). Write ONLY the files named in your task.

## Read first

- AI_translation\skills\termbase-builder.md. Follow it.
- AI_translation\audience_profile\plain.md. The audience has no Buddhist background, so understanding comes first.
- 0-INBOX\temp\pipeline\hindi-style.md. Its cross-book core terms and its "Lessons from the Russian review" are binding wherever they apply.
- The book's approved zero-shot term list (0-INBOX\temp\pipeline\pi-N-hi\hi-zeroshot-terms.md) and harmonise notes (harmonise-notes.md / notes-*.md). These record choices the user has already seen.
- Format reference only: the approved Russian termbase AI_translation\russian\pi-N-pali-russian-termbase-plain.md.

## Input and output

- Input: AI_translation\hindi\pi-N-pali-word-hindi-senses-plain.md, one line per Pāli headword: `hw: {tag: a / b; tag2: c}`.
- Your decisions go in 0-INBOX\temp\pipeline\pi-N-hi\termbase\decisions<-suffix>.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason`. sense_index is 0-based, in the senses file's order.
- Assembler: `python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_assemble.py N`. It:
  - keeps single-candidate senses;
  - requires one decision for every multi-candidate sense;
  - lets you re-align a single-candidate sense;
  - lists any term chosen outside the candidates for the user's approval;
  - writes AI_translation\hindi\pi-N-pali-hindi-termbase-plain.md plus the report termbase-decisions.md;
  - fails on any error.

## How to choose

1. **Multi-candidate senses.** Pick the one term a plain Hindi reader understands best and that fits the register. Prefer, in this order:
   - (a) the core term in hindi-style.md or the approved zero-shot term list;
   - (b) the form the harmonised translation uses most;
   - (c) the clearest plain-Hindi candidate.
   
   Give the term in dictionary form.
2. **Family consistency.** All inflections and compounds of one Pāli lemma, used in the same sense, get the same Hindi word. Examples:
   - vicikicchā / vicikicchaṃ / vicikicchānusaya → संशय …
   - every arahatta form → अर्हत्-पद
   - lokuttara → लोकोत्तर
   
   Scan the whole senses file for families by stem, using a script. Where a single-candidate sense drifted from its family's word, add a re-align decision. Keep genuine sense differences (e.g. dhamma परिघटना vs शिक्षा vs मन के विषय).
3. **Keep distinct Pāli terms distinct.** Do not give two different Pāli technical terms the same Hindi word where the text contrasts them. Known pairs:
   - vicikicchā / kaṅkhā
   - mettā / abyāpāda
   - kukkucca / uddhacca
   - vīriya / padhāna-vāyāma
   - sammappadhāna / sammāvāyāma (if both occur)
   - upādāna / rāga
   - yoga / ogha
   - abyākata in its two senses (नैतिक रूप से अनिर्धारित; "undeclared")
4. **Term form.** No ", ", " / " or "; " inside a term. Use " और " or rephrase.
5. **Outside terms.** A term outside the candidates only when every candidate is wrong for a plain reader, and give the reason.

## Verify

The assembler must print "no errors".

Then run a family scan that lists any lemma family which still has more than one Hindi word for the same sense. Fix it, or explain why the variation is intended.

## Report (short)

- The assembler's summary line.
- The number of family re-alignments.
- The outside-candidate choices.
- The 15 most consequential choices: high-frequency terms and contested pairs.
- Anything you are unsure of.

Do not use the words "seed" or "unseeded" anywhere.
