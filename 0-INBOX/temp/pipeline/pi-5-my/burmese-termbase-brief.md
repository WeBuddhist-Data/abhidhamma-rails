# Brief: termbase-builder, Pāli→Burmese plain (pi-5, Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Call Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Write helper scripts to files. Write ONLY inside `0-INBOX/temp/pipeline/pi-5-my/termbase/` (plus the two files the assembler writes). Never use the system temp directory (not /tmp, not /private/tmp, no `cd /tmp`). Don't commit. Never use the words for a planted starting value or its negative. The termbase is built only from this book's own evidence and the locked pi-1 … pi-4 termbases: no existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`).

## Read first
- `AI_translation/skills/termbase-builder.md`. Follow it.
- `AI_translation/audience_profile/plain.md`: understanding comes first.
- `0-INBOX/temp/pipeline/burmese-style.md`: the user-approved core terms, the «Lessons from earlier tracks» and the pi-1 … pi-4 termbase sections are binding.
- **The LOCKED pi-4, pi-3, pi-2 and pi-1 termbases are binding:** `AI_translation/burmese/pi-{4,3,2,1}-pali-burmese-termbase-plain.md` with `0-INBOX/temp/pipeline/pi-{4,3,2,1}-my/termbase/APPROVED.md` (incl. their change notes: pi-4 narassa «မြို့», sāci «ကွေ့ဝိုက်သော»; pi-3 buddho «နားလည်ပြီးသော»; pi-2 maccu «သေဆုံးခြင်း», siṅga, sevanā path sense; pi-1 bahiddhā, proper names stay names, nāma-rūpa «စိတ်ပိုင်း / ရုပ်ပိုင်း»). Same Pāli headword in the same sense = pi-4's term (else pi-3's, else pi-2's, else pi-1's), unless that term never occurs in the pi-5 text: then keep the pi-5 form and report it, or align it (ALIGNED / OUTSIDE) when the locked term is a review change (decide and explain). tathāgata / bhagavā «မြတ်စွာဘုရား».
- This book's choices: `pi-5-my/my5-zeroshot-terms.md` and `pi-5-my/notes-sample.md` (approved sample: Āmantā «ဟုတ်ပါသည်», Na hevaṃ vattabbe «ဤသို့ မဆိုသင့်ပါ», kathā «ဆွေးနွေးချက်», vagga «ဝဂ်», sakavādī / paravādī «မိမိဘက် / တစ်ဖက်သား», saccikaṭṭhaparamatthena «အမှန်တကယ် အဆုံးစွန် အနက်အားဖြင့်»), `pi-5-my/harmonise-notes.md` (book-wide forms), `pi-5-my/mapper-my/map-table.md` (Q1–Q8), `notes-ch2-15.md`, `notes-ch16-31.md`, `map-harmonise-notes.md` (§A: 32 text inconsistencies for the rails step; §B kept sense differences, `scan-after-kept.tsv`), `pi-5-my/senses/` (gen_decisions_my.py NEW_SENSE: 76 new senses, and the logged reasons).
- Method model: the approved pi-4 run `pi-4-my/burmese-termbase-brief.md` and its tools in `pi-4-my/termbase/` (family_scan.py, synonym_check.py, show.py, hwinfo.py, pi123_match.py, newcheck.py …). Copy and adapt them into `pi-5-my/termbase/` (pi-5 paths; match against pi-4, pi-3, pi-2 and pi-1). Never edit anything in `pi-1-my/` … `pi-4-my/`.

## Input and output
- Input: `AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md` (5418 headwords, 5553 senses; 370 senses have more than one candidate).
- Decisions: `pi-5-my/termbase/decisions-A.tsv`, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based in the senses file's order). Group them in commented parts (multi-candidate, family alignment, locked-term alignment, text inconsistencies).
- Assembler: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/termbase_assemble.py 5 burmese my plain`. It keeps single-candidate senses, requires one decision for every multi-candidate sense, allows re-aligning a single-candidate sense (ALIGNED), lists terms outside the candidates (OUTSIDE), writes `AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md` and `pi-5-my/termbase/termbase-decisions.md`, and fails on any error.
- Family scan: before / after outputs to `family-scan-before.txt` / `family-scan-after.txt`.
- Helpers: `pi-5-my/senses/ids.py <headword>`, `pi-5-my/senses/ctx.py`.

## How to choose
1. **Multi-candidate senses:** the one term a plain Burmese reader understands best: (a) the locked pi-4 / pi-3 / pi-2 / pi-1 term; (b) the approved core term (burmese-style.md, my5-zeroshot-terms.md, the harmonise decisions); (c) the form the translation uses most; (d) the clearest plain candidate. Dictionary form as in the mapping rules.
2. **Family consistency:** all inflections and compounds of one Pāli lemma in the same sense get the same Burmese word (the dialectic frame words, the doctrinal terms of each kathā, the path / fruit terms, the sutta stock lists). Keep the genuine sense differences in the senses file (the new senses and the kept splits).
3. **Keep contrasted pairs distinct** (burmese-style.md lessons; e.g. sekha «ကျင့်ကြံဆဲသူ» vs paṭipannaka «ကျင့်ကြံသူ», bandhana vs saṃyojana, nikati vs sāci).
4. **Term form:** no ", ", " / ", "; " or «၊» inside a term. Never a dash.
5. **Outside terms** only when every candidate is wrong for a plain reader, or to follow a locked earlier-book review change; give the reason.
6. Choose ONE term for each text inconsistency in `mapper-my/map-harmonise-notes.md` §A where a term decides it (e.g. nicca vs dhuva, taṇhā «တပ်မက်မှု» vs «တဏှာ», dhammacakka, ruhiruppādaka, parinibbuta, thera «မထေရ်» vs «ထေရ်», iṭṭha, parinipphanna, upacaya, sukhadukkha, nirodhadhamma), so the rails translation becomes consistent; list the items a term cannot decide (spelling, missing text, word order) for the rails step.

## Verify
The assembler prints "no errors". The family scan (after) lists no lemma family with more than one Burmese word for the same sense, unless explained.

## Report (short, plain, numbers first)
The assembler's summary line; how many senses took pi-4's / pi-3's / pi-2's / pi-1's term; family re-alignments; the outside choices with reasons; the most consequential choices (with the alternative rejected); senses that depart from pi-1 … pi-4 and why; the §A items decided / left for rails; anything a Burmese speaker should check. The coordinator reviews and locks it under the user's standing go-ahead; do not call it locked yourself.
