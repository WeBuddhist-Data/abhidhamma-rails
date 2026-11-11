# Brief: termbase-builder, Pāli→Hindi plain, pi-1 (Dhammasaṅgaṇī)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`. Write ONLY the files named in your task (in 0-INBOX\temp\pipeline\pi-1-hi\termbase\). Do not touch 1-SOURCES\, 4-SYSTEM\, AI_translation\ (the assembler writes there, not you), and do not run git. Do not use the words "seed" or "unseeded" anywhere.

## Read first

- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-termbase-brief.md: the brief used for the approved pi-3/pi-4/pi-5 Hindi termbases. Its "How to choose" rules 1–5 apply here unchanged; this file only adds what is specific to pi-1.
- AI_translation\audience_profile\plain.md (no Buddhist background; understanding first).
- 0-INBOX\temp\pipeline\hindi-style.md (core terms; binding).
- 0-INBOX\temp\pipeline\pi-1-hi\hi-zeroshot-terms.md (the pi-1 binding term list: headings and all matrix items) and harmonise-notes-hi.md. The user has approved the pi-1 translation built from these.

## Input, output, tools

- Input: AI_translation\hindi\pi-1-pali-word-hindi-senses-plain.md (2,487 headwords, 2,527 senses; 125 senses have 2+ candidates). Line N of this file = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-1-hi\termbase\decisions-part<K>.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based in the senses line). Start the file with a `#` comment line naming your line range.
- Helper (read its docstring): `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\termbase\tb_tool_pi1.py`
  - `list <from> <to> [--multi]`: your senses with candidate counts from the pi-1 map, decisions so far, and the same headword's terms in the approved pi-3/4/5 Hindi termbases ("prior").
  - `fam <regex>`: a whole lemma family across all of pi-1 (use it for every family you touch, e.g. `fam "^vicikicch"`, `fam "sahagat"`).
  - `prior <regex>`: a family in the pi-3/4/5 termbases.
  - `hcount <hindi> …`: how often a string occurs in the harmonised pi-1 Hindi translation.
  - `check <from> <to>`: every multi-candidate sense in your range decided, no forbidden characters, outside-candidate choices listed. Must print "no errors".
- The final assembler (`python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_assemble.py 1`) is run by the coordinator after all parts exist; you only need `check` to pass for your range.

## pi-1 specifics

1. **Order of preference for multi-candidate senses:** (a) a core term in hindi-style.md or the pi-1 term list (hi-zeroshot-terms.md); (b) the term the approved pi-3/4/5 termbases give the same Pāli word in the same meaning ("prior"), when it is among the candidates; (c) the form the pi-1 translation uses most (map counts / hcount); (d) the clearest plain-Hindi candidate. Dictionary form.
2. **Family alignment** (re-align decisions on single-candidate senses) only where the same Pāli lemma in the same meaning drifted to a different Hindi word. Grammatical variants inside one sense (e.g. मन का विषय / मन के विषय) are not drift: choose the dictionary form. Genuine sense splits in the senses file stay split.
3. **Cross-book differences: report, do not force.** Where pi-1's term for a sense differs from the term the pi-3/4/5 termbases agree on for the same Pāli word and meaning, keep the pi-1 term unless the prior term is among the candidates (then rule 1b applies), and list the case in your report under "Cross-book differences" (pali | sense | pi-1 term | prior term(s) | books). The user decides those.
4. **Known pi-1 open points, decide and give the reason:**
   - kammassa katattā: the translation has two forms, «किए गए कर्म के कारण» (list lead) and «कर्म किए जाने के कारण» (elsewhere). Pick one for the whole book.
   - ekaṃsa (and related): «पक्का» vs «एक बात».
   - Same Hindi for different Pāli words; keep them apart where the text puts them side by side (check with `show`-style reading of the segments, or `fam`/`hcount`): nandī and pāmojja (both आनंद); sallakkhaṇā (wisdom list) and sañjānanā (perception list) (both पहचानना); ketu (ketukamyatā) and dhajo, both झंडा, which stand in the same conceit list; saṅkhā and saṅgaṇī (गणना); pathā and magga (मार्ग); samuṭṭhāna and uppanna (उत्पन्न); vatthu and āyatana (आधार). Where a split needs a term outside the candidates, give it as an OUTSIDE choice with its reason.
   - sīlabbata: pi-1 «सदाचार और व्रत», pi-5 «कर्मकांड और व्रत». Cross-book item: report it.
5. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash.

## Report (short, under 300 words)

- The `check` output line for your range.
- Number of multi-candidate decisions and of family re-alignments.
- Outside-candidate choices with reasons.
- The 15 most consequential choices (high-frequency terms, contested pairs, the open points above that fall in your range).
- Cross-book differences (the table described in rule 3).
- Anything you are unsure of.
