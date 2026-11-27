# Brief: pi-7 Burmese keyword mapping, PHASE 2 (chapter group <GROUP>)

## Read first
Read these and follow them as binding:
- The phase-1 brief `0-INBOX/temp/pipeline/pi-7-my/burmese-mapper-brief.md`: all rules, sources, per-chapter output and the three verify checks.
- The phase-1 results in `pi-7-my/mapper-my/`:
  - `map-table.md`: rules T1–T13, M1, M2, and the pi-1 … pi-6 rules they build on.
  - `frame-coverage.md`: the whole-book dry run, with the 238 keywords the module does not map yet and the 297 stem-fallback uses.
  - `map-harmonise-notes.md`.
  - `map7_rules.py`: md5 909bed2528b27eb55051c73f3ce28f81.
  - `map_sample.py`.

## Coordinator decisions on phase 1 (2026-11-26, under the user's standing go-ahead)
- Phase 1 is approved as built, and T1–T13, M1 and M2 hold book-wide.
- The unclear points are settled as phase 1 mapped them:
  - **U1:** assādeti is the bare «သာယာ», by the ending rule.
  - **U2:** an act compound takes the whole verb phrase, and its karoti / katvā get (no direct equivalent). This follows pi-1's one-word-two-members decision.
  - **U3:** a pi-1 … pi-6 value is kept wherever it is present in the segment as a phrase; otherwise the pi-7 text's word is used (as for paccavekkhati).
  - **U4:** uppajjeyya(ṃ) keeps «နိုင်».
  - **U5:** Xpaccayā keeps «ကြောင့်» (pi-2), and Xpaccayena drops «ဖြင့်» (pi-5).
- The text inconsistencies (§A, 12 items) stay for the rails step.

## This run
- Map only the chapters of your group, in chapter order: <CHAPTERS>.
- Write ONE script, `mapper-my/map_<GROUPID>.py`. It imports `map7_rules` and holds only chapter tables and new context functions for your group.
- **Do NOT edit `map7_rules.py`.** Other agents map the other groups at the same time.
  - If a module value is wrong for your chapters, override it in your script's tables or context functions.
  - List each override under «Module overrides» in your notes. The coordinator moves agreed overrides into the module in phase 3.
- **Stem fallback (S1):** check every stem-fallback value your chapters get by eye, against the segment and the keyword's sense. Override the wrong ones, and record the kept / corrected counts.
- **Unmapped keywords:** map every keyword your chapters have that the module leaves unmapped. Use the text's phrase, in dictionary form, following the rules.
- **What you write:** only your group's `<ch>.mapped.md` files and `mapper-my/notes-<GROUPID>.md`. The notes cover:
  - rules used;
  - new rules, with reasons;
  - module overrides;
  - values that differ from pi-1 … pi-6 or from the sample for the same keyword, with the reason;
  - S1 review counts;
  - text inconsistencies for the rails step;
  - unclear mappings.
- **Leave alone:** the other groups' files, `map-table.md` and `map-harmonise-notes.md`. Do not assemble.
- **Verify every chapter** with the three checks of the phase-1 brief: preservation `bad []`, 0 unexplained presence failures, and no «, » / «၊» / « / » in values. The script prints them per chapter.
- **Reproducibility:** a second run must give byte-identical files.

## Working rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails.
- Write only inside `0-INBOX/temp/pipeline/pi-7-my/mapper-my/`. Put helper scripts in `mapper-my/work/`, with your GROUPID in their names.
- Never use /tmp or /private/tmp, and never `cd /tmp`.
- Never commit.
- Never open `0-INBOX/temp/language-priority/` or any existing Burmese translation, nissaya or web source.
- Never edit pi-1-my … pi-6-my or the pi-7 zero-shot text.
- Never use the words for a planted starting value or its negative.
- Do not stop for approval.
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`, called by its full path, never through a quoted shell variable.
- Run long scripts in the background.

## Final report (short, numbers first)
- Per chapter: lines, `bad`, presence failures, and the (no direct equivalent) count.
- Then:
  - S1 kept / corrected;
  - keywords newly mapped;
  - new rules;
  - module overrides;
  - differing values, with reasons;
  - text inconsistencies;
  - unclear mappings.
