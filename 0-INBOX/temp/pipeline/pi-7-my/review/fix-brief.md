# Brief: apply the bilingual-review fixes to the pi-7 Burmese rails

## Setup and rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`, called by its full path. Put scripts in files.
- `regen_rails.sh` is a zsh script and slow: run it with `zsh`, in the background.
- Write only in `0-INBOX/temp/pipeline/pi-7-my/rails/` and `pi-7-my/review/`, plus the rails output folder through regen_rails.sh.
- Never use the system temp directory: not /private/tmp, not /tmp, no `cd /tmp`. Scratch files go in `pi-7-my/rails/`.
- Never commit.
- Never use the words for a planted starting value or its negative.
- No existing Burmese translation, nissaya or web source. Never open `0-INBOX/temp/language-priority/`.
- Read `pi-1-my/` … `pi-6-my/` only; never edit them.

## Where to fix
The rails text `AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters/` is built by `pi-7-my/rails/regen_rails.sh`: the layer `my_formulas_rails.py` + `build_rails.py`, then the rules `residual_rules.py` / `apply_termbase.py`.
- **Model:** `pi-6-my/rails/apply_fixes.py` and `pi-6-my/review/fix-notes.md`.
- **Repeated formulas** go into the rails layer, as labelled patches with exact counts, so every repetition changes together. In this book that means:
  - the case of a subject in the pañhāvāra example frames;
  - the stacking «၊»;
  - the coordination «…လည်းကောင်း».
- **Rules on the built text keyed on the Pāli** are allowed where the frames come from several generators (as in pi-6). They go in a new `pi-7-my/rails/apply_fixes.py`, run by regen_rails.sh after the existing rules. Each rule is restricted to segment IDs or Pāli triggers, with expected counts; the run fails on a mismatch. Log them to `rails/fixes-log.tsv`.
- **Never edit:**
  - the zero-shot chapters, the generators or `my7_formulas.py`;
  - any termbase / decisions / APPROVED.md file.

## Inputs
- **Reports:** `pi-7-my/review/report-A.md` (A1–A9), `report-B.md` (B1–B19), `report-C.md` (C1–C6).
- **Pāli:** `AI_translation/pali/pi-7_split_chapters/`.
- **Style:** `0-INBOX/temp/pipeline/burmese-style.md`.

## Termbase change already made (2026-11-26, coordinator)
See APPROVED.md «Change 2026-11-26»:
- **B15:** the hetuka headings now read «… အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ / သုံးမျိုးတွဲ».
- **B16 / A7:** bhindati is «သင်းခွဲသည်».

The new sha256 is ceb0842a98d4a219466e1fc494f071773710cb9963554bd1dc8dd6e61fecff74. It is already in regen_rails.sh TB_SHA, and the termbase-folder md5s are re-recorded in protected-md5-before.txt.

Re-run the zero-shot adherence with the new termbase and update the classification. The rows the change makes GENUINE are fixed by your rules / patches.

## Decisions (coordinator, under the user's standing go-ahead)

### APPLY (meaning), book-wide by pattern
Find EVERY instance by script against the Pāli, in ALL 75 chapters, not only the reviewer's part. Reviewers A and C found the same kind of error in their parts (A1, C1).
- **The conditioning subject in the pañhāvāra example clauses must be the subject.**
  - A nominative subject takes «…သည်», and co-subjects take «Xလည်းကောင်း၊ Yလည်းကောင်း».
  - The conditioned items take «…အား» (several: «…အားလည်းကောင်း၊ …အားလည်းကောင်း»).
  - Never move a conditioning item into the dative list, never drop it, and never mark it «ကို».
  - This covers:
    - B1–B9;
    - the recurring patterns B7 («SUBJ X-assa ca Y-ānañca») and B8 (senāsanaṃ / cittaṃ / neuter -aṃ nominatives as «ကို»);
    - A1 (Adinnādānaṃ «…ယူခြင်းသည်»);
    - C1 (uppannā / anuppannā / uppādī hetū «…အမြစ်တို့သည်», with «၊» between the two recipients).

  Write a case check that pairs each Pāli example clause with its Burmese. Use B's description: nominative / neuter «-aṃ» subject, genitive / dative recipients, «ca … ca». It must report 0 left.
