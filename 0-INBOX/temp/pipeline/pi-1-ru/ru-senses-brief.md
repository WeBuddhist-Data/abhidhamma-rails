# Brief: word-sense-grouper, Pāli→Russian, pi-1 (Dhammasaṅgaṇī)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own part files, plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-1-ru\senses\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git, never write "seed". You cannot write report files for me: return your report as text.

## Read first
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\russian-style.md (Russian conventions, core terms, the review lessons on pairs that must stay distinct).
- For format and granularity: the user-approved Russian senses files of earlier books, AI_translation\russian\pi-4-pali-word-russian-senses-plain.md and pi-5-…-plain.md (look at 40 lines of each; grep them for headwords you meet, and reuse their tag wording where the meaning is the same).
- The tooling and conventions of the Hindi pi-1 run (adapt, don't copy blindly): 0-INBOX\temp\pipeline\pi-1-ru\ref\hi_senses_tool_pi1.py (build from a decisions file + verify) and ref\hi_senses-conventions.md (how pi-1's headwords were split: rūpa, dhamma, kāya, citta/mano, the matrix items, the synonym strings).

## Input
0-INBOX\temp\pipeline\pi-1-ru\senses\agg-part<K>.tsv (the sample uses agg-sample.tsv). One line per Pāli headword (case merged, order = first appearance in the map):
`headword <TAB> en≈ English hints <TAB> russian_value=count[example ids] | … <TAB> NDE=<count>`
pi-1 has NO English senses file. Column 2 is only a HINT (the English equivalents the English pi-1 map gives that headword). Use it to write good English tags; it is not a list of senses.

## Output
0-INBOX\temp\pipeline\pi-1-ru\senses\part<K>-senses.md (the sample: sample-senses.md), same headwords, same order, one line each:
`pali: {english sense tag: рус_a / рус_b; tag2: рус_c}`

## Guidance
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful (as the pi-4/pi-5 files do: "{wholesome, said of states (nominative pl.): благой}"). Never copy a Russian value or the bare English hint as the tag. A script may draft tags from a table you write, but you write that table yourself, headword by headword.
- Grammatical variants of one Russian lemma (number, gender, case, short/long form, participle/infinitive of the same verb) are ONE sense; list them with " / ", most frequent first.
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split into separate senses only for genuinely different meanings, e.g. rūpa as материальная форма (material form) vs видимая форма (visible object) vs форма / мир форм (the fine-material sphere); dhamma as явление vs объект ума vs Учение; kāya as умственное тело (mental body) vs тело (physical body); mano as ум vs разум (in the citta synonym string); vuṭṭhāna as избавление (from offences) vs выход (from attainments). When unsure, look at the segments by their example ids in AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-1_split_chapters\.
- Values containing " … " (gapped phrases) are kept as written; they are one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " и " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".

## Parts 1–4 (after the sample): binding
The user approved the sample (senses\sample-senses.md, decisions-sample.txt) on 2026-11-14, judgement calls included (ārabbha, parāmāsa, Dukaṃ and kāma splits; cittaṃ ум / вид ума). The parts run ONE AT A TIME (user), so read the finished earlier parts' decisions files too and keep their tags and splits for the same families.
- senses\senses-conventions.md (READ-ONLY) and senses\senses_tool_ru.py (`build|verify|todo|show --part K`; READ-ONLY, call it, don't edit it). Write your decisions to senses\decisions-part<K>.txt and build with the tool.
- Part 1 contains the 120 sample headwords: copy their decisions from decisions-sample.txt unchanged.
- The same headword family gets the same tag wording as in the sample and earlier parts (X-indriyaṃ, X-balaṃ, citta-X, a-/an- negatives, the matrix items).

## Sample only: also write (for the parallel agents)
- senses\senses-conventions.md: the split/merge conventions you settled for pi-1 Russian (modelled on the Hindi file), with the tags of the recurring headword families.
- senses\senses_tool_ru.py: build `<out>-senses.md` from a decisions file you write (decisions-<part>.txt) and verify it; usable by later agents with `--part K`.

## Verify (skill step 6) with a script
The headword list of your output equals the input's, same order, no duplicates; every attested Russian value appears under its headword (allowing the " / "→" и " rewrite); no tag equals its value; every line parses as `hw: {tag: v / v; tag: v}`. Print counts and differences.

## Report (under 400 words, as text)
Headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; the conventions you settled; 10–15 example lines for review (including the multi-sense ones); anything genuinely unclear.
