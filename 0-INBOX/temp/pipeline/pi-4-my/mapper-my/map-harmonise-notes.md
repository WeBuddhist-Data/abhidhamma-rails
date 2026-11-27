# pi-4 Burmese keyword mapping (Puggalapaññatti «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»): consistency scan notes

Brief: `../burmese-mapper-brief.md` (whole book, one script). Model: the pi-3 pass (`pi-3-my/mapper-my/map-harmonise-notes.md`).
Changes only through `map_all.py` / `presence_check.py` (backed up first in `harmonise-backup/`: both scripts,
`map-table.md` and all 12 `*.mapped.md`), then the script was re-run. No mapped file was edited by hand. Burmese only
from this track's final pi-4 text, `my4-zeroshot-terms.md` and the final pi-1 / pi-2 / pi-3 mappings; no other Burmese
source, no web source; `0-INBOX/temp/language-priority/` not opened; `pi-1-my/`, `pi-2-my/`, `pi-3-my/` only read.
Translation files untouched. Nothing committed.

## Numbers

- Scan (`map_scan.py` = pi-3 `harmonise_map_scan.py` with the pi-4 chapter order; first letter case-insensitive, all 12
  `*.mapped.md`): keywords with more than one value **95 before → 89 after** (`scan-before.tsv`, `scan-after.tsv`;
  segment IDs per value in `scan-before-detail.txt`, `scan-after-detail.txt`). 6 resolved, none new.
- Values changed by the pass: 4 (ch4 1, ch5 2, ch6 1); every other mapped line is byte-identical to the backup.
- Verification after the pass: the brief's keyword-preservation one-liner prints `bad []` for all 12 files (250
  lines); presence failures 0 in every chapter; no «, » / «၊» / « / » in any value.
- Assembled: `AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md`, 250 lines, every ID once and in
  the Pāli file's order, keyword lists identical to `AI_translation/pali/pi-4-keywords-by-reference-pali-plain.md`
  (5828 keyword uses).

## Aligned (same keyword, same kind of segment)

- **A1** puggalo appasādaṃ janeti: two text orders from the composer → one value «ပုဂ္ဂိုလ် … မကြည်ညိုမှုကို ဖြစ်စေသည်»
  (as puggalo pasādaṃ janeti), ^4-164 / ^4-165.
- **A2** absolutives (pi-1: absolutives keep «…၍»): āvikatvā, dubbalyaṃ āvikatvā, pariyogāhetvā, paccakkhāya had a bare
  stem where the text has only the negative absolutive «မXဘဲ» (anāvikatvā, apariyogāhetvā, appaccakkhāya) → always
  «…၍»; presence rule «neg-abs» (presence_check.py: «X၍» against «မXဘဲ», the pi-1 rule 8 positive part).
- **A3** nirodha = «ချုပ်ငြိမ်းခြင်း» where the text has the noun; «ချုပ်ငြိမ်း» stays only where the text has
  dukkhanirodha(gāminī) «ချုပ်ငြိမ်းရာ» (grammar, kept).
- **A4** spacing only: unnaḷo = «ဘဝင် မြင့်သော», mukharo = «စကား များသော» in ^4-118 and ^4-119 alike (the text writes
  «ဘဝင်မြင့်သူ / စကားများသူ» in ^4-118 but «ဘဝင် မမြင့်သူ / စကား မများသူ» in ^4-119; both chunks are present in both).

## Kept differences (89), by reason

- **Sense by context, one sense per segment** (pi-1 decision 3; the function and its stems are in `map_all.py`):
  dhamma, dhammaṃ, rūpa, sammā, dukkha, dukkhassa, sukha, phala, phalaṃ, vaṇṇa, saṅkhāra, sota, puthu, kula, hetu,
  gāmī, gandha, gate, gataṃ, eḷaka, daṇḍa, mukhā, mutta, mūla, mūlaṃ, kasira, kammaṃ, kattā, kārī, kāyena (pi-2: the
  mental body in the third jhāna), obhāso, pada, patta, pāpa, pāṇa, raja, sacca, sama, samāpattiyā, sutte, ṭhita,
  ṭhite, upapanno, vācāya, āhāro, attha, atthe, bhabba, bhūta, byāpajjati, indriya, indriyānaṃ, sota, ekanta, eva,
  evaṃ, evameva, aggaṃ (dhajagga «ဖျား» / rajagga: no word of its own), ajinaṃ, anussati, para (name syllable /
  «သူတစ်ပါး»).
- **Person-type NAME vs the same word as an adjective** (P1 / rule 3): niyato (NAME «လမ်းကြောင်း ကျိန်းသေသူ» / the
  sotāpanna formula «ကျိန်းသေသော»), sampajāno (NAME / «sato sampajāno» «…သိမြင်သော»), vāco, pameyyo (su- / du- /
  a-), sambuddho (P2: in paccekasambuddho = (no direct equivalent)), paññatti / puggalapaññatti (book title / the
  designation, approved terms).
