# Brief: pi-5 Burmese keyword mapping, PHASE 3 (whole book: consistency and assembly)

Read first, and follow as binding, the phase-1 brief `0-INBOX/temp/pipeline/pi-5-my/burmese-mapper-brief.md` (rules, sources, verify checks) and the phase-2 brief `burmese-mapper-brief-phase2.md` (with the coordinator decisions on phase 1). Then the results in `pi-5-my/mapper-my/`: `map5_rules.py`, `map_ch1.py`, `map_ch2-15.py`, `map_ch16-31.py`, `map-table.md`, `frame-coverage.md`, `map-harmonise-notes.md`, `notes-ch2-15.md` (rules S1–S6, module overrides), `notes-ch16-31.md` (rules G1–G5, module overrides).

## Coordinator decisions on phase 2 (2026-11-21, under the user's standing go-ahead)
- S2–S6 and G1–G5 are approved book-wide. S1 (stem fallback, 726 uses in ch2–15) is approved only after the review below.
- Module overrides that hold beyond one segment go into `map5_rules.py` (now yours to edit); single-segment forms stay as per-segment rules in the chapter scripts. The three mechanics noted in ch2–15 (`neg_value` with a gapped negative, `glue` across a noun phrase, `phrase_ok` vs `presence` for «Xပြီး ဖြစ်») are fixed in the module.
- parinibbāyī «…ပြုသော» (Q8 / pi-4); agent nouns stay «…သူ»; person-type names keep their approved names (P1).

## Tasks
1. **Module consolidation:** move the agreed overrides into `map5_rules.py`, fix the three mechanics, and re-run `map_ch1.py`, `map_ch2-15.py`, `map_ch16-31.py` (in that order). Every value change against the current `.mapped.md` files must be listed with its reason in `mapper-my/phase3-changes.tsv` (segment, keyword, old, new, reason); no unexplained change.
2. **S1 review:** list every stem-fallback value (all chapters), check each against the segment's Burmese and the keyword's sense; correct the wrong ones by rule; record the count kept / corrected in the notes.
3. **Book-wide consistency scan** over all 32 `*.mapped.md` (model `pi-4-my/mapper-my/map_scan.py`): every keyword with more than one value is aligned (state the rule) or kept as a genuine sense / grammar / text difference (state why). Write the result into `mapper-my/map-harmonise-notes.md` (§B scan before / after), and merge the text inconsistencies of `notes-ch2-15.md` and `notes-ch16-31.md` into §A (one numbered list, duplicates joined) for the rails step. Do not change the translation.
4. **Verify all 32 files** with the three checks (preservation `bad []`, presence 0 unexplained, no «, » / «၊» / « / » in values). A second run of the three scripts must give byte-identical files.
5. **Assemble:** `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/mapper_chunks.py assemble AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md 0-INBOX/temp/pipeline/pi-5-my/mapper-my AI_translation/burmese/pi-5-keywords-by-reference-pali-burmese-plain.md`: every ID once, unchanged keyword counts.

## Rules
Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails; write only inside `0-INBOX/temp/pipeline/pi-5-my/mapper-my/` (helpers in `mapper-my/work/`) and the one assembled output file above. Never /tmp or /private/tmp, never `cd /tmp`, never commit, never open `0-INBOX/temp/language-priority/` or any existing Burmese translation / nissaya / web source, never edit pi-1-my … pi-4-my or the pi-5 zero-shot text, never use the words for a planted starting value or its negative. Do not stop for approval.

## Final report (short, numbers first)
Values changed by task 1 and 2 (counts by reason); S1 kept / corrected; scan before / after with kept differences; verify results for all 32 files and the byte-identical re-run; assembly result (IDs, keyword counts); the merged text-inconsistency list (count); unclear mappings left.
