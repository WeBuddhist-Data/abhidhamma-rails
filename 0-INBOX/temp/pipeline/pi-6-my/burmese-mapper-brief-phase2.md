# Brief: pi-6 Burmese keyword mapping, PHASE 2 (chapter group <GROUP>)

Read first, and follow as binding, the phase-1 brief `0-INBOX/temp/pipeline/pi-6-my/burmese-mapper-brief.md` (all rules, sources, per-chapter output and the three verify checks), then the phase-1 results in `pi-6-my/mapper-my/`: `map-table.md` (rules R1–R9 and the pi-1 … pi-5 rules they build on), `frame-coverage.md` (incl. the whole-book dry run: the 218 keywords the module does not map yet, and the 88 stem-fallback keywords to check by eye), `map-harmonise-notes.md`, `map6_rules.py`, `map_sample.py`.

## Coordinator decisions on phase 1 (2026-11-22, under the user's standing go-ahead)
Phase 1 is approved as built: R1–R9 hold book-wide. The unclear points are settled as the text renders them: the two root-predicate shapes of R4 (attributive where the text has «ရှိ» / «based on», noun where it has a copula); abyākata as a root base stays adjectival; a keyword with two forms in the text takes the segment's own form; Āmantā «ဟုတ်ပါသည်» and No «မဟုတ်ပါ» whole, Natthi as mapped; Samuṭṭhānāhārārammaṇā joined. nāma = «စိတ်ပိုင်း» (mentality), arūpa as plane «ရုပ်မရှိသော ဘုံ», the hetuvāra synonyms as mapped. The text inconsistencies A1–A6 stay for the rails step.

## This run
- Map only the chapters of your group, in chapter order: <CHAPTERS>.
- Write ONE script `mapper-my/map_<GROUPID>.py` that imports `map6_rules` and holds only chapter tables and new context functions for your group. **Do NOT edit `map6_rules.py`** (two other agents map the other groups at the same time). If a module value is wrong for your chapters, override it in your script's tables / context functions and list it under «Module overrides» in your notes; the coordinator moves agreed overrides into the module in phase 3.
- Check every stem-fallback value your chapters get (S1) by eye against the segment and the keyword's sense; override the wrong ones; record kept / corrected counts.
- Write only your group's `<ch>.mapped.md` files and `mapper-my/notes-<GROUPID>.md` (rules used, new rules with reasons, module overrides, values that differ from pi-1 … pi-5 or from the sample for the same keyword with the reason, S1 review counts, text inconsistencies for the rails step, unclear mappings). Do not touch the other groups' files, `map-table.md` or `map-harmonise-notes.md`. Do not assemble.
- Verify every chapter with the three checks of the phase-1 brief (preservation `bad []`, presence 0 unexplained failures, no «, » / «၊» / « / » in values); the script prints them per chapter.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails; write only inside `0-INBOX/temp/pipeline/pi-6-my/mapper-my/` (helper scripts in `mapper-my/work/`, named with your GROUPID). Never /tmp or /private/tmp, never `cd /tmp`, never commit, never open `0-INBOX/temp/language-priority/` or any existing Burmese translation / nissaya / web source, never edit pi-1-my … pi-5-my, never use the words for a planted starting value or its negative. Do not stop for approval.

## Final report (short, numbers first)
Per chapter: lines, `bad`, presence failures, (no direct equivalent) count. Then: S1 kept / corrected, new rules, module overrides, differing values with reasons, text inconsistencies, unclear mappings.
