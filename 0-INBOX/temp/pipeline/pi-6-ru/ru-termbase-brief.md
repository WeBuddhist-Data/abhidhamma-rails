# Brief: termbase-builder, Pāli→Russian plain, pi-6 (Yamaka)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B`. LF line endings. Write ONLY in 0-INBOX\temp\pipeline\pi-6-ru\termbase\. Do not touch 1-SOURCES\, 4-SYSTEM\ or AI_translation\ (the assembler writes there, not you), do not edit any pi-1 … pi-5 file, never create files at the repo root (not even an empty one) or in a system temp folder, do not run git. Never use the words "seed" or "unseeded" anywhere. Grep only the specific files named here, never a whole folder. No Vietnamese files. You cannot write report files for me: return your report as text.

The user approves the termbase explicitly afterwards; your job is a clean, consistent proposal plus the list of points the user must decide.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\pi-2-ru\ru-termbase-brief.md (the pi-2 Russian brief; its rules apply here with "pi-6" for "pi-2" where this brief does not say otherwise) and 0-INBOX\temp\pipeline\hindi-termbase-brief.md, section "How to choose".
- The user's termbase decisions of the earlier books (binding wherever pi-6 has the same Pāli word in the same meaning): 0-INBOX\temp\pipeline\pi-1-ru\termbase\APPROVED.md, 0-INBOX\temp\pipeline\pi-2-ru\termbase\APPROVED.md.
- AI_translation\audience_profile\plain.md (no Buddhist background; understanding first).
- 0-INBOX\temp\pipeline\russian-style.md (core terms and the pairs that must stay distinct; binding).
- The pi-6 decisions the user approved: 0-INBOX\temp\pipeline\pi-6-ru\ru-zeroshot-terms.md, pi-6-ru\zeroshot-coordinator-rules.md, pi-6-ru\mapper-ru\ru-map-conventions-pi6.md, pi-6-ru\senses\senses-conventions.md.

## Input, output, tools
- Input: AI_translation\russian\pi-6-pali-word-russian-senses-plain.md (1,126 headwords, 1,133 senses; only 7 senses have 2+ candidates: the Yamaka is very regular). Line N = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-6-ru\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based within the senses line). Start the file with a `#` comment line.
- Helper: `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-6-ru\termbase\tb_tool_ru.py` (READ-ONLY; call it, don't edit it): `list <from> <to> [--multi]`, `fam <regex>`, `prior <regex>` (the approved pi-1 … pi-5 Russian termbases), `hcount <russian> …` (the merged pi-6 Russian zero-shot), `check <from> <to>` (must print "no errors" for 1 1126).
- Then run the assembler yourself to confirm: `python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_assemble.py 6 russian ru plain` must print "no errors" (it writes the termbase and termbase-decisions.md; that is expected).
- You may write a read-only cross-book helper in termbase\ (pi-2-ru\termbase\crossbook_ru.py is the model: senses whose term differs from the approved pi-1 … pi-5 term for the same headword and meaning).

## Russian pi-6 specifics
1. **Order of preference for multi-candidate senses:** (a) a core term in russian-style.md, a user decision (pi-1 / pi-2 APPROVED.md, the pi-6 decisions above); (b) the approved earlier-book term for the same Pāli word in the same meaning, when it is among the candidates; (c) the form the pi-6 translation uses most (map counts / hcount); (d) the clearest plain-Russian candidate. Dictionary form. A gapped candidate («момент распада … ума», «существование … с пятью составляющими») is never the term when the plain phrase is a candidate.
2. **Family alignment** (decisions on single-candidate senses) only where the same Pāli lemma in the same meaning drifted to a different Russian word across the chapters. Grammatical variants inside one sense are not drift. The approved sense splits stay split (arahato, Rūpadhātuṃ, the dukkha forms, rūpaṃ, upapajjissati).
3. **Cross-book differences: report, do not force.** Where pi-6's term differs from the approved earlier term for the same Pāli word and meaning, keep the pi-6 term unless the prior term is among the candidates (then 1b applies), and list the case under "Cross-book differences" (pali | sense | pi-6 term | prior term(s) | books). Known ones: kāyikaṃ / cetasikaṃ dukkhaṃ «телесное / душевное страдание» (pi-1 / pi-2 «… боль»); pajahati «устранять» (pi-5 «отбрасывать»); sukhaṃ «удовольствие» (pi-1 «счастье»); ñāṇavippayutta «без знания» (pi-2 «не связанный со знанием»). The user decides those.
4. **Points for the user (report with the segments, do not change the translation):**
   - Pacchimabhavikānaṃ: one sense with two candidates (user-approved). Propose the term, and say that the translation keeps «в последний раз» before «перерождается» (one person group, coordinator rule) so the rails step needs a note.
   - The dhātu-question heading «об элементах» in the anusaya chapter, where dhātu means plane.
   - uppajjamānaṃ / nirujjhamānaṃ: «возникающий / прекращающийся» (pi-5) vs the noun in the past-time section.
5. **Keep distinct Pāli terms distinct** where the text puts them side by side (check with `fam`, `hcount` and the segments): the seven anusayas; uppajjati «возникать» vs upapajjati «перерождаться»; pajahati «устранять» vs parijānāti «полностью понимать» vs bhāveti «развивать» vs sacchikaroti «осуществлять»; ekamūla «имеющий общий корень» vs aññamaññamūla «имеющий взаимный корень»; hetu «причина» (hetuvāra only) vs mūla «корень».
6. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash. Gapped values with " … " are allowed only where no plain candidate exists.
7. **Outside terms:** only when every candidate is wrong for a plain reader; give the reason. These need the user's approval.

## Report (under 450 words, as text)
- The `check` and assembler output lines.
- Number of multi-candidate decisions and of family re-alignments.
- Outside-candidate choices with reasons.
- The 15 most consequential choices.
- Cross-book differences (the table described in rule 3), the main ones first.
- Points for the user.
- Anything you are unsure of.
