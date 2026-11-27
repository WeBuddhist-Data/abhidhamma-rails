# Brief: consistency pass over the pi-3 Burmese keyword mapping, then assemble

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails (macOS, zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Scratch only in `0-INBOX/temp/pipeline/pi-3-my/mapper-my/` (never the system temp directory, not even /private/tmp). Never commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/` and `pi-2-my/` only. Back up every script you edit into `mapper-my/harmonise-backup/` and snapshot all `*.mapped.md` there first.

Four scripts mapped the 16 files: `map_all.py` (preamble, 1-uddeso, 2-pathamanayo: the user-approved sample), `map_ch3-6-8-9.py`, `map_ch7-10-11.py`, `map_ch12-15.py`, each with `map-table*.md`. Rules: `pi-3-my/burmese-mapper-brief.md` (incl. «Approved sample»: M1–M9 and the 11 approved differences), the approved pi-1 / pi-2 rules it cites, and each agent's new rules (ch3-6-8-9 M10–M13; ch7-10-11 M1–M5; ch12-15 Q1–Q6: several are the same rule under different names). Model: the pi-2 pass, `pi-2-my/mapper-my/map-harmonise-brief.md` and `map-harmonise-notes.md`.

## Decisions (apply; changes only through the scripts, then re-run them)
1. The approved sample values (preamble, 1-uddeso, 2-pathamanayo) and the approved differences from pi-1 / pi-2 stay unchanged.
2. Same keyword, same kind of segment, same value book-wide. Scan all `*.mapped.md` for keywords with more than one value; align each (state the rule) or keep it as a genuine sense / grammar difference (state why). Known: upari «အထက်» vs «အထက်တွင်» vs «ထို့အထက်»; dhammā vippayuttā (relative clause «ကင်းကွာသော သဘောတရား» vs frame «သဘောတရား … ကင်းကွာသော»); bhavena vippayuttā contiguous vs gapped; pucchake «ဖော်ပြချက်» vs pucchakena «မေးခွန်း»; the "su" fragments; punareva; buddho; arūpa (^3-352 «ရုပ် မဟုတ်သော» vs planes «ရုပ်မရှိသော»); sukha «သာယာသော» (sample function).
3. One merged rule list: the instrumental / dative rule (ch3-6-8-9 M11 = ch7-10-11 M1 = ch12-15 Q1), the vippayuttā pairing (M12 / M2–M3 / Q2), kehici «အချို့» (M10 / M5 / Q3), the verse words (M13 / Q5 / ch7-10-11 verse list), and one documented list of presence-check endings across all scripts.
4. maccu: the pi-3 text has «သေခြင်း»; the pi-2 termbase now has maccu «သေဆုံးခြင်း» (user-approved review change). Map what the pi-3 text says, and list it as a text inconsistency for the rails step.
5. Absolutives «…၍», no « / » alternatives, no «၊» or ", " in values.
6. Do not change the translation files. List text inconsistencies you meet in the notes for the rails step.

## Verify (all must pass)
- For all 16 files: the keyword-preservation one-liner in the mapper brief prints `bad []`; each script's presence verifier reports 0 failures; no ", " / «၊» / « / » in any value.
- The scan in 2 shows only logged, justified differences.
- Assemble: move any `*sample*` files out of `mapper-my/` first if present, then
  `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/mapper_chunks.py assemble AI_translation/pali/pi-3-keywords-by-reference-pali-plain.md 0-INBOX/temp/pipeline/pi-3-my/mapper-my AI_translation/burmese/pi-3-keywords-by-reference-pali-burmese-plain.md`: every ID once, unchanged keyword counts (568 lines).

## Log and report
`mapper-my/map-harmonise-notes.md`: decisions, scripts changed, values changed per chapter, scan before/after, kept differences with reasons, text inconsistencies for the rails step. Final report short, numbers first.
