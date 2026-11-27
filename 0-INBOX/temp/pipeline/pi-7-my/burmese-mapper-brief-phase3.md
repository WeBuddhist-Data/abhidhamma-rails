# Brief: pi-7 Burmese keyword mapping, PHASE 3 (whole book: consistency and assembly)

## Read first
Follow these as binding:
- The phase-1 brief `0-INBOX/temp/pipeline/pi-7-my/burmese-mapper-brief.md`: rules, sources, verify checks.
- The phase-2 brief `burmese-mapper-brief-phase2.md`, with the coordinator decisions on phase 1.

Then read the results in `pi-7-my/mapper-my/`:
- `map7_rules.py`, `map_sample.py`, `map_g1.py` … `map_g6.py`;
- `map-table.md`, `frame-coverage.md`, `map-harmonise-notes.md`;
- `notes-g1.md` … `notes-g6.md`.

## Coordinator decisions on phase 2 (2026-11-26, under the user's standing go-ahead)

**Group rules.** All group rules are approved book-wide: g1's four applications, g3 G1–G5, g4 G1–G5, g5 G5-1–G5-6 and g6 G6-1–G6-6. The S1 values all six groups kept are approved.

**Module overrides that hold beyond one segment go into `map7_rules.py`**, which is now yours to edit. Single-segment forms stay as per-segment rules in the group scripts.

**Module fixes.** Fix these in the module, then re-run every script:
1. **Word boundaries.** A value chunk must match on Burmese word boundaries, so a value can never be only the start of a longer word. This fixes ajjhattikassa «အတွင်း» → «အတွင်းပိုင်း» and cakkaṃ «စက်» → «စက်ဝိုင်း». Re-check every value the change touches.
2. **pīti.** FRAME must not split pīti into pi + iti; pīti is «ပီတိ».
3. **tadārammaṇatā.** The module misread the generator string. Use the text's phrase, one value per form the text has. This also changes the 5 uses in the sample 1-02.
4. **noupādā / Noupādā** = «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော». The positive upādā keeps its pi-1 … pi-3 value.
5. **R1 order.** The R1 base form is tried before the term family, so a «-ñca» form takes its base form's value (g6 G6-2).
6. **Negatives.** Drop the gapped negative candidate «N ဖြစ်သော … မဟုတ်» when the plain «N မဟုတ်သော» stands in the segment (g6 G6-3, g3 G1).
7. **Numbers.** The number parser knows «bīsa» (chabbīsa).
8. **One value per term.** A term's value does not depend on its case, e.g. asekkhassa = asekkho's value.
9. **Dictionary forms.** These dictionary forms hold book-wide:
   - gaṇetabbā «ရေတွက်ရမည့်»
   - vitthāretabbāni «အကျယ် ချဲ့ရမည့်»
   - uppādenti «ဖြစ်စေသည်»
   - vipassanti «ထိုးထွင်း၍ ရှုသည်»
   - bhāgo «အပိုင်း»
   - pañcaviññāṇaṃ «သိစိတ် ငါးပါး»
   - paripuṇṇo «ပြည့်စုံသော»