- **Word vs fragment** (rule 8, as pi-3 uppannā): pahīno / pahīnaṃ / pahīnā / pahīnāni («ပယ်ပြီးသော» for the word,
  «ပယ်ရသော» for the fragment of appahīna «မပယ်ရသေး»), vigata (NAME part «ကင်းပြီး» / «ကင်း»), manasi, phāsu,
  attanā («မိမိကိုယ်တိုင်» / brahmabhūtena attanā «မိမိကိုယ်»), gahapati (gahapatikula «သူကြွယ်မျိုး»), nirodha.
- **The text words the same Pāli differently** (each listed for the rails step below): senāsana, sappi, atthaṃ,
  byañjanaṃ, suṇāti, sutvā, paṭipanno, sammāpaṭipannā, abhisamayo, dubbaṇṇo, nikati, gilāna, ṭhito, dhāraṇatā (now one
  form where both occur: «စွဲမှတ်ထားခြင်း» / «စွဲမှတ် ထားခြင်း» by segment).

## Text inconsistencies for the rails step (translation not edited)

1. sātthaṃ sabyañjanaṃ: ^4-107 / ^4-108 «အနက်အဓိပ္ပာယ်နှင့် ပြည့်စုံသော၊ စကားလုံးနှင့် ပြည့်စုံသော» vs ^4-177
   «အနက် ပြည့်စုံသော၊ သဒ္ဒါ ပြည့်စုံသော»; pakāsenti «ထုတ်ဖော် ပြ» vs pakāseti «ထင်ရှားပြ».
2. senāsana: «ကျောင်းအိပ်ရာနေရာ» (requisites ^4-116, ^4-117, ^4-192) vs «အိပ်ရာ နေရာ» (^4-172, ^4-182).
3. sappi: «ထောပတ်» (^4-176 sappitela) vs «ထောပတ်ကြည်» (^4-199, where navanīta is «ထောပတ်»).
4. dīgharattaṃ: «ရှည်လျားသော ကာလပတ်လုံး» (^4-113, ^4-163) vs «ကြာမြင့်စွာ» (^4-116, ^4-117, where ciraṃ is absent).
5. paṭipanna: «ကျင့်ကြံ…» (most) vs «ကျင့်…» (^4-164 / ^4-165 «ကောင်းစွာ / မှန်ကန်စွာ ကျင့်သူတို့», ^4-189
   dhammānudhammappaṭipanno «…ကျင့်သူ»); ^4-62 has «မှန်ကန်စွာ ကျင့်ကြံသော».
6. suṇāti / sutvā: «ကြားရ» (^4-91 …), «ကြား» (^4-194, ^4-195), «ကြားနာ» (^4-177).
7. abhisamaya: «ထင်ထင်ရှားရှား … သိမြင်ခြင်း» (^4-60 anabhisamayo) vs «ထိုးဖောက် သိမြင်ခြင်း» (^4-148 … dhammābhisamayo),
   which is close to paṭivedha «ထိုးဖောက်၍ သိခြင်း» (^4-60).
8. nikati: «ကောက်ကျစ်ခြင်း» (^4-52, pi-2) vs «စဉ်းလဲခြင်း» (^4-179), the word of sāṭheyya (^4-51).
9. dubbaṇṇa: «အဆင်း ညှိုး» (^4-116 cloth) vs «အဆင်း ဆိုး» (^4-168, ^4-184 persons).
10. phale ṭhito: NAME «ဖိုလ်၌ တည်နေသူ» (^4-15 …) vs ^4-29 / ^4-30 «ဖိုလ်၌ တည်သောအခါ».
11. gilāna: «လူနာ» vs «သူနာ» in the requisite formula gilānapaccaya (^4-116, ^4-117, ^4-192) — probably the idiom;
    to confirm.
12. ^4-M-14: «မဂ်နှင့် ပြည့်စုံသူ လေးယောက်» vs «ဖိုလ်နှင့် ပြည့်စုံသော ပုဂ္ဂိုလ် လေးယောက်» (the same Pāli frame
    «… samaṅgino puggalā»; the group NAME is «မဂ်နှင့် ပြည့်စုံသော ပုဂ္ဂိုလ် Nယောက်»).
13. ^4-M-10 (22) / (23): the Pāli lists four names per line (Rūpappamāṇo, rūpappasanno, …), the Burmese two (each pair
    joined «… အတိုင်းအတာ ထား၍ …၌ ကြည်ညိုသူ», as the niddesa ^4-171 / ^4-172 treats each pair as one type).
14. Spacing only: dhāraṇatā «စွဲမှတ် မထားခြင်း» (^4-59) / «စွဲမှတ်ထားခြင်း» (^4-79); unnaḷo, mukharo (A4).
15. Pāli: ^4-70 «Katamo ca pugalo» (misprint of puggalo; mapped as puggalo).
