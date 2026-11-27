# Brief: pi-5 Burmese keyword mapping, PHASE 2 (chapter group <GROUP>)

Read first, and follow as binding, the phase-1 brief `0-INBOX/temp/pipeline/pi-5-my/burmese-mapper-brief.md` (all rules, sources, per-chapter output and the three verify checks), then the phase-1 results in `pi-5-my/mapper-my/`: `map-table.md` (rules Q1–Q8), `frame-coverage.md`, `map-harmonise-notes.md`, `map5_rules.py`, `map_ch1.py`.

## Coordinator decisions on phase 1 (2026-11-20, under the user's standing go-ahead)
Phase 1 is approved as built: Q1–Q8 hold book-wide. The unclear points are settled as the text renders them: appiyaṃ «ဦးစားမပေး» + karitvā (no direct equivalent); Āmantā «ဟုတ်ပါသည်» whole; -ī adjectives / -vādī epithets «…သော» (Q8), agent nouns «…သူ»; bhikkhave «ရဟန်း» (as pi-1 … pi-4); anamataggo keeps the text's negative. The 9 text inconsistencies stay for the rails step.

## This run
- Map only the chapters of your group, in chapter order: <CHAPTERS>.
- Write ONE script `mapper-my/map_<GROUPID>.py` that imports `map5_rules` (`R.Mapper(chapter_tables=…, ctx=…, funcs=…)`) and holds only chapter tables and new context functions for your group. **Do NOT edit `map5_rules.py`** (another agent maps the other group at the same time). If a module value is wrong for your chapters, override it in your script's tables / context functions and list it under «Module overrides» in your notes; the coordinator moves agreed overrides into the module in phase 3.
- Write only your group's `<ch>.mapped.md` files and `mapper-my/notes-<GROUPID>.md` (rules used, new rules with reasons, module overrides, values that differ from pi-1 … pi-4 or from ch1 for the same keyword with the reason, text inconsistencies for the rails step, unclear mappings). Do not touch the other group's files, `map-table.md` or `map-harmonise-notes.md`. Do not assemble.
- Verify every chapter with the three checks of the phase-1 brief (preservation `bad []`, presence 0 unexplained failures, no «, » / «၊» / « / » in values); the script prints them per chapter.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails; write only inside `0-INBOX/temp/pipeline/pi-5-my/mapper-my/` (helper scripts in `mapper-my/work/`). Never /tmp or /private/tmp, never `cd /tmp`, never commit, never open `0-INBOX/temp/language-priority/` or any existing Burmese translation / nissaya / web source, never edit pi-1-my … pi-4-my, never use the words for a planted starting value or its negative. Do not stop for approval.

## Final report (short, numbers first)
Per chapter: lines, `bad`, presence failures, (no direct equivalent) count. Then: new rules, module overrides, differing values with reasons, text inconsistencies, unclear mappings.
