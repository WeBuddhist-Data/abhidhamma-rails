# Brief: Pāli→Burmese keyword mapping (pi-4, Puggalapaññatti «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`; helper scripts in files. Write ONLY inside `0-INBOX/temp/pipeline/pi-4-my/mapper-my/`. Never use the system temp directory. Don't commit. Never use the words for a planted starting value or its negative. Source rule: never open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`); no web searches. Read `pi-1-my/`, `pi-2-my/` and `pi-3-my/` only; never edit them. Never use /private/tmp.

## Read first
- `AI_translation/skills/keyword-equivalence-mapper.md` (the skill you execute).
- `0-INBOX/temp/pipeline/burmese-style.md`; `pi-4-my/my4-zeroshot-terms.md`, `pi-4-my/harmonise-notes.md`, `harmonise-table.tsv` (the forms the pi-4 text uses; the text is FINAL, map against the CURRENT chapter files).
- **The user-approved pi-1 Burmese mapping rules (binding):** `0-INBOX/temp/pipeline/pi-1-my/burmese-mapper-brief.md` (incl. «Approved sample»), `pi-1-my/mapper-my/map-table.md` (rules 1–11, approved) and the agreed later rules in `pi-1-my/mapper-my/map-table-*.md` and `map-harmonise-notes.md` (absolutives keep «…၍»; «samaye X» = «အချိန်၌ ရှိသော X»; relative pronouns Yo / Yā / Yaṃ = (no direct equivalent) where the Burmese builds the clause with «ရှိသော»/«ရှိသမျှ»; one sense per segment; no « / » alternatives; caya = (no direct equivalent) where the text renders apacaya with one word).
- **pi-1, pi-2 and pi-3 values are binding for the same keyword in the same kind of segment:** `AI_translation/burmese/pi-{1,2,3}-keywords-by-reference-pali-burmese-plain.md` (pi-3's approved rules in `pi-3-my/burmese-mapper-brief.md` «Approved sample» M1–M9 and `pi-3-my/mapper-my/map-harmonise-notes.md`; pi-2 first where pi-1 and pi-2 differ, incl. pi-2's approved rules in `pi-2-my/burmese-mapper-brief.md` «Approved sample», `pi-2-my/mapper-my/map-table.md` N1–N11 and `map-harmonise-notes.md`), provided the value occurs in the pi-4 segment (the pi-4 text reuses their Burmese for identical Pāli).
- Method model: `pi-3-my/mapper-my/map_all.py` with the shared `pi-3-my/mapper-my/presence_check.py` and `harmonise_rules.py` (tables, compose rules, context functions, presence verifier). Copy the approach into your own script; do not import it if importing runs it.

## Per chapter <ch>
- Keywords `mapper-my/<ch>.keywords.md`; Burmese `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/<ch>.md`; Pāli `AI_translation/pali/pi-4_split_chapters/<ch>.md`.
- Output `mapper-my/<ch>.mapped.md`: same lines and order, same keywords in the same order, each `pali=ဗမာ`.

## Verify each chapter (all must pass)
1. Keyword preservation, which must print `bad []`:
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-4-my/mapper-my');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
2. Presence: every chunk of every value occurs in that segment's Burmese (allowing only the particles / endings the approved rules strip); list and justify every exception.
3. No ", " and no «၊» inside any value; no « / » alternatives.

## This run: the WHOLE book (12 files, 250 lines), one script
The book is small, so one agent maps all chapters (standing go-ahead from the user, 2026-11-19: no approval stop; the coordinator reviews the result).
1. Write `mapper-my/map_all.py` (pi-4; one table section per chapter; runs the verifier) and `mapper-my/map-table.md` (rules used, any NEW rule explained, the keyword → Burmese table, count of values taken unchanged from pi-1 / pi-2 / pi-3). Do preamble, 1-matika and 2-ekaka first and check them; then the rest.
2. Person-type names: the keyword for a person type maps to the approved name from `pi-4-my/my4-zeroshot-terms.md` (the same value in mātikā, heading and definition).
3. Consistency scan over all `*.mapped.md`: keywords with more than one value are aligned (state the rule) or kept as a genuine sense / grammar difference (state why) in `mapper-my/map-harmonise-notes.md`; list text inconsistencies you meet for the rails step (do not change the translation).
4. Assemble: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/mapper_chunks.py assemble AI_translation/pali/pi-4-keywords-by-reference-pali-plain.md 0-INBOX/temp/pipeline/pi-4-my/mapper-my AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md`: every ID once, unchanged keyword counts.

## Final report (short)
Per chapter: line count, verifier results, (no direct equivalent) count; new rules beyond pi-1's / pi-2's / pi-3's; values that differ from pi-1 / pi-2 / pi-3 for the same keyword, with the reason; the consistency scan before / after; text inconsistencies for the rails step; genuinely unclear mappings.
