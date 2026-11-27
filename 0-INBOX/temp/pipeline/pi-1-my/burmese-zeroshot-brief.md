# Brief: Burmese zero-shot, remaining chapters (pi-1, Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and call Python as `python3 -I -X utf8`. Write helper scripts to files rather than inline `-c` with regexes. Write ONLY your own chapter files, plus your generator, check and notes named after your chapters, inside `0-INBOX/temp/pipeline/pi-1-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative; say "sample" or "model".

You may be paused for usage limits and resumed later: write your generator chapter by chapter, run it and save each chapter file as soon as it passes, and keep your notes file current.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`: the binding rules, the SOURCE RULE (Pāli only; never look up, download or copy any existing Burmese translation or nissaya; no web searches), typography, the dash rule, the approved core terms.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- The approved model (READ-ONLY unless your prompt says otherwise):
  - `pi-1-my/my_formulas.py`: the shared module. Import it (`sys.path.insert(0, <that folder>)`); add your frames in memory in YOUR script. Do not edit it; log every new string in your notes.
  - `pi-1-my/make_sample.py` (copy functions, don't import: it writes files when run), `check_sample.py` (adapt it as `check_<your chapters>.py`), `my-zeroshot-terms.md` (copy its strings verbatim), `notes-sample.md` (the reasons).
  - The model output `AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/` (preamble, 1-matika and, once written, 2-01).
- Cross-check of MEANING only (translate FROM THE PĀLI, never copy wording): the English zero-shot `AI_translation/english/pi-1-english-plain-zeroshot_split_chapters/<same file>`, the Marathi final `AI_translation/marathi/pi-1-marathi-plain-rails_split_chapters/<same file>` and the Marathi termbase `AI_translation/marathi/pi-1-pali-marathi-termbase-plain.md` (how each term was understood).

## The 2-01 engine (approved model, read `pi-1-my/notes-ch2-01.md` and `make_ch2-01.py`)
- NEVER run `make_sample.py` or `make_ch2-01.py`: they rewrite shared files (`my-zeroshot-terms.md`, the model chapters).
- `F.translate_cu(text)` handles headings (HEAD), «(Ka)» lines and clause text. Extend in memory: `F.NAMES`, `F.SYN`, `F.GEN`, `F.BODY`, `F.CITTA_KIND`, `F.QUAL`, `F.QUAL_ADV`, `F.ARAMMANA`, `F.HEAD`, `F.COLO`, `F.VAR_KIND`, or pairs in `F.CU_EXTRA_RULES`; then call `F.rebuild_cu()`. An unmatched line raises `Miss`; two different synonyms of one list with the same Burmese also raise `Miss`.
- Checker notes from 2-01: «မနော» goes in NOT_NEG; new privative stems in PRIV; new number words in NUM_PI; «သို့မဟုတ်» and «မဟာ» contain a «မ» that is not a negation (handle them in the checker, do not avoid the words).
- Frames (copy verbatim): Katame dhammā kusalā? = ကုသိုလ် သဘောတရားများ ဟူသည် အဘယ်တို့နည်း။; tasmiṃ samaye X hoti = ထိုအချိန်၌ X ရှိသည်; question ထိုအချိန်၌ ရှိသော X ဟူသည် အဘယ်နည်း။; closer ဤသည်မှာ ထိုအချိန်၌ ရှိသော X ဖြစ်သည်။; ṭhapetvā X = X-ကို ချန်ထား၍; eko X = X တစ်ပါး.
- Factor names: phassa တွေ့ထိမှု, vedanā ခံစားမှု, saññā မှတ်သိမှု, cetanā စေ့ဆော်မှု, citta စိတ်, pīti ပီတိ, sukha သာယာမှု, upekkhā ဥပေက္ခာ, ekaggatā စိတ်၏ စူးစိုက်မှု; -indriya X၏ စွမ်းရည်; -bala X၏ စွမ်းအား; khandha အစုအဝေး; viññāṇa သိစိတ်; saṅkhāra ပြုပြင်ဖန်တီးမှု; dhātu ဓာတ်; jhāna ဈာန်; magga မဂ်. The full list is the «Cittuppāda (2-01)» section of `my-zeroshot-terms.md`.

## About the text
The Cittuppāda chapters ask «Katame dhammā kusalā? Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti …, tasmiṃ samaye phasso hoti, vedanā hoti …» and define each factor with a synonym list: «Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – ayaṃ tasmiṃ samaye phasso hoti.» Then the saṅgaha / suññata summaries and the other cittas (unwholesome, resultant, functional). The Rūpakaṇḍa classifies matter; the Nikkhepakaṇḍa and the Aṭṭhakathākaṇḍa explain the Mātikā items, so they reuse the Mātikā strings of my_formulas.py.

## Source and output
- Source: `AI_translation/pali/pi-1_split_chapters/<ch>.md`
- Output: `AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/<ch>.md` (same filename).
- Generator `pi-1-my/make_<your chapters>.py`; notes `pi-1-my/notes-<your chapters>.md`; check `pi-1-my/check_<your chapters>.py`.

## Rules
- Identical Pāli = identical Burmese, within your chapters and with the model. GENERATE every chapter with a script that composes the frames; don't type repeated formulas by hand. Where the model's table covers a term, phrase or Mātikā item, use it unchanged.
- Synonym lists: each Pāli synonym its own Burmese item, the same as the model's table where it has one, order and count kept; no two synonyms of one list share a Burmese word unless the Pāli repeats the word. A new synonym gets a plain word distinct from the existing table values, logged in your notes.
- Polarity and numbers exact; check per line by script.
- A NEW recurring term or phrase: record it in your notes, one «Pāli = Burmese» per line. Do not edit my-zeroshot-terms.md or my_formulas.py. A consistency pass aligns all agents afterwards.
- No notes of your own inside the translation. Variant brackets as the model.
- «…pe…» and «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has «–» or «—», same spot and count per line. No «।», no «:-», no «?». Statements end with «။».

## Verify every chapter (all must pass before you report)
```
python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-1_split_chapters AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters <ch>.md
python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-1_split_chapters/<ch>.md AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/<ch>.md
python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-1_split_chapters/<ch>.md AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK. Plus your own check: 0 mismatches. (check_text_pe.py leaves copies in `pi-6-mr/chk-pe/`: delete your chapter copies there afterwards.)

## Final report (short)
Per chapter: checks passed, segment count, your check result; key new terms (or point to your notes); unsure Pāli and source slips.
