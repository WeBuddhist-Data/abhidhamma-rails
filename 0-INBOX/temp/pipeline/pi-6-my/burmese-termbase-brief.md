# Brief: termbase-builder, Pāli→Burmese plain (pi-6, Yamaka «အတွဲလိုက် မေးဖြေခြင်း»)

## Setup and rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Call it by that full path, never through a quoted shell variable. Write helper scripts to files.
- Write ONLY inside `0-INBOX/temp/pipeline/pi-6-my/termbase/`, plus the two files the assembler writes.
- Never use the system temp directory: not /tmp, not /private/tmp, no `cd /tmp`.
- Don't commit.
- Never use the words for a planted starting value or its negative.
- Build the termbase only from this book's own evidence and the locked pi-1 … pi-5 termbases. Use no existing Burmese translation, nissaya or web source, and never open `0-INBOX/temp/language-priority/`.

## Read first
- `AI_translation/skills/termbase-builder.md`. Follow it.
- `AI_translation/audience_profile/plain.md`: understanding comes first.
- `0-INBOX/temp/pipeline/burmese-style.md`: the user-approved core terms, the «Lessons from earlier tracks» and the pi-1 … pi-5 termbase sections are binding.
- **The LOCKED pi-5, pi-4, pi-3, pi-2 and pi-1 termbases are binding:** `AI_translation/burmese/pi-{5,4,3,2,1}-pali-burmese-termbase-plain.md`, with `0-INBOX/temp/pipeline/pi-{5,4,3,2,1}-my/termbase/APPROVED.md` and their change notes. These include:
  - pi-5:
    - paṭivedha family «ထိုးဖောက်၍ သိ…», kept apart from vipassanā;
    - abhisamaya family «ထင်ထင်ရှားရှား သိမြင်…»;
    - abhisambuddh- family «ကိုယ်တိုင် အပြည့်အဝ သိမြင်…»;
    - thero «မထေရ်»;
    - voropeti «သတ်»;
    - ānantarika «ချက်ချင်း အကျိုးပေးသော ကံ»;
    - samphaṃ «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား»;
    - the sabyābajjha pair.
  - pi-4: narassa, sāci.
  - pi-3: buddho.
  - pi-2: maccu, siṅga, the path senses.
  - pi-1:
    - bahiddhā;
    - proper names stay names;
    - nāma-rūpa «စိတ်ပိုင်း / ရုပ်ပိုင်း».
