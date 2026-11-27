# Brief: termbase-builder, Pāli→Burmese plain (pi-1, Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Call Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (the system python3 is too old). Write helper scripts to files. Write ONLY inside `0-INBOX/temp/pipeline/pi-1-my/termbase/` (plus the two files the assembler writes). Never use the system temp directory. Don't commit. Never use the words for a planted starting value or its negative. The termbase is built only from this book's own evidence: no existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/burmese-religious-affairs/`).

## Read first
- `AI_translation/skills/termbase-builder.md`. Follow it.
- `AI_translation/audience_profile/plain.md`: understanding comes first.
- `0-INBOX/temp/pipeline/burmese-style.md`: the user-approved core terms and the «Lessons from earlier tracks» are binding.
- This book's choices: `pi-1-my/my-zeroshot-terms.md` (approved sample + 2-01 model), `pi-1-my/harmonise-notes.md` and `harmonise-table.tsv` (the consistency pass: one form per item, binding), `pi-1-my/mapper-my/map-harmonise-notes.md` (kept sense differences).
- Method model: the approved Marathi pi-1 termbase run, `0-INBOX/temp/pipeline/pi-1-mr/marathi-termbase-brief.md` and its tools in `pi-1-mr/termbase/` (family_scan.py, synonym_check.py, show.py …). Copy and adapt the tools into `pi-1-my/termbase/` (Burmese file paths; Myanmar script; the Burmese particles in place of the Marathi endings). Never copy Marathi terms.

## Input and output
- Input: `AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md` (2485 headwords, 2520 senses; 67 senses have more than one candidate).
- Decisions: `pi-1-my/termbase/decisions-A.tsv`, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based in the senses file's order).
- Assembler: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/termbase_assemble.py 1 burmese my plain`. It keeps single-candidate senses, requires one decision for every multi-candidate sense, allows re-aligning a single-candidate sense (ALIGNED), lists terms outside the candidates (OUTSIDE), writes `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md` and `pi-1-my/termbase/termbase-decisions.md`, and fails on any error.
- Family scan: write before / after outputs to `family-scan-before.txt` / `family-scan-after.txt`.
- Helper: `pi-1-my/senses/ids.py <headword>` (every Burmese value with its segment ids); `pi-1-my/senses/seg_my.py <id>` (Pāli and Burmese of a segment).

## How to choose
1. **Multi-candidate senses:** the one term a plain Burmese reader understands best: (a) the approved core term (burmese-style.md, my-zeroshot-terms.md, harmonise decisions); (b) the form the translation uses most; (c) the clearest plain candidate. Dictionary form as in the mapping rules (no final case particle or plural marker; attributive «…သော» for adjectives).
2. **Synonym lists:** each Pāli synonym of a definition list keeps its own Burmese word; never pick a term another synonym of the same list already uses (check the definition lines). Never a value that joins readings with « / ».
3. **Family consistency:** all inflections and compounds of one Pāli lemma in the same sense get the same Burmese word (factor names, triad / dyad terms, sense bases, elements). Keep the genuine sense differences recorded in the senses file (rūpa ×3, kāya ×2, bahiddhā ×3, dukkha ×3, maggaṃ, Chanda, cetasika, phala, hetū, sineho …).
4. **Keep contrasted pairs distinct:** vicikicchā / kaṅkhā, mettā / abyāpāda, kukkucca / uddhacca, vīriya / padhāna-vāyāma, thina / middha, hiri / ottappa, lobha / rāga / abhijjhā, samatha / samādhi / ekaggatā, paññā / ñāṇa / vijjā, sukha (pleasure) / sukha (easy).
5. **Term form:** no ", ", " / ", "; " or «၊» inside a term. Never a dash.
6. **Outside terms** only when every candidate is wrong for a plain reader; give the reason. These go to the user for approval.
7. Known open points to decide and explain: paṭicca (အကြောင်းတို့ကို မှီ၍ vs အကြောင်းအကျိုး ဆက်စပ်); ākāsa (ဟင်းလင်းပြင် vs ကောင်းကင်, by sense); sukhā (သာယာသော vs ချိုသော); para (သူတစ်ပါး vs ပရ); the translation-level differences noted in `pi-1-my/agents.txt` (Suññata / Appaṇihita headings, kusala-hetu «ကုသိုလ် အမြစ်» vs «ကုသိုလ်၏ အမြစ်», kilesavatthu): choose ONE term so the rails translation becomes consistent.

## Verify
The assembler prints "no errors". The family scan (after) lists no lemma family with more than one Burmese word for the same sense, unless explained.

## Report (short, plain, numbers first)
The assembler's summary line; the number of family re-alignments; the outside choices with reasons; the 15 most consequential choices (with the alternative rejected); anything unsure that a Burmese speaker should check.
