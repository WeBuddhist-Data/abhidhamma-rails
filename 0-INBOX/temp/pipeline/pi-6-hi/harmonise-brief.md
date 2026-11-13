# Brief: consistency (harmonise) pass, pi-6 Hindi plain zero-shot

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files. Write only in AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\ (the 44 files) and 0-INBOX\temp\pipeline\pi-6-hi\. Never create files at the repo root. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git.

## Situation
Eight agents translated the 43 chapter files of the Yamaka in parallel from one approved sample (0-INBOX\temp\pipeline\pi-6-hi\sample\, built by build_sample_hi.py) and terms file (hi-zeroshot-terms.md), each with builder scripts (pi-6-hi\build_*_hi.py) and a notes file (pi-6-hi\notes-*.md). preamble.md and the sample lines (1-mulayamaka.md non-empty lines 1–122; 2-01-khandhayamaka.md lines 1–27, 219–248, 518–547) are user-approved and must stay unchanged. Where the same Pāli occurs in different files, the Hindi must now be identical, and where the same Pāli phrase or frame is built differently in different chapters, one form must win.

## Method (as the pi-2 pass)
Model: 0-INBOX\temp\pipeline\pi-2-hi\harmonise_hi.py and find_divergences_hi.py (read them; adapt paths and file list). Write pi-6-hi\harmonise_hi.py that applies fixed old → new strings to the Hindi files, where a rule only touches a Hindi line whose aligned Pāli line (non-empty line i ↔ non-empty line i) matches the rule's Pāli pattern. Back up the pre-pass files to pi-6-hi\backup-pre-harmonise\ first (only if it does not exist; always start from it so the script can be rerun), log every rule to pi-6-hi\harmonise-log.tsv (rule, file, replacements, lines). Line counts, IDs, heading levels and dashes must not change. Support --dry.
Do NOT rebuild with the builders (that would drop the pass); edit the outputs with the script. Note in pi-6-hi\harmonise-notes.md which builder constant would need the same change.

## Step 1: find divergences systematically
Write pi-6-hi\find_divergences_hi.py:
- (a) Whole segments and whole lines: group across all files by their Pāli text (normalised: strip ^id, variant brackets, (Ka)/(Kha) labels, collapse spaces); where the Pāli is identical but the Hindi differs, list them.
- (b) Recurring phrases: the being/place phrases in the answers (upapajjantānaṃ, cavantānaṃ, parinibbantānaṃ, pacchimabhavikānaṃ, sacakkhuka/acakkhuka …, itaresaṃ …, catuvokāra/pañcavokāra, asaññasatta, arūpa, apāya …), the short answers (Āmantā, No, Natthi, Uppajjati …), the question frames, the headings, the pariññā frames. Compare their Hindi across files.
Write the result to pi-6-hi\divergences.md. Also compare the "Pāli = Hindi" lines across all notes-*.md.

## Step 2: decisions
Known divergences (decide each with the rule in item 6):
1. Beings with/without a sense organ (sacakkhuka, acakkhuka, sasotaka, asotaka, saghānaka …): Āyatana chapter «आँख के साथ / बिना आँख के», Khandha «आँख वाले लेकिन कान-रहित», Indriya «आँख वाले / आँख से रहित». One scheme for the whole book (with/without each organ; a mixed pair), applied everywhere.
2. The sota pun (dibbasotaṃ, taṇhāsotaṃ): Dhātu chapter «“कान” (सोत)», Indriya chapter «दिव्य कान और तृष्णा की धारा, कान हैं», Āyatana «तृष्णा की धारा». One treatment; no Pāli word in Devanāgarī added as a gloss unless the user's approved sample does so (it does not), so prefer a plain-Hindi solution.
3. catuvokāra / pañcavokāra together: «चार या पाँच समूहों वाले अस्तित्व» vs «चार समूहों वाले और पाँच समूहों वाले अस्तित्व». One form.
4. Short answers: Natthi = «ऐसा कोई नहीं है।» in most chapters vs «ऐसा नहीं होता।» in the Anusaya chapter (7-01 … 7-11). Check what the Pāli context is in each; if the meaning is the same, one form.
5. Feminine/masculine/plural agreement of the process verbs is decided by the subject noun (क्षमता, परिघटना, अनुभूति, रचना feminine; समूह, तत्व, इंद्रिय-क्षेत्र masculine): agreement differences are not divergences, but the same subject must get the same verb form everywhere.
6. For every other divergence of identical Pāli: the approved sample and terms file win, then the chapter whose builder the others imported (build_sample_hi, build_2_hi for the Khandha-type chapters, build_7a_hi for Anusaya, build_10a_hi for Indriya), then pi-1/pi-2 Hindi, then the form with more occurrences. Renderings that differ because the Pāli differs, and source slips translated as written, stay.
7. Do not change the approved sample lines, preamble, or headings fixed in the terms file.

## Step 3: apply and verify
Run harmonise_hi.py. Then run find_divergences_hi.py again: identical-Pāli divergences (a) must be 0 except where the Pāli differs only inside variant brackets or the text was rightly kept as written (list those). For every file:
- `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters <file>.md` (OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py <pali> <hindi>` (OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <pali> <hindi>` (0 mismatches)
- preamble.md and the sample lines unchanged vs backup.
Also grep the whole set for: «—», «:-», «धर्म», «seed», Latin letters outside [..] brackets.

## Final report (short, under 350 words)
Rules applied (count per rule and file group), the choices you made under 1–6 with reasons, divergences left on purpose, check results, and anything that needs the user's eye.
