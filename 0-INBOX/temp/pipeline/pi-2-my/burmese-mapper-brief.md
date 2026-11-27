# Brief: Pāli→Burmese keyword mapping (pi-2, Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`; helper scripts in files. Write ONLY inside `0-INBOX/temp/pipeline/pi-2-my/mapper-my/`. Never use the system temp directory. Don't commit. Never use the words for a planted starting value or its negative. Source rule: never open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`); no web searches. Read `pi-1-my/` only; never edit it.

## Read first
- `AI_translation/skills/keyword-equivalence-mapper.md` (the skill you execute).
- `0-INBOX/temp/pipeline/burmese-style.md`; `pi-2-my/my2-zeroshot-terms.md`, `pi-2-my/harmonise-notes.md`, `harmonise-table.tsv` (the forms the pi-2 text uses; the text is FINAL, map against the CURRENT chapter files).
- **The user-approved pi-1 Burmese mapping rules (binding):** `0-INBOX/temp/pipeline/pi-1-my/burmese-mapper-brief.md` (incl. «Approved sample»), `pi-1-my/mapper-my/map-table.md` (rules 1–11, approved) and the agreed later rules in `pi-1-my/mapper-my/map-table-*.md` and `map-harmonise-notes.md` (absolutives keep «…၍»; «samaye X» = «အချိန်၌ ရှိသော X»; relative pronouns Yo / Yā / Yaṃ = (no direct equivalent) where the Burmese builds the clause with «ရှိသော»/«ရှိသမျှ»; one sense per segment; no « / » alternatives; caya = (no direct equivalent) where the text renders apacaya with one word).
- **pi-1 values are binding for the same keyword in the same kind of segment:** `AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md`, provided the value occurs in the pi-2 segment (the pi-2 text reuses pi-1's Burmese for identical Pāli).
- Method model: `pi-1-my/mapper-my/map_all.py` (tables, compose rules, context functions, presence verifier). Copy the approach into your own script; do not import it if importing runs it.

## Per chapter <ch>
- Keywords `mapper-my/<ch>.keywords.md`; Burmese `AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/<ch>.md`; Pāli `AI_translation/pali/pi-2_split_chapters/<ch>.md`.
- Output `mapper-my/<ch>.mapped.md`: same lines and order, same keywords in the same order, each `pali=ဗမာ`.

## Verify each chapter (all must pass)
1. Keyword preservation, which must print `bad []`:
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-2-my/mapper-my');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
2. Presence: every chunk of every value occurs in that segment's Burmese (allowing only the particles / endings the approved rules strip); list and justify every exception.
3. No ", " and no «၊» inside any value; no « / » alternatives.

## This run: SAMPLE only
preamble and 1-khandhavibhango. Write `mapper-my/map_all.py` (pi-2; one table section per chapter; it writes only the chapters it covers; runs the verifier) and `mapper-my/map-table.md` (rules used, any NEW rule explained, the keyword → Burmese table, and the count of values taken unchanged from pi-1). Stop after the sample.

## Approved sample (user, 2026-11-18): binding for all later chapters
- `mapper-my/map-table.md` (pi-1 rules + N1–N11) and the values in `preamble.mapped.md` / `1-khandhavibhango.mapped.md` are approved, incl. the six deliberate differences from pi-1 (ajjhattaṃ, bahiddhā, uppanno, hīno, paccayā, vuccati rūpaṃ).
- Parallel agents: do NOT edit `map_all.py`, `map-table.md` or the sample outputs. Write your own `mapper-my/map_<your chapters>.py` (copy the sample's tables, compose rules, context functions and verifier) and `mapper-my/map-table-<your chapters>.md` with any NEW rule or value (each explained).

## Final report (short)
Per chapter: line count, verifier results, (no direct equivalent) count; new rules beyond pi-1's (for the user's review); values that differ from pi-1 for the same keyword, with the reason; genuinely unclear mappings.
