# Brief: consistency pass over the pi-2 Burmese keyword mapping, then assemble

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails (macOS, zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Scratch only in `0-INBOX/temp/pipeline/pi-2-my/mapper-my/`. Never commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/` only. Back up every script you edit into `mapper-my/harmonise-backup/` and snapshot all `*.mapped.md` there first.

Eight scripts mapped the 19 chapters: `map_all.py` (preamble, 1-khandhavibhango: the user-approved sample), `map_2-4.py`, `map_5-7-11.py`, `map_6.py`, `map_12-14.py`, `map_15-16.py`, `map_17.py`, `map_18.py`, each with `map-table*.md`. Rules: `pi-2-my/burmese-mapper-brief.md` (incl. «Approved sample»), the approved pi-1 rules (`pi-1-my/mapper-my/map-table.md` 1–11, `map-harmonise-notes.md`), the sample's N1–N11, and each agent's new rules (C*, M*, N12+, P*). Model: the pi-1 pass, `pi-1-my/mapper-my/map-harmonise-brief.md` and `map-harmonise-notes.md`.

## Decisions (apply; changes only through the scripts, then re-run them)
1. The approved sample values (preamble, ch1) and the six approved differences from pi-1 stay unchanged.
2. Same keyword, same kind of segment, same value book-wide. Scan all `*.mapped.md` for keywords with more than one value; align each (state the rule) or keep it as a genuine sense / grammar difference (state why). Expect sense splits such as paccayā (chain «ကြောင့်» vs «X-paccayā» «အကြောင်းပြု၍»), dhātu (plane «ဘုံ» vs element «ဓာတ်»), hetu (root vs cause), rūpa (three senses), paṭigha, attha, dhamma (teaching vs phenomenon), ajjhattaṃ.
3. One form for the presence-check endings across all scripts (merge the agents' P*/M1/N12 ending lists into one documented list) and one rule for persons «…သူ» vs attributive «…သော» (pi-1 practice).
4. (no direct equivalent): relative pronouns as approved; compound members rendered inside one Burmese word (caya rule) consistently across chapters.
5. Absolutives «…၍», «samaye X» = «အချိန်၌ ရှိသော X», no « / » alternatives, no «၊» or ", " in values.
6. Do not change the translation files. List text inconsistencies you meet (e.g. vaṇṇamacchariya «ဂုဏ်သတင်း» vs «ဂုဏ်ကျေးဇူး», kulamacchariya at ^2-U50, abhijjhādomanassā «…မှု» vs pi-1 «…ခြင်း», the missing mutta at ^2-356) in the notes for the rails step.

## Verify (all must pass)
- For all 19 chapters: the keyword-preservation one-liner in the mapper brief prints `bad []`; each script's presence verifier reports 0 failures; no ", " / «၊» / « / » in any value.
- The scan in 2 shows only logged, justified differences.
- Assemble: move any `*sample*` files out of `mapper-my/` first if present, then
  `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/mapper_chunks.py assemble AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md 0-INBOX/temp/pipeline/pi-2-my/mapper-my AI_translation/burmese/pi-2-keywords-by-reference-pali-burmese-plain.md` — every ID once, unchanged keyword counts (1541 lines).

## Log and report
`mapper-my/map-harmonise-notes.md`: decisions, scripts changed, values changed per chapter, scan before/after, kept differences with reasons, text inconsistencies for the rails step. Final report short, numbers first.
