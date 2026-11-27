# Brief: word-sense-grouper, Pāli→Burmese (pi-4, Puggalapaññatti «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Scripts in files. Write only in `0-INBOX/temp/pipeline/pi-4-my/senses/` (and, after the full run is approved and done, the one output file below). Never use the system temp directory (not even /private/tmp). Don't commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/`, `pi-2-my/` and `pi-3-my/` only.

**Read first:**
- `AI_translation/skills/word-sense-grouper.md` (follow it exactly) and the approved pi-3 run: `0-INBOX/temp/pipeline/pi-3-my/burmese-senses-brief.md` (incl. «Full run»), its tools `pi-3-my/senses/senses_my.py`, `gen_decisions_my.py`, `lookup_my.py`, and the results `AI_translation/burmese/pi-{1,2,3}-pali-word-burmese-senses-plain.md`.
- `0-INBOX/temp/pipeline/burmese-style.md`; `pi-4-my/my4-zeroshot-terms.md` (the person-type names), `pi-4-my/harmonise-notes.md`, `pi-4-my/mapper-my/map-table.md` (rules P1–P8, A2) and `map-harmonise-notes.md` (the kept sense differences, e.g. eka «တစ်စေ့» in Ekabījī, vaṇṇa praise, pāṇa, indriya in indriyasaṃvara, dhamme in diṭṭhe dhamme, vuṭṭhāti attainment / illness, bhagavā epithet at ^4-177).

**Tags and granularity:**
- **pi-3, then pi-2, then pi-1 Burmese senses are binding** for the same headword: same split and same English tag wherever pi-4's Burmese values fit those senses; add a sense only where pi-4 evidence shows a genuinely new meaning.
- For headwords new in pi-4, take the ENGLISH tags (never the values) from the Marathi pi-4 senses `AI_translation/marathi/pi-4-pali-word-marathi-senses-plain.md`, adjusted to the Burmese evidence.
- Grammatical variants of one Burmese lemma = ONE sense (" / ", most frequent first); synonyms of one meaning = ONE sense as candidates; split only for genuinely different meanings; a value under only one sense; English tags, real glosses; no "; " or "/" inside a candidate except " / ".

**Tools (copied into pi-4-my/senses/):** `senses_my.py` (build / verify, unchanged), `ids.py <headword>` (every pi-4 Burmese value with its segment ids; already pointed at the pi-4 map). Write `gen_decisions_my.py` from pi-3's (read pi-3, then pi-2, then pi-1 Burmese senses first, then Marathi pi-4 tags; keep its MANUAL / LUMP_OK mechanism and its logged-reason rule). Input `agg-part1.tsv` (2133 headwords).

**This run: sample, then the full set, without an approval stop** (user's standing go-ahead, 2026-11-19; the coordinator reviews the result). First `agg-sample.tsv` (first 80 headwords) → `decisions-sample.txt` → `sample-senses.md`, VERIFY OK; then `gen_decisions_my.py agg-part1.tsv decisions-part1.txt`, settle every UNRESOLVED and check every REVIEW headword by hand; `senses_my.py build agg-part1.tsv decisions-part1.txt part1-senses.md` then `verify` → VERIFY OK; the first 80 lines must equal sample-senses.md; copy to `AI_translation/burmese/pi-4-pali-word-burmese-senses-plain.md` and verify the copy.

**Final report (short):** headword / sense counts and verify results; multi-sense and multi-candidate counts; each UNRESOLVED and REVIEW decision in one line; every new sense with its reason; how many headwords took pi-3 / pi-2 / pi-1 senses unchanged; tool changes.
