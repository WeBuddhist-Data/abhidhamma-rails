# Brief: independent review of the Burmese Yamaka (pi-6, «အတွဲလိုက် မေးဖြေခြင်း»)

You are an independent reviewer and a careful Pāli–Burmese bilingual checker.

## Rules
- You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files. Never use /tmp or /private/tmp. Call python by that full path, never through a quoted shell variable.
- Do NOT open the Burmese termbase, senses or keyword files, the zero-shot Burmese, or any notes or scripts in 0-INBOX. Review the translation against the Pāli on its own.
- Do NOT open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`), and do no web searches.

## Inputs
- **Pāli:** `AI_translation/pali/pi-6_split_chapters/<ch>.md`.
- **Burmese:** the same filenames in `AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters/`.
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^6-8-112). Within a segment, lines align one to one.
- **Optional reference for hard readings:** the English zero-shot `AI_translation/english/pi-6-english-plain-zeroshot_split_chapters/<same file>`, if it exists. The Pāli is the authority.
- **pi-1 … pi-5 consistency:** you may read the finished Burmese in `AI_translation/burmese/pi-{1,2,3,4,5}-burmese-plain-rails_split_chapters/`. Where a pi-6 line or term has Pāli identical to pi-1 … pi-5, check that it has the same Burmese, and report differences as MAJOR consistency.
- **Audience:** `AI_translation/audience_profile/plain.md`: clear, natural, modern written Burmese, nothing added.

## About the text
The Yamaka asks its questions in pairs. Each chapter (roots, aggregates, bases, elements, truths, formations, latent tendencies, mind, dhammas, faculties) has three parts:
- **paṇṇattivāra:** padasodhana, the cakka, and the suddha questions;
- **pavattivāra:** arising / ceasing, by person (yassa), place (yattha), and person-and-place; in past, present and future, and in the anuloma / paccanīka forms;
- **pariññāvāra.**

The questions have the form «Yo / Yassa / Yattha … P, … Q?». The answers are «Āmantā.», «No.», «Natthi.», or a split answer such as «X-ānaṃ P, no ca tesaṃ Q. Y-ānaṃ P ceva Q ca.».

Everything turns on:
- **polarity in every clause:** na / no / a-; P vs na P in the paccanīka form; «no ca» in split answers;
- **who and where:** yassa = person, yattha = place, and the beings or planes named in split answers;
- **tense and aspect:** past «uppajjittha», present «uppajjati», future «uppajjissati»; the moments uppādakkhaṇa / bhaṅgakkhaṇa; uppajjamāna «ဖြစ်ပေါ်ဆဲ» vs uppanna «ဖြစ်ပေါ်ပြီးသော»; the planes and their beings;
- **slot order:** which term is P and which is Q, kept in the right slot in both halves of the pair;
- **sameness:** the same Pāli frame gets the same Burmese frame everywhere, and the same proposition gets the same Burmese wording in all its repetitions;
- **lists and numbers:** item by item;
- **shared terms:** terms shared with pi-1 … pi-5 keep their final Burmese.

## Known conventions you should NOT report as errors
- **Punctuation:**
  - «…pe…» becomes one «…».
  - Statements end with «။» and lists use «၊».
  - There is no «?»: questions end «…သလော။» / «…နည်း။».
  - Quotes “…” / ‘…’ only where the Pāli has them.
  - Digits are as the Pāli; item letters are (က) (ခ) (ဂ).
- **Title:** «အတွဲလိုက် မေးဖြေခြင်း».
- **Answers:** Āmantā «ဟုတ်ပါသည်။», No «မဟုတ်ပါ။», Natthi «မရှိပါ။». This is the polite answer register; pi-3 has «မရှိ။» in a different register, which is known.
- **Frame words:**
  - anuloma / paccanīka «အဟုတ်ပြ ပုံစံ / အငြင်းပြ ပုံစံ»;
  - cakka «လှည့်ပတ်ခြင်း»;
  - the moments «ဖြစ်ခြင်း ခဏ / ပြိုပျက်ခြင်း ခဏ»;
  - the vāra names «Xအလိုက် ဖော်ပြချက်» / «ဖြစ်ပေါ်ခြင်း»;
  - cavati «စုတေ»; upapajjati «ပြန်လည် ဖြစ်ပေါ်».
- **Relatives:**
  - yattha «အကြင်နေရာ၌»;
  - yassa (person) «အကြင်သူအား»;
  - yassa cittassa anantarā «အကြင်စိတ်၏ ချက်ချင်း နောက်၌», in all 273 places;
  - the beings of a plane «…ဘုံ၌ ရှိသူ(တို့)», and the plane «…ဘုံ».
- **Terms:**
  - kāyasaṅkhāra «ကိုယ်၏ ပြုပြင်ဖန်တီးမှု» (the in-and-out breath), vacī- / cittasaṅkhāra «နှုတ်၏ / စိတ်၏ …»;
  - anusaya «ကိန်းအောင်းခြင်း», sānusaya «ကိန်းအောင်းခြင်း ရှိသူ»;
  - nāma «စိတ်ပိုင်း»;
  - arūpa as plane «ရုပ်မရှိသော ဘုံ»;
  - rūpadhātu as element «အဆင်းအရောင် ဓာတ်», as plane «ရုပ်ဘုံ»;
  - aññindriya «အပြည့်အဝ သိမြင်ခြင်း»;
  - hetu «အကြောင်း» in the hetuvāra list;
  - sacchikaroti «မျက်မှောက်ပြု», with the spaced negative «မျက်မှောက် မပြု»;
  - proper names stay names.
- **Brackets and slips:**
  - Variant brackets «[ပါဌ်ကွဲ (…): …]»; sigla stay in Roman script.
  - Source slips are translated as written and are known. Report one only if the Burmese is wrong for the intended reading.
  - Burmese adds a head noun («သဘောတရား», «အရာ», «ပုဂ္ဂိုလ်») where the Pāli has a bare adjective. That is known: do not report it unless it changes the meaning.

## Your part
<PART>

## Check every segment for
1. **CRITICAL: meaning errors.**
   - Polarity: a negation lost or added.
   - P / Q swapped, or a person / place / tense / moment wrong.
   - An answer that contradicts the question, or a split answer with the wrong beings, planes or negation.
   - A wrong term.
   - A list item lost, added, swapped or merged; a wrong number.
   - Omitted or added content, or content on the wrong ID.
2. **MAJOR.**
   - Burmese that is ungrammatical or misleading, so a reader would likely misread it.
   - The same Pāli frame, proposition or stock passage rendered inconsistently within your part, or against identical pi-1 … pi-5 Pāli.
3. **MINOR.**
   - Awkward wording, or a heavy word where a plain one exists.
   - Pāli left in Roman script outside variant brackets and sigla.

Also check typography:
- dashes «–» / «—» only where the Pāli has them, with the same count per line;
- no «।» and no «?»;
- no double blank lines.

## How to check
1. **Check BY SCRIPT, per line:**
   - numbers and counts;
   - polarity per clause (Pāli na / no / a- vs Burmese «မ» / «မဟုတ်» / «မရှိ»);
   - the answer type (Āmantā / No / Natthi / split);
   - tense markers (past «ခဲ့», future «လိမ့်မည် / မည့်», present);
   - the yassa / yattha leads;
   - dash and quote counts;
   - that each recurring Pāli line always gets the same Burmese.

   The book is extremely formulaic, so the scripts carry most of the load.
2. **Read closely** the lines the scripts flag. Also read, spread over all your chapters:
   - every chapter opening (uddesa, padasodhana, the cakka);
   - the first full round of each pavattivāra (anuloma and paccanīka, with every tense);
   - every split answer type;
   - the pariññāvāra.

   Read the files in parts; they are large.

## Report (concise, as your final message: you cannot write files)
- **A table:** ID | file | severity | Pāli (short) | Burmese (short) | problem | suggested Burmese fix (the full corrected phrase).
  - Number your rows with your letter (A1, A2 … / B1 … / C1 …).
  - Give one row per recurring pattern, with the IDs or the count.
- **Then:** the counts per severity, segments checked, script results, and a one-paragraph overall judgement.
