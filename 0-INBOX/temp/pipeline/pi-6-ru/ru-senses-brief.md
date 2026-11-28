# Brief: word-sense-grouper, Pāli→Russian, pi-6 (Yamaka)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings. Write ONLY your own part files, plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-6-ru\senses\. Never create files at the repo root (not even an empty one) or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 … pi-5 file, do not run git, never write "seed" or "unseeded". Grep only the specific files named here, never a whole folder. No Vietnamese files. You cannot write report files for me: return your report as text.

## Read first
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\russian-style.md (Russian conventions, core terms, the review lessons on pairs that must stay distinct).
- The approved Russian senses of the earlier books (binding where pi-6 has the same headword in the same sense): AI_translation\russian\pi-1 … pi-5-pali-word-russian-senses-plain.md (grep them for every headword you meet; 286 of pi-6's 1,126 headwords have a line in one of them, 29 of the 123 sample headwords). Reuse their tag wording and splits where the Russian values match; add senses only for values they do not have.
- 0-INBOX\temp\pipeline\pi-1-ru\senses\senses-conventions.md and 0-INBOX\temp\pipeline\pi-2-ru\senses\senses-conventions.md (the split/merge conventions and family tags).
- 0-INBOX\temp\pipeline\pi-2-ru\senses\senses_tool_ru.py (build from a decisions file, verify, todo, show, prior, reuse) and decisions-sample.txt (the decisions format).
- pi-6 English senses, AI_translation\english\pi-6-pali-word-english-senses-plain.md: a good source for English tag wording and for which pi-6 headwords have more than one meaning. It is English, so its splits are a hint, not binding: split the Russian where the Russian values carry different meanings.
- The approved pi-6 map conventions: 0-INBOX\temp\pipeline\pi-6-ru\mapper-ru\ru-map-conventions-pi6.md and the notes-map-G*.md files there (why a headword has the values it has: root compounds, tense values, persons and planes, moment phrases).

## Input
0-INBOX\temp\pipeline\pi-6-ru\senses\agg-part<K>.tsv (the sample uses agg-sample.tsv: the first 110 rows of part 1 plus every multi-value row of the book, 123 rows, 14 multi-value). One line per Pāli headword (case merged, order = first appearance in the map):
`headword <TAB> en≈ English hints <TAB> russian_value=count[example ids] | … <TAB> NDE=<count>`
Column 2 is only a HINT (the English equivalents the English pi-6 map gives that headword). It is not a list of senses.

## Output
0-INBOX\temp\pipeline\pi-6-ru\senses\part<K>-senses.md (the sample: sample-senses.md), same headwords, same order, one line each:
`pali: {english sense tag: рус_a / рус_b; tag2: рус_c}`

## Guidance
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful (as the earlier files do: "{wholesome, said of states (nominative pl.): благой}"). Never copy a Russian value or the bare English hint as the tag. A script may draft tags from a table you write, but you write that table yourself, headword by headword (copying an earlier book's tag for the same headword and sense is fine).
- Grammatical variants of one Russian lemma (number, gender, case, short/long form, participle/infinitive of the same verb, the perfective / imperfective pair of one verb) are ONE sense; list them with " / ", most frequent first.
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split into separate senses only for genuinely different meanings (the earlier conventions list the known ones: rūpa, dhamma, kāya, citta/mano …). When unsure, look at the segments by their example ids in AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-6_split_chapters\. Multi-value headwords in the sample to decide with reasons: arahato (архат / Достойный in the homage line), Pacchimabhavikānaṃ (жить последней жизнью / в последний раз), Rūpadhātuṃ (мир форм / элемент видимых форм), dukkhaṃ (боль as the faculty / страдание as the truth), upapajjissati (one value comes from a source slip rendered as meant at ^6-3-212), uppajjamānaṃ / nirujjhamānaṃ (participle / the moment noun in the past-time section), the «… ума» gapped moment phrases.
- Values containing " … " (gapped phrases) are kept as written; they are one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " и " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".

## Parts 1–2 (after the sample): binding
The user approved the sample (senses\sample-senses.md, decisions-sample.txt) AS IS on 2026-11-27, including Pacchimabhavikānaṃ as ONE sense with two candidates and the splits of arahato, Rūpadhātuṃ, the dukkha forms, rūpaṃ and upapajjissati. There are 2 parts of 563 headwords; they run at the same time (user: pi-6 runs agents in parallel), one agent per part.
- senses\senses-conventions.md (READ-ONLY) and senses\senses_tool_ru.py (`build|verify|todo|show|prior|reuse --part K`; READ-ONLY, call it, don't edit it). Write your decisions to senses\decisions-part<K>.txt and build with the tool.
- Every headword that is in the sample (agg-sample.tsv: the first 110 rows of part 1 and the multi-value rows, some of which are in part 2): copy its decision from decisions-sample.txt unchanged.
- The same headword family gets the same tag wording as in the sample and senses-conventions.md (root compounds, tense forms, persons, planes, moment phrases, X-indriyaṃ, the seven anusayas, headings). The other part runs at the same time: follow the conventions file closely so both parts agree; the coordinator compares the families afterwards.
- For every headword an earlier book has, run `prior` and keep the earlier tag where the Russian values match.

## Sample only: also write (for the later parts)
- senses\senses-conventions.md: the split/merge conventions for pi-6 Russian (start from the pi-1 / pi-2 files; record what pi-6 adds: the root compounds, the tense pairs, the person / plane / moment phrases, the yamaka headings), with the tags of the recurring headword families.
- senses\senses_tool_ru.py: the pi-2 tool adapted to pi-6 paths (map, Pāli and Russian chapter folders, senses folder; `prior` over the pi-1 … pi-5 Russian senses files), `build|verify|todo|show|prior|reuse --part K` plus `sample`. Write your decisions to senses\decisions-sample.txt and build with it.

## Verify (skill step 6) with the tool
The headword list of your output equals the input's, same order, no duplicates; every attested Russian value appears under its headword (allowing the " / "→" и " rewrite); no tag equals its value; every line parses as `hw: {tag: v / v; tag: v}`. Print counts and differences.

## Report (under 400 words, as text)
Headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; how many lines reuse an earlier book's tag; the conventions you settled; 10–15 example lines for review (including the multi-sense ones); anything genuinely unclear.
