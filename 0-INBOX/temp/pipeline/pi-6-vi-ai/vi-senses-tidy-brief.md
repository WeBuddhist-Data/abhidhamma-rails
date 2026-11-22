# Brief: tidy pass over the pi-6 Vietnamese senses parts 1-5, then merge

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (scripts with the Write tool at full paths; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8 -B`. You are the only agent running. Edit ONLY 0-INBOX\temp\pipeline\pi-6-vi-ai\senses\decisions-part1..5.txt (never decisions-sample.txt: the sample's 91 lines inside part 1 stay as they are), rebuild with senses_tool_vi.py, and write new files only in senses\ (a tidy script, tidy-log.tsv, tidy-notes.md) and the merged output named below. LF line endings. Nothing at the repo root, outside the repo or in a system temp folder; no __pycache__. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git, never write "seed". No web. Return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. Grep only single named files.

## Context
Five agents grouped the senses in parallel (vi-senses-brief.md; conventions senses\senses-conventions.md; the approved sample decisions-sample.txt). Each part verifies, but the same headword family may be worded differently across parts. agents-run.md ("Word senses") lists their open points.

## Do
1. Back up decisions-part1..5.txt to senses\backup-pre-tidy\.
2. Find family wording differences in code across the five parts (same family = same Pāli pattern; compare the tag after the grammatical label is stripped), at least these families: the X-mūlakaṃ section labels («phần dựa trên …»); the «…cittassa uppādakkhaṇe / bhaṅgakkhaṇe» phrases; the samaṅgī persons (maggasamaṅgī, aggamaggasamaṅgī, anāgāmimaggasamaṅgī, cittasamaṅgī, pacchimacittasamaṅgī); the Suddha-X-vāro and -mūlacakkavāro headings; the other X-vāro / -vāre headings; the yamaka titles; the past / future verb tags (pajahittha «a defilement already given up» describes the object: re-gloss the act, as the uppajjittha / parijānittha tags do); the participles uppajjamāna / nirujjhamāna, uppanna / niruddha (same wording pattern for each pair); the X-dhātu(ṃ) members (one pattern «the X element»); kāmadhātuṃ / rūpadhātuṃ / arūpadhātuṃ (in the Anusaya chapters they are only the plane: a plane tag, not «element or plane»; Rūpadhātuṃ in part 3 keeps its two senses).
3. kāyasaṅkhāro / vacīsaṅkhāro / cittasaṅkhāro: in the Yamaka these are defined in the text (^6-6-1: assāsapassāsā kāyasaṅkhāro, vitakkavicārā vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro). Their reused pi-1 … pi-5 tag («volition expressed through the body» etc.) is another meaning: give them pi-6 tags that say this (e.g. "the bodily formation, in-and-out breathing (nominative sg.)").
4. Choose one wording per family (prefer the sample's / senses-conventions.md wording, then a pi-1 … pi-5 tag, then the majority), apply it with exact replacements in the decisions files (logged in tidy-log.tsv: part, headword, old tag, new tag, reason), rebuild each part with the tool and verify each.
5. Merge: adapt 0-INBOX\temp\pipeline\pi-5-vi-ai\senses\merge_senses_vi.py to pi-6 (copy to senses\merge_senses_vi.py; do not edit the pi-5 file) and run it with --write → AI_translation\vietnamese\pi-6-pali-word-vietnamese-senses-plain.md (headwords in agg-all.tsv order, five parts VERIFY OK, no warnings).

## Verify
Every part: senses_tool_vi.py verify --part K → VERIFY OK; the merged file has 1,126 headwords in agg-all order; part 1's 91 sample lines unchanged (compare with sample-senses.md); LF, no CR.

## Report (under 350 words, as text)
Families found and the wording chosen for each; lines changed per part; verify results; the merged file's counts (headwords, senses, multi-sense, multi-candidate); anything left for the user (termbase level).
