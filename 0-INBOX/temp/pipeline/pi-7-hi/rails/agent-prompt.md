# Common prompt for the pi-7 rails agents (the per-agent prompt names the files)

Translate pi-7 (Paṭṭhāna) Pāli → Hindi (plain audience), rails method.

Read and follow D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\hi-rails-brief.md in full (it names everything else to read). The user APPROVED the sample on 2026-11-13, so it is now binding: AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\1-00-paccaya.md, 0-INBOX\temp\pipeline\pi-7-hi\rails\sample-1\1-01-a-sample.md and 1-01-b-sample.md, rails\hi-rails-formulas.md (copy every string verbatim, including the "(not yet in the sample)" lines) and rails\build_rails_sample.py (import read-only: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails"); import build_rails_sample as S`; never edit or run it as a script). Also read rails\notes-sample.md.

Other agents translate other pi-7 files in parallel. Keep identical Pāli → identical Hindi by using the formulas file and the sample builder's constants; put any NEW recurring formula in rails\notes-<your files>.md so the later alignment pass can reconcile. Translate source slips exactly as written (only pure spelling slips as the word meant) and list them.

Write ONLY your output files (AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\<f>.md) and your own helper scripts/notes in 0-INBOX\temp\pipeline\pi-7-hi\rails\ named after your files (write scripts with the Write tool, never via a shell redirect). Never create files at the repo root or in any system temp/scratchpad folder; never run git; never write "seed"/"unseeded"; no em/en dash except where the Pāli has one at that spot. You cannot write report files: return your report as text.

Run every check in the brief on each file (check_chapter_ids, dashcheck, verify_hi with only the expected {…} bracket and Siyā "?" flags, no double blank lines, no CR, no Latin outside variant brackets, termbase adherence) and fix genuine problems; then read your Hindi as a plain reader would and fix anything unnatural while keeping every termbase term. Final report under 350 words, as in the brief.
