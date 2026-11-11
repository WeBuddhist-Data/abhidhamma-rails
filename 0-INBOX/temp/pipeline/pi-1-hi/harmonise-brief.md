# Brief: consistency (harmonise) pass, pi-1 Hindi plain zero-shot

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files. Write only in AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters\ (the 14 part files) and 0-INBOX\temp\pipeline\pi-1-hi\. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git.

## Situation
Nine agents translated the 12 parts in parallel from one term list (pi-1-hi\hi-zeroshot-terms.md), each with a builder script (pi-1-hi\build_*_hi.py) and a notes file (pi-1-hi\notes-*.md). preamble.md, 1-matika.md and the first 122 non-empty lines of 2-01 (= pi-1-hi\ch2-01-sample.md) are user-approved and must stay unchanged (except where a decision below says otherwise; none currently does).
Where the same Pāli occurs in different parts, the Hindi must now be identical. The coordinator's list of known divergences and decisions is in pi-1-hi\harmonise-notes.md; the decisions below override it.

## Method (as the English pi-1 pass)
Model: 0-INBOX\temp\pipeline\pi-1-en\harmonise.py (read it). Write pi-1-hi\harmonise_hi.py that applies fixed old → new strings to the Hindi part files, where a rule only touches a Hindi line whose aligned Pāli line (non-empty line i ↔ non-empty line i) matches the rule's Pāli pattern. Back up the pre-pass files to pi-1-hi\backup-pre-harmonise\ first, log every rule to pi-1-hi\harmonise-log.tsv (rule, part, replacements, lines). Line counts, IDs, heading levels and dashes must not change. Support --dry.
Do NOT rebuild with the builders (that would drop the pass); edit the outputs with the script. You may note in harmonise-notes-hi.md which builder constant would need the same change.

## Step 1: find divergences systematically
Write pi-1-hi\find_divergences_hi.py:
- (a) Whole segments: group segments across all parts by their Pāli text (normalised: strip the ^id, variant brackets, collapse spaces); where the Pāli is identical but the Hindi differs, list them.
- (b) Recurring Pāli phrases: for frequent Pāli terms and formula phrases (factor names, defilement names, synonym-string openings, the sphere lists, ṭhapetvā / avasesā frames, tadekaṭṭhā, sīlabbataparāmāsa, sakkāyadiṭṭhi, the lobha / dosa / moha / diṭṭhi / vicikicchā / uddhacca / thina / middha / kukkucca / māna strings, kāmacchanda, viññatti, upacaya, santati, paṭipadā / abhiññā, adhipati, bhūmi, āruppa, sasaṅkhāra, bahūsu siglum), collect the Hindi each part uses for it (use the notes files and the builders' tables, then confirm in the outputs).
Write the result to pi-1-hi\divergences.md. 4-01 and 4-02/4-03 were done by different agents and both composed long strings (lobha/kāma, sīlabbata, sakkāyadiṭṭhi bodies, mind-type lists); expect many divergences there.

## Step 2: decisions
Fixed by the coordinator:
1. ^1-1-2-12-0 Appamāṇāni = «अपरिमित रूपों पर विजय के आधार» (not «असीम भाव»).
2. sammappadhāna (2-03, 2-05, and wherever else) = «सही परिश्रम», so it differs from sammāvāyāma = सही प्रयास. Check परिश्रम is not used for another Pāli word first; report if it is.
3. viññatti = «प्रकट अभिव्यक्ति»; kāyaviññatti / vacīviññatti = «शरीर द्वारा प्रकट अभिव्यक्ति» / «वाणी द्वारा प्रकट अभिव्यक्ति» (3-01/3-02/3-03 and Hindi pi-5). Align ch5 (शारीरिक/वाचिक संकेत) and 4-02 (^1-1201, «… द्वारा अभिव्यक्ति»).
4. khippābhiññā = शीघ्र (not तीव्र). For the paṭipadā qualifiers and the adhipati qualifiers of a jhāna, the same Pāli must get the same Hindi in 2-01/2-02 and 2-03/2-05: pick ONE clause shape (look at both in context; prefer the one that reads better in the longest lines) and apply it everywhere. Log your choice.
5. bhūmi (catūsu / tīsu bhūmīsu in running text) = «स्तर» (4-02 already; ch5 K4/V4 «लोकों» → «स्तरों»). The approved heading Tebhūmaka = «तीनों लोकों से संबंधित» stays.
6. Siglum bahūsu = «(कई संस्करणों में)» (pi-3), everywhere.
7. sārāga next to rāga: one rendering for both 4-01 and 4-02 (choose between गहरा राग / प्रबल राग; the terms file's sārāga = राग stays where rāga is not beside it).
8. For every other divergence of identical Pāli between 4-01 and 4-02/4-03: prefer the 4-01 form, unless 4-02/4-03's form matches an approved earlier Hindi book (pi-3/4/5 termbases in AI_translation\hindi\) or the matrix/terms file and 4-01's does not. Same rule between other parts: the terms file and the approved sample win, then an earlier Hindi book, then the part with more occurrences.
9. Do not change: the approved sample and matrix; renderings that differ because the Pāli differs; source slips translated as written.

## Step 3: apply and verify
Run harmonise_hi.py. Then run find_divergences_hi.py again: segment-level divergences (a) must be 0 except where the Pāli differs only inside variant brackets or the text was rightly kept as written (list those). For every part:
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters` (all OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <pali> <hindi>` (0 mismatches, 0 extra)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py <pali> <hindi>` (OK)
- 1-matika.md, preamble.md and the first lines of 2-01 unchanged vs backup.
Also grep the whole set for: «—», «:-», «धर्म», «seed», Latin letters outside [..] brackets, «असीम भाव», «संकेत», «तीव्र उच्च».

## Final report (short)
Rules applied (count per rule and part), choices you made under 4/7/8 with reasons, divergences left on purpose, check results, and anything that needs the user's eye.
