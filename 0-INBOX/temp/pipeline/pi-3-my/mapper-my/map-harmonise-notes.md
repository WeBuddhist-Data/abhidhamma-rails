# pi-3 Burmese keyword mapping (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»): consistency pass (harmonise) notes

Brief: `map-harmonise-brief.md`. Model: the pi-2 pass (`pi-2-my/mapper-my/map-harmonise-brief.md`, `map-harmonise-notes.md`).
Changes only through the mapping scripts (backed up first in `harmonise-backup/`: the four `map_*.py`, the four
`map-table*.md`, and all 16 `*.mapped.md` in `harmonise-backup/mapped/`), then every script was re-run. No mapped file
was edited by hand. Burmese only from this track's final pi-3 text and the final pi-1 / pi-2 mappings; no other Burmese
source, no web source; `0-INBOX/temp/language-priority/` not opened; `pi-1-my/` and `pi-2-my/` only read. Translation
files, 1-SOURCES/, 4-SYSTEM/ and other tracks untouched. Nothing committed.

## Numbers

- Values changed: **55** in 5 chapter files; preamble, 1, 2, 3, 4, 5, 7, 9, 10, 12, 15: 0.
  6: 1 · 8: 11 · 11: 41 · 13: 1 · 14: 1 (`harmonise_map_diff.py`).
- The approved sample is unchanged: `preamble.mapped.md`, `1-uddeso.mapped.md`, `2-pathamanayo.mapped.md` and
  `map-table.md` are byte-identical to the backup after the re-run (the 11 approved differences from pi-1 / pi-2 and
  ñassāmi «သိရတော့သည်» stay).
- Book-wide scan (`harmonise_map_scan.py`, first letter case-insensitive, all 16 `*.mapped.md`): keywords with more
  than one value **13 before → 9 after** (`scan-before.tsv`, `scan-after.tsv`; segment IDs per value in
  `scan-before-detail.txt`, `scan-after-detail.txt`). 4 resolved, 1 reduced, none new. Every one of the 9 is a
  logged, justified difference (table below).
- Lemma-level scan (`harmonise_lemma_scan.py`: keywords grouped across case / number endings, e.g. Arūpino / Arūpīhi,
  hetukā dhammā / hetukehi dhammehi): groups with more than one value **19 before → 18 after**
  (`lemma-scan-before.txt`, `lemma-scan-after.txt`); every remaining group is listed below with its reason.
- Script tables (`harmonise_tables.py`): across all `T_*` tables and CTX of the four scripts, one key has two values
  (sammā: homage «အပြည့်အဝ» CTX[T-1] vs «မှန်ကန်သော», approved); the three agents' tables agree on every shared key.
- Verification (all pass; `harmonise-verify.txt`): the brief's keyword-preservation one-liner prints `bad []` for all
  16 files (568 lines); every script's presence verifier reports 0 failures; the book-wide check with the ONE
  `presence_check.py` over all 8442 values: 0 failures; no «, » / «၊» / « / » in any value.
- Assembled: `AI_translation/burmese/pi-3-keywords-by-reference-pali-burmese-plain.md`, **568 lines**, every ID once
  and in the Pāli file's order, keyword lists identical to `AI_translation/pali/pi-3-keywords-by-reference-pali-plain.md`
  (8442 keyword uses). No `*sample*` file was in `mapper-my/`.

## Scripts changed

- All four `map_*.py`: their own copies of the presence check (ATTR_FROM … presence(); the four copies were
  byte-identical) replaced by an import of the ONE shared `presence_check.py` (decision 3; the module's docstring is
  the documented ending list). `map_all.py` got only this change (and its docstring line); its output is identical.
  Checked before any value changed: with the alignments switched off, all 16 mapped files were byte-identical.
- The three chapter scripts (`map_ch3-6-8-9.py`, `map_ch7-10-11.py`, `map_ch12-15.py`): `lookup()` renamed
  `_lookup()`; a wrapper `lookup()` applies `harmonise_rules.apply()` to the keyword's FINAL value only (not to the inner
  lookups of compose / nominative-redirect rules, which look other keywords up: a first run without that guard let
  rule R leak into ch15's «dhammehi vippayuttā» via ch12-15's redirect to «dhammā vippayuttā»; fixed before the
  final run). Their REASONS take `harmonise_rules.REASONS`; their map-table rules text ends with a short
  «map-harmonise» section (`harmonise_rules.TABLE_NOTE`). No UNEXPLAINED row in any `map-table*.md`.
