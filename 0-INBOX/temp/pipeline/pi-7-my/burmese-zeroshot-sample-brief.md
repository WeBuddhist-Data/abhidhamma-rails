# Brief: Burmese zero-shot SAMPLE for pi-7 (Paṭṭhāna)

## Setup
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Use the Read/Write tools for files.
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (the system python3 is too old). Call it by that full path, never through a quoted shell variable. Write helper scripts to files rather than inline `-c` with regexes.
- Scratch, scripts and notes go only in `0-INBOX/temp/pipeline/pi-7-my/`.
- Never use the system temp directory: not /tmp, not /private/tmp, no `cd /tmp`.
- Do not commit.
- Never use the words for a planted starting value or its negative; say "sample" or "model".

## What you are building
You write the model that later agents copy for the rest of the book (76 files, 4.7 MB of Pāli). The shared pieces (formula module, term list) matter as much as the text.
- Write part by part and save as soon as each part passes: you may be paused for usage limits and resumed later.
- Keep your notes current.
- Stop after the sample. The coordinator reviews it.

## Source rule (binding, user 2026-11-16/17)
- Translate FROM THE PĀLI only.
- Never look up, open or copy any existing Burmese translation or nissaya, and never open `0-INBOX/temp/language-priority/`.
- Do no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`: binding rules, typography, the dash rule, the approved core terms and the locked pi-1 … pi-6 termbase sections.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- **pi-1 … pi-6 Burmese are binding** wherever the Paṭṭhāna uses their terms, lists and sentences:
  - the Mātikā triads and dyads (pi-1);
  - the 24 conditions wherever pi-2 (paccayākāra) or later books name them;
  - khandha / āyatana / dhātu / indriya names;
  - citta types, vatthu, paṭisandhi, mahābhūta / upādārūpa, cittasamuṭṭhāna, kaṭattārūpa, āhāra, jhāna and magga factors;
  - the realms and the person types;
  - the Yamaka (pi-6) and Kathāvatthu (pi-5) frames where they recur.

  Use the FINAL Burmese: the rails texts `AI_translation/burmese/pi-{1,2,3,4,5,6}-burmese-plain-rails_split_chapters/` and the locked termbases `AI_translation/burmese/pi-{1,…,6}-pali-burmese-termbase-plain.md` (see their `pi-N-my/termbase/APPROVED.md`).

  The modules show how the final strings are produced. Import or copy them READ-ONLY, and never edit anything in pi-1-my/ … pi-6-my/, so that identical Pāli gets identical Burmese:
  - `pi-1-my/my_formulas.py` + `pi-1-my/rails/`;
  - `pi-2-my/my2_formulas.py` + `pi-2-my/rails/`;
  - `pi-5-my/my5_formulas.py` + `pi-5-my/rails/`;
  - `pi-6-my/my6_formulas.py` + `pi-6-my/rails/` (incl. `apply_fixes.py`).

  Where the zero-shot module and the rails differ, the RAILS text wins.
- **Method model** (formula module + generator):
  - `pi-6-my/make_sample.py`, `pi-6-my/check_sample.py`, `pi-5-my/make_sample.py`;
  - the Marathi pi-7 run `0-INBOX/temp/pipeline/pi-7-mr/make_sample.py`, `mr_formulas.py`, `sample_tables.py` and `notes-sample.md`. Take only the method and the frame inventory from it, never Marathi words.
- **Cross-check of MEANING only (never wording):** the English pi-7 zero-shot `AI_translation/english/pi-7-english-plain-zeroshot_split_chapters/<same file>` and the Marathi pi-7 rails `AI_translation/marathi/pi-7-marathi-plain-rails_split_chapters/<same file>`.

## About the text
The Paṭṭhāna lists the 24 conditions (paccaya) and defines each, in 1-00-paccaya («Hetupaccayoti – hetū hetusampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ hetupaccayena paccayo.»). The 24 are: hetu, ārammaṇa, adhipati, anantara, samanantara, sahajāta, aññamañña, nissaya, upanissaya, purejāta, pacchājāta, āsevana, kamma, vipāka, āhāra, indriya, jhāna, magga, sampayutta, vippayutta, atthi, natthi, vigata, avigata.

It then applies them to the triads and dyads of the Dhammasaṅgaṇī mātikā.
- **Seven sections per triad:** paṭicca-, sahajāta-, paccaya-, nissaya-, saṃsaṭṭha-, sampayutta- and pañhāvāra.
- **Orders in each section:** forward (anuloma), negative (paccanīya) and the two mixed orders; the analysis (vibhaṅga); and the counting (saṅkhyāvāra: «Hetuyā nava, ārammaṇe tīṇi …»).
- **The main frame:** «Kusalaṃ dhammaṃ paṭicca kusalo dhammo uppajjati hetupaccayā – kusalaṃ ekaṃ khandhaṃ paṭicca tayo khandhā …».

Everything turns on:
- which state conditions which, i.e. the order and case of the two terms («X paṭicca Y», «X Yassa … paccayena paccayo»);
- the condition named;
- polarity (na-hetupaccayā …, «nahetuyā»);
- the numbers in the counts («nava, tīṇi, ekaṃ, pañca …»);
- the khandha counts (ekaṃ / dve / tayo).

The book repeats its frames hundreds of thousands of times. Every frame must be ONE Burmese string, built by a function of its terms.

## Core terms
Choose these with care and log each choice, because the whole book repeats them:
- paccaya (check pi-2's paccayākāra and the termbases first) and «paccayena paccayo»;
- paṭicca, uppajjati «ဖြစ်ပေါ်»;
- the 24 condition names in the nominative, the -paccayā ablative and the counting locative «Hetuyā / Ārammaṇe»;
- the section and vāra names, and anuloma / paccanīya (pi-6 has anuloma / paccanīka «အဟုတ်ပြ / အငြင်းပြ ပုံစံ»; decide whether the Paṭṭhāna sense is the same and say why);
- the doctrinal terms: sahajāta, taṃsamuṭṭhāna rūpa, cittasamuṭṭhāna rūpa, mahābhūta, upādārūpa, kaṭattārūpa, paṭisandhi, vatthu;
- the number words.

Propose the Burmese book title for the Paṭṭhāna: plain, Burmese only.

## Your output
1. The WHOLE of `1-00-paccaya.md` (33 KB: the 24 conditions and their definitions) and the WHOLE of `1-02-vedanattika.md` (73 KB: a full triad with all seven sections, the counts and the pañhāvāra). Use the same filenames in `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/`, saving part by part.
2. `pi-7-my/my7_formulas.py`: the shared pi-7 module that later agents import. It holds:
   - every frame as a function of its terms, conditions, polarity and numbers;
   - the condition names in each case;
   - the section and vāra headings, and the chapter names and colophons;
   - the triad / dyad term tables (from pi-1 final);
   - the number words;
   - the reused terms.
3. `pi-7-my/make_sample.py`. It imports my7_formulas.py and writes the two files, using frames and tables for the repeated parts. Hand-written strings are allowed only for unique lines, kept in a table in the script. It stops on any unmatched sentence.
4. `pi-7-my/my7-zeroshot-terms.md`: every formula and term as «Pāli = Burmese», grouped: the book title, headings, the 24 conditions in each case, the frames by section / order / polarity, the counting frames, the doctrinal terms, the number words.
5. `pi-7-my/check_sample.py`. It checks per line:
   - polarity per clause;
   - the condition named;
   - the term order (conditioning → conditioned);
   - numbers and khandha counts;
   - that every recurring frame gets the same Burmese;
   - the table values, with 0 mismatches.

   It also runs a **pi-1 … pi-6 reuse test**: every term and Pāli sentence of the sample that also occurs in pi-1 … pi-6 must have exactly their final Burmese (report n / n identical).
6. `pi-7-my/notes-sample.md`: your choices, unsure Pāli, and source slips.

## Rules
- **Identity:** identical Pāli = identical Burmese, within pi-7 and with pi-1 … pi-6 final. Each Pāli synonym gets its own Burmese.
- **Exactness:** polarity and numbers must be exact; check them by script.
- **Structure:**
  - Headings keep their #-level.
  - Block IDs are exact.
  - One blank line between segments, the source's number of non-empty lines per segment, and no double blank lines.
- **Punctuation:**
  - «…pe…» / «…Pe…» become one «…».
  - DASH RULE: «–» only where the Pāli line has one, in the same spot and with the same count.
  - No «।», no «:-», no «?». Questions end with their question particle (လော / နည်း) and «။»; statements end with «။».
  - No quote marks where the Pāli has none.
- **Digits and brackets:** digits as the Pāli, e.g. «(1)». Variant brackets as pi-1: «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]». The Pāli writes variants in braces, «{paccayoti (syā.)}»; render them in the bracket form.
- **Language:** natural plain Burmese, with nothing added. Book title in Burmese only.
- **Source slips:** translate as written and flag them in the notes.

## Verify every file (all must pass)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-7_split_chapters AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-7_split_chapters/<ch>.md AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-7_split_chapters/<ch>.md AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/<ch>.md
```
- All three must print OK. If check_text_pe needs a scratch copy, keep it under `pi-7-my/chk-pe/` and delete it afterwards; never write in `pi-6-mr/`.
- Your own check must give 0 mismatches, and the reuse test n / n.

## Final report (short)
- The checks per file, segment counts, your check result, and the reuse test.
- The main choices: book title, headings, the 24 conditions, the frames, what was reused from pi-1 … pi-6, and new terms.
- Unsure Pāli and source slips.

## Approval
The user gave a standing go-ahead on 2026-11-19. The coordinator reviews and approves the sample; still stop after the sample and report.
