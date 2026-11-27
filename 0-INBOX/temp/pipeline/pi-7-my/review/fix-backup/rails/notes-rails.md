# pi-7 Burmese rails translation (Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»): notes

Method (as the approved pi-6 Burmese rails run, pi-6-my/rails/, read only; brief `pi-7-my/burmese-rails-brief.md`):
rails = the harmonised zero-shot (AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters, read only) brought
into agreement with the locked termbase (AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md, sha256 faef9155…,
read only; termbase/APPROVED.md, decisions-A.tsv, notes-part5.txt) and with the §A text items of
mapper-my/map-harmonise-notes.md, keeping pi-1 … pi-6 identity, identical Pāli = identical Burmese, the dash and quote
rules, «။» / «၊» and the structure. The zero-shot is built by 18 formula generators that import each other in memory
(make_sample, make_ch1-01 … make_ch5-13-20 + my7_formulas.py; the preamble is the fixed table of regen_zeroshot.sh),
so a systematic change is a source patch of a RAILS LAYER run in memory (no generator is edited) and single-segment
differences are explicit rules on the built text. **Result: 23 source patches (families L01 … L10), 3 residual rules
(R01 … R03); 170 of 27749 non-empty lines changed; adherence 1751 misses → 1695 (GENUINE 56 rows fixed, 0 left;
1691 INFLECTION + 4 ARTEFACT, all verified); ALL CHECKS PASSED; a second run of regen_rails.sh changes no byte.**
Rebuild and check everything with `zsh 0-INBOX/temp/pipeline/pi-7-my/rails/regen_rails.sh` (two builds of ~7–8 min
each: run it in the background). Sources: the Pāli, the termbase / decisions / APPROVED.md / notes-part5.txt, the
zero-shot and its generators, its keyword map, map-harmonise-notes.md and the final pi-1 … pi-6 rails only. No Burmese
translation, nissaya or web source was used; language-priority/ was not opened; nothing committed; the system temp
folder not used (scratch files in rails/ only; no __pycache__ written: sys.dont_write_bytecode).

Brief note: the brief's §A numbering («2, 6, 8–13 decided; 1, 3, 4, 5, 6, 7, 14 left») is pi-6's; the pi-7 lists
are termbase/notes-part5.txt 5e (23 decided, 15 left) and map-harmonise-notes.md §A 1–38, followed here.

## Files
- protected-md5-before.txt: md5s of 292 files recorded before any work (protected_list.py): the termbase, the 75
  zero-shot chapters + merged file, both keyword files, the 18 generators and the agents' 18 check scripts (+
  check_text_pe7.py), my7_formulas.py, regen_zeroshot.sh, my7-zeroshot-terms.md, notes-*.md, harmonise files,
  termbase/APPROVED.md, decisions-A.tsv, termbase-decisions.md, notes-part5.txt, map-harmonise-notes.md, the pi-1 …
  pi-6 termbases and final rails chapters. regen_rails.sh step 0 checks all of them.
- build_rails.py: the import chain (regen_zeroshot.sh header) is: sample <- my7_formulas; 1-01, 1-03-05 <- sample;
  2-01-02 <- 1-03-05; 2-03-06 <- 1-01 + 1-03-05; 2-07-11 <- 2-01-02; 2-12-17, 3-01-02 <- 2-03-06; 3-03-06, 3-07-08-10
  <- 3-01-02; 3-09 <- 3-03-06; 4-01 <- 3-07-08-10; 4-02-09 <- 2-07-11 + 2-12-17 + 3-03-06 + 3-07-08-10; 4-10-14 <- 3-09 +
  4-01 + 4-02-09; 4-15-21 <- 4-10-14; 5-01-04 <- 2-07-11 + 2-12-17 + 3-09 + 4-01; 5-05-12, 5-13-20 <- 5-01-04.
  my7_formulas / make_sample are imported by name (several generators pop them for fresh copies), the generators load
  each other by file path. Each generator runs in its own process (as regen_zeroshot.sh; 7 side by side); in it a
  meta-path finder serves my7_formulas / make_sample and importlib.util.spec_from_file_location is wrapped so that any
  pi-7-my/make_*.py loaded by path gets the PATCHED source: a patch reaches every downstream chapter at any depth and
  every fresh copy. Each patch must match its stated count in its file's source, and a patch that no run applies
  fails the build. `--plain DIR`: no patches, 75 of 75 files byte-identical to the zero-shot (checked every run).
  layer-log.tsv: every patch with its count, the number of loads (69 loads of my7_formulas …) and its reason.
