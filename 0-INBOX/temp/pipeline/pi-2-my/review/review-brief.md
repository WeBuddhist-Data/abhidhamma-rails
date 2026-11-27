# Brief: independent review of the Burmese Vibhaṅga (pi-2, «ခွဲခြမ်းစိတ်ဖြာခြင်း»)

You are an independent reviewer and a careful Pāli–Burmese bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files.
- Do NOT open the Burmese termbase, senses or keyword files, the zero-shot Burmese, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.
- Do NOT open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`), and do no web searches.

## Inputs
- **Pāli:** `AI_translation/pali/pi-2_split_chapters/<ch>.md`
- **Burmese:** the same filenames in `AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters/`
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^2-112); lines align one to one within a segment.
- **Optional reference** for hard readings: the English zero-shot `AI_translation/english/pi-2-english-plain-zeroshot_split_chapters/<same file>`. The Pāli is the authority.
- **Pi-1 consistency:** the finished Burmese Dhammasaṅgaṇī `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/` may be read to check that a pi-2 line whose Pāli is identical to a pi-1 line has the same Burmese (report differences as MAJOR consistency).
- **Audience:** `AI_translation/audience_profile/plain.md`: clear, natural, modern written Burmese, nothing added.

## About the text
The Vibhaṅga has 18 chapters (khandha, āyatana, dhātu, sacca, indriya, paṭiccasamuppāda, satipaṭṭhāna, sammappadhāna, iddhipāda, bojjhaṅga, magga, jhāna, appamaññā, sikkhāpada, paṭisambhidā, ñāṇa, khuddakavatthu, dhammahadaya). Most chapters have three parts: suttantabhājanīya (the sutta exposition), abhidhammabhājanīya (the abhidhamma exposition, reusing the Dhammasaṅgaṇī citta and factor formulas) and pañhāpucchaka (the mātikā triads and dyads asked of each item). Everything turns on:
- the synonym lists: each Pāli item its own Burmese, order and count kept, no item lost, added or merged; the same Pāli synonym the same Burmese everywhere;
- the eleven qualifiers of the khandha chapter (atīta … santike), the aggregates, bases, elements, truths, faculties, the twelve links (paccayā chains), the factor names and the citta qualifiers;
- polarity (a-/an-/na-/no- terms, na hoti), numbers, «ṭhapetvā» exceptions, included / not included (saṅgahita / asaṅgahita), the mātikā terms in the pañhāpucchaka;
- the lists in khuddakavatthu (ch17, the long lists of defilements: mada, pamāda, thambha …) and the dhammahadaya tables (ch18, planes, beings, lifespans, numbers).

## Known conventions you should NOT report as errors
- «…pe…» / «…Pe…» become one «…». Statements end with «။», lists use «၊», no «?». Quotes “…” / ‘…’. Digits as the Pāli; item letters (က) (ခ) (ဂ).
- Definition frame: «ထိုအချိန်၌ ရှိသော X ဟူသည် အဘယ်နည်း။ ထိုအချိန်၌ A၊ B၊ C ရှိသမျှ – ဤသည်မှာ ထိုအချိန်၌ ရှိသော X ဖြစ်သည်။».
- Headings: Suttantabhājanīyaṃ «သုတ္တန်အလိုက် ခွဲခြမ်း ဖော်ပြချက်», Abhidhammabhājanīyaṃ «အဘိဓမ္မာအလိုက် ခွဲခြမ်း ဖော်ပြချက်», Pañhāpucchakaṃ «မေးခွန်းများဖြင့် ဖော်ပြချက်»; X-vibhaṅgo «X ကို ခွဲခြမ်းစိတ်ဖြာခြင်း»; khandha = အစုအဝေး.
- dhamma = သဘောတရား; kusala / akusala = ကုသိုလ် / အကုသိုလ်; abyākata = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော; uppanna = ဖြစ်ပေါ်ပြီးသော, samuppanna = ဖြစ်ပေါ်လာသော; ajjhatta «မိမိ၌ ရှိသော», bahiddhā «မိမိ၏ ပြင်ပ၌ ရှိသော» (other bahiddhā senses: «ပြင်ပ၌», «အပြင်ဘက်»); phassa တွေ့ထိမှု, vedanā ခံစားမှု, saññā မှတ်သိမှု, saṅkhārā ပြုပြင်ဖန်တီးမှုများ, viññāṇa သိစိတ်, cetanā စေ့ဆော်မှု, vitakka / vicāra စတင်ကြံစည်မှု / ဆက်လက်သုံးသပ်မှု; -indriya X၏ စွမ်းရည်; ākāsa ဟင်းလင်းပြင်; paṭiccasamuppāda အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ; nāma-rūpa စိတ်ပိုင်း / ရုပ်ပိုင်း; dhātu as plane «ဘုံ» vs element «ဓာတ်»; proper names stay names.
- Variant brackets «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]». Source slips are translated as written and are known; report one only if the Burmese is wrong for the intended reading.

## Check every segment for
**1. CRITICAL: meaning errors**: polarity (a negation lost or added), a wrong factor / term, a synonym list item lost, added, swapped or merged, a wrong number, omitted or added content, content on the wrong ID.
**2. MAJOR**: Burmese that is ungrammatical or misleading so a reader would likely misread it; the same Pāli formula or synonym rendered inconsistently within your part (or against identical pi-1 Pāli).
**3. MINOR**: awkward wording, a heavy word where a plain one exists, Pāli left in Roman script outside variant brackets.
**Also typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।», no «?»; no double blank lines.

## How to check
Check BY SCRIPT, per line: numbers (Pāli number words / digits vs Burmese number words / digits), dash counts, the synonym count per definition line (Pāli items vs Burmese items split on «၊»), polarity (Pāli negations vs Burmese «မ» / «မဟုတ်» / «မရှိ»), and that each recurring Pāli synonym and each recurring Pāli line always gets the same Burmese. Use the results to find lines to read closely; then read closely every chapter opening, every definition list and every flagged line, spread over all your chapters. The files are large: read them in parts, focus close reading on distinct (non-repeated) lines.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Burmese (short) | problem | suggested Burmese fix (the full corrected phrase). Number your rows with your letter (A1, A2 … or B1, B2 …).
- One row per recurring pattern, with the IDs or the count.
- Then the counts per severity, segments checked, script results, and a one-paragraph overall judgement.