- New modules: `presence_check.py` (the merged ending list), `harmonise_rules.py` (the alignments R, V, S).
- New helpers (read-only on the mapping): `harmonise_map_scan.py`, `harmonise_lemma_scan.py`, `harmonise_show.py`,
  `harmonise_tables.py`, `harmonise_map_diff.py`; one-off patcher `harmonise_patch.py` (idempotent).

## Decisions applied

1. **Approved sample and the approved differences**: unchanged (map_all.py does not import harmonise_rules; its output
   and map-table.md are byte-identical). The sample's values bind the later chapters where the keyword and the kind of
   segment are the same (uppannā positive vs fragment, hetukā dhammā gap M4, rūpa / dukkha / sukha by sense, sammā).
2. **Same keyword, same kind of segment, same value** (scan): aligned (harmonise_rules.py)
   - **R** dhammā vippayuttā «သဘောတရား … ကင်းကွာသော» → «ကင်းကွာသော သဘောတရား» (ch8 ^3-306–^3-316: 11). ch8's
     segments have the same frame as ch11's 56 («…ena ye dhammā sampayuttā, tehi dhammehi ye dhammā vippayuttā, te
     dhammā … vippayuttā»): the adjacent Pāli biterm is the relative clause «ye dhammā vippayuttā», text «ကင်းကွာသော
     သဘောတရားများ» (pi-1 dhammā saṅkhatā order, ch7-10-11 M2). The subject + predicate value «သဘောတရား … Pသော» (sample
     P1, ch3-6-8-9 M12) stays for dhammā saṅgahitā (2, 4, 5, 13, 15) and dhammā asaṅgahitā (3, 6), whose Pāli has no
     adjacent «ye dhammā P» (checked for every use).
   - **V** item + verb biterms: dhammehi vippayuttā «သဘောတရား … ကင်းကွာသော» → «သဘောတရားများနှင့် ကင်းကွာသော» (ch11
     ^3-370–^3-408: 38), = ch15's 38: the first occurrence is the item «X-ehi dhammehi ye dhammā vippayuttā», text
     «…သဘောတရားများနှင့် ကင်းကွာသော» (present in all 38 ch11 segments; the later «tehi dhammehi …» «ထိုသဘောတရားတို့နှင့်»
     does not decide); bhavena vippayuttā ^3-365 / ^3-366 «ဘဝ … ကင်းကွာသော» → «ဘဝနှင့် … ကင်းကွာသော» (2), as ch15
     ^3-470 / ^3-471; viññāṇena vippayuttā ^3-362 «သိစိတ် … ကင်းကွာသော» → «သိစိတ်နှင့် … ကင်းကွာသော» (1), as ch15 ^3-466.
   - **S** sukha ^3-210 (ch6), ^3-437 (ch13), ^3-451 (ch14) «သာယာသော» → «သာယာမှု» (3). The sample's f_sukha took the
     first sukh- word of the Pāli, here «Sukhāya vedanāya», which is a keyword of its own (Sukhāya / sukhāya «သာယာသော»);
     the fragment sukha belongs to sukhasahagatehi (text «သာယာမှုနှင့်အတူ ဖြစ်သော»), as in the same long dyad-list
     segments ^3-227, ^3-447, ^3-455 and the sample's ^3-91 sukhasahagatā «သာယာမှု». sukha now has one value book-wide.
   Checked and already one value (no change): upari / Uddhaṃ «အထက်» (^3-190, ^3-352, ^3-447; ^3-192, ^3-416: text
   «အထက်တွင်» / «ထို့အထက်တွင်», the locative goes and «ထို့» is tato, rule 1; ch7-10-11 M4's «ch13 has «အထက်တွင်»» was
   the text, not the value); kehici «အချို့» (161); su «ကောင်းစွာ» and buddho «နားလည်အပ်သော» (ch6 ^3-227 by CTX, ch14
   ^3-455 by table: the same values); maccu / mataṃ «သေခြင်း» (decision 4); pucchake / pucchakena and punareva (kept,
   below); arūpa ^3-352 (kept, below).
