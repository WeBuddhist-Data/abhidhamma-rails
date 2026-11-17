# Brief: consistency (harmonise) pass, pi-2 Russian plain zero-shot

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write only in AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\ (the 19 part files) and 0-INBOX\temp\pipeline\pi-2-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the builders, do not run git, never write "seed". You cannot write report files for me: return your report as text.

## Situation
Ten agents translated the 18 chapters one after another, each importing the earlier builders (0-INBOX\temp\pipeline\pi-2-ru\build_*_ru.py, notes-*.md, ru-zeroshot-terms.md). preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md (= pi-2-ru\ch1-sample.md) are user-approved and stay unchanged. Where the same Pāli occurs in different chapters, or in pi-1 (whose Russian is final and reviewed: AI_translation\russian\pi-1-russian-plain-rails_split_chapters\), the Russian must now be identical, and one Pāli term gets one Russian term. Rules: russian-style.md.

## Method (as the pi-1 pass)
Models: 0-INBOX\temp\pipeline\pi-1-ru\harmonise_ru.py and find_divergences_ru.py (read them).
Write pi-2-ru\harmonise_ru.py: fixed old → new strings applied to the Russian chapter files, each rule touching only a Russian line whose aligned Pāli line (non-empty line i ↔ i) matches the rule's Pāli pattern (or a listed block ID). Back up the pre-pass files to pi-2-ru\backup-pre-harmonise\ once and always start from the backup (rerunnable); log every replacement to pi-2-ru\harmonise-log.tsv (rule, part, line, old, new). Line counts, IDs, heading levels and dashes must not change. Support --dry. Do NOT rebuild with the builders; note in pi-2-ru\harmonise-notes.md which builder constants would need the same change.

## Step 1: find divergences
Write pi-2-ru\find_divergences_ru.py:
- (a) whole segments across all 18 chapters grouped by normalised Pāli (strip ^id and variant brackets, collapse spaces, drop the space before punctuation): identical Pāli, different Russian → list;
- (b) the same for pi-2 segments whose Pāli is identical to a pi-1 segment (pi-1 Russian wins);
- (c) recurring Pāli terms and phrases across chapters (collect from the notes files and builders, confirm in the outputs): at least the realm and god names, kāmesumicchācāra, veramaṇī, the vīriya / paññā / sati / samādhi strings, the jhāna formula pieces, the lokuttara openings, the question-section predicates, «это называется «X»», «нельзя определить …», the counted names, sajjha / rajata, dhamme ñāṇaṃ, abhiññeyya.
Write the result to pi-2-ru\divergences.md.

## Step 2: decisions
Fixed by the coordinator:
1. **^2-220 (5-indriyavibhango) is a real error:** the vīriyindriya string ends «…, сила усердия, правильное усилие, – это …», but the Pāli ends «vīriyabalaṃ – idaṃ vuccati» (no sammāvāyāmo). Remove «, правильное усилие» there. Check every other vīriya string in the book against its own Pāli line the same way (an item in the Russian that the Pāli line lacks, or the reverse) and fix what you find.
2. **kāmesumicchācāra** = «неправильное поведение в чувственных удовольствиях» everywhere (ch4, 11, 17, pi-5); align ch14's precept names («неподобающее поведение»).
3. **Akaniṭṭha and the formless-realm gods:** one wording within pi-2. Use the god-list wording of ch18 (^2-1021 … ^2-1028, from pi-5: «высочайшие боги», «боги, достигшие сферы …») also in ^2-1020, and list the difference from pi-1 (^1-1287 ff. «богов Аканиттха», «богов, рождённых в сфере …») in harmonise-notes.md under "cross-book differences" for the user.
4. **sajjha / rajata** (both «серебро» in ch3): keep them apart where they stand in the same list; check the commentary (1-SOURCES\Commentaries\, Vibhaṅga aṭṭhakathā) and pi-1's rendering of the same list, and choose; report the choice.
5. **dhamme ñāṇaṃ:** «знание Учения» (the path-knowledge catukka in ch16) vs «знание явлений» (the paṭisambhidā formula, ch15/16) differ in meaning: keep both, list it.
6. **The one remaining «X, – это» after a plain noun or list** (find it): drop the comma.
7. For every other divergence of identical Pāli: pi-1 Russian wins; then the approved sample and ru-zeroshot-terms.md; then an earlier Russian book (pi-3/4/5 termbases in AI_translation\russian\); then the chapter with more occurrences.
8. Do not change: the approved sample; renderings that differ because the Pāli differs; source slips translated as written (each chapter's notes file lists them); deliberate context splits recorded in the notes (e.g. veramaṇī «воздержание» in precept names vs «уклонение» in the abstention list, saṅgati «встреча» (people) vs «сочетание» (dependent origination)).

## Step 3: apply and verify
Run harmonise_ru.py, then find_divergences_ru.py again: (a) and (b) must be 0 except where the Pāli differs only inside variant brackets or the text was rightly kept as written (list those). For every chapter:
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters <ch>.md` (OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <russian>` (0 mismatches, 0 extra)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py <pali> <russian> …` (OK)
- preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md unchanged vs the backup.
Also grep the whole set for: «—», «:-», «ли» as a word, «seed», Latin outside [..], «неподобающее поведение», «сила усердия, правильное усилие, – это» on a line whose Pāli lacks sammāvāyāmo.

## Final report (under 450 words, as text)
Rules applied (count per rule and chapter), the choices you made under 4 and 7 with reasons, divergences left on purpose, cross-book differences for the user, check results.
