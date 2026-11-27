# Brief: word-sense-grouper, Pāli→Burmese (pi-3, Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Scripts in files. Write only in `0-INBOX/temp/pipeline/pi-3-my/senses/` (and, after the full run is approved and done, the one output file below). Never use the system temp directory (not even /private/tmp). Don't commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/` and `pi-2-my/` only.

**Read first:**
- `AI_translation/skills/word-sense-grouper.md` (follow it exactly) and the approved pi-2 run: `0-INBOX/temp/pipeline/pi-2-my/burmese-senses-brief.md` (incl. «Full run»), its tools `pi-2-my/senses/senses_my.py`, `gen_decisions_my.py`, and the results `AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md`, `AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md`.
- `0-INBOX/temp/pipeline/burmese-style.md`; `pi-3-my/my3-zeroshot-terms.md`, `pi-3-my/harmonise-notes.md`, `pi-3-my/mapper-my/map-harmonise-notes.md` (the kept sense differences: arūpa, dukkha, rūpa, hetukā dhammā, uppannā, sammā, pucchake / pucchakena …) and `pi-3-my/burmese-mapper-brief.md` «Approved sample» (saṅgaha «အကျုံးဝင်ခြင်း» vs pi-1 / pi-2 «စုစည်းခြင်း» / «အကျဉ်းချုပ်»: a different sense).

**Tags and granularity:**
- **pi-2 then pi-1 Burmese senses are binding** for the same headword: same split and same English tag wherever pi-3's Burmese values fit those senses; add a sense only where pi-3 evidence shows a genuinely new meaning (e.g. saṅgaha = inclusion).
- For headwords new in pi-3, take the ENGLISH tags (never the values) from the Marathi pi-3 senses `AI_translation/marathi/pi-3-pali-word-marathi-senses-plain.md`, adjusted to the Burmese evidence.
- Grammatical variants of one Burmese lemma = ONE sense (" / ", most frequent first); synonyms of one meaning = ONE sense as candidates; split only for genuinely different meanings; a value under only one sense; English tags, real glosses; no "; " or "/" inside a candidate except " / ".

**Tools (copied into pi-3-my/senses/):** `senses_my.py` (build / verify, unchanged), `ids.py <headword>` (every pi-3 Burmese value with its segment ids; adapt its paths to pi-3 if needed). Write `gen_decisions_my.py` from pi-2's (read pi-2 then pi-1 Burmese senses first, then Marathi pi-3 tags; keep its MANUAL / LUMP_OK mechanism). Input `agg-part1.tsv` (658 headwords).

**This run: SAMPLE only.** `agg-sample.tsv` (first 80 headwords) → `decisions-sample.txt` → `sample-senses.md`; `senses_my.py verify agg-sample.tsv sample-senses.md` must print VERIFY OK. Write the generator so it can later cover all of agg-part1.tsv (report its dry-run UNRESOLVED / REVIEW counts). Stop after the sample.

**Final report (short):** headword count and verify result; multi-sense and multi-candidate counts; every split or clash in the sample with the decision; how many headwords took pi-2 / pi-1 senses unchanged; tool changes.

**Full run (sample approved by the user, 2026-11-19, incl. the rūpa / sammā splits and the new saṅgaho / saṅgaha «inclusion», vippayogo «dissociation» senses):** keep the 80 sample headwords exactly; run `gen_decisions_my.py agg-part1.tsv decisions-part1.txt`, settle every UNRESOLVED (5: dukkha, dukkhaṃ, niyatehi, hetukehi, niyatehi dhammehi) and check every REVIEW (17) headword by hand; `senses_my.py build agg-part1.tsv decisions-part1.txt part1-senses.md` then `verify` → VERIFY OK; the first 80 lines must equal sample-senses.md; copy to `AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md` and verify the copy. Note for maccu: the pi-3 text has «သေခြင်း»; record it as attested (the termbase step decides; the pi-2 termbase has «သေဆုံးခြင်း»).
