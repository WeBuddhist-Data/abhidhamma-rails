# Brief: word-sense-grouper, Pāli→Burmese (pi-1, Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Run Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (the system python3 is too old). Write helper scripts to files. Write only in `0-INBOX/temp/pipeline/pi-1-my/senses/` (and, after the full run is approved and done, the one output file named below). Never use the system temp directory. Don't commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/burmese-religious-affairs/`).

**Read first:**
- `AI_translation/skills/word-sense-grouper.md`, and follow it exactly.
- `0-INBOX/temp/pipeline/burmese-style.md` (approved core terms), `pi-1-my/my-zeroshot-terms.md`, `pi-1-my/harmonise-notes.md`, `pi-1-my/mapper-my/map-harmonise-notes.md` (the kept sense differences, e.g. rūpa ×3, bahiddhā ×3, paṭigha ×2, kāya ×2).
- The approved Marathi pi-1 senses (format and granularity model): `0-INBOX/temp/pipeline/pi-1-mr/marathi-senses-brief.md` and `AI_translation/marathi/pi-1-pali-word-marathi-senses-plain.md`.
- **English tags:** there is no English senses file for pi-1. Take the ENGLISH tags (never the Marathi values) of the same headword from the Marathi pi-1 senses file as your starting gloss, and adjust them where the Burmese evidence shows a different split. Same tag wording where the same headword and sense recur.

**Input:** `pi-1-my/senses/agg-part1.tsv` (2485 headwords; the English column is empty). Line: `headword <TAB> (empty) <TAB> burmese_value=count[example ids] | … <TAB> NDE=<count>`.

**Method:** adapt the approved Marathi tool `pi-1-my/senses/senses_sample.py` (copied from pi-1-mr) into `pi-1-my/senses/senses_my.py`: replace the Devanagari checks with Myanmar (U+1000–U+109F), and the Marathi join word with « နှင့် » if an attested value ever contains " / ". Keep build / verify. Helper `pi-1-my/senses/ids.py <headword>` lists every Burmese value with all its segment ids (it reads the Burmese keyword map). A small generator that turns the Marathi English tags into decision lines is the expected way to cover 2485 headwords; then review each headword's Burmese values by hand where they split or look odd.

**Guidance:**
- Grammatical variants of one Burmese lemma (with / without a particle, «…သော» / «…ခြင်း» of the same verb, counted / bare) are ONE sense, joined with " / ", most frequent first.
- Synonyms for the SAME meaning go in ONE sense as candidates; the termbase step picks one.
- Split only for genuinely different meanings: rūpa as matter (ရုပ်) / visible object (အဆင်းအရောင်) / fine-material plane (သိမ်မွေ့သော ရုပ်); kāya as body (ကိုယ်) vs mental body (စိတ်၏ အဖော်တို့); paṭigha aversion (မုန်းတီးမှု) vs impact (ထိခိုက်မှု); bahiddhā in others / outside / external; dhamma as phenomena (သဘောတရား) vs object of mind; maggaṃ way (လမ်း) vs path (မဂ်). When unsure, open the segments by id in `AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/` and `AI_translation/pali/pi-1_split_chapters/`.
- A value may appear under only one sense of a headword. If one value carries two meanings, put it under its majority sense and say so in the other sense's tag.
- Tags in English, short, a real gloss, never a copy of the value. A candidate must not contain "; " or "/" except as the separator " / ".
- NDE occurrences are excluded already; don't add "(no direct equivalent)".

**This run: SAMPLE only.** Use `pi-1-my/senses/agg-sample.tsv` (the first 82 headwords of agg-part1.tsv) → `decisions-sample.txt` → `sample-senses.md`; `senses_my.py verify agg-sample.tsv sample-senses.md` must print VERIFY OK. Also write the generator so it can later cover all of agg-part1.tsv. Stop after the sample: the user reviews it.

**Full run (sample approved by the user, 2026-11-17).**
- `sample-senses.md` / `decisions-sample.txt` are approved: their 82 headwords keep exactly those senses and tags (paṭicca stays one sense with two candidates; indriya one sense; Dhamma two senses).
- Use `gen_decisions_my.py agg-part1.tsv decisions-part1.txt`, then settle every UNRESOLVED headword (several Marathi senses) and check every REVIEW headword (values lumped into one sense) by hand, as in the guidance. Save the decisions file as you go.
- `senses_my.py build agg-part1.tsv decisions-part1.txt part1-senses.md`, then `senses_my.py verify agg-part1.tsv part1-senses.md` must print VERIFY OK; the first 82 lines must equal sample-senses.md.
- Copy part1-senses.md to `AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md` and verify that copy too.

**Final report (short):** headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; every split or synonym clash in the sample with the decision taken; anything in the tool you changed.
