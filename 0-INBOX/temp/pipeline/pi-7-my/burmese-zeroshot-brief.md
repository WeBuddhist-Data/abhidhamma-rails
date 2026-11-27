# Brief: Burmese zero-shot, remaining chapters (pi-7, Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»)

## Setup and rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Call it by that full path, never through a quoted shell variable. Put scripts in files.
- Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus your generator, check and notes named after your chapters, inside `0-INBOX/temp/pipeline/pi-7-my/`.
- Never use the system temp directory: not /tmp, not /private/tmp, no `cd /tmp`.
- Do not commit.
- Never use the words for a planted starting value or its negative.
- You may be paused for usage limits and resumed later. Generate chapter by chapter, save each chapter as soon as it passes, and keep your notes current.

## Source rule (binding)
- Translate FROM THE PĀLI only.
- Never open or copy any existing Burmese translation or nissaya, and never open `0-INBOX/temp/language-priority/`.
- No web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`. It is binding, including the locked pi-1 … pi-6 termbase sections.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- **The approved pi-7 sample is READ-ONLY and the model for everything.** The coordinator approved it on 2026-11-23 under the user's standing go-ahead; the decisions are in `pi-7-my/agents.txt`. Its files:
  - `pi-7-my/my7_formulas.py`: import it. Extend its tables in memory in YOUR script, never edit it, and log every new string in your notes.
  - `pi-7-my/make_sample.py`: copy functions from it, but never run it, because it rewrites shared files.
  - `check_sample.py` and `chk_mutate.py`: adapt them as `check_<your chapters>.py`, including the polarity, condition, term-order, number, recurring-sentence and reuse tests.
  - `check_text_pe7.py`.
  - `my7-zeroshot-terms.md`: copy its strings verbatim.
  - `notes-sample.md`.
  - The outputs `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/1-00-paccaya.md` and `1-02-vedanattika.md`.
- **Approved choices:**
  - the title «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»;
  - paccaya «အကြောင်း», and «Xpaccayena paccayo» «Nဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်»;
  - the 24 condition names in all their cases, and the counts «Nဟူသော အကြောင်း၌ …ခု»;
  - paṭicca / nissāya «…ကို မှီ၍»;
  - the section and order headings, anuloma / paccanīya «အဟုတ်ပြ / အငြင်းပြ ပုံစံ»;
  - variants in braces «{ပါဌ်ကွဲ (…): …}», as the Pāli has them.
- **pi-1 … pi-6 final Burmese are binding for identical Pāli:**
  - the Mātikā triads and dyads;
  - khandha / āyatana / dhātu / indriya names;
  - citta, the realms and the person types;
  - path and fruit.

  They are in the rails texts `AI_translation/burmese/pi-{1,…,6}-burmese-plain-rails_split_chapters/` and the locked termbases `AI_translation/burmese/pi-{1,…,6}-pali-burmese-termbase-plain.md`. Read them the way the sample's module does. Never edit anything in `pi-1-my/` … `pi-6-my/`, or the sample's shared files in `pi-7-my/`.
- **Cross-check of MEANING only (never wording):**
  - the English pi-7 zero-shot `AI_translation/english/pi-7-english-plain-zeroshot_split_chapters/<same file>`;
  - the Marathi pi-7 rails `AI_translation/marathi/pi-7-marathi-plain-rails_split_chapters/<same file>`.
- **Method model for the frames:** `0-INBOX/temp/pipeline/pi-7-mr/make_<chapters>.py` and `notes-<chapters>.md`. Use the frame inventory only, never Marathi words.

## About the text
Each triad / dyad chapter repeats the sample's seven sections:
- paṭicca, sahajāta, paccaya, nissaya, saṃsaṭṭha, sampayutta and pañhā;
- each in the anuloma, paccanīya, anuloma-paccanīya and paccanīya-anuloma orders;
- each with its vibhaṅga and its saṅkhyāvāra counts.

What changes is the chapter's terms: the triad or dyad, or in the dukatika / tikaduka chapters a dyad combined with a triad. Build each term and each frame once and fill the frames from them, so identical Pāli gets identical Burmese. Every one of these must match the Pāli exactly, checked by script:
- the term order (conditioning → conditioned);
- the condition named;
- polarity (na-Xpaccayā, naXe);
- every number and khandha count.

## Source and output
- **Source:** `AI_translation/pali/pi-7_split_chapters/<ch>.md`.
- **Output:** `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/<ch>.md`.
- **Generator:** `pi-7-my/make_<chapters>.py`.
- **Check:** `pi-7-my/check_<chapters>.py`.
- **Notes:** `pi-7-my/notes-<chapters>.md`.

## Rules
- **Identity:** identical Pāli = identical Burmese, within pi-7, with the sample, and with pi-1 … pi-6 final.
- **Generate every chapter by script:** frames and tables for the repeated parts, and hand-written strings for unique prose, kept in a table in the script (as the sample does). The script stops on any unmatched sentence.
- **Exactness:** polarity and numbers must be exact, checked by script.
- **Structure:**
  - Headings keep their #-level.
  - Block IDs are exact.
  - Keep the source's number of non-empty lines per segment, one blank line between segments, and no double blank lines.
- **New recurring terms or phrases:** record each in your notes as «Pāli = Burmese», one per line. Do not edit my7_formulas.py or my7-zeroshot-terms.md; a consistency pass aligns all agents afterwards.
- **Punctuation:**
  - «…pe…» / «…Pe…» become one «…».
  - DASH RULE: «–» only where the Pāli line has one, in the same spot and with the same count.
  - No «।», «:-» or «?». Questions end with their particle (လော / နည်း) and «။»; statements end with «။».
  - No quote marks where the Pāli has none.
- **Digits and variants:** digits as the Pāli; variants as the sample.
- **Source slips:** translate as written, and log them.

## Verify every chapter (all must pass before you report)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-7_split_chapters AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-7-my/check_text_pe7.py AI_translation/pali/pi-7_split_chapters/<ch>.md AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-7_split_chapters/<ch>.md AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/<ch>.md
```
- All must print OK. If check_text_pe7 needs a scratch copy, use a folder named after your chapters under `pi-7-my/chk-pe/`, and delete it afterwards.
- Your own check must also pass: 0 mismatches, and the reuse test n / n.

## Final report (short)
- For each chapter: the checks, segment count, own check, and reuse n / n.
- The key new terms and frames, or a pointer to your notes.
- Unsure Pāli and source slips.
