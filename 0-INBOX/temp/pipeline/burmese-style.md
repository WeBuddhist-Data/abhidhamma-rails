# Burmese plain translations: shared style rules (pi-1 and later books)

Audience: AI_translation/audience_profile/plain.md. Write clear, modern, natural Burmese that a general Burmese reader follows easily. Minor clarification through wording is OK, but add nothing that is absent from the source. Priority: understanding > accuracy > readability > consistency.

Status: approved by the user with the pi-1 sample (2026-11-16); binding.

## Sources (copyright rule, user 2026-11-16)
- Translate FROM THE PĀLI only: AI_translation/pali/pi-N_split_chapters/.
- Do NOT use, look up or copy any existing Burmese translation or nissaya of the Abhidhamma: not the Religious Affairs (သာသနာရေးဦးစီးဌာန) translation, not Wikisource, not dhammadownload.com, not archive.org nissaya collections, not any web source. No web searches for Burmese renderings.
- Cross-check of MEANING only (never wording): the English zero-shot (AI_translation/english/pi-N-english-plain-zeroshot_split_chapters/) and the finished Marathi / Hindi tracks of the same book.
- The only free Burmese reference is the public-domain palm-leaf Mātikā nissaya in 0-INBOX/temp/language-priority/burmese-nissaya-pilot/. It is not transcribed; do not try to read it.

## Language and vocabulary
- Modern written (literary) Burmese, plain and simple: statements end in သည် / ၏ forms; possessive ၏, locative ၌ / တွင်; avoid archaic nissaya style (no ၎င်း-chains, no word-by-word gloss order).
- Use the Burmese Buddhist words that ordinary Burmese readers already know and use, e.g. ကုသိုလ်, အကုသိုလ်, စိတ်, ရုပ်, ဝေဒနာ, နိဗ္ဗာန်, မြတ်စွာဘုရား, ရဟန်း, ရဟန္တာ. These are normal Burmese words, not opaque Pāli.
- Do NOT leave a technical Pāli compound in Burmese script that an ordinary reader does not know (e.g. a triad or dyad name such as saṃkiliṭṭhasaṃkilesika). Translate its meaning in plain Burmese.
- Each Pāli term keeps one Burmese rendering per sense, the same everywhere. Identical Pāli = identical Burmese.
- Unicode Burmese only (never Zawgyi). Spell in standard Myanmar orthography.
- Book titles: Burmese only, no Pāli name and no bracketed gloss. Mid-sentence, put the title in quotes.

## Typography
- A statement ends with «။». A list or clause break uses «၊». A question ends with its question particle (လော / နည်း) and «။». No «?», no «।».
- Quotes: “…” outer, ‘…’ inner.
- **DASH RULE (user, strict):** «–» only where the Pāli has «–» or «—», at the same spot, with the same count on every line. Never add one anywhere else. No «:-». Rephrase instead.
- «…pe…» and «…Pe…» become one «…» at the same spot (do not use the traditional ပ / ပေ။).
- Digits: where the Pāli has digits, e.g. «(1)», keep the same international digits (the checker reads them). Numbers written as Pāli words become Burmese number words.
- Item letters: Pāli (Ka) (Kha) (Ga) … become (က) (ခ) (ဂ) … in the same order.
- Variant readings in square brackets keep the sigla and the variant's Pāli in Roman script, with a Burmese label: «[ပါဌ်ကွဲ (Syā.): …]» when a word differs; «[စာလုံးပေါင်းကွဲ (Syā.): …]» for spelling only. Same count of «[» as the Pāli line.
- Editorial notes in square brackets are translated.

## Structure (hard rules)
- Every block ID stays exactly as in the source, at the end of the last line of its segment, in the same order.
- Headings keep their #-level.
- Each segment has exactly the source's number of non-empty lines, one blank line between segments, no double blank lines.
- Identical Pāli formulas get identical Burmese: build tables and frames in a script (formula module + generator), as in the Marathi runs.

## Lessons from earlier tracks (apply from the start)
- abyākata = neither wholesome nor unwholesome (ethically indeterminate), not "neutral" feeling.
- Keep distinct, one word each: vicikicchā vs kaṅkhā; mettā vs abyāpāda; kukkucca vs uddhacca; vīriya vs padhāna / vāyāma.
- samudaya = arising; yoni ≠ saṃsāra.
- Synonym lists: each Pāli synonym gets its own Burmese word; no two synonyms of one list share a word unless the Pāli repeats it.

