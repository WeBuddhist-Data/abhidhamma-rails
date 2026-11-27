# Brief: consistency pass over the pi-1 Burmese keyword mapping, then assemble

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails (macOS, zsh). Python: `python3 -I -X utf8` for scripts without PIL. Scratch only in `0-INBOX/temp/pipeline/pi-1-my/mapper-my/`. Never commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (do NOT open `0-INBOX/temp/language-priority/burmese-religious-affairs/`). Back up every script you edit into `mapper-my/harmonise-backup/` and snapshot all `*.mapped.md` there first.

Seven scripts mapped the 14 chapters in parallel: `map_all.py` (preamble, 1-matika: the user-approved sample), `map_2-01.py`, `map_2-02-03.py`, `map_2-04-05.py`, `map_3.py`, `map_4.py`, `map_5.py`, each with `map-table*.md`. Rules: `burmese-mapper-brief.md` (incl. «Approved sample»), `map-table.md` rules 1–11 (approved) and each agent's rules 12+.

## Decisions (apply them; changes only through the scripts, then re-run them)
1. **Absolutives keep «…၍»** (ṭhapetvā = ချန်ထား၍, paṭicca in «X paṭicca» = အကြောင်းတို့ကို မှီ၍, ārabbha = အာရုံပြု၍, upādāya / nissāya = မှီ၍, upasampajja = ဝင်စား၍ …): the majority (2-01, 2-02/03, 2-04/05, 5). Approved rule 4 (verb + «သည်») applies to finite verbs only. Fix map_4.py (and any other outlier). paṭicca in paṭiccasamuppāda keeps the Mātikā value.
2. **«samaye X» = «အချိန်၌ ရှိသော X»** everywhere (2-01 rule 13).
3. **One sense per segment for rūpa:** no «ရုပ် / အဆင်းအရောင်» or «သိမ်မွေ့သော ရုပ် / ရုပ်» alternatives. Choose by the compound the keyword comes from in that segment (rūpāyatana / rūpadhātu / rūpārammaṇa / X-viññeyya rūpa as object seen = အဆင်းအရောင်; rūpāvacara = သိမ်မွေ့သော ရုပ်; matter = ရုပ်). Where one keyword string really covers both senses in one segment, pick the sense of its FIRST occurrence in the Pāli segment and log it.
4. **Headings:** a heading keyword takes the Burmese of that heading in the text (e.g. Suññata). If the text's headings differ between chapters for the same Pāli, report it (do not edit the translation).
5. **Same keyword, same kind of segment, same value** book-wide: run a scan (all `*.mapped.md`) listing every keyword with more than one value and the chapters; for each, either align it (state the rule) or keep it as a genuine sense / grammar difference (state why). Keep the sample values for Mātikā items.
6. Leave «(no direct equivalent)» for Yo / Yā / Yaṃ and caya as they are (consistent decision).

## Verify (all must pass)
- For each of the 14 chapters: the keyword-preservation one-liner in `burmese-mapper-brief.md` prints `bad []`; the script's presence verifier reports 0 failures; no ", " or «၊» in any value.
- The scan in 5 shows only logged, justified differences.
- Assemble: move any `*sample*` files out of `mapper-my/` first if present, then
  `python3 -I -X utf8 0-INBOX/temp/pipeline/mapper_chunks.py assemble AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md 0-INBOX/temp/pipeline/pi-1-my/mapper-my AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md`
  It must report every ID once and unchanged keyword counts (1916 lines).

## Log and report
`mapper-my/map-harmonise-notes.md`: each decision applied, scripts changed, values changed (count per chapter), the scan before/after, every kept difference with its reason. Final report short, numbers first.