- **B10** (stray «ca» slip, 3 places): use the intended X→X reading, as at 3-10 line 590.
- **B13 and B14** (slips): «dhammaṃ» is not a third item; ^7-35-101 «novigatapaccayena» in an anuloma list gets the intended positive avigata. Log both as spelling-only slips.
- **A2:** «paṭisandhikkhaṇe natthi» = «ပဋိသန္ဓေ နေသော ခဏ၌ မရှိ», in every instance.
- **A5:** «…avigatapaccayā» closing a «vitthāretabbā» list = «…အကြောင်းအထိ», where the Pāli marks the end of the list.

### APPLY (consistency), book-wide
- **B11:** «A ca B ca N» coordinations become «A Nလည်းကောင်း၊ B Nလည်းကောင်း», never the stacking form. Find every one by the Pāli.
- **B12:** a real stack of two «…သော» qualifiers on one noun takes «၊» between them, e.g. «အမြစ် မရှိသော၊ အကြောင်း ရှိသော အစုအဝေး».
  - This applies book-wide, including the approved sample. It replaces the earlier plain-space convention for descriptive qualifiers such as ahetuka, because the plain space misparses.
  - Apply it only where both are qualifiers of the same noun in the Pāli.
- **A3:** (Cakkaṃ kātabbaṃ) = «(စက်ဝိုင်း ပြုရမည်)» everywhere.
- **A4:** idaṃ nānākaraṇaṃ = «ဤသည်မှာ ကွဲပြားမှု ဖြစ်သည်».
- **B16 / A7:** saṅghaṃ bhindati = «သံဃာကို သင်းခွဲသည်», following the termbase change.
- **B15:** the hetuka headings follow the termbase change. That covers the 2-04 triad title and the 4-01 dyad titles, plus every heading, colophon and note that names them.
- **B17:** tīṇiyeva moho takes one form. Use the reading the Pāli gives, «… သုံးခု၌သာ မောဟ», if that is what it means in all instances; otherwise give the majority form, with a reason.
- **C2, C3:** the order phrase goes outside the quote in the chapter-end titles (as 5-xx / 2-17), and C3's added quotes go.
- **C4 / A9:** «((မသေချာ))» becomes «(မသေချာ)» everywhere.

### APPLY (minor)
- **A6:** the note gets a subject.
- **A8:** the note gets a subject.
- **B18:** Vārasattakaṃ is «ဖော်ပြချက် ခုနစ်မျိုး».
- **B19:** vimati is «သံသယ».
- **C6:** «…ကိုလည်း၊ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် …» (the «၊» against the garden path), in all instances of the frame.

### KEEP
- **C5:** two condition locatives sharing one count keep the Pāli's list with no connector (harmonise H13). This is a known convention.

### Verify every pattern by script
For every pattern, find ALL instances by script and apply only where the Pāli matches. Identical Pāli must stay identical Burmese.

## Verify (all must pass, in regen_rails.sh)
- **Per chapter:** all 75 files pass check_chapter_ids.py, the text check (rails wrapper) and check_marks.py.
- **Adherence:** GENUINE 0.
- **Case check:** 0 left.
- **pi-1 … pi-6 identity** unchanged:
  - pi-1 12/12, pi-2 74/74, pi-3 2/2, pi-4 7230/7230, pi-5 6/6, pi-6 3/3.
  - If a fix would change a sentence shared with pi-1 … pi-6, keep the earlier book's Burmese for that sentence and report it.
- **Alignment:** align_check 0 differing; align_hidden 0.
- **Line scan:** line_scan 0.
- **Unchanged inputs:**
  - the zero-shot files are unchanged;
  - the termbase hash equals the new lock;
  - the protected md5s are unchanged.
- **Reproducibility:** a second run gives byte-identical output.

## Report (short, numbers first)
- Per fix ID: the instances changed.
- Lines changed per chapter, against the pre-fix rails and against the zero-shot.
- The check results.
- Anything not applied, and why.

Put the same in `review/fix-notes.md`, together with the decisions above.
