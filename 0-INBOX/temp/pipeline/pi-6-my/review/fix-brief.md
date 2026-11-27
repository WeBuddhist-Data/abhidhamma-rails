# Brief: apply the bilingual-review fixes to the pi-6 Burmese rails

## Setup and rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Call it by its full path, never through a quoted shell variable. Put scripts in files.
- `regen_rails.sh` is a zsh script: run it with `zsh`, not bash.
- Write only in `0-INBOX/temp/pipeline/pi-6-my/rails/` and `pi-6-my/review/`, plus the rails output folder through regen_rails.sh.
- Never use the system temp directory: not /private/tmp, not /tmp, no `cd /tmp`.
- Never commit.
- Never use the words for a planted starting value or its negative.
- No existing Burmese translation, nissaya or web source. Never open `0-INBOX/temp/language-priority/`.
- Read `pi-1-my/` … `pi-5-my/` only; never edit them.

## Where to fix
The rails text `AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters/` is built by `pi-6-my/rails/regen_rails.sh`, with the layer `my_formulas_rails.py` + `build_rails.py` and the rules `apply_termbase.py`. The model is `pi-5-my/rails/apply_fixes.py` and `pi-5-my/review/fix-notes.md`.
- **Repeated formulas:** a fix that changes a repeated formula or proposition goes into the rails layer, as labelled patches with exact counts, so every repetition changes together. The Yamaka is generated from frames, so most fixes belong here.
- **Single-segment fixes:** these go into a new `pi-6-my/rails/apply_fixes.py`, run by regen_rails.sh after the existing rules. Use explicit rules restricted to segment IDs or Pāli triggers, with expected counts; the run fails on a mismatch. Log them to `rails/fixes-log.tsv`.
- **Never edit:** the zero-shot chapters, the generators, `my6_formulas.py`, or any termbase / decisions / APPROVED.md file. The termbase stays as locked (sha256 847e49cd…).

## Inputs
- The reviews: `pi-6-my/review/report-A.md` (A1–A6), `report-B.md` (B1–B7) and `report-C.md` (C1–C9).
- Pāli: `AI_translation/pali/pi-6_split_chapters/`.
- Style: `0-INBOX/temp/pipeline/burmese-style.md`.

## Decisions (coordinator, under the user's standing go-ahead)

### APPLY (meaning)
- **C1:** avaseso kāyo / avasesā upekkhā keep their head noun: «ကြွင်းကျန်သော ကိုယ်သည် …», «ကြွင်းကျန်သော ဥပေက္ခာတို့သည် …». Do this in all six lines, and check by script for every «avasesa + noun» in the indriya niddesa.
- **B2:** in the pacchimacitta lines (6-01 / 6-02, 24 lines), kāmāvacarānaṃ names the beings: «အကြင်စိတ်၏ ချက်ချင်း နောက်၌ နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့် ကာမဘုံ၌ ရှိသူတို့ …».
  - This is the termbase's beings sense of kāmāvacarānaṃ, so classify the adherence row as CONTEXT with a check. Do not change the termbase.
  - Apply the same to rūpāvacarānaṃ / arūpāvacarānaṃ if the same frame has them.
- **B4,** in the same lines: the apposition without «အနက်», «…ပရိနိဗ္ဗာန် ပြုမည့်သူတို့၊ စုတေဆဲ ထိုသူတို့အား».
- **B3:** ^6-6-147 «ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်၌လည်း …», as ^6-6-158.
- **A1:** the rūpa word-play at ^6-2-26 / 27 / 28 (6 lines) gets the gloss, as the sota one: «… အရာသည် “ရူပ” (ရုပ် သို့မဟုတ် သဘော) ဖြစ်သည်၊ ရုပ် အစုအဝေး မဟုတ်။», and the paccanīka the same.

### APPLY (consistency, book-wide by frame)
- **Genitive persons before a moment or a mind (C2, C3, B5):** where a genitive plural of persons / beings stands before «…၏ … ခဏ၌» or a mind / moment phrase, and is picked up by tesaṃ / tassa, use the genitive «…တို့၏», not «…တို့၊». The model is the existing «Sabbesaṃ cittassa bhaṅgakkhaṇe» → «…တို့၏ စိတ်၏ …». Examples:
  - «သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူတို့၏ ဒုတိယ စိတ် ဖြစ်နေစဉ်၊ …»
  - «အခြားသူတို့၏ စိတ်၏ ဖြစ်ခြင်း ခဏ၌ ထိုသူတို့အား»
  - «ပထမ ဈာန်ကို ဝင်စားနေသူ ကာမဘုံ၌ ရှိသူတို့၏ ဝင်လေ ထွက်လေတို့၏ ဖြစ်ခြင်း ခဏ၌ ထိုသူတို့အား»

  Find every instance by script, in all chapters, and apply it only where the Pāli has the genitive plural.
  - Where two genitives are stacked (samāpannānaṃ kāmāvacarānaṃ), join them as the text already does elsewhere, without «၊».
  - Keep «၊» where the Pāli lists separate groups.
