# Brief: termbase-builder, Pāli→Hindi plain, pi-7 (Paṭṭhāna)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -B -X utf8`. Write ONLY the files named in your task (in 0-INBOX\temp\pipeline\pi-7-hi\termbase\), and helper scripts named tb7_*.py there. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\, 4-SYSTEM\, AI_translation\ (except that running the assembler writes the termbase file there), and do not run git. Do not use the words "seed" or "unseeded" anywhere. You cannot write report files for me: return your report as text.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-termbase-brief.md: the brief used for the approved pi-3/pi-4/pi-5 Hindi termbases. Its "How to choose" rules 1–5 apply here unchanged.
- 0-INBOX\temp\pipeline\pi-6-hi\hi-termbase-brief.md, pi-6-hi\termbase\termbase-decisions.md and pi-6-hi\termbase\cross-book-differences.md: how the approved pi-6 termbase was decided (the closest model; same method).
- AI_translation\audience_profile\plain.md; 0-INBOX\temp\pipeline\hindi-style.md (core terms; binding).
- 0-INBOX\temp\pipeline\pi-7-hi\hi-zeroshot-terms.md (the pi-7 binding term list: book title «कारण-संबंध», the 24 condition names with «-कारण», division and section headings, frames) and pi-7-hi\harmonise-notes.md (the triad/dyad names and the forms the harmonise pass fixed). The user approved the pi-7 translation built from these.
- 0-INBOX\temp\pipeline\pi-7-hi\mapper-hi\hi-map-conventions-pi7.md and pi-7-hi\senses\senses-conventions-pi7.md (how values and senses were formed).

## Input, output, tools
- Input: AI_translation\hindi\pi-7-pali-word-hindi-senses-plain.md (2,315 headwords, 2,347 senses; 113 senses have 2+ candidates). Line N of this file = headword N.
- Decisions: 0-INBOX\temp\pipeline\pi-7-hi\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based in the senses line). Start with a `#` comment line. Family re-alignments of single-candidate senses go in the same file (one decision per key; the assembler fails on duplicates).
- Helper (read its docstring): `python -I -B -X utf8 0-INBOX\temp\pipeline\pi-7-hi\termbase\tb_tool_pi7.py`
  - `list <from> <to> [--multi]`: senses with candidate counts, decisions so far, and the same headword's terms in the approved pi-1..pi-6 Hindi termbases ("prior").
  - `fam <regex>`: a lemma family across all of pi-7. `prior <regex>`: a family in the pi-1..6 termbases. `hcount <hindi> …`: occurrences in the merged pi-7 Hindi zero-shot. `check <from> <to>`: must print "no errors".
- Assembler: `python -I -B -X utf8 0-INBOX\temp\pipeline\hindi_termbase_assemble.py 7` → AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md and termbase\termbase-decisions.md. It must finish with "no errors".

## Task
1. **Multi-candidate senses (113):** decide each by the order: (a) a core term in hindi-style.md or the pi-7 terms file / harmonise-notes; (b) the approved pi-1, pi-2 or pi-6 termbase's term for the same Pāli word in the same meaning, if it is among the candidates; then pi-3/4/5; (c) the form the pi-7 translation uses most; (d) the clearest plain-Hindi candidate. Dictionary form; prefer the ungapped form over a gapped (" … ") one when both are attested. Most of these are drift between parallel agents (natthi, jappeti, gaṇhāti, pāṇaṃ, kātabba-, the crime list, paripuṇṇa …): pick one term each.
2. **Family alignment** across the whole book: where the same Pāli lemma in the same meaning drifted to different Hindi in different headwords (case forms, -ti/-ñca/-pi forms, the condition names in their positive / negative / count forms, the triad and dyad items and names, the na-/no-/nana- items, the kind labels), re-align single-candidate senses to one term. Grammatical variants inside one sense are not drift. Genuine sense splits stay split. Use `fam`.
3. **Cross-book differences: report, do not force.** Where pi-7's term differs from the term the pi-1/pi-2/pi-6 (or pi-3/4/5) termbase gives the same Pāli word in the same meaning, keep the pi-7 term unless the prior term is among the candidates (then rule 1b), and list the case. Write 0-INBOX\temp\pipeline\pi-7-hi\termbase\cross-book-differences.md (pali | sense | pi-7 term | prior term(s) | books), most important first. The user decides those.
4. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash. A term may contain ": " only where the value itself is a heading with a colon; the tools split tag and term at the first ": ".
5. Run `check 1 2315` ("no errors") and the assembler ("no errors").

## Report (short, under 400 words)
- The `check` line and the assembler's summary line.
- The multi-candidate decisions in groups (the 20 most consequential individually), the number of family re-alignments and the most consequential ones.
- Outside-candidate choices with reasons.
- The number of cross-book differences and the 15 most important.
- Anything you are unsure of.