- my_formulas_rails.py: the layer (PATCHES by file, reasons per family L01 … L10).
- apply_termbase.py + residual_rules.py → apply-log.tsv: 3 rules, 3 replacements (each in its segment, Pāli checked).
- adherence_my.py (pi-6's, unchanged logic); adherence-zeroshot.txt is the input (179700 checked, 1751 misses),
  reproduced each run. classify_misses.py (pi-6's logic) + classify_rules.py (rules built from the termbase itself:
  one per gerundive and per condition headword) → adherence-classified.tsv / classify-out.txt; rails_misses_check.py.
- line_scan.py → line-scan-zeroshot.txt (443 flags) / line-scan-rails.txt (0): 37 families (the rails changes as
  eq / forbid, the decided §A items and approved choices as req proofs), all with Pāli hits.
- termbase-proposals.tsv (2 rows), pi123456_identity.py (runs harmonise_pi123456.py on the rails folder),
  align_explained.py, check_text_pe_rails.py (copy of check_text_pe7.py writing its fold copies to rails/chk-pe, run
  one file at a time), diff_count.py → lines-changed.txt, output-md5.txt.
  Inspection helpers (not part of the checks): misses_view.py, seg.py, kwin.py, ctx.py, pair.py, pair2.py, yatha.py,
  explore.py, line_adh.py (line-level adherence, information only).

## Misses by class (adherence-classified.tsv; 1751 zero-shot rows, 0 rails-introduced)
| class | rows | what |
|---|---|---|
| GENUINE | 56 (53 id / keyword pairs) | fixed: avasesa 22 (L01), suciṇṇāni 14 (L03), tadārammaṇatā 3 + niruddhe 3 (L04), vibhajantena 1 (L05), pavattipaṭisandhi 2 (L07), uposathakammaṃ 6 + ekāgārikaṃ 5 (L09) |
| INFLECTION | 1691 | finite «…ရမည်» / negative «…ရမည် မဟုတ်» of the attributive gerundive terms «…ရမည့်» (vitthāretabba 607, kātabba 455, gaṇetabba 346, vibhajitabba 45, pahātabba 33, …: 1524); the condition frame form «Nဟူသော အကြောင်း» / «… အကြောင်း မဟုတ်ခြင်း» of the ablative terms in headings («Hetu-ārammaṇapaccayā») and notes («yathā ārammaṇapaccayā») (167) |
| ARTEFACT | 4 | katvā in «uposathakammaṃ katvā» «ဥပုသ်ကို စောင့်ထိန်း၍» (§A8: the act compound carries the verb; termbase proposal) |
| CONTEXT | 0 | |
| UNVERIFIED | 0 | |

Each INFLECTION rule is built from one termbase sense and checked on the segment (the verb + «ရမည်» not followed by
«့»; the bare name not followed by «ကြောင့်») and on its Pāli («tabb»; the keyword in a heading or in a «( … )» note);
a row that no rule verifies fails the run. The loose test cannot see L02, L06, L08, L10, R01 … R03 and the L09 cut
lists (the old form holds the term's chunks); line_scan proves them line by line.

## Layer (23 patches, families L01 … L10) and rules (3)
- L01 avasesa family «ကြွင်းကျန်…» (coordinator change before the lock; = pi-1 / pi-2 / pi-5 / pi-6; the substantive
  «ကြွင်းကျန်သည်တို့» = pi-6): «ကြွင်းသော / ကြွင်းသည်(တို့)» → «ကြွင်းကျန်…» in my7_formulas (1), make_ch1-01 (4),
  make_ch2-01-02 (3), make_ch2-12-17 (1), make_ch3-01-02 (5), make_ch3-07-08-10 (1): 30 of 30 Pāli avases- uses.
- L02 nānākaraṇa «ကွဲပြားမှု» (§A27 decided, locked pi-5, one noun for nānā(karaṇa)): «ကွဲပြားချက်» → «ကွဲပြားမှု» in
  make_ch1-01 NANAKARANA, make_ch1-03-05 NANAKARANA (+ 4 comments), and «(Nissayampi ninnānaṃ)» «ကွဲပြားခြင်း မရှိ» →
  «ကွဲပြားမှု မရှိ» (make_ch2-01-02): 93 + 1 uses (ninnānākaraṇaṃ / -ā, nānākaraṇaṃ, nānaṃ, ninnānaṃ). nānattaṃ
  «ကွဲပြားခြင်း» (^7-4-33, another word) and nānākkhaṇika «ခဏ ကွဲပြားသော» untouched.
- L03 §A15 suciṇṇāni «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှု(တို့)» (make_ch1-03-05): 21 uses (1-03 … 1-05, 2-01, 2-07, 2-08, 2-10).
- L04 §A16 tadārammaṇatā «ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့်» and §A35 niruddhe «ချုပ်ငြိမ်းသွားသောအခါ» (make_ch1-01 frame
  «niruddhe vipāko tadārammaṇatā uppajjati»): 6 + 6 uses (1-01, 2-05).
- L05 §A37 vibhajantena «ခွဲခြမ်းစိတ်ဖြာလျက်» (make_ch3-07-08-10): 1 use (3-10 ^7-U409).
- L06 §A14 ṭhānāṭhānakosallassa «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း» (make_ch1-03-05 KOSALLA): 6 uses.
- L07 §A19 pavatti «ဘဝ ဖြစ်စဉ်» (make_ch2-01-02 PAVATTI): 6 uses (2-01, 2-07).
- L08 nillopaṃ «လုယက်ပစ္စည်း» (termbase notes-part5 5g, = pi-5 rails): «ဥစ္စာကို လုယူ… / ဥစ္စာကို…» → «လုယက်ပစ္စည်းကို …»
  (my7_formulas deeds list, make_ch1-01 -tvā list; the cut list follows the module): 14 uses (1-01, 1-02, 2-02, 3-10, 4-01).
- L09 §A8 act compounds carry their verb, also cut by …pe…: uposathakammaṃ / uposathaṃ «ဥပုသ်…» → «ဥပုသ် စောင့်ထိန်းခြင်း…»
  (make_ch2-07-11; = the 63 other cut uses): 6 uses; the 6 cut deed lists of 3-10 / 4-01 (make_ch3-07-08-10):
  ekāgārikaṃ «အိမ်တစ်လုံးတည်းကို… » → «… ဝိုင်း၍ တိုက်…», gāmaghātaṃ «ရွာကို…» → «ရွာကို ဖျက်ဆီး၍ လုယက်…» (6 + 6).
- L10 §A18 / uppanna before its noun (make_ch1-03-05 lexicon, longest match first): «uppannaṃ samāpajjati / -anti»
  «ဖြစ်ပေါ်ပြီးသည်ကို ဝင်စား…» → «ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို ဝင်စား…» (5 uses: 1-03 ×3, 2-07, 2-10; = the majority 12 of
  17) and «uppannaṃ utuṃ upanissāya» «ဖြစ်ပေါ်ပြီးသည်ကို ရာသီဥတုကို» → «ဖြစ်ပေါ်ပြီးသော ရာသီဥတုကို» (4-02 ^7-36-477, = 2-12).
- R01 §A36 saññojanādidukāni «နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ» (4-17 heading ^7-4-3-3-12-4-0; = 5-02 / 5-08 …).
- R02 / R03 §A4 «yathā [W] X-sadisaṃ» one shape «… Xနှင့် တူသည့်အတိုင်း» (the majority 8 of 10): ^7-4-32 «Yathā anulomaṃ
  sahajātasadisaṃ» and ^7-35-169 «Yathā sappītike nahetupaccayasadisaṃ» («…ကဲ့သို့ … တူသည်» → «…၏ / …၌ … တူသည့်အတိုင်း»).

## Lines changed per chapter (non-empty lines)
1-01 11/2551, 1-02 3/385, 1-03 8/544, 1-04 3/485, 1-05 5/184, 2-01 13/732, 2-02 2/203, 2-03 1/380, 2-05 1/337, 2-07 9/385, 2-08 3/143, 2-10 4/255, 2-15 3/183, 2-16 1/99, 2-17 4/241, 3-01 5/805, 3-02 5/734, 3-03 2/533, 3-04 4/457, 3-05 4/431, 3-06 1/5, 3-07 6/407, 3-08 3/329, 3-09 28/1867, 3-10 8/433, 4-01 30/1714, 4-02 1/1808, 4-11 1/85, 4-17 1/137 — total 170 of 27749; the other chapters 0.

## §A items (mapper-my/map-harmonise-notes.md; termbase notes-part5 5e)
Decided by a term (23): fixed where the text differed — 4 -sadisa (R02 / R03; the adverbial «…နှင့် တူအောင်» and «-sadisā»
«တူကြသည်» stay, INFLECTION as decided), 8 act compounds (L09), 14 (L06), 15 (L03), 16 (L04), 19 (L07), 27 (L02), 35
(L04), 36 (R01), 37 (L05); already in the text (line_scan req proofs where a family fits) — 1 samanantarā, 2 paccavekkh-,
3 kusalākusalaṃ, 7 assādeti (the shared ending «သာယာ နှစ်သက်သည်» kept, the term's word is in it), 9 kātabbā two senses,
11 paṭicca / nissāya, 13 «-to … ဟု», 21 sekkha, 22 passitvā, 23 naviññeyyo, 24 rūpī / arūpī, 30 lokiya / kāmāvacara,
33 nevadassanena (one term; its two clause shapes belong to the two frames pahātabba / pahātabbahetuka).
Left for the rails step (15):
- 5 **kept** (Burmese needs a head noun; no keyword carries it): «ကံ» after the kamma labels, «စိတ်» after kiriya and the
  mind moments, «အမှု» after suciṇṇāni (now book-wide, L03), «ရုပ်» after -samuṭṭhāna, «ပြဿနာ» after paṭhamasseva,
  «အပိုင်း» after suddhake / arūpamissake, «ထိုအမှု» for tassa (paṭighātatthāya); «သဘောတရား» as the frame's noun.
- 6 **kept**: «သဘောတရား» inside the -sadisa / -mūla notes as the phase-3 coordinator set it (gap where possible).
- 10 **kept**: the list comma inside terms (abyākata and the stacked qualifiers «A၊ B N», harmonise H6, approved).
- 12 **kept as written**: the slips are translated as written; where only the spelling slipped the intended word's term
  already stands (vicākānaṃ, lokuttarasa, uppajanti, asakkho, sāsavoca, ovattā, nano ca …).
- 17 **kept**: tassa paṭighātatthāya is uniform «ထိုအမှုကို ချေဖျက်ရန်».
- 18 **fixed** (L10).
- 20 **kept**: the verb is not dropped: Burmese is verb-final, «ဖြစ်ပေါ်သည်» closes the sentence once (^7-9-19 …).
- 25 **kept**: arūpadukasadisā «ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲ» (the plane; for a Burmese speaker, doubt 4).
- 26 **kept**: ^7-35-204 and ^7-35-243 are different Pāli («suddhake arūpamissake ca» / «suddhike arūpe ca missake ca»).
- 28 **kept**: «ပယ်ရမည် မဟုတ်သော» is the termbase's negative of pahātabba (na-X), not a slip.
- 29 **kept**: keyword-file gaps, no text effect.
- 31 **kept**: «(dassane ekaṃ, nadassane dve)» spelled out (an evident ellipsis, harmonise H8).
- 32 **kept**: Anulomadukatikapaṭṭhānato split into the order and the quoted title (Burmese cannot keep one compound).
- 34 **kept as written**: «… အစု» for the singular -gocchakaṃ (^7-5-14-6-0), «… အစုများ» for -gocchakāni.
- 38 **kept**: «နတ်မျက်စိ / နတ်နား» joined = the pi-2 / pi-5 witnessed terms (the term «နတ်» is in it).

## Checks (regen_rails.sh, all pass)
- Protected files: 292 md5s unchanged; termbase sha256 = the lock (faef9155…).
- Reproduction: build without the layer = zero-shot, 75 of 75 files byte-identical.
- check_chapter_ids, check_text_pe7 (rails copy, one file at a time) and check_marks: all 75 files OK; typography OK.
- Adherence: zero-shot 1751 misses (input reproduced) → rails 1695, all known INFLECTION / ARTEFACT rows; GENUINE 56
  rows (53 id / keyword pairs) fixed, 0 left; 0 unverified.
- align_check_my: 1074 repeated Pāli sentences, 0 differing (zero-shot 0); align_hidden_my: 0 unmatched;
  align_explained: 0 unexplained.
- pi-1 … pi-6 identity: 12/12, 74/74, 2/2, 7230/7230, 6/6, 3/3 (as the zero-shot; none worse).
- line_scan: 0 lines left (zero-shot 443 flags; 37 of 37 families with Pāli hits).
- Rerun: a second regen_rails.sh run changes no byte (88 output files).

## Termbase proposals (rails/termbase-proposals.tsv; termbase not changed, the coordinator decides)
1. nillopaṃ «လုယက်» → «လုယက်ပစ္စည်း» (the object the rails write, = pi-5 rails; no text effect).
2. katvā gloss: in «uposathakammaṃ katvā» the act compound carries the verb «ဥပုသ်ကို စောင့်ထိန်း၍» (gloss only).

## Termbase doubts (termbase not changed)
1. **The act compounds cut by …pe…** (L09): the rails give the cut forms the term's verb without its ending
   («… ဝိုင်း၍ တိုက်…», «ရွာကို ဖျက်ဆီး၍ လုယက်…», «ဥပုသ် စောင့်ထိန်းခြင်း…»); the other members of the cut deed lists stay
   objects («အိမ်ကို…», «လုယက်ပစ္စည်းကို…», «လမ်းခရီး၌…», «သူတစ်ပါး၏ မယားထံ…»). A Burmese speaker may prefer all
   members with or all without their verbs.
2. **paripanthe** «လမ်း»: the text has «လမ်းခရီး၌ ဓားပြ တိုက်သည်» (contains the term; 5g allows it); pi-5 rails «လမ်း၌».
3. **nillopaṃ in the approved sample** (1-02, 3 lines) changes with L08 (5g directs it).
4. **arūpadukasadisā** (§A25) may name the arūpāvacara dyad «ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ» (kept as the text).
5. **The gerundive terms** are attributive «…ရမည့်» while the text uses them as the notes' verbs «…ရမည်» (1524 INFLECTION
   rows); a finite sense or a gloss «(finite in the notes)» would make the loose test see them.
