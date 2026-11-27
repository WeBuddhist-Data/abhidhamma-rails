# Brief: independent review of the Burmese Dhammasaṅgaṇī (pi-1, «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»)

You are an independent reviewer and a careful Pāli–Burmese bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files.
- Do NOT open the Burmese termbase, senses or keyword files, the zero-shot Burmese, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.
- Do NOT open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`), and do no web searches.

## Inputs
- **Pāli:** `AI_translation/pali/pi-1_split_chapters/<ch>.md`
- **Burmese:** the same filenames in `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/`
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^1-112); lines align one to one within a segment.
- **Optional reference** for hard readings: the English zero-shot `AI_translation/english/pi-1-english-plain-zeroshot_split_chapters/<same file>`. The Pāli is the authority.
- **Audience:** `AI_translation/audience_profile/plain.md`: clear, natural, modern written Burmese, nothing added.

## About the text
The Dhammasaṅgaṇī opens with the mātikā (22 triads, 100 dyads, 42 suttanta dyads), then defines states. The citta chapter asks «Katame dhammā kusalā? Yasmiṃ samaye … cittaṃ uppannaṃ hoti …, tasmiṃ samaye phasso hoti, vedanā hoti …» and defines each factor with a synonym list («Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – ayaṃ tasmiṃ samaye phasso hoti.»). Then the other cittas, matter (rūpa), the nikkhepa summary and the commentary chapter. Everything turns on:
- the synonym lists: each Pāli item its own Burmese, order and count kept, no item lost, added or merged; the same Pāli synonym the same Burmese everywhere;
- the factor names and the citta qualifiers (sahagata / sampayutta / sasaṅkhārika, objects, jhāna factors);
- polarity (a-/an-/na-/no- terms, na hoti), numbers, «ṭhapetvā» exceptions, included / not included, the mātikā terms.

## Known conventions you should NOT report as errors
- «…pe…» / «…Pe…» become one «…». Statements end with «။», lists use «၊», no «?». Quotes “…” / ‘…’. Digits as the Pāli; item letters (က) (ခ) (ဂ).
- Definition frame: «ထိုအချိန်၌ ရှိသော X ဟူသည် အဘယ်နည်း။ ထိုအချိန်၌ A၊ B၊ C ရှိသမျှ – ဤသည်မှာ ထိုအချိန်၌ ရှိသော X ဖြစ်သည်။».
- dhamma = သဘောတရား; kusala / akusala = ကုသိုလ် / အကုသိုလ်; abyākata = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော; uppanna = ဖြစ်ပေါ်ပြီးသော, samuppanna = ဖြစ်ပေါ်လာသော; phassa တွေ့ထိမှု, vedanā ခံစားမှု, saññā မှတ်သိမှု, cetanā စေ့ဆော်မှု, citta စိတ်, vitakka / vicāra စတင်ကြံစည်မှု / ဆက်လက်သုံးသပ်မှု; kāya- in kāyapassaddhi … = စိတ်၏ အဖော်တို့ (the mental body); -indriya X၏ စွမ်းရည်; ākāsa ဟင်းလင်းပြင်; paṭiccasamuppāda အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ; nāma-rūpa စိတ်ပိုင်း / ရုပ်ပိုင်း; proper names (Paranimmitavasavattī …) stay names.
- Variant brackets «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]». Source slips are translated as written and are known; report one only if the Burmese is wrong for the intended reading.

## Check every segment for
**1. CRITICAL: meaning errors**: polarity (a negation lost or added), a wrong factor / term, a synonym list item lost, added, swapped or merged, a wrong number, omitted or added content, content on the wrong ID.
**2. MAJOR**: Burmese that is ungrammatical or misleading so a reader would likely misread it; the same Pāli formula or synonym rendered inconsistently within your part.
**3. MINOR**: awkward wording, a heavy word where a plain one exists, Pāli left in Roman script outside variant brackets.
**Also typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।», no «?»; no double blank lines.

## How to check
Check BY SCRIPT, per line: numbers (Pāli number words vs Burmese number words), dash counts, the synonym count per definition line (Pāli items vs Burmese items split on «၊»), polarity (Pāli negations vs Burmese «မ» / «မဟုတ်» / «မရှိ»), and that each recurring Pāli synonym always gets the same Burmese. Use the results to find lines to read closely; then read closely every chapter opening, every definition list and every flagged line, spread over all your chapters.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Burmese (short) | problem | suggested Burmese fix (the full corrected phrase).
- One row per recurring pattern, with the IDs or the count.
- Then the counts per severity, segments checked, script results, and a one-paragraph overall judgement.
