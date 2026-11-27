# Brief: Burmese zero-shot SAMPLE for pi-1 (Dhammasaṅgaṇī)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and call Python as `python3 -I -X utf8` (it resolves to miniconda 3.13). Write helper scripts to files rather than inline `-c` with regexes. Scratch, scripts and notes only in `0-INBOX/temp/pipeline/pi-1-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative in any file; say "sample" or "model".

This is the FIRST Burmese text in the vault. You write the model that later agents copy for the rest of the book, so the shared pieces (formula module, term list) matter as much as the text. Save each file as soon as it passes. Keep your notes current. Stop after this sample: the user reviews it before anything else runs.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`: binding rules, the source rule (Pāli only, no existing Burmese translations, no web lookups), typography, the dash rule.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- Method model (formula module + generator): `0-INBOX/temp/pipeline/pi-1-mr/mr_formulas.py`, `make_sample.py`, `check_sample.py` (Marathi pi-1 sample). Copy the method, not the Marathi words.
- Cross-check of MEANING only (translate FROM THE PĀLI, never copy wording): the English zero-shot `AI_translation/english/pi-1-english-plain-zeroshot_split_chapters/1-matika.md`, the Marathi final `AI_translation/marathi/pi-1-marathi-plain-rails_split_chapters/1-matika.md` and the Marathi termbase `AI_translation/marathi/pi-1-pali-marathi-termbase-plain.md` (shows how each triad / dyad term was understood).

## About the text
The Mātikā (matrix) lists the 22 triads (Tikamātikā, items (Ka) (Kha) (Ga)) and 100 Abhidhamma dyads in groups (Hetugocchaka, Cūḷantaraduka, Āsavagocchaka … Piṭṭhiduka), then 42 suttanta dyads (Suttantikadukamātikā). Each item is a noun phrase «X dhammā.» Many dyads are built from a few patterns: «X dhammā / na X dhammā», «sahetukā / ahetukā», «X-sampayuttā / X-vippayuttā», «X ceva Y ca / Y ceva no ca X» and so on. Group closers like «Hetugocchakaṃ.» end each group.

## Your output
1. `AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/preamble.md` (Pāli: `AI_translation/pali/pi-1_split_chapters/preamble.md`).
2. The WHOLE of `1-matika.md` in the same folder (Pāli: `AI_translation/pali/pi-1_split_chapters/1-matika.md`, 564 lines).
3. `0-INBOX/temp/pipeline/pi-1-my/my_formulas.py`: the shared module later agents import: the term table (Pāli stem = Burmese), the dyad / triad patterns (positive, negated, «ceva … ca» / «ceva no ca» forms), item letters, headings, number words, the variant-bracket labels.
4. `pi-1-my/make_sample.py`: your generator; it imports my_formulas.py and writes both files. Generate every segment from the tables and patterns; it stops on any line no rule matches.
5. `pi-1-my/my-zeroshot-terms.md`: every formula and term as «Pāli = Burmese», one per line, grouped (book frame, dhamma / core terms, triads, dyad patterns, group names, headings). This is what the user reviews and approves.
6. `pi-1-my/check_sample.py`: your own per-line check: item letters, negations (every Pāli «a-/an-/na/no/neva» has its Burmese negation), the «[» variant labels, and that each term's Burmese is the table value (0 mismatches).
7. `pi-1-my/notes-sample.md`: your choices with one-line reasons (especially: the word for dhamma = phenomenon; how you keep the triad / dyad names plain), unsure Pāli, source slips.

## Key choices to make and record
- dhamma (phenomenon) in «X dhammā»: pick the Burmese word an ordinary reader understands as "states / phenomena" and that does not read as "the Teaching" in this context. Record the choice and the alternative you rejected.
- kusala / akusala / abyākata: the established ကုသိုလ် / အကုသိုလ်, and a plain rendering of abyākata meaning "neither wholesome nor unwholesome" (not "neutral feeling").
- Dyad and triad names: plain descriptive Burmese, never a bare Pāli compound in Burmese script.
- Book title (Dhammasaṅgaṇī) in Burmese only; «Abhidhammapiṭake» line as in the other languages.

## Rules
- Identical Pāli = identical Burmese. Polarity and numbers exact; checked by script.
- Headings keep their #-level. Block IDs exact, one blank line between segments, the source's number of non-empty lines per segment, no double blank lines.
- «…pe…» / «…Pe…» become one «…».
- DASH RULE: «–» only where the Pāli line has one, same spot, same count. No «।», no «:-», no «?».
- Variant readings: «[ပါဌ်ကွဲ (Syā.): <Pāli>]» for a different word, «[စာလုံးပေါင်းကွဲ (Syā.): <Pāli>]» for spelling only; keep the sigla as written and capitalise the first letter (Syā., Sī., Kaṃ., Pī.).
- Natural plain Burmese; nothing added. No notes of your own inside the translation.

## Verify every file (all must pass)
```
python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-1_split_chapters AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters <ch>.md
python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-1_split_chapters/<ch>.md AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/<ch>.md
python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-1_split_chapters/<ch>.md AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (check_text_pe.py leaves copies in `pi-6-mr/chk-pe/`: delete your chapter copies there afterwards). Plus your own check: 0 mismatches.

## Final report (short)
Checks per file, segment counts, your check result, the main choices (dhamma, kusala / akusala / abyākata, how the dyad patterns read, group names, headings), unsure Pāli and source slips.