**Unclear points, decided:**
- **Gocchaka dyad items (g3 G1 vs T13, g5 U-g5-1):** the item term is the bare noun «N» in every case. This is the binding pi-1 Mātikā value (hetū «အမြစ်», āsavā «စိတ်အစွန်းအထင်း», saṃyojanā «နှောင်ကြိုး» …) under pi-1 rule 2. Its negative is «N မဟုတ်သော». T13's «N ဖြစ်သော» goes, book-wide.
- **The head noun «သဘောတရား» the text adds inside -sadisa / -mūla notes (g5 U-g5-2, g6 G6-6, g4 upādinnamūlake):** leave it out with a « … » gap wherever the second chunk does not start with a particle. Keep it inside the value only where a gap is impossible. Use one rule everywhere and log the exceptions.
- **The -sadisa note shapes:** «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း» each takes its own segment's form. They are text items for the rails step, not mapping errors.
- **nevadassanena (g2 / g5 / g6):** one form book-wide, the one the text has in most segments. Log the others for the rails step.
- **naviññeyyo «မသိနိုင်သော»:** the text's own negative stays, as a lexical negative and not the na-X rule.
- **Locative absolutes** keep the attributive without «အခါ» (gaṇite «ရေတွက်သော»).
- **ṭhitena «တည်၍»** and **gambhīrā «နက်နဲ»**.
- **Act compounds** keep U2: the whole verb phrase, with karoti / katvā as (no direct equivalent). gāmaghātaṃ before «…pe…» stays the bare «ရွာ».
- **natthi:** «မရှိ» where «မရှိသည်» stands only inside a longer term (g4 G3). Otherwise use the module value.
- **g2 decisions:**
  - sekkha / asekkha as a qualifier take «…၏», following the binding pi-1 / pi-2 value; person nouns stay bare.
  - kāraṇena = «နည်းလမ်း».
  - uposathakammaṃ = «ဥပုသ် စောင့်ထိန်းခြင်း» where the text has the phrase.
  - G2-3 follows the head-noun gap rule above.
  - gahite = «ယူသော», as a locative absolute.
  - dassitanayena keeps «အတိုင်း» where the text has it.
- **For any other open point,** apply this principle: the value is the keyword's own meaning, in dictionary form, present in the segment as a phrase, with no plural or case particle and no translator's addition.

**Text inconsistencies stay for the rails step.** Do not change the translation. This covers the 1-01 vs 1-03 … 1-05 drift in ṭhānāṭhānakosalla, suciṇṇāni and tadārammaṇatā, and pavatti vs pi-6, along with the rest.

## Tasks
1. **Module consolidation.** Move the agreed overrides into `map7_rules.py` and apply the module fixes. Then re-run `map_sample.py` and `map_g1.py` … `map_g6.py`, removing from the group scripts whatever the module now does.
   - List every value change against the current `.mapped.md` files in `mapper-my/phase3-changes.tsv`: segment, keyword, old, new, reason.
   - No change may be unexplained.
2. **S1 review.** List every stem-fallback value left in all 75 chapters. Re-check only the values that changed, and record the counts.
3. **Book-wide consistency scan** over all 75 `*.mapped.md`. Model it on `pi-6-my/mapper-my/work/` scan scripts or `pi-5-my/mapper-my/`.
   - Every keyword with more than one value is either aligned (state the rule) or kept as a genuine sense / grammar / text difference (state why).
   - Write the result into `mapper-my/map-harmonise-notes.md` §B, scan before / after.
   - Merge the text inconsistencies of notes-g1 … g6 and the phase-1 §A into §A: one numbered list, duplicates joined, for the rails step.
4. **Verify all 75 files** with the three checks: preservation `bad []`; presence 0 unexplained; no «, » / «၊» / « / » in values. A second run of all seven scripts must give byte-identical files.
5. **Assemble.** Run:
   ```
   /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/mapper_chunks.py assemble AI_translation/pali/pi-7-keywords-by-reference-pali-plain.md 0-INBOX/temp/pipeline/pi-7-my/mapper-my AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md
   ```
   Every ID must appear once, with unchanged keyword counts.

## Rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails.
- Write only inside `0-INBOX/temp/pipeline/pi-7-my/mapper-my/` (helpers in `mapper-my/work/`) and the one assembled output file above.
- Never use /tmp or /private/tmp, and never `cd /tmp`.
- Never commit.
- Never open `0-INBOX/temp/language-priority/` or any existing Burmese translation, nissaya or web source.
- Never edit pi-1-my … pi-6-my or the pi-7 zero-shot text.
- Never use the words for a planted starting value or its negative.
- Do not stop for approval.
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`, called by its full path. Run long scripts in the background.

## Final report (short, numbers first)
1. Values changed by tasks 1 and 2, counted by reason.
2. S1 kept / corrected.
3. The scan before / after, with the differences kept.
4. Verify results for all 75 files and the byte-identical re-run.
5. The assembly result (IDs, keyword counts).
6. The merged text-inconsistency list (count).
7. Unclear mappings left.
