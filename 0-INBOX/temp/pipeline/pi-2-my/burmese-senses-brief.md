# Brief: word-sense-grouper, Pāli→Burmese (pi-2, Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Scripts in files. Write only in `0-INBOX/temp/pipeline/pi-2-my/senses/` (and, after the full run is approved and done, the one output file below). Never use the system temp directory. Don't commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/` only.

**Read first:**
- `AI_translation/skills/word-sense-grouper.md` (follow it exactly) and the approved pi-1 run: `0-INBOX/temp/pipeline/pi-1-my/burmese-senses-brief.md` (incl. «Full run»), its tools `pi-1-my/senses/senses_my.py`, `gen_decisions_my.py`, and the result `AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md`.
- `0-INBOX/temp/pipeline/burmese-style.md`; `pi-2-my/my2-zeroshot-terms.md`, `pi-2-my/harmonise-notes.md`, `pi-2-my/mapper-my/map-harmonise-notes.md` (the kept sense differences: paccayā, dhātu, hetu, rūpa, paṭigha, attha, dhamma, ajjhattaṃ, bahiddhā …).

**Tags and granularity:**
- **pi-1 Burmese senses are binding** for the same headword: same split and same English tag wherever pi-2's Burmese values fit those senses; add a sense only where pi-2 evidence shows a genuinely new meaning.
- For headwords new in pi-2, take the ENGLISH tags (never the values) from the Marathi pi-2 senses `AI_translation/marathi/pi-2-pali-word-marathi-senses-plain.md`, adjusted to the Burmese evidence.
- Grammatical variants of one Burmese lemma = ONE sense (" / ", most frequent first); synonyms of one meaning = ONE sense as candidates; split only for genuinely different meanings; a value under only one sense; English tags, real glosses; no "; " or "/" inside a candidate except " / ".

**Tools (copied into pi-2-my/senses/):** `senses_my.py` (build / verify, unchanged), `gen_decisions_my.py` (adapt: read pi-1 Burmese senses first, then Marathi pi-2 tags; keep its MANUAL / LUMP_OK mechanism), `ids.py <headword>` (every pi-2 Burmese value with its segment ids). Input `agg-part1.tsv` (4956 headwords).

**This run: SAMPLE only.** `agg-sample.tsv` (first 82 headwords) → `decisions-sample.txt` → `sample-senses.md`; `senses_my.py verify agg-sample.tsv sample-senses.md` must print VERIFY OK. Write the generator so it can later cover all of agg-part1.tsv (report its dry-run UNRESOLVED / REVIEW counts). Stop after the sample.

**Full run (sample approved by the user, 2026-11-18, incl. the ajjhattaṃ and dukkha splits):** keep the 82 sample headwords exactly; run `gen_decisions_my.py agg-part1.tsv decisions-part1.txt`, settle every UNRESOLVED (38) and check every REVIEW (256) headword by hand; `senses_my.py build agg-part1.tsv decisions-part1.txt part1-senses.md` then `verify` → VERIFY OK; the first 82 lines must equal sample-senses.md; copy to `AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md` and verify the copy.

**Final report (short):** headword count and verify result; multi-sense and multi-candidate counts; every split or clash in the sample with the decision; how many headwords took pi-1's senses unchanged; tool changes.
