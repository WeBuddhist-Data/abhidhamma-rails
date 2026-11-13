# Brief: consistency (harmonise) pass, pi-7 Hindi plain zero-shot

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -B -X utf8`. Write only in AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\ (the 76 files) and 0-INBOX\temp\pipeline\pi-7-hi\. Never create files at the repo root or in any system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git, never write "seed". You cannot write report files for me: return your report as text.

## Situation
Fourteen agents translated the 74 remaining files of the Paṭṭhāna in parallel from one approved sample (0-INBOX\temp\pipeline\pi-7-hi\sample\, built by build_sample_hi.py; preamble.md and 1-00-paccaya.md) and terms file (hi-zeroshot-terms.md), each with a builder (pi-7-hi\build_*_hi.py) and a notes file (pi-7-hi\notes-*.md). The user approved the sample, the title «कारण-संबंध», the 24 condition names and the Siyā question frame. preamble.md, 1-00-paccaya.md and the sample lines (1-01-kusalattika.md non-empty lines 1–128, 129–190, 1235–1262) must stay unchanged. Where the same Pāli occurs in different files the Hindi must now be identical, and where the same Pāli word, heading or frame was rendered differently by different agents, one form must win.

My summary of every agent's report, with the divergences already spotted, is 0-INBOX\temp\pipeline\pi-7-hi\run-reports.md (lines marked HARMONISE). Read it and all notes-*.md.

## Method (as the pi-6 pass)
Model: 0-INBOX\temp\pipeline\pi-6-hi\harmonise_hi.py and find_divergences_hi.py (read them; adapt). Write pi-7-hi\harmonise_hi.py that applies fixed old → new strings to the Hindi files, where a rule only touches a Hindi line whose aligned Pāli line (non-empty line i ↔ non-empty line i) matches the rule's Pāli pattern (or a heading level / position condition). Back up the pre-pass files to pi-7-hi\backup-pre-harmonise\ first (only if it does not exist; always start from it so the script can be rerun), log every rule to pi-7-hi\harmonise-log.tsv (rule, file, replacements, lines). Line counts, IDs, heading levels and dashes must not change. Support --dry. Do NOT rebuild with the builders; edit the outputs with the script. Note in pi-7-hi\harmonise-notes.md which builder would need the same change.

## Step 1: find divergences systematically
Write pi-7-hi\find_divergences_hi.py:
- (a) Whole lines: group across all files by their Pāli text (normalised: strip ^id, {…} variants, count markers like "(3)", collapse spaces); where the Pāli is identical but the Hindi differs, list them.
- (b) Recurring words and frames: every heading (by Pāli heading text), the triad and dyad names wherever they occur (headings, closing lines, cross-references such as "kusalattike", "hetudukaṃ"), the pañhāvāra sub-kind labels (sahajātaṃ, purejātaṃ, pacchājātaṃ, nānākkhaṇikā, ārammaṇādhipati, sahajātādhipati, anantarūpanissayo, pakatūpanissayo …), the moment words (anuloma, gotrabhu, vodāna, bhavaṅga, āvajjanā, cuticitta, upapatticitta, paṭisandhi, vuṭṭhāna, parikamma, phalasamāpatti), the counting frames (ghaṭanā, sabhāga, mūlaka, dukaṃ/tikaṃ … headings, the number words), the negated items (na-, nana-, nano-), "X ceva Y ca", "X ceva na ca Y", the editorial notes (saṃkhittaṃ, vitthāretabbaṃ, sadisaṃ, kātabbaṃ, cakkaṃ, gamana, mūlaṃ …), Paccanīyuddhāro, niṭṭhitaṃ.
Write the result to pi-7-hi\divergences.md.

## Step 2: decisions
Order of authority: (1) the approved sample, 1-00-paccaya.md and hi-zeroshot-terms.md; (2) 1-01-kusalattika.md (the file the others follow; it holds the sample); (3) pi-1 Hindi (AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\1-matika.md and the pi-1 termbase) for matrix items, pi-2/pi-6 Hindi for other shared terms; (4) the form with more occurrences. Then:
1. **Triad and dyad names**: one name per triad and per dyad, used identically in its headings, in combined headings (dyad-triad, triad-dyad, triad-triad, dyad-dyad), in closing lines and in cross-references. Pattern «<X> वाला तीन/दो का वर्गीकरण» with X taken from the pi-1 item wording. The name used in the triad's or dyad's own file (1-xx/2-xx for triads, 3-xx/4-01 for dyads) is the starting point; fix only names that are ungrammatical or unreadable (e.g. «कर्म से उत्पन्न वाला»), keeping the pi-1 wording, and list every name you set in harmonise-notes.md as a table (Pāli | Hindi).
2. **Paccanīyuddhāro, niṭṭhitaṃ (closing lines), the sub-kind labels, nānākkhaṇikā, the moment words, ghaṭanā, sabhāga, mūla (series start), gamana, cakkaṃ, number words beyond 23**: one form each, by the order of authority.
3. **Double negation** (nanahetu etc.): the unquoted form «मूल रूपी न होने वाली न होने वाली»; no quotation marks around items.
4. **"X ceva na ca Y"**: the pi-1 wording of the same matrix item exactly.
5. **{…} editorial notes or queries without a siglum** (e.g. {hetuyā aṭṭha?}): keep the Pāli inside «[पाठभेद: <Pāli>]», the same way as the sigla variants. Never translate bracket contents.
6. **Count lines and ghaṭanā lines**: the sample's count_hi format (commas, «और» before the last item), no quotation marks.
7. Agreement differences decided by the subject (plural subject «कारण होती हैं») are not divergences, but the same subject gets the same verb form everywhere.
8. Source slips translated as written stay as written (user rule: no emendations). Renderings that differ because the Pāli differs stay.
9. Do not change preamble.md, 1-00-paccaya.md or the sample lines.

## Step 3: apply and verify
Run harmonise_hi.py. Then run find_divergences_hi.py again: identical-Pāli divergences (a) must be 0 except where the Pāli differs only inside {…} or the text was rightly kept as written (list those). For every file:
- `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-7_split_chapters AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters <file>.md` (OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py <pali> <hindi>` (OK apart from the expected {…} bracket flags and the "?" flags on Siyā lines)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <pali> <hindi>` (0 mismatches)
- preamble.md, 1-00-paccaya.md and the sample lines unchanged vs backup.
Also grep the whole set for «—», «:-», «धर्म», «seed», Latin letters outside [..] brackets, CR, double blank lines.

## Final report (short, under 400 words)
Rules applied (count per rule and file group), the names and forms you chose under 1–6 with reasons, divergences left on purpose, check results, and anything that needs the user's eye.