3. **One merged rule list** (the parallel agents' rules under one name each; the values agree, see the table check
   and the scans):
   - **Instrumental / dative / locative items take the value of their nominative** (ch3-6-8-9 M11 = ch7-10-11 M1 =
     ch12-15 Q1; pi-1 rule 1: no case particle, the text's «…နှင့်» / «ဖြင့်» / «တွင်» go): Vedanākkhandhena = ခံစားမှု
     အစုအဝေး, indriyena = စွမ်းရည်, bhavena = ဘဝ, Hetūhi = အမြစ်, Rūpīhi = ရုပ် ဖြစ်သော (sample Rūpino), Arūpīhi =
     ရုပ် မဟုတ်သော (sample Arūpino); «X dhammehi» = the pi-1 / pi-2 «X dhammā» phrase where the text has it, else X +
     « သဘောတရား» (rule 5; gap « … » for fragments, sample M4); an instrumental that pi-1 / pi-2 map as such keeps that
     value (dassanena «သစ္စာကို မြင်ခြင်း»); one Pāli word upādādhammehi = «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား»
     (pi-1 upādā dhammā). The three implementations stay in their scripts (case_variants / nom_lookup / nom_redirect,
     different candidate-ending lists); no keyword or lemma gets two values from them (lemma scan).
   - **The vippayuttā / sampayuttā pairing** (ch3-6-8-9 M12 = ch7-10-11 M2 / M3 = ch12-15 Q2, now rules R and V):
     predicate alone = ယှဉ်တွဲသော / ကင်းကွာသော (whatever the text's «…ကြသည် / …ကြသနည်း / …သည့်အရာ»); «ye dhammā P»
     = «Pသော သဘောတရား» (R); the frame «te dhammā … P» = «သဘောတရား … Pသော» (sample P1); «X-ena / X-ehi P» = Xနှင့်
     (inner «များ» stays) + « Pသော» contiguous or « … Pသော» gapped; «X … Pသော» where the text attaches no «နှင့်» to X
     (Kusalehi «ကုသိုလ် သဘောတရားများနှင့်»); Adhimokkhena = ဆုံးဖြတ်မှု (= Q6).
   - **kehici = «အချို့»** (ch3-6-8-9 M10 = ch7-10-11 M5 = ch12-15 Q3; text «…တို့၏ အချို့နှင့်», rule 1); «na kehici»
     segments have no kehici keyword.
   - **The verse words** (ch3-6-8-9 M13 = ch12-15 Q5 = ch7-10-11 T_FRAME verse list), one value each: upari / Uddhaṃ
     အထက်; pare နောက် (tato pare); gocchaka / gocchake / gocchakesu အစု; antara / antare / antarā ကြားညှပ်;
     duke / dukā နှစ်မျိုးတွဲ; vidhā မျိုး, tiṃsa သုံးဆယ်, Samatiṃsa သုံးဆယ်ပါး အပြည့်; tathariva ထို့အတူ; the counts
     with «ပါး» (cuddasa, pannarasa, soḷasa, ekūnavīsati, paññāsa, Tevīsa, tecattālīsaṃ, sattacattālīsa);
     sattacattālīsa dhammā သဘောတရား လေးဆယ့်ခုနစ်ပါး; bhavā ဘဝ; labbhati / labbhare တွေ့ရသည် (negative in the text,
     rule 8); niddese အကျယ် ဖော်ပြချက်; Navamassa နဝမ; saṅgahaṃ gatā အကျုံးဝင်သော; manasi နှလုံးသွင်းခြင်း;
     manena စိတ်, yuttā ယှဉ်သော; vicāraṇā ဆက်လက်သုံးသပ်မှု; Samucchede ပိုင်းဖြတ်ခြင်း; maccu / mataṃ သေခြင်း;
     pumaṃ ယောက်ျား; su ကောင်းစွာ, buddho နားလည်အပ်သော; mogha အချည်းနှီး, pucchakena မေးခွန်း.
   - **Headings**: the ordinals as the text writes them (ပဉ္စမ … စုဒ္ဒသမ, = ch3-6-8-9 «as before», ch7-10-11 T_FRAME,
     ch12-15 Q4); the «…padaniddeso» members sampayutta / vippayutta / saṅgahita / asaṅgahita = «…သော» (N11).
   - **Presence-check endings**: ONE documented list, `presence_check.py` (pi-2's merged list + the sample's M7
     «သနည်း ရာ သေးသည်»); the agents added none.
4. **maccu**: the pi-3 text has «သေခြင်း» (^3-227, ^3-455: «… အိုခြင်း၊ သေခြင်း၊ ရုပ် …»); mapped as the text says
   (2 uses; mataṃ «သေခြင်း» 2). Listed for the rails step (below).
5. **Absolutives «…၍»** (ṭhapetvā «ချန်ထား၍» 87, paṭicca «အကြောင်းတို့ကို မှီ၍» 5; no value ends in «ပြီး» or «လျက်»);
   no « / » alternatives, no «၊» or «, » in any value.
6. **Translation files not changed.** Text inconsistencies met are listed for the rails step (below).

## Scan before / after

Before (13): arūpa, bhavena vippayuttā, dhammehi vippayuttā, dhammā vippayuttā, dukkha, hetukehi dhammehi, hetukā
dhammā, rūpa, sammā, sukha, uppannehi, uppannā, viññāṇena vippayuttā. Resolved (4): dhammā vippayuttā (R),
dhammehi vippayuttā, viññāṇena vippayuttā (V), sukha (S). Reduced (1): bhavena vippayuttā (3 values → 2, V). New:
none. 13 − 4 = 9.

### Every kept difference (exact scan, 9)

| keyword | values (uses; chapters) | why kept |
|---|---|---|
| arūpa | ရုပ်မရှိသော (14; 2 6 7 11 14 15) · ရုပ် မဟုတ်သော (1; 10) | Sense: the planes arūpāvacara / arūpabhava «ရုပ်မရှိသော ဘုံ» vs ^3-352 verse «Arūpakkhandhā cattāro» = the non-material aggregates «ရုပ် မဟုတ်သော အစုအဝေး» (= the sample's Arūpino / ch6, ch14 Arūpīhi «ရုပ် မဟုတ်သော»; pi-1 arūpino). Text: «ရုပ်မရှိသော» is not in ^3-352 |
| bhavena vippayuttā | ဘဝနှင့် … ကင်းကွာသော (4; 11 15) · ဘဝနှင့် ကင်းကွာသော (3; 11 15) | Rule V: gapped where other items stand between (^3-365, ^3-366, ^3-470, ^3-471), contiguous where Rūpabhavena / bhavena is the last item (^3-364, ^3-468, ^3-469). Grammar (text order) |
| dukkha | နာကျင်မှု (11) · ဒုက္ခ (10) · နာကျင် (5) | Sense, sample f_dukkha (approved): dukkhindriya «နာကျင်မှု» / dukkhasacca «ဒုက္ခ» / fragment of adukkhamasukha «နာကျင်» (positive part of «မနာကျင်», rule 8) |
| hetukehi dhammehi | အမြစ် ရှိသော သဘောတရား (8; 6 11 14 15) · အမြစ် … သဘောတရား (2; 15) | Sample M4 (approved, = hetukā dhammā ^3-94 / ^3-159): the negated «neva dassanena na bhāvanāya pahātabbahetukehi» (^3-486, ^3-511) «…အမြစ် ရှိသည် မဟုတ်သော သဘောတရား» has the phrase only with a gap. Grammar |
| hetukā dhammā | အမြစ် ရှိသော သဘောတရား (4; 2 7) · အမြစ် … သဘောတရား (2; 2) | Approved sample M4 (the same split). Grammar |
| rūpa | ရုပ် (18) · သိမ်မွေ့သော ရုပ် (12) · အဆင်းအရောင် (4; 2) | Sense, sample f_rupa (approved): rūpakkhandha matter / rūpāvacara, rūpabhava fine-material / rūpāyatana, rūpadhātu visible object; checked: in every segment the first rūpa compound is the fragment's compound |
| sammā | မှန်ကန်သော (11) · အပြည့်အဝ (1; preamble) | Approved: the homage sammāsambuddha (pi-1 / pi-2 preamble) vs sammappadhāna |
| uppannehi | ဖြစ်ပေါ်သော (1; 11) · ဖြစ်ပေါ်ပြီးသော (1; 15) | ^3-385 uppannehi = the fragment of Anuppannehi «မဖြစ်ပေါ်သေးသော» (rule 8, as the sample's ^3-102) vs ^3-491 Uppannehi = the word «ဖြစ်ပေါ်ပြီးသော» (as the sample's ^3-101 Uppannā). Grammar (fragment vs word) |
| uppannā | ဖြစ်ပေါ်သော (2; 2 7) · ဖြစ်ပေါ်ပြီးသော (1; 2) | Approved sample split (^3-101 word vs ^3-102 fragment); ch7 ^3-273 is the fragment «မဖြစ်ပေါ်သေးသော». Grammar |

### Lemma-level groups kept (18)

arūp, dukkh, hetuk dhamm, rūp, samm, uppann: as the exact scan. bhav vippayutt: rule V (contiguous / gapped).
avitakk dhamm, savitakk dhamm, saṃsaṭṭh dhamm: the fragment inside a compound (avitakkavicāramattā,
savitakkasavicārā, cittasaṃsaṭṭhasamuṭṭhānā) has the gap «X … သဘောတရား», the word itself (Avitakkā, Savitakkehi,
saṃsaṭṭhehi) is contiguous (sample M4). dhamm vippayutt: dhammā vippayuttā «ကင်းကွာသော သဘောတရား» (relative clause)
vs dhammehi vippayuttā «သဘောတရားများနှင့် ကင်းကွာသော» (item + verb): two constructions (R, V). sukh: Sukhāya /
sukhāya «သာယာသော» (pleasant feeling, attributive) vs the fragment sukha «သာယာမှု» (sukhasahagata, sukhindriya).
khandh: khandhato «အစုအဝေး ရေတွက်ရာ» (approved sample M3) vs the noun. man: manena «စိတ်» in the verse «manena yuttā»
(text «စိတ်နှင့် ယှဉ်သော»; «မနော» is not in ^3-316) vs mana / mano «မနော» in manāyatana / manoviññāṇa. pucchak:
pucchake «ဖော်ပြချက်» (approved sample M9, ^3-112 variant note «…pañhāpucchake», pañhā = «မေးခွန်း») vs pucchakena
«မေးခွန်း» (^3-318, ^3-518 moghapucchakena «မေးခွန်း အချည်းနှီး»; «ဖော်ပြချက်» is not in those segments; REPORT 2).
sat, upād, upādān: different words with one stem (sati / sataṃ «တစ်ရာ»; upādā / upādānaṃ; upādāna / upādāniyā).

### Other checks

- punareva = (no direct equivalent) (^3-178): the Pāli variant is kept in Roman script inside the text's bracket
  «[စာလုံးပေါင်းကွဲ (Pī.): punareva]» (pi-1 brief; the sample's M9 distinction: a translated note gets values).
- The 11 approved differences from pi-1 / pi-2 and the agents' «differs from pi-1 / pi-2» rows (antare «ကြားညှပ်»,
  maccu «သေခြင်း», pare «နောက်», arūpa ^3-352 …) all have their reasons in the map-tables; no UNEXPLAINED row.

## Text inconsistencies for the rails step (translation not edited)

1. maccu: ^3-227 (ch6) and ^3-455 (ch14) «သေခြင်း» (also mataṃ, jātijarāmataṃ «… သေခြင်း»), while the pi-2 termbase now
   has maccu «သေဆုံးခြင်း» (user-approved review change); pi-2's mapping has «သေမင်း» (death personified). Decide the
   pi-3 word for the verse list jāti / jarā / maccu.
2. pucchaka: ^3-112 (variant note «dukapañhāpucchake») «မေးခွန်းများဖြင့် ဖော်ပြချက်» vs ^3-318 / ^3-518
   (moghapucchakena) «မေးခွန်း»: the same word as «exposition» and as «question»; check.
3. The «tehi dhammehi ye dhammā …» clause: «ထိုသဘောတရားတို့နှင့်» (plural «တို့») next to the items' «…သဘောတရားများနှင့်»
   and «ထိုသဘောတရားများသည်» in the same segments (ch8, ch10, ch11): two plural markers for the same dhammehi / dhammā
   (style; the mapping takes the item form, rule V).
4. arūpa spacing: «ရုပ်မရှိသော» (planes, one word) vs «ရုပ် မဟုတ်သော» / «ရုပ် ဖြစ်သော» (spaced): spelling only.
