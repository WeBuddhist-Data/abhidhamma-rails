# Brief: Pāli→Burmese keyword mapping (pi-7, Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»)

## Rules for this run
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`, called by its full path (never through a quoted shell variable). Put helper scripts in files.
- Write ONLY inside `0-INBOX/temp/pipeline/pi-7-my/mapper-my/`.
- Never use the system temp directory: never /private/tmp or /tmp, and no `cd /tmp`.
- Don't commit.
- Never use the words for a planted starting value or its negative.
- Source rule: never open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`), and no web searches.
- Read `pi-1-my/` … `pi-6-my/` only; never edit them.

## Read first
- **The skill you execute:** `AI_translation/skills/keyword-equivalence-mapper.md`.
- **Style and the pi-7 text's own forms:**
  - `0-INBOX/temp/pipeline/burmese-style.md`;
  - `pi-7-my/my7-zeroshot-terms.md`, `pi-7-my/notes-*.md`, `pi-7-my/harmonise-notes.md`, `pi-7-my/harmonise-table.tsv`;
  - the shared values in `pi-7-my/my7_formulas.py` and the group generators.

  These are the forms the pi-7 text uses. The text is FINAL (harmonised), so map against the CURRENT chapter files.
- **The user-approved pi-1 Burmese mapping rules (binding):**
  - `0-INBOX/temp/pipeline/pi-1-my/burmese-mapper-brief.md`, including «Approved sample»;
  - `pi-1-my/mapper-my/map-table.md` (rules 1–11);
  - the agreed later rules in `pi-1-my/mapper-my/map-table-*.md` and `map-harmonise-notes.md`. These say:
    - absolutives keep «…၍»;
    - relative pronouns get (no direct equivalent) where the Burmese builds the clause with «ရှိသော»;
    - one sense per segment;
    - no « / » alternatives.
- **pi-1 … pi-6 values are binding** for the same keyword in the same kind of segment, provided the value occurs in the pi-7 segment (the pi-7 text reuses their Burmese for identical Pāli). The values are in `AI_translation/burmese/pi-{1,2,3,4,5,6}-keywords-by-reference-pali-burmese-plain.md`. Their rules:
  - pi-2: N1–N11;
  - pi-3: M1–M9;
  - pi-4;
  - pi-5: Q1–Q8, S1–S6, G1–G5;
  - pi-6: R1–R9 and the group rules G / V / W, in `pi-6-my/mapper-my/map-table.md`, `notes-g1/g2/g3.md`, `map-harmonise-notes.md` and the phase-3 brief `pi-6-my/burmese-mapper-brief-phase3.md`. That brief also holds the five mechanics phase 3 fixed:
    - the literal tier needs `phrase_ok`;
    - base_forms skips finite «-anti»;
    - shared_being stays in one clause;
    - -amāno is a person;
    - the «Xပြီး မဟုတ်» ending.
- **Method model:** the pi-6 run.
  - `pi-6-my/mapper-my/map6_rules.py` is the final, side-effect-free shared module, with its BOOK table.
  - Also study `map_sample.py`, `map_g1.py` and `frame_coverage.py`.
  - Copy the approach into your own module; do not import a pi-6 file if importing runs it.

## Per chapter <ch>
- **Keywords:** `mapper-my/<ch>.keywords.md`, split by the coordinator: 75 files, 15312 lines, about 3 MB.
- **Burmese:** `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/<ch>.md` (merged copy: `AI_translation/burmese/pi-7-burmese-plain-zeroshot.md`).
- **Pāli:** `AI_translation/pali/pi-7_split_chapters/<ch>.md`.
- **Output:** `mapper-my/<ch>.mapped.md`. Same lines and order, same keywords in the same order, each written `pali=ဗမာ`.

## Verify each chapter (all must pass)
1. Keyword preservation, which must print `bad []`:
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-7-my/mapper-my');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
2. Presence: every chunk of every value must occur in that segment's Burmese, as a phrase. Only the particles and endings the approved rules strip are allowed to differ. List and justify every exception.
3. No ", " and no «၊» inside any value, and no « / » alternatives.

## This run: PHASE 1 of 3 (preamble, 1-00-paccaya and 1-02-vedanattika only)
pi-7 is huge and extremely formulaic, so mapping runs in three phases. The user's standing go-ahead (2026-11-19 / 2026-11-21) means there is no approval stop; the coordinator reviews each phase.
- **Phase 1 (you):** the sample chapters. They hold the whole machinery, so they fix the mapping of every recurring frame keyword for the whole book:
  - the 24 condition names in every case;
  - «paccayena paccayo», paṭicca, uppajjati;
  - the term qualifiers, the khandha counts, and the counting frames;
  - the section / order / vāra headings;
  - the notes.
- **Phase 2 (later, parallel agents):** the triad, dyad, dukatika / tikaduka and part-5 groups, importing your shared module.
- **Phase 3 (later):** book-wide consistency scan and assembly.

### Your tasks
1. **Shared module.** Write `mapper-my/map7_rules.py` so that later agents can import it WITHOUT side effects (no work at import time). It holds:
   - the frame / stock-keyword tables;
   - the condition names in each case and polarity;
   - the stacked term qualifiers «A၊ B N» and the na-X forms of part 5;
   - the compose rules, the context functions and the presence verifier, with the phrase_ok literal tier.

   Start from pi-6's `map6_rules.py`: copy it, do not import it. Keep the module general: a keyword whose value depends on the frame gets a context function, not a sample-only line rule.
2. **Sample script.** Write `mapper-my/map_sample.py`. It uses the module, maps the preamble, 1-00-paccaya and 1-02-vedanattika, and runs the verifier. Produce their `.mapped.md` files.
3. **Rules table.** Write `mapper-my/map-table.md`:
   - the rules used, with pi-1 … pi-6 rules by name;
   - any NEW rule, explained;
   - the frame keyword → Burmese table;
   - the count of values taken unchanged from pi-1 … pi-6.
4. **Recurring frames check (for phase 2).**
   - Script a list of the 300 most frequent keywords of the WHOLE book (all `*.keywords.md`), with the value your module gives each.
   - Check the presence of those values over the whole book's Burmese (all 75 chapter files).
   - Do a whole-book dry run: how many keyword uses the module maps, leaves unmapped, or maps by stem fallback.
   - Write `mapper-my/frame-coverage.md`: keyword, uses, value, presence rate, and the chapters where it fails and why. Add a suggested split of the remaining 72 chapters into phase-2 groups of similar size.
   - Fix the module where a failure is a module error. Leave genuine context differences to a context function, or note them.
5. **Notes.** Record keyword ambiguities and text inconsistencies you meet in `mapper-my/map-harmonise-notes.md`. Do not change the translation.
6. Do NOT map other chapters, and do NOT assemble.

## Final report (short)
- Per file: line count, verifier results, and the (no direct equivalent) count.
- New rules beyond pi-1 … pi-6's.
- Values that differ from pi-1 … pi-6 for the same keyword, with the reason.
- Frame-coverage summary: how many of the 300 reach 100% presence, the dry-run counts, and the suggested phase-2 groups.
- Text inconsistencies for the rails step.
- Genuinely unclear mappings.
