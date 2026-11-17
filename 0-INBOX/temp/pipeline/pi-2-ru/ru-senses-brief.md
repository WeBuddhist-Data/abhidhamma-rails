# Brief: word-sense-grouper, Pāli→Russian, pi-2 (Vibhaṅga)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own part files, plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-2-ru\senses\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 file, do not run git, never write "seed". You cannot write report files for me: return your report as text.

## Read first
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\russian-style.md (Russian conventions, core terms, the review lessons on pairs that must stay distinct).
- The approved pi-1 Russian run (binding where pi-2 has the same headword in the same sense; pi-2 repeats many pi-1 passages word for word):
  - AI_translation\russian\pi-1-pali-word-russian-senses-plain.md (the merged approved senses: grep it for every headword you meet; 1,341 of pi-2's 4,958 headwords have a line there, 59 of the 120 sample headwords). Reuse its tag wording and splits where the Russian values match; add senses only for values pi-1 does not have.
  - 0-INBOX\temp\pipeline\pi-1-ru\senses\senses-conventions.md (the split/merge conventions and family tags).
  - 0-INBOX\temp\pipeline\pi-1-ru\senses\senses_tool_ru.py (build from a decisions file, verify, todo, show) and decisions-sample.txt (the decisions format).
- Approved Russian senses of other books, for format and wording: AI_translation\russian\pi-4-pali-word-russian-senses-plain.md and pi-5-…-plain.md (grep for headwords you meet).
- pi-2 English senses, AI_translation\english\pi-2-english-senses-plain.md: a good source for English tag wording and for which pi-2 headwords have more than one meaning. It is English, so its splits are a hint, not binding: split the Russian where the Russian values carry different meanings.

## Input
0-INBOX\temp\pipeline\pi-2-ru\senses\agg-part<K>.tsv (the sample uses agg-sample.tsv: the first 90 rows of part 1 plus the next 30 multi-value rows). One line per Pāli headword (case merged, order = first appearance in the map):
`headword <TAB> en≈ English hints <TAB> russian_value=count[example ids] | … <TAB> NDE=<count>`
Column 2 is only a HINT (the English equivalents the English pi-2 map gives that headword). It is not a list of senses.

## Output
0-INBOX\temp\pipeline\pi-2-ru\senses\part<K>-senses.md (the sample: sample-senses.md), same headwords, same order, one line each:
`pali: {english sense tag: рус_a / рус_b; tag2: рус_c}`

## Guidance
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful (as the pi-1/pi-4/pi-5 files do: "{wholesome, said of states (nominative pl.): благой}"). Never copy a Russian value or the bare English hint as the tag. A script may draft tags from a table you write, but you write that table yourself, headword by headword (copying a pi-1 tag for the same headword and sense is fine).
- Grammatical variants of one Russian lemma (number, gender, case, short/long form, participle/infinitive of the same verb) are ONE sense; list them with " / ", most frequent first.
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split into separate senses only for genuinely different meanings (the pi-1 conventions list the known ones: rūpa, dhamma, kāya, citta/mano, vuṭṭhāna …). When unsure, look at the segments by their example ids in AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-2_split_chapters\.
- Values containing " … " (gapped phrases) are kept as written; they are one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " и " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".
- Approved pi-2 map decisions to respect: N-vidhena keywords carry no «классификация» (Duvidhena = «на два вида», Ekavidhena = «по одному»), see 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\ru-map-conventions-pi2.md.

## Parts 1–8 (after the sample): binding
The user approved the sample (senses\sample-senses.md, decisions-sample.txt) AS IS on 2026-11-17, including the three judgement calls: āyatana split «сфера восприятия» (sense base) / «сфера» (head of a named base); vitakko «направленная мысль» (the mental factor) / «мысль» (minor-topic headings); upādāya «производный» / «в связи с» / «в силу»; and the N-group vs division-into-N-kinds split. There are 8 parts of about 620 headwords (same load as the pi-1 parts). The parts run ONE AT A TIME (user), so read the finished earlier parts' decisions files too and keep their tags and splits for the same families.
- senses\senses-conventions.md (READ-ONLY) and senses\senses_tool_ru.py (`build|verify|todo|show|prior|reuse --part K`; READ-ONLY, call it, don't edit it). Write your decisions to senses\decisions-part<K>.txt and build with the tool.
- Part 1 contains the 120 sample headwords: copy their decisions from decisions-sample.txt unchanged.
- The same headword family gets the same tag wording as in the sample and earlier parts (X-indriyaṃ, X-balaṃ, citta-X, a-/an- negatives, the matrix items, the number headings).
- For every headword that pi-1 has, run `prior` and keep the pi-1 tag where the Russian values match.

## Sample only: also write (for the later parts)
- senses\senses-conventions.md: the split/merge conventions for pi-2 Russian (start from the pi-1 file; record what pi-2 adds), with the tags of the recurring headword families.
- senses\senses_tool_ru.py: the pi-1 tool adapted to pi-2 paths (map, Pāli and Russian chapter folders, senses folder), `build|verify|todo|show --part K` plus `sample`. Write your decisions to senses\decisions-sample.txt and build with it.

## Verify (skill step 6) with the tool
The headword list of your output equals the input's, same order, no duplicates; every attested Russian value appears under its headword (allowing the " / "→" и " rewrite); no tag equals its value; every line parses as `hw: {tag: v / v; tag: v}`. Print counts and differences.

## Report (under 400 words, as text)
Headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; how many lines reuse a pi-1 tag; the conventions you settled; 10–15 example lines for review (including the multi-sense ones); anything genuinely unclear.
