# Brief: termbase-builder, Pāli→Burmese plain (pi-3, Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Call Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Write helper scripts to files. Write ONLY inside `0-INBOX/temp/pipeline/pi-3-my/termbase/` (plus the two files the assembler writes). Never use the system temp directory (not even /private/tmp). Don't commit. Never use the words for a planted starting value or its negative. The termbase is built only from this book's own evidence and the locked pi-1 / pi-2 termbases: no existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`).

## Read first
- `AI_translation/skills/termbase-builder.md`. Follow it.
- `AI_translation/audience_profile/plain.md`: understanding comes first.
- `0-INBOX/temp/pipeline/burmese-style.md`: the user-approved core terms, the «Lessons from earlier tracks» and the pi-1 / pi-2 termbase sections are binding.
- **The LOCKED pi-2 and pi-1 termbases are binding:** `AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md` + `0-INBOX/temp/pipeline/pi-2-my/termbase/APPROVED.md` (incl. the 2026-11-18 review changes: maccu «သေဆုံးခြင်း», siṅga «ဟန်လုပ်မှု / ဟန်လုပ်ခြင်း», sevanā path sense), then `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md` + `pi-1-my/termbase/APPROVED.md` (bahiddhā «မိမိ၏ ပြင်ပ၌», proper names stay names, nāma-rūpa «စိတ်ပိုင်း / ရုပ်ပိုင်း» …). Same Pāli headword in the same sense = pi-2's term (else pi-1's), unless that term never occurs in the pi-3 text: then keep the pi-3 form and report it, or align it (ALIGNED / OUTSIDE) when the locked term is a user-approved review change (maccu: decide and explain; the pi-3 text has «သေခြင်း»).
- This book's choices: `pi-3-my/my3-zeroshot-terms.md` (approved sample), `pi-3-my/harmonise-notes.md`, `pi-3-my/mapper-my/map-harmonise-notes.md` (kept sense differences; text inconsistencies: maccu, pucchaka «ဖော်ပြချက်» vs «မေးခွန်း», «တို့» / «များ», arūpa spacing), `pi-3-my/burmese-mapper-brief.md` «Approved sample» (saṅgaha «အကျုံးဝင်ခြင်း» …).
- Method model: the approved pi-2 run `pi-2-my/burmese-termbase-brief.md` and its tools in `pi-2-my/termbase/` (family_scan.py, synonym_check.py, show.py, hwinfo.py, pi1_match.py …). Copy and adapt them into `pi-3-my/termbase/` (pi-3 paths; match against BOTH pi-2 and pi-1). Never edit anything in `pi-1-my/` or `pi-2-my/`.

## Input and output
- Input: `AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md` (658 headwords, 663 senses; 6 senses have more than one candidate).
- Decisions: `pi-3-my/termbase/decisions-A.tsv`, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based in the senses file's order).
- Assembler: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/termbase_assemble.py 3 burmese my plain`. It keeps single-candidate senses, requires one decision for every multi-candidate sense, allows re-aligning a single-candidate sense (ALIGNED), lists terms outside the candidates (OUTSIDE), writes `AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md` and `pi-3-my/termbase/termbase-decisions.md`, and fails on any error.
- Family scan: before / after outputs to `family-scan-before.txt` / `family-scan-after.txt`.
- Helpers: `pi-3-my/senses/ids.py <headword>`; `pi-3-my/seg.py` (segment viewer).

## How to choose
1. **Multi-candidate senses:** the one term a plain Burmese reader understands best: (a) the locked pi-2 / pi-1 term; (b) the approved core term (burmese-style.md, my3-zeroshot-terms.md, harmonise decisions); (c) the form the translation uses most; (d) the clearest plain candidate. Dictionary form as in the mapping rules.
2. **Family consistency:** all inflections and compounds of one Pāli lemma in the same sense get the same Burmese word (topic names, saṅgaha / asaṅgaha, sampayutta / vippayutta, the instrumental items). Keep the genuine sense differences in the senses file (rūpa ×3, sammā ×2, dukkha ×2, arūpa ×2, saṅgaha inclusion vs pi-1 / pi-2 senses).
3. **Keep contrasted pairs distinct** (burmese-style.md lessons).
4. **Term form:** no ", ", " / ", "; " or «၊» inside a term. Never a dash.
5. **Outside terms** only when every candidate is wrong for a plain reader, or to follow a locked pi-2 / pi-1 review change; give the reason. These go to the user for approval.
6. Choose ONE term for each text inconsistency in `mapper-my/map-harmonise-notes.md` so the rails translation becomes consistent (maccu, pucchaka, the plural markers where a termbase term decides them).

## Verify
The assembler prints "no errors". The family scan (after) lists no lemma family with more than one Burmese word for the same sense, unless explained.

## Report (short, plain, numbers first)
The assembler's summary line; how many senses took pi-2's / pi-1's term; family re-alignments; the outside choices with reasons; the most consequential choices (with the alternative rejected); senses that depart from pi-2 / pi-1 and why; anything a Burmese speaker should check. The user must approve explicitly; do not call it locked.