## Cross-book core terms
Approved by the user on 2026-11-16: the full list is 0-INBOX/temp/pipeline/pi-1-my/my-zeroshot-terms.md (book frame, Mātikā triads and dyads, cluster names, headings) and the code is pi-1-my/my_formulas.py. The main ones:
- dhamma (phenomenon) = သဘောတရား (plural သဘောတရားများ); not bare တရား.
- kusala / akusala = ကုသိုလ် / အကုသိုလ်; abyākata = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော.
- Dhammasaṅgaṇī = သဘောတရားများကို စုစည်းရေတွက်ခြင်း; Abhidhammapiṭake = အဘိဓမ္မာပိဋကတွင်; Mātikā = ခေါင်းစဉ်စာရင်း.
- vedanā = ခံစားမှု; sukha / dukkha (feeling) = သာယာ / နာကျင်; vitakka / vicāra = စတင်ကြံစည်မှု / ဆက်လက်သုံးသပ်မှု.
- sampayutta / vippayutta = Nနှင့် ယှဉ်တွဲသော / Nနှင့် ကင်းကွာသော; sa-X = N၏ အာရုံ ဖြစ်နိုင်သော.
- Negation: free na / no = «… မဟုတ်»; privative a- / an- = မ + verb; pahātabba = ပယ်ရမည့် (negative ပယ်ရမည် မဟုတ်).
- Clusters «N-တို့၏ အစု»: hetu အမြစ်, āsava စိတ်အစွန်းအထင်း, saṃyojana နှောင်ကြိုး, gantha အထုံး, ogha ရေအလျဉ်, yoga ထမ်းပိုး, nīvaraṇa အတားအဆီး, parāmāsa မှားယွင်းသော ယူဆမှု, upādāna စွဲလမ်းမှု, kilesa ကိလေသာ.
- cetasika = စိတ်၏ အဖော်; vijjā / avijjā = အမှန်သိမြင်မှု / အမှန်ကို မသိမှု; nāma / rūpa = စိတ်ပိုင်း / ရုပ်ပိုင်း; samatha / vipassanā = စိတ်ငြိမ်သက်ခြင်း / ထိုးထွင်းသိမြင်ခြင်း.
- Planes: ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ.

## pi-1 termbase (locked 2026-11-17)
- The locked termbase is `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md`; see `0-INBOX/temp/pipeline/pi-1-my/termbase/APPROVED.md`.
- Changes to the earlier wording: paṭiccasamuppāda = «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ»; Suññatavāro = «ဆိတ်သုဉ်းခြင်း ဖော်ပြချက်»; uppanna = «ဖြစ်ပေါ်ပြီးသော», samuppanna = «ဖြစ်ပေါ်လာသော»; ākāsa = «ဟင်းလင်းပြင်»; vibhava = «ဘဝ ပျောက်ကွယ်ခြင်း».
- Rules: proper names stay names (Paranimmitavasavattī = «ပရနိမ္မိတဝသဝတ္တီ»); nāma-rūpa = «စိတ်ပိုင်း / ရုပ်ပိုင်း».

## Verify (must pass)
```
python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py <pali_split_dir> <burmese_split_dir> <ch>.md
python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py <pali_file> <burmese_file>
python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py <pali_file> <burmese_file>
```
All must print OK (equal lines, dashes, ellipses, no «।», no «:-», no double blanks, item numbers and «[» counts). Also: no «?» and no Zawgyi-only code points.

## pi-2 termbase (locked 2026-11-18)
- `AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md`; see `0-INBOX/temp/pipeline/pi-2-my/termbase/APPROVED.md` (sha256 715bebdddc3ae9a65a2032124ea52b6b7baa69c725a083883e863d7f688e8769; review changes A8, B1, B2 2026-11-18).

## pi-3 termbase (locked 2026-11-19)
- `AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md`; see `0-INBOX/temp/pipeline/pi-3-my/termbase/APPROVED.md` (sha256 857bfa8eff945d72eb1a52ec55c452798b34f9d11860322bfe7cc15096f243f3; review change A3 / B3 2026-11-19).

## pi-4 termbase (locked 2026-11-19)
- `AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md`; see `0-INBOX/temp/pipeline/pi-4-my/termbase/APPROVED.md` (sha256 6ba052ff7edfcfa36d808b8aaf8b69600ce303d13381aaee4b8a81d3d92c2723; review changes 2026-11-20).

## pi-5 termbase (locked 2026-11-22)
- `AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md`; see `0-INBOX/temp/pipeline/pi-5-my/termbase/APPROVED.md` (sha256 e45d99f4d08fed7d0343cbdf86c5d5d06d91db836b4b3af6b6b150b6adf6e5fa; rails-step and review changes 2026-11-22). paṭivedha family «ထိုးဖောက်၍ သိ…» (pi-4), apart from vipassanā «ထိုးထွင်းသိမြင်ခြင်း»; thero «မထေရ်»; eva «ပင်».

## pi-6 termbase (locked 2026-11-22)
- `AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md`; see `0-INBOX/temp/pipeline/pi-6-my/termbase/APPROVED.md` (sha256 847e49cdef8bc8c3f90d2de9f92fd0c6479f60e17a04c8243286b12602a86453). Beings / persons genitives «…၌ ရှိသူ / …သူ»; yattha «အကြင်နေရာ»; uppajjamāna «ဖြစ်ပေါ်ဆဲ» vs uppanna «ဖြစ်ပေါ်ပြီးသော»; kāyasaṅkhāra «ကိုယ်၏ ပြုပြင်ဖန်တီးမှု»; anuloma / paccanīka «အဟုတ်ပြ / အငြင်းပြ ပုံစံ».

## pi-7 termbase (locked 2026-11-26)
- `AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md`; see `0-INBOX/temp/pipeline/pi-7-my/termbase/APPROVED.md` (sha256 ceb0842a98d4a219466e1fc494f071773710cb9963554bd1dc8dd6e61fecff74; review change 2026-11-26: hetuka headings «… အမြစ် ရှိခြင်း …», bhindati «သင်းခွဲသည်»). The 24 conditions «Nဟူသော အကြောင်း» (frame forms N / «…ကြောင့်» / «…ကြောင့် မဟုတ်»); paccaya «အကြောင်း»; paṭicca / nissāya «မှီ၍»; samanantara «ကောင်းစွာ ချက်ချင်း နောက်»; nānākaraṇa «ကွဲပြားမှု»; avasesa «ကြွင်းကျန်သော».
