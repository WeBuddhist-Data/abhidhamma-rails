# Brief: apply the approved review fixes to the Russian pi-6 rails

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B`. LF line endings. Write ONLY: the rails chapter files in AI_translation\russian\pi-6-russian-plain-rails_split_chapters\ (through your script), and your script, log and backup in 0-INBOX\temp\pipeline\pi-6-ru\review\. Never create files at the repo root (not even an empty one) or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, the termbase, the maps or any pi-1 … pi-5 file; do not run git; never write "seed" or "unseeded". Grep only the files named here. No Vietnamese files. Return your report as text.

## The user's decisions (2026-11-28, binding)
- **Apply all of section A** of 0-INBOX\temp\pipeline\pi-6-ru\review\review-summary.md (read it and the per-reviewer files findings-r1.md … findings-r8.md in the same folder for the IDs, lines and wording).
- **Keep «там»** after a place just named, everywhere (do not drop any, including the 6-02 line 225 one listed in A6: leave it).
- **Source slips stay as written** (the four uppajjati / upapajjati swaps, ^6-10-452 bhavissanti, ^6-9-192); number agreement keeps Russian agreement. No change.
- **9-01: keep the plural** «То, что не является благими, не является благими явлениями?». No change.
- sarūpaka and bare rūpaṃ «форма» stay as they are.

## How
1. Copy every rails file you will change into review\backup-pre-fixes\ first.
2. Write review\apply_review_fixes_ru.py: explicit, counted rules (old → new, with the file, and the expected count; or a Pāli-anchored rule where the Russian string also occurs elsewhere unchanged). It must be idempotent (a rule whose new text is already in place is skipped) and log every change to review\fixes-log.tsv (file, line, old, new). Read each target segment against the Pāli before writing its rule.
3. Notes on the rows:
   - A1 (ch. 8 past-time questions): keep every word; move only the clause boundary so the second half is the question («У кого ум миновал момент возникновения, этот момент, и время его прошло, у того ум миновал момент прекращения, этот момент, и время его прошло?»); do the same for (б), the negative forms (не миновал …, время не прошло) and the «Какой ум …, тот ум …?» / «У кого какой ум …» forms; check each against its Pāli. The answers stay.
   - A2: «В момент распада ума, а также у вошедших …» only where the Pāli lists the moment and the persons as separate cases (^6-8-66 … 73); check whether the same Pāli shape occurs in other chapters and report it (do not change other chapters without a matching Pāli).
   - A4: plural verb only where the Russian has two or more coordinated subjects; keep the rest of the sentence.
   - A5: insert «у них» only where the Pāli has tesaṃ before the ca … ca pair; where two «и» would then stand side by side awkwardly, prefer the form the sibling sentences already use; report what you did per group.
   - A6: apply the listed items except the 6-02 «там». «остальное тело является телом» only where the Pāli has avaseso kāyo (and the same for avasesā upekkhā etc.); check 3-01 and 10-01 and any chapter with the same Pāli.
4. Identical Pāli must keep identical Russian: after the fixes, run 0-INBOX\temp\pipeline\pi-6-ru\harmonise_scan.py 40 --rails (and with `--sent`) and confirm no new divergence.
5. Then run `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-6-ru\rails\rails_paren_stop_fix.py` (bracket full stops; must report 0 or only the known sigla lines).

## Verify (all must pass, for every changed file)
check_chapter_ids.py, dashcheck.py, pi-1-ru\verify_ru.py (as in ru-rails-brief.md); no «ли», no Latin outside variant brackets, no double blank lines, no CR, no em dash.

## Report (under 400 words, as text)
Rules applied with counts per row (A1 … A6); what you checked against the Pāli; anything you could not apply and why; the scan results.
