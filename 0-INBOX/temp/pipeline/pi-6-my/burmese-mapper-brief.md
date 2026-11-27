# Brief: Pāli→Burmese keyword mapping (pi-6, Yamaka «အတွဲလိုက် မေးဖြေခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`; helper scripts in files. Write ONLY inside `0-INBOX/temp/pipeline/pi-6-my/mapper-my/`. Never use the system temp directory. Don't commit. Never use the words for a planted starting value or its negative. Source rule: never open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`); no web searches. Read `pi-1-my/` … `pi-5-my/` only; never edit them. Never use /private/tmp or /tmp (no `cd /tmp`).

## Read first
- `AI_translation/skills/keyword-equivalence-mapper.md` (the skill you execute).
- `0-INBOX/temp/pipeline/burmese-style.md`; `pi-6-my/my6-zeroshot-terms.md`, `pi-6-my/notes-*.md`, `pi-6-my/harmonise-notes.md`, `pi-6-my/harmonise-table.tsv`, the shared values in `pi-6-my/my6_formulas.py` (the forms the pi-5 text uses; the text is FINAL, map against the CURRENT chapter files).
- **The user-approved pi-1 Burmese mapping rules (binding):** `0-INBOX/temp/pipeline/pi-1-my/burmese-mapper-brief.md` (incl. «Approved sample»), `pi-1-my/mapper-my/map-table.md` (rules 1–11, approved) and the agreed later rules in `pi-1-my/mapper-my/map-table-*.md` and `map-harmonise-notes.md` (absolutives keep «…၍»; «samaye X» = «အချိန်၌ ရှိသော X»; relative pronouns Yo / Yā / Yaṃ = (no direct equivalent) where the Burmese builds the clause with «ရှိသော»/«ရှိသမျှ»; one sense per segment; no « / » alternatives; caya = (no direct equivalent) where the text renders apacaya with one word).
- **pi-1 … pi-5 values are binding for the same keyword in the same kind of segment:** `AI_translation/burmese/pi-{1,2,3,4,5}-keywords-by-reference-pali-burmese-plain.md` (pi-3's approved rules in `pi-3-my/burmese-mapper-brief.md` «Approved sample» M1–M9 and `pi-3-my/mapper-my/map-harmonise-notes.md`; pi-2 first where pi-1 and pi-2 differ, incl. pi-2's approved rules in `pi-2-my/burmese-mapper-brief.md` «Approved sample», `pi-2-my/mapper-my/map-table.md` N1–N11 and `map-harmonise-notes.md`; pi-4's rules in `pi-4-my/mapper-my/map-table.md` and `map-harmonise-notes.md`; pi-5's rules Q1–Q8, S1–S6, G1–G5 in `pi-5-my/mapper-my/map-table.md`, `notes-ch2-15.md`, `notes-ch16-31.md`, `map-harmonise-notes.md`), provided the value occurs in the pi-6 segment (the pi-6 text reuses their Burmese for identical Pāli).
- Method model: the pi-5 run: `pi-5-my/mapper-my/map5_rules.py` (shared side-effect-free module: Mapper, compose rules, presence check), `map_ch1.py`, `frame_coverage.py`; and `pi-3-my/mapper-my/presence_check.py` (tables, compose rules, context functions, presence verifier). Copy the approach into your own script; do not import it if importing runs it.

## Per chapter <ch>
- Keywords `mapper-my/<ch>.keywords.md`; Burmese `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/<ch>.md` (FINAL, harmonised; merged copy `AI_translation/burmese/pi-6-burmese-plain-zeroshot.md`); Pāli `AI_translation/pali/pi-6_split_chapters/<ch>.md`.
- Output `mapper-my/<ch>.mapped.md`: same lines and order, same keywords in the same order, each `pali=ဗမာ`.

## Verify each chapter (all must pass)
1. Keyword preservation, which must print `bad []`:
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-6-my/mapper-my');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
2. Presence: every chunk of every value occurs in that segment's Burmese (allowing only the particles / endings the approved rules strip); list and justify every exception.
3. No ", " and no «၊» inside any value; no « / » alternatives.

## This run: PHASE 1 of 3 — preamble, 1-mulayamaka and 2-01-khandhayamaka only
pi-6 is large (44 files, 3023 lines, 500 KB of keywords) and very formulaic, so mapping runs in three phases (standing go-ahead from the user, 2026-11-19 / 2026-11-21: no approval stop; the coordinator reviews each phase):
- **Phase 1 (you):** the sample chapters. They hold the whole question / answer machinery (padasodhana, cakka, suddha, pavatti uppāda / nirodha in every tense and polarity, person / place / moment leads, answers, pariññā), so they fix the mapping of every recurring frame keyword for the whole book.
- Phase 2 (later, three agents in parallel): 2-02 … 5-03; 6-01 … 8 (with 7-01 … 7-11); 9-01 … 10-13, importing your shared module.
- Phase 3 (later): book-wide consistency scan and assembly.

### Your tasks
1. Write a **shared module** `mapper-my/map6_rules.py` that later agents import WITHOUT side effects (no work at import time): the frame / stock-keyword tables, tense and polarity handling of the verbs, the compose rules, the context functions and the presence verifier, settled on the sample chapters. Start from pi-5's `map5_rules.py` (copy, do not import it; its Q1–Q8 / S / G rules hold where they apply). Keep it general: a keyword whose value depends on the frame gets a context function, not a sample-only line rule.
2. Write `mapper-my/map_sample.py` (uses the module; maps preamble, 1-mulayamaka, 2-01-khandhayamaka; runs the verifier) and produce their `.mapped.md` files.
3. Write `mapper-my/map-table.md`: rules used (pi-1 … pi-5 rules by name), any NEW rule explained, the frame keyword → Burmese table, the count of values taken unchanged from pi-1 … pi-5.
4. **Recurring frames check (for phase 2):** script a list of the 200 most frequent keywords of the WHOLE book (all `*.keywords.md`) with the value your module gives each, and check presence of those values over the whole book's Burmese (all 44 chapter files); write `mapper-my/frame-coverage.md` (keyword, uses, value, presence rate, chapters where it fails and why). Fix the module where a failure is a module error; leave genuine context differences to a context function or note them.
5. Keyword ambiguities and text inconsistencies you meet: `mapper-my/map-harmonise-notes.md` (do not change the translation).
6. Do NOT map other chapters and do NOT assemble.

## Final report (short)
Per file: line count, verifier results, (no direct equivalent) count; new rules beyond pi-1 … pi-5's; values that differ from pi-1 … pi-5 for the same keyword, with the reason; frame-coverage summary (how many of the 200 reach 100% presence); text inconsistencies for the rails step; genuinely unclear mappings.
