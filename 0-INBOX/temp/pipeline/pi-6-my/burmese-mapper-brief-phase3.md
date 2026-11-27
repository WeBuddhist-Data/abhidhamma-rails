# Brief: pi-6 Burmese keyword mapping, PHASE 3 (whole book: consistency and assembly)

Read these first and follow them as binding:
- the phase-1 brief `0-INBOX/temp/pipeline/pi-6-my/burmese-mapper-brief.md` (rules, sources, verify checks);
- the phase-2 brief `burmese-mapper-brief-phase2.md` (with the coordinator's decisions on phase 1).

Then read the results in `pi-6-my/mapper-my/`:
- `map6_rules.py`, `map_sample.py`, `map_g1.py`, `map_g2.py`, `map_g3.py`;
- `map-table.md`, `frame-coverage.md`, `map-harmonise-notes.md`;
- `notes-g1.md`, `notes-g2.md`, `notes-g3.md`.

## Coordinator decisions on phase 2 (2026-11-22, under the user's standing go-ahead)
- **Approved book-wide:** the group rules G1–G11 (g1), V1–V7 (g2) and g3's new rules. The stem fallback (S1) is approved only after the review in task 2. g3's own unclear points are open for you to settle by the same principles below; log each one.
- **Module overrides go into `map6_rules.py`**, which is now yours to edit: f_rupam_g1, the g1 table `T_ALL` and the functions `FUNCS_G1` (f_aka, f_saka, f_citta, f_nayatana), O1–O9 of g2, and any g3 override that holds beyond one segment. Single-segment forms stay as per-segment rules in the group scripts. Fix these mechanics in the module:
  1. The `literal` tier of `pi_get` must require `phrase_ok`: the value's words must stand together in the segment, not scattered (g2 O1, kāyasaṅkhāro).
  2. `base_forms` must not read a finite «-anti» as «-aṃ + ti» (g1 override 4, parijānanti).
  3. The R5 `shared_being` regex must stay inside one clause (g2 O2, ^6-6-47).
  4. -amāno (masculine nominative) is a person «…ဆဲသူ» where the text has «…ဆဲသူ» (g2 O3).
  5. Add the ending rule «Xပြီး မဟုတ်» (perfect predicate negated), so that uppannaṃ is «ဖြစ်ပေါ်ပြီးသော» in every segment (g2 U4).
- **Unclear points, decided:**
  - g1 U1 nāyatanā: the gapped value «အာရုံခံ နယ်ပယ် … မဟုတ်သော» (rule 1, no plural marker in a value).
  - g1 U2 sa-X-ka persons: «X ရှိသော / X မရှိသော», the dictionary form; it is present by the ending rule.
  - g1 U3 and g2 O6: Yattha «အကြင်နေရာ», and Yassa yattha «အကြင်သူအား အကြင်နေရာ».
  - g1 U4: the slip uppajjittharūpāyatanañca is mapped as g1 chose. It is also a rails text item.
  - g2 U1: sānusayo / niranusayo «ကိန်းအောင်းခြင်း ရှိသူ / မရှိသူ» (the whole meaning of the word).
  - g2 U2: the cited sections are without quotation marks.
  - g2 U3 saraṇaaraṇā: keep «အတွဲ» only where the Pāli keyword itself names the pair (-duka). Otherwise use «ပဋိပက္ခ ရှိသော ပဋိပက္ခ မရှိသော».
  - g2 U5: Aṭṭhamako «အဋ္ဌမ», as pi-5 (binding).
  - g2 U6: tesaṃyeva «ထိုသူ» (R1, rule 1). The text's «ထိုသူတို့၏ပင်» stays in the text.
  - g2 U7: vattamāne «ဖြစ်နေသော» and bhaṅgā «ပြိုပျက်သော», the dictionary forms, present by the ending rule.
  - g3 (rules W1–W7 approved; its overrides O1–O7 go into the module where they hold beyond one segment):
    - U1: anaññātaññassāmīti without «အရာ», since that is the text's added head noun (T4).
    - U2: kusalānaṃ uppādakkhaṇe keeps the module value, without «သဘောတရား» (T3).
    - U3: the gapped value of Abyākatañca dhamme is approved (like g1 U1).
    - U4: add a verifier ending so that a joined compound verb also matches its spaced negative («မျက်မှောက်ပြု» / «မျက်မှောက် မပြု»). sacchikar- then takes the joined «မျက်မှောက်ပြု…» everywhere, and W6 goes. The spacing itself is rails item T2.
    - U5–U7: as g2 U5, U7 and g1 U2.
    - U8: Yamakapakaraṇaṃ «အတွဲလိုက် မေးဖြေခြင်း ကျမ်း» («ကျမ်း» is pakaraṇa; as pi-2).
  - The general principle for any other open point: the value is the keyword's own meaning, in dictionary form, present in the segment as a phrase. It carries no plural or case particle and no translator's addition.
- **Text inconsistencies stay for the rails step.** Do not change the translation.

## Tasks
1. **Module consolidation.** Move the agreed overrides into `map6_rules.py` and fix the five mechanics. Then re-run `map_sample.py`, `map_g1.py`, `map_g2.py` and `map_g3.py` in that order, removing from the group scripts whatever the module now does. List every value change against the current `.mapped.md` files, with its reason, in `mapper-my/phase3-changes.tsv` (segment, keyword, old, new, reason). No change may be unexplained.
2. **S1 review.** List every stem-fallback value left in all 44 chapters. Check each against the segment's Burmese and the keyword's sense. Correct the wrong ones by rule, and record the counts kept / corrected in the notes. g1 and g2 already reviewed theirs; re-check only values that changed.
3. **Book-wide consistency scan** over all 44 `*.mapped.md` files (model `pi-5-my/mapper-my/` scan script, or `pi-4-my/mapper-my/map_scan.py`). Every keyword with more than one value is either aligned (state the rule) or kept as a real sense, grammar or text difference (state why). Write the result into `mapper-my/map-harmonise-notes.md` (§B, scan before / after). Merge the text inconsistencies of notes-g1, notes-g2 and notes-g3 and the harmonise A-items into §A: one numbered list, duplicates joined, for the rails step.
4. **Verify all 44 files** with the three checks: preservation `bad []`; presence 0 unexplained; no «, » / «၊» / « / » in values. A second run of the four scripts must give byte-identical files.
5. **Assemble:**
   ```
   /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/mapper_chunks.py assemble AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md 0-INBOX/temp/pipeline/pi-6-my/mapper-my AI_translation/burmese/pi-6-keywords-by-reference-pali-burmese-plain.md
   ```
   Every ID must appear once, with unchanged keyword counts.

## Rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails.
- Write only inside `0-INBOX/temp/pipeline/pi-6-my/mapper-my/` (helpers in `mapper-my/work/`) and the one assembled output file above.
- Never use /tmp or /private/tmp, and never `cd /tmp`.
- Never commit.
- Never open `0-INBOX/temp/language-priority/` or any existing Burmese translation, nissaya or web source.
- Never edit pi-1-my … pi-5-my or the pi-6 zero-shot text.
- Never use the words for a planted starting value or its negative.
- Do not stop for approval.
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. In zsh a glob with no match fails, so list files with python.

## Final report (short, numbers first)
1. Values changed by tasks 1 and 2, counted by reason.
2. S1 kept / corrected.
3. The scan before / after, with the differences kept.
4. Verify results for all 44 files and the byte-identical re-run.
5. The assembly result (IDs, keyword counts).
6. The merged text-inconsistency list (count).
7. Unclear mappings left, and how you settled g3's.