- **C6:** «…pacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe» takes the attributive «…ဖြစ်ပေါ်မည့် ထိုစိတ်၏ …», as the parallel frames in 5-xx / 9-xx.
- **C4:** a restated answer verb takes «ကြ» exactly when the question's verb has «ကြ» (same subject).
- **B1:** in the dhātu / vedanā lists, put «၊» before the apariyāpanna item instead of «နှင့်» (145 lines). The model is the two places in 7-06 / 7-08 that already have «၊».
- **C7:** give the 9-01 padasodhana (^6-9-1 … 8) one treatment of head noun and number for kusala / akusala / abyākata, in anuloma and paccanīka. Follow the text's majority form.
- **C9:** «၊» before «သို့သော်» in the split answers that lack it (6 places), as all the others.
- **A2 / B6 / C5:** «Sabbesaṃ» «သူ အားလုံးတို့၏» → «သူအားလုံးတို့၏» book-wide (202 places). This rendering does not occur in pi-1 … pi-5.

### APPLY (minor)
- **A3:** the sadisa notes at ^6-4-10: «(အသံ အပိုင်းသည် နှာခေါင်း အပိုင်းနှင့် တူညီသည်)», «(လျှာ အပိုင်းလည်း နှာခေါင်း ဓာတ် အပိုင်းနှင့် တူညီသည်)», «(အထိအတွေ့ အပိုင်းသည် နှာခေါင်း အပိုင်းနှင့် တူညီသည်)». Use the same form for any other X-sadisa note of this kind.
- **A4:** (Cakkaṃ bandhitabbaṃ) «(လှည့်ပတ်ခြင်းကို ဖွဲ့ရမည်)», without «အပြည့်အစုံ», in all 15 places.
- **A5:** ^6-4-12 as ^6-4-17's rendering of the same sense.

### APPLY (quote rule; A6, B7, C8)
- No quote mark where the Pāli has none. This covers:
  - the labels in the editorial notes («“အကြင်နေရာ၌” အပိုင်း» → «အကြင်နေရာ၌ အပိုင်း»);
  - quoted answers in notes («“ဟုတ်ပါသည်”» → «ဟုတ်ပါသည်»);
  - yāva saraṇaaraṇā;
  - any other added quote.
- **Keep two kinds:**
  - the approved «“X” ပြီးဆုံးပြီ» chapter-end form, the pi-1 … pi-5 pattern;
  - the two word-play glosses «“သောတ” (…)» and «“ရူပ” (…)», where the quote marks a Pāli word being mentioned.
- Check that the quote counts per line then match the Pāli, except for these kept kinds.

### Not reported, and stays
Head nouns that Burmese needs (termbase §A14) stay, unless they change the meaning, as C1 did.

## Verify (all must pass, in regen_rails.sh)
- **All 44 files:** check_chapter_ids.py, check_text_pe (wrapper) and check_marks.py are OK.
- **Adherence:** GENUINE 0, with every new miss classified with a check.
- **pi-1 … pi-5 identity is unchanged:**
  - pi-1: 10/10
  - pi-2: 14/14
  - pi-3: 10/332, plus 322 explained
  - pi-4: 10/10
  - pi-5: 2791/2791

  If a fix would change a sentence shared with pi-1 … pi-5, keep the earlier book's Burmese for that sentence and report it.
- **Alignment:** align_check gives 0 differing, and align_hidden gives 0.
- **Other checks:**
  - line_scan: 0.
  - The zero-shot files are unchanged.
  - The termbase hash equals the lock.
  - The protected md5s are unchanged.
- **Stability:** a second run gives byte-identical output.

## Report (short, numbers first)
- For each fix ID: the instances changed.
- The lines changed per chapter, against the pre-fix rails and against the zero-shot.
- The check results.
- Anything not applied, and why.

Put the same into `review/fix-notes.md`, with the decisions above.