- **Which locked term applies:** for the same Pāli headword in the same sense, use pi-5's term; else pi-4's, pi-3's, pi-2's, pi-1's, in that order.
  - **The locked term never occurs in the pi-6 text:** keep the pi-6 form and report it, or align it (ALIGNED / OUTSIDE) when the locked term is a review change. Decide and explain.
  - **A sense new in pi-6:** it takes its own term (see the senses file's new senses and logged reasons).
- **This book's choices:**
  - `pi-6-my/my6-zeroshot-terms.md` and `pi-6-my/notes-sample.md`. The approved sample has:
    - Āmantā «ဟုတ်ပါသည်», No «မဟုတ်ပါ», Natthi «မရှိပါ»;
    - hetu «အကြောင်း» in the hetuvāra list;
    - anuloma / paccanīka «အဟုတ်ပြ ပုံစံ / အငြင်းပြ ပုံစံ»;
    - cavati «စုတေ».
  - `pi-6-my/harmonise-notes.md`: the book-wide forms.
  - `pi-6-my/mapper-my/map-table.md`: rules R1–R9.
  - `notes-g1.md`, `notes-g2.md`, `notes-g3.md`.
  - `map-harmonise-notes.md`: §A, the 14 text items for the rails step; §B, the kept sense / grammar differences.
- **The senses step's logs** in `pi-6-my/senses/`: new senses and reasons.
- **Method model:** the approved pi-5 run, `pi-5-my/burmese-termbase-brief.md` and its tools in `pi-5-my/termbase/` (build.py with the raw-*.tsv parts, family_scan.py, pi1234_match.py, newcheck.py, hwinfo.py …).
  - Copy and adapt them into `pi-6-my/termbase/`, with pi-6 paths, matching against pi-5, pi-4, pi-3, pi-2 and pi-1.
  - Keep pi-5's layout: raw-multi / raw-align / raw-family / raw-textinc, composed by `build.py` into decisions-A.tsv. The coordinator makes later changes through it.
  - Never edit anything in `pi-1-my/` … `pi-5-my/`.

## Input and output
- **Input:** `AI_translation/burmese/pi-6-pali-word-burmese-senses-plain.md`.
- **Decisions file:** `pi-6-my/termbase/decisions-A.tsv`.
  - One line each: `hw|sense_index<TAB>term<TAB>short reason`. sense_index is 0-based, in the senses file's order.
  - Group the lines in commented parts: multi-candidate, family alignment, locked-term alignment, text inconsistencies.
- **Assembler:** `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/termbase_assemble.py 6 burmese my plain`.
  - It keeps single-candidate senses and requires one decision for every multi-candidate sense.
  - It allows re-aligning a single-candidate sense (ALIGNED) and lists terms outside the candidates (OUTSIDE).
  - It writes `AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md` and `pi-6-my/termbase/termbase-decisions.md`, and fails on any error.
- **Family scan:** write the before / after outputs to `family-scan-before.txt` / `family-scan-after.txt`.
- **Helpers:** `pi-6-my/senses/ids.py <headword>` and the senses step's context tools.

## How to choose
1. **Multi-candidate senses:** pick the one term a plain Burmese reader understands best, in this order:
   1. the locked pi-5 … pi-1 term;
   2. the approved core term (burmese-style.md, my6-zeroshot-terms.md, the harmonise decisions);
   3. the form the translation uses most;
   4. the clearest plain candidate.

   Use the dictionary form, as in the mapping rules.
2. **Family consistency:** all inflections and compounds of one Pāli lemma in the same sense get the same Burmese word. This covers:
   - the Yamaka frame words: the pair questions, the vāra names, the moments «ဖြစ်ခြင်း ခဏ / ပြိုပျက်ခြင်း ခဏ», and the planes and beings of a plane;
   - the doctrinal terms of each chapter: the roots, aggregates, bases, elements, truths, formations, latent tendencies «ကိန်းအောင်းခြင်း», citta, dhamma and the 22 faculties;
   - the path / fruit terms.

   Keep the genuine sense differences of the senses file.
3. **Keep contrasted pairs distinct:**
   - the burmese-style.md lessons;
   - sekha vs paṭipannaka;
   - rūpadhātu as plane vs as element;
   - aññaṃ as faculty vs "other";
   - the kāmāvacara plane / beings vs adjective.
4. **Term form:** no ", ", " / ", "; " or «၊» inside a term, and never a dash.
5. **Outside terms:** use one only when every candidate is wrong for a plain reader, or to follow a locked earlier-book review change. Give the reason.
6. **Text inconsistencies:** choose ONE term for each item in `mapper-my/map-harmonise-notes.md` §A that a term can decide (for example the uppāda vāra name vs the moment, kāyasaṅkhāra «ကိုယ်၏ …», the spacing of sacchikaroti). That makes the rails translation consistent. List the items a term cannot decide (spelling, slips, added head nouns, word order) for the rails step.
7. **Identity with earlier books:** a pi-6 sentence that also occurs in pi-1 … pi-5 keeps their final rails Burmese, so a term must not break it. Check the shared sentences, with the tool model `pi-6-my/harmonise_pi12345.py`, and report any conflict instead of choosing against it.

## Verify
- The assembler prints "no errors".
- The family scan (after) lists no lemma family with more than one Burmese word for the same sense, unless explained.

## Report (short, plain, numbers first)
- The assembler's summary line.
- How many senses took pi-5's / pi-4's / pi-3's / pi-2's / pi-1's term.
- The family re-alignments.
- The outside choices, with reasons.
- The most consequential choices, with the alternative rejected.
- The senses that depart from pi-1 … pi-5, and why.
- The §A items decided, and those left for rails.
- Anything a Burmese speaker should check.

The coordinator reviews and locks the termbase under the user's standing go-ahead. Do not call it locked yourself.
