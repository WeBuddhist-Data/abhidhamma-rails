# Brief: word-sense-grouper, Pāli→Burmese (pi-7, Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»)

## Setup and rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Call it by that full path, never through a quoted shell variable. Put scripts in files.
- Write only in `0-INBOX/temp/pipeline/pi-7-my/senses/`, plus, at the end, the one output file named below.
- Never use the system temp directory: not /tmp, not /private/tmp, no `cd /tmp`.
- Don't commit.
- Never use the words for a planted starting value or its negative.
- No existing Burmese translation, nissaya or web source. Never open `0-INBOX/temp/language-priority/`.
- Read `pi-1-my/` … `pi-6-my/` only; never edit them.

## Read first
- `AI_translation/skills/word-sense-grouper.md`. Follow it exactly.
- The approved pi-6 run:
  - its brief `0-INBOX/temp/pipeline/pi-6-my/burmese-senses-brief.md`;
  - its tools in `pi-6-my/senses/` (`senses_my.py`, `gen_decisions_my.py`, `lookup_my.py`, `ids.py` and the helpers);
  - the results `AI_translation/burmese/pi-{1,2,3,4,5,6}-pali-word-burmese-senses-plain.md`.
- `0-INBOX/temp/pipeline/burmese-style.md`.
- The pi-7 notes:
  - `pi-7-my/my7-zeroshot-terms.md`, `pi-7-my/harmonise-notes.md` and `harmonise-table.tsv`;
  - `pi-7-my/mapper-my/map-table.md` (rules T1–T13, M1, M2);
  - `notes-g1.md` … `notes-g6.md` (group rules and values that differ from pi-1 … pi-6, with reasons) and `phase3-changes.tsv`;
  - `map-harmonise-notes.md`: §A the 38 text items, §B the 88 keywords kept with more than one value (grammar, construction, sense, text; `work/scan-class.tsv`), §F unclear points.

Some pi-7 senses to watch for:
- the 24 condition names (hetu, ārammaṇa, adhipati, kamma, vipāka, āhāra, indriya, jhāna, magga, atthi, natthi, vigata …) as a CONDITION («Nဟူသော အကြောင်း», the Paṭṭhāna sense) vs their ordinary senses in earlier books (hetu «အမြစ်» root, ārammaṇa object, kamma, vipāka result, magga path, atthi "is"); keep them apart where the values differ.
- the triad / dyad terms as qualifiers vs nouns (vipāka «ကံ၏ အကျိုး ဖြစ်သော» vs the condition), the gocchaka items as bare nouns.
- anuloma: the order «အဟုတ်ပြ ပုံစံ» vs the mind moment «လျော်ညီခြင်း စိတ်»; paccanīya «အငြင်းပြ ပုံစံ».
- cakka «စက်ဝိုင်း»; paṭicca / nissāya «မှီ၍»; samanantara «ကောင်းစွာ ချက်ချင်း နောက်».

## Tags and granularity
- **Earlier books' Burmese senses are binding for the same headword.** Check pi-6 first, then pi-5, pi-4, pi-3, pi-2, pi-1. Keep the same split and the same English tag wherever pi-7's Burmese values fit those senses. Add a sense only where the pi-7 evidence shows a genuinely new meaning; a different grammatical form of one meaning is not new.
- **Headwords new in pi-7:** take the English tags (never the values) from the Marathi pi-7 senses `AI_translation/marathi/pi-7-pali-word-marathi-senses-plain.md`, adjusted to the Burmese evidence.
- **Sense grouping:**
  - Grammatical variants of one Burmese lemma make ONE sense (" / ", most frequent first).
  - Synonyms of one meaning make ONE sense, as candidates.
  - Split only for genuinely different meanings.
  - A value goes under only one sense.
- **Tags and candidates:** English tags, with real glosses. No "; " or "/" inside a candidate except " / ".

## Tools
- Copy them from `pi-6-my/senses/` into `pi-7-my/senses/` (incl. its MR_ADJUST mechanism).
- `senses_my.py` (build / verify): use it unchanged.
- `ids.py <headword>`: point it at the pi-7 map `AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md`.
- `gen_decisions_my.py`: adapt it to read the pi-6, pi-5, pi-4, pi-3, pi-2 and pi-1 Burmese senses in that order, then the Marathi pi-7 tags. Keep its MANUAL / LUMP_OK mechanism and its logged-reason rule.

## Inputs (already prepared by the coordinator)
- `pi-7-my/senses/agg-part1.tsv`: 2312 headwords, with the tag column empty. Three headwords with only (no direct equivalent) values are omitted; see `omitted-nde-only.txt`.
- `agg-sample.tsv`: the first 80 headwords.

## This run: sample, then the full set, without an approval stop
The user gave a standing go-ahead on 2026-11-19; the coordinator reviews the result.
1. Run the sample: `agg-sample.tsv` → `decisions-sample.txt` → `sample-senses.md`, and check VERIFY OK.
2. Run the full set: `gen_decisions_my.py agg-part1.tsv decisions-part1.txt`. Settle every UNRESOLVED and check every REVIEW headword by hand.
3. Build and verify: `senses_my.py build agg-part1.tsv decisions-part1.txt part1-senses.md`, then `verify`, which must give VERIFY OK. The first 80 lines must equal `sample-senses.md`.
4. Copy the result to `AI_translation/burmese/pi-7-pali-word-burmese-senses-plain.md` and verify the copy.
5. Run the build twice to show it is byte-identical.

## Final report (short)
- Headword and sense counts, and the verify results.
- Multi-sense and multi-candidate counts.
- Each UNRESOLVED and REVIEW decision, in one line each.
- Every new sense, with its reason.
- How many headwords took pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 senses unchanged.
- Any tool changes.
