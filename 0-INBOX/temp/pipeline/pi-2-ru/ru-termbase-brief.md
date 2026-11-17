# Brief: termbase-builder, Pāli→Russian plain, pi-2 (Vibhaṅga)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY in 0-INBOX\temp\pipeline\pi-2-ru\termbase\. Do not touch 1-SOURCES\, 4-SYSTEM\ or AI_translation\ (the assembler writes there, not you), do not edit any pi-1 file, never create files at the repo root or in a system temp folder, do not run git. Never use the words "seed" or "unseeded" anywhere. You cannot write report files for me: return your report as text.

The user approves the termbase explicitly afterwards; your job is a clean, consistent proposal plus the list of points the user must decide.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\pi-1-ru\ru-termbase-brief.md (the pi-1 Russian brief: its rules 1–6 apply here with "pi-2" for "pi-1"; this brief adds what is specific to pi-2) and 0-INBOX\temp\pipeline\hindi-termbase-brief.md, section "How to choose".
- 0-INBOX\temp\pipeline\pi-1-ru\termbase\APPROVED.md: the user's pi-1 termbase decisions (binding wherever pi-2 has the same Pāli word in the same meaning).
- AI_translation\audience_profile\plain.md (no Buddhist background; understanding first).
- 0-INBOX\temp\pipeline\russian-style.md (core terms and the pairs that must stay distinct; binding).
- 0-INBOX\temp\pipeline\pi-2-ru\ru-zeroshot-terms.md, pi-2-ru\harmonise-notes.md, pi-2-ru\mapper-ru\ru-map-conventions-pi2.md, pi-2-ru\senses\senses-conventions.md and pi-2-ru\senses\parts-notes.md (the pi-2 terms, the consistency pass, the map and senses conventions the user approved).

## Input, output, tools
- Input: AI_translation\russian\pi-2-pali-word-russian-senses-plain.md (4,958 headwords, 5,112 senses; 170 senses have 2+ candidates). Line N = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-2-ru\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based within the senses line). Start the file with a `#` comment line.
- Helper: `python -I -X utf8 0-INBOX\temp\pipeline\pi-2-ru\termbase\tb_tool_ru.py` (READ-ONLY; call it, don't edit it)
  - `list <from> <to> [--multi]`: senses with candidate counts from the pi-2 map, decisions so far, and the same headword's terms in the approved Russian pi-1/3/4/5 termbases ("prior").
  - `fam <regex>`: a whole lemma family across pi-2.
  - `prior <regex>`: a family in the pi-1/3/4/5 Russian termbases.
  - `hcount <russian> …`: occurrences in the merged pi-2 Russian zero-shot.
  - `check <from> <to>`: every multi-candidate sense decided, no forbidden characters, outside choices listed. Must print "no errors" for 1 4958.
- Then run the assembler yourself to confirm: `python -I -X utf8 0-INBOX\temp\pipeline\termbase_assemble.py 2 russian ru plain` must print "no errors" (it writes the termbase and termbase-decisions.md; that is expected).

## Russian pi-2 specifics
1. **Order of preference for multi-candidate senses:** (a) a core term in russian-style.md, a user decision (pi-1 APPROVED.md, the pi-2 decisions below) or the pi-2 term list; (b) the approved pi-1 Russian termbase term for the same Pāli word in the same meaning, when it is among the candidates (pi-2 repeats many pi-1 passages word for word); then pi-3/4/5; (c) the form the pi-2 translation uses most (map counts / hcount); (d) the clearest plain-Russian candidate. Dictionary form (nominative; adjectives masculine singular unless the concept is plural; verbs infinitive or the participle the text uses).
2. **Family alignment** (decisions on single-candidate senses) only where the same Pāli lemma in the same meaning drifted to a different Russian word. Grammatical variants inside one sense are not drift: choose the dictionary form. The approved sense splits stay split.
3. **Cross-book differences: report, do not force.** Where pi-2's term differs from the approved pi-1 term (or what pi-3/4/5 agree on) for the same Pāli word and meaning, keep the pi-2 term unless the prior term is among the candidates (then 1b applies), and list the case under "Cross-book differences" (pali | sense | pi-2 term | prior term(s) | books). Known one: the god names (pi-1 «боги Аканиттха» vs pi-2 «высочайшие боги»). The user decides those.
4. **User decisions on pi-2 so far (binding):** N-vidhena = «на два вида», «по одному», «на десять видов» … WITHOUT «классификация»; non-word fragments, bare prepositions and keywords with no word of their own are NDE (already out of the senses); the senses sample and its splits (āyatana «сфера восприятия» / «сфера», vitakko «направленная мысль» / «мысль», upādāya «производный» / «в связи с» / «в силу», N-group vs division into N kinds).
5. **Keep distinct Pāli terms distinct** where the text puts them side by side (check with `fam`, `hcount` and the segments). Known points from the senses parts, decide and give the reason:
   - **rūpataṇhā:** the senses file has only «жажда мира форм», but the Russian also has «жажда видимых форм» 5 times (the sense-object cravings, e.g. 2-909, where the map holds one value per keyword per segment). Do not invent a sense; report it under "points for the user" with the segments, so the rails step can keep both.
   - **veramaṇī** «воздержание / уклонение» vs **virati** «воздержание»: they stand side by side in the abstention lists; keep them apart (the senses parts note: «воздержание» in the precept names, «уклонение» in the abstention list).
   - **nimmāna** «творение / сотворение», **upapatti** «перерождение / рождение» (upapattidevā «боги по рождению»): pick one each or say why both contexts need their own word.
   - **sukhaṃ «приятное» (2-594)** is bodily pleasure in the jhāna passage but sits in the happiness sense; report, don't force.
   - The pi-1 pairs: vīriya «усердие» vs padhāna / vāyāma «усилие»; vicikicchā «колебание» vs kaṅkhā «сомнение»; kukkucca «угрызения» vs uddhacca «беспокойство»; mettā vs abyāpāda; abhiniveso «убеждённость» vs sīlabbataparāmāsa; sārāga family «пристрастие» vs rāga «страсть»; ujutā «прямизна» vs ujukatā «прямота».
   - Other open points the user knows of (report the termbase term, don't change the translation): veramaṇī as above; dhamme ñāṇaṃ (two senses); sāmisa «плотский»; ātāpa «ревностность»; the wind names (vāta senses).
6. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash. Gapped values with " … " are allowed as attested.
7. **Outside terms:** only when every candidate is wrong for a plain reader; give the reason. These need the user's approval.

## Report (under 450 words, as text)
- The `check` and assembler output lines.
- Number of multi-candidate decisions and of family re-alignments.
- Outside-candidate choices with reasons.
- The 15 most consequential choices (high-frequency terms, contested pairs, the points above).
- Cross-book differences (the table described in rule 3), the main ones first.
- Points for the user (rūpataṇhā etc.).
- Anything you are unsure of.
