# Brief: alignment pass, pi-7 Hindi plain RAILS translation

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -B -X utf8`. Write only in AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\ (75 files) and 0-INBOX\temp\pipeline\pi-7-hi\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git, never write "seed". You cannot write report files for me: return your report as text.

## Situation
Fourteen agents translated the 74 files of the Paṭṭhāna in parallel from one approved sample (rails\sample-1\, built by build_rails_sample.py; preamble.md and 1-00-paccaya.md) with the user-approved termbase AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md and formulas file rails\hi-rails-formulas.md. Each wrote a builder (rails\build_rails_*.py) and notes (rails\notes-*.md). preamble.md, 1-00-paccaya.md and the sample lines (1-01-kusalattika.md non-empty lines 1–190 and 1235–1262) are user-approved and must stay unchanged. Where the same Pāli occurs in different files, the Hindi must now be identical, and where the same Pāli word, note or frame was rendered differently by different agents, one form must win.

My summary of every agent's report is rails\run-reports.md: lines marked ALIGN, CHECK and REVIEW list the divergences already spotted. Read it and all rails\notes-*.md.

## Method (as the pi-7 zero-shot harmonise pass)
Model: 0-INBOX\temp\pipeline\pi-7-hi\harmonise_hi.py and find_divergences_hi.py (read them; adapt to the rails folder). Write rails\align_rails_pi7.py that applies fixed old → new strings to the Hindi files, where a rule only touches a Hindi line whose aligned Pāli line (non-empty line i ↔ non-empty line i) matches the rule's Pāli pattern. Back up to rails\backup-pre-align\ first (only if it does not exist; always start from it so the script can be rerun), log every rule to rails\align-log.tsv (rule, file, replacements, lines). Line counts, IDs, heading levels and dashes must not change. Support --dry. Do NOT rebuild with the builders.

## Step 1: find divergences
Write rails\find_divergences_rails.py: (a) whole lines grouped by normalised Pāli (strip ^id, {…} variants, count markers "(3)", collapse spaces) where the Hindi differs; (b) recurring words and notes: the editorial notes in brackets (Mūlaṃ kātabbaṃ / pucchitabbaṃ, sadisaṃ, saṃkhittaṃ, vitthāretabbaṃ, gaṇetabbaṃ, (Avipākaṃ / Savipākaṃ – n), cakkaṃ …), kātabba-, the pañhāvāra lists (crimes, upanissaya actions, the analytical knowledges, saka/parapariggahe, chandarāga, pisuṇaṃ bhaṇati), headings, triad/dyad names, the na-/no-/nana- items, anidassanasappaṭigha. Output rails\divergences.md.

## Step 2: decisions
Order of authority: (1) the termbase (approved; a term is used in its exact wording, inflected as needed); (2) the approved sample, 1-00-paccaya.md and hi-rails-formulas.md; (3) 1-01-kusalattika.md; (4) pi-1 Hindi (1-matika.md, pi-1 termbase) for matrix items, pi-2/pi-6 Hindi for other shared terms; (5) the form with more occurrences. Specifically:
1. **kātabba-** (all forms): the termbase term «करना चाहिए», inflected for agreement («करने चाहिए» with a plural subject); not «तैयार करना / शामिल करना / बनाना चाहिए».
2. **Editorial notes:** one wording each for the same Pāli note across the book (e.g. Mūlaṃ kātabbaṃ, Mūlaṃ pucchitabbaṃ, (Avipākaṃ – n), (evaṃ gaṇetabbaṃ), «…vārampi paṭiccavārasadisaṃ» with one verb number).
3. **Words without a termbase entry** that agents rendered differently (saka/parapariggahe, dhammapaṭisambhidā vs the termbase's dhammappaṭisambhidāya «परिघटनाओं का विश्लेषणात्मक ज्ञान», niruttipaṭisambhidā, pisuṇaṃ bhaṇati «चुगली की बात / बातें», sukhindriya / dukkhindriya, sahajātā as an adjective …): one form each, by the order above; where a sibling termbase entry exists, follow it.
4. **anidassanasappaṭigha** and other items where some agents kept pi-1's internal comma and the termbase writes one term: follow the termbase wording; keep a comma only where the Hindi sentence needs it.
5. **Subject agreement where the Pāli drops the subject** (REVIEW lines): leave as is unless a line is plainly ungrammatical; list the cases.
6. **^7-8-37 (2-02):** the Pāli leaves out "khandhānaṃ"; an agent added «समूहों». The user rule is to translate as written: remove the added noun and render the adjective phrase alone as a substantive («…वालों के लिए»).
7. Source slips translated as written stay as written; renderings that differ because the Pāli differs stay; agreement differences decided by the subject are not divergences.
8. Do not change preamble.md, 1-00-paccaya.md or the sample lines.

## Step 3: apply and verify
Run align_rails_pi7.py, then find_divergences_rails.py again: identical-Pāli divergences must be 0 except where the Pāli differs only inside {…} or the text was rightly kept as written (list those). For every file: check_chapter_ids (OK), verify_hi (OK apart from the expected {…} bracket and Siyā "?" flags), dashcheck (0 mismatches); preamble, 1-00 and the sample lines unchanged vs backup; grep for «—», «:-», «धर्म», «seed», Latin outside [..], CR, double blank lines. Run termbase adherence on the folder before and after and report both lines.

## Final report (short, under 400 words)
Rules applied (count per rule and file group), the forms you chose under 1–6 with reasons, divergences left on purpose, check results, and anything that needs the user's eye.
