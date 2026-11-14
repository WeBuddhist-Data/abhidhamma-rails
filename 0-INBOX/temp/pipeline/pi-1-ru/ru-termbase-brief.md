# Brief: termbase-builder, Pāli→Russian plain, pi-1 (Dhammasaṅgaṇī)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY in 0-INBOX\temp\pipeline\pi-1-ru\termbase\. Do not touch 1-SOURCES\, 4-SYSTEM\ or AI_translation\ (the assembler writes there, not you), never create files at the repo root or in a system temp folder, do not run git. Never use the words "seed" or "unseeded" anywhere. You cannot write report files for me: return your report as text.

The user approves the termbase explicitly afterwards; your job is a clean, consistent proposal plus the list of points the user must decide.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-termbase-brief.md, section "How to choose" (rules 1–5). They apply here with Russian in place of Hindi; this brief adds what is specific to Russian pi-1.
- AI_translation\audience_profile\plain.md (no Buddhist background; understanding first).
- 0-INBOX\temp\pipeline\russian-style.md (core terms and the review lessons on pairs that must stay distinct; binding).
- 0-INBOX\temp\pipeline\pi-1-ru\ru-zeroshot-terms.md (the pi-1 term list: headings and all matrix items) and pi-1-ru\harmonise-notes.md. The user approved the pi-1 translation built from these.
- 0-INBOX\temp\pipeline\pi-1-ru\agents-run.md: the user decisions so far (mātikā «матрица», vicāra «удержание мысли», saṅkhāra «формирующие факторы», dosa «злоба», asaṅkhata «необусловленное», paṭiccasamuppāda «возникновение в зависимости от условий», pahātabbahetukā «чьи корни устраняются …», cittuppāda «вид ума» in ch5, the senses-sample splits).

## Input, output, tools
- Input: AI_translation\russian\pi-1-pali-word-russian-senses-plain.md (2,479 headwords, 2,528 senses; 106 senses have 2+ candidates). Line N = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-1-ru\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based within the senses line). Start the file with a `#` comment line.
- Helper (read its docstring; it was adapted from the Hindi tool, so "Hindi" in its help text means Russian): `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\termbase\tb_tool_ru.py`
  - `list <from> <to> [--multi]`: senses with candidate counts from the pi-1 map, decisions so far, and the same headword's terms in the approved Russian pi-3/4/5 termbases ("prior").
  - `fam <regex>`: a whole lemma family across pi-1.
  - `prior <regex>`: a family in the pi-3/4/5 Russian termbases.
  - `hcount <russian> …`: occurrences in the merged pi-1 Russian zero-shot.
  - `check <from> <to>`: every multi-candidate sense decided, no forbidden characters, outside choices listed. Must print "no errors" for 1 2479.
- Then run the assembler yourself to confirm: `python -I -X utf8 0-INBOX\temp\pipeline\termbase_assemble.py 1 russian ru plain` must print "no errors" (it writes the termbase and termbase-decisions.md; that is expected).

## Russian pi-1 specifics
1. **Order of preference for multi-candidate senses:** (a) a core term in russian-style.md, the pi-1 term list or a user decision above; (b) the term the approved pi-3/4/5 Russian termbases give the same Pāli word in the same meaning ("prior"), when it is among the candidates; (c) the form the pi-1 translation uses most (map counts / hcount); (d) the clearest plain-Russian candidate. Dictionary form (nominative; adjectives masculine singular unless the concept is plural; verbs infinitive or the participle the text uses).
2. **Family alignment** (decisions on single-candidate senses) only where the same Pāli lemma in the same meaning drifted to a different Russian word. Grammatical variants inside one sense are not drift: choose the dictionary form. The approved sense splits stay split.
3. **Cross-book differences: report, do not force.** Where pi-1's term differs from what pi-3/4/5 agree on for the same Pāli word and meaning (e.g. dhammāyatana: pi-1 «объекты ума», pi-3/4 «умственные объекты»), keep the pi-1 term unless the prior term is among the candidates (then 1b applies), and list the case under "Cross-book differences" (pali | sense | pi-1 term | prior term(s) | books). The user decides those.
4. **Keep distinct Pāli terms distinct** where the text puts them side by side (check with `fam`, `hcount` and the segments). Known points, decide and give the reason:
   - abhiniveso «приверженность / убеждённость» vs sīlabbataparāmāsa «приверженность обрядам и обетам» (they stand in one list).
   - parāmāsa «искажение» vs «приверженность» (the approved split).
   - kusalato / kiriyato / vipākato: one sense each with «благой ум / в благом виде» etc.; choose one term per sense.
   - sacca «истинный» vs «истина», eva «полностью» vs «несомненно» (thin splits; keep unless clearly wrong, and say so).
   - vīriya «усердие» vs padhāna / vāyāma «усилие»; vicikicchā «колебание» vs kaṅkhā «сомнение»; kukkucca «угрызения» vs uddhacca «беспокойство»; mettā vs abyāpāda (russian-style.md).
   - sammappadhāna «правильное усилие» = sammāvāyāma's Russian (user-accepted pairing; do not change, just list it).
5. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash. Gapped values with " … " are allowed as attested.
6. **Outside terms:** only when every candidate is wrong for a plain reader; give the reason. These need the user's approval.

## Report (under 450 words, as text)
- The `check` and assembler output lines.
- Number of multi-candidate decisions and of family re-alignments.
- Outside-candidate choices with reasons.
- The 15 most consequential choices (high-frequency terms, contested pairs, the open points above).
- Cross-book differences (the table described in rule 3), the main ones first.
- Anything you are unsure of.
